# 정보 및 시스템 제어 연구실 (Laboratory for information and Control Systems, LiCS)

**KAIST 항공우주공학과·안보과학기술대학원 · 최한림 교수**

- 분야: 다중 에이전트 추정과 제어, 불확실성 아래의 의사결정, 다수 무인기의 임무 할당과 경로 계획, 레이더 자원 할당, 위성 임무 계획, 학습 기반 항법과 제어
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 다중 로봇 협업·물류 자동화[^board][^p1], 제어 이론·제어 공학[^board][^p6], 강화학습[^p5], 로봇 항법·SLAM[^board][^p4], 다중 에이전트 시스템·분산 의사결정[^p2], 상태 추정·필터링(데이터 동화)[^p6], 드론·무인 항공기[^board], 궤도역학·우주 궤적 설계[^p3]
- 홈페이지: <http://lics.kaist.ac.kr/>
- 근거와 출처: [정보 및 시스템 제어 연구실 근거 페이지](lics-sources.md)

> 여러 대의 무인기·위성 같은 항공우주 시스템이 정보를 추정하고 서로 일을 나누어 임무를 계획하도록 하는 추정·제어·의사결정 방법을 연구하는 연구실이다.[^board][^prof]

## 무엇을 연구하나

학과 연구실 소개는 정보 및 시스템 제어 연구실(LiCS)을 항공우주 시스템에서의 정보 추론과 제어를 연구하는 연구실로 소개한다. 연구실은 멀티 무인기 코디네이션(여러 대의 무인기가 일을 나누고 움직임을 맞추는 일), 레이더 자원 할당(한 장비로 탐색·추적 같은 여러 기능을 하는 다기능 레이더의 시간과 에너지를 여러 임무에 나누어 주는 일), 학습 기반 무인기 경로 계획과 제어, 위성 임무 계획 같은 여러 분야의 기술을 항공우주 시스템에 접목한다고 적는다.[^board]

연구실 누리집의 교수 소개는 연구분야를 센서 네트워크를 위한 추정과 제어(Estimation and Control for Sensor Networks), 다중 에이전트 시스템(여러 자율적 주체, 곧 에이전트가 서로 영향을 주고받는 시스템)을 위한 의사결정(Decision Making for Multi-Agent Systems)으로 적는다.[^prof] 학과 연구실 소개는 연구분야를 다중 에이전트 추정 및 제어, 불확실성하의 의사결정, 무인기 임무계획 및 자원할당으로 적는다.[^board] 안보과학기술대학원 교수 명단은 교수의 연구분야를 인공지능/무인체계로, 세부 연구 분야를 군집시스템, 자율화, 자원관리, AI응용으로 적는다.[^gst]

대표 논문으로 보면, 여러 종류의 무인기가 시간 제약을 지키며 일을 나누어 맡는 임무 할당 알고리즘을 만들었고,[^p1] 중앙 서버 없이 이웃끼리만 통신하는 다중 에이전트 망에서 무리별 정보를 모으는 합의 기반 알고리즘을 제안했다.[^p2] 궤도에서 예측하기 어렵게 기동하는 대상을 추력이 제한된 우주선으로 따라가는 궤도 전이 기법을 개발했고,[^p3] 좁은 실내에서 지상 로봇이 2차원 라이다(레이저를 쏘아 주변 물체까지의 거리를 재는 센서)로 길을 찾도록 학습한 항법 시스템을 만들었다.[^p4] 강화학습 정책이 처음 보는 환경에서도 통하도록 하는 학습 방법,[^p5] 센서와 구동기의 고장을 함께 찾아내는 관측기(시스템의 입력과 측정값으로 직접 재지 않는 내부 상태를 추정하는 계산 방법),[^p6] 항공기 궤적 자료의 표현을 정답 표시 없이 학습하는 틀,[^p7] 항공기 운동처럼 여러 모드가 섞인 동역학을 자료로 배우는 시스템 식별 방법도 내놓았다.[^p8]

구성원 소개에 적힌 연구 관심사에는 다중 에이전트 경로 탐색과 계획, 위성 스케줄링, 우주선 의사결정과 운동 계획, 최적 제어, 강화학습, 베이즈 추론과 분산 자료 융합, 무인기 하드웨어와 유도·항법·제어, 설명 가능한 인공지능이 있다.[^members]

## 주요 연구 주제

### 1. 다중 에이전트 임무 할당과 분산 협업

학과 연구실 소개가 첫 분야로 드는 멀티 무인기 코디네이션의 갈래다.[^board] 대표 논문 1은 여러 종류의 무인기가 함께 임무를 수행할 때 전체 임무를 마치는 시각을 줄이도록 일을 나누는 재균형 알고리즘을 제안했고,[^p1] 대표 논문 2는 무리로 나뉜 분산 통신망에서 합의 방법으로 무리별 개수와 합을 모으는 알고리즘을 제안했다.[^p2] 논문 목록에는 여러 기지에서 출발하는 이종 차량 경로 문제를 메시지 전달 방식으로 푸는 사전 공개본, 격자 지도를 바탕으로 다수 무인 이동체의 임무를 할당하고 경로를 계획하는 논문, 군집 로봇의 협업 지도 작성을 위한 탐사·임무 할당 논문도 있다.[^journal]

### 2. 위성 임무 계획과 우주 궤도 임무

학과 연구실 소개가 드는 위성 임무 계획의 갈래다.[^board] 논문 목록에는 중계 위성을 거쳐 자료를 내려받는 지구 관측 위성 스케줄링 논문과 ChatGPT를 이용한 지구 관측 위성 임무 스케줄링 논문이 있고,[^journal] 학회 논문 목록에는 위성 군집의 관측·중계·자료 전송 스케줄링을 혼합 정수 선형 계획법(일부 변수가 정수 값만 가질 수 있는 선형 최적화 문제의 풀이 틀)으로 다룬 논문들이 있다.[^conf] 대표 논문 3은 궤도에서 기동하는 대상을 따라가는 우주선의 궤도 전이 기법을 다룬다.[^p3]

### 3. 학습 기반 항법과 제어

학과 연구실 소개가 드는 학습 기반 무인기 경로 계획과 제어의 갈래다.[^board] 대표 논문 4는 최적화 기반 기준 항법 알고리즘을 신경망이 따라 배우게 해 좁고 복잡한 실내에서 지상 로봇이 빠르게 길을 찾도록 했다.[^p4] 대표 논문 5는 강화학습(시행착오로 보상을 최대로 하는 행동을 배우는 기계학습 방법) 정책을 뜻이 같은 다른 환경으로 옮기는 학습 방법을 다룬다.[^p5] 논문 목록에는 로봇 자율성에 대규모 사전 학습 모델(파운데이션 모델)을 쓰는 연구를 정리한 총설과, 도메인 추상화를 이용해 여러 영역의 계획 문제를 학습하는 논문도 있다.[^journal]

### 4. 추정·고장 진단과 궤적 표현 학습

교수 소개가 연구분야로 드는 추정의 갈래다.[^prof][^deptlist] 대표 논문 6은 센서와 구동기의 고장을 함께 찾아내고 구별하는 다중 모드 신경망 적응 관측기를 제안하고 쿼드콥터 무인기 사례로 확인했다.[^p6] 대표 논문 7은 항공기 궤적 자료의 표현을 자기 지도 학습(정답 표시 없이 자료 자체에서 학습 목표를 만드는 학습 방식)으로 배우는 틀을, 대표 논문 8은 가우시안 과정(함수의 값들을 결합 정규 분포를 따르는 확률 변수로 보아 예측값과 그 불확실성을 함께 내는 통계 모형)을 여러 개 써서 여러 모드가 섞인 동역학을 배우는 시스템 식별 방법을 제안했다.[^p7][^p8] 학회 논문 목록에는 신뢰도 변수와 혼합 모형을 써서 일부 정보원이 잘못돼도 버티는 베이즈 분산 자료 융합 논문도 있다.[^conf]

## 응용 분야

학과 연구실 소개는 연구실의 기술을 무인기, 다기능 레이더, 위성 같은 항공우주 시스템에 접목한다고 적는다.[^board] 대표 논문은 다수 무인기의 임무 할당,[^p1] 우주선의 궤도 전이,[^p3] 실내 지상 로봇의 항법,[^p4] 쿼드콥터 무인기의 고장 진단,[^p6] 항공 교통 관리를 위한 궤적 분석과 추적을 다룬다.[^p7][^p8] 안보과학기술대학원 교수 명단은 연구분야를 인공지능/무인체계로 분류하고,[^gst] 논문 목록에는 유도탄 유도, 무기-표적 할당, 전투 체계의 임무 할당처럼 국방 분야에 응용한 논문도 있다.[^journal][^conf]

## 대표 논문

랩 PUBLICATIONS 목록의 2021–2026년 학술지 논문 가운데 연구 갈래마다 고르게, 교수가 저자이고 초록을 확인할 수 있는 논문 8편을 골랐다. 여덟 편 모두 교수가 마지막 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^journal] |
|---|---|---|---|---|
| 1 | 2023 | [Makespan-Minimizing Heterogeneous Task Allocation under Temporal Constraints](https://doi.org/10.3390/aerospace10121032) · Aerospace | 여러 종류의 무인기로 이루어진 시스템이 여러 임무를 해내려면 임무 할당이 핵심이다. 이 논문은 이종 다수 무인기가 임무를 수행할 경로를 만드는 「재균형 알고리즘」을 제안했다. 상황이 바뀌는 환경에서 해를 빨리 찾도록 탐욕적 휴리스틱(매 단계에서 당장 가장 나아 보이는 선택을 고르는 근사 풀이 방법)을 쓰고, 시간 제약을 지키도록 「배회」라는 변수를 새로 넣었다. 알고리즘은 마지막 임무가 끝나는 시각(makespan)을 줄이도록 처음 할당과 재할당의 두 단계로 나뉜다. 모의실험에서 제약이 많은 조건에서도 효과가 있었고, 순차 탐욕 알고리즘, 유전 알고리즘, 담금질 기법에 견주어 계산 시간이 줄고 성능이 나아졌다.[^p1] | 1저자 B.-M. Jeong, 마지막 저자 최한림 (6명) |
| 2 | 2023 | [Consensus-based clustering and data aggregation in decentralized network of multi-agent systems](https://doi.org/10.7717/peerj-cs.1445) · PeerJ Computer Science | 다중 에이전트 시스템은 많은 에이전트와 서로 다르게 연결된 망을 다룰 수 있는 최적화 알고리즘이 필요하다. 무리로 나뉜 환경에서 중앙 없이 통신하며 계획하려면 다른 무리에서 오는 잡음을 걸러 무리 정보를 정확히 알아야 한다. 이 논문은 합의 방법(이웃끼리 값을 주고받으며 모두가 같은 값으로 모이게 하는 분산 계산)으로 무리 안의 개수(COUNT)와 합(SUM)을 모으는 분산 자료 집계 알고리즘을 제안했다. 무리 단위로 정확히 모으도록 신뢰 값을 넣었고, 보정 변수로 정확도와 계산 시간을 조절한다. 크고 성긴 망, 좁은 통신 대역 조건의 모의실험에서 집계값이 적당한 정확도와 시간 안에 수렴했다. 연구진은 이 도구가 이종 다중 에이전트·다중 임무 환경의 분산 임무 할당 알고리즘 개발에 쓰일 것으로 본다.[^p2] | 1저자 J. J. Damanik, 마지막 저자 최한림 (5명) |
| 3 | 2024 | [Receding Horizon Lambert Transfer for Thrust-Limited Non-Cooperative Space Missions](https://doi.org/10.2514/1.a36123) · Journal of Spacecraft and Rockets | 궤도에서 상대가 협조하지 않고 기동하는 임무는 쫓는 쪽 우주선이 기동하는 대상을 따라잡으려는 추격-회피 문제로 다뤄진다. 두 번의 순간 추력으로 궤도를 옮기는 기존 램버트 해(두 위치와 그 사이 비행 시간이 주어질 때 두 위치를 잇는 궤도를 구하는 풀이)는 예측할 수 없게 기동하는 대상을 따라가기에 맞지 않는다. 이 논문은 순간이 아닌 연속 추력으로 대상을 적응적으로 따라가는 이동 지평 램버트 전이 기법을 내놓았다. 이 기법과 추가 유도 전략을 Kerbal Space Program 기반 미분 게임 대회에서 구현해 시험했고, 여러 시나리오의 임무를 마쳐 대회 1위를 했다.[^p3] | 1저자 S. J. Kim, 마지막 저자 최한림 (3명) |
| 4 | 2024 | [LiCS: Navigation Using Learned-Imitation on Cluttered Space](https://doi.org/10.1109/lra.2024.3518078) · IEEE Robotics and Automation Letters | 좁은 실내 환경에서 무인 지상 차량이 2차원 라이다로 빠르고 안정적으로 길을 찾는 항법 시스템 LiCS를 제안했다. 트랜스포머 신경망에 행동 복제(전문가가 보인 상태별 행동을 지도 학습으로 따라 배우는 모방 학습 방법)를 써서 최적화 기반 기준 알고리즘을 배우게 했고, 학습한 정책이 흔들리지 않도록 시범을 보일 때 가우시안 잡음을 넣었다. 모의실험과 실제 하드웨어 실험으로 평가했다. 장애물이 매우 많은 모의 환경에서 항법 성공률 100%로 다른 기준 방법들을 모두 앞섰고, 하드웨어 실험에서는 최대 1.5 m/s 속도로 안전하게 이동했다.[^p4] | 1저자 J. J. Damanik, 마지막 저자 최한림 (4명) |
| 5 | 2025 | [Enhancing generalization in reinforcement learning for robotic control through deep policy similarities](https://doi.org/10.1177/17298806251332359) · International Journal of Advanced Robotic Systems | 로봇 제어용 강화학습이 처음 보는 환경에서도 통하도록 하는 학습 기반 바이시뮬레이션 방법 DeePS(Deep Policy Similarities)를 제안했다. 바이시뮬레이션(두 상태에서 받는 보상과 이어지는 상태 변화가 같으면 두 상태를 같은 것으로 보는 관계)을 보상 기준으로 재는 기존 방식은 보상 구조가 일정하지 않은 환경에서 정책을 옮기기 어렵다. DeePS는 정책의 유사성을 쓰고, 그 유사도 척도를 순방향 동역학 모델로 근사해 뜻이 같은 환경들 사이에 정책을 옮긴다. 보상을 무작위로 바꾼 잡음 섞인 카트폴 환경에서 시험 보상이 Soft Actor-Critic보다 53.5%, Deep Bisimulation for Control(DBC)보다 79.0% 높았다. Minigrid 단순 건너기 환경의 제로샷 평가에서는 DBC보다 79.9%, RAPID보다 99.5% 높았다.[^p5] | 1저자 M. C. Lim, 마지막 저자 최한림 (2명) |
| 6 | 2025 | [Multi-modal Neural Adaptive Observer for Sensor and Actuator Fault Detection and Identification](https://doi.org/10.1007/s42405-024-00823-4) · International Journal of Aeronautical and Space Sciences | 센서 고장과 구동기 고장은 서로 얽혀 나타나, 어느 쪽 고장인지 가려내기 어렵고 잘못된 경보가 많아진다. 이 논문은 신경망 적응 관측기(신경망으로 모르는 동역학을 보완하며 상태를 추정하는 관측기)를 다중 모드로 넓혀 이 얽힘을 줄였다. 서로 다른 고장 모드를 나타내는 관측기 여러 개를 두고, 관측기의 안정성과 고장 식별 가능성을 함께 고려해 각 모드의 사후 확률을 갱신하는 규칙을 만들었다. 각 관측기가 더 빨리 수렴하도록 하는 방식도 고안했고, 리아푸노프 안정성 분석(상태에 따라 값이 정해지는 양의 함수가 시간에 따라 줄어드는지로 시스템의 안정성을 판정하는 방법)을 했다. 쿼드콥터 무인기의 고장 탐지·식별 사례에서 고장 식별 능력과 안정성이 뛰어났다.[^p6] | 1저자 W.-C. Lee, 마지막 저자 최한림 (3명) |
| 7 | 2025 | [Aircraft Trajectory Segmentation-based Contrastive Coding: A Framework for Self-supervised Trajectory Representation](https://doi.org/10.1109/ojits.2025.3574746) · IEEE Open Journal of Intelligent Transportation Systems | 항공 교통 관리에서는 궤적을 분류하고 묶는 일이 기본 과제다. 이 논문은 항공 교통 궤적 자료의 뜻을 담은 표현을 배우는 자기 지도 시계열 표현 학습 틀 ATSCC를 내놓았다. 궤적을 구간으로 나눌 수 있다는 성질을 이용하고, 스스로 정한 구간 안에서 표현이 일관되도록 했다. 세 공항의 자료 네 묶음으로 실험해, 학습한 표현으로 분류와 군집을 했을 때 다른 최신 표현 학습 기법보다 성능이 좋았고, 표현이 항공기의 기동 절차와 맞아떨어졌다. 공항 구성이 달라도 쓸 수 있고 끊긴 궤적에도 적용되며, 공항 구성·기동 절차·정답 표시 같은 사전 입력 없이 이런 성능을 냈다. 궤적 자료와 구현 코드는 공개됐다.[^p7] | 1저자 T. Phisannupawong, 마지막 저자 최한림 (3명) |
| 8 | 2021 | [Bayesian nonparametric state-space model for system identification with distinguishable multimodal dynamics](https://doi.org/10.2514/1.i010891) · Journal of Aerospace Information Systems | 시스템 식별은 시계열 자료 뒤에 있는 물리 동역학을 배우는 일이다. 가우시안 과정 상태공간 모델은 예측의 불확실성까지 낼 수 있지만, 가우시안 전이 모델에 기대므로 항공기 운동처럼 더 복잡한 전이를 나타내기 어렵다. 이 논문은 여러 개의 가우시안 과정 전이 모델로 여러 모드가 섞인 동역학을 나타내는 틀을 제안하고, 상호 정보량(두 변수가 서로에 대해 알려 주는 정보의 양) 정칙화를 더해 서로 구별되고 해석 가능한 여러 동역학 모델을 배우는 InfoSSM으로 넓혔다. 단순한 듀빈스 차량(일정한 속도로 앞으로만 움직이며 최소 회전 반경이 정해진 차량 모형)과 고충실도 비행 모의기의 두 수치 실험으로 성능과 해석 가능성을 보였고, 베이즈 필터링과 함께 항공 교통 관제의 추적에 쓰는 예도 들었다.[^p8] | 1저자 Y.-J. Park, 마지막 저자 최한림 (3명) |

## 교수와 전문 분야

최한림 교수는 KAIST 항공우주공학과에서 학사(2000년)와 석사(2002년)를, MIT 항공우주학과(Aeronautics and Astronautics)에서 박사(2009년)를 받았고, MIT 항공우주학과에서 박사후연구원을 지냈다.[^prof][^deptlist] 학과 교수진 목록과 누리집 교수 소개는 직위를 교수(Professor)로 적는다.[^deptlist][^prof] 학과 교수진 목록은 연구분야를 다중 에이전트 추정과 제어(Multi Agent Estimation and Control), 로봇 센서 네트워크(Robotic Sensor Networks), 불확실성 아래의 의사결정(Decision Making under Uncertainty)으로 적는다.[^deptlist] 안보과학기술대학원 교수 명단에도 소속학과 항공우주공학과, 연구실 Information & Control Systems Lab.으로 실려 있다.[^gst]

랩 논문 목록의 2021–2026년 항목을 제목으로 보면, 다수 무인기의 임무 할당과 경로 계획, 지구 관측 위성의 스케줄링, 우주선의 궤도 전이와 궤적 최적화, 학습 기반 로봇 항법과 강화학습, 고장 탐지와 시스템 식별, 항공 교통 궤적 분석, 스크램제트 엔진 비행체의 궤적 최적화, 유도 기법을 다룬다.[^journal][^conf]

## 구성원

2026년 10월 23일 랩 PEOPLE 메뉴 Current Members 페이지 기준이다. 박사후연구원 2명, 박사과정(Ph.D. Candidates) 13명, 석사과정(M.S. Candidates) 9명, 파트타임 박사과정(Part-time Ph.D.) 2명이다. 연구 주제 칸은 카드의 Research Areas·Research Interests 표기이고, 파트타임 박사과정의 괄호는 카드의 Work Experience에 적힌 소속 기관이다. 대표 논문 참여 칸은 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Byeongmin Jeong | 박사후연구원 | Multi-Agent Systems, Machine Learning | bmjeong@lics.kaist.ac.kr | 1 |
| Jaeho Lee | 박사후연구원 | Multi-Agent Path Finding, Multi-Agent Path Planning, Vehicle routing problem, Terrain-referenced navigation | jhlee@lics.kaist.ac.kr |  |
| Minkyu Shin | 박사과정 | Optimal Control, Optimal Design, Artificial Intelligence | mkshin@lics.kaist.ac.kr |  |
| Sujeong Park | 박사과정 | Decision Making, Artificial Intelligence | sjpark@lics.kaist.ac.kr |  |
| Changkyo Shin | 박사과정 | Bayesian Inference, Decentralized Data Fusion | ckshin@lics.kaist.ac.kr |  |
| Yunseo Oh | 박사과정 | Multi-Agent Systems, Tactical Swarm UAV | ysoh@lics.kaist.ac.kr | 1 |
| Chaehyeon Kim | 박사과정 | Multi-Agent Systems, Machine Learning, Optimal Control | chkim@lics.kaist.ac.kr |  |
| Minji Hong | 박사과정 | Multi-Agent Path Finding (MAPF), Neuro-symbolic AI | mjhong@lics.kaist.ac.kr |  |
| Haneul Lee | 박사과정 | Image Processing-based Artificial Intelligence, eXplainable Artificial Intelligence (XAI) | sky.lee@kaist.ac.kr |  |
| Thaweerath Phisannupawong | 박사과정 | Space Situations Awareness, Artificial Intelligence | petch@lics.kaist.ac.kr | 7 |
| Minchae Kim | 박사과정 | Spacecraft Decision Making | mckim@lics.kaist.ac.kr | 3 |
| Heeyeon Kim | 박사과정 | Optimal Control, Reinforcement Learning, Multi-Agent Systems | hykim00@lics.kaist.ac.kr |  |
| Donghwan Kim | 박사과정 | Multi-Agent Systems, Optimal Control | dhkim@lics.kaist.ac.kr |  |
| Jinhyeok Park | 박사과정 | UAV Hardware, UAV GNC, Reinforcement Learning | jhpark@lics.kaist.ac.kr |  |
| Dong-Woo Han | 박사과정 | Optimal control, Astrodynamics, Multi-Agent Path Planning | dongwoo.han@kaist.ac.kr |  |
| Jindeok Park | 석사과정 | Multi-Agent Systems, Satellite Scheduling | jdpark@lics.kaist.ac.kr |  |
| Kyeongmin Lee | 석사과정 | Machine Learning, Reinforcement Learning, Spacecraft Autonomous Control | rudals0n@kaist.ac.kr |  |
| Seunghyeon Yang | 석사과정 | Optimal control, Sequential Convex Programming | shyang@lics.kaist.ac.kr |  |
| Wajih Imliki | 석사과정 | Aerial Robotics, Autonomous Systems, Data Analysis | wajih.imliki@kaist.ac.kr |  |
| Wooju Ko | 석사과정 | Multi-Agent Systems, Satellite Scheduling | wjko@lics.kaist.ac.kr |  |
| Taeoh Kim | 석사과정 | Artificial Intelligence, Uncertainty Estimation | tokim@lics.kaist.ac.kr |  |
| Yongju Jung | 석사과정 | Perception, Planning, and Control for UAVs, Learning-based Autonomy for Robotics, Multi-Agent Systems & Swarm Intelligence | yjjung@lics.kaist.ac.kr |  |
| Minseong Ryu | 석사과정 | Artificial Intelligence, Multi-Agent Systems, Decision Making | msryu@lics.kaist.ac.kr |  |
| Hojun Kim | 석사과정 | Spacecraft Motion Planning, Fast Adaptation | hjkim@lics.kaist.ac.kr |  |
| Eun-Mi Oh | 박사과정 (파트타임, Korea Aerospace Research Institute) | Model-/data-based trajectory prediction, Decision support tool for air traffic management | emoh@lics.kaist.ac.kr |  |
| Sanghwan Seol | 박사과정 (파트타임, Agency for Defense Development) | Missile guidance and control, Multi-Target tracking | shseol@lics.kaist.ac.kr |  |

## 최근 논문 목록 (2021–2026)

랩 PUBLICATIONS 메뉴의 Journal 목록(International·Domestic)과 Conference 목록(International) 가운데 2021–2026년 항목 45편이다. 국제 학술지 17편, 국내 학술지 12편, 국제 학회 논문 16편이며, 각 줄은 랩 표기 그대로이고 끝의 대괄호에 목록 구분을 붙였다. 연도는 각 줄에 적힌 연도로 묶었고, 연도가 적히지 않은 학회 항목 1편은 「연도 표기 없음」에 두었다. 2025년 국제 학술지 가운데 "Available at SSRN 5062181 (2025)"로 적힌 항목은 학술지 게재본이 아니라 SSRN에 올린 사전 공개본이다. Conference 목록의 Domestic 칸에는 항목이 없다.[^journal][^conf]

**2025**

- Kim, S. J., Kim, M., Kim, C. H., & Choi, H. L. (2025). Integrated Earth Observation Satellite Scheduling with Relay-Assisted Downlink. Aerospace Science and Technology, 110864. [국제 학술지]
- Jeong, Byeong-Min, Dae-Sung Jang, and Han-Lim Choi. “Decentralized message passing algorithm for heterogeneous multi-depot vehicle routing problems.” Available at SSRN 5062181 (2025). [국제 학술지]
- Phisannupawong, Thaweerath, Joshua J. Damanik, and Han-Lim Choi. “Aircraft Trajectory Segmentation-based Contrastive Coding: A Framework for Self-supervised Trajectory Representation.” IEEE Open Journal of Intelligent Transportation Systems (2025). [국제 학술지]
- Lee, Woo-Cheol, Kyuman Lee, and Han-Lim Choi. “Multi-modal Neural Adaptive Observer for Sensor and Actuator Fault Detection and Identification.” International Journal of Aeronautical and Space Sciences 26.3 (2025): 1146-1157. [국제 학술지]
- Lim, Ming Chong, and Han-Lim Choi. “Enhancing generalization in reinforcement learning for robotic control through deep policy similarities.” International Journal of Advanced Robotic Systems 22.2 (2025): 17298806251332359. [국제 학술지]
- 김성준, 김민채, 최한림. (2025). ChatGPT 기반 지구 관측 위성 임무 스케줄링. 제어로봇시스템학회 논문지, 31(5), 510-516. 10.5302/J.ICROS.2025.25.0007 [국내 학술지]
- 신창교, 정병민, 서덕현, 심성준, 김주영, 최한림. (2025). 군집 로봇의 협업 지도 작성을 위한 경계 기반 탐사 및 임무 할당 알고리즘. 한국군사과학기술학회지 , 28(2), 217-223. https://doi.org/10.9766/kimst.2025.28.2.217 [국내 학술지]
- Roh, Daegyeong, et al. “Adaptive Initial Condition Search for Projectile Motion Simulations with Locally Sparse Terminal Conditions.” AIAA AVIATION FORUM AND ASCEND 2025. 2025. [국제 학회]
- Ryu, SeungKeol, et al. “Wind Aware Batch Informed Trees for Path Planning of Small UAS to Minimize Travel Time.” AIAA AVIATION FORUM AND ASCEND 2025. 2025. [국제 학회]
- Kim, SeongMin, et al. “Missile Trajectory Prediction Under Diverse Error Conditions Using Hypernetwork-Based Continual Learning.” AIAA AVIATION FORUM AND ASCEND 2025. 2025. [국제 학회]
- Han, Dong-Woo, et al. “Satellite Constellation Design Method for Long-Term Simulations Using Spherical Nearest Neighbor Index.” AIAA AVIATION FORUM AND ASCEND 2025. 2025. [국제 학회]
- Kim, Minchae, et al. “On Space Asset Protection Against Non-Cooperative Pursuer Using Guard Satellite.” AIAA SCITECH 2025 Forum. 2025. [국제 학회]
- Kim, Sung Jun, et al. “Satellite Scheduling Framework of Observation-Relay-Downlink With a Mixed-Integer Linear Programming Model.” AIAA SCITECH 2025 Forum. 2025. [국제 학회]

**2024**

- Jang, Dae-Sung, et al. “Unlocking robotic autonomy: A survey on the applications of foundation models.” International Journal of Control, Automation and Systems 22.8 (2024): 2341-2384. [국제 학술지]
- Damanik, Joshua Julian, et al. “Lics: Navigation using learned-imitation on cluttered space.” IEEE Robotics and Automation Letters (2024). [국제 학술지]
- Son, Jiwon, et al. “Refined mode classification and performance analysis method of dual-mode scramjet vehicles for flight trajectory optimization.” Aerospace Science and Technology 152 (2024): 109366. [국제 학술지]
- Kim, Sung Jun, Minchae Kim, and Han-Lim Choi. “Receding Horizon Lambert Transfer for Thrust-Limited Non-Cooperative Space Missions.” Journal of Spacecraft and Rockets (2024): 1-13. [국제 학술지]
- 고효상, 손지원, 이관중, 최한림. (2024). 이중모드 스크램제트 엔진 비행체의 등-동압 상승 시 요구 연료량 계산을 통한 최적 궤적 분석. 한국항공우주학회지, 52(8), 655-664. 10.5139/JKSAS.2024.52.8.655 [국내 학술지]
- 정병민, 장대성, 황남웅, 김준원, 최한림. (2024). 격자 지도 기반의 다수 무인 이동체 임무 할당 및 경로 계획. 항공우주시스템공학회지, 18(2), 56-63. [국내 학술지]
- 고효상, 이단일, 이명화, 최한림. (2024). 협업 유도탄 간 상대 충돌 각 제어 임무에서 통신 구조에 따른 유도기법의 영향 분석. 항공우주시스템공학회지, 18(2), 1-11. [국내 학술지]
- Kim, Chae-Hyeon, Sung Jun Kim, and Han-Lim Choi. “Heterogeneous satellite task scheduling with revisit time minimization using milp formulation.” AIAA SCITECH 2024 Forum. 2024. [국제 학회]
- Kim, Chae-Hyeon, Sung Jun Kim, and Han-Lim Choi. “Optimal Integrated Scheduling of Observation and Download Tasks for Multiple Satellites with Memory Constraints.” 2024 IEEE 20th International Conference on Automation Science and Engineering (CASE). IEEE, 2024. [국제 학회]
- Kim, Sung Jun, Chae-Hyeon Kim, and Han-Lim Choi. “Observation task scheduling of satellite constellation with consensus-based task pruning.” AIAA SCITECH 2024 Forum. 2024. [국제 학회]
- Kim, Sung Jun, et al. “Optimal Surveillance Scheduling for Multiple SAR-EO Satellite Train Constellation.” AIAA AVIATION FORUM AND ASCEND 2024. 2024. [국제 학회]
- Son, Jiwon, et al. “Trajectory Optimization of Dual Mode Scramjet Engine Vehicle Using a Refined Quasi One-Dimensional Combustion Model.” AIAA AVIATION FORUM AND ASCEND 2024. 2024. [국제 학회]
- Shin, Changkyo, et al. “Fault-tolerant Bayesian Decentralized Data Fusion Using Reliability Variables and Mixture Models.” 2024 27th International Conference on Information Fusion (FUSION). IEEE, 2024. [국제 학회]
- Lee, Jong-Won, Yun-Seo Oh, and Han-Lim Choi. “Heterogeneous UAV Task Allocation Using Shapley Value-Based Clustering.” 2024 24th International Conference on Control, Automation and Systems (ICCAS). IEEE, 2024. [국제 학회]
- Kim, Heeyeon, et al. “GNN-based task assignment in combat system.” Asia Pacific International Symposium On Aerospace Technology (APISAT 2024). Adelaide, South Australia: Engineers Australia, 2024. [국제 학회]
- Hong, Minji, et al. “LLM-based prompt for group selection in combat system unexpected situation management.” Asia Pacific International Symposium On Aerospace Technology (APISAT 2024). Adelaide, South Australia: Engineers Australia, 2024. [국제 학회]

**2023**

- Park, Hyeon-Woo, and Han-Lim Choi. “Weapon-target assignment and firing scheduling for rapid engagement with heterogeneous interceptors.” International Journal of Aeronautical and Space Sciences 24.3 (2023): 890-904. [국제 학술지]
- Damanik, Joshua Julian, et al. “Consensus-based clustering and data aggregation in decentralized network of multi-agent systems.” PeerJ Computer Science 9 (2023): e1445. [국제 학술지]
- Jeong, Byeong-Min, et al. “Makespan-Minimizing Heterogeneous Task Allocation under Temporal Constraints.” Aerospace 10.12 (2023): 1032. [국제 학술지]
- 고효상, 이명화, 최한림. (2023). 고속표적의 정보 오차를 고려한 Capture Region 기반의 최적 종말 교전 기하 분석. 제어로봇시스템학회 논문지, 29(8), 572-583. 10.5302/J.ICROS.2023.23.0053 [국내 학술지]
- 정병민, 장대성, 황남웅, 김준원, 최한림. (2023). 시간 제한 조건을 고려한 유전 알고리즘 기반 다수 무인기 임무계획기법. 항공우주시스템공학회지, 17(2), 78-85. [국내 학술지]

**2022**

- Cho, Sung-Bong, and Han-Lim Choi. “A convex programming-based approach to trajectory optimization for survivability enhancement of homing missiles.” International Journal of Aeronautical and Space Sciences 23.5 (2022): 992-1008. [국제 학술지]
- 고효상, 최한림, 장종윤, 김준, 유구현. (2022). 순차 컨벡스 프로그래밍 기반 무인기 설계 형상의 성능 분석. 한국항공우주학회지, 50(11), 771-781. 10.5139/JKSAS.2022.50.11.771 [국내 학술지]
- 최한림. (2022, 2). 인공지능 기반 유도제어 연구의 흐름. 항공우주매거진, 16(1), 40-52. [국내 학술지]

**2021**

- Ha, Jung-Su, Hyeok-Joo Chae, and Han-Lim Choi. “A diffusion wavelets-based multiscale framework for inverse optimal control of stochastic systems.” International Journal of Systems Science 52.11 (2021): 2228-2240. [국제 학술지]
- Chae, Hyeok-Joo, and Han-Lim Choi. “Domain-abstraction-based approach for learning multidomain planning.” Journal of Aerospace Information Systems 18.11 (2021): 790-802. [국제 학술지]
- Park, Young-Jin, Soon-Seo Park, and Han-Lim Choi. “Bayesian nonparametric state-space model for system identification with distinguishable multimodal dynamics.” Journal of Aerospace Information Systems 18.3 (2021): 116-131. [국제 학술지]
- Kim, Iksoo, Han-Lim Choi, and In-Soo Jeon. “Closed-form impact-angle-control guidance of nose-dive missiles for maximum terminal speed.” International Journal of Aeronautical and Space Sciences 22.6 (2021): 1428-1439. [국제 학술지]
- 윤다인, 김영원, 이창훈, 최한림, 유혁. (2021). 한국형 우주비행기의 기준 항력 추종 기반 재진입 유도 기법. 한국항공우주학회지, 49(8), 637-648. 10.5139/JKSAS.2021.49.8.637 [국내 학술지]
- 김도운, 이우철, 최한림, 박준태, 박준현, 서정직. (2021). 전투기탑재 다기능 레이다의 공대공 및 공대지 동시 운용 모드를 위한 스케줄링 기법. 한국항공우주학회지, 49(7), 581-588. 10.5139/JKSAS.2021.49.7.581 [국내 학술지]
- 고효상, 양재훈, 여재익, 최한림. (2021). 스크램제트 추진 시스템의 비행 제어를 통한 연소기의 추력 분석. 한국추진공학회지, 25(1), 29-41. 10.6108/KSPE.2021.25.1.029 [국내 학술지]

**연도 표기 없음**

- Damanik, Joshua Julian, and Han-Lim Choi. “Contrastive Learning-Based Air Traffic Trajectory Representation: A Case Study on Incheon International Airport.” [국제 학회]

## 연락과 위치

- 연구실: 34141 대전광역시 유성구 대학로 291 KAIST 항공우주공학과, 교수실 N7-5동 302호[^board][^deptlist]
- 전화: 042-350-3727[^board][^deptlist]
- 교수 이메일: hanlimc@kaist.ac.kr[^board][^deptlist][^prof]
[^prof]: 연구실 누리집 PEOPLE 메뉴 Professor 페이지 <http://lics.kaist.ac.kr/people-professor/> (교수 학력, 연구분야, 이메일, 2026-10-23 열람)
[^members]: 연구실 누리집 PEOPLE 메뉴 Current Members 페이지 <https://lics.kaist.ac.kr/people-current-members/> (구성원 과정·학력·연구 관심사·이메일, 2026-10-23 열람)
[^journal]: 연구실 누리집 PUBLICATIONS 메뉴 Journal 페이지 <http://lics.kaist.ac.kr/publications-journal/> (국제·국내 학술지 목록, 2026-10-23 열람)
[^conf]: 연구실 누리집 PUBLICATIONS 메뉴 Conference 페이지 <https://lics.kaist.ac.kr/publications-conference/> (국제 학회 논문 목록, 2026-10-23 열람)
[^board]: KAIST 항공우주공학과 연구실 소개 「Laboratory for information and Control Systems」 <https://ae.kaist.ac.kr/boards/view/board_lab/89> (연구실명, 연구실 소개, 연구분야, 연락처, 2021-08-16 게시, 2026-10-23 열람)
[^deptlist]: KAIST 항공우주공학과 교수진 목록 <https://ae.kaist.ac.kr/boards/lists/board_faculty/sc_category/1/> (직위, 학위, 연구분야, 교수실 위치, 2026-10-23 열람)
[^gst]: KAIST 안보과학기술대학원 교수 명단 5쪽 <https://gst.kaist.ac.kr/member/faculty/?page=5> (소속학과, 연구분야와 세부 연구 분야, 연구실 이름, 2026-10-23 열람)
[^p1]: B.-M. Jeong 외, H.-L. Choi, Aerospace 10, 1032 (온라인 2023-12-14). <https://doi.org/10.3390/aerospace10121032> 초록 기준.
[^p2]: J. J. Damanik 외, H.-L. Choi, PeerJ Computer Science 9, e1445 (온라인 2023-08-28). <https://doi.org/10.7717/peerj-cs.1445> 초록 기준.
[^p3]: S. J. Kim, M. Kim, H.-L. Choi, Journal of Spacecraft and Rockets 62, 1109-1121 (2025). <https://doi.org/10.2514/1.a36123> 초록 기준.
[^p4]: J. J. Damanik, J.-W. Jung, C. A. Deresa, H.-L. Choi, IEEE Robotics and Automation Letters 10, 2000-2007 (2025). <https://doi.org/10.1109/lra.2024.3518078> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: M. C. Lim, H.-L. Choi, International Journal of Advanced Robotic Systems 22, 17298806251332359 (온라인 2025-04-13). <https://doi.org/10.1177/17298806251332359> 초록 기준.
[^p6]: W.-C. Lee, K. Lee, H.-L. Choi, International Journal of Aeronautical and Space Sciences 26, 1146-1157 (온라인 2024-10-01). <https://doi.org/10.1007/s42405-024-00823-4> 초록 기준(출판사 논문 페이지).
[^p7]: T. Phisannupawong, J. J. Damanik, H.-L. Choi, IEEE Open Journal of Intelligent Transportation Systems 6, 738-757 (2025). <https://doi.org/10.1109/ojits.2025.3574746> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: Y.-J. Park, S.-S. Park, H.-L. Choi, Journal of Aerospace Information Systems 18, 116-131 (2021). <https://doi.org/10.2514/1.i010891> 초록 기준.

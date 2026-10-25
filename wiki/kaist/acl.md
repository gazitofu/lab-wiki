# 차량 제어 연구실 (Automotive Control Lab, ACL)

**KAIST 기계공학과 · 최세범 교수**

- 분야: 차량 동역학과 제어, 경로 추종·충돌 회피·적응 순항 제어, 노면 마찰과 차량 상태 추정, 클러치·변속기 등 동력 전달계 제어, 서스펜션 고장 진단
- 대분야: 기계·로봇·제조
- 태그: 제어 이론·제어 공학[^me][^p1][^p7], 자율주행[^p2][^p3][^p5], 전기차[^p6], 고장 진단·수명 예측[^p8]
- 홈페이지: <https://acl.kaist.ac.kr/>
- 근거와 출처: [차량 제어 연구실 근거 페이지](acl-sources.md)

> 자동차가 빠르게 달리거나 미끄러운 길을 달릴 때도 정해진 경로를 안정적으로 따라가고 충돌을 피하도록 조향과 제동을 제어하는 방법, 노면 마찰과 차량 상태를 추정하는 방법, 클러치와 변속기 같은 동력 전달 장치를 제어하는 방법을 연구하는 기계공학과 연구실이다.[^me][^p1][^p3][^p6][^p7]

## 무엇을 연구하나

연구실은 KAIST 기계공학과 최세범 교수가 이끄는 차량 제어 연구실이다. 누리집은 영문 이름을 Automotive Control Lab, 줄인 이름을 ACL로 적는다.[^home][^intro] 누리집 소개는 연구실이 2006년 최세범 교수가 KAIST의 Graduate School of Automotive Technology(GSAT)에 부임하면서 세워졌다고 적고, 연구 관심을 차량의 연료를 아끼는 기술을 위한 통합 시스템 설계와 제어로 적는다.[^intro] 기계공학과 연구실 명단은 연구주제를 차량 동역학과 제어(Vehicle Dynamics and Control), 연료 절감 기술과 안전(Fuel Saving Technology and Safety), 센서 응용(Sensor application)으로, 주요 응용 산업을 자동차와 교통 환경으로 적는다.[^me] 기계공학과 교수진 목록은 연구분야를 Fuel Saving Technologies, Vehicle Dynamics Control, Active Safety로 적는다.[^mefac] 차량 동역학(vehicle dynamics)은 차가 가속·제동·선회할 때 차체와 바퀴에 걸리는 힘과 그에 따른 움직임을 다루는 분야다.

대표 논문과 최근 논문으로 보면 연구는 네 갈래로 모인다. 첫째는 자동차가 정해진 경로를 따라가고 앞차나 장애물과 부딪치지 않도록 조향과 제동, 가속을 정하는 제어다. 대표 논문 1은 고속 주행에서 모델 예측 제어(MPC)로 조향과 제동을 함께 정해 어느 타이어도 노면 마찰 한계를 넘지 않게 했고, 대표 논문 2는 앞차의 움직임이 불확실해도 충돌을 피하는 적응 순항 제어를 설계했다.[^p1][^p2] 대표 논문 3은 회피 중에 노면 마찰 계수를 실시간으로 추정해 곧바로 쓰는 충돌 회피 시스템을, 대표 논문 4는 충돌 회피용 비선형 모델 예측 제어를 신경망이 모방 학습하게 해 실시간으로 돌리는 구조를, 대표 논문 5는 주변 차량의 차선 변경 의도를 추론하고 궤적을 예측하는 추정기를 냈다.[^p3][^p4][^p5] 최근 논문 목록에도 조향과 제동을 함께 쓰는 경로 추종, 관절형 차량의 튜브 기반 견고 MPC, 순수 추종(pure pursuit) 방식의 전방 주시 거리 최적화, 긴급 충돌 회피 경로 계획, 미끄러운 노면의 충돌 회피 시스템에 관한 논문이 이어진다.[^cr]

둘째는 제어에 필요한 타이어·노면과 차량의 상태를 재거나 추정하는 연구다. 대표 논문 3의 노면 마찰 계수 추정기가 이 갈래에 걸쳐 있다.[^p3] 최근 논문 목록에는 타이어 종방향 강성의 실시간 추정, 관절형 차량의 횡미끄럼각과 코너링 강성 추정, 무게중심 높이 추정, 지능형 타이어로 하는 타이어 하중과 차량 파라미터 추정, 초음파 반사 신호와 합성곱 신경망으로 타이어 앞 노면 종류를 알아내는 연구, 바퀴 정렬(토 각)의 어긋남 검출, 차선 수준 도로 지도를 원호 스플라인으로 근사하는 연구가 있다.[^cr]

셋째는 엔진·모터의 힘을 바퀴로 전하는 동력 전달계의 제어다. 대표 논문 6은 듀얼 클러치 변속기를 단 전기차의 변속 궤적을 이차 계획법으로 실시간 최적화했고, 대표 논문 7은 볼-램프 듀얼 클러치 변속기의 클러치 구동기에 남는 불확실성을 외란 관측기로 추정했다.[^p6][^p7] 최근 논문 목록에는 습식 클러치의 미끄럼 체결 제어와 열을 고려한 마찰 모형, 토크 컨버터 록업 클러치 제어, 다입력 다출력 MPC 변속, 전기차 구동계의 백래시를 줄이는 저크 억제 제어와 반복 학습 제어, 회생 제동 토크 제어, 4륜 구동 차량의 제어에 관한 논문이 있다.[^cr]

넷째는 서스펜션과 조향 같은 섀시 장치의 추정·진단·제어다. 대표 논문 8은 자기유변 댐퍼의 고장을 차량에 달린 가속도계 두 개만으로 진단하는 알고리즘을 냈다.[^p8] 최근 논문 목록에는 반능동 서스펜션의 상대 속도 추정과 주행 상황 인식에 따른 댐퍼 모드 전환, 스티어 바이 와이어의 조향 반력 제어기 설계, 바퀴마다 조향·구동하는 차량의 구동 고장 진단에 관한 논문이 있다.[^cr]

## 주요 연구 주제

### 1. 경로 추종과 충돌 회피를 위한 조향·제동 제어

고속 주행이나 극한 상황에서는 모형의 불확실성이 제어 오차와 제어 실패로 이어질 수 있다.[^p1] 대표 논문 1은 여러 점에서 선형화하는 방법으로 선형화 오차를 줄이고 구동기의 지연을 반영한 모형으로 예측 오차를 줄인 뒤, 튜브 MPC를 바탕으로 어느 타이어도 마찰 한계를 넘지 않는 조향·제동 입력을 만들고, MPC가 해를 찾을 수 있는 조건을 제시하고 증명했다.[^p1] 대표 논문 3은 많은 충돌 회피 연구가 타이어-노면 마찰 계수를 알려진 상수로 두는 한계를 넘으려고, 경로 계획기·추종 제어기와 짧은 시간에 마찰 계수를 추정하는 추정기를 묶어 추정값을 회피에 실시간으로 쓰고 그 반응으로 다시 추정하게 했다.[^p3] 대표 논문 4는 조향과 제동을 통합한 비선형 모델 예측 제어로 회피 능력을 끌어내고, 이를 심층 신경망이 모방 학습하게 하되 학습 데이터를 오프라인으로 만들 수 있는 구조와 파라미터 변화에 견고하게 하는 입력 무차원화를 넣었다.[^p4] 대표 논문 1, 3, 4.

### 2. 적응 순항 제어와 주변 차량 예측

대표 논문 2는 앞차의 앞으로의 움직임이 불확실해도 충돌을 피하도록, 오버슈트를 피하는 데 필요한 최소 제어 노력을 위험으로 정의하는 일반화된 위험 틀과, 오버슈트가 없음을 보장하면서 제어 노력을 최소로 하는 위험 유지 전략을 만들어 적응 순항 제어에 적용했다.[^p2] 대표 논문 5는 충돌 회피 시스템이 위험이 가장 적은 경로를 계획하는 데 필요한 주변 차량 행동 예측을 위해, 프레네 좌표계에서 만든 여러 후보 경로에 선형화 재귀 최소제곱 추정을 적용하고 경로마다 모드 확률을 구해 차선 변경 의도를 추론하는 다중 모델 기반 적응 추정기를 냈다.[^p5] 대표 논문 2, 5.

### 3. 클러치·변속기 등 동력 전달계 제어

대표 논문 6은 듀얼 클러치 변속기를 단 전기차에서 변속 과정마다 동력 전달계 모형을 세우고, 변속 충격을 줄이는 주파수 성형 저크를 목적 함수로, 운전자 페달 입력과 토크·토크 변화율·저크 한계를 제약으로 둔 이차 계획법 문제를 풀어 변속 궤적과 피드포워드 입력을 만들었다.[^p6] 대표 논문 7은 클러치 구동기의 에너지 소비와 두 클러치가 동시에 맞물릴 때의 역토크를 줄이도록 설계된 볼-램프 듀얼 클러치 변속기에서, 구동기 부품 마찰로 생기는 불확실성을 외란 이득이 시간에 따라 바뀌어도 수렴이 보장되는 확장 고차 외란 관측기로 추정했다.[^p7] 두 논문 모두 동력 전달계를 흉내 낸 테스트벤치 실험으로 검증했다.[^p6][^p7] 대표 논문 6, 7.

### 4. 서스펜션 장치의 상태 추정과 고장 진단

대표 논문 8은 변위 센서를 더 달아야 했던 기존 방법과 달리 차량에 달린 가속도계 두 개만으로, 타카기-스게노 퍼지 미지 입력 관측기로 서스펜션 상태를 추정하고 서포트 벡터 머신 분류기로 경험적 문턱값 없이 자기유변 댐퍼의 상태를 판정하는 고장 진단 알고리즘을 냈다. 쿼터카 시험대에서 여러 노면 조건에 견고함을 보였다.[^p8] 대표 논문 8.

### 5. 누리집에 소개된 연구 주제

누리집 Research Topics는 연료 절감 기술, 능동 안전, 차량 동역학 제어, 기타 기술의 네 묶음에 19개 주제를 소개한다. 여기에는 최근 논문에서 다루는 제어 외에도 엔진 밸브 구동, 공회전 정지·재시동, 운전자 모형 같은 주제가 포함된다.[^topics]

- **듀얼 클러치 변속기**: 두 클러치를 번갈아 쓰면서 변속 중에도 동력 전달을 이어가는 장치다. 소개 페이지는 클러치 토크를 정밀하게 제어하고, 작동 에너지와 출발·변속 때의 충격을 줄이는 것을 연구 목표로 적는다.[^dct]
- **디젤 엔진의 저온 연소 제어**: 배기가스를 엔진 안으로 되돌리는 비율을 높여 입자상 물질과 질소산화물을 줄이는 연소 조건을 다룬다. 연소 방식의 빠른 전환과 여러 입력·출력을 함께 다루는 제어가 필요하다고 설명한다.[^diesel]
- **캠리스 엔진 밸브 구동**: 캠축 대신 전자적으로 제어하는 밸브 구동기를 써서 흡기·배기 밸브가 열리는 시점과 열리는 높이를 조절하는 기술이다.[^camless]
- **공회전 정지·재시동**: 연료 절감과 편안하고 정밀한 제어를 목표로, 자기 차량과 앞차의 정보를 함께 이용해 교통 정체와 주행 조건에 맞춰 엔진을 제어하는 방식을 소개한다.[^isg]
- **충돌 전 감지와 에어백 제어**: 레이더 신호와 차량 상태 신호를 함께 이용해 충돌 상황을 구분하고 에어백 작동 알고리즘에 연결하는 연구다.[^precrash]
- **경량 차량 안전**: 승객 안전과 에너지 효율을 함께 고려한 삼륜 차량 ZEROE의 설계 개념을 소개한다. 탄소섬유·알루미늄 차체, 앞뒤로 배치한 좌석, 충돌 때 승객을 보호하기 위한 확장형 충돌 구역을 제시한다.[^light]
- **바퀴 잠김 방지 제어**: 제동 중 바퀴의 미끄러짐을 연속적으로 제어하는 방식을 소개한다. 앞바퀴와 뒷바퀴의 제어 역할을 나누는 개념을 설명한다.[^abs]
- **운전자 모형**: 사람이 여러 전방 지점을 내다보며 곡선 도로에 맞춰 조향하는 특징을 반영해, 차량의 옆 방향 운동에 대한 운전자 모형을 만드는 연구다.[^driver]
- **전자식 쐐기 브레이크**: 바퀴와 패드 사이에 생기는 힘을 제동에 보태는 자기강화 효과와 비원형 기어를 이용하는 브레이크를 소개한다.[^ewb]

## 대표 논문

출판사 등록 서지에서 최세범 교수가 저자로 오른 2021–2026년 논문 가운데 교수가 마지막 저자이고 초록을 구할 수 있는 논문을 연구 갈래마다 고르게 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학회·학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2023 | [Robust Tube-MPC Based Steering and Braking Control for Path Tracking at High-Speed Driving](https://doi.org/10.1109/tvt.2023.3292616) · IEEE Transactions on Vehicular Technology | 고속에서 정해진 경로를 안정적으로 따라가도록 조향과 제동을 함께 정하는 제어 방법을, 견고한 모델 예측 제어(MPC, 모형으로 앞으로의 움직임을 예측해 매 순간 알맞은 입력을 계산하는 제어) 틀에서 제안했다. 극한 주행에서는 모형의 불확실성이 제어 오차와 실패로 이어질 수 있어, 여러 점에서 선형화하는 방법으로 선형화 오차를 줄이고, 구동기의 지연을 반영한 모형으로 예측 오차를 줄였다. 튜브 MPC(불확실성이 있어도 실제 상태가 계획한 상태 주변의 일정한 범위 안에 머물도록 설계하는 MPC)를 바탕으로 한 제어기는 노면 마찰 한계를 지키며, 어느 타이어도 마찰 한계를 넘지 않는 조향·제동 입력을 만든다. MPC가 해를 찾을 수 있는 조건을 제시하고 증명했고, 여러 시험 상황의 시뮬레이션과 실험으로 효과를 보였다.[^p1] | 1저자 J. Lee, 마지막 저자 최세범 |
| 2 | 2026 | [Collision-Free Adaptive Cruise Control via a Risk Holding Strategy Based on a Generalized Risk Framework](https://doi.org/10.1109/tiv.2026.3693769) · IEEE Transactions on Intelligent Vehicles | 적응 순항 제어(ACC, 앞차와의 간격을 지키며 속도를 자동으로 조절하는 기능)는 앞차가 앞으로 어떻게 움직일지 확실히 알 수 없어도 충돌을 피해야 한다. 기존의 제약 기반·비용 기반 제어는 충돌 안전과 승차감을 정량적으로 맞추기 어려웠다. 이 논문은 오버슈트(목표를 넘어서는 움직임)를 피하는 데 필요한 최소 제어 노력을 오버슈트 위험으로 정의하고, 이를 폐루프 시스템의 극점으로 나타내는 일반화된 위험 틀을 만들어 2차·3차 시스템의 안전 지표를 얻었다. 그리고 오버슈트가 없음을 보장하면서 제어 노력을 최소로 하는 위험 유지 전략을 ACC 설계에 적용했다. 시뮬레이션에서 여러 주행 상황에 걸쳐 충돌을 견고하게 피하고 승차감이 나아졌으며, MPC는 예측 모형에 따라 결과의 편차가 컸다. 여러 노면 마찰 조건에서의 성능도 살폈다.[^p2] | 1저자 G. Ko, 마지막 저자 최세범 |
| 3 | 2024 | [Development of Collision Avoidance System Integrated With Real-Time Tire–Road Friction Coefficient Estimation](https://doi.org/10.1109/tits.2024.3454803) · IEEE Transactions on Intelligent Transportation Systems | 조향과 제동을 함께 쓰는 충돌 회피 연구는 많지만, 회피에 중요한 타이어-노면 마찰 계수를 알려진 상수로 가정하는 경우가 많아 노면 상태가 바뀌면 제대로 대응하기 어려웠다. 이 논문은 마찰 계수를 실시간으로 추정해 곧바로 쓰는 충돌 회피 시스템을 제안했다. 마찰 계수의 변화를 반영하고 갱신된 차량 상태를 빠르게 되먹이는 경로 계획기와 추종 제어기를 설계했고, 추정에 필요한 충분한 가진(추정에 쓸 만큼 차량 움직임을 일으키는 입력)이 오래 이어지지 않는 회피 상황에서도 짧은 시간에 빠르고 정확하게 추정하는 마찰 계수 추정기를 만들었다. 둘을 묶어 추정값을 회피에 실시간으로 쓰고 그 반응으로 다시 추정하게 해, 노면 마찰이 바뀌어도 회피 성능이 좋고 두 부분이 서로를 돕는 선순환이 생김을 보였다.[^p3] | 1저자 H. Lee, 마지막 저자 최세범 |
| 4 | 2024 | [Imitation Learning of Nonlinear Model Predictive Control for Emergency Collision Avoidance](https://doi.org/10.1109/tiv.2023.3309962) · IEEE Transactions on Intelligent Vehicles | 충돌 회피 시스템을 위해, 조향과 제동을 통합한 비선형 모델 예측 제어(NMPC)로 회피 능력을 최대로 끌어내고, 실시간으로 돌 수 있도록 이를 심층 신경망(DNN)이 모방 학습(본보기 제어기의 입력과 출력을 따라 배우는 학습)하게 하는 제어 구조를 제안했다. 앞선 연구는 위험한 상황인데도 모방용 데이터를 실제 제어 대상으로 실험해 얻어야 했고 모델 파라미터를 다루는 데 약점이 있었다. 이 논문은 피드포워드·피드백 구조로 학습 데이터를 오프라인으로 만들 수 있게 하고, 입력을 무차원화하는 과정을 넣어 파라미터 변화에 견고하게 했다. CarSim 기반 사람-차량 상호작용 시뮬레이션에서 오프라인으로 학습한 신경망을 문제없이 적용했고 파라미터 변화에도 견고했다.[^p4] | 1저자 S. Kim, 마지막 저자 최세범 |
| 5 | 2023 | [Lane Change–Intention Inference and Trajectory Prediction of Surrounding Vehicles on Highways](https://doi.org/10.1109/tiv.2023.3266102) · IEEE Transactions on Intelligent Vehicles | 충돌 회피 시스템이 위험이 가장 적은 경로를 계획하려면 주변 차량의 행동 예측이 중요하다. 이 논문은 주변 차량의 차선 변경 의도를 추론하고 궤적을 예측하는 다중 모델 기반 적응 추정기(MMAE)를 제안했다. 도로 곡률 변화에 강한 프레네 좌표계에서 3차 스플라인 곡선으로 경로를 만들고, 선형화 재귀 최소제곱 추정(LRLSE)으로 대상 차량의 지난 궤적에서 미래 궤적을 적응적으로 예측한다. 경로의 끝점을 정하는 미리보기 시간을 시간에 따라 바뀌는 값으로 두어 실시간으로 갱신하고, 여러 경로에 LRLSE를 적용해 경로마다 모드 확률을 구한 뒤 이 확률과 미리보기 시간으로 차선 변경 의도를 추론한다. 실제 차량 궤적 데이터셋 highD로 기존 방법과 비교했고, 학습용 데이터가 많이 필요하지 않으며 계산 부담이 낮아 실시간성이 높다.[^p5] | 1저자 J. Do, 마지막 저자 최세범 |
| 6 | 2023 | [Real-Time Optimization of Gear Shift Trajectories Using Quadratic Programming for Electric Vehicles With Dual Clutch Transmissions](https://doi.org/10.1109/tvt.2023.3246179) · IEEE Transactions on Vehicular Technology | 듀얼 클러치 변속기를 단 전기차의 변속 궤적을 실시간으로 최적화하는 방법이다. 변속 과정마다 동력 전달계 모형을 세워 상태를 예측하고, 변속 충격을 줄이면서 하위 제어기의 대역폭 한계를 고려하도록 주파수 성형한 저크(jerk, 가속도가 변하는 빠르기)를 목적 함수로 삼았다. 변속 과정 사이 모형 전환이 매끄럽도록, 그리고 실시간으로 바뀔 수 있는 운전자의 페달 입력을 반영하도록 등식 제약을 두고, 토크·토크 변화율·저크의 최댓값을 부등식 제약으로 제한해 이차 계획법(QP) 문제로 만들었다. QP 풀이기로 얻은 최적해로 변속 궤적과 피드포워드 입력을 만들고, 테스트벤치 실험으로 성능을 검증했다.[^p6] | 1저자 T. Lee, 마지막 저자 최세범 |
| 7 | 2023 | [Extended High-Order Disturbance Observer-Based Clutch Actuator Model Uncertainty Estimation of Ball-Ramp Dual-Clutch Transmission](https://doi.org/10.1109/tcst.2022.3215840) · IEEE Transactions on Control Systems Technology | 볼-램프 듀얼 클러치 변속기(BR-DCT)는 기존 듀얼 클러치 변속기의 단점을 보완하려고 제안된 것으로, 클러치 구동기의 에너지 소비와 두 클러치가 동시에 맞물리는 타이업 때의 역토크를 줄이도록 설계됐다. 셀프 에너자이징(self-energizing) 원리를 써서 클러치 구동기의 주된 불확실성인 마찰 계수 없이 구동기 모형을 쓸 수 있지만, 구동기 부품 사이 마찰로 생기는 측정 오차가 작은 불확실성을 남긴다. 이 논문은 외란 이득이 시간에 따라 바뀌는 시스템에서도 수렴이 보장되는 확장 고차 외란 관측기(EH-DOB)로 이 불확실성을 추정하는 방법을 내고, 추정 오차의 수렴을 증명했다. BR-DCT를 단 동력 전달계를 흉내 낸 테스트벤치 실험에서 추정이 정확했고, 외란 제거 제어에 쓸 만큼 정확하고 안정적임을 확인했다.[^p7] | 1저자 D.-H. Kim, 마지막 저자 최세범 |
| 8 | 2022 | [Takagi–Sugeno Fuzzy Observer-Based Magnetorheological Damper Fault Diagnosis Using a Support Vector Machine](https://doi.org/10.1109/tcst.2021.3123611) · IEEE Transactions on Control Systems Technology | 자기유변(MR) 댐퍼의 고장 진단 알고리즘을 제안했다. 기존 방법은 상용 차량에 달린 가속도계 두 개에 더해 변위 센서를 써야 해 상용 차량에 적용하기 어려웠다. 이 논문은 가속도계 두 개만 쓴다. 타카기-스게노(T-S) 퍼지 미지 입력 관측기로 서스펜션 상태를 추정하는데, 댐퍼의 히스테리시스(같은 입력에도 이전 상태에 따라 출력이 달라지는 성질)와 알 수 없는 노면 높이의 영향 속에서도 댐퍼 상태를 추정할 수 있고, 리아푸노프 안정성 정리로 관측기의 안정성을 확인했다. 경험적으로 정한 문턱값 없이 서포트 벡터 머신(SVM) 분류기로 댐퍼 상태를 판정해 고장 신호를 만든다. 쿼터카 시험대에서 여러 노면 조건에 견고함을 보였고, 차량에 쓰는 값싼 양산 센서로 진단 알고리즘 설계의 수고를 줄일 수 있다고 밝혔다.[^p8] | 1저자 K. Jeong, 마지막 저자 최세범 |

## 교수와 전문 분야

최세범 교수는 KAIST 기계공학과 교수다. 기계공학과 교수진 목록은 연구분야를 Fuel Saving Technologies, Vehicle Dynamics Control, Active Safety로 적고,[^mefac] 교수 소개 페이지는 연구 관심을 차량 동역학과 제어(Vehicle Dynamics and Control), 연료 절감 기술(Fuel Saving Technology)로 적는다.[^prof] 미래자동차학제전공 교수진에도 소속학과 기계공학과, 주요연구분야 「자동차 제어」로 올라 있다.[^fv]

교수 소개 페이지에 따르면 서울대학교에서 기계공학 학사(1981–1985), KAIST에서 기계공학 석사(1985–1987), University of California, Berkeley에서 기계공학 박사(1990–1993)를 했다. Agency for Defense Development 연구원(1987–1990), UC Berkeley Institute of Transportation Studies의 Assistant Research Engineer(1993–1997), TRW Automotive의 Principal Engineer(1997–2006)를 거쳐, 2006–2008년 KAIST Graduate School of Automobile Technology 부교수를 지냈고 2009년부터 기계공학과 교수다.[^prof] 같은 페이지는 TRW Automotive에서 ABS(급제동 때 바퀴가 잠기지 않게 제동력을 조절하는 장치) 제어 로직 선행 개발(1997–2000), 2륜·4륜 구동력 제어(TC) 로직 개발(2001–2002), ESP(차체 자세 제어 장치) 로직 선행 개발(2002–2003), ROM control logic 개발(2004–2005), 디지털 밸브 제어 로직 개발(2005–2006)을, UC Berkeley에서 엔진 연료 분사·토크 제어 알고리즘 개발(1990–1993)과 자동화 고속도로 시스템(automated highway system)의 자율 주행 차량 제어 로직 개발(1993–1997)을 맡았다고 적는다. ASME(1993년부터), SAE(1997년부터), KSAE(2006년부터) 회원이다.[^prof]

교수 소개 페이지가 적은 수상은 다음과 같다. 2020년 Korean Federation of Science & Technology Societies의 'Sci. & Tech. Excellent Paper Award'(논문 「Engine Net Torque Compensation Through Driveline Torque Estimation in a Parallel Hybrid Vehicle」), 2016년 Institute of Mechanical Engineers, U.K.의 'Award for Risk Reduction in Mechanical Engineering'(논문 「Integrated Vehicle Mass Estimation for Vehicle Safety Control using the Recursive Least-Squares Method and Adaptation Laws」 등), 2016년 16th Asia Design Engineering Workshop의 'Innovative Design Contest Award'(「Safe Attachable Wheelchair Assistive Device in Capstone Design」), 2016년 The Korean Society of Automotive Engineers의 'Academic Award'(논문 「Pressure Model Based Coordinated Control of VGT and Dual-loop EGR in a Diesel Engine Air-path System」 등), 1999년 IEEE Control Systems Society의 IEEE Transactions on Control Systems Technology Outstanding Paper Award(논문 「Air-to-Fuel Control of Spark Ignition Engines using Gaussian Network Sliding Control」), 1998년 University of California의 'Distinguished Service Team Award'(자동화 차량 제어 시스템 개발과 1997년 San Diego 시연)다.[^prof]

논문으로 보면 전문 분야는 차량 동역학을 바탕으로 한 주행 제어(경로 추종, 충돌 회피, 적응 순항 제어, 주변 차량 예측), 클러치·변속기 같은 동력 전달계의 모형화와 제어, 서스펜션 장치의 상태 추정과 고장 진단이다(대표 논문 1–8).[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

기계공학과 연구실 명단은 주요 응용 산업을 자동차와 교통 환경으로 적는다.[^me] 대표 논문들은 고속 주행의 경로 추종(대표 논문 1), 앞차를 따라가는 순항 제어(대표 논문 2), 노면 마찰이 바뀌는 상황과 긴급 상황의 충돌 회피(대표 논문 3, 4), 고속도로 주변 차량의 차선 변경 예측(대표 논문 5), 전기차 변속(대표 논문 6), 듀얼 클러치 변속기의 클러치 구동기(대표 논문 7), 상용 차량 서스펜션 댐퍼의 고장 진단(대표 논문 8)을 대상으로 삼았고, 시뮬레이션과 차량 실험, 테스트벤치, 쿼터카 시험대, 실제 차량 궤적 데이터셋으로 검증했다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 구성원

2026년 10월 25일 열람한 누리집 게시 명단이다. Students에는 박사과정 5명·석사과정 3명, Postdoc에는 박사후연구원 4명이 올라 있다. 과정 시작 연도는 명시되어 있지 않으며 이메일은 모두 `[@]` 표기다.[^students][^postdoc]

| 이름 | 과정 | 시작 연도 | 연구 주제(게시 원문) | 대표 논문 참여 |
|---|---|---|---|---|
| 고건희 (GEONHEE KO) | 박사 | 미기재 | Autonomous vehicle path planning & control, system identification | 2 |
| 전진환 (JINHWAN JEON) | 박사 | 미기재 | Lane Detection based Vehicle Localization |  |
| 임채호 (CHAEHO LIM) | 박사 | 미기재 | Vehicle dynamics and control |  |
| 정태우 (TAEWOO JEONG) / 랩 대표 | 박사 | 미기재 | Vehicle dynamics and control |  |
| 정세민 (SEMIN JEONG) | 박사 | 미기재 | Vehicle dynamics and control |  |
| 송주오 (JUO SONG) | 석사 | 미기재 | Vehicle dynamics and control |  |
| 이현민 (HYEONMIN LEE) | 석사 | 미기재 | Vehicle dynamics and control |  |
| 함제현 (JEHYEON HAHM) | 석사 | 미기재 | Vehicle dynamics and control |  |
| 김승택 (SEUNGTAEK KIM) | 박사후 | 미기재 | Vehicle dynamics and control, Path planning and tracking control | 4 |
| 김진욱 (JINWOOK KIM) | 박사후 | 미기재 | 4WIS 4WID system, Vehicle dynamics and control |  |
| 이해우 (HAEWOO LEE) | 박사후 | 미기재 | Powertrain modeling and control, Vehicle dynamics and control |  |
| 오지열 (JIYEOL OH) | 박사후 | 미기재 | Vehicle dynamics and control |  |

대표 논문 참여는 위 대표 논문 표의 번호이며 영문 이름의 완전 일치로 표시했다.[^students][^postdoc]

## 졸업생 진로

누리집의 Ph.D Alumni 34개·M.S Alumni 22개 항목을 옮겼다. 진로는 누리집의 Current Position 표기이며 각 기관의 현재 재직을 별도로 확인한 것은 아니다. 박사후연구원 4명은 박사 졸업생 구획에도 올라 있으므로 구성원과 졸업생의 수를 더해 고유 인원으로 세지 않는다. `-`는 누리집의 원래 표기다.[^alumni]

| 이름 | 학위 | 졸업 연도 | 누리집 게시 진로 |
|---|---|---|---|
| Jinsung Kim (김진성) | 박사 | 2013 | Hyundai motors corp. (현대자동차) |
| Hyomin Jin (진효민) | 박사 | 2014 | Hyundai Autron (현대오트론) |
| Mooryong Choi (최무룡) | 박사 | 2014 | Hyundai Motor corp. (현대자동차) |
| Kwanghyun Cho (조광현) | 박사 | 2014 | Pusan National University (부산대학교) |
| Jiwon Oh (오지원) | 박사 | 2016 | Hyundai motors corp. (현대자동차) |
| Heeram Park (박희람) | 박사 | 2017 | LS Mtron (LS 엠트론) |
| Jonghwa Kim (김종화) | 박사 | 2017 | Samsung Electronics (삼성전자) |
| Chulwoo Moon (문철우) | 박사 | 2018 | Chonnam National University (전남대학교) |
| Sooyoung Kim (김수영) | 박사 | 2018 | SOOKMYUNG WOMEN’S UNIVERSITY (숙명여자대학교) |
| Kyoungseok Han (한경석) | 박사 | 2018 | Hanyang University (한양대학교) |
| Hojin Jung (정호진) | 박사 | 2019 | 한국교통대학교 |
| Seung-Uk Park (박승욱) | 박사 | 2019 | KATECH (한국자동차연구원) |
| Gieso Park (박기서) | 박사 | 2020 | University of Ulsan (울산대학교) |
| Hyunseok Choi (최현석) | 박사 | 2020 | Agency for Defence Development (국방과학연구소) |
| Yunhyoung Hwang (황윤형) | 박사 | 2021 | Jeonbuk National University (전북대학교) |
| Kicheol Jeong (정기철) | 박사 | 2021 | KATECH (한국자동차연구원) |
| Minhyun Kim (김민현) | 박사 | 2021 | MoveAWheeL (모바휠) |
| Jinrak Park (박진락) | 박사 | 2021 | Hyundai motors corp. (현대자동차) |
| Donghyun Kim (김동현) | 박사 | 2022 | Hyundai motors corp. (현대자동차) |
| Sanghun Jung (정상훈) | 박사 | 2022 | Hyundai motors corp. (현대자동차) |
| Jonghyup Lee (이종협) | 박사 | 2023 | SOOKMYUNG WOMEN’S UNIVERSITY (숙명여자대학교) |
| Taeheon Lee (이태헌) | 박사 | 2023 | Hyundai motors corp. (현대자동차) |
| Seungin Sin (신승인) | 박사 | 2023 | Samsung Electronics (삼성전자) |
| DASOL JEONG (정다솔) | 박사 | 2023 | Pusan National University (부산대학교) |
| HWANGJAE LEE (이황재) | 박사 | 2024 | - |
| YOONJIN HWANG (황윤진) | 박사 | 2024 | Hankook Tire (한국타이어) |
| HYUNGJEEN CHOI (최형진) | 박사 | 2024 | KATECH (한국자동차연구원) |
| YUNTAE KIM (김윤태) | 박사 | 2025 | KATECH (한국자동차연구원) |
| BYUNGJUN KIM (김병준) | 박사 | 2025 | KATECH (한국자동차연구원) |
| JONGYONG DO (도종용) | 박사 | 2025 | Hyundai motors corp. (현대자동차) |
| SEUNGTAEK KIM (김승택) | 박사 | 2025 | KAIST ACL (차량제어연구실) |
| JINWOOK KIM (김진욱) | 박사 | 2025 | KAIST ACL (차량제어연구실) |
| HAEWOO LEE (이해우) | 박사 | 2026 | KAIST ACL (차량제어연구실) |
| JIYEOL OH (오지열) | 박사 | 2026 | KAIST ACL (차량제어연구실) |
| Kwanghui Kim (김광희) | 석사 | 2008 | MANDO (만도) |
| Jongmin Ko (고종민) | 석사 | 2008 | Traffic environment research center (환경부 국립환경과학원 교통환경연구소) |
| Leehyoung Cho (조이형) | 석사 | 2008 | Doosan Infracore (두산 인프라코어) |
| Sungryong Kim (김성룡) | 석사 | 2009 | Samsung Tales (삼성 탈레스) |
| Kanghyun Nam (남강현) | 석사 | 2009 | DGIST |
| Hyunwoo Son (손현우) | 석사 | 2009 | Doosan heavy industries (두산중공업) |
| Seongsoo Kim (김성수) | 석사 | 2010 | KEPCO NF (한전원자력원료) |
| Sungho Choi (최성호) | 석사 | 2010 | Hyundai motors corp. (현대자동차) |
| Youngsik Yoon (윤영식) | 석사 | 2011 | Hyundai motors corp. (현대자동차) |
| Daeil Kim (김대일) | 석사 | 2013 | Hyundai motors corp. (현대자동차) |
| Yoonkab Noh (노윤갑) | 석사 | 2014 | Hyundai motors corp. (현대자동차) |
| Ahmed Sadek | 석사 | 2017 | - |
| EunJae Lee (이은재) | 석사 | 2016 | Hankook Tire (한국타이어) |
| Hanseon Ga (가한선) | 석사 | 2017 | Hyundai motors corp. (현대자동차) |
| Saebom Kim (김새봄) | 석사 | 2017 | Hanon Systems (한온시스템) |
| Jinseung Lee (이진승) | 석사 | 2018 | KATECH (한국자동차연구원) |
| Sihyun Seong (성시현) | 석사 | 2020 | - |
| Hyunwoo Jin (진현우) | 석사 | 2023 | Hyundai Mobis (현대모비스) |
| Hohyon Choi (최호현) | 석사 | 2023 | Hyundai motors corp. (현대자동차) |
| SUNGYOON IM (임성윤) | 석사 | 2024 | - |
| GWANGHUN LEE (이광훈) | 석사 | 2025 | Hyundai motors corp. (현대자동차) |
| SANGWOO SHIN (신상우) | 석사 | 2025 | KAIST PML(Precision Mechatronics Laboratory) |

## 최근 논문 목록 (2021–2026)

랩이 게시한 연도를 기준으로 국제 학술지 60편·국제 학회 8편·국내 학회 발표 13건을 옮겼다. 국내 학술지 페이지의 7개 항목은 모두 2020년 이전이다. 기존 Crossref 목록 66편은 모두 랩 국제 목록에서 제목이 대응했고, 국제 논문 2편과 국내 학회 발표 13건을 보완했다. 아래 날짜·저자·학술지 표기는 랩 목록을 따르며 출판사 서지와 차이가 있는 항목은 근거 페이지에 남겼다.[^labij][^labic][^labdj][^labdc]

### 국제 학술지

**2026**

- Byungjun Kim, Seibum B. Choi, Sooyoung Kim, “Optimal input shape terminal iterative learning control for robust backlash mitigation in EV powertrains”, CONTROL ENGINEERING PRACTICE, vol.175, 2026.08[^labij]
- Byungjun Kim, Seibum B. Choi, Sooyoung Kim, “Relative Velocity Estimation for Semi-active Suspension with Disturbance-Decoupled Kalman Filtering Using Production Vehicle Sensors”, PROCEEDINGS OF THE INSTITUTION OF MECHANICAL ENGINEERS PART D-JOURNAL OF AUTOMOBILE ENGINEERING, 2026.06[^labij]
- Geonhee Ko, Seibum B. Choi, ” Priority-Aware Tracking of Infeasible Trajectories via Smooth Input Saturation and Asymmetric Control Structure”, International Journal of Automotive Technology, 2026.06[^labij]
- Yuntae Kim, Byungjun Kim, Dasol Jeong, Hyuck-Kee Lee, Seibum B. Choi, “Energy-based Adaptive Cruise Control with Structurally Induced Self-Excited Driving for Car-Following”, IEEE Transactions on Intelligent Transportation Systems, 2026.09[^labij]
- Geonhee Ko, Seibum B. Choi, “Collision-Free Adaptive Cruise Control via a Risk Holding Strategy Based on a Generalized Risk Framework”, IEEE Transactions on Intelligent Vehicles, vol.11, no.7, pp.857-868, 2026.7[^labij]
- Jinhwan Jeon, Seibum B. Choi, “Tree-Structured Recursive Arc Spline Approximation of Complex Lane-Level Maps with G¹ Continuity”, INTERNATIONAL JOURNAL OF AUTOMOTIVE TECHNOLOGY, 2026.05[^labij]
- Jiyeol Oh, Seibum B. Choi, “Operating Principles of Weight Distribution Hitches and Their Impact on Handling Characteristics of Vehicle-Trailer Systems”, Vehicle System Dynamics, Vehicle System Dynamics, pp.1-27, 2026.04[^labij]
- Byungjun Kim , DongHyun Kim, Seibum B. Choi, and Jonghyup Lee, “Model-based Optimal Anti-jerk Control for Electric Vehicle Powertrain with Backlash”, International Journal of Control, Automation, and Systems, vol. 24, pp. 991-1005, 2026.04[^labij]
- Chaeho Lim, Seonggyeong Ju, Yunjeong Hwang, Hanseon Ga, Jinseok Song, Seibum B. Choi, Sooyoung Kim, “Regenerative Braking Torque Control with Tire-Force-Based Limiting for Vehicle Stability of a Front–Rear Motor-Driven EV”, CONTROL ENGINEERING PRACTICE, v.169, 2026.04[^labij]
- Seungtaek Kim, Jonghyup Lee, Kyoungseok Han, Seibum B. Choi, “Bridging the Sim-to-real Gap: A Control Framework for Imitation Learning of Model Predictive Control”, INTERNATIONAL JOURNAL OF CONTROL AUTOMATION AND SYSTEMS, 2026.02[^labij]
- Jinwook Kim, Seibum Choi, “Machine Learning based Drive Fault Diagnosis and Isolation Algorithm for 4WIS4WID Vehicle using Residual Visualization”, IEEE Transactions on Intelligent Vehicles vol.11, no. 5, pp. 629-642, 2026.5,[^labij]

**2025**

- Yuntae Kim, Seibum B. Choi, “DAMPER MODE CHANGE BASED ON DRIVING CONDITION RECOGNITION FOR SEMI-ACTIVE SUSPENSION ON RANDOM ROAD PROFILE”, INTERNATIONAL JOURNAL OF AUTOMOTIVE TECHNOLOGY, 2025.10[^labij]
- Jinhwan Jeon, Seibum B. Choi, “Efficient Arc Spline Approximation of Large Sized Complex Lane-Level Road Maps”, IEEE Transactions on Intelligent Transportation Systems, vol. 26, no. 10, 2025.06[^labij]

**2024**

- Jiyeol Oh, Seibum B. Choi, “Optimal Tongue Weight Selection Criteria for Light Vehicle-Trailer Combinations”, Vehicle System Dynamics, v.63, no.12, pp.2347-2370, 2024.10[^labij]
- Hwangjae Lee, Seibum Choi, “Development of Collision Avoidance System Integrated with Real-Time Tire-Road Friction Coefficient Estimator”, IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS vol.25, no.12, pp.21327-21342, 2024.10[^labij]
- Haewoo Lee, Seibum Choi, “Path Planning using Dual Connecting Points Optimization for Emergency Collision Avoidance”, IEEE Transactions on Intelligent Vehicles vol.10, no.3, pp.2127-2139, 2024.8[^labij]
- Jinhwan Jeon, Yoonjin Hwang, Seibum B. Choi, “Reliability-based G1 Continuous Arc Spline Approximation”, COMPUTER AIDED GEOMETRIC DESIGN Volume 112, 2024.07[^labij]
- Seungin Shin, Seibum B. Choi, “Control-Oriented Modeling of Wet Clutch Friction considering Thermal Dynamics”, MECHATRONICS vol.99, 2024.05[^labij]
- Hyungjeen Choi, Seibum Ben Choi, “Design of The Steering Feedback Controller of A Steer-by-Wire System Using Admittance Model”, INTERNATIONAL JOURNAL OF AUTOMOTIVE TECHNOLOGY, vol.25, no.3, pp.565-574, 2024.06[^labij]
- Jongyong Do, Dongyoon Hyun, Kyoungseok Han, Seibum B. Choi, “Real-time Estimation of Longitudinal Tire Stiffness Considering Dynamic Characteristics of Tire”, MECHATRONICS vol.98, 2024.04[^labij]
- Dasol Jeong, Seibum Choi, “Tube-based Robust Model Predictive Control for Tracking Control of Autonomous Articulated Vehicles”, IEEE TRANSACTIONS ON INTELLIGENT VEHICLES vol.9, no.1, pp.2184-2196, 2024.01[^labij]
- Dasol Jeong, Seibum Choi, “Efficient Trajectory Planning for Autonomous Vehicles Using Quadratic Programming with Weak Duality”, IEEE TRANSACTIONS ON INTELLIGENT VEHICLES vol.9, no.1, pp.2878-2892, 2024.01[^labij]
- Seungtaek Kim, Kyoungseok Han, Seibum B. Choi, “Imitation Learning of Nonlinear Model Predictive Control for Emergency Collision Avoidance”, IEEE TRANSACTIONS ON INTELLIGENT VEHICLES vol.9, no.1, pp.2908-2922, 2024.01[^labij]
- Seungtaek Kim, Jonghyup Lee, Kyoungseok Han, Seibum B. Choi, “Vehicle Path Tracking Control Using Pure Pursuit with MPC-based Look-ahead Distance Optimization“, IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY vol.73, no.1, pp.53-66, 2024.01[^labij]
- Yuntae Kim, Seibum B. Choi, Jiwon J. Oh, Jeongsoo Eo, “Satisfactory Driving Mode Classification based on Pedal Operation Characteristics”, IEEE TRANSACTIONS ON INTELLIGENT VEHICLES vol.9, no.1, pp.2988-2998, 2024.01[^labij]

**2023**

- Jonghyup Lee, Yoonjin Hwang, Seibum B. Choi, “Robust Tube-MPC based Steering and Braking Control for Path Tracking at High-Speed Driving“, IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY vol.72, no.12, pp.15301~15316, 2023.06[^labij]
- Donghyun Kim, Seibum B. Choi, “Composite Control Law for Nonlinear Systems with Mismatched Disturbances for a Ball-Ramp Dual-Clutch Transmission”, IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS vol.24, no.10, pp.11265-11277, 2023.10[^labij]
- Jongyong Do, Kyoungseok Han, Seibum B. Choi, “Lane Change–Intention Inference and Trajectory Prediction of Surrounding Vehicles on Highways”, IEEE TRANSACTIONS ON INTELLIGENT VEHICLES vol.8, no. 7, pp.3813~3825, 2023.7[^labij]
- Hojin Jung, Seibum Ben Choi, “Modified Generalised Maxwell Slip Based Electro-hydraulic Transfer Case Modeling for All-wheel Drive Vehicle Simulation”, INTERNATIONAL JOURNAL OF AUTOMOTIVE TECHNOLOGY vol. 24, no. 1, pp.45-54, 2023.02[^labij]
- Taeheon Lee, Seibum B. Choi, “Real-time Optimization of Gear Shift Trajectories using Quadratic Programming for Electric Vehicles with Dual Clutch Transmission”, IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY vol. 72, no. 7, pp.8647~8660 , 2023.6[^labij]
- Hwangjae Lee, Seibum Choi, “Model Predictive Control based Multifunctional Advanced Driver-Assistance System Specialized for Rear-End Collision Avoidance”, INTERNATIONAL JOURNAL OF AUTOMOTIVE TECHNOLOGY vol. 24, no. 3, pp.799~809, 2023.5[^labij]
- Hwangjae Lee, Seibum Choi, “Online Detection of Toe Angle Misalignment Based on Lateral Tire Force and Tire Aligning Moment”, INTERNATIONAL JOURNAL OF AUTOMOTIVE TECHNOLOGY vol. 24, no. 3, pp.623~632, 2023.5[^labij]
- Seungin Shin, Seibum B. Choi, “Observer-based Iterative Learning Control for a High Relative Degree Nonlinear System and its Application to a Vehicular Wet-clutch System”, MECHANISM AND MACHINE THEORY vol. 180, 105158, 2023.2[^labij]
- Donghyun Kim, Seibum B. Choi, “Extended Disturbance Observer for Nonlinear System with Time Varying Disturbance Gain”, INTERNATIONAL JOURNAL OF ADAPTIVE CONTROL AND SIGNAL PROCESSING vol. 37, no. 1, pp. 347~355, 2023.2[^labij]
- Jonghyup Lee, Seibum Choi, “Integrated Control of Steering and Braking for Path Tracking using Multi-Point Linearized MPC”, IEEE TRANSACTIONS ON INTELLIGENT VEHICLES vol. 8, no. 5, pp. 3324~3335, 2023.5[^labij]
- Donghyun Kim, Seibum Ben Choi, “Extended High-order Disturbance Observer based Clutch Actuator Model Uncertainty Estimation of Ball-ramp Dual-clutch Transmission”, IEEE TRANSACTIONS ON CONTROL SYSTEMS TECHNOLOGY vol. 31, no. 3, pp. 1220~1234, 2023.5[^labij]
- Byungjun Kim, Seibum Ben Choi, Young Kwon Kim, “Observer-based Control for a Torque Converter Lock-up Clutch Utilizing a Steady-state Torque Map”, IEEE TRANSACTIONS ON CONTROL SYSTEMS TECHNOLOGY vol. 31, no. 3, pp. 1208~1219, 2023.5[^labij]

**2022**

- Yongseop Jeong, Jinsun Park, Donghyeon Cho, Yoonjin Hwang, Seibum Choi, In So Kweon, “Lightweight Depth Completion Network with Local Similarity-Preserving Knowledge Distillation”, SENSORS, vol. 22, no. 19, 2022.10[^labij]
- Donghyun Kim, Seibum B. Choi, “Design of Ball-Ramp Dual Clutch Transmission to Reduce Uncertainties in Clutch Actuator and Tie-up Effect”, MECHANISM AND MACHINE THEORY ,vol.176, 2022.10[^labij]
- Dasol Jeong, Seibum Choi, “Tracking Control Based on Model Predictive Control Using Laguerre Functions with Pole Optimization”, IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS, vol. 23, no. 11, 2022.11[^labij]
- Seungin Shin, Donghyun Kim, Seibum Choi, “Apparatus for Identification of Frictional and Thermal Characteristics of a Wet Clutch”,INTERNATIONAL JOURNAL OF AUTOMOTIVE TECHNOLOGY, vol.23, no. 6, 2022.12[^labij]
- Hwangjae Lee, Seibum Choi, “Development of Collision Avoidance System in Slippery Road Conditions”, IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS, Vol. 23, 2022.10[^labij]
- Yunhyoung Hwang, Seibum B. Choi, “Awareness on Present and Future Trajectory of Vehicle Using Multiple Hypotheses in the Mixed Traffic of Intersection”, IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS, vol. 23, no. 10, 2022.10[^labij]
- Dasol Jeong, Geonhee Ko, Seibum B. Choi, “Estimation of Sideslip Angle and Cornering Stiffness of an Articulated Vehicle Using a Constrained Lateral Dynamics Model”, MECHATRONICS, vol.85, 2022.08[^labij]
- Jinrak Park, Seibum Choi, “Adaptive Slip Engagement Control of a Wet Clutch in Vehicle Powertrain Based on Transmitted Torque Estimation”, MECHANICAL SYSTEMS AND SIGNAL PROCESSING, vol.171, 2022.05[^labij]
- Jonghyup Lee, Seibum Choi, “Nonlinear Model Predictive Control for Path Tracking in High-Speed Corner Entry Situations”, INTERNATIONAL JOURNAL OF AUTOMOTIVE TECHNOLOGY vol. 23, no. 5, pp. 1373-1382, 2022.10[^labij]
- Yoonjin Hwang, Yongseop Jeong, Inso Kweon, Seibum B. Choi, “Identification of Vehicle Dynamics Model and Lever-arm for Arbitrarily Mounted Motion Sensor”, IEEE SENSORS JOURNAL, vol.22, no.10, pp.9843~9856, 2022.05[^labij]
- Taeheon Lee, Dong-Hyun Kim, Seibum B. Choi, “Driveline Modeling with Transmission Loss and Robust Torque Observer Design for Dual Clutch Transmission”, IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY, vol.71, no.2, pp.1267~1279, 2022.02[^labij]
- Jinrak Park, Seibum Choi, “Gear shifting based on MIMO model predictive control for convenient adjustment of shifting performance”, IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY Vol. 71, No. 1, pp. 233-249, January 2022[^labij]
- Kicheol Jeong, Seibum B. Choi, “Takagi-Sugeno fuzzy observer based magnetorheological damper fault diagnosis using a support vector machine”, IEEE TRANSACTIONS ON CONTROL SYSTEMS TECHNOLOGY, vol.30, no.4, pp.1723~1735, 2022.07[^labij]
- Hojin Jung, Dohyun Jung, Seibum B. Choi, “LQR Control of an All-Wheel Drive Vehicle Considering Variable Input Constraint”, IEEE TRANSACTIONS ON CONTROL SYSTEMS TECHNOLOGY, v.30, no.1, pp.85-96, 2022.01[^labij]

**2021**

- Jinhwan Jeon ,Yoonjin Hwang ,Yongseop Jeong ,Sangdon Park,In So Kweon, Seibum B. Choi, “Lane Detection Aided Online Dead Reckoning for GNSS Denied Environments”, SENSORS, 2021.10[^labij]
- Giseo Park, Seibum Choi, “A Model Predictive Control for Path Tracking of Electronic-Four-Wheel Drive Vehicles”, IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY v. 70, No. 11, pp. 11352-11364, 2021.11[^labij]
- Yoonjin Hwang, Yongseop Jeong, In So Kweon, Seibum Choi, “Online Misalignment Estimation of Strapdown Navigation for Land Vehicle under Dynamic Condition”, INTERNATIONAL JOURNAL OF AUTOMOTIVE TECHNOLOGY v.22 no.6 2021.12[^labij]
- Dasol Jeong, Seibum B. Choi, Jonghyup Lee, Mintae Kim, Hojong Lee , “Tire dimensionless numbers for analysis of tire characteristics and intelligent tire signals”, MECHANICAL SYSTEMS AND SIGNAL PROCESSING, v.161, 2021.12[^labij]
- Giseo Park, Seibum B. Choi , “An Integrated Observer for Real-Time Estimation of Vehicle Center of Gravity Height”, IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS, v.22, no.9, pp.5660-5671, 2021.09[^labij]
- Kyoungseok Han, Giseo Park, Gokul S. Sankar, Kanghyun Nam, Seibum B. Choi , “Model Predictive Control Framework for Improving Vehicle Cornering Performance Using Handling Characteristics”, IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS, v.22, no.5, pp.3014-3024, 2021.05[^labij]
- Min-Hyun Kim, Jongchan Park, Seibum Choi , “Road Type Identification Ahead of the Tire Using D-CNN and Reflected Ultrasonic Signals”, INTERNATIONAL JOURNAL OF AUTOMOTIVE TECHNOLOGY, v.22, no.1, pp.47-54, 2021.02[^labij]
- Jinrak Park, Seibum Choi , “Optimization method of reference slip speed in clutch slip engagement in vehicle powertrain”, INTERNATIONAL JOURNAL OF AUTOMOTIVE TECHNOLOGY, v.22, no.1, pp.55-67, 2021.02[^labij]
- Dasol Jeong, Seungtaek Kim, Jonghyup Lee, Seibum B. Choi, Mintae Kim, Hojong Lee , “Estimation of Tire Load and Vehicle Parameters Using Intelligent Tires Combined With Vehicle Dynamics”, IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, v.70, pp.9502412, 2021.01[^labij]

### 국제 학회

**2026**

- Taewoo Jeong, Byungjun Kim, Dong-Hyun Kim, Jinwook Kim and Seibum B. Choi, “Power-on Downshift with Clutch Kissing Point Detection utilizing Ball-Ramp Dual Clutch Transmission Asymmetry”, The 10th IEEE Conference on Control Technology and Applications (CCTA), Vancouver, BC, Canada, August, 2026.[^labic]
- Semin Jeong, Jiyeol Oh, Seibum B. Choi, “Design of a Sensorless Trailer Anti-lock Braking System based on Trailer Swing Detection”, in Proceedings of 2026 American Control Conference, New Orleans, LA.[^labic]

**2025**

- Seungtaek Kim, Seibum B. Choi, “Approximate Robust Tube Nonlinear Model Predictive Control for Vehicle Collision Avoidance”, The 9th IEEE Conference on Control Technology and Applications (CCTA), San Diego, USA, August, 2025.[^labic]
- Haewoo Lee, Seibum B. Choi, “Emergency Lane Change Trajectory Planning for High Center of Gravity Vehicles using Time-Domain Dual Connecting Points Optimization”, The 9th IEEE Conference on Control Technology and Applications (CCTA), San Diego, USA, August, 2025.[^labic]

**2024**

- Byungjun Kim, Seibum B. Choi, “Iterative Learning Control for Linear Hybrid System with Iteration-varying References”, International Conference on Control and Robotics, Yokohama (Japan), December, 2024.[^labic]
- Jinhwan Jeon, Chaeho Lim, Yoonjin Hwang, Seibum B. Choi, “Detection and Classification of Driving Maneuver Events for Automatic Lane Map Generation”, 27th IEEE International Conference on Intelligent Transporation Systems, September 24-27, 2024, Edmonton, Canada[^labic]

**2023**

- Byungjun Kim, and Seibum B. Choi, “Terminal iterative learning control for an electrical powertrain system with backlash”, 2023 IEEE International Conference on Systems, Man, and Cybernetics (SMC), Maui, USA, 2023[^labic]

**2022**

- Jongyong Do, Kyoungseok Han, and Seibum B. Choi, “Inference of Vehicle Lane Change Intention Using Multiple Model Estimator in Automated Highway Driving”, IEEE, in Proceeding of 22nd International Conference on Control, Automation and Systems (ICCAS), Nov. 27- Dec. 1, 2022, BEXCO, Busan, Korea[^labic]

### 국내 학회 발표

**2026**

- 정태우, 김병준, 김동현, 김진욱, 최세범, “볼-램프 듀얼 클러치 트랜스미션을 활용한 저단 변속에서의 클러치 토크 추정”, 2026 한국자동차공학회 춘계학술대회[^labdc]

**2025**

- 정세민, 오지열, 최세범, “트레일러 센서 부재 환경을 고려한 트레일러 스윙 감지 알고리즘”, 2025 한국자동차공학회 추계학술대회[^labdc]
- 전진환, 최세범, “도로 네트워크 분할 기반의 효율적인 대규모 정밀지도 원호 매개변수화 기법”, 2025 한국자동차공학회 춘계학술대회[^labdc]

**2024**

- 오지열, 최세범, 정상훈, “대역통과필터 기반 차량 질량 추정 알고리즘”, 2024 한국자동차공학회 추계학술대회[^labdc]
- 임채호, 전진환, 황윤진, 최세범, “원호 스플라인 근사를 이용한 주행 기동 이벤트의 감지 및 분류”, 2024 한국자동차공학회 춘계학술대회[^labdc]

**2023**

- 고건희, 최세범, “충돌 방지를 위한 오버슈트가 없는 FRACC(Full-range Adaptive Cruise Control) 시스템 설계”, 2023 한국자동차공학회 추계학술대회[^labdc]
- 전진환, 황윤진, 최세범, “멀티모달 센서퓨전 기반 차량 주행 기록 복원”, 2023 한국자동차공학회 춘계학술대회[^labdc]
- 오지열, 최세범, “대형트럭 보조 브레이크 시스템을 위한 브레이크 잠김 방지 시스템”, 2023 한국자동차공학회 대전∙세종∙충청지회 춘계학술대회[^labdc]

**2022**

- 김승택, 한경석, 최세범, “긴급 충돌 회피를 위한 비선형 모델 예측 제어 기반 조향 및 브레이크 통합 제어”, 2022 한국자동차공학회 추계학술대회[^labdc]
- 오지열, 최세범, “타이어-차량 인터랙티브 모델 기반 인휠 모터 차량의 요레이트 제어”, 2022 한국자동차공학회 춘계학술대회[^labdc]

**2021**

- 이해우, 최세범, “자동변속기 락업클러치의 모델 예측 슬립 제어”, 2021 한국자동차공학회 추계학술대회[^labdc]
- 신승인, 최세범, “습식 클러치 특성 시험 장치 설계”, 2021 한국자동차공학회 대전∙세종∙충청지회 춘계학술대회[^labdc]
- 도종용, 최세범, 현동윤, “타이어의 동적 특성을 반영한 종방향 타이어 강성계수 추정”, 2021 한국자동차공학회 춘계학술대회[^labdc]

## 과제

누리집 Projects는 Active Projects에 4개, Previous Projects에 55개 과제를 게시한다. 아래는 해당 구획과 기간·기관을 그대로 옮긴 목록이다. 종료일이 없는 기간은 임의로 채우지 않았다. 기관은 누리집에 적힌 지원 기관 표기이며 발주·수행 관계를 별도 원부로 확인한 것은 아니다.[^projects]

### Active Projects 구획

| 과제명 | 기간(게시 표기) | 지원 기관(게시 표기) |
|---|---|---|
| 거점기반 Lv.4+ 자율주행 대형트럭 차량플랫폼 기술개발 | 2022.04 - | 스카이오토넷 |
| 구동 및 조향 일체형 플러그앤 드라이브 모듈 기술 개발 | 2023.04 - | 에이치엘만도 |
| 인프라 기반의 ADAS를 위한 정밀 차선 지도의 자동 생성 및 자동 갱신 알고리즘 개발 | 2024.05 - | 연구재단 |
| xEV 차량의 견인 모드 주행 안정성 향상을 위한 제어 알고리즘 개발 | 2024.03 - | 현대자동차 |

### Previous Projects 구획

| 과제명 | 기간(게시 표기) | 지원 기관(게시 표기) |
|---|---|---|
| AGV/AMR 스마트 예지 시스템 | 2025.07 – 2026.07 | 티로보틱스 |
| 순간 토크 프로파일을 이용한 노면 최적 슬립 타겟 생성 | 2025.07 – 2026.07 | 현대자동차 |
| 캐빈교체형 자율셔틀 공용섀시플랫폼 기술 개발 | 2021.04 – 2025.03 | 한국자동차연구원 |
| 주행 중 감쇠력 튜닝이 가능한 전기차용 스마트 댐퍼 시스템 개발 | 2022.04 – 2025.03 | 네오테크 |
| 전기자동차 구동계의 충격 저감을 위한 백래시 추정 알고리즘과 최적 토크 프로파일 생성 | 2023.04 – 2024.04 | 현대자동차 |
| 주행성능 확보를 위한 구동 조향 통합형 독립조향 구동 매커니즘 개발 | 2023.04 – 2024.03 | 현대자동차 |
| Multi EXV 시스템 모델링 모델 기반 관측기 개발 및 제어 | 2022.05 – 2022.09 | 한온시스템 |
| 휴대성과 편리성이 강화된 휠체어 전동화 키드 UX 환경개선 및 사업화모델 혁신디자인 개발 | 2020.04 – 2022.12 | (주)아이디썸 |
| 자기강화 원리를 이용한 초고효율 동력전달장치의 기계특성기반 고효율 변속 제어기 및 고성능 상태 추정기 개발 | 2020.03 – 2022.02 | 한국연구재단 |
| 대용량 BRT 파라미터 추정과 주행 최적 경로 생성 | 2019.04 – 2021.12 | 한국철도기술연구원 |
| 자기강화 원리를 이용한 초고효율 동력 전달 및 제어 장치에 관한 연구 | 2017.03 – 2020.02 | 한국연구재단 |
| 타이어 마모 미세먼지 발생량 평가용 주행모드 개발 | 2021.06 – 2021.10 | 한국자동차연구원 |
| 운전자 맞춤 가감속 패턴 도출 | 2020.09 – 2021.08 | Hyundai motors corp . |
| 신규 댐퍼클러치 제어로직 개발(2020년도) | 2020.03 – 2021.02 | Hyundai motors corp . |
| 항복강도 60kPa급 MR물질을 활용한 차량용 쇽업소버(댐퍼)및 엔진마운트 개발 | 2017.11 – 2020.12 | 알엠에스테크놀러지(주) |
| 브레이크-바이-와이어성능향상위한타이어강성계수실시간추정로직개발(2019) | 2019.11 – 2020.10 | Hyundai motors corp . |
| HK i-Tire 하중/마모 예측 기술 개발 | 2017.05 – 2020.08 | 한국타이어 테크노돔 |
| 습식 DCT의 전달 토크 특성 분석 및 시스템 모델링, 강건 토크 추종 제어기 개발 | 2017.04 – 2020.05 | Hyundai motors corp . |
| 자동변속기 모델 기반 변속 제어 연구(2019) | 2019.03 – 2020.02 | Hyundai motors corp . |
| 자기강화 원리를 이용한 초고효율 동력 전달 및 제어 장치에 관한 연구(2017) | 2017.03 – 2020.02 | 한국연구재단 |
| 모델기반 BBW 고장 진단 알고리즘 기술 개발(2018) | 2018.11 – 2019.10 | Hyundai motors corp . |
| AGV Suspension 기술 개발 | 2019.02 – 2019.08 | 엘지전자(주) |
| 토크관측기를 이용한 건식 클러치 전달토크 모델링 및 제어 | 2017.06 – 2019.06 | Hyundai motors corp . |
| 모델기반 변속 상태 추정 및 강건 제어기 설계 연구(2017) | 2017.03 – 2018.12 | 국방과학연구소 |
| 실시간 차량 무게 중심 높이 추정 알고리즘 개발(2017년)(2017) | 2017.11 – 2018.10 | Hyundai motors corp . |
| 하이브리드 4륜 구동 시스템의 ABS/TCS 제어 알고리즘 개발 | 2016.07 – 2018.06 | Hyundai motors corp . |
| 차체 거동 센서 및 휠가속도센서를 이용한 가변댐퍼의 상대속도 추정로직 개발 | 2017.07 – 2018.01 | Hyundai motors corp . |
| 센서융합 기반 차량 상태 추정 로직 개발 | 2016.11 – 2017.10 | Hyundai motors corp . |
| 사용자 니즈를 반영한 3륜 Micro-모빌리티 사업 | 2015.06 – 2017.05 | (주)영신테크 |
| Integrated vehicle chassis | 2012.03 – 2017.02 | Personal plug & play digital electric car research center |
| 전동식 브레이크 패드 마찰 계수 추정 알고리즘 개발 | 2015.11 – 2016.10 | Hyundai motors corp . |
| 구동력 및 주행 안정성 향상을 위한 1,300Nm급 전동유압 모듈화방식 AWD 시스템 및 제어기술 개발 | 2014.10 – 2016.05 | 인팩 |
| 친환경 저소음 전동 레저카트 개발 및 상용화전략 수립 | 2015.07 – 2015.11 | KAIST |
| 전동식 브레이크 클램핑력 추정 알고리즘 개발 | 2014.11 – 2015.10 | Hyundai motor corp. |
| 센서기반 전동형 댐퍼 및 차량용 능동 샤시 모듈 개발 | 2013.09 – 2018.08 | 화신Eng. |
| 자기강화 원리를 이용한 초 고효율 클러치 액츄에이터 기술 사업화 | 2014.07 – 2014.12 | KAIST |
| Airbag algorithm development for integrated vehicle chassis control | 2014.01 – 2014.09 | Infobank. |
| Development of Braking/Driving torque estimation for Vehicle State Observers | 2013.11 – 2014.10 | Hyundai motor corp. |
| Integrated control based on low-temperatue combution engine model for heavy industries | 2009.06 – 2014.05 | Doosan infracore |
| Development of control logic for dry dual-clutch module | 2011.06 – 2013.02 | PHC Valeo |
| Development of integrated 0drivnig-braking control for handling performance | 2012.09 – 2013.08 | Hyundai motors corp . |
| 자율주행자동차 경진대회 차량제작 지원 | 2011.07 – 2012.10 | Hyundai motors corp . |
| Development of vehicle longitudinal controller | 2009.12 – 2012.03 | Hyundai motors corp. |
| 개인용 플러그 앤 플레이 디지털 전기자동차 연구 | 2011.03 – 2012.02 | 한국연구재단 |
| Development of x-by wire system integrated with driving condition/vehicle information | 2010.04 – 2012.03 | Hyundai motors corp. |
| Evaluation and design for driving performance of diesel-hybrid bus | 2010.05 – 2012.04 | KIMM |
| EWB(Electronic Wedge Brake) System development for brake-by-wire system | 2008.06 – 2012.05 | Mando |
| Development of green car regenerative-braking reliabilty evaluation techniques | 2009.06 – 2012.05 | KATECH |
| Recognition of vehicle on/off condition for pro-active idle-stop based on ranging sensor in driving | 2008.03 – 2010.01 | ETRI |
| 온라인전기자동차 동역학 특성연구 | 2009.05 – 2009.12 | KAIST |
| Development of crash algorithm based on crash prediction data | 2008.04 – 2009.08 | Hyundai Motors corp. |
| Development of roll over prevention control logic | 2007.03 – 2008.02 | Hyundai Mobis |
| Development of driver model for lateral vehicle dynamics | 2007.10 – 2008.09 | HankookTire |
| Light vehicle with active safety | 2007.10 – 2008.05 | Clean energy research center, KAIST Institute |
| Development of integrated control algorithm for variable wheeled platform | 2007.09 – 2008.09 | ADD |

## 연락과 위치

- 연구실: N7-5동 203호, 대전광역시 유성구 대학로 291[^intro]
- 교수 연구실: 기계동(N7) 5105호[^mep]
- 전화: 연구실 042-350-4160, 교수 042-350-4120, 팩스 042-350-4110[^intro][^prof][^mep]
- 교수 이메일: sbchoi@kaist.ac.kr[^mep][^fv]
[^p1]: J. Lee, Y. Hwang, S. B. Choi, IEEE Transactions on Vehicular Technology 72, 15301-15316 (2023). <https://doi.org/10.1109/tvt.2023.3292616> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: G. Ko, S. B. Choi, IEEE Transactions on Intelligent Vehicles 11, 857-868 (2026). <https://doi.org/10.1109/tiv.2026.3693769> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: H. Lee, S. Choi, IEEE Transactions on Intelligent Transportation Systems 25, 21327-21342 (2024). <https://doi.org/10.1109/tits.2024.3454803> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: S. Kim, K. Han, S. B. Choi, IEEE Transactions on Intelligent Vehicles 9, 2908-2922 (2024). <https://doi.org/10.1109/tiv.2023.3309962> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. Do, K. Han, S. B. Choi, IEEE Transactions on Intelligent Vehicles 8, 3813-3825 (2023). <https://doi.org/10.1109/tiv.2023.3266102> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: T. Lee, S. B. Choi, IEEE Transactions on Vehicular Technology 72, 8647-8660 (2023). <https://doi.org/10.1109/tvt.2023.3246179> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: D.-H. Kim, S. B. Choi, IEEE Transactions on Control Systems Technology 31, 1220-1234 (2023). <https://doi.org/10.1109/tcst.2022.3215840> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: K. Jeong, S. B. Choi, IEEE Transactions on Control Systems Technology 30, 1723-1735 (2022). <https://doi.org/10.1109/tcst.2021.3123611> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 차량 제어 연구실 누리집 첫 화면 <https://acl.kaist.ac.kr/> (누리집 이름 ACL – Automotive Control Lab, 2026-10-23 열람)
[^intro]: 같은 누리집 Introduction 페이지 <https://acl.kaist.ac.kr/introduction/> (연구실 설립, 연구 관심, 위치, 전화, 2026-10-23 열람)
[^prof]: 같은 누리집 Professor 페이지 <https://acl.kaist.ac.kr/professor/> (직위, 연구 관심, 연락처, 학력, 경력, 업무 경험, 학회 활동, 수상, 2026-10-23 열람)
[^me]: KAIST 기계공학과 연구분야 연구실 명단 <https://me.kaist.ac.kr/research/research_010100.html> (최세범 교수 항목: 연구주제, 주요 응용 산업, 연구실 이름, 웹사이트, 2026-10-23 열람)
[^mefac]: KAIST 기계공학과 교수진 목록 2쪽 <https://me.kaist.ac.kr/team/team_010100.html?page=2&plist=&find_field=&find_word=&find_state=&find_ordby=&conf=&mode=1> (최세범 교수 항목: 연구분야, 연구실, 최종학위, 2026-10-23 열람)
[^mep]: KAIST 기계공학과 교수 상세(최세범) <https://me.kaist.ac.kr/pop/team.html?uid=58&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 연구실 웹사이트, 이메일, 사무실, 전화, 2026-10-23 열람)
[^fv]: KAIST 미래자동차학제전공 교수진 <https://fv.kaist.ac.kr/index.php?mid=fv01_03> (최세범 교수 항목: 소속학과, 주요연구분야, 전화, 이메일, 웹사이트, 2026-10-23 열람)
[^cr]: 2021–2026년 논문의 출판사 등록 서지(Crossref) <https://api.crossref.org/> (저자 확인 기준은 근거 페이지, 2026-10-23 조회)

[^students]: ACL Students 구성원 <https://acl.kaist.ac.kr/students/> (2026-10-25 열람)
[^postdoc]: ACL Postdoc 구성원 <https://acl.kaist.ac.kr/postdoc/> (2026-10-25 열람)
[^alumni]: ACL Alumni 졸업생 진로 <https://acl.kaist.ac.kr/alumni/> (2026-10-25 열람)
[^labij]: ACL 국제 학술지 목록 <https://acl.kaist.ac.kr/international-journal/> (2026-10-25 열람)
[^labic]: ACL 국제 학회 목록 <https://acl.kaist.ac.kr/international-conference/> (2026-10-25 열람)
[^labdj]: ACL 국내 학술지 목록 <https://acl.kaist.ac.kr/domestic-journal/> (2026-10-25 열람)
[^labdc]: ACL 국내 학회 목록 <https://acl.kaist.ac.kr/domestic-conference/> (2026-10-25 열람)
[^projects]: ACL 과제 목록 <https://acl.kaist.ac.kr/projects/> (2026-10-25 열람)
[^topics]: ACL 연구 주제 목차 <https://acl.kaist.ac.kr/research-topics/> (2026-10-25 열람)
[^dct]: ACL 듀얼 클러치 변속기 연구 소개 <https://acl.kaist.ac.kr/research-dual-clutch-transmission-dct/> (2026-10-25 열람)
[^diesel]: ACL 디젤 엔진 제어 연구 소개 <https://acl.kaist.ac.kr/research-diesel-engine-control-ltc-mode/> (2026-10-25 열람)
[^camless]: ACL 캠리스 엔진 연구 소개 <https://acl.kaist.ac.kr/camless-engine/> (2026-10-25 열람)
[^isg]: ACL 공회전 정지·재시동 연구 소개 <https://acl.kaist.ac.kr/research-idle-stop-and-go/> (2026-10-25 열람)
[^precrash]: ACL 충돌 전 감지와 제어 연구 소개 <https://acl.kaist.ac.kr/research_pre-collision-detection-and-control/> (2026-10-25 열람)
[^light]: ACL 경량 차량 안전 연구 소개 <https://acl.kaist.ac.kr/research_light-vehicle-safety/> (2026-10-25 열람)
[^abs]: ACL 바퀴 잠김 방지 제어 연구 소개 <https://acl.kaist.ac.kr/research_advanced-abs/> (2026-10-25 열람)
[^driver]: ACL 운전자 모형 연구 소개 <https://acl.kaist.ac.kr/research_human-driver-model/> (2026-10-25 열람)
[^ewb]: ACL 전자식 쐐기 브레이크 연구 소개 <https://acl.kaist.ac.kr/research_electronic-wedge-brake/> (2026-10-25 열람)

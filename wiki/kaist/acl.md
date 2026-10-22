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

## 최근 논문 목록 (2021–2026)

최세범 교수가 저자로 참여한 2021–2026년 학술지 논문 59편과 학회 논문 7편이다. 저자·제목·학술지·학회 표기는 출판사가 등록한 서지를 따랐다.[^cr]

**2026**

- Byungjun Kim, Seibum B. Choi, Sooyoung Kim. "Optimal input shape terminal iterative learning control for robust backlash mitigation in EV powertrains". *Control Engineering Practice*.
- Yuntae Kim, Byungjun Kim, Dasol Jeong, Hyuck-Kee Lee, Seibum B. Choi. "Energy-Based Adaptive Cruise Control With Structurally Induced Self-Excited Driving for Car-Following". *IEEE Transactions on Intelligent Transportation Systems*.
- Taewoo Jeong, Byungjun Kim, Dong-Hyun Kim, Jinwook Kim, Seibum B. Choi. "Power-on Downshift with Clutch Kissing Point Detection utilizing Ball-Ramp Dual Clutch Transmission Asymmetry". *2026 IEEE Conference on Control Technology and Applications (CCTA)*.
- Geonhee Ko, Seibum B. Choi. "Collision-Free Adaptive Cruise Control via a Risk Holding Strategy Based on a Generalized Risk Framework". *IEEE Transactions on Intelligent Vehicles*.
- Byungjun Kim, Yuntae Kim, Seibum B. Choi, Sooyoung Kim. "Relative velocity estimation for semi-active suspension with disturbance-decoupled Kalman filtering using production vehicle sensors". *Proceedings of the Institution of Mechanical Engineers, Part D: Journal of Automobile Engineering*.
- Geonhee Ko, Seibum B. Choi. "Priority-Aware Tracking of Infeasible Trajectories via Smooth Input Saturation and Asymmetric Control Structure". *International Journal of Automotive Technology*.
- Jinhwan Jeon, Seibum B. Choi. "Tree-Structured Recursive Arc Spline Approximation of Complex Lane-Level Maps with G1 Continuity". *International Journal of Automotive Technology*.
- Jinwook Kim, Seibum B. Choi. "Machine Learning Based Drive Fault Diagnosis and Isolation Algorithm for 4WIS4WID Vehicle Using Residual Visualization". *IEEE Transactions on Intelligent Vehicles*.
- Byungjun Kim, DongHyun Kim, Seibum B. Choi, Jonghyup Lee. "Model-Based Optimal Anti-jerk Control for Electric Vehicle Powertrain with Backlash". *International Journal of Control, Automation, and Systems*.
- Chaeho Lim, Seonggyeong Ju, Yunjeong Hwang, Hanseon Ga, Jinseok Song, Seibum B. Choi, Sooyoung Kim. "Regenerative braking torque control with tire-force-based limiting for vehicle stability of a front-rear motor-driven EV". *Control Engineering Practice*.
- Seungtaek Kim, Jonghyup Lee, Kyoungseok Han, Seibum B. Choi. "Bridging the Sim-to-Real Gap: A Control Framework for Imitation Learning of Model Predictive Control". *International Journal of Control, Automation, and Systems*.

**2025**

- Yuntae Kim, Yoonjin Hwang, Seibum B. Choi. "Damper Mode Change Based on Driving Condition Recognition for Semi-active Suspension on Random Road Profile". *International Journal of Automotive Technology*.
- Jinhwan Jeon, Seibum B. Choi. "Efficient Arc Spline Approximation of Large Sized Complex Lane-Level Road Maps". *IEEE Transactions on Intelligent Transportation Systems*.
- Seungtaek Kim, Kyoungseok Han, Seibum B. Choi. "Approximate Robust Tube Nonlinear Model Predictive Control for Vehicle Collision Avoidance". *2025 IEEE Conference on Control Technology and Applications (CCTA)*.
- Haewoo Lee, Seibum B. Choi. "Emergency Lane Change Trajectory Planning for High Center of Gravity Vehicles using Time-Domain Dual Connecting Points Optimization". *2025 IEEE Conference on Control Technology and Applications (CCTA)*.
- Haewoo Lee, Seibum B. Choi. "Path Planning Using Dual Connecting Points Optimization for Emergency Collision Avoidance". *IEEE Transactions on Intelligent Vehicles*.

**2024**

- Byungjun Kim, Seibum B. Choi. "Iterative Learning Control for Linear Hybrid System with Iteration-Varying References". *2024 6th International Conference on Control and Robotics (ICCR)*.
- Hwangjae Lee, Seibum Choi. "Development of Collision Avoidance System Integrated With Real-Time Tire-Road Friction Coefficient Estimator". *IEEE Transactions on Intelligent Transportation Systems*.
- Jiyeol Oh, Seibum B. Choi. "Optimal tongue weight selection criteria for light vehicle-trailer combinations". *Vehicle System Dynamics*.
- Jinhwan Jeon, Chaeho Lim, Yoonjin Hwang, Seibum B. Choi. "Detection and Classification of Driving Maneuver Events for Automatic Lane Map Generation". *2024 IEEE 27th International Conference on Intelligent Transportation Systems (ITSC)*.
- Jinhwan Jeon, Yoonjin Hwang, Seibum B. Choi. "Reliability-based G1 continuous arc spline approximation". *Computer Aided Geometric Design*.
- Seungin Shin, Seibum B. Choi. "Control-oriented modeling of wet clutch friction considering thermal dynamics". *Mechatronics*.
- Jongyong Do, Dongyoon Hyun, Kyoungseok Han, Seibum B. Choi. "Real-time estimation of longitudinal tire stiffness considering dynamic characteristics of tire". *Mechatronics*.
- Hyungjeen Choi, Seibum Choi. "Design of the Steering Feedback Controller of a Steer-by-Wire System Using Admittance Model". *International Journal of Automotive Technology*.
- Dasol Jeong, Seibum B. Choi. "Efficient Trajectory Planning for Autonomous Vehicles Using Quadratic Programming With Weak Duality". *IEEE Transactions on Intelligent Vehicles*.
- Seungtaek Kim, Kyoungseok Han, Seibum B. Choi. "Imitation Learning of Nonlinear Model Predictive Control for Emergency Collision Avoidance". *IEEE Transactions on Intelligent Vehicles*.
- Yuntae Kim, Seibum B. Choi, Jiwon J. Oh, Jeongsoo Eo. "Satisfactory Driving Mode Classification Based on Pedal Operation Characteristics". *IEEE Transactions on Intelligent Vehicles*.
- Dasol Jeong, Seibum B. Choi. "Tube-Based Robust Model Predictive Control for Tracking Control of Autonomous Articulated Vehicles". *IEEE Transactions on Intelligent Vehicles*.
- Seungtaek Kim, Jonghyup Lee, Kyoungseok Han, Seibum B. Choi. "Vehicle Path Tracking Control Using Pure Pursuit With MPC-Based Look-Ahead Distance Optimization". *IEEE Transactions on Vehicular Technology*.

**2023**

- Jonghyup Lee, Yoonjin Hwang, Seibum B. Choi. "Robust Tube-MPC Based Steering and Braking Control for Path Tracking at High-Speed Driving". *IEEE Transactions on Vehicular Technology*.
- Byungjun Kim, Seibum B. Choi. "Terminal Iterative Learning Control for an Electrical Powertrain System with Backlash". *2023 IEEE International Conference on Systems, Man, and Cybernetics (SMC)*.
- Dong-Hyun kim, Seibum B. Choi. "Composite Control Law for Nonlinear Systems With Mismatched Disturbances for a Ball-Ramp Dual-Clutch Transmission". *IEEE Transactions on Intelligent Transportation Systems*.
- Jongyong Do, Kyoungseok Han, Seibum B. Choi. "Lane Change–Intention Inference and Trajectory Prediction of Surrounding Vehicles on Highways". *IEEE Transactions on Intelligent Vehicles*.
- Taeheon Lee, Seibum B. Choi. "Real-Time Optimization of Gear Shift Trajectories Using Quadratic Programming for Electric Vehicles With Dual Clutch Transmission". *IEEE Transactions on Vehicular Technology*.
- Hwangjae Lee, Seibum Ben Choi. "Model Predictive Control Based Multifunctional Advanced Driver-Assistance System Specialized for Rear-End Collision Avoidance". *International Journal of Automotive Technology*.
- Hwangjae Lee, Seibum Ben Choi. "Online Detection of Toe Angle Misalignment Based on Lateral Tire Force and Tire Aligning Moment". *International Journal of Automotive Technology*.
- Dong-Hyun Kim, Seibum B. Choi. "Extended High-Order Disturbance Observer-Based Clutch Actuator Model Uncertainty Estimation of Ball-Ramp Dual-Clutch Transmission". *IEEE Transactions on Control Systems Technology*.
- Jonghyup Lee, Seibum B. Choi. "Integrated Control of Steering and Braking for Path Tracking Using Multi-Point Linearized MPC". *IEEE Transactions on Intelligent Vehicles*.
- Byungjun Kim, Seibum B. Choi, Youngkwon Kim. "Observer-Based Control for a Torque Converter Lock-Up Clutch Utilizing a Steady-State Torque Map". *IEEE Transactions on Control Systems Technology*.
- Ho Jin Jung, Seibum Ben Choi. "Modified Generalised Maxwell Slip Based Electro-Hydraulic Transfer Case Modeling for All-wheel Drive Vehicle Simulation". *International Journal of Automotive Technology*.
- Seungin Shin, Seibum B. Choi. "Observer-based iterative learning control for a high relative degree nonlinear system and its application to a vehicular wet-clutch system". *Mechanism and Machine Theory*.

**2022**

- Seungin Shin, Dong-Hyun Kim, Seibum B. Choi. "Apparatus for Identification of Frictional and Thermal Characteristics of a Wet Clutch". *International Journal of Automotive Technology*.
- Jongyong Do, Kyoungseok Han, Seibum B. Choi. "Inference of Vehicle Lane Change Intention Using Multiple Model Estimator in Automated Highway Driving". *2022 22nd International Conference on Control, Automation and Systems (ICCAS)*.
- Dong‐Hyun Kim, Seibum B. Choi. "Extended disturbance observer for nonlinear system with time‐varying disturbance gain". *International Journal of Adaptive Control and Signal Processing*.
- Dasol Jeong, Seibum B. Choi. "Tracking Control Based on Model Predictive Control Using Laguerre Functions With Pole Optimization". *IEEE Transactions on Intelligent Transportation Systems*.
- Yunhyoung Hwang, Seibum B. Choi. "Awareness on Present and Future Trajectory of Vehicle Using Multiple Hypotheses in the Mixed Traffic of Intersection". *IEEE Transactions on Intelligent Transportation Systems*.
- Dong-Hyun Kim, Seibum B. Choi. "Design of Ball-Ramp dual clutch transmission to reduce uncertainties in clutch actuator and tie-up effect". *Mechanism and Machine Theory*.
- Hwangjae Lee, Seibum Choi. "Development of Collision Avoidance System in Slippery Road Conditions". *IEEE Transactions on Intelligent Transportation Systems*.
- Jonghyup Lee, Seibum Choi. "Nonlinear Model Predictive Control for Path Tracking in High-Speed Corner Entry Situations". *International Journal of Automotive Technology*.
- Yongseop Jeong, Jinsun Park, Donghyeon Cho, Yoonjin Hwang, Seibum B. Choi, In So Kweon. "Lightweight Depth Completion Network with Local Similarity-Preserving Knowledge Distillation". *Sensors*.
- Dasol Jeong, Geonhee Ko, Seibum B. Choi. "Estimation of sideslip angle and cornering stiffness of an articulated vehicle using a constrained lateral dynamics model". *Mechatronics*.
- Kicheol Jeong, Seibum B. Choi. "Takagi–Sugeno Fuzzy Observer-Based Magnetorheological Damper Fault Diagnosis Using a Support Vector Machine". *IEEE Transactions on Control Systems Technology*.
- Yoonjin Hwang, Yongseop Jeong, In So Kweon, Seibum B. Choi. "Identification of Vehicle Dynamics Model and Lever-Arm for Arbitrarily Mounted Motion Sensor". *IEEE Sensors Journal*.
- Jinrak Park, Seibum Choi, Jiwon Oh, Jeongsoo Eo. "Adaptive slip engagement control of a wet clutch in vehicle powertrain based on transmitted torque estimation". *Mechanical Systems and Signal Processing*.
- Taeheon Lee, Dong-Hyun Kim, Seibum B. Choi. "Driveline Modeling With Transmission Loss and Robust Torque Observer Design for Dual Clutch Transmission". *IEEE Transactions on Vehicular Technology*.
- Jinrak Park, Seibum Choi. "Gear Shifting Based on MIMO Model Predictive Control for Convenient Adjustment of Shifting Performance". *IEEE Transactions on Vehicular Technology*.
- Hojin Jung, Dohyun Jung, Seibum B. Choi. "LQR Control of an All-Wheel Drive Vehicle Considering Variable Input Constraint". *IEEE Transactions on Control Systems Technology*.

**2021**

- Dasol Jeong, Seibum B. Choi, Jonghyup Lee, Mintae Kim, Hojong Lee. "Tire dimensionless numbers for analysis of tire characteristics and intelligent tire signals". *Mechanical Systems and Signal Processing*.
- Yoonjin Hwang, Yongseop Jeong, In So Kweon, Seibum Choi. "Online Misalignment Estimation of Strapdown Navigation for Land Vehicle under Dynamic Condition". *International Journal of Automotive Technology*.
- Giseo Park, Seibum B. Choi. "A Model Predictive Control for Path Tracking of Electronic-Four-Wheel Drive Vehicles". *IEEE Transactions on Vehicular Technology*.
- Jinhwan Jeon, Yoonjin Hwang, Yongseop Jeong, Sangdon Park, In So Kweon, Seibum B. Choi. "Lane Detection Aided Online Dead Reckoning for GNSS Denied Environments". *Sensors*.
- Giseo Park, Seibum B. Choi. "An Integrated Observer for Real-Time Estimation of Vehicle Center of Gravity Height". *IEEE Transactions on Intelligent Transportation Systems*.
- Kyoungseok Han, Giseo Park, Gokul S. Sankar, Kanghyun Nam, Seibum B. Choi. "Model Predictive Control Framework for Improving Vehicle Cornering Performance Using Handling Characteristics". *IEEE Transactions on Intelligent Transportation Systems*.
- Jinrak Park, Seibum Choi. "Optimization Method of Reference Slip Speed in Clutch Slip Engagement in Vehicle Powertrain". *International Journal of Automotive Technology*.
- Min-Hyun Kim, Jongchan Park, Seibum Choi. "Road Type Identification Ahead of the Tire Using D-CNN and Reflected Ultrasonic Signals". *International Journal of Automotive Technology*.
- Dasol Jeong, Seungtaek Kim, Jonghyup Lee, Seibum B. Choi, Mintae Kim, Hojong Lee. "Estimation of Tire Load and Vehicle Parameters Using Intelligent Tires Combined With Vehicle Dynamics". *IEEE Transactions on Instrumentation and Measurement*.

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

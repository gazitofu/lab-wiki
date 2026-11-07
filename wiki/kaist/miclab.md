# Mobility Intelligence and Control Laboratory (MIC Lab)

**KAIST 조천식모빌리티대학원 · 최경환 조교수**

- 분야: 학습 기반 최적 제어, 차량 운동 제어, 전동기 구동 제어, 차량 에너지·열 관리
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 제어 이론·제어 공학[^themes][^control], 강화학습[^themes], 차량 동역학·섀시 제어[^vehicle], 전동기·발전기 설계·구동 제어[^component], 전기차[^control]
- 영문 이름: Kyunghwan Choi
- 홈페이지: <https://kaist-mic-lab.github.io>
- 근거와 출처: [MIC Lab 근거 페이지](miclab-sources.md)

> 차량이 주행하고 에너지를 쓰는 방법을 수학적으로 정하고, 실제 운전 중 들어오는 정보로 제어기와 차량 모형을 갱신하는 연구실이다. 전동기부터 차량 전체, 도로와 연결된 이동 체계까지 함께 다룬다.[^home][^themes][^control]

## 무엇을 연구하나

MIC Lab은 최경환 교수가 이끄는 모빌리티(사람과 물건의 이동 수단과 그 체계) 지능·제어 연구실이다. 연결·자동화·전동화된 차량을 대상으로 최적 제어(시스템의 변화와 제약을 고려해 정한 성능 기준을 가장 좋게 하는 입력을 구하는 방법)와 학습 기반 제어를 연구한다.[^profile] 연구 대상은 도로·교통 정보를 사용하는 이동 체계, 조향·제동·구동 장치를 함께 움직이는 차량, 전동기의 전압·전류·회전력을 다루는 부품으로 나뉜다.[^control] 전압은 전하를 이동시키는 전기적 위치 에너지 차이이고, 전류는 단위 시간에 흐르는 전하량이며, 전하는 전기적 상호작용을 결정하는 물질의 성질이다. 회전력은 힘과 회전축에서 그 힘의 작용선까지의 수직 거리에 따라 정해지는 회전 작용의 양이다.

공통 질문은 측정한 정보를 바탕으로 어떤 입력을 가해야 에너지 사용, 주행 오차, 승차감 같은 성능 기준을 만족하면서 물리적 한계와 안전 제약을 지킬 수 있는가이다. 차량 수준에서는 구동·제동·조향·현가 장치의 동작을 조정하고, 부품 수준에서는 전동기의 전압이나 전력 변환 장치의 스위칭을 정해 전류와 회전력을 제어한다. 전기차 구동계의 제어와 자동화된 차량의 움직임을 서로 다른 수준의 최적 제어 문제로 다룬다.[^control] 현가 장치는 차체와 바퀴 사이에서 하중을 지지하고 노면 충격과 진동을 전달·완화하는 장치이며, 스위칭은 전기적 연결 상태를 바꾸는 동작이다.

연구의 다른 축은 제어에 필요한 모형·상태·가치·정책을 운전 중 학습하는 일이다. 온라인 학습은 운영 중 들어오는 자료로 학습 모형을 갱신하는 방법이다. 연구실은 강화학습(Reinforcement Learning, 시행착오에서 얻은 보상을 바탕으로 행동 규칙을 배우는 기계학습 방법)을 통해 실제 상태 변화에서 가치와 행동 규칙을 배우고, 물리 정보를 이용해 동역학 모형을 갱신하며, 측정값에서 현재 상태를 추정하는 방법을 개발한다.[^themes] 가치와 정책을 근사하는 일, 모형을 학습하는 일, 두 역할을 결합하는 일을 구분한다.[^themes] 여기서 상태는 시스템의 현재 상황을 표현하는 변수들의 묶음이고, 정책은 상태나 관측 정보에 따라 행동을 정하는 규칙이다.

이 연구는 계산량과 정보 부족이라는 두 문제를 함께 다룬다. 긴 시간 범위의 최적 행동을 매번 계산하기 어렵거나, 차량의 성질과 운전 환경이 정확히 알려져 있지 않고 계속 변할 수 있기 때문이다. 학습한 가치나 정책으로 계산을 근사하고, 새 측정값을 이용해 필요한 모형과 상태 정보를 보완한다. 모든 학습 제어기가 자동으로 최적이거나 안전하다고 전제하지 않으며, 학습 대상·정보 가정·안정성·제약 충족과 실제 성능을 각각 따지는 연구 틀을 제시한다.[^control][^themes]

## 주요 연구 주제

### 실제 운전 중의 강화학습과 앞날을 내다보는 제어

강화학습은 실제로 관측한 상태 변화에서 이후의 가치를 학습하는 데 쓰인다. 연구실은 가치 추정과 정책 갱신을 함께 수행하는 방법, 가치 추정은 고정한 채 여러 단계 앞의 행동을 계산해 현재 행동을 개선하는 방법을 구분한다. 의미 정보를 이용하는 갈래에서는 시각·언어 모형이나 언어 모형이 추출한 과제 관련 정보를 가치 학습에 반영하고 이어 정책을 개선한다. 시간에 따라 조건이 변하는 문제에서는 충분한 환경 정보를 상태에 더했을 때 시간에 무관한 형태의 최적 제어 문제로 바꿀 수 있는 조건을 다룬다.[^themes]

대표 논문 5는 미지의 외부 영향이 있는 위치 제어 장치에서 동역학을 추정하고, 행동을 정하는 신경망과 이후의 가치를 추정하는 신경망을 함께 갱신한다. 신경망은 연결된 계산 단위와 그 연결에 부여한 값을 이용해 입력에서 출력을 만드는 학습 모형이다. 시뮬레이션(수학 모형으로 대상의 동작을 계산해 보는 방법)에서 시간에 따라 달라지는 외부 영향 아래의 추종 제어를 다뤘다.[^p5]

### 차량 운동과 타이어 모형의 학습

차량 수준의 연구는 조향·구동·제동·현가 장치를 함께 조정하는 운동 제어와, 운전 조건에 따라 제어기의 설정값을 맞추는 과정을 다룬다.[^vehicle] 대표 논문 3은 타이어 힘을 직접 측정하지 않고 차량의 옆 방향 움직임과 회전 움직임의 오차로 앞·뒤 타이어의 옆 방향 힘 모형을 갱신한다. 신경망이 현재의 수정 정보를 만들고 표 형태의 저장 공간이 이전에 학습한 관계를 보존해, 미래의 여러 움직임을 계산하는 차량 제어에 재사용하도록 했다.[^p3]

대표 논문 4는 모든 바퀴의 방향을 조절하는 차량에 수축 이론(서로 다른 초기 조건에서 시작한 시스템의 움직임 사이 간격이 줄어드는 성질을 다루는 이론)과 신경망을 결합했다. 차량 모형의 불확실성을 신경망으로 근사·보상하고, 신경망의 값을 갱신하는 규칙과 제어 안정성을 분석했다. 검증은 수치 시뮬레이션으로 제시했다.[^p4]

### 물리 제약을 지키는 전동기 모형과 적응 제어

부품 수준의 연구는 전동기와 그 전력 변환 장치를 대상으로, 상위 제어기가 요청한 회전력을 전압과 스위칭 입력으로 구현하는 방법을 다룬다.[^component] 전류·전압·온도 등의 한계 안에서 회전력 추종과 구동 손실을 함께 고려하며, 제어기와 추정기의 설정값을 실제 장치의 응답에 맞게 조정하는 과정도 연구 대상으로 삼는다. 장기간 운전의 영향을 학습하는 방법과 이전 학습을 보존하는 방법은 연구 확장 방향으로 제시한다.[^component]

동기전동기(회전하는 자기장과 같은 속도로 도는 전동기)는 전기차의 구동 부품 연구 대상이다.[^control][^p6] 자기장은 자석이나 전류가 자기적 힘을 미치는 공간의 상태다. 연구실은 새 운전 자료로 동역학 모형을 학습하면서 이전에 학습한 제어 관련 특성을 유지하는 방법, 물리 조건을 학습의 명시적 제약으로 넣는 방법, 측정 결과를 입력 결정에 되돌려 쓰는 피드백 과정에서 신경망 제어기를 직접 적응시키는 방법을 연구한다. 환경 조건을 추정해 미리 학습한 가치 모형을 재구성하는 방법도 주요 갈래다.[^themes]

대표 논문 6은 전동기 권선의 쇄교자속(도선을 감은 각 부분을 통과하는 자기선속을 모두 더한 양)을 운전 중 학습하는 모형을 제안했다. 자기선속은 면을 통과하는 자기장의 양을 나타내는 물리량이다. 물리 법칙과 모형의 제약을 지키도록 신경망의 갱신 규칙을 구성하고 동기전동기 구동 시뮬레이션으로 평가했다.[^p6] 대표 논문 7은 전압 제약을 제약 최적화 문제에 넣어 신경망 적응 제어기의 갱신 규칙을 도출하고, 전동기의 성질이 정확히 알려져 있지 않은 조건에서 추종 오차와 제약 충족을 분석했다.[^p7]

대표 논문 2는 전동기의 기존 동역학 방정식과 쇄교자속 표를 국소 모형과 추정기로 바꿔, 전동기 성질의 변화에 대응하면서 여러 최적 운전 방식을 함께 다루는 예측 회전력 제어를 제안했다. 실험과 수치 시뮬레이션으로 방법을 평가했다.[^p2]

### 도로 구간을 이용한 에너지 관리

이동 체계 수준에서는 도로·교통·주변 환경 정보를 이용해 주행 전체의 에너지와 열 관리를 계획한다.[^mobility] 대표 논문 1은 차량의 상세한 미래 움직임 대신 도로 구간별 에너지 수요와 이동 시간을 예측하도록 에너지 관리 문제를 재구성했다. 실제 자료에 기초한 지도 정보와 경로 복원 방법으로 예측에 필요한 정보를 구성하고, 시뮬레이션에서 그 예측을 이용한 에너지 관리의 최적성 손실(전체를 가장 좋게 했을 때보다 나빠진 정도)을 평가했다.[^p1]

## 대표 논문

KAIST 재직 시기의 2025–2026년 논문 가운데 이동 체계의 에너지 관리, 차량 운동, 전동기 제어, 온라인 학습 갈래를 고르게 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자와 교수 역할 |
|---|---|---|---|---|
| 1 | 2026 | [Synthesis of a Link-Level Energy-Time Predictor Toward the Implementation of a Link-Based Predictive EMS](https://doi.org/10.1109/access.2026.3726602) · IEEE Access | 차량의 미래 움직임을 세밀하게 예측하는 대신 도로 구간별 에너지 수요와 이동 시간을 예측해 에너지 관리를 수행한다. 예측 문제를 이 두 변수로 재구성하고, 지도 정보와 경로 복원 방법을 이용한 예측 모형을 개발했다. 시뮬레이션에서 최적성 손실 1.91%를 보고했다.[^p1] | 1저자 Geunyoung Park · 최경환 중간 저자 · 마지막 저자 Dongsuk Kum |
| 2 | 2026 | [Model-Adaptive Predictive Torque Control of IPMSMs for Online Optimal Operation: A Lookup-Table-Free Approach](https://doi.org/10.1109/tte.2026.3695345) · IEEE Transactions on Transportation Electrification | 전동기 성질이 달라져도 여러 최적 운전 방식을 함께 다루는 예측 회전력 제어를 제안했다. 기존 동역학 방정식과 쇄교자속 표를 국소 모형과 추정기로 바꾸고, 제약 최적화 문제를 운전 중 풀도록 구성했다. 실험과 수치 시뮬레이션으로 평가했다.[^p2] | 1저자 Jongseok Kim · 최경환 중간 저자 · 마지막 저자 Ki-Bum Park |
| 3 | 2026 | [Online Learning of Control-Oriented Lateral Tire-Force Maps for Vehicle MPC](https://doi.org/10.1109/iwis70716.2026.11667752) · IWIS | 타이어 힘을 직접 측정하지 않고 차량의 옆 방향 움직임과 회전 움직임의 오차로 앞·뒤 타이어의 힘 모형을 갱신한다. 신경망의 수정 정보를 표에 보존해 이후의 차량 움직임 예측에 다시 사용한다. 타이어 성질과 조향이 달라지는 시뮬레이션에서 순간값이나 최근 자료만 이용하는 갱신 방식보다 힘과 예측의 오차를 줄였다.[^p3] | 1저자 Donghwa Hong · 최경환 마지막 저자 |
| 4 | 2026 | [All-Wheel Steering Vehicle Control Based on Contraction Theory with Neural Network](https://doi.org/10.1109/amc67705.2026.11435819) · AMC | 모든 바퀴를 조향하는 차량의 제어에 수축 이론과 신경망을 결합했다. 신경망으로 모형의 불확실성을 근사·보상하고, 제어기의 수축 성질과 학습 과정의 안정성을 분석했다. 닫힌 제어 과정이 시간이 지난 뒤 일정 범위 안에 머무르는 성질을 보이고, 수치 시뮬레이션으로 제어 방법을 검증했다.[^p4] | 1저자 Myeongseok Ryu · 최경환 마지막 저자 |
| 5 | 2025 | [Online Actor Critic Learning for Optimal Tracking in Servo Positioning Systems](https://doi.org/10.1109/iecon58223.2025.11221457) · IECON | 알려지지 않은 외부 영향이 있는 위치 제어 장치에서 동역학을 추정하는 필터와, 행동·가치를 학습하는 신경망을 함께 사용했다. 학습 오차의 변화와 닫힌 제어 과정의 안정성을 분석하고, 시간에 따라 외부 영향이 변하는 시뮬레이션에서 추종 제어를 평가했다.[^p5] | 1저자 Hyochan Lee · 최경환 마지막·교신저자 |
| 6 | 2025 | [Physics-Informed Online Learning of Flux Linkage Model for Synchronous Machines](https://doi.org/10.1109/iecon58223.2025.11221587) · IECON | 동기전동기의 쇄교자속을 물리 법칙과 모형의 제약에 맞춰 운전 중 학습하는 방법을 제안했다. 신경망의 갱신 규칙을 최적화 조건에 맞게 구성하고, 쇄교자속 추정기로 사용할 수 있도록 했다. 전동기 구동 시뮬레이션으로 검증했다.[^p6] | 1저자 Seunghun Jang · Myeongseok Ryu · 최경환 마지막 저자 |
| 7 | 2025 | [Constrained Optimization-Based Neuro-Adaptive Control (CONAC) for Synchronous Machine Drives Under Voltage Constraints](https://doi.org/10.1109/iecon58223.2025.11221692) · IECON | 전동기 성질을 정확히 모르는 상태에서 신경망을 운전 중 학습시키는 적응 제어를 제안했다. 전압 제약을 최적화 문제에 포함하고 그 식에서 학습 규칙을 도출했다. 추종 오차가 일정 범위를 벗어나지 않는 성질, 신경망 값의 수렴, 제약 충족을 분석하고 비선형 전동기 시뮬레이션으로 평가했다.[^p7] | 1저자 Myeongseok Ryu · 최경환 중간 저자 · 마지막 저자 Christoph M. Hackl |

## 교수와 전문 분야

최경환 교수는 KAIST 기계공학 학사(2014), 석사(2016), 박사(2020)를 받았다. KAIST 친환경·스마트자동차 연구센터에서 박사후연구원(2020년 3월–2021년 1월)과 연구조교수(2021년 1월–2022년 2월)를 지냈고, GIST 기계공학 관련 학과 조교수(2022년 3월–2025년 5월)와 인공지능대학원 겸임교수(2022년 9월–2025년 5월)를 거쳐 2025년 5월 KAIST 조천식모빌리티대학원 조교수로 부임했다.[^profile] 연구실 소개는 연결·자동화·전동화 차량의 최적 제어와 학습 기반 제어를 전문 분야로 적는다.[^profile]

최근 논문으로 보면 전문 분야는 주행 전체의 에너지 관리에 필요한 예측 모형,[^p1] 불확실성이 있는 전동기의 최적 구동과 물리 기반 모형 학습,[^p2][^p6][^p7] 타이어 모형과 조향 제어,[^p3][^p4] 제어 중 행동과 가치를 학습하는 방법으로 이어진다.[^p5]

## 구성원

2026-11-07 연구실 Current Members에 게시된 PI 외 17명이다. 과정은 박사후연구원 2명, 박사과정 3명, 석박사통합과정 3명, 석사과정 3명, 연구원 2명, 학부 인턴 4명이다. 연구 주제와 학교 이메일은 연구실 게시 표기다. 「대표 논문 참여」는 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Ahmad Mouri Zadeh Khaki (아흐마드 모우리 자데 카키) | 박사후연구원 |  | He is currently working on LLM-based Multi-agent Systems and FPGA acceleration of deep learning algorithms for Robots and Autonomous Vehicles applications. His research interests include Embedded Systems , Deep Learning , and Multi-agent Systems . | ahmadmouri@kaist.ac.kr |  |
| Geunyoung Park (박근영) | 박사후연구원 |  | He is currently working on optimal energy and thermal management of electrified vehicles. His research interests include optimal control , predictive energy management , vehicle thermal management systems , and data-driven modeling and control . | geunyoung.park@kaist.ac.kr | 1 |
| Seunghun Jang (장승훈) | 박사과정 | 2022 (MIC Lab 합류) | His current research interests include state estimation of Synchronous Machines (SMs) , physics-informed online learning of SMs , optimal control of electric drives . | shjang7071@kaist.ac.kr | 6 |
| Myeongseok Ryu (유명석) | 박사과정 |  | His research interests include neuro-adaptive control , contraction theory , and online optimization . | dding_98@kaist.ac.kr | 4, 6, 7 |
| Hyochan Lee (이효찬) | 박사과정 |  | His current research interests include intelligent control of mobility systems using reinforcement learning and deep learning , tracking control of electromechanical systems , and the development of advanced control theories such as nonlinear adaptive control , optimal control , and learning-based control . | hyochanlee@kaist.ac.kr | 5 |
| Changeun Park (박창은) | 석박사통합과정 |  | His current research interests include optimal control , particularly model predictive control (MPC) . | aegis3141@kaist.ac.kr |  |
| Soobin Hwang (황수빈) | 석박사통합과정 |  | Her research interests include Vehicle dynamics control . | sbhwang@kaist.ac.kr |  |
| Minsoh Kim (김민서) | 석박사통합과정 |  | Her research interests include optimal control and learning-based control . | minsoh.kim@kaist.ac.kr |  |
| Naol Samuel Erega (나올 사무엘 에레가) | 석사과정 |  | His research interests include neural network-based control, system estimations, and unmanned ground vehicle(UGV) dynamics. | samuelnaol7@kaist.ac.kr |  |
| Yejin Jang (장예진) | 석사과정 |  | Her research interests include Vehicle Dynamics control . | jangyj@kaist.ac.kr |  |
| Md Symum Hossain (사이뭄 호싸인) | 석사과정 |  | His research interests include Quantum Computing , Quantum Algorithm , and Machine Learning(QML) . | symum.h@kaist.ac.kr |  |
| Donghwa Hong (홍동화) | 연구원 |  | His research focuses on learning-based identification of uncertain dynamics and state and parameter estimation , with applications to vehicle and robotic systems . | fairytale@kaist.ac.kr | 3 |
| Jiyun Kim (김지윤) | 연구원 |  | Her research interests include learning-based motion planning, autonomous driving, and intelligent robotic systems . She focuses on developing reliable and robust decision-making methods based on imitation learning, vision-language models and vision-language-action models (VLMs/VLAs) , and robot foundation models. Her long-term goal is to build safer and more human-centered autonomous systems that can operate effectively in complex real-world environments. | JiyunKim@kaist.ac.kr |  |
| Tarekegn Sami Gulilat | 학부 인턴 | 2026-06 (연구 인턴 합류) | His research interests include autonomous racing , opponent trajectory prediction , and uncertainty-aware, chance-constrained motion planning , in particular using Gaussian processes and conformal prediction to quantify prediction uncertainty for head-to-head overtaking on the F1TENTH (RoboRacer) platform. | samitarekegn101@kaist.ac.kr |  |
| Teodor Penchev (테오도르 펜체프) | 학부 인턴 |  | His research interests include reinforcement learning , model-based reinforcement learning , and hierarchical control frameworks for robotic systems . | teodorpenchev04@kaist.ac.kr |  |
| Habeebullah Adeleke (하비불러  아델레케) | 학부 인턴 | 2026 (MIC Lab 합류) | His current research focuses on reinforcement learning-based control for humanoid robots , with broader interests in robotics , robot learning , control systems , embedded systems , and mechatronics . | Habeebullah.a@kaist.ac.kr |  |
| Kyumin Lee (이규민) | 학부 인턴 |  | His research interests include vehicle state estimation , vehicle motion control , model predictive control , and end-to-end autonomous driving . | mumu211@kaist.ac.kr |  |

## 졸업생과 이전 구성원

연구실 Alumni에 게시된 석사 구획 5명과 학부 인턴 구획 4명이다. 학위와 연도, 진로는 각 인물의 게시 소개를 따른다. 이전 GIST 소속 시기의 구성원이 함께 들어 있다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jaejoon Kim (김재준) | 석사 (2025) |  |
| Yeongho Jeong (정영호) | 석사 (2025) |  |
| Minseok Seo (서민석) | 석사과정 |  |
| Minji Kim (김민지) | 석사 (2025) |  |
| Seongjae Shin (신성재) | 석사 (2024) | GIST 박사과정 (2025) |
| Seongyeon Hwang (황성연) | 학부 인턴 |  |
| Angus Siegloff (앵거스 시그로프) | 학부 인턴 |  |
| Seonsoo Kim (김선수) | 학부 인턴 | Agency for Defense Development, AI Center |
| Semin Jeong (정세민) | 학부 인턴 | Ph.D. Student at KAIST, ACL |

## 최근 논문 목록 (2021–2026)

연구실 Publications의 국제 학술지 13편, 국제 학회 30편, 국내 학술지 5편, 국내 학회 22편, 석사 학위 논문 5편, 사전 공개본 3편, 개별 초록을 게시한 심사 중 원고 5편으로 총 83편이다. 교수의 2025년 5월 KAIST 조교수 부임 전과 이전 KAIST 연구직 재직 시기의 논문이 섞여 있다. 제목·저자·발표처는 연구실 표기이고, 학회 목록의 accepted는 「채택」, 심사 중 원고와 사전 공개본은 별도 표시했다. 심사 중 원고의 연도는 누리집 구역 표기다.[^pubs][^profile][^submitted]

**2026**

- Hyochan Lee , Kyunghwan Choi \*. "From Bellman Consistency toward Bellman Optimality: Constrained Online Critic Learning for Nonlinear Optimal Control". *Withheld during double-blind review , 2026 (심사 중)*.
- Myeongseok Ryu , Donghwa Hong , Kyunghwan Choi \*. "Constrained Optimization-Based Neuro-Adaptive Control (CONAC) for Unknown Systems Under Multiple Convex Input Constraints". *Withheld during double-blind review , 2026 (심사 중)*.
- Angus Siegloff , Myeongseok Ryu , Kyunghwan Choi \*. "Physics-Constrained Kalman Filtering for Wheel Normal Load Estimation Using Suspension and IMU Measurements". *IEEE Transactions on Vehicle Technology , 2026 (심사 중)*.
- Jiyun Kim , Kyunghwan Choi \*. "CAR Planner: Constrained-Attention-Based Robust Imitation Learning for Autonomous Driving". *Withheld during double-blind review , 2026 (심사 중)*.
- Changeun Park , Seunghun Jang , Kyunghwan Choi \*. "Online Adaptive Differentiable Predictive Control With Application to IPMSM MTPA Control". *IEEE International Transportation Electrification Conference & Expo, Asia-Pacific (ITEC-AP) , 2026 (심사 중)*.
- Geunyoung Park , Kyunghwan Choi , Dongsuk Kum \*. "Synthesis of a Link-Level Energy-Time Predictor Toward the Implementation of a Link-based Predictive EMS". *IEEE Access (Early Access) , 2026 · DOI: <https://doi.org/10.1109/ACCESS.2026.3726602>*.
- Jongseok Kim , Kyunghwan Choi , Youngseok Lee , Ki-Bum Park \*. "Model-Adaptive Predictive Torque Control of IPMSMs for Online Optimal Operation: A Lookup-Table-Free Approach". *IEEE Transactions on Transportation Electrification (Early Access) , 2026 · DOI: <https://doi.org/10.1109/TTE.2026.3695345>*.
- Jiyun Kim , Ahmad Mouri Zadeh Khaki , Kyunghwan Choi \*. "TRIAD Planner: Three-Level Robust Imitation Learning for Autonomous Driving". *Conference on Robot Learning (CoRL) (채택), 2026*.
- Myeongseok Ryu , Donghyun Hwang , Youngsik Yoon , Kyunghwan Choi \*. "Constrained Optimization-Based Yaw-Rate Reference Map Generation for Active Rear Steering Control of Four-Wheel-Steering Vehicles". *International Conference on Control, Automation and Systems (ICCAS) (채택), 2026*.
- Myeongseok Ryu , Kyunghwan Choi \*, Sesun You. "Vector-Space Optimization Framework Based on Projected Contraction Condition for Control Design with Input Saturation". *International Federation of Automatic Control (IFAC) World Congress (채택), 2026*.
- Seunghun Jang , Kyunghwan Choi \*. "Online Physics-Informed Learning-Based Identification: Application to Adaptive MTPA Control of Synchronous Machines". *International Federation of Automatic Control (IFAC) World Congress (채택), 2026*.
- Hyochan Lee , Kyunghwan Choi \*. "Online Constrained Reinforcement Learning for Optimal Tracking". *International Federation of Automatic Control (IFAC) World Congress (채택), 2026*.
- Pilwon Hur \*, Hyosung Ahn , Kyunghwan Choi , Junpyo Lee. "Industry-Integrated Motor Systems Education: Bridging Classical Control, AI, and Real-World Applications". *International Federation of Automatic Control (IFAC) World Congress (채택), 2026*.
- Jiyun Kim , Kyunghwan Choi \*. "CARE Planner : Constrained Attention and Risk-aware Planning for Imitation based Autonomous Driving". *International Federation of Automatic Control (IFAC) World Congress (채택), 2026*.
- Donghwa Hong , Kyunghwan Choi \*. "Online Learning of Control-Oriented Lateral Tire-Force Maps for Vehicle MPC". *International Workshop on Intelligent Systems (IWIS) , pp. 1-4, 2026 · DOI: <https://doi.org/10.1109/IWIS70716.2026.11667752>*.
- Kyunghwan Choi \*. "Traffic Network-Aware Energy Management for FCEVs: Integrating Trip-Specific Control and Long-Run Optimality". *Asian Control Conference (ASCC) (채택), 2026*.
- Ahmad Mouri Zadeh Khaki , Kyunghwan Choi \*. "LLM-PPO Driver: Improving Autonomous Driving via LLM-Guided Reward Shaping and Imitation Learning". *Asian Control Conference (ASCC) (채택), 2026*.
- Donghwa Hong , Kyunghwan Choi \*. "Integral Error-Based Adaptive Neural Identifier for Nonlinear Lateral Tire Forces". *IEEE International Conference on Advanced Motion Control (AMC) , pp. 1-6, 2026 · DOI: <https://doi.org/10.1109/AMC67705.2026.11435827>*.
- Myeongseok Ryu , Kyunghwan Choi \*. "All-Wheel Steering Vehicle Control Based on Contraction Theory with Neural Network". *IEEE International Conference on Advanced Motion Control (AMC) , pp. 1-6, 2026 · DOI: <https://doi.org/10.1109/AMC67705.2026.11435819>*.
- Seunghun Jang , Kyunghwan Choi \*. "V2X-Based Predictive Thermal Management for Battery Electric Vehicles 전기차의 V2X 기반 예측 열관리 제어". *대한전기자동차학회 (KIEV) , 2026*.
- Donghwa Hong , Kyunghwan Choi \*. "State-Error-Based Online Learning of Control-Oriented Tire Force Models Using Grid Memory 제어 지향 타이어 횡력 모델의 그리드 메모리를 이용한 상태 오차 기반 온라인 학습". *제어로봇시스템학회 (ICROS) , pp. 843-844, 2026*.
- Changeun Park , Kyunghwan Choi \*. "Online learning-based linear model predictive control approximation 온라인 학습 기반 선형 모델 예측 제어 근사". *제어로봇시스템학회 (ICROS) , pp. 165-166, 2026*.
- Naol Samuel Erega , Kyunghwan Choi \*. "End-to-End Online LSTM Control for Robust 4WS Path Tracking under Combined Disturbances 복합 외란 하에서 강인한 4WS 경로 추종을 위한 엔드투엔드 온라인 LSTM 제어". *제어로봇시스템학회 (ICROS) , pp. 503-504, 2026*.
- Myeongseok Ryu , Kyunghwan Choi \*. "Constrained Optimization-Based Performance Improvement Analysis of Vehicle Lateral Control Using All-Wheel Steering 사륜 조향 시스템을 통한 횡 차량 거동 향상의 제약 최적화 기반 분석". *제어로봇시스템학회 (ICROS) , pp. 505-506, 2026*.
- Hyochan Lee , Kyunghwan Choi \*. "Constrained Optimization Formulation of Bellman Optimality Equation for Online Reinforcement Learning 온라인 강화학습을 위한 벨만 최적 방정식의 제약 최적화 문제". *제어로봇시스템학회 (ICROS) , pp. 557-558, 2026*.
- Seunghun Jang , Kyunghwan Choi \*. "Concurrent Learning-Based Adaptive Online Identification of Battery Thermal Dynamics 동시학습 기반 배터리 열동역학 온라인 잔차 학습". *제어로봇시스템학회 (ICROS) , pp. 525-526, 2026*.
- Ahmad Mouri Zadeh Khaki , Kyunghwan Choi \*. "LLM-driven Semantic Guidance for Enhancing Reinforcement Learning-based Autonomous Driving through Reward Engineering 강화학습 기반 자율주행 성능 향상을 위한 보상 설계 기반 LLM 주도 의미적 가이던스". *제어로봇시스템학회 (ICROS) , pp. 933-934, 2026*.
- Jiyun Kim , Kyunghwan Choi \*. "CARE Planner : Constrained Attention and Risk-aware Planning for Imitation-based Autonomous Driving CARE Planner : 모방학습 기반 자율주행을 위한 제약 어텐션 및 위험 인지 플래닝". *제어로봇시스템학회 (ICROS) , pp. 475-476, 2026*.
- Jiyun Kim , Kyunghwan Choi \*. "Robust Imitation Learning with Attention Constraints and Risk Awareness for Motion Planning in Autonomous Driving". *Gwangju Institute of Science and Technology (GIST) Library , 2026*.
- Donghwa Hong , Kyunghwan Choi \*. "Integral Error-Based Adaptive Neural Identifier for a Class of Uncertain Nonlinear Systems". *Gwangju Institute of Science and Technology (GIST) Library , 2026*.

**2025**

- Geunyoung Park , Kyunghwan Choi , Minjun Kim , EunAe Cho , Kyungsub Sung , Dongsuk Kum \*. "Development of a Real-time Link-Based Predictive Energy Management Strategy for Extending FCEV Lifespan Using an Experiment-driven Degradation Model". *Applied Energy , vol. 397, no. 16, 2025 · DOI: <https://doi.org/10.1016/j.apenergy.2025.126246>*.
- Geunyoung Park , Kyunghwan Choi , Dongsuk Kum \*. "Predictive Control of a Dog-Clutch Transmission via a Transformer-Based Velocity Prediction". *IEEE Transactions on Vehicular Technology , vol. 74, no. 5, pp. 7430-7443, 2025 · DOI: <https://doi.org/10.1109/TVT.2024.3468390>*.
- Kyunghwan Choi \*, Seongjae Shin , Minseok Seo. "Cooperative Merging in Mixed Traffic Based on Strategic Influence of Connected Automated Vehicles on Human-Driven Vehicle Behavior". *Advanced Intelligent Systems , pp. 2400797, 2025 · DOI: <https://doi.org/10.1002/aisy.202400797>*.
- Minseok Seo , Kyunghwan Choi \*. "State-Dependent Lagrange Multipliers for State-Wise Safety in Constrained Reinforcement Learning". *International Conference on Robot Intelligence Technology and Applications (RiTA) (채택), 2025 · DOI: <https://doi.org/10.36227/techrxiv.175979326.64150311/v1>*.
- Jiyun Kim , Kyunghwan Choi \*. "Mitigating Attention Collapse via Mean-Deviation Constrained Optimization". *International Conference on Robot Intelligence Technology and Applications (RiTA) (채택), 2025 · DOI: <https://doi.org/10.36227/techrxiv.175877819.93334616/v3>*.
- Hyochan Lee , Kyunghwan Choi \*. "Constrained Optimization Formulation of Bellman Optimality Equation for Online Reinforcement Learning". *International Conference on Robot Intelligence Technology and Applications (RiTA) (채택), 2025*.
- Hyochan Lee , Kyunghwan Choi \*, Wooyong Kim \*. "Using Deep Reinforcement Learning for Dynamic Gain Adjustment of a Disturbance Observer". *International Conference on Control, Automation and Systems (ICCAS) , pp. 1273-1278, 2025 · DOI: <https://doi.org/10.23919/ICCAS66577.2025.11301220>*.
- Seunghun Jang , Myeongseok Ryu , Kyunghwan Choi \*. "Physics-Informed Online Learning of Flux Linkage Model for Synchronous Machine". *Annual Conference of the IEEE Industrial Electronics Society (IECON) , pp. 1-7, 2025 · DOI: <https://doi.org/10.1109/IECON58223.2025.11221587>*.
- Hyochan Lee , Kyunghwan Choi \*. "Online Actor Critic Learning for Optimal Tracking in Servo Positioning Systems". *Annual Conference of the IEEE Industrial Electronics Society (IECON) , pp. 1-7, 2025 · DOI: <https://doi.org/10.1109/IECON58223.2025.11221457>*.
- Yeongho Jeong , Kyunghwan Choi \*. "LMI-based Neural Network Observer for State and Nonlinearity Estimation". *Annual Conference of the IEEE Industrial Electronics Society (IECON) , pp. 1-7, 2025 · DOI: <https://doi.org/10.1109/IECON58223.2025.11221827>*.
- Myeongseok Ryu , Niklas Monzen , Pascal Seitter , Kyunghwan Choi , Christoph M. Hackl \*. "Constrained Optimization-Based Neuro-Adaptive Control (CONAC) for Synchronous Machine Drives Under Voltage Constraints". *Annual Conference of the IEEE Industrial Electronics Society (IECON) , pp. 1-7, 2025 · DOI: <https://doi.org/10.1109/IECON58223.2025.11221692>*.
- Myeongseok Ryu , Jiyun Kim , Kyunghwan Choi \*. "Imposing a Weight Norm Constraint for Neuro-Adaptive Control". *European Control Conference (ECC) , pp. 380-385, 2025 · DOI: <https://doi.org/10.23919/ECC65951.2025.11186942>*.
- Hyochan Lee , Kyunghwan Choi \*. "Online Reinforcement Learning for Optimal Tracking in Servo Positioning Systems 온라인 강화학습 기반 서보 시스템의 최적 각도 추종 제어". *제어로봇시스템학회 (ICROS) , pp. 727-728, 2025*.
- Jiyun Kim , Kyunghwan Choi \*. "CAR Planner: Constrained-Attention-Based Robust Imitation Learning for Autonomous Driving CAR Planner: 제약 어텐션 기반 강건 모방학습 플래너". *한국자동차공학회 추계학술대회 (KSAE) , pp. 938-944, 2025*.
- Minseok Seo , Kyunghwan Choi \*. "Cooperative Merging in Mixed Traffic Based on Strategic Influence of Connected Automated Vehicles on Human-Driven Vehicle Behavior 혼합 교통 환경에서 CAV의 전략적 개입을 통한 협력적 합류 제어". *한국자동차공학회 추계학술대회 (KSAE) , pp. 945-951, 2025*.
- Seunghun Jang , Kyunghwan Choi \*. "Physics-Informed Online Learning for Stator Flux Linkage Estimation in Synchronous Machines 동기전동기의 실시간 고정자 쇄교자속 추정을 위한 물리정보기반 학습". *제어로봇시스템학회 (ICROS) , pp. 592-593, 2025*.
- Minseok Seo , Kyunghwan Choi \*. "State-wise Safety in Autonomous Driving via Lagrangian-based Constrained Reinforcement Learning 라그랑지안 기반 제약 강화 학습을 통한 자율주행 시스템의 상태별 안정성 보장". *한국자동차공학회 춘계학술대회 (KSAE) , pp. 802, 2025*.
- Minseok Seo , Kyunghwan Choi \*. "State-wise Safety in Autonomous Driving via Lagrangian-based Constrained Reinforcement Learning". *Gwangju Institute of Science and Technology (GIST) Library , 2025*.
- Myeongseok Ryu , Kyunghwan Choi \*. "Constrained Optimization-Based Neuro-Adaptive Control (CoNAC) for Euler-Lagrange Systems". *Gwangju Institute of Science and Technology (GIST) Library , 2025*.
- Jiyun Kim , Kyunghwan Choi \*. "CAR Planner: Constrained-Attention-Based Robust Imitation Learning for Autonomous Driving". *Techrxiv , 2025 (사전 공개본) · DOI: <https://doi.org/10.36227/techrxiv.175979328.80125117/v1>*.

**2024**

- Kyunghwan Choi , Jongseok Kim , Ki-Bum Park \*. "Generalized Model Predictive Torque Control of Synchronous Machine". *IEEE/ASME Transactions on Mechatronics , pp. 1-11, 2024 · DOI: <https://doi.org/10.1109/TMECH.2024.3461209>*.
- Kyunghwan Choi , Geunyoung Park , Dongsuk Kum \*. "An Analytical Approach to the Predictive Energy Management of Connected HEVs: What Information Do We Need to Guarantee Global Optimality?". *IEEE Transactions on Intelligent Transportation Systems , vol. 25, no. 9, pp. 12749-12761, 2024 · DOI: <https://doi.org/10.1109/TITS.2024.3384358>*.
- Yeongho Jeong , Seunghun Jang , Kyunghwan Choi \*. "Neural Network-based Nonlinearity Estimation of Voltage Source Inverter for Synchronous Machine Drives". *IEEE International Symposium on Industrial Electronics (ISIE) , pp. 1-5, 2024 · DOI: <https://doi.org/10.1109/ISIE54533.2024.10595703>*.
- Seunghun Jang , Bernd Pfeifer , Christoph M. Hackl , Kyunghwan Choi \*. "Extended State Observer Based Stator Flux Linkage Estimation of Nonlinear Synchronous Machines". *IEEE International Symposium on Industrial Electronics (ISIE) , pp. 1-5, 2024 · DOI: <https://doi.org/10.1109/ISIE54533.2024.10595772>*.
- Geunyoung Park , Kyunghwan Choi , Dongsuk Kum \*. "Stack Degradation Protection of FCEVs via Predictive Energy Management Strategy with Segmented Roads". *American Control Conference (ACC) , pp. 3643-3649, 2024 · DOI: <https://doi.org/10.23919/ACC60939.2024.10644649>*.
- Kyunghwan Choi , Kyung-Soo Kim \*. "Current Status and Future Trends in Synchronous Machine Control Technologies: A Focus on Torque Control 동기전동기 제어기술 동향 및 발전방향: 토크제어를 중심으로". *Journal of Institute of Control, Robotics and Systems , vol. 30, no. 4, pp. 479-491, 2024 · DOI: <https://doi.org/10.5302/J.ICROS.2024.24.0052>*.
- Kunwoo Na , Youngkook Kim , Kyunghwan Choi , Wooyong Kim \*. "A Current-sensor Error Compensation Algorithm for Battery Management Systems Based on Sigma-point Kalman Filter 시그마–포인트 칼만 필터를 사용한 배터리 관리 시스템의 전류 센서 오차 보상 알고리즘". *Journal of Institute of Control, Robotics and Systems , vol. 30, no. 10, pp. 1131-1138, 2024 · DOI: <https://doi.org/10.5302/J.ICROS.2024.24.0095>*.
- Hyochan Lee , Kyunghwan Choi \*. "Using Deep Reinforcement Learning for Intelligent Gain Adjustment of a Disturbance Observer 외란관측기의 심층강화학습 기반 지능형 자동 동조 기법". *제어로봇시스템학회 (ICROS) , pp. 292-293, 2024*.
- Seunghun Jang , Kyunghwan Choi \*. "Stator Flux Linkage Estimation of Nonlinear Synchronous Machines Based on the State Observer 상태 관측기 기반 비선형 동기기의 고정자 쇄교자속 추정". *제어로봇시스템학회 (ICROS) , pp. 308-309, 2024*.
- Yeongho Jeong , Kyunghwan Choi \*. "Neural Network-based Nonlinearity Estimation of Voltage Source Inverter for Synchronous Machine Drives 동기전동기 구동용 전압원 인버터의 인공 신경망 기반 비선형성 추정". *제어로봇시스템학회 (ICROS) , pp. 312-313, 2024*.
- Myeongseok Ryu , Kyunghwan Choi \*. "Approximation-based Steering Controller with Deep Neural Network 심층신경망 근사기반 조향 제어기". *제어로봇시스템학회 (ICROS) , pp. 884-885, 2024*.
- Seunghun Jang , Kyunghwan Choi \*. "Online Stator Flux Linkage Estimation of Synchronous Machines". *Gwangju Institute of Science and Technology (GIST) Library , 2024*.
- Myeongseok Ryu , Kyunghwan Choi \*. "CNN-based End-to-End Adaptive Controller with Stability Guarantees". *Arxiv , 2024 (사전 공개본) · DOI: <https://doi.org/10.48550/arXiv.2403.03499>*.
- Kyunghwan Choi , Christoph M. Hackl \*. "A Lyapunov-Based Approach to Nonlinear Programming and Its Application to Nonlinear Model Predictive Torque Control". *Techrxiv , 2024 (사전 공개본) · DOI: <https://doi.org/10.36227/techrxiv.171085098.82768159/v1>*.

**2023**

- Wooyong Kim , Kunwoo Na , Kyunghwan Choi \*. "A Current Sensor Fault-detecting Method for Onboard Battery Management Systems of Electric Vehicles Based on Disturbance Observer and Normalized Residuals". *International Journal of Control, Automation and Systems , vol. 21, no. 11, pp. 3563-3573, 2023 · DOI: <https://doi.org/10.1007/s12555-023-0377-8>*.
- Minseong Choi , Kyunghwan Choi , Minsu Cho , Minyoung Lee , Kyung-Soo Kim \*. "Chattering Reduction of Sliding Mode Control via Nonlinear Disturbance Observer for Anti-lock Braking System and Verification with Carsim Simulation". *International Journal of Automotive Technology , vol. 24, no. 4, pp. 1141–1149, 2023 · DOI: <https://doi.org/10.1007/s12239-023-0093-7>*.
- Minseok Seo , Seongjae Shin , Kyungjoong Kim , Kyunghwan Choi \*. "Reinforcement Learning-Based Collision Avoidance of a Connected and Automated Vehicle at Merging Roads". *International Workshop on Intelligent Systems (IWIS) , pp. 1-5, 2023 · DOI: <https://doi.org/10.1109/IWIS58789.2023.10284616>*.
- Myeongseok Ryu , Junseo Ha , Minji Kim , Kyunghwan Choi \*. "A Comparative Study of Reinforcement Learning and Analytical Methods for Optimal Control". *International Workshop on Intelligent Systems (IWIS) , pp. 1-5, 2023 · DOI: <https://doi.org/10.1109/IWIS58789.2023.10284677>*.
- Kyunghwan Choi , Ki-Bum Park \*. "Model Predictive Torque Control of Synchronous Machines Without a Current or Stator Flux Reference Generator". *IEEE International Symposium on Industrial Electronics (ISIE) , pp. 1-6, 2023 · DOI: <https://doi.org/10.1109/ISIE51358.2023.10228177>*.
- Jonghwan Kim , Youngseok Lee , Kyunghwan Choi , Jiho Song , Kinum Kim \*. "Performance Comparison of Long-Horizon FCS-MPC for IPMSM Considering THDi and Inverter Loss". *International Conference on Power Electronics and ECCE Asia (ICPE - ECCE Asia) (채택), pp. 1680-1685, 2023 · DOI: <https://doi.org/10.23919/ICPE2023-ECCEAsia54778.2023.10213826>*.
- Seunghun Jang , Kyunghwan Choi \*. "Stator Flux Linkage Estimation of Synchronous Machines Based on Integration Error Estimation for Improved Transient Performance". *IEEE Conference on Decision and Control (CDC) , pp. 4197-4202, 2023 · DOI: <https://doi.org/10.1109/CDC49753.2023.10383827>*.
- Kunwoo Na , Kyunghwan Choi , Wooyong Kim \*. "A Current Sensor Fault-detecting Method for Electric Vehicle Battery Systems Based on Disturbance Observer 외란 관측기를 사용한 전기차 배터리 시스템의 전류 센서 고장 감지 방법". *Journal of Institute of Control, Robotics and Systems , vol. 29, no. 12, pp. 1052-1059, 2023 · DOI: <https://doi.org/10.5302/J.ICROS.2023.23.0124>*.
- Minseok Seo , Kyunghwan Choi \*. "Path Control of a Connected and Automated Vehicle at Intersections and Merging Zones Using Attention Mechanism-Based Reinforcement Learning 어텐션 메커니즘 기반 강화학습을 활용한 교차로 및 합류 구간에서의 커넥티드 자율주행차 경로 제어". *한국자동차공학회 추계학술대회 (KSAE) , pp. 725, 2023*.
- Myeongseok Ryu , Kyunghwan Choi \*. "Integrated Motion Control of Four in-Wheel Motor Actuated Vehicles Considering Path Tracking, Ride Comfort, and Energy Efficiency 경로 추종, 동적 승차감, 그리고 에너지 효율을 고려한 전륜 인휠모터 자동차의 통합 운동 제어". *한국자동차공학회 추계학술대회 (KSAE) , pp. 490, 2023*.
- Seunghun Jang , Kyunghwan Choi \*. "Sator Flux Linkage Estimation Method of Synchronous Machines Based on Integration Error Estimation 적분 오차 추정 기반 동기 전동기의 쇄교 자속 추정 기법". *제어로봇시스템학회 (ICROS) , pp. 177-178, 2023*.
- Myeongseok Ryu , Kyunghwan Choi \*. "Data-driven Modeling of Model Residuals for Linear Model Predictive Control of Nonlinear Systems 비선형 시스템의 선형모델예측제어를 위한 데이터 기반 시스템 잔차 모델링". *제어로봇시스템학회 (ICROS) , pp. 837-838, 2023*.

**2022**

- Hyochan Lee , Hyeoncheol Lee , Jaekwang Lee , Hyunduck Choi , Kyunghwan Choi , Younghun Kim , Seokkyoon Kim \*. "Output-Feedback Multi-Loop Positioning Technique via Dual Motor Synchronization Approach for Elevator System Applications". *Energies , vol. 15, no. 23, pp. , 2022 · DOI: <https://doi.org/10.3390/en15239147>*.
- Kyunghwan Choi , Wooyong Kim \*. "Real-Time Predictive Energy Management Strategy for Fuel Cell-Powered Unmanned Aerial Vehicles Based on the Control-Oriented Battery Model". *IEEE Control Systems Letters , vol. 7, pp. 943-948, 2022 · DOI: <https://doi.org/10.1109/LCSYS.2022.3228946>*.
- Kyunghwan Choi , Jihye Byun , Sangmin Lee , In Gwun Jang \*. "Adaptive Equivalent Consumption Minimization Strategy (A-ECMS) for the HEVs With a Near-Optimal Equivalent Factor Considering Driving Conditions". *IEEE Transactions on Vehicular Technology , vol. 71, no. 3, pp. 2538-2549, 2022 · DOI: <https://doi.org/10.1109/TVT.2021.3127691>*.
- Wooyong Kim , Kyunghwan Choi \*. "Current Sensorless State of Charge Estimation Approach for Onboard Battery Systems with an Unknown Current Estimator". *Journal of Energy Storage , vol. 52, 2022 · DOI: <https://doi.org/10.1016/j.est.2022.104726>*.
- Jongseok Kim , Jiho Song , Kyunghwan Choi \*, Ki-Bum Park \*. "A Comparison of DPWM and Inverter Loss Energy Based FCS-MPC for IPMSM". *IEEE International Power Electronics and Motion Control Conference (PEMC) , pp. 943-948, 2022 · DOI: <https://doi.org/10.1109/PEMC51159.2022.9962845>*.
- Hyochan Lee , Youngseok Lee , Kyunghwan Choi , Seokkyoon Kim \*. "Speed Tracking for Servo Systems via Active Pole-Zero Cancellation Stabilization Technique 서보 시스템 응용을 위한 능동형 영-극점 상쇄 속도 추종 기술". *Journal of Institute of Control, Robotics and Systems , vol. 28, no. 11, pp. 1045-1051, 2022 · DOI: <https://doi.org/10.5302/J.ICROS.2022.22.0137>*.
- Kyunghwan Choi , Dongsuk Kum \*. "Current Status and Future Trends of Electrified Powertrain Technologies 전동화 파워트레인 기술 동향 및 발전 방향: 아키텍처와 제어전략을 중심으로". *Mobility Research , vol. 2, no. 1, pp. 23-42, 2022 · DOI: <https://doi.org/10.23257/mobile.2.1.202203.002>*.

## 특허

연구실 Publications의 국제 등록 3건, 국제 출원 중 1건, 국내 등록 3건이다. 기준 기간은 2021-10-13–2026-10-13이며, 날짜는 게시된 등록일 또는 출원일이다. 교수의 2025년 5월 KAIST 조교수 부임 전 항목이 포함된 개인 특허 목록이다.[^pubs][^profile]

- K.-S. Kim, K. Choi , and I. G. Jang, “Method and apparatus for controlling power of hybrid vehicle considering driving environment,” U.S. Patent 12,097,840 , Sep. 24, 2024. (상태 등록)
- K.-S. Kim, K. Choi , and S.-K. Kim, “Method and apparatus for real-time estimation of full parameters of permanent magnet synchronous motor,” U.S. Patent 11,614,488 , Mar. 28, 2023. (상태 등록)
- I. G. Jang, D. Kum, K.-S. Kim, K. Jang, C. Lee, J. H. Kim, K. Choi , and M. Kim, “Apparatus and method for operating accessories of vehicle during engine stop using one-way clutch pulley,” U.S. Patent 11,607,944 , Mar. 21, 2023. (상태 등록)
- K.-S. Kim, K. Choi , and I. G. Jang, “Method and apparatus for controlling power of hybrid vehicle considering transient characteristics,” U.S. Patent Application 18/648,697 , Apr. 29, 2024, pending. (상태 출원 중)
- 김경수, 최경환 , 장인권, “하이브리드 차량의 과도특성을 고려한 동력제어 방법 및 장치,” 대한민국 특허 10-2701529 , 2024.8.28. (상태 등록)
- 김경수, 최경환 , 장인권, “하이브리드 차량의 주행환경을 고려한 동력제어 방법 및 장치,” 대한민국 특허 10-2508409 , 2023.3.6. (상태 등록)
- 김경수, 최경환 , 김석균, “영구자석동기모터 전체 파라미터의 실시간 추정 방법 및 장치,” 대한민국 특허 10-2437244 , 2022.8.24. (상태 등록)

## 연구 과제

연구실 Research Projects의 과제 23건과 교수 소개의 과제 1건으로, 수행 기간이 2021-10-13–2026-10-13과 겹치는 항목이다. 교수의 2025년 5월 KAIST 조교수 부임 전과 이전 KAIST 연구직 재직 시기 과제가 섞여 있다. 지원 기관과 역할은 게시 표기이며, 역할은 최경환 교수 기준이다.[^projects][^profile]

- 글로벌생산제조기술연구소 (지원 교육부 (한국연구재단); 기간 2026.09.01 - 2035.08.31; 역할 Co-Principal Investigator)
- 산업 특화 Physical AI 파운데이션 모델 개발 및 차세대 융합형 인재양성 (지원 과학기술정보통신부 (정보통신기획평가원); 기간 2026.04.01 - 2029.12.31; 역할 Researcher)
- 안정성 및 제약조건을 충족하는 온라인 심층학습 및 모빌리티 시스템 제어 응용 (지원 한국연구재단 우수신진연구; 기간 2025.03.01 - 2029.02.28; 역할 Principal Investigator)
- 심층학습의 제어 관점 해석과 모빌리티 시스템 적용 연구 (지원 Korean Advanced Institute of Science and Technology (KAIST); 기간 2025.03.01 - 2028.12.31; 역할 Principal Investigator)
- 국토교통 DNA 플러스 도로교통분야 융합기술대학원 (지원 국토교통부 (국토교통과학기술진흥원); 기간 2022.05.01 - 2027.12.31; 역할 Researcher)
- 초실감 보병 전투 기술 훈련 기술 (지원 국방부; 기간 2022.12.01 - 2027.11.30; 역할 Co-Principal Investigator)
- 주행성능 향상 및 튜닝성 개선을 위한 RWS제어로직 개발(2차년도) (지원 현대자동차; 기간 2026.09.07 - 2027.09.06; 역할 Principal Investigator)
- 물류 작업 및 탑승형 고속 이동을 위한 휴머노이드 전신동역학 제어 기술 개발 (지원 KAIST 모빌리티 AX 연구소; 기간 2026.07.01 - 2027.05.31; 역할 Principal Investigator)
- 비정형 농업 환경 자율주행을 위한 VLM 기반 상황인식 및 경로 플래닝 기술 개발 (지원 KAIST 모빌리티 AX 연구소; 기간 2026.07.01 - 2027.05.31; 역할 Principal Investigator)
- e-모빌리티 통합 열·에너지 관리 연구 수행을 위한 시험 인프라 구축 (지원 과학기술정보통신부 (한국연구재단); 기간 2026.03.01 - 2027.02.28; 역할 Principal Investigator)
- 차량 엔진 오일 펌프용 고정밀·고효율 구동을 위한 인버터 및 구동 제어 기술 개발 (지원 SNT모티브; 기간 2026.04.27 - 2026.12.31; 역할 Principal Investigator)
- 주행성능 향상 및 튜닝성 개선을 위한 RWS제어로직 개발(1차년도) (지원 현대자동차; 기간 2025.06.23 - 2026.06.22; 역할 Principal Investigator)
- 고하중 물류 운송을 위한 로봇 기반 협력 운송 기술 개발 (지원 KAIST 모빌리티 AX 연구소; 기간 2025.07.01 - 2026.05.31; 역할 Principal Investigator)
- 미래형자동차 핵심기술 R&D 전문인력양성 (지원 산업통상자원부; 기간 2022.03.01 - 2025.02.28; 역할 Researcher)
- 급변부하 압축기 토크 제어 알고리즘 개발 (지원 LG 전자; 기간 2024.05.20 - 2024.08.19; 역할 Principal Investigator)
- 동기전동기를 위한 일반화된 모델예측토크제어 기법 개발 (지원 Gwangju Institute of Science and Technology (GIST); 기간 2022.03.01 - 2024.02.29; 역할 Principal Investigator)
- 전기차 기반의 모빌리티 제어로직 최적화 개발 (지원 (주)이모션; 기간 2023.10.18 - 2024.01.31; 역할 Principal Investigator)
- 자율주행을 위한 PBV용 조향제어기술 연구 (지원 한국전자통신연구원; 기간 2023.08.01 - 2023.11.30; 역할 Principal Investigator)
- 자율주행 기능지원을 위한 소프트웨어 오픈 API를 가지는 전기차용 샤시플랫폼 개발 (지원 한국자동차연구원; 기간 2022.06.01 - 2023.05.31; 역할 Co-Principal Investigator)
- 전기자동차의 최적 동력 분배 및 회수 전략 기초 연구 I (지원 (주)퓨처이브이; 기간 2022.05.01 - 2023.04.30; 역할 Principal Investigator)
- 수소버스 구동시스템 성능 평가기술 및 장비개발 (지원 국토교통과학기술진흥원; 기간 2021.01.01 - 2021.12.31; 역할 Co-Principal Investigator)
- 전기차 연관산업 육성기반 조성사업 (지원 제주특별자치도; 기간 2019.01.01 - 2021.12.31; 역할 Researcher)
- 인프라 센싱 기반 자율 주행 전기 자동차 개발 연구 (지원 한국과학기술원; 기간 2019.08.01 - 2021.12.31; 역할 Researcher)
- 자율주행 전기차용 고성능 조향제어기술 개발 (지원 한국자동차연구원; 기간 2019.1.–2021.12.)

## 수상과 선정

연구실 News & Events에 게시된 2023–2026년의 수상 소식 8건이다. 날짜는 소식의 게시일이며, 수상 이름과 등급은 게시 제목 표기다. 교수의 2025년 5월 KAIST 조교수 부임 전 성과가 섞여 있다.[^news1][^news2][^news3][^news4][^news5][^profile]

- 2026-08-28 · International Federation of Automatic Control (IFAC) World Congress 2026 Silver Award 수상 소식[^news1]
- 2026-07-03 · Institute of Control, Robotics and Systems (ICROS) 2026 Best Paper Awards 수상 소식[^news1]
- 2025-12-17 · International Conference on Robot Intelligence Technology and Applications (RiTA) 2025 Best Intelligence Paper Award 수상 소식[^news2]
- 2025-07-23 · IEEE International Workshop on Intelligent Systems (IWIS) 2025 Best Presentation Paper Award 수상 소식[^news3]
- 2024-09-06 · JMST Outstanding Contribution Award 수상 소식[^news3]
- 2024-07-03 · Institute of Control, Robotics and Systems (ICROS) 2024 Outstanding Young Researcher Award 수상 소식[^news4]
- 2024-07-03 · Institute of Control, Robotics and Systems (ICROS) 2024 Best Paper Award 수상 소식[^news4]
- 2023-07-03 · Institute of Control, Robotics and Systems (ICROS) 2023 Best Paper Awards 수상 소식[^news5]

논문 목록은 Myeongseok Ryu·Kyunghwan Choi의 「Data-driven Modeling of Model Residuals for Linear Model Predictive Control of Nonlinear Systems」에 ICROS 2023 Best Paper Award를, Jiyun Kim·Kyunghwan Choi의 「Mitigating Attention Collapse via Mean-Deviation Constrained Optimization」에 RiTA 2025 Best Intelligent Paper Award를 적는다. Jiyun Kim·Kyunghwan Choi의 「CARE Planner : Constrained Attention and Risk-aware Planning for Imitation-based Autonomous Driving」에는 ICROS 2026 Best Paper Award를 적는다.[^pubs]

## 연락과 위치

- 교수 업무 이메일: kh.choi@kaist.ac.kr[^home]
- 교수 기관 전화: +82-42-350-1764[^home]
- 위치: 대전광역시 유성구 문지로 193, 우편번호 34051. 교수실 F405, 연구실 F417.[^home]
[^home]: MIC Lab 첫 화면, 연구실 소개와 Contact Us. <https://kaist-mic-lab.github.io> 관측 2026-11-07.
[^profile]: Kyunghwan Choi, 교수 소개·경력·학력·참여 과제. <https://kaist-mic-lab.github.io/members/khChoi> 관측 2026-11-07.
[^control]: MIC Lab, Control Problems: Future Mobility Control Landscape. <https://kaist-mic-lab.github.io/research/control_problems/CP_control_problems/> 관측 2026-11-07.
[^vehicle]: MIC Lab, Vehicle-Level Optimal Control. <https://kaist-mic-lab.github.io/research/control_problems/CP_vehicle_level_optimal_control/> 관측 2026-11-07.
[^mobility]: MIC Lab, Mobility-System-Level Optimal Control. <https://kaist-mic-lab.github.io/research/control_problems/CP_mobility_system_level_optimal_control/> 관측 2026-11-07.
[^themes]: MIC Lab, Research Themes: Online Learning-Based Optimal Control. <https://kaist-mic-lab.github.io/research/research_themes/RT_research_themes> 관측 2026-11-07.
[^members]: MIC Lab Current Members, 현재 과정과 연구 소개. <https://kaist-mic-lab.github.io/members/researcher> 관측 2026-11-07.
[^alumni]: MIC Lab Alumni, 석사·학부 인턴 구획. <https://kaist-mic-lab.github.io/members/alumni> 관측 2026-11-07.
[^pubs]: MIC Lab, Publications, 논문·학위 논문·심사 중 원고·사전 공개본·특허·논문 수상 표시. <https://kaist-mic-lab.github.io/publications> 관측 2026-11-07.
[^projects]: MIC Lab, Projects, Ongoing·Completed 과제의 지원·기간·역할. <https://kaist-mic-lab.github.io/research/projects> 관측 2026-11-07.
[^component]: MIC Lab, Component-Level Optimal Control, 전동기·전력 변환 장치의 회전력 제어와 설정값 조정. <https://kaist-mic-lab.github.io/research/control_problems/CP_component_level_optimal_control> 관측 2026-11-07.
[^submitted]: MIC Lab, Online Adaptive Differentiable Predictive Control With Application to IPMSM MTPA Control, ITEC-AP 2026 submitted 및 게시 초록. <https://kaist-mic-lab.github.io/publications/2026-online-adaptive/> 관측 2026-11-07.
[^news1]: MIC Lab, News & Events 1쪽, 2026년 수상 소식과 게시 날짜. <https://kaist-mic-lab.github.io/news> 관측 2026-11-07.
[^news2]: MIC Lab, News & Events 2쪽, RiTA 2025 수상 소식과 게시 날짜. <https://kaist-mic-lab.github.io/news/page2> 관측 2026-11-07.
[^news3]: MIC Lab, News & Events 3쪽, IWIS 2025·JMST 2024 수상 소식과 게시 날짜. <https://kaist-mic-lab.github.io/news/page3> 관측 2026-11-07.
[^news4]: MIC Lab, News & Events 4쪽, ICROS 2024 수상 소식과 게시 날짜. <https://kaist-mic-lab.github.io/news/page4> 관측 2026-11-07.
[^news5]: MIC Lab, News & Events 5쪽, ICROS 2023 수상 소식과 게시 날짜. <https://kaist-mic-lab.github.io/news/page5> 관측 2026-11-07.
[^p1]: G. Park, K. Choi, D. Kum, IEEE Access (2026). <https://doi.org/10.1109/access.2026.3726602> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070417804> (위 DOI의 OpenAlex 등록 초록, 관측 2026-11-07).
[^p2]: J. Kim, K. Choi, Y. Lee, K.-B. Park, IEEE Transactions on Transportation Electrification (2026). <https://doi.org/10.1109/tte.2026.3695345> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070417804> (위 DOI의 OpenAlex 등록 초록, 관측 2026-11-07).
[^p3]: D. Hong, K. Choi, International Workshop on Intelligent Systems (IWIS), 1-4 (2026). <https://doi.org/10.1109/iwis70716.2026.11667752> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070417804> (위 DOI의 OpenAlex 등록 초록, 관측 2026-11-07).
[^p4]: M. Ryu, K. Choi, IEEE International Workshop on Advanced Motion Control (AMC), 1-6 (2026). <https://doi.org/10.1109/amc67705.2026.11435819> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070417804> (위 DOI의 OpenAlex 등록 초록, 관측 2026-11-07).
[^p5]: H. Lee, K. Choi, Annual Conference of the IEEE Industrial Electronics Society (IECON), 1-7 (2025). <https://doi.org/10.1109/iecon58223.2025.11221457> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070417804> (위 DOI의 OpenAlex 등록 초록, 관측 2026-11-07).
[^p6]: S. Jang, M. Ryu, K. Choi, Annual Conference of the IEEE Industrial Electronics Society (IECON), 1-7 (2025). <https://doi.org/10.1109/iecon58223.2025.11221587> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070417804> (위 DOI의 OpenAlex 등록 초록, 관측 2026-11-07).
[^p7]: M. Ryu 외, C. M. Hackl, Annual Conference of the IEEE Industrial Electronics Society (IECON), 1-7 (2025). <https://doi.org/10.1109/iecon58223.2025.11221692> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070417804> (위 DOI의 OpenAlex 등록 초록, 관측 2026-11-07).

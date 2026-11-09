# 지능형 로봇시스템 연구실 (Intelligent Robotic Systems Lab, IRSL)

**KAIST 전기및전자공학부 · 김민준 부교수**

- 분야: 로봇의 접촉과 움직임 제어, 로봇 팔의 물체 조작, 공중 로봇 설계[^research][^dept]
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 제어 이론·제어 공학[^interaction][^constraints], 로봇 조작·파지[^wholearm][^spacetime], 드론·무인 항공기[^sam], 인간–로봇 상호작용[^physicalai], 설계 최적화(위상·형상 최적화)[^sam]
- 홈페이지: <https://irsl-robotics.github.io/>
- 근거와 출처: [지능형 로봇시스템 연구실 근거 페이지](irsl-sources.md)

> 로봇이 사람·물체와 접촉하며 안전하게 움직이는 방법을 연구하고, 로봇 팔의 감지·조작과 높은 곳에서 일하는 공중 로봇의 설계로 연결하는 연구실이다.[^research][^wholearm][^sam]

## 무엇을 연구하나

김민준 교수가 이끄는 연구실은 로봇이 물리 세계와 안전하고 자율적으로 상호작용하는 방법을 연구한다. 연구는 움직임과 안전을 다루는 제어, 주변을 이해하고 행동을 배우는 지능, 실제 로봇의 기계 구조와 장치를 함께 다룬다. 지상 로봇과 공중 로봇 모두를 대상으로 하며, 단순한 위치 이동을 넘어 물체를 다루고 환경과 접촉하는 작업을 다룬다.[^research][^wholearm][^sam]

첫째 문제는 로봇이 예상하지 못한 힘이나 접촉을 만났을 때 어떻게 움직여야 하는가이다. 제어(관측한 상태를 바탕으로 입력을 정해 원하는 움직임이나 상태를 만드는 일)를 통해 정밀한 움직임과 접촉에 순응하는(접촉으로 받는 힘에 맞춰 움직임이 바뀌는) 움직임을 함께 구현하려 한다. 로봇이 사람을 돕고 주변과 접촉하는 상황에서 힘과 움직임을 조절하고 안정된 움직임을 유지하는 원리를 연구한다.[^interaction] 사람이 로봇에 닿는 위치를 감지하고 동시에 여러 접촉을 추적하는 방법을 연구한다.[^physicalai] 사람이 시범을 보이는 원격 조작(떨어진 곳에서 조작 장치로 로봇의 움직임을 제어하는 일)과 학습을 로봇 팔 전체의 행동으로 연결한다.[^wholearm]

둘째 문제는 로봇 팔의 어느 부분이 무엇과 닿았는지 알아내고 그 접촉을 행동에 활용하는 것이다. 손끝뿐 아니라 팔의 여러 부분을 감지와 작업에 함께 쓰는 방법을 연구한다.[^wholearm] 또 기계학습(자료나 경험에서 규칙과 예측·행동 방법을 익히는 계산 방법)으로 장면의 공간 구조를 표현하고, 물체를 여러 손가락으로 잡거나 카메라 한 대의 영상으로 정밀하게 조작하는 행동을 생성하는 모형을 연구한다.[^spacetime] 시간에 따라 주변의 입체 구조와 움직임을 유지·갱신하는 표현도 연구 방향으로 제시한다.[^spacetime]

셋째 문제는 원하는 작업을 할 수 있는 실제 로봇을 어떻게 설계하는가이다. 공중 작업에서는 날아가는 능력뿐 아니라 특정 방향으로 힘을 가하고 접촉 중에도 자세를 유지하는 능력이 필요하다. 연구실은 케이블에 매달린 공중 로봇의 기계 구성과 구동 방식에 작업 요구를 넣어 설계를 최적화(주어진 조건 안에서 목적에 가장 맞는 값을 찾는 계산)한다. 건물·교량·탑·풍력발전기처럼 사람이 접근하기 어려운 구조물의 검사·보수·도구 작업을 장기 목표로 제시한다.[^sam]

## 주요 연구 주제

### 1. 불확실성과 접촉을 고려한 제어

강인제어(모형의 오차나 외부 영향이 있어도 정해진 성능을 유지하도록 하는 제어), 외란 관측기(측정값과 모형을 이용해 알려지지 않은 외부 영향을 추정하는 계산 장치), 마찰 추정과 보상을 연구한다. 모델 예측 제어(모형으로 미래 상태를 예측하고 목표와 제한 조건을 고려해 다음 입력을 정하는 제어)에서는 접촉 위치와 힘, 외부 영향의 추정치를 미래 움직임 계산에 반영한다. 상태·입력과 접촉의 한계를 제어 계산에 직접 넣는 방법도 개발한다.[^interaction][^constraints] 대표 논문 1, 4, 8이 이 갈래를 보여 준다.[^p1][^p4][^p8]

### 2. 로봇 팔 전체의 접촉 감지와 조작

로봇 팔 전체에서 접촉 위치와 힘을 알아내고, 팔의 자세와 힘을 조절해 물체를 다루는 방법을 연구한다.[^wholearm] 고유감각 센서(자기 몸의 위치·움직임·힘 같은 상태를 측정하는 센서)로 얻은 정보에서 여러 접촉 위치를 찾아내며, 접촉을 단순히 피해야 할 충돌로만 취급하지 않고 작업에 활용하려 한다. 원격 조작으로 사람의 팔 사용 방식을 시범으로 얻고, 이를 새로운 접촉과 작업 조건에 적응하는 행동으로 학습하는 것이 연구 방향이다.[^wholearm] 대표 논문 3은 측정 정보에 맞는 여러 접촉 위치를 생성하는 방법을 다룬다.[^p3]

### 3. 공간 정보와 학습을 이용한 물체 조작

장면에서 행동과 관계있는 위치에 계산을 집중하고, 여러 가능한 물체 잡기 자세와 조작 행동을 표현하는 생성 모형(학습한 분포에서 새로운 자료나 행동을 만들어 내는 계산 모형)을 연구한다. 모방학습(다른 주체가 보여 준 행동을 자료로 삼아 행동 방법을 배우는 기계학습)을 통해 카메라 한 대의 영상에서도 조작에 필요한 공간 정보를 찾는 방향을 다룬다. 주변 세계의 입체 구조와 변화를 계속 유지하는 모형을 지각·예측·행동에 연결하는 것은 장기 목표다.[^spacetime] 대표 논문 2는 로봇 손끝의 이동 경로를 시각적 주의 위치로 활용한다.[^p2]

### 4. 공중 접촉 작업을 위한 로봇 설계

공중 로봇이 물체와 접촉하며 작업하도록 이동·자세 유지·힘 발생 요구를 기계 구성과 구동 설계의 최적화 문제에 넣는다.[^sam] 케이블 지지의 장점을 유지하면서 주변 작업 공간 안에서 능동적으로 이동하고, 원하는 위치와 방향에서 구조물에 접촉하는 로봇을 개발한다.[^sam] 대표 논문 5는 작업에 필요한 힘과 회전 효과를 고려한 드론 설계, 대표 논문 6은 기체의 압축·팽창으로 복원력을 얻는 기체 스프링과 조절 가능한 감쇠를 결합한 구동 장치, 대표 논문 7은 여러 공중 로봇의 협력 파지(함께 물체를 잡아 유지하는 일)를 다룬다. 감쇠는 운동에 따른 기계적 에너지가 소모되어 진동이나 운동이 줄어드는 작용이고, 에너지는 물리적인 일을 할 수 있는 능력을 나타내는 양이다.[^p5][^p6][^p7]

## 대표 논문

KAIST 재직 시기의 연구에서 접촉 제어, 학습 기반 조작, 접촉 감지, 공중 로봇·구동 장치의 갈래를 담도록 골랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 저자 역할은 게시된 저자 순서이며 교신저자 여부를 뜻하지 않는다.

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Contact-responsive high-gain robot motion controllers using a constrained disturbance observer](https://doi.org/10.1007/s11370-026-00744-z) · Intelligent Service Robotics | 목표 움직임을 정밀하게 따르는 로봇이 예상하지 못한 접촉에는 대응하도록 제어기를 제안했다. 제한 조건을 고려한 모형의 움직임을 먼저 정하고 실제 로봇이 이를 따르게 한다. 관절의 회전 힘을 재는 센서가 없는 협동 로봇에서 접촉 대응을 실험했다.[^p1] | 1저자 Ji Wan Han · 마지막 저자 Min Jun Kim |
| 2 | 2026 | [Spatially Conditioned Diffusion Policy: Learning Precise and Robust Manipulation with a Single RGB Camera](https://doi.org/10.48550/arxiv.2606.14535) · arXiv 판, CoRL 2026 채택 | 카메라 한 대의 전체 장면에서 로봇 손끝이 이동할 경로를 따라 시각 정보를 뽑아 조작 행동을 만드는 방법을 제안했다. 모의실험에서 여러 카메라를 쓰는 비교 방법과 비슷한 성능을 보였고, 실제 환경에서도 정밀 조작과 시각적 방해에 대한 견고함을 보였다.[^p2] | Seoyoon Kim·Kanghyun Kim(누리집 공동 1저자) · 마지막 저자 Min Jun Kim[^selected] |
| 3 | 2025 | [CDM: Contact Diffusion Model for Multi-Contact Point Localization](https://doi.org/10.1109/icra55743.2025.11127780) · IEEE ICRA | 로봇의 관절과 바닥 연결부에서 잰 힘 정보가 같아도 가능한 접촉 위치는 여러 개일 수 있다. 잡음을 단계적으로 제거하며 자료를 생성하는 확산 모형으로 그 가능성을 표현하고, 과거 추정과 로봇 표면의 형상을 함께 써 접촉 위치를 찾았다. 모의실험과 실제 로봇으로 확인했다.[^p3] | 1저자 Seo Wook Han · 마지막 저자 Min Jun Kim |
| 4 | 2024 | [Disturbance-Aware Model Predictive Control of Underactuated Robotics Systems](https://doi.org/10.1109/iros58592.2024.10801851) · IEEE/RSJ IROS | 독립적으로 가할 수 있는 입력이 움직임의 자유도(독립적으로 바뀔 수 있는 운동 좌표의 수)보다 적은 로봇에서 외부 영향을 추정하고, 그 값을 미래 움직임 예측에 직접 넣는 제어 방법을 제안했다. 예측과 실제 상태 사이 차이가 일정 범위에 머무는 성질을 분석했고, 회전하는 날개 네 개로 나는 로봇의 모의실험에서 효과를 보였다.[^p4] | 1저자 Jiwon Kim · 마지막 저자 Min Jun Kim |
| 5 | 2024 | [Design of a Fully Actuated Drone with Non-Isotropic Wrench Shape](https://doi.org/10.1109/iros58592.2024.10801419) · IEEE/RSJ IROS | 드론이 접촉 작업에 필요한 힘과 회전 효과를 낼 수 있으면서 제자리 비행에 드는 에너지를 줄이도록 설계하는 방법을 제안했다. 모든 방향에 균등한 힘을 내는 구성에 맞추는 대신 작업에 필요한 힘의 범위를 설계 조건에 넣었으며, 효과는 모의실험으로 확인했다.[^p5] | 1저자 Seong-Su Park · 마지막 저자 Min Jun Kim |
| 6 | 2025 | [A visco-elastic actuator with linear gas spring and variable damping](https://doi.org/10.1016/j.mechatronics.2025.103334) · Mechatronics | 기체가 든 두 공간과 액체 흐름을 조절하는 장치로 복원력과 감쇠를 갖춘 구동 장치를 제안했다. 강성(변형에 저항하는 정도)은 작동 전에, 감쇠는 작동 중에 조절한다. 이동 작업의 제어 성능과 충격 안전성 사이의 관계를 살피고 감쇠를 조절할 가능성을 보였다.[^p6] | 1저자 Florian Loeffl · 공저자 Min Jun Kim |
| 7 | 2023 | [Passivity-based Decentralized Control for Collaborative Grasping of Under-Actuated Aerial Manipulators](https://doi.org/10.1109/icra48891.2023.10160334) · IEEE ICRA | 여러 공중 로봇이 물체를 함께 잡도록 각 로봇을 분산 제어하는 방법을 제안했다. 외부에서 받은 에너지보다 더 많은 에너지를 내보내지 않는 성질을 바탕으로 로봇들을 연결하며, 임의 수의 로봇을 모듈식으로 결합하는 구조와 협력 파지 모의실험을 제시했다.[^p7] | 1저자 Jinyeong Jeong · 마지막 저자 Min Jun Kim |
| 8 | 2022 | [A Memory-based SO(3) Parameterization: Theory and Application to 6D Impedance Control with Radially Unbounded Potential Function](https://doi.org/10.1109/icra46639.2022.9812268) · IEEE ICRA | 과거 회전 경로를 누적해 여러 바퀴의 회전을 표현하는 방법을 제안했다. 이를 위치와 회전의 변위에 따른 힘 반응을 정하는 로봇 제어에 적용해 큰 회전 변위를 다루도록 했고, 모의실험과 실험으로 확인했다.[^p8] | 1저자 Jinyeong Jeong · 마지막 저자 Min Jun Kim |

## 교수와 전문 분야

김민준 교수는 2010년 고려대학교 학사, 2016년 POSTECH 박사 학위를 받았다. 2016년 3–5월 POSTECH 박사후연구원, 2016년 6월–2020년 7월 독일 DLR 연구원을 거쳐 2020년 8월 KAIST 조교수로 부임했으며 2025년 9월부터 부교수다.[^members] 학부는 주요 연구를 물리적 로봇 상호작용, 협동 로봇, 공중 조작으로 소개한다.[^dept] 최근 논문에서 드러나는 전문 분야는 불확실성과 접촉을 고려한 제어, 로봇 팔의 접촉 위치 추정, 학습 기반 조작, 공중 작업용 로봇의 설계와 협력 제어다.[^p1][^p2][^p3][^p4][^p5][^p7]

## 응용 분야

사람 가까이에서 접촉하며 일하는 로봇 팔, 물체를 여러 손가락으로 잡고 다루는 로봇, 높은 곳의 구조물을 검사하고 보수하는 공중 로봇이 주요 응용이다. 공중 로봇의 보수·표면 작업·도구 사용은 연구실이 제시하는 목표이며, 개별 논문의 실증 수준은 대표 논문 설명과 같다.[^interaction][^spacetime][^sam]

## 구성원

연구실 Members의 Ph.D. Candidates 11명과 MS Candidates 3명이다. 과정은 누리집 표기이며, 「대표 논문 참여」는 대표 논문의 전체 저자와 같은 이름을 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Kanghyun Kim | 박사과정 | 2 |
| Jinyeong Jeong | 박사과정 | 7, 8 |
| Ji Wan Han | 박사과정 | 1 |
| Seo Wook Han | 박사과정 | 3 |
| Seongsu Park | 박사과정 |  |
| Jiwon Kim | 박사과정 | 4 |
| Sungmin Kim | 박사과정 |  |
| Sanghoon Lee | 박사과정 |  |
| Taeho Yun | 박사과정 |  |
| Sunho Kim | 박사과정 |  |
| Jaehun Jeong | 박사과정 |  |
| Seoyoon Kim | 석사과정 | 2 |
| Jinyeol Kim | 석사과정 |  |
| Seungmin Shin | 석사과정 |  |

## 졸업생과 이전 구성원

연구실 Members의 Alumni에 게시된 석사 학위 기록 14건이다. 2023년 2월–2026년 8월의 기록이며, 박사과정 계속 여부는 누리집 표기다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jiwan Han | M.S. (2023.02) | 박사과정 계속 |
| Seo Wook Han | M.S. (2024.02) | 박사과정 계속 |
| Hyojun Lee | M.S. (2024.02) |  |
| Seongsu Park | M.S. (2024.08) | 박사과정 계속 |
| Suhwan Sung | M.S. (2024.08) |  |
| Jiwon Kim | M.S. (2025.02) | 박사과정 계속 |
| Sungmin Kim | M.S. (2025.02) | 박사과정 계속 |
| Sanghoon Lee | M.S. (2025.02) | 박사과정 계속 |
| Taeho Yun | M.S. (2025.08) | 박사과정 계속 |
| Young Bin Lee | M.S. (2025.08) |  |
| Seung Min Yang | M.S. (2025.08) |  |
| Sunho Kim | M.S. (2026.08) | 박사과정 계속 |
| Wonjun Han | M.S. (2026.08) |  |
| Jaehun Jeong | M.S. (2026.08) | 박사과정 계속 |

## 최근 논문 목록 (2021–2026)

연구실 All Publications의 국제 논문·발표 28편과 국내 논문·발표 8편, Members에 게시된 국제 논문·발표 6편으로 총 42편이다. 연도는 각 연도 구역 또는 개별 발표처 표기다. 제목·저자·발표처는 연구실 표기이며, 학술지의 Accepted는 「게재 승인」, 구성원 쪽에서 채택을 밝힌 학회 논문은 「채택」으로 표시했다. 포스터·워크숍은 누리집 표기를 함께 적었다.[^allpub][^members][^selected]

**2026**

- J. Jeong, and M. J. Kim. "Direction-Preserving 6D Impedance Control Using Observer-Based Extended Unit Quaternion". *IEEE RA-L, 2026, 게재 승인; DOI: 10.1109/lra.2026.3746072*.
- J. W. Han, and M. J. Kim. "Contact-responsive high-gain robot motion controllers using a constrained disturbance observer". *Intelligent Service Robotics; DOI: 10.1007/s11370-026-00744-z*.
- S. W. Han, and M. J. Kim. "Mixture of Flow Matching and Particle Filter for Proprioception-Based Online Contact Estimation". *IEEE T-RO, 2026*.
- S. Kim \* , K. Kim \* , D. Ko, Y. J. Heo, and M. J. Kim. "Spatially Conditioned Diffusion Policy: Learning Precise and Robust Manipulation with a Single RGB Camera". *CoRL 2026 (\* Co-first authors) (채택); DOI: 10.48550/arxiv.2606.14535*.
- S. Shin, J. Kim, and M. J. Kim. "Dual-Attachment Cable Suspension System for Zero-Gravity Emulation of Space Manipulators". *ICCAS 2026 (채택)*.
- S. Lee, J. Jeong, S. Shin, and M. J. Kim. "Motor-Side Friction Observer-based Hand Guiding with Joint Torque Measurements". *ICCAS 2026 (채택)*.
- Y. B. Lee \* , T. H. Yun \* , and M. J. Kim. "Extreme High-Gain Friction Observer of Flexible Joint Robots With L1 Adaptive Framework". *IEEE T-RO (\* Co-first authors) (게재 승인)*.

**2025**

- T. H. Yun, F. Beck, M. J. Kim † and J. Lee †. "Exact Fractional Order Impedance Rendering for Highly Flexible and Multi-Jointed Robots Using Time-Delay Estimation". *IEEE RA-L; DOI: 10.1109/lra.2025.3625498*.
- F. C. Loeffl, F. Beck, J. Lee, M. J. Kim, and M. Keppler. "A Visco-Elastic Actuator with Linear Gas Spring and Variable Damping". *Mechatronics; DOI: 10.1016/j.mechatronics.2025.103334*.
- T. M. Luu, Y. Lee, D. Lee, S. Kim, M. J. Kim, and C. D. Yoo. "Enhancing Rating-Based Reinforcement Learning to Effectively Leverage Feedback from Large Vision-Language Models". *ICML 2025*.
- S. W. Han, and M. J. Kim. "CDM: Contact Diffusion Model for Multi-Contact Point Localization". *IEEE ICRA 2025; DOI: 10.1109/icra55743.2025.11127780*.
- W. Han, and M. J. Kim. "Tension Estimation in Cable Suspended Aerial Systems Using a Nonlinear Disturbance Observer". *IEEE ICCAS 2025*.
- K. Kim , J. Lee, and M. J. Kim. "Augmented SE(3)-diffusion models for Fingered Grasp Generation from Raw 3D Scenes with a Single Tabletop Object". *IEEE SII 2025*.
- S. W. Han , and M. J. Kim. "Learning Multi-Contact Localization via Diffusion Models with Proprioceptive Sensing". *2025 RSS Workshop on Navigating Contact Dynamics in Robotics*.

**2024**

- K. Kim, M. J. Kim. "SPLIT: SE(3)-diffusion via Local Geometry-based Score Prediction for 3D Scene-to-Pose-Set Matching Problems". *arXiv preprint*.
- D. Lee, D. Ko, M. J. Kim, W. K. Chung. "Bidirectional Energy Flow Modulation for Passive Admittance Control". *IEEE T-RO; DOI: 10.1109/tro.2024.3443690*.
- J. Kim, and M. J. Kim. "Disturbance-Aware Model Predictive Control of Underactuated Robotics Systems". *IEEE/RSJ IROS 2024; DOI: 10.1109/iros58592.2024.10801851*.
- S. Park, and M. J. Kim. "Design of a Fully Actuated Drone with Non-Isotropic Wrench Shape". *IEEE/RSJ IROS 2024; DOI: 10.1109/iros58592.2024.10801419*.
- T. H. Yun, and M. J. Kim. "Disturbance Observer With Constraints". *IEEE L-CSS 2024; DOI: 10.1109/lcsys.2024.3418878*.
- S. W. Han, M. Iskandar, J. Lee and M. J. Kim. "Online Multi-Contact Feedback Model Predictive Control for Interactive Robotic Tasks". *IEEE ICRA 2024; DOI: 10.1109/icra57147.2024.10611151*.
- J. W. Han, D. Park, and M. J. Kim. "Constrained Nonlinear Disturbance Observer for Robotic Systems". *IEEE ICRA 2024; DOI: 10.1109/icra57147.2024.10611091*.
- M. Song, Y. Kim, M. J. Kim, and D. Park. "Graph-Based 3D Collision-Distance Estimation Network with Probabilistic Graph Rewiring". *IEEE ICRA 2024; DOI: 10.1109/icra57147.2024.10611465*.
- J. Jeong, S. Park, S. Lee, D. Youn, and M. J. Kim. "Designing an End-to-End UAV System for Insulator Inspection under Transmission Tower Environments". *IEEE ICEIC 2024; DOI: 10.1109/iceic61013.2024.10457221*.
- S. W. Han, M. Iskandar, J. Lee, and M. J. Kim. "Optimization-based Multi-Contact Force Control". *The 19th KRoC*.
- J. Han, and M. J. Kim. "QP-Based Precision Robot Motion Control with Robot Environment Interaction Capability and Sensorless Setup". *The 19th KRoC*.
- K. Kim, and M. J. Kim. "Manipulation planning, Optimization-based planning, Neural graspable set". *The 19th KRoC*.
- T. Kim, J. W. Han , and M. J. Kim. "Safe Robot Teleoperation with Constrained Nonlinear Disturbance Observer". *IEEE RiTA 2024*.
- J. W. Han , and M. J. Kim. "Learning-based method for Estimating Free Motion Disturbances Using Historical Velocity Memory". *(poster presentation), IEEE ICCAS 2024*.
- S. W. Han , and M. J. Kim. "Contact Estimation Diffusion Model for Collaborative Robots". *(poster presentation), IEEE ICCAS 2024*.
- S. M. Kim , and M. J. Kim. "Learning Reactive Motion Policies by Leveraging Latent Data Manifolds". *(poster presentation), IEEE ICCAS 2024*.

**2023**

- K. Kim, D. Park, and M. J. Kim. "A Reachability Tree-Based Algorithm for Robot Task and Motion Planning". *IEEE ICRA 2023*.
- S. W. Han, and M. J. Kim. "Proprioceptive Sensor-Based Simultaneous Multi-Contact Point Localization and Force Identification for Robotic Arms". *IEEE ICRA 2023; DOI: 10.1109/icra48891.2023.10161173*.
- J. Jeong, and M. J. Kim. "Passivity-based Decentralized Control for Collaborative Grasping of Under-Actuated Aerial Manipulators". *IEEE ICRA 2023; DOI: 10.1109/icra48891.2023.10160334*.
- Y. Sarkisov, A. Coelho, M. Santos, M. J. Kim, D. Tsetserukou, C. Ott, and K. Kondak. "Hierarchical Whole-body Control of the cable-Suspended Aerial Manipulator endowed with Winch-based actuation". *IEEE ICRA 2023; DOI: 10.1109/icra48891.2023.10160718*.
- S. W. Han, and M. J. Kim. "Multi-Contact Point Localization and Force Identification for Collaborative Robot Arm using Proprioceptive Sensor". *The 18th KRoC*.
- J. Jeong, and M. J. Kim. "Decentralized Passive Impedance Control Method for Collaborative Grasping of Aerial Manipulators". *The 18th KRoC*.
- K. Kim, D. Park, and M. J. Kim. "Reachability tree-based Task and Motion Planner using Abstract Action Plan Sampling". *The 18th KRoC*.
- H. Lee, S. Kim, and M. J. Kim. "Safe Parameter Automated Tuning of Robust Control of Manipulator without Expert Intervention". *KSPE 2023 Autumn Conference*.

**2022**

- J. Jeong, H. Mishra, C. Ott, and M. J. Kim. "A Memory-based SO(3) Parameterization: Theory and Application to 6D Impedance Control with Radially Unbounded Potential Function". *IEEE ICRA 2022; DOI: 10.1109/icra46639.2022.9812268*.
- M. J. Kim, A. Werner, F. Loeffl, and C. Ott. "Passive Impedance Control of Robots with Viscoelastic Joints via Inner-loop Torque Control". *IEEE T-RO; DOI: 10.1109/tro.2021.3071617*.
- S. Lee, J. Jeong, and M. J. Kim. "Implementation of Impedance Controller for Redundant Robot Manipulators Using Extended Exponential Coordinates". *The 37th ICROS*.

**2021**

- J. Jeong, M. J. Kim. "Interaction control of under-actuated UAV capable of exerting downward force". *ANBRE21*.

## 특허

연구실 All Publications의 국내 특허 4건이다. 출원일 또는 등록일이 2023년 10월–2024년 12월인 기록이다.[^allpub]

- 2024 · 김민준, 한지완 “최소한의 센서 사용으로 안전을 위한 복수의 제약조건 설정이 가능한 로봇 정밀 제어 프레임워크”, 국내특허, 출원번호: 10-2024-0196135/1, 출원일자: 2024.12.24
- 2024 · 김민준, 정진영 “회전 변위의 제약이 없는 다관절 로봇의 작업공간 유연제어방법”, 국내특허, 등록번호: 10-2624551, 등록일자: 2024년 1월 9일
- 2023 · 김민준, 이효준, 김성민, “전문가 개입 없이 안전한 매니퓰레이터의 강인제어 매개변수 자동 튜닝 방법”, 국내특허, 출원번호: 10-2023-0181280, 출원일자: 2023.12.13
- 2023 · 김민준, 한지완, 김지원, “운동량 기반으로 추정한 외력을 이용하여 주변 환경과 상호 작용이 가능한 로봇 제어 시스템 및 방법”, 국내특허, 출원번호: 10-2023-0134387, 출원일자: 2023.10.10

## 수상과 선정

연구실 Members와 All Publications가 논문 옆에 적은 2022년 학회 수상 2건이다. 연도는 발표처의 연도 표기이며, 별도의 수상 일자는 게시되어 있지 않다.[^members][^allpub]

- 2022 · T. H. Yun · Undergraduate Excellent Dissertation Award · The 17th Korea Robotics Society Annual Conference (KRoC2022)
- 2022 · S. Lee, J. Jeong, M. J. Kim · outstanding undergraduate paper award · The 37th ICROS

## 연락과 위치

- 교수 이메일: minjun.kim@kaist.ac.kr[^members]
- 위치: 전기및전자공학부동(E3-2) 3234호[^dept]
- 교수 연락처: 7464(학부 교수 소개 표기)[^dept]

## 각주
[^dept]: KAIST 전기및전자공학부, 김민준 교수 소개. <https://ee.kaist.ac.kr/professor/17498/> (관측 2026-11-09).
[^members]: 연구실, Members. <https://irsl-robotics.github.io/profiles/> (관측 2026-11-09).
[^research]: 연구실, Research. <https://irsl-robotics.github.io/research/> (관측 2026-11-09).
[^allpub]: 연구실, All Publications. <https://irsl-robotics.github.io/all_publications/> (관측 2026-11-09).
[^selected]: 연구실, Selected Publications. <https://irsl-robotics.github.io/selected_publications/> (관측 2026-11-09).
[^interaction]: 연구실, Physical Interaction Control. <https://irsl-robotics.github.io/projects/physical-interaction-control/> (관측 2026-11-09).
[^constraints]: 연구실, Constraint-Aware Control. <https://irsl-robotics.github.io/projects/constraint-aware-control/> (관측 2026-11-09).
[^wholearm]: 연구실, Whole-Arm Physical Intelligence. <https://irsl-robotics.github.io/projects/whole-arm-physical-intelligence/> (관측 2026-11-09).
[^spacetime]: 연구실, Spatio-Temporal Embodied Intelligence. <https://irsl-robotics.github.io/projects/spatio-temporal-embodied-intelligence/> (관측 2026-11-09).
[^sam]: 연구실, SAM2. <https://irsl-robotics.github.io/projects/sam2/> (관측 2026-11-09).
[^physicalai]: 연구실, Physical AI. <https://irsl-robotics.github.io/research/physical-ai/> (관측 2026-11-09).
[^p1]: J. W. Han, M. J. Kim, Intelligent Service Robotics 19, 89 (2026). <https://doi.org/10.1007/s11370-026-00744-z> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101828960,publication_year:2021-2026> (관측 2026-11-09).
[^p2]: S. Kim 외, M. J. Kim, arXiv (2026). <https://doi.org/10.48550/arxiv.2606.14535> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2606.14535> (관측 2026-11-09).
[^p3]: S. W. Han, M. J. Kim, IEEE ICRA (2025). <https://doi.org/10.1109/icra55743.2025.11127780> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101828960,publication_year:2021-2026> (관측 2026-11-09).
[^p4]: J. Kim, M. J. Kim, IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (2024). <https://doi.org/10.1109/iros58592.2024.10801851> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101828960,publication_year:2021-2026> (관측 2026-11-09).
[^p5]: S.-S. Park, M. J. Kim, IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (2024). <https://doi.org/10.1109/iros58592.2024.10801419> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101828960,publication_year:2021-2026> (관측 2026-11-09).
[^p6]: F. Loeffl 외, M. Keppler, Mechatronics (2025). <https://doi.org/10.1016/j.mechatronics.2025.103334> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101828960,publication_year:2021-2026> (관측 2026-11-09).
[^p7]: J. Jeong, M. J. Kim, IEEE ICRA (2023). <https://doi.org/10.1109/icra48891.2023.10160334> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101828960,publication_year:2021-2026> (관측 2026-11-09).
[^p8]: J. Jeong, H. Mishra, C. Ott, M. J. Kim, IEEE ICRA (2022). <https://doi.org/10.1109/icra46639.2022.9812268> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101828960,publication_year:2021-2026> (관측 2026-11-09).

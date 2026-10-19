# DAIM 연구실 (DAIM Labs)

**KAIST 산업및시스템공학과 · 장영재 교수**

- 분야: 반도체 공장 천장 반송 로봇(OHT) 운영, 무인 운반차(AGV)·자율 이동 로봇(AMR) 경로 계획, 강화학습(시행착오로 최적 행동을 배우는 인공지능) 기반 물류 제어, 디지털 트윈과 시뮬레이션, 피지컬 AI 자율 제조
- 홈페이지: <https://daim.kaist.ac.kr/>
- 근거와 출처: [DAIM 근거 페이지](daim-sources.md)

> 반도체·디스플레이 공장 안에서 수백 대의 운반 로봇이 서로 막히지 않고 제때 물건을 나르도록 길을 정하고 일을 배정하는 방법을 연구하는 연구실이다. 강화학습 같은 인공지능과 공장을 가상으로 똑같이 옮긴 디지털 트윈을 써서, 실제 공장에 들어가는 로봇 운영 시스템을 기업과 함께 만든다.[^home][^p1][^p2]

## 무엇을 연구하나

연구실 첫 화면은 "로봇과 로봇을 연결하여 제조혁신을 선도합니다"라는 문구를 내건다.[^home] 연구 분야 페이지는 산업 적용 사례로 AI 협업지능 기반 반도체 OHT 시스템, 디스플레이 물류 크레인 시스템, 양방향 격자형 AGV 운영 시스템, 디지털 트윈 기반 알고리즘 학습·검증, 물류 로봇 특화 AI 예지보전(고장을 미리 알아채는 기술)을 든다.[^research] 과제 목록에는 SYNUS Tech, LG전자, General Motors, 한국타이어, LG CNS, 삼성중공업, 삼성전자 등과 함께한 공장 물류·생산 일정 연구가 있다.[^projects]

첫 번째 갈래는 **반도체 공장의 천장 반송 로봇(OHT) 운영**이다. OHT(Overhead Hoist Transport)는 반도체 웨이퍼 공장 천장의 레일을 따라 달리며 공정 장비 사이로 웨이퍼 묶음(로트)을 나르는 로봇으로, 한 공장에서 수백 대가 움직인다. 연구실은 교통 상황을 보고 어느 차량에 어떤 운송을 맡길지 정하는 Q러닝(시행착오로 최적 행동을 배우는 강화학습의 한 방법) 기반 배차 알고리즘을 만들었고,[^p2] 디지털 트윈과 시뮬레이션으로 이동 시간을 예측해 막히는 길을 피하는 경로 제어(액티브 Q 라우팅)를 실제 대형 반도체 공장 사례로 검증했다.[^p1] 레일 구조와 운영 규칙을 반영해 짧은 시간 뒤의 이동 시간을 예측하는 모델도 내놓았다.[^p3]

두 번째 갈래는 **무인 운반차(AGV)와 이동 로봇의 경로 계획**이다. 창고에서 수많은 AGV가 선반을 나를 때 서로 길을 막아 아무도 움직이지 못하는 교착 상태(deadlock)가 생길 수 있다. 연구실은 일부 차량의 경로를 미리 예약해 다른 차량의 이동 방향을 제한하는 방식으로 교착을 막으면서 차량 수가 많아도 잘 동작하는 알고리즘을 만들었다.[^p4][^p5] 여러 회사의 서로 다른 로봇(OHT, AGV 등)을 소프트웨어 하나로 함께 제어하는 "소프트웨어 정의 공장" 제어 시스템도 축소 반도체 공장에서 시연했다.[^p6]

세 번째 갈래는 **제조 운영 최적화와 교육**이다. 삼성전자 표면 실장 생산 라인의 부품 공급(키팅) 작업을 순차적 의사결정 문제로 풀었고,[^p7] 교수가 맡은 학부 과목 「제조 프로세스 혁신」에 디지털 트윈·AI·로봇 실습을 넣어 학생 성적이 오른 결과를 보고했다.[^p8][^prof]

연구실 소식은 KAIST 산업경영학동 1층의 피지컬 AI 기반 무인공장 테스트베드 '카이로스'가 2026년 3월 23일 시연과 함께 공개됐다고 전한다.[^home] 교수는 지역·대학·연구기관 협력의 제조 피지컬 AI 실증 체계를 만들고 로봇 운영 플랫폼 '카이로스'를 개발한 성과로 2026년 과학·정보통신의 날에 정보통신 유공 홍조근정훈장을 받았다.[^gsds-medal]

## 주요 연구 주제

### 1. 반도체 OHT 배차·경로 제어

강화학습 배차, 디지털 트윈 경로 제어, 이동 시간 예측.[^p1][^p2][^p3][^research] 대표 논문 1, 2, 3.

### 2. AGV·이동 로봇 경로 계획과 통합 제어

교착 방지 경로 탐색, 이기종 로봇 통합 제어.[^p4][^p5][^p6] 대표 논문 4, 5, 6.

### 3. 제조 운영 최적화와 공학 교육

자동 키팅 일정, Industry 4.0 수업 설계.[^p7][^p8] 대표 논문 7, 8.

## 대표 논문

랩 학술 성과 목록의 2021–2026년 국제 학술지·학술대회 논문에서 주제별로 골랐다. 1은 랩 목록이 저자를 줄여 적어 Crossref 저자 순서를 따랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2025 | [Autonomous Robot Orchestration Solution for OHT With Active Q Routing and Digital Twin](https://doi.org/10.1109/tsm.2025.3594651) · IEEE Transactions on Semiconductor Manufacturing | 반도체 공장의 대규모 OHT 차량을 강화학습, 시뮬레이션, 실시간 디지털 트윈으로 함께 움직이게 하는 로봇 운영 시스템(AROS). 시뮬레이션으로 이동 시간을 예측해 막히는 길을 피하는 액티브 Q 라우팅으로 평균 배송 시간을 줄이고 처리량을 늘렸으며, 실제 대형 반도체 공장 사례로 확인했다.[^p1] | 1저자 Jaeho Lee, 장영재 공저(8명 중 여섯째), 마지막 저자 Jaeung Lee |
| 2 | 2022 | [Practical Q-Learning-Based Route-Guidance and Vehicle Assignment for OHT Systems in Semiconductor Fabs](https://doi.org/10.1109/tsm.2022.3168702) · IEEE Transactions on Semiconductor Manufacturing | 반도체 공장에서 수백 대의 OHT 가운데 어느 차량에 운송을 맡길지를 교통 상황을 보고 정하는 Q러닝 기반 배차 알고리즘 여러 개를 제안하고 기존 방식과 비교했다. 실제 대규모 공장에서 쓸 만큼 효율적이고 빠르다.[^p2] | 1저자 Sangpyo Hong, 마지막 저자 장영재 |
| 3 | 2024 | [Short-Term Travel Time Prediction Model for OHT Systems in Semiconductor Fabs](https://doi.org/10.1109/case59546.2024.10711669) · IEEE CASE 2024 | OHT 레일 구조와 운영 규칙을 반영해 짧은 시간 뒤의 이동 시간(곧 다가올 혼잡도)을 예측하는 모델. 지연 유형을 전체 흐름과 차량 하나하나의 움직임으로 나눠 정의했고, 예측값을 쓴 경로 알고리즘이 기존 방법보다 나았다.[^p3] | 1저자 Jaeho Lee, 마지막 저자 장영재 |
| 4 | 2024 | [Deadlock Prevention and Multi Agent Path Finding Algorithm Considering Physical Constraint for a Massive Fleet AGV System](https://doi.org/10.1016/j.asoc.2024.111725) · Applied Soft Computing | 물류 창고에서 선반을 나르는 수많은 AGV가 서로 막혀 멈추는 교착을 막는 경로 알고리즘. 예약된 경로를 달리는 차량은 일부 길만 쓰게 하고 나머지 차량은 제한 없는 길로 계획해, 교착을 막으면서 차량이 많아도 잘 동작했다.[^p4] | 1저자 Chang Hyun Chung, 마지막 저자 장영재 |
| 5 | 2022 | [Deadlock Avoidance Dynamic Routing Algorithm for a Massive Bidirectional Automated Guided Vehicle System](https://doi.org/10.1109/wsc57314.2022.10015233) · Winter Simulation Conference 2022 | 양방향으로 다니는 AGV가 계속 새 일을 받는 환경에서 교착을 막는 방법. 일부 차량의 경로 방향을 제한하는 경로 예약과 예약 상태에 맞춰 최단 경로를 찾는 방법을 결합했고, 상용 시뮬레이션 소프트웨어로 효율과 확장성을 확인했다.[^p5] | 1저자 Kang Min Kim, 마지막 저자 장영재 |
| 6 | 2026 | [Heterogeneous multi-agent fleet control system for material handling in a Software-Defined Factory](https://doi.org/10.1016/j.jmsy.2026.01.005) · Journal of Manufacturing Systems | 하드웨어마다 따로 제어하던 공장 물류를 소프트웨어 하나로 통합하는 "소프트웨어 정의 공장" 개념과 제어 시스템. 여러 회사 로봇의 통신·위치·주행·작업 배정을 한곳에서 관리하고, 축소 반도체 공장에서 OHT와 AGV를 함께 운영해 보였다.[^p6] | 1저자 Muhammad Umar Farooq, 마지막 저자 장영재 |
| 7 | 2023 | [Sequential Decision-Making Framework for Robotic Mobile Fulfillment System-Based Automated Kitting System](https://doi.org/10.1109/wsc60868.2023.10407259) · Winter Simulation Conference 2023 | 삼성전자 표면 실장 부품 생산 라인에 도입된 이동 로봇 기반 자동 키팅(필요한 부품을 묶어 제때 공급하는 작업)을 순차적 의사결정 문제로 풀고 일정 알고리즘을 제안했다. 시뮬레이션에서 문제 규모가 커져도 성능과 안정성이 유지됐다.[^p7] | 1저자 Jaeung Lee, 장영재 공저(넷째), 마지막 저자 Eoksu Sim |
| 8 | 2026 | [Advancing Manufacturing Process Education for Industry 4.0: A Multi-Case Study](https://doi.org/10.1002/cae.70136) · Computer Applications in Engineering Education | 2024·2025년 봄 학부 수업 「제조 프로세스 혁신」에 디지털 트윈, AI, 시뮬레이션, IoT와 자율 이동 로봇 실습을 넣고 팀 기반·문제 기반 학습을 도입했다. 기존 강의식보다 성적이 23.75%(2024)와 16%(2025) 올랐다.[^p8] | 1저자 Muhammad Umar Farooq, 마지막 저자 장영재 |

## 교수와 전문 분야

장영재 교수는 미국 보스턴대 항공우주공학 학사(1997), MIT 기계공학 석사(1999)·운영과학 석사(2001)·기계공학 박사(2007)를 받았다. 미국 Micron Technology에서 프로젝트 매니저(2007–2010)로 일한 뒤 2010년 11월 KAIST에 부임해 조교수, 부교수(2017.3–2025.2)를 거쳐 2025년 3월부터 교수다.[^prof] 「제조 프로세스 혁신」과 「공급체인관리」를 가르치고, 책 Management Concert(Businessbooks Press, 2010)를 냈다.[^prof]

교수 연구팀과 KAIST 연구소 기업 다임리서치는 AI 자율 제조 연구로 2025년 INFORMS Analytics Conference에서 우수 혁신사례상(IAAA)을 받았다.[^gsds-iaaa]

논문으로 보면 전문 분야는 세 갈래다.

- **반도체 자동 물류(AMHS, 공장 안 물건을 자동으로 나르는 설비 전체) 운영**: OHT 배차·경로, 이동 시간 예측.[^p1][^p2][^p3]
- **다중 로봇 경로 계획과 제어 시스템**: AGV 교착 방지, 이기종 로봇 통합 제어.[^p4][^p5][^p6]
- **제조 운영 의사결정과 공학 교육**: 키팅 일정, 시뮬레이션 기반 검증, Industry 4.0 제조 교육.[^p7][^p8]

## 응용 분야

대표 논문과 과제로 보면 반도체·디스플레이 공장 자동 물류, 물류 창고 로봇, 자동차·타이어 공장 생산 일정, 전자 부품 생산 라인에 닿아 있다.[^p1][^p4][^p7][^projects] 연구실 소식에는 2025년 '피지컬 AI 핵심기술 실증' 시범사업 수주가 있다.[^news]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다. 연구 주제는 랩 표기를 옮겼다. 연구실 대표(Captain)는 박사과정 Hyunjae Lee다.[^team][^home] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Muhammad Umar Farooq | 연구원 | Mobile & Industrial Robots, Robot Design, ROS | muhammadumarfarooq@kaist.ac.kr | 6, 8 |
| ChangHyun Chung | 연구원 | Automated Guided Vehicle Routing, Deadlock Avoidance, Reinforcement Learning | cch0720@kaist.ac.kr | 4, 5 |
| Hyunjae Lee | 박사과정 | Reinforcement Learning, Simulation | hyunjae.lee@kaist.ac.kr |  |
| Lennard Heuer | 박사과정 | Natural Language Processing, Data Mining | lennard.heuer@kaist.ac.kr |  |
| AeHyang Park | 박사과정 | Heterogeneous Multi-Robot Scheduling | ahpark@kaist.ac.kr |  |
| JoongHoo Park | 박사과정 | AMHS operations | joonghoo@kaist.ac.kr |  |
| San Kwon | 석사과정 | AMHS Operations, Layout Generation | ksanbenji@kaist.ac.kr |  |
| Hyeseo Yoon | 석사과정 | AMHS Simulation | khidb57@kaist.ac.kr |  |
| Chien-Shih Sun | 석사과정 | AMHS Simulation | chien-shih@kaist.ac.kr |  |
| WonSeok Jang | 석사과정 | Reinforcement Learning, Predictive Maintenance | cotidie@kaist.ac.kr |  |
| SahngJin Ban | 석사과정 | AMHS Simulation | sahngjin.ban@kaist.ac.kr |  |
| MinGyu SUH | 석사과정 | AMHS Simulation | mg0208@kaist.ac.kr |  |
| HyeongJin Kim | 석사과정 | AMHS Simulation | hyeongjin0803@kaist.ac.kr |  |
| Heesoo Lee | 석사과정 | AMHS Operations | hslee_@kaist.ac.kr |  |
| Gaeun Kim | 학부 연구생 | AMHS Simulation | gaeun-48@kaist.ac.kr |  |
| Gookhee Shin | 학부 연구생 | AMHS Simulation | annshin06@kaist.ac.kr |  |
| Seongwon Hong | 인턴 |  |  |  |
| HyeMin Kim | 행정 직원 |  |  |  |
| HyunSuk Jung | 행정 직원 |  |  |  |

## 졸업생

랩 졸업생 페이지는 이름, 학위, 졸업 연도만 적는다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| ChangHyun Chung | Ph.D. (2026) |  |
| Jaeung Lee | Ph.D. (2026) |  |
| Sungwook Jang | Ph.D. (2026) |  |
| Sungwoo Park | M.S. (2026) |  |
| Soyoung Bang | M.S. (2026) |  |
| Sanguk Im | M.S. (2026) |  |
| JaeHo Lee | Ph.D. (2025) |  |
| Tae Hoon Kim | M.S. (2025) |  |
| Gyuho Lee | M.S. (2025) |  |
| Nakjoon Im | M.S. (2025) |  |
| Japhne Ferdinandz | M.S. (2025) |  |
| Taejong Park | Ph.D. (2024) |  |
| Sejong Lim | M.S. (2024) |  |
| MinSoo Kim | Ph.D. (2023) |  |
| DongHwi Shin | M.S. (2023) |  |
| EunHyo Chang | M.S. (2023) |  |
| MinSeok Lee | Ph.D. (2023) |  |
| YeEun Won | M.S. (2023) |  |
| JinHyeok Park | Ph.D. (2022) |  |
| MunKi Jo | M.S. (2022) |  |
| SangPyo Hong | Ph.D. (2022) |  |
| SoEui Yeon | M.S. (2022) |  |
| DongMin Kim | M.S. (2022) |  |
| JiYoon Myung | M.S. (2022) |  |
| DaeMook Kang | M.S. (2021) |  |
| HanGyul Moon | M.S. (2021) |  |
| Seol Hwang | Ph.D. (2021) |  |
| KangMin Kim | M.S. (2021) |  |
| SeokJoong Kim | M.S. (2021) |  |
| SungWook Jang | M.S. (2021) |  |
| HyeMin Cho | M.S. (2021) |  |
| Vina Sari Yosephine | Ph.D. (2020) |  |
| JaeUng Lee | M.S. (2020) |  |
| JunHui Lee | M.S. (2020) |  |
| IllHoe Hwang | Ph.D. (2019) |  |
| JungHoon Kim | Ph.D. (2018) |  |
| SeungMin Jeong | Ph.D. (2018) |  |
| ShinWoong Sung | Ph.D. (2018) |  |
| HyeonJun Sim | M.S. (2018) |  |
| HakYoung Choi | M.S. (2017) |  |
| HyunSuk Baek | M.S. (2017) |  |
| Meixiang Jin | M.S. (2017) |  |
| KyoungMin Cho | M.S. (2017) |  |
| JaeRyong Yeo | M.S. (2016) |  |
| SunKyung Oh | M.S. (2015) |  |
| JuYeong Lee | M.S. (2015) |  |
| DaeYoung Kim | M.S. (2014) |  |
| HyunJu Cho | M.S. (2014) |  |
| GwangJae Yu | M.S. (2013) |  |

## 최근 논문 목록 (2021–2026)

랩 학술 성과 목록의 2021–2026년 국제 학술지, 국제 학술대회, 국내 학술대회 발표 78편이다. 일부 항목은 랩 목록이 저자를 "et al."로 줄여 적었다.[^papers]

**2026**

- Chien-Shih Sun and Young Jae Jang. "Automated Vision-Based Congestion Detection System for Overhead Hoist Transports". *IEEE International Conference on Automation Science and Engineering (CASE), 2026, Shenyang, China*.
- San Kwon, Young Jae Jang. "Congestion-Aware Automated Roadmap Design for Automated Material Handling Systems". *IEEE International Conference on Automation Science and Engineering (CASE), 2026, Shenyang, China*.
- Japhne Ferdinandz, JoongHoo Park, Young Jae Jang. "A Digital Twin Framework for Dynamic Routing of Overhead Hoist Transport in Semiconductor Fabs". *IEEE International Conference on Automation Science and Engineering (CASE), 2026, Shenyang, China*.
- Farooq Muhammad Umar and Young Jae Jang. "Heterogeneous multi-agent fleet control system for material handling in a Software-Defined Factory". *Journal of Manufacturing Systems, vol. 85, 2026, pp. 513-530*.
- Farooq Muhammad Umar and Young Jae Jang. "Advancing Manufacturing Process Education for Industry 4.0: A Multi-Case Study". *Computer Applications in Engineering Education, vol. 34, 2026, p. e70136*.
- Hyeseo Youn and Young Jae Jang. "3D Shuttle 기반 자동화창고 환경에서의 작업자 충돌위험 판단 프레임워크". *대한산업공학회 2026 춘계학술대회, June. 2026, Gyeongju, Korea*.
- Hyunjae Lee and Young Jae Jang. "Double Deep Rank 구조의 단일 SKU Carrier에 대한 Schedule-Aware Storage Location Assignment 최적화". *대한산업공학회 2026 춘계학술대회, June. 2026, Gyeongju, Korea*.
- San Kwon and Young Jae Jang. "제조 물류 병목을 고려한 AMR 트랙 레이아웃 자동 설계". *대한산업공학회 2026 춘계학술대회, June. 2026, Gyeongju, Korea*.
- San Kwon and Young Jae Jang. "공장 CAD 이미지 기반의 AMR 레이아웃 자동 생성 연구". *한국CDE학회 2026 동계학술대회, Feb. 2026, Jeju, Korea*.
- Changhyun Chung and Young Jae Jang. "무인 운반차 시스템에서의 교착 상태 예방 경로 탐색". *한국CDE학회 2026 동계학술대회, Feb. 2026, Jeju, Korea*.

**2025**

- Sanguk Im, Young Jae Jang. "Health Index-based Risk-aware Dispatching for Overhead Hoist Transport Systems in Semiconductor Fab". *WSC, 8 Dec. 2025, Seattle, Washington, United States*.
- Sung Woo Park, Sungwook Jang, Young Jae Jang. "Proactive Hot Lot Routing for OHT Systems in Semiconductor FAB". *WSC, 8 Dec. 2025, Seattle, Washington, United States*.
- Soyeong Bang, Young Jae Jang. "Hybrid Control Method for Autonomous Mobile Robot (AMR) in Manufacturing Logistics Systems". *WSC, 8 Dec. 2025, Seattle, Washington, United States*.
- Lennard Heuer, Young Jae Jang. "Bridging the Gap Between Business Users and Optimization: a Novel LLM-Powered Interactive Framework for Production Planning". *INFORMS Annual Meeting, 28 Oct. 2025, Atlanta, Georgia, United States*.
- Jaeung Lee, Sungwook Jang, Young Jae Jang. "Simulation-based Evaluation of Idle Vehicle Positioning Problem on Logistics Performance in OHT Systems". *ASMC, 8 May. 2025, Albany, New York, United States*.
- Sungwook Jang, Young Jae Jang. "Mathematical and Simulation-Based Analysis of Multiple-Load Mobile Transport Systems in Semiconductor Manufacturing". *ASMC, 6 May. 2025, Albany, New York, United States*.
- Muhammad Umar Farooq, Young Jae Jang. "Node-based navigation system for multiple mobile robot control on a shop floor". *ICARA, 12-14 Feb. 2025, Zagreb, Croatia*.
- Lee, Jaeho, et al. "Autonomous Robot Orchestration Solution for OHT With Active Q Routing and Digital Twin". *IEEE Transactions on Semiconductor Manufacturing, vol. 38, 2025, pp. 404-412*.
- Hyunjae Lee and Young Jae Jang. "Multi-modal 환경에서의 MCS 관점 기반 반도체 Fab 물류 운영 최적화". *대한산업공학회 2025 추계학술대회, 6 Nov. 2025, Daejon, Korea*.
- Changhyun Chung and Young Jae Jang. "하드웨어 제약을 반영한 AGV 시스템의 충돌 예방 경로 최적화". *대한산업공학회, 한국경영과학회, 한국시뮬레이션학회 2025 춘계공동학술대회, 20 June. 2025, Jeju, Korea*.
- Jaeung Lee and Young Jae Jang. "반도체 팹 내 OHT 유휴 차량의 동적 대기 위치 결정을 위한 k-Median 기반 알고리즘". *대한산업공학회, 한국경영과학회, 한국시뮬레이션학회 2025 춘계공동학술대회, 20 June. 2025, Jeju, Korea*.
- Sungwook Jang and Young Jae Jang. "ALNS 알고리즘을 활용한 다중 적재 물류 반송 시스템 운영 최적화". *대한산업공학회, 한국경영과학회, 한국시뮬레이션학회 2025 춘계공동학술대회, 20 June. 2025, Jeju, Korea*.
- Sung Woo Park and Young Jae Jang. "OHT 시스템에서의 우선 처리 로트 신속 운송을 위한 강화학습 기반 Q(λ)-Routing 전략". *대한산업공학회, 한국경영과학회, 한국시뮬레이션학회 2025 춘계공동학술대회, 20 June. 2025, Jeju, Korea*.
- Soyeong Bang and Young Jae Jang. "제조 물류 시스템에서의 AMR의 하이브리드 제어 전략: 휴리스틱 기반 우회 의사결정 최적화". *대한산업공학회, 한국경영과학회, 한국시뮬레이션학회 2025 춘계공동학술대회, 20 June. 2025, Jeju, Korea*.
- Hyunjae Lee and Young Jae Jang. "Development and Case Study of a Single-Crane Task Allocation System for Secondary Battery Formation Process". *한국 CDE학회 2025 동계학술대회, 20 Feb. 2025, Pyeongchang, Korea*.
- Sanguk Im and Young Jae Jang. "Anomaly Detection and Health State Monitoring through Cluster-Based Operational State Identification in OHT Systems". *한국 CDE학회 2025 동계학술대회, 20 Feb. 2025, Pyeongchang, Korea*.
- Sung Woo Park and Young Jae Jang. "A Study on Routing Improvement for Priority Lots in OHT Systems". *한국 CDE학회 2025 동계학술대회, 20 Feb. 2025, Pyeongchang, Korea*.
- Soyeong Bang and Young Jae Jang. "Hybrid Control System for Autonomous Mobile Robots in Manufacturing: Integrating Centralized Control and Decentralized Control". *한국 CDE학회 2025 동계학술대회, 20 Feb. 2025, Pyeongchang, Korea*.

**2024**

- Jang, Young Jae, et al. "Concept of Digital Twins for Autonomous Manufacturing through Virtual Learning and Commissioning". *WSC, 17 Dec. 2024, Orlando, Florida, United States*.
- Ferdinandz Japhne and Young Jae Jang. "Digital Twin Based Dynamic Routing for Overhead Hoist Transport Systems in Semiconductor FAB". *WSC, 17 Dec. 2024, Orlando, Florida, United States*.
- Jang, Sungwook, and Young Jae Jang. "Dynamic Multiple-Load Mobile Transport Operation in Semiconductor Fab". *WSC, 17 Dec. 2024, Orlando, Florida, United States*.
- Lee, Jaeung, and Young Jae Jang. "Idle Vehicle Allocation Problem in Automated Material Handling Systems: A Case Study in Rechargeable Battery Production". *WSC, 16 Dec. 2024, Orlando, Florida, United States*.
- Lennard Heuer and Young Jae Jang. "Integrating Large Language Models into Production Planning: A Framework for Simulation-Based Optimization". *INFORMS, 21 Oct. 2024, Seattle, United States*.
- Lee, Jaeho, and Young Jae Jang. "Short-Term Travel Time Prediction Model for OHT Systems in Semiconductor Fabs". *IEEE CASE, 28 Aug. 2024, Bari, Italy*.
- Lee, Minseok, Hwang, Illhoe, Jang, Sungwook, Im, Nakjoon, and Young Jae Jang. "Markov Decision Process Approach for Battery Charging of an Automated Guided Vehicle". *Ubiquitous Robots, 24 June 2024, New York, United States*.
- Kim, Taehoon, and Young Jae Jang. "Autonomous Manufacturing with a Massive Fleet of Material Handling Robots". *2024 SMMSO Conference, 9 June 2024, Naples, Italy*.
- Kim, Taehoon, and Young Jae Jang. "Case Study on Efficient Material Handling System Through Task Assignment Based on the Health Status of OHT and AMR". *2024 STOCHMOD Conference, 5 June 2024, Milan, Italy*.
- Park, Jinhyeok, Shin, Donghwi, Hong, Sangpyo, Hwang, Illhoe, Hwang, Seol, Jang, Young Jae, Lee, Jaeho, Lee, Jaeung. "Autonomous Robot Orchestration Solution for OHT with Machine Learning and Digital Twin". *2024 35th Annual SEMI Advanced Semiconductor Manufacturing Conference (ASMC), 13 May 2024, Albany, United States*.
- Park, Jinhyeok, et al. "Autonomous Robot Orchestration Solution for OHT with Machine Learning and Digital Twin FA: Factory Automation". *2024 35th Annual SEMI Advanced Semiconductor Manufacturing Conference (ASMC), 13 May 2024, Albany, United States*.
- Farooq, Muhammad Umar, et al. "DAIM-HRI: A New Human-Robot Integration Technology for Industries". *2024 IEEE International Conference on Advanced Robotics and Its Social Impacts (ARSO), 20 Apr. 2024, Hong Kong, China*.
- Chung, Chang Hyun and Young Jae Jang. "Deadlock Prevention and Multi Agent Path Finding Algorithm Considering Physical Constraint for a Massive Fleet AGV System". *Applied Soft Computing, vol. 161, 2024, p. 111725*.
- Kim, Taehoon, and Young Jae Jang. "그래프 네트워크 관점에서의 OHT 선로 레이아웃 설계 최적화 연구". *2024년 대한산업공학회(KIIE) 추계공동학술대회, 24 Oct. 2024, Seoul, Korea*.
- Kim, Taehoon, and Young Jae Jang. "Optimization Study on the Introduction of OHT Systems in the Rechargeable Battery Production Process". *2024년 대한산업공학회(KIIE) 춘계공동학술대회, 2 May 2024, Yeosu, Korea*.
- Im, Nakjoon, and Young Jae Jang. "AGV 충전 환경 및 운영 최적화를 위한 시뮬레이션 모델 제안". *2024년 대한산업공학회(KIIE) 춘계공동학술대회, 2 May 2024, Yeosu, Korea*.
- Lee, Gyuho, and Young Jae Jang. "공장 레이아웃에 따른 AGV와 AMR 시스템 효율성 비교 연구". *2024년 대한산업공학회(KIIE) 춘계공동학술대회, 2 May 2024, Yeosu, Korea*.
- Lee, Jaeung, and Young Jae Jang. "자동화 물류 시스템 차량 간 상호 작용을 고려한 이벤트 기반 모델링 및 이산사건시뮬레이션". *2024년 대한산업공학회(KIIE) 춘계공동학술대회, 2 May 2024, Yeosu, Korea*.
- Kim, Taehoon, and Young Jae Jang. "이차전지 제조 공정에서의 컨베이어와 OHT 시스템 비교". *한국 CDE학회 2024 동계학술대회, 30 Jan. 2024, Pyeongchang, Korea*.
- Im, Nakjoon, and Young Jae Jang. "AGV 충전 운영 연구를 위한 이산 사건 시뮬레이션". *한국 CDE학회 2024 동계학술대회, 30 Jan. 2024, Pyeongchang, Korea*.
- Lee, Gyuho, and Young Jae Jang. "Probabilistic Roadmap 알고리즘을 활용한 AGV와 AMR 시스템의 효율성 비교 연구". *한국 CDE학회 2024 동계학술대회, 30 Jan. 2024, Pyeongchang, Korea*.

**2023**

- Lee, Jaeung, et al. "Sequential Decision-Making Framework for Robotic Mobile Fulfillment System-Based Automated Kitting System". *2023 Winter Simulation Conference (WSC), 11 Dec. 2023*.
- Jang, Young Jae, et al. "자율제조 기반 군집 로봇 제어 및 운영연구". *한국 CDE학회 2023 하계학술대회, 24 Aug. 2023, Pyeongchang, Korea*.
- Hong, Sangpyo, and Young Jae Jang. "시뮬레이션과 디지털트윈 차이 및 자율제조의 역할". *한국 CDE학회 2023 하계학술대회, 24 Aug. 2023, Pyeongchang, Korea*.
- Jang, Young Jae. "제조 물류 로봇에서의 대규모 언어 모델 활용과 로봇 협업 인터페이스 구축을 통한 제조 자동화". *한국 CDE학회 2023 하계학술대회, 24 Aug. 2023, Pyeongchang, Korea*.
- Jang, Young Jae. "중소기업 자율생산을 위한 대규모 언어 모델과 로봇 공학". *한국 CDE학회 2023 하계학술대회, 24 Aug. 2023, Pyeongchang, Korea*.
- Jang, Young Jae. "자율제조 개념과 실증 사례". *한국 CDE학회 2023 하계학술대회, 24 Aug. 2023, Pyeongchang, Korea*.
- Lim, Sejong, and Young Jae Jang. "OHT 이상상태 측정을 위한 레이아웃 내 트랙 선정 및 스케줄링 연구". *2023년 대한산업공학회 춘계공동학술대회, 2 June 2023, Korea*.
- Jang, Sungwook, and Young Jae Jang. "ALNS 알고리즘을 활용한 다중 적재 차량 스케줄링". *2023년 대한산업공학회 춘계공동학술대회, 2 June 2023, Korea*.
- Lee, Jaeho, and Young Jae Jang. "주행 시간 예측 모델을 활용한 OHT 시스템 동적 경로 할당 알고리즘". *2023년 대한산업공학회 춘계공동학술대회, 2 June 2023, Korea*.
- Chung, Changhyun, and Young Jae Jang. "제조 물류 로봇 AGV/AMR의 충돌 방지 예방 경로 설계 자동화". *2023년 대한산업공학회 추계공동학술대회, 3 Nov. 2023, Korea*.
- Jang, Sungwook, and Young Jae Jang. "시뮬레이션을 통한 다수의 작업물의 적재가 가능한 물류 반송 시스템 분석". *2023년 대한산업공학회 추계공동학술대회, 3 Nov. 2023, Korea*.
- Jang, Young Jae, and Taehoon Kim. "이차전지 제조 공정에서의 컨베이어와 OHT 시스템 비교 분석". *2023년 대한산업공학회 추계공동학술대회, 3 Nov. 2023, Korea*.
- Kim, Minsoo, and Young Jae Jang. "공정 내 물류 반송 시스템이 생산 처리량에 미치는 영향 분석: 재공품의 증가에 따라 생산 처리량은 정말 수렴하는가?". *한국 CDE학회 2023 동계학술대회, 9 Feb. 2023, Korea*.
- Lee, Jaeung, and Young Jae Jang. "시뮬레이션 기반 자동화 창고 저장소 할당 연구". *한국 CDE학회 2023 동계학술대회, 9 Feb. 2023, Korea*.
- Shin, Donhwi, and Young Jae Jang. "반도체 FAB 내 물류 자동화 시스템이 생산 능력에 미치는 영향 분석". *한국 CDE학회 2023 동계학술대회, 9 Feb. 2023, Korea*.

**2022**

- Kim, Kang Min, Chang Hyun Chung, and Young Jae Jang. "Deadlock Avoidance Dynamic Routing Algorithm for a Massive Bidirectional Automated Guided Vehicle System". *2022 Winter Simulation Conference (WSC), 11 Dec. 2022*.
- Jang, Young Jae, and Sangpyo Hong. "Industry Case Semiconductor Fab OHT Management System and Digital Twin for OHT Operation". *2022 Winter Simulation Conference (WSC), 11 Dec. 2022*.
- Myung, Jiyoon, et al. "Anomaly Detection for OHT System in Semiconductor Fab". *2022 Winter Simulation Conference (WSC), 11 Dec. 2022*.
- Park, Tae Jong, and Young Jae Jang. "Discrete Lot-Sizing Problem of Single Machine Based on Reinforcement Learning Approach". *2022 International Symposium on Semiconductor Manufacturing Intelligence (ISMI), 11 Nov. 2022*.
- Myung, Jiyoon, and Young Jae Jang. "A Conditional Recurrent Autoencoder for Anomaly Detection in Overhead Hoist Transport Systems According to Their Operational State". *2022 International Symposium on Semiconductor Manufacturing Intelligence (ISMI), 11 Nov. 2022*.
- Lee, Jaeho, and Young Jae Jang. "The Graph Neural Network–Based Dynamic Routing Algorithm for Overhead Hoist Transport Vehicles in Semiconductor Fabrication Plants". *2022 International Symposium on Semiconductor Manufacturing Intelligence (ISMI), 11 Nov. 2022*.
- Jang, Sungwook, and Young Jae Jang. "Storage Assignment Problem for Automated Warehouse in Manufacturing Systems". *2022 International Symposium on Semiconductor Manufacturing Intelligence (ISMI), 11 Nov. 2022*.
- Jang, Young Jae, et al. "Education System for Automated Material Handling System Design with Digital Twin and LEGO Robotics". *2022 International Symposium on Semiconductor Manufacturing Intelligence (ISMI), 11 Nov. 2022*.
- Kim, Min-Soo, et al. "Performance Evaluation of Conveyor-less Matrix Assembly System Using Simulation and Mathematical Models". *2022 ASME International Mechanical Engineering Congress & Exposition (IMECE), 30 Oct. 2022*.
- Kim, Min-Soo, et al. "A Dynamic Programming-Based Heuristic Algorithm for a Flexible Job Shop Scheduling Problem of a Matrix System in Automotive Industry". *2022 IEEE 18th International Conference on Automation Science and Engineering (CASE), 20 Aug. 2022*.
- Lee, Min Seok, and Young Jae Jang. "The AGV Battery Swapping Policy Based on Reinforcement Learning". *2022 IEEE 18th International Conference on Automation Science and Engineering (CASE), 20 Aug. 2022*.
- Hong, Sangpyo, Illhoe Hwang, and Young Jae Jang. "Practical Q-Learning-Based Route-Guidance and Vehicle Assignment for OHT Systems in Semiconductor Fabs". *IEEE Transactions on Semiconductor Manufacturing, vol. 35, no. 3, 2022, pp. 385-396*.

**2021**

- Noh, Yuna, et al. "Modeling Individual Differences in Driver Workload Inference Using Physiological Data". *International Journal of Automotive Technology, vol. 22, 2021, pp. 201-212*.
- 박진혁, 이민석, and 장영재. "자율주행 자동차에서 제어권 전환 시 운전자, 차량, 환경 데이터에 기반한 복합 주행 안정 판단 알고리즘 제안 및 검증". *한국 CDE 학회 논문집 26.1 (2021): 70-80*.

## 특허

- OHT 시스템의 구조, 이동체를 제어하는 전자 장치 및 그 동작 방법 (발명자 장영재, 파루크 무하마드 우마르; 출원번호 10-2025-0029226; 출원일 2025.03.06)

## 산학·연구 과제

랩 과제 목록(2쪽, 16건)의 협력 기관과 연구 기간이다. 종료일이 비어 있는 과제는 랩 표기 그대로다.[^projects]

- AI기반 물류 자동화 시스템 개발 (기간 2018.03–2025.01; 협력 기관 SYNUS Tech)
- ACS 운영 효율화 연구 (기간 2021.04–2022.10; 협력 기관 LG 전자)
- 매트릭스 구조의 자동차 공장을 위한 트림 공정 생산 스케줄링 연구 (기간 2021.07–2022.07; 협력 기관 General Motors)
- 타이어 공장 물류 자동화 시스템 최적화 (기간 2019.01–; 협력 기관 한국타이어)
- 강화 학습 기반의 듀얼 스토커 스케줄링 알고리즘 개발 (기간 2019.01–2019.12; 협력 기관 LG CNS)
- 무선전력 기반의 공장 자동 반송 시스템 설계 및 운영 연구 (기간 2016.11–2019.10; 협력 기관 한국연구재단)
- 배관재 납기 예측 모델 및 최적화 개발에 관한 용역 (기간 2016.07–2017.04; 협력 기관 삼성중공업)
- 정유 플랜트 O&M 지식베이스 프레임워크 통합 시스템 개념 설계 (기간 2017.10–; 협력 기관 한국산업기술평가관리원)
- 알고리즘 기반 생산실적 지표 및 생산향상 계획 산출 방법론 제안 (기간 2016.12–2017.11; 협력 기관 삼성전자)
- 제조 스케줄링 시스템 및 프로세스 연구 (기간 2018.03–2018.11; 협력 기관 코오롱 글로텍)
- 혼합현실 및 빅데이터 기반 STADS 솔루션 플랫폼 개발 과제 (기간 2016.11–2017.07; 협력 기관 정보통신기획평가원)
- 배관 자재 제작 할당 최적화 모델 개발에 관한 용역 (기간 2018.02–2018.07; 협력 기관 삼성중공업)
- 머신러닝 기반의 제어권 전환시 운전자 행태 분석 기술 개발 (기간 2018.01–2018.12; 협력 기관 한국전자통신연구원)
- SCM 네트워크를 고려한 생산 최적화 연구 (기간 2014.06–2015.04; 협력 기관 이랜드)
- 카이스트-코오롱 빅데이터 & 비즈니스 애널리틱스 과제 (기간 2014.11–2017.07; 협력 기관 코오롱)
- 동계스포츠빅데이터 분석을 통한 경기력 향상 모델 개발 및 모니터링 시스템 구축 (기간 2014.07–2019.05; 협력 기관 한국체육대학교 산학협력단)

## 소식

- IEEE CASE 2026
- 2026.06 대한산업공학회 @Gyeongju
- 2026.03.23 AI 운영 무인공장, 카이로스 시연
- 2026.2 졸업식
- 2026.2 한국CDE학회 @Pyeongchang
- 2025.12 피지컬 AI 융합기술 산학 교류회 (with 졸업생)
- 2025.12 WSC @Seattle
- 2025.10 INFORMS @Georgia
- 2025.08 피지컬 AI 핵심기술 시범사업 수주
- 2025.06 대한산업공학회 @Jeju
- 2025.05 ASMC @NewYork

## 교수 수상

- Best Paper Award, International Conference on Intelligent Logistics and Manufacturing Systems (2013)
- Korea Research Foundation Scholar’s Research Grant (2013)
- KAIST Award for Revolutionary Research (2012)
- Maekyung Daily Jung Junki Award (2011)
- Korea Research Foundation Young Scholar’s Research Grant (2011)
- Cost Reduction Best Practice Award – Micron Technology (2009)
- Park Prize for the Best Research at the 4th International Conference on Axiomatic Design (2006)

## 연락과 위치

- 교수 이메일: yjang@kaist.ac.kr[^home][^prof]
- 교수 전화: 042-350-3130[^prof]
- 연구실 전화: 042-350-3170[^home]
- 연구실 대표(Captain): hyunjae.lee@kaist.ac.kr[^home]
- 주소: KAIST, 대전 유성구 대학로 291[^home]

[^home]: DAIM 누리집 첫 화면 <https://daim.kaist.ac.kr/> (2026-10-19 열람)
[^prof]: DAIM 교수 소개 <https://daim.kaist.ac.kr/21> (2026-10-19 열람)
[^team]: DAIM 구성원 페이지 <https://daim.kaist.ac.kr/122325403> (2026-10-19 열람)
[^alumni]: DAIM 졸업생 페이지 <https://daim.kaist.ac.kr/36> (2026-10-19 열람)
[^research]: DAIM 연구 분야(산업 적용) 페이지 <https://daim.kaist.ac.kr/24> (2026-10-19 열람)
[^projects]: DAIM 과제 목록 <https://daim.kaist.ac.kr/22> 1–2쪽 (2026-10-19 열람)
[^papers]: DAIM 학술 성과 목록 <https://daim.kaist.ac.kr/38> (2026-10-19 열람)
[^news]: DAIM 연구실 소식 <https://daim.kaist.ac.kr/29> (2026-10-19 열람)
[^gsds-medal]: KAIST 데이터사이언스대학원 소식 「장영재 교수, 정보통신 유공 홍조근정훈장 수훈」 <https://gsds.kaist.ac.kr/eng/sub05/view/id/443> (2026-10-20 열람)
[^gsds-iaaa]: KAIST 데이터사이언스대학원 소식 「2025 INFORMS Analytics Conference 우수 혁신사례상 수상」 <https://gsds.kaist.ac.kr/news/view/page/1/id/350> (2026-10-20 열람)
[^p1]: J. Lee 외, J. Lee, IEEE Transactions on Semiconductor Manufacturing 38, 404-412 (2025). <https://doi.org/10.1109/tsm.2025.3594651> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p2]: S. Hong, I. Hwang, Y. J. Jang, IEEE Transactions on Semiconductor Manufacturing 35, 385-396 (2022). <https://doi.org/10.1109/tsm.2022.3168702> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Lee, Y. J. Jang, 2024 IEEE 20th International Conference on Automation Science and Engineering (CASE), 1608-1613 (2024). <https://doi.org/10.1109/case59546.2024.10711669> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: C. H. Chung, Y. J. Jang, Applied Soft Computing 161, 111725 (2024). <https://doi.org/10.1016/j.asoc.2024.111725> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p5]: K. M. Kim, C. H. Chung, Y. J. Jang, 2022 Winter Simulation Conference (WSC), 1-12 (2022). <https://doi.org/10.1109/wsc57314.2022.10015233> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: M. U. Farooq, Y. J. Jang, Journal of Manufacturing Systems 85, 513-530 (2026). <https://doi.org/10.1016/j.jmsy.2026.01.005> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p7]: J. Lee 외, E. Sim, 2023 Winter Simulation Conference (WSC), 1972-1983 (2023). <https://doi.org/10.1109/wsc60868.2023.10407259> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: M. U. Farooq, Y. J. Jang, Computer Applications in Engineering Education 34, e70136 (온라인 2026-01-04). <https://doi.org/10.1002/cae.70136> 초록 기준.

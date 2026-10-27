# 배터리 시스템 연구실 (Battery System Laboratory, BSL)

**KAIST 조천식모빌리티대학원·미래자동차학제전공(겸임) · 이윤구 부교수**

- 영문 교수 이름: Yoon Koo Lee[^pi]
- 분야: 배터리 소재·전극·셀에서 모듈·팩과 이동체까지 잇는 모델링, 상태 추정, 제어와 설계 최적화[^home][^research]
- 대분야: 기계·로봇·제조, 에너지·환경·지구
- 태그: 이차전지 소재[^research][^p1], 배터리 관리 시스템[^research], 열전달·열관리[^research], 전기차[^prof], 과학·공학 AI[^research]
- 홈페이지: <https://bsl.kaist.ac.kr/>

> 배터리 안의 반응·변형·발열과 노화를 계산하고, 그 결과를 배터리 관리와 전기차·드론·에너지 저장장치의 안전한 설계로 잇는 연구실이다.[^home][^research]

## 무엇을 연구하나

배터리를 이루는 소재의 성질부터 실제 차량의 운행까지 연결해 연구한다. 전극(전류가 드나들며 화학반응에 참여하는 부분)의 구조와 셀(전지의 기본 단위)의 형태가 배터리 성능에 미치는 영향을 계산하고, 셀을 묶은 모듈과 모듈을 묶은 팩의 설계로 확장한다. 전기화학(화학반응과 전기 현상의 관계), 기계적 변형, 열과 열화(시간이나 사용에 따라 재료나 장치의 성질·성능이 저하되는 현상)를 함께 다루는 것이 중심이다.[^home][^research]

소재·전극 연구에서는 리튬 금속 전지(리튬 금속을 전극으로 쓰는 전지)와 칼륨이온 전지(칼륨 이온이 이동하며 충방전하는 전지)를 다룬다. 리튬이 나뭇가지 모양으로 자라는 수지상 성장, 반응에 다시 참여하지 못하는 비활성 리튬의 축적, 전극 내부의 입자와 빈 공간이 성능·변형에 주는 영향을 모형으로 분석한다. 대표 논문은 흑연에 들어간 칼륨 이온의 농도에 따라 달라지는 소재 성질을 원자 규모에서 계산하고 전극 규모의 모형에 연결했다.[^research][^p1]

배터리 관리 시스템(Battery Management System, BMS: 배터리 상태를 감시하고 충방전을 제어하는 회로와 알고리즘)도 연구한다. 셀 사이 충전 상태를 맞추는 셀 밸런싱, 온도와 건강 상태 추정, 고장 진단을 다룬다. 실측 자료와 물리 모형을 결합하고, 전류·전압과 사용 이력에서 상태를 추정하는 인공지능을 개발한다. 사용 후 다시 쓰는 배터리 모듈에서는 제한된 센서로 각 셀의 온도를 추정하는 방법을 연구한다.[^research]

시스템 연구에서는 교통 상황, 차량의 움직임, 배터리와 냉각 장치를 한 모의실험 환경에 연결한다. 주행 조건에 따른 에너지 소비와 노화를 함께 고려하고, 전기차의 배터리 구성·드론의 배터리 열관리·급속 충전 조건을 최적화한다. 열폭주(배터리 내부 발열이 스스로 가속되는 현상)가 시작되고 다른 셀로 퍼지는 과정도 계산해 안전 설계에 활용하려 한다.[^research]

## 주요 연구 주제

### 전극 미세구조와 전지 성능을 연결하는 모형

전극의 미세구조(내부 입자·빈 공간 등의 구성과 배치)에서 이온이 이동하는 경로와 소재의 성질을 계산해 전지 성능 모형에 반영한다. 리튬이온 전지의 전극 조성·구조를 바꾸는 연구, 리튬 금속 표면에서의 성장과 비활성 리튬층을 분석하는 연구를 함께 진행한다. 칼륨이온 전지 논문에서는 밀도 범함수 이론(Density Functional Theory, DFT: 전자 밀도로 물질의 에너지와 성질을 계산하는 방법)을 전극 입자 연결 모형과 결합해 전기화학적 성능과 기계적 안정성을 살폈다.[^research][^p1]

### 물리와 실측 자료를 함께 쓰는 상태 추정·제어

열화 이력을 반영하는 셀 밸런싱과 건강 상태 추정 모형을 개발한다. 건강 상태(State of Health, SOH: 배터리의 초기 상태를 기준으로 본 성능 상태) 추정에는 온도·충방전 조건·사용 이력을 반영한 자료와 물리적 제약을 활용한다. 또한 실제 주행 중 발생한 전류·전압 변화에서 임피던스(시간에 따라 변하는 전기 입력에 대한 전압과 전류의 관계)를 추정하고, 그 자료를 이용해 배터리의 거동을 표현하는 등가 회로 모형의 값을 찾는다.[^research]

### 열관리와 열폭주 전파

배터리 내부 온도 차이와 발열을 계산하고 셀·모듈의 열관리 설계를 연구한다. 열폭주 연구는 열분석 자료에서 발열 반응 성분을 나누어 보고, 화학반응을 표현하는 신경망(연결된 계산 단위의 관계를 학습하는 모형)을 이용해 반응 속도를 결정하는 값을 구하는 방향이다. 열폭주 시작과 전파를 예측하는 모형을 만들어 배터리 시스템의 안전 설계와 연결하려 한다.[^research]

### 차량·드론과 충전 운전의 통합 설계

전극·셀·모듈·팩·차량 수준의 설계 조건을 연결하고, 차량 운행과 충전 계획까지 함께 고려한다. 실제 차량 주행을 반영한 모의실험, 드론 운용 조건에서의 전기화학·열 연계 모형, 온도와 전극 표면의 리튬 석출을 고려한 급속 충전 조건 설계가 연구 대상이다. 차량 연구는 내연기관 차량을 전기차로 바꾸는 설계와 성능 검증도 포함한다.[^research][^prof]

## 대표 논문

2024년 3월 KAIST 부임 이후 KAIST 소속으로 출판된 논문 가운데 교수의 저자·소속·출판 시기와 초록을 함께 확인한 2편을 골랐다. '쉽게 말하면' 칸은 해당 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문 | 쉽게 말하면 | 교수 역할 |
|---|---|---|---|---|
| 1 | 2025 | [Advanced Multiscale Modeling of Potassium-Ion Batteries for Interplay of Electrochemical and Mechanical Behavior Across Scales](https://doi.org/10.1002/sstr.202400640) · Small Structures | 칼륨이온 전지는 충방전 중 흑연 전극이 팽창하면서 성능과 기계적 안정성이 영향을 받는다. 원자 규모 계산으로 얻은 소재 성질을 전극의 입자 연결 모형에 넣어 전기화학적 거동과 변형을 함께 분석했다. 이온 농도에 따라 성질이 달라지는 점을 반영해야 하며, 성질을 일정하게 놓으면 분석 결과에 차이가 생긴다고 보고했다.[^p1] | 교신저자, KAIST 조천식모빌리티대학원 소속[^p1] |
| 2 | 2025 | [Modeling and Validation of Driving Performance of Electric Vehicle Converted From Internal Combustion Engine Vehicle](https://doi.org/10.1109/TTE.2024.3392208) · IEEE Transactions on Transportation Electrification | 수동 변속기를 갖춘 내연기관 차량을 전기차로 바꾸고 주행 성능을 예측하는 모형을 만들었다. 주행거리·최고속도·가속 시험으로 예측과 실제 결과를 비교했다. 변속 일정을 배터리 구성의 최적화에 반영해 목표 주행거리와 가속 성능을 만족하는 배터리 수와 연결 구성을 찾도록 했다.[^p2] | 교신저자(연구실 * 표시), KAIST 조천식모빌리티대학원 소속[^p2] |

## 교수와 전문 분야

이윤구 교수는 서울대학교에서 2009년 학사, University of Michigan에서 2010년 석사와 2015년 기계공학 박사 학위를 받았다. 박사학위 논문은 리튬이온 전지의 전이금속 용출·침적 영향을 다중 규모로 다뤘다. LG화학 배터리 연구개발에서 2015년 3월부터 2020년 2월까지, 한밭대학교 기계공학과 조교수로 2020년 3월부터 2024년 2월까지 근무했고, 2024년 3월 KAIST 조천식모빌리티대학원 부교수로 부임했다. 연구실 교수 소개는 2025년 9월부터 미래자동차학제전공(Division of Future Vehicle)의 Adjunct Professor(겸임교수)를 함께 적는다.[^pi][^fv]

학과 교수 소개는 전극에서 셀·모듈·팩·시스템까지의 배터리 연구를 실험과 모의실험으로 연결하는 것을 전문 분야로 든다. 전기화학·변형·열·노화 모형과 안전을 고려한 모듈·팩 설계, 내연기관 차량의 전기차 전환을 연구한다.[^prof] 대표 논문은 원자 규모 소재 성질과 전극의 전기화학·기계 거동을 연결하는 모델링,[^p1] 차량 성능의 모형·실험 대조와 배터리 구성 최적화를 보여 준다.[^p2]

## 응용 분야

전기차·드론·에너지 저장장치용 배터리 팩 설계, 온도 관리와 셀 밸런싱, 사용 후 배터리의 상태 평가와 재사용을 다룬다. 연구 소개는 배터리 관리 방법을 모듈·팩·시스템에서 검증하고 전기차·에너지 저장장치·도심항공모빌리티로 적용 범위를 넓힌다고 설명한다.[^research] 과제 목록에는 선박용 에너지 저장장치의 안전 모니터링, 이동형 저장장치 실증, 사용 후 배터리 모듈·팩 제품화, 항만 이동체용 배터리 팩 연구가 올라 있다.[^projects]

## 구성원

2026년 10월 27일 연구자 페이지 기준으로 박사후연구원 2명, 박사과정 2명, 석사과정 5명, 인턴 1명이다. 과정과 연구 주제는 게시 구획·카드를 따랐다. 박사후연구원과 인턴의 시작 날짜는 연구실 소식에 적힌 합류 날짜이고, 학생은 현행 과정의 시작 연월이다.[^members][^news] Cheoljin Shin의 카드 소속은 Department of AI Experience로 적혀 있다. 아래 연구 주제의 영문 약어는 카드 표기다. '대표 논문 참여'는 위 표의 전체 저자 목록에서 이름이 확인되는 경우의 번호다.[^members][^p1]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Dongmin Kim | 박사후연구원 | 2025.03 | Battery Management System; Driving Analysis | kspp8795@kaist.ac.kr |  |
| Jinho Ha | 박사후연구원 | 2026.02.26 | Li-based Modeling; Parameter ID; Optimization | hajho0329@kaist.ac.kr |  |
| Yeonghwan Jang | 박사과정 (Lab Leader) | 2025.03 | Lithium Metal Battery; Battery Design | yeonghwan@kaist.ac.kr |  |
| Dongwook Kim | 박사과정 | 2026.09 | Thermal Runaway; TR Propagation | dongwook.kim@kaist.ac.kr |  |
| Dain Kim | 석사과정 | 2025.09 | Lithium Metal Battery; Drone Optimization | dyne_2@kaist.ac.kr |  |
| Donghae Kim | 석사과정 | 2026.03 | BMS; Cell Balancing; Dynamic EIS | eastsea517@kaist.ac.kr |  |
| Hyoungbin Seo | 석사과정 | 2026.09 | Thermal Management; Thermal Runaway | hyoungbseo@kaist.ac.kr |  |
| Cheoljin Shin | 석사과정 (Department of AI Experience, KAIST) | 2026.09 | State Estimation; Impedance Analysis | cheoljin.shin@kaist.ac.kr |  |
| Retaj Iftikhar | 석사과정 | 2026.09 | AI based optimization; AI based control | retaj_iftikhar@kaist.ac.kr |  |
| Junyeob Lim | 인턴 | 2026.09.07 | Electrochemical Modeling; Parameter ID |  |  |

## 졸업생과 이전 구성원

2026년 10월 27일 Alumni 페이지의 6명이다. 학위·기간은 한밭대학교 학력 표기이며, 이윤구 교수의 KAIST 부임 전 이력이 섞여 있다. 진로의 별도 기준 날짜는 적혀 있지 않다.[^alumni][^pi]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jeu Shin | B.S., Mech. Eng., Hanbat Univ. (2020.03–2024.08) | Ajou University, Dept. of Energy Systems Research |
| Hyunwoo Lim | M.S., Mech. Eng., Hanbat Univ. (2023.03–2025.02) |  |
| Chae-eun Sung | M.S., Mech. Eng., Hanbat Univ. (2023.03–2025.02) |  |
| Seonghyeon Jeon | B.S., Mech. Eng., Hanbat Univ. (2018.03–2024.08) |  |
| Changmin Kim | B.S., Mech. Eng., Hanbat Univ. (2018.03–2024.02) | Samsung SDI |
| Juhyun Park | M.S., Mech. Eng., Hanbat Univ. (2021.03–2023.02) | Institute of Vehicle Engineering |

## 최근 논문 목록 (2021–2026)

연구실 Publication 페이지의 학술지 논문 19편과 학회 발표 61건이다. 전극의 구조·반응·변형에서 배터리 팩·전기차 성능과 제어까지를 다룬다. 이윤구 교수는 2024년 3월 KAIST에 부임했으며 아래에는 이전 소속 시절 항목도 섞여 있다.[^pubs][^pi] 학술지 논문은 2021–2026년 구역을, 날짜가 붙은 학회 발표는 2021년 10월 13일부터 2026년 10월 13일까지를 기준으로 했다. 학회 연도·시기는 누리집 기재값이며, 학술지의 †는 누리집이 1저자, *는 교신저자로 풀이한 표시다. 2026년 전고체 전지 미세구조 논문은 9월 1일 소식의 게재 승인 상태를 함께 적었다.[^pubs][^news]

**2026**

- Chaeeun Sung † , Jihwan Song, Yoon Koo Lee\*. "From microstructure to performance through coupled electrochemical and mechanical insights in all-solid-state batteries (게재 승인: 2026-09-01 연구실 소식)". *Journal of Energy Storage*.
- Dongmin Kim † , Yoon Koo Lee , Kitae Jang\*. "Vehicle-Level Modeling of Internal Resistance Degradation and Influential Parameter Analysis in Lithium-Ion Battery Packs Using Real-World Data". *eTransportation*.
- Yeonghwan Jang , Dain Kim , Donghae Kim , Jinho Ha , Yoonkoo Lee. "AI-Driven Host Structure Design for Lithium Electrode Assemblies". *2026 Spring Meeting of the Korean Ceramic Society, Sep. 30 – Oct. 2, 2026*.
- Donghae Kim , Hyoungbin Seo , Cheoljin Shin , Yoonkoo Lee. "Wavelet-Based Impedance Extraction from Lithium-ion Battery Operating Data for Real-Time BMS Applications". *2026 Annual Conference, The Korean Institute of Power Electronics, Jul. 2026*.
- Yeonghwan Jang , Yoonkoo Lee. "Physics-Informed Multi-Feature SOH Estimation for Lithium-Ion Batteries". *20th U.S. National Congress on Theoretical and Applied Mechanics & Jun. 2026*.
- Dongmin Kim , Yoonkoo Lee. "Physics-informed unsupervised learning for capacity degradation analysis of electric vehicle battery packs, Artificial intelligence and machine learning for energy storage materials, mechanics, and systems". *20th U.S. National Congress on Theoretical and Applied Mechanics & Jun. 2026*.
- Leekyo Jeong, Yoonkoo Lee , Namwoo Kang. "Distributional Reinforcement Learning-Based Inparing for EV Battery Cooling Channel Design Optimization". *ASME 2026 International Design Technical Conferences & Computers and Information in Engineering Conference, Aug. 2026*.
- Jinho Ha , Yoonkoo Lee. "Design of Optimal Fast Charging Protocol Accounting for Temperature and Lithium Plating of Lithium-ion Batteries". *2026 Spring Conference, The Korean Society of Automotive Engineers, May. 2026*.
- Dongmin Kim , Hyeongbin Seo , Yeonghwan Jang , Yoonkoo Lee. "Kalman Filter–Based Algorithm Development for Estimating the State-of-Temperature of NCA Lithium-Ion Battery Cells". *2026 Spring Conference, The Korean Society of Automotive Engineers, May. 2026*.
- Donghae Kim , Yoonkoo Lee. "Comparative Study of Isolated and Non-isolated Converter-based Active Cell Balancing Topologies for Lithium-ion Batteries". *2026 Spring Conference, The Korean Society of Automotive Engineers, May. 2026*.
- Dain Kim , Donghae Kim , Yoonkoo Lee. "Electrochemical Behavior Analysis of 2D Lithium-Metal Batteries under Passive Cell Balancing Circuits". *2026 Spring Conference, The Korean Society of Automotive Engineers, May. 2026*.
- Dongmin Kim , Jinho Ha , Yeonghwan Jang , Dain Kim , Yoonkoo Lee. "Development of a Data-Driven Electrochemical-Thermal Coupling Model for Thermal Response Analysis of an 18650 Cylindrical Lithium-Ion Cell". *2026 Spring Conference, The Korean Society of Mechanical Engineers CAE, May. 2026*.
- Dain Kim , Buyong Shin, Ungki Lee, Yoonkoo Lee. "Development of an Electrochemical–Thermal Coupled Model Reflecting High C-Rate Drone Operating Conditions". *2026 Spring Conference, The Korean Electrochemical Society, Apr. 2026*.
- Jaehee Kim , Yoonkoo Lee. "Multiphysics Driven Design of Core–Shell Silicon Anodes for Lithium-Ion Batteries". *2026 Spring Conference, The Korean Electrochemical Society, Apr. 2026*.
- Yeonghwan Jang , Yoonkoo Lee. "Physics-Informed Neural Networks for Battery SoH Estimation with Degradation-Aware Multi-Feature Inputs". *2026 Spring Conference, The Korean Electrochemical Society, Apr. 2026*.
- Dongwook Kim , Yoonkoo Lee. "Module-Level Thermal Runaway Propagation Analysis Based on ARC test of a Single Cell". *2026 Spring Conference, The Korean Electrochemical Society, Apr. 2026*.
- Dongwook Kim , Yoonkoo Lee. "CRNN-Based Modeling of SOC-Dependent Thermal Runaway Kinetics and Numerical Analysis of Thermal Runaway Propagation". *2026 Spring Conference, The Korean Society for Computational Mechanics, Feb. 2026*.
- Yeonghwan Jang , Yoonkoo Lee. "Phase-Field Analysis of Electrochemically Driven Interfacial Instability in Lithium Deposition". *2026 Spring Conference, The Korean Society for Computational Mechanics, Feb. 2026*.

**2025**

- Subeen Kim † , Yun Kim, Yoon Koo Lee \*, Jihwan Song\*. "Advanced multiscale modeling of potassium-ion batteries for interplay of electrochemical and mechanical behavior across Scales". *Small Structure, 335, 138202*.
- Juhyun Park † , Hyunwoo Lim † , Sangjun Kim, Jihwan Song\*, Yoon Koo Lee \*. "Modeling and validation of driving performance of electric vehicle converted from internal combustion engine vehicle". *IEEE Transactions on Transportation Electrification, 11 (1), 486-498*.
- Dain Kim , Seonghyeon Jeon, Yoonkoo Lee. "Electrochemical and Mechanical Impact of Inactive Lithium Layer Growth on Lithium Metal Battery". *2025 Fall Conference, The Korean Electrochemical Society, Nov. 2025*.
- Dongmin Kim , Kitae Jang, Yoonkoo Lee. "Speed Control for Reducing Motor Current Consumption in BEVs under High-Speed Driving: A MATLAB–VISSIM Co-Simulation Study". *2025 Fall Conference, Korean Society of Automotive Engineers, Nov. 2025*.
- Dongwook Kim , Yoonkoo Lee. "Thermal Runaway Characteristics Analysis of Cylindrical Lithium-ion LCO Batteries in an Oven Test Using 3D Simulation". *2025 Fall Conference, Korean Society of Automotive Engineers, Nov. 2025*.
- Jeu Shin, Dongeon Lee, Ungki Lee, Namwoo Kang, Yoonkoo Lee. "Development of a cell–vehicle–operations multi-scale design optimization framework for SAEV". *2025 Fall Conference, Korean Society of Automotive Engineers, Nov. 2025*.
- Dongwook Kim , Yoonkoo Lee. "Chemical Reaction Neural Network based DSC Analysis for the Thermal Reaction Mechanism of Li-ion Battery NCM333 Cathode". *2025 Chungcheong Branch Fall Conference, Korean Society of Mechanical Engineers, Nov. 2025*.
- Donghae Kim , Yoonkoo Lee. "Comparative Analysis of Passive, Active Cell Balancing for Cylindrical NCM Battery". *2025 Chungcheong Branch Fall Conference, Korean Society of Mechanical Engineers, Nov. 2025*.
- Dongmin Kim , Kitae Jang, Yoonkoo Lee. "Development of a Battery-in-the-Loop-Based Simulator for Testing Electric Autonomous Vehicles". *2025 Spring Conference, Korean Society of Automotive Engineers, May. 2025*.
- Dongmin Kim , Kitae Jang, Yoonkoo Lee. "Development of a Battery-in-the-Loop System for Battery Performance Testing Under Realistic Driving Environments". *2025 Spring Conference, Korean Society of Mechanical Engineers, April. 2025*.
- Dongmin Kim , Kitae Jang, Yoonkoo Lee. "Development of a Battery-in-the-Loop System for Battery Performance Testing Under Realistic Driving Environments". *2025 Spring Academic Conference, CAE and Applied Mechanics Division, KSME, Apr. 2025*.
- Dain Kim , Seonghyeon Jeon, Yoonkoo Lee. "Electrochemical and Mechanical Impact of Dead Lithium Layer Growth on Lithium Metal Battery". *2025 Spring Academic Conference, CAE and Applied Mechanics Division, KSME, Apr. 2025*.
- Subeen Kim, Yoonkoo Lee , Jihwan Song. "Multiscale Design Integrated with DFT for Interrelation Electrochemical-Mechanical Behavior of Potassium-Ion Batteries Across Scales". *2025 Spring Academic Conference, The Korean Electrochemical Society, Apr. 2025*.
- Yeonghwan Jang , Jeu Shin, Yoonkoo Lee. "Phase-Field Modeling of Lithium Dendrite Growth Morphology Depending on Surface Patterning in Li-Metal Batteries". *2025 Spring Academic Conference, The Korean Electrochemical Society, Apr. 2025*.
- Jeu Shin, Yoonkoo Lee. "Development of a Physics-Based Accelerated Degradation Model for Predicting Lithium-Ion Battery Degradation". *2025 Spring Academic Conference, The Korean Electrochemical Society, Apr. 2025*.
- Yoonkoo Lee. "Multi-scale, Multi-physics Battery Research for Safe & High-Performance Battery Systems". *2025 Spring Academic Conference, The Korean Electrochemical Society, Apr. 2025*.

**2024**

- Jeu Shin † , Yoon Koo Lee \*. "Multi-scale mechanical-electrochemical coupled modeling of stress generation and its impact on different battery cell geometries". *Journal of Power Sources, 595, 234064*.
- Yoon Koo Lee † , Chaeeun Sung, Jiyeon Kim, Chaemin Hong, Jinnil Choi\*. "Multiphysics modeling of the influence of initial pressure on mechanical and electrochemical performance of all-solid-state batteries". *Journal of Energy Storage, 82, 110431*.
- Yoon Koo Lee † , Hosop Shin\*. "Modeling and simulation of a composite solid-state battery: The effects of stack pressure on electrochemical and mechanical behavior". *Journal of Energy Storage, 78, 110051*.
- Leekyo Jeong, Yoonkoo Lee , Namwoo Kang. "Reinforcement learning-based optimal design of cooling channels for batteries in electric vehicles". *2024 Fall Academic Conference, KSME, Nov. 2024*.
- Hyunwoo Lim, Yoonkoo Lee , Jihwan Song. "Study on irreversible swelling based on battery cell count through experiments and development of predictive models". *2024 Fall Academic Conference, Reliability Engineering Division, KSME, Nov. 2024*.
- Chaeeun Sung, Jihwan Song, Yoonkoo Lee. "Comprehensive analysis of the effect of all-solid-state battery internal structure on performance". *2024 Fall Academic Conference, CAE & Applied Mechanics Division, KSME, Nov. 2024*.
- Jeu Shin, Yoonkoo Lee. "Development of an Accelerated Simulation Model for Predicting Degradation and Optimizing Performance of Lithium-Ion Batteries". *2024 Fall Academic Conference, CAE & Applied Mechanics Division, KSME, Nov. 2024*.
- Yoonkoo Lee. "Battery Module Design Optimization for Thermal and Mechanical Safety". *International Congress of Theoretical and Applied Mechanics (ICTAM 2024), Aug. 2024*.
- Yoonkoo Lee. "Multi-Scale, Multi-Physics Research for Next-Generation Battery System Design (Invited Presentation)". *2024 Spring Academic Conference, Chungcheong Branch, KSME, Jun. 2024*.
- Subin Kim, Yoonkoo Lee , Jihwan Song. "Design of high-performance potassium-ion batteries via multiscale approach combined with DFT calculations". *2024 Spring Academic Conference, Chungcheong Branch, KSME, Jun. 2024*.
- Hyunwoo Lim, Yoonkoo Lee , Jihwan Song. "Effects of Mechanical Behavior Between Cells on Electrochemical Performance Based on the Number of Battery Cells". *2024 Spring Academic Conference, Chungcheong Branch, KSME, Jun. 2024*.
- Chaeeun Sung, Yoonkoo Lee , Jihwan Song. "Effect of inter-particle contact area within the microstructure of all-solid-state batteries on the electrochemical performance". *2024 Spring Academic Conference, Chungcheong Branch, KSME, Jun. 2024*.
- Jeu Shin, Yoonkoo Lee. "Impact of Battery Internal Structural Geometry on Battery Performance: A Mechanical–Electrochemical Performance Analysis". *2024 Spring Academic Conference, Chungcheong Branch, KSME, Jun. 2024*.
- Yoonkoo Lee. "Multi-scale, multi-physics research for next-generation battery system design (Lecture by Young Researchers)". *2024 Spring Academic Conference, Chungcheong Branch, KSME, Jun. 2024*.
- Subin Kim, Yoonkoo Lee , Jihwan Song. "A comprehensive understanding of electrochemical–mechanical behavior of potassium-ion batteries via multiscale design integrated with DFT calculations". *2024 Spring Academic Conference, CAE & Applied Mechanics Division, KSME, May 2024*.
- Yoonkoo Lee , Chaeeun Sung, Jihwan Song, Jinnil Choi. "Multiphysics modeling of the influence of initial pressure on mechanical and electrochemical performance of all-solid-state batteries". *2024 Spring Academic Conference, CAE & Applied Mechanics Division, KSME, May 2024*.

**2023**

- Ungki Lee † , Namwoo Kang\*, Yoon Koo Lee \*. "Shared autonomous electric vehicle system design and optimization under dynamic battery degradation considering varying load conditions". *Journal of Cleaner Production, 138795*.
- Ungki Lee † , Namwoo Kang\*, Yoon Koo Lee \*. "Optimization of module structure considering mechanical and thermal safety of pouch cell lithium-ion batteries using a reliability-based design optimization approach". *Journal of Energy Storage, 72, 108650*.
- Yoon Koo Lee † \*. "An optimization framework for enhancing cycle life of composite positive electrodes in lithium-ion batteries via composition ratio optimization". *Journal of the Electrochemical Society, 170, 060528*.
- Yoon Koo Lee † \*, Sung Hyun Jeon, Youngmoo Jeon. "Modeling of electrochemical performance and its relation to mechanical responses of li metal batteries". *Journal of the Electrochemical Society, 170, 060520*.
- Yoonkoo Lee , Ungki Lee, Namwoo Kang. "Optimization Study of Mechanical and Thermal Safety in Pouch-Type Lithium-Ion Battery Module Structure Using Reliability-Based Design Optimization (RBDO)". *2023 Fall Academic Conference, Reliability Engineering Division, KSME, Nov. 2023*.
- Hyunwoo Lim, Yoonkoo Lee. "Analysis of electrochemical performance due to mechanical pressure and deformation between battery cells based on the number of cells and stack orientation". *2023 Fall Academic Conference, Reliability Engineering Division, KSME, Nov. 2023*.
- Chaeeun Sung, Yoonkoo Lee. "Microstructure dependent electrochemical performance changes in all-solid-state battery". *2023 Fall Academic Conference, CAE & Applied Mechanics Division, KSME, Nov. 2023*.
- Subin Kim, Yoonkoo Lee , Jihwan Song. "Multiscale design of high-performance potassium ion batteries". *2023 Fall Academic Conference, CAE & Applied Mechanics Division, KSME, Nov. 2023*.
- Yoonkoo Lee. "Multi-scale research for safe and efficient energy system implementation with batteries". *2023 Spring Academic Conference, KSME, May 2023*.
- Hyunwoo Lim, Juhyun Park, Subin Kim, Yoonkoo Lee. "Validation of performance prediction models for electric vehicle conversion vehicles through vehicle performance testing". *2023 Spring Academic Conference, CAE & Applied Mechanics Division, KSME, May 2023*.
- Chaeeun Sung, Yoonkoo Lee. "The influence of the microstructure of solid-state batteries on their electrochemical performance". *2023 Spring Academic Conference, CAE & Applied Mechanics Division, KSME, May 2023*.
- Seonghyeon Jeon, Yoonkoo Lee. "Electrochemical-mechanical modes for predicting swelling in lithium metal batteries". *2023 Spring Academic Conference, CAE & Applied Mechanics Division, KSME, May 2023*.
- Jeu Shin, Yoonkoo Lee. "Study on the impact of the geometric shape of lithium-ion battery on mechanical and electrochemical performance". *2023 Spring Academic Conference, CAE & Applied Mechanics Division, KSME, May 2023*.

**2022**

- Yoon Koo Lee † \*. "Effect of porous structure and morphology of cathode on the degradation of lithium-ion batteries". *Journal of Energy Storage, 52, 104788*.
- Yoon Koo Lee † , Ungki Lee † , Namwoo Kang\*. "Multi-scale design optimization of electric vehicles by analytical target cascading: from battery cell level to marketing level". *Journal of Cleaner Production, 368, 133235*.
- Yoon Koo Lee † , Juhyun Park, Hosop Shin\*. "Multi-scale analysis of cathode microstructural effects on electrochemical and stress responses of lithium-ion batteries". *Journal of Power Sources, 548, 232050*.
- Hosop Shin † , Yoon Koo Lee † , Wei Lu\*. "Structural degradation of graphite anode induced by dissolved manganese ions in Lithium-ion batteries". *Journal of Power Sources, 528, 231223*.
- Yoon Koo Lee † , Hosop Shin\*. "Modeling study of stress generation of a single active material particle connected to solid electrolyte in solid-state batteries". *Electrochimica Acta, 403, 139639*.
- Changmin Kim, Yoonkoo Lee. "Mechanical deformation and electrochemical performance due to volume expansion of lithium-ion battery cells". *2022 Chungcheong Branch Fall Conference, KSME, Oct. 2022*.
- Juhyun Park, Yoonkoo Lee. "Battery optimal design for performance satisfaction of modified electric vehicles". *2022 Autumn Conference, Chungcheong Branch of KSME, Oct. 2022 (Excellent Paper Selection)*.
- Hosop Shin, Yoonkoo Lee. "Analysis of microstructure geometric effects on electrochemical and stress response of lithium-ion batteries using 3D randomized microstructures". *19th U.S. National Congress on Theoretical and Applied Mechanics, Jun. 2022*.
- Yoonkoo Lee , Juhyun Park. "Modeling study of stress generation and its impact on cell performance of multi-layered electrodes in lithium-ion batteries". *19th U.S. National Congress on Theoretical and Applied Mechanics, Jun. 2022*.
- Ungki Lee, Yoonkoo Lee , Namwoo Kang. "Multiscale design optimization of electric vehicles by analytical target cascading: from battery cell level to marketing level". *Asian Society for Structural and Multidisciplinary Optimization, May 2022*.
- Yoonkoo Lee , Ungki Lee, Namwoo Kang. "A study on multi-scale optimization of electric vehicles". *2022 Spring Conference, CAE and Applied Mechanics Division, KSME, May 2022*.
- Juhyun Park, Yoonkoo Lee. "Prediction of cell performance of electric vehicles with manual transmission". *2022 Spring Conference, CAE and Applied Mechanics Division, KSME, May 2022*.

**2021**

- Yoon Koo Lee † \*. "Effect of transition metal ions on solid electrolyte interphase layer on the graphite electrode in lithium ion battery". *Journal of Power Sources, 484, 229270*.
- Yoon Koo Lee † \*, Jihwan Song, Jonghyun Park. "Multi-scale coupled mechanical-electrochemical modeling for study on stress generation and its impact on multi-layered electrodes in lithium-ion batteries". *Electrochimica Acta, 138682*.
- Yun Kim, Jun Keun Chae, Jong-Hwan Lee, Eunpyo Choi, Yoon Koo Lee , Jihwan Song\*. "Free manipulation system for nanorobot cluster based on complicated multi-coil electromagnetic actuator". *Scientific Reports, 11 (1), 1-9*.
- Yoonkoo Lee. "Multi-scale design and application of lithium-ion battery". *2021 Autumn Conference, Korean Society for Manufacturing and Management, Dec. 2021*.
- Yoonkoo Lee. "Multi-scale research on electric vehicle batteries". *2021 Autumn Conference, Korea Productivity Society, Nov. 2021*.

## 연구 과제

2026년 10월 26일 Project 페이지에 올라 있는 14건이다. 기간의 시작일이 2021년 10월 13일부터 2026년 10월 13일까지인 항목이며, 아래 끝 날짜는 게시된 과제 기간이다. 기관 이름은 누리집 기관 칸, 협력 기관은 Counterpart 칸의 표기를 따른다.[^projects]

- 2026 글로컬랩 프로젝트 - Global Institute of Manufacturing Technology (기간 2026.09.01 – 2035.08.31; 사업 2026 글로컬랩 프로젝트; 협력 기관 한밭대학교; 역할 누리집 기관 표기: 공주대학교)
- 선박용 BESS 안전성 향상을 위한 상태 모니터링 기술 조사·분석 (기간 2026.09.23 – 2026.12.15; 사업 선박용 BESS 안전성 향상 선행기술조사; 협력 기관 KRISO; 역할 누리집 기관 표기: 선박해양플랜트연구소(KRISO))
- 리튬이온 배터리의 개별 열화 이력을 고려한 AI 기반 적응형 액티브 밸런싱 (기간 2026.09.01 – 2027.08.31; 사업 이공분야 학술지원 석사과정생연구장려금지원사업; 협력 기관 한국과학기술원; 역할 누리집 기관 표기: 한국과학기술원(KAIST))
- 태양광 연계형 이동형 ESS(ESV) 고도화 및 실증 기술개발 (기간 2026.06.01 – 2027.05.31; 사업 (애로기술) 지역 창업기업 애로기술 해결 기술개발 사업; 협력 기관 한국과학기술원; 역할 누리집 기관 표기: 한국과학기술원(KAIST))
- 선박용 BESS 화재 예방을 위한 조기 감지 및 경보 기술 조사 분석 (기간 2026.05.01 – 2026.10.15; 사업 선박용 BESS 안전성 향상 선행기술조사; 협력 기관 KRISO; 역할 누리집 기관 표기: 선박해양플랜트연구소(KRISO))
- 범용 LEA 핵심 성능 확보 및 설계 가속화를 위한 AI 기반 능동형 설계-해석 융합 플랫폼 개발 (기간 2026.04.01 – 2029.12.31; 사업 2026년도 리튬메탈음극의 범용적 활용을 위한 모듈형 LEA 핵심기술개발 사업; 협력 기관 중앙대학교; 역할 누리집 기관 표기: 중앙대학교)
- 고성능 건식 음극 구현을 위한 고이온/고전자전도 요소 기술 개발 (기간 2026.04.01 – 2029.12.31; 사업 2026년도 배터리 및 전기전자 분야 신규 지원대상 연구개발과제; 협력 기관 한국화학연구원; 역할 누리집 기관 표기: 동화일렉트로라이트)
- AI기반 사용후 배터리 정밀 등급화를 활용한 적용처별 모듈⋅팩 제품화 실증 (기간 2026.04.01 – 2028.12.30; 사업 공공연구성과 실증 시범사업; 협력 기관 숙명여자대학교 · 한국기계연구원; 역할 누리집 기관 표기: 한국과학기술원(KAIST))
- 스마트 항만 내 다양한 전동화 모빌리티의 이차전지 Physical AI 안전 관제 시스템과 이를 적용한 Port AGV용 배터리팩 솔루션 국산화 개발 (기간 2026.04.01 – 2028.03.31; 사업 2026년도 민관공동기술사업화R&D; 협력 기관 여수항만공사; 역할 누리집 기관 표기: 씨티앤에스(CTNS))
- 전력 및 에너지 핵심기술 기반 차세대 리더 양성 (기간 2026.03.01 – 2026.12.31; 사업 전력 및 에너지 핵심기술 기반 차세대 리더 양성; 협력 기관 한국과학기술원; 역할 누리집 기관 표기: 기후에너지환경부)
- 생성형 인공지능 기술을 이용한 사용후 배터리 모듈 진단 시스템 개발 (기간 2025.10.01 – 2026.07.31; 사업 이차전지 전후방 기업 역량강화 지원사업(R&D); 협력 기관 전북테크노파크 · MONA; 역할 누리집 기관 표기: 한국과학기술원(KAIST))
- 제조업 혁신을 위한 Agentic AI 기반 자율 설계 플랫폼 개발 (기간 2025.07.01 – 2027.12.31; 사업 연구개발특구육성(R&D); 협력 기관 나니아랩스; 역할 누리집 기관 표기: 나니아랩스)
- 자가 적응 AI기반 이차전지 모듈팩 전주기 통합 시스템 개발 (기간 2024.12.01 – 2027.11.30; 사업 전략기술 테마별 프로젝트(DCP); 협력 기관 CTNS; 역할 누리집 기관 표기: KAIST 제조AI 빅데이터센터)
- 중소 제조기업 현장 작업자 친화형 제조자산 3차원 획득·변환·관리 기술 개발 [상품명:Factory Studio Suite] (기간 2024.07.01 – 2026.12.30; 사업 스마트 제조혁신 기술개발사업(R&D); 협력 기관 주식회사 디지포레; 역할 누리집 기관 표기: 주식회사 디지포레)

## 특허와 출원

Publication 페이지의 번호가 붙은 특허·출원 136항목 가운데 출원일 또는 등록일이 2021년 10월 13일부터 2026년 10월 13일까지인 국가별 기록이 있는 81항목이다. 아래 국가별 출원·등록 기록은 128행이며 같은 발명의 여러 국가·출원 기록이 섞여 있다. 이윤구 교수의 KAIST 부임 전인 한밭대학교·LG화학 시절 항목과 이후 등록 기록도 포함한다. 제목 앞 대괄호 연도는 누리집 표기이고, 기간 판정은 함께 적힌 날짜를 기준으로 했다.[^pubs][^pi]

- [2026] 주행 데이터 기반의 배터리 임피던스 추정 방법 및 장치 · [KR] 출원 1020260151432 (2026.08.07) (번호 135; 발명자 김동해 | 김동민 | 이윤구)
- [2026] 배터리 임피던스 추정 방법 및 장치 · [KR] 출원 1020260141175 (2026.07.30) (번호 134; 발명자 김동해 | 김동민 | 이윤구)
- [2025] 전기차 실제 환경 주행 성능 시뮬레이팅 시스템 및 그 동작 방법 · [KR] 출원 1020250138080 (2025.09.24) (번호 133; 발명자 김동민 | 이윤구 | 장기태)
- [2025] 냉각부재를 구비한 배터리 모듈 및 배터리 팩 및 전력 저장장치 · [KR] 출원 1020250077612 (2025.06.13) (번호 132; 발명자 유재민 | 문정오 | 신은규 | 이윤구)
- [2025] 부반응의 반응속도 조절을 통해 가속화된 리튬이온 배터리의 열화 예측 방법 및 이를 이용한 예측 시스템 및 컴퓨터 판독 가능 기록매체 · [KR] 출원 1020250076896 (2025.06.12) (번호 131; 발명자 신제우 | 이윤구)
- [2025] Battery Module, Battery Pack Including Same Battery Module, and Automobile Including Same Battery Pack · [US] 출원 19049602 (2025.02.10) (번호 130; 발명자 Sung-Won Seo | Dong-Yeon Kim | Ho-June Chi | Dal-Mo Kang | Jin-Hak Kong | Jeong-O Mun | Yoon-Koo Lee | Yong-Seok Choi | Alexander Eichhorn | Andreas Track)
- [2025] BATTERY MODULE INCLUDING COOLING MEMBER, AND BATTERY PACK AND ENERGY STORAGE SYSTEM INCLUDING THE SAME · [US] 출원 19008066 (2025.01.02) (번호 129; 발명자 Jae-Min YOO | Jeong-O MUN | Eun-Gyu SHIN | Yoon-Koo LEE)
- [2024] BATTERY MODULE, AND BATTERY RACK AND POWER STORAGE DEVICE COMPRISING BATTERY MODULE · [US] 출원 18952062 (2024.11.19) (번호 128; 발명자 Jae-Min YOO | Eun-Gyu SHIN | Sang-Hyun JO | Jeong-O MUN | Yoon-Koo LEE)
- [2024] BATTERY MODULE INCLUDING COOLING MEMBER, AND BATTERY PACK AND ENERGY STORAGE SYSTEM INCLUDING THE SAME · [US] 출원 18920394 (2024.10.18) (번호 127; 발명자 Jae-Min YOO | Jeong-O MUN | Eun-Gyu SHIN | Yoon-Koo LEE)
- [2024] 배터리 모듈, 이러한 배터리 모듈을 포함하는 배터리 랙 및 전력 저장 장치 · [KR] 출원 1020240136006 (2024.10.07) ／ 등록 1028519230000 (2025.08.25) (번호 126; 발명자 유재민 | 신은규 | 조상현 | 문정오 | 이윤구)
- [2024] 폐전지로부터의 금속 회수 방법 및 시스템 · [KR] 출원 1020240069591 (2024.05.28) ／ 등록 1028371110000 (2025.07.17) (번호 125; 발명자 유재민 | 강달모 | 문정오 | 이윤구)
- [2024] Battery module including base plate having gas discharge passage, and battery pack and energy storage system including the same · [US] 출원 18668963 (2024.05.20) ／ 등록 12355090 (2025.07.08) (번호 124; 발명자 Jae-Min Yoo | Jeong-O Mun | Eun-Gyu Shin | Yoon-Koo Lee)
- [2024] Battery module having swelling gauge, and battery pack comprising same · [US] 출원 18657302 (2024.05.07) ／ 등록 12368203 (2025.07.22) (번호 123; 발명자 Sung-Won Seo | Dal-Mo Kang | Jeong-O Mun | Yoon-Koo Lee | Eun-Ah Ju)
- [2024] Battery module including cooling member, and battery pack and energy storage system including the same · [US] 출원 18639727 (2024.04.18) ／ 등록 12155052 (2024.11.26) (번호 122; 발명자 Jae-Min Yoo | Jeong-O Mun | Eun-Gyu Shin | Yoon-Koo Lee)
- [2024] Battery module, battery pack including same battery module, and automobile including same battery pack · [US] 출원 18402240 (2024.01.02) ／ 등록 12261326 (2025.03.25) (번호 121; 발명자 Sung-Won Seo | Dong-Yeon Kim | Ho-June Chi | Dal-Mo Kang | Jin-Hak Kong | Jeong-O Mun | Yoon-Koo Lee | Yong-Seok Choi | Alexander Eichhorn | Andreas Track)
- [2023] Battery module, battery rack comprising same, and power storage device · [US] 출원 18505866 (2023.11.09) ／ 등록 12341218 (2025.06.24) (번호 120; 발명자 Eun-Gyu Shin | Jeong-O Mun | Jae-Min Yoo | Yoon-Koo Lee | Yong-Seok Choi | Jee-Soon Choi)
- [2023] Battery Module Having Improved Cooling Structure · [US] 출원 18372864 (2023.09.26) (번호 119; 발명자 Sung-Won Seo | Dal-Mo Kang | Jeong-O Mun | Yoon-Koo Lee)
- [2023] BATTERY MODULE, AND BATTERY PACK AND VEHICLE COMPRISING THE SAME · [US] 출원 18213832 (2023.06.24) (번호 118; 발명자 Mi-Geum CHOI | Dal-Mo KANG | Jeong-O MUN | Yoon-Koo LEE)
- [2023] BATTERY MODULE HAVING SIMPLE SENSING STRUCTURE · [US] 출원 18115669 (2023.02.28) (번호 117; 발명자 Hee-Jun JIN | Sung-Won SEO | Yoon-Koo LEE | Jeong-O MUN | Eun-Ah JU)
- [2023] Reusable pouch type secondary battery, battery module comprising the same and method of reusing battery module · [US] 출원 18113780 (2023.02.24) ／ 등록 12062751 (2024.08.13) (번호 116; 발명자 Hee-Jun Jin | Sung-Won Seo | Yoon-Koo Lee | Eun-Ah Ju | Jeong-O Mun)
- [2023] 미세구조를 갖는 리튬 이차전지용 양극 활물질 및 활물질의 미세구조를 이용하여 전지의 성능을 예측하는 방법 · [KR] 출원 1020230017430 (2023.02.09) (번호 115; 발명자 이윤구 | 신호섭)
- [2023] Battery module housing having easily reusable recyclable, and reworkable adhesion structure and battery module comprising same · [US] 출원 18166274 (2023.02.08) ／ 등록 12176504 (2024.12.24) (번호 114; 발명자 Eun-Gyu Shin | Dal-Mo Kang | Jeong-O Mun | Yoon-Koo Lee)
- [2022] BATTERY PACK · [US] 출원 18080544 (2022.12.13) (번호 113; 발명자 Sung-Won SEO | Jeong-O MUN | Yoon-Koo LEE | Ho-June CHI)
- [2022] Battery module, battery pack including same battery module, and automobile including same battery pack · [US] 출원 17978676 (2022.11.01) ／ 등록 11923562 (2024.03.05) (번호 112; 발명자 Sung-Won Seo | Dong Yeon Kim | Ho-June Chi | Dal-Mo Kang | Jin-Hak Kong | Jeong-O Mun | Yoon-Koo Lee | Yong-Seok Choi | Alexander Eichhorn | Andreas Track)
- [2022] Reusable pouch type secondary battery, battery module comprising the same and method of reusing battery module · [US] 출원 17741767 (2022.05.11) ／ 등록 11616250 (2023.03.28) (번호 111; 발명자 Hee-Jun Jin | Sung-Won Seo | Yoon-Koo Lee | Eun-Ah Ju | Jeong-O Mun)
- [2021] BATTERY MODULE INCLUDING GAS CUTOFF STRUCTURE · [JP] 출원 34530287 (2021.02.26) ／ 등록 07317233 (2023.07.20) (번호 110; 발명자 Eun Gyu SHIN | Jeong Oh MOON | Yoon Koo LEE | Eun Ah JU)
- [2021] Battery module, and battery pack and vehicle comprising the same · [US] 출원 17173183 (2021.02.10) ／ 등록 11728531 (2023.08.15) (번호 109; 발명자 Mi-Geum Choi | Dal-Mo Kang | Jeong-O Mun | Yoon-Koo Lee)
- [2020] Battery Module, And Battery Pack And Vehicle Comprising Same Battery Module · [US] 출원 17773413 (2020.11.11) ／ 등록 12315956 (2025.05.27) / [JP] 출원 34510196 (2020.11.11) ／ 등록 07372447 (2023.10.23) (번호 108; 발명자 Kyung-Mo Kim | Eun-Gyu Shin | Jae-Min Yoo | Hyeon-Ki Yun | Yoon-Koo Lee | Eun-Ah Ju | Jeong-O Mun)
- [2020] Battery module, and battery rack and power storage device comprising battery module · [US] 출원 17424993 (2020.10.19) ／ 등록 12176569 (2024.12.24) / [JP] 출원 33540565 (2020.10.19) ／ 등록 07252347 (2023.03.27) (번호 107; 발명자 Jae-Min Yoo | Eun-Gyu Shin | Sang-Hyun Jo | Jeong-O Mun | Yoon-Koo Lee)
- [2020] Battery module, and battery rack and power storage device, each comprising same battery module · [US] 출원 17639147 (2020.09.02) ／ 등록 12294070 (2025.05.06) / [JP] 출원 34504270 (2020.09.02) ／ 등록 07379657 (2023.11.06) (번호 106; 발명자 Eun-Gyu Shin | Jeong-O Mun | Jae-Min Yoo | Yoon-Koo Lee)
- [2020] BATTERY MODULE, BATTERY PACK, AND VEHICLE · [JP] 출원 34509691 (2020.08.20) ／ 등록 07366236 (2023.10.12) (번호 105; 발명자 Eun-Gyu SHIN | Seung-Hyun KIM | Jae-Min YOO | Young-Seok LEE | Jeong-O MUN | Yoon-Koo LEE)
- [2020] BATTERY MODULE · [EP] 출원 20902383.7 (2020.08.19) ／ 등록 04033593 (2024.10.02) / [JP] 출원 34514233 (2020.08.19) ／ 등록 07416917 (2024.01.09) (번호 104; 발명자 Eun Gyu SHIN | Jae Min YOO | Jeong Oh MOON | Yoon Koo LEE)
- [2020] Battery Pack and Vehicle Comprising Battery Pack · [EP] 출원 20850728.5 (2020.08.03) ／ 등록 03989337 (2024.10.02) / [JP] 출원 34502154 (2020.08.03) ／ 등록 07334326 (2023.08.18) (번호 103; 발명자 Eun-Ah Ju | Sung-Won Seo | Jae-Min Yoo | Jeong-O Mun | Yoon-Koo Lee)
- [2020] Battery module system comprising external short-circuit device and cooling device · [US] 출원 17625469 (2020.07.06) ／ 등록 12040510 (2024.07.16) / [JP] 출원 33570507 (2020.07.06) ／ 등록 07412452 (2023.12.28) (번호 102; 발명자 Jae-Min Yoo | Jeong-O Mun | Eun-Gyu Shin | Yoon-Koo Lee | Yong-Seok Choi | Jee-Soon Choi)
- [2020] Battery module, battery rack comprising same, and power storage device · [US] 출원 17431388 (2020.06.23) ／ 등록 11870094 (2024.01.09) / [EP] 출원 20834689.0 (2020.06.23) ／ 등록 03965220 (2024.04.24) / [JP] 출원 33557060 (2020.06.23) ／ 등록 07268188 (2023.04.24) (번호 101; 발명자 Eun-Gyu Shin | Jeong-O Mun | Jae-Min Yoo | Yoon-Koo Lee | Yong-Seok Choi | Jee-Soon Choi)
- [2020] Battery pack with energy drain resistor for preventing fire propagation · [US] 출원 17298261 (2020.06.04) ／ 등록 11764447 (2023.09.19) / [EP] 출원 20851714.4 (2020.06.04) ／ 등록 03958341 (2025.04.23) / [JP] 출원 33529022 (2020.06.04) ／ 등록 07186876 (2022.12.01) (번호 100; 발명자 Eun-Gyu Shin | Jeong-O Mun | Jae-Min Yoo | Yoon-Koo Lee)
- [2020] Battery module including base plate having gas discharge passage, and battery pack and energy storage system including the same · [US] 출원 17294562 (2020.05.27) ／ 등록 12015165 (2024.06.18) / [EP] 출원 20827285.6 (2020.05.27) ／ 등록 03905426 (2024.03.13) / [JP] 출원 33530228 (2020.05.27) ／ 등록 07170872 (2022.11.04) (번호 99; 발명자 Jae-Min Yoo | Jeong-O Mun | Eun-Gyu Shin | Yoon-Koo Lee)
- [2020] BATTERY RACK AND POWER STORAGE DEVICE COMPRISING SAME · [US] 출원 17298375 (2020.05.12) ／ 등록 12002938 (2024.06.04) / [EP] 출원 20818712.0 (2020.05.12) ／ 등록 03905375 (2025.09.10) / [JP] 출원 33545772 (2020.05.12) ／ 등록 07308961 (2023.07.06) (번호 98; 발명자 Jae-Min Yoo | Jeong-O Mun | Eun-Gyu Shin | Yoon-Koo Lee)
- [2020] 가스 차단 구조체를 포함하는 전지모듈 · [KR] 출원 1020200039868 (2020.04.01) ／ 등록 1028145660000 (2025.05.26) (번호 97; 발명자 신은규 | 문정오 | 이윤구 | 주은아)
- [2020] Battery cell, and battery module, battery rack and energy storage system including the same · [US] 출원 16979600 (2020.01.20) ／ 등록 11962020 (2024.04.16) / [JP] 출원 32548960 (2020.01.20) ／ 등록 07090725 (2022.06.16) (번호 96; 발명자 Eun-Gyu Shin | Jae-Min Yoo | Yoon-Koo Lee | Dal-Mo Kang | Jeong-O Mun)
- [2019] Battery module having swelling gauge, and battery pack comprising same · [US] 출원 17281140 (2019.12.20) ／ 등록 12027715 (2024.07.02) / [EP] 출원 19908315.5 (2019.12.20) ／ 등록 03893319 (2024.10.02) / [JP] 출원 33514082 (2019.12.20) ／ 등록 07046268 (2022.03.24) (번호 94; 발명자 Sung-Won Seo | Dal-Mo Kang | Jeong-O Mun | Yoon-Koo Lee | Eun-Ah Ju)
- [2019] 배터리 모듈, 이러한 배터리 모듈을 포함하는 배터리 팩 및 자동차 · [KR] 출원 1020190161962 (2019.12.06) ／ 등록 1027865230000 (2025.03.20) (번호 92; 발명자 김경모 | 신은규 | 유재민 | 윤현기 | 이윤구 | 주은아 | 문정오)
- [2019] Battery pack and vehicle comprising same battery pack · [US] 출원 17260751 (2019.11.07) ／ 등록 12183936 (2024.12.31) / [EP] 출원 19899079.8 (2019.11.07) ／ 등록 03848995 (2024.09.18) (번호 90; 발명자 Eun-Ah Ju | Dal-Mo Kang | Jeong-O Mun | Sung-Won Seo | Yoon-Koo Lee)
- [2019] 배터리 모듈, 이러한 배터리 모듈을 포함하는 배터리 랙 및 전력 저장 장치 · [KR] 출원 1020190136956 (2019.10.30) ／ 등록 1027735890000 (2025.02.21) (번호 89; 발명자 신은규 | 문정오 | 유재민 | 이윤구)
- [2019] 배터리 모듈 및 이러한 배터리 모듈을 포함하는 배터리 랙 및 전력 저장 장치 · [KR] 출원 1020190117415 (2019.09.24) ／ 등록 1027990120000 (2025.04.17) (번호 88; 발명자 신은규 | 문정오 | 유재민 | 이윤구)
- [2019] Battery module including heat-shrinkable tube · [US] 출원 16769479 (2019.08.26) ／ 등록 11594780 (2023.02.28) / [JP] 출원 32536141 (2019.08.26) ／ 등록 07062196 (2022.04.22) (번호 87; 발명자 Jae-Min Yoo | Eun-Gyu Shin | Jeong-O Mun | Yoon-Koo Lee)
- [2019] 연쇄발화 방지를 위한 에너지 드레인 저항체를 구비한 배터리 팩 · [KR] 출원 1020190097677 (2019.08.09) ／ 등록 1027664960000 (2025.02.06) (번호 86; 발명자 신은규 | 문정오 | 유재민 | 이윤구)
- [2019] 배터리 팩 및 이러한 배터리 팩을 포함하는 자동차 · [KR] 출원 1020190094572 (2019.08.02) ／ 등록 1028199180000 (2025.06.09) (번호 85; 발명자 주은아 | 서성원 | 유재민 | 문정오 | 이윤구)
- [2019] 외부 단락 장치 및 냉각 장치를 구비하는 배터리 모듈 시스템 · [KR] 출원 1020190082289 (2019.07.08) ／ 등록 1028259060000 (2025.06.23) (번호 84; 발명자 유재민 | 문정오 | 신은규 | 이윤구 | 최용석 | 최지순)
- [2019] Battery module, battery pack comprising same battery module, and vehicle comprising same battery pack · [KR] 출원 1020190080195 (2019.07.03) ／ 등록 1027489830000 (2024.12.26) / [US] 출원 16759067 (2019.07.03) ／ 등록 11456502 (2022.09.27) / [EP] 출원 19830344.8 (2019.07.03) ／ 등록 03731302 (2023.12.13) / [JP] 출원 32524307 (2019.07.03) ／ 등록 07083897 (2022.06.03) (번호 83; 발명자 Eun-Gyu Shin | Jeong-O Mun | Yoon-Koo Lee)
- [2019] 가스배출통로를 구비한 베이스 플레이트를 포함한 배터리 모듈 및 배터리 팩 및 전력 저장장치 · [KR] 출원 1020190071733 (2019.06.17) ／ 등록 1027511110000 (2025.01.02) (번호 82; 발명자 유재민 | 문정오 | 신은규 | 이윤구)
- [2019] 배터리 랙 및 이를 포함하는 전력 저장 장치 · [KR] 출원 1020190066645 (2019.06.05) ／ 등록 1027439010000 (2024.12.12) (번호 81; 발명자 유재민 | 문정오 | 신은규 | 이윤구)
- [2019] Battery module having improved cooling structure · [US] 출원 16767457 (2019.03.08) ／ 등록 11811040 (2023.11.07) / [EP] 출원 19814466.9 (2019.03.08) ／ 등록 03716392 (2025.07.23) / [JP] 출원 32528094 (2019.03.08) ／ 등록 07082665 (2022.05.31) (번호 80; 발명자 Sung-Won Seo | Dal-Mo Kang | Jeong-O Mun | Yoon-Koo Lee)
- [2019] Battery module, battery pack including battery module, and vehicle including battery pack · [KR] 출원 1020190018662 (2019.02.18) ／ 등록 1024554710000 (2022.10.12) / [EP] 출원 19772159.0 (2019.02.18) ／ 등록 03675274 (2023.04.05) / [JP] 출원 32518385 (2019.02.18) ／ 등록 07045571 (2022.03.24) (번호 79; 발명자 Sung-Won Seo | Dal-Mo Kang | Jeong-O Mun | Yoon-Koo Lee | Alexander Eichhorn | Andreas Track)
- [2019] Battery module, battery pack including same battery module, and automobile including same battery pack · [US] 출원 16629793 (2019.02.13) ／ 등록 11522246 (2022.12.06) / [EP] 출원 24184816.7 (2019.02.13) ／ 등록 04447193 (2025.04.02) / [JP] 출원 31571294 (2019.02.13) ／ 등록 07045592 (2022.03.24) (번호 78; 발명자 Sung-Won Seo | Dong-Yeon Kim | Ho-June Chi | Dal-Mo Kang | Jin-Hak Kong | Jeong-O Mun | Yoon-Koo Lee | Yong-Seok Choi | Alexander Eichhorn | Andreas Track)
- [2018] 배터리 팩 및 이러한 배터리 팩을 포함하는 자동차 · [KR] 출원 1020180164610 (2018.12.18) ／ 등록 1025447850000 (2023.06.13) (번호 76; 발명자 주은아 | 강달모 | 문정오 | 서성원 | 이윤구)
- [2018] Battery module housing having easily reusable, recyclable, and reworkable adhesion structure and battery module comprising same · [US] 출원 16625453 (2018.12.14) ／ 등록 11611125 (2023.03.21) / [EP] 출원 18901341.0 (2018.12.14) ／ 등록 03644398 (2025.06.18) / [JP] 출원 31566688 (2018.12.14) ／ 등록 07038944 (2022.03.11) (번호 75; 발명자 Eun-Gyu Shin | Dal-Mo Kang | Jeong-O Mun | Yoon-Koo Lee)
- [2018] Battery module having improved cooling structure · [US] 출원 16618534 (2018.12.05) ／ 등록 11264668 (2022.03.01) / [EP] 출원 18897735.9 (2018.12.05) ／ 등록 03671946 (2023.04.26) / [JP] 출원 31568612 (2018.12.05) ／ 등록 07045605 (2022.03.24) (번호 74; 발명자 Sung-Won Seo | Dal-Mo Kang | Jeong-O Mun | Yoon-Koo Lee)
- [2018] Battery pack and method of manufacturing the same · [US] 출원 16618993 (2018.11.30) ／ 등록 11302982 (2022.04.12) / [EP] 출원 18895603.1 (2018.11.30) ／ 등록 03627584 (2023.11.22) (번호 73; 발명자 Eunah Ju | Sung Won Seo | Heejun Jin | Yoonkoo Lee | Jeong Oh Moon | Andreas Track | Alexander Eichhorn | Valentin Brokop)
- [2018] Battery module, and battery pack and vehicle comprising same · [US] 출원 16625414 (2018.11.28) ／ 등록 11196120 (2021.12.07) / [JP] 출원 31566694 (2018.11.28) ／ 등록 07045566 (2022.03.24) (번호 72; 발명자 Eun-Ah Ju | Sung-Won Seo | Yoon-Koo Lee | Hee-Jun Jin | Jeong-O Mun | Alexander Eichhorn | Andreas Track | Valentin Brokop)
- [2018] Battery module including sensing assembly and bus bar assembly · [US] 출원 16621322 (2018.11.06) ／ 등록 11830974 (2023.11.28) / [EP] 출원 18879472.1 (2018.11.06) ／ 등록 03671937 (2024.06.12) / [JP] 출원 31569669 (2018.11.06) ／ 등록 07045568 (2022.03.24) (번호 71; 발명자 Hee-Jun Jin | Sung-Won Seo | Yoon-Koo Lee | Eun-Ah Ju | Ho-June Chi | Jeong-O Mun)
- [2018] Battery module comprising bus bar assembly · [US] 출원 16620266 (2018.10.31) ／ 등록 11223092 (2022.01.11) / [EP] 출원 18873468.5 (2018.10.31) ／ 등록 03671901 (2025.08.13) / [JP] 출원 31569667 (2018.10.31) ／ 등록 07047218 (2022.03.28) (번호 70; 발명자 Hee-Jun Jin | Sung-Won Seo | Yoon-Koo Lee | Eun-Ah Ju | Jeong-O Mun)
- [2018] 폐전지로부터의 금속 회수 방법 및 시스템 · [KR] 출원 1020180124716 (2018.10.18) ／ 등록 1026714850000 (2024.05.28) (번호 69; 발명자 유재민 | 강달모 | 문정오 | 이윤구)
- [2018] Battery module having bus bar assembly · [US] 출원 16620385 (2018.10.11) ／ 등록 11289776 (2022.03.29) / [EP] 출원 18884722.2 (2018.10.11) ／ 등록 03671902 (2025.05.21) / [JP] 출원 31564425 (2018.10.11) ／ 등록 07045590 (2022.03.24) (번호 68; 발명자 Hee-Jun Jin | Sung-Won Seo | Yoon-Koo Lee | Eun-Ah Ju | Jeong-O Mun)
- [2018] 열수축성 튜브를 포함하는 배터리 모듈 · [KR] 출원 1020180109834 (2018.09.13) ／ 등록 1024244000000 (2022.07.19) (번호 67; 발명자 유재민 | 신은규 | 문정오 | 이윤구)
- [2018] Battery module, battery pack and vehicle including the same · [US] 출원 16339583 (2018.07.12) ／ 등록 11349172 (2022.05.31) / [EP] 출원 18835416.1 (2018.07.12) ／ 등록 03522255 (2023.08.30) / [JP] 출원 31528766 (2018.07.12) ／ 등록 07034415 (2022.03.04) (번호 66; 발명자 Hee-Jun Jin | Sung-Won Seo | Yoon-Koo Lee | Eun-Ah Ju | Jeong-O Mun)
- [2018] 개선된 냉각 구조를 갖는 배터리 모듈 · [KR] 출원 1020180066302 (2018.06.08) ／ 등록 1023723480000 (2022.03.03) (번호 64; 발명자 서성원 | 강달모 | 문정오 | 이윤구)
- [2018] Battery module · [US] 출원 16341236 (2018.05.28) ／ 등록 11437660 (2022.09.06) / [EP] 출원 18817606.9 (2018.05.28) ／ 등록 03550661 (2025.07.02) / [JP] 출원 31538381 (2018.05.28) ／ 등록 07034417 (2022.03.04) (번호 63; 발명자 Eun-Ah Ju | Sung-Won Seo | Yoon-Koo Lee | Hee-Jun Jin | Jeong-O Mun)
- [2018] Battery module, battery pack including battery module, and vehicle including battery pack · [US] 출원 16461167 (2018.04.13) ／ 등록 11456500 (2022.09.27) / [JP] 출원 31531137 (2018.04.13) ／ 등록 07062164 (2022.04.22) (번호 61; 발명자 Ho-June Chi | Jeong-O Mun | Jin-Yong Park | Sung-Won Seo | Yoon-Koo Lee)
- [2018] Drawer-type battery pack · [EP] 출원 18784544.1 (2018.04.02) ／ 등록 03565023 (2022.07.20) (번호 59; 발명자 Sung-Won Seo | Dal-Mo Kang | Jeong-O Mun | Yoon-Koo Lee | Ho-June Chi)
- [2018] Battery pack having crash beam and drain structure · [US] 출원 16349530 (2018.03.26) ／ 등록 11450913 (2022.09.20) (번호 58; 발명자 Sung-Won Seo | Jeong-O Mun | Yoon-Koo Lee | Ho-June Chi | Dal-Mo Kang)
- [2018] BATTERY MODULE HAVING SIMPLE SENSING STRUCTURE · [EP] 출원 18772425.7 (2018.02.21) ／ 등록 03483980 (2025.06.04) (번호 55; 발명자 Hee-Jun JIN | Sung-Won SEO | Yoon-Koo LEE | Jeong-O MUN | Eun-Ah JU)
- [2018] Battery module · [US] 출원 16469368 (2018.02.12) ／ 등록 11777157 (2023.10.03) / [EP] 출원 18824223.4 (2018.02.12) ／ 등록 03567670 (2025.08.20) (번호 53; 발명자 Eun-Ah Ju | Hang-June Choi | Sung-Won Seo | Dal-Mo Kang | Jeong-O Mun | Yoon-Koo Lee)
- [2018] Apparatus for predicting deformation of battery module · [US] 출원 16314707 (2018.01.23) ／ 등록 11561152 (2023.01.24) / [EP] 출원 18743976.5 (2018.01.23) ／ 등록 03483978 (2023.03.29) (번호 51; 발명자 Dong-Yeon Kim | Jin-Hak Kong | Yong-Seok Choi | Sung-Won Seo | Yoon-Koo Lee | Dal-Mo Kang | Jeong-O Mun)
- [2018] Battery pack including heat conduction medium with louver fin shape · [JP] 출원 31528758 (2018.01.17) ／ 등록 07037005 (2022.03.08) (번호 50; 발명자 Ho-June Chi | Dal-Mo Kang | Jeong-O Mun | Sung-Won Seo | Yoon-Koo Lee)
- [2018] Battery pack · [US] 출원 16310539 (2018.01.04) ／ 등록 11605857 (2023.03.14) (번호 48; 발명자 Sung-Won Seo | Jeong-O Mun | Yoon-Koo Lee | Ho-June Chi)
- [2017] 배터리 모듈, 이를 포함하는 배터리 팩 및 자동차 · [KR] 출원 1020170176339 (2017.12.20) ／ 등록 1023195370000 (2021.10.25) (번호 45; 발명자 주은아 | 서성원 | 이윤구 | 진희준 | 문정오 | 아히혼 | 알렉산더 | 트락 | 안드레아스 | 브로콥 | 발렌틴)
- [2017] Battery module having cooling channel, and assembling method and frame assembly thereof · [JP] 출원 30538608 (2017.09.27) ／ 등록 07034411 (2022.03.04) (번호 41; 발명자 Ji-Su Yoon | Yoon-Koo Lee | Dal-Mo Kang | Sang-Woo Ryu | Jeong-O Mun | Sung-Won Seo)
- [2017] Battery module, and battery pack and vehicle comprising the same · [US] 출원 15738376 (2017.04.05) ／ 등록 11380955 (2022.07.05) (번호 30; 발명자 Mi-Geum Choi | Jeong-O Mun | Dal-Mo Kang | Yoon-Koo Lee | Jung-Been You | Dong-Yeon Kim | Jin-Hak Kong | Yong-Seok Choi)
- [2017] Battery pack and vehicle comprising battery pack · [EP] 출원 17789745.1 (2017.01.16) ／ 등록 03361555 (2022.06.01) (번호 24; 발명자 Yoon-Koo Lee | Jeong-O Mun | Mi-Geum Choi)
- [2016] 방열부재를 구비한 전지모듈 · [KR] 출원 1020160070301 (2016.06.07) ／ 등록 1023202630000 (2021.10.26) (번호 11; 발명자 유재욱 | 문정오 | 이윤구 | 정병천 | 최종운)

## 수상

연구실 소식의 수상 글 4건과 학회 발표 목록의 Excellent Paper Selection 1건이다. 학회 발표 목록의 2022년 항목은 KAIST 부임 전 기록이며, 수상 명칭과 등급은 게시 표기를 따른다.[^news][^pubs][^pi]

- 2026-09-01 · Cheoljin Shin과 Donghae Kim이 KSME-SEMES Open Innovation Challenge에서 Encouragement Award(장려상)를 받았다. 연구 주제는 건식 식각의 포커스 링 마모로 인한 플라스마 불균일을 유전율과 열전도도 분포의 공동 설계로 보정하는 전략이다.
- 2026-05-18 · Yeonghwan Jang이 한국전기화학회 춘계학술대회에서 물리 정보를 활용한 배터리 건강 상태 추정 연구로 수상했다.
- 2025-11-10 · Dongwook Kim이 대한기계학회 충청지회 추계학술대회에서 Top prize, Donghae Kim이 Excellence Prize를 받았다.
- 2025-10-31 · Yeonghwan Jang·Dain Kim·Dongwook Kim·Donghae Kim이 미래내일 청년 일경험 지원사업에서 excellence award를 받았다.
- 2022.10 · Juhyun Park·Yoonkoo Lee의 전기차 개조 차량 배터리 최적 설계 발표가 대한기계학회 충청지회 추계학술대회에서 Excellent Paper Selection으로 기재됐다.

## 소식

2024년 7월 1일부터 2026년 9월 20일까지 연구실이 게시한 연구 발표·세미나·논문 게재 승인·특허 출원·과제 선정 등의 소식 19건이다. 아래 날짜는 소식 게시 날짜이며, 논문 출판일이나 특허 출원일과 같다는 뜻은 아니다.[^news]

- 2026-09-20 · 이윤구 교수가 HKUST의 International Electrochemistry Summit 2026에서 배터리 모델링·설계·제어를 연결하는 다중 규모·다중 물리 연구 틀을 초청 강연했다.
- 2026-09-01 · 전고체 전지 미세구조의 전기화학·기계 거동 연구가 Journal of Energy Storage에 게재 승인됐다.
- 2026-08-31 · Donghae Kim의 리튬이온 배터리 개별 열화 이력을 고려한 AI 기반 적응형 액티브 밸런싱 과제가 선정됐다. 게시 기간은 2026.09.01–2027.08.31이다.
- 2026-08-13 · Donghae Kim이 차량 주행 데이터 기반 배터리 임피던스 추정 방법 및 장치의 국내 특허 출원을 알렸다.
- 2026-08-05 · Dongmin Kim의 실제 운행 자료 기반 배터리 팩 내부 저항 열화 모델링 논문이 eTransportation에 게재 승인됐다.
- 2026-07-30 · Donghae Kim이 배터리 임피던스 추정 방법 및 장치의 국내 특허 출원을 알렸다.
- 2026-07-30 · Yeonghwan Jang이 LG에너지솔루션 산학협력컨퍼런스에서 노화와 열을 연결한 모형을 이용한 리튬이온 배터리 열폭주 연구를 발표했다.
- 2026-04-28 · MathWorks의 Sean Oh와 MATLAB·Simulink를 이용한 배터리 및 시스템 모델링 세미나를 열었다.
- 2026-03-05 · MathWorks의 Sean Oh와 배터리 열폭주 조기 경보 방법에 관한 연구실 세미나를 열었다.
- 2025-12-16 · Purdue University의 Hosop Shin 교수와 재제조 배터리 기술에 관한 연구실 세미나를 열었다.
- 2025-12-08 · Dongmin Kim이 이윤구·장기태 교수와 함께 전기차 실제 환경 주행 성능 시뮬레이팅 시스템 및 그 동작 방법의 특허 출원을 알렸다.
- 2025-12-05 · Yeonghwan Jang·Dongwook Kim·Dain Kim·Donghae Kim이 COMSOL Conference에 참가했다.
- 2025-11-04 · 칼륨이온 배터리 연구가 KAIST 공학자의 오리연못 2025년 2호 학과 연구 하이라이트에 소개됐다.
- 2025-10-31 · Yeonghwan Jang·Dain Kim·Dongwook Kim이 HRD 최종 연구 보고회에서 연구를 발표했다.
- 2025-08-29 · 조천식모빌리티대학원 공동 워크숍에서 연구 주제를 공유하고 모빌리티 관련 연구실과 공동 연구 가능성을 논의했다.
- 2025-08-21 · Dongmin Kim·Yeonghwan Jang·Dain Kim·Dongwook Kim·Donghae Kim이 HRD 프로그램을 통해 배터리 셀 사이 편차 추정 연구를 진행한다고 알렸다.
- 2025-05-27 · Missouri S&T의 Jonghyun Park 교수와 경북대학교의 Jimin Oh 교수를 초청해 이차전지 세미나를 열었다.
- 2024-09-01 · 연구 성과가 KAIST Breakthroughs 2024년 가을호에 소개됐다.
- 2024-07-01 · 연구실 교수와 학과 교수의 미래 모빌리티 대담이 KAISTian Newsletter 2024년 봄·여름호에 소개됐다.

## 연락과 위치

- 교수 연구실: KAIST 문지캠퍼스 Faculty Wing F434[^pi][^prof]
- 누리집 공통 연구실 위치: 대전광역시 유성구 문지로 193, KAIST 문지캠퍼스 Faculty Wing F440[^pi]
- 전화: +82-42-350-1762[^pi]
- 교수 이메일: yoonklee@kaist.ac.kr[^pi]
- [근거와 확인 범위](bsl-sources.md)
[^home]: 연구실 첫 화면 <https://bsl.kaist.ac.kr/> (2026-10-26 열람).
[^pi]: 연구실 교수 소개 <https://bsl.kaist.ac.kr/member> (2026-10-26 열람).
[^fv]: KAIST 미래자동차학제전공 교수진의 이윤구 교수 항목 <https://fv.kaist.ac.kr/index.php?mid=fv01_03> (2026-10-27 열람). 소속학과는 조천식모빌리티대학원으로 기재돼 있다.
[^research]: 연구실 Research <https://bsl.kaist.ac.kr/research> (2026-10-26 열람). Simulation & Prediction, AI & Control, Optimization & Demonstration의 개별 연구 설명.
[^prof]: KAIST 조천식모빌리티대학원 이윤구 교수 소개 <https://mo.kaist.ac.kr/professor/%EC%9D%B4%EC%9C%A4%EA%B5%AC/> (2026-10-27 열람).
[^members]: 연구실 Researchers <https://bsl.kaist.ac.kr/researchers> (2026-10-27 열람).
[^alumni]: 연구실 Alumni <https://bsl.kaist.ac.kr/alumni> (2026-10-27 열람).
[^pubs]: 연구실 Publication의 Journal, Patent, Conference 목록 <https://bsl.kaist.ac.kr/publication> (2026-10-26 열람).
[^projects]: 연구실 Project <https://bsl.kaist.ac.kr/project> (2026-10-26 열람).
[^news]: 연구실 Board의 Recent News <https://bsl.kaist.ac.kr/news> (2026-10-26 열람).
[^p1]: S. Kim, Y. Kim, Y. K. Lee, J. Song, Small Structures 6, 2400640 (온라인 2025-04-06). <https://doi.org/10.1002/sstr.202400640> 초록 기준(출판사 논문 페이지). 초록 원문 <https://onlinelibrary.wiley.com/doi/10.1002/sstr.202400640>.
[^p2]: J. Park 외, Y. K. Lee, IEEE Transactions on Transportation Electrification 11, 486-498 (2025). <https://doi.org/10.1109/TTE.2024.3392208> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/sstr.202400640%7C10.1016/j.electacta.2021.138682%7C10.1016/j.electacta.2021.139639%7C10.1016/j.est.2022.104788%7C10.1016/j.est.2023.108650%7C10.1016/j.est.2023.110051%7C10.1016/j.est.2024.110431%7C10.1016/j.est.2026.124264%7C10.1016/j.etran.2026.100627%7C10.1016/j.jclepro.2022.133235%7C10.1016/j.jclepro.2023.138795%7C10.1016/j.jpowsour.2020.229270%7C10.1016/j.jpowsour.2022.231223%7C10.1016/j.jpowsour.2022.232050%7C10.1016/j.jpowsour.2024.234064%7C10.1038/s41598-021-98957-y%7C10.1109/tte.2024.3392208%7C10.1149/1945-7111/acd962%7C10.1149/1945-7111/acdd28>.

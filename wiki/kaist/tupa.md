# 교통·도시계획 AI 연구실 (TUPA, Transport and Urban Planning with AI)

**KAIST 조천식모빌리티대학원 · 김인희 교수**

- 분야: 인프라 기반 자율주행(교차로·도로 설비가 차량 판단을 돕는 방식)과 차량–사물 통신(C-V2X), 디지털 트윈(현실의 도로와 차량을 컴퓨터 속에 똑같이 옮긴 가상 모형)·교통 시뮬레이션과 드라이빙 시뮬레이터 실험, 대형 언어 모델(LLM) 기반 교통 수요 시뮬레이션, 도시 이동의 접근성·형평성 분석, 보행자·군중 안전과 재난 대응
- 대분야: 건설·도시·인프라, 컴퓨팅·AI
- 태그: 교통·도시 계획[^research][^p6][^p5], 자율주행[^research], 디지털 트윈[^research][^home], 대형 언어 모델[^research]
- 홈페이지: <https://www.inhi.kim/>
- 근거와 출처: [TUPA 근거 페이지](tupa-sources.md)

> 사람들이 도시에서 더 안전하고 편하게 이동하도록 교통 시스템을 인공지능과 시뮬레이션으로 연구하는 연구실이다. 가상 도로와 운전 시뮬레이터로 운전자·보행자 반응을 실험하고, 교통 데이터로 사고 위험과 이동 패턴을 분석해 자율주행 시대의 교차로·도로 운영과 도시 설계를 돕는다.[^home][^research]

## 무엇을 연구하나

연구실은 KAIST 조천식모빌리티대학원 소속으로, 더 안전하고 스마트하며 지속가능한 모빌리티 시스템을 만들어 일상의 이동을 개선하는 것을 목표로 하고, 인공지능·디지털 트윈·시뮬레이션·데이터 기반 의사결정을 결합해 실제 도시·교통 문제를 푼다고 소개한다. KAIST 스핀아웃 기업 dochak과 함께 교통 시뮬레이션, 디지털 트윈, 드라이빙 시뮬레이터, 가상환경, 원격주행 기술로 연구와 실무를 잇는다고도 적는다.[^home] 연구 페이지는 연구를 다섯 축으로 나눈다.[^research]

첫째 **인프라 기반 자율주행**은 차량 혼자 판단하기 어려운 상황에서 교차로 같은 인프라가 C-V2X 통신과 엣지 연산(데이터가 생기는 현장 가까이에서 하는 계산)으로 속도를 제안하고, 노변 센서와 원격주행까지 제어 고리에 넣는 틀을 연구한다.[^research] 연구실은 신호 교차로의 딜레마 구간에서 통신 상태에 따라 운전자가 어떻게 반응하는지 시뮬레이터로 실험했다.[^p1]

둘째 **Physical AI**는 실제 세상에서 움직여야 하는 AI를 가상 환경에서 먼저 검증하는 연구로, 미시 교통 시뮬레이션(차량 한 대 한 대의 움직임을 흉내 내는 시뮬레이션)과 디지털 트윈을 결합하고 사람이 직접 운전하는 드라이빙 시뮬레이터 실험을 한다.[^research] 운전자가 자전거·전동킥보드를 추월하는 행동,[^p2] 보행자 수를 알려 주는 경고가 제동 행동에 주는 효과를 가상현실 운전 실험으로 분석했다.[^p3]

셋째 **LLM 기반 교통 시뮬레이션**은 대형 언어 모델과 생성 모델로 가상의 인구와 개인별 하루 활동 일정을 만들어 실제 도로망 시뮬레이션까지 잇는다.[^research] 드문드문하고 잡음 많은 GPS 기록에서 이동 경로를 복원하는 딥러닝 방법,[^p4] 도시 전체 도로망의 빠진 교통량을 채우는 방법을 개발했다.[^p5]

넷째 **도시 과학**은 20분 도시(생활에 필요한 곳을 20분 안에 갈 수 있는 도시 구상), 접근성·형평성, 공유 모빌리티와 대중교통 연계처럼 도시 규모의 이동 현상을 데이터로 분석한다.[^research] 거리의 풍경과 소리가 공유자전거 이용에 주는 영향을 분석했다.[^p6]

다섯째 **재난 AI**는 보행자와 군중이 몰릴 때의 압사·혼잡 위험을 예측하고 사고 전 상충을 실시간으로 평가하며, 가상현실 보행 시뮬레이터로 안전한 공간 설계를 돕는다.[^research] 신호 없는 교차로의 보행자 충돌 위험을 미리 평가하는 방법,[^p7] 코로나19 전후 노인 보행자 사고의 중상·사망 요인 변화를 분석했다.[^p8]

## 주요 연구 주제

### 1. 인프라 기반 자율주행과 C-V2X

딜레마 구간 통신 조건별 운전자 반응.[^p1] 대표 논문 1.

### 2. 드라이빙 시뮬레이터와 인간 요인

마이크로모빌리티 추월, 보행자 규모 경고.[^p2][^p3] 대표 논문 2, 3.

### 3. 교통 데이터 복원과 시뮬레이션

GPS 경로 복원, 도시 도로망 교통량 결측 보정.[^p4][^p5] 대표 논문 4, 5.

### 4. 도시 과학과 보행자 안전

시청각 인지와 공유자전거, 보행자 미래 충돌 평가, 노인 보행자 사고 요인.[^p6][^p7][^p8] 대표 논문 6, 7, 8.

## 대표 논문

랩 논문 목록의 2021–2026년 학술지 논문 가운데 교수가 마지막 저자인 것에서 다섯 연구 축을 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2025 | [How do the drivers react to different C-V2X-based communication conditions in dilemma zones? A driving simulator study](https://doi.org/10.1016/j.aap.2025.108208) · Accident Analysis & Prevention | 신호가 노란불로 바뀔 때 설지 갈지 애매한 딜레마 구간에서, 차량–사물 통신(C-V2X)이 주는 녹색 신호 남은 시간 정보가 운전자 판단을 어떻게 바꾸는지 Unity·VISSIM 연동 시뮬레이터로 운전자 62명에게 실험했다. 통신이 끊기면 그냥 통과하려는 경향이 커졌고, 정보가 제대로 오거나 잠시 끊겼다 오면 그 경향이 줄었다. 정보가 완전할 때 신호 위반 비율이 3.44% 줄었다.[^p1] | 1저자 Shi Ye, 마지막 저자 김인희 |
| 2 | 2026 | [Micro Mobility Safety Challenges: A Study on Drivers Overtaking Bicycles and E-Scooters in Relation to Road Conditions and Prior Riding Experience](https://doi.org/10.1016/j.trf.2025.103482) · Transportation Research Part F | 가상현실 운전 시뮬레이터로 30명이 자전거와 전동킥보드를 추월하는 행동을 분석했다. 직접 타 본 경험이 있는 운전자는 옆 간격을 더 넓게 두었고, 노면 상태가 나쁘면 간격과 시선 고정이 늘었다. 경험은 전동킥보드 추월 속도에 뚜렷한 영향을 주지 않았다.[^p2] | 1저자 Hyunchul Park, 마지막 저자 김인희 |
| 3 | 2024 | [Effects of driver's braking behavior by the real-time pedestrian scale warning system](https://doi.org/10.1016/j.aap.2024.107685) · Accident Analysis & Prevention | 횡단보도 앞 보행자 무리의 인원 정보를 알려 주는 운전자 경고 시스템을 가상현실 운전 시뮬레이터와 시선 추적기로 시험했다. 보행자가 많다는 정보를 받으면 충돌까지 남은 시간과 횡단보도까지의 거리가 12% 늘고 동공 지름이 9% 커지는 등 더 안전하게 제동했고, 밤에도 효과가 있었다.[^p3] | 1저자 Hyunchul Park, 마지막 저자 김인희 |
| 4 | 2025 | [Enhanced trajectory reconstruction from sparse and noisy GPS data: A progressive chunked transformer approach](https://doi.org/10.1016/j.commtr.2025.100200) · Communications in Transportation Research | 드문드문하고 잡음 많은 GPS 기록에서 이동 경로를 복원하는 딥러닝 모델(ProChunkFormer)을 만들었다. 먼저 중간 빈도의 경로를 만들고 나머지를 여러 조각으로 나눠 동시에 복원해, 오차 누적과 계산량을 줄였다. 택시 궤적 자료에서 기록 간격이 240초까지 벌어진 경우 정확도를 23.1% 높였다.[^p4] | 1저자 Yonghui Liu, 마지막 저자 김인희 |
| 5 | 2023 | [Large-Scale Network Imputation and Prediction of Traffic Volume Based on Multi-Source Data Collection System](https://doi.org/10.1177/03611981231158324) · Transportation Research Record | 교통 검지기를 새로 바꾸는 과정에서 생긴 대량의 빠진 자료를, 두 종류 검지기의 자료를 함께 배우는 시공간 그래프 신경망(도로망의 연결 구조와 시간 흐름을 함께 배우는 인공지능)으로 채웠다. 대전시 전체 도로망에 적용해 평균 오차가 5분당 12대 미만이었다.[^p5] | 1저자 Donghyun Kwon, 마지막 저자 김인희 |
| 6 | 2025 | [Synergistic role of audio-visual perceptions in promoting bikeshare for active travel](https://doi.org/10.1016/j.trd.2025.104806) · Transportation Research Part D | 중국 선전의 대규모 공유자전거 이용 자료와 어떤 요인이 결과에 얼마나 영향을 주었는지 보여 주는 설명 가능한 공간 기계학습으로, 넓은 범위의 도시 환경과 함께 거리에서 보이는 풍경과 들리는 소리가 자전거 이용에 주는 영향을 분석했다. 넓은 범위의 환경 요인이 가장 컸지만 가까운 범위에서는 소리가 풍경보다 설명력이 컸고, 안전하다고 느끼는 풍경과 자연의 소리처럼 둘이 어울릴 때 효과가 더 컸다.[^p6] | 1저자 Kaihan Zhang, 마지막 저자 김인희 |
| 7 | 2026 | [Evaluation of Pedestrian Future Conflict at Non-Signalized Intersections Based on Probabilistic Trajectory Prediction](https://doi.org/10.1109/tits.2026.3661062) · IEEE Transactions on Intelligent Transportation Systems | 신호 없는 교차로에서 보행자와 차량의 미래 충돌을 미리 평가하기 위해, 확률적 경로 예측과 새 안전 지표(SPTTC)를 결합했다. 네 가지 예측 모델과 결합해 F1 점수 0.77–0.84로 기준 방법보다 나았고, 아이처럼 예측하기 어려운 보행자, 밤, 빠진 자료 같은 상황에도 견고했다.[^p7] | 1저자 Tengfeng Lin, 마지막 저자 김인희 |
| 8 | 2024 | [Temporal instability of the determinants of fatal/severe elderly pedestrian injury outcomes in intersections and non-intersections before, during, and after the COVID-19 pandemic](https://doi.org/10.1016/j.aap.2024.107676) · Accident Analysis & Prevention | 서울의 2018–2022년 노인 보행자(64세 초과) 교통사고 자료로, 교차로와 비교차로에서 코로나19 전·중·후에 중상·사망에 영향을 준 요인을 따로 분석했다. 요인의 영향이 장소와 시기마다 달라졌고, 예컨대 팬데믹 뒤에는 횡단보도 위치가 교차로에서 사망 가능성을 더 크게 낮췄다.[^p8] | 1저자 Reuben Tamakloe, 마지막 저자 김인희 |

## 교수와 전문 분야

김인희 교수는 공주대 학사(2005)·석사(2007)와 호주 퀸즐랜드대 토목공학 박사(2014)를 받았다. 독일 교통 소프트웨어 기업 PTV Group에서 교통 엔지니어·플래너로 일했고(2007–2012), 호주 모나시대 토목공학과 강사·선임 강사(2015–2020), KAIST 건설및환경공학과 초빙교수(2019–2020), 공주대 부교수(2020–2022)를 거쳐 2023년부터 KAIST 조천식모빌리티대학원 부교수다. 미국 뉴욕대 겸임 부교수(2024–), 모나시대 겸임 선임 강사(2020–)도 맡고 있다.[^mo][^people] 연구실 소개는 교수가 KAIST 모빌리티 AX 연구소장과 KAIST–NYU 공동연구그룹 모빌리티 AI 분과장을 맡고 있다고 적는다.[^home]

논문으로 보면 전문 분야는 세 갈래다.

- **운전자·보행자 행동 실험과 교통안전 분석**.[^p1][^p2][^p3][^p7][^p8]
- **교통 데이터 복원·예측을 위한 딥러닝**.[^p4][^p5]
- **도시 이동과 공유 모빌리티 분석**.[^p6]

## 응용 분야

대표 논문과 과제 목록으로 보면 자율주행 교차로 운영, 도로교통 디지털 트윈, 보행자 안전 경고 시스템, 교통 수요 분석과 도시계획에 닿아 있다.[^p1][^p3][^p5][^projects] 연구실 첫 화면은 저널 논문 90편, 교수로 임용된 졸업생 6명을 적고,[^home] 특허 목록에는 보행자 규모 정보 기반 운전자 경고, 환경 영향을 고려한 강화학습 신호 제어 같은 출원이 있다.[^papers]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다. "시작"은 랩이 적은 입학 연도다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Gyounghoon Chun | 박사후연구원 |  | 교차로 운영 · 강화학습 |  |
| Taeho Oh | 박사후연구원 |  | AI 인프라 교통 운영 · 디지털 트윈·메타버스 기반 교통 시뮬레이션 · 월드 모델 · 원격 조종 | 1, 2, 3 |
| Fan Wu | 박사후연구원 |  | 교통 상태 추정 · 기계학습 |  |
| Meng Li | 박사후연구원 |  | 비전-언어 모델 · 자율주행차 · 교통 시뮬레이션 · 월드 모델 |  |
| Linkun Liu | 박사과정 | 2026 | 지능형 교통체계(ITS) · 자율주행차 · AI 안전 |  |
| Yu Deng | 박사과정 | 2026 | 멀티모달 데이터 분석 · 자율주행 안전성 평가 · 비전-언어 모델(VLM) |  |
| Jaehyuck Lim | 박사과정 | 2026 | 휴머노이드 · Sim-to-Real 전이 · 시뮬레이터 기반 교통안전 | 2 |
| Eric Min Kim | 박사과정 | 2026 |  |  |
| Hyunchul Park | 박사과정 | 2025 | V2X 기반 휴머노이드 드라이버 · 자율주행차 안전성 평가 · 인간 중심 교통안전 | 2, 3 |
| Kaihan Zhang | 박사과정 | 2024 | 보행자 안전 · 설명가능 AI · 가로경관 인지 | 6, 8 |
| Ng Hui Zhi | 박사과정 | 2024 | 로보택시 · 차량 운영 관리 · 전동킥보드 · 안전 · 강화학습 |  |
| Kervin Lucas | 박사과정 | 2024 | 신뢰할 수 있는 AI · 활동기반모형 내 LLM 활용 · 활동 스케줄러 |  |
| Donghyun Kwon | 박사과정 | 2023 | LLM 기반 활동기반모형 · 통행수요 시뮬레이션 · 교통 데이터 결측 보정 및 예측 | 5 |
| Younghi Liu | 박사과정 | 2023 |  |  |
| Tengfeng Lin | 박사과정 | 2022 | 보행자 안전 · 상충 지표 · 궤적 예측 · 군중 시뮬레이션 | 7 |
| Sara Abbasvand | 석사과정 | 2026 | 교통계획 · 대중교통 노선망 설계 · 교통 데이터 분석 |  |
| Daeyong Kim | 석사과정 | 2026 | 비전-언어 모델(VLM) · 비전-언어-행동 모델(VLA) · 딥러닝 아키텍처 및 멀티모달 학습 · 종단간 자율주행 |  |
| Chanwoo Moon | 석사과정 | 2026 | AI 기반 통행행태 모델링 · 행태 검증 · LLM 코딩 에이전트 기반 교통 시뮬레이션 · 교통 분야 에이전틱 AI · 대규모 언어모델 |  |
| Jihye Eum | 석사과정 | 2026 |  |  |
| Jongmyeung Ahn | 석사과정 | 2026 |  |  |
| Jungyoon Kim | 석사과정 | 2025 | 인간-컴퓨터 상호작용(HCI) · 자율주행·모빌리티 시스템 월드 모델 · VR/AR/XR |  |
| Junyoung Kim | 석사과정 | 2025 | 인간-로봇 안전 · 인간-로봇 상호작용 · 군중 동역학 · 로보틱스 · 디지털 트윈 · 인간공학 |  |
| MyeongHyeon Kim | 석사과정 | 2025 | 자율주행로봇(AMR) 내비게이션 · SPaT/R2X · ROS 2/Nav2 · 교차로 지능화 |  |
| Truyen Le-Minh | 석사과정 | 2025 | 교통안전 · 학습 기반 자율주행 제어 · 교통 시뮬레이션 |  |
| Yeji Yoo | 석사과정 | 2025 | 시뮬레이션 · 군중 동역학 · 보행자 안전 |  |
| Awais Anwer | 석사과정 (과정 표기 없음) |  | 교통 분야 에이전틱 AI · 교통 데이터 결측 보정 및 예측 |  |
| Yunha Lee | 인턴 (Stanford University, 2025–2026) |  |  |  |
| Biniam | 인턴 (KAIST 전산학부, 2026) |  |  |  |
| Jeongin Huh (허정인) | 인턴 (이화여대, 2026) |  |  |  |
| Chengjie | 방문 학생 (Southeast University, 2025) |  |  |  |
| Lurong Xu | 방문 학생 (Monash University, 2024–2025) |  |  |  |
| Changhee Kim | 인턴 (KAIST 전산학부, 2025) |  |  |  |
| Yeungmi Choi | 행정 직원 |  |  |  |

## 졸업생

랩 구성원 페이지 졸업생 구간의 이름, 과정, 랩이 적은 현재 소속이다. 교수의 모나시대 재직 시기 박사 졸업생을 포함한다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Reuben Tamakloe | 연구진(조교수) | 국민대 교수 |
| Jinwon Yoon | 박사후연구원 종료 (2025) | 고려대 조교수 |
| Taeho Oh | 박사 (2025) | KAIST 박사후연구원 |
| Dong Xiao | 박사 (2024) | Monash University 연구원 |
| Chunliang Wu | 박사 (2023) | Lecturer (Assistant Professor), University of Western Australia |
| Zahra Nourmohammadi | 박사 (2022) | UNSW |
| Wenhua Jiang | 박사 (2022) | University of Edinburgh 연구원 |
| Bo Wang | 박사 (2022) | University of Melbourne 연구원 |
| Kai Huang | 박사 (2020) | Southeast University 조교수 |
| Tianqi Gu | 박사 (2020) | Monash University 조교수 |
| Xinyuan Chen | 박사 (2019) | 난징항공항천대 조교수 |
| Wentao Jing | 박사 (2018) | HyperPay 최고운영책임자 |
| Xiaoying Cao | 박사 (2017) | VicRoads 선임 평가관 |
| Songmi Paek | 석사 (2026) | 국토연구원 |
| Jaehyuck Lim | 석사 (2026) | KAIST 박사과정 |
| Jaeeun Jung | 석사 (2026) | 한국철도기술연구원 |
| Eric Min Kim | 석사 (2026) | KAIST 박사과정 |
| Junyuk Lee | 석사 (2026) | KAIST 박사과정 |
| Kexin Zhu | 석사 (2026) | 상하이 현대자동차(랩 표기 Hyundai Motos in Shanghai) |
| Jihae Peak | 석사 (2026) | 코레일 |
| Hyeoncheol Noh | 석사 (2026) | 코레일 |
| Chungkyo Hong | 석사 (2026) | 코레일 |
| Hyunchul Park | 석사 (2025) | KAIST 박사과정 |
| Donghyun Kwon | 석사 (2023) | KAIST 박사과정 |
| Fatemeh Nourmohammadi | 석사 (2023) | UNSW 박사과정 |

## 최근 논문 목록 (2021–2026)

랩 논문 목록의 2021년 이후 학술지 논문 66편, 학술대회 논문 72편, 단행본 장 1편이다. 학술대회 논문과 단행본 장은 학술지명 뒤에 표시했다.[^papers]

**2027**

- Fan Wu, Taeho Oh, Sanghoon Son, Inhi Kim, Kitae Jang, Meng Li. "Reassessing Autonomous Vehicle-Dedicated Lanes for Sustainable Planning under Realistic Driving Behavior". *Transportation Research Board (학술대회)*.

**2026**

- Benwang Chen, Jian Li, Jiyuan Song, Yao Tu, Lei Yang, Inhi Kim, Heye Huang, Kitae Jang. "RS-Mamba: Temporal State Space Modeling for Single-Image Rolling Shutter Deblurring". *IEEE Internet of Things Journal*.
- Jihye Baek, Jungyoon Kim, Hyunchul Park, Inhi Kim. "How age-related constraints reshape transport disadvantage in dynamic railway information systems: Evidence from virtual aging simulation". *Journal of Urban Mobility*.
- Zhuonan Jiang, Tianqi Gu, Jiayan Zhang, Hyungchul Chung, Inhi Kim. "Carbon savings in ride-pooling: A data-driven, route-based analysis from East Asia". *Transportation Research Part D: Transport and Environment*.
- Reuben Tamakloe, Kaihan Zhang, Donghyun Kwon, Inhi Kim. "Elderly pedestrian safety in silver zones: A temporal instability analysis of injury severity determinants". *Journal of Traffic and Transportation Engineering*.
- Inhi Kim, Kitae Jang, Shin Hyoung Park and Shin-Hyung Cho. "Heuristic Approach for Solving Demand Responsive Transport Scheduling Problems". *International Conference Series on Competition and Ownership in Land Passenger Transport (학술대회)*.
- Zechao Ma, Tianqi Gu, Jiayan Zhang, Long Cheng, Inhi Kim, Bin Yu. "Carbon-efficient ride-pooling at intercity railway hubs: Nonlinear topological mechanisms and algorithmic insights". *Transportation Research Part D: Transport and Environment*.
- Shi Ye, Taeho Oh, Yasir Ali, Inhi Kim, Seunghee Park, Tiantian Chen. "Impact of C-V2X-enabled stop/go advisory system on driving behavior in yellow-light dilemmas: evidence from a bivariate copula model". *Analytic Methods in Accident Research*.
- Gyounghoon Chun, Kaihan Zhang, Reuben Tamakloe, Taeho Oh, Inhi Kim. "Built Environment Determinants of E-Scooter Route Deviations: A Macro- and Micro-Scale Analysis". *Cities*.
- Changhun Kim, Junghwa Kim, Inhi Kim. "Identifying critical urban traffic risks for autonomous vehicle crash severity". *Journal of Transportation Safety & Security*.
- Jungyoon Kim, Junyoung Kim, Inhi Kim. "Same Environment, Opposite Errors: Asymmetric Effects of Rendering Type on Spatial Internalization and Externalization in VR". *ISMAR 2026 (학술대회)*.
- Yonghui Liu, Inhi Kim. "Multi-Camera Pedestrian Full Trajectory Perception Using YOLO, DeepSORT, and Homography Transform". *The 15th Asia-Pacific Conference on Transportation and the Environment (학술대회)*.
- Hui Zhi Ng, Inhi Kim. "Evaluation of Pedestrian Future Conflict at Non-Signalized Intersections Based on Probabilistic Trajectory Prediction". *The 15th Asia-Pacific Conference on Transportation and the Environment (학술대회)*.
- Chanwoo Moon, Kaihan Zhang, Jinehee Kim, Inhi Kim. "The Impact of Head-Up Display Warnings on Aggressive Driving: Visual and Behavior Insights". *The 15th Asia-Pacific Conference on Transportation and the Environment (학술대회)*.
- Meng Li, Shunchao Wang, Yuhao Wang, Zhibin Li. "Generalizable Semantic-aware Road Network Representation Learning". *The 15th Asia-Pacific Conference on Transportation and the Environment (학술대회)*.
- Hyunchul Park, Taeho Oh, Yonghui Liu, Inhi Kim. "Cross-Taxonomy Label Alignment in Transportation Networks". *The 15th Asia-Pacific Conference on Transportation and the Environment (학술대회)*.
- Jaehyuck Lim, Inhi Kim. "A Generalizable Semantic Graph Learning Framework for Road Network Representation". *The 15th Asia-Pacific Conference on Transportation and the Environment (학술대회)*.
- Jungyoon Kim, Inhi Kim, Taeho Oh. "Cross-Taxonomy Label Alignment in Transportation Networks With Prompt-Driven Large Language Models". *The 15th Asia-Pacific Conference on Transportation and the Environment (학술대회)*.
- Tengfeng Lin, Tiantian CHEN, Inhi Kim. "Analyzing the Impact of Network Latency When Integrating Real-Time Vehicle Information in a Virtual Environment". *The 15th Asia-Pacific Conference on Transportation and the Environment (학술대회)*.
- Tengfeng Lin, Yeji Yoo, Seunghee Park, Majid Sarvi, Inhi Kim. "Evaluating Spatiotemporal Influence on Trip Chain Prediction". *The 15th Asia-Pacific Conference on Transportation and the Environment (학술대회)*.
- Tengfeng Lin, Zhixiong Jin, Hwasoo Yeo, Inhi Kim. "Trip Generation in the Philippines: Analysis of Traditional, Geospatial, and AI-based Models". *The 2026 World Congress on Advances in Civil, Environmental & Materials Research (학술대회)*.
- Reuben Tamakloe, Inhi Kim. "Sequential Generation Procedure of Population Synthesis Using Conditional Generative Adversarial Network to Overcome Re-sampling Stage". *The 15th Asia-Pacific Conference on Transportation and the Environment (학술대회)*.
- Myeonghyeon Kim, Junyoung Kim, Inhi Kim, Gyounghun Chun. "Understanding the Impact of Environmental and Rider Factors on Scooter Safety: A Virtual Reality Study". *The 15th Asia-Pacific Conference on Transportation and the Environment (학술대회)*.
- Truyen Le-Minh, Inhi Kim. "E-Scooter Alarm Warning System for Pothole Detection: A Simulation Study". *The 15th Asia-Pacific Conference on Transportation and the Environment (학술대회)*.
- Min Kim, Inhi Kim. "Characterizing Spatiotemporal Patterns of Shared Micro-Electric Vehicle Charging and Usage Behavior: Evidence from a Multi-City Pilot Project". *The 15th Asia-Pacific Conference on Transportation and the Environment (학술대회)*.
- Kervin Lucas, Tengfeng Lin, Junyuk Lee, Inhi Kim. "Recursive Neurosymbolic Optimization for the Semantic Repair of Structurally Inconsistent Household Travel Surveys Using LLM". *The 15th Asia-Pacific Conference on Transportation and the Environment (학술대회)*.
- Shi Ye, Taeho Oh, Yasir Ali, Inhi Kim and Tiantian Chen. "Impact of C-V2X-enabled Stop/Go Advisory System on Driving Behavior in Yellow-light Dilemmas: Evidence from a Random-Parameters Bivariate Copula Model". *Road Safety and Simulation Conference (학술대회)*.
- Inhi Kim, Kitae Jang, Shin Hyoung Park and Shin-Hyung Cho. "Mode Choice Behavior based Spatial Impact Analysis of Mobility Hubs Integrating High-speed Modes: Urban Air Mobility and Express Rail in Seoul Metropolitan Area". *19th International Conference on Competition and Land Passenger Transport (학술대회)*.
- Inhi Kim, Kitae Jang, Shin Hyoung Park and Shin-Hyung Cho. "Heuristic Approach for Solving Demand Responsive Transport Scheduling Problems". *19th International Conference on Competition and Land Passenger Transport (학술대회)*.
- Myeonghyeon Kim, Junyoung Kim, Seunghee Park, Inhi Kim. "Time-Aware Crosswalk Navigation for Autonomous Mobile Robots Using SPaT-Based R2X Communication". *2026 IEEE 29th International Conference on Intelligent Transportation Systems (ITSC) (학술대회)*.
- Kexin Zhu; Inhi Kim. "Safety-Critical Interactions of Electric Scooter Riders in Urban Traffic: Evidence from a VR-Based Experiment". *The 15th Asia-Pacific Conference on Transportation and the Environment (학술대회)*.
- Zechao Ma, Tianqi Gu, Graham Currie, Long Cheng, Inhi Kim. "From anxiety to advantage: a multi-year longitudinal evidence of behavioral and spatial adaptation in electric ride-hailing". *Travel Behaviour and Society*.
- Tengfeng Lin, Tiantian Chen, Inhi Kim. "Integrating deep learning–based motion prediction into extreme value theory: Incorporating motion heterogeneity and interaction behavior into crash risk estimation". *Analytic Methods in Accident Research*.
- Reuben Tamakloe, Livingstone Divine Caesar, Inhi Kim. "How vehicle-to-grid configurations shape plug-in electric vehicle purchase intentions: Evidence of non-transferable effects". *Technological Forecasting and Social Change*.
- Lurong Xu, Tengfeng Lin, Steve O’Hern, Alexa Delbosc, Zhuo Chen, Inhi Kim, Shuli Luo. "When feeling safe becomes risky: A VR-EEG-computer vision framework for analyzing cyclist safety in dynamic traffic environment". *Accident Analysis & Prevention*.
- Hyungchul Chung, Tianqi Gu, Kaihan Zhang, Inhi Kim, Xiang Wang, Long Cheng. "What makes older adults transfer? built environment drivers of metro–bus interchange: a case of Suzhou, Jiangsu, China". *Case Studies on Transport Policy*.
- Yiping Yan, Ying Yang, Inhi Kim. "Embodied Intelligence at Scale: Cross-Platform Transfer and Large-Scale Sensing in Autonomous Mobility". *Communications in Transportation Research*.
- Junyoung Kim, Jungyoon Kim, Kexin Zhu, Inhi Kim, Seunghee Park. "Is Meshing Always Necessary? The Limited Impact of Rendering Fidelity on VR Spatial Perception". *2026 IEEE Conference on Virtual Reality and 3D User Interfaces Abstracts and Workshops (VRW) (학술대회)*.
- Tengfeng Lin, Zhixiong Jin, Hwasoo Yeo, Inhi Kim. "Evaluation of Pedestrian Future Conflict at Non-Signalized Intersections Based on Probabilistic Trajectory Prediction". *IEEE Transactions on Intelligent Transportation Systems*.
- Taeho Oh, Eric Min Kim, Thanh-Tung Nguyen, Hyeonjun Jeong, Yoojin Choi, Lucas Liebe, Seonmyeong Lee, Hanbin Jang, Gyounghoon Chun, Inhi Kim, Kitae Jang, Heejin Ahn, Dongsuk Kum, In Gwun Jang, Dongman Lee. "Scalable and interoperable C-V2X framework for real-time intelligent decision support in autonomous mobility". *Communications in Transportation Research*.
- Reuben Tamakloe, Linus Dinam Caesar, Inhi Kim. "Determinants of battery electric vehicle adoption concerns: insights from commercial fleet owners". *Transportation Research Part A: Policy and Practice 205, 104874*.
- Hyunchul Park, Taeho Oh, Jaehyuck Lim, Inhi Kim. "Micro Mobility Safety Challenges: A Study on Drivers Overtaking Bicycles and E-Scooters in Relation to Road Conditions and Prior Riding Experience". *Transportation Research Part F: Traffic Psychology and Behaviour 117, 103482*.
- Jiaqi Zhang, Junfeng Jiao, Xin Wang, Inhi Kim, Tianqi Gu. "Who waits longer to pick you up? behavioral and spatial inequities in ride-hailing pickup time based on real-world platform data". *Travel Behaviour and Society 43, 101224*.
- Kaihan Zhang, Bo Chen, Reuben Tamakloe, Yang Bai, Inhi Kim. "Does the streetscape built environment matter in explaining crash injury severity among older adults?". *Journal of Transport Geography 131, 104540*.
- Chutian Zhuang, Tianqi Gu, Inhi Kim, Hyungchul Chung, Kaihan Zhang. "Platform-induced time-space trade-offs in ride-hailing: Multi-homing as a response to operational constraints". *Journal of Transport Geography 131, 104533*.
- Kaihan Zhang, Xiaoyu Liu, Qihao Cui, Xueting Gao, Mengqiu Cao, Inhi Kim. "Social-psychological determinants and nonlinear thresholds: behavioral insights into urban air mobility adoption as an airport shuttle". *Transportation Research Part A: Policy and Practice 205, 104856*.
- Tianqi Gu, Inhi Kim, Lei Cheng. "Managing coexistence between taxis and ride-hailing services: A longitudinal case study of operational strategies and policy implications". *Case Studies on Transport Policy, 101718*.

**2025**

- Jaehyuck Lim, Shin Hyoung Park, Inhi Kim. "The Impact of Head-Up Display Warnings on Aggressive Driving: Visual and Behavior Insights". *2025 IEEE 28th International Conference on Intelligent Transportation Systems (ITSC) (학술대회)*.
- Hui Zhi Ng, Jaehyuck Lim, Taeho Oh, Inhi Kim. "Convenience Seekers vs. Traditionalists: Modeling Driver Heterogeneity in Parking App Adoption". *2025 IEEE 28th International Conference on Intelligent Transportation Systems (ITSC) (학술대회)*.
- Kexin Zhu; Inhi Kim; Taeho Oh; Shinhyoung Park. "SPaT-Driven Robust Crosswalk Navigation for Autonomous Mobile Robots". *2025 IEEE 28th International Conference on Intelligent Transportation Systems (ITSC) (학술대회)*.
- Donghyun Kwon, Inhi Kim. "Generational Shifts in Autonomous Child Transport". *20th ITS Asia Pacific Forum 2025 (학술대회)*.
- Kervin Lucas, Alexis Fillone, Inhi Kim. "Probabilistic Trajectory Prediction-Based Evaluation of Pedestrian Future Conflicts at Non-Signalized Intersections". *20th ITS Asia Pacific Forum 2025 (학술대회)*.
- Kervin Lucas, Junyuk Lee, Songmi Paek, Inhi Kim. "PhysMamba-Flow: Accelerating Physically Plausible Crowd Simulation with Flow Matching and Bidirectional Mamba". *20th ITS Asia Pacific Forum 2025 (학술대회)*.
- Min Kim, Taeho Oh, Inhi Kim. "Integrating Deep Learning–Based Motion Prediction into Extreme Value Theory: Incorporating Motion Heterogeneity and Interaction Behavior into Crash Risk Estimation". *20th ITS Asia Pacific Forum 2025 (학술대회)*.
- Yonghui Liu, Inhi Kim. "Understanding Driver Cognitive and Behavioral Responses to Adaptive AR-HUD Navigation Systems". *2025 IEEE 28th International Conference on Intelligent Transportation Systems (ITSC) (학술대회)*.
- Yonghui Liu, Inhi Kim. "Effect of Take-Over Support Strategy on Situation-Awareness Recovery and Hazard Attention after Take-Over". *2025 IEEE 28th International Conference on Intelligent Transportation Systems (ITSC) (학술대회)*.
- Yonghui Liu, Inhi Kim. "Severity-Controllable Adversarial Testing of Highway Automated Vehicles Using Naturalistic Aggressive-Moment Statistics". *29TH INTERNATIONAL CONFERENCE OF HONG KONG SOCIETY FOR TRANSPORTATION STUDIES 2025 (학술대회)*.
- Yonghui Liu, Inhi Kim. "Network-level design of cacc in mixed traffic: a robust optimization framework with heterogeneous human drivers". *20th ITS Asia Pacific Forum 2025 (학술대회)*.
- Jaehyuck Lim, Inhi Kim. "Plausible Choices or Behavioural Evidence?Benchmarking SP-Grounded LLM Traveller Agents". *20th ITS Asia Pacific Forum 2025 (학술대회)*.
- Tengfeng Lin, Zhixiong Jin, Hwasoo Yeo, Inhi Kim. "Is Charging the Bottleneck? Scaling Electric Robotaxi Fleets on Manhattan’s Real Charging Infrastructure". *20th ITS Asia Pacific Forum 2025 (학술대회)*.
- Myeonghyeon Kim, Inhi Kim. "Enhanced trajectory reconstruction from sparse and noisy GPS data: A progressive chunked transformer approach". *20th ITS Asia Pacific Forum 2025 (학술대회)*.
- Jaehyuck Lim, Hyunchul Park, Taeho Oh, Inhi Kim. "The impact of information delivery systems in tunnels depending on lighting intensity and speed limit". *Tunnelling and Underground Space Technology 157, 106365*.
- Kaihan Zhang, Reuben Tamakloe, Inhi Kim. "Elderly Pedestrian Crash Severity: Exploring the Role of Human Perceived Streetscape Design Using Explainable Ensemble Learning". *TRB 104th Annual Meeting (학술대회)*.
- Yuting Liu, Qingyuan Li, Inhi Kim. "Enhanced trajectory reconstruction from sparse and noisy GPS data: A progressive chunked transformer approach". *Communications in Transportation Research 5, 100200*.
- Reuben Tamakloe, Mahdi Khorasani, Subasish Das, Inhi Kim. "Pattern recognition in crash clusters involving vehicles with advanced driving technologies". *Accident Analysis & Prevention 218, 108072*.
- Tengfeng Lin, Zhixiong Jin, Hwasoo Yeo, Inhi Kim, Kaihan Zhang. "A Surrogate Safety Measure at Non-Signalized Intersections Based on Probability Trajectory Prediction". *TRB 104th Annual Meeting (학술대회)*.
- Shi Ye, Tiantian Chen, Oscar Oviedo-Trespalacios, Yasir Ali, Taeho Oh, Inhi Kim. "How do the drivers react to different C-V2X-based communication conditions in dilemma zones? A driving simulator study". *Accident Analysis & Prevention 221, 108208*.
- Reuben Tamakloe, Mahdi Khorasani, Inhi Kim. "Differences in injury severities between elderly and non-elderly taxi driver at-fault crashes: Temporal instability and out-of-sample prediction". *Accident Analysis & Prevention 211, 107865*.
- Zhonghui Jiang, Tianqi Gu, Jiaqi Zhang, Hyungchul Chung, Inhi Kim. "Carbon savings in ride-pooling: A data-driven, route-based analysis from East Asia". *Transportation Research Part D: Transport and Environment 144, 104764*.
- Donghyun Kwon, Inhi Kim. "Customized Deep Generative Models to Resolve the Sampling Bias in Population Synthesis". *TRB 104th Annual Meeting (학술대회)*.
- Kaihan Zhang, Qunshan Song, Hui Ma, Waishan Qiu, Mei Li, Inhi Kim. "Synergistic role of audio-visual perceptions in promoting bikeshare for active travel". *Transportation Research Part D: Transport and Environment 145, 104806*.
- Songmi Paek, Tiantian Chen, Inhi Kim. "Redefining Urban Access: A Fresh Look at Accessibility and Equity in the 20-Minute City". *TRB 104th Annual Meeting (학술대회)*.
- Hyunchul Park, Taeho Oh, Jaehyuck Lim, Inhi Kim. "Micromobility Safety Challenges: A Study on Drivers Overtaking Bicycles and E-Scooters According to Road Conditions and Cross-Modal Experience". *TRB 104th Annual Meeting (학술대회)*.
- Tianqi Gu, Weiping Xu, Peiran Shi, Rongrong Wang, Inhi Kim. "Taxi in competition with online car-hailing drivers: policy implication to operating strategies". *Multimodal Transportation 3 (2), 100129*.
- Jaeeun Jung, Inhi Kim, Jinwon Yoon. "EcoMRL: Deep Reinforcement Learning-Based Traffic Signal Control for Urban Air Quality". *International Journal of Sustainable Transportation 19 (8), 720-729*.
- Jaeeun Jung, Gyounghoon Chun, Inhi Kim. "A Novel Roundabout Operation Strategy Using Reinforcement Learning Based Single-Agent Robot Speed Control". *TRB 104th Annual Meeting (학술대회)*.
- Yuting Liu, Inhi Kim. "Sequential Decomposition and Attribution for Trajectory Forecasting". *Knowledge-Based Systems, 115204*.
- Jinwon Yoon, Byeongjoon Noh, Inhi Kim. "DARK-LLM: Description Data Auto-Labeling with Reliable Keyword Using LLM for Analyzing Causes of Autonomous Vehicle Disengagements". *TRB 104th Annual Meeting (학술대회)*.
- Fatemeh Nourmohammadi, Zahra Nourmohammadi, Inhi Kim, Heechan Kang. "Impact of COVID-19 pandemic on characteristic of bike-sharing systems near metro and bus stations". *International Journal of Urban Sciences 29 (3), 563-581*.
- Tianqi Gu, Kaihan Zhang, Weiping Xu, Chutian Zhuang, Zhonghui Jiang, Inhi Kim, Hyungchul Chung. "Free interchange for better transit? Assessing the multi-dimensional impacts on metro to bus interchange behavior − insights from an explainable machine learning method". *Travel Behaviour and Society 38, 100923*.

**2024**

- Kaihan Zhang, Reuben Tamakloe, Inhi Kim. "The Role of Human Subjective Perceptions and Objective Measurements of the Urban Environment in Explaining Pedestrian Injury Severity". *ICTCT Conference (학술대회)*.
- Chengzhong Tu, Lei Wang, Jaehyuck Lim, Inhi Kim. "Advancements and prospects in multisensor fusion for autonomous driving". *Journal of Intelligent and Connected Vehicles 7 (4), 245-247*.
- Tengfeng Lin, Zhixiong Jin, Hwasoo Yeo, Inhi Kim. "Predicted Relative Time-to-Collision: Evaluating Pedestrian Potential Risk at Non-Signalized Intersections". *ICTCT Conference (학술대회)*.
- Songmi Paek, Hyungchul Chung, Inhi Kim. "Assessing Mass Circular Tram Service Equity in Metropolitan City". *TRB 103rd Annual Meeting (학술대회)*.
- Reuben Tamakloe, Kaihan Zhang, Asim Alogaili, Inhi Kim. "Differences Between Pedestrian Injury Severity Determinants at School and Non-School Zones: New Findings from Streetscape Quality Factors". *ICTCT Conference (학술대회)*.
- Kaihan Zhang, Reuben Tamakloe, Inhi Kim. "Factors Influencing Injury Severity Among Elderly Pedestrians: Insights from Urban Imagery and Explainable Machine Learning". *ICTCT Conference (학술대회)*.
- Kaihan Zhang, Reuben Tamakloe, Mengqiu Cao, Inhi Kim. "Exploring fatal/severe pedestrian injury crash frequency at school zone crash hotspots: using interpretable machine learning to assess the micro-level street environment". *Journal of Transport Geography 121, 104034*.
- Tianqi Gu, Inhi Kim, Graham Currie, Weiping Xu. "Understanding shared bike usages toward metros with fewer physical road separations". *Case Studies on Transport Policy 18, 101281*.
- Reuben Tamakloe, Kaihan Zhang, Inhi Kim. "Variability in the Impact of Factors Influencing Elderly Pedestrian-Injuries in Crashes at Intersections and Non-Intersections Before, During, and After the COVID-19 Pandemic". *ICTCT Conference (학술대회)*.
- Francis G Phi, Bumsu Cho, Jungeun Kim, Hyungik Cho, Yun Wook Choo, Dookie Kim, Inhi Kim. "Machine learning application to seismic site classification prediction model using Horizontal-to-Vertical Spectral Ratio (HVSR) of strong-ground motions". *Geomechanics & Engineering 37 (6), 539-554*.
- Duy Quy Nguyen-Phuoc, Nhat Xuan Mai, Inhi Kim, Oscar Oviedo-Trespalacios. "Questioning penalties and road safety Policies: Are they enough to deter risky motorcyclist Behavior?". *Accident Analysis & Prevention 207, 107756*.
- Reuben Tamakloe, Kaihan Zhang, Inhi Kim. "Temporal instability of the determinants of fatal/severe elderly pedestrian injury outcomes in intersections and non-intersections before, during, and after the COVID-19 pandemic". *Accident Analysis & Prevention 205, 107676*.
- Hyunsu Park, Shin-Hyung Cho, Inhi Kim, Kitae Jang, Shin Hyoung Park. "Is It Possible to Substitute the Taxi Travel Demand to Demand Responsive Transport?". *Transit Data 2024 (학술대회)*.
- Jaehyuck Lim, Hyunchul Park, Taeho Oh, Inhi Kim. "The Impact of Information Delivery System in Tunnels Depending on Lighting Intensity and Speed Limit". *TRB 103rd Annual Meeting (학술대회)*.
- Taeho Oh, Inhi Kim, Zhibin Li. "Exploring Safe Overtaking Behavior Threshold Considering Human Interactions Using Multi-Agent Driving Simulator". *TRB 103rd Annual Meeting (학술대회)*.
- Taeho Oh, Jaehyuck Lim, Reuben Tamakloe, Zhibin Li, Inhi Kim. "Enhancing mutual understanding of e-scooter user's perspective in overtaking maneuver through replaying own driving trajectory". *Accident Analysis & Prevention 207, 107750*.
- Dongyang Xiao, Inhi Kim, Nan Zheng. "Does built environment have impact on traffic congestion?-A bootstrap mediation analysis on a case study of Melbourne". *Transportation Research Part A: Policy and Practice 190, 104297*.
- Reuben Tamakloe, Kaihan Zhang, Ahmed Hossain, Inhi Kim, Shin Hyoung Park. "Critical risk factors associated with fatal/severe crash outcomes in personal mobility device rider at-fault crashes: A two-step inter-cluster rule mining technique". *Accident Analysis & Prevention 199, 107527*.
- Hyunchul Park, Taeho Oh, Inhi Kim. "Effects of driver's braking behavior by the real-time pedestrian scale warning system". *Accident Analysis & Prevention 205, 107685*.
- Donghyun Kwon, Eui-Jin Kim, Inhi Kim. "Customized Deep Generative Models to Resolve the Sampling Bias in Population Synthesis". *TRB 103rd Annual Meeting (학술대회)*.
- Shin-Hyung Cho, Kitae Jang, Inhi Kim, Shin Hyoung Park. "Evaluating the Sustainable Urban Mobility for Public Transit Incorporating Geospatial Modeling Approach". *Transit Data 2024 (학술대회)*.

**2023**

- Wenhua Jiang, Nan Zheng, Inhi Kim. "Missing data imputation for transfer passenger flow identified from in-station WiFi systems". *Transportmetrica B: Transport Dynamics 11 (1), 325-342*.
- Bo Wang, Hai L Vu, Inhi Kim, Chen Cai. "Distributional prediction of short-term traffic using neural networks". *Engineering Applications of Artificial Intelligence 126, 107061*.
- Fatemeh Nourmohammadi, Zahra Nourmohammadi, Jinwoo Lee, Inhi Kim. "Designing Patrol Ship Routes Based on Multi Data Sources for Marine Environment". *TRB 102nd Annual Meeting (학술대회)*.
- Hyunchul Park, Taeho Oh, Inhi Kim. "Effects of Driver's Braking Response by the Real-Time Pedestrian Scale Warning System". *TRB 102nd Annual Meeting (학술대회)*.
- Donghyun Kwon, Inhi Kim. "Enhancing Deep Generative Models for Distinguishing Sampling Zeros and Structural Zeros in Population Synthesis". *hEART 2023 Symposium (학술대회)*.
- Jaeeun Jung, Taeho Oh, Inhi Kim, Shinhyoung Park. "Open-Sourced Real-Time Visualization Platform for Traffic Simulation". *ANT Conference 2023 (학술대회)*.
- Chunliang Wu, Inhi Kim, Zhenliang Ma. "Deep Reinforcement Learning Based Traffic Signal Control: A Comparative Analysis". *ANT Conference 2023 (학술대회)*.
- Donghyun Kwon, Changhee Lee, Heechan Kang, Inhi Kim. "Large-Scale Network Imputation and Prediction of Traffic Volume Based on Multi-Source Data Collection System". *Transportation Research Record 2677 (9), 30-42*.
- Zahra Nourmohammadi, Fatemeh Nourmohammadi, Inhi Kim, Shin Hyoung Park. "A deep spatiotemporal approach in maritime accident prediction: A case study of the territorial sea of South Korea". *Ocean Engineering 270, 113565*.
- Hyeokjun Jang, Kitae Jang, Inhi Kim. "Analyzing the Impact of Autonomous Vehicles on Urban Traffic Flow at the Large Scale Network Using Real-World Data". *IEEE ITSC 2023 (학술대회)*.
- Yeji Yoo, Tiantian Chen, Kitae Jang, Inhi Kim. "Impact on Platooning of Autonomous Vehicles Using Macro to Micro Simulations". *ANT Conference 2023 (학술대회)*.
- Taeho Oh, Inhi Kim, Zhibin Li. "Robust Overtaking Behavior with Human Interaction in Multi-Agent Driving Simulator Supported by Machine Learning". *TRB 102nd Annual Meeting (학술대회)*.
- Sicong Zhu, Hao Yue, Tatsuto Suzuki, Inhi Kim, Lei Yu, Qing Lan. "A UWB/INS Trajectory Tracking System Application in a Cycling Safety Study". *Sensors 23 (7), 3629*.

**2022**

- Hyunchul Park, Taeho Oh, Inhi Kim. "Validation of Spatial Orientation Skill Using Virtual Reality Treadmill". *ITS World Congress 2022 (학술대회)*.
- Donghyun Kwon, Taeho Oh, Changhee Lee, Inhi Kim. "Large Scale Multi-Source Traffic Flow Forecasting Based on Attention Based Spatio-Temporal Graph Convolutional Networks – LSTM". *ITS World Congress 2022 (학술대회)*.
- Taeho Oh, Yanping Xu, Zhibin Li, Inhi Kim. "Driving Risk Analysis Based on Driving Experience at Hook-Turn Intersection Using the Emerging Virtual Reality Technology". *Journal of Advanced Transportation 2022 (1), 8929826*.
- Taeho Oh, Inhi Kim. "Overtaking Maneuvers Using Multi-Agent Systems on a Two-Lane Two-Way Road". *ITS World Congress 2022 (학술대회)*.
- Bo Wang, Hai L. Vu, Inhi Kim, Chen Cai. "Short-term traffic flow prediction in bike-sharing networks". *Journal of intelligent transportation systems 26 (4), 461-475*.
- Yegi Yoo, Inhi Kim. "Connected Autonomous Vehicles Intersection Capacity Analysis Considering HCM 7th: Case Study of Jeju Innovation City". *Journal of Korean Society of Transportation 40 (6), 879-894*.
- Dong Xiao, Inhi Kim, Nan Zheng. "Recent advances in understanding the impact of built environment on traffic performance". *Multimodal Transportation 1 (4), 100034*.
- Lurong Xu, Taeho Oh, Inhi Kim, Xiaojian Hu. "Are shared streets acceptable to pedestrians and drivers? Evidence from Virtual Reality experiments". *PLoS one 17 (4), e0266591*.
- Hyunchul Park, Taeho Oh, Inhi Kim. "A Study on Validation of Omnidirectional VR Treadmill by Comparison of Spatial Orientation Skills". *The Journal of The Korea Institute of Intelligent Transport Systems 21 (5)*.
- Hyeonchoel Jeong, Inhi Kim, Keejun Han, Jungeun Kim. "Comprehensive Analysis of Traffic Accidents in Seoul: Major Factors and Types Affecting Injury Severity". *Applied Sciences 12 (4), 1790*.
- Yeji Yoo, Donghyun Kwon, Inhi Kim. "An Impact of Vehicles in the Platooning on the Road Network". *ITS World Congress 2022 (학술대회)*.
- Khaled Shaaban, Kiran Shakeel, Taha Hossein Rashidi, Inhi Kim. "Measuring users’ satisfaction of the road network using structural equation modeling". *International journal of sustainable transportation 16 (9), 792-803*.

**2021**

- L. Wu, Inhi Kim. "International Encyclopedia of Transportation". *Elsevier (단행본 장)*.
- Tianqi Gu, Inhi Kim, Graham Currie. "The two-wheeled renaissance in China-an empirical review of bicycle, E-bike, and motorbike development". *International journal of sustainable transportation 15 (4), 239-258*.
- Milad Haghani, Michiel C.J. Bliemer, Bilal Farooq, Inhi Kim, Zhibin Li, Cheol Oh, Zahra Shahhoseini, Hamish MacDougall. "Applications of brain imaging methods in driving behaviour research". *Accident Analysis & Prevention 154, 106093*.
- Yeji Yoo, J. Kang, S. Park, Inhi Kim. "Priority Signal Effect on S-BRT (Super Bus Rapid Transit)". *EASTS 2021 (학술대회)*.
- Chunliang Wu, Hyungchul Chung, Zhiyuan Liu, Inhi Kim. "Examining the effects of the built environment on topological properties of the bike-sharing network in Suzhou, China". *International Journal of Sustainable Transportation 15 (5), 338-350*.
- Donghyun Kwon, Hyunchul Park, Inhi Kim. "Traffic Data Calibration Collected by RSE Detectors Based on Deep Learning". *EASTS 2021 (학술대회)*.
- Bo Wang, Khaled Shaaban, Inhi Kim. "Revealing the hidden features in traffic prediction via entity embedding". *Personal and Ubiquitous Computing 25 (1), 21-31*.
- Lurong Xu, Taeho Oh, X. Hu, Inhi Kim. "Explore the Applicability of Shared Streets with Virtual Reality Technology: A Case Study of Suzhou, China". *TRB 100th Annual Meeting (학술대회)*.
- Zahra Nourmohammadi, Yeji Yoo, Inhi Kim. "Explore the Applicability of Machine Learning Method to Find Marine Causalities: A Case Study of Territorial Sea of South Korea". *EASTS 2021 (학술대회)*.
- Sicong Zhu, Inhi Kim, Keechoo Choi. "High-resolution simulation-based analysis of leading vehicle acceleration profiles at signalized intersections for emission modeling". *International Journal of Sustainable Transportation 15 (5), 375-385*.
- Chunliang Wu, Inhi Kim, Hyungchul Chung. "The effects of built environment spatial variation on bike-sharing usage: A case study of Suzhou, China". *Cities 110, 103063*.
- Jaeeun Jung, Taeho Oh, Inhi Kim. "Volume Delay Function Calibration Based on GPS Trajectory Data". *Journal of Korean Society of Transportation 39 (4), 399-408*.
- Khaled Shaaban, Iman Gharraie, Emanuele Sacchi, Inhi Kim. "Severity analysis of red-light-running-related crashes using structural equation modeling". *Journal of Transportation Safety & Security 13 (3), 278-297*.

## 특허

랩 논문 목록의 특허 구간이다.[^papers]

- 2024 · 경로 리플레이에 기반한 시각 전황을 활용하여 운전행태를 자기평가하는 방법 및 시스템 (Method and System for Self-Evaluating Driving Behavior Using Visual Context Based on Route Replay) (상태 대한민국 특허 출원)
- 2024 · 스트리트 뷰 이미지를 이용하여 전동 모빌리티의 경로선택을 분석하는 방법 및 시스템 (Method and System for Analyzing Route Selection of Electric Mobility Using Street View Images) (상태 대한민국 특허 출원)
- 2024 · 조건부 적대적 생성 모델 기반 교통수요 분석의 맞춤형 합성인구 생성 방법 및 시스템 (Method and System for Generating Customized Synthetic Population for Traffic Demand Analysis Based on Conditional Adversarial Generative Model) (상태 대한민국 특허 출원)
- 2024 · 확률 궤적 예측을 기반으로 비신호 교차로에서 보행자의 미래 충돌을 평가하는 방법 및 시스템 (Method and System for Evaluating Future Pedestrian Collisions at Unsignalized Intersections Based on Probabilistic Trajectory Prediction) (상태 대한민국 특허 출원)
- 2024 · 교통량 제어 계획을 이용한 교통신호 계획 생성 장치 및 방법 (Traffic Signal Plan Generation Device and Method Using Traffic Volume Control Plan) (상태 대한민국 특허 출원)
- 2024 · 환경영향을 고려한 강화학습 기반의 신호제어방법 및 시스템 (Reinforcement Learning-Based Signal Control Method and System Considering Environmental Impact) (상태 대한민국 특허 출원)
- 2024 · 보행자 규모 정보에 기반한 실시간 운전자 경고 방법 및 시스템 (Real-Time Driver Warning Method and System Based on Pedestrian Scale Information) (상태 대한민국 특허 출원)
- 2020 · 교통신호기 제어장치 (Traffic Signal Control Device) (상태 대한민국 등록특허 10-2166283)

## 연구 과제

랩 과제 페이지의 과제명(국문·영문), 기간, 지원 기관과 역할(PI는 연구책임자, Co-PI는 공동 연구책임자)이다.[^projects]

- 산업 특화 Physical AI 파운데이션 모델 개발 (Development of Industry-Specific Physical AI Foundation Models) (기간 2026–2029; 지원 IITP; 역할 PI)
- World Foundation Model 기반 E2E 자율주행기술 개발 및 실차 기반 글로벌 실증 (Development and Global Real-World Validation of World Foundation Model-Based End-to-End Autonomous Driving Technology) (기간 2026–2030; 지원 MSS; 역할 Co-PI)
- 혼재교통 환경을 위한 Physical AI·인프라 중심 자율주행 제어 프레임워크 개발 (Development of a Physical AI and Infrastructure-Centric AV Control Framework for Mixed-Autonomy Traffic Environments) (기간 2026–2030; 지원 NRF; 역할 PI)
- AI Plus K-건설 인프라 리질리언스 선도연구센터(ERC) (AI Plus K-Construction Infrastructure Resilience-ERC) (기간 2025–2032; 지원 NRF; 역할 Co-PI)
- 메타버스 기반 자율주행 가상환경 및 실증 기술 개발 (Development of Virtual Environment and Demonstration Technology for Automated Driving based on Metaverse) (기간 2023–2028; 지원 MOLIT; 역할 Co-PI)
- 반도체 제조라인 Intra-Fab 물류 운영 전략 연구 (Study on the Operation Strategies of Intra-Fab Transportation Systems in Semiconductor Manufacturing Lines) (기간 2023–2026; 지원 Samsung; 역할 Co-PI)
- 자율주행 Lv.4/4+ 빅데이터를 활용한 도로교통 디지털 트윈 개발 (Road Traffic Digital Twin Development Using Autonomous Driving Lv.4/4+ Big Data) (기간 2022–2026; 지원 MOLIT; 역할 Co-PI)
- 차기 팬데믹 대비 공유 모빌리티-대중교통 운영 계획 (Shared Mobility–Mass Transit Operational Plan for Preparing the Next Pandemic) (기간 2021–2026; 지원 NRF; 역할 PI)
- 2026–2030 한-아세안 교통협력 로드맵 (2026–2030 ASEAN-Korea Transport Cooperation Roadmap) (기간 2025–2025; 지원 MOLIT; 역할 PI)
- 보도 중심 지도 데이터를 활용한 배송로봇 경로 최적화 연구 (A Study on Delivery Robot Route Optimization Using Sidewalk-Centered Map Data) (기간 2024–2025; 지원 NRF; 역할 PI)
- 디지털 트윈 기술과 연계한 미시교통 시뮬레이션 개발 (Development of Microscopic Traffic Simulation through Integration with Digital Twin Technology) (기간 2023–2025; 지원 KAIST; 역할 PI)
- 빅데이터 플랫폼 및 센터 구축 (Big Data Platform and Centre Development) (기간 2021–2021; 지원 NIA; 역할 Co-PI)
- 2021 데이터 플래그십 사업 (2021 Data Flagship) (기간 2021–2022; 지원 NIA; 역할 Co-PI)
- 고양 창릉 공공주택지구 교통영향평가 (Goyang Changneung Public Housing District Traffic Impact Assessment) (기간 2021–2021; 지원 Korea Eng.; 역할 PI)
- 대심도 지하공간 지진 대비 데이터 융합 방재 기술 (Data Fusion Based Disaster Prevention Technology to Earthquakes for Deep and Large Underground Space) (기간 2021–2024; 지원 NRF; 역할 Co-PI)
- 해양 궤적 데이터 보간 기술 개발 (Development of Ocean Trajectory Data Interpolation) (기간 2021–2021; 지원 Join In; 역할 PI)
- 해양 궤적 데이터 분석 및 시각화 (Ocean Trajectory Data Analysis and Visualization) (기간 2021–2021; 지원 CRLab; 역할 PI)
- Super BRT 미시 시뮬레이션 분석 (Super BRT Micro Simulation Analysis) (기간 2020–2020; 지원 KRRI; 역할 PI)

## 소식

랩 소식 게시판의 글 제목과 분류다.[^news]

- 2026-09-01 · [과제 선정] Hyunchul Park Wins an NRF Research Grant
- 2026-08-16 · [사람들] Dr. Reuben Tamakloe appointed to faculty at Kookmin University
- 2026-07-24 · [과제 선정] 중소기업벤처 과제 수주
- 2026-07-15 · [일반] 도지사, KAIST 모빌리티 AX 연구소에서 계획 발표
- 2026-07-10 · [일반] 15th APTE 성공적 개최
- 2026-06-26 · [사람들] Appointed to the Editorial Board of Scientific Reports
- 2026-06-20 · [과제 선정] TUPA Secure Grants in the Global R&D Challenge
- 2026-06-17 · [과제 선정] Postdoc Researchers Taeho Oh, Fan Wu, and Meng Li – NRF Postdoc Group Grant Award
- 2026-06-15 · [수상] 코레일 파견 석사과정, 수석 졸업
- 2026-05-15 · [과제 선정] KAIST Cho Chun Shik Graduate School of Mobility to Spearhead Physical AI Talent Development
- 2026-05-15 · [과제 선정] IITP 생성형 AI 선도인재 양성사업 선정
- 2026-04-20 · [사람들] Dr. Meng Li 합류
- 2026-04-13 · [과제 선정] NRF Award – Core Research Program
- 2026-03-11 · [사람들] Dr. Fan Wu 합류
- 2025-12-31 · [수상] 국토부 장관상 수상
- 2025-12-17 · [수상] KAIST Global Research Collaboration
- 2025-12-03 · [수상] 국토교통부 장관상 대상 수상
- 2025-10-22 · [수상] 이준욱, NRF 석사 우수장학금 선정
- 2025-10-12 · [일반] Kaihan, AOTULE 컨퍼런스 2025 참가
- 2025-09-26 · [수상] 임재혁, 박창호 장학금 수상
- 2025-09-24 · [수상] 김창희, KAIST-PTV 인턴십 최우수 선정
- 2025-09-12 · [수상] 홍충교, 최우수 학생상 수상
- 2025-08-25 · [일반] 국내 최초 PTV 공인 트레이너 배출
- 2025-08-25 · [사람들] 신입 석사과정 Truyen Le-Minh 합류
- 2025-06-16 · [일반] NSF IRSC 프로그램, TUPA 방문
- 2025-05-28 · [수상] 2025 수원 ITS AP 포럼 우수논문상
- 2025-05-13 · [일반] TUPA+PTV 그룹 인턴·URP 모집
- 2025-04-28 · [일반] 용산국제업무지구 미래교통포럼
- 2025-04-11 · [수상] 루벤 타마클로, 2025 장영실 펠로우 선정
- 2025-01-17 · [수상] Multimodal Transportation 2024 최우수 논문상
- 2025-01-08 · [수상] TRB 104th 우수논문상 (만점 평가)
- 2024-11-28 · [일반] 2024 ASEAN-ROK 인적자원개발 프로그램
- 2024-11-22 · [일반] ASEAN 교통장관회의 로드맵 발표
- 2024-11-13 · [일반] KAIST 모빌리티연구소 내포 개소
- 2024-11-05 · [일반] 제8차 UN ESCAP 교통위원회 참여
- 2024-10-19 · [논문] ICTCT 2024 논문 6편 발표
- 2024-09-02 · [과제 선정] 박사후연구원 성장형 공동연구 과제 선정
- 2024-09-02 · [과제 선정] 정재은, NRF 박사과정생 연구장려금 선정
- 2024-07-26 · [수상] 박현철, 김영한 글로벌리더 장학생 선정
- 2024-05-09 · [수상] 한국ITS학회 최우수 발표상 2건
- 2024-04-30 · [수상] 권동현, MESH Young Scholar Award 수상
- 2024-04-22 · [일반] TU Berlin–KAIST 세미나
- 2024-04-19 · [수상] 박현철, 우수조교상 수상
- 2024-04-01 · [과제 선정] 박현철, NRF 연구장려금 선정
- 2024-02-02 · [수상] 박현철, 대한교통학회 우수 졸업생 표창
- 2024-01-25 · [일반] 원격제어 기술 협력 MOU 체결
- 2023-12-15 · [일반] 제1회 스타트업 아이디어 콘테스트
- 2023-12-04 · [일반] 딥모빌리티 컨소시엄 출범
- 2023-11-28 · [수상] KAIST Q-Day 교원 특별상 수상
- 2023-10-19 · [수상] 수도권 교통혁신 공모전 수상
- 2023-07-25 · [일반] 2023 모빌리티 서머캠프 (제주)
- 2023-05-29 · [일반] NYU 총장 KAIST 방문
- 2023-05-16 · [일반] 원희룡 국토교통부 장관 KAIST 방문
- 2023-05-10 · [사람들] Fatemeh, UNSW 박사과정 진학
- 2023-05-10 · [사람들] Dr. Chunliang Wu, UWA 교수 임용
- 2023-05-01 · [일반] Prof. Lily Elefteriadou 초청 세미나
- 2023-04-21 · [수상] 한국ITS학회 우수논문상
- 2023-04-09 · [일반] 2023 서울모빌리티쇼 전시
- 2023-02-14 · [사람들] 김인희 교수, KAIST 부임
- 2022-11-16 · [일반] 드론(초경량비행장치) 조종 자격 취득
- 2022-10-08 · [논문] TRB 2023 논문 4편 채택
- 2022-10-04 · [일반] 대한교통학회 40주년 학술대회 & 제10회 국제대중교통포럼
- 2022-10-04 · [논문] ITS 세계총회 2022 (로스앤젤레스) 발표
- 2022-09-30 · [수상] 카카오모빌리티 데이터 경진대회 1위
- 2022-07-20 · [수상] 2022 한국ITS학회 최우수 발표상: Fatemeh
- 2022-07-01 · [수상] 제32회 과학기술우수논문상: 정재은
- 2022-06-23 · [수상] 한국ITS학회 학부 특별세션 대상
- 2022-05-23 · [수상] 대한교통학회 제86회 학술발표회 우수논문 3편
- 2022-04-21 · [수상] 대한교통학회지 2021 최우수논문상: 정재은
- 2022-02-07 · [일반] 2021 데이터 플래그십 과제 '우수' 평가
- 2021-12-09 · [논문] NeurIPS 2021 발표: Bo Wang
- 2021-12-02 · [수상] 2021 추계 교통학회 우수논문상 3편
- 2021-11-29 · [사람들] Dong Xiao 박사과정 중간심사 통과
- 2021-11-12 · [수상] 유예지, 박창호 장학금 수여
- 2021-11-11 · [논문] 제85회 추계 교통학술대회 발표 (제주)
- 2021-11-02 · [수상] 추계 ITS학회 우수논문상: 4학년 박현철
- 2021-10-22 · [논문] 2021 추계 ITS학회 논문 6편 발표
- 2021-10-18 · [일반] YSC 젊은 교통학자들의 TUPA 방문 세미나
- 2021-09-07 · [사람들] Bo Wang 박사 최종심사 통과
- 2021-08-23 · [수상] 해양수산 빅데이터 경진대회 대상·최우수상·우수상 석권
- 2021-07-20 · [과제 선정] 우수신진연구 최초혁신실험실 선정
- 2021-05-26 · [과제 선정] 2021 기초연구실 지원사업 선정
- 2021-05-10 · [사람들] Wenhua 박사 최종 전 심사 통과
- 2021-05-06 · [수상] 2021 춘계 ITS학술대회 우수논문상
- 2021-04-25 · [논문] 2021 춘계 ITS학회 발표 (강릉)
- 2021-04-02 · [사람들] 오태호 progress review
- 2021-02-21 · [과제 선정] 기초연구사업 신진연구자 과제 선정
- 2021-01-06 · [수상] 2020 추계 ITS학회 우수논문상
- 2020-11-24 · [논문] 2020 추계 ITS학회 발표 (제주)
- 2020-11-18 · [일반] 교통신호기 제어장치 특허 출원
- 2020-11-02 · [수상] 2020 추계 교통학회 우수논문상: 3학년 정재은
- 2020-10-22 · [논문] Active Transportation 특별호 편집 참여
- 2020-10-16 · [일반] 한국에서 새 TUPA 출범 (공주대)
- 2020-10-14 · [논문] TRB 2021 논문 채택
- 2020-09-17 · [일반] Monash 6년을 마치며
- 2020-09-16 · [사람들] Monash 겸임교수(Adjunct Senior Lecturer) 위촉
- 2020-08-31 · [사람들] Bo 중간심사 통과
- 2020-07-30 · [사람들] 오태호 (SEU 공동과정) confirmation 통과
- 2020-07-29 · [사람들] Dong confirmation 통과
- 2020-06-24 · [사람들] Lilian progress review 우수 통과
- 2019-10-16 · [논문] 99th TRB 논문 채택
- 2019-09-06 · [사람들] Bo Wang confirmation 통과
- 2019-06-06 · [수상] Tianqi, 최우수 박사연구상 수상 (XJTLU 공동 워크숍)
- 2019-04-16 · [일반] 제1회 지속가능 건설 워크숍
- 2019-03-28 · [수상] Wenhua, 공과대학 국제연구 여행상 수상
- 2019-01-21 · [논문] 98th TRB 연차대회 참가
- 2018-12-21 · [일반] Monash 교통분야 세계 1위 (CWUR)
- 2018-12-11 · [논문] 제24회 HKSTS 국제학술대회 발표
- 2018-11-26 · [사람들] Tianqi Gu 중간심사 통과
- 2018-11-19 · [일반] Ogden 2018 교통 강연: Bart van Arem
- 2018-10-26 · [사람들] Wenhua confirmation 통과
- 2018-10-11 · [사람들] Xinyuan 최종심사 통과
- 2018-10-06 · [논문] TRB 2019 논문 5편 채택
- 2018-09-15 · [일반] 제5회 한중 지속가능교통 공동세미나 (KAIST)
- 2018-09-12 · [일반] 옌청 스마트파킹 포럼 초청 강연
- 2018-08-03 · [일반] ISTS & IWTDCS 2018
- 2018-07-12 · [일반] Monash 특별 강연
- 2018-06-23 · [사람들] 2018 SEU-Monash 공동석사 졸업식
- 2018-03-09 · [일반] Transport Innovation 특별 강연
- 2017-12-01 · [사람들] Tianqi Gu confirmation 통과
- 2017-11-29 · [일반] Clayton-Sunway 공동지도 박사과정 신설
- 2017-11-22 · [사람들] Kai Huang confirmation 통과
- 2017-10-16 · [사람들] 신입 박사과정 Wenhua Jiang 합류
- 2017-10-04 · [논문] TRB 2018 논문 채택
- 2017-09-08 · [사람들] Xiaoying(Shelley) Cao 박사학위 수여
- 2017-07-09 · [논문] CICTP 2017 (상하이) 참가
- 2017-06-25 · [사람들] 2014 코호트 Monash 졸업
- 2017-06-23 · [일반] CCDI 특별 초청 강연
- 2017-06-07 · [일반] 쑤저우 공유자전거 프로그램 개막 연설
- 2017-04-28 · [일반] 2017 Monash 쑤저우 공개 강연
- 2017-04-27 · [일반] ITS 소장 Rose 교수·Vu 교수 쑤저우 방문
- 2017-04-25 · [일반] 우시 로드레이지 과제 성공적 완료
- 2017-04-21 · [일반] 쑤저우 파트너 기관 협력 미팅
- 2017-04-17 · [일반] Prof. S.C. Wong 아주대 방문 강연
- 2017-03-26 · [일반] CCDI Tao Liu 특별 강연
- 2017-03-23 · [일반] 쑤저우산업원구(SIP) 전시센터 견학
- 2017-02-13 · [논문] CICTP 2017 다수 논문 채택
- 2016-11-09 · [과제 선정] JITRI 연구과제 수주 (400만 위안)
- 2016-10-18 · [일반] ITS China, Monash 방문
- 2016-09-01 · [사람들] Wentao Jing 중간심사 통과
- 2016-08-15 · [사람들] Shelley 최종 전 심사 통과
- 2016-07-20 · [사람들] 쑤저우 구쑤구 공안 교통 전문가 위촉
- 2016-07-19 · [일반] 초청 강연: 이선하 교수·Yuanqiu Bao
- 2016-07-19 · [일반] 제1회 SEU-Monash 워크숍
- 2016-07-12 · [일반] ISTS & IWTDCS 2016 (제주)
- 2016-07-04 · [일반] 2016 쑤저우 홍수와 교통 영향
- 2016-07-04 · [사람들] 첫 쑤저우 기반 박사 Xinyuan confirmation
- 2016-06-28 · [일반] Graham Currie 교수 쑤저우 공개 강연
- 2016-06-22 · [수상] 장쑤성 최우수 교육과정상 (2014 코호트)
- 2016-06-07 · [일반] 쑤저우 캠퍼스 연구석사 과정 도입
- 2016-06-07 · [일반] Jeff 교수·Barry, 쑤저우 방문
- 2016-05-19 · [일반] Monash 토목공학과장 쑤저우 방문
- 2016-05-19 · [과제 선정] 우시 안전보안연구소 과제 수주

## 연락과 위치

- 교수 이메일: inhi.kim@kaist.ac.kr, 교내 전화 1760[^mo]
- 위치: KAIST 문지캠퍼스 F동 433호 (대전 유성구 문지로 193)[^contact][^mo]

[^home]: TUPA 누리집 첫 화면 <https://www.inhi.kim/> (2026-10-19 열람)
[^research]: TUPA 연구 페이지 <https://www.inhi.kim/research> (2026-10-19 열람)
[^people]: TUPA 구성원 페이지 <https://www.inhi.kim/people> (2026-10-19 열람)
[^papers]: TUPA 논문 목록(저널·특허·학술대회·단행본) <https://www.inhi.kim/publications> (2026-10-19 열람)
[^projects]: TUPA 과제 페이지 <https://www.inhi.kim/projects> (2026-10-19 열람)
[^news]: TUPA 소식 게시판 <https://www.inhi.kim/news> (2026-10-19 열람)
[^contact]: TUPA 연락처 <https://www.inhi.kim/contact> (2026-10-19 열람)
[^mo]: KAIST 조천식모빌리티대학원 교수 소개(김인희) <https://mo.kaist.ac.kr/professor/%EA%B9%80%EC%9D%B8%ED%9D%AC/> (2026-10-19 열람)
[^p1]: S. Ye 외, I. Kim, Accident Analysis & Prevention 221, 108208 (2025). <https://doi.org/10.1016/j.aap.2025.108208> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: H. Park, T. Oh, J. Lim, I. Kim, Transportation Research Part F: Traffic Psychology and Behaviour 117, 103482 (2026). <https://doi.org/10.1016/j.trf.2025.103482> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p3]: H. Park, T. Oh, I. Kim, Accident Analysis & Prevention 205, 107685 (2024). <https://doi.org/10.1016/j.aap.2024.107685> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: Y. Liu, Q. Li, I. Kim, Communications in Transportation Research 5, 100200 (2025). <https://doi.org/10.1016/j.commtr.2025.100200> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p5]: D. Kwon, C. Lee, H. Kang, I. Kim, Transportation Research Record: Journal of the Transportation Research Board 2677, 30-42 (온라인 2023-03-28). <https://doi.org/10.1177/03611981231158324> 초록 기준.
[^p6]: K. Zhang 외, I. Kim, Transportation Research Part D: Transport and Environment 145, 104806 (2025). <https://doi.org/10.1016/j.trd.2025.104806> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p7]: T. Lin, Z. Jin, H. Yeo, I. Kim, IEEE Transactions on Intelligent Transportation Systems 27, 4300-4314 (2026). <https://doi.org/10.1109/tits.2026.3661062> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: R. Tamakloe, K. Zhang, I. Kim, Accident Analysis & Prevention 205, 107676 (2024). <https://doi.org/10.1016/j.aap.2024.107676> 초록 기준(Semantic Scholar 등록 초록).

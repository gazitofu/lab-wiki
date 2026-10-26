# 우주선원형개발연구실 (Spacecraft Prototyping Laboratory, SPL)

**KAIST 항공우주공학과 · 윤효상 교수**

- 분야: 우주 광통신(위성 레이저 통신과 광학 지상국), 별 추적기·태양 센서 같은 위성 자세 결정 센서, 위성 자세 결정·제어와 궤도 운용, 초저고도 위성, 큐브위성용 위성항법 전파엄폐 수신기
- 대분야: 기계·로봇·제조, 전기전자·반도체·광학
- 태그: 광통신[^research][^p3][^p4], 제어 이론·제어 공학[^aelab][^p4], 위성 원격탐사[^research], 유도·항법·제어(GNC)[^aelab], 위성항법(GNSS)[^research], 상태 추정·필터링(데이터 동화)[^p1]
- 홈페이지: <https://spacecraft.kaist.ac.kr/>
- 근거와 출처: [우주선원형개발연구실 근거 페이지](spacecraft-sources.md)

> 레이저로 위성과 지상, 위성과 위성을 잇는 우주 광통신, 위성이 자기 방향을 재는 별 추적기와 태양 센서, 위성의 자세 결정·제어와 궤도 운용을 연구하는 항공우주공학과 연구실이다.[^aelab][^research] 연구실은 망원경을 갖춘 광학 지상국을 직접 만들어 운용한다.[^aelab][^research]

## 무엇을 연구하나

연구실은 KAIST 항공우주공학과 윤효상 교수의 연구실이다. 학과 연구실 소개(2021-08-16 게시)에 따르면 연구실은 미래 우주 비행체 기술과 관련된 연구를 하며, 그 가운데 차세대 통신 기법인 우주 광통신(Free Space Laser Communication), 위성의 자세 측정에 필요한 센서인 별 추적기, 위성 궤도 유도·항법·제어(Satellite Orbit Guidance, Navigation, and Control) 연구에 집중한다.[^aelab] 같은 소개는 연구실이 추정 이론과 위성 자세 결정·제어 분야에서 논문을 발표해 왔고, 천문 관측용 광학 지상국을 직접 구축·운용하며 천체와 위성 자료를 모아 분석해 연구에 쓴다고 적는다.[^aelab] 학과 교수진 목록은 교수의 연구분야를 Spacecraft Systems, Laser Communications, Star Trackers로 적는다.[^aefac]

누리집 Research 페이지는 날짜 없이 여섯 가지 연구 주제를 소개한다. 레이저 통신을 위한 광학 지상국 개발, 위성 간 광학 통신 시스템 개발, 별 추적기(star tracker, 별 사진으로 위성이 향한 방향을 알아내는 센서)의 모듈화, 디지털 태양 센서(sun sensor, 태양이 있는 방향을 재어 위성의 자세를 정하는 센서) 개발, 초저고도(VLEO, Very Low Earth Orbit) 인공위성 기술 개발, 큐브위성 탑재용 위성항법시스템 전파엄폐 소프트웨어 정의 라디오 개발이다.[^research] 학과 연구실 소개는 연구실이 정부출연연구소와 여러 대학과 협업하며 과제를 수행한다고 적고, 누리집 소식은 2022년 11월 미래도전 과제 「초저고도 광학 인공위성 설계 및 핵심기술 개발」이 단계전환평가를 통과했다고 알린다.[^aelab][^notice]

## 주요 연구 주제

### 1. 별 추적기와 위성 자세 결정

Research 페이지에 따르면 우주선에 실리는 별 추적기는 데이터로 정리된 수많은 별의 위치를 바탕으로 우주선의 자세를 결정한다.[^research] 연구실은 별 추적기의 모듈화에서 범용성, 소형화, 병렬성, 저비용을 주안점으로 들고, 태양 센서는 가볍고 정확하며 시야각(FOV, Field of View)이 넓게 만드는 것을 목표로 한다.[^research] 누리집 소식에 따르면 2021년 1월 연구실의 초소형 별 추적기가 완성됐다.[^notice] 대표 논문 1은 별 영상만으로 별 추적기의 변수와 자세를 한꺼번에 추정해 보정하는 방법이고, 대표 논문 2는 별 추적기의 광학 변수 오차가 자세 출력에 남기는 오차를 유색 잡음(colored noise, 시간에 따라 값끼리 서로 연관된 잡음)으로 모형화해 칼만 필터(Kalman filter, 잡음 섞인 측정값으로 시스템 상태를 차례로 추정하는 계산 방법)로 함께 추정하는 방법이다.[^p1][^p2] 2021–2026년 논문 목록에는 지구 자전을 이용한 큐브위성 별 추적기 보정(2022), 레이저로 만든 그래핀 회절 광학 소자(2023), 빠르게 도는 환경에서 별 추적기 영상의 롤링 셔터 왜곡을 딥러닝으로 보정하는 연구(2025), 회절 렌즈 배열을 단 태양 센서 시제품(2024)도 있다.[^pubs]

위성 자세를 바꾸는 구동 장치도 다룬다. 2021–2026년 논문 목록에는 임의로 배치한 반작용 휠 묶음이 낼 수 있는 최대 토크와 각운동량 범위를 구하는 연구(2021)와 그 최대 토크를 빨리 계산하는 알고리즘(2024), 소형 위성용 제어 모멘트 자이로(control moment gyroscope, 회전하는 바퀴의 회전축 방향을 바꿔 위성을 돌리는 힘을 내는 구동 장치)의 개발 현황·토크 측정·시험대 개발(2023, 2024)이 있다.[^pubs]

### 2. 위성 레이저 통신의 지향·포착·추적

Research 페이지는 레이저 통신이 지상과 위성 사이에서 송신단과 수신단이 서로를 정확히 향해야 하므로 지상에서 위성을 정확히 추적할 수 있어야 한다고 설명하고, 연구실이 지름 30 cm 망원경을 쓰는 광학 지상국을 개발하고 있다고 적는다.[^research] 누리집 소식에 따르면 연구실은 2020년 11월 지상국의 별 찾기 알고리즘과 자동 추적 시스템으로 국제우주정거장을 추적·관측했고, 같은 해 12월 레이저 통신 지상국이 될 천문관측돔을 유레카관(N27) 옥상에 설치했다.[^notice] 위성 간 광학 통신에 대해서는 레이저 통신 장치를 실은 소형 인공위성을 개발하는 것이 목표이며, 위성이 레이저 신호를 정확히 보내려면 위성의 자세와 진동을 정밀하게 제어해야 한다고 적는다.[^research] 대표 논문 3은 위성 간 광 링크를 처음 잇는 포착(acquisition) 단계에서 상대 위성이 있을 수 있는 영역을 훑는 스캔 패턴이고, 대표 논문 4는 위성의 미세 진동이 레이저 지향을 흔드는 것을 다중 속도 적응 제어로 줄이는 방법이다.[^p3][^p4] 2021–2026년 논문 목록에는 초소형 위성 레이저 통신 시스템의 지향 오차를 해석적으로 평가한 연구(2024)와 디지털 필터 설계(2025)도 있다.[^pubs]

### 3. 저궤도·초저고도 위성의 궤도 운용

Research 페이지는 위성의 비행 고도가 낮을수록 지구 대기의 영향으로 에너지가 빠르게 줄어 수명이 짧아지지만 땅에 가까이 날아 해상도 높은 영상을 찍을 수 있다고 설명한다.[^research] 초저고도 위성 설계에는 통신과 자세 제어 같은 하위 시스템 외에 임무 설계, 저고도 우주 환경 해석, 구조 모델 환경 시험, 임무 시뮬레이션을 아우르는 시스템 공학이 필요하다고 적는다.[^research] 누리집 소식에 따르면 연구실은 2021년 1월 국방과학연구소가 주관하는 미래도전기술개발사업 과제에 착수했고, 이 과제는 KAIST, 세종대학교, 한국천문연구원, (주)세트렉아이의 합동 연구로 국내 위성 임무 가운데 가장 낮은 고도의 위성 임무를 설계한다고 적었다.[^notice] 대표 논문 5는 공기 저항 차이를 이용해 저궤도 군집 위성의 궤도상 간격을 맞추는 동안 배터리 전력이 부족해지지 않도록 위성 자세를 정하는 전략이다.[^p5]

### 4. 큐브위성용 위성항법 전파엄폐 수신기

Research 페이지에 따르면 저궤도 위성에 실린 위성항법시스템 전파엄폐(GNSS RO, Global Navigation Satellite System Radio Occultation) 수신기는 지구 가장자리 너머로 뜨거나 지는 위성항법 위성의 신호를 받아 지구 대기를 관측한다.[^research] 낮은 고도각에서 오는 신호가 약해 높은 수준의 안테나·수신기 기술이 필요하고, 습한 대류권을 지나는 신호를 받으려면 여러 도플러 모형에 기반한 개방 루프 추적(open-loop tracking)이 필요하다고 적는다.[^research] 연구실은 대기 변수를 높은 정확도로 산출하려고 소프트웨어 정의 라디오(software-defined radio, 신호 처리 기능을 하드웨어 대신 소프트웨어로 구현한 무선 수신기)를 개발하고 야외 실험으로 성능을 검증한다.[^research] 대표 논문 6은 연구실 졸업생이 1저자인 공동 연구로, 항공 무선 장비의 펄스 간섭에 대응해 받은 신호 표본을 0으로 만드는 블랭킹이 위성항법 L5/E5a 코드의 상관 특성에 주는 영향을 분석했다.[^p6]

## 대표 논문

교수는 2019년부터 KAIST에 있다. 누리집 Publication 목록의 2021–2026년 국제 학술지 논문 가운데 초록을 확인할 수 있는 여섯 편을 네 연구 갈래에 나눠 골랐다. 누리집 목록은 교신저자를 표시하지 않아 저자 칸에는 저자 순서만 적었다. 대표 논문 6은 교수가 여덟 명 가운데 넷째 저자인 공동 연구다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2022 | [Star Tracker Geometric Calibration Through Full-State Estimation Including Attitude](https://doi.org/10.1007/s42405-021-00432-5) · International Journal of Aeronautical and Space Sciences | 별 영상만으로 별 추적기를 보정하는 방법이다. 앞선 연구와 달리 모든 변수와 자세를 하나의 최소제곱 문제로 한꺼번에 추정해 최적으로 보정하며, 이 계산은 차례로 갱신하는 재귀 추정 형태로 쉽게 바꿀 수 있다. 보정 결과로 자세 결정에 쓸 별 추적기의 전체 성능을 추정하는 방법도 내놓았다. 별 영상만 쓰므로 궤도 위와 지상의 보정 모두에 쓸 수 있다. 시뮬레이션에서 보정 성능이 이전 보정 방법보다 약 4배 나아졌고, 실제 별 영상으로 보정 실험도 했다. | 1저자 윤효상, 마지막 저자 J. Wi (3명) |
| 2 | 2023 | [Modeling and Filtering Colored Noise of a Star Tracker](https://doi.org/10.1007/s40295-023-00376-w) · The Journal of the Astronautical Sciences | 별 추적기의 광학계 오차에서 생기는 자세 오차 모형을 세우고, 이 오차를 고려하는 자세 칼만 필터를 제안했다. 발사 전후에 보정해도 오차가 없는 변수를 실제로 얻을 수는 없어 출력에 백색이 아닌 잡음 오차가 생기고, 오차 모형은 제조사의 영업 비밀이어서 위성에서 바로 추정하기 어렵다. 광학 변수 오차로 생기는 자세 편향을 카메라 모델 변수와 그 공분산으로 유색 잡음으로 모형화하고, 벡터 자기회귀 모형으로 재귀 형태를 유도했다. 유색 잡음 칼만 필터는 이 자세 오차를 위성 자세, 자이로 편향과 함께 추정한다. 더 추정할 상태는 셋뿐이고 제조사의 민감한 정보가 들어가지 않는다. 시뮬레이션으로 알고리즘의 안정성과 신뢰성을 보였다. | 1저자 J. Wi, 마지막 저자 윤효상 (3명) |
| 3 | 2025 | [Satellite Scanning Pattern for Optical Acquisition Considering Elliptical Shaped Field of Uncertainty](https://doi.org/10.1109/taes.2025.3526107) · IEEE Transactions on Aerospace and Electronic Systems | 위성 위치 오차의 분포를 바탕으로 위성 간 광 링크의 포착 시간을 줄이는 스캔 방법이다. 위치 오차를 방향마다 퍼짐이 다른 다변수 가우스 분포로 모형화하고, 그 분포의 5시그마 영역을 불확실 영역(FOU)으로 정했다. 진행 방향 오차가 커서 FOU는 흔히 타원 모양이 되며, 이 타원 영역을 효율적으로 훑는 스캔 패턴을 제안했다. 몬테카를로 시뮬레이션과 NEXTSat-2의 GPS 자료 분석으로 검증했고, FOU가 더 타원에 가까울 때 기존 방법보다 효과적이었다. NEXTSat-2에서는 단축과 장축의 비가 0.2 미만인 경우가 70%였고, 제안한 방법의 효율이 확인됐다. | 1저자 J. Yun, 마지막 저자 윤효상 (3명) |
| 4 | 2025 | [Simple Multirate Adaptive Control on Spacecraft Jitter Rejection for the FSO Pointing System](https://doi.org/10.1109/taes.2025.3601111) · IEEE Transactions on Aerospace and Electronic Systems | 위성의 자유공간 광(FSO) 통신은 정밀한 지향이 필요한데, 위성 플랫폼의 기계적 미세 진동이 지향을 떨어뜨린다. 지향 장치의 구동기인 고속 조향 거울은 과도 운동의 속도가 일정하지 않아 효과가 제한된다. 이 연구는 더 빠른 센서 속도로 과도 거동을 잡는 다중 속도 적응 알고리즘을 제안하고, 다중 속도 구조를 담은 오차 함수의 기울기 갱신식을 유도해 수렴과 안정 조건을 따졌다. 시뮬레이션에서 복합 정현파 외란에 대해 단일 속도 방법보다 효과적이었고, 광학 시험대 실험 자료도 시뮬레이션과 일치했다. | 1저자 K. Baeck, 마지막 저자 윤효상 (3명) |
| 5 | 2025 | [A Pitch-Roll Attitude Strategy for LEO Constellation Phasing with Differential Drag Under Power Constraints](https://doi.org/10.1007/s42405-025-01071-w) · International Journal of Aeronautical and Space Sciences | 차등 항력은 추진제 없이 저궤도 군집 위성의 위상(군집 안 위성들의 궤도상 간격)을 맞추는 기법이다. 최대·최소 항력 사이를 오가는 기존 방법은 전력 불안정을 일으켜 배터리 충전 모드에 들어가게 하고 위상 조정을 끊는다. 이 연구는 공기 저항과 발전량을 함께 높이는 피치·롤 자세 전략을 내놓았다. 실시간 태양 방향을 바탕으로 한 목적 함수를 최대화해 자세를 정한다. 대표적인 저궤도 군집 모델 두 가지로 시뮬레이션한 결과 배터리 충전 상태를 70% 문턱 위로 유지해 잦은 충전 모드 진입을 피했고, 위상 조정 시간과 총 고도 손실이 줄었다. | 1저자 S. Kim, 마지막 저자 윤효상 (2명) |
| 6 | 2025 | [GNSS L5/E5a Code Properties in the Presence of a Blanker](https://doi.org/10.33012/navi.700) · NAVIGATION: Journal of the Institute of Navigation | 위성항법 L5/E5a 코드는 기존 GPS L1 C/A 코드보다 상관 특성이 좋지만, 거리 측정 장비와 전술 항법 장치의 펄스 같은 고유한 간섭 환경에 놓인다. 민간 항공은 대책으로 시간 블랭킹, 곧 받은 신호의 세기가 문턱을 넘으면 표본을 0으로 만드는 방법을 가정한다. 이 연구는 시뮬레이션으로 1 ms 적분 시간에서 블랭킹 듀티 사이클 0%–75%일 때의 코드 특성을 분석했다. 자기 상관과 상호 상관의 보호는 줄었지만 듀티 사이클 약 60%까지는 L1 C/A 코드보다 나았고, 75%까지 늘면 이 장점이 줄었다. 도플러 잔차가 상관 특성에 주는 영향은 작았다. | 1저자 S. Kim, 넷째 저자 윤효상, 마지막 저자 D. M. Akos (8명) |

## 교수와 전문 분야

윤효상 교수(Yoon, Hyosang)는 KAIST 항공우주공학과 부교수다. 누리집 People 페이지에 따르면 KAIST에서 항공우주공학 학사(2008)와 석사(2010)를 받았고, 석사 논문은 Star Recognition Algorithm in Dynamic Environment이다. 2017년 MIT 항공우주공학(Aeronautics and Astronautics) 박사를 받았고, 박사 논문은 Pointing and Tracking System Analysis and Design for Optical Intersatellite Communication Link이다.[^people] 2008–2014년 Satrec Initiative AOCS 팀 연구원(Associate Research Engineer), 2017–2019년 Planet Labs GNC 엔지니어를 거쳐, 2019–2025년 KAIST 항공우주공학과 조교수, 2025년부터 부교수다.[^people] 누리집 소식은 2025년 9월 부교수 승진을 알린다.[^notice] 학과 교수진 목록은 직위를 Associate Professor로, 학력을 B.S. KAIST('08), M.S. KAIST('10), Ph.D. MIT('17)로 적는다.[^aefac]

People 페이지의 연구 경력에 따르면 교수는 Satrec Initiative에서 DubaiSat-2와 Deimos-2의 자세 결정·제어와 시스템 공학, GPS를 이용한 위성 궤도 결정을 맡았다. MIT STAR Lab에서는 NODE(Nanosatellite Optical Downlink Experiment) 프로젝트의 지상국 개발과 FLARE(Free-space LaserCom. and Radiation Experiment) 프로젝트의 자세 결정·제어, NASA 지원 큐브위성 시제품 프로젝트에 참여했고, Planet Labs에서는 GNC, 별 추적기, 자세 보정, SkySat LEOP와 SkySat 추력기 운용을 맡았다.[^people] 연구 주제와 논문으로 보면 전문 분야는 별 추적기와 태양 센서 같은 위성 자세 센서의 설계·보정, 추정 이론에 기반한 위성 자세 결정과 제어, 위성 레이저 통신의 지향·포착·추적이다.[^aefac][^research][^pubs]

## 응용 분야

Research 페이지는 레이저 통신을 큰 안테나가 필요한 전파 통신과 거리가 멀어질수록 떨어지는 위성 간 통신 속도 문제의 해법으로, 초저고도 위성을 해상도 높은 영상 촬영 수단으로, 전파엄폐 수신기를 지구 대기 관측 수단으로 소개한다.[^research] 누리집 소식은 2021년 1월 국방과학연구소가 주관하는 미래도전기술개발사업 과제 착수와 2022년 11월 미래도전 과제 「초저고도 광학 인공위성 설계 및 핵심기술 개발」의 단계전환평가 통과를 알린다.[^notice] 2025년 국내 학회 발표 목록에는 한국군사과학기술학회에서 발표한 위성 간 광통신 링크 포착 연구도 있다.[^pubs]

## 구성원

누리집 People 페이지의 박사과정 9명(석박사 통합과정 1명 포함), 석사과정 7명, 연구원(Contract Researcher) 1명, 모두 17명이다. 「시작」은 각 카드에 현재 과정이 시작됐다고 적힌 연도와 달이고, 「연구 주제」는 카드의 Research Topic 칸이다. Research Topic이 TBD로 적힌 카드는 연구 주제 칸을 비웠다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| 파울로 (Paulo Kemper) | 박사과정 | 2021.9 | CubeSat navigation systems, Star Tracking algorithms |  |
| 위준성 (Wi, Junsung) | 박사과정 | 2022.3 | Satellite Attitude Determination, Deorbit Satellite Guidance & Control | 1, 2 |
| 박용준 (Park, Yongjun) | 박사과정 | 2022.9 | Satellite Attitude Determination, Satellite Optimum Navigation |  |
| 한효근 (Han, Hyogeun) | 박사과정 | 2023.3 | Attitude Determination Sensor Calibration, Sun Sensor with Diffraction Optics |  |
| 윤정인 (Yun, Jeongin) | 석박사통합과정 | 2021.3 | Space Manipulator Control, Inter-satellite Laser Link Simulation | 3, 4 |
| 김형철 (Kim, Hyeongcheol) | 박사과정 | 2024.03 | Control Moment Gyroscope |  |
| 최상헌 (Choi, Sangheon) | 박사과정 | 2025.2 | Orbit Determination, Space Situational Awareness |  |
| 장재훈 (Jang, Jaehun) | 박사과정 | 2025.9 | Magnetometer Calibration |  |
| 문동민 (Moon, Dongmin) | 박사과정 | 2026.02 | Attitude Determination and Control System, Sensor Calibration Algorithm |  |
| 박정호 (Park, Jeongho) | 석사과정 | 2025.03 | VLEO Satellite Adaptive Attitude Control, Satellite Attitude Determination |  |
| 김형준 (Kim, Hyungjun) | 석사과정 | 2025.03 | Inter-satellite communication |  |
| 김성열 | 석사과정 | 2025.03 |  |  |
| 배형준 (Bae, Hyungjun) | 석사과정 | 2026.03 |  |  |
| 신정욱 (Shin, Jungwook) | 석사과정 | 2026.03 |  |  |
| Bryce Moran | 석사과정 | 2026.08 |  |  |
| 이상훈 (Sanghun Lee) | 석사과정 (Space Exploration Engineering Program) | 2026.09 |  |  |
| 오유나 (Oh, Yuna) | 연구원 | 2025.3 | Spacecraft Robust Attitude Control |  |

## 졸업생과 이전 구성원

누리집 People 페이지 Alumni 구역의 박사(Ph.D.) 2명과 석사(Master) 3명, 모두 5명이다. 진로는 카드에 현재 소속으로 적힌 곳이고, 학위 논문은 석사 졸업생 카드에 적힌 석사 논문 제목이다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| 백기욱 (Baeck, Kiwook) | Ph.D. (2026) | ETRI |  |
| 김시현 (Kim, Sihyun) | Ph.D. (2026) |  |  |
| 이윤후 (Lee, Yoonhoo) | M.S. (2024) | Flight Control Software Engineer, Satrec Initiative, Daejeon, Korea | Robust 𝐻∞ sub-optimal controller design for satellite attitude control under actuator saturation and uncertainties |
| 김승환 (Kim, Seunghwan) | M.S. | M.S. Student, CU Boulder, Boulder, CO | Development of a GNSS radio occultation software-defined receiver prototype for cubesats |
| 안정우 (Ahn, Jeongwoo) | M.S. (2026) | LIG Nex1 |  |

## 최근 논문 목록 (2021–2026)

누리집 Publication 페이지에서 연도가 2021–2026년인 항목 49건이다. 국제 학술지 논문 12편, 국제 학술대회 논문 6편, 국내 학술지 논문 2편, 국내 학술대회 논문 29편이고, 연도별로 2025년 14, 2024년 17, 2023년 10, 2022년 5, 2021년 3건이다. 누리집 목록은 2026년 2월 19일에 마지막으로 고쳐졌다. 이 목록은 윤효상 교수의 논문 목록이어서 다른 기관 연구진이 이끈 공동 연구도 들어 있다. 교수는 2019년부터 KAIST에 있어, 이 기간의 항목은 모두 교수의 KAIST 재직 시기에 나왔다. 각 줄은 누리집 표기를 그대로 옮겼다.[^pubs]

**2025**

- Sihyun Kim, Hyosang Yoon, “A Pitch-Roll Attitude Strategy for LEO Constellation Phasing with Differential Drag Under Power Constraints”, International Journal of Aeronautical and Space Sciences, October 2025
- Kiwook Baeck, Hyosang Yoon, "Meta-heuristic-based design of high-order stable digital filters using pole-zero placement", Signal Processing, Vol. 239, September 2025
- Kiwook Baeck, Jeongin Yun, Hyosang Yoon, "Simple Multirate Adaptive Control on Spacecraft Jitter Rejection for the FSO Pointing System", IEEE Transactions on Aerospace and Electronic Systems, Vol. 61, August 2025.
- Seunghwan Kim, Nicolas Gault, Yongrae Jo, Hyosang Yoon, Byungwoon Park, Axel Garcia-Pena, Christophe Macabiau, and Dennis M. Akos, “GNSS L5/E5a Code Properties in the Presence of a Blanker”, NAVIGATION: Journal of the Institute of Navigation, Vol. 72, Issue 2, June 2025
- Jeongin Yun, Kiwook Baeck, Hyosang Yoon, "Satellite Scanning Pattern for Optical Acquisition Considering Elliptical Shaped Field of Uncertainty," IEEE Transactions on Aerospace and Electronic Systems, Vol. 61, June 2025.
- Yongjoon Park, Dongmin Moon, Hyosang Yoon, “DEEP LEARNING-ENHANCED ROLLING SHUTTER CORRECTION FOR STAR TRACKERS IN HIGH ANGULAR VELOCITY ENVIRONMENTS”, 76th International Astronautical Congress 2025, Sydney, Australia, September 2025
- 최상헌, 한효근, 윤정인, 최우진, 윤효상, "각도 기반 상대 궤도결정의 한계와 PAT 탐색영역 축소", 2025 한국군사과학기술학회 추계학술대회, 2025.
- 김형준, 윤정인, 장재훈, 최우진, 윤효상, "비콘리스 광통신 링크 획득을 위한 타원형 FOU 스캐닝 기법", 2025 한국군사과학기술학회 추계학술대회, 2025.
- 윤정인, 김형준, 한효근, 최상헌, 윤효상, 최우진, "위성 간 광통신 획득 검증을 위한 시뮬레이터 개발," 2025 한국군사과학기술학회 추계학술대회, 2025.
- 박정호, 박용준, 문동민, 윤효상, 신구환, 이대희, 이재진, 박수종, 김건희, 황인영, 나경수, "cFS 기반 큐브위성 탑재 소프트웨어의 PIL 시뮬레이션 개발", 한국항공우주학회 2025년도 추계학술대회, 2025.
- 윤정인, 윤효상, 신구환, 이대희, 이재진, 박수종, 김건희, 황인영, 나경수, "큐브위성 자세제어계 개발 및 검증 현황,“ 한국항공우주학회 2025년도 추계학술대회, 2025.
- 백기욱, 윤효상, "자유공간 광통신 빔 조향 시스템의 이해", 2025년도 한국통신학회 하계종합학술발표회, 2025.
- 문동민, 장재훈, 박용준, 윤정인, 윤효상, "확장 칼만 필터 기반 자이로 센서 및 별 추적기 정렬 오차 보정 지상 실험", 한국항공우주학회 2025 춘계학술대회, 2025.
- 안정우, 윤효상, "별추적기 식별 알고리즘의 CNN 기반 별 패턴 분류 및 시뮬레이션", 한국항공우주학회 2025년도 춘계학술대회, 2025.

**2024**

- Dongwook Yang, Younggeun Lee, Hyeokin Kang, Quang Huy Vu, Guseon Kang, Seung Eon Lee, Hyogeun Han, Seunghwan Kim, Han Ku Nam, Soongeun Kwon, Hyug-Gyo Rhee, Joohyung Lee, Hongki Yoo, Hyosang Yoon, Young-Jin Kim, “Green Manufacturing of Electrically-Tunable Smart Light-Weight Planar Optics: A Review." International Journal of Precision Engineering and Manufacturing-Green Technology, vol. 11, page 1029-1051, May 2024.
- Baeck, K., Wi, J., Yoon, H., "Analytic pointing error evaluation on nano-satellite laser communication system," Optics Comunications 559 (2024), 130419
- Park, Y., Baeck, K., Yoon, H., "A Novel Fast Algorithm for Maximum Torque of General Reaction-Wheel Array", 2024 AIAA SciTech Forum, Orlando.
- Yoon, H., Kim, H., Yun, J., Yoon, H., "Momentum Management of Reaction Wheels for an Asymmetric Geostationary Satellite: with GK-2A Flight Data Analysis", 2024 AIAA SciTech Forum, Orlando.
- Kemper, P., Han, H., Yoon, H., "Cost-effective Platform for Validating Optical Autonomous Navigation Systems and Algorithms on Earth", 2024 AIAA SciTech Forum, Orlando.
- Kemper, P., Marin, M., Yoon, H., "Using Star Density Tessellation to Evaluate the Impact of a Star Tracker’s Field of View Shape on its Performance", 2024 AIAA SciTech Forum, Orlando.
- Goo-Hwan Shin, Hyosang Yoon, Hyeongcheol Kim, Dong-Soo Choi, Jae-Suk Lee, Yeong-Ho Shin, Eunji Lee, Sang-sub Park, Seokju Kang, "Control Moment Gyroscope Torque Measurements Using a Kistler Table for Microsatellite Applications", 우주기술과 응용 (Journal of Space Technology and Applications), vol.4, no.1, pp.12-26, 2024.
- 김승환, 한효근, 이영근, 윤효상, 김영진, “초박형 회절렌즈 어레이를 이용한 인공위성 태양 센서 프로토타입 개발,” 한국정밀공학회 2024년도 추계학술대회, 2024.
- 위준성, 윤효상, "차분 항력을 이용한 궤도이탈 유도제어", 한국국방우주학회 2024년 추계학술대회, 2024.
- 김승환, 한효근, 박용준, 문동민, 김예지,윤효상, “위성항법시스템 전파엄폐 지상 실험을 위한 테스트베드 개발,” 한국항공우주학회 2024년도 추계학술대회, 2024.
- 장재훈, 윤효상, "L4 탐사선의 자유공간 광통신을 위한 요구조건 분석", 한국항공우주공학회 2024년도 우주학술대회, 2024.
- 윤정인, 오유나, 윤효상, "추력기의 영공간을 이용한 오프-모듈레이션 명령 생성", 한국항공우주공학회 2024년도 우주학술대회, 2024.
- 김형철, 신구환, 윤효상, 최동수, 이제석, 신영호, 이은지, 강석주, "소형위성용 제어모멘트자이로 테스트베드의 자세제어 시험기능 구현현황", 한국항공우주공학회 2024년도 우주학술대회, 2024.
- 백기욱, 윤효상, “적응형 피드백 필터를 적용한 위성 레이저 통신 신호 추적 제어기,” 제 34회 통신정보 합동 학술대회, 2024.
- 오유나, 윤효상, "태양전지판을 고려한 정지궤도 위성의 유연구조물 동역학 모델링 및 자세제어", 한국항공우주공학회 2024년도 춘계학술대회, 2024.
- 장재훈, 윤효상, 김영진, 김신형, 김재윤, 김태원, 백기욱, 이동일, 노정훈, 신승우, "소형 위성간 통신 선행기술 및 요구조건 분석", 한국항공우주공학회 2024년도 춘계학술대회, 2024.
- 김형철, 신구환, 윤효상, 최동수, 이재석, 신영호, 이은지, 강석주, "소형 위성의 신속 자세 제어를 위한 제어모멘트자이로의 테스트베드 개발현황", 한국항공우주공학회 2024년도 춘계학술대회, 2024.

**2023**

- Lee, Y., Low, M., Yang, D., Nam, H., Le, TSD., Lee, S., Han, H., Kim, S., Vu, Q., Yoo, H., Yoon, H., Lee, J., Sandeep, CSS., Lee, K., Kim, S., Kim, Y., "Ultra-thin light-weight laser-induced graphene (LIG) diffractive optics", Light: Science & Applications (2023)12:146
- Wi, J., Baeck, K., Yoon, H., "Modeling and Filtering Colored Noise of a Star Tracker", The Journal of the Astronautical Sciences 70, 8 (2023)
- Shin, G., Yoon, H., Kim, H., Choi, D., Lee, J., Shin, Y., Lee, E., "Highly Agile Actuator Development Status of an 800 mNm Control Moment Gyro (CMG)", 우주기술과 응용 (Journal of Space Technology and Applications), 2023.
- 박용준, 위준성, 한효근, 백기욱, 윤효상, “초저고도 광학 인공위성 실시간 임무 시뮬레이터 개발”, 한국항공우주학회 2023년도 우주학술대회, 2023.
- 한효근, 위준성, 박용준, 윤효상, "초저고도 섭동을 모사한 환경에서의 궤도 전파 및 고도 유지 시뮬레이션," 한국항공우주학회 2023년도 우주학술대회, 2023.
- 장재훈, 백기욱, 박용준, 윤효상, "이종 위성 간 레이저 통신 개념 설계 및 요구조건 분석", 한국항공우주학회 2023년도 우주학술대회, 2023.
- 위준성, 박용준, 한효근, 백기욱, 윤효상, "초저고도 광학 인공위성 체계 개발 현황", 한국항공우주학회 2023년도 우주학술대회, 2023.
- 백기욱, Paulo Kemper, 윤효상, “하향링크를 위한 위성 레이저 통신 탑재체 EM 개발”, 제30회 광전자 및 광통신 학술대회, 2023.
- 한효근, 이영근, 김승환, 양동욱, 윤효상, 김영진, "초박형 회절렌즈 어레이를 장착한 태양센서의 성능 검증", 한국정밀공학회 2023 춘계학술대회, 2023.
- 백기욱, Paulo Kemper, 윤효상, "Development of Small Size Space Laser Communication Terminal Prototype", 한국우주과학회 2023년 봄 학술대회, 2023.

**2022**

- Han, H., Baeck, K., Wi, J., Yoon, H., "Low-budget CubeSat star tracker calibration using Earth’s rotation." Advances in Space Research 70.7 (2022): 1880-1889.
- Yoon, H., Baeck, K., Wi, J., "Star Tracker Geometric Calibration Throught Full-State Estimation Including Attitude," International Journal of Aeronautical and Space Sciences, 23, 180-191 (2022)
- Paulo Kemper, Mikaël Marin, 윤효상, "Analysis of the Detector Shape Influence on Star Trackers' Performance", 한국항공우주공학회 2022 추계학술대회, 2022.
- 백기욱, Paulo Kemper, 장재훈, 이윤후, 윤효상, "우주광통신을 위한 광학 지상국 시스템의 DM 개발", 한국항공우주공학회 2022 추계학술대회, 2022.
- 한효근, 이영근, 김영진, 윤효상, "초박형 회절렌즈를 장착한 별 추적기의 성능 검증", 한국정밀공학회 2022년도 춘계학술대회, 2022.

**2021**

- Yoon, H., “Maximum Reaction-Wheel Array Torque/Momentum Envelopes for General Configurations," Journal of Guidance, Control, and Dynamics, 44.6 (2021): 1219-1223
- Baeck, K., Yoon, H., "Analytic Evaluation of Pointing Error on Free-space Optical Communication Satellite," the 12th Asia-Pacific International Symposium on Aerospace Technology (APISAT 2021), Jeju, 2021.
- 윤효상, 백기욱, 위준성, 박용준, 윤정인, 한효근, "초저고도 광학 인공위성 설계 및 핵심기술 개발", 한국항공우주학회 2021년도 춘계학술대회, 2021.

## 소식

누리집 Notice 페이지에 2021년 10월 이후 날짜로 실린 소식 12건이다. 날짜는 누리집 표기이며, 이틀에 걸친 행사는 두 날짜를 함께 적었다.[^notice]

- 2025-09-01 · 윤효상 교수님께서 부교수 (Associate Professor)로 승진하셨습니다.
- 2024-01-10~11 · 박용준, 김형철, 파울로 학생이 미국 플로리다 주 올랜도에서 개최된 AIAA SciTech 학회에서 발표를 수행하였습니다.
- 2023-08-22 · 윤효상 교수님께서 '2023 유도항법제어 심포지엄'에서 'KAIST 우주분야 연구현황'이라는 주제로 발표를 수행하셨습니다.
- 2023-06-28·29 · 위준성, 장재훈 학생이 한국항공우주공학회 '제1회 우주학술대회' 에서 발표를 수행하였고, 박용준, 한효근 학생이 포스터 발표를 수행하였습니다.
- 2023-05-11 · 한효근 학생이 '한국정밀공학회 2023 춘계학술대회'에서 발표를 수행했습니다.
- 2023-04-28 · 백기욱 학생이 '한국우주과학회 2023년 봄 학술대회'에서 발표를 수행했습니다.
- 2023-04-03 · 윤효상 교수님께서 언론사 조선비즈와 "젊은 두뇌가 뛴다" 인터뷰를 진행하셨습니다.
- 2023-01-24 · 윤효상 교수님께서 대통령실 누리홀에서 열린 첨단과학기술 젊은리더와의 오찬간담회에 참석하셨습니다.
- 2022-11-17·18 · 백기욱, 파울로 학생이 '한국항공우주공학회 2022년도 추계학술대회'에서 발표를 수행하였습니다.
- 2022-11-09 · 미래도전 과제 '초저고도 광학 인공위성 설계 및 핵심기술 개발'의 단계전환평가를 통과하였습니다.
- 2022-07-01 · 박용준 학생이 '2022 GNC 심포지엄'에서 발표를 수행하였습니다.
- 2022-05-13 · 한효근 학생이 '한국정밀공학회 2022 춘계학술대회'에서 발표를 수행했습니다.

## 수상

누리집 Notice 페이지의 수상 소식이다.[^notice]

- 2023-09-20 · 윤효상 교수님께서 "제4회 포니정 영리더상" 수상자로서 시상하셨습니다.

## 연락과 위치

- 연구실: KAIST N7-2 Room 4309, 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea[^contact] (학과 교수진 목록은 N7-2 #4309, 학과 연구실 소개는 N7-2동 #4309로 적는다[^aefac][^aelab])
- 교수 이메일: hyosang.yoon@kaist.ac.kr[^contact][^aelab][^aefac]
- 전화: 교수 +82-42-350-3734, 연구실 +82-42-350-3774[^contact]
[^p1]: H. Yoon, K. Baeck, J. Wi, International Journal of Aeronautical and Space Sciences 23, 180-191 (온라인 2022-01-01). <https://doi.org/10.1007/s42405-021-00432-5> 초록 기준.
[^p2]: J. Wi, K. Baeck, H. Yoon, The Journal of the Astronautical Sciences 70, 8 (온라인 2023-03-29). <https://doi.org/10.1007/s40295-023-00376-w> 초록 기준(출판사 논문 페이지).
[^p3]: J. Yun, K. Baeck, H. Yoon, IEEE Transactions on Aerospace and Electronic Systems 61, 6110-6124 (2025). <https://doi.org/10.1109/taes.2025.3526107> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: K. Baeck, J. Yun, H. Yoon, IEEE Transactions on Aerospace and Electronic Systems 61, 17017-17028 (2025). <https://doi.org/10.1109/taes.2025.3601111> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: S. Kim, H. Yoon, International Journal of Aeronautical and Space Sciences 27, 2488-2504 (온라인 2025-10-24). <https://doi.org/10.1007/s42405-025-01071-w> 초록 기준(출판사 논문 페이지).
[^p6]: S. Kim 외, D. M. Akos, NAVIGATION: Journal of the Institute of Navigation 72, navi.700 (온라인 2025-06-23). <https://doi.org/10.33012/navi.700> 초록 기준(OpenAlex 등록 초록).
[^research]: 연구실 누리집 Research 페이지 <https://spacecraft.kaist.ac.kr/Research> (연구 주제 여섯 가지, 날짜 없음, 2026-10-23 열람)
[^people]: 연구실 누리집 People 페이지 <https://spacecraft.kaist.ac.kr/People> (Professor, Ph.D. Candidates, M.S. Students, Contract Researcher, Alumni, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publication 페이지 <https://spacecraft.kaist.ac.kr/publication> (International Journal, International Conferences, Domestic Journal, Domestic Conferences, 「Last update: 2026.Feb.19」, 2026-10-23 열람)
[^notice]: 연구실 누리집 Notice 페이지 <https://spacecraft.kaist.ac.kr/Notice> (Recent Notice와 History, 2026-10-23 열람)
[^contact]: 연구실 누리집 Contact 페이지 <https://spacecraft.kaist.ac.kr/contact> (2026-10-23 열람)
[^aelab]: KAIST 항공우주공학과 연구실 소개 「Spacecraft Prototyping Laboratory, SPL」 <https://ae.kaist.ac.kr/boards/view/board_lab/91> (연구실명, 교수, 연구실 소개, 웹사이트, 이메일, Tel, Office, 연구분야, 2021-08-16 게시, 2026-10-23 열람)
[^aefac]: KAIST 항공우주공학과 교수진 목록 <https://ae.kaist.ac.kr/boards/lists/board_faculty/sc_category/1/> (윤효상 항목의 직위, Career, Tel, Website, E-mail, 연구분야, 연구실, 2026-10-23 열람)

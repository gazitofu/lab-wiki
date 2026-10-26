# 항공우주시스템 및 제어 연구실 (Aerospace Systems and Control Lab., ASCL)

**KAIST 항공우주공학과 · 방효충 교수**

- 분야: 인공위성·우주비행체의 자세 제어와 추정, 우주비행체 항법(행성 진입·착륙 항법, 근접 운용을 위한 상대 자세 추정)과 소형 위성 임무, 멀티로터 등 무인기의 데이터 기반 비행 제어와 고장 진단, 지형참조항법과 영상 기반 항법
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 제어 이론·제어 공학[^aelab][^sc-spin][^p4], 강화학습[^p6], 고장 진단·수명 예측[^p5], 3차원 복원·인식[^p3], 컴퓨터 비전[^p3][^p8], 과학·공학 AI[^aelab][^p3][^p8]
- 홈페이지: <http://ascl.kaist.ac.kr>
- 근거와 출처: [ASCL 근거 페이지](ascl-sources.md)

> 무인비행체와 인공위성 같은 항공우주 시스템이 갈 길을 정하고(유도), 자기 위치와 자세를 알아내며(항법), 정한 대로 움직이게 하는(제어) 방법을 연구하는 항공우주공학과 연구실로, 고정익·헬리콥터·멀티로터 무인기를 운용·실험하고 큐브위성 제작·운용 경험을 바탕으로 인공위성을 연구하며 기계학습과 인공지능도 접목한다.[^aelab]

## 무엇을 연구하나

연구실은 KAIST 항공우주공학과 방효충 교수의 연구실이다. 학과 연구실 소개는 연구실 이름을 「항공우주시스템 및 제어 연구실」(Aerospace Systems and Control)로 적고,[^aelab] 누리집은 ASCL(Aerospace Systems and Control Lab.)로 적는다.[^prof] 학과 연구실 소개에 따르면 연구실은 항공우주 시스템인 무인비행체 시스템과 인공위성 시스템의 유도(guidance, 비행체가 목표에 이르도록 따라갈 경로나 진행 방향을 정하는 일), 제어(control, 비행체가 정한 대로 움직이도록 구동 장치에 줄 입력을 정하는 일), 항법(navigation, 비행체의 위치·속도·자세를 추정하는 일)을 연구한다. 무인비행체는 고정익, 헬리콥터, 멀티로터(회전 날개인 로터를 여러 개 단 비행체)형 기체를 모두 운용·연구·실험하고, 인공위성은 큐브위성 제작과 운용 경험을 토대로 연구와 지상시험, 제작을 한다. 기계학습과 인공지능 연구도 항공우주 시스템 분야에 접목하려고 활발히 진행하며, 여러 기업체·연구소와 연구개발을 하고 여러 연구실과 협업·방문 연구를 한다고 적는다.[^aelab] 학과 교수진 목록은 교수의 연구분야를 Spacecraft Flight Dynamics and Control(우주비행체 비행역학·제어), UAV Guidance and Navigation(무인기 유도·항법)으로 적는다.[^aefac]

누리집 Research 메뉴는 연구를 Spacecraft GNC Algorithm(우주선의 유도·항법·제어 알고리즘), UAV GNC Algorithm(무인기의 유도·항법·제어 알고리즘), System Developments(시스템 개발) 세 갈래로 나눈다.[^scgnc][^uavgnc][^sys] 우주선 갈래의 목차는 궤도의 유도·항법·제어(최적 궤적 설계, 편대비행 제어와 항법, 궤도 결정, 궤적 수정 기동)와 자세 제어·결정(회전으로 자세를 안정시키는 위성의 장동·스핀 역전 제어, 벡터 관측을 이용한 자세·각속도 추정, 별 추적기 알고리즘 설계, 자세·궤도 제어 시뮬레이터)으로 나뉜다.[^scgnc] 궤적 최적화 글은 이를 시간이나 연료 소모 같은 성능 지수를 최소로 하도록 우주선의 제어 입력과 상태의 시간 이력을 정하는 과정으로 설명하고, 연구실이 연료 최적 지구-달 궤적과 최소 시간 지구-화성 궤적을 설계한 경험이 있으며 의사 스펙트럼 방법, 유전·진화 알고리즘, 경사 기반 방법, 순차 이차 계획법(SQP), 연속(호모토피) 방법 같은 수치 기법을 다룬다고 적는다.[^sc-traj] 편대비행 글은 위성 편대비행을 여러 위성이 무리를 지어 더 크고 대개 더 비싼 위성 한 대의 목표를 함께 이루는 개념으로 소개하고, 충격 기동으로 편대를 제어하는 전략과, 카메라로는 상대 거리를 바로 잴 수 없어 관측 가능성을 보장하는 상대 궤적을 함께 설계해야 하는 각도 측정 항법(angles-only navigation)을 연구했다고 적는다.[^sc-ff] 자세 추정 글은 별 추적기·태양 센서·자기장 센서 같은 벡터 관측 센서로 자세를 결정하는 알고리즘과 소프트웨어, 칼만 필터와 비선형 관측기를 이용한 추정, 자이로스코프 없이 벡터 관측만으로 각속도를 실시간 추정하는 연구를 소개하고,[^sc-att] 별 추적기 글은 낮은 고도나 높은 각속도 같은 가혹한 조건에서도 견디는 동적 환경의 별 인식 알고리즘을 연구했다고 적는다.[^sc-star]

무인기 갈래의 목차는 경로 계획·유도·항법·제어와 영상 기반 응용 두 칸으로 나뉜다. 경로 계획·유도·항법·제어 칸에는 여러 무인기의 협력 유도와 임무 경로 계획(레이더망 기만이나 방공망 제압 같은 국방 임무 포함), 협력 표적 추정을 위한 실시간 궤적 생성, 공항 주변 공역의 도착 항공기 순서·일정 최적화, 감시 임무의 경유점 계획, 장애물 탐지·회피와 충돌 탐지·해결, 지형참조항법과 영상 보조 지형참조항법, 벡터장 유도 법칙, 고고도 장기체공 무인기, 소형 전기 동력 패러포일의 유도·제어, 활공 탄약의 유도·항법·제어가 있고, 영상 기반 응용 칸에는 다중 표적 추적, 표적 추적과 위치 추정, 편대비행을 위한 상대 항법, 영상 항법, 자동 착륙, 지상 표적 인식이 있다.[^uavgnc] 지형참조항법 글은 GPS 같은 외부 위치 정보를 쓸 수 없을 때 지형 위를 낮게 나는 비행체에 위치 정보를 주는 항법으로 소개하고, 연구실이 확장 칼만 필터, HELI/SITAN, 점 질량 필터 기반 베이즈 필터로 지형참조항법 시스템을 구현했다고 적는다.[^uav-trn] 벡터장 유도 글은 공간의 각 점에 속도 벡터를 정해 둔 벡터장을 비행체가 따라가게 하는 유도 방법을 소개하고 도착 각도·시간·속도 제어와 착륙 접근, 편대비행 랑데부, 공중급유에 쓸 수 있다고 적는다.[^uav-vf] 자동 착륙 글은 고정익 무인기가 활주로 모서리나 표지를 영상으로 찾아 착륙하고 회전익 무인기가 표지나 헬리패드를 찾아 자동 착륙하는 기법을 소개한다.[^uav-land]

시스템 개발 갈래의 목차는 우주선 관련 시스템(QB50 프로젝트, 초소형 위성 개발, 자세 결정 시험대, 제어 모멘트 자이로스코프(CMG), 반구형 공진 자이로스코프(HRG), 광섬유 자이로스코프(FOG), 자유 비행 우주 로봇 실험대, 별 시뮬레이터 지상 시험대)과 무인기 관련 시스템(무인 항공 시스템, 소형 탑재 컴퓨터, 한국로봇항공기경연대회, 짐벌 시스템, 시선 추적기)으로 나뉜다.[^sys] 초소형 위성 글은 학부생과 함께한 캔샛(CanSat) 프로그램에서 출발해 큐브위성 키트로 위성 본체(버스) 개발에 나섰고 지상국 설비를 갖췄으며, KAIST 인공위성연구센터(SATREC)가 운영한 과학기술위성 3호(STSAT3)의 자세 제어 비행 소프트웨어 설계를 이끌었다고 적는다.[^sys-nano] QB50 글은 유럽연합이 지원하는 국제 협력 사업 QB50에 연구실 팀이 최종 참가 그룹으로 뽑혀, 하부 열권을 관측하는 2U 큐브위성 LINK(Little Intelligent Nanosatellite of KAIST)의 개발을 소개한다.[^sys-qb50] CMG 글은 CMG가 반작용 휠보다 큰 토크를 내지만 특이 배치와 복잡한 제어 법칙이라는 문제가 있어, 연구실이 CMG 하드웨어를 만들고 특이점 회피 알고리즘을 개발해 지상 시험으로 성능을 확인했다고 적는다.[^sys-cmg] 자유 비행 우주 로봇 실험대는 화강암 탁자 위에서 마찰을 줄인 로봇으로 한 개의 회전과 두 개의 병진 자유도를 갖는 평면 운동을 만들어 우주선 랑데부·도킹을 지상에서 모사한다.[^sys-robot] 무인기 쪽에서는 2003년부터 무인기 시스템을 개발했고, 팀(HIGHEST, 2009년에 HeXUS로 이름을 바꿈)이 2009년 제8회 한국로봇항공기경연대회에서 Grand Prize를 받았다고 적는다.[^sys-krac]

누리집 논문 목록의 2021–2025년 항목에서 우주 쪽은 유연한 부속물을 가진 위성의 자세 제어, 액체 추진제가 출렁이는 위성의 상태 추정, 별 추적기를 쓰는 자세 추정, 화성 진입·하강·착륙(EDL) 항법, 우주비행체 근접 운용을 위한 상대 자세 추정과 랑데부 유도, 지구와 달 사이 공간(시스루나 공간)의 소형 위성 군집, 큐브위성용 전계 방출 전기 추진(FEEP) 설계를 다룬다.[^ij][^ic] 무인기 쪽은 멀티로터·틸트로터·테일시터 무인기의 적응 제어와 비선형 동적 역변환 제어, SINDy·쿠프만 연산자·가우시안 과정 회귀로 자료에서 비행 동역학을 찾아내는 데이터 기반 제어와 고장 진단, 강화학습을 쓰는 충돌 회피와 착륙, 도심 항공 모빌리티(UAM) 경로 추종을 다루고,[^ij][^ic][^dc] 항법 쪽은 파티클 필터·팩터 그래프 기반 지형참조항법, 항공 영상의 의미 정보와 지도를 이용한 위치 추정, 다중 GNSS 위성 선택을 다룬다.[^ij][^ic] 목록에는 탄도 미사일 추적, 요격 유도, 자폭형 무인기의 종말 유도, 자동 표적 인식을 위한 SAR 영상 생성처럼 국방 응용을 겨냥한 표적 추적·유도 연구도 있다.[^ij][^dj][^ic]

## 주요 연구 주제

### 1. 인공위성 자세 추정과 제어

연구 페이지의 자세 제어·결정 글들은 회전 안정 위성의 장동·스핀 역전 제어에 한 단계 예측을 쓰는 비선형 예측 제어를 적용한 연구,[^sc-spin] 벡터 관측 기반 자세 추정과 자이로스코프 없는 각속도 추정,[^sc-att] CMG 하드웨어와 특이점 회피 알고리즘[^sys-cmg]을 소개한다. 대표 논문 1은 정지궤도 위성이 추력기를 쓸 때 생기는 충격 토크 때문에 별 영상의 잡음이 정규 분포를 벗어나는 문제를, 가우시안 혼합 모델을 이은 적응 확장 칼만 필터로 다뤄 자세 추정 성능을 높였다.[^p1] 2021–2025년 논문 목록에는 관성 모멘트가 불확실한 유연 우주선의 진동 억제 적응 제어(Acta Astronautica, 2025), CMG로 자세를 바꾸는 우주선의 심층 강화학습 자세 제어(Advances in Space Research, 2025), 액체 추진제 탱크를 가진 우주선의 출렁임 변수 관측기(Acta Astronautica, 2023), 소형 위성용 제어 모멘트 자이로스코프 개발(한국항공우주학회지, 2025)도 있다.[^ij][^dj]

### 2. 우주비행체 항법과 근접 운용

연구 페이지는 궤도 결정을 지상 추적과 지상 통신 없는 자율 항법 두 갈래로 나눠 다루고,[^sc-od] 편대비행의 각도 측정 항법을 소개한다.[^sc-ff] 대표 논문 2는 화성 진입 단계에서 지상 전파 비컨, 관성 측정 장치(IMU), 대기·공력가열 센서의 측정을 이상값에 강한 칼만 필터로 합쳐 위치와 매개변수를 추정했다.[^p2] 대표 논문 3은 단안 카메라 영상으로 협조하지 않는 목표 우주선의 상대 위치와 방향을 추정하면서, 특징점 예측에 트랜스포머 신경망을 썼다.[^p3] 2021–2025년 논문 목록에는 시스루나 공간 소형 위성 군집의 안정성·자율성 연구(IEEE Access 2025, Aerospace 2024 등), 큐브위성용 전계 방출 전기 추진의 다목적 설계 최적화(Aerospace Science and Technology, 2024), 랑데부의 시간 최적 유도 법칙(International Journal of Aeronautical and Space Sciences, 2024), 화성 착륙 동력 하강 단계의 실시간 유도(Advances in Space Research, 2021)도 있다.[^ij]

### 3. 무인기의 데이터 기반 비행 제어·고장 진단과 학습

대표 논문 4는 탑재물 때문에 동역학이 불확실한 멀티로터의 지배 방정식을 SINDy로 자료에서 찾아낸 뒤, 그 모델로 장애물을 피하며 궤적을 따라가는 모델 예측 제어를 만들었다.[^p4] 대표 논문 5는 쿠프만 연산자로 멀티로터를 선형 모델로 나타내고 루엔버거 관측기로 고장 난 구동기를 찾아냈다.[^p5] 대표 논문 6은 패러포일이 착륙할 때 지상 위험을 피하는 조종 법칙을 아래를 내려다본 영상만으로 강화학습해, 벡터장 유도 법칙을 쓰는 규칙 기반 방식과 비교했다.[^p6] 2021–2025년 논문 목록에는 가우시안 과정 회귀를 쓰는 비선형 동적 역변환 제어(Aerospace Science and Technology, 2025), 연료·탑재물 불확실성을 고려한 모델 참조 적응 제어(Proceedings of the Institution of Mechanical Engineers, Part G, 2025), 동축 도데카콥터(coaxial dodecacopter)의 고장 허용 제어 배분(Control Engineering Practice, 2025), 멀티로터 무인기의 비선형 동적 역변환 제어에서 시간 지연을 줄이는 연구(Journal of Guidance, Control, and Dynamics, 2024)도 있다.[^ij]

### 4. 지형·영상 정보를 이용한 비행체 항법

연구 페이지는 GPS를 쓸 수 없을 때를 대비한 지형참조항법과,[^uav-trn] 관성 측정과 수치 지형 고도 자료(DTED)를 함께 써서 영상 항법의 오차 누적을 억제하는 영상 보조 지형참조항법을 소개한다.[^uav-vatrn] 대표 논문 7은 지형참조항법의 파티클 필터가 여러 봉우리를 가진 분포 때문에 퇴화하는 문제를, 입자를 그럴듯한 지형 등고선 쪽으로 옮기는 표본 추출 전략으로 줄였다.[^p7] 대표 논문 8은 딥러닝으로 의미 분할한 항공 영상을 의미 정보가 표시된 지도 자료와 맞춰, 영상이 회전해도 바뀌지 않게 위치와 방향을 추정했다.[^p8] 2021–2025년 논문 목록에는 팩터 그래프 기반 지형참조항법(International Journal of Control, Automation, and Systems, 2024)과 레이더 고도계 오차를 적응적으로 추정하는 지형참조항법(International Journal of Aeronautical and Space Sciences, 2025)도 있다.[^ij]

## 대표 논문

누리집 International Journals 페이지의 2021–2025년 학술지 논문 가운데 방효충 교수가 저자이고 초록을 확인할 수 있는 여덟 편을 네 연구 갈래(인공위성 자세 추정과 제어, 우주비행체 항법과 근접 운용, 무인기의 데이터 기반 비행 제어·고장 진단과 학습, 지형·영상 정보를 이용한 비행체 항법)에 나눠 골랐다. 2, 4–8번은 교수가 마지막 저자이고, 1, 3번은 교수가 네 저자 가운데 셋째다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^ij] |
|---|---|---|---|---|
| 1 | 2023 | [GMM-Based Adaptive Extended Kalman Filter Design for Satellite Attitude Estimation under Thruster-Induced Disturbances](https://doi.org/10.3390/s23094212) · Sensors | 별 추적기는 노출 시간 동안 별을 담아 중심점을 더 잘 재려고 보통 별 영상의 초점을 흐려 찍는다. 위성이 기동하는 동안에는 화면 속 별 점이 위성 움직임의 영향을 받아 중심점 측정 정확도가 떨어지고 별 방향 벡터도 나빠질 수 있다. 정지궤도 위성은 궤도 외란 속에서 궤도 요소를 유지하거나 바꾸려고 탑재 추력기를 쓰는데, 추력기 정렬 오차가 있고 토크 명령이 충격 모양의 신호로 나가 목표 토크를 만들기 어렵다. 이 충격 토크가 위성의 각속도를 갑자기 바꾸어 별 영상에도 영향을 주므로, 별 영상의 잡음이 정규 분포를 따르지 않게 된다. 이를 다루려고 예측한 상태로 측정 벡터를 예측하는 적응 확장 칼만 필터를 구현하고, 여기에 가우시안 혼합 모델(GMM, 여러 정규 분포에 가중치를 주어 합친 확률 모형)을 이어 각 정규 분포에 가중치를 주어 측정 벡터를 더 잘 예측하게 했다. 모의 결과 GMM-EKF는 자세 추정에서 EKF보다 성능이 30% 나았고, 저자들은 이 방법이 정지궤도 위성의 궤도 유지 기동 중에 쓰기에 더 매력적인 방법이 될 수 있다고 적는다.[^p1] | 1저자 T. Kim, 셋째 저자 방효충, 마지막 저자 H. Yoon (4명) |
| 2 | 2023 | [A Distributionally Robust Fusion Framework for Autonomous Multisensor Spacecraft Navigation during Entry Phase of Mars Entry, Descent, and Landing](https://doi.org/10.3390/rs15041139) · Remote Sensing | 차세대 화성 진입·하강·착륙(EDL)의 진입 단계를 위한 강인한 다중 센서 항법 필터를 설계했다. 진입 단계는 화성 착륙 과정에서 가장 길고 불확실한 구간이며, 이 단계의 항법 성능이 동력 하강 단계가 끝날 때의 착륙 정밀도를 정한다. 지상에 놓인 전파 비컨 배열, 관성 측정 장치(IMU), 진입 비행체 몸체의 대기·공력가열 센서 배열이 잰 값을 M-추정 기반 반복 확장 칼만 필터(MIEKF) 틀로 합쳤다. 여러 센서를 함께 써서 위치 정확도를 높이고, 다른 방식으로는 관측할 수 없는 매개변수도 추정한다. 통계적으로 강인한 필터 형식이라 정규 분포를 벗어나는 측정 잡음, 곧 센서 고장이나 간섭 같은 이상값 사건이 있어도 상태와 매개변수를 정확히 추정한다. 낙하산 단계의 추정 오차를 크게 줄여 고른 착륙 지점에 정밀하게 내릴 가능성을 높였다. 상태 여섯 개와 매개변수 세 개를 추정했고, 확장 칼만 필터(EKF)·무향 칼만 필터(UKF)와 비교했으며, 현실적인 센서 측정 시나리오의 상세 모의에서 미래 행성 정밀 착륙 요구를 맞출 수 있음을 보였다.[^p2] | 1저자 N. S. Zewge, 마지막 저자 방효충 (2명) |
| 3 | 2024 | [Transformer Network-Aided Relative Pose Estimation for Non-cooperative Spacecraft Using Vision Sensor](https://doi.org/10.1007/s42405-023-00703-3) · International Journal of Aeronautical and Space Sciences | 랑데부 운용에서 다가가는 위성(chaser)을 기준으로, 협조하지 않는 목표 우주선의 상대 6자유도 자세(위치와 방향)를 단안 카메라 영상으로 추정한다. 목표 위성의 특징점을 예측하는 데 합성곱 신경망(CNN) 대신 고해상도 트랜스포머 신경망을 썼고, 저자들은 트랜스포머 안의 자기 주의(self-attention) 구조가 CNN의 한계를 넘는 장점이 있다고 적는다. 먼저 역 직접 선형 변환(IDLT)으로 목표 위성의 3차원 모델을 복원하고, 학습 기반 영상 처리 부분과 자세 계산의 기하 최적화로 추정 과정을 짰다. 영상 처리 부분은 CNN 구조로 목표의 위치를 찾고, 트랜스포머 기반 핵심점 검출 신경망이 2차원 핵심점을 예측한다. 신뢰도 점수에 따라 예측한 핵심점을 3차원 모델의 점에 대응시켜 효율적 PnP(perspective-n-point, 영상 속 점과 알려진 3차원 점의 대응으로 카메라 자세를 구하는 문제) 방법으로 자세를 계산하고, 비선형 반복 계산인 가우스-뉴턴 방법으로 다듬는다. 우주선 자세 추정 데이터셋으로 학습·시험해 위치와 회전 값 모두에서 우수한 정확도를 보였고, 자기 주의 구조 덕분에 우주 영상의 크게 바뀌는 배경과 조명 조건에서도 강인했다. 낮은 입력 영상 해상도에서 부동소수점 연산과 학습 매개변수를 적게 써 계산 자원도 덜 쓴다.[^p3] | 1저자 J. Ahmed, 셋째 저자 방효충, 마지막 저자 Y. Choi (4명) |
| 4 | 2025 | [Sparse Identification of Nonlinear Dynamics-Based Model Predictive Control for Multirotor Collision Avoidance](https://doi.org/10.1049/cth2.70049) · IET Control Theory & Applications | 탑재물 때문에 생기는 불확실성과 알려지지 않은 동역학을 고려해, 멀티로터의 충돌 회피를 위한 데이터 기반 모델 예측 제어(MPC) 방법을 제안했다. SINDy(sparse identification of nonlinear dynamics)로 멀티로터의 지배 방정식을 얻는데, SINDy는 소수의 주된 함수가 시스템의 거동을 주로 결정한다는 가정 아래 적은 자료로 방정식을 찾아낸다. 기준 제어기와 MPC를 결합한 자료 수집 틀로 모델 식별에 쓸 다양한 궤적을 만들고, 멀티로터 동역학의 사전 지식을 반영한 후보 함수 목록과 정규화 기법으로 SINDy 모델의 정확도를 높였다. 이렇게 얻은 모델로 MPC가 장애물 회피를 포함한 상태·입력 제약을 지키며 궤적을 정확히 따라가게 했다. 모의 결과 SINDy는 질량 매개변수의 불확실성과 공력 효과를 반영한 지배 방정식을 찾아냈고, 제안한 방법은 매개변수 불확실성과 알려지지 않은 공력 모델 때문에 성능이 떨어지는 기존 MPC보다 장애물 회피와 궤적 추종 모두에서 나았다.[^p4] | 1저자 J. D. Lee, 마지막 저자 방효충 (4명) |
| 5 | 2024 | [Data-Driven Fault Detection and Isolation for Multirotor System Using Koopman Operator](https://doi.org/10.1007/s10846-024-02142-y) · Journal of Intelligent & Robotic Systems | 쿠프만 연산자와 루엔버거 관측기를 이용한 멀티로터 시스템의 데이터 기반 고장 검출·분리(FDI)를 다뤘다. 쿠프만 연산자는 비선형 동역학계를 선형계로 바꿀 수 있는 무한 차원 선형 연산자이며, 이 변환으로 선형 고장 검출 방법을 비선형계에 쓰려는 것이 목표다. 먼저 대각 성분만 있지 않은 관성 텐서, 무게중심 변화, 공력 효과, 구동기 동역학을 고려해 멀티로터를 나타내는 쿠프만 연산자 기반 선형 모델을 만들었다. 여러 후보 리프팅 함수(상태를 선형 모델의 변수로 옮기는 함수)의 예측 성능을 평균 제곱근 오차로 비교해 가장 알맞은 것을 골랐다. 이어 이 선형 모델로 쿠프만 연산자 기반 루엔버거 관측기를 만들어, 고장 난 구동기를 가려낼 잔차를 생성했다. 모의와 실험에서 이 관측기는 고장 자료를 따로 정의하지 않고도 편향(bias)과 효율 손실 같은 구동기 고장을 검출했다.[^p5] | 1저자 J. D. Lee, 마지막 저자 방효충 (5명) |
| 6 | 2024 | [Data-Driven Hazard Avoidance Landing of Parafoil: A Deep Reinforcement Learning Approach](https://doi.org/10.2514/1.i011281) · Journal of Aerospace Information Systems | 패러포일의 자율 착륙 위험 회피 기술을 강화학습 기반 방식과 규칙 기반 방식 두 가지로 구현하고, 강화학습 방식을 지지했다. 두 방식의 상대적 장점과 행동상의 닮은 점도 제시했다. 데이터 기반 방식에서는 관측 자료를 한 가지 종류로 맞추려고 비행체 동역학을 따로 덧붙이지 않고, 바로 아래를 향한 영상의 연속만 관찰하는 결정 과정을 설계했다. 에이전트(학습하며 행동을 정하는 주체)는 이 과정에서 위험 회피 조종 법칙을 처음부터 끝까지 한 번에 배운다. 반면 규칙 기반 방식은 유도·제어 계층, 비행체의 동역학 상태, 지상 장애물의 수치 정보를 명시적으로 쓴다. 강화학습에는 soft actor-critic 방법을 써서 아래 방향 영상을 패러포일 브레이크 조작으로 바꾸는 정책을 학습했고, 규칙 기반 방식에는 각 위험 요소를 밀어내는 원천으로 보는 벡터장 유도 법칙을 썼다. 두 방식을 설계할 때 경험적으로 같은 점과 다른 점을 보이고, 여러 시험 사례의 수치 실험으로 강화학습 방법을 검증하며 두 방식의 결과 궤적을 비교했다.[^p6] | 1저자 J. Park, 마지막 저자 방효충 (2명) |
| 7 | 2025 | [Contours-Seeking Proposal Density Particle Filter and Resilient Terrain-Referenced Navigation](https://doi.org/10.1109/taes.2025.3588823) · IEEE Transactions on Aerospace and Electronic Systems | 보조 항법 시스템은 비행체를 강인하게 운용하는 데 꼭 필요하며, 지형참조항법처럼 자체 센서만으로 동작하는 틀에서 특히 그렇다. 그런데 여러 봉우리를 가진 가능도, 매우 비선형적인 지형 고도, 알 수 없는 예측 편향 때문에 사후 분포가 여러 봉우리를 갖고 예측하기 어려워지며, 그 결과 파티클 필터(가중치를 붙인 많은 표본으로 확률 분포를 나타내 상태를 추정하는 방법)가 퇴화한다. 이 연구는 이 문제에 맞춘 표본 추출 전략으로 파티클 필터의 수치 불안정과 퇴화를 다뤘다. 가우시안 혼합 무작위 강제(random forcing) 방식이 입자를 지형 경사를 따라, 그리고 편향을 거슬러 가장 그럴듯한 지형 등고선 쪽으로 밀어 준다. 혼합 성분 하나하나가 가능도의 봉우리 하나에 대응해 모델에 담지 않은 지형 특징에도 적응한다. 보조 표본 추출로 이 혼합 표본 추출을 가능성이 높은 입자에만 골라 적용해, 덜 퇴화하고 가중치가 고른 입자 집합을 얻었다. 수치 실험에서 가중치 분산을 줄이고 유효 표본 수를 늘렸으며, 심한 미지 예측 편향과 여러 봉우리를 가진 측정 잡음처럼 상황이 나빠질 때도 강한 복원력을 보여 오랜 시간 믿을 수 있는 파티클 필터링을 보장했다.[^p7] | 1저자 J. Park, 마지막 저자 방효충 (2명) |
| 8 | 2024 | [Visual Semantic Context and Efficient Map-Based Rotation-Invariant Estimation of Position and Heading](https://doi.org/10.33012/navi.634) · NAVIGATION: Journal of the Institute of Navigation | 영상이 회전해도 결과가 바뀌지 않고 시간이 지나도 일관된, 시각 지도 기반 위치·방향(heading) 추정 시스템을 제안했다. 이를 위해 의미 분할로 나뉜 영역들이 반지름 방향과 둘레 방향으로 어떻게 분포하는지를 이용한다. 특정한 위치와 방향을 나타내려고 「시각적 의미 문맥(visual semantic context)」이라는 새 개념을 도입해, 극좌표 방식으로 의미 정보를 모으고 차이 척도를 함께 쓴다. 시스템은 딥러닝으로 의미 분할한 항공 영상에서 얻은 시각적 의미 문맥을, 의미가 표시된 데이터베이스의 시각적 의미 문맥들과 맞춰 본다. 모든 경우를 다 찾아보는 비싼 계산을 줄이려고 두 단계 최소화를 쓴다. 첫 단계는 방향 변수를 주변화(그 변수가 가질 수 있는 값을 모두 고려해 합쳐 없애는 일)하고 위치를 대략 찾는데, 이때 콜모고로프-스미르노프 검정으로 가능성이 낮은 후보를 걸러 탐색 범위를 크게 줄인다. 둘째 단계에서 추정값을 다듬는다. 수치 실험에서 제안한 알고리즘은 위치와 방향을 찾아냈고, 영상 회전에 영향을 받지 않았으며, 축척 정보가 부정확해도 강인했다.[^p8] | 1저자 J. Park, 마지막 저자 방효충 (4명) |

## 교수와 전문 분야

방효충 교수(Bang, Hyochoong)는 KAIST 항공우주공학과 교수다. 학과 교수진 목록은 직위를 Professor로, 학력을 B.S. Seoul Nat'l Univ('85), M.S. Seoul Nat'l Univ('87), Ph.D. Texas A&M Univ('92)로 적는다.[^aefac] 누리집 교수 소개(Curriculum Vitae)에 따르면 서울대학교 항공공학(Aeronautical Engineering)에서 학사(1985)와 석사(1987)를, 미국 Texas A&M University 항공우주공학(Aerospace Engineering)에서 박사(1992)를 받았다. 박사 논문은 「Maneuver and Vibration Control of Flexible Space Structures by using Lyapunov Stability Theory」(지도교수 John L. Junkins)다.[^prof] 같은 소개의 경력 칸은 Texas A&M University 연구조교(Research Assistant, 1989.1–1992.5), U.S. Naval Postgraduate School 연구조교수(Research Assistant Professor, 1992.7–1994.12), 한국항공우주연구원 선임연구원(Senior Researcher, 1995.3–1999.8), 충남대학교 조교수(1999.9–2000.12)를 거쳐 KAIST 조교수(2001–2003.2), 부교수(2003–2009.2), 교수(2009.3–)로 적는다. 경력 칸의 보직은 항공우주공학과 학과장(Head of Department of Aerospace Engineering, 2012–2016), 공과대학 부학장(Vice Dean, College of Engineering, 2017–2019.2), Director of KAIST Institute for Security Convergence Research center(ISCR, 2019.3–2021.8), Head of Interdisciplinary Program on Space Exploration Engineering(SPEX, 2008–2017), Director of High-Speed Vehicle Research Center(2015–present), Director for National Space Lab.(NSL, 2008–Present), Director for National Research Lab.(NRL) in Space Fine Attitude Control Lab.(2002–2007)이고, 학회와 자문 활동으로 Senior vice president of The Korean Society for Aeronautical and Space Sciences(KSAS, 2020.3–present), Chair of National defense subcommittee of Presidential Advisory Council on Science and Technology(2021.1–present)를 적는다.[^prof]

교수 소개의 연구 관심(Research interest)은 위성 자세 동역학과 제어(Satellite attitude dynamics and control), 우주선 유도·항법(Spacecraft guidance and navigation), 행성 간 임무 설계(Inter-planetary mission design), 우주 시스템(Space systems), 무인기 비행 동역학과 제어(UAV flight dynamics and control), 무인기 비행 제어 시스템 설계(UAV flight control systems design), 항공우주 비행체 궤적 계획과 최적화(Aerospace vehicle trajectory planning and optimization)다. KAIST에서는 2001년 1월부터 Dynamics, Flight Performance and Stability, Aerospace Sensors and Actuators, Spacecraft Attitude Dynamics Control, Aerospace S/W, Experiment in Aerospace Control, Spacecraft Guidance and Control 등을 가르쳤다고 적는다. 학술 활동으로 American Institute of Aeronautics and Astronautics(AIAA) Senior member, IEEE Member, KSAS Journal과 IJCAS 편집위원(Editorial board, 2006–present), Korea Academy of Science and Technology(KAST) Junior member(2002–present) 등을 적고, 책으로 「The Finite Element Method using MATLAB」(CRC Press, 1997, Young W. Kwon과 공저)와 「Flight Dynamics and Control」(Kyung Moon Press, 2004, 국문, 공저)을 적는다.[^prof]

교수 소개의 수상 칸은 2002년 Young Scientist Award(젊은과학자상, Presidential Award)와 National Research Lab.(NRL)(Presidential Researcher), 2004년 Excellent Paper Award(과학기술우수논문상, The Korean Federation of Science and Technology Societies), 2005년 Top 50 Best Research Award(Ministry of Science and Technology), 2007년 Merit Award, Deputy Prime Minister(과학기술부총리상) 등을 적고, 교수가 지도교수(Advisor)를 맡은 팀이 한국로봇항공기경연대회(Korea Robot Aircraft Competition)에서 받은 상으로 제5회 Gold Prize(2006), 제6회 Bronze Prize(2007), 제7회 Silver Prize(2008), 제8회 Grand Prize(2009)를 적는다.[^prof] 누리집 과제 페이지(2018년 1월 갱신 표기)는 1999–2017년에 시작한 과제 129건을 적는데, 위탁기관으로 한국항공우주연구원, 국방과학연구소, 한국연구재단, 방위사업청, 공군사관학교, 한국과학재단, 기업체 등이 나온다.[^projects]

논문으로 보면 지금의 전문 분야는 네 갈래다. 첫째, 별 추적기를 쓰는 인공위성 자세 추정이다(대표 논문 1).[^p1] 둘째, 화성 진입 항법과 근접 운용의 상대 자세 추정 같은 우주비행체 항법이다(대표 논문 2, 3).[^p2][^p3] 셋째, 자료로 찾은 모델과 강화학습을 쓰는 무인기의 비행 제어·고장 진단·착륙이다(대표 논문 4–6).[^p4][^p5][^p6] 넷째, 지형과 항공 영상을 이용해 비행체의 위치를 추정하는 항법이다(대표 논문 7, 8).[^p7][^p8]

## 응용 분야

학과 연구실 소개는 연구실이 다수의 기업체·연구소와 연구개발을 진행한다고 적는다.[^aelab] 연구 페이지는 영상 기반 상대 항법을 도킹, 공중급유, 편대비행 임무에,[^uav-relnav] 고고도 장기체공 무인기를 숲과 바다의 감시·관측에,[^uav-hale] 지형참조항법을 군용·민간 항공 전자 장비의 통합 항법에 쓸 수 있다고 적고,[^uav-trn] 도착 항공기의 순서·일정 연구는 관제사가 터미널 공역의 항공기에 비행 명령을 내리는 일을 돕기 위한 것이라고 적는다.[^uav-arr] 대표 논문 2는 미래 행성 정밀 착륙을,[^p2] 대표 논문 3은 우주 랑데부 운용을 대상으로 한다.[^p3] 졸업생 진로 칸에 가장 많이 나오는 기관은 한국항공우주연구원(27명)이고, 국방과학연구소(10명)가 그다음이며, 그 밖에 Nearthlab, Satrec Initiative, KAI, Hanwha 계열 회사, LIG Nex1, Samsung Electronics, Hyundai Motor Group, ETRI, Chosun University, The University of Sheffield, TU Delft 등이 있다.[^alumni]

## 구성원

누리집 Members 메뉴의 Post Doctors 5명(2025년 10월 9일 갱신 표기), Ph.D. Candidates 16명(2026년 10월 9일 갱신 표기, Full-time 14명과 Part-time 2명), M.S. Candidates 19명(2026년 3월 8일 갱신 표기, Full-time 18명과 Part-time 1명)이다.[^postdoc][^phd][^ms] Research Professor, Contract Researcher, Intern, Visiting Scholars 페이지는 지금 해당 인원이 없다고 적는다.[^empty] 과정은 페이지 표기를 옮겼고 Part-time은 페이지의 구분이다. 시작은 각자 이력에 적힌 박사후연구원·박사과정·석사과정 시작 연도이며, 「가을학기」는 이름 앞 번호에 붙은 s 표기(페이지 설명: Joined in fall semester)를 옮긴 것이다. 연구 주제는 이력의 Research Topic·Research Interests 칸이다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Marin Mikaël | 박사후연구원 | 2020 |  |  |
| 이성헌 (Lee, Seongheon) | 박사후연구원 | 2020 |  |  |
| Arshad, Muhammad Awais | 박사후연구원 (Mechanical Engineering Research Institute, KAIST) | 2023 |  | 3 |
| Zewge, Natnael S. | 박사후연구원 | 2024 | Statistical signal processing methods for multisensor navigation in air, land, sea, and space applications; Machine learning and optimization techniques for sensor data processing | 1, 2 |
| 이동우(Lee, Dongwoo) | 박사후연구원 (Mechanical Engineering Research Institute, KAIST) | 2025 |  | 4, 5 |
| 심태민 (Shim, Taemin) | 박사과정 | 2017 | Coaxial Rotor Helicopter Modeling and Control; Rotary Wing Aircraft Guidance |  |
| 문민기(Mun, Mingi) | 박사과정 | 2021 |  |  |
| 이호형(Lee, Hohyeong) | 박사과정 | 2022 가을학기 |  |  |
| 임철수(Lim, Chulsoo) | 박사과정 | 2023 가을학기 | Reinforcement Learning, Agile flight |  |
| Mola, Habtamu | 박사과정 | 2023 가을학기 |  |  |
| Gadisa, Dinaol Zelalem | 박사과정 | 2023 가을학기 |  |  |
| 김영재(Kim, Youngjae) | 박사과정 | 2024 |  | 4 |
| 임석재(Im, Sukjae) | 박사과정 | 2024 |  | 5 |
| Mohammed, Haruna Hamza | 박사과정 | 2024 가을학기 |  |  |
| 이호선(Lee, Hosun) | 박사과정 | 2025 | Nonlinear control; Data-driven system identification |  |
| 장보현(Chang, Bohyun) | 박사과정 | 2025 | Relative Navigation in Spacecraft Proximity Operation; Photogrammetry, Sensor Fusion, SLAM |  |
| 한지호(Han, Jiho) | 박사과정 | 2025 | Path following; UAV control |  |
| 박경수(Park, Geongsu) | 박사과정 | 2025 가을학기 | Spacecraft Attitude and Orbit Determination, Control; Control Moment Gyro |  |
| 박주형(Park, Juhyeong) | 박사과정 | 2026 가을학기 | (Flexible) Satellite attitude determination and control; Nonlinear adaptive, and prescribed performance control |  |
| 김은혁 (Kim, Eunhyouek) | 박사과정 (Part-time) | 2021 | Optimization of Ion-thruster operation for small satellite; Optimization of constellation orbit design |  |
| 신동민 (Shin, Dongmin) | 박사과정 (Part-time) | 2025 가을학기 |  |  |
| 강명진 (Kang, Myeongjin) | 석사과정 | 2025 |  |  |
| 김동현 (Kim, Donghyeon) | 석사과정 | 2025 |  |  |
| 김여원 (Kim, Yeowon) | 석사과정 | 2025 |  |  |
| 이동연 (Lee, Dongyeon) | 석사과정 | 2025 |  |  |
| 정민혁 (Jeong, Minhyeok) | 석사과정 | 2025 |  |  |
| 조병현 (Cho, Byeonghyeon) | 석사과정 | 2025 |  |  |
| Radoslaw, Szydilk | 석사과정 | 2025 | Sampling based motion and path planning for UAVs; Distributed algorithms for multi-agent systems |  |
| Kasprzak, Tomasz | 석사과정 | 2025 | Cost-Efficient Passive Radar-Guided UAVs; Loitering munition |  |
| Homoki, Gergely | 석사과정 | 2025 가을학기 | Satellite Constellations |  |
| Zhemisbek, Dilnaz | 석사과정 | 2025 가을학기 |  |  |
| 김규담 (Kim, Gyudam) | 석사과정 | 2026 |  |  |
| 신예담 (Shin, Grace Yedam) | 석사과정 | 2026 |  |  |
| 이경환 (Lee, Kyunghwan) | 석사과정 | 2026 |  |  |
| 이윤지 (Lee, Yoonji) | 석사과정 | 2026 |  |  |
| Örs, Serkan Burak | 석사과정 | 2026 | Spacecraft Attitude Determination and Control |  |
| 김태헌(Kim, Taehun) | 석사과정 | 2026 가을학기 | Spacecraft Attitude Determination and Control |  |
| Wierzejski, Maciej | 석사과정 | 2026 가을학기 | Uncertainty-Aware Trajectory Prediction and Track Re-Association for Aerial Objects; Uncertainty-Aware Prediction of Terminal Airspace Traffic Complexity |  |
| Zwierzynski, Jan | 석사과정 | 2026 가을학기 | Simulation and control of multirotor UAVs under system and environmental uncertainties; Resilient UAV control under actuator degradation and disturbances |  |
| 우진호 (Woo, Jinho) | 석사과정 (Part-time) | 2025 |  |  |

## 졸업생과 이전 구성원

누리집 Alumni 페이지(머리에 2025년 10월 9일 갱신 표기)의 Post Ph.D. 칸 19개, Ph.D. 칸 71개, M.S. 칸 88개 항목을 사람별로 묶은 132명이다. 한 사람이 여러 칸에 적힌 경우(석사 뒤 박사, 박사 뒤 박사후연구원 등)는 한 줄에 모았고, 학위·과정 뒤의 연도는 각 항목 머리의 두 자리 연도 표기(예: 03-07s)를 네 자리로 바꾼 기간이다. 진로는 그 사람의 이력 항목에서 「present」로 적힌 직장·직위이며 괄호 안은 그 시작 연도다. 지금 구성원 표에 있는 사람은 「현재 구성원」으로 적었다. 학위 논문은 이력 항목의 M.S. Thesis·Ph.D. Dissertation 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Alkaabi, Abdulla Ali Salem | 석사 2024–2026 |  |  |
| 고만준 (Koh, Man Jun) | 석사 2024–2026 |  |  |
| 김현민(Kim, Hyeonmin) | 석사 2024–2026 |  |  |
| 박상욱(Park, Sangwook) | 석사 2024–2026 | Major, ROK Airforce and Defense Acquisition Program Administration (2012–) |  |
| 박태윤(Park, Taeyoon) | 석사 2024–2026 |  |  |
| 원동식(Won, Dongshik) | 박사 2019–2026 |  |  |
| Mohammed, Irfan Rashed | 박사 2021–2025 · 석사 2012–2014 |  | 박사: A study on cognitive intelligence-based small satellite constellations for cislunar space; 석사: MEMS-based Optimal Attitude Determination System Design for Nanosatellites |
| 김강산(Kim, Kangsan) | 석사 2023–2025 | Officer, Republic of Korea Airforce, Korea (2015–) | 석사: Infra-Red Scene Simulator for Satellite-Based Hypersonic Target Detection |
| 김남수(Kim, Lamsu) | 박사후연구원 2025 · 박사 2020–2025 · 석사 2018–2020 | Senior researcher, PGM Division, Hanhwa Aerospace (2025–) | 박사: Data-Driven Incremental Flight Dynamics and Center of Gravity Control for Tailsitter Drones; 석사: Maneuvering target tracking with 3D variable turn model and kinematic constraint |
| 김성중(Kim, Sungjoong) | 박사 2019–2025 · 석사 2017–2019 |  | 석사: Vision-Based Map Referenced UAV Navigation using Terrain Classification |
| 박주형(Park, JuHyeong) | 석사 2023–2025 | 현재 구성원(박사과정) | 석사: Vibartion Suppression Adaptive Prescribed Performance Control for Flexible Spacecraft with Uncertain Moment of Inertia |
| 안형주(Ahn, Hyungjoo) | 박사 2020–2025 · 석사 2018–2020 |  | 박사: An Integrated Motion Planning Framework for Autonomous Aerial Robots in Complex Environments; 석사: Receding Horizon Motion Planning for Multi-rotor with Point Cloud Environment |
| 오승렬(Oghim, Snyoll) | 박사 2019–2025 |  | 박사: Time/Fuel-Optimal Guidance Laws for Spacecraft Rendezvous |
| 이동우(Lee, Dongwoo) | 박사 2021–2025 · 석사 2019–2021 | 현재 구성원(박사후연구원) | 석사: Model reference adaptive control design for quadrotor UAV transporting unknown payloads |
| 이유진(Lee, Yujin) | 석사 2023–2025 |  | 석사: Prescribed Performance-Based Attitude Takeover Control Using Time-Delay Estimation for Combined Spacecraft With Model Uncertainties |
| 이호선(Lee, Hosun) | 석사 2023–2025 | 현재 구성원(박사과정) | 석사: Agile Transition Control of a Novel Tailsitter UAV Using a Momentum Exchange Device |
| 장광우(Jang, Kwangwoo) | 박사 2020–2025 · 석사 2018–2020 |  | 석사: Attitude Control Strategy of Quad-Tiltrotor UAV in Transition Mode |
| 장보현(Chang, Bohyeon) | 석사 2023–2025 | 현재 구성원(박사과정) | 석사: Point Cloud Registration Algorithm Using LiDAR Intensity Measurement for On-Orbit Geometry Reconstruction and Relative Navigation |
| 한지호(Han, Jiho) | 석사 2023–2025 | 현재 구성원(박사과정) | 석사: Dual Virtual Target-Based Quadratic Polynomial Curve Fitting Guidance for Urban Air Mobility Path Following |
| Ahmed, Jamal | 박사 2019–2024 | Manager (Control Electronics), Space & Upper Atmosphere Research Commission (SUPARCO), Pakistan (2024–) | 박사: Deep Learning based Relative Pose Estimation of Non-Cooperative Spacecraft using Vision Sensors |
| Liao, Jingxian | 박사 2020–2024 | Post Doctoral, Industrial Artificial Intelligence Centre, Shenzhen Institute for Advanced Study, UESTC, Shenzhen, China (2024–) | 박사: Nonlinear Blended Aerodynamic Modeling and Anti-harmonic Disturbance Robust Control of Fixed-wing Tilt-rotor UAV during Transition |
| Mahammed, Haruna Hamza | 석사 2022–2024 | 현재 구성원(박사과정) | 석사: CubeSat Hyperspectral Imager for Earth Observation: Optimal Design, Performance Analysis, and Optomechanical Ruggedization |
| Zewge, Natnael S. | 박사 2020–2024 | 현재 구성원(박사후연구원) | 박사: Robust Multisensor Fusion for Autonomous Spacecraft Navigation during Final Approach for Mars Entry, Descent, and Landing |
| 김영재(Kim, Youngjae) | 석사 2022–2024 | 현재 구성원(박사과정) | 석사: DNN Regression-based Rotor Control Strategy for Coaxial Drone in Indoor Environment |
| 김한익 (Kim, Hanik) | 박사 2019–2024 |  | 박사: An Algorithm to Determine Collision Objects in Near-Keplerian Orbit Using Mathematical Modelling of Past Position Range |
| 박주호 (Park, Jooho) | 박사 2019–2024 | Senior Engineer, KARI, Daejeon, Korea (2012–) | 박사: Cascade Nonlinear Observer Design for Large Amplitude of Slosh Variables in Spacecraft Maneuver with Liquid Propellant Tank |
| 박준우 (Park, Junwoo) | 박사 2018–2024 · 석사 2016–2018 | Aerospace Engineer, Nearthlab, Daejeon, Korea (2024–) | 박사: A Study on Robust Particle Filtering in Terrain-referenced Navigation; 석사: Integrated Navigation of Interferometric Radar Altimeter-aided Terrain-referenced Navigation and Inertial Navigation |
| 임석재(Im, Sukjae) | 석사 2022–2024 | 현재 구성원(박사과정) | 석사: A Study on Target Defense Game Using Deep Reinforcement Learning in the Context of Unmanned Aerial Vehicle |
| Arshad, Muhammad Awais | 박사 2018–2023 | 현재 구성원(박사후연구원) | 박사: Motion Planning for Multirotor Aerial Robots in Indoor Environments Using Convex Optimization |
| Gadisa, Dinaol Zelalem | 석사 2021–2023 | 현재 구성원(박사과정) | 석사: Modeling and Parametric Performance Analysis of Field Emission Electric Propulsion |
| 김태영 (Kim, Taeyoung) | 박사 2016–2023 · 석사 2014–2016 | Staff Engineer, Samsung Electronics, Hwaseong, Korea (2023–) | 박사: A Study on Background Texture Enhancement of Simulated Infrared Images Using a Generative Model; 석사: Tightly Coupled SDINS/Star Sensor Integration Algorithm Based on Multiple Star Line of Sight Vectors |
| 김태호 (Kim, Taeho) | 박사후연구원 2023 · 박사 2017–2023 · 석사 2015–2017 | Senior researcher, Satellite Navigation Section, ETRI(Electronics and Telecommunications Research Institute), Daejeon, Korea (2026–) | 박사: GMM-based Adaptive Extended Kalman Filter Design for Satellite Attitude Estimation under Thruster Induced Disturbances; 석사: Improving the Attitude Determination Accuracy for Nanosatellites Using MEMS Sensors |
| 박한석(Park, Hanseok) | 석사 2021–2023 | NFO(Naval Flight Officer), Airwing 6th of R.O.K Navy (2013–) | 석사: Reinforcement Learning-Based Guidance Algorithm for UAV Autonomous Shipboard Landing under Heave Motion |
| 이재호(Lee, Jaeho) | 석사 2021–2023 |  | 석사: Mothership Delivery System using Reinforcement Learning |
| 임철수(Lim, Chulsoo) | 석사 2021–2023 | 현재 구성원(박사과정) | 석사: Deep Reinforcement Learning Using Time-Series Data for Collision Avoidance of UAVs in High-Speed Environments |
| 한해윤(Han, Haeyoon) | 석사 2021–2023 |  | 석사: Monocular Pose Estimation for Relative Navigation of Uncooperative Spacecraft |
| 홍경우 (Hong, Kyungwoo) | 박사 2018–2023 · 석사 2016–2018 | Senior Research Engineer, Future Innovation Research Team, Telepix, Daejeon, Korea (2023–) | 박사: Navigation with Visual Measurements in the form of Gaussian Mixture Models; 석사: Parallel Resampling Algorithm for GPU-Accelerated Particle Filter |
| 권동영 (Kwon, Dongyoung) | 박사 2016–2022 | Senior Engineer, Korea Aerospace Research Institute, Daejeon, Korea (2009–) | 박사: Sequential Convex Programming Approach for Real-Time Guidance During the Powered Descent Phase of Mars Landing Mission |
| 노준영(Noh, Junyoung) | 석사 2020–2022 |  | 석사: Terrain-following guidance based on model predictive control |
| 이다현(Lee, Dahyun) | 석사 2020–2022 | Researcher, Hyundai Motor Group, Uiwang, Korea (2022–) | 석사: Motion Planning of Space Manipulator for Capturing a Tumbling Non-cooperative Target using Reinforcement Learning |
| 장유동(Chang, Youdong) | 석사 2019–2022 | Junior Engineer, Hanwha Systems, Yongin, Korea (2022–) | 석사: Study on Neural Networks and Transfer Learning for Synthetic Aperture Radar Images Change Detection |
| 정명숙 (Jeong, Myeongsook) | 박사 2017–2022 | Senior Research Engineer, Korea Aerospace Research Institute, Daejeon, Korea (2011–) | 박사: Airport Aircraft Taxi Time Prediction Modeling using Machine Learning Approaches |
| 권혁준(Kwon, Hyeokjoon) | 석사 2019–2021 | Research Engineer, Nearthlab, Seoul, Korea (2021–) | 석사: Low-thrust spacecraft trajectory and guidance law design using reinforcement learning |
| 문민기(Mun, Mingi) | 석사 2019–2021 | 현재 구성원(박사과정) | 석사: H-infinity controller design for attitude control of a satellite with flexible appendages |
| 문성태 (Moon, SungTae) | 박사 2018–2021 | Engineer, Korea Aerospace Research Institute(KARI), Daejeon, Korea (2012–) | 박사: Development of energy-efficient swarming flight system based on the improved fair hungarian algorithm |
| 신종진 (Shin, Jongjin) | 박사 2017–2021 | Senior Researcher, Agency for Defense Development, Daejeon, Korea (2005–) | 박사: UAV path planning under dynamic threats using an improved PSO algorithm |
| 정성민(Jung, Sungmin) | 석사 2019–2021 | CPT, 901th Aviation Battalion ROK Army (2012–) | 석사: Flight control of a drone equipped with a pusher type actuator using fuzzy logic control approach |
| 정옥철 (Jung, Okchul) | 박사 2012–2021 | Senior Research Engineer, Korea Aerospace Research Institute, Daejeon, Korea (2006–) | 박사: Recurrent Neural Network Approach for Trajectory Prediction of Uncontrolled Space Object Reentry |
| Huang, Hsiu-Hsuan | 석사 2018–2020 | Research Engineer, National Chung-Shan Istitute of Science and Technology, Taoyuan, Taiwan (2020–) | 석사: GPU-accelerated Optimization of CubeSat Constellation Design Considering Cloud Cover Uncertainty |
| Marin Mikaël | 박사 2015–2020 | 현재 구성원(박사후연구원) | 박사: A Research On High-speed Star-tracker for Attitude Determination and Control System of Spacecrafts |
| 김기덕 (Kim, Kiduck) | 박사후연구원 2020 · 박사 2015–2020 · 석사 2013–2015 | Senior Researcher, Korea Aerospace Research Institute, Daejeon, Korea (2020–) | 박사: Patterned singular value approach for robust star pattern matching algorithm; 석사: New Star Identification Algorithm using Ring Projection Transform and Vector Sum Approach |
| 이성헌 (Lee, Seongheon) | 박사 2016–2020 · 석사 2014–2016 | 현재 구성원(박사후연구원) | 박사: Dynamic modeling and control of mechanical systems using machine learning approaches and their applications to a quadrotor UAV; 석사: Predictive Ground Collision Avoidance System for the Low-Level Terrain Flight |
| 이호성 (Lee, Hosung) | 박사 2016–2020 | Senior Engineer, Agency for Defense Development, Daejeon, Korea (2002–) | 박사: Design of efficient thrust management algorithm for variable thrust solid propulsion system with multi-nozzles |
| 정우영 (Jung, Wooyoung) | 박사 2014–2020 · 석사 2012–2014 | Research Engineer, Nearthlab, Daejeon, Korea (2021–) | 박사: Model predictive control based fault-tolerant control of multirotor UAV under actuator fault and failure; 석사: Three-Dimensional Vector Field Guidance Law to Control UAV |
| Umar Shafiq | 박사 2015–2019 |  | 박사: Design and Attitude Control of a Spinning OctaSail Solar Sailcraft |
| 곽필원(Kwak, Pilwon) | 석사 2017–2019 |  | 석사: Machine Learining for Automatic Target Recognition |
| 김동훈 (Kim, Donghun) | 박사 2015–2019 | Senior Engineer, Hanwha R&D, Daejeon, Korea (2005–) | 박사: Geomagnetic Matching Using Neural Network |
| 나윤주 (Na, YunJu) | 박사후연구원 2019 · 박사 2013–2019 · 석사 2011–2013 | Senior Researcher, Korea Aerospace Research Institute, Daejeon, Korea (2019–) | 박사: Vision-Based Relative Navigation Using Dual Quaternion for Spacecraft Proximity Operations; 석사: Development of Miniature Reaction Wheel Assembly and Attitude Control System for Nanosatellites |
| 목성훈 (Mok, Sung-Hoon) | 박사후연구원 2017–2019 · 박사 2010–2014 · 석사 2008–2010 | Post Doctoral Researcher, Faculty of Aerospace Engineering, TU Delft(Technische Universiteit Delft), Delft, Netherlands (2019.03–) | 박사: Impulsive Control Strategy for Spacecraft Formation Flying Using Orbital Drift; 석사: Impulsive Control of Satellite Formation Flying using Orbital Energy |
| 이상헌(Lee, Sanghun) | 석사 2015–2019 | Research Engineer, Koreanair R&D Center, Daejeon, Korea (2009–) | 석사: Research on Flare Path Generation for Improving Automatic Landing Accuracy of Fixed-Wing UAV |
| 이정신 (Lee, Jungshin) | 박사 2017–2019 · 석사 2002–2005 | Senior Engineer, Agency for Defense Development, Daejeon, Korea (2005–) | 박사: Study on Three-dimensional Terrain Referenced Navigation using Machine Learning; 석사: Singularity Avoidance by Cooperative Game Theory for Control Moment gyros |
| 김영주(Kim, Youngjoo) | 박사후연구원 2018 · 박사 2013–2018 · 석사 2011–2013 | Research Associate, Department of Automatic Control and Systems, The University of Sheffield, Sheffield, United Kingdom (2018.6–) | 박사: Ambiguous Measurement Update in Particle Filtering; 석사: Vision-Based UAV Navigation Aided by Terrain Elevation Map |
| 서현호 (Seo, Hyunho) | 박사 2011–2018 | Senior Research Engineer, Korea Aerospace Research Institute, Daejeon, Korea (2006–) | 박사: Steering Logic of Control Moment Gyros Using Artificial Potential |
| 임이랑 (Lim, Yeerang) | 박사후연구원 2018 · 박사 2011–2018 · 석사 2009–2011 | Guest Researcher, Institute of Aeronautics and Astronautics, Faculty V: Mechanical Engineering and Transport Systems, TUB(Technische Universitat Berlin), Berlin, Germany (2018.7–) | 박사: Robust Model Predictive Control for Satellite Formation Keeping with Eccentricity/Inclination Vector Separation; 석사: Attitude Determination and Control of Nano-Satellites |
| 장석원(Jang, Sukwon) | 박사 2013–2018 | Senior Research Engineer, ADD(Agency for Defense Development), Daejeon, Korea (2001–) | 박사: Digital Contour Model Based Terrain Referenced Navigation |
| 정유연 (Jung, Youeyun) | 박사후연구원 2016–2017, 2018 · 박사 2012–2015 | Senior Researcher, Korea Aerospace Research Institute, Daejeon, Korea (2018.12–) | 박사: Mars Precision Landing Guidance based on Model Predictive Control Approach |
| 홍진성 (Hong, Jinsung) | 박사 2012–2018 · 석사 2005–2007 | Senior Research Engineer, Agency for Defense Development, Daejeon, Korea (2008–) | 박사: Cooperative Circular Pattern Target Tracking Using Navigation Function; 석사: Vision-Based Autonomous Landing of a Rotocraft UAV |
| 강상욱 (Kang, Sangwook) | 박사 2012–2017 | Senior Research Engineer, Korea Aerospace Research Institute, Daejeon, Korea (2005–) | 박사: Adaptive Backstepping RBF Neural Network Controller Design for a Mars Lander |
| 김경희 (Kim, Kyunghee) | 박사후연구원 2016–2017 · 박사 2010–2016 | Space Parts Test Center, KTL(Korea Testing Laboratory), Jinju, Korea (2017–) | 박사: Dynamics and Adaptive Control for Spacecraft Relative Motion with Disturbances and Parametric Uncertainties |
| 김예현(Kim, Yehyun) | 석사 2015–2017 |  | 석사: Command Generation for High Gain Antenna on Lunar Orbiter to Communicate with Deep Space Network |
| 김종범 (Kim, Jongbum) | 박사 2013–2017 |  | 박사: Attitude Control of Small Satellite using only Magnetic Torquers |
| 박우상(Park, Woosang) | 석사 2015–2017 |  | 석사: Ground Test of Terrain Relative Navigatioin based on Crater Matching Algorithm for Precise Lunar Landing |
| 심태민(Shim, Taemin) | 석사 2015–2017 | 현재 구성원(박사과정) | 석사: Autonomous Landing of a UAV on a Moving Target Using Vector Field Guidance Approach |
| 이홍주(Lee, Hongju) | 석사 2014–2016 |  | 석사: Verification of Apollo Lunar Descent Guidance Algorithm using Multi-Rotor System |
| 조성은 (Jo, Sungeun) | 박사 2012–2016 |  | 박사: Development and analysis of high range precision and spatial resolutioin 3-dimentional imaging flash LIDAR using a polarization modulating Pockels cell and a micro-polarizer CCD camera |
| 탁기현(Tak, Kihyeon) | 석사 2014–2016 | Research Engineer, KAI, SaCheon, Korea (2016–) | 석사: Verification of Real-time Embedded Object Recognition and Tracking, and Localization System using a multirotor |
| 피재환 (Pi, Jaehwan) | 박사후연구원 2015–2016 · 박사 2011–2015 · 석사 2009–2011 | Research Engineer & Senior Research Engineer, KARI(Korea Aerospace Research Institute), Daejeon, Korea (2016–) | 박사: Trajectory Design for Improving Observability of Angles-Only Relative Navigation between Two Satelites; 석사: Relative Angles-Only Navigation for Satellite Relative Motion |
| 권재욱 (Kwon, Jaewook) | 박사 2012–2015 | Senior Research Engineer, Korea Aerospace Research Institute, Daejeon, Korea (2000–) | 박사: Virtual Trajectory Augmented Landing Control Based on Dual Quaternion for Lunar Lander |
| 김찬호(Kim, Chanho) | 석사 2013–2015 | Research Engineer, Hanwha, Daejeon, Korea (2015–) | 석사: Rotation Invariant Target Recognition with Semi-Supervised Learning for UAVs |
| 이영희(Lee, Yunghee) | 석사 2013–2015 |  | 석사: Genetic and Local Search Hybrid Algorithm Application for Initial Estimation of Solar Sailing Spacecraft Two Point Boundary Value Problem |
| 조수장 (Jo, Sujang) | 박사후연구원 2015 · 박사 2011–2015 · 석사 2009–2011 | Research Engineer & Senior Research Engineer, KARI(Korea Aerospace Research Institute), Daejeon, Korea (2016–) | 박사: Optimal Angular Velocity Estimation of Spacecraft Using Only Star Tracker Measurements; 석사: Gyroscope Calibration and Attitude Control using MRP-based Nonlinear Observer |
| 주정민 (Joo, Jungmin) | 박사 2010–2015 | Research Engineer&Senior Research Engineer, Korea Aerospace Research Institute, Daejeon, Korea (2004–) | 박사: Study on Ionospheric Correction and Irregularity Monitoring Method for Regional Navigation Satellite System |
| Tania Savitri | 석사 2012–2014 | Pubnative APAC Inc, Seoul, Korea (2015–) | 석사: Optimal Design of Grid Coverage by Satellite Constellation using Genetic Algorithm |
| 구성모(Ku, Sungmo) | 석사 2012–2014 | Research Engineer, KAI, SaCheon, Korea (2014–) | 석사: Solar sail Trajectory Optimization using Rapidly Converging Evolutionary Neural Network |
| 변수영(Byeon, Sooyung) | 석사 2012–2014 |  | 석사: Optimal Closed-Loop Launch Vehicle Ascent Guidance and Control under Disturbances |
| 이동진 (Lee, Dongjin) | 박사후연구원 2013–2014 · 박사 2008–2013 · 석사 2006–2008 | Adjunct Professor, Department of unmmaned aerial vehicle a, Han-Seo University, Taean, Korea (2014–) | 박사: Vision-aided Terrain Referenced Navigation for Unmanned Aerial Vehicles; 석사: Autorotation of an UAV Helicopter via Reinforcement Learning Control |
| 전병일(Jeon, Byoungil) | 석사 2012–2014 | Engineer, KAERI(Korea Atomic Energy Research Institute), Daejeon, Korea (2014–) | 석사: Ground Target Recognition using Support Vector Machine for UAVs |
| 김광수 (Kim, Kwangsoo) | 박사 2007–2013 | Research Engineer & Senior Research Engineer, Korea Aerospace Research Institute, Daejeon, Korea (2002–) | 박사: Adaptive Nonlinear Control for a Reusable Space Vehicle's Longitudinal Motion under Model Uncertainties and Physical Constraints |
| 박장성(Park, Jangseong) | 석사 2011–2013 | LIG Nex1 (2013–) | 석사: Vision-only Relative Navigation for formation flying and aerial refueling of UAVs |
| 백광열 (Baek, Kwangyul) | 박사 2008–2013 · 석사 2006–2008 | Research Engineer, ADD(Agency for Defense Development), Daejeon, Korea (2013–) | 박사: Adaptive Sparse Grid Quadrature Filter for Nonlinear Estimation; 석사: Vision-based Target Tracking Architecture of an Unmanned Aerial Vehicle |
| 이동헌 (Lee, Donghun) | 박사후연구원 2010–2013 · 박사 2007–2010 · 석사 2005–2007 | Research Engineer & Senior Research Engineer, KARI(Korea Aerospace Research Institute), Daejeon, Korea (2013–) | 박사: Fuel Optimal Earth-Moon Transfer Trajectories using Low-Thruster; 석사: Fuel Optimal, Low Thruster, Earth escape/Moon Capture Trajectories Design |
| 이주영(Lee, Juyoung) | 석사 2011–2013 |  |  |
| 임승한 (Lim, Seunghan) | 박사 2009–2013 · 석사 2007–2009 | Research Engineer, ADD(Agency for Defense Development), Daejeon, Korea (2013–) | 박사: Guidance Laws using Vector Field to Control Arrival Angle, Time, and Speed for UAVs; 석사: Waypoint Guidance of Cooperative UAVs for Intelligence, Surveillance and Reconnaissance |
| 전대근 (Jeon, Daekeun) | 박사 2010–2013 | Senior Research Engineer, Korea Aerospace Research Institute, Daejeon, Korea (2005–) | 박사: Asynchronous Multi-Sensor Target Tracking with Nonlinear Models |
| Masaud, Shehryar | 석사 2010–2012 | Samsung Electronics (2012–) | 석사: Study of Vision Based Pose Estimation for UAV. |
| 이대로 (Lee, Daero) | 박사후연구원 2011–2012 | Post Doctoral Researcher, New Mexico State University, Las Cruces, USA (2012–) |  |
| 이원석 (Lee, Wonseok) | 박사후연구원 2011–2012 · 박사 2007–2011 · 석사 2005–2007 | Research Engineer, ADD(Agency for Defense Development), Daejeon, Korea (2013–) | 박사: Cooperative Guidance of Multiple UAVs for Improved Target Tracking; 석사: Ducted Fan UAV System Analysis and Fuzzy Controller |
| 이일형 (Lee, Ilhyoung) | 박사 2005–2012 | Samsung Advanced Institute of Technology (2012–) | 박사: Line-of-sight Guidance Law for Phantom Track Generation Using Unmanned Aerial Vehicles |
| 장성호 (Chang, Sungho) | 박사 2007–2012 | Research Engineer & Senior Research Engineer, Korea Aerospace Research Institute, Daejeon, Korea (2000–) | 박사: Dynamic Characteristic Analysis and Fuzzy Control in the Full Conversion of a Smal Tiltrotor Unmanned Aerial Vehicle |
| 최문천(Choi, Mooncheon) | 석사 2010–2012 | Hyundai MOBIS (2012–) | 석사: Trajectory of Terrain-Following/Terrain -Avoidance Flight for Real-Time Implementation |
| 최윤혁 (Choi, Yoonhyuk) | 박사후연구원 2010–2012 · 박사 2006–2010 · 석사 2004–2006 | Research Engineer, ADD(Agency for Defense Development), Daejeon, Korea (2012–) | 박사: Impulsive Formation Control Using Orbital Energy and Angular Momentum Vector; 석사: Reaction Wheels Control Allocation for Reducing Input Command Noise |
| 최재혁(Choi, Jaehyuk) | 석사 2010–2012 | Nearthlab, Bundang, Korea (2015–) | 석사: Vision-Based Automatic Landing on a Moving Target for Unmanned Helicopters |
| Temirbolatov, Yerzhan | 석사 2009–2011 |  | 석사: Angular Velocity Estimation for GEO Satellite using Star Tracker Measurements |
| 김응현 (Kim, Eunghyun) | 박사 2004–2011 | Research Engineer & Senior Research Engineer, Korea Aerospace Research Institute, Daejeon, Korea (1996–) | 박사: Attitude-Independent Magnetometer Calibration Considering Magnetic Torque Coupling Effect |
| 명현삼 (Myung, Hyunsam) | 박사 2005–2011 · 석사 2001–2003 |  | 박사: Study on Nutation and spin Inversion Control of Spin-Stabilized Spacecraft; 석사: Nonlinear Predictive Attitude Control of Spacecraft Under External Disturbances |
| 용기력 (Yong, Kilyuk) | 박사 2005–2011 | Senior Research Engineer, Korea Aerospace Research Institute, Daejeon, Korea (1997–) | 박사: Hybrid Estimation of AOCS Sensor and Spacecraft Dynamic Parameter |
| 정영석 (Chung, Youngsuk) | 석사 2009–2011 | Nearthlab, Bundang, Korea (2015–) | 석사: Improvement Study of B-Plane Method for Trajectory Correction Maneuver of Lunar Exploration (Major Advisor: Hyochoong Bang, Co-Advisor : Park, Chul) |
| 조동현 (Cho, Donghyun) | 박사 2007–2011 | Senior Research Engineer, Korea Aerospace Research Institute, Daejeon, Korea (2011–) | 박사: Spacecraft Trajectory Correction Maneuver Design using the Improved B-plane Targeting Method |
| 최인호 (Choi, Inho) | 박사 2006–2011 | Research Engineer & Senior Research Engineer, Korea Aerospace Research Institute, Daejeon, Korea (1996–) | 박사: Adaptive Non-linear Flight Controllers Design for a Quadrotor UAV |
| 강태화 (Kang, Taehwa) | 석사 2008–2010 | Army Aviation Officer Pilot(AH-1S) (2006–) | 석사: Vision-based Ground Target Tracking using Guidance Filter for a Rotary UAV |
| 박영웅 (Park, Youngwoong) | 박사 2002–2010 | Research Engineer, Korea Aerospace Research Institute, Daejeon, Korea (1995–) | 박사: Attitude Controller Design for Orbital Target Tracking of Geostationary Satellite under Avoidance Constraint |
| 윤효상 (Yoon, Hyosang) | 석사 2008–2010 | Research Engineer, Avionics Group, Satreci, Daejeon, Korea (2010–) | 석사: Star Recognition Algorithm in Dynamic Environment |
| 은연주 (Eun, Yeonju) | 박사 2005–2010 · 석사 2002–2004 | Senior Research Engineer, Korea Aerospace Research Institute, Daejeon, Korea (2009–) | 박사: Optimal Scheduling of Arrival Flights in a Terminal Airspace; 석사: Cooperative Control of Multiple UCAVs for SEAD |
| 이광현 (Lee, Kwanghyun) | 박사 2003–2010 | Research Engineer & Senior Research Engineer, ADD(Agency for Defense Development), Daejeon, Korea (1991–) | 박사: Self-Reconfigurable Flight Control Via Control Allocation For Overly Actuated System |
| 정보영 (Jeong, Boyoung) | 석사 2008–2010 | LIG Nex1 (2010–) | 석사: Terrain Aided Inertial Navigation for Precise Planetary Landing |
| 김해동 (Kim, Haedong) | 박사 2005–2009 | Research Engineer & Senior Research Engineer, Korea Aerospace Research Institute, Daejeon, Korea (2000–) | 박사: Optimal Design of Sparse Satellite Coverage Constellations Using Genetic Algorithms |
| 이준호(Lee, Joonho) | 석사 2007–2009 | Research Engineer, Avionics Group, Satreci, Daejeon, Korea (2006–) | 석사: Small Satellite Agile Maneuver Using Control Moment Gyroscope and Thruster |
| 이현재 (Leeghim, Henzeh) | 박사후연구원 2007–2009 · 박사 2002–2007 | Associate Professor, Department of aerospace engineering, Chosun University, Gwangju, Korea (2012–) | 박사: Optimal Steering Laws for Control Moment Gyros |
| 임형철 (Lim, Hyungchul) | 박사 2003–2009 | Research Engineer, GPS Research Group, Korea Astronomy Observatory, Daejeon, Korea (2000–) | 박사: Adaptive Control for Satellite Formation Flying with Thrust Uncertainties |
| Aorpimai, Manop | 박사후연구원 2008 |  |  |
| 노은정 (Roh, Eunjung) | 석사 2006–2008 | KIAT(Korea Institute of Aerospace Technology), Koreanair Aerospace Division, Daejeon, Korea (2008–) | 석사: Design of Control Laws for TCM on Interplanetary Missions |
| 박종오 (Park, Jongoh) | 박사후연구원 2005–2008 | Adjunct Professor, Department of Electronics Engineering, Dong-A University, Busan, Korea (2008–) |  |
| 서인호 (Seo, Inho) | 박사 2004–2008 | Research Engineer & Senior Research Engineer, SaTReC(Satellite Technology Research Center), KAIST, Daejeon, Korea (2000.12–) | 박사: Nonlinear Momentum Transfer Control of a Gyrostat with a Discrete Damper using Neural Networks |
| 이상종 (Lee, Sangjong) | 박사 2004–2008 | Research Engineer & Senior Research Engineer, KARI(Korea Aerospace Research Institute), Daejeon, Korea (1996–) | 박사: Trajectory Optimization and Nonlinear Tracking Control for Stratospheric Airship Platform |
| 이영구 (Lee, Younggu) | 석사 2006–2008 | NFO(Naval Flight Officer), Airwing 6th of R.O.K Navy (2002–) | 석사: Relative Position and Attitude Estimation of Spacecraft in Formation Flying Using Kalman filters and Particle Filter |
| 오충석(Oh, Choongsuk) | 박사 2003–2007 · 석사 2001–2003 | Research Engineer, KARI(Korea Aerospace Research Institute), Daejeon, Korea (2007.8–) | 박사: Adaptive Control for the Attitude Maneuver of Flexible Spacecraft Under Disturbance Sources; 석사: An Experimental Study on Attitude Control of Spacecraft Using Two-Axis Hardware Testbed |
| 김부성 (Kim, Boosung) | 석사 2004–2006 | Hyundai MOBIS (2006–) | 석사: Research for Automated UAV Path Planning |
| Somasundar Kannan | 석사 2003–2005 |  | 석사: Nonlinear control of small scale Rotary wing Unmanned Aerial Vehicle(R-UAV) using Backstepping |
| 나채진 (Na, Chaejin) | 석사 2003–2005 |  | 석사: Parameter Estimation of Helicopter Model Using Unscented Kalman Filter |
| 오세붕 (Oh, Seboung) | 석사 2003–2005 | LG Electronics, Korea (2005.3–) | 석사: Study on Satellite Vibration Control using Adaptive Control Scheme |
| 한수철 (Han, Sucheol) | 석사 2003–2005 | Pilot, Korea Air Force (1997–) | 석사: Proportional Navigation-Based Optimal Collision Avoidance for UAVs |
| 김근태 (Kim, Kuntae) | 석사 2002–2004 | Hyundai MOBIS (2004.3–) | 석사: Application of the Vision-Based Navigation and Control for Autonomous Spacecraft Docking |

## 최근 논문 목록 (2021–2026)

누리집 International Journals·Domestic Journals·International Conferences·Domestic Conferences 네 페이지(머리에 2025년 10월 9–10일 갱신 표기)의 2021–2025년 연도 구역에 실린 222편이다. 국제 학술지 48편(160–207번), 국내 학술지 16편(83–98번), 국제 학회 논문 66편(203–268번), 국내 학회 논문 92편(286–377번)이며, 네 페이지 모두 2026년 구역은 없다. 연도는 페이지의 연도 구역이고, 연도마다 국제 학술지, 국내 학술지, 국제 학회, 국내 학회 순으로 적었다. 국내 학술지·학회 논문은 끝에 (국내)를 붙였다. 제목·저자·학술지와 학회 이름은 누리집 표기 그대로이고, 제목에 따옴표가 없는 항목은 누리집의 한 줄을 그대로 적었다. 2021년 구역의 국제 학술지 163번은 누리집이 「submitted to」로 적은 투고 논문이라 끝에 「(투고)」를 붙여 출판된 논문과 구분했다. 같은 논문이 두 연도 구역에 함께 실린 경우(국제 학술지 169번과 204번, 170번과 179번)도 누리집 목록대로 각각 적었다.[^ij][^dj][^ic][^dc]

**2025**

- Junwoo Park, and Hyochoong Bang. "Contours-seeking Proposal Density Particle Filter and Resilient Terrain-referenced Navigation". *IEEE Transactions on Aerospace and Electronic Systems, 2025.07*.
- Jayden Dongwoo Lee, Donghoon Seo, Jongho Shin, Hyochoong Bang. "Fast real-time state-of-health estimation method for lithium-ion battery using sparse identification of nonlinear dynamics". *Journal of Intelligent & Robotic Systems, v.111, no.3, 2025.08*.
- Mohammed Irfan Rashed, Hyochoong Bang. "Enhanced stability of cislunar-based small satellite constellations via Preferential-EKF". *IEEE Access, v.13, 2025.07*.
- Jayden Dongwoo Lee, Lamsu Kim, Kwangwoo Jang, Seongheon Lee, Hyochoong Bang. "Feedback linearization-based model reference adaptive control for multirotor UAVs under uncertainties from fuel and payload". *Proceedings of the Institution of Mechanical Engineers, Part G: Journal of Aerospace Engineering, v.239, no.9, 2025.07*.
- Jayden Dongwoo Lee, Youngjae Kim, Lamsu Kim, Natnael S. Zewge, Hyochoong Bang. "Sparse online Gaussian process regression-based robust nonlinear dynamic inversion for multirotor with forward-flight ground effect". *Aerospace Science and Technology, v.162, 2025.06*.
- Natnael S. Zewge, Hyochoong Bang. "Fast multi-constellation GNSS satellite selection: convex and mixed-integer programming approaches". *IEEE Transactions on Vehicular Technology, v.74, no.6, 2025.06*.
- Jayden Dongwoo Lee, Youngjae Kim, Yoonseong Kim, Hyochoong Bang. "Sparse identification of nonlinear dynamics-based model predictive control for multirotor collision avoidance". *IET Control Theory & Applications, v.19, no.1, 2025.06*.
- Mohammed Irfan Rashed, Hyochoong Bang. "In-orbit target-based autonomy for enhanced stability of the small satellite constellations in cislunar space". *International Journal of Aeronautical and Space Sciences, 2025.06*.
- Juhyeong Park, Jayden Dongwoo Lee, Hyochoong Bang. "Vibration suppression adaptive prescribed performance control for flexible spacecraft with uncertain moment of inertia". *Acta Astronautica, v.235, 2025.05*.
- Han-Ik Kim, Hyochoong Bang. "Trajectory linearisation of relative motion to elliptical orbit target using Tschauner–Hempel equation". *International Journal of Aeronautical and Space Sciences. 2025.05*.
- Snyoll Oghim, Junwoo Park, Hyochoong Bang, Henzeh Leeghim. "Deep reinforcement learning-based attitude control for spacecraft using control moment gyros". *Advances in Space Research, v.75, no.1, 2025.01*.
- Dain Yoon, Kyungmi Na, Jayden Dongwoo Lee, Changhun Lee, Hyochoong Bang. "Practical fault-tolerant control allocation based on attainable control set analysis for a coaxial dodecacopter". *Control Engineering Practice, v.156, 2025.01*.
- Sungjoong Kim, Junwoo Park, Hyochoong Bang. "Enhanced terrain-referenced navigation through adaptive radar altimeter error estimation with Monte Carlo sampling". *International Journal of Aeronautical and Space Sciences, v.26, no.4, 2025.01*.
- 이종국, 송태성, 김민영, 송덕기, 강정민, 김경민 (LIG Nex1), 오승렬, 박주형, 방효충 (KAIST), 김용복, 석병석 (KARI). "50-200kg급 소형 위성용 '제어 모멘트 자이로스코프' 개발". *한국항공우주학회지, 2025.02 (국내)*.
- Dinaol Gadisa and Haruna H. Mohammed and Hyochoong Bang. "Performance Characterization of FEEP Thruster using Various Propellants". *39th International Electric Propulsion Conference (IEPC 2025), 2025. 09. 14 ~ 09. 19*.
- Man Jun Koh and Natnael. S. Zewge and Hyochoong Bang. "Optimal Asteroid Selection in Vision Based Deep Space Navigation". *AAS/AIAA Astrodynamics Specialist Conference 2025, 2025. 08. 10 ~ 08. 14*.
- Hyeonmin Kim and Jayden Dongwoo Lee and Bohyun Chang and Hyochoong Bang. "Adaptive Sliding Window Factor Graph Optimization For Enhanced UWB_INS Integrated UAV Localization". *EUCASS 2025, 2025. 06. 30 ~ 07. 04*.
- Yujin Lee and Juhyeong Park and Jayden Dongwoo Lee and Hyochoong Bang. "Prescribed Performance Attitude Takeover Control of Postcapture Combined Spacecraft with Time-Delay Estimation". *EUCASS 2025, 2025. 06. 30 ~ 07. 04*.
- Dohyun Kim and Jayden Dongwoo Lee and Hyochoong Bang and Jungho Bae. "Reinforcement Learning-based Fault-Tolerant Control for Quadrotor with Online Transformer Adaptation". *IEEE International Conference on Robotics & Automation (ICRA 2025), 2025. 06. 01 ~ 06. 06*.
- Chulsoo Lim, Hyungjoo Ahn, Seongheon Lee, Natnael S. Zewge, Bohyun Chang and Hyochoong Bang. "Dual-Augmented Time-Series Data for Deep Reinforcement Learning in High-Speed Collision Avoidance of UAV". *AIAA SCITECH 2025 Forum. 2025*.
- Jiho Han, Jayden Dongwoo Lee, and Hyochoong Bang. "Dual Virtual Target-Based Polynomial Curve Fitting Guidance for Urban Air Mobility Path Following". *AIAA SCITECH 2025 Forum. 2025. 01. 06 ~ 10*.
- Kangsan Kim, Bohyun Chang, and Hyochoong Bang. "Infra-Red Scene Simulation Framework for Space-Based Hypersonic Vehicle Observation". *AIAA SCITECH 2025 Forum. 2025. 01. 06 ~ 10*.
- Bohyun Chang and Jayden Dongwoo Lee and Hyochoong Bang. "Key Feature Detection for Rendezvous and Proximity Operation Using BRDF Segmentation Algorithm". *AIAA SCITECH 2025 Forum, 2025. 01. 06 ~ 10*.
- 임철수, 방효충. "무인기간 통신 가능 거리 고려하의 멀티에이전트 강화학습". *한국군사과학기술학회 종합학술대회 2025 (국내)*.
- 김성중, 방효충. "잔차 정규성 기반의 적응형 모드 천이를 적용한 지형참조항법용 IMM 필터링". *한국군사과학기술학회 종합학술대회 2025 (국내)*.
- 박상욱, 이동우, 김영재, 임철수, 방효충. "저가, 소모성 무인편대군의 공중 표적추적을 위한 센서 융합 연구". *한국군사과학기술학회 종합학술대회 2025 (국내)*.
- 고만준, Natnael S. Zewge, 이동우, 방효충, 홍경우, 원동식, 고동욱. "심우주 탐사를 위한 최적 삼각측량 기반 광학 항법 연구". *항공우주학회 우주학술대회 2025 (국내)*.
- 박태윤, 김남수, 방효충, 강상욱. "지형참조항법을 활용한 화성 EDL 비행체의 정밀항법필터 설계 연구". *항공우주학회 우주학술대회 2025 (국내)*.
- 김남수, 박태윤, 방효충, 오승렬, 강상욱. "화성 EDL 비행체의 정밀착륙을 위한 항법 시스템에 대한 연구". *항공우주학회 우주학술대회 2025 (국내)*.
- 이호선, 이동우, 김동현, 이상민, 류태규, 방효충. "이단계 칼만 필터 기반 분산형 전기 추진 비행체의 구동기 고장 진단 및 고장 허용 제어". *항공우주시스템공학회 춘계학술대회 2025 (국내)*.
- ARSHAD, 김태호, 방효충. "합성 적외선 이미지의 사실감 향상을 위한 U-Net과 PatchGAN 기반 적대적 정제에 대한 연구". *항공우주학회 춘계학술발표회 2025 (국내)*.
- 이유진, 박주형, 이동우, 방효충. "시간 지연 추정 기법을 이용한 결합 우주비행체의 성능 보장 자세 제어". *항공우주학회 춘계학술발표회 2025 (국내)*.
- 김현민, 이동우, 장보현, 방효충. "거리 기반 적응형 슬라이딩 윈도우 팩터그래프 UAV 위치추정 기법". *항공우주학회 춘계학술발표회 2025 (국내)*.
- 강민우, 이동우, 윤성훈, 방효충. "물리정보-SINDy를 통한 고정익 항공기의 공력 모델링 및 슬라이딩 모드 외란 관측기를 통한 강인한 비선형 모델예측제어 기법 설계". *항공우주학회 춘계학술발표회 2025 (국내)*.
- 한지호, 방효충. "이중 가상 타겟을 이용한 이차다항식 곡선 피팅 유도 기법의 수학적 분석". *항공우주학회 춘계학술발표회 2025 (국내)*.
- 장보현, 김강산, 이호형, 방효충. "미지의 우주물체의 형상복원 및 상대항법을 위한 LiDAR 포즈그래프 최적화 기법 연구". *항공우주학회 춘계학술발표회 2025 (국내)*.
- 임철수, 방효충. "통신거리를 고려한 달 탐사 군집 로버의 다중 에이전트 강화 학습". *항공우주학회 춘계학술발표회 2025 (국내)*.
- 박태윤, 김남수, 이호형, 장보현, 방효충. "일괄처리방식 TERCOM을 활용한 행성 착륙선의 INS/TRN 복합항법연구". *항공우주학회 춘계학술발표회 2025 (국내)*.

**2024**

- Junwoo Park, Hyochoong Bang. "Sparse instantiation of bias nodes for factor graph-based terrain-referenced navigation". *International Journal of Control, Automation, and Systems, v.22, no.11, 2024.11*.
- Lamsu Kim, Jayden Dongwoo Lee, Seongheon Lee, Hyochoong Bang. "Fault detection for re-initialization of online Gaussian process regression using kernel linear independence test". *International Journal of Control, Automation, and Systems, v.22, no.11, 2024.11*.
- Suk Hyun Yeo, Dinaol Gadisa, Hideaki Ogawa, Hyochoong Bang. "Multi-objective design optimization and physics-based sensitivity analysis of field emission electric propulsion for CubeSat platforms". *Aerospace Science and Technology, v.154, 2024.11*.
- Jayden Dongwoo Lee, Lamsu Kim, Seongheon Lee, Hyochoong Bang. "Data-driven fault diagnosis of nonlinear systems with parameter uncertainty using deep Koopman operator and weighted-window extended dynamic mode decomposition". *International Journal of Control, Automation, v.22, no.11, 2024.11*.
- Seungryeol Oh, Hyochoong Bang. "Time-optimal guidance laws using a frequency-domain approach for spacecraft rendezvous". *International Journal of Aeronautical and Space Sciences, v.26, 2024.11*.
- Jayden Dongwoo Lee, Sukjae Im, Lamsu Kim, Hyungjoo Ahn, Hyochoong Bang. "Data-driven fault detection and isolation for multirotor system using Koopman operator". *Journal of Intelligent & Robotic Systems, v.110, article 128, 2024.09*.
- Mohammed Irfan Rashed, Hyochoong Bang. "A study of cislunar-based small satellite constellations with sustainable autonomy". *Aerospace, v.11, no.9, 2024.09*.
- Jamal Ahmed, Awais Arshad, Hyochoong Bang, Yoonhyuk Choi. "Transformer network-aided relative pose estimation for non-cooperative spacecraft using vision sensor". *International Journal of Aeronautical and Space Sciences, 2024.07*.
- Lamsu Kim, Jayden Dongwoo Lee, Natnael S. Zewge, Hyochoong Bang. "Gaussian process-based state derivative estimator with temporal input in incremental flight control design". *Aerospace Science and Technology, 2024.03*.
- Kwangwoo Jang, Hyochoong Bang, Yoonsoo Kim. "Mitigating time-delay in nonlinear dynamics inversion for multirotor unmanned aerial vehicles". *Journal of Guidance, Control, and Dynamics, v.47, 2024.03*.
- Junwoo Park, Sungjoong Kim, Kyungwoo Hong, Hyochoong Bang. "Visual semantic context and map-based rotation-invariant efficient estimation of position and heading". *Navigation: Journal of the Institute of Navigation, v.71, issue 1, 2024.03*.
- Seungryeol Oh, Yoonjae Kim, Hyochoong Bang, Deoksu Lim, Junyoung Ko. "SAR image generation method using DH-GAN for automatic target recognition". *Sensors, v.24, 2024.01*.
- Junwoo Park, Hyochoong Bang. "Data-driven hazard-avoidance landing of parafoil: a deep reinforcement learning approach". *AIAA Journal of Aerospace Information Systems, v.21, no.1, 2024.01*.
- 김태호, 방효충, 김강산. "Grad-CAM 기반의 설명가능한 인공지능을 사용한 합성 이미지 개선 방법". *한국군사과학기술회지, 2024.12 (국내)*.
- 이호형, 안형주, 임석재, 장광우, 박준우, 임철수, 한지호, 허준회, 한유근, 방효충. "단안 카메라와 6축 관성 센서를 이용한 회전하는 정지 플랫폼의 자세 추정 기법". *한국항공우주학회지, 2024.09 (국내)*.
- 이동우, 임철수, 홍경우, 방효충, 임동주, 박대성, 송기훈. "지형 추종을 위한 모델예측제어와 비선형 외란관측기를 이용한 백스테핑 제어기법 설계". *한국군사과학기술회지, 2024.08 (국내)*.
- Natnael. S. Zewge and Hyochoong Bang. "Outlier-Resilient Fusion of X-ray Pulsar and Optical Measurements for Autonomous Spacecraft Navigation". *ICCAS 2024, 2024. 10. 29 ~ 11. 01*.
- Natnael. S. Zewge and Hyochoong Bang. "Robust Centroid and Apparent Diameter Extraction via Convex Optimization for Optical Spacecraft Navigation". *IEEE SENSORS 2024, 2024. 10. 20 ~ 23*.
- Juhyeong Park and Jayden Dongwoo Lee and Hyochoong Bang. "Adaptive Prescribed Performance Attitude Control for Flexible Spacecraft Using Observer". *IAC 2024, 2024. 10. 14 ~ 18*.
- Hyeongjoo Ahn and Hyochoong Bang. "Medial Axis Transformation-Based Convex Model Predictive Control for Multirotor Indoor Autonomous Flight with Fixed Altitude". *ICAS 2024, 2024. 09. 09 ~ 13*.
- Mohammed Irfan Rashed and Hyochoong Bang. "Preferential Autonomy-based Ground Operations for Small Satellite Constellations in CisLunar Space". *AIAA SCITECH 2024 Forum, 2024. 01. 08 ~ 12*.
- 김현민, 이동우, 방효충. "미식별 선박 탐지를 위한 국내·외 RF 감시·정찰 위성 기술 개발 사례 연구". *항공우주학회 추계학술발표회 2024 (국내)*.
- 이동우, 김영재, 방효충. "삼중화 비행제어 컴퓨터를 위한 SINDy기반의 모델 예측 보팅 알고리즘 설계". *항공우주학회 추계학술발표회 2024 (국내)*.
- 임철수, 이동우, 방효충. "Interacting Multiple Model 기반 활용한 탐사 로버의 항법 센서 결함 탐지 연구". *항공우주학회 추계학술발표회 2024 (국내)*.
- 김강산, 장보현, 방효충. "위성 기반 적외선 센서를 위한 극초음속 표적 모델링 기법". *항공우주학회 추계학술발표회 2024 (국내)*.
- 장보현, 이동우, 방효충. "우주물체 능동제어위성 개발을 위한 구간별 상대항법 개념설계". *항공우주학회 추계학술발표회 2024 (국내)*.
- 이동우, 방효충. "SINDy를 이용한 데이터 기반의 센서 및 구동기 고장 진단 및 분리". *항공우주학회 추계학술발표회 2024 (국내)*.
- 한지호, 이동우, 방효충. "바람 환경에서의 도심항공교통(UAM) 경로 추종 유도". *항공우주학회 추계학술발표회 2024 (국내)*.
- 이호선, 방효충. "오픈 루프 리액션 휠을 추가한 수직이착륙 테일시터 무인기의 천이 비행 종축 제어". *항공우주학회 추계학술발표회 2024 (국내)*.
- Habtamu Mengistu, Hyochoong Bang. "Enhancing Autonomous Air Combat Maneuver Decision-Making Using Noisy-Dueling DDQN". *항공우주학회 추계학술발표회 2024 (국내)*.
- 김영재, 장광우, 이동우, 이호선, 방효충. "삼중화 비행제어컴퓨터를 위한 FPGA 보팅 알고리즘 설계 및 구현". *항공우주학회 추계학술발표회 2024 (국내)*.
- 이유진, 장보현, 방효충. "우주비행체 근접 운용 시나리오 모사를 위한 랩 스케일 지상 테스트베드 개발". *항공우주학회 추계학술발표회 2024 (국내)*.
- 이동우, 방효충. "멀티로터를 위한 SINDy 기반의 비선형 외란 관측기 설계". *제39회 제어·로봇·시스템학회 학술대회 2024 (국내)*.
- 이동우, 김영재, 김남수, 방효충. "지면효과를 갖는 멀티로터를 위한 Spare Online Process Regression 기반의 고도제어 기법". *제39회 제어·로봇·시스템학회 학술대회 2024 (국내)*.
- Irfan Rashed, 방효충. "자율성 개발 및 유지 – 지속 가능한 군를 형성하는 조소형 위성을 위한 뉴스페이스 챌린지". *항공우주학회 우주학술대회 2024 (국내)*.
- 김남수, 이호형, 박태윤, 방효충, 김재인, 강상욱. "화성정밀착륙을 위한 화성착륙선의 동역학 시뮬레이션 및 칼만필터 설계 연구". *항공우주학회 우주학술대회 2024 (국내)*.
- 이동우, 방효충. "가우시안 프로세스 회귀를 이용한 멀티로터의 데이터 기반의 고장 진단". *항공우주시스템공학회 춘계학술대회 2024 (국내)*.
- 이동우, 김영재, 방효충. "삼중 비행제어컴퓨터 및 센서를 위한 계층적 보팅 알고리즘 개발". *항공우주시스템공학회 춘계학술대회 2024 (국내)*.
- Muhammad Awais Arshad, Taeho Kim, Hyochoong Bang. "Improved Adversarial Networks for Synthetic Infrared Image Refinement". *대한전기학회 춘계학술대회 2024 (국내)*.
- 장보현, 김한익, 방효충. "라이다 강도 측정값과 재질의 BRDF 특성을 이용한 인공위성의 표면 재질 추정 및 분할". *항공우주학회 춘계학술발표회 2024 (국내)*.
- 김채현, 김성준, 문민기, 최한림, 방효충. "교차 관측 주기 최소화를 위한 이종 고기동 위성 임무 스케줄링". *항공우주학회 춘계학술발표회 2024 (국내)*.
- 한지호, 이동우, 방효충. "이중 가상 타겟을 이용한 무인기의 경로 추종 유도". *항공우주학회 춘계학술발표회 2024 (국내)*.
- 김강산, 김시현, 장보현, 방효충. "극초음속 표적 탐지 및 추적알고리즘을 위한 적외선 이미지 시뮬레이터". *항공우주학회 춘계학술발표회 2024 (국내)*.
- 박주형, 이동우, 김태호, 방효충. "유연 우주비행체의 성능 보장 자세 제어에 관한 연구". *항공우주학회 춘계학술발표회 2024 (국내)*.
- 임철수, 장보현, 김강산, 임석재, 김영재. "저궤도에서의 단안 EO 카메라와 기반 모델을 이용한 탄도 미사일 검출 및 초기 낙하 궤도 추정". *항공우주학회 춘계학술발표회 2024 (국내)*.
- 강민우, 이동우, 윤성훈, 방효충. "SINDy를 사용한 고정익 항공기의 세로축 비선형 모델예측제어 기법 설계". *항공우주학회 춘계학술발표회 2024 (국내)*.
- 이동우, 임석재, 방효충. "SINDy를 이용한 쿼드로터의 데이터 기반 모델링 및 고장진단". *항공우주학회 춘계학술발표회 2024 (국내)*.
- 이호선, 김강산, 방효충. "움직이는 지상 차량에서의 운용을 고려한 수직이착륙 테일 시터 무인기 속도 제어 기법 설계". *항공우주학회 춘계학술발표회 2024 (국내)*.
- 김남수, 방효충. "가우시안 과정 회귀 기반 증분동역학 비선형 제어기 분석". *항공우주학회 춘계학술발표회 2024 (국내)*.

**2023**

- J. Liao and H. Bang. "Transition Nonlinear Blended Aerodynamic Modeling and Anti-Harmonic Disturbance Robust Control of Fixed-Wing Tiltrotor UAV". *Drones*.
- T. Kim, N.S. Zewge, H. Bang, H. Yoon. "GMM-Based Adaptive Extended Kalman Filter Design for Satellite Attitude Estimation under Thruster-Induced Disturbances". *Sensors, Vol. 23, 2023*.
- N.S. Zewge, H. Bang. "A distributionally robust fusion framework for autonomous multisensor spacecraft navigation during entry phase of mars entry, descent, and landing". *Remote Sensing, Vol. 15, 2023*.
- M.A. Arshad, J. Ahmed, H. Bang. "Quadrotor path planning and polynomial trajectory generation using quadratic programming for indoor environments". *Drones, Vol. 7, 2023*.
- M.I. Rashed, H. Bang. "A study of cognitive computing in nanosatellite constellations for synergic autonomy in CisLunar space". *Advances in Space Research, 2023*.
- J. Park, H. Bang, K. Park, S. Lee. "Cascade nonlinear observer design for large amplitude of slosh variables in spacecraft maneuver with liquid propellant tank". *Acta Astronautica 213, pp. 35-48, 2023*.
- 이호형, 김남수, 이동우, 장광우, 조경용, 박태산, 방효충. "속도 변화를 고려한 자폭형 고정익 무인기의 관측각 제어 기반 종말 유도 법칙 설계". *한국항공우주학회지, 2023 (국내)*.
- 진재현, 이창훈, 방효충, 김영원, 박준우, 김태훈. "탄도탄 방어용 직격 요격미사일의 최적 형상설계를 위한 성능분석". *한국항공우주학회지, Journal of Institute of Control, Robotics and Systems, 2023 (국내)*.
- 이호형, 김남수, 이동우, 장광우, 조경용, 박태산, 방효충. "속도 변화를 고려한 자폭형 고정익 무인기의 관측각 제어 기반 종말 유도 기법 설계". *한국항공우주학회지, 2023 (국내)*.
- K Jang, KW Hong, H Bang, SI Lee, J Jeon, K Song. "Computational Guidance Algorithm for Terrain Following Using Model Predictive Path Integral Method". *한국항공우주학회지, 2023 (국내)*.
- H Lee, L Kim, D Lee, K Jang, K Jo, T Park, H Bang. "Development of Look Angle Guidance Law for Loitering Munition Under Velocity Change". *한국항공우주학회지,2023 (국내)*.
- K Hong, S Kim, H Bang, K Seo, J Jeon. "Accelerated Algorithm for Generating Measurements of Terrain Following Radar Based on Digital Elevation Models". *한국항공우주학회지, 2023 (국내)*.
- K Hong, S Kim, H Bang, J Jeon, W Choi. "Trajectory Generation Algorithm for Terrain Following based on Terrain Elevation". *한국항공우주학회지, 2023 (국내)*.
- Mohammed I. Rashed and H. Bang. "Autonomous Mission and Operations Planning for Small-satellite Constellations". *17th Annual SpaceOps, 2023. 03. 06*.
- J. Lee, and H. Bang. "Reinforcement Learning-based Nonlinear Disturbance Observer for UAV with Parametric Uncertainty and Unmodeled Dynamics". *AIAA SciTech Forum 2023, 2023. 01. 23 ~ 27*.
- J. Lee, J. Park, D. Lee, and H. Bang. "Sequential Cooperative Reinforcement Learning of Mothership Routing Problem". *AIAA SciTech Forum 2023, 2023. 01. 23 ~ 27*.
- K. Hong, Y. Kim, and H. Bang. "A New Parallel Resampling Algorithm for GPU-Accelerated Particle Filter". *AIAA SciTech Forum 2023, 2023. 01. 23 ~ 27*.
- J.Park and H. Bang. "Factor Graph Optimization for Integration of Inertial and Terrain-referenced Navigation". *AIAA SCITECH 2024 Forum, 2023*.
- J.Park and H. Bang. "Tight Integration of Inertial and Terrain-referenced Navigation under Biased Odometry and Measurements via Factor Graph Optimization". *The 23rd International Conference on Control, Automation and Systems (ICCAS 2023), 2023*.
- Paulo Kemper, Mikael Marin, Hyosang Yoon. "Using Star Density Tessellation to Evaluate the Impact of a Star Tracker’s Field of View Shape on its Performance". *AIAA SciTech, 2023*.
- Paulo Kemper; Mikael Marin; Hyosang Yoon. "Analysis of the impact of star catalog thinning on resource-limited star trackers performance". *CubeSat Symposium 2023*.
- D. Kim, S. Lee, J.D. Lee, H. Lee and H. Bang. "Guided Exploration Reinforcement Learning for UAV Pursuit-Evasion Games". *International Conference on Robot Intelligence Technology and Applications, 2023*.
- J.D. Lee, L. Kim. H. Lee and H. Bang. "Data-Driven Fault Detection and Identification of Nonlinear Systems Using Weighted Window Extended Dynamic Mode Decomposition". *2023 23nd International Conference on Control, Automation and Systems (ICCAS), 2023*.
- L Kim, JD Lee, H Bang. "Fault Diagnosis Using Kernel Linear Independence Test in Reproducing Kernel Hilbert Space". *2023 23rd International Conference on Control, Automation and Systems, 2023*.
- MI Rashed and H. Bang. "Normalizing In-Orbit Anomalies and Retaining Stability Using Preferential-EKF for Autonomous Small Satellite Constellations in CisLunar Space". *2023 23rd International Conference on Control, Automation and Systems, 2023*.
- Yong-Ha Hwang, Kwangwoo Jang, Hyungjoo Ahn, Hyochoong Bang, Jae-Hung Han. "In-Flight Structural Test of a Hoverbike Using Fiber Optic Sensors". *Smart Materials, Adaptive Structures and Intelligent Systems, 2023*.
- Mohammed Irfan Rashed, Hyochoong Bang, Nate McCoun. "Parametric Assessment to Fully Deploy Autonomous Small Satellite Constellations for Cislunar Space". *37th Annual Small Satellite Conference, 2023*.
- 김성중, 방효충. "Zernike 모멘트를 이용한 3차원 복원 지형의 정합". *항공우주학회 춘계학술발표회 2023 (국내)*.
- 박준우, 방효충. "파티클 필터 기반 지형 참조 항법의 가중치 평준화를 위한 보조 변수 추출 및 혼합 제안분포의 설계". *항공우주학회 춘계학술발표회 2023 (국내)*.
- 홍경우, 박준우, 방효충. "영상 특징 추출기 오차를 고려한 쿨백-라이블러 발산". *항공우주학회 춘계학술발표회 2023 (국내)*.
- 이동우, 방효충. "불확실성을 가지는 멀티로터를 위한 강화학습 기반의 비선형 외란관측기 설계". *항공우주학회 춘계학술발표회 2023 (국내)*.
- 이동우, 방효충. "쿠푸만 연산자를 이용한 쿼드로터의 데이터 기반 모델링 및 고장진단". *항공우주학회 춘계학술발표회 2023 (국내)*.
- 이동우, 방효충. "쿠푸만 연산자를 이용한 데이터 기반의 비선형시스템의 고장 진단". *제어로봇시스템학회 학술대회 2023 (국내)*.
- 이동우, 김민우, 김도현, 송민규, 변재민, 한승준, 방효충. "가변 후퇴익을 적용한 소형 자폭형 무인기의 유도제어 시스템 설계". *한국군사과학기술학회 추계학술대회 2023 (국내)*.

**2022**

- J. Lee and H. Bang. "Ground Track Control Using Differential Drag for Small Earth Observation Satellite Constellations". *AIAA Journal of Spacecraft and Rockets, Vol. 59, No. 5, May 2022*.
- H. Han, H. Kim, and H. Bang. "Monocular Pose Estimation of an Uncooperative Spacecraft Using Convexity Defect Features". *Sensors, Vol. 22, No. 21, Nov. 2022*.
- M.I. Rashed and H. Bang. "A Study of Autonomous Small Satellite Constellations for Disaster Management and Deep Space Strategy". *Remote Sensing, Vol. 14, Issue 23, Dec. 2022*.
- T. Kim and H. Bang. "Fractal Texture Enhancement of Simulated Infrared Images Using a CNN-Based Neural Style Transfer Algorithm with a Histogram Matching Technique". *Sensors, Vol. 23, No. 1, Dec. 2022*.
- M.A. Arshad, J. Ahmed, and H. Bang. "Path Planning and Polynomial Trajectory Generation using Quadratic Programming for Complex Indoor Environment". *Drones, 2022*.
- N.S. Zewge and H. Bang. "A Distributionally Robust Fusion Framework for Autonomous Multisensor Spacecraft Navigation during Entry Phase of Mars Entry, Descent, and Landing". *Remote Sensing, 2022*.
- J.D. Lee, L. Kim, K. Jang, S. Lee and H. Bang. "Feedback Linearization based Model Reference Adaptive Control for Multirotor UAVs under Uncertainties from Fuel and Payload". *Proceedings of the Institution of Mechanical Engineers, Part G*.
- 박한석, 방효충. "강화학습 기반 해상에서 UAV의 함상 자율착륙을 위한 경로계획". *한국해군과학기술학회지, 제5권 제1호, pp. 38-46, 2022.03 (국내)*.
- Awais Arshad, 박준우, 방효충, 김윤영, 김희수, 이요선, 최성호. "사격 차선 정렬을 위한 영상 기반의 관성 센서 편차 보상". *한국항공우주학회지, 제50권 제9호, pp. 617-625, 2022.09 (국내)*.
- 김남수, 이동우, 이호형, 홍수운, 방효충. "고정익 UAV 모델링 및 비행조종컴퓨터 기반 오토파일럿 통합 시뮬레이션 HILS 환경 구축". *한국항공우주학회지, 제50권 제12호, pp. 857-866, 2022.12 (국내)*.
- J. Park and H. Bang. "Evenly Weighted Particle Filter for Terrain-referenced Navigation using Gaussian Mixture Proposal Distribution". *International Conference on Unmanned Aircraft Systems 2022, 2022. 06. 22*.
- D. Lee, M. Kang, S. Han, and H. Bang. "Terrain Following of Tiltrotor UAV using MPC and Nonlinear Disturbance Observer-based Backstepping". *2022 22nd International Conference on Control, Automation and Systems, 2022. 11. 27 ~ 12. 01*.
- Mohammed I. Rashed and H. Bang. "Strategies for Autonomous Small-satellite Technology Transfer from LEO to CisLunar Space". *2022 22nd International Conference on Control, Automation and Systems, 2022. 11. 27 ~ 12. 01*.
- Natnael S. Zewge and H. Bang. "Reentry-phase Tracking of a Ballistic Missile in the Presence of Radar Glint Noise". *2022 22nd International Conference on Control, Automation and Systems, 2022. 11. 27 ~ 12. 01*.
- Mohammed I. Rashed and H. Bang. "A Study on Self-organizing small-satellite Constellation and its Ground Stations for Real-time and Commercial Applications". *2022 Asia-Pacific International Symposium on Aerospace Technology, 2022. 10. 12 ~ 14*.
- D. Lee, L. Kim, C. Lim, and H. Bang. "Incremental Nonlinear Dynamic Control for UAM with Coaxial Rotors Performance Degradation". *2022 Asia-Pacific International Symposium on Aerospace Technology, 2022. 10. 12 ~ 14*.
- J.Park and H. Bang. "Deterministic Reallocation Algorithm for Evenly Weighted Particle Filter". *2022 Asia-Pacific International Symposium on Aerospace Technology, 2022. 10. 12 ~ 14*.
- J. Ahmed, Muhammad A. Arshad, and H. Bang. "3D Model Points Reconstruction and Pose Solver for Vision Based Relative Navigation between Spacecrafts". *2022 Asia-Pacific International Symposium on Aerospace Technology, 2022. 10. 12 ~ 14*.
- H. Ahn and H. Bang. "Reinforcement Learning based Multirotor Obstacle Avoidance with Omnidirectional Depth Map". *2022 Asia-Pacific International Symposium on Aerospace Technology, 2022. 10. 12 ~ 14*.
- Muhammad A. Arshad, J. Ahmed, and H. Bang. "Path planning for Unmanned Aerial Vehicles using Direct Collocation Nonlinear Programming". *2022 Asia-Pacific International Symposium on Aerospace Technology, 2022. 10. 12 ~ 14*.
- H. Lee and H. Bang. "Improved Visual Inertial Odometry under Control Command and Model Dynamics". *2022 Asia-Pacific International Symposium on Aerospace Technology, 2022. 10. 12 ~ 14*.
- Natnael S. Zewge and H. Bang. "Moving Horizon Estimation-based Target Tracking for Terminal Ballistic Missile Defense". *2022 Asia-Pacific International Symposium on Aerospace Technology, 2022. 10. 12 ~ 14*.
- J. Lee and H. Bang. "Shared Reinforcement Learning for Vehicle Routing Problem with Heterogeneous Fleet". *2022 Asia-Pacific International Symposium on Aerospace Technology, 2022. 10. 12 ~ 14*.
- Mohammed I. Rashed and H. Bang. "Role of AI in Nano-satellite Constellations for Autonomy". *11th Nanosatellite Symposium, 2022. 10. 10*.
- D. Lee, L. KIm, H. Ahn, and H. Bang. "Fault-tolerant Control for Aircraft with Structural Damage using Gaussian Process Regression". *33rd Congress of the International Council of the Aeronautical Sciences 2022, 2022. 09. 04 ~ 09*.
- L. Kim, D. Lee, and H. Bang. "Incremental Nonlinear Dynamic Control With Sparse Non-parametric Bayesian Regression of Damaged Aircraft". *33rd Congress of the International Council of the Aeronautical Sciences 2022, 2022. 09. 04 ~ 09*.
- H. Ahn, C. Lim, D. Lee, and H. Bang. "Safe Reinforcement Learning based Multi-rotor Collision Avoidance with Unexpected Obstacles". *33rd Congress of the International Council of the Aeronautical Sciences 2022, 2022. 09. 04 ~ 09*.
- J. Park, H. Lee, and H. Bang. "Balanced Cooperative Target Search of Mobile Sensor Fleet under Localization Uncertainty". *2022 IEEE 61st Conference on Decision and Control, 2022. 08. 11*.
- Mohammed I. Rashed and H. Bang. "Design and Optimization of an Autonomous Constellation of Small-satellites for LEO and Beyond". *36th Annual Small Satellite Conference, 2022. 08. 10*.
- D. Lee, C. Lim, S. Lee, H. Kwwn, S. Lee, W. Choi, Y. Choi, and H. Bang. "Dynamic Performance Analysis of Hybrid-Electric Propulsion Systems for an Urban Air Mobility". *9th European Conference for Aeronautics and Space Sciences, 2022. 06. 27 ~ 07. 01*.
- Natnael S. Zewge, T. Kim, and H. Bang. "Navigation Under Abrupt Motion Disturbances: A Convex Programming Perspective". *2022 IEEE 9th International Workshop on Metrology for AeroSpace, 2022. 06. 27 ~ 29*.
- Natnael S. Zewge, T. Kim, and H. Bang. "A Convex Optimization Approach to Satellite Selection for Global Navigation". *2022 IEEE 95th Vehicular Technology Conference, 2022. 06. 19 ~ 22*.
- Natnael S. Zewge, J. Ahmed, and H. Bang. "Outlier-Robust Constrained State Estimation via L1 and Huber Penalization". *2022 13th Asian Control Conference, 2022. 05. 04 ~ 07*.
- J. Liao and H. Bang. "Precise Missile Autopilot Design Using Nonlinear Sliding Mode Control". *2022 13th Asian Control Conference, 2022. 05. 04 ~ 07*.
- D. Lee, K. Jang, L. Kim, S. Lee, and H. Bang. "Closed-Loop MRAC Augmented LQR with Integral Action for Quadrotor UAV under the Uncertainties". *2022 CEAS Guidance, Navigation, and Control Conference, 2022. 05. 03 ~ 05*.
- J. Ahmed and H. Bang. "Vision Based Relative Pose Estimation of Un-cooperative Spacecraft Using Deep Learning". *International Conference on Space, 2022, 2022. 03. 28*.
- S. Kim, K. Hong, and H. Bang. "Vision-based Map-referenced Navigation using Terrain Classification of Aerial Images". *AIAA SciTech 2022 Forum, 2022. 01. 03 ~ 07*.
- J. Park, S. Lee, Y. Kim, and H. Bang. "Hazard Avoidance Landing of Loaded Parafoil Using Deep Reinforcement Learning". *AIAA SciTech 2022 Forum, 2022. 01. 03 ~ 07*.
- 이호형, 박한석, 한유근, 허준회, 이영기, 강인영, 방효충, 픽셀 이동량을 고려하여 강건성을 향상시킨 영상 내 객체 추적 기법, 항공우주학회 추계학술발표회 2022, 2022. 11. 16 ~ 18 (국내)
- 이호형, 박한석, 한유근, 허준회, 이영기, 강인영, 방효충, 단안 카메라를 이용한 회전 각도 추정 성능 향상 기법, 항공우주학회 추계학술발표회 2022, 2022. 11. 16 ~ 18 (국내)
- 김한익, 방효충, 원 궤도 표적 원거리 랑데부 위한 요구조건 분석 및 해석적 유도, 항공우주학회 추계학술발표회 2022, 2022. 11. 16 ~ 18 (국내)
- 박준우, 안형주, 방효충, 자기 위치 정보가 불확실한 상황에서 다수 모바일 센서를 활용한 균형 잡힌 목표물 위치 탐색, 항공우주학회 추계학술발표회 2022, 2022. 11. 16 ~ 18 (국내)
- 박준우, 방효충, 결정론적 표본 재추출 파티클 필터와 표적 추적 문제로의 활용, 항공우주학회 추계학술발표회 2022, 2022. 11. 16 ~ 18 (국내)
- Mohammed I. Rashed, 방효충, 지구 및 달 궤도를 위한 초소형 위성군의 자율성 구축 능력, 항공우주학회 추계학술발표회 2022, 2022. 11. 16 ~ 18 (국내)
- 김영재, 김남수, 안형주, 이동우, 이호형, 임철수 ,임석재, 방효충, 실내 자율비행을 위한 프로펠러 오버래핑 구조 멀티콥터 개발, 항공우주학회 추계학술발표회 2022, 2022. 11. 16 ~ 18 (국내)
- 이재호, 박준우, 방효충, 유전 알고리즘을 활용한 이기종 함대 배송 경로 설계, 항공우주학회 추계학술발표회 2022, 2022. 11. 16 ~ 18 (국내)
- 이동우, 김영재, 임석재, 방효충, 항공기 Wing Rock 운동을 위한 SINDy를 사용한 모델참조 적응제어 기법 설계, 항공우주학회 추계학술발표회 2022, 2022. 11. 16 ~ 18 (국내)
- 안형주, 방효충, 강화학습에 기반한 깊이 이미지 활용 실내 무인기 동적 장애물 회피, 항공우주학회 추계학술발표회 2022, 2022. 11. 16 ~ 18 (국내)
- 김한익, 방효충, MBSE requirement diagram을 활용한 달 로버의 운용 및 제작 요구조건 분석, 항공우주시스템공학회 2022년도 추계학술대회, 2022 .11. 02 ~ 05 (국내)
- Marin Mikaël, 김태호, 방효충, S-band Communication and Software Defined Radio Ground Station for RANDEV CubeSat, 2022년도 한국전자파학회 하계종합학술대회, 2022. 08. 19 (국내)
- 이동우, 임철수, 이성헌, 방효충, 권혁준, 이승욱, 최월선, 최영일, UAM 하이브리드 전기추진시스템 성능 분석을 위한 시뮬레이션 개발, 항공우주학회 춘계학술발표회 2022, 2022. 04.20~22, 2022. 4. 20 ~ 22 (국내)
- 홍경우, 김성중, 노준영, 방효충, 임동주, 항공기 기동 한계를 고려한 지형 추적 궤적 재성형 알고리즘, 항공우주학회 춘계학술발표회 2022, 2022. 04.20~22, 2022. 4. 20 ~ 22 (국내)
- 홍경우, 방효충, 공면 조건을 이용한 영상 기반 항공기 카메라 자세 추정, 항공우주학회 춘계학술발표회 2022, 2022. 04.20~22, 2022. 4. 20 ~ 22 (국내)
- 김성중, 방효충, 이상훈, 제현국, 3차원 복원 지형과 수치표면모델 정합을 통한 항공기 위치 및 자세 추정, 항공우주학회 춘계학술발표회 2022, 2022. 4. 20 ~ 22 (국내)
- 박준우, 김성중, 홍경우, 방효충, 시각적 의미 문맥을 활용한 항공기 위치 및 방향각 추정, 항공우주학회 춘계학술발표회 2022, 2022. 4. 20 ~ 22 (국내)
- 김남수, 홍수운, 방효충, 고정익 UAV의 모델링 및 유도 제어기 통합 시뮬레이션 환경 제작, 항공우주학회 춘계학술발표회 2022, 2022. 4. 20 ~ 22 (국내)

**2021**

- O. Jung, J. Seong, Y. Jung, H.C. Bang. "Recurrent neural network model to predict re-entry trajectories of uncontrolled space objects". *Advances in Space Research, 2021*.
- J. Shin and H.C.Bang. "UAV Path Planning under Dynamics Threats Using and Improved PSO Algorithm". *International Journal of Aerospace Engineering, Volume 2020 (2020), Article ID 8820284, 17 pages, Dec, 2020*.
- Moon S, Lee D, Lee D, Kim D, Bang H. "Energy-Efficient Swarming Flight Formation Transitions Using the Improved Fair Hungarian Algorithm". *Sensors. 2021, no 4, 1260*.
- S.H. Mok and H.C. Bang. "Optimal Multi-Target Overflight Using Ground-Track Adjustment". *Astronaut Sci, Vol. 68, pp. 150 - 171, Feb. 2021*.
- HG. Harno, Y.S. Kim, J. Moon and H.C. Bang. "Zonotopic Kalman filtering for stability augmentation and flight envelope estimation". *Proceedings of the Institution of Mechanical Engineers, Part G, Journal of Aerospace Engineering, 2021*.
- K. Hong, S. Kim, J. Park and H. Bang. "Navigation using Particle Filter under GNSS-Denied Environment Based on Semantic Segmentation of Aerial Images". *submitted to AIAA Journal of Aerospace Information Systems, Jan. 2021 (투고)*.
- S. Moon, W. Youn and H. Bang. "Novel Deep-Learning-Aided Multimodal Target Tracking". *in IEEE Sensors Journal, vol. 21, no. 18, pp. 20730-20739, 15 Sept.15, 2021*.
- H. Ahn, J. Park, Y. Kim, and H. Bang. "Model Predictive Control-Based Multirotor Three-Dimensional Motion Planning with Point Cloud Obstacle". *in AIAA Journal of Aerospace Information Systems, 30 Nov. 2021*.
- D. Kwon, Y. Jung, Y. Cheon and H. Bang. "Sequential convex programming approach for real-time guidance during the powered descent phase of mars landing missions". *Advances in Space Research, 1 Dec. 2021*.
- 박준우, 안형주, 정성민, 노준영, 홍경우, 장광우, 김성중, 방효충, 김진원, 허준회, 박장호, 서송원. "지연된 측정치를 가진 저속 회전 유도형 탄약의 롤각 추정 및 비행 실험을 통한 검증". *한국항공우주학회지, 제49권 제5호, pp. 373-381, 2021.05 (국내)*.
- 이동우, 김남수, 장광우, 이성헌, 방효충, 유상하중의 불확실성을 고려한 쿼드로터의 모델 참조 적응제어 기법 설계, 한국항공우주학회지, 제49권 제9호, pp. 749-757, 2021.09 (국내)
- D. Lee, K. Jang, H. Lee, and H. Bang, Design for a Dual-Redundant Flight Control Computer Using a Model Predictive Voting Algorithm", 9th International Conference on Robot Intelligence Technology and Applications 2021, 2021. 12. 16 - 17
- H. Ahn, K. Jang, D. Lee, J. Park, K. Hong, and H. Bang. "Experimental Model of Coaxial Rotors Performace Degradation Induced by Wake Effect". *2021 Asia-Pacific International Symposium on Aerospace Technology 2021, 2021. 11. 15 - 17*.
- J. Liao and H. Bang, "Augmented Lagrange Based Particle Swarm Optimization for Missile Interception Guidance, 2021 Asia-Pacific International Symposium on Aerospace Technology 2021, 2021. 11. 15 - 17
- J. Lee, H. Lee, J. Noh, and H. Bang. "A traffic navigation for urban air mobility with reinforcement learning". *2021 Asia-Pacific International Symposium on Aerospace Technology, 2021. 11. 15 - 17*.
- D. Lee, N. Kim, J. Lee, and H. Bang. "Gaussian Process-Based Feedback Linearization Control for Quad-Tiltrotor". *2021 Asia-Pacific International Symposium on Aerospace Technology, 2021. 11. 15 - 17*.
- Natnael S. Zewge and H. Bang. "Enhanced-Precision Entry Phase Navigation for Mars Landing Using Surface Radio, IMU, and Environmental Sensors". *2021 Asia-Pacific International Symposium on Aerospace Technology, 2021. 11. 15 - 17*.
- J. Park, S. Kim, K. Hong, and H. Bang. "Visual Semantic Context of Sementically Segmented Aerial Image". *2021 Asia-Pacific International Symposium on Aerospace Technology, 2021. 11. 15 - 17*.
- J. Liao and H. Bang. "Parameter Tuning of Linear Active Disturbance Rejection Controller for Altitude Based on Particle Swarm Optimization". *2021 21st International Conference on Control, Automation and Systems, 2021. 10. 12 ~ 15*.
- Natanel S. Zewge and H. Bang. "Integrated Inertial and Radio Based State and Parameter Estimation for Mars Entry Phase Spacecraft Navigation". *2021 21st International Conference on Control, Automation and Systems, 2021. 10. 12 ~ 15*.
- T. Kim, Moriba K. Jah, B A. Jones, and H. Bang. "Time-series Classification of GEO Satellites Using Deep Convolutional Neural Network in Angular Momentum H-space Doma". *7th annual Space Traffic Management Conference, 2021. 01. 28*.
- 이동우, 이재호, 방효충, 쿼드로터의 자세 제어를 위한 슈퍼 트위스팅 슬라이딩 모드 제어기법, 제36회 제어로봇시스템학회 학술대회, 2021. 06. 21~23 (국내)
- 노준영, 이호형, 이동우, 방효충, 드론에서의 움직이는 표적 추적을 위한 짐벌 자동 제어 알고리즘, 항공우주학회 춘계학술발표회 2021, 2021. 7. 07~09 (국내)
- 김남수, 김성중, 이동우, 방효충, 고정익 항공기 착륙 시뮬레이션을 위한 6자유도 착륙 장치 모델링, 항공우주학회 춘계학술발표회 2021, 2021. 7. 07~09 (국내)
- 박준우, 채혁주, 박수정, 최한림, 방효충, 안경수, 김영곤, 심층 강화학습을 이용한 선도 추격자 대항 전투기 회피 기동 연구, 항공우주학회 춘계학술발표회 2021, 2021. 7. 07~09 (국내)
- 박준우, 방효충, 탑재체를 탑재한 조종 낙하산의 심층 강화학습을 통한 자동 착륙, 항공우주학회 춘계학술발표회 2021, 2021. 7. 07~09 (국내)
- 김태호, 한해윤, 문민기, 방효충, 잔여 자기 쌍극자 모멘트에 의한 외란 토크가 초소형 위성의 자세 지향에 미치는 영향 분석, 항공우주학회 춘계학술발표회 2021, 2021.07.07-09 (국내)
- 홍경우, 김성중, 이호형, 김남수, 박준우, 방효충, 공면조건을 이용한 카메라 장착 오차 추정, 항공우주학회 춘계학술발표회 2021, 2021.07.07-09 (국내)
- 이동우, 장광우, 김남수, 이성헌, 방효충, 운송용 쿼드로터의 불확실성을 고려한 모델 참조 적응제어 기법 설계, 항공우주학회 춘계학술발표회 2021, 2021.07.07-09 (국내)
- 이동우, 안형주, 방효충, 이중화 비행제어시스템 설계 및 동기화 기법 연구, 항공우주학회 춘계학술발표회 2021, 2021.07.07-09 (국내)
- 김한익, 방효충, An analysis of 1U size cubesat Cassegrain telescope thermal expansion caused by solar radiation in space, 한국광학회 하계 2021, 2021. 07.04-07 (국내)
- 김한익, 방효충, An optical drawing tolerance compensation analysis of 1U size Cubesat Cassegrain telescope, 한국항공우주학회 춘계 2021, 2021. 07. 07-09 (국내)
- 김한익, 문민기, 이준호, 방효충, An optical payload accommodation analysis for 1U size CubeSat hyper-spectral camera design using the draft drawings , 한국항공우주학회 추계 2020, 2020.11.18-20 (국내)
- 김태영, Moriba Jah, 방효충, 딥러닝을 활용한 각운동량 도메인에서의 지구정지궤도 위성의 시계열 분류 기법, 한국항공우주학회 춘계 2021, 2021. 07. 07-09 (국내)
- 김태영, 정재현, 방효충, 다중센서 교차 검증 기법을 통한 레이다 항법장치 (EGI/IMU) 비행 중 교정 방법, 한국항공우주학회 춘계 20201, 2021, 07. 07-09 (국내)
- 문민기, 방효충, H∞ 제어기법을 이용한 유연 구조물을 가진 인공위성의 자세제어, 항공우주학회 추계학술발표회, 2021. 2021. 11. 17~19 (국내)
- 장광우, 방효충, 모델 예측 경로 적분 제어를 응용한 멀티콥터 UAV의 경로점 통과를 위한 유도 기법, 항공우주학회 추계학술발표회, 2021. 2021. 11. 17-19 (국내)
- 장광우, 이동우, 방효충, 쿼드로터 UAV의 앞섬 보상기를 이용한 비선형 동적 모델역변환 제어기 설계 및 실험, 항공우주학회 춘계학술발표회, 2021. 2021. 07. 07-09 (국내)
- 이호형, 장광우, 이재호, 방효충, 독립 변수 변경과 변수 최적화를 통한 요격 미사일의 최소 시간 궤적 성형, 한국항공우주학회 추계학술발표회 2021, 2021. 11 (국내)
- 이동우, 김남수, 장광우, 이호형, 방효충, 가우시안 프로세스 기반의 틸트로터의 적응제어기법 설계, 항공우주학회 추계학술발표회 2021. 2021. 11. 17-19 (국내)
- 김성중, 노준영, 방효충, 지형추적 시스템 검증을 위한 비행 시뮬레이션 환경 구축, 한국항공우주학회 추계학술발표회 2021. 2021. 11. 17~19 (국내)
- 박준우, 방효충, 지형 고도 구배 기반의 제안 분포 파티클 필터를 활용한 지형 참조 항법, 한국항공우주학회 추계학술발표회 2021. 2021. 11. 17~19 (국내)
- 박준우, 김성중, 홍경우, 방효충, 의미론적 분할된 항공 영상을 이용한 시각적 의미 문맥의 오차 특성 분석, 한국항공우주학회 추계학술발표회 2021. 2021. 11. 17~19 (국내)
- 안형주, 홍경우, 박준우, 이동우, 장광우, 방효충, 후류 효과로 인한 동축 로터의 성능 감소에 대한 실험적 모델, 한국항공우주학회 추계학술발표회 2021. 2021. 11. 17~19 (국내)
- 김남수, 방효충, SINDy를 사용한 고정익 항공기 운동방정식 추정, 한국항공우주학회 추계학술발표회 2021. 2021. 11. 17~19 (국내)

## 과제

누리집 Projects 페이지(머리에 2018년 1월 5일 갱신 표기)에 실린 과제 129건(진행중인 과제 9건, 종료된 과제 120건) 가운데 기간이 2021년 10월 13일 뒤까지 이어지는 1건이다. 과제명과 기간은 누리집 표기이고, 이 과제의 위탁기관 칸은 「OOO」로 적혀 있다.[^projects]

- 지형참조항법 알고리즘 개발 (기간 2016-11-01–2021-10-31)

## 연락과 위치

- 연구실: 34141 대전광역시 유성구 대학로 291 KAIST 항공우주공학과, 교수실 N7-2동 #3303[^aelab][^aefac]
- 교수 이메일과 전화: hcbang@kaist.ac.kr, 042-350-3722[^aelab][^aefac]
- 팩스: +82-42-350-3710[^prof]
[^aelab]: KAIST 항공우주공학과 연구실 소개(Aerospace Systems and Control) <https://ae.kaist.ac.kr/boards/view/board_lab/86> (연구실명, 교수, 연구실 소개, 연구분야, 이메일·전화·교수실, 2026-10-26 열람)
[^aefac]: KAIST 항공우주공학과 교수진 목록 <https://ae.kaist.ac.kr/boards/lists/board_faculty/sc_category/1/> (방효충 항목, 2026-10-26 열람)
[^prof]: 누리집 Professor 페이지 <http://ascl.kaist.ac.kr/index.php?mid=professor> (Curriculum Vitae, 2026-10-26 열람)
[^postdoc]: 누리집 Post Doctors 페이지 <http://ascl.kaist.ac.kr/index.php?mid=post_doctors> (2026-10-26 열람)
[^phd]: 누리집 Ph.D. Candidates 페이지 <http://ascl.kaist.ac.kr/index.php?mid=PhD> (2026-10-26 열람)
[^ms]: 누리집 M.S. Candidates 페이지 <http://ascl.kaist.ac.kr/index.php?mid=ms> (2026-10-26 열람)
[^empty]: 누리집 Research Professor <http://ascl.kaist.ac.kr/index.php?mid=research_professor>, Contract Researcher <http://ascl.kaist.ac.kr/index.php?mid=contract_researcher>, Intern <http://ascl.kaist.ac.kr/index.php?mid=Intern>, Visiting Scholars <http://ascl.kaist.ac.kr/index.php?mid=visiting_scholars> 페이지 (2026-10-26 열람)
[^alumni]: 누리집 Alumni 페이지 <http://ascl.kaist.ac.kr/index.php?mid=alumni> (Post Ph.D., Ph.D., M.S. 칸, 2026-10-26 열람)
[^ij]: 누리집 International Journals 페이지 <http://ascl.kaist.ac.kr/index.php?mid=int_journals> (2026-10-26 열람)
[^dj]: 누리집 Domestic Journals 페이지 <http://ascl.kaist.ac.kr/index.php?mid=domestic_jounals> (2026-10-26 열람)
[^ic]: 누리집 International Conferences 페이지 <http://ascl.kaist.ac.kr/index.php?mid=int_confs> (2026-10-26 열람)
[^dc]: 누리집 Domestic Conferences 페이지 <http://ascl.kaist.ac.kr/index.php?mid=domestic_confs> (2026-10-26 열람)
[^projects]: 누리집 Projects 페이지(국문) <http://ascl.kaist.ac.kr/index.php?mid=projects_ko> (진행중인 과제·종료된 과제 칸, 2026-10-26 열람)
[^scgnc]: 누리집 Research 메뉴 Spacecraft GNC Algorithm 목차 <http://ascl.kaist.ac.kr/index.php?mid=spacecraft_gnc_01> (2026-10-26 열람)
[^sc-traj]: 누리집 Research 메뉴 Spacecraft Optimal Trajectory Design <http://ascl.kaist.ac.kr/index.php?mid=spacecraft_gnc_02> (2026-10-26 열람)
[^sc-ff]: 누리집 Research 메뉴 Spacecraft Formation Flying Control & Navigation <http://ascl.kaist.ac.kr/index.php?mid=spacecraft_gnc_03> (2026-10-26 열람)
[^sc-od]: 누리집 Research 메뉴 Spacecraft Orbit Determination <http://ascl.kaist.ac.kr/index.php?mid=spacecraft_gnc_04> (2026-10-26 열람)
[^sc-spin]: 누리집 Research 메뉴 Nutation and Spin Inversion Control of Spin-stabilized Spacecraft <http://ascl.kaist.ac.kr/index.php?mid=spacecraft_gnc_06> (2026-10-26 열람)
[^sc-att]: 누리집 Research 메뉴 Attitude and Angular Rate Estimation Using Vector Observations <http://ascl.kaist.ac.kr/index.php?mid=spacecraft_gnc_07> (2026-10-26 열람)
[^sc-star]: 누리집 Research 메뉴 Star Tracker Algorithm Design <http://ascl.kaist.ac.kr/index.php?mid=spacecraft_gnc_08> (2026-10-26 열람)
[^uavgnc]: 누리집 Research 메뉴 UAV GNC Algorithm 목차 <http://ascl.kaist.ac.kr/index.php?mid=uav_gnc_01> (2026-10-26 열람)
[^uav-arr]: 누리집 Research 메뉴 Optimal Scheduling of Arrival Flight in Terminal Airspaces <http://ascl.kaist.ac.kr/index.php?mid=uav_gnc_04> (2026-10-26 열람)
[^uav-trn]: 누리집 Research 메뉴 Terrain-referenced Navigation (TRN) System <http://ascl.kaist.ac.kr/index.php?mid=uav_gnc_08> (2026-10-26 열람)
[^uav-relnav]: 누리집 Research 메뉴 Vision-based Relative Navigation for Formation Flying <http://ascl.kaist.ac.kr/index.php?mid=uav_gnc_10> (2026-10-26 열람)
[^uav-land]: 누리집 Research 메뉴 Vision-based Autonomous Landing <http://ascl.kaist.ac.kr/index.php?mid=uav_gnc_13> (2026-10-26 열람)
[^uav-vatrn]: 누리집 Research 메뉴 Vision-aided Terrain Referenced Navigation <http://ascl.kaist.ac.kr/index.php?mid=uav_gnc_15> (2026-10-26 열람)
[^uav-vf]: 누리집 Research 메뉴 Vector Field Guidance Law <http://ascl.kaist.ac.kr/index.php?mid=uav_gnc_16> (2026-10-26 열람)
[^uav-hale]: 누리집 Research 메뉴 High Altitude Long Endurance UAVs <http://ascl.kaist.ac.kr/index.php?mid=uav_gnc_17> (2026-10-26 열람)
[^sys]: 누리집 Research 메뉴 System Developments 목차 <http://ascl.kaist.ac.kr/index.php?mid=systems_01> (2026-10-26 열람)
[^sys-nano]: 누리집 Research 메뉴 Nano-satellite Development <http://ascl.kaist.ac.kr/index.php?mid=systems_02> (2026-10-26 열람)
[^sys-qb50]: 누리집 Research 메뉴 QB50 Project <http://ascl.kaist.ac.kr/index.php?mid=systems_15> (2026-10-26 열람)
[^sys-cmg]: 누리집 Research 메뉴 CMGs (Control Moment Gyroscopes) <http://ascl.kaist.ac.kr/index.php?mid=systems_04> (2026-10-26 열람)
[^sys-robot]: 누리집 Research 메뉴 Free-Flying Space Robotics Experimental Test Bed <http://ascl.kaist.ac.kr/index.php?mid=systems_07> (2026-10-26 열람)
[^sys-krac]: 누리집 Research 메뉴 Korea Robot Aircraft Competition <http://ascl.kaist.ac.kr/index.php?mid=systems_11> (2026-10-26 열람)
[^p1]: T. Kim, N. S. Zewge, H. Bang, H. Yoon, Sensors 23, 4212 (온라인 2023-04-23). <https://doi.org/10.3390/s23094212> 초록 기준.
[^p2]: N. S. Zewge, H. Bang, Remote Sensing 15, 1139 (온라인 2023-02-19). <https://doi.org/10.3390/rs15041139> 초록 기준.
[^p3]: J. Ahmed, A. Arshad, H. Bang, Y. Choi, International Journal of Aeronautical and Space Sciences 25, 1146-1165 (온라인 2024-03-17). <https://doi.org/10.1007/s42405-023-00703-3> 초록 기준.
[^p4]: J. D. Lee, Y. Kim, Y. Kim, H. Bang, IET Control Theory & Applications 19, e70049 (온라인 2025-06-22). <https://doi.org/10.1049/cth2.70049> 초록 기준.
[^p5]: J. D. Lee 외, H. Bang, Journal of Intelligent & Robotic Systems 110, 128 (온라인 2024-09-03). <https://doi.org/10.1007/s10846-024-02142-y> 초록 기준.
[^p6]: J. Park, H. Bang, Journal of Aerospace Information Systems 21, 58-74 (2024). <https://doi.org/10.2514/1.i011281> 초록 기준.
[^p7]: J. Park, H. Bang, IEEE Transactions on Aerospace and Electronic Systems 61, 15627-15641 (2025). <https://doi.org/10.1109/taes.2025.3588823> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: J. Park, S. Kim, K. Hong, H. Bang, NAVIGATION: Journal of the Institute of Navigation 71, navi.634 (온라인 2024-02-09). <https://doi.org/10.33012/navi.634> 초록 기준(OpenAlex 등록 초록).

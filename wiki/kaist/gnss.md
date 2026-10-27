# 위성항법시스템 연구실 (Global Navigation Satellite Systems Laboratory, GNSS Lab)

**KAIST 항공우주공학과 · 이지윤 교수**

- 분야: 고안전성 위성항법과 무결성 감시(GNSS 보강 시스템, 전리층 위협), 다중 센서 통합 항법의 고장 검출·보호 수준, 도심 항공 모빌리티(UAM)의 안전 분리, GNSS 전리층·전파 엄폐 원격탐사
- 대분야: 기계·로봇·제조, 에너지·환경·지구
- 태그: 위성 원격탐사[^board][^remote][^p7], 자율주행[^board][^p4], 로봇 항법·SLAM[^p4], 과학·공학 AI[^p5], 위성항법(GNSS)[^p1], 도심 항공 모빌리티(UAM)[^p6], 우주 플라즈마·우주 기상[^p1][^p2]
- 홈페이지: <https://gnss.kaist.ac.kr/>
- 근거와 출처: [위성항법시스템 연구실 근거 페이지](gnss-sources.md)

> 고안전성 항법 시스템, 여러 항법 센서를 묶는 센서 융합 기술, GNSS를 이용한 위성 원격탐사를 연구하는 항공우주공학과 연구실이다.[^board] 학과 연구실 소개는 기존 민간항공기뿐 아니라 도심 항공 모빌리티, 자율주행차, 무인기 같은 미래 교통수단을 위한 고정밀 고안전성 항법 시스템을 연구한다고 적는다.[^board]

## 무엇을 연구하나

연구실은 KAIST 항공우주공학과 이지윤 교수의 연구실이다. 학과 연구실 소개는 연구실 이름을 「위성항법 시스템 연구실(Global Navigation Satellite Systems Laboratory, GNSS Lab)」로 적고, 연구실이 고안전성 항법 시스템, 센서 융합 기술, 위성 원격탐사 연구를 한다고 소개한다.[^board] 누리집 첫 화면은 연구실을 Global Navigation Satellite Systems Lab at KAIST로 적는다.[^home] GNSS(Global Navigation Satellite System, 여러 위성이 보내는 신호로 수신기의 위치와 시각을 구하는 위성항법 체계)를 쓰는 항법에서 연구실이 내세우는 주제는 무결성(integrity, 항법 정보를 믿어도 되는 정도로, 정보가 틀렸을 때 사용자에게 제때 경고하는 능력을 포함한다)이다. 학과 연구실 소개의 연구분야 칸은 항법 무결성을 맨 앞에 두고, 교수 페이지는 안전이 중요한 시스템의 무결성 보장을 전문 분야로 든다.[^board][^prof]

학과 연구실 소개에 따르면 연구실은 특히 무결성 아키텍처 설계, 항법 센서(GNSS, INS, LiDAR, RADAR, 영상 센서 등) 융합 기술, 항공 교통과 안전 운항 기술에 집중한다. 또 우주 환경 모니터링, 고층대기 탐사, 자연재해 감지와 예보를 위한 GNSS 원격탐사 연구를 한다.[^board] 학과 연구실 소개의 연구분야 칸은 항법 무결성, 센서 융합, 원격탐사이고[^board], 학과 교수진 목록은 교수의 연구분야를 Global Navigation Satellite System, Safety Critical Systems, Aircraft and Spacecraft Navigation, Remote Sensing으로 적는다.[^aefac]

누리집 교수 페이지는 교수의 전문 분야(Expertise)를 항공우주·지상 운송체의 항법, 안전이 중요한 시스템의 무결성 보장, 대기·우주 과학을 위한 원격탐사로 적는다. 연구(Research) 항목으로는 GNSS 보강 시스템(augmentation system, 기준국이나 위성이 GNSS 오차 보정 정보와 무결성 정보를 만들어 사용자에게 보내는 시스템), 안전이 중요한 시스템의 무결성 감시와 고장 검출·분리, 무인 항공 시스템(UAS)의 강건한 유도·항법, GNSS 신호가 나쁜 환경에서의 다중 센서 통합 항법, GNSS 전리층·대기 관측과 GNSS 전파 엄폐를 든다.[^prof] 누리집 Research 메뉴는 UAM Navigation과 Remote Sensing 두 갈래로 나뉘고, UAM Navigation 페이지는 GNSS Augmentation Systems와 Integrity for Multi-Sensor Navigation Systems를, Remote Sensing 페이지는 Ionospheric studies via GNSS observations와 GNSS Radio Occultation을 주제로 든다.[^uam][^remote]

## 주요 연구 주제

### 1. GNSS 보강 시스템의 무결성과 전리층 위협

교수 페이지와 UAM Navigation 페이지는 GNSS 보강 시스템을 연구 주제로 든다.[^prof][^uam] 대표 논문 1·2는 전리층(ionosphere, 지구 대기 위쪽에서 기체가 전리되어 자유 전자가 많은 층)이 만드는 신호 섬광과 지연이 보강 시스템의 오차와 무결성 경계에 주는 영향을 다룬다.[^p1][^p2]

대표 논문 1은 전리층 섬광 때 신호 추적이 끊기지 않은 채 반송파 위상이 한 주기 단위로 바뀌는 회절 유발 사이클 슬립이 지상 기반 보강 시스템(GBAS)의 오차와 감시기 통계량을 얼마나 키우는지를 브라질에서 모은 고속 GPS 자료로 분석했다.[^p1] 대표 논문 2는 위성 기반 보강 시스템(SBAS)이 방송하는 전리층 오차 경계의 크기를 줄이기 위해, 관측이 부족한 곳의 전리층 불규칙 위협 모델을 3차원 지표로 다시 매개변수화하고 한국 지역 SBAS 가용성으로 효과를 보였다.[^p2] 누리집 소식에 따르면 졸업생 선기영 박사의 박사 학위 논문은 전리층 섬광이 GBAS의 안전에 미치는 영향을 종합적으로 특성화했고, 이 논문으로 RTCA William E. Jackson Award를 받았다.[^rtca]

### 2. 다중 센서 통합 항법의 무결성

교수 페이지는 안전이 중요한 시스템의 무결성 감시와 고장 검출·분리, GNSS 신호가 나쁜 환경에서의 다중 센서 통합 항법을 연구 주제로 들고[^prof], UAM Navigation 페이지는 Integrity for Multi-Sensor Navigation Systems를 주제로 든다.[^uam] 학과 연구실 소개는 GNSS, INS, LiDAR, RADAR, 영상 센서 같은 항법 센서의 융합 기술을 적는다.[^board]

대표 논문 3은 GNSS와 관성 측정 장치(IMU)를 칼만 필터로 묶은 항법에서 IMU 고장이 위치 추정 오차로 퍼지는 방식을 해석적으로 유도하고, 이를 바탕으로 고장 검출기와 보호 수준(protection level, 위치 오차가 넘지 않는다고 보증하는 경계) 식을 만들었다.[^p3] 대표 논문 4는 도시 환경에서 쓰이는 FastSLAM 항법의 무결성 위험을 정상 조건과 고장 조건 모두에서 평가하는 틀을 내놓았다.[^p4] 대표 논문 5는 차분 GNSS 기준국의 다중경로 오차를 심층 신경망으로 모델링해 줄이는 방법이다.[^p5] 누리집 소식에 따르면 무인기 응용을 위한 LIRTK의 센서 고장 대비 무결성 보장을 다룬 ION GNSS+ 2023 발표(Integrity Assurance of LIRTK Using SS-RAIM Against Sensor Faults for UAV Applications)가 Best Presentation Award를 받았다.[^n1819]

### 3. 도심 항공 모빌리티(UAM)의 안전 분리

학과 연구실 소개는 연구실이 항공 교통과 안전 운항 기술에 집중한다고 적는다.[^board] 대표 논문 6은 도심 항공 모빌리티(UAM, 도시 위 공역을 쓰는 새로운 항공 교통)에서 비행 중에 탐지·회피 시스템으로 충돌을 피하는 전술적 충돌 해소를 위한 최소 분리 경계를 정하는 방법을 제안했다.[^p6] 누리집 소식에 따르면 회피 위험 비율 모델에 바탕을 둔 UAM 전술적 충돌 해소의 최소 분리 경계 논문이 2024년 디지털 항공전자 시스템 학회(DASC)에서 Best of Conference (1st Place) Award를 받았고[^n1863], UAM의 충돌 검출·회피 성능에 따른 최소 분리 거리 민감도 분석 논문이 2023년 항법시스템학회 정기학술대회에서 우수논문상을 받았다.[^n1824]

### 4. GNSS 전리층·전파 엄폐 원격탐사

교수 페이지는 GNSS 전리층·대기 관측과 GNSS 전파 엄폐(radio occultation, RO, 저궤도 위성이 지평선 쪽으로 지는 GNSS 위성의 신호를 받아, 신호가 대기를 지나며 휘고 늦어지는 정도로 대기와 전리층의 상태를 알아내는 관측 기법)를, Remote Sensing 페이지는 GNSS 관측을 통한 전리층 연구와 GNSS Radio Occultation을 연구 주제로 든다.[^prof][^remote] 학과 연구실 소개는 이 원격탐사 연구의 목적을 우주 환경 모니터링, 고층대기 탐사, 자연재해 감지와 예보로 적는다.[^board]

대표 논문 7은 엄폐 안테나만으로는 필요한 보정을 할 수 없는 위성에서, 정밀 궤도 결정용 안테나 자료를 함께 써 빈 구간을 채우고 전리층 전자 밀도를 얻는 방법을 다목적실용위성 5호(KOMPSAT-5) 자료로 검증했다.[^p7] 대표 논문 8은 미국을 지난 두 차례 개기일식의 총전자수 자료로, 일식이 플라즈마 감소 외의 전리층 교란을 만드는지를 따져 보았다.[^p8] 누리집 소식에 따르면 「광선 추적 시뮬레이션을 활용한 GNSS-RO 총전자량의 잔여 굴절 오차 분석」 논문이 2024년 항법시스템학회 정기학술대회에서 우수논문상을 받았다.[^n1873]

## 대표 논문

이지윤 교수가 저자인 2021–2026년 논문 가운데 네 연구 갈래(GNSS 보강 시스템의 무결성과 전리층 위협, 다중 센서 통합 항법의 무결성, UAM 안전 분리, GNSS 전리층·전파 엄폐 원격탐사)에서 초록을 확인할 수 있는 여덟 편을 골랐다. 여덟 편 모두 교수가 마지막 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [Analysis of Diffraction-Induced Residual Errors in GNSS Augmentation Systems Under Ionospheric Scintillation](https://doi.org/10.1109/TAES.2025.3624709) · IEEE Transactions on Aerospace and Electronic Systems | 전리층 섬광(ionospheric scintillation, 전리층의 불규칙한 구조 때문에 위성 신호의 세기와 위상이 빠르게 흔들리는 현상) 때 GNSS 보강 시스템에 모델링되지 않은 무결성 위험을 줄 수 있는 회절 유발 잔여 오차를 다뤘다. 신호를 놓친 뒤 생겨 쉽게 검출·배제되는 기존 사이클 슬립(cycle slip, 반송파 위상의 주기 셈이 갑자기 어긋나는 일)과 달리, 회절 유발 사이클 슬립은 추적이 이어지는 중에 생겨 위상이 한 주기 단위로 바뀌고, 이 변화가 평활화된 의사거리(pseudorange, 신호의 전파 시간으로 잰 위성까지의 거리)와 무결성 감시기 검정 통계량에 모두 영향을 준다. 브라질에서 모은 고속 GPS 자료로 전리층 지연을 없앤(IFree) 평활 의사거리와 코드-반송파 발산(CCD) 감시기 검정 통계량에 주는 잡음 기여를 유도했다. 섬광이 가장 심한 조건(S4 값 1.0 초과)에서 IFree 평활 의사거리 오차는 이 자료에서 최대 약 8 m에 이르렀고, 이 오차를 감싸는 표준편차는 표준 GBAS 오차 모델을 넘었다. CCD 감시기 검정 통계량은 평상시 잡음 수준의 최대 세 배였다. 저자들은 S4 선별과 감시기 조정으로 줄이지 않으면 이 사이클 슬립이 섬광 조건에서 보강 시스템의 무결성에 크게 영향을 줄 수 있다고 적는다.[^p1] | 1저자 A. K. Sun, 마지막 저자 이지윤 (3명) |
| 2 | 2022 | [Undersampled Ionospheric Irregularity Threat Parameterization Using a Three-Dimensional Model for Satellite-Based Augmentation Systems](https://doi.org/10.1109/TAES.2022.3199192) · IEEE Transactions on Aerospace and Electronic Systems | 단일 주파수 위성 기반 보강 시스템(SBAS)은 전리층 격자점(IGP)마다 수직 전리층 지연 추정값과 그 무결성 경계인 격자 전리층 수직 오차(GIVE)를 계산해 방송한다. GIVE의 가장 큰 몫은 관측이 부족한 곳의 전리층 불규칙 위협 모델에서 나온다. 이 논문은 GIVE를 줄이기 위한 위협 모델 매개변수화 방법을 내놓았다. 관측 방향 사이의 각도 간격이 얼마나 고른지를 재는 지표를 새로 설계해 기존 지표(fit radius, 상대 중심 지표 RCM)에 더했고, 이 3차원 지표와 한국 GNSS 기준국의 과거 전리층 폭풍 자료로 위협 모델을 만들었다. 한국 지역 SBAS 가용성을 모의한 예비 평가에서 이 방법을 GIVE 감시 알고리즘에 적용하자 수직 유도 접근(APV-I)의 99.9% 가용성이 최대 12% 개선됐다.[^p2] | 1저자 E. Bang, 마지막 저자 이지윤 (2명) |
| 3 | 2023 | [Navigation Safety Assurance of a KF-Based GNSS/IMU System: Protection Levels Against IMU Failure](https://doi.org/10.33012/navi.612) · NAVIGATION: Journal of the Institute of Navigation | 칼만 필터(KF, 측정값과 운동 모형을 함께 써 상태를 차례로 추정하는 방법)로 묶은 GNSS/IMU 항법에서 관성 측정 장치(IMU) 고장에 대비하는 무결성·연속성 알고리즘을 제안했다. 앞선 연구는 주로 GNSS 고장을 다루고 IMU 고장 가설은 다루지 않았다. GNSS 측정은 칼만 필터의 측정 갱신 단계에 쓰이지만 IMU 측정은 상태 예측 단계에 쓰여, 고장이 사용자 상태 오차로 퍼지는 방식이 GNSS와 다르다. 연속된 IMU 고장이 사용자 상태 오차에 주는 영향을 해석적으로 유도하고, 이를 바탕으로 칼만 필터 이노베이션(측정값과 예측값의 차이)을 쓰는 고장 검출기와, 연속된 IMU 고장 영향 아래에서도 사용자 상태 오차를 안전하게 감싸는 보호 수준 식을 만들었다.[^p3] | 1저자 J. Lee, 마지막 저자 이지윤 (5명) |
| 4 | 2025 | [Fault Modes and Methods to Evaluate Integrity Risk for FastSLAM-Based Navigation](https://doi.org/10.1049/rsn2.70029) · IET Radar, Sonar & Navigation | FastSLAM(위치 후보를 확률적으로 추적하며 위치와 지도를 함께 추정하는 기법)은 도시 환경에서 강건한 항법 해를 주고, 자율주행의 안전을 위해서는 그 무결성을 보장하는 일이 중요하다. 앞선 연구의 경험적 무결성 위험 평가는 위험을 지나치게 보수적으로 추정했고 고장 조건을 고려하지 않았다. 이 연구는 세 가지를 내놓았다. 추정 정확도를 해치지 않으면서 경험적 위험의 보수성을 줄이는 가중치·재표본 기법, 동적 갱신 단계의 제어 입력 고장을 검출·분리하는 감시 방법, 자료 연관 고장을 확률 모형으로 고려하는 보수적 무결성 위험 평가 방법이다. 모의 결과 정상 시나리오와 고장 시나리오 모두에서 무결성 성능이 크게 개선됐다.[^p4] | 1저자 P. H. Choi, 마지막 저자 이지윤 (5명) |
| 5 | 2022 | [DNN-Based Approach to Mitigate Multipath Errors of Differential GNSS Reference Stations](https://doi.org/10.1109/TITS.2022.3207281) · IEEE Transactions on Intelligent Transportation Systems | 차분 GNSS의 주요 오차 성분 가운데 하나는 기준국의 다중경로(multipath, 신호가 주변 물체에 반사되어 여러 경로로 수신기에 들어오는 현상) 오차다. 이 논문은 심층 신경망(DNN)을 쓰는 다중경로 모델링 방법을 내놓았다. 기준국 주변의 피할 수 없는 변화로 생기는 다중경로 오차의 변화를 잡기 위해 신호 대 잡음비와 위성 기하를 특징 변수로 썼다. 실험 자료로 정상 다중경로와 변하는 다중경로 두 경우에서 성능을 보였고, 보정 뒤 남은 다중경로 오차는 표준화된 오차 모델 안에 잘 들어왔다.[^p5] | 1저자 D. Min, 마지막 저자 이지윤 (6명) |
| 6 | 2024 | [Determining Minimum Separation Boundary for UAM Tactical Deconfliction](https://doi.org/10.33012/2024.19601) · Proceedings of the ION 2024 Pacific PNT Meeting | 도심 항공 모빌리티가 자리 잡으면 좁은 공역의 밀도가 높아져 공중 충돌 위험이 커지므로, 다른 항공기와 고정 장애물로부터 안전한 분리를 보장하는 충돌 해소(deconfliction)가 중요하다. 충돌 해소는 비행 전의 전략적 단계와 비행 중의 전술적 단계로 나뉜다. 넓은 공역을 쓰는 기존 항공기의 분리 기준을 UAM에 그대로 쓰면 공역 효율이 크게 떨어질 수 있어, 안전 요구를 지키면서 좁힌 분리 경계가 필요하다. 전략적 충돌 해소의 최소 분리 경계를 다룬 앞선 연구를 넓혀, 전략적 충돌 해소가 실패할 때 탐지·회피(DAA) 시스템으로 충돌을 줄이는 전술적 충돌 해소의 최소 분리 경계를 정하는 방법을 제안했다. DAA 시스템의 성능을 나타내는 두 핵심 변수에 초점을 맞췄고, UAM에 맞는 DAA 시스템인 ACAS X에 적용한 사례 연구에서 전술적 충돌 해소를 쓰면 쓰지 않는 경우에 비해 분리 경계를 12% 줄일 수 있었다.[^p6] | 1저자 J. Kim, 마지막 저자 이지윤 (5명) |
| 7 | 2024 | [Multiantenna-Based Data Filling Method for Retrieving Electron Density Profiles From GNSS Radio Occultation Data](https://doi.org/10.1109/TGRS.2024.3449337) · IEEE Transactions on Geoscience and Remote Sensing | GNSS 전파 엄폐로 저궤도(LEO) 고도 아래의 전리층 전자 밀도를 얻으려면 엄폐 쪽 총전자수(TEC)에서 비엄폐 쪽 TEC를 빼는 보정이 필요하다. 그러나 엄폐 안테나가 비엄폐 쪽 TEC를 관측하지 못하는 임무에는 이 보정을 쓸 수 없다. 이 논문은 여러 안테나 자료로 빈 곳을 채워 전자 밀도를 얻는 방법을 제안했다. 정밀 궤도 결정(POD) 안테나로 관측한 비엄폐 쪽 TEC를 엄폐 안테나로 관측한 엄폐 쪽 TEC와 이어 보정을 쓸 수 있게 하고, 두 안테나 자료 사이에 남은 빈 구간은 척도 높이가 변하는 엡스타인 함수로 모델링했다. 함수의 최적 매개변수는 내점법으로 정했다. 다목적실용위성 5호(KOMPSAT-5) 자료에 적용해 같은 곳의 이오노존데 관측과 비교한 결과, 이 방법으로 얻은 전자 밀도가 이오노존데 측정값과 잘 맞았다.[^p7] | 1저자 H. Chang, 마지막 저자 이지윤 (5명) |
| 8 | 2025 | [Do Solar Eclipses Generate Propagating Ionospheric Perturbations?](https://doi.org/10.1029/2025JA033746) · Journal of Geophysical Research: Space Physics | 일식 때 플라즈마가 줄어드는 현상은 잘 알려져 있지만, 일식이 다른 형태의 전리층 교란을 만드는지는 논란이 있다. 미국을 지난 두 차례 개기일식(2017년, 2024년)을 사례로, 일식 경로를 따라 총전자수(TEC)로 전리층 교란을 추적했다. 평활 필터(Savitzky–Golay 필터)로 교란을 찾으면 개기 중에는 음의 TEC 교란이, 일식 시작과 끝 무렵에는 양의 교란이 나타났는데, 이는 그 시기의 빠른 TEC 변화가 만든 필터 인공물로 해석됐다. 진동형 필터(다항식 추세 제거)를 쓰면 경로를 따라 준주기적인 여러 겹의 교란층이 보이지만, 이 필터는 추세를 없애는 과정에서 파동 모양의 인공물을 만들어 그 무늬는 실제 교란을 나타내지 않는다. 저자들은 잘 알려진 플라즈마 감소 말고 일식이 만드는 전리층 교란은 필터 인공물과 구별되지 않아 뚜렷하지 않다고 결론짓는다.[^p8] | 1저자 A. K. Sun, 마지막 저자 이지윤 (5명) |

## 교수와 전문 분야

이지윤 교수(Lee, Jiyun)는 KAIST 항공우주공학과 교수다. 학과 교수진 목록은 직위를 Professor로, 학력을 B.S. Yonsei Univ ('97), M.S. Univ. of Colorado ('99), Stanford Univ ('01), Ph.D. Stanford Univ ('05)로 적는다.[^aefac] 누리집 교수 페이지는 직함을 KAIST Endowed Chair Professor로 적고, 학력을 Stanford University 항공우주공학과 박사(2005)와 석사(2001), University of Colorado at Boulder 항공우주공학과 석사(1999), 연세대학교 천문대기과학과 학사(1997)로 적는다.[^prof] 누리집 소식에 따르면 교수는 2023년 3월 1일부로 KAIST 지정석좌교수에 임명됐다.[^n1817]

교수 페이지가 적는 주요 수상(Selected Honors and Awards)은 미국 항법학회(ION) Best Paper Awards(2003, 2004, 2016), 미국 연방항공청(FAA) Recognition(2008, 2013), KAIST 항공우주공학과 Outstanding Teaching Award(2013, 2016), KAIST 공과대학 Outstanding Project Advisor Award(2010), FAA NAVTAC KUDOS Award(2009)다.[^prof] 누리집 소식에 따르면 교수는 항공용 위성 기반 항법 시스템의 안전을 보장하는 기술에 기여한 공로로 ION의 2023 Thurlow Award를 한국 연구자로는 처음 받았고[^n1848], 무인 항공기와 도심 항공 모빌리티의 안전한 자율 운항을 돕는 항법 기술 연구로 한국항공우주학회 KSAS-금곡 젊은연구자상을 받았다.[^n1876] 교수 페이지는 학회 활동으로 ION Satellite Division Secretary(2022–2024), ION Council Technical Representative(2019–2020), ION Navigation Associate Editor, IEEE Signal Processing Magazine Guest Associate Editor, Korea Navigation Institute(KONI)와 Institute of Positioning, Navigation and Timing(IPNT)의 Director, 국토교통부·과학기술정보통신부·해양수산부 등의 위원회 위원을 적는다.[^prof]

교수 페이지의 전문 분야 세 가지(항공우주·지상 운송체의 항법, 안전이 중요한 시스템의 무결성 보장, 대기·우주 과학을 위한 원격탐사)와 2021–2026년 논문 목록을 함께 보면, 교수의 전문 분야는 위성항법 보강 시스템과 다중 센서 항법의 무결성 설계, 전리층 위협 모델링, GNSS를 이용한 전리층·대기 원격탐사다.[^prof][^journal][^intconf]

## 응용 분야

학과 연구실 소개는 연구실이 기존 민간항공기와 도심 항공 모빌리티, 자율주행차, 무인기 같은 미래 교통수단을 위한 고정밀 고안전성 항법 시스템을 연구하고, 우주 환경 모니터링, 고층대기 탐사, 자연재해 감지와 예보를 위한 GNSS 원격탐사를 연구한다고 적는다.[^board] 대표 논문 4는 FastSLAM 무결성 보장이 자율주행 응용의 안전에 중요하다고 적고[^p4], 대표 논문 6은 도심 항공 모빌리티의 공역 효율과 안전을 함께 다룬다.[^p6]

## 구성원

누리집 People 페이지의 박사후연구원 2명, 박사과정 6명, 석사과정 2명, 모두 10명이다(Staff 페이지와 Students 페이지는 같은 카드를 나눠 싣는다). 「시작」은 카드에 적힌 since·admitted 학기다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다. 다만 대표 논문 3·5의 저자 Minchan Kim은 졸업생 표의 같은 이름 박사 졸업생(2018)과 현재 박사후연구원 가운데 누구인지 가릴 수 없어 표시하지 않았다.

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Minchan Kim | 박사후연구원 | Spring 2026 | byd04063@kaist.ac.kr | 4, 6 |
| Gihun Nam | 박사후연구원 | Fall 2026 | nam0603@kaist.ac.kr | 4, 6 |
| Yunjung Choi | 박사과정 | Spring 2021 | clarayj@kaist.ac.kr |  |
| Jaehee Chang | 박사과정 | Spring 2023 | chang.cathy7@kaist.ac.kr |  |
| Junsoo Kim | 박사과정 | Spring 2024 | jsoo526@kaist.ac.kr | 6 |
| Jihyeok Park | 박사과정 | Fall 2025 | 1999jimmy@kaist.ac.kr |  |
| Minsung Kim | 박사과정 | Fall 2026 | 9574m@kaist.ac.kr |  |
| Jimin Do | 박사과정 | Spring 2026 | djm0328@kaist.ac.kr |  |
| Jonghyeon Park | 석사과정 | Spring 2025 | bellhyeon@kaist.ac.kr |  |
| Seungjun Heo | 석사과정 | Spring 2026 | superjunn00@kaist.ac.kr |  |

## 졸업생

누리집 Alumni 페이지의 박사(Ph. D.) 14줄과 석사(M. S.) 19줄, 모두 33줄이다. 같은 사람이 석사 줄과 박사 줄에 함께 오른 경우가 있다. 진로는 Current Position 칸이고, 학위 논문은 Dissertation·Thesis 칸이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Noah Minchan Kim | Ph.D. (2026) | Postdoctoral researcher, Department of Aerospace Engineering, KAIST, Daejeon, Rep. of Korea | Research on Integrity Architecture of RTK/INS Integrated Navigation System Tolerant to Cycle Slips |
| Andrew Kiyoung Sun | Ph.D. (2025) | Postdoctoral researcher, Satellite Navigation and Sensing Laboratory, University of Colorado Boulder, CO, United States | GBAS Integrity under Ionospheric Scintillation: Error Characterization, Modeling, and Performance Evaluation |
| Pil Hun Choi | Ph.D. (2025) | Hanwha Aerospace, Daejeon, Rep. of Korea | Methodology for FastSLAM navigation integrity assurance : Fault classification and monitoring based on particle filter characteristics |
| Dongchan Min | Ph.D. (2024) | Postdoctoral researcher, Department of Aeronautics and Astronautics, Stanford University, CA, United States | Integrity Architecture for Carrier-phase Differential GNSS System Using Solution Separation RAIM |
| Hyeyeon Chang | Ph.D. (2023) | Postdoctoral researcher, Satellite Navigation and Sensing Laboratory, University of Colorado Boulder, CO, United States | GNSS RO ionospheric electron density retrieval through multi-antenna-based data filling |
| Haerhee Park | Ph.D. (2022) | Senior Researcher, Department of Navigation, Agency for Defense Development (ADD), Daejeon, Rep. of Korea | Research on Integrity Assurance of Extended Kalman Filter-based Terrain Referenced Navigation System |
| Seokhyun Shin | Ph.D. (2021) | Senior Researcher, Department of Navigation, Agency for Defense Development (ADD), Daejeon, Rep. of Korea | Multi-matching based vision navigation algorithm referencing a low-resolution map |
| Dongwoo Kim | Ph.D. (2021) | Senior Researcher, KARI (Korea Aerospace Research Institute), Daejeon, Rep. of Korea | Safety assured navigation in polar regions: Kalman filter-based integrity monitoring methods considering fault duration |
| Seongkyun Jeong | Ph.D. (2020) | Associate Professor, Department of Human Intelligence and Robot Engineering, Sangmyung University, Cheonan, Rep. of Korea | Multi-test and CUSUM Method based Spoofing Detection Algorithm for GNSS Augmentation System |
| Jinsil Lee | Ph.D. (2019) | Senior Researcher, KARI (Korea Aerospace Research Institute), Daejeon, Rep. of Korea | Research on Integrity Architecture of GNSS/INS Integrated Navigation Systems |
| Moonseok Yoon | Ph.D. (2018) | Senior Researcher, KARI (Korea Aerospace Research Institute), Daejeon, Rep. of Korea | Towards Worldwide GNSS-Based Landing Systems: Modeling and Probabilistic Integrity Assessment of Low-latitude Ionospheric Threat |
| Kihun Lee | Ph.D. (2018) | Senior Researcher, Department of Navigation, Agency for Defense Development (ADD), Daejeon, Rep of Korea | Study on the Performance Enhancement of GNSS Anti-jamming Array Antenna by Symmetric STAP and Time Delay Compensation |
| Minchan Kim | Ph.D. (2018) | Senior Researcher, KARI (Korea Aerospace Research Institute), Daejeon, Rep. of Korea | High Integrity Local-Area Differential GNSS to Support Unmanned Aircraft System Navigation |
| Eugene Bang | Ph.D. (2017) | Assistant Professor, School of Aerospace Engineering, Gyeongsang National University, Jinju, Rep. of Korea | Road to Enhanced SBAS : Spatio-temporal Expansion of Ionospheric Delay Estimation and Bounding Technique |
| Namkyu Woo | M.S. (2024) | Researcher, Department of Navigation, Agency for Defense Development (ADD), Daejeon, Rep of Korea | Navigation Safety Distance between aircraft of Ground Based Augmentation System |
| Junsoo Kim | M.S. (2024) | Ph.D. Candidate, Department of Aerospace Engineering , KAIST, Daejeon, Rep. of Korea | Safety Risk Assessment based Minimum Separation Distance for UAM Operations |
| Sunjin Kim | M.S. (2023) | Researcher, Department of Navigation, Agency for Defense Development (ADD), Daejeon, Rep of Korea | Singular spectrum analysis based mstid detection and characteristics parameter modeling method |
| YunJung Kim | M.S. (2022) | Researcher, Department of Navigation, Agency for Defense Development (ADD), Daejeon, Rep of Korea | Integrity Assurance Method for CDGNSS-based Autonomous Airborne Refueling under Ephemeris Fault Conditions |
| Gihun Nam | M.S. (2021) | Ph.D. Candidate, Department of Aerospace Engineering , KAIST, Daejeon, Rep. of Korea | Continuity sub-optimal allocation algorithm for real-time innovation-based IMU fault monitor |
| Hyojin Lee | M.S. (2021) | Samsung Electronics, Hwaseong, Rep. of Korea | Navigation performance based satellite selection for multi-constellation RAIM to support safe operation of UAM |
| Kiyoung Sun | M.S. (2020) | Ph.D. Candidate, Department of Aerospace Engineering , KAIST, Daejeon, Rep. of Korea | Availability Assessment of Dual-Frequency GNSS based Aviation Applications under Ionospheric Scintillation |
| Dongchan Min | M.S. (2019) | Postdoctoral researcher, Department of Aeronautics and Astronautics, Stanford University, CA, United States | Deep Neural Network Based Multipath Mitigation Method for Carrier-Based Differential GNSS Systems |
| Giseon Hong | M.S. (2019) | Research Engineer, Satrec Initiative Co. Ltd., Daejeon, Rep. of Korea | Safe Separation Distance Determination for Unmanned Aerial System Traffic Management |
| Junyoung Han | M.S. (2018) | Research Engineer, Agency for Defense Development (ADD), Daejeon, Rep of Korea | Simulation-based Flight Technical Error Modeling for Low Altitude Drone Operations |
| Eunjeong Hyeon | M.S. (2017) | Assistant Professor, Department of Mechanical Engineering, University of California, Riverside, CA, United States | Integrity Monitoring of GNSS/Barometer Sensor Integration using RAIM Algorithm |
| Dong-Kyeong Lee | M.S. (2016) | Ph.D. Candidate, Department of Aerospace Engineering Sciences, University of Colorado Boulder, Boulder, CO, USA | Fast Location Surveying Algorithm to Support the Deployment of Mobile DGNSS |
| Dongwoo Kim | M.S. (2015) | Senior Researcher, KARI (Korea Aerospace Research Institute), Daejeon, Rep. of Korea | Characterization and Overbounding Methods of GNSS Clock and Ephemeris Error to Support ARAIM |
| Kiwan Kim | M.S. (2015) | Engineer, Kakao Mobility Corp., Seongnam, Rep. of Korea | Flight Technical Error Modeling for Deriving Safe Separation between UAVs |
| Chorong Ryu | M.S. (2014) | Engineer, Hyundai Motor Company, Hwaseong, Rep. of Korea |  |
| Moonsoek Yoon | M.S. (2014) | Senior Researcher, KARI (Korea Aerospace Research Institute), Daejeon, Rep. of Korea | Characteristics of Medium-scale Traveling Ionospheric Disturbances in the Korean Region |
| Yun-Jung Choi | M.S. (2013) | Researcher, KIAST (Korea Institute of Aviation Safety Technology), Incheon, Rep. of Korea | Research on Ionospheric Anomaly for CAT-I GBAS Operation in South Korea |
| Kwang-Seob Jeong | M.S. (2012) |  | Improving the Accuracy of GPS Receiver Inter-frequency Bias Estimation Through Time Series Analysis |
| Eugene Bang | M.S. (2012) | Assistant Professor, School of Aerospace Engineering, Gyeongsang National University, Jinju, Rep. of Korea | Automated Speed Estimation Algorithm of Ionospheric Wave Front for Ground-Based Augmentation Systems |

## 최근 논문 목록 (2021–2026)

누리집 Publications 메뉴의 Journal Articles, Int. Conferences, Dom. Conferences 페이지에 오른 2021–2026년 항목이다. 학술지 19편, 국제 학술대회 42편, 국내 학술대회 23편, 모두 84편이다.[^journal][^intconf][^domconf] 저자·제목·학술지 표기는 각 항목의 서지 그대로이며, 연도는 누리집이 적은 연도다. 학술대회 날짜가 열람일 뒤인 국내 학술대회 항목 1편은 누리집에 적힌 예정 날짜를 함께 표시했다.

**2026**

- Jaehee Chang, Jiyun Lee, Sergey Sokolovskiy, Zhen Zeng, John Braun. "3D Ray Tracing Analysis of Residual Ionospheric Errors in GNSS RO Bending Angles Using IRI-2020". *Proceedings of the 39th International Technical Meeting of the Satellite Division of The Institute of Navigation (ION GNSS+ 2026), Orlando, Florida (국제 학회)*.
- Jonghyeon Park, Jaehee Chang, Jiyun Lee. "Wavelet-Based Local Spectral Width for Bending Angle Uncertainty Estimation in GNSS-RO Phase Matching". *11th International Radio Occultation Working Group (IROWG-11) , Leibnitz, Austria (국제 학회)*.
- Junsoo Kim, Gihun Nam, Jiyun Lee, Dongchan Min, Sam Pullen. "Horizontal Minimum Separation Boundary Using Detection and Avoidance Models for UAM Tactical Deconfliction". *2026 AIAA DATC/IEEE 45th Digital Avionics Systems Conference (DASC), Orlando, Florida (국제 학회)*.
- Jaehee Chang, Jiyun Lee, Sergey Sokolovskiy, Zhen Zeng, John Braun. "Characterizing Residual Ionospheric Errors in GNSS RO Bending Angles: A Comparative Analysis of COSMIC-1 and COSMIC-2". *11th International Radio Occultation Working Group (IROWG-11) , Leibnitz, Austria (국제 학회)*.
- Jimin Do, Gihun Nam, Kiyoung Sun, Jiyun Lee. "Residual Ionospheric Errors of the NeQuick-G Model for LEO PNT". *2026 European Geosciences Union (EGU) (국제 학회)*.
- Jihyeok Park, Jaehee Chang, Jiyun Lee. "Physics-Guided Neural Network for Correcting Residual Ionospheric Error in GNSS Radio Occultation Bending Angle". *ION Pacific PNT (국제 학회)*.
- Jonghyeon Park, Jaehee Chang, Jiyun Lee. "Wavelet-Transform-based Phase Matching for Tropospheric Retrieval in GNSS Radio Occultation". *ION Pacific PNT (국제 학회)*.
- Junsoo Kim, Gihun Nam, Jiyun Lee, Dongchan Min, Sam Pullen. "Determining the Minimum Lateral Separation Distance for UAM Using ADS-B Information". *ION Pacific PNT (국제 학회)*.
- Jonghyeon Park, Jihyeok Park, Jaehee Chang, Jiyun Lee. "Sharpness Parameter를 사용한 GNSS RO 대기경계층 산출 품질 관리 평가". *항법시스템학회 정기학술대회 (국내 학회, 누리집 기재 날짜 2026-11-06)*.
- Junsoo Kim, Gihun Nam, Jimin Do, Jiyun Lee. "LEO SoP PNT를 위한 TOA 거리 제약 기반 위성 상태 보정정보 생성 기법". *한국항공우주학회 우주학술대회 (국내 학회)*.
- Junsoo Kim, Gihun Nam, Jimin Do, Jiyun Lee. "다중 빔 LEO 위성 기반 SoP PNT를 위한 빔별 시계 오차 추정 기법". *한국항공우주학회 우주학술대회 (국내 학회)*.
- Gihun Nam, Jimin Do, Junsoo Kim, Jiyun Lee. "LEO 보강 GBAS의 정상상태 무결성 성능 분석". *한국항공우주학회 우주학술대회 (국내 학회)*.
- Junsoo Kim, Jimin Do, Jiyun Lee. "Iridium 신호를 활용한 GNSS/LEO/INS 통합 항법 시스템의 성능 평가". *한국항공우주학회 춘계학술대회 (국내 학회)*.

**2025**

- Hyosub Kil, Andrew K. Sun, Se-Heon Jeong, Woo Kyoung Lee, Jeong-Heon Kim, Jiyun Lee. "Assessment of the Generation of Traveling Ionospheric Disturbances by Solar Terminators". *JGR Space Physics, vol. 131, iss. 1, no. e2025JA034724 (doi:10.1029/2025JA034724) (학술지)*.
- Andrew K. Sun, Sam Pullen, Jiyun Lee. "Analysis of Diffraction-Induced Residual Errors in GNSS Augmentation Systems under Ionospheric Scintillation". *IEEE Transactions on Aerospace and Electronic Systems, vol. Early Access (doi:10.1109/TAES.2025.3624709) (학술지)*.
- Dongchan Min, Noah Minchan Kim, Gihun Nam, Jiyun Lee, Sam Pullen. "SS-RAIM-Based Integrity Architecture for CDGNSSs Against Satellite Measurement Faults". *Navigation, vol. 72, iss. 4 (doi:10.33012/navi.718) (학술지)*.
- Andrew K. Sun, Hyosub Kil, Hyeyeon Chang, Woo Kyoung Lee, Jiyun Lee. "Do Solar Eclipses Generate Propagating Ionospheric Perturbations?". *Journal of Geophysical Research: Space Physics, vol. 130, iss. 6, pp. e2025JA033746 (doi:10.1029/2025JA033746) (학술지)*.
- Pil Hun Choi, Gihun Nam, Dongchan Min, Noah Minchan Kim, Jiyun Lee. "Fault Modes and Methods to Evaluate Integrity Risk for FastSLAM-Based Navigation". *IET Radar, Sonar & Navigation, vol. 19, iss. 1 (doi:10.1049/rsn2.70029) (학술지)*.
- Andrew K. Sun, Jiyun Lee, Sam Pullen, Maria Caamano. "A Stochastic Modeling Approach for Phase Transition-Induced Errors in GBAS under Ionospheric Scintillation". *Proceedings of the 38th International Technical Meeting of the Satellite Division of The Institute of Navigation (ION GNSS+ 2025), Baltimore, MD (doi:10.33012/2025.20391) (국제 학회)*.
- Maria Caamano, Daniel Gerbeth, Susumu Saito, Andrew K. Sun, Jiyun Lee, Sam Pullen. "Impact of Dual-Frequency Multi-Constellation GBAS Data Link Constraints on Integrity Monitoring". *Proceedings of the 38th International Technical Meeting of the Satellite Division of The Institute of Navigation (ION GNSS+ 2025), pp. 276-290 (doi:10.33012/2025.20303) (국제 학회)*.
- Dongchan Min, Jiyun Lee. "Enhancing Availability of SS-RAIM Based CDGNSS Using Integer Aperture Bootstrapping". *Proceedings of the 2025 International Technical Meeting of The Institute of Navigation, Long Beach, CA, pp. 331 - 342 (doi:10.33012/2025.20006) (국제 학회)*.
- Jaehee Chang, Andrew K Sun, Jihyeok Park, Jiyun Lee, Y. Jade Morton. "A Method of Estimating Residual Bending Error in GNSS-RO Absolute TEC". *Proceedings of the 2025 International Technical Meeting of The Institute of Navigation, Long Beach, CA, pp. 151-160 (doi:10.33012/2025.20005) (국제 학회)*.
- Junsoo Kim, Noah Minchan Kim, Donguk Kim, Jiyun Lee. "CNAV URA 기반 WAD-RNSS의 Advanced RAIM 성능 평가". *한국항공우주학회 추계학술대회 (국내 학회)*.
- Gihun Nam, Jimin Do, Jiyun Lee, Jeongtae Bae. "저궤도 위성 기반 SOP 항법 오차 요소 분석 및 성능 분석". *한국항공우주학회 추계학술대회 (국내 학회)*.
- Minseong Kim, Noah Minchan Kim, Dongchan Min, Gihun Nam, Jiyun Lee. "Deep Ensemble 추정 오차 분포에 대한 페어드 오버바운딩 적용". *한국항공우주학회 추계학술대회 (국내 학회)*.
- Jihyeok Park, Jaehee Chang, Kiyoung Sun, Jiyun Lee. "개선된 Kappa Correction 모델 기반 GNSS-RO 굴절각 잔여 전리권 오차의 보정 성능 분석". *항법시스템학회 정기학술대회 (국내 학회)*.
- Jonghyeon Park, Jihyeok Park, Jaehee Chang, Jiyun Lee. "Local Spectral Width 기반 적응형 Radio-holographic 필터를 이용한 GNSS-RO Phase Matching 기법 연구". *항법시스템학회 정기학술대회 (국내 학회)*.
- Jimin Do, Gihun Nam, Kiyoung Sun, Jiyun Lee. "NeQuick 보정 정보 모델의 저궤도 위성 잔류 전리층 지연 오차 분석". *항법시스템학회 정기학술대회 (국내 학회)*.
- Kiyoung Sun, Jiyun Lee. "전리권 신틸레이션 환경에서의 GBAS 무결성 연구". *항법시스템학회 정기학술대회 (국내 학회)*.
- Junsoo Kim, Noah Minchan Kim, Jiyun Lee, Donguk Kim. "한국형 WAD-RNSS를 위한 CNAV 기반 URA 산출 기법". *한국항공우주학회 우주학술대회 (국내 학회)*.
- Jihyeok Park, Jaehee Chang, Kiyoung Sun, Jiyun Lee. "GNSS RO 중성 대기 굴절각 내 잔여 전리권 오차 보정을 위한 Kappa Correction 모델 개선 연구". *한국항공우주학회 우주학술대회 (국내 학회)*.

**2024**

- Hyeyeon Chang, Woo Kyoung Lee, Hyosub Kil, Hyosang Yoon, Jiyun Lee. "Multiantenna-based Data Filling Method for Retrieving Electron Density Profiles from GNSS Radio Occultation Data". *IEEE Transactions on Geoscience and Remote Sensing, vol. 62 (doi:10.1109/TGRS.2024.3449337) (학술지)*.
- Hyosub Kil, Andrew K. Sun, Woo Kyoung Lee, Hyeyeon Chang, Jiyun Lee. "Assessment of the Origin of a Plasma Depletion Band Over the United States During the 8 September 2017 Geomagnetic Storm". *Geophysical Research Letters, vol. 51, iss. 7, pp. e2024GL108334 (doi:10.1029/2024GL108334) (학술지)*.
- Andrew K. Sun, Hyosub Kil, Hyeyeon Chang, Woo Kyoung Lee, Jiyun Lee. "Investigation of the Development of Traveling Ionospheric Disturbances during the Total Solar Eclipses on 21 August 2017 and 8 April 2024". *AGU Fall Meeting 2024, Washington D.C. (국제 학회)*.
- Andrew K. Sun, Charles L. Rino, Y. Jade Morton, Brian Breitsch, Jiyun Lee. "Phase Screen Model for Extreme Scintillations: Evaluating Theoretical Limits in Propagation Approximations". *AGU Fall Meeting 2024, Washington D.C. (국제 학회)*.
- Junsoo Kim, Gihun Nam, Dongchan Min, Jiyun Lee, Sam Pullen. "Minimum Separation Boundary for UAM Tactical Deconfliction Based on Avoidance Risk Ratio Model". *2024 AIAA DATC/IEEE 43rd Digital Avionics Systems Conference (DASC), San Diego, CA (doi:10.1109/DASC62030.2024.10748735) (국제 학회)*.
- Andrew K. Sun, Jiyun Lee, Sam Pullen. "Impact of Phase Transitions Due to Ionospheric Scintillation on GBAS Integrity". *Proceedings of the 37th International Technical Meeting of the Satellite Division of The Institute of Navigation (ION GNSS+ 2024), Baltimore, MD (국제 학회)*.
- Jaehee Chang, Andrew K. Sun, Jihyeok Park, Y. Jade Morton, Jiyun Lee. "Quantifying the Impact of Ionospheric Bending on GNSS-RO Absolute TEC Retrieval During Solar Cycle 25". *10th International Radio Occultation Working Group (IROWG-10), Boulder, CO (국제 학회)*.
- Andrew K. Sun, Hyosub Kil, Hyeyeon Chang, Woo Kyoung Lee, Jiyun Lee. "Assessment of Ionospheric Perturbations during Total Solar Eclipses". *45th COSPAR Scientific Assembly, Busan, Republic of Korea (국제 학회)*.
- Jaehee Chang, Andrew K. Sun, Jiyun Lee, Hyeyeon Chang, Yang Wang, Lei Liu, Y. Jade Morton, Douglas Hunt. "Estimation of the Residual Error due to Ionospheric Bending in Relative TEC using COSMIC-2 GPS-RO Measurements". *Proceedings of the ION 2024 Pacific PNT Meeting, pp. 22-35 (doi:10.33012/2024.19607) (국제 학회)*.
- Junsoo Kim, Gihun Nam, Dongchan Min, Noah Minchan Kim, Jiyun Lee. "Determining Minimum Separation Boundary for UAM Tactical Deconfliction". *Proceedings of the ION 2024 Pacific PNT Meeting, pp. 502 - 513 (doi:10.33012/2024.19601) (국제 학회)*.
- Andrew K. Sun, Y. Jade Morton, Jiyun Lee. "Ionospheric Scintillation Effects across Multiple Carrier Frequency Bands Transmitted from LEO Satellites". *Proceedings of the 2024 International Technical Meeting of The Institute of Navigation, Long Beach, CA, pp. 109 - 125 (doi:10.33012/2024.19525) (국제 학회)*.
- Gihun Nam, Jimin Do, Jiyun Lee, Gwanghee Jo. "LEO PNT 무결성 연구 동향". *한국항공우주학회 추계학술대회 (국내 학회)*.
- Jaeryoung Lee, Minseong Kim, Dongchan Min, Jiyun Lee. "몬테카를로 시뮬레이션을 통한 Factor Graph Optimization 기반 GNSS 시스템의 위치 오차 확률 분포 분석". *항법시스템학회 정기학술대회 (국내 학회)*.
- Jaehee Chang, Jiyun Lee. "광선 추적 시뮬레이션을 활용한 GNSS-RO 총전자량의 잔여 굴절 오차 분석". *항법시스템학회 정기학술대회 (국내 학회)*.
- Jihyeok Park, Jaehee Chang, Kiyoung Sun, Jiyun Lee. "기하 광학법 기반 중성 대기 굴절각 추정을 위한 GNSS-RO 데이터 처리 알고리즘 설계". *항법시스템학회 정기학술대회 (국내 학회)*.
- Minseong Kim, Dongchan Min, Minchan Kim, Jiyun Lee. "군집 위성 임무를 위한 GNSS및 상대 거리 측정치 기반 상대 항법 시스템 정확성 민감도 분석". *항법시스템학회 정기학술대회 (국내 학회)*.
- Jimin Do, Gihun Nam, Jiyun Lee. "저궤도 통신 위성과 GNSS 중궤도 위성을 활용한 항법 성능 분석 시뮬레이터 개발 및 정확도 민감도 분석". *항법시스템학회 정기학술대회 (국내 학회)*.
- Jonghyeon Park, Jaehee Chang, Jiyun Lee. "GNSS-RO 개루프 신호를 이용한 전리권 하층부 총전자량 산출 알고리즘 설계". *항법시스템학회 정기학술대회 (국내 학회)*.
- Jaeryoung Lee, Kiyoung Sun, Jiyun Lee. "한반도 지역에 대한 NeQuick G 모델의 TEC 추정 오차 분석 2024년 5월 10-11일 지자기 폭풍 사례 연구". *한국항공우주학회 우주학술대회 (국내 학회)*.
- Jaehee Chang, Kiyoung Sun, Jiyun Lee. "COSMIC-2 GNSS-RO 측정치를 활용한 단일 및 이중 주파수 기반 총전자량 비교 분석". *통신정보 합동학술대회 (국내 학회)*.

**2023**

- Jinsil Lee, Minchan Kim, Dongchan Min, Sam Pullen, Jiyun Lee. "Navigation Safety Assurance of a KF-Based GNSS/IMU System: Protection Levels Against IMU Failure". *NAVIGATION: Journal of the Institute of Navigation, vol. 70, iss. 4 (doi:10.33012/navi.612) (학술지)*.
- Andrew K. Sun, Hyosub Kil, Hyeyeon Chang, Jiyun Lee. "Study of the Characteristics and Sources of Late-Night Equatorial Electron Density Irregularities". *AGU Annual Meeting 2023, San Francisco, CA (국제 학회)*.
- Hyeyeon Chang, Lei Liu, Y. Jade Morton, Tibor Durgonics, Jun Wang, Dominic J. Fuller-Rowell, Douglas Hunt, John Braun, Jan-Peter Weiss, Jaehee Chang, Andrew K. Sun, Jiyun Lee. "Preliminary Assessment of Scintillation Data from the Spire Global and PlanetIQ Radio Occultation Constellation". *AGU Annual Meeting 2023, San Francisco, CA (국제 학회)*.
- Hyeyeon Chang, Jaehee Chang, Andrew K. Sun, Wookyoung Lee, Hyosub Kil, Jiyun Lee. "Performance Assessment of Ionospheric Electron Density Profiles retrieved from KOMPSAT-5 by Comparing with Ground-based and Space-based Observations". *AGU Annual Meeting 2023, San Francisco, CA (국제 학회)*.
- Jaehee Chang, Andrew K. Sun, Hyeyeon Chang, Yang Wang, Lei Liu, Douglas Hunt, Y. Jade Morton, Jiyun Lee. "Preliminary Assessment of the Residual Error due to Ionospheric Bending in the COSMIC-2 RO TEC by Comparing Results from Single- and Dual-frequency Methods". *AGU Annual Meeting 2023, San Francisco, CA (국제 학회)*.
- Junsoo Kim, Gihun Nam, Dongchan Min, Noah Minchan Kim, Jiyun Lee. "Safety Risk Assessment Based Minimum Separation Boundary". *2023 IEEE/AIAA 42nd Digital Avionics Systems Conference (DASC), Barcelona, Spain, pp. 1-8 (doi:10.1109/DASC58513.2023.10311141) (국제 학회)*.
- Andrew K. Sun, Jaehee Chang, Jiyun Lee, Brian Breitsch, Y. Jade Morton, Sam Pullen. "Mid-Latitude Ionospheric Scintillation Impact on Availability of Dual-frequency GNSS Augmentation Systems". *Proceedings of the 36th International Technical Meeting of the Satellite Division of The Institute of Navigation (ION GNSS+ 2023), Denver, Colorado (국제 학회)*.
- Dongchan Min, Noah Minchan Kim, Junsoo Kim, Jiyun Lee, Sam Pullen. "SS-RAIM based Integrity Architecture for CDGNSS Systems against Satellite Measurement Faults". *Proceedings of the 36th International Technical Meeting of the Satellite Division of The Institute of Navigation (ION GNSS+ 2023), Denver, Colorado, pp. 2550 - 2569 (doi:10.33012/2023.19219) (국제 학회)*.
- Noah Minchan Kim, Dongchan Min, Jiyun Lee. "Integrity Assurance of LIRTK Using SS-RAIM Against Sensor Faults for UAV Applications". *Proceedings of the 36th International Technical Meeting of the Satellite Division of The Institute of Navigation (ION GNSS+ 2023), Denver, Colorado, pp. 2242 - 2257 (doi:10.33012/2023.19457) (국제 학회)*.
- Jiyun Lee, Gihun Nam, Dongchan Min, Andrew K. Sun, Sam Pullen. "Network-Based Augmentation System (NBAS) Architectures Optimized to Support Urban Air Mobility (UAM)". *2023 International Technical Meeting of The Institute of Navigation, Long Beach, CA (doi:10.33012/2023.18603) (국제 학회)*.
- Andrew K. Sun, Jaehee Chang, Jiyun Lee, Brian Breitsch, Y. Jade Morton. "Availability Assessment of Dual-Frequency GNSS-Based Augmentation Systems Under Equatorial Ionospheric Scintillations". *2023 International Technical Meeting of The Institute of Navigation, Long Beach, CA, pp. 937-949 (doi:10.33012/2023.18617) (국제 학회)*.

**2022**

- Dongchan Min, Minchan Kim, Jinsil Lee, Mihaela-Simona Circiu, Michael Meurer, Jiyun Lee. "DNN-Based Approach to Mitigate Multipath Errors of Differential GNSS Reference Stations". *IEEE Transactions on Intelligent Transportation Systems, pp. 1-7 (doi:10.1109/TITS.2022.3207281) (학술지)*.
- Eugene Bang, Jiyun Lee. "Undersampled Ionospheric Irregularity Threat Parameterization Using a Three-Dimensional Model for Satellite-Based Augmentation Systems". *IEEE Transactions on Aerospace and Electronic Systems, pp. 1-24 (doi:10.1109/TAES.2022.3199192) (학술지)*.
- Hyeyeon Chang, Jiyun Lee, Hyosang Yoon, Y. Jade Morton, Alex Saltman. "Performance assessment of radio occultation data from GeoOptics by comparing with COSMIC data". *Earth, Planets and Space, vol. 74, no. 108 (doi:10.1186/s40623-022-01667-6) (학술지)*.
- Haerhee Park, Jinsil Lee, Jiyun Lee. "Error modelling method of extended Kalman filter-based terrain referenced navigation system for integrity assurance under nominal conditions". *IET Radar, Sonar & Navigation, vol. 16, no. 9, pp. 1516-1529 (doi:10.1049/rsn2.12277) (학술지)*.
- Hyosub Kil, Hyeyeon Chang, Woo Kyoung Lee, Larry J. Paxton, Andrew K. Sun, Jiyun Lee. "The Origin of Multitude Plasma Depletions Detected During the 12 February 2000 and 29 October 2003 Geomagnetic Storms". *Journal of Geophysical Research: Space Physics, vol. 127, no. 3 (doi:10.1029/2021JA030169) (학술지)*.
- Halim Lee, Sam Pullen, Jiyun Lee, Byungwoon Park, Moonseok Yoon, Jiwon Seo. "Optimal Parameter Inflation to Enhance the Availability of Single-Frequency GBAS for Intelligent Air Transportation". *IEEE Transactions on Intelligent Transportation Systems, pp. 1-8 (doi:10.1109/TITS.2022.3157138) (학술지)*.
- Dongwoo Kim, Jiyun Lee. "Kalman-filter-based Integrity Evaluation Considering Fault Duration: Application to GNSS-based Attitude Determination". *GPS Solutions, vol. 26, no. 51 (doi:10.1007/s10291-022-01234-2) (학술지)*.
- Hyeyeon Chang, Hyosub Kil, Andrew K. Sun, Shunrong Zhang, Jiyun Lee. "Ionospheric disturbances in low- and midlatitudes during the geomagnetic storm on 26 August 2018". *Journal of Geophysical Research: Space Physics, vol. 127, no. 2 (doi:10.1029/2021JA029879) (학술지)*.
- Hyosub Kil, Andrew K. Sun, Hyeyeon Chang, Larry J. Paxton, Romina Nikoukar, Jiyun Lee. "Characteristics and Sources of Electron Density Irregularities in the Low Latitude F Region". *AGU Fall Meeting 2022, Chicago, IL (국제 학회)*.
- Hyosub Kil, Hyeyeon Chang, Andrew K. Sun, Jiyun Lee. "Study of the drivers of the equatorial ionization anomaly using ICON and COSMIC2 data". *AGU Fall Meeting 2022, Chicago, IL (국제 학회)*.
- Hyeyeon Chang, Jaehee Chang, Andrew K. Sun, Woo Kyoung Lee, Jiyun Lee. "Preliminary results of electron density profiles retrieved from KOMPSAT-5 Radio Occultation Data". *AGU Fall Meeting 2022, Chicago, IL (국제 학회)*.
- Jaehee Chang, Hyeyeon Chang, Jiyun Lee. "Cycle Slip Mitigation for Total Electron Content Retrieval using GeoOptics Radio Occultation Data". *AGU Fall Meeting 2022, Chicago, IL (국제 학회)*.
- Gihun Nam, Andrew K. Sun, Jiyun Lee, Sam Pullen. "Networked UAV Detection and Alerting of Ionospheric Anomalies within LADGNSS Navigation Framework". *Proceedings of the 35th International Technical Meeting of the Satellite Division of The Institute of Navigation (ION GNSS+ 2022), Denver, Colorado, pp. 1529-1536 (doi:10.33012/2022.18424) (국제 학회)*.
- Gihun Nam, Dongchan Min, Noah Minchan Kim, Jiyun Lee, Sam Pullen. "Optimal Smoothing and Monitor Strategies for DFDC Local-Area DGNSS under Anomalous Ionospheric Conditions". *Proceedings of the 2022 International Technical Meeting of The Institute of Navigation, Long Beach, California, pp. 1156 - 1174 (doi:10.33012/2022.18166) (국제 학회)*.
- Noah Minchan Kim, Dongchan Min, Jiyun Lee. "Correct Fix Probability Improvement Method via INS Aiding to Single Epoch RTK System". *Proceedings of the 2022 International Technical Meeting of The Institute of Navigation, Long Beach, California, pp. 1304 - 1319 (doi:10.33012/2022.18167) (국제 학회)*.

**2021**

- Dongwoo Kim, Moonseok Yoon, Sam Pullen, Jiyun Lee. "Closed-form analysis of undetected range errors due to ionospheric impacts for GBAS category I operations". *NAVIGATION, vol. 68, no. 3, pp. 507-519 (doi:10.1002/navi.442) (학술지)*.
- Andrew K. Sun, Hyeyeon Chang, Sam Pullen, Hyosub Kil, Jiwon Seo, Y. Jade Morton, Jiyun Lee. "Markov Chain-based Stochastic Modeling of Deep Signal Fading: Availability Assessment of Dual-frequency GNSS-based Aviation under Ionospheric Scintillation". *Space Weather, vol. 19, no. 9, pp. e2020SW002655 (doi:10.1029/2020SW002655) (학술지)*.
- Hyeyeon Chang, Moonseok Yoon, Sam Pullen, Lenoardo Marini-Pereira, Jiyun Lee. "Ionospheric spatial decorrelation assessment for GBAS daytime operations in Brazil". *Navigation, vol. 68, no. 2, pp. 391-404 (doi:10.1002/navi.418) (학술지)*.
- Hyeyeon Chang, Hyosub Kil, Andrew K. Sun, Shunrong Zhang, Jiyun Lee. "Bubble-like Ionospheric Irregularities observed in the United States during the 26 August 2018 Geomagnetic Storm". *AGU Fall Meeting 2021, New Orleans, LA (국제 학회)*.
- Gihun Nam, Dongwoo Kim, Noah Minchan Kim, Jiyun Lee, Sam Pullen. "Enhanced Local-Area DGNSS for Autonomous Vehicle Navigation: Optimal Smoothing Strategy". *Proceedings of the 34th International Technical Meeting of the Satellite Division of The Institute of Navigation (ION GNSS+ 2021), St. Louis, Missouri, pp. 4080 - 4096 (doi:10.33012/2021.18066) (국제 학회)*.
- Andrew K. Sun, Jiyun Lee, Xiaoqing Pi, Martin Kriegel, Jens Berdermann. "GNSS Carrier Frequency Dependence of Ionospheric Scintillation Index in Equatorial Regions". *Proceedings of the XXXIVth URSI General Assembly and Scientific Symposium, Rome, Italy (국제 학회)*.
- Jaehee Chang, Hyeyeon Chang, Jiyun Lee. "Preliminary Assessment of GeoOptics and Spire CubeSat RO Performance by Comparing with COSMIC-2". *BIEN 2021, Daejeon (국제 학회)*.

## 수상

누리집 News 글 가운데 수상을 알리는 글이다. 날짜는 글의 게시일이다.[^news] 2022-07-08과 2022-08-30에 올라온 네 글은 2021년의 수상(2021 IPNT, 2021년 대학원생 국방학술대회, 2021년 한국항공우주학회 항공우주교육상, 한국해군과학기술학회 2021년도 동계 학술대회)을 알리며, 수상 날짜를 적지 않아 2021년 10월 이전의 수상일 수 있다.

- 2026-10-06 · Dr. Kiyoung Sun Receives the Kwon Sejin Fellowship (KSF)
- 2026-07-31 · Dr. Kiyoung Sun Wins RTCA William E. Jackson Award
- 2025-12-01 · Jinyoung Yun Wins Best Paper Award at 2025 IPNT Undergraduate Research Paper Competition
- 2025-12-01 · Dr. Kiyoung Sun Receives Outstanding Doctoral Dissertation Award from KAIST Aerospace Engineering Alumni Association
- 2025-12-01 · Dr. Kiyoung Sun Wins Best Presentation Award at ION GNSS+ 2025
- 2024-12-04 · Prof. Jiyun Lee Receives KSAS-Keumkok Young Researcher Award
- 2024-12-04 · Ph.D. Student Jaehee Chang awarded Best Paper Award at IPNT 2024
- 2024-11-01 · Ph.D. Student Junsoo Kim awarded Best of Conference (1st Place) Award at DASC 2024
- 2024-11-01 · Ph.D. Student Kiyoung Sun awarded Best Presentation Award at ION GNSS+ 2024
- 2024-03-08 · Prof. Jiyun Lee Receives 2023 Thurlow Award
- 2023-11-21 · M.S. Student Junsoo Kim awarded Best Paper Award at IPNT 2023
- 2023-11-21 · Ph.D. Student Minchan Kim awarded Best Presentation Award at ION GNSS+ 2023
- 2023-01-13 · Ph.D. Student Gihun Nam awarded Best Paper Award at IPNT 2022
- 2022-08-30 · M.S. Student Yun-Jung Kim awarded Best Paper Award at the Korea Society for Naval Science and Technology 2021 Winter Conference
- 2022-07-08 · 이지윤 교수, 한국항공우주학회 항공우주교육상 수상
- 2022-07-08 · Ph.D. Student Ki-young Sun awarded Excellent Paper Award at IPNT 2021
- 2022-07-08 · M.S. Student Yun-jung Kim awarded Grand Prize at the 2021 National Defense Academic Conference

## 소식

누리집 News 글 가운데 수상 글이 아닌 것으로, 2021년 10월 이후의 일을 알리는 다섯 글이다. 날짜는 글의 게시일이다. 2022-07-08에 올라온 두 글은 2021년 11월의 위촉을 알린다.[^news]

- 2023-11-21 · Prof. Jiyun Lee Appointed as KAIST Endowed Chair Professor
- 2023-01-13 · Prof. Jiyun Lee elected as ION Satellite Division Secretary
- 2022-08-07 · Prof. Jiyun Lee appointed as KAIST Ombudsperson
- 2022-07-08 · 이지윤 교수, 우주개발진흥실무위원회 제8기 민간위원 연임
- 2022-07-08 · Prof. Jiyun Lee appointed as a member of the Science and Technology Diplomacy Advisory Committee

## 연락과 위치

- 교수 연구실: N7-2 #4305[^prof][^aefac]
- 교수 전화: 042-350-3725[^prof][^aefac]
- 교수 이메일: jiyunlee@kaist.ac.kr[^prof][^aefac][^board]
[^p1]: A. K. Sun, S. Pullen, J. Lee, IEEE Transactions on Aerospace and Electronic Systems 62, 8505-8512 (2026). <https://doi.org/10.1109/taes.2025.3624709> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: E. Bang, J. Lee, IEEE Transactions on Aerospace and Electronic Systems, 1-24 (2022). <https://doi.org/10.1109/taes.2022.3199192> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Lee 외, J. Lee, NAVIGATION: Journal of the Institute of Navigation 70, navi.612 (온라인 2023-09-01). <https://doi.org/10.33012/navi.612> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: P. H. Choi 외, J. Lee, IET Radar, Sonar & Navigation 19, e70029 (온라인 2025-05-15). <https://doi.org/10.1049/rsn2.70029> 초록 기준.
[^p5]: D. Min 외, J. Lee, IEEE Transactions on Intelligent Transportation Systems 23, 25047-25053 (2022). <https://doi.org/10.1109/tits.2022.3207281> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: J. Kim 외, J. Lee, ION Pacific PNT, 502-513 (온라인 2024-05-08). <https://doi.org/10.33012/2024.19601> 초록 기준(연구실 누리집 Int. Conferences 페이지 게시 초록).
[^p7]: H. Chang 외, J. Lee, IEEE Transactions on Geoscience and Remote Sensing 62, 1-14 (2024). <https://doi.org/10.1109/tgrs.2024.3449337> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: A. K. Sun 외, J. Lee, Journal of Geophysical Research: Space Physics 130, e2025JA033746 (온라인 2025-06-04). <https://doi.org/10.1029/2025ja033746> 초록 기준.
[^home]: 연구실 누리집 첫 화면 <https://gnss.kaist.ac.kr/> (GNSS LAB, About Us, Latest News, 2026-10-23 열람)
[^board]: KAIST 항공우주공학과 연구실 소개 「위성항법시스템 연구실」 <https://ae.kaist.ac.kr/boards/view/board_lab/87> (교수, 연구실 소개, 웹사이트 주소, 이메일 주소, 연구분야, 2026-10-23 열람)
[^aefac]: KAIST 항공우주공학과 교수진 목록 <https://ae.kaist.ac.kr/boards/lists/board_faculty/sc_category/1/> (이지윤 항목의 직위, Career, Tel, Website, E-mail, 연구분야, 연구실, 2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <https://gnss.kaist.ac.kr/?page_id=71> (Office, E-mail, Phone, Education, Expertise, Research, Selected Honors and Awards, Selected Professional Activities, 2026-10-23 열람)
[^people]: 연구실 누리집 People 페이지 <https://gnss.kaist.ac.kr/?page_id=73>, Staff 페이지 <https://gnss.kaist.ac.kr/?page_id=1893>, Students 페이지 <https://gnss.kaist.ac.kr/?page_id=56> (2026-10-23 열람)
[^alumni]: 연구실 누리집 Alumni 페이지 <https://gnss.kaist.ac.kr/?page_id=69> (Ph. D., M. S., 2026-10-23 열람)
[^uam]: 연구실 누리집 Research > UAM Navigation 페이지 <https://gnss.kaist.ac.kr/?page_id=1334> (2026-10-23 열람)
[^remote]: 연구실 누리집 Research > Remote Sensing 페이지 <https://gnss.kaist.ac.kr/?page_id=1337> (2026-10-23 열람)
[^journal]: 연구실 누리집 Publications > Journal Articles 페이지 1·2쪽 <https://gnss.kaist.ac.kr/?page_id=108> (63 entries, 2026-10-23 열람)
[^intconf]: 연구실 누리집 Publications > Int. Conferences 페이지 1–3쪽 <https://gnss.kaist.ac.kr/?page_id=112> (126 entries, 2026-10-23 열람)
[^domconf]: 연구실 누리집 Publications > Dom. Conferences 페이지 <https://gnss.kaist.ac.kr/?page_id=114> (2026-10-23 열람)
[^news]: 연구실 누리집 News 페이지 1–3쪽 <https://gnss.kaist.ac.kr/?page_id=1379>와 각 글 페이지 (2026-10-23 열람)
[^rtca]: 연구실 누리집 News 글 「Dr. Kiyoung Sun Wins RTCA William E. Jackson Award」 <https://gnss.kaist.ac.kr/?p=2083> (2026-07-31 게시, 2026-10-23 열람)
[^n1819]: 연구실 누리집 News 글 「Ph.D. Student Minchan Kim awarded Best Presentation Award at ION GNSS+ 2023」 <https://gnss.kaist.ac.kr/?p=1819> (2023-11-21 게시, 2026-10-23 열람)
[^n1863]: 연구실 누리집 News 글 「Ph.D. Student Junsoo Kim awarded Best of Conference (1st Place) Award at DASC 2024」 <https://gnss.kaist.ac.kr/?p=1863> (2024-11-01 게시, 2026-10-23 열람)
[^n1824]: 연구실 누리집 News 글 「M.S. Student Junsoo Kim awarded Best Paper Award at IPNT 2023」 <https://gnss.kaist.ac.kr/?p=1824> (2023-11-21 게시, 2026-10-23 열람)
[^n1873]: 연구실 누리집 News 글 「Ph.D. Student Jaehee Chang awarded Best Paper Award at IPNT 2024」 <https://gnss.kaist.ac.kr/?p=1873> (2024-12-04 게시, 2026-10-23 열람)
[^n1817]: 연구실 누리집 News 글 「Prof. Jiyun Lee Appointed as KAIST Endowed Chair Professor」 <https://gnss.kaist.ac.kr/?p=1817> (2023-11-21 게시, 2026-10-23 열람)
[^n1848]: 연구실 누리집 News 글 「Prof. Jiyun Lee Receives 2023 Thurlow Award」 <https://gnss.kaist.ac.kr/?p=1848> (2024-03-08 게시, 2026-10-23 열람)
[^n1876]: 연구실 누리집 News 글 「Prof. Jiyun Lee Receives KSAS-Keumkok Young Researcher Award」 <https://gnss.kaist.ac.kr/?p=1876> (2024-12-04 게시, 2026-10-23 열람)

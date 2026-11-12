# 예보분석응용실험실 (Forecast, Analysis, Application Lab., FAA)

**서울대학교 자연과학대학 지구환경과학부 · 김정훈 부교수**

- 분야: 대기과학, 항공기상, 위험기상 예측
- 대분야: 에너지·환경·지구
- 태그: 기후·극한 기상[^meso], 유체역학·유동[^aviation][^meso]
- 홈페이지: <https://faa.snu.ac.kr/>
- 근거와 출처: [예보분석응용실험실 근거 페이지](faa-sources.md)

> 비행에 영향을 주는 바람·구름·얼음과 집중호우·강풍·안개의 발생 원리를 밝히고, 이를 항공 위험기상 예측과 안전한 비행경로 계산에 연결하는 연구실이다.[^research][^aviation][^meso]

## 무엇을 연구하나

예보분석응용실험실은 대기의 움직임을 나타내는 수식으로 날씨를 계산하는 수치예보모델과 실제 관측을 연결한다. 난류(액체나 기체의 흐름이 불규칙하게 변하며 여러 크기의 소용돌이를 만드는 현상), 착빙(물체 표면에 얼음이 형성되어 달라붙거나 쌓이는 현상), 깊은 대류(공기가 구름 속에서 높은 고도까지 오르내리는 운동)를 예측하고 비행경로를 계산하는 것이 항공기상 연구의 중심이다. 또 지상·레이더·위성 관측과 세밀한 수치모의를 함께 이용해 집중호우와 강풍 등 위험기상의 발생 원리를 연구한다.[^research][^aviation][^meso]

첫째 갈래는 **위험기상을 관측하고 그 세기를 추정하는 일**이다. 대표 논문 1은 무인항공기의 바람 관측으로 서울 근교 지표 부근 난류를 분석했다. 지면 가까운 곳에서 난류가 강하게 나타났고, 하천변 산책로와 건물에 둘러싸인 지역 사이에도 차이가 있었다. 초록은 건물이 흐름을 막는 효과를 지역 차이의 가능한 원인으로 제시한다.[^p1] 대표 논문 2는 위성의 여러 관측 채널을 기계학습에 연결해 대류 구름 주변 난류를 여러 높이에서 추정했다. 항공기 관측과 대조한 결과 아래쪽 높이 구간에서 좋은 성능을 보였고, 대류권계면(대류권과 성층권 사이의 경계)과 그 위에서는 정확도가 다소 낮아졌다.[^p2] 대류권은 지표에서 시작해 기상 현상이 주로 일어나는 대기층이고, 성층권은 그 위에서 높이에 따라 기온이 대체로 올라가는 대기층이다.

둘째 갈래는 **항공 운항에 쓸 예측 알고리즘을 만드는 일**이다. 연구실은 기온·상대습도·수직속도·구름 속 물의 양을 이용한 착빙 예측과, 서로 다른 수치모델·진단값을 묶은 앙상블 예측을 개발한다.[^aviation] 대표 논문 3은 기상청 전 지구 모델에 맞춰 착빙 예측 알고리즘을 조정하고 연구용 항공기 관측으로 평가했다.[^p3] 대표 논문 4는 깊은 대류 영역에 대한 확률예측과 발생 여부 예측을 함께 만들었으며, 개별 진단값이나 단일 모델 기반 예측보다 좋은 성능을 보였다.[^p4]

셋째 갈래는 **날씨가 비행경로와 비행시간에 주는 영향을 함께 계산하는 일**이다. 제트기류(상층 대기에서 띠 모양으로 빠르게 흐르는 바람)는 항로와 비행시간을 바꾸지만 주변 난류는 안전에 영향을 준다. 연구실은 유리한 바람을 따르는 경로와 난류를 피하는 경로를 비교한다.[^aviation] 대표 논문 5는 북대서양의 장기간 재분석 자료로 이 관계를 분석했다. 바람 변화로 생긴 비행시간 절약이 난류 회피에 필요한 시간 증가로 상쇄되거나 뒤집힐 수 있음을 보였다.[^p5]

넷째 갈래는 **넓은 기압계와 지역적인 공기 흐름이 함께 만드는 위험기상**이다. 연구실은 종관규모 환경과 중규모 과정의 상호작용을 집중호우·산악 강풍·안개에서 연구한다.[^meso] 대표 논문 6은 영남 지역 장마철 집중호우를 기압 유형별로 나누고 밤에 넓게 이동하는 비와 낮에 국지적으로 발생하는 비의 차이를 분석했다.[^p6] 대표 논문 7은 영동 지역 산맥 풍하측(바람이 산을 넘어 내려가는 쪽) 강풍의 기압 유형과 발생 원리를 비교했다.[^p7] 대표 논문 8은 황해에서 국지적으로 형성된 안개가 해안과 내륙으로 퍼지는 과정을 분석했다. 초기 형성에는 열복사에 의한 냉각이 지배적이었고, 지표 부근 부력(공기나 물 속에서 주변의 압력 차이 때문에 위쪽으로 받는 힘)으로 생긴 난류가 안개층의 수직 성장을 일으켰다.[^p8]

## 주요 연구 주제

### 항공 난류와 바람 변화

연구실은 산을 넘는 흐름에서 생기는 산악파(지형을 지나는 공기가 위아래로 진동하며 만드는 파동), 구름이 없는 곳의 청천난류, 지표 가까운 저고도 난류의 발생 원리를 연구한다. 흐름의 불안정과 높이에 따른 풍속 차이를 진단해 난류 예측을 만들고, 바람의 속도나 방향이 공간적으로 달라지는 윈드시어(Wind Shear)의 예측모델과 관측 기반 실시간 탐지 시스템도 개발했다. 연구실은 두 시스템이 나로우주센터에서 운영된다고 설명한다.[^aviation]

### 착빙과 깊은 대류 예측

영하에서도 액체로 남아 있는 과냉각 물방울은 비행 중 항공기에 얼음을 쌓이게 할 수 있다. 연구실은 수치예보모델이 계산한 대기와 구름 상태를 착빙 가능성으로 바꾸는 한국형 착빙 예측 알고리즘인 Korean Forecast Icing Potential을 개발했다. 깊은 대류 연구에서는 여러 모델과 진단값을 결합해 항공 운항에 위험한 구름 영역의 발생 가능성과 위치를 예측한다.[^aviation][^p3][^p4]

### 집중호우·지형성 강수·강풍

연구실은 기압계가 제공하는 넓은 환경 속에서 국지적인 공기 수렴, 대류에서 퍼져 나오는 흐름, 산악 지형이 강수를 어떻게 강화하는지 연구한다. 한국의 집중호우를 지형과 해안의 영향으로 나누고, 장기간 관측에서 중규모 대류계(여러 대류 구름이 조직적으로 모여 함께 움직이는 기상계)의 구조와 강수 기여를 분석한다. 산맥 아래로 가속하는 하강풍에서는 기압 유형과 산악파의 반사·붕괴 등을 비교하며 장기적인 특성과 미래 변화도 연구한다.[^meso]

### 해무와 항공 시정

연구실은 황해에서 발생해 인천국제공항 운항에 영향을 준 해무(바다 위에 생기는 안개)를 수치모의했다. 해수면 온도와 공기 온도의 차이가 변할 때 난류와 안개의 수직 발달이 어떻게 달라지는지 연구하고, 열복사·공기 이동·구름 속 물방울 과정의 기여를 분석한다.[^meso] 대표 논문 8은 국지 고기압과 낮은 고도의 역전층(높이에 따라 기온이 올라가는 공기층)이 안개 형성에 유리한 환경을 만들었던 황해 사례를 다룬다. 안개는 내륙으로 들어간 뒤 난류에 의한 혼합과 낮 동안의 건조로 소멸했으며, 초기 형성과 수직 성장에는 서로 다른 과정이 작용했다.[^p8]

### 기후 변동과 항로

연구실은 날마다 달라지는 날씨에 따른 경로 계산과 함께, 느리게 변하는 기후가 제트기류·선호 항로·비행시간을 어떻게 바꾸는지 연구한다. 북대서양에서는 난류 회피에 드는 시간 증가가 바람 변화에 따른 시간 절약을 상쇄할 수 있음을 분석했고, 태평양으로 연구를 넓히고 있다.[^aviation][^p5]

## 대표 논문

서울대 재직 시기의 논문 중 난류 관측·위성 추정·착빙·대류 예측·항로·집중호우·산악 강풍·안개를 고르게 다루도록 골랐다. 연도와 제목은 각 논문의 등록 서지를 따르며, ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2026 | [Analyses of Atmospheric Turbulence Near Surface Observed by Uncrewed Aerial Vehicle in the Suburban Area of Seoul Metropolitan, South Korea](https://doi.org/10.1029/2025gl119855)[^p1] | 서울 근교에서 무인항공기로 바람을 관측해 지표 부근 난류를 추정했다. 높이와 주변 도시 구조에 따라 난류가 달라 안전한 비행경로 계획에서 이를 고려해야 한다고 제시했다. |
| 2 | 2025 | [Machine Learning-Based Turbulence Intensity Estimation Near Convective Clouds in East Asia Using GK-2A Satellite Observations](https://doi.org/10.1029/2025gl119119)[^p2] | 여러 채널의 위성 자료를 학습모형에 넣어 여름철 난류 강도를 높이별로 추정했다. 항공기 관측과 대조하고 대류 주변 난류 감시를 보완할 가능성을 보였다. |
| 3 | 2024 | [Operational Aviation Icing Forecast Algorithm for the Korea Meteorological Administration](https://doi.org/10.1175/waf-d-23-0160.1)[^p3] | 기상청 전 지구 예보모델에 맞춰 착빙 예측 알고리즘의 입력과 가중치(각 입력값이 결과에 미치는 영향을 조절하는 계수)를 조정했다. 기존 방식에 비해 성능이 개선됐고 연구용 항공기 관측으로 한반도 착빙 예측 능력을 평가했다. |
| 4 | 2025 | [Multimodel and Multidiagnostic Ensemble-Based Deep Convective Area Forecast for Aviation Operations Using the Global Unified Model and Korean Integrated Model](https://doi.org/10.1175/waf-d-25-0006.1)[^p4] | 서로 다른 수치모델과 여러 대류 진단값을 결합해 위험한 구름 영역을 예측했다. 깊은 대류의 발생 여부와 확률을 예측하는 두 방식 모두 개별 진단값과 단일 모델 방식보다 좋은 성능을 보였다. |
| 5 | 2026 | [Combined impact of jet stream and turbulence on long-term trans-oceanic flight routes over North Atlantic Ocean using ERA5 reanalysis](https://doi.org/10.1038/s41598-026-57066-4)[^p5] | 북대서양 항로에서 바람이 주는 시간 절약과 난류 회피에 드는 시간을 함께 계산했다. 난류 회피 시간이 늘면서 바람 변화의 이득을 상쇄하거나 뒤집는 결과를 보였다. |
| 6 | 2025 | [Spatio-Temporal Characteristics of Heavy Rainfall Events During the Changma in Southeastern Korea](https://doi.org/10.1029/2025ea004351)[^p6] | 영남 지역 장마철 집중호우를 기압 유형으로 나눴다. 이동하는 저기압 아래의 야간 광역 강수와 북서태평양 아열대 고기압 가장자리의 낮 시간 국지 강수가 서로 다른 과정을 따른다는 점을 분석했다. |
| 7 | 2022 | [Classification of Synoptic Patterns With Mesoscale Mechanisms for Downslope Windstorms in Korea Using a Self-Organizing Map](https://doi.org/10.1029/2021jd035867)[^p7] | 영동 지역 산맥 풍하측 강풍을 기압 유형으로 분류했다. 유형마다 공기 흐름과 산악파 작용이 달라지는 점을 분석해 강풍 예측과 미래 변화 연구에 쓸 수 있는 분류를 제시했다. |
| 8 | 2026 | [Numerical simulation and physical understanding of a locally initiated sea fog event over the eastern Yellow Sea with a transition of air–sea temperature difference](https://doi.org/10.1002/qj.70228)[^p8] | 관측과 수치모의로 황해 해무의 형성·내륙 이동·소멸·수직 발달을 분석했다. 초기 형성에는 열복사에 의한 냉각이 지배적이었고, 안개층의 수직 성장에는 지표 부근 부력으로 생긴 난류가 작용했다. |

## 교수와 전문 분야

김정훈 부교수의 전공은 일기예보 및 응용기상이다. 부경대학교 대기과학 학사(2003), 강릉원주대학교 대기과학 석사(2006), 연세대학교 대기과학 박사(2011)를 받았다. 연세대학교 박사후연구원, 미국 항공우주국 Ames Research Center 박사후연구원, 미국 해양대기청 항공기상센터에서 연구 경력을 쌓은 뒤 2018년 서울대학교 조교수로 부임했으며 2023년부터 부교수로 재직한다.[^faculty][^prof]

전문 분야는 관측과 수치모의를 이용한 위험기상의 원리 분석, 항공 난류·착빙·대류 예측, 기상 조건을 고려한 항로 계산이다. 연구실은 대기과학 지식을 항공 운항의 안전과 효율에 연결하는 방향을 제시한다.[^research][^aviation][^meso]

## 응용 분야

연구실은 항공기 운항의 난류·착빙·깊은 대류 회피, 공항 저고도 위험기상 예측, 바람과 난류를 고려한 비행경로, 우주 발사 운용의 윈드시어 감시를 응용 대상으로 든다. 집중호우와 산악 강풍의 발생 원리 연구는 위험기상 예측과 재난 대응을 위한 이해를 높이는 데 목적이 있다.[^aviation][^meso]

## 구성원

2026년 11월 12일 People에 게시된 현재 구성원 18명이다. 교수 1명, 연구원 3명, Ph. D. Candidate 8명, Ph. D. Student 5명, Master's Student 1명이며 과정·공개 연구 주제·학교 이메일은 랩 게시 표기를 따른다. ‘대표 논문 참여’는 위 표의 번호이고, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 김정훈(Jung-Hoon Kim) | Associate Professor |  | jhkim99@snu.ac.kr | 1, 2, 3, 4, 5, 6, 7, 8 |
| 민재식(Jae-Sik Min) | 연구원 | Atmospheric boundary layer analysis using ground-based observations | min_jaesik@snu.ac.kr | 1 |
| 이단비(Dan-Bi Lee) | 연구원 | Aviation Turbulence |  | 2, 4 |
| 이윤진(Yoonjin Lee) | 연구원 |  | yoonjin1217@snu.ac.kr | 2 |
| 김정회(Jeonghoe Kim) | Ph. D. Candidate | Low-level turbulence | jeonghoekim.14@snu.ac.kr | 1, 8 |
| 백성호(Sung-Ho Baek) | Ph. D. Candidate | Convective-Related Turbulence | shbaek2629@snu.ac.kr |  |
| 김은태(Eun-Tae Kim) | Ph. D. Candidate | Aircraft icing, Heavy Snowfall, Orographic effect | etkim97@snu.ac.kr |  |
| 신예원(Yewon Shin) | Ph. D. Candidate | Mountain Wave Turbulence & Downslope Windstorm; 석사 학위논문: 태백산맥 풍하측 강풍의 종관규모 유형과 중규모 메커니즘 연구 (2023. 02.) | yesone42@snu.ac.kr | 7 |
| 이주헌(Ju Heon Lee) | Ph. D. Candidate | Aviation Turbulence (Clear-air turbulence, Near-cloud turbulence); 석사 학위논문: 수치모델링 실험을 통한 태풍 하기비스 주변 난류 발생 메커니즘 특성 이해 (2023. 02.) | juheon919@snu.ac.kr |  |
| 박이준(Yi-June Park) | Ph. D. Candidate | Mesoscale convective system, Extreme/heavy rainfall event, Mesoscale simulation | pijasd@snu.ac.kr | 4, 6 |
| 김주섭(Juseob Kim) | Ph. D. Candidate | Aviation Meteorology (Wind shear, Turbulence) | kjs2350@snu.ac.kr |  |
| 박준석(Junseok Park) | Ph. D. Candidate | Mesoscale Convective System | junseokp@snu.ac.kr |  |
| 김준희(Joon Hee Kim) | Ph. D. Student | Aviation Meteorology (Aircraft routing, Clear-air turbulence, Jet stream) | ktx7364@snu.ac.kr | 5 |
| 박정훈(Junghoon Park) | Ph. D. Student | Jet Superposition, High-impact Weather Events | junghoon1473@snu.ac.kr |  |
| 강준호(Junho Kang) | Ph. D. Student | Mountain Meteorology (Downslope Windstorm, Orographic Precipitation) | leonardo47@snu.ac.kr |  |
| 백서현(Seohyun Baek) | 석사과정 |  | seohyun49@snu.ac.kr |  |
| 배혁진(Hyeokjin Bae) | Ph. D. Student | Low-level turbulence | hyeokjin3860@snu.ac.kr |  |
| 최은호(Eunho Choi) | Ph. D. Student | Wind shear, Atmospheric turbulence and observations | ehchoi219@snu.ac.kr |  |

## 졸업생과 이전 연구원

Alumni 구획에 Former Researcher로 게시된 7명이다. 학위 논문 뒤 연월은 누리집 표기다.[^people][^alumni]

| 이름 | 게시 역할·학위·연도 | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| 이은정(Eunjeong Lee) | Former Researcher | KIAPS |  |
| 박자린(Ja-Rin Park) | Former Researcher | KIAPS |  |
| 노유정(Yoo-Jeong Noh) | Former Researcher | CSU/CIRA |  |
| 김수현(Soo-Hyun Kim) | Former Researcher | NASA |  |
| 변가영(Ka-Young Byeon) | Former Researcher | Korea Meteorological Administration | 석사 학위논문: 2019년 3월 15일 한반도 발생 토네이도 사례의 종관 분석 및 중규모 메커니즘 연구 (2023. 08.) |
| 양성일(Sung-Il Yang) | Former Researcher |  | 석사 학위논문: 한반도에서 발생한 중규모 대류계 주변의 난류 발생 메커니즘 사례 연구 (2024. 02.) |
| 정민혁(Minhyeok Jung) | Former Researcher | Korea Polar Research Institute |  |

People의 Students 구획에는 김정민(Jeongmin Kim)이 Former Researcher로 기재되어 있다.[^former]

## 최근 논문 목록 (2021–2026)

연구실 Publication에 게시된 학술지 논문 31편이다. 제목·저자·발표처·연도는 연구실 표기이며 별표는 누리집 표시 *다. DOI가 있는 항목에는 링크를 붙였다.[^publications] 2021년은 연도 구역을 포함하며, 날짜가 밝혀진 논문은 2021년 10월 22일 이후를 따른다. 대표 논문 표의 연도·제목은 등록 서지 기준이다.

**2026**

- Kim, S.-H., J.-H. Kim\*, J. Kim, J.-S. Min, 2026. "[Analyses of Low-Level Turbulence Observed by Unmanned Aerial Vehicle in Suburb of Seoul Metropolitan](https://doi.org/10.1029/2025gl119855)". *Geophysical Research Letter, 53, e2025GL119855*.
- Kim, E.-T. and J.-H. Kim\*, S.-M. Kim, and Y.-J. Lim, 2026. "[Orographic and Coastal Impacts on Unexpected Snowstorm Development in Seoul Metropolitan Area](https://doi.org/10.1016/j.uclim.2026.102999)". *Urban Climate, 68, 102999*.
- Kim, J. H., and J.-H. Kim\*, 2026. "[Combined Impact of Jet stream and Turbulence on Long-term Trans-Oceanic Flight Routes over North Atlantic Ocean using ERA5 reanalysis data](https://doi.org/10.1038/s41598-026-57066-4)". *Scientific Reports, 16, 27143 (2026)*.

**2025**

- Kim, J., J.-H. Kim\*, C. E. Dorman, and H. J. S. Fernando, 2025. "[Numerical simulation and physical understanding of a locally initiated sea fog over Eastern Yellow Sea with a transition of air-sea temperature difference](https://doi.org/10.1002/qj.70228)". *Quarterly Journal of the Royal Meteorological Society, e70228*.
- Shin, Y., J.-H. Kim\*, R. D. Sharman, T. L. Keller, S. B. Trier, and J. D. Doyle, 2025. "[Generation Mechanisms of Mountain-Wave Turbulence in the Upper Troposphere and Lower Stratosphere over Alaska](https://doi.org/10.1175/mwr-d-25-0166.1)". *Monthly Weather Review, 154, 813–834*.
- Dorman, C. E., J. Kim, J.-H. Kim, D. Koračin, R. N. Dimitrova, and H. J. S. Fernando, 2025. "[An anatomy of fog over Nova Scotia under a ridge on 8 September 2021](https://doi.org/10.1002/qj.70139)". *Quarterly Journal of the Royal Meteorological Society, e70139*.
- Lee, Y., D.-B. Lee, and J.-H. Kim\*, 2025. "[Machine Learning-Based Turbulence Intensity Estimation Near Convective Clouds in East Asia Using GK-2A Satellite Observations](https://doi.org/10.1029/2025gl119119)". *Geophysical Research Letters, e2025GL119119*.
- Park, Y.-J., J.-H. Kim\*, S.-W. Son, Y.-M. Cha, E.-J. Cha, S.-S. Shin, and H.-S. Kang, 2025. "[Spatio-Temporal Characteristics of Heavy Rainfall Events During the Changma in Southeastern Korea](https://doi.org/10.1029/2025ea004351)". *Earth and Space Science, e2025EA004351*.
- Park, Y.-J., J.-H. Kim\*, D.-B. Lee, H.-J. Choi, S.-H. Kim, M. Steiner, and S. H. Kim, 2025. "[Multi-Model and -Diagnostic Ensemble-based Deep Convective Area Forecast for Aviation Operations using the Global Unified Model and Korean Integrated Model](https://doi.org/10.1175/waf-d-25-0006.1)". *Weather and Forecasting, 40(10), 2055-2077*.
- Park, J.-S. and J.-H. Kim\*, 2025. "[Lightning Climatology over the Korean Peninsula and Its Relationship with Topography and Atmospheric Condition](https://doi.org/10.14191/atmos.2025.35.3.345)". *Atmosphere, 35(3), 345-367. (In Korean with English abstract)*.
- Kang, J., Y. Shih, and J.-H. Kim\*, 2025. "[Classification of Synoptic Flows and Mesoscale Mechanisms for Downslope Windstorms in the Lee of Sobaek Mountains in Korea](https://doi.org/10.14191/atmos.2025.35.3.293)". *Atmosphere, 35(3), 293-313. (In Korean with English abstract)*.
- Jung, M. and J.-H. Kim\*, 2025. "Characteristics of Sea Breezes on the Three Coasts of the Korean Peninsula Using Long-Term Ground Observation Data". *Atmosphere, 35(2), 193-205. (In Korean with English abstract)*.
- Lee, J., J.-H. Kim\*, S. B. Trier, R. D. Sharman, and J. D. Doyle, 2025. "[Generation Mechanisms of Near-Cloud Turbulence Events in the Upper-Level Outflow of Tropical Cyclone Hagibis](https://doi.org/10.1175/mwr-d-24-0116.1)". *Monthly Weather Review, 153(3), 521-542*.
- Kim, J.-S., J.-H. Kim\*, D.-B. Lee, and G. Lee, 2025. "[Characteristics of Convectively Induced Turbulence Derived from the Weather Radar Data in Korea](https://doi.org/10.14191/atmos.2025.35.1.065)". *Atmosphere, 35(1), 65–84. (In Korean with English abstract)*.

**2024**

- Baek, S.-H., J.-H. Kim\*, S.-H. Kim, Y. Lee, Y.-J. Noh, and S.-M. Lee, 2024. "[Characteristics of Convectively Induced Turbulence in East Asia Using Geostationary Korea Multi-Purpose Satellite-2A (GK-2A) and In Situ Aircraft Data](https://doi.org/10.1029/2024jd041671)". *JGR Atmospheres, e2024JD041671*.
- Byeon, G.-Y., J.-H. Kim\*, and Y.-J. Park, 2024. "[Synoptic and Meso Scale Mechanisms of Reported Tornado-like Gust Wind Event in Korea Using High-resolution Numerical Simulation](https://doi.org/10.14191/atmos.2024.34.4.397)". *Atmosphere, 34(4), 397-415. (In Korean with English abstract)*.
- Yang, S.-I., J. H. Lee, and J.-H. Kim\*, 2024. "[A Case Study on Near-Cloud Turbulence around the Mesoscale Convective System in the Korean Peninsula](https://doi.org/10.14191/atmos.2024.34.2.153)". *Atmosphere, 34(2), 153-176. (In Korean with English abstract)*.
- Kim, E. -T., J. -H. Kim\*, S. -H. Kim, and C. Morcrette, 2024. "[Operational Aviation Icing Forecast Algorithm for the Korea Meteorological Administration](https://doi.org/10.1175/waf-d-23-0160.1)". *Weather and Forecasting, 39(3), 501-521*.

**2023**

- Lee, Y., S. Kim, Y. Noh, and J. -H. Kim, 2023. "[Deep Learning–Based Summertime Turbulence Intensity Estimation Using Satellite Observations](https://doi.org/10.1175/jtech-d-22-0137.1)". *Journal of Atmospheric and Oceanic Technology, 40(11), 1433-1448*.
- Ko, H. -C., H. -Y. Chun, R. D. Sharman, and J. -H. Kim, 2023. "[Comparison of eddy dissipation rate estimated from operational radiosonde and commercial aircraft observations in the United States](https://doi.org/10.1029/2023jd039352)". *JGR Atmoshperes, 128(20), e2023JD039352*.
- Kim, S. -H.\*, J. -H. Kim\*, H. -Y. Chun, and R. D. Sharman, 2023. "[Global response of upper-level aviation turbulence from various sources to climate change](https://doi.org/10.1038/s41612-023-00421-3)". *npj Climate and Atmoshperic Science, 6, 92*.
- Lee, J. H., Kim, J. -H.\*, Sharman, R. D., Kim, J., and Son, S. -W., 2023. "[Climatology of Clear-Air Turbulence in Upper Troposphere and Lower Stratosphere in the Northern Hemisphere Using ERA5 Reanalysis Data](https://doi.org/10.1029/2022jd037679)". *JGR Atmospheres, 128(1), e2022JD037679*.
- Park, Y. and J.-H. Kim\*, 2023. "[Aviation Convective Index for Deep Convective Area using the Global Unified Model of the Korean Meteorological Administration, Korea: Part 2. Seasonal Optimization and Case Studies](https://doi.org/10.14191/atmos.2023.33.5.531)". *Atmosphere, 33(5), 519-530. (In Korean with English abstract)*.
- Park, Y. and J.-H. Kim\*, 2023. "[Aviation Convective Index for Deep Convective Area using the Global Unified Model of the Korean Meteorological Administration, Korea: Part 1. Development and Statistical Evaluation](https://doi.org/10.14191/atmos.2023.33.5.519)". *Atmosphere, 33(5), 531-548. (In Korean with English abstract)*.

**2022**

- Tsai, C. -L., K. Kim, Y. -C. Liou, J. -H. Kim, and G. Lee, 2022. "[Orographic-Induced Strong Wind Associated with a Low-Pressure System under Clear-Air Condition During ICE-POP 2018](https://doi.org/10.1029/2021jd036418)". *JGR Atmospheres, 127(13), e2021JD036428*.
- Kim, S. -H., J. Kim, J. -H. Kim\*, and H. -Y. Chun, 2022. "[Characteristics of the Derived Energy Dissipation Rate using 1-Hz Commercial Aircraft Quick Access Recorder (QAR) Data](https://doi.org/10.5194/amt-15-2277-2022)". *Atmoshpereic Measurement Techniques, 15(7), 2277-2298*.
- Park, J. -R., J. -H. Kim\*, Y. Shin, S. -H. Kim, H. -Y. Chun, W. Jang, C. -L. Tsai, and G. Lee, 2022. "[A Numerical Simulation of Strong Windstorm Event in the Taebaek Mountain Region during the ICE-POP 2018](https://doi.org/10.1016/j.atmosres.2022.106158)". *Atmospheric Research, 272, 106158*.
- Shin, Y., J. -H. Kim\*, H. -Y. Chun, W. Jang, and S. -W. Son, 2022. "[Classification of Synoptic Patterns for Downslope Windstorms in Korea using the Self-Organizing Map](https://doi.org/10.1029/2021jd035867)". *JGR Atmospheres, 127(6), e2021JD035867*.
- Lee, D. -B., H. -Y. Chun, S. -H. Kim, R. D. Sharman, and J. -H. Kim, 2022. "[Development and evaluation of Global Korean Aviation Turbulence Forecast Systems with outputs of an Operational Numerical Weather Prediction Model and In Situ Flight Turbulence Observation Data](https://doi.org/10.1175/waf-d-21-0095.1)". *Weather and Forecasting, 37(3), 371-392*.
- Kim, J. and J. -H. Kim\*, 2022. "[Retrieval and quality assessment of atmospheric wind from the aircraft-based observation near Incheon International Airport, Korea](https://doi.org/10.14191/atmos.2022.32.4.323)". *Atmosphere, 32(4), 323-340. (In Korean with English abstract)*.

**2021**

- Park, C., S. -W. Son, J. Kim, E. -C. Chang, J. -H. Kim, E. Jo, D. -H. Cha, and S. Jeong, 2021. "[Diverse synoptic weather patterns of warm-season heavy rainfall events in South Korea](https://doi.org/10.1175/mwr-d-20-0388.1)". *Monthly Weather Review, 149(11), 3875-3893*.

## 과제

첫 화면에 게시된 과제 7건이다. 수행 기간이 2021년 10월 22일–2026년 10월 22일과 겹치는 과제로, 지원기관과 기간은 연구실 표기다.[^home]

- 공항기상 예측 및 후처리 기술개발 (지원 한국기상산업기술원; 기간 2022-2026)
- 공항•공역 위험기상 확률예측 기술개발 (지원 한국기상산업기술원; 기간 2022-2026)
- 지형 등 외부요인에 의한 강수발달 효과 분석 (지원 한국기상산업기술원; 기간 2023-2027)
- 대기 중력파와 관련된 비대류 난류 발생 메커니즘 및 장기 변동성 연구 (지원 한국연구재단; 기간 2019-2024)
- 윈드시어예측모듈 검증 및 발사 적용을 위한 연구 (지원 항공우주연구원; 기간 2023-2025)
- 공항 특화 저고도 항공기상 모델링 기반 기술 개발 (지원 국립기상과학원; 기간 2022-2024)
- 지역별 강수 현상의 시공간 구조 특성 분석 및 예보활용기술 개발 (지원 국립기상과학원; 기간 2022-2024)

## 수상과 선정

연구실 소식과 구성원 소개에 게시된 수상 5건이다. 연도는 누리집의 사건 연도 표기이고 날짜는 게시되어 있지 않다.[^awards][^student-awards]

- 2025 · 김은태: 세계기상의 날 기념 항공기상업무 발전 유공자 포상
- 2024 · 박준석: 한국기상학회 가을학술대회 우수논문발표상
- 2023 · 김주섭: 한국기상학회 가을학술대회 우수논문발표상
- 2023 · 신예원·양성일: 한국기상학회 봄학술대회 우수논문발표상
- 2022 · 김은태·신예원: 한국기상학회 봄학술대회 우수논문발표상

## 연락과 위치

- 교수 이메일: jhkim99@snu.ac.kr[^people][^prof]
- 교수 연구실: 서울대학교 501동 421호, 전화 02-880-6718[^faculty][^people]
- 실험실: 서울시 관악구 관악로 1 서울대학교 501동 508호, 전화 02-880-8124[^faculty][^home]

## 각주
[^research]: 연구실 Research, 항공 위험기상 예측과 중규모 위험기상의 연구 방향. <https://faa.snu.ac.kr/research/> 관측 2026-11-12.
[^aviation]: 연구실 Aviation Meteorology, 난류·윈드시어·착빙·대류·비행경로 연구 소개. <https://faa.snu.ac.kr/research/aviation-meteorology/> 관측 2026-11-12.
[^meso]: 연구실 Mesoscale Severe Weather, 집중호우·지형성 강수·중규모 대류계·산맥 풍하측 강풍·해무 연구 소개. <https://faa.snu.ac.kr/research/mesoscale-severe-weather/> 관측 2026-11-12.
[^faculty]: 서울대학교 지구환경과학부 김정훈 교수 소개, 직급·전공·연구실·실험실·학력·주요 경력. <https://sees.snu.ac.kr/research-faculty/faculty/fulltime?mode=view&profidx=51> 관측 2026-11-12.
[^prof]: 연구실 Professor, Jung-Hoon Kim, 직급·연락처·경력·학력. <https://faa.snu.ac.kr/member/prof/> 관측 2026-11-12.
[^people]: 연구실 People, 현재 구성원·과정·연구 주제·연락처와 이전 연구원·학위 논문·진로. <https://faa.snu.ac.kr/people/> 관측 2026-11-12.
[^alumni]: 연구실 Alumni 개별 소개 7명. <https://faa.snu.ac.kr/member/soo-hyun-kim/> <https://faa.snu.ac.kr/member/minhyeok-jung/> <https://faa.snu.ac.kr/member/eunjeong-lee/> <https://faa.snu.ac.kr/member/ja-rin-park/> <https://faa.snu.ac.kr/member/dr-yoo-jeong-noh/> <https://faa.snu.ac.kr/member/sung-il-yang/> <https://faa.snu.ac.kr/member/ka-young-byeon/> 관측 2026-11-12.
[^former]: 연구실 Students, Jeongmin Kim, Former Researcher 표기. <https://faa.snu.ac.kr/member/jeongmin-kim/> 관측 2026-11-12.
[^publications]: 연구실 Publication 및 논문별 상세, 저자·제목·학술지·연도·DOI. <https://faa.snu.ac.kr/publication/> 관측 2026-11-12.
[^home]: 연구실 첫 화면, What we are working on 과제 7건과 실험실 연락·위치. <https://faa.snu.ac.kr/> 관측 2026-11-12.
[^awards]: 연구실 소식, 2024년 가을·2023년 가을·2023년 봄·2022년 봄 한국기상학회 우수논문발표상. <https://faa.snu.ac.kr/announcements/document/60/> <https://faa.snu.ac.kr/announcements/document/58/> <https://faa.snu.ac.kr/announcements/document/57/> <https://faa.snu.ac.kr/announcements/document/56/> 관측 2026-11-12.
[^student-awards]: 연구실 Eun-Tae Kim 소개, 2025년 세계기상의 날 기념 항공기상업무 발전 유공자 포상 및 2022년 한국기상학회 봄학술대회 우수논문발표상. <https://faa.snu.ac.kr/member/eun-tae-kim/> 관측 2026-11-12.
[^p1]: S.-H. Kim, J.-H. Kim, J. Kim, J.-S. Min, Geophysical Research Letters (2026). <https://doi.org/10.1029/2025gl119855> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100405461,publication_year:2021-2026>. 관측 2026-11-12.
[^p2]: Y. Lee, D.-B. Lee, J.-H. Kim, Geophysical Research Letters (2025). <https://doi.org/10.1029/2025gl119119> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100405461,publication_year:2021-2026>. 관측 2026-11-12.
[^p3]: E. T. Kim, J.-H. Kim, S.-H. Kim, C. J. Morcrette, Weather and Forecasting (2024). <https://doi.org/10.1175/waf-d-23-0160.1> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100405461,publication_year:2021-2026>. 관측 2026-11-12.
[^p4]: Y.-J. Park 외, S. H. Kim, Weather and Forecasting (2025). <https://doi.org/10.1175/waf-d-25-0006.1> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100405461,publication_year:2021-2026>. 관측 2026-11-12.
[^p5]: J. H. Kim, J.-H. Kim, Scientific Reports (2026). <https://doi.org/10.1038/s41598-026-57066-4> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100405461,publication_year:2021-2026>. 관측 2026-11-12.
[^p6]: Y.-J. Park 외, H.-S. Kang, Earth and Space Science (2025). <https://doi.org/10.1029/2025ea004351> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100405461,publication_year:2021-2026>. 관측 2026-11-12.
[^p7]: Y. Shin 외, S.-W. Son, Journal of Geophysical Research Atmospheres (2022). <https://doi.org/10.1029/2021jd035867> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100405461,publication_year:2021-2026>. 관측 2026-11-12.
[^p8]: J. Kim, J.-H. Kim, C. E. Dorman, H. J. S. Fernando, Quarterly Journal of the Royal Meteorological Society (2026). <https://doi.org/10.1002/qj.70228> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1002/qj.70228>. 관측 2026-11-12.

# 음향 및 진동 연구실 (Acoustics and Vibration Laboratory)

**서울대학교 공과대학 기계공학부 · 강연준 교수**

- 분야: 음향 재료, 차량 소음과 진동, 실험·해석 결합, 소음 제어, 제품 음질[^department][^intro]
- 대분야: 기계·로봇·제조, 소재
- 태그: 진동·소음 공학[^tpa][^brake], 음향·오디오 AI[^active]
- 홈페이지: <https://acustica.snu.ac.kr/>
- 근거와 출처: [음향 및 진동 연구실 근거 페이지](acustica-sources.md)

> 자동차와 기계에서 소리와 떨림이 생기고 전해지는 과정을 분석하고, 소음을 줄이는 재료·부품·제어 방법과 제품의 소리를 평가하는 방법을 연구한다.[^intro][^department]

## 무엇을 연구하나

연구실은 1997년 3월 설립되었으며, 자동차의 소음과 진동을 중심으로 연구한다. 진동은 물체의 위치 등 측정할 수 있는 양이 기준 상태 주위에서 반복적으로 변하는 현상이다. 연구실은 재료 안에서 소리가 약해지는 과정, 부품 사이로 떨림이 전달되는 과정, 사람이 제품 소리를 받아들이는 방식을 함께 다룬다. 소음·진동·거친 승차감을 아우르는 NVH(Noise, Vibration and Harshness)가 주요 응용 분야다.[^intro][^brake][^quality]

첫째는 **소음을 줄이는 재료의 성질을 예측하는 연구**다. 여기서 에너지는 물리계가 일을 하거나 상태를 변화시킬 수 있는 능력을 나타내는 물리량이다. 흡음재(입사한 소리의 에너지를 흡수하는 재료)와 차음재(소리가 반대쪽으로 전달되는 것을 줄이는 재료)를 다룬다. 재료 내부의 빈 공간과 뼈대가 소리에 어떻게 반응하는지 계산하고, 열에 오래 노출되어 내부 구조가 변할 때 흡음 성능이 어떻게 달라지는지도 분석한다.[^macro][^aging] 섬유 단면 영상과 신경망(연결된 계산 단위들의 신호 전달로 자료의 관계를 학습하는 계산 모형)을 연결해 재료의 성질을 예측하는 방법도 연구한다.[^soundai]

둘째는 **소리와 진동이 어느 부품을 거쳐 전달되는지 밝히는 연구**다. 노면 소음은 달리는 차량의 타이어와 도로가 상호작용하면서 생기는 소음이다. 연구실은 전달 경로 분석(소음·진동의 발생원에서 관측 지점까지 이르는 경로별 기여를 구하는 방법)을 통해 현가장치(차체와 바퀴를 연결하고 도로의 충격과 진동을 조절하는 장치)의 각 부품이 차실 소음에 미치는 영향을 구한다.[^tpa] 또 부품별 실험 결과와 계산 모형을 결합해 조립된 구조의 반응을 예측한다. 계산 모형은 대상의 성질과 움직임을 수학적 관계로 나타내어 계산할 수 있게 한 모형이다. 계산만으로 다루기 어려운 실제 특성과 실험만으로 얻기 어려운 연결 지점의 정보를 함께 활용하는 방향이다.[^substructure][^hybrid]

셋째는 **학습 모형과 사람이 듣는 소리를 연결하는 연구**다. 능동 소음 제어(원래 소음과 겹쳐 소리를 상쇄하도록 제어음을 발생시키는 방법)에서는 승객의 위치나 탑승 여부에 따라 스피커에서 귀까지 소리가 전달되는 특성이 달라지는 문제를 다룬다. 연구실은 이런 변화에 맞춰 전달 특성을 예측하는 학습 모형을 연구한다.[^active] 기계가 내는 소리와 떨림에서 고장 상태의 특징을 찾는 연구도 소개한다.[^fault] 제품 음질에서는 단순한 소리 크기를 넘어 날카로움·거칠기와 사람의 선호 사이의 관계를 분석해 평가 지표를 만드는 것이 목표다.[^quality]

## 주요 연구 주제

### 흡음 재료의 구조와 열 노화

재료의 음향 성능을 예측할 때는 재료 전체의 성질과 내부의 작은 구조를 함께 다룬다. 기공(재료 내부의 빈 공간)이 서로 열린 발포체(재료 안에 기체 공간을 만들어 형성한 구조)에서는 내부 막이 열 때문에 손상되면서 소리가 흡수되는 특성이 변한다. 연구실은 작은 구조의 계산 모형에서 공기 흐름과 열 전달을 계산해 재료 전체의 음향 성능을 예측한다.[^macro][^aging] 대표 논문 7은 열 노화(열에 노출되어 재료의 성질이 시간에 따라 변하는 현상)에 따른 흡음 저하를 내부 막의 손상과 연결했고, 대표 논문 3의 학회 초록은 방향에 따른 구조 차이를 학습 모형에 반영하는 접근을 제시한다.[^p7][^p3]

### 부품의 전달 경로와 실험·해석 모형 결합

차량이 완성되기 전에도 부품별 특성으로 전체 소음과 진동을 예측하는 것이 목표다. 동적 특성은 시간에 따라 변하는 자극에 대상이 반응하는 성질이다. 부분 구조 합성(부품별 동적 특성과 연결 조건을 이용해 조립체의 움직임을 계산하는 방법)은 연결 지점에서 힘이 균형을 이루고 각 부품의 변형이 서로 맞아야 한다는 조건을 쓴다. 연구실은 주파수(주기적으로 변하는 현상이 단위 시간에 반복되는 횟수)에 따른 응답 자료를 이용하는 방법을 주로 사용한다.[^substructure] 실험·해석 융합 연구에서는 실제로 측정한 특성과 계산으로 얻은 연결 지점의 정보를 결합하는 모형을 다룬다.[^hybrid] 대표 논문 1은 공작기계(재료를 절삭·성형해 부품을 만드는 기계)의 회전축과 공구 연결부를, 대표 논문 2는 운전자 입력에 맞춰 차량의 소리와 화면을 재현하는 가상 개발 환경을 다룬다.[^p1][^p2]

### 학습 모형을 이용한 소음 해석·제어와 고장 진단

차실의 소리 전달 특성이 달라지면 제어음의 효과도 달라질 수 있다. 연구실은 조건별로 측정한 자료로 신경망을 학습시켜 이 전달 특성을 예측하는 방법을 소개한다.[^active] 대표 논문 6의 학회 초록에서는 차실 조건에 맞춰 제어음의 전달 경로 추정치를 갱신하고, 대표 논문 4에서는 운전 중 얻은 자료로 소음 경로별 기여를 분석했다.[^p6][^p4] 고장 진단에서는 가속도(단위 시간에 대한 속도의 변화율)나 소리를 기록한 신호(정보를 나타내는 물리적 양이나 그 변화)에서 정상·고장 상태를 구별하는 특징을 찾는 학습 방법을 다룬다.[^fault]

### 전동 제동 장치, 제품 음질과 한국 종

전동 브레이크에서는 구동부의 진동이 장치의 여러 부품을 거쳐 운전자에게 전달되는 과정을 분석한다. 발생원·전달 경로·받는 지점을 나누어 원인을 찾고, 부품의 동적 특성을 바꿔 공진(외부 자극이 대상의 고유한 진동 방식에 에너지를 효율적으로 전달해 응답이 크게 나타나는 현상)을 피하는 방향을 연구한다.[^brake] 대표 논문 5는 회전 구동과 소음·진동의 관계를 분석했고, 대표 논문 8은 브레이크에서 생기는 낮은 주파수의 소음이 전달되는 경로를 다뤘다.[^p5][^p8] 제품 음질 연구는 실제 사용자의 소리 선호와 소리의 물리적 특성 사이의 관계를 평가 지표로 연결한다.[^quality] 한국 종에서는 소리의 세기가 주기적으로 달라지는 현상을 분석하고, 종을 치는 위치와 소리의 지속 특성을 연구한다.[^bell]

## 대표 논문

서울대 재직 시기의 2021–2026년 논문 가운데 부품 결합·가상 개발, 흡음 재료, 소음 해석·제어, 제동 장치의 갈래를 나누어 골랐다. 아래에는 학술지 논문, 학회 논문과 학회 초록을 구분했다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 주요 저자는 원문 순서의 첫 저자와 강연준 교수이며, 강 교수는 아래 항목 모두의 공동저자다.

| 번호 | 연도 | 논문·발표처 | 주요 저자 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2026 | [Identifying the Properties of Tapered Spindle-tool Joints using IRCSA and Optimization](https://doi.org/10.5050/ksnve.2026.36.2.127) · Transactions of the Korean Society for Noise and Vibration Engineering · 학술지 논문 | Kyeong-Rok Park; Yeon June Kang | 측정 지점의 응답을 연결부의 회전 운동까지 포함하는 자료로 바꾸어 공작기계의 회전축·공구 연결부 특성을 추정했다. 측정 불확실성을 줄이는 최적화를 함께 적용하고, 공구를 조이는 힘에 따른 연결부 특성의 변화를 분석했다.[^p1] |
| 2 | 2025 | [Model Based NVH Simulator for Virtual Development](https://doi.org/10.4271/2025-01-0059) · SAE technical papers on CD-ROM/SAE technical paper series · 학회 논문 | Sang‐Young Park; Yeon June Kang | 부품의 실험 모형과 차량 주행 모형을 연결해 운전자의 조작에 맞는 소리와 화면을 재현하는 시뮬레이터(대상 시스템의 동작을 모사하는 장치나 프로그램)를 구현했다. 부품과 도로·운전 조건을 바꾼 가상 차량의 주관 평가를 실제 시제품의 평가와 비교했다.[^p2] |
| 3 | 2025 | [Acoustic performance prediction of fibrous materials using anisotropic and fundamental parameter distributions](https://doi.org/10.1121/10.0037290) · The Journal of the Acoustical Society of America · 학회 초록 | Dongyung Kim; Yeon June Kang | 섬유 내부 구조가 방향마다 다른 점을 자료에 담아 음향 성능을 예측하는 학습 모형을 제시한 학회 초록이다. 균일한 재료로 가정하는 모형과 비교해 예측 성능과 계산 효율을 평가하고 설계 활용 가능성을 제시했다.[^p3] |
| 4 | 2023 | [Noise contribution analysis of road noise with transfer path analysis based on neural network in the box car system](https://doi.org/10.3397/in_2023_0165) · NOISE-CON proceedings · 학회 논문 | Uyeup Park; Yeon June Kang | 차량을 단순화한 실험 모형의 운전 자료를 신경망에 학습시켜 경로별 소음 기여를 구했다. 전통적인 전달 경로 분석과 비교해 결과를 검증했으며, 별도 충격 시험 등의 측정 부담을 줄이는 접근을 제시했다.[^p4] |
| 5 | 2023 | [Experimental study on improving the noise and vibration characteristics of electric brake systems using order analysis](https://doi.org/10.3397/in_2023_0328) · NOISE-CON proceedings · 학회 논문 | Jeongwoo Woo; Yeon June Kang | 전동 브레이크의 회전 구동과 각 부품의 진동·소음을 함께 분석했다. 회전으로 생기는 자극이 구조의 고유한 진동 특성과 맞물리는 문제를 파악하고, 부품 특성을 바꾸어 공진을 피하는 방향을 제시했다.[^p5] |
| 6 | 2023 | [Updating the secondary path using deep learning models to enhance the performance of active road noise control](https://doi.org/10.1121/10.0022989) · The Journal of the Acoustical Society of America · 학회 초록 | Jun Young Oh; Yeon June Kang | 차실의 조건이 변할 때 제어음이 전달되는 경로를 학습 모형으로 예측하고 실시간으로 갱신한 학회 초록이다. 보간(알려진 자료점 사이의 값을 추정하는 방법)과 비교해 예측 정확도와 자료 저장량을 평가했고, 실험에서 능동 노면 소음 제어 성능의 개선을 확인했다.[^p6] |
| 7 | 2022 | [Effect of thermal aging on the transport and acoustic properties of partially reticulated polyurethane foams](https://doi.org/10.1121/10.0014913) · The Journal of the Acoustical Society of America · 학술지 논문 | Sung Soo Yang; Yeon June Kang | 열에 노출된 흡음재에서 성능이 떨어지는 원인을 공기 흐름에 대한 저항과 내부 막의 손상으로 분석했다. 내부 구조를 모사한 계산으로 변화를 살펴 고온 환경에서의 재료 내구성을 평가하는 근거를 제시했다.[^p7] |
| 8 | 2022 | [A Study on the Reduction of Creep Groan Noise in Electric Commercial Vehicle using Transfer Path Analysis](https://doi.org/10.5050/ksnve.2022.32.4.346) · Transactions of the Korean Society for Noise and Vibration Engineering · 학술지 논문 | Uyeup Park; Yeon June Kang | 차량이 출발하거나 서서히 멈출 때 브레이크 마찰로 생기는 소음의 전달 경로를 분석했다. 흡진기(진동하는 보조 구조를 붙여 대상의 진동을 줄이는 장치)를 적용해 소음 수준과 발생률이 줄어드는 것을 보였다.[^p8] |

## 교수와 전문 분야

강연준 교수는 서울대학교에서 학사와 석사를, 1994년 Purdue University에서 기계공학 박사 학위를 받았다. 기계공학부 경력에는 1997년부터 서울대학교에서 교수·부교수·조교수로 재직한 것으로 적혀 있다.[^department] 교수 소개는 음향공학, 소음·진동공학을 전공으로 들고, 음향 재료·노면 소음·실험과 해석의 결합·음질을 연구 관심으로 제시한다.[^professor] 최근 논문에서는 재료의 구조와 흡음, 기계 연결부의 동특성, 운전 자료에 기반한 소음 분석, 제동 소음 제어가 전문 분야로 이어진다.[^p1][^p3][^p4][^p8]

## 응용 분야

자동차와 건물의 흡음·차음 설계, 차량의 노면 소음과 전동 브레이크 소음 개선, 기계 부품을 바꿨을 때의 진동 예측이 주요 응용이다.[^macro][^tpa][^brake][^hybrid] 실제 차량을 만들기 전 가상 환경에서 소리와 운전 조건을 평가하는 개발 방법도 다룬다.[^p2] 제품 소리의 선호도 평가와 한국 종의 소리 특성 분석도 연구 대상으로 제시한다.[^quality][^bell]

## 구성원

2026년 11월 6일 관측한 Current Member 목록과 개별 소개의 16명이다. 석박사통합과정 7명, 박사과정 3명, 석사과정 6명이며, 연구 주제와 학교 이메일은 랩 게시 표기를 따른다. ‘대표 논문 참여’는 위 표의 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 남정민 | 석박사통합과정 | Road Noise Control in NVH | skskskrnrn@snu.ac.kr |  |
| 오준영 | 석박사통합과정 | Road Noise Control in NVH | eric6518@snu.ac.kr |  |
| 우정우 | 박사과정 | Road Noise Control in NVH | wjw0252@snu.ac.kr |  |
| 김재윤 | 석박사통합과정 | Hybrid CAE/CAT | wodbs1027@snu.ac.kr |  |
| 김현균 | 박사과정 | Road Noise Control in NVH | guykim97@snu.ac.kr |  |
| 김주영 | 석박사통합과정 | Road Noise Control in NVH | juyoung@snu.ac.kr |  |
| 김도용 | 석박사통합과정 | Acoustical Material | younggarisnu@snu.ac.kr |  |
| 이정협 | 석박사통합과정 | Sound Quality | jhlee97@snu.ac.kr |  |
| 정원구 | 박사과정 | Acoustical Material | jwg0812@snu.ac.kr |  |
| 문희재 | 석사과정 |  | moonhj107@snu.ac.kr |  |
| 김호재 | 석박사통합과정 |  | kimhj9810@snu.ac.kr |  |
| 이규성 | 석사과정 |  | jayzzim@snu.ac.kr |  |
| 곽병민 | 석사과정 |  | dqudalsb@snu.ac.kr |  |
| 설민관 | 석사과정 |  | heyseol2963@snu.ac.kr |  |
| 이한별 | 석사과정 |  | phantom2b@snu.ac.kr |  |
| 장재준 | 석사과정 |  | wns6274@snu.ac.kr |  |

## 졸업생 진로

Alumni 목록과 개별 소개에 실린 71개 항목이다. 학위·졸업연도·진로는 랩의 게시 표기를 따르며, 같은 이름이 현재 구성원과 졸업생 목록에 함께 적힌 경우에도 각 목록의 표기를 따른다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 박경록 | M.S. (2026) | 한화에어로스페이스 |
| 안홍철 | M.S. (2026) | 한화에어로스페이스 |
| 홍은표 | M.S. (2026) | 현대기아자동차 |
| 정원구 | M.S. (2025) | 현대기아자동차 |
| 박우엽 | Ph.D. (2025) | 한화오션 |
| 정현우 | M.S. (2024) | 삼성전자 |
| 손제현 | M.S. (2024) | 현대기아자동차 |
| 이원섭 | M.S. (2024) | 현대기아자동차 |
| 양성수 | Ph.D. (2024) | 삼성전자 |
| 김현균 | M.S. (2024) | 서울대학교 기계공학부 음향진동연구실 박사과정 |
| 정인화 |  |  |
| 김철희 |  |  |
| 김진섭 |  |  |
| 이군희 |  |  |
| 구금표 |  |  |
| 김표재 |  |  |
| 이명준 |  |  |
| 신재성 |  |  |
| 이원혁 |  |  |
| 주형준 |  |  |
| 김영기 |  |  |
| 한제헌 |  |  |
| 배성윤 |  |  |
| 홍종호 |  |  |
| 김승한 |  |  |
| 김상훈 |  |  |
| 박소희 |  |  |
| 오상훈 |  |  |
| 박한길 |  |  |
| 김정훈 |  |  |
| 송문성 |  |  |
| 손인석 |  |  |
| Amir Hamza |  |  |
| 안성종 |  |  |
| 김규식 |  |  |
| 김정수 |  |  |
| 김찬중 |  |  |
| 이윤창 |  |  |
| 최우석 |  |  |
| 권가희 |  |  |
| 이민규 |  |  |
| 하헌주 |  |  |
| 송현진 |  |  |
| 김호용 |  |  |
| 박한솔 |  |  |
| 성원찬 |  |  |
| 김희수 |  |  |
| 임승택 |  |  |
| 신명호 |  |  |
| 강경민 |  |  |
| 김태식 |  |  |
| 손명섭 |  |  |
| 정원태 |  |  |
| 민동우 |  |  |
| 전주현 |  |  |
| 이형래 |  |  |
| 이경준 |  |  |
| 최재영 |  |  |
| 강성호 |  |  |
| 김동민 |  |  |
| 체말리 엘리아스 |  |  |
| 박재혁 |  |  |
| 김준구 |  |  |
| 박윤설 |  |  |
| 홍경준 |  |  |
| 표희수 |  |  |
| 조현호 |  |  |
| 주경훈 |  |  |
| 최익성 |  |  |
| 우정우 |  |  |
| 황의석 |  |  |

## 최근 5년 논문 목록

2021–2026년 학술지 목록의 26편이다. 연도·제목·저자·발표처는 연구실 표기를 따르고 DOI를 함께 적었다. 온라인 출판 연도와 학술지의 연도 구역이 다른 경우에도 아래 연도는 연구실의 구역 표기다.

**2026**

- Uyeup Park, Yeon June Kang. "Physics-guided neural network for force identification in component-based transfer path analysis". *Mechanical Systems and Signal Processing 250 (2026): 114112 · DOI: 10.1016/j.ymssp.2026.114112[^j312]*.
- Uyeup Park, Yeon June Kang. "Physics-guided neural network-based operational transfer path analysis". *Journal of Sound and Vibration (2026): 119491 · DOI: 10.1016/j.jsv.2025.119491[^j313]*.
- Jun Young Oh, Ju Young Kim, Chi Sung Oh, Ji Hyun Doe, Yeon June Kang. "Head-tracking active road noise control by real-time path adaptation using neural networks". *Mechanical Systems and Signal Processing 250 (2026): 114106 · DOI: 10.1016/j.ymssp.2026.114106[^j314]*.
- Won Gu Jung, Do Yong Kim, Jung Wook Lee, Yeon June Kang. "Deep learning-based approach for linking microstructural and macroscopic acoustic properties of sound-absorbing polyurethane foam". *The journal of the Acoustical Society of America 159 (5) : 3819-3834 · DOI: 10.1121/10.0043476[^j315]*.
- Jun Young Oh, Ju Young Kim, Chi Sung Oh, Kyoung Hoon Lee, Yeon June Kang. "End-to-end virtual sensing with head tracking using a temporal convolutional network for active noise control". *Mechanical Systems and Signal Processing 260 (2026): 114940 · DOI: 10.1016/j.ymssp.2026.114940[^j316]*.
- Jae Yun Kim, Kyeong Rok Park, Chang Ho Lee, Sung Hyun Jang, Yeon June Kang. "Expanded inverse receptance coupling substructure analysis for the robust prediction of tool-tip frequency response function in machine tools". *Journal of Manufacturing Processes 178 : 572-588 · DOI: 10.1016/j.jmapro.2026.10.005[^j317]*.

**2025**

- Sung Soo Yang, Inhwa Jung, Yeon June Kang. "Enhancing the acoustic durability of sound-absorbing polyurethane foam via graphene oxide impregnation". *Journal of Polymer Research 32, 7 (2025) · DOI: 10.1007/s10965-024-04223-w[^j304]*.
- Jeong Min Nam, Sang Yong Park, Jae Yun Kim, Yeon June Kang. "Optimal sensor placement method for system equivalent model mixing using correction forces". *Mechanical Systems and Signal Processing 237 (2025): 113150 · DOI: 10.1016/j.ymssp.2025.113150[^j305]*.
- Jun Young Oh, Munhwan Cho, Yeon June Kang. "Optimization of suspension bushing stiffness in early development stages using blocked force and energy index". *Mechanical Systems and Signal Processing 237 (2025): 113157 · DOI: 10.1016/j.ymssp.2025.113157[^j306]*.
- Uyeup Park, Kyoung-UK Nam, Yeon June Kang. "Prediction of road noise reduction using transfer path analysis with virtual spring". *Applied Acoustics 240 : 110879 · DOI: 10.1016/j.apacoust.2025.110879[^j307]*.
- Munhwan Cho, Jun Young Oh, David P. Song, Dennis de Klerk, Yeon June Kang. "Prediction of frequency response function changes of an automotive suspension assembly by injection-based dynamic substructuring". *Mechanical Systems and Signal Processing 228 (2025): 112479 · DOI: 10.1016/j.ymssp.2025.112479[^j308]*.
- Jung Hyub Lee, Jun Young Oh, Kyoung Hoon Lee, and Yeon June Kang. "Optimal driving sound conditions including concentration using the attention network test and the potential of recommending individual optimal driving sound". *The journal of the Acoustical Society of Korea · DOI: 10.7776/ask.2025.44.3.249[^j310]*.

**2024**

- Jun Young Oh, Hyun Woo Jung, Myung Han Lee, Kyoung Hoon Lee and Yeon June Kang. "Enhancing Active Noise Control of Road Noise using Deep Neural Network to Update Secondary Path Estimate in Real Time". *Mechanical Systems and Signal Processing, 206() : 110940 · DOI: 10.1016/j.ymssp.2023.110940[^j300]*.
- Sung Soo Yang, Won Gu Jung, and Yeon June Kang. "Microstructural design of rigid porous materials using a Bayesian optimization method". *Journal of Mechanical Science and Technology, 38(5) : 2265-2275 · DOI: 10.1007/s12206-024-0408-2[^j301]*.
- Uyeup Park, Yeon June Kang. "Operational transfer path analysis based on neural network". *Journal of Sound and Vibration, 539() : 118364 · DOI: 10.1016/j.jsv.2024.118364[^j302]*.
- Sung Soo Yang, Inhwa Jung, Yeon June Kang. "Multiscale acoustical study on graphene oxide impregnated polyurethane foam". *Macromolecular Research, 32, 935-946 (2024) · DOI: 10.1007/s13233-024-00281-7[^j303]*.

**2023**

- Jaehyuk Lee, Jaehyung Kim, Yujin Shin, Juhyun Jeon, Yeon June Kang, Inhwa Jung. "Multilayered graphene oxide impregnated polyurethane foam for ultimate sound absorbing performance: Algorithmic approach and experimental validation". *Applied Acoustics, 203() : 109194 · DOI: 10.1016/j.apacoust.2022.109194[^j295]*.
- Hansol Park, Yeon June Kang. "Analysis of three-dimensional dynamic behavior in rigid frame structures". *Journal of Sound and Vibration, 551() : 117601 · DOI: 10.1016/j.jsv.2023.117601[^j296]*.
- Hansol Park, Mookwon Kim, Kwangduk Baek and Yeon June Kang. "Experimental evaluation models of vehicle ride quality for two vibration types: primary ride and secondary ride". *Journal of Mechanical Science and Technology, 37(2) : 2301-2309 · DOI: 10.1007/s12206-023-0406-9[^j297]*.
- Sung Soo Yang, Jun Heo, Jung Wook Lee, Sung Hwan Park and Yeon June Kang. "Acoustic study on the thermal aging of sound-absorbing polyurethane foam". *Journal of Mechanical Science and Technology, 37(10) : 5047-5054 · DOI: 10.1007/s12206-023-0911-x[^j298]*.
- So Hee Park, Chan Jung Kim and Yeon June Kang. "Evaluation of the Supporting Mounts of a Three-in-One Electric Drive Unit Using a Hybrid Simulation Model". *Machines, 11(11) : 1026[^j299]*.
- Heon Ju Ha, Sung Soo Yang and Yeon June Kang. "A Study on the Sound Effect of Slits with or without an Acoustic Sealing". *Transactions of the Korean Society for Noise and Vibration Engineering, 33(3) : 240-248 · DOI: 10.5050/ksnve.2023.33.3.240[^j309]*.

**2022**

- Yun Seol Park, Yeon June Kang, Mun Hwan Cho, Chi Sung Oh. "Coherence-based sensor set expansion for optimal sensor placement in active road noise control". *Mechanical Systems and Signal Processing, 169() : 108788 · DOI: 10.1016/j.ymssp.2021.108788[^j291]*.
- Ho Yong Kim, Yeon June Kang. "Energy flow analysis of poroelastic media". *Journal of Sound and Vibration, 538() : 117236 · DOI: 10.1016/j.jsv.2022.117236[^j292]*.
- Uyeup Park, Ju Hyun Jeon, Sung Ho You, and Yeon June Kang. "A Study on the Reduction of Creep Groan Noise in Electric Commercial Vehicle using Transfer Path Analysis". *Transactions of the Korean Society for Noise and Vibration Engineering, 32(4) : 346-353 · DOI: 10.5050/ksnve.2022.32.4.346[^j293]*.
- Sung Soo Yang, Jung Wook Lee, Jong Hyun Kim, Yeon June Kang. "Effect of thermal aging on the transport and acoustic properties of partially reticulated polyurethane foams". *The Journal of the Acoustical Society of America, 152(4) : 2369 · DOI: 10.1121/10.0014913[^j294]*.

## 최근 5년 학회 발표 목록

Conferences의 원문 305건 가운데 발표 기간이 최근 5년에 드는 72건이다. 연·월은 누리집 표기이고 일자는 게시되어 있지 않다. 제목·대회명·기간과 장소·참가자는 랩 게시 표기를 따르며, 「참가자」를 완전한 저자 목록으로 간주하지 않는다.[^conference][^conferencearchive]

**2025**

- 신경망 기반 운전중 전달경로분석법을 통한 소음기여도 및 전달함수 추정. 2025년도 한국음향학회 춘계학술발표대회 · 2025/May. 참가자: 박우엽, 강연준.[^c1287]
- 운전 집중력 향상을 위한 주행음 선정 및 추천 모델 개발. 2025년도 한국음향학회 춘계학술발표대회 · 2025/May. 참가자: 이정협, 오준영, 이경훈, 강연준.[^c1288]
- Acoustic performance prediction based on microstructural distributions using a deep learning model. 25th International Congress on Acoustics and 188th Meeting of the Acoustical Society of America · 2025/May, New Orleans, USA. 참가자: Do Yong Kim, Yeon June Kang.[^c1290]
- 딥러닝을 활용한 강성 결합품 동특성 예측 연구. 2025년 춘계 소음진동 학술대회 · 2025/May. 참가자: 김현균, 강연준.[^c1291]
- 오토인코더 모델을 활용한 반도체 핸들러 실시간 고장진단. 2025년 춘계 소음진동 학술대회 · 2025/May. 참가자: 김주영, 이준호, 강연준.[^c1292]
- Spindle-Tool Joint Property 추정. 2025년 춘계 소음진동 학술대회 · 2025/May. 참가자: 박경록, 장성현, 이창호, 강연준.[^c1293]
- 고무 부시의 고주파수 동적 강성 데이터 베이스 개발. 2025년 춘계 소음진동 학술대회 · 2025/May. 참가자: 홍은표, 남정민, 박상영, 강연준.[^c1294]
- Real-time fault diagnosis of semiconductor handlers using multiple autoencoders. The 31st International Congress on Sound and Vibration · 2025/July, Incheon, South Korea. 참가자: JuYoung Kim, Wonsup Lee, Junho Lee, Yeon June Kang.[^c1295]
- Study on optimal driving sound conditions based on concentration using the attention network test(ANT). The 31st International Congress on Sound and Vibration · 2025/July, Incheon, South Korea. 참가자: Jung-Hyub Lee, Jun-Young Oh, Kyong-Hoon Lee, Yeon June Kang.[^c1296]
- 액추에이터 구동 소음 예측을 위한 하이브리드 해석 모델 구축. 2025년 춘계 소음진동 학술대회 · 2025/May. 참가자: 안홍철, 강연준.[^c1297]
- Optimizing of bushing stiffness for vehicle vibration reduction using dynamic substructuring approach. Inter - Noise 2025 · 2025/August, Sao Paulo, Brazil. 참가자: Hyunkyoon Kim, Jun Young Oh, Yeon June Kang.[^c1298]
- 공작기계 스핀들-공구 결합부 특성 예측. 2025 한국정밀공학회 추계학술대회 · 2025/Nov, 전남 여수. 참가자: 박경록, 강연준(서울대학교), 장성현, 이창호(DN솔루션즈).[^c1299]
- 공작기계 주파수 응답함수 추정을 위한 향상된 리셉턴스 결합 기법. 2025 한국정밀공학회 추계학술대회 · 2025/Nov, 전남 여수. 참가자: 김재윤, 강연준, 박경록(서울대학교), 이창호, 장성현(DN솔루션즈).[^c1300]
- 딥러닝 모델 기반 헤드트래킹 능동 노면 소음 제어. 2025년도 한국음향학회 추계 공동학술대회 · 2025/Nov, 전남 여수. 참가자: 오준영, 김주영(서울대학교), 오치성(현대자동차), 도지현(에이알이), 강연준(서울대학교).[^c1301]
- 양이 회전형 마이크 기반 3차원 음원 위치 추정. 2025년도 한국음향학회 추계 공동학술대회 · 2025/Nov, 전남 여수. 참가자: 김현균, 안세민, 문희재, 강연준, 안성훈(서울대학교).[^c1302]
- 미세구조 분포 기반 딥러닝을 활용한 섬유형 흡음재의 음향 성능 예측. 2025년도 한국음향학회 추계 공동학술대회 · 2025/Nov, 전남 여수. 참가자: 김도용(서울대학교), 이정욱, 이진형(현대자동차), 강연준(서울대학교).[^c1303]
- 전류 기반 내부 가진력 모델을 통한 전동기 NVH 특성 분석. 2025년도 추계 소음진동 학술대회 · 2025/Nov, 경북 경주. 참가자: 우정우, 박우엽(서울대학교), 김병준(현대모비스), 강연준(서울대학교).[^c1304]
- 고주파수 대역 고무 부시 점탄성 모델링을 통한 복소 동강성 식별. 2025년도 추계 소음진동 학술대회 · 2025/Nov, 경북 경주. 참가자: 홍은표, 남정민(서울대학교), 박상영(현대자동차), 강연준(서울대학교).[^c1305]

**2024**

- 신경망 기반의 구동중 전달경로분석을 이용한 소형 차량 모델의 소음 기여도 분석. 2024년도 춘계 소음진동 학술대회 · 2024/May. 참가자: 박우엽, 강연준.[^c1274]
- Interface reduction 기법을 이용한 해석 모델의 면결합 FBS 기법. 2024년도 춘계 소음진동 학술대회 · 2024/May. 참가자: 김재윤, 강연준.[^c1275]
- 딥러닝 기반 실시간 머리 위치에 따른 2차 경로 추정 업데이트를 통한 노면 능동소음제어 성능 향상. 2024년도 한국음향학회 춘계학술발표대회 · 2024/May. 참가자: 오준영, 이경훈, 장국진, 강연준.[^c1276]
- 심리음향 기반 만족도 및 운전 집중력을 고려한 최적 주행음 도출 프로세스 개발. 2024년도 한국음향학회 춘계학술발표대회 · 2024/May. 참가자: 오준영, 이정협, 이경훈, 장국진, 강연준.[^c1277]
- 티코노프 정칙화를 활용한 디커플링 기법의 정확도 개선 연구. 2024년도 한국음향학회 춘계학술발표대회 · 2024/May. 참가자: 남정민, 강연준, 박상영.[^c1278]
- 딥러닝 기반 다공성 재료의 음향 성능 예측 모델 개발. 2024년도 한국음향학회 춘계학술발표대회 · 2024/May. 참가자: 정원구, 이정욱, 박성환, 강연준.[^c1279]
- 오토인코더 모델을 활용한 반도체 핸들러 장비의 실시간 고장진단. 2024년도 추계 소음진동 학술대회 · 2024/Oct. 참가자: 김주영, 강연준, 이준호.[^c1280]
- FBS 기반 차량 지지부 강성 최적화 기법 연구. 2024년도 추계 소음진동 학술대회 · 2024/Oct. 참가자: 김현균, 강연준.[^c1281]
- Interface reduction 기법을 이용한 해석 모델의 면결합 FBS 기법. 2024년도 추계 소음진동 학술대회 · 2024/Oct. 참가자: 김재윤, 강연준, 장성현, 이창호.[^c1282]
- 신경망 회로 기반 q-축 전류를 이용한 전동식 브레이크 시스템의 진동 특성 예측. 2024년도 추계 소음진동 학술대회 · 2024/Oct. 참가자: 우정우, 강연준, 김병준.[^c1283]
- 수정력 기반 시스템 등가 모델 혼합법을 활용한 최적 센서 배치법. 2024년도 추계 소음진동 학술대회 · 2024/Oct. 참가자: 남정민, 강연준(서울대), 박상영(현대자동차).[^c1284]
- NVH 성능 향상을 위한 개발 초기단계에서의 서스펜션 부시 강성 최적화. 2024년도 한국음향학회 추계학술발표대회 · 2024/Oct. 참가자: 오준영, 강연준, 조문환.[^c1285]
- 딥러닝 기반 폴리우레탄 폼의 음향 특성 예측 연구. 2024년도 한국음향학회 추계학술발표대회 · 2024/Oct. 참가자: 정원구, 강연준, 이정욱, 박성환.[^c1286]

**2023**

- 해석모델의 모드 형상을 이용한 면 결합 FBS 기법. 2023년도 춘계 소음진동 학술대회 · 2023/May. 참가자: 김재윤, 강연준, 김명규.[^c1247]
- 부분 기여도 함수를 이용한 전동식 브레이크 시스템의 소음원 규명에 관한 연구. 2023년도 춘계 소음진동 학술대회 · 2023/May. 참가자: 우정우, 박우엽, 김병준, 강연준.[^c1248]
- RCSA 기법을 이용한 결합 시스템의 동특성 예측 연구. 2023년도 춘계 소음진동 학술대회 · 2023/May. 참가자: 손제현, 강연준.[^c1249]
- 가속 시험 모형을 이용한 흡차음 부품의 음향성능 열화 모델링. 2023년도 춘계 소음진동 학술대회 · 2023/May. 참가자: 허준, 양성수, 이정욱, 박성환, 강연준.[^c1250]
- 현가계 서브프레임에 대한 해석-시험 융합 연구. 2023년도 춘계 소음진동 학술대회 · 2023/May. 참가자: 남정민, 박상영, 최인정, 강연준.[^c1251]
- 머신 러닝을 이용한 차량 내 음향전달함수 예측 기법 연구. 2023년도 춘계 소음진동 학술대회 · 2023/May. 참가자: 정현우, 오준영, 이명한, 강연준.[^c1252]
- 단위부품의 설계변경에 따른 시스템 동특성 변화 예측. 2023년도 춘계 소음진동 학술대회 · 2023/May. 참가자: 박한솔, 강연준.[^c1253]
- 베이지안 최적화를 활용한 반도체 핸들러 고장진단. 2023년도 춘계 소음진동 학술대회 · 2023/May. 참가자: 이원섭, 박우엽, 이성호, 강연준.[^c1254]
- Index for Evaluating the NVH Performance of Rubber Bushings. The 29th International Congress on Sound and Vibration, · 2023/July, Prague, Czech. 참가자: Jun Young Oh, Mun Hwan Cho, David P Song, Yeon June Kang.[^c1255]
- A Study on Hybrid Transfer Function Prediction Model Based on SEMM. The 29th International Congress on Sound and Vibration · 2023/July, Prague, Czech. 참가자: Jae Yun Kim, Jeong Min Nam, Yeon June Kang.[^c1256]
- A Study on the Acoustic Durability of Sound Absorbing Porous Materials. The 29th International Congress on Sound and Vibration · 2023/July, Prague, Czech. 참가자: Sung Soo Yang, Jung Wook Lee, Sung Hwan Park, Yeon June Kang.[^c1257]
- Experimental study on improving the noise and vibration characteristics of electric brake systems using order analysis. Inter - Noise 2023 · 2023/Aug. 참가자: Jeongwoo Woo, Yeon June Kang, Byung Jun Kim.[^c1258]
- Model optimization in system equivalent model mixing using analytical modal analysis. Inter - Noise 2023 · 2023/Aug. 참가자: Jeongmin Nam, Yeonjune Kang, Sangyoung Park, Injeong Choi.[^c1259]
- Noise contribution analysis of road noise with transfer path analysis based on neural network in the box car system. Inter - Noise 2023 · 2023/Aug. 참가자: Uyeup Park, Yeon June Kang.[^c1260]
- 복소 신경망을 이용한 소형 차량 모델의 전달 경로 분석. 2023년도 추계 소음진동 학술대회 · 2023/Oct. 참가자: 박우엽, 강연준.[^c1261]
- 전동식 브레이크 시스템의 작동 진동 특성 파악 및 저감 연구. 2023년도 추계 소음진동 학술대회 · 2023/Oct. 참가자: 우정우, 김병준, 설용철, 강연준.[^c1262]
- 시스템 등가 모델 합성법에 대한 최적 센서 위치 선정법. 2023년도 추계 소음진동 학술대회 · 2023/Oct. 참가자: 남정민, 박상영, 강연준.[^c1263]
- 결합부 모델링을 이용한 면결합 조건 FBS 구현. 2023년도 추계 소음진동 학술대회 · 2023/Oct. 참가자: 김재윤, 송문근, 강연준.[^c1264]
- FEA 기반 RCSA 기법을 이용한 공작기계의 동특성 예측 연구. 2023년도 추계 소음진동 학술대회 · 2023/Oct. 참가자: 손제현, 이창호, 장성현, 강연준.[^c1265]
- 시스템 동특성 위상 정보를 이용한 진동 제어에 대한 연구. 2023년도 추계 소음진동 학술대회 · 2023/Oct. 참가자: 김현균, 강연준.[^c1266]
- 이중 오토인코더 모델을 활용한 반도체 핸들러 고장진단. 2023년도 추계 소음진동 학술대회 · 2023/Oct. 참가자: 이원섭, 김주영, 강연준.[^c1267]
- 딥러닝 기반 실시간 2차 경로 추정 업데이트 기법을 통한 로드노이즈 능동 제어 성능 향상. 2023년도 추계 소음진동 학술대회 · 2023/Oct. 참가자: 오준영, 정현우, 이명한, 이경훈, 강연준.[^c1268]
- 다공성 재료의 Morphology 변화에 기반한 흡차음 열화 모델링. 2023년도 추계 소음진동 학술대회 · 2023/Oct. 참가자: 허준, 양성수, 이정욱, 박성환, 강연준.[^c1269]
- 심리음향 파라미터를 이용한 최적 주행음 조건 도출. 2023년도 추계 소음진동 학술대회 · 2023/Oct. 참가자: 정현우, 오준영, 이명한, 이경훈, 강연준.[^c1270]
- 입상 재료의 흡음 특성 연구. 2023년도 추계 소음진동 학술대회 · 2023/Oct. 참가자: 양성수, 강연준.[^c1271]
- Updating the Secondary path estimate using deep learning models to enhance the performance of active road noise control. Acoustics · 2023/Dec, Sydney, Australia. 참가자: Jun Young Oh, Hyun Woo Jung, Myung Han Lee, Kyoung Hoon Lee and Yeon June Kang.[^c1272]
- Development of a Thermal Aging Model for Sound absorbing Polyurethane Foam. Acoustics · 2023/Dec, Sydney, Australia. 참가자: Sung Soo Yang, Jung Wook Lee, Sung Hwan Park, Yeon June Kang.[^c1273]

**2022**

- 다공성 흡음재 음향 성능 향상을 위한 단위 셀 설계 기법 연구. 2022년도 춘계 소음진동 학술대회 · 2022/May. 참가자: 양성수, 강연준.[^c1237]
- Complex Power를 이용한 결합시스템의 동특성 예측. 2022년도 춘계 소음진동 학술대회 · 2022/May. 참가자: 오준영, 강연준, 조문환, 송현진.[^c1238]
- 타이어 가진력 수치 계산 최적화 및 Unit Balancing Method. 2022년도 춘계 소음진동 학술대회 · 2022/May. 참가자: 남정민, 강연준, 박상영.[^c1239]
- 티호노프 정규화를 통한 로드노이즈 전달경로분석 정확도 향상 연구. 2022년도 춘계 소음진동 학술대회 · 2022/May. 참가자: 박우엽, 강연준, 남경욱.[^c1240]
- Measurement of Tire Transfer Function using FBS Decoupling Method. The 28th International Congress on Sound and Vibration · 2022/July, Singapore. 참가자: Jeongmin Nam, Sung Soo Yang, Jun Young Oh and Yeon June Kang.[^c1241]
- 소형 차량 모델 대상 입력점 강성 변경에 따른 실내 소음 예측 연구. 2022년도 추계 소음진동 학술대회 · 2022/Nov. 참가자: 박우엽, 남경욱, 강연준.[^c1242]
- 비선형 연결부의 NVH 성능 평가를 위한 인덱스 제시. 2022년도 추계 소음진동 학술대회 · 2022/Nov. 참가자: 오준영, 강연준, 조문환, 송현진.[^c1243]
- 방음용 실란트를 이용한 틈새 소음 저감에 대한 연구. 2022년도 추계 소음진동 학술대회 · 2022/Nov. 참가자: 하헌주, 강연준.[^c1244]
- 등가 모델 혼합을 이용한 시스템 전달함수 예측. 2022년도 추계 소음진동 학술대회 · 2022/Nov. 참가자: 김재윤, 강연준.[^c1245]
- 흡음구조 설계를 위한 민감도 분석 연구. 2022년도 추계 소음진동 학술대회 · 2022/Nov. 참가자: 양성수, 강연준.[^c1246]
- 자동차 브레이크 시스템의 동특성 파악 및 소음/진동원 분석에 관한 연구. 2022년도 추계 소음진동 학술대회 · 2022/Nov. 참가자: 우정우, 강연준, 전준철.[^c1289]

**2021**

- 연결부의 특성을 고려한 결합시스템 동특성 예측 정확도 개선. 2021년도 추계 소음진동 학술대회 · 2021/Nov. 참가자: 오준영, 강연준.[^c1234]
- 다공성 재료의 셀 멤브레인 함량 조정에 따른 흡음 성능 향상. 2021년도 추계 소음진동 학술대회 · 2021/Nov. 참가자: 양성수, 강연준.[^c1235]
- 추가 참조 센서를 이용한 디커플링 기법의 실험적 오차 개선. 2021년도 추계 소음진동 학술대회 · 2021/Nov. 참가자: 남정민, 강연준, 박상영.[^c1236]

## 특허

게시 출원일 또는 등록일이 2021-10-22–2026-10-22에 드는 6건이다. 발명자·번호·날짜는 랩의 표기를 따른다.[^patents]

- 구분 국내 · 강연준, 김현균, 문희재, 안성훈, 안세민, 2026, 회전형 음향 신호 센서를 포함하는 음원 위치 추정 장치 및 이를 이용하는 음원 위치 추정 방법, 출원번호 1020260027599, 출원일자 2026년 02월 11일
- 구분 국내 · 강연준, 김도용, 이정욱, 정원구, 2025, 우레탄 폼의 음향 성능 예측 방법 및 시스템, 출원번호 1020250111979, 출원일자 2025년 08월 13일
- 구분 USA · Jung Wook Lee, Sung Je Kim, Hyeong Rae Lee, Sung Soo Yang, and Yeon June Kang, 2023, Method for predicting physical properties of amorphous porous material, 등록번호 16/990,449, 등록일자 2023년 08월 17일
- 구분 국내 · 강연준, 조문환, 이강덕, 오치성, 유정근, 박윤설, 2022, 정보량 기반의 참조 센서 선정 및 이를 이용한 능동 소음 제어, 출원번호 1020220092697, 출원일자 2022년 07월 26일
- 구분 국내 · 강연준, 유정근, 오치성, 이강덕, 조문환, 박윤설, 2021, 후보 참조 센서 기반의 소음 제어를 위한 장치 및 방법, 출원번호 1020210181773, 출원일자 2021년 12월 17일
- 구분 국내 · 강연준, 조문환, 박윤설, 오치성, 김동민, 이강덕, 2021, 부분 상관 함수 기반의 소음 제어를 위한 장치 및 방법, 출원번호 1020210181798, 출원일자 2021년 12월 17일

## 수상과 선정

2021-10-22–2026-10-22에 게시된 수상·연구장려금 선정 17개 항목이다. 앞의 날짜는 글 게시일이고, 수상 이름에 든 연도는 원문 표기를 따른다. 같은 수상을 알린 글은 한 항목으로 묶었다.[^awards][^awards2][^awards3][^g124]

- 2026-08-25 · 오준영, 2026년도 한국음향학회 춘계학술발표대회 우수 발표상 선정[^g163]
- 2025-12-15 · 이정협, 2025년도 한국음향학회 에스티아이엔지니어링 학생논문상 선정[^b159]
- 2025-12-15 · 김현균, 2025년도 한국음향학회·한국음악지각인지학회 추계공동학술대회 우수발표상 선정[^b158][^g156]
- 2025-12-01 · 이정협, 2025년도 한국음향학회 추계 공동학술대회 우수 논문상 선정[^g156]
- 2025-11-14 · 김재윤, 2024 한국정밀공학회 추계학술대회 공작기계 부문 부문별 학술대회 최우수논문 수상자 선정[^b155]
- 2025-09-24 · 김현균, INTER-NOISE 2025 Young Professionals 수상[^b153]
- 2025-05-16 · 박우엽, 2025 한국음향학회 춘계학술발표대회 학술대회우수발표논문 선정[^a149][^g142]
- 2025-01-13 · 강연준, 2024년도 한국소음진동공학회 (주)NSV학술상 수상[^b138]
- 2025-01-13 · 정원구, 2024 한국음향학회 추계학술발표대회 학술대회우수발표논문 선정[^b137]
- 2024-07-11 · 우정우, 2024년도 하반기 (주)NSV연구장려금 수혜자 선정[^b103]
- 2024-07-11 · 오준영·우정우, 2024 한국음향학회 춘계학술발표대회 학술대회우수발표논문 선정[^b102]
- 2024-03-11 · 강연준, 서울대학교 공과대학 훌륭한 공대교수상(산학협력상) 수상[^a104]
- 2023-04-21 · 강연준, 과학기술진흥 유공 대통령 표창 수상[^a105][^g124]
- 2022-12-11 · 강연준, 2022년 12월 현대엔지비 전문기술교육 우수 강사상 수상[^b99]
- 2022-09-11 · 박우엽, 2022년도 하반기 (주)NSV연구장려금 수혜자 선정[^a101]
- 2022-09-11 · 박우엽, INTER-NOISE 2022 Young Professionals 수상[^b100]
- 2021-11-11 · 남정민, 2021년도 추계 소음진동 학술대회 일반세션 학생 우수발표자 선정[^b98]

## 연락과 위치

- 연구실: 서울특별시 관악구 관악로 1 서울대학교 제1공학관 301동 221호, 우편번호 08826. 전화 02-880-1692.[^contact]
- 교수실: 301동 1519호. 연락 페이지의 전화는 02-880-1692이며, 기계공학부 교수 상세의 교수 전화는 02-880-1691이다.[^contact][^department]
- 기계공학부 교수 상세의 연구 공간: 301동 221호(02-880-1692), 314동 102호(02-880-9203).[^department]
- 교수 이메일: yeonjune@snu.ac.kr.[^professor][^contact]
- 연구실 연락 이메일: juyoung@snu.ac.kr.[^contact]

## 각주
[^intro]: 연구실 Introduction. <https://acustica.snu.ac.kr/introduction/> 관측 2026-11-06.
[^professor]: 강연준 교수 소개. <https://acustica.snu.ac.kr/yeonjune/> 관측 2026-11-06.
[^macro]: 음향 재료의 거시적 성질 예측 연구. <https://acustica.snu.ac.kr/research2/> 관측 2026-11-06.
[^aging]: 음향 재료의 미세 구조와 노화 연구. <https://acustica.snu.ac.kr/microscopic-approach-for-the-aging-of-acoustical-materials/> 관측 2026-11-06.
[^soundai]: 흡음 재료에 대한 인공지능 연구. <https://acustica.snu.ac.kr/ai-application-in-sound-absorbing-material/> 관측 2026-11-06.
[^active]: 능동 노면 소음 제어와 인공지능 연구. <https://acustica.snu.ac.kr/ai-application-in-road-noise-active-noise-control/> 관측 2026-11-06.
[^fault]: 기계 고장 진단 연구. <https://acustica.snu.ac.kr/ai-application-in-fault-diagnosis/> 관측 2026-11-06.
[^tpa]: 전달 경로 분석 연구. <https://acustica.snu.ac.kr/transfer-path-analysis/> 관측 2026-11-06.
[^substructure]: 동적 부분 구조 합성 연구. <https://acustica.snu.ac.kr/dynamic-substructuring/> 관측 2026-11-06.
[^hybrid]: 실험·해석 모형 결합 연구. <https://acustica.snu.ac.kr/hybrid-cae-cat/> 관측 2026-11-06.
[^brake]: 전동 제동 장치의 소음·진동 연구. <https://acustica.snu.ac.kr/nvh-analysis-of-electric-brake-system/> 관측 2026-11-06.
[^quality]: 제품 음질 평가 연구. <https://acustica.snu.ac.kr/sound-quality/> 관측 2026-11-06.
[^bell]: 한국 종 연구. <https://acustica.snu.ac.kr/korean-bell/> 관측 2026-11-06.
[^conference]: Conferences 목록. <https://acustica.snu.ac.kr/%ec%bb%a8%ed%8d%bc%eb%9f%b0%ec%8a%a4/> 관측 2026-11-06.
[^conferencearchive]: 학회 발표 상세 사이트맵. <https://acustica.snu.ac.kr/conference-sitemap.xml> 관측 2026-11-06.
[^patents]: Patents 목록. <https://acustica.snu.ac.kr/patents/> 관측 2026-11-06.
[^awards]: Awards 목록 1쪽. <https://acustica.snu.ac.kr/awards/> 관측 2026-11-06.
[^awards2]: Awards 목록 2쪽. <https://acustica.snu.ac.kr/awards/?pageid=2&mod=list> 관측 2026-11-06.
[^awards3]: Awards 목록 3쪽. <https://acustica.snu.ac.kr/awards/?pageid=3&mod=list> 관측 2026-11-06.
[^contact]: 연락과 위치. <https://acustica.snu.ac.kr/%ec%b0%be%ec%95%84%ec%98%a4%ec%8b%9c%eb%8a%94%ea%b8%b8/> 관측 2026-11-06.
[^department]: 서울대학교 기계공학부 강연준 교수 상세. <https://me.snu.ac.kr/snu__professor/%ea%b0%95%ec%97%b0%ec%a4%80-kang-yeon-june/> 관측 2026-11-06.
[^members]: 연구실 Current Member 및 구성원 개별 소개. <https://acustica.snu.ac.kr/member/> <https://acustica.snu.ac.kr/member/%eb%82%a8%ec%a0%95%eb%af%bc/> <https://acustica.snu.ac.kr/member/%ec%98%a4%ec%a4%80%ec%98%81/> <https://acustica.snu.ac.kr/member/%ea%b9%80%e3%85%87%e3%85%87/> <https://acustica.snu.ac.kr/member/%ea%b9%80%ec%9e%ac%ec%9c%a4/> <https://acustica.snu.ac.kr/member/%ea%b9%80%ed%98%84%ea%b7%a0/> <https://acustica.snu.ac.kr/member/%ea%b9%80%ec%a3%bc%ec%98%81/> <https://acustica.snu.ac.kr/member/%ea%b9%80%eb%8f%84%ec%9a%a9/> <https://acustica.snu.ac.kr/member/%ec%9d%b4%ec%a0%95%ed%98%91/> <https://acustica.snu.ac.kr/member/%ec%a0%95%ec%9b%90%ea%b5%ac/> <https://acustica.snu.ac.kr/member/%eb%ac%b8%ed%9d%ac%ec%9e%ac/> <https://acustica.snu.ac.kr/member/%ea%b9%80%ed%98%b8%ec%9e%ac/> <https://acustica.snu.ac.kr/member/%ec%9d%b4%ea%b7%9c%ec%84%b1/> <https://acustica.snu.ac.kr/member/%ea%b3%bd%eb%b3%91%eb%af%bc/> <https://acustica.snu.ac.kr/member/%ec%84%a4%eb%af%bc%ea%b4%80/> <https://acustica.snu.ac.kr/member/%ec%9d%b4%ed%95%9c%eb%b3%84/> <https://acustica.snu.ac.kr/member/%ec%9e%a5%ec%9e%ac%ec%a4%80/> 관측 2026-11-06.
[^alumni]: 연구실 Alumni 및 졸업생 개별 소개. <https://acustica.snu.ac.kr/alumni/> <https://acustica.snu.ac.kr/alumni/%ec%a0%95%ec%9d%b8%ed%99%94/> <https://acustica.snu.ac.kr/alumni/%ea%b9%80%ec%b2%a0%ed%9d%ac/> <https://acustica.snu.ac.kr/alumni/%ea%b9%80%ec%a7%84%ec%84%ad/> <https://acustica.snu.ac.kr/alumni/%ec%9d%b4%ea%b5%b0%ed%9d%ac/> <https://acustica.snu.ac.kr/alumni/%ea%b5%ac%ea%b8%88%ed%91%9c/> <https://acustica.snu.ac.kr/alumni/%ea%b9%80%ed%91%9c%ec%9e%ac/> <https://acustica.snu.ac.kr/alumni/%ec%9d%b4%eb%aa%85%ec%a4%80/> <https://acustica.snu.ac.kr/alumni/%ec%8b%a0%ec%9e%ac%ec%84%b1/> <https://acustica.snu.ac.kr/alumni/%ec%9d%b4%ec%9b%90%ed%98%81/> <https://acustica.snu.ac.kr/alumni/%ec%a3%bc%ed%98%95%ec%a4%80/> <https://acustica.snu.ac.kr/alumni/%ea%b9%80%ec%98%81%ea%b8%b0/> <https://acustica.snu.ac.kr/alumni/%ed%95%9c%ec%a0%9c%ed%97%8c/> <https://acustica.snu.ac.kr/alumni/%eb%b0%b0%ec%84%b1%ec%9c%a4/> <https://acustica.snu.ac.kr/alumni/%ed%99%8d%ec%a2%85%ed%98%b8/> <https://acustica.snu.ac.kr/alumni/%ea%b9%80%ec%8a%b9%ed%95%9c/> <https://acustica.snu.ac.kr/alumni/%ea%b9%80%ec%83%81%ed%9b%88/> <https://acustica.snu.ac.kr/alumni/%eb%b0%95%ec%86%8c%ed%9d%ac/> <https://acustica.snu.ac.kr/alumni/%ec%98%a4%ec%83%81%ed%9b%88/> <https://acustica.snu.ac.kr/alumni/%eb%b0%95%ed%95%9c%ea%b8%b8/> <https://acustica.snu.ac.kr/alumni/%ea%b9%80%ec%a0%95%ed%9b%88/> <https://acustica.snu.ac.kr/alumni/%ec%86%a1%eb%ac%b8%ec%84%b1/> <https://acustica.snu.ac.kr/alumni/%ec%86%90%ec%9d%b8%ec%84%9d/> <https://acustica.snu.ac.kr/alumni/amir-hamza/> <https://acustica.snu.ac.kr/alumni/%ec%95%88%ec%84%b1%ec%a2%85/> <https://acustica.snu.ac.kr/alumni/%ea%b9%80%ea%b7%9c%ec%8b%9d/> <https://acustica.snu.ac.kr/alumni/%ea%b9%80%ec%a0%95%ec%88%98/> <https://acustica.snu.ac.kr/alumni/%ea%b9%80%ec%b0%ac%ec%a4%91/> <https://acustica.snu.ac.kr/alumni/%ec%9d%b4%ec%9c%a4%ec%b0%bd/> <https://acustica.snu.ac.kr/alumni/%ec%b5%9c%ec%9a%b0%ec%84%9d/> <https://acustica.snu.ac.kr/alumni/%ea%b6%8c%ea%b0%80%ed%9d%ac/> <https://acustica.snu.ac.kr/alumni/%ec%9d%b4%eb%af%bc%ea%b7%9c/> <https://acustica.snu.ac.kr/alumni/%ed%95%98%ed%97%8c%ec%a3%bc/> <https://acustica.snu.ac.kr/alumni/%ec%86%a1%ed%98%84%ec%a7%84/> <https://acustica.snu.ac.kr/alumni/%ea%b9%80%ed%98%b8%ec%9a%a9/> <https://acustica.snu.ac.kr/alumni/%eb%b0%95%ed%95%9c%ec%86%94/> <https://acustica.snu.ac.kr/alumni/%ec%84%b1%ec%9b%90%ec%b0%ac/> <https://acustica.snu.ac.kr/alumni/%ea%b9%80%ed%9d%ac%ec%88%98/> <https://acustica.snu.ac.kr/alumni/%ec%9e%84%ec%8a%b9%ed%83%9d/> <https://acustica.snu.ac.kr/alumni/%ec%8b%a0%eb%aa%85%ed%98%b8/> <https://acustica.snu.ac.kr/alumni/%ea%b0%95%ea%b2%bd%eb%af%bc/> <https://acustica.snu.ac.kr/alumni/%ea%b9%80%ed%83%9c%ec%8b%9d/> <https://acustica.snu.ac.kr/alumni/%ec%86%90%eb%aa%85%ec%84%ad/> <https://acustica.snu.ac.kr/alumni/%ec%a0%95%ec%9b%90%ed%83%9c/> <https://acustica.snu.ac.kr/alumni/%eb%af%bc%eb%8f%99%ec%9a%b0/> <https://acustica.snu.ac.kr/alumni/%ec%a0%84%ec%a3%bc%ed%98%84/> <https://acustica.snu.ac.kr/alumni/%ec%9d%b4%ed%98%95%eb%9e%98/> <https://acustica.snu.ac.kr/alumni/%ec%9d%b4%ea%b2%bd%ec%a4%80/> <https://acustica.snu.ac.kr/alumni/%ec%b5%9c%ec%9e%ac%ec%98%81/> <https://acustica.snu.ac.kr/alumni/%ec%a0%95%ed%98%84%ec%9a%b0/> <https://acustica.snu.ac.kr/alumni/%ec%86%90%ec%a0%9c%ed%98%84/> <https://acustica.snu.ac.kr/alumni/%ea%b0%95%ec%84%b1%ed%98%b8/> <https://acustica.snu.ac.kr/alumni/%ec%9d%b4%ec%9b%90%ec%84%ad/> <https://acustica.snu.ac.kr/alumni/%ea%b9%80%eb%8f%99%eb%af%bc/> <https://acustica.snu.ac.kr/alumni/%ec%b2%b4%eb%a7%90%eb%a6%ac-%ec%97%98%eb%a6%ac%ec%95%84%ec%8a%a4/> <https://acustica.snu.ac.kr/alumni/%eb%b0%95%ec%9e%ac%ed%98%81/> <https://acustica.snu.ac.kr/alumni/%ea%b9%80%ec%a4%80%ea%b5%ac/> <https://acustica.snu.ac.kr/alumni/%eb%b0%95%ec%9c%a4%ec%84%a4/> <https://acustica.snu.ac.kr/alumni/%ed%99%8d%ea%b2%bd%ec%a4%80/> <https://acustica.snu.ac.kr/alumni/%ed%91%9c%ed%9d%ac%ec%88%98/> <https://acustica.snu.ac.kr/alumni/%ec%a1%b0%ed%98%84%ed%98%b8/> <https://acustica.snu.ac.kr/alumni/%ec%a3%bc%ea%b2%bd%ed%9b%88/> <https://acustica.snu.ac.kr/alumni/%ec%96%91%ec%84%b1%ec%88%98/> <https://acustica.snu.ac.kr/alumni/%ec%b5%9c%ec%9d%b5%ec%84%b1/> <https://acustica.snu.ac.kr/alumni/%ec%a0%95%ec%9b%90%ea%b5%ac/> <https://acustica.snu.ac.kr/alumni/%ec%9a%b0%ec%a0%95%ec%9a%b0/> <https://acustica.snu.ac.kr/alumni/%ea%b9%80%ed%98%84%ea%b7%a0/> <https://acustica.snu.ac.kr/alumni/%ed%99%a9%ec%9d%98%ec%84%9d/> <https://acustica.snu.ac.kr/alumni/%eb%b0%95%ea%b2%bd%eb%a1%9d/> <https://acustica.snu.ac.kr/alumni/%ec%95%88%ed%99%8d%ec%b2%a0/> <https://acustica.snu.ac.kr/alumni/%ed%99%8d%ec%9d%80%ed%91%9c/> <https://acustica.snu.ac.kr/alumni/%eb%b0%95%ec%9a%b0/> 관측 2026-11-06.
[^j291]: 연구실 논문 상세, Coherence-based sensor set expansion for optimal sensor placement in active road noise control. <https://acustica.snu.ac.kr/publication/coherence-based-sensor-set-expansion-for-optimal-sensor-placement-in-active-road-noise-control/> 관측 2026-11-06.
[^j292]: 연구실 논문 상세, Energy flow analysis of poroelastic media. <https://acustica.snu.ac.kr/publication/energy-flow-analysis-of-poroelastic-media/> 관측 2026-11-06.
[^j293]: 연구실 논문 상세, A Study on the Reduction of Creep Groan Noise in Electric Commercial Vehicle using Transfer Path Analysis. <https://acustica.snu.ac.kr/publication/a-study-on-the-reduction-of-creep-groan-noise-in-electric-commercial-vehicle-using-transfer-path-analysis/> 관측 2026-11-06.
[^j294]: 연구실 논문 상세, Effect of thermal aging on the transport and acoustic properties of partially reticulated polyurethane foams. <https://acustica.snu.ac.kr/publication/effect-of-thermal-aging-on-the-transport-and-acoustic-properties-of-partially-reticulated-polyurethane-foams/> 관측 2026-11-06.
[^j295]: 연구실 논문 상세, Multilayered graphene oxide impregnated polyurethane foam for ultimate sound absorbing performance: Algorithmic approach and experimental validation. <https://acustica.snu.ac.kr/publication/multilayered-graphene-oxide-impregnated-polyurethane-foam-for-ultimate-sound-absorbing-performance-algorithmic-approach-and-experimental-validation/> 관측 2026-11-06.
[^j296]: 연구실 논문 상세, Analysis of three-dimensional dynamic behavior in rigid frame structures. <https://acustica.snu.ac.kr/publication/analysis-of-three-dimensional-dynamic-behavior-in-rigid-frame-structures/> 관측 2026-11-06.
[^j297]: 연구실 논문 상세, Experimental evaluation models of vehicle ride quality for two vibration types: primary ride and secondary ride. <https://acustica.snu.ac.kr/publication/experimental-evaluation-models-of-vehicle-ride-quality-for-two-vibration-types-primary-ride-and-secondary-ride/> 관측 2026-11-06.
[^j298]: 연구실 논문 상세, Acoustic study on the thermal aging of sound-absorbing polyurethane foam. <https://acustica.snu.ac.kr/publication/acoustic-study-on-the-thermal-aging-of-sound-absorbing-polyurethane-foam/> 관측 2026-11-06.
[^j299]: 연구실 논문 상세, Evaluation of the Supporting Mounts of a Three-in-One Electric Drive Unit Using a Hybrid Simulation Model. <https://acustica.snu.ac.kr/publication/evaluation-of-the-supporting-mounts-of-a-three-in-one-electric-drive-unit-using-a-hybrid-simulation-model/> 관측 2026-11-06.
[^j300]: 연구실 논문 상세, Enhancing Active Noise Control of Road Noise using Deep Neural Network to Update Secondary Path Estimate in Real Time. <https://acustica.snu.ac.kr/publication/enhancing-active-noise-control-of-road-noise-using-deep-neural-network-to-update-secondary-path-estimate-in-real-time/> 관측 2026-11-06.
[^j301]: 연구실 논문 상세, Microstructural design of rigid porous materials using a Bayesian optimization method. <https://acustica.snu.ac.kr/publication/microstructural-design-of-rigid-porous-materials-using-a-bayesian-optimization-method/> 관측 2026-11-06.
[^j302]: 연구실 논문 상세, Operational transfer path analysis based on neural network. <https://acustica.snu.ac.kr/publication/operational-transfer-path-analysis-based-on-neural-network/> 관측 2026-11-06.
[^j303]: 연구실 논문 상세, Multiscale acoustical study on graphene oxide impregnated polyurethane foam. <https://acustica.snu.ac.kr/publication/multiscale-acoustical-study-on-graphene-oxide-impregnated-polyurethane-foam/> 관측 2026-11-06.
[^j304]: 연구실 논문 상세, Enhancing the acoustic durability of sound-absorbing polyurethane foam via graphene oxide impregnation. <https://acustica.snu.ac.kr/publication/enhancing-the-acoustic-durability-of-sound-absorbing-polyurethane-foam-via-graphene-oxide-impregnation/> 관측 2026-11-06.
[^j305]: 연구실 논문 상세, Optimal sensor placement method for system equivalent model mixing using correction forces. <https://acustica.snu.ac.kr/publication/optimal-sensor-placement-method-for-system-equivalent-model-mixing-using-correction-forces/> 관측 2026-11-06.
[^j306]: 연구실 논문 상세, Optimization of suspension bushing stiffness in early development stages using blocked force and energy index. <https://acustica.snu.ac.kr/publication/optimization-of-suspension-bushing-stiffness-in-early-development-stages-using-blocked-force-and-energy-index/> 관측 2026-11-06.
[^j307]: 연구실 논문 상세, Prediction of road noise reduction using transfer path analysis with virtual spring. <https://acustica.snu.ac.kr/publication/prediction-of-road-noise-reduction-using-transfer-path-analysis-with-virtual-spring/> 관측 2026-11-06.
[^j308]: 연구실 논문 상세, Prediction of frequency response function changes of an automotive suspension assembly by injection-based dynamic substructuring. <https://acustica.snu.ac.kr/publication/prediction-of-frequency-response-function-changes-of-and-automotive-suspension-assembly-by-injection-based-dynamic-substructuring/> 관측 2026-11-06.
[^j309]: 연구실 논문 상세, A Study on the Sound Effect of Slits with or without an Acoustic Sealing. <https://acustica.snu.ac.kr/publication/a-study-on-the-sound-effect-of-slits-with-or-without-an-acoustic-sealing/> 관측 2026-11-06.
[^j310]: 연구실 논문 상세, Optimal driving sound conditions including concentration using the attention network test and the potential of recommending individual optimal driving sound. <https://acustica.snu.ac.kr/publication/optimal-driving-sound-conditions-including-concentration-using-the-attention-network-test-and-the-potential-of-recommending-individual-optimal-driving-sound/> 관측 2026-11-06. Jung Hyub Lee, Jun Young Oh, Kyoung Hoon Lee, Yeon June Kang, The Journal of the Acoustical Society of Korea 44(3), 249-259 (2025-05-31). <https://doi.org/10.7776/ask.2025.44.3.249> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://www.jask.or.kr/articles/article/mzVq/> 관측 2026-11-06.
[^j312]: 연구실 논문 상세, Physics-guided neural network for force identification in component-based transfer path analysis. <https://acustica.snu.ac.kr/publication/physics-guided-neural-network-for-force-identification-in-component-based-transfer-path-analysis/> 관측 2026-11-06.
[^j313]: 연구실 논문 상세, Physics-guided neural network-based operational transfer path analysis. <https://acustica.snu.ac.kr/publication/physics-guided-neural-network-based-operational-transfer-path-analysis/> 관측 2026-11-06.
[^j314]: 연구실 논문 상세, Head-tracking active road noise control by real-time path adaptation using neural networks. <https://acustica.snu.ac.kr/publication/head-tracking-active-road-noise-control-by-real-time-path-adaptation-using-neural-networks/> 관측 2026-11-06.
[^j315]: 연구실 논문 상세, Deep learning-based approach for linking microstructural and macroscopic acoustic properties of sound-absorbing polyurethane foam. <https://acustica.snu.ac.kr/publication/deep-learning-based-approach-for-linking-microstructural-and-macroscopic-acoustic-properties-of-sound-absorbing-polyurethane-foam/> 관측 2026-11-06.
[^j316]: 연구실 논문 상세, End-to-end virtual sensing with head tracking using a temporal convolutional network for active noise control. <https://acustica.snu.ac.kr/publication/end-to-end-virtual-sensing-with-head-tracking-using-a-temporal-convolutional-network-for-active-noise-control/> 관측 2026-11-06.
[^j317]: 연구실 논문 상세, Expanded inverse receptance coupling substructure analysis for the robust prediction of tool-tip frequency response function in machine tools. <https://acustica.snu.ac.kr/publication/expanded-inverse-receptance-coupling-substructure-analysis-for-the-robust-prediction-of-tool-tip-frequency-response-function-in-machine-tools/> 관측 2026-11-06.
[^c1234]: 연구실 학회 발표 상세, 연결부의 특성을 고려한 결합시스템 동특성 예측 정확도 개선. <https://acustica.snu.ac.kr/conference/%ec%97%b0%ea%b2%b0%eb%b6%80%ec%9d%98-%ed%8a%b9%ec%84%b1%ec%9d%84-%ea%b3%a0%eb%a0%a4%ed%95%9c-%ea%b2%b0%ed%95%a9%ec%8b%9c%ec%8a%a4%ed%85%9c-%eb%8f%99%ed%8a%b9%ec%84%b1-%ec%98%88%ec%b8%a1-%ec%a0%95/> 관측 2026-11-06.
[^c1235]: 연구실 학회 발표 상세, 다공성 재료의 셀 멤브레인 함량 조정에 따른 흡음 성능 향상. <https://acustica.snu.ac.kr/conference/%eb%8b%a4%ea%b3%b5%ec%84%b1-%ec%9e%ac%eb%a3%8c%ec%9d%98-%ec%85%80-%eb%a9%a4%eb%b8%8c%eb%a0%88%ec%9d%b8-%ed%95%a8%eb%9f%89-%ec%a1%b0%ec%a0%95%ec%97%90-%eb%94%b0%eb%a5%b8-%ed%9d%a1%ec%9d%8c-%ec%84%b1/> 관측 2026-11-06.
[^c1236]: 연구실 학회 발표 상세, 추가 참조 센서를 이용한 디커플링 기법의 실험적 오차 개선. <https://acustica.snu.ac.kr/conference/%ec%b6%94%ea%b0%80-%ec%b0%b8%ec%a1%b0-%ec%84%bc%ec%84%9c%eb%a5%bc-%ec%9d%b4%ec%9a%a9%ed%95%9c-%eb%94%94%ec%bb%a4%ed%94%8c%eb%a7%81-%ea%b8%b0%eb%b2%95%ec%9d%98-%ec%8b%a4%ed%97%98%ec%a0%81-%ec%98%a4/> 관측 2026-11-06.
[^c1237]: 연구실 학회 발표 상세, 다공성 흡음재 음향 성능 향상을 위한 단위 셀 설계 기법 연구. <https://acustica.snu.ac.kr/conference/%eb%8b%a4%ea%b3%b5%ec%84%b1-%ed%9d%a1%ec%9d%8c%ec%9e%ac-%ec%9d%8c%ed%96%a5-%ec%84%b1%eb%8a%a5-%ed%96%a5%ec%83%81%ec%9d%84-%ec%9c%84%ed%95%9c-%eb%8b%a8%ec%9c%84-%ec%85%80-%ec%84%a4%ea%b3%84-%ea%b8%b0/> 관측 2026-11-06.
[^c1238]: 연구실 학회 발표 상세, Complex Power를 이용한 결합시스템의 동특성 예측. <https://acustica.snu.ac.kr/conference/complex-power%eb%a5%bc-%ec%9d%b4%ec%9a%a9%ed%95%9c-%ea%b2%b0%ed%95%a9%ec%8b%9c%ec%8a%a4%ed%85%9c%ec%9d%98-%eb%8f%99%ed%8a%b9%ec%84%b1-%ec%98%88%ec%b8%a1/> 관측 2026-11-06.
[^c1239]: 연구실 학회 발표 상세, 타이어 가진력 수치 계산 최적화 및 Unit Balancing Method. <https://acustica.snu.ac.kr/conference/%ed%83%80%ec%9d%b4%ec%96%b4-%ea%b0%80%ec%a7%84%eb%a0%a5-%ec%88%98%ec%b9%98-%ea%b3%84%ec%82%b0-%ec%b5%9c%ec%a0%81%ed%99%94-%eb%b0%8f-unit-balancing-method/> 관측 2026-11-06.
[^c1240]: 연구실 학회 발표 상세, 티호노프 정규화를 통한 로드노이즈 전달경로분석 정확도 향상 연구. <https://acustica.snu.ac.kr/conference/%ed%8b%b0%ed%98%b8%eb%85%b8%ed%94%84-%ec%a0%95%ea%b7%9c%ed%99%94%eb%a5%bc-%ed%86%b5%ed%95%9c-%eb%a1%9c%eb%93%9c%eb%85%b8%ec%9d%b4%ec%a6%88-%ec%a0%84%eb%8b%ac%ea%b2%bd%eb%a1%9c%eb%b6%84%ec%84%9d/> 관측 2026-11-06.
[^c1241]: 연구실 학회 발표 상세, Measurement of Tire Transfer Function using FBS Decoupling Method. <https://acustica.snu.ac.kr/conference/measurement-of-tire-transfer-function-using-fbs-decoupling-method/> 관측 2026-11-06.
[^c1242]: 연구실 학회 발표 상세, 소형 차량 모델 대상 입력점 강성 변경에 따른 실내 소음 예측 연구. <https://acustica.snu.ac.kr/conference/%ec%86%8c%ed%98%95-%ec%b0%a8%eb%9f%89-%eb%aa%a8%eb%8d%b8-%eb%8c%80%ec%83%81-%ec%9e%85%eb%a0%a5%ec%a0%90-%ea%b0%95%ec%84%b1-%eb%b3%80%ea%b2%bd%ec%97%90-%eb%94%b0%eb%a5%b8-%ec%8b%a4%eb%82%b4-%ec%86%8c/> 관측 2026-11-06.
[^c1243]: 연구실 학회 발표 상세, 비선형 연결부의 NVH 성능 평가를 위한 인덱스 제시. <https://acustica.snu.ac.kr/conference/%eb%b9%84%ec%84%a0%ed%98%95-%ec%97%b0%ea%b2%b0%eb%b6%80%ec%9d%98-nvh-%ec%84%b1%eb%8a%a5-%ed%8f%89%ea%b0%80%eb%a5%bc-%ec%9c%84%ed%95%9c-%ec%9d%b8%eb%8d%b1%ec%8a%a4-%ec%a0%9c%ec%8b%9c/> 관측 2026-11-06.
[^c1244]: 연구실 학회 발표 상세, 방음용 실란트를 이용한 틈새 소음 저감에 대한 연구. <https://acustica.snu.ac.kr/conference/%eb%b0%a9%ec%9d%8c%ec%9a%a9-%ec%8b%a4%eb%9e%80%ed%8a%b8%eb%a5%bc-%ec%9d%b4%ec%9a%a9%ed%95%9c-%ed%8b%88%ec%83%88-%ec%86%8c%ec%9d%8c-%ec%a0%80%ea%b0%90%ec%97%90-%eb%8c%80%ed%95%9c-%ec%97%b0%ea%b5%ac/> 관측 2026-11-06.
[^c1245]: 연구실 학회 발표 상세, 등가 모델 혼합을 이용한 시스템 전달함수 예측. <https://acustica.snu.ac.kr/conference/%eb%93%b1%ea%b0%80-%eb%aa%a8%eb%8d%b8-%ed%98%bc%ed%95%a9%ec%9d%84-%ec%9d%b4%ec%9a%a9%ed%95%9c-%ec%8b%9c%ec%8a%a4%ed%85%9c-%ec%a0%84%eb%8b%ac%ed%95%a8%ec%88%98-%ec%98%88%ec%b8%a1/> 관측 2026-11-06.
[^c1246]: 연구실 학회 발표 상세, 흡음구조 설계를 위한 민감도 분석 연구. <https://acustica.snu.ac.kr/conference/%ed%9d%a1%ec%9d%8c%ea%b5%ac%ec%a1%b0-%ec%84%a4%ea%b3%84%eb%a5%bc-%ec%9c%84%ed%95%9c-%eb%af%bc%ea%b0%90%eb%8f%84-%eb%b6%84%ec%84%9d-%ec%97%b0%ea%b5%ac/> 관측 2026-11-06.
[^c1247]: 연구실 학회 발표 상세, 해석모델의 모드 형상을 이용한 면 결합 FBS 기법. <https://acustica.snu.ac.kr/conference/%ed%95%b4%ec%84%9d%eb%aa%a8%eb%8d%b8%ec%9d%98-%eb%aa%a8%eb%93%9c-%ed%98%95%ec%83%81%ec%9d%84-%ec%9d%b4%ec%9a%a9%ed%95%9c-%eb%a9%b4-%ea%b2%b0%ed%95%a9-fbs-%ea%b8%b0%eb%b2%95/> 관측 2026-11-06.
[^c1248]: 연구실 학회 발표 상세, 부분 기여도 함수를 이용한 전동식 브레이크 시스템의 소음원 규명에 관한 연구. <https://acustica.snu.ac.kr/conference/%eb%b6%80%eb%b6%84-%ea%b8%b0%ec%97%ac%eb%8f%84-%ed%95%a8%ec%88%98%eb%a5%bc-%ec%9d%b4%ec%9a%a9%ed%95%9c-%ec%a0%84%eb%8f%99%ec%8b%9d-%eb%b8%8c%eb%a0%88%ec%9d%b4%ed%81%ac-%ec%8b%9c%ec%8a%a4%ed%85%9c/> 관측 2026-11-06.
[^c1249]: 연구실 학회 발표 상세, RCSA 기법을 이용한 결합 시스템의 동특성 예측 연구. <https://acustica.snu.ac.kr/conference/rcsa-%ea%b8%b0%eb%b2%95%ec%9d%84-%ec%9d%b4%ec%9a%a9%ed%95%9c-%ea%b2%b0%ed%95%a9-%ec%8b%9c%ec%8a%a4%ed%85%9c%ec%9d%98-%eb%8f%99%ed%8a%b9%ec%84%b1-%ec%98%88%ec%b8%a1-%ec%97%b0%ea%b5%ac/> 관측 2026-11-06.
[^c1250]: 연구실 학회 발표 상세, 가속 시험 모형을 이용한 흡차음 부품의 음향성능 열화 모델링. <https://acustica.snu.ac.kr/conference/%ea%b0%80%ec%86%8d-%ec%8b%9c%ed%97%98-%eb%aa%a8%ed%98%95%ec%9d%84-%ec%9d%b4%ec%9a%a9%ed%95%9c-%ed%9d%a1%ec%b0%a8%ec%9d%8c-%eb%b6%80%ed%92%88%ec%9d%98-%ec%9d%8c%ed%96%a5%ec%84%b1%eb%8a%a5-%ec%97%b4/> 관측 2026-11-06.
[^c1251]: 연구실 학회 발표 상세, 현가계 서브프레임에 대한 해석-시험 융합 연구. <https://acustica.snu.ac.kr/conference/%ed%98%84%ea%b0%80%ea%b3%84-%ec%84%9c%eb%b8%8c%ed%94%84%eb%a0%88%ec%9e%84%ec%97%90-%eb%8c%80%ed%95%9c-%ed%95%b4%ec%84%9d-%ec%8b%9c%ed%97%98-%ec%9c%b5%ed%95%a9-%ec%97%b0%ea%b5%ac/> 관측 2026-11-06.
[^c1252]: 연구실 학회 발표 상세, 머신 러닝을 이용한 차량 내 음향전달함수 예측 기법 연구. <https://acustica.snu.ac.kr/conference/%eb%a8%b8%ec%8b%a0-%eb%9f%ac%eb%8b%9d%ec%9d%84-%ec%9d%b4%ec%9a%a9%ed%95%9c-%ec%b0%a8%eb%9f%89-%eb%82%b4-%ec%9d%8c%ed%96%a5%ec%a0%84%eb%8b%ac%ed%95%a8%ec%88%98-%ec%98%88%ec%b8%a1-%ea%b8%b0%eb%b2%95/> 관측 2026-11-06.
[^c1253]: 연구실 학회 발표 상세, 단위부품의 설계변경에 따른 시스템 동특성 변화 예측. <https://acustica.snu.ac.kr/conference/%eb%8b%a8%ec%9c%84%eb%b6%80%ed%92%88%ec%9d%98-%ec%84%a4%ea%b3%84%eb%b3%80%ea%b2%bd%ec%97%90-%eb%94%b0%eb%a5%b8-%ec%8b%9c%ec%8a%a4%ed%85%9c-%eb%8f%99%ed%8a%b9%ec%84%b1-%eb%b3%80%ed%99%94-%ec%98%88/> 관측 2026-11-06.
[^c1254]: 연구실 학회 발표 상세, 베이지안 최적화를 활용한 반도체 핸들러 고장진단. <https://acustica.snu.ac.kr/conference/%eb%b2%a0%ec%9d%b4%ec%a7%80%ec%95%88-%ec%b5%9c%ec%a0%81%ed%99%94%eb%a5%bc-%ed%99%9c%ec%9a%a9%ed%95%9c-%eb%b0%98%eb%8f%84%ec%b2%b4-%ed%95%b8%eb%93%a4%eb%9f%ac-%ea%b3%a0%ec%9e%a5%ec%a7%84%eb%8b%a8/> 관측 2026-11-06.
[^c1255]: 연구실 학회 발표 상세, Index for Evaluating the NVH Performance of Rubber Bushings. <https://acustica.snu.ac.kr/conference/index-for-evaluating-the-nvh-performance-of-rubber-bushings/> 관측 2026-11-06.
[^c1256]: 연구실 학회 발표 상세, A Study on Hybrid Transfer Function Prediction Model Based on SEMM. <https://acustica.snu.ac.kr/conference/a-study-on-hybrid-transfer-function-prediction-model-based-on-semm/> 관측 2026-11-06.
[^c1257]: 연구실 학회 발표 상세, A Study on the Acoustic Durability of Sound Absorbing Porous Materials. <https://acustica.snu.ac.kr/conference/a-study-on-the-acoustic-durability-of-sound-absorbing-porous-materials/> 관측 2026-11-06.
[^c1258]: 연구실 학회 발표 상세, Experimental study on improving the noise and vibration characteristics of electric brake systems using order analysis. <https://acustica.snu.ac.kr/conference/experimental-study-on-improving-the-noise-and-vibration-characteristics-of-electric-brake-systems-using-order-analysis/> 관측 2026-11-06.
[^c1259]: 연구실 학회 발표 상세, Model optimization in system equivalent model mixing using analytical modal analysis. <https://acustica.snu.ac.kr/conference/model-optimization-in-system-equivalent-model-mixing-using-analytical-modal-analysis/> 관측 2026-11-06.
[^c1260]: 연구실 학회 발표 상세, Noise contribution analysis of road noise with transfer path analysis based on neural network in the box car system. <https://acustica.snu.ac.kr/conference/noise-contribution-analysis-of-road-noise-with-transfer-path-analysis-based-on-neural-network-in-the-box-car-system/> 관측 2026-11-06.
[^c1261]: 연구실 학회 발표 상세, 복소 신경망을 이용한 소형 차량 모델의 전달 경로 분석. <https://acustica.snu.ac.kr/conference/%eb%b3%b5%ec%86%8c-%ec%8b%a0%ea%b2%bd%eb%a7%9d%ec%9d%84-%ec%9d%b4%ec%9a%a9%ed%95%9c-%ec%86%8c%ed%98%95-%ec%b0%a8%eb%9f%89-%eb%aa%a8%eb%8d%b8%ec%9d%98-%ec%a0%84%eb%8b%ac-%ea%b2%bd%eb%a1%9c-%eb%b6%84/> 관측 2026-11-06.
[^c1262]: 연구실 학회 발표 상세, 전동식 브레이크 시스템의 작동 진동 특성 파악 및 저감 연구. <https://acustica.snu.ac.kr/conference/%ec%a0%84%eb%8f%99%ec%8b%9d-%eb%b8%8c%eb%a0%88%ec%9d%b4%ed%81%ac-%ec%8b%9c%ec%8a%a4%ed%85%9c%ec%9d%98-%ec%9e%91%eb%8f%99-%ec%a7%84%eb%8f%99-%ed%8a%b9%ec%84%b1-%ed%8c%8c%ec%95%85-%eb%b0%8f-%ec%a0%80/> 관측 2026-11-06.
[^c1263]: 연구실 학회 발표 상세, 시스템 등가 모델 합성법에 대한 최적 센서 위치 선정법. <https://acustica.snu.ac.kr/conference/%ec%8b%9c%ec%8a%a4%ed%85%9c-%eb%93%b1%ea%b0%80-%eb%aa%a8%eb%8d%b8-%ed%95%a9%ec%84%b1%eb%b2%95%ec%97%90-%eb%8c%80%ed%95%9c-%ec%b5%9c%ec%a0%81-%ec%84%bc%ec%84%9c-%ec%9c%84%ec%b9%98-%ec%84%a0%ec%a0%95/> 관측 2026-11-06.
[^c1264]: 연구실 학회 발표 상세, 결합부 모델링을 이용한 면결합 조건 FBS 구현. <https://acustica.snu.ac.kr/conference/%ea%b2%b0%ed%95%a9%eb%b6%80-%eb%aa%a8%eb%8d%b8%eb%a7%81%ec%9d%84-%ec%9d%b4%ec%9a%a9%ed%95%9c-%eb%a9%b4%ea%b2%b0%ed%95%a9-%ec%a1%b0%ea%b1%b4-fbs-%ea%b5%ac%ed%98%84/> 관측 2026-11-06.
[^c1265]: 연구실 학회 발표 상세, FEA 기반 RCSA 기법을 이용한 공작기계의 동특성 예측 연구. <https://acustica.snu.ac.kr/conference/fea-%ea%b8%b0%eb%b0%98-rcsa-%ea%b8%b0%eb%b2%95%ec%9d%84-%ec%9d%b4%ec%9a%a9%ed%95%9c-%ea%b3%b5%ec%9e%91%ea%b8%b0%ea%b3%84%ec%9d%98-%eb%8f%99%ed%8a%b9%ec%84%b1-%ec%98%88%ec%b8%a1-%ec%97%b0%ea%b5%ac/> 관측 2026-11-06.
[^c1266]: 연구실 학회 발표 상세, 시스템 동특성 위상 정보를 이용한 진동 제어에 대한 연구. <https://acustica.snu.ac.kr/conference/%ec%8b%9c%ec%8a%a4%ed%85%9c-%eb%8f%99%ed%8a%b9%ec%84%b1-%ec%9c%84%ec%83%81-%ec%a0%95%eb%b3%b4%eb%a5%bc-%ec%9d%b4%ec%9a%a9%ed%95%9c-%ec%a7%84%eb%8f%99-%ec%a0%9c%ec%96%b4%ec%97%90-%eb%8c%80%ed%95%9c/> 관측 2026-11-06.
[^c1267]: 연구실 학회 발표 상세, 이중 오토인코더 모델을 활용한 반도체 핸들러 고장진단. <https://acustica.snu.ac.kr/conference/%ec%9d%b4%ec%a4%91-%ec%98%a4%ed%86%a0%ec%9d%b8%ec%bd%94%eb%8d%94-%eb%aa%a8%eb%8d%b8%ec%9d%84-%ed%99%9c%ec%9a%a9%ed%95%9c-%eb%b0%98%eb%8f%84%ec%b2%b4-%ed%95%b8%eb%93%a4%eb%9f%ac-%ea%b3%a0%ec%9e%a5/> 관측 2026-11-06.
[^c1268]: 연구실 학회 발표 상세, 딥러닝 기반 실시간 2차 경로 추정 업데이트 기법을 통한 로드노이즈 능동 제어 성능 향상. <https://acustica.snu.ac.kr/conference/%eb%94%a5%eb%9f%ac%eb%8b%9d-%ea%b8%b0%eb%b0%98-%ec%8b%a4%ec%8b%9c%ea%b0%84-2%ec%b0%a8-%ea%b2%bd%eb%a1%9c-%ec%b6%94%ec%a0%95-%ec%97%85%eb%8d%b0%ec%9d%b4%ed%8a%b8-%ea%b8%b0%eb%b2%95%ec%9d%84-%ed%86%b5/> 관측 2026-11-06.
[^c1269]: 연구실 학회 발표 상세, 다공성 재료의 Morphology 변화에 기반한 흡차음 열화 모델링. <https://acustica.snu.ac.kr/conference/%eb%8b%a4%ea%b3%b5%ec%84%b1-%ec%9e%ac%eb%a3%8c%ec%9d%98-morphology-%eb%b3%80%ed%99%94%ec%97%90-%ea%b8%b0%eb%b0%98%ed%95%9c-%ed%9d%a1%ec%b0%a8%ec%9d%8c-%ec%97%b4%ed%99%94-%eb%aa%a8%eb%8d%b8%eb%a7%81/> 관측 2026-11-06.
[^c1270]: 연구실 학회 발표 상세, 심리음향 파라미터를 이용한 최적 주행음 조건 도출. <https://acustica.snu.ac.kr/conference/%ec%8b%ac%eb%a6%ac%ec%9d%8c%ed%96%a5-%ed%8c%8c%eb%9d%bc%eb%af%b8%ed%84%b0%eb%a5%bc-%ec%9d%b4%ec%9a%a9%ed%95%9c-%ec%b5%9c%ec%a0%81-%ec%a3%bc%ed%96%89%ec%9d%8c-%ec%a1%b0%ea%b1%b4-%eb%8f%84%ec%b6%9c/> 관측 2026-11-06.
[^c1271]: 연구실 학회 발표 상세, 입상 재료의 흡음 특성 연구. <https://acustica.snu.ac.kr/conference/%ec%9e%85%ec%83%81-%ec%9e%ac%eb%a3%8c%ec%9d%98-%ed%9d%a1%ec%9d%8c-%ed%8a%b9%ec%84%b1-%ec%97%b0%ea%b5%ac/> 관측 2026-11-06.
[^c1272]: 연구실 학회 발표 상세, Updating the Secondary path estimate using deep learning models to enhance the performance of active road noise control. <https://acustica.snu.ac.kr/conference/updating-the-secondary-path-estimate-using-deep-learning-models-to-enhance-the-performance-of-active-road-noise-control/> 관측 2026-11-06.
[^c1273]: 연구실 학회 발표 상세, Development of a Thermal Aging Model for Sound absorbing Polyurethane Foam. <https://acustica.snu.ac.kr/conference/development-of-a-thermal-aging-model-for-sound-absorbing-polyurethane-foam/> 관측 2026-11-06.
[^c1274]: 연구실 학회 발표 상세, 신경망 기반의 구동중 전달경로분석을 이용한 소형 차량 모델의 소음 기여도 분석. <https://acustica.snu.ac.kr/conference/%ec%8b%a0%ea%b2%bd%eb%a7%9d-%ea%b8%b0%eb%b0%98%ec%9d%98-%ea%b5%ac%eb%8f%99%ec%a4%91-%ec%a0%84%eb%8b%ac%ea%b2%bd%eb%a1%9c%eb%b6%84%ec%84%9d%ec%9d%84-%ec%9d%b4%ec%9a%a9%ed%95%9c-%ec%86%8c%ed%98%95/> 관측 2026-11-06.
[^c1275]: 연구실 학회 발표 상세, Interface reduction 기법을 이용한 해석 모델의 면결합 FBS 기법. <https://acustica.snu.ac.kr/conference/interface-reduction-%ea%b8%b0%eb%b2%95%ec%9d%84-%ec%9d%b4%ec%9a%a9%ed%95%9c-%ed%95%b4%ec%84%9d-%eb%aa%a8%eb%8d%b8%ec%9d%98-%eb%a9%b4%ea%b2%b0%ed%95%a9-fbs-%ea%b8%b0%eb%b2%95/> 관측 2026-11-06.
[^c1276]: 연구실 학회 발표 상세, 딥러닝 기반 실시간 머리 위치에 따른 2차 경로 추정 업데이트를 통한 노면 능동소음제어 성능 향상. <https://acustica.snu.ac.kr/conference/%eb%94%a5%eb%9f%ac%eb%8b%9d-%ea%b8%b0%eb%b0%98-%ec%8b%a4%ec%8b%9c%ea%b0%84-%eb%a8%b8%eb%a6%ac-%ec%9c%84%ec%b9%98%ec%97%90-%eb%94%b0%eb%a5%b8-2%ec%b0%a8-%ea%b2%bd%eb%a1%9c-%ec%b6%94%ec%a0%95-%ec%97%85/> 관측 2026-11-06.
[^c1277]: 연구실 학회 발표 상세, 심리음향 기반 만족도 및 운전 집중력을 고려한 최적 주행음 도출 프로세스 개발. <https://acustica.snu.ac.kr/conference/%ec%8b%ac%eb%a6%ac%ec%9d%8c%ed%96%a5-%ea%b8%b0%eb%b0%98-%eb%a7%8c%ec%a1%b1%eb%8f%84-%eb%b0%8f-%ec%9a%b4%ec%a0%84-%ec%a7%91%ec%a4%91%eb%a0%a5%ec%9d%84-%ea%b3%a0%eb%a0%a4%ed%95%9c-%ec%b5%9c%ec%a0%81/> 관측 2026-11-06.
[^c1278]: 연구실 학회 발표 상세, 티코노프 정칙화를 활용한 디커플링 기법의 정확도 개선 연구. <https://acustica.snu.ac.kr/conference/%ed%8b%b0%ec%bd%94%eb%85%b8%ed%94%84-%ec%a0%95%ec%b9%99%ed%99%94%eb%a5%bc-%ed%99%9c%ec%9a%a9%ed%95%9c-%eb%94%94%ec%bb%a4%ed%94%8c%eb%a7%81-%ea%b8%b0%eb%b2%95%ec%9d%98-%ec%a0%95%ed%99%95%eb%8f%84/> 관측 2026-11-06.
[^c1279]: 연구실 학회 발표 상세, 딥러닝 기반 다공성 재료의 음향 성능 예측 모델 개발. <https://acustica.snu.ac.kr/conference/%eb%94%a5%eb%9f%ac%eb%8b%9d-%ea%b8%b0%eb%b0%98-%eb%8b%a4%ea%b3%b5%ec%84%b1-%ec%9e%ac%eb%a3%8c%ec%9d%98-%ec%9d%8c%ed%96%a5-%ec%84%b1%eb%8a%a5-%ec%98%88%ec%b8%a1-%eb%aa%a8%eb%8d%b8-%ea%b0%9c%eb%b0%9c/> 관측 2026-11-06.
[^c1280]: 연구실 학회 발표 상세, 오토인코더 모델을 활용한 반도체 핸들러 장비의 실시간 고장진단. <https://acustica.snu.ac.kr/conference/%ec%98%a4%ed%86%a0%ec%9d%b8%ec%bd%94%eb%8d%94-%eb%aa%a8%eb%8d%b8%ec%9d%84-%ed%99%9c%ec%9a%a9%ed%95%9c-%eb%b0%98%eb%8f%84%ec%b2%b4-%ed%95%b8%eb%93%a4%eb%9f%ac-%ec%9e%a5%eb%b9%84%ec%9d%98-%ec%8b%a4/> 관측 2026-11-06.
[^c1281]: 연구실 학회 발표 상세, FBS 기반 차량 지지부 강성 최적화 기법 연구. <https://acustica.snu.ac.kr/conference/fbs-%ea%b8%b0%eb%b0%98-%ec%b0%a8%eb%9f%89-%ec%a7%80%ec%a7%80%eb%b6%80-%ea%b0%95%ec%84%b1-%ec%b5%9c%ec%a0%81%ed%99%94-%ea%b8%b0%eb%b2%95-%ec%97%b0%ea%b5%ac/> 관측 2026-11-06.
[^c1282]: 연구실 학회 발표 상세, Interface reduction 기법을 이용한 해석 모델의 면결합 FBS 기법. <https://acustica.snu.ac.kr/conference/interface-reduction-%ea%b8%b0%eb%b2%95%ec%9d%84-%ec%9d%b4%ec%9a%a9%ed%95%9c-%ed%95%b4%ec%84%9d-%eb%aa%a8%eb%8d%b8%ec%9d%98-%eb%a9%b4%ea%b2%b0%ed%95%a9-fbs-%ea%b8%b0%eb%b2%95-2/> 관측 2026-11-06.
[^c1283]: 연구실 학회 발표 상세, 신경망 회로 기반 q-축 전류를 이용한 전동식 브레이크 시스템의 진동 특성 예측. <https://acustica.snu.ac.kr/conference/%ec%8b%a0%ea%b2%bd%eb%a7%9d-%ed%9a%8c%eb%a1%9c-%ea%b8%b0%eb%b0%98-q-%ec%b6%95-%ec%a0%84%eb%a5%98%eb%a5%bc-%ec%9d%b4%ec%9a%a9%ed%95%9c-%ec%a0%84%eb%8f%99%ec%8b%9d-%eb%b8%8c%eb%a0%88%ec%9d%b4%ed%81%ac/> 관측 2026-11-06.
[^c1284]: 연구실 학회 발표 상세, 수정력 기반 시스템 등가 모델 혼합법을 활용한 최적 센서 배치법. <https://acustica.snu.ac.kr/conference/%ec%88%98%ec%a0%95%eb%a0%a5-%ea%b8%b0%eb%b0%98-%ec%8b%9c%ec%8a%a4%ed%85%9c-%eb%93%b1%ea%b0%80-%eb%aa%a8%eb%8d%b8-%ed%98%bc%ed%95%a9%eb%b2%95%ec%9d%84-%ed%99%9c%ec%9a%a9%ed%95%9c-%ec%b5%9c%ec%a0%81/> 관측 2026-11-06.
[^c1285]: 연구실 학회 발표 상세, NVH 성능 향상을 위한 개발 초기단계에서의 서스펜션 부시 강성 최적화. <https://acustica.snu.ac.kr/conference/nvh-%ec%84%b1%eb%8a%a5-%ed%96%a5%ec%83%81%ec%9d%84-%ec%9c%84%ed%95%9c-%ea%b0%9c%eb%b0%9c-%ec%b4%88%ea%b8%b0%eb%8b%a8%ea%b3%84%ec%97%90%ec%84%9c%ec%9d%98-%ec%84%9c%ec%8a%a4%ed%8e%9c%ec%85%98-%eb%b6%80/> 관측 2026-11-06.
[^c1286]: 연구실 학회 발표 상세, 딥러닝 기반 폴리우레탄 폼의 음향 특성 예측 연구. <https://acustica.snu.ac.kr/conference/%eb%94%a5%eb%9f%ac%eb%8b%9d-%ea%b8%b0%eb%b0%98-%ed%8f%b4%eb%a6%ac%ec%9a%b0%eb%a0%88%ed%83%84-%ed%8f%bc%ec%9d%98-%ec%9d%8c%ed%96%a5-%ed%8a%b9%ec%84%b1-%ec%98%88%ec%b8%a1-%ec%97%b0%ea%b5%ac/> 관측 2026-11-06.
[^c1287]: 연구실 학회 발표 상세, 신경망 기반 운전중 전달경로분석법을 통한 소음기여도 및 전달함수 추정. <https://acustica.snu.ac.kr/conference/%ec%8b%a0%ea%b2%bd%eb%a7%9d-%ea%b8%b0%eb%b0%98-%ec%9a%b4%ec%a0%84%ec%a4%91-%ec%a0%84%eb%8b%ac%ea%b2%bd%eb%a1%9c%eb%b6%84%ec%84%9d%eb%b2%95%ec%9d%84-%ed%86%b5%ed%95%9c-%ec%86%8c%ec%9d%8c%ea%b8%b0/> 관측 2026-11-06.
[^c1288]: 연구실 학회 발표 상세, 운전 집중력 향상을 위한 주행음 선정 및 추천 모델 개발. <https://acustica.snu.ac.kr/conference/%ec%9a%b4%ec%a0%84-%ec%a7%91%ec%a4%91%eb%a0%a5-%ed%96%a5%ec%83%81%ec%9d%84-%ec%9c%84%ed%95%9c-%ec%a3%bc%ed%96%89%ec%9d%8c-%ec%84%a0%ec%a0%95-%eb%b0%8f-%ec%b6%94%ec%b2%9c-%eb%aa%a8%eb%8d%b8-%ea%b0%9c/> 관측 2026-11-06.
[^c1289]: 연구실 학회 발표 상세, 자동차 브레이크 시스템의 동특성 파악 및 소음/진동원 분석에 관한 연구. <https://acustica.snu.ac.kr/conference/%ec%9e%90%eb%8f%99%ec%b0%a8-%eb%b8%8c%eb%a0%88%ec%9d%b4%ed%81%ac-%ec%8b%9c%ec%8a%a4%ed%85%9c%ec%9d%98-%eb%8f%99%ed%8a%b9%ec%84%b1-%ed%8c%8c%ec%95%85-%eb%b0%8f-%ec%86%8c%ec%9d%8c-%ec%a7%84%eb%8f%99/> 관측 2026-11-06.
[^c1290]: 연구실 학회 발표 상세, Acoustic performance prediction based on microstructural distributions using a deep learning model. <https://acustica.snu.ac.kr/conference/acoustic-performance-prediction-based-on-microstructural-distributions-using-a-deep-learning-model/> 관측 2026-11-06.
[^c1291]: 연구실 학회 발표 상세, 딥러닝을 활용한 강성 결합품 동특성 예측 연구. <https://acustica.snu.ac.kr/conference/%eb%94%a5%eb%9f%ac%eb%8b%9d%ec%9d%84-%ed%99%9c%ec%9a%a9%ed%95%9c-%ea%b0%95%ec%84%b1-%ea%b2%b0%ed%95%a9%ed%92%88-%eb%8f%99%ed%8a%b9%ec%84%b1-%ec%98%88%ec%b8%a1-%ec%97%b0%ea%b5%ac/> 관측 2026-11-06.
[^c1292]: 연구실 학회 발표 상세, 오토인코더 모델을 활용한 반도체 핸들러 실시간 고장진단. <https://acustica.snu.ac.kr/conference/%ec%98%a4%ed%86%a0%ec%9d%b8%ec%bd%94%eb%8d%94-%eb%aa%a8%eb%8d%b8%ec%9d%84-%ed%99%9c%ec%9a%a9%ed%95%9c-%eb%b0%98%eb%8f%84%ec%b2%b4-%ed%95%b8%eb%93%a4%eb%9f%ac-%ec%8b%a4%ec%8b%9c%ea%b0%84-%ea%b3%a0/> 관측 2026-11-06.
[^c1293]: 연구실 학회 발표 상세, Spindle-Tool Joint Property 추정. <https://acustica.snu.ac.kr/conference/spindle-tool-joint-property-%ec%b6%94%ec%a0%95/> 관측 2026-11-06.
[^c1294]: 연구실 학회 발표 상세, 고무 부시의 고주파수 동적 강성 데이터 베이스 개발. <https://acustica.snu.ac.kr/conference/%ea%b3%a0%eb%ac%b4-%eb%b6%80%ec%8b%9c%ec%9d%98-%ea%b3%a0%ec%a3%bc%ed%8c%8c%ec%88%98-%eb%8f%99%ec%a0%81-%ea%b0%95%ec%84%b1-%eb%8d%b0%ec%9d%b4%ed%84%b0-%eb%b2%a0%ec%9d%b4%ec%8a%a4-%ea%b0%9c%eb%b0%9c/> 관측 2026-11-06.
[^c1295]: 연구실 학회 발표 상세, Real-time fault diagnosis of semiconductor handlers using multiple autoencoders. <https://acustica.snu.ac.kr/conference/real-time-fault-diagnosis-of-semiconductor-handlers-using-multiple-autoencoders/> 관측 2026-11-06.
[^c1296]: 연구실 학회 발표 상세, Study on optimal driving sound conditions based on concentration using the attention network test(ANT). <https://acustica.snu.ac.kr/conference/study-on-optimal-driving-sound-conditions-based-on-concentration-using-the-attention-network-testant/> 관측 2026-11-06.
[^c1297]: 연구실 학회 발표 상세, 액추에이터 구동 소음 예측을 위한 하이브리드 해석 모델 구축. <https://acustica.snu.ac.kr/conference/%ec%95%a1%ec%b6%94%ec%97%90%ec%9d%b4%ed%84%b0-%ea%b5%ac%eb%8f%99-%ec%86%8c%ec%9d%8c-%ec%98%88%ec%b8%a1%ec%9d%84-%ec%9c%84%ed%95%9c-%ed%95%98%ec%9d%b4%eb%b8%8c%eb%a6%ac%eb%93%9c-%ed%95%b4%ec%84%9d/> 관측 2026-11-06.
[^c1298]: 연구실 학회 발표 상세, Optimizing of bushing stiffness for vehicle vibration reduction using dynamic substructuring approach. <https://acustica.snu.ac.kr/conference/optimizing-of-bushing-stiffness-for-vehicle-vibration-reduction-using-dynamic-substructuring-approach/> 관측 2026-11-06.
[^c1299]: 연구실 학회 발표 상세, 공작기계 스핀들-공구 결합부 특성 예측. <https://acustica.snu.ac.kr/conference/%ea%b3%b5%ec%9e%91%ea%b8%b0%ea%b3%84-%ec%8a%a4%ed%95%80%eb%93%a4-%ea%b3%b5%ea%b5%ac-%ea%b2%b0%ed%95%a9%eb%b6%80-%ed%8a%b9%ec%84%b1-%ec%98%88%ec%b8%a1/> 관측 2026-11-06.
[^c1300]: 연구실 학회 발표 상세, 공작기계 주파수 응답함수 추정을 위한 향상된 리셉턴스 결합 기법. <https://acustica.snu.ac.kr/conference/%ea%b3%b5%ec%9e%91%ea%b8%b0%ea%b3%84-%ec%a3%bc%ed%8c%8c%ec%88%98-%ec%9d%91%eb%8b%b5%ed%95%a8%ec%88%98-%ec%b6%94%ec%a0%95%ec%9d%84-%ec%9c%84%ed%95%9c-%ed%96%a5%ec%83%81%eb%90%9c-%eb%a6%ac%ec%85%89/> 관측 2026-11-06.
[^c1301]: 연구실 학회 발표 상세, 딥러닝 모델 기반 헤드트래킹 능동 노면 소음 제어. <https://acustica.snu.ac.kr/conference/%eb%94%a5%eb%9f%ac%eb%8b%9d-%eb%aa%a8%eb%8d%b8-%ea%b8%b0%eb%b0%98-%ed%97%a4%eb%93%9c%ed%8a%b8%eb%9e%98%ed%82%b9-%eb%8a%a5%eb%8f%99-%eb%85%b8%eb%a9%b4-%ec%86%8c%ec%9d%8c-%ec%a0%9c%ec%96%b4/> 관측 2026-11-06.
[^c1302]: 연구실 학회 발표 상세, 양이 회전형 마이크 기반 3차원 음원 위치 추정. <https://acustica.snu.ac.kr/conference/%ec%96%91%ec%9d%b4-%ed%9a%8c%ec%a0%84%ed%98%95-%eb%a7%88%ec%9d%b4%ed%81%ac-%ea%b8%b0%eb%b0%98-3%ec%b0%a8%ec%9b%90-%ec%9d%8c%ec%9b%90-%ec%9c%84%ec%b9%98-%ec%b6%94%ec%a0%95/> 관측 2026-11-06.
[^c1303]: 연구실 학회 발표 상세, 미세구조 분포 기반 딥러닝을 활용한 섬유형 흡음재의 음향 성능 예측. <https://acustica.snu.ac.kr/conference/%eb%af%b8%ec%84%b8%ea%b5%ac%ec%a1%b0-%eb%b6%84%ed%8f%ac-%ea%b8%b0%eb%b0%98-%eb%94%a5%eb%9f%ac%eb%8b%9d%ec%9d%84-%ed%99%9c%ec%9a%a9%ed%95%9c-%ec%84%ac%ec%9c%a0%ed%98%95-%ed%9d%a1%ec%9d%8c%ec%9e%ac/> 관측 2026-11-06.
[^c1304]: 연구실 학회 발표 상세, 전류 기반 내부 가진력 모델을 통한 전동기 NVH 특성 분석. <https://acustica.snu.ac.kr/conference/%ec%a0%84%eb%a5%98-%ea%b8%b0%eb%b0%98-%eb%82%b4%eb%b6%80-%ea%b0%80%ec%a7%84%eb%a0%a5-%eb%aa%a8%eb%8d%b8%ec%9d%84-%ed%86%b5%ed%95%9c-%ec%a0%84%eb%8f%99%ea%b8%b0-nvh-%ed%8a%b9%ec%84%b1-%eb%b6%84/> 관측 2026-11-06.
[^c1305]: 연구실 학회 발표 상세, 고주파수 대역 고무 부시 점탄성 모델링을 통한 복소 동강성 식별. <https://acustica.snu.ac.kr/conference/%ea%b3%a0%ec%a3%bc%ed%8c%8c%ec%88%98-%eb%8c%80%ec%97%ad-%ea%b3%a0%eb%ac%b4-%eb%b6%80%ec%8b%9c-%ec%a0%90%ed%83%84%ec%84%b1-%eb%aa%a8%eb%8d%b8%eb%a7%81%ec%9d%84-%ed%86%b5%ed%95%9c-%eb%b3%b5%ec%86%8c/> 관측 2026-11-06.
[^a104]: 연구실 게시 글, [서울대학교 공과대학] 강연준 교수님. <https://acustica.snu.ac.kr/awards/document/104/> 관측 2026-11-06.
[^a105]: 연구실 게시 글, [대통령 표창] 강연준 교수님. <https://acustica.snu.ac.kr/awards/document/105/> 관측 2026-11-06.
[^a149]: 연구실 게시 글, [2025 한국음향학회 춘계학술발표대회] 박우엽. <https://acustica.snu.ac.kr/awards/document/149/> 관측 2026-11-06.
[^a101]: 연구실 게시 글, [2022년도 하반기 NSV연구장려금] 박우엽. <https://acustica.snu.ac.kr/awards/document/101/?pageid=3> 관측 2026-11-06.
[^g124]: 연구실 게시 글, 2023년 4월 강연준 교수님 대통령 표창. <https://acustica.snu.ac.kr/gallery/document/124/> 관측 2026-11-06.
[^b159]: 연구실 게시 글, [2025년도 한국음향학회 에스티아이엔지니어링 학생논문상] 이정협. <https://acustica.snu.ac.kr/awards/document/159/> 관측 2026-11-06.
[^b158]: 연구실 게시 글, [2025년도 한국음향학회·한국음악지각인지학회 추계공동학술대회] 김현균. <https://acustica.snu.ac.kr/awards/document/158/> 관측 2026-11-06.
[^b155]: 연구실 게시 글, [2024 한국정밀공학회 추계학술대회] 김재윤. <https://acustica.snu.ac.kr/awards/document/155/> 관측 2026-11-06.
[^b153]: 연구실 게시 글, [INTER-NOISE 2025] 김현균. <https://acustica.snu.ac.kr/awards/document/153/> 관측 2026-11-06.
[^b138]: 연구실 게시 글, [2024년도 한국소음진동공학회 (주)NSV학술상] 강연준 교수님. <https://acustica.snu.ac.kr/awards/document/138/> 관측 2026-11-06.
[^b137]: 연구실 게시 글, [2024 한국음향학회 추계학술발표대회] 정원구. <https://acustica.snu.ac.kr/awards/document/137/> 관측 2026-11-06.
[^b103]: 연구실 게시 글, [2024년도 하반기 NSV연구장려금] 우정우. <https://acustica.snu.ac.kr/awards/document/103/> 관측 2026-11-06.
[^b102]: 연구실 게시 글, [2024 한국음향학회 춘계학술발표대회] 오준영, 우정우. <https://acustica.snu.ac.kr/awards/document/102/> 관측 2026-11-06.
[^b99]: 연구실 게시 글, [현대엔지비] 강연준 교수님. <https://acustica.snu.ac.kr/awards/document/99/> 관측 2026-11-06.
[^b100]: 연구실 게시 글, [INTER-NOISE 2022] 박우엽. <https://acustica.snu.ac.kr/awards/document/100/> 관측 2026-11-06.
[^b98]: 연구실 게시 글, [2021년도 추계 소음진동 학술대회] 남정민. <https://acustica.snu.ac.kr/awards/document/98/> 관측 2026-11-06.
[^g163]: 연구실 게시 글, 2026년 5월 한국음향학회. <https://acustica.snu.ac.kr/gallery/document/163/> 관측 2026-11-06.
[^g156]: 연구실 게시 글, 2025년 11월 한국음향학회. <https://acustica.snu.ac.kr/gallery/document/156/> 관측 2026-11-06.
[^g142]: 연구실 게시 글, 2025년 5월 음향학회. <https://acustica.snu.ac.kr/gallery/document/142/> 관측 2026-11-06.
[^p1]: K.-R. Park 외, Y. J. Kang, Transactions of the Korean Society for Noise and Vibration Engineering (2026). <https://doi.org/10.5050/ksnve.2026.36.2.127> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5045817352,publication_year:2021-2026> 관측 2026-11-06.
[^p2]: S.-Y. Park 외, V. V. Gonçalves, SAE technical papers on CD-ROM/SAE technical paper series (2025). <https://doi.org/10.4271/2025-01-0059> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5045817352,publication_year:2021-2026> 관측 2026-11-06.
[^p3]: D. Kim, Y. J. Kang, The Journal of the Acoustical Society of America (2025). <https://doi.org/10.1121/10.0037290> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5045817352,publication_year:2021-2026> 관측 2026-11-06.
[^p4]: U. Park, Y. J. Kang, NOISE-CON proceedings (2023). <https://doi.org/10.3397/in_2023_0165> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5045817352,publication_year:2021-2026> 관측 2026-11-06.
[^p5]: J. Woo, Y. J. Kang, B. J. Kim, NOISE-CON proceedings (2023). <https://doi.org/10.3397/in_2023_0328> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5045817352,publication_year:2021-2026> 관측 2026-11-06.
[^p6]: J. Y. Oh 외, K. H. Lee, The Journal of the Acoustical Society of America (2023). <https://doi.org/10.1121/10.0022989> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5045817352,publication_year:2021-2026> 관측 2026-11-06.
[^p7]: S. S. Yang, J. W. Lee, J.-H. Kim, Y. J. Kang, The Journal of the Acoustical Society of America (2022). <https://doi.org/10.1121/10.0014913> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5045817352,publication_year:2021-2026> 관측 2026-11-06.
[^p8]: U. Park, J. H. Jeon, S. H. You, Y. J. Kang, Transactions of the Korean Society for Noise and Vibration Engineering (2022). <https://doi.org/10.5050/ksnve.2022.32.4.346> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5045817352,publication_year:2021-2026> 관측 2026-11-06.

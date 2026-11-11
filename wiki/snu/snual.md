# SNU Automotive Laboratory (SNUAL)

**서울대학교 공과대학 기계공학부 · 민경덕 교수**

- 분야: 자동차 동력원, 연료전지의 성능·내구성, 수소·이종 연료 엔진, 전기차 배터리 냉각, 모터 손실과 온도 예측[^prof][^fuel][^engine][^battery][^motor]
- 대분야: 기계·로봇·제조, 에너지·환경·지구
- 태그: 연료전지[^fuel], 열전달·열관리[^battery][^motor], 연소·엔진[^engine]
- 홈페이지: <http://snual.snu.ac.kr/>
- 근거와 출처: [SNUAL 근거 페이지](snual-sources.md)

> 자동차를 움직이는 동력원이 전기와 열을 어떻게 만들고 사용하는지 실험과 계산으로 분석하며, 연료전지·엔진·배터리·모터의 성능과 내구성을 연구한다.[^fuel][^engine][^battery][^motor]

## 무엇을 연구하나

SNUAL은 서울대학교 기계공학부 민경덕 교수가 이끄는 연구실이다. 학과는 실험실명을 「동력공학 연구실」로, 연구실 누리집은 「SNU Automotive Laboratory」로 적는다.[^prof][^home] 연구는 연료전지, 엔진 연소, 배터리, 모터의 네 갈래다. 장치 내부에서 일어나는 반응과 물질 이동을 분석하고, 이를 차량 전체의 동력 공급과 냉각 시스템으로 연결한다.[^fuel][^engine][^battery][^motor]

첫 갈래는 고분자 전해질막 연료전지(긴 사슬 형태의 분자로 된 막을 통해 수소 이온을 전달하며 수소와 산소의 반응으로 전기를 얻는 장치)다. 내부 저항을 전류에 대한 반응 특성으로 나누어, 산소가 이동할 때 생기는 저항과 전하가 전달될 때 생기는 저항 등을 분석한다. 막의 수분이 부족하거나 물이 과도하게 쌓이면 성능이 나빠질 수 있으므로, 물의 확산과 수분량에 따른 성질도 측정한다. 전기적 저항과 물 이동에 관한 분석을 바탕으로 연료전지 한 개부터 여러 개를 쌓은 묶음까지 운전 상태를 예측하는 계산 모형을 개발하고, 차량의 공기 공급·가습·냉각 장치와 연결한다.[^fuel]

둘째 갈래는 연소(연료가 산화제와 반응하며 열을 내는 과정)를 이용하는 엔진이다. 산화제는 다른 물질에서 전자를 받는 물질이다. 수소 엔진에서는 희박 연소(연료를 완전히 태우는 데 필요한 양을 넘는 공기를 공급하는 연소)의 안정성과 열효율을 높이기 위해 내부 흐름, 점화에 필요한 에너지, 분사 방식과 밸브가 열리는 시점을 분석한다. 수소와 디젤을 함께 쓰는 이종 연료 엔진에서는 여러 점화·분사 방식을 같은 엔진에서 비교한다. 기계학습은 자료에서 패턴을 배워 예측·분류 알고리즘을 만드는 계산 분야다. 강화학습(시행착오에서 받은 보상을 바탕으로 행동을 배우는 기계학습 방법)을 적용해 운전 조건을 자동으로 조정하는 연구도 한다.[^engine]

셋째 갈래는 전기차 배터리의 열관리다. 배터리 묶음의 냉각 방식과 유로를 계산한다. 유로는 유체(흐르며 모양이 바뀌는 물질로, 액체와 기체를 함께 이르는 말)가 흐르는 통로다. 냉각 방식에 따라 배터리 내부의 온도 차이와 열화(사용하거나 보관하는 동안 성능과 상태가 나빠지는 현상)가 어떻게 달라지는지 실험한다. 전산 유체 해석(유체의 흐름과 열 전달을 수치 계산으로 구하는 방법)으로 자세한 흐름을 살피는 모형과, 차량 시스템을 빠르게 분석하는 간략한 모형을 함께 개발한다. 열폭주(발열과 온도 상승이 서로를 촉진해 온도가 급격히 오르는 현상)를 예측하는 모형에는 배터리 내부 반응과 방출 기체의 성분 변화를 넣으며, 기체의 흐름과 연소가 주변 배터리로 열을 전달하는 과정도 계산하려 한다.[^battery]

넷째 갈래는 전기 모터의 손실과 열이다. 전자기 해석(전기와 자기의 작용을 계산하는 방법)과 유동 해석을 연결해 모터에서 유용한 동력으로 바뀌지 않는 손실을 원인별로 나눈다. 직류는 전류의 방향이 일정한 전기이고, 교류는 전류의 방향과 크기가 주기적으로 바뀌는 전기다. 모터·인버터(직류 전기를 교류 전기로 바꾸는 장치)·감속기(회전 속도를 낮추는 동력 전달 장치)의 손실을 계산하는 모형을 만들고, 주행 조건에 따른 손실과 온도를 예측한다. 열이 전달되는 관계를 이용해 모터의 코일(전류가 흐르도록 도선을 감은 부분)과 회전자(모터 안에서 회전하는 부분)의 온도를 연결하는 모형도 개발한다.[^motor]

## 주요 연구 주제

### 1. 연료전지 내부 저항과 수분, 차량 시스템

연료전지 내부에서 산소와 물이 이동하는 과정, 수분량에 따른 막의 성질, 성능이 떨어지는 원인을 분석한다. 실험으로 얻은 성질을 계산 모형과 연결하고, 가습기와 공기 압축기 등 보조 장치까지 포함해 차량의 전력 소비를 연구한다.[^fuel] 대표 논문 1은 산소 전달 저항을 구분하는 분석법을, 대표 논문 2는 수증기를 주고받는 막 가습기와 연료전지 시스템의 계산 모형을 다룬다.[^p1][^p2]

### 2. 수소·이종 연료 엔진의 연소와 배출물 예측

수소를 쓰거나 서로 다른 연료를 함께 쓰는 엔진에서 연소의 안정성, 열효율과 배출물의 관계를 실험한다.[^engine] 압력은 표면에 수직으로 작용하는 힘을 단위 면적으로 나눈 양이다. 노킹(정상적으로 퍼지는 불꽃 앞쪽의 혼합기가 스스로 점화하며 압력 진동을 일으키는 현상)을 예측하는 연구와, 학습한 모형을 다른 배출물 예측으로 옮기는 연구도 한다.[^article][^p6] 대표 논문 4는 물 직접분사, 대표 논문 5는 대체연료를 섞은 차량의 온실가스 배출, 대표 논문 7은 분무(액체를 방울로 흩뿌리는 과정)가 벽에 부딪힐 때 생기는 액막(표면을 덮는 얇은 액체층)을 다룬다.[^p4][^p5][^p7]

### 3. 배터리 냉각, 열화와 열폭주

냉각수를 흘리는 통로의 형상과 냉각 방식에 따른 배터리의 온도 분포를 연구한다. 배터리 내부 온도 차이가 장기 사용에 미치는 영향은 충방전 실험과 내부 반응을 계산하는 모형으로 분석한다. 열폭주 모형에서는 열이 옆으로 퍼지는 과정과 방출 기체의 흐름·연소를 함께 다루려 한다.[^battery] 대표 논문 3은 주행 모드와 외기 온도에 따라 냉난방과 배터리 열관리에 쓰이는 전력이 어떻게 달라지는지 분석했다.[^p3]

### 4. 모터 손실과 차량 동력원의 에너지 흐름

모터의 손실을 공기와의 마찰, 전류가 흐르며 생기는 발열 등으로 구분하고, 구동계를 이루는 장치별 손실과 온도를 예측하는 모형을 개발한다. 여러 운전 조건의 실험 결과와 계산을 비교해 모형을 조정하며, 차량의 동력 공급 과정에서 에너지가 어디로 전달되고 손실되는지 분석한다.[^motor] 차량 전동화(차량의 구동에 전기를 사용하는 기술로 바꾸는 일)의 온실가스 배출량을 시나리오별로 비교한 연구도 있다.[^p8]

## 대표 논문

민경덕 교수가 저자로 참여한 서울대 재직 시기의 연구 가운데 연료전지, 배터리 열관리, 엔진 및 배출물 예측, 차량 전동화를 고르게 담도록 골랐다. 두 편은 학회 초록이며 발표처 뒤에 표시했다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2024 | [Method for Precise Oxygen Resistance Analysis in Polymer Electrolyte Membrane Fuel Cells Under Various Operating Conditions](https://doi.org/10.1149/ma2024-02443068mtgabs) · ECS Meeting Abstracts (학회 초록) | 연료전지 내부에서 산소가 이동하기 어려운 원인을 나누어 알아보는 분석법을 제안했다. 촉매가 모인 구조를 나타낸 모형과 산소 전달 저항 분석을 결합해, 기체 자체의 확산과 좁은 통로에서의 이동, 이온을 전달하는 물질의 막을 지날 때 생기는 저항을 구분했다. 이 막의 저항이 온도와 습도에 따라 달라지는 관계를 계산하는 식을 만들고, 여러 전류 조건에서 내부 저항 요소가 각각 기여하는 정도를 분석했다.[^p1] | 첫 저자 Hyunsoo Chun, 마지막 저자 Kyoungdoug Min |
| 2 | 2024 | [Development of a Dynamic Model for a Shell-and-Tube Type Gas-to-Gas Polysulfone Hollow Fiber Membrane Humidifier and Optimization of Operating Conditions and Fiber Dimensions to Maximize PEMFC Stack Power in Hydrogen Fuel Cell Vehicles](https://doi.org/10.1149/ma2024-02463281mtgabs) · ECS Meeting Abstracts (학회 초록) | 연료전지의 막이 알맞은 수분을 유지하도록 돕는 가습기를 연구했다. 속이 빈 섬유 모양의 막으로 수증기가 전달되는 현상을 실험과 계산으로 분석하고, 온도에 따른 수분 흡수 특성을 반영하는 모형을 도입했다. 가습기뿐 아니라 공기 압축기, 열교환기와 연료전지 묶음을 연결해 시간에 따른 작동 상태를 계산했다. 운전 조건과 섬유 치수가 출력에 미치는 영향을 분석해 적절한 조건과 형상을 찾았다.[^p2] | 첫 저자 Jiwoong Kim, 마지막 저자 Kyoungdoug Min |
| 3 | 2024 | [Comprehensive Analysis of Battery Thermal Management and Energy Consumption in an Electric Vehicle: Impact of Driving Modes and Ambient Temperatures](https://doi.org/10.1007/s12239-024-00202-8) · International Journal of Automotive Technology | 전기차의 주행 방식과 외부 온도가 배터리 열관리 및 차량의 에너지 소비에 미치는 영향을 분석했다. 추운 조건에서는 난방이, 더운 조건에서는 냉방이 소비량 증가의 주된 원인이었다. 배터리의 온도를 조절하는 시스템은 저온과 고온에서 성능 저하를 줄였으며, 배터리 열관리와 차량 냉난방을 함께 최적화할 필요성을 제시했다.[^p3] | 첫 저자 Inji Park, 마지막 저자 Kyoungdoug Min |
| 4 | 2025 | [Experimental research of water direct injection in the cylinder for the nitrogen oxides reduction and high load extension of the hydrogen direct injection spark ignition engine](https://doi.org/10.1177/14680874251325311) · International Journal of Engine Research | 수소를 엔진 내부에 직접 분사하고 불꽃으로 점화하는 엔진에서 물을 직접 분사하는 전략을 실험했다. 물 분사량과 시점을 조정해 질소산화물 배출을 줄이면서 운전 부하를 높일 가능성을 살폈다. 초록은 물 분사가 질소산화물을 줄이고 높은 부하로 운전할 수 있는 범위를 넓혔다고 보고한다.[^p4] | 첫 저자 Seungil Lee, 마지막 저자 Kyoungdoug Min |
| 5 | 2026 | [Tank-to-Wheel Greenhouse Gas Emissions of Methanol–Gasoline Blends: Vehicle Emissions and Fuel-Based Emission Factors](https://doi.org/10.3390/en19194657) · Energies | 메탄올을 가솔린과 섞었을 때 실제 차량 운행에서 나오는 이산화탄소·메탄·아산화질소를 함께 평가했다. 혼합 비율이 낮은 경우 메탄올 비율이 늘수록 이산화탄소는 대체로 줄었지만, 메탄과 아산화질소는 일관된 변화가 없었다. 여러 혼합 비율에 맞춰 운전할 수 있는 차량에서는 메탄올 비율 증가에 따라 세 기체의 배출이 모두 감소했다. 연료 성질만으로 계산한 값과 차량에서 얻은 값을 비교해, 혼합 연료를 평가할 때 실제 차량 배출도 함께 살펴야 함을 보였다.[^p5] | 첫 저자 Sungwoo Kim, 마지막 저자 Kyoungdoug Min |
| 6 | 2023 | [Task Transfer Learning for Prediction of Transient Nitrogen Oxides, Soot, and Total Hydrocarbon Emissions of a Diesel Engine](https://doi.org/10.1109/access.2023.3294976) · IEEE Access | 디젤 엔진의 질소산화물, 그을음과 전체 탄화수소 배출을 각각 예측할 때 학습을 처음부터 반복하는 부담을 줄이는 방법이다. 한 배출물을 예측하도록 학습한 모형을 가져와 마지막 두 층만 다시 학습해 다른 배출물을 예측했다. 실제 주행을 대표하는 시간 변화 자료에서 가능한 전이 조합을 평가했고, 원래 모형과 전이한 모형의 예측 성능 차이가 작아 기존 모형을 재사용하는 방법이 유효함을 보였다.[^p6] | 첫 저자 Seunghyup Shin, 마지막 저자 Kyoungdoug Min |
| 7 | 2022 | [MODELING OF SPRAY WALL IMPINGEMENT AND FUEL FILM FORMATION UNDER THE GASOLINE DIRECT INJECTION CONDITION](https://doi.org/10.1615/atomizspr.2022037224) · Atomization and Sprays | 가솔린을 직접 분사하는 엔진에서 연료 방울이 벽에 부딪혀 튀거나 벽 위에 막을 만드는 현상을 계산했다. 충돌 뒤 생기는 방울의 움직임을 평면상에서 다루는 모형을 넣고, 빛을 이용해 측정한 분무 반경 및 연료막의 형태·두께와 비교했다. 제안한 모형은 조건마다 모형 상수를 바꾸지 않아도 분무 반경 실험과 기존 모형보다 잘 맞았지만, 연료막 계산에는 추가 개선이 필요하다고 밝혔다.[^p7] | 첫 저자 Junghyun Kim, 마지막 저자 Kyoungdoug Min |
| 8 | 2025 | [Scenario-Based Analysis of Greenhouse Gas Reduction Potential for Passenger Vehicles, Considering Electrification in the Republic of Korea](https://doi.org/10.1007/s12239-025-00255-3) · International Journal of Automotive Technology | 한국의 승용차 등록 대수, 평균 주행거리와 새로 등록하는 차량의 평균 온실가스 배출량에 관한 시나리오를 조합해 전체 배출량을 예측했다. 가장 낙관적인 시나리오에서도 국가 감축 목표 달성이 어렵다고 분석했다. 신차 배출 규제를 모두 충족하더라도 목표 감축량의 절반에 못 미치며, 새로 등록하는 차량이 모두 무배출 차량인 경우에도 목표에 약간 못 미친다는 결과를 제시했다.[^p8] | 첫 저자 Haechan Choi, 마지막 저자 Kyoungdoug Min |

## 교수와 전문 분야

민경덕 교수는 서울대학교 기계공학과에서 학사(1986)와 석사(1988), 미국 MIT 기계공학과에서 박사(1994)를 받았다. 1994–1995년 MIT Sloan Automotive Laboratory 박사후연구원, 1995–1997년 독일 슈투트가르트의 Daimler Benz 엔진 연구소를 거쳤다.[^prof] 연구실 교수 소개는 1997년부터 서울대학교 교수로 재직한다고 적는다.[^pi]

학과는 전공을 「자동차 동력원」으로, 연구분야를 엔진 해석 및 실험, 연료전지 실험 및 해석, 전기차 배터리시스템 열관리로 적는다.[^prof] 연구실의 현재 연구 소개와 대표 논문을 함께 보면 전문 분야는 엔진의 연소·배출물 예측, 연료전지 내부의 저항·수분 이동과 시스템 모형, 배터리와 모터의 열관리로 이어진다.[^fuel][^engine][^battery][^motor][^p1][^p4][^p6]

## 응용 분야

연료전지 자동차와 상용차의 공기 공급·가습·냉각 시스템 설계, 수소 엔진의 연소 안정화와 열효율 개선, 전기차 배터리의 냉각 및 안전성 분석, 모터의 손실·온도 예측을 대상으로 한다.[^fuel][^engine][^battery][^motor] 연구 소개 기사는 현대자동차그룹과 협력한 공동 연구실에서 전기차의 에너지 흐름과 냉각 방법을 연구한다고 적는다.[^article]

## 구성원

2026년 11월 9일 연구실 Member 게시판의 24명이다. 과정·직위는 누리집의 M.S. Course, Ph.D Course, Postdoctoral Researcher, Research Professor에 대응하며, 연구 주제와 학교 이메일은 게시 표기다.[^members1][^members2] 「대표 논문 참여」는 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 김영웅 | 석사과정 | Loss Analysis and Thermal Management System for Motor | qufgoskawk@snu.ac.kr |  |
| 김정호 | 석사과정 | Thermal management system modeling for battery | wjdghqkek@snu.ac.kr |  |
| 신지훈 | 석사과정 | PEM Fuel Cell Experiment | yh04167@snu.ac.kr |  |
| 이건우 | 석사과정 | Thermal managenent system simulation for battery | gunwoo0915@snu.ac.kr |  |
| 이은규 | 석사과정 | Thermal Management System experiment and simulation for battery | dmsrb0409@snu.ac.kr |  |
| 김민호 | 석사과정 | Reinforcement learning applications for engine | alsgh0485@snu.ac.kr |  |
| 조영빈 | 석사과정 | Thermal management system simulation for battery | cyb1894@snu.ac.kr |  |
| 심현빈 | 석사과정 | Thermal management system modeling for battery | shbaby13@snu.ac.kr |  |
| 류태우 | 석사과정 | Modeling and Analysis of PEM Fuel Cell | twryu1643@snu.ac.kr |  |
| 임동현 | 박사과정 | Thermal Management System modeling and experiment for battery | oeroer113@snu.ac.kr |  |
| 전현수 | 박사과정 | PEM Fuel Cell Experiment | bandagom95@snu.ac.kr |  |
| 박인상 | 박사과정 | Thermal Management System Simulation for battery and motor | insang98@snu.ac.kr |  |
| 이승현 | 박사과정 | Experiment and Simulation for Hydrogen combustion engine & Battery | lshlee1336@snu.ac.kr |  |
| 김예빈 | 박사과정 | Modeling and Analysis of PEM Fuel Cell | aria1121@snu.ac.kr |  |
| 장정효 | 박사과정 | PEM Fuel Cell Experiment | chang.junghyo@snu.ac.kr |  |
| 최해찬 | 박사과정 | Battery thermal runaway modeling | haechan@snu.ac.kr |  |
| 김병재 | 박사과정 | Thermal Management System simulation for battery | pjae10@snu.ac.kr |  |
| 이상엽 | 박사과정 | Thermal management system simulation for battery | saltlake9707@snu.ac.kr |  |
| 박범준 | 박사과정 | Deep learning applications for batteries | qjawns513@snu.ac.kr |  |
| 김규범 | 박사과정 | Thermal management system modeling for battery | rbqja3@snu.ac.kr |  |
| 김세현 | 박사과정 | Modeling and Analysis of PEM Fuel Cell | kms3047@snu.ac.kr |  |
| 김세현 | 박사과정 | Loss analysis and Thermal management system modeling for Motor | blessksh@snu.ac.kr |  |
| 김지웅 | 박사후연구원 | PEM Fuel Cell system modeling | woong2079@snu.ac.kr |  |
| 명차리 | 연구교수 | Evaluation of the exhaust gas emission and energy efficiency / Research on hydrogen combustion characteristics in lean combustion engine | gascar@snu.ac.kr |  |

## 졸업생과 이전 구성원

2026년 11월 9일 연구실 Alumni 게시판의 103명이다. 학위·과정과 진로는 누리집이 적은 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 김현주 | 석사 | LG 에너지솔루션 |
| 김지웅 | 박사 | École polytechnique fédérale de Lausanne |
| 김상우 | 석사 | 현대모비스 의왕연구소 |
| 김우재 | 박사 | 삼성전자 Foundry사업부 |
| 신승협 | 박사 | 세종대학교 |
| 김현욱 | 석사 | SK하이닉스 |
| 김승재 | 석사 | 해군사관학교 |
| 김민재 | 석사 | 현대자동차 배터리성능시험팀 |
| 박지환 | 박사 | 삼성전자 설비기술연구소 |
| 이승일 | 박사 | 삼성전자 설비기술연구소 |
| 심재봉 | 박사 | 삼성전자 설비기술연구소 |
| 신석원 | 석사 | 현대자동차 msv전기차성능시험팀 |
| 김영섭 | 석사 | LIG 넥스원 |
| 문선영 | 박사 | 한국기계연구원 열에너지솔루션연구실 |
| 김정현 | 박사 | 삼성전자 Foundry사업부 |
| 강혜현 | 포스트 닥터 | 현대중공업 지능제어시스템연구실 |
| 강민수 | 석사 | 현대자동차 연료전지설계팀 |
| 정종원 | 박사 | 삼성전자 설비기술연구소 |
| 이용주 | 박사 | 삼성전자 설비기술연구소 |
| 이영복 | 박사 | 한국에너지기술연구원 에너지변환연구실 |
| 김기홍 | 석사 | 삼성전자 반도체연구소 |
| 고인석 | 박사 | 삼성전자 반도체연구소 |
| 송세진 | 석사 | 한국조선해양 첨단추진시스템연구실 |
| 최재현 | 석사 | 현대자동차 연료전지설계팀 |
| 주상현 | 박사 | 현대자동차 미래혁신1팀 |
| 조석원 | 박사 | Sandia National Laboratory |
| 송치헌 | 석사 | Tenergy 전동화 개발팀 |
| 남태우 | 석사 | 두산 인프라코어 |
| 김청환 | 석사 | Tenergy 엔진설계팀 |
| 송병근 | 석사 | 현대자동차 연료전지설계팀 |
| 박민제 | 박사 | SK innovation |
| 이규상 | 석사 | University of Washington Holmberg Lab. |
| 김규진 | 박사 | 현대자동차 남양연구소 파워트레인열유동해석팀 |
| 김주한 | 박사 | Argonne National Laboratory |
| 이재엽 | 석사 | 삼성전자 반도체연구소 |
| 강재구 | 석사 | 한겨레신문 사회부 |
| 원동규 | 석사 | 현대자동차 남양연구소 엔진성능시험3팀 |
| 이유일 | 석사 | 서울대학교 김민수 교수님 연구실 |
| 차재혁 | 석사 | 삼성전자 혁신센터 |
| 이윤우 | 석사 | 현대자동차 남양연구소 파워트레인성능시험3팀 |
| 김동수 | 석사 | University Cambridge London |
| 안현철 | 석사 | 국방과학연구소 |
| 이성문 | 석사 | 삼성전자 반도체연구소 |
| 강형묵 | 석사 | Bain & Company Manager |
| 오환영 | 박사 | 한국에너지기술연구원 연료전지연구실 |
| 김남호 | 박사 | Applied Materials |
| 이정우 | 박사 | 충남대학교 자율운항시스템공학과 교수 |
| 김진희 | 석사 | 국방과학연구소 |
| 박재만 | 박사 | 현대자동차 환경기술연구소 연료전지설계팀 |
| 김형준 | 석사 | 현대건설기계 |
| 용진우 | 석사 | 르노삼성자동차 |
| 조성우 | 석사 | 두산인프라코어 기술원 하이브리드 동력기술팀 |
| 노현우 | 석사 | 현대기아자동차 파워트레인매니지먼트팀 |
| 구태형 | 석사 | 현대자동차 남양연구소 전동화시스템시험팀 |
| 이승하 | 박사 | 현대자동차 남양연구소 엔진성능시험2팀 |
| 정대봉 | 박사 | 삼성전자 종합기술원 |
| 이준용 | 박사 | 현대자동차 남양연구소 엔진선행개발팀 |
| 임준원 | 석사 | 현대기아자동차 연비환경전략팀 |
| 송현수 | 석사 | 현대자동차 남양연구소 전기차성능시험팀 |
| 이승현 | 박사 | 현대자동차 선행기술원 |
| 기민영 | 석사 | 현대자동차 남양연구소 엔진제어개발팀 |
| 이정연 | 석사 |  |
| 이경현 | 박사 | 현대자동차 남양연구소 엔진성능시험2팀 |
| 유성은 | 박사 | 현대자동차 남양연구소 엔진선행개발팀 |
| 조준현 | 박사 | 한국에너지기술연구원 에너지효율소재연구본부 |
| 이재영 | 석사 | 콘티넨탈 오토모티브 시스템 ㈜ |
| 김보경 | 석사 | 르노삼성자동차 중앙연구소 냉각공조설계 |
| 허동한 | 석사 | 현대자동차 남양연구소 엔진성능시험1팀 |
| 박원아 | 박사 | 경성대학교 기계자동차공학과 |
| 이효원 | 석사 | 현대자동차 남양연구소 상용엔진성능시험팀 |
| 하태훈 | 박사 | 가천대학교 기계공학과 |
| 최승목 | 박사 | 현대자동차 남양연구소 엔진성능시험3팀 |
| 강상규 | 박사 | 서울대학교 조선해양공학부 |
| 김민재 | 박사 | 명지대학교 |
| 이상열 | 박사 | 한성대학교 기계전자공학부 |
| 온형석 | 박사 | 현대자동차 선행기술원 |
| 김성욱 | 석사 | - |
| 홍국의 | 석사 | 현대기아자동차 중장기사업기획팀 |
| 이동훈 | 석사 | 현대자동차 남양연구소 연료전지제어개발팀 |
| 김영진 | 석사 | 르노삼성자동차 중앙연구소 PT제어개발팀 |
| 권혁선 | 박사 | 르노삼성자동차 중앙연구소 |
| 이학범 | 석사 | Stanford University |
| 방정환 | 박사 | 현대자동차 남양연구소 에너지제어리서치랩 |
| 이정원 | 석사 | 르노삼성자동차 중앙연구소 PT제어개발팀 |
| 권욱 | 석사 | 네모 파트너즈 SCG |
| 임재만 | 박사 | Siemens |
| 박순영 | 석사 | 한국항공우주연구원 추진3동엔진팀 |
| 김용래 | 박사 | 한국기계연구원 그린동력연구실 |
| 성현택 | 석사 | 삼성중공업 |
| 박상언 | 석사 | 현대자동차 남양연구소 파워트레인성능시험1팀 |
| 김용태 | 석사 | - |
| 이훈구 | 석사 | 현대자동차 남양연구소 엔진성능시험2팀 |
| 장용석 | 석사 | 산업은행 리스크관리본부(런던지점) |
| 정재경 | 석사 | 현대자동차 남양연구소 엔진성능시험3팀 |
| 장진석 | 석사 | 현대차동차 남양연구소 파워트레인센터 엔진성능시험2팀 |
| 윤일한 | 석사 | 현대자동차 드라이빙익스피리언스팀 |
| 김세준 | 박사 | 현대자동차 연비시험1팀 |
| 최회명 | 박사 | 가천대학교 기계공학과 |
| 임용섭 | 석사 | 대구경북과학기술원(DGIST) 기초학부 |
| 김만식 | 박사 | 국방과학연구소 |
| 유상석 | 석사 | 충남대학교 기계공학부 |
| 김형욱 | 박사 | - |
| 조훈 | 박사 | - |

## 최근 논문 목록 (2021–2026)

연구실의 국제 학술지 57항목, 국내 학회 67항목과 국제 학회 10항목이다. 연도는 누리집의 연도 구역이며, 제목·저자·발표처는 게시 표기다. 제목 끝의 줄임표도 게시 표기다. DOI는 해당 문헌의 식별자다.[^pubscope]

### 국제 학술지

**2026**

- Yebeen Kim, Sanggyu Kang, Kyoungdoug Min. "Integrated modeling and multi-objective optimization of a PE…". *Applied Thermal Engineering*. DOI <https://doi.org/10.1016/j.applthermaleng.2026.132017>.[^j1]
- Jiwoong Kim, Sehyeon Kim, Hosik Lee, Sanggyu Kang, Kyoungdoug Min. "Integrated multiscale modeling and coordinated balance-of-pl…". *Applied Energy*. DOI <https://doi.org/10.1016/j.apenergy.2026.128258>.[^j1]
- Jiwoong Kim, Sehyeon Kim, Seong-Yong Woo, Jaebong Sim, Hosik Lee, Sanggyu Kang, Kyoungdoug Min. "A novel approach to modeling of polymer electrolyte membrane…". *Applied Energy*. DOI <https://doi.org/10.1016/j.apenergy.2026.128190>.[^j1]
- Junghyun Kim , Kyoungdoug Min. "Curl turbulent kinetic energy as a flame-surface-related Ind…". *Applied Thermal Engineering*. DOI <https://doi.org/10.1016/j.applthermaleng.2026.131711>.[^j1]
- Sehyeon Kim, Jiwoong Kim, Hyunsoo Chun, Junghyo Chang, Jihun Shin, Sanggyu Kang, Kyoungdoug Min. "Hydration-dependent electrochemical parameters for improved …". *Chemical Engineering Journal*. DOI <https://doi.org/10.1016/j.cej.2026.177556>.[^j1]
**2025**

- Junghyun Kim, Kyoungdoug Min. "Quantitative Parameter of Resolved Turbulence for LES Turbul…". *Total Environment Engineering*. DOI <https://doi.org/10.1016/j.teengi.2025.100061>.[^j1]
- Kiyeon Kim, Jeongho Kim, Seungil Lee, Seungjae Kim, Jongyoon Son, Seunghyun Lee, Kyoungdoug Min, Chalee Myung, Kyungwook Min, Jeongwoo Lee. "Comparative study of hydrogen combustion modes in a single-c…". *Applied Thermal Engineering*. DOI <https://doi.org/10.1016/j.applthermaleng.2025.129230>.[^j1]
- Sungwoo Kim, Kyoungdoug Min. "Particle number and size distribution in hybrid electric veh…". *Fuel*. DOI <https://doi.org/10.1016/j.fuel.2025.137527>.[^j1]
- Jaebong Sim, Junghyo Chang, Jiwoong Kim, Hyunsoo Chun, Yebeen Kim, Byeongjae Kim, Sanggyu Kang, Kyoungdoug Min. "Impacts of carbon corrosion, freeze/thaw, and acidic solutio…". *Journal of Power Sources*. DOI <https://doi.org/10.1016/j.jpowsour.2025.236869>.[^j1]
- Seungil Lee, Jeongwoo Lee, Seungjae Kim, Kiyeon Kim, Seunghyun Lee, Kyoungdoug Min. "Experimental research of water direct injection in the cylin…". *International Journal of Engine Research*. DOI <https://doi.org/10.1177/14680874251325311>.[^j1]
- Kiyeon Kim, Seungil Lee, Seungjae Kim, Seunghyun Lee, Kyoungdoug Min, Sechul Oh, Jongyoon Son, Jeongwoo Lee. "Nitrogen Oxides Reduction Potential Via Water Direct Injecti…". *SAE Technical Paper*. DOI <https://doi.org/10.4271/2025-01-8427>.[^j1]
- Haechan Choi, Jihwan Park, Cha-Lee Myung, Hoimyung Choi, Inji Park, Charyung Kim, Kyoungdoug Min. "Scenario-Based Analysis of Greenhouse Gas Reduction Potentia…". *International Journal of Automotive Technology*. DOI <https://doi.org/10.1007/s12239-025-00255-3>.[^j1]
- Seunghyun Lee, Kiyeon Kim, Jeongwoo Lee, Yongrae Kim, Jaeyoung Cho, Sechul Oh, Kyoungdoug Min. "NOx reduction in hydrogen-fueled direct-injected spark ignit…". *Energy*. DOI <https://doi.org/10.1016/j.energy.2025.136085>.[^j1]
**2024**

- Hyunsoo Chun, Youngseop Lee, Jiwoong Kim, Jung Hyo Chang, Jaebong Sim, Jin Young Kim, Kyoungdoug Min. "Synergistic analysis of oxygen transport resistance in polym…". *Energy Conversion and Management*. DOI <https://doi.org/10.1016/j.enconman.2024.119270>.[^j1]
- Jiwoong Kim, Sehyeon Kim, Seong-Yong Woo, Hyunsoo Chun, Jaebong Sim, Sanggyu Kang, Kyoungdoug Min. "In-situ analysis of water transport properties through a rei…". *Chemical Engineering Journal*. DOI <https://doi.org/10.1016/j.cej.2024.158078>.[^j1]
- Woojae Kim, Jongwon Chung, Junghyun Kim, Cha-Lee Myung, Kyeonghyeon Lee, Jongbum Park, Kyungdoug Min. "The Effect of Water Injection on a Naturally Aspirated Spark…". *International Journal of Automotive Technology*.[^j2]
- Ki Yeon Kim, Seung il Lee, Seung Hyun Lee, Seung Jae Kim, Kyoung Doug Min, Jeong Woo Lee. "Efects of Various Bore–Stroke Ratios on Hydrogen Direct Inje…". *International Journal of Automotive Technology*.[^j2]
- Seungjae Kim, Jeongwoo Lee, Seungil Lee, Seunghyun Lee, Kiyeon Kim, Kyoungdoug Min. "Efects of Various Compression Ratios on a Direct Injection S…". *International Journal of Automotive Technology*. DOI <https://doi.org/10.1007/s12239-024-00096-6>.[^j2]
- Jeongwoo Lee, Sanghyun Chu, Jaegu Kang, Kyoungdoug Min. "Experimental Research on the Carbon Dioxides Reduction Poten…". *International Journal of Automotive Technology*. DOI <https://doi.org/10.1007/s12239-024-00026-6>.[^j2]
- Jeongwoo Lee, Sanghyun Chu, Jaegu Kang, Kyoungdoug Min. "Efects of Varying Equivalence Ratios on the Combustion Efcie…". *International Journal of Automotive Technology*.[^j2]
- Jiwoong Kim, Sehyeon Kim, Hyunsoo Chun, Jaebong Sim, Seong-Young Woo, Sanggyu Kang, Kyoungdoug Min. "Comprehensive analysis of polysulfone membrane humidifier in…". *Journal of Membrane Science*. DOI <https://doi.org/10.1016/j.memsci.2024.123234>.[^j2]
- Jeongwoo Lee, Sanghyun Chu, Insuk Ko, Jaegu Kang, Hyunsung Jung, Yohan Chi, Kyoungdoug Min. "Effects of dual-spark ignition system with two different pis…". *INTERNATIONAL JOURNAL OF ENGINE RESEARCH*. DOI <https://doi.org/10.1177/14680874241272886>.[^j2]
- Hyunsoo Chun, Jung Hyo Chang, Ji-woong Kim, Jaebong Sim, Kyoungdoug Min. "Durability analysis of polymer electrolyte membrane fuel Cel…". *International Journal of Hydrogen Energy*. DOI <https://doi.org/10.1016/j.ijhydene.2024.05.154>.[^j2]
- Yebeen Kim, Jiwoong Kim and Kyoungdoug Min. "Analysis of Power Consumption on BOP System in a Fuel Cell E…". *International Journal of Automotive Technology*. DOI <https://doi.org/10.1007/s12239-024-00064-0>.[^j2]
- Jaebong Sim, Jiwoong Kim, Hyunsoo Chun, Junghyo Chang, Yebeen Kim, Byeongjae Kim, Sanggyu Kang, Kyoungdoug Min. "Variation in performance and characteristics of long-term op…". *Journal of Power Sources*. DOI <https://doi.org/10.1016/j.jpowsour.2023.234026>.[^j2]
- Jaebong Sim, Hyunsoo Chun, Junghyo Chang, Jiwoong Kim, Byeongjae Kim, Yebeen Kim, Sanggyu Kang, Kyoungdoug Min. "Impacts of characteristics of carbon black comprising microp…". *Journal of Power Sources*. DOI <https://doi.org/10.1016/j.jpowsour.2023.233989>.[^j2]
**2023**

- Jihwan Park, Seunghyup Shin, Sechul Oh, Sangyul Lee, Woojae Shin, Kyoungdoug Min. "Knock Onset Determination with 1D CNN Using Random Search Hy…". *International Journal of Automotive Technology*. DOI <https://doi.org/10.1007/s12239-023-0113-7>.[^j2]
- Seungil Lee, Yongjoo Lee, Joohan Kim, Namho Kim, Chalee Myung, Hoimyung Choi, Kyoungdoug Min. "Effect of Active Eco-Mode on Reduction of On-Road Co2 Emissi…". *International Journal of Automotive Technology*. DOI <https://doi.org/10.1007/s12239-023-0115-5>.[^j2]
- Seunghyun Lee, Yongrae Kim, Jeoungwoo Lee, Kiyeon Kim, Seungil Lee, Kyoungdoug Min, Sechul Oh. "Energy and exergy analyses of hydrogen-fueled spark ignition…". *Fuel*. DOI <https://doi.org/10.1016/j.fuel.2023.128588>.[^j2]
- Hyunjung Oh, Kyoung-Pyo Ha, Kyoungdoug Min. "Development of a New Measurement System for Piston Ring Fric…". *International Journal of Automotive Technology*. DOI <https://doi.org/10.1007/s12239-023-0098-2>.[^j2]
- Seunghyup Shin, Minjae Kim, Jihwan Park, Sangyul Lee, Kyoungdoug Min. "Task Transfer Learning for Prediction of Transient Nitrogen …". *IEEE Access*. DOI <https://doi.org/10.1109/access.2023.3294976>.[^j3]
- Junghyun Kim, Kyoungdoug Min. "Analysis of Combustion Cyclic Variation in a Lean Burn Spark…". *Fuel*. DOI <https://doi.org/10.1016/j.fuel.2023.127886>.[^j3]
- Seokwon Cho, Chiheon Song, Youngbok Lee, Namho Kim, Sechul Oh, Kyoungdoug Min. "Prediction of knock propensity using stochastic modeling in …". *INTERNATIONAL JOURNAL OF ENGINE RESEARCH*. DOI <https://doi.org/10.1177/14680874221074993>.[^j3]
**2022**

- Jeongwoo Lee, Sanghyun Chu, Donghyun Lim, Hyunsung Jung, Yohan Chi, Kyoungdoug Min. "Comparison of combustion and emission characteristics under …". *Energy*. DOI <https://doi.org/10.1016/j.energy.2021.122855>.[^j3]
- Minsoo Kang, Jaebong Sim, Kyoungdoug Min. "Analysis of performance degradation on the components in pol…". *Journal of Power Sources*. DOI <https://doi.org/10.1016/j.jpowsour.2022.232236>.[^j3]
- Jaebong Sim, Minsoo Kang, Kyoungdoug Min. "Effects of porosity gradient and average pore size in the in…". *Journal of Power Sources*. DOI <https://doi.org/10.1016/j.jpowsour.2022.231912>.[^j3]
- Jaebong Sim, Minsoo Kang, Hwanyeong Oh, Eunsook Lee, Jy-Young Jyoung, Kyoungdoug Min. "The effect of gas diffusion layer on electrochemical effecti…". *Renewable Energy*. DOI <https://doi.org/10.1016/j.renene.2022.07.096>.[^j3]
- Jaebong Sim, Minsoo Kang, Hwanyeong Oh, Eunsook Lee, Jy-Young Jyoung, Kyoungdoug Min. "Effects of porosity gradient and average pore size in the in…". *Renewable Energy*.[^j3]
- Jaebong Sim, Minsoo Kang, Kyoungdoug Min, Eunsook Lee, Jy-Young Jyoung. "Effects of microporous layer penetration ratio and substrate…". *Journal of Mechanical Science and Technology*. DOI <https://doi.org/10.1007/s12206-022-0841-z>.[^j3]
- Insuk Ko, Junghyun Kim, Kyoungdoug Min. "Understanding the effect of turbulent flow on the combustion…". *Fuel*. DOI <https://doi.org/10.1016/j.fuel.2022.123773>.[^j3]
- Taewoo Nam, Sanghyun Chu, Sunyoung Moon, Kyoungdoug Min. "Effects of Piston Bowl Geometries On Diesel and Gasoline Dua…". *International Journal of Automotive Technology*. DOI <https://doi.org/10.1007/s12239-022-0086-y>.[^j3]
- Jaebong Sim, Minsoo Kang, Jiwoong Kim, Kyoungdoug Min. "Effects of operating conditions, various properties of the g…". *Renewable Energy*. DOI <https://doi.org/10.1016/j.renene.2022.06.132>.[^j4]
- Minsoo Kang, Jaebong Sim, Kyoungdoug Min. "Analysis of surface and interior degradation of gas diffusio…". *International Journal of Hydrogen Energy*. DOI <https://doi.org/10.1016/j.ijhydene.2022.06.256>.[^j4]
- Kihong Kim, Donghyun Lim, Hyungjin Shin, Sanghyun Chu, Jeongwoo Lee, Kyoungdoug Min. "High-load expansion varying effective compression ration usi…". *International Journal of Automotive Technology*.[^j4]
- Seunghyup Shin, Youngbok Lee, Yongjoo Lee, Jihwan Park, Minjae Kim, Sangyul Lee, Kyoungdoug Min. "Designing a steady-state experimental dataset for predicting…". *Expert Systems with Applications*. DOI <https://doi.org/10.1016/j.eswa.2022.116919>.[^j4]
- Jaebong Sim, Minsoo Kang, Kyoungdoug Miㅜ, Eunsook Lee, Jy-Young Jyoung. "Effect of capillary pressure gradient in microporous layer o…". *International Journal of Hydrogen Energy*. DOI <https://doi.org/10.1016/j.ijhydene.2022.03.265>.[^j4]
- Jaebong Sim, Minsoo Kang, Kyoungdoug Min, Eunsook Lee, Jy-Young Jyoung. "Effects of carbon corrosion on proton exchange membrane fuel…". *Renewable Energy*. DOI <https://doi.org/10.1016/j.renene.2022.04.015>.[^j4]
- Sunyoung Moon, Gyujin Kim, Youngbok Lee, Yongjoo Lee, Kyoungdoug Min. "Numerical analysis of the combustion and emission characteri…". *International Journal of Automotive Technology*. DOI <https://doi.org/10.1007/s12239-022-0039-5>.[^j4]
- Youngbok Lee, Yongjoo Lee, Sunyoung Moon, Seungha Lee, Youngjun Roh, Kyoungdoug Min. "Development of semi-empirical soot emission model for a CI e…". *SCIENCE OF THE TOTAL ENVIRONMENT*. DOI <https://doi.org/10.1016/j.scitotenv.2022.153327>.[^j4]
- Donghyun Lim, Jeongwoo Lee, Hyungjin Shin, Kihong Kim, Sunyoung Moon, Kyoungdoug Min. "Effect of swirl motion on combustion and emissions character…". *International Journal of Automotive Technology*. DOI <https://doi.org/10.1007/s12239-022-0035-9>.[^j4]
- Junghyun Kim, Jongwon Chung, Jaeyeop Lee, Sunyoung Moon, Kyoungdoug Min. "Modeling of spray wall impingement and fuel film formation u…". *ATOMIZATION AND SPRAYS*. DOI <https://doi.org/10.1615/atomizspr.2022037224>.[^j4]
- Jeongwoo Lee, Sanghyun Chu, Donghyun Lim, Hyunsung Jung, Yohan Chi, and Kyoungdoug Min. "Comparison of Combustion and Emission Characteristics under …". *Energy*. DOI <https://doi.org/10.1016/j.energy.2021.122855>.[^j4]
- Namho Kim, Jongwon Chung, Joohan Kim, Seokwon Cho, Kyoungdoug Min. "Effect of injection parameters on combustion and emission ch…". *ENERGY CONVERSION AND MANAGEMENT*. DOI <https://doi.org/10.1016/j.enconman.2021.115059>.[^j4]
**2021**

- YoungGyun Kim, Younggyun Cho, Youngbok Lee, Kyoungdoug Min, SungHoon Ahn. "Nanoscale Ag/WO3 Multilayered Fabry-Perot Cavities for Color…". *ACS Applied Nano Materials*. DOI <https://doi.org/10.1021/acsanm.1c01918>.[^j4]
- Jongmyung Kim, Jihwan Park, Seunghyup Shin, Yongjoo Lee, Kyoungdoug Min, Sangyul Lee#, Minjae Kim. "Prediction of engine NOx for virtual sensor using deep neura…". *OIL & GAS SCIENCE AND TECHNOLOGY-REVUE D IFP ENERGIES NOUVELLES*. DOI <https://doi.org/10.2516/ogst/2021054>.[^j5]
- Seokwon Cho, Chiheon Song, Namho Kim, Sechul Oh, Dong Han, Kyoungdoug Min. "Influence of the wall temperatures of the combustion chamber…". *Applied Thermal Engineering*.[^j5]
- Insuk Ko, Federico Rulli, Stefano Fontanesi, Alessandro d’Adamo, Kyoungdoug Min. "Methodology for the large eddy simulation and particle image…". *International Journal of Engine Research*.[^j5]

### 국내 학회

**2025**

- 장정효, 전현수, 민경덕. "Investigation of Durability and Internal Resistance Behavior…". *2025 한국전기화학회 추계총회 및 학술발표회*.[^d1]
- 김세현, 김지웅, 민경덕. "Effects of water content and temperature on ECSA and hydrog…". *2025 한국전기화학회 추계총회 및 학술발표회*.[^d1]
- 전현수, 신지훈, 김세현, 장정효, 민경덕. "Integration of NDMS Derived Ionomer Hydration and Catalyst A…". *2025 한국전기화학회 추계총회 및 학술발표회*.[^d1]
- 신지훈, 전현수, 김형석, 민경덕. "Analysis of Water Diffusion Behavior in PEMFC Electrolyte Me…". *2025 한국전기화학회 추계총회 및 학술발표회*.[^d1]
- 장정효, 전현수, 신지훈, 민경덕. "라디칼 스캐빈저 적용에 따른 고분자 전해질 연료전지의 내구성 및 내부 저항 특성 분석". *2025 한국자동차공학회 추계학술대회*.[^d1]
- 김세현, 김지웅, 민경덕. "수분 함량 및 온도가 PEMFC의 ECSA와 수소 크로스오버에 미치는 영향". *2025 한국자동차공학회 추계학술대회*.[^d1]
- 박인상, 김세현, 김영웅, 임재만, 서인기, 민경덕. "CFD를 활용한 매입형 영구자석 동기전동기의 손실 및 효율 맵 구축에 대한 연구". *2025 한국자동차공학회 추계학술대회*.[^d1]
- 김정호, 김기연, 이승현, 구준모, 김정기, 이정우, 명차리, 민경덕. "수소 전기점화 내연기관에서 스파크 플러그 사양이 연소 특성에 미치는 영향 분석". *2025 한국자동차공학회 추계학술대회*.[^d1]
- 김세현, 박인상, 김영웅, 박철수, 안희원, 민경덕. "Calorimetric Method를 통한 주행사이클의 PE시스템 손실 추정". *2025 한국자동차공학회 추계학술대회*.[^d1]
- 김규범, 명차리, 이현우, 박인지, 이민호, 민경덕. "외기 온도가 전기자동차의 에너지 소비량에 미치는 영향에 관한 연구". *2025 한국자동차공학회 추계학술대회*.[^d1]
- 조영빈, 이상엽, 민경덕. "유동 유도판을 적용한 파우치형 배터리 액침 냉각 시스템의 민감도 분석 및 다목적 최적화". *2025 한국자동차공학회 추계학술대회*.[^d1]
- 박범준, 김병재, 민경덕. "리튬 이온 배터리 모듈의 열적 특성 분석을 위한 등가 회로 네트워크 모델링". *2025 한국자동차공학회 추계학술대회*.[^d1]
- 김준형, 이승현, 이은규, 민경덕. "S-ECM: 전극 내 화학양론비 기반 등가회로모델을 사용한 배터리셀 모델링 정확도 개선". *2025 한국자동차공학회 추계학술대회*.[^d1]
- 김현주, 최해찬, 민경덕. "배터리 구성요소의 세부적인 열분해 반응 을 고려한 개선된 열 폭주 모델링". *2025 한국자동차공학회 춘계학술대회*.[^d1]
- 최해찬, 김현주, 민경덕. "Vent gas 의 연소를 고려한 배터리 모듈 내 열폭주 확산 모델링". *2025 한국자동차공학회 춘계학술대회*.[^d1]
- 이상엽, 민경덕. "급속충전 조건에서 다양한 배터리 냉각방식의 민감도 분석을 위한 CFD 해석 연구". *2025 한국자동차공학회 춘계학술대회*.[^d2]
- 이승현, 김우재, 김준형, 이상준, 권오현, 이학수, 김민재, 민경덕. "대용량 파우치 배터리 셀 내에서의 온도구배 현상과 열화 특성 분석". *2025 한국자동차공학회 춘계학술대회*.[^d2]
- 김예빈, 김지웅, 김세현, 강상규, 민경덕. "연료전지 전기버스의 열관리 시스템 통합 모델링 및 핀-튜브 라디에이터의 형상 최적화". *2025 한국자동차공학회 춘계학술대회*.[^d2]
**2024**

- 김세현, 김지웅, 김예빈, 강상규, 민경덕. "고분자 전해질막 연료전지 스택의 냉각 시스템 설계에 따른 특성 연구". *2024 한국자동차공학회 추계학술대회*.[^d2]
- 김규범, 임동현, 이현우, 김자룡, 박인지, 민경덕. "실도로 주행 조건에서 주행모드가 전기자동차의 에너지 소바량에 미치는 영향에 관한 연구". *2024 한국자동차공학회 추계학술대회*.[^d2]
- 김세현, 김현욱, 박인상, 민경덕. "IPMSM 의 열전달 모델 기반 모터 온도 추정". *2024 한국자동차공학회 추계학술대회*.[^d2]
- 박범준, 김우재, 이승현, 김민재, 박철수, 민경덕. "셀 간 편차 연구를 위한 리튬 이온 배터리의 등가 회로 네트워크 모델링". *2024 한국자동차공학회 추계학술대회*.[^d2]
- 박인상, 김현욱, 김세현, 임재만, 서인기, 민경덕. "CFD를 활용한 매입형 영구자석 동기전동기의 손실량 분석에 대한 연구". *2024 한국자동차공학회 추계학술대회*.[^d2]
- 김준형, 이승현, 김우재, 김민재, 민경덕. "NMC 리튬이온 배터리셀의 HPPC 실험을 통한 휴지 단계 전압 분석 및 등가회로모델 패러미터 추정". *2024 한국자동차공학회 추계학술대회*.[^d2]
- 이승현, 김우재, 김민재, 김준형, 이상준, 권오현, 민경덕. "냉각방식에 따른 배터리 내 온도구배 현상과 열화 특성 분석". *2024 한국자동차공학회 추계학술대회*.[^d2]
- 최해찬, 민경덕. "발열 반응 모델링을 통한 양극재에 따른 열폭주 경향성 분석". *2024 한국자동차공학회 춘계학술대회*.[^d2]
- 김지웅, 김예빈, 김병재, 김세현, 민경덕. "수소전기버스 차량의 K-WHVC 모드에 의한 연료전지 시스템 특성 연구". *2024 한국자동차공학회 춘계학술대회*.[^d2]
- 장정효, 김지웅, 전현수, 민경덕. "다양한 전압 조건에서 PEMFC의 MEA 및 GDL의 내구 성능 분석". *2024 한국자동차공학회 춘계학술대회*.[^d2]
- 전현수, 이영섭, 김지웅, 장정효, 김진영, 민경덕. "다양한 작동 조건에서 고분자 전해질 막 연료 전지의 정밀한 산소 저항 분석을 위한 방법론". *2024 한국자동차공학회 춘계학술대회*.[^d2]
- 김예빈, 김지웅, 민경덕. "연료전지 전기 버스의 BOP 시스템 제어로직 분석에 기반한 차량의 에너지 흐름에 관한 연구". *2024 한국자동차공학회 춘계학술대회*.[^d2]
- 김승재, 이승일, 이승현, 김기연, 이정우, 민경덕. "수소 직분 SI 엔진의 NOx 배출물 저감을 위한 물 직분사 전략에 관한 연구". *2024 한국자동차공학회 춘계학술대회*.[^d3]
- 이상엽, 김우재, 박철수, 이건구, 엄기문, 민경덕. "CFD를 활용한 양면냉각 배터리 팩의 냉각 성능 향상에 대한 연구". *2024 한국자동차공학회 춘계학술대회*.[^d3]
**2023**

- 전현수, 장정효, 김지웅, 민경덕. "시간 이완 분포 분석을 통한 고분자 전해질막 연료전지 기체확산층의 미세다공층 유무에 따른 내구 특성 분석". *2023 한국자동차공학회 추계학술대회*.[^d3]
- 최해찬, 박인상, 김우재, 박원아, 기원용, 오해진, 민경덕. "3-D CFD를 활용한 배터리 팩에서의 열폭주 확산 모델링". *2023 한국자동차공학회 추계학술대회*.[^d3]
- 김승재, 이승일, 이승현, 김기연, 이정우, 민경덕. "수소 직분 SI 엔진의 희박 연소 조건 하 연소실 최적화 및 과급을 통한 부하 확장에 관한 연구". *2023 한국자동차공학회 추계학술대회*.[^d3]
- 김현욱, 임동현, 박지환, 김지웅, 민경덕. "딥러닝을 활용한 실차 실험 기반 공기 압축기 모터 온도 예측". *2023 한국자동차공학회 추계학술대회*.[^d3]
- 김병재, 김지웅, 김예빈, 민경덕. "전기차 배터리 팩 냉각 시스템 모델 개발". *2023 한국자동차공학회 추계학술대회*.[^d3]
- 김민재, 박지환, 이종권, 김지호, 민경덕. "CNN 기반 연소실 내 와류 검출 모델 개발". *2023 한국자동차공학회 추계학술대회*.[^d3]
- 김예빈, 김지웅, 김병재, 민경덕. "수소 연료전지 자동차의 PEMFC 시스템 시뮬레이션 모델 개발". *2023 한국자동차공학회 추계학술대회*.[^d3]
- 김기연, 장일품, 이승일, 이승현, 민경덕, 이정우. "수소 직분 전기점화 엔진의 운전 변수 별 질소산화물과 열효율 특성에 관한 실험적 분석". *2023 한국자동차공학회 춘계학술대회*.[^d3]
- 임동현, 김강진, 박인상, 명차리, 민경덕. "전기자동차 1회 충전 주행거리 측정시험 개선방안에 관한 연구". *2023 한국자동차공학회 춘계학술대회*.[^d3]
- 박인상, 최해찬, 민경덕. "CFD를 활용한 액침 냉각식 배터리 모듈의 냉각 성능 개선에 대한 연구". *2023 한국자동차공학회 춘계학술대회*.[^d3]
- 이승현, 이승일, 김승재, 김기연, 이정우, 민경덕. "수소 직분 전기점화 엔진에서의 스트로크-보어 비에 따른 운전 조건 별 연소 특성 분석". *2023 한국자동차공학회 춘계학술대회*.[^d3]
- 장정효, 심재봉, 김지웅, 전현수, 김병재, 민경덕. "고분자 전해질 연료전지의 MEA 내구성 평가 방법의 비교". *2023 한국자동차공학회 춘계학술대회*.[^d3]
- 김지웅, 심재봉, 김예빈, 전현수, 장정효, 김병재, 민경덕. "작동 조건에 따른 PEMFC 단위 셀 모델 개발". *2023 한국자동차공학회 춘계학술대회*.[^d3]
**2022**

- 심재봉, 김지웅, 장정효, 민경덕. "가속화 시험법이 기체확산층의 내구 및 성능에 미치는 영향". *2022 한국수소및신에너지학회 추계학술대회*.[^d4]
- 오현정, 하경표, 조진우, 민경덕. "이중 피스톤 구조의 부동 라이너 기법을 활용한 피스톤 링 마찰 특성에 관한 실험적 연구". *2022 한국자동차공학회 추계학술대회*.[^d4]
- 이승현, 오세철, 김용래, 김기연, 이정우, 이승일, 민경덕. "수소 SI엔진에서의 0-D two-zone model과 공기과잉률과 점화시기에 따른 엑서지 분석". *2022 한국자동차공학회 추계학술대회*.[^d4]
- 김예빈, 김영섭, 김우재, 신석원, 이호식, 강상규, 민경덕. "시뮬레이션을 통한 작동 조건에 따른 BOP system 출력 특성에 관한 연구". *2022 한국자동차공학회 추계학술대회*.[^d4]
- 김지웅, 심재봉, 장정효, 민경덕. "수소 부족을 이용한 PEMFC 스택의 탄소 부식에 대한 실험적 연구". *2022 한국자동차공학회 추계학술대회*.[^d4]
- 심재봉, 강민수, 김지웅, 김예빈, 민경덕. "Effect of operating conditions, various properties of gas di…". *2022 한국유체공학학술대회*.[^d4]
- 김영섭, 강혜현, 김우재, 이호식, 강상규, 민경덕. "시뮬레이션을 통한 연료전지/배터리 용량 최적화 연구". *2022 한국자동차공학회 춘계학술대회*.[^d4]
- 박인상, 임동현, 민경덕. "천연가스/디젤 융합연소에 대한 압축비 및 피스톤 형상의 영향에 관한 연구". *2022 한국자동차공학회 춘계학술대회*.[^d4]
- 김우재, 김정현, 정종원, 김영섭, 민경덕, 박철수. "연소실 벽면 온도 변화에 따른 노킹의 상관관계 분석". *2022 한국자동차공학회 춘계학술대회*.[^d4]
- 박지환, 신승협, 이상열, 김민재, 최승목, 임혁, 민경덕. "연소압 센서 및 딥러닝 점화 지연 예측 모델 기반 노킹 발생 확률 예측". *2022 한국자동차공학회 춘계학술대회*.[^d4]
**2021**

- 강혜현, 김우재, 김영섭, 이호식, 강상규, 민경덕. "수소연료전기자동차의 열관리 시스템 시뮬레이션 모델 개발". *2021 한국자동차공학회 추계학술대회 및 전시회*.[^d4]
- 이승일, 김강진, 박인상, 민경덕, 우수형, 곽영홍, 이종혁, 김진순. "SI 엔진의 유동 및 점화 시스템 개선을 통한 희박 연소 한계 확장에 관한 연구". *2021 한국자동차공학회 추계학술대회 및 전시회*.[^d4]
- 문선영, 주상현, 남태우, 민경덕. "3-D CFD를 이용한 이종 연료 융합연소 특성에 대한 수치 해석적 연구". *2021 한국자동차공학회 추계학술대회 및 전시회*.[^d4]
- 오현정, 하경표, 민경덕. "피스톤 링 마찰 측정시스템 개발". *2021 한국자동차공학회 추계학술대회 및 전시회*.[^d4]
- 심재봉, 강민수, 윤지호, 민경덕. "내구성 평가 방법으로 유도된 탄소 부식이 고분자 전해질 연료 전지 성능에 미치는 영향". *2021 한국자동차공학회 추계학술대회 및 전시회*.[^d4]
- 박지환, 신승협, 이승현, 정인수, 민경덕. "딥러닝을 이용한 노킹 센서 기반 노킹 강도 예측 모델 개발". *2021 한국자동차공학회 추계학술대회 및 전시회*.[^d5]
- 김정현, 민경덕. "LES를 활용한 엔진 내 연소율 사이클 편차 원인에 대한 분석". *2021 한국자동차공학회 추계학술대회 및 전시회*.[^d5]
- 강민수, 심재봉, 민경덕. "동결/해동 프로토콜을 적용한 MEA와 GDL의 기계적열화에 관한 연구". *2021 한국자동차공학회 춘계학술대회*.[^d5]
- 이용주, 이영복, 민경덕, 이승하, 노영준. "디젤 엔진의 0D Soot 모델 개발 Part. 1: Spray 모델링". *2021 한국자동차공학회 춘계학술대회*.[^d5]
- 이영복, 이용주, 민경덕, 이승하, 노영준. "디젤 엔진의 0D Soot 모델 개발 Part. 2: Soot 모델링". *2021 한국자동차공학회 춘계학술대회*.[^d5]
- 정종원, 김우재, 김정현, 민경덕. "광학적 진단을 활용한 가솔린 직분사 인젝터의 soot 생성 계측 및 정량화". *2021 한국자동차공학회 춘계학술대회*.[^d5]
- 임동현, 신형진, 김기홍, 민경덕. "디젤/가솔린 융합 연소에서 스월 유동이 연소 특성과 배기에 미치는 영향도 파악에 관한 연구". *2021 한국자동차공학회 춘계학술대회*.[^d5]

### 국제 학회

**2025**

- Haechan Choi, Hyunjoo Kim, Kyoungdoug Min. "Modeling of Thermal Runaway Propagation in Battery Module Co…". *SAE Thermal Management Systems Symposium (SAE TMSS)*.[^c1]
- Sangyeop Lee, Cheolsoo Park, Kyoungdoug Min. "Sensitivity Analysis of Various Cooling Methods for Battery …". *SAE Thermal Management Systems Symposium (SAE TMSS)*.[^c1]
- Yebeen Kim, Jiwoong Kim, Sehyeon Kim, Sanggyu Kang, Kyoungdoug Min. "Integrated Modeling of a Fuel Cell Stack and Thermal Managem…". *European Fuel Cells and Hydrogen*.[^c1]
- Jiwoong Kim, Sehyeon Kim, Seong-Yong Woo, Sanggyu Kang, Kyoungdoug Min. "Comprehensive Insights into Water Transport Properties and D…". *EFCF 2025: European Fuel Cell Forum*.[^c1]
**2024**

- Hyunsoo Chun, Youngseop Lee, Jiwoong Kim, Jung Hyo Chang, Jin Young Kim, Kyoungdong Min. "Method for Precise Oxygen Resistance Analysis in Polymer Ele…". *PRiME 2024 : Joint International Meeting*. DOI <https://doi.org/10.1149/ma2024-02443068mtgabs>.[^c1]
- Jiwoong Kim, Sehyeon Kim, Hyunsoo Chun, Sanggyu Kang, Kyoungdoug Min. "Development of a Dynamic Model for a Shell-and-Tube Type Gas…". *PRiME 2024 : Joint International Meeting*. DOI <https://doi.org/10.1149/ma2024-02463281mtgabs>.[^c1]
- Seungil Lee, Seunghyun Lee, Seungjae Kim, Kiyeon Kim, Jeongwoo Lee, Kyoungdoug Min. "Experimental analysis of the water direct injection effects …". *THIESEL 2024 Conference on Thermo-and Fluid Dynamic Processes for clean propulsoin powerplants*.[^c1]
**2023**

- Jihwan Park, Seunghyup Shin, Sangyul Lee, Minjae Kim, Seungmok Choi, Hyuk Im, Kyoungdoug Min. "Mass Burned Fraction Prediction with 1-dimensional Convoluti…". *SAE Energy & Propulsion Conference & Exhibition*.[^c1]
**2022**

- Jaebong Sim, Jiwoong Kim, Junghyo Chang, Eunsook Lee, Jy-young Jyoung, Kyoungdoug Min. "Effects of Accelerated Stress Tests on the Durability and Pe…". *WFCC2022: World Fuel Cell Conference*.[^c1]
- Hyunjung Oh, Kyoung-Pyo Ha, Kyoungdoug Min. "Development of Piston Ring Friction Measurement System". *INSA(Institut National Des Sciences Appliquees)*.[^c1]

## 과제

수행 기간이 2021년 10월 22일–2026년 10월 22일과 겹치는 과제 25건이다. 제목, 주관 기관과 기간은 연구실 Project 게시판 표기다.[^projects1][^projects2]

- 전기차 열에너지 분석을 위한 PE 해석 모델 개발과 효율 향상 연구 (주관 기관 현대엔지비(주); 기간 2022-12-26 ~ 2023-12-25)
- 배터리시스템 성능/기능 시험법 개발과 기준 검증 프로세스 연구 (주관 기관 현대엔지비(주); 기간 2022-12-26 ~ 2023-12-25)
- 중대형 상용차용 고내구 고강성 기체확산층 기술 개발 (주관 기관 한국산업기술평가관리원; 기간 2022-01-01 ~ 2022-12-31)
- 선박 유해배출가스 감축을 위한 중소형 선박용 엔진의 저인화점 대체연료 분사시스템 개발 (주관 기관 한국산업기술평가관리원; 기간 2022-01-01 ~ 2023-03-31)
- 연료전지 시스템과 전기자동차 열관리에 개발에 관한 자문 (주관 기관 (주)테너지; 기간 2022-10-01 ~ 2023-09-30)
- 액침식 BPA 냉각유로 해석 및 예측모델 개발 (주관 기관 현대모비스(주); 기간 2022-08-01 ~ 2023-06-30)
- 연료전지 MEA/Stack 내구평가 및 분석 (주관 기관 주식회사 에픽; 기간 2022-07-25 ~ 2023-07-24)
- 전기차 1회 충전 주행거리 사후관리 방안 도출 연구 (주관 기관 한국교통안전공단; 기간 2022-07-14 ~ 2022-12-23)
- 내연차 차기 배출허용기준(유로7) 설정 적용 연구 (주관 기관 환경부; 기간 2022-06-15 ~ 2023-06-30)
- 수소버스 연료전지 하이브리드 최적화 기술개발 및 실증 (주관 기관 한국에너지기술평가원; 기간 2022-04-01 ~ 2022-12-31)
- 무탄소 수소연료 기반 직접분사식 수소엔진 원천기술 개발 (주관 기관 한국산업기술평가관리원; 기간 2022-04-01 ~ 2022-12-31)
- 전기차 열관리 시스템의 RIG 시험을 통한 설계 및 제어검증 (주관 기관 (주)테너지; 기간 2022-01-01 ~ 2022-03-31)
- 전과정평가(LCA) 기반의 자동차 환경성 분석 (주관 기관 한국자동차연구원; 기간 2021-07-07~2021-12-20)
- 연료전지 단위셀 성능평가 용역 (주관 기관 국토교통부; 기간 2021-10-08 ~ 2021-12-07)
- 연료전지 열관리 시스템의 거동분석 및 모델구축 (주관 기관 국토교통부; 기간 2021-03-01~2021-12-31)
- 선박 유해배출가스 감축을 위한 중소형 선박용 엔진의 저인화점 대체연료 분사시스템 개발 (주관 기관 산업통상자원부; 기간 2021-01-01~2021-12-31)
- 중대형 상용차용 고내구 고강성 기체확산층 개발 (주관 기관 산업통상자원부; 기간 2021-01-01~2021-12-31)
- 연료전지 시스템과 전기자동차 열관리에 개발에 관한 자문 (주관 기관 민간기관; 기간 2021-10-01~2022-09-30)
- Ammonia의 선박엔진 적용성 평가에 관한 연구 (주관 기관 민간기관; 기간 2021-08-01~2021-10-31)
- 유로7 가솔린 엔진의 연비개선을 위한 냉각시스템의 해석 검증과 차량 냉각 개선 (주관 기관 민간기관; 기간 2021-04-06~2022-02-28)
- 연소압기반제어 연소 예측 제어를 위한 연소압 신호 처리 및 노킹 예측 제어 방법 개발 (주관 기관 민간기관; 기간 2021-03-01~2022-02-28)
- 한국형 Green NCAP 평가기술 개발 기획 (주관 기관 국토교통부; 기간 2021-04-08~2022-04-07)
- 차기 HEV 린번엔진의 사이클편차 예측을 위한 LES 유동/분무 해석기술 개발 (주관 기관 민간기관; 기간 2020-09-01~2023-08-31)
- 가솔린엔진의 냉각최적화와 노킹개선 열관리 연구 (주관 기관 민간기관; 기간 2020-09-01~2021-10-29)
- 내연기관 열효율 개선 및 Heat Energy Balance에 대한 연구 (주관 기관 민간기관; 기간 2020-04-01~2022-03-31)

## 특허

교수 소개의 특허 목록에서 2022년 항목 1건이다. 연도는 누리집의 연도 구역 표기이고 날짜는 게시되어 있지 않다. pending은 출원 중이라는 누리집 표기다.[^pi]

- 2022 · Hydrophobic-treated metallic gas diffusion layer, membrane-electrode assembly and fuel cell (국가 KOREA; 상태 pending)

## 수상과 선정

연구실 News & Gallery에 게시된 수상·선정 두 건이다. 괄호의 게시일은 글이 올라온 날짜다.[^award1][^award2]

- 2022-06-16 (게시일) · 민경덕 교수, 2022학년도 훌륭한 공대교수상.
- 2022-12-16 (게시일) · 민경덕 교수, FISITA Academy of Technical Leadership 선정.

## 소식

연구실 News & Gallery의 연구 소개 글이다.[^article]

- 2024-01-05 · 자동차 동력원의 탈탄소화 연구 소개: 수소 엔진의 연소 최적화, 배터리 냉각과 열폭주 예측, 연료전지 버스의 에너지 흐름 및 내구성 연구를 소개했다.

## 연락과 위치

- 교수 사무실: 서울대학교 301동 1422호[^prof]
- 교수 전화: 02-880-1661, 팩스 02-883-0179[^prof]
- 교수 이메일: kdmin@snu.ac.kr[^prof]
- 연구실: 서울시 관악구 관악로 1 서울대학교 314동 205호·206호(우편번호 08826)[^prof][^contact]
- 연구실 전화: 02-880-7124(205호), 02-880-8363(206호), 팩스 02-874-2001[^prof][^contact]
- 연락 이메일: chang.junghyo@snu.ac.kr[^contact]
[^home]: SNU Automotive Laboratory 첫 화면. <http://snual.snu.ac.kr/> 관측일 2026-11-09.
[^prof]: 서울대학교 기계공학부 민경덕 교수 상세. <https://me.snu.ac.kr/snu__professor/%eb%af%bc%ea%b2%bd%eb%8d%95-min-kyoungdoug/> 관측일 2026-11-09.
[^pi]: SNUAL Professor, 학력·경력·특허·수상. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub1_1> 관측일 2026-11-09.
[^fuel]: SNUAL 연료전지 연구 소개. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub2_1_1> 관측일 2026-11-09.
[^engine]: SNUAL 엔진 연소 연구 소개. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub2_1_2> 관측일 2026-11-09.
[^battery]: SNUAL 배터리 연구 소개. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub2_1_3> 관측일 2026-11-09.
[^motor]: SNUAL 모터 연구 소개. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub2_1_4> 관측일 2026-11-09.
[^members1]: SNUAL Member 첫째 쪽. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub1_2> 관측일 2026-11-09.
[^members2]: SNUAL Member 둘째 쪽. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub1_2&page=2> 관측일 2026-11-09.
[^alumni]: SNUAL Alumni 첫째–일곱째 쪽. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub1_3> <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub1_3&page=2> <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub1_3&page=3> <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub1_3&page=4> <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub1_3&page=5> <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub1_3&page=6> <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub1_3&page=7> 관측일 2026-11-09.
[^pubscope]: SNUAL International Journals·Domestic Conferences·International Conferences 게시 목록. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub3_2> <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub3_3> <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub3_4> 관측일 2026-11-09.
[^projects1]: SNUAL Project 첫째 쪽. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub2_2> 관측일 2026-11-09.
[^projects2]: SNUAL Project 둘째 쪽. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub2_2&page=2> 관측일 2026-11-09.
[^article]: SNUAL, SNU innovations의 자동차 동력원 연구 소개, 게시일 2024-01-05. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub4_1&wr_id=64> 관측일 2026-11-09.
[^award1]: SNUAL, 2022학년도 훌륭한 공대교수상, 게시일 2022-06-16. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub4_1&wr_id=54> 관측일 2026-11-09.
[^award2]: SNUAL, FISITA Academy of Technical Leadership 수상, 게시일 2022-12-16. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub4_1&wr_id=57> 관측일 2026-11-09.
[^contact]: SNUAL Contact. <http://snual.snu.ac.kr/sub5_1.php> 관측일 2026-11-09.
[^j1]: SNUAL International Journals 1쪽. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub3_2> 관측일 2026-11-09.
[^j2]: SNUAL International Journals 2쪽. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub3_2&page=2> 관측일 2026-11-09.
[^j3]: SNUAL International Journals 3쪽. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub3_2&page=3> 관측일 2026-11-09.
[^j4]: SNUAL International Journals 4쪽. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub3_2&page=4> 관측일 2026-11-09.
[^j5]: SNUAL International Journals 5쪽. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub3_2&page=5> 관측일 2026-11-09.
[^d1]: SNUAL Domestic Conferences 1쪽. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub3_3> 관측일 2026-11-09.
[^d2]: SNUAL Domestic Conferences 2쪽. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub3_3&page=2> 관측일 2026-11-09.
[^d3]: SNUAL Domestic Conferences 3쪽. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub3_3&page=3> 관측일 2026-11-09.
[^d4]: SNUAL Domestic Conferences 4쪽. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub3_3&page=4> 관측일 2026-11-09.
[^d5]: SNUAL Domestic Conferences 5쪽. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub3_3&page=5> 관측일 2026-11-09.
[^c1]: SNUAL International Conferences 1쪽. <http://snual.snu.ac.kr/bbs/board.php?bo_table=sub3_4> 관측일 2026-11-09.
[^p1]: H. Chun 외, K. Min, ECS Meeting Abstracts (2024). <https://doi.org/10.1149/ma2024-02443068mtgabs> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5010685701,publication_year:2021-2026> OpenAlex 출판일 2024-11-22. 관측일 2026-11-09.
[^p2]: J. Kim 외, K. Min, ECS Meeting Abstracts (2024). <https://doi.org/10.1149/ma2024-02463281mtgabs> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5010685701,publication_year:2021-2026> OpenAlex 출판일 2024-11-22. 관측일 2026-11-09.
[^p3]: I. Park 외, K. Min, International Journal of Automotive Technology (2024). <https://doi.org/10.1007/s12239-024-00202-8> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5010685701,publication_year:2021-2026> OpenAlex 출판일 2024-12-31. 관측일 2026-11-09.
[^p4]: S. Lee 외, K. Min, International Journal of Engine Research (2025). <https://doi.org/10.1177/14680874251325311> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5010685701,publication_year:2021-2026> OpenAlex 출판일 2025-04-11. 관측일 2026-11-09.
[^p5]: S. Kim, M.-H. Lee, C.-L. Myung, K. Min, Energies (2026). <https://doi.org/10.3390/en19194657> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5010685701,publication_year:2021-2026> OpenAlex 출판일 2026-10-01. 관측일 2026-11-09.
[^p6]: S. Shin 외, K. Min, IEEE Access (2023). <https://doi.org/10.1109/access.2023.3294976> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5010685701,publication_year:2021-2026> OpenAlex 출판연도 2023. 관측일 2026-11-09.
[^p7]: J. Kim 외, K. Min, Atomization and Sprays (2022). <https://doi.org/10.1615/atomizspr.2022037224> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5010685701,publication_year:2021-2026> OpenAlex 출판연도 2022. 관측일 2026-11-09.
[^p8]: H. Choi 외, K. Min, International Journal of Automotive Technology (2025). <https://doi.org/10.1007/s12239-025-00255-3> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5010685701,publication_year:2021-2026> OpenAlex 출판일 2025-04-28. 관측일 2026-11-09.

# 원자력에너지변환 및 전력이용 연구실 (Nuclear Energy Conversion and Electrification Laboratory)

**KAIST 원자력및양자공학과 · 정용훈 교수**

- 분야: 원자력발전소 중대사고 대처(원자로 용기 밖 냉각과 임계 열유속, 격납 건물 안 에어로졸 거동과 풀 스크러빙, 중대사고 해석 코드), 선박용 소형 모듈 원자로와 피동 잔열 제거 계통, 용융염 고속로·소듐냉각고속로의 다물리 해석과 고유 안전, 원자로 계통 열수력 해석 모형
- 대분야: 에너지·환경·지구, 기계·로봇·제조
- 태그: 원자로·원자력 시스템[^p5][^p6][^p8], 열전달·열관리[^p1][^p2], 유체역학·유동[^p4], 분무·에어로졸[^p3]
- 홈페이지: 학과 교수 소개 페이지 <https://nuclear.kaist.ac.kr/people/professor.php>
- 근거와 출처: [원자력에너지변환 및 전력이용 연구실 근거 페이지](necel-sources.md)

> 원자력발전소 중대사고 때 원자로 용기 밖 냉각과 격납 건물 안 에어로졸 거동을 실험과 계산으로 연구하고, 쇄빙선용 소형 원자로와 용융염 고속로 같은 차세대 원자로의 설계와 안전 해석을 다루는 원자력및양자공학과의 연구실이다.[^deptlab][^p2][^p3][^p4][^p5][^p7]

## 무엇을 연구하나

연구실은 KAIST 원자력및양자공학과 정용훈 교수의 연구실이다. 학과 연구그룹 페이지는 「원자력발전시스템」 그룹 아래 이 연구실을 「원자력에너지변환 및 전력이용 연구실」로 적고,[^deptlab] 영문 연구그룹 페이지는 「Nuclear Power System」 그룹 아래 Nuclear Energy Conversion and Electrification Laboratory로 적는다.[^deptlaben] 학과 연구센터 페이지는 「신형 원자로 연구센터 (정용훈 교수)」를 올리고, 영문 페이지는 이를 New Reactor Research Center로 적는다.[^center][^centeren]

교수가 2021–2026년에 낸 학술지 논문 38편을 보면, 연구는 원자력발전소의 중대사고(설계에서 가정한 범위를 넘어 노심이 크게 손상되는 사고) 대처와 안전 계통, 그리고 선박용 소형 원자로와 용융염 원자로 같은 차세대 원자로의 설계·해석에 걸쳐 있다.[^cr] 끓음과 기체 주입 흐름을 재는 실험과,[^p2][^p4] 사고 해석 코드와 다물리 해석(서로 영향을 주는 여러 물리 현상을 한 계산 안에서 함께 푸는 해석)을 쓰는 계산을 함께 한다.[^p3][^p7] 논문은 네 갈래로 묶인다.

첫째 갈래는 **중대사고 때 원자로 용기 밖 냉각과 임계 열유속**이다. 노심이 녹는 사고 때 원자로 용기 바깥을 물로 식혀 녹은 노심을 용기 안에 붙잡아 두는 전략을 IVR-ERVC(In-Vessel Retention through External Reactor Vessel Cooling)라 한다.[^p1][^p2] 이전 연구들은 ERVC의 성능 한계를 임계 열유속(CHF, 표면이 끓음으로 열을 빼낼 수 있는 한계 열유속)으로 평가해 왔다.[^p2] 대표 논문에서는 질량 유속, 가열면 기울기, 압력, 국소 건도를 하나씩 따로 조절한 흐름 끓음 실험으로 증기의 움직임이 CHF 발생을 직접 일으킨다는 것을 확인했고,[^p2] 아래를 향한 가열면에서 물이 흐르며 끓을 때의 CHF를 예측하는 기계론적 모델을 액체 하층 건조 모델을 바탕으로 만들었다.[^p1] 최근 논문 목록에는 낮은 기울기의 아래를 향한 가열면에서 CHF와 증기 기포 거동을 잰 실험(International Journal of Heat and Mass Transfer, 2025), IVR-ERVC와 노심 용융물 받이(core catcher) 조건의 반기계론적 CHF 모델(International Communications in Heat and Mass Transfer, 2026), 부식되기 쉬운 재료와 산성 유체가 함께 끓음 위기에 주는 영향(International Communications in Heat and Mass Transfer, 2023), 가열기 크기·방향·표면 형상에 따른 CHF 실험 평가(International Communications in Heat and Mass Transfer, 2022), 사고 저항성 핵연료(ATF) 피복관용 양극 산화 지르코늄 합금 표면의 CHF(International Journal of Heat and Mass Transfer, 2021), 저압 수직 사각 유로의 과냉 흐름 끓음 CHF 모델(International Journal of Heat and Mass Transfer, 2021), APR1400 원자로의 중대사고에서 IVR-ERVC 조건의 원자로 용기 하부 파손 가능성 분석(Nuclear Engineering and Design, 2021), i-SMR에 IVR-ERVC 전략을 쓸 때의 열적 안전 여유 평가(Nuclear Engineering and Technology, 2026)도 있다.[^cr]

둘째 갈래는 **중대사고 해석과 격납 건물 보호**다. 격납 건물은 원자로를 둘러싸 방사성 물질이 밖으로 나가지 않게 막는 건물이다. 대표 논문에서는 중대사고 종합 해석 코드 CINEMA로 여러 구획으로 나뉜 격납 건물 실험 VANAM-M3를 계산해, 격납 건물 안의 열수력(유체의 흐름과 열 전달)과 물을 빨아들이는 에어로졸(기체 속에 떠 있는 고체·액체 입자)의 거동을 이 코드가 재현하는지 평가했다.[^p3] 또 물속 수직 노즐로 공기를 불어 넣는 실험으로, 풀 스크러빙(기체를 물웅덩이 속으로 통과시켜 기체에 섞인 입자 등을 물에 붙잡아 두는 방법)에서 기체 주입 흐름이 제트로 바뀌는 기준을 새로 제안하고 그 전이가 풀 스크러빙 효율에 주는 영향을 확인했다.[^p4] 최근 논문 목록에는 벤투리 스크러빙 노즐을 쓴 물웅덩이 속 기포 거동 실험(Nuclear Engineering and Technology, 2021), 노즐 크기가 풀 스크러빙의 에어로졸 제거에 주는 영향(Nuclear Engineering and Design, 2021), 기체 주입 유량에 따른 풀 스크러빙 실험과 해석 모델(Nuclear Engineering and Design, 2025), CINEMA 코드로 계산한 QUENCH-06 실험의 고온 연료봉 다발 거동(Annals of Nuclear Energy, 2023), 실리카겔을 쓰는 원자력발전소 감압 계통(Nuclear Engineering and Design, 2021), 상변화 물질로 격납 건물의 틈을 스스로 막는 전략(Nuclear Engineering and Design, 2023), 원자력발전소에서 여러 목적으로 입자를 자기력으로 거둬들이는 방법(Nuclear Engineering and Technology, 2021), 케이블 화염 시험 설비 주변 온도에 따른 non-Class 1E 케이블의 난연 성능(Nuclear Technology, 2022)도 있다.[^cr]

셋째 갈래는 **선박용·소형 원자로와 피동 잔열 제거 계통**이다. 대표 논문에서는 쇄빙선용 일체형 소형 모듈 원자로(SMR, 공장에서 모듈로 만들어 옮겨 설치할 수 있게 설계한 출력이 작은 원자로) KA-130을 설계하고, 출력을 바꾸는 능력과 배의 움직임을 넣은 소형 냉각재 상실 사고의 안전성을 해석했다.[^p5] 원자력 추진 선박에 쓰도록 공기 냉각과 바닷물 냉각을 함께 쓰는 작고 오래 운전할 수 있는 피동 잔열 제거 계통(PRHRS, 전원이나 사람의 조작 없이 원자로가 멈춘 뒤 남는 열을 빼내는 계통)을 설계하고, 원자로 안전 해석 코드 MARS-KS로 사고 때 거동을 해석했다.[^p6] 최근 논문 목록에는 바닷물을 최종 열 제거원으로 쓰는 PRHRS 개념 연구(International Journal of Naval Architecture and Ocean Engineering, 2024)와 여러 조건에서 그 성능을 잰 실험(Nuclear Engineering and Design, 2025), 작고 오래 운전할 수 있는 PRHRS의 변수 분석(Nuclear Technology, 2024), 원자력 쇄빙선의 핵심 기술 연구(International Journal of Naval Architecture and Ocean Engineering, 2025), 하이브리드 초소형 모듈 원자로의 원자로 용기 보조 냉각 계통 여러 형상 조사(Nuclear Engineering and Design, 2021)도 있다. 에너지 이용을 다룬 논문으로는 분산 전원용 태양·원자력 하이브리드 계통의 타당성(Energy Conversion and Management, 2021)과 담수화에 쓸 열을 내는 NDP-400의 예비 설계(Arabian Journal for Science and Engineering, 2025)가 있다.[^cr]

넷째 갈래는 **차세대 원자로의 다물리 해석과 고유 안전**이다. 대표 논문에서는 감속 반사체를 둔 초소형 용융염 고속로를 GeN-Foam과 OpenMC로 계산해, 중성자 모델과 열수력 모델이 다물리 해석 결과에 주는 영향을 체계적으로 평가했다.[^p7] 또 소듐냉각고속로(액체 소듐으로 식히고 고속 중성자로 핵분열을 이어 가는 원자로)의 냉각재 온도 계수를 개선하려고 제안된 과도 상태 안전용 부유 흡수체(FAST)가 일으키는 진동을, 기계 장치 없이 피동적으로 없애는 감쇠 FAST를 제안했다.[^p8] 최근 논문 목록에는 산화베릴륨 반사체를 둔 고속 스펙트럼 용융염 원자로의 다물리 해석(Annals of Nuclear Energy, 2025), 용융염 계통에서 녹아 있는 물질의 이동을 여러 규모로 잇는 모델링(International Journal of Heat and Mass Transfer, 2026), 개량 연소로(advanced burner reactor)에서 고유 안전성을 높이는 FAST 설계 최적화(Annals of Nuclear Energy, 2022)가 있다. 원자로 계통 열수력 해석 코드의 모형을 다듬는 논문으로는 인공 신경망으로 얻은 새 순 증기 발생 상관식으로 개선한 과냉 비등 모델(Nuclear Engineering and Technology, 2022), RELAP5/Mod3.3에 넣은 재관수 중 액적 지름 변화 모델(Nuclear Engineering and Design, 2022), 증기 응축 모사를 위한 유체 간 상사 기준의 간접 검증(Nuclear Engineering and Design, 2021), 역지 밸브의 닫힘 특성에 따른 압력 상승의 전산유체역학 해석(Annals of Nuclear Energy, 2021)이 있다.[^cr]

## 주요 연구 주제

### 1. 중대사고 때 원자로 용기 밖 냉각과 임계 열유속

아래를 향한 가열면의 흐름 끓음 CHF 실험과 액체 하층 건조 모델에 바탕을 둔 CHF 예측 모델을 다룬다(대표 논문 1, 2).[^p1][^p2]

### 2. 중대사고 해석과 격납 건물 보호

중대사고 해석 코드로 격납 건물 안의 열수력과 에어로졸 거동을 계산하고, 풀 스크러빙의 기체 주입 흐름을 실험한다(대표 논문 3, 4).[^p3][^p4]

### 3. 선박용·소형 원자로와 피동 잔열 제거 계통

쇄빙선용 소형 모듈 원자로 KA-130의 설계·안전 해석과, 공기 냉각과 바닷물 냉각을 함께 쓰는 피동 잔열 제거 계통을 다룬다(대표 논문 5, 6).[^p5][^p6]

### 4. 차세대 원자로의 다물리 해석과 고유 안전

감속 반사체를 둔 용융염 고속로의 다물리 해석과, 소듐냉각고속로의 부유 흡수체를 다룬다(대표 논문 7, 8).[^p7][^p8]

## 대표 논문

KAIST 소속으로 출판된 2021–2026년 학술지 논문 가운데 정용훈 교수가 마지막 저자인 논문을 네 연구 갈래에 두 편씩 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^cr] |
|---|---|---|---|---|
| 1 | 2025 | [Mechanistic CHF model development based on the liquid sublayer dryout model for flow boiling phenomena under IVR-ERVC conditions](https://doi.org/10.1016/j.anucene.2025.111627) · Annals of Nuclear Energy | 아래를 향한 가열면을 따라 물이 흐르며 끓을 때, 특히 원자로 용기 밖을 물로 식혀 녹은 노심을 용기 안에 붙잡아 두는 IVR-ERVC의 운전 환경에서 임계 열유속(CHF)을 예측하는 기계론적 모델을 액체 하층 건조(LSD, liquid sublayer dryout) 모델을 바탕으로 만들었다. LSD 모델로 CHF를 정확히 예측하려고 액체와 증기의 상대 속도, 증기 슬러그(길쭉하게 뭉친 증기 덩어리)의 길이, 액체 속도, 액체 하층 두께 같은 핵심 변수를 정의했고, 이 변수들을 이전 실험으로 잘 밝혀진 증기 슬러그의 움직임 관점에서 해석했다. ULPU, FIRM, MIT, KAIST의 기존 실험 결과와 비교해 모델을 검증했고, 평균 제곱근 오차 14.53%로 예측 성능이 뛰어났다.[^p1] | 1저자 Min Suk Lee, 마지막 저자 정용훈 |
| 2 | 2022 | [Flow boiling experiments for CHF evaluation under downward-facing heating including flow visualization: Effects of pressure, orientation, mass flux, and local quality](https://doi.org/10.1016/j.anucene.2022.108994) · Annals of Nuclear Energy | IVR-ERVC는 중대사고 대처 전략의 하나이고, 이전 연구들은 ERVC의 성능 한계를 CHF로 평가했다. 그러나 실험 변수를 하나씩 따로 조절하지 않아 각 변수가 CHF에 주는 영향과 변수 사이의 상호작용을 평가하는 데 한계가 있었다. 이 연구는 변수를 따로 조절해 각각의 영향을 체계적으로 평가했다. 실험 변수는 질량 유속, 가열면 기울기, 압력, 국소 건도(흐름 속 증기의 질량 비율)이고, 범위는 ERVC를 쓰는 중대사고 조건에서 정했다. 특히 이전에 활발히 다루지 않은 낮은 기울기와 가압 조건을 고려했다. 동시에 흐름을 눈으로 보는 유동 가시화로 변수 변화에 따른 증기의 생성과 움직임을 관찰해 CHF 경향을 해석했고, 변수 실험으로 증기의 움직임이 CHF 발생을 직접 일으킨다는 것을 확인했다.[^p2] | 1저자 Jun Yeong Jung, 마지막 저자 정용훈 |
| 3 | 2026 | [Analysis of thermal-hydraulic and aerosol behavior in the VANAM-M3 experiment using the CINEMA code](https://doi.org/10.1016/j.anucene.2026.112454) · Annals of Nuclear Energy | 중대사고 종합 해석 코드 CINEMA(Code for INtegrated severe accident Evaluation and MAnagement)를 여러 구획으로 나뉜 VANAM-M3 실험에 적용해, 격납 건물 안의 열수력과 흡습성(공기 중의 수분을 빨아들이는 성질) 에어로졸 거동을 함께 재현하는지 평가했다. 16개 구획, 28개 유로, 47개 열 구조물로 모델을 만들었고, 열수력은 CSPACE가, 에어로졸의 이동과 침착은 SIRIUS가 계산했다. 계산은 증기 주입과 응축 단계 전체에서 압력, 대기 온도, 공기 중 수산화나트륨(NaOH) 농도의 시간 변화를 재현했고, 자연 순환이 활발한 곳(예: R5, R7 구획과 돔)에서 잘 맞았다. 차이는 혼합이 약하고 층이 나뉜 채 남는 안쪽 구획과 고리 모양 구획에 한정됐으며, 이는 유로 형상에 대한 민감도와 일차원 완전 혼합 표현의 한계를 반영한다. 흡습성 모델로 NaOH 에어로졸의 주입 뒤 최고 농도와 침착에 따른 농도 감소를 재현했다. 시험이 끝났을 때의 질량 수지는 에어로졸 제거가 주로 바닥으로의 중력 침강으로 이루어졌고, 벽 침착은 부피 응축 아래의 확산영동(diffusiophoresis, 기체 성분의 농도 차이 때문에 그 속의 입자가 움직이는 현상)이 좌우했음을 보여 준다. CINEMA는 증기 응축과 흡습성 에어로졸이 얽힌 격납 건물 규모 상황에서 믿을 만한 예측 성능을 보였다.[^p3] | 1저자 Dong-Hun Shin, 마지막 저자 정용훈 |
| 4 | 2022 | [Observation of the jet transition at a single vertical nozzle under pool scrubbing conditions](https://doi.org/10.1016/j.anucene.2022.109041) · Annals of Nuclear Energy | 물속에 기체를 불어 넣을 때 생기는 흐름은 주입 구역에서 풀 스크러빙 효율에 크게 영향을 준다. 풀 스크러빙 연구에서 흔히 쓰던 웨버 수(유체의 관성력과 표면 장력의 비) 기준의 제트 전이 기준은 고속 기체 제트를 포함한 넓은 유량 범위를 다루지 못했다. 이 연구는 5 mm 수직 노즐로 물속 공기 주입 실험을 했다. 공기 주입 모습을 고속 카메라로 보고 섀도그래피(빛을 비춰 생긴 그림자 무늬로 흐름이나 물체의 모양을 보는 방법)로 분석했으며, 물웅덩이 중심선을 따라 국소 기공률(그 자리에서 기체가 차지하는 부피 비율)을 광섬유 탐침으로 쟀다. 측정 결과로 명목 마하 수(흐름 속도를 음속으로 나눈 값) 조건에 바탕을 둔 제트 전이 기준을 제안했고, 제염 계수(DF, 걸러 내기 전의 양을 걸러 낸 뒤의 양으로 나눈 값) 실험으로 흐름 형태의 전이가 풀 스크러빙 효율에 주는 영향을 확인했다. 제안한 전이 기준은 DF 실험 결과와 맞았다.[^p4] | 1저자 Jongwoong Yoon, 마지막 저자 정용훈 |
| 5 | 2024 | [Design and analysis of KA-130, the marine-based SMR for icebreakers](https://doi.org/10.1016/j.nucengdes.2024.113127) · Nuclear Engineering and Design | 쇄빙선용으로 설계한 일체형 소형 모듈 원자로 KA-130은 원자력 추진으로 북극 항로를 다니기 위한 탄소 배출 없는 방안이다. 일체형 원자로라 주요 1차 계통 기기가 모두 원자로 압력 용기 안에 들어 있어, 대형 냉각재 상실 사고(원자로 냉각재 계통의 큰 배관이 깨져 냉각재가 빠져나가는 사고)가 생길 수 없고 원자로 안전성이 높아진다. 부하 추종 능력(요구되는 출력의 변화에 맞춰 출력을 바꾸는 능력)을 평가해 2분 안에 효율적으로 출력을 바꿀 수 있음을 보였다. 소형 냉각재 상실 사고(SBLOCA) 안전 해석에서는 배의 움직임을 최소 임계 열유속비(MCHFR, 임계 열유속을 실제 열유속으로 나눈 값의 최솟값) 계산에 넣고 민감도 분석으로 중요한 시나리오를 찾았다. 가장 제한적인 경우는 안전 주입 배관이 완전히 끊어지고 초기 압력이 낮으며 노심 출구 온도가 높고 출력이 노심 아래쪽에 몰린 경우였다. 해석 결과 노심이 물에 잠긴 상태가 유지되고 붕괴열(핵분열 생성물이 방사성 붕괴를 하며 내는 열)이 성공적으로 제거됐으며, 규제 기준과 KA-130 고유 기준에 맞춘 허용 기준(MCHFR과 노심 위 수위 조건)을 만족했다.[^p5] | 1저자 Jihee Kim, 마지막 저자 정용훈 |
| 6 | 2023 | [Design and transient analysis of a compact and long-term-operable passive residual heat removal system](https://doi.org/10.1016/j.net.2023.08.004) · Nuclear Engineering and Technology | 원자력 선박 추진은 탄소를 내지 않는 차세대 동력원으로 떠오르고 있고, 장기 안전을 위해 알맞은 피동 잔열 제거 계통(PRHRS)이 필요하다. 바다에서는 안전 지원이 어렵고 공간이 좁아 운전 시간에 제한이 없고 작게 만들 수 있는 점이 특히 중요하다. 그래서 공기 냉각과 바닷물 냉각을 함께 쓰는 것을 핵심 설계 개념으로 하는 작고 오래 운전할 수 있는 PRHRS를 제안했고, 실현 가능성을 확인하려고 계통 설계와 사고 시나리오의 과도 해석(시간에 따라 바뀌는 상태를 따라가는 해석)을 했다. 설계 결과 바닷물 냉각이 계통 전체 크기를 크게 줄여 이 계통을 실현할 수 있음을 보였다. 과도 해석에는 MARS-KS 코드를 써서 소내 정전(발전소의 교류 전원이 모두 끊긴 상태) 조건의 계통 거동을 분석했다. 제안한 설계는 설계 요건을 충분한 여유로 만족했다. 냉각재 온도는 36시간 안에 안전 정지 조건에 이르렀고 최대 냉각률은 시간당 40 °C를 넘지 않았다. 오래 운전하면서 작게 만들려면 공기 냉각과 바닷물 냉각이 둘 다 필요하다고 평가했다.[^p6] | 1저자 Wooseong Park, 마지막 저자 정용훈 |
| 7 | 2026 | [Systematic investigation on neutronics and thermal-hydraulics model for multi-physics analysis of micro molten salt fast reactor with moderating reflector](https://doi.org/10.1016/j.net.2026.104114) · Nuclear Engineering and Technology | 용융염 고속로(MSFR, 핵연료를 녹은 염에 섞어 순환시키며 고속 중성자로 핵분열을 이어 가는 원자로)에 감속 반사체를 두면 고속 중성자(속도를 늦추지 않은 중성자)와 열중성자(감속돼 느려진 중성자) 스펙트럼의 장점을 함께 갖는 이중 스펙트럼 노심이 되지만, 국소 출력이 크게 치솟고 반사체 온도 계수(반사체 온도가 바뀔 때 핵분열 연쇄 반응의 세기가 바뀌는 비율)가 양(+)이 된다. 그 영향은 정상 상태와 과도 상태에서 거의 다뤄지지 않았다. 이를 메우려고 GeN-Foam과 OpenMC로 감속 반사체가 있는 MSFR의 다물리 거동에 중성자 모델과 열수력 모델이 주는 영향을 체계적으로 평가했다. 먼저 여러 다군 단면적(MGXS, 중성자 에너지를 여러 구간으로 나눠 구간마다 평균한 단면적. 단면적은 중성자와 원자핵이 반응할 확률을 면적으로 나타낸 값) 모델로 다군 확산 해석을 해, 30군 구조와 여러 영역 공간 균질화를 쓴 정밀 MGXS 모델이 상당히 정확한 예측을 준다는 것을 보였다. 다음으로 정상 상태 다물리 계산에서는 열수력 계산에 반사체 영역을 따로 모델링하고 정밀 MGXS 모델을 함께 쓰는 것이 정확한 계산에 꼭 필요함을 보였다. 끝으로 사고 시나리오의 과도 해석으로 계통의 기본 동특성을 살폈다. 단순 MGXS 모델은 음(-)의 온도 되먹임에 출력 반응이 늦었고, 양의 반사체 온도 계수의 효과는 짧은 기간에는 크지 않았다.[^p7] | 1저자 Wooseong Park, 마지막 저자 정용훈 |
| 8 | 2022 | [A study of the behavior of the floating absorber for safety at transient (FAST) in an innovative sodium-cooled fast reactor (iSFR)](https://doi.org/10.1016/j.anucene.2022.109364) · Annals of Nuclear Energy | 음의 반응도 되먹임(출력이나 온도가 오를 때 핵분열 연쇄 반응을 약하게 하는 성질)은 사고 때 열출력과 기기 온도의 변화를 억누르는 원자로의 가장 중요한 고유 안전 특성 가운데 하나다. 소듐냉각고속로(SFR)의 냉각재 온도 계수를 개선해 원자로 계통이 스스로 안정되도록, 과도 상태 안전용 부유 흡수체(FAST)가 제안되어 있다. 이전 연구들은 FAST가 정지 실패 예상 과도(ATWS, 예상되는 이상 상황에서 원자로 긴급 정지가 작동하지 않은 경우) 조건에서 출력 폭주와 온도 진동을 일으킨다고 보였다. 이 연구는 FAST의 거동과 진동에 영향을 주는 변수를 수식으로 설명하고, 기계 장치 없이 진동을 피동적으로 없애는 감쇠 FAST를 제안했다. 감쇠 FAST는 FAST 바닥 높이와 평형 위치의 차이가 가장 큰 높이에서 핀 지름을 줄여 감쇠비(진동이 줄어드는 정도를 나타내는 값)를 높인다. 혁신 소듐냉각고속로(iSFR)의 ATWS 조건에서 성능을 평가한 결과, 7 mm 감쇠 FAST는 보호 동작 없는 과도 과출력 사고에서 음의 반응도를 한쪽 방향으로만 넣어 진동 없이 노심 출력을 크게 낮췄다. 이전 FAST가 냉각재 끓는점에 거듭 다가가며 진동한 것과 달리, 감쇠 FAST는 냉각재 온도를 800 °C 아래로 안정되게 유지했고 다른 ATWS 사고에서도 최고 냉각재 온도를 낮췄다.[^p8] | 1저자 Seongmin Lee, 마지막 저자 정용훈 |

## 교수와 전문 분야

정용훈 교수는 KAIST에서 원자력공학 학사(1996), 원자력및양자공학 석사(1998)와 박사(2003)를 받았다.[^deptdetail] 학과 교수 소개와 연구그룹 페이지는 최종학위를 「Ph.D. (2003) KAIST」로, 직위를 교수로 적는다.[^deptprof][^deptlab] 교수 상세 창의 경력(Experience) 칸은 MIT Post-doctoral Fellow(2003-2004), KAIST Research Scientist(2003-2005), KAIST Lecturer(2005), KAIST Assistant Research Professor(2005-2007), MOST 3N (New, Nuclear, New Frontier) 연구자(2007-2009), KAIST 원자력 및 양자공학과 조교수(2007-2011)와 부교수(2011-현재), UC Berkeley 방문교수(2016-2017)를 적고, KAIST 미래형 고속로 설계 및 안전해석 WCU 사업단 단장을 「2009-현재」로 적는다.[^deptdetail] 학과 연구센터 페이지는 「신형 원자로 연구센터」 항목에 교수 이름을 함께 적는다.[^center]

교수 상세 창은 연구 분야(Research Field)를 원자력발전소 설계 및 안전해석, 원자력수소, 해수담수화, 전기자동차, 전력수송 시스템으로 적는다.[^deptdetail]

논문으로 보면 전문 분야는 원자로 열수력과 원자력 안전이며 네 갈래를 이룬다.[^cr]

- **끓음 열전달과 임계 열유속**: 중대사고 때 원자로 용기 밖 냉각 조건의 흐름 끓음 실험과 CHF 예측 모델.[^p1][^p2]
- **중대사고 해석과 격납 건물 안 에어로졸**: 중대사고 해석 코드 CINEMA의 검증과 풀 스크러빙 실험.[^p3][^p4]
- **선박용 소형 원자로와 피동 안전 계통**: 쇄빙선용 소형 모듈 원자로 설계와 공기·바닷물 냉각 피동 잔열 제거 계통.[^p5][^p6]
- **차세대 원자로의 다물리·고유 안전 해석**: 용융염 고속로의 중성자·열수력 결합 계산과 소듐냉각고속로의 부유 흡수체.[^p7][^p8]

2021–2026년 학술지 논문 38편 가운데 31편에서 교수가 마지막 저자다.[^cr]

## 응용 분야

대표 논문이 겨냥하는 응용은 원자력발전소의 중대사고 대처와 원자력 추진 선박, 차세대 원자로다. CHF 모델은 원자로 용기 밖을 식혀 녹은 노심을 용기 안에 붙잡아 두는 IVR-ERVC 조건을 대상으로 하고,[^p1] 중대사고 해석 코드 CINEMA의 검증은 격납 건물 해석에 쓰일 바탕을 마련한다.[^p3] 풀 스크러빙 실험은 물웅덩이로 기체 속 입자를 걸러 내는 효율과 이어진다.[^p4] KA-130은 원자력 추진으로 북극 항로를 다니는 쇄빙선을 위한 원자로이고,[^p5] 공기·바닷물 냉각 피동 잔열 제거 계통은 공간이 좁고 안전 지원이 어려운 바다에서 쓰는 원자력 추진 선박을 위한 것이다.[^p6] 용융염 고속로와 소듐냉각고속로 연구는 이 원자로들의 다물리 해석과 고유 안전성을 다룬다.[^p7][^p8] 최근 논문 목록에는 담수화에 쓸 열을 내는 NDP-400의 예비 설계와 분산 전원용 태양·원자력 하이브리드 계통 연구도 있다.[^cr]

## 최근 논문 목록 (2021–2026)

정용훈 교수가 저자로 참여한 2021–2026년 학술지 논문 38편이다(2026년 5편, 2025년 7편, 2024년 3편, 2023년 4편, 2022년 8편, 2021년 11편). 저자·제목·학술지 표기는 출판사가 등록한 서지를 따랐고, 연도는 서지에 적힌 출판 연도이며, 연도 안에서는 출판 연월이 늦은 논문부터 적었다(연월이 없는 논문은 그 연도의 끝에 두었다).[^cr] 38편 모두 논문 기록이 교수 소속을 KAIST로 적는다.[^oa]

**2026**

- Dong-Hun Shin, Jaehyun Ham, Sang Ho Kim, Chae Hyun Kim, Young Hee Kim, Yong Hoon Jeong. "Analysis of thermal-hydraulic and aerosol behavior in the VANAM-M3 experiment using the CINEMA code". *Annals of Nuclear Energy 236, 112454 (2026)*.
- Wooseong Park, Guanyu Su, Yong Hoon Jeong. "Integrated cross-scale modeling of dissolved phase transport in molten salt systems". *International Journal of Heat and Mass Transfer 264, 128777 (2026)*.
- Dong-Hun Shin, Sang Ho Kim, Donggun Son, Yonadan Choi, Young Hee Kim, Hyoung Suk Yu, Yong Hoon Jeong. "Assessment of thermal safety margins for the IVR-ERVC strategy of the i-SMR using the CINEMA code". *Nuclear Engineering and Technology 58, 104307 (2026)*.
- Wooseong Park, Yong Hoon Jeong. "Systematic investigation on neutronics and thermal-hydraulics model for multi-physics analysis of micro molten salt fast reactor with moderating reflector". *Nuclear Engineering and Technology 58, 104114 (2026)*.
- Min Suk Lee, Jun Yeong Jung, Yong Hoon Jeong. "Development of a semi-mechanistic liquid sublayer dryout CHF model for IVR-ERVC and core catcher systems: Parameter analysis and physical consistency assessment". *International Communications in Heat and Mass Transfer 172, 110375 (2026)*.

**2025**

- Min Suk Lee, Jun Yeong Jung, Yong Hoon Jeong. "Mechanistic CHF model development based on the liquid sublayer dryout model for flow boiling phenomena under IVR-ERVC conditions". *Annals of Nuclear Energy 222, 111627 (2025)*.
- Yong Hwan Yoo, Wooseong Park, Hagtae Kim, Kilsung Kwon, Yong Hoon Jeong, Soo Hyoung Kim. "Experimental investigation on the performance and characteristics of the seawater cooled PRHRS (SWC-PRHRS) under various conditions". *Nuclear Engineering and Design 442, 114279 (2025)*.
- Wooseong Park, Yong Hoon Jeong. "GeN-Foam and OpenMC simulation for multi-physics analysis of fast-spectrum molten salt reactor with beryllium oxide reflector". *Annals of Nuclear Energy 218, 111378 (2025)*.
- Min Suk Lee, Hyoung Suk Yu, Jun Yeong Jung, Dong Hoon Kam, Yong Hoon Jeong. "Experimental analyses of flow boiling heat transfer on downward-facing surface at low inclination: Critical heat flux and vapor bubble dynamics". *International Journal of Heat and Mass Transfer 244, 126960 (2025)*.
- Yo Han Kim, Jongwoong Yoon, Yong Hoon Jeong. "Experimental investigation of pool scrubbing with respect to gas injection flow rate and analytical model development". *Nuclear Engineering and Design 433, 113754 (2025)*.
- H. J. Jeong, J. S. Song, G. M. Lee, H. Cho, S. S. Lim, Y. Alessi, M. Albooq, J. J. Choi, Y. H. Jeong, H. Kwon. "Preliminary Design of NDP-400: Economical Heat Generation for Efficient Desalination". *Arabian Journal for Science and Engineering 50, 3617-3628 (2025)*.
- Yong Hwan Yoo, Han Koo Jeong, Jihoon Lee, Young Woo Rhee, Si Hyung Kim, Seung Youb Han, Yeongin Park, Soo Hyoung Kim, Yong Hoon Jeong, Hagtae Kim. "Study on key technologies of a nuclear-powered icebreaker". *International Journal of Naval Architecture and Ocean Engineering 17, 100703 (2025)*.

**2024**

- Wooseong Park, Yong Hwan Yoo, Kyung Jun Kang, Yong Hoon Jeong. "Parametric Analysis of the Compact and Long-Term-Operable Passive Residual Heat Removal System". *Nuclear Technology 211, 2278-2291 (2024)*.
- Jihee Kim, Hyun Woo Jeon, Soo Hyoung Kim, Yong Hoon Jeong. "Design and analysis of KA-130, the marine-based SMR for icebreakers". *Nuclear Engineering and Design 422, 113127 (2024)*.
- Yong Hwan Yoo, Han Koo Jeong, Wooseong Park, Soo Hyoung Kim, Yong Hoon Jeong. "Study on the seawater cooled PRHRS of a nuclear propulsion ship with the upper heat exchanger for driving force and the seawater heat exchanger as an ultimate heat sink". *International Journal of Naval Architecture and Ocean Engineering 16, 100588 (2024)*.

**2023**

- Wooseong Park, Yong Hwan Yoo, Kyung Jun Kang, Yong Hoon Jeong. "Design and transient analysis of a compact and long-term-operable passive residual heat removal system". *Nuclear Engineering and Technology 55, 4335-4349 (2023)*.
- Jun Yeong Jung, Min Suk Lee, Yong Hoon Jeong. "Combined effect of a corrodible material and acidic fluid on flow boiling crisis". *International Communications in Heat and Mass Transfer 143, 106717 (2023)*.
- Woonho Jeong, Donggun Son, Jaehwan Park, Yong Hoon Jeong. "Simulation of high temperature fuel rod bundle behavior during the QUENCH-06 experiment using CINEMA code". *Annals of Nuclear Energy 182, 109598 (2023)*.
- Yonadan Choi, Jun Yeong Jung, Min Suk Lee, Yong Hoon Jeong. "Preliminary study on a new self-sealing strategy for nuclear reactor containment buildings using phase change materials". *Nuclear Engineering and Design 402, 112099 (2023)*.

**2022**

- Tae Beom Lee, Yong Hoon Jeong. "Improvement of the subcooled boiling model using a new net vapor generation correlation inferred from artificial neural networks to predict the void fraction profiles in the vertical channel". *Nuclear Engineering and Technology 54, 4776-4797 (2022)*.
- Seongmin Lee, Yonghee Kim, Yonadan Choi, Yong Hoon Jeong. "A study of the behavior of the floating absorber for safety at transient (FAST) in an innovative sodium-cooled fast reactor (iSFR)". *Annals of Nuclear Energy 179, 109364 (2022)*.
- Seongmin Lee, Yong Hoon Jeong. "Inherent safety enhancement by design optimization of a floating absorber for safety at transient (FAST) in an advanced burner reactor". *Annals of Nuclear Energy 172, 109026 (2022)*.
- Ju Hyun Park, Yong Hoon Jeong. "Modeling of droplet diameter changes during reflood into RELAP5/Mod3.3". *Nuclear Engineering and Design 393, 111791 (2022)*.
- Min Suk Lee, Jun Yeong Jung, Dong Hoon Kam, Yong Hoon Jeong. "Experimental evaluations of the critical heat flux in terms of the heater dimensions, orientation, and surface morphology". *International Communications in Heat and Mass Transfer 136, 106211 (2022)*.
- Jongwoong Yoon, Yo Han Kim, Yong Hoon Jeong. "Observation of the jet transition at a single vertical nozzle under pool scrubbing conditions". *Annals of Nuclear Energy 171, 109041 (2022)*.
- Jun Yeong Jung, Min Suk Lee, Hae Min Park, Yong Hoon Jeong. "Flow boiling experiments for CHF evaluation under downward-facing heating including flow visualization: Effects of pressure, orientation, mass flux, and local quality". *Annals of Nuclear Energy 171, 108994 (2022)*.
- Youngseob Moon, Yonghoon Jeong. "Analysis on Fire-Retardant Performance of non–Class 1E Cables Depending on the Ambient Temperature Condition Surrounding the Facilities for Flame Test of Cables". *Nuclear Technology 208, 1393-1405 (2022)*.

**2021**

- Yo Han Kim, Jongwoong Yoon, Yong Hoon Jeong. "Experimental study of the nozzle size effect on aerosol removal by pool scrubbing". *Nuclear Engineering and Design 385, 111544 (2021)*.
- Dong Hoon Kam, Yong Hoon Jeong, Sung-Min Choi, Jong-Il Yun. "Magnetic withdrawal of particles for multiple purposes in nuclear power plants". *Nuclear Engineering and Technology 53, 3979-3989 (2021)*.
- Dong Hoon Kam, Yong Hoon Jeong, Sung-Min Choi, Jong-Il Yun, Min Suk Lee. "Depressurization of nuclear power plants through a silica gel-based system". *Nuclear Engineering and Design 381, 111333 (2021)*.
- Jung Hyun Song, Jun Yeong Jung, Soon Heung Chang, Yong Hoon Jeong. "Mechanistic CHF model development for subcooled flow boiling in a vertical rectangular channel under low pressure". *International Journal of Heat and Mass Transfer 174, 121328 (2021)*.
- Seongmin Lee, Young Jae Choi, Jeong Ik Lee, Yong Hoon Jeong. "Investigation of various reactor vessel auxiliary cooling system geometries for a hybrid micro modular reactor". *Nuclear Engineering and Design 379, 111239 (2021)*.
- Khalid Khasawneh, Yong Hoon Jeong. "Indirect validation of fluid-to-fluid scaling criteria for modeling steam condensation based on empirical correlations and CFD simulations". *Nuclear Engineering and Design 378, 111235 (2021)*.
- Yu Jung Choi, Dong Hoon Kam, Petros Papadopoulos, Terttaliisa Lind, Yong Hoon Jeong. "Experimental investigation on bubble behaviors in a water pool using the venturi scrubbing nozzle". *Nuclear Engineering and Technology 53, 1756-1768 (2021)*.
- Muritala Alade Amidu, Yacine Addad, Jeong Ik Lee, Dong Hoon Kam, Yong Hoon Jeong. "Investigation of the pressure vessel lower head potential failure under IVR-ERVC condition during a severe accident scenario in APR1400 reactors". *Nuclear Engineering and Design 376, 111107 (2021)*.
- Dong Hoon Kam, Hyoung Suk Yu, Yong Hoon Jeong, Yang Jeong Park, Jung Woo Kim, Sung Oh Cho. "CHF on Anodized Zirconium-based Alloy Surfaces with Protective Oxide Layers for ATF cladding". *International Journal of Heat and Mass Transfer 170, 120936 (2021)*.
- Nam-Seok Kim, Yong-Hoon Jeong. "An investigation of pressure build-up effects due to check valve’s closing characteristics using dynamic mesh techniques of CFD". *Annals of Nuclear Energy 152, 107996 (2021)*.
- In Woo Son, Yong Hoon Jeong, Young Jae Choi, Jeong Ik Lee. "Feasibility study of solar-nuclear hybrid system for distributed power source". *Energy Conversion and Management 230, 113808 (2021)*.

## 연락과 위치

- 위치: 원자력및양자공학과 N7-1 3403호(학과 교수 소개의 Office-Rm 표기)[^deptprof]
- 전화: 3826(학과 교수 소개의 Tel 표기)[^deptprof]
- 교수 이메일: jeongyh@kaist.ac.kr[^deptprof][^deptlab]
[^p1]: M. S. Lee, J. Y. Jung, Y. H. Jeong, Annals of Nuclear Energy 222, 111627 (2025). <https://doi.org/10.1016/j.anucene.2025.111627> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p2]: J. Y. Jung, M. S. Lee, H. M. Park, Y. H. Jeong, Annals of Nuclear Energy 171, 108994 (2022). <https://doi.org/10.1016/j.anucene.2022.108994> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p3]: D.-H. Shin 외, Y. H. Jeong, Annals of Nuclear Energy 236, 112454 (2026). <https://doi.org/10.1016/j.anucene.2026.112454> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p4]: J. Yoon, Y. H. Kim, Y. H. Jeong, Annals of Nuclear Energy 171, 109041 (2022). <https://doi.org/10.1016/j.anucene.2022.109041> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p5]: J. Kim, H. W. Jeon, S. H. Kim, Y. H. Jeong, Nuclear Engineering and Design 422, 113127 (2024). <https://doi.org/10.1016/j.nucengdes.2024.113127> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p6]: W. Park, Y. H. Yoo, K. J. Kang, Y. H. Jeong, Nuclear Engineering and Technology 55, 4335-4349 (2023). <https://doi.org/10.1016/j.net.2023.08.004> 초록 기준(OpenAlex 등록 초록).
[^p7]: W. Park, Y. H. Jeong, Nuclear Engineering and Technology 58, 104114 (2026). <https://doi.org/10.1016/j.net.2026.104114> 초록 기준(OpenAlex 등록 초록).
[^p8]: S. Lee, Y. Kim, Y. Choi, Y. H. Jeong, Annals of Nuclear Energy 179, 109364 (2022). <https://doi.org/10.1016/j.anucene.2022.109364> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^deptprof]: KAIST 원자력및양자공학과 교수 소개 페이지 <https://nuclear.kaist.ac.kr/people/professor.php> (정용훈 교수 항목의 최종학위, Office-Rm, Tel, Email, 2026-10-25 열람)
[^deptdetail]: KAIST 원자력및양자공학과 교수 소개 페이지 <https://nuclear.kaist.ac.kr/people/professor.php> (정용훈 교수의 Education, Experience, Research Field, 교수 상세 창, 2026-10-25 열람)
[^deptlab]: KAIST 원자력및양자공학과 연구그룹 페이지 「원자력발전시스템」 <https://nuclear.kaist.ac.kr/research/the_lap.php?category=001> (원자력에너지변환 및 전력이용 연구실, 교수 정용훈, education·email 칸, 2026-10-25 열람)
[^deptlaben]: KAIST 원자력및양자공학과 영문 연구그룹 페이지 「Nuclear Power System」 <https://nuclear.kaist.ac.kr/eng/research/the_lap.php?category=001> (Nuclear Energy Conversion and Electrification Laboratory, Professor Jeong, Yong Hoon, 2026-10-25 열람)
[^center]: KAIST 원자력및양자공학과 연구센터 페이지 <https://nuclear.kaist.ac.kr/research/researchcenter.php> (신형 원자로 연구센터 (정용훈 교수), 2026-10-25 열람)
[^centeren]: KAIST 원자력및양자공학과 영문 연구센터 페이지 <https://nuclear.kaist.ac.kr/eng/research/researchcenter.php> (New Reactor Research Center, 2026-10-25 열람)
[^cr]: Crossref 출판사 등록 서지 <https://api.crossref.org/> (교수 이름과 ORCID 0000-0001-9708-9475로 찾은 2021년 이후 학술지 논문의 저자·제목·학술지·권·쪽·출판 연월, 2026-10-25 조회)
[^oa]: OpenAlex 저자·논문 기록 <https://api.openalex.org/> (ORCID 0000-0001-9708-9475가 연결된 교수 저자 기록의 2021년 이후 논문과 논문별 교수 소속, 2026-10-25 조회)

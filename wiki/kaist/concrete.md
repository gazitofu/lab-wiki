# 콘크리트 연구실 (Research group for concrete structures, materials and construction)

**KAIST 건설및환경공학과 · 김재홍 부교수 · 데이터사이언스대학원(겸임) · AX학과(겸임)**

- 영문 이름: concrete.kaist
- 분야: 콘크리트 재료·구조·시공, 자료 기반 재료 평가, 이산화탄소를 활용하는 건설재료, 굳기 전 콘크리트의 흐름과 시공 성능[^dept][^research]
- 대분야: 건설·도시·인프라, 소재
- 태그: 과학·공학 AI[^research], 유체역학·유동[^research], 순환·지속가능 소재[^research]
- 홈페이지: <https://concrete.kaist.ac.kr>
- 근거와 출처: [콘크리트 연구실 근거 페이지](concrete-sources.md)

> 콘크리트가 잘 흐르고 원하는 모양으로 굳도록 재료의 성질과 시공 방법을 함께 연구하며, 자동 실험·인공지능과 이산화탄소 활용을 건설재료 개발에 연결한다.[^research]

## 무엇을 연구하나

이 연구실은 콘크리트(결합재에 물과 모래·자갈을 섞어 굳힌 건설재료)의 재료 성능과 구조물 시공을 함께 다룬다. 굳은 뒤 힘을 견디는 성질뿐 아니라, 굳기 전 재료가 거푸집(콘크리트를 부어 원하는 모양으로 굳히는 틀) 안으로 얼마나 잘 들어가는지도 연구한다. 학과 소개는 재료 특성, 흐름과 작업 편의성, 경제성과 환경 영향을 함께 고려하는 연구를 설명한다.[^home][^dept][^research]

첫 갈래는 자동 실험과 인공지능(Artificial Intelligence, AI)이다. 시멘트(물과 반응해 굳으며 다른 재료를 서로 묶는 분말 재료) 분산제(뭉친 입자가 흩어진 상태를 유지하도록 돕는 첨가제)의 성능을 평가하는 자동 실험을 수행하고, 건설재료의 성질에 맞는 기계학습(자료에서 규칙을 배워 예측이나 판단을 하는 계산 방법) 알고리즘을 개발한다.[^research] 연구 소개는 관측에 기반한 학습과 서로 다른 자료 환경 사이에서 배운 지식을 옮기는 학습 방법을 제시한다.[^research] 대표 논문 1은 흐름 영상을 시간 순서대로 읽는 계산 모형으로 재료의 흐름 특성을 추정한다.[^p1]

둘째 갈래는 유변학(물질이 힘을 받을 때 변형되거나 흐르는 거동을 다루는 학문)으로 시공 성능을 설명하는 연구다. 연구실은 굳기 전 콘크리트가 퍼지는 시험 결과를 항복응력(재료가 지속해서 흐르기 시작하는 데 필요한 단위 면적당 힘의 문턱)과 소성점도(흐르기 시작한 뒤 전단속도 증가에 대한 전단응력 증가의 비율)로 바꾸는 모형을 제안한다.[^research] 진동으로 콘크리트를 다질 때 틀을 채우는 과정과 콘크리트가 거푸집에 가하는 압력도 계산·실험으로 다룬다.[^p3][^p5]

셋째 갈래는 이산화탄소를 건설재료에 활용하는 연구다. 양생(재료가 굳고 성능을 얻도록 온도·수분 등의 조건을 관리하는 과정)에 쓰는 알칼리성 용액에 이산화탄소를 미리 녹이고, 그 용액으로 고로 슬래그(철을 만드는 고로에서 쇳물과 분리되는 비금속 부산물) 모르타르(시멘트 같은 결합재에 물과 잔골재를 섞은 재료)를 처리한다. 재료 내부의 탄산화(이산화탄소가 재료 성분과 반응해 탄산염을 만드는 현상)를 이용해 강도와 이산화탄소 흡수량을 함께 다루며, 표면 처리로 염화물의 침투를 줄이는 방법도 연구한다.[^research][^p4][^p7]

넷째 갈래는 산업 부산물을 재활용하는 경량 골재(콘크리트에 섞는 모래·자갈 같은 알갱이 재료인 골재 가운데 밀도가 낮은 것)다.[^research] 석탄 연소재와 준설토(물 밑에서 파낸 흙)를 가열해 만든 골재나 그대로 쓰는 석탄 연소 바닥재를 건설재료에 활용한다.[^research] 골재 내부의 빈 공간이 물을 빨아들이면 반죽의 흐름이 달라지므로, 주변 반죽과 골재 사이의 물 흡수 관계를 설명하는 물리 모형을 연구한다.[^research] 대표 논문 8은 경량 골재 콘크리트를 관으로 밀어 보낼 때의 압력과 흐름 변화를 다룬다.[^p8]

## 주요 연구 주제

### 자동 실험과 자료 기반 재료 평가

자동 실험으로 시멘트 분산제의 성능 자료를 만들고, 그 자료를 기계학습과 결합해 건설재료의 성질을 평가한다. 연구실은 분산제의 고분자(반복되는 구성 단위가 길게 연결된 분자) 구조에 따른 반응 차이를 파악하고 건설재료에 맞는 학습 방법을 개발한다고 설명한다.[^research]

### 굳기 전 콘크리트의 흐름과 시공

흐름 시험 결과로 재료 특성을 정하고, 진동을 가했을 때 틀을 채우는 과정과 큰 구조물의 거푸집 압력을 예측한다.[^research][^p3][^p5]

### 이산화탄소를 이용한 양생과 표면 처리

이산화탄소를 녹인 용액으로 재료를 양생하거나 표면을 처리해, 재료의 강도와 염화물 침투 저항을 살핀다. 수용액을 이용한 양생에서는 3일 처리 직후 강도에는 이점이 없었지만 이어 습윤 양생을 하면 28일 강도가 높아졌다고 보고한다.[^research][^p4][^p7]

### 부산물을 이용한 경량 골재

산업 부산물로 만든 골재를 콘크리트에 이용하면서 물 흡수와 흐름 특성을 연구한다. 경량화뿐 아니라 혼합과 펌프 이송 과정에서도 필요한 재료 조건을 살피는 주제다.[^research][^p8]

## 대표 논문

KAIST 재직 시기의 2021–2026년 논문 가운데 자동 실험·자료 기반 예측, 흐름과 시공, 이산화탄소 활용, 경량 골재를 다루는 8편을 골랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 저자 순서는 전체 저자 목록을 따르고 교신저자는 교수 CV의 표시를 따랐다.[^cv]

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Identifying Bingham parameters from the video of mini-slump flow or channel flow](https://doi.org/10.1617/s11527-026-03294-z) · Materials and Structures | 미니 슬럼프(반죽이 중력으로 퍼지는 정도를 재는 소형 시험)와 수로 흐름 시험의 영상을 읽어, 빙엄 모형(항복응력을 넘은 뒤 전단속도와 전단응력 사이의 관계를 직선으로 나타내는 유동 모형)의 재료 특성을 추정한다. 시간 순서가 있는 자료를 다루는 장단기 기억망(Long Short-Term Memory, LSTM)에 영상의 어느 부분을 중요하게 볼지 정하는 기능을 결합했다. 유체 흐름 계산 자료로 학습한 모형이 실제 흐름과 잘 맞는 값을 냈고, 영상의 초기 구간만으로도 두 재료 특성을 추정할 수 있어 시공 중 실시간 관찰에 활용할 가능성을 보였다.[^p1] | 1저자 In Kuk Kang, 마지막 저자 김재홍 |
| 2 | 2025 | [Yielding mechanisms and structuration of sodium silicate-activated fly ash and slag pastes: Origins of critical strains](https://doi.org/10.1016/j.conbuildmat.2025.142213) · Construction and Building Materials | 규산나트륨으로 반응을 활성화한 비산재와 고로 슬래그 반죽이 흐르기 시작하는 원인을 살폈다. 서로 다른 두 변형 문턱을 확인했으며, 작은 쪽은 반응 생성물 사이 연결이 끊어지는 현상, 큰 쪽은 미세 입자 사이 상호작용과 관련됐다. 되돌릴 수 있는 입자 뭉침은 초기 점도 회복을 돕지만, 입자 사이 연결이 되돌릴 수 없게 끊어지면 시간이 지난 뒤 점도 회복이 줄어든다고 설명했다.[^p2] | 1저자 Mohammed Fouad Alnahhal, 김재홍은 4명 중 3번째 저자 |
| 3 | 2024 | [Form pressure exerted by concrete for a large-scale structure: Its quantification and physicochemical interpretation](https://doi.org/10.1016/j.cscm.2024.e03304) · Case Studies in Construction Materials | 원전 격납 구조물의 콘크리트 시공을 고려한 실물 모형 시험에서 거푸집 옆면에 작용하는 압력을 측정했다. 콘크리트를 층별로 부을 때의 최대 압력이 온도와 굳는 시간에 따라 달라짐을 살폈다. 기존 기준의 예측식과 비교한 뒤, 콘크리트 온도에 기반한 간단한 최대 압력 예측식을 제안했다.[^p3] | 1저자 Tae Yong Shin, 마지막·교신저자 김재홍[^cv] |
| 4 | 2024 | [Surface coating method for cement-based materials to improve chloride ion penetration resistance using amine-based CO2 solvent](https://doi.org/10.1016/j.jcou.2024.102823) · Journal of CO2 Utilization | 이산화탄소를 녹인 아민계 용액으로 모르타르 표면을 처리하고 염화물 침투 저항을 평가했다. 표면 처리 전 건조 등의 조건, 처리 시기, 용액 농도가 성능에 영향을 주었다. 이른 시기에 처리한 시편이 늦게 처리한 시편보다 침투 저항이 높았고, 표면층의 확산 분석은 이산화탄소를 녹인 용액이 침투를 막는 층으로 작용함을 뒷받침했다.[^p4] | 1저자 Seong Ho Han, 마지막·교신저자 김재홍[^cv] |
| 5 | 2023 | [Flow simulation of fresh concrete accounting for vibrating compaction](https://doi.org/10.1016/j.cemconres.2023.107300) · Cement and Concrete Research | 진동으로 다지는 효과를 포함해 굳기 전 콘크리트가 틀을 채우는 과정을 계산했다. 봉 형태 진동기의 진동이 약해지는 정도를 모형화하고, 진동을 받는 콘크리트의 흐름 특성을 계산에 넣었다. 계산한 채움 형태가 실물 모형 시험 결과와 합리적으로 맞았으며, 재료의 흐름 특성과 진동 감쇠에 따른 채움 정도를 예측하는 방법을 제시했다.[^p5] | 1저자 Tae Yong Shin, 마지막·교신저자 김재홍[^cv] |
| 6 | 2023 | [Performance of CO2-Cured Alkali-Activated Slag Pastes During Curing and Exposure](https://doi.org/10.1186/s40069-022-00563-3) · International Journal of Concrete Structures and Materials | 알칼리로 반응을 활성화한 고로 슬래그 반죽에 이산화탄소 양생을 적용한 뒤, 물속 양생과 해수 노출에서 강도와 반응 생성물을 비교했다. 초기 이산화탄소 양생으로 강도를 얻었고, 이후 해수에 노출한 시편에서는 탄산칼슘이 추가로 생겨 작은 빈 공간을 채우면서 강도 감소가 관찰되지 않았다. 활성화 용액의 농도에 따라 이산화탄소가 퍼지는 정도와 초기 탄산화가 달라짐을 설명했다.[^p6] | 1저자 Yubin Jun, 마지막·교신저자 김재홍[^cv] |
| 7 | 2022 | [The use of alkaline CO2 solvent for the CO2 curing of blast-furnace slag mortar](https://doi.org/10.1016/j.conbuildmat.2022.127977) · Construction and Building Materials | 이산화탄소를 미리 녹인 알칼리성 물에 고로 슬래그 모르타르를 담가 양생하는 공정을 제안했다. 재료 전체를 감싸는 큰 가스 양생실이 필요하지 않은 방법이다. 3일 동안의 처리로 탄산화는 일어났지만 3일 강도에는 이점이 없었다. 이어 습윤 양생을 하자 추가 반응이 진행돼 28일 강도가 높아졌고, 이산화탄소 흡수량은 기존 이산화탄소 양생과 비슷한 수준이었다.[^p7] | 1저자 Seong Ho Han, 마지막·교신저자 김재홍[^cv] |
| 8 | 2022 | [Quantitative evaluation on the pumpability of lightweight aggregate concrete by a full-scale pumping test](https://doi.org/10.1016/j.cscm.2022.e01075) · Case Studies in Construction Materials | 경량 골재 콘크리트를 실제 크기의 수평 관으로 밀어 보내며 압력 분포와 반죽의 흐름·수분 변화를 측정했다. 골재의 빈 공간이 물을 흡수하고 펌프 압력이 그 흡수를 늘려 흐름을 어렵게 만드는 문제를 다뤘다. 일반 콘크리트보다 이송 효율이 떨어지는 현상을 관 벽의 윤활층 성질 저하와 연결했으며, 사전 처리 없이 펌프로 이송할 때 충분한 배합수가 필요하다고 설명했다.[^p8] | 1저자 Tae Yong Shin, 마지막·교신저자 김재홍[^cv] |

## 교수와 전문 분야

김재홍 부교수는 KAIST 건설및환경공학과에서 학사(2002), 석사(2004), 박사(2008)를 받았다. Northwestern University 박사후연구원(2008년 11월–2011년 7월), UNIST 도시환경공학부 조교수(2011년 8월–2015년 8월)·부교수(2015년 9월–2018년 2월)를 거쳐 2018년 3월부터 KAIST 건설및환경공학과 부교수로 재직하고 있다.[^dept][^cv]

2026년 7월 갱신된 CV는 KAIST 데이터사이언스대학원과 AX학과의 Affiliated Professor(겸임교수)를 함께 적는다. 2022년 1월부터 KAIST Research Center for Underground City of the Future의 Director(센터장)를 맡고 있다.[^cv]

학과 소개의 전문 분야는 건설 분야의 인공지능·자료 기반 혁신, 탄소중립을 위한 지속가능 재료, 유변학에 기반한 시공 성능 최적화, 콘크리트 구조물의 한계상태(안전성이나 사용성의 요구를 만족하지 못하기 시작하는 상태) 해석이다. 연구실의 논문에서는 재료 특성의 영상 기반 추정, 진동을 고려한 흐름 계산, 이산화탄소 양생과 표면 처리로 이어진다.[^dept][^p1][^p4][^p5][^p7]

## 응용 분야

건설재료의 품질 평가, 콘크리트의 거푸집 채움과 압력 예측, 이산화탄소를 이용한 재료 처리, 산업 부산물을 이용한 경량 건설재료가 주요 응용이다. 빌딩·교량·도로·지하구조물·해양구조물 등 콘크리트를 사용하는 사회기반시설의 재료와 시공이 연구 대상이다.[^dept][^research]

## 구성원

2026년 11월 6일 연구실 Group에 게시된 연구교수 1명, 박사과정 4명, 석사과정 5명이다. 연구 주제와 학교 이메일은 Group 표기이며, 과정 시작 연도는 같은 이름으로 적힌 교수 CV의 기록을 함께 썼다. 「대표 논문 참여」는 전체 저자 목록에서 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members][^cv] Group은 Yumi Oh와 Abdullahi Abdirahman Mohamed를 석사과정으로, Tae Hoon Han을 박사과정으로 게시하지만 교수 CV는 이들의 2026년 학위 취득을 적는다. 두 표기를 각각 그대로 두었다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Yubin Jun | 연구교수 |  | Sustainability | yubinjun@kaist.ac.kr | 6, 7 |
| Tae Hoon Han | 박사과정 |  | Durability; chloride-attack fragility | tht0817@kaist.ac.kr | 4 |
| Seung Mo Kim | 박사과정 | 2024 | Smart dynamic casting | mo7884@kaist.ac.kr |  |
| Inkuk Kang | 박사과정 | 2024 | Data science approach; automated experiment | kkkjd125@kaist.ac.kr |  |
| Kwang Min Park | 박사과정 |  | Digital fabrication | pkm7527@kaist.ac.kr |  |
| Yumi Oh | 석사과정 |  | solid-waste valorization | yoomi0303@kaist.ac.kr |  |
| Abdullahi Abdirahman Mohamed | 석사과정 |  | Magnetorheology | abdirahman_mohamed@kaist.ac.kr |  |
| Jongsu Choi | 석사과정 | 2025 | Magnetorheology | cjs990630jong@kaist.ac.kr |  |
| Jisu Han | 석사과정 | 2025 | CCUS | hanjisu@kaist.ac.kr |  |
| Byeonggeon Ahn | 석사과정 |  | rheology | abg2abg@kaist.ac.kr |  |

## 지도 학생과 학위 취득 기록

2026년 7월 갱신된 교수 CV의 Graduate Student Supervision에 적힌 22명이다. 학위 취득을 적은 18명과 학위 없이 석사과정 시작만 적은 4명이 포함된다. 이름·학위·연도·진로는 CV 표기이며, 「시작」은 과정 시작 연도다. Group의 구성원 표와 구분해 적었다.[^cv]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| MinHyeong Kim | 석사과정 (시작 2026) |  |
| Byoung Geon Ahn | 석사과정 (시작 2026) |  |
| Jongsu Choi | 석사과정 (시작 2025) |  |
| Jisu Han | 석사과정 (시작 2025) |  |
| Abdullahi Abdirahman Mohamed | 석사 (KAIST) (2026) | Abaal Construction & Drilling Ltd. |
| Yumi Oh | 석사 (KAIST) (2026) | GS Engineering & Construction Corp. |
| Sultana Afroja | 석사 (KAIST) (2025) | Louisiana State University |
| Kyuhyoung Kevin Cho | 석사 (KAIST) (2025) | HanmiGlobal Co., Ltd. |
| Gwangmin Park | 석사 (KAIST) (2025) | 박사과정, 시작 2025 |
| Seung Mo Kim | 석사 (KAIST) (2024) | 박사과정, 시작 2024 |
| Inkuk Kang | 석사 (KAIST) (2024) | 박사과정, 시작 2024 |
| Jesse Harold Hilario | 석사 (KAIST) (2023) | University of Santo Tomas |
| Meseret Hailu Tadesse | 석사 (KAIST) (2023) |  |
| Tae Hoon Han | 석사 (KAIST) (2022); 박사 (KAIST, 2026) |  |
| Dong Jin Jeong | 박사 (KAIST) (2025) |  |
| Tae Yong Shin | 박사 (KAIST) (2022) | Research Institute of Industrial Science & Technology |
| Arham Taseer | 석사 (KAIST) (2022) | Orsted Engineering and Construction |
| Seong Ho Han | 박사 (KAIST) (2022) | Missouri University of Science and Technology |
| Jin Hyun Lee | 박사 (KAIST) (2022) | Samsung C&T Corporation |
| Shestakova Yekaterina | 석사 (KAIST) (2022) | Copenhagen Offshore Partners A/S, Seoul Office |
| Byoung Il Choi | 석사 (KAIST) (2019) | Korea Shipbuilding & Offshore Engineering, Co. |
| Hye Rim Jang | 석사 (UNIST) (2014) |  |

## 학위 논문

연구실 Group의 「MS theses and PhD dissertations in the research group」에 적힌 2014–2025년 학위 논문 16건이다. Group 구성원 표와 이름이 겹치는 학위 논문도 들어 있다. 이름·학위·연도·제목·기관은 Group 표기다.[^members]

| 이름 | 학위·연도 | 학위 논문 | 학위 기관 |
|---|---|---|---|
| Kyuhyoung Cho | MS Thesis (2025) | Hydraulic reaction of refined ladle furnace slag mixed with calcium carbonate and gypsum | Korea Advanced Institute of Science and Technology |
| Afroja Sultana | MS Thesis (2025) | Experimental study on the application of aragonite and calcite in cementitious materials | Korea Advanced Institute of Science and Technology |
| Dong Jin Jeong | PhD Dissertation (2025) | Development of probabilistic assessment methodology for thermal cracking caused by cement hydration | Korea Advanced Institute of Science and Technology |
| Gwang Min Park | MS Thesis (2025) | Precast hollow member printing method utilizing rheological analysis based on vibration effect | Korea Advanced Institute of Science and Technology |
| Seung Mo Kim | MS Thesis (2024) | Preliminary experiment for precast concrete module printing utilizing for modular construction  | Korea Advanced Institute of Science and Technology |
| In Kuk Kang | MS Thesis (2024) | Domain adversarial neural network to determine unbiased Bingham parameters | Korea Advanced Institute of Science and Technology |
| Jesse Harold Hilario | MS Thesis (2023) | Enhancing the reactivity and strength of fly ash-calcium sulfoaluminate cement using gypsum modifier | Korea Advanced Institute of Science and Technology |
| Meseret Hailu Tadesse | MS Thesis (2023) | Evaluation of cracking potential of roller compacted concrete dam | Korea Advanced Institute of Science and Technology |
| Arham Taseer | MS Thesis (2023) | A rheological model using the Lagrangian finite element approach to study the flow of fresh concrete | Korea Advanced Institute of Science and Technology |
| Tae Yong Shin | PhD Dissertation (2023) | Rheological modeling and flow simulation to evaluate the filling ability of fresh concrete | Korea Advanced Institute of Science and Technology |
| Seong Ho Han | PhD Dissertation (2022) | Development of the aqueous CO2 curing and treatment for cement-based materials using CO2 solvent | Korea Advanced Institute of Science and Technology |
| Jin Hyun Lee | PhD Dissertation (2022) | Matric suction of raw materials and its effect on the fresh-state properties of cement-based materials toward 3D printing application | Korea Advanced Institute of Science and Technology |
| Yekaterina Shestakova | MS Thesis (2022) | Application of machine learning algorithms to the simplification of the performance evaluation process of cement dispersants | Korea Advanced Institute of Science and Technology |
| Tae Hoon Han | MS thesis (2022) | Chloride-attack fragility curve of reinforced concrete considering the variation of concrete’s diffusivity | Korea Advanced Institute of Science and Technology |
| Byoung Il Choi | MS Thesis (2019) | Formulation of rheological model of cement suspension considering the thixotropy and shear thinning phenomenon | Korea Advanced Institute of Science and Technology |
| Hye Rim Jang | MS Thesis (2014) | Optimized Protocol to Measure the Flow Curve of Cement Paste and Its Verification with Gravity-Induced Flow Simulation | Ulsan National Institute of Science and Technology |

## 최근 논문 목록 (2021–2026)

연구실 Publications·Research와 교수 CV에 게시된 논문 가운데 37편이다. 기존 두 쪽의 24편과 CV에서 더한 13편으로, 2022년 7편, 2023년 6편, 2024년 8편, 2025년 8편, 2026년 8편이다. 제목·저자·발표처·연도는 각 목록의 표기를 따른다.[^pubs][^research][^cv]

교수 CV의 전체 목록에는 이전 소속 시기의 논문도 있으며, 이 절은 2021–2026년 범위의 논문을 다룬다. CV에서 더한 논문의 별표는 CV가 밝힌 교신저자 표시다. 2026년 Symposium Paper 1편도 포함한다.[^cv]

**2026**

- Park, GM; Shin, TY; Kim, JH\*; "Slipform-based vertical precast concrete printing with embedded reinforcement and hollow cross sections", COMPUTERS AND CONCRETE, vol.37, no.5, pp.899~912, 2026.05; http://dx.doi.org/10.12989/cac.2026.37.5.899 [^cv]
- Jun, Y; Hilario, JHP; Cho, K; Shin, TY; Kim, JH\*; "Comparative effects of limestone and fly ash on hydration, rheology, and strength of blended cements", JOURNAL OF SUSTAINABLE CEMENT-BASED MATERIALS, vol.15, no.5, pp.1569~1581, 2026.05; http://dx.doi.org/10.1080/21650373.2025.2605154 [^cv]
- Jun, Y; Hilario, JHP; Han, SH; Kim, JH\*; "Influence of curing conditions on microstructural evolution in cement pastes: a comparative study", JOURNAL OF SUSTAINABLE CEMENT-BASED MATERIALS, vol.15, no.3, pp.1048~1058, 2026.03; http://dx.doi.org/10.1080/21650373.2025.2588316 [^cv]
- Kim, SM; Kim, JH\*; "Vibration-assisted rheological control for 3D printing of precast concrete modules", JOURNAL OF BUILDING ENGINEERING, vol.119, 2026.02; http://dx.doi.org/10.1016/j.jobe.2025.115145 [^cv]
- Shin, TY; Han, S; You, R; Jun, Y; Kim, JH\*; "Rheological modification of alkali-activated slag mortar: Roles of sodium gluconate retarder and dispersants", JOURNAL OF BUILDING ENGINEERING, vol.120, 2026.02; http://dx.doi.org/10.1016/j.jobe.2026.115592 [^cv]
- Maierdan, Y; Kang, IK; Kim, JH; Kawashima, S; "Tuning clay self-assembly for 3D printing of bio-stabilized earthen materials", MATTER, vol.9, no.2, 2026.02; http://dx.doi.org/10.1016/j.matt.2025.102522 [^cv]
- Kang, IK; Kim, JH\*; Shin, TY; Song, H; Lei, L; Kim, T; "Breaking the flow-stability trade-off: Leveraging depletion forces through amine copolymer", JOURNAL OF BUILDING ENGINEERING, vol.117, 2026.01; http://dx.doi.org/10.1016/j.jobe.2025.114847 [^cv]
- Kim, JH; Kang, IK; “Integration of Automated Experiment and Data Science for Enhanced Evaluation of Cement Dispersant Performance”, : Superplasticizers and Other Chemical Admixtures in Concrete, Symposium Paper, SP-369, pp. 1-8, 2026.07, DOI: 10.14359/51750716 [^cv]

**2025**

- Han, S; Shin, TY; Kim, SM; Kim, JH; Khayat, KH; "CO2-induced changes in rheology, structural evolution, and particle characteristics of cement paste", CEMENT & CONCRETE COMPOSITES, vol.163, 2025.10; https://doi.org/10.1016/j.cemconcomp.2025.106180
- Kim, JH; Kang, IK; Shin, TY; Park, CK; "Automated experimentation for evaluating cement dispersant performance", CEMENT AND CONCRETE RESEARCH, vol.194, 2025.08; https://doi.org/10.1016/j.cemconres.2025.107895
- Alnahhal, MF; Kim, T; Kim, JH; Hajimohammadi, A; "Yielding mechanisms and structuration of sodium silicate-activated fly ash and slag pastes: Origins of critical strains", CONSTRUCTION AND BUILDING MATERIALS, vol.489, 2025.08; https://doi.org/10.1016/j.conbuildmat.2025.142213
- Han, TH; Jun, Y; Kim, JH; "Effect of hydrates of ITZ on chloride-attack resistance in alkali-activated slag mortar", JOURNAL OF SUSTAINABLE CEMENT-BASED MATERIALS, vol.14, no.7, pp.1281~1292, 2025.07; https://doi.org/10.1080/21650373.2025.2494061
- Al Khaffaf, I; Hawileh, RA; Sahoo, S; Abdalla, JA; Kim, JH; "Toward carbon- neutral construction: A review of zero-carbon concrete", JOURNAL OF BUILDING ENGINEERING, vol.99, 2025.04; https://doi.org/10.1016/j.jobe.2024.111578
- Han, S; Kim, JH; Singh, RK; Shah, SP; "CO2 utilization for cementitious materials - A review", KSCE JOURNAL OF CIVIL ENGINEERING, vol.29, 2025.04; https://doi.org/10.1016/j.kscej.2025.100227
- Hawileh, RA; Shaw, SK; Assad, M; Dey, A; Abdalla, JA; Kim, JH; "Influence of Fly Ash on the Compressive Strength of Ultrahigh-Performance Concrete: A State-of-the-art Review Towards Sustainability", INTERNATIONAL JOURNAL OF CONCRETE STRUCTURES AND MATERIALS, vol.19, 2025.04; https://doi.org/10.1186/s40069-024-00757-x
- Kang, IK; Shin, TY; Kim, JH; "Unbiased rheological properties determined by adversarial training with Bingham equation", CEMENT & CONCRETE COMPOSITES, vol.157, 2025.03; https://doi.org/10.1016/j.cemconcomp.2025.105943

**2024**

- Han, S; Han, TH; Hilario, JHP; Kim, JH; "Pre-treatment of waste hydrated cement used for replacement of fine aggregate using amine-based CO2 solvent", JOURNAL OF BUILDING ENGINEERING, vol.97, 2024.11; https://doi.org/10.1016/j.jobe.2024.110711
- Jun, Y; Hilario, JHP; Kang, IK; Park, CK; Lee, H; Kim, JH; "Properties of cement-based materials incorporating byproduct colloidal nanosilica", CONSTRUCTION AND BUILDING MATERIALS, vol.453, 2024.11; https://doi.org/10.1016/j.conbuildmat.2024.139055
- Jun, Y; Hilario, JHP; Kim, JH; "Hydration characteristics and hydration products of calcium sulfoaluminate cement and fly ash blended pastes", JOURNAL OF SUSTAINABLE CEMENT-BASED MATERIALS, vol.13, no.10, pp.1470~1482, 2024.10; https://doi.org/10.1080/21650373.2024.2394769
- Han, SH; Kim, SM; Jun, Y; Han, TH; Kim, JH; "Carbon-captured sodium hydroxide solution for sustainable alkali-activated slag", SUSTAINABLE MATERIALS AND TECHNOLOGIES, vol.40, 2024.07; https://doi.org/10.1016/j.susmat.2024.e00915
- Shin, TY; Han, S; Lee, JH; Kim, JH; "Form pressure exerted by concrete for a large-scale structure: Its quantification and physicochemical interpretation", CASE STUDIES IN CONSTRUCTION MATERIALS, vol.20, 2024.07; https://doi.org/10.1016/j.cscm.2024.e03304
- Shin, Tae Y; Kim, JH; "Vibrorheology of fresh cement-based materials with different compaction energy", CONSTRUCTION AND BUILDING MATERIALS, vol.427, 2024.05; https://doi.org/10.1016/j.conbuildmat.2024.136228
- Jun, Y.; Han, S.H.; Kim, J.H.; "Performance of CO2-cured alkali-activated blast-furnace slag incorporating magnesium oxide", CONSTRUCTION AND BUILDING MATERIALS, vol.429, 2024.05; https://dx.doi.org/10.1016/j.conbuildmat.2024.136462
- Han, S; Han, TH; Kim, JH; "Surface coating method for cement-based materials to improve chloride ion penetration resistance using amine-based CO 2 solvent", JOURNAL OF CO2 UTILIZATION, vol.83, 2024.05; https://doi.org/10.1016/j.jcou.2024.102823

**2023**

- Kang, IK; Shin, TY; Kim, JH; "Observation-informed modeling of artificial neural networks to predict flow and bleeding of cement-based materials", CONSTRUCTION AND BUILDING MATERIALS, vol.409, 2023.12; https://doi.org/10.1016/j.conbuildmat.2023.133811
- Shin, TY; Kim, JH; "Flow simulation of fresh concrete accounting for vibrating compaction", CEMENT AND CONCRETE RESEARCH, vol.173, 2023.11; https://doi.org/10.1016/j.cemconres.2023.107300
- Jun, YB; Han, SH; Bae, YH; Kim, JH; "Seawater-mixed alkali-activated materials: a comparative investigation of metal slag suitability", JOURNAL OF SUSTAINABLE CEMENT-BASED MATERIALS, vol.12, no.7, pp.907~923, 2023.07; https://doi.org/10.1080/21650373.2022.2135039
- Han, SH; Jun, Y; Kim, JH; "The use of monoethanolamine CO2 solvent for the CO2 curing of cement-based materials", SUSTAINABLE MATERIALS AND TECHNOLOGIES, vol.35, 2023.04; https://doi.org/10.1016/j.susmat.2022.e00559
- Kim, JH; Shin, TY; Yekaterina, S; Park, CK; "Data science approach to find an outlier in the group of cement dispersants", CONSTRUCTION AND BUILDING MATERIALS, vol.368, 2023.03; https://doi.org/10.1016/j.conbuildmat.2023.130347
- Jun, Y; Han, SH; Kim, JH; "Performance of CO2-Cured Alkali-Activated Slag Pastes During Curing and Exposure", INTERNATIONAL JOURNAL OF CONCRETE STRUCTURES AND MATERIALS, vol.17, no.2, pp.345~355, 2023.01; https://dx.doi.org/10.1186/s40069-022-00563-3

**2022**

- Shin, TY; Kim, JH; "First step in modeling the flow table test to characterize the rheology of normally vibrated concrete", CEMENT AND CONCRETE RESEARCH, vol.152, 2022.02; https://doi.org/10.1016/j.cemconres.2021.106678
- Han SH, Jun Y, and Kim JH (2022), The use of alkaline CO2 solvent for the CO2 curing of blast-furnace slag mortar, Constr Build Mater 342: 127977, https://doi.org/10.1016/j.conbuildmat.2022.127977
- Lee, JH; Kim, JH\*; "Matric suction and its effect on the shape stability of 3D printed concrete", CEMENT AND CONCRETE RESEARCH, vol.159, 2022.09; http://dx.doi.org/10.1016/j.cemconres.2022.106864 [^cv]
- Kim, JH; Shin, TY; Park, CB; Park, CK; "Quantitative evaluation of energy transfer of concrete vibrator", ACI MATERIALS JOURNAL, vol.119, no.5, pp.261~268, 2022.09; http://dx.doi.org/10.14359/51735979 [^cv]
- Lee, JH; Kim, JH\*; "Matric suction of fine sand and its effect on the shape stability of 3D printed cement mortar", CONSTRUCTION AND BUILDING MATERIALS, vol.341, 2022.07; http://dx.doi.org/10.1016/j.conbuildmat.2022.127618 [^cv]
- Shin, TY; Kim, YH; Park, CB; Kim, JH\*; "Quantitative evaluation on the pumpability of lightweight aggregate concrete by a full-scale pumping test", CASE STUDIES IN CONSTRUCTION MATERIALS, vol.16, 2022.06; http://dx.doi.org/10.1016/j.cscm.2022.e01075 [^cv]
- Yoon, J; Choi, BI; Kim, JH\*; "Adsorption properties of polycarboxylate ether-based superplasticizer on cement particles and their resultant dispersion", FRONTIERS OF STRUCTURAL AND CIVIL ENGINEERING, vol.16, no.4, pp.506~514, 2022.04; http://dx.doi.org/10.1007/s11709-022-0813-5 [^cv]

## 수상과 선정

교수 CV에 적힌 기간 안 수상 4건으로 교수 수상 3건과 지도 학생 수상 1건이다. Inkuk Kang의 수상은 연도만 적혀 있고 날짜는 게시되어 있지 않다.[^cv]

- 2025 · Inkuk Kang, BK21 Best Paper Award
- 2024-04-18 · Best Paper Presentation Award (Korean Recycled Construction Resources Institute)
- 2023-02-15 · KAIST 우수강의상 (Prize for Excellence in Teaching)
- 2022-06-24 · Korea Ground Granulated Blast-Furnace Slag Association 표창 (Commendation)

## 연락과 위치

- 교수 이메일: jae.kim@kaist.ac.kr[^members][^ack]
- 교수 연구실: W1-2동 3205호, 전화 042-350-3639[^dept]
- 콘크리트 재료 분석 실험실: W1-2동 3221호[^home]
- 콘크리트 성능 평가 실험실: W1-2동 B101호[^home]

## 각주
[^home]: 연구실 첫 화면, 연구 그룹 소개·연구 관심 분야·실험실 위치. <https://concrete.kaist.ac.kr> (관측일 2026-11-06).
[^dept]: KAIST 건설및환경공학과 김재홍 교수 소개, 직위·학력·경력·전문 분야·수상·연락. <https://cee.kaist.ac.kr/boards/view/professor/75/sc_category/1> (관측일 2026-11-06).
[^research]: 연구실 Research, 자동 실험·흐름 평가·이산화탄소 활용·경량 골재 소개. <https://concrete.kaist.ac.kr/research> (관측일 2026-11-06).
[^members]: 연구실 Group, 교수·연구교수·박사과정·석사과정·학위 논문. <https://concrete.kaist.ac.kr/members> (관측일 2026-11-06).
[^pubs]: 연구실 Publications, 2023–2025년 학술지 논문 목록. <https://concrete.kaist.ac.kr/publications> (관측일 2026-11-06).
[^ack]: 연구실 Acknowledgement, 대학원 지원 안내와 교수 이메일. <https://concrete.kaist.ac.kr/projects> (관측일 2026-11-06).
[^cv]: Jae Hong Kim 교수 CV(2026년 7월 갱신), 소속·경력·수상·지도 학생·학술지 및 기타 논문. 원문 <https://docs.google.com/document/d/136t9QohXzYLp2GAh3U8HlvdfuSoBFmCbW1H3g6cYEq0/edit>, 텍스트 <https://docs.google.com/document/d/136t9QohXzYLp2GAh3U8HlvdfuSoBFmCbW1H3g6cYEq0/export?format=txt> (관측일 2026-11-06).
[^p1]: I. K. Kang, T. Y. Shin, J. H. Kim, Materials and Structures (2026). <https://doi.org/10.1617/s11527-026-03294-z> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100374308,publication_year:2021-2026> (관측일 2026-11-06).
[^p2]: M. F. Alnahhal, T. Kim, J. H. Kim, A. Hajimohammadi, Construction and Building Materials (2025). <https://doi.org/10.1016/j.conbuildmat.2025.142213> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100374308,publication_year:2021-2026> (관측일 2026-11-06).
[^p3]: T. Y. Shin, S. H. Han, J. H. Lee, J. H. Kim, Case Studies in Construction Materials (2024). <https://doi.org/10.1016/j.cscm.2024.e03304> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100374308,publication_year:2021-2026> (관측일 2026-11-06).
[^p4]: S. H. Han, T. H. Han, J. H. Kim, Journal of CO2 Utilization (2024). <https://doi.org/10.1016/j.jcou.2024.102823> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100374308,publication_year:2021-2026> (관측일 2026-11-06).
[^p5]: T. Y. Shin, J. H. Kim, Cement and Concrete Research (2023). <https://doi.org/10.1016/j.cemconres.2023.107300> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100374308,publication_year:2021-2026> (관측일 2026-11-06).
[^p6]: Y. Jun, S. H. Han, J. H. Kim, International Journal of Concrete Structures and Materials (2023). <https://doi.org/10.1186/s40069-022-00563-3> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100374308,publication_year:2021-2026> (관측일 2026-11-06).
[^p7]: S. H. Han, Y. Jun, J. H. Kim, Construction and Building Materials (2022). <https://doi.org/10.1016/j.conbuildmat.2022.127977> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100374308,publication_year:2021-2026> (관측일 2026-11-06).
[^p8]: T. Y. Shin, Y.-H. Kim, C.-B. Park, J. H. Kim, Case Studies in Construction Materials (2022). <https://doi.org/10.1016/j.cscm.2022.e01075> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100374308,publication_year:2021-2026> (관측일 2026-11-06).

# 전력시스템연구실 (Power Systems Laboratory, PSL)

**서울대학교 공과대학 전기·정보공학부 · 이규섭 부교수**

- 분야: 재생에너지 계통 연계, 직류 전력망 운용·제어, 다중 에너지 시스템, 해상풍력 제어·계통 계획
- 대분야: 전기전자·반도체·광학, 에너지·환경·지구
- 태그: 스마트 그리드·전력 관리[^research], 제어 이론·제어 공학[^research], 전력전자 변환기·전력 변환 시스템[^research]
- 홈페이지: <https://sites.google.com/view/snupsl>
- 근거와 출처: [PSL 근거 페이지](psl-sources.md)

> 재생에너지와 저장장치가 연결된 전력망을 안정적으로 제어하고, 설비의 운전과 전력 거래를 최적화하는 연구실이다.[^home][^about][^p6][^p7]

## 무엇을 연구하나

전력시스템연구실은 발전·송전·배전 설비가 연결된 전력계통을 연구한다. 태양광과 풍력처럼 발전량이 달라지는 전원이 늘어나는 상황에서 전력망을 안정적으로 운용할 방법을 찾는다. 특히 인버터(직류 전기를 교류 전기로 바꾸는 장치)를 통해 전력망에 연결되는 자원이 중심이다. 연구 소개는 전력계통이 받아들일 수 있는 재생에너지 용량을 평가하고, 재생에너지 연계를 위한 제어 방법을 개발하는 것을 목표로 밝힌다.[^home][^dept][^research]

연구 대상에는 교류(전류의 방향이 주기적으로 바뀌는 전기)와 직류(전류의 방향이 바뀌지 않는 전기)가 함께 있는 전력망이 포함된다. 고전압 직류 송전인 HVDC(High-Voltage Direct Current)와 중전압 직류 배전인 MVDC(Medium-Voltage Direct Current)를 이용해 전력전자 기반 자원을 전력망에 연결한다. Research는 수요자 측 저전압 응용부터 초고전압 응용까지 직류 전력망의 운용·제어를 연구하며, 재생에너지를 수용하는 교류·직류 혼합 전력망의 설계를 목표로 적는다.[^home][^research]

제어 연구는 직류 설비, 수소 설비, 재생에너지 발전기에 어떤 동작 지시를 줄지 정하는 일이다. 랩은 새로운 제어 방법을 소프트웨어와 실시간 시뮬레이터(실제 시간의 흐름에 맞춰 모형의 동작을 계산하는 장치)로 시험한다고 설명한다. 운용 연구에서는 설비의 조건을 최적화 문제로 표현하고, 에너지 시스템 전체의 운전 지점을 정한다.[^about]

전기뿐 아니라 수소·가스·열을 함께 다루는 다중 에너지 시스템(Multi-Energy System, MES)도 연구한다. 섹터 커플링(전기·수소·열 등 여러 에너지 부문을 변환·운용 관계로 연결하는 것) 가운데 전기와 수소의 연결에 주목하며, 특히 수소 시스템을 중심으로 MES의 종합적인 운용·제어 방법을 개발하는 것이 목표다. 또 해상풍력을 전력계통에 연결하기 위한 풍력터빈(바람의 에너지를 회전 운동으로 바꾸는 기계)의 새 제어 방법과 전력계통 계획(설비 구성과 운용 조건을 검토해 전력 공급 체계를 정하는 일) 기술을 연구한다.[^research]

최근 논문은 충전기 사이에서 정보를 교환하며 충전 전력을 정하는 분산 제어(여러 제어기가 동작 결정을 나눠 맡는 방식), 급격한 변화 뒤 전력망의 최저 주파수를 계산하는 방법, 배전망의 전압·무효전력 제어를 다룬다. 전압은 전하당 전기적 위치에너지의 차이를 나타내는 양이고, 주파수는 반복되는 변화의 단위 시간당 횟수다. 무효전력은 교류에서 전원과 설비 사이를 오가는 에너지에 대응하며 평균적인 일로 소비되는 유효전력과 구분한다.[^p1][^p2][^p3]

## 주요 연구 주제

### 재생에너지 계통 연계

재생에너지를 얼마나 전력계통에 연결할 수 있는지 평가하고, 계통의 안정을 지원하는 제어 방법을 개발한다. 연구 소개는 그리드포밍(grid-forming, 전력변환기가 교류 전압의 크기·주파수 기준을 형성하는 제어)을 그 방법의 예로 든다. 용량 평가와 제어 방법의 개발이 이 갈래의 연구 목표다.[^research]

관련 논문에서는 빠른 주파수 응답 자원(Fast Frequency Response Resource, FFRR)이 주로 쓰이는 계통에서 큰 변화 뒤 주파수가 어디까지 떨어지는지 추정한다. 내부 제어 방식이 공개되지 않은 장치의 응답을 근사하고, 제주 계통 사례에서 계산 결과를 시험했다.[^p2] 또 인버터 기반 자원(Inverter-Based Resource, IBR) 사이의 상호작용을 고려한 계통 강도 제약을 발전기 기동정지계획에 넣는 방법을 제안했다.[^p4]

### 직류 전력망

직류 전력망의 운용과 제어를 수요자 측 저전압 응용부터 초고전압 응용까지 다룬다. 목표는 재생에너지를 수용하는 미래 교류·직류 혼합 전력망을 설계하는 것이다.[^research] 중전압 직류 전기차 충전소를 다룬 논문에서는 여러 충전기가 서로 정보를 교환해 각자의 충전 전력을 결정하는 방법을 제안했다. 배터리의 충전 상태와 차량의 체류 시간을 고려하면서 충전기 전체의 전력 합계가 충전소 정격 용량을 넘지 않도록 한다. 정격 용량은 설비가 정해진 조건에서 처리하도록 정한 용량이다.[^p1]

배전망의 전력 흐름을 나타내는 식을 반복해서 선형화하고, 전력 손실과 전압 추정값을 갱신하면서 전압·무효전력 제어 문제를 푼다.[^p3] 다른 연구에서는 배전망의 여러 스위치를 어떤 순서로 조작할지 강화학습(행동의 결과로 받는 보상을 바탕으로 행동 방식을 배우는 방법)으로 정한다. 여러 스위치의 동시 변경과 실제 개별 조작의 차이를 운용 문제에 반영하고, 사례 시험에서 순차 조작에 따른 정전·전압 불안정·선로 과부하를 다뤘다.[^p5]

### 다중 에너지 시스템

수소 시스템에 초점을 두고 전기·가스·열 등 여러 에너지 형태를 함께 다루는 시스템의 운용·제어를 연구한다. 수전해 장치(전기를 써서 물을 수소와 산소로 분해하는 장치)와 연료전지(연료가 전자를 내놓고 다른 물질이 그 전자를 받는 반응으로 전기를 생산하는 장치)를 통해 전기·수소망을 연결하고, 두 망을 협조적으로 운용·제어하는 관계를 설명한다. 여기서 전자는 음의 전하를 띠는 기본 입자다. 연구 목표는 MES를 위한 종합적인 운용·제어 방법의 개발이다.[^research]

전력 자원의 운용 논문에서는 태양광·풍력을 묶어 거래하는 가상발전소(Virtual Power Plant, VPP)의 수익을 높일 입찰가격을 다항 회귀로 추정한다. 제주 전력계통 모형과 전력시장 모형을 연결해 입찰 전략을 평가했다.[^p6] 태양광 발전과 에너지저장장치(Energy Storage System, ESS)를 함께 운영하는 연구에서는 한국의 전력 정산 규칙과 발전량 예측 오차를 고려해 운전 일정을 정하고, 상용 시험 설비에서 검증했다.[^p7]

### 해상풍력

해상풍력을 전력계통에 통합하는 기술을 연구한다. 해상풍력용 풍력터빈의 새 제어 방법과 전력계통 계획 기술을 개발하는 것이 목표다. 연구 소개는 풍력터빈 제어와 송전망에 연결할 때의 전력계통 계획을 두 과제로 구분한다.[^research]

## 대표 논문

2021–2026년 목록 가운데 이규섭 교수의 서울대 부임(2024년 3월) 뒤 논문 7편을 골랐다. 직류 충전 제어, 계통 안정도, 배전망 최적화, 시장·저장 운용을 고르게 포함한다. 연도는 누리집의 출판 연도이고, ‘쉽게 말하면’ 칸은 ResearchGate 등록 초록만을 근거로 썼다.[^faculty][^pubs]

| 번호 | 연도 | 논문 · 게재처 | 쉽게 말하면 | 이규섭 교수의 저자 위치 |
|---|---|---|---|---|
| 1 | 2026 | [Distributed Optimal Charging Strategy of MVDC Electric Vehicle Ultra-Fast Charging Station to Manage Peak Load and Consumer Convenience](https://doi.org/10.1109/TTE.2026.3678287) · IEEE Transactions on Transportation Electrification | 여러 충전기가 정보를 나눠 각 차량의 충전 전력을 결정한다. 충전 상태가 낮고 체류 시간이 짧은 차량을 우선하면서 충전소의 전체 용량을 지킨다. 제어 모형의 안정도를 분석하고 시뮬레이션으로 중앙 집중 방식과 비슷한 성능을 확인했다.[^p1] | 마지막 저자 |
| 2 | 2026 | [An Analytic Method for Frequency Nadir Estimation in Fast Frequency Response Resource (FFRR) Dominant Power Systems](https://doi.org/10.1109/TPWRD.2026.3662444) · IEEE Transactions on Power Delivery | 내부 제어가 공개되지 않거나 복잡한 자원의 주파수 응답을 근사해, 큰 변화 뒤 주파수의 최저값을 계산한다. 제주 전력계통과 고전압 직류 설비 모형으로 시험했고, 초록은 전력계통 해석 소프트웨어 PSS/E의 결과와 거의 같은 예측을 보고한다.[^p2] | 마지막 저자 |
| 3 | 2026 | [Iterative Linear Programming-Based Angle-Relaxed Branch Flow Model and Its Application to Volt-Var Control](https://doi.org/10.1109/TSG.2025.3618926) · IEEE Transactions on Smart Grid | 배전망의 전력 흐름을 나타내는 식을 선형 문제로 바꿔 반복해서 푼다. 매 단계에서 손실과 전압 추정값을 갱신한다. 수학적 분석과 수치 시험으로 계산을 반복할 때 결과가 원래 교류 전력 흐름 식의 답에 가까워지는지 확인하고, 전압·무효전력 제어에 적용했다.[^p3] | 마지막 저자 |
| 4 | 2025 | [Strength-constrained unit commitment in IBR dominant power systems](https://doi.org/10.23919/IEN.2025.0011) · iEnergy | 인버터로 연결되는 전원이 많은 계통에서, 여러 전원 사이의 영향을 반영한 계통 강도 조건을 발전기 운전 계획에 넣는다. 원래의 비선형 문제를 혼합정수선형계획(정수 선택과 연속적인 값을 선형 식으로 함께 다루는 최적화)으로 바꿔 시험 계통과 수정한 한국 계통에서 평가했다.[^p4] | 마지막 저자 |
| 5 | 2025 | [Sequential Control of Individual Switches for Real-Time Distribution Network Reconfiguration Using Deep Reinforcement Learning](https://doi.org/10.1109/TSG.2025.3580063) · IEEE Transactions on Smart Grid | 배전망 연결 구조를 바꾸는 스위치를 개별적으로 조작할 순서까지 정한다. 강화학습의 학습 환경에 스위치 조작 조건과 망 연결 조건을 넣었다. 사례 시험에서 조작 순서를 최적화해 부분 정전, 전압 불안정과 선로 과부하를 방지하는 결과를 제시했다.[^p5] | 5명 중 3번째 |
| 6 | 2025 | Data-Driven Optimal Bidding Algorithm for VPP Using Polynomial Regression Model: Actual Case Study of Jeju Island · IEEE Access | 태양광·풍력 기반 가상발전소가 한국 전력시장에서 수익을 높이도록 입찰가격을 계산한다. 입찰가격과 수익 사이의 관계를 다항식으로 맞춰 최적값에 가까운 가격을 추정한다. 시뮬레이션에서 격자 탐색 방식과 수익 성능을 비교하고 계산 부담을 줄였다.[^p6] | 마지막 저자 |
| 7 | 2025 | Optimal Scheduling and Commercial Testbed-Based Verification of Integrated PV-ESS Systems Considering Settlement Rules in South Korea · IEEE Transactions on Sustainable Energy | 태양광과 저장장치의 운전 일정을 한국의 전력 정산 규칙에 맞춰 정한다. 예측 오차에 대응하는 최적화와 재계획을 함께 쓴다. 상용 시험 설비의 시뮬레이션과 실험에서 기존 규칙 기반 알고리즘보다 수익이 9.3% 증가했다고 보고한다.[^p7] | 6명 중 2번째 |

## 교수와 전문 분야

이규섭 교수는 서울대학교에서 2013년 학사, 2020년 박사 학위를 받았다. 2020년 3월–2021년 8월 서울대학교 전력연구소 선임연구원, 2021년 9월–2024년 2월 한국에너지공과대학교(KENTECH) 에너지공학부 조교수를 거쳐 2024년 3월 서울대학교에 부임했다. 학과 교수 소개의 현재 머리 표기는 부교수다.[^faculty]

학과가 적은 전공은 전력계통, 전력계통안정도, 직류 전력망, 멀티에너지시스템이다.[^faculty] 최근 논문으로 보면 전력망 제어기의 안정도 해석, 전력 흐름을 계산하는 모형과 최적화, 재생에너지·저장장치의 경제적 운용을 연결하는 것이 전문 분야다.[^p1][^p2][^p3][^p4][^p6][^p7]

## 응용 분야

중전압 직류 전기차 충전소, 재생에너지 연계 전력망, 배전망 스위치 운용, 가상발전소 입찰, 태양광·저장장치의 운전 일정에 적용한다.[^p1][^p4][^p5][^p6][^p7] 랩은 한국전력공사(KEPCO), 한국전기연구원(KERI), 전력거래소(KPX)를 포함한 여러 협력 기관과 함께 일하고 있다고 밝힌다.[^home]

## 구성원

2026년 10월 26일 누리집의 Researcher와 Student에 게시된 비PI 22명이다. 연구교수 1명, 박사후연구원 1명, 석박사통합과정 3명, 박사과정 9명, 석사과정 6명, 방문 학생 2명이다. 시작은 현재 소속·과정에 붙은 연도이고, 주제는 게시된 연구 관련 문구다.[^researcher][^student] ‘대표 논문 참여’는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Jae-Yeop Jung | 연구교수 | 2024 | Power System Stability, Inertia Estimation, Grid Strength Evaluation | 2 |
| Seung-Chan Jo | 박사후연구원 | 2024 | Distribution Network Management, Machine Learning | 3, 5 |
| Jeong-Gyu Seo | 석박사통합과정 | 2018 | AC/DC hybrid power grid including HVDC systems; optimization formulation to maximize capacity of renewable energy into transmission systems |  |
| Jae-Myung Hong | 석박사통합과정 | 2021 | optimization formulation of hybrid AC/DC hybrid networks |  |
| Ji-Min Lee | 박사과정 | 2024 | power systems and wind power integration technology |  |
| Seong-Cheon Cho | 박사과정 | 2024 | DC grids; MVDC control structure and distributed communication | 1 |
| Yun-Chae Na | 박사과정 | 2024 | fault calculation and protection of VSC-based DC grid |  |
| Seong-Jeon Lee | 박사과정 | 2024 | GFM-based integration of RESs and inertia emulation using wind farms |  |
| Seo-Rin Yoo | 박사과정 | 2025 | Inverter-Based Resource (IBR) in the form of a black box through an impedance-based method |  |
| Jing Cui | 박사과정 | 2025 | stable and efficient integration of offshore wind energy |  |
| Seyon Kim | 석박사통합과정 | 2024 | integrating RES and EV into grid; sustainable grid systems |  |
| Su-Won Ryu | 박사과정 | 2026 | renewable energy and grid reliability | 6 |
| Gi-Hwan Yoon | 박사과정 | 2026 | VPP and DERMS; frequency/voltage stability, load transient analysis, sub-synchronous oscillations; grid stability challenges posed by large-scale AI datacenter loads |  |
| Junhwa Ra | 박사과정 | 2026 | ADMS-based real-time operation; DER/ESS coordination; flexibility markets at the distribution level; distribution-level ESS deployment; renewable curtailment under network constraints; Dynamic Operating Envelope (DOE)-based control; Non-Wires Alternatives (NWA); data-driven grid operation using digital twins and AI |  |
| Jun-Seok Park | 석사과정 | 2024 | power systems; interested in AI and/or DR for future research, but nothing has been decided yet |  |
| Joon-Young Lee | 석사과정 | 2024 | rapidly changing power system market driven by distributed energy |  |
| Gajin Kim | 석사과정 | 2025 | applying deep learning and reinforcement learning to power systems |  |
| Dahyun Jung | 석사과정 | 2026 | how wind farms and ESS can be effectively integrated into power systems |  |
| Junyeong Hwang | 석사과정 | 2026 | DC grid technologies; efficient power systems for future energy networks |  |
| Donggyun Kim | 석사과정 | 2026 | overall power systems; system optimization |  |
| Jinzhu Yu | 방문 학생 | 2025 | control of nonlinear uncertain systems; distributed coordination in multi-agent systems; control and optimization of AC/DC microgrids |  |
| Fang Daohong | 방문 학생 | 2025 | Electric Vehicle-Grid Integration; power ancillary service markets; deep reinforcement learning algorithms for energy scheduling and grid optimization |  |

## 졸업생 진로

Alumni의 박사 1명과 석사 3명이다. 학위·연도·진로는 누리집 표기다. 연구실은 2024년 3월 KENTECH의 ESCO 연구실에서 서울대 PSL로 이전했으며, 이 목록은 이전 소속에서 이어진 연구실 이력도 함께 담는다.[^alumni][^news]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Seok-Young Lee | Ph.D (2024) | Senior Researcher at Samsung Electronics |
| Jin-Ho Choi | Master (2025) | Researcher at SNUPSL |
| Su-Won Ryu | Master (2025) | Manager at KPX |
| Hae-Min Ju | Master (2024) | Researcher at Hyosung |

## 최근 논문 목록 (2021–2026)

Publication의 33편 가운데 출판 연도 2021–2026년의 25편이다. 2021년 논문은 그 해 전체를 포함한다. 이규섭 교수의 서울대 부임은 2024년 3월이므로 그 이전 소속 시기의 논문도 포함된다. 제목·저자·게재처는 누리집 표기이며, 별표는 뜻을 풀이하지 않고 누리집 표시로 남겼다.[^pubs][^faculty]

**2026**

- Seong-Cheon Cho, Jae-Won Chang, and Gyu-Sub Lee\*. "Distributed Optimal Charging Strategy of MVDC Electric Vehicle Ultra-fast Charging Station to Manage Peak Load and Consumer Convenience". *IEEE Transactions on Transportation Electrification, vol. 12, no. 4, pp. 6998-7012*.
- Seungchan Jo, Jae-Young Oh, and Gyu-Sub Lee\*. "A Successive Linear Linear/Convex Programming Framework under a Voltage-Current Representation for Loss-Minimizing Optimal Power Flow". *International Journal of Electrical Power & Energy Systems, vol. 179, 112000*.
- Yunchae Na, Gyeong-Hun Kim, Jin-Hong Jeon, Wookwon Kim, Juyong Kim, and Gyu-Sub Lee\*. "Fault Current Calculation of Medium-Voltage Hybrid AC/DC Distribution Networks: Presenting a Comprehensive Approach". *IEEE Power and Energy Magazine*.
- Jaeyeop Jung, Jeonghoo Park, Jin-Ho Choi, and Gyu-Sub Lee\*. "An Analytic Method for Frequency Nadir Estimation in Fast Frequency Response Resource (FFRR) Dominant Power Systems". *IEEE Transactions on Power Delivery*.
- Jae-Sung Lim, Sung-Wook Lee, Do-Hoon, Kwon, Gyu-Sub Lee, and S eung-Ill Moon. "Data-driven Three-step Optimal Frequency Scheme for Alleviating Grid Frequency Regulation in MT-HVDC Linked Grids". *International Journal of Electrical Power & Energy Systems, vol. 176, 111747*.
- Seungchan Jo, Jae-Young Oh, Gyu-Sub Lee\*. "Iterative Linear Programming-based Angle-Relaxed Branch Power Flow Model and Its Application to Volt-Var Control". *IEEE Transactions on Smart Grid*.

**2025**

- Seorin Yoo, Yunchae Na, Seong-Jeon Lee, Seungchan Jo, Gyu-Sub Lee\*. "Aggregation Modeling of VSCs Based on Parameter Identification for Power Systems with High Renewable Penetration". *IEEE Access*.
- Su-Won Ryu, Seung-Il Moon, Gyu-Sub Lee\*. "Data-driven Optimal Bidding Algorithm for VPP Using Polynomial Regression Model: Actual Case Study of Jeju Island". *IEEE Access*.
- Jae-Young Oh, Seokhwa Oh, Gyu-Sub Lee, Yong Tae Yoon, Seungchang Jo. "Sequential Control of Individual Swithches for Real-time Distribution Network Reconfiguration Using Deep Reinforcement Learning". *IEEE Transactions on Smart Grid, vol. 16, no. 5, pp. 3666-3683*.
- Hyunkyeong Hwang, Ah-Yun Yoon, Gyu-Sub Lee, Seung-Il Moon. "Evaluating demand flexibility of commercial building HVAC systems in South Korea". *International Journal of Electrical Power & Energy Systems, vol. 169, 110769*.
- Jae-Sung Lim, Haesong Cho, Do-Hoon Kwon, Gyu-Sub Lee. "Bi-LSTM based fault diagnosis scheme having high accuracy for Medium-Voltage Direct Current systems using pre-and post-processing". *International Journal of Electrical Power & Energy Systems, vol. 169, 110793*.
- Yong-Kyu Kim, Sang-Ho Lee, Gyu-Sub Lee\*. "Strength-constrained Unit Commitment in IBR Dominant Power Systems". *iEnergy, vol. 4, no. 2, pp. 121-131*.
- Rae-Kyun Kim, Gyu-Sub Lee, Jae-Gyun Park, Hyoseop Lee, Seung-Il Moon, and Jae-Won Chang. "Optimal Scheduling and Commercial Testbed-based Verification of Integrated PV-ESS Systems Considering Settlement Rules in South Korea". *IEEE Transactions on Sustainable Energy, vol. 16, no. 2, pp. 1372-1387*.

**2024**

- Lismer Andres Caceres-Najarro, Joonsung Jung, Yonggeon Lee, Seorin Yoom Nuhammad Salman, Jip Ki m, Gyu-Sub Lee\*, and Youngtae Noh. "Towards Energy Independence at KENTECH: A Comprehensive Microgrid Implementation Roadmap". *Heliyon, vol. 10, no. 21, pp. 1-32*.

**2023**

- Seok-Young Lee, Gyu-Sub Lee\*, Seung-Il Moon, and Yong-Tae Yoon. "Optimization of Iron and Steel Manufacturing Plant Considering Electricity Price Tariff and Electric Arc Furnace Control". *IET Generation, Transmission, and Distribution, pp. 1-14*.
- Jae-Won Chang, Gyu-Sub Lee\*, and Seaseung Oh. "Bus Impedance Matrix Estimation Using Non-PMU Measurements". *IEEE Transactions on Power Systems, vol. 38, no. 2, pp. 1743-1746*.
- Gyu-Sub Lee, Do-Hoon Kwon, Yong-Kyu Kim, and Seung-Il Moon. "A New Communication-free Grid Frequency and AC Voltage Control of Hybrid LCC-VSC-HVDC Systems for Offshore Wind Farm Integration". *IEEE Transactions on Power Systems, vol. 38, no. 2, pp. 1309-1321*.
- Jae-Won Chang, Suyong Chae, and Gyu-Sub Lee\*. "Distributed Optimal Power Sharing Strategy in an Islanded Hybrid AC/DC Microgrid to Improve Efficiency". *IEEE Transactions on Power Delivery, vol. 38, no. 1, pp. 724-737*.

**2022**

- Yong-Kyu Kim, Gyu-Sub Lee\*, Jong-Su Yoon, and Seung-Il Moon. "Evaluation for Maximum Allowable Capacity of Renewable Energy Source Considering AC System Strength Measures". *IEEE Transactions on Sustainable Energy, vol. 13, no. 2, pp. 1123-1134*.
- Yong-K yu Kim, Gyu-Sub Lee\*, Chan-Ki Kim, and Seung-Il Moon. "A n Improved AC System Strength Measure for Evaluation of Power Stability and Temporary Overvoltage in Hybrid Multi-infeed HVDC Systems". *IEEE Transactions on Power Delivery, vol. 37, no. 1, pp. 638-649*.

**2021**

- Jae-Won Chang, Gyu-Sub Lee, Pyeong-Ik H wang, and Seung-Il Moon. "A Novel Distributed Control Method for Interlinking Converters in an Islanded Hybrid AC/DC Microgrid". *IEEE Transactions on Smart Grid, vol. 12, no. 5, pp. 3765-3779*.
- Gyu-Sub Lee, Pyeong-Ik Hwang, and Seung-Il Moon. "Reactive Power Control of Hybrid Multi-terminal HVDC Systems Considering the Interaction Between the AC Network and Multiple LCCs". *IEEE Transactions on Power Systems, vol. 36, no. 5, pp. 4562-4574*.
- Gyu-Sub Lee, Do-Hoon Kwon, and Seung-Il Moon. "DC Current and Voltage Droop Control Method of Hybrid HVDC Systems for an Offshore Wind Farm Connection to Enhance AC Voltage Stability". *IEEE Transactions on Energy Conversion, vol. 36, no. 1, pp. 468-479*.
- Chun-Kwon Lee, Gyu-Sub Lee, and Seung-Jin Chang. "Solution to Fault of Multi-terminal DC Transmission Systems based on High Temperature Superconducting DC Cables". *E nergies, vol. 14, no. 1292*.
- Seong-Yoon Song, Chang-Hee Han, Gyu-Sub Lee, R. McCann, and Gil-Soo Jang. "Voltage-sensitivity-approach-based Adaptive Droop Control Strategy of Hybrid STATCOM". *IEEE Transactions on Power Systems, vol. 36, no. 1, pp. 389-401*.

## 과제

Project의 진행 과제 15건과 종료 과제 28건, 합계 43건이다. 기간은 누리집이 게시한 시작·종료 연월과 단계 표기를 유지했으며, 2021-10-22–2026-10-22에 시작 또는 종료 연월이 걸리는 항목이다. 2021년 9월에 시작한 2건은 종료 연월이 기간 안이다. 이규섭 교수의 서울대 부임(2024년 3월) 전 시작한 이전 소속 시기의 과제도 포함된다. 진행·종료 구획은 누리집 분류로, 현재 진행 여부를 기간에서 다시 추정한 것이 아니다.[^projects][^faculty]

- AI/SW Integrated HVDC Power Systems Energy Innovation Research Center (역할 Principal Investigator; 지원 KETEP; 기간 04.2026-12.2026, 1st Stage)
- Hierarchical Control of Multi-Terminal HVDC Systems Using Distortion-free Power-Line-Based Communication (역할 Principal Investigator; 지원 NRF; 기간 03.2026-02.2031)
- International P-HILS Research Platform for Fundamental Technology Development of Future Power Systems (역할 Participating Researcher; 지원 SNU; 기간 02.2026-01.2027)
- Large-scale ESS Modeling for Grid Impact Analysis (역할 Principal Investigator; 지원 HD Hynudai; 기간 02.2026-12.2026)
- Research on Grid Connection Technology for the Seonamhae Offshore Wind Project (역할 Principal Investigator; 지원 Yooshin; 기간 10.2025-09.2027)
- Cultivating Global Experts for Leadership in Electronic Power Grid Technology (역할 Principal Investigator; 지원 KETEP; 기간 10.2025-09.2026; 협력 기관 Chung-Ang University (Prof. Jae-Won Chang))
- Research on Grid Code and Criteria Considering Future Power System Change (역할 Principal Investigator; 지원 KEPRI; 기간 09.2025-08.2027; 협력 기관 Korea University (Prof. Gilsoo Jang), Yonsei University (Prof. Kyeon Hur), and KENTECH (Prof. Jip Kim))
- Developing an Optimal Energy Plan for Semiconductor Fabs Considering the Future Energy Policy and Grid Stability (역할 Principal Investigator; 지원 Samsung Electronics; 기간 09.2025-02.2028)
- Development of Advanced Power System Stability Analysis for Expanding DC Transmission and Distribution Systems (역할 Participating Researcher; 지원 KETEP; 기간 04.2025-03.2029; 협력 기관 KERI)
- Power System Stability Analysis Solution for Integrated Operation of Distributed Energy Resources (역할 Principal Investigator; 지원 KIER; 기간 01.2025-10.2026)
- Development of WAMAC Technology (역할 Participating Researcher; 지원 KEPRI; 기간 01.2025-10.2027; 협력 기관 Kwangwoon University (Prof. Minhan Yoon) and Korea University (Prof. Gilsoo Jang))
- Distributed Control Technology for DC Local Grids (역할 Principal Investigator; 지원 KETI; 기간 05.2025-08.2026)
- (Engineering Research Center, ERC) Resilient Autonomous Grid Research Center (역할 Participating Researcher; 지원 NRF; 기간 06.2023-02.2030; 협력 기관 Korea University (Prof. Gilsoo Jang))
- Development of Grid-connected Operation and Control Techniques of Fuel cell and Water Electrolysis for Power Grid Stabilization (역할 Participating Researcher; 지원 KETEP; 기간 04.2023-12.2026; 협력 기관 KIER)
- Development and Demonstration of Community Energy Management System (CEMS) for Demand-Based Energy Efficiency (역할 Participating Researcher; 지원 KETEP; 기간 04.2023-12.2026; 협력 기관 GS E&C)
- Research on the Grid Connection Infrastructure of Retired Coal Power Plants (역할 Principal Investigator; 지원 KEPCO; 기간 02.2026-03.2026)
- Stability Assessment Technology of VSC-based MTDC/AC Systems (역할 Participating Researcher; 지원 KEPRI; 기간 08.2023-05.2026; 협력 기관 Kyungpook National University (Prof. Jaejung Jung))
- Roadmap for Future Power Industry for Multi Energy Systems (역할 Principal Investigator; 지원 KERI; 기간 07.2025-11.2025)
- Distributed Control Technology for DC Local Grids (역할 Principal Investigator; 지원 KETI; 기간 05.2025-12.2025)
- Power System Analysis Program Development for Variations in External Condition (역할 Principal Investigator; 지원 Samsung Electronics; 기간 01.2025-12.2025)
- Roadmap of Inverter-based Future Power Systems (역할 Principal Investigator; 지원 Next Group; 기간 10.2024-03.2025)
- Policy Study for Promoting New Business in Electric Power Industry (역할 Principal Investigator; 지원 KETEP; 기간 09.2024-09.2025)
- Optimal Design of Large-scale Offshore Wind Farm Considering Stable Integration to Power Grids (역할 Principal Investigator; 지원 Youngin Energy Solution; 기간 08.2024-12.2024)
- Design and Investigation of Renewable Energy Hub-Terminal (ReHT) for Enhancing Hosting Capacity of Large Power Systems (역할 Principal Investigator; 지원 Hanyang; 기간 05.2024-12.2024; 협력 기관 KENTECH (Prof. Seungil Moon))
- Power System Database Development Considering Load Characteristics (역할 Principal Investigator; 지원 KERI; 기간 04.2024-11.2024)
- Power System Design to Provide Appropriate Electrical Energy to Yongin Industrial Complex (역할 Principal Investigator; 지원 Samsung Electronics; 기간 01.2024-12.2024)
- Modeling of Carbon Neutral Transmission Network Considering Distributed Localization of Renewable Energy and Loads (역할 Participating Researcher; 지원 KEPRI; 기간 07.2023-06.2025; 협력 기관 GIST (Prof. Yunsu Kim))
- Real-time Simulation Modeling of Active Synchronous Condenser (역할 Principal Investigator; 지원 ILJIN; 기간 11.2023-10.2024)
- Operation System for AC/DC Hybrid Distribution Networks (역할 Principal Investigator; 지원 KETEP; 기간 09.2022-07.2025; 협력 기관 KERI)
- Design and Analysis of AC/DC Hybrid Distribution Networks (역할 Principal Investigator; 지원 KETEP; 기간 09.2022-08.2025; 협력 기관 KEPRI)
- Development of Verification Technology for Improving Receptivity and Transmission Capacity of Offshore Wind Energy (역할 Participating Researcher; 지원 KEPRI; 기간 08.2022-06.2025; 협력 기관 Hanyang University (Prof. Raeyoung Kim))
- Development and Operation of MMC Type ESS Based Mobile Green Hub Station with Renewable Resources (역할 Participating Researcher; 지원 KETEP; 기간 11.2021-12.2024; 협력 기관 LS ELECTRIC)
- Insulation Coordination Study of Large-scale Offshore Wind Farms (역할 Principal Investigator; 지원 Youngin Energy Solution; 기간 05.2024-08.2024)
- System Analysis for Offshore Wind Farm Connection to the Transmission Networks (역할 Principal Investigator; 지원 Youngin Energy Solution; 기간 01.2024-06.2024)
- Analysis of Maximum Distance for Offshore Wind Power Delivery (역할 Principal Investigator; 지원 KOWP; 기간 04.2024-06.2024)
- Control of Hybrid Multi-terminal HVDC System for Integrating Large-scale Renewable Energy (역할 Principal Investigator; 지원 NRF; 기간 09.2021-02.2024)
- Development of Inertia Providing Control for Wind Turbine to Enhance Frequency Stability (역할 Principal Investigator; 지원 KERI; 기간 03.2023-11.2023)
- Development of Evaluation and Operation Strategies on Large Scale P2X Technologies to Increase Acceptance in Electric Gri d (역할 Participating Researcher; 지원 KETEP; 기간 11.2021-10.2023; 협력 기관 Institute for Advanced Engineering (IAE))
- Roadmap of Renewable Energy-based Self Sufficient KENTECH Campus Microgrid (역할 Principal Investigator; 지원 KENTECH; 기간 11.2022-06.2023)
- Strategy for RE100 Company using Renewable Energy in Jeollanam-do (역할 Principal Investigator; 지원 GEI; 기간 11.2022-05.2023)
- Grid Reform Roadmap Towards Renewable-oriented System for 2050 Net Zero Goal (역할 Participating Researcher; 지원 KERI; 기간 03.2022-08.2022)
- Development of Byproduct Gas Power Plant Operation System (역할 Participating Researcher; 지원 HD Hyundai Elec; 기간 01.2022-11.2024)
- Implementation of Secondary Control Algorithm for MMC HVDC System (역할 Principal Investigator; 지원 Pion Elec; 기간 09.2021-02.2022)

## 연락과 위치

- 교수 이메일: lgs1106@snu.ac.kr[^home]
- 연구실 위치: 서울특별시 관악구 관악로 1 서울대학교 301동 652-2호·609호. 학과 교수 소개의 연구실은 301동 609호다.[^home][^faculty]
- 기관 전화: +82-2-880-1770[^home]

## 각주
[^home]: 첫 화면. <https://sites.google.com/view/snupsl> (관측 2026-10-26).
[^about]: About Us. <https://sites.google.com/view/snupsl/about-us> (관측 2026-10-26).
[^research]: Research의 Renewable Energy Integration, DC Grid, Multi Energy System (MES), Offshore Wind Energy. <https://sites.google.com/view/snupsl/research> (관측 2026-10-26).
[^faculty]: 학과 교수 소개. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p898> (관측 2026-10-26).
[^dept]: 학과 연구실 상세. <https://ece.snu.ac.kr/research-faculty/research/lab?labidx=139&md=view> (관측 2026-10-26).
[^pubs]: Publication. <https://sites.google.com/view/snupsl/publication> (관측 2026-10-26).
[^researcher]: Researcher. <https://sites.google.com/view/snupsl/member/researcher> (관측 2026-10-26).
[^student]: Student. <https://sites.google.com/view/snupsl/member/student> (관측 2026-10-26).
[^alumni]: Alumni. <https://sites.google.com/view/snupsl/member/alumni> (관측 2026-10-26).
[^news]: News의 2024년 3월 1일 연구실 이전 안내. <https://sites.google.com/view/snupsl/news> (관측 2026-10-26).
[^projects]: Project. <https://sites.google.com/view/snupsl/project> (관측 2026-10-26).
[^p1]: S.-C. Cho, J.-w. Chang, G.-S. Lee, IEEE Transactions on Transportation Electrification 12, 6998-7012 (2026). <https://doi.org/10.1109/TTE.2026.3678287> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/403227532_Distributed_Optimal_Charging_Strategy_of_MVDC_Electric_Vehicle_Ultra-fast_Charging_Station_to_Manage_Peak_Load_and_Consumer_Convenience>.
[^p2]: J. Jung, J. Park, J.-H. Choi, G.-S. Lee, IEEE Transactions on Power Delivery 41, 1337-1349 (2026). <https://doi.org/10.1109/TPWRD.2026.3662444> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/400560170_An_Analytic_Method_for_Frequency_Nadir_Estimation_in_Fast_Frequency_Response_Resource_FFRR_Dominant_Power_Systems>.
[^p3]: S. Jo, J.-Y. Oh, G.-S. Lee, IEEE Transactions on Smart Grid 17, 402-414 (2026). <https://doi.org/10.1109/TSG.2025.3618926> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/396301218_Iterative_Linear_Programming-based_Angle-Relaxed_Branch_Flow_Model_and_Its_Application_to_Volt-Var_Control>.
[^p4]: Y.-K. Kim, S.-H. Lee, G.-S. Lee, iEnergy 4, 121-131 (2025). <https://doi.org/10.23919/IEN.2025.0011> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/392848634_Strength-constrained_unit_commitment_in_IBR_dominant_power_systems>.
[^p5]: J.-Y. Oh 외, S. Jo, IEEE Transactions on Smart Grid 16, 3666-3683 (2025). <https://doi.org/10.1109/TSG.2025.3580063> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/392749017_Sequential_Control_of_Individual_Switches_for_Real-time_Distribution_Network_Reconfiguration_Using_Deep_Reinforcement_Learning>.
[^p6]: S.-W. Ryu, S.-I. Moon, G.-S. Lee, IEEE Access 13, 195657-195672 (2025). <https://www.researchgate.net/scientific-contributions/Seung-Il-Moon-8437728> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/scientific-contributions/Seung-Il-Moon-8437728>.
[^p7]: R.-K. Kim 외, J.-W. Chang, IEEE Transactions on Sustainable Energy 16, 1372-1387 (2025). <https://www.researchgate.net/scientific-contributions/Seung-Il-Moon-8437728> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/scientific-contributions/Seung-Il-Moon-8437728>.

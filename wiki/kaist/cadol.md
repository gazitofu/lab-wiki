# 전산공기역학 및 최적설계 연구실 (Computational Aerodynamics and Design Optimization Laboratory, CADOL)

**KAIST 항공우주공학과 · 권오준 명예교수**

- 분야: 비정렬 격자 기반 전산유체역학, 공력 성능 예측과 형상 최적화, 로터와 복합형 무인 회전익기의 공력 해석, 층류–난류 천이 예측, 충격파·와류 계산용 고차 정확도 기법과 인공신경망을 이용한 해 재구성, 복사 전달 방정식 계산, 희박기체 영역 해석
- 대분야: 기계·로봇·제조
- 태그: 유체역학·유동[^lab][^p1][^p4], 과학·공학 AI[^p7], 열전달·열관리[^p8], 희박 기체 역학[^lab]
- 홈페이지: 학과 연구실 소개 페이지 <https://ae.kaist.ac.kr/boards/view/board_lab/75>
- 근거와 출처: [전산공기역학 및 최적설계 연구실 근거 페이지](cadol-sources.md)

> 비정렬 격자 기반의 수치해석 기법으로 풍력 터빈, 고정익기, 발사체, 헬리콥터, 수중물체 등의 공력 성능을 예측하고 형상을 최적화하는 항공우주공학과의 전산공기역학 연구실이다.[^lab] 2021–2024년 대표 논문은 로터의 정지 비행 성능, 층류–난류 천이 예측, 충격파와 와류를 높은 해상도로 계산하는 수치 기법과 인공신경망을 이용한 해 재구성, 복사 전달 방정식의 계산 방법을 다룬다.[^p1][^p4][^p5][^p7][^p8]

## 무엇을 연구하나

연구실은 KAIST 항공우주공학과 권오준 교수의 연구실이다. 학과 연구실 소개는 연구실명을 「전산공기역학 및 최적설계 연구실」로, 영문 이름을 CADOL (Computational Aerodynamics and Design Optimization Laboratory)로 적고, 연구분야로 전산유체역학(Computational Fluid Dynamics, CFD, 유체의 흐름을 나타내는 방정식을 컴퓨터로 풀어 흐름을 구하는 분야)을 든다.[^lab] 교수는 1994년 항공우주공학과에 부임해 2022년 정년 퇴임했고, 학과 교수진 페이지는 교수를 명예교수 명단에 싣는다.[^retire][^emer]

학과 연구실 소개에 따르면 연구실은 비정렬 격자(unstructured mesh, 계산 영역을 행과 열의 규칙적인 배열을 따르지 않는 칸들로 나눈 계산 격자) 기반의 수치해석 기법을 바탕으로 공력(공기 흐름이 물체에 주는 힘) 성능을 예측하고 형상을 최적화한다. 풍력 터빈, 미사일, 고정익기, 발사체, 헬리콥터, 수중물체 등의 공력 해석부터 희박기체(분자가 다른 분자와 부딪히기 전까지 움직이는 평균 거리를 흐름의 길이 규모에 대해 무시할 수 없는 기체) 영역의 해석까지 여러 분야에서 CFD 해석을 한다.[^lab] 영문 연구실 소개는 비행기, 풍력 터빈, 헬리콥터, 수중 운동체, 발사체의 공력 형상을 수치 모사해 공력 계수와 층류–난류 천이(laminar-turbulent transition, 층을 이루며 흐르던 흐름이 불규칙하게 요동하는 난류로 바뀌는 현상) 위치 같은 공력 성능을 예측하고, 주어진 공력 형상을 수치 계산으로 최적화한다고 적는다.[^laben]

2021–2024년 대표 논문은 로터의 정지 비행(hover, 공중의 한 자리에 머무는 비행) 성능과 복합형 무인 회전익기의 공력 해석,[^p1][^p2][^p3] 교차류(crossflow, 경계층 안에서 바깥 흐름 방향과 수직인 방향의 흐름 성분)가 일으키는 천이를 포함한 층류–난류 천이 예측,[^p4] 충격파와 와류를 높은 해상도로 계산하는 고차 정확도 기법과 인공신경망을 이용한 해 재구성(격자 칸의 평균값에서 칸 경계의 값을 추정하는 계산 단계),[^p5][^p6][^p7] 3차원 복사 전달 방정식(복사가 매질을 지나며 흡수·방출·산란으로 세기가 변하는 과정을 나타내는 방정식)의 각도 이산화(복사가 나아갈 수 있는 방향 전체를 유한한 수의 방향으로 나누는 일)를 다룬다.[^p8] 로터와 날개–와류 상호작용 계산에는 비정렬 격자와 직교 격자(Cartesian mesh, 좌표축에 나란한 칸으로 나눈 격자)를 함께 쓰는 혼합 격자와 레이놀즈 평균 나비에–스토크스(RANS, 흐름 변수를 평균과 요동으로 나누어 평균을 취한 유체 운동 방정식으로, 요동의 효과는 난류 모형으로 나타낸다) 해석 프로그램을 썼다.[^p1][^p2][^p6]

## 주요 연구 주제

### 1. 회전익기 로터의 공력 해석

영문 연구실 소개는 헬리콥터를 수치 모사 대상으로 든다.[^laben]
대표 논문 1은 비정렬 격자와 직교 격자를 섞은 혼합 격자의 RANS 해석 프로그램으로 HVAB 로터의 정지 비행을 계산했다. 층류–난류 교차류 천이를 예측하는 개선 천이 모형 γ-Reθt-CF+와, 비점성 유속을 계산하는 개선 기법 ESWENO-P를 썼다. 먼저 PSP 로터 형상으로 계산에 넣을 난류 강도를 정하는 변수 연구를 하고 시험 설비 벽의 영향을 살핀 뒤, 그 조건으로 HVAB 로터의 추력·토크 계수와 성능 지수(figure of merit, 같은 추력을 낼 때 이상적인 로터에 필요한 동력과 실제 동력의 비), 천이 위치와 날개 끝 와류 궤적을 분석했다.[^p1]
대표 논문 2는 압력 감응 도료(PSP) 로터의 정지 비행을 같은 방식으로 계산해 천이 시작 위치와 추력 계수, 토크 계수, 성능 지수를 실험 자료와 비교했고, 동체와 시험 설비 벽이 정지 비행 성능에 주는 영향을 조사했다.[^p2]
대표 논문 3은 프로펠러 두 개, 주날개와 꼬리날개를 단 동체, 동축 로터로 이루어진 개념 설계 고속 복합형 무인 회전익기를 비정렬 RANS 해석 프로그램으로 계산했다. 정지 비행, 저속 전환 비행, 고속 비행, 최대 비행 속도 조건에서 추진 구성 요소의 공력 계수를 비교하고, 동축 로터·프로펠러·날개 사이의 상호작용과 지면이 공력 성능에 주는 영향을 조사했다.[^p3]

### 2. 층류–난류 천이 예측

영문 연구실 소개는 수치 모사로 공력 계수와 함께 층류–난류 천이 위치를 예측한다고 적는다.[^laben]
대표 논문 4는 비정렬 격자 기반 RANS 해석 프로그램에 넣은 γ-Reθt-CF+ 천이 모형을 평가했다. 3차원 채널 속 돌기 문제를 완전 난류로 계산해 천이 모형과 결합한 k–ω 전단응력수송(SST) 난류 모형의 구현을 확인하고, 6:1 장구형 회전타원체의 받음각 세 가지에서 천이 시작 위치를 실험과 비교해 천이 모형을 검증했다. 이어 자연 층류형 공통 연구 모형(CRM-NLF)의 표면 마찰 분포, 표면 압력 분포, 천이 시작 위치를 예측하고, 성긴·중간·조밀 격자로 격자 해상도를 검토한 뒤 받음각 네 가지에서 공력 성능을 실험과 비교했다.[^p4]
대표 논문 1·2의 로터 계산도 같은 천이 모형으로 교차류가 일으키는 천이를 예측했다.[^p1][^p2] 최근 논문 목록에는 천이 유동 계산 기법 논문(Computers & Fluids, 2021)과 정지 비행 로터 날개의 성능에 교차류 천이가 주는 영향을 계산한 논문(Aerospace Science and Technology, 2021)도 있다.[^cr]

### 3. 고차 정확도 수치 기법과 인공신경망

대표 논문 5는 에너지 안정 가중 본질적 비진동(ESWENO) 기법의 가중 함수를 고쳐 고차 정확도·고해상도의 ESWENO-P 기법을 만들었다. 가중 함수에 사용자가 정하는 새 매개변수를 넣고 WENO-ZP 기법의 미세 조정 항을 가져왔으며, 충격파와 와류가 있는 1차원·2차원 표준 문제로 정확도와 해상도를 검증했다. ESWENO-P는 ESWENO보다 강한 불연속 근처에서 안정적이었고, WENO-ZP보다 미세 조정 항의 매개변수에 덜 민감했다.[^p5]
대표 논문 6은 물체 가까이의 비정렬 격자와 바깥의 직교 격자로 이루어진 혼합 격자에서 2차원·3차원 날개–와류 상호작용 문제를 계산해, 직교 격자에 쓴 WENO 계열 기법들의 해상도를 압력 계수 분포로 비교했다. ESWENO-P 기법이 기존 WENO 계열 기법보다 안정적이었고 날개꼴·날개–와류 상호작용 문제를 일관되게 높은 해상도로 풀었다.[^p6]
대표 논문 7은 다층 퍼셉트론(MLP)이라는 인공신경망으로 CFD의 해를 재구성할 수 있는지 살폈다. WENO3의 입력과 출력으로 만든 학습 자료와 WENO3의 입력을 WENO7의 출력에 잇는 학습 자료로 MLP를 학습시켜 Sod 문제와 Shu–Osher 문제로 평가했고, 가장 정확한 해를 낸 MLP는 비정렬 격자의 초음속 채널 문제 등에서도 계산에 쓰는 이웃 칸 범위를 넓히지 않고 WENO3보다 정확한 해를 냈다.[^p7]

### 4. 복사 열전달 계산

대표 논문 8은 3차원 복사 전달 방정식(RTE)에 쓰는 새 각도 이산화 방법 RPAD(repulsive particle angular discretization)를 제안했다. 입체각을 되도록 고르게 나누려고 단위 구면 위에서 서로 밀어내는 입자를 두고 그 위치를 복사 방향으로 썼다. 흡수·방출 매질이 찬 원통형 공간 문제와 순수 산란을 다루는 로켓 배기 플룸 기저부 가열 문제로 다른 각도 이산화 방법과 비교했고, 연구진은 RPAD가 시험한 다른 방법과 비슷하거나 더 정확한 해를 준다고 정리했다.[^p8]

## 대표 논문

권오준 교수가 저자로 참여한 2021–2024년 논문 가운데 논문 기록에 교수 소속이 KAIST 항공우주공학과로 적혀 있고 초록을 확인할 수 있는 여덟 편을 연구 갈래별로 골랐다. 1·2·4·7·8번은 교수가 마지막 저자이고, 3·5·6번은 교수가 3명 가운데 2번째 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2022 | [Numerical simulation of HVAB rotor in hover using a mixed-mesh flow solver](https://doi.org/10.1007/s12206-022-0529-4) · Journal of Mechanical Science and Technology 36 | 비정렬 격자와 직교 격자를 섞은 혼합 격자를 쓰는 RANS 전산유체역학 해석 프로그램으로 HVAB 로터를 계산했다. 층류–난류 천이를 예측하려고 개선한 교차류 천이 모형 γ-Reθt-CF+를 쓰고, 해상도 높은 흐름 해를 얻으려고 비점성 유속 계산에 개선 기법 ESWENO-P를 썼다. 계산에 넣을 난류 강도를 찾으려고 먼저 PSP 로터 형상으로 변수 연구를 했고, National Full-Scale Aerodynamics Complex 시험 설비 벽의 영향도 조사했다. 그다음 PSP 로터 계산에서 얻은 조건으로 HVAB 로터의 성능을 예측해 추력·토크 계수와 성능 지수를 분석하고, 층류–난류 천이 위치와 날개 끝 와류 궤적 같은 흐름 특성도 살폈다.[^p1] | 1저자 Sang Hyun Park, 마지막 저자 Oh Joon Kwon(권오준 교수) (2명) |
| 2 | 2021 | [Numerical Study of Effects of Fuselage and Facility Wall on PSP Rotor Performance in Hover](https://doi.org/10.1007/s42405-021-00420-9) · International Journal of Aeronautical and Space Sciences 23 | 비정렬 혼합 격자 기반 RANS 전산유체역학 해석 프로그램으로 압력 감응 도료(PSP) 로터의 정지 비행을 계산했다. 교차류가 일으키는 천이와 흐름 박리를 포함한 층류–난류 천이 시작을 예측하려고 개선 천이 모형 γ-Reθt-CF+를 쓰고, 와류를 높은 해상도로 잡으려고 직교 격자의 비점성 유속 계산에 개선 기법 ESWENO-P를 썼다. 예측한 천이 시작 위치와 추력 계수, 토크 계수, 성능 지수로 본 로터 공력 성능을 실험 자료와 비교했고, 동체와 시험 설비 벽이 정지 비행 성능에 주는 영향도 조사했다.[^p2] | 1저자 Sang Hyun Park, 마지막 저자 Oh Joon Kwon(권오준 교수) (2명) |
| 3 | 2023 | [Aerodynamic Analysis of High-Speed Compound Unmanned Rotorcraft Using an Unstructured Flow Solver](https://doi.org/10.1007/s42405-023-00595-3) · International Journal of Aeronautical and Space Sciences 24 | 비정렬 RANS 해석 프로그램으로 고속 복합형 무인 회전익기를 계산했다. 계산에 쓴 기체는 개념 설계한 회전익기로, 프로펠러 두 개, 주날개와 꼬리날개를 단 동체, 동축 로터로 이루어진다. 정지 비행, 저속 전환 비행, 고속 비행, 최대 비행 속도의 조건에서 추진 구성 요소의 공력 계수를 비교해 공력 특성을 살폈다. 동축 로터, 프로펠러, 날개 사이의 유체 역학적 상호작용과, 지면이 회전익기의 공력 성능에 주는 영향도 조사했다.[^p3] | 1저자 Sang Hyun Park, 마지막 저자 Sang Lee (3명), 권오준 교수는 2번째 저자 |
| 4 | 2022 | [Prediction and Analysis of Transitional Crossflows Using γ-Reθt-CF+ Model](https://doi.org/10.1007/s42405-022-00457-4) · International Journal of Aeronautical and Space Sciences 23 | 비정렬 격자 기반 RANS 전산유체역학 해석 프로그램으로 γ-Reθt-CF+ 천이 모형을 수치적으로 평가했다. 먼저 3차원 채널 속 돌기 검증 문제를 완전 난류로 계산해, 천이 모형과 결합한 k–ω 전단응력수송 난류 모형의 구현을 확인했다. 천이 모형은 6:1 장구형 회전타원체의 받음각 세 가지에서 천이 시작 위치를 실험 결과와 비교해 검증했다. 이어 이 모형으로 자연 층류형 공통 연구 모형(CRM-NLF)의 표면 마찰 분포, 표면 압력 분포, 천이 시작 위치를 예측했고, 이를 위해 고정 받음각에서 성긴·중간·조밀 격자로 격자 해상도를 검토했다. CRM-NLF의 공력 성능은 받음각 네 가지에서 실험과 비교했다.[^p4] | 1저자 Sang Hyun Park, 마지막 저자 Oh Joon Kwon(권오준 교수) (3명) |
| 5 | 2022 | [Improved high-order high-resolution energy stable weighted essentially non-oscillatory plus scheme for shock/vortex problems](https://doi.org/10.1063/5.0083675) · AIP Advances 12 | 에너지 안정 가중 본질적 비진동(ESWENO) 기법의 가중 함수를 고쳐 고차 정확도·고해상도의 ESWENO-P 기법을 개발했다. 가중 함수에 사용자가 정하는 새 매개변수를 넣은 뒤, WENO-ZP 기법의 미세 조정 항을 고친 가중 함수에 가져왔고, 미세 조정 항에 든 매개변수의 값은 변수 연구로 정했다. 충격파와 와류가 있는 잘 알려진 1차원·2차원 표준 흐름 문제로 정확도와 해상도를 검증했다. ESWENO-P는 ESWENO보다 강한 불연속 근처에서 안정적이었고, WENO-ZP보다 미세 조정 항의 매개변수에 덜 민감했다. 연구진은 ESWENO-P가 기존 WENO 계열 기법과 견주어 계산 부담을 크게 늘리지 않고 흐름을 일관되게 높은 해상도로 풀어낸다고 정리했다.[^p5] | 1저자 S. H. Park, 마지막 저자 S. Lee (3명), 권오준 교수는 2번째 저자 |
| 6 | 2022 | [Assessment of a High-Order High-Resolution ESWENO-P Scheme for AVI/BVI Problems](https://doi.org/10.1007/s42405-022-00525-9) · International Journal of Aeronautical and Space Sciences 23 | 혼합 격자 기반 RANS 전산유체역학 해석 프로그램으로 2차원·3차원 날개–와류 상호작용 문제를 평가했다. 격자는 물체 가까이의 비정렬 영역과 바깥의 직교 영역으로 이루어진다. 와류를 높은 해상도로 잡으려고 직교 격자에서는 WENO 계열 기법으로, 비정렬 격자에서는 Roe의 유속 차분 분할 기법으로 비점성 유속을 계산했다. WENO 계열 기법들의 해상도를 압력 계수 분포로 비교한 결과, ESWENO-P 기법이 기존 WENO 계열 기법보다 안정적이고 날개꼴·날개–와류 상호작용 문제를 일관되게 높은 해상도로 풀었다.[^p6] | 1저자 Sang Hyun Park, 마지막 저자 Sang Lee (3명), 권오준 교수는 2번째 저자 |
| 7 | 2024 | [Solution reconstruction for computational fluid dynamics via artificial neural network](https://doi.org/10.1007/s12206-023-1220-0) · Journal of Mechanical Science and Technology 38 | 인공신경망으로 전산유체역학의 해를 재구성할 가능성을 살폈다. 여러 신경망 모형 가운데 다층 퍼셉트론(MLP)을 골라 그 수치적 특성을 먼저 조사했다. WENO3의 입력과 출력 관계로 학습 자료 α를, WENO3의 입력을 WENO7의 출력에 잇는 학습 자료 β를 만들어 MLP를 각각 6,000개와 10,000개 학습시켰다. 강한 불연속을 다루는 능력은 Sod 문제로, 충격파와 사인파 모양 밀도파가 섞인 더 일반적인 흐름 문제의 성능은 Shu–Osher 문제로 평가했다. 두 문제에서 가장 정확한 해를 낸 학습 자료 β의 MLP는 상호작용하는 폭발파 문제와 비정렬 격자의 초음속 채널 문제에서도 계산에 쓰는 이웃 칸 범위를 넓히지 않고 WENO3보다 정확한 해를 냈다. 연구진은 MLP가 기존 재구성 기법보다 정확하게 해를 재구성할 가능성이 있다고 결론지었다.[^p7] | 1저자 Seongmun Jung, 마지막 저자 Oh Joon Kwon(권오준 교수) (2명) |
| 8 | 2022 | [An Angular Discretization Method Using Repulsive Particles for the Three-Dimensional Radiative Transfer Equation](https://doi.org/10.1007/s42405-022-00468-1) · International Journal of Aeronautical and Space Sciences 23 | 3차원 복사 전달 방정식(RTE)에 쓰는 새 각도 이산화 방법 RPAD를 제안했다. 입체각을 되도록 고르게 나누려고 단위 구면 위에서 서로 밀어내는 입자를 두고, 그 위치를 복사 방향으로 바로 썼다. 제어 각 사이의 최소 거리로 견준 결과 RPAD의 복사 방향 분포가 가장 고르게 나왔고, 반 입체각에 대한 1차 모멘트 적분도 가장 정확했다. 순수 흡수·방출 매질이 찬 원통형 공간 문제에서는 FTn FVM, IUSD, RPAD의 최대 복사 열유속 오차가 비슷했지만, 좌표계에 대한 표면 방향이 바뀔 때 RPAD의 열유속 변동이 가장 작았다. 순수 산란을 다루는 로켓 배기 플룸 기저부 가열 문제에서는 IUSD나 RPAD의 최대 오차가 가장 작았고 FTn FVM이 그다음이었다. 연구진은 RPAD가 시험한 다른 각도 이산화 방법과 비슷하거나 더 정확한 해를 준다고 정리했다.[^p8] | 1저자 Seongmun Jung, 마지막 저자 Oh Joon Kwon(권오준 교수) (3명) |

## 교수와 전문 분야

권오준 교수(Kwon, Oh-Joon)는 KAIST 항공우주공학과 명예교수다. 학과 교수진 페이지의 명예교수 탭은 교수를 Emeritus Professor로 싣고, 학력을 B.S. Seoul Nat'l Univ ('79), M.S. KAIST ('81), Ph.D. Georgia Tech ('88)로, 연구분야를 Computational Aerodynamics, Design Optimization으로 적는다.[^emer] 같은 페이지의 교수 탭 명단에는 교수 이름이 없고,[^fac] 영문 교수진 페이지는 교수를 Professor로 적는다.[^facen] 학과 뉴스에 따르면 교수는 1994년 부임해 2022년까지 약 28년 동안 항공우주공학과에 재직했고, 2022년 6월 16일 정년 퇴임행사가 열렸다.[^retire] 학과 이전 구성원 페이지의 역대 학과장 표는 교수를 2005.03.01.–2007.03.31. 전공책임교수로 적는다.[^chair] 2022학년도 봄학기에는 「공기역학 Ⅱ」 강의로 학과 우수 강의상을 받았다.[^lecture]

교수가 저자로 참여한 2021–2024년 논문을 보면 교수의 전문 분야는 비정렬 격자 기반 RANS 해석 프로그램으로 로터와 날개·동체 같은 공력 형상의 공력을 계산하는 전산공기역학이다.[^p1][^p3][^p4] 층류–난류 천이 모형, 충격파와 와류를 높은 해상도로 계산하는 WENO 계열 고차 정확도 기법, 인공신경망을 이용한 수치 재구성, 3차원 복사 전달 방정식의 각도 이산화를 다뤘고,[^p4][^p5][^p7][^p8] 방출 분광으로 이산화탄소 온도를 재는 논문에도 공저자로 참여했다.[^cr]

## 응용 분야

학과 연구실 소개는 풍력 터빈, 미사일, 고정익기, 발사체, 헬리콥터, 수중물체를 공력 해석 대상으로 들고,[^lab] 영문 연구실 소개는 비행기, 풍력 터빈, 헬리콥터, 수중 운동체, 발사체를 수치 모사 대상으로 든다.[^laben] 대표 논문 3은 고속 복합형 무인 회전익기의 정지·전환·고속 비행 조건 공력을, 대표 논문 4는 자연 층류형 공통 연구 모형(CRM-NLF)의 천이와 공력 성능을 다루고, 대표 논문 8은 로켓 배기 플룸 기저부 가열을 표준 문제의 하나로 계산했다.[^p3][^p4][^p8]

## 최근 논문 목록 (2021–2026)

권오준 교수가 저자로 참여한 2021–2024년 논문 13편이다(2024년 1편, 2023년 1편, 2022년 5편, 2021년 6편). 학술지 논문 11편과 AIAA Scitech 2021 Forum 발표 논문 2편이다. 저자·제목·학술지 표기는 출판사가 등록한 서지를 따랐고, 연도는 첫 출판 연도이며, 연도 안에서는 출판일이 늦은 논문부터 적었다.[^cr][^oa] 교수는 2022년 정년 퇴임했고, 2023–2024년 논문 두 편도 논문 기록에 교수 소속이 KAIST 항공우주공학과로 적혀 있다.[^retire][^oa]

**2024**

- Seongmun Jung, Oh Joon Kwon. "Solution reconstruction for computational fluid dynamics via artificial neural network". *Journal of Mechanical Science and Technology 38, 229-244 (2024)*.

**2023**

- Sang Hyun Park, Oh Joon Kwon, Sang Lee. "Aerodynamic Analysis of High-Speed Compound Unmanned Rotorcraft Using an Unstructured Flow Solver". *International Journal of Aeronautical and Space Sciences 24, 1077-1085 (2023)*.

**2022**

- Sang Hyun Park, Oh Joon Kwon, Sang Lee. "Assessment of a High-Order High-Resolution ESWENO-P Scheme for AVI/BVI Problems". *International Journal of Aeronautical and Space Sciences 23, 882-895 (2022)*.
- Sang Hyun Park, Oh Joon Kwon. "Numerical simulation of HVAB rotor in hover using a mixed-mesh flow solver". *Journal of Mechanical Science and Technology 36, 2969-2979 (2022)*.
- Seongmun Jung, Sung Min Jo, Oh Joon Kwon. "An Angular Discretization Method Using Repulsive Particles for the Three-Dimensional Radiative Transfer Equation". *International Journal of Aeronautical and Space Sciences 23, 501-510 (2022)*.
- Sang Hyun Park, Jaeseong Han, Oh Joon Kwon. "Prediction and Analysis of Transitional Crossflows Using γ-Reθt-CF+ Model". *International Journal of Aeronautical and Space Sciences 23, 461-470 (2022)*.
- S. H. Park, O. J. Kwon, S. Lee. "Improved high-order high-resolution energy stable weighted essentially non-oscillatory plus scheme for shock/vortex problems". *AIP Advances 12, 045106 (2022)*.

**2021**

- Sang Hyun Park, Oh Joon Kwon. "Numerical Study of Effects of Fuselage and Facility Wall on PSP Rotor Performance in Hover". *International Journal of Aeronautical and Space Sciences 23, 19-30 (2021)*.
- Jaeseong Han, Je Young Hwang, Oh Joon Kwon. "Numerical investigation of effect of crossflow transition on rotor blade performance in hover". *Aerospace Science and Technology 114, 106733 (2021)*.
- Ho Jun Kim, Oh Joon Kwon. "Numerical simulation of transitional flows using a blended IDDES and correlation-based transition model". *Computers & Fluids 222, 104916 (2021)*.
- Hanseul Shim, Sung Min Jo, Oh Joon Kwon, Gisu Park. "Temperature measurement of carbon dioxide using emission spectroscopy". *Journal of Quantitative Spectroscopy and Radiative Transfer 260, 107463 (2021)*.
- Seongmun Jung, Oh Joon Kwon. "A Flux Reconstruction Model Based on an Artificial Neural Network". *AIAA Scitech 2021 Forum (2021)*.
- Sang Hyun Park, Jaeseong Han, Oh Joon Kwon. "Numerical Study of HVAB Rotor Using a Mixed Mesh Flow Solver". *AIAA Scitech 2021 Forum (2021)*.

## 수상

항공우주공학과 뉴스가 알린 2021–2026년 수상 두 건이다. 날짜는 뉴스가 적은 시상일이다.[^lecture][^safety]

- 2022-08-04 · 항공우주공학과 2022학년도 봄학기 우수 강의상(권오준 교수, 「공기역학 Ⅱ」 강의)
- 2021-11-08 · 안전관리위원회 2020년도 하반기 안전관리우수연구실(2020-12-28 기준, 정기안전교육 이수율로 선정)

## 연락과 위치

- 위치: 항공우주공학과 N7-2동 #3308(학과 연구실 소개의 Office 표기)[^lab][^emer]
- 우편 주소: 34141 대전광역시 유성구 대학로 291 KAIST 항공우주공학과[^lab]
- 전화: 042-350-3760(학과 연구실 소개의 Tel), 82 42 350 3720(학과 교수진 명예교수 탭의 Tel)[^lab][^emer]
- 교수 이메일: ojkwon@kaist.ac.kr[^lab][^emer]
[^p1]: S. H. Park, O. J. Kwon, Journal of Mechanical Science and Technology 36, 2969-2979 (온라인 2022-06-20). <https://doi.org/10.1007/s12206-022-0529-4> 초록 기준(출판사 논문 페이지).
[^p2]: S. H. Park, O. J. Kwon, International Journal of Aeronautical and Space Sciences 23, 19-30 (온라인 2021-10-15). <https://doi.org/10.1007/s42405-021-00420-9> 초록 기준(출판사 논문 페이지).
[^p3]: S. H. Park, O. J. Kwon, S. Lee, International Journal of Aeronautical and Space Sciences 24, 1077-1085 (온라인 2023-05-30). <https://doi.org/10.1007/s42405-023-00595-3> 초록 기준(출판사 논문 페이지).
[^p4]: S. H. Park, J. Han, O. J. Kwon, International Journal of Aeronautical and Space Sciences 23, 461-470 (온라인 2022-04-22). <https://doi.org/10.1007/s42405-022-00457-4> 초록 기준(출판사 논문 페이지).
[^p5]: S. H. Park, O. J. Kwon, S. Lee, AIP Advances 12, 045106 (온라인 2022-04-04). <https://doi.org/10.1063/5.0083675> 초록 기준.
[^p6]: S. H. Park, O. J. Kwon, S. Lee, International Journal of Aeronautical and Space Sciences 23, 882-895 (온라인 2022-09-24). <https://doi.org/10.1007/s42405-022-00525-9> 초록 기준(출판사 논문 페이지).
[^p7]: S. Jung, O. J. Kwon, Journal of Mechanical Science and Technology 38, 229-244 (온라인 2024-01-08). <https://doi.org/10.1007/s12206-023-1220-0> 초록 기준(출판사 논문 페이지).
[^p8]: S. Jung, S. M. Jo, O. J. Kwon, International Journal of Aeronautical and Space Sciences 23, 501-510 (온라인 2022-05-31). <https://doi.org/10.1007/s42405-022-00468-1> 초록 기준(출판사 논문 페이지).
[^lab]: KAIST 항공우주공학과 연구실 소개 「Computational Aerodynamics and Design Optimization」 <https://ae.kaist.ac.kr/boards/view/board_lab/75> (연구실명, 교수, 연구실 소개, 웹사이트·이메일·Tel·Office, 연구분야, 2021-08-16 게시, 2026-10-25 열람)
[^laben]: KAIST 항공우주공학과 영문 연구실 소개 「Computational Aerodynamics and Design Optimization Laboratory」 <https://ae.kaist.ac.kr/boards/view/board_lab_en/12086> (Lab., P.I., Laboratory Introduction, Research field, 2021-10-11 게시, 2026-10-25 열람)
[^emer]: KAIST 항공우주공학과 교수진 명예교수 탭 <https://ae.kaist.ac.kr/boards/lists/board_faculty/sc_category/2/> (권오준 항목의 Emeritus Professor, Career, Tel, Website, E-mail, 연구분야, 연구실, 2026-10-25 열람)
[^fac]: KAIST 항공우주공학과 교수진 교수 탭 <https://ae.kaist.ac.kr/boards/lists/board_faculty/sc_category/1/> (2026-10-25 열람)
[^facen]: KAIST 항공우주공학과 영문 교수진 페이지 <https://ae.kaist.ac.kr/boards/lists/board_faculty_en> (Kwon, Oh-Joon 항목, 2026-10-25 열람)
[^chair]: KAIST 항공우주공학과 이전 구성원 페이지 <https://ae.kaist.ac.kr/pages/sub/sub01_04_04> (역대 학과장 표, 2026-10-25 열람)
[^retire]: KAIST 항공우주공학과 뉴스 「권오준 교수, 정년 퇴임행사 개최」 <https://ae.kaist.ac.kr/boards/view/board_news/12653> (2022-07-06 게시, 2026-10-25 열람)
[^lecture]: KAIST 항공우주공학과 뉴스 「2022.8.4., 2022학년도 봄학기 우수강의상 시상식 개최」 <https://ae.kaist.ac.kr/boards/view/board_news/12676> (2022-08-05 게시, 2026-10-25 열람)
[^safety]: KAIST 항공우주공학과 뉴스 「2021년도 안전관리우수연구실 시상식 개최」 <https://ae.kaist.ac.kr/boards/view/board_news/12280> (2021-11-09 게시, 2026-10-25 열람)
[^oa]: OpenAlex 저자 기록 <https://api.openalex.org/> (교수 ORCID 0000-0002-5044-7236이 붙은 저자 기록의 2021년 이후 논문 13건과 각 논문의 교수 소속, 2026-10-25 조회)
[^cr]: Crossref 출판사 등록 서지 <https://api.crossref.org/> (교수 이름·ORCID 검색과 논문의 저자·제목·학술지·권·쪽·출판일, 2026-10-25 조회)

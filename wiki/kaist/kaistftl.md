# 핵융합 및 플라즈마 이론 연구실 (Fusion and Plasma Theory Lab)

**KAIST 원자력및양자공학과 · 최경진 교수**

- 분야: 핵융합 플라즈마의 난류와 수송 이론, 띠흐름(zonal flow)과 빠른 이온, 자이로운동론 시뮬레이션, 토카막과 스텔러레이터 사이의 3차원 자기장 배치, 개방형 자기장 장치의 가둠 이론, 산업·저온 플라즈마의 불안정성, 우주·천체 플라즈마
- 대분야: 물리·양자, 에너지·환경·지구
- 태그: 핵융합[^p3][^p4][^p5], 플라즈마[^home][^p2], 과학·공학 AI[^p3][^p6], 우주 플라즈마·우주 기상[^home]
- 홈페이지: <https://sites.google.com/view/kaistftl>
- 근거와 출처: [핵융합 및 플라즈마 이론 연구실 근거 페이지](kaistftl-sources.md)

> 핵융합 에너지 연구, 산업·저온 플라즈마, 우주·천체 플라즈마를 연구 분야로 드는 원자력및양자공학과의 플라즈마 이론 연구실이다.[^home] 2025–2026년 대표 논문은 토카막·스텔러레이터 플라즈마의 난류와 띠흐름을 해석 이론과 자이로운동론 시뮬레이션으로 다루고, KSTAR 토카막 등의 실험 자료를 분석한다.[^p1][^p3][^p5][^p7]

## 무엇을 연구하나

연구실은 KAIST 원자력및양자공학과 최경진 교수의 연구실이다. 학과 연구그룹 페이지는 「핵융합 및 플라즈마」 그룹 아래 이 연구실을 「핵융합 및 플라즈마 이론 연구실」로 적고,[^deptlab] 영문 연구그룹 페이지는 Fusion and Plasma Theory Laboratory로 적는다.[^deptlaben] 누리집은 연구실 이름을 KAIST Fusion & Plasma Theory Lab으로 적는다.[^home] 교수는 2024년부터 KAIST 원자력및양자공학과 조교수다.[^prof]

누리집 첫 화면은 연구 분야를 세 갈래로 든다.[^home] 첫째 갈래인 핵융합 에너지 연구(Fusion Energy Research)의 주제는 수송 예측을 위한 비국소 난류(non-local turbulence) 동역학 모형화, 토카막과 스텔러레이터 사이의 숨은 3차원 자기장 배치(Hidden 3D configuration between tokamak & stellarator), 고성능 개방형 자기장 장치(open-field machine)의 가둠 이론이다.[^home] 둘째 갈래인 산업·저온 플라즈마(Industrial and Low-temp. Plasmas)의 주제는 고출력 운전 영역에서의 불안정성 억제와, 난류를 이용해 임계를 넘어 성능을 끌어올리는 일(Maximizing performance beyond criticality with turbulence)이다.[^home] 셋째 갈래인 우주·천체 플라즈마(Space and Astrophysical Plasmas)의 주제는 자기권과 태양풍에서 자기 조직화로 생기는 간헐성(intermittency)과, 오로라와 강착 원반에서의 비정상 가속(anomalous acceleration)이다.[^home]

2025–2026년 대표 논문은 모두 핵융합 플라즈마를 다룬다. 띠흐름과 E × B 계단 구조를 해석 이론으로 다룬 논문,[^p1][^p2] 자이로운동론 시뮬레이션으로 토카막의 자기섬(magnetic island)과 저주파 파동, 스텔러레이터의 난류를 계산한 논문,[^p3][^p4][^p5] 실험 자료로 전자 열 수송을 학습한 신경망 모형과 KSTAR 요동 자료의 통계 분석이 있다.[^p6][^p7]

## 주요 연구 주제

### 1. 난류와 띠흐름(zonal flow) 이론

누리집은 핵융합 에너지 연구의 첫 주제로 수송 예측을 위한 비국소 난류 동역학 모형화를 든다.[^home]
대표 논문 1은 E × B 계단(E × B staircase, 전기장과 자기장이 만드는 흐름의 전단층이 반경 방향으로 간격을 두고 늘어선 구조)이 흐름 분포에서 튀어나온 곳과 파인 곳의 짝(bump-hole pair)이 자라며 저절로 무너지는 것에 맞서 유지되는 조건을 해석 이론으로 구했다. 계단을 유지하는 데 필요한 임계 E × B 전단율은 흐름 성분의 규모에 따라 달라, 규모가 작은 흐름 성분일수록 무너지기 쉬웠다. 빠른 이온(fast ion)을 넣으면 표류파의 반경 방향 군속도가 줄어 임계 전단율이 크게 낮아졌고, 연구진은 이 결과가 KSTAR FIRE 모드 플라즈마에서 계단 구조가 오래 유지된 최근 실험 관측과 맞는다고 적었다.[^p1]
대표 논문 2는 차니–하세가와–미마(Charney–Hasegawa–Mima) 방정식에서 띠흐름 세 개가 서로 결합하는 비선형 방정식을 유도했다. 띠흐름끼리는 직접 상호작용하지 못하지만 표류파 두 개와 띠흐름 하나가 얽힌 결합을 거쳐 상호작용할 수 있고, 파장이 가장 짧은 띠흐름이 파장이 긴 두 띠흐름으로 붕괴하며 포화한다. 연구진은 이 붕괴가 잇따라 일어나 요동 에너지가 긴 파장 쪽으로 옮겨 가고, 오랜 시간이 지나면 대부분의 에너지가 계가 허용하는 가장 긴 파장의 띠흐름 세 개에 모인다고 예측했다.[^p2]

### 2. 자이로운동론 시뮬레이션

대표 논문 3은 전역 토로이달 자이로운동론 코드에 운동론–MHD 과정을 모두 같은 틀에서 다루는 시뮬레이션 모형을 넣고, 자기 가둠 핵융합 플라즈마의 저주파 파동과 난류 연구용으로 검증했다. 전자와 이온의 질량비가 작다는 점을 이용해 전자 반응을 해석적인 부분과 그렇지 않은 부분으로 나누는 이론 틀을 세웠고, 이 모형은 이론과 시뮬레이션 모두에서 이상 MHD 모형으로 환원될 수 있다. 연구진은 DIII-D 토카막의 내부 꼬임 모드(internal kink mode)를 시뮬레이션해 검증했고, 큰 시뮬레이션 자료로 꼬임 불안정성을 예측하는 대리 모형(surrogate model)을 학습시켰다. 통계 분석에서는 안전 인자 q = 1 자기면의 반경 위치, 압력 기울기, q의 최솟값, q = 1 면 안쪽의 플라즈마 베타가 예측에 가장 중요한 변수였다.[^p3]
대표 논문 4는 공명 자기 섭동을 건 KSTAR 토카막에서 자기섬이 이온 온도 기울기(ITG) 난류에 주는 영향을 자이로운동론 시뮬레이션으로 계산했다. 수송은 ITG 난류와 스스로 생긴 소용돌이 흐름·띠흐름 사이의 비선형 상호작용이 정했고, 요동과 수송은 단면과 토로이달 방향 모두에서 방향에 따라 다른 구조를 보였다. 자기섬은 입자와 열의 난류 수송을 크게 늘렸고, X점이 바깥쪽 중간 평면에 있을 때 X점 근처 공명층을 지나는 수송이 커졌다. 시뮬레이션은 KSTAR 실험과 시간 주파수·수직 파수 스펙트럼에서 정량적으로 맞았다.[^p4]

### 3. 3차원 자기장 배치(스텔러레이터)

누리집은 핵융합 에너지 연구의 주제로 토카막과 스텔러레이터 사이의 숨은 3차원 자기장 배치를 든다.[^home]
대표 논문 5는 준등역학(quasi-isodynamic) 스텔러레이터에서 밀도 기울기가 일으키는 강하게 불안정한 갇힌 전자 모드(trapped electron mode)를 전역 자이로운동론 시뮬레이션으로 찾았다. 고유 모드는 자기장 곡률이 불리하고 자기장이 약하며 갇힌 전자가 많은 토러스 안쪽에 모였다. 불안정성은 실공간의 난류 확산(turbulence spreading)과 불안정한 영역에서 감쇠 영역으로 가는 스펙트럼 전달로 포화했고, 정상 상태의 난류는 큰 입자 흐름을 일으켰다. 연구진은 이 결과가 최적화된 스텔러레이터 반응로에서 핵융합 연료를 가두고 핵융합 재(fusion ash)를 빼내는 일에 의미가 있을 수 있다고 적었다.[^p5]

### 4. 실험 자료 기반 수송 분석

대표 논문 6은 구형 토카막 실험 장치 NSTX(National Spherical Torus Experiment)의 TRANSP 해석 결과로 학습한 전자 열 수송 신경망 모형(ETT-NN)을 개발했다. 합성곱 신경망과 순환 신경망을 함께 써서 난류 수송의 공간·시간 비국소성과 다중 규모 특징을 반영했고, 해석 분석과 예측 시뮬레이션으로 검증했다. 미세 찢김 모드, 갇힌 전자 모드, 운동론적 풍선 모드, 전자 온도 기울기 모드가 나타나는 방전에서 변수를 바꿔 본 결과, 모형은 기존 자이로운동론 시뮬레이션과 이론에서 본 것과 같은 경향을 보였다.[^p6]
대표 논문 7은 KSTAR에서 저가둠–고가둠(L-H) 전이와 외부에서 건 공명 자기 섭동(RMP)에 따른 난류 통계를 분석했다. 전자 밀도, 전자 온도, 폴로이달 자기장의 시간 변화율 요동을 정보 기하 척도(정보율과 정보 길이)와 첨도·분산으로 분석했고, 가장자리 RMP가 결맞은 모드를 억누르면서 간헐성을 키운다는 것을 보였다.[^p7]

## 대표 논문

최경진 교수가 KAIST에 부임한 2024년 뒤 출판된 논문 가운데 논문 기록에 교수 소속이 KAIST로 적혀 있고 초록을 확인할 수 있는 2025–2026년 논문 일곱 편을 연구 갈래별로 골랐다. 1·2번은 교수가 1저자이고, 3–7번은 교수가 중간 저자로 참여한 공동 연구다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [A theory of E × B staircase stability: favorable role of fast ions](https://doi.org/10.1088/1741-4326/ae97f4) · Nuclear Fusion 66 | E × B 흐름의 전단층이 반경 방향으로 늘어선 E × B 계단이, 흐름 분포에서 튀어나온 곳과 파인 곳의 짝이 자라며 저절로 무너지는 것에 맞서 유지되는 조건을 해석 이론으로 구했다. 계단을 유지하는 데 필요한 임계 E × B 전단율은 흐름 성분의 규모에 따라 달라, 규모가 작은 흐름 성분일수록 본래 무너지기 쉬웠다. 모형에 빠른 이온을 넣자 임계 전단율이 크게 낮아졌는데, 빠른 이온 때문에 표류파의 반경 방향 군속도가 줄기 때문이다. 연구진은 빠른 이온이 날카로운 계단 구조를 유지하는 데 유리하게 작용하며, 이 결과가 KSTAR FIRE 모드 플라즈마에서 계단 구조가 오래 유지된 최근 실험 관측과 맞는다고 적었다.[^p1] | 1저자 G.J. Choi(최경진 교수), 3명 |
| 2 | 2026 | [Nonlinear coupling of three zonal flow modes in the Charney–Hasegawa–Mima system](https://doi.org/10.1063/5.0331299) · Physics of Plasmas 33 | 차니–하세가와–미마 방정식에서 띠흐름 세 개의 비선형 결합을 기술하는 방정식을 유도했다. 띠흐름끼리는 직접 상호작용하지 못하지만, 표류파 두 개와 띠흐름 하나가 얽힌 비선형 결합을 거쳐 서로 영향을 줄 수 있다. 연구진은 이 결합의 기본 성질을 잘 알려진 표류파 세 개의 결합과 견주었다. 파장이 가장 짧은 띠흐름은 파수 맞춤 조건을 만족하는 더 긴 파장의 띠흐름 둘로 붕괴하며 포화했다. 연구진은 이런 붕괴가 잇따라 일어나 에너지가 긴 파장 쪽으로 옮겨 가는 단순한 모형을 제안했고, 오랜 시간 뒤에는 요동 에너지 대부분이 계가 허용하는 가장 긴 파장의 띠흐름 세 개에 모인다고 예측했다.[^p2] | 1저자 G. J. Choi(최경진 교수), 마지막 저자 Y.-S. Na (4명) |
| 3 | 2026 | [Formulation and verification of multiscale gyrokinetic simulation of kinetic-MHD processes in toroidal plasmas](https://doi.org/10.1063/5.0313923) · Physics of Plasmas 33 | 핵융합 플라즈마의 저주파 파동과 난류를 계산하는 모형을 구현하고, DIII-D 토카막의 내부 꼬임 불안정성 계산으로 검증했다. 시뮬레이션 자료를 학습한 대리 모형으로 꼬임 불안정성을 예측하고, 예측에 중요한 플라즈마 변수를 분석했다.[^p3] | 1저자 Xishuo Wei, 마지막 저자 Zhihong Lin (14명), 최경진 교수는 3번째 저자 |
| 4 | 2025 | [Gyrokinetic simulations of the effects of magnetic islands on microturbulence in KSTAR](https://doi.org/10.1088/1741-4326/ada049) · Nuclear Fusion 65 | 공명 자기 섭동을 건 KSTAR 토카막에서 자기섬이 이온 온도 기울기(ITG) 난류에 주는 영향을 자이로운동론 시뮬레이션으로 계산했다. 수송은 ITG 난류와 스스로 생긴 소용돌이 흐름·띠흐름 사이의 비선형 상호작용이 정했고, 그 결과 요동과 수송은 폴로이달 단면과 토로이달 방향 모두에서 방향에 따라 다른 구조를 보였다. 자기섬은 입자와 열의 난류 수송을 크게 늘렸다. 난류 수송은 토로이달 방향을 따라 달라졌고, 자기섬의 X점이 바깥쪽 중간 평면에 있을 때 X점 근처 공명층을 지나는 수송이 커졌다. 시뮬레이션은 시간 주파수와 수직 파수 스펙트럼에서 KSTAR 실험과 정량적으로 맞았다.[^p4] | 1저자 Xishuo Wei, 마지막 저자 Dmitri Orlov (11명), 최경진 교수는 3번째 저자 |
| 5 | 2025 | [Trapped electron mode in a quasi-isodynamic stellarator](https://doi.org/10.1088/1741-4326/adf1b7) · Nuclear Fusion 65 | 전역 자이로운동론 시뮬레이션으로 준등역학 스텔러레이터에서 밀도 기울기가 일으키는 강하게 불안정한 갇힌 전자 모드를 찾았다. 고유 모드는 자기장 곡률이 불리하고 자기장이 약하며 갇힌 전자가 많은 토러스 안쪽에 모였다. 불안정성은 실공간의 난류 확산과, 불안정한 영역에서 감쇠하는 영역으로 가는 스펙트럼 전달이라는 비선형 과정으로 포화했다. 정상 상태의 난류는 큰 입자 흐름을 일으켰고, 연구진은 이것이 최적화된 스텔러레이터 반응로에서 핵융합 연료를 가두고 핵융합 재를 빼내는 일에 중요한 의미가 있을 수 있다고 적었다.[^p5] | 1저자 Javier H. Nicolau, 마지막 저자 Zhihong Lin (5명), 최경진 교수는 4번째 저자 |
| 6 | 2025 | [Development of a data-driven neural network model for electron thermal transport in NSTX](https://doi.org/10.1088/1741-4326/adec01) · Nuclear Fusion 65 | 구형 토카막의 전자 열 수송(ETT)을 더 빠르고 정확하게 계산하려고, NSTX의 TRANSP 해석 결과로 학습한 전자 열 수송 신경망 모형(ETT-NN)을 개발했다. 합성곱 신경망과 순환 신경망을 함께 써서, 기존 모형이 제한적으로만 다뤄 온 난류 수송의 공간·시간 비국소성과 다중 규모 특징을 함께 반영했다. 모형은 해석 분석과 Tokamak Reactor Integrated Automated Suite for Simulation and Computation 코드를 쓴 예측 시뮬레이션으로 검증되어 비교적 높은 정확도를 보였다. 미세 찢김 모드, 갇힌 전자 모드, 운동론적 풍선 모드, 전자 온도 기울기 모드가 나타나는 시험 방전에서 변수를 바꿔 본 결과, 모형은 기존 자이로운동론 시뮬레이션이나 이론과 같은 경향을 보이면서 난류 수송의 전역적 성질도 담았다. 연구진은 모형이 무차원 변수를 써서 다른 장치의 자료를 더해 적용 범위를 넓힐 수 있다고 적었다.[^p6] | 1저자 H. Chung, 마지막 저자 Y.-S. Na (7명), 최경진 교수는 3번째 저자 |
| 7 | 2025 | [Turbulence statistical analysis of the L-H transition and RMPs in KSTAR](https://doi.org/10.1088/1361-6587/ae087a) · Plasma Physics and Controlled Fusion 67 | KSTAR에서 저가둠–고가둠(L-H) 전이와 외부에서 건 공명 자기 섭동(RMP)에 따른 난류 통계를 조사했다. 전자 밀도, 전자 온도, 미르노프 코일(자기장의 시간 변화를 재는 코일)로 잰 폴로이달 자기장 시간 변화율의 요동 시계열을 정보 기하 척도(정보율 Γ와 정보 길이 L)와 첨도 κ, 분산 σ²로 분석했다. 밀도가 낮은(n_e ∼ 1.2 × 10^19 m^-3) 플라즈마에서는 L-H 전이 전에 밀도·온도·자기장 요동을 잇는 ∼80 kHz 자기 모드가 나타나, 가장자리 국재 모드(ELM, 플라즈마 가장자리에서 되풀이해 터지는 불안정성)가 있는 H 모드까지 이어졌다. 가장자리 RMP(ERMP)는 이 결맞은 모드를 억누르지만 간헐성을 키워, 시간에 따른 확률 밀도 함수를 갑자기 바꾸는 잦은 분출과 정보율의 큰 급등을 만들었다. 연구진은 정보 기하가 간헐적 사건을 깔끔하게 잡아내고 비평형 확률 분포의 변화를 정량화하며, 공명 자기 섭동이 가장자리 수송과 상관에 주는 영향을 여러 진단 자료에 걸쳐 하나의 간결한 지표로 평가할 수 있다고 정리했다.[^p7] | 1저자 Eun-jin Kim, 마지막 저자 Yong-Su Na (9명), 최경진 교수는 6번째 저자 |

## 교수와 전문 분야

최경진 교수(CHOI, Gyungjin)는 KAIST 원자력및양자공학과 조교수다.[^prof][^dept] 누리집 교수 소개에 따르면 서울대학교에서 원자핵공학(Nuclear Engineering) 학사(2009–2012, 물리학 부전공)와 박사(2012–2019)를 받았다.[^prof] 이어 UC Irvine 물리천문학과(Dept. Physics and Astronomy) 박사후연구원(Postdoctoral Scholar, 2019–2021), 서울대학교 NIFTEP 선임연구원(Senior Researcher, 2021–2022)과 연구조교수(Assistant Research Professor, 2022–2024)를 거쳐 2024년부터 KAIST 원자력및양자공학과 조교수(Assistant Professor)다.[^prof] 학과 교수 소개는 최종학위를 Ph.D. (2019) Seoul National Univ.로 적는다.[^dept]

누리집 교수 소개가 고른 논문(Selected Publications) 다섯 편은 자기섬의 측지 음향 모드(geodesic acoustic mode, 띠흐름이 진동하며 압력 요동을 동반하는 모드) 운동론, 빠른 이온이 띠흐름의 표류파 난류 조절을 강화하는 원리, 토카막 자기섬 주변 소용돌이 흐름의 장기 변화, DIII-D 토카막 저주파 알펜 모드(Alfvénic mode, 자기력선을 따라 전해지는 자기장 요동 파동)의 자이로운동론 시뮬레이션, 3차원 자기장이 일으키는 띠흐름 감쇠를 다룬다.[^prof] 교수가 저자로 참여한 2021–2026년 학술지 논문 목록을 보면 교수의 전문 분야는 토카막 플라즈마의 띠흐름·소용돌이 흐름과 난류, 자기섬, 빠른 이온 효과의 이론과 자이로운동론 시뮬레이션이고, KSTAR와 DIII-D 실험 해석, 스텔러레이터와 장 반전 배치(field-reversed configuration, 플라즈마 전류가 만든 자기장으로 바깥 자기장을 뒤집어 플라즈마를 가두는 배치) 플라즈마의 난류 연구에도 공동 저자로 참여했다.[^cr]

## 응용 분야

누리집은 연구 분야로 핵융합 에너지 연구와 함께 산업·저온 플라즈마와 우주·천체 플라즈마를 든다.[^home] 대표 논문 5는 결과가 최적화된 스텔러레이터 반응로에서 핵융합 연료를 가두고 핵융합 재를 빼내는 일에 의미가 있을 수 있다고 적고,[^p5] 대표 논문 6은 무차원 모형에 다른 장치의 자료를 더해 구형 토카막의 전자 열 수송 특성을 밝히는 데 쓸 수 있다고 적는다.[^p6]

## 구성원

누리집 Students 페이지의 M.S. Students 1명과 Undergraduate Students 1명, 모두 2명이다. Ph.D. Students 구역에는 이름이 적혀 있지 않다. 과정은 구역 이름이고, 이메일은 페이지 표기다.[^students] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Mikhail Angel C. Torio | 석사과정 | mikhail.torio@kaist.ac.kr | 1 |
| 이진규 | 학부 연구생 |  |  |

## 최근 논문 목록 (2021–2026)

최경진 교수가 저자로 참여한 2021–2026년 학술지 논문 33편이다(2026년 6편, 2025년 5편, 2024년 9편, 2023년 5편, 2022년 1편, 2021년 7편). 저자·제목·학술지 표기는 출판사가 등록한 서지를 따랐고, 연도는 첫 출판 연도이며, 연도 안에서는 출판일이 늦은 논문부터 적었다.[^cr] 교수는 2024년 KAIST에 부임했고, 이 목록에는 부임 전 UC Irvine과 서울대학교 시기의 논문이 섞여 있다.[^prof][^cr] 대표 논문 1–7은 논문 기록에 교수 소속이 KAIST로 적힌 논문이다.

**2026**

- Andreas Bierwage, Wonjun Lee, Young-chul Ghim, Panith Adulsiriswad, Nobuyuki Aiba, Seungmin Bong, Gyungjin Choi, Matteo Valerio Falessi, Philipp Lauber, Masatoshi Yagi. "Study of low-frequency core-edge coupling in a tokamak: II. Spatial channeling & focusing in antenna-driven MHD". *Fundamental Plasma Physics 20, 100131 (2026)*.
- Wonjun Lee, Andreas Bierwage, Seungmin Bong, Jaewook Kim, K.D. Lee, J.G. Bak, G.J. Choi, C. Sung, Y.-c. Ghim. "Study of low-frequency core–edge coupling in a tokamak: I. Experimental observation in KSTAR". *Fundamental Plasma Physics 20, 100137 (2026)*.
- G.J. Choi, M.A. Torio, T.S. Hahm. "A theory of E × B staircase stability: favorable role of fast ions". *Nuclear Fusion 66, 106002 (2026)*.
- G. J. Choi, S. J. Park, T. S. Hahm, Y.-S. Na. "Nonlinear coupling of three zonal flow modes in the Charney–Hasegawa–Mima system". *Physics of Plasmas 33, 072302 (2026)*.
- Xishuo Wei, Pengfei Liu, Gyungjin Choi, Guillaume Brochard, Jian Bao, Javier H. Nicolau, Yuehao Ma, Haotian Chen, Handi Huang, Shuying Sun, Yangyang Yu, Ethan Green, Fernando Eizaguirre, Zhihong Lin. "Formulation and verification of multiscale gyrokinetic simulation of kinetic-MHD processes in toroidal plasmas". *Physics of Plasmas 33, 043901 (2026)*.
- Yong-Su Na, S.J. Park, H. Han, Janghyeok Lee, C. Heo, S.C. Hong, C. Sung, D. Kim, J. Kang, Y.H. Lee, J. Chung, T.S. Hahm, B. Kim, J.G. Bak, R. Budny, M.S. Cha, G.J. Choi, M.J. Choi, J. Gwak, S.H. Hahn, J. Jang, K.C. Lee, J.H. Kim, S.K. Kim, W.C. Kim, J. Ko, W.H. Ko, C.Y. Lee, J.H. Lee, J.H. Lee, J.K. Lee, J.P. Lee, K.D. Lee, J.-K. Park, J.M. Park, Y.S. Park, J. Seo, S.M. Yang, S.W. Yoon. "On FIRE mode in KSTAR". *Nuclear Fusion 66, 026049 (2026)*.

**2025**

- Eun-jin Kim, Huiwon Chung, Minjun Choi, Yoonji Lee, Seongjun Han, Gyungjin Choi, Jong Gyu Park, Seong Moo Yang, Yong-Su Na. "Turbulence statistical analysis of the L-H transition and RMPs in KSTAR". *Plasma Physics and Controlled Fusion 67, 105002 (2025)*.
- Javier H. Nicolau, Xishuo Wei, Pengfei Liu, Gyungjin Choi, Zhihong Lin. "Trapped electron mode in a quasi-isodynamic stellarator". *Nuclear Fusion 65, 086049 (2025)*.
- H. Chung, C.Y. Lee, G.J. Choi, S.M. Kaye, B.P. LeBlanc, J.W. Berkery, Y.-S. Na. "Development of a data-driven neural network model for electron thermal transport in NSTX". *Nuclear Fusion 65, 086028 (2025)*.
- Chweeho Heo, SangJin Park, GyungJin Choi, Jaewook Kim, Eun-jin Kim, YoungMu Jeon, Minjun J. Choi, Hyunsun Han, Choongki Sung, TaikSoo Hahm, Yong-Su Na. "Experimental identification of I-mode characteristics at the edge of FIRE mode in KSTAR". *Nuclear Fusion 65, 036003 (2025)*.
- Xishuo Wei, Javier H Nicolau, Gyungjin Choi, Zhihong Lin, Seong-Moo Yang, SangKyeun Kim, WooChang Lee, Chen Zhao, Tyler Cote, JongKyu Park, Dmitri Orlov. "Gyrokinetic simulations of the effects of magnetic islands on microturbulence in KSTAR". *Nuclear Fusion 65, 026026 (2025)*.

**2024**

- Y. Lee, P. Aleynikov, P. C. de Vries, H.-T. Kim, J. Lee, M. Hoppe, J.-K. Park, G. J. Choi, J. Gwak, Y.-S. Na. "Binary Nature of Collisions Facilitates Runaway Electron Generation in Weakly Ionized Plasmas". *Physical Review Letters 133, 175102 (2024)*.
- E.S. Yoon, T.S. Hahm, G.J. Choi, Y.W. Cho, A. Ishizawa, M.J. Choi, J.M. Kwon. "Turbulence spreading induced E × B vortex flow generation in a magnetic island". *Nuclear Fusion 64, 126050 (2024)*.
- P. Liu, X. Wei, Z. Lin, W.W Heidbrink, G. Brochard, G.J. Choi, J.H. Nicolau, W. Zhang. "Cross-scale interaction between microturbulence and meso-scale reversed shear Alfvén eigenmodes in DIII-D plasmas". *Nuclear Fusion 64, 076007 (2024)*.
- D. Kim, S.J. Park, G.J. Choi, Y.W. Cho, J. Kang, H. Han, J. Candy, E.A. Belli, Y.-S. Na, T.S. Hahm, C. Sung. "Investigation of fast ion effects on core turbulence in FIRE mode plasmas". *Nuclear Fusion 64, 066013 (2024)*.
- G. J. Choi. "Kinetic theory of island geodesic acoustic mode". *Physics of Plasmas 31, 042304 (2024)*.
- G. J. Choi. "Theory of self-generated vortex flows in a tokamak magnetic island". *Reviews of Modern Plasma Physics 8, 11 (2024)*.
- Bin Ahn, Yegeon Lim, Hoiyun Jeong, Hae June Lee, Gyung Jin Choi, Y.-C. Ghim. "Charged particle collisionless transport near the X-point of the two-wire model". *Journal of Plasma Physics 90, 975900204 (2024)*.
- SeongMoo Yang, Jong-Kyu Park, YoungMu Jeon, Nikolas C. Logan, Jaehyun Lee, Qiming Hu, JongHa Lee, SangKyeun Kim, Jaewook Kim, Hyungho Lee, Yong-Su Na, Taik Soo Hahm, Gyungjin Choi, Joseph A. Snipes, Gunyoung Park, Won-Ha Ko. "Tailoring tokamak error fields to control plasma instabilities and transport". *Nature Communications 15, 1275 (2024)*.
- Wonjun Tae, E. S. Yoon, Min Sup Hur, G. J. Choi, J. M. Kwon, M. J. Choi. "Unveiling non-flat profiles within magnetic islands in tokamaks". *Physics of Plasmas 31, 020702 (2024)*.

**2023**

- G.J. Choi, P.H. Diamond, T.S. Hahm. "On how fast ions enhance the regulation of drift wave turbulence by zonal flows". *Nuclear Fusion 64, 016029 (2023)*.
- D. Kim, S.J. Park, G.J. Choi, Y.W. Cho, J. Kang, H. Han, J. Candy, E.A. Belli, T.S. Hahm, Y.-S. Na, C. Sung. "Turbulence stabilization in tokamak plasmas with high population of fast ions". *Nuclear Fusion 63, 124001 (2023)*.
- T. S. Hahm, G. J. Choi, S. J. Park, Y.-S. Na. "Fast ion effects on zonal flow generation: A simple model". *Physics of Plasmas 30, 072501 (2023)*.
- G.J. Choi. "Self-generated vortex flows in a tokamak magnetic island with a background flow". *Nuclear Fusion 63, 066032 (2023)*.
- Wonjun Lee, Jaewook Kim, Semin Joung, G. J. Choi, J. Kim, M. Woo, T. Rhee, K. D. Lee, J. G. Bak, J. S. Kang, Y.-C. Ghim. "Non-monotonic radial structures of fluctuating temperatures and densities associated with fishbone activities in KSTAR". *Physics of Plasmas 30, 022502 (2023)*.

**2022**

- G. J. Choi, T. S. Hahm. "Long Term Vortex Flow Evolution around a Magnetic Island in Tokamaks". *Physical Review Letters 128, 225001 (2022)*.

**2021**

- Javier H. Nicolau, Gyungjin Choi, Jingyuan Fu, Pengfei Liu, Xishuo Wei, Zhihong Lin. "Global gyrokinetic simulation with kinetic electron for collisionless damping of zonal flow in stellarators". *Nuclear Fusion 61, 126041 (2021)*.
- X.S. Wei, W.H. Wang, Z. Lin, G.J. Choi, S. Dettrick, C. Lau, P.F. Liu, T. Tajima. "Effects of zonal flows on ion temperature gradient instability in the scrape-off layer of a field-reversed configuration". *Nuclear Fusion 61, 126039 (2021)*.
- W.W. Heidbrink, G.J. Choi, M.A. Van Zeeland, M.E. Austin, G.H. Degrandchamp, D.A. Spong, A. Bierwage, N.A. Crocker, X.D. Du, P. Lauber, Z. Lin, G.R. McKee. "Isotope dependence of beta-induced Alfvén eigenmode (BAE) and low frequency mode (LFM) stability in DIII-D". *Nuclear Fusion 61, 106021 (2021)*.
- S.M. Yang, J.-K. Park, Y.S. Na, Y. In, H. Hahn, J.W. Jeon, J.W. Yoo, W.H. Ko, K.D. Lee, J.H. Lee, J.W. Lee, S.C. Hong, Y.J. Shi, N.C. Logan, Q. Hu, G.J. Choi. "Parametric dependencies of locked mode thresholds in KSTAR L-mode plasmas". *Nuclear Fusion 61, 086009 (2021)*.
- G.J. Choi, P. Liu, X.S. Wei, J.H. Nicolau, G. Dong, W.L. Zhang, Z. Lin, W.W. Heidbrink, T.S. Hahm. "Gyrokinetic simulation of low-frequency Alfvénic modes in DIII-D tokamak". *Nuclear Fusion 61, 066007 (2021)*.
- W H Wang, J Bao, X S Wei, Z Lin, G J Choi, S Dettrick, A Kuley, C Lau, P F Liu, T Tajima. "Effects of equilibrium radial electric field on ion temperature gradient instability in the scrape-off layer of a field-reversed configuration". *Plasma Physics and Controlled Fusion 63, 065001 (2021)*.
- T. S. Hahm, Y. J. Kim, P. H. Diamond, G. J. Choi. "Anisotropic E × B shearing rate in a magnetic island". *Physics of Plasmas 28, 022302 (2021)*.

## 연락과 위치

- 위치: 원자력및양자공학과 N7-1 2402호(학과 교수 소개의 교수 연구실 표기)[^dept]
- 우편 주소: Department of Nuclear and Quantum Engineering, N7-1, 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of KOREA[^home]
- 전화: +82-42-350-3818(교수)[^prof]
- 교수 이메일: gyungjinc@kaist.ac.kr[^prof]
[^p1]: G. J. Choi, M. A. Torio, T. S. Hahm, Nuclear Fusion 66, 106002 (온라인 2026-08-25). <https://doi.org/10.1088/1741-4326/ae97f4> 초록 기준.
[^p2]: G. J. Choi, S. J. Park, T. S. Hahm, Y.-S. Na, Physics of Plasmas 33, 072302 (온라인 2026-07-10). <https://doi.org/10.1063/5.0331299> 초록 기준.
[^p3]: X. Wei 외, Z. Lin, Physics of Plasmas 33, 043901 (온라인 2026-04-06). <https://doi.org/10.1063/5.0313923> 초록 기준.
[^p4]: X. Wei 외, D. Orlov, Nuclear Fusion 65, 026026 (온라인 2025-01-06). <https://doi.org/10.1088/1741-4326/ada049> 초록 기준.
[^p5]: J. H. Nicolau 외, Z. Lin, Nuclear Fusion 65, 086049 (온라인 2025-07-31). <https://doi.org/10.1088/1741-4326/adf1b7> 초록 기준.
[^p6]: H. Chung 외, Y.-S. Na, Nuclear Fusion 65, 086028 (온라인 2025-07-22). <https://doi.org/10.1088/1741-4326/adec01> 초록 기준.
[^p7]: E.-j. Kim 외, Y.-S. Na, Plasma Physics and Controlled Fusion 67, 105002 (온라인 2025-09-29). <https://doi.org/10.1088/1361-6587/ae087a> 초록 기준.
[^home]: 연구실 누리집 첫 화면 <https://sites.google.com/view/kaistftl> (연구실 이름, Research Areas 세 갈래와 주제, 주소, 2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <https://sites.google.com/view/kaistftl/members/professor> (교수 이름·이메일·전화, 경력과 학력, Selected Publications 다섯 편, 2026-10-23 열람)
[^students]: 연구실 누리집 Students 페이지 <https://sites.google.com/view/kaistftl/members/students> (Ph.D.·M.S.·Undergraduate Students 구역, 구성원 2명과 이메일, 2026-10-23 열람)
[^dept]: KAIST 원자력및양자공학과 교수 소개 페이지 <https://nuclear.kaist.ac.kr/people/professor.php> (최경진 조교수 항목의 최종학위, 연구실 위치, 전화, 홈페이지, 이메일, 2026-10-23 열람)
[^deptlab]: KAIST 원자력및양자공학과 연구그룹 페이지 「핵융합 및 플라즈마」 <https://nuclear.kaist.ac.kr/research/the_lap.php?category=003> (핵융합 및 플라즈마 이론 연구실, 조교수 최경진, 2026-10-23 열람)
[^deptlaben]: KAIST 원자력및양자공학과 영문 연구그룹 페이지 「Nuclear Fusion & Plasma」 <https://nuclear.kaist.ac.kr/eng/research/the_lap.php?category=003> (Fusion and Plasma Theory Laboratory, Assistant Professor Choi, Gyungjin, 2026-10-23 열람)
[^cr]: Crossref 출판사 등록 서지 <https://api.crossref.org/> (교수 ORCID 0000-0003-0044-1650이 붙은 2021년 이후 학술지 논문의 저자·제목·학술지·권·쪽·출판일, 2026-10-23 조회)

# 최적 설계 연구실 (AI-based Design Optimization Laboratory, AIDOL)

**KAIST 기계공학과 · 이익진 교수**

- 분야: 불확실성을 고려한 설계(신뢰성 해석·신뢰성 기반 최적설계), 대리 모델과 다중 충실도 모델링, 통계적 모델 보정, 위상 최적화와 인공지능 기반 설계, 제조 공정·제품 설계 최적화 응용
- 대분야: 기계·로봇·제조, 수학·통계
- 태그: 과학·공학 AI[^p1][^p4], 통계적 추론·검정[^area][^p5], 생성 인공지능[^p7], 3D 프린팅[^p8]
- 홈페이지: <http://idol.kaist.ac.kr/>
- 근거와 출처: [최적 설계 연구실 근거 페이지](idol-sources.md)

> 실제 공학 현장에는 시스템 고장을 일으킬 수 있는 불확실성이 많다는 데서 출발해, 신뢰도를 확보하면서 시스템의 기능을 최대로 하는 설계 방법을 연구한다. 계산 비용이 큰 공학 설계에 쓰는 근사 모델, 시험 자료와 모델의 일치를 높이는 통계적 모델 보정, 위상 최적화와 인공지능도 연구 주제로 든다.[^area]

## 무엇을 연구하나

연구실 누리집 첫 화면은 연구실을 KAIST AI-based design optimization lab(AIDOL)으로 소개한다.[^home] 기계공학과 교수 소개는 교수의 연구분야를 Design under uncertainties and applications(불확실성 아래의 설계와 그 응용), Statistical input identification(통계적 입력 식별)으로 적는다.[^meprof] 기계공학과 연구분야 안내는 교수를 소재/역학/제조 분야의 핵심교수로 올리고, 연구주제로 Simulation-based Design under Uncertainty, Statistical Input/Output Identification, Topology Optimization, Surrogate Modeling, Statistical Model Calibration, Reliability Analysis, Analytical Target Cascading을 적는다.[^meres]

연구 분야 페이지(Research Area)는 연구 주제로 신뢰성 기반 최적설계(RBDO, 입력에 불확실성이 있어도 정한 신뢰도를 만족하도록 설계를 최적화하는 방법), 신뢰성 기반 강건 최적설계, 시스템 신뢰성 해석과 최적설계, 정보가 부족한 경우의 불확실성 아래 설계, 입력 변수가 서로 상관된 경우의 불확실성 아래 설계, 병렬 계산을 쓰는 샘플링 기반 RBDO, 대리 모델 생성(메타모델링, 실제 시스템이나 성능을 근사하는 모델을 만드는 일), 통계적 모델 보정과 검증, 다분야 설계 최적화, 위상 최적화, 인공지능의 열한 가지를 든다.[^area]

같은 페이지는 여러 산업에서 불확실성 아래 공학 시스템의 신뢰성이 중요해지면서 소비자의 요구를 만족하는 더 안전하고 믿을 만한 제품 설계가 필요해졌다고 적는다. 이어서 신뢰성 해석, 시장 시스템을 고려한 신뢰성 기반 설계, 통계적 모델 보정, 대리 모델링, 복합재료·구조의 다중 스케일 설계 최적화, 분석적 목표 전개를 글로 설명한다.[^area]

## 주요 연구 주제

### 1. 신뢰성 해석과 신뢰성 기반 최적설계

연구 분야 페이지에 따르면 신뢰성 해석은 제품의 신뢰도를 계산하는 일이고, 그 결과는 신뢰성 기반 최적설계의 확률 제약 조건(고장 확률이 정해진 값을 넘지 않아야 한다는 조건)으로 쓰인다. 신뢰성 해석 방법은 해석적 방법과 시뮬레이션·샘플링 방법으로 나뉜다. 해석적 방법에는 1차 신뢰도법(FORM), 2차 신뢰도법(SORM), 최대 가능 파손점(MPP) 기반 방법이 있고, 샘플링 방법에는 몬테카를로 시뮬레이션(MCS), 중요도 샘플링, 라틴 하이퍼큐브 샘플링이 있다. 연구실은 기존 해석적 방법인 SORM과 차원 감소법(DRM)의 효율과 정확도를 높이는 알고리즘을 연구해 왔다.[^area]

같은 페이지는 시장 시스템을 고려한 신뢰성 기반 설계(RBDMS)도 소개한다. 제조사 관점에서 이익을 최대로 하는 시장 시스템 설계(DMS)는 제품 속성에 대한 소비자 선호를 추정해 시장 점유율과 이익을 계산하는데, 이를 신뢰성 기반 최적설계와 합쳐 신뢰도가 공학 모델과 시장 모델에 함께 주는 영향을 본다.[^area]

최근 논문은 신경망으로 적은 표본에서 목표 신뢰도의 백분위 값을 추정하는 역신뢰성 해석(대표 논문 1)과, 다중 충실도 틀 위에서 적응형 크리깅을 잇달아 적용해 변수가 많은 문제의 고장 확률을 구하는 방법(대표 논문 2)이 있다.[^p1][^p2] 논문 목록에는 시간에 따라 변하는 신뢰성을 심층 가우스 과정으로 해석하는 연구, 가중 신뢰성 기반 최적설계, 여러 시뮬레이션 모델을 쓰는 시스템 신뢰성 기반 최적설계, 신뢰성 기반 최적설계 방법론을 정리한 리뷰도 있다.[^pubs]

### 2. 대리 모델과 다중 충실도 모델링

대리 모델(메타모델)은 실제 시스템이나 성능을 근사하는 모델로, 비선형 해석이나 충돌 해석처럼 계산 비용이 큰 공학 설계 최적화에 쓰인다. 연구 분야 페이지는 표본을 되도록 적게 쓰면서 충분한 정확도를 얻는 것을 목표로 든다. 적은 표본으로 대리 모델을 만드는 방법으로 최소제곱 회귀, 서포트 벡터 회귀, 방사 기저 함수, 크리깅을 들고, 대리 모델의 정확도를 확인하는 검증 기법과 표본을 효율적으로 더하는 순차 샘플링을 함께 적는다.[^area]

최근 논문은 저충실도 자료(정확도가 낮은 모델이나 해석에서 얻은 자료)와 고충실도 자료(정확도가 높은 모델이나 해석에서 얻은 자료)에 서로 다른 선형 임베딩을 두는 코크리깅(대표 논문 3)과, 두 자료의 입력 변수가 서로 다를 때 쓰는 신경망 구조(대표 논문 4)가 있다.[^p3][^p4] 논문 목록에는 함수의 기울기 정보도 함께 쓰는 적응형 크리깅의 새 표본 추출 방법, 재해석 기반 다중 충실도 대리 모델, 저충실도 정보로 실험 계획을 정하는 다중 충실도 대리 모델링 방법도 있다.[^pubs]

### 3. 통계적 모델 보정

연구 분야 페이지는 모델 기반 설계가 이론으로는 자리 잡았지만 산업 적용은 아직 미숙하고, 그 첫째 이유가 모델이 시험을 대신할 만큼 정확한지에 대한 불확실성이라고 적는다. 모델은 실험과 맞지 않는 경우가 많아 보정이 필요하며, 연구실은 시험 자료와 모델의 일치를 높이는 통계적 모델 보정을 최대 우도 추정과 베이즈 갱신으로 수치 예제와 공학 예제에 적용한다.[^area]

최근 논문은 시험 자료가 부족한 환경에서 모르는 모델 변수의 분포를 추정하는 베이즈 모델 보정(대표 논문 5)이 있다.[^p5] 논문 목록에는 우연적 불확실성과 인식적 불확실성 아래의 통계적 모델 보정과 설계 최적화, 서로 상관된 미지 모델 변수의 보정, 준정적 상태(하중을 천천히 가하는 조건)에서 상관관계를 고려한 Johnson-Cook 매개변수(금속이 영구 변형될 때의 저항을 변형 정도·변형 속도·온도로 나타내는 재료 모델의 계수)의 분포 추정 연구도 있다.[^pubs]

### 4. 위상 최적화와 인공지능 기반 설계

연구 분야 페이지는 연구 주제로 위상 최적화와 인공지능을 든다.[^area] 최근 논문은 위치와 방향에 따라 달라지는 기하학적 불확실성을 설계 변수를 둔 점(설계 절점)의 이동으로 모델링한 신뢰성 기반 위상 최적화(대표 논문 6)와, 생성적 적대 신경망으로 목표 성능을 만족하는 타이어 트레드 무늬(타이어가 노면에 닿는 면의 홈 무늬)를 자동으로 만드는 설계 틀(대표 논문 7)이 있다.[^p6][^p7] 논문 목록에는 자료가 적은 환경에서 위상 최적화의 구조 성능을 높이는 딥러닝 틀, 위상 최적화의 초매개변수를 다중 충실도 대리 모델로 최적화하는 연구도 있다.[^pubs]

### 5. 다분야 설계 최적화와 복합재 구조 최적화

연구 분야 페이지에 따르면 자동차 같은 대규모 복합 시스템은 변수와 응답으로 얽힌 여러 계층의 하위 시스템으로 이루어져 한 번에 최적화하기 어렵고, 유한요소 해석 같은 시간이 많이 드는 계산이 필요하다. 그래서 하위 시스템을 따로 최적화하며 서로 조정하는 분해 기반 최적화를 쓰는데, 연구실은 이 조정 전략인 분석적 목표 전개(ATC)를 여러 방식으로 개발·개선해 왔고, 변수의 불확실성을 함께 다루는 ATC를 주요 연구 주제로 든다.[^area]

같은 페이지는 섬유 강화 복합재료와 구조의 다중 스케일 설계 최적화도 소개한다. 제조 공정 제약을 고려하고 비선형 헤비사이드 함수를 써서, 기존 이산 재료 최적화(DMO) 모델보다 최적해의 수렴 속도를 높인 HPDMO 모델을 제안했다고 적는다. 또 적층 복합재를 실제로 쓰려면 구조의 국부 파손 위험을 줄이는 제조 제약 조건을 고려해야 한다는 과제도 적는다.[^area]

### 6. 응용: 제조 공정과 제품 설계

최근 논문은 레이저 분말 베드 융합(LPBF)으로 만드는 Fe–4.5Si 합금(철–규소 합금)의 자기적 성질을 실험 계획법과 기계학습으로 최적화한 연구(대표 논문 8)가 있다.[^p8] 논문 목록에는 열전 발전 시스템의 다중 충실도 설계 최적화, LPBF 얇은 벽 구조의 공정 조건 범위 모델링, 배터리 열관리 시스템의 다목적 최적화, 경계 초소의 감시 카메라 배치 최적화, 스피커 해석 모델의 재료 물성 보정 연구도 있다.[^pubs]

## 대표 논문

이익진 교수가 마지막 저자인 2021–2026년 학술지 논문 가운데 연구 갈래마다 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2022 | [Efficient sampling-based inverse reliability analysis combining Monte Carlo simulation (MCS) and feedforward neural network (FNN)](https://doi.org/10.1007/s00158-021-03144-2) · Structural and Multidisciplinary Optimization | 역신뢰성 해석은 목표 신뢰도가 주어졌을 때 성능 함수(설계가 요구 성능을 만족하는지 나타내는 함수)의 백분위 값을 구하는 일이다. 고차원이거나 비선형성이 강한 성능 함수에는 몬테카를로 시뮬레이션 같은 샘플링 방법이 알맞은 후보로 꼽히지만, 이 방법은 정확한 대신 표본이 많이 필요해 시간이 오래 걸린다. 이 연구는 대리 모델을 쓰지 않는 샘플링 기반 방법을 내놓았다. 성능 분포를 이루는 적은 표본(보통 10–100개)과 그 분포의 실제 백분위 값 사이의 관계를 순방향 신경망(FNN, 입력에서 출력 쪽으로 한 방향으로만 계산이 흐르는 신경망)에 학습시키고, 학습 자료는 여러 베타 분포(정해진 구간 안의 값을 다루는 확률 분포의 한 종류)로 만들었다. 커널 밀도 추정(표본마다 매끄러운 함수를 놓고 더해 분포 모양을 추정하는 방법)과 등간격 점으로 학습 입력의 차원을 없애는 학습 방법도 제안했다. 비교 결과 표본을 그대로 학습한 방법(방법 2)이 표본에 커널 분포를 맞춰 백분위를 바로 구하는 방법(방법 1)보다 정확했고, 커널 밀도 추정과 등간격 점을 쓴 방법(방법 3)은 방법 2보다 정확하고 학습 계산도 효율적이었다. 방법 3은 높은 신뢰도 문제에도 쓸 수 있고, 고차원 문제에서 크리깅 기반 방법보다 정확했다.[^p1] | 1저자 U. Lee, 마지막 저자 이익진 (2명) |
| 2 | 2024 | [Consecutive adaptive Kriging method for high-dimensional reliability analysis based on multi-fidelity framework](https://doi.org/10.1007/s00158-023-03727-1) · Structural and Multidisciplinary Optimization | 고장 확률을 효율적으로 계산하려고 적응형 크리깅 방법이 많이 연구됐지만, 차원의 저주(입력 변수가 많은 고차원 문제에서 나타나는 계산상의 어려움) 때문에 고차원 신뢰성 해석에는 한계가 있다. 이 연구는 다중 충실도 메타모델링에 바탕을 둔 연속 적응형 크리깅 틀을 내놓았다. 첫 단계에서는 단변량 표본(변수를 하나씩만 바꿔 뽑은 표본)으로 1차 고차원 모델 표현(HDMR, 여러 변수의 함수를 각 변수만의 함수들의 합으로 나타내는 근사)에 적응형 크리깅을 적용하고, 이 표본으로 혼합 HDMR 모델을 만든다. 둘째 단계에서는 혼합 HDMR을 저충실도 모델로 삼아 계층 크리깅 모델(저충실도 모델을 바탕에 두고 고충실도 자료로 고쳐 나가는 크리깅)을 만들고 다변량 표본(여러 변수를 함께 바꿔 뽑은 표본)으로 적응형 크리깅을 수행한다. 다변량 표본은 저충실도 모델을 보정하는 고충실도 표본으로 쓰이면서 혼합 HDMR의 혼합 매개변수도 추정해, 모델이 문제의 종류에 맞춰지게 한다. 수치 예제와 공학 응용에서 정확한 고장 확률을 효율적으로 구했다.[^p2] | 1저자 Y. Park, 마지막 저자 이익진 (2명) |
| 3 | 2026 | [Linear embedding-enhanced co-Kriging incorporating distinct projection matrices across fidelity levels](https://doi.org/10.1115/1.4071406) · Journal of Mechanical Design | 다중 충실도 모델링은 정확도가 다른 자료를 합쳐 고충실도 해석의 높은 계산 비용을 줄인다. 기존 방법 대부분은 저충실도와 고충실도 자료에 같은 저충실도 임베딩 함수(입력 변수를 다른 좌표 공간으로 옮겨 나타내는 함수)를 적용할 수 있다고 가정하지만, 실제 문제에서는 이 가정이 자주 깨진다. 그러면 고충실도에만 있는 응답 특성이 무시되고, 고충실도 응답을 예측할 때 맞지 않는 저충실도 점을 참고해 정확도가 떨어질 수 있다. 이 연구는 두 자료에 서로 다른 선형 임베딩 함수를 두는 선형 임베딩 강화 코크리깅(LECOK)을 제안했다. 두 임베딩을 모두 넣은 커널(두 점이 얼마나 닮았는지 계산하는 함수)로 공분산 행렬(변수들이 함께 변하는 정도를 모은 행렬)을 만들고, 적은 고충실도 표본으로 고충실도 임베딩 함수를 추정하는 어려움을 덜려고 슈티펠 다양체(Stiefel manifold, 열 벡터들이 서로 수직인 단위 벡터로 이루어진 행렬들의 집합) 위의 최적화를 썼다. 저충실도와 고충실도 임베딩 함수가 닮은 정도에 맞춰 적용 범위를 넓혔고, 수치 예제와 공학 예제로 보였다.[^p3] | 1저자 Y. Park, 마지막 저자 이익진 (3명) |
| 4 | 2024 | [Modified structure of deep neural network for training multi-fidelity data with non-common input variables](https://doi.org/10.1115/1.4064782) · Journal of Mechanical Design | 다중 충실도 대리 모델은 저충실도·고충실도 자료로 공학 성능을 예측하는 모델을 효율적으로 만든다. 딥러닝을 쓴 다중 충실도 신경망 구조도 나왔지만, 기존 구조는 두 자료의 입력 변수가 같다고 가정하며 실제 공학 시스템에서는 그렇지 않은 경우가 많다. 이 연구는 입력 변수가 다른 다중 충실도 자료를 위한 복합 신경망 구조를 내놓았다. 저충실도와 고충실도 자료의 입력 변수를 잇는 입력 매핑 신경망을 넣어, 두 변수의 물리적 관계를 몰라도 전체 모델을 학습하면서 함께 학습되게 했고, 이를 위한 손실 함수(학습 중 예측과 정답의 차이를 재는 함수)와 활성 변수를 제안했다. 수학 예제와 타이어 성능에 관한 공학 문제에서 대부분 기존 대리 모델보다 정확했고, 비선형 함수나 이산적인 함수(값이 연속으로 이어지지 않고 끊어진 함수)의 대리 모델에 유리했다.[^p4] | 1저자 H. Jo, 마지막 저자 이익진 (5명) |
| 5 | 2022 | [A bayesian model calibration under insufficient data environment](https://doi.org/10.1007/s00158-022-03196-y) · Structural and Multidisciplinary Optimization | 신뢰성 기반 최적설계로 제품을 개발하려면 모르는 모델 변수의 불확실성을 밝혀야 하지만, 비용과 시간 때문에 시험 자료가 부족한 경우가 많다. 이 연구는 자료가 부족한 환경에서 역 불확실성 정량화, 곧 통계적 모델 보정을 정확하고 효율적으로 하는 방법을 베이즈 모델 보정 틀 위에 내놓았다. 먼저 출력(부품) 시험 자료로 사전 분포(자료를 반영하기 전에 세운 확률 분포)를 예측한다. 이때 최대 우도 추정으로 통계 매개변수와 분포 종류를 구하고, 피셔 정보 행렬(자료가 매개변수에 대해 담은 정보의 양을 나타내는 행렬)로 추정한 매개변수의 분산을 계산한다. 다음으로 입력(쿠폰, 곧 재료 시편) 시험 자료를 반영한 우도(주어진 매개변수 아래에서 관측 자료가 나올 가능성)와 사전 분포를 베이즈 정리로 합쳐 사후 분포(자료를 반영해 고친 확률 분포)를 예측한다. 이렇게 각각으로는 부족한 시험 자료를 함께 써서 자료 부족 문제를 다루고, 수학·공학 예제로 검증했다.[^p5] | 1저자 J. Choo, 마지막 저자 이익진 (3명) |
| 6 | 2022 | [Modeling of geometric uncertainties in topology optimization via the shift of design nodes](https://doi.org/10.1007/s00158-022-03277-y) · Structural and Multidisciplinary Optimization | 실제 환경에서 기계 구조물은 위치나 방향에 따라 달라지는 기하학적 불확실성을 겪어 성능이 떨어질 수 있다. 이 연구는 절점 설계 변수를 쓰는, 기하학적 불확실성 아래의 신뢰성 기반 위상 최적화 틀을 내놓았다. 절점 밀도 기반 위상 최적화는 절점 밀도를 거리에 따라 보간한 밀도장(각 위치에 재료가 있는 정도를 나타내는 분포)으로 구조 배치를 나타내는데, 불확실성에 따른 기하 변화를 설계 절점의 이동과 그에 따른 밀도장의 섭동으로 모델링했다. 절점 이동의 방향과 크기는 카루넨-뢰브 전개(확률장을 서로 상관없는 확률 변수와 함수의 곱의 합으로 나타내는 방법)로 이산화한 확률장(위치마다 값이 확률적으로 달라지는 양)과 밀도장의 유사 기울기 함수로 정한다. 이 모델로 이중 루프 신뢰성 기반 위상 최적화 문제를 세우고, 순차 최적화·신뢰성 평가 방법(최적화와 신뢰성 평가를 번갈아 하는 방법)으로 분리한 뒤 민감도(설계 변수가 바뀔 때 결과가 바뀌는 정도)를 해석적으로 유도했다. 공간과 방향에 따라 고르지 않은 불확실성을 포함한 수치 예제로 검증했다.[^p6] | 1저자 J. Kim, 마지막 저자 이익진 (2명) |
| 7 | 2022 | [Deep generative tread pattern design framework for efficient conceptual design](https://doi.org/10.1115/1.4053469) · Journal of Mechanical Design | 타이어 트레드 무늬는 자동차 성능에 직접 영향을 준다. 기존 개발 과정에서 개념 설계(제품의 대략적인 형태와 구성을 정하는 초기 설계) 단계는 설계자와 엔지니어가 손으로 주고받는 반복 작업 때문에 시간이 오래 걸리고, 최악의 경우 처음부터 다시 해야 한다. 이 연구는 목표 타이어 성능을 만족하는 여러 트레드 무늬를 개념 설계 단계에서 자동으로 만드는 심층 생성 설계 틀을 내놓았다. 생성 모델과 타이어 성능 평가 함수를 합친 함수를 최적화해 원하는 무늬를 얻는다. 이를 위해 트레드 무늬 분야 지식을 바탕으로 이미지 전처리, 생성적 적대 신경망(GAN), 2차원 이미지 기반 성능 평가 함수, 설계 생성·탐색, 이미지 후처리 방법을 제안했다. 수치 결과에서 여름용·겨울용·사계절용 같은 목표 성능을 만족하는 여러 트레드 무늬를 만들었다.[^p7] | 1저자 M. Lee, 마지막 저자 이익진 (6명) |
| 8 | 2025 | [Efficient Optimization of Magnetic Properties of Fe–4.5 Si Alloy in Laser Powder Bed Fusion (LPBF)](https://doi.org/10.1007/s40684-024-00683-z) · International Journal of Precision Engineering and Manufacturing-Green Technology | 기존 연구는 상대 밀도(재료의 이론 밀도에 대한 실제 밀도의 비율)와 기계적 성질을 높이는 최적 공정 변수를 찾았지만, 반복 실험 때문에 실험 비용이 컸다. 이 연구는 두 가지 실험 계획법과 기계학습 알고리즘으로 Fe–4.5Si 소재의 자기적 성질을 최적화하는 효율적인 틀을 내놓았다. 틀은 세 단계로, (1) 정육면체 시편으로 높은 상대 밀도를 보장하는 공정 변수 영역을 찾고, (2) 토로이드(고리 모양) 시편으로 최대 비투자율(재료의 투자율을 진공의 투자율로 나눈 값)과 철손(자기장이 바뀔 때 철심에서 열로 잃는 에너지) 같은 자기적 성질을 예측하는 대리 모델을 만들고, (3) 이 대리 모델과 다목적 유전 알고리즘(MOGA, 여러 후보 해를 교배·변이시키며 여러 목표의 절충안을 찾는 최적화 방법)으로 자기적 성질을 다목적 최적화한다. 적은 실험으로 공정 변수를 효율적으로 최적화할 수 있었고, 이 틀은 연구 초기에 특정 소재에 대한 사전 지식이 없어도 다른 소재에 적용할 수 있다.[^p8] | 1저자 B. U. Song, 마지막 저자 이익진 (7명) |

## 교수와 전문 분야

이익진 교수는 KAIST 기계공학과 교수다.[^meprof][^melist] 연구실 Professor 페이지에 따르면 교수는 서울대학교에서 기계공학 학사(1993–2001)와 석사(2001–2003)를, University of Iowa에서 기계공학 박사(2003–2008)를 받았다. University of Iowa에서 연구조교(2003–2008)·강의조교(2006–2007), 박사후연구원(2008.8–2011.7), Adjunct Professor(2010.7–2011.7)를 지냈고, University of Connecticut 조교수(2011.8–2013.7)를 거쳐 KAIST 조교수(2013.8–2017.8), 부교수(2017.9–2021.2), 교수(2021.3–)가 됐다.[^prof]

같은 페이지는 수상으로 ISSMO/Springer Prize for a young scientist(International Society of Structural and Multidisciplinary Optimization, 2009), 대한기계학회 CAE 및 응용역학 부문 유망과학기술자(2014), KSCM Young Investigator Award(2017), KAIST Outstanding teaching award(ME5895 Probabilistic Engineering Design, 2017년 봄), KSME CAE & Applied Mechanics Young Investigator Award(2018)를 적고, Marquis Who's Who in America 64판(2010)에 실렸다고 적는다. 교수는 Trans. Korean Soc. Mech. Eng. A(대한기계학회논문집 A)의 Associate Editor(2014–)를 맡고 있고, 여러 국제 학회의 조직·학술 위원회에 참여했다.[^prof]

교수의 박사 학위 논문은 단변량 차원 감소법을 쓴 신뢰성 기반 최적설계와 강건 최적설계(입력의 흔들림에 따른 성능 변동을 줄이도록 하는 설계)를 다뤘다(University of Iowa, 2008).[^pubpage] 기계공학과 교수 소개는 교수의 연구분야를 Design under uncertainties and applications, Statistical input identification으로 적는다.[^meprof] 논문으로 보면 최근의 전문 분야는 신뢰성 해석(대표 논문 1, 2), 다중 충실도 대리 모델(대표 논문 3, 4), 통계적 모델 보정(대표 논문 5), 신뢰성 기반 위상 최적화와 생성 모델 기반 설계(대표 논문 6, 7), 제조 공정 최적화(대표 논문 8)다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

기계공학과 연구분야 안내는 교수 연구의 주요 응용 산업으로 자동차와 제조업을 든다.[^meres] Projects 페이지의 진행 중 과제는 과학기술정보통신부의 피지컬AI 기반 협업지능 Sim-to-Real 통합 플랫폼 기술 개발(2026.08–2030)과 4대 과학기술원 InnoCORE 연구단 「AI 기반 지증형 설계-제조 통합 연구단 (PRISM-AI)」(2025.08–2029), 스퀘어네트의 소량 다품종 유제품 품질 관리를 위한 AI 기반 제조공정 최적화(2025–2029), HD현대중공업의 PINN(물리 법칙을 학습에 반영한 신경망) 기반 연료공급 이중관 응력·진동 예측(2026.04–2026.12), SK hynix의 강화학습을 이용한 Mask Fab 자동화 스케줄링(2026.05–2026.12)이다. 끝난 과제 가운데 2021년 이후까지 이어진 것에는 타이어 스타일링 패턴 자동 생성과 해석 예측력 향상(한국타이어앤테크놀로지), 시스템 강도 성능 예측과 다중 충실도 모델 개발(현대엔지비), 감시정찰 센서 조합·배치 최적화(LIG넥스원), 다목적 기동지원 로봇 최적화 설계(육군본부), 산업체 다원 폐열 재생 열전발전 시스템 개발·실증(에너지기술평가원), 직접 공기 포집(DAC, 공기 중 이산화탄소를 바로 잡아내는 기술) 공정 설계(Saudi Aramco – KAIST CO2 Management Center) 과제가 있다.[^projects]

Academic news 게시판에는 교수가 발표자로 나선 KAIST 산학협동 공개강좌 세 차례(2024–2026년)와 KAIST-한온시스템 「인공지능과 최적설계」(2023년)가 올라 있고, 강좌 제목은 인공지능을 활용한 해석 예측과 설계 최적화를 다룬다.[^seminar] 논문 목록에는 열전 발전 시스템, 배터리 열관리 시스템, LPBF 공정, 경계 초소의 감시 카메라 배치, 스피커 해석 모델에 설계 최적화와 모델 보정을 적용한 연구가 있다.[^pubs]

## 구성원

누리집 Members 메뉴의 박사후연구원(Post-docs) 3명, 박사과정(Ph.D. students) 12명(Full Time 8명, Part Time 4명), 석사과정(M.S. students) 8명, 모두 23명이다. 「시작」은 각 카드에서 지금의 과정·직위가 시작된 연월이고, 박사후연구원 Mingyu Lee는 KAIST Mechanical Engineering Research Institute 박사후 경력이 시작된 연월이다. 과정 칸의 괄호는 카드가 적은 소속(Division of Future Vehicle, Department of AX)이나 시간제(Part Time) 표기다. 「연구 주제」는 카드의 Research area 줄이고, 이메일은 카드에 적힌 학교 주소만 실었다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^postdocs][^phd][^ms]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Mingyu Lee (이민규) | 박사후연구원 | 2023.9 | Advanced data-driven modeling, structural optimization, and artificial intelligence (AI) | mglee91@kaist.ac.kr | 3, 7 |
| Qi Su | 박사후연구원 | 2026.2 | Marine renewable energy, Slender structures, Flexible risers and cables, AI-based design optimization, Statistics | suqi@kaist.ac.kr |  |
| Jianhao Fang | 박사후연구원 | 2026.4 | Digital Twin, Artificial Intelligence, Reduced Order Modeling, Design Under Uncertainty, Wind Energy |  |  |
| Jonghyun Kim (김종현) | 박사과정 | 2019.9 | Topology optimization | opdotcom@kaist.ac.kr | 6 |
| Chulhyun Hwang (황철현) | 박사과정 | 2022.9 | Thermoelectric module and electric vehicle thermal management system | jub29@kaist.ac.kr |  |
| Byeong Uk Song (송병욱) | 박사과정 | 2023.3 | Modeling and optimization | busong@kaist.ac.kr | 4, 8 |
| Geonwoo Lee (이건우) | 박사과정 | 2023.3 | Topology optimization and artificial intelligence (AI) | rjsdn1979@kaist.ac.kr |  |
| Juyoung Lee (이주영) | 박사과정 | 2023.3 | Multi-fidelity surrogate modeling | 2ju02@kaist.ac.kr |  |
| Jaeyoung Jeong (정재영) (Lab Representative) | 박사과정 | 2024.3 |  | jjy4321@kaist.ac.kr |  |
| Ji-Hwan Park (박지환) | 박사과정 | 2025.3 | Topology optimization | p3533010@kaist.ac.kr |  |
| Seung-Gyu Lim (임승규) | 박사과정 | 2026.3 | Modeling and optimization | dlatmdrb77@kaist.ac.kr |  |
| Yun-Seog Nam (남윤석) | 박사과정 (Part Time) | 2015.3 |  | indy11@kaist.ac.kr |  |
| Sang-Min Kim (김상민) | 박사과정 (Part Time) | 2018.3 |  |  |  |
| Hwan-Ho Lee (이환호) | 박사과정 (Part Time) | 2019.03 |  | whiteleo@kaist.ac.kr |  |
| Yoon-Yi Hwang (황윤이) | 박사과정 (Part Time) | 2020.9 |  | hyn1014@kaist.ac.kr |  |
| Sohyun Lee (이소현) | 석사과정 | 2025.3 |  | lshyun224@kaist.ac.kr |  |
| Agil Pramudya Kaswiyanto | 석사과정 | 2025.3 |  | agilpramudya@kaist.ac.kr |  |
| Changjun Lee (이창준) | 석사과정 | 2025.3 |  | ericlee8@kaist.ac.kr |  |
| Jihui Moon (문지희) | 석사과정 | 2025.9 |  | jh.moon@kaist.ac.kr |  |
| Dongjun Han (한동준) | 석사과정 | 2025.9 |  | 1223han@kaist.ac.kr |  |
| Jaeyun Kim (김재윤) | 석사과정 (Division of Future Vehicle) | 2026.3 |  | maximkim2@kaist.ac.kr |  |
| Suyeon Yoon (윤수연) | 석사과정 (Department of AX) | 2026.9 |  | suyeonyoon@kaist.ac.kr |  |
| Hyojoon Kim (김효준) | 석사과정 (Department of AX) | 2026.9 |  | jkim720@kaist.ac.kr |  |

## 졸업생과 이전 구성원

누리집 Alumni 페이지의 31명이다. Post doc. 구역 1명, Ph.D 구역 14명, M.S 구역 16명이며, Ph.D 구역의 Yuwei Shi는 카드에 방문 연구(Visiting research Ph.D) 기간이 적힌 사람이다. 학위 칸은 각 카드 첫 줄의 학위·과정 표기이고, 기간은 그 줄에 적힌 연월이다. 진로 칸은 카드의 Current position 줄이며, 그 줄이 없는 카드는 비워 두었다. Yong kook-Kim의 카드에는 기간이 적혀 있지 않다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Zunyi Duan | Postdoc in Mechanical Engineering, KAIST (2017.4–2019.2) | Northwestern Polytechnical University |
| Yuwei Shi | Visiting research Ph.D (2025.9–2026.9) |  |
| Youngseo Park (박영서) | Ph.D in Mechanical Engineering, KAIST (2022.3–2026.8) | 한국에너지기술연구원 (KIER) |
| Minjik Kim (김민직) | Ph.D in Mechanical Engineering, KAIST (2021.3–2025.8) | Samsung Electronics |
| Seonghyeok Yang (양성혁) | Ph.D in Mechanical Engineering, KAIST (2020.3–2024.2) | 국방과학연구소 (ADD) |
| Hwisang Jo (조휘상) | Ph.D in Mechanical Engineering, KAIST (2019.3–2024.2) | Samsung Electronics |
| Jeonghwan Choo (추정환) | Ph.D in Mechanical Engineering, KAIST (2017.8–2023.8) | HL Mando |
| Jeongwoo Park (박정우) | Ph.D in Mechanical Engineering, KAIST (2018.3–2023.2) | Hyundai Motor Company (HMC) |
| Ungki Lee (이웅기) | Ph.D in Mechanical Engineering, KAIST (2018.3–2022.2) | 고려대학교 세종캠퍼스 조교수 |
| Yongsu Jung (정용수) | M.S./Ph.D Integrated in Mechanical Engineering, KAIST (2016.3–2022.2) | 홍익대학교 세종캠퍼스 조교수 |
| Seongmin Pae (배성민) | Ph.D in Mechanical Engineering, KAIST (2014.9–2022.2) | 한온시스템 |
| Jaeeun Yoo (유재은) | Ph.D in Mechanical Engineering, KAIST (2015.3–2021.2) | 국방과학연구소 (ADD) |
| Kyeonghwan Kang (강경환) | Ph.D in Mechanical Engineering, KAIST (2016.3–2020.8) | Samsung Electronics |
| Kyungeun Lee (이경은) | Ph.D in Mechanical Engineering, KAIST (2015.3–2019.8) | SK Hynix |
| SangHyeon Choi (최상현) | Ph.D in Mechanical Engineering, KAIST (2013.3–2018.8) | 한국항공우주연구원 (KARI) |
| Ji-Ung Choi (최지웅) | M.S in Mechanical Engineering, KAIST (2023.3–2025.2) | 솔루엠 |
| Ji-Hwan Jang (장지환) | M.S in Mechanical Engineering, KAIST (2023.3–2025.2) | Hyundai Mobis |
| Hyeon-woo Ryu (류현우) | M.S in Mechanical Engineering, KAIST (2022.9–2024.8) |  |
| Sania Shujaat | M.S in Mechanical Engineering, KAIST (2022.9–2024.8) |  |
| Sung-Won Cho (조성원) | M.S in Mechanical Engineering, KAIST (2022.3–2024.2) | KAIST ME doctoral degree |
| Oliviero Cazzaniga | M.S in Mechanical Engineering, KAIST (2021.7–2024.2) |  |
| Minwoo Kim (김민우) | M.S in Mechanical Engineering, KAIST (2020.3–2022.2) | Hyundai Motor Company (HMC) |
| Sunghyun Jeon (전승현) | M.S in Mechanical Engineering, KAIST (2020.3–2022.2) | Hyundai Motor Company (HMC) |
| Hye-Won Choi (최혜원) | M.S in Division of Future Vehicle, KAIST (2019.9–2021.08) | Hyundai Motor Company (HMC) |
| Yong kook-Kim (김용국) | M.S in Mechanical Engineering, KAIST |  |
| Kwang-soo Park (박광수) | M.S in Mechanical Engineering, KAIST (2017.9–2020.2) | KAIST AI doctoral degree |
| Jong-min Lee (이종민) | M.S in Mechanical Engineering, KAIST (2016.3–2018.2) | 배달의민족 |
| Dong-Hee Lee (이동희) | M.S in Mechanical Engineering, KAIST (2015.3–2017.2) | Hyundai Motor Company (HMC) |
| Joon-Ho Song (송준호) | M.S in Mechanical Engineering, KAIST (2014.9–2016.8) | 한국항공우주(KAI) |
| Kwang-Won Lee (이광원) | M.S in Mechanical Engineering, KAIST (2014.3–2016.2) |  |
| Seongbin Kang (강성빈) | M.S in Mechanical Engineering, KAIST (2014.3–2016.2) | Hyundai Motor Company (HMC) |

## 최근 논문 목록 (2021–2026)

누리집 Publication 메뉴의 세 목록(Papers in Technical Journals (International), International Conference Proceedings, Domestic Conference Proceedings) 가운데 2021–2026년 연도 구역의 87편이다. 학술지 논문 69편(2021–2026년), 국제 학회 발표 8편(2021–2023년), 국내 학회 발표 10편(2021년)이고, 학회 발표는 끝에 (국제 학회)·(국내 학회)를 붙였다. 국제·국내 학회 목록에는 각각 2023년, 2021년 뒤의 연도 구역이 없다. 저자 표기, 제목, 학술지·학회와 권·쪽은 누리집 그대로다. 2021년 구역에는 2021년 10월 전에 나온 논문과 발표도 들어 있다.[^pubs]

**2026**

- Park, J., Lee, M., & Lee, I. (2026). Outlier-aware multi-fidelity surrogate-based hyperparameter optimization for topology optimization. Computers & Structures, 333, 108476.
- Park, Y., Lee, M., & Lee, I. (2026). Linear embedding-enhanced co-Kriging incorporating distinct projection matrices across fidelity levels. Journal of Mechanical Design, 148(9), 091707.
- Yan, J., Liu, X., Lu, H., Zhou, X., Lee, I., & Su, Q. (2026). Deep learning-driven layout optimization of the floating offloading hose under multiple correlated wind-wave sea states. Ocean Engineering, 364, 127011.
- Jung, Y., Park, Y., & Lee, I. (2026). Non-hierarchical multi-output multi-fidelity Gaussian processes using a structure-aware composite kernel. Knowledge-Based Systems, 116634.
- Lee, Y. J., Hwang, C., Lee, H., Lee, I., & Kim, S. J. (2026). Highly energy-efficient manifold microchannel for cooling electronics with a coefficient of performance over 100,000. Energy Conversion and Management, 358, 121422.
- Shi, Y., Lin, C., Lee, M., Shen, J., Lee, I., & Ma, Y. (2026). An efficient reliability-based design optimization approach based on probability quantile estimation and structural constraint integration. Computers & Industrial Engineering, 112102.
- Shi, Y., Lee, I., Hu, W., Wan, L., & Ma, Y. (2026). Efficient time-variant reliability analysis through parallel adaptive Gaussian process modeling based on look-ahead sampling strategy. Reliability Engineering & System Safety, 112734.
- Yan, J., Hu, W., Zhang, T., Cheng, S., Zhao, F., Fang, J., … & Lee, I. (2026). Multi-Target-Reliability-Based Design Optimization: A New RBDO Method Considering Multiple Target Reliabilities Simultaneously. Journal of Mechanical Design, 1-43.
- Jung, Y., Lee, U., & Lee, I. (2026). An integrated framework for reliability analysis and design optimization using input, simulation, and experimental data: Confidence-based design optimization under aleatory and epistemic uncertainty. Reliability Engineering & System Safety, 111895.
- Park, Y., Song, B. U., Choi, J. P., Lee, P. H., Jung, Y., & Lee, I. (2026). Advanced non-hierarchical co-Kriging using latent map multi-output Gaussian process. Applied Mathematical Modelling, 116573.
- Jung, Y., Lee, M., & Lee, I. (2026). Data-driven Time-variant Reliability Analysis using Deep Gaussian Processes. Reliability Engineering & System Safety, 112395.
- Shi, Y., Lee, I., Lin, C., & Ma, Y. (2026). Stepwise Error Reduction: A Novel Look-Ahead Learning Strategy for Accelerating System Reliability Assessment. IEEE TRANSACTIONS ON RELIABILITY, 75, 218-232.
- Lee, M., Lee, J., Song, B. U., & Lee, I. (2026). A novel low-fidelity-guided design of experiments for multi-fidelity surrogate modeling. Advanced Engineering Informatics, 69, 104076.
- Lee, G., Lee, M., & Lee, I. (2026). Domain-embedded deep learning frameworks for topology optimization: Enhancing structural performance under data scarce environments. Advances in Engineering Software, 212, 104064.
- Lee, M., Lee, J., Choi, J. H., Kim, N. H., & Lee, I. (2026). A novel adaptive quality-based multi-fidelity surrogate framework for multiple low-fidelity data sources. Advanced Engineering Informatics, 69, 103973.
- Hu, W., Liao, J., Yan, J., Fang, J., Zhao, F., Lee, I., & Tan, J. (2026). Spatiotemporal-Dependent Reliability Analysis with Adaptive Sampling Physics-Informed Neural Networks. Reliability Engineering & System Safety, 111560.

**2025**

- Cho, H., Kim, M., Park, Y., Lee, H., Lee, I., & Ryu, S. (2025). Comparative study of Gaussian process and additive Gaussian process for multi-objective optimization in air-cooled battery thermal management systems. Journal of Mechanical Science and Technology, 1-12.
- Park, Y., Park, J., Tran, Q. D., Lee, I., & Jang, G. W. (2025). Global-Local Search for Topology Optimization of Linkage Mechanisms Using Spring-Connected Link Model. Journal of Mechanical Design, 1-31.
- Gasmi, K., Djeddou, F., & Lee, I. (2025). Advanced sequential optimization and reliability assessment (ASORA) method for reliability-based design optimization of helical gear pair design. Structural and Multidisciplinary Optimization, 68(10), 1-21.
- Zhang, T., Hu, W., Zhao, F., Yan, J., Tang, N., Lee, I., & Tan, J. (2025). Long-Term Extreme Response Evaluation of Stochastic Models Using Adaptive Stochastic Importance Sampling. Reliability Engineering & System Safety, 111028.
- Song, B. U., Choi, J. P., Lee, P. H., Jung, M. K., Shin, D., Ha, T., & Lee, I. (2025). Efficient Optimization of Magnetic Properties of Fe–4.5 Si Alloy in Laser Powder Bed Fusion (LPBF). International Journal of Precision Engineering and Manufacturing-Green Technology, 1-14.
- Lee, M., Jeong, M. G., Lee, J., Lee, B. J., & Lee, I. (2025). Efficient and robust thermal battery design optimization leveraging physically similar data. Applied Thermal Engineering, 126009.
- Ahmed, F., Picard, C., Chen, W., Mccomb, C., Wang, P., Lee, I., … & Menzel, S. (2025). Datasets in Engineering Design. Journal of Mechanical Design, 1-8.
- Jeong, J., Lee, M., Yang, S., Baek, S., Park, B., Kim, D., & Lee, I. (2025). Optimization framework for surveillance camera layouts considering infiltration routes in general outposts (GOPs). Expert Systems with Applications, 263, 125804.

**2024**

- Gu, J., Jung, Y., Ahn, J., Ahn, J., Choi, J., Kang, B., … , Lee, I. & Park, I. (2024). Auxetic Kirigami Structure-Based Self-Powered Strain Sensor with Customizable Performance using Machine Learning. Nano Energy, 110124.
- Kim, M., Kook, J., Andersen, P. R., & Lee, I. (2024). An automated framework for material property calibration in loudspeaker simulation model. Advances in Engineering Software, 197, 103748.
- Song, Y. U., Song, B. U., Jung, M. K., Lee, C., Choi, J. P., & Lee, I. (2024). Multi-fidelity Gaussian process modeling of a thin-walled structure for laser powder bed fusion (LPBF) process window. Journal of Manufacturing Processes, 127, 107-114.
- Jung, Y., Kim, M., Cho, H., Hu, W., & Lee, I. (2024). Confidence-based design optimization using multivariate kernel density estimation under insufficient input data. Probabilistic Engineering Mechanics, 103702.
- Jo, H., Song, B. U., Huh, J. Y., Lee, S. K., & Lee, I. (2024). Modified structure of deep neural network for training multi-fidelity data with non-common input variables. Journal of Mechanical Design, 146, 101702-1.
- HU, Weifei, et al. Reliability-based design optimization: a state-of-the-art review of its methodologies, applications, and challenges. Structural and Multidisciplinary Optimization, 2024, 67.9: 168.
- Lee, M., Jung, Y., Hwang, C., Kim, M., Kim, M., Lee, U., & Lee, I. (2024). An efficient multi-fidelity design optimization framework for a thermoelectric generator system. Energy Conversion and Management, 315, 118788.
- Choo, J., Jung, Y., Jo, H., & Lee, I. (2024). Statistical model calibration of correlated unknown model variables through identifiability improvement. Probabilistic Engineering Mechanics, 103670.
- Lee, J., Lee, M., Lee, B. J., & Lee, I. (2024). A comprehensive multi-fidelity surrogate framework based on Gaussian process for datasets with heterogeneous responses. Knowledge-Based Systems, 111827.
- Yang, B., Wang, X., Cheng, C., Lee, I., & Hu, Z. (2024, May). Surrogate model-based method for reliability-oriented buckling topology optimization under random field load uncertainty. In Structures (Vol. 63, p. 106382). Elsevier.
- Acar, E., Jain, N., Ramu, P., Hwang, C., & Lee, I. (2024). A survey on design optimization of battery electric vehicle components, systems, and management. Structural and Multidisciplinary Optimization, 67(3), 1-34.
- Yang, S., Lee, M., Jung, Y., Cho, H., Hu, W., & Lee, I. (2024). An effective active learning strategy for reliability-based design optimization under multiple simulation models. Structural Safety, 107, 102426.
- Lee, H., Lee, M., Jung, J., Lee, I., & Ryu, S. Enhancing Injection Molding Optimization for SFRPs Through Multi‐Fidelity Data‐Driven Approaches Incorporating Prior Information in Limited Data Environments. Advanced Theory and Simulations, 2400130.
- Cheng, C., Yang, B., Wang, X., & Lee, I. Uncertainty‐oriented thermoelastic topology optimization with stress constraint. International Journal for Numerical Methods in Engineering, e7441.
- Park, Y., & Lee, I. (2024). Consecutive adaptive Kriging method for high-dimensional reliability analysis based on multi-fidelity framework. Structural and Multidisciplinary Optimization, 67(1), 1-18.
- Lee, M., Noh, Y., & Lee, I. (2024). A novel sampling method for adaptive gradient-enhanced Kriging. Computer Methods in Applied Mechanics and Engineering, 418, 116456.

**2023**

- Lee, J., Park, D., Lee, M., Lee, H., Park, K., Lee, I., & Ryu, S. (2023). Machine learning-based inverse design methods considering data characteristics and design space size in materials design and manufacturing: a review. Materials Horizons.
- Li, K., Li, Q., Lv, L., Song, X., Ma, Y., & Lee, I. (2023). A nonlinearity integrated bi-fidelity surrogate model based on nonlinear mapping. Structural and Multidisciplinary Optimization, 66(9), 196.
- Hu, W., Yan, J., Zhao, F., Jiang, C., Liu, H., Cho, H., & Lee, I. (2023). Surrogate-Based Time-Dependent Reliability Analysis for a Digital Twin. Journal of Mechanical Design, 1-36.
- Choo, J., Jung, Y., Jo, H., Kim, J., & Lee, I. (2023). Distribution estimation of Johnson-Cook parameters considering correlation in quasi-static state. International Journal of Mechanical Sciences, 108086.
- Yang, S., Lee, M., & Lee, I. (2023). A new sampling approach for system reliability-based design optimization under multiple simulation models. Reliability Engineering & System Safety, 231, 109024.
- Park, J. W., & Lee, I. (2023). A new framework for efficient sequential sampling-based RBDO using space mapping. Journal of Mechanical Design, 145(3), 031702.
- Park, S. H., Kim, Y., Jang, H., Hwang, C., Choi, J., Lee, I., & Oh, M. W. (2023). Fe-Ni-Cr diffusion barrier for high-temperature operation of Bi2Te3. Journal of Alloys and Compounds, 932, 167537.
- Lee, J., Lee, M., Lee, B., Lee, I. (2023). Hierarchical Gaussian process surrogate modeling framework for heterogeneous multi-fidelity dataset. In IDETC 2023 (국제 학회)

**2022**

- Lee, M., Jung, Y., Choi, J., & Lee, I. (2022). A reanalysis-based multi-fidelity (RBMF) surrogate framework for efficient structural optimization. Computers & Structures, 273, 106895.
- Lee, I., Lee, U., Ramu, P., Yadav, D., Bayrak, G., & Acar, E. (2022). Small failure probability: principles, progress and perspectives. Structural and Multidisciplinary Optimization, 65(11), 1-34.
- Ramu, P., Thananjayan, P., Acar, E., Bayrak, G., Park, J. W., & Lee, I. (2022). A survey of machine learning techniques in structural and multidisciplinary optimization. Structural and Multidisciplinary Optimization, 65(9), 1-31.
- Kim, M., Jung, Y., Lee, M., & Lee, I. (2022). An expected uncertainty reduction of reliability: adaptive sampling convergence criterion for Kriging-based reliability analysis. Structural and Multidisciplinary Optimization, 65(7), 1-11.
- Kim, J., & Lee, I. (2022). Modeling of geometric uncertainties in topology optimization via the shift of design nodes. Structural and Multidisciplinary Optimization, 65(7), 1-13.
- Lee, M., Park, Y., Jo, H., Kim, K., Lee, S., & Lee, I. (2022). Deep generative tread pattern design framework for efficient conceptual design. Journal of Mechanical Design, 144(7), 071703.
- Lee, U., Jeon, S., & Lee, I. (2022). Design for shared autonomous vehicle (SAV) system employing electrified vehicles: Comparison of battery electric vehicles (BEVs) and fuel cell electric vehicles (FCEVs). Cleaner Engineering and Technology, 8, 100505.
- Yang, S., Jo, H., Lee, K., & Lee, I. (2022). Expected system improvement (ESI): A new learning function for system reliability analysis. Reliability Engineering & System Safety, 222, 108449.
- Choo, J., Jung, Y., & Lee, I. (2022). A bayesian model calibration under insufficient data environment. Structural and Multidisciplinary Optimization, 65(3), 1-20.
- Jung, Y., Jo, H., Choo, J., & Lee, I. (2022). Statistical model calibration and design optimization under aleatory and epistemic uncertainty. Reliability Engineering & System Safety, 222, 108428.
- Kim, S., Lee, U., Lee, I., & Kang, N. (2022). Idle vehicle relocation strategy through deep learning for shared autonomous electric vehicle system optimization. Journal of Cleaner Production, 333, 130055.
- Lee, U., & Lee, I. (2022). Sampling-based weighted reliability-based design optimization. Structural and Multidisciplinary Optimization, 65(1), 1-20.
- Lee, U., & Lee, I. (2022). Efficient sampling-based inverse reliability analysis combining Monte Carlo simulation (MCS) and feedforward neural network (FNN). Structural and Multidisciplinary Optimization, 65(1), 1-22.
- Park, J., Lee, I. (2022). A new framework for efficient sequential sampling-based RBDO using space mapping. In IDETC 2022 (국제 학회)

**2021**

- Jung, Y., & Lee, I. (2021). Optimal design of experiments for optimization-based model calibration using Fisher information matrix. Reliability Engineering & System Safety, 216, 107968.
- Kim, D., & Lee, I. (2021). Efficient high-dimensional metamodeling strategy using selectively high-ordered kriging HDMR (SH-K-HDMR). Journal of Mechanical Science and Technology, 35(11), 5099-5105.
- Acar, E., Bayrak, G., Jung, Y., Lee, I., Ramu, P., & Ravichandran, S. S. (2021). Modeling, analysis, and optimization under uncertainties: a review. Structural and Multidisciplinary Optimization, 64(5), 2909-2945.
- Lee, J. K., Lee, I., & Lee, J. W. (2021). Reliability-based acoustical topology optimization of mufflers under noise frequency and temperature uncertainties. Mechanical Systems and Signal Processing, 160, 107854.
- Pae, S., Jo, H., & Lee, I. (2021). Error-lumped inverse uncertainty quantification of automotive heat exchangers (HEXs) using large-scale database from system level tests. Structural and Multidisciplinary Optimization, 64(4), 2709-2724.
- Jo, H., Lee, K., Lee, M., Jung, Y., & Lee, I. (2021). Optimization-based model calibration of marginal and joint output distributions utilizing analytical gradients. Structural and Multidisciplinary Optimization, 63(6), 2853-2868.
- Jung, Y., Kang, K., Cho, H., & Lee, I. (2021). Confidence-based design optimization for a more conservative optimum under surrogate model uncertainty caused by Gaussian process. Journal of Mechanical Design, 143(9).
- Yoo, J., Jang, I.G. & Lee, I. (2021). Multi-resolution topology optimization using adaptive isosurface variable grouping (MTOP-aIVG) for enhanced computational efficiency. Struct Multidisc Optim 63, 1743–1766.
- Kang, K., & Lee, I. (2021). Efficient high-dimensional metamodeling strategy using recursive decomposition coupled with sequential sampling method. Structural and Multidisciplinary Optimization, 63(1), 375-390.
- Lee, U., Jeon, S., Lee, I. (2021, August). Shared autonomous vehicle system design for battery electric vehicle (BEV) and fuel cell electric vehicle (FCEV). In IDETC/CIE 2021 (국제 학회)
- Jeon, S., Lee, I. (2021). Optimization of specifications and operation conditions of PEM fuel cell system using data-driven surrogate model. In ICEMS 2021 (국제 학회)
- Yang, S., Lee, I.(2021, June). System reliability analysis using predictive system uncertainty. In WCSMO 14 (국제 학회)
- Lee, M., Park, Y., Jo, Hw., Kim, K., Lee, S., Lee, I. (2021, June). Efficient tire pattern design using deep learning methodology. In WCSMO 14 (국제 학회)
- Jo, Hw., Lee, I. (2021, June). An enhanced framework of model calibration using the modular Bayesian approach for identifiability problem. In WCSMO 14 (국제 학회)
- KIM, J., Lee, I. (2021, June). Modeling of geometric uncertainties in topology optimization via the shift of design nodes. In WCSMO 14 (국제 학회)
- Hwang, Ch., Hong, S., Kang, S., Park, S., Lee, I. (2021). Study of Applying Thermoelectric Cooling System to EV Motor Cooling System. 대한금속재료학회(추계) (국내 학회)
- Hwanh, Ch., Kim, Y., Park, S., Lee, I. (2021). Development of improved diffusion barrier for bismuth telluride thermoelectric module. 대한금속재료학회(춘계) (국내 학회)
- Choi, Hy., Lee, I. (2021). Model-based MATLAB/Simulink automatic code generation and code analysis. IEIE2021(하계) (국내 학회)
- Lee, M., Park, Y., Jo, Hw., Kim, K., Lee, S., Lee, I. (2021). Efficient tire pattern design framework using generative adversarial networks. KSME2021(CAE 및 응용역학부문 춘계) (국내 학회)
- Lee, U., Lee, I. (2021). Weighted reliability-based design optimization. KSME2021(CAE 및 응용역학부문 춘계) (국내 학회)
- Park, J., Lee, I. (2021). Reliability analysis using space mapping under multi-fidelity model conditions. KSME2021(CAE 및 응용역학부문 춘계) (국내 학회)
- Yang, S., Lee, I. (2021). New system reliability analysis method to reduce system uncertainty. KSME2021(CAE 및 응용역학부문 춘계) (국내 학회)
- Kim, M., Lee, I. (2021). Meta criterion for expected uncertainty reduction of reliability under Kriging model. KSME2021(CAE 및 응용역학부문 춘계) (국내 학회)
- Park, Y., Lee, I. (2021). Adaptive Kriging method for high dimensional reliability analysis using high dimensional model representation. KSME2021(CAE 및 응용역학부문 춘계) (국내 학회)
- Jeon, S., Lee, I. (2021). Optimization of specifications and operation conditions of PEM fuel cell system using data-driven surrogate model. KSME2021(CAE 및 응용역학부문 춘계) (국내 학회)

## 과제

누리집 Projects 페이지의 진행 중(In progress) 과제 5건과, 끝난(Finished) 과제 가운데 끝난 해가 2021년 이후인 15건, 모두 20건이다. 과제 이름, 기간, 지원 기관은 목록 그대로이며, 「스마트 디지털 엔지니어링 전문인력양성사업」에는 지원 기관이 적혀 있지 않다. 끝난 해가 2021년으로만 적힌 과제 3건은 2021년 10월 전에 끝났을 수 있다.[^projects]

- 피지컬AI 기반 협업지능 Sim-to-Real 통합 플랫폼 기술 개발 (기간 2026.08 ~ 2030; 지원 과학기술정보통신부; 상태 진행 중)
- 4대 과학기술원 InnoCORE연구단: AI 기반 지증형 설계-제조 통합 연구단 (PRISM-AI) (기간 2025.08 ~ 2029; 지원 과학기술정보통신부; 상태 진행 중)
- 소량 다품종 유제품의 품질 관리를 위한 AI 기반 제조공정 최적화 기술개발 (기간 2025 ~ 2029; 지원 스퀘어네트; 상태 진행 중)
- PINN 기반 연료공급 이중관 내부 응력∙진동 예측 기술 개발 (기간 2026.04 ~ 2026.12; 지원 HD현대중공업; 상태 진행 중)
- 강화학습을 이용한 Mask Fab 자동화 Scheduling 기술 개발 (기간 2026.05 ~ 2026.12; 지원 SK hynix; 상태 진행 중)
- 산업체 다원 폐열 재생 열전발전 시스템 개발 및 실증 (기간 2021 ~ 2025; 지원 에너지기술평가원; 상태 종료)
- 해석결과의 산포 영향도 예측 위한 프로세스 개발 (기간 2025.06 ~ 2025.12; 지원 현대기아; 상태 종료)
- 다목적 기동지원 로봇 최적화 설계 (기간 2025. 05 ~ 2025. 12; 지원 육군본부; 상태 종료)
- FEA 예측력 향상을 위한 AI 기반 Tuning Parameter 최적화 Tool 개발 (기간 2024.11 ~ 2025.10; 지원 한국타이어앤테크놀로지; 상태 종료)
- A novel process design for DAC for energy consumption minimization using efficient multi-fidelity Bayesian optimization (기간 2024.09 ~ 2025.08; 지원 Saudi Aramco – KAIST CO2 Management Center; 상태 종료)
- 스마트 디지털 엔지니어링 전문인력양성사업 (기간 2019 ~ 2024; 상태 종료)
- AI 기반 단품 데이터를 이용한 시스템 강도 성능 예측 모델 개발 (기간 2023 ~ 2024; 지원 현대엔지비; 상태 종료)
- 연속 감시정찰을 위한 인공지능 기반 센서 조합 및 배치 최적화 (기간 2022 ~ 2023; 지원 LIG넥스원; 상태 종료)
- DoE 시험 모델과 엔진 물리 모델을 이용한 다중 충실도 모델 개발 (기간 2022 ~ 2023; 지원 현대엔지비; 상태 종료)
- 신소재/신구조 로봇 그리퍼 프레임 개발 (기간 2022 ~ 2023; 지원 현대엔지비; 상태 종료)
- EEDI Phase 4 및 EEOI 대응을 위한 EGCIS Package 시스템 개발 (기간 2020 ~ 2022; 지원 한국조선해양(주); 상태 종료)
- 글로벌 특이점 연구사업 – 미세먼지 연구 (기간 2019 ~ 2021; 지원 기관 자체 사업; 상태 종료)
- AI 연계 Virtual 예측 향상 기술 개발 (기간 2021 ~ 2022; 지원 한국타이어앤테크놀로지; 상태 종료)
- 인공 지능을 활용한 타이어 스타일링 패턴 자동 생성 및 성능 최적화 (기간 2020 ~ 2021; 지원 한국타이어앤테크놀로지; 상태 종료)
- 택배 운송에 최적화된 친환경 하이브리드 디젤-전기 소형트럭 개발 기획 (기간 2018 ~ 2021; 지원 국토교통부; 상태 종료)

## 수상

누리집 Awards 게시판의 글 6건(2022년 4월–2024년 12월)이다. 날짜는 글 본문에 적힌 연·월이고, 제목과 과정·직위 표기는 게시판 그대로다.[^award]

- 2024-12 · 이민규 박사 2024 KAIST 기계공학과우수상-기계동문회장상 수상
- 2024-05 · 이민규 박사 대한기계학회 CAE 및 응용역학부문 우수 학위논문상 수상
- 2024-05 · 양성혁 박사 대한기계학회 CAE 및 응용역학부문 우수논문상 수상
- 2024-01 · 이민규 박사 한국최적설계학회 우수 학위논문상 수상
- 2023-08 · 최지웅 석사과정 창업 아이디어 경진대회 수상
- 2022-04 · 황철현 석사과정 대한금속재료학회 포스터 발표 우수상 수상

## 소식

누리집 Academic news 게시판의 강좌 글 4건(2023년 7월–2026년 2월)과 Alumni news 게시판의 졸업생 교수 임용 글 2건(2024년 3월, 2025년 3월), 모두 6건이다. 강좌 글의 날짜는 제목 아래 적힌 기간이고, 임용 글의 날짜는 본문에 적힌 임용일이다. 제목은 게시판 표기 그대로다.[^seminar][^alumninews]

- 2026-02-25–2026-02-27 · KAIST 산학협동 공개강좌 “해석에서 설계 최적화 및 PINN/LMM 활용까” 개최
- 2025-03-01 · 정용수 박사 홍익대학교 세종캠퍼스 조교수 임용
- 2025-02-10–2025-02-12 · KAIST 산학협동 공개강좌 “AI 기반 설계: 해석에서 설계 최적화까지” 개최
- 2024-03-01 · 이웅기 박사 고려대학교 세종캠퍼스 조교수 임용
- 2024-02-19–2024-02-21 · KAIST 산학협동 공개강좌 “인공지능과 설계: 해석 예측에서 설계 최적화까지” 개최
- 2023-07-26–2023-07-28 · KAIST-한온시스템 “인공지능과 최적설계” 개최

## 연락과 위치

- 연구실: Rm 5126 (Lab), Building N7-4, Department of Mechanical Engineering, KAIST, 전화 (+82)-42-350-5041[^contact]
- 교수실과 전화: Rm 7109, Building N7-4, +82-42-350-3041[^prof][^contact]
- 교수 이메일: ikjin.lee@kaist.ac.kr[^prof][^meprof]
[^p1]: U. Lee, I. Lee, Structural and Multidisciplinary Optimization 65, 8 (온라인 2021-12-18). <https://doi.org/10.1007/s00158-021-03144-2> 초록 기준(출판사 논문 페이지).
[^p2]: Y. Park, I. Lee, Structural and Multidisciplinary Optimization 67, 11 (온라인 2024-01-24). <https://doi.org/10.1007/s00158-023-03727-1> 초록 기준(출판사 논문 페이지).
[^p3]: Y. Park, M. Lee, I. Lee, Journal of Mechanical Design 148, 091707 (온라인 2026-04-02). <https://doi.org/10.1115/1.4071406> 초록 기준.
[^p4]: H. Jo 외, I. Lee, Journal of Mechanical Design 146, 101702 (온라인 2024-03-05). <https://doi.org/10.1115/1.4064782> 초록 기준.
[^p5]: J. Choo, Y. Jung, I. Lee, Structural and Multidisciplinary Optimization 65, 96 (온라인 2022-02-28). <https://doi.org/10.1007/s00158-022-03196-y> 초록 기준(출판사 논문 페이지).
[^p6]: J. Kim, I. Lee, Structural and Multidisciplinary Optimization 65, 191 (온라인 2022-06-28). <https://doi.org/10.1007/s00158-022-03277-y> 초록 기준(출판사 논문 페이지).
[^p7]: M. Lee 외, I. Lee, Journal of Mechanical Design 144, 071703 (온라인 2022-02-15). <https://doi.org/10.1115/1.4053469> 초록 기준.
[^p8]: B. U. Song 외, I. Lee, International Journal of Precision Engineering and Manufacturing-Green Technology 12, 1133-1146 (온라인 2025-02-03). <https://doi.org/10.1007/s40684-024-00683-z> 초록 기준.
[^home]: 최적 설계 연구실 누리집 첫 화면 <http://idol.kaist.ac.kr/> (환영 문구, 문의처, 바닥글, 2026-10-23 열람)
[^area]: 연구실 누리집 Research Area 페이지 <http://idol.kaist.ac.kr/courses/> (연구 주제 열한 가지, Reliability Analysis, Reliability-Based Design for Market System, Statistical Model Calibration, Surrogate Modeling, Multi-scale design optimization of composite material and structure, Analytical Target Cascading, 2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <http://idol.kaist.ac.kr/members/professor/> (EDUCATION, PROFESSIONAL EXPERIENCES, AWARDS, PROFESSIONAL SERVICES, 2026-10-23 열람)
[^pubpage]: 연구실 누리집 Publication 페이지 <http://idol.kaist.ac.kr/research/> (Books, Ph. D. Thesis, Technical Notes, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publication 메뉴의 세 목록 <http://idol.kaist.ac.kr/research/papers_international/> , <http://idol.kaist.ac.kr/research/international_conference/> , <http://idol.kaist.ac.kr/research/domestic_conference/> (2021–2026년 연도 구역, 2026-10-23 열람)
[^postdocs]: 연구실 누리집 Post-docs 페이지 <http://idol.kaist.ac.kr/members/postdocs/> (2026-10-23 열람)
[^phd]: 연구실 누리집 Ph.D. students 페이지 <http://idol.kaist.ac.kr/members/phd/> (Full Time Students, Part Time Students, 2026-10-23 열람)
[^ms]: 연구실 누리집 M.S. students 페이지 <http://idol.kaist.ac.kr/members/ms/> (2026-10-23 열람)
[^alumni]: 연구실 누리집 Alumni 페이지 <http://idol.kaist.ac.kr/members/alumni/> (Post doc., Ph.D, M.S 구역, 2026-10-23 열람)
[^projects]: 연구실 누리집 Projects 페이지 <http://idol.kaist.ac.kr/projects/> (In progress, Finished, 2026-10-23 열람)
[^seminar]: 연구실 누리집 Academic news 게시판 <http://idol.kaist.ac.kr/news/seminar/> (2026-10-23 열람)
[^alumninews]: 연구실 누리집 Alumni news 게시판 <http://idol.kaist.ac.kr/news/alumni-news/> (2026-10-23 열람)
[^award]: 연구실 누리집 Awards 게시판 <http://idol.kaist.ac.kr/news/award/> (2026-10-23 열람)
[^contact]: 연구실 누리집 Contacts 페이지 <http://idol.kaist.ac.kr/contacts/> (2026-10-23 열람)
[^meprof]: KAIST 기계공학과 교수 소개(이익진) <https://me.kaist.ac.kr/pop/team.html?uid=46&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 웹사이트, 이메일, 사무실, 전화, 2026-10-23 열람)
[^melist]: KAIST 기계공학과 교수진 목록 2쪽 <https://me.kaist.ac.kr/team/team_010100.html?page=2&plist=&find_field=&find_word=&find_state=&find_ordby=&conf=&mode=1> (이익진 교수 항목, 2026-10-23 열람)
[^meres]: KAIST 기계공학과 연구분야 안내 「소재/역학/제조」 <https://me.kaist.ac.kr/research/research_010200.html> (이익진 교수 항목: 연구주제, 주요 응용 산업, 연구실, 2026-10-23 열람)

# 전산역학 및 생체역학 연구실 (Computational Mechanics and Biomechanics Laboratory, CMB Lab)

**KAIST 기계공학과 · 김현진 교수**

- 분야: 전산역학, 심혈관·뇌혈관 혈류 시뮬레이션, 혈관·조직 역학, 다중 스케일·다중 물리 모델링, 축소 차수 모델과 불확실성 정량화
- 대분야: 기계·로봇·제조
- 태그: 유체역학·유동[^research][^p2][^p4], 열전달·열관리[^mm], 생체역학[^research], 전산역학·수치 해석[^mm]
- 홈페이지: <https://cmb.kaist.ac.kr/>
- 근거와 출처: [전산역학 및 생체역학 연구실 근거 페이지](cmb-sources.md)

> 몸속의 피 흐름과 혈관·조직이 받는 힘, 그리고 둘이 서로 주고받는 영향을 컴퓨터 계산으로 밝히는 방법을 만드는 연구실이다. 물리 법칙에 바탕을 둔 모델에 의료 영상과 생리 자료를 결합해 환자 한 사람 한 사람에 맞춘 시뮬레이션을 하고, 진단·치료 계획·의료기기 설계 연구를 돕는 것을 목표로 한다.[^home]

## 무엇을 연구하나

연구실은 복잡한 역학계와 생리계를 분석하는 계산 방법을 연구한다. 유체역학(액체·기체의 흐름을 다루는 학문), 고체역학(고체가 힘을 받아 변형하는 것을 다루는 학문), 물질과 열이 옮겨 가는 수송 현상을 의료 영상, 생리 자료, 자료 기반 방법과 결합해 다중 스케일·다중 물리 모델과 환자 맞춤 모델을 만들고, 이 모델로 심혈관계와 뇌혈관계의 혈류, 조직 변형, 관류, 수송을 정량적으로 조사한다. 연구 페이지는 이 일의 목표를 작동 원리에 대한 이해를 넓히고 임상 평가, 치료 계획, 의료기기 설계 연구를 돕는 것으로 적는다.[^research]

연구는 세 영역으로 나뉜다. 첫째는 계산 방법 자체로, 다중 스케일·다중 물리 모델링과, 계산 비용을 줄이는 축소 차수 모델(자세한 3차원 계산을 차원과 변수를 줄인 식으로 바꿔 빠르게 풀게 만든 모델) 및 불확실성 정량화다. 둘째는 심혈관 생체역학으로, 관상동맥 혈류와 허혈성 심장질환, 복부 대동맥류(배 부위 대동맥 벽이 약해져 부풀어 오른 상태)의 혈류와 벽 역학, 정맥 혈류와 간헐적 공압 압박(공기 압력으로 다리에 시간에 따라 바뀌는 압박을 가하는 치료 기기)을 다룬다. 셋째는 뇌혈관·뇌 역학으로, 뇌 관류와 자동 조절(혈압이 바뀌어도 기관의 혈류를 일정하게 지키려고 작은 동맥이 지름을 스스로 바꾸는 작용), 뇌혈관망과 곁순환(주 혈관이 좁아지거나 막힐 때 다른 혈관 길로 피가 돌아 공급되는 흐름)을 다룬다.[^research] 기계공학과 교수 소개는 교수의 연구분야를 Computational mechanics, Cardiovascular biomechanics, Clinical applications로 적는다.[^meprof]

연구 페이지의 진행 중 과제 표에는 연구실이 주관하는 과제 3건(환자 맞춤 진단 기술 기반 심혈관·뇌혈관 M3DT, 디지털 트윈 기반 뇌 모니터링을 위한 다중 스케일 뇌 역학 모델, 뇌 질환 조기 발견을 위한 신경·심장 통합 디지털 트윈)과 공동으로 참여하는 과제 2건이 있다.[^research]

## 주요 연구 주제

### 1. 계산 방법: 다중 스케일·다중 물리 모델과 축소 차수 모델

몸속에서는 혈류, 조직 역학, 물질 수송이 여러 공간·시간 규모에 걸쳐 서로 영향을 준다. 연구실은 차원을 줄인 혈관 모델과 3차원 조직 영역을 결합하는 계산 틀을 만든다. 이렇게 하면 꼭 필요한 국소 물리는 남기면서 계산 비용을 줄이고, 결합한 영역 사이에서 역학·수송 변수를 일관되게 주고받을 수 있다.[^mm]

- 혼합 차원 유체–구조 상호작용(흐르는 유체와 그 흐름에 밀려 변형하는 구조물이 서로 영향을 주고받는 현상): 1차원 변형 혈류 모델과 3차원 조직 역학을 결합해 혈관 속 압력, 혈관 변형, 바깥에서 가하는 하중의 상호작용을 나타낸다. 유체 쪽과 구조 쪽이 압력과 단면 변형을 번갈아 주고받으며, 전체 3차원 계산과 비교해 비슷한 시간 응답을 훨씬 적은 계산 비용으로 얻었다고 연구 페이지는 적는다.[^mm]
- 혈관–조직 수송: 큰 혈관은 1차원 흐름·수송 방정식으로, 작은 혈관은 3차원 조직 속 연속체로 나타내고 양방향으로 결합해 에너지나 질량의 전달이 맞도록 한다. 혈관 배치와 조직의 불균일성이 국소적으로 어떤 영향을 주는지를 균질한 생체 열전달·다공성 매질 설명보다 자세히 볼 수 있다.[^mm]
- 혈관망에서 조직까지: 동맥·정맥망, 모세혈관 앞뒤 구간, 3차원 관류 영역을 잇고, 혈관의 수동적 역학과 능동적 자동 조절을 넣어 전신 압력, 중력, 혈관 강성, 대사 요구가 국소 관류에 주는 영향을 본다.[^mm]

3차원 계산은 자세하지만 비용이 크다. 연구실은 적은 수의 3차원 전산유체역학(컴퓨터로 유체의 흐름을 계산하는 방법) 계산에서 형상에 따른 압력–유량 관계를 맞춰 넣은 1차원 축소 차수 모델을 만들고, 협착·굽음·분지에서 생기는 압력 손실을 반영한다. 이 모델을 확률적 방법과 결합해 모델 예측의 변동을 정량화하고 영향이 큰 생리·역학 매개변수를 찾는다. 연구 페이지는 이 모델이 고해상도 계산을 대신하지 않고 보완하는 도구라고 적는다.[^uq] 대표 논문 1, 2.[^p1][^p2]

### 2. 심혈관 생체역학: 관상동맥, 복부 대동맥류, 정맥

관상동맥 연구에서는 의료 영상으로 환자의 관상동맥 모양을 재구성하고, 3차원 전산유체역학 결과를 1차원 축소 차수 모델에 넣어 복잡한 협착 혈관의 박동성 흐름을 빠르게 계산한다. 이 모델을 생리 정보를 넣은 집중 정수 모델(혈관계의 각 부분을 저항·용량 같은 몇 개 요소로 묶어 나타낸 단순한 모델)과 이어 분획 혈류 예비력(관상동맥이 좁아진 곳 뒤쪽 압력을 대동맥 압력으로 나눈 값으로, 협착이 혈류를 얼마나 막는지 나타내는 지표)과 그 생리적 변동을 분석하고, 만성 완전 폐색(관상동맥이 오랫동안 완전히 막혀 있는 상태) 뒤쪽의 압력 회복과 심근 관류에 곁혈관의 성질이 주는 영향을 대규모 가상 모델로 비교한다. 연구 페이지는 이 마지막 연구가 진행 중이고, 가상 사례 4만 5천 개를 다룬 연구는 심사 중이라고 적는다.[^coronary] 대표 논문 3.[^p3]

복부 대동맥류 연구에서는 환자 맞춤 대동맥류 모양에서 박동성 혈류를 계산하고, 여러 심장 주기에 걸친 위상 평균으로 지속되는 흐름 구조와 순간적인 요동을 구분한다. 흐름 해석에서 얻은 압력을 구조 해석에 넣되 혈관 벽과 혈관 속 혈전을 서로 다른 재료로 나타내 각각의 반응을 따로 보고, 벽과 혈전에 걸리는 응력을 각각의 강도 추정치와 비교하는 지표로 파열이 일어나기 쉬운 부위를 평가한다. 연구 페이지는 이 지표 연구가 진행 중이라고 적는다.[^aneurysm] 대표 논문 4.[^p4]

정맥 연구는 다리에 시간에 따라 바뀌는 바깥 압력을 가하는 간헐적 공압 압박을 다룬다. 1차원 변형 정맥 흐름, 3차원 조직 역학, 집중 정수 정맥망을 결합해 압박 한 주기 전체를 계산하고, 압박 설정, 조직 성질, 정맥망 동역학이 정맥 유량·압력·벽 전단 응력에 주는 영향을 본다. 조사한 조건에서는 최대 압박 압력과 유지 시간이 혈류 반응을 주로 결정했다. 초음파로 잰 넙다리 정맥 속도와 단면적으로 계산 결과를 비교한다.[^venous] 대표 논문 1, 5.[^p1][^p5]

### 3. 뇌혈관·뇌 역학: 뇌 관류, 혈관망, 곁순환

뇌 관류 연구에서는 영상에서 얻은 혈관망과 3차원 조직 관류 영역을 잇는 환자 맞춤 다중 스케일 모델을 만든다. 각 동맥이 맡은 뇌 조직의 질량과 혈류 요구로 동맥마다 필요한 유량을 정하는 공급–수요 경계 조건을 쓰고, 영상 해상도보다 가는 혈관은 합성 혈관 트리로 채운다. 세동맥(동맥에서 갈라져 모세혈관으로 이어지는 가는 동맥)의 능동적 확장·수축을 넣어 대동맥 압력, 중력, 혈관 강성, 대사 요구의 영향을 함께 본다. 조사한 조건에서 자동 조절은 세동맥 지름을 바꿔 뇌 혈류를 비교적 좁은 범위 안에 지켰고, 정맥 부피는 주로 자세에 따라 바뀌었다.[^cerebral] 대표 논문 6.[^p6]

뇌혈관망 연구에서는 국소 조직의 혈류 요구, 혈관과 조직 사이의 거리, 혈류를 유지하는 역학적 비용을 고려하는 알고리즘으로 합성 혈관 트리를 만든다. 조직 성장 기반 방법에서는 혈관과 조직 영역이 함께 자라며 공급할 조직이 늘면 가지가 더해진다. 곁혈관의 굵기·밀도·분포를 바꿔 가며 협착이 있을 때 관류가 얼마나 회복되는지 보고, 윌리스 고리(뇌 아래쪽에서 주요 뇌동맥들을 서로 이어 주는 고리 모양 혈관 연결)의 해부학적 변이와 자동 조절 능력이 뇌 압력·유량 재분배에 주는 영향을 연구한다. 조사한 조건에서 곁혈관의 굵기가 개수보다 관류 회복에 더 크게 작용했다. 연구 페이지는 합성 혈관망을 고해상도 영상과 해부학 측정으로, 관류 결과를 생리 범위와 자기공명영상 관류 자료로 대조한다고 적는다.[^networks] 대표 논문 7, 8.[^p7][^p8]

## 대표 논문

김현진 교수가 저자인 2022–2026년 학술지 논문 가운데, 교수가 마지막 저자이거나 첫 저자인 논문을 세 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [Efficient multi-fidelity fluid-structure interaction modeling for pulsatile blood flow in deformable biological tissues](https://doi.org/10.1007/s10439-025-03966-x) · Annals of Biomedical Engineering | 바깥 압박으로 생기는 조직 변형과 혈류 변화를 계산하려면 보통 유체–구조 상호작용 해석이 필요하지만 계산 부담이 크다. 이 연구는 1차원 변형 혈류 식을 3차원 코시 운동 방정식(고체가 힘을 받아 움직이고 변형하는 것을 나타내는 기본 식)과 결합한 다중 충실도(정밀한 모델과 단순한 모델을 섞어 쓰는 방식) 해석 틀을 만들었다. 단순한 원통 형상과 대상자 맞춤 형상에서 전체 해석과 비교해 두 형상 모두 유량 오차가 1% 미만이었고, 단순 형상에서는 주기 대부분 동안 압력 오차가 2% 미만이었다. 계산 비용은 전체 3차원 해석보다 원통 형상에서 9분의 1, 대상자 맞춤 형상에서 46분의 1로 줄었고, 간헐적 공압 압박 한 주기 전체를 단순 형상은 457초, 대상자 맞춤 형상은 42.2분에 계산했다.[^p1] | 1저자 C. M. Lee, 마지막 저자 김현진 (7명) |
| 2 | 2025 | [Developing a reduced order model for pulsatile blood flow simulations using minimal three-dimensional simulation data](https://doi.org/10.1016/j.cmpb.2025.108994) · Computer Methods and Programs in Biomedicine | 박동성 혈류의 전체 3차원 계산은 비용이 크고, 기존 축소 차수 모델은 경험적 매개변수에 기대어 복잡한 형상에서 정확도가 떨어진다. 이 연구는 서로 다른 유량 조건의 3차원 시뮬레이션 세 번의 결과에 단순화한 1차원 혈류 식의 매개변수를 맞춰 압력–유량 관계를 얻는 1차원 모델을 내놓았다. 협착이 있는 이상화 원통, 환자 맞춤 대동맥 축착(대동맥 일부가 좁아진 상태) 모델, 여러 병변이 이어진 관상동맥 모델에서 3차원 계산과 비교하니 평균 상대 오차가 모든 경우 2.0% 미만, 관상동맥 모델에서는 1.0% 미만이었다. 복잡한 형상에서는 널리 쓰이는 경험적 협착 모델보다 정확했고, 데스크톱에서 64코어 고성능 계산 시스템의 3차원 계산보다 최대 3000배 빨랐다.[^p2] | 1저자 W. Choi, 마지막 저자 김현진 (3명) |
| 3 | 2026 | [Effects of pulsatile flow on fractional flow reserve assessed using a reduced-order model](https://doi.org/10.1007/s10439-026-04292-6) · Annals of Biomedical Engineering | 계산으로 구한 분획 혈류 예비력은 관상동맥 협착의 기능적 심각도를 몸을 열지 않고 평가하는 대안이지만, 생리적 변동 속에서 얼마나 믿을 만한지는 풀리지 않은 문제다. 3차원 계산에서 얻은 축소 차수 모델과 다항식 카오스 전개(입력의 불확실성이 결과에 어떻게 퍼지는지 다항식으로 계산하는 방법)를 결합하고, 1차원 관상동맥 혈류 계산을 생리 정보를 넣은 집중 정수 회로망과 이어, 심근 역학과 전신 순환에 관한 생리 매개변수 17개를 무작위 입력으로 다뤘다. 전역 민감도 분석(입력 매개변수 각각이 결과의 변동에 얼마나 기여하는지 따지는 방법)에서 심근(심장 근육) 압박 매개변수가 분획 혈류 예비력 변동의 주된 요인이었고, 그다음은 대동맥 압력에 영향을 주는 일부 전신·심장 매개변수였다. 임상 판단 기준 근처를 포함한 모든 조건에서 분획 혈류 예비력은 넓은 생리적 불확실성에도 안정했고, 평균과 표준편차 사이에 강한 선형 관계가 있었다.[^p3] | 1저자 W. Choi, 마지막 저자 김현진 (5명) |
| 4 | 2023 | [Convergence of phase-averaged, transitional flow in an abdominal aortic aneurysmal model](https://doi.org/10.1115/1.4063066) · Journal of Biomechanical Engineering | 복부 대동맥류는 층류(흐름이 층을 이루며 고르게 흐르는 상태) 영역에서도 천이 유동(층류와 난류 사이의 중간 성격을 띠는 흐름) 특성을 보일 수 있다. 환자 맞춤 복부 대동맥류 모델에서 주기적인 박동성 경계 조건으로 심장 주기 257번에 걸친 혈류 시뮬레이션을 하고, 여러 주기 수로 평균한 위상 평균(여러 주기에서 같은 시점의 값을 모아 평균하는 것) 해를 124주기 평균 해와 비교했다. 많은 주기로 평균할수록 차이가 작았고, 순간 해는 위상 평균 해에서 나타난 요동을 보여 주지 못했다. 대동맥류의 천이 혈류를 다루려면 비주기적이고 흐트러진 흐름 특성을 담는 위상 평균 해를 보고해야 하며, 평균은 많은 심장 주기에 걸쳐 구하는 편이 좋다고 결론지었다.[^p4] | 1저자 김현진, 마지막 저자 K. Jansen (6명) |
| 5 | 2026 | [Computational investigation of intermittent pneumatic compression operating parameters and tissue mechanics in lower-limb venous hemodynamics](https://doi.org/10.1016/j.compbiomed.2026.111767) · Computers in Biology and Medicine | 간헐적 공압 압박은 만성 정맥 부전(다리 정맥의 피가 심장 쪽으로 잘 돌아가지 못하는 상태)의 예방과 관리에 널리 쓰이지만, 작동 조건, 조직 역학, 정맥 혈류 사이의 관계는 충분히 밝혀지지 않았다. 1차원 변형 혈류, 3차원 조직 역학, 집중 정수 상류 정맥망을 결합한 다중 충실도 해석 틀로, 압박 방 수, 압박 유지 시간, 최대 압박 압력, 체지방 통계에서 얻은 조직 성질을 바꿔 가며 정맥 유량·압력·벽 전단 응력(흐르는 피가 혈관 벽을 따라 미는 힘)을 계산했다. 최대 압박 압력과 유지 시간이 정맥 혈류 변화를 주로 결정했다. 압력이 높을수록 혈관 안쪽이 더 좁아지고 유량 맥동이 커졌고, 유지 시간이 길수록 먼 쪽에 피가 더 고였고 최대 유량과 압력이 높아졌다. 방 수의 영향은 작았고, 무른 조직일수록 변형과 혈류 반응이 컸다. 초음파 측정에서도 압박으로 넙다리 정맥의 혈류 속도와 단면적이 늘어 모델 예측을 뒷받침했다.[^p5] | 1저자 Y. Choi, 마지막 저자 김현진 (7명) |
| 6 | 2026 | [Multiscale modeling of posture-dependent cerebrovascular hemodynamics with autoregulatory coupling](https://doi.org/10.1016/j.compbiomed.2026.111502) · Computers in Biology and Medicine | 뇌 혈류는 전신과 자세의 변화를 보상하는 자동 조절 덕분에 안정하게 유지된다. 동맥·정맥망을 모세혈관 앞뒤 단계까지 담고 3차원 관류 영역과 결합한 다중 스케일 뇌혈관 모델에 수동적 혈관 역학과 능동적 자동 조절을 넣어, 대동맥 압력 30–150 mmHg와 누운 자세·선 자세·거꾸로 선 자세에서 혈관 벽 강성을 바꿔 가며 계산했다. 동맥 변형과 전체 혈관 부피는 전신 압력과 중력에 크게 좌우됐고, 정맥 부피는 압력 변화에는 비교적 안정했지만 자세에 따라 크게 바뀌었다. 능동적 자동 조절은 세동맥 지름을 바꿔 뇌 혈류를 거의 일정하게 지켰고, 혈관이 유연할수록 자세에 따른 부피 변화와 자동 조절 반응이 커졌다.[^p6] | 1저자 김현진, 마지막 저자 K.-H. Jung (5명) |
| 7 | 2026 | [Computational Modeling of Collateral Circulation and Arteriolar Vasodilation in Ischemic Tissue Perfusion](https://doi.org/10.1007/s10439-026-04052-6) · Annals of Biomedical Engineering | 곁순환과 세동맥 확장이라는 두 보상 기전을 다중 스케일 혈류 관류 시뮬레이션 틀에 넣었다. 허혈 영역에 피를 보내는 곁혈관을 무작위로 만들면서 밀도·굵기·공간 분포를 바꾸고, 세동맥 확장은 국소 대사·혈류 자극에 대한 혈관 평활근 세포(혈관 벽에서 수축·이완하는 근육 세포)의 반응으로 모델링했으며, 이상화 형상과 대상자 맞춤 뇌혈관 모델에 인공 협착을 넣어 관류에 주는 영향을 봤다. 영상 해상도보다 가는 곁혈관만으로는 관류 개선이 제한적이었고 그 효과가 혈관 굵기와 밀도에 크게 달렸지만, 곁순환과 혈관 확장을 함께 넣으면 조직 관류가 더 뚜렷하게 좋아졌다. 저자들은 세동맥 확장이 허혈 보상의 주된 기전이고 곁순환은 이차적으로 돕는다고 해석했다.[^p7] | 1저자 N. Moreaux, 마지막 저자 김현진 (7명) |
| 8 | 2023 | [Tissue-growth based Synthetic Tree Generation and Perfusion Simulation](https://doi.org/10.1007/s10237-023-01703-8) · Biomechanics and Modeling in Mechanobiology | 조직과 혈관 사이의 공급–수요 관계를 고려해 합성 혈관 트리를 만드는 알고리즘을 구현했다. 의료 영상에서 큰 동맥을 분할하고, 그 동맥에서 시작한 합성 트리가 공급할 조직을 채우며 대사 요구를 맞추는 작은 혈관망으로 자라게 했으며, 만들어지는 트리 부피에 영향을 주지 않고 병렬로 실행되도록 최적화했다. 혈관 트리에서는 1차원 혈류 방정식을, 조직에서는 다공성 매질 가정의 다르시 흐름 방정식(구멍이 많은 물질 속을 지나는 흐름을 나타내는 식)을 풀고 두 식을 끝 가지에서 결합했다. 이상화 모델로 검증했고, 제약 구성 최적화(constrained constructive optimization, 혈관 가지를 하나씩 더해 가며 최적화하는 기존 혈관 트리 생성 방법)보다 적은 계산 비용으로 현실적인 합성 트리를 만들었으며, 뇌에 피를 보내는 동맥과 좌우 심실에 피를 보내는 관상동맥에 적용했다.[^p8] | 1저자 김현진 (4명) |

## 교수와 전문 분야

김현진 교수는 KAIST 기계공학과 부교수다.[^pi] 기계공학과 교수 소개는 연구분야를 Computational mechanics, Cardiovascular biomechanics, Clinical applications로, 연구실을 「전산역학 및 생체역학 연구실」로 적는다.[^meprof] 학과 연구분야 안내의 「헬스케어/나노/광학」 항목은 연구주제를 Blood flow simulations of the cardiovascular system, Cardiovascular biomechanics, Clinical applications로 적는다.[^meres]

연구실 교수 소개 페이지에 따르면 교수는 KAIST 기계공학과에서 학사(1999–2003, summa cum laude)를, Stanford University 기계공학과에서 석사와 박사(2003–2009)를 받았다. 박사 논문은 관상동맥 혈류의 3차원 유한요소(물체나 영역을 작은 조각으로 나눠 계산하는 수치 해석 방법) 모델링이고 지도교수는 Charles A. Taylor다. Rensselaer Polytechnic Institute(2009)와 University of Colorado Boulder(2010)의 박사후연구원, HeartFlow, Inc.의 Senior Research Engineer(2010–2020)를 거쳐 2021년부터 KAIST 기계공학과 부교수다. 교수 소개에 적힌 수상·장학은 Robert J. Melosh Medal Competition 결선 진출(Finalist, 2009), Stanford Graduate Fellowship(2005–2008), Summer Bioengineering Meeting의 석사과정 학생 포스터 경연(Biofluids, Heat and Mass Transfer) 2위(2005), Stanford Engineering Fellowship(2003–2005)이다.[^pi]

교수의 논문 목록 가운데 누리집이 「– 2021」 구역에 묶은 20편은 KAIST 부임 전 시기를 포함한 2021년까지의 논문으로, 관상동맥 혈류의 3차원 유한요소 계산 방법, 심혈관계 자동 조절 기전을 넣은 동맥 혈류 모델, 집중 정수 심장 모델과 3차원 대동맥 모델의 결합, 관상동맥 CT 혈관조영 기반 혈류 계산과 혈관 벽 응력·플라크 연구 등을 다룬다.[^pubs] 강의는 학부의 유체역학, 수치해석, 기계공학 문제 해결을 위한 프로그래밍과 대학원의 고급 유체역학, 심혈관 생체역학 개론, 전산유체역학 및 열전달, 수치 선형대수 등을 맡았다.[^teaching]

논문으로 보면 KAIST에서의 전문 분야는 세 갈래다. 다중 충실도 유체–구조 상호작용과 3차원 계산 자료로 맞춘 1차원 축소 차수 모델 같은 계산 방법(대표 논문 1, 2),[^p1][^p2] 관상동맥 분획 혈류 예비력의 불확실성, 복부 대동맥류의 천이 유동, 간헐적 공압 압박 아래 정맥 혈류 같은 심혈관 혈류 해석(대표 논문 3, 4, 5),[^p3][^p4][^p5] 자세와 자동 조절을 넣은 뇌혈관 혈류, 곁순환, 합성 혈관 트리 기반 관류 같은 뇌혈관 모델링(대표 논문 6, 7, 8)이다.[^p6][^p7][^p8] 소식에는 교수가 2026년 8월 International Federation of Automatic Control 2026 Busan에서 심혈관 질환을 위한 디지털 트윈을 주제로 발표한 일 등 학회·세미나 발표가 올라 있다.[^news]

## 응용 분야

누리집은 연구의 쓰임을 진단, 치료 계획, 의료기기 설계 연구의 지원으로 적는다.[^home][^research] 대표 논문으로는 관상동맥 협착 평가에 쓰는 분획 혈류 예비력이 생리적 변동 속에서 얼마나 안정한지(대표 논문 3), 간헐적 공압 압박 기기의 작동 조건과 다리 조직 성질이 정맥 혈류에 주는 영향(대표 논문 1, 5), 협착이 있을 때 뇌 조직 관류를 지키는 보상 기전(대표 논문 7)이 있다.[^p1][^p3][^p5][^p7] 연구 페이지는 복부 대동맥류 연구에서 응력과 강도를 비교하는 지표를 파열과 관련된 생체역학 지표로 평가하고 있다고 적는다.[^aneurysm] 진행 중 과제의 지원 기관은 누리집 표기로 Ministry of Food and Drug Safety · KHIDI, Samsung Research Funding & Incubation Center, National Research Foundation of Korea, Ministry of Science and ICT다.[^research]

## 구성원

연구실 누리집 Members 페이지의 박사과정 8명, 석사과정 2명, Researchers 칸 2명(연구원 1명, InnoCORE 박사후연구원 1명), 모두 12명이다.[^people] 과정과 시작 연월은 각 카드의 표기("Ph.D. program since 2023.03" 등)이고, 이름 옆 괄호는 카드에 함께 적힌 국문 이름이다. 이메일은 카드에 적힌 KAIST 주소다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Seo Yeon Kim (김서연) | 박사과정 | 2023.03 | seoye1202@kaist.ac.kr |  |
| Chanhee An (안찬희) | 박사과정 | 2023.09 | an981031@kaist.ac.kr |  |
| Seung Min Lee (이승민) | 박사과정 | 2024.03 | lsmmailacc@kaist.ac.kr | 4, 8 |
| Chang Min Lee (이창민) | 박사과정 | 2024.03 | cmlee@kaist.ac.kr | 1, 4, 5, 6, 7 |
| Youngjae Choi (최영재) | 박사과정 | 2024.03 | yjchoi95@kaist.ac.kr | 1, 5, 6 |
| Hyeonggue Song (송형규) | 박사과정 | 2025.02 | momentum@kaist.ac.kr |  |
| Wonjin Choi (최원진) | 박사과정 | 2025.02 | wj0220@kaist.ac.kr | 2, 3 |
| Nolan Rene Moreaux | 박사과정 | 2025.09 | nolan.moreaux@kaist.ac.kr | 7 |
| Jiwoo Lee (이지우) | 석사과정 | 2026.03 | ejiu@kaist.ac.kr |  |
| Chae Jong Lee (이채종) | 석사과정 | 2026.09 | cjong17@kaist.ac.kr |  |
| Hyeok Sul Kwon (권혁술) | 연구원 |  | soori1029@kaist.ac.kr |  |
| Sumit Kumar Das | 박사후연구원 | 2026.09 | sumitkumardas@kaist.ac.kr |  |

## 졸업생

누리집 Members 페이지 Alumni 표의 석사 졸업생 9명(2023년 2월–2026년 8월 졸업)이다. 학위와 졸업 시기, 학위 논문 제목, 졸업 뒤 진로는 표 그대로이고, 표가 진로를 적지 않은 행은 비워 두었다. 이름 옆 괄호는 표에 함께 적힌 국문 이름이다. 이 가운데 5명은 현재 구성원 표에도 있다(박사과정 4명, 연구원 1명).[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Jan Wissing | M.S. (Aug 2026) |  | Quantification of Pulsatility-Induced Cerebral Blood Volume Changes as a Primary Driver of Cerebrospinal Fluid Motion |
| Se Hyeog Kim (김세혁) | M.S. (Aug 2026) |  | Definition of a Coronary Plaque Rupture Risk Index and Its Sensitivity Analysis |
| Hyeok Sul Kwon (권혁술) | M.S. (Feb 2026) |  | Estimating Coronary Blood Flow Using a Reduced-Order Model of the Advection-Diffusion Equation |
| Hyeonggue Song (송형규) | M.S. (Feb 2025) | Ph.D., KAIST | Development of multiscale computational methods for mass and heat transfer of the body tissue that considers interactions between the tissue and blood flow |
| Wonjin Choi (최원진) | M.S. (Feb 2025) | Ph.D., KAIST | Study on the variability and sensitivity of fractional flow reserve to pulsatile physiological uncertainties |
| Chang Min Lee (이창민) | M.S. (Feb 2024) | Ph.D., KAIST | Development and the application of the physiological model of the cerebrovascular system based on the supply-demand relationship of the arteries and tissues |
| Seung Min Lee (이승민) | M.S. (Feb 2024) | Ph.D., KAIST | Developing blood vessel generation model based on loss function minimization |
| Inpyo Lee (이인표) | M.S. (Aug 2023) |  | Developing a surrogate model for minimizing computational expense of pulsating blood flow simulation |
| Hans Christian Rundfeldt | M.S. (Feb 2023) | Ph.D., UMC Utrecht | Simulation of cerebrovascular perfusion using realistic synthetic tree generation (dual degree with KIT) |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지 Journal papers 목록의 2022–2026년 연도 구역 15편이다. 그보다 앞선 논문은 누리집이 「– 2021」 한 구역으로 묶어 적으며, 교수는 2021년 KAIST에 왔다. 제목·저자·학술지 표기는 누리집 그대로이고, 교수가 공동저자로 참여한 다른 연구실 주도 논문도 목록대로 실었다.[^pubs][^pi]

**2026**

- Youngjae Choi, Chang Min Lee, Kiwon Lee, Mihyun Lee, Seung-Hoon Kim, Yong-Soon Yoon, Hyun Jin Kim. "Computational investigation of intermittent pneumatic compression operating parameters and tissue mechanics in lower-limb venous hemodynamics". *Computers in Biology and Medicine 212:111767*.
- Wonjin Choi, Bon-Kwon Koo, Jung-Kyu Han, Inpyo Lee, Hyun Jin Kim. "Effects of pulsatile flow on fractional flow reserve assessed using a reduced-order model". *Annals of Biomedical Engineering*.
- Hyun Jin Kim, Chang Min Lee, Youngjae Choi, Hyeyeon Chang, Keun-Hwa Jung. "Multiscale modeling of posture-dependent cerebrovascular hemodynamics with autoregulatory coupling". *Computers in Biology and Medicine 203:111502*.
- Nolan Moreaux, Chang Min Lee, Bon-Kwon Koo, Keun-Hwa Jung, Jung-Kyu Han, Hyeyeon Chang, Hyun Jin Kim. "Computational Modeling of Collateral Circulation and Arteriolar Vasodilation in Ischemic Tissue Perfusion". *Annals of Biomedical Engineering*.
- Chang Min Lee, Youngjae Choi, Hyun Jin Kim. "Efficient multi-fidelity fluid-structure interaction modeling for pulsatile blood flow in deformable biological tissues". *Annals of Biomedical Engineering*.

**2025**

- C.H. Lee, S.K. Jeong, H.J. Kim, R.S. Rosenson, W. Yang, K.H. Jung. "Arteriopathic Effects of Hypertension by Signal Intensity Gradient from Time-of-Flight Magnetic Resonance Angiography". *Clinical Neuroradiology*.
- Chan-Hyuk Lee, Seul-Ki Jeong, Hyun Jin Kim, Robert S. Rosenson, Wookjin Yang, Keun Hwa Jung. "Association of Carotid Artery Stenosis with Cerebral Artery Signal Intensity Gradient on Time-of-Flight Magnetic Resonance Angiography". *Frontiers in Neurology 16:1576655*.
- Wonjin Choi, Inpyo Lee, Hyun Jin Kim. "Developing a reduced order model for pulsatile blood flow simulations using minimal three-dimensional simulation data". *Computer Methods and Programs in Biomedicine 271:108994*.
- Chang Min Lee, Hans Christian Rundfeldt, Keun-Hwa Jung, Hyeyeon Chang, Hyun Jin Kim. "Physiologic model of the cerebrovascular system using supply and demand between arteries and tissues". *Scientific Reports 15:27785*.
- J.P. Dmochowski, L. Cardoso, N. Khadka, K. Lee, S. Kim, K. Kim, H. Chun, S. Choo, H.J. Kim, A.D. Shereen, M. Bikson. "Assessing the Effect of Automated Thermo-Mechanical Therapy on Abdominal Blood Flow With Magnetic Resonance Imaging". *NMR in Biomedicine 38(5):e70024*.

**2024**

- D. Kwak, Y. Im, H. Nam, U. Nam, S. Kim, W. Kim, H.J. Kim, J. Park, J.S. Jeon. "Analyzing the effects of helical flow in blood vessels using acoustofluidic-based dynamic flow generator". *Acta Biomaterialia*.
- Hans Christian Rundfeldt, Chang Min Lee, Hanyoung Lee, Keun-Hwa Jung, Hyeyeon Chang, Hyun Jin Kim. "Cerebral Perfusion Simulation using Realistically Generated Synthetic Trees for Healthy and Stroke Patients". *Computer Methods and Programs in Biomedicine 244:107956*.

**2023**

- Hyun Jin Kim, Chang Min Lee, Hans Christian Rundfeldt, Inpyo Lee, Seungmin Lee, Kenneth Jansen. "Convergence of phase-averaged, transitional flow in an abdominal aortic aneurysmal model". *Journal of Biomechanical Engineering 145(11):111007*.
- Hyun Jin Kim, Hans Christian Rundfeldt, Inpyo Lee, Seungmin Lee. "Tissue-growth based Synthetic Tree Generation and Perfusion Simulation". *Biomechanics and Modeling in Mechanobiology 22:1095–1112*.

**2022**

- S.Y. Lee, M.H. Lee, S.K. Jo, I.H. Yoo, B.E. Sarankhuu, H.J. Kim, et al. "Effects and Mechanism of Particulate Matter on Tendon Healing Based on Integrated Analysis of DNA Methylation and RNA Sequencing Data in a Rat Model". *International Journal of Molecular Sciences 23(15):8170*.

## 과제

연구 페이지 「Ongoing funded projects」 표의 진행 중 과제 5건이다. 과제 이름, 지원 기관, 역할(Lead·Joint)은 표 그대로이고, 표에는 과제 기간이 적혀 있지 않다.[^research]

- Cardiovascular and cerebrovascular M3DT based on patient-specific diagnostic technology (지원 Ministry of Food and Drug Safety · KHIDI; 역할 Lead)
- Multiscale brain mechanics model for digital-twin-based brain monitoring (지원 Samsung Research Funding & Incubation Center; 역할 Lead)
- Integrated Neuro-Cardio Digital Twin for Early Detection of Brain Pathology (지원 National Research Foundation of Korea; 역할 Lead)
- Research center for a precision medicine platform based on smart hemodynamic indices (지원 National Research Foundation of Korea; 역할 Joint)
- Power-autonomous Subsea Engineering for Intelligent Data-center Operating Networks (지원 Ministry of Science and ICT; 역할 Joint)

## 수상

누리집 News 페이지에서 Award로 표시된 글 4건(2024년 4월–2025년 11월)이다. 모두 구성원의 학회 논문상이고, 날짜와 문장은 게시된 그대로다.[^news]

- 2025.11.07 · Chanhee An received the Best Paper Award at the 2025 Fall Conference of the Korean Society of Visualization, held in Pusan, Korea.
- 2025.09.13 · Wonjin Choi received the Best Paper Award at the 18th Asian Congress of Fluid Mechanics, held in Seoul, Korea.
- 2025.05.24 · Chang Min Lee received the Best Paper Award at 2025년 순환기의공학회 하계학술대회.
- 2024.04.19 · Chang Min Lee received the Best Paper Award (우수논문상) at KSME 유체공학부문 2024년 춘계학술강연회.

## 소식

누리집 News 페이지의 발표·강연·학위 과정 소식 46건(2022년 5월–2026년 8월)이다. 누리집의 소식 기록은 2022년 5월부터 시작한다. 날짜와 문장은 게시된 그대로다.[^news]

- 2026.08.27 · Hyun Jin Kim presented on “Digital twins for cardiovascular diseases: from modeling to clinical translation” at the International Federation of Automatic Control 2026 Busan.
- 2026.07.21 · Hyeonggue Song presented his research at the World Congress of Computational Mechanics in Munich, Germany.
- 2026.07.13 · Youngjae Choi, Seoyeon Kim, Chanhee An, and Wonjin Choi presented their research at the World Congress of Biomechanics in Vancouver, Canada.
- 2025.12.12 · Chanhee An presented her research at the 2025 Conference of the Korean Society of Mechanical Engineering in Jungsun, Korea.
- 2025.11.14 · Youngjae Choi presented his research at the 2025 Fall Conference of the Korean BioChip Society in Jeju Island, Korea.
- 2025.11.06 · Chanhee An presented her research at the 2025 Fall Conference of the Korean Society of Visualization in Pusan, Korea.
- 2025.09.12 · Wonjin Choi presented his research at the 18th Asian Congress of Fluid Mechanics in Seoul, Korea.
- 2025.07.23 · Wonjin Choi and Chang Min Lee presented their research at the 18th US National Congress on Computational Mechanics in Chicago, USA.
- 2025.05.23 · Chang Min Lee presented his research at 2025년 순환기의공학회 하계학술대회.
- 2025.02.14 · Hyeonggue Song and Wonjin Choi completed their M.S. degrees.
- 2024.11.08 · Hyeonggue Song, Wonjin Choi, Nolan Rene Moreaux and Chang Min Lee presented their research at the KSME 2024 Annual Meeting (대한기계학회 2024년 학술대회) in Jeju Island, Korea.
- 2024.08.29 · Wonjin Choi and Chang Min Lee presented their research at the 26th International Congress of Theoretical and Applied Mechanics in Daegu, Korea.
- 2024.08.26 · Hyeonggue Song presented his research at the 26th International Congress of Theoretical and Applied Mechanics in Daegu, Korea.
- 2024.04.18 · Hyun Jin Kim presented in the Department of Mechanical Engineering, Kyung Hee University.
- 2023.12.07 · Seung Min Lee completed her final presentation in the master’s program.
- 2023.12.05 · Chang Min Lee completed his final presentation in the master’s program.
- 2023.12.02 · Hyun Jin Kim presented at 순환기의공학회 동계학술대회.
- 2023.11.21 · Hyeonggue Song presented his research at the 76th Annual Meeting of the APS Division of Fluid Dynamics in Washington, D.C., USA.
- 2023.11.20 · Seung Min Lee and Chang Min Lee presented their research at the 76th Annual Meeting of the APS Division of Fluid Dynamics in Washington, D.C., USA.
- 2023.11.06 · Hyun Jin Kim presented at KIST 의사과학자 양성사업 온라인 세미나.
- 2023.09.20 · Hyun Jin Kim presented at Daejeon Science High School.
- 2023.08.07 · Chang Min Lee and Seung Min Lee completed their proposal presentations in the master’s program.
- 2023.07.25 · Hans Christian Rundfeldt presented his research at the 17th U.S. National Congress on Computational Mechanics.
- 2023.06.30 · Hyun Jin Kim presented at 2023년 한국전산역학회 학술대회.
- 2023.06.27 · Hyun Jin Kim presented at ERC 정기 세미나.
- 2023.06.17 · Hyun Jin Kim presented at 순환기의공학회 하계학술대회.
- 2023.06.14 · Inpyo Lee and Asem Mahmoud completed their final presentations in the master’s program.
- 2023.05.21 · Hyun Jin Kim presented at AI 기반 디지털 바이오 심포지엄.
- 2023.05.18 · Chang Min Lee presented his research at KSME 유체공학부문 2023년 춘계학술대회.
- 2023.05.11 · Hyun Jin Kim presented at 정밀공학회 젊은 공학자 초청 세션.
- 2023.04.19 · Hyun Jin Kim presented at 서울대학교병원 SGR Seminar.
- 2023.04.11 · Hyun Jin Kim presented at 서울대학교 기계공학부 유체공학 세미나.
- 2023.02.23 · Inpyo Lee and Asem Mahmoud completed their proposal presentations in the master’s program.
- 2022.12.19 · Hans Christian Rundfeldt completed his final defense in the master’s program.
- 2022.12.09 · Hyun Jin Kim presented at 2022 SCRC 심포지엄.
- 2022.12.02 · Hans Christian Rundfeldt and Inpyo Lee presented their research at 2022년 가시화학회 추계학술대회.
- 2022.10.10 · Hyun Jin Kim presented at 대한기계학회 2022년도 학술대회.
- 2022.10.09 · Hyun Jin Kim presented at 제10회 서울아산병원 의공학연구소 심포지엄.
- 2022.10.04 · Hyun Jin Kim presented at 한국중재의료기기학회 2022년도 추계학술대회.
- 2022.09.24 · Hyun Jin Kim presented at 대한심장학회 제66차 추계학술대회.
- 2022.09.20 · Hyun Jin Kim presented at the 20th Asian Oceanian Congress of Radiology and the 78th Annual Meeting of the Korean Society of Radiology.
- 2022.08.23 · Hans Christian Rundfeldt completed his midterm presentation in the master’s program.
- 2022.06.25 · Hyun Jin Kim presented in the biofluid session at the 2022 Annual Meeting of the Korean Society for Mathematical Biology (2022 한국수리생물학회 연례 학술대회).
- 2022.06.23 · Hyun Jin Kim presented in the biological fluid session at the 12th National Congress on Fluids Engineering (제12회 한국유체공학학술대회).
- 2022.05.20 · Hyun Jin Kim presented at 2022년 가시화학회 춘계학술대회.
- 2022.05.05 · Hyun Jin Kim presented at 대한기계학회 바이오공학부문 2022년 춘계학술대회.

## 연락과 위치

- 연구실: Room 6123 & 6124, Building N7-4, Department of Mechanical Engineering, KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon 34141[^home]
- 교수실과 전화: 기계동(N7) 6112, 042-350-7925[^meprof]
- 교수 이메일: kim.hyunjin@kaist.ac.kr[^meprof]
- Openings 페이지는 학부생·석사과정·박사과정 자리가 열려 있고, 기계공학·생명공학·응용수학·컴퓨터과학 배경의 지원자를 환영하며, 수치 시뮬레이션이나 의료 영상 경험은 도움이 되지만 필수는 아니라고 안내한다.[^openings]
[^p1]: C. M. Lee 외, H. J. Kim, Annals of Biomedical Engineering 54, 3124-3139 (온라인 2026-03-11). <https://doi.org/10.1007/s10439-025-03966-x> 초록 기준.
[^p2]: W. Choi, I. Lee, H. J. Kim, Computer Methods and Programs in Biomedicine 271, 108994 (2025). <https://doi.org/10.1016/j.cmpb.2025.108994> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: W. Choi 외, H. J. Kim, Annals of Biomedical Engineering (온라인 2026-07-24). <https://doi.org/10.1007/s10439-026-04292-6> 초록 기준.
[^p4]: H. J. Kim 외, K. Jansen, Journal of Biomechanical Engineering 145, 111007 (온라인 2023-08-11). <https://doi.org/10.1115/1.4063066> 초록 기준.
[^p5]: Y. Choi 외, H. J. Kim, Computers in Biology and Medicine 212, 111767 (2026). <https://doi.org/10.1016/j.compbiomed.2026.111767> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: H. J. Kim 외, K.-H. Jung, Computers in Biology and Medicine 203, 111502 (2026). <https://doi.org/10.1016/j.compbiomed.2026.111502> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: N. Moreaux 외, H. J. Kim, Annals of Biomedical Engineering 54, 3446-3464 (온라인 2026-03-13). <https://doi.org/10.1007/s10439-026-04052-6> 초록 기준.
[^p8]: H. J. Kim, H. C. Rundfeldt, I. Lee, S. Lee, Biomechanics and Modeling in Mechanobiology 22, 1095-1112 (온라인 2023-03-04). <https://doi.org/10.1007/s10237-023-01703-8> 초록 기준.
[^home]: 전산역학 및 생체역학 연구실 누리집 첫 화면 <https://cmb.kaist.ac.kr/> (연구실 소개, Research areas, News, Openings, 주소, 2026-10-23 열람)
[^research]: 연구실 누리집 Research 페이지 <https://cmb.kaist.ac.kr/research/> (연구 소개, 세 연구 영역, Ongoing funded projects, 2026-10-23 열람)
[^mm]: 연구실 누리집 Research 「Multiscale and Multiphysics Modeling」 페이지 <https://cmb.kaist.ac.kr/research/multiscale-multiphysics/> (2026-10-23 열람)
[^uq]: 연구실 누리집 Research 「Efficient Computational Modeling and Uncertainty Quantification」 페이지 <https://cmb.kaist.ac.kr/research/efficient-modeling-uq/> (2026-10-23 열람)
[^coronary]: 연구실 누리집 Research 「Coronary Hemodynamics and Ischemic Heart Disease」 페이지 <https://cmb.kaist.ac.kr/research/coronary/> (2026-10-23 열람)
[^aneurysm]: 연구실 누리집 Research 「Abdominal Aortic Aneurysm Hemodynamics and Mechanics」 페이지 <https://cmb.kaist.ac.kr/research/aneurysm/> (2026-10-23 열람)
[^venous]: 연구실 누리집 Research 「Venous Hemodynamics and Intermittent Pneumatic Compression」 페이지 <https://cmb.kaist.ac.kr/research/venous/> (2026-10-23 열람)
[^cerebral]: 연구실 누리집 Research 「Cerebral Perfusion and Autoregulation」 페이지 <https://cmb.kaist.ac.kr/research/cerebral-perfusion/> (2026-10-23 열람)
[^networks]: 연구실 누리집 Research 「Cerebrovascular Networks and Collateral Circulation」 페이지 <https://cmb.kaist.ac.kr/research/cerebrovascular-networks/> (2026-10-23 열람)
[^pi]: 연구실 누리집 Principal investigator 페이지 <https://cmb.kaist.ac.kr/pi/> (Education, Experience, Honors, 2026-10-23 열람)
[^people]: 연구실 누리집 Members 페이지 <https://cmb.kaist.ac.kr/people/> (Ph.D. Students, M.S. Students, Researchers, Alumni, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publications 페이지 <https://cmb.kaist.ac.kr/publications/> (Journal papers 42건, 2026-10-23 열람)
[^news]: 연구실 누리집 News 페이지 <https://cmb.kaist.ac.kr/news/> (News & events, 2026-10-23 열람)
[^teaching]: 연구실 누리집 Teaching 페이지 <https://cmb.kaist.ac.kr/teaching/> (2026-10-23 열람)
[^openings]: 연구실 누리집 Openings 페이지 <https://cmb.kaist.ac.kr/openings/> (2026-10-23 열람)
[^meprof]: KAIST 기계공학과 교수 소개(김현진) <https://me.kaist.ac.kr/pop/team.html?uid=103&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 연구실 웹사이트, 이메일, 사무실, 전화, 2026-10-23 열람)
[^meres]: KAIST 기계공학과 연구분야 「헬스케어/나노/광학」 <https://me.kaist.ac.kr/research/research_010400.html> (김현진 교수 항목, 2026-10-23 열람)

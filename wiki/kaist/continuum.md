# Solids Lab @ KAIST (Hansohl Research LAB)

**KAIST 기계공학과 · 조한솔 교수**

- 분야: 고체역학·연속체 역학, 탄성체·고분자 고체의 큰 변형과 파괴, 체심입방 금속 결정의 소성, 극한 하중 아래 재료 모델의 통계적 추론과 불확실성 정량화, 구조 설계 결정체와 무질서 소재, 3D·4D 프린팅 소재의 미세역학
- 대분야: 기계·로봇·제조, 소재
- 태그: 연성 소재·고분자[^cont][^p1][^p8], 3D 프린팅[^micro][^geometry][^p7], 과학·공학 AI[^extreme]
- 홈페이지: <https://continuum.kaist.ac.kr/>
- 근거와 출처: [Solids Lab 근거 페이지](continuum-sources.md)

> 고체와 응집 물질(원자·분자가 촘촘히 모여 있는 고체·액체 상태의 물질)이 크게 변형되고 흐르고 서로 작용할 때의 역학 원리를 밝히고, 그 이해를 바탕으로 극한·다중 물리 환경에서 쓸 새 소재, 미세구조, 장치를 더 잘 설계하도록 돕는 연구실이다.[^home]

## 무엇을 연구하나

연구실은 고체역학(고체가 힘을 받아 변형하고 부서지는 것을 다루는 학문)과 응집 물질의 새로운 영역에서 어려운 문제를 다룬다고 소개한다. 중심 과제는 고체와 응집 물질의 큰 변형, 흐름, 상호작용이 어떤 역학 기구로 일어나는지 이해하고, 그 이해를 극한·다중 물리 환경의 새 소재와 미세구조, 장치 설계에 쓰는 것이다.[^home] 연구 페이지는 이 일을 이론 역학, 응용·계산 수학과 물리, 재료과학이 만나는 자리에서 한다고 적고, 연구 주제로 고분자 고체·액체와 결정 물질의 연속체·통계 역학과 유변학(물질이 힘을 받아 흐르고 변형하는 성질을 다루는 학문), 다기능 기계 장치와 로봇형 물질의 미세역학·기하·위상과 적층 제조, 극한·결합 환경의 고체·소재·장치를 위한 과학 계산과 불확실성 정량화(모델 예측이 얼마나 불확실한지 수치로 따지는 방법)를 든다.[^research]

방법의 중심은 연속체 역학(물질을 끊김 없이 이어진 덩어리로 보고 힘과 변형의 관계를 식으로 다루는 이론)이다. 연구실은 이를 이론 모델링, 실험, 계산을 함께 쓰는 방식으로 적용하며, 아주 부드러운 소재부터 매우 단단한 금속 결정(5·6족의 내화 금속(녹는점이 아주 높은 금속) 등)까지를 대상으로 삼는다.[^cont]

연구 페이지는 연구를 네 갈래로 나눈다. 연성 소재부터 금속 결정까지의 연속체 역학, 극한·희귀 사건의 통계 역학과 통계적 추론, 「소재가 곧 기계」라는 구조 설계 소재, 불균질 소재의 미세역학과 3D·4D 프린팅이다.[^research]

## 주요 연구 주제

### 1. 연속체 역학: 연성 소재의 손상·파괴와 금속 결정의 소성

연구실은 고분자 고체·액체와 결정 물질이 극한 또는 결합된 환경에서 크게 변형되고 흐르는 원리를 연속체 역학으로 이해하려 한다.[^cont] 연성 소재 쪽에서는 손상, 파괴, 치유를 반응, 확산, 탄성이 함께 얽힌 화학·기계 결합 현상으로 보고, 실제 고분자 그물 구조와 연성 소재에서 일어나는 이 과정을 담는 연속체 구성 이론(소재에 가한 힘과 그 변형의 관계를 정하는 식)을 분자 수준 사건의 통계 역학 원리에서 착안해 만든다. 목표는 합성·자연 연성 소재의 큰 변형과 파단을 예측하는, 결정론적 방법과 통계 역학 방법을 함께 쓰는 틀이다.[^extreme] 탄성체(고무처럼 크게 늘어났다가 돌아오는 고분자 소재)의 흠 크기에 따라 달라지는 파괴(대표 논문 1)와 아주 빠른 변형률 속도까지의 폴리우레탄-우레아 탄성체 모델(대표 논문 2)이 이 갈래의 논문이다.[^p1][^p2]

금속 결정 쪽에서는 체심입방(정육면체 꼭짓점과 가운데에 원자가 놓인 결정 구조) 금속의 결정 소성(결정 속 원자 면이 미끄러지며 생기는 영구 변형)을 다룬다. 탄탈럼의 변형 기구와 전위(결정 속 원자 배열이 어긋난 선 모양 결함)의 변화를 단결정과 다결정 수준에서 설명하는 모델(대표 논문 4)이 있다.[^p4]

### 2. 극한·희귀 사건의 통계적 추론

연구실은 충돌·충격 같은 복잡한 하중에서 소재, 미세구조, 장치에 생기는 손상·파괴 같은 극한·희귀한 기계적 사건을 예측하려고 통계적 추론, 기계학습, 불확실성 정량화 기법을 쓴다. 지금은 5·6족 내화 금속 같은 금속 단결정·다결정에 집중하고, 앞으로 비정질(원자 배열에 규칙이 없는) 연성 소재와 장치로 넓히려 한다.[^extreme] 베이즈 추론(관측 자료로 모델 변수의 확률 분포를 고쳐 나가는 방법)으로 체심입방 몰리브덴 단결정 모델의 변수와 불확실성을 따진 연구(대표 논문 3)가 이 갈래의 논문이다.[^p3]

### 3. 소재가 곧 기계: 구조 설계 결정체와 무질서 소재

연구실은 구조 설계 단결정·다결정(내부 구조를 설계해 결정과 같은 배열로 만든 소재)을 설계하고 3D 프린팅해 그 극한 역학을 보인다. 이렇게 크기를 키운 방법으로 원자 결정 속 결정립(결정 하나하나의 알갱이) 안과 결정립 사이의 기구를 눈으로 보려 하고, 새 불균질 소재와 장치에서 거시적 상변태(물질의 상태가 바뀌는 현상)와 상분리가 나타나게 해 「소재가 곧 기계」임을 보이려 한다.[^geometry] 단단한 성분과 부드러운 성분으로 만든 구조 설계 다결정에서 결정립 경계 설계의 역할을 살핀 연구(대표 논문 5)가 이 갈래의 논문이다.[^p5]

또 다른 줄기는 무질서 물질의 역학, 기하, 통계다. 내부 대칭과 장거리 질서를 가진 구조 설계 소재에서는 얻지 못한 기계·화학·광학 기능을 얻으려고 미세구조의 무질서를 설계하고 이용하며, 그 바탕의 물리·수학 원리를 밝히려 한다.[^geometry] 방향에 거의 상관없는 회복력과 에너지 소산을 보이는 불균질 무질서 소재(대표 논문 6)가 이 줄기의 논문이다.[^p6]

### 4. 불균질 소재의 미세역학과 3D·4D 프린팅

새 적층 제조 기술을 키우려면 미세구조, 공정, 성질 사이의 관계를 이해해야 한다는 것이 연구 페이지의 설명이다. 연구실은 3D·4D 프린팅(시간이 지나거나 자극을 받으면 모양이 바뀌도록 프린팅하는 방식)한 소재, 부품, 장치의 거시적 기계적 특징을 예측하는 미세역학(소재 속 작은 구조의 변형으로 전체 성질을 설명하는 역학) 도구를 만들고, 이 방법으로 정밀한 다중 소재 3D·4D 프린팅 공정의 역학적 근거를 마련한다.[^micro] 3D 프린팅한 디지털 소재가 큰 변형에서 보이는 방향에 따른 성질 차이를 다룬 연구(대표 논문 7)가 이 갈래의 논문이다.[^p7]

상분리 고분자(서로 섞이지 않는 성분이 나뉘어 두 영역을 이룬 고분자)의 역학도 다룬다. 고무 같은 성질과 열가소성(열을 받으면 무르고 식으면 굳는 성질) 특징을 함께 가진 다상 고분자·탄성체에서 작은 변형부터 극한 변형까지의 미세 변형 기구를 탐구하는 방법을 개발하며, 실제 상분리 연성 소재에서 흔한 미세구조를 흉내 낸 모델을 쓴다.[^micro] 무작위 미세구조를 가진 열가소성 탄성체의 큰 변형 미세역학 연구(대표 논문 8)가 이 줄기의 논문이다.[^p8]

## 대표 논문

조한솔 교수가 저자인 2023–2026년 학술지 논문 가운데 연구 페이지의 네 갈래에 고르게 담기도록 여덟 편을 골랐다. 여섯 편은 교수가 마지막 저자이고, 4번은 두 번째 저자, 8번은 첫 저자이며, 여덟 편 모두 누리집 목록이 교수를 교신저자로 표시한다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2024 | [Size-dependent fracture in elastomers: Experiments and continuum modeling](https://doi.org/10.1103/physrevmaterials.8.115602) · Physical Review Materials | 탄성체는 들어 있는 흠의 크기에 따라 늘어나는 정도와 파괴 성질이 크게 달라진다. 이 연구는 실험과 수치 시뮬레이션을 함께 써서, 이 크기 의존 파괴를 비국소 연속체 모델(한 점의 상태를 그 주변 영역까지 함께 고려해 계산하는 모델)로 정량적으로 설명했다. 모델의 핵심은 유한한 파괴 진행 영역에 해당하는 고유 길이 척도이고, 이 값은 실험에서 추정했다. 중간 정도(~100%)에서 매우 큰(~1000%) 신축성을 가진 여러 합성 탄성체와 복잡한 형상의 시편에 적용했다. | 1저자 J. Lee, 마지막·교신 저자 조한솔 (7명) |
| 2 | 2023 | [A polyurethane-urea elastomer at low to extreme strain rates](https://doi.org/10.1016/j.ijsolstr.2023.112360) · International Journal of Solids and Structures | 여러 공학 용도에 알맞은 폴리우레탄-우레아 탄성체의 극한 역학 거동을 다루는 유한 변형 비선형 구성 모델을 내놓았다. 미세역학과 열역학에 바탕을 둔 이 모델은 낮은 변형률 속도부터 높은 변형률 속도까지 소재의 회복력과 에너지 소산을 담아낸다. 레이저로 미세 입자를 쏘아 부딪치게 하는 충돌 시험에서는 변형률 속도가 10⁶ s⁻¹를 넘었고, 이 불균질한 변형을 모사한 결과가 실험과 잘 맞았다. 이는 10⁻³–10⁶ s⁻¹, 적어도 9자릿수에 걸친 변형률 속도에서 모델의 예측력을 뒷받침한다. | 1저자 J. Lee, 마지막·교신 저자 조한솔 (5명) |
| 3 | 2026 | [Bayesian inference and uncertainty quantification for modeling of body-centered-cubic single crystals](https://doi.org/10.1016/j.ijplas.2026.104678) · International Journal of Plasticity | 체심입방 단결정을 예측하는 모델은 재료 변수가 많아 불확실성이 크고, 극한 하중에서 특히 어렵다. 이 연구는 정적 하중부터 충격파 하중까지 받는 몰리브덴 단결정에 대해, 서로 다른 변형 기구를 앞세운 두 결정 소성 모델의 재료 변수를 베이즈 모델 보정으로 확률적으로 추정했다. 전역 민감도 분석으로 변수의 불확실성이 정적·충격 응답 시뮬레이션에 주는 영향을 정량화했고, 보정 범위 밖에서도 두 모델을 검증해 충격 하중 아래 탄소성 응답을 좌우하는 물리 기구를 찾았다. | 1저자 S. Lee, 마지막·교신 저자 조한솔 (6명) |
| 4 | 2023 | [Deformation, dislocation evolution and the non-Schmid effect in body-centered-cubic single- and polycrystal tantalum](https://doi.org/10.1016/j.ijplas.2023.103529) · International Journal of Plasticity | 기계·열적 극한 환경의 핵심 구조 소재로 쓰이는 체심입방 탄탈럼의 변형 기구와 전위 변화를 설명하는 물리 기반 연속체 결정 소성 모델을 내놓았다. 중간 규모 전위 동역학 시뮬레이션에서 정보를 얻은 이 모델은 정적(10⁻³ s⁻¹)부터 극한(5000 s⁻¹)까지의 변형률 속도와 상온 및 더 높은 온도(873K)에서 단결정·다결정의 큰 비탄성 거동을 담아낸다. 다결정 시편에서는 변형이 커지면서 결정 방위 분포와 전위 밀도가 어떻게 바뀌는지 측정했고, 시뮬레이션이 넓은 범위의 변형, 변형률 속도, 온도에서 다결정 거동의 주요 특징을 재현했다. | 1저자 S. Lee, 교신 저자 조한솔(2번째, 10명) |
| 5 | 2025 | [Stiffness, strength, energy dissipation and reusability in heterogeneous architected polycrystals](https://doi.org/10.1098/rspa.2025.0268) · Proceedings of the Royal Society A | 단단한 플라스토머(힘을 받으면 영구 변형하는 고분자)와 부드러운 엘라스토머로 이루어진 불균질 구조 설계 다결정을 설계·제작·시험해 회복력과 에너지 소산을 함께 보이게 했다. 무작위 방향의 결정립을 나누는 결정립 경계를 설계해 경계 영역 전체에 연결성과 강도를 주었다. 3D 프린팅한 시제품의 실험과 수치 시뮬레이션으로, 결정립 내부와 경계의 상호작용이 탄성 강성과 비탄성 강도의 결정립 크기 효과를 만든다는 것과, 손상 뒤에는 설계한 경계가 국부 파손의 전파를 막아 재사용성과 에너지 소산 능력에 결정적이라는 것을 보였다. | 1저자 S. Lee, 마지막·교신 저자 조한솔 (2명) |
| 6 | 2025 | [Extreme resilience and dissipation in heterogeneous disordered materials](https://doi.org/10.1016/j.jmps.2025.106246) · Journal of the Mechanics and Physics of Solids | 결정 격자 위에 설계한 불균질 소재는 장거리 질서와 대칭 때문에 탄성·비탄성 성질이 방향에 따라 달라진다. 이 연구는 방향에 거의 상관없는 회복력과 에너지 소산 능력을 보이는 불균질 무질서 소재를 쉽게 설계하는 방법을 내놓았다. 3D 프린팅한 시제품의 실험과 수치 시뮬레이션으로 적은 수의 무작위 점만으로도 거의 완전한 등방성(성질이 방향과 무관함)을 얻을 수 있음을 보였고, 무작위 하위 영역 사이에 연결성을 더하면 탄성 강성, 소성 강도, 에너지 소산, 형상 회복, 구조 안정성, 재사용성이 크게 향상됨을 보였다. | 1저자 J. Moon, 마지막·교신 저자 조한솔 (4명) |
| 7 | 2026 | [Mechanical anisotropy of 3D-printed digital materials at large strains](https://doi.org/10.1039/d6sm00036c) · Soft Matter | 3D 프린팅한 불균질 연성 소재가 큰 변형에서 방향에 따라 다른 역학 성질을 보이는 바탕의 미세구조 기구를 다뤘다. 이를 위해 기계 실험, 현미경 분석, 미세역학 모델링을 함께 썼다. | 1저자 S. Lee, 마지막·교신 저자 조한솔 (6명) |
| 8 | 2024 | [Large strain micromechanics of thermoplastic elastomers with random microstructures](https://doi.org/10.1016/j.jmps.2024.105615) · Journal of the Mechanics and Physics of Solids | 열가소성 폴리우레탄(TPU)은 플라스토머 성질의 「단단한」 영역과 탄성체 성질의 「부드러운」 영역으로 이루어진 블록 공중합체(성질이 다른 고분자 사슬 토막이 이어진 고분자)로, 두 영역의 부피 비율과 미세구조에 따라 회복력이 크면서도 에너지를 소산하는 큰 변형 특성을 보인다. 이 연구는 매우 무질서한 미세구조를 가진 TPU의 미세 변형 기구를 다루는 새 방법을 개발했다. 단단한 영역이 무작위로 흩어진 경우와 무작위로 이어진 경우의 새 미세역학 모델을 단단한 영역 부피 비율 26.9%–52.2%에서 제안하고, 앞서 보고된 거시적 큰 변형 실험 자료와 비교했으며, 두 형태의 차이가 미세구조 수준의 형상 회복과 에너지 소산에 주는 역할을 살폈다. | 1저자·교신 저자 조한솔, 마지막 저자 M. C. Boyce (7명) |

## 교수와 전문 분야

조한솔 교수는 KAIST 기계공학과 교수진 목록과 교수 소개에 올라 있다. 학과 교수 소개는 연구분야를 Solid mechanics, continuum mechanics, soft/hard condensed matter로, 연구실을 「Solids Lab @ KAIST」로 적는다.[^meprof][^melist]

연구실 누리집의 교수 소개에 따르면 교수는 서울대학교에서 조선해양공학과 기계항공공학 학사(2004)를 받았고(Outstanding MAE S.B. Thesis Award), MIT에서 기계공학 석사(2009)와 박사(2014)를 받았다. 박사 과정의 부전공은 Applied Quantum and Statistical Mechanics이고, Kwan-Jeong Scholarship을 받았으며, 지도교수는 M. C. Boyce다. 대우조선해양(Daewoo Shipbuilding and Heavy Industries)의 Member of Technical Staff(2004–2007), Sandia National Laboratories LAMMPS 연구조교(2008), MIT 기계공학과 연구조교(2008–2014), MIT 화학공학과 박사후연구원(2014–2016), Los Alamos National Laboratory 이론 부문 T3 박사후연구원(2016–2018)을 거쳐 2019년부터 KAIST에 있다. 교수 소개는 KAIST 직위를 기계공학 조교수·부교수(2019–2024년에는 항공우주와 함께)로 적고, MIT 화학공학과 방문학자(2024–2025)도 적는다.[^prof] 연구실 소식은 연구실이 2025년 3월 KAIST 기계공학과로 옮겨 합류했다고 적는다.[^newsarc]

KAIST 부임 전 논문은 누리집 목록이 「pre kaist」 아래 따로 둔다. 탄탈럼 단결정·쌍결정의 미세 기둥 압축(2019), 비슈미트 효과(결정면의 미끄러짐이 그 면 방향의 전단 응력만으로 정해지지 않는 현상)를 가진 체심입방 금속의 소성(2018), 열가소성 탄성체의 변형 기구와 구성 모델링(2017), 불균질 연성 결정의 역학(2016), 탄성 공중합체의 큰 변형과 테일러 충격 거동(2015), 분절 공중합체·폴리우레아의 회복력과 소산(2013–2014) 같은 연구가 있고, 분자 동역학 프로그램 LAMMPS의 ReaxFF 퍼텐셜(2010)도 목록에 있다.[^pubs]

논문으로 보면 KAIST에서의 전문 분야는 탄성체의 크기 의존 파괴와 극한 변형률 속도 모델 같은 연성 소재의 연속체 역학(대표 논문 1, 2), 체심입방 금속 결정의 소성과 그 모델의 통계적 추론(대표 논문 3, 4), 구조 설계 다결정과 무질서 소재(대표 논문 5, 6), 3D 프린팅 소재와 열가소성 탄성체의 미세역학(대표 논문 7, 8)이다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

연구실은 극한·다중 물리 환경에서 쓸 새 소재, 미세구조, 장치의 설계를 연구의 쓰임으로 적는다.[^home] 연구 페이지는 손상·파괴 예측의 대상 하중으로 충돌과 충격을 들고,[^extreme] 정밀한 다중 소재 3D·4D 프린팅 공정에 역학적 근거를 주는 것을 미세역학 연구의 쓰임으로 적는다.[^micro] 대표 논문은 탄탈럼을 기계·열적 극한 환경의 핵심 구조 소재로, 폴리우레탄-우레아를 여러 공학 용도에 맞는 소재로 소개한다.[^p2][^p4]

## 구성원

누리집 Our Team 페이지의 구성원 8명이다. 과정과 시작 연도는 각 소개 첫 줄의 표기이고, 연구 주제는 소개 끝 줄의 표기 그대로이며, 이름 옆 괄호는 함께 적힌 국문 이름이다. Jaehee Lee는 장영실 Fellow(Cornell + KAIST), Seunghyeon Lee는 InnoCore Fellow로 적혀 있다.[^team] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Jaehee Lee (재희) | 장영실 Fellow, Cornell + KAIST | 2025 | soft matter, coupled, continuum mechanics, variational principles | 1, 2, 6, 8 |
| Gisoo Lee (기수) | 박사과정 | 2022 | micromechanics + phase separation, mechanics + 3d/4d printing | 6, 7 |
| Seunghyeon Lee (승현) | InnoCore Fellow, KAIST | 2026 | crystal plasticity, statistical inference + uncertainty quantification | 3, 4 |
| Jehoon Moon (제훈) | 박사과정 | 2024 | mechanics + transport + photonics, disordered matter, statistical mechanics | 6, 8 |
| Seunghwan Lee (승환) | 박사과정 | 2024 | polycrystals + grain boundaries, mechanics + 3d/4d printing | 5, 7 |
| Jeongun Lee (정운) | 박사과정 | 2025 | continuum + statistical mechanics, soft matter, polymer physics | 1 |
| Seunghee Yun (승희) | 박사과정 | 2024 | co-advised by Prof Sanha Kim; mechanics and (micro-) manufacturing, liquid crystalline elastomers | 1, 7 |
| Danbi Kim (단비) | S.M. Course | 2025 |  |  |

## 졸업생과 학부 참여자

누리집 Our Team 페이지 「Alum & Thesis」의 학위 8건(박사 2건, 석사 6건, 2021–2026년)과 「Undergraduates, Friends & Visitors」 칸의 12명이다. 학위 논문 제목과 진로는 페이지 표기 그대로이고, 같은 사람이 석사와 박사로 두 번 나오는 경우가 있다. 학부 참여자 칸의 기간은 페이지 표기이며, 기간이 적혀 있지 않은 이름도 있다.[^team]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Seunghyeon Lee | Ph.D. (2026) | InnoCore Fellow, KAIST | Extreme deformation of body-centered cubic crystals: Constitutive modeling and uncertainty quantification |
| Jaehee Lee | Ph.D. (2025) | Postdoctoral Associate, Silberstein Lab + Roeder Lab, Cornell University | Extreme deformation and fracture in elastomers: Experiments and multiscale-multiphysics-multiphase modeling |
| Jeongun Lee | S.M. (2025) | Ph.D. Candidate, KAIST | Damage, fracture and viscoelasticity in elastomers |
| Jehoon Moon | S.M. (2024) | Ph.D. Candidate, KAIST | Extreme resilience and dissipation in heterogeneous disordered materials |
| Seunghwan Lee | S.M. (2024) | Ph.D. Candidate, KAIST | Stiffness, strength, dissipation and reusability in heterogeneous architected polycrystals |
| Seunghyeon Lee | S.M. (2023) | Ph.D. Candidate, KAIST | Deformation and dislocation evolution in single- and polycrystal bcc materials |
| Gisoo Lee | S.M. (2022) | Ph.D. Candidate, KAIST | Extreme resilience and dissipation in elasto-plastomeric crystals |
| Jaehee Lee | S.M. (2021) | Postdoctoral Associate, Silberstein Lab + Roeder Lab, Cornell University | A polyurethane-urea elastomer at low to extreme strain rates |
| Yeosan Tak | Undergraduates, Friends & Visitors (Summer 2026 -) |  |  |
| Okjin Lee | Undergraduates, Friends & Visitors |  |  |
| Gayun Ko | Undergraduates, Friends & Visitors (Winter 2025) |  |  |
| Minho Kwon | Undergraduates, Friends & Visitors (Spring 2024) |  |  |
| Danbi Kim | Undergraduates, Friends & Visitors (Summer 2023 - Winter 2024) |  |  |
| Shinyoung Na | Undergraduates, Friends & Visitors |  |  |
| Sooyeon Ma | Undergraduates, Friends & Visitors (Summer 2022) |  |  |
| Jeongun Lee | Undergraduates, Friends & Visitors (Winter 2021 - Winter 2022) |  |  |
| Yin Oh | Undergraduates, Friends & Visitors (Summer 2021) |  |  |
| Jehoon Moon | Undergraduates, Friends & Visitors (Summer 2020 - Winter 2021) |  |  |
| Jaehee Chang | Undergraduates, Friends & Visitors (Summer 2020) |  |  |
| Gisoo Lee | Undergraduates, Friends & Visitors (Fall 2019 - Summer 2020) |  |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지 「papers + preprints」 목록 가운데 KAIST 부임 전 논문을 따로 둔 「pre kaist」 줄 위의 2021–2026년 항목 17편이다. 학술지 논문 14편과, 학술지 출판 전 사전 공개본으로 「arXiv, 2026」이라 적힌 3편이다. 제목·저자·학술지 표기는 누리집 그대로이고 저자 이름 뒤 †는 누리집이 적은 교신저자 표시다. 교수가 교신저자가 아닌 공동연구 논문도 목록대로 실었다.[^pubs]

**2026**

- J. Park, M. Batool, S. H. Lee, J. Moon, H. Cho, X. Ni†. "A liquid metal-epoxy system with spatio-temporally programmable multilevel stiffness". *arXiv, 2026*.
- J. Moon, S. H. Lee, G. Lee, J. U. Lee, H. Cho†. "Mechanical isotropy of heterogeneous octahedral materials". *arXiv, 2026*.
- G. Kim, T. Lee, M. Yoo, J. U. Lee, H. Cho, H. Lee†. "Phase-controlled bimodal four-dimensional printing of liquid crystal elastomers". *arXiv, 2026*.
- J. Jin, J. Bae, G. Lee, H. Cho, J. Lee†. "Cryogenic microcrack suppression and gas-barrier retention enabled by plasma-engineered pet nanomaterials". *Composites Science and Technology, 286, 2026*.
- G. Lee, J. U. Lee, J. Lee, J. An, H. Lee, H. Cho†. "Tunable viscoelasticity in phase-separated soft materials". *International Journal of Solids and Structures, 339, 2026*.
- S. H. Lee, G. Lee, S. Yun, S. Lee, J. Lee, H. Cho†. "Mechanical anisotropy of 3D-printed digital materials at large strains". *Soft Matter, 22 (28), 2026*.

**2025**

- S. Lee, T. Ngyuen, D. J. Luscher, S. J. Fensin, J. S. Carpenter, H. Cho†. "Bayesian inference and uncertainty quantification for modeling of body-centered-cubic single crystals". *International Journal of Plasticity, 201, 2025*.
- S. H. Lee, H. Cho†. "Stiffness, strength, energy dissipation and reusability in heterogeneous architected polycrystals". *Proceedings of the Royal Society A, 481, 2324, 2025*.
- J. Moon, G. Lee, J. Lee, H. Cho†. "Extreme resilience and dissipation in heterogeneous disordered materials". *Journal of the Mechanics and Physics of Solids, 204, 2025*.

**2024**

- J. Lee, J. U. Lee, S. Yun, H. Lee, H. Cho†. "Size-dependent fracture in elastomers: Experiments and continuum modeling". *Physical Review Materials, 8 (11), 2024*.
- H. Cho†, J. Lee, J. Moon, E. Pöselt, G. C. Rutledge, M. C. Boyce. "Large strain micromechanics of thermoplastic elastomers with random microstructures". *Journal of the Mechanics and Physics of Solids, 187, 2024*.
- G. Lee, J. Lee, S. Lee, S. Rudykh, H. Cho†. "Extreme resilience and dissipation in heterogeneous elasto-plastomeric crystals". *Soft Matter, 20 (2), 2024*.

**2023**

- Y. Zhang, N. Chen†, C. A. Bronkhorst, H. Cho, R. Argus. "Data-driven statistical reduced-order modeling and quantification of polycrystal mechanics leading to porosity-based ductile damage". *Journal of the Mechanics and Physics of Solids, 179, 2023*.
- J. Lee, S. Lee, S. A. Chester, H. Cho†. "Finite element implementation of a gradient-damage theory for fracture in elastomeric materials". *International Journal of Solids and Structures, 279, 2023*.
- J. Lee, D. Veysset, A. J. Hsieh, H. Cho†. "A polyurethane-urea elastomer at low to extreme strain rates". *International Journal of Solids and Structures, 280, 2023*.
- S. Lee, H. Cho†, C. A. Bronkhorst, R. Pokharel, D. W. Brown, B. Clausen, S. C. Vogel, V. Anghel, G. T. Gray III, J. R. Mayeur. "Deformation, dislocation evolution, slip instability and the non-Schmid behavior in body-centered-cubic single- and polycrystalline tantalum". *International Journal of Plasticity, 163, 2023*.

**2021**

- C. A. Bronkhorst†, H. Cho†, P. W. Marcy, S. A. Vander Wiel, D. Versino, S. Gupta, V. Livescu, G. T. Gray III. "Local micro-mechanical stress conditions leading to pore nucleation during dynamic loading". *International Journal of Plasticity, 137, 2021*.

## 학회 발표

누리집 Publications 페이지 「Recent Presentations」의 5건(2024–2026년)이다. 제목·발표자·학회 표기는 누리집 그대로다.[^pubs]

- H. Cho, S. Lee, T. Ngyuen, D. J. Luscher, S. J. Fensin. "Statistical inference and uncertainty quantification for modeling of bcc single crystals". *International Conference on Plasticity, Damage and Fracture (ICPDF), Geelong, 2026*.
- S. H. Lee, G. Lee, S. Yun, S. Lee, J. Lee, H. Cho. "Mechanical anisotropy of 3D-printed digital materials at large strains". *Annual Technical Meeting of the Society of Engineering Sciences, Atlanta, GA, 2025*.
- J. U. Lee, J. Lee, H. Cho. "Experiments and nonlocal continuum modeling of the size-dependent fracture in elastomers". *24th International Congress on Theoretical and Applied Mechanics, Daegu, 2024*.
- S. H. Lee, H. Cho. "Stiffness, strength and reusability in architected polycrystals". *19th European Mechanics of Materials Conference, Barcelona, 2024*.
- J. Lee, J. Moon, H. Cho, G. C. Rutledge, M. C. Boyce. "Micromechanics of thermoplastic elastomers with random microstructures". *March Meeting of the American Physical Society, Minneapolis, MN, 2024*.

## 수상

누리집 첫 화면 News and Highlights와 소식 모음 페이지(news arXiv)의 수상 글 8건(2023년 5월–2026년 2월)이다. 구성원의 학회 논문상·포스터상, 학위 논문상, KAIST 총장상이며, 날짜와 문장은 게시된 그대로다.[^home][^newsarc]

- Feb 2026 · Jehoon won the Outstanding Poster Award for "Mechanics of Heterogeneous Disordered Materials (JMPS 2025)" at KSCM 2026. Many congratulations!
- April 2025 · Jaehee won the Outstanding Ph.D. Thesis Award from the Korea Society of Mechanical Engineers. Many congratulations!
- Oct 2024 · Jaehee and Jehoon shared the KAIST Presidential Award (카이스트 총장상) for Outstanding Paper (citing JMPS 2024). Good for our two JHs!
- Oct 2024 · Seunghyeon won the KAIST Presidential Award (카이스트 총장상) for Outstanding Paper (citing IJP 2023). Congratulations!
- Nov 2023 · Gisoo won the Outstanding S.M. Thesis Award from the KAIST Aerospace Department. Many congratulations!
- May 2023 · Seunghyeon won the Outstanding Thesis Award from the Applied Mechanics Division of the Korea Society of Mechanical Engineers (KSME). Many congratulations!
- May 2023 · Jaehee won the Outstanding Paper Award for her work on "nonlocal fracture in elastomers" at the KSME Applied Mechanics Division Spring Meeting, 2023. Great news!
- May 2023 · Jehoon won the Outstanding Paper Award for his work on "isotropy and disorder" at the KSME Applied Mechanics Division Spring Meeting, 2023. Many congratulations!

## 소식

첫 화면 News and Highlights의 13건과 소식 모음 페이지의 46건, 모두 59건(2022년 10월–2026년 11월)이다. 두 페이지의 수상 글은 위 「수상」에 따로 실었다. 날짜와 문장은 게시된 그대로이고, 2026년 11월 항목은 앞으로 할 강의를 알린 글이다. 연구실은 2025년 3월 기계공학과로 옮겨 합류했으며, 그 전 소식에는 KAIST 항공우주공학과(Aerospace Department)의 석사 논문상과 AE Research Highlight 소개 글이 있다.[^home][^newsarc]

- Nov 2026 · Hansohl delivers a short course on continuum mechanics at the KSME Fall Meeting in Jeju.
- October 2026 · Hansohl has been invited to give a talk in the Mechanical Engineering Department Seminar at Columbia University in the City of New York.
- August 2026 · Our lab is featured in the August issue of the KAIST ME Newsletter.
- July 2026 · Seunghwan's work on mechanical anisotropy in 3D-printed materials has been featured as an Inside Cover in Soft Matter. Check out Soft Matt. 2026.
- July 2026 · Hansohl has been invited to give a seminar at Leibniz University Hannover (postponed).
- July 2026 · Hansohl has been invited to give a presentation at the 17th World Congress on Computational Mechanics (WCCM-ECCOMAS 2026) in Munich, Germany.
- June 2025 · Seunghee (with 정운) presented his work on viscoelasticity of liquid crystal elastomers at the 20th U.S. Nat. Cong. Theo. Appl. Mech. (USNCTAM 2026), Pasadena, CA.
- June 2026 · Hansohl co-organized a symposium (with Eric, Shawn) on coupled mechanics at USNCTAM 2026.
- June 2026 · Seunghyeon successfully defended his Ph.D. thesis. We've got another Ph.D. from the group. Many congratulations, Dr. Lee!
- April 2026 · Hansohl has been invited to deliver a presentation in the Materials and Solid Mechanics Seminar Series at Brown University.
- Jan 2026 · Hansohl has been invited to give a presentation at the coming Advances in Applied Mechanics Conference (AAM 2026), Gran Canaria, Spain (declined).
- Jan 2026 · Hansohl presented our work (with 승현) on uncertainty quantification for modeling of bcc materials at the Int. Conf. of Plasticity (ICPDF 2026), Geelong, Australia.
- Jan 2026 · Jaehee has recently joined the Silberstein and Roeder labs at Cornell University as a postdoctoral associate. Wishing her all the best!
- Oct 2025 · Seunghwan's work on two-phase architected polycrystals has been featured as a Cover in Proceedings of the Royal Society A. Check out Proc. R. Soc. A 2025.
- Oct 2025 · Gisoo, Seunghwan and Jaehee (invited; with 한솔, 정운) presented at the 2025 SES Annual Meeting hosted by Georgia Tech (SES 2025), Atlanta, GA.
- Sep 2025 · Seunghyeon presented his work on statistical inference for crystal plasticity at the 18th Int. Conf. on Computational Plasticity (COMPLAS 2025), Barcelona, Spain.
- August 2025 · Hansohl presented at the 2nd German-Korean Computational Mechanics Workshop hosted by Technische Universität Dresden (Prof. M. Kaliske), DE (with 제훈, 기수, 재희).
- July 2025 · Hansohl presented at the 11th KMSM (Korea Multiscale Mechanics Society) Symposium (with 제훈, 기수).
- July 2025 · Our lab and student office have relocated to Rm 3124 and 3125, N7. We do appreciate the help and support from the MechE staff and faculty.
- April 2025 · Jaehee has been selected as a Jang Young Sil Fellow (장영실 펠로우). Great news!
- March 2025 · Our group is moving to and joining the Mechanical Engineering Department, KAIST in March, 2025.
- March 2025 · Jeongun presented his recent work on modeling of viscoelastomers at the American Physical Society (APS) March Meeting, Annaheim, CA.
- Dec 2024 · Jaehee successfully defended her Ph.D. thesis. We've got our first Ph.D. from the group. Many congratulations, Dr. Lee!
- Nov 2024 · Our work on nonlocal modeling of elastomer fracture has been featured as an Editors' Suggestion in Phys. Rev. Mat. Check out PRM 2024.
- Oct 2024 · Hansohl co-chaired the 2024 Monie A. Ferst Award Symposium hosted by Georgia Tech. The Boyce Group alums got together to celebrate MCB's achievements as a mentor.
- Sep 2024 · Our work on (ugly yet elegant) bcc single- and polycrystals is featured as one of the most popular articles in IJP. Check out IJP 2023 and JMPS 2023.
- Aug 2024 · Jehoon presented his work on "disordered microstructures" at the 26th (100 years) International Congress of Theoretical and Applied Mechanics (ICTAM), Daegu.
- Aug 2024 · Jeongun presented his work on "size-dependent fracture in elastomers" at ICTAM, Daegu.
- Aug 2024 · Gisoo presented his work at the Society of Engineering Science (SES) Annual Technical Meeting, Hangzhou, China.
- Aug 2024 · Hansohl served as a member of local organizing committee for ICTAM, Daegu.
- June 2024 · Hansohl has been invited for a small talk at Conferences Internationales Materiaux et Technologies (CIMTEC) 2024 held in Montecatini Terme, Italy.
- June 2024 · Seunghyeon has been offered a summer opportunity again at the Los Alamos National Laboratory. He stays with the Theoretical Division. Good for him, again!
- May 2024 · Seunghwan presented his work on "mechanics of architected heterogeneous polycrystals" at the 19th European Mechanics of Materials Conference (EMMC19), Madrid, Spain.
- May 2024 · Our work on "mechanics of random microstructures in thermoplastic elastomers" is featured in KAIST Engineering News. Check out JMPS 2024.
- April 2024 · Hansohl presented at the Franklin Medal Laureate Symposium honoring MCB, hosted by the University of Pennsylvania and John Bassani. What a moment for MCB!
- March 2024 · Jaehee and Jehoon presented our recent work on "macro/micromechanics of two-phase elastomers" at American Physical Society (APS) March, Minneapolis, NM, US.
- Jan 2024 · Gisoo's work on "elasto-plastomeric crystals" is featured in AE Research Highlight. Check out Soft Matter 2023.
- Jan 2024 · Hansohl presented (invited; with 재희, 제훈, 기수) at the International Conference of Plasticity, Damage and Fracture (Plasticity 2024), Panama City.
- Dec 2023 · Hansohl delivered a seminar on "isotropy and engineered disorder" (with 제훈, 기수, 재희) at the Mechanical Engineering Department, Yonsei University.
- Nov 2023 · Hansohl presented at the KSME Fall Meeting (유망과학자세션 with 기수, 제훈).
- Oct 2023 · Hansohl presented at the 2023 SES Annual Technical Meeting (with 제훈, 기수), hosted by the University of Minnesota, Twin Cities; the city of Purple Rain.
- Aug 2023 · Jaehee's work on "a thermoplastic elastomer at extreme rates" in collaboration with Army Research Lab is featured in AE Research Highlight. Check out IJSS 2023.
- Aug 2023 · Hansohl presented at Apple Park, the corporate headquarters of Apple Inc on "modeling and simulations of extreme events in polymers" (with 재희, 기수).
- July 2023 · Hansohl visited the Theoretical Division (T) at Los Alamos National Laboratory (LANL) to deliver an invited seminar (with 재희, 승환, 승현; host: D. J. Luscher, T3).
- July 2023 · Hansohl presented (invited; with 재희, 정운, 제훈) at the 17th US National Congress on Computational Mechanics (USNCCM), Albuquerque, NM, US.
- July 2023 · Seunghyeon presented his research on "bcc sigle- and polycrystals in extremes" at the USNCCM, Albuquerque, NM, US.
- July 2023 · Hansohl has been invited for a small talk at the coming International Workshop on Multi-scale Science and Engineering held in Okinawa, Japan.
- June 2023 · Seunghyeon has been offered a summer internship at LANL. He is visiting T3 (Fluids/Solids) to collaborate on crystal mechanics for his thesis work. Good for him!
- May 2023 · Our work on bcc crystals is featured in KAIST News. Check out our recent papers on the extreme mechanics of bcc single- and polycrystals (IJP 2021, IJP 2023, JMPS 2023).
- April 2023 · Jehoon presented his research on "engineered disorder" (with 기수, 재희, 수연)" at Materials Research Society (MRS) Spring Meeting, San Francisco, CA, US.
- March 2023 · Jaehee presented her research on "nonlocal fracture in elastomers (with 정운)" at American Physical Society (APS) March Meeting, Las Vegas, NV, US.
- Jan 2023 · Hansohl has been invited for presentation at the International Conference of Plasticity, Damage and Fracture (Plasticity 2023).
- Dec 2022 · Hansohl has been invited as a keynote at the Korea Society of Computational Mechanics (KSCM) Winter Workshop, 2022.
- Dec 2022 · Hansohl delivered an invited talk on "extreme resilience and dissipation in soft materials (with 기수, 제훈, 승환)" at the Multiscale Mechanics Society Winter Meeting.
- Dec 2022 · Hansohl delivered an invited talk on "anomalous plasticity in bcc single- and polycrystals (with 승현)" at the Mechanical Engineering Department, Postech.
- Nov 2022 · Hansohl delivered an invited talk on "extreme resilience and dissipation in heterogeneous soft crystals (with 기수, 제훈)" at the ENGE 2022.
- Nov 2022 · Hansohl delivered an invited talk on "modeling extreme deformation and failure in elastomers (with 재희, 정운)" at the Rheological Society of Korea Fall Meeting.
- Oct 2022 · Hansohl delivered an invited talk on "nonlocal continuum modeling of elastomers (with 재희, 승현, 정운)" in the Mechanics Seminar Series at Seoul National University
- Oct 2022 · Jaehee, Gisoo and Seunghyeon presented their work at the 10th International Conference on Multiscale Materials Modeling (MMM10), Baltimore, MD, US.

## 연락과 위치

- 연구실: 기계동(N7) 3124호(실험실), 3125호(대학원생실), 전화 82-42-350-3070 / 5753[^team]
- 교수실과 전화: 기계동(N7) 7110호(서관), 042-350-3030[^meprof]
- 교수 이메일: hansohl@kaist.ac.kr[^meprof]
- 첫 화면은 2026/2027년부터 함께 연구할 박사·석사과정 학생과 개별연구 학부생을 모집한다고 안내한다.[^home]
[^p1]: J. Lee 외, H. Cho, Physical Review Materials 8, 115602 (온라인 2024-11-05). <https://doi.org/10.1103/physrevmaterials.8.115602> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J. Lee 외, H. Cho, International Journal of Solids and Structures 280, 112360 (2023). <https://doi.org/10.1016/j.ijsolstr.2023.112360> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: S. Lee 외, H. Cho, International Journal of Plasticity 201, 104678 (2026). <https://doi.org/10.1016/j.ijplas.2026.104678> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: S. Lee 외, J. R. Mayeur, International Journal of Plasticity 163, 103529 (2023). <https://doi.org/10.1016/j.ijplas.2023.103529> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: S. Lee, H. Cho, Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences 481, 20250268 (온라인 2025-10-22). <https://doi.org/10.1098/rspa.2025.0268> 초록 기준.
[^p6]: J. Moon, G. Lee, J. Lee, H. Cho, Journal of the Mechanics and Physics of Solids 204, 106246 (2025). <https://doi.org/10.1016/j.jmps.2025.106246> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: S. Lee 외, H. Cho, Soft Matter 22, 4722-4743 (2026). <https://doi.org/10.1039/d6sm00036c> 초록 기준.
[^p8]: H. Cho 외, M. C. Boyce, Journal of the Mechanics and Physics of Solids 187, 105615 (2024). <https://doi.org/10.1016/j.jmps.2024.105615> 초록 기준(Semantic Scholar 등록 초록).
[^home]: Solids Lab 누리집 첫 화면 <https://continuum.kaist.ac.kr/home> (연구실 소개, 연구 갈래, News and Highlights, 모집 안내, 2026-10-23 열람)
[^research]: Solids Lab 누리집 Research 페이지 <https://continuum.kaist.ac.kr/research> (연구 소개, Research themes, 2026-10-23 열람)
[^cont]: Solids Lab 누리집 Research 「Continuum mechanics」 페이지 <https://continuum.kaist.ac.kr/research/continuum-mechanics> (2026-10-23 열람)
[^extreme]: Solids Lab 누리집 Research 「Extreme and Rare Events」 페이지 <https://continuum.kaist.ac.kr/research/extreme-events> (손상·파괴·치유, 극한 소재의 통계적 추론, 2026-10-23 열람)
[^geometry]: Solids Lab 누리집 Research 「Mechanics and Geometry」 페이지 <https://continuum.kaist.ac.kr/research/geometry2> (The matter is the machine, 무질서 물질의 역학·기하·통계, 2026-10-23 열람)
[^micro]: Solids Lab 누리집 Research 「Heterogeneous Materials」 페이지 <https://continuum.kaist.ac.kr/research/micromechanics2> (3D/4D 프린팅의 역학, 상분리 고분자의 역학, 2026-10-23 열람)
[^team]: Solids Lab 누리집 Our Team 페이지 <https://continuum.kaist.ac.kr/our-team> (구성원, Alum & Thesis, Undergraduates, Friends & Visitors, 연락처, 2026-10-23 열람)
[^prof]: Solids Lab 누리집 교수 소개 페이지 <https://continuum.kaist.ac.kr/our-team/hansohl-cho> (학력, 경력, 2026-10-23 열람)
[^pubs]: Solids Lab 누리집 Publications 페이지 <https://continuum.kaist.ac.kr/publications> (papers + preprints, pre kaist, Recent Presentations, 2026-10-23 열람)
[^newsarc]: Solids Lab 누리집 소식 모음 페이지 <https://continuum.kaist.ac.kr/home/news-arxiv> (2022년 10월–2025년 10월 소식, 2026-10-23 열람)
[^meprof]: KAIST 기계공학과 교수 소개(조한솔) <https://me.kaist.ac.kr/pop/team.html?uid=138&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 이메일, 교수실, 전화, 2026-10-23 열람)
[^melist]: KAIST 기계공학과 교수진 목록 2쪽 <https://me.kaist.ac.kr/team/team_010100.html?page=2&plist=&find_field=&find_word=&find_state=&find_ordby=&conf=&mode=1> (조한솔 교수 항목의 연구분야, 연구실, 최종학위, 2026-10-23 열람)

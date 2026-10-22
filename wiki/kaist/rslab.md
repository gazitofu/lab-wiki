# 로봇 및 시뮬레이션 연구실 (RS Lab)

**KAIST 기계공학과 · 이두용 교수**

- 분야: 혈관 시술용 능동 조향 가이드와이어·카테터 구동기, 햅틱 제어와 원격 조작, 의료 시술 시뮬레이션(연조직 변형·절단, 혈관 조영 영상 렌더링, 햅틱 인터페이스)
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 수술·의료 로봇[^robotics][^mefield], 햅틱[^robotics][^sim][^p2], 제어 이론·제어 공학[^robotics][^p2], 소프트 로보틱스[^p4][^p5], 컴퓨터 그래픽스·기하 처리[^sim][^p7], 과학·공학 AI[^p8]
- 홈페이지: <https://sites.google.com/view/rslab-kaist/>
- 근거와 출처: [로봇 및 시뮬레이션 연구실 근거 페이지](rslab-sources.md)

> 혈관 시술에 쓰는 가이드와이어의 끝을 스스로 휘게 하는 의료 기구, 조작자의 손에 힘을 전하는 햅틱 장치와 그 제어, 수술과 의료 시술을 컴퓨터로 재현하는 의료 시뮬레이션을 연구하는 기계공학과 연구실이다.[^robotics][^sim] 기계공학과 연구분야 안내는 이 연구실의 연구주제를 Medical Robotics & Haptics와 Medical Simulation으로, 주요 응용 산업을 의료기기로 적는다.[^mefield]

## 무엇을 연구하나

연구실은 KAIST 기계공학과 이두용 교수의 연구실이다. 기계공학과 교수 소개는 연구실 이름을 「로봇 및 시뮬레이션 연구실」로, 교수의 연구분야를 Medical Robotics, Medical Simulation으로 적는다.[^me] 누리집 Researches 메뉴는 연구를 의료 로봇(Medical Robotics)과 의료 시뮬레이션(Medical Simulation) 두 갈래로 나눈다.[^robotics][^sim] 교수 페이지는 교수의 연구 관심을 의료 응용을 위한 로봇과 시뮬레이션으로 적고, 특히 로봇 의료기기와, 훈련과 계획을 위해 햅틱 인터페이스를 갖춘 고충실도 상호작용 의료 시뮬레이션을 든다.[^prof]

의료 로봇 갈래의 첫 주제는 햅틱 렌더링(haptic rendering, 물체와 닿을 때 생기는 힘을 계산해 사용자의 손에 전하는 일)을 위한 제어 방법이다. 연구 페이지에 따르면 주종 제어 시스템(master-slave control system)에서는 조작자가 멀리 떨어진 곳의 슬레이브 로봇을 다루고, 슬레이브 로봇이 주변 환경과 주고받는 힘과 토크를 조작자의 손에 전해 느끼게 할 수 있다. 연구실은 여러 의료 로봇과 기기에 쓰는 햅틱 마스터(조작자가 손으로 잡고 움직이는 장치)와 그 제어 방법을 개발해 왔고, 이 제어 방법은 실제 환경을 가상 환경으로 바꾸면 햅틱 시뮬레이션에도 쓸 수 있다고 연구 페이지는 적는다. 연구 페이지의 그림은 시간 지연이 있는 상황의 모델 매개 원격 조작, 햅틱 시뮬레이션의 안정화, 능동 조향 카테터 로봇용 햅틱 마스터(2017년부터, Ministry of Trade, Industry & Energy)를 보여 준다.[^robotics]

둘째 주제는 능동 조향 가이드와이어(active-steering guidewire)다. 가이드와이어는 카테터(혈관 등에 넣는 가는 관)를 혈관을 따라 목표 병변까지 이끄는 의료 기구다. 연구 페이지에 따르면 시술 중에는 가이드와이어가 목표 병변에 닿기까지 혈관의 여러 갈래에서 끝을 손으로 구부려 모양을 잡아야 해서, 가이드와이어를 환자의 혈관에 여러 번 넣었다 빼게 된다. 연구실은 끝부분을 스스로 휘게 할 수 있는 가이드와이어를 개발해 왔고, 연구 페이지는 이 가이드와이어가 지름이 작은 혈관에도 안전하게 들어갈 수 있다고 적는다. 가이드와이어는 사람의 혈압과 혈류 속도를 비슷한 혈관 모양에서 재현하는 혈액 순환 장치에서 시험하고, 가이드와이어 몸체를 만드는 압출 공정(재료를 틀 구멍으로 밀어내 긴 모양으로 뽑는 공정) 장치도 개발해 왔다.[^robotics]

의료 시뮬레이션 갈래는 세 주제다. 시뮬레이션 모델링은 수술과 의료 시술의 시뮬레이션에 필요한 사람의 장기·조직, 의료 기기, 그 사이 상호작용의 모델을 만드는 일로, 실제 물체의 기하학적·물리적 특성을 가상 모델에 담아 정확하고 빠른 실시간 상호작용 시뮬레이션의 바탕으로 삼는다. 시각 렌더링(visual rendering, 시뮬레이션 장면을 화면에 그려 내는 일)은 계산 부담이 큰 고충실도 상호작용 의료 시뮬레이션의 실시간 화면을 위해 빠르고 정확한 계산 방법을 다룬다. 의료 시뮬레이션용 햅틱 인터페이스는 실시간 상호작용의 촉감을 사용자의 손에 전하는 햅틱 장치와 그 제어 방법이다.[^sim] 연구 페이지의 그림은 영률이 다른 물체 모델, 에너지 보존 적분법을 쓴 카테터 모델, 연조직 절단 시뮬레이션, 혈관 조영 시뮬레이션용 투시 영상 렌더링, 입자 기반 혈류 모델, 기계 학습 기반 내시경 영상 렌더링(2019년부터, National Research Foundation of Korea), 바늘 시술과 관상동맥 시술의 시뮬레이션과 햅틱 인터페이스, 햅틱 렌더링의 실시간 계산 방법을 보여 준다.[^sim]

기계공학과 연구분야 안내는 이 연구실을 로보틱스/제어/모빌리티 분야에 연구주제 Medical Robotics & Haptics, Medical Simulation으로, 헬스케어/나노/광학 분야에 연구주제 Medical Robotics, Medical Simulation으로 함께 싣고, 두 곳 모두 주요 응용 산업을 의료기기로 적는다.[^mefield][^mefield4] 누리집 첫 화면은 2024년 Springer에서 나온 책 Control Design for Haptic Systems를 소개한다.[^home] 2021–2026년 논문 목록에는 햅틱 시스템 제어, 수압으로 휘는 미세 가이드와이어와 그 제작 공정, 연조직 절단·변형 시뮬레이션, 혈관 조영 X선 영상 렌더링, 혈관 주사 증강현실 시뮬레이션 논문이 이어진다.[^cr]

## 주요 연구 주제

### 1. 햅틱 제어와 원격 조작

햅틱 시스템은 사용자가 손으로 잡은 장치를 통해 멀리 있는 로봇이나 가상 환경이 물체와 닿을 때의 힘을 느끼게 한다. 연구 페이지는 연구실이 여러 의료 로봇과 기기의 햅틱 마스터와 그 제어 방법을 개발해 왔다고 적고, 그림으로 시간 지연이 있는 원격 조작과 햅틱 시뮬레이션의 안정화를 든다.[^robotics]

대표 논문 1은 모델 매개 원격 조작(MMT)을 다룬다. MMT는 조작자 쪽 장치(마스터)에 원격 환경의 모델을 두고 조작자에게 돌려줄 힘을 빠른 주기로 계산해, 시간 지연이 있어도 안정성을 높이는 방식이다. 이 논문은 모델이 실제 환경과 어긋날 때를 대비해 모델의 기준점을 적응적으로 옮기는 방법을 내놓았다.[^p1] 대표 논문 2는 신호를 일정 간격의 값으로 바꾸는 과정에서 햅틱 시스템에 에너지가 더해져 불안정해지는 문제를 다루고, 가상 환경의 강성(단단한 정도)이 바뀌는 빠르기를 조절해 입력-상태 안정성(ISS, 입력이 유한하면 시스템의 상태도 유한하게 머무는 성질) 조건을 만족시키는 제어 방법을 내놓았다.[^p2] 누리집 소식 글에 따르면 이 갈래의 연구를 담은 책 Control Design for Haptic Systems(부제 Enhancing the Stability and Rendering Performance)를 김수용 박사(2022년 KAIST 기계공학과 박사, 한국전자통신연구원)와 교수가 함께 써서 2024년 Springer에서 냈다. 소식 글은 이 책이 햅틱 시스템의 구성, 주요 제어 기술, 안정성과 성능을 높이는 새 방법을 실험 사례와 함께 소개하는, 학사과정 3–4학년과 대학원생, 현업 엔지니어를 위한 교재라고 적는다.[^book] 대표 논문 1, 2.[^p1][^p2]

### 2. 능동 조향 가이드와이어와 미세 구동기

연구실은 혈관 속에서 끝을 휘게 할 수 있는 가는 가이드와이어를, 압력을 넣으면 휘는 유연한 관으로 만든다. 대표 논문 4는 지름 400 μm의 수압 조향 가이드와이어로, 안쪽에 미세 무늬가 있는 유연한 편심 관(구멍이 한쪽으로 치우친 관)이 압력을 받으면 두 가지 곡률로 휜다. 3D 프린팅한 원통 틀에 무늬를 찍고 실리콘을 입힌 뒤 틀을 화학적으로 녹여 없애는 방식으로 만들었다.[^p4] 대표 논문 5는 자기유변 탄성체(magnetorheological elastomer, 자기장에 반응하는 입자를 섞은 탄성 고분자)와 자기장으로 1 mm 미만 크기 압력 구동기의 치수를 마이크로미터 단위 정밀도로 정하는 제작 방법을 내놓았다.[^p5] 대표 논문 6은 닫힌 성형과 펨토초 레이저로 무늬를 새긴 스테인리스강 심(core) 틀로, 안쪽 면에 무늬가 있는 편심 관 모양 구동기를 접착 없이 만드는 방법을 내놓았다.[^p6]

최근 논문 목록에는 압력 구동 미세 가이드와이어에서 X선 투시 조영제가 X선에 보이는 정도와 조향 성능에 주는 영향을 다룬 학회 논문(2022, EMBC)과, 자기유변 탄성체로 만든 소프트 구동기의 제작 공정 제어를 다룬 Journal of Institute of Control, Robotics and Systems 논문(2024)도 있다.[^cr] 대표 논문 4, 5, 6.[^p4][^p5][^p6]

### 3. 의료 시뮬레이션: 변형·절단, 영상 렌더링, 햅틱 인터페이스

대표 논문 7은 수술 시뮬레이션에서 연조직을 자르는 장면을 실시간으로 계산하는 방법을 다룬다. 변형은 규칙적인 육면체 요소만으로 계산하고, 화면 표시와 충돌 감지에 쓰는 표면 구조는 육면체 안에 심은 뒤 절단은 둘을 따로 처리해 계산 부담을 줄였다.[^p7] 대표 논문 8은 저해상도로 계산한 변형 시뮬레이션 결과에서 고해상도 결과를 추정하는 신경망 학습 방법으로, 변형 에너지(물체가 변형되며 안에 쌓이는 에너지)가 비슷한 장면끼리 학습 자료를 짝짓는다.[^p8] 대표 논문 3은 심장 카테터 시술 시뮬레이션에 쓰는 실리콘 고무 햅틱 구동기로, 수압으로 안쪽 방을 부풀려 지나가는 카테터에 저항을 주거나 카테터를 밀어 되돌리고, 음의 압력으로 통로를 넓혀 여러 지름의 카테터를 쓸 수 있게 한다.[^p3]

최근 논문 목록에는 혈관 모델의 중심선과 원뿔대를 써서 혈관 조영 시뮬레이션의 X선 영상을 실시간으로 그리는 Transactions of the Korean Society of Mechanical Engineers - B 논문(2022)과, 혈관 주사 증강현실 시뮬레이션에서 바늘 손잡이의 움직임을 추적하는 학회 논문(2023, ICCAS)도 있다.[^cr] 대표 논문 3, 7, 8.[^p3][^p7][^p8]

## 대표 논문

이두용 교수가 저자인 2021–2026년 논문 가운데 초록을 확인할 수 있는 여덟 편을 세 연구 갈래(햅틱 제어와 원격 조작, 능동 조향 가이드와이어와 미세 구동기, 의료 시뮬레이션)에 고르게 담도록 골랐다. 여덟 편 모두 교수가 마지막 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^cr] |
|---|---|---|---|---|
| 1 | 2021 | [Adaptive Model-Mediated Teleoperation for Tasks Interacting With Uncertain Environment](https://doi.org/10.1109/access.2021.3112207) · IEEE Access | 모델 매개 원격 조작(MMT)은 조작자 쪽(마스터)에 환경 모델을 두고 조작자에게 돌려줄 힘을 빠른 주기로 계산해, 시간 지연이 있을 때 시스템 안정성을 높이는 방식이다. 그러나 환경을 미리 알 수 없거나 환경이 바뀌면 모델이 실제와 어긋나 대개 성능이 좋지 않다. 이 논문은 기존 MMT가 환경 속 물체 표면에 고정하던 모델의 기준점을 적응적으로 옮기는 MMT를 제안했고, 이렇게 하면 시스템 안정성이 시간 지연과 무관해질 수 있다고 적는다. 실험에서 모델이 어긋날 때 기존 MMT에 비해 안정성이 나아졌다. 환경 속 물체에 가하는 힘 조절과 물체 강성(단단한 정도) 구별의 두 과제로 사용자 실험을 한 결과, 물체에 가한 힘의 오차가 크게 줄었고 마스터에 전해지는 힘의 오차도 최소 20.2% 개선됐다. 같은 시간 지연에서 참가자들은 기존 MMT에 비해 최대 40.9% 작은 강성 차이까지 구별했다.[^p1] | 1저자 C. Kim, 마지막 저자 이두용 (2명) |
| 2 | 2022 | [Control of Haptic Systems Based on Input-to-State Stability](https://doi.org/10.1109/access.2022.3157610) · IEEE Access | 신호를 일정 간격의 값으로 바꾸는 이산화는 햅틱 시스템에 에너지를 더해 시스템을 불안정하게 만들기 쉽다. 널리 쓰이는 수동성(passivity) 기반 제어는 시스템이 만들어 내는 에너지가 0 아래에 머물도록 전하는 힘을 제한해 안정시키지만, 보수적이어서 햅틱 렌더링 성능을 희생하는 경우가 많다. 이 논문은 햅틱 시스템에 연결된 가상 환경의 강성이 바뀌는 빠르기를 조절해 입력-상태 안정성(ISS) 조건을 만족시키는 제어 방법을 제안했다. 시스템을 선형 시변 시스템(시간에 따라 계수가 바뀌는 선형 모형)으로 모형화해 ISS 조건을 이끌어 냈고, 이 조건을 만족하면 시스템이 만들어 내는 잉여 에너지는 안정성을 유지하면서 양의 유한한 값 아래에 머문다. 널리 쓰이는 수동성 기반 방법인 가상 커플링, 힘 제한 방법과 실험으로 견주었더니 조작자에게 더 많은 에너지가 전해져 그만큼 큰 강성을 표현할 수 있었고, 전달한 힘의 제곱평균제곱근 오차(오차를 제곱해 평균한 뒤 제곱근을 취한 값)와 최대 오차가 각각 최소 86%, 50% 줄었다.[^p2] | 1저자 S. Kim, 마지막 저자 이두용 (2명) |
| 3 | 2024 | [A Hydraulic Haptic Actuator for Simulation of Cardiac Catheters](https://doi.org/10.1109/toh.2024.3364689) · IEEE Transactions on Haptics | 심장 카테터 시뮬레이션에서 수동·능동 햅틱 힘을 함께 주는, 실리콘 고무로 만든 햅틱 구동기를 내놓았다. 구동기는 바깥 모양이 토러스(가운데가 뚫린 고리 모양)이고 안에 타원 모양 방이 있으며 수압으로 움직인다. 방에 양의 압력을 넣어 부풀리면 가운데 통로를 조여 지나가는 카테터에 저항을 주고, 더 부풀리면 카테터를 붙잡아 축 방향으로 밀어 되돌리는 능동 힘을 낸다. 방에 음의 압력을 넣으면 통로가 넓어져, 실제 의료용 카테터의 여러 지름을 시뮬레이션 중에 쓰고 바꿔 끼울 수 있다. 통로 지름은 최대 1.6배까지 넓어져 5–7 Fr(1 Fr = 1/3 mm) 카테터가 지나간다. 실험에서 0–2.0 N의 수동 힘과 최대 2.0 N의 능동 힘을 냈고, 저자들은 이 힘이 심장 카테터 시뮬레이션에 충분하다고 적는다. 명령한 힘 곡선과 실제로 낸 힘의 차이는 제곱평균제곱근 오차 0.10 N, L2 노름 상대 오차(곡선 전체에 걸친 오차의 크기를 명령한 힘 곡선 전체의 크기로 나눈 값) 10.51%였다.[^p3] | 1저자 C. Li, 마지막 저자 이두용 (2명) |
| 4 | 2021 | [Hydraulically Steerable Micro Guidewire Capable of Distal Sharp Steering](https://doi.org/10.1109/tbme.2020.3013267) · IEEE Transactions on Biomedical Engineering | 지금의 조향 카테터와 가이드와이어는 지름이 크거나 끝을 급하게 꺾지 못해 지름이 작은 혈관으로 들어가지 못하는 경우가 많다. 이 논문은 지름 400 μm의 수압 조향 가이드와이어를 제안해, 갈라지는 각도가 90도보다 큰 지름 1 mm 혈관에 들어갈 수 있게 했다. 조향 기구는 안쪽에 미세 무늬가 있는 유연한 편심 관으로, 압력을 받으면 두 가지 곡률로 휜다. 끝쪽 2 mm 구간의 급한 곡선은 좁은 혈관 안에서도 꺾는 각도를 크게 해 지름이 작은 혈관으로 들어가게 하고, 그 뒤 9 mm 구간의 완만한 곡선은 조향 거리를 길게 해 비교적 지름이 큰 혈관으로 들어가게 한다. 조향 기구는 접착이나 분할 없이 틀로 만든다. 3D 프린팅한 원통 틀에 도장으로 무늬를 찍고 실리콘을 입힌 뒤 틀을 화학적으로 없앤다. 사람 동맥의 점도·압력·유속과 혈관 갈림 모양을 재현하도록 만든 혈액 순환 장치에서 원하는 갈래로 넣는 성능을 시험해, 갈림 각도 128도의 지름 1 mm 혈관에 들어갔다. 구동 유체를 포함해 생체 적합 재료만 쓴다.[^p4] | 1저자 S. Kang, 마지막 저자 이두용 (2명) |
| 5 | 2025 | [Magnetorheological-Elastomer-Based and Hydraulically Steerable Actuator for Micro Guidewire and Catheter](https://doi.org/10.1109/tmrb.2025.3527718) · IEEE Transactions on Medical Robotics and Bionics | 조향 가이드와이어와 카테터의 압력 구동 기구는 1 mm 미만 크기로 줄이면 만들기 어렵다. 압력 구동기의 바깥지름이 1 mm 미만으로 작아지면 성형에서 생기는 미세 기포나 표면장력 때문에 생기는 표면 요철이 구동 성능에 영향을 줄 수 있다. 이 논문은 1 mm 미만 크기의 압력 구동기를 만드는 새 제작 방법을 내놓았다. 자기유변(MR) 탄성체와 자기장으로 구동기의 치수를 마이크로미터 단위 정밀도로 정한다. 지름 0.7 mm, 편심 80 μm로 설계한 구동기를 각각 절대 오차 12 μm, 3 μm로 만들었다. 만든 미세 구동기의 조향 성능을 실험으로 시험했고, 유한요소 해석으로 편심을 최적화해 길이 5.41 mm에서 124도의 급한 굽힘 각도를 냈다.[^p5] | 1저자 M. S. Kim, 마지막 저자 이두용 (3명) |
| 6 | 2025 | [Manufacturing of hydraulically steerable actuator using closed molding and core template for vascular intervention guidewires](https://doi.org/10.1088/1361-6439/adaf2f) · Journal of Micromechanics and Microengineering | 압력 구동 방식을 쓰는 혈관 시술용 능동 조향 카테터와 가이드와이어는 안전하고 작게 만들 수 있으며 다루기 쉬울 것으로 기대되어 연구되어 왔다. 그러나 마이크로 크기로 만드는 방법은 내구성이 낮고, 조향 모양이 제한되며, 세포 독성과 적용 범위의 한계가 있다. 이 논문은 닫힌 성형과 레이저로 무늬를 새긴 심(core) 틀로 미세 가이드와이어용 수압 조향 구동기를 만드는 방법을 제안했다. 원통형 심 틀은 생체 적합성을 위해 스테인리스강으로 만들고 펨토초 레이저 가공으로 무늬를 새겼으며, 무늬의 상대 오차는 최대 15.04%였다. 이 방법은 안쪽 면에 무늬가 있는 편심 관인 미세 구동기를 접착 없이 만든다. 심 틀에 새기는 무늬의 모양으로 조향 모양을 설계해, 두 곡률로 휘는 지름 600 μm 구동기를 만들었고 최대 굽힘 각도 132.93도, 조향 거리 9.20 mm를 얻었다. 사람의 혈류를 닮게 만든 뇌혈관 갈림 모형에서 원하는 갈래로 넣는 실험을 해, 지름 4.2 mm와 1.5 mm, 갈림 각도 112도의 혈관 갈림을 지나갔다.[^p6] | 1저자 C. Y. Park, 마지막 저자 이두용 (2명) |
| 7 | 2021 | [Adaptive surface representation based on homogeneous hexahedrons for interactive simulation of soft tissue cutting](https://doi.org/10.1016/j.cmpb.2020.105873) · Computer Methods and Programs in Biomedicine | 연조직을 자르는 상호작용 시뮬레이션은 수술과 의료 시술 시뮬레이션에 꼭 필요하지만, 절단은 유한 요소의 연결 구조와 모양을 바꾸어 계산 부담을 크게 늘린다. 이 논문은 모델 경계와 부피 유한 요소 사이의 작은 틈을 근사해 이 문제를 다룬다. 변형은 규칙적인 육면체 요소만으로 계산하고, 물체를 화면에 보이고 충돌을 감지하는 데 쓰는 표면 구조는 육면체 안에 심는다. 절단은 육면체와 표면 구조에서 따로 처리한다. 잘린 육면체는 모양을 바꾸지 않고 복제하고, 표면 구조는 절단 경로에 맞춰 잘린 면을 나타낸다. 잘린 면과 육면체 사이 틈 때문에 생기는 부정확함은 부분 요소를 쓰는 방법으로 보완한다. 시뮬레이션 결과 추가 계산 부담이 문헌의 기존 방법의 34%와 37.12%로 줄었다. 저자들은 이 방법이 잘린 면을 적응적으로 근사해 시뮬레이션의 실시간 성능을 높인다고 적는다.[^p7] | 1저자 S. P. Byeon, 마지막 저자 이두용 (2명) |
| 8 | 2026 | [Strain-energy-based training of super-resolution for deformation simulation](https://doi.org/10.1093/jcde/qwag015) · Journal of Computational Design and Engineering | 지도 학습 초해상도 방법은 저해상도 시뮬레이션 결과에서 고해상도 결과를 추정한다. 보통 고해상도 자료와 그것을 낮춘 저해상도 자료를 짝지어 신경망을 학습시키는데, 이는 저해상도 모델과 고해상도 모델이 전체적으로 비슷하게 움직인다고 가정한다. 그러나 수치적 경직화(numerical stiffening) 때문에 저해상도 모델은 대개 고해상도 모델보다 단단하게 움직여 이 가정이 자주 맞지 않는다. 이 논문은 선형 변형체 시뮬레이션에서 이 문제를 줄이는 지도 학습 초해상도 방법을 제안했다. 정규화한 변형 에너지, 변형 에너지의 정규화한 시간 변화율, 전체 변형 에너지에 대한 각 모드(물체가 변형하는 기본 모양)의 기여가 비슷한 저해상도·고해상도 시뮬레이션 장면을 짝지어 학습 자료를 만든다. 학습에서 줄여 나가는 오차 값인 손실 함수에는, 신경망의 결과가 유한요소법의 방정식을 맞추지 못하는 정도를 나타내는 방정식 잔차도 넣었다. 시간에 따른 변형을 단계별로 계산하는 시간 적분 방식은, 유한요소 잔차와 관련된 신경 탄젠트 커널(학습 중 신경망의 출력이 바뀌는 방식을 나타내는 행렬)의 고윳값 분포를 살펴 골랐다. 기존 다운샘플링 방법에 비해 보, 코끼리, 아르마딜로 모델에서 최대 상대 변위 오차를 각각 25%, 54%, 38% 줄였다.[^p8] | 1저자 Q. Yuan, 마지막 저자 이두용 (2명) |

## 교수와 전문 분야

이두용 교수(Doo Yong Lee)는 KAIST 기계공학과 교수다. 기계공학과 교수 소개는 최종학위를 Ph.D., Rensselaer Polytechnic Institute (1993)로, 연구분야를 Medical Robotics, Medical Simulation으로 적는다.[^me] 누리집 교수 페이지에 따르면 Seoul National University의 Department of Control and Instrumentation Engineering에서 학사(1985)를, 미국 Rensselaer Polytechnic Institute의 Department of Electrical, Computer, and Systems Engineering에서 석사(1987)와 박사(1993)를 받았고, 1993–1994년 Rensselaer Polytechnic Institute의 Information Technology Services에서 postdoctoral Research Associate로 있었다. 1994년 KAIST 기계공학과에 부임했고 KAIST의 POSCO Endowed Chair Professor다. 2010–2012년 Korea Health Industry Development Institute의 Director of Health Technology Infrastructure, 2017–2021년 KAIST 기계공학과 Head of Department, 2021년 Institute of Control, Robotics, and Systems(ICROS) President를 지냈다. 1997년 Osaka University, 2003년 Saga University, 2004–2005년 University of California, Irvine의 visiting scholar였다.[^prof]

교수 페이지가 적는 수상은 Rensselaer Polytechnic Institute의 Charles M. Close Doctoral Prize(1993), Korean Society of Mechanical Engineers(KSME)의 Baekahm Paper Award(1999), ICROS의 Young Researcher Paper Award(2002), IEEE Systems, Man, and Cybernetics Society의 Franklin V. Taylor Memorial Award(2004), 2007 International Conference on Control, Automation, and Systems(ICCAS)의 Outstanding Paper Award, KSME Outstanding Service Award(2012), ICROS의 Fumio Harashima Mechatronics Award(2015), KSME Distinguished Leadership Award in Bioengineering(2018), 이 분야 기술 기여에 대한 Korea Prime Minister's Commendation(2018)이다. National Academy of Engineering of Korea 회원, ICROS Fellow, IEEE Senior Member이고 Society of Manufacturing Engineers(SME), KSME, Korean Society of Medical and Biological Engineering(KOSOMBE) 회원이며, 2017년 KSME Vice President를 지냈다.[^prof]

학술 활동으로는 International Journal of Control, Automation, and Systems의 Editor(2018–2020), IEEE Transactions on Systems, Man, and Cybernetics, Part B의 Associate Editor(2001–2012), Journal of Mechanical Science and Technology의 Associate Editor(2000–2012)를 지냈고, ICCAS 2014의 Organizing Chair와 ICCAS 2008의 Program Chair를 맡았다. IEEE와 IFAC(International Federation of Automatic Control)의 기술·프로그램 위원회에서 활동한다고 교수 페이지는 적는다.[^prof]

2021–2026년 논문으로 보면 전문 분야는 햅틱 시스템의 제어와 원격 조작, 수압으로 휘는 미세 가이드와이어·카테터 구동기의 설계와 제작, 연조직 변형·절단과 혈관 시술의 실시간 의료 시뮬레이션이다.[^cr]

## 응용 분야

기계공학과 연구분야 안내는 이 연구실의 주요 응용 산업을 의료기기로 적는다.[^mefield][^mefield4] 연구 페이지가 드는 응용은 여러 의료 로봇과 기기의 햅틱 마스터, 능동 조향 카테터 로봇, 혈관 시술용 가이드와이어, 수술과 의료 시술의 시뮬레이션(바늘 시술, 관상동맥 시술, 혈관 조영, 내시경)이다.[^robotics][^sim] 교수 페이지는 상호작용 의료 시뮬레이션의 쓰임을 훈련과 계획으로 적는다.[^prof] 책 소개 소식 글은 햅틱 시스템이 쓰이는 분야로 가상현실 시뮬레이션, 메타버스 응용, 원격 조작 로봇 시스템을 든다.[^book]

## 구성원

누리집 Members 페이지의 박사후 연구원(Post-Doc.) 1명, 박사과정(Ph.D. Students) 2명, 석사과정(M.S. Students) 1명, Research Assistant 1명, 모두 5명이다. 이름은 페이지 표기 그대로이고, 이메일은 페이지가 적은 KAIST 주소다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Han, Hyung Taeg | 박사후연구원 | hyungtaeghan@kaist.ac.kr |  |
| Kim, Gyeong Hyun | 박사과정 | rmggjb@kaist.ac.kr |  |
| Kim, Min Sung | 박사과정 | mskim201@kaist.ac.kr | 5 |
| Shijun Piao | 석사과정 | sj_park@kaist.ac.kr |  |
| Bae, Miae | Research Assistant |  |  |

## 졸업생과 이전 구성원

누리집 Alumni 페이지는 1–68번 68명의 이름과 진로를 번호가 큰 쪽부터 적는다. 학위와 졸업 연도는 적혀 있지 않다. 진로는 페이지 표기 그대로이고, 다섯 명은 진로 줄이 없다. 39번 Yves Riffard의 줄은 교환학생 기간(Exchange student, Feb. 2000 ~ July 2000)이다.[^alumni] 소식 글은 이 가운데 김수용(Suyong Kim)을 2022년 KAIST 기계공학과 박사, 한국전자통신연구원(Electronics and Telecommunications Research Institute) 연구원으로 적는다.[^book]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Qiaodi Yuan |  |  |
| Hyeok Namgung |  | LG Electronics |
| Eunha Sim |  | RIST |
| Chanyoung Park |  | Samsung Electro-Mechanics |
| Minju Kim |  | Hanwha Aerospace |
| Seungik Lee |  | Samsung Electronics |
| Chengjie Li |  | Jiangsu Ocean Univ |
| Suyong Kim |  | ETRI |
| Cheongjun Kim |  | Korea Automotive Technology Institute |
| Seunggyu Kang |  | Samsung Electronics |
| Hyehyun Han |  | Korea Institute of Science and Technology |
| Seong Pil Byeon |  | Agency for Defense Development |
| Taewook Huh |  | Krafton Inc. |
| Myeongjin Kim |  | Chonnam National University |
| Seokwon Jeon |  | Hyundai Motor |
| Hyeongju Han |  |  |
| Heejae Goh |  | GalionTech |
| Jongbeam Lee |  | TmaxSoft |
| Heewon Min |  | Samsung Electronics |
| Suhwan Park |  | Samsung Electronics |
| Jihye Hwang |  | Samsung Electronics |
| Hyunseok Lee |  | LG Electronics |
| Dongjun Lee |  | Kakao |
| Dongmouyng Lee |  | Samsung Electronics |
| Yunjin Gu |  | KTH Royal Institute of Technology (Sweden) |
| Yeonggi Jung |  | Katech |
| Su Bon Kim |  |  |
| Hyuk Wang |  | Hyundai Autron |
| Nguyen Trung Tuan |  | Denmark Technical University (DTU) |
| Yves Riffard (France) | Exchange student (Feb. 2000 ~ July 2000) |  |
| Md.Helal-An-Nahiyan |  |  |
| Nguyen Tien Thinh |  | Viettel Research and Development Institute |
| Buwon Kang |  | Samsung Heavy Industries |
| Ayoung Hong |  | Chonnam National University |
| Hashim Iqbal |  | UET Lahore(Faisalabad Campus), Pakistan |
| Dong Gun Lee |  | Samsung Heavy Industries |
| Muhammad Awais Hafeez |  |  |
| Hyun Young Choi |  | Samsung Display |
| Tapomayukh Bhattacharjee |  | Georgia Institute of Technology |
| Jae Hyeoung Jang |  | Daewoo Shipbuilding & Marine Engineering |
| Hyojun Woo |  | Daewoo Shipbuilding & Marine Engineering |
| In Sik Yu |  | LG Electronics |
| Yong Shin Lee |  | Agency for Defense Development |
| Woo Seok Kim |  | Kim & Chang law firm |
| Jae Kyoung Joo |  | Small and medium Business Corporation |
| Young Ha Jeon |  | Halla Climate Control Corporation |
| Jun Yong Kwon |  | Agency for Defense Development |
| Woo Suk Kim |  | Samsung Electronics |
| Moon Hwan Lee |  | Hyundai Motor Company |
| Gunhee Kim |  | Seoul National University |
| Dong Jun Chung |  | MSIP |
| Kyung Dae Kang |  | Samsung Techwin |
| Hae Seop Jang |  | Mecasys |
| Myung Hwan Oh |  | Samsung Corning Precision Glass |
| Seong Jin Yim |  | Seoul National Univ. of Science and Technology |
| Hoe Ryong Jung |  | Samsung Heavy Industries |
| Jang Ho Cho |  | KIMM |
| Woojin Ahn |  | Rensselaer Polytechnic Institute |
| Hyoung Il Son |  | Chonnam National University |
| Nam Soo Park |  | Agency for Defense Development |
| Sung Jo Kwak |  | Halla Climate Control Corporation |
| Min Seog Choi |  | Samsung Electronics |
| Hyun Soo Woo |  | KIMM |
| Seung Pil Yoo |  | LG Innotek |
| Kyungno Lee |  | Korea National University of Transportation |
| Seong Youb Chung |  | Korea National University of Transportation |
| Hyun Joong Yoon |  | Catholic University Of DaeGu |
| Myun Joong Hwang |  | University of Seoul |

## 최근 논문 목록 (2021–2026)

누리집에는 논문 목록 메뉴가 없다. 아래는 출판사 등록 서지(Crossref)에 이두용 교수가 저자로 오른 2021–2026년 논문과 책 13건이다(학술지 논문 10편, 학회 논문집 논문 2편, 책 1권). 저자·제목·학술지·학회 표기는 출판사 등록 서지의 표기이고, 연도는 출판사 서지의 발행 연도다.[^cr]

**2026**

- Qiaodi Yuan and Doo Yong Lee. "Strain-energy-based training of super-resolution for deformation simulation". *Journal of Computational Design and Engineering (doi:10.1093/jcde/qwag015)*.

**2025**

- Min Sung Kim, Chan Young Park, and Doo Yong Lee. "Magnetorheological-Elastomer-Based and Hydraulically Steerable Actuator for Micro Guidewire and Catheter". *IEEE Transactions on Medical Robotics and Bionics (doi:10.1109/tmrb.2025.3527718)*.
- Chan Young Park and Doo Yong Lee. "Manufacturing of hydraulically steerable actuator using closed molding and core template for vascular intervention guidewires". *Journal of Micromechanics and Microengineering (doi:10.1088/1361-6439/adaf2f)*.

**2024**

- Chengjie Li and Doo Yong Lee. "A Hydraulic Haptic Actuator for Simulation of Cardiac Catheters". *IEEE Transactions on Haptics (doi:10.1109/toh.2024.3364689)*.
- Suyong Kim and Doo Yong Lee. "Control Design for Haptic Systems". *KAIST Research Series, Springer (책) (doi:10.1007/978-981-99-8598-2)*.
- Min-Sung Kim, Chan-Young Park, and Doo-Yong Lee. "Control of Manufacturing Process of Soft Actuator Made of Magnetorheological Elastomer". *Journal of Institute of Control, Robotics and Systems (doi:10.5302/j.icros.2024.24.0021)*.

**2023**

- Qiaodi Yuan and Doo Yong Lee. "Tracking of Needle Grip for the Augmented Reality Simulation of Vascular Injection". *2023 23rd International Conference on Control, Automation and Systems (ICCAS) (doi:10.23919/iccas59377.2023.10316921)*.

**2022**

- Suyong Kim and Doo Yong Lee. "Control of Haptic Systems Based on Input-to-State Stability". *IEEE Access (doi:10.1109/access.2022.3157610)*.
- Chan Young Park and Doo Yong Lee. "Effects of a Fluoroscopy Agent on Radio Opacity and Steering Performance of Pressure-Driven Steerable Micro Guidewire". *2022 44th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC) (doi:10.1109/embc48229.2022.9871241)*.
- Suyong Kim and Doo-Yong Lee. "X-ray Image Rendering Using Centerlines and Truncated Cones of Blood Vessel Model for Real-time Simulation of Angiography". *Transactions of the Korean Society of Mechanical Engineers - B (doi:10.3795/ksme-b.2022.46.6.313)*.

**2021**

- Cheongjun Kim and Doo Yong Lee. "Adaptive Model-Mediated Teleoperation for Tasks Interacting With Uncertain Environment". *IEEE Access (doi:10.1109/access.2021.3112207)*.
- Seong Pil Byeon and Doo Yong Lee. "Adaptive surface representation based on homogeneous hexahedrons for interactive simulation of soft tissue cutting". *Computer Methods and Programs in Biomedicine (doi:10.1016/j.cmpb.2020.105873)*.
- Seunggyu Kang and Doo Yong Lee. "Hydraulically Steerable Micro Guidewire Capable of Distal Sharp Steering". *IEEE Transactions on Biomedical Engineering (doi:10.1109/tbme.2020.3013267)*.

## 소식

누리집 What's up 페이지의 글이다.[^news][^book]

- 2024-02-20 · 기계공학과 이두용 교수 공저 Control Design for Haptic Systems 출간

## 연락과 위치

- 교수 연구실: 기계동(N7) 5202[^me]
- 교수 전화: 042-350-3229[^me][^prof], 팩스 +82-42-350-3210[^prof]
- 교수 이메일: leedy@kaist.ac.kr[^me][^prof]
- 연구실 주소: Dept. Of Mechanical Engineering, KAIST 291 Daehak-ro, Yuseong-gu, Daejeon, 34141, Republic of Korea[^home]
[^p1]: C. Kim, D. Y. Lee, IEEE Access 9, 128188-128201 (2021). <https://doi.org/10.1109/access.2021.3112207> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: S. Kim, D. Y. Lee, IEEE Access 10, 27242-27254 (2022). <https://doi.org/10.1109/access.2022.3157610> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: C. Li, D. Y. Lee, IEEE Transactions on Haptics 17, 461-470 (2024). <https://doi.org/10.1109/toh.2024.3364689> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: S. Kang, D. Y. Lee, IEEE Transactions on Biomedical Engineering 68, 728-735 (2021). <https://doi.org/10.1109/tbme.2020.3013267> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: M. S. Kim, C. Y. Park, D. Y. Lee, IEEE Transactions on Medical Robotics and Bionics 7, 77-84 (2025). <https://doi.org/10.1109/tmrb.2025.3527718> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: C. Y. Park, D. Y. Lee, Journal of Micromechanics and Microengineering 35, 035003 (온라인 2025-02-10). <https://doi.org/10.1088/1361-6439/adaf2f> 초록 기준.
[^p7]: S. P. Byeon, D. Y. Lee, Computer Methods and Programs in Biomedicine 200, 105873 (2021). <https://doi.org/10.1016/j.cmpb.2020.105873> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: Q. Yuan, D. Y. Lee, Journal of Computational Design and Engineering 13, 69-83 (온라인 2026-02-24). <https://doi.org/10.1093/jcde/qwag015> 초록 기준.
[^home]: 연구실 누리집 첫 화면 <https://sites.google.com/view/rslab-kaist/> (THINGS WE DO, VIDEO LIST, Control Design for Haptic Systems 소개, 바닥글 주소, 2026-10-23 열람)
[^robotics]: 연구실 누리집 Researches > Medical Robotics 페이지 <https://sites.google.com/view/rslab-kaist/researches/medical-robotics> (Control Method for Haptic Rendering, Active-Steering Guidewire, 2026-10-23 열람)
[^sim]: 연구실 누리집 Researches > Medical Simulation 페이지 <https://sites.google.com/view/rslab-kaist/researches/medical-simulation> (Simulation Modeling, Visual Rendering, Haptic Interface for Medical Simulation, 2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <https://sites.google.com/view/rslab-kaist/people/members/professor> (E-mail, Phone, Fax, 학력·경력·수상·학회 활동, 2026-10-23 열람)
[^members]: 연구실 누리집 Members 페이지 <https://sites.google.com/view/rslab-kaist/people/members> (Post-Doc., Ph.D. Students, M.S. Students, Research Assistant, 2026-10-23 열람)
[^alumni]: 연구실 누리집 Alumni 페이지 <https://sites.google.com/view/rslab-kaist/people/alumni> (1–68번, 2026-10-23 열람)
[^news]: 연구실 누리집 What's up 페이지 <https://sites.google.com/view/rslab-kaist/whatup> (2026-10-23 열람)
[^book]: 연구실 누리집 What's up 글 「기계공학과 이두용 교수 공저 Control Design for Haptic Systems 출간」 <https://sites.google.com/view/rslab-kaist/whatup/기계공학과-이두용-교수-공저-control-design-for-haptic-systems-출간> (2024-02-20 게시, 2026-10-23 열람)
[^cr]: 2021–2026년 논문과 대표 논문의 출판사 등록 서지(Crossref) <https://api.crossref.org/> (교수 확인 기준은 근거 페이지, 2026-10-23 조회)
[^me]: KAIST 기계공학과 교수 상세(이두용) <https://me.kaist.ac.kr/pop/team.html?uid=42&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 연구실 웹사이트, E-mail, Office, Phone, 2026-10-23 열람)
[^mefield]: KAIST 기계공학과 연구분야 로보틱스/제어/모빌리티 페이지 <https://me.kaist.ac.kr/research/research_010100.html> (이두용 항목의 연구주제, 주요 응용 산업, 연구실, 2026-10-23 열람)
[^mefield4]: KAIST 기계공학과 연구분야 헬스케어/나노/광학 페이지 <https://me.kaist.ac.kr/research/research_010400.html> (이두용 항목의 연구주제, 주요 응용 산업, 2026-10-23 열람)

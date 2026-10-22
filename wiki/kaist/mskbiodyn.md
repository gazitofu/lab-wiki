# 근골격 운동역학 연구실 (Musculoskeletal BioDynamics Lab)

**KAIST 기계공학과 · 구승범 교수**

- 분야: 근골격 생체역학, 이중 X선 투시 영상을 이용한 관절 뼈 움직임 분석, 근골격 모델링·시뮬레이션, 강화학습 기반 신경근 제어 시뮬레이션, 운동 보조 기기 제어
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 착용형 로봇·외골격[^ad][^p7][^p8], 강화학습[^nc][^p5][^p8], X선 영상·회절[^ma][^p2], 3차원 복원·인식[^ma][^p2], 계산신경과학[^nc][^p5], 디지털 휴먼·아바타[^nc][^p6], 제어 이론·제어 공학[^ad][^p8], 재활·보조·접근성 기술[^ad]
- 홈페이지: <https://mskbiodyn.kaist.ac.kr/>
- 근거와 출처: [근골격 운동역학 연구실 근거 페이지](mskbiodyn-sources.md)

> 사람이 걸을 때 뼈와 근육, 신경이 움직임을 어떻게 만들어 내는지 재고 계산하는 연구실이다. 고속 X선 영상으로 관절 속 뼈의 움직임을 재고, 살아 있는 사람에게서 직접 잴 수 없는 관절 안의 힘을 근골격 모델로 계산하며, 강화학습으로 가상 인체 모델을 걷게 해 신경 제어의 원리를 살피고, 가상 인체로 외골격 같은 운동 보조 기기의 제어 방법을 만들고 시험한다.[^home][^ma][^mm][^nc][^ad]

## 무엇을 연구하나

누리집 첫 화면은 연구실의 목표를 「근골격 동역학과 AI 기반 신경운동 생성 융합을 통한 정형외과 헬스케어 및 운동 보조 기술 혁신」으로 적는다. 연구 비전 절은 인대 손상, 변형, 노화, 관절 퇴행으로 관절이 망가지는 이유와 사람이 계속 움직이게 하는 방법을 묻고, 사람의 움직임을 그것을 만드는 뼈와 근육, 신경 제어 수준까지 연구한다고 소개한다. 보이지 않는 것을 재고 잴 수 없는 것을 시뮬레이션하는 것이 연구 방식이며, 의사가 관절을 되살리도록 돕고 몸이 한계에 이른 사람을 로봇이 돕게 하는 것을 목표로 적는다.[^home] 기계공학과 교수 소개는 연구분야를 Human musculoskeletal biomechanics(사람 근골격 생체역학)와 Human joint kinematic analysis and dynamics simulation(사람 관절의 운동학 분석과 동역학 시뮬레이션)으로 적는다.[^mep] 기계공학과 연구분야 페이지는 헬스케어/나노/광학 분야에서 교수의 연구주제를 Human Joint Kinematics, Musculoskeletal Biomechanics, Orthopaedic Medical Devices로, 로보틱스/제어/모빌리티 분야에서 Human movement and control, Movement assistance로 적는다.[^mer4][^mer1]

Research 메뉴는 연구를 네 묶음으로 나눈다. 뼈와 몸 표면의 움직임을 정밀하게 재는 동작 분석, 몸 안 관절에 걸리는 힘을 계산하는 근골격 모델링·시뮬레이션, 가상 인체가 걷도록 가르치는 신경근 제어와 운동 생리 연구, 몸에 맞게 작동하는 운동 보조 기기 연구다.[^ma][^mm][^nc][^ad] 측정에는 힘판(발이 디딜 때 바닥에 가하는 힘을 재는 판)과 무선 근전도 장비를 동기화한 광학 동작 포착 장비와, 걷는 사람의 관절을 따라가며 두 방향에서 연속 X선 영상을 찍는 로봇형 이중 X선 투시 장비를 쓴다.[^ma][^eq] 계산에는 해부 구조를 따른 무릎·발 관절과 Hill형 근육 모델을 넣은 하지 근골격 모델과, 심층 강화학습(시행착오를 거쳐 보상이 커지는 행동을 배우는 기계학습)으로 훈련한 신경망 제어기를 쓴다.[^home][^mm][^nc] 장비 페이지는 사람의 움직임에서 에너지 효율이 높은 로봇 동작을 만드는 연구에 쓰는 Unitree G1 휴머노이드 로봇 두 대도 든다.[^eq]

대표 논문으로 보면 연구는 네 갈래다. 첫째, 걷기 자료와 X선 영상으로 사람의 움직임과 관절 속 뼈의 움직임을 재는 연구다. 20–59세 건강한 남성 120명의 일상 동작을 모은 공개 데이터셋 Gait120과(대표 논문 1), 전방십자인대와 전외측인대를 함께 재건한 무릎의 걷기 중 움직임을 이중 X선 투시 영상으로 잰 연구가 있다(대표 논문 2).[^p1][^p2] 둘째, 근골격 모델로 인대 손상이나 평발이 관절 안의 힘을 어떻게 바꾸는지 계산한 연구다(대표 논문 3, 4).[^p3][^p4] 셋째, 신경망 제어기로 근골격 모델을 걷고 달리게 하며 척수 반사의 역할과 달릴 때 팔을 흔드는 이유를 살핀 연구다(대표 논문 5, 6).[^p5][^p6] 넷째, 엉덩관절 보조 기기를 입은 사람의 반응을 재고, 걸음 단계를 추정하지 않는 엉덩관절 외골격 제어기를 만든 연구다(대표 논문 7, 8).[^p7][^p8] 연구 페이지는 정형외과 의사들과 함께 무릎 내전 모멘트, 발목 일률 같은 3차원 보행 지표를 무릎·발목 골관절염, 뇌성마비, 발 변형의 X선 소견과 잇는 임상 보행 분석도 동작 분석 장비의 쓰임으로 든다.[^ma]

## 주요 연구 주제

### 1. 정밀 동작 분석: 몸 표면과 뼈의 움직임

연구실 동작 분석실은 광학 동작 포착 장비(Vicon)를 힘판, 무선 근전도와 동기화해 쓴다. 몸에 붙인 반사 마커를 고속 적외선 카메라가 따라가 3차원 궤적을 만들고, 이를 지면반력과 합쳐 역운동학으로 관절 각도를, 역동역학으로 관절 모멘트와 일률을 계산한다. 이 자료는 근골격 시뮬레이션의 기준 동작으로도 쓴다.[^ma] 쓰임으로는 공개 보행·근전도 데이터셋 Gait120 구축, 사람마다 걸음의 운동학이 사람을 구별할 만큼 고유하다는 것을 보이고 기계학습으로 비정상 보행 양상을 찾아낸 연구, 압력 깔창과 발-지면 접촉 모델로 지면반력을 추정하고 가속도계 하나로 전신 동작을 예측하는 연구를 든다.[^ma]

피부에 붙인 마커는 움직이는 동안 뼈 위에서 미끄러지고 흔들린다. 연구 페이지는 이 연조직 오차가 특히 허벅지에서 재려는 관절 움직임만큼 클 수 있다고 적는다. 연구실은 몸 표면과 연조직이 뼈대 위에서 움직이는 방식을 나타내는 변형 가능한 인체 모델을 만들어 마커 궤적에 맞추고, 피부 움직임을 빼 뼈의 움직임을 되찾는다. 같은 모델을 일반 영상에 맞추면 카메라만으로 3차원 몸 형태와 뼈대 움직임을 추정하는 마커 없는 동작 포착이 되어, 실험실 밖에서도 움직임을 잴 수 있다.[^ma]

피부 기반 측정으로는 관절 면이 서로 미끄러지고 구르는 것 같은 뼈 사이의 작은 움직임을 잡을 수 없다. 연구실은 이를 직접 재려고 X선으로 뼈대를 두 방향에서 고속 촬영하는 장비를 개발했다. 이 로봇형 이중 X선 투시 장비는 무릎이나 발목 같은 대상 관절을 따라가며, 사람이 러닝머신을 걷는 동안 100 Hz로 두 방향 X선 영상을 연속 촬영한다. CT로 만든 3차원 뼈 모델을 각 영상 쌍에 맞추는 3차원-2차원 정합으로 관절 속 각 뼈의 6자유도 움직임을 얻는다.[^ma] 모의 X선 영상(DRR, digitally reconstructed radiograph)을 빨리 만드는 방법, 뼈 모양과 밀도의 통계 모델, 해부학적 기준점 자동 검출 같은 영상 분석 방법도 함께 개발한다. 이 장비로 걷는 동안 건강한 무릎·발목·발 관절의 움직임, 인대 손상과 변형이 바꾼 관절 움직임, 수술이 자연스러운 관절 움직임을 얼마나 되살리는지를 잰다.[^ma] 대표 논문 1은 20–59세 건강한 남성 120명이 평지 걷기, 계단과 경사로 오르내리기, 앉고 일어서기 등 일곱 가지 동작을 하는 동안 광학 동작 포착 장비, 힘판, 표면 근전도 센서로 모은 데이터셋이고,[^p1] 대표 논문 2는 이중 X선 투시 영상과 뼈 모양·밀도의 통계 모델, 2D-3D 정합으로 재건 수술을 받은 무릎의 뼈 움직임을 재구성해 건강한 무릎과 비교했다.[^p2] 대표 논문 1, 2.

### 2. 근골격 모델링과 관절 하중 계산

연골 면 사이의 접촉력, 인대의 장력, 근육 하나하나의 힘처럼 관절 안의 힘은 살아 있는 사람에게서 직접 잴 수 없다. 연구실은 이를 추정하려고 실제 해부 구조를 따르는 관절을 넣은 근골격 모델을 만든다. 관절면 접촉과 연동 움직임을 넣은 무릎, 여러 분절로 나눈 발, 척추뼈와 갈비뼈를 하나씩 나타낸 척추가 그 예다. 잰 동작과 지면반력으로 모델을 움직여 근육 힘과 관절 접촉력을 풀고, 센서를 넣은 무릎 인공관절에서 얻은 힘 같은 생체 내 자료와 비교해 검증한다.[^mm] 쓰임으로는 전신 모델의 관절면에 접촉 요소를 넣어 걷는 동안 무릎 안쪽·바깥쪽 접촉력을 예측하고 센서 인공관절 측정값과 비교한 무릎 접촉 모델, 이중 X선 투시 측정으로 무릎을 굽힐 때 정강뼈가 함께 미끄러지고 도는 관계를 모델로 만든 연구, 발목과 발 안의 여러 관절(쇼파르·리스프랑·중족지 관절)의 접촉력과 근육 힘을 계산하는 다섯 분절 발 모델, 같은 대상자와 동작으로 OpenSim과 AnyBody Modeling System을 비교한 연구를 든다.[^mm]

손상과 변형은 움직임뿐 아니라 관절 안 구조물이 힘을 나눠 받는 방식도 바꾸고, 연구 페이지는 이런 하중 분포 변화가 2차 손상과 관절 퇴행으로 이어질 수 있다고 적는다. 연구실은 근골격 모델과 유한요소 모델을 특정 손상·변형에 맞게 고치고, 잰 동작 자료로 돌려 인대·연골·연조직의 하중 변화를 계산한다.[^mm] 대표 논문 3은 사체 자료로 만든 인대 14개의 무릎 모델에서 전방십자인대의 강성을 낮추거나 처음 길이를 늘려 손상 정도를 나타내고, 걷는 동안 정강뼈가 앞으로 밀리는 정도와 인대 장력의 변화를 계산했다.[^p3] 대표 논문 4는 다섯 분절 발 모델에서 스프링 인대의 강성을 낮춰 유연성 평발을 나타내고, 이를 전신 근골격 모델에 붙여 걷기를 역동역학으로 계산해 평발인 참가자의 경거관절 바깥쪽 접촉력이 정상 발 참가자보다 유의하게 크다는 것을 보였다.[^p4]

연구실은 수술도 가상으로 한다. 인대 이식편을 붙이는 위치나 어느 관절을 고정·재정렬할지 같은 수술 선택지에 맞춰 근골격 모델의 해부 구조를 바꾸고, 각 사람의 잰 동작으로 걷기를 시뮬레이션해 선택지마다 관절 안정성, 인대 힘, 관절 접촉력을 비교한다. 3차원 의료 영상으로 인대 재건용 터널 위치와 환자 맞춤 이식편 모양 같은 수술 세부도 계획한다.[^mm] 예로 대퇴골 부착 위치를 달리한 전방십자인대 이식편 비교와 거골하 관절 유합 시뮬레이션을 들고, 유연성 평발의 절골술과, 근위 경골 절골술(정강뼈 윗부분을 잘라 다리 축을 바로잡는 수술)을 포함한 무릎 절골술로 가상 수술을 넓히고 있다고 적는다.[^mm] 대표 논문 3, 4.

### 3. 신경근 제어와 강화학습 보행 시뮬레이션

근골격 모델은 몸 안에 작용하는 힘을 보여 주지만 스스로 움직이지 못하고, 순간마다 각 근육을 얼마나 세게 수축할지 정하는 제어기가 필요하다. 연구실은 이 제어기를 심층 강화학습으로 훈련한다. 신경망 제어기는 물리 시뮬레이션 속 시행착오로 최대 150개 근육의 전신 모델을 움직이는 법을 배우며, 먼저 잰 사람 동작을 흉내 낸 뒤 스스로 걷고 달린다. 훈련한 제어기는 다른 바닥면, 몸, 과제처럼 보지 못한 조건에 놓을 수 있어, 사람에게 시험하기 어렵거나 위험한 질문을 시뮬레이션으로 살필 수 있다.[^nc] 쓰임으로 연구 페이지는 미끄러운 바닥에서 맞서는 다리 근육의 동시 수축이 높은 제어기가 더 안정적으로 걸었다는 결과, 이상적인 러닝머신은 평지 걷기와 같은 다리 움직임을 만들고 차이는 벨트가 걸음마다 받는 힘에 맞서 속도를 유지하지 못할 때 생긴다는 결과, 같은 대상자에게 순동역학 시뮬레이션과 기존 역동역학 분석을 비교해 역동역학이 기계적 일률을 낮게 추정하며 그 주된 이유가 식을 맞추는 데 필요한 잔차 힘이라는 결과를 든다.[^nc]

걷기는 신경계 여러 수준에서 제어된다. 연구 페이지는 뇌가 걸음마다 예측적인 긴 지연의 명령을 보내고, 척수 반사는 근육과 관절이 느낀 것에 수십 밀리초 안에 반응한다고 설명한다. 사람에게서는 두 경로가 늘 함께 작동해 각각의 몫을 가리기 어렵기 때문에, 연구실은 경로를 나눈 신경 제어기를 만들어 근골격 모델을 걷게 훈련하고 한 번에 한 경로씩 빼는 가상 절제(virtual ablation)로 각 경로의 역할을 살핀다.[^nc] 대표 논문 5는 척수 상위 경로만 있는 제어기, 반사만 있는 제어기, 반사 이득을 동적으로 조절하는 제어기, 둘을 합친 제어기의 네 구조를 14자유도·Hill형 근육 22개 근골격 모델에서 근위 정책 최적화로 훈련해 비교했다.[^p5] 대표 논문 6은 근육 150개를 넣은 전신 달리기 모델과 인공 신경망 기반 달리기 제어기로 팔을 능동적으로 흔들 때, 수동적으로 흔들릴 때, 팔을 고정할 때를 시뮬레이션해 비교했다.[^p6] 연구 페이지는 연구팀이 NeurIPS 2023 MyoChallenge 보행 부문에서 2위를, 2024년에는 15개국 54개 팀 가운데 1위를 했다고 적는다.[^nc] 대표 논문 5, 6.

### 4. 운동 보조 기기와 사람 중심 제어

연구 페이지는 보조 기기가 관절에 토크를 더하기만 하는 것이 아니라고 설명한다. 몸에 바깥 힘이 작용하면 신경계가 관절과 근육의 협응을 바꾸며, 이 조정은 기기를 돕기도 하고 거스르기도 한다. 기기는 흔히 사용자 평균으로 평가되지만 평균은 사람마다 다른 반응을 가릴 수 있어, 연구실은 보조를 받을 때의 걸음과 근육 활동 변화를 집단과 개인 수준에서 함께 잰다.[^ad] 대표 논문 7은 엉덩관절 보조 소프트 엑소슈트를 입은 건강한 성인 22명에게 걸음 주기 안에서 시작·정점·끝 시점이 다른 보조 힘 프로파일 8가지를 주고 하지 운동학과 근전도를 쟀다.[^p7]

사람에게 직접 보조 기기를 맞추는 일은 느리고 힘들며 일부 설정은 위험할 수 있다. 연구실은 강화학습 보행 제어기로 움직이는 근골격 모델에 모의 기기를 붙여 걷게 하고, 제어기 설정이 대사 비용, 관절 하중, 안정성에 미치는 영향을 사람이 기기를 입기 전에 시험한 뒤 유망한 제어기만 사람 실험으로 넘긴다.[^ad] 대표 논문 8은 걸음 단계를 따로 추정하지 않고 지연·증폭한 엉덩관절 각도에 고조파 성분을 더해 보조 토크를 만드는 제어기(MDOFC)를 제안하고, 강화학습 기반 신경망 제어기를 쓴 순동역학 보행 시뮬레이션으로 변수를 최적화했다.[^p8] 연구 페이지는 엉덩관절 근육처럼 특정 근육을 약하게 만든 환자 모델에 여러 관절 보조 기기를 붙이고 기기 제어기를 강화학습으로 훈련해 정상에 가까운 걸음을 되찾게 하는 연구로, 근력이 약한 사람을 위한 보조를 임상 시험 전에 설계한다고 적는다.[^ad]

유연한 소재로 만든 소매·슈트 같은 소프트 착용형 기기는 단단한 틀이 없어, 기기가 내는 모든 힘이 피부와 연조직을 거쳐 관절에 닿는다. 연구실은 사실적인 몸 표면 모델(STAR)을 뼈대 모델과 맞추고 기기 안쪽 면과 피부의 접촉을 풀어, 보조 관절 토크와 피부 압력, 구동기마다 내야 할 힘을 한 번의 시뮬레이션에서 얻는 방법을 개발한다. 무릎을 감싸는 얇은 육면체 셀이 하나하나 수축하는 보조 소매(THAS)도 제안해, 소매 앞쪽을 수축해 무릎 펴기를 돕는 방식과 뒤쪽을 수축해 굽히기를 돕는 방식을 비교했다.[^ad] 대표 논문 7, 8.

## 대표 논문

누리집 Publications 목록의 2021–2026년 학술지 논문 가운데 구승범 교수에게 교신 표시(*)가 있는 논문에서, 네 연구 갈래에 고르게 여덟 편을 골랐다. 여덟 편 모두 구승범 교수가 마지막 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2025 | [Comprehensive human locomotion and electromyography dataset: Gait120](https://doi.org/10.1038/s41597-025-05391-0) · Scientific Data | 사람의 걸음과 그 변화를 이해하려면 여러 나이대와 동작을 아우르는 자료가 필요하다. 20–59세 건강한 남성 120명이 평지 걷기, 계단 오르기·내려가기, 경사로 오르기·내려가기, 앉았다 일어서기·섰다 앉기의 일곱 가지 동작을 하는 동안 광학 동작 포착 장비, 힘판, 오른쪽 다리의 표면 근전도 센서로 자료를 모았다. 최종 데이터셋은 모든 동작에 걸친 6,882개 동작 주기와 전신 관절 운동학, 근육 활동 양상을 담는다. 일상 동작에서 넓은 성인 남성 집단의 움직임과 근육 활성 변화를 이해하는 데 보탬이 될 것으로 본다.[^p1] | 1저자 J. Boo(Junyo Boo), 마지막·교신 저자 구승범 (4명) |
| 2 | 2026 | [ISB clinical biomechanics award winner 2025: Residual translational and rotational kinematics after combined anterior cruciate ligament and anterolateral ligament reconstruction during walking – A biplanar fluoroscopy analysis](https://doi.org/10.1016/j.clinbiomech.2026.106870) · Clinical Biomechanics | 전방십자인대가 끊어지면 무릎이 불안정해지고, 재건 수술 뒤에도 불안정이 남는 환자가 있어 무릎의 보조 안정 구조인 전외측인대가 주목받는다. 단일 다발 전방십자인대 재건과 전외측인대 재건을 함께 받은 10명과 건강한 10명이 러닝머신을 걷는 동안 이중 X선 투시 영상 장비로 찍고, 뼈 모양·밀도의 통계 모델과 2D-3D 정합으로 각자의 3차원 모델과 무릎 움직임을 재구성했다. 수술한 무릎은 반대쪽 무릎과 건강한 무릎에 비해 디딤기(발이 바닥에 닿아 있는 구간)의 17–85% 구간에서 정강뼈가 유의하게 앞으로 더 밀렸고, 디딤기 초반(15–37%)에는 정강뼈의 안쪽 회전이 건강한 무릎보다 유의하게 컸다. 이 수술 조합이 정상 관절 움직임을 다 되살리지 못하고 불안정이 남는다고 본다.[^p2] | 1저자 J. Oh(Jeongseok Oh), 마지막·교신 저자 구승범 (4명) |
| 3 | 2023 | [Influences of Partial Anterior Cruciate Ligament Injury on Anterior Cruciate Ligament Tensional Force and Kinematic Stability During Walking](https://doi.org/10.1115/1.4054982) · Journal of Biomechanical Engineering | 전방십자인대의 부분 파열이나 늘어남은 무릎의 동적 기능을 바꾸지만, 걷는 동안 무릎 움직임에 미치는 영향은 자료가 부족하다. 정상인 5명의 동작과 지면반력을 재고, 사체 자료로 인대 14개를 넣은 무릎 모델을 만든 뒤 전방십자인대의 처음 길이와 강성을 바꿔 손상 모델을 만들어 걷기 근골격 시뮬레이션을 했다. 인대 강성을 원래의 25%로 낮추면 정강뼈의 평균 앞쪽 이동이 2.6 ± 0.7 mm, 처음 길이를 10% 늘리면 2.6 ± 0.3 mm 유의하게 늘었다. 부분 파열에서는 손상 정도가 커지면서 인대 힘이 비선형으로 줄었고 늘어난 인대에서는 선형으로 줄었으며, 부분 파열은 이동 방향의 불안정을, 완전 파열은 회전과 이동 방향의 불안정을 함께 일으켰다.[^p3] | 1저자 Y.-J. Koo(Young-Jun Koo), 마지막·교신 저자 구승범 (4명) |
| 4 | 2023 | [Increase in lateral contact force in the tibiotalar joint during walking in flatfoot patients with reduced stiffness of the spring ligament](https://doi.org/10.1016/j.jbiomech.2023.111711) · Journal of Biomechanics | 유연성 평발의 안쪽 아치가 낮아지고 뒷발이 바깥으로 기우는 변형은 걷는 동안 경거관절 주변의 힘 분포를 바꿔 2차 손상 위험을 높인다. 경거관절 주변의 동역학을 계산하는 다섯 분절 발 모델을 만들고, 정상 발 모델의 스프링 인대 강성을 바꿔 평발 모델을 만들었다. 정상 발 10명과 유연성 평발 10명의 걷기 자료(몸 움직임, 지면반력, 발바닥 압력)로 전신 근골격 모델의 역동역학 시뮬레이션을 했다. 평발 참가자는 경거관절 바깥쪽 접촉력(체중의 1.19배 대 0.80배)이 유의하게 컸고 압력 중심이 더 뒤쪽에 있었으며(33.7% 대 46.6%), 뒤정강근 힘의 평균과 최댓값도 컸다(체중의 3.06배 대 2.22배, 4.52배 대 3.33배). 이런 역학 변화가 관절염 위험에 영향을 줄 수 있다고 본다.[^p4] | 1저자 Y. Son(Yooha Son), 마지막·교신 저자 구승범 (3명) |
| 5 | 2026 | [Spinal reflexes with dynamic gain modulation contribute to robust walking: a comparative study of simulated neural controllers](https://doi.org/10.1186/s12984-026-02157-6) · Journal of NeuroEngineering and Rehabilitation | 사람의 걷기는 예측적이고 지연이 긴 척수 상위(뇌 쪽) 명령과 반응적이고 지연이 짧은 척수 반사를 합친 위계적 운동 제어로 만들어진다. 가상 절제 틀에서 네 가지 제어기 구조(척수 상위만, 반사만, 이득을 동적으로 조절하는 반사, 둘의 결합)를 비교했고, 각 구조는 척수 상위 부분으로 다층 퍼셉트론을 쓰며 14자유도·Hill형 근육 22개 근골격 모델에서 기준 동작을 따르도록 근위 정책 최적화로 훈련했다. 교란이 없을 때는 척수 상위 제어기도 결합 제어기와 비슷한 정확도로 하지 운동학을 재현했지만(평균 RMSE ≈ 1–2°), 골반에 가한 힘이나 바닥 속도 변화 같은 교란에서는 반사가 있는 제어기가 생존율이 높고 전체 근육 활성을 적게 썼다. 척수 반사 경로의 주된 기능은 환경이 불확실할 때 빠르고 노력을 아끼는 교란 대응이며, 사람과 비슷한 걸음 단계별 반사 조절은 교란 훈련 뒤에만 나타났다.[^p5] | 1저자 G. Park(Gunwoo Park), 마지막·교신 저자 구승범 (4명) |
| 6 | 2025 | [Active Arm Swing During Running Improves Rotational Stability of the Upper Body and Metabolic Energy Efficiency](https://doi.org/10.1007/s10439-025-03688-0) · Annals of Biomedical Engineering | 달릴 때 팔 흔들기가 상체 안정에 주는 이점은 연구됐지만 대사 에너지 효율에서의 역할은 논란이 남아 있다. 팔을 능동적으로 흔들면 몸통의 세로축 회전과 대사 에너지 소비가 함께 줄어든다는 가설을, 근육 150개를 넣은 전신 근골격 달리기 모델과 인공 신경망 기반 달리기 제어기로 시험했다. 능동적으로 흔드는 팔, 수동적으로 흔들리는 팔, 고정한 팔의 세 조건에서 이동 거리당 에너지 비용은 각각 5.52, 5.73, 5.82 J/kg-m로 능동 조건이 가장 낮았고, 팔 근육의 에너지 소비는 능동 조건에서 컸지만 전체 소비는 작았다. 몸통 세로축 회전도 능동 조건에서 가장 작아, 달릴 때 팔 흔들기가 에너지를 아끼는 능동적 방식이라는 근거로 본다.[^p6] | 1저자 Y.-J. Koo(Young-Jun Koo), 마지막·교신 저자 구승범 (3명) |
| 7 | 2026 | [Common gait modulation by presence of hip assistance, individual motor strategies by assistance timing](https://doi.org/10.1016/j.gaitpost.2026.110286) · Gait & Posture | 엉덩관절 보조 소프트 엑소슈트는 보조 힘 프로파일의 시점을 옮겨 조정하는데, 프로파일에 대한 반응이 사람들 사이에 일반화되는지 사람마다 다른지는 분명하지 않았다. 1.1 m/s로 걷는 건강한 성인 22명(11명씩 두 집단)에게 슈트만 입은 상태와, 걸음 주기 안의 시작·정점·끝 시점을 달리한 엉덩관절 보조 힘 프로파일 8가지(A–H)를 비교하고, 한 프로파일을 오래 쓰는 조건도 살폈다. 보조는 프로파일과 관계없이 일관된 반응을 낳아 엉덩관절 최대 굽힘(8개 중 7개)과 발목 최대 배측굴곡(8개 중 8개)이 늘고 가자미근 활성(8개 중 6개)이 줄었으며, 프로파일 사이 평균 차이는 작았다. 걸음 단위 분류에서 다른 참가자로는 일반화가 약했지만 한 사람 안에서는 프로파일이 뚜렷이 구별됐다(macro-F1 > 0.98). 착용형 보조의 평가와 최적화는 공통 반응과 개인별 반응을 함께 고려해야 한다고 본다.[^p7] | 1저자 J. Kim(Juhyeop Kim), 마지막·교신 저자 구승범 (5명) |
| 8 | 2026 | [Design and Validation of a Modified Delayed Output Feedback Controller for Hip Exoskeleton Assistance](https://doi.org/10.1109/tnsre.2026.3682054) · IEEE Transactions on Neural Systems and Rehabilitation Engineering | 기존 보행 보조 제어기는 추정한 걸음 단계에 맞춰 미리 정한 토크 프로파일을 주는데, 방향 전환 같은 변화에 약하다. 지연·증폭한 관절 각도로 단계 추정 없이 토크를 만드는 지연 출력 되먹임 제어(DOFC)는 단순한 모양의 토크만 낼 수 있었고, 이 논문은 고조파 성분을 더해 적응적인 토크 프로파일을 만드는 MDOFC를 제안했다. 변수는 강화학습 기반 신경망 제어기를 쓴 순동역학 보행 시뮬레이션으로 최적화했다. 시뮬레이션에서 MDOFC는 DOFC처럼 변수 두 개만으로 순 대사 비용 감소를 늘렸고, 단기 랴푸노프 지수로 본 동적 안정성을 최대 45 W까지 유지했다. 사람 실험에서는 DOFC와 비슷한 대사 비용 감소를 기계적 일률을 8.8% 적게 쓰며 얻었다.[^p8] | 1저자 S. Yoon(Seungwoo Yoon), 마지막·교신 저자 구승범 (4명) |

## 교수와 전문 분야

구승범 교수는 KAIST 기계공학과 교수이며, 기계공학과 교수 소개는 최종학위를 Ph.D., Stanford University (2006), 연구실을 근골격 운동역학 연구실로 적는다.[^mep][^mel] 연구실 Professor 페이지에 따르면 서울대학교에서 학사(1993–2000년)와 석사(2000–2002년)를, 미국 Stanford University에서 기계공학 박사(2002–2006년)를 받았고, 박사 논문은 건강한 사람, 전방십자인대 결손 환자, 골관절염 환자의 걸음 생체역학에 따른 무릎 관절 연골의 형태 변화를 다뤘다. 이후 Stanford University 기계공학과 박사후연구원(2006–2007년)과 같은 대학 영상의학과 Staff Research Scientist(2007–2009년)를 거쳐 중앙대학교 기계공학부 조교수(2009–2013년)와 부교수(2013–2018년)를 지냈다.[^prof] 연구 페이지는 Stanford 시절에 관절 하중과 접촉 기하가 연골 두께와 어떻게 관련되는지 연구했다고 적는다.[^mm]

Professor 페이지는 학회 활동으로 International Society of Biomechanics Council member(2025년부터), Asian-Pacific Association for Biomechanics Council member(2021년부터), ISO/TC150 Member(2017–2022년)를 적고, Frontiers in Bioengineering and Biotechnology(2023–2024년), International Journal of Precision Engineering and Manufacturing(2017–2024년), Journal of Mechanical Science and Technology(2016–2025년), Transactions of the Korean Society of Mechanical Engineers(2013–2018년)의 Associate Editor를 지냈다고 적는다. 국내에서는 대한기계학회 평의원(2016년부터), 대한정형외과연구학회 평의원(2016년부터), 대한생체역학회 이사(2014년부터), 대한기계학회 바이오공학부문 이사(2010년부터)를 적는다.[^prof] 같은 페이지의 Awards 칸은 2013–2017년 항목으로 중앙대학교 재직 시기에 해당하며, 「Winner of the Sixth Grand Challenge Competition to Predict In-vivo Knee Loads」(2016, ASME Bioengineering 주최, NIH 후원), 「Second place in the Fifth Grand Challenge Competition to Predict In-vivo Knee Loads」(2014), 「KSME Research Excellence Award in Bioengineering」(2017), Journal of Biomechanics의 「Certificate of Excellence in Reviewing」(2014)과 국내 학회·학술지의 Best paper·Best poster 항목 6건을 적는다.[^prof] 연구 페이지는 2016년 대회 우승을 연구실의 무릎 접촉 모델 성과로 소개한다.[^mm]

News 페이지에 따르면 교수는 2023년 7월 일본 교토에서 열린 ISB TGCS(Technical Group on Computer Simulation) 학술대회에서 「Forward dynamics gait simulation of musculoskeletal human model using reinforcement learning」을 주제로 기조 강연을 했다. 같은 페이지는 Journal of Mechanical Science and Technology Associate Editor 활동으로 받은 Outstanding Contribution Award(2024년 3월 27일, 9월 26일 게시)와 대한기계학회(KSME) Certificate of Appreciation(2025년 5월 21일 게시)도 적는다.[^news] Classes 페이지는 대학원 강의 ME642 Biomechanics(생체역학, 2021·2022·2024·2026년 가을 학기)와 학부 강의 ME454 동역학시스템 프로그래밍 등을 적는다.[^classes]

논문으로 보면 최근 전문 분야는 네 갈래다. 동작 포착·근전도 데이터셋과 이중 X선 투시 영상으로 사람의 움직임과 관절 속 뼈 움직임을 재는 측정(대표 논문 1, 2),[^p1][^p2] 인대 손상과 평발이 관절 하중에 주는 영향을 계산하는 근골격 모델링(대표 논문 3, 4),[^p3][^p4] 신경망 제어기로 근골격 모델을 걷고 달리게 해 신경 제어와 운동 원리를 살피는 시뮬레이션(대표 논문 5, 6),[^p5][^p6] 엉덩관절 보조 기기에 대한 사람의 반응과 외골격 제어기 설계(대표 논문 7, 8)다.[^p7][^p8]

## 응용 분야

첫 화면은 연구실의 연구가 운동 과학을 환자와 일상생활의 실제 이익으로 바꾼다고 적고 세 방향을 든다. 정형외과 분야에서는 인대 손상, 발 변형, 관절 퇴행이 관절 움직임과 하중을 어떻게 바꾸는지 보이고, 전방십자인대 재건술과 절골술 같은 수술 치료가 자연스러운 관절 기능을 얼마나 되살리는지 평가한다. 일상 이동 분야에서는 미끄러운 바닥에서 사람이 안정을 유지하는 방식과 낙상에 이르는 원인을 연구하고 사람마다 도움이 되는 보조 기기를 개발한다. 연구 공동체에는 Gait120 같은 공개 데이터셋을 나누고 NeurIPS MyoChallenge 같은 벤치마크에 참여한다.[^home] 기계공학과 연구분야 페이지는 교수 연구의 주요 응용 산업을 「의료 / 인체 운동 보조 기술」로 적는다.[^mer1] News 페이지에 따르면 연구실은 2023년 Robot World(Kintex)에서 KIMM의 하드웨어 시제품과 함께, 형상기억합금 구동기로 걷기를 돕는 소프트 슈트의 시뮬레이션을 선보였다.[^news] 장비 페이지는 사람의 움직임에서 에너지 효율이 높은 로봇 동작을 만드는 연구에 휴머노이드 로봇을 쓴다고 적는다.[^eq]

## 구성원

연구실 누리집 Members 페이지의 학생 10명이다(박사과정 5, 석사과정 5). 과정과 시작은 카드의 「Started PhD course in …」·「Started MS course in …」 줄이고, 연구 주제는 카드에 적힌 연구 항목을 「;」로 이었다. 박사과정 5명의 카드에는 KAIST 석사 학위(2020–2026년)와 석사 논문 제목도 적혀 있다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Junyo Boo (부준요) | 박사과정 | September 2022 | Dual X-ray fluoroscopic analysis for skeletal kinematics of the foot; Anatomical multi-segment foot model for dynamics simulation; Forward dynamics simulation of musculoskeletal human model | 1 |
| GUNWOO PARK (박건우) | 박사과정 | March 2023 | Supervised learning on gait kinematic data; Deep-learning-based human motion generation | 5, 7 |
| Beomsoo Shin (신범수) | 박사과정 | March 2023 | Anatomical knee joint model for dynamics simulation; Forward dynamics simulation musculoskeletal human model |  |
| Jonghyeon park (박종현) | 박사과정 | March 2024 | Deformable dynamics model for human-exoskeleton interface; Reinforcement learning of human-exoskeleton interaction |  |
| Kyubin chun (천규빈) | 박사과정 | March 2026 | Human movement kinematics and EMGs in large cohort; Neural control during gait perturbations |  |
| JEONGHA CHO (조정하) | 석사과정 | March 2024 | Dynamics and control of human motion |  |
| Jaehyun park (박재현) | 석사과정 | September 2025 | Foot and ankle kinematics during walking; Dual X-ray 2D/3D skeleton registration |  |
| Sunghyun Kim (김성현) | 석사과정 | March 2026 | Gait assistive device control; Humanoid robot control |  |
| Hyeonwoo Lee (이현우) | 석사과정 | March 2026 | Knee kinematics changes with high tibial osteotomy; Dual X-ray 2D/3D skeleton registration |  |
| JOEUN Lee (이조은) | 석사과정 | September 2026 | Kinematics and kinetics of fall during walking; Neuronal control during standing and falls |  |

## 졸업생과 이전 구성원

누리집 Alumni 페이지의 20명이다. 학위·과정 칸은 카드의 학위·연구원 줄(Obtained PhD degree at KAIST, MS degree, Postdoctoral Fellow 등)을 그대로 이었고, 진로는 카드 첫 줄, 학위 논문은 카드의 Thesis 줄이다(박사·석사 논문이 모두 있으면 「/」로 이었다).[^alumni] 교수는 2018년까지 중앙대학교 기계공학부에 있었고 카드 대부분은 학위를 받은 학교를 적지 않으므로, 2018년 이전에 시작한 학위와 연구원 경력은 KAIST가 아닌 이전 소속 시기의 것일 수 있다.[^prof][^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Jeongseok Oh (오정석) | Postdoctoral Fellow, 2025-2026; Obtained PhD degree at KAIST, 2021-2025; Obtained MS degree at KAIST, 2019-2021 | SK Robotics | Knee Arthrokinematics in Single- and Double-Bundle ACL Reconstructions Assessed by Bi-Planar Fluoroscopy / Shape and pose estimation of a skeleton in X-ray images using statistical shape and intensity model |
| JUHYEOP KIM (김주협) | MS degree, 2024-2026 | Samsung Electronics, MX Division since March 2026 |  |
| HYEYEONG KONG (공혜영) | MS degree, 2023-2026 | Graduate (PhD) student at KAIST since March 2026 |  |
| Seungwoo yoon (윤승우) | Postdoctoral Fellow from September 2024 to August 2025; Obtained PhD degree at KAIST, 2020-2024; Obtained MS degree at KAIST, 2018-2020 | Samsung Electronics Future Robotics Task Force since September 2025 | Optimization of delayed output feedback control algorithms for torque generation in hip-joint wearable robot using forward dynamics human gait simulation / Haptic interface for endoscopy simulation |
| MINSEUNG KIM (김민승) | MS degree, 2023-2025 | Graduate (PhD) student at KAIST since March 2026 | Investigation of frequency response of numerical muscle models |
| DONGWOOK SEO (서동욱) | Research assistant from August 2023 to August 2024 | Misto Footwear (FILA) Sports Science Team |  |
| Young-jun koo (구영준) | Postdoctoral Fellow from April 2020 to March 2023; PhD degree, 2016-2020; MS degree, 2014-2016 | ETRI Government Research Center since July 2023 | Development of physiological knee models and musculoskeletal simulation techniques for gait simulation with virtual knee osteotomy / Quantification of kinematics and skin movements of the knee during treadmill walking |
| AILIAN CHI (지애련) | MS degree, 2020-2023 | Hankook Tire Daejeon R&D Center since 2024 | Performance of lower-extremity exercise-based muscle fatigue and recovery model |
| yooha son (손유하) | MS Degree, 2021-2023 | Samsung Electronics, MX Division since March 2023 | Osteotomy Simulation for Normal Gait Recovery of Flexible Flatfoot Patients and Comparison of Kinematics by Osteotomy techniques |
| mingi jung (정민기) | MS degree, 2020-2022 | Intelligent Robotics Research Center, Korea Electronics Technology Institute (KETI) since August 2022 | Generation of subject-specific motions at various walking speeds using meta reinforcement learning and generative adversarial networks |
| suil jeon (전수일) | MS degree, 2019- 2021 | Graduate (PhD) student at Postech (South Korea) since March 2021 | Anomalous gait feature detection using three-dimensional walking data with dimension reduction |
| cong-bo phan (판콩보) | Postdoctoral Fellow, from March 2019 to June 2020; PhD degree, 2015-2019; MS degree, 2013-2015 | Research Manager, FPT Software, Vietnam | Foot and ankle kinematics during walking using a bi-planar fluoroscopic system / Template-based prediction of anatomical skeletal landmarks and regions for biomechanical applications |
| Guonhui Shin (신건희) | MS degree, 2018 - 2020 | LG Display CTO Group since 2021 | CCTV internal and external parameter estimation using multiple view images for crime scene investigation |
| Jeongwon kIM (김정원) | MS degree, 2018 - 2020 | Samsung Electro-Mechanics since 2020 | Estimation of ankle joint dynamics after flatfoot correction surgery using musculoskeletal simulation |
| yongcheol kim (김용철) | PhD degree, 2014 - 2019; MS degree, 2012 - 2014 | Agency for Defense Development since 2019 | Foot joint kinetics estimation using musculoskeletal dynamics simulation / Development of a musculoskeletal model of the thoracic spine for human dynamics simulation |
| Yihwan Jung (정이환) | PhD degree, 2014 - 2018; MS degree, 2012 - 2014 | Agency for Defense Development since 2018 | Knee kinetics estimation using musculoskeletal simulation / Ground reaction force estimation during walking using human multi-body dynamics simulation |
| Duc-phong Nguyen (웬득펑) | MS degree, 2016 - 2018 | Graduate (PhD) student at University of Technology of Compiègne (France) since March 2019 | Human motion prediction for walking with different weight conditions |
| Jungbin Lee (이중빈) | MS degree, 2016 - 2017 | Graduate (PhD) student at Postech (South Korea) since March 2019 | Three-dimensional human motion estimation with a single camera during walking |
| Duc-manh Ta (타덕만) | PhD at the University of Tennessee at Knoxville (US), 2017 - 2019; MS degree, 2014 - 2016 | JointVue in US | Edge-based Robust 2D Image Registration |
| Yoon Kwak (곽윤) | MS degree, 2014 - 2016 | Agency for Defense Development since 2016 | Estimating mechanical properties of hindfoot plantar tissue using multi-layer hyperelastic model |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지 Journal Papers 목록의 2021–2026년 구역 논문 가운데 19편이다(2026년 4, 2025년 5, 2024년 2, 2023년 4, 2022년 2, 2021년 2). 각 줄은 누리집이 적은 저자, 제목, 학술지·학회, 권·쪽, 연월을 그대로 옮겼고, 목록이 교신저자에 붙인 *도 그대로 두었다. 19편 가운데 18편은 구승범 교수에게 *가 있고, 2025년 구역의 MyoChallenge 2024 벤치마크 논문(NeurIPS Datasets and Benchmarks Track) 1편에는 * 표시가 없다.[^pubs]

**2026**

- Park G, Yoon S, De Groote F, Koo S\*, Spinal Reflexes with Dynamic Gain Modulation Contribute to Robust Walking: A Comparative Study of Simulated Neural Controllers, Journal of NeuroEngineering and Rehabilitation, Early online, September 2026.
- Kim J, Park G, Yang S, Lee G, Koo S\*, Common gait modulation by presence of hip assistance, individual motor strategies by assistance timing, Gait & Posture, Vol. 130:110286, October 2026.
- Yoon S, Lee D, Lee H, Koo S\*, Design and validation of a modified delayed output feedback controller for hip exoskeleton assistance, IEEE Transactions on Neural Systems and Rehabilitation Engineering, Vol. 34:1921-1931, April 2026.
- Oh J, Yoon S, Wang JH, Koo S\*, ISB clinical biomechanics award winner 2025: Residual translational and rotational kinematics after combined anterior cruciate ligament and anterolateral ligament reconstruction during walking – A biplanar fluoroscopy analysis, Clinical Biomechanics, Vol. 137:106870, July 2026.

**2025**

- Han HS, Yang HJ, Ogihara N, Lee T, Koo S\*, Lee DY, Lee KM\*, Evaluation of different hindfoot kinematics according to various shoe types during walking using biplanar fluoroscopy, Journal of Biomechanics, Vol. 191:112914, October 2025.
- Wang C, Tan CK, Hodossy BK, Lyu S, Schumacher P, Heald J, Biegun K, Hromadka S, Sahani M, Park G, Shin B, Park J, Koo S, Zuo C, Ma C, Sui Y, Hansen N, Tao S, Gao Y, Su H, Song S, Gionfrida L, Sartori M, Durandau G, Kumar V, Caggiano V, MyoChallenge 2024: A New Benchmark for Physiological Dexterity and Agility in Bionic Humans, The Thirty-ninth Annual Conference on Neural Information Processing Systems (NeurIPS) Datasets and Benchmarks Track, September 2025.
- Yoon S, Koo S\*, A comparative study of ANN-based forward dynamics and inverse dynamics in human gait analysis, Journal of Biomechanics, Vol. 189:112800, August 2025.
- Boo J, Seo D, Kim M, Koo S\*, Comprehensive human locomotion and electromyography dataset: Gait120, Scientific Data, Vol. 12:1023, June 2025.
- Koo Y, Ogihara N, Koo S\*, Active arm swing during running improves rotational stability of the upper body and metabolic energy efficiency, Annals of Biomedical Engineering, Vol. 53:1003-1013, February 2025.

**2024**

- Oh J, Koo S\*, Fast digitally reconstructed radiograph generation using particle-based statistical shape and intensity model, Journal of Medical Imaging, Vol. 11(3):033503, June 2024.
- Boo J, Koo YJ, Lee JH, Jang WY, Koo S\*, Hindfoot Joint Kinematics Analysis after the Resection of Talocalcaneal Coalition, Gait & Posture, Vol. 111:48-52, June 2024.

**2023**

- Koo Y, Hwangbo J, Koo S\*, Higher coactivations of lower limb muscles increase stability during walking on slippery ground in forward dynamics musculoskeletal simulation, Scientific Reports, Vol. 13, 22808, December 2023.
- Park G, Ryu S, Park SK, Yoon S, Koo S\*, Uncertainties of three-dimensional motion prediction from a single virtual accelerometer during walking and running, IEEE Sensors Journal, Vol. 23(21):26776-26785, November 2023.
- Son Y, Lee KM, Koo S\*, Increase in lateral contact force in the tibiotalar joint during walking in flatfoot patients with reduced stiffness of the spring ligament, Journal of Biomechanics, Vol. 157:111711, August 2023.
- Koo Y, Seon JK, Lee G, Koo S\*, Influences of partial anterior cruciate ligament injury on anterior cruciate ligament tensional force and kinematic stability during walking, Journal of Biomechanical Engineering, Vol. 145(1):011003, January 2023.

**2022**

- Jung M, Koo S\*, Physical factors that differentiate body kinematics between treadmill and overground walking, Frontiers in Bioengineering and Biotechnology, August 2022.
- Jeon S, Lee KM, Koo S\*, Anomalous gait feature classification from 3-D motion capture data, IEEE Journal of Biomedical and Health Informatics, Vol. 26(2):696-703, February 2022.

**2021**

- Phan CB, Lee KM, Kwon SS, Koo S\*, Kinematic instability in the joints of flatfoot subjects during walking: A biplanar fluoroscopic study, Journal of Biomechanics, Vol. 127:110681, October 2021.
- Park G, Lee KM, Koo S\*, Uniqueness of gait kinematics in a cohort study, Scientific Reports, Vol. 11, Article number: 15248, July 2021.

## 소식

누리집 News 페이지의 2021년 10월 13일 이후 항목 가운데 연구·학술 활동 소식 40건이다(2026년 6, 2025년 3, 2024년 13, 2023년 8, 2022년 8, 2021년 2). 날짜와 내용은 페이지 표기 그대로이며, 같은 날짜에 같은 글이 두 번 실린 2건은 한 번만 실었다.[^news]

- 2026.9.29 · Prof. Dimitry Sayenko from the Houston Methodist Research Institute visited KAIST and gave a talk entitled "Electrophysiological Mechanisms and Clinical Effects of Transcutaneous and Epidural Spinal Stimulation for Motor Recovery."
- 2026.8.1 · Our group participated in IEEE BioRob 2026 held in Edmonton, Canada. Jonghyeon Park presented in both a rapid-fire poster presentation session and a regular poster session. Prof. Koo gave an invited talk at a workshop titled "Bridging Human Locomotion Neuromechanics and Assistive Robotics" and joined a panel discussion as a panelist.
- 2026.7.11 · Our group participated in the World Congress of Biomechanics held in Vancouver, Canada. Jeongseok Oh, Gunwoo Park, and Kyubin Chun presented their work in poster sessions. Prof. Koo gave a spotlight talk in the Knee Joint and Osteoarthritis session and co-moderated a session on clinical practice in knee OA.
- 2026.4.23 · Members of our group participated in the KSME Bioengineering 2026 conference, held in Yeosu, South Korea (April 22–24, 2026). Jonghyeon Park and Jeongha Cho contributed with both oral and poster presentations. Notably, Jeongha Cho received a Best Paper Award for his work, with the official award ceremony to be held during the 2027 meeting.  (KSME: Korean Society of Mechanical Engineers)
- 2026.4.23 · Jeongseok Oh was honored with the Best PhD Thesis Award by KSME. This recognition was granted for his doctoral thesis titled "Knee Arthrokinematics in Single- and Double-Bundle ACL Reconstructions Assessed by Bi-Planar Fluoroscopy."
- 2026.4.20 · Members of our group participated in the NCM 2026 conference in Kobe, Japan (April 20–24). Gunwoo Park and Kyubin Chun shared their latest research through poster presentations. (NCM: Neural Control of Movement)
- 2025.07.29 · Our paper titled "Residual Translational and Rotational Kinematics After Combined ACL and Anterolateral Ligament Reconstruction During Walking" (Authors: Jeongseok Oh, Seungwoo Yoon, Joon-Ho Wang, Seungbum Koo) was awarded the Clinical Biomechanics Award at the 30th Congress of the International Society of Biomechanics (ISB) held in Stockholm, Sweden. Jeongseok Oh, the first author, delivered a plenary presentation during the award session.
- 2025.07.11 · Prof. Seungbum Koo gave an invited talk on "Changes in Mechanical Stress Distribution in Injured Knees and Feet" in Seoul National University Hospital Musculoskeletal Research Symposium held in Seoul National University Hospital, Seoul, South Korea.
- 2025.05.21 · Prof. Seungbum Koo received a Certificate of Appreciation from the Korean Society of Mechanical Engineers (KSME) in recognition of his contributions as an Associate Editor in the field of Bio Engineering for the Journal of Mechanical Science and Technology (JMST).
- 2024.12.14 · Our team (MSKBioDyn2024) (Ph.D. candidates Gunwoo Park, Beomsoo Shin, and Jonghyeon Park) participated in the MyoChallenge competition - a competitive event at the Neural Information Processing Systems (NeurIPS) Conference held in December 2024 in Vancouver, Canada-and won first place in the locomotion (walking) challenge among 54 teams from 15 countries. This competition was sponsored by Google DeepMind, Google Cloud, and Össur. As a part of the competition, Gunwoo Park, Jonghyeon Park, and Beomsoo Shin attended the NeurIPS 2024 Conference in Vancouver, Canada, and presented at the Competition Workshop “MyoChallenge 2024: Physiological Dexterity and Agility in Bionic Humans.”
- 2024.11.8 · Our group gave six talks including Prof. Koo's invited talk at the Annual Meeting of Korean Society of Mechanical Engineers held in Jeju ICC, Republic of Korea.
- 2024.09.26 · Prof. Koo received the Outstanding Contribution Award from the Journal of Mechanical Science and Technology for his Associate Editor work for the journal.
- 2024.08.31 · Hyeyeong Kong and Kyubin Chun gave oral presentations in the annual meeting of Korean Society of Biomechanics. Kyubin received best paper award.
- 2024.07.01 · Seungwoo Yoon and Jeongseok Oh presented posters in the annual conference of ESB (European Society of Biomechanics) 2024 held in Edinburgh, UK.
- 2024.05.31 · Invited seminar by Dr. Nathan Netravali on Applying AI+Computational Modeling to Medical Devices Dr. Nathan A. Netravali, Director R+D, Smith and Nephew, Andover, MA, USA
- 2024.04.25 · Jonghyeon Park received Excellent MS Thesis award and Jeongseok Oh and Seungwoo Yoon received Best Paper award in the Spring Conference of KSME Bioengineering, held in Yeosu, Republic of Korea.
- 2024.04.25 · Junyo Boo, Beomsoo Shin and Jonghyeon Park presented in the Spring Conference of KSME Bioengineering, held in Yeosu, Republic of Korea.
- 2024.04.16 · Gunwoo presented poster at 33rd Annual Meeting of Neural Control of Movement held in Dubrovnik, Croatia.
- 2024.03.27 · Prof. Seungbum Koo received Outstanding Contribution Award for his contribution to the Journal of Mechanical Science and Technology (JMST) as an Associate Editor.
- 2024.02.15 · Invited seminar by Dr. Valentina Camomilla on Soft tissue artifacts in human movement analysis : anatomy of an enemy Dr. Valentina Camomilla, Associate Professor of Biomechanics, University of Rome Foro Italico, Rome, Italy
- 2024.02.04 · Junyo Boo and Beomsoo Shin presented posters in the Annual Conference of Orthopaedic Research Society (ORS), held in Long Beach, CA, USA.
- 2024.02.03 · Prof. Koo moderated a session "Modeling, Diagnosis, and Treatment of Collapsing Foot Deformity" in the Annual Conference of Orthopaedic Research Society (ORS), held in Long Beach, CA, USA.
- 2023.12.16 · We took the 2nd place in locomotion track in NeurIPS 2023 MyoChallenge Competition.
- 2023.12.01 · We had two oral presentations in the KSB and KSSB joint conference. Jeongseok Oh, Seungbum Koo, Analysis of accuracy of 2D-3D registration of knee using mobile bi-planar fluoroscopy device Junyo Boo, Seungbum Koo, Estimating quantified foot joint kinematics in virtual injury scenarios using dynamics simulation
- 2023.11.15 · We joined AP-Biomech 2023 held in Kuala Lumpur, Malaysia. We had one oral presentation and Prof. Koo moderated two keynote sessions. Seungwoo Yoon, Seungbum Koo, Analysis of Delayed Output Feedback Control Parameters Using Forward Dynamics Skeletal Simulation
- 2023.11.02 · We joined KSME 2023 Conference held in Songdo, South Korea. We had three oral presentations.
- 2023.10.01 · We presented a simulation of soft suit with shape-memory-alloy actuators to assist walking along with a hardware prototype from KIMM in Robot World 2023, Kintex, South Korea.
- 2023.08.01 · We had two oral presentations and two posters in the ISB meeting held in Fukuoka, Japan from July 30th to August 3rd.
- 2023.07.28 · Prof. Seungbum Koo delivered a keynote lecture at the ISB TGCS (Technical Group on Computer Simulation) Conference held in Kyoto, Japan, July 26-28, 2023. The title of the lecture was "Forward dynamics gait simulation of musculoskeletal human model using reinforcement learning." The ISB TGCS is a biennial conference focused on computer simulation in biomechanics, especially human movement, motor control, and robotics related to biomechanics. The 19th conference featured two keynote lectures, with Professor Seungbum Koo discussing the reinforcement learning-based human motion controllers in musculoskeletal dynamics simulations and their research applications such as muscle activation patterns and assistive device co-simulation.
- 2023.04.23 · We received two awards in the spring meeting of KSME Bioengineering. Ailian Chi (Master student) received best paper award. Gunwoo Park (PhD student) received Excellent Thesis Award for his master's thesis.
- 2022.12.20 · Prof. Koo is invited as a keynote speaker at ISB TGCS 2023.
- 2022.11.24 · Prof. Mark Latash visited KAIST and gave a talk on "Mechanisms of intentional and unintentional movements."
- 2022.11.11 · Yooha Son (Master student) received best paper award in the 2022 Annual conference of Korean Society of Mechanical Engineers held in Jejudo, South Korea.
- 2022.07.14 · Prof. Seungbum Koo gave an invited talk "Seeing the unseen movements of the foot using bi-plane fluoroscopic imaging" in the Foot and Ankle session at the 2022 World Congress of Biomechanics held in Taipei, Taiwan.
- 2022.07.14 · We presented four talks (Young-Jun Koo, Seungwoo Yoon, Jeongseok Oh, Ailian Chi) and one poster (Mingi Jeong) in the 2022 World Congress of Biomechanics held in Taipei, Taiwan.
- 2022.04.22 · Young-Jun Koo, PhD (Postdoctoral Fellow) and Yooha Son (Master student) received best paper award in the Spring Conference of Bioengineering Division of Korean Society of Mechanical Engineers held in Taean, South Korea.
- 2022.03.22 · Prof. Koo gave an online invited talk on "Training a walking controller for human musculoskeletal simulation using the deep reinforcement learning" in Toyo University, Tokyo, Japan.
- 2022.02.18 · Prof. Koo gave an online invited talk on "Deep reinforcement learning to create a gait controller of a musculoskeletal human model" in Biomechanics, Aalborg University, Aalborg, Denmark.
- 2021.11.12 · Invited seminar by Dr. Anna-Maria Liphardt on Space flight research for a better understanding of the role of mechanical loading for cartilage health Dr. Anna-Maria Liphardt, Rheumatology & Immunology, University Hospital Erlangen & Friedrich-Alexander-University Erlangen-Nürnberg, Erlangen, Germany
- 2021.10.16 · Prof. Koo and his colleagues received a poster presentation award in the 65th Annual Congress of the Korean Orthopaedic Association for the study on ankle stress X-ray examination to quantify ligament instability after ankle fracture treatment.

## 연락과 위치

- 주소: (34141) 대전광역시 유성구 대학로 291 한국과학기술원(KAIST) 기계공학과 N7-3동 5206호[^contact]
- 전화: 042-350-3241[^contact][^mep]
- 교수 이메일: skoo@kaist.ac.kr[^mep]
[^p1]: J. Boo, D. Seo, M. Kim, S. Koo, Scientific Data 12, 1023 (온라인 2025-06-18). <https://doi.org/10.1038/s41597-025-05391-0> 초록 기준.
[^p2]: J. Oh, S. Yoon, J. H. Wang, S. Koo, Clinical Biomechanics 137, 106870 (2026). <https://doi.org/10.1016/j.clinbiomech.2026.106870> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: Y.-J. Koo, J. K. Seon, G. Lee, S. Koo, Journal of Biomechanical Engineering 145, 011003 (온라인 2022-08-19). <https://doi.org/10.1115/1.4054982> 초록 기준.
[^p4]: Y. Son, K. M. Lee, S. Koo, Journal of Biomechanics 157, 111711 (2023). <https://doi.org/10.1016/j.jbiomech.2023.111711> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: G. Park, S. Yoon, F. De Groote, S. Koo, Journal of NeuroEngineering and Rehabilitation (온라인 2026-09-22). <https://doi.org/10.1186/s12984-026-02157-6> 초록 기준.
[^p6]: Y.-J. Koo, N. Ogihara, S. Koo, Annals of Biomedical Engineering 53, 1003-1013 (온라인 2025-02-03). <https://doi.org/10.1007/s10439-025-03688-0> 초록 기준.
[^p7]: J. Kim 외, S. Koo, Gait & Posture 130, 110286 (2026). <https://doi.org/10.1016/j.gaitpost.2026.110286> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: S. Yoon, D. Lee, H.-J. Lee, S. Koo, IEEE Transactions on Neural Systems and Rehabilitation Engineering 34, 1921-1931 (2026). <https://doi.org/10.1109/tnsre.2026.3682054> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 근골격 운동역학 연구실 누리집 첫 화면 <https://mskbiodyn.kaist.ac.kr/> (연구실 목표, Research Vision and Mission, 2026-10-23 열람)
[^contact]: 근골격 운동역학 연구실 누리집 Contacts 페이지 <https://mskbiodyn.kaist.ac.kr/home/contacts> (주소, 전화, 2026-10-23 열람)
[^prof]: 근골격 운동역학 연구실 누리집 Professor 페이지 <https://mskbiodyn.kaist.ac.kr/members/professor> (Education, Professional Experience, Professional Services, Awards, 2026-10-23 열람)
[^members]: 근골격 운동역학 연구실 누리집 Members 페이지 <https://mskbiodyn.kaist.ac.kr/members> (2026-10-23 열람)
[^alumni]: 근골격 운동역학 연구실 누리집 Alumni 페이지 <https://mskbiodyn.kaist.ac.kr/members/alumni> (2026-10-23 열람)
[^ma]: 근골격 운동역학 연구실 누리집 Research: Precision Motion Analysis 페이지 <https://mskbiodyn.kaist.ac.kr/research/motion-analysis> (2026-10-23 열람)
[^mm]: 근골격 운동역학 연구실 누리집 Research: Computing the Forces Inside Our Joints 페이지 <https://mskbiodyn.kaist.ac.kr/research/musculoskeletal-modeling> (2026-10-23 열람)
[^nc]: 근골격 운동역학 연구실 누리집 Research: Teaching Virtual Humans to Walk 페이지 <https://mskbiodyn.kaist.ac.kr/research/neuromuscular-control-ai> (2026-10-23 열람)
[^ad]: 근골격 운동역학 연구실 누리집 Research: Making Assistive Devices Work for the Body 페이지 <https://mskbiodyn.kaist.ac.kr/research/assistive-devices> (2026-10-23 열람)
[^eq]: 근골격 운동역학 연구실 누리집 Equipment 페이지 <https://mskbiodyn.kaist.ac.kr/research/equipment> (2026-10-23 열람)
[^pubs]: 근골격 운동역학 연구실 누리집 Publications 페이지 <https://mskbiodyn.kaist.ac.kr/publications> (Journal Papers, 목록 범위는 근거 페이지, 2026-10-23 열람)
[^news]: 근골격 운동역학 연구실 누리집 News 페이지 <https://mskbiodyn.kaist.ac.kr/news> (2026-10-23 열람)
[^classes]: 근골격 운동역학 연구실 누리집 Classes 페이지: Undergraduate <https://mskbiodyn.kaist.ac.kr/classes/undergraduate>, Graduate <https://mskbiodyn.kaist.ac.kr/classes/graduate> (2026-10-23 열람)
[^mep]: KAIST 기계공학과 교수 소개(구승범) <https://me.kaist.ac.kr/pop/team.html?uid=3&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 이메일, 위치, 전화, 2026-10-23 열람)
[^mel]: KAIST 기계공학과 교수진 목록 <https://me.kaist.ac.kr/team/team_010100.html> (구승범 교수 항목, 2026-10-23 열람)
[^mer1]: KAIST 기계공학과 연구분야 로보틱스/제어/모빌리티 페이지 <https://me.kaist.ac.kr/research/research_010100.html> (구승범 교수의 연구주제·주요 응용 산업·연구실 항목, 2026-10-23 열람)
[^mer4]: KAIST 기계공학과 연구분야 헬스케어/나노/광학 페이지 <https://me.kaist.ac.kr/research/research_010400.html> (구승범 교수의 연구주제·연구실 항목, 2026-10-23 열람)

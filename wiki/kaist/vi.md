# 시각 지능 연구실 (Visual Intelligence Lab, VILab)

**KAIST 기계공학과 · 윤국진 교수**

- 분야: 자율주행을 위한 종단간 주행과 경로 예측·계획, 이벤트 카메라·360도 카메라 같은 새로운 센서의 영상 인식, LiDAR·4D 레이더·카메라를 묶는 3차원 인지와 장면 복원, 생성 모델과 비전-언어 모델, 적은 라벨로 배우는 영상 분할과 영상 복원
- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 컴퓨터 비전[^home][^faculty], 자율주행[^home][^research][^p1], 3차원 복원·인식[^home][^research][^p6], 멀티모달 AI[^research][^faculty][^p5], 생성 인공지능[^home][^research]
- 홈페이지: <https://vi.kaist.ac.kr/>
- 근거와 출처: [시각 지능 연구실 근거 페이지](vi-sources.md)

> 사진과 영상, 여러 센서 자료를 컴퓨터가 알아보고 3차원 세계를 이해하게 하는 컴퓨터 비전 연구실이다. 핵심 연구 분야로 종단간 자율주행, 생성 AI와 멀티모달 언어 모델, 이벤트 카메라 기반 비전, 3차원 장면 복원과 이해를 든다. 누리집 논문 목록의 2021–2026년 구역에는 CVPR·ECCV·ICCV·NeurIPS 같은 컴퓨터 비전·기계학습 학회 논문을 중심으로 146편이 있다.[^home][^pubs]

## 무엇을 연구하나

시각 지능 연구실(Visual Intelligence Lab, VILab)은 KAIST 기계공학과 윤국진 교수가 이끄는 연구실이다.[^home][^me] 누리집 첫 화면은 연구실이 컴퓨터 비전(computer vision, 컴퓨터가 사진·영상을 알아보고 해석하게 하는 분야), 로보틱스, 기계학습을 연구하며, 복잡한 실제 세계를 이해하고 재구성하며 그 세계와 상호작용하는 지능 시스템을 만드는 것을 목표로 한다고 소개한다. 핵심 연구 분야로는 종단간 자율주행(End-to-End Autonomous Driving), 생성 AI와 멀티모달 언어 모델(Generative AI & Multi-modal Language Models), 이벤트 기반 비전(Event-based Vision), 3차원 장면 복원과 이해(3D Scene Reconstruction & Understanding)의 네 가지를 든다.[^home]

Faculty 페이지의 교수 소개 글은 연구실이 시각 신호와 여러 종류의 신호로 기계가 실제 세계를 지각하고 이해하고 그 세계와 상호작용하는 방법을 연구한다고 적는다. 연구의 중심은 컴퓨터 비전이고, 현재 관심 분야로 종단간 자율주행, 생성 AI와 멀티모달 언어 모델, 비전-언어-행동 모델(VLA, vision-language-action, 영상과 말로 된 지시를 함께 받아 로봇 등이 할 행동을 내놓는 모델), 이벤트 기반 비전, 3차원 장면 복원과 이해를 든다.[^faculty]

Research 페이지는 연구 분야를 12개로 나눠 소개한다. 종단간 자율주행, 비전 기반 모델(Foundation Model for Vision), 비전 생성 모델(Generative Models for Vision), 새로운 센서(이벤트 카메라, 360도 카메라), 멀티모달 학습(여러 센서의 결합, 영상과 언어의 결합), 3차원 비전(새 시점 합성, 3차원 장면 이해), 경로 예측과 계획(Trajectory Prediction / Planning), 자세 추정(사람 동작 예측, 6D 자세 추정), 3차원 인지(3D LiDAR 의미 분할, 3차원 물체 검출), 2차원 인지(물체 추적, 광류, 약지도 의미 분할), 비전을 위한 기계학습(다중 작업 학습, 적대적 공격, 테스트 시점 적응), 저수준 비전(악천후 제거, 프레임 보간, 초해상도, 모션 디블러링)이다.[^research]

기계공학과 교수 소개는 교수의 연구분야를 Computer Vision, Machine Learning, Pattern Analysis로 적는다.[^mepop] 기계공학과 연구분야 페이지는 교수를 로보틱스/제어/모빌리티 분야의 핵심교수로 싣고, 연구주제로 자율주행을 위한 영상 기반 첨단 운전자 보조 시스템(Vision-based ADAS), 영상으로부터의 3차원 복원, 여러 표적의 검출과 추적, 시각 주행 거리 측정(visual odometry)과 광류 추정을 든다.[^mer1]

누리집 Publications 목록의 2021–2026년 구역에는 논문 146편이 있다. 그 가운데 학회 논문이 113편이며, CVPR 35편, ECCV 30편, ICCV 20편, NeurIPS 7편이 많다.[^pubs]

## 주요 연구 주제

### 1. 자율주행: 종단간 주행과 경로 예측·계획

Research 페이지는 종단간 자율주행을 센서의 원래 입력에서 주행 동작까지를 하나의 신경망이나 처리 흐름으로 곧바로 배우는 방식으로 설명한다. 인지, 예측, 계획을 한 모델로 묶어 시스템을 단순하게 하고 일관된 실시간 판단을 할 수 있게 한다고 적는다.[^research] 경로 예측은 차량과 보행자 같은 움직이는 대상의 앞으로의 움직임을 추정하는 일이고, 계획은 그 정보로 자율 로봇이나 차량의 안전하고 효율적인 움직임을 정하는 일이라고 설명한다.[^research]

대표 논문으로는 카메라 시점 변화에 강건한 종단간 자율주행 틀(NeurIPS 2025, 대표 논문 1)과, 여러 주행 궤적 데이터셋에서 따로 훈련한 모델들의 매개변수를 하나로 합쳐(모델 병합) 새 환경의 움직임 계획에 쓰는 방법(ICCV 2025, 대표 논문 2)이 있다.[^p1][^p2] 논문 목록에는 궤적으로 이끄는 월드 모델(world model)을 쓴 종단간 자율주행 HEAT(IEEE Robotics and Automation Letters, 2026, 게재 승인), 의사 시뮬레이션으로 차량과 도로 기반 시설의 협력 계획을 평가하는 벤치마크 VIPS(ECCV 2026), 충돌을 고려해 매개변수를 나눠 훈련하는 방식으로 예측과 계획을 하나로 묶는 연구(ECCV 2026), 확산 모델 기반 움직임 계획의 보상 최적화(IROS 2025), 경로 예측의 테스트 시점 훈련 T4P(CVPR 2024), 미래 관계 추론을 쓴 차량 경로 예측(ICLR 2023), 3차원 차선 검출(ECCV 2026)도 있다.[^pubs]

Projects 페이지는 교수가 PI로 적힌 과제로 멀티모달 센서 기반의 스스로 개선하는 자율주행 연구(한국연구재단, 2026–2029), 강건한 자율주행을 위한 자료 증강과 센서 융합 기술 개발(42dot, 2024–2026), 비정형 비포장 환경의 자율주행 핵심 기술 개발(Hanwha Aerospace, 2023–2026)을 싣는다.[^projects]

### 2. 이벤트 카메라와 360도 카메라 (Novel Sensor)

Research 페이지는 새로운 센서가 일반 RGB 카메라로 얻지 못하는 시각 정보를 주어 어려운 조건에서도 인지할 수 있게 한다고 소개한다. 이벤트 카메라(event camera)는 밝기 변화를 비동기적으로(asynchronously) 마이크로초 단위의 지연으로 기록해 움직임 번짐을 피하고 극단적인 조명에서도 쓸 수 있으며, 빠른 움직임 분석, 넓은 밝기 범위 영상(HDR), 끊김 없는 시간의 인지에 알맞다고 적는다.[^research] 360도 카메라는 한 시점에서 주변 전체를 찍어 자율주행과 로보틱스의 상황 인식을 돕는다고 설명한다.[^research]

대표 논문으로는 이벤트 카메라 두 대의 자료를 시간에 걸쳐 모아 거리를 재는 스테레오 정합(IEEE TPAMI 2026, 대표 논문 3), 이벤트 카메라를 3차원 물체 검출에 들여와 프레임 사이 구간에도 물체를 찾는 방법(CVPR 2025, 대표 논문 4), 360도 영상을 원하는 투영 방식의 고해상도 영상으로 키우는 초해상도(CVPR 2022, 대표 논문 8)가 있다.[^p3][^p4][^p8] 논문 목록에는 이벤트 기반 새 물체의 6D 자세 추적(CVPR 2026), 이벤트 기반 특징점 추적의 시간 집계를 강화학습으로 조절하는 연구(ECCV 2026), 짝지어지지 않은 자료로 하는 이벤트 기반 모션 디블러링(CVPR 2026), 이벤트 기반 전방위 다시점 스테레오 EOMVS(IEEE Robotics and Automation Letters, 2021), 노출 시간을 모르는 영상의 이벤트 기반 디블러링(ECCV 2022), 이벤트 카메라 자료로 이끄는 극한 조건의 사람 자세 추정·추적 벤치마크 데이터셋(NeurIPS 2024), 실내 파노라마 합성(ECCV 2022)도 있다.[^pubs] Projects 페이지에는 교수가 PI인 이벤트 카메라 기반 컴퓨터 비전 알고리즘 연구(한국연구재단, 2018–2022)와 이벤트 카메라의 3차원 특징점 추적 알고리즘 과제(KAIST, 2025)가 있다.[^projects]

### 3. 여러 센서와 언어를 함께 쓰는 멀티모달 학습 (Multi-Modal Learning)

Research 페이지는 멀티모달 학습이 종류가 다른 센서의 서로 보완하는 정보를 묶어 더 믿을 만하고 완전한 인지를 얻는다고 소개한다. LiDAR, 레이더(RADAR), 카메라를 함께 쓰면 각각의 장점인 기하, 움직임, 강건함, 질감을 살릴 수 있어 악천후나 시야가 나쁜 상황에서 3차원 인지가 좋아진다고 적는다. 비전-언어 모델(vision-language model, 영상과 글을 함께 배워 영상 내용을 말로 다루는 모델)은 영상과 글의 공동 표현을 배워 높은 수준의 의미 이해를 준다고 설명한다.[^research]

대표 논문 5(CVPR 2024)는 날씨에 둔감한 4D 레이더와 LiDAR를 센서 특성과 날씨 조건에 맞춰 합치는 3차원 물체 검출 방법이다.[^p5] 논문 목록에는 움직이는 물체에 반사된 전파의 주파수 변화로 얻는 속도 정보(도플러 정보)를 고려한 LiDAR·레이더 융합(ICCV 2025), 악천후에서 카메라·LiDAR·4D 레이더의 신뢰도를 고려한 융합(ECCV 2026), 4D 레이더 정보를 모델의 입력 단서(프롬프트)로 주고 그 지식을 LiDAR 모델로 옮기는(지식 증류) LiDAR 기반 전천후 3차원 물체 검출(ECCV 2024), 스테레오 이벤트·RGB·열화상 카메라와 4D 레이더, 두 대의 LiDAR로 여러 주행 조건에서 강건한 멀티모달 인지를 다룬 DSERT-RoLL(CVPR 2026)이 있다.[^pubs] 영상과 언어 쪽으로는 3차원을 인식하는 대형 언어 모델로 1인칭 시점의 사람 동작을 예측하는 연구(ECCV 2026), 예측 불확실성으로 범용 추론을 일으키는 이중 시스템 비전-언어-행동 모델(NeurIPS 2026, 채택), 영상과 글을 짝지은 데이터의 학습 정보를 합성 표본에 압축해 학습에 쓰는 비전-언어 데이터셋 증류(CVPR 2026, ECCV 2026)가 있다.[^pubs]

### 4. 3차원 비전: 장면 복원, 새 시점 합성, 3차원 인지

Research 페이지는 3차원 비전이 물체와 장면의 3차원 구조를 이해하고 재구성하는 분야이며, 새 시점 합성(novel view synthesis)은 적은 수의 입력 영상만으로 찍지 않은 시점의 장면을 그려 내는 일이라고 설명한다. NeRF(신경 방사장)와 3D Gaussian Splatting 같은 기법이 연속된 3차원 표현을 배워 실감 나는 렌더링을 한다고 적는다.[^research] 3차원 인지에서는 LiDAR 점구름의 점마다 의미 라벨을 붙이는 3D LiDAR 의미 분할과, 3차원 공간에서 물체를 찾아 분류하는 3차원 물체 검출을 다룬다.[^research] 자세 추정은 사람이나 물체의 공간 배치를 알아내는 일로, 6D 자세 추정은 물체의 3차원 위치와 방향을 함께 정한다고 설명한다.[^research]

대표 논문 6(CVPR 2023)은 방사장 최적화와 영상 초해상도가 서로를 이끌도록 함께 최적화해 고해상도 새 시점 합성 성능을 높인 연구다.[^p6] 논문 목록에는 기하에 바탕을 둔 영상 확산 모델로 하는 새 시점 합성 GeoNVS(ECCV 2026), 방해물이 없는 3D Gaussian Splatting을 위한 PriSplat(ECCV 2026), 열화의 종류와 상관없이 쓰는 피드포워드 Gaussian Splatting ReSplat(ICLR 2026), 단일 원천 영역 일반화를 위한 LiDAR 의미 분할 표현 학습(IEEE TPAMI, 2026), 손상된 LiDAR 자료의 의미 분할 테스트 시점 훈련(CVPR 2026), 모델 없이 새 물체의 6D 자세를 추정하는 Any6D(CVPR 2025), 머리 전체 복원을 위한 4차원 머리 지도(ICCV 2025)가 있다.[^pubs]

### 5. 적은 라벨로 배우는 영상 분할과 비전을 위한 기계학습

Research 페이지는 약지도 의미 분할(WSSS)을 태그, 점, 상자 같은 약한 라벨로 픽셀 단위 분할을 만들어 내는 일로 설명하고, 라벨을 다는 비용을 크게 줄이면서 큰 규모의 훈련을 할 수 있게 한다고 적는다.[^research] 비전을 위한 기계학습에서는 모델이 배우고 적응하고 일반화하는 방식을 개선하는 일을 다루며, 여러 작업을 한 모델로 함께 배우는 다중 작업 학습, 사람이 알아채기 어려운 작은 교란으로 모델을 속이는 적대적 공격, 라벨 없이 처음 보는 환경에 맞춰 모델을 그때그때 고치는 테스트 시점 적응을 든다.[^research]

대표 논문 7(CVPR 2024)은 분할용 기반 모델 SAM의 지식을 훈련 중에 분류기로 옮겨 약지도 의미 분할의 초기 단서를 개선한 연구다.[^p7] 논문 목록에는 서로 다른 종류의 라벨을 함께 쓰는 약지도 인스턴스 분할 WISH(CVPR 2025), 확산 모델로 이끄는 약지도 의미 분할(ECCV 2024), 다중 작업 최적화에서 작업 우선순위를 수치로 나타내는 연구(CVPR 2024)와 작업 그룹을 골라 갱신하는 연구(ICLR 2025), 다른 모델에도 통하는(transferable) 적대적 공격을 위한 프롬프트 기반 대조 학습(ECCV 2024), 대화형 분할의 테스트 시점 적응(ICCV 2025)이 있다.[^pubs]

### 6. 영상 복원과 생성 모델

Research 페이지는 저수준 비전이 기본적인 영상 신호를 복원하거나 개선하거나 분석해 뒤따르는 인지 모델의 신뢰성을 돕는 분야라고 설명하고, 비, 안개, 눈, 연무로 떨어진 화질을 되살리는 악천후 제거, 영상 프레임 사이에 중간 프레임을 만드는 프레임 보간, 저해상도 영상에서 고해상도 영상을 만드는 초해상도, 움직임으로 번진 영상을 선명하게 되살리는 모션 디블러링을 든다.[^research] 비전 생성 모델은 자료의 분포를 모형으로 배워 실감 나는 영상, 동영상, 장면을 합성하며, 비전 기반 모델은 많고 다양한 자료로 훈련해 적은 감독으로도 여러 시각 작업에 적응하는 큰 모델이라고 설명한다.[^research]

논문 목록에는 스펙트럼 기반 공간 묶기로 하는 악천후 제거(ICCV 2025), 저조도 영상 개선·프레임 보간·디블러링을 한 틀로 다루는 이벤트 기반 방법(ICCV 2025), 추가 매개변수 없이 고정된 확산 모델로 글 지시를 따르는 제로샷 주행 장면 생성과 자료 증강 FrozenDrive(ECCV 2026), 극단적인 자세 추정(Extreme Pose Estimation)을 위해 영상 생성 모델을 강화하는 ExPose(CVPR 2026)가 있다.[^pubs] Projects 페이지에는 생성 AI 기반 16비트 HDR 솔루션 개발(Samsung Electronics, 2025–2026)과 기록 영상 콘텐츠 활용을 위한 아웃페인팅(outpainting, 영상의 바깥 영역을 이어 그리는 기술) AI와 공간 확장 기술 개발(2026–2028)이 있다.[^projects]

### 7. 다른 연구실과 함께한 연구

논문 목록에는 가스 센서와 딥러닝을 묶어 가스의 종류를 가려내는 공동 연구 논문이 여럿 있다. 배치가 고른 가스 센서 배열과 딥러닝으로 하는 실시간 다중 가스 판별(ACS Sensors, 2022), 여러 마이크로 LED를 넣은 나노 구조 가스 센서와 딥러닝에 바탕을 둔 초저전력 전자 코 시스템(ACS Nano, 2023), 저전력 가스 센서와 오보닉 문턱 스위치를 쓴 뉴로모픽 후각(Science Advances, 2025, 게재 승인) 등이다.[^pubs] 같은 목록에는 가스 센서로 가스 종류를 실시간 판별하는 장치와 가변 광조사로 가스 종을 식별하는 방법의 특허도 있다.[^pubs] 그 밖에 제로샷 컴퓨터 비전 틀로 여러 규모의 응축 현상을 분석한 연구(Advanced Science, 2026, 게재 승인)와, 환경 조건에 따라 달라지는 단백질 상 분리를 예측하고 조절하는 기계학습 틀(Nature Communications, 2026)도 있다.[^pubs]

## 대표 논문

누리집 Publications 목록의 2021–2026년 논문 가운데 윤국진 교수가 마지막 저자인 논문에서, 첫 화면과 Research 페이지의 연구 분야에 고르게 여덟 편을 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2025 | [VR-Drive: Viewpoint-Robust End-to-End Driving with Feed-Forward 3D Gaussian Splatting](https://doi.org/10.52202/085713-3828) · NeurIPS 2025 | 종단간 자율주행(E2E-AD)은 인지, 예측, 계획을 데이터로 배우는 하나의 틀로 묶는 방식이지만, 차량마다 카메라 배치가 달라 생기는 시점 변화에 강건하게 만드는 일은 아직 풀리지 않은 문제다. 연구진은 3차원 장면 복원을 보조 과제로 함께 배워, 주행 계획에 맞춘 새 시점 영상을 합성하는 종단간 자율주행 틀 VR-Drive를 제안했다. 장면마다 따로 합성하던 이전 방식과 달리 한 번의 계산으로 결과를 내는(feed-forward) 방식이라, 추가 라벨 없이 적은 시점의 영상으로 훈련 중에 바로 자료를 늘릴 수 있다. 여러 시점의 정보를 시간에 걸쳐 주고받게 하는 시점 혼합 메모리 뱅크와, 원래 시점의 지식을 합성한 시점으로 옮기는 증류 방법도 더했다. 시점이 바뀐 상황에서 합성으로 생긴 잡음을 줄이고 계획 성능을 높였으며, 새 카메라 시점에서 종단간 자율주행 성능을 평가하는 벤치마크 데이터셋도 공개했다.[^p1] | 1저자 H. Cho(Hoonhee Cho), 마지막 저자 윤국진 (7명). 누리집 목록은 앞의 네 저자 이름 뒤에 *를 붙인다. |
| 2 | 2025 | [Interaction-Merged Motion Planning: Effectively Leveraging Diverse Motion Datasets for Robust Planning](https://doi.org/10.1109/iccv51701.2025.02657) · ICCV 2025 (Highlight) | 움직임 계획(motion planning)은 자율 주행 로봇의 핵심 부분이다. 여러 주행 궤적 데이터셋이 있지만, 차량·보행자 같은 행위자 사이의 상호작용과 환경 특성이 달라 목표 영역에 효과적으로 쓰기 어렵다. 도메인 적응이나 앙상블 학습 같은 기존 방법은 여러 원천 데이터셋을 쓰지만 영역 사이의 불균형, 앞서 배운 것을 잊는 문제(catastrophic forgetting), 높은 계산 비용을 겪는다. 연구진은 서로 다른 영역에서 훈련한 모델 매개변수 체크포인트를 목표 영역 적응에 쓰는 IMMP를 제안했다. 먼저 원천 영역에서 행위자의 행동과 상호작용을 담아 다양한 정보를 뽑는 사전 병합을 하고, 이어서 병합으로 목표 영역에 적응할 수 있는 모델을 만들어 다양한 상호작용을 효율적으로 옮긴다. 여러 계획 벤치마크와 모델에서 기존 방법보다 좋은 성능을 보였다.[^p2] | 1저자 G. Lee(Giwon Lee), 마지막 저자 윤국진 (5명). 누리집 목록은 앞의 두 저자 이름 뒤에 *를 붙인다. |
| 3 | 2026 | [Temporal Stereo Matching from Event Cameras via Joint Learning with Stereoscopic Flow](https://doi.org/10.1109/tpami.2025.3645734) · IEEE TPAMI | 이벤트 카메라는 생물의 망막에서 착안한 동적 시각 센서로, 밝기 범위가 넓고 시간 해상도가 높으며 전력 소모가 적어 극한 조건에서도 3차원 환경을 지각할 수 있다. 이벤트 자료는 시간에 따라 끊임없이 기록되어 픽셀의 움직임을 자세히 담는다. 연구진은 이 시간적 밀도를 살려 과거 정보를 계속 이어 쓰는 시간적 이벤트 스테레오 틀을 내놓았다. 스테레오 정합(두 카메라 영상의 같은 점을 짝지어 거리를 구하는 일) 신경망을, 두 카메라에서 픽셀의 움직임을 추적하는 입체 흐름(stereoscopic flow)과 함께 훈련하며, 광류의 정답 자료 대신 시차 지도로 움직임 흐름을 학습한다. 입체 흐름으로 정보를 시간에 걸쳐 모아 스테레오 정합 성능을 높였고, 논문은 MVSEC, DSEC, M3ED, EVIMO2 데이터셋에서 최고 수준(state-of-the-art)의 결과를 얻었다고 적는다. 과거 자료를 단계적으로 쌓는 방식이라 계산 효율도 높다.[^p3] | 1저자 J.-Y. Kang(Jae-Young Kang), 마지막 저자 윤국진 (3명). 누리집 목록은 앞의 두 저자 이름 뒤에 *를 붙인다. |
| 4 | 2025 | [Ev-3DOD: Pushing the Temporal Boundaries of 3D Object Detection with Event Cameras](https://doi.org/10.1109/cvpr52734.2025.02533) · CVPR 2025 (Highlight) | 점구름(point cloud)에서 3차원 물체를 찾는 일은 자율주행 시스템에 중요하며, 안전하려면 정확도뿐 아니라 속도와 낮은 지연이 필요하다. 하지만 LiDAR와 카메라처럼 정해진 프레임 속도로 찍는 센서는 지연과 대역폭에 한계가 있어 기존 알고리즘이 이 요구를 맞추지 못한다. 논문은 비동기식 이벤트 카메라를 3차원 물체 검출에 처음 들여왔다고 적는다. 이벤트 카메라의 높은 시간 해상도와 낮은 대역폭으로 빠른 3차원 검출을 하며, 동기화된 자료가 없는 프레임 사이 구간에도 이벤트 카메라로 이전 3차원 정보를 불러와 물체를 찾는다. 3차원 경계 상자 정답을 100 FPS로 담은 이벤트 기반 3차원 검출 데이터셋 Ev-Waymo와 DSEC-3DOD도 만들어 이 분야의 첫 벤치마크로 내놓았다.[^p4] | 1저자 H. Cho(Hoonhee Cho), 마지막 저자 윤국진 (4명). 누리집 목록은 앞의 두 저자 이름 뒤에 *를 붙인다. |
| 5 | 2024 | [Towards Robust 3D Object Detection with LiDAR and 4D Radar Fusion in Various Weather Conditions](https://doi.org/10.1109/cvpr52733.2024.01436) · CVPR 2024 | 정상 날씨와 악천후를 아우르는 여러 날씨에서 3차원 물체를 찾는 일은 안전한 자율주행에 꼭 필요하다. 최근 연구는 날씨에 둔감한 4D 레이더를 LiDAR 같은 다른 센서와 함께 쓰지만, 센서 특성과 날씨 조건을 고려하지 않고 정보를 합치며 물체 위치를 찾는 데 쓸모 있는 높이 정보 일부를 잃는다. 연구진은 LiDAR의 정밀한 3차원 지도화와 4D 레이더의 넓은 범위·날씨에 둔감한 측정이라는 서로 다른 3차원 공간 패턴을 고려해, 3차원 공간 관계에 따라 융합 특징을 뽑는 3D-LRF 모듈을 제안했다. 이어서 날씨 조건에 따라 융합 특징의 정보 흐름을 조절하는 게이트 신경망으로 두 센서의 장점을 함께 살린 특징을 얻는다. 논문은 여러 날씨 조건의 3차원 물체 검출에서 최고 수준(SoTA)의 성능을 냈다고 적는다.[^p5] | 1저자 Y. Chae(Yujeong Chae), 마지막 저자 윤국진 (3명) |
| 6 | 2023 | [Cross-Guided Optimization of Radiance Fields with Multi-View Image Super-Resolution for High-Resolution Novel View Synthesis](https://doi.org/10.1109/cvpr52729.2023.01196) · CVPR 2023 | 새 시점 합성은 여러 시점의 영상과 카메라 자세로 임의 시점의 영상을 만들어 내는 일이다. NeRF(신경 방사장)는 연속된 부피 표현을 배워 임의 해상도로 새 시점을 합성할 수 있지만, 좌표를 입력받는 신경망의 주파수 특성에 크게 기대어 고해상도 새 시점 합성 성능을 높이는 데 한계가 있다. 연구진은 단일 영상 초해상도와 방사장 최적화가 서로를 이끌도록 함께 최적화하는 틀을 제안했다. 방사장을 최적화하는 동안 훈련 시점 영상들에 다중 시점 초해상도를 하고, 단일 영상 초해상도로 얻은 특징 지도와 훈련 시점 영상들의 오차를 모아 만든 복셀 단위 불확실성 장을 합쳐 초해상도 결과를 갱신한다. 이 갱신을 되풀이하면 훈련 시점 영상이 여러 시점 사이의 일관성과 세밀한 고주파 정보를 함께 갖게 되어 고해상도 새 시점 합성 성능이 오른다. 논문은 여러 벤치마크에서 기존 방법을 크게 앞섰다고 적는다.[^p6] | 1저자 Y. Yoon(Youngho Yoon), 마지막 저자 윤국진 (2명) |
| 7 | 2024 | [From SAM to CAMs: Exploring Segment Anything Model for Weakly Supervised Semantic Segmentation](https://doi.org/10.1109/cvpr52733.2024.01844) · CVPR 2024 (Oral) | 약지도 의미 분할은 영상 단위의 분류 라벨만으로 분할을 배우는 일이다. 최근 연구는 분할용 기반 모델인 SAM(Segment Anything Model)을 추론 단계에서 써서 좋은 결과를 냈지만, 초기 단서로 쓰는 클래스 활성화 지도(CAM, 분류 모델이 어느 부분을 보고 그 클래스로 판단했는지 나타낸 지도)의 잡음에 여전히 약하다. 연구진은 훈련 과정에서 SAM의 지식을 분류기에 직접 옮겨 CAM 자체의 품질을 높이는 S2C 틀을 제안했다. S2C는 SAM의 자동 분할 결과로 만든 조각별 대표 특징을 기준으로 각 특징이 자기 조각의 대표 특징에는 가깝고 다른 조각의 대표 특징에서는 멀어지게 하는 부분(SSC)과, 클래스마다 CAM에서 프롬프트를 뽑아 SAM으로 클래스별 분할 마스크를 만드는 부분(CPM)으로 이루어진다. 마스크는 SAM과 CAM의 신뢰도를 함께 고려한 점수로 모아 하나의 자기 지도 신호가 된다. 논문은 모든 벤치마크에서 최고 수준(state-of-the-art)의 성능을 냈다고 적는다.[^p7] | 1저자 H. Kweon(Hyeokjun Kweon), 마지막 저자 윤국진 (2명) |
| 8 | 2022 | [SphereSR: 360° Image Super-Resolution with Arbitrary Projection via Continuous Spherical Image Representation](https://doi.org/10.1109/cvpr52688.2022.00559) · CVPR 2022 (Oral) | 360도 영상은 같은 크기의 센서에 어안 렌즈로 찍기 때문에, 시야가 좁은 일반 원근 영상보다 각 해상도가 낮다. 그래서 360도 영상을 초해상도로 키우는 것이 유용하다. 기존 시도는 대부분 위도에 따라 왜곡이 생기는 등장방형 투영(ERP, 구면 영상을 위도·경도 격자의 직사각형으로 펼치는 방식)을 썼고, 출력 영상도 같은 형식이라 다른 투영 방식으로 바꿀 때 정보가 더 사라질 수 있다. 연구진은 저해상도 360도 영상에서 연속적인 구면 영상 표현을 만들어, 주어진 구면 좌표의 RGB 값을 예측함으로써 원하는 투영 방식의 고해상도 영상을 만드는 SphereSR을 제안했다. 정이십면체를 바탕으로 구면 자료를 표현하고 구 표면에서 특징을 효율적으로 뽑는 모듈과, 구면 좌표에서 RGB 값을 예측하는 구면 국소 암시적 영상 함수(SLIIF)를 내놓았다. 논문은 여러 벤치마크에서 기존 방법을 크게 앞섰다고 적는다.[^p8] | 1저자 Y. Yoon(Youngho Yoon), 마지막 저자 윤국진 (4명) |

## 교수와 전문 분야

윤국진 교수(Kuk-Jin Yoon)는 KAIST 기계공학과 교수다.[^mepop][^faculty] Faculty 페이지에 따르면 KAIST에서 Electrical Engineering and Computer Science 학사(1998년 2월), 석사(2000년 2월), 박사(2006년 2월) 학위를 받았다. 박사 학위 논문 제목은 "Robust Correspondence Search under Photometric Variations and Image Ambiguity"다.[^faculty] 기계공학과 교수 소개는 최종학위를 Ph.D., KAIST (2006)로, 연구분야를 Computer Vision, Machine Learning, Pattern Analysis로 적는다.[^mepop]

Faculty 페이지의 경력은 다음과 같다. 박사 학위 뒤 KAIST Robotics and Computer Vision Lab 박사후연구원(2006년 3–5월), 프랑스 INRIA Rhône-Alpes Perception Team 박사후연구원(2006년 8월–2008년 8월)을 거쳐, 광주과학기술원(GIST) School of Electrical Engineering and Computer Science에서 조교수(Assistant Professor, 2008년 8월–2014년 8월)와 부교수(Associate Professor, 2014년 9월–2018년 2월)로 일했다. 2013년 9월–2014년 8월에는 한국과학기술연구원(KIST) 방문 연구원이었다. 2018년 2월 KAIST 기계공학과 부교수가 되었고, 2024년 3월부터 교수다. 2023년 8월–2024년 7월에는 Samsung Research America(Mountain View) 방문 연구원이었다.[^faculty] KAIST에서 맡은 직책으로는 Head of KAIST Robotics Program(2023년 2–7월), Deputy Director of KAIST AI Institutes(2025년 2월–2026년 7월), Interim Dean of KAIST College of AI(2025년 12월–2026년 7월)를 적고, 2026년 7월부터 Dean of KAIST College of AI와 Director of KAIST AI Institutes를 맡고 있다고 적는다. 함께 소속된 곳(Affiliated with)으로는 Department of AX, Kim Jaechul Graduate School of AI, KAIST Institute for Robotics, Division of Future Vehicle을 적는다.[^faculty]

학술 활동으로 Faculty 페이지는 IEEE TPAMI(2023년 4월부터), Computer Vision and Image Understanding(2023년 3월부터), International Journal of Automotive Technology(2017년부터)의 Associate Editor를 적고, CVPR, ICCV, ECCV, NeurIPS, ICML, ICLR 같은 학회의 Area Chair 또는 Senior Area Chair를 맡아 왔다고 적는다(ICCV 2025는 Lead AC).[^faculty] 국내 활동으로는 Hyundai Motors Group (HMG) Autonomous Driving Challenge 2025의 Organizer와 Korean Conference on Computer Vision (KCCV 2022)의 Program Chair를 적는다.[^faculty] 공공 활동으로는 Presidential Council on National Artificial Intelligence Strategy의 Member(2025년 9월부터)와 Committee on Autonomous Vehicle Accident Investigation, KATRI/KOTSA의 Member(2025년 7월–2027년 7월)를 적는다.[^faculty] 기업 자문으로는 Samsung Electronics의 External Advisory Committee(2022년 3–12월), 42dot의 Technical Adviser(2022년 2–8월), Avikus의 Technical Adviser(2021년 2–8월)를 적는다.[^faculty]

Faculty 페이지의 수상 목록에서 2021–2026년 항목은 KAIST Education Innovation Award(2026), KAIST Major Achievements in 14 Future Technology Areas (Autonomous Driving)(2026), KAIST Impact Research Award(2025), IEEE/CVF WACV Test of Time Award(2025), Samsung HumanTech Paper Award Bronze Prize (as an Advisor)(2023), 35th Workshop on Image Processing and Image Understanding Best Paper Award (Gold Prize)(2023), 34th Workshop on Image Processing and Image Understanding Best Paper Awards (Grand and Gold Prizes)(2022), Technology Innovation Award, College of Engineering, KAIST(2022), Selection of KAIST's Top 10 Research Achievements(2022), KI (KAIST Institute) Convergence Researcher Award(2021), Event-based Stereo Challenge in CVPRW 2021의 The 1st and 3rd Place(2021)다.[^faculty]

교수 CV는 연구 관심을 컴퓨터 비전, 기계학습, 패턴 인식으로 적고, 세부 관심으로 자율 시스템과 로보틱스를 위한 시각 지능, 이벤트·360도·RGB-D(색 영상과 깊이 영상을 함께 담은 자료)·LiDAR·레이더를 쓰는 이벤트 기반·멀티모달 시각 센싱, 체화 AI(embodied AI)와 자율주행을 위한 월드 모델과 기반 모델, 기하를 고려한 3차원 장면 이해(다시점 복원, SLAM(자기 위치 추정과 지도 작성을 함께 하는 기술), 시각 주행 거리 측정), 여러 물체의 검출·추적과 움직임 이해, 다중 센서 융합과 약하거나 제한된 감독에서의 학습을 든다.[^cv] 2021–2026년 대표 논문으로 보면 최근 전문 분야는 종단간 자율주행과 움직임 계획(대표 논문 1, 2), 이벤트 카메라 기반 3차원 인지(대표 논문 3, 4), LiDAR·4D 레이더 융합 3차원 검출(대표 논문 5), 새 시점 합성(대표 논문 6), 약지도 의미 분할(대표 논문 7), 360도 영상 초해상도(대표 논문 8)다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

기계공학과 연구분야 페이지는 교수 연구의 주요 응용 산업을 모빌리티와 로보틱스로 적는다.[^mer1] Projects 페이지의 과제 가운데 자율주행 쪽으로는 강건한 자율주행을 위한 자료 증강과 센서 융합(42dot), 주변 환경 인지와 지도 정보를 쓴 물체 예측 모델(Hyundai NGV), 자율주행용 저수준 영상 융합(Hyundai Motors), 비정형 비포장 환경의 자율주행(Hanwha Aerospace), 센서 기반 시설 협력 자율주행 연결 기술(지원 Ministry of Trade, Industry and Energy (MOTIE), 기관 LG Electronics)이 있다.[^projects] 그 밖에 자연어 처리 지식 기반의 휴머노이드 로봇 조종사 개발(지원 Ministry of National Defense, 기관 Agency for Defense Development (ADD)), 양극(cathode) SEM 영상의 입자 자동 분석(LG Energy Solution), 생성 AI 기반 16비트 HDR 솔루션(Samsung Electronics), C-arm X선 동영상 엔진 개발(DK Medical Systems), 수하물 X선 판독 훈련 시스템용 AI 모듈, 미래 도시를 위한 도시 AI 기술 공동 연구(GS E&C)도 있다.[^projects]

## 구성원

누리집 People 페이지 Current Members의 34명 가운데 행정 직원(Administrative Assistant) 1명을 뺀 33명이다(박사후연구원 3명, 박사과정 19명, 석사과정 8명, 인턴 3명). 과정은 카드가 놓인 구역(Postdocs, PhD Students, Masters Students, Interns)을 옮긴 것이고, 괄호 안은 카드에 적힌 소속 학과·프로그램(인턴은 학교와 학과)이다. Part-time 표기는 쉼표로 이어 적었다. 연구 주제는 카드의 Research Interests이며, 카드가 TBD로 적은 사람은 칸이 비어 있다. 대표 논문 참여 칸은 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Hyeonseong Kim | 박사후연구원 |  | brian617@kaist.ac.kr | 5 |
| Youngho Yoon | 박사후연구원 | Novel View Synthesis, Neural Radiance Fields | dudgh1732@kaist.ac.kr | 6, 8 |
| Hoonhee Cho | 박사후연구원 | Stereo Vision, Multi-modal sensor | gnsgnsgml@kaist.ac.kr | 1, 3, 4 |
| Jihun Kim | 박사과정 (Mechanical Engineering) | Semantic Segmentation, Domain Adaptation, Point Cloud, Foundation Model | jihun1998@kaist.ac.kr |  |
| Byeongin Joung | 박사과정 (Mechanical Engineering) |  | byeonginjoung@kaist.ac.kr |  |
| Hyun-Kurl Jang | 박사과정 (Mechanical Engineering) | 3D Vision | jhg0001@kaist.ac.kr |  |
| Jaeseok Jeong | 박사과정 (Mechanical Engineering) | 3D Vision | jason.jeong@kaist.ac.kr |  |
| Jin-Ho Kim | 박사과정 (Mechanical Engineering, Part-time) |  | jinho99@kaist.ac.kr |  |
| Minjun Kang | 박사과정 (The Robotics Program) | World Model, Generative AI | kmmj2005@kaist.ac.kr |  |
| Jongoh Jeong | 박사과정 (The Robotics Program) | Visual Recognition, Domain Adaptation/Generalization | jeong2@kaist.ac.kr |  |
| Changgyoon Oh | 박사과정 (Mechanical Engineering) | Generative Models | changgyoon@kaist.ac.kr |  |
| Jegyeong Cho | 박사과정 (Mechanical Engineering) |  | j2k0618@kaist.ac.kr |  |
| Wooseong Jeong | 박사과정 (Mechanical Engineering) |  | stk14570@kaist.ac.kr | 2 |
| Jaewoo Jeong | 박사과정 (Mechanical Engineering) | Human Motion Forecasting, Trajectory Prediction | jeong207@kaist.ac.kr | 2 |
| Yuhwan Jeong | 박사과정 (Mechanical Engineering) | Optical Flow, Diffusion Models | jeongyh98@kaist.ac.kr |  |
| Yunseo Yang | 박사과정 (Mechanical Engineering) |  | acorn@kaist.ac.kr |  |
| Jongseob Yun | 박사과정 (Mechanical Engineering, Part-time) |  | jseob.y@kaist.ac.kr |  |
| Minseok Kim | 박사과정 (Mechanical Engineering) |  | alstjrx1x1@kaist.ac.kr |  |
| Jae-Young Kang | 박사과정 (Mechanical Engineering) | Autonomous Driving, Event-based Vision | mickeykang@kaist.ac.kr | 1, 3, 4 |
| Hoyong Kwon | 박사과정 (The Robotics Program) | Semantic Segmentation, Foundation Model | kwonhoyong3@kaist.ac.kr |  |
| Giwon Lee | 박사과정 (Mechanical Engineering) |  | dlrldnjs@kaist.ac.kr | 1, 2 |
| Daehyun We | 박사과정 (The Robotics Program) |  | greathyun@kaist.ac.kr |  |
| Seonkyu Song | 석사과정 (Mechanical Engineering) |  | sok9854@kaist.ac.kr |  |
| Yujin Bae | 석사과정 (The Robotics Program) |  | yujinbae@kaist.ac.kr |  |
| Jiyong Boo | 석사과정 (Mechanical Engineering) |  | boojiyong@kaist.ac.kr |  |
| Jinnyeong Yang | 석사과정 (Division of Future Vehicle) |  | jinnyeong6118@kaist.ac.kr |  |
| Hyemin Yang | 석사과정 (The Robotics Program) |  | hyemin0806@kaist.ac.kr | 1 |
| Wonyoung Lee | 석사과정 (Kim Jaechul Graduate School of AI) |  | bsis2one0@kaist.ac.kr |  |
| Youngho Kim | 석사과정 (Mechanical Engineering) |  | kmax2001@kaist.ac.kr | 4 |
| Yeoeun Kim | 석사과정 (Department of AX) |  | ye.kim@kaist.ac.kr |  |
| Hajoon Park | 인턴 (KAIST Mechanical Engineering) |  | dareum@kaist.ac.kr |  |
| Jinhyeok Ju | 인턴 (KAIST Mechanical Engineering) |  | 02jerry@kaist.ac.kr |  |
| Haneul Seong | 인턴 (KAIST Mechanical Engineering) |  | castlesky@kaist.ac.kr |  |

## 졸업생과 이전 구성원

누리집 People 페이지 Alumni 구역의 카드 74장 전부다(Postdoc Alumni 1장, Ph.D. Graduates 25장, M.S. Graduates 48장). 연구실에서 석사를 마치고 박사과정을 이어 간 사람은 누리집이 석사 카드를 따로 두고 진로를 "Continued to Ph.D. at VILab"으로 적으며, 박사과정을 마친 뒤 박사후연구원으로 남은 사람도 박사 카드와 박사후연구원 카드가 따로 있다. 그래서 같은 사람이 두 줄로 나오거나 현재 구성원 표에도 있다. 학위 칸의 Ph.D·Masters·Postdoc과 괄호 안 과정(Integrated M.S.-Ph.D.)은 카드 표기이고, 연도 칸은 카드의 졸업 연월(박사후연구원은 기간)이다. 교수가 KAIST로 옮겨 온 2018년 2월 이전에 졸업한 사람도 이 명단에 함께 있다.[^people][^faculty]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Taeyeop Lee | Postdoc (2025-03 – 2026-08) | KIST |
| Hunmin Yang | Ph.D (2026-02) | ADD |
| Yujeong Chae | Ph.D (2026-02) | NVIDIA Korea |
| Youngho Yoon | Ph.D (Integrated M.S.-Ph.D.) (2026-02) | KAIST Postdoc (VILab) |
| Hyeonseong Kim | Ph.D (Integrated M.S.-Ph.D.) (2026-02) | KAIST Postdoc (VILab) |
| Hoonhee Cho | Ph.D (2026-02) | KAIST Postdoc (VILab) |
| Seongyong Ahn | Ph.D (2025-02) | ADD |
| Taewoo Kim | Ph.D (2025-02) | Qualcomm |
| Sung-Hoon Yoon | Ph.D (2025-02) | DGIST |
| Daehee Park | Ph.D (2025-02) | DGIST |
| Hyeokjun Kweon | Ph.D (2025-02) | Chung-Ang University |
| Taeyeop Lee | Ph.D (2025-02) | KAIST Postdoc (VILab) |
| Inkyu Shin | Ph.D (2024-02) | TikTok |
| Pranjay Shyam | Ph.D (2022-08) | Faurecia Irystec |
| Lin Wang | Ph.D (2021-08) | NTU-Singapore |
| S. Mohammad Mostafavi I | Ph.D (2021-08) | Learning Unit (Lunit) |
| Jeong-Kyun Lee | Ph.D (2020-02) | Qualcomm |
| Chang-Ryeol Lee | Ph.D (2019-08) | SLAMcore in UK |
| Yeong-Jun Cho | Ph.D (2018-08) | Chonnam University |
| Han-Mu Park | Ph.D (2018-02) | Korea Electronics Technology Institute (KETI) |
| Min-Gyu Park | Ph.D (2017-02) | Korea Electronics Technology Institute (KETI) |
| Yong-Ho Shin | Ph.D (2017-02) | Qualcomm Korea |
| Seung-Hwan Bae | Ph.D (2015-08) | Inha University |
| Min-Koo Kang | Ph.D (2015-08) | Korea Institute of Science and Technology (KIST) |
| Jong-Hee Park | Ph.D (2015-08) | Korea Electronics Technology Institute (KETI) |
| Ju-Hong Yoon | Ph.D (2014-08) | Korea Electronics Technology Institute (KETI) |
| Heejun Park | Masters (2026-08) | Hyundai |
| Giwon Lee | Masters (2026-02) | Continued to Ph.D. at VILab |
| Daehyun We | Masters (2026-02) | Continued to Ph.D. at VILab |
| Minseok Kim | Masters (2025-02) | Continued to Ph.D. at VILab |
| Jae-Young Kang | Masters (2025-02) | Continued to Ph.D. at VILab |
| Hoyong Kwon | Masters (2025-02) | Continued to Ph.D. at VILab |
| Youngjin Oh | Masters (2025-02) |  |
| Yuhwan Jeong | Masters (2024-02) | Continued to Ph.D. at VILab |
| Yunseo Yang | Masters (2024-02) | Continued to Ph.D. at VILab |
| In-Chul Chung | Masters (2023-08) | HD Korea Shipbuilding & Offshore Engineering |
| Wooseong Jeong | Masters (2023-02) | Continued to Ph.D. at VILab |
| Jegyeong Cho | Masters (2023-02) | Continued to Ph.D. at VILab |
| Jihun Kim | Masters (2023-02) | Continued to Ph.D. at VILab |
| Jeong-Min Lee | Masters (2023-02) | KETI |
| Yoonsu Kang | Masters (2023-02) |  |
| Hoonhee Cho | Masters (2022-02) | Continued to Ph.D. at VILab |
| Changgyoon Oh | Masters (2022-02) | Continued to Ph.D. at VILab |
| Kang-Il Lee | Masters (2022-02) | Machine Intelligence Lab, Seoul National University (Ph.D Candidate) |
| Yujeong Chae | Masters (2021-02) | Continued to Ph.D. at VILab |
| Taewoo Kim | Masters (2021-02) | Continued to Ph.D. at VILab |
| Won-June Cho | Masters (2021-02) | NaverLabs |
| Kwon-Young Ryu | Masters (2021-02) | Postech (Ph.D Candidate) |
| Kyeong-Seob Song | Masters (2021-02) | Hyundai Motors |
| Jung-Won Lee | Masters (2021-02) | Hyundai Motors |
| Jaeseok Jeong | Masters (2020-08) | Continued to Ph.D. at VILab |
| Jongseob Yun | Masters (2020-08) | Continued to Ph.D. at VILab |
| Hee-Chan Jung | Masters (2020-08) | Avikus |
| Sung-Hyun Park | Masters (2020-08) | Bear Robotics |
| Sung-Hoon Yoon | Masters (2020-02) | Continued to Ph.D. at VILab |
| Yeon-Kun Lee | Masters (2020-02) | NCSOFT |
| Jeong-Yun Na | Masters (2018-08) | Hyundai Mobis |
| Hyeok-Jae Choi | Masters (2018-02) | SUALAB |
| Jae-Han Park | Masters (2018-02) | Algorigo |
| Yong-Hoon Kwon | Masters (2017-08) | Korea Electronics Technology Institute (KETI) |
| Jae-Won Yae | Masters (2017-02) | LG Electronics |
| Yeong-Won Kim | Masters (2016-08) | VUNO inc |
| Se-Hoon Park | Masters (2016-02) | LG Electronics |
| Dae-Yong Cho | Masters (2016-02) | KIST |
| Su-A Kim | Masters (2015-08) | Intel Visual Computing Institute |
| Dae-Won Ko | Masters (2015-02) | POSTECH Full-time Researcher |
| Hee-Jong Hong | Masters (2015-02) | Hanhwa Corporation |
| Yeong-Jun Cho | Masters (2014-02) | Continued to Ph.D. at VILab |
| Chang-Ryeol Lee | Masters (2013-02) | Continued to Ph.D. at VILab |
| Dae-Young Kim | Masters (2012-02) | Hyundai Motors |
| Seung-Hwan Jung | Masters (2012-02) | Hyundai Motors |
| Min-Gyu Park | Masters (2011-08) | Continued to Ph.D. at VILab |
| Yong-Ho Shin | Masters (2011-02) | Continued to Ph.D. at VILab |
| Min-Gil Shin | Masters (2010-08) | LG Electronics |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지는 연도 구역 2026–2021과 -2020 구역에 논문과 특허를 함께 싣는다.[^pubs] 아래는 2021–2026년 구역의 논문 146편이다(2026년 40편, 2025년 25편, 2024년 28편, 2023년 18편, 2022년 19편, 2021년 16편). 학회 논문 113편, 학술지 논문 27편, 워크숍 논문 6편이다. 저자 순서와 이름 뒤 *·†, 제목, 학술지·학회 표기와 연도는 누리집 그대로이고, 누리집이 붙인 발표 형식(Oral, Highlight)과 워크숍 이름도 옮겼다. 누리집은 *와 †의 뜻을 적지 않는다. 연도는 누리집 연도 구역 기준이다. 누리집 자료는 학술지 논문 9편의 상태를 accepted로 적어 「게재 승인, 누리집 자료 표기」로 표시했다. 그 가운데 TPAMI 2편은 News 페이지가 2025-12-05에 게재를 알렸고 Crossref에 권·쪽이 있는 출판 서지가 있어 그 서지를 함께 적었다. 2026년 구역의 NeurIPS 2026 논문 3편은 News 페이지가 2026-09-25에 채택을 알린 학회 논문이라 「채택」으로 표시했다.[^pubs][^news]

**2026**

- Hoonhee Cho\*, Giwon Lee\*, Jae-Young Kang\*, Hyemin Yang\*, Heejun Park\*, Kuk-Jin Yoon. "HEAT: Heterogeneous End-to-End Autonomous Driving via Trajectory-Guided World Models". *IEEE Robotics and Automation Letters (RA-L) 2026 (게재 승인, 누리집 자료 표기)*.
- Hyemin Yang\*, Wooseong Jeong\*, Giwon Lee\*, Kuk-Jin Yoon. "Triggering Generalist Reasoning via Predictive Uncertainty for Dual-System VLA". *NeurIPS 2026 (채택)*.
- Hyun-Kurl Jang, Jihun Kim, Kuk-Jin Yoon. "Preference-Guided Adaptation for Open-Vocabulary Semantic Segmentation via Prompt Disagreement". *NeurIPS 2026 (채택)*.
- Jaewoo Jeong\*, Seonkyu Song\*, Hyeonwoo Park, Yujin Bae, Jegyeong Cho, Giwon Lee, Daehee Park, Kuk-Jin Yoon. "SRA: Spatial Reasoning Adapter via Evolving Social Interaction Graphs for Trajectory Prediction". *NeurIPS 2026 (채택)*.
- Jinho Kim, Kuk-Jin Yoon. "Encoder-Level Temporal Fusion Transformers for Robust Multi-Object Tracking". *IEEE Access 2026 (게재 승인, 누리집 자료 표기)*.
- Hoonhee Cho\*, Jae-Young Kang\*, Giwon Lee\*, Hyemin Yang\*, Heejun Park\*, Kuk-Jin Yoon. "VIPS: Vehicle-Infrastructure Cooperative Planning Benchmark via Pseudo-Simulation". *ECCV 2026 (Oral)*.
- Yunseo Yang\*, Youngho Yoon\*, Kuk-Jin Yoon. "PriSplat: Propagating Reliable Multi-view Information for Distractor-Free 3DGS". *ECCV 2026 (Oral)*.
- Minjun Kang, Inkyu Shin, Taeyeop Lee, Myungchul Kim, In So Kweon, Kuk-Jin Yoon. "GeoNVS: Geometry Grounded Video Diffusion for Novel View Synthesis". *ECCV 2026 (Oral)*.
- Jiyong Boo, Byeongin Joung, Hyemin Yang, Kuk-Jin Yoon. "HSDF-Lane: Height-Aligned Signed Distance Field with Semantic Lane Prior for 3D Lane Detection". *ECCV 2026*.
- Youngho Kim\*, Hoonhee Cho\*, Jae-Young Kang, Kuk-Jin Yoon. "GoStop: Reinforcement Learning for Adaptive Temporal Aggregation in Event-Based Feature Tracking". *ECCV 2026*.
- Heejun Park, Jaeseok Jeong, Kuk-Jin Yoon. "RAF: Reliability-Aware Fusion of Camera, LiDAR, and 4D RADAR for Robust 3D Object Detection in Adverse Weather". *ECCV 2026*.
- Daehyun We, Youngho Yoon, Jiyong Boo, Kuk-Jin Yoon. "MotionEditGS: Editing Motion and Appearance of 4D Scenes from Monocular Video via Semantically Anchored Gaussians". *ECCV 2026*.
- Hyun-Kurl Jang\*, Jihun Kim\*, Hyeokjun Kweon\*, Kuk-Jin Yoon. "Distill Once, Adapt Life-Long: Exploring Dataset Distillation for Continual Test-Time Adaptation". *ECCV 2026*.
- Taewon Seo\*, Seonae Jeon\*, Giwon Lee\*, Kuk-Jin Yoon†, Daehee Park†. "Unified Prediction and Planning via Conflict-Aware Disjoint Parameter Training". *ECCV 2026*.
- Yujin Bae\*, Jaewoo Jeong\*, Hyeonseong Kim\*, Kuk-Jin Yoon. "Ego-human Motion Prediction with 3D-aware LLM". *ECCV 2026*.
- Yuhwan Jeong\*, Hyeonseong Kim\*, Daehyun We\*, Seonkyu Song\*, Jinnyeong Yang\*, Hyun-Kurl Jang, Youngho Yoon, Kuk-Jin Yoon. "FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model". *ECCV 2026*.
- Sung-Hoon Yoon\*, Hoyong Kwon\*, Changgyoon Oh\*, Kuk-Jin Yoon. "DINOde: Continuous Vision-Text Alignment for Open-Vocabulary Semantic Segmentation". *ECCV 2026*.
- Jongoh Jeong, Sun-Kyung Lee, Kuk-Jin Yoon. "Rank-Aware Hyperbolic Alignment for Vision-Language Dataset Distillation". *ECCV 2026; Also at Workshop: Second Workshop on Curated Data for Efficient Learning · ECCV 2026 Workshop*.
- Jihun Kim\*, Hyun-Kurl Jang\*, Hyemin Yang\*, Jinnyeong Yang\*, Hyeokjun Kweon\*, Kuk-Jin Yoon. "Bootstrapping a 4D LiDAR Annotation Tool from Video Foundation Models". *ECCV Workshop 2026; Workshop: Second Workshop on Curated Data for Efficient Learning · ECCV 2026 Workshop (Oral)*.
- Yuhwan Jeong, Kuk-Jin Yoon. "Reuse Before You Retrieve: Diagnosing Headroom and Complementarity for Test-Time Augmentation of Embodied Multimodal Policies". *ECCV Workshop 2026; Workshop: Workshop on Embodied Multimodal Reasoning in Physical Environments · ECCV 2026 Workshop*.
- Jegyeong Cho, Kuk-Jin Yoon. "Global Information Thresholding for Sufficient and Necessary Circuits". *CVPR 2026*.
- Hyeonseong Kim\*, Hyun-Kurl Jang\*, Kuk-Jin Yoon. "Test-Time Training for LiDAR Semantic Segmentation under Corruption via Geometric Inlier Discrimination". *CVPR 2026*.
- Jae-Young Kang\*, Hoonhee Cho\*, Taeyeop Lee\*, Minjun Kang, Bowen Wen, Youngho Kim, Kuk-Jin Yoon. "Event6D: Event-based Novel Object 6D Pose Tracking". *CVPR 2026*.
- Youngho Yoon, Wonjune Cho, Hyunho Ha, Sujung Kim, Kuk-Jin Yoon. "ExPose: Reinforcing Video Generation Models for Extreme Pose Estimation". *CVPR 2026*.
- Wooseong Jeong\*, Wonyoung Lee\*, Kuk-Jin Yoon. "Preference-Aligned LoRA Merging: Preserving Subspace Coverage and Addressing Directional Anisotropy". *CVPR 2026*.
- Jihun Kim\*, Hoyong Kwon\*, Hyeokjun Kweon\*, Kuk-Jin Yoon. "Bootstrapping Video Semantic Segmentation Model via Distillation-assisted Test-Time Adaptation". *CVPR 2026*.
- Hoonhee Cho\*, Jae-Young Kang\*, Yuhwan Jeong\*, Yunseo Yang, Wonyoung Lee, Youngho Kim, Kuk-Jin Yoon. "DSERT-RoLL: Robust Multi-Modal Perception for Diverse Driving Conditions with Stereo Event-RGB-Thermal Cameras, 4D Radar, and Dual-LiDAR". *CVPR 2026*.
- Hoonhee Cho\*, Yuhwan Jeong\*, Kuk-Jin Yoon. "Event-based Motion Deblurring with Unpaired Data". *CVPR 2026 (Highlight)*.
- Wonyoung Lee\*, Wooseong Jeong\*, Kuk-Jin Yoon. "Label-Free Cross-Task LoRA Merging with Null-Space Compression". *CVPR 2026*.
- Jongoh Jeong\*, Hoyong Kwon\*, Minseok Kim\*, Kuk-Jin Yoon. "Multimodal Distribution Matching for Vision-Language Dataset Distillation". *CVPR 2026; Also at Workshop: Workshop on Emerging Directions in Data for Multimodal Foundation Models · CVPR 2026 Workshop*.
- Jongoh Jeong, Hunmin Yang, Jaeseok Jeong, Kuk-Jin Yoon. "Improving Black-Box Generative Attacks via Generator Semantic Consistency". *ICLR 2026*.
- Youngho Yoon, Kuk-Jin Yoon. "ReSplat: Degradation-agnostic Feed-forward Gaussian Splatting via Self-guided Residual Diffusion". *ICLR 2026*.
- Jangwon Bae†, Minjun Kang, Donghyuk Lee, Kuk-Jin Yoon†, Yongwon Jung†. "A machine learning framework for predicting and modulating condition-dependent protein phase separation". *Nature Communications 2026*.
- Hyeonseong Kim, Yoonsu Kang, Changgyoon Oh, Kuk-Jin Yoon. "Toward Enhanced Representation Learning for Single-Source Domain Generalization in LiDAR Semantic Segmentation". *TPAMI 2026 (게재 승인, 누리집 자료 표기; News 2025-12-05 TPAMI 게재 소식, Crossref 서지 48권 6053-6070, 2026)*.
- Jae-Young Kang\*, Hoonhee Cho\*, Kuk-Jin Yoon. "Temporal Stereo Matching from Event Cameras via Joint Learning with Stereoscopic Flow". *TPAMI 2026 (게재 승인, 누리집 자료 표기; News 2025-12-05 TPAMI 게재 소식, Crossref 서지 48권 4098-4113, 2026)*.
- Donghyeong Lee, Seokwan Roh, Jaewoo Jeong, Kuk-Jin Yoon, Jungchul Lee, Youngsuk Nam. "Analysis of Multiscale Condensation Phenomena Using a Zero-Shot Computer Vision Framework". *Advanced Science 2026 (게재 승인, 누리집 자료 표기)*.
- Wooseong Jeong, Jegyeong Cho, Youngho Yoon, Jaeyoung Lee, Kuk-Jin Yoon. "Stabilizing Multi-Task Latent Spaces: Recursive Refinement With Coordinators in Partially Labeled Learning". *IEEE Access 2026 (게재 승인, 누리집 자료 표기)*.
- Jinho Kim, Kuk-Jin Yoon. "Gated Temporal Fusion Transformers for Robust Multi-Object Tracking". *WACV 2026*.
- Minseok Kim, Jiyong Boo, Kuk-Jin Yoon. "Generalized Category Discovery for LiDAR Semantic Segmentation". *WACV 2026*.
- Changgyoon Oh\*, Hyeonseong Kim\*, Daehyun We\*, Jongoh Jeong, Yujeong Chae, Kuk-Jin Yoon. "DOODLE: Diffusion-based Out-of-Distribution Learning for Open-set LiDAR Semantic Segmentation". *WACV 2026*.

**2025**

- Hoonhee Cho\*, Jae-Young Kang\*, Giwon Lee\*, Hyemin Yang\*, Heejun Park, Seokwoo Jung, Kuk-Jin Yoon. "VR-Drive: Viewpoint-Robust End-to-End Driving with Feed-Forward 3D Gaussian Splatting". *NeurIPS 2025*.
- Daehee Park, Monu Surana, Pranav Desai, Ashish Mehta, Reuben MV John, Kuk-Jin Yoon. "Generative Active Learning for Long-tail Trajectory Prediction via Controllable Diffusion Model". *ICCV 2025*.
- Jihun Kim\*, Hoyong Kwon\*, Hyeokjun Kweon\*, Wooseong Jeong, Kuk-Jin Yoon. "DC-TTA: Divide-and-Conquer Framework for Test-Time Adaptation of Interactive Segmentation". *ICCV 2025*.
- Giwon Lee\*, Wooseong Jeong\*, Daehee Park, Jaewoo Jeong, Kuk-Jin Yoon. "Interaction-Merged Motion Planning: Effectively Leveraging Diverse Motion Datasets for Robust Planning". *ICCV 2025 (Highlight)*.
- Yujeong Chae, Heejun Park, Hyeonseong Kim, Kuk-Jin Yoon. "Doppler-Aware LiDAR-Radar Fusion for Weather-Robust 3D Detection". *ICCV 2025*.
- Jae-Young Kang\*, Hoonhee Cho\*, Kuk-Jin Yoon. "Unleashing the Temporal Potential of Stereo Event Cameras for Continuous-Time 3D Object Detection". *ICCV 2025*.
- Taewoo Kim, Kuk-Jin Yoon. "Event-guided Unified Framework for Low-light Video Enhancement, Frame Interpolation, and Deblurring". *ICCV 2025*.
- Yuhwan Jeong\*, Yunseo Yang\*, Youngho Yoon\*, Kuk-Jin Yoon. "Robust Adverse Weather Removal via Spectral-based Spatial Grouping". *ICCV 2025*.
- Youngho Kim\*, Hoonhee Cho\*, Kuk-Jin Yoon. "From Sharp to Blur: Unsupervised Domain Adaptation for 2D Human Pose Estimation Under Extreme Motion Blur Using Event Cameras". *ICCV 2025*.
- Hoonhee Cho\*, Yuhwan Jeong\*, Kuk-Jin Yoon. "Learning Large Motion Estimation from Intermediate Representations with a High-Resolution Optical Flow Dataset Featuring Long-Range Dynamic Motion". *ICCV 2025 (Highlight)*.
- Wooseong Jeong\*, Jegyeong Cho\*, Youngho Yoon\*, Kuk-Jin Yoon. "Synchronizing Task Behavior: Aligning Multiple Tasks during Test-Time Training". *ICCV 2025*.
- Wooseong Jeong, Kuk-Jin Yoon. "Resolving Token-Space Gradient Conflicts: Token Space Manipulation for Transformer-Based Multi-Task Learning". *ICCV 2025*.
- Jongseob Yun, Yong-Hoon Kwon, Min-Gyu Park, Ju-Mi Kang, Min-Ho Lee, Inho Chang, Ju Hong Yoon, Kuk-Jin Yoon. "WarpHE4D: Dense 4D Head Map toward Full Head Reconstruction". *ICCV 2025*.
- Mingu Kang, Joon-Kyuu Han, Kichul Lee, Jaeseok Jeong, Chanyoung Yoo, Jeong Woo Jeon, Byongwoo Park, Wonho Choi, Junseong Ahn, Kuk-Jin Yoon, Cheol Seong Hwang, Inkyu Park. "Neuromorphic olfaction with ultralow-power gas sensors and ovonic threshold switch". *Science Advances 2025 (게재 승인, 누리집 자료 표기)*.
- Giwon Lee\*, Daehee Park\*, Jaewoo Jeong\*, Kuk-Jin Yoon. "Non-differentiable Reward Optimization for Diffusion-based Autonomous Motion Planning". *IROS 2025*.
- Hyeokjun Kweon, Kuk-Jin Yoon. "WISH: Weakly Supervised Instance Segmentation using Heterogeneous Labels". *CVPR 2025 (Highlight)*.
- Taeyeop Lee, Bowen Wen, Minjun Kang, Gyuree Kang, In So Kweon, Kuk-Jin Yoon. "Any6D: Model-free 6D Pose Estimation of Novel Objects". *CVPR 2025*.
- Hoonhee Cho\*, Jae-Young Kang\*, Youngho Kim, Kuk-Jin Yoon. "Ev-3DOD: Pushing the Temporal Boundaries of 3D Object Detection with Event Cameras". *CVPR 2025 (Highlight)*.
- Jaewoo Jeong, Seohee Lee, Daehee Park, Giwon Lee, Kuk-Jin Yoon. "Multi-modal Knowledge Distillation-based Human Trajectory Forecasting". *CVPR 2025*.
- Jongoh Jeong, Hunmin Yang, Kuk-Jin Yoon. "Boosting Adversarial Transferability with a Generative Model Perspective". *CVPR Workshop 2025; Workshop: 3rd Workshop on Generative Models for Computer Vision · CVPR 2025 Workshop*.
- Wooseong Jeong, Kuk-Jin Yoon. "Selective Task Group Updates for Multi-Task Optimization". *ICLR 2025*.
- Hoonhee Cho, Jae-Young Kang, Taewoo Kim, Yuhwan Jeong, Kuk-Jin Yoon. "Unifying Low-Resolution and High-Resolution Alignment by Event Cameras for Space-Time Video Super-Resolution". *WACV 2025*.
- Inkyu Shin, Qihang Yu, Ming-Hsuan Yang, Xiaohui Shen, In So Kweon, Kuk-Jin Yoon, Liang-Chieh Chen. "Enhancing Temporal Consistency in Video Editing by Reconstructing Videos with 3D Gaussian Splatting". *Transactions on Machine Learning Research (TMLR) 2025*.
- Byeongju Lee, Mingu Kang, Kichul Lee, Yujeong Chae, Kuk-Jin Yoon, Dae-Sik Lee, Inkyu Park. "Multigas Identification by Temperature-Modulated Operation of a Single Anodic Aluminum Oxide Gas Sensor Platform and Deep Learning Algorithm". *ACS Sensors 2025*.
- Wooseong Jeong, Jihun Kim, Hyeokjun Kweon, Kuk-Jin Yoon. "Multi-View 3D Scene Abstraction From Drone-Captured RGB Images". *IEEE Access 2025*.

**2024**

- Hoonhee Cho\*, Taewoo Kim\*, Yuhwan Jeong, Kuk-Jin Yoon. "A Benchmark Dataset for Event-Guided Human Pose Estimation and Tracking in Extreme Conditions". *NeurIPS 2024*.
- Hyun-Kurl Jang\*, Jihun Kim\*, Hyeokjun Kweon\*, Kuk-Jin Yoon. "TALoS: Enhancing Semantic Scene Completion via Test-time Adaptation on the Line of Sight". *NeurIPS 2024*.
- Hunmin Yang, Jongoh Jeong, Kuk-Jin Yoon. "Prompt-Driven Contrastive Learning for Transferable Adversarial Attacks". *ECCV 2024 (Oral)*.
- Taewoo Kim, Jaeseok Jeong, Hoonhee Cho, Yuhwan Jeong, Kuk-Jin Yoon. "Towards Real-world Event-guided Low-light Video Enhancement and Deblurring". *ECCV 2024*.
- Hoyong Kwon, Jaeseok Jeong, Sung-Hoon Yoon, Kuk-Jin Yoon. "Phase Concentration and Shortcut Suppression for Weakly Supervised Semantic Segmentation". *ECCV 2024*.
- Hoonhee Cho\*, Jae-Young Kang\*, Kuk-Jin Yoon. "Temporal Event Stereo via Joint Learning with Stereoscopic Flow". *ECCV 2024*.
- Hoonhee Cho\*, Sung-Hoon Yoon\*, Hyeokjun Kweon\*, Kuk-Jin Yoon. "Finding Meaning in Points: Weakly Supervised Semantic Segmentation for Event Cameras". *ECCV 2024*.
- Sung-Hoon Yoon, Hoyong Kwon\*, Jaeseok Jeong\*, Daehee Park, Kuk-Jin Yoon. "Diffusion-Guided Weakly Supervised Semantic Segmentation". *ECCV 2024*.
- Hyeonseong Kim\*, Sung-Hoon Yoon\*, Minseok Kim, Kuk-Jin Yoon. "On-the-fly Category Discovery for LiDAR Semantic Segmentation". *ECCV 2024*.
- Yunseo Yang\*, Jihun Kim\*, Kuk-Jin Yoon. "Syn-to-Real Domain Adaptation for Point Cloud Completion via Part-based Approach". *ECCV 2024*.
- Taewoo Kim\*, Hoonhee Cho\*, Kuk-Jin Yoon. "CMTA: Cross-Modal Temporal Alignment for Event-guided Video Deblurring". *ECCV 2024*.
- Youngho Yoon\*, Hyun-Kurl Jang\*, Kuk-Jin Yoon. "GMT: Enhancing Generalizable Neural Rendering via Geometry-Driven Multi-Reference Texture Transfer". *ECCV 2024*.
- Yujeong Chae, Hyeonseong Kim, Changgyoon Oh, Minseok Kim, Kuk-Jin Yoon. "LiDAR-based All-weather 3D Object Detection via Prompting and Distilling 4D Radar". *ECCV 2024*.
- Yuhwan Jeong\*, Hoonhee Cho\*, Kuk-Jin Yoon. "Towards Robust Event-based Networks for Nighttime via Unpaired Day-to-Night Event Translation". *ECCV 2024*.
- Hyeokjun Kweon\*, Jihun Kim\*, Kuk-Jin Yoon. "Weakly Supervised Point Cloud Semantic Segmentation via Artificial Oracle". *CVPR 2024*.
- Hyeokjun Kweon, Kuk-Jin Yoon. "From SAM to CAMs: Exploring Segment Anything Model for Weakly Supervised Semantic Segmentation". *CVPR 2024 (Oral)*.
- Yujeong Chae, Hyeonseong Kim, Kuk-Jin Yoon. "Towards Robust 3D Object Detection with LiDAR and 4D Radar Fusion in Various Weather Conditions". *CVPR 2024*.
- Wooseong Jeong, Kuk-Jin Yoon. "Quantifying Task Priority for Multi-Task Optimization". *CVPR 2024*.
- Sung-Hoon Yoon, Hoyong Kwon, Hyeonseong Kim, Kuk-Jin Yoon. "Class Tokens Infusion for Weakly Supervised Semantic Segmentation". *CVPR 2024*.
- Jaewoo Jeong\*, Daehee Park\*, Kuk-Jin Yoon. "Multi-agent Long-term 3D Human Pose Forecasting via Interaction-aware Trajectory Conditioning". *CVPR 2024 (Highlight)*.
- Hoonhee Cho, Taewoo Kim, Yuhwan Jeong, Kuk-Jin Yoon. "TTA-EVF: Test-Time Adaptation for Event-based Video Frame Interpolation via Reliable Pixel and Sample Estimation". *CVPR 2024*.
- Taewoo Kim\*, Hoonhee Cho\*, Kuk-Jin Yoon. "Frequency-aware Event-based Video Deblurring for Real-World Motion Blur". *CVPR 2024*.
- Daehee Park, Jaeseok Jeong, Sung-Hoon Yoon, Jaewoo Jeong, Kuk-Jin Yoon. "T4P: Test-Time Training of Trajectory Prediction via Masked Autoencoder and Actor-specific Token Memory". *CVPR 2024*.
- Byeongin Joung, Byeong-Uk Lee, Jaesung Choe, Ukcheol Shin, Minjun Kang, Taeyeop Lee, In So Kweon, Kuk-Jin Yoon. "Stable Surface Regularization for Fast Few-Shot NeRF". *3DV 2024*.
- Hunmin Yang\*, Jongoh Jeong\*, Kuk-Jin Yoon. "FACL-Attack: Frequency-Aware Contrastive Learning for Transferable Adversarial Attacks". *AAAI 2024*.
- Daehee Park, Jaewoo Jeong, Kuk-Jin Yoon. "Improving Transferability for Cross-domain Trajectory Prediction via Neural Stochastic Differential Equation". *AAAI 2024*.
- Inkyu Shin, Dahun Kim, Qihang Yu, Jun Xie, Hong-Seok Kim, Bradley Green, In So Kweon, Kuk-Jin Yoon, Liang-Chieh Chen. "Video-kMaX: A Simple Unified Approach for Online and Near-Online Video Panoptic Segmentation". *WACV 2024*.
- Minjie Liu, Hongjian Wang, Kuk-Jin Yoon, Lin Wang. "Disentangled Cross-modal Fusion for Event-guided Image Super-Resolution". *IEEE Transactions on Artificial Intelligence 2024 (게재 승인, 누리집 자료 표기)*.

**2023**

- Jihun Kim, Hyeokjun Kweon, Yunseo Yang, Kuk-Jin Yoon. "Learning Point Cloud Completion without Complete Point Clouds: A Pose-aware Approach". *ICCV 2023*.
- Hoonhee Cho\*, Hyeonseong Kim\*, Yujeong Chae, Kuk-Jin Yoon. "Label-Free Event-based Object Recognition via Joint Learning with Image Reconstruction from Events". *ICCV 2023 (Oral)*.
- Hoonhee Cho, Yuhwan Jeong, Taewoo Kim, Kuk-Jin Yoon. "Non-Coaxial Event-guided Motion Deblurring with Spatial Alignment". *ICCV 2023*.
- Muhammad Jehanzeb Mirza, Inkyu Shin, Wei Lin, Andreas Schriebl, Kunyang Sun, Jaesung Choe, Mateusz Kozinski, Horst Possegger, In So Kweon, Kuk-Jin Yoon, Horst Bischof. "MATE: Masked Autoencoders are Online 3D Test-Time Learners". *ICCV 2023*.
- Inkyu Shin, Dahun Kim, Qihang Yu, Jun Xie, Hong-Seok Kim, Bradley Green, In So Kweon, Kuk-Jin Yoon, Liang-Chieh Chen. "Video-kMaX: A Simple Unified Approach for Online and Near-Online Video Panoptic Segmentation". *CVPR Workshop 2023; Workshop: CVPR 2023 Workshop*.
- Valts Blukis, Taeyeop Lee, Jonathan Tremblay, Bowen Wen, In So Kweon, Kuk-Jin Yoon, Dieter Fox, Stan Birchfield. "One-Shot Neural Fields for 3D Object Understanding". *CVPR Workshop 2023; Workshop: CVPR 2023 Workshop*.
- Taewoo Kim, Yujeong Chae, Hyun-Kurl Jang, Kuk-Jin Yoon. "Event-based Video Frame Interpolation with Cross-Modal Asymmetric Bidirectional Motion Fields". *CVPR 2023*.
- Hoonhee Cho, Jegyeong Cho, Kuk-Jin Yoon. "Learning to Adaptive Dense Event Stereo from Image Domain". *CVPR 2023*.
- Hyeokjun Kweon\*, Sung-Hoon Yoon\*, Kuk-Jin Yoon. "Weakly Supervised Semantic Segmentation via Adversarial Learning of Classifier and Reconstructor". *CVPR 2023*.
- Youngho Yoon, Kuk-Jin Yoon. "Cross-Guided Optimization of Radiance Fields with Multi-View Image Super-Resolution for High-Resolution Novel View Synthesis". *CVPR 2023*.
- Hyeonseong Kim\*, Yoonsu Kang\*, Changgyoon Oh, Kuk-Jin Yoon. "Single Domain Generalization for LiDAR Semantic Segmentation". *CVPR 2023*.
- Taeyeop Lee, Jonathan Tremblay, Valts Blukis, Bowen Wen, Byeong-Uk Lee, Inkyu Shin, Stan Birchfield, In So Kweon, Kuk-Jin Yoon. "TTA-COPE: Test-Time Adaptation for Category-Level Object Pose Estimation". *CVPR 2023*.
- Daehee Park, Hobin Ryu, Yunseo Yang, Jegyeong Cho, Jiwon Kim, Kuk-Jin Yoon. "Leveraging Future Relationship Reasoning for Vehicle Trajectory Prediction". *ICLR 2023*.
- Hyeokjun Kweon\*, Hyeonseong Kim\*, Yoonsu Kang\*, Youngho Yoon\*, Wooseong Jeong, Kuk-Jin Yoon. "Pixel-wise Warping for Deep Image Stitching". *AAAI 2023*.
- Youngrae Kim\*, Jinsu Lim\*, Hoonhee Cho\*, Minji Lee\*, Dongman Lee, Kuk-Jin Yoon, Ho-Jin Choi. "Efficient Reference-based Video Super-Resolution (ERVSR): Single Reference Image Is All You Need". *WACV 2023*.
- Seongyong Ahn, Inwook Shim, Jihong Min, Kuk-Jin Yoon. "EasyFuse: Easy-to-Learn Visible and Infrared Image Fusion Framework based on Unpaired Set". *Pattern Recognition Letters 2023*.
- Incheol Cho, Kichul Lee, Young Chul Sim, Jaeseok Jeong, Minkyu Cho, Heechan Jung, Mingu Kang, Yong-Hoon Cho, Seung Chul Ha, Kuk-Jin Yoon, Inkyu Park. "Deep Learning-based Gas Identification by Time-variant Illumination of a Single Micro LED-embedded Gas Sensor". *Light: Science & Applications 2023 (게재 승인, 누리집 자료 표기)*.
- Kichul Lee, Incheol Cho, Mingu Kang, Jaeseok Jeong, Minho Choi, Kie Young Woo, Kuk-Jin Yoon\*, Yong-Hoon Cho\*, Inkyu Park\*. "Ultra-Low-Power E-Nose System Based on Multi-Micro-LED-Integrated, Nanostructured Gas Sensors and Deep Learning". *ACS Nano 2023*.

**2022**

- Hyeokjun Kweon, Kuk-Jin Yoon. "Joint Learning of 2D-3D Weakly Supervised Semantic Segmentation". *NeurIPS 2022*.
- Tae-Woo Kim, Jeong-Min Lee, Lin Wang, Kuk-Jin Yoon. "Event-guided Deblurring of Unknown Exposure Time Videos". *ECCV 2022 (Oral)*.
- Changgyoon Oh\*, Wonjune Cho\*, Yujeong Chae\*, Daehee Park\*, Lin Wang, Kuk-Jin Yoon. "BIPS: Bi-modal Indoor Panorama Synthesis via Residual Depth-aided Adversarial Learning". *ECCV 2022*.
- Sung-Hoon Yoon\*, Hyeokjun Kweon\*, Jegyeong Cho, Shingeong Kim, Kuk-Jin Yoon. "Adversarial Erasing Framework via Triplet with Gated Pyramid Pooling Layer for Weakly Supervised Semantic Segmentation". *ECCV 2022*.
- Hoonhee Cho, Kuk-Jin Yoon. "Selection and Cross Similarity for Event-Image Deep Stereo". *ECCV 2022*.
- Minjun Kang, Jaesang Choe, Hywon Ha, Hae-Gon Jeon, Sunghoon Im, In So Kweon, Kuk-Jin Yoon. "Facial Depth and Normal Estimation using Single Dual-Pixel Camera". *ECCV 2022*.
- Pranjay Shyam, Kuk-Jin Yoon, Kyung-Soo Kim. "Multi-source Domain Alignment for Robust Segmentation in Unknown Targets". *IROS 2022*.
- Youngho Yoon, Inhcul Chung, Lin Wang, Kuk-Jin Yoon. "SphereSR: 360° Image Super-Resolution with Arbitrary Projection via Continuous Spherical Image Representation". *CVPR 2022 (Oral)*.
- Taeyeop Lee, Byeong-Uk Lee, Inkyu Shin, Jaesung Choe, Ukcheol Shin, In So Kweon, Kuk-Jin Yoon. "UDA-COPE: Unsupervised Domain Adaptation for Category-level Object Pose Estimation". *CVPR 2022*.
- Inkyu Shin, Yi-Hsuan Tsai, Bingbing Zhuang, Samuel Schulter, Buyu Liu, Sparsh Garg, In So Kweon, Kuk-Jin Yoon. "MM-TTA: Multi-Modal Test-Time Adaptation for 3D Semantic Segmentation". *CVPR 2022*.
- Pranjay Shyam, Kyung-Soo Kim\*, Kuk-Jin Yoon\*. "GIQE: Generic Image Quality Enhancement via N-th Order Iterative Degradation". *CVPR 2022*.
- YeongWoo Nam, Sayed Mohammad Mostafavi Isfahani, Kuk-Jin Yoon, Jonghyun Choi. "Stereo Depth from Events Cameras: Concentrate and Focus on the Future". *CVPR 2022*.
- Pranjay Shyam, Sumit Mishra, Kuk-Jin Yoon, Kyung-Soo Kim. "Infra Sim-to-Real: An Efficient Baseline and Dataset for Infrastructure based Online Object Detection and Tracking using Domain Adaptation". *IEEE Intelligent Vehicles Symposium (IV) 2022*.
- Hoonhee Cho, Kuk-Jin Yoon. "Event-image Fusion Stereo using Cross-modality Feature Propagation". *AAAI 2022*.
- Lin Wang, Kuk-Jin Yoon. "Deep Learning for HDR Imaging: State-of-the-Art and Future Trends". *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI) 2022*.
- Lin Wang, Tae-Kyun Kim, Kuk-Jin Yoon. "Joint Framework for Single Image Reconstruction and Super-Resolution With an Event Camera". *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI) 2022*.
- Joon-Kyu Han, Mingu Kang, Jaeseok Jeong, Incheol Cho, Ji-Man Yu, Kuk-Jin Yoon, Inkyu Park\*, Yang-Kyu Choi\*. "Artificial Olfactory Neuron for an In-Sensor Neuromorphic Nose". *Advanced Science 2022*.
- Mingu Kang, Incheol Cho, Jaeho Park, Jaeseok Jeong, Kichul Lee, Byeongju Lee, Dionisio Del Orbe Henriquez, Kuk-Jin Yoon\*, Inkyu Park\*. "High Accuracy Real-Time Multi-Gas Identification by a Batch-Uniform Gas Sensor Array and Deep Learning Algorithm". *ACS Sensors 2022*.
- Mohammad Mostafavi, Yeongwoo Nam, Jonghyun Choi, Kuk-Jin Yoon. "E2SRI: Learning to Super-Resolve Intensity Images From Events". *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI) 2022*.

**2021**

- Pranjay Shyam, Sandeep Singh Sengar, Kuk-Jin Yoon, Kyung-Soo Kim. "Lightweight HDR Camera ISP for Robust Perception in Dynamic Illumination Conditions via Fourier Adversarial Networks". *BMVC 2021*.
- Hyeokjun Kweon\*, Sung-Hoon Yoon\*, Hyeonseong Kim, Daehee Park, Kuk-Jin Yoon. "Unlocking the Potential of Ordinary Classifier: Class-specific Adversarial Erasing Framework for Weakly Supervised Semantic Segmentation". *ICCV 2021*.
- Lin Wang, Yujeong Chae, Kuk-Jin Yoon. "Dual Transfer Learning for Event-based End-task Prediction via Pluggable Event to Image Translation". *ICCV 2021*.
- Mohammad Mostafavi, Kuk-Jin Yoon, Jonghyun Choi. "Event-Intensity Stereo: Estimating Depth by the Best of Both Worlds". *ICCV 2021*.
- Haoang Li, Kai Chen, Kyungdon Joo, Pyojin Kim, Kuk-Jin Yoon, Zhe Liu, Yunhui Liu. "Learning Icosahedral Spherical Probability Map Based on Bingham Mixture Model for Vanishing Point Estimation". *ICCV 2021*.
- Pranjay Shyam, Sandeep Singh Sengar, Kuk-Jin Yoon, Kyung-Soo Kim. "Evaluating Region Modification based Data Augmentation Techniques for Low Level Vision Tasks". *IJCAI Workshop 2021; Workshop: Workshop on AI for Autonomous Driving · IJCAI 2021 Workshop*.
- Lin Wang, Yujeong Chae\*, Sung-Hoon Yoon\*, Tae-Kyun Kim, Kuk-Jin Yoon. "EvDistill: Asynchronous Events to End-task Learning via Bidirectional Reconstruction-guided Cross-modal Knowledge Distillation". *CVPR 2021*.
- Pranjay Shyam, Kuk-Jin Yoon, Kyung-Soo Kim. "Adversarially-trained Hierarchical Feature Extractor for Vehicle Re-identification". *ICRA 2021*.
- Pranjay Shyam, Kuk-Jin Yoon, Kyung-Soo Kim. "Towards Domain Invariant Single Image Dehazing". *AAAI 2021*.
- Lin Wang, Kuk-Jin Yoon. "Semi-supervised Student-Teacher Learning for Single Image Super-Resolution". *Pattern Recognition 2021*.
- Kwonoyoung Ryu, Kang-il Lee, Jegyeong Cho, Kuk-Jin Yoon. "Scanline Resolution-invariant Depth Completion using a Single Image and Sparse LiDAR Point Cloud". *IEEE Robotics and Automation Letters (RA-L) 2021*.
- Hoonhee Cho, Jaeseok Jeong, Kuk-Jin Yoon. "EOMVS: Event-based Omnidirectional Multi-View Stereo". *IEEE Robotics and Automation Letters (RA-L) 2021*.
- Ji-il Park, Yeongseok Lee, Eungyo Suh, Hyunyoung Jeon, Kuk-Jin Yoon, Kyung-Soo Kim. "Improvement of Optical Flow Estimation by Using the Hampel Filter for Low-End Embedded Systems". *IEEE Robotics and Automation Letters (RA-L) 2021*.
- Lin Wang, Kuk-Jin Yoon. "PSAT-GAN: Efficient Adversarial Attacks against Holistic Scene Understanding". *IEEE Transactions on Image Processing (TIP) 2021*.
- Lin Wang, Kuk-Jin Yoon. "Knowledge Distillation and Student-Teacher Learning for Visual Intelligence: A Review and New Outlooks". *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI) 2021*.
- S. Mohammad Mostafavi I., Lin Wang, Kuk-Jin Yoon. "Learning to Reconstruct HDR Images from Events, with Applications to Depth and Flow Prediction". *International Journal of Computer Vision (IJCV) 2021*.

## 특허

누리집 Publications 페이지 Patents 항목 가운데 등록일(등록 전이면 출원일)이 2021년 10월 13일 이후인 17건이다(등록 7건, 출원 10건). 날짜 칸은 등록일, 등록 전이면 출원일이다. 제목, 발명자, 국가, 번호, 상태(Active, Application)는 누리집 표기 그대로다.[^pubs]

- 2024.03.05 · 이미지 스티칭 학습 및 평가를 위한 이미지 데이터셋 생성 장치 및 그 방법 (발명자 윤국진, 권혁준, 강윤수, 정우성, 김현성, 박휘성; 국가 KR; 등록번호 10-2645640-0000; 등록일 2024.03.05; 출원번호 10-2021-0157112; 출원일 2021.11.15; 상태 Active)
- 2023.12.27 · 이벤트 카메라를 이용한 비디오 프레임 보간 장치 및 방법 (발명자 윤국진, 김태우; 국가 KR; 출원번호 10-2023-0192590; 출원일 2023.12.27; 상태 Application)
- 2023.12.26 · 분류기와 이미지 복원기 간의 적대적 학습을 통한 의미론적 영상 분할 방법 (발명자 윤국진, 윤성훈, 권혁준; 국가 KR; 출원번호 10-2023-0190705; 출원일 2023.12.26; 상태 Application)
- 2023.11.28 · 학습 장치, 학습 방법 및 이를 이용한 테스트 장치 및 테스트 방법 (발명자 윤국진, 정재우, 김지훈; 국가 KR; 출원번호 10-2023-0168434; 출원일 2023.11.28; 상태 Application)
- 2023.09.27 · 무인 이동체 계기판 인식 시스템 및 이의 동작 방법 (발명자 윤국진, 오창균, 조제경, 정유환; 국가 KR; 출원번호 10-2023-0131095; 출원일 2023.09.27; 상태 Application)
- 2023.08.23 · 다시점 영상 스티칭을 위한 색 보정 방법, 영상 합성 방법, 영상 처리 장치, 저장 매체 및 컴퓨터 프로그램 (발명자 윤국진, 권혁준, 정재석, 박휘성; 국가 KR; 등록번호 10-2571528-0000; 등록일 2023.08.23; 출원번호 10-2021-0167053; 출원일 2021.11.29; 상태 Active)
- 2023.08.23 · 이미지 스티칭을 위한 장치 및 그 방법 (발명자 윤국진, 권혁준, 강윤수, 정우성, 김현성, 박휘성; 국가 KR; 등록번호 10-2571530-0000; 등록일 2023.08.23; 출원번호 10-2021-0157069; 출원일 2021.11.15; 상태 Active)
- 2023.03.10 · 가스센서를 이용한 실시간 가스 종류 판별장치 및 방법 (발명자 박인규, 강민구, 윤국진, 조인철, 정재석; 국가 KR; 등록번호 10-2510314-0000; 등록일 2023.03.10; 출원번호 10-2021-0035601; 출원일 2021.03.19; 상태 Active)
- 2022.12.29 · 블러 이미지 복원 장치 및 그 방법 (발명자 윤국진, 김태우; 국가 KR; 출원번호 10-2022-0188515; 출원일 2022.12.29; 상태 Application)
- 2022.11.01 · 삼자 적대적 지우기 방식을 활용한 약-지도 의미론적 영역 분할 신경망 학습 방법 및 장치 (발명자 윤국진, 윤성훈, 권혁준, 조제경; 국가 KR; 출원번호 10-2022-0143872; 출원일 2022.11.01; 상태 Application)
- 2022.10.14 · 가변광조사를 이용한 광활성 가스센서의 가스종 식별방법 (발명자 박인규, 조인철, 윤국진, 조민규; 국가 KR; 등록번호 10-2456291-0000; 등록일 2022.10.14; 출원번호 10-2020-0168210; 출원일 2020.12.04; 상태 Active)
- 2022.09.06 · 전방향 영상의 딥러닝을 이용한 물체 감지 방법 및 장치, 그리고 이를 이용한 차량 자율 주행 방법 및 드론 자율 주행 방법 (발명자 윤국진, 이연건, 정재석, 윤종섭, 조원준; 국가 KR; 등록번호 10-2442545-0000; 등록일 2022.09.06; 출원번호 10-2020-0048643; 출원일 2020.04.22; 상태 Active)
- 2022.02.17 · 고해상도 강도 이미지 생성 방법 및 장치 (발명자 윤국진, Mostafavi I., S. Mohammad, 최종현; 국가 KR; 등록번호 10-2366187-0000; 등록일 2022.02.17; 출원번호 10-2020-0070044; 출원일 2020.06.10; 상태 Active)
- 2021.11.30 · Gas species identification method of photoactive gas sensor by using variable light radiation (발명자 Inkyu Park, Incheol Cho, Kuk-Jin Yoon, Minkyu Cho; 국가 US; 출원번호 18/265,379; 출원일 2021.11.30; 상태 Application)
- 2021.11.30 · Gas species identification method of photoactive gas sensor by using variable light radiation (발명자 Inkyu Park, Incheol Cho, Kuk-Jin Yoon, Minkyu Cho; 국가 EU; 출원번호 21900960.2; 출원일 2021.11.30; 상태 Application)
- 2021.10.27 · 카메라와 라이다를 이용한 정밀한 깊이 정보 추정 시스템 및 그 방법 (발명자 윤국진, 류권영, 이강일, 조제경; 국가 KR; 출원번호 10-2021-0144185; 출원일 2021.10.27; 상태 Application)
- 2021.10.13 · 약-지도 의미론적 영역 분할 신경망 학습 방법 및 장치 (발명자 윤국진, 윤성훈, 권혁준, 김현성, 박대희; 국가 KR; 출원번호 10-2021-0135458; 출원일 2021.10.13; 상태 Application)

## 연구 과제

누리집 Projects 페이지 과제 50건 가운데 진행 중(Ongoing)이거나 2021년 10월 이후에 끝난 39건이다(진행 중 13건, 완료 26건). 과제 이름 앞의 (PI)는 누리집이 교수의 역할로 적은 표기다. 기간, 지원(Funding), 기관(Organization), 상태는 누리집 표기 그대로다.[^projects]

- Global Humanities and Social Sciences Convergence Research: Development of a Multimodal AI-based Reading Disability Diagnosis and Learning Support System (기간 09/2026 - 02/2027; 지원 Ministry of Education; 기관 National Research Foundation of Korea (NRF), Inha University; 상태 Ongoing)
- (PI) Long-Horizon Agentic AI Research (기간 07/2026 - 12/2031; 지원 Ministry of Science and ICT; 기관 National Research Foundation of Korea (NRF); 상태 Ongoing)
- Development of Outpainting AI and Spatial Expansion Technology for Utilizing Archive Video Contents (기간 04/2026 - 12/2028; 지원 Ministry of Science and ICT; 기관 Institute for Information & Communications Technology Planning & Evaluation (IITP); 상태 Ongoing)
- Development of High-precision Hand-crafting and Service Technologies based on Physical AI (기간 04/2026 - 12/2026; 지원 Ministry of Science and ICT; 기관 Institute for Information & Communications Technology Planning & Evaluation (IITP); 상태 Ongoing)
- (PI) Multi-modal Sensor based Self-improving Autonomous Driving Research (기간 03/2026 - 02/2029; 지원 Ministry of Science and ICT; 기관 National Research Foundation of Korea (NRF); 상태 Ongoing)
- (PI) GS E&C-KAIST Joint R&D on Urban AI Technologies for Future Cities (기간 06/2025 - 08/2028; 지원 GS E&C; 상태 Ongoing)
- (PI) Development of a C-arm X-ray Video Engine (기간 07/2025 - 12/2026; 지원 DK Medical Systems; 상태 Ongoing)
- (PI) Large-Scale Language Model Innovation Research Group (기간 07/2025 - 12/2029; 지원 Ministry of Science and ICT (InnoCore); 기관 KAIST; 상태 Ongoing)
- Bio-Embodied Physical AI Research Group (기간 07/2025 - 12/2029; 지원 Ministry of Science and ICT (InnoCore); 기관 DGIST; 상태 Ongoing)
- (PI) AI Robot-Based Digital Twin Care Platform for Continuous Integrated Care of the Elderly (기간 05/2025 - 02/2026; 지원 Ministry of Health and Welfare; 기관 Korea Health Industry Development Institute (KHIDI); 상태 Completed)
- (PI) Development of a Generative AI-Based 16-bit HDR Solution (기간 05/2025 - 04/2026; 지원 Samsung Electronics; 상태 Completed)
- (PI) Automated Particle Analysis Technology Using Cathode SEM Images (기간 03/2025 - 10/2025; 지원 LG Energy Solution; 상태 Completed)
- (PI) Computer Vision Research Based on Multimodal Cameras for Robust Autonomous Driving (기간 03/2022 - 02/2026; 지원 Ministry of Science and ICT; 기관 National Research Foundation of Korea (NRF); 상태 Completed)
- (PI) AI Research Hub Project (기간 07/2024 - 12/2028; 지원 Ministry of Science and ICT; 기관 Institute for Information & Communications Technology Planning & Evaluation (IITP); 상태 Ongoing)
- (PI) Military-Specialized AI Curriculum Development and Operation (AI Leadership, Policy, Project Course) (기간 06/2024 - 12/2026; 지원 Ministry of Science and ICT; 기관 Institute for Information & Communications Technology Planning & Evaluation (IITP); 상태 Ongoing)
- Development of Autonomous Driving Connectivity Technology Based on Sensor Infrastructure Cooperation (기간 01/2024 - 06/2027; 지원 Ministry of Trade, Industry and Energy (MOTIE); 기관 LG Electronics; 상태 Ongoing)
- (PI) Development of a Humanoid Robot Pilot Based on Natural Language Processing Knowledge Base (기간 01/2022 - 05/2027; 지원 Ministry of National Defense; 기관 Agency for Defense Development (ADD); 상태 Ongoing)
- (PI) Graph-Based Approach to 3D Feature Point Tracking Algorithms of Event Cameras (기간 01/2025 - 06/2025; 지원 KAIST; 상태 Completed)
- (PI) Development of Data Augmentation and Sensor Fusion Technologies for Robust Autonomous Driving (기간 12/2024 - 02/2026; 지원 42dot; 상태 Completed)
- (PI) Samsung Electronics DS Division Strategic Industry-Academia Project (기간 09/2023 - 09/2025; 지원 Samsung Electronics; 상태 Completed)
- (PI) Object Prediction Model Using Surrounding Environment Perception and Map Information (기간 06/2024 - 05/2025; 지원 Hyundai NGV; 상태 Completed)
- Development of AI Sub-Modules for Intelligent Baggage X-ray Interpretation Training System (기간 03/2023 - 06/2024; 기관 National Research Foundation of Korea (NRF); 상태 Completed)
- (PI) Development of Core Technologies for Autonomous Driving in Unstructured Off-Road Environments (기간 07/2023 - 06/2026; 지원 Hanwha Aerospace; 상태 Completed)
- AI Research for Intelligent X-ray Luggage Scanning Systems (기간 07/2021 - 06/2024; 지원 National Research Foundation of Korea (NRF); 상태 Completed)
- Development of a 2kg-Class Small EOTS for Drones (기간 01/2021 - 11/2023; 지원 EO Systems; 상태 Completed)
- Development of Real-Time Hologram Acquisition and Preprocessing Technology for 5G Services Based on Deep Learning (기간 01/2023 - 12/2023; 기관 KETI; 상태 Completed)
- (DeepView - Main/Part 1) Development of a High-Performance Visual Discovery Platform (기간 01/2023 - 02/2024; 기관 ETRI; 상태 Completed)
- (PI) Development of Artificial Intelligence Technology for Continuous Self-Improvement (기간 01/2023 - 12/2023; 기관 IITP; 상태 Completed)
- (PI) Domain Adaptation for AI-based Detection and Monitoring (기간 10/2022 - 09/2023; 지원 LIG Nex1; 상태 Completed)
- (PI) Low-level Image Fusion for Autonomous Driving (기간 11/2022 - 11/2023; 지원 Hyundai Motors; 상태 Completed)
- (PI) Development of an Iron Plate Abrasion Rate Recognition System (기간 05/2021 - 01/2022; 지원 Samsung Heavy Industry; 상태 Completed)
- (PI) Intelligent Focus Adjustment for Dual Pixel Cameras (기간 09/2020 - 09/2023; 지원 Samsung Advanced Institute of Technology; 상태 Completed)
- (PI) Deep-learning-based 5G Real-time Hologram Generation and Processing (기간 2020 - 2023; 기관 IITP; 상태 Completed)
- Research on Self-improving AI (기간 04/2020 - 12/2023; 기관 National Research Foundation of Korea (NRF); 상태 Completed)
- Deep View - Research on Vision- and Learning-based Scene Understanding and Event Forecasting (기간 2019 - 2023; 기관 MSIP; 상태 Completed)
- Research on Autonomous Multi-agent CPS (기간 12/2019 - 12/2024; 기관 Agency for Defense Development (ADD); 상태 Completed)
- Research on Mapping and Perception (기간 2019 - 2022; 지원 NaverLabs; 상태 Completed)
- Development of Quadruped Robot for Surveillance, Reconnaissance, and Search Missions (기간 12/2019 - 11/2024; 지원 Defense Acquisition Program Administration (DAPA); 기관 Agency for Defense Development (ADD); 상태 Completed)
- (PI) Research on Event Camera-based Computer Vision Algorithms for Visual Intelligence (기간 03/2018 - 02/2022; 지원 Ministry of Science and ICT; 기관 National Research Foundation of Korea (NRF); 상태 Completed)

## 수상

누리집 News 페이지에서 award로 분류된 소식 가운데 2021년 10월 13일 이후의 6건이다. 제목 문구는 누리집 그대로다. 교수의 수상은 위 「교수와 전문 분야」에 적었다.[^news]

- 2025-03-18 · Winning the Test of Time Award at IEEE/CVF WACV 2025
- 2024-12-03 · QIF 2024 South Korea: Two Papers from Visual Intelligence Lab Selected for Winners
- 2023-03-02 · Won a Bronze Prize at Signal Proscessing Division of 29th Samsung Humantech Paper Award
- 2023-02-10 · Won a Gold Prize at 35th Workshop on Image Processing and Understanding (IPIU 2023)
- 2022-04-01 · Winning the 2nd place in PBVS SSHODC 2022 challenge
- 2022-02-10 · VILab Wins Grand Prize and Gold Prize at 34th Workshop on Image Processing and Understanding (IPIU 2022)

## 소식

누리집 News 페이지 소식 가운데 2021년 10월 13일 이후의 논문 채택·게재(publication) 30건, 교수 임명·학술 활동(service) 5건, 졸업생 진로(career) 1건이다. 같은 기간의 새 학생 입학 환영 글과 학위수여식 글은 연구실 생활 글이라 싣지 않았다. 제목 문구는 누리집 그대로다.[^news]

- 2026-09-25 · Paper accepted to IEEE RA-L
- 2026-09-25 · Papers accepted to NeurIPS 2026
- 2026-06-18 · Papers accepted to ECCV 2026
- 2026-02-22 · Papers accepted to CVPR 2026
- 2026-01-26 · Papers accepted to ICLR 2026
- 2025-12-17 · Professor Kuk-Jin Yoon Appointed as Interim Dean of KAIST College of AI
- 2025-12-05 · Papers published to TPAMI 2025
- 2025-11-06 · Papers accepted to WACV 2026
- 2025-09-18 · A Paper accepted to NeurIPS 2025
- 2025-06-26 · Papers accepted to ICCV 2025
- 2025-06-20 · A Paper accepted to IROS 2025
- 2025-02-27 · Papers accepted to CVPR 2025
- 2025-02-23 · Hyeokjun Kweon, Daehee Park, and Sung-Hoon Yoon Appointed as University Professors
- 2025-02-19 · Professor Kuk-Jin Yoon Appointed as Deputy Director of KAIST AI Institute
- 2025-02-19 · Professor Kuk-Jin Yoon Appointed as Area Chair for ICML 2025 and NeurIPS 2025, and Senior Area Chair for ICCV 2025
- 2025-01-23 · A Paper accepted to ICLR 2025
- 2024-10-29 · A Paper accepted to WACV 2025
- 2024-10-19 · Professor Kuk-Jin Yoon Appointed as an Organizer for the 2025 HMG Autonomous Driving Challenge
- 2024-09-27 · Papers accepted to NeurIPS 2024
- 2024-07-02 · Papers accepted to ECCV 2024
- 2024-02-27 · Papers accepted to CVPR 2024
- 2023-12-10 · Papers accepted to AAAI 2024
- 2023-10-21 · A Paper accepted to WACV 2024
- 2023-10-15 · A Paper accepted to 3DV 2024
- 2023-07-14 · Papers accepted to ICCV 2023
- 2023-04-13 · Professor Kuk-Jin Yoon has been appointed as an Associate Editor for IEEE TPAMI
- 2023-02-28 · Papers accepted to CVPR 2023
- 2023-01-22 · A Paper accepted to ICLR 2023
- 2022-11-19 · A Paper accepted to AAAI 2023
- 2022-09-15 · A Paper accepted to NeurIPS 2022
- 2022-08-17 · A Paper accepted to WACV 2023
- 2022-07-31 · A Paper accepted to IROS 2022
- 2022-07-04 · Papers accepted to ECCV 2022
- 2022-03-03 · Papers accepted to CVPR 2022
- 2021-12-01 · A Paper accepted to AAAI 2022
- 2021-10-16 · A Paper accepted to BMVC 2021

## 연락과 위치

- 주소: KAIST Mechanical Engineering Bldg (N7-4), 291, Daehak-ro, Yuseong-gu, Daejeon, Republic of Korea(누리집 표기)[^contact]
- 교수실: N7-4 #6101, 연구실: N7-4 #5123[^contact]
- 전화: 교수실 (042) 350 7319, 연구실 (042) 350 7359[^contact]
- 교수 이메일: kjyoon@kaist.ac.kr[^contact][^mepop]
- 대학원 지원: Faculty 페이지는 대학원생·인턴·박사후연구원으로 함께하고 싶으면 CV와 연구 관심을 짧게 적어 교수에게 이메일로 보내라고 안내한다.[^faculty]
[^p1]: H. Cho 외, K.-J. Yoon, Advances in Neural Information Processing Systems 38, 127297-127318 (2025). <https://doi.org/10.52202/085713-3828> 초록 기준(arXiv 판).
[^p2]: G. Lee 외, K.-J. Yoon, 2025 IEEE/CVF International Conference on Computer Vision (ICCV), 1-12 (2025). <https://doi.org/10.1109/iccv51701.2025.02657> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J.-Y. Kang, H. Cho, K.-J. Yoon, IEEE Transactions on Pattern Analysis and Machine Intelligence 48, 4098-4113 (2026). <https://doi.org/10.1109/tpami.2025.3645734> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: H. Cho, J.-Y. Kang, Y. Kim, K.-J. Yoon, 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 27197-27210 (2025). <https://doi.org/10.1109/cvpr52734.2025.02533> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: Y. Chae, H. Kim, K.-J. Yoon, 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 15162-15172 (2024). <https://doi.org/10.1109/cvpr52733.2024.01436> 초록 기준(학회 논문집 페이지 게시 초록).
[^p6]: Y. Yoon, K.-J. Yoon, 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 12428-12438 (2023). <https://doi.org/10.1109/cvpr52729.2023.01196> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: H. Kweon, K.-J. Yoon, 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 19499-19509 (2024). <https://doi.org/10.1109/cvpr52733.2024.01844> 초록 기준(학회 논문집 페이지 게시 초록).
[^p8]: Y. Yoon, I. Chung, L. Wang, K.-J. Yoon, 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 5667-5676 (2022). <https://doi.org/10.1109/cvpr52688.2022.00559> 초록 기준(Semantic Scholar 등록 초록).
[^home]: VILab 누리집 첫 화면 <https://vi.kaist.ac.kr/> (연구실 소개와 핵심 연구 분야 네 가지, 2026-10-23 열람)
[^research]: VILab 누리집 Research 페이지 <https://vi.kaist.ac.kr/pages/research/> (연구 분야 12개와 세부 주제의 설명, 2026-10-23 열람)
[^faculty]: VILab 누리집 Faculty 페이지 <https://vi.kaist.ac.kr/pages/faculty/> (교수 소개 글, 경력, 자문, 학력, 수상, 학술·공공 봉사, 2026-10-23 열람)
[^cv]: 윤국진 교수 CV(PDF, 누리집 People·Faculty 페이지 연결) <https://vi.kaist.ac.kr/assets/docs/Prof_Kuk-Jin_Yoon_CV.pdf> (연구 관심, 경력, 논문·특허·과제 목록, 2026-10-23 열람)
[^people]: VILab 누리집 People 페이지 <https://vi.kaist.ac.kr/pages/people/> (교수 카드, 현재 구성원 34명(행정 직원 1명 포함), 졸업생 카드, 2026-10-23 열람)
[^pubs]: VILab 누리집 Publications 페이지 <https://vi.kaist.ac.kr/pages/publications/> (연도 구역 2026–2021과 -2020, 논문·워크숍 논문·특허, 2026-10-23 열람)
[^projects]: VILab 누리집 Projects 페이지 <https://vi.kaist.ac.kr/pages/projects/> (과제 50건의 기간·지원·기관·상태, 2026-10-23 열람)
[^news]: VILab 누리집 News 페이지 <https://vi.kaist.ac.kr/pages/news/> (소식 90건, 2026-10-23 열람)
[^contact]: VILab 누리집 Contact 페이지 <https://vi.kaist.ac.kr/pages/contact/> (전화, 주소, 교수실·연구실 호실, 이메일, 2026-10-23 열람)
[^me]: KAIST 기계공학과 교수진 목록 2쪽 <https://me.kaist.ac.kr/team/team_010100.html?page=2> (연구분야, 연구실, 최종학위, 2026-10-23 열람)
[^mepop]: KAIST 기계공학과 교수 소개(윤국진) <https://me.kaist.ac.kr/pop/team.html?uid=39&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 이메일, 교수실, 전화, 2026-10-23 열람)
[^mer1]: KAIST 기계공학과 연구분야 로보틱스/제어/모빌리티 페이지 <https://me.kaist.ac.kr/research/research_010100.html> (교수의 연구주제와 주요 응용 산업, 2026-10-23 열람)

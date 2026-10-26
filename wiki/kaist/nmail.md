# 뉴로-기계 증강지능 연구실 (Neuro-Machine Augmented Intelligence Lab, NMAIL)

**KAIST 전산학부 · 조성호 교수**

- 분야: 지능 로봇·로봇 학습, 착용형·증강 지능, 뇌-컴퓨터 인터페이스, 헬스케어 인공지능
- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 신경 인터페이스·뇌-컴퓨터 인터페이스[^bci][^p2][^p3], 착용형 로봇·외골격[^soft][^p1], 재활·보조·접근성 기술[^p1][^p2], 컴퓨터 비전[^vis][^p4], 3차원 복원·인식[^vis][^p5][^p8], 과학·공학 AI[^chemo][^p7], 로봇 조작·파지[^p6], 상태 추정·필터링(데이터 동화)[^p8]
- 홈페이지: <http://nmail.kaist.ac.kr/wordpress/>
- 근거와 출처: [NMAIL 근거 페이지](nmail-sources.md)

> 사람의 지적·인지적·신체적 능력을 키우는 것을 목표로, 로봇의 지능, 뇌 신호로 기계를 움직이는 인터페이스, 몸에 다는 센서와 의료·화학 측정 자료를 읽어 내는 인공지능을 함께 연구하는 연구실이다.[^home][^vision]

## 무엇을 연구하나

연구실은 사람의 능력을 지적·인지적·신체적으로 키우는(augment) 것을 목표로 내세우고, 사람의 지능과 기계의 지능을 매끄럽게 이으면 사람을 넘어서는 지능에 이를 수 있다고 믿는다고 소개한다.[^home] Vision 페이지는 지적·신체적 능력이 키워진 「메타 휴먼」을 만드는 것을 연구실의 비전으로 적고, 이를 위해 자율 기계, 착용형 컴퓨팅, 뇌-컴퓨터 인터페이스(BCI, 뇌 신호를 읽어 컴퓨터나 기계를 움직이는 기술), 증강현실 기반 인터페이스 같은 기술을 연구해 왔으며 이 기술들을 하나로 묶어 사람의 능력을 키우려 한다고 적는다.[^vision] 같은 페이지는 기술이 사람을 앞지르거나 대신하기보다 사람을 돕고 사람의 능력을 키우는 데 쓰여야 한다고 밝힌다.[^vision]

누리집은 연구를 세 영역으로 나눈다.[^home] 로봇 지능(Robotic Intelligence)에는 로봇을 위한 인공지능, 시각 지능, 행동 지능, 소프트 로보틱스(부드러운 소재로 만든 로봇)가, 뉴로-하이브리드 지능(Neuro-Hybrid Intelligence)에는 뇌-컴퓨터 인터페이스, 감성 지능, 동물 컴퓨팅이, 증강 지능(Augmented Intelligence)에는 감각 지능, 헬스케어 인공지능, 심층 분석이 든다.[^home] 연구 메뉴는 이 밖에 근육 신호와 기계를 잇는 인터페이스(Muscle-Machine Interfaces), 물리적 몸체 지능(Physically Embodied Intelligence), 딥 케모메트릭스(Deep Chemometrics, 화학 측정 자료를 딥러닝으로 분석하는 연구)를 따로 둔다.[^home]

대표 논문으로 보면 연구는 여섯 갈래다. 첫째, 뇌졸중 생존자의 손 재활을 돕는 소프트 로봇 장갑과 영상 기반 의도 인식이다(대표 논문 1).[^p1] 둘째, 뇌파(EEG, 머리에서 재는 뇌의 전기 신호)로 휠체어를 움직이거나 운동 상상을 구분하는 뇌-컴퓨터 인터페이스다(대표 논문 2, 3).[^p2][^p3] 셋째, 두 영상에서 같은 지점을 찾는 영상 정합과 여러 장의 사진으로 3차원 모델을 만드는 다시점 스테레오(MVS)다(대표 논문 4, 5).[^p4][^p5] 넷째, 서로 다른 로봇 손에 적응하는 로봇 파지 학습이다(대표 논문 6).[^p6] 다섯째, 표면증강 라만 분광(SERS) 신호를 딥러닝으로 분석해 세균을 가려내는 연구다(대표 논문 7).[^p7] 여섯째, 몸에 단 적은 수의 관성 측정 장치(IMU)로 온몸의 움직임을 추정하는 연구다(대표 논문 8).[^p8]

## 주요 연구 주제

### 1. 손 재활을 돕는 소프트 웨어러블 로봇

손 기능이 떨어진 뇌졸중 생존자가 여러 손 자세를 연습하도록, 팔의 움직임과 손이 물체와 닿는 모습을 영상·깊이 자료로 분석해 원하는 손 자세를 예측하고, 손가락 하나하나를 굽히고 펴게 거드는 소프트 로봇 장갑으로 그 자세를 돕는 재활 시스템을 만들었다.[^p1] 연구실 연구 소개 글은 이 연구를 KAIST 기계공학과 Hyung Soon Park 교수 연구실과의 공동 연구로 적는다.[^r-rehab] 누리집의 Soft Robotic Intelligence 분류에는 힘줄-덮개 구조(관 안에 넣은 줄을 당겨 손가락에 힘을 전하는 방식)의 소프트 착용형 로봇 장갑으로 모양이 변하는 물체를 잡는 연구 등 착용형 손 로봇 연구가 함께 모여 있다.[^soft] 대표 논문 1.

### 2. 뇌-컴퓨터 인터페이스

몸을 움직이는 상상(운동 상상)에서 나오는 뇌파를 실시간으로 읽어 휠체어를 모는 시스템에, 라이다(LiDAR, 레이저로 주변까지의 거리를 재는 센서)로 파악한 주변 환경을 함께 고려하는 공유 제어를 넣었다.[^p2] 여러 사람의 뇌파 자료로 만든 분류 모델을 새 사용자에게 맞출 때, 자료를 준 사람마다 새 사용자와의 차이를 따져 영향을 선택적으로 제한하는 도메인 적응 방법도 내놓았다.[^p3] 논문 목록에는 귀 뇌파(ear-EEG) 기술과 그 응용을 정리한 리뷰와, 말하는 상상과 귀 뇌파로 가전을 제어하는 BCI 시스템 논문도 있다.[^pubs] 누리집의 Brain-Computer Interfaces 분류에는 귀 뇌파로 말하는 상상을 구분하는 BCI, 뇌파 반응으로 로봇의 행동을 학습시키는 시스템, 몰입형 가상현실을 쓴 운동 상상 훈련 같은 연구 소개 글이 모여 있다.[^bci] 대표 논문 2, 3.

### 3. 시각 지능과 3차원 복원

장면 변화가 크거나 무늬가 적은 영상에서도 두 영상의 같은 지점을 찾도록, 영상을 의미 단위(토픽)의 분포로 나타내는 영상 정합 방법을 만들었다.[^p4] 밤·악천후·계절 변화 속에서 영상으로 카메라의 위치와 방향을 찾는 시각적 위치 추정 연구도 연구 소개 글에 올라 있다.[^r-semidense] 3차원 복원에서는 앞서 추정한 깊이 정보를 활용해 실시간으로 정밀한 3차원 모델을 만드는 온라인 다시점 스테레오 방법을 내놓았고,[^p5] 연구 소개 글은 부분적으로 만들어진 모델을 보며 촬영 경로를 계속 다시 계획하는 3차원 모델링 연구를 함께 소개한다.[^r-mvs] 누리집의 Visonal Intelligence 분류에는 영상 정합, 시각적 위치 추정, 다시점 스테레오 3차원 복원, 로봇 파지 연구 소개 글이 함께 모여 있다.[^vis] 대표 논문 4, 5.

### 4. 로봇 파지 학습

한 가지 그리퍼(로봇 손)로 학습한 파지 모델을 다른 그리퍼에 옮기려면 자료를 새로 만들고 다시 학습해야 하는 문제를 풀려고, 대략의 파지 자세를 먼저 예측하고 그리퍼에 맞춘 동작을 예측한 뒤 강화학습으로 다듬는 하이브리드 구조를 만들었다.[^p6] 논문 목록에는 로봇 조작 지식을 지식 그래프로 정리해 물체의 의미에 맞게 잡는 방법을 배우는 연구도 있다.[^pubs] 대표 논문 6.

### 5. 라만 분광 신호의 딥러닝 분석

연구실은 주변 매질의 신호가 섞인 SERS 스펙트럼을 딥러닝 모델로 분석해, 세균을 따로 분리하지 않고도 두 종류의 세균과 매질을 가려내는 방법을 내놓았다.[^p7] 연구 소개 글은 혈액 속 표지 물질의 SERS 신호를 딥러닝으로 분석해 알츠하이머병을 진단하는 플랫폼 연구를 KAIST 신소재공학과 Yeon Sik Jung 교수 연구실과의 공동 연구로 소개한다.[^r-sers] 누리집의 Deep Chemometrics 분류에는 이 두 연구 소개 글이 있다.[^chemo] 대표 논문 7.

### 6. 착용형 센서로 사람 동작을 읽는 인공지능

몸에 단 몇 개의 관성 측정 장치 자료에서 온몸의 움직임과 그 불확실성을 함께 추정하는 확률 모델을 만들었다.[^p8] 연구 소개 글에는 스마트워치를 라켓을 잡지 않은 팔에 차고 테니스 샷을 감지·분류하는 시스템,[^r-tennis] 손에 직접 인쇄하는 나노메시 센서와 메타 학습을 묶어 손동작을 빠르게 알아보는 연구도 있다.[^r-nanomesh] 대표 논문 8.

## 대표 논문

랩 Journal Publications·Conference Proceedings 목록의 2021–2026년 논문 가운데 조성호 교수가 마지막 저자인 논문을, 여섯 연구 갈래에 고르게 담도록 골랐다. 누리집 목록은 교신저자를 따로 표시하지 않는다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2024 | [Multiple Hand Posture Rehabilitation System Using Vision-Based Intention Detection and Soft-Robotic Glove](https://doi.org/10.1109/tii.2023.3348826) · IEEE Transactions on Industrial Informatics | 손 기능이 떨어진 뇌졸중 생존자가 일상생활에 필요한 여러 손 자세를 스스로 연습하도록 돕는 손 재활 시스템이다. 근전도·뇌파 같은 생체 신호로 여러 손 자세에 대한 의도를 알아내기는 어려워, 실시간으로 분류하면 성능이 낮았다. 이 연구는 사용자의 팔 움직임과 손이 물체와 닿는 모습을 담은 영상·깊이 자료를 분석해 원하는 손 자세를 예측하는 영상 기반 의도 인식 틀과, 손가락 하나하나를 굽히고 펴게 돕는 8자유도 소프트 로봇 장갑을 함께 만들었다. 사용자가 원하는 자세를 만들려고 힘을 쓸 때 장갑이 손가락 움직임을 거들어 능동 재활을 돕는다. 일상생활에서 가장 자주 쓰이는 다섯 손 자세로 물건을 집어 옮기는 실시간 과제에서, 건강한 사람 5명과 뇌졸중 생존자 3명의 원하는 자세를 평균 정확도 각각 90.4 ± 3.6%, 80.3 ± 4.6%로 예측하고 거들었으며, 이전 연구들이 보고한 방법보다 나았다.[^p1] | 1저자 E. Rho, 마지막 저자 조성호 (9명) |
| 2 | 2023 | [Asynchronous Motor Imagery BCI and LiDAR-Based Shared Control System for Intuitive Wheelchair Navigation](https://doi.org/10.1109/jsen.2023.3281756) · IEEE Sensors Journal | 운동 상상(몸을 움직이는 상상)으로 생기는 뇌 신호를 실시간으로 분석해 휠체어를 움직이는 뇌 제어 이동 시스템이다. 몸을 움직이지 않아도 되므로 운동 장애가 있는 환자도 운전할 수 있게 하려는 것이다. 사용자가 원하는 때에 명령을 내는 비동기식 BCI는 오류가 나기 쉬워, 뇌파와 함께 계속 갱신되는 주변 환경 정보를 고려하는 공유 제어를 넣어 운전자가 정확히 조작하지 않아도 주행 성능이 나아지게 했다. 라이다와 관성 측정 장치(IMU)를 단 휠체어로 실제 환경에서 공유 제어를 쓸 때와 쓰지 않을 때, 뇌 제어와 키보드로 각각 운전하는 비교 실험을 했다. 참가자 5명 가운데 비동기식 BCI만으로 주행 과제에 실패한 3명도 공유 제어로는 과제를 마쳤고, 걸린 시간과 안전 면에서 뇌 신호 운전과 널리 쓰는 입력 장치 운전 사이의 차이가 줄었다.[^p2] | 1저자 J. W. Choi, 마지막 저자 조성호 (4명) |
| 3 | 2024 | [Selective Multi-Source Domain Adaptation Network for Cross-Subject Motor Imagery Discrimination](https://doi.org/10.1109/tcds.2023.3314351) · IEEE Transactions on Cognitive and Developmental Systems | 뇌파 BCI로 운동 상상을 구분하려면 사용자가 많은 자료를 모으는 데 큰 수고가 든다. 이를 줄이는 한 방법은 여러 사람의 자료로 분류 모델을 만들고 새 사용자의 정답 없는 자료만으로 모델을 맞추는 비지도 도메인 적응(학습한 모델을 다른 자료 분포에 맞추는 방법)이다. 그런데 운동 상상의 뇌 패턴은 사람마다 달라, 여러 사람의 자료를 쓸 때는 각 사람 자료의 믿을 만한 정도를 따져야 한다. 이 연구는 자료를 준 사람마다 도메인 적응을 하고 새 사용자와의 차이에 따라 각자의 영향을 선택적으로 제한하는 Selective-MDA를 내놓았다. 공개 데이터셋 두 개(BCI Competition IV IIa, Autocalibration and Recurrent Adaptation)로 평가하고, 차이 기준으로 고른 사람 수에 따라 구분 성능이 어떻게 달라지는지 비교했다. 여러 사람의 자료로 학습할 때 어떤 사람의 자료를 고르느냐가 성능에 영향을 준다는 점을 보였다.[^p3] | 1저자 J. Lee, 마지막 저자 조성호 (3명) |
| 4 | 2024 | [TopicFM+: Boosting Accuracy and Efficiency of Topic-Assisted Feature Matching](https://doi.org/10.1109/tip.2024.3473301) · IEEE Transactions on Image Processing | 장면 변화가 크거나 무늬가 적은 어려운 상황에서 두 영상의 같은 지점을 찾는 영상 정합을, 계산 효율에 무게를 두고 다뤘다. 트랜스포머(자료의 모든 부분 사이 관계를 계산하는 신경망 구조)로 장면 전체의 맥락을 담으려던 이전 방법은 계산이 많이 들고, 공간 구조나 의미 있는 모양 같은 높은 수준의 맥락을 충분히 담지 못할 수 있었다. 이 연구는 각 영상을 의미 구조를 나타내는 토픽들의 다항 분포로 나타내는 토픽 모델링 방식으로 맥락을 담아, 변별력 있는 특징을 얻는다. 거친 단계의 정합에서는 정해진 크기의 토픽과 작은 특징에만 주의(attention) 층을 써서 효율을 높이고, 세밀한 단계에서는 동적 특징 다듬기 망으로 결과를 정밀하게 했다. 앙상블 기법 없이 Image Matching Challenge 2023에서 상위 9%에 들었고, 다른 트랜스포머 기반 방법보다 계산 비용을 약 50% 줄였다.[^p4] | 1저자 K. T. Giang, 마지막 저자 조성호 (3명) |
| 5 | 2023 | [Prior depth-based multi-view stereo network for online 3D model reconstruction](https://doi.org/10.1016/j.patcog.2022.109198) · Pattern Recognition | 실시간으로 정밀한 3차원 모델을 만드는 온라인 다시점 스테레오(MVS, 여러 위치에서 찍은 사진으로 깊이를 계산하는 방법) 문제를 다뤘다. 이전 연구 대부분은 짧은 시간 동안 찍은 여러 영상으로 깊이 지도를 차례로 추정하는 모션 스테레오 방식을 썼는데, 빨리 계산하려고 영상을 줄이거나 단순한 알고리즘을 써서 만들어진 3차원 모델이 부정확했다. 이 연구는 앞서 차례로 추정한 깊이들에서 사전 깊이 정보를 끌어내 깊이 지도를 더 정밀하게 추정하는 온라인 MVS 방법을 내놓았다. 사전 깊이에 바탕한 가시성 정보로 비용 볼륨(후보 깊이마다 영상 사이 불일치를 담은 자료)을 만들고 사전 깊이를 그 안에 합쳐, 스테레오 정합 성능과 추정한 깊이의 완전성을 크게 높였다. 실험에서 다른 MVS·모션 스테레오 방법보다 나았고, 특히 3차원 모델의 완전성을 크게 높였다.[^p5] | 1저자 S. Song, 마지막 저자 조성호 (4명) |
| 6 | 2023 | [HybGrasp: A Hybrid Learning-to-Adapt Architecture for Efficient Robot Grasping](https://doi.org/10.1109/lra.2023.3329622) · IEEE Robotics and Automation Letters | 로봇 조작은 여러 분야에서 쓰이지만 로봇 파지 시스템의 적응성을 높이는 연구는 적었다. 대부분의 연구는 그리퍼(로봇 손) 하나를 기준으로 모델을 만들어 그리퍼의 복잡성과 일반성 사이에서 한쪽을 내주게 된다. 한 그리퍼로 미리 학습한 모델을 다른 그리퍼에 옮기려면 새 데이터셋을 만들고 파지를 다시 학습해야 해 비효율적이고 규모를 키우기 어렵다. 이 연구는 서로 다른 그리퍼 설계에 효율적으로 적응하도록 배우는 하이브리드 구조를 내놓았다. 평행 그리퍼 모델로 대략의 파지 자세를 예측하고, 합성곱 신경망으로 적응 동작을 예측한 뒤, 강화학습으로 그 동작을 다듬는 세 단계다. 생성한 데이터셋과 실제 환경 모두에서 기존 방법보다 파지 성능이 크게 나아졌다.[^p6] | 1저자 J. Mun, 마지막 저자 조성호 (7명) |
| 7 | 2022 | [Separation-free bacterial identification in arbitrary media via deep neural network-based SERS analysis](https://doi.org/10.1016/j.bios.2022.113991) · Biosensors and Bioelectronics | 식품 안전 분석과 감염병 진단에는 여러 세균에 두루 쓰이고 빠른 세균 검출 기술이 필요하다. 표면증강 라만 분광(SERS)은 다양한 미생물을 검출하는 방법으로 떠올랐지만, 세균을 둘러싼 매질의 강한 신호가 목표 신호를 덮어 시간이 걸리고 번거로운 세균 분리 단계가 필요했다. 이 연구는 새로 제안한 딥러닝 모델 DualWKNet(이중 가지 넓은 커널 망)으로 SERS 분석을 보강해, 분리 절차 없이 흔한 세균 두 종(E. coli, S. epidermidis)과 그 매질의 신호를 분류했다. 분류 정확도는 최대 98%였고, SERS와 딥러닝을 묶어 짧은 측정 시간과 적은 학습 자료로 임의의 매질 속 세균을 분리 없이 검출하는 방법을 보였다.[^p7] | 1저자 E. Rho, 마지막 저자 조성호 (8명) |
| 8 | 2025 | [Probabilistic Inertial Poser (ProbIP): Uncertainty-Aware Human Motion Modeling from Sparse Inertial Sensors](https://doi.org/10.1109/iccv51701.2025.02402) · IEEE/CVF International Conference on Computer Vision (ICCV 2025) | 몸에 다는 관성 측정 장치(IMU)는 거슬리지 않게 움직임을 추적하지만, 센서를 붙이는 자리가 적어 온몸의 세밀한 움직임을 잡을 때 불확실성이 생긴다. 기존 방법은 물리적으로 그럴듯한 움직임 패턴을 골라 이 문제를 줄였지만 자료에 들어 있는 불확실성을 직접 다루지는 않았다. 이 연구는 적은 수의 IMU 자료를 물리 제약 없이 사람 동작 예측으로 바꾸는 확률 모델 ProbIP를 내놓았다. RU-Mamba 블록으로 회전에 대한 확률 분포(행렬 피셔 분포)를 예측해 회전 행렬과 그 불확실성을 함께 추정하고, 층을 거치며 동작 분포를 점점 좁히는 PDN 기법으로 다양한 동작에서 안정적으로 학습하게 했다. IMU 6개 이하로 여러 공개 데이터셋에서 최신 기법 수준(state-of-the-art)의 성능을 보였다.[^p8] | 1저자 M. Kim, 마지막 저자 조성호 (3명) |

## 교수와 전문 분야

조성호 교수는 KAIST 전산학부 교수다. 전산학부 교수진 페이지는 연구분야를 소프트웨어 디자인, 비주얼 컴퓨팅, 인공지능·정보서비스, 인터랙티브 컴퓨팅으로, 전공을 증강지능, 생체신호기반 상호작용, 지능 로봇으로 적는다.[^cs] 연구실 Professor 페이지는 전산학부 Professor 외에 AI컴퓨팅학과, AX학과, 로봇공학학제전공, 전기및전자공학부·반도체시스템공학과, 인체증강연구소, 제조 피지컬 AI 센터의 「Associated Professor」와, KAIST 다온 AX 센터와 실패연구소(KAIST Center for Ambitious Failure)의 「Director」를 적는다.[^prof] 반도체시스템공학과 교수진에도 연구분야 「컴퓨터, 인공지능 및 소프트웨어」, 연구실 「뉴로-기계 증강지능 연구실」로 올라 있다.[^ssep]

교수는 서울대학교에서 기계항공공학 학사(1999)를, MIT에서 기계공학 석사(S.M., 2001)와 전기공학·컴퓨터과학 박사(Ph.D., 2006)를 받았다.[^prof][^cs] Professor 페이지가 적는 연구 관심사는 지능 로보틱스와 딥 로봇 학습, 착용형 지능과 증강 지능, 뉴로-하이브리드 지능과 뇌-컴퓨터 인터페이스, 헬스케어 지능이다.[^prof] 연구실 Theses 페이지의 학위 논문 목록은 2010년 2월부터 이어진다.[^theses]

논문으로 보면 전문 분야는 여섯 갈래다. 소프트 로봇 장갑을 쓴 손 재활(대표 논문 1),[^p1] 운동 상상 뇌파를 쓰는 뇌-컴퓨터 인터페이스(대표 논문 2, 3),[^p2][^p3] 영상 정합과 다시점 스테레오 3차원 복원(대표 논문 4, 5),[^p4][^p5] 로봇 파지 학습(대표 논문 6),[^p6] 라만 분광 신호의 딥러닝 분석(대표 논문 7),[^p7] 착용형 관성 센서로 하는 사람 동작 추정(대표 논문 8)이다.[^p8]

## 응용 분야

대표 논문들은 뇌졸중 생존자의 손 재활(대표 논문 1)과 운동 장애가 있는 사람의 휠체어 운전(대표 논문 2)을 응용 대상으로 든다.[^p1][^p2] 대표 논문 7은 식품 안전 분석과 감염병 진단을 위한 세균 검출을 목표로 한다.[^p7] 연구 소개 글은 혈액 표지 물질의 SERS 분석으로 하는 알츠하이머병 진단 플랫폼과,[^r-sers] 스마트워치로 테니스 샷을 기록해 모바일 앱에 요약해 보여 주는 시제품을 소개한다.[^r-tennis] 논문 목록에는 말하는 상상과 귀 뇌파로 가전을 제어하는 BCI 시스템 논문이 있다.[^pubs]

## 구성원

연구실 누리집 Postdoctoral Associates 페이지의 박사후연구원 1명과 Research Assistants 페이지의 박사과정 9명, 석사과정 8명이다.[^members] 연구 주제 칸은 두 페이지가 각 구성원 옆에 적은 연구 분류(Machine Intelligence, Neuro-Hybrid Intelligence, Augmented Intelligence)다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Eojin Rho | 박사후연구원 | Machine Intelligence | 1, 7 |
| Seunghun Koh | 박사과정 | Neuro-Hybrid Intelligence |  |
| Sejoon Huh | 박사과정 | Machine Intelligence | 2, 6 |
| Jaehoon Choi | 박사과정 | Neuro-Hybrid Intelligence |  |
| Jiho Kwak | 박사과정 | Machine Intelligence |  |
| Yeonseo Lee | 박사과정 | Augmented Intelligence |  |
| Haram Kwon | 박사과정 | Neuro-Hybrid Intelligence |  |
| Chaeeun Hwang | 박사과정 | Neuro-Hybrid Intelligence |  |
| Guebin Hwang | 박사과정 | Machine Intelligence |  |
| Jonghee Jeon | 박사과정 | Machine Intelligence |  |
| Taewoo Kim | 석사과정 | Machine Intelligence |  |
| Sangeun Kim | 석사과정 | Machine Intelligence |  |
| Sunghyun Chang | 석사과정 | Augmented Intelligence |  |
| Jinwoo Jeong | 석사과정 | Neuro-Hybrid Intelligence |  |
| Hyosup Shin | 석사과정 | Augmented Intelligence |  |
| Jimin Heo | 석사과정 | Neuro-Hybrid Intelligence |  |
| Chanwoo Cho | 석사과정 | Machine Intelligence |  |
| Donghyun Kim | 석사과정 | Augmented Intelligence |  |

## 졸업생과 학위 논문

누리집 Theses 페이지의 학위 논문 44건(박사 10건, 석사 34건, 2010년 2월–2024년 8월)이다. 이름, 학위 논문 제목, 학위와 연월은 페이지 표기 그대로이고, 석사 3건은 「Master’s Thesis (Robotics Program)」로 적혀 있다. 여섯 명은 석사와 박사 학위 논문으로 두 번 나온다. 페이지는 졸업생의 진로를 적지 않는다.[^theses]

| 이름 | 학위·과정 (연도) | 학위 논문 |
|---|---|---|
| Khang Truong Giang | PhD Thesis (Aug 2024) | 단안 이미지에서 난해한 3D 장면을 재구성하기 위한 학습 |
| 황규빈 | Master’s Thesis (Aug 2024) | 로봇 수용 요인에 대한 메타분석 및 비주얼 서보잉을 활용한 자세 기반 시선 감지 시스템 |
| 황채은 | Master’s Thesis (Feb 2024) | 뇌-컴퓨터 인터페이스 기반 웨어러블 로봇 장갑 제어를 위한 동작 상상 훈련 프로토콜 연구 |
| 권하람 | Master’s Thesis (Aug 2023) | 뇌-컴퓨터 인터페이스에서의 머리 방향 적용을 통한 가상환경상의 1인칭 움직임 제어 성능 향상 |
| 이연서 | Master’s Thesis (Aug 2023) | 웨어러블 목줄 디바이스를 이용한 반려동물 상태 모니터링 시스템 |
| 곽지호 | Master’s Thesis (Feb 2023) | 지식 그래프를 활용한 로봇의 의미론적 파지법에 대한 연구 |
| Netiwit Kaongoen | PhD Thesis (Aug 2022) | 귀-주변 뇌파 기반 일상생활용 웨어러블 뇌-컴퓨터 인터페이스 |
| 최진우 | PhD Thesis (Feb 2022) | 직관적인 비동기식 뇌-컴퓨터 인터페이스 모빌리티 제어를 위한 가상착용형 스캐폴딩 및 반자율주행 기법 |
| 이호창 | Master’s Thesis (Feb 2022) | 인공지능의 접목을 통한 장갑형 웨어러블 로봇의 활용도 개선 |
| 최재훈 | Master’s Thesis (Feb 2022) | 귀-주변 전극 기반 뇌-컴퓨터 인터페이스를 사용한 발화상상 의도 분석 |
| 김대겸 | PhD Thesis (Aug 2021) | 증강 지능을 통한 소프트 웨어러블 손 로봇 융합 방법 |
| Khang Truong Giang | Master’s Thesis (Aug 2021) | 온라인 3차원 복원을 위한 순차적 정보 기반의 깊이 추정 |
| 허세준 | Master’s Thesis (Aug 2021) | 운동 연상 기반 제어 애플리케이션의 성능에 미치는 구체적 가상현실 피드백의 영향 조사 |
| 고승훈 | Master’s Thesis (Feb 2021) | 설명가능한 인공지능과 사용자간의 순환형 상호작용이 주는 효과에 대한 분석 및 측정방법에 관한 연구 |
| Hanyu Liu | Master’s Thesis (Robotics Program) (Feb 2021) | DEM을 이용한 입자 재밍 기술 기반의 가변 강성 소프트 액츄에이터 시뮬레이션 |
| 송수환 | PhD Thesis (Feb 2020) | 드론 활용 온라인 3차원 모델 생성을 위한 경로계획 방법 |
| 박정국 | PhD Thesis (Feb 2020) | 심층 회선 신경망의 베이지언 가중치 감쇠: 근사화와 일반화 |
| 박준용 | Master’s Thesis (Feb 2020) | 동적 물체의 특징점 제거를 기반으로 한 Visual SLAM |
| 조수민 | PhD Thesis (Aug 2019) | 모사학습 및 행동 조합에 기반한 로봇의 작업 행동 학습 및 생성 |
| 김두영 | PhD Thesis (Feb 2019) | 인간 동작 추정을 위한 소프트 웨어러블 센서의 설계 및 보정 기법 |
| 최진우 | Master’s Thesis (Feb 2019) | 차량의 오작동으로 인한 뇌파 변화 연구 |
| Bivan Alzacky Harmanto | Master’s Thesis (Feb 2019) | 딥러닝의 개인화를 위한 상호 반복적 피드백 모델 |
| 하지수 | Master’s Thesis (Feb 2019) | 소프트 손바닥 그리퍼와 완전 연결 신경망을 활용한 물체 식별 |
| 김승운 | Master’s Thesis (Feb 2019) | 선박 내부 실시간 정보 공유를 위한 통신 중계 시스템 및 웹 기반 사용자 인터페이스 연구 |
| 김병형 | PhD Thesis (Aug 2018) | 일상생활에서 발생하는 감정의 역학관계를 파악하는 웨어러블 정서 라이프로그 시스템 개발 |
| Kent Sommer | Master’s Thesis (Aug 2018) | 심층 강화 학습을 통한 메플리스 내비게이션 |
| 한승현 | Master’s Thesis (Feb 2018) | 딥러닝을 활용한 마이크로플루이딕 소프트센서의 특성 분석 |
| 배병욱 | Master’s Thesis (Feb 2017) | 일인칭 행동 인식을 위한 컨볼루션 순환 신경망 연구 |
| 유문원 | Master’s Thesis (Aug 2016) | 지인 사진을 이용한 P300 신호 기반 사용자 인증 시스템 |
| Netiwit Kaongoen | Master’s Thesis (Aug 2016) | 성능 향상을 위한 ASSR/P300-하이브리드 청각 뇌-컴퓨터 인터페이스 |
| 이홍구 | PhD Thesis (Aug 2016) | 비교사 학습에 기반한 온라인 주행 영역 검출 연구 |
| 전진성 | Master’s Thesis (Feb 2016) | 설치류 모델에서의 명령 기반 공간 탐색 |
| 김용원 | Master’s Thesis (Aug 2015) | 일상생활 활용을 위한 뇌파도 측정 및 시선 추척을 이용한 하이브리드형 웨어러블 인터페이스 |
| Theodore F. Morse | Master’s Thesis (Feb 2015) | 다중 기기 내 주요 알림 기기 선택 기술 |
| 송수환 | Master’s Thesis (Feb 2015) | 야외 환경 라이다 데이터 분석을 위한 경계선 강화 슈퍼 복셀 분할 방법 및 응용 |
| 최봉재 | Master’s Thesis (Aug 2014) | 저가형 하이브리드 뇌-컴퓨터 인터페이스에 기반한 휴머노이드 로봇의 조종과 인식 |
| 조재상 | Master’s Thesis (Feb 2013) | 뇌파기반 뇌-기계 인터페이스를 위한 계층적 베이지안 모델링 |
| Xuanquyen Nguyen | Master’s Thesis (Aug 2012) | 머리 움직임을 허용하는 시선추적기를 이용한 휠체어 제어 |
| 조수민 | Master’s Thesis (Feb 2012) | 선별된 시연 동작을 통한 점진적 로봇 행동학습 |
| 이홍구 | Master’s Thesis (Feb 2012) | 생체 모방 로봇의 연구: 이족보행로봇과 선충로봇의 설계 |
| 조영래 | Master’s Thesis (Robotics Program) (Aug 2011) | 사용자 입력 문자에 반응하는 군집 로봇 행동 구현 |
| 이건홍 | Master’s Thesis (Robotics Program) (Aug 2011) | 실내 서비스 로봇을 위한 거리 정보와 영상 정보를 이용한 물체 인식 알고리즘 |
| 전은철 | Master’s Thesis (Feb 2011) | 모바일 로봇을 이용한 실시간 실내환경 3D 맵 구축 |
| 박지환 | Master’s Thesis (Feb 2010) | 스테레오 비전을 이용한 실시간 인간형 로봇 궤적 추출 및 네비게이션 |

## 최근 논문 목록 (2021–2026)

누리집 Journal Publications·Conference Proceedings 목록의 2021–2026년 논문 49편이다. 학술지 29편과 학회 논문 20편이며, 연도마다 학술지 논문을 먼저 적었다. 각 줄의 저자·제목·학술지·학회 표기는 누리집 그대로다. 학술지 한 편(IEEE Robotics and Automation Letters, RoboSoft 2024 발표)은 누리집에 출판 연도가 적혀 있지 않아 목록 끝 「연도 표기 없음」에 두었다. 누리집 저자 표기에 조성호 교수가 없는 학술지 논문 두 편(2021년 Sequential Depth Completion…, 2022년 View Path Planning…)도 목록대로 실었다.[^pubs]

**2026**

- Y Lee et al, 1-D Collocated Dual-Gradient Sensory Fibers for Comprehensive Sensing and Decoding of Complex Human Motion and Physiology, Advanced Materials, July 2026

**2025**

- JB Lee et al, Reflection-Enhanced Raman Identification of Single Bacterial Cells Patterned Using Capillary Assembly, ACS Sensors, 10:8, 5908-5917, Aug 2025
- B Lee, JK Park, KT Giang, S Jo, S Song, MVS-GS: High-Quality 3D Gaussian Splatting Mapping via Online Multi-View Stereo, IEEE Access, 13:1-13, 2025
- M Kim, Y Jeon, S Jo, Probabilistic Inertial Poser (ProbIP): Uncertainty-aware Human Motion Modeling from Sparse Inertial Sensors, International Conference on Computer Vision (ICCV 2025)

**2024**

- K T Giang, S Song, S Jo, TopicFM+: Boosting Accuracy and Efficiency of Topic-Assisted Feature Matching, IEEE Transactions on Image Processing, 33: 6016-6028, Oct 2024
- S Ko, BH Kim, S Jo, Understanding the User Perception and Experience of Interactive Algorithmic Recourse Customization, ACM Transactions on Computer-Human Interaction, 31(3), Aug 2024
- M Kim, S Huh, HJ park, SH Cho, MY Lee, S Jo, YS Jung, Surface-Functionalized SERS Platform for Deep Learning-Assisted Diagnosis of Alzheimer’s Disease, Biosensors and Bioelectronics, 251, May 2024
- J Lee, J Choi, S Jo, Selective Multi-source Domain Adaptation Network for Subject Independent Motor Imagery Discrimination, IEEE Transactions on Cognitive and Developmental Systems, 16:3, 923-934, June 2024
- E Rho, H Lee, Y Lee, K Lee, J Mun, M Kim, D Kim, HS Park, S Jo, Multiple Hand Posture Rehabilitation System using Vision-Based Intention Detection and Soft Robotic Glove, IEEE Transactions on Industrial Informatics, 20:4, 6499-6509, April 2024
- J Park, S Yang, S Jo, Silent Impact: Tracking Tennis Shots from the Passive Arm, The ACM Symposium on User Interface Software and Technology 2024 (UIST 2024)
- K T Giang, S Song, S Jo, Learning to Produce Semi-dense Correspondences for Visual Localization, Conference on Computer Vision and Pattern Recognition 2024 (CVPR 2024)

**2023**

- J Mun, KT Giang, Y Lee, N Oh, S Huh, M Kim, S Jo, HybGrasp: A Hybrid Learning-to-Adapt Architecture for Efficient Robot Grasping, IEEE Robotics and Automation Letters, 8:12, 8390-8397, Dec 2023 (presented in ICRA 2024)
- N Kaongoen, J Choi, JW Choi, H Kwon, C Hwang, G Hwang, BH Kim, S Jo, The Future of Wearable EEG: A Review of Ear-EEG Technology and its Applications, Journal of Neural Engineering, 20:5, Oct 2023
- JH Choi, N Kaongoen,H Choi, M Kim, BH Kim, S Jo, Decoding Auditory-Evoked Response in Affective States using Wearable Around-Ear EEG System, Biomedical Physics & Engineering Express, Aug 2023
- BH Kim, JW Choi, H Lee, S Jo, A Discriminative SPD Feature Learning Approach on Riemannian Manifolds for EEG Classification, Pattern Recognition, 143, 2023
- JW Choi, J Park, S Huh, S Jo, Asynchronous Motor Imagery BCI and LiDAR-based Shared Control System for Intuitive Wheelchair Navigation, IEEE Sensors Journal, 23(14):16252-16263, 2023
- JW Choi, H Kwon, J Choi, N kaongoen, C Hwang, M Kim, BH Kim, S Jo, Neural Applications Using Immersive Virtual Reality: A Review on EEG Studies, IEEE Transactions on Neural Systems & Rehabilitation Engineering, 31: 1645-1658, 2023
- S Song, KT Giang, D Kim, S Jo, Prior depth-based multi-view stereo network for online 3D model reconstruction, Pattern Recognition, 136, April 2023
- J Lee, C Chung, H Lee, S Jo, JJ Whang, VISTA: Visual-Textual Knowledge Graph Representation Learning, Findings of Empirical Methods in Natural Language Processing (Findings of EMNLP), 2023
- N Kaongoen, S Jo, Adapting Artifact Subspace Reconstruction Method for Single-Channel EEG using Signal Decomposition Techniques, 45th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC’23), 2023
- KT Giang, S Song, S Jo, TopicFM: Robust and Interpretable Topic-Assisted Feature Matching, 37th AAAI Conference on Artificial Intelligence (AAAI-23), 2023
- JW Choi, J Choi, S Jo, Reference Bank Multi-feature Extraction for EEG-based Concentration Discrimination, 11th IEEE International Winter Conference on Brain-Computer Interface 2023
- C Hwang, JW Choi, S Jo, Effect of Grasping Speed for Action Observation During Wearable Robotic Glove-based Motor Imagery Traing, 11th IEEE International Winter Conference on Brain-Computer Interface 2023
- H Kwon, J Choi, JW Choi, S Jo, Subject-Aware User State Classification with Deep Learning Models: An Exploratory Study, 11th IEEE International Winter Conference on Brain-Computer Interface 2023

**2022**

- K Kim et al, A substrate-less nanomesh receptor with meta-learning for rapid hand task recognition, Nature Electronics, 39, Dec 2022
- N Kaongoen, J Choi, S Jo, A Novel Online BCI System Using Speech Imagery and Ear-EEG for Home Appliances Control, Computer Methods and Programs in Biomedicine, 224, 107022, Sept 2022
- J Kwak, J Lee, J J Whang, S Jo, Semantic Grasping via a Knowledge Graph of Robotic Manipulation: A Graph Representation Learning Approach, IEEE Robotics and Automation Letters, 7(4), 9397-9404, Oct. 2022 (presented in IROS 2022)
- E Rho, M Kim, S H Cho, B Choi, H Park, H Jang, Y S Jung, S Jo, Separation-free bacterial identification in arbitrary media via deep neural network-based SERS analysis, Biosensors and Bioelectronics, 202(5), 113991, April 2022
- J Park, D Kim, S Huh, S Jo, Maximization and Restoration: Action Segmentation through Dilation Passing and Temporal Reconstruction, Pattern Recognition, 129, 108764, Sept. 2022
- BH Kim, S Jo, S Choi, ALIS: Learning Affective Causality behind Daily Activities from a Wearable Life-Log System, IEEE Transactions on Cybernetics, 52:12, 13212-13224, 2022
- S Song, D Kim, S Choi, View Path Planning via Online Multi-View Stereo for 3D Modeling of Large-Scale Structures, IEEE Transactions on Robotics, 38(1): 372-390, 2022
- KT Giang, S Song, S Jo, Curvature-Guided Dynamic Scale Networks for Multi-view Stereo, 2022 International Conference on Learning Representations (ICLR)
- J Choi, N Kaongoen, S Jo, Investigation on Effect of Speech Imagery EEG Data Augmentation with Actual Speech,10th IEEE International Winter Conference on Brain-Computer Interface 2022
- N Kaongoen, J Jeon, S Jo, Enhancing the Performance of P300-based BCIs by tDCS of the Left VL-PFC,10th IEEE International Winter Conference on Brain-Computer Interface 2022
- H Kwon, C Hwang, S Jo, Vision Combined with MI-Based BCI in Soft Robotic Glove Control,10th IEEE International Winter Conference on Brain-Computer Interface 2022

**2021**

- E Rho, D Kim, H Lee, S Jo, Learning Fingertip Force to Grasp Deformable Objects for Soft Wearable Hand Robot with TSM, IEEE Robotics and Automation Letters (presented in IROS2021), 6:4, 8126-8133, Oct 2021
- M Kim, H Choi, K-J Cho, S Jo, Single to Multi: Data-driven High Resolution Calibration Method for Piezoresistive Sensor Array, IEEE Robotics and Automation Letters, 6(3): 4970-4977, July 2021
- KT Giang, S Song, D Kim, S Choi, Sequential Depth Completion with Confidence Estimation for 3D Model Reconstruction, IEEE Robotics and Automation Letters, 6(2) : 327- 334, 2021
- D Kim, SH Kim, T Kim, BB Kang, M Lee, W Park, S Ku, D Kim, J Kwon, H Lee, J Bae, YL Park, KJ Cho, S Jo, Review of machine learning methods in soft robotics, PLOS ONE, Feb 2021
- S Cheon, D Kim, S Kim, BB Kang, J Lee, HS Gong, S Jo, KJ Cho, J Ahn, Identifying power grasp intention with a single sEMG sensor for reliable robotic assistance, IEEE Transactions on Medical Robotics and Bionics, 3(1): 179-189, 2021
- N Kaongoen, J Choi, S Jo, Speech-imagery-based Brain-Computer Interface system using ear-EEG, Journal of Neural Engineering, 18(1), 8016023, Feb 2021
- B H Kim, J H Kwak, M Kim, S Jo, Affect-driven Robot Behavior Learning System using EEG Signals for Less Negative Feelings and More Positive Outcomes, 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
- M Lee, et al. Dynamic Humanoid Locomotion over Uneven Terrain with Streamlined Perception-Control Pipeline, 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
- J Lee, JW Choi, S Jo, Subject-Independent Motor Imagery EEG Classification Based on Graph Convolutional Network, Asian Conference on Pattern Recognition (ACPR 2021)
- N Oh, J Park, J H Kwak, S Jo, A Robot Capable of Proactive Assistance through Handovers for Sequential Tasks, 2021 18th International Conference on Ubiquitous Robots (UR)
- JW Choi, BH Kim, S Jo, Asynchronous Motor Imagery Brain-Computer Interface for Simulated Drone Control, 9th IEEE International Winter Conference on Brain-Computer Interface 2021
- N Kaongoen, J Choi, S Jo, Transcranial Direct-Current Stimulation Effect on a Speech-Imagery-based BCI, 9th IEEE International Winter Conference on Brain-Computer Interface 2021
- BH Kim, JW Choi, S Jo, Rank-based Discriminative Feature Learning for Motor Imagery Classification in EEG Signals, 9th IEEE International Winter Conference on Brain-Computer Interface 2021

**연도 표기 없음**

- E Rho, W Kim, J Mun, SY Y, K-J Cho, S Jo, Impact of Physical Parameters and Vision Data on Deep Learning-based Grip Force Estimation for Fluidic Origami Soft Grippers, IEEE Robotics and Automation Letters, (presented in RoboSoft 2024)

## 연구 소개 글

누리집 Research 메뉴의 연구 소개 글 가운데 2021년 10월 13일 이후 게시된 10건이다. 날짜는 글의 게시일이고 제목은 게시된 그대로다.[^ri][^ai]

- 2025-10-25 · Probabilistic Inertial Poser
- 2024-09-06 · Tracking Tennis Shots from the Passive Arm
- 2024-02-27 · Semi-dense Correspondences for Visual Localization
- 2024-02-23 · Deep learning-based SERS platform for daignosis of Alzheimer’s disease
- 2023-08-18 · Vision-based Intention Detection for Hand Rehabilitation
- 2023-05-16 · Learning-to-Adapt Architecture for Efficient Robot Grasping
- 2022-12-23 · Human sensory intelligence with meta learned substrate-less nanomesh receptor
- 2022-12-07 · TopicFM – Robust and Interpretable Feature Matching
- 2022-12-01 · Multi-View Stereo Network for Online Large-Scale 3D Reconstruction
- 2022-01-12 · Deep learning-based SERS analysis for bacteria detection in arbitrary media

## 학생 연구 프로그램

누리집 Undergraduate Research Program 페이지는 연구실에서 진행한 학부생 연구 과제 32건(2008년 가을–2026년 봄)을 적는다. 2021년 이후 과제는 14건이며, 관성 센서·인체 모형·골격·글 자료를 함께 학습하는 사람 활동 이해 모델(2026년 봄), 사람 손 모양 로봇 손이 언어 안내로 물체를 다루는 능력을 익히는 연구(2025년 가을), 확산 모델(생성형 인공지능의 한 방식)로 뇌파 자료를 만들어 BCI 성능을 높이는 연구(2024년 봄), 뇌-컴퓨터 인터페이스와 머리 자세 추정으로 하는 휠체어 제어(2022년 가을) 등이다.[^urp] High School Research & Education Program 페이지는 대전영재과학고·한국과학영재학교 학생과 함께한 연구·교육 과제 17건과, 한국과학영재학교 HRP 과제 17건을 적는다. 그 가운데 2021년 이후 과제는 각각 11건과 7건이다.[^hs]

## 연락과 위치

- 교수 연구실: 전산학부동(E3-1) 2433호[^cs][^ssel]
- 교수 연구실 전화: 3540 (전산학부 교수 소개의 표기)[^cs]
- Contacts 페이지는 연구실에서 URP·개별 연구·졸업 연구를 하려는 KAIST 학부생과 대학원 연구실 배정에 관심 있는 학생에게 연락을 권하고, 다른 대학 학생으로 대학원 진학을 통해 이 연구실에서 일하려는 경우에는 충분히 일찍 연락하라고 안내한다. KAIST 이노코어 프로그램에 참여해 박사후연구원 지원이 가능하다고 적는다.[^contacts]
- 소프트웨어: 연구실 Software 페이지가 GitHub 저장소 <https://github.com/KAIST-NMAIL>를 안내한다.[^software]
[^p1]: E. Rho 외, S. Jo, IEEE Transactions on Industrial Informatics 20, 6499-6509 (2024). <https://doi.org/10.1109/tii.2023.3348826> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J. W. Choi, J. Park, S. Huh, S. Jo, IEEE Sensors Journal 23, 16252-16263 (2023). <https://doi.org/10.1109/jsen.2023.3281756> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Lee, J. W. Choi, S. Jo, IEEE Transactions on Cognitive and Developmental Systems 16, 923-934 (2024). <https://doi.org/10.1109/tcds.2023.3314351> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: K. T. Giang, S. Song, S. Jo, IEEE Transactions on Image Processing 33, 6016-6028 (2024). <https://doi.org/10.1109/tip.2024.3473301> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: S. Song, K. G. Truong, D. Kim, S. Jo, Pattern Recognition 136, 109198 (2023). <https://doi.org/10.1016/j.patcog.2022.109198> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: J. Mun 외, S. Jo, IEEE Robotics and Automation Letters 8, 8390-8397 (2023). <https://doi.org/10.1109/lra.2023.3329622> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: E. Rho 외, S. Jo, Biosensors and Bioelectronics 202, 113991 (2022). <https://doi.org/10.1016/j.bios.2022.113991> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: M. Kim, Y. Jeon, S. Jo, 2025 IEEE/CVF International Conference on Computer Vision (ICCV), 1-10 (2025). <https://doi.org/10.1109/iccv51701.2025.02402> 초록 기준(학회 논문집 페이지 게시 초록: ICCV 2025 Open Access Repository <https://openaccess.thecvf.com/content/ICCV2025/html/Kim_Probabilistic_Inertial_Poser_ProbIP_Uncertainty-aware_Human_Motion_Modeling_from_Sparse_ICCV_2025_paper.html>, 2026-10-23 열람).
[^home]: 뉴로-기계 증강지능 연구실 누리집 첫 화면 <http://nmail.kaist.ac.kr/wordpress/> (연구실 소개, Research Area, 메뉴, 2026-10-23 열람)
[^vision]: 뉴로-기계 증강지능 연구실 누리집 Vision 페이지 <http://nmail.kaist.ac.kr/wordpress/index.php/vision/> (2026-10-23 열람)
[^prof]: 뉴로-기계 증강지능 연구실 누리집 Professor 페이지 <http://nmail.kaist.ac.kr/wordpress/index.php/professor-jo-sungho/> (소속·직함, Education, Research Interests, 2026-10-23 열람)
[^members]: 뉴로-기계 증강지능 연구실 누리집 Postdoctoral Associates 페이지 <http://nmail.kaist.ac.kr/wordpress/index.php/postdoctoral-associates/>, Research Assistants 페이지 <http://nmail.kaist.ac.kr/wordpress/index.php/students/> (2026-10-23 열람)
[^theses]: 뉴로-기계 증강지능 연구실 누리집 Theses 페이지 <http://nmail.kaist.ac.kr/wordpress/index.php/theses/> (2026-10-23 열람)
[^pubs]: 뉴로-기계 증강지능 연구실 누리집 Journal Publications 페이지 <http://nmail.kaist.ac.kr/wordpress/index.php/publications/>, Conference Proceedings 페이지 <http://nmail.kaist.ac.kr/wordpress/index.php/conference-proceedings/> (목록 범위는 근거 페이지, 2026-10-23 열람)
[^soft]: 뉴로-기계 증강지능 연구실 누리집 Research 메뉴 Soft Robotic Intelligence 분류 <http://nmail.kaist.ac.kr/wordpress/index.php/category/research/robotic-intelligence/wearable-soft-robot/> (착용형 손 로봇 연구 소개 글 목록, 2026-10-23 열람)
[^bci]: 뉴로-기계 증강지능 연구실 누리집 Research 메뉴 Brain-Computer Interfaces 분류 <http://nmail.kaist.ac.kr/wordpress/index.php/category/research/neuro-machine-intelligence/brain-computer-interfaces/> (뇌-컴퓨터 인터페이스 연구 소개 글 목록, 2026-10-23 열람)
[^vis]: 뉴로-기계 증강지능 연구실 누리집 Research 메뉴 Visonal Intelligence 분류 <http://nmail.kaist.ac.kr/wordpress/index.php/category/research/robotic-intelligence/visonal-intelligence/> (영상 정합·위치 추정·3차원 복원 연구 소개 글 목록, 2026-10-23 열람)
[^chemo]: 뉴로-기계 증강지능 연구실 누리집 Research 메뉴 Deep Chemometrics 분류 <http://nmail.kaist.ac.kr/wordpress/index.php/category/research/neuro-inspired-intelligence/deep-chemometrics/> (SERS 딥러닝 분석 연구 소개 글 2건, 2026-10-23 열람)
[^ri]: 뉴로-기계 증강지능 연구실 누리집 Research 메뉴 Robotic Intelligence 분류 <http://nmail.kaist.ac.kr/wordpress/index.php/category/research/robotic-intelligence/> (연구 소개 글 제목과 게시일, 2026-10-23 열람)
[^ai]: 뉴로-기계 증강지능 연구실 누리집 Research 메뉴 Augmented Intelligence 분류 <http://nmail.kaist.ac.kr/wordpress/index.php/category/research/neuro-inspired-intelligence/> (연구 소개 글 제목과 게시일, 2026-10-23 열람)
[^r-rehab]: 연구 소개 글 「Vision-based Intention Detection for Hand Rehabilitation」 <http://nmail.kaist.ac.kr/wordpress/index.php/2023/08/18/vision-based-intention-detection-for-hand-rehabilitation/> (2023-08-18 게시, 2026-10-23 열람)
[^r-semidense]: 연구 소개 글 「Semi-dense Correspondences for Visual Localization」 <http://nmail.kaist.ac.kr/wordpress/index.php/2024/02/27/semi-dense-correspondences-for-visual-localization/> (2024-02-27 게시, 2026-10-23 열람)
[^r-mvs]: 연구 소개 글 「Multi-View Stereo Network for Online Large-Scale 3D Reconstruction」 <http://nmail.kaist.ac.kr/wordpress/index.php/2022/12/01/active-3d-modeling-via-online-multi-view-stereo/> (2022-12-01 게시, 2026-10-23 열람)
[^r-sers]: 연구 소개 글 「Deep learning-based SERS platform for daignosis of Alzheimer’s disease」 <http://nmail.kaist.ac.kr/wordpress/index.php/2024/02/23/deep-learning-based-sers-platform-for-daignosis-of-alzheimers-disease/> (2024-02-23 게시, 2026-10-23 열람)
[^r-tennis]: 연구 소개 글 「Tracking Tennis Shots from the Passive Arm」 <http://nmail.kaist.ac.kr/wordpress/index.php/2024/09/06/tracking-tennis-shots-from-the-passive-arm/> (2024-09-06 게시, 2026-10-23 열람)
[^r-nanomesh]: 연구 소개 글 「Human sensory intelligence with meta learned substrate-less nanomesh receptor」 <http://nmail.kaist.ac.kr/wordpress/index.php/2022/12/23/a-substrate-less-nanomesh-recprot-with-meta-learning/> (2022-12-23 게시, 2026-10-23 열람)
[^urp]: 뉴로-기계 증강지능 연구실 누리집 Undergraduate Research Program 페이지 <http://nmail.kaist.ac.kr/wordpress/index.php/undergraduate-research-program/> (2026-10-23 열람)
[^hs]: 뉴로-기계 증강지능 연구실 누리집 High School Research & Education Program 페이지 <http://nmail.kaist.ac.kr/wordpress/index.php/high-school-research-education-program/> (2026-10-23 열람)
[^contacts]: 뉴로-기계 증강지능 연구실 누리집 Contacts 페이지 <http://nmail.kaist.ac.kr/wordpress/index.php/contacts/> (2026-10-23 열람)
[^software]: 뉴로-기계 증강지능 연구실 누리집 Software 페이지 <http://nmail.kaist.ac.kr/wordpress/index.php/software/> (2026-10-23 열람)
[^cs]: KAIST 전산학부 교수 소개(조성호) <https://cs.kaist.ac.kr/people/view?idx=27&kind=faculty&menu=160> (직위, 연구분야, 전공, 학위, 교수연구실, 전화, 2026-10-23 열람)
[^ssel]: KAIST 반도체시스템공학과 연구실 목록 <https://sse.kaist.ac.kr/research-laboratory/> (뉴로-기계 증강지능 연구실 항목, 2026-10-23 열람)
[^ssep]: KAIST 반도체시스템공학과 교수진 <https://sse.kaist.ac.kr/professor/> (조성호 교수 항목, 2026-10-23 열람)

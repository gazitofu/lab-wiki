# 생체역학 연구실 (Biomechanics Lab)

**KAIST 기계공학과 · 박수경 교수**

- 분야: 인체 운동의 생체역학, 동적 보행과 에너지 소비, 자세 제어와 감각 통합, 웨어러블 센서·영상 기반 동작 분석, 스포츠 생체역학
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 착용형 생체 센서[^swv][^p2][^p4], 과학·공학 AI[^dw][^swv][^p2], 강화학습[^pc][^p1], 착용형 로봇·외골격[^dw][^notice], 컴퓨터 비전[^swv]
- 홈페이지: <https://biomech.kaist.ac.kr/>
- 근거와 출처: [생체역학 연구실 근거 페이지](biomech-sources.md)

> 사람이 걷고, 균형을 잡고, 운동하는 움직임을 역학 모델로 설명하고 예측하는 연구실이다. 걷기의 역학과 에너지 소비, 넘어지지 않게 자세를 잡는 원리, 몸에 단 센서나 카메라로 움직임을 재는 방법, 운동 동작 분석을 연구하고, 이렇게 얻은 지식을 공학 시스템을 개선하는 데 쓰는 것을 목표로 한다.[^greet][^home]

## 무엇을 연구하나

연구실 Greetings 페이지는 연구 관심을 사람의 움직임을 이해하는 데 두고, 움직임의 역학과 제어를 보여 주는 설명 모델이나 예측 모델로 이를 다룬다고 소개한다. 궁극적인 목표는 사람 움직임에 대한 지식을 공학 시스템을 개선하는 데 쓰는 것이며, 이론과 실험 연구는 동역학, 진동, 제어, 생리학에 걸쳐 있다.[^greet] 첫 화면은 연구 주제로 동적 보행(Dynamic Locomotion), 에너지 소비량(Energy Expenditure), 자세 제어(Postural Control), 감각 통합(Sensory Integration), 웨어러블 기기를 이용한 생체역학 분석, 영상 응용(Vision Applications), 스포츠 생체역학을 든다.[^home] 기계공학과는 교수의 연구분야를 생체역학(Biomechanics), 동적 보행, 자세 제어, 스포츠 역학, 생체모사(Biomimetics)로 적고, 연구분야 페이지는 연구주제를 생체역학과 건강 모니터링(Health Monitoring)으로 적는다.[^mep][^mer]

Research 메뉴는 연구를 네 묶음으로 나눈다. 동적 보행과 에너지 소비, 자세 제어와 감각 통합, 스마트 웨어러블과 영상 응용, 스포츠 생체역학이다.[^dw][^pc][^swv][^sb] 방법으로는 사람의 움직임을 단순한 역학 모델로 나타내는 동역학·진동 모델링과 인공지능 모델을 함께 쓰고, 자세 반응에는 강화학습 모델을, 웨어러블 동작 분석에는 여러 종류의 데이터를 묶은 생체역학·인공지능 모델을 쓴다고 적는다.[^dw][^pc][^swv]

대표 논문으로 보면 연구는 네 갈래다. 첫째, 걷는 동안의 에너지 소비량을 몸에 단 센서 하나로 추정하는 방법과 이를 위한 측정 절차다(대표 논문 2, 3).[^p2][^p3] 둘째, 외부에서 밀릴 때 사람이 균형 전략을 바꾸는 원리를 강화학습 최적화 모델로 설명한 연구다(대표 논문 1).[^p1] 셋째, 손목에 찬 관성 센서 하나로 골프 스윙 궤적을 추적하는 방법이다(대표 논문 4).[^p4] 넷째, 태권도 보호구를 지난 힘에서 실제 타격력을 추정하는 방법이다(대표 논문 5).[^p5] 2021–2026년 논문 목록에는 이 밖에 걸음 동작과 기계학습으로 근전도 신호를 예측하는 연구, 에너지 소비량과 열 손실을 함께 다룬 연구, Respiratory Kinetics를 이용해 엉덩관절 외골격의 보조를 사람마다 맞추는 시간 효율적인 절차, 카메라 영상으로 관성 센서 자료를 바로잡는 골프 스윙 모니터링 연구(International Society of Biomechanics 2025 학회 발표)도 있다.[^pubs]

## 주요 연구 주제

### 1. 동적 보행과 에너지 소비

사람의 걷기는 여러 관절과 근육을 복잡하게 제어해 이루어지지만, 몸의 무게중심이 진동하는 운동으로 단순하게 나타내 이해할 수 있다. 연구 페이지는 이를 용수철이 달린 거꾸로 선 진자로 나타내는 SLIP(Spring Loaded Inverted Pendulum) 모델로 설명하고, 이런 보행 모델에 동역학·진동 모델링과 인공지능을 적용해 실제 사람의 걸음을 분석하고 재현하는 것을 목표로 적는다.[^dw] 세부 주제로는 탄성 다리를 가진 두 발 보행 모델과 그 진동 특성, SLIP 모델에 기반한 운동학 자료(움직임의 위치·각도 자료) 추정, 상체 모델링을 이용한 지면반력 추정, 연조직 모델링으로 달리기 SLIP 모델을 개선하는 연구를 든다.[^dw]

에너지 소비량은 운동 수행 능력과 웨어러블 보조 기기를 평가하는 정량 지표로 쓰이지만, 호흡 가스로 재는 방법은 비용이 많이 들고 값이 흔들려 쓰임이 제한된다. 연구실은 생체역학 정보로 에너지 소비량을 예측해 정확하게 추정하고, 열 손실 분석으로 그 변동을 보정하는 연구를 한다고 적는다.[^dw] 세부 주제는 여러 관절의 역학적 일로 에너지 소비량을 추정하는 연구, 시간 효율적인 데이터 수집 절차로 외골격(H10, Angel Robotics Inc.)의 보조 효과를 평가하는 연구, 열 손실에 따른 에너지 소비량 변동 연구다.[^dw] 엉치뼈에 붙인 관성 측정 장치(IMU) 하나로 걷는 동안의 에너지 소비량을 추정하는 방법과, 걷는 속도를 서서히 높이는 연속 측정 절차로 학습 데이터를 빨리 모으는 방법이 이 갈래의 논문이다.[^p2][^p3] 대표 논문 2, 3.

### 2. 자세 제어와 감각 통합

사람은 여러 외부 교란에 유연하게 대응하며 균형을 유지한다. 연구 페이지는 이 자세 제어가 발목 전략과 엉덩관절 전략 같은 여러 신체 부위의 움직임 전략과, 감각 되먹임에 따라 전략을 바꾸는 방식으로 이루어진다고 설명하고, 여러 교란 조건에서 사람의 자세 반응에 강화학습 모델을 적용해 사람과 비슷한 적응 제어 전략을 찾는다고 적는다.[^pc] 세부 주제는 자세 전략과 되먹임 제어, 교란에 대한 자세 적응, 사람다운 자세 전략을 위한 강화학습이다.[^pc]

균형은 중추신경계가 눈, 전정기관, 근방추 같은 균형 감각 기관의 정보를 합쳐 유지한다. 질병·노화·부상으로 감각이 서로 어긋나거나 잡음이 생기면 균형을 잡기 어려워지는데, 연구실은 관절 움직임 자료, 반사 반응, 지각 측정으로 중추신경계의 다중 감각 통합을 분석하고 모델로 나타낸다.[^pc] 세부 주제는 운동 지각, 내부 추정기·제어기 모델, 여러 감각 신호의 신경 처리다.[^pc] 뒤로 밀리는 교란에서 발목 전략이 엉덩관절 전략으로 바뀌는 현상을, 생체역학 제약을 넣은 강화학습 최적화 모델로 재현한 논문이 이 갈래에 속한다.[^p1] 대표 논문 1.

### 3. 웨어러블·영상 기반 동작 분석

웨어러블 기기로 현장에서 실시간으로 움직임을 분석하려는 수요가 스포츠와 헬스케어 분야에서 늘고 있지만, 센서의 종류와 붙이는 위치의 제약 때문에 쓰임이 제한된다. 연구실은 여러 종류의 데이터를 바탕으로 한 생체역학·인공지능 모델링으로, 적은 수의 센서만으로 사람 몸의 움직임을 분석하는 연구를 한다.[^swv] 세부 주제는 관성 측정 장치 하나로 관절 움직임 추정, 손목 착용 기기로 지면반력 추정, 여러 데이터를 묶은 골프 스윙 궤적 추정이다.[^swv]

휴대 기기에 흔히 들어 있는 카메라로 현장에서 움직임을 분석하는 연구도 한다. 연구 페이지는 생체역학 모델과 영상 기반 인공지능을 결합해, 값싼 장비로도 실험실 수준의 동작 분석을 하는 것을 목표로 적고, 세부 주제로 영상 자료를 이용한 관성 센서 오차 보정과, 영상으로 얻은 무게중심 위치로 걸음의 지면반력을 추정하는 연구를 든다.[^swv] 손목에 찬 관성 센서 하나로 골프 스윙 궤적을 추적하는 논문이 이 갈래에 속한다.[^p4] 대표 논문 4.

### 4. 스포츠 생체역학

스포츠 생체역학은 운동 중 사람 몸의 역학적 특성을 분석해 경기력을 높이고 부상 위험을 줄인다. 연구 페이지는 기존 분석 방법이 현장에서 쓰기 어렵고 실시간 평가에 한계가 있어, 여러 종목에서 모은 데이터로 운동 기술을 정량적으로 평가하고 경기력을 높이는 전략을 연구한다고 적는다.[^sb] 세부 주제로 생체역학을 이용한 현장 모니터링과, 전자 호구를 이용한 태권도 타격력 추정을 든다.[^sb] 태권도 몸통 보호구의 충격 감쇠 특성을 재고, 보호구를 지난 힘에서 실제 타격력을 추정한 논문이 이 갈래에 속한다.[^p5] 대표 논문 5.

## 대표 논문

누리집 International Journal 목록에 출판 논문으로 오른 2021–2026년 학술지 논문 다섯 편을 모두 담았다. 다섯 편 모두 박수경 교수가 마지막 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2025 | [Biomechanical optimization and reinforcement learning provide insight into transition from ankle to hip strategy in human postural control](https://doi.org/10.1038/s41598-025-97637-5) · Scientific Reports | 사람의 자세 제어 전략은 주로 발목을 쓰는 전략과 엉덩관절을 쓰는 전략으로 나뉘며, 교란의 크기와 발 디딤면 크기에 따라 달라진다. 뒤쪽 방향 교란(backward perturbation)에 대한 사람의 자세 반응을 분석하고, 발목에서 엉덩관절 전략으로 바뀌는 현상이 생체역학 제약을 넣은 최적화로 설명되는지 살폈다. 압력 중심(CoP, 발바닥에 걸리는 힘이 모이는 점)이 중족골 관절까지만 움직일 수 있다는 제약을 두고, 이 제약을 어길 때의 벌점과 바로 선 자세 회복, 제어 노력 줄이기를 목표 함수에 담은 강화학습 기반 최적화 모델을 만들었다. 모델은 사람의 자세 반응에서 보이는 발목-엉덩관절 전략 전환을 재현했고, 교란이 커질수록 발목 토크는 제한되고 엉덩관절 움직임은 커지는 양상이 사람의 적응과 맞았다. 비선형 최적화를 구현할 수 있는 강화학습 모델이 사람 움직임의 다양한 적응 특성을 분석하는 도구가 될 수 있다고 본다.[^p1] | 1저자 S. Hong(Seongwoong Hong), 마지막 저자 박수경 (2명) |
| 2 | 2025 | [Estimation of walking energy expenditure using a single sacrum-mounted IMU based on biomechanically-informed machine learning](https://doi.org/10.1038/s41598-025-28393-9) · Scientific Reports | 걷는 동안의 에너지 소비량을 엉치뼈에 붙인 관성 측정 장치(IMU) 하나로 추정하는 방법이다. 몸의 부위별로 나눠 보니, 체중을 받치는 다리(지지 다리)의 시상면(몸을 좌우로 나누는 면) 관절 일률이 전신 관절 일률과 강하게 상관했다(대상자와 걷는 속도 전반에서 R > 0.9). 효율로 가중한 부위별 관절 일률과 전신 에너지 소비량 사이의 비례 관계를 회귀로 먼저 세우고, IMU 자료에서 부위별 관절 동역학을 예측하는 가벼운 인공 신경망과 묶어, 지지 다리 일률로 전신 에너지 소비량을 추정했다. 러닝머신에서 여러 속도로 걸은 건강한 성인 13명으로 검증했으며 기준값은 간접 열량 측정(들이쉬고 내쉰 기체로 에너지 소비를 재는 방법)으로 쟀다. 결과는 한 사람 안의 속도 사이와 사람 사이 모두에서 변동 계수 2% 미만으로 일관됐고, 독립된 집단에서 에너지 소비량을 RMSE 0.69 W/kg로 추정했다.[^p2] | 1저자 J. Jung(Jinsung Jung), 마지막 저자 박수경 (6명) |
| 3 | 2025 | [A time-efficient continuous ramp protocol for data-driven walking energy expenditure estimation across multiple speeds](https://doi.org/10.1186/s12984-025-01707-8) · Journal of NeuroEngineering and Rehabilitation | 웨어러블 기기로 여러 속도의 보행 에너지 소비량을 추정하는 데이터 기반 모델을 만들려면 다양한 데이터가 많이 필요한데, 한 속도로 몇 분씩 걷기를 되풀이하는 단계형 측정은 시간이 많이 든다. 한 번 걷는 동안 속도를 서서히 높이는 연속 경사 측정 절차를 데이터 기반 방법과 결합하고 기존 단계형 절차와 비교했다. 14명이 관성 측정 장치 4개를 달고 러닝머신을 걸었다. 연속 절차는 10분 동안 속도를 1.0 m/s에서 1.75 m/s까지 직선으로 높였고, 단계 절차는 같은 범위의 다섯 속도를 6분씩 걸었다. 호흡 지연을 보정하자 두 절차의 에너지 소비량에는 차이가 없었다. 추가로 모은 13명으로 상용 스마트워치와 비교했더니, 두 데이터로 학습한 딥러닝 모델의 평균 오차는 13.1%(단계)와 10.7%(연속)로 비슷했고 둘 다 스마트워치보다 유의하게 나았다. 연속 절차의 더 다양한 데이터로 학습한 딥러닝 모델은 관성 측정 장치 하나만으로도 넓은 속도 범위에서 고르게 낮은 오차를 냈다.[^p3] | 1저자 H. Jeong(Hyunho Jeong), 마지막 저자 박수경 (2명) |
| 4 | 2024 | [Enhancing accuracy and convenience of golf swing tracking with a wrist-worn single inertial sensor](https://doi.org/10.1038/s41598-024-59949-w) · Scientific Reports | 손목에 찬 관성 센서 하나로 골프 스윙 궤적을 더 정확하게 추적하려고 센서 방향 추정과 누적 오차(드리프트) 줄이기라는 두 기술 문제를 다뤘다. 어드레스 구간의 특정 신호에서 일정한 센서 방향을 뽑아 합성곱 신경망으로 추정을 학습시켰다. 어드레스, 백스윙 정점, 피니시에서 손목 속도에 제약을 걸고, 피니시의 손목 변위가 3차원 스윙 평면 위 가상의 원에 맞도록 해 드리프트를 줄였다. 프로와 아마추어를 포함한 오른손잡이 남성 골퍼 20명이 드라이버와 7번 아이언으로 친 자료로 검증했다. 방향 추정 오차는 기준 방법의 약 60%였고 드리프트 오차는 절반으로 줄었으며, 스윙 전 구간의 추적 성능은 약 17 cm로 여러 종류의 센서를 쓰는 방법과 비슷했다.[^p4] | 1저자 M. Kim(Myeongsub Kim), 마지막 저자 박수경 (2명) |
| 5 | 2026 | [Estimating actual striking forces using attenuation properties of Taekwondo protectors](https://doi.org/10.1371/journal.pone.0328749) · PLOS One | 보호구는 충격력을 크게 줄이는데, 선수에게서 실제 타격력을 직접 재기는 실용·안전 문제로 어렵고 보호구의 감쇠가 실제 충격을 가린다. 태권도 몸통 보호구의 충격 감쇠 특성을 재고, 보호구를 지난 힘에서 원래의 타격력을 추정하는 방법을 내놓았다. 진자로 크기와 접촉 시간이 다른 충격을 되풀이해 줄 수 있는 시험 장치를 만들어, 보호구를 입힌 마네킹에 들어간 힘과 보호구를 지난 힘을 동시에 쟀다. 300 N부터 5800 N까지 감쇠 비율이 일정했고 충격 시간의 영향은 작았으며, 들어간 힘과 전달된 힘 사이의 선형 관계(R² ≥ 0.987)에서 감쇠 계수를 얻었다. 진자 시험으로 검증한 추정 입력 힘 궤적의 nRMSE는 3.5%였고, 최대 힘, 충격 시간, 충격량의 평균 절대 백분율 오차는 각각 4.7%, 1.4%, 3.5%였다. 태권도 선수 5명의 정해진 발차기에 감쇠 계수를 적용하자 최대 타격력은 약 1300–1800 N으로 추정됐다.[^p5] | 1저자 M. Chae(Minho Chae), 마지막 저자 박수경 (6명) |

## 교수와 전문 분야

박수경 교수는 KAIST 기계공학과 교수이며, 기계공학과 교수 소개는 연구분야를 Biomechanics, Dynamic Walking, Postural Control, Sports Mechanics, Biomimetics로, 연구실을 생체역학 연구실로 적는다.[^mep][^mel] 연구실 Professor 페이지에 따르면 교수는 KAIST 기계공학과에서 학사(1995년 2월)와 석사(1997년 2월)를, 미국 University of Michigan에서 기계공학 박사(2002년 4월)를 받았다.[^prof] 같은 페이지는 연구 관심을 동적 보행(Dynamic Walking), 자세 제어(Postural Control), 감각 통합(Sensory Integration), 생체모사 센서(Biomimetic Sensors), 스포츠 생체역학과 계측(Sports Biomechanics and Instrumentation)으로 적는다.[^prof]

Professor 페이지의 Honors and Awards 칸은 1996–2014년 항목으로, 「Best Paper Award, Education division, Korean Society of Mechanical Engineers」(2014), 「KAIST Creative Teaching Award」(2014), 「Young Investigator Award, Bioengineering division, Korean Society of Mechanical Engineers」(2013), 「Young Investigator Award, Korea Women Engineering Society」(2011), 「Best Paper Award, Bioengineering division, Korean Society of Mechanical Engineering」(2008), 「ME outstanding Instructor Award」(2011, 2005, 2004), 「Outstanding Graduate Instructor Award, ASEE, The University of Michigan」(2002), 「Korean Government Overseas Scholarship Grantee」(1996–1998)를 적는다.[^prof] 학회 활동으로는 International Society of Gait and Posture Research와 Korean Society of Mechanical Engineers의 Board member(2014~), Korean Society of Mechanical Engineers Bioengineering Division과 Korean Society of Biomechanics의 Board member·Founding member(2007~)를 적고, 2008–2013년 여러 학술대회의 Organizing Committee, Program Chair 등을 맡았다고 적는다.[^prof] Notice 게시판에 따르면 교수는 2023년 7월 30일부터 8월 3일까지 일본 후쿠오카에서 열린 International Society of Biomechanics(ISB2023) 학술대회에서 「Complementary Roles of Biomechanics and Machine Learning in Human Motion Monitoring」을 주제로 기조 강연을 했다.[^notice]

논문으로 보면 최근 전문 분야는 네 갈래다. 강화학습 최적화로 사람의 자세 전략 전환을 설명하는 자세 제어 모델링(대표 논문 1),[^p1] 몸에 단 관성 센서 하나로 걷기의 에너지 소비량을 추정하는 방법과 그 학습 데이터를 모으는 절차(대표 논문 2, 3),[^p2][^p3] 손목 착용 관성 센서로 골프 스윙을 추적하는 웨어러블 동작 분석(대표 논문 4),[^p4] 태권도 보호구의 충격 감쇠로 타격력을 추정하는 스포츠 생체역학(대표 논문 5)이다.[^p5] 누리집 학술지 목록의 2004–2020년 논문에는 탄성 다리 보행 모델로 걸음의 역학을 설명한 연구, 사람의 자세 되먹임 반응과 운동 지각 연구, 전정기관 털세포의 섬모 다발(stereocilia)이 신호를 키우는 방식을 역학 모델로 나타내고 이를 본뜬 생체모사 관성 센서 연구도 있다.[^pubs]

## 응용 분야

기계공학과 연구분야 페이지는 교수 연구의 주요 응용 산업을 헬스케어, 모니터링과 트레이닝으로 적는다.[^mer] 연구 페이지는 웨어러블 기기와 휴대 기기 카메라로 현장에서 실시간으로 동작을 분석하려는 수요가 스포츠와 헬스케어 분야에서 늘고 있다고 적고, 에너지 소비량을 운동 수행 능력과 웨어러블 보조 기기를 평가하는 정량 지표로 든다.[^swv][^dw] Notice 게시판에 따르면 웨어러블 로봇 회사 Angel Robotics와 연구실은 2025년 2월 18일 웨어러블 로봇 기술의 산학 협력을 위한 업무 협약(MOU)을 맺었고,[^notice] 연구 페이지는 이 회사의 외골격(H10) 보조 효과 평가를 연구 주제로 든다.[^dw] 2025–2026년 특허 목록에는 웨어러블 기기를 이용한 골프 스윙 동작 분석 방법과 센서를 포함하는 전자 장치가 있다.[^patents]

## 구성원

연구실 누리집 Members 메뉴의 6명이다(박사후연구원 1, 박사과정 3, 석사과정 2). 과정은 페이지의 구역 이름(Postdoctoral Researchers, Ph.D Candidates, Master Candidates)이고, 연구 주제는 카드에 적힌 Research Interest, 이메일은 카드의 학교 주소다.[^members] 박사후연구원 Hong, Seongwoong은 Alumni 페이지에도 2025년 박사 졸업생으로 올라 있다.[^alumni] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Hong, Seongwoong | 박사후연구원 | Reinforcement Learning for Biomechanical Optimality | sw.hong@kaist.ac.kr | 1 |
| Chae, Minho | 박사과정 |  | minho.chae@kaist.ac.kr | 5 |
| Park, Guena | 박사과정 |  | guena.park@kaist.ac.kr |  |
| Yang, Eunbean | 박사과정 |  | eunbean.yang@kaist.ac.kr |  |
| Kim, Sangmin | 석사과정 |  | sangminkim@kaist.ac.kr |  |
| Kim, Gihyun | 석사과정 |  | gihyunkim@kaist.ac.kr |  |

## 졸업생과 이전 구성원

누리집 Alumni 페이지의 박사 졸업생 14명과 석사 졸업생 20명이다. 학위·과정 칸은 페이지의 구역(Ph.D. Alumni, Master’s Degree Alumni)이고, 연도는 각자 학력 칸에 적힌 그 학위의 연도다. 학력 칸에 그 학위 연도가 없는 2명(Jung, Changkeun; Lee, Sanghoon)과 학력 칸이 없는 1명(Jung, Hanna)은 연도를 비웠다. 진로는 각 카드의 「Currently」 줄이고, 학위 논문은 Theses 페이지가 같은 이름으로 적은 영문 제목과 연월이다.[^alumni][^theses]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Kim, Seyoung | Ph.D. (2011) | Korea Institute of Machinery & Materials | Human posture and gait control adjustability described by dynamic model (Feb 2011) |
| Yi, Yongwoo | Ph.D. (2011) | Samsung Display | Multi-sensory integration for the whole body linear motion perception (Feb 2011) |
| Park, Heewon | Ph.D. (2015) | LG Electronics | Study of human walking mechanism based on mechanical work analysis: young, elderly, and OA patients (Feb 2015) |
| Lee, Changwon | Ph.D. (2018) | Samsung Electronics | Unmeasured motion estimation method based on the novel dynamic model of golf swing motion (Feb 2018) |
| Lim, Hyerim | Ph.D. (2018) | Professor @Kumoh National Institute of Technology | Investigation of mechanical dominance of human walking through the dynamic analysis of lower limbs motions (Feb 2018) |
| Lee, Myunghyun | Ph.D. (2020) | Agency for Defense Development | Three dimensional walking dynamic model and its applications (Aug 2020) |
| Oh, Keonyoung | Ph.D. (2016) | Professor @Kyungpook National University | A dynamic analysis on mechanism of improved running economy by assisting foot joint stiffness (Aug 2016) |
| Choi, Hyeob | Ph.D. (2020) | Beflex Inc. | Three dimensional dynamics analysis of golf swing by solving upper limb closed chain problem (Aug 2020) |
| Jung, Changkeun | Ph.D. | Beflex Inc. |  |
| Kim, Bumjoon | Ph.D. (2023) | Korea Institute of Machinery & Materials as Post-doc | A Study on Estimating Energy Expenditure during Running Using Inertial Sensor: Incorporating Biomechanical Characteristics and Machine Learning (Aug 2023) |
| Kim, Myeongsub | Ph.D. (2023) | Samsung Electronics | A Study on Inertial Sensor-Based Motion Estimation Methods Applying Biomechanical Characteristics and Machine Learning: Application to Golf Swing Motion (Aug 2023) |
| Jeong, Hyunho | Ph.D. (2025) | KAIST(EXO Lab) as Post-doc | IMU-based estimation of energy expenditure and evaluation of exoskeletal assistance strategies using a time-efficient data collection protocol (Aug 2025) |
| Hong, Seongwoong | Ph.D. (2025) | KAIST(AI-CRED Institute) as Post-doc | Optimization Characteristics of Human Postural Control Transition via Reinforcement Learning (Aug 2025) |
| Jung, Jinsung | Ph.D. (2026) | Angel Robotics | Energy Expenditure Estimation Based on Gait Mechanics Using Wearable Devices (Feb 2026) |
| Lim, Koeun | M.S. (2008) | BIOTRONIK Neuro | Modeling of a biomimetic inertial sensor inspired by amplifying mechanisms of vestibular stereocilia bundle (Feb 2008) |
| Jang, Jeehoon | M.S. (2008) |  |  |
| Hwang, Byungchoon | M.S. (2008) |  | Changes of postural feedback gain scaling with constrained somatosensory cues (Aug 2008) |
| Kang, Hyunmin | M.S. (2009) |  | Gait strategy change as function of human walking speed (Feb 2009) |
| Jung, Hanna | M.S. |  |  |
| Park, Hyeyoung | M.S. (2010) |  |  |
| Yeom, Jin | M.S. (2010) | Agency for Defense Development | Finite collision model for the double support phase of human walking (Feb 2010) |
| Hong, Hyunhwa | M.S. (2012) |  | Mechanism of gait dynamics deterioration in the elderly walking (Feb 2012) |
| Kim, Juhyung | M.S. (2012) |  |  |
| Jung, Ju-Ho | M.S. (2012) | Beflex Inc. |  |
| Song, Hyunggwi | M.S. (2015) | Professor @Chungbuk National University |  |
| Ryu, Hansol | M.S. (2016) | Georgia Tech as Post-doc | Estimating anterior-posterior ground reaction force using compliant legged walking model (Feb 2016) |
| Choi, Osung | M.S. (2017) | Hyundai Motors |  |
| Lee, Eunkang | M.S. (2017) | Hyundai Motors | Study on motion sickness on HMD system latency in rotation and translation stimulus (Feb 2017) |
| Park, Junhyeok | M.S. (2018) | Samsung Electronics |  |
| Kim, Jeongheon | M.S. (2020) | Samsung Electronics | Design of golf putting detection algorithm based on a inertial-sensor using natural frequency (Feb 2020) |
| Lee, Kibum | M.S. (2021) | Assistant Research Engineer @ Telepix | Prediction of wrist position using the data set from single inertial sensor and artificial neural networks in upper limb repetitive rotational motion (Feb 2022) |
| Lee, Sanghoon | M.S. |  |  |
| Kim, Keonwoo | M.S. (2025) | Hankook Tire | Biomechanical modeling of upper limb and center of mass estimation based on wrist position data for wearable applications (Aug 2025) |
| Park, Wooyoung | M.S. (2026) |  |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications 메뉴의 2021–2026년 논문 57편이다. International Journal 목록에 출판 논문으로 오른 학술지 5편(2024–2026년), International Conference 목록의 국제 학회 발표 16편(2021–2025년), Domestic Conference 목록의 국내 학회 발표 36편(2023–2025년)이며, 연도마다 이 순서로 적었다. 각 줄은 누리집이 적은 저자, 제목, 학술지·학회, 연도를 그대로 옮긴 것이다.[^pubs]

**2026**

- Minho Chae, Jonghak Hwang, Woosup Han, Sihyun Ryu, Sangkyoon Park, Sukyung Park, Estimating Actual Striking Forces Using Attenuation Properties of Taekwondo Protectors, PLOS ONE 21(1), 2026

**2025**

- Jinsung Jung, Hyerim Lim, Hyunho Jeong, Sameer Upadhye, Joo H. Kim and Sukyung Park, Estimation of Walking Energy Expenditure using a Single Sacrum-Mounted IMU Based on Biomechanically-Informed Machine Learning, Scientific Reports, 25.15, 2025
- Hyunho Jeong, and Sukyung Park, A Time-Efficient Continuous Ramp Protocol for Data-Driven Walking Energy Expenditure Estimation across Multiple Speeds, Journal of NeuroEngineering and Rehabilitation 22.206 ,2025.
- Seongwoong Hong, and Sukyung Park, Biomechanical Optimization and Reinforcement Learning Provide Insights into Ankle-to-Hip Strategy Transitions in Human Postural Control, Scientific Reports 25.15, 2025.
- Wooyoung Park and Sukyung Park, sEMG Prediction Using Gait Kinematics and Machine Learning, International Society of Biomechanics, 2025
- Seongwoong Hong and Sukyung Park, Learning Human Postural Strategies: Reinforcement Learning Approach Incorporating a CoP Constraint, International Society of Biomechanics, 2025
- Hyunho Jeong and Sukyung Park, Time-Efficient Protocol for Personalizing Hip Exoskeleton Assistance Using a Respiratory Kinetics, International Society of Biomechanics, 2025
- Minho Chae, Jonghak Hwang, Wooseop Han, Sangkyoon Park, Sihyun Ryu and Sukyung Park, Actual Strike Force Estimation in Combat Sports Using Correlated Sensor Data, International Society of Biomechanics, 2025
- Guena Park and Sukyung Park, Inertial Measurement Unit Data Correction Using Consumer-grade Camera Recordings for Golf Swing Monitoring, International Society of Biomechanics, 2025
- Wooyoung Park, Eunbean Yang, Joo H. Kim and Sukyung Park, Beyond Mechanical Work: Heat Loss in Energy Expenditure, International Society of Biomechanics, 2025
- Jinsung Jung, Joo H. Kim and Sukyung Park, Stance Leg Sagittal Power as a Predictor of Whole Body Energy Expenditure in Walking, International Society of Biomechanics, 2025
- 박수경, 양은빈, 보행 시 하지 열유속의 변화 특성에 관한 고찰, 대한기계학회, 2025
- 박수경, 채민호, XAI 기반 보행 시 무게중심 운동학의 주요 상체 인자 분석, 대한기계학회, 2025
- 박수경, 박우영, 중강도 운동 시 위상각과 혈당 변화 사이의 상관관계 고찰, 대한기계학회, 2025
- 박수경, 정진성, 달리기 시 지지다리 발목 관절 역학을 재현하는 Unified-SLIP 모델, 대한기계학회, 2025
- 박수경, 홍성웅, 정시우, 박근아, Analysis of Age-Related Changes in Postural Control Characteristics using RL, 대한기계학회, 2025
- 양은빈, 박수경, 보행 시 하지 열유속 특성과 에너지 소비량 변동성과의 연관성 고찰, 대한생체역학회, 2025
- 박근아, 박수경, 생체역학 AI를 활용한 IMU 기반 스윙 모션 추정 연구, 대한생체역학회, 2025
- 채민호, 박수경, 보행 시 무게중심의 운동학 특성에 대한 기여도 고찰, 대한생체역학회, 2025
- 양은빈, 박우영, 박수경, 에너지 소비량 변동성과 열손실간 상관관계 고찰: 걷기를 중심으로, 대한기계학회, 2025
- 정진성, 김주현, 박수경, 걷기 시 지지다리 시상면 역학 일 기반 전신 에너지소비량 추정, 대한기계학회, 2025
- 김건우, 채민호, 박수경, 웨어러블 기반 보행 분석을 위한 팔 스윙 동작의 동역학 기반 모델링, 대한기계학회, 2025
- 박근아, 박수경, 골프 스윙 임팩트 전후 손목 궤적 추정을 위한 IMU–영상 결합 방법, 대한기계학회, 2025

**2024**

- Myeongsub Kim, and Sukyung Park, Enhancing Accuracy and Convenience of Golf Swing Tracking with a Wrist-Worn Single Inertial Sensor, Scientific Reports 24.14, 2024
- 양은빈, 박우영, 이상훈, 전유진, 박형순, 박수경, 열유속이 대사 에너지 소비량 변동성에 미치는 영향, 대한기계학회, 2024
- 박근아, 박수경, 비전데이터 학습을 통한 IMU 기반 모션 추정 연구, 대한기계학회, 2024
- 정진성, 박수경, 다리길이 변화 특성을 고려한 달리기 시 발목 토크 재현, 대한기계학회, 2024
- 김건우, 유소현, 박수경, 보행 동역학 상관관계를 활용한 단일 손목 관성센서 기반 지면반력 추정 방법 연구, 대한기계학회, 2024
- 채민호, 홍찬표, 박수경, 진동 특성 활용 격투기 타격 충격력 추정 방안 제시 , 대한기계학회, 2024
- 홍성웅, 박수경, 자세 제어 전환 메커니즘:제약조건으로 인한 제어 목표 우선순위 변화 학습 ,대한생체역학회, 2024
- 박근아, 박수경, 골프 스윙 일관성을 활용한 IMU 기반 스윙 모션 추정 연구 ,대한생체역학회, 2024
- 정진성, 박수경, 타원형 편심 발의 SLIP모델 적용을 통한 달리기 시 하지 관절 궤적 재현 ,대한생체역학회, 2024
- 김건우, 박수경, 보행동작 연관성을 활용한 단일 손목 관성센서 데이터 기반 전후방 지면반력 추정 방법 연구 ,대한생체역학회, 2024
- 채민호, 홍찬표, 박수경, 역동역학 기반 격투기 타격 충격력 측정 방안 제시, 대한생체역학회, 2024
- 박근아, 박수경, 멀티모달기반 골프 스윙 시 손목 IMU 오리엔테이션 보정 방법 연구, 대한기계학회 바이오공학부문, 2024
- 채민호, 박수경, 태권도 전자호구의 실험적 분석을 통한 점수 인식 실패 원인 규명, 대한기계학회 바이오공학부문, 2024
- 정현호, 박수경, 데이터 효율적인 기계 학습 기반 보행 에너지 소비량 추정 기법, 대한기계학회 바이오공학부문, 2024
- 홍성웅, 박수경, 강화학습을 사용한 직립 자세제어 시 제약조건이 제어 적응에 미치는 영향 고찰, 대한기계학회 바이오공학부문, 2024
- 정진성, 홍성웅, 정시우, 노승주, 박수경, 지면반력 주파수 특성을 활용한 달리기 시 IMU 기반 착지패턴 분류, 대한기계학회 바이오공학부문, 2024

**2023**

- Seungjoo Noh, and Sukyung Park, The static method of computing leg stiffness in running measures a smaller value than the dynamic method, International Society of Biomechanics, 2023
- Myeongsub Kim, and Sukyung Park, Tracking golf swing trajectory using a single imu by applying biomechanics and machine learning, International Society of Biomechanics, 2023
- Jinsung Jung, Jongbin Kim, Sang-Kyoon Park and Sukyung Park, Changes in Leg Stiffness as a Result of Differences in Leg BMD in Various Age Groups During Running, International Society of Biomechanics, 2023
- Seongwoong Hong and Sukyung Park, Emulating human postural control adjustment with perturbation using quadratic objective function, International Society of Biomechanics, 2023
- Bumjoon Kim, and Sukyung Park, Improving estimation accuracy of energy expenditure during running from a single IMU by estimating mechanical power via estimating ground reaction force, International Society of Biomechanics, 2023
- 정현호, 박수경, 연속적 보행 에너지 소모량 측정 방법의 오차 분석, 대한생체역학회, 2023
- 홍성웅, 박수경, 강화학습을 활용한 사람 자세제어 모사, 대한생체역학회, 2023
- 정진성, 박수경, 달리기 시 연조직 에너지 소산 추정 모델링, 대한생체역학회, 2023
- 정현호, 박수경, 전이학습을 이용한 단일 IMU 기반 보행 에너지 소비량 추정 방법, 대한기계학회, 2023
- 홍성웅, 박수경, 생체역학 제한조건을 반영한 최적제어를 활용한 직립 자세제어 변화 예측, 대한기계학회, 2023
- 김범준, 박수경, 단일 관성센서로부터 생체역학 지표 도출을 통한 달리기시 에너지 소비량 추정 정확도 향상 연구, 대한기계학회 바이오공학부문, 2023
- 김명섭, 박수경, 생체역학과 머신러닝을 이용한 단일 관성센서 기반 골프 스윙 모니터링 정확도 향상 기술, 대한기계학회 바이오공학부문, 2023
- 정진성, 박수경, 인체 연조직 상대운동을 반영한 달리기 시 지면반력 임팩트 모델링, 대한기계학회 바이오공학부문, 2023
- 홍성웅, 박수경, 최적제어를 활용한 외란에 따른 자세제어 전략 변화 재현, 대한기계학회 바이오공학부문, 2023

**2021**

- Seongwoong Hong, Jung Kim, and Sukyung Park, Identifying the Objective of Human Behavior using Inverse Reinforcement Learning, International Society of Biomechanics, 2021
- Jinsung Jung, Jung Kim, and Sukyung Park, Reproducing the characteristics of sEMG MPF change based on joint mechanical work, International Society of Biomechanics, 2021
- Myeongsub Kim, Jung Kim, and Sukyung Park, Meta-learning for personalized golf swing monitoring to overcome motion variability between users, International Society of Biomechanics, 2021
- Bumjoon Kim, and Sukyung Park, Internal work could be used to estimate energy expenditure at various running intensities, International Society of Biomechanics, 2021

## 특허

누리집 Patent 목록의 2021–2026년 항목 3건이다. 연도는 목록이 적은 연도이고, 목록에는 출원·등록 구분과 번호가 없다.[^patents]

- 2026 · 센서를 포함하는 전자 장치 및 그의 동작 방법 (발명자 박수경, 채민호, 박근아, 황진환, 신승혁, 강정관)
- 2025 · 근감소증의 조기 징후를 진단하는 방법 및 그 장치 (발명자 박수경)
- 2025 · 웨어러블 기기를 이용한 골프 스윙 동작 분석 방법, 이를 제공하는 컴퓨팅 장치 및 컴퓨터 프로그램 (발명자 박수경, 박근아)

## 소식

누리집 Notice 게시판의 글 3건 전부다. 날짜는 게시일이고 제목은 게시판 표기 그대로다.[^notice]

- 2025-06-23 · Angel Robotics and Biomechanics Lab Sign MOU for Joint Research on Wearable Robots
- 2023-08-16 · Prof. Park gave a keynote at ISB/JSB 2023
- 2022-06-24 · Our Lab on ME newsletter!

## 연락과 위치

- 주소: (34141) 대전광역시 유성구 대학로 291 한국과학기술원 기계공학동 2216호[^contact]
- 연구실 전화·팩스: 042-350-3271 / 042-350-5230[^contact]
- 교수 연구실: 기계동(N7-3) 5204호, 전화 042-350-3230[^prof][^mep]
- 교수 이메일: sukyungp@kaist.ac.kr[^prof][^mep]
[^p1]: S. Hong, S. Park, Scientific Reports 15, 13640 (온라인 2025-04-20). <https://doi.org/10.1038/s41598-025-97637-5> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J. Jung 외, S. Park, Scientific Reports 15, 44933 (온라인 2025-12-29). <https://doi.org/10.1038/s41598-025-28393-9> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: H. Jeong, S. Park, Journal of NeuroEngineering and Rehabilitation 22, 206 (온라인 2025-10-01). <https://doi.org/10.1186/s12984-025-01707-8> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: M. Kim, S. Park, Scientific Reports 14, 9201 (온라인 2024-04-22). <https://doi.org/10.1038/s41598-024-59949-w> 초록 기준.
[^p5]: M. Chae 외, S. Park, PLOS One 21, e0328749 (온라인 2026-01-13). <https://doi.org/10.1371/journal.pone.0328749> 초록 기준.
[^home]: 생체역학 연구실 누리집 첫 화면 <https://biomech.kaist.ac.kr/> (연구 분야 소개, 연구실 소개 문장, 연락처, 2026-10-23 열람)
[^greet]: 생체역학 연구실 누리집 Greetings 페이지 <https://biomech.kaist.ac.kr/?page_id=24> (2026-10-23 열람)
[^contact]: 생체역학 연구실 누리집 Contact Us 페이지 <https://biomech.kaist.ac.kr/?page_id=35> (주소, 전화·팩스, 2026-10-23 열람)
[^prof]: 생체역학 연구실 누리집 Professor 페이지 <https://biomech.kaist.ac.kr/?page_id=43> (연락처, Research Interests, Education, Honors and Awards, Professional Affiliations & Activities, 2026-10-23 열람)
[^dw]: 생체역학 연구실 누리집 Research: Dynamic Walking & Energetics 페이지 <https://biomech.kaist.ac.kr/?page_id=112> (2026-10-23 열람)
[^pc]: 생체역학 연구실 누리집 Research: Postural Control & Sensory Integration 페이지 <https://biomech.kaist.ac.kr/?page_id=113> (2026-10-23 열람)
[^swv]: 생체역학 연구실 누리집 Research: Smart Wearables & Vision Applications 페이지 <https://biomech.kaist.ac.kr/?page_id=114> (2026-10-23 열람)
[^sb]: 생체역학 연구실 누리집 Research: Sports Biomechanics 페이지 <https://biomech.kaist.ac.kr/?page_id=115> (2026-10-23 열람)
[^members]: 생체역학 연구실 누리집 Members 메뉴: Doctoral Researchers <https://biomech.kaist.ac.kr/?page_id=56>, Master Candidates <https://biomech.kaist.ac.kr/?page_id=73> (2026-10-23 열람)
[^alumni]: 생체역학 연구실 누리집 Alumni 페이지 <https://biomech.kaist.ac.kr/?page_id=74> (Ph.D. Alumni, Master’s Degree Alumni, 2026-10-23 열람)
[^theses]: 생체역학 연구실 누리집 Theses 페이지 <https://biomech.kaist.ac.kr/?page_id=1946> (Doctoral Dissertation, Master’s Thesis, 2026-10-23 열람)
[^pubs]: 생체역학 연구실 누리집 Publications 메뉴: International Journal <https://biomech.kaist.ac.kr/?page_id=137>, International Conference <https://biomech.kaist.ac.kr/?page_id=144>, Domestic Conference <https://biomech.kaist.ac.kr/?page_id=1951> (목록 범위는 근거 페이지, 2026-10-23 열람)
[^patents]: 생체역학 연구실 누리집 Patent 페이지 <https://biomech.kaist.ac.kr/?page_id=831> (2026-10-23 열람)
[^notice]: 생체역학 연구실 누리집 Notice 게시판 <https://biomech.kaist.ac.kr/?cat=9> (2026-10-23 열람)
[^mep]: KAIST 기계공학과 교수 소개(박수경) <https://me.kaist.ac.kr/pop/team.html?uid=21&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 이메일, 연구실 위치, 전화, 2026-10-23 열람)
[^mel]: KAIST 기계공학과 교수진 목록 <https://me.kaist.ac.kr/team/team_010100.html> (박수경 교수 항목, 2026-10-23 열람)
[^mer]: KAIST 기계공학과 연구분야 로보틱스/제어/모빌리티 페이지 <https://me.kaist.ac.kr/research/research_010100.html> (박수경 교수의 연구주제·주요 응용 산업·연구실 항목, 2026-10-23 열람)

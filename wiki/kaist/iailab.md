# 산업 인공지능 연구실 (Industrial Artificial Intelligence Laboratory, iAI Lab)

**KAIST 기계공학과 · 이승철 교수**

- 분야: 물리 지식을 넣은 인공지능(물리 정보 신경망·연산자 학습)으로 유동·열 문제 풀기, 능동 학습을 쓴 금속·2차원 소재·3D 프린팅 수지의 조건 탐색, 설비 진단용 진동 신호 생성, 마이크 배열을 쓴 음원 위치 추정과 음향 기반 공간 추정
- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 과학·공학 AI[^home][^p1][^p4], 유체역학·유동[^projects][^p1][^p2], 3D 프린팅[^p3][^p5], 스마트 제조[^projects][^p3][^p6], 고장 진단·수명 예측[^p6], 음향·오디오 AI[^topics][^p7][^p8]
- 홈페이지: <https://iailab.kaist.ac.kr/>
- 근거와 출처: [산업 인공지능 연구실 근거 페이지](iailab-sources.md)

> 기계공학을 바탕으로 여러 공학 시스템에 인공지능을 적용하는 KAIST 기계공학과 연구실이다. 물리 법칙을 학습에 넣은 신경망으로 유동·열 문제를 풀고, 기계학습으로 금속 합금·2차원 소재·3D 프린팅 수지의 조건을 찾으며, 설비 진단용 진동 신호를 만들고 소리로 음원의 방향과 방의 모양을 추정한다. 연구실은 2023년 8월 KAIST로 옮겨 왔다.[^home][^topics][^news]

## 무엇을 연구하나

연구실 누리집 첫 화면은 연구실을 Industrial Artificial Intelligence (iAI) Laboratory로 소개하고, 첨단 인공지능 기술로 여러 산업의 AI 혁신을 이끄는 것을 목표로 한다고 적는다.[^home] 기계공학에 뿌리를 두고 다양한 공학 시스템에 AI를 적용하는 일에 집중하며, AI의 기초 이해는 필요하지만 이론 개발보다 AI 응용(AIX)에 더 무게를 둔다고 밝힌다.[^home] 핵심 연구 영역으로는 물리 정보 기반 AI(Physics-Informed AI, 물리 법칙에 관한 지식을 학습에 넣은 인공지능), 공학을 위한 대형 언어 모델(LLM, 많은 글을 학습해 글을 이해하고 만들어 내는 큰 인공지능 모델), 물리적 AI(Physical AI, 실제 몸체를 갖고 주변 환경과 주고받으며 움직이는 인공지능과 지능형 시스템)의 세 가지를 든다.[^home] 연구실에 들어오려는 사람에게는 제조 AI, 로봇 AI, 소재 AI, 의료 AI의 네 영역을 제시한다.[^home]

TOPICS 페이지는 같은 세 핵심 영역 아래 AI + Manufacturing, AI + Materials, AI + Acoustics, AI + Physics, AI + Healthcare, AI + Robotics의 여섯 묶음을 둔다.[^topics] 교수 소개 페이지는 교수의 연구가 기계 시스템, 스마트 제조, 소재, 헬스케어를 위한 산업 인공지능에 초점을 두고, KAIST에서 지식이 이끄는 AI(knowledge-guided AI)와 AI가 이끄는 지식 발견(AI-driven knowledge discovery)으로 넓혀 간다고 적는다.[^prof] 기계공학과 교수 소개는 연구분야를 Industrial AI, Manufacturing AI, Physics-informed AI로 적는다.[^meprof]

## 주요 연구 주제

### 1. 물리 지식 기반 인공지능

유동이나 열전달처럼 편미분 방정식(여러 변수에 대한 변화율 사이의 관계로 물리 현상을 나타내는 방정식)으로 기술되는 현상을, 물리 지식을 넣은 신경망으로 풀거나 시뮬레이션 대신 계산하게 한다. 연구실은 핵심 연구 영역의 첫째로 물리 정보 기반 AI를 들고,[^home] 과제 목록에는 연구실이 KAIST로 옮긴 2023년 8월 28일에 시작한 「물리기반 인공지능의 공학 분야 활용을 위한 요소 기술 연구」(한국과학기술원, 2023.08.28–2026.12.31, PI)가 있다.[^projects][^news] 같은 목록에는 포스코홀딩스 지원으로 CFD(전산유체역학, 유체의 흐름을 컴퓨터로 수치 계산하는 방법) 결과를 CNN 기반 U-net(영상의 각 화소 값을 예측하도록 만든 합성곱 신경망 구조)으로 내삽(이미 계산한 점들 사이의 값을 추정하는 일)하는 과제(2024.05.03–2025.04.25)와 DeepONet 기반 연산자 학습(함수를 입력받아 함수를 내놓는 대응 관계를 신경망으로 배우는 방법)으로 CFD 결과를 내삽·고해상화하는 과제(2025.07–2025.12), 풍산-KAIST 미래기술연구센터 지원으로 물리지식인공지능 기반 시뮬레이션 대리 모델링(시뮬레이션의 입력과 출력 관계를 학습해 시뮬레이션 대신 결과를 내는 모델을 만드는 일)을 통해 탄 공력 성능(탄이 공기 속을 날 때 받는 힘에 관한 성능)을 예측하는 과제(2026.01–)가 있다.[^projects] 대표 논문 1은 주파수별로 나눈 흐름의 모드 표현을 DeepONet에 넣어 시간에 따라 변하는 흐름을 예측했고, 대표 논문 2는 물리 정보 신경망(PINN, 물리 법칙을 나타내는 방정식을 학습의 오차 계산에 넣어 그 법칙을 따르도록 학습시키는 신경망)이 유체 문제에서 국소 최솟값(일정한 범위 안에서만 최소인 값)에 빠지는 문제를 학습 매개변수를 주기적으로 다시 조절하는 방법으로 다뤘다.[^p1][^p2]

### 2. 소재 인공지능

기계학습으로 소재의 공정 조건과 조성을 고르고, 계산이나 실험 횟수를 줄여 원하는 소재를 찾는다. 첫 화면은 연구 영역의 하나로 소재 AI를 들고, TOPICS 페이지는 AI + Materials 묶음을 둔다.[^home][^topics] 과제 목록에는 co-PI로 참여하는 「인공지능 기술 및 데이터를 활용한 우주항공용 초내열 비철 금속소재의 HUB 구축」(과학기술정보통신부, 2024.07–2028.12)과 포스코홀딩스 지원으로 진행 중인 「물리지식기반 미세조직 예측 인공지능 모델 개발」(PI)이 있다.[^projects] 대표 논문 3은 파레토 능동 학습(서로 맞바뀌는 두 성질을 함께 따지며 다음에 실험할 후보를 기계학습 모델이 고르는 방법)으로 3D 프린팅한 Ti-6Al-4V 합금의 공정·열처리 조건을 찾았고, 대표 논문 4는 능동 학습으로 MXene(주기율표 가운데 부분의 금속 원소인 전이금속이 탄소나 질소와 결합한 화합물, 곧 탄화물·질화물로 된 원자 몇 층 두께의 2차원 소재) 가운데 열역학적으로 안정한 것을 가려냈으며, 대표 논문 5는 회귀 모델로 3D 프린팅용 엘라스토머(잡아당기면 늘어났다가 힘을 빼면 원래 모양으로 돌아오는 고분자) 수지의 배합을 찾았다.[^p3][^p4][^p5]

### 3. 제조 공정과 설비 진단 인공지능

제조 공정과 설비에서 나오는 데이터로 공정 조건을 정하고 설비 고장을 진단하는 인공지능을 연구한다. 첫 화면은 연구 영역의 하나로 제조 AI를 들고, TOPICS 페이지는 AI + Manufacturing 묶음을 둔다.[^home][^topics] 과제 목록에는 co-PI로 참여하는 「AI 기반 지능형 설계-제조 통합 연구단 (InnoCORE)」(과학기술정보통신부, 2025.07–)과 「첨단제조지능혁신센터 (글로컬랩)」(교육부, 한국연구재단, 2025.09–)이 있다.[^projects] 대표 논문 3은 레이저로 금속 가루를 녹여 쌓는 3D 프린팅 공정의 조건을 능동 학습으로 찾았다.[^p3] 대표 논문 6은 고장 예지·건전성 관리(PHM, 설비 상태를 살펴 고장을 미리 알아내고 남은 수명을 예측해 관리하는 일)용 진단 모델을 학습시킬 고장 진동 신호가 부족한 문제를 다뤄, 사용자가 신호 특징을 조절하며 진동 신호를 만드는 생성 모델을 제안했다.[^p6]

### 4. 음향 인공지능

소리를 재고 분석해 소리가 나는 곳과 공간의 모양을 알아낸다. TOPICS 페이지의 AI + Acoustics 묶음은 평면형과 구형 마이크 배열(여러 마이크를 정해진 모양으로 늘어놓은 측정 장치)로 여러 음원의 위치를 높은 해상도와 정확도로 찾는 소리 가시화(Sound Visualization)를 소개한다.[^topics] 과제 목록에는 한국표준과학연구원 지원의 「이동식 모니터링을 위한 음향 신호의 예측 및 분리 기술 개발」(2023.01.01–2023.12.31, PI)이 있다.[^projects] 대표 논문 7은 마이크 네 개로 된 배열에서 소리 세기 측정의 치우침을 가역 신경망(입력에서 출력으로, 출력에서 입력으로 양쪽 계산이 모두 되는 신경망)으로 보정해 소리가 오는 방향을 추정했고, 대표 논문 8은 음향 반향(소리가 벽에 부딪혀 되돌아온 것)으로 방의 평면도와 높이 지도를 추론하는 EchoScan을 제안했다.[^p7][^p8]

## 대표 논문

이승철 교수가 교신저자인 2024–2026년 학술지 논문 가운데 KAIST 소속으로 발표했고 초록을 확인할 수 있는 여덟 편을 네 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다. 연도는 출판사 서지의 출판 연도다. 누리집 논문 목록은 일부 저자 이름 뒤에 *, 공동 1저자에 +를 붙이며, 표의 교신저자와 공동 1저자는 이 표시를 따랐다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^journal] |
|---|---|---|---|---|
| 1 | 2026 | [Spectral Modal Operator Learning Framework with Decoupled Spatial and Temporal Representations for Unsteady Flows](https://doi.org/10.1063/5.0327449) · Physics of Fluids | 시간에 따라 변하는 물리 현상은 시간 의존 편미분 방정식으로 기술되며, 조건을 바꿔 가며 수치 시뮬레이션을 되풀이하면 계산 비용이 크다. POD-DeepONet 같은 기존 연산자 학습 틀은 모드 분해(복잡한 변동을 몇 가지 기본 패턴의 합으로 나누는 방법)에서 공간과 시간 표현이 얽혀 있어 고주파 변동과 비선형 모드 사이의 상호작용을 잡기 어렵다. 이 논문은 주파수별로 나눈 모드 표현을 DeepONet 구조에 넣은 SPOD-DeepONet을 제안했다. 여러 조건에서 뽑은 공간 기저(흐름의 모양을 나타내는 기본 패턴)를 트렁크 신경망(DeepONet에서 위치를 입력받는 부분 신경망)에 넣고, 시간과 조건을 맡는 하위 신경망으로 이뤄진 브랜치 신경망(DeepONet에서 조건을 입력받는 부분 신경망)이 시간·조건에 따른 계수를 예측해 공간 표현을 시간·조건 변화와 떼어 놓았다. 시간에 따라 바뀌는 흐름의 기준 문제 두 개에서 큰 규모와 작은 규모의 변동을 모든 시간 구간에 걸쳐 정확히 잡았고, Naïve-DeepONet, Fourier Neural Operator, POD-DeepONet과 비교해 더 빨리 수렴했으며 고주파 소용돌이 구조를 더 잘 복원하고 물리적으로 일관된 파워 스펙트럼 밀도(신호의 세기가 주파수별로 나뉜 분포) 분포를 냈다.[^p1] | 공동 1저자 C. Won(Chaeyun Won)·J. Lee(Jongmok Lee), 교신저자 이승철 (5명) |
| 2 | 2025 | [Physics Informed Neural Networks for Fluid Flow Analysis with Repetitive Parameter Initialization](https://doi.org/10.1038/s41598-025-99354-5) · Scientific Reports | 물리 정보 신경망은 편미분 방정식으로 기술되는 물리계의 거동을 잡는 데 널리 쓰여 왔지만, 다루기 까다로운(stiff) 유체 문제에서는 흐름이 정체되는 문제를 겪고 국소 최솟값으로 수렴해 물리적으로 맞지 않는 해를 내곤 한다. 이 논문은 학습 매개변수를 주기적으로 조절해 국소 최솟값에서 빠져나와 다른 해를 찾게 하는 "재초기화" 학습 전략을 제안했다. 높은 레이놀즈 수(흐름에서 관성의 효과와 점성의 효과의 비를 나타내는 수) 700과 1,000의 2차원 정상 상태(시간이 지나도 변하지 않는 상태) 뚜껑 구동 공동 유동(윗면이 움직이는 네모난 공간 안의 흐름)에서 소용돌이와 전단층(속도가 다른 흐름이 맞닿아 어긋나는 층)을 모의했고, 두 경우 모두 가장 낮은 평균 제곱 오차(예측과 정답 차이의 제곱을 평균한 값)를 얻었다고 보고했다. 주성분 분석(여러 변수에 흩어진 자료의 변화를 소수의 새 축으로 요약하는 통계 방법)으로 학습 중 모델 매개변수가 조절되는 모습도 확인했다.[^p2] | 공동 1저자 J. Lee(Jongmok Lee)·S. Shin(Seungmin Shin), 교신저자 M. Choi(Minseok Choi)·이승철 (8명) |
| 3 | 2025 | [Active Learning Framework to Optimize Process Parameters for Additive-manufactured Ti-6Al-4V](https://doi.org/10.1038/s41467-025-56267-1) · Nature Communications | 레이저 분말 베드 용융(금속 가루를 얇게 깔고 레이저로 녹여 한 층씩 쌓는 3D 프린팅 방식)으로 Ti-6Al-4V 합금(티타늄에 알루미늄과 바나듐을 섞은 합금)을 만들 때, 강도와 연성(끊어지지 않고 늘어나는 성질)이 서로 맞바뀌는 관계 때문에 시행착오로 공정·열처리 조건을 찾기는 비효율적이다. 이 논문은 파레토 능동 학습과 목표를 정한 실험 검증으로 296개 후보의 조건 공간을 탐색해 강도와 연성을 함께 높이는 조건을 찾았다. 찾은 조건으로 만든 합금은 모두 기존 연구의 합금과 비교해 비슷한 강도에서는 연성이 더 높고 비슷한 연성에서는 강도가 더 높았으며, 최종적으로 극한 인장 강도(끊어지기 전까지 견딘 최대 인장 응력) 1190 MPa과 총 연신율(끊어질 때까지 늘어난 길이의 비율) 16.5%의 합금을 만들었다.[^p3] | 공동 1저자 J. A. Lee(Jeong Ah Lee)·J. Park(Jaejung Park), 교신저자 이승철·H. S. Kim(Hyoung Seop Kim) (7명) |
| 4 | 2024 | [Active Learning Framework for Expediting the Search of Thermodynamically Stable MXenes](https://doi.org/10.1021/acsnano.4c08621) · ACS Nano | MXene은 조성과 원소 비율이 다양해 전극, 촉매, 슈퍼커패시터(전기를 짧은 시간에 저장했다 내놓는 축전 장치) 등에 쓰일 수 있는데, 그러려면 먼저 열역학적으로 안정하고 합성할 수 있는 MXene을 가려내야 한다. 밀도 범함수 이론(DFT, 양자역학으로 물질의 전자 구조와 에너지를 계산하는 방법)으로 계산한 볼록 껍질 위 에너지(Ehull, 같은 조성에서 에너지가 최저인 물질 조합과 그 물질 사이의 에너지 차이)가 안정성을 가늠하는 척도지만 계산 비용이 커 탐색 범위가 좁다. 이 논문은 대리 모델과 효용 함수(다음에 계산할 후보의 가치를 점수로 매기는 함수)로 이뤄진 능동 학습 틀을 제안해, 23,857개 MXene 가운데 DFT 계산 480번만으로 열역학적으로 안정한 MXene 126개를 찾았고 그중 89개는 안정성이 보고된 적이 없었다. 무작위로 고른 1693개 MXene에서는 안정한 것이 2개뿐이었다.[^p4] | 1저자 J. Park(Jaejung Park), 교신저자 H. Park(Haesun Park)·이승철 (6명) |
| 5 | 2026 | [Machine Learning Guided Formulation Design of DLP Printable Elastomers Beyond Viscosity Stretchability Tradeoff](https://doi.org/10.1038/s41467-026-73735-4) · Nature Communications | 통 광중합(액체 수지가 담긴 통에 빛을 쬐어 한 층씩 굳히는 3D 프린팅 방식)용 고성능 수지는 점도(액체의 끈끈한 정도), 굳는 속도, 기계적 성질이 서로 얽혀 개발이 어렵고, 프린팅으로 시험하는 기존 방식은 점도가 높거나 느리게 굳는 배합을 평가하지 못한다. 이 논문은 소량 배합 선별, 기계학습 최적화, 기능 검증을 잇는 데이터 효율적인 절차를 제시했다. 프린팅이 되는 배합과 되지 않는 배합을 아우르는 배합 목록을 만들고 작은 틀에서 굳혀 물성을 재어, 프린팅 한계와 떼어 학습 자료의 범위를 넓혔다. 점도, 굳는 시간, 파단 연신율(끊어질 때까지 늘어난 비율), 인장 탄성률(당길 때 생기는 응력과 늘어난 비율 사이의 비례 상수)로 학습한 회귀 모델로 가공성이 알맞고 잘 늘어나는 배합을 찾았고, 열·기계 분석에서 고른 그물 구조와 향상된 안정성을 확인했으며 프린팅한 부품은 튼튼한 내구성을 보였다. 저자들은 이 절차가 소프트 로봇과 프로그래밍 가능한 3차원 장치용 기능 소재 설계에 쓰일 수 있다고 적는다.[^p5] | 공동 1저자 Y. Song(Younghan Song)·B. Park(Bumsoo Park), 교신저자 이승철·J. Na(Jongbeom Na) (6명) |
| 6 | 2026 | [Deep Learning-based Vibration Signal Generation with Frequency-Amplitude Variability](https://doi.org/10.57062/ijpem-st.2026.00052) · International Journal of Precision Engineering and Manufacturing-Smart Technology | 기계학습 기반 설비 진단은 고장 예지·건전성 관리에 중요하지만, 산업 현장의 고장 데이터, 특히 진동 신호가 부족해 실제로 쓰기 어렵다. 생성적 적대 신경망(GAN, 데이터를 만드는 신경망과 진짜인지 가리는 신경망이 서로 겨루며 학습하는 생성 모델) 같은 기존 데이터 생성 방법은 특정 고장 유형만 만들 뿐 사용자가 신호 특성을 조절할 수 없었다. 이 논문은 Information Maximizing GAN(생성 조건과 결과 사이의 정보량을 키우도록 학습해 만든 데이터의 특징을 조절할 수 있게 한 GAN)에 합성곱 블록 주의 모듈(CBAM, 신경망이 중요한 특징과 위치에 가중치를 두게 하는 구성 요소)을 결합해 생성 과정에 신호 특징 정보를 넣고, 정규분포의 확률 밀도 함수(값이 어디에 얼마나 몰려 있는지 나타내는 함수)에 기반한 손실 함수(모델의 출력이 목표와 얼마나 다른지 재는 함수)로 신호 특징을 정답 표시 없이 뽑아 조절하게 했다. 만든 진동 데이터를 실제 데이터와 정성·정량 비교로 검증했고, 생성한 특징이 조절되는 것을 확인했다.[^p6] | 공동 1저자 H. Park(Hyungsik Park)·M. Lee(Minhyung Lee), 교신저자 이승철 (5명) |
| 7 | 2025 | [Dual-port Conditional Invertible Neural Network for Sound Intensity Compensation in Sound Source Localization](https://doi.org/10.1109/tim.2025.3547117) · IEEE Transactions on Instrumentation and Measurement | 음원 위치 추정(소리가 나는 곳의 방향이나 위치를 알아내는 기술)에서 소리가 오는 방향(DOA)을 정확히 구하는 일은 결과로부터 원인을 거꾸로 찾는 역문제다. 음향 인텐시티(소리 에너지가 흐르는 세기와 방향) 측정은 헬름홀츠 수(kd, 소리의 파수 k와 마이크 간격 d를 곱한 값)가 낮을 때 방향을 정확히 추정해 마이크 배열을 작게 만들 수 있지만, kd가 높으면 소리 방향에 따라 측정 지향성(방향에 따라 감도가 달라지는 성질)이 고르지 않아 인텐시티가 치우치고 추정이 부정확해진다. 이 치우침은 마이크 수가 적은 장치에서 더 두드러진다. 이 논문은 정규화 흐름(되돌릴 수 있는 변환을 거듭해 단순한 확률 분포를 복잡한 분포로 바꾸는 방법)에 기반한 가역 신경망에 헬름홀츠 수를 참조하는 전역 조건 포트와 치우친 방향 추정을 보정하는 관측 조건 포트를 단 Dual-port CINN을 제안했다. 마이크 4개로 된 사면체 배열로 kd 0–π 범위의 시뮬레이션에서 학습·검증했고, 무향실(소리가 벽에서 반사되지 않도록 만든 방)에서 마이크 간격 0.14 m 배열과 0.01 m 배열 등으로 실험했다.[^p7] | 1저자 I. Jeong(Iljoo Jeong), 교신저자 I.-J. Jung(In-Jee Jung)·이승철 (6명) |
| 8 | 2024 | [EchoScan: Scanning Complex Room Geometries via Acoustic Echoes](https://doi.org/10.1109/taslp.2024.3485516) · IEEE/ACM Transactions on Audio, Speech, and Language Processing | 실내 공간의 형상을 정확히 추정하는 일은 디지털 트윈(실제 대상을 컴퓨터 안에 재현한 모형)을 만드는 데 중요하며, 낯선 환경의 길 안내와 어두운 곳에서의 대피 계획 같은 산업 응용이 있다. 기존 소리 기반 방법은 벽 위치나 방 크기 같은 매개변수를 추정해 다룰 수 있는 방 형태가 제한됐다. 이 논문의 EchoScan은 음향 반향을 쓰는 심층 신경망으로, 방의 평면도 지도와 높이 지도를 직접 추론해 곡면 벽이 있는 복잡한 방도 다룬다. 평면도와 높이 지도를 예측하는 분할 과제(그림의 각 화소가 어느 영역에 속하는지 가르는 과제)로 저차와 고차 반사(소리가 벽에 한 번 또는 여러 번 부딪혀 돌아온 반사)를 모두 쓰며, 고차 반사 덕분에 오디오 기기 위치에서 보이지 않는 벽이 있어도 복잡한 방 모양을 추론한다. Manhattan·Atlanta 배치를 포함한 복잡한 환경에서 합성한 실내 충격 응답(RIR, 방 안에서 낸 짧은 소리가 마이크에 닿는 응답)으로, 시판 기기와 호환되는 오디오 장치 배치를 써서 학습·평가했다.[^p8] | 공동 1저자 I. Yeon(Inmo Yeon)·I. Jeong(Iljoo Jeong), 교신저자 이승철·J.-W. Choi(Jung-woo Choi) (4명) |

## 교수와 전문 분야

이승철 교수는 KAIST 기계공학과 부교수다.[^prof][^meprof] 교수 소개 페이지의 Affiliation 칸에 따르면 2023년부터 KAIST 기계공학과 Associate Professor이고, 2026년부터 KAIST College of AI의 Department of AX 겸임교수(Adjunct Professor)를 맡고 있다.[^prof] 그 전에는 2010–2013년 University of Michigan 기계공학과 박사후 연구원(Postdoctoral Research Fellow), 2013–2017년 UNIST 기계공학과 조교수, 2018–2020년 POSTECH 기계공학과 조교수, 2021–2023년 같은 학과 부교수를 지냈고, POSTECH의 Graduate School of Artificial Intelligence, Department of Industrial and Management Engineering, School of Interdisciplinary Bioscience and Bioengineering 겸임교수(Adjunct Professor)와 연세대학교 Institute of Convergence Research and Education in Advanced Technology의 Affiliate Professor를 겸했다.[^prof] 연구실 소식은 2023년 8월 28일 "iAI lab moves to KAIST."라고 알린다.[^news] 학력은 서울대학교 기계항공공학 학사(2001년), University of Michigan at Ann Arbor 기계공학 석사(2008년)와 박사(2010년)다.[^prof][^meprof]

교수 소개 페이지의 Honors and Awards 칸은 2025–2026년에 "한국연구재단, 2026년 산학협력 유공 교육부 장관표창 수상", "대한기계학회 2025 김윤영AI교육혁신상 수상", "2025 한국소음진동공학회 학술상 수상"을 적는다.[^prof] 2023년 칸의 IJPEM Award는 연구실 소식에 따르면 IJPEM에 실린 리뷰 논문 "Recent Advances of Artificial Intelligence in Manufacturing Industrial Sectors: A Review"가 받은 2023년 상이고, 같은 해 칸에는 "대한기계학회 CAE 및 응용역학 젊은연구자상 수상"도 있다.[^prof][^news] 그 전 UNIST·POSTECH 재직 시기 칸에는 Best Teaching Award(UNIST 2016년, POSTECH 기계공학과 2019·2022년), "2021년 대한민국 올해의 10대 기계기술 수상"(Award for Top 10 Mechanical Technologies of 2021), 한국소음진동공학회 "KTM테크놀로지(주) 학술상"(2021년), 한국PHM학회 유망과학자상(2020년), 대한기계학회 신뢰성젊은연구자상(2017년) 등이 있다.[^prof] 연구실 소식은 2021년 10대 기계기술 수상 대상을 딥러닝 기반 음원 위치 추정 기술로 적는다.[^news]

Academic Service 칸은 International Journal of Precision Engineering and Manufacturing - Smart Technology(IJPEM-ST) Associate Editor(2023년–현재), International Journal of Precision Engineering and Manufacturing(IJPEM) Editorial Board(2021년–현재), 대한금속재료학회 인공지능재료과학 분과 위원장(2024–2025년), 한국생산제조학회 제조AI 부문 위원장(2026년), 대한기계학회 신뢰성 부문 부회장(2022년–현재), 소재 국가기술전략센터 기술자문위원회 위원(인공지능기반 소재 분과, 2024년–현재) 등을 적는다.[^prof]

논문으로 보면 KAIST에서의 전문 분야는 공학 문제에 인공지능을 적용하는 산업 인공지능이다. 물리 정보 신경망과 연산자 학습으로 유동 문제 풀기(대표 논문 1, 2),[^p1][^p2] 능동 학습과 회귀 모델을 쓴 금속·2차원 소재·3D 프린팅 수지 탐색(대표 논문 3–5),[^p3][^p4][^p5] 설비 진단용 진동 신호 생성(대표 논문 6),[^p6] 음원 방향 추정과 음향 기반 실내 형상 추정(대표 논문 7, 8)에 걸친다.[^p7][^p8]

## 응용 분야

첫 화면은 연구실이 LG Electronics(Production Engineering Research Institute, Virtual Design), LG Energy Solution(Manufacturing Intelligence Center, Simulation AI Team), Samsung Electronics Foundry Business(Product & Test Engineering)의 target lab으로 선정됐다고 적는다.[^home] 과제 목록에는 포스코홀딩스(CFD 결과 내삽, 미세조직 예측), 풍산-KAIST 미래기술연구센터(탄 공력 성능 예측), 과학기술정보통신부(우주항공용 초내열 비철 금속소재, 설계-제조 통합 연구단), 교육부와 한국연구재단(첨단제조지능혁신센터)이 지원하는 KAIST 시기 과제가 있다.[^projects] 연구실 소식은 2025년 11월 포스코그룹 테크포럼에서 포스코홀딩스와의 산학협력 과제가 도약상을 받았다고 적는다.[^news]

의료 쪽으로는 첫 화면이 의료 AI를, TOPICS 페이지가 AI + Healthcare를 연구 영역으로 든다.[^home][^topics] 과제 목록에는 co-PI로 참여하는 3D 바이오리액터 자동화 배양시스템 개발 과제(2023.04.01–2026.12.31)가 진행 중으로 적혀 있다.[^projects]

대표 논문 8은 실내 공간 형상 추정이 디지털 트윈 구축, 낯선 환경의 길 안내, 어두운 곳의 대피 계획에 쓰일 수 있다고 적고, 대표 논문 5는 소프트 로봇용 기능 소재 설계를 응용으로 든다.[^p8][^p5] 졸업생 진로에는 SK Hynix, LG Energy Solution, LG Electronics, Samsung Electronics, POSCO 같은 기업과 Korea Institute of Materials Science(KIMS), Korea Electronics Technology Institute(KETI) 같은 연구기관이 있다.[^researchers]

## 구성원

연구실 누리집 RESEARCHERS 페이지의 POSTDOCTORAL RESEARCHERS 2명, Ph.D. Students 1명, MS Students 13명, Undergraduate Interns 5명, 모두 21줄이다.[^researchers] 과정은 페이지 표기이며, 박사후연구원의 InnoCORE Fellow와 박사과정 학생의 지원사업 표기는 이름 뒤에 적힌 것을 과정 칸에 함께 적었다. 시작 칸은 각 카드의 시작 시기이고, MS Students 13명 가운데 5명은 시작 시기가 2027.03 ~로 적혀 있다. 이 가운데 이상백(Sangbaek Lee)·전병규(Byeongkyu Jeon)와 같은 한글 이름이 Undergraduate Interns 칸에도 있다. 학부 인턴 칸은 한글 이름만 적는다. 연구 주제는 카드의 AIX 줄에 적힌 경우만 옮겼고, 이메일은 카드에 적힌 학교 주소다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Hong-Kyun Noh (노홍균) | 박사후연구원 (InnoCORE Fellow) | 2025.09 ~ |  | hknoh@kaist.ac.kr | 6 |
| Junbeom Son (손준범) | 박사후연구원 (InnoCORE Fellow) | 2026.09 ~ |  | junson@kaist.ac.kr |  |
| Jaejung Park (박재정) | 박사과정 (박사과정생연구장려금지원사업, IPESK 차세대공학연구자) | 2024.09 ~ | Materials | parkfrank01@kaist.ac.kr | 3, 4, 6 |
| Yenee Oh (오예니) | 석사과정 | 2025.03 ~ |  | yeneeoh@kaist.ac.kr |  |
| Minhyung Lee (이민형) | 석사과정 | 2025.09 ~ |  | mhlee@kaist.ac.kr | 6 |
| Min-Woo Park (박민우) | 석사과정 | 2026.03 ~ |  | pak1309@kaist.ac.kr |  |
| YongGyu Seo (서용규) | 석사과정 | 2026.03 ~ |  | yonggyuseo@kaist.ac.kr |  |
| Ahmed Mohamed | 석사과정 | 2026.09 ~ |  | alhedai@kaist.ac.kr |  |
| Seonguk Choi (최성욱) | 석사과정 | 2026.09 ~ |  | s_uchoi@kaist.ac.kr |  |
| Juhyun Choi (최주현) | 석사과정 | 2026.09 ~ |  | juhyunchoi@kaist.ac.kr |  |
| Donghyun Lim (임동현) | 석사과정 | 2026.09 ~ |  | eastwise.lim@kaist.ac.kr |  |
| Byeongkyu Jeon (전병규) | 석사과정 | 2027.03 ~ |  |  |  |
| Suuk Lee (이수욱) | 석사과정 | 2027.03 ~ |  |  |  |
| Jonghoon Kim (김종훈) | 석사과정 | 2027.03 ~ |  |  |  |
| Sangbaek Lee (이상백) | 석사과정 | 2027.03 ~ |  |  |  |
| Rian Ryu (유리안) | 석사과정 | 2027.03 ~ |  |  |  |
| 오상근 | 학부 인턴 |  |  |  |  |
| 송민준 | 학부 인턴 |  |  |  |  |
| 김예임 | 학부 인턴 |  |  |  |  |
| 이상백 | 학부 인턴 |  |  |  |  |
| 전병규 | 학부 인턴 |  |  |  |  |

## 졸업생과 이전 구성원

RESEARCHERS 페이지 ALUMNI 칸의 34명 전부다. 박사후연구원(Postdoc) 2명, 박사(Ph.D.) 9명, 석사(MS) 22명, 방문 학생(Visitors) 1명이다. 학위·과정 칸은 칸 이름과 줄에 적힌 연도(박사후연구원과 방문 학생은 기간)이고, 학위논문 제목과 진로는 페이지 표기 그대로다. 연구실은 2023년 8월 KAIST로 옮겼으므로, 그 전에 졸업하거나 떠난 사람은 교수가 UNIST(2013–2017년)·POSTECH(2018–2023년)에 있던 시기의 구성원이다.[^researchers][^prof][^news]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Bayu Adhi Tama | Postdoc (2018.09 ~ 2020.08) | Research Assistant Professor at the University of Maryland, Baltimore County |  |
| Bumsoo Park | Postdoc (2023.09 ~ 2026.02) | Assistant Professor at Seoul National University of Science and Technology (SeoulTech) |  |
| Jongmok Lee (이종목) | Ph.D. (2026.06) | LG Energy Solution | Physics-Informed Deep Learning for Boundary-Dominated Phenomena in Engineering Systems with Arbitrary Geometries: From Modeling to Optimization |
| Keonhyeok Park (박건혁) | Ph.D. (2026.02) | LG Electronics → Samsung Electronics | Physics-Informed Deep Learning for Engineering Applications: From Ultrasonic Imaging to Inverse Design |
| Iljeok Kim (김일적) | Ph.D. (2024.08) | SK Hynix | Leveraging Physics Knowledge in Deep Learning for Manufacturing Systems |
| Hyunsuk Huh (허현석) | Ph.D. (2024.08) | SK Hynix | Manufacturing Process Monitoring Methods using Deep Learning: from Prediction to Diagnosis |
| Iljoo Jeong (정일주) | Ph.D. (2024.08) | Korea Electronics Technology Institute (KETI) | Knowledge-guided Deep Learning Approaches for Acoustic Environment Measurement |
| Taewan Kim (김태완) | Ph.D. (2024.02) | Korea Electrotechnology Research Institute (KERI) and National AI for Science Research Center (NAIS) | Industrial Artificial Intelligence from Data Analytics to Simulation |
| Sooyoung Lee (이수영) | Ph.D. (2023.05) | SK Hynix → Assistant Professor at Chung-Ang University | Towards Deep Learning-enabled Engineering for Expedited Understanding and Mitigation of Physical Phenomena |
| Juwon Na (나주원) | Ph.D. (2022.12) | Korea Institute of Materials Science (KIMS) | Deep Learning for Microscopy Image Analysis in Materials Science: Restoration and Recognition |
| Sung Wook Kim (김승욱) | Ph.D. (2022.06) | Samsung Electronics → Korea Institute of Industrial Technology (KITECH) | Battery Health Management Through Physics-Informed Neural Networks: Thermal Runaway Modeling and Capacity Estimation |
| Hyeokjin Kweon (권혁진) | MS (2026.02) | SK Hynix | Uncertainty-Aware Deep Learning Framework for Vision-Based Three-Dimensional Flow Field Reconstruction |
| Chaeyun Won (원채윤) | MS (2025.06) | LG Electronics | Neural Operator Learning for Approximating Spatio-Temporal Systems: Integrating DeepONet with Dimension Reduction |
| Jaejung Park (박재정) | MS (2024.01) | Ph.D. student at iAI lab, KAIST | Machine Learning-based Surrogate Modeling to Expedite the Exploration of the Extensive Chemical Space of MXenes |
| Jaejun Lee (이재준) | MS (2024.01) | Ph.D. student at at the University of Illinois Urbana-Champaign, USA | Surrogate Models for Predicting Elastic Moduli of Metal-Organic Frameworks via Multiscale Features |
| Hyeongsik Park (박형식) | MS (2024.01) | LG Energy Solution | Deep Learning-based Vibration Signal Generation with Frequency-Amplitude Variability |
| Jihun Lee (이지훈) | MS (2023.06) | Samsung Electronics | Generative Neural Networks in Industrial Applications: Acoustic Metaporous Materials Design and Virtual Vibration Signal Synthesis |
| Seungmin Shin (신승민) | MS (2023.06) | LG Electronics | Training Strategy for Physics-informed Neural Networks with a Focus on Fluid Dynamics |
| Heekyu Kim (김희규) | MS (2023.06) | Ph.D. student at the Multiscale Mechanics & Modeling lab, KAIST | Active Learning Platform for Accelerating the Search of High-Voltage Cathode Materials in an Extensive Chemical Space |
| Yongtae Kim (김용태) | MS (2022.12) | POSCO | End Point Oxygen and Temperature Prediction based on Feature Clustering in Basic Oxygen Furnace Steelmaking |
| Dogyeom Park (박도겸) | MS (2022.12) | Co-founder of Amber Road | Lightweight Convolutional Neural Network for Real-time Fault Diagnosis on Edge Device |
| Jeongsan Kim (김정산) | MS (2022.07) | Samsung Electronics | Attention-based Explainable Feature Extraction Model for Anomaly Detection in Gearbox |
| Eonho Im (임언호) | MS (2022.02) | POSCO and co-founder of Amber Road | Robust Machine Learning Method for Surface Crack Prediction of Continuous Casting Steel |
| Gyuwon Kim (김규원) | MS (2022.02) | Mando → Samsung Electronics → Ph.D. students at Georgia Institute of Technology, USA | Deep Learning Methods to Enhance the Temporal Resolution in Functional Biomedical Imaging |
| Changyun Choi (최창윤) | MS (2021.07) | Minds and Company | Directed Graph Based Refinement of 3D Human Motion Data using Spatial-Temporal Information |
| Jonghwan Lee (이종환) | MS (2021.07) | Ph.D. student at the University of Bristol, UK | Deep Learning-based Analysis on Physical Factors of Bar Warping in Rolling Process |
| Yunseob Hwang (황윤섭) | MS (2021.02) | Deep Bio | Convolutional Neural Network based Small Bowel Lesion Detection in Capsule Endoscopy |
| Namjeong Lee (이남정) | MS (2021.02) | SK On → NVIDIA | Fault Diagnostics for Rotating Machinery using Deep Learning: Ensemble Model of Frequency Spectrum, Spectrogram, and Orbit |
| Kangsan Lee (이강산) | MS (2021.02) | Minds and Company | Deep Learning-based Object Tracking in Soccer Data |
| Heechang Kim (김희창) | MS (2017.12) | Freelancer | Mechanical Properties Assessment and Reliability Verification for FDM 3D Printed Products |
| Suhyun Kim (김수현) | MS (2017.12) | Hanwha Techwin | Deep Learning Applications in Manufacturing: Human Motion Recognition and Sound-based Fault Detection |
| Sunhee Woo (우선희) | MS (2016.12) | LG Electronics | Machine Learning Toolbox and PCA Visualization for Data-Driven PHM |
| Hyungcheol Min (민형철) | MS (2016.02) | Hyundai Heavy Industries | Statistical Approaches for Fault Diagnostics and Root Cause Analysis with Industrial Applications: MLCC and Rotating Machinery |
| Zhishan Wang | Visitor, Exchange Student (MS Program), RWTH Aachen University (2026.03 ~2026.06) |  |  |

## 최근 논문 목록 (2021–2026)

누리집 Journal 페이지의 2021–2026년 연도 구역 83편과 Conference 페이지 International Conferences·Domestic Conferences 부분의 2021–2025년 연도 구역 134편(국제 학회 37편, 국내 학회 97편), 모두 217편이다. Conference 페이지에는 2026년 구역이 없다. 학술지 논문은 2026년 9편, 2025년 12편, 2024년 9편, 2023년 19편, 2022년 19편, 2021년 15편이고, 국제 학회 논문은 2025년 9편, 2024년 5편, 2023년 8편, 2022년 6편, 2021년 9편, 국내 학회 논문은 2025년 14편, 2024년 11편, 2023년 22편, 2022년 23편, 2021년 27편이다. 아래 목록은 연도마다 학술지, 국제 학회, 국내 학회 순이며, 연도는 누리집의 연도 구역이고 각 줄은 누리집 표기 그대로다. 저자 이름 뒤 *와 +, 줄 끝의 (+ equally contributed)는 누리집 표기다. 연구실은 2023년 8월 KAIST로 옮겼으므로 2021–2022년 구역 전부와 2023년 구역 일부는 교수가 POSTECH에 있던 시기의 논문이고, 2021년 구역에는 2021년 10월 전에 나온 논문도 들어 있다. 이승철 교수가 공저자로만 참여한 논문도 누리집 목록대로 실었다.[^journal][^conference][^news]

**2026**

- Jihoon Kim+, Yenee Oh+, Jaejung Park, Bumsoo Park, Seungchul Lee\*, and Bong Jae Lee\*, 2026, "Accurate Thermal Analysis of a Li-ion Battery under Various Operating Conditions via a Physics-informed Deep Operator Network," International Communications in Heat and Mass Transfer, 112465, Vol. 180, Part 1, https://doi.org/10.1016/j.icheatmasstransfer.2026.112465 (+ equally contributed).
- Heechang Kim, Qianying Cao, Hyomin Shin, Seungchul Lee, George Em Karniadakis, and Minseok Choi\*, 2026, "Physics-Informed Laplace Neural Operator for Solving Partial Differential Equations," Journal of Computational Physics, Vol. 566, https://doi.org/10.1016/j.jcp.2026.115291.
- Hyeokjin Kweon, Mi Hyun Lim, David W Jang, Keonhyeok Park, Seungchul Lee\*, and Do Hyun Kim\*, 2026, "Deep Learning–Based Prediction of Epithelial Cytokine Responses for the Selection of Functionally Consistent Airway Organoids," Biomimetics, 11(8), 547, https://doi.org/10.3390/biomimetics11080547.
- Chaeyun Won+, Jongmok Lee+, Anna Lee, Bumsoo Park, and Seungchul Lee\*, 2026, "Spectral Modal Operator Learning Framework with Decoupled Spatial and Temporal Representations for Unsteady Flows," Physics of Fluids, https://doi.org/10.1063/5.0327449 (+ equally contributed).
- Younghan Song+, Bumsoo Park+, Seungbae Jeon, Hyeokjin Kweon, Seungchul Lee\*, and Jongbeom Na\*, 2026, "Machine Learning Guided Formulation Design of DLP Printable Elastomers Beyond Viscosity Stretchability Tradeoff," Nature Communications, https://doi.org/10.1038/s41467-026-73735-4 (+ equally contributed).
- Hyungsik Park+, Minhyung Lee+, Jaejung Park, Hong-Kyun Noh, and Seungchul Lee\*, 2026, "Deep Learning-based Vibration Signal Generation with Frequency-Amplitude Variability," International Journal of Precision Engineering and Manufacturing-Smart Technology, https://doi.org/10.57062/ijpem-st.2026.00052 (+ equally contributed).
- Jongmok Lee, Chaeyun Won, Anna Lee, Bumsoo Park, Sooyoung Lee\*, and Seungchul Lee\*, 2026, "A Geometry-adaptive Physics-informed Operator Framework Generalized for Arbitrary Geometries," Engineering Applications of Artificial Intelligence, Vol. 174, https://doi.org/10.1016/j.engappai.2026.114457.
- Bumsoo Park+, Julius Mauch+, Hyeokjin Kweon+, Jochen Kriegseis, Seungchul Lee\*, and Hyoungsoo Kim\*, 2026, "STAR-APTV: Deep Learning-Enabled 3D Flow Reconstruction in Evaporating Multicomponent Droplets," Measurement, Vol. 266, https://doi.org/10.1016/j.measurement.2026.120368 (+ equally contributed).
- Donghyun Ra, Jaeryun Lee, Minwoo Lee, Seongmin Kwak, Seungjoon Bang, Seungchul Lee\*, and Sooyoung Lee\*, 2026, "Physics-informed Machine Learning across Manufacturing Processes: Recent Advances, Challenges, and Directions," Journal of Manufacturing Systems, Vol. 85, pp. 72-95, https://doi.org/10.1016/j.jmsy.2026.01.002.

**2025**

- Woosang Shin+, Iljeok Kim+, Jonghyeon Lee, Seungchul Lee, and Jong Pil Yun\*, 2025, "High-Resolution Neural Attenuation Field for Industrial Computed Tomography," Expert Systems with Applications, https://doi.org/10.1016/j.eswa.2025.130535 (+ equally contributed).
- Jongyeon Yoon, Jeongsan Kim, Jongwoo Lim, Ivo Dobrev, Christof Röösli, Seungchul Lee\*, Il Joon Moon\*, and Namkeun Kim\*, 2025, "Automated High-Fidelity 3D Reconstruction of Middle-Ear Ossicles from Low-Resolution Clinical CT using a Deep Learning Pipeline," Hearing Research, https://doi.org/10.1016/j.heares.2025.109492.
- Iljoo Jeong+, Hyunsuk Huh+, Bumsoo Park, Anna Lee, In-Jee Jung\*, and Seungchul Lee\*, 2025, "MicGraphNet: Microphone Graph Network for Cross Correlation-based Time Delay Estimation for Accurate Sound Source Localization," Measurement, https://doi.org/10.1016/j.measurement.2025.119552 (+ equally contributed).
- Sung Ho Hong\*, Sebin Lee, and Seungchul Lee\*, 2025, "Novel Evaluation Method for Wear Volume Based on Wear Scars Using Segmentation and Principal Component Analysis," Tribology Transactions, https://doi.org/10.1080/10402004.2025.2569634.
- Keonhyeok Park, Jun Hyeong Park, Bumsoo Park, Hyung Jin Lee, Sooyoung Lee, Iljoo Jeong, Anna Lee, Choon-Su Park\*, and Seungchul Lee\*, 2025, "Deep Learning Framework for Image Enhancement of Phased Array Ultrasonic Imaging," Results in Engineering, https://doi.org/10.1016/j.rineng.2025.106929.
- Hyunsuk Huh+, Iljoo Jeong+, Anna Lee, Seungchul Lee\*, and Young-Sik Shin\*, 2025, "Leveraging Falling Acceleration and Body Part Clustering for Physics-based Human Fall Detection with Millimeter Wave Radar," Engineering Applications of Artificial Intelligence, Vol. 159, Part A, https://doi.org/10.1016/j.engappai.2025.111500 (+ equally contributed).
- Hong-Kyun Noh, Chaeyun Won, Jongmok Lee, Sanghun Choi\*, Seungchul Lee\*, and Jae Hyuk Lim\*, 2025, "Physics-informed Machine Learning: Technological Trends in Turbulence Flow, Topology Optimization, and Convergence Enhancement with Temporal Causality Consideration," JMST Advances, http:/doi.org/10.1007/s42791-025-00101-8 (invited).
- Soo Young Lee, Jihun Lee, Joongseok Lee\*, and Seungchul Lee\*, 2025, "Deep Learning-accelerated Multiple Design Generation for Sound-absorbing Metaporous Materials," Engineering Applications of Artificial Intelligence, Vol. 156, Part C, 111172, https://doi.org/10.1016/j.engappai.2025.111172.
- Jongmok Lee+, Seungmin Shin+, Taewan Kim, Bumsoo Park, Ho Choi, Anna Lee, Minseok Choi\* and Seungchul Lee\*, 2025, "Physics Informed Neural Networks for Fluid Flow Analysis with Repetitive Parameter Initialization," Scientific Reports, 15, 16740, http:/doi.org/10.1038/s41598-025-99354-5 (+ equally contributed).
- Jongmok Lee, Seungmin Shin, Ho Choi, Anna Lee, Bumsoo Park\*, and Seungchul Lee\*, 2025, "Extended Multiphysics-informed Neural Network for Conjugate Heat Transfer Problems," International Journal of Heat and Mass Transfer, Vol. 246, 127098, https://doi.org/10.1016/j.ijheatmasstransfer.2025.127098.
- Iljoo Jeong, Bumsoo Park, Keonhyuk Park, Anna Lee, In-Jee Jung\*, and Seungchul Lee\*, 2025, "Dual-port Conditional Invertible Neural Network for Sound Intensity Compensation in Sound Source Localization," IEEE Transactions on Instrumentation and Measurement, Vol. 74, pp. 1-12, https://doi.org/10.1109/TIM.2025.3547117.
- Jeong Ah Lee+, Jaejung Park+, Man Jae Sagong, Soung Yeoul Ahn, Jung-Wook Cho, Seungchul Lee\*, and Hyoung Seop Kim\*, 2025, "Active Learning Framework to Optimize Process Parameters for Additive-manufactured Ti-6Al-4V with High Strength and Ductility," Nature Communications, 16, Article number: 931 (2025), https://doi.org/10.1038/s41467-025-56267-1. (+ equally contributed)
- Hong-Kyun Noh, Seungchul Lee, Jeong-Hoon Park, and Jae Hyuk Lim, "Real-time Response Estimation of Time-dependent PDEs via Causality-aware Physics-informed Machine Learning: Robustness to Unmodeled Effects," the 9th Asian Congress on Computational Mechanics & the 7th Australasian Conference on Computational Mechanics (APCOM-ACCM 2025), Brisbane, Australia.
- Jaejung Park, Hyeonho Park, Bumsoo Park, Kyoungdoc Kim, and Seungchul Lee, "Physics-Informed Neural Network for Predicting Grain Structure Evolution Governed by the Allen-Cahn Equation," the 9th Asian Congress on Computational Mechanics & the 7th Australasian Conference on Computational Mechanics (APCOM-ACCM 2025), Brisbane, Australia.
- Bumsoo Park, Hyeokjin Kweon, Jaejung Park, and Seungchul Lee, "Diffusion-based Generative Topology Design under Uncertain Boundary Conditions," the 9th Asian Congress on Computational Mechanics & the 7th Australasian Conference on Computational Mechanics (APCOM-ACCM 2025), Brisbane, Australia.
- Jihoon Kim, Bumsoo Park, Jaejung Park, Miran Ryu, Seungchul Lee, Bong Jae Lee, 2025, "Temperature Field Prediction of a Li-ion Battery using Deep Operator Network under Various Operating Conditions," the 11th JSME-KSME Thermal and Fluids Engineering Conference (J-K TFEC11), Okinawa, Japan.
- Bumsoo Park, Keonhyeok Park, and Seungchul Lee, 2025, "Physics-guided Generative Framework for Inverse Design of Acoustic Scattering Objects," the 31st International Congress on Sound and Vibration (ICSV31), Incheon, Korea.
- Jongmok Lee, and Seungchul Lee, 2025, "Geometry-adaptive Physics-informed DeepONet for Acoustic Scatterer," the 31st International Congress on Sound and Vibration (ICSV31), Incheon, Korea.
- Hyeokjin Kweon, Jaejung Park, Bumsoo Park, Sung-Ho Hong,and Seungchul Lee, 2025, "Physics-Informed Multi-Modal Framework for Multi-Bearing Fault Diagnosis," the 31st International Congress on Sound and Vibration (ICSV31), Incheon, Korea.
- Seohyun Lee, Jongwoo Lim, Soomin Lee, Jeonsan Kim, Seungchul Lee, and Namkeun Kim, 2025, "Deep Learning-Based Approach for Automatic Segmentation and Reconstruction of Middle Ear Ossicle Bone Computed Tomography Images," the International Symposium on Middle Ear Mechanics in Research and Otology (MEMRO 2025) at Leuven, Belgium.
- Inmo Yeon, Iljoo Jeong, Seungchul Lee and Jung-woo Choi, 2025, "EchoScan: Scanning Complex Room Geometries via Acoustic Echoes," 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2025) at Hyderabad, India.
- 노홍균, 이승철, 임재혁, 2025, "고차 미분과 센서 배치 최적화를 적용한 물리지식기반 신경망의 보·판 진동 거동 실시간 추론," 한국전산구조공학회 추계학술대회, 대전
- 박재정, 정진영, 박범수, 민경민, 이승철, 2025, "Enhancing Energy Density and Structural Stability of Nickel Manganese Oxide Cathode through Compositionally Complex Multi-Cation Doping Strategy," 대한금속·재료학회 추계학술대회, 광주
- 권혁진, 박재정, 박범수, 홍성호, 이승철, 2025, "Bearing Fault Diagnosis System using a Large Language Model: Improving Reliability through Multi-Agent Framework," 한국트라이볼로지 추계학술대회, 제주
- 이승철, 2025, "Developing an e-Book for "AI for Mechanical Engineering" Course Using ChatGPT: A Case Study," 대한기계학회, 교육 부문 춘계학술대회, 서울
- 이승철, 이종목, 원채윤, 2025, "가상 제품 설계 및 개발을 위한 물리 인공지능 기반 전산해석 가속화," 한국소음진동공학회 춘계학술대회, 제주
- 이종목, 박건혁, 원채윤, 이승철, 2025, "형상 변화를 고려한 음향 산란체의 파동 전파 및 산란 특성 분석," 한국소음진동공학회 춘계학술대회, 제주
- 권혁진, 박재정, 박범수, 홍성호, 이승철, 2025, "단일 결함 학습을 통한 베어링 복합 결함 진단 방법," 한국트라이볼로지학회 춘계학술대회, 영주
- Jaejung Park, Jinyoung Jeong, Bumsoo Park, Kyoungmin Min, and Seungchul Lee, 2025, "Identification of High-entropy Nickel Manganese Cathode with High Energy Density and Structural Stability through Machine-learning Interatomic Potential," 대한금속재료학회 춘계학술대회, 제주
- 박범수, 권혁진, 정해동, 이승철, 2025, "경계 조건의 불확실성을 포함한 3차원 위상 최적화를 위한 확산모델," 대한기계학회 CAE 및 응용역학 부문 춘계학술대회, 제주
- 이종목, 박건혁, 박재정, 오예니, 이승철, 2025, "형상 변화를 반영한 음향 산란체의 파동 전파 및 산란 특성 해석," 대한기계학회 CAE 및 응용역학 부문 춘계학술대회, 제주
- 원채윤, 이종목, 이승철, 2025, "SPOD-DeepONet: 주파수 영역 직교 분해를 활용한 실시간 시공간 유체 유동 예측 및 해석," 대한기계학회 CAE 및 응용역학 부문 춘계학술대회, 제주
- 권혁진, 박범수, Julius Mauch, Jochen Kriegseis, 이승철, 김형수, 2025, "실험 기반 미세 유체 유동장 3차원 시각화를 위한 딥러닝 기법," 대한기계학회 CAE 및 응용역학 부문 춘계학술대회, 제주
- 박범수, 박재정, 이승철, 2025, "스마트 자율 제조에서의 인공지능 역할," 대한기계학회 신뢰성 부문 춘계학술대회, 경주.
- 박범수, 권혁진, 정해동, 이승철, 2025, "확산 모델을 활용한 하중 불확실성을 고려한 3D 위상 최적화," 대한기계학회 신뢰성 부문 춘계학술대회, 경주.

**2024**

- Inmo Yeon+, Iljoo Jeong+, Seungchul Lee\* and Jung-woo Choi\*, 2024, "EchoScan: Scanning Complex Room Geometries via Acoustic Echoes" Vol. 32, pp. 4768-4782, EEE Transactions on Audio, Speech and Language Processing, https://doi.org/10.1109/TASLP.2024.3485516. (+ equally contributed)
- Minseon Kim, Jaejung Park, Heekyu Kim, Jaejun Lee, Inhyo Lee, Seungchul Lee\*, and Kyoungmin Min\*, 2024, "Next-Generation Cathodes for Calcium-Ion Batteries: Leveraging NASICON Structures for Enhanced Stability and Energy Density," Energy Storage Materials, Vol. 73, November 2024, 103827, https://doi.org/10.1016/j.ensm.2024.103827.
- Jaejung Park, Jongmok Lee, Jaejun Lee, Kyoungmin Min, Haesun Park\*, and Seungchul Lee\*, 2024, "Active Learning Framework for Expediting the Search of Thermodynamically Stable MXenes in the Extensive Chemical Space," ACS Nano, https://doi.org/10.1021/acsnano.4c08621.
- Inhyo Lee+, Jaejun Lee+, Minseon Kim, Jaejung Park, Heekyu Kim, Seungchul Lee\*, and Kyoungmin Min\*, 2024, "Uncovering the Relationship between Metal Elements and Mechanical stability in Metal-Organic Framework," ACS Applied Materials & Interfaces, 16, 39, 52162–52178, https://doi.org/10.1021/acsami.4c07775. (+ equally contributed)
- Jaejung Park, Minseon Kim, Heekyu Kim, Jaejun Lee, Inhyo Lee, Haesun Park, Anna Lee, Kyoungmin Min\*, and Seungchul Lee\*, 2024, "Exploring the Large Chemical Space in Search of Thermodynamically Stable and Mechanically Robust MXenes via Machine Learning," Physical Chemistry Chemical Physics, https://doi.org/10.1039/D3CP06337B.
- Iljoo Jeong, Hyunsuk Huh, In-Jee Jung\*, and Seungchul Lee\*, 2024, "Deep Learning-based Approach to Improve the Accuracy of TDOA-based Sound Source Localization," Journal of the Acoustical Society of Korea, 43(2), pp. 178-183, https://doi.org/10.7776/ASK.2024.43.2.178. (in Korean)
- Jihoon Kim, Jihun Lee, Taewan Kim, Seungchul Lee\*, and Chan Il Park\*, 2024, "Analysis of Spur Gear Vibration Data on Backlash and Prediction of Backlash Based on Deep Learning," Transactions on the Korean Society for Noise and Vibration Engineering, pp. 78-83, https://doi.org/10.5050/KSNVE.2024.34.1.078. (in Korean)
- Taewan Kim and Seungchul Lee\*, 2024, "Deep Learning Integrated Bayesian Health Indicator for Cross-machinery Health Monitoring," Structural Health Monitoring, Vol. 23, Issue 6, https://doi.org/10.1177/14759217241227599.
- Iljoo Jeong, In-Jee Jung\*, and Seungchul Lee\*, 2024, "Application of Deep Learning for Accurate Source Localization using Sound Intensity Vector," Journal of the Acoustical Society of Korea, 43(1), pp. 72-77, https://doi.org/10.7776/ASK.2024.43.1.072. (in Korean)
- Bumsoo Park, Jaejung Park, and Seungchul Lee, 2024, "Diffusion Models for Designing High-entropy Alloys with Targeted Mechanical Properties," the 8th International Conference on Electronic Materials and Nanotechnology for Green Environment (ENGE 2024), Jeju, Korea.
- Jaejung Park, Jinyoung Jeong, Bumsoo Park, Kyoungmin Min, and Seungchul Lee, 2024, "Transfer Learning Approach for Identifying High-entropy Nickel Manganese Cathode with High Energy Density and Structural Stability," the 8th International Conference on Electronic Materials and Nanotechnology for Green Environment (ENGE 2024), Jeju, Korea.
- Bumsoo Park, and Seungchul Lee, 2024, "Self-supervised Fault Detection and Classification in Laser Powder Bed Fusion," the 26th International Congress of Theoretical and Applied Mechanics (ICTAM2024), Daegu, Korea.
- Keonhyeok Park, Soo Young Lee, Hyung Jin Lee, Choon-Su Park, and Seungchul Lee, 2024, "Physics integrated Neural Networks for Design of Acoustic Scatterer," the 26th International Congress of Theoretical and Applied Mechanics (ICTAM2024), Daegu, Korea.
- Jae Hyuk Lim, Myeong-Seok Go, Hong-Kyun Noh, and Seungchul Lee, 2024, "Identifying Cracked/Damaged Structures and their Locations using Physics-informed Machine Learning with Sparse Measurements," the 16th World Congress on Computational Mechanics (WCCM), Vancouver, British Columbia, Canada
- 이종목, 원채윤, 이승철, 2024, "Geometry-adaptive Physics-informed DeepONet," 한국전산구조공학회 학술심포지엄, 전주
- 원채윤, 이동현, 김동성, 이승철, 2024, "현미경 이미지 외벽 형상 분석을 통한 딥러닝 기반 자동 초점화 프레임워크 개발," 한국정밀공학회 추계학술대회, 경주
- 이종목, 박범수, 이승철, 2024, "형상 변화를 반영할 수 있는 물리 지식 기반 딥오넷," 대한기계학회 본부학술대회, 제주
- 원채윤, 이종목, 이승철, 2024, "가변 조건 내의 공통 기저를 반영한 딥 오퍼레이터 네트워크," 대한기계학회 본부학술대회, 제주
- 박건혁, 이수영, 정일주, 이형진, 박춘수, 이승철, 2024, "Deep Learning-based Image Translation for Ultrasonic Imaging Enhancement with Experimental Validation," 한국소음진동공학회 추계학술대회, 정선
- 연인모, 정일주, 이승철, 최정우, 2024, "실내 충격 응답을 활용한 복잡한 방 형상 추정 기법," 한국음향학회 춘계학술발표대회, 제주
- 정일주, 허현석, 정인지, 이승철, 2024, "딥러닝을 활용한 도달시간차 기반 음원 위치 추정 성능 개선 연구," 한국음향학회 춘계학술대회, 제주
- 허현석, 정일주, 이승철, 2024, "고장 상태 음향 신호 분리를 위한 세그멘테이션과 준지도 학습의 통합적 접근," 한국음향학회 춘계학술대회, 제주
- 이승철, 2024, "Deep Learning in Scientific Computing," 한국전산구조공학회 춘계학술대회, 제주
- 이종목, 박건혁, 이승철, 2024, "형상 변화를 반영할 수 있는 물리지식기반 딥오넷 모델," 한국전산구조공학회 춘계학술대회, 제주
- 박건혁, 이수영, 박형진, 박춘수, 이승철, 2024, "Physics-informed Deep Learning Approach for Inverse Design of Acoustic Scatterer," 한국전산구조공학회 춘계학술대회, 제주

**2023**

- Changyun Choi, Jongmok Lee, Hyun-Joon Chung, Jaejung Park, Bumsoo Park, Seokman Sohn, and Seungchul Lee\*, 2023, "Directed Graph-Based Refinement of Three-Dimensional Human Motion Data using Spatial-Temporal Information," International Journal of Precision Engineering and Manufacturing - Smart Technology (IJPEM-ST), 2(1):33-46, https://doi.org/10.57062/ijpem-st.2023.0094.
- Jaejun Lee+, Inhyo Lee+, Jaejung Park, Heekyu Kim, Minseon Kim, Kyungmin Min\*, and Seungchul Lee\*, 2023, "Optimal Surrogate Models for Predicting Elastic Moduli of MOFs via Multiscale Features," Chemistry of Materials, 35(24), 10457–10475, https://doi.org/10.1021/acs.chemmater.3c01885. (+ equally contributed)
- Iljeok Kim, Sung Wook Kim, Jeongsan Kim, Hyunsuk Huh, Iljoo Jeong, Taegyu Choi, Jeongchan Kim, and Seungchul Lee\*, 2023, "Single Domain Generalizable and Physically Interpretable Bearing Fault Diagnosis for Unseen Working Conditions," Expert Systems with Applications, https://doi.org/10.1016/j.eswa.2023.122455.
- Sebin Lee, Taewan Kim, Seungchul Lee\*, and Sung-Ho Hong\*, 2023, "Novel Method of Measuring Wear using Deep Learning," Tribology International, https://doi.org/10.1016/j.triboint.2023.109043.
- Juwon Na+, Jaejun Lee+, Seong-Hoon Kang, Se-Jong Kim, and Seungchul Lee\*, 2023, "Label-free Grain Segmentation for Optical Microscopy Images via Unsupervised Image-to-Image Translation," Materials Characterization, https://doi.org/10.1016/j.matchar.2023.113410. (+ equally contributed)
- Heekyu Kim, Jaejung Park, Minseon Kim, Jajun Lee, Inhyo Lee, Kyoungmin Min\*, and Seungchul Lee\*, 2023, "Active Learning Platform for Accelerating the Search for High-Voltage Cathode Materials in an Extensive Chemical Space," Journal of Physical Chemistry C, https://doi.org/10.1021/acs.jpcc.3c05812.
- Keonhyeok Park, Choon-Su Park, Jun Hyeong Park, Hyung Jin Lee, and Seungchul Lee\*, 2023, "Deep Learning-Based Conversion of Phased Array Ultrasonic Imaging using U-Net," Journal of the Korean Society for Nondestructive Testing, 43(4), pp. 285-291. (in Korean)
- Kyung Seok Choi, DoGyeom Park, Jin Su Kim, Dae Young Cheung, Bo-In Lee, Young-Seok Cho, Jin Il Kim, Seungchul Lee and Han Hee Lee\*, 2023, "Deep Learning in Negative Small Bowel Capsule Endoscopy Improves Small Bowel Lesion Detection and Diagnostic Yield," Digestive Endoscopy, https://doi.org/10.1111/den.14670.
- Heekyu Kim+, Hae-Yeon Park+, DoGyeom Park, Sun Im\*, and Seungchul Lee\*, 2023, "Non-invasive Way to Diagnose Dysphagia by Training Deep Learning Model with Spectrograms," Biomedical Signal Processing and Control, 86, Part B, https://doi.org/10.1016/j.bspc.2023.105259. (+ equally contributed)
- Mi Hyun Lim+, Seungmin Shin+, Keonhyeok Park, Jaejung Park, Sung Won Kim, Mohammed Abdullah Basurrah, Seungchul Lee\*, and Do Hyun Kim\*, 2023, "Deep Learning Model for Predicting Airway Organoid Differentiation," Tissue Engineering and Regenerative Medicine, https://doi.org/10.1007/s13770-023-00563-8. (+equally contributed)
- Juwon Na, Se-Jong Kim, Heekyu Kim, Seong-Hoon Kang, and Seungchul Lee\*, 2023, "A Unified Microstructure Segmentation Approach via Human-In-The-Loop Machine Learning," Acta Materialia, 255, https://doi.org/10.1016/j.actamat.2023.119086.
- Myeong-Seok Go, Jae Hyuk Lim\*, and Seungchul Lee, 2023, "Physics-informed Neural Network-based Surrogate Model for a Virtual Thermal Sensor with Real-time Simulation," International Journal of Heat and Mass Transfer, 214(2023), https://doi.org/10.1016/j.ijheatmasstransfer.2023.124392.
- Hong-Kyun Noh, In-Ho Choi, Jae Jae Hyuk Lim\*, Seungchul Lee, Taejoo Kim, and Deog-Kwan Kim, 2023, "Surrogate Modeling of the Fan Plot of a Rotor System considering Composite Blades using Convolutional Neural Networks with Image Composition," Journal of Computational Design and Engineering, 10(3), 1250-1266, https://doi.org/10.1093/jcde/qwad049.
- Iljoo Jeong, Soo Young Lee, Keonhyeok Park, Iljeok Kim, Hyunsuk Huh, and Seungchul Lee\*, 2023, "Wafer Map Failure Pattern Classification using Geometric Transformation-Invariant Convolutional Neural Network," Scientific Reports, https://doi.org/10.1038/s41598-023-34147-2.
- Iljeok Kim, Juwon Na, Jong Pil Yun\*, and Seungchul Lee\*, 2023, "Deep Feature Selection Framework for Quality Prediction in Injection Molding Process," IEEE Transactions on Industrial Informatics, https://doi.org/10.1109/TII.2023.3268421.
- Do-Won Kim, Myeong-Seok Go, Jae Hyuk Lim\*, and Seungchul Lee, 2023, "Data-driven Stress and Strain Curves of the Unidirectional Composites by Deep Neural Networks with Principal Component Analysis and Selective-data Augmentation," Composite Structures, 313(1), https://doi.org/10.1016/j.compstruct.2023.116902.
- Taewi Kim, Insic Hong, Yeonwook Roh, Dongjin Kim, Sung Wook Kim, Sunghoon Im, Changhwan Kim, Kiwon Jang, Seongyeon Kim, Minho Kim, Jieun Park, Dohyeon Gong, Kihyeon Ahn, Jingoo Lee, Gunhee Lee, Hak-Seung Lee, Jeehoon Kang, Ji Man Hong, Seungchul Lee, Sungchul Seo, Bon-Kwon Koo\*, Je-sung Koh\*, Seungyong Han\* and Daeshik Kang\*, 2023, "Spider-inspired Tunable Mechanosensor for Biomedical Applications," npj Flexible Electronics, 7(12), https://doi.org/10.1038/s41528-023-00247-2.
- Jeong Ah Lee, Jaejung Park, Yeon Taek Choi, Rae Eon Kim, Jaimyun Jung\*, Seungchul Lee\*, Min Hong Seo, and Hyoung Seop Kim\*, 2023, "Influence of Tensile Properties on Hole Expansion Ratio Investigated using a Generative Adversarial Imputation Network with Explainable Artificial Intelligence," Journal of Materials Science, https://doi.org/10.1007/s10853-023-08315-8.
- Sung Wook Kim, Eunji Kwak, Ki-Yong Oh\*, and Seungchul Lee\*, 2023, "Modeling and Prediction of Lithium-Ion Battery Thermal Runaway via a Multiphysics-Informed Neural Network," Journal of Energy Storage, 60, 106654, https://doi.org/10.1016/j.est.2023.106654.
- Jongmok Lee, Keonhyeok Park, Hyunjoon Chung and Seungchul Lee, 2023, "Deep Learning-based Human Action Recognition with Exo-Suit," 20th International Conference on Ubiquitous Robots (UR), Honolulu, USA.
- Hyunsuk Huh, Jeong-Jung Kim, Iljeok Kim, Iljoo Jeong, Doo-Yeol Koh, Chang-Hyun Kim, and Seungchul Lee, 2023, "Estimation of Simulated Physical Properties of an Object using Robot with Tactile Sensors and Attention Mechanism," 20th International Conference on Ubiquitous Robots (UR), Honolulu, USA.
- Taewan Kim, Jaejung Park, Sebin Lee, and Seungchul Lee, 2023, "Multi-Agent Deep Reinforcement Learning for Efficient Traffic Signal Control," 20th International Conference on Ubiquitous Robots (UR), Honolulu, USA.
- Sun Im, Heekyu Kim, DoGyeon Park, Hae-Yeon Park, and Seungchul Lee, 2023, "Non-invasive Way to Diagnose Dysphagia using Deep Learning Model with Voice Spectrograms," 31st DRS Annual Meeting, San Francisco, CA, USA.
- Iljeok Kim, Juwon Na, Jong Pil Yun and Seungchul Lee, 2023, "Feature Selection for Process Optimization using Interpretable AI: Case Study on Injection Molding," Proceeding of the 9th International Conference on Manufacturing, Machine Design and Tribology (ICMDT2023), Jeju, Korea.
- Seongwook Choi+, Jinge Yang+, Soo Young Lee+, Jiwoong Kim, Byullee Park, Seungchul Lee, and Chulhong Kim, 2023, "Improvement of Spatiotemporal Resolution based on Deep Learning in 3D Photoacoustic Tomography," The Conference on Optoacoustic Methods and Applications in Biophotonics, part of European Conferences on Biomedical Optics, Munich, Germany.
- Seongwook Choi, Jinge Yang, Soo Young Lee, Jiwoong Kim, Seungchul Lee, and Chulhong Kim, 2023, "3D Photoacoustic Computed Tomography Enhanced by 3D Progressive U-shaped Enhancement Network (3D-pU-net)," The conference on Photons Plus Ultrasound: Imaging and Sensing 2023, 123790I (2023) https://doi.org/10.1117/12.2648107, part of SPIE BiOS, San Francisco, USA.
- Jongbeom Kim, Gyuwon Kim, Lei Li, Pengfei Zhang, Jin Young Kim, Yeonggeun Kim, Hyung Ham Kim, Lihong V. Wang, Seungchul Lee, and Chulhong Kim, 2023, "Fast Superresolution Multiscale Photoacoustic Imaging via a Deep Learning Approach," The conference on Photons Plus Ultrasound: Imaging and Sensing 2023, part of SPIE BiOS, San Francisco, USA.
- 박재정, 이승철, 2023, "Applications of Artificial Intelligence in Regenerative Medicine," 한국조직공학재생의학회 교육/신진연구자 통합 심포지엄, 서울
- 김민선, 박재정, 김희규, 이재준, 이인효, 이승철, 민경민, 2023, "차세대 칼슘 이온 배터리 양극재 설계 및 선별을 위한 기계학습 플랫폼," 대한기계학회 본부추계학술대회, 송도.
- 박재정, 이재준, 이인효, 민경민, 이승철, 2023, "High-entropy Doping Strategy with Machine Learning for Maximizing Stability and Energy Density of Co-free Layered Cathode Materials," 대한금속재료학회 추계학술대회, 대구.
- 이세빈, 김태완, 이승철, 홍성호, 2023, "딥러닝 기반 마모 흔적 측정 방법," 한국트라이볼로지학회 추계학술대회, 경주.
- 이지훈, 김태완, 박형식, 이승철, 2023, "디지털 전환을 위한 필요조건: 가상 데이터 생성과 시뮬레이션 계산 가속화," 한국소음진동공학회 추계학술대회, 여수.
- 김일적, 원홍인, 윤종필, 이승철, 2023, "학습되지 않은 작동 환경에 대한 웨이브 제너레이터 베어링 고장 진단," 한국소음진동공학회 추계학술대회, 여수.
- 박건혁, 이수영, 정일주, 박준형, 이형진, 박춘수, 이승철, 2023, "고품질 및 빠른 초음파 영상 변환을 위한 딥러닝 기반 접근법," 한국소음진동공학회, 삼척.
- 정일주, 연인모, 최정우, 이승철, 2023, "메타버스 구현을 위한 음향 에코 기반 딥러닝 방 구조 예측," 한국소음진동공학회, 삼척.
- 이재준, 박재정, 이승철, 2023, "RL-GPT: 금속-유기 골격체 역설계를 위한 강화학습 기반 생성 사전학습 모델," 대한기계학회 CAE및응용역학 부문 춘계학술대회, 부산.
- 박재정, 김민선, 김희규, 이재준, 이인효, 민경민, 이승철, 2023, "제1원리 계산과 머신러닝을 활용한 기계적으로 견고한 MXene 식별," 대한기계학회 CAE및응용역학 부문 춘계학술대회, 부산.
- 이종목, 신승민, 김태완, 이승철, 2023, "물성 변화를 고려한 이중 열 교환 모사 물리기반 인공지능," 대한기계학회 CAE및응용역학 부문 춘계학술대회, 부산.
- 신승민, 이종목, 김태완, 이창환, 예인수, 최호, 이승철, 2023, "유동 해석을 위한 물리기반 인공신경망 재초기화 전략," 대한기계학회 CAE및응용역학 부문 춘계학술대회, 부산.
- 김태완, 신승민, 이종목, 이창환, 예인수, 최호, 이승철, 2023, "빠른 수치 시뮬레이션 보간을 위한 물리지식기반 컨볼루션 프레임워크," 대한기계학회 CAE및응용역학 부문 춘계학술대회, 부산.
- 김희규, 김민선, 박재정, 이재준, 이인효, 민경민, 이승철, 2023, "능동적 학습법과 결합한 기계학습 모델을 사용한 높은 평균전압을 갖는 배터리 검색 가속화: 배터리 데이터 부족 문제의 극복," 대한금속재료학회 춘계학술대회, 제주.
- 박재정, 김희규, 이재준, 박해선, 이승철, 2023, "능동적 학습과 결합된 제1원리 계산을 사용한 열역학적으로 안정된 MXenes 탐색," 대한금속재료학회 춘계학술대회, 제주.
- 이재준, 이인효, 김희규, 박재정, 김민선, 민경민, 이승철, 2023, "피쳐 조합을 통한 기계적으로 안정적인 Metal-organic Frameworks 발견 가속화," 대한금속재료학회 춘계학술대회, 제주.
- 이승철, 2023, "딥러닝 기반 재료 연구: 재료 이미지 개선, 역설계, 실험식 예측," 대한금속재료학회 춘계학술대회, 제주.
- 박형식, 이지훈, 이승철, 2023, "진동신호의 크기와 위상 성분을 모두 생성하는 GANs," 대한기계학회 신뢰성 부문 춘계학술대회, 제주도.
- 이지훈, 박형식, 이승철, 2023, "딥러닝 기반 인버전 및 속성 조작을 이용한 정상 신호로부터의 결함 진동 신호 생성 방법," 대한기계학회 신뢰성 부문 춘계학술대회, 제주도.
- 이세빈, 이종목, 이승철, 2023, "세그멘테이션을 활용한 오간 모듈 좌표 인식," 대한기계학회 신뢰성 부문 춘계학술대회, 제주도.
- 이승철, 2023, "ChatGPT 활용해서 연구하기: 교수와 대학원생 입장에서," 대한기계학회 신뢰성 부문 춘계학술대회, 제주도.
- 허현석, 김정중, 고두열, 김창현, 이승철, 2023, "딥러닝을 이용한 촉각센서 기반 물체 특성 예측 및 로봇 중요 동작 선택," 제18회 한국로봇종합학술대회, 평창.

**2022**

- Taewan Kim and Seungchul Lee\*, 2022, "A Novel Unsupervised Clustering and Domain Adaptation Framework for Rotating Machinery Fault Diagnosis," IEEE Transactions on Industrial Informatics, 19(9), https://doi.org/10.1109/TII.2022.3228395.
- Soo Young Lee, Jihun Lee, Joong Seok Lee\*, and Seungchul Lee\*, 2022, "Deep Learning-based Prediction and Interpretation of Physical Phenomena for Metaporous Materials," Materials Today Physics, 30, 100946, https://doi.org/10.1016/j.mtphys.2022.100946.
- Hyeonji Kim+, Keonhyeok Park+, Jung-Min Yon+, Sung Won Kim, Soo young Lee, Iljoo Jeong, Jinah Jang\*, Seungchul Lee\*, and Dong-Woo Cho\*, 2022, "Predicting Multipotency of Human Adult Stem Cells Derived from Various Donors through Deep Learning," Scientific Reports, https://doi.org/10.1038/s41598-022-25423-8 (+ equally contributed)
- Hyunsuk Huh, Jeong-Jung Kim, Doo-Yeol Koh, Chang-Hyun Kim, and Seungchul Lee\*, 2022, "Tactile Sensor-based Object Recognition Method Robust to Gripping Conditions Using Fast Fourier Convolution Algorithm," Journal of Korea Robotics Society, 17(3), pp. 365-372, https://doi.org/10.7746/jkros.2022.17.3.365 [in Korean].
- Gyuwon Kim+, Jung Ho Jeon+, Keonhyeok Park, Sung Won Kim, Do Hyun Kim\*, and Seungchul Lee\*, 2022, "High Throughput Screening of Mesenchymal Stem Cell Lines using Deep Learning," Scientific Reports, 12, 17507 (2022), https://doi.org/10.1038/s41598-022-21653-y. (+ equally contributed)
- Seongwook Choi+, Jinge Yang+, Soo Young Lee+, Jiwoong Kim, Seungchul Lee\*, and Chulhong Kim\*, 2022, "Deep Learning Enhances Multiparametric Dynamic Volumetric Photoacoustic Computed Tomography in Vivo (DL-PACT)," Advanced Science, https://doi.org/10.1002/advs.202202089. (+ equally contributed)
- Yuyeon Jung+, Taewan Kim+, Mi-Ryung Han, Geun Young Kim, Seungchul Lee\*, and Youn Jin Choi\*, 2021, "Machine Learning Approach of Ovarian Tumor Diagnosis Using Deep Convolutional Neural Networks," Scientific Reports, 12, 17024 (2022), https://doi.org/10.1038/s41598-022-20653-2. (+ equally contributed)
- Hae-Yeon Park+, DoGyeom Park+, Hye Seon Kang, HyunBum Kim, Seungchul Lee\*, and Sun Im\*, "Post-stroke Respiratory Complications using Machine Learning with Voice Features from Mobile Devices," Scientific Reports, 12, 16682 (2022), https://doi.org/10.1038/s41598-022-20348-8. (+ equally contributed)
- Bayu Adhi Tama, Malinda Vania, Seungchul Lee\*, and Sunghoon Lim\*, 2022, "Recent Advances in the Application of Deep Learning for Fault Diagnosis of Rotating Machinery Using Vibration Signals," Artificial Intelligence Review, https://doi.org/10.1007/s10462-022-10293-3.
- Hyoungcheol Kwon, Hyunsuk Huh, Hwiwon Seo, Songhee Han, Imhee Won, Jiwoong Sue, Dongyean Oh, Felipe Iza, Seungchul Lee\*, Sung Kye Park, and Seonyong Cha, 2022, "TCAD Augmented Generative Adversarial Network for Hot-spot Detection and Mask-layout Optimization in a Large Area HARC Etching Process," Physics of Plasma, https://doi.org/10.1063/5.0093076.
- Soo Young Lee, Jiho Chang, and Seungchul Lee\*, 2022, "Point-level Deep Learning Approach for 3D Acoustic Source Localization," Smart Structures and Systems, 29(6), https://doi.org/10.12989/sss.2022.29.6.000 .
- Keonhyeok Park+, Jong Young Lee+, Soo Young Lee, Iljoo Jeong, Jin Won Kim, Sun Ah Nam, Hyung Wook Kim\*, Seungchul Lee\*, Yong Kyun Kim\*, 2022, "Deep Learning Predicts the Differentiation of Kidney Organoids Derived from Human Induced Pluripotent Stem Cells," Kidney Research and Clinical Practice, https://doi.org/10.23876/j.krcp.22.017. (+ equally contributed)
- Sung Wook Kim, Ki-Yong Oh\*, and Seungchul Lee\*, 2022, "Novel Informed Deep Learning-Based Prognostics Framework for On-Board Health Monitoring of Lithium-Ion Batteries," Applied Energy, 315(1), https://doi.org/10.1016/j.apenergy.2022.119011.
- Soo Young Lee, Jiho Chang\*, and Seungchul Lee\*, 2022, "Deep Learning-enabled High-resolution and Fast Sound Source Localization in Spherical Microphone Array System," IEEE Transactions on Instrumentation & Measurement, Vol. 71, pp. 1-12, https://doi.org/10.1109/TIM.2022.3161693.
- Bayu Adhi Tama, Soo Young Lee, and Seungchul Lee\*, 2022, "A Systematic Mapping Study and Empirical Comparison of Data-driven Intrusion Detection Techniques in Industrial Control Networks," Archives of Computational Methods in Engineering, https://doi.org/10.1007/s11831-022-09767-y.
- Soo Young Lee, Choon-Su Park, Keonhyeok Park, Hyung Jin Lee\*, and Seungchul Lee\*, 2022, "A Physics-informed and Data-driven Deep Learning Approach for Wave Propagation and its Scattering Characteristics," Engineering with Computers, https://doi.org/10.1007/s00366-022-01640-7.
- Jongbeom Kim+, Gyuwon Kim+, Lei Li+, Pengfei Zhang, Jin Young Kim, Yeonggeun Kim, Hyung Ham Kim, Lihong V. Wang\*, Seungchul Lee\*, and Chulhong Kim\*, 2022, "Deep Learning Acceleration of Multiscale Superresolution Localization Photoacoustic Imaging," Light: Science & Applications, 11, 131, https://doi.org/10.1038/s41377-022-00820-w. (+ equally contributed)
- Gyuwon Kim+, Jongbeom Kim+, Woo June Choi\*, Chulhong Kim\*, and Seungchul Lee\*, 2022, "Integrated Deep Learning Framework for Accelerated Optical Coherence Tomography Angiography," Scientific Reports, 12, 1289, https://doi.org/10.1038/s41598-022-05281-0. (+ equally contributed)
- Sung Wook Kim, Junho Gong, Sang Won Lee\*, and Seungchul Lee\*, 2022, "Recent Advances of Artificial Intelligence in Manufacturing Industrial Sectors: A Review," International Journal of Precision Engineering and Manufacturing, https://doi.org/10.1007/s12541-021-00600-3 [invited].
- Hyunsuk Huh, Jeong-Jung Kim, Doo-Yeol Koh, Chang-Hyun Kim, and Seungchul Lee, 2022, "Deep Learning-based Physical Property Estimation of an Object using Gripper with Tactile Sensor," The 22nd International Conference on Control, Automation and Systems (ICCAS 2022), Busan, Korea.
- Kyung Seok Choi, Han Hee Lee, DoGyeom Park, Seungchul Lee, Dae Young Cheung, Bo‐In Lee, Young-Seok Cho, Jin Il Kim, and Myung‐Gyu Choi, 2022, "Reanalysis of Negative Small Bowel Capsule Endoscopy by Deep Convolutional Neural Network Model Improved Diagnostic Yield and Could Change the Outcome," UEG (United European Gastroenterology) Week, Vienna, Austria.
- Soo Young Lee, Jiho Chang, and Seungchul Lee, 2022, "Non-Contact Boundary Condition Quantification Using Data-Driven Beamforming Approach," International Congress on Acoustics (ICA 2022), Gyeongju, Korea.
- Iljoo Jeong, Injee Jung, Keonhyeok Park, Soo Young Lee, Jiho Chang, and Seungchul Lee, 2022, "Robust Sound Source Localization Against Background Noise By Deep Reconstruction Method," International Congress on Acoustics (ICA 2022), Gyeongju, Korea.
- Jongmok Lee, Junbum Park, Sungmin Kim, Seokman Sohn, and Seungchul Lee, "Deep learning-based Human Safety Management," ifip International Conference APMS (Advances in Production Management Systems) 2022, Gyeongju, Korea.
- G. Kim, J. Kim, W. J. Choi, C. Kim, and S. Lee, 2022, "Integrated Deep Learning Framework for Accelerated Optical Coherence Tomography Angiography," the International Society for Optics and Photonics (SPIE) Photonics West 2022, San Francisco, USA.
- 이정아, 박재정, 최연택, 김래언, 서민홍, 정재면, 이승철, 김형섭, 2022, "설명가능 기계학습을 결합한 생산적 적대 대치법 신경망을 사용한 구멍확장성 분석," 한국소성가공학회 추계학술대회, 제주.
- 이승철, 2022, "기계공학자를 위한 인공지능 교육은 뭐가 달라야 하는가?" 대한기계학회 추계학술대회, 제주.
- 이수영, 조완호, 정인지, 장지호, 이승철, 2022, "딥러닝 기반 음향 암호 기법," 한국소음진동공학회 추계학술대회, 제주.
- 이정아, 박재정, 최연택, 김래언, 서민홍, 정재면, 이승철, 김형섭, "생산적 적대 대치법 신경망과 설명 가능한 인공지능을 활용한 구멍 확장성 영향 요소 분석," 대한금속재료학회 추계학술대회, 제주.
- 이종목, 박준범, 김성민, 손석만, 이승철, 2022, "이상치 탐지를 이용한 산업 현장 내 위험 행동 분류," 대한기계학회 IT융합 부문 춘계학술대회, 안동.
- 이승철, 2022, "물리지식기반 인공지능에 대한 소개와 고찰," 한국소음진동공학회 춘계학술대회, 창원.
- 이수영, 이지훈, 이중석, 이승철, 2022, "딥러닝 기반 메타포러스 물질의 흡음 성능 예측 및 해석," 한국소음진동공학회 춘계학술대회, 창원.
- 이지훈, 이수영, 이중석, 이승철, 2022, "적대적 생성 신경망을 활용한 층 구조 메타포러스 역설계," 한국소음진동공학회 춘계학술대회, 창원.
- 박건혁, 이수영, 정일주, 박춘수, 이형진, 이승철, 2022, "음향 산란 역설계를 위한 물리 기반 딥러닝 접근법," 한국소음진동공학회 춘계학술대회, 창원.
- 정일주, 정인지, 이승철, 2022, "물리 기반 인공신경망을 활용한 3차원 음향인텐시티의 위치추정 오차," 한국소음진동공학회 춘계학술대회, 창원.
- 신민철, 이승철, 2022, "진동 신호에서의 데이터 불균형 문제 완화를 위한 생성 모델 적용," 한국소음진동공학회 춘계학술대회, 창원.
- 박도겸, 이승철, 2022, "에지 디바이스에서 크립그론 검출을 위한 경량 딥러닝 모델," 한국소음진동공학회 춘계학술대회, 창원.
- 이승철, 2022, "물리지식기반 인공지능에 대한 소개와 고찰," 대한기계학회 CAE및응용역학 부문 춘계학술대회, 부산.
- 김정산, 이승철, 2022, "이상치 탐지를 위한 주목 메커니즘 기반 설명가능한 특징 추출 모델," 대한기계학회 CAE및응용역학 부문 춘계학술대회, 부산.
- 김일적, 이승철, 2022, "베어링 결함 진단을 위한 시뮬레이션 데이터 기반 도메인 일반화," 대한기계학회 CAE및응용역학 부문 춘계학술대회, 부산.
- 이수영, 이형진, 박춘수, 박건혁, 이승철, 2022, "물리기반 인공신경망을 활용한 파동 산란 예측 모델 구축 및 물리적 정합성 분석," 대한기계학회 CAE및응용역학 부문 춘계학술대회, 부산.
- 김승욱, 곽은지, 오기용, 이승철, 2022, "리튬이온전지 열폭주 시뮬레이션을 위한 다중물리기반 인공지능," 대한기계학회 CAE및응용역학 부문 춘계학술대회, 부산.
- 신승민, 이지훈, 김태완, 최호, 이승철, 2022, "원형 실린더 주변의 비정상 층류 유동 해석을 통한 물리기반 인공지능 고찰," 대한기계학회 CAE및응용역학 부문 춘계학술대회, 부산.
- 김태완, 이승철, 2022, "다중 좌표계를 이용한 물리기반 인공지능," 대한기계학회 CAE및응용역학 부문 춘계학술대회, 부산.
- Juwon Na, Jaejun Lee, and Seungchul Lee, 2022, "AI Metallurgist: Data-driven Discovery of Mathematical Expressions via Natural Language Processing," 대한금속재료학회, 창원.
- 신민철, 이승철, 2022, "진동 신호에서의 데이터 불균형 문제 완화를 위한 생성 모델 적용," 대한기계학회 신뢰성 부문 춘계학술대회, 제주도.
- 김일적, 김정산, 이승철, 2022, "단일 도메인 일반화 및 물리적으로 설명 가능한 베어링 고장 진단," 대한기계학회 신뢰성부문 춘계학술대회, 제주도.
- 박도겸, 나주원, 이승철, 2022, "에지 디바이스에서 크립그론 검출을 위한 경량 딥러닝 모델," 대한기계학회 신뢰성부문 춘계학술대회, 제주도.

**2021**

- Sampa Misra, Seungwan Jeon, Ravi Managuli, Seiyon Lee, Gyuwon Kim, Chiho Yoon, Seungchul Lee, Richard G. Barr\*, and Chulhong Kim\*, 2021, "Bi-modal Transfer Learning for Classifying Breast Cancers via Combined B-mode and Ultrasound Strain Imaging," IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control, 69(1), pp. 222-232, 10.1109/TUFFC.2021.3119251. (front cover page)
- Do-Won Kim, Jae Hyuk Lim\*, and Seungchul Lee, 2021, "Prediction and Validation of the Transverse Mechanical Behavior of Unidirectional Composites Considering Interfacial Debonding through Convolutional Neural Networks," Composites Part B: Engineering, https://doi.org/10.1016/j.compositesb.2021.109314.
- Taewan Kim+, Young Hoon Choi+, Jin Ho Choi, Sang Hyub Lee, Seungchul Lee\*, and In Seok Lee\*, 2021, "Gallbladder Polyp Classification in Ultrasound Images using a New Ensemble Model," Journal of Clinical Medicine, 10(16), 3585, https://doi.org/10.3390/jcm10163585. (+ equally contributed)
- Chang Kyo Oh+, Taewan Kim+, Yu Kyung Cho, Dae Young Cheung, Bo‐In Lee, Young‐Seok Cho, Jin Il Kim, Myung‐Gyu Choi, Han Hee Lee\*, and Seungchul Lee\*, 2021, "Convolutional Neural Network-based Object Detection Model to Identify Gastrointestinal Stromal Tumors on Endoscopic Ultrasonography Images," Journal of Gastroenterology and Hepatology, https://doi.org/10.1111/jgh.15653. (+ equally contributed)
- Bayu Adhi Tama, and Seungchul Lee\*, 2021, "Comments on Stacking Ensemble based Deep Neural Networks Modeling for Effective Epileptic Seizure Detection," Expert Systems with Applications, https://doi.org/10.1016/j.eswa.2021.115488.
- Juwon Na, Gyuwon Kim, Seong-Hoon Kang, Se-Jong Kim\*, and Seungchul Lee\*, 2021, "Deep Learning-based Discriminative Refocusing of Scanning Electron Microscopy Images for Materials Science," Acta Materialia, 214, 116987, https://doi.org/10.1016/j.actamat.2021.116987.
- Jaimyun Jung+, Juwon Na+, Hyung Keun Park, Jeong Min Park, Gyuwon Kim, Seungchul Lee\*, and Hyoung Seop Kim\*, 2021, "Super-resolving Material Microstructure Image via Deep Learning for Microstructure Characterization and Mechanical Behavior Analysis," npj Computational Materials, 7(96), https://doi.org/10.1038/s41524-021-00568-8. (+ equally contributed)
- Soo Young Lee+, Jiho Chang+, and Seungchul Lee\*, 2021, "Deep Learning-based Method for Multiple Sound Source Localization with High Resolution and Accuracy," Mechanical Systems and Signal Processing, 161, 107959, https://doi.org/10.1016/j.ymssp.2021.107959. (+ equally contributed)
- Sung Wook Kim, Seong-Hoon Kang, Se-Jong Kim\*, and Seungchul Lee\*, 2021, "Estimating the Phase Volume Fraction of Multi-Phase Steel via Unsupervised Deep Learning," Scientific Reports, 11, 5902, https://doi.org/10.1038/s41598-021-85407-y.
- Sung Wook Kim, Iljeok Kim, Jonghwan Lee, and Seungchul Lee\*, 2021, "Knowledge Integration into Deep Learning in Dynamical Systems: An Overview and Taxonomy," Journal of Mechanical Science and Technology, 35(4), https://doi.org/10.1007/s12206-021-0342-5 [invited].
- Sung Wook Kim, Ki-Yong Oh, and Seungchul Lee\*, 2021, "Physics-Informed Neural Network For Estimation Of Lithium-Ion Battery State-of-Health," Transactions on the Korean Society for Noise and Vibration Engineering, 31(2), pp. 178-185, https://doi.org/10.5050/KSNVE.2021.31.2.178 [In Korean].
- Andrew Glaeser, Soo Young Lee, Yunseob Hwang, Vignesh Selvaraj, Kangsan Lee, Namjeong Lee, Seungchul Lee, and Sangkee Min\*, 2021, "Applications of Deep Learning for Fault Detection in Industrial Cold Forging," International Journal of Production Research, https://doi.org/10.1080/00207543.2021.1891318.
- Yongju Kim, Hyung Keun Park, Jaimyun Jung, Peyman Asghari-Rad, Seungchul Lee, Jin You Kim, Hwan Gyo Jung, and Hyoung Seop Kim\*, 2021, "Exploration of Optimal Microstructure and Mechanical Properties in Continuous Microstructure Space using a Variational Autoencoder," Materials & Design, Vol. 202, https://doi.org/10.1016/j.matdes.2021.109544.
- Gyuwon Kim, Soo Young Lee, Jong-Seok Oh, and Seungchul Lee\*, 2021, "Deep Learning-based Estimation of the Unknown Road Profile and State Variables for the Vehicle Suspension System," IEEE Access, 13878-13890, https://doi.org/10.1109/ACCESS.2021.3051619.
- Yunseob Hwang+, Han Hee Lee+, Chunghyun Park, Bayu Adhi Tama, Jin Su Kim, Dae Young Cheung, Woo Chul Chung, Young-Seok Cho, Kang-Moon Lee, Myung-Gyu Choi, Seungchul Lee\*, and Bo-In Lee\*, 2021, "Improved Classification and Localization Approach to Small Bowel Capsule Endoscopy Using Convolutional Neural Network," Digestive Endoscopy, 33, pp. 598-607, https://doi.org/10.1111/den.13787. (+ equally contributed)
- Hyuckcheol Kwon, Jongwhan Lee, Seungchul Lee, Taekyu An, Youngseok Cho, and Jeasook Chung, 2021, "Analysis and Control of Bar Warping in Roughing Mill of HSM," ASIA STEEL 2021, Gyeongju, Korea.
- Iljeok Kim, Sung Wook Kim, Jeongsan Kim, Taegyu Choi, Jungchan Kim, and Seungchul Lee, 2021, "A Novel Interpretable and Generalized Learning Method for Bearing Fault Diagnosis," PHMAP 2021, Seoul, Korea.
- Soo Young Lee, Jiho Chang, and Seungchul Lee, 2021, "Point-level Deep Learning Approach for 3D Sound Source Localization in Spherical Microphone Array," PHMAP 2021, Seoul, Korea.
- Sung Wook Kim, Ki-Yong Oh, and Seungchul Lee, 2021, "A Novel Physics-Infused Recurrent Neural Network for Health Monitoring of Lithium-Ion Batteries," PHMAP 2021, Seoul, Korea.
- Taewan Kim and Seungchul Lee, 2021, "Deep Learning-based Bearing Health Indicator Construction for Better RUL Prediction," PHMAP 2021, Seoul, Korea.
- Soo Young Lee, Jiho Chang, and Seungchul Lee, 2021, "Deep Learning-enhanced Single Point Sound Source Localization for Spherical Microphone Array," inter-noise 2021, Online.
- Hyunsuk Huh, and Seungchul Lee, 2021, "Background Noise Removal Technique using Deep Learning Segmentation Network without Segmentation Map," inter-noise 2021, Online.
- Gyuwon Kim, and Seungchul Lee, 2021, "Generative Adversarial Neural Network for Unsupervised Bearing Fault Detection," inter-noise 2021, Online.
- Taewan Kim and Seungchul Lee, 2021, "Deep Learning-based Health Indicator for Better Bearing RUL Prediction," inter-noise 2021, Online.
- Seungchul Lee, 2021, "Deep Learning-based Sound Source Localization and its Applications," The Korean Society for Noise and Vibration Engineering, Jeju, Korea.
- Soo Young Lee, Hyoungjin Lee, Chunsoo Park and Seungchul Lee, 2021, "Deep Learning for Simulating the Wave Propagation and its Scattering Physics," The Korean Society for Noise and Vibration Engineering, Jeju, Korea.
- Iljoo Jeong, Mooyeob Lee and Seungchul Lee, 2021, "Wafer Failure Map Retrieval using Multiple Global Descriptors," The Korean Society for Noise and Vibration Engineering, Jeju, Korea.
- Taewan Kim, and Seungchul Lee, 2021, "Unsupervised Fault Clustering Method using Adversarial Autoencoder and Gaussian Mixture Model," The Korean Society for Noise and Vibration Engineering, Jeju, Korea.
- Jeongsan Kim, and Seungchul Lee, 2021, "Anomaly Detection in Planetary Gear via Generative Deep Learning Model using Short Time Fourier Transformation with Order Representation," The Korean Society for Noise and Vibration Engineering, Jeju, Korea.
- Seungchul Lee, 2021, "Recent Trends in Physics-informed Deep Learning," The Korean Society of Mechanical Engineers, Gwangju, Korea.
- Juwon Na, Se-Jong Kim, and Seungchul Lee, 2021, "Weakly Supervised Microstructure Segmentation via Scribble Annotations," The Korean Society of Mechanical Engineers, Gwangju, Korea.
- Jongmok Lee, Changyun Choi, Junbum Park, Sungmin Kim, Seokman Sohn, and, Seungchul Lee, 2021, "Deep Learning-based Human Action Recognition in Real-Time to Prevent Industrial Workplace Accident," The Korean Society of Mechanical Engineers, Gwangju, Korea.
- 김세종, 강성훈, 정재면, 이호원, 오세혁, 오영석, 나주원, 이승철, 2021, "딥러닝을 이용한 광학 미세조직 결함 보정," 대한금속재료학회 추계학술대회, 제주도, 한국.
- Juwon Na, Se-Jong Kim, and Seungchul Lee, 2021, "Deep Learning-based Grain Boundary Detection on Polycrystalline Materials in an Unsupervised Manner," The Korean Institute of Metals and Materials, Jeju, Korea.
- Juwon Na, Se-Jong Kim, and Seungchul Lee, 2021, "Weakly Supervised Microstructure Segmentation via Scribble Annotations," The Korean Institute of Metals and Materials, Jeju, Korea. (Best Paper Award)
- Jongmok Lee, Changyun Choi, Junbum Park, Sungmin Kim, Seokman Sohn, and Seungchul Lee, 2021, "Deep Learning-based Human Action Recognition to Prevent Industrial Workplace Accident," The Korea Society of Safety, Yeosu, Korea.
- Changyun Choi and Seungchul Lee, 2021, "Missing Marker Refinement for Motion Data using Directed Graph Neural Network," The Korean Society for Noise and Vibration Engineering, Pyeongchang, Korea.
- Hyunsuk Huh and Seungchul Lee, 2021, "Important Feature Extraction for Classification using Deep Segmentation Model," The Korean Society for Noise and Vibration Engineering, Pyeongchang, Korea.
- Iljeok Kim, Jeongsan Kim, Taegyu Choi, Jungchan Kim, and Seungchul Lee, 2021, "Bearing Fault Diagnosis using Explainable CNN and Signal Processing," The Korean Society for Noise and Vibration Engineering, Pyeongchang, Korea.
- Soo Young Lee, Jiho Chang, and Seungchul Lee, 2021, "Super-resolved Sound Source Localization via Deep Learning," The Korean Society for Noise and Vibration Engineering, Pyeongchang, Korea.
- Juwon Na, Seungchul Lee, and Se Jong Kim, 2021, "Deep Learning-based Grain Boundary Contrast Enhancement," Materials Research Society of Korea, Online.
- Gyuwon Kim, Jongbeom Kim, Woo June Choi, Chulhong Kim, and Seungchul Lee, 2021, "Deep Learning-based Acceleration of Optical Coherence Tomography Angiography," The Korean Society of Medical & Biological Engineering, Online. (Best Paper Award)
- Jiho Chang, Sooyoung Lee, and Seungchul Lee, 2021, "Deep Learning-based Sound Source Localization with High Resolution," The Acoustical Society of Korea, Jeju, Korea.
- Sung Wook Kim, Ki-Yong Oh, and Seungchul Lee, 2021, "SOH Monitoring and RUL Estimation of Lithium-Ion Batteries using Physics Infused Deep Learning," Reliability Engineering Division in the Korean Society of Mechanical Engineers, Jeju, Korea.
- Taewan Kim, and Seungchul Lee, 2021, "Bearing Health Indicator Construction using Adversarial Autoencoder," Reliability Engineering Division in the Korean Society of Mechanical Engineers, Jeju, Korea.
- Jongmok Lee, Changyun Choi, Junbum Park, Sungmin Kim, Seokman Sohn, and Seungchul Lee, 2021, "Deep Learning-based Human Action Recognition to Prevent Industrial Workplace Accidents," Reliability Engineering Division in the Korean Society of Mechanical Engineers, Jeju, Korea.
- Jeongsan Kim, Iljeok Kim, Jungchan Kim, Taegyu Choi, and Seungchul Lee, 2021, "Deep Learning-based Planetary Gear Fault Diagnosis using Frequency Domain Averaging," Reliability Engineering Division in the Korean Society of Mechanical Engineers, Jeju, Korea.
- Jong Hwan Lee, Eon Ho Im, Hyuck Cheol Kwon, Jea Sook Chung, and Seungchul Lee, 2021, "Deep Learning-based Analysis on Physical Factors of Bar Warping in Rolling Process," Reliability Engineering Division in the Korean Society of Mechanical Engineers, Jeju, Korea.
- Il Joo Jeong and Seungchul Lee, 2021, "Wafer Map Failure Pattern Classification using Geometrical Transformation Invariant Convolutional Neural Network," Reliability Engineering Division in the Korean Society of Mechanical Engineers, Jeju, Korea.
- Gyuwon Kim, Jongbeom Kim, Woo June Choi, Chulhong Kim, and Seungchul Lee, 2021, "Integrated Deep Learning Framework for Accelerated Optical Coherence Tomography Angiography," Bio Engineering Division in the Korean Society of Mechanical Engineers, Online.
- Keonhyeok Park, Hyeonji Kim, Gyuwon Kim, Jinah Jang and Seungchul Lee, 2021, "Morphological Prediction of hTMSCs Lineage to Keratocyte using Deep Learning," Bio Engineering Division in the Korean Society of Mechanical Engineers, Online.

## 특허

Journal 페이지 Patent 부분의 Registered 8건 가운데 날짜가 2021년 10월 13일 이후인 6건(2022년 2월–2026년 3월)과 Filed 6건 전부(2022년 1월–2023년 5월 출원), 모두 12건이다. 줄 앞 날짜는 줄에 적힌 등록일 또는 출원일이고, 각 줄의 발명자·국가·번호·비고는 누리집 표기 그대로다. 모든 특허는 이승철 교수와 다른 발명자가 함께 적혀 있다. 날짜가 2023년 8월 전인 특허는 교수가 POSTECH에 있던 시기에 등록·출원한 것이다.[^journal][^prof]

- 2026-03-10 · APPARATUS FOR DIAGNOSING DISEASE CAUSING VOICE AND SWALLOWING DISORDERS AND METHOD FOR DIAGNOSING SAME, 임선/이승철/주영훈/한연재/전주형, US, 2026년 3월 10일, 12,573,504 B2 (상태 등록)
- 2025-10-14 · CELL SELECTION APPARATUS AND METHOD, 김도현/김성원/곽승기/전정호/이재선/이승철/김규원, US, 2025년 10월 14일, P2020412-04-US (상태 등록)
- 2024-02-26 · 딥러닝을 이용한 볼의 마모량 측정 방법, 홍성호/이승철/이세빈/김태완, 대한민국, 2024년 2월 26일, 10-2642450 (상태 등록)
- 2022-08-30 · 세포 선별 장치 및 방법, 김도현/김성원/곽승기/전정호/이재선/이승철/김규원, 대한민국, 2022년 8월 30일, 10-2439441 (상태 등록)
- 2022-06-23 · 인공지능 신경망을 이용한 고해상도 음원지도 취득 및 분석방법 및 시스템, 장지호/이승철/이수영, 2022년 6월 23일, 대한민국, 10-2414021, (비즈웨이브 주식회사로 25,000천원 기술이전, 유럽/미국 출원 중, PCT/KR2021/006616) (상태 등록)
- 2022-02-03 · 캡슐 내시경 영상 판독 시스템 및 방법, 이한희/이승철/황윤섭, 2022년 2월 3일, 대한민국, 10-2359984 (미국 출원 중, PCT/KR2021/004735) (상태 등록)
- 2022-01-24 · 담낭 용종 판단 시스템 및 그 방법, 이인석/최영훈/이승철/김태완, 대한민국, 2022년 1월 24일 출원, 10-2022-0010235 (상태 출원)
- 2022-02-21 · 오가노이드 선별 장치 및 방법, 김도현/이승철/김성원/임미현/박건혁/신승민, 대한민국, 2022년 2월 21일 출원, 10-2022-0022545 (상태 출원)
- 2022-04-08 · 신경망 학습부 및 이를 포함하는 개선된 음원지도 제공 시스템, 장지호/조완호/이승철/이수영, 대한민국, 2022년 4월 8일 출원, 10-2022-0043976 (상태 출원)
- 2022-12-02 · 난소 종양 분류 방법 및 장치, 최윤진/이승철/김태완/정유연, 대한민국, 2022년 12월 2일 출원, 10-2022-0167068 (상태 출원)
- 2022-12-17 · 가상의 데이터 생성을 통한 자동 고장 진단 장치 및 그 작동 방법, 이승철/김민호/신민철, 대한민국, 2022년 12월 17일 출원, 10-2022-0170093 (상태 출원)
- 2023-05-08 · 인공지능 기반 고장 특성 조작을 이용한 설비의 정상 신호로부터 고장 신호 생성 기술, 이승철/박형식/이지훈, 대한민국, 2023년 5월 8일 출원, 10-2023-0059375 (상태 출원)

## 연구 과제

RESEARCH 메뉴 PROJECTS 페이지의 On-going 표 가운데 7건과 Completed 표 가운데 끝난 날이 2021년 10월 13일 이후인 12건, 모두 19건이다. 과제명·지원 기관·기간·역할(PI, co-PI)은 표 그대로이고, 상태는 표의 구분(On-going은 진행, Completed는 종료)이다. On-going 표의 「물리지식기반 미세조직 예측 인공지능 모델 개발」은 시작·끝 칸이 비어 있다. 연구실이 KAIST로 옮긴 2023년 8월 전에 시작한 과제는 교수가 POSTECH에 있던 시기에 시작한 과제다.[^projects][^news]

- 물리지식기반 미세조직 예측 인공지능 모델 개발 (지원 포스코홀딩스; 역할 PI; 상태 진행)
- 물리지식인공지능기반 시뮬레이션 대리 모델링을 통한 탄 공력 성능 예측 프로그램 개발 (지원 풍산-KAIST 미래기술연구센터; 기간 2026.01–; 역할 PI; 상태 진행)
- 첨단제조지능혁신센터 (글로컬랩) (지원 교육부, 한국연구재단; 기간 2025.09–; 역할 co-PI; 상태 진행)
- AI 기반 지능형 설계-제조 통합 연구단 (InnoCORE) (지원 과학기술정보통신부; 기간 2025.07–; 역할 co-PI; 상태 진행)
- 인공지능 기술 및 데이터를 활용한 우주항공용 초내열 비철 금속소재의 HUB 구축 (지원 과학기술정보통신부; 기간 2024.07–2028.12; 역할 co-PI; 상태 진행)
- 물리기반 인공지능의 공학 분야 활용을 위한 요소 기술 연구 (지원 한국과학기술원; 기간 2023.08.28–2026.12.31; 역할 PI; 상태 진행)
- 입체적 요철 구조의 물질 투과성 박막 스캐폴드 및 투과성 초미세관류 기반 in situ 균일 세포 응집/증식/분화용 3D 바이오리액터 자동화 배양시스템 개발 (지원 한국산업기술평가관리원; 기간 2023.04.01–2026.12.31; 역할 co-PI; 상태 진행)
- DeepONet 기반 연산자 학습을 이용한 CFD 결과 내삽 및 고해상화 기술 개발 (지원 포스코 홀딩스; 기간 2025.07–2025.12; 역할 PI; 상태 종료)
- CNN 기반의 U-net을 사용한 CFD 내삽기술 개발 (지원 포스코홀딩스; 기간 2024.05.03–2025.04.25; 역할 PI; 상태 종료)
- 상호연동 모듈형 허리, 어깨, 무릎 근력보조 엑소수트 기술 개발 (지원 국방과학연구소; 기간 2019.06–2024.12; 역할 co-PI; 상태 종료)
- 발전소 안전환경 정착을 위한 IoT기반 작업안전관리 플랫폼 개발 (지원 한국에너지기술평가원; 기간 2020.05.01–2024.10.31; 역할 co-PI; 상태 종료)
- 이동식 모니터링을 위한 음향 신호의 예측 및 분리 기술 개발 (지원 한국표준과학연구원; 기간 2023.01.01–2023.12.31; 역할 PI; 상태 종료)
- 소성로 내부 현상 실시간 가시화를 위한 시뮬레이션 기술 개발 (지원 포스코홀딩스; 기간 2022.10.24–2023.09.22; 역할 PI; 상태 종료)
- 딥러닝 알고리즘 적용 원전 회전 기기 고장 데이터 생성 기술 개발 (지원 한국수력원자력 (K-CLOUD); 기간 2021.06.01–2023.05.31; 역할 PI; 상태 종료)
- 인공지능 기반 건전성 관리 지능화: 유사/비유사 환경에서의 강건성 증대를 위한 딥러닝 기반 진단·예지 요소 기술 개발 (지원 한국연구재단; 기간 2020.03–2022.12; 역할 PI; 상태 종료)
- 배경소음 및 잔향에 강건한 고해상도 음원 지도 알고리즘 개발 (지원 한국표준과학연구원; 기간 2021.04.01–2022.12.31; 역할 PI; 상태 종료)
- 블레이드 Tip Timing 센서 신호처리/진단 알고리즘 코드화 및 성능 평가 (지원 두산에너빌리티; 기간 2021.09.01–2022.12.31; 역할 PI; 상태 종료)
- 상용화를 위한 인공지능 이용 호흡기도 오가노이드의 표준화 (지원 서울성모병원; 기간 2021.07.01–2022.06.30; 역할 co-PI; 상태 종료)
- Decomposed and Physics-guided AI 기반 주편크랙 예측기술 개발 (지원 POSCO; 기간 2020.11.01–2021.10.31; 역할 PI; 상태 종료)

## 소식

NEWS 2026 페이지와 NEWS 메뉴의 2021–2025년 페이지에서 날짜가 2021년 10월 15일–2026년 10월 22일인 글 467건이다. 날짜는 글에 붙은 날짜(기간 글은 시작과 끝)이고, 문구는 글 제목 줄 그대로다. 2021년 12월 글 1건은 날짜가 달까지만 적혀 있다. 2023년 8월 28일 전 글은 연구실이 KAIST로 옮기기 전, 교수가 POSTECH에 있던 시기의 소식이다.[^news][^prof]

- 2026-10-22 · 이승철 교수, Samsung SDI 기술 세미나에서 "Active Learing in Process Optimization, and eXplainable AI for Manufacturing" 주제로 발표
- 2026-10-14 · 이승철 교수, 한전 전력연구원 'AI-PHM 기술의 산학연 융복합' 세미나에서 'Agentic AI 시대, 공학자의 역할은 어떻게 바뀌는가?' 주제로 발표
- 2026-10-11 · Prof. Seungchul Lee gives an Educational Workshop at the International Conference on the Technology of Plasticity 2026 (ICTP2026)
- 2026-10-07 · 이승철 교수, HD건설기계 및 HD현대사이트솔루션 임원 대상, 'Agentic AI 시대, 건설기계산업 공학 연구의 새로운 패러다임' 강연
- 2026-10-02 · 이승철 교수, 울산대 Industrial AX 대학원에서 'Agentic AI 관점에서 바라본 공학 연구의 변화' 주제로 세미나 진행
- 2026-09-30 · 이승철 교수, 2026년 산학협력 유공자 교육부 장관 표창 수상
- 2026-09-28–2026-10-01 · AI4Sci Korea 2026, Seoul Dragon City
- 2026-09-16–2026-09-18 · 한국센서학회 추계학술대회, 여수 (Physical AI 시대를 여는 초감각 센서기술)
- 2026-09-04 · 대한기계학회 신뢰성부문 산학연 워크삽, 포스코타워 역삼
- 2026-09-03 · 풍산-KAIST 미래기술연구센터 2026년 워크샵 및 3차 운영위원회
- 2026-09-02 · HD건설기계, iAI 연구실 방문
- 2026-09-01 · 연구 성과 홍보: 3D 프린팅으로 달걀부터 1kg 물병까지 ‘척척’ 잡는 부드러운 로봇 손 만들었다
- 2026-08-26 · A group of students from Zhejiang University visits KAIST.
- 2026-08-24–2026-08-26 · iAI participates in the 19th East Asia SIAM (EASIAM) Annual Meeting in Jeju, Korea.
- 2026-08-21 · 최성욱 학생, 경북대학교 기계공학부 "최우수졸업생상" 수상
- 2026-08-20 · Tianjin University visits KAIST to explore international collaboration
- 2026-08-19–2026-08-21 · 대한금속재료학회 인공지능재료과학 분과, 제13회 재료인공지능 여름학교 @ 경북대학교
- 2026-08-19 · 대한기계학회 기계인공지능연구회 전문가 심포지엄, 고려대학교
- 2026-08-13 · SHI-KAIST 차세대선박연구센터 개소식 참석
- 2026-08-12 · Congratulations to Yenee Oh on successfully passing her master's preliminary exam !!!
- 2026-08-10–2026-08-11 · 대한기계학회 기계인공지능 연구회, LLM 기반 AI 에이전트 강습회, 광주과학기술원
- 2026-07-27 · 대한기계학회 CAE 및 응용역학 부문, 기계공학도를 위한 Agentic AI 실전 강습회, 동국대학교
- 2026-07-20–2026-07-24 · iAI participates in the 17th World Congress on Computational Mechanics (WCCM-ECCOMAS 2026) in Munich, Germany.
- 2026-07-14 · 한국생산제조학회 춘계학술대회 참가, 강릉세이트존스 호텔
- 2026-07-13–2026-07-15 · 대한기계학회 기계인공지능 연구회, 인공지능 여름학교, 연세대
- 2026-07-09 · 한국과학영재학교 R&E 여름방학 현장연구학습 시작
- 2026-07-08 · iAI Undergraduate Research Interns
- 2026-07-02 · iAI 연구실, 한국소성·가공학회 전문교육 진행 @ 카이스트, 대전
- 2026-07-01 · iAI attends the seminar titled "Bioelectronics: From Exploratory Research to Medical Translation" by Prof. John A. Rogers of Northwestern University.
- 2026-07-01 · 박재정 학생, 국가소재연구데이터센터 사용자 클럽 분과 워크샵 참가
- 2026-06-29–2026-07-03 · Prof. Sooyoung Lee at Chung-Ang University gives a presentation entitled "Physical AI for Manufacturing: A Call for Clarity and Rigor" at the international conference on PRecision Engineering and Sustainable Manufacturing (PRESM) at Singapore.
- 2026-06-25 · 풍산-KAIST 미래기술연구센터 2차 운영위원회 발표
- 2026-06-18 · 산자부 기계장비사업 (약칭: 세포응집체 배양자동화 과제) 4차년도 워크샵 참석, 포항
- 2026-06-18 · 이승철 교수, HD건설기계 자문위원회 기술 토론회 참가
- 2026-06-16 · 이승철 교수, 국민대학교 ERC (로봇 기능성 스킨 및 초감각 연구센터) 전문가 초청 워크샵 발표, 서울
- 2026-06-09 · 한국생산기술연구원 2026년 심화형 제조 AI 전문가 교육 프로그램, 송도
- 2026-06-04–2026-06-05 · InnoCORE Workshop for InnoCORE Fellows
- 2026-06-04 · 김윤영 교수님, 카이스트 기계공학과 학부생 대상 강연
- 2026-06-02 · Jongmok Lee successfully completes his doctoral dissertation defense. Congrats !!!
- 2026-06-01 · HD현대사이트솔루션, iAI 연구실 방문
- 2026-05-29–2026-05-30 · The KAIST ME delegation visits the Department of Mechanical Engineering at Tsinghua University to facilitate a joint exchange on AI education and research.
- 2026-05-27–2026-05-29 · 한국소음진동공학회 춘계학술대회 참가, 삼척 (쏠비치)
- 2026-05-26 · 한국생산기술연구원 2026년 심화형 제조 AI 전문가 교육 프로그램, 송도
- 2026-05-19 · Prof. Sooyoung Lee at Chung-Ang University gives a presentation entitled "Towards Engineering Intelligence: Foundations of Engineering-Centric AI for Analysis and Optimization" at ACSMO 2026, Busan.
- 2026-05-14–2026-05-15 · 2026년 KAIST 산학협동 공개강좌, AI가 대신 일하는 시대: LLM 기반 산업 AI Agent 설계와 구현 (58명 참가)
- 2026-05-14 · 중앙대 이수영 교수, 한국정밀공학회 춘계학술대회 정밀공학의 AI 융합을 위한 전략 포럼에서 [공학 지능을 위한 '도메인 기반 AI'의 도전과 기회] 주제로 강연.
- 2026-05-12 · 한국생산기술연구원 2026년 심화형 제조 AI 전문가 교육 프로그램, 송도
- 2026-05-06–2026-05-08 · 대한기계학회 CAE및응용역학 부문 춘계학술대회 참가, 여수 (소노캄)
- 2026-04-30 · 한국생산기술연구원 2026년 심화형 제조 AI 전문가 교육 프로그램, 송도
- 2026-04-27–2026-04-28 · InnoCORE Workshop on Global Manufacturing AX Forum
- 2026-04-08–2026-04-10 · 산업인공지능 연구실, 대한기계학회 신뢰성 부문 춘계학술대회 참여, 제주 (롯데호텔)
- 2026-04-08 · 튜토리얼 세션: PINN-guided LLM 에이전트와 신뢰성
- 2026-04-06 · 이승철 교수, HD건설기계 교수자문위원회 자율화분야 자문위원 위촉
- 2026-04-02 · 한국생산기술연구원 2026년 심화형 제조 AI 전문가 교육 프로그램, 송도
- 2026-03-31 · 이승철 교수, 대구경북과학기술원 로봇및기계전자공학 세미나, 대구
- 2026-03-27 · 풍산-KAIST 미래기술연구센터 1차 운영위원회
- 2026-03-26–2026-03-27 · 한국설비진단자격인증원 강습회, 여수(히든베이 호텔)
- 2026-03-26 · Technical Tour: KIMM
- 2026-03-25–2026-03-26 · A delegation from the Department of Mechanical Engineering at Tsinghua University visits KAIST to discuss the future of AI education and research collaboration in ME.
- 2026-03-18–2026-03-19 · 이승철 교수, 한국센서학회 AI센서플랫폼 세션에서 초청발표, 서울
- 2026-03-10 · 박범수 교수, 연구실 방문
- 2026-03-06 · 카이스트 AI수학대학원 Opening Workshop 참석, 대전
- 2026-03-04 · 초내열소재 HUB 2단계 착수회의 참석, 부산 (호메르스 호텔 )
- 2026-03-01 · Dr. Bumsoo Park Appointed as Assistant Professor in MSDE at Seoul National University of Science and Technology (SeoulTech) where he will lead the Manufacturing AI lab.
- 2026-02-27 · 대한기계학회 기계인공지능연구회 주관, 물리지식기반 인공지능 워크샵, 포스코타워 역삼
- 2026-02-25–2026-02-27 · 카이스트 기계공학과, 'AI 기반 설계: 해석에서 설계 최적화 및 PINN/LLM 활용까지' 동계 산학협동 강좌, 대전
- 2026-02-23 · 산업 인공지능 연구실, "AI 시대, 대학교육의 재설계" 워크샵 참석, 대전
- 2026-02-10–2026-02-11 · 대한금속·재료공학회 인공지능재료과학분과 제12회 재료인공지능 겨울학교 진행, 한국생산기술연구원 지능화뿌리기술연구소 (인천 송도국제도시)
- 2026-01-19–2026-01-22 · 대한기계학회 기계인공지능연구회 주관, 인공지능 겨울학교, 광주
- 2026-01-15 · 연구 성과 홍보: 중앙대 기계공학부 이수영 교수 연구팀, 물리기반 인공지능으로 미래 제조 청사진 제시
- 2026-01-14 · 산업인공지능연구실, 한국최적설계학회 (Korean Society for Design Optimization) 참가, 대전
- 2026-01-08 · KAIST 기계공학과 뉴스레터 홍보용 포스터
- 2025-12-30 · NOVIC+ Thesis Festival
- 2025-12-29 · Dr. Bumsoo Park will be joining the Department of Manufacturing Systems and Design Engineering (MSDE) at Seoul National University of Science and Technology (SeoulTech) as an Assistant Professor, starting on March 1, 2026. Congratulations!
- 2025-12-23 · Hyeokjin Kweon successfully completes his master's thesis defense. Congrats !!!
- 2025-12-19 · 이승철 교수, 대한기계학회 2025 김윤영AI교육혁신상 수상.
- 2025-12-18 · Dr. Doksoo Lee gives a seminar entitled “Co-Design of Programmable Material Systems,” hosted by Prof. Seungchul Lee.
- 2025-12-16 · 글로컬랩 '첨단제조지능혁신센터' 참여기업 대상 설명회 참석, 대전
- 2025-12-16 · 제 3회 국가 소재 데이터 스테이션(K-MDS) 사용자 클럽 통합 워크숍 및 제 4회 소재 연구데이터 활용 인공지능 기술 워크숍 참석, 대전
- 2025-12-10–2025-12-12 · 대한기계학회 창립 80주년 기념 학술대회 참가, 하이원 그랜드호텔 컨벤션타워 (강원랜드)
- 2025-12-08 · Keonhyeok Park successfully completes his doctoral dissertation defense. Congrats !!!
- 2025-12-07–2025-12-10 · iAI lab attends the 9th Asian Congress on Computational Mechanics & the 7th Australasian Conference on Computational Mechanics (APCOM-ACCM 2025), Brisbane, Australia.
- 2025-11-27 · 한국전산구조공학회 추계학술대회, 대전
- 2025-11-26–2025-11-28 · 한국소음진동공학회 추계학술대회, 경주
- 2025-11-18 · 포스코그룹 테크포럼에서 포스코홀딩스와의 산학협력 과제가 도약상을 수상
- 2025-11-07 · 한국설비진단자격인증원 자격인증시험, KAIST 기계공학동 (N7)
- 2025-10-30 · 박재정 학생, 대한금속·재료학회 추계학술대회, 광주 김대중컨벤션센터
- 2025-10-16 · 권혁진 학생, 한국트라이볼로지 학회에서 발표, 제주
- 2025-10-15 · 대한용접·접합학회 추계학술대회 특별세션 (인공지능 기술 및 데이터를 활용한 초내열소재 HUB 1단계 결과 발표회 및 시연회)
- 2025-09-25 · iAI attends the seminar “How to Turn Imagination into Reality” by Prof. Dennis Hong.
- 2025-09-22 · iAI attends the KAIST Day for Igniting MICCAI 2025 (The Medical Image Computing and Computer Assisted Intervention Society).
- 2025-09-19 · 산업 인공지능 연구실, 기계공학과 연구실 소개 행사 참가.
- 2025-09-12 · 대한기계학회 신뢰성부문 산학연 협동 세미나 '반도체 신뢰성: 패키징, 디지털 트윈, AI 응용' 포스코타워 역삼
- 2025-09-08 · 박재정 학생, IPESK (한국이공학진흥원) 차세대공학연구자에 선정. 축하합니다.
- 2025-08-29–2026-02-26 · Prof. Seungchul Lee will be on sabbatical leave for six months.
- 2025-08-29 · A group of students from Zhejiang University in China visit the KAIST ME Department (hosted by Prof. Ikjin Lee).
- 2025-08-28 · 박재정 학생이 이공분야 학문후속세대 지원사업 박사과정생연구장려금지원사업에 선정되었습니다. 축하합니다.
- 2025-08-21 · 한국전산유체공학회 30주년 기념, AI-CFD International Mini Symposium om "Scientific Machine Learning and AI for CFE," POSCO Tower, Seoul
- 2025-08-20 · 대한기계학회 기계인공지능연구회, 기계인공지능 전문가 심포지엄, 포스코타워 역삼
- 2025-08-08 · 한국전산구조공학회 신기술강습회"유한요소 이론부터 Abaqus 실습까지 한눈에" 참가 (연세대)
- 2025-08-05 · Congratulations to Hyeokjin Kweon on successfully passing his master's preliminary exam !!!
- 2025-07-28 · 중앙대 이수영 교수, "슬기로운 대학원 생활 2.0: 학위 과정 때 이걸 알았더라면" 주제로 기계공학과 세미나 (hosted by 김미소 교수)
- 2025-07-24 · 한국소성·가공학회, 전문교육 (제목: 실험/해석 데이터 부족 문제 해결을 위한 능동학습과 해석 가속화를 위한 연산자 학습), 한밭대
- 2025-07-21 · Prof. Sooyoung Lee gives a seminar at the Cho Chun Shik Graduate School of Mobility (hosted by Prof. In Gwun Jang)
- 2025-07-17–2025-07-18 · 한국소음진동공학회 산하 한국설비진단자격인증원 워크샵 (단양 소노벨)
- 2025-07-14–2025-07-16 · 대한기계학회 기계인공지능 연구회, 인공지능 여름학교, 아주대 (조기 마감)
- 2025-07-07–2025-07-11 · Prof. Seungchul Lee organizes "Theme Area T14: AI Applications for Sound and Vibration and Condition Monitoring" as a theme co-chair at the 31st International Congress on Sound and Vibration (ICSV31), Incheon, Korea
- 2025-07-03–2025-07-04 · 대한기계학회 CAE및응용역학 부문, 'CAE 및 응용역학을 위한 인공지능' 여름 강습회, 건국대 (141명 조기마감)
- 2025-06-30–2025-07-01 · 대한금속·재료학회 인공지능재료과학 분과, 제11회 재료인공지능 여름학교 진행 (국민대, 164명 참가)
- 2025-06-24 · Prof. Dong-Gyu Ahn from Chosun University gives a seminar entitled "Remanufacturing of Mechanical Parts using Additive Manufacturing Technology." (hosted by Prof. Young-Jin Kim)
- 2025-06-23–2025-08-22 · iAI member Jaejung Park is working as a visiting researcher in Prof. Kyoungmin Min's lab at Yonsei University.
- 2025-06-20 · 이승철 교수, 대한기계학회 교육부문에서 'Developing an e-Book for "AI for Mechanical Engineering" Course Using ChatGPT: A Case Study' 발표 (서울시립대학교)
- 2025-06-18 · Jaejun Lee (iAI M.S. alumnus) visits the iAI lab to give a seminar.
- 2025-06-17–2025-06-21 · International Symposium on Middle Ear Mechanics in Research and Otology (MEMRO 2025) at Leuven, Belgium
- 2025-06-17 · Chaeyun Won successfully completes her master's thesis defense. Congrats !!!
- 2025-06-12 · 이승철 교수, 국민대학교 신소재공학부에서 '인공지능 관점에서 바라본 재료과학 연구'세미나 진행
- 2025-06-12 · 이승철 교수, 대한기계학회 가상제품개발연구회 심포지엄에서 "제품 가상화 설계를 위한 물리지식기반 인공지능의 역할" 발표
- 2025-06-05 · 이승철 교수, 중앙대학교 기계공학부에서 '인공지능 관점에서 바라본 기계공학 연구'세미나 진행
- 2025-05-30 · 숙명여자대학교 김윤영 석좌교수님, '김교수가 들려주는 슬기로운 대학원 생활' 주제로 세미나 (This seminar is hosted by Prof. Seunghwa Ryu).
- 2025-05-27 · Prof. Jonghyun Park from Missouri University of Science and Technology gives a seminar entitled "Converging Materials Science, Advanced Manufacturing, and Management for Lithium-ion Batteries." This seminar is hosted by Prof. Yoon Koo Lee.
- 2025-05-21–2025-05-23 · 한국소음진동공학회 춘계학술대회 참가 (제주)
- 2025-05-16 · 김일적, 정일주, 허현석, 김태완 박사 졸업생, 연구실 방문 및 선후배 간담회
- 2025-05-15 · 김규원 석사 졸업생 (25년 9월 미국 조지아텍 박사과정 입학 예정), 연구실 방문 및 세미나
- 2025-05-10 · 한국설비진단자격인증원 자격인증시험, KAIST 창의학습관
- 2025-04-23–2025-04-25 · 한국트라이볼로지학회 춘계학술대회 (영주)
- 2025-04-23–2025-04-25 · 대한금속·재료학회 춘계학술대회 참가 (제주)
- 2025-04-16–2025-04-19 · 대한기계학회 CAE 및 응용역학 부문 춘계학술대회 참가 (제주)
- 2025-04-11 · 2025년 NOVIC+ 센터 신입생 환영회
- 2025-04-09–2025-04-11 · 대한기계학회 신뢰성 부문 춘계학술대회 (경주 코오롱 호텔)
- 2025-04-06–2025-04-11 · 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2025) at Hyderabad, India
- 2025-03-28 · 이승철 교수, 국가과학기술연구회 글로벌 TOP 전략연구단 책임자문위원 위촉
- 2025-03-20–2025-03-21 · 이승철 교수, 한국설비진단자격인증원 설비진단기술강습회 참가 (대전)
- 2025-03-13 · 신승민 졸업생, LG전자 생산기술원 타겟랩 활동으로 연구실 방문
- 2025-03-07 · Dr. Moon-Jo Kim from KITECH gives a seminar entitled "Two Novel Approaches for Enhancing Aluminum Casting Process: Electric Current and Artificial Intelligence" (hosted by Prof. Seungchul Lee)
- 2025-03-05 · KAIST 기계공학과 진입생 오리엔테이션과 학사과정 개강파티
- 2025-02-28 · 이승철 교수, KAIST-LG이노텍 산학협력 교류회 참석 (대전, KAIST)
- 2025-02-27 · Dr. Sunghee Yun, Co-founder and CTO of Erudio Bio, Inc., visits KAIST.
- 2025-02-26 · 이승철 교수, 대한기계학회 제1차 기계산업혁신포럼 '다가오는 양자시대, 양자기술과 기계공학의 접점' 행사 참가 (서울)
- 2025-02-17–2025-02-19 · 대한금속·재료학회 인공지능재료과학 분과, 제10회 재료인공지능 겨울학교를 고려대학교에서 진행 (108명 참가)
- 2025-02-13 · 이승철 교수, 국립한밭대학교 반도체 전공트랙 학생 대상 '능동 학습 (Active Learning)' 강의
- 2025-02-11 · 대한기계학회 기계인공지능 연구회와 포항공대 수리 데이터과학 연구소, Scientific Machine Learning Workshop 개최 (포스코 센터, 224명 참가)
- 2025-02-10–2025-02-12 · 카이스트 기계공학과, 'AI 기반 설계: 해석에서 설계 최적화까지' 동계 산학협동 강좌, 대전 (63명 참가)
- 2025-02-06 · 이승철 교수, 대한기계학회 AI융합교육(소)위원회 참가 (서울)
- 2025-02-06 · 연구 성과 홍보: 티타늄 3D프린팅 최적의 공정조건 AI가 찾아준다
- 2025-02-05–2025-02-07 · iAI attends the 2025 Nature Conference 'Materials for AI, AI for Materials' at KAIST
- 2025-02-04 · 이승철 교수: 국립금오공과대학교 기계시스템공학부 세미나 (invited by 손정우 교수)
- 2025-01-24 · 이승철 교수, 한국소음진동공학회 2025년도 신년교례회 참석 (서울)
- 2025-01-20–2025-01-22 · 대한기계학회 기계인공지능 연구회에서 주관하는 고급인공지능 강습회, 전북대 (132명 참가)
- 2025-01-18–2025-01-19 · 대한기계학회 기계인공지능 연구회 이사회(겸 신년회), 서울
- 2025-01-17 · 이승철 교수, 한국과학기술연구원 (KIST) 계산과학연구센터에서 세미나 진행 (서울)
- 2025-01-09–2025-01-10 · 이승철 교수, 대한금속·재료학회 전산재료과학분과 동계 촉매 심포지엄 참석 (대전, 한밭대)
- 2024-12-18 · 이종목 학생, '상호연동 모듈형 허리, 어깨, 무릎 근력보조 엑소수트 기술 개발' 과제 최종 평가에서 인공지능 기반 임무모션 판별 시연
- 2024-12-18 · K-MDS 사용자 클럽 통합 워크숍 & 인공지능 기술 워크숍, 대전
- 2024-12-17 · 이승철 교수, 한국건설기술연구원에서 '물리지식기반 인공지능' 세미나 진행
- 2024-12-06 · 경북대학교 경북대 미래형자동차기술융합혁신인재양성사업단에서 세미나 진행 (경북대 최상헌 교수 초청).
- 2024-12-06 · 이세빈 학생, 한국기계기술단체총연합회에서 우수논문상 수상
- 2024-12-03–2024-12-06 · iAI lab attends the 7th International Conference on Materials and Reliability (ICMR-2024) at Busan, Korea.
- 2024-11-24–2024-11-27 · iAI lab attends the 8th International Conference on Electronic Materials and Nanotechnology for Green Environment (ENGE 2024) at Jeju, Korea.
- 2024-11-21–2024-11-22 · 이승철 교수, 한국전산구조공학회 학술심포지엄 참가 (전주 전북대학교 국제컨벤션센터)
- 2024-11-13–2024-11-15 · 산업 인공지능 연구실, 한국정밀공학회 추계학술대회 참가 (경주 화백컨벤션센터)
- 2024-11-12 · HD현대사이트솔루션의 이동욱 대표님을 모시고 '쇠에 인공지능을 더하다' 주제로 기계공학과 세미나 진행
- 2024-11-09 · 한국설비진단자격인증원 자격인증시험, 충남대
- 2024-11-06–2024-11-08 · 산업 인공지능 연구실, 대한기계학회 본부학술대회 참가 (제주국제컨벤션센터)
- 2024-11-04 · Dr. Sunghee Yun gives a seminar titled "AI: Technology, Industry, Market & Hardware." (hosted by Prof. Seungchul Lee)
- 2024-11-01 · 이승철 교수, 대한외과학회에서 'Evolution of Medical Cognitive Intelligence: Future Changes Driven by Multimodal AI' 발표
- 2024-10-31 · 이승철 교수, 한국생산기술연구원 지능화뿌리기술연구소에서 '산업 인공지능' 주제로 세미나 진행 (온라인).
- 2024-10-29 · 연구 성과 홍보: 꿈의 신소재, '맥신' 안정성 판단 AI 개발...중앙대-KAIST, 열역학적 안정성 판단 효율 100배 높여
- 2024-10-28–2024-10-30 · 산업 인공지능 연구실, 대한금속재료학회 추계학술대회 참가 (알펜시아 리조트 평창)
- 2024-10-23–2024-10-25 · 산업 인공지능 연구실, 한국소음진동공학회 추계학술대회 참가 (하이원 리조트 정선)
- 2024-10-21–2024-10-22 · 이승철 교수, DN Solutions 기술전략워크샵에서 "형상 변화를 반영할 수 있는 물리지식기반 인공지능: 계산 가속화 관점에서" 주제로 발표 (창원)
- 2024-10-17 · 이승철 교수, 한국소성가공학회 추계학술대회에서 "공학적 사로로 풀어보는 인공지능 활용 길라잡이" 주제로 기조강연 (제주 신화월드)
- 2024-10-15 · 이승철 교수, 카이스트 기계공학과 도시락 세미나에서 발표.
- 2024-09-27 · 산업 인공지능 연구실, 기계공학과 연구실 소개 행사 참가.
- 2024-09-12 · 2024 소재 기술 지능화/자동화 워크샵, 서울대
- 2024-09-11 · 이승철 교수, 전북대 건지리버럴아츠 강의에서 '인공지능의 현재와 미래' 주제로 강연
- 2024-09-06 · 이승철 교수, 대한기계학회 신뢰성부문 & 재료및파괴부문 2024년 산·학·연 협동 세미나 "미래 자동차 기술의 내구/신뢰성" 참가 (서울 포스코타워 역삼)
- 2024-09-05 · 이승철 교수, 소재R&D분야 AI 활용 및 관련 과제 워크숍에 참가 (대전 ICC 호텔)
- 2024-09-03 · 이승철 교수, 한국기계연구원에서 '기계공학 문제 해결을 위한 인공지능' 강연
- 2024-08-30 · 박범수 박사, 2024년 박사후국내연수사업에 "물리 지식을 활용한 생성형 인공지능 기반 기계 시스템 해석 경량화 및 설계기술 개발" 주제로 선정. 축하합니다.
- 2024-08-26–2024-08-30 · iAI lab attends the 26th International Congress of Theoretical and Applied Mechanics (ICTAM2024) at Daegu, Korea.
- 2024-08-22–2024-08-23 · 한국최적설계학회 24년도 하계 강습회, 한국과학기술원
- 2024-08-14 · iAI gives a one-day tutorial on PINN and DeepONet to Hankook Tire & Technology.
- 2024-08-12 · 대한기계학회 기계인공지능 연구회, 중앙대학교에서 '기계인공지능 신진연구자 심포지엄' 개최
- 2024-08-08–2024-08-09 · 한국설비진단자격인증원 워크샵, 포항
- 2024-08-07 · 34 students from Zhejiang University in China visit the iAI Lab and the KAIST ME Department.
- 2024-07-29–2024-08-01 · Prof. Sung-Ho Hong gives a poster presentation entitled "Proposal of a New Method for Measuring Wear Scars Using Deep Learning (Sebin Lee, Taewan Kim, Seungchul Lee, Sung-Ho Hong)" at The 7th International Conference on Material Strength and Applied Mechanics (MSAM 2024), Győr, Hungary.
- 2024-07-25 · 이수영 교수, 박범수 박사, 박재정 학생이 한국소성∙ 가공학회 전문교육을 '소성가공 분야 예시를 통한 능동 학습과 물리지식기반 인공지능 소개'주제로 진행
- 2024-07-22–2024-07-26 · Prof. Seungchul Lee attends the 16th World Congress on Computational Mechanics (WCCM) at Vancouver, British Columbia, Canada.
- 2024-07-15–2024-07-19 · Prof. Seungchul Lee visits the University of Michigan, Dearborn for research collaboration.
- 2024-07-10–2024-07-12 · 대한기계학회 기계인공지능 연구회, 숙명여자대학교에서 '고급 기계인공지능 강습회' 개최
- 2024-07-09 · 이승철 교수, 2024 KAIST-LG H&A본부 Future Webinar에 '디지털 트윈 계산 가속화를 위한 물리지식기반 인공지능' 발표
- 2024-07-03–2024-07-05 · 대한금속재료학회 인공지능재료과학 분과, 대학원생 대상 '고급 재료인공지능 여름학교'를 한국과학기술원에서 개최
- 2024-07-01–2024-07-03 · 대한금속재료학회 인공지능재료과학 분과, 대학생 대상 '기초 재료인공지능 여름학교'를 한국과학기술원에서 개최
- 2024-06-24 · iAI students successfully complete their doctoral dissertation defense. Congrats !!!
- 2024-06-21 · 이승철 교수, 한국트라이볼로지학회와 경북 지역에너지 클러스터 인재 양성 사업이 공동 주최하는 산학 강좌에서 '인공지능을 활용한 풍력 터빈 상태진단 소개' 강연 (경주 힐튼 호텔)
- 2024-06-20 · 이승철 교수, 대한기계학회 교육부문 춘계학술대회에서 '기계공학자를 위한 인공지능 교육과 기계인공지능 연구회 사례 소개' 발표 (소노문 단양)
- 2024-06-19 · 이승철 교수, 'AI 자율제조' 행사 참가
- 2024-06-03 · Lecture series in 'AI in ME'
- 2024-05-29–2024-05-31 · 한국음향학회 춘계학술대회 참가, 제주 부영호텔&리조트
- 2024-05-22–2024-05-24 · 한국소음진동공학회 춘계학술대회, 제주 라마다 호텔
- 2024-05-16 · 이승철 교수, 육군미래혁신연구센터에서 강연.
- 2024-05-15 · The course titled "AI for Mechanical Engineering" is now open
- 2024-05-11 · 한국설비진단자격인증원 자격인증시험, KAIST 창의학습관
- 2024-05-09 · 대구과학고등학교 35기 학생, 카이스트 방문
- 2024-05-08 · 이승철 교수, 2024학년도 봄학기 기계공학과 새내기 세미나에서 "기계에서도 인공지능을 한다고?" 주제로 강연
- 2024-05-01–2024-05-03 · 대한기계학회 CAE및응용역학부문 춘계학술대회, 제주 휘닉스 섭지코지
- 2024-04-24–2024-04-26 · 이승철 교수, 대한금속재료학회 춘계학술대회 참가 (창원 컨벤션센터)
- 2024-04-19 · 이세빈 학생, '딥러닝을 활용한 마모흔 측정 기반의 마모량 평가' 연구로 한국트라이볼로지학회 제75회 춘계학술대회에서 최우수 논문상 수상
- 2024-04-17–2024-04-19 · 한국전산구조공학회 정기학술대회, 제주 신화월드
- 2024-04-12 · 연구실 석사 졸업생 이재준 군이 "성공적인 박사 유학 전략" 주제로 세미나 진행
- 2024-04-09 · iAI lab members enjoy cherry blossoms on the KAIST campus
- 2024-04-08 · 2024년 NOVIC+ 센터 신입생 환영회
- 2024-04-01 · 산업인공지능 연구실 의료인공지능 팀, 서울성모병원의 김도현 교수님 팀과 협업 회의 진행
- 2024-03-29 · 이승철 교수, 연세대학교 기계공학과 대학원 세미나에서 "디지털 전환을 위한 필요조건: 인공지능 기반 시뮬레이션 계산 가속화" 발표 (hosted by 이창훈 교수)
- 2024-03-28 · 중앙대 이수영 교수, 기계로봇연구정보센터 홈페이지에 신진연구자 인터뷰 소개
- 2024-03-26 · 이승철 교수, 경희대학교 우주과학과 콜로키움에서 "물리지식기반 인공지능의 최신 연구동향과 과학 및 공학에서의 적용사례" 발표 (hosted by 문용재 교수)
- 2024-03-26 · 이승철 교수, 한국철도기술연구원에서 "디지털 전환을 위한 필요조건: 인공지능 기반 시뮬레이션 계산 가속화" 발표 (hosted by 고효인 박사)
- 2024-03-21–2024-03-22 · 한국설비진단자격인증원 2024 설비진단기술강습회, 대전 선샤인호텔
- 2024-03-20–2024-03-22 · 대한기계학회 신뢰성부문 2024년 춘계학술대회, 여수 소노캄
- 2024-03-19 · 한국전기연구원 김남균 원장님께서 '전기화와 우리의 대응' 주제로 KAIST 기계공학과 정기세미나 강연.
- 2024-02-29 · 이승철 교수, 전산유체공학회 AI CFD 연구회 미니 워크샵 참석 (서강대).
- 2024-02-23 · 강릉원주대학교 박찬일 교수님 연구실로부터 회전체 장비 이전
- 2024-02-22 · 이승철 교수, K-MDS 사용자 클럽 통합 워크숍 및 제2회 소재 연구데이터 활용 인공지능 기술 워크숍에 참석 (대전 KW 컨벤션 3층 컨벤션홀).
- 2024-02-19–2024-02-21 · KAIST 기계공학과, "인공지능과 설계: 해석 예측에서 설계 최적화까지" 산학협동 강좌 개최 (104명 참가).
- 2024-02-16 · 이승철 교수, DN솔루션즈 New Learn 세미나에 '제조업 AI 활용방안 및 기술동향 파악' 주제로 강연 (현장 150명 + 온라인 70명).
- 2024-02-15 · 이승철 교수, 한국전산구조공학회 신기술강습회 "물리지식기반 오퍼레이터 러닝과 모델축소를 이용한 구조해석 실습" 참가
- 2024-02-14 · Keonhyeok Park and Jongmok Lee successfully complete the Ph.D. proposal. Congratulations!
- 2024-02-06–2024-02-07 · Prof. Seungchul Lee visits Samsung Heavy Industries at Geoje for the SHI-KAIST Tech Forum.
- 2024-01-31–2024-02-01 · A Scientific Machine Learning Workshop is held at KAIST.
- 2024-01-30 · 이승철 교수, 국립금오공과대학교 기계설계공학과에 손정우 교수님 초청으로 세미나 "디지털 전환을 위한 필요조건: 인공지능 기반 시뮬레이션 계산 가속화" 진행
- 2024-01-29 · 캐드앤그래픽스 2024년 1월호에 '물리 지식 기반 인공지능 차수 축소 모델' 기고문
- 2024-01-25 · 이승철 교수, "거대 언어 모델 원리 및 ChatGPT 활용 기초" 주제로 한국통신학회 아이디어 경진대회 튜토리얼 강연 (invited by 신원용 교수).
- 2024-01-22–2024-01-24 · 기계인공지능연구회, 2024년 대학생 대상 인공지능 강습회를 숭실대학교에서 개최 (100명 참가).
- 2024-01-21 · 이수영 박사가 후배들에게 연구 관련해서 멘토링한 내용을 '(선배가 후배에게 알려주는) 슬기로운 대학원 생활' 제목으로 유튜브에 연재 시작
- 2024-01-19 · 3월 중앙대 기계공학과 임용예정인 이수영 박사가 "My Academic Journey from Graduate Student to Incoming Professor" 주제로 세미나 진행
- 2024-01-16 · 이승철 교수, 한국소음진동공학회 2024년도 신년교례회 참석
- 2024-01-16 · Dr. Bumsoo Park gives a lab tour to students from Dalian University of Technology, China.
- 2024-01-08 · iAI alumnus, Dr. Sooyoung Lee, will be joining the Department of Mechanical Engineering at Chung-Ang University as an Assistant Professor, starting from 03/01/24. Congratulations!
- 2023-12-27 · 'Deep learning acceleration of multiscale superresolution localization photoacoustic imaging' is selected as the ESI Highly Cited Paper in November 2023 in Light: Science & Applications (LSA).
- 2023-12-19 · 이승철 교수, 연세대 이차전지센터에서 주관하는 AI + 배터리 워크샵에서 '물리지식기반 배터리 용량/수명 예측' 발표.
- 2023-12-15 · 박건혁 학생, 한국비파괴검사학회에서 우수논문발표상 수상
- 2023-12-12 · Three iAI students successfully complete the master's thesis defense. Congratulations !!!
- 2023-12-08 · 이승철 교수, 제3차 실용인공지능학회 학술대회 (AAiCON2023) 에서 '물리지식기반 인공지능 소개와 응용' 주제로 전북대 임재혁 교수님과 함께 진행.
- 2023-12-02 · Prof. Seungchul Lee gives a plenary speech at the international conference on Emerging Technologies in Mechanical Engineering (ETME 2023) in Beijing, China.
- 2023-11-18 · 박재정 학생, 2023년 제 14차 한국조직공학·재생의학회 교육/신진연구자 통합 심포지엄에서 "Applications of Artificial Intelligence in Regenerative Medicine" 발표 (서울대병원 CJ홀, 제일제당홀).
- 2023-11-16 · The review paper titled "Recent Advances of Artificial Intelligence in Manufacturing Industrial Sectors: A Review," which was published in IJPEM, has been recognized with the IJPEM Award of 2023.
- 2023-11-10 · 이승철 교수, CAE 컨퍼런스에서 "산업현장에서의 AI 성공 전략과 물리지식기반 인공지능 차수축소모델" 발표.
- 2023-11-01 · 기계인공지능연구회, 대한기계학회 본부학술대회(송도컨벤시아)에서 'AI Impacts Across ME Domains' 특별세션 개최.
- 2023-10-31 · 정주영 창업경진대회 데모데이 2023, 앰버로드 최우수상 수상
- 2023-10-26 · 임언호, 박도겸 졸업생, 10월 디캠프 '앰버로드' 우승
- 2023-10-25–2023-10-27 · iAI lab attends the conference of the Korean Institute of Metals and Materials at Daegu, Korea.
- 2023-10-23 · 이승철 교수, POSCO 스마트기술 경진대회에서 "산업에서 성공하기 위한 인공지능 핵심기술" 초청 강연.
- 2023-10-23 · Taewan Kim successfully completes his doctoral dissertation defense. Congrats !!!
- 2023-10-20 · 이승철 교수, 서울대 기계공학과 역학 세미나에서 "디지털 전환을 위한 필요조건: 가상 데이터 생성과 시뮬레이션 계산 가속화" 강연.
- 2023-10-18–2023-10-20 · iAI lab attends the conference of the Korean Tribology Society at Gyeongju, Korea.
- 2023-10-13 · 이승철 교수, 다학제융합클러스터 4차 워크샵에서 "디지털 트윈의 가상 시나리오 계산 가속화를 위한 물리지식기반 인공지능 차수 축소 모델" 발표
- 2023-10-12 · 산업 인공지능 연구실 (김태완, 이종목, 신승민 학생 참여), 포스코홀딩스 AI연구소 산학과제가 2023 포스코그룹 AI DAY 에서 혁신상 대상 수상.
- 2023-10-11–2023-10-13 · iAI lab attends the KSNVE conference at Yeosu, Korea.
- 2023-09-22 · 이승철 교수, 국가 소재 데이터 스테이션 (K-MDS) '사용자 클럽 발기인 총회' 참석.
- 2023-09-21 · 이승철 교수, 한국소음진동공학회 임원진 한국항공우주연구원 방문.
- 2023-09-11–2023-09-14 · iAI members attend PHMAP 2023 (Asia Pacific Conference of the Prognostics and Health Management Society) at Tokyo, Japan.
- 2023-09-08 · 'AI시대의 기계공학의 위기와 기회 - 기계공학 교육의 역할' 기계산업혁신포럼에 참가.
- 2023-09-07–2023-09-08 · 대한기계학회 신뢰성부문 산학연 협동 세미나 개최.
- 2023-09-04–2023-09-08 · iAI attends the IEEE IUS 2023 (International Ultrasonic Symposium) at Montreal, Quebec, Canada.
- 2023-08-29 · 이승철 교수, 현대자동차 R&D 기술 포럼에서 "디지털 트윈의 가상 시나리오 계산 가속화를 위한 물리지식기반 인공지능 차수축소모델" 강연.
- 2023-08-28 · 연구 성과 홍보: 재료연-포항공대 공동연구팀, 통합된 미세조직 상 구분 프레임워크 개발.
- 2023-08-28 · iAI lab moves to KAIST.
- 2023-08-24 · 이승철 교수, 대한금속재료학회 하계기술강좌 (양재 aT센터) 에서 '산업에 성공하기 위한 인공지능 핵심 기술' 주제로 발표.
- 2023-08-23–2023-08-25 · 대한금속재료학회 인공지능재료과학분과, 2023 하계단기강좌 "머신러닝과 딥러닝의 기초 및 응용 (초급)" 를 부경대학교에서 진행.
- 2023-08-21–2023-08-23 · 한국자동차공학회, '자동차공학과 인공지능의 만남' 강습회를 인하대에서 진행.
- 2023-08-18 · 대한기계학회 기계인공지능연구회, '기계공학과 인공지능의 만남' 주제로 기계인공지능 심포지엄을 가천대에서 진행.
- 2023-08-16–2023-08-17 · 대한기계학회 기계인공지능연구회, '대학원생 대상 고급인공지능' 강습회를 숭실대에서 진행.
- 2023-08-09–2023-08-11 · 한국소음진동공학회 AI혁신위원회/한양대 LINC3.0사업단 공동 주관, '소음진동 AI와 미래모빌리티' 강습회를 한양대에서 진행 (조기 마감).
- 2023-08-08 · Iljeok Kim successfully completes his Ph.D. proposal. Congratulations!
- 2023-08-04 · '물리지식기반 인공지능' 주제로 포스코타워 역삼 이벤트홀에서 연구 교류회 진행 (조기 마감).
- 2023-07-31 · 이승철 교수, 제3회 KERI (한국전기연구원) 포럼에서 '산업 인공지능: 적용 방법과 사례' 주제로 발표.
- 2023-07-26 · SK on visits POSTECH iAI Lab.
- 2023-07-17 · Prof. Seungchul Lee gives a talk titled "Industrial AI with Domain Knowledge Augmented" at DGIST workshop.
- 2023-07-12 · 이승철 교수, 선린대학교 혁신교수법 워크샵에서 "인공지능의 이해와 ChatGPT 수업에 적용하기" 강연.
- 2023-07-04–2023-07-07 · Four students from Daegu Science High School visit the iAI lab as part of a research program for high school students.
- 2023-07-04 · Prof. Seungchul Lee gives a tutorial titled "Physics-informed Neural Networks with Data" at the 18th International Conference on Intelligent Autonomous Systems (IAS-18) in Suwon, Korea.
- 2023-06-26–2023-06-28 · iAI lab attends the 20th international conference on Ubiquitous Robots (UR 2023) at Honolulu, USA.
- 2023-06-21 · iAI lab provides a one-day tutorial to POSCO, focusing on case studies and hands-on coding.
- 2023-06-21–2023-06-22 · Apple Manufacturing R&D Accelerator is hosting the Smart Manufacturing Forum at Pohang, Korea.
- 2023-06-19–2023-08-25 · Four students are participating in the undergraduate research program during the summer break.
- 2023-06-19–2023-09-01 · iAI member (Jaejung Park) visits the POSTECH-CATHOLIC Biomedical Engineering Institute (PCBMI) as a visiting researcher.
- 2023-06-19 · 한국설비진단자격인증원 워크샵을 부산에서 진행.
- 2023-06-19 · 언론 홍보: 새로운 유형 불량도 척척 잡아… AI 만난 스마트팩토리 진화
- 2023-06-15 · KISTI (Korea Institute of Science and Technology Information) visits the iAI lab to discuss a virtual manufacturing platform.
- 2023-06-14 · Seungmin Shin successfully completes his master's thesis defense. Congrats !!!
- 2023-06-13 · Heekyu Kim successfully completes his master's thesis defense. Congrats !!!
- 2023-06-12 · Jihun Lee successfully completes his master's thesis defense. Congrats !!!
- 2023-06-12 · 언론 홍보: 셀로이드, 산자부 과제 선정... "세포치료제 첨단 생산 장비 개발" (기계 김동성, 이승철 교수)
- 2023-06-09 · 대한기계학회 포항지회, 산학연 기술교류회를 포항공대 국제관 대회의실에서 진행
- 2023-06-07 · 이승철 교수, 한국원자력연구원에서 "산업인공지능의 정의와 응용사례" 세미나 진행.
- 2023-06-01 · 이강산 졸업생이 LAB ZINE VOL.8 에 소개되었습니다.
- 2023-05-30 · 한국생산기술연구원 김병학 박사님을 모시고 '인공지능 객체 탐지/추적 및 다중 도메인 데이터 처리 기술' 세미나 진행.
- 2023-05-27 · Prof. Seungchul Lee gives an invited talk titled "AI and Big Data: Clinical Implication" at 2023 6th APCMS (Asia-Pacific CardioMetabolic Syndrome) Congress, Seoul, Korea.
- 2023-05-24–2023-05-26 · iAI lab attends the KSNVE conference at Samcheok, Korea.
- 2023-05-24 · HD Korea Shipbuilding & Offshore Engineering visits POSTECH iAI Lab.
- 2023-05-20 · Prof. Seungchul Lee gives an invited talk at the KSIAM (Korean Society for Industrial and Applied Mathematics) Spring Conference at Pyeongchang, Korea.
- 2023-05-18 · 이승철 교수, 대한기계학회 CAE및응용역학 부문 'CAE 및 응용역학 젊은연구자상' 수상.
- 2023-05-18 · 대한기계학회 CAE및응용역학 부문 산업인공지능 연구실 수상
- 2023-05-17–2023-05-19 · iAI lab attends the KSME conference of the CAE and Applied Mechanics division at Busan, Korea.
- 2023-05-16 · 한국생산기술연구원 홍영선 박사님을 모시고 'Life Cycle Management Technology to Vitalize the Future Mobility Ecosystem' 세미나 진행.
- 2023-05-09 · 대한기계학회 신뢰성 부문, 한국서부발전 디지털기술공유센터과 업무협약 체결.
- 2023-05-03 · Prof. George Em Karniadakis gives a seminar talk titled "From Physics-Informed Machine Learning to Physics-Informed Machine Intelligence: Quo Vadimus?" at the Department of Mathematics at POSTECH, hosted by Prof. Minseok Choi.
- 2023-05-02 · 한국생산기술연구원 이정훈 박사님을 모시고 '산업용 첨단 3D프린팅 기술 및 응용' 세미나 진행.
- 2023-05-02 · LG Energy Solution visits POSTECH iAI Lab.
- 2023-04-27 · 이종목 학생, 대한기계학회 IT 융합 부문 우수논문상 수상.
- 2023-04-26–2023-04-28 · iAI lab attends the conference of the Korean Institute of Metals and Materials at Jeju, Korea.
- 2023-04-21 · 알키미스트 과제 3단계 2차년도 1차 워크샵 참여 (이승철 교수, 박재정, 이세빈)
- 2023-04-21 · Prof. Seungchul Lee gives an invited talk titled "PINN-driven Surrogated Modeling to Accelerate Virtual Scenario Calculations in Digital Twins" at 2023 SoftWare Convergence Symposium (SWCS 2023) in Seoul.
- 2023-04-18 · 한국생산기술연구원 김건우 박사님을 모시고 'Cooling Textile' 세미나 진행.
- 2023-04-12 · Samsung Electronics' Foundry Business visits POSTECH iAI Lab.
- 2023-04-06–2023-07-27 · 산업 인공지능 연구실이 삼성중공업에 인공지능 핵심역량 향상 이론 및 실습 강의 진행. (1주일에 8시간)
- 2023-03-31 · LG Energy Solution visits POSTECH to discuss the future of battery manufacturing intelligence.
- 2023-03-30 · 이승철 교수, 포항공대 기계공학과 학과입문 수업에서 "기계도 똑똑해질 수 있을까?" 제목으로 강의.
- 2023-03-29 · Soo Young Lee successfully completes his doctoral dissertation defense. Congrats !!!
- 2023-03-28 · 한국생산기술연구원 송람 박사님을 모시고 '알루미늄 합금에 대한 연속주조 공정 및 최신 연구 동향 소개' 세미나 진행.
- 2023-03-27 · iAI lab members enjoy cherry blossoms on the POSTECH campus
- 2023-03-23 · 나주원 박사, 대한기계학회 신뢰성부문 우수학위논문상 수상.
- 2023-03-22–2023-03-24 · iAI lab attends the KSME conference of the Reliability Engineering division at Jeju, Korea.
- 2023-03-16–2023-03-17 · 2023 설비진단기술 강습회를 대전 호텔 선샤인에서 진행.
- 2023-03-15 · Prof. Seungchul Lee gives a seminar talk entitled "Industrial AI with Domain Knowledge Augmented" at the department of Computer Engineering, Gachon University.
- 2023-03-12 · 이승철 교수, HD현대일렉트릭-KAIST OPEN형 R&D 협약식 참석
- 2023-03-10 · Dr. Youngkyu Kim (KIST) presents a talk titled 'Physics-Informed Data Assimilation and Data-Driven Reduced Order Model for Digital Twin Applications' at the ME POSTECH seminar series, which is hosted by Prof. Seungchul Lee.
- 2023-03-08–2023-03-10 · iAI lab attends the 9th International Conference on Manufacturing, Machine Design and Tribology (ICMDT 2023) at Jeju, Korea.
- 2023-03-07 · 한국생산기술연구원 원홍인 박사님을 모시고 '압출 설비의 디지털 트윈 모델과 비전 기반 진동 모니터링 기술' 세미나 진행.
- 2023-02-28 · 한국생산기술연구원 박지용 박사님을 모시고 '4차 산업혁명시대, 3D 프린팅 기술' 세미나 진행.
- 2023-02-23 · 한국설비진단자격인증원 워크샵을 여수에서 진행.
- 2023-02-22 · 연구 성과 홍보: 모터 등 회전기기 결함 탐지하는 AI…"스마트팩토리에 활용"
- 2023-02-21 · 이승철 교수와 윤종필 박사, 포항공대-한국생산기술연구원 공동 세미나 수업 진행 (23년 1학기, 생산제조기술 및 시스템)
- 2023-02-21–2023-02-22 · 산업인공지능 연구실 (박건혁 학생), 한국산업응용수학회에서 주관하는 2023년 겨울 인공지능 튜토리얼 '그래프 신경망과 생성모델'에 참가.
- 2023-02-15–2023-02-17 · iAI lab attends the 18th Korea Robotics Society Annual Conference (KRoC 2023) at Pyeongchang, Korea.
- 2023-02-15–2023-02-17 · 산업인공지능 연구실 (박형식, 이세빈 학생), 대한금속재료학회 인공지능 재료과학분과 2023 동계단기강좌 '딥러닝 이론과 구현 (중급)' 에 참가
- 2023-02-14 · 연구 성과 홍보: '몸속 천둥번개' 딥러닝으로 더 빠르고 선명하게 혈관을 찍는다
- 2023-02-09–2023-02-10 · iAI lab attends the conference of society for Computational Design and Engineering (CDE) at Pyeongchang, Korea.
- 2023-01-30–2023-02-01 · 포항공대 기계공학과, LINC3.0 사업 일환으로 '산업체 재직자 대상 산업 인공지능 핵심 기초 교육' 을 경주 더케이호텔에서 진행.
- 2023-01-27 · 이승철 교수, 서울성모병원 순환기내과에서 '의료 인공지능 기초와 응용 사례' 세미나.
- 2023-01-20 · 산업인공지능 연구실 (이승철 교수, 박재정, 김희규, 이재준), '데이터 기반 소재 설계 및 탐색 기술' 관련 연구실과 교류회 진행.
- 2023-01-11–2023-01-13 · 대한기계학회 인공지능머신연구회, 2023년 기계공학 학부생을 위한 인공지능 강습회 주관 (신청서 및 행사 안내 홈페이지)
- 2023-01-10 · 산업인공지능 연구실 (이승철 교수, 김태완, 이종목, 신승민), 포항공대 수학과 최민석 교수님 연구실과 물리지식기반 인공지능 관련 연구 교류회 진행.
- 2023-01-05–2023-01-06 · 산업인공지능 연구실 (이승철 교수, 박재정, 김희규, 이재준), 대한금속재료학회에서 주관하는 '전산재료과학 촉매 심포지엄' 에 참가.
- 2022-12-26 · POSTECH-KAIST-KRISS Joint Workshop
- 2022-12-19 · 산업인공지능 연구실 석사 졸업생인 포스코 임언호 과장님께서 사내벤처 연계창업 프로그램을 통해 '앰버로드' 회사를 창업하셨습니다.
- 2022-12-16 · KAKAO ENTERPRISE AI REPORT 발간: 도메인 지식 기반의 AI 기술과 산업 현장 적용 (산업 인공지능 연구실 기고문)
- 2022-12-16 · 알키미스트 과제 3단계 3차 워크샵 참여 (이승철 교수, 이종목, 박재정, 이세빈)
- 2022-12-14 · 새내기연구참여 수업 시연행사
- 2022-12-13 · 이승철 교수, 포항공대 기계공학과 2022년 우수 강의 교수상 수상
- 2022-12-13 · 이수영 학생, 포항공대 기계공학과 2022년 대학원생 우수논문상 수상
- 2022-12-12 · Juwon Na successfully completes his doctoral dissertation defense. Congrats !!!
- 2022-12-12 · Two iAI students successfully defend the MS dissertation. Congrats !!!
- 2022-12-06 · 연구 성과 홍보: 음성 활용 AI로 흡인성 폐렴 위험 예측한다.
- 2022-12-02 · 이승철 교수, 한국소성가공학회에서 '재료 설계를 위한 인공지능 기초' 전문교육을 제주도에서 진행.
- 2022-12-01 · Soo Young's collaborative work is featured as the back cover of Advanced Science.
- 2022-11-28 · 이승철 교수, 한국생산기술연구원 뿌리기술연구소 자문회의 참가.
- 2022-11-19 · 대한신경외과학회 대한디지털융합신경외과연구회 제2차학술대회
- 2022-11-19 · 이승철 교수, 한국심초음파학회 AI 연구회 동계 심포지움에서 'AI and Cardiovascular Medicine: Engineer's Perspective' 주제로 연세대 세브란스 병원에서 세미나 발표.
- 2022-11-18 · 이승철 교수, 중앙대학교 광명병원에서 '사례 중심으로 고찰해 본 의료 인공지능' 주제로 세미나 발표.
- 2022-11-18 · 이승철 교수, '기계상태진단 개론' 공저자로 출판 (책임저자: 동국대 WISE캠 홍성호 교수).
- 2022-11-16 · Taewan Kim took second place in the Asia - East and Oceania - Student Category of the steelChallenge-17
- 2022-11-09 · 대한기계학회 인공지능머신연구회에서 본부학술대회 기간에 특별세션 + AI Party + 홍보 부스
- 2022-11-09–2022-11-11 · iAI attends the KSME conference at Jeju, Korea.
- 2022-11-03 · 이승철 교수, 2022년 한국소음진동공학회 AI혁신위원회 회장으로서 감사패 수상
- 2022-11-03 · 이승철 교수, 2022년 글로벌 핵심인재 양성지원사업 우수성과 대상 수상 (포스터)
- 2022-11-02 · 이승철 교수, '2022년 기계의 날' 산학연 협력 유공자 산업통산자원부 장관 표창 수상
- 2022-11-02–2022-11-04 · iAI attends the KSNVE conference at Jeju, Korea.
- 2022-10-27 · 이승철 교수, 한국PHM학회 제1회 PHM 산업 사례 심포지엄에서 "Key to the Success of Industrial AI: Physics-informed Neural Networks" 발표
- 2022-10-26 · 이승철 교수, 포항공대 인공지능 최고경영자과정에서 '산업에서 성공하기 위한 인공지능 핵심기술' 주제로 강연.
- 2022-10-24–2022-10-28 · iAI attends the ICA 2022 (International Congress on Acoustics) conference at Gyeongju, Korea.
- 2022-10-24 · 이승철 교수는 성균관대학교에서 세미나 진행 (Industrial AI: Physics-informed AI and Data-driven Inverse Design)
- 2022-10-19 · Prof. Kornel F. Ehmann gives a ME seminar talk entitled "Hybrid Multi-scale Manufacturing Processes and Systems." (hosted by Prof. Dongwoo Cho)
- 2022-10-11–2022-10-21 · 산업인공지능 연구실은 포항공대 인공지능연구원 인공지능 교육 프로그램 중, 현대제철 재직자분들에게 '인공지능 기초'를 2주간 교육
- 2022-10-05 · 이승철 교수는 "AI 응용 및 적용사례" 제목으로 포항공과대학교 직원 대상 AI 특강 진행.
- 2022-09-29 · Prof. Seungchul Lee gives an invited talk entitled "Physics-informed AI and its Applications" at 2022 Korea Supercomputing Conference.
- 2022-09-28 · 이승철 교수는 "인공지능과 공존하는 삶" 제목으로 전북대학교 건지리버럴아츠 특강 진행.
- 2022-09-27 · 전북대학교 임재혁 교수님, 포항 방문 및 '생성모델, 역설계기법, PINN을 이용한 항공우주분야 연구주제의 최신해결사례' 세미나 발표 (hosted by 이승철 교수)
- 2022-09-26–2022-09-29 · iAI (Jongmok Lee, Taewan Kim, Dogyeom Park, and Seungmin Shin) attends the APMS 2022 conference (Advances in Production Management Systems) at Gyeongju, Korea.
- 2022-09-23 · 이승철 교수는 "Industrial AI: Physics-informed AI and Inverse Design" 제목으로 서울과학기술대학교에서 세미나 진행.
- 2022-09-22 · 알키미스트 과제 3단계 2차 워크샵 참여 (이승철 교수, 이종목, 박재정, 이세빈)
- 2022-09-21 · SpaceX에 송영준 박사, "우주 산업과 레이터" 제목으로 포항공대 기계공학과 세미나 강연 (hosted by 이승철 교수)
- 2022-09-20 · 황윤섭, 이남정 졸업생이 포항에 방문
- 2022-09-19–2022-09-22 · iAI (Prof. Seungchul Lee) attends the Interspeech 2022 conference at Incheon, Korea.
- 2022-09-19 · 우선희 졸업생이 포항에 방문하여 세미나 진행
- 2022-09-16 · 이승철 교수, 푸드테크 기반 외식산업 혁신 생태계 조성을 위한 업무협약식 참석 (경상북도청)
- 2022-09-07 · Prof. Seungchul Lee gives an invited talk entitled "Physics-informed AI for CAE" at Tech Forum of Hyundai Motor Company, hosed by 전동화음향진동리서치랩.
- 2022-09-06 · 이승철 교수 인터뷰, "만능 아닌 AI, 한계 넘으려면 ‘물리 이론’ 강화해야"
- 2022-09-03 · 이승철 교수, 심장대사증후군 학회에서 "AI and Cardiovascular Medicine" 주제로 발표.
- 2022-08-23 · 이승철 교수는 "Industrial AI: Physics-informed AI and Inverse Design" 제목으로 한양대학교에서 세미나 진행 (Hosted by 소홍윤 교수님).
- 2022-08-22 · 이승철 교수, 서울대학교 재료공학부에서 주최하는 "재료설계 및 재료공정 분야에 데이터사이언스의 응용" 세미나에 "Data-driven Materials Science: Microstructure Image Enhancement, Inverse Design, Equation Discovery" 제목으로 발표.
- 2022-08-18–2022-08-19 · 산업인공지능 연구실 (이승철 교수, 이수영, 김태완, 박재정), '기구 위상 자율설계' 강습회에 참가
- 2022-08-17 · 산업인공지능 연구실, '유한요소해석과 최적설계 기초' 강습회에 참가
- 2022-08-09–2022-08-10 · 한국소음진동공학회 AI혁신위원회에서 소음진동을 위한 인공지능 강습회를 연세대학교에서 개최.
- 2022-08-08 · 한국소음진동학회 미래융합부문위원회/AI혁신위원회 공동주관으로 '인공지능으로 소리를 보다' 주제로 연세대학교에서 세미나 개최.
- 2022-08-04–2022-08-05 · 대한기계학회 인공지능머신연구회에서 2022년 인공지능 여름학교를 경북대학교에서 대면으로 개최.
- 2022-07-21 · 정해동 박사가 포항에 방문하여 세미나 진행
- 2022-07-13 · 대한기계학회 신뢰성부문 산학연 협동 세미나 '미래 모빌리티와 신뢰성' 을 중앙대학교에서 개최.
- 2022-07-04–2022-08-26 · iAI members (Taewan Kim, Seungmin Shin, and Jongmok Lee) work at POSCO N.EX.T Hub as a visiting researcher.
- 2022-07-04–2022-07-06 · 대한기계학회 인공지능머신연구회에서 2022년 고급인공지능 강습회를 광주과학기술원에서 대면으로 개최.
- 2022-06-30–2022-07-01 · Prof. Seungchul Lee attends the conference of the PHM Korea 2022 at Seoul, Korea.
- 2022-06-29 · Prof. Seungchul Lee gives an invited talk entitled "Physics-informed AI and Data-driven Inverse Design" at Samsung Advanced Institute of Technology (SAIT).
- 2022-06-22–2022-09-02 · iAI member (Jihun Lee) works at the Korea Research Institute of Standards and Science (KRISS) as a visiting researcher.
- 2022-06-17 · Jeongsan Kim successfully completes his M.S. dissertation defense on "Attention-based Explainable Feature Extraction Model for Anomaly Detection in Gearbox." Congrats !!!
- 2022-06-13 · 연구 성과 홍보: 물리 이론 학습하는 인공지능 탄생, 응용문제도 '척척'
- 2022-06-12 · Prof. Seungchul Lee gives an invited talk entitled "AI Applications in Healthcare" at the conference of the Korean Association of Stem Cell & Tissue Regeneration.
- 2022-05-31 · Sung Wook Kim successfully completes his doctoral dissertation defense on "Battery Health Management Through Physics-Informed Neural Networks: Thermal Runaway Modeling and Capacity Estimation." Congrats !!!
- 2022-05-26 · 이종목 학생이 대한기계학회 IT융합 부문 우수논문상을 수상.
- 2022-05-25–2022-05-27 · iAI attends the KSNVE conference at Changwon, Korea.
- 2022-05-19 · 김규원 학생이 대한기계학회 CAE 및 응용역학 부문 우수학위논문상을 수상.
- 2022-05-19–2022-05-20 · iAI attends the KSME conference of the CAE and Applied Mechanics division at Busan, Korea.
- 2022-05-17 · 연구 성과 홍보: 물리식 접한 AI, 배터리 용량 예측 향상시킨다.
- 2022-05-16 · 연구 성과 홍보: 인공지능 광음향기술로 고속, 고해상도 혈관영상 찍는다.
- 2022-05-04 · 이수영 학생, 대학원혁신 및 기계공학과4단계 BK21 사업 미래기계기술 프론티어 리더 양성 교육연구단에서 2022년 혁신 포스테키안 펠로우십에 선정.
- 2022-04-29 · Juwon Na attends the conference of the Korean Institute of Metals and Materials, Changwon, Korea.
- 2022-04-29 · 산업인공지능 연구실이 무은재 학부생을 위한 '3시간 만에 로봇 만들기' 행사 진행.
- 2022-04-27 · Graphical abstract: physics-informed AI for lithium-ion batteries (물리식을 만난 AI, 배터리 잔존수명 예측 정확도 및 강건성을 향상시키다)
- 2022-04-21 · Prof. Seungchul Lee attends the conference of the Korean Tribology Society at Jeju, Korea.
- 2022-04-20 · 이승철 교수, 2022년 ICT 기술사업화 페스티벌에서 정보통신기획평가원 원장상 수상.
- 2022-04-13–2022-07-13 · 산업 인공지능 연구실이 삼성중공업에 인공지능 핵심역량 향상 이론 및 실습 강의 진행. (1주일에 8시간)
- 2022-04-08 · Dr. Sunghee Yun from Gauss Labs gives a POSTECH ME seminar talk entitled "Time-series learning and its applications in manufacturing." (hosted by Prof. Seungchul Lee)
- 2022-04-05 · The official website for the Apple Manufacturing R&D Accelerator has been launched.
- 2022-03-30 · 이승철 교수는 "4차 산업혁명 시대! 인공지능 기술이 산업을 지배한다" 제목으로 전북대학교 건지리버럴아츠 특강 진행.
- 2022-03-29 · 이승철 교수는 카카오엔터프라이즈에 연구실 소개 세미나 진행. (카카오엔터프라이즈 소개 영상)
- 2022-03-24 · Graphical abstract for physics-informed AI (물리도 배우는 AI, 디지털 트윈의 핵심이 되다.)
- 2022-03-24 · 이승철 교수, 대한기계학회 신뢰학술상 수상.
- 2022-03-23–2022-03-25 · iAI attends the KSME conference of the reliability engineering division at Jeju, Korea.
- 2022-03-21–2022-03-22 · Prof. Seungchul Lee gives a seminar entitled 'Key to the Success of Industrial AI' to Hyundai Steel at Pohang.
- 2022-03-07 · iAI member (Iljeok Kim) works at the Korea Institute of Industrial Technology (KITECH) as a visiting researcher.
- 2022-03-01 · 이승철 교수는 카카오엔터프라이즈 자문위원 (AI Fellow) 로 위촉
- 2022-02-25 · 포스텍-가톨릭대 의생명공학연구원 공동연구지원사업 발표회
- 2022-02-25 · 한국소음진동학회 미래융합부문위원회/AI혁신위원회 공동주관으로 '인공지능으로 소리를 보다' 주제로 포항공대에서 세미나 개최 (postponed due to COVID-19)
- 2022-02-22 · 포항공대-한국생산기술연구원 공동 세미나 수업 개최 (22년 1학기, 생산제조기술 및 시스템)
- 2022-02-21–2022-02-23 · 대한기계학회 인공지능머신연구회에서 2022년 인공지능 겨울학교를 카이스트에서 진행합니다.
- 2022-02-16 · 서울대학교 기계공학부 김윤영 교수님의 [대학원생을 위한 연구입문 가이드]를 소개합니다.
- 2022-02-15 · 산업인공지능 연구실, 강습회 성공개최로 한국설비진단자격인증원 감사패 받아.
- 2022-02-07 · 카카오엔터프라이즈 김세웅 상무님을 모시고 "AI 기술의 비즈니스 응용" 주제로 세미나 진행
- 2022-01-25 · 나주원 학생이 포항공과대학교 기계공학과와 미래기계기술 프론티어 리더 양성 교육연구단에서 2021년 대학원생 우수논문상 수상하였습니다.
- 2022-01-22–2022-01-27 · Gyuwon Kim attends the International Society for Optics and Photonics (SPIE) Photonics West 2022 (online) and present an oral presentation, "Deep Learning Enables Accelerated Optical Coherence Tomography Angiography."
- 2022-01-19–2022-01-21 · 대한기계학회 인공지능머신연구회에서 2022년 고급인공지능 강습회를 포항공대에서 대면으로 진행합니다. (강습회 강의 자료)
- 2022-01-18 · 주)비케이비젼에 최수용 이사님께서 '산업현장의 진동진단 기술 분야 소개 및 진단 사례 연구' 주제로 포항공대에서 세미나 진행
- 2022-01-17 · iAI member (Hyunsuk Huh) works at the Korea Institute of Machinery & Materials (KIMM) as a visiting researcher.
- 2022-01-03–2022-02-07 · 학부생 겨울방학 연구참여
- 2021-12-29 · KRISS-POSTECH Joint Workshop
- 2021-12-13 · 새내기연구참여 수업 시연행사
- 2021-12-10 · Prof. Seungchul Lee gives a talk entitled "AI Meets Physics: Physics-informed NN and Data-driven Scientific Discovery" at the Symposium on AI for Mechanical Engineering, GIST. [YouTube]
- 2021-12-08 · 이승철 교수는 한국트라이볼로지학회 산학강좌에서 "인공지능 기반 상태감시 및 진단에 대한 고찰" 제목으로 세미나 발표.
- 2021-12-06 · 이수영 학생은 글로벌 핵심인재 양성지원 사업 우수성과 공모전에 대상 수상.
- 2021-12-02–2021-12-03 · 동국대 홍성호 교수님과 이승철 교수가 2021년도 설비진단기술강습회를 준비합니다.
- 2021-12 · Two iAI students successfully defend the MS dissertation. Congrats !!!
- 2021-11-25 · 이승철 교수는 2021년도 한국소음진동공학회 'KTM테크놀로지(주) 학술상' 을 수상
- 2021-11-25 · 이수영 학생은 2021년도 한국소음진동공학회 학생우수발표상을 수상
- 2021-11-24–2021-11-26 · iAI attends the KSNVE conference at Jeju, Korea.
- 2021-11-19 · 이승철 교수는 경북지역 에너지 클러스터 인재양성 사업 단기강좌에 "딥러닝 기반 풍력터빈 기어박스 상태 진단" 을 경주에서 발표.
- 2021-11-17 · Prof. Hyungmin Jun from Jeonbuk National University gives a talk entitled "Self-assembled DNA Nanomaterials with Designable Structures and Functions" at POSTECH ME seminar (hosted by Prof. Seungchul Lee)
- 2021-11-12 · Prof. Seungchul Lee gives a talk entitled "AI Meets Physics vs. Physics Meets AI" at RIST (Research Institute of Industrial Science & Technology), Pohang.
- 2021-11-08 · 이승철 교수는 '산업 인공지능과 영상기반 작업자 인지 기술' 제목으로 한국생산기술연구원 대경지역 첨단메카트로닉스연구그룹에서 세미나 발표.
- 2021-11-05 · iAI lab and SDDO lab (by Prof. Hyunseok Oh) hold a joint workshop for research collaboration at Gwangju.
- 2021-11-04 · iAI (deep learning-based sound source localization) is awarded for the Top 10 Mechanical Technologies of 2021.
- 2021-11-03–2021-11-05 · iAI attends the KSME conference at Gwangju, Korea.
- 2021-11-03 · Prof. Seungchul Lee organizes the special session at the conference of the Korean Society of Mechanical Engineering on behalf of the AI ME group.
- 2021-11-02 · 이승철 교수는 2021년 2학기 기계공학과 학과입문 수업에 '인공지능이 기계와 상관있어?" 라는 주제로 강의
- 2021-11-01 · 김희창 졸업생이 포항에 방문하여 세미나 진행
- 2021-10-29 · Prof. Seungchul Lee gives a talk entitled "Industrial AI: Manufacturing, Materials, and Healthcare" at Sungkyunkwan University at Suwon, Korea.
- 2021-10-25 · Prof. Seungchul Lee gives a talk at 2021 Korea Supercomputing Conference.
- 2021-10-20–2021-10-22 · Juwon Na attends the conference of the Korean Institute of Metals and Materials, Jeju, Korea.
- 2021-10-15 · Prof. Seungchul Lee gives a talk entitled "Key to the Success of Industrial AI" at the POSCO FORUM at Seoul, Korea.

## 연락과 위치

- 위치: 교수실 기계공학동(N7) 6102호[^meprof][^prof]
- 전화: 교수 042-350-3026[^meprof]
- 교수 이메일: seunglee@kaist.ac.kr[^meprof][^prof]
[^p1]: C. Won 외, S. Lee, Physics of Fluids 38, 064123 (온라인 2026-06-22). <https://doi.org/10.1063/5.0327449> 초록 기준.
[^p2]: J. Lee 외, S. Lee, Scientific Reports 15, 16740 (온라인 2025-05-14). <https://doi.org/10.1038/s41598-025-99354-5> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. A. Lee 외, H. S. Kim, Nature Communications 16, 931 (온라인 2025-01-22). <https://doi.org/10.1038/s41467-025-56267-1> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: J. Park 외, S. Lee, ACS Nano 18, 29678-29688 (온라인 2024-10-14). <https://doi.org/10.1021/acsnano.4c08621> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: Y. Song 외, J. Na, Nature Communications 17, 7167 (온라인 2026-06-04). <https://doi.org/10.1038/s41467-026-73735-4> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: H. Park 외, S. Lee, International Journal of Precision Engineering and Manufacturing-Smart Technology 4, 109-126 (2026). <https://doi.org/10.57062/ijpem-st.2026.00052> 초록 기준.
[^p7]: I. Jeong 외, S. Lee, IEEE Transactions on Instrumentation and Measurement 74, 1-12 (2025). <https://doi.org/10.1109/tim.2025.3547117> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: I. Yeon, I. Jeong, S. Lee, J.-W. Choi, IEEE/ACM Transactions on Audio, Speech, and Language Processing 32, 4768-4782 (2024). <https://doi.org/10.1109/taslp.2024.3485516> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 산업 인공지능 연구실 누리집 첫 화면 <https://iailab.kaist.ac.kr/> (연구실 소개, 핵심 연구 영역, 연구 참여 영역, target lab 선정, 2026-10-23 열람)
[^prof]: 연구실 누리집 PEOPLE 메뉴 PROFESSOR 페이지 <https://iailab.kaist.ac.kr/people/professor> (교수 소개, Education, Contact Information, Affiliation, Honors and Awards, Academic Service, 2026-10-23 열람)
[^researchers]: 연구실 누리집 PEOPLE 메뉴 RESEARCHERS 페이지 <https://iailab.kaist.ac.kr/people/researchers> (POSTDOCTORAL RESEARCHERS, GRADUATE STUDENTS, Undergraduate Interns, ALUMNI, 2026-10-23 열람)
[^topics]: 연구실 누리집 RESEARCH 메뉴 TOPICS 페이지 <https://iailab.kaist.ac.kr/research/topics> (2026-10-23 열람)
[^projects]: 연구실 누리집 RESEARCH 메뉴 PROJECTS 페이지 <https://iailab.kaist.ac.kr/research/projects> (On-going, Completed, 2026-10-23 열람)
[^journal]: 연구실 누리집 PUBLICATION 메뉴 Journal 페이지 <https://iailab.kaist.ac.kr/publication/journal> (Journals 연도 구역, Patent, 목록 범위는 근거 페이지, 2026-10-23 열람)
[^conference]: 연구실 누리집 PUBLICATION 메뉴 Conference 페이지 <https://iailab.kaist.ac.kr/publication/conference> (International Conferences, Domestic Conferences, 2026-10-23 열람)
[^news]: 연구실 누리집 NEWS 2026 페이지 <https://iailab.kaist.ac.kr/news-2026>와 NEWS 메뉴 연도별 페이지 <https://iailab.kaist.ac.kr/news/2025>, <https://iailab.kaist.ac.kr/news/2024>, <https://iailab.kaist.ac.kr/news/2023>, <https://iailab.kaist.ac.kr/news/2022>, <https://iailab.kaist.ac.kr/news/2021> (2026-10-23 열람)
[^meprof]: KAIST 기계공학과 교수 소개(이승철) <https://me.kaist.ac.kr/pop/team.html?uid=117&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 이메일, 사무실, 전화, 2026-10-23 열람)

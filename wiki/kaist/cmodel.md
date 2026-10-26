# 연소 모델링 연구실 (Combustion Modeling Lab)

**KAIST 항공우주공학과 · 신동혁 교수**

- 분야: 가스터빈·로켓 엔진 연소기를 위한 연소 모델과 반응 유동의 고정밀 시뮬레이션, 수소 화염의 역화와 화염 속도, 진동하는 화염의 응답과 연소 불안정 예측, 비정상 난류 제트의 혼합, 분무 연소 솔버와 병렬 계산 코드 개발
- 대분야: 기계·로봇·제조, 에너지·환경·지구
- 태그: 연소·엔진[^home][^deptlab], 유체역학·유동[^p4][^p5], 고성능 컴퓨팅(HPC)[^home]
- 홈페이지: <https://cmodel.kaist.ac.kr/>
- 근거와 출처: [연소 모델링 연구실 근거 페이지](cmodel-sources.md)

> 연소 모델과 반응 유동(화학 반응이 함께 일어나는 흐름)의 고정밀 시뮬레이션 방법을 개발하는 연구실이다. 복잡한 형상과 자세한 화학·유체 과정을 다루는 병렬 계산 코드를 만들어 가스터빈과 로켓 엔진 안의 연소를 모사하고, 연소 불안정, 난류 화염 속도, 연료와 산화제의 혼합 같은 연소 과정의 모델을 연구한다.[^home][^deptlab]

## 무엇을 연구하나

연소 모델링 연구실(Combustion Modeling Lab)은 KAIST 항공우주공학과 신동혁 교수가 이끄는 연구실이다.[^deptlab][^deptfac] 누리집 첫 화면은 연구실의 목표를 연소 모델과 반응 유동의 고정밀 시뮬레이션 방법 개발로 적는다. 연구의 중심은 복잡한 형상과 자세한 화학·유체 과정을 다룰 수 있는, 견고하고 병렬성이 높은 CFD(전산유체역학, 흐름을 컴퓨터로 계산하는 방법) 코드를 개발하는 일이고, 이 코드로 가스터빈이나 로켓 엔진 같은 실제 엔진 안의 연소 과정을 모사해 깨끗하고 안정적이며 효율적인 연소 시스템의 설계를 돕는다.[^home] 첫 화면은 연구실이 연소 불안정, 난류 화염 속도, 연료와 산화제의 혼합, 액적 분열(droplet breakout) 같은 여러 연소 과정의 모델 개발에도 관심을 둔다고 적고, TITAN, ARCHER, COMET, BRIDGES 같은 슈퍼컴퓨터에서 10,000개가 넘는 CPU 코어로 난류 연소 시뮬레이션을 해 온 경험이 많다고 소개한다.[^home]

항공우주공학과 연구실 소개 글은 연소기 안에서 유체역학, 열역학, 열전달, 화학동역학 같은 복잡한 현상이 함께 일어나 연소불안정성, 역화, 소염, 공해물질 발생 같은 문제가 생길 수 있다고 설명하고, 연구실이 화염 거동의 근본적 이해로 이 문제를 예측하고 해결하는 것을 목표로 한다고 적는다.[^deptlab] 실사용 연소기 시뮬레이션에는 계산 속도가 빠른 RANS(Reynolds-Averaged Navier-Stokes, 흐름을 시간 평균한 방정식으로 푸는 방법)와 LES(Large Eddy Simulation, 큰 규모의 소용돌이는 직접 계산하고 격자로 풀지 못하는 규모의 효과는 모델로 나타내는 방법)를 쓰고, 난류 화염의 근본 연구에는 정확도가 높은 DNS(Direct Numerical Simulation, 모든 규모의 난류 소용돌이를 모델 없이 직접 계산하는 방법)를 쓴다.[^deptlab] 연구실은 자체 계산 클러스터를 갖추고 국가 슈퍼컴퓨터로 대규모 계산을 하며, 시뮬레이션의 정확도를 높이고 계산 시간을 줄여 궁극적으로 가상설계와 디지털 트윈(Digital Twin)을 구현하는 것을 목표로 둔다.[^deptlab] 같은 글은 연구분야를 High fidelity simulations, Turbulent combustion, Combustion instability, Gas turbines, Super-computing으로 적고, 학과 교수진 목록은 교수의 연구분야를 Combustion, Propulsion, Energy, Simulation으로 적는다.[^deptlab][^deptfac]

누리집 Research 페이지는 연구 주제를 일곱 가지로 든다. 미립화·증발·연소 과정을 처음 원리부터 푸는 분무 연소 솔버, 가스터빈 연소기의 고정밀 시뮬레이션, 화염 전달 함수 모델링을 통한 연소 불안정 예측, 비정상 제트(시간에 따라 흐름 상태가 변하는 분출 흐름)의 난류 혼합, 나이(age) 개념에 바탕을 둔 새로운 난류 연소 모델링, 연료 분무 동역학, 고성능 계산을 위한 코드 개발이다.[^research]

## 주요 연구 주제

### 1. 수소 화염의 역화와 화염 속도 (Hydrogen Flames: Flashback and Flame Speed)

학과 연구실 소개 글은 연구실이 다루는 연소기 문제로 역화(화염이 연료 공급 쪽으로 거슬러 들어가는 현상)와 소염을 든다.[^deptlab] 최근 논문 목록에는 수소를 섞은 예혼합 선회 화염에서 역화 양상이 바뀌는 과정을 다룬 연구(2026), 난류 채널 흐름 속 희박 수소 화염의 흐름 속도와 화염 속도를 다룬 연구(2025)가 있다.[^pubs] 대표 논문 1은 수소와 공기를 미리 섞은 층류 화염을 계산하기 위한 동적 화염 두께 증가 모델을 고쳐 제안하고, 공개 소스 프로그램 OpenFOAM에 구현해 네 가지 화염 배치로 검증했다.[^p1]

### 2. 진동하는 화염의 응답과 연소 불안정 (Oscillating Flames and Combustion Instability)

Research 페이지는 화염 전달 함수 모델링을 통한 연소 불안정 예측을 연구 주제로 들고, 학과 연구실 소개 글은 연소불안정성을 연구실이 예측하고 해결하려는 연소기 문제의 하나로 든다.[^research][^deptlab] 최근 논문 목록에는 주기적으로 진동하는 난류 예혼합 화염의 운동학을 앙상블 평균으로 분석한 연구(2023)가 있다.[^pubs] 대표 논문 2는 주기적으로 진동하는 화염 가까운 영역의 난류 화염 속도와 난류 마크스타인 길이를 점근 해석과 3차원 수치 계산으로 구했고, 대표 논문 3은 스스로 진동하는 원뿔형 화염에 바깥 교란을 가했을 때 진동이 억제되는 기구를, 화염은 CFD로 풀고 음향장은 저차 모델로 나타내는 혼합 계산 틀로 밝혔다.[^p2][^p3]

### 3. 비정상 난류 제트의 혼합 (Turbulent Mixing in Unsteady Jets)

Research 페이지는 비정상 제트의 난류 혼합과, 나이(age) 개념에 바탕을 둔 새로운 난류 연소 모델링을 연구 주제로 든다.[^research] 대표 논문 5는 유체가 흐름 속에 머문 시간을 제트 유체의 질량 가중 흐름 나이로 잰다.[^p5] 대표 논문 5는 유입을 멈춰 감속하는 난류 원형 제트에서 제트 유체의 질량 분율과 질량 가중 흐름 나이가 새로운 자기 유사 상태에 이르는 것을 DNS로 보였고, 대표 논문 4는 멈추는 난류 제트에서 스칼라 소산율의 변화를 DNS와 이론으로 분석해 감속 제트에 맞게 고친 모델을 제안했다.[^p5][^p4] 최근 논문 목록에는 정상 상태 난류 원형 제트의 혼합 분율 분산과 스칼라 소산율 모델링(2022), 난류 축대칭 제트의 3차원 대규모·초대규모 응집 구조(2022) 연구도 있다.[^pubs]

### 4. 분무 연소 솔버와 계산 코드 개발 (Spray Combustion Solver and Code Development)

Research 페이지는 액체 연료가 잘게 부서지는 미립화, 증발, 연소 과정을 함께 푸는 분무 연소 솔버를 개발하고 있다고 적는다. 연소 솔버 PeleLM과 다상 유동 라이브러리 IRL을 결합했고, 결합한 PeleLM+IRL로 진동하는 액체 제트를 모사해 그 방위각 방향 불안정을 연구한다.[^research] 같은 페이지는 University of Melbourne의 Richard Sandberg 교수와 함께 난류 연소를 모사하는 DNS 코드를 개발한다고 적는다. 이 코드 HiPSTAR(The High-Performance Solver for Turbulence and Aeroacoustic Research)는 처음에 반응이 없는 난류 흐름을 모사하려고 개발되었다.[^research] 최근 논문 목록에는 PeleLM에 기하학적 VOF(Volume of Fluid) 기반 다상 유동 솔버를 확장한 연구(2026), 경직 반응계의 시간 적분을 자동 인코더와 신경 상미분방정식으로 빠르게 하는 연구(2025), 유전 알고리즘으로 제트 연료의 대리 연료를 구성한 연구(2026)가 있다.[^pubs]

## 대표 논문

누리집 Publications 목록의 2021–2026년 학술지 논문 가운데 신동혁 교수가 저자인 논문에서, 연구 갈래마다 초록을 구할 수 있는 다섯 편을 골랐다. 교수는 1·2·4번에서 마지막 저자, 5번에서 첫 저자, 3번에서 다섯 명 가운데 넷째 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2024 | [Development of a modified dynamic flame thickened model for laminar premixed hydrogen/air flames](https://doi.org/10.1007/s12206-024-0647-2) · Journal of Mechanical Science and Technology | 수소와 공기를 미리 섞은 층류 예혼합 화염(흐름이 흐트러지지 않고 매끄러운 상태에서 미리 섞인 연료와 공기가 타는 화염)을 위한 동적 화염 두께 증가 모델(화염을 계산 격자로 풀 수 있도록 두껍게 늘이면서 화염 속도를 지키는 연소 모델)을 고쳐 제안하고, 검증 시뮬레이션을 했다. 모델은 공개 소스 프로그램 OpenFOAM v9에 구현했고, 1차원 층류 예혼합 화염, 축대칭 정체점 화염, 축대칭 분젠 화염, 2차원 블러프 바디(흐름을 막는 뭉툭한 물체) 화염의 네 가지 화염을 모사했다. 1차원 화염 계산으로 두께 증가 모델의 타당성을 다시 확인했고, 정체점 화염 계산으로 모델 변수인 최적 수정 계수를 찾았다. 분젠 화염 계산에서는 화염 속도와 신장률(화염 면적이 시간에 따라 늘어나는 정도를 그 면적으로 나눈 값)이 잘 유지되었다. 2차원 블러프 바디 화염 계산에서는 제안한 모델이 특히 낮은 당량비(실제 연료·공기 비를 완전 연소에 맞는 연료·공기 비로 나눈 값) 조건에서 두께를 늘이지 않은 기준 계산과 비슷한 신장 층류 화염 속도를 냈고, 기준 자료에 견주어 적절한 예측 정확도를 보였다.[^p1] | 1저자 M. Choi(Minjun Choi), 마지막 저자 신동혁 (3명) |
| 2 | 2023 | [Turbulent Flame Speed and Turbulent Markstein Length in the Near Field of a Harmonically Oscillating Flame](https://doi.org/10.1080/00102202.2023.2251169) · Combustion Science and Technology | 난류 화염 속도와 난류 마크스타인 길이(화염이 늘어날 때 화염 속도가 바뀌는 정도를 나타내는 길이 척도)를 해석과 수치 방법으로 연구했다. 주기적으로 진동하는 화염에 점근 해석(어떤 변수를 극한으로 보내 근사식을 끌어내는 방법)을 적용해, 늘어나지 않은 상태의 난류 화염 속도와 난류 마크스타인 길이를 나타내는 명시적인 식을 얻었다. 3차원 레벨셋 방법(화염 면을 함수의 등고선으로 나타내 추적하는 계산 방법)으로 층류 화염 속도, 화염 고정 장치의 진동 진폭, 난류 강도, 흐름 방향 길이 척도를 바꾸며 수치 계산을 했다. 하류로 가면서 늘어나지 않은 난류 화염 속도는 포물선 꼴로, 마크스타인 길이는 직선 꼴로 커졌다. 얻은 식은 계산 결과와 맞아 가까운 영역의 화염 동역학을 이해하게 해 준다. 먼 영역에서는 계산에서 두 값이 포화되었는데, 이것은 점근 해석으로 잡히지 않았다.[^p2] | 1저자 J. Sohn(Jungho Sohn), 마지막 저자 신동혁 (3명) |
| 3 | 2026 | [Nonlinear forced response of a self-excited conical lean-premixed flame](https://doi.org/10.1063/5.0342290) · Physics of Fluids | 스스로 진동하는 원뿔형 화염에 바깥에서 주기적인 교란을 가했을 때의 응답을, 화염 동역학은 CFD로 풀고 음향장은 저차 모델(적은 수의 변수로 나타낸 간단한 모델)로 나타내는 혼합 계산 틀로 연구했다. 이 틀은 계산 노력을 열음향 비선형성의 주된 원천인 화염 동역학에 모은다. 교란 없이 스스로 진동할 때 열 방출률 변동은 화염 끝이 떨어져 나가는 현상(pinch-off)이 좌우해, 떨어져 나가기 직전에 가장 크고 떨어져 나간 화염 덩어리가 사라질 때 가장 작다. 교란을 가하면 이 틀은 앞선 실험이 보고한 음압 변동의 억제 구간과 감쇠 정도를 만족스럽게 재현했다. 진동 억제는 음압 변동과 열 방출률 변동의 위상이 일치하던 상태에서 서로 어긋나는 상태로 바뀌어 열음향 결합이 약해지고 음향 에너지 생성이 줄어들기 때문에 생긴다. 레일리 지수 분석은 교란이 주로 화염 끝이 떨어져 나가는 화염 위쪽에 영향을 주고, 화염 아래쪽의 파동 묶음 꼴 구조는 거의 바뀌지 않음을 보였다. 연구진은 화염 끝이 떨어져 나가는 현상을 바깥 교란과 열음향 억제를 잇는 핵심 기구로 지목했다.[^p3] | 1저자 F. Bian(Fang Bian), 넷째 저자 신동혁, 마지막 저자 Y. Guan(Yu Guan) (5명) |
| 4 | 2025 | [Spatial and temporal characteristics of scalar dissipation rate in a stopping turbulent jet](https://doi.org/10.1017/jfm.2025.273) · Journal of Fluid Mechanics | 멈추는 난류 제트에서 스칼라 소산율(분자 확산으로 농도 변동이 소산되는 정도를 나타내는 양)이 어떻게 바뀌는지 DNS와 이론으로 분석했다. 제트를 멈추면 스칼라 소산율의 감속파가 축 방향 속도의 감속파와 비슷한 빠르기로 하류로 퍼진다. 감속파의 상류 쪽에서는 중심선의 평균 스칼라 소산율이 축 방향 거리에 비례하고 시간의 제곱에 반비례한다. 감속파가 지나간 뒤에는 스칼라 소산율과 그 축 방향·반경 방향·방위각 방향 성분의 정규화한 반경 방향 분포가 정상 상태와 다른 자기 유사 상태(감속 자기 유사 분포)에 이른다. 평균 스칼라 소산율 수송 방정식에서는 감속 자기 유사 상태에서도 생성항과 소멸항이 지배적이다. 이론 접근은 이 수송 방정식에 있는 난류 변동항의 반경 방향 분포를 명시적으로 예측한다. 연구진은 난류 스칼라 소산율 모델 세 가지를 검증하고, 자기 유사성 분석에 바탕을 두어 감속 제트에 알맞게 고친 모델을 제안했다.[^p4] | 1저자 V. Aparece-Scutariu(Vlad Aparece-Scutariu), 마지막 저자 신동혁 (3명) |
| 5 | 2022 | [Unsteady self-similarity of jet fluid age and mass fraction](https://doi.org/10.1063/5.0132042) · Physics of Fluids | 감속하는 난류 원형 제트의 스칼라 혼합을 DNS로 조사했다. 비정상 흐름에서 새로운 자기 유사 상태(분포를 그 위치의 대표 크기로 나누면 위치와 관계없이 같은 모양이 되는 상태)를 찾아 모델로 나타내고, 중심선을 따라 관련 물리량이 어떻게 바뀌는지 예측하는 것이 목표다. 제트 유체의 질량 분율과, 제트 유체의 질량 가중 흐름 나이로 잰 유체 체류 시간은 통계적으로 정상인 난류 제트에서 자기 유사한 반경 방향 분포를 보인다. 유입을 멈추면 감속파가 제트를 지나가고, 그 뒤에서 두 스칼라 변수에 정상 상태 제트와 다른 새로운 자기 유사 상태가 나타난다. 정상 상태와 달리 감속 제트에서 제트 유체의 질량 분율은 하류 거리에 따라 직선으로 늘고, 중심선의 질량 가중 흐름 나이는 하류 거리에 계속 비례한다. 스칼라 수송 수지 분석은 두 스칼라 모두에서 반경 방향 수송항이 커지고, 제트 질량 분율의 흐름 방향 수송항 기여는 정상과 비정상 경우 사이에 부호가 바뀜을 보였다.[^p5] | 1저자 신동혁, 마지막 저자 E. S. Richardson(Edward S. Richardson) (4명) |

## 교수와 전문 분야

신동혁 교수(Dong-hyuk Shin)는 KAIST 항공우주공학과 부교수다.[^prof][^deptfac] 교수 페이지에 따르면 KAIST에서 항공우주공학 학사(2006, 최우등, 수학 부전공)를, Georgia Institute of Technology에서 항공우주공학 박사(2012)를 받았다. 이후 Georgia Institute of Technology 박사후연구원(2013/01 – 2013/03), 프랑스 CERFACS(Centre Européen de Recherche et de Formation Avancée en Calcul Scientifique)의 Marie-Curie research fellow(2013/04 – 2014/03), University of Southampton 연구원(Research fellow, 2014/04 – 2015/06), University of Edinburgh 강사(Lecturer, 누리집 표기로 조교수에 해당, 2015/07 – 2019/07)를 거쳤다.[^prof] 교수실은 N7-2동 4304호다.[^prof][^deptlab]

학과 교수진 목록은 교수의 연구분야를 연소, 추진, 에너지, 시뮬레이션으로 적고, 학과 연구실 소개 글은 고정밀 시뮬레이션, 난류 연소, 연소 불안정, 가스터빈, 슈퍼컴퓨팅을 연구분야로 든다.[^deptfac][^deptlab] 2021–2026년 대표 논문으로 보면 최근 전문 분야는 수소 화염을 위한 연소 모델(대표 논문 1), 진동하는 화염의 화염 속도와 열음향 응답(대표 논문 2, 3), 비정상 난류 제트의 혼합과 그 모델링(대표 논문 4, 5)이다.[^p1][^p2][^p3][^p4][^p5]

## 응용 분야

누리집 첫 화면은 연구실의 코드가 가스터빈이나 로켓 엔진 같은 실제 엔진 안의 연소 과정을 모사해 깨끗하고 안정적이며 효율적인 연소 시스템의 설계를 돕는 데 쓰일 수 있다고 적는다.[^home] 학과 연구실 소개 글은 연소기 안의 연소불안정성, 역화, 소염, 공해물질 발생 같은 문제의 예측과 해결, 시뮬레이션에 바탕을 둔 가상설계와 디지털 트윈 구현을 목표로 든다.[^deptlab]

## 구성원

누리집 Graduate students 페이지의 박사후연구원(Post-Doc) 2명, 박사과정(Ph.D. Candidates) 8명, 석사과정(M.S. Candidates) 6명, 연구 직원(Research Staff) 2명, 모두 18명이다. 시작 칸은 카드가 적은 KAIST 현재 과정의 시작 연도이고, 연구 주제 칸은 카드의 Research Interest를 그대로 옮겼다. 연구 직원 Bian Fang의 과정 칸 괄호에는 카드가 적은 다른 학교 박사과정 줄을 그대로 옮겼다. 대표 논문 참여 칸은 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^grad]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| 김용제 (Kim, Yong Jea) | 박사후연구원 |  | Combustion Instability, Active Control of Themoacoustic Systems, Modelling and Experimental Approaches to Thermal Fluid Systems | yongjeakim@kaist.ac.kr | 1 |
| 첸 바오 (Chen, Bao) | 박사후연구원 |  | High-speed flow and combustion, Rotating detonation engine | aerochen@kaist.ac.kr |  |
| 구인영 (Gu, Inyeong) | 박사과정 | 2023 | DNS simulation, Gas turbine engine, NOx emission, Chemical mechanism | inyeong.gu@kaist.ac.kr |  |
| 최낙정 (Choi, Nakjeong) | 박사과정 | 2023 | DNS simulation, Gas turbine engine, NOx emission, Chemical mechanism | simply0116@kaist.ac.kr |  |
| 김형우 (Kim, Hyoungwoo) | 박사과정 | 2023 | DNS simulation, Multiphase, Spray combustion | kimhw001@kaist.ac.kr |  |
| 손주훈 (Son, Juhoon) | 박사과정 | 2024 | Combustion instability, Gas turbine engine | juhoon.son@kaist.ac.kr | 2 |
| 백민하 (Baek, Minha) | 박사과정 | 2024 | Flame Wall Interaction(FWI), Flashback, Gas turbine engine | minha.baek@kaist.ac.kr |  |
| 윤효상 (Yoon, Hyosang) | 박사과정 | 2024 | Flame instability, Gas turbine engine | yoon8787@kaist.ac.kr |  |
| 윤재원 (Yoon, Jaewon) | 박사과정 | 2025 | Gas turbine Engine, Jet in Crossflow | jwyoon00@kaist.ac.kr |  |
| 김선창 (Kim, Sunchang) | 박사과정 | 2026 | Rocket injector, Supercritical combustion | sunkim252@kaist.ac.kr |  |
| 박상현 (Park, Sanghyuen) | 석사과정 | 2025 | Gas turbine engine | sanghyuen12@kaist.ac.kr |  |
| 김민호 (Kim, Minho) | 석사과정 | 2025 | Shape optimization, Gas turbine engine | minho.kim@kaist.ac.kr |  |
| 킬리치 메르베 (Kilic, Merve) | 석사과정 | 2026 | Gas turbine engine | Merve.kilic@kaist.ac.kr |  |
| 김민태 (Kim, Mintae) | 석사과정 | 2026 | Gas turbine engine, Combustion | ener67@kaist.ac.kr |  |
| 김경욱 (Kim, Gyeonguk) | 석사과정 | 2026 | Gas turbine engine, Liquid propellant | kimgu019@kaist.ac.kr |  |
| 마네 리테시 프라탑 (Mane, Ritesh Pratap) | 석사과정 | 2026 | Swirling jet | ritesh.mane@kaist.ac.kr |  |
| 김진성 (Kim, Jinseong) | 연구 직원 |  | Turbulent flame, Rocket engine |  |  |
| 비엔 팡 (Bian, Fang) | 연구 직원 (2024-present, Ph.D., Aerospace Engineering, The Hong Kong Polytechnic University, Hong Kong, China) |  | Numerical simulation of thermoacoustic instability | fangbian@kaist.ac.kr | 3 |

## 졸업생과 이전 구성원

누리집 Alumni & Past affiliated members 페이지의 Ph.D. 3명, M.S. 5명, Past affiliated members 5명, 모두 13명이다. 학위·과정 칸은 카드의 마지막 학력 줄을, 연도는 그 줄의 연도를 옮겼다(김승환 카드는 「Completion of Master course」로 적는다). 졸업생 카드는 진로를 적지 않는다. Past affiliated members 가운데 Zhen Zhang과 Yajin Lyu는 카드가 「Visiting researcher at the University of Edinburgh」로 적어, 교수가 University of Edinburgh에 있던 시기의 방문 연구자다. Dr. Vlad Aparece-Scutariu 행의 진로 칸은 카드가 적은 기관이고, 학위 논문 칸은 카드의 Dissertation 표기다.[^alumni][^prof]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| 손정호 (Sohn, Jungho) | Ph.D., Aerospace Engineering, KAIST, Daejeon, South Korea (2026) |  |  |
| 최민준 (Choi, Minjun) | Ph.D., Aerospace Engineering, KAIST, Daejeon, South Korea (2026) |  |  |
| 김강환 (Kim, Kanghwan) | Ph.D., Aerospace Engineering, KAIST, Daejeon, South Korea (2026) |  |  |
| 곽근재 (Kwak, Keunjae) | M.S., Aerospace Enginnering, KAIST, Daejeon, South Korea (2026) |  |  |
| 골랩 패트릭 (Gołab, Patryk) | M.S., Aerospace Engineering, KAIST, Daejeon, South Korea (2026) |  |  |
| 알마즈로이 모하메드 (Almazrouei, Mohammed) | M.S., Aerospace Engineering, KAIST, Daejeon, South Korea (2025) |  |  |
| 백향목 (Baek, Hyangmok) | M.S., Aerospace Engineering, KAIST, Daejeon, South Korea (2025) |  |  |
| 김승환 (Kim, Seung Hwan) | Completion of Master course, Aerospace Engineering, KAIST, Daejeon, South Korea (2024) |  |  |
| 바이칸 메르트 야쿠프 (Baykan, Mert Yakup) | Past affiliated member (B.S., Aerospace Enginnering, KAIST, Daejeon, South Korea) (2026) |  |  |
| Dr. Vlad Aparece-Scutariu | Past affiliated member | Romanian Research and Development Institute for Gas Turbine | Numerical and theoretical investigation of turbulent unsteady jets and plumes |
| Zhen Zhang | Past affiliated member (Visiting researcher at the University of Edinburgh) |  |  |
| Yajin Lyu | Past affiliated member (Visiting researcher at the University of Edinburgh) |  |  |
| 김재현 (Kim, Jaehyeon) | Past affiliated member (M.S., Aerospace Engineering, Sunchon National University, Suncheon, South Korea) (2020) |  |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지의 International Journals 목록은 학술지 논문 33편을 싣고, Conference Proceedings와 Invited talks 항목은 비어 있다.[^pubs] 아래는 끝에 2021–2026년이 적힌 13편이다(2026년 4편, 2025년 3편, 2024년 1편, 2023년 2편, 2022년 3편). 2021년이 적힌 논문은 없다. 저자 표기, 제목, 학술지, 연도는 누리집 그대로다.[^pubs]

**2026**

- M. Choi, M. Baek, J. I. Ryu, D-H. Shin. "Flashback Mode Transitions in Premixed Hydrogen-Enriched Swirl Flames". *Combustion Science and Technology*.
- F. Bian, J. Zhang, C. Wang, D-H. Shin, Y. Guan. "Nonlinear forced response of a self-excited conical lean-premixed flame". *Physics of Fluids*.
- J. Son, Y. Gil, S. Ko, D-H. Shin, S. Park. "Development of jet surrogate fuel formulated by genetic algorithm". *Fuel*.
- H. Kim, R. Chiodi, M. Day, Y. J. Kim, D-H. Shin. "A geometric volume of fluid-based multiphase flow solver extension to the reacting flow solver, PeleLM". *Advances in Engineering Software*.

**2025**

- J. Sohn, M. Lee, D-H. Shin. "Characteristics of flow velocity and flame speed in a turbulent channel flow for lean hydrogen flames". *Proceedings of the Combustion Institute*.
- M. Y. Baykan, V. Vijayarangan, D-H. Shin, H. G. Im. "Accelerated integration of stiff reactive systems using gradient-informed autoencoder and neural ordinary differential equation". *Combustion Theory and Modelling*.
- V. Aparece-Scutariu, M. Choi, D-H. Shin. "Spatial and temporal characteristics of scalar dissipation rate in a stopping turbulent jet". *Journal of Fluid Mechanics*.

**2024**

- M. Choi, Y. J. Kim, D-H. Shin. "Development of a modified dynamic flame thickened model for laminar premixed hydrogen/air flames". *Journal of Mechanical Science and Technology*.

**2023**

- J. Sohn, J. Son, D-H. Shin. "Turbulent Flame Speed and Turbulent Markstein Length in the Near Field of a Harmonically Oscillating Flame". *Combustion Science and Technology*.
- K. Kim, Y. J. Kim, A. Aspden, D-H. Shin. "Ensemble-Averaged Kinematics of Harmonically Oscillating Turbulent Premixed Flames". *Combustion and Flame*.

**2022**

- V. Aparece-Scutariu, D-H. Shin. "Spatial characteristics and modelling of mixture fraction variance and scalar dissipation rate in steady turbulent round jets". *International Journal of Heat and Fluid Flow*.
- M. Samie, V. Aparece-Scutariu, P. Lavoie, D-H. Shin, A. Pollard. "Three-dimensional large-scale and very-large-scale coherent structures in a turbulent axisymmetric jet". *Journal of Fluid Mechanics*.
- D-H. Shin, A. Aspden, V. Aparece-Scutariu, E. S. Richardson. "Unsteady self-similarity of jet fluid age and mass fraction". *Physics of Fluids*.

## 연락과 위치

- 연구실·교수실: Room 4304, Building N7-2, Department of Aerospace Engineering, 291 Daehak-ro, Yoosung-gu, Daejeon, South Korea(누리집 표기), 항공우주공학과 표기로 N7-2동 #4304[^contact][^deptlab]
- 전화: +82-42-350-3732[^contact][^prof]
- 교수 이메일: donghyuk.shin@kaist.ac.kr[^contact][^prof][^deptlab]
[^home]: Combustion Modeling Lab 누리집 첫 화면 <https://cmodel.kaist.ac.kr/> (Introduction, 2026-10-23 열람)
[^research]: Combustion Modeling Lab 누리집 Research 페이지 <https://cmodel.kaist.ac.kr/research> (연구 주제 일곱 가지, 2026-10-23 열람)
[^prof]: Combustion Modeling Lab 누리집 Prof. Dong-hyuk Shin 페이지 <https://cmodel.kaist.ac.kr/members/prof-dong-hyuk-shin> (직위, 학력, 경력, 이메일, 전화, 교수실, 2026-10-23 열람)
[^grad]: Combustion Modeling Lab 누리집 Graduate students 페이지 <https://cmodel.kaist.ac.kr/members/graduate-students> (Post-Doc 2명, Ph.D. Candidates 8명, M.S. Candidates 6명, Research Staff 2명, 2026-10-23 열람)
[^alumni]: Combustion Modeling Lab 누리집 Alumni & Past affiliated members 페이지 <https://cmodel.kaist.ac.kr/members/alumni-past-affiliated-members> (Ph.D. 3명, M.S. 5명, Past affiliated members 5명, 2026-10-23 열람)
[^pubs]: Combustion Modeling Lab 누리집 Publications 페이지 <https://cmodel.kaist.ac.kr/publications> (International Journals 33편, 2026-10-23 열람)
[^contact]: Combustion Modeling Lab 누리집 Contact 페이지 <https://cmodel.kaist.ac.kr/contact> (주소, 이메일, 전화, 2026-10-23 열람)
[^deptlab]: KAIST 항공우주공학과 연구실 소개 「Combustion Modeling Lab」 <https://ae.kaist.ac.kr/boards/view/board_lab/12439> (연구실명, 교수, 연구실 소개, 연구분야, 웹사이트, 이메일, 전화, 위치, 2022-03-07 게시, 2026-10-23 열람)
[^deptfac]: KAIST 항공우주공학과 구성원 교수진 목록 <https://ae.kaist.ac.kr/boards/lists/board_faculty/sc_category/1/> (직위, 학력, 연구분야, 웹사이트, 위치, 2026-10-23 열람)
[^p1]: M. Choi, Y. J. Kim, D.-h. Shin, Journal of Mechanical Science and Technology 38, 3769-3790 (온라인 2024-07-04). <https://doi.org/10.1007/s12206-024-0647-2> 초록 기준(출판사 논문 페이지).
[^p2]: J. Sohn, J. Son, D.-H. Shin, Combustion Science and Technology 197, 497-524 (2025). <https://doi.org/10.1080/00102202.2023.2251169> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: F. Bian 외, Y. Guan, Physics of Fluids 38, 073610 (온라인 2026-07-08). <https://doi.org/10.1063/5.0342290> 초록 기준.
[^p4]: V. Aparece-Scutariu, M. Choi, D.-h. Shin, Journal of Fluid Mechanics 1010, A21 (온라인 2025-05-08). <https://doi.org/10.1017/jfm.2025.273> 초록 기준.
[^p5]: D.-h. Shin, A. J. Aspden, V. Aparece-Scutariu, E. S. Richardson, Physics of Fluids 35, 015139 (온라인 2023-01-17). <https://doi.org/10.1063/5.0132042> 초록 기준.

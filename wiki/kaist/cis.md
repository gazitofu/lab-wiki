# 제어 및 지능형 시스템 연구실 (Control and Intelligent Systems Lab, CIS Lab)

**KAIST 전기및전자공학부·안보과학기술대학원 · 안희진 교수**

- 분야: 제어 이론과 인공지능을 잇는 안전한 학습 기반 제어, 인식 불확실성을 고려한 자율주행차의 제어와 운동 계획, 여러 차량의 교차로 조정과 차량·도로 인프라의 협력 인지, 지능형 인프라를 갖춘 축소 도시 테스트베드
- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 제어 이론·제어 공학[^home][^p1][^p2], 자율주행[^gst][^p1][^p8], 교통·도시 계획[^research][^p7]
- 홈페이지: <https://cis.kaist.ac.kr/>
- 근거와 출처: [제어 및 지능형 시스템 연구실 근거 페이지](cis-sources.md)

> 안전하고 서로 협력하는 지능형 시스템을 만드는 연구실로, 제어 이론과 현대 인공지능을 이어 하나의 에이전트부터 대규모 다중 에이전트 시스템까지 다룬다.[^home]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 안희진 교수가 이끄는 연구실이다. 누리집은 이름을 Control and Intelligent Systems Lab(CIS Lab)으로 적고, 전기및전자공학부 교수 소개는 소속연구실을 「제어 및 지능형 시스템 연구실」로 적는다.[^home][^ee] 첫 화면 소식은 교수가 2022년 7월 KAIST 전기및전자공학부에서 연구실을 시작했다고 적는다.[^home] 전기및전자공학부 교수 소개는 교수의 주요 연구를 제어, 최적화, 로보틱스, 지능형교통시스템으로 적고,[^ee] 안보과학기술대학원 교수 명단은 교수의 소속학과를 전기및전자공학부로, 연구분야를 인공지능/무인체계로, 세부 연구 분야를 제어·지능형시스템·최적화·자율주행으로 적는다.[^gst] 연구실은 스스로를 안전하고 협력하는 지능형 시스템을 만드는 곳으로 소개하고, 연구가 제어 이론(측정값을 바탕으로 시스템이 원하는 대로 움직이도록 입력을 정하는 방법을 수학 모형으로 설계하고 분석하는 분야)과 현대 인공지능을 이으며 하나의 에이전트(스스로 판단해 움직이는 주체)부터 대규모 다중 에이전트 시스템까지 다룬다고 적는다.[^home]

연구 페이지는 연구를 두 묶음으로 나눈다. 첫째 묶음 **Safe Intelligence**는 믿을 수 있고 안전한 학습 기반 지능형 시스템을 위한 방법을 개발하는 일로, 증명할 수 있는 안전, 분포 변화(학습 때와 실제 사용 때의 자료 분포가 달라지는 일)와 불확실성 아래의 안전, 더 넓은 AI 안전 문제를 다룬다고 적는다.[^research] 둘째 묶음 **Collaborative Intelligence**는 흩어진 여러 종류의 센서에서 정보를 모으고 다양한 자율 에이전트에게 조율된 안내를 주어 더 안전하고 효율적으로 운행하게 하는 협력 지능 플랫폼, 곧 운영 센터를 개발하는 일이다. 이 묶음 아래에 다중 차량·다중 에이전트 계획, 협력 인지(한 차량이나 장치가 주변 차량·도로 시설의 센서 정보를 받아 합쳐 주변을 알아보는 일), 피지컬 AI(실제 물리 세계에서 감지하고 움직이는 기계에 들어간 인공지능)와 로봇 플랫폼을 든다.[^research]

연구 페이지의 스마트 시티 테스트베드는 실제 교차로 지도를 1:15 비율로 줄이고 차량과 인프라, 다른 구조물도 같은 1:15 비율로 줄인 시험 환경으로, 연구실은 이를 「semi-realistic」 테스트베드라 부른다. 실제와 같은 센서와 통신, 제어 잡음이 들어 있어 시뮬레이션과 구분되고, 신호등 같은 인프라도 센서와 계산 모듈을 갖춘 「지능형」 인프라로 다룬다. 이 인프라는 V2X(차량이 다른 차량, 도로 시설 등 주변의 여러 대상과 정보를 주고받는 통신 기술)로 차량과 정보를 계속 나누며, 교통 흐름을 능동적으로 제어하고 협력 인지를 하는 미래 기술 개발에 쓰인다고 적는다.[^research]

첫째 갈래는 **안전한 학습 기반 제어**다. 대표 논문에서는 신경망 인식의 불확실성을 증거 딥러닝(예측과 함께 그 예측을 뒷받침하는 근거의 양을 내놓도록 신경망을 학습하는 방법)으로 반영하고, 분포 강건 최적화(확률분포를 정확히 모를 때 가능한 분포들의 모음 가운데 가장 나쁜 경우에도 성립하도록 푸는 최적화)로 인식 신뢰도에 따라 제약의 보수성(위험을 피하려고 여유를 두는 정도)을 조절하는 모델 예측 제어(시스템 모형으로 앞으로의 움직임을 예측하며 매 시점 최적의 입력을 다시 계산하는 제어 방법) DRO-EDL-MPC를 만들었다.[^p1] 교통 표지 인식처럼 인식 모듈의 출력이 불확실할 때도 가능한 상황마다 붙은 제약을 높은 확률로 지키는 확률 제약 제어(제약을 정해 둔 확률 이상으로 지키도록 입력을 정하는 제어)를 제안했고,[^p2] 샘플링(확률에 따라 표본을 여러 개 뽑아 계산하는 방법)이나 분포 가정 없이 신경망 예측의 불확실성을 추정하는 HCM(Hyperspherical Confidence Mapping)을 제안했다.[^p3] 어떤 기본 제어 입력이든 샘플링으로 안전을 따져, 샘플한 후보가 모두 위험하면 기본 입력을 덮어쓰는 안전 필터(제어기가 낸 입력을 검사해 안전 조건을 어길 때 안전한 입력으로 바꾸는 구성 요소)도 제시했다.[^p4] 최근 논문 목록에는 오프라인 강화학습(이미 모아 둔 자료만으로 보상을 크게 하는 행동을 배우는 기계학습 방법)의 정책(상황마다 어떤 행동을 할지 정하는 규칙)을 확률 제약으로 걸러 안전을 지키는 연구(IROS, 2026, 채택), 불확실한 환경에서 확률적으로 재귀적 실현 가능성(지금 계획을 풀 수 있으면 다음 시점에도 풀 수 있는 성질)을 갖도록 운동 계획(로봇이나 차량이 어떤 경로와 동작으로 움직일지 정하는 일)을 세우는 연구(IFAC World Congress, 2026, 채택), 데이터셋의 포괄 범위(coverage)를 바탕으로 데이터셋 품질을 계산 효율적으로 재는 방법(AISTATS, 2025)도 있다.[^pubs]

둘째 갈래는 **협력 지능: 다중 차량 조정과 협력 인지**다. 대표 논문에서는 협력 인지에서 인프라 자료의 역할을 정량적으로 따졌고,[^p5] 신호등 없는 교차로에서 여러 차량을 조정하는 Decision Transformer(지난 상태·행동과 앞으로 얻을 보상의 합을 차례로 입력받아 다음 행동을 예측하는 신경망 모델) 기반 방법을 만들었다.[^p6] 교차로에 다가오는 차량이 멈출 때 지킬 최적 간격을 인프라가 안내하는 시스템을 제시했고,[^p7] 센싱·엣지 컴퓨팅(자료가 생기는 곳 가까이에서 계산을 처리하는 방식)·통신 기능을 갖춘 지능형 인프라가 들어간 1:15 축소 테스트베드 CIVAT을 만들었다.[^p8] 최근 논문 목록에는 인프라가 자율주행차에 최적 가속을 안내해 교통 흐름의 충격파(멈추거나 느려진 차량 흐름이 뒤쪽으로 퍼져 나가는 현상)를 줄이는 연구(ITSC, 2025), 차량 재배치 없이(relocation-free) 순차적으로 주차·출차하는 고밀도 자동 발레 주차(운전자가 내린 뒤 차량이 스스로 주차 자리까지 가서 주차하는 기능) 연구(ITSC, 2026, 채택), 차량 상태 추정을 위한 온라인 센서 선택(IFAC World Congress, 2026, 채택), 자율 모빌리티의 실시간 지능형 의사결정을 돕는 C-V2X(셀룰러 이동통신망을 이용하는 V2X 통신) 틀(Communications in Transportation Research, 2025)도 있다.[^pubs]

## 주요 연구 주제

### 1. 안전한 학습 기반 제어(Safe Intelligence)

인식 결과의 불확실성을 제어 계산에 반영하고, 위험한 제어 입력을 걸러 차량의 안전을 지키는 방법을 연구한다.[^p1][^p2][^p3][^p4][^research] 대표 논문 1–4.

### 2. 협력 지능: 다중 차량 조정과 협력 인지(Collaborative Intelligence)

차량과 도로 인프라가 센서 정보를 나누고, 교차로에서 여러 차량의 움직임과 간격을 조정하는 방법을 연구한다.[^p5][^p6][^p7][^p8][^research] 대표 논문 5–8.

## 대표 논문

랩 Publications 페이지의 2023–2026년 논문 가운데 안희진 교수가 마지막 저자인 학술지·학회 논문을 두 연구 갈래에 고르게 담도록 골랐다. 여덟 편 모두 교수가 KAIST에서 연구실을 시작한 2022년 7월 뒤의 논문이다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [DRO-EDL-MPC: Evidential Deep Learning-Based Distributionally Robust Model Predictive Control for Safe Autonomous Driving](https://doi.org/10.1109/lra.2026.3655206) · IEEE Robotics and Automation Letters | 자율주행차의 운동 계획에서 안전은 중요한 문제다. 지금의 자율주행차는 신경망 기반 인식에 기대는데, 그 추론 결과로 제어를 결정하면 인식에 들어 있는 불확실성 때문에 큰 안전 위험이 생긴다. 증거 딥러닝(EDL)으로 인식의 두 가지 불확실성(자료 자체의 무작위성에서 오는 것과 모델의 지식 부족에서 오는 것)을 함께 고려하는 분포 강건 최적화(DRO) 틀을 제시했다. 증거 분포를 바탕으로 한 새로운 모호성 집합(가능한 확률분포들의 모음)이 인식 신뢰도에 따라 보수성을 동적으로 조절하고, 이 제약을 모델 예측 제어(MPC)에 넣어 자율주행에 쓸 수 있는 계산 가능한 DRO-EDL-MPC 알고리즘을 만들었다. CARLA 시뮬레이터에서 인식 신뢰도가 높을 때는 효율을 유지하고 낮을 때는 보수적인 제약을 적용함을 확인했다.[^p1] | 1저자 Hyeongchan Ham, 마지막 저자 안희진 |
| 2 | 2023 | [Chance-Constrained Control with Imperfect Perception Modules](https://doi.org/10.23919/acc55779.2023.10155868) · American Control Conference (ACC) | 자율 시스템은 여러 환경에서 동작해야 하지만 지금 어떤 환경인지 알아보기 어려운 때가 많다. 예를 들어 자율주행차는 교통 표지에 따라 멈추거나 제한 속도를 지켜야 하는데, 신경망 같은 최신 인식 모듈도 표지를 바르게 읽는다고 보장하지 못한다. 인식 모듈의 불확실한 출력이 사실상 상황(모드)을 정한다는 점을 고려해, 가능한 모드마다 붙은 제약들을 높은 확률로 지키도록 보장하는 확률 제약 제어 식을 제안했다. 각 모드의 확률은 베이즈 규칙(새로 얻은 정보로 확률을 고쳐 계산하는 규칙)과 샘플링으로 계산하며, 인식 모듈 학습에 쓰이지 않은 새로운 상황의 제약도 지킬 수 있음을 증명했다. 자료가 적어 생기는 오차를 고려해 높은 신뢰도로 제약 만족을 보장하는 강건한 식도 제시했다. 교통 표지를 분류하는 신경망을 학습한 자율주행차 예에서, 신경망의 출력마다 운동 계획이 높은 확률로 제약을 지킴을 보였다.[^p2] | 1저자 Beomjun Kim, 마지막 저자 안희진 |
| 3 | 2026 | [Uncertainty Estimation via Hyperspherical Confidence Mapping](https://arxiv.org/abs/2605.05964) · International Conference on Learning Representations (ICLR), 채택 | 자율주행, 의료, 제조처럼 위험이 큰 분야에서는 신경망 예측의 불확실성을 수치로 나타내는 일이 꼭 필요하다. 기존 방법은 비용이 큰 샘플링이나 제한적인 분포 가정에 기대는 경우가 많아, 샘플링도 분포 가정도 없이 불확실성을 추정하는 틀 HCM(Hyperspherical Confidence Mapping)을 제안했다. 출력을 크기와, 단위 초구(길이가 단위 길이인 벡터들이 이루는 여러 차원의 구면) 위에 놓이도록 제약한 방향 벡터로 나누고, 이 기하 제약이 어긋난 정도를 불확실성으로 해석한다. 이렇게 하면 회귀(연속된 값을 예측하는 문제)와 분류(정해진 범주 가운데 하나를 고르는 문제) 모두에 쓸 수 있고, 같은 입력에 늘 같은 값을 내며 해석할 수 있는 추정값을 얻는다. 여러 벤치마크와 실제 산업 과제에서 앙상블(여러 모델의 예측을 함께 쓰는 방법)·증거 기반 방법과 같거나 나은 성능을 훨씬 낮은 추론 비용으로 냈고, 신뢰도와 오차가 더 잘 맞았다.[^p3] | 1저자 Eunseo Choi, 마지막 저자 안희진 |
| 4 | 2026 | [Sampling-Based Safety Filter with Probabilistic Restrictiveness Guarantee](https://arxiv.org/abs/2604.22149) · IEEE Conference on Decision and Control (CDC), 채택 | 자율 시스템에서 안전은 꼭 필요하지만, 기본 제어기에 형식적인 안전 보장을 주기는 여전히 어렵다. 어떤 기본 제어 입력이든 안전하게 만드는 모듈형 샘플링 기반 안전 필터를 제안했다. 필터는 매 시간 단계마다 SV-MPC(Stein Variational Model Predictive Control)로 만든 제어열(앞으로 여러 시점에 넣을 제어 입력을 차례로 늘어놓은 것) 샘플로 기본 입력의 안전을 따진다. 이 방법은 안전 조건을 반영한 제어열의 사후 분포(조건을 반영해 고쳐 계산한 확률분포)를 근사해, 복잡하고 볼록하지 않은(영역 안 두 점을 잇는 선분이 영역 밖으로 나갈 수 있는) 환경에서 여러 갈래로 나뉜 안전 영역을 잡아낸다. 샘플한 제어열 후보가 모두 위험하다고 판단되면 기본 입력을 덮어써 안전을 보장하고, 시나리오 접근법(무작위로 뽑은 표본으로 문제를 풀고 그 결과가 성립할 확률을 보장하는 방법)으로 필터의 제한성(restrictiveness)에 대한 확률 보장을 준다. 단일 차량과 다중 차량의 충돌 회피 과제에서, 기본 제어기가 실패할 수 있는 장애물 많은 환경을 지나가는 데 효과가 있음을 보였다.[^p4] | 1저자 Junyoung Park, 마지막 저자 안희진 |
| 5 | 2025 | [Rethinking the Role of Infrastructure in Collaborative Perception](https://doi.org/10.1007/978-3-031-91813-1_14) · European Conference on Computer Vision Workshop (ECCVW) | 협력 인지(CP)는 자기 에이전트(정보를 받아 합치는 쪽)가 주변 차량과 인프라의 센서 정보를 받아 합쳐 인지 능력을 높이는 과정이다. 센서를 단 인프라가 필요한지 판단하려면 협력 인지에서 인프라 자료의 역할을 폭넓고 정량적으로 분석해야 하지만, 그런 분석은 아직 부족했다. 먼저 차량이 자기 에이전트인 기존 차량 중심 협력 인지에서 인프라 자료가 얼마나 중요한지 정량적으로 평가했다. 이어 인프라가 자기 에이전트인 인프라 중심 협력 인지를 차량 중심 협력 인지와 비교했다. 인프라 자료를 넣으면 3차원 물체 탐지 정확도가 최대 10.30% 높아졌고, 인프라 중심 협력 인지는 차량 중심 협력 인지에 비해 잡음에 강건했고 정확도가 최대 46.47% 높았다.[^p5] | 1저자 Hyunchul Bae, 마지막 저자 안희진 |
| 6 | 2026 | [A Decision Transformer for Generalizable Multi-Vehicle Coordination at Unsignalized Intersections](https://doi.org/10.1109/iv66570.2026.11623990) · IEEE Intelligent Vehicles Symposium (IV) | 신호등 없는 교차로에서 여러 차량을 조정하는 Decision Transformer 기반 방법을 제시했다. 기존 강화학습이나 최적화 기반 방법과 달리, 조정 문제를 순서 예측 문제로 세워 GPT(Generative Pre-trained Transformer, 앞선 자료로 다음 자료를 예측하도록 미리 학습하는 신경망 구조) 구조의 장점을 활용한다. 이 설계로 다양한 상황과 불확실한 교통 흐름에 맞춰 여러 차량의 최적 입력 순서를 만든다. 실험에서 기존 오프라인 강화학습과 GPT 기반 기준 방법보다 성공률이 높았다. 또 처음 보는 교차로 구조에도 잘 일반화되고 인식 잡음에도 강건함을 시뮬레이션과 실제 축소 테스트베드에서 확인했다.[^p6] | 1저자 Eunjae Lee, 마지막 저자 안희진 |
| 7 | 2024 | [Infrastructure-guided Optimal Spacing for Vehicles Approaching Intersections](https://doi.org/10.1109/iv55156.2024.10588708) · IEEE Intelligent Vehicles Symposium (IV) | 교차로 빨간불에 서는 일은 도심 교통에서 이동 시간 지연의 주요 원인 가운데 하나다. 운전자는 앞차에 될 수 있는 한 가까이 붙어 서는 경우가 많은데, 출발할 때 안전 거리를 확보하려고 기다려야 해서 지연이 더 생길 수 있다. 차량이 멈출 때 최적 간격을 유지하도록 안내하는 인프라 기반 최적 간격 시스템을 제시했다. 초록불로 바뀌면 모든 차량이 될 수 있는 한 빨리 교차로에 들어가도록 차량 사이의 최적 간격을 구하는 최적화 문제를 세우고, 이를 효율적으로 풀려고 두 대씩만 다루는 하위 문제로 나눠 차례로 풀었다. 시뮬레이션으로 이동 시간 지연을 줄이는 효과를 확인했다.[^p7] | 1저자 Yoojin Choi, 마지막 저자 안희진 |
| 8 | 2026 | [Miniature Testbed for Validating Multi-Agent Cooperative Autonomous Driving](https://doi.org/10.1109/icra57385.2026.11696666) · IEEE International Conference on Robotics and Automation (ICRA) | 협력 자율주행은 차량과 지능형 도로 인프라가 실시간으로 협력해 차량의 자율성을 넓히는 일로, 어렵지만 꼭 풀어야 할 문제다. 그런데 기존 테스트베드 가운데 센싱·엣지 컴퓨팅·통신 기능을 갖춘 지능형 인프라를 쓰는 곳이 없어, 협력 자율주행을 검증하는 1:15 축소 테스트베드 CIVAT을 설계하고 만들었다. 축소한 도시 지도, 센서를 단 자율주행차, 지능형 인프라로 이뤄진다. 공용 Wi-Fi와 ROS2(로봇 소프트웨어를 만드는 데 쓰는 공개 소프트웨어 틀) 위에서 발행-구독 방식(보내는 쪽이 주제별로 자료를 올리고 받는 쪽이 필요한 주제를 구독해 받는 방식)으로 V2V(차량 사이)·V2I(차량과 인프라 사이) 통신을 묶어, 차량과 인프라가 정보를 주고받으며 협력 주행을 하게 했다. 사례 연구로 인프라 기반 인지와 교차로 관리 실험에서 시스템을 검증했다.[^p8] | 1저자 Hyunchul Bae, 마지막 저자 안희진 |

## 교수와 전문 분야

안희진 교수는 서울대학교에서 학사(B.S., 2012)를, MIT에서 S.M.(2014)과 박사(Ph.D., 2018)를 받았다.[^team][^profile] 누리집 Profile 페이지의 경력 칸은 MERL Visiting Research Scientist(2018–2019), UBC ECE & CS Postdoctoral Research Fellow(2020–2022), Seoul National University ECE Assistant Professor(2022), KAIST EE Assistant Professor(2022–현재)를 적는다.[^profile] 첫 화면 소식은 교수가 2022년 7월 KAIST 전기및전자공학부(School of Electrical Engineering)에서 연구실을 시작했다고 적는다.[^home] 직위는 Profile 페이지가 Assistant Professor at KAIST로, Team 페이지가 Associate Professor at KAIST EE로, 전기및전자공학부 교수 소개가 부교수로 적는다.[^profile][^team][^ee] 전기및전자공학부 교수 소개는 교수의 주요 연구분야를 AI & Machine Learning, Robotics & Control, Big Data로, 디비전을 Signal로 적는다.[^ee]

Profile 페이지의 수상 칸은 ICROS 2024의 Outstanding Young Researcher Award와, KAIST EE의 Outstanding Lecture Award 두 번(2022년 가을 학기 EE688 Optimal Control Theory, 2023년 봄 학기 EE202 Signals and Systems)을 적는다.[^profile] 대외 활동 칸은 한국공학한림원 자율주행위원회 분과위원(2023–현재), 주행사업자추진협의회 위원(2025–현재), 국토교통부 자율주행자동차 시범운행지구 위원회 위원(2025–현재), 서울특별시 자율주행자동차 시범운행지구 운영위원회 위원(2025–현재), 제주 자율주행자동차 시범운행지구 운영위원회 위원(2024–현재)과, 28th ACM International Conference on Hybrid Systems: Computation and Control(2025)의 PC Member, IEEE Conference on Control Technology and Applications(CCTA) 2027의 D&I Co-Chair, IFAC World Congress 2026의 D&I Chair, IFAC Technical Committee 2.4 Optimal Control의 Member를 적는다.[^profile] 첫 화면 소식은 교수가 2024년 6월 IEEE IV Symposium Workshop에서 "Safe Autonomous Driving under Perception Uncertainties", 2024년 8월 8th IFAC Conference on Nonlinear Model Predictive Control에서 "Safety Guarantee in Learning-based Control"이라는 제목으로 기조 발표(keynote presentation)를 했고, 2025년 11월 ICCAS 2025에서 "Sampling-based Model Predictive Control" 튜토리얼 강연을 했다고 적는다.[^home]

Publications 페이지 「Before 2023」 구역(2014–2022년)의 논문 제목은 주로 교차로에서 차량 충돌을 막기 위한 안전 검증과 제어, 도달 가능성 분석(시스템이 앞으로 이를 수 있는 상태의 범위를 계산하는 방법)에 기반한 자율주행 의사결정, 여러 갈래(multimodal) 확률분포에 대한 안전한 운동 계획, 차량 인터넷(Internet of Vehicles)의 센서 선택과 엣지 컴퓨팅, 무선 네트워크 제어 시스템의 전송 일정 계획을 다룬다.[^pubs] KAIST 시기의 논문으로 보면 지금의 전문 분야는 두 갈래다. 첫째, 학습 기반 인식과 제어에 불확실성이 있을 때도 안전을 보장하는 제어다(대표 논문 1–4).[^p1][^p2][^p3][^p4] 둘째, 여러 차량과 도로 인프라가 정보를 나누며 협력하는 인지와 교차로 조정, 그리고 이를 검증하는 축소 테스트베드다(대표 논문 5–8).[^p5][^p6][^p7][^p8]

## 응용 분야

연구 페이지는 스마트 시티 테스트베드의 지능형 인프라가 차량과 정보를 계속 나누어 교통 흐름을 능동적으로 제어하고 협력 인지를 하는 미래 기술 개발에 쓰인다고 적는다.[^research] 대표 논문은 자율주행차의 안전한 운동 계획,[^p1][^p2] 신호등 없는 교차로의 다중 차량 조정과 교차로 앞 차량 간격 안내,[^p6][^p7] 협력 자율주행 검증용 테스트베드를 대상으로 한다.[^p8] 특허 목록에는 비신호 교차로의 차량 제어, 협력 인식 모듈의 병렬적 연결에 기초한 객체 탐지, 차량 간 추천 간격 산출, 인프라 중심 협동 인지 시스템을 통한 물체 탐지 정확도 증강에 관한 국내 출원이 있다.[^pubs] 졸업생 진로로는 RideFlux, Samsung Electronics, University of Maryland 박사과정이 적혀 있다.[^team]

## 구성원

2026년 10월 23일 랩 Team 페이지 기준이다. Researcher 칸의 박사후연구원 3명과 Graduate Students 칸의 박사과정 8명, 석사과정 4명이며, 과정은 카드 표기(Post doc, Ph.D. Student, M.S. Student)를 옮겼고 Eunjae Lee 카드의 Student Representative도 카드 표기다. 연구 주제는 카드의 Research Interest이고, 시작은 첫 화면 소식의 합류 글에 적힌 연월이다.[^team][^home] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Minhee Kang | 박사후연구원 | 2023-08 | Road Safety for CAVs with AI and V2X System | 5, 6, 7, 8 |
| Boseok Kim | 박사후연구원 |  | Model Predictive Control, Safety Filter |  |
| Anchita Dey | 박사후연구원 |  | Model predictive control, Nonlinear and adaptive control, Convex optimization, System identification |  |
| Yoojin Choi | 박사과정 | 2022-08 | Control Systems for Multi-Agent Coordination | 6, 7 |
| Hyunchul Bae | 박사과정 | 2023-02 | V2X Collaborative Perception | 5, 8 |
| Eunseo Choi | 박사과정 | 2023-02 | Model Confidence for Robust Learning-Based Control | 3 |
| Junyeop Kwon | 박사과정 | 2025-09 | Safe Learning-Based Control for Autonomous Driving, Latent World Model |  |
| Bon Jae Choe | 박사과정 | 2024-02 | Automated Valet Parking Systems, Planning and Scheduling |  |
| Eunjae Lee | 박사과정 (Student Representative) | 2023-08 | Reinforcement Learning for Vehicle Coordination | 6, 8 |
| Jehyeop Han | 박사과정 | 2024-02 | Sensor Selection | 8 |
| Nayeon Jung | 박사과정 | 2024-02 | Multi-Agent Systems, Game Theory |  |
| Minwoo Song | 석사과정 | 2025-02 | Collaborative Perception for Multi-Agent Systems | 5 |
| Hyeongchan Ham | 석사과정 | 2025-02 | AI safety | 1 |
| Seonho Yoo | 석사과정 |  | Safe Learning-Based Control, AI safety |  |
| Seungsu Kang | 석사과정 |  | AI safety |  |

## 졸업생과 이전 구성원

랩 Team 페이지 Alumni 칸의 4명이다. 학위와 연도는 랩 표기("MS 2026" 등)를 옮겼고, 진로는 "Now at"·"Now a" 뒤에 적힌 곳이다.[^team]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Sein Lee | M.S. (2026) | RideFlux |
| Kangyeon Kim | M.S. (2026) |  |
| Hyeontae Sung | M.S. (2024) | Ph.D. student at University of Maryland |
| Junyoung Park | M.S. (2027) | Samsung Electronics |

## 최근 논문 목록 (2021–2026)

랩 Publications 페이지 International 칸의 2023–2026년 구역 20편과 「Before 2023」 구역 가운데 2021–2022년에 나온 3편, Domestic 칸의 2024–2025년 국내 학회·학술지 글 13편이다. 연도는 페이지의 연도 구역이고(「Before 2023」 구역 항목은 서지에 적힌 연도), 제목·저자·학술지와 학회 이름은 랩 표기 그대로다. 이 목록은 교수 개인의 논문 목록이라, 교수가 KAIST에서 연구실을 시작한 2022년 7월 전에 출판된 논문(2021년 2편)도 들어 있다. 2026년 구역에서 「(채택)」을 붙인 7편은 첫 화면 소식이 채택(accepted)을 알린 학회 논문으로, 출판된 판의 서지(DOI)가 없는 것이다.[^pubs][^home]

**2026**

- Junyoung Park, Hyeontae Sung, Heejin Ahn. "Sampling-Based Safety Filter with Probabilistic Restrictiveness Guarantee". *IEEE Conference on Decision and Control (CDC), Hawaii, USA (채택)*.
- Kangyeon Kim, Seonho Yoo, Heejin Ahn. "Safety-Ensuring Offline Reinforcement Learning via Chance-Constrained Policy Filtering". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Pennsylvania, USA (채택)*.
- A. Colombo, A. Micheletti, Jehyeop Han, Heejin Ahn, M. Farina. "Self-localization by camera polling: a novel sensor scheduling problem". *IEEE International Conference on Intelligent Transportation Systems (ITSC), Naples, Italy (채택)*.
- Bon Choe, Minhee Kang, Heejin Ahn. "High-Density Automated Valet Parking with Relocation-Free Sequential Operations". *IEEE International Conference on Intelligent Transportation Systems (ITSC), Naples, Italy (채택)*.
- Hyeontae Sung, Hyeongchan Ham, Junyoung Park, Kai Ren, Heejin Ahn. "Probabilistic Recursively Feasible Motion Planning Under Uncertain Environments". *International Federation of Automatic Control World Congress (IFAC WC), Busan, Republic of Korea (채택)*.
- Jehyeop Han, Minhee Kang, A. Colombo, M. Farina, Heejin Ahn. "Knapsack-based Online Sensor Selection for Vehicle State Estimation". *International Federation of Automatic Control World Congress (IFAC WC), Busan, Republic of Korea (채택)*.
- Hyunchul Bae, Eunjae Lee, Jehyeop Han, Minhee Kang, Jaehyeon Kim, Junggeun Seo, Minkyun Noh, Heejin Ahn. "Miniature Testbed for Validating Multi-Agent Cooperative Autonomous Driving". *IEEE International Conference on Robotics and Automation (ICRA), Vienna, Austria, doi:10.1109/icra57385.2026.11696666*.
- Eunseo Choi, Ho-Yeon Kim, Jaewon Lee, Taeyong Jo, Myungjun Lee, Heejin Ahn. "Uncertainty Estimation via Hyperspherical Confidence Mapping". *International Conference on Learning Representations (ICLR), Rio de Janeiro, Brazil (채택)*.
- Eunjae Lee, Minhee Kang, Yoojin Choi, Heejin Ahn. "A Decision Transformer for Generalizable Multi-Vehicle Coordination at Unsignalized Intersections". *IEEE Intelligent Vehicles Symposium (IV), Detroit, MI, USA, doi:10.1109/iv66570.2026.11623990*.

**2025**

- Hyeongchan Ham, Heejin Ahn. "DRO-EDL-MPC: Evidential Deep Learning-Based Distributionally Robust Model Predictive Control for Safe Autonomous Driving". *IEEE Robotics and Automation Letters, Presented at ICRA 2026, doi:10.1109/lra.2026.3655206*.
- Taeho Oh, Eric Min Kim, Thanh-Tung Nguyen, Hyeonjun Jung, Yoojin Choi, Lucas Liebe, Seonmyeong Lee, Hanbin Jang, Gyounghoon Chun, Inhi Kim, Kitae Jang, Heejin Ahn, Dongsuk Kum, In Gwun Jang, Dongman Lee. "Scalable and Interoperable C-V2X Framework for Real-time Intelligent Decision Support in Autonomous Mobility". *Communications in Transportation Research, doi:10.26599/commtr.2026.9640001*.
- Minhee Kang, Yoojin Choi, Eunseo Choi, Heejin Ahn. "Shockwave Minimization within the Mesoscopic: Infrastructure-guided Optimal Acceleration for Autonomous Vehicle". *In Proc. IEEE International Conference on Intelligent Transportation Systems (ITSC), Nov. 2025, doi:10.1109/itsc60802.2025.11423175*.
- Beomjun Kim, Jaehwan Kim, Kangyeon Kim, Sunwoo Kim, Heejin Ahn. "A Computation-efficient Method of Measuring Dataset Quality based on the Coverage of the Dataset". *In Proc. International Conference on Artificial Intelligence and Statistics (AISTATS), May. 2025*.
- Jongseok Kim, Seongil Kim, Duck-Su Lee, Heejin Ahn, Ki-Bum Park. "MW-rated Induction Motor Control equipped with Fault-Ride-Through Capability for an Electric Propulsion Ship using Model Predictive Control". *In Proc. IEEE Energy Conversion Congress and Exposition (ECCE), Oct. 2025, doi:10.1109/ecce55643.2024.10861477*.
- Junyoung Park, Hyeontae Sung, Heejin Ahn. "제어 장벽 함수를 이용한 샘플링 기반 안전 필터 연구". *한국통신학회 인공지능 학술대회 논문집, 제주 (국내)*.
- Hyeongchan Ham, Heejin Ahn. "시각 정보를 이용한 3DGS 기반 안전 경로 계획". *한국통신학회 인공지능 학술대회 논문집, 제주 (국내)*.
- Eunjae Lee, Minhee Kang, Yoojin Choi, Heejin Ahn. "비신호 교차로 다중 차량 제어를 위한 GPT 기반 Decision Transformer 연구". *제어로봇시스템학회 국내학술대회 논문집, 전북 (국내)*.
- Jehyeop Han, Junggeun Seo, Jaehyeon Kim, Hyunchul Bae, Eunjae Lee, Minkyun Noh, Heejin Ahn. "도심 자율주행 기술 검증을 위한 1:15 스케일 테스트베드 개발 Part I : 다중 차량 시스템 설계 및 적용". *제어로봇시스템학회 국내학술대회 논문집, 전북 (국내)*.
- Minhee Kang, Eunjae Lee, Yoojin Choii, Heejin Ahn. "차량 간 통신 기반 비신호교차로 내 협력형 자율주행차량 전략 개발". *한국자동차공학회 춘계학술대회, 제주 (국내)*.
- Hyeongchan Ham, Heejin Ahn. "안전한 자율 로봇 제어를 위한 모델 예측 제어와 강화 학습 기술 개발 동향 및 사례 분석". *제어로봇시스템학회지, 31(1), 6-12 (국내)*.
- Hyeongchan Ham, Heejin Ahn. "안전한 모델 예측 제어와 강화 학습에 대한 연구 동향". *제어로봇시스템학회 논문지, 31(2), 87-97 (국내)*.
- Heejin Ahn. "특집호 서문: 학습 기반 모델 예측 제어". *제어로봇시스템학회 논문지, 31(2), 77-77. 10.5302/J.ICROS.2025.25.9001 (국내)*.

**2024**

- Kai Ren, Colin Chen, Hyeontae Sung, Heejin Ahn, Ian Mitchell, Maryam Kamgarpour. "Recursively Feasible Chance-constrained Model Predictive Control under Gaussian Mixture Model Uncertainty". *IEEE Transactions on Control Systems Technology (Early Access), Nov. 2024*.
- Hyunchul Bae, Minhee Kang, Minwoo Song, Heejin Ahn. "Rethinking the Role of Infrastructure in Collaborative Perception". *In Proc. European Conference on Computer Vision Workshop (ECCVW) [oral], Sep. 2024*.
- Yoojin Choi, Minhee Kang, Heejin Ahn. "Infrastructure-guided Optimal Spacing for Vehicles Approaching Intersections". *In Proc. IEEE Intelligent Vehicles Symposium (IV), June 2024*.
- Y. Wang, E. Hansen, H. Ahn. "Hierarchical planning for autonomous parking in dynamic environments". *IEEE Transactions on Control Systems Technology, vol. 32, no. 4, pp. 1386-1398, July 2024*.
- Hyeontae Sung, Eunseo Choi, Heejin Ahn. "Optimal Acceleration Profiles of Multiple Vehicles Using Model Predictive Control". *제어로봇시스템학회 국내학술대회 논문집, 대전 (국내)*.
- Hyeontae Sung, Kangyeon Kim, Heejin Ahn. "Computation Analysis on Safe Chance-constrained Model Predictive Control under Gaussian Mixture Uncertainty". *제어로봇시스템학회 국내학술대회 논문집, 대전 (국내)*.
- Hyunchul Bae, Eunjae Lee, Sein Lee, Jehyeop Han, Heejin Ahn. "도심 자율주행 기술 검증을 위한 소형 테스트베드". *한국 ITS 학회 학술대회, 804-808 (국내)*.
- Yoojin Choi, Heejin Ahn. "예약 기반 교차로 제어 시스템에 횡단보도의 영향의 분석". *한국 ITS 학회 학술대회, 76-79 (국내)*.
- Eunjae Lee, Hyunchul Bae, Sein Lee, Heejin Ahn. "Model Predictive Control 기반 1:15 scale RC car 의 경로 추종 성능 향상". *한국 ITS 학회 학술대회, 405-409 (국내)*.

**2023**

- Beomjun Kim, Heejin Ahn. "Chance-Constrained Control with Imperfect Perception Modules". *In Proc. American Control Conference (ACC), June 2023, pp. 2568-2573*.
- K. Ren, H. Ahn, M. Kamgarpour. "Chance-constrained trajectory planning with multimodal environmental uncertainty". *IEEE Control Systems Letters, vol. 7, pp. 13-18, 2023. (Presented at IEEE Conference on Decision and Control)*.

**2022**

- Y. Ma, J. Guo, Y. Wang, A. Chakrabarty, H. Ahn, P. Orlik, C. Lu. "Optimal dynamic transmission scheduling for wireless networked control systems". *IEEE Transactions on Control Systems Technology, vol. 30, no. 6, pp. 2360-2376, Nov. 2022*.

**2021**

- H. Ahn, C. Chen, I. M. Mitchell, M. Kamgarpour. "Safe motion planning against multimodal distributions based on a scenario approach". *IEEE Control Systems Letters, vol.6, pp. 1142-1147, June 2021. (Presented at IEEE Conference on Decision and Control)*.
- H. Ahn, K. Berntorp, P. Inani, A. Ram, S. Di Cairano. "Reachability-based decision making for autonomous driving: Theory and experiment". *IEEE Transactions on Control Systems Technology, vol. 29, no. 5, pp. 1907-1921, Sep. 2021*.

## 특허

랩 Publications 페이지 Patents 칸 9건 가운데 2024–2025년에 출원한 국내 특허 4건이다. 제목·발명자·출원번호는 랩 표기 그대로다.[^pubs]

- 2025-11-25 · 비신호 교차로에서의 차량 제어 방법, 비신호 교차로에서의 차량 제어를 위해 인공신경망을 학습시키는 방법 (국가 대한민국; 출원번호 10-2025-0180258; 발명자 Heejin Ahn, Eunjae Lee, Minhee Kang, Yoojin Choi)
- 2024-11-15 · 협력 인식 모듈의 병렬적 연결에 기초하여 객체를 탐지하는 방법 및 장치 (국가 대한민국; 출원번호 10-2024-0163570; 발명자 Heejin Ahn, Hyunchul Bae, Minhee Kang)
- 2024-11-15 · 차량간 추천 간격 산출 방법 및 이를 수행하기 위한 컴퓨팅 장치 (국가 대한민국; 출원번호 10-2024-0163174; 발명자 Heejin Ahn, Yoojin Choi, Minhee Kang, Youngki Kim)
- 2024-11-12 · 인프라 중심의 협동 인지 시스템을 통한 물체 탐지 정확도 증강 방법 및 시스템 (국가 대한민국; 출원번호 10-2024-0160273; 발명자 Heejin Ahn, Hyunchul Bae, Minhee Kang, Minwoo Song)

## 수상

첫 화면 소식의 수상 글 11건(2022년 12월–2026년 9월)과, Publications 페이지가 ECCE 논문 항목 끝에 함께 적은 수상 1건이다. 문구는 누리집 표기 그대로이고, 마지막 항목은 페이지에 수상 날짜가 적혀 있지 않다.[^home][^pubs]

- 2026-09 · Hyeongchan has been selected as a Next-Generation Engineering Researcher supported by IPESK.
- 2026-08 · Bon receives the Encouragement Prize at the 2026 IEEE ITSS Society Korea Chapter Student 3MT Competition.
- 2025-12 · Hyeongchan and Eunjae receive the Excellence Award at the miliTECH Challenge 2025.
- 2025-12 · Seonho, Kangyeon, and Prof. Ahn receive the Best Paper Award at ICROS Daejeon–Chungcheong Regional Conference 2025.
- 2025-09 · Hyeongchan Ham, Eunjae Lee, and Prof. Ahn receive the Best Paper Award at Korea AI Conference 2025.
- 2025-08 · Nayeon Jung and Prof. Ahn receive the Best Poster Award at BIEN 2025.
- 2025-08 · Hyeongchan Ham and Prof. Ahn receive the Outstanding Poster Award at BIEN 2025.
- 2024-07 · Prof. Ahn receives the Outstanding Young Researcher Award at ICROS 2024.
- 2024-07 · Hyeontae Sung, Kangyeon Kim, and Prof. Ahn receive the Best Paper Award at ICROS 2024.
- 2023-06 · Prof. Ahn receives the Outstanding Lecture Award for "EE202 Signals and Systems".
- 2022-12 · Prof. Ahn receives the Outstanding Lecture Award for "EE688 Optimal Control Theory".
- Third Paper Award by Industrial Drives Committee (Publications 페이지 IEEE Energy Conversion Congress and Exposition (ECCE) 논문 「MW-rated Induction Motor Control equipped with Fault-Ride-Through Capability for an Electric Propulsion Ship using Model Predictive Control」 항목, 날짜 없음)

## 소식

첫 화면 CIS News의 2022년 7월–2026년 10월 글 가운데 논문 소식 18건, 강연·학술 활동 11건, 연구실 시작 소식 1건으로 모두 30건이다. 날짜는 글의 연월이고 문구는 누리집 표기 그대로다.[^home]

- 2026-10 · Minwoo and Minhee's paper is accepted to WACV, Buena Vista, Florida, USA.
- 2026-07 · Junyoung and Hyeontae's paper is accepted to CDC, Honolulu, Hawaii, USA.
- 2026-07 · Hyeongchan, Boseok, and Minwoo's paper is accepted to RSS Workshop, Sydney, Australia.
- 2026-06 · Kangyeon and Seonho's paper is accepted to IROS, Pennsylvania, USA.
- 2026-05 · Jehyeop's paper is accepted to ITSC, Naples, Italy.
- 2026-05 · Bon's paper is accepted to ITSC, Naples, Italy.
- 2026-05 · Hyeontae's paper is accepted to IFAC World Congress, Busan, Republic of Korea.
- 2026-05 · Jehyeop's paper is accepted to the IFAC World Congress, Busan, Republic of Korea
- 2026-01 · Hyunchul, Eunjae, and Jehyeop's paper is accepted to ICRA, Vienna, Austria.
- 2026-01 · Eunseo's paper is accepted to ICLR, Rio de Janeiro, Brazil.
- 2026-01 · Eunjae's paper is accepted to IV, Detroit, MI, USA.
- 2025-12 · Hyeongchan's paper is accepted to the IEEE Robotics and Automation Letters (RA-L).
- 2025-11 · Prof. Ahn gives a tutorial talk entitled "Sampling-based Model Predictive Control" at ICCAS 2025.
- 2025-07 · Minhee's paper is accepted to the IEEE International Conference on Intelligent Transportation Systems (ITSC), Gold Coast, Australia.
- 2025-05 · Prof. Ahn gives a talk at the Women in Engineering Session at the Korean Society of Automotive Engineers 2025 Annual Spring Conference.
- 2025-04 · Prof. Ahn gives a talk at 2025 KAIST-Hwaseong Science Hub Program.
- 2025-04 · Prof. Ahn gives a talk at KAIST Cho Chun Shik Graduate School of Mobility Colloquium.
- 2024-12 · Prof. Ahn gives a talk at 2024 Brainlink Conference on Urban Transport Infrastructure.
- 2024-11 · Prof. Ahn participates in the MIT EECS Academic Job Search Seminar as a panelist (invited by Prof. Saman Amarasinghe).
- 2024-11 · Prof. Ahn gives a talk at the UNIST ME Colloquium.
- 2024-11 · Prof. Ahn gives a talk at the DGIST EECS Colloquium.
- 2024-09 · Prof. Ahn gives a tutorial talk at the 5th Korea Artificial Intelligence Conference.
- 2024-09 · Hyeontae's paper is accepted to the IEEE Transactions on Control Systems Technology.
- 2024-09 · Hyunchul's paper is accepted to the European Conference on Computer Vision Workshop (ECCVW), Milan, Italy.
- 2024-08 · Prof. Ahn gives a keynote presentation entitled "Safety Guarantee in Learning-based Control" at the 8th IFAC Conference on Nonlinear Model Predictive Control.
- 2024-06 · Prof. Ahn gives a keynote presentation entitled "Safe Autonomous Driving under Perception Uncertainties" at IEEE IV Symposium Workshop.
- 2024-06 · Yoojin's paper is accepted to the IEEE Intelligent Vehicles (IV) Symposium, Jeju, Korea.
- 2024-02 · One paper is accepted to the IEEE Transactions on Control Systems Technology.
- 2023-07 · One paper is accepted to the American Control Conference (ACC), San Diego, USA.
- 2022-07 · Prof. Ahn starts CIS at KAIST, School of Electrical Engineering.

## 연락과 위치

- 주소: School of Electrical Engineering, KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea[^contact]
- 교수 연구실(PI Office): E3-2 3235, 전화 +82(042) 350-7471[^contact]
- 학생 연구실: Student Office 1 E3-2 3240(전화 +82(042) 350-7571), Student Office 2 E3-2 3246[^contact]
- 교수 이메일: heejin.ahn@kaist.ac.kr[^ee][^profile]
[^home]: 연구실 누리집 첫 화면 <https://cis.kaist.ac.kr/> (소개 문구와 CIS News 2022–2026, 2026-10-23 열람)
[^team]: Team 페이지 <https://cis.kaist.ac.kr/team> (Principal Investigator, Researcher, Graduate Students, Alumni 칸, 2026-10-23 열람)
[^research]: Research 페이지 <https://cis.kaist.ac.kr/research> (Safe Intelligence, Collaborative Intelligence, Smart city testbed 칸, 2026-10-23 열람)
[^pubs]: Publications 페이지 <https://cis.kaist.ac.kr/publications> (Preprints, International, Domestic, Patents 칸, 2026-10-23 열람)
[^contact]: Contact 페이지 <https://cis.kaist.ac.kr/contact> (2026-10-23 열람)
[^profile]: 교수 Profile 페이지 <https://cis.kaist.ac.kr/profileheejin-ahn> (Education, Experience, Awards & Honors, Professional Activities, 2026-10-23 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(안희진) <https://ee.kaist.ac.kr/professor/%ec%95%88%ed%9d%ac%ec%a7%84/> (2026-10-23 열람)
[^gst]: KAIST 안보과학기술대학원 교수 명단 3쪽 <https://gst.kaist.ac.kr/member/faculty/?page=3> (2026-10-23 열람)
[^p1]: H. Ham, H. Ahn, IEEE Robotics and Automation Letters 11, 3015-3022 (2026). <https://doi.org/10.1109/lra.2026.3655206> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: B. Kim, H. Ahn, 2023 American Control Conference (ACC), 2568-2573 (2023). <https://doi.org/10.23919/acc55779.2023.10155868> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: E. Choi 외, H. Ahn, International Conference on Learning Representations (ICLR), Rio de Janeiro, Brazil (채택) (2026). <https://arxiv.org/abs/2605.05964> 초록 기준(arXiv 판).
[^p4]: J. Park, H. Sung, H. Ahn, IEEE Conference on Decision and Control (CDC), Hawaii, USA (채택) (2026). <https://arxiv.org/abs/2604.22149> 초록 기준(arXiv 판).
[^p5]: H. Bae, M. Kang, M. Song, H. Ahn, Lecture Notes in Computer Science, 212-227 (온라인 2025-05-12). <https://doi.org/10.1007/978-3-031-91813-1_14> 초록 기준(같은 제목의 arXiv 판 <https://arxiv.org/abs/2410.11259>).
[^p6]: E. Lee, M. Kang, Y. Choi, H. Ahn, 2026 IEEE Intelligent Vehicles Symposium (IV), 1273-1278 (2026). <https://doi.org/10.1109/iv66570.2026.11623990> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: Y. Choi, M. Kang, H. Ahn, 2024 IEEE Intelligent Vehicles Symposium (IV), 1615-1620 (2024). <https://doi.org/10.1109/iv55156.2024.10588708> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: H. Bae 외, H. Ahn, 2026 IEEE International Conference on Robotics and Automation (ICRA), 6693-6700 (2026). <https://doi.org/10.1109/icra57385.2026.11696666> 초록 기준(같은 제목의 arXiv 판 <https://arxiv.org/abs/2511.11022>).

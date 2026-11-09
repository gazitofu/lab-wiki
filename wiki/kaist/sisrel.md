# 스마트 정보 시스템 연구실 (Smart Information Systems Research Lab., SISReL)

**KAIST 전기및전자공학부 · 성영철 교수**

- 분야: 강화학습의 이론과 알고리즘, 다중 과제·다목적·다중 에이전트 학습, 대형 언어 모델의 추론과 로봇의 행동 학습[^intro][^research]
- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 강화학습[^intro][^research], 대형 언어 모델[^research], 보행·휴머노이드 로봇[^robot]
- 홈페이지: <https://sites.google.com/view/sisrelkaist>
- 근거와 출처: [스마트 정보 시스템 연구실 근거 페이지](sisrel-sources.md)

> 행동의 결과에서 배우는 강화학습을 중심으로, 여러 과제와 목표를 함께 다루는 학습 이론·알고리즘을 만들고 언어 모델의 판단과 로봇의 움직임으로 연결하는 연구실이다.[^intro][^research]

## 무엇을 연구하나

스마트 정보 시스템 연구실은 강화학습(reinforcement learning, RL: 행동 뒤에 주어지는 평가값의 누적을 크게 하도록 시행착오로 행동을 배우는 방법)을 연구한다.[^intro][^research] 확률론(불확실한 사건이 일어날 가능성을 수학적으로 다루는 분야), 통계학(자료를 모으고 분석해 대상의 특성을 추론하는 분야), 기하학(도형과 공간의 성질을 다루는 수학 분야), 최적화(주어진 조건 안에서 목적에 가장 맞는 값을 찾는 계산)를 이론적 바탕으로 삼고, 2016년부터 강화학습에 집중해 왔다. 연구 대상은 행동을 정하는 정책(주어진 상태나 관측에 따라 어떤 행동을 할지 정하는 규칙)을 어떻게 학습하고 평가하며 새로운 상황에 적용할지다. 연구 소개는 탐색(아직 해 보지 않은 행동을 시험해 정보를 얻는 일), 보상(학습 주체의 행동 결과에 주어지는 평가값)이 드문 환경, 이미 기록된 경험을 이용하는 학습, 여러 과제와 목표, 여러 학습 주체의 협력을 주요 갈래로 든다.[^intro][^research]

첫째 축은 제한된 경험과 관측으로 행동을 배우는 방법이다. 오프라인 강화학습(환경과 새로 상호작용하지 않고 미리 모은 경험 자료로 행동 규칙을 배우는 방법)에서는 기록된 경험을 조합하는 능력과 학습의 안정성을 함께 다룬다. 대표 논문 5는 행동의 장기적 평가를 이용하는 계산과 경험의 성과를 조건으로 행동을 배우는 방법을 결합했다. 대표 논문 6은 관측 자료의 항목 일부가 빠졌다는 정보를 학습 모형에 넣어 불완전한 관측에서 행동을 정하도록 했고, 대표 논문 8은 여러 시점의 자료를 묶어 다음 묶음에 필요한 정보를 넘기는 학습 구조를 제안했다.[^p5][^p6][^p8]

둘째 축은 여러 과제와 목표, 여러 행동 주체를 함께 다루는 학습이다. 보상의 분포(어떤 값들이 각각 어느 정도 나타나는지를 표현한 것)가 과제마다 다르면 학습이 한쪽으로 치우칠 수 있다. 대표 논문 2는 과제별 보상의 크기를 학습 이력에 따라 조절하고 학습 모형을 주기적으로 초기화하는 방법을 제안했다. 대표 논문 4는 여러 목표 중 성과가 가장 낮은 목표를 높이는 문제를 수학적으로 정리하고 반복 계산의 마지막 결과가 목표한 값에 가까워짐을 분석했다. 대표 논문 1은 함께 행동하는 주체마다 행동의 이득을 추정해 협력과 경험 활용의 효율을 개선하는 방법을 다뤘다.[^p2][^p4][^p1]

셋째 축은 대형 언어 모델(large language model, LLM: 많은 글을 학습해 언어를 이해하고 생성하는 큰 인공지능 모형)과 로봇이다. 연구실은 대형 언어 모델에 기반한 에이전트(agent: 주변 정보를 바탕으로 행동을 선택해 목표를 수행하는 주체)의 추론과 긴 작업의 계획을 연구한다.[^research] 대표 논문 3의 ReflAct는 언어 모델 에이전트가 다음 행동만 계획하는 대신 현재 상태와 목표의 관계를 계속 되짚게 하는 방법이다.[^p3] 로봇에서는 시각-언어-행동 모델(vision-language-action model, VLA: 시각 정보와 언어 지시를 받아 행동을 정하는 인공지능 모형)과 강화학습으로 다양한 움직임을 학습하며, POSCO와 로보티즈 AI Worker 휴머노이드(사람의 몸 형태를 본뜬 로봇)를 이용한 연구를 진행한다.[^research][^robot]

무선 통신(기기 사이의 선 연결 없이 공간에 퍼지는 전기적 진동으로 정보를 주고받는 통신)도 교수의 연구 관심에 포함된다. 대표 논문 7은 신호(정보를 나타내는 물리량의 변화)가 송신기에서 수신기로 바로 도달하는 경로와 반사면을 거치는 경로를 함께 추정하는 방법을 제안했다. 반사면과 송수신 부품의 규칙적인 배열, 전달 경로가 드문 특성을 이용해 두 단계로 추정하고, 반사면 부품의 불완전성 등 실제 구현에서 생기는 문제도 다뤘다.[^pi][^p7]

## 주요 연구 주제

### 기록된 경험과 불완전한 관측에서 배우기

연구실은 오프라인 강화학습과 모방학습(전문가의 행동 예시에서 행동 규칙을 배우는 방법), 환경 변화에 대한 적응을 연구한다. 대표 논문 5는 기록 속 경험을 이어 활용하도록 행동의 장기적 평가를 학습에 보탰다. 대표 논문 6과 8은 각각 관측 항목이 빠지는 경우와 현재 관측만으로 전체 상황을 알 수 없는 경우를 다룬다.[^research][^p5][^p6][^p8]

### 다중 과제와 다목적 학습

서로 다른 과제를 한 모형으로 배우는 다중 과제 강화학습과, 상충할 수 있는 여러 목표를 함께 고려하는 다목적 강화학습을 연구한다. 과제별 보상 분포를 조절하는 학습 방법과 목표들 사이에서 가장 낮은 성과를 높이는 방법을 개발하며, 학습 과정의 안정성과 수학적 성질을 함께 분석한다.[^research][^p2][^p4]

### 여러 행동 주체의 협력

연구실은 다중 에이전트 강화학습을 주요 연구 갈래로 삼는다. 대표 논문 1은 공동 행동의 결과에서 각 주체의 행동이 기여한 정도를 추정하는 방법을 제안한다. 다른 주체의 학습 때문에 상황이 달라지는 문제와 각 주체 자신의 행동 규칙이 바뀌는 문제를 함께 고려해, 과거 경험을 활용하면서 협력을 배우도록 했다.[^research][^p1]

### 언어 모델의 판단과 휴머노이드 제어

연구실은 언어 모델 에이전트의 과제 중심 추론, 긴 작업의 계획, 로봇의 행동 학습을 연구한다. ReflAct는 에이전트의 현재 상태와 목표가 어긋나는 문제를 지속적인 되짚기로 다루며, 휴머노이드 연구는 여러 작업에 공통으로 쓸 행동 규칙과 계획부터 개별 움직임을 정하는 제어까지 다룬다.[^research][^p3][^robot]

## 대표 논문

KAIST 재직 시기의 최근 논문 가운데 연구 갈래를 고르게 보여 주는 8편이다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 주요 저자의 교신 표시는 연구실의 논문 목록 표기를 따른다.[^journals]

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Generalized Per-Agent Advantage Estimation for Multi-Agent Policy Optimization](https://doi.org/10.65109/obia4073) · AAMAS | 협력하는 행동 주체마다 행동의 이득을 추정하는 방법을 제안했다. 행동 확률을 이용한 계산과 과거 경험의 반영 비율 조절을 결합해, 각 주체의 기여를 구분하고 협력과 학습 효율을 높였다.[^p1] | 1저자 Seongmin Kim, 마지막 저자 성영철 |
| 2 | 2025 | [ARS: Adaptive Reward Scaling for Multi-Task Reinforcement Learning](https://proceedings.mlr.press/v267/cho25d.html) · ICML | 과제마다 보상 분포가 달라 학습이 어려운 문제를 다룬다. 학습 이력에 따라 보상 크기를 조절하고 학습 모형을 주기적으로 초기화해 과제 간 균형과 학습의 안정성을 높였다.[^p2] | 1저자 Myungsik Cho, 교신저자 성영철 |
| 3 | 2025 | [ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection](https://doi.org/10.18653/v1/2025.emnlp-main.1697) · EMNLP | 언어 모델 에이전트가 상황과 맞지 않는 생각을 이어 가는 문제를 다룬다. 다음 행동만 계획하는 대신 현재 상태와 목표의 관계를 계속 되짚게 해 의사결정의 신뢰성을 높였다.[^p3] | 1저자 Jeonghye Kim·Sojeong Rhee(공동 기여), 공동 교신저자 성영철·Kyomin Jung |
| 4 | 2025 | [Multi-Objective Reinforcement Learning with Max-Min Criterion: A Game-Theoretic Approach](https://doi.org/10.52202/085713-2847) · NeurIPS | 여러 목표 가운데 성과가 가장 낮은 목표를 높이는 학습 문제를 게임 이론으로 정리했다. 행동 규칙을 갱신하는 계산을 단순화하고 반복 계산의 마지막 결과가 목표한 값에 가까워짐을 분석했으며 실험으로 학습 성능을 평가했다.[^p4] | 1저자 Woohyeon Byeon, 교신저자 성영철 |
| 5 | 2024 | [Adaptive Q-Aid for Conditional Supervised Learning in Offline Reinforcement Learning](https://doi.org/10.52202/079017-2764) · NeurIPS | 미리 모은 행동 기록을 조합해 활용하는 능력과 학습의 안정성을 함께 얻으려는 방법이다. 기록의 성과에 따라 행동의 장기적 평가를 학습에 보태는 정도를 조절했다.[^p5] | 1저자 Jeonghye Kim, 교신저자 성영철 |
| 6 | 2024 | [Robust Reinforcement Learning under Dimension-Wise State Information Drop](https://doi.org/10.1109/access.2024.3462803) · IEEE Access | 관측 자료의 일부 항목이 빠지는 상황에서도 행동을 정하도록, 어떤 항목이 빠졌는지를 나타내는 정보를 학습 구조에 넣었다. 불완전한 관측을 다루는 성능을 기존 방법과 비교했다.[^p6] | 1저자 Gyeongmin Kim, 교신저자 성영철 |
| 7 | 2023 | [Joint Direct and Indirect Channel Estimation for RIS-Assisted Millimeter-Wave Systems Based on Array Signal Processing](https://doi.org/10.1109/twc.2023.3262492) · IEEE Transactions on Wireless Communications | 송수신기 사이의 직접 경로와 반사면을 거치는 경로를 함께 추정하는 방법이다. 부품 배열의 규칙성과 드문 전달 경로를 이용하는 계산을 제안하고 실제 부품의 불완전성 등도 다뤘다.[^p7] | 1저자 Song Noh, 공저자 성영철 |
| 8 | 2022 | [Blockwise Sequential Model Learning for Partially Observable Reinforcement Learning](https://doi.org/10.1609/aaai.v36i7.20764) · AAAI | 현재의 관측만으로 전체 상황을 알 수 없는 문제를 다룬다. 여러 시점의 자료를 묶음별로 학습하고 다음 묶음에 필요한 정보를 넘기는 구조를 만들어, 불완전한 관측에서 행동을 배우도록 했다.[^p8] | 1저자 Giseung Park, 교신저자 성영철 |

## 교수와 전문 분야

성영철 교수는 서울대학교 전자공학과에서 학사와 석사 학위를, 2005년 Cornell University 전기및컴퓨터공학 분야에서 박사 학위를 받았다. Qualcomm의 연구개발 조직에서 무선 통신과 모뎀 설계를 연구한 뒤 2007년 2월 KAIST에 조교수로 부임했으며, 2010년 3월 부교수, 2018년 9월 교수로 재직하기 시작했다.[^intro][^pi] 전기및전자공학부 교수 소개는 주요 연구를 강화학습과 인공지능 에이전트로 적는다.[^dept]

교수 개인 소개의 연구 관심은 강화학습, 통계적 신호 처리(우연한 변동을 포함한 관측 자료에서 정보를 추정하고 판단하는 방법), 무선 통신이다.[^pi] 최근 논문으로 보면 전문 분야는 기록된 경험과 불완전한 관측을 이용한 학습, 여러 과제·목표·행동 주체를 함께 다루는 학습 이론과 알고리즘, 언어 모델 에이전트의 판단으로 이어진다. 통신에서는 직접·반사 전달 경로를 추정하는 방법을 연구했다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

연구실은 강화학습의 응용 대상으로 인공지능 로봇, 스마트 공장, 대형 언어 모델과 스스로 과제를 수행하는 인공지능을 든다. 국가 인공지능 연구 거점 사업의 로봇 기반 모형 연구에 참여하고, POSCO와 휴머노이드의 작업 계획·행동 규칙·움직임 제어를 연구한다.[^research][^robot] 과제 목록에는 자율 드론을 위한 과제 중심 강화학습, 스마트 도시의 분산 교통 관리, 재난 대응, 기기 가까이에 둔 계산 자원의 운영 최적화도 있다.[^research]

## 구성원

2026년 11월 9일 연구실 Members 쪽의 교수 외 구성원 14명이다. 박사후연구원 1명, 박사과정 11명, 석사과정 2명이며, 이름·과정·연구 주제는 해당 쪽의 표기다.[^members] 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Myungsik Cho | 박사후연구원 | Reinforcement Learning; Multi-Task Learning; Vision Language Action Models | 2 |
| Jongeui Park | 박사과정 | Offline Reinforcement Learning; Vision Language Action Models | 2 |
| Sungho Choi | 박사과정 | Reinforcement Learning; Imitation Learning | 8 |
| JongSeong Chae | 박사과정 | Reinforcement Learning; Imitation Learning |  |
| Jiwon Jeon | 박사과정 | Multi-Agent Systems; RL for LLMs; LLM Reasoning and Agents | 1 |
| Seongmin Kim | 박사과정 | Reinforcement Learning; Multi-Agent Systems; LLM-aided RL | 1 |
| Jeonghye Kim | 박사과정 | Offline Reinforcement Learning; RL for LLMs; LLM Reasoning and Agents | 2, 3, 5, 6 |
| Yongjae Shin | 박사과정 | Offline Reinforcement Learning; Multimodal Reinforcement Learning; Vision Language Action Models |  |
| Woohyeon Byeon | 박사과정 | Reinforcement Learning and Game; LLM Reasoning and Agents | 4 |
| Gyeongmin Kim | 박사과정 | Robust Reinforcement Learning; Offline Reinforcement Learning | 6 |
| JeongWoo Park | 박사과정 | Multimodal Reinforcement Learning; Vision Language Action Models; Motion Planning |  |
| Sojeong Rhee | 박사과정 | RL for LLMs; LLM Reasoning and Agents | 3 |
| Byeonguk Kim | 석사과정 | Agentic Robots |  |
| DongGyu Kim | 석사과정 | Agentic Robots |  |

## 졸업생 진로

Members 쪽의 박사 학위 기록 16건과 석사 학위 기록 33건이다. 같은 사람이 석사와 박사 양쪽에 적힌 경우 각 학위 기록을 유지했으며, 현재 구성원인 사람의 과거 학위도 포함한다. 학위 연월과 진로는 연구실의 표기다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jowoon Chong | 박사 (2009.08) | Associate Professor, Sungkyunkwan University (Formerly, Tenured Associate Professor at Texas Tech, TX) |
| Heejung Yu | 박사 (2011.02) | Professor, Korea University Sejong Campus |
| Haksoo Kim | 박사 (2013.02) | National Security Research Institute (NSRI) |
| Cheulsoon Kim | 박사 (2013.02) | ETRI |
| Juho Park | 박사 (2013.08) | ETRI |
| Donggun Kim | 박사 (2015.08) | Samsung Electronics |
| Gilwon Lee | 박사 (2016.08) | Samsung Research America (Formerly, Intel, Santa Clara, CA, Software Engineer) |
| Junyeong Seo | 박사 (2018.08) | Samsung Electronics, Modem design team |
| Jungho So | 박사 (2018.08) | Samsung Electronics, Modem design team |
| Sohee Bae | 박사 (2021.08) | CEO of SayBerryGames, Inc. |
| Seungyul Han | 박사 (2021.08) | Associate Professor, AI Graduate School, UNIST |
| Whiyoung Jung | 박사 (2022.08) | LG AI Research |
| Woojun Kim | 박사 (2023.02) | Assistant Professor, Dept. of Industrial & Systems Engineering, KAIST |
| Suyoung Lee | 박사 (2024.02) | Gameplay AI Team, Krafton |
| Giseung Park | 박사 (2024.08) | Postdoc at Robot Vision and Learning Lab. Dept. of Computer Science, University of Toronto |
| Myungsik Cho | 박사 (2025.08) | Postdoc, SISReL KAIST |
| Haksoo Kim | 석사 (2008.02) | National Security Research Institute (NSRI) |
| Song Noh | 석사 (2010.02) | Associate Professor, Incheon National University (Formerly, System Engineer at Intel, Hillsboro, OR) |
| Yirang Lim | 석사 (2010.02) | Fintech Product Owner (PO), Coupang Pay |
| Junse Lee | 석사 (2011.02) | Assistant Professor, Sungshin Women's University |
| Bora Lim | 석사 (2011.02) | Samsung Electronics |
| Yuni Lee | 석사 (2011.08) |  |
| Gilwon Lee | 석사 (2012.02) | Samsung Research America |
| Jungho So | 석사 (2013.02) | Samsung Electronics |
| Junyeong Seo | 석사 (2013.02) | Samsung Electronics |
| Jihoon Chung | 석사 (2014.02) | WorldQuant |
| Sangwoon Kwak | 석사 (2014.02) | ETRI |
| Gwonhan Mun | 석사 (2015.02) | ETRI |
| Yongjin Kwon | 석사 (2016.02) | ADD |
| Seungyul Han | 석사 (2016.02) | Associate Professor, AI Graduate School, UNIST with PhD, SISReL, KAIST |
| Whiyoung Jung | 석사 (2017.02) | LG AI Research |
| Hyungcheol Noh | 석사 (2018.02) | TmaxSoft |
| Woojun Kim | 석사 (2018.02) | Assistant Professor, Dept. of Industrial & Systems Engineering, KAIST |
| Giseung Park | 석사 (2018.08) | Postdoc at Robot Vision and Learning Lab. Dept. of Computer Science, University of Toronto |
| Myungsik Cho | 석사 (2019.02) | Postdoc at SISReL, KAIST |
| Sungho Choi | 석사 (2020.02) | PhD Program, SISReL, KAIST |
| Jongeui Park | 석사 (2020.02) | PhD Program, SISReL, KAIST |
| Jongseong Chae | 석사 (2021.02) | PhD Program, SISReL, KAIST |
| Jeewon Jeon | 석사 (2022.02) | PhD Program, SISReL, KAIST |
| Inuk Son | 석사 (2023.02) | SK Hynix |
| Seongmin Kim | 석사 (2023.02) | PhD Program, SISReL, KAIST |
| Dongwook  Lee | 석사 (2023.02) | Imagoworks, Inc. |
| Jeonghye Kim | 석사 (2024.02) | PhD Program, SISReL, KAIST |
| Yongjae Shin | 석사 (2024.02) | PhD Program, SISReL, KAIST |
| Woohyeon Byeon | 석사 (2024.08) | PhD Program, SISReL, KAIST |
| Kyeongmin Kim | 석사 (2025.02) | PhD Program, SISReL, KAIST |
| Hyunyoung Nam | 석사 (2026.02) | Samsung Electronics |
| JeongWoo Park | 석사 (2026.02) | PhD Program, SISReL, KAIST |
| Sojeong Rhee | 석사 (2026.02) | PhD Program, SISReL, KAIST |

## 최근 논문 목록 (2021–2026)

연구실 Journals, Conferences and Workshops, By Topic에 게시된 최근 논문 48편이다. 제목·저자·발표처는 연구실 표기이며, 별표와 공동 기여 표기도 해당 목록을 따른다. 「채택」은 학회 채택으로 게시된 항목이고, 「누리집 기재 날짜」는 발표 예정으로 적힌 학회 날짜다. 사전 공개본은 별도로 표시했다.[^journals][^conferences][^topics]

**2026**

- Seongmin Kim, Woohyeon Byeon, Jiwon Jeon, Seungyul Han\*, and Youngchul Sung\*. "Addressing exogeneous variability in cooperative multi-agent reinforcement learning". *Conference on Neural Information Processing Systems (NeurIPS ), Dec. 2026 (채택)*.
- Woohyeon Byeon, Seongmin Kim, Jiwon Jeon, Woojun Kim\*, and Youngchul Sung\*. "AGiR: Mitigating gift over-reliance in mixed motive games". *Conference on Neural Information Processing Systems (NeurIPS ), Dec. 2026 (채택)*.
- Jiwon Jeon+, Myungsik Cho+, Woojun Kim, Seongmin Kim, Woohyeon Byeon, Seungyul Han\*, and Youngchul Sung\*. "MASTARS: Multi-agent sequential trajectory augmentation with return-conditioned subgoals". *Conference on Neural Information Processing Systems (NeurIPS ), Dec. 2026 (+ Equal contribution) (채택)*.
- Giseung Park+, Hyunyoung Nam+, Woohyeon Byeon, Amir Leshem and Youngchul Sung\*. "Constrained multi-objective reinforcement learning with max-min criterion". *International Conference on Machine Learning (ICML), Seoul, Korea, Jul. 2026 (+ Equal contribution)*.
- Jiwon Jeon+, Myungsik Cho+, Youngchul Sung\*. "STAIRS-Former: Spatio-Temporal Attention with Interleaved Recursive Structure TransFormer for Offline Mulit-task Multi-agent Reinforcement Learning". *International Conference on Learning Representations (ICLR) , Rio de Janeiro, Brazil, April 2026 (+ Equal contribution)*.
- Yongjae Shin, Jongseong Chae, Jongeui Park, and Youngchul Sung\*. "Flow Matching with Injected Noise for Offline-to-Online Reinforcement Learning". *International Conference on Learning Representations (ICLR) , Rio de Janeiro, Brazil, April 2026*.
- Jongseong Chae, Jongeui Park, Yongjae Shin, Gyeongmin Kim, Seungyul Han, and Youngchul Sung\*. "Flow Actor-Critic for Offline Reinforcement Learning". *International Conference on Learning Representations (ICLR) , Rio de Janeiro, Brazil, April 2026*.
- Yongjae Shin, Jongseong Chae, Seongmin Kim, Jongeui Park, and Youngchul Sung\*. "Adaptive action chunking via multi-chunk Q value estimation". *to be presented at NeurIPS 2026 Workshop PTA: From Pretrained Representations to Acting Agents, Dec. 2026 (누리집 기재 날짜)*.
- Jiwon Jeon+, Myungsik Cho+, Jeonghye Kim, and Youngchul Sung\*. "Inject a turn, not a token: Learning where to redirect LLM reasoning for self-correction". *COLM 2026 Workshop on Efficient Reasoning, Oct. 2026*.
- Sojeong Rhee+, Seohui Bae+, Jongeui Park, Whiyoung Jung, Soonyoung Lee, Woohyung Lim and Youngchul Sung\*. "Align as act: Innovations-based reward decomposition for LLM agents". *COML 2026 Workshop on Agent Behavior, Oct. 2026 (+ Co-first authors)*.
- Seongmin Kim, Giseung Park, Woojun Kim, Jeewon Jeon, Seungyul Han\*, and Youngchul Sung. "Generalized Per-Agent Advantage Estimation for Multi-Agent Policy Optimization". *International Conference on Autonomous Agents and Multiagent Systems; DOI <https://doi.org/10.65109/obia4073>*.
- Woohyeon Byeon, Jiwon Jeon, Jeonghye Kim, Youngchul Sung\*. "Be my tutor: On-policy co-distillation for mutual LLM improvement via peer feedback". *preprint, Jun. 2026 (사전 공개본); DOI <https://doi.org/10.48550/arxiv.2606.14368>*.

**2025**

- Woohyeon Byeon, Giseung Park, Jongseong Chae, Amir Leshem and Youngchul Sung\*. "Multi-objective reinforcement learning with max-min criterion: A game-theoretic approach". *Conference on Neural Information Processing Systems (NeurIPS ) , San Diego, CA, Dec. 2025; DOI <https://doi.org/10.52202/085713-2847>*.
- Jeonghye Kim+, Sojeong Rhee+, Minbeom Kim, Dohyung Kim, Sangmook Lee, Youngchul Sung\* and Kyomin Jung\*. "ReflAct: World-grounded decision making in LLM agents via goal-state reflection". *the 2025 Conference of Emplical Methods for Natural Language Processing (EMNLP). (+Equal Contribution), Suzhou, China, Nov. 2025; DOI <https://doi.org/10.18653/v1/2025.emnlp-main.1697>*.
- Myungsik Cho, Jongeui Park, Jeonghye Kim and Youngchul Sung\*. "ARS: Adaptive reward scaling for multi-task reinforcement learning". *International Conference on Machine Learning (ICML), Vancouver, Canada, Jul. 2025*.
- Yongjae Shin, Jeonghye Kim, Whiyoung Jung, Sunghoon Hong, Deunsol Yoon, Youngsoo Jang, Geonhyeong Kim, Jongseong Chae, Youngchul Sung, Kanghoon Lee, and Woohyung Lim\*. "Online pre-training for offline-to-online reinforcement learning". *International Conference on Machine Learning (ICML), Vancouver, Canada, Jul. 2025*.
- Jeonghye Kim, Yongjae Shin, Whiyoung Jung, Sunghoon Hong, Deunsol Yoon, Youngchul Sung, Kanghoon Lee, and Woohyung Lim\*. "Penalizing infeasible actions and reward scaling in reinforcement learning with offline data". *International Conference on Machine Learning (ICML), Vancouver, Canada, Jul. 2025*.
- Giseung Park, Whiyoung Jung, Seungyul Han, Sungho Choi and Youngchul Sung\*. "Adaptive multi-model fusion learning for sparse-reward reinforcement learning". *Neurocomputing, vol. 633, Jun. 2025; DOI <https://doi.org/10.1016/j.neucom.2025.129748>*.
- Giseung Park and Youngchul Sung\*. "Reward dimension reduction for scalable multi-objective reinforcement learning". *International Conference on Learning Representations (ICLR) , Singapore, Apr. 2025*.
- Seohui Bae, Jeonghye Kim, Youngchul Sung and Woohyung Lim\*. "Align while search: Belief-guided exploratory inference for test-time world alignment". *the Exploration in AI Today (EXAIT) Workshop at ICML 2025, Jul. 2025*.

**2024**

- Jeonghye Kim, Suyoung Lee, Woojun Kim, and Youngchul Sung\*. "Adaptive Q-aid for conditional supervised learning in offline reinforcement learning". *Conference on Neural Information Processing Systems (NeurIPS ), Vancouver, Canada, Dec. 2024; DOI <https://doi.org/10.52202/079017-2764>*.
- Gyeongmin Kim, Jeonghye Kim, Suyoung Lee, Jaewoo Baek, Howon Moon, Sangheon. Shin and Youngchul Sung\*. "Robust reinforcement learning under dimension-wise state information drop". *IEEE Access, vol. 12, pp. 135283 - 135299, 2024; DOI <https://doi.org/10.1109/access.2024.3462803>*.
- Sangdon Park, Sohee Bae, Joohyung Lee\* and Youngchul Sung\*. "Real-time dynamic pricing for edge computing services: A market perspective". *IEEE Access, vol. 12, pp. 134754 - 134769, 2024; DOI <https://doi.org/10.1109/access.2024.3462499>*.
- Giseung Park, Woohyeon Byeon, Seongmin Kim, Elad Habakuk, Amir Leshem and Youngchul Sung\*. "The max-min formulation of multi-objective reinforcement learning: From theory to a model-free algorithm". *International Conference on Machine Learning (ICML), Vienna, Austria, Jul. 2024*.
- Myungsik Cho, Jongeui Park, Suyoung Lee and Youngchul Sung\*. "Hard task first: Multi-task reinforcement learning through task scheduling". *International Conference on Machine Learning (ICML), Vienna, Austria, Jul. 2024*.
- Jeonghyee Kim, Suyoung Lee, Woojun Kim\*, and Youngchul Sung\*. "Decision convformer: Local filtering in metaformer is sufficient for decision making". *International Conference on Learning Representations (ICLR) , Vienna, Austria, May 2024*.
- Jongeui Park, Myungsik Cho, and Youngchul Sung. "EMPO: A clustering-based on-policy algorithm for offline reinforcement learning". *ICML Workshop: Aligning Reinforcement Learning Experimentalists and Theorists, Jul. 2024*.

**2023**

- Woojun Kim+, Yongjae Shin+, Jongeui Park, and Youngchul Sung\*. "Sample-efficient and safe deep reinforcement learning via reset deep ensemble agents". *Conference on Neural Information Processing Systems (NeurIPS ), New Orleans, LA, Dec. 2023 (+Equal contribution)*.
- Sungho Choi, Seungyul Han\*, Woojun Kim, Jongseong Chae, Whiyoung Jung, and Youngchul Sung. "Domain adaptive imitation learning with visual observation". *Conference on Neural Information Processing Systems (NeurIPS ), New Orleans, LA, Dec. 2023*.
- Suyoung Lee, Myungsik Cho, and Youngchul Sung\*. "Parameterizing Non-Parametric Meta-Reinforcement Learning Tasks via Subtask Decomposition". *Conference on Neural Information Processing Systems (NeurIPS ), New Orleans, LA, Dec. 2023*.
- Song Noh, Kyungsik Seo, Youngchul Sung, David Love, Junse Lee\* and Heejung Yu\*. "Joint direct and indirect channel estimation for RIS-assisted millimeter-wave systems based on array signal processing". *IEEE Transactions on Wireless Communications, vol. 22, no. 11, pp. 8378 - 8391, Nov. 2023; DOI <https://doi.org/10.1109/twc.2023.3262492>*.
- Woojun Kim+, Jeonghye Kim+ and Youngchul Sung\*. "LESSON: Learning to integrate exploration strategies for reinforcement learning via an option framework". *International Conference on Machine Learning (ICML), Hawaii, HI, Jul. 2023 (+Equal contribution)*.
- Woojun Kim and Youngchul Sung\*. "An adaptive entropy regularization framework for multi-agent reinforcement learning". *International Conference on Machine Learning (ICML), Hawaii, HI, Jul. 2023*.
- M. Shahjalal, W. Kim, W. Khalid, S. Moon, M. Khan, S. Liu, S. Lim, E. Kim, D. Yun, J. Lee, W. Lee, S. Hwang, D. Kim, J. Lee, H. Yu, Y. Sung, and Y. Jang\*. "Enabling technologies for AI empowered 6G massive radio access networks". *ICT Express, vol. 9, no. 3, pp. 341 - 355, Jun. 2023; DOI <https://doi.org/10.1016/j.icte.2022.07.002>*.
- Jeonghye Kim, Woojun Kim, and Suyoung Lee, and Youngchul Sung. "Decision convformer: Local filtering in metaformer is sufficient for decision making". *Foundation Model and Decision Making (FMDM) Workshop at NeurIPS 2023, New Orleans, LA, Dec. 2023*.
- Seongmin Kim, Woojun Kim, Jeewon Jeon, Youngchul Sung and Seungyul Han. "Off-policy multi-agent policy optimization with multi-step counterfactual advantage estimation". *Adaptive and Learning Agents (ALA) Workshop at AAMAS 2023, London, UK, May 2023 (Non-archival workshop: Submission to other conference allowed)*.
- Woojun Kim and Youngchul Sung. "Parameter Sharing with network pruning for scalable multi-agent deep reinforcement learning". *International Conference on Autonomous Agents and Multiagent Systems (AAMAS), London, UK, May 2023*.
- Woojun Kim, Whiyoung Jung, Myungsik Cho, and Youngchul Sung. "A variational approach to mutual information-based coordination for multi-agent reinforcement learning". *International Conference on Autonomous Agents and Multiagent Systems (AAMAS), London, UK, May 2023*.

**2022**

- Whiyoung Jung, Myungsik Cho, Jongeui Park and Youngchul Sung\*. "Quantile constrained reinforcement learning: A reinforcement learning framework constraining outage probability". *Conference on Neural Information Processing Systems (NeurIPS ) 2022, New Orleans, LA, Nov. 2022*.
- Jongseong Chae, Seungyul Han\*, Whiyoung Jung, Myungsik Cho, Sungho Choi, and Youngchul Sung. "Robust imitation learning against variations in environment dynamics". *International Conference on Machine Learning (ICML) 2022, Baltimore, MD, Jul. 2022*.
- Jeewon Jeon, Woojun Kim\*, Whiyoung Jung and Youngchul Sung\*. "MASER: Multi-agent reinforcementlearning with subgoals generated from experience replay buffer". *International Conference on Machine Learning (ICML) 2022, Baltimore, MD, Jul. 2022*.
- Song Noh, Junse Lee, Gilwon Lee, Kyungsik Seo, Youngchul Sung and Heejung Yu\*. "Channel Estimation Techniques for RIS-Assisted Communication: Millimeter-Wave and Sub-THz Systems". *IEEE Vehicular Technology Magazine, vol. 17, no. 2, pp. 64 - 73, Jun. 2022; DOI <https://doi.org/10.1109/mvt.2022.3158765>*.
- Giseung Park, Sungho Choi and Youngchul Sung\*. "Blockwise sequential model learning for partially observable reinforcement learning". *the 36rd AAAI Conference on Artificial Intelligence (AAAI ) 2022, Vancouver, Canada, Feb. 2022; DOI <https://doi.org/10.1609/aaai.v36i7.20764>*.
- Woojun Kim and Youngchul Sung. "An adaptive entropy regularizatio framework for multi-agent reinforcement learning". *ICML 2022 Workshop: Decision Awareness in Reinforcement Learning (DARL), Baltimore, MD,Jul. 2022 (Non-archival workshop: Submission to other conference allowed. See the ICML 23 version above.)*.
- Woojun Kim, Whiyoung Jung, Myungsik Cho, and Youngchul Sung. "A variational approach to mutual information-based coordination for multi-agent reinforcement learning". *ICML 2022 Workshop: AI for Agent-Based Modelling (AI4ABM), Baltimore, MD,Jul. 2022 (Non-archival workshop: Submission to other conference allowed. See the AAMAS 23 version above.)*.
- Jongeui Park and Youngchul Sung. "Nonlinear rescaling of acquisition metric values based on distribution fitting". *ICML 2022 Workshop: Adaptive Experimental Design and Active Learning in the Real World (ReALML), Baltimore, MD, Jul. 2022*.
- Myungsik Cho, Whiyoung Jung, and Youngchul Sung. "Multi-task reinforcement learning with task representation method". *ICLR 2022 Workshop on Generalizable Policy Learning in Physical World (GPL), Apr. 2022*.

**2021**

- Seungyul Han and Youngchul Sung\*. "A max-min entropy framework for reinforcement learning". *Conference on Neural Information Processing Systems (NeurIPS) 2021, Dec. 2021*.

## 과제

연구실 Research 쪽의 수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 10건이다. 과제명·지원기관·기간은 연구실 표기이고, 종료 월을 비워 둔 항목은 그 표기를 유지했다.[^research]

- NRF Basic Research Lab. (한국연구재단 기초연구실): Fundamental Research on Vision-Language-Action (VLA) Models for Human-Collaborative Physical AI Agents (기간 2026.07 - ; 지원 NRF)
- National AI Hub Project (국가 AI 연구 거점 ): Physical AI and Robotic Foundation Models (기간 2024.07 - ; 지원 IITP; 역할 PI: Kee-Eung Kim)
- Generative Model-based Efficient Reinforcement Learning Algorithms for Multi-modal Expansion in Generalized Environments (기간 2025.03 - ; 지원 NRF)
- Development of Core Technologies for Task-Oriented Reinforcement Learning for Commercialization   of Autonomous Drones (기간 2022.04 - ; 지원 IITP)
- Development of Artificial Intelligence Technology for Self-Improving Competency-Aware Learning Capabilities (기간 2022.04 - ; 지원 IITP)
- Deep Multi-Agent Reinforcement Learning of Markov Games for Distributed Traffic Management in Smart Cities (기간 2022.09 - 2024.08; 지원 NRF Korea-Israel Joint Project)
- Information Theory-Based Reinforcement Learning for Generalized Environments (기간 2021.03 - 2025.02; 지원 NRF)
- Development of Disaster Response Algorithm through Internet Big Data Analysis Based on Artificial Intelligence (기간 2019.09 - 2022.09; 지원 NRF)
- Center for Applied Research in Artificial Intelligence (기간 2019.12 - 2026.04; 지원 ADD)
- Machine Learning-based Edge Computing Operation Optimization (기간 2019.04 - 2021.12; 지원 IITP)

## 수상과 선정

연구실 소식의 수상·후보 선정·과제 선정 3건과 Members 쪽에 적힌 졸업생 수상 1건이다. 「Nominee」는 수상 후보 선정이다. 2025년 수상 항목의 연도는 누리집 표기이고 날짜는 게시되어 있지 않다.[^news][^members][^vla]

- 2026/06 · 성영철 교수가 연구책임자인 「사람과 협력하는 피지컬 인공지능 에이전트를 위한 시각-언어-행동 모델 핵심 기술 연구」가 한국연구재단 기초연구실 과제로 선정됐다.
- 2026/03 · 「Generalized Per-Agent Advantage Estimation for Multi-Agent Policy Optimization」이 AAMAS 2026 Best Paper Award Nominee로 선정됐다.
- 2026/03 · 김정혜 학생이 Microsoft Research Asia의 Award of Excellent Intern을 받았다.
- 2025 · Whiyoung Jung이 LG Award를 받았다.

## 소식

연구실 News & Notices에 게시된 2021년 12월–2026년 9월의 논문 채택·연구 성과·연구 착수·사업 참여 소식 22건이다. 날짜는 게시 목록의 연월 표기다.[^news]

- 2026/09 · 논문들이 NeurIPS 2026에 채택됐다.
- 2026/08 · 대형 언어 모델 에이전트의 강화학습 사후 학습 연구 결과를 COLM 2026 Workshop on Agent Behavior에서 발표할 예정이라고 알렸다.
- 2026/06 · POSCO와 로보티즈 AI Worker를 이용한 휴머노이드 연구를 시작했다.
- 2026/05 · 다목적 강화학습 논문이 ICML 2026에 채택됐다.
- 2026/01 · 논문 세 편이 ICLR 2026에 채택됐다.
- 2025/08 · 논문 한 편이 NeurIPS 2025에 채택됐다.
- 2025/08 · 국가 소버린 인공지능 연구팀 선정에 연구실이 참여했다고 알렸다.
- 2025/08 · 대형 언어 모델 에이전트 논문 ReflAct가 EMNLP 2025에 채택됐다.
- 2025/05 · 대형 언어 모델 에이전트 ReflAct의 연구 성과를 소개했다.
- 2025/05 · 다중 과제 강화학습 방법 ARS의 Meta-World MT10 연구 성과를 소개했다.
- 2025/05 · 논문 세 편이 ICML 2025에 채택됐다.
- 2025/02 · 논문 한 편이 ICLR 2025에 채택됐다.
- 2024/09 · 논문 한 편이 NeurIPS 2024에 채택됐다.
- 2024/05 · 논문 두 편이 ICML 2024에 채택됐다.
- 2023/09 · 논문 세 편이 NeurIPS 2023에 채택됐다.
- 2023/04 · 논문 두 편이 ICML 2023에 채택됐다.
- 2023/01 · 오프라인 강화학습 논문 Decision ConvFormer가 ICLR 2024에 채택됐다.
- 2022/09 · 정휘영 박사의 제약 강화학습 논문이 NeurIPS 2022에 채택됐다.
- 2022/07 · ICML 2022 워크숍에서 논문 세 편을 발표한다고 알렸다.
- 2022/05 · 전지원 학생의 다중 에이전트 강화학습 논문 MASER가 ICML 2022에 채택됐다.
- 2022/05 · 채종성 학생의 환경 변화에 대한 모방학습 논문이 ICML 2022에 채택됐다.
- 2021/12 · 박기승 학생이 주저자로 참여한 부분 관측 강화학습 논문이 AAAI 2022에 채택됐다.

## 연락과 위치

- 교수 연구실: 대전광역시 유성구 대학로 291 KAIST IT융합빌딩(N1) 614호[^dept][^intro]
- 학생 연구실: N1 619호[^intro]
- 교수 전화: +82-42-350-3484[^home]
- 연구실 전화: +82-42-350-5484[^home]
- 팩스: +82-42-350-8084[^home]
- 교수 이메일: ycsung@kaist.ac.kr[^home][^intro]
[^home]: SISReL, Introduction. <https://sites.google.com/view/sisrelkaist/introduction> (관측 2026-11-09).

[^intro]: SISReL, Brief Introduction. <https://sites.google.com/view/sisrelkaist/introduction/detailintro> (관측 2026-11-09).

[^research]: SISReL, Research. <https://sites.google.com/view/sisrelkaist/research> (관측 2026-11-09).

[^pi]: Youngchul Sung, 교수 소개. <https://sites.google.com/view/youngchulsung> (관측 2026-11-09).

[^dept]: KAIST 전기및전자공학부, 성영철 교수 소개. <https://ee.kaist.ac.kr/professor/12208/> (관측 2026-11-09).

[^members]: SISReL, Members. <https://sites.google.com/view/sisrelkaist/members> (관측 2026-11-09).

[^journals]: SISReL, Journals and Top Machine Learning Conferences. <https://sites.google.com/view/sisrelkaist/publications/journals> (관측 2026-11-09).

[^conferences]: SISReL, Conferences and Workshops. <https://sites.google.com/view/sisrelkaist/publications/conferences> (관측 2026-11-09).

[^topics]: SISReL, By Research Topic. <https://sites.google.com/view/sisrelkaist/publications/by-topic> (관측 2026-11-09).

[^news]: SISReL, News & Notices. <https://sites.google.com/view/sisrelkaist/news-notices> (관측 2026-11-09).

[^robot]: SISReL, POSCO와 휴머노이드 연구. <https://sites.google.com/view/sisrelkaist/news-notices/robotis_ai_worker> (관측 2026-11-09).

[^vla]: SISReL, 한국연구재단 기초연구실 과제 선정. <https://sites.google.com/view/sisrelkaist/news-notices/vlaproject> (관측 2026-11-09).

[^p1]: S. Kim 외, Y. Sung, Adaptive Agents and Multi-Agents Systems (2026). <https://doi.org/10.65109/obia4073> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5020240958,publication_year:2021-2026> (관측 2026-11-09).

[^p2]: M. Cho, J. Park, J. Kim, Y. Sung, Proceedings of the 42nd International Conference on Machine Learning 267, 10583–10601 (2025). <https://proceedings.mlr.press/v267/cho25d.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v267/cho25d.html> (관측 2026-11-09).

[^p3]: J. Kim 외, K. Jung, Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, 33433–33465 (2025). <https://doi.org/10.18653/v1/2025.emnlp-main.1697> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://aclanthology.org/2025.emnlp-main.1697/> (관측 2026-11-09).

[^p4]: W. Byeon 외, Y. Sung, NeurIPS (2025). <https://doi.org/10.52202/085713-2847> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5020240958,publication_year:2021-2026> (관측 2026-11-09).

[^p5]: J. Kim, S. Lee, W. Kim, Y. Sung, NeurIPS (2024). <https://doi.org/10.52202/079017-2764> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5020240958,publication_year:2021-2026> (관측 2026-11-09).

[^p6]: G. Kim 외, Y. Sung, IEEE Access (2024). <https://doi.org/10.1109/access.2024.3462803> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5020240958,publication_year:2021-2026> (관측 2026-11-09).

[^p7]: S. Noh 외, H. Yu, IEEE Transactions on Wireless Communications (2023). <https://doi.org/10.1109/twc.2023.3262492> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5020240958,publication_year:2021-2026> (관측 2026-11-09).

[^p8]: G. Park, S. Choi, Y. Sung, Proceedings of the AAAI Conference on Artificial Intelligence (2022). <https://doi.org/10.1609/aaai.v36i7.20764> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5020240958,publication_year:2021-2026> (관측 2026-11-09).

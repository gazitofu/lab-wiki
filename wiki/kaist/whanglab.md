# 데이터 지능 연구실 (Data Intelligence Lab, DI Lab)

**KAIST 전기및전자공학부 · 황의종 교수**

- 분야: 데이터 중심 AI, 책임 있는 AI(공정성·견고성·개인정보 보호·설명 가능성), 빅데이터와 AI의 통합, 대형 언어 모델 평가
- 대분야: 컴퓨팅·AI
- 태그: 대형 언어 모델[^home][^p1][^p2], 생성 인공지능[^p3], 멀티모달 AI[^p5], AI·기계학습 보안·프라이버시[^p3], 책임 있는 AI·공정성[^p4], 설명 가능한 AI(XAI)[^p8], 데이터 중심 AI·데이터 효율 학습[^p5], 연속학습[^p7]
- 홈페이지: <https://sites.google.com/view/whanglab/di-lab>
- 근거와 출처: [데이터 지능 연구실 근거 페이지](whanglab-sources.md)

> 기계학습 모델의 공정성·견고성·개인정보 보호·설명 가능성 문제를 모델이 아니라 학습에 쓰는 데이터를 모으고, 고치고, 늘리고, 고르는 쪽에서 푸는 연구실이다. 관계형 데이터베이스의 규칙을 이용해 대형 언어 모델이 사실을 바르게 아는지 체계적으로 시험하는 평가 연구도 한다.[^home][^projects][^p1][^p2]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 황의종 교수가 이끄는 데이터 지능 연구실(Data Intelligence Lab)이다.[^home][^ee] 누리집 첫 화면은 연구실의 사명을 데이터 지능 연구의 한계를 넓히고 KAIST에서 다음 세대를 이끌 연구자를 길러 내는 것이라고 적는다. 연구실은 책임 있는 AI(Responsible·Trustworthy·Safe AI, 공정성과 안전처럼 사회가 요구하는 조건을 지키는 인공지능), 데이터 중심 AI(Data-centric AI, 모델 구조보다 학습 데이터를 고쳐 성능과 신뢰성을 높이는 접근), 빅데이터와 AI의 통합을 대형 언어 모델(LLM)·에이전트형 AI(Agentic AI)·물리 AI(Physical AI)를 포함한 기계학습 전반에서 다룬다고 소개한다. Google Research, Microsoft Research, Samsung Research와 삼성전자, SK Hynix, SK Telecom과 가깝게 협력한다고도 적는다.[^home]

Projects 페이지는 연구실이 특히 기계학습의 공정성(fairness, 성별·인종 같은 민감한 집단에 불리한 예측을 하지 않는 성질), 견고성(robustness, 잡음이나 오류가 섞인 데이터에서도 성능이 유지되는 성질), 개인정보 보호(privacy), 설명 가능성(explainability, 모델이 왜 그런 예측을 했는지 사람이 알 수 있게 하는 성질)의 문제를 데이터에서 출발해 풀려 한다고 적는다. 그리고 논문을 네 갈래로 묶는다. 데이터 수집·생성·레이블링(데이터에 정답 표시를 붙이는 일), 데이터 정제·검증·증강(학습 데이터를 변형하거나 합성해 늘리는 일)·선택, 모델 학습, 모델 설명·검증·평가다. 이와 따로 기계학습의 데이터 수집·품질 문제와 견고성·공정성을 정리한 설문 논문(한 분야의 연구를 모아 정리한 논문)과 튜토리얼도 묶어 둔다.[^projects]

최근 논문으로 보면 세 줄기가 두드러진다. 첫째는 대형 언어 모델이 사실을 정확히 아는지를 관계형 데이터베이스(표로 정리한 자료와 표 사이의 연결을 함께 담은 데이터베이스)의 규칙으로 자동 검증하는 평가 벤치마크(모델 성능을 비교하는 시험 문제 모음)다(대표 논문 1, 2).[^p1][^p2] 둘째는 공정성과 개인정보 보호를 지키며 데이터를 모으고 만들어 내는 방법으로, 공정성을 고려해 레이블을 붙일 표본을 고르는 능동 학습과 개인정보 보호와 공정성을 함께 지키는 합성 데이터 생성이 있다(대표 논문 3, 4).[^p3][^p4] 셋째는 데이터 증강·선택과 학습 가중치 조정으로 모델을 견고하고 공정하게 만드는 방법이다(대표 논문 5–7).[^p5][^p6][^p7] 여기에 데이터 처리 방식이 모델 설명을 어떻게 바꾸는지 살핀 연구가 더해진다(대표 논문 8).[^p8]

최근 논문 목록에는 질문의 표현 방식에 따라 대형 언어 모델의 답이 달라지는 틀 효과를 줄이는 DeFrame(ACL Findings 2026), 학년에 맞춰 가르치는 교사 역할의 대형 언어 모델을 다룬 Classroom AI(npj Artificial Intelligence 2026), 공정한 온라인 대전 게임을 위한 부정행위 방지 프레임워크 RoDAC(KDD 2026), 표준 미국 영어 밖의 방언을 다루는 대화 생성 프레임워크 DialectLLM(NeurIPS 2026 채택), SHAP 설명이 여러 가지로 나올 수 있는 문제를 다룬 연구(NeurIPS 2026 채택)도 있다.[^pubs]

## 주요 연구 주제

### 1. 대형 언어 모델의 사실성 평가

관계형 데이터베이스의 무결성 제약(데이터가 지켜야 하는 규칙)으로 대형 언어 모델에 물을 질문과 답을 자동으로 만들고, 답뿐 아니라 답에 이른 근거까지 검증하는 벤치마크.[^p1] 값이 유효했던 기간을 함께 저장하는 시간 데이터베이스로 시간에 따라 바뀌는 사실을 묻는 벤치마크.[^p2] 질문의 틀에 따라 답이 치우치는 문제를 줄이는 DeFrame(ACL Findings 2026)과 표 데이터를 함께 다뤄 사실 응답을 개선하는 연구(사전 공개)도 같은 갈래다.[^pubs][^projects] 대표 논문 1, 2.

### 2. 공정성과 개인정보 보호를 지키는 데이터 수집·생성

공정성을 높이는 데 가장 도움이 되는 표본을 골라 레이블을 붙이는 공정 능동 학습,[^p4] 개인정보 보호와 공정성을 함께 지키는 합성 데이터 생성 프레임워크.[^p3] 개인 단위 공정성을 위해 레이블을 뒤집는 iFlipper(SIGMOD 2023), 정확하고 공정한 모델을 위해 데이터를 골라 모으는 Slice Tuner(SIGMOD 2021)도 Projects 페이지가 이 갈래에 둔다.[^projects][^pubs] 대표 논문 3, 4.

### 3. 데이터 증강과 선택

종류가 다른 자료 사이 의미가 어긋난 표본을 만들어 멀티모달 모델의 자료 종류 불균형을 줄이는 증강,[^p5] 잡음 섞인 데이터에서 회귀(연속된 값을 예측하는 과제) 모델을 위한 증강과 견고한 학습의 결합.[^p6] 클래스 증분 학습에서 기울기를 이용해 섞을 표본을 고르는 GradMix(KDD 2026), 입력과 정답의 관계가 시간에 따라 바뀌는 개념 변화(concept drift)에 맞서 학습할 데이터 구간을 고르는 Quilt(AAAI 2024)도 이 갈래다.[^projects][^pubs] 대표 논문 5, 6.

### 4. 공정하고 견고한 모델 학습

새 클래스를 단계적으로 더 배우는 클래스 증분 학습에서 표본 가중치를 조정해 특정 집단이 앞서 배운 것을 더 많이 잊는 불공정을 줄이는 방법.[^p7] 클래스 증분 학습에서 모델의 확신도를 실제 정답률에 맞추는 보정 방법 T-CIL(CVPR 2025), 학습할 때와 쓸 때 데이터의 상관관계가 달라지는 상황(correlation shift)에서의 공정한 학습(ICML 2023), 공정하고 견고한 학습을 위한 표본 선택(NeurIPS 2021)도 이 갈래다.[^projects][^pubs] 대표 논문 7.

### 5. 모델 설명과 검증

표 데이터의 특징을 어떻게 표현하느냐에 따라 SHAP(각 입력 특징이 예측에 얼마나 기여했는지 계산하는 설명 방법)의 특징 중요도가 달라질 수 있음을 보인 연구.[^p8] 같은 예측에 대해 SHAP 설명이 여러 가지로 나오는 문제를 다룬 연구(NeurIPS 2026 채택)는 Projects 페이지가 이 갈래에 둔다. 논문 목록에는 설명을 먼저 고려한 군집화 XClusters(AAAI 2023)도 있다.[^projects][^pubs] 대표 논문 8.

## 대표 논문

황의종 교수가 저자인 2021–2026년 논문 가운데 초록을 확인할 수 있는 논문을 연구 갈래마다 고르게 골랐다. 8편 모두 교수가 마지막 저자이고, 누리집 목록은 교신저자를 따로 표시하지 않는다.[^pubs] "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2024 | [ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models](https://doi.org/10.52202/079017-1681) · NeurIPS 2024 | 대형 언어 모델(LLM)을 평가하는 기존 벤치마크는 사람이 직접 만들거나, 자동으로 만들더라도 여러 단계를 거치는 모델의 사고 과정을 평가하지 못한다. 연구진은 개체-관계(ER) 모형에 바탕을 둔 기존 관계형 데이터베이스가 LLM에 물을 구조화된 지식을 담고 있다는 점에 주목했다. 지식 그래프와 달리 관계형 데이터베이스에는 무결성 제약이 있어, 함수 종속성(어떤 속성값이 정해지면 다른 속성값이 하나로 정해지는 관계)으로 답에 꼭 필요한 핵심어를 짚고, 외래 키 제약(한 표의 값이 다른 표의 값을 가리키도록 묶는 규칙)으로 표를 이어 여러 단계를 거치는 질문을 만들고 중간 답을 점검할 수 있다. 이 제약으로 어떤 데이터베이스든 LLM 벤치마크로 바꾸는 ERBench를 제안했다. 데이터베이스가 바뀌어도 계속 평가할 수 있고, 멀티모달 질문과 여러 프롬프트 기법을 지원한다. 여러 분야의 데이터베이스로 벤치마크를 만들어 최신 LLM을 폭넓게 비교했고, 답의 정오뿐 아니라 맞는 핵심어가 있는지로 답의 근거까지 검증할 수 있음을 보였다. | 공동 1저자 J. Oh·S. Kim(\*), 7명 중 마지막 저자 황의종 |
| 2 | 2026 | [Harnessing Temporal Databases for Systematic Evaluation of Factual Time-Sensitive Question-Answering in Large Language Models](https://www.arxiv.org/abs/2508.02045) · ICLR 2026 | 사실은 시간이 지나면 바뀌므로 LLM은 시간에 따라 달라지는 사실 지식을 정확하게 다뤄야 한다. 시간에 민감한 사실 질의응답(TSQA) 과제는 많이 만들어졌지만, 기존 벤치마크는 사람 손이 많이 들어 규모 있고 폭넓은 평가가 어렵다. 연구진은 시간 데이터베이스와 시간 함수 종속성, 시간 SQL, 시간 조인 같은 데이터베이스 기법으로 TSQA 문제와 답의 쌍을 체계적으로 만드는 벤치마크 TDBench를 제안했다. 기존의 답 정확도와 함께, 모델의 설명 속 시간 언급이 맞는지를 따지는 새 평가 지표 time accuracy도 도입했다. 최신 LLM 실험에서 TDBench가 사람의 노동을 줄이면서 규모 있고 폭넓은 TSQA 평가를 가능하게 하고, 위키백과·위키데이터에 집중된 기존 평가를 보완해 특정 응용 분야의 데이터로도 LLM을 평가할 수 있게 함을 보였다. | 1저자 S. Kim, 4명 중 마지막 저자 황의종 |
| 3 | 2025 | [PFGuard: A Generative Framework with Privacy and Fairness Safeguards](https://arxiv.org/abs/2410.02246) · ICLR 2025 | 믿을 수 있는 AI를 위해 생성 모델(학습한 데이터와 비슷한 새 데이터를 만드는 모델)은 개인정보 보호와 공정성을 함께 지켜야 한다. 두 목표는 따로 연구돼 왔고 최근에는 기존 기법을 합치자는 제안이 나왔지만, 단순히 합치면 소수 집단의 표본이 공정성을 위해 반영되다가 개인정보 보호 때문에 억눌리는 충돌이 생길 수 있다. 연구진은 이 충돌이 개인정보 침해와 예상하지 못한 공정성-유용성 맞교환 같은 부작용으로 이어짐을 보였다. 이를 줄이려고 개인정보 보호·공정성·유용성을 함께 다루는 생성 프레임워크 PFGuard를 제안했다. 여러 교사 모델의 앙상블(여러 모델의 결과를 합치는 방법)로 공정한 학습 단계와 개인정보를 지키는 학습 단계 사이의 충돌을 조정하고, 앙상블 학습으로 높은 유용성을 얻는다. 실험에서 PFGuard는 고차원 데이터의 합성 데이터를 만들면서 차분 프라이버시(DP, 개인 한 사람의 데이터가 결과에 주는 영향을 수학적으로 제한하는 개인정보 보호 기준) 보장과 공정한 생성 모델 학습의 수렴을 함께 이뤘다. | 1저자 S. Kim, 4명 중 마지막 저자 황의종 |
| 4 | 2024 | [Falcon: Fair Active Learning using Multi-armed Bandits](https://doi.org/10.14778/3641204.3641207) · VLDB 2024 (PVLDB) | 편향된 데이터는 불공정한 모델로 이어지므로, 데이터를 모으고 레이블을 붙이는 단계부터 공정성을 넣어야 한다. 연구진은 표본을 전략적으로 골라 모델 공정성을 높이는 데이터 중심의 공정 능동 학습(레이블을 붙일 표본을 골라 가며 배우는 방식) 프레임워크 Falcon을 제안했다. 사용자가 정한 집단 공정성 척도에 대해, 공정성 개선에 가장 도움이 되는 '목표 집단'(예: 속성=여성, 레이블=긍정)의 표본을 찾는다. 목표 집단은 표본을 고를 때 아직 알 수 없는 정답 레이블로 정의되므로, 예측한 레이블이 기대와 달라 목표 집단 밖이면 그 표본의 사용을 미루는 시행착오 방법을 썼다. 정보가 많은 표본을 고를수록 미뤄질 가능성도 커지는 맞교환이 있고 최적 균형은 데이터마다 다르므로, 이 맞교환을 정책으로 나타내고 적대적 다중 슬롯머신(multi-armed bandit, 여러 선택지를 번갈아 시도하며 보상이 큰 쪽을 찾는 방법) 방법으로 가장 좋은 정책을 자동으로 고른다. 실험에서 Falcon은 기존 공정 능동 학습 방법보다 공정성·정확도·효율이 좋았고, 정확도와 공정성 사이의 맞교환을 제대로 지원한 방법은 Falcon뿐이었으며 최대 공정성 점수는 두 번째로 좋은 결과보다 1.8–4.5배 높았다. | 1저자 K. Tae, 5명 중 마지막 저자 황의종 |
| 5 | 2025 | [MIDAS: Misalignment-based Data Augmentation Strategy for Imbalanced Multimodal Learning](https://doi.org/10.52202/085713-4942) · NeurIPS 2025 | 멀티모달 모델(이미지·글처럼 종류가 다른 자료를 함께 다루는 모델)은 우세한 한 종류의 자료에 지나치게 기대 최적 성능을 내지 못하는 경우가 많다. 기존 연구는 학습 목표나 최적화 절차를 고쳤고, 데이터 중심의 해법은 덜 탐구됐다. 연구진은 종류가 다른 자료끼리 의미가 맞지 않는 어긋난 표본을 만들고, 자료 종류마다의 확신도로 레이블을 붙여 모델이 서로 모순된 신호에서도 배우게 하는 데이터 증강 전략 MIDAS를 제안했다. 확신도 기반 레이블이 여전히 확신이 큰 쪽을 편들 수 있어, 확신이 가장 낮은 자료 종류의 손실 가중치를 학습 중에 높이는 약한 자료 종류 가중을 더했다. 또 어긋난 특징이 맞는 특징과 더 비슷할수록 어려운 표본이 되어 모델이 클래스를 더 잘 구분하게 되므로, 이런 의미가 모호한 어긋난 표본에 우선순위를 주는 어려운 표본 가중을 제안했다. 여러 멀티모달 분류 벤치마크에서 MIDAS는 자료 종류 불균형 문제에서 관련 기준 방법보다 뛰어났다. | 공동 1저자 S. Hwang·S. Choi(\*), 3명 중 마지막 저자 황의종 |
| 6 | 2024 | [RC-Mixup: A Data Augmentation Strategy against Noisy Data for Regression Tasks](https://doi.org/10.1145/3637528.3671993) · KDD 2024 | 잡음이 섞인 데이터가 있을 때 회귀 과제를 위한 견고한 데이터 증강을 연구했다. 널리 쓰이는 Mixup(두 표본을 선형으로 섞어 새 표본을 만드는 증강) 같은 기법은 주로 이미지 분류용이고, 회귀에 특화된 C-Mixup은 레이블 사이 거리에 따라 섞을 표본을 고르지만 잡음 섞인 표본과 깨끗한 표본을 가리지 못한다. 한편 여러 차례의 모델 학습으로 잡음 데이터에 강한 모델을 만드는 견고한 학습도 많이 연구돼 왔다. 연구진은 C-Mixup과 여러 차례의 견고한 학습을 긴밀하게 결합한 RC-Mixup을 제안했다. C-Mixup은 견고한 학습이 깨끗한 데이터를 찾는 일을 돕고, 견고한 학습은 C-Mixup에 더 깨끗한 데이터를 준다. 견고한 학습 알고리즘 자체는 고치지 않고 데이터 섞기만으로 이득을 보는 데이터 중심 방식이라는 점이 장점이다. 실험에서 잡음 데이터 벤치마크에 대해 C-Mixup과 견고한 학습 기준 방법보다 크게 좋았고, 여러 견고한 학습 방법과 함께 쓸 수 있었다. | 1저자 S. Hwang, 3명 중 마지막 저자 황의종 |
| 7 | 2026 | [Fair Class-Incremental Learning using Sample Weighting](https://doi.org/10.1145/3770854.3780167) · KDD 2026 | 클래스 증분 학습에서는 정확도가 주로 연구됐고 공정성은 상대적으로 덜 다뤄졌다. 현재 과제의 표본을 모두 그대로 학습에 쓰면 클래스를 포함한 특정 민감 집단이 앞서 배운 것을 불공정하게 잊는 파국적 망각이 생긴다. 연구진은 현재 과제 데이터의 평균 기울기 벡터가 민감 집단의 평균 기울기 벡터와 '반대 방향'일 때, 곧 두 벡터의 내적이 음수일 때 망각이 일어남을 이론으로 분석했다. 그리고 현재 과제 표본의 학습 가중치를 조정해 평균 기울기 벡터의 방향을 바꿈으로써 성능이 낮은 집단의 망각을 줄이고 공정성을 이루는 프레임워크를 제안했다. 여러 집단 공정성 척도에 대해 민감 집단의 전체 손실과 집단 사이 격차를 함께 줄이는 최적화 문제를 세우고, 이 문제를 선형 계획법으로 풀 수 있음을 보여 효율적인 공정성 인식 표본 가중(FSW) 알고리즘을 제안했다. 실제 데이터 실험에서 FSW는 최신 방법들보다 정확도-공정성 맞교환 결과가 좋았다. | 공동 1저자 J. Park·M. Kim(\*), 3명 중 마지막 저자 황의종 |
| 8 | 2025 | [SHAP-based Explanations are Sensitive to Feature Representation](https://doi.org/10.1145/3715275.3732105) · FAccT 2025 | 예측 하나에서 각 입력 특징이 얼마나 기여했는지 보여 주는 국소 특징 기반 설명은 설명 가능한 AI(XAI) 도구의 핵심이다. 이 설명은 '해석 가능한' 특징 표현을 기준으로 특징 중요도를 계산하는데, 표 데이터에서는 특징값 자체를 해석 가능하다고 보는 경우가 많다. 연구진은 데이터를 다루는 방식의 선택이 이런 설명에 주는 영향을 살폈다. 나이를 히스토그램(값을 구간으로 나눠 나타낸 것)으로 표현하거나 인종을 특정 방식으로 부호화하는 것처럼 단순하고 흔한 데이터 처리 기법만으로 SHAP 같은 널리 쓰이는 방법이 정하는 특징 중요도를 조작할 수 있음을 보였다. 설명이 특징 표현에 민감하다는 점은 공격자가 차별 같은 문제를 가리는 데 악용할 수 있다. 기존 연구는 데이터를 편향시키거나 모델을 조작하는 공격에 집중했고, 저자들은 자신들이 아는 한 평범해 보이는 표준 데이터 처리 기법만으로 설명 도구가 오도될 수 있음을 보인 첫 연구라고 밝힌다. | 1저자 H. Hwang, 6명 중 마지막 저자 황의종 |

## 교수와 전문 분야

황의종 교수(Steven Euijong Whang)는 KAIST 전기및전자공학부 종신 부교수(Tenured Associate Professor)이고 데이터 지능 연구실을 이끈다. Professor 페이지는 연구 관심을 데이터 중심 AI와 책임 있는 AI로 적는다.[^prof] 전기및전자공학부 교수 소개는 직위를 부교수로, 디비전을 Computer와 Communication으로, 주요 연구분야를 Big Data로, 주요 연구를 Big Data, AI, Responsible AI, Data-Centric AI, Data Science로 적는다.[^ee]

Professor 페이지 경력에 따르면 교수는 2018년 2월 KAIST 전기및전자공학부 조교수로 부임해 2020년 9월 부교수, 2024년 3월 종신 부교수가 됐다. 2019년 11월부터 AI대학원(Graduate School of AI), 2023년 3월부터 반도체시스템공학과(Dept. of Semiconductor System Engineering)의 겸임교수(Adjunct Professor)이고, 2020년 3월부터 2023년 2월까지 권오현 석좌교수(Kwon Oh-Hyun Endowed Chair Professor)였다. 2025년 7월부터 2026년 6월까지는 Stanford University 컴퓨터과학과 방문 부교수(Visiting Associate Professor, 호스트 Christopher Ré)로 연구년을 보냈다.[^prof][^news]

교수는 KAIST에서 전산학 학사 학위(2003)를, Stanford University에서 컴퓨터과학 석사 학위(2007, 지도교수 Jennifer Widom)와 박사 학위(2012, 지도교수 Hector Garcia-Molina)를 받았고, 2012년 7월부터 12월까지 Stanford University 박사후연구원이었다. 2012년 12월부터 2018년 1월까지 Google Research에서 연구원(Research Scientist)으로 일하며 기계학습 플랫폼 TensorFlow Extended(TFX)의 데이터 인프라를 함께 개발했다. 학생 때는 Yahoo! Research와 HP Labs에서 연구 인턴을 했다.[^prof]

Professor 페이지가 적는 수상과 영예는 다음과 같다. KAIST 재직 중에는 VLDB 2026 Distinguished Associate Editor Award(2026년 9월), KAIST 공과대학 Impact Research Award(2025년 12월), Y-KAST(Young Korean Academy of Science and Technology) 회원 선출(2024년 12월), Google Research Award(2022년 6월, 2023년 10월, 2024년 10월), KAIST 전기및전자공학부 우수강의상(Best Teaching Award, 2022년 10월, EE477 Database and Big Data Systems), Google AI Focused Research Award(2018년 10월–2021년 9월), KAIST EE Best Paper Award(2019년 7월), IEEE Senior Member(2019년 4월)를 적는다. 그 이전에는 WebDB 워크숍 Best Paper Award(2015년 5월), IBM PhD Fellowship(2011년 3월–2012년 2월), Stanford School of Engineering Fellowship(2007–2008), KFAS(Korea Foundation for Advanced Studies) 장학금(2005–2007), KAIST 졸업 때의 KAIST President's Prize for Academic Excellence(2003년 2월)를 적는다.[^prof]

학계 활동으로는 IEEE TKDE(IEEE Transactions on Knowledge and Data Engineering) Senior Associate Editor(2026–), IEEE TKDE Associate Editor(2023–2027), VLDB(2025–2027)·ACM SIGMOD 2027 Associate Editor, NeurIPS 2026·ICLR 2025–2027·ICML 2026–2027 Area Chair, IEEE ICDE 운영위원(2026–), ACM SIGMOD Jim Gray Doctoral Dissertation Award 위원회(2026)를 맡는다. VLDB 2026 패널 의장과 QDB 워크숍(VLDB 2026) General Chair를 맡았고, NYU-KAIST 협력의 Inclusive AI Center 의장(2023–)과 Google-KAIST Partnership 의장(2019–2021)을 지냈다.[^prof]

누리집 소식에 따르면 교수는 2022년 3월 한국연구재단 중견연구자 지원 사업(Mid-Career Researcher Program)에 연구책임자로 선정돼 5년 동안 Data-centric Trustworthy AI 연구를 지원받게 됐고, 2022년 4월에는 IITP(Institute for Information & communication Technology Planning & evaluation)의 Human-centered AI core technology R&D로 5년 동안 지원받게 됐다.[^news]

논문으로 보면 교수의 전문 분야는 데이터 관리 기술로 기계학습의 신뢰성을 높이는 데이터 중심의 책임 있는 AI다. 공정성을 고려한 데이터 수집(대표 논문 4)과 지속 학습(대표 논문 7), 개인정보 보호와 공정성을 함께 지키는 데이터 생성(대표 논문 3), 잡음에 강한 데이터 증강(대표 논문 5, 6), 설명의 신뢰성(대표 논문 8), 데이터베이스 기법을 이용한 대형 언어 모델 평가(대표 논문 1, 2)가 여기에 든다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8] 2018년 이전 Stanford·Google 시기의 논문은 같은 대상을 가리키는 서로 다른 기록을 찾아 묶는 개체 해소(entity resolution), 정보 유출 관리, Google의 데이터셋 관리 시스템 Goods, 기계학습 플랫폼 TFX와 데이터 검증을 다룬다.[^pubs]

## 응용 분야

누리집은 Google Research, Microsoft Research, Samsung Research와 삼성전자, SK Hynix, SK Telecom과 가깝게 협력한다고 적는다.[^home] 논문 목록에는 공정한 온라인 대전 게임을 위한 데이터 중심 부정행위 방지 프레임워크 RoDAC(KDD 2026), 학년에 맞춘 교사 역할의 대형 언어 모델 Classroom AI(npj Artificial Intelligence 2026), 시간 정보를 묻는 검색의 결과 순서를 다시 매기는 Q-TIE(EMNLP 2026 채택), 산업용 이미지에 레이블을 붙이는 데이터 프로그래밍 기반 시스템 Inspector Gadget(VLDB 2021)이 있다.[^pubs] 대표 논문 2는 위키백과·위키데이터 밖의 특정 응용 분야 데이터로도 대형 언어 모델을 평가할 수 있게 한다고 적는다.[^p2]

## 구성원

2026년 10월 23일 연구실 누리집 Students 페이지 기준이다. Ph.D. Students 칸 7명과 M.S. Students 칸 3명이며, 과정은 누리집 칸을 옮기고 괄호에 누리집이 덧붙인 표기를 적었다. Hyunseo Jeong은 누리집이 M.S. Students 칸에 (Spring 2027)로 적는다. Students 페이지는 구성원의 이메일을 적지 않는다.[^students] Students 페이지는 2022–2026년 구성원의 연구 인턴십으로 NVIDIA Research, Google DeepMind & Youtube, Microsoft Research Asia, Krafton AI, Amazon, NYU Center for Responsible AI를 적는다.[^students] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Min Su Kim | 박사과정 | 6, 7 |
| Jaeyoung Park | 박사과정 | 4, 7 |
| Soyeon Kim | 박사과정 | 1, 2, 3 |
| Junseok Seo | 박사과정 (Lab Leader) | 1 |
| Kahee Lim | 박사과정 |  |
| Jio Oh | 박사과정 | 1 |
| So Young Choi | 박사과정 | 5 |
| Suyeon Seong | 석사과정 |  |
| Seung Hyun Do | 석사과정 |  |
| Hyunseo Jeong | 석사과정 (Spring 2027) |  |

## 졸업생과 이전 구성원

누리집 Students 페이지의 Graduate Alumni, Visiting Student Researcher, Undergraduate Alumni 칸에 이름이 적힌 71줄이다. 박사 5줄, 석사 14줄, 방문 학생 연구원 1줄, 학부생 51줄(학부 졸업 연구 17, 학부생 연구 프로그램 URP 5, 전기및전자공학부 산학 인턴십 개별연구 25, 개별연구 4)이다. 학위 시기와 학위 논문, 첫 직장·진로는 누리집 표기를 옮겼다. Hyunseung Hwang과 Geon Heo는 석사와 박사 두 줄에 모두 있고, 석사 뒤 박사과정을 이어 가는 7명은 위 구성원 표에도 있다. 학부생 줄의 괄호는 누리집이 적은 학기와 산학 인턴십 기관이며 진로가 아니다. 개별연구 칸은 이름 네 개만 적고 모두 95명이라고 적는다.[^students]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Hyunseung Hwang | Ph.D. in Aug. 2026 | New York University (Postdoc @ Center for Responsible AI) | Enhancing Explainability in Machine Learning: Explainable Clustering and Explanation Multiplicity |
| Seong-Hyeon Hwang | Ph.D. in Feb. 2026 | Samsung Research (AI Systems team) | Data Augmentation Strategies for Robust AI under Practical Conditions |
| Geon Heo | Ph.D. in Feb. 2025, Postdoc until Mar. 2025 | Samsung Research (AI Productivity team) | Data-centric Approaches to AI Accuracy, Privacy, Security |
| Yuji Roh | Ph.D. in Feb. 2024, Postdoc until June 2024 | Google Inc. (Youtube, Research Scientist @ DeepMind) | Towards Practical Model Fairness for Trustworthy and Safe AI |
| Ki Hyun Tae | Ph.D. in Feb. 2024 | Samsung Research (Data Intelligence team) | Towards Responsible AI: Data-centric Solutions for Fairness |
| So Young Choi | M.S. in Feb. 2026 | continuing as a Ph.D. student | Misalignment-based Data Augmentation Strategy for Imbalanced Multimodal Learning |
| Seungjun Oh | M.S. in Feb. 2026 | first employment: NAVER Ads Product team | Multi-Agent Contextualization for Time Series Analysis |
| Kahee Lim | M.S. in Feb. 2025 | continuing as a Ph.D. student | Evaluation and Improvement of Response Consistency in Fairness-Related Tasks of Large Language Models |
| Jio Oh | M.S. in Feb. 2025 | continuing as a Ph.D. student | Relational Database based Automatically Verifiable Hallucination Benchmark for Large Language Models |
| Chanho Lee | M.S. in Feb. 2024 | continuing as a Ph.D. student, currently on leave at Krafton Inc. | Robust Label Cleaning on Class Imbalanced Data Using SHAP |
| Junseok Seo | M.S. in Feb. 2024 | continuing as a Ph.D. student | Relaxation Methods of Differential Privacy on Deep Learning Models and Large Language Models |
| Soyeon Kim | M.S. in Feb. 2023 | continuing as a Ph.D. student | Fair and Private Image Data Generation |
| Jaeyoung Park | M.S. in Feb. 2023 | continuing as a Ph.D. student | FairCIL: Fair Few-shot Class-incremental Learning |
| Min Su Kim | M.S. in Feb. 2022 | continuing as a Ph.D. student | Automatic Data Calibration and Selection Techniques for Addressing Drifting Data in Machine Learning |
| Hyunseung Hwang | M.S. in Aug. 2021 | continuing as a Ph.D. student | Automatic and Explainable Data Visualizations for COVID-19 |
| Byungkyu Lee | M.S. in Aug. 2021 | SK Hynix Virtual | An Integrated Framework of Feature and Dataset Selection for Machine Learning |
| Dayun Lee | M.S. in Feb. 2021 | first employment: Samsung LSI | A Fully-Integrated Data Drift Detection and Stitching System for Machine Learning |
| Seonghyeon Hwang | M.S. in Feb. 2021 | continuing as a Ph.D. student | Data Mixing Augmentation Techniques for Regression |
| Geon Heo | M.S. in Feb. 2020 | continued as a Ph.D. student | Massive Image Labeling using Crowdsourcing and Data Programming: A Big Data AI Integration Perspective |
| Aiden Chang | Visiting Student Researcher, Spring-Summer 2024 |  |  |
| DoKyun Lee | Thesis Research, Spring 2026 |  |  |
| Seung Hyun Do | Thesis Research, Fall 2025 |  |  |
| Youngmoo Kim | Thesis Research, Fall 2023 |  |  |
| Beomjoon Yang | Thesis Research, Fall 2023 |  |  |
| Bom Hyeok Lim | Thesis Research, Spring 2023 |  |  |
| Young-Woo Shin | Thesis Research, Spring 2023 |  |  |
| Gyeongseop Shin | Thesis Research, Spring 2023 |  |  |
| Bryan Nathanael Wijaya | Thesis Research, Spring 2023 |  |  |
| Berhane Weldegebriel | Thesis Research, Fall 2022 |  |  |
| Jinhoon Moon | Thesis Research, Fall 2022 |  |  |
| Youngjun Song | Thesis Research, Spring 2021 |  |  |
| Hyo Gyeong Choe | Thesis Research, Spring 2021 |  |  |
| Xinyue Ma | Thesis Research, Spring 2021 |  |  |
| Soyeon Kim | Thesis Research, Spring-Summer 2020 |  |  |
| WonHyeon Kim | Thesis Research, Spring 2020 |  |  |
| Hyun Jin Hwang | Thesis Research, Spring 2019 |  |  |
| Kyeong Ha Rho | Thesis Research, Spring-Fall 2018 |  |  |
| Himani Paudayal | Undergraduate Research Program (URP), Undergraduate Research Program, Winter 2024 - Spring 2025 |  |  |
| Hojin Yu | Undergraduate Research Program (URP), Undergraduate Research Program, Winter 2021-Spring 2022 |  |  |
| Sabina Abdurakhmanova | Undergraduate Research Program (URP), Summer-Fall 2021 |  |  |
| Thao Phuong | Undergraduate Research Program (URP), Summer-Fall 2019 |  |  |
| Mengge Li | Undergraduate Research Program (URP), Spring-Fall 2018 |  |  |
| Yeonil Ryu | KAIST EE Co-op Internship Individual Study, Ocean Drive Studio, Summer 2026 |  |  |
| IkHyeon Cho | KAIST EE Co-op Internship Individual Study, Hankook Tire, Summer 2026 |  |  |
| Wonhyeok Cho | KAIST EE Co-op Internship Individual Study, Hyundai Auto, Summer 2026 |  |  |
| Minho Yang | KAIST EE Co-op Internship Individual Study, Hankook Tire, Summer 2026 |  |  |
| Jae Young Cho | KAIST EE Co-op Internship Individual Study, Samsung Electronics, Summer 2024 |  |  |
| Youngju Yoo | KAIST EE Co-op Internship Individual Study, Naver, Winter 2022 |  |  |
| Seoyeon Kim | KAIST EE Co-op Internship Individual Study, T3Q, Winter 2022 |  |  |
| Yun Jae Won | KAIST EE Co-op Internship Individual Study, Naver, Winter 2022 |  |  |
| Jeongyoub Cha | KAIST EE Co-op Internship Individual Study, Naver, Summer 2022 |  |  |
| Yubin Choi | KAIST EE Co-op Internship Individual Study, Hankook Tire Digital Transformation Team, Summer 2022 |  |  |
| Seunghyun Lee | KAIST EE Co-op Internship Individual Study, Naver, Winter 2021 |  |  |
| Jae Sung Lee | KAIST EE Co-op Internship Individual Study, Samsung Electronics, Winter 2021 |  |  |
| JaeGu Kim | KAIST EE Co-op Internship Individual Study, SelectStar, Summer 2021 |  |  |
| Sawyun Kyae | KAIST EE Co-op Internship Individual Study, SelectStar, Summer 2021 |  |  |
| Seeyeon Kim | KAIST EE Co-op Internship Individual Study, T3Q, Winter 2020 |  |  |
| Jiwon Jung | KAIST EE Co-op Internship Individual Study, Samsung Electronics, Winter 2020 |  |  |
| Sangmin Woo | KAIST EE Co-op Internship Individual Study, SK Telecom ML Infra lab, Summer 2019 |  |  |
| Chanho Lee | KAIST EE Co-op Internship Individual Study, Kakao Corp Recommender Systems Team, Summer 2020 |  |  |
| SeungYeon Cho | KAIST EE Co-op Internship Individual Study, Naver Corp Maps Service Platform Team, Summer 2020 |  |  |
| Youngjong Jeong | KAIST EE Co-op Internship Individual Study, Naver Corp, Winter 2019 |  |  |
| Jun Beum Kim | KAIST EE Co-op Internship Individual Study, SK Telecom, Winter 2019 |  |  |
| Wooseok Cho | KAIST EE Co-op Internship Individual Study, SK Telecom ML Infra lab, Summer 2019 |  |  |
| Min Su Kim | KAIST EE Co-op Internship Individual Study, Naver Corp, Winter 2018 |  |  |
| Jae Hyun Kwak | KAIST EE Co-op Internship Individual Study, SK Telecom, Winter 2018 |  |  |
| Rang Hyun Joh | KAIST EE Co-op Internship Individual Study, SK Telecom, Summer 2018 |  |  |
| Seongjae Seo | Individual Study, Summer 2026 |  |  |
| Hyunseo Jeong | Individual Study, Spring 2026 |  |  |
| Jaeeun Kim | Individual Study, Winter 2024-Summer 2025 |  |  |
| Seung Hyun Do | Individual Study, Summer 2025 |  |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지의 2021–2026년 연도 구역 35편이다(2022년 구역은 없다). 학회 논문(C) 27편, 학술지·학술지형 간행물(J) 7편, 튜토리얼(T) 1편이며, 번호는 [C23]–[C49], [J10]–[J16], [T3]이다. [J14]와 [J15]는 교수가 엮은 IEEE Data Engineering Bulletin 특집호다. 2026년 구역의 [C49]·[C48] 두 편은 누리집이 「Preprint」로 적은 사전 공개 논문이고, NeurIPS 2026의 [C47]·[C46]과 EMNLP 2026의 [C45] 세 편은 누리집이 「Accepted to」로 적은 채택 논문이다. 제목·저자·학회와 학술지 표기는 누리집 그대로이고, 저자 이름 뒤 *는 누리집이 적은 공동 기여 표시다. 교수는 2018년 2월부터 KAIST에 있어 모두 KAIST 재직 시기의 논문이다.[^pubs][^prof]

**2026**

- J. Oh, S. Do, Y. Lee, S. E. Whang, and D. Kang. "Foundations of Proactive Agents: Principles, Technical Layers, and Proactivity-Gym". *Preprint*.
- J. Oh, G. Heo, S. Oh, H. Kim, J. Bak, J. Wang, X. Xie, and S. E. Whang. "Talking with Tables for Better LLM Factual Data Interactions". *Preprint*.
- J. Oh, P. Vicinanza, T. Butler, S. E. Whang, D. Hong, and A. Namboori. "DialectLLM: A Dialect-Aware Dialog[ue] Generation Framework Beyond Standard American English". *Accepted to 40th Annual Conference on Neural Information Processing Systems (NeurIPS), Sydney, Australia, Dec. 2026*.
- H. Hwang, S. Lee, L. Rosenblatt, S. E. Whang, and J. Stoyanovich. "Explanation Multiplicity in SHAP: Characterization and Assessment". *Accepted to 40th Annual Conference on Neural Information Processing Systems (NeurIPS), Sydney, Australia, Dec. 2026*.
- S. Kim, H. Kim, J. Bak, and S. E. Whang. "Q-TIE: A Lightweight and Generalizable Re-ranking Framework for Temporal Information Retrieval". *Accepted to 2026 Conf. on Empirical Methods in Natural Language Processing (EMNLP), Budapest, Hungary, Oct. 2026*.
- M. Kim, J. Park, C. Lee, G. Seo, S. E. Whang, and H. Lee. "RoDAC: A Robust Data-centric Anti-Cheat Framework for Fair Online Competitive Gaming". *In Proc. 32nd ACM SIGKDD Int'l Conf. on Knowledge Discovery and Data Mining (KDD), Jeju, Korea, Aug. 2026*.
- M. Kim, S. Hwang, and S. E. Whang. "GradMix: Gradient-based Selective Mixup for Robust Data Augmentation in Class-Incremental Learning". *In Proc. 32nd ACM SIGKDD Int'l Conf. on Knowledge Discovery and Data Mining (KDD), Jeju, Korea, Aug. 2026*.
- J. Park\*, M. Kim\*, and S. E. Whang. "Fair Class-Incremental Learning using Sample Weighting". *In Proc. 32nd ACM SIGKDD Int'l Conf. on Knowledge Discovery and Data Mining (KDD), Jeju, Korea, Aug. 2026*.
- K. Lim, S. Kim, and S. E. Whang. "DeFrame: Debiasing Large Language Models Against Framing Effects". *In Proc. 64th Annual Meeting of the Association for Computational Linguistics (ACL) Findings, San Diego, California, July 2026*.
- S. Kim, J. Wang, X. Xie, and S. E. Whang. "Harnessing Temporal Databases for Systematic Evaluation of Factual Time-Sensitive Question-Answering in Large Language Models". *In Proc. 14th Int'l Conference on Learning Representations (ICLR), Rio de Janeiro, Brazil, April 2026*.
- J. Oh, S. E. Whang, J. Evans, and J. Wang. "Classroom AI: Large Language Models as Grade-Specific Teachers". *npj Artificial Intelligence 2, 28 (2026) (a Nature Portfolio journal)*.

**2025**

- S. Hwang\*, S. Choi\*, and S. E. Whang. "MIDAS: Misalignment-based Data Augmentation Strategy for Imbalanced Multimodal Learning". *In Proc. 39th Annual Conference on Neural Information Processing Systems (NeurIPS), San Diego, California, Dec. 2025*.
- H. Hwang, A. Bell, J. Fonseca, V. Pliatsika, J. Stoyanovich, and S. E. Whang. "SHAP-based Explanations are Sensitive to Feature Representation". *In Proc. 2025 ACM Conference on Fairness, Accountability, and Transparency (FAccT), Athens, Greece, June 2025*.
- S. Hwang, M. Kim, and S. E. Whang. "T-CIL: Temperature Scaling using Adversarial Perturbation for Calibration in Class-Incremental Learning". *In Proc. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Nashville, Tennessee, June 2025*.
- S. Kim, Y. Roh, G. Heo, and S. E. Whang. "PFGuard: A Generative Framework with Privacy and Fairness Safeguards". *In Proc. 13th Int'l Conference on Learning Representations (ICLR), Singapore, April 2025*.
- S. E. Whang ed. "Special Issue on Large Language Models and Data Systems". *IEEE Data Engineering Bulletin, Mar. 2025*.

**2024**

- J. Oh\*, S. Kim\*, J. Seo, J. Wang, R. Xu, X. Xie, and S. E. Whang. "ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models". *In Proc. 38th Annual Conference on Neural Information Processing Systems (NeurIPS), Dec. 2024. (Spotlight)*.
- S. Hwang, M. Kim, and S. E. Whang. "RC-Mixup: A Data Augmentation Strategy against Noisy Data for Regression Tasks". *In Proc. 30th ACM SIGKDD Int'l Conf. on Knowledge Discovery and Data Mining (KDD), Barcelona, Spain, Aug. 2024*.
- K. Tae, H. Zhang, J. Park, K. Rong, and S. E. Whang. "Falcon: Fair Active Learning using Multi-armed Bandits". *In Proc. 50th Int'l Conf. on Very Large Data Bases (VLDB), Guangzhou, China, Aug. 2024*.
- Y. Roh, Q. Liu, H. Gui, Z. Yuan, Y. Tang, S. E. Whang, L. Liu, S. Bi, L. Hong, E. H. Chi, and Z. Zhao. "LEVI: Generalizable Fine-tuning via Layer-wise Ensemble of Different Views". *In Proc. 41st Int'l Conf. on Machine Learning (ICML), Vienna, Austria, July 2024*.
- S. E. Whang ed. "Special Issue on Data-centric Responsible AI". *IEEE Data Engineering Bulletin, Mar. 2024*.
- M. Kim, S. Hwang, and S. E. Whang. "Quilt: Robust Data Segment Selection against Concept Drifts". *In Proc. 38th AAAI Conference on Artificial Intelligence (AAAI), Vancouver, Canada, Feb. 2024*.

**2023**

- Y. Roh, K. Lee, S. E. Whang, and C. Suh. "Improving Fair Training under Correlation Shifts". *In Proc. 40th Int'l Conf. on Machine Learning (ICML), Honolulu, Hawaii, July 2023*.
- Y. Roh, W. Nie, D. Huang, S. E. Whang, A. Vahdat, A. Anandkumar. "Dr-Fairness: Dynamic Data Ratio Adjustment for Fair Training on Real and Generated Data". *In Proc. Transactions on Machine Learning Research (TMLR), 2023. (New Machine Learning journal)*.
- H. Zhang\*, K. Tae\*, J. Park, X. Chu, and S. E. Whang. "iFlipper: Label Flipping for Individual Fairness". *In Proc. 2023 ACM SIGMOD Int'l Conf. on Management of Data (SIGMOD), Seattle, Washington, June 2023*.
- G. Heo and S. E. Whang. "Redactor: A Data-centric and Individualized Defense Against Inference Attacks". *In Proc. 37th AAAI Conference on Artificial Intelligence (AAAI), Washington, DC, Feb. 2023*.
- H. Hwang and S. E. Whang. "XClusters: Explainability-first Clustering". *In Proc. 37th AAAI Conference on Artificial Intelligence (AAAI), Washington, DC, Feb. 2023*.
- S. E. Whang, Y. Roh, H. Song, and J. Lee. "Data Collection and Quality Challenges in Deep Learning: A Data-Centric AI Perspective". *The VLDB Journal, 2023*.

**2021**

- Y. Roh, K. Lee, S. E. Whang, and C. Suh. "Sample Selection for Fair and Robust Training". *In Proc. 35th Annual Conference on Neural Information Processing Systems (NeurIPS), Dec. 2021*.
- J. Lee, Y. Roh, H. Song, and S. E. Whang. "Machine Learning Robustness, Fairness, and their Convergence (Tutorial)". *In Proc. 27th ACM SIGKDD Int'l Conf. on Knowledge Discovery and Data Mining (KDD), Aug. 2021*.
- S. E. Whang, K. Tae, Y. Roh, and G. Heo. "Responsible AI Challenges in End-to-end Machine Learning". *IEEE Data Engineering Bulletin, Mar. 2021*.
- K. Tae and S. E. Whang. "Slice Tuner: A Selective Data Acquisition Framework for Accurate and Fair Machine Learning Models". *In Proc. 2021 ACM SIGMOD Int'l Conf. on Management of Data (SIGMOD), June 2021*.
- Y. Roh, K. Lee, S. E. Whang, and C. Suh. "FairBatch: Batch Selection for Model Fairness". *In Proc. 9th Int'l Conference on Learning Representations (ICLR), May 2021*.
- G. Heo, Y. Roh, S. Hwang, D. Lee, and S. E. Whang. "Inspector Gadget: A Data Programming-based Labeling System for Industrial Images". *In Proc. 47th Int'l Conf. on Very Large Data Bases (VLDB), Copenhagen, Denmark, Aug. 2021*.
- Y. Roh, G. Heo, and S. E. Whang. "A Survey on Data Collection for Machine Learning: a Big Data - AI Integration Perspective". *In IEEE Transactions on Knowledge and Data Engineering (TKDE), April 2021*.

## 수상

누리집 Students 페이지 Student Awards 칸에서 2021년 10월 이후의 학생 수상 7건이다. 날짜는 누리집이 적은 연·월이고, 괄호는 누리집이 적은 주제다. 교수의 수상은 「교수와 전문 분야」에 적었다.[^students]

- 2026-03 · KAIST Breakthroughs, Jaeyoung Park and Min Su Kim (Improving Fairness in Class-Incremental Learning using Sample Weighting)
- 2026-02 · Best PhD Dissertation Award, College of Engineering, KAIST, Seong-Hyeon Hwang (Data Augmentation Strategies for Robust AI under Practical Conditions)
- 2025-10 · KAIST EE Best TA Award, Jio Oh
- 2024-08 · KAIST Breakthroughs, Seong-Hyeon Hwang and Min Su Kim (AI updates itself by selecting and augmenting the data it trains on)
- 2023-03 · KAIST Breakthroughs, Ki Hyun Tae (Data-centric solutions for Responsible AI: fair data labeling and acquisition)
- 2022-10 · Microsoft Research PhD Fellowship, Yuji Roh
- 2022-04 · KAIST EE 2021 Best Research Achievement Award, Yuji Roh

## 초청 강연과 튜토리얼

누리집 Talks 페이지에서 2021년 12월부터 2025년 11월 사이의 22건이다. 날짜, 강연 제목, 자리 순으로 누리집 표기를 옮겼다. 같은 제목으로 여러 곳에서 한 강연은 따로 적었고, 순서는 누리집이 강연 제목별로 묶은 순서다.[^talks]

- 2025-11 · Data-centric Responsible AI from General ML to LLMs · MSRA workshop @ Stanford University
- 2025-10 · Data-centric Responsible AI from General ML to LLMs · Tech Talk at Systems Research @ Google (SRG)
- 2025-09 · Data-centric Responsible AI from General ML to LLMs · Keynote talk at Workshop on Data-driven AI (DATAI) @ VLDB
- 2025-10 · Data-centric Responsible AI and the NYU Collaboration · NYU Global AI Frontier Lab Workshop
- 2025-10 · Data-centric AI and Database Design: Knowing Your Data · Stanford University CS145 (Intro to Big Data Systems) Guest Lecture
- 2025-05 · Large Language Model Hallucination Benchmarking Research with MSRA · Korea and MSRA Societal AI Workshop
- 2024-12 · ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models (NeurIPS 2024 Spotlight) · Microsoft Research Abstracts Podcast
- 2024-10 · Recent Advances in Data-centric Responsible AI and the NYU-KAIST Collaboration · NYU Center for Responsible AI
- 2024-06 · Towards a Holistic Framework for Data-centric Responsible AI · Keynote talk at Guide-AI Workshop @ ACM SIGMOD
- 2024-02 · Towards a Holistic Framework for Data-centric Responsible AI · Data Lab Seminar @ Northeastern University
- 2023-09 · Towards a Holistic Framework for Data-centric Responsible AI · Samsung Advanced Institute of Technology
- 2023-07 · AI Fairness: Model-centric and Data-centric Approaches · Tutorial at Korean Artificial Intelligence Association Summer Conference
- 2023-04 · Towards a Holistic Framework for Responsible AI · NYU Tandon Center for Responsible AI
- 2023-03 · Towards a Holistic Framework for Responsible AI · Google TFX (US & Korea teams) TechTalk
- 2023-02 · Towards a Holistic Framework for Responsible AI · Seoul National University
- 2022-12 · Towards a Holistic Framework for Responsible AI · Korea-Japan Database (KJDB) Workshop
- 2022-11 · Towards a Holistic Framework for Responsible AI · Microsoft Research Asia Responsible AI Lecture Series
- 2023-02 · Machine Learning Fairness and Its Convergence with Robustness · Tutorial at IEEE Big Data and Smart Computing (BigComp)
- 2022-08 · Data-driven / Responsible AI Research Landscape · Women Tech Stars (Google Explore CSR)
- 2022-06 · Data-driven / Responsible AI Research Landscape · Data-driven AI Workshop at KCC
- 2022-06 · Enterprise Data Management for AI · KAIST AI Chief AI Officer (CAIO) Program
- 2021-12 · Responsible AI: Model-centric and Data-centric Approaches · AI & Fairness panel talk, KAIST International Symposium on AI and Future Society

## 소식

누리집 News 페이지에서 2021년 10월부터 2026년 9월 사이의 66건이다. 날짜는 누리집이 적은 연·월이고, 글은 누리집 표기 그대로다.[^news][^home]

- 2026-09 · Explanation Multiplicity in SHAP: Characterization and Assessment (NYU collaboration) and DialectLLM: A Dialect-Aware Dialog[ue] Generation Framework Beyond Standard American English (Amazon collaboration) accepted to NeurIPS 2026. Congrats Hyunseung Hwang and Jio Oh!
- 2026-09 · Received a Distinguished Associate Editor award for VLDB 2026.
- 2026-08 · Q-TIE: A Lightweight and Generalizable Re-ranking Framework for Temporal Information Retrieval accepted to EMNLP 2026. Congrats Soyeon Kim!
- 2026-08 · Hyunseung Hwang will start his professional career as a Postdoc at the NYU Center for Responsible AI. Congrats and looking forward to a very bright future!
- 2026-07 · Serving as a Senior Associate Editor of IEEE Transactions of Knowledge and Data Engineering (TKDE).
- 2026-05 · RoDAC: A Robust Data-centric Anti-Cheat Framework for Fair Online Competitive Gaming accepted to ACM SIGKDD 2026. Congrats Minsu Kim and Chanho Lee!
- 2026-04 · DeFrame: Debiasing Large Language Models Against Framing Effects accepted to ACL Findings 2026. Congrats Kahee Lim and Soyeon Kim!
- 2026-04 · Serving in the ACM SIGMOD Jim Gray Doctoral Dissertation Awards Committee
- 2026-02 · Seong-Hyeon Hwang will start his professional career at the Samsung Research AI Systems team. Seungjun Oh will start his professional career at the NAVER Ads Product team. Congrats and looking forward to a very bright future!
- 2026-02 · Seong-Hyeon Hwang won the Best PhD Dissertation Award, College of Engineering, KAIST (among 9 in KAIST CoE and only recipient from KAIST EE). Congrats!
- 2026-02 · Classroom AI: Large Language Models as Grade-Specific Teachers accepted to npj Artificial Intelligence (a Nature sub-journal). Congrats Jio Oh!
- 2026-01 · Harnessing Temporal Databases for Systematic Evaluation of Factual Time-Sensitive Question-Answering in Large Language Models accepted to ICLR 2026. Congrats Soyeon Kim!
- 2025-11 · Fair Class-Incremental Learning using Sample Weighting and GradMix: Gradient-based Selective Mixup for Robust Data Augmentation in Class-Incremental Learning accepted to ACM SIGKDD 2026. Congrats Jaeyoung Park, Minsu Kim, and Seong-Hyeon Hwang!
- 2025-10 · Gave a Tech Talk at Systems Research @ Google (SRG) titled Data-centric Responsible AI from General ML to LLMs
- 2025-10 · Gave a Stanford CS145 (Intro to Big Data Systems) Guest Lecture titled Data-centric AI and Database Design: Knowing Your Data
- 2025-09 · MIDAS: Misalignment-based Data Augmentation Strategy for Imbalanced Multimodal Learning accepted to NeurIPS 2025. Congrats Seong-Hyeon Hwang and So Young Choi!
- 2025-09 · Gave the keynote talk Data-centric Responsible AI from General ML to LLMs at the Data-driven AI (DATAI) workshop @ VLDB 2025
- 2025-07 · Started sabbatical as a Visiting Associate Professor at the Stanford University Computer Science department (host: Prof. Christopher Ré).
- 2025-06 · Happy to be part of the creation of the Hector Garcia-Molina SIGMOD Distinguished Mentorship Award.
- 2025-04 · SHAP-based Explanations are Sensitive to Feature Representation accepted to ACM FAccT 2025. Congrats Hyunseung Hwang!
- 2025-03 · The IEEE Data Engineering Bulletin 2025 March Special Issue on Large Language Models and Data Systems is now available (I am the Associate Editor).
- 2025-03 · Geon Heo will start his professional career at the Samsung Research AI Productivity team. Congrats and looking forward to a very bright future!
- 2025-03 · T-CIL: Temperature Scaling using Adversarial Perturbation for Calibration in Class-Incremental Learning accepted to CVPR 2025. Congrats Seong-Hyeon Hwang and Minsu Kim!
- 2025-02 · Suyeon Seong joined our lab. Welcome!
- 2025-01 · PFGuard: A Generative Framework with Privacy and Fairness Safeguards accepted to ICLR 2025. Congrats Soyeon Kim, Yuji Roh, and Geon Heo!
- 2025-01 · Two new videos (lab introduction and recent research) have been posted.
- 2024-12 · Elected as a Y-KAST (Young Korean Academy of Science and Technology) member. Articles in Korean and English.
- 2024-12 · Talked about ERBench (NeurIPS'24 Spotlight) on the Microsoft Research Abstracts podcast.
- 2024-10 · Gave the talk Recent Advances in Data-centric Responsible AI and the NYU-KAIST Collaboration at the NYU Center for Responsible AI.
- 2024-10 · Supported by a new Google Research Award for a year in collaboration with the Core ML team!
- 2024-09 · ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models accepted to NeurIPS 2024 (Spotlight). Congrats Jio Oh, Soyeon Kim, and Junseok Seo!
- 2024-08 · Jaeyoung Park presented our Falcon paper at VLDB 2024, and Seong-Hyeon Hwang and Minsu Kim presented our RC-Mixup paper at ACM SIGKDD 2024.
- 2024-07 · Our lab attended the first Data Intelligence Workshop in Korea.
- 2024-06 · Gave the keynote talk Towards a Holistic Framework for Data-centric Responsible AI at the Guide-AI workshop @ ACM SIGMOD 2024.
- 2024-05 · RC-Mixup: A Data Augmentation Strategy against Noisy Data for Regression Tasks accepted to ACM SIGKDD 2024. Congrats Seong-Hyeon Hwang and Minsu Kim!
- 2024-05 · LEVI: Generalizable Fine-tuning via Layer-wise Ensemble of Different Views accepted to ICML 2024. Congrats Yuji Roh!
- 2024-04 · The IEEE Data Engineering Bulletin 2024 March Special Issue on Data-centric Responsible AI is now available.
- 2024-03 · Seungjun Oh joined our lab. Welcome!
- 2024-03 · Promoted to Tenured Associate Professor.
- 2024-02 · Ki Hyun Tae and Yuji Roh are the first Ph.D. graduates from our lab employed to Samsung Research and Google, respectively. Congrats and looking forward to a very bright future!
- 2023-12 · Falcon: Fair Active Learning using Multi-armed Bandits accepted to VLDB 2024. Congrats Ki Hyun Tae and Jaeyoung Park!
- 2023-12 · Serving as an Associate Editor for VLDB 2025 (PVLDB Volume 18)
- 2023-12 · Quilt: Robust Data Segment Selection against Concept Drifts accepted to AAAI 2024. Congrats Minsu Kim and Seong-Hyeon Hwang!
- 2023-11 · Serving as an Associate Editor for the IEEE TKDE journal
- 2023-11 · The second NYU-KAIST Inclusive AI Center workshop was held at NYU.
- 2023-10 · Supported by a new Google Research Award for a year in collaboration with the TensorFlow Extended (TFX) team!
- 2023-08 · The NYU-KAIST Inclusive AI Center workshop was held at KAIST.
- 2023-06 · Yuji Roh is a research intern at Google DeepMind & Youtube during the summer.
- 2023-04 · Improving Fair Training under Correlation Shifts accepted to ICML 2023. Congrats Yuji Roh!
- 2023-04 · Dr-Fairness: Dynamic Data Ratio Adjustment for Fair Training on Real and Generated Data accepted to Transactions on Machine Learning Research (TMLR), a new Machine Learning journal. Congrats Yuji Roh!
- 2023-03 · Gave a tech talk on Responsible AI to the Google TensorFlow Extended (TFX) US and Korea teams.
- 2022-03 · Kahee Lim and Jio Oh joined our lab. Welcome!
- 2022-12 · Data Collection and Quality Challenges in Deep Learning: A Data-Centric AI Perspective accepted to the VLDB Journal. Congrats Yuji Roh!
- 2022-11 · Gave a tech talk on Responsible AI to Microsoft Research Asia.
- 2022-11 · Two papers Redactor: A Data-centric and Individualized Defense Against Inference Attacks and XClusters: Explainability-first Clustering were accepted to AAAI 2023. Congrats Geon Heo and Hyunseung Hwang!
- 2022-10 · Yuji Roh is a recipient of the prestigious Microsoft Research PhD Fellowship 2022. She is among 36 students worldwide and the only recipient from universities in Korea. Congrats Yuji Roh! (KAIST article English & Korean, interview)
- 2022-10 · Received a KAIST EE Best Teaching Award for EE477 Database and Big Data Systems, Spring 2022 (# students: 64, course rating: 4.84/5, which is highest among all KAIST EE undergrad courses). Supported by a Google Cloud Platform (GCP) Education Grant.
- 2022-08 · iFlipper: Label Flipping for Individual Fairness accepted to ACM SIGMOD 2023. Congrats Ki Hyun Tae and Jaeyoung Park!
- 2022-06 · Supported the ACM Conference on Fairness, Accountability, and Transparency (FAccT 2022) as a Volunteers Co-Chair with all my students being volunteers. There were >120 student volunteers in total. Nice work all!
- 2022-06 · Yuji Roh is a research intern at NVIDIA Research during the summer.
- 2022-06 · Supported by a Google Research Award for a year in collaboration with the TensorFlow Extended (TFX) team!
- 2022-04 · Supported by the Institute for Information & communication Technology Planning & evaluation (IITP) for 5 years (Human-centered AI core technology R&D)
- 2022-04 · Yuji Roh was awarded the KAIST EE 2021 Best Research Achievement Award (Among 6 in KAIST EE, 1 in Computer Division). Congrats Yuji!
- 2022-03 · Junseok Seo and Chanho Lee joined our lab. Welcome!
- 2022-03 · Supported by the National Research Foundation of Korea for 5 years (Mid-Career Researcher Program, PI, Data-centric Trustworthy AI)
- 2021-12 · Gave the talk Responsible AI: Model-centric and Data-centric Approaches at the AI & Fairness panel @ KAIST International Symposium on AI and Future Society with Tulsee Doshi (Head of Product, Google), Kangwook Lee (Professor, Univ. Wisconsin Madison), Been Kim (Research Scientist, Google Brain), and Changho Suh (Professor, KAIST).

## 연락과 위치

- 교수연구실: KAIST IT융합빌딩(N1) 516호, 전화 042-350-7443[^ee][^prof]
- 연구실: KAIST N1 519호[^prof]
- 교수 이메일: swhang@kaist.ac.kr[^ee]
- 누리집 첫 화면은 의욕 있는 석사·박사과정 학생을 찾는다며, 지원 전에 읽을 안내 문서와 추천 과목 목록, 연구실 소개 영상을 함께 걸어 둔다.[^home]
[^p1]: J. Oh 외, S. E. Whang, Advances in Neural Information Processing Systems 37, 53064-53101 (2024). <https://doi.org/10.52202/079017-1681> 초록 기준(arXiv 판 <https://arxiv.org/abs/2403.05266>).
[^p2]: S. Kim, J. Wang, X. Xie, S. E. Whang, International Conference on Learning Representations (ICLR) (2026). <https://www.arxiv.org/abs/2508.02045> 초록 기준(arXiv 판).
[^p3]: S. Kim, Y. Roh, G. Heo, S. E. Whang, International Conference on Learning Representations (ICLR) (2025). <https://arxiv.org/abs/2410.02246> 초록 기준(arXiv 판).
[^p4]: K. H. Tae 외, S. E. Whang, Proceedings of the VLDB Endowment 17, 952-965 (온라인 2024-05-02). <https://doi.org/10.14778/3641204.3641207> 초록 기준.
[^p5]: S.-H. Hwang, S. Choi, S. E. Whang, Advances in Neural Information Processing Systems 38, 164035-164057 (2025). <https://doi.org/10.52202/085713-4942> 초록 기준(arXiv 판 <https://arxiv.org/abs/2509.25831>).
[^p6]: S.-H. Hwang, M. Kim, S. E. Whang, Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, 1155-1165 (온라인 2024-08-24). <https://doi.org/10.1145/3637528.3671993> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: J. Park, M. Kim, S. E. Whang, Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1, 1125-1134 (온라인 2026-04-20). <https://doi.org/10.1145/3770854.3780167> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: H. Hwang 외, S. E. Whang, Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency, 1588-1601 (온라인 2025-06-23). <https://doi.org/10.1145/3715275.3732105> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 연구실 누리집 첫 화면 <https://sites.google.com/view/whanglab/di-lab> (연구실 소개, 학생 모집 안내, Latest News, 2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <https://sites.google.com/view/whanglab/professor> (Biography, Contact Information, Education, Experience, Honors, Professional Service, 2026-10-23 열람)
[^students]: 연구실 누리집 Students 페이지 <https://sites.google.com/view/whanglab/students> (Ph.D.·M.S. Students, Graduate Alumni, Visiting Student Researcher, Student Awards, Student Internships, Undergraduate Alumni, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publications 페이지 <https://sites.google.com/view/whanglab/publications> (논문 목록, 2026-10-23 열람)
[^projects]: 연구실 누리집 Projects 페이지 <https://sites.google.com/view/whanglab/projects> (연구 목표와 연구 갈래별 논문, 2026-10-23 열람)
[^news]: 연구실 누리집 News 페이지 <https://sites.google.com/view/whanglab/news> (2018–2026년 소식, 2026-10-23 열람)
[^talks]: 연구실 누리집 Talks 페이지 <https://sites.google.com/view/whanglab/talks> (2026-10-23 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(황의종) <https://ee.kaist.ac.kr/professor/15612/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 디비전, 학위, 대표업적, 2026-10-23 열람)

# 데이터 사이언스 연구실

**KAIST 전산학부 · 차미영 교수**

- 분야: 데이터 과학, 전산사회과학, 통계분석[^faculty]
- 대분야: 컴퓨팅·AI, 인문·사회·경제
- 태그: 계산 사회과학[^lab][^p7], 대형 언어 모델[^p1][^p8], 위성 원격탐사[^p5], 기후·극한 기상[^p4], 연합학습·분산 학습[^p6], AI·기계학습 보안·프라이버시[^p6], 책임 있는 AI·공정성[^p8]
- 홈페이지: <https://cs.kaist.ac.kr/research/labView?sn=102&menu=64>

> 가짜뉴스와 세관 탈세를 가리고, 위성 영상으로 지역 경제를 추정하며, 인공지능이 사회 속에서 어떻게 판단하고 영향을 주는지 연구하는 연구실이다.

## 무엇을 연구하나

데이터 사이언스 연구실은 빅데이터(대규모로 쌓이는 자료)와 계산 방법으로 사회문제를 다룬다. 학과 소개가 제시하는 대상은 가짜뉴스 탐지, 세관 탈세 선별, 생체 이상 신호 구분, 기후 모델링(기후의 작동과 변화를 계산 모형으로 나타내는 일), 이미지·영상 기반 빈곤 예측이다. 바탕에는 네트워크 과학(대상 사이의 연결 구조와 그 작용을 연구하는 분야), 계산 사회과학(자료와 계산 방법으로 사회 현상을 연구하는 분야), 전산통계(계산을 이용해 자료의 특성을 추정하고 판단하는 통계 방법)가 있다.[^lab]

정보의 내용뿐 아니라 표현 방식과 사람의 판단도 연구한다. 가짜뉴스 탐지에서는 대형 언어 모델(Large Language Model, 많은 글을 학습해 언어를 이해하고 생성하는 인공지능 모델)을 이용해 문체를 바꾸는 공격에 대응하는 학습 자료를 만든다. 기후 허위정보 연구는 기후과학 자체를 부정하는 주장과, 기후변화는 인정하면서 대응 정책을 공격하는 주장을 구분한다. 언어 모델이 옳다고 평가하는 행동, 사람이 할 것이라고 예측하는 행동, 모델 자신이 고르는 행동 사이의 차이도 살핀다.[^p1][^p7][^p8]

현장의 판단을 돕는 연구도 이어진다. 세관에서는 상품의 품목 번호를 제안하면서 담당자가 읽을 수 있는 이유를 제공하고, 나라 사이에서 무역 원자료를 공유하지 않으면서 탈세 탐지에 필요한 지식을 나누는 방법을 제안한다. 위성 영상에서는 마을과 지역의 정보를 결합해 경제 지표를 예측하고, 기후 자료에서는 해상도(자료가 공간을 구분하는 세밀함)를 높이는 계산 방법을 개발한다. 여러 기관의 학습 결과를 함께 쓸 때 악성 참여자의 영향으로부터 각 기관의 학습을 지키는 방법도 연구한다.[^p2][^p3][^p4][^p5][^p6]

## 주요 연구 주제

### 허위정보와 인공지능의 사회적 판단

AdStyle은 뉴스의 뜻을 유지한 채 표현 방식을 바꾸는 공격을 학습 자료에 넣어 탐지기를 훈련하는 방법이다. 언어 모델로 다양한 문체 변환 지시문을 만들고, 탐지기가 구별하기 어려운 사례를 생성한다. 실험에서는 가짜뉴스 자료에서 탐지 성능과 공격에 대한 견고함이 개선됐다.[^p1] 기후 담론 분석에서는 브라질의 유튜브 자료를 바탕으로, 과학적 사실을 부정하는 담론에서 기후 대응책을 공격하는 담론으로의 전환을 관찰했다.[^p7] 또 언어 모델의 도덕적 판단과 인간 행동에 대한 예측이 서로 다르게 나타나며, 모델의 자체 결정은 자신의 인간 행동 예측보다 도덕적 판단을 따르는 경향을 보고했다.[^p8]

### 세관의 상품 분류와 탈세 탐지

상품 분류 연구는 무역 상품에 국제 품목 번호를 부여하는 업무를 돕는다. 분류 번호만 출력하지 않고 담당자가 판단 근거를 읽을 수 있는 문서를 함께 제안한다.[^p2] 탈세 탐지 연구는 도메인 적응(학습에 쓰인 자료와 다른 조건의 자료에도 배운 지식을 적용하는 방법)을 이용한다. 각 나라의 무역 정보를 현지에 두면서, 탈세 사례에서 얻은 대표 특징을 나눠 다른 나라의 탐지를 돕는 방식이다.[^p3]

### 위성 영상과 기후 자료로 지역 상태 추정

위성 영상 연구는 마을의 경제적 특성과 지역 사이의 관계를 함께 배워 인구·구매력·에너지 소비 같은 지표를 추정한다. 지리 단위를 하나만 쓰는 대신 여러 수준의 정보를 결합한다.[^p5] 기후 상세화 연구는 성긴 공간 격자(공간을 구획해 계산값을 배치한 틀)의 계산 결과에서 세밀한 격자의 기후 자료를 만든다. 자기지도학습(자료 자체에서 학습에 필요한 목표를 구성하는 방법)으로 기상 변수(날씨의 상태를 나타내는 양)의 분포(값이 나타나는 양상)와 변수 사이 관계를 이용하며, 고해상도 정답 자료에 의존하지 않는 방법을 제안했다.[^p4]

### 여러 기관이 함께 하는 학습의 안전성

연합학습(기관이나 기기가 자료를 한곳에 모으지 않고 학습 결과를 주고받는 방법)에서는 악성 참여자가 잘못된 모델 갱신을 보내 학습을 방해할 수 있다. FedDefender는 중앙에서 그런 참여자를 가려내는 방어와 함께 쓸 수 있도록, 각 참여 기관 쪽에서 자신의 학습을 보호하는 방법을 제안했다. 악성 갱신의 영향을 견디는 내부 조정과, 오염됐을 수 있는 전체 모델에서 필요한 지식을 추출하는 과정을 결합한다.[^p6]

## 대표 논문

허위정보와 사회적 판단, 세관 업무, 위성·기후 분석, 학습 안전성을 다룬 논문 8편이다. “쉽게 말하면” 칸은 각 논문의 OpenAlex 등록 초록만을 근거로 썼다. 저자 역할은 서지의 저자 순서다.[^bib]

| 번호 | 연도 | 논문 · 발표처 | 쉽게 말하면 | 교수의 저자 위치 |
|---|---|---|---|---|
| 1 | 2025 | [Adversarial Style Augmentation via Large Language Model for Robust Fake News Detection](https://doi.org/10.1145/3696410.3714569) · WWW 2025 | 가짜뉴스의 문체를 바꾸면 기존 탐지기가 속을 수 있다는 문제를 다뤘다. 언어 모델이 다양한 문체 변환 공격 지시문을 만들게 하고, 탐지기에 어려운 사례를 학습 자료로 보태는 AdStyle을 제안했다. 가짜뉴스 평가 자료에서 탐지 성능과 문체 변환 공격에 대한 견고함이 개선됐다.[^p1] | 마지막 저자 |
| 2 | 2024 | [Explainable Product Classification for Customs](https://doi.org/10.1145/3635158) · ACM Trans. Intell. Syst. Technol. | 무역 상품의 국제 품목 번호를 정하는 세관 업무를 돕는 모델을 관세청과 함께 제안했다. 가능한 분류 번호와 담당자가 이해할 수 있는 설명 문서를 함께 제공한다. 분류 요청 사례 평가와 세관 전문가 대상 연구에서, 설명을 동반한 제안이 분류 검토의 시간과 노력을 줄일 수 있음을 보고했다.[^p2] | 마지막 저자 |
| 3 | 2022 | [Knowledge Sharing via Domain Adaptation in Customs Fraud Detection](https://doi.org/10.1609/aaai.v36i11.21465) · AAAI 2022 | 나라별로 축적한 탈세 지식을 나누는 DAS 플랫폼을 제안했다. 무역 원자료를 현지에 두면서 다른 나라에 적용할 수 있는 대표 특징을 공유한다. 여러 나라의 수입 신고 자료로, 공유 지식이 참여국의 탈세 탐지를 도울 수 있음을 시험했다.[^p3] | 마지막 저자 |
| 4 | 2024 | [Self-Supervised Vision for Climate Downscaling](https://doi.org/10.24963/ijcai.2024/825) · IJCAI 2024 | 기후 계산은 계산량 때문에 성긴 공간 격자를 쓰곤 한다. 이 결과를 세밀한 자료로 바꾸기 위해, 고해상도 정답 자료 없이 기상 변수의 분포와 변수 사이 관계를 학습하는 방법을 제안했다. 여러 상세화 배율에서 기존 기준 방법에 비해 성능과 실행 시간이 개선됐다고 보고했다.[^p4] | 마지막 저자 |
| 5 | 2022 | [Learning Economic Indicators by Aggregating Multi-Level Geospatial Information](https://doi.org/10.1609/aaai.v36i11.21464) · AAAI 2022 | 낮에 촬영한 위성 영상으로 경제 지표를 추정한다. 작은 공동체의 경제적 상태를 먼저 배우고, 그 사이의 연결과 지역 수준의 특징을 함께 결합한다. 인구·구매력·에너지 소비 예측을 평가했으며, 한 나라에서 배운 특징을 다른 나라에 적용할 수 있는지도 시험했다.[^p5] | 마지막 저자 |
| 6 | 2023 | [FedDefender: Client-Side Attack-Tolerant Federated Learning](https://doi.org/10.1145/3580305.3599346) · KDD 2023 | 여러 기관이 함께 학습할 때 악성 참여자가 보내는 잘못된 갱신으로부터 각 기관을 지킨다. 각 기관의 학습 조정과 전체 모델에서 지식을 받아들이는 과정을 함께 바꿔 공격의 영향을 줄인다. 중앙의 방어가 공격자를 가려내지 못할 때도 적용할 수 있고, 기존 중앙 방어와 함께 사용할 수 있는 구조다.[^p6] | 마지막 저자 |
| 7 | 2026 | [Mapping Emerging Climate Misinformation Playbooks in the Global South](https://doi.org/10.1145/3805689.3806492) · FAccT 2026 | 브라질의 기후 관련 유튜브 영상 자료와 내용 분석을 결합해 허위정보의 변화를 살폈다. 기후과학을 부정하는 주장뿐 아니라, 기후변화를 인정하면서 재생에너지·기후 정책·환경 옹호자를 공격하는 주장이 늘어나는 전환을 보고했다. 이런 담론이 참여를 끌어내는 방식과 플랫폼의 책임 문제를 논의한다.[^p7] | 공저자 |
| 8 | 2026 | [Machine Behavior in Relational Moral Dilemmas: Moral Rightness, Predicted Human Behavior, and Model Decisions](https://doi.org/10.18653/v1/2026.findings-acl.1547) · ACL Findings 2026 | 언어 모델이 무엇을 도덕적으로 옳다고 보는지, 사람이 어떻게 행동할 것으로 예측하는지, 스스로 무엇을 선택하는지를 비교했다. 도덕적 판단은 공정성을 지향하지만 인간 행동 예측은 관계의 가까움에 따라 충성을 중시하는 방향으로 달라졌다. 모델의 자체 결정은 자신의 행동 예측보다 도덕적 판단을 따르는 경향을 보여, 사회적 맥락을 이해하는 일과 결정에 반영하는 일의 차이를 드러냈다.[^p8] | 마지막 저자 |

## 교수와 전문 분야

차미영 교수는 KAIST 전산학부 교수이며, 학과가 적은 전공은 데이터과학·전산사회과학·통계분석이다. KAIST에서 2008년 박사학위를 받았다.[^faculty][^roster] 2024 ACM Distinguished Member 선정 소식은 차 교수가 2010년 KAIST에 부임했으며 ‘인류를 위한 데이터과학(Humanity for Data Science)’ 연구실을 이끌고, 독일 막스플랑크 연구소에서도 연구를 병행한다고 적는다.[^award] 2025년 8월 학과 소식은 차 교수가 독일에서 ‘막스플랑크 소셜 앤드 컬렉티브 인텔리전스 연구소’를 이끌며 위성 영상 기반 경제지표 탐지와 가짜뉴스 자동 분류 연구를 한다고 소개한다.[^international]

최근 논문에서 드러나는 전문성은 사회적 문제에 맞춘 학습 방법을 만들고 그 판단을 분석하는 일이다. 뉴스의 표현 변화에 흔들리지 않는 탐지, 세관의 설명 가능한 분류와 나라 사이 지식 공유, 위성·기후 자료의 공간적 분석, 여러 기관이 함께 학습할 때의 공격 방어를 다룬다.[^p1][^p2][^p3][^p4][^p5][^p6] 기후 허위정보의 사회적 변화와 언어 모델의 판단 방식도 함께 분석한다.[^p7][^p8]

## 응용 분야

연구 대상은 뉴스의 진위 판단, 세관의 상품 분류와 탈세 위험 선별, 지역 경제와 빈곤의 추정, 기후 자료의 상세화다.[^lab][^p1][^p2][^p3][^p4][^p5] 여러 기관이 자료를 나눠 가진 환경에서 학습의 안전성을 높이는 방법과, 사회적 판단을 돕는 언어 모델의 행동을 평가하는 문제로도 이어진다.[^p6][^p8]

## 최근 논문 목록 (2021–2026)

교수가 KAIST 소속으로 참여한 2021–2026년 논문이다. CoRR 항목은 arXiv 사전 공개본이며, 출판판과 사전 공개본은 각각의 서지 항목으로 적었다.[^bib][^affiliations]

**2026**

- Luiz Felipe Vecchietti, Minji Lee, Begench Hangeldiyev, Bryan Nathanael Wijaya, Hyunkyu Jung, Hahnbeom Park, Tae-Kyun Kim, Meeyoung Cha, Ho Min Kim. "Interpretable Machine Learning for Protein Science: Structure, Function, and Interactions". *ACM Comput. Surv. 58(11): 289:1-289:24 (2026)*.
- Sumin Lee, Sungwon Park, Jeasurk Yang, Jihee Kim, Meeyoung Cha. "Generalizable Slum Detection from Satellite Imagery with Mixture-of-Experts". *AAAI 2026: 38826-38834*.
- Sunguk Shin, Fangzhao Wu, Byung-Jun Lee, Meeyoung Cha, Sungwon Park. "SGT: Securing Open-Source LLMs Against Malicious Fine-tuning via Safety Guidance Trigger". *ACL (1) 2026: 10194-10207*.
- Jiseon Kim, Jea Kwon, Luiz Felipe Vecchietti, Wenchao Dong, Jaehong Kim, Meeyoung Cha. "Machine Behavior in Relational Moral Dilemmas: Moral Rightness, Predicted Human Behavior, and Model Decisions". *ACL (Findings) 2026: 30938-30955*.
- Marcelo Sartori Locatelli, Wenchao Dong, Pedro Loures Alzamora, Pedro Dutenhefner, Wagner Meira Jr., Meeyoung Cha, Virgílio A. F. Almeida. "Mapping Emerging Climate Misinformation Playbooks in the Global South". *FAccT 2026: 4220-4242*.
- Jiseon Kim, Jea Kwon, Luiz Felipe Vecchietti, Wenchao Dong, Jaehong Kim, Meeyoung Cha. "Machine Behavior in Relational Moral Dilemmas: Moral Rightness, Predicted Human Behavior, and Model Decisions". *CoRR abs/2604.21871 (2026)*.
- Marcelo Sartori Locatelli, Wenchao Dong, Pedro Loures Alzamora, Pedro Dutenhefner, Wagner Meira Jr., Meeyoung Cha, Virgílio A. F. Almeida. "Mapping Emerging Climate Misinformation Playbooks in the Global South". *CoRR abs/2604.24223 (2026)*.

**2025**

- Sungwon Park, Sungwon Han, Meeyoung Cha. "Enhancing Domain Generalization for Robust Machine-Generated Text Detection". *IEEE Trans. Knowl. Data Eng. 37(12): 7140-7153 (2025)*.
- Kyeongjin Ahn, Sungwon Han, Sungwon Park, Jihee Kim, Sangyoon Park, Meeyoung Cha. "Generalizable Disaster Damage Assessment via Change Detection with Vision Foundation Model". *AAAI 2025: 27784-27792*.
- Minhyuk Song, Sungwon Han, SeungEon Lee, Donghyun Ahn, Jihee Kim, Meeyoung Cha. "Measuring Fine-Grained Urban Air Temperature with Satellite Imagery". *AAAI 2025: 28397-28404*.
- Wenchao Dong, Megha Sundriyal, Seongchan Park, Jaehong Kim, Meeyoung Cha, Tanmoy Chakraborty, Wonjae Lee. "Parallel Communities Across the Surface Web and the Dark Web". *EMNLP (Findings) 2025: 18199-18218*.
- Sumin Lee, Sungwon Park, Jeasurk Yang, Dongman Lee, Jihee Kim, Meeyoung Cha. "Slum Detection Beyond Labels: A Decade of Poverty Mapping Using Satellite Imagery and Minimal Ground Truth Data". *GoodIT 2025: 41-46*.
- Sumin Lee, Hyoshin Kim, Donghyun Ahn, Donggyu Lee, Jungwon Kim, Hyeok Yun, Chaemin Jang, WoonChul Jung, Dongman Lee, Meeyoung Cha, Jihee Kim. "Tracking Economic Disparities in North Korea: Satellite Imagery Analysis Using AI with Policy Insights". *GoodIT 2025: 155-163*.
- Donghyun Ahn, Sumin Lee, Donggyu Lee, Jungwon Kim, Sungwon Han, SeungEon Lee, Younhyung Chae, Jihee Kim, Meeyoung Cha. "LLM-Driven Socio-Economic Estimation for Visegrád Countries". *GoodIT 2025: 282-287*.
- Sungwon Han, Seungeon Lee, Meeyoung Cha, Sercan Ö. Arik, Jinsung Yoon. "Retrieval Augmented Time Series Forecasting". *ICML 2025*.
- Sungwon Park, Dongjoon Lee, Kyeongjin Ahn, Yubin Choi, Junho Lee, Meeyoung Cha, Kyung Ryul Park. "Classifying and Tracking International Aid Contribution Towards SDGs". *IJCAI 2025: 9845-9852*.
- Sungwon Park, Sungwon Han, Xing Xie, Jae-Gil Lee, Meeyoung Cha. "Adversarial Style Augmentation via Large Language Model for Robust Fake News Detection". *WWW 2025: 4024-4033*.
- Jiseon Kim, Jea Kwon, Luiz Felipe Vecchietti, Alice Oh, Meeyoung Cha. "Exploring Persona-dependent LLM Alignment for the Moral Machine Experiment". *CoRR abs/2504.10886 (2025)*.
- Sungwon Han, Seungeon Lee, Meeyoung Cha, Sercan Ö. Arik, Jinsung Yoon. "Retrieval Augmented Time Series Forecasting". *CoRR abs/2505.04163 (2025)*.
- Sungwon Park, Dongjoon Lee, Kyeongjin Ahn, Yubin Choi, Junho Lee, Meeyoung Cha, Kyung Ryul Park. "Classifying and Tracking International Aid Contribution Towards SDGs". *CoRR abs/2505.15223 (2025)*.
- Donggyu Lee, Sungwon Park, Yerin Hwang, Hyoshin Kim, Hyunwoo Oh, Jungwon Kim, Meeyoung Cha, Sangyoon Park, Jihee Kim. "Benchmarking LLM Causal Reasoning with Scientifically Validated Relationships". *CoRR abs/2510.07231 (2025)*.
- Sumin Lee, Sungwon Park, Jeasurk Yang, Jihee Kim, Meeyoung Cha. "Generalizable Slum Detection from Satellite Imagery with Mixture-of-Experts". *CoRR abs/2511.10300 (2025)*.

**2024**

- Jea Kwon, Sunpil Kim, Dong-Kyum Kim, Jinhyeong Joo, SoHyung Kim, Meeyoung Cha, C. Justin Lee. "SUBTLE: An Unsupervised Platform with Temporal Link Embedding that Maps Animal Behavior". *Int. J. Comput. Vis. 132(10): 4589-4615 (2024)*.
- Kyeongjin Ahn, SeungEon Lee, Sungwon Han, Cheng-Yaw Low, Meeyoung Cha. "Uncertainty-Aware Face Embedding With Contrastive Learning for Open-Set Evaluation". *IEEE Trans. Inf. Forensics Secur. 19: 7176-7186 (2024)*.
- Eunji Lee, Sihyeon Kim, Sundong Kim, Soyeon Jung, Heeja Kim, Meeyoung Cha. "Explainable Product Classification for Customs". *ACM Trans. Intell. Syst. Technol. 15(2): 25:1-25:24 (2024)*.
- Jaehong Kim, Chaeyoon Jeong, Seongchan Park, Meeyoung Cha, Wonjae Lee. "How Do Moral Emotions Shape Political Participation? A Cross-Cultural Analysis of Online Petitions Using Language Models". *ACL (Findings) 2024: 16274-16289*.
- Mingi Shin, Hyojin Chin, Hyeonho Song, Yubin Choi, Junghoi Choi, Meeyoung Cha. "Context-Aware Offensive Language Detection in Human-Chatbot Conversations". *BigComp 2024: 270-277*.
- Minji Lee, Luiz Felipe Vecchietti, Hyunkyu Jung, Hyun Joo Ro, Meeyoung Cha, Ho Min Kim. "Robust Optimization in Protein Fitness Landscapes Using Reinforcement Learning in Latent Space". *ICML 2024: 26976-26990*.
- Karandeep Singh, Chaeyoon Jeong, Naufal Shidqi, Sungwon Park, Arjun Nellikkattil, Elke Zeller, Meeyoung Cha. "Self-Supervised Vision for Climate Downscaling". *IJCAI 2024: 7456-7464*.
- Karandeep Singh, Chaeyoon Jeong, Naufal Shidqi, Sungwon Park, Arjun Nellikkattil, Elke Zeller, Meeyoung Cha. "Self Supervised Vision for Climate Downscaling". *CoRR abs/2401.09466 (2024)*.
- Wenchao Dong, Assem Zhunis, Hyojin Chin, Jiyoung Han, Meeyoung Cha. "I Am Not Them: Fluid Identities and Persistent Out-group Bias in Large Language Models". *CoRR abs/2402.10436 (2024)*.
- Sungwon Han, Hyeonho Song, Sungwon Park, Meeyoung Cha. "FedMID: A Data-Free Method for Using Intermediate Outputs as a Defense Mechanism Against Poisoning Attacks in Federated Learning". *CoRR abs/2404.11905 (2024)*.
- Minji Lee, Luiz Felipe Vecchietti, Hyunkyu Jung, Hyun Joo Ro, Meeyoung Cha, Ho Min Kim. "Robust Optimization in Protein Fitness Landscapes Using Reinforcement Learning in Latent Space". *CoRR abs/2405.18986 (2024)*.
- Kyeongjin Ahn, Sungwon Han, Sungwon Park, Jihee Kim, Sangyoon Park, Meeyoung Cha. "Generalizable Disaster Damage Assessment via Change Detection with Vision Foundation Model". *CoRR abs/2406.08020 (2024)*.
- Sungwon Han, Donghyun Ahn, SeungEon Lee, Minhyuk Song, Sungwon Park, Sangyoon Park, Jihee Kim, Meeyoung Cha. "GeoSEE: Regional Socio-Economic Estimation With a Large Language Model". *CoRR abs/2406.09799 (2024)*.
- Sungwon Park, Sungwon Han, Meeyoung Cha. "Adversarial Style Augmentation via Large Language Model for Robust Fake News Detection". *CoRR abs/2406.11260 (2024)*.
- Wenchao Dong, Assem Zhunis, Dongyoung Jeong, Hyojin Chin, Jiyoung Han, Meeyoung Cha. "Persona Setting Pitfall: Persistent Outgroup Biases in Large Language Models Arising from Social Identity Adoption". *CoRR abs/2409.03843 (2024)*.
- Jeasurk Yang, Sumin Lee, Sungwon Park, Minjun Lee, Meeyoung Cha. "Poverty mapping in Mongolia with AI-based Ger detection reveals urban slums persist after the COVID-19 pandemic". *CoRR abs/2410.09522 (2024)*.

**2023**

- Suyoung Lee, Wonho Song, Suman Jana, Meeyoung Cha, Sooel Son. "Evaluating the Robustness of Trigger Set-Based Watermarks Embedded in Deep Neural Networks". *IEEE Trans. Dependable Secur. Comput. 20(4): 3434-3448 (2023)*.
- Karandeep Singh, SeungEon Lee, Giuseppe (Joe) Labianca, Jesse Michael Fagan, Meeyoung Cha. "Multi-Stage Machine Learning Model for Hierarchical Tie Valence Prediction". *ACM Trans. Knowl. Discov. Data 17(6): 83:1-83:20 (2023)*.
- Sundong Kim, Tung-Duong Mai, Sungwon Han, Sungwon Park, Thi Nguyen Duc Khanh, Jaechan So, Karandeep Singh, Meeyoung Cha. "Active Learning for Human-in-the-Loop Customs Inspection". *IEEE Trans. Knowl. Data Eng. 35(12): 12039-12052 (2023)*.
- Hwaran Lee, Seokhee Hong, Joonsuk Park, Takyoung Kim, Meeyoung Cha, Yejin Choi, Byoung Pil Kim, Gunhee Kim, Eun-Ju Lee, Yong Lim, Alice Oh, Sangchul Park, Jung-Woo Ha. "SQuARe: A Large-Scale Dataset of Sensitive Questions and Acceptable Responses Created through Human-Machine Collaboration". *ACL (1) 2023: 6692-6712*.
- Karandeep Singh, Chaeyoon Jeong, Sungwon Park, Arjun N. Babur, Elke Zeller, Meeyoung Cha. "Self-supervised learning for climate downscaling". *BigComp 2023: 13-17*.
- Vyacheslav Shen, Dong-Kyum Kim, Elke Zeller, Meeyoung Cha. "Neural Classification of Terrestrial Biomes". *BigComp 2023: 163-166*.
- Gabriel Lima, Nina Grgic-Hlaca, Meeyoung Cha. "Blaming Humans and Machines: What Shapes People's Reactions to Algorithmic Harm". *CHI 2023: 372:1-372:26*.
- Donghyun Ahn, Minhyuk Song, SeungEon Lee, Yubin Choi, Jihee Kim, Sangyoon Park, Hyunjoo Yang, Meeyoung Cha. "Fine-Grained Socioeconomic Prediction from Satellite Images with Distributional Adjustment". *CIKM 2023: 3717-3721*.
- Aitolkyn Baigutanova, Diego Sáez-Trumper, Miriam Redi, Meeyoung Cha, Pablo Aragón. "A Comparative Study of Reference Reliability in Multiple Language Editions of Wikipedia". *CIKM 2023: 3743-3747*.
- Karandeep Singh, Yu-Che Tsai, Cheng-Te Li, Meeyoung Cha, Shou-De Lin. "GraphFC: Customs Fraud Detection with Label Scarcity". *CIKM 2023: 4829-4835*.
- Seonyeong Song, Hyeonho Song, Kunwoo Park, Jiyoung Han, Meeyoung Cha. "Detecting Contextomized Quotes in News Headlines by Contrastive Learning". *EACL (Findings) 2023: 685-692*.
- Sungwon Han, Mingi Shin, Sungkyu Park, Changwook Jung, Meeyoung Cha. "Unified Neural Topic Model via Contrastive Learning and Term Weighting". *EACL 2023: 1794-1809*.
- Gabriel Lima, Nina Grgic-Hlaca, Jin Keun Jeong, Meeyoung Cha. "Who Should Pay When Machines Cause Harm? Laypeople's Expectations of Legal Damages for Machine-Caused Harm". *FAccT 2023: 236-246*.
- Sungwon Han, Sungwon Park, Fangzhao Wu, Sundong Kim, Bin Zhu, Xing Xie, Meeyoung Cha. "Towards Attack-tolerant Federated Learning via Critical Parameter Analysis". *ICCV 2023: 4976-4985*.
- Junho Lee, Hyeonho Song, Dongjoon Lee, Sundong Kim, Jisoo Sim, Meeyoung Cha, Kyung Ryul Park. "Machine Learning Driven Aid Classification for Sustainable Development". *IJCAI 2023: 6040-6048*.
- Sungwon Park, Sungwon Han, Fangzhao Wu, Sundong Kim, Bin Zhu, Xing Xie, Meeyoung Cha. "FedDefender: Client-Side Attack-Tolerant Federated Learning". *KDD 2023: 1850-1861*.
- Aitolkyn Baigutanova, Jaehyeon Myung, Diego Sáez-Trumper, Ai-Jou Chou, Miriam Redi, Changwook Jung, Meeyoung Cha. "Longitudinal Assessment of Reference Quality on Wikipedia". *WWW 2023: 2831-2839*.
- Sungwon Han, SeungEon Lee, Fangzhao Wu, Sundong Kim, Chuhan Wu, Xiting Wang, Xing Xie, Meeyoung Cha. "DualFair: Fair Representation Learning at Both Group and Individual Levels via Contrastive Self-supervision". *WWW 2023: 3766-3774*.
- Seonyeong Song, Hyeonho Song, Kunwoo Park, Jiyoung Han, Meeyoung Cha. "Detecting Contextomized Quotes in News Headlines by Contrastive Learning". *CoRR abs/2302.04465 (2023)*.
- Aitolkyn Baigutanova, Jaehyeon Myung, Diego Sáez-Trumper, Ai-Jou Chou, Miriam Redi, Changwook Jung, Meeyoung Cha. "Longitudinal Assessment of Reference Quality on Wikipedia". *CoRR abs/2303.05227 (2023)*.
- Sungwon Han, SeungEon Lee, Fangzhao Wu, Sundong Kim, Chuhan Wu, Xiting Wang, Xing Xie, Meeyoung Cha. "DualFair: Fair Representation Learning at Both Group and Individual Levels via Contrastive Self-supervision". *CoRR abs/2303.08403 (2023)*.
- Gabriel Lima, Nina Grgic-Hlaca, Meeyoung Cha. "Blaming Humans and Machines: What Shapes People's Reactions to Algorithmic Harm". *CoRR abs/2304.02176 (2023)*.
- Karandeep Singh, Yu-Che Tsai, Cheng-Te Li, Meeyoung Cha, Shou-De Lin. "GraphFC: Customs Fraud Detection with Label Scarcity". *CoRR abs/2305.11377 (2023)*.
- Hwaran Lee, Seokhee Hong, Joonsuk Park, Takyoung Kim, Meeyoung Cha, Yejin Choi, Byoung Pil Kim, Gunhee Kim, Eun-Ju Lee, Yong Lim, Alice Oh, Sangchul Park, Jung-Woo Ha. "SQuARe: A Large-Scale Dataset of Sensitive Questions and Acceptable Responses Created Through Human-Machine Collaboration". *CoRR abs/2305.17696 (2023)*.
- Sungwon Park, Sungwon Han, Fangzhao Wu, Sundong Kim, Bin Zhu, Xing Xie, Meeyoung Cha. "FedDefender: Client-Side Attack-Tolerant Federated Learning". *CoRR abs/2307.09048 (2023)*.
- Sungwon Han, Sungwon Park, Fangzhao Wu, Sundong Kim, Bin Zhu, Xing Xie, Meeyoung Cha. "Towards Attack-tolerant Federated Learning via Critical Parameter Analysis". *CoRR abs/2308.09318 (2023)*.
- Donghyun Ahn, Minhyuk Song, SeungEon Lee, Yubin Choi, Jihee Kim, Sangyoon Park, Hyunjoo Yang, Meeyoung Cha. "Fine-Grained Socioeconomic Prediction from Satellite Images with Distributional Adjustment". *CoRR abs/2308.15979 (2023)*.
- Aitolkyn Baigutanova, Diego Sáez-Trumper, Miriam Redi, Meeyoung Cha, Pablo Aragón. "A Comparative Study of Reference Reliability in Multiple Language Editions of Wikipedia". *CoRR abs/2309.00196 (2023)*.
- Eunji Lee, Sihyeon Kim, Sundong Kim, Soyeon Jung, Heeja Kim, Meeyoung Cha. "Explainable Product Classification for Customs". *CoRR abs/2311.10922 (2023)*.

**2022**

- Jaeheon Kim, Donghee Yvette Wohn, Meeyoung Cha. "Understanding and identifying the use of emotes in toxic chat on Twitch". *Online Soc. Networks Media 27: 100180 (2022)*.
- Gabriel Lima, Jiyoung Han, Meeyoung Cha. "Others Are to Blame: Whom People Consider Responsible for Online Misinformation". *Proc. ACM Hum. Comput. Interact. 6(CSCW1): 106:1-106:25 (2022)*.
- Mahmoudreza Babaei, Juhi Kulshrestha, Abhijnan Chakraborty, Elissa M. Redmiles, Meeyoung Cha, Krishna P. Gummadi. "Analyzing Biases in Perception of Truth in News Stories and Their Implications for Fact Checking". *IEEE Trans. Comput. Soc. Syst. 9(3): 839-850 (2022)*.
- Sungwon Park, Sungwon Han, Donghyun Ahn, Jaeyeon Kim, Jeasurk Yang, Susang Lee, Seunghoon Hong, Jihee Kim, Sangyoon Park, Hyunjoo Yang, Meeyoung Cha. "Learning Economic Indicators by Aggregating Multi-Level Geospatial Information". *AAAI 2022: 12053-12061*.
- Sungwon Park, Sundong Kim, Meeyoung Cha. "Knowledge Sharing via Domain Adaptation in Customs Fraud Detection". *AAAI 2022: 12062-12070*.
- Sungwon Han, Sungwon Park, Fangzhao Wu, Sundong Kim, Chuhan Wu, Xing Xie, Meeyoung Cha. "FedX: Unsupervised Federated Learning with Cross Knowledge Distillation". *ECCV (30) 2022: 691-707*.
- Gabriel Lima, Nina Grgic-Hlaca, Jin Keun Jeong, Meeyoung Cha. "The Conflict Between Explainable and Accountable Decision-Making Algorithms". *FAccT 2022: 2103-2113*.
- Sungwon Park, Karandeep Singh, Arjun Nellikkattil, Elke Zeller, Tung-Duong Mai, Meeyoung Cha. "Downscaling Earth System Models with Deep Learning". *KDD 2022: 3733-3742*.
- Assem Zhunis, Gabriel Lima, Hyeonho Song, Jiyoung Han, Meeyoung Cha. "Emotion Bubbles: Emotional Composition of Online Discourse Before and After the COVID-19 Outbreak". *WWW 2022: 2603-2613*.
- Sungkyu Park, Hyeonho Song, Sungwon Han, Berhane Weldegebriel, Lev Manovich, Emanuele Arielli, Meeyoung Cha. "Using Web Data to Reveal 22-Year History of Sneaker Designs". *WWW 2022: 2967-2977*.
- Sungwon Park, Sundong Kim, Meeyoung Cha. "Knowledge Sharing via Domain Adaptation in Customs Fraud Detection". *CoRR abs/2201.06759 (2022)*.
- Sungwon Park, Sungwon Han, Donghyun Ahn, Jaeyeon Kim, Jeasurk Yang, Susang Lee, Seunghoon Hong, Jihee Kim, Sangyoon Park, Hyunjoo Yang, Meeyoung Cha. "Learning Economic Indicators by Aggregating Multi-Level Geospatial Information". *CoRR abs/2205.01472 (2022)*.
- Gabriel Lima, Nina Grgic-Hlaca, Jin Keun Jeong, Meeyoung Cha. "The Conflict Between Explainable and Accountable Decision-Making Algorithms". *CoRR abs/2205.05306 (2022)*.
- Sungwon Han, Sungwon Park, Fangzhao Wu, Sundong Kim, Chuhan Wu, Xing Xie, Meeyoung Cha. "FedX: Unsupervised Federated Learning with Cross Knowledge Distillation". *CoRR abs/2207.09158 (2022)*.

**2021**

- Seunghyun Yoon, Kunwoo Park, Minwoo Lee, Taegyun Kim, Meeyoung Cha, Kyomin Jung. "Learning to Detect Incongruence in News Headline and Body Text via a Graph Neural Network". *IEEE Access 9: 36195-36206 (2021)*.
- Oh-Hyun Kwon, Inho Hong, Jeasurk Yang, Donghee Yvette Wohn, Woo-Sung Jung, Meeyoung Cha. "Urban green space and happiness in developed countries". *EPJ Data Sci. 10(1): 28 (2021)*.
- Hyeonho Song, Kunwoo Park, Meeyoung Cha. "Finding epic moments in live content through deep learning on collective decisions". *EPJ Data Sci. 10(1): 43 (2021)*.
- Yuan Yuan, Muzhi Guan, Zhilun Zhou, Sundong Kim, Meeyoung Cha, Depeng Jin, Yong Li. "Disruption in Chinese E-Commerce During COVID-19". *Frontiers Comput. Sci. 3: 668711 (2021)*.
- Gabriel Lima, Assem Zhunis, Lev Manovich, Meeyoung Cha. "On the Social-Relational Moral Standing of AI: An Empirical Study Using AI-Generated Art". *Frontiers Robotics AI 8: 719944 (2021)*.
- Gabriel Lima, Meeyoung Cha, Chihyung Jeon, Kyungsin Park. "The Conflict Between People's Urge to Punish AI and Legal Systems". *Frontiers Robotics AI 8: 756242 (2021)*.
- Sungwon Park, Sungwon Han, Sundong Kim, Danu Kim, Sungkyu Park, Seunghoon Hong, Meeyoung Cha. "Improving Unsupervised Image Clustering With Robust Learning". *CVPR 2021: 12278-12287*.
- Changwook Jung, Inho Hong, Diego Sáez-Trumper, Damin Lee, Jaehyeon Myung, Danu Kim, Jinhyuk Yun, Woo-Sung Jung, Meeyoung Cha. "Information flow on COVID-19 over Wikipedia: A case study of 11 languages". *WWW (Companion Volume) 2021: 627-628*.
- Sungkyu Park, Jamie Yejean Park, Hyojin Chin, Jeong-han Kang, Meeyoung Cha. "An Experimental Study to Understand User Experience and Perception Bias Occurred by Fact-checking Messages". *WWW 2021: 2769-2780*.
- Suyoung Lee, Wonho Song, Suman Jana, Meeyoung Cha, Sooel Son. "Evaluating the Robustness of Trigger Set-Based Watermarks Embedded in Deep Neural Networks". *CoRR abs/2106.10147 (2021)*.
- Eunji Lee, Sundong Kim, Sihyun Kim, Sungwon Park, Meeyoung Cha, Soyeon Jung, Suyoung Yang, Yeonsoo Choi, Sungdae Ji, Minsoo Song, Heeja Kim. "Classification of Goods Using Text Descriptions With Sentences Retrieval". *CoRR abs/2111.01663 (2021)*.

## 수상과 선정

2021년 10월 13일부터 2026년 10월 13일까지의 수상·선정이다. 연도만 적힌 항목은 그 연도를 표시했다.[^award]

- 2024 · 차미영 교수, ACM Distinguished Member(특훈회원) 선정

## 연락과 위치

- 교수연구실: KAIST E3-1, 2425호[^faculty][^roster]
- 연구실 소개 쪽 전화: 042-350-3574[^lab]
- 주소: 대전광역시 유성구 대학로 291, KAIST 전산학부[^lab]

## 각주
[^lab]: KAIST 전산학부, 데이터 사이언스 연구실 소개. 사회문제·연구 대상·기초 방법론·전화·주소. <https://cs.kaist.ac.kr/research/labView?sn=102&menu=64> 열람 2026-10-28.
[^faculty]: KAIST 전산학부, 차미영 교수 소개. 직위·학위·전공·교수연구실. <https://cs.kaist.ac.kr/people/view?idx=418&kind=faculty&menu=160> 열람 2026-10-28.
[^roster]: KAIST 전산학부 교수진 명단, 차미영 교수 항목. <https://cs.kaist.ac.kr/people/faculty> 관측 2026-10-27.
[^bib]: dblp, Meeyoung Cha. 2021–2026년 구역의 논문 서지와 전체 저자 순서. ORCID 0000-0003-4085-9648. <https://dblp.org/pid/57/4924.html> 열람 2026-10-28. 교신·책임저자 역할은 이 서지에서 추정하지 않았다.
[^affiliations]: OpenAlex, ORCID 0000-0003-4085-9648 저자의 2021–2026년 논문 기록. 저자 소속은 논문 서지에서 얻은 값이다. <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0003-4085-9648,publication_year:2021-2026> 수집 2026-10-27, 소속 대조 2026-10-28.
[^award]: KAIST 전산학부, 「차미영 교수, 2024 ACM Distinguished Member 선정」. 연구실 명칭·KAIST 부임·독일 연구 병행·선정 사실. <https://cs.kaist.ac.kr/spotlights/research?menu=&page=3> 열람 2026-10-28.
[^international]: KAIST 전산학부, 「AI, 여성에게 무한한 기회 열어줘…제한 없이 도전해야」, 2025년 8월 소개. 독일 연구 활동과 연구 주제. <https://cs.kaist.ac.kr/spotlights/people?menu=&page=2> 열람 2026-10-28.
[^p1]: S. Park 외, M. Cha, WWW 2025, 4024-4033 (2025). <https://doi.org/10.1145/3696410.3714569> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0003-4085-9648,publication_year:2021-2026>.
[^p2]: E. Lee 외, M. Cha, ACM Trans. Intell. Syst. Technol. 15, 25:1-25:24 (2024). <https://doi.org/10.1145/3635158> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0003-4085-9648,publication_year:2021-2026>.
[^p3]: S. Park, S. Kim, M. Cha, AAAI 2022, 12062-12070 (2022). <https://doi.org/10.1609/aaai.v36i11.21465> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0003-4085-9648,publication_year:2021-2026>.
[^p4]: K. Singh 외, M. Cha, IJCAI 2024, 7456-7464 (2024). <https://doi.org/10.24963/ijcai.2024/825> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0003-4085-9648,publication_year:2021-2026>.
[^p5]: S. Park 외, M. Cha, AAAI 2022, 12053-12061 (2022). <https://doi.org/10.1609/aaai.v36i11.21464> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0003-4085-9648,publication_year:2021-2026>.
[^p6]: S. Park 외, M. Cha, KDD 2023, 1850-1861 (2023). <https://doi.org/10.1145/3580305.3599346> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0003-4085-9648,publication_year:2021-2026>.
[^p7]: M. S. Locatelli 외, V. A. F. Almeida, FAccT 2026, 4220-4242 (2026). <https://doi.org/10.1145/3805689.3806492> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0003-4085-9648,publication_year:2021-2026>.
[^p8]: J. Kim 외, M. Cha, ACL (Findings) 2026, 30938-30955 (2026). <https://doi.org/10.18653/v1/2026.findings-acl.1547> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0003-4085-9648,publication_year:2021-2026>.

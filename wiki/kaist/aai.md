# 응용인공지능 연구실 (Applied Artificial Intelligence Laboratory, AAILab)

**KAIST AX학과·산업및시스템공학과·안보과학기술대학원 · 문일철 교수**

- 분야: 확산 모델을 비롯한 심층 생성 모델의 학습과 표본 생성, 잡음 레이블 학습·데이터셋 증류 같은 불완전한 데이터와 데이터 효율 학습, 대규모 언어 모델의 정렬과 지식 증류, 다중 에이전트 강화학습, 이산 사건·행위자 기반 모델링과 시뮬레이션(M&S)과 그 사회·경제·국방 시스템 응용
- 대분야: 컴퓨팅·AI, 산업·시스템
- 태그: 생성 인공지능[^ax][^p1][^p2], 대형 언어 모델[^p5][^p6], 강화학습[^p7][^p6], 계산 사회과학[^home][^research]
- 홈페이지: <https://aai.kaist.ac.kr/>
- 근거와 출처: [AAILab 근거 페이지](aai-sources.md)

> 생성 모델, 불완전한 데이터에서의 학습, 대규모 언어 모델, 다중 에이전트 강화학습 같은 기계학습 방법을 개발하고,[^ax][^p1][^p3][^p5][^p7] 복잡한 사회·경제 시스템과 국방 조직을 컴퓨터 모형으로 재현해 이해하고 설계하는 모델링·시뮬레이션을 함께 연구하는 KAIST 연구실이다.[^research][^p8]

## 무엇을 연구하나

연구실은 KAIST 문일철 교수가 이끄는 연구실이다.[^members][^ax] 누리집은 제목에 국문 이름 「카이스트 응용인공지능 연구실」을 쓰고, 영문 이름을 Applied Artificial Intelligence Laboratory로 적으며 약칭 AAILab을 쓴다.[^home][^contact] 누리집 첫 화면과 Research 페이지는 연구실이 우리 사회의 복잡한 사회·경제 시스템을 어떻게 이해하고 설계하고 관리할지를 연구한다고 소개하고, 그런 시스템의 예로 산업 조직, 군·정보 조직, 새로 생겨나는 스마트 시장, 주식 시장과 그 투자자, 사이버 공간의 소셜 미디어를 든다.[^home][^research] Research 페이지는 시스템의 크기와 그 안의 상호작용이 커지면서 사람의 통찰과 지혜에 계산 방법론의 뒷받침이 필요해졌다고 보고, 연구 목표로 복잡한 사회·경제 시스템을 이해·설계·관리하는 새 계산 방법론을 만드는 일과 그 방법론을 실제 시스템에 적용하는 일을 들며, 방법으로 사회 연결망 분석(사람이나 조직 사이의 관계를 점과 선으로 나타내 그 구조를 분석하는 방법), 행위자 기반 모델링과 시뮬레이션(개별 행위자와 그들이 상호작용하는 규칙을 정해 시스템 전체의 움직임을 컴퓨터로 재현하는 방법), 멀티미디어 데이터 마이닝(여러 형태의 미디어 자료에서 쓸모 있는 규칙과 패턴을 찾아내는 일), 위험 관리를 위한 베이지안 네트워크(변수들 사이의 조건부 확률 관계를 화살표로 이은 그래프로 나타낸 확률 모형)를 든다.[^research] 누리집의 논문 목록은 논문을 Machine Learning과 Agent Modeling 두 분류로 나눈다.[^pubs] KAIST AI대학 AX학과 교수진 페이지는 교수의 연구분야를 Generative Model / Probabilistic Model로, 핵심 AI 역량을 Generative AI & Inverse Design, Data-Centric AI, Foundation Models, Multi-Agent Systems로 적고,[^ax] 안보과학기술대학원 교수 명단은 연구분야를 인공지능/무인체계로, 세부 연구 분야를 메타학습(여러 과제에서 얻은 학습 경험을 바탕으로 새 과제를 배우는 방법 자체를 학습하는 일)과 생성모델(학습 데이터의 분포를 배워 그 분포를 따르는 새 데이터를 만들어 내는 모델)로 적는다.[^gst] KAIST 연구자 포털은 교수의 연구 관심을 Modeling and Simulation, Deep Generative Model, Artificial Intelligence, Robotics로 적는다.[^pure]

첫째 갈래는 **확산 모델의 학습과 표본 생성**이다. 확산 모델은 데이터에 잡음을 단계적으로 더하는 과정을 거꾸로 되돌리도록 학습해 새 데이터를 만드는 생성 모델이다. 누리집 첫 화면의 Research area는 대표 연구를 소개하며 확산 모델, 추론 시점 확장(inference-time scaling, 학습이 끝난 모델로 결과를 만들 때 들이는 계산을 늘려 결과의 질을 높이는 방법), 기각 표본추출(rejection sampling, 뽑은 표본을 정해진 확률에 따라 받아들이거나 버려 목표 분포의 표본을 얻는 방법), 메트로폴리스-헤이스팅스 알고리즘(현재 표본에서 새 후보를 제안하고 정해진 확률로 받아들이거나 버리기를 되풀이해 목표 분포의 표본을 얻는 방법), 안전한 이미지 생성 같은 키워드를 붙인다.[^home] 대표 논문에서는 이미 학습한 확산 모델이 표본을 만들 때 판별기(주어진 표본이 실제 데이터인지 모델이 만든 것인지 가려내도록 학습한 신경망)가 표본 경로의 사실성을 알려 주도록 해 생성 품질을 높이는 판별기 안내(Discriminator Guidance)를 내놓았고,[^p1] 표본 생성의 단계마다 표본의 질을 평가해 받아들이거나 다시 다듬는 확산 기각 표본추출(DiffRS)을 만들었다.[^p2] 최근 논문 목록에는 점수(score, 데이터 분포의 로그 확률 밀도를 데이터에 대해 미분한 값) 기반 확산 모델의 학습 기법(Soft Truncation, ICML 2022), 편향된 데이터셋에서 편향 없는 확산 모델을 학습하는 연구와 잡음 레이블에 강건한 확산 모델(ICLR 2024), 확산 모델로 비지도 표현 학습(정답 표시가 없는 자료에서 자료의 특징 표현을 배우는 일)을 하는 Diffusion Bridge AutoEncoders(ICLR 2025), 글로 그림을 만드는 확산 모델의 텍스트 임베딩(글을 신경망이 다루는 수치 벡터로 바꾼 것)을 다루는 연구 두 편(NeurIPS 2025), 메트로폴리스-헤이스팅스 알고리즘으로 표본 생성을 빠르게 하고 바로잡는 AC-Sampler(ICLR 2026), 시험 시점의 표본 보상 안내(ICML 2026)도 있다.[^pubs]

둘째 갈래는 **불완전한 데이터와 데이터 효율 학습**이다. 정답 표시 가운데 일부가 틀린 잡음 레이블, 학습 때와 분포가 다른 자료, 계산과 저장 비용이 큰 대규모 데이터셋처럼 학습 자료에 결함이 있거나 비용이 클 때 모델을 학습시키는 방법을 다룬다.[^p3][^p4][^members] 대표 논문에서는 잡음 레이블과 깨끗한 레이블의 관계를 나타낸 전이 행렬을 재표본추출(resampling, 자료에서 표본을 다시 뽑아 학습에 쓰는 방법)로 활용하는 RENT를 내놓았고,[^p3] 큰 데이터셋의 필요한 정보를 신경장(neural field, 좌표를 입력받아 그 위치의 값을 내놓는 신경망으로 신호를 나타내는 방법)에 담아 작은 합성 데이터셋으로 압축하는 데이터셋 증류 방법 DDiF를 만들었다.[^p4] 연구실 구성원 페이지의 연구 관심에도 잡음 레이블 학습, 양성-미표시 학습(Positive-Unlabeled Learning, 레이블이 붙은 양성 표본과 레이블이 없는 표본만으로 분류기를 학습하는 방법), 분포 이동(학습 자료와 실제로 다룰 자료의 분포가 서로 달라지는 일), 데이터셋 증류, 코어셋 선택(전체 데이터셋을 대신해 학습에 쓸 대표 부분 집합을 고르는 일)이 있다.[^members] 최근 논문 목록에는 생성 모델로 잡음 예측을 바로잡는 연구(ICML 2022), 주파수 영역(신호를 주파수 성분별로 나누어 나타낸 표현)에서 데이터셋을 증류하는 FreD(NeurIPS 2023), 손실 곡률(모델 매개변수가 바뀔 때 손실 값의 그래프가 휘어진 정도)을 맞춰 데이터셋을 고르고 줄이는 연구(AISTATS 2023), 능동 학습(정답을 붙일 자료를 모델이 골라 가며 학습하는 방법) 연구 두 편(NeurIPS 2021, ICML 2023), 학습 때 보지 못한 도메인(자료가 나온 환경이나 분포)으로의 일반화(ICLR 2024)와 열린 집합 도메인 적응(학습 자료에 없던 클래스가 섞인 새 도메인의 자료에 모델을 맞추는 일, NeurIPS 2022)도 있다.[^pubs]

셋째 갈래는 **대규모 언어 모델의 정렬과 지식 증류**다. 정렬은 언어 모델의 출력이 사람의 선호와 의도에 맞도록 조정하는 일을 말한다. 대표 논문에서는 큰 교사 언어 모델의 지식을 작은 학생 모델에 옮기는 지식 증류에서 교사와 학생 사이에 두는 보조 분포를 일반화한 AMiD를 내놓았고,[^p5] 사람의 선호로 언어 모델을 강화학습(행동의 결과로 받는 보상을 바탕으로 시행착오를 거치며 행동 방식을 배우는 기계학습 방법)시킬 때 기준 정책(상황에 따라 어떤 행동이나 출력을 낼지 정하는 규칙)과의 차이를 토큰(언어 모델이 글을 처리하는 낱낱의 단위)의 의미까지 고려해 재는 정칙화(학습 목표에 벌점 항을 더해 해가 원하는 성질을 갖게 하는 방법) 기법인 바서슈타인 정책 정칙화(WPR)를 제안했다.[^p6] 최근 논문 목록에는 구체 점수 맞춤(concrete score matching, 이산 자료에서 한 값과 그 이웃 값들의 확률 비율을 모델이 맞추도록 학습하는 방법)으로 대규모 언어 모델을 증류하는 연구(ICLR 2026), 바서슈타인 거리(한 분포를 다른 분포로 옮기는 데 드는 최소 이동 비용으로 정한 두 확률 분포 사이의 거리) 기반의 지식 증류 WASD(누리집 표기 NeurIPS 2026), 데이터 분포의 비율을 추정하는 선호 최적화(사람이 고른 선호 응답 자료로 모델을 조정하는 방법, NeurIPS 2025), 여러 문서에 걸친 관계 추출(글에서 개체 사이의 관계를 찾아내는 일, ACL 2024)과 시각-언어 모델의 프롬프트 학습(모델에 넣는 입력 문구나 그 벡터를 학습해 과제에 맞추는 방법, AAAI 2024)도 있다.[^pubs] 2024년 연구팀은 멀티모달(텍스트·이미지 등 서로 다른 형태의 정보를 함께 다루는) 대규모 모델의 미세 조정(이미 학습한 모델을 특정 자료로 추가 학습시키는 일) 연구 결과를 적용해 ICML 2024의 멀티모달 작업계획 생성 경진대회(EgoPlan)에서 우승했고,[^news-icml24] 2026년에는 여러 AI 파운데이션 모델(대규모 데이터를 학습해 다양한 작업에 활용할 수 있는 범용 AI 모델)을 각각 독립적인 에이전트(스스로 판단하고 행동하는 주체)로 구성해 서로 답을 검증하고 토론하게 하는 멀티에이전트 구조로 ICML 2026 워크숍의 시각적 물리 문제 풀이 챌린지에서 우승했다.[^news-icml26]

넷째 갈래는 **다중 에이전트 강화학습과 모델링·시뮬레이션**이다. 다중 에이전트 강화학습은 여러 행위 주체가 함께 행동하며 시행착오로 보상을 키우는 행동을 배우는 강화학습이다. 대표 논문에서는 에이전트가 자신이 겪는 궤적(시간에 따라 이어지는 관측과 행동의 순서열)의 종류를 알아내 과제 유형을 인식하고 그 정보를 행동에 쓰게 하는 TRAMA를 내놓았고,[^p7] 인공지능 학습용 시뮬레이터에서 모델의 결합 구조를 실행 중에 바꿔 무인 수상정(USV, 사람이 타지 않고 물 위를 다니는 배) 시뮬레이션을 빠르게 하는 DEVS(시스템을 사건이 일어날 때마다 상태가 바뀌는 모델들과 그 결합으로 기술하는 이산 사건 시스템 명세 형식론) 기반 가속 기법을 만들었다.[^p8] 최근 논문 목록에는 일화 기억(과거에 겪은 개별 경험을 저장해 두었다가 꺼내 쓰는 기억)을 효율적으로 쓰는 협력형 다중 에이전트 강화학습(ICLR 2024)과 잠재 목표(자료의 특징을 압축해 나타낸 공간 속에서 정한 목표 상태)가 이끄는 다중 에이전트 강화학습 LAGMA(ICML 2024), 무기–표적 할당 문제(여러 무기를 여러 표적에 배정하는 조합 최적화 문제)를 강화학습으로 푸는 연구(Journal of Aerospace Information Systems, 2023·2026), 행위자 기반 모델의 매개변수를 자동으로 보정(모델의 출력이 관측 자료와 맞도록 매개변수 값을 정하는 일)하는 연구(Autonomous Agents and Multi-Agent Systems, 2021; AAMAS 2022), 다리 건설의 교통 분산 효과를 다룬 도시 행정 행위자 기반 모델(Journal of Artificial Societies and Social Simulation, 2022), 금융과 시장 집중을 다룬 행위자 기반 모델(같은 학술지, 2025), 세종시 자동 쓰레기 수거 시스템의 디지털 트윈(실제 시설이나 시스템을 컴퓨터 안에 재현하고 관측 자료와 연결해 시험과 예측에 쓰는 모형) 모델링과 보정(ANNSIM 2023)도 있다.[^pubs] 교수는 군집체계(여러 개체가 무리를 이뤄 함께 임무를 수행하도록 묶은 체계)를 연구하는 국방 지능형 군집체계 연구센터의 센터장이며, 이 센터 누리집은 교수의 연구 분야를 AI/M&S 연구, 군집체계 학습용 M&S 연구, 군집체계 AI연구로 적는다.[^disc] 연구실이 만든 AI 드론과 공중전 시뮬레이터는 2025년 KAIST Institute의 Prototype 우수상을 받았다.[^aw-proto]

## 주요 연구 주제

### 1. 확산 모델의 학습과 표본 생성

판별기 안내와 확산 기각 표본추출처럼 이미 학습한 확산 모델의 표본 생성을 개선하는 방법, 편향되거나 잡음 섞인 데이터에서 확산 모델을 학습하는 방법, 글로 그림을 만드는 확산 모델의 안내.[^home][^p1][^p2][^pubs]

### 2. 불완전한 데이터와 데이터 효율 학습

전이 행렬을 활용한 잡음 레이블 학습, 신경장과 주파수 영역을 이용한 데이터셋 증류, 도메인 일반화와 능동 학습.[^p3][^p4][^members][^pubs]

### 3. 대규모 언어 모델의 정렬과 지식 증류

보조 분포를 일반화한 언어 모델 지식 증류, 토큰의 의미를 고려하는 사람 선호 정렬, 멀티모달 대규모 모델의 미세 조정.[^p5][^p6][^news-icml24]

### 4. 다중 에이전트 강화학습과 모델링·시뮬레이션

궤적의 종류를 인식하는 다중 에이전트 강화학습, 인공지능 학습용 시뮬레이션의 가속, 사회·경제 시스템과 국방 조직의 행위자 기반 모델링.[^p7][^p8][^research][^disc]

## 대표 논문

누리집 논문 목록의 2021–2026년 논문 가운데 문일철 교수가 마지막 저자인 학회 논문을 네 연구 갈래에 두 편씩 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2023 | [Refining Generative Process with Discriminator Guidance in Score-based Diffusion Models](https://arxiv.org/abs/2211.17091) · ICML 2023 | 제안한 판별기 안내(Discriminator Guidance)는 이미 학습한 확산 모델의 표본 생성을 개선하려는 방법이다. 잡음을 걷어 내며 표본을 만드는 경로가 실제 데이터처럼 보이는지 아닌지를 판별기가 명시적으로 알려 준다. GAN(생성자와 판별기를 서로 겨루게 하며 함께 학습시키는 생성 모델)과 달리 점수 신경망과 판별기를 함께 학습할 필요가 없다. 대신 점수 학습이 끝난 뒤 판별기를 학습하므로 판별기 학습이 안정적이고 빨리 수렴한다. 표본을 만들 때는 판별기를 속이도록 하는 보조 항을 이미 학습한 점수에 더한다. 이 항은 판별기가 최적일 때 모델의 점수를 데이터의 점수로 바로잡아 주므로, 판별기가 점수 추정을 보완하는 방식으로 돕는다는 뜻이다. 이 방법으로 256×256 해상도의 ImageNet에서 FID(생성 이미지와 실제 이미지의 특징 분포 사이 거리를 재는 지표) 1.83, 재현율(recall, 생성 표본이 실제 데이터 분포를 덮는 정도를 나타내는 지표) 0.64로 최고 수준(state-of-the-art)의 결과를 얻었고, 이는 검증 데이터의 FID 1.68, 재현율 0.66과 비슷하다.[^p1] | 1저자 D. Kim, 마지막 저자 문일철 |
| 2 | 2024 | [Diffusion Rejection Sampling](https://pure.kaist.ac.kr/en/publications/diffusion-rejection-sampling/) · ICML 2024 | 강력한 사전 학습 확산 모델이 나오면서, 잘 학습된 확산 모델 아래에서 표본 생성 성능을 높이는 방법의 개발이 활발해졌다. 이 논문은 단계마다 표본 생성의 전이 커널(한 단계의 상태에서 다음 단계의 상태로 옮겨 갈 확률을 정한 분포)을 참 전이 커널에 맞추는 기각 표본추출 방식의 확산 기각 표본추출(DiffRS)을 소개한다. 이 방법은 중간 단계마다 표본의 질을 평가하고, 표본에 따라 들이는 노력을 달리해 표본을 다듬는 장치로 볼 수 있다. 이론 분석에서 DiffRS가 사전 학습 모델보다 더 좁은 표본 생성 오차 한계를 얻을 수 있음을 보였다. 실험에서 벤치마크 데이터셋에서 최고 수준의 성능을 냈고, 빠른 확산 표본 생성기와 대규모 글-이미지 확산 모델에서도 효과가 있음을 보였다.[^p2] | 1저자 B. Na, 마지막 저자 문일철 |
| 3 | 2024 | [Dirichlet-based Per-Sample Weighting by Transition Matrix for Noisy Label Learning](https://pure.kaist.ac.kr/en/publications/dirichlet-based-per-sample-weighting-by-transition-matrix-for-noi/) · ICLR 2024 | 잡음 레이블(학습 자료에 붙은 정답 표시 가운데 틀린 것)로 학습할 때는 잡음 레이블 분포와 깨끗한 레이블 분포의 관계를 명시적으로 모형화한 전이 행렬(깨끗한 레이블이 각 잡음 레이블로 바뀌어 붙을 확률을 모은 행렬)이 분류기나 위험(risk, 모델의 손실을 데이터 분포에 대해 평균한 값)의 통계적 일관성(자료의 수가 한없이 늘어날 때 추정이 참값으로 수렴하는 성질)을 얻는 데 쓰여 왔다. 이전 연구는 전이 행렬을 어떻게 쓰느냐보다 어떻게 잘 추정하느냐에 더 집중했다. 연구팀은 전이 행렬을 잘 활용하는 일이 중요하다고 보고, 재표본추출에 바탕을 둔 새 활용법 RENT를 제안했다. 먼저 현재의 활용법이 구현에서 한계를 가질 수 있음을 보였다. 재가중(reweighting, 표본마다 손실에 곱하는 가중치를 달리 주는 방법)을 확장해 디리클레 분포(합이 1인 여러 확률 값의 묶음에 대한 확률 분포) 기반의 표본별 가중치 표집(DWS) 틀을 제안하고, 이 틀 안에서 재가중과 재표본추출을 비교했다. DWS 분석을 바탕으로 잡음 전이 행렬을 쓰는 재표본추출 방법 RENT를 내놓았다. 실험에서 RENT는 여러 벤치마크 데이터셋에서 재가중을 포함한 기존 전이 행렬 활용법보다 꾸준히 나았다.[^p3] | 1저자 H. S. Bae, 마지막 저자 문일철 |
| 4 | 2025 | [Distilling Dataset into Neural Field](https://pure.kaist.ac.kr/en/publications/distilling-dataset-into-neural-field/) · ICLR 2025 | 대규모 데이터셋은 고성능 딥러닝 모델을 학습시키는 데 꼭 필요하지만 계산과 저장 비용도 크게 든다. 이를 극복할 해법으로, 큰 데이터셋을 학습에 필요한 핵심 정보를 간직한 작은 합성 데이터셋으로 압축하는 데이터셋 증류(dataset distillation)가 떠올랐다. 이 논문은 신경장에 큰 데이터셋의 필요한 정보를 저장하는 새 매개변수화(합성 데이터를 어떤 변수들로 나타내 학습할지 정하는 방식) 틀 DDiF(Distilling Dataset into Neural Field)를 제안했다. 좌표를 입력받아 값을 내놓는 신경장의 고유한 성질 덕분에 DDiF는 정보를 효과적으로 보존하고 여러 모양의 데이터를 쉽게 만들어 낸다. 합성 표본 하나에 쓰는 예산이 같을 때 DDiF가 일부 이전 연구보다 표현력이 크다는 점을 이론으로 확인했다. 여러 실험에서 DDiF는 이미지 영역을 넘어 영상, 소리, 3차원 복셀(3차원 공간을 같은 크기의 정육면체 칸으로 나누고 칸마다 값을 둔 자료)까지 포함한 여러 벤치마크 데이터셋에서 우수한 성능을 보였다.[^p4] | 1저자 D. Shin, 마지막 저자 문일철 |
| 5 | 2026 | [AMiD: Knowledge Distillation for LLMs with α-mixture Assistant Distribution](https://arxiv.org/abs/2510.15982) · ICLR 2026 | 자기회귀(앞서 나온 토큰을 바탕으로 다음 토큰을 차례로 만들어 내는) 대규모 언어 모델(LLM)은 많은 과제에서 크게 발전했지만 계산과 메모리 비용이 크다. 지식 증류(KD)는 분포를 맞추는 방식으로 큰 교사 모델의 지식을 작은 학생 모델에 옮겨 이 문제를 덜어 준다. 이전 연구는 여러 차이 척도를 제안했지만, 교사와 학생의 용량 차이와, LLM의 고차원 출력에서 비롯된 0에 가까운 확률들이 일으키는 학습 불안정은 근본적인 한계로 남아 있다. 이를 넘으려고 보조 분포(교사와 학생의 분포 사이에 두는 중간 분포)를 암묵적이거나 명시적으로 쓰는 방법들이 최근 나왔지만, 보간 경로(두 분포 사이를 잇는 중간 분포들의 경로)와 발산(두 확률 분포가 서로 다른 정도를 재는 양)을 체계적으로 살피지 않은 단편적인 접근이었다. 이 논문은 새로운 일반화된 보조 분포 묶음인 α-혼합 보조 분포와, 보조 분포를 쓰는 지식 증류의 통합 틀인 α-혼합 증류(AMiD)를 제안했다. α-혼합 보조 분포는 이전의 모든 접근에서 고정돼 있던 분포 설계 변수 α를 새로 도입해 보조 분포를 연속적으로 확장한다. 또 AMiD는 보조 분포와 함께 쓰는 발산의 묶음을 최적성에 근거해 일반화했는데, 이 묶음도 이전 연구에서는 제한돼 있었다. 여러 실험에서 AMiD는 더 넓고 이론적 근거를 갖춘 보조 분포 공간을 활용해 우수한 성능과 학습 안정성을 보였다.[^p5] | 1저자 D. Shin, 마지막 저자 문일철 |
| 6 | 2026 | [Semantic-aware Wasserstein Policy Regularization for Large Language Model Alignment](https://arxiv.org/abs/2602.01685) · ICLR 2026 | 대규모 언어 모델은 흔히 인간 피드백 강화학습(RLHF, 사람이 매긴 선호로 만든 보상으로 모델을 강화학습시키는 방법)으로 사람의 선호에 맞춘다. 이 방법에서 언어 모델의 정책은 대개 기준 정책과의 KL 발산(쿨백–라이블러 발산, 두 확률 분포의 차이를 재는 양의 하나) 정칙화를 붙인 보상 최대화로 최적화된다. 그러나 KL 발산과 그 변형인 f-발산들은 같은 위치(인덱스)에 있는 토큰의 확률만 비교해 의미의 유사성을 잡아내지 못한다. 이 논문은 토큰 공간의 기하를 반영하는 엔트로피(확률 분포의 불확실한 정도를 나타내는 양) 정칙화 바서슈타인 거리에 바탕을 둔, 의미를 고려하는 RLHF용 정칙화인 바서슈타인 정책 정칙화(WPR)를 제안했다. 이 거리의 쌍대 정식화(최적화 문제를 짝이 되는 다른 변수에 대한 문제로 바꿔 쓴 형태)는 정칙화를 최적 쌍대 변수로 보상에 더하는 벌점 항으로 나타내므로, 표준 강화학습 알고리즘과 함께 쓸 수 있는 다루기 쉬운 목표가 된다. 실험에서 이 방법은 KL 발산·f-발산 기반의 기준 방법보다 나았고, 정렬에 의미를 고려한 정책 거리가 이롭다는 점을 보였다.[^p6] | 1저자 B. Na, 마지막 저자 문일철 |
| 7 | 2025 | [Trajectory-Class-Aware Multi-Agent Reinforcement Learning](https://pure.kaist.ac.kr/en/publications/trajectory-class-aware-multi-agent-reinforcement-learning/) · ICLR 2025 | 다중 에이전트 강화학습에서 일반화는, 과제마다 따로 특화된 정책에 기대지 않고 서로 다른 공동 정책이나 협력이 필요할 수 있는 여러 과제를 풀어야 하는 어려운 문제다. 연구팀은 이런 문제를 다중 과제라 부르고, 한 번의 학습 과정으로 에이전트가 이 다중 과제 환경에서 두루 대응하도록 학습시켰다. 이를 위해 TRAMA(TRajectory-class-Aware Multi-Agent reinforcement learning)를 내놓았다. TRAMA에서 에이전트는 부분 관측으로 자신이 겪고 있는 궤적의 클래스를 알아내 과제 유형을 인식하고, 이 궤적 인식이나 예측을 행동 정책의 추가 정보로 쓴다. 이를 위한 세 가지 주요 목표는 (a) 궤적들 사이의 핵심 유사성을 반영한 궤적 임베딩(자료를 벡터로 바꿔 나타낸 것)을 만드는 양자화된 잠재 공간(자료의 특징을 정해진 몇 개의 대표 벡터 가운데 하나로 나타내는 공간) 구성, (b) 이 궤적 임베딩을 이용한 궤적 군집화(비슷한 자료끼리 묶는 일), (c) 궤적 클래스를 인식하는 정책 구축이다. 특히 (c)를 위해 에이전트마다 궤적 클래스를 예측하는 궤적 클래스 예측기와, 궤적 클래스마다의 궤적 클래스 표현 모델을 설계했다. 각 에이전트는 이 궤적 클래스 표현과 자신의 부분 관측을 함께 바탕으로 과제를 인식하며 행동한다. StarCraft II 위에 만든 다중 과제 문제를 포함한 여러 과제에서 평가했고, 최고 수준의 기준 방법들보다 성능이 더 나아졌다.[^p7] | 1저자 H. Na, 마지막 저자 문일철 |
| 8 | 2024 | [DEVS-Based Simulation Acceleration for AI Training: Unmanned Surface Vehicle Case](https://doi.org/10.1109/wsc63780.2024.10838795) · Winter Simulation Conference (WSC 2024) | 무인 수상정(USV)의 쓰임이 늘면서 인공지능 학습용 시뮬레이터 개발이 중요해지고 있다. 이 논문은 DSDEVS(시뮬레이션 도중 모델의 결합 구조를 바꿀 수 있도록 확장한 DEVS 형식론)로 가능해진 모델 구조의 동적 변경을 써서, 분야별 특성을 고려한 DEVS 기반 시뮬레이션 가속 기법을 소개한다. 사례 연구에서는 무인 수상정의 기동·센서 모델 결합 구조를 시뮬레이션 실행 중에 바꾸는 방식으로 가속 기법을 평가했다. 이런 변화는 시뮬레이션 실행 중 불필요한 이벤트 교환을 줄여 실행 속도를 높인다. 또 USV 모델의 시간 진행을 동적으로 조절할 수 있게 해 시뮬레이션 속도를 높일 수 있다. 사례 연구는 이 방법이 시뮬레이션 실행을 효과적으로 빠르게 하지만 시뮬레이션 정확도와 맞바꾸는 관계가 있음을 보였다.[^p8] | 1저자 J. Choi, 마지막 저자 문일철 |

## 교수와 전문 분야

문일철 교수는 KAIST AI대학 AX학과의 중점교원이며,[^ax] KAIST 연구자 포털은 직위를 Professor, 소속을 Department of AX (AI Transformation)로 적는다.[^pure] 연구실 누리집은 연구실 주소를 산업및시스템공학과(Department of Industrial and Systems Engineering)로 적고 구성원 페이지에서 교수의 직함을 KAIST Chair Professor로 적으며,[^contact][^members] 안보과학기술대학원 교수 명단에도 소속학과 산업및시스템공학과로 올라 있다.[^gst] 2026년 7월 KAIST 뉴스는 교수를 AX학과 교수로 적는다.[^news-icml26] 연구실 공지는 산업및시스템공학과, AX학과, 데이터사이언스대학원, 김재철AI대학원, 항공우주공학과를 통해 연구실에 진학할 수 있다고 안내한다.[^apply] 2022년 9월 KAIST 뉴스는 교수를 데이터사이언스대학원의 책임교수로 적고, 이 대학원이 주관해 KAIST에 처음 개설한 「기초 기계학습」 마이크로 디그리(교과목 분야별로 정한 최소 학점을 짧은 기간에 집중 이수한 사람에게 정규 학위와 구분되는 별도의 학위를 주는 제도)를 소개한다.[^news-md]

연구자 포털에 따르면 교수는 2004년 서울대학교에서 학사(B.E.)를, 2008년 미국 카네기멜런 대학교(Carnegie Mellon University)에서 박사 학위를 받았다.[^pure] 박사 학위 논문은 카네기멜런 대학교 전산학부(School of Computer Science)의 「Destabilization of Adversarial Organizations with Strategic Interventions」(2008)다.[^thesis] 2008–2011년 KAIST 박사후연구원을 거쳐 2011–2017년 조교수, 2017–2025년 부교수로 일했고 2025년부터 교수(Full Professor)다.[^pure] 연구자 포털은 교수의 주요 연구 성과로 확산 모델의 판별기 안내(Diffusion with Discriminator Guidance), 변분 오토인코더(입력을 잠재 변수의 확률 분포로 바꾸었다가 다시 복원하도록 학습하는 생성 모델)의 적응형 사전 분포(사전 분포는 자료를 보기 전에 잠재 변수나 매개변수에 대해 가정해 두는 확률 분포, Adaptive Prior of Variational Autoencoder), 모델링과 시뮬레이션의 자동 보정(Automatic Calibration of Modeling and Simulation)을 든다.[^pure] 교수는 국방 지능형 군집체계 연구센터의 센터장이고,[^disc] KAIST 뉴스는 교수를 정보통신기획평가원 사람중심인공지능 핵심원천기술개발사업 과제의 연구책임자로 적는다.[^news-icml24][^news-icml26]

논문으로 보면 지금의 전문 분야는 네 갈래다. 첫째, 판별기 안내와 기각 표본추출처럼 확산 모델의 표본 생성을 개선하는 방법이다(대표 논문 1, 2).[^p1][^p2] 둘째, 잡음 레이블과 데이터셋 증류처럼 학습 자료의 결함과 비용을 다루는 기계학습 방법이다(대표 논문 3, 4).[^p3][^p4] 셋째, 대규모 언어 모델의 지식 증류와 사람 선호 정렬이다(대표 논문 5, 6).[^p5][^p6] 넷째, 다중 에이전트 강화학습과 인공지능 학습용 이산 사건 시뮬레이션이다(대표 논문 7, 8).[^p7][^p8] 2021–2026년 논문 목록에는 이 밖에 행위자 기반 모델로 주택 금융과 불평등, 금융과 시장 집중을 분석한 연구와 방문 보건의료 인력을 돕는 웹 기반 돌봄 연계 시스템 개발 연구도 있다.[^pubs]

## 응용 분야

AX학과 교수진 페이지는 교수의 주요 응용분야를 Mobility & Robotics, Manufacturing & Smart Factory, Finance & Social Systems로 적는다.[^ax] Research 페이지는 복잡한 군 조직을 모델링·시뮬레이션하는 일이 새 부대 구조를 설계하고 관리하는 데 흔히 쓰이고, 도시 인구를 모델링·시뮬레이션해 재난 관리 지침과 기술을 준비하며, 관리자와 정책 결정자가 데이터 마이닝과 사회 연결망 분석으로 사람들의 생각을 이해한다는 예를 든다.[^research] 2024년 KAIST 뉴스는 ICML 2024 경진대회의 기술이 최소한의 학습만으로 로봇이 멀티모달 정보와 기초 상식을 활용해 자율 제조와 서비스를 하도록 하는 것을 핵심으로 한다고 적고, 교수는 이 기술의 본질이 휴머노이드 제조 로봇에 쓰일 수 있는 상식을 가진 인공지능이라고 말했다.[^news-icml24] 2026년 KAIST 뉴스는 시각적 물리 문제 풀이 기술이 항공기와 로봇, 자율주행, 우주 시스템 등에서 실제 물리 환경을 고려한 설계와 의사결정에 쓰일 것으로 기대한다고 적는다.[^news-icml26] 국방 지능형 군집체계 연구센터는 드론·UAV, AI, 소프트웨어 플랫폼 등 여러 기술을 융합한 군집체계 연구를 한다고 소개하며,[^disc-home] 연구실은 2025년 OPEN KAIST에서 군집체계와 AI 드론 프로그램을 시연했다.[^news-open]

## 구성원

2026년 10월 25일 연구실 누리집 Members 페이지 기준이다. 페이지에 실린 구성원 가운데 교수와 직원(Staff)을 제외한 17명이며, 과정은 페이지 표기(Post-doctoral Researcher, PhD Student, MS Student, MS Students)를 옮겼고 Donghyeok SHIN과 Shin Jiwoo는 페이지에 과정 표기가 없다. 연구 주제는 페이지의 Research interest 칸이고, 이메일은 페이지에 적힌 학교 주소다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Byeonghu NA | 박사후연구원 | Deep Generative Model: Diffusion Model, Variational Autoencoder, Large Language Models; Insufficient/incomplete Dataset: Noisy Label Learning, Positive-Unlabeled Learning, Distribution Shift | byeonghu.na@kaist.ac.kr | 2, 3, 5, 6 |
| Donghyeok SHIN |  | Machine learning; Dataset Distillation, Coreset Selection; Knowledge Distillation | tlsehdgur0@kaist.ac.kr | 2, 4, 5 |
| Suhyeon JO | 박사과정 | Machine learning | suhyeonjo@kaist.ac.kr | 5, 6 |
| Yeongmin KIM | 박사과정 | Generative AI; Probabilistic Modeling | alsdudrla10@kaist.ac.kr | 1, 2, 5, 6 |
| Minsang PARK | 박사과정 | Deep Generative Model | pagemu@kaist.ac.kr | 2 |
| Sumin LEE | 박사과정 |  | sumlee@kaist.ac.kr | 7 |
| Gyuwon SIM | 박사과정 | Generative Model | gkwlaks4886@kaist.ac.kr | 4 |
| Mina KANG | 박사과정 |  | kasong13@kaist.ac.kr | 6 |
| Jiseok KWAK | 박사과정 | Machine Learning | jskwak@kaist.ac.kr |  |
| Seok Beom LEE | 석사과정 |  | sukbumyi@kaist.ac.kr |  |
| Young Min KIM | 석사과정 | Generative Models, Preference Alignment | swimskykim@kaist.ac.kr |  |
| Taekyu KIM | 석사과정 |  | taekyu@kaist.ac.kr |  |
| Kangje MOON | 석사과정 |  | 3x7equal21@kaist.ac.kr |  |
| Taewoo KIM | 석사과정 |  | dylan013@kaist.ac.kr |  |
| Minju CHO | 석사과정 |  | mummyee@kaist.ac.kr |  |
| Kyoungram PARK | 석사과정 |  | rampark@kaist.ac.kr |  |
| Shin Jiwoo |  |  | natu33@kaist.ac.kr |  |

## 졸업생과 이전 구성원

연구실 누리집 Alumni 페이지의 PhD Alumni 18명, Master Alumni 24명과 Fomer Staff 칸에 Post-doctoral researcher로 적힌 1명이다. 학위·과정 칸은 페이지의 분류(PhD Alumni, Master Alumni, Fomer Staff)와 그 뒤에 적힌 학위 표기이고, 괄호 안은 페이지의 재적 기간 표기(Lab Tenure 등)다. 진로는 페이지가 적은 곳이고, 학위 논문은 누리집 Thesis 목록에서 이름이 같은 졸업생의 논문을 옮겼다.[^alumni][^thesis]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Doyun Kwon | Master Alumni (Lab Tenure: 2024-2026) |  |  |
| Zeynep ALTINER | Master Alumni (Lab Tenure: 2024-2026) | Samsung Electronics DS |  |
| Yeeun Park | Master Alumni (Lab Tenure: 2024-2026) |  |  |
| Changseok HAN | PhD Alumni (Lab Tenure: 2022-2026) |  |  |
| Juho CHOI | Master Alumni (2023-2025) |  |  |
| Kwanghyeon LEE | Master Alumni, MS (Lab Tenure: 2023-2025) |  |  |
| Hyungho NA | PhD Alumni (Lab Tenure: 2021-2025) | Ulsan National Institute of Science and Technology (UNIST), Assistant professor |  |
| Muhyun BYUN | PhD Alumni, PhD (Lab Tenure: 2021-2024) |  |  |
| Yunkyeong SEO | PhD Alumni, PhD (Lab Tenure: 2020-2024) | Samsung Global Research |  |
| Seungjae SHIN | PhD Alumni, MS, PhD (Lab Tenure: 2018-2024) | Qualcomm | Master's Thesis (2020): Neutralizing Gender Bias in Word Embedding with Latent Disentanglement and Counterfactual Generation |
| Youngjae CHO | Master Alumni (2022-2023) | AI Startup | Master's Thesis (2024): Enhancing Flexibility and Adaptability of Bayesian Prompt Learning in Vision-Language Pretrained Model |
| Yeodong YOUN | Master Alumni (2021-2023) |  | Master's Thesis (2023): Probabilistic Representation Learning for Improved Cross-modal Retrieval Using Density-wise Similarity |
| JoonHo JANG | PhD Alumni, MS, PhD (Lab Tenure: 2017-2023) | SAIT | PhD Dissertation (2024): Robust Feature Alignment for Mitigating Negative Transfer in Domain Adaptation; Master's Thesis (2019): Mask Modeling for Attention Mechanism in Sentiment Analysis |
| Dongjun KIM | PhD Alumni, Integrated MS-PhD (Lab Tenure: 2017-2023) | SONY | PhD Dissertation (2023): A Study on the Score-based Diffusion Model for Improved Training, Flexible Inference, and Efficient Sampling |
| Sungeun KIM | Master Alumni (2021-2022) | NIMS | Master's Thesis (2023): Receptive Field Depth Selection in Graph Neural Network for Node Classification Task |
| Taesub YUN | PhD Alumni, PhD (Lab Tenure: 2017-2022) | Korea University (Sejong Campus), Tenure Track Professor | PhD Dissertation (2022): A Study on the Impact of Financial Quantitative Easing on Economic Inequality: Using Agent-Based Simulations |
| Mingi JI | PhD Alumni, MS, PhD (Lab Tenure: 2016-2022) | Google Korea | PhD Dissertation (2022): Feature Based Knowledge Distillation for Image Recognition; Master's Thesis (2018): Earthwork Planning in Various Environment via Reinforcement Learning |
| Yoon-Yeong KIM | PhD Alumni, MS-PhD (Lab Tenure: 2016-2022) | Univ. of Seoul, Stat. Dept. Tenure Track Professor | PhD Dissertation (2023): Research on Improving Generalization of Deep Active Learning by Perturbing Input Space; Master's Thesis (2018): Black-Box Expectation-Maximization Algorithm for Estimating Latent States of High-Speed Vehicles |
| Hyun SAGONG | Master Alumni (2020-2021) | SK Hynix |  |
| Jeahoon LEE | Master Alumni (2020-2021) | SK Hynix | Master's Thesis (2022): Similarity Search on Wafer Bin Map through Nonparametric and Hierarchical Clustering |
| Yongjin SHIN | Master Alumni (2019~2021) | AI Startup | Master's Thesis (2021): Localized Binary Cross-Entropy for Federated Learning |
| Kyu Seok KIM | Master Alumni (2019-2020) | AI Startup | Master's Thesis (2021): Deep Hierarchical Clustering with Dirichlet Forest Prior |
| Hyemi KIM | Master Alumni (2018-2020) | Naver | Master's Thesis (2020): Counterfactual Inference and Counterfactual Data Generation through Latent Disentanglement |
| Minjae JUNG | Master Alumni (2018-2020) | TmaxData AI | Master's Thesis (2020): Air Combat Basic System Model for Learning Engagement |
| Weonyoung JOO | PhD Alumni, PhD (Lab Tenure: 2016-2020) | EWHA Womans University, Stats Dept., Tenure Track Professor | PhD Dissertation (2020): Pathwise Gradient Estimators for Various Probability Distributions in Deep Generative Models |
| Kyungwoo SONG | PhD Alumni, MS-PhD (Lab Tenure: 2015-2020) | Yonsei Univ. Applied Stat. Dept. Tenure Track Professor | PhD Dissertation (2021): Context-Aware Model with Generalized Structured Gate and Attention; Master's Thesis (2017): Deep Ideal Point Estimation with Network |
| Dohyung KIM | PhD Alumni, PhD (Lab Tenure: 2015-2019) | ADD |  |
| Kiung KIM | Master Alumni (2016) | AI Startup |  |
| JunKeon PARK | Master Alumni (2016-2018) | TmaxData AI | Master's Thesis (2018): Dynamic Topic Modeling with Neural Variational Inference |
| Su-Jin SHIN | PhD Alumni, MS, PhD (Lab Tenure: 2013-2018) | ADD | PhD Dissertation (2019): Hierarchical Mixture Modelings for Different Types of Data: A Nonparametric Bayesian Approach; Master's Thesis (2015): Incorporating Domain Knowledge into Hierarchical Topic Models with Dirichlet Forest Priors |
| Sungrae PARK | PhD Alumni, MS, PhD (Lab Tenure: 2012-2018) | Naver Clova | PhD Dissertation (2018): Adversarial Dropout for Deep Neural Networks; Master's Thesis (2014): Associated Topic Model with Social Measurement |
| Wonsung LEE | PhD Alumni, Integrated MS-PhD (Lab Tenure: 2012-2018) | SKT AI | PhD Dissertation (2018): Deep Generative Models for Collaborative Filtering with Multi-Source and High Dimensional Data |
| Do-Hyeong KIM | Master Alumni (2016-2017) | SKT AI | Master's Thesis (2018): Imitation Learning for Different Player Style using Generative Adversarial Networks |
| Doosup CHOI | Master Alumni (2014-2016) | LG Electronics | Master's Thesis (2016): Keyword Influence Kalman Filter for Keyword Frequency Estimation |
| Doyun KIM | Master Alumni (2014-2016) | NCSoft AI | Master's Thesis (2016): Inverse Modeling of Combat Behavior with Virtual-Constructive Simulation Training |
| Chi-jung JUNG | Master Alumni (2014-2016) |  | Master's Thesis (2016): Intelligent Behavior Modeling on Information Delivery of Time-Sensitive Targets |
| Junseok LEE | Master Alumni (2013-2015) | Samsung Electronics | Master's Thesis (2015): Decentralized Task Assignment Methodology with Spatial Constraint |
| Ah-Ram KANG | Master Alumni (2013-2015) |  | Master's Thesis (2015): Comparative studies of command and control structure between ROK and US field artillery organization |
| Jang Won BAE | PhD Alumni, PhD (Lab Tenure: 2011-2015) | KoreaTech, School of Industrial Management, Tenure Track Professor | PhD Dissertation (2015): Agent-Based Efficient Modeling and Simulation with Formalism |
| Sehoon LEE | Master Alumni (2012-2014) | ADD |  |
| HeeSun BAE | PhD Alumni | KAIST E2-2, 4109 | Master's Thesis (2022): Latent label generation can help improve classification performance degradation when learning with noisy labels |
| GeunHo LEE | Master Alumni (2011-2013) | ADD | Master's Thesis (2013): Design and Evaluation of Disaster Response Organizational Structure for Resource Demand and Supply |
| Junghyun AHN | Fomer Staff, Post-doctoral researcher |  |  |

## 최근 논문 목록 (2021–2026)

연구실 누리집 Publications의 International Journal 목록 2021–2026년 12편과 International Conference 목록 2021–2026년 46편(워크숍 논문 3편 포함), 모두 58편이다(2021년 8편, 2022년 10편, 2023년 10편, 2024년 12편, 2025년 9편, 2026년 9편). 제목·저자·학술지와 학회 이름·날짜·장소는 누리집 표기이고, 연도는 목록의 연도 칸이다. 같은 해 안에서는 학술지 논문을 먼저, 학회 논문을 그다음에 누리집 번호의 역순으로 두었다. 누리집이 「Accepted」로 적은 학술지 논문 1편은 「게재 승인」으로 표시했다. 목록 줄에 학회 이름이 없는 2026년 3편은 각 논문 상세 쪽의 서지를 붙였고, 이 가운데 NeurIPS 2026 논문 2편은 학회가 열람일 뒤인 2026년 12월에 열려 누리집 기재 학회 이름과 날짜를 그대로 적었다. 연도 칸이 2005로 적힌 NeurIPS 2025 논문 1편은 학회 이름에 따라 2025년에 두었다.[^pubs]

**2026**

- Han, C. S., Na, H., Choi, J., Park, Y., Hwang, J., Moon, I. C., & Yun, T. S. "AI-Integrated Architecture for Theater Missile Defense Simulation". *International Journal of Control, Automation, and Systems, 게재 승인(Accepted) (2026, May)*.
- Hyungho Na, Jaemyung Ahn, and Il-Chul Moon. "Multi-agent Reinforcement Learning Considering Agent Priority for Weapon-Target Assignment". *Journal of Aerospace Information Systems, 23, 6, 464–479 (2026, June)*.
- Richard Lee Kim, Yeongmin Kim, Gyuwon Sim, Taekyu Kim, Minsang Park, and Il-Chul Moon. "Best-of-N Guidance for Test-time Diffusion Alignment". *The Fortieth Annual Conference on Neural Information Processing Systems (NeurIPS 2026), Sydney, Australia, Dec 6-12, 2026*.
- Byeonghu Na, Donghyeok Shin, Yeongmin Kim, Mina Kang, and Il-Chul Moon. "WASD: Wasserstein-based Knowledge Distillation for Large Language Models". *The Fortieth Annual Conference on Neural Information Processing Systems (NeurIPS 2026), Sydney, Australia, Dec 6-12, 2026*.
- Yeongmin Kim, Donghyeok Shin, Byeonghu Na, Minsang Park, Richard Lee Kim, and Il-Chul Moon. "Lookahead Sample Reward Guidance for Test-Time Scaling of Diffusion Models". *International Conference on Machine Learning (ICML 2026), Seoul, South Korea, Jul 6-11, 2026*.
- Yeongmin Kim, Donghyeok Shin, Mina Kang, Byeonghu Na, and Il-Chul Moon. "Distillation of Large Language Models via Concrete Score Matching". *International Conference on Learning Representations (ICLR 2026), April 23-27, Rio de Janeiro, Brazil (2026)*.
- Minsang Park, Gyuwon Sim, Hyungho Na, Jiseok Kwak, Sumin Lee, Richard Lee Kim, Donghyeok Shin, Byeonghu Na, Yeongmin Kim, Il-chul Moon. "AC-Sampler: Accelerate and Correct Diffusion Sampling with Metropolis-Hastings Algorithm". *International Conference on Learning Representations (ICLR 2026), April 23-27, Rio de Janeiro, Brazil (2026)*.
- Byeonghu Na, Hyungho Na, Yeongmin Kim, Suhyeon Jo, HeeSun Bae, Mina Kang, and Il-Chul Moon. "Semantic-aware Wasserstein Policy Regularization for Large Language Model Alignment". *International Conference on Learning Representations (ICLR 2026), April 23-27, Rio de Janeiro, Brazil (2026)*.
- Donghyeok Shin, Yeongmin Kim, Suhyeon Jo, Byeonghu Na, and Il-Chul Moon. "AMiD: Knowledge Distillation for LLMs with α-mixture Assistant Distribution". *International Conference on Learning Representations (ICLR 2026), April 23-27, Rio de Janeiro, Brazil (2026)*.

**2025**

- Seo, Yunkyeong, Altiner, Zeynep, Lee, Sumin, Moon, Il-Chul and Yun, Tae-Sub. "Finance and Market Concentration Using Agent-Based Modeling: Evidence from South Korea". *Journal of Artificial Societies and Social Simulation, 28, 3, 5 (2025, Jun)*.
- Jiwoo Shin, Byeonghu Na, Mina Kang, Wonhyeok Choi, and Il-chul Moon. "Prompt-Based Safety Guidance Is Ineffective for Unlearned Text-to-Image Diffusion Models". *NeurIPS 2025 Workshop on Generative and Protective AI for Content Creation, Dec 6, San Diego, USA (2025)*.
- Byeonghu Na, Mina Kang, Jiseok Kwak, Minsang Park, Jiwoo Shin, SeJoon Jun, Gayoung Lee, Jin-Hwa Kim, and Il-Chul Moon. "Training-Free Safe Text Embedding Guidance for Text-to-Image Diffusion Models". *Neural Information Processing Systems (NeurIPS 2025), Dec 2, San Diego, USA (2025)*.
- Byeonghu Na, Minsang Park, Gyuwon Sim, Donghyeok Shin, HeeSun Bae, Mina Kang, Se Jung Kwon, Wanmo Kang, and Il-Chul Moon. "Diffusion Adaptive Text Embedding for Text-to-Image Diffusion Models". *Neural Information Processing Systems (NeurIPS 2025), Dec 2, San Diego, USA (2025)*.
- Yeongmin Kim, Heesun Bae, Byeonghu Na, and Il-Chul Moon. "Preference Optimization by Estimating the Ratio of the Data Distribution". *Neural Information Processing Systems (NeurIPS 2025), Nov 30, San Diego, USA (2025)*.
- Yeeun Park, Hyungho Na, and Il-Chul Moon. "Simulation Analysis of Sensor Placement and Target Interaction in DEVS Formalism". *Annual Modeling and Simulation Conference 2025, May 26-29, Madrid, Spain (2025)*.
- Yeongmin Kim, Kwanghyeon Lee, Minsang Park, Byeonghu Na, and Il-Chul Moon. "Diffusion Bridge AutoEncoders for Unsupervised Representation Learning". *International Conference on Learning Representations (ICLR 2025), Apr 24-28, Singapore, Singapore (2025)*.
- Hyungho Na, Kwanghyeon Lee, Sumin Lee, and Il-Chul Moon. "Trajectory-Class-Aware Multi-Agent Reinforcement Learning". *International Conference on Learning Representations (ICLR 2025), Apr 24-28, Singapore, Singapore (2025)*.
- Donghyeok Shin, HeeSun Bae, Gyuwon Sim, Wanmo Kang, and Il-Chul Moon. "Distilling Dataset into Neural Field". *International Conference on Learning Representations (ICLR 2025), Apr 24-28, Singapore, Singapore (2025)*.

**2024**

- Tae-Sub Yun, Hee-Sun Bae, IL-Chul Moon, Deokjong Jeong. "The relationship between housing finance and inequality". *Journal of Economic Interaction and Coordination (2024, Mar)*.
- Kwanghyeon Lee, Mina Kang, Hyungho Na, Heesun Bae, Byeonghu Na, Doyun Kwon, Seungjae Shin, Yeongmin Kim, Taewoo Kim, Seungmin Yun, Il-Chul Moon. "DPO-Finetuned Large Multi-Modal Planner with Retrieval-Augmented Generation". *Multi-modal Foundation Model meets Embodied AI Workshop, ICML2024, Jul 26, Vienna, Austria (2024)*.
- Juho Choi, Jang Won Bae, and Il-Chul Moon. "DEVS-Based Simulation Acceleration for AI Training: Unmanned Surface Vehicle Case". *Winter Simulation Conference (WSC2024), Dec 15-18, Orlando, USA (2024)*.
- Byeonghu Na, Suhyeon Jo, Yeongmin Kim, and Il-Chul Moon. "Reward-based Input Construction for Cross-document Relation Extraction". *Annual Meeting of the Association for Computational Linguistics (ACL 2024), Aug 11-16, Bangkok, Thailand (2024)*.
- Byeonghu Na, Yeongmin Kim, Minsang Park, Donghyeok Shin, Wanmo Kang, and Il-Chul Moon. "Diffusion Rejection Sampling". *International Conference on Machine Learning (ICML 2024), Jul 21-27, Vienna, Austria (2024)*.
- Hyungho Na and Il-Chul Moon. "LAGMA: LAtent Goal-guided Multi-agent Reinforcement Learning". *International Conference on Machine Learning (ICML 2024), Jul 21-27, Vienna, Austria (2024)*.
- Hyungho Na, Yunkyeong Seo, and Il-Chul Moon. "Efficient Episodic Memory Utilization of Cooperative Multi-Agent Reinforcement Learning". *International Conference on Learning Representations (ICLR 2024), May 7-11, Vienna, Austria (2024)*.
- Yeongmin Kim, Byeonghu Na, JoonHo Jang, Minsang Park, Dongjun Kim, Wanmo Kang, and Il-Chul Moon. "Training Unbiased Diffusion Models From Biased Dataset". *International Conference on Learning Representations (ICLR 2024), May 7-11, Vienna, Austria (2024)*.
- HeeSun Bae, Seungjae Shin, Byeonghu Na, and Il-Chul Moon. "Dirichlet-based Per-Sample Weighting by Transition Matrix for Noisy Label Learning". *International Conference on Learning Representations (ICLR 2024), May 7-11, Vienna, Austria (2024)*.
- Byeonghu Na, Yeongmin Kim, HeeSun Bae, Jung Hyun Lee, Se Jung Kwon, Wanmo Kang, and Il-Chul Moon. "Label-Noise Robust Diffusion Models". *International Conference on Learning Representations (ICLR 2024), May 7-11, Vienna, Austria (2024)*.
- Seungjae Shin, Heesun Bae, Byeonghu Na, Yoon-Yeong Kim, and Il-Chul Moon. "Unknown Domain Inconsistency Minimization for Domain Generalization". *International Conference on Learning Representations (ICLR 2024), May 7-11, Vienna, Austria (2024)*.
- Youngjae Cho, HeeSun Bae, Seungjae Shin, YeoDong Youn, Weonyoung Joo, and Il-Chul Moon. "Make Prompts Adaptable : Bayesian Modeling for Vision-Language Prompt Learning with Data-Dependent Prior". *AAAI Conference on Artificial Intelligence (AAAI 2024), Feb 22-25, Vancouver, Canada (2024)*.

**2023**

- Lee, J., Park, S., Cho, M., Kang, J., Kim, M., Choi, S., Kim, S., Choi, J., Han, K. S., Kim, C., Moon, I. C., Choi, M. K., & Jang, S. "Development of a web-based care networking system to support visiting healthcare professionals in the community". *BMC Health Services Research, 23, 1 (2023, Dec)*.
- Kim, D., Song, K., Kim, Y., Shin, Y., Kang, W., Moon, I. C., & Joo, W. "Sequential Likelihood-Free Inference with Neural Proposal". *Pattern Recognition Letters, 169, 102-109 (2023, May)*.
- Na, H., Ahn, J., & Moon, I. C. "Weapon–Target Assignment by Reinforcement Learning with Pointer Network". *Journal of Aerospacce Information Systems, 20, 1, 53-59 (2023, Jan)*.
- DongHyeok Shin, Seungjae Shin, and Il-Chul Moon. "Frequency Domain-based Dataset Distillation". *Neural Information Processing Systems (NeurIPS 2023), Dec 10-16, New Orleans, USA (2023)*.
- Suhyeon Jo, Donghyeok Shin, Byeonghu Na, JoonHo Jang, and Il-Chul Moon. "Hierarchical Multi-Label Classification with Partial Labels and Unknown Hierarchy". *ACM International Conference on Information and Knowledge Management (CIKM 2023), Oct 21-25, Birmingham, United Kingdom (2023)*.
- Yoon-Yeong Kim, Youngjae Cho, JoonHo Jang, Byeonghu Na, Yeongmin Kim, Kyungwoo Song, Wanmo Kang, and Il-Chul Moon. "SAAL: Sharpness-Aware Active Learning". *International Conference on Machine Learning (ICML 2023), Jul 25-27, Hawaii, USA (2023)*.
- Dongjun Kim, Yeongmin Kim, Se Jung Kwon, Wanmo Kang, and Il-Chul Moon. "Refining Generative Process with Discriminator Guidance in Score-based Diffusion Models". *International Conference on Machine Learning (ICML 2023), Jul 25-27, Hawaii, USA (2023)*.
- Seungjae Shin, Heesun Bae, DongHyeok Shin, Weonyoung Joo, and Il-Chul Moon. "Loss Curvature Matching for Dataset Selection and Condensation". *International Conference on Artificial Intelligence and Statistics (AISTATS 2023), Apr 25-27, Valencia, Spain (2023)*.
- Muhyun Byun, Hyungho Na, and Il-Chul Moon. "Time-Efficient Weapon-Target Assignment by Actor-Critic Reinforcement". *IEEE Conference on System, Man, and Cybernetics (SMC 2023), Oct 1-4, Mau, Hawaii, USA (2023)*.
- Tae Sub Yun, Minsang Park, and Il-Chul Moon. "Modeling and Calibrating Digital Twin of Automatic Garbage Collection System in Sejong City". *Annual Modeling and Simulation Conference (ANNSIM 2023), May 23-26, Ontario, Canada (2023)*.

**2022**

- Yun, T., Kim, D., Moon, I. C., & Bae, J. W. "Agent-Based Model for Urban Administration: A Case Study of Bridge Construction and its Traffic Dispersion Effect". *Journal of Artificial Societies and Social Simulation, 25, 5 (2022, Oct)*.
- Yun, W.-S., Ko, S., Byun, M., Kim, H., Moon, I. C., & Lee, T. E. "Toward Robust Battle Experimental Design for Command and Control of Mechanized Infantry Brigade". *Military Operations Research, 27, 1, 45-72 (2022, Feb)*.
- Yeongmin Kim, Dongjun Kim, HyeonMin Lee, and Il-Chul Moon. "Unsupervised Controllable Generation with Score-based Diffusion Models: Disentangled Latent Code Guidance". *Neural Information Processing Systems (NeurIPS 2022), Nov 28-Dec 9, New Orleans, USA (2022)*.
- Seungjae Shin, Byeonghu Na, HeeSun Bae, JoonHo Jang, Hyemi Kim, Kyungwoo Song, Youngjae Cho, and Il-Chul Moon. "Improving Group-based Robustness and Calibration via Ordered Risk and Confidence Regularization". *Workshop on Spurious Correlations, Invariance and Stability, International Conference on Machine Learning (ICML Workshop 2022), Jul 22, Baltimore, USA (2022)*.
- Tae-Sub Yun, Hanbit Lee, and Il-Chul Moon. "Finance and Decreasing Business Dynamics: Using Macroeconomic Agent-Based Simulation". *Social Simulation Conference (SSC 2022), Sep 14, Milan, Italy (2022)*.
- Dongjun Kim, Tae-Sub Yun, Il-Chul Moon, and Jang Won Bae. "Automatic Calibration Framework of Agent-Based Models for Dynamic and Heterogeneous Parameters". *International Conference on Autonomous Agent and Multi-Agent Systems (AAMAS 2022), May 9, Virtual Conference (2022)*.
- Dongjun Kim, Byeonghu Na, Se Jung Kwon, Dongsoo Lee, Wanmo Kang, and Il-Chul Moon. "Maximum Likelihood Training of Implicit Nonlinear Diffusion Model". *Neural Information Processing Systems (NeurIPS 2022), Nov 28-Dec 9, New Orleans, USA (2022)*.
- JoonHo Jang, Byeonghu Na, Dong Hyeok Shin, Mingi Ji, Kyungwoo Song, and Il-Chul Moon. "Unknown-Aware Domain Adversarial Learning for Open-Set Domain Adaptation". *Neural Information Processing Systems (NeurIPS 2022), Nov 28-Dec 9, New Orleans, USA (2022)*.
- HeeSun Bae, Seungjae Shin, Byeonghu Na, JoonHo Jang, and Il-Chul Moon. "From Noisy Prediction to True Label: Noisy Prediction Calibration via Generative Model". *International Conference on Machine Learning (ICML 2022), Jul 17, Baltimore, USA (2022)*.
- Dongjun Kim, Seungjae Shin, Kyungwoo Song, Wanmo Kang, and Il-Chul Moon. "Soft Truncation: A Universal Training Technique of Score-based Diffusion Model for High Precision Score Estimation". *International Conference on Machine Learning (ICML 2022), Jul 17, Baltimore, USA (2022)*.

**2021**

- Lee, J. H., Moon, I. C., & Oh, R. "Similarity Search on Wafer Bin Map Through Nonparametric and Hierarchical Clustering". *IEEE Transactions on Semiconductor Manufacturing, 34, 4, 464-474 (2021, Nov)*.
- Kim, Y., Kim, H., Lee, W., Choi, H., & Moon, I. C. "Black-Box Expectation–Maximization Algorithm for Estimating Latent States of High-Speed Vehicles". *Journal of Aerospace Information Systems, 18, 4, 175-192 (2021, Apr)*.
- Kim, D., Yun, T., Moon, I., & Bae, J. W. "Automatic calibration of dynamic and heterogeneous parameters in agent-based models". *Autonomous Agents and Multi-Agent Systems, 35, 2, 1-66 (2021, Aug)*.
- Yoon-Yeong Kim, Kyungwoo Song, JoonHo Jang, and Il-Chul Moon. "LADA: Look-Ahead Data Acquisition via Augmentation for Deep Active Learning". *Neural Information Processing Systems (NeurIPS 2021), Dec 7-10, Virtual Conference (2021)*.
- Mingi Ji, Seungjae Shin, Seunghyun Hwang, Gibeom Park, and Il-Chul Moon. "Refine Myself by Teaching Myself : Feature Refinement via Self-Knowledge Distillation". *Conference on Computer Vision and Pattern Recognition (CVPR 2021), Jun 19-25, Virtual Conference (2021)*.
- Hyemi Kim, Seungjae Shin, JoonHo Jang, Kyungwoo Song, Weonyoung Joo, Wanmo Kang, and Il-Chul Moon. "Counterfactual Fairness with Disentangled Causal Effect Variational Autoencoder". *AAAI Conference on Artificial Intelligence (AAAI 2021), Feb 2-9, Virtual Conference (2021)*.
- Kyungwoo Song, Yohan Jung, Dongjun Kim, and Il-Chul Moon. "Implicit Kernel Attention". *AAAI Conference on Artificial Intelligence (AAAI 2021), Feb 2-9, Virtual Conference (2021)*.
- Mu Hyun Byun, and Il-Chul Moon. "Categorization of AI-Enabled Command and Control in Ballistic Missile Defense". *International Command and Control Research and Technology Symposium (ICCRTS 2021), Oct 18, Virtual Conference (2021)*.

## 과제

KAIST 뉴스와 국방 지능형 군집체계 연구센터 누리집이 문일철 교수를 연구책임자나 센터장으로 적은 과제와 연구센터다.

- 정보통신기획평가원(IITP) 사람중심인공지능 핵심원천기술개발사업 「이종 데이터 기반 상식 추출·이해·추론을 위한 인공지능 기술개발」[^news-icml24][^news-icml26] (역할 문일철 교수 연구책임자)
- 국방 지능형 군집체계 연구센터(DISC, Defense Intelligent Swarm Research Center): 정보통신기획평가원(IITP) 지원으로 KAIST가 운영하는 연구센터로, 2026년 KAIST 뉴스는 「ITRC 국방군집체계연구센터」로 적는다. 센터 누리집은 문일철 교수를 센터장으로, 3세부 「분산형 군집 Embodied AI 연구」의 연구자로 적는다[^disc][^news-lig][^news-icml26] (역할 문일철 교수 센터장)

## 수상

2021년 10월 13일부터 2026년 10월 13일까지 연구실 누리집 Awards 게시판에 실린 연구실과 구성원의 수상 글이다. 날짜는 게시일이고, 상 이름은 글의 표기다. 두 차례의 ICML 챌린지 우승은 같은 내용을 다룬 KAIST 뉴스도 근거로 달았다.

- 2026-07-23 · ICML 2026 공식 워크숍 AI4Math Workshop의 「시각적으로 정의된 물리 문제 풀기(Visual Grounded Physics Problem Solving)」 국제 챌린지 우승(ICML 공식 시상식 1등상), 응용인공지능연구실 연구진 5명 참가[^aw-icml26][^news-icml26]
- 2026-01-07 · 신동혁(산업및시스템공학과 박사과정), Qualcomm Innovation Fellowship Korea 선정[^aw-qif26]
- 2025-12-17 · 연구실에서 제작한 AI Drone 및 공중전 시뮬레이터, KAIST Institute Prototype 우수상[^aw-proto]
- 2025-12-17 · 나병후 박사, KAIST Institute for Robotics 우수연구자상[^aw-nbh-ki]
- 2025-09-04 · ITRC Challenge 2025 창의도전상(AWS): Zeynep·이석범·김영민 학생, 발표 제목 'AI-to-Drone'(AI 기반 군집드론제어)[^aw-itrc]
- 2025-02-18 · 나병후 박사, 공과대학 박사학위 최우수논문상[^aw-nbh-best]
- 2025-02-17 · 나형호 박사, Global Leadership Award(총장 수여)[^aw-nhh]
- 2024-12-30 · 나병후(산업및시스템공학과 박사과정), Qualcomm Innovation Fellowship Korea 선정[^aw-qif24b]
- 2024-12-18 · 박예은, 육군 M&S 국제학술대회 논문 장려상[^aw-army]
- 2024-08-05 · 나형호 학생, 특화연구센터 우수 연구인력 표창(2023년 TDRC 단계평가)[^aw-tdrc]
- 2024-07-31 · ICML 2024 멀티모달 작업계획 생성 경진대회(EgoPlan) 우승: 우승상(Outstanding Champion Award)과 혁신상(Innovation Award), 이광현·강미나(산업및시스템공학과 석사과정) 등 11명 팀[^aw-icml24][^news-icml24]
- 2024-03-06 · 김동준 박사, 우수학위논문상(총장 명의)[^aw-kdj]
- 2024-01-19 · 신승재·배희선(산업및시스템공학과 박사과정), Qualcomm Innovation Fellowship Korea 2024 재선정[^aw-qif24a]
- 2023-03-04 · 지민기 박사, 우수학위논문상(총장 명의)[^aw-jmg]
- 2023-03-02 · 신승재·배희선(산업및시스템공학과 박사과정), Qualcomm Innovation Fellowship Korea 선정[^aw-qif23]

## 소식

같은 기간 KAIST 뉴스에 실린 연구실 관련 글 가운데 수상과 과제를 알린 글 밖의 글이다. 날짜는 게시일이다.

- 2025-11-25 · KAIST 소식 「전 국민 과학문화 시대 연다.. KSOP· OPEN KAIST·AI 사관학교로」의 사진 설명: 2025 OPEN KAIST에서 산업및시스템공학과 문일철 교수 연구실이 진행한 군집체계와 AI 드론 프로그램 시연[^news-open]

## 연락과 위치

- 연구실: 4116, E2-2, Department of Industrial and Systems Engineering, KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea(누리집 Contact 표기)[^contact]
- 연구실 전화와 이메일: +82-42-350-3158 / +82-42-350-3118, icmoon@kaist.ac.kr[^contact]
- 교수 연구실: 산업경영학동(E2-2) 4110호, 전화 042-350-3118, 이메일 icmoon@kaist.ac.kr(AX학과 교수진 페이지 표기)[^ax]
[^home]: 응용인공지능 연구실 누리집 첫 화면 <https://aai.kaist.ac.kr/> (연구실 소개, Research area의 논문 13편과 키워드, 2026-10-25 열람)
[^research]: 응용인공지능 연구실 누리집 Research <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub3_1> (2026-10-25 열람)
[^members]: 응용인공지능 연구실 누리집 Members <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub2_1> (이름, 과정, Research interest, 이메일, 2026-10-25 열람)
[^alumni]: 응용인공지능 연구실 누리집 Alumni <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub2_2> (분류, 진로, 재적 기간, 2026-10-25 열람)
[^contact]: 응용인공지능 연구실 누리집 Contact <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub1_1> (주소, 전화, 이메일, 2026-10-25 열람)
[^pubs]: 응용인공지능 연구실 누리집 Publications의 International Journal 목록 <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub5_4> (1–3쪽)과 International Conference 목록 <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub5_5> (1–7쪽), 두 목록의 Agent Modeling 분류 화면, 2026년 논문 3편의 상세 쪽 (2026-10-25 열람)
[^thesis]: 응용인공지능 연구실 누리집 Thesis 목록 <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub5_2> (1–3쪽, 2026-10-25 열람)
[^apply]: 응용인공지능 연구실 누리집 Awards 게시판 공지 「Application to AAILab, KAIST」 <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub7_1&wr_id=56> (2026-10-25 열람)
[^ax]: KAIST AI대학 AX학과 교수진 <https://aicollege.kaist.ac.kr/ax/faculty> (문일철 항목의 직위, 전화, 이메일, 위치, 연구분야, 주요 응용분야, 핵심 AI 역량, 2026-10-25 열람)
[^pure]: KAIST 연구자 포털(PURE) 문일철 <https://pure.kaist.ac.kr/en/persons/il-chul-moon/> (직위, 소속, 학력, 경력, 연구 관심, 주요 연구 성과, 2026-10-25 열람)
[^gst]: KAIST 안보과학기술대학원 교수 명단 2쪽 <https://gst.kaist.ac.kr/member/faculty/?page=2> (문일철 항목의 소속학과, 연구분야, 세부 연구 분야, 연구실, 2026-10-25 열람)
[^disc]: 국방 지능형 군집체계 연구센터 Researchers <http://disc.kaist.ac.kr/bbs/board.php?bo_table=sub1_2> (문일철(센터장) 항목, 2026-10-25 열람)
[^disc-home]: 국방 지능형 군집체계 연구센터 누리집 첫 화면 <http://disc.kaist.ac.kr/> (About DISC, 2026-10-25 열람)
[^news-icml24]: KAIST 뉴스 「문일철 교수팀, 북경대와 영국 ICL 제치고 ICML 2024 챌린지 우승」(2024-07-30 게시) <https://news.kaist.ac.kr/news/html/news/?mode=V&mng_no=38670> (2026-10-25 열람)
[^news-icml26]: KAIST 뉴스 「'물리 세계 이해하는 AI' 세계 최고…ICML 2026 국제 AI 챌린지 우승」(2026-07-23 게시) <https://news.kaist.ac.kr/news/html/news/?mode=V&mng_no=64810> (2026-10-25 열람)
[^news-open]: KAIST 뉴스 「전 국민 과학문화 시대 연다.. KSOP· OPEN KAIST·AI 사관학교로」(2025-11-25 게시, 사진 설명) <https://news.kaist.ac.kr/news/html/news/?mode=V&mng_no=54990> (2026-10-25 열람)
[^news-md]: KAIST 뉴스 「KAIST 최초의 마이크로 디그리, 데이터사이언스 대학원 '기초 기계학습' 개설」(2022-09-08 게시) <https://news.kaist.ac.kr/news/html/news/?mode=V&mng_no=23350> (2026-10-25 열람)
[^news-lig]: KAIST 뉴스 「LIG넥스원과 ‘국방 자율시스템 연구센터’ 설립·협력 확대」(2025-07-03 게시) <https://news.kaist.ac.kr/news/html/news/?mode=V&mng_no=48630> (2026-10-25 열람)
[^aw-icml26]: 응용인공지능 연구실 누리집 Awards 「[Award] ICML'26 AI4Math Visual Grounded Physics Problem Solving 우승」(2026-07-23 게시) <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub7_1&wr_id=69> (2026-10-25 열람)
[^aw-qif26]: 응용인공지능 연구실 누리집 Awards 「[Award] 신동혁 학생의 Qualcomm Innovation Fellowship Korea 수상」(2026-01-07 게시) <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub7_1&wr_id=68> (2026-10-25 열람)
[^aw-proto]: 응용인공지능 연구실 누리집 Awards 「[Award] AI Drone 및 공중전 시뮬레이터 KAIST Institute Prototype 우수상 수상」(2025-12-17 게시) <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub7_1&wr_id=66> (2026-10-25 열람)
[^aw-nbh-ki]: 응용인공지능 연구실 누리집 Awards 「[Award] 나병후 박사 KAIST Institute 우수연구자상 수상」(2025-12-17 게시) <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub7_1&wr_id=65> (2026-10-25 열람)
[^aw-itrc]: 응용인공지능 연구실 누리집 Awards 「[Award] ITRC Challenge 2025 창의도전상(AWS) 수상」(2025-09-04 게시) <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub7_1&wr_id=64> (2026-10-25 열람)
[^aw-nbh-best]: 응용인공지능 연구실 누리집 Awards 「[Award] 나병후 박사, 공과대학 박사학위 최우수논문상 수상」(2025-02-18 게시) <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub7_1&wr_id=63> (2026-10-25 열람)
[^aw-nhh]: 응용인공지능 연구실 누리집 Awards 「[Award] 나형호 박사, Global Leadership Award 수상」(2025-02-17 게시) <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub7_1&wr_id=62> (2026-10-25 열람)
[^aw-qif24b]: 응용인공지능 연구실 누리집 Awards 「[Award] 나병후 학생의 Qualcomm Innovation Fellowship Korea 수상」(2024-12-30 게시) <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub7_1&wr_id=61> (2026-10-25 열람)
[^aw-army]: 응용인공지능 연구실 누리집 Awards 「[Award] 육군 M&S 국제학술대회 논문 장려상 수상」(2024-12-18 게시) <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub7_1&wr_id=60> (2026-10-25 열람)
[^aw-tdrc]: 응용인공지능 연구실 누리집 Awards 「[Award] 특화연구센터 우수 연구인력 수상」(2024-08-05 게시) <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub7_1&wr_id=58> (2026-10-25 열람)
[^aw-icml24]: 응용인공지능 연구실 누리집 Awards 「[Award] ICML 2024 Challenge Award」(2024-07-31 게시) <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub7_1&wr_id=57> (2026-10-25 열람)
[^aw-kdj]: 응용인공지능 연구실 누리집 Awards 「[Award] 김동준 박사, 우수학위논문상 수상」(2024-03-06 게시) <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub7_1&wr_id=55> (2026-10-25 열람)
[^aw-qif24a]: 응용인공지능 연구실 누리집 Awards 「[Award] 배희선, 신승재 학생의 Qualcomm Innovation Fellowship Korea (재)수상」(2024-01-19 게시) <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub7_1&wr_id=54> (2026-10-25 열람)
[^aw-jmg]: 응용인공지능 연구실 누리집 Awards 「[Award] 지민기 박사, 우수학위논문상 수상」(2023-03-04 게시) <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub7_1&wr_id=53> (2026-10-25 열람)
[^aw-qif23]: 응용인공지능 연구실 누리집 Awards 「[Award] 배희선, 신승재 학생의 Qualcomm Innovation Fellowship Korea 수상」(2023-03-02 게시) <https://aai.kaist.ac.kr/bbs/board.php?bo_table=sub7_1&wr_id=52> (2026-10-25 열람)
[^p1]: D. Kim 외, I.-C. Moon, International Conference on Machine Learning (ICML 2023; 누리집 표기) (2023). <https://arxiv.org/abs/2211.17091> 초록 기준(arXiv 판).
[^p2]: B. Na 외, I.-C. Moon, 41st International Conference on Machine Learning, ICML 2024 (2024). <https://pure.kaist.ac.kr/en/publications/diffusion-rejection-sampling/> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p3]: H. S. Bae, S. Shin, B. Na, I.-C. Moon, 12th International Conference on Learning Representations, ICLR 2024 (2024). <https://pure.kaist.ac.kr/en/publications/dirichlet-based-per-sample-weighting-by-transition-matrix-for-noi/> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p4]: D. Shin 외, I.-C. Moon, 13th International Conference on Learning Representations, ICLR 2025, 60903-60934 (2025). <https://pure.kaist.ac.kr/en/publications/distilling-dataset-into-neural-field/> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p5]: D. Shin 외, I.-C. Moon, International Conference on Learning Representations (ICLR 2026; 누리집 표기) (2026). <https://arxiv.org/abs/2510.15982> 초록 기준(arXiv 판).
[^p6]: B. Na 외, I.-C. Moon, International Conference on Learning Representations (ICLR 2026; 누리집 표기) (2026). <https://arxiv.org/abs/2602.01685> 초록 기준(arXiv 판).
[^p7]: H. Na, K. Lee, S. Lee, I.-C. Moon, 13th International Conference on Learning Representations, ICLR 2025, 86428-86454 (2025). <https://pure.kaist.ac.kr/en/publications/trajectory-class-aware-multi-agent-reinforcement-learning/> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p8]: J. Choi, J. W. Bae, I.-C. Moon, 2024 Winter Simulation Conference (WSC), 2118-2129 (2024). <https://doi.org/10.1109/wsc63780.2024.10838795> 초록 기준(OpenAlex 등록 초록).

# 데이터 마이닝 연구실 (Data Mining Lab)

**KAIST 전산학부·김재철AI대학원·데이터사이언스대학원 · 이재길 교수·석좌교수(Endowed Chair Professor)·학부장(Head)**

- 분야: 데이터 중심 인공지능, 시계열·이동 경로 데이터 분석, 온라인 이상 탐지, 연속학습, 분산 딥러닝
- 대분야: 컴퓨팅·AI
- 태그: 데이터 중심 AI·데이터 효율 학습[^research][^p1][^p2], 이상·변화점 탐지[^research][^p4], 연속학습[^p5][^p6], 연합학습·분산 학습[^research][^projects], 생성 인공지능[^p1][^projects], 대형 언어 모델[^projects], 멀티모달 AI[^p8]
- 홈페이지: <https://www.kaistdmlab.org/>
- 근거와 출처: [데이터 마이닝 연구실 근거 페이지](kaistdmlab-sources.md)

> 대규모 자료에서 패턴과 지식을 찾는 데이터 마이닝을 연구하며, 흐르는 자료와 이동 경로를 분석하고 잘못되거나 부족한 정답 표시, 변화하는 학습 환경, 자료 처리 비용의 문제를 푸는 연구실이다.[^research]

## 무엇을 연구하나

KAIST 전산학부 이재길 교수가 이끄는 데이터 마이닝 연구실은 2010년 12월 교수의 KAIST 부임과 함께 설립되었다. 데이터 마이닝(많은 자료에서 의미 있는 패턴과 지식을 찾아내는 기술)의 성능과 결과의 품질을 함께 다룬다. 연구 소개는 처리 성능을 높이기 위한 분산 처리(계산을 여러 컴퓨터나 장치에 나누어 수행하는 방식), 표본 추출, 색인을 들고, 분석 품질을 높이기 위해 오류가 있거나 부족한 라벨(학습 자료에 붙인 정답·범주 표시)을 다룬다고 설명한다. 교수 소개는 데이터 중심 AI(Data-Centric Artificial Intelligence, 학습 자료의 품질·선택·구성을 중심으로 인공지능을 개선하는 접근), 딥러닝(여러 단계의 표현을 학습하는 신경망을 이용한 기계학습), 이동·스트림 데이터 마이닝과 분산 딥러닝을 연구 관심으로 든다.[^cs][^research][^prof]

첫 갈래는 **학습 자료의 품질과 선택**이다. 잘못 붙은 정답에 견디는 학습 방법과 정답 표시가 부족한 자료를 활용하는 방법을 개발한다. 능동학습(모델이 정답을 요청할 자료를 고르는 학습 방법)에서는 관심 있는 범주에 속한 자료를 고르는 것과 학습에 유익한 자료를 고르는 것 사이의 균형을 MQ-Net(Meta-Query-Net)으로 조절한다. 시계열(시간 순서대로 놓인 관측 자료)의 정답 부족 문제에서는 대상 구간의 앞뒤 맥락을 바꿔 붙이고, 서로 다른 맥락에서도 정답 표시가 일관되도록 학습하는 방법을 제안했다. MRCA(Multi-Round Collaborative Augmentation)는 인스턴스 분할(이미지에서 개별 물체가 차지하는 영역을 각각 구분하는 작업) 모델의 피드백을 받아 합성할 물체의 종류·수·크기를 조정한다. 확산 모델(잡음을 넣는 과정과 그에 대응하는 생성 과정을 학습하는 모델)을 이용한 자료 생성을 여러 차례 학습과 연결해, 드문 범주의 자료를 보완하는 연구다.[^research][^p2][^p3][^p1]

둘째 갈래는 **시간에 따라 들어오는 자료와 사람·물건의 이동 분석**이다. 스트림 데이터(새 관측값이 계속 들어오는 자료)의 이상 탐지(자료에서 평소 양상과 다른 관측을 찾는 작업), 예측, 구간 분할을 다룬다. ARCUS는 데이터의 양상이 변하는 개념 변화에 대응하기 위해 여러 이상 탐지 모델을 보유하고, 현재 자료에 맞는 모델을 조합하며 모델 묶음을 갱신한다. 오토인코더(입력의 표현을 학습하고 그 표현에서 입력을 복원하도록 훈련하는 모델)를 쓰는 이상 탐지 방법에 적용할 수 있도록 설계했다. 이동 자료에서는 택시 수요·교통량·사고 위험 예측과 장소 추천을 연구한다고 밝힌다. Pincette는 이동통신 궤적에서 실제 방문한 POI(Point of Interest, 개별 관심 장소)를 추정하는 문제를 정의하고, 도로망과 장소의 맥락 등 외부 자료를 함께 이용하는 알고리즘을 제안했다.[^contact] 연구 소개는 시계열 분석을 위한 AutoML(Automated Machine Learning, 기계학습의 설계·학습 과정 일부를 자동화하는 기술)도 개발 대상으로 든다.[^research][^p4]

셋째 갈래는 **새 과제에 적응하면서 이전 지식을 유지하는 연속학습**이다. 연속학습은 새로운 자료나 과제가 차례로 주어질 때 앞서 배운 지식을 유지하며 계속 배우는 방법이다. AdaPromptCL은 과제 사이 의미의 유사성에 따라 프롬프트(모델의 반응이나 학습을 유도하기 위해 제공하는 입력) 묶음을 배정하고 계속 조정한다. AccuACL(Accumulated informativeness-based Active Continual Learning)은 새 과제의 학습뿐 아니라 이전 지식의 유지도 고려해 정답을 붙일 자료를 고른다. 이 논문은 피셔 정보 행렬(모델의 매개변수 변화가 관측 자료의 확률에 미치는 민감도를 나타내는 수학적 표현)을 선택 기준으로 이용한다. 과제 소개는 잡음과 편향에 대응하고 그래프 자료로 확장하는 연속학습을 개발한다고 설명한다.[^p5][^p6][^projects]

연구 범위는 **분산 학습과 언어 모델, 행동 자료 분석**으로도 이어진다. 연구 소개는 2024–2027년 SW Star Lab 과제 단계에서 자료를 나누는 학습과 모델을 나누는 학습을 지원하는 분산 딥러닝 플랫폼 개발을 계획한다고 밝힌다. 과제 소개에는 LLM(Large Language Model, 많은 언어 자료로 학습해 글을 이해하고 생성하는 모델)의 언러닝(학습한 특정 자료의 영향을 모델에서 제거하는 기술)에서 지식이 지나치게 삭제되는 문제를 다루는 연구가 있다. 스마트폰 행동 분석 공저 연구는 앱 안의 화면 상태 변화에서 반복 행동을 추출하고 언어 모델로 행동 과제를 정리하는 SHIRBT-MMF(Smartphone Human Interaction-based Routine Behavior Task Mining, Modeling, and Feature Extraction) 체계를 제안했다. 초록은 이 체계를 이용해 일상 스트레스를 관찰하고 시간에 따른 특징 변화에 대응한다고 설명한다.[^research][^projects][^p7] 비전-언어 모델(Vision-Language Model, VLM, 이미지와 글을 함께 다루는 모델) 연구에서는 RA-TTA(Retrieval-Augmented Test-Time Adaptation)를 제안했다. 테스트 시점 적응(Test-Time Adaptation, TTA)은 실제 입력이 주어지는 시점에 그 자료의 환경에 맞춰 모델의 동작이나 예측을 조정하는 방법이다. RA-TTA는 각 입력 이미지에 맞는 외부 이미지를 검색해 예측을 다듬으며, 세밀한 글 설명을 이용해 외부에서 얻는 지식의 세부 수준을 확장한다.[^p8]

## 주요 연구 주제

### 1. 학습 자료의 오류·부족·불균형 다루기

정답 표시 오류에 견디는 학습, 관심 범주 밖 자료가 섞인 능동학습의 자료 선택, 시계열의 앞뒤 맥락을 이용한 정답 보완, 모델의 피드백에 따른 반복적 자료 합성을 다룬다.[^research][^p1][^p2][^p3]

### 2. 데이터 흐름의 이상 탐지와 이동 자료 분석

시간에 따라 양상이 달라지는 자료에서 이상을 찾는 모델 조합·갱신과, 택시 수요·교통량·교통사고 위험 예측 및 장소 추천을 연구한다. 시계열 분석의 자동화와 이동통신 궤적에서 방문 장소를 추정하는 방법도 연구 대상이다.[^research][^p4][^contact]

### 3. 연속학습과 학습 자료 선택

새 과제와 이전 과제 사이의 관계에 따라 학습용 입력 묶음을 조정하고, 새로운 지식의 습득과 이전 지식의 유지를 함께 고려해 정답을 요청할 자료를 선택한다.[^p5][^p6]

### 4. 분산 딥러닝·언어 모델과 행동 분석

여러 계산 장치에 학습을 나누는 플랫폼, 언어 모델에서 특정 학습 자료의 영향을 제거하는 방법, 스마트폰 화면의 상태 변화에서 반복 행동을 추출하는 자료 분석 체계를 개발한다. 이미지와 글을 함께 다루는 모델의 예측을 외부 이미지 검색으로 보완하는 적응 방법도 연구한다.[^research][^projects][^p7][^p8]

## 대표 논문

2021–2026년 연구 가운데 이재길 교수가 저자인 논문 8편을 자료 품질, 시계열, 연속학습, 행동 분석과 비전-언어 모델의 적응에 걸쳐 골랐다. 학회 논문집과 연구자가 공개한 사전 공개본, 연구실이 게시한 논문 PDF의 초록을 이용했다. ARCUS는 KDD 2022 채택을 명시한 arXiv 판이고, AccuACL은 arXiv 사전 공개본으로 표시했다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [Sample-Efficient Multi-Round Generative Data Augmentation for Long-Tail Instance Segmentation](https://doi.org/10.52202/085713-2454) · NeurIPS 2025 | 이미지 속 물체를 구분하는 모델이 어떤 자료를 어려워하는지 알려 주면, 생성 모델이 그 피드백에 맞춰 필요한 물체를 만든다. 범주별 생성 수와 크기를 조정하고 학습 중 여러 차례 반복해 드문 범주의 자료를 보완한다. MRCA(Multi-Round Collaborative Augmentation)는 비교한 기존 방법에 필요한 자료 생성량의 6%만 사용하면서 이를 웃도는 성능을 보고했다.[^p1] | Byunghyun Kim, Minyoung Bae, Jae-Gil Lee(마지막 저자) |
| 2 | 2022 | [Meta-Query-Net: Resolving Purity-Informativeness Dilemma in Open-set Active Learning](https://doi.org/10.52202/068431-2278) · NeurIPS 2022 | 정답을 붙일 자료를 고를 때 관심 범주 밖의 자료를 거르는 데만 집중하면 학습에 유익한 자료를 놓칠 수 있다. MQ-Net은 능동학습의 여러 회차에서 얻은 자료로 두 기준의 균형을 조정하며, 별도 검증 자료 없이 선택기를 학습한다. 여러 범위 밖 자료 혼입 상황에서 기존 방법 대비 정확도 개선을 보고했다.[^p2] | Dongmin Park 외, Jae-Gil Lee(마지막 저자) |
| 3 | 2023 | [Context Consistency Regularization for Label Sparsity in Time Series](https://proceedings.mlr.press/v202/shin23e.html) · ICML 2023 | 시계열의 일부 구간에만 정답이 있을 때, 대상 구간 자체는 유지하면서 앞뒤 맥락을 달리 붙여 학습 자료를 만든다. 서로 다른 맥락을 붙인 자료 사이에서 신뢰도를 고려한 정답 표시를 공유해 예측이 일관되도록 학습하며, 실제 시계열 자료에서 기존 비교 방법을 웃도는 결과를 보고했다.[^p3] | Yooju Shin 외, Jae-Gil Lee(7명 중 6번째), Byung Suk Lee |
| 4 | 2022 | [Adaptive Model Pooling for Online Deep Anomaly Detection from a Complex Evolving Data Stream](https://doi.org/10.1145/3534678.3539348) · KDD 2022, 초록은 arXiv 판 | 들어오는 자료의 양상이 복잡하고 계속 바뀌면 하나의 탐지 모델로 대응하기 어렵다. ARCUS는 현재 자료에 맞는 여러 모델을 조합해 이상을 찾고, 변화에 따라 보유한 모델 묶음을 갱신한다. 여러 오토인코더 기반 탐지 방법에 적용할 수 있는 체계를 제안하고, 복잡성과 시간상 변화를 지닌 자료에서 정확도 개선을 보고했다.[^p4] | Susik Yoon, Youngjun Lee, Jae-Gil Lee(4명 중 3번째), Byung Suk Lee |
| 5 | 2024 | [One Size Fits All for Semantic Shifts: Adaptive Prompt Tuning for Continual Learning](https://proceedings.mlr.press/v235/kim24ai.html) · ICML 2024 | 새 과제의 의미가 이전 과제와 얼마나 다른지에 맞춰 프롬프트 묶음을 관리하는 AdaPromptCL을 제안했다. 과제 사이 유사성을 고려해 묶음을 배정하고 계속 다듬는다. 의미 변화의 정도가 다양한 평가 자료에서 기존 프롬프트 방법보다 최대 21.3% 개선된 결과를 보고했다.[^p5] | Doyoung Kim 외, Jae-Gil Lee(마지막 저자) |
| 6 | 2025 | [Active Learning for Continual Learning: Keeping the Past Alive in the Present](https://doi.org/10.48550/arXiv.2501.14278) · arXiv 사전 공개본 | 새 자료를 배우는 동안 이전 과제를 잊지 않도록, 정답을 붙일 자료를 고르는 AccuACL을 제안했다. 새 지식만을 기준으로 선택하는 문제를 다루기 위해 피셔 정보를 이용하며, 자료 선택 기준의 이론적 성질과 계산 확장성을 함께 다뤘다. 여러 연속학습 방법에 적용한 실험 결과를 보고했다.[^p6] | Jaehyun Park, Dongmin Park, Jae-Gil Lee(마지막 저자) |
| 7 | 2025 | [Leveraging Smartphone Human Interaction Routine Behavior Task Mining and Modeling for Daily Stress Monitoring](https://doi.org/10.1145/3770644) · IMWUT 9(4), 187 | 스마트폰 앱 사용량을 합산하는 대신 앱 안에서 반복되는 행동 과제를 찾아 스트레스와 관련된 특징을 얻는 체계를 제안했다. 순차 패턴 탐색과 언어 모델 기반 과제 정리를 결합해 화면 상태 변화에서 특징을 추출한다. 초록은 시간에 따른 자료·특징 변화에 대응하고 개인화한 스트레스 관찰에서 비교 방법 대비 개선을 보고했다.[^p7] | Hansoo Lee 외, Jae-Gil Lee(5명 중 4번째), Uichin Lee |
| 8 | 2025 | [RA-TTA: Retrieval-Augmented Test-Time Adaptation for Vision-Language Models](https://www.kaistdmlab.org/_files/ugd/c5ff4f_29115a906b4a40a0888dc7ae85cdb10a.pdf) · ICLR 2025 | 이미지와 글을 함께 다루는 모델은 미리 학습한 자료와 실제 입력의 성질이 달라지면 예측이 흔들릴 수 있다. RA-TTA는 모델 내부의 지식에 더해 입력 이미지에 맞는 외부 이미지를 검색해 예측을 보완한다. 세밀한 글 설명을 이용해 검색에서 얻는 지식의 세부 수준을 확장하며, 여러 평가 자료에서 기존 방법 대비 개선을 보고했다.[^p8] | Youngjun Lee 외, Jae-Gil Lee(마지막 저자·교신저자) |

## 교수와 전문 분야

이재길(Jae-Gil Lee) 교수는 전산학부 교수·석좌교수·학부장이며, 김재철AI대학원과 데이터사이언스대학원을 겸무한다. 전산학부 교수 명단은 전문 분야를 빅데이터·데이터마이닝·딥러닝으로 적는다. 교수 소개는 2010년 12월 KAIST 지식서비스공학 분야에 부임했고, 2020년 10월부터 전산학부 부교수, 2022년 9월부터 전산학부 교수로 재직한다고 적는다.[^faculty][^prof][^promotion]

최근 연구로 보면 전문 분야는 학습 자료의 오류·부족과 생성 자료의 효율을 다루는 데이터 중심 AI, 변화하는 시계열의 이상 탐지, 새 과제와 이전 지식의 균형을 다루는 연속학습으로 이어진다.[^p1][^p2][^p3][^p4][^p5][^p6] 비전-언어 모델의 환경 적응도 다룬다.[^p8] 연구실 구성원 페이지는 명예교수 항목에 Kyu-Young Whang을 별도로 소개하고 Database and Multimedia Lab의 전통을 잇는다고 적는다.[^members]

학회 운영 활동으로 이재길 교수는 KDD 2026의 General Co-Chair, DASFAA 2024의 Program Committee Co-Chair, Data Intelligence Workshop 2024의 Organizing Chair를 맡았다.[^chair][^service]

## 응용 분야

연구 소개는 공장·도시·데이터센터에서 생성되는 데이터 흐름의 분석, 택시 수요·교통량·사고 위험 예측과 장소 추천을 든다.[^research] 과제에는 센서 스트림의 이상 탐지, 서비스 장애 예측, 이동 자료를 이용한 군중 관리, 생성 이미지를 이용한 학습 자료 불균형 완화, 언어 모델의 언러닝이 있다.[^projects] 공저 논문에서는 스마트폰의 반복 행동을 이용한 일상 스트레스 관찰 체계를 개발했다.[^p7] 감염병의 디지털 접촉 추적에 이용할 수 있도록 이동통신 궤적에서 방문 장소를 추정하는 방법도 제안했다.[^contact]

## 구성원

2026년 10월 27일 연구실 Members 페이지의 Current Members 기준으로 박사후 2명, 박사과정 7명, 석사과정 10명이다. 과정은 InnoCore Postdoc, Ph.D. Student, Master Student 표기에 따른다. "대표 논문 참여"는 위 표의 번호이며, 논문 전체 저자 목록에서 같은 이름을 확인한 사람에게 표시했다.[^members]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Sungwon Park | 박사후연구원 |  |
| Youngjun Lee | 박사후연구원 | 2, 4, 5, 8 |
| Jihwan Bang | 박사과정 | 2, 5, 8 |
| Minyoung Bae | 박사과정 | 1 |
| Joeun Kim | 박사과정 |  |
| Byunghyun Kim | 박사과정 | 1, 3 |
| Jaehyun Park | 박사과정 | 6 |
| Hyunjin Kim | 박사과정 |  |
| Chanjae Song | 박사과정 |  |
| Junwoo Lee | 석사과정 |  |
| Jaemin Han | 석사과정 |  |
| Sugeun Yoon | 석사과정 |  |
| Euisoo Jung | 석사과정 |  |
| Suyeon Lee | 석사과정 |  |
| Wonhyeok Choi | 석사과정 |  |
| Geon Kang | 석사과정 |  |
| Hyewon Lee | 석사과정 |  |
| Uimin Lee | 석사과정 |  |
| Jaemin Kim | 석사과정 |  |

## 졸업생과 이전 구성원

2026년 10월 27일 Members 페이지의 박사 졸업생 19명과 석사 졸업생 48명이다. 박사는 2016–2026년, 석사는 2013–2026년의 학기 표기다. 같은 사람이 석사와 박사 목록에 각각 실려 있으며, 진로는 연구실이 게시한 기관·과정 표기다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Sungsu Lim | Ph.D. (Fall 2016) | Chungnam National University |
| Jungeun Kim | Ph.D. (Fall 2017) | Inha University |
| Sundong Kim | Ph.D. (Fall 2019) | GIST |
| Seungki Hong | Ph.D. (Spring 2020) | Samsung SDS |
| Minseo Kang | Ph.D. (Spring 2020) | SK Holdings |
| Jin-woo Lee | Ph.D. (Spring 2020) | Samsung SDS |
| Minsoo Choy | Ph.D. (Fall 2020) | Naver |
| Hwanjun Song | Ph.D. (Spring 2021) | KAIST |
| Susik Yoon | Ph.D. (Spring 2021) | Korea University |
| Minseok Kim | Ph.D. (Fall 2022) | Meta |
| Sejin Kim | Ph.D. (Spring 2023) | Chungnam National University |
| Dongmin Park | Ph.D. (Spring 2024) | KRAFTON |
| Yooju Shin | Ph.D. (Spring 2024) | Amazon |
| Junhyeok Kang | Ph.D. (Fall 2024) | LG AI Research |
| Patara Trirat | Ph.D. (Spring 2025) | DeepAuto (startup) |
| Doyoung Kim | Ph.D. (Spring 2026) | Amazon |
| Youngeun Nam | Ph.D. (Spring 2026) | University of Toronto (postdoc) |
| Youngjun Lee | Ph.D. (Fall 2026) | KAIST (postdoc) |
| Jihye Na | Ph.D. (Fall 2026) | Samsung Research |
| Juyup Sung | Master (Spring 2013) |  |
| Minsoo Choy | Master (Spring 2013) | Ph.D. Program |
| Jungeun Kim | Master (Spring 2013) | Ph.D. Program |
| Seunghyun Moon | Master (Fall 2013) | 29CM |
| Eunji Kim | Master (Spring 2015) | Attached Institute of ETRI |
| Junghoon Kim | Master (Spring 2015) | UNIST |
| Hwanjun Song | Master (Spring 2016) | Ph.D. Program |
| Hyunyoung Kim | Master (Spring 2016) | Zum Internet |
| Hyunseok Yang | Master (Fall 2016) |  |
| Hyungook Kang | Master (Fall 2016) | AKA Intelligence |
| Sojin Kim | Master (Fall 2016) | KT Research |
| Susik Yoon | Master (Spring 2017) | Ph.D. Program |
| Hyeongju Choi | Master (Spring 2017) | Naver |
| Daehoon Kim | Master (Fall 2017) | HayanMind Inc. (startup) |
| Soojeong Yu | Master (Fall 2017) | SK Telecom |
| Sohyun Kim | Master (Spring 2018) | RideFlux (startup) |
| Gwangseon Jang | Master (Spring 2018) | KISTI |
| Minseok Kim | Master (Fall 2018) | Ph.D. Program |
| Younghun Song | Master (Spring 2019) | Coupang Play |
| Hyunsoo Kim | Master (Spring 2019) | KT Research |
| Yooju Shin | Master (Fall 2019) | Ph.D. Program |
| Dongmin Park | Master (Spring 2020) | Ph.D. Program |
| Junhyeok Kang | Master (Spring 2020) | Ph.D. Program |
| Yu Yao | Master (Spring 2020) | ByteDance |
| Patara Trirat | Master (Fall 2020) | Ph.D. Program |
| Sewon Kim | Master (Fall 2020) | Onepredict (startup) |
| Youngjun Lee | Master (Spring 2021) | Ph.D. Program |
| Changseok Han | Master (Spring 2021) |  |
| Soojin Lim | Master (Fall 2021) | Team Blackbird (startup) |
| Andrei Son | Master (Fall 2021) | Philip Morris |
| Doyoung Kim | Master (Spring 2022) | Ph.D. Program |
| Youngeun Nam | Master (Spring 2022) | Ph.D. Program |
| Jihye Na | Master (Fall 2022) | Ph.D. Program |
| Hyangsuk Min | Master (Fall 2022) | HL Mando |
| Taeyoon Kim | Master (Spring 2023) | Kurly |
| Minyoung Bae | Master (Fall 2023) | Ph.D. Program |
| Joeun Kim | Master (Fall 2023) | Ph.D. Program |
| Byunghyun Kim | Master (Spring 2024) | Ph.D. Program |
| Yeongsin Byeon | Master (Spring 2024) | KOLON BENIT |
| Jaehyun Park | Master (Spring 2025) | Ph.D. Program |
| Seola Choi | Master (Spring 2025) | Samsung Research |
| Irfan Akbar | Master (Spring 2025) | Samsung Electronics |
| Seonghyun Park | Master (Spring 2025) |  |
| Kiseon Yu | Master (Spring 2025) | SK Hynix |
| Hyunjin Kim | Master (Spring 2026) | Ph.D. Program |
| Seonghye Cho | Master (Spring 2026) | SK Telecom |
| Youngjin Seo | Master (Spring 2026) | Freelancer |
| Jeongwoo Son | Master (Fall 2026) | Boss Semiconductors |

## 최근 논문 목록 (2021–2026)

시계열의 이상 탐지·예측, 학습 자료의 선택과 품질, 연속학습, 이동 자료 분석, 언어·시각 모델을 다룬다. 연구실 Publications 페이지의 2021–2026년 구역에 있는 학회·학술지·튜토리얼 55편이며 제목·저자·발표처는 연구실 표기다. 연구실 소식에서 채택을 확인한 학회 항목은 채택으로 표시했다. 그 밖의 2026년 학회 항목의 월은 누리집 기재 날짜다.[^pubs][^home][^accept]

**2026**

- Son, J., Na, J., Lee, U., and Lee, J. "STAAR: Spatio-Temporal Attention over Adaptive Regions for Traffic Forecasting". *In Proc. 35th ACM Int'l Conf. on Information and Knowledge Management (CIKM), Rome, Italy, Nov. 2026*.
- Choi, S., Kim, H., Lee, J., and Park, C. "Compositional Spectral Prompts for LLM-based Online Time Series Forecasting". *In Proc. 35th ACM Int'l Conf. on Information and Knowledge Management (CIKM), Rome, Italy, Nov. 2026*.
- Kim, H., Nam, Y., Han, J., Choi, W., and Lee, J. "Clustering-Based Balanced Sampling and Allocation with Data Parallelism for High-Performance Fine-Tuning". *In Proc. 2026 Conf. on Empirical Methods in Natural Language Processing (EMNLP), Budapest, Hungary, Oct. 2026 (채택)*.
- Nam, Y., Kim, J., Song, H., Yoon, S., Lee, J., and Lee, B. S. "TimelyRAG: Semantic-Temporal Hybrid Retrieval for Time-Critical Question Answering in Overlapping-Evolving Documents". *In Findings of the Association for Computational Linguistics: EMNLP 2026, Budapest, Hungary, Oct. 2026 (채택)*.
- Choi, J., Yun, T., Ban, M., Sun, G., Lee, J., and Song, H. "Towards Query-Agnostic RAG Evaluation via Query Coverage and Claim Verifiability". *In Proc. 3rd Annual Conf. on Language Modeling (COLM), San Francisco, California, Oct. 2026*.
- Lee, Y., Kim, D., Kang, J., Song, H., and Lee, J. "CURE: Cumulative Knowledge Reuse for Efficient Device-Server Hybrid Inference in Vision-Language Models". *In Proc. 19th European Conf. on Computer Vision (ECCV), Malmö, Sweden, Sept. 2026 (채택)*.
- Kim, D., Lee, Y., Kim, J., Bang, J., Song, H., Yoon, S., and Lee, J. "Breaking the Reference Bottleneck via Learning to Rewrite Conversational Queries without Gold Reference Passages". *In Proc. 43rd Int'l Conf. on Machine Learning (ICML), Seoul, Korea, July 2026 (채택)*.
- Na, J., Trirat, P., Park, C., and Lee, J. "Time-PEFT: Temporal and Multichannel Complexity-Based Fine-Tuning for Time-Series Foundation Models". *In Proc. 43rd Int'l Conf. on Machine Learning (ICML), Seoul, Korea, July 2026 (채택)*.
- Kim, J., Yoon, S., Le, X., Nam, Y., Kim, D., Song, H., and Lee, J. "QuDAR: Query-Wise Dual-Perspective Adaptive Retrieval". *In Proc. 64th Annual Meeting of the Association for Computational Linguistics (ACL), San Diego, California, July 2026 (채택)*.
- Jung, E., Kim, B., Kim, H., Cho, S., and Lee, J. "Accelerating Diffusion via Hybrid Data-Pipeline Parallelism Based on Conditional Guidance Scheduling". *In Proc. 2026 IEEE/CVF Conf. on Computer Vision and Pattern Recognition (CVPR), Denver, Colorado, June 2026 (채택)*.
- Park, J., Ahn, M., Kim, M., Lee, J., Lee, J., and Park, D. "See and Fix the Flaws: Enabling VLMs and Diffusion Models to Comprehend Visual Artifacts via Agentic Data Synthesis". *In Proc. 2026 IEEE/CVF Conf. on Computer Vision and Pattern Recognition (CVPR), Denver, Colorado, June 2026 (채택)*.
- Ban, M., Choi, J., Min, H., Kim, N. H., Kim, M., Lee, J., and Song, H. "Completing Missing Annotation: Multi-Agent Debate for Accurate and Scalable Relevant Assessment for IR Benchmarks". *In Proc. 14th Int'l Conf. on Learning Representations (ICLR), Rio de Janeiro, Brazil, Apr. 2026*.
- Trirat, P., Shin, Y., Kang, J., Nam, Y., Na, J., Bae, M., Kim, J., Kim, B., and Lee, J. "Universal Time-Series Representation Learning: A Survey". *ACM Computing Surveys (CSUR), Online Published, May 2026*.

**2025**

- Kim, B., Bae, M., and Lee, J. "Sample-Efficient Multi-Round Generative Data Augmentation for Long-Tail Instance Segmentation". *In Proc. 39th Annual Conf. on Neural Information Processing Systems (NeurIPS), San Diego, California, Dec. 2025*.
- Lee, H., Park, T., Koh, Y., Lee, J., and Lee, U. "Leveraging Smartphone Human Interaction Routine Behavior Task Mining and Modeling for Daily Stress Monitoring". *In Proc. 2026 ACM Int'l Joint Conf. on Pervasive and Ubiquitous Computing (UbiComp) / Proc. ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT), Vol. 9, No. 4, pp. 187:1 ~ 187:45, Dec. 2025*.
- Trirat, P. and Lee, J. "MONAQ: Multi-Objective Neural Architecture Querying for Time-Series Analysis on Resource-Constrained Devices". *In Findings of the Association for Computational Linguistics: EMNLP 2025, Suzhou, China, Nov. 2025*.
- Nam, Y., Na, J., Yoon, S., Song, H., Lee, J., and Lee, B. S. "Bi-Modal Learning for Networked Time Series". *In Proc. 31st ACM SIGKDD Int'l Conf. on Knowledge Discovery and Data Mining (KDD), Toronto, Canada, pp. 2162~2173, Aug. 2025*.
- Na, J., Nam, Y., Kang, J., and Lee, J. "Mitigating Source Label Dependency in Time-Series Domain Adaptation under Label Shifts". *In Proc. 31st ACM SIGKDD Int'l Conf. on Knowledge Discovery and Data Mining (KDD), Toronto, Canada, pp. 2150~2161, Aug. 2025*.
- Na, J., Nam, Y., Yoon, S., Song, H., Lee, B. S., and Lee, J. "Mobility Networked Time-Series Forecasting Benchmark Datasets". *In Proc. 19th Int'l AAAI Conference on Web and Social Media (ICWSM), Copenhagen, Denmark, pp. 2539~2549, June 2025 (Dataset Track)*.
- Park, J., Park, D., and Lee, J. "Active Learning for Continual Learning: Keeping the Past Alive in the Present". *In Proc. 13th Int'l Conf. on Learning Representations (ICLR), Singapore, Singapore, Apr. 2025*.
- Lee, Y., Kim, D., Kang, J., Bang, J., Song, H., and Lee, J. "RA-TTA: Retrieval-Augmented Test-Time Adaptation for Vision-Language Models". *In Proc. 13th Int'l Conf. on Learning Representations (ICLR), Singapore, Singapore, Apr. 2025*.
- Park, S., Han, S., Xie, X., Lee, J., and Cha, M. "Adversarial Style Augmentation via Large Language Model for Robust Fake News Detection". *In Proc. The 2025 ACM Web Conference (TheWebConf), Sydney, Australia, pp. 4024~4033, Apr. 2025*.
- Kang, J., Shin, Y., and Lee, J. "VarDrop: Enhancing Training Efficiency by Reducing Variate Redundancy in Periodic Time Series Forecasting". *In Proc. 39th AAAI Conf. on Artificial Intelligence (AAAI), Philadelphia, Pennsylvania, pp. 17742~17749, Feb. 2025*.
- Kim, J., Seo, Y., Kim, Y., Kang, J., Shin, J., Trirat, P., and Lee, J. "Large Language Models are Zero-Shot Point-of-Interest Recommenders". *Data Mining and Knowledge Discovery, Vol. 39, No. 80, pp. 1~46, Sept. 2025*.
- Trirat, P. and Lee, J. "TFAS: Zero-Shot NAS for General Time-Series Analysis with Time-Frequency Aware Scoring". *Machine Learning, Vol. 114, No. 223, pp. 1~33, Aug. 2025*.
- Trirat, P. and Lee, J. "Neural Architecture Search for Anomaly Detection in Multivariate Time Series". *IEEE Trans. on Emerging Topics in Computational Intelligence (TETCI), Vol. 9, No. 4, pp. 2924~2939, Aug. 2025*.

**2024**

- Shin, Y., Park, J., Yoon, S., Song, H., Lee, B. S., and Lee, J. "Exploiting Representation Curvature for Boundary Detection in Time Series". *In Proc. 38th Annual Conf. on Neural Information Processing Systems (NeurIPS), Vancouver, Canada, Dec. 2024*.
- Bae, M., Shin, Y., Nam, Y., Lee, Y. S., and Lee, J. "Semi-Supervised Learning for Time Series Collected at a Low Sampling Rate". *In Proc. 30th ACM SIGKDD Int'l Conf. on Knowledge Discovery and Data Mining (KDD), Barcelona, Spain, pp. 59~70, Aug. 2024*.
- Kim, D., Yoon, S., Park, D., Lee, Y., Song, H., Bang, J., and Lee, J. "One Size Fits All for Semantic Shifts: Adaptive Prompt Tuning for Continual Learning". *In Proc. 41st Int'l Conf. on Machine Learning (ICML), Vienna, Austria, July 2024*.
- Bang, J., Ahn, S., and, Lee, J. "Active Prompt Learning in Vision Language Models". *In Proc. 2024 IEEE/CVF Conf. on Computer Vision and Pattern Recognition (CVPR), Seattle, Washington, pp. 26994~27004, June 2024*.
- Nam, Y., Yoon, S., Shin, Y., Bae, M., Song, H., Lee, J., and Lee, B. S. "Breaking the Time-Frequency Granularity Discrepancy in Time-Series Anomaly Detection". *In Proc. The 2024 ACM Web Conference (TheWebConf), Singapore, Singapore, pp. 4204~4215, May 2024*.
- Kim, D., Park, D., Shin, Y., Bang, J., Song, H., and Lee, J. "Adaptive Shortcut Debiasing for Online Continual Learning". *In Proc. 38th AAAI Conf. on Artificial Intelligence (AAAI), Vancouver, Canada, pp. 13122~13131, Feb. 2024*.
- Song, H., Kim, M., and Lee, J. "Toward Robustness in Multi-label Classification: A Data Augmentation Strategy against Imbalance and Noise". *In Proc. 38th AAAI Conf. on Artificial Intelligence (AAAI), Vancouver, Canada, pp. 21592~21601, Feb. 2024*.

**2023**

- Park, D., Choi, S., Kim, D., Song, H., and Lee, J. "Robust Data Pruning under Label Noise via Maximizing Re-labeling Accuracy". *In Proc. 37th Annual Conf. on Neural Information Processing Systems (NeurIPS), New Orleans, Louisiana, Dec. 2023*.
- Nam, Y., Trirat P., Kim, T., Lee, Y., and Lee, J. "Context-Aware Deep Time-Series Decomposition for Anomaly Detection in Businesses". *In Proc. 2023 European Conf. on Machine Learning and Principles and Practice of Knowledge Discovery in Databases (ECML PKDD), Torino, Italy, pp. 330~345, Sept. 2023*.
- Shin, Y., Yoon, S., Song, H., Park, D., Kim, B., Lee, J., and Lee, B. S. "Context Consistency Regularization for Label Sparsity in Time Series". *In Proc. 40th Int'l Conf. on Machine Learning (ICML), Honolulu, Hawaii, pp. 31579~31595, July 2023*.
- Min, H. and Lee, J. "Temporal Convolutional Network-Based Time-Series Segmentation". *In Proc. 2023 IEEE Int'l Conf. on Big Data and Smart Computing (BigComp), Jeju, Korea, pp. 269 ~ 276, Feb. 2023 (regular paper)*.
- Trirat, P., Nam, Y., Kim, T., and Lee, J. "AnoViz: A Visual Inspection Tool of Anomalies in Multivariate Time Series". *In Proc. 37th AAAI Conf. on Artificial Intelligence (AAAI), Washington, DC, pp. 16488 ~ 16490, Feb. 2023*.
- Song, H., Kim, M., Park, D., Shin, Y., and Lee, J. "Learning from Noisy Labels with Deep Neural Networks: A Survey". *IEEE Trans. on Neural Networks and Learning Systems (TNNLS), Vol. 34, No. 11, pp. 8135~8153, Nov. 2023*.
- Whang, S. E., Roh, Y., Song, H., Lee, J. "Data Collection and Quality Challenges in Deep Learning: A Data-Centric AI Perspective". *The VLDB Journal, Vol. 32, No. 4, pp. 791 ~ 813, July 2023*.
- Trirat, P., Yoon, S., and Lee, J. "MG-TAR: Multi-view Graph Convolutional Networks for Traffic Accident Risk Prediction". *IEEE Trans. on Intelligent Transportation Systems (T-ITS), Vol. 24, No. 4, pp. 3779 ~ 3794, Apr. 2023*.

**2022**

- Park, D., Shin, Y., Bang, J., Lee, Y., Song, H., and Lee, J. "Meta-Query-Net: Resolving Purity-Informativeness Dilemma in Open-set Active Learning". *In Proc. 36th Annual Conference on Neural Information Processing Systems (NeurIPS), New Orleans, Louisiana, Dec. 2022*.
- Park, D., Kang, J., Song, H., Yoon, S., and Lee, J. "Multi-view POI-level Cellular Trajectory Reconstruction for Digital Contact Tracing of Infectious Diseases". *In Proc. of 22nd IEEE Int'l Conf. on Data Mining (ICDM), Orlando, Florida, pp. 1137 ~ 1142, Nov. 2022*.
- Yoon, S., Lee, Y., Lee, J., and Lee, B. S. "Adaptive Model Pooling for Online Deep Anomaly Detection from a Complex Evolving Data Stream". *In Proc. 28th ACM SIGKDD Int'l Conf. on Knowledge Discovery and Data Mining (KDD), Washington, D.C., pp. 2347 ~ 2357, Aug. 2022*.
- Shin, Y., Yoon, S., Kim, S., Song, H., Lee, J., and Lee, B. S. "Coherence-based Label Propagation over Time Series for Accelerated Active Learning". *In Proc. 10th Int'l Conf. on Learning Representations (ICLR), Virtual Event, Apr. 2022*.
- Kim, M., Song, H., Shin, Y., Park, D., Shin, K., and Lee, J. "Meta-Learning for Online Update of Recommender Systems". *In Proc. 36th AAAI Conf. on Artificial Intelligence (AAAI), Virtual Event, pp. 4065 ~ 4074, Feb. 2022*.
- Kim, D., Min, H., Nam, Y., Song, H., Yoon, S., Kim, M., and Lee, J. "COVID-EENet: Predicting Fine-Grained Impact of COVID-19 on Local Economies". *In Proc. 36th AAAI Conf. on Artificial Intelligence (AAAI), Virtual Event, pp. 11971 ~ 11981, Feb. 2022*.
- Whang, K., Lee, J., Lim, H., and Na, I. "A Bird's Eye View of the 4th Industrial Revolution Technologies". *IEEE Data Engineering Bulletin, Vol. 45, No. 3, pp. 4 ~ 16, Sept. 2022*.

**2021**

- Park, D., Song, H., Kim, M., and Lee, J. "Task-Agnostic Undesirable Feature Deactivation Using Out-of-Distribution Data". *In Proc. 35th Annual Conference on Neural Information Processing Systems (NeurIPS), Virtual Event, pp. 4040 ~ 4052, Dec. 2021*.
- Song, H., Kim, E., Jampani, V., Sun, D., Lee, J., and Yang, M. "Exploiting Scene Depth for Object Detection with Multimodal Transformers". *In Proc. 32nd British Machine Vision Conference (BMVC), Virtual Event, UK, pp. 1 ~ 14, Nov. 2021*.
- Song, H., Kim, M., Park, D., Shin, Y., and Lee, J. "Robust Learning by Self-Transition for Handling Noisy Labels". *In Proc. 27th ACM SIGKDD Int'l Conf. on Knowledge Discovery and Data Mining (KDD), Virtual Event, Singapore, pp. 1490 ~ 1500, Aug. 2021*.
- Yoon, S., Shin, Y., Lee, J., and Lee, B. S. "Multiple Dynamic Outlier-Detection from a Data Stream by Exploiting Duality of Data and Queries". *In Proc. 2021 ACM Int'l Conf. on Management of Data (SIGMOD), Virtual Event, China, pp. 2063 ~ 2075, June 2021*.
- Trirat, P. and Lee, J. "DF-TAR: A Deep Fusion Network for Citywide Traffic Accident Risk Prediction with Dangerous Driving Behavior". *In Proc. The Web Conference 2021 (TheWebConf), Virtual Event, Slovenia, pp. 1146 ~ 1156, Apr. 2021*.
- Kim, M., Song, H., Kim, D., Shin, K., and Lee, J. "PREMERE: Meta-Reweighting via Self-Ensembling for Point-of-Interest Recommendation". *In Proc. 35th AAAI Conf. on Artificial Intelligence (AAAI), Virtual Event, pp. 4164 ~ 4171, Feb. 2021*.
- Lee, J., Roh, Y., Song, H., and Whang, S. E. "Machine Learning Robustness, Fairness, and their Convergence". *In Proc. 27th ACM SIGKDD Int'l Conf. on Knowledge Discovery and Data Mining (KDD), Virtual Event, Singapore, pp. 4046 ~ 4047, Aug. 2021*.

## 과제

수행 기간이 2021년 10월 13일–2026년 10월 13일과 하루라도 겹치는 과제 8건이다. 과제 이름·역할·지원기관·기간은 연구실 Projects 페이지 표기다.[^projects]

- DB4DL: High-Usability and Performance In-Memory Distributed DBMS for Deep Learning (역할 Principle Investigator; 지원 Institute for Information & Communications Technology Planning & Evaluation (IITP); 기간 4/1/2020 ~ 12/31/2027)
- Robust, Fair, Extensible Data-Centric Continual Learning (역할 Principle Investigator; 지원 Institute for Information & Communications Technology Planning & Evaluation (IITP); 기간 4/1/2022 ~ 12/31/2026)
- Core Technologies for Crowd Management Systems Using AI and Mobility Big Data (역할 Principle Investigator; 지원 National Research Foundation of Korea (NRF); 기간 3/1/2023 ~ 2/28/2026)
- Online Deep Learning Technology for Anomaly Detection from Sensor Stream Big Data (역할 Principle Investigator; 지원 Samsung Electronics Co., Ltd.; 기간 9/16/2020 ~ 9/15/2025)
- Improving the Responsibility of LLMs via Unlearning on Intel Gaud (역할 Principle Investigator; 지원 Naver Cloud (and Intel); 기간 7/1/2024 ~ 6/30/2027)
- Data Augmentation Technology using Synthesized Data for Improving AI Model Performance (역할 Principle Investigator; 지원 Samsung Electronics Co., Ltd.; 기간 5/31/2024 ~ 5/30/2025)
- Development of Real-Time Service Incident Prediction Technology (역할 Principle Investigator; 지원 Samsung Electronics Co., Ltd.; 기간 7/1/2021 ~ 7/31/2023)
- AutoML for Deep Learning Analytics of Multivariate Stream Big Data (역할 Principle Investigator; 지원 National Research Foundation of Korea (NRF); 기간 9/1/2020 ~ 2/28/2023)

## 수상과 선정

연구실 Award 목록에서 2021년 10월 13일–2026년 10월 13일에 게시한 수상·선정 소식 5건이다.[^awards][^award2025]

- 2025-02-14 · 연구실의 「Reducing Real-World AI Training Cost and Its Application to Control of Infectious Diseases」가 KAIST의 2024년 연구성과로 선정되었다.
- 2023-12-18 · 이재길 교수가 College of Engineering Technology Innovation Award를 받았다.
- 2023-11-28 · 이재길 교수가 Q 부문 KAIST Q-Day Faculty Special Award를 받았다.
- 2023-04-21 · 이재길 교수가 정보통신 분야 Prime Minister's Commendation을 받았다.
- 2021-10-15 · 이재길 교수가 NeurIPS 2021 Outstanding Reviewer Award 수상자로 선정되었다.

## 최근 소식

논문 채택, 학회 운영, 연구 지원에 관한 소식이다. 게시 날짜는 2022년 1월 21일–2026년 8월 21일이다.[^accept][^home][^emnlp][^eccv][^chair][^service][^grants]

- 2026-08-21 · EMNLP 2026에 논문 2편이 채택되었다.
- 2026-08-13 · 이재길 교수가 8월 9–13일 제주에서 열린 KDD 2026의 General Co-Chair를 맡았다.
- 2026-06-18 · CURE 논문이 ECCV 2026에 채택되었다.
- 2026-05-01 · ICML 2026에 논문 2편이 채택되었다.
- 2026-04-07 · QuDAR 논문이 ACL 2026에 채택되었다.
- 2026-02-21 · CVPR 2026에 논문 2편이 채택되었다.
- 2025-09-19 · MRCA 논문이 NeurIPS 2025에 채택되었다.
- 2025-05-15 · KDD 2025에 논문 2편이 채택되었다.
- 2025-01-23 · ICLR 2025에 논문 2편이 채택되었다.
- 2024-12-10 · VarDrop 논문이 AAAI 2025에 채택되었다.
- 2024-09-26 · 시계열 경계 탐지 논문이 NeurIPS 2024에 채택되었다.
- 2024-07-12 · 이재길 교수가 Data Intelligence Workshop 2024의 Organizing Chair를 맡았다.
- 2024-07-04 · 이재길 교수가 DASFAA 2024의 Program Committee Co-Chair를 맡았다.
- 2024-07-01 · NAVER-Intel-KAIST Joint AI Research Center를 통해 언어 모델의 학습 내용 삭제 연구 지원을 받았다.
- 2024-05-31 · 삼성리서치에서 학습 자료 불균형을 다루는 데이터 합성 연구 지원을 받았다.
- 2024-05-17 · KDD 2024에 논문이 채택되었다.
- 2024-05-02 · ICML 2024에 논문이 채택되었다.
- 2024-02-27 · CVPR 2024에 논문이 채택되었다.
- 2024-01-23 · TheWebConf 2024에 논문이 채택되었다.
- 2023-12-09 · AAAI 2024에 논문 2편이 채택되었다.
- 2023-09-22 · 라벨 오류가 있는 자료의 가지치기 논문이 NeurIPS 2023에 채택되었다.
- 2023-04-25 · Context Consistency Regularization 논문이 ICML 2023에 채택되었다.
- 2022-09-15 · Meta-Query-Net 논문이 NeurIPS 2022에 채택되었다.
- 2022-05-19 · 온라인 이상 탐지 논문이 KDD 2022에 채택되었다.
- 2022-04-14 · IITP의 Robust, Fair, Extensible Data-Centric Continual Learning 과제 연구 지원을 받았다.
- 2022-01-21 · 시계열의 라벨 전파 논문이 ICLR 2022에 채택되었다.

## 연락과 위치

- 교수 전화: +82-42-350-3545, 팩스: +82-42-350-1610[^prof]
- 교수연구실: E3-1, 2435호(전산학부 교수 명단)[^faculty]
- 연구실 사무실: E3-1, 2442호(전산학부 연구실 소개)[^cs]
[^home]: Data Mining Lab 첫 화면. 2026-10-27 관측. <https://www.kaistdmlab.org/>
[^cs]: KAIST 전산학부 데이터 마이닝 연구실 소개. 2026-10-27 관측. <https://cs.kaist.ac.kr/research/labView?sn=113&menu=64>
[^faculty]: KAIST 전산학부 교수 명단, 이재길 항목. 2026-10-27 관측. <https://cs.kaist.ac.kr/people/faculty>
[^prof]: Jae-Gil Lee 교수 소개: 소속·겸무, 경력, 연구 관심, 전화·팩스. 2026-10-28 관측. <https://www.kaistdmlab.org/jaegil>
[^research]: 연구 소개: 데이터 마이닝의 성능·품질, 시계열·이동 자료, 라벨 오류·부족, 분산 딥러닝 계획. 2026-10-27 관측. <https://www.kaistdmlab.org/research>
[^members]: Members: Professor, Current Members, Professor in Emeritus, Ph.D. Graduates, Master Graduates. 2026-10-27 관측. <https://www.kaistdmlab.org/members>
[^pubs]: Publications, 2021–2026년 구역의 Conference·Journal·Tutorial 항목. 2026-10-27 관측. <https://www.kaistdmlab.org/publications>
[^projects]: Projects: 진행·이전 과제와 각 과제의 목표, 지원기관·기간. 2026-10-27 관측. <https://www.kaistdmlab.org/projects>
[^accept]: Paper Accept 목록에 표시된 논문 채택 소식과 게시 날짜. 2026-10-28 관측. <https://www.kaistdmlab.org/news-1/categories/paper-accept>
[^chair]: KDD 2026 General Co-Chair, 게시 날짜 2026-08-13. 2026-10-28 관측. <https://www.kaistdmlab.org/post/kdd-2026-general-co-chair>
[^service]: Service 목록: Data Intelligence Workshop 2024 Organizing Chair, DASFAA 2024 Program Committee Co-Chair. 2026-10-28 관측. <https://www.kaistdmlab.org/news-1/categories/service>
[^grants]: Research Grant 목록: NAVER-Intel-KAIST, 삼성 자료 합성, IITP 연속학습 연구 지원 소식. 2026-10-28 관측. <https://www.kaistdmlab.org/news-1/categories/research-grant>
[^awards]: Award 목록의 2021-10-15, 2023-04-21, 2023-11-28, 2023-12-18, 2025-02-14 항목. 2026-10-28 관측. <https://www.kaistdmlab.org/news-1/categories/award>
[^award2025]: AI 학습 비용과 감염병 대응 연구의 KAIST 연구성과 선정, 게시 날짜 2025-02-14. 2026-10-28 관측. <https://www.kaistdmlab.org/post/2024-kaist-top-10-research-achievements>
[^emnlp]: EMNLP 2026 Paper Accept: Main·Findings 각 1편 채택, 게시 표시 Aug 21, 수정 표시 Aug 29. 글 안의 학회 연도는 2026년이다. 2026-10-28 관측. <https://www.kaistdmlab.org/post/emnlp-2026-paper-accept>
[^eccv]: ECCV 2026 Paper Accept: CURE 채택, 게시 표시 Jun 18. 글 안의 학회 연도는 2026년이다. 2026-10-28 관측. <https://www.kaistdmlab.org/post/eccv-2026-paper-accept>
[^promotion]: Promotion 목록: 학부장·석좌교수 임명과 교수 승진. 2026-10-28 관측. <https://www.kaistdmlab.org/news-1/categories/promotion>
[^contact]: D. Park, J. Kang, H. Song, S. Yoon, J.-G. Lee, 2022 IEEE International Conference on Data Mining (ICDM), 1137–1142. DOI 10.1109/ICDM54844.2022.00144. 초록 기준(연구실 게시 PDF 초록). 초록 원문 <https://www.kaistdmlab.org/_files/ugd/c5ff4f_9961bdd46834470fbc73f0b0de28264b.pdf>. 2026-10-28 관측. <https://www.kaistdmlab.org/_files/ugd/c5ff4f_9961bdd46834470fbc73f0b0de28264b.pdf>
[^p1]: B. Kim, M. Bae, J.-G. Lee, Advances in Neural Information Processing Systems 38 (2025). <https://doi.org/10.52202/085713-2454> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://papers.nips.cc/paper_files/paper/2025/hash/69f59f96c3aae0ba9f463e7903715e1e-Abstract-Conference.html>. 2026-10-28 관측.
[^p2]: D. Park 외, J.-G. Lee, Advances in Neural Information Processing Systems 35 (2022). <https://doi.org/10.52202/068431-2278> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://papers.nips.cc/paper_files/paper/2022/hash/cba6f4460a1f395f68a88598c86e79bd-Abstract-Conference.html>. 2026-10-28 관측.
[^p3]: Y. Shin 외, B. S. Lee, Proceedings of the 40th International Conference on Machine Learning 202, 31579-31595 (2023). <https://proceedings.mlr.press/v202/shin23e.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v202/shin23e.html>. 2026-10-28 관측.
[^p4]: S. Yoon, Y. Lee, J.-G. Lee, B. S. Lee, arXiv (KDD 2022 Research Track 채택 표기) (온라인 2022-06-09). <https://doi.org/10.1145/3534678.3539348> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2206.04792>. 2026-10-28 관측.
[^p5]: D. Kim 외, J.-G. Lee, Proceedings of the 41st International Conference on Machine Learning 235, 24658-24673 (2024). <https://proceedings.mlr.press/v235/kim24ai.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v235/kim24ai.html>. 2026-10-28 관측.
[^p6]: J. Park, D. Park, J.-G. Lee, arXiv 사전 공개본 (온라인 2025-04-21). <https://doi.org/10.48550/arXiv.2501.14278> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2501.14278>. 2026-10-28 관측.
[^p7]: H. Lee 외, U. Lee, Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies 9, 187:1-187:45 (2025). <https://doi.org/10.1145/3770644> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://ic.kaist.ac.kr/publications/papers/lee2025leveraging.pdf>. 2026-10-28 관측.
[^p8]: Y. Lee 외, J.-G. Lee, International Conference on Learning Representations (ICLR 2025) (2025). <https://www.kaistdmlab.org/_files/ugd/c5ff4f_29115a906b4a40a0888dc7ae85cdb10a.pdf> 초록 기준(연구실 게시 PDF 초록). 초록 원문 <https://www.kaistdmlab.org/_files/ugd/c5ff4f_29115a906b4a40a0888dc7ae85cdb10a.pdf>. 2026-10-28 관측.

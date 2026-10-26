# 바이오정보시스템 연구실 (Bio-Information System Laboratory, BISL)

**KAIST 바이오및뇌공학과 · 이도헌 교수**

- 분야: 빅데이터와 인공지능 기반 신약 개발(약물 표적·부작용 단백질·약물 반응 예측, 네트워크 기반 약물 재창출, 천연물 기반 신약 후보 발굴), 해석 가능한 딥러닝과 유전자 네트워크로 질병 유전자와 환자 맞춤 치료 표적 찾기, 합성생물학을 위한 인공지능, 바이오정보학·의료정보학·데이터마이닝
- 대분야: 컴퓨팅·AI, 기초생명·생물물리
- 태그: 그래프 기계학습·지식 그래프[^p1][^p6], 과학·공학 AI[^research][^home], 바이오정보학·계산생물학[^research], AI 신약 개발[^p1], 설명 가능한 AI(XAI)[^resources]
- 홈페이지: <https://biosoft.kaist.ac.kr/>
- 근거와 출처: [바이오정보시스템 연구실 근거 페이지](biosoft-sources.md)

> 유전체·단백질·약물 반응 같은 대규모 생물 데이터를 인공지능과 생물학적 네트워크 분석으로 다뤄 신약 개발 문제를 푸는 바이오및뇌공학과 연구실이다. 2005년에 국가지정연구실로 지정되었고, 지금은 빅데이터와 인공지능 기반 신약 개발, 합성생물학을 위한 인공지능을 연구·교육 주제로 든다.[^home][^research]

## 무엇을 연구하나

누리집 첫 화면은 연구실이 의생명 분야의 문제를 풀 정보 기술을 개발한다고 소개하고, 지금의 연구·교육 주제로 「Big Data and AI-Based Drug Discovery」(빅데이터와 인공지능 기반 신약 개발)와 「AI for Synthetic Biology」(합성생물학을 위한 인공지능)를 든다.[^home] 연구 페이지는 신약 개발에 쓰는 빅데이터로 유전체학, 단백체학(몸속 단백질 전체를 분석하는 분야), 임상시험, 화합물 라이브러리 자료를 들고, 이 자료가 질병 기전과 약물 표적을 찾고 환자 반응을 예측하는 데 쓰이며, 기계학습이 약물 표적 찾기, 후보 물질 선별, 독성 예측, 임상시험 최적화 같은 단계를 돕는다고 설명한다.[^research]

연구 페이지는 연구실이 국책 사업인 바이오시너지 사업(bio-synergy project)으로 10년 넘게 디지털 가상 인체 시스템 CODA를 개발해 왔다고 적는다. CODA는 해석 가능한 심층 신경망(판단 근거를 사람이 따라가 볼 수 있게 만든 신경망)과 네트워크 생물학 방법을 만드는 기반이 되어, 복합 질환을 막고 치료할 신약과 기능성 식품 개발에 쓰인다고 소개한다.[^research] 교수 페이지는 교수가 이 사업단(유전자동의보감 국책사업단)의 단장을 2013–2022년에 맡았다고 적는다.[^prof] 교수가 마지막 저자로 쓴 책의 한 장(2021년)은 CODA 네트워크가 세포 사이 관계로 서로 이어진 수백 개의 세포별 네트워크로 이루어지고, 세포별 네트워크마다 분자, 세포 기능, 질병 수준의 층이 서로 연결되어 분자에서 질병까지의 생물 현상을 해석하거나 모의실험할 수 있다고 설명한다.[^coda]

합성생물학(생물 시스템을 새로 설계해 만들거나 기존 시스템을 다시 설계해 바이오 연료·의약품 같은 원하는 물질을 만드는 분야)에서는 유전체·단백체·대사체 자료를 분석해 설계한 생물이 여러 조건에서 어떻게 움직일지 예측하는 모형, 유전자 회로 설계, 실험 자동화에 인공지능을 쓰는 방향을 연구 페이지가 소개한다.[^research] 특허 목록에는 2024년에 출원한 「효소 반응 데이터 생성 방법 및 장치」가 있다.[^patents]

바이오및뇌공학과 교수진 목록은 교수의 연구분야를 바이오정보학, 의료정보학, 신경정보학, 데이터마이닝으로 적고, 누리집 교수 페이지는 관심 분야를 바이오정보학(Bioinformatics), 데이터마이닝(Data Mining), 의료정보학(Healthcare Informatics)으로 적는다.[^deptlist][^prof] 누리집 Resources 페이지는 연구실이 최근 개발해 GitHub에 공개한 분석 도구로, 생물 데이터를 해석하는 해석 가능한 신경망 VNN(Interpretable Neural Network for Biological Data Interpretation)과 MSGAT(Metapath-based Synchronized Graph Attention Network Model)를 들고, 연구실이 이용 허가를 받은 공개 생물 데이터베이스로 dbGaP(미국 국립보건원의 유전형·표현형 자료 저장소), DrugBank(약물과 약물 표적 데이터베이스), UK Biobank(영국의 대규모 유전·건강 자료)를 든다.[^resources]

## 주요 연구 주제

### 1. 약물 표적·부작용 단백질·약물 반응 예측

약이 몸속 어느 단백질에 작용하는지, 어떤 단백질이 부작용과 관련되는지, 세포가 약에 어떻게 반응하는지를 대규모 자료와 계산으로 예측한다. 대표 논문 1은 단백질 상호작용 네트워크(단백질들이 서로 붙어 작용하는 관계를 점과 선으로 나타낸 연결망) 위의 어떤 단백질이든 약물 부작용 관련 여부를 대규모로 예측하는 계산 방법 LAPINE을 제안했다.[^p1] 대표 논문 2는 약물을 처리한 뒤의 유전자 발현 변화와 다층 분자 네트워크를 써서 유전자에서 표적 단백질로 거슬러 올라가는 방법을 내놓았고, 대표 논문 3은 서로 다른 약물 반응 선별 자료를 하나로 통합한 세포주 표현을 딥러닝으로 만들어 약물 반응 예측에 썼다.[^p2][^p3] 특허 목록에는 2021년에 등록된 「딥러닝기반 화합물 의약효과 예측방법」이 있다.[^patents]

### 2. 네트워크 기반 약물 재창출과 천연물 신약 후보 발굴

이미 쓰이는 약을 다른 질병에 쓰는 약물 재창출과, 전통 의학 자료와 천연물에서 신약 후보를 찾는 일을 생물학적 네트워크와 계산 선별로 연구한다. 대표 논문 4는 파킨슨병 관련 경로에 함께 나타나는 상호작용의 중요도를 연결선 가중치로 반영한 네트워크로 파킨슨병 약물 재창출 방법을 제안했고, 대표 논문 5는 전통 한의학의 천연물 자료와 화합물-유전자 상호작용 자료를 결합해 질병별 천연물 유래 약물 후보를 고르는 파이프라인 NaCTR을 내놓았다.[^p4][^p5]

### 3. 해석 가능한 딥러닝·유전자 네트워크로 질병 유전자와 맞춤 표적 찾기

질병을 일으키는 유전자, 환자마다 다른 치료 표적, 여러 유전 변이의 조합 효과를 해석 가능한 딥러닝과 유전자 네트워크로 찾는다. 대표 논문 6은 그래프 어텐션 오토인코더로 암 종류별 암 유발 유전자를 예측하는 파이프라인 CancerGATE를 제안했다.[^p6] 대표 논문 7은 개인별 유전자 네트워크에서 유전자 무리의 결속 정도를 재는 점수를 만들어 유방암 환자별 치료 표적을 예측했으며, 연구실 소식은 이 기술을 COSINET으로 소개했다.[^p7][^news] 대표 논문 8은 정밀도가 다른 두 종류의 자료를 단계적으로 학습하는 딥러닝 기법으로 조현병에 영향을 주는 유전 변이 조합을 찾았고, 연구실 소식은 이 논문을 인공지능으로 조현병 치료의 실마리를 찾은 연구로 소개했다.[^p8][^news]

논문 목록에는 질병 유전자에 대한 기존 지식만으로 네트워크를 탐색해 자가면역 질환에 관여하는 조직 사이 신호 물질을 찾는 방법 InTiCAR(2025년)와, 면역세포와 암세포 양쪽의 CRISPR 유전자 선별 자료를 함께 분석해 면역항암 표적을 찾는 계산 방법(2022년)도 있다.[^inticar][^crispr]

### 4. 공동 연구

교수가 공동 저자로 참여한 공학 연구도 목록에 있다. 땀 속 대사물질을 표지 없이 시간 순서대로 재는 착용형 표면증강 라만 분광 패치(2025년, 11명 중 열째 저자)와, 근적외선 라이트필드 카메라로 얻은 얼굴 3차원 영상에서 표정을 읽는 기계학습 카메라(2022년, 7명 중 여섯째 저자) 연구다.[^sers][^lfc] 감염병의 회복 시간과 전파율에 따른 대유행 위험을 사람 사이 연결망에서 모의실험한 연구(2021년)도 있다.[^epi]

## 대표 논문

이도헌 교수가 KAIST에 있는 2021–2026년의 학술지 논문 가운데 교수가 마지막 저자이고 초록을 확인할 수 있는 논문을, 위의 세 연구 갈래에 고르게 여덟 편 골랐다. 저자 순서는 학술지 서지 기록(Crossref)을 따랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2022 | [Large-scale prediction of adverse drug reactions-related proteins with network embedding](https://doi.org/10.1093/bioinformatics/btac843) · Bioinformatics | 약물 부작용은 신약 개발과 임상 약리학의 큰 문제이고, 대부분은 약물이 의도하지 않은 표적에 작용해 생기므로 부작용에 책임 있는 약물 표적을 찾는 일이 중요하다. 부작용과 단백질의 관계를 분석하는 계산 방법이 여럿 나왔지만, 부작용 관련 단백질을 넓은 범위에서 믿을 만하게 찾는 일은 여전히 어렵다. 이 논문은 단일 표적 화합물(single-target compound)이라는 새 개념과 네트워크 임베딩(연결망의 각 점을 연결 관계를 반영한 숫자 묶음으로 바꾸는 기법)을 결합한 계산 방법 LAPINE을 제안해, 단백질 상호작용 네트워크 안의 어떤 단백질에 대해서도 부작용 관련 여부를 대규모로 예측할 수 있게 했다. 기준 자료 분석에서 분석 대상 단백질의 범위를 넓힐 필요를 확인했고, 알려진 부작용 관련 단백질을 높은 비율로 되찾았다. 앞서 제안된 방법에 비해 믿을 만한 예측을 냈으며(가치 부가 양성 예측도 0.12, P < 0.001), 두 사례 연구에서 예측한 단백질 대부분이 문헌 근거로 뒷받침되었다. 소스 코드는 GitHub와 Figshare에 공개했다.[^p1] | 1저자 J. Park(Jaesub Park), 마지막 저자 이도헌 (5명) |
| 2 | 2023 | [Reverse tracking from drug-induced transcriptomes through multilayer molecular networks reveals hidden drug targets](https://doi.org/10.1016/j.compbiomed.2023.106881) · Computers in Biology and Medicine | 약물의 분자 표적을 찾는 일은 신약 개발에 꼭 필요하다. 최근의 계산 방법은 주로 화합물과 단백질의 구조 정보에 기대는데, 3차원 구조 정보는 얻기 어렵고 2차원 구조를 쓰는 기계학습 방법은 자료 불균형 문제를 겪는다. 이 논문은 약물을 처리한 뒤의 유전자 전사 변화 자료와 다층 분자 네트워크를 써서, 유전자에서 표적 단백질로 거슬러 올라가는 역추적 방법을 제시했다. 어떤 단백질이 약물로 생긴 유전자 발현 변화를 얼마나 잘 설명하는지를 점수로 매기고, 이 점수로 알려진 약물 표적을 예측해 검증했다. 유전자 전사 자료를 쓰는 다른 방법보다 성능이 좋았고 약물의 분자 작용 기전도 제시할 수 있었으며, 코로나바이러스처럼 정해진 구조 정보가 없는 대상의 표적 예측에도 쓸 가능성이 있다고 적는다.[^p2] | 1저자 G. Kim(Gwangmin Kim), 마지막 저자 이도헌 (2명) |
| 3 | 2025 | [Unsupervised cell line embedding using pairwise drug response correlation](https://doi.org/10.1016/j.csbj.2025.06.018) · Computational and Structural Biotechnology Journal | 사람 세포주(실험실에서 계속 키울 수 있게 만든 사람 세포) 모델은 질병과 세포 기능을 이해하는 데 필요하고, 화합물과 그 효과를 체계적으로 선별할 수 있어 신약 개발에서 특히 중요하다. 그러나 측정 기법이 제각각이고 화합물 선별 자료와 오믹스 자료 속 세포주 특성 정보가 흩어져 있어 활용이 어렵다. 이 논문은 대조 학습(비슷한 것끼리는 가깝게, 다른 것끼리는 멀게 나타내도록 배우는 학습 방식)에 바탕을 둔 비지도 딥러닝 모델로 서로 다른 약물 반응 선별 자료를 하나의 세포주 임베딩(세포주의 특성을 담은 숫자 표현)으로 통합했다. 세포주 1,136개의 약물 반응 자료로 모델을 학습한 뒤 학습에 쓰지 않은 세포주 537개를 더 임베딩해, 유전자 발현 자료가 있는 Cancer Dependency Map(DepMap)의 암 세포주 1,673개 전체를 갖췄다. 이 임베딩을 넣으면 약물 시너지 예측, 세포주 약물 반응 예측 같은 과제의 기계학습 성능이 과제에 따라 다른 정도로 높아졌다. SHAP(각 입력이 예측 결과에 기여한 몫을 나누어 보여 주는 설명 기법)으로 임베딩에 크게 기여한 유전자를 찾았더니, 이 유전자들은 여러 암의 약물 내성과 여러 암 종류에 강하게 연관되어 있었다.[^p3] | 1저자 Y. Kim(Yutae Kim), 마지막 저자 이도헌 (2명) |
| 4 | 2024 | [Drug repurposing for Parkinson’s disease by biological pathway based edge-weighted network proximity analysis](https://doi.org/10.1038/s41598-024-71922-1) · Scientific Reports | 파킨슨병은 두 번째로 흔한 신경 퇴행성 질환이고 수명이 늘면서 심각해지고 있지만, 지금의 치료는 대부분 증상을 덜어 줄 뿐 진행을 막지 못한다. 신경 퇴행성 질환의 기전은 복잡해 생물 요소 사이의 상호작용을 이해해야 하고, 이 관계는 생물학적 네트워크로 효과적으로 분석할 수 있으며, 네트워크 안 상호작용마다 중요도가 다르다는 점을 고려하는 것도 중요하다. 이 논문은 파킨슨병 약물 재창출(이미 쓰이는 약을 다른 질병 치료에 쓰는 것)을 위해, 여러 파킨슨병 관련 경로에서 나타나는 상호작용을 다른 상호작용보다 중요하게 보고 그 중요도를 연결선 가중치에 반영하는 생물학적 경로 기반 가중 네트워크 구성 방법을 제안했다. 이 방법으로 알려진 파킨슨병 약물과 그렇지 않은 약물 사이의 효능 차이가 뚜렷하게 나타났고, 상호작용의 중요도 차이를 고려하지 않는 방법보다 약물-질병 상호작용을 정확히 예측했으며, 네트워크 안에서 약물과 질병을 잇는 경로가 그 약물의 작용 기전과 들어맞았다. 연구진은 이 방법으로 파킨슨병의 새 약물 후보와 그 작용 기전을 찾을 수 있다고 제시한다.[^p4] | 1저자 M. Han(Manyoung Han), 마지막 저자 이도헌 (3명) |
| 5 | 2024 | [NaCTR: Natural product-derived compound-based drug discovery pipeline from traditional oriental medicine by search space reduction](https://doi.org/10.1016/j.csbj.2024.10.035) · Computational and Structural Biotechnology Journal | 신약 개발 과정은 시간과 비용이 많이 들고 실패 위험이 높아, 그 위험을 줄이는 것이 중요한 목표다. 전통 동양 의학의 천연물은 오랜 사용 역사로 효능과 안전성이 뒷받침되어 주목받고, 여러 생물 데이터베이스를 쓰는 계산 방법도 많이 연구되었다. 그러나 전통 의학 자료에는 최근 흔해진 질병 정보가 부족하고, 실험 자료는 표적 후보의 범위를 지나치게 넓게 내놓기 쉽다. 이 논문은 두 접근을 결합해 주어진 질병에 대한 천연물 유래 약물 후보를 제안하는 계산 신약 후보 발굴 파이프라인 NaCTR을 제시했다. 먼저 문헌과 공개 데이터베이스에서 그 질병의 표현형(겉으로 드러나는 증상과 특징)과 질병 유전자를 찾고, 전통 의학의 표현형 기록과 화합물-유전자 상호작용 자료를 함께 써서 치료 가능성이 있는 천연물 후보를 고른 뒤, 그 천연물에 든 화합물을 독성과 약동학(몸에 들어간 약이 흡수·분포·대사·배설되는 과정) 성질로 다시 걸렀다. 파킨슨병을 사례로 시험해 글루타티온과 다른 화합물 네 개를 새 약물 후보로 제안하고 문헌 근거를 함께 제시했다.[^p5] | 1저자 S. Jung(Seunghwan Jung), 마지막 저자 이도헌 (5명) |
| 6 | 2024 | [CancerGATE: Prediction of cancer-driver genes using graph attention autoencoders](https://doi.org/10.1016/j.compbiomed.2024.108568) · Computers in Biology and Medicine | 암 종류마다 다른 암 유발 유전자(암이 생기고 자라는 데 핵심인 유전자)를 찾는 일은 각 암의 분자 기전을 이해하고 알맞은 치료를 정하는 데 중요하다. 그래프 딥러닝으로 암 유발 유전자를 찾는 방법이 널리 쓰이지만, 학습에 쓰는 암 유발 유전자가 적고 그 유전자 쪽으로 치우쳐 개별 암 종류에서는 성능이 제한되었다. 이 논문은 그래프 어텐션 오토인코더(GATE: 연결망에서 이웃 정보의 중요도를 따져 모으며, 입력을 스스로 되살리는 방식으로 특징을 배우는 신경망)를 자기 지도 방식으로 학습해 암 종류마다 적용할 수 있는 파이프라인 CancerGATE를 제안했다. 암 유전체 아틀라스(TCGA)의 15개 암 종류, 시료 20,079개의 생물학적 네트워크 구조와 다중 오믹스 자료를 쓰고, 모델이 계산한 어텐션 계수를 암과 정상 상태에서 비교해 암 유발 유전자의 순위를 매겼다. 암 종류별로 이전 그래프 딥러닝 모델보다 AUPRC(예측 성능 지표의 하나)가 높았고 그 차이는 1.5%에서 36.5%였다. 학습에 쓴 암 유발 유전자에 치우치지 않음을 보여 특정 암에서 암 유발 유전자의 기전을 드러냈고, 특정 암의 치료 표적이 될 수 있는 새 암 유발 유전자 후보를 제안했다.[^p6] | 1저자 S. Jung(Seunghwan Jung), 마지막 저자 이도헌 (3명) |
| 7 | 2024 | [Community cohesion looseness in gene networks reveals individualized drug targets and resistance](https://doi.org/10.1093/bib/bbae175) · Briefings in Bioinformatics | 사회과학에서 공동체 결속은 개인의 건강을 정하는 데 중요한 역할을 한다. 유전자 네트워크에도 서로 촘촘히 연결된 유전자 무리(공동체) 구조가 있어, 이 개념을 유전자 사이에 적용하면 정밀 종양학에서 단일 유전자 기반 바이오마커(질병 상태를 알려 주는 생체 지표)의 한계를 넘을 수 있다. 이 논문은 개인별 유전자 네트워크에서 각 공동체가 유전자 사이의 상호작용과 세포 기능을 유지하는 능력을 정량화하는 공동체 결속 점수를 개발했다. 유방암을 개념 검증 사례로 환자 시료 950개의 점수 분포를 재고, 두 단계로 개인별 치료 표적을 예측했다. 먼저 점수가 가장 많이, 또 상대적으로 낮아진 공동체 안에서 약물 표적이 될 수 있는 유전자를 고르고, 이어 각 개인 네트워크에서 결속 약화에 크게 기여하는 유전자를 찾아 표적을 좁혔다. 약물 감수성 자료로 볼 때 효과적인 개인별 항암 화학요법 표적 예측 성능이 이전 접근보다 최소 네 배 높았고, 알려진 유방암 아형을 찾아냈으며, 삼중음성 유방암의 새 표적 치료 후보(예: KIT, GABRP)를 제안했다. 또 ER 양성 유방암에서 타목시펜 반응을 예측하고, 개인 특성에 따라 내분비 치료 내성을 줄일 병용 요법 후보(예: NAMPT·RXRA 억제제)를 제안했다.[^p7] | 1저자 S. Wang(Seunghyun Wang), 마지막 저자 이도헌 (2명) |
| 8 | 2024 | [Interpretation of SNP combination effects on schizophrenia etiology based on stepwise deep learning with multi-precision data](https://doi.org/10.1093/bfgp/elad041) · Briefings in Functional Genomics | 조현병 전장 유전체 연관 분석(GWAS: 유전체 전체에서 질병과 관련된 유전 변이를 찾는 연구)은 위험 유전자 자리를 많이 찾았지만, 여러 단일염기다형성(SNP: 사람마다 다른 DNA 염기 하나의 차이)의 상호작용이 조현병 감수성에 어떻게 작용하는지는 분명하지 않다. 이 논문은 분자·세포 기능을 거치는 SNP 조합 효과를 탐색하려고, 정밀도가 다른 두 수준의 자료를 단계적으로 학습하는 딥러닝 기법 SLEM을 제안했다. 정밀하지만 양이 적은 여러 층의 실험 자료로 먼저 뼈대 네트워크를 만들고, 덜 정밀하지만 양이 많은 GWAS 자료로 중간 상호작용의 세기를 학습한다. 학습된 네트워크로 가능한 모든 SNP 조합이라는 다루기 어려울 만큼 넓은 공간에서 효과적인 SNP 상호작용을 찾을 수 있었고, 추출한 SNP 조합은 어떤 단일 SNP보다 정확도가 높았으며 독립 자료에서도 정확도를 유지했다. 학습된 네트워크는 SNP 조합이 분자·세포 상호작용을 거쳐 조현병 발병에 이르는 과정을 해석할 수 있게 한다.[^p8] | 1저자 Y. Jo(Yousang Jo), 마지막 저자 이도헌 (4명) |

## 교수와 전문 분야

이도헌 교수는 KAIST 바이오및뇌공학과 교수다. 누리집 교수 페이지는 현재 직책으로 KAIST 기획처장(Vice President, Office of Planning and Budget), 바이오및뇌공학과 교수, 공학생물학대학원 교수, 바이오정보시스템 연구실 책임자, 바이오시너지 연구센터(Bio-Synergy Research Center) 센터장을 적는다.[^prof] KAIST에서 전산학으로 학사(1990년), 석사(1992년), 박사(1995년) 학위를 받았고, 2002년부터 바이오및뇌공학과 교수로 있다.[^prof][^deptprof]

누리집 교수 페이지가 적는 경력은 국가과학기술연구회 이사(2023년–), 바이오헬스 데이터플랫폼협의체 공동위원장(2024년–), 한국합성생물학 발전협의회 융합분과장(2023년–), 국회미래연구원 이사(2025년–), 대한디지털치료학회 부회장(2021년–), KAIST 교무처장(2023–2024년), KAIST 100년 비전위원회 위원장(2021–2022년), 국가과학기술자문회의 위원(2020–2022년), 한국생명정보학회 회장(2019–2020년), 유전자동의보감 국책사업단장(2013–2022년)이다. 학술지 IEEE/ACM Transactions on Computational Biology and Bioinformatics의 부편집장(2025년–)과 ACM Transactions on Internet Technology의 부편집장(2001–2010년)을 맡았고, Stanford University 의과대학, Indiana University Bloomington, University of Texas at Austin, Translational Genomics Research Institute(TGen), 미국 국립보건원(NIH)에서 겸직·방문 교수나 연구원으로 지냈다.[^prof] 학과 교수 소개는 이 밖에 바이오및뇌공학과 학과장(2011–2014년), IBM-KAIST 바이오컴퓨팅 연구센터 센터장(2004년–), 정문술바이오정보전자센터 센터장(2019년–), 바이오정보시스템 국가지정연구실 책임교수(2005년–)를 적는다.[^deptprof]

학과 교수 소개는 수상 경력으로 온빛학술상(한국생명정보학회), IBM-Shared University Research Award, ACM International Workshop on Text Mining for Bioinformatics와 International Conference on Genome Informatics의 우수논문상, KAIST 공동연구상, KAIST 국제협력대상, 국회의정연수원 우수강의상을 연도 없이 적는다.[^deptprof] 연구실 소식은 교수가 2023년 7월 과학기술정보통신부 장관 표창을 받았다고 알렸고, 공적을 「디지털 가상인체기술을 개발하여 미국 FDA 임상 진입에 성공하는 등 천연물 바이오 분야의 혁신적 성과 창출에 기여」로 옮겼다. 2024년 2월에는 한국공학한림원 신입 일반회원 선정을, 2026년 2월에는 KAIST 개교 55주년 기념식의 비전 리더십상 수상을 알렸다.[^news]

전문 분야는 생물 데이터를 계산으로 분석하는 바이오정보학과 데이터마이닝이다.[^deptlist][^prof] 교수 페이지는 논문·특허 실적을 「Around 200 International Papers and 40 Technical Patents in Bioinformatics and Data Mining」으로 적는다.[^prof] 학과 교수 소개가 드는 대표 연구실적에는 유방암 전이를 네트워크로 분류한 연구(Molecular Systems Biology, 2007년), 여러 수준의 맥락 지향 방향성 연관을 통합해 약물 효과를 분석하는 CODA(Scientific Reports, 2017년), 천연 화합물의 약리 효과를 표현형 중심 네트워크 분석으로 찾은 연구(Scientific Reports, 2018년) 등이 있다.[^deptprof] 2021년 이후에는 위의 대표 논문처럼 네트워크 임베딩, 그래프 어텐션 오토인코더, 대조 학습 같은 기계학습 방법을 약물 표적·약물 재창출·질병 유전자 문제에 적용하는 연구를 이어 왔다.[^p1][^p3][^p6]

## 응용 분야

연구 페이지는 CODA 기반 방법이 복합 질환을 막고 치료할 신약과 기능성 식품 개발에 쓰인다고 적고, 합성생물학에서는 단백질이나 화학물질 같은 원하는 산물을 만드는 합성 경로 설계를 목표로 든다.[^research] 대표 논문들은 약물 부작용의 기전 이해와 예방(대표 논문 1), 파킨슨병의 새 약물 후보 찾기(대표 논문 4·5), 유방암 환자별 항암 표적과 병용 요법 후보 제안(대표 논문 7)을 응용으로 제시한다.[^p1][^p4][^p5][^p7] 2023년 7월 장관 표창의 공적 문구는 교수가 디지털 가상인체기술을 개발해 미국 FDA 임상 진입에 성공하는 등 천연물 바이오 분야의 성과에 기여했다고 적는다.[^news]

## 구성원

Members 페이지의 22명이다. 박사후연구원(Postdoctoral Researchers) 2명, 박사과정(Doctoral Students) 13명, 석사과정(Master Students) 7명이며, 카드는 한글·영문 이름과 분야 표기 한 줄만 적는다. 표의 연구 주제 칸은 그 분야 표기 그대로이고, 출신 전공처럼 적힌 것이 많다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| 김지은(Jieun Kim) | 박사후연구원 | Biomedical Science |  |
| 유승윤(Yu Seungyoon) | 박사후연구원 | Biological Science |  |
| 박주연(Jooyeon Park) | 박사과정 | Animal Biotechnology |  |
| 이남주(Namjoo Lee) | 박사과정 | Neuroscience |  |
| 권오현(Ohhyun Kwon) | 박사과정 | Biology |  |
| 김재홍(Jaehong Kim) | 박사과정 | Bio and Brain Engineering |  |
| 한재욱(Jaywook Han) | 박사과정 | Biology |  |
| 김한진(Hanjin Kim) | 박사과정 | Computer Science |  |
| 김서진(Seojin Kim) | 박사과정 | Bio and Brain Engineering |  |
| 한만영(Manyoung Han) | 박사과정 | Bio and Brain Engineering | 4, 5 |
| 김의연(Uiyun Kim) | 박사과정 | Computer Science |  |
| 이시윤(Siyun Lee) | 박사과정 | Biomedical Engineering |  |
| 김상원(Sangwon Kim) | 박사과정 | Systems Biology & Computer Science |  |
| 정연주(Yeonju Jeong) | 박사과정 | Computer Science |  |
| 이예지(Yeji Lee) | 박사과정 | Stem Cell Biology |  |
| 박지원(Jiwon Park) | 석사과정 | Life Science & Artificial Intelligence |  |
| 최민경(Minkyoung Choi) | 석사과정 | Chemical and Biomolecular Engineering |  |
| 안규찬(Gyuchan An) | 석사과정 | Bio and Brain Engineering & Computer Science |  |
| Jasmine King | 석사과정 | Biomedical & Electrical Engineering |  |
| 강민서(Minseo Kang) | 석사과정 | Integrative Bioscience and Biotechnology |  |
| 김상준(Sangjune Kim) | 석사과정 | Computer Engineering |  |
| 김성훈(Seonghun Kim) | 석사과정 | Life Science |  |

## 졸업생과 이전 구성원

Alumni 페이지의 진로 기관 카드에 적힌 73줄이다. 대학(University) 칸 25줄, 국립 연구기관·정부 기관(National Research Institutes and Government Offices) 칸 16줄, 기업(Enterprises) 칸 32줄이며, 같은 이름이 두 기관에 적힌 사람이 2명 있다(Hojung Nam, Kyungwook Lee). 진로 칸은 카드의 기관 이름과 사람 옆에 적힌 직위 그대로이고, 직위가 없는 줄은 기관 이름만 적었다. 페이지는 학위와 졸업 연도를 적지 않는다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Dokyun Na |  | Chungang university · Professor |
| Daewon Kim |  | Chungang university · Professor |
| Eunjung Lee |  | Harvard Medical school · Professor |
| Philhyun Lee |  | Harvard Medical school · Professor |
| Seunghyun Wang |  | Harvard Medical school · Postdoc |
| Hojung Nam |  | GIST · Professor |
| Yongdeuk Hwang |  | Suwon University · Professor |
| Jinmyung Jung |  | Suwon University · Professor |
| Honghee Won |  | Sunkyunkwan University · Professor |
| Junho Kim |  | Sunkyunkwan University · Professor |
| Sangwoo Kim |  | Yonsei University · Professor |
| Inho Park |  | Yonsei University · Professor |
| Hojung Nam |  | Yonsei University · Professor |
| Sohyun Hwang |  | Cha Medical University · Professor |
| Sungwon Jung |  | Gachon University · Professor |
| Seongwoon Hwang |  | Hongik University · Professor |
| Sunyong Yoo |  | Chonnam University · Professor |
| Sejoon Lee |  | Seoul National University Hospital · Professor |
| Jaegyun Jung |  | Seoul National University Hospital · Professor |
| Jaesub Park |  | Cambridge Stem Cell Institute · Postdoc |
| Hyeoncheol Jeong |  | Wellcome Sanger Institute · Postdoc |
| Junseok Park |  | Baylor College of Medicine · Assistant Professor |
| SunJae Lee |  | KAIST · Professor |
| Sangyeon Lee |  | Seoul St. Mary's Hospital · Professor |
| Jaejoon Choi |  | UNIST · Professor |
| Byungwook Lee |  | KRIBB · Senior Researcher |
| Hyojin Kang |  | KISTI · Researcher |
| Hyojung Paik |  | KISTI · Senior Researcher |
| Junhawk Lee |  | KISTI · Senior Researcher |
| Yonghoon Kim |  | KISTI · Researcher |
| Ali Zeeshan Ijaz |  | KISTI · Researcher |
| Thai Quang Tung |  | KISTI · Researcher |
| Jisung Park |  | KISTI · Researcher |
| Juhyun Jung |  | Suwon District Court · Judge |
| Minsoo Kim |  | KICOX |
| Sunghwa Bae |  | NIFDSE |
| Yousang Jo |  | KIOM · Senior Researcher |
| Suji Jo |  | KIAT |
| Taewoo Ryu |  | APEC climate center |
| Jongan Lee |  | RDA |
| Junhyuk Lee |  | IBS · Researcher |
| Jaehun Lee |  | Samsung Card |
| Suhyun Ha |  | Samsung Card |
| Moonshik Shin |  | Samsung Card |
| Mijin Kwon |  | Samsung Electronics |
| Gwangmin Kim |  | Samsung Electronics |
| Yeongrok Kim |  | Samsung Electronics |
| Kyungrin No |  | Moloco |
| Namhoon Kim |  | Microsoft |
| Kiryong Ha |  | Meta |
| Ryukwang Jung |  | Krafton |
| Hasun Ryu |  | Kakao Brain |
| Saehwan Lee |  | Upstage |
| Kwangmin Kim |  | LG AI |
| Soorin Yim |  | LG AI |
| Kyungwook Lee |  | LG AI |
| Hyundai Choi |  | LGE |
| Jueun Choi |  | LGE |
| Seockhyeon Moon |  | Coupang |
| Namjin Gu |  | Samjin |
| Dongjin Jang |  | AWS |
| Hyejin Kam |  | Dubu |
| Gyuil Cho |  | Deloitte |
| Seungsu Lee |  | NHN |
| Woochang Hwang |  | CardiaTec |
| Chungsoon Jeong |  | Doeat |
| Kyungwook Lee |  | Standigm |
| Minseon Hwang |  | Waycen |
| Yijin Kim |  | KB Insurance |
| Jiyeon Chun |  | WOORI Financial Capital |
| Seunghwan Jung |  | Hanmi Pharmaceutical |
| Docyong Kim |  | Spreading Scent Company |
| Yutae Kim |  | UX Factory |

## 최근 논문 목록 (2021–2026)

2021–2026년 논문 16편이다(2025년 3, 2024년 5, 2023년 1, 2022년 5, 2021년 2). Publications 페이지의 2021–2026년 25줄 가운데 의생명 수록 범위 밖의 9줄은 목록에 없다.[^pubs] 제목과 학술지 표기는 누리집 그대로이고, 누리집 목록에 저자가 없어 저자는 학술지·사전 공개본 서지 기록(Crossref)을 따랐다.[^cr]

- bioRxiv 사전 공개본 2편은 그렇게 표시했다. 2022년 「Intercellular CRISPR Screens …」는 같은 해 Frontiers in Immunology 논문과 같은 연구다.[^pubs][^cr]
- 2021년 「Integrated Network-Based Computational Analysis for Drug Development」는 책 「Recent Advances in Biological Network Analysis」의 한 장이다.[^pubs][^cr]
- 의생명 연구는 자연·공학과 직접 연계된 연구만 싣는 이 위키의 수록 범위에 따라 논문마다 초록으로 확인했다. 우울증 환자의 신체 활동과 자해 행동의 연관을 다룬 임상 코호트 연구(학술지 논문과 사전 공개본 2줄), 식물 추출물의 동물 효능 연구, 갑상선암 세포 사멸 기전 연구, 그리고 기존 분석 도구를 적용해 질병·치료 후보를 살핀 전통 의학 처방 분석(학술지 논문과 사전 공개본 2줄)·유방암 예후 집단 분석(같은 논문 2줄)·분자 도킹 후보 선별 연구는 싣지 않았다(사유는 근거 페이지).

**2025**

- Jaehun Jeon, Sangyeon Lee, Seongok Chae, Joo Hoon Lee, Hanjin Kim, Eun-Sil Yu, Hamin Na, Taejoon Kang, Hyung-Soon Park, Doheon Lee, Ki-Hun Jeong. "All-flexible chronoepifluidic nanoplasmonic patch for label-free metabolite profiling in sweat". *Nature Communications 16 (8017), 2025*.
- Yutae Kim, Doheon Lee. "Unsupervised cell line embedding using pairwise drug response correlation". *Computational and Structural Biotechnology Journal, 2025*.
- Kwansoo Kim, Manyoung Han, Doheon Lee. "InTiCAR: Network-based identification of significant inter-tissue communicators for autoimmune diseases". *Computational and Structural Biotechnology Journal 27, 333-345, 2025*.

**2024**

- Seunghwan Jung, Kwansoo Kim, Seunghyun Wang, Manyoung Han, Doheon Lee. "NaCTR: Natural product-derived compound-based drug discovery pipeline from traditional oriental medicine by search space reduction". *Computational and Structural Biotechnology Journal 23, 3869-3877, 2024*.
- Manyoung Han, Seunghwan Jung, Doheon Lee. "Drug repurposing for Parkinson’s disease by biological pathway based edge-weighted network proximity analysis". *Scientific Reports*.
- Seunghwan Jung, Seunghyun Wang, Doheon Lee. "CancerGATE: Prediction of cancer-driver genes using graph attention autoencoders". *Computers in Biology and Medicine*.
- Seunghyun Wang, Doheon Lee. "Community cohesion looseness in gene networks reveals individualized drug targets and resistance". *Briefings in Bioinformatics*.
- Yousang Jo, Maree J Webster, Sanghyeon Kim, Doheon Lee. "Interpretation of SNP combination effects on schizophrenia etiology based on stepwise deep learning with multi-precision data". *Briefings in Functional Genomics*.

**2023**

- Gwangmin Kim, Doheon Lee. "Reverse tracking from drug-induced transcriptomes through multilayer molecular networks reveals hidden drug targets". *Computers in Biology and Medicine*.

**2022**

- Jaesub Park, Sangyeon Lee, Kwansoo Kim, Jaegyun Jung, Doheon Lee. "Large-scale prediction of adverse drug reactions-related proteins with network embedding". *Bioinformatics*.
- Soorin Yim, Woochang Hwang, Namshik Han, Doheon Lee. "Computational Discovery of Cancer Immunotherapy Targets by Intercellular CRISPR Screens". *Frontiers in Immunology*.
- Sang-In Bae, Sangyeon Lee, Jae-Myeong Kwon, Hyun-Kyung Kim, Kyung-Won Jang, Doheon Lee, Ki-Hun Jeong. "Machine Learned Light Field Camera that Reads Facial Expression from High Contrast and Illumination Invariant 3D Facial Images". *Advanced Intelligent Systems*.
- Sangyeon Lee, Hanjin Kim, Doheon Lee. "Linearization Autoencoder: an autoencoder-based regression model with latent space linearization". *bioRxiv 사전 공개본, 2022*.
- Soorin Yim, Woochang Hwang, Namshik Han, Doheon Lee. "Intercellular CRISPR Screens Enhance the Discovery of Cancer Immunotherapy Targets". *bioRxiv 사전 공개본, 2022*.

**2021**

- Kiseong Kim, Sunyong Yoo, Sangyeon Lee, Doheon Lee, Kwang-Hyung Lee. "Network Analysis to Identify the Risk of Epidemic Spreading". *Applied Sciences*.
- Mijin Kwon, Soorin Yim, Gwangmin Kim, Doheon Lee. "Integrated Network-Based Computational Analysis for Drug Development". *Recent Advances in Biological Network Analysis*.

## 특허

Patents 페이지 31건 가운데 연도가 2021년 이후인 3건이다. 페이지는 특허마다 제목, 연도, 상태(출원·등록)만 적고 번호와 날짜는 적지 않는다. 2021년 등록 1건은 연도만 있어 2021년 10월 13일 전에 등록되었을 수도 있다.[^patents]

- 2024 · 효소 반응 데이터 생성 방법 및 장치 (상태 출원)
- 2023 · 해석가능한 심층학습 모델 학습방법 및 장치, 진단 방법 및 장치 (상태 출원)
- 2021 · 딥러닝기반 화합물 의약효과 예측방법 (상태 등록)

## 수상

News 페이지의 수상 소식 3건이다. 교수 수상 2건과 학생 5명의 경진대회 수상 1건이며, 제목은 페이지 표기 그대로이고 괄호의 수상자는 글 본문이 적은 이름이다.[^news]

- 2026-02-12 · 이도헌 교수님 KAIST 개교 55주년 기념식 '비전 리더십상' 수상
- 2023-09-08 · 2023 K-ium 의료 인공지능 경진대회 최우수상(1위) 수상 (수상자 김서진, 한성주, 김세현, 정다연, 채윤병)
- 2023-07-19 · 과학기술정보통신부 장관 표창 수상 (수상자 이도헌 교수)

## 소식

News 페이지의 글 27건(2023년 6월–2026년 9월) 가운데 수상 소식 3건, 연구실 행사·교류 글 17건, 졸업생의 진로·수상 소식 2건을 뺀 5건이다. 교수의 위촉·선정 소식 3건과, 연구실 논문을 소개한 글 2건이다. 제목은 페이지 표기 그대로다.[^news]

- 2025-03-04 · 이도헌 교수님, 국회미래연구원 제3기 이사 위촉
- 2024-04-23 · 유전자 커뮤니티 결속력 측정 기술 COSINET 개발
- 2024-02-01 · 이도헌 교수님 한국공학한림원 선정
- 2023-09-28 · '증상 억제만 가능했던 조현병, AI로 치료 실마리 찾았다'
- 2023-09-20 · 이도헌 교수님 한국생명공학연구원(KRIBB) 과학자문위원 위촉

## 연락과 위치

- 위치: Room 503, E16 ChungMoonSoul B/D(Contact us 페이지), 교수실 E16 1111호(학과 교수 소개)[^contact][^deptprof]
- 주소: 291 Daehak-ro, Yuseong-gu, Daejeon, Republic of Korea(누리집 꼬리말은 CMS Building (E16), KAIST로 적는다)[^contact][^home]
- 전화: 042-350-4353, 4356, 5356(연구실), 팩스 042-350-8680, 교수 전화 042-350-4316[^home][^deptlist]
- 이메일: 교수 dhlee@kaist.ac.kr, 연구실 연락 sjkim@biosoft.kaist.ac.kr(Contact us 페이지)[^home][^deptlist][^contact]
[^p1]: J. Park 외, D. Lee, Bioinformatics 39, btac843 (온라인 2022-12-29). <https://doi.org/10.1093/bioinformatics/btac843> 초록 기준.
[^p2]: G. Kim, D. Lee, Computers in Biology and Medicine 158, 106881 (2023). <https://doi.org/10.1016/j.compbiomed.2023.106881> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: Y. Kim, D. Lee, Computational and Structural Biotechnology Journal 27, 2566-2573 (온라인 2025-06-12). <https://doi.org/10.1016/j.csbj.2025.06.018> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: M. Han, S. Jung, D. Lee, Scientific Reports 14, 21258 (온라인 2024-09-11). <https://doi.org/10.1038/s41598-024-71922-1> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: S. Jung 외, D. Lee, Computational and Structural Biotechnology Journal 23, 3869-3877 (온라인 2024-10-29). <https://doi.org/10.1016/j.csbj.2024.10.035> 초록 기준.
[^p6]: S. Jung, S. Wang, D. Lee, Computers in Biology and Medicine 176, 108568 (2024). <https://doi.org/10.1016/j.compbiomed.2024.108568> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: S. Wang, D. Lee, Briefings in Bioinformatics 25, bbae175 (온라인 2024-04-15). <https://doi.org/10.1093/bib/bbae175> 초록 기준.
[^p8]: Y. Jo, M. J. Webster, S. Kim, D. Lee, Briefings in Functional Genomics 23, 663-671 (온라인 2023-09-21). <https://doi.org/10.1093/bfgp/elad041> 초록 기준.
[^inticar]: K. Kim, M. Han, D. Lee, Computational and Structural Biotechnology Journal 27, 333-345 (온라인 2025-01-13). <https://doi.org/10.1016/j.csbj.2025.01.003> 초록 기준(Semantic Scholar 등록 초록).
[^crispr]: S. Yim, W. Hwang, N. Han, D. Lee, Frontiers in Immunology 13, 884561 (온라인 2022-05-16). <https://doi.org/10.3389/fimmu.2022.884561> 초록 기준.
[^sers]: J. Jeon 외, K.-H. Jeong, Nature Communications 16, 8017 (온라인 2025-08-27). <https://doi.org/10.1038/s41467-025-63510-2> 초록 기준.
[^lfc]: S.-I. Bae 외, K.-H. Jeong, Advanced Intelligent Systems 4, 2100182 (온라인 2021-12-16). <https://doi.org/10.1002/aisy.202100182> 초록 기준.
[^epi]: K. Kim, S. Yoo, S. Lee, D. Lee, K.-H. Lee, Applied Sciences 11, 2997 (온라인 2021-03-26). <https://doi.org/10.3390/app11072997> 초록 기준.
[^coda]: M. Kwon, S. Yim, G. Kim, D. Lee, 「Integrated Network-Based Computational Analysis for Drug Development」, Recent Advances in Biological Network Analysis (Springer, 온라인 2021-01-14). <https://doi.org/10.1007/978-3-030-57173-3_8> 출판사 책 페이지의 초록 기준.
[^home]: 연구실 누리집 첫 화면 <https://biosoft.kaist.ac.kr/> (연구실 소개, 연구·교육 주제, 교수 이메일, 꼬리말의 주소·전화, 2026-10-23 열람)
[^research]: 연구실 누리집 Research 페이지 <https://biosoft.kaist.ac.kr/research.html> (Big Data and AI-Based Drug Discovery, AI for Synthetic Biology, 2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <https://biosoft.kaist.ac.kr/dhlee.html> (현재 직책, 관심 분야, 학력, 경력, 논문·특허 실적, 2026-10-23 열람)
[^members]: 연구실 누리집 Members 페이지 <https://biosoft.kaist.ac.kr/members.html> (화면이 불러오는 같은 누리집의 자료 <https://biosoft.kaist.ac.kr/files/data/members.json>, 2026-10-23 열람)
[^alumni]: 연구실 누리집 Alumni 페이지 <https://biosoft.kaist.ac.kr/alumni.html> (화면이 불러오는 같은 누리집의 자료 <https://biosoft.kaist.ac.kr/files/data/alumni.json>, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publications 페이지 <https://biosoft.kaist.ac.kr/publications.html> (화면이 불러오는 같은 누리집의 자료 <https://biosoft.kaist.ac.kr/files/data/papers.json>; 목록 범위는 근거 페이지, 2026-10-23 열람)
[^patents]: 연구실 누리집 Patents 페이지 <https://biosoft.kaist.ac.kr/patents.html> (화면이 불러오는 같은 누리집의 자료 <https://biosoft.kaist.ac.kr/files/data/patents.json>, 2026-10-23 열람)
[^news]: 연구실 누리집 News 페이지 <https://biosoft.kaist.ac.kr/news.html> (화면이 불러오는 같은 누리집의 자료 <https://biosoft.kaist.ac.kr/files/data/news.json>의 글 27건, 2026-10-23 열람)
[^contact]: 연구실 누리집 Contact us 페이지 <https://biosoft.kaist.ac.kr/contact.html> (연구실 위치·주소·연락 이메일, 2026-10-23 열람)
[^resources]: 연구실 누리집 Resources 페이지 <https://biosoft.kaist.ac.kr/resources.html> (공개 분석 도구, 생물 데이터베이스, 2026-10-23 열람)
[^cr]: 학술지·사전 공개본 서지 기록(Crossref) <https://api.crossref.org/> (2021–2026년 목록 논문의 저자·DOI·출판일, 제목 검색 2026-10-23 조회)
[^deptlist]: KAIST 바이오및뇌공학과 교수진 목록 <https://bioeng.kaist.ac.kr/index.php?mid=bio_03_01> (이도헌 교수 항목: 직위, 박사 학위, 연구분야, 연구실, 전화, 이메일, 2026-10-23 열람)
[^deptprof]: KAIST 바이오및뇌공학과 교수 소개(이도헌) <https://bioeng.kaist.ac.kr/index.php?document_srl=6840&mid=bio_03_01> (직위, 최종학위, 연구분야, 경력, 대외활동, 수상 경력, 대표 연구실적, 2026-10-23 열람)

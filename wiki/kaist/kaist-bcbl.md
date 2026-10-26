# 단백질생물정보학 연구실 (Bioinformatics and Computational Biology Lab, BCBL)

**KAIST 바이오및뇌공학과 · 김동섭 교수**

- 분야: 단백질 구조·기능과 생체분자 상호작용의 계산 예측, 계산 단백질·항체 설계, 면역 단백질 결합 예측, 계산 신약 개발과 화학물질 독성 예측, 3차원 유전체 구조와 유전자 발현 자료의 딥러닝 분석
- 대분야: 컴퓨팅·AI, 기초생명·생물물리
- 태그: 구조생물학[^sb][^bbs2022][^p1], 그래프 기계학습·지식 그래프[^p1][^p4][^p6], 과학·공학 AI[^bbs2022][^p2][^p7], 바이오정보학·계산생물학[^labintro], AI 신약 개발[^dd], 단일 세포·공간 오믹스[^p8]
- 홈페이지: <https://sites.google.com/view/kaist-bcbl>
- 근거와 출처: [BCBL 근거 페이지](kaist-bcbl-sources.md)

> 물리·화학·계산의 원리로 단백질 같은 생체분자의 구조와 기능, 상호작용을 예측하는 계산 방법을 만들고, 이를 단백질 설계와 신약 개발에 쓰는 생물정보학 연구실이다.[^labintro][^sb][^pd][^dd] 2021–2026년 대표 논문은 그래프 신경망과 딥러닝으로 단백질 도킹 모델을 평가하고, 변이의 해로움과 B세포 면역우세, 약물-표적 결합을 예측하며, 항체를 설계하고, 화학물질의 유해 결과 경로를 잇는 네트워크를 만들고, 염색질 고리와 단일세포 유전자 발현을 예측하는 방법을 다룬다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 무엇을 연구하나

연구실은 KAIST 바이오및뇌공학과 김동섭 교수가 이끄는 연구실이다.[^prof][^deptprof] 누리집은 첫 화면에 이름을 Bioinformatics and Computational Biology Lab으로 적고 사이트 이름을 BCBL @ KAIST로 쓴다.[^home] 학과 교수 소개와 학과 연구실 목록은 국문 이름을 「단백질생물정보학 연구실」로 적는다.[^deptprof][^labs] 학과 연구실 소개는 연구실의 목표를 물리·화학·계산의 원리로 분자 수준의 생물 시스템 전반을 연구해 그 시스템을 이해하고 수학·계산 모형을 개발하는 것으로 적는다. 이렇게 하면 예측이 가능한 생체 시스템 모형을 세울 수 있고, 그 모형을 신약 개발과 새로운 진단 같은 응용에 쓸 수 있다고 밝힌다.[^labintro] 주요 연구 분야로는 단백질 구조와 기능의 예측·분석, 단백질 상호작용의 계산 연구, 계산 단백질 설계, 계산 신약 개발을 든다.[^labintro]

교수는 2020년 학과 소식지 인터뷰에서 생물정보학을 생물학과 의학의 여러 문제를 풀려고 생명·의료 정보로 여러 분석 방법과 전산 예측 모델을 개발하는 분야로 설명했다.[^bbs2020] 2022년 학과 소식지 인터뷰 「구조생물학과 AI」에서는 단백질이 아미노산 서열에 따라 여러 구조로 접히고 그 구조가 기능과 깊이 관련되며, 엑스선이나 핵자기공명 같은 실험 방법 말고도 인공지능으로 아미노산 서열에서 구조를 예측할 수 있다고 설명했다. 자신의 관심은 구조 예측을 넘어, 특정 단백질이 다른 물질이나 분자와 결합할 수 있는지, 결합한다면 얼마나 강하게 결합하는지 같은 단백질의 기능을 이해하는 데 있다고 밝혔다.[^bbs2022] 지금 연구할 가치가 있는 분야로는 여러 단백질이 모여 이룬 단백질 복합체(protein complex)의 구조 예측과 단백질과 다른 분자 사이의 결합 세기 예측을 들었다. 이런 분야는 실험으로 구조를 밝히기 어려워 인공지능 모델을 만들 데이터가 부족하므로, 연구실에서는 단백질 서열 같은 여러 출처의 데이터를 가져와 모델을 개발하고 시험한다고 설명했다.[^bbs2022] 원하는 기능을 하는 단백질이 어떤 구조를 가져야 하고 그 구조를 가지려면 어떤 아미노산 서열이어야 하는지를 계산하는 단백질 디자인, 그리고 질병을 일으키는 단백질에 강하게 결합해 그 단백질을 억제하는 저분자 화합물이나 자연계에 없는 새 단백질의 설계에도 인공지능을 쓸 수 있다고 말했다.[^bbs2022]

누리집 Research 메뉴는 연구를 세 갈래로 나눈다. 구조 생물정보학(Structural Bioinformatics) 페이지는 상동성 모델링(진화적으로 관련된 단백질 가운데 구조가 밝혀진 것을 본보기로 삼아 단백질의 3차원 구조를 세우는 방법), 루프 모델링, 분자 동역학(원자 사이에 작용하는 힘을 계산해 원자들의 시간에 따른 움직임을 따라가는 시뮬레이션) 같은 계산 방법으로 생체분자의 구조와 기능을 예측하는 일, 단백질-단백질·단백질-DNA·단백질-RNA·단백질-약물 같은 생물학적 상호작용의 결합 친화도(두 분자가 서로 붙는 세기)와 결합 구조를 대규모 생물 빅데이터와 여러 도구·시뮬레이션으로 예측하는 일, 단백질 모델링과 단백질-단백질 도킹(두 분자가 맞물리는 위치와 방향을 컴퓨터로 찾는 계산), 분자 동역학 시뮬레이션으로 질병을 일으키는 돌연변이를 예측하는 일, 차세대 염기서열 분석(NGS, DNA·RNA의 염기서열을 한꺼번에 대량으로 읽는 기술) 실험 자료와 여러 시뮬레이션 도구로 3차원 유전체 구조와 그 기능적 결과를 예측하는 일을 적는다.[^sb] 계산 단백질 설계(Computational Protein Design) 페이지는 이미 밝혀진 단백질의 데이터 분석과 새로 설계한 단백질 모델의 계산 시뮬레이션으로 새로운 구조와 기능을 가진 단백질을 설계하는 일, 특정 문제를 위한 도구·소프트웨어부터 단백질 설계와 평가의 전체 파이프라인까지 새 단백질 설계 알고리즘을 개발하는 일, 치료용 단백질 의약품을 설계·개발하는 일을 적는다. 특히 LRR 단백질을 구조의 뼈대(scaffold)로 쓰고 항체와 비슷한 기능을 하는 「리피바디(repebody)」 설계를 전문으로 한다고 밝힌다.[^pd] 계산 신약 개발(Computational Drug Discovery) 페이지는 계산 약물 설계·개발을 위한 화학정보학(cheminformatics, 화학 물질의 구조와 성질 자료를 컴퓨터로 저장·분석하는 분야)을 들고, 최근에는 약물 설계와 검증 과정을 자동화하는 딥러닝 알고리즘을 개발한다고 적는다. 정교한 약물 설계와 약물 재창출(이미 개발된 약을 다른 질병에 쓰는 일)에 필요한 약물 표적 예측 도구와 서버도 개발한다고 적는다.[^dd]

누리집 Server and Software 페이지는 연구실이 공개한 서버와 소프트웨어 11가지를 관련 논문(2010–2025년)과 함께 올린다.[^sw] 단백질과 면역 쪽으로는 B세포(항체를 만드는 면역세포) 면역우세(항원의 여러 부분 가운데 일부에 면역 반응이 몰리는 현상)의 위계 양상을 밝히는 BIDpred, 돌연변이 효과 예측기 MTBAN, 펩타이드와 MHC 1형(class I) 분자의 결합 예측 모델, 결합 단백질 뼈대 라이브러리 LibBP, 서열로 키나아제별 인산화 자리를 예측하는 PostMod가 있다. 약물 쪽으로는 강화학습과 도킹으로 분자를 최적화하는 MORLD, 역도킹으로 약물 표적을 찾는 CRDS, 키나아제의 약물 내성 돌연변이를 분자 도킹으로 평가하는 KRDS, 랜덤 포레스트 기반 표적 탐색 서버 RF-QSAR가 있고, 유전체 쪽으로는 3차원 유전체 상호작용 뷰어·데이터베이스 3DIV와 히스톤 변형 양상으로 기능별 유전자 조절을 분석한 ImpoHis가 있다.[^sw]

2021–2026년 대표 논문은 네 갈래로 묶인다. 첫째 갈래는 **단백질 구조와 상호작용 예측**이다. 대표 논문에서는 컴퓨터로 단백질들이 맞물리는 모양을 맞춰 본 도킹 모델 가운데 실제 구조에 가까운 모델을 고르려고, 3차원 분자 구조 모델링에서 성과를 보인 등변 그래프 신경망 GVP-GNN을 바탕으로 단백질-단백질 도킹 모델의 점수를 매기는 그래프 신경망 방법 G-RANK를 만들었다.[^p1] 한 단백질과 진화적으로 관련된 서열만으로 학습하는 심층 생성 모델에 지식 증류(먼저 학습한 모델의 예측을 다른 모델이 배우게 하는 학습 기법)를 적용해 단백질 변이가 해로운지를 예측하는 MTBAN도 만들고 웹서버로 공개했다.[^p2] 최근 논문 목록에는 그래프 합성곱 신경망으로 단백질-리간드(생체 분자에 결합해 복합체를 이루는 물질) 결합 친화도를 예측하는 모델(PLOS ONE, 2021)도 있다.[^pubs]

둘째 갈래는 **항체·면역 단백질의 설계와 예측**이다. 대표 논문에서는 항체가 항원과 주로 맞닿아 결합하는 부분인 상보성 결정 부위(CDR)를 설계하는 모델 AbFlex를 만들었는데, 항체-항원 복합체 구조 자료가 부족한 문제를 데이터 효율이 높은 등변 그래프 신경망과 CDR을 유연하게 정의하는 데이터 증강으로 풀었다.[^p3] 백신 설계에 중요한 B세포 면역우세의 특성을 통계로 찾고, 그 특성을 단백질 언어 모델의 임베딩과 그래프 어텐션 네트워크로 학습해 면역우세 점수를 예측하는 BIDpred도 만들었다.[^p4] 최근 논문 목록에는 짝지은 두 사슬의 T세포 수용체(TCR) 서열 자료로 TCR과 항원결정부위(항체나 면역세포 수용체가 알아보고 결합하는 항원의 부분)의 상호작용을 예측하는 TSpred(Bioinformatics, 2024)와, 항원결정부위가 공간에서 모여 있는 성질을 그래프 어텐션 네트워크로 잡아 B세포 항원결정부위를 예측하는 연구(Scientific Reports, 2024)도 있다.[^pubs]

셋째 갈래는 **계산 신약 개발과 독성 예측**이다. 대표 논문에서는 표적 단백질과 분자의 결합을 예측할 때, 표적에 결합하는 분자들의 화학적 유사성으로 비슷한 표적끼리 묶어 함께 학습시키고 단일 작업 모델의 예측을 길잡이로 삼는 지식 증류를 더한 다중 작업 학습(여러 과제를 한 모델로 함께 학습하는 기계학습 방법) 방식을 제안했다.[^p5] 2026년 논문에서는 화학물질-단백질 상호작용, 단백질-단백질 상호작용, 유전자 온톨로지, 유해 결과 경로(AOP, 화학물질 노출이 분자 수준의 첫 사건과 핵심 사건들을 거쳐 해로운 결과로 이어지는 과정을 정리한 모형) 자료를 여러 층으로 합친 네트워크 AOP Network Box를 만들어, 화학물질과 관련된 AOP를 찾고 화학물질·생체 분자·사건 사이의 알려지지 않았던 관계를 발견하도록 했다.[^p6] 최근 논문 목록에는 신약 개발에 네트워크 연결 예측(link prediction, 네트워크에서 아직 이어지지 않은 두 점 사이에 연결이 생길 가능성을 추정하는 방법)을 적용한 연구를 개관한 글(Expert Opinion on Drug Discovery, 2024)과, 유전체 자료와 분자 자료를 합쳐 Klebsiella pneumoniae의 항균제 최소 억제 농도를 예측하는 연구(Scientific Reports, 2024)도 있다.[^pubs]

넷째 갈래는 **유전체 구조와 유전자 발현 자료의 계산 분석**이다. 구조 생물정보학 페이지는 차세대 염기서열 분석 실험 자료와 시뮬레이션 도구로 3차원 유전체 구조와 그 기능적 결과를 예측한다고 적고,[^sb] 학과 연구실 소개는 실험 그룹과 함께 차세대 염기서열 분석 자료로 후성유전체(DNA 염기서열을 바꾸지 않으면서 유전자 발현을 조절하는 DNA·히스톤의 화학적 표지와 염색질 상태 전체)를 연구하는 계산 도구를 개발하는 계산 후성유전체학(Computational Epigenomics)도 연구 분야로 든다.[^labintro] 대표 논문에서는 전사인자 결합 자료 없이 조직별 후성유전체 자료로 조직마다 다른 염색질 고리(DNA와 단백질의 복합체인 염색질이 접혀, DNA 위에서 떨어진 두 자리가 공간에서 맞닿아 생긴 고리 구조)를 예측하는 딥러닝 모델 DeepLUCIA를 만들었다.[^p7] 2026년 논문에서는 측정 시점이 적고 간격이 고르지 않은 단일세포 유전자 발현 자료(세포 하나하나에서 따로 잰 유전자 발현 자료)로 측정하지 않은 시점의 유전자 발현을 예측하는 언어 모델 기반 틀 scMix를 만들었다. RWKV 구조의 시간 감쇠 장치로 시간에 따른 의존성을 모델링하고, 측정하지 않은 시점을 건너뛰는 장치로 오차가 쌓이는 문제를 줄였다.[^p8]

## 주요 연구 주제

### 1. 단백질 구조와 상호작용 예측

단백질-단백질 도킹 모델의 점수 매기기(G-RANK), 단백질 변이의 해로움 예측(MTBAN), 상동성 모델링과 분자 동역학으로 생체분자의 구조·기능과 결합을 예측하는 계산 방법.[^p1][^p2][^sb]

### 2. 항체·면역 단백질의 설계와 예측

항체 상보성 결정 부위 설계(AbFlex), B세포 면역우세 예측(BIDpred), 리피바디 같은 치료용 단백질의 계산 설계.[^p3][^p4][^pd]

### 3. 계산 신약 개발과 독성 예측

다중 작업 학습으로 약물-표적 결합 예측, 화학물질과 유해 결과 경로를 잇는 다층 네트워크(AOP Network Box), 약물 표적 예측 도구와 서버.[^p5][^p6][^dd]

### 4. 유전체 구조와 유전자 발현 자료의 계산 분석

조직별 염색질 고리 예측(DeepLUCIA), 단일세포 유전자 발현의 시간 변화 예측(scMix), 3차원 유전체 구조 예측.[^p7][^p8][^sb]

## 대표 논문

랩 Publications 페이지의 2021–2026년 논문 가운데 김동섭 교수가 마지막 저자인 학술지 논문을 네 연구 갈래에서 두 편씩 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2023 | [G-RANK: an equivariant graph neural network for the scoring of protein–protein docking models](https://doi.org/10.1093/bioadv/vbad011) · Bioinformatics Advances | 단백질 복합체의 구조 예측은 생명공학의 여러 응용에 중요하고, 널리 쓰이는 예측 방법이 계산 도킹이다. 단백질-단백질 도킹 모델의 점수를 매기는 도구가 많이 개발됐지만, 구조를 모르는 단백질 복합체에서 실제 구조에 가까운 모델을 정확히 골라내는 일은 여전히 어렵다. 등변 그래프 신경망의 한 종류로 여러 3차원 분자 구조 모델링 과제에서 성과를 보인 GVP-GNN(geometric vector perceptron–graph neural network)을 바탕으로, 단백질-단백질 도킹 모델의 점수를 매기는 방법 G-RANK를 내놓았다. 서로 다른 두 시험 자료로 평가했을 때 최고 수준(state-of-the-art)의 점수 함수들과 비슷하거나 더 나은 성능을 보였고, 소스 코드를 공개했다.[^p1] | 1저자 H. Y. Kim, 마지막 저자 김동섭 |
| 2 | 2021 | [An enhanced variant effect predictor based on a deep generative model and the Born-Again Networks](https://doi.org/10.1038/s41598-021-98693-3) · Scientific Reports | 사람 유전 질환 연구에는 정확하고 믿을 만한 변이 효과 예측 도구가 중요하다. 많은 예측기가 개발됐지만 상당수가 데이터 순환성(학습에 쓴 자료와 평가에 쓰는 자료가 서로 얽히는 문제)을 안고 있다. 변이의 해로움을 예측하는 방법 MTBAN(Mutation effect predictor using the Temporal convolutional network and the Born-Again Networks)을 제시했다. 앞서 개발한 심층 자기회귀 생성 모델(서열의 앞부분으로 다음 자리를 차례로 예측하며 서열의 확률을 배우는 생성 모델) mutationTCN에 지식 증류 기법의 한 형태인 Born-Again Networks(BAN)를 적용해 변이 효과 예측 성능을 높였다. 모델은 완전한 비지도 학습(정답 표시 없이 자료만으로 학습하는 방법) 방식이고 한 단백질과 진화적으로 관련된 서열만으로 학습하므로, 지도 학습(정답이 표시된 자료로 학습하는 방법) 예측기에 흔한 데이터 순환성 문제를 겪지 않는다. 해로운 사람 단백질 변이와 무해한 변이로 이뤄진 시험 자료에서 잘 알려진 다른 변이 효과 예측기들과 비교해 뛰어난 예측 능력을 보였고, 누구나 쓸 수 있는 웹서버를 공개했다.[^p2] | 1저자 H. Y. Kim, 마지막 저자 김동섭 |
| 3 | 2024 | [AbFlex: designing antibody complementarity determining regions with flexible CDR definition](https://doi.org/10.1093/bioinformatics/btae122) · Bioinformatics | 항체는 외부 병원체에 맞서 면역계가 만드는 단백질이고, 항원에 특이적으로 결합하는 항체를 설계하는 일은 항체 치료제 개발의 핵심 단계다. 항체의 상보성 결정 부위(CDR)가 표적 항원과의 결합을 주로 맡으므로, CDR은 항원을 알아보도록 설계해야 한다. 항체 설계 모델 AbFlex를 개발했고, 구조 예측 정확도와 아미노산 복원율(설계한 서열의 아미노산이 원래 서열과 일치하는 비율)에서 최고 수준(state-of-the-art)의 성능을 보였다. 새로 설계한 항체 모델 가운데 >38%는 원래 항체(wild type)보다 항원과의 결합 에너지가 나은 것으로 추정됐다. 항체-항원 복합체 구조 자료가 부족한 어려움을 넘으려고 두 전략을 썼다. 하나는 데이터 효율이 더 높은 등변 그래프 신경망 모델을 쓰는 것이고, 더 중요한 다른 하나는 CDR을 유연하게 정의하는 새 데이터 증강 전략으로, 이 전략이 CDR 예측 모델의 성능을 크게 높였다.[^p3] | 1저자 W. Jeon, 마지막 저자 김동섭 |
| 4 | 2025 | [BIDpred: unraveling B cell Immunodominance hierarchical pattern using statistical feature discovery and deep learning prediction](https://doi.org/10.3389/fimmu.2025.1646946) · Frontiers in Immunology | B세포 면역우세에 대한 지식은 효과적인 면역 반응을 끌어낼 백신을 설계하는 데 중요하지만, 면역우세가 얼마나 흔하고 어떤 특성을 가지는지는 잘 알려져 있지 않다. 새로운 데이터 처리 방법으로 면역우세 점수를 도입하고, 잔기(단백질 사슬을 이루는 아미노산 하나하나)와 패치(이웃한 잔기들의 묶음) 수준에서 B세포 면역우세의 통계적으로 유의한 특성을 찾았다. 이를 바탕으로 단백질 언어 모델 임베딩과 그래프 어텐션 네트워크로 새로 찾은 특성을 학습해 면역우세 점수를 예측하는 BIDpred(B cell ImmunoDominance predictor)를 개발했다. BIDpred는 면역우세 점수 예측에서 기존 방법들보다 나은 성능을 보였고, 일반적인 B세포 항원결정부위 예측에서도 최고 수준 방법들과 견줄 만한 정확도를 유지했다. 저자들은 B세포 면역우세 양상을 체계적으로 분석하고 예측한 첫 연구로 본다.[^p4] | 1저자 S. Choi, 마지막 저자 김동섭 |
| 5 | 2022 | [Prediction of drug–target interactions through multi-task learning](https://doi.org/10.1038/s41598-022-23203-y) · Scientific Reports | 신약 개발에서는 표적 단백질과 분자의 결합을 알아내는 일이 중요하다. 다중 작업 학습은 과제마다 정보가 적을 때 과제 사이에 지식을 나누려고 도입됐지만, 때로 전체 성능을 떨어뜨리거나 과제별 성능 사이에 맞바꿈을 낳는다. 그룹 선택과 지식 증류로 평균 성능을 높이면서 개별 과제의 성능 저하도 최소로 줄이는 일반적인 다중 작업 학습 방식을 제안했다. 그룹은 표적마다 결합하는 리간드 집합 사이의 화학적 유사성으로 고르고, 같은 그룹의 비슷한 표적을 함께 학습시켰다. 학습 중에는 교사 어닐링(teacher annealing, 교사 모델의 예측과 실제 정답을 섞는 비율을 학습 중에 바꿔 가는 방법)을 곁들인 지식 증류를 적용해, 다중 작업 모델이 단일 작업 모델의 예측을 길잡이로 삼게 했다. 그 결과 단일 작업 학습과 기존 다중 작업 학습보다 평균 성능이 높았다. 추가 분석에서 다중 작업 학습은 성능이 낮은 과제에 특히 효과적이었고, 지식 증류는 다중 작업 학습에서 개별 과제의 성능 저하를 피하는 데 도움이 됐다.[^p5] | 1저자 C. Moon, 마지막 저자 김동섭 |
| 6 | 2026 | [AOP Network Box: An Integrative Framework for Bridging Adverse Outcome Pathways and Biological Networks](https://doi.org/10.1021/acs.chemrestox.6c00041) · Chemical Research in Toxicology | 유해 결과 경로(AOP)는 화학물질 노출을 분자 개시 사건(MIE)과 핵심 사건(KE)을 거쳐 유해 결과(AO)로 잇는, 생물학적 기전에 바탕을 둔 모형이다. 그런데 이미 알려진 AOP와 연관된 화학물질이나 생체 분자와 사건 사이의 연관 같은 AOP 자료에는 뚜렷한 빈틈이 있다. 이를 풀려고 화학물질-단백질 상호작용(CPI), 단백질-단백질 상호작용(PPI), 유전자 온톨로지(GO), AOP 네트워크 자료를 합친 다층 네트워크 AOP Network Box를 개발했다. 이 통합 자료로 화학물질과 연관된 AOP를 찾고, 화학물질·생체 분자·사건 사이에 알려지지 않았던 관계를 발견할 수 있어 화학물질이 유해 결과를 낳는 기전을 더 깊이 이해하게 돕는다. 웹 플랫폼으로 누구나 쓸 수 있게 공개했다.[^p6] | 1저자 M. Na, 마지막 저자 김동섭 |
| 7 | 2022 | [DeepLUCIA: predicting tissue-specific chromatin loops using Deep Learning-based Universal Chromatin Interaction Annotator](https://doi.org/10.1093/bioinformatics/btac373) · Bioinformatics | 유전자 조절에서 염색질 고리가 중요하다는 점은 널리 받아들여진다. 염색질 고리를 예측하는 방법은 주로 전사인자(TF) 결합에 의존하는 방법과 유전체 변이에 바탕을 둔 방법 두 가지인데, 어느 쪽도 사람 조직의 유전자 조절을 충분히 이해하게 해 주지 못한다. 이를 풀려고 딥러닝 기반 염색질 고리 예측 모델 DeepLUCIA(Deep Learning-based Universal Chromatin Interaction Annotator)를 개발했다. DeepLUCIA는 기존 TF 결합 의존 방법들이 결정적으로 기대는 TF 결합 자료를 쓰지 않는데도 그 방법들과 견줄 만한 예측 정확도를 보였다. 더 중요하게는 유전체 변이 기반 방법이 다루지 못하는 조직별 후성유전체 자료로 조직별 염색질 고리를 예측할 수 있다. 브루가다 증후군, COVID-19 중증도, 나이 관련 황반변성을 대상으로 한 전장 유전체 연관 분석(GWAS, 유전체 전체의 변이와 형질 사이의 연관을 찾는 분석)에서 찾은 단일 염기 다형성(SNP, 같은 종의 개체마다 다른 DNA 염기 한 개의 차이)의 새 표적 유전자 몇 개를 예측해 쓸모를 보였다.[^p7] | 1저자 D. Yang, 마지막 저자 김동섭 |
| 8 | 2026 | [scMix: learning temporal dynamics of gene expression under irregular time intervals](https://doi.org/10.1093/bioinformatics/btag080) · Bioinformatics | 시간에 따른 유전자 발현을 이해하는 일은 세포의 발달과 분화 연구의 기본이다. 실제로 시간에 따라 잰 단일세포 자료는 측정 시점이 적고 그 간격이 고르지 않은 경우가 많아, 실험 조건 때문에 관측 사이의 간격이 불규칙해진다. 기존 방법은 시점을 하나씩 차례로 예측하면서도 시간 간격을 명시적으로 모델링하는 장치가 없어 오차가 쌓인다. 여러 과거 시점에서 예측할 수 있는, 언어 모델 기반의 단일세포 유전자 발현 예측 틀 scMix를 내놓았다. RWKV(Receptance Weighted Key Value) 구조 위에 세우고 그 시간 감쇠 장치로 시간에 따른 의존성을 모델링했다. 측정하지 않은 시점을 건너뛰게 하는 델타 시간 장치로 오차 누적을 줄이고 견고성을 높였으며, 예측한 유전자 발현 궤적의 시간적 일관성을 높이는 추세 정규화 전략도 더했다. 측정하지 않은 시점의 유전자 발현 예측에서 기존 방법들을 앞서는 최고 수준의 성능을 보였고, 이어지는 분석 과제(downstream tasks)에서도 뛰어난 결과를 냈다.[^p8] | 1저자 S. Han, 마지막 저자 김동섭 |

## 교수와 전문 분야

김동섭 교수는 서울대학교에서 화학 학사(1985.3–1989.2)와 석사(1989.3–1991.2)를, 미국 Brown University에서 화학 박사(1993.9–1998.5)를 받았다.[^prof] 미국 University of Pennsylvania의 Laboratory for Research on the Structure of Matter에서 박사후연구원(1998.5–2000.12)으로, 미국 Oak Ridge National Laboratory의 Protein Informatics Group에서 박사후연구원(2001.1–2003.1)으로 일했다.[^prof] 학과 교수 소개에 따르면 KAIST 바이오및뇌공학과 조교수(2003.02–2006.08)와 부교수(2006.09–2012.08)를 거쳐 2012년 9월부터 교수다.[^deptprof] 학과 교수진 목록은 연구분야를 바이오정보학, 계산생물학, 분자모델링으로 적는다.[^deptlist]

교수는 2020년 인터뷰에서 박사학위 연구 주제가 계산화학이었고, 인간게놈프로젝트가 진행되고 완성되던 2000년대 초에 새로 발굴된 단백질의 구조를 예측하는 연구에 흥미를 느껴 계산화학에서 공부한 여러 모델링 기법을 적용할 수 있겠다는 생각으로 이 분야 연구로 옮겼다고 말했다.[^bbs2020] 2017년 인터뷰에서는 박사 과정 때 컴퓨터 시뮬레이션으로 화학 반응이 어떻게 일어나는지, 화학물질이 시간에 따라 어떻게 움직이는지를 연구했다고 말했다.[^bbs2017]

누리집 교수 페이지는 연구 관심을 생물정보학, 단백질 구조 예측, 단백질 기능 예측, 단백질 설계, 단백질-단백질 상호작용, 단백질-리간드 상호작용, 생물정보 파이프라인, 생체분자 시뮬레이션, 막단백질(세포막에 박혀 있거나 붙어 있는 단백질), 이온 채널(세포막에서 이온이 지나가는 통로를 이루는 단백질), 단백질 구조 변화의 동역학(Protein Conformational Dynamics), 분자 동역학과 몬테카를로(난수로 표본을 뽑아 확률적으로 계산하는 방법) 시뮬레이션(긴 시간 규모의 동역학 시뮬레이션 알고리즘, 몬테카를로 기반 최적화 알고리즘)으로 적는다.[^prof] 학과 연구실 소개는 연구실이 단백질의 원격 상동체(서열은 많이 달라도 진화적으로 이어진 단백질)를 찾는 알고리즘, 단백질 상호작용 접촉면의 핫스팟(접촉면 잔기 가운데 결합 에너지에 대한 기여가 두드러진 잔기) 예측 방법, 단백질의 상관 돌연변이(단백질의 서로 다른 자리에서 함께 일어나는 돌연변이)를 찾고 그 정보로 서열 정렬을 최적화하는 방법, 인산화 자리 예측 방법, 단백질 도메인-펩타이드 결합 에너지 계산 방법을 개발하고 질병 원인 돌연변이를 찾았다고 적는다. 그 가운데 결합 에너지 계산 방법은 RECOMB DREAM4 challenge의 SH3 도메인(펩타이드의 특정 서열에 결합하는 단백질 구조 단위의 한 종류) 펩타이드 인식 예측 과제에서 가장 좋은 성능(best performance)을 보였다고 적는다. 분열효모(S. pombe, 세포가 둘로 갈라져 늘어나는 효모의 한 종류) 돌연변이 라이브러리 국제 연구 컨소시엄에 참여해 그 사업에 필요한 생물정보 작업 대부분을 맡는다고도 적는다.[^labintro] 학과 교수 소개의 대표 연구실적 9편(2008–2017년)에는 결합 단백질 뼈대 라이브러리 LibBP(Bioinformatics, 2016), 턱없는 척추동물의 가변 림프구 수용체를 바탕으로 한 결합 뼈대 설계(PNAS, 2012), 분열효모 유전체 전체 유전자 결실 세트 분석(Nature Biotechnology, 2010), 단백질 상호작용 핫스팟 모델링(Nucleic Acids Research, 2009)이 들어 있다.[^deptprof]

랩 Publications 페이지의 목록(2005–2026년, 105줄)을 구간별로 보면, 2005–2009년 구간 논문은 접힘 인식(서열로 단백질이 어떤 접힘 구조에 속하는지 알아내는 방법)·원격 상동체 탐지·2차 구조(단백질 사슬이 국소적으로 이루는 나선·판 같은 규칙적 구조) 함량 예측 같은 단백질 구조 예측과 서열 정렬, 공진화하는 잔기(진화 과정에서 함께 변해 온 아미노산 자리) 분석, 단백질 상호작용과 리간드 결합 네트워크를 주로 다룬다. 2010–2014년 구간에는 히스톤 변형 분석, 분열효모의 화학-유전 프로파일(유전자를 하나씩 없앤 균주들이 화학물질에 보이는 반응 양상), 결합 단백질 설계가 더해지고, 2015–2019년 구간에는 염색체 형태 포착(chromosome conformation capture, 세포핵 안에서 공간적으로 맞닿은 DNA 부위 쌍을 찾는 실험 방법) 자료와 3차원 유전체, 역도킹 기반 표적 탐색, 딥러닝 예측 모델이 나온다. 2020년 이후 논문은 딥러닝·그래프 신경망·강화학습으로 변이 효과와 결합 친화도, 면역 수용체 결합, 염색질 고리, 유전자 발현을 예측하거나 분자와 항체를 설계하는 연구가 중심이다.[^pubs]

논문으로 보면 지금의 전문 분야는 네 갈래다. 첫째, 그래프 신경망과 심층 생성 모델로 단백질 복합체 구조와 변이 효과를 예측하는 방법이다(대표 논문 1, 2).[^p1][^p2] 둘째, 항체 결합 부위 설계와 B세포 면역우세 예측처럼 면역 단백질을 설계하고 예측하는 계산 방법이다(대표 논문 3, 4).[^p3][^p4] 셋째, 약물-표적 결합 예측과 화학물질 유해 결과 경로 네트워크 같은 계산 신약 개발·독성 예측이다(대표 논문 5, 6).[^p5][^p6] 넷째, 염색질 고리와 단일세포 유전자 발현처럼 유전체 구조와 발현 자료를 딥러닝으로 예측하는 방법이다(대표 논문 7, 8).[^p7][^p8]

## 응용 분야

학과 연구실 소개는 연구실이 세우려는 예측 가능한 생체 시스템 모형을 신약 개발과 새로운 진단 같은 응용에 쓸 수 있다고 적고,[^labintro] 계산 단백질 설계 페이지는 치료용 단백질 의약품, 특히 리피바디의 설계·개발을,[^pd] 계산 신약 개발 페이지는 정교한 약물 설계와 약물 재창출에 쓰는 약물 표적 예측 도구·서버를 든다.[^dd] 2022년 인터뷰에서 교수는 단백질의 구조와 기능을 연구하는 구조생물학이 신약 개발에 아주 가까운 분야라고 말했다.[^bbs2022] 대표 논문은 항체 치료제 개발을 위한 항체 설계,[^p3] 백신 설계를 위한 B세포 면역우세 예측,[^p4] 신약 개발의 약물-표적 결합 예측,[^p5] 화학물질의 유해 결과 기전 이해[^p6]를 대상으로 하고, G-RANK는 생명공학의 여러 응용에 쓸 도구로 제시됐다.[^p1]

## 구성원

2026년 10월 25일 랩 Members 페이지 기준이다. Postdoctoral Researcher 칸 2명, Ph.D. Students 칸 9명, Integrated Ph.D. Students 칸 2명, M.S. Students 칸 2명이며, 과정 칸은 칸 이름을 우리말로 옮긴 것이다. 연구 주제는 각 사람의 Interest 줄이고, Chaeyoung Moon과 Sungjin Choi에게는 이 줄이 없다. 이메일은 페이지에 적힌 학교 이메일이다. 페이지는 각 사람의 학사·석사·박사 전공도 함께 적는다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Woosung Jeon | 박사후연구원 | Protein Bioinformatics | jjs092@kaist.ac.kr | 2, 3 |
| Ha Young Kim | 박사후연구원 | Protein Bioinformatics | ha01994@kaist.ac.kr | 1, 2 |
| Boram Lee | 박사과정 | Genome & Proteome informatics | brlee920@kaist.ac.kr |  |
| Sujae Jeong | 박사과정 | Protein Bioinformatics | jsj0739@kaist.ac.kr |  |
| Shangjin Han | 박사과정 | Drug discovery | hanshangjin@kaist.ac.kr | 8 |
| Chaeyoung Moon | 박사과정 |  | cy.moon@kaist.ac.kr | 5 |
| Minju Na | 박사과정 | Bioinformatics & Drug discovery | ijudy96@kaist.ac.kr | 6 |
| Jeongyeon Lee | 박사과정 | Drug discovery | wjddus420@kaist.ac.kr |  |
| Joohyun Cho | 박사과정 | Protein design | Joohyun98@kaist.ac.kr |  |
| Dongje Moon | 박사과정 | Protein Bioinformatics | dongje.moon@kaist.ac.kr |  |
| Sojeong Bae | 박사과정 | Bioinformatics | sojeongbae@kaist.ac.kr |  |
| Sungjin Choi | 석박사통합과정 |  | csungjin@kaist.ac.kr | 4 |
| Donghyeon Kim | 석박사통합과정 | Drug discovery | kdysmurf@kaist.ac.kr |  |
| Hyuijeong Han | 석사과정 | Bioinformatics | hanjy0507@kaist.ac.kr |  |
| Seoyoon Huh | 석사과정 | Bioinformatics | seoyoon.h@kaist.ac.kr |  |

## 졸업생과 이전 구성원

랩 Alumni 페이지의 24명이다. Ph.D. 칸 14명, M.S. 칸 8명, Post-Doctoral Researchers 칸 2명이며, 학위·과정 칸은 칸 이름을 옮겼다. 페이지는 졸업 연도와 진로를 적지 않고, 각 사람의 학사·석사·박사 전공을 적는다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jeongtae Son | Ph.D. |  |
| Dongchan Yang | Ph.D. |  |
| KyoungYeul Lee | Ph.D. |  |
| Taesu Chung | Ph.D. |  |
| Aeri Lee | Ph.D. |  |
| Seungpyo Hong | Ph.D. |  |
| Youngmahn Han | Ph.D. |  |
| Chan-Seok Jeong | Ph.D. |  |
| Minho Lee | Ph.D. |  |
| Inkyung Jung | Ph.D. |  |
| Keunwan Park | Ph.D. |  |
| Soyoung Lee | Ph.D. |  |
| Sangjo Han | Ph.D. |  |
| Byung-chul Lee | Ph.D. |  |
| Seongtaek Oh | M.S. |  |
| Hyoa Kang | M.S. |  |
| Seungtaek Yu | M.S. |  |
| Won-chul Lee | M.S. |  |
| Sheehyun Kim | M.S. |  |
| Changwon Keum | M.S. |  |
| Heesung Ahn | M.S. |  |
| Hyeshik Chang | M.S. |  |
| Seungsoo Han | Post-Doctoral Researcher |  |
| Kyuil Cho | Post-Doctoral Researcher |  |

## 최근 논문 목록 (2021–2026)

랩 Publications 페이지의 「2026-」 구역 2편과 「2020-2025」 구역의 2021–2025년 논문 13편 가운데, 자연·공학과 직접 연계된 연구만 싣는 이 위키의 의생명 수록 범위에 드는 14편이다(2026년 2, 2025년 1, 2024년 5, 2023년 1, 2022년 2, 2021년 3, 범위는 근거 페이지). 연도는 각 줄에 적힌 연도이고, 각 줄은 저자·제목·학술지 표기와 DOI 주소까지 페이지에 적힌 그대로다.[^pubs]

**2026**

- M. Na and D. Kim; AOP Network Box: An Integrative Framework for Bridging Adverse Outcome Pathways and Biological Networks. Chem. Res. Toxicol. 20 July 2026; 39 (7): 1311–1319. https://doi.org/10.1021/acs.chemrestox.6c00041
- S. Han and D. Kim, scMix: learning temporal dynamics of gene expression under irregular time intervals, Bioinformatics, Volume 42, Issue 3, March 2026, btag080, https://doi.org/10.1093/bioinformatics/btag080

**2025**

- Choi, S., Kim, D. BIDpred: unraveling B cell Immunodominance hierarchical pattern using statistical feature discovery and deep learning prediction. Frontiers in Immunology, 16, 1646946. (2025). https://doi.org/10.3389/fimmu.2025.1646946

**2024**

- Choi, S., Kim, D. B cell epitope prediction by capturing spatial clustering property of the epitopes using graph attention network. Sci Rep 14, 27496 (2024). https://doi.org/10.1038/s41598-024-78506-z
- Ryu, B., Jeon, W. & Kim, D. Integrating genomic and molecular data to predict antimicrobial minimum inhibitory concentration in Klebsiella pneumoniae. Sci Rep 14, 25951 (2024). https://doi.org/10.1038/s41598-024-75973-2
- H. Y. Kim, S. Kim, W.-Y. Park, D. Kim, "TSpred: a robust prediction framework for TCR–epitope interactions using paired chain TCR sequence data," Bioinformatics, 2024, doi: https://doi.org/10.1093/bioinformatics/btae472.
- W. Jeon and D. Kim, "AbFlex: designing antibody complementarity determining regions with flexible CDR definition," Bioinformatics, 2024, doi: https://doi.org/10.1093/bioinformatics/btae122.
- J. Son and D. Kim, "Applying network link prediction in drug discovery: an overview of the literature," Expert Opinion on Drug Discovery, 2024. doi: https://doi.org/10.1080/17460441.2023.2267020.

**2023**

- H. Y. Kim, S. Kim, W.-Y. Park, D. Kim, "G-RANK: An equivariant graph neural network for the scoring of protein-protein docking models," Bioinformatics Advances, 2023, doi: https://doi.org/10.1093/bioadv/vbad011.

**2022**

- C. Moon and D. Kim, "Prediction of drug–target interactions through multi-task learning," Scientific Reports, 2022, doi: https://doi.org/10.1038/s41598-022-23203-y.
- D. Yang, T. Chung, and D. Kim, "DeepLUCIA: predicting tissue-specific chromatin loops using Deep Learning-based Universal Chromatin Interaction Annotator," Bioinformatics, 2022, doi: https://doi.org/10.1093/bioinformatics/btac373.

**2021**

- Y Seo, S Bang, J Son, D Kim, Y Jeong, P Kim, J Yang, JH Eom, N Choi, HN Kim, "Brain physiome: A concept bridging in vitro 3D brain models and in silico models for predicting drug toxicity in the brain," Bioactive Materials, 2021, doi: https://doi.org/10.1016/j.bioactmat.2021.11.009.
- H. Y. Kim, W. Jeon, and D. Kim, "An enhanced variant effect predictor based on a deep generative model and the Born-Again Networks," Scientific Reports, 2021, doi: https://doi.org/10.1038/s41598-021-98693-3.
- J. Son and D. Kim, "Development of a graph convolutional neural network model for efficient prediction of protein-ligand binding affinities," PLOS ONE, 2021, doi: https://doi.org/10.1371/journal.pone.0249404.

## 연락과 위치

- 주소: 34141 대전광역시 유성구 대학로 291 한국과학기술원(KAIST) 바이오및뇌공학과[^deptprof]
- 교수 연구실: 1101호, E16[^deptlist][^deptprof]
- 교수 이메일과 전화: kds@kaist.ac.kr, +82-42-350-4317, 팩스 +82-42-350-4310[^prof]
[^home]: 연구실 누리집 첫 화면 <https://sites.google.com/view/kaist-bcbl> (2026-10-25 열람)
[^prof]: 누리집 Professor 페이지 <https://sites.google.com/view/kaist-bcbl/people/professor> (직위, 소속, 연락처, Education, Research Experience, Research Interests, 2026-10-25 열람)
[^members]: 누리집 Members 페이지 <https://sites.google.com/view/kaist-bcbl/people/members> (2026-10-25 열람)
[^alumni]: 누리집 Alumni 페이지 <https://sites.google.com/view/kaist-bcbl/people/alumni> (2026-10-25 열람)
[^sb]: 누리집 Research 메뉴 Structural Bioinformatics 페이지 <https://sites.google.com/view/kaist-bcbl/research/structural-bioinformatics> (2026-10-25 열람)
[^pd]: 누리집 Research 메뉴 Computational Protein Design 페이지 <https://sites.google.com/view/kaist-bcbl/research/computational-protein-design> (2026-10-25 열람)
[^dd]: 누리집 Research 메뉴 Computational Drug Discovery 페이지 <https://sites.google.com/view/kaist-bcbl/research/computational-drug-discovery> (2026-10-25 열람)
[^sw]: 누리집 Server and Software 페이지 <https://sites.google.com/view/kaist-bcbl/server-and-software> (2026-10-25 열람)
[^pubs]: 누리집 Publications 페이지 <https://sites.google.com/view/kaist-bcbl/publications> (「2026-」부터 「2005-2009」까지 다섯 구역, 2026-10-25 열람)
[^deptlist]: KAIST 바이오및뇌공학과 교수진 목록 <https://bioeng.kaist.ac.kr/index.php?mid=bio_03_01> (2026-10-25 열람)
[^deptprof]: KAIST 바이오및뇌공학과 교수 소개(김동섭) <https://bioeng.kaist.ac.kr/index.php?document_srl=6762&mid=bio_03_01> (연구실명, 최종학위, 연구분야, 경력, 대표 연구실적, 2026-10-25 열람)
[^labs]: KAIST 바이오및뇌공학과 연구실/센터 목록 <https://bioeng.kaist.ac.kr/index.php?mid=bio_02_02> (Bioinformatics / Systems Biology 칸, 2026-10-25 열람)
[^labintro]: KAIST 바이오및뇌공학과 연구실 소개(단백질생물정보학 연구실) <https://bioeng.kaist.ac.kr/index.php?document_srl=10899&mid=bio_02_02> (연구실 목표와 Protein Bioinformatics, Computational Protein Design, Computational Drug Discovery, Computational Epigenomics 칸, 게시 날짜 표기 없음, 2026-10-25 열람)
[^bbs2022]: KAIST 바이오및뇌공학과 소식지 「[과학산책] 김동섭 교수, 구조생물학과 AI」(2022-08-01 게시) <https://bioeng.kaist.ac.kr/index.php?document_srl=16413&mid=bio_05_04> (2026-10-25 열람)
[^bbs2020]: KAIST 바이오및뇌공학과 소식지 「[학과 교수 취재] 김동섭 교수」(2020-03-11 게시) <https://bioeng.kaist.ac.kr/index.php?document_srl=13883&mid=bio_05_04> (2026-10-25 열람)
[^bbs2017]: KAIST 바이오및뇌공학과 소식지 「[학과 교수 취재] 김동섭 교수. 할 수 있는 일에 최선을 다하는 미덕」(2017-06-30 게시) <https://bioeng.kaist.ac.kr/index.php?document_srl=5012&mid=bio_05_04> (2026-10-25 열람)
[^p1]: H. Y. Kim, S. Kim, W.-Y. Park, D. Kim, Bioinformatics Advances 3, vbad011 (온라인 2023-02-03). <https://doi.org/10.1093/bioadv/vbad011> 초록 기준.
[^p2]: H. Y. Kim, W. Jeon, D. Kim, Scientific Reports 11, 19127 (온라인 2021-09-27). <https://doi.org/10.1038/s41598-021-98693-3> 초록 기준.
[^p3]: W. Jeon, D. Kim, Bioinformatics 40, btae122 (온라인 2024-03-06). <https://doi.org/10.1093/bioinformatics/btae122> 초록 기준.
[^p4]: S. Choi, D. Kim, Frontiers in Immunology 16, 1646946 (온라인 2025-08-13). <https://doi.org/10.3389/fimmu.2025.1646946> 초록 기준.
[^p5]: C. Moon, D. Kim, Scientific Reports 12, 18323 (온라인 2022-10-31). <https://doi.org/10.1038/s41598-022-23203-y> 초록 기준.
[^p6]: M. Na, D. Kim, Chemical Research in Toxicology 39, 1311-1319 (온라인 2026-06-16). <https://doi.org/10.1021/acs.chemrestox.6c00041> 초록 기준(Europe PMC 등록 초록).
[^p7]: D. Yang, T. Chung, D. Kim, Bioinformatics 38, 3501-3512 (온라인 2022-05-31). <https://doi.org/10.1093/bioinformatics/btac373> 초록 기준.
[^p8]: S. Han, D. Kim, Bioinformatics 42, btag080 (온라인 2026-02-15). <https://doi.org/10.1093/bioinformatics/btag080> 초록 기준.

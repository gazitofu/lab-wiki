# DSAIL (Data Science & Artificial Intelligence Lab)

**KAIST 산업및시스템공학과·데이터사이언스대학원·안보과학기술대학원 · 박찬영 교수**

- 분야: 그래프 표현 학습, 추천 시스템, 멀티모달 학습(장면 그래프 생성, 멀티모달 LLM), LLM 에이전트와 검색 증강 질의응답, 과학을 위한 AI(분자·소재·세포·물리 시뮬레이션), 시계열·시공간 예측
- 대분야: 컴퓨팅·AI
- 태그: 그래프 기계학습·지식 그래프[^research][^p1][^p2], 대형 언어 모델[^research][^p3][^p4], 멀티모달 AI[^home][^research], 컴퓨터 비전[^research][^p5], 과학·공학 AI[^research][^p7][^p8]
- 홈페이지: <https://dsail.kaist.ac.kr/>
- 근거와 출처: [DSAIL 근거 페이지](dsail-sources.md)

> 관계형 데이터, 멀티모달 데이터, 과학 데이터처럼 복잡한 데이터를 이해하는 인공지능을 만들고, 거기서 배운 표현을 추론, 개인화, 발견으로 잇는 연구실이다.[^home]

## 무엇을 연구하나

DSAIL(Data Science & Artificial Intelligence Lab)은 KAIST 박찬영 교수가 이끄는 연구실이다.[^home][^professor] 교수 페이지는 교수의 소속을 산업및시스템공학과(Department of Industrial and Systems Engineering), Graduate School of AI, 데이터사이언스대학원(Graduate School of Data Science), Department of AX(College of AI)로 적고, 학생은 이 네 곳 가운데 어디로든 연구실에 들어올 수 있다고 안내한다.[^professor][^gst][^gsds] 안보과학기술대학원 교수 목록도 박찬영 교수를 소속학과 Department of Industrial & Systems Engineering, 연구실 Data Science & Artificial Intelligence Lab (DSAIL)로 싣는다.[^gst]

누리집 첫 화면은 「Learning, reasoning, and discovery from complex data」(복잡한 데이터에서 배우고, 추론하고, 발견한다)를 표어로 건다. 관계형 데이터(개체와 개체 사이의 관계로 이루어진 데이터), 멀티모달 데이터(이미지·글처럼 종류가 다른 자료가 함께 있는 데이터), 과학 데이터를 이해하는 인공지능을 만들어 학습한 표현(데이터의 특징을 기계학습 모델이 계산에 쓰는 수치 벡터 등으로 나타낸 것)을 추론, 개인화, 발견으로 잇는다고 소개한다. 연구 범위로는 그래프(점과 점을 잇는 선으로 대상과 그 관계를 나타낸 자료)·관계 학습, 개인화 추천, 멀티모달 지능, 에이전트 AI(목표를 이루려고 스스로 판단하고 도구를 쓰며 행동하는 인공지능), 과학을 위한 AI를 들고, 이 분야들에서 복잡한 데이터로 배운 표현이 일반화, 추론, 의사결정, 발견을 어떻게 뒷받침할 수 있는지 연구한다고 적는다.[^home]

Research 페이지는 연구를 여섯 분야(그래프 표현 학습, 추천 시스템, 멀티모달 학습, LLM 에이전트·안전성, 과학을 위한 AI, Time-series & Spatio-temporal Modeling)와 실세계 응용으로 나누고, 논문마다 주된 기여에 따라 한 분야를 배정한다.[^research] 여기서 LLM은 대형 언어 모델(Large Language Model, 많은 글을 학습해 글을 이해하고 만들어 내는 큰 인공지능 모델)의 줄임말이다. 아래 논문 목록에 실은 2021–2026년 논문 145편을 이 배정으로 나누면 과학을 위한 AI 52편, 그래프 표현 학습 31편, LLM 에이전트·안전성 17편, 추천 시스템 17편, 멀티모달 학습 15편, 실세계 응용 8편, 시계열·시공간 모델링 5편이다.[^pubs] 페이지는 연구실의 최근 연구 대부분이 분야가 겹치는 곳에 있다고 적고, 그런 교차 주제로 과학 파운데이션 모델(그래프 학습과 등변 학습을 분자·메시·세포에 적용), 개인화 에이전트(사용자를 기억하는 에이전트와 스스로 개선되는 추천 시스템), 멀티모달·체화 에이전트(행동하는 시각-언어 모델과 차트·영상을 읽는 에이전트), 과학용 LLM과 에이전트(스펙트럼을 읽고 합성을 계획하며 분자와 세포를 추론하는 LLM과 에이전트), 효율적인 LLM·멀티모달 모델을 든다.[^research]

대표 논문에서는 그래프를 변형하지 않고 자기 지도 학습(사람이 붙인 정답 없이 데이터 자체에서 학습 신호를 만들어 배우는 방법)을 하는 방법을 만들었고,[^p1] 시간에 따라 바뀌는 그래프에서 예측과 그 설명을 함께 내놓는 모델을 제안했다.[^p2] 대형 언어 모델이 협업 필터링(여러 사용자의 상호작용 기록에서 취향이 비슷한 사용자와 아이템을 찾아 추천하는 방법) 추천 모델의 지식을 쓰게 해 상호작용 기록이 적을 때와 많을 때 모두 추천을 잘하게 했고,[^p3] 대형 언어 모델 기반 추천이 사용자 행동의 순서를 이해하는지 점검한 뒤 순서 정보를 넣는 방법을 제안했다.[^p4] 이미지 속 물체와 그 관계를 그래프로 나타내는 장면 그래프 생성에서 주석이 없는 관계를 활용하는 자기 학습(모델이 스스로 예측해 붙인 라벨로 다시 학습하는 방법) 틀을 만들었고,[^p5] 모호한 질문에 답하는 검색 증강 생성(질문과 관련된 글을 먼저 찾아 그 내용을 바탕으로 답을 만드는 방식)의 정확도와 효율을 함께 높였다.[^p6] 분자 쌍의 상호작용을 핵심 부분 구조로 예측하는 방법과,[^p7] 참조 물질을 검색해 무기물의 합성 원료를 찾는 방법도 제안했다.[^p8]

## 주요 연구 주제

### 1. 그래프 표현 학습

Research 페이지는 이 분야(Graph & Relational Learning)를 네트워크, 지식 그래프(사실을 개체와 관계로 정리한 그래프), 하이퍼그래프(선 하나가 셋 이상의 점을 함께 이을 수 있는 그래프), 상호작용 구조 같은 관계형 데이터에서 잡음, 부족한 라벨, 분포 변화(학습할 때와 쓸 때 데이터의 통계적 성질이 달라지는 것) 속에서도 일반화되는 표현을 배우는 연구로 정의한다. 연구 질문으로는 구조의 잡음과 적대적 공격(모델의 판단을 틀리게 하려고 입력을 일부러 조작하는 공격) 아래에서 그래프 모델이 믿을 만하게 동작하는 법, 라벨이 몇 개뿐일 때 배울 수 있는 것, 분산된 클라이언트·연속 데이터 흐름·고차 구조로 그래프 학습을 넓히는 법을 든다.[^research] 대표 논문 1은 그래프를 변형하는 증강 없이 그래프를 자기 지도 학습하는 AFGRL을,[^p1] 대표 논문 2는 시간 그래프 신경망(시간에 따라 연결이 생기고 바뀌는 그래프를 다루는 신경망)의 예측을 스스로 설명하는 TGIB를 제안했다.[^p2] Projects 페이지의 진행 중 과제에는 여러 모달리티와 분야에 쓸 수 있는 그래프 파운데이션 모델 과제와 그래프 빅데이터를 위한 파운데이션 모델 개발 과제가 있다.[^projects]

### 2. 추천 시스템

Research 페이지는 이 분야(Personalized Intelligence & Recommendation)를 상호작용 데이터에서 사용자와 아이템을 모델링하는 연구로 정의하고, 협업 필터링부터 대형 언어 모델 기반 추천 시스템과 스스로 진화하는 추천 시스템까지 다룬다고 적는다. 연구 질문으로는 대형 언어 모델이 협업 신호와 순차 신호를 실제로 이해하는지, 롱테일 사용자·아이템과 빠진 모달리티를 어떻게 다룰지, 사용자 표현과 추천 시스템 자체가 시간에 따라 어떻게 진화할 수 있는지를 든다.[^research] 대표 논문 3은 사전 학습된 협업 필터링 추천 모델의 지식을 대형 언어 모델이 쓰게 하는 A-LLMRec을,[^p3] 대표 논문 4는 순차 추천 모델이 뽑은 사용자 표현을 대형 언어 모델에 증류(한 모델이 배운 지식을 다른 모델이 따라 배우게 하는 학습 방법)하는 LLM-SRec을 제안했다.[^p4]

### 3. 멀티모달 학습

Research 페이지는 이 분야(Multimodal Intelligence)를 이미지, 영상, 언어를 정렬해 세밀한 이해와 조합적 추론을 효율적으로 뒷받침하는 표현을 만드는 연구로 정의하고, 국문 소개에서는 장면 그래프 생성부터 효율적인 멀티모달 LLM까지 시각-언어 이해를 다룬다고 적는다. 연구 질문으로는 약한 감독이나 자연어 감독만으로 장면 그래프를 배울 수 있는지, 멀티모달 LLM에서 정보를 잃지 않고 시각 토큰을 언제 덜어낼 수 있는지, 모델이 조합적 시각 추론을 어떻게 익히는지를 든다.[^research] 대표 논문 5는 주석이 없는 관계 묶음에 의사 라벨(모델이 예측해 임시로 붙인 정답)을 붙여 장면 그래프 생성 모델을 학습시키는 자기 학습 틀 ST-SGG를 제안했다.[^p5] Projects 페이지의 진행 중 과제에는 시각 데이터 기억을 위한 장면 그래프 생성 기술 연구가 있다.[^projects]

### 4. LLM 에이전트·안전성

Research 페이지는 이 분야(Agentic AI & Reasoning)를 여러 단계에 걸쳐 추론하고 도구와 기억을 쓰며 행동하고 피드백으로 개선되는 LLM 에이전트를 다루는 연구로 정의하고, 최종 답만이 아니라 과정으로 평가하며 사용자마다의 안전 요구에 맞추는 것을 목표로 적는다. 국문 소개는 도구 사용 에이전트의 평가·최적화와 사용자 맞춤 안전성을 다룬다고 적는다. 연구 질문으로는 에이전트의 최종 답만이 아니라 추론 궤적을 어떻게 평가할지, 다중 에이전트 시스템이 실패했을 때 어느 에이전트의 책임인지와 에이전트가 사용자를 어떻게 기억할지, 하나의 안전 기준이 모든 사용자에게 맞는지, 큰 모델의 계산(토큰, 어텐션, 디코딩 단계) 가운데 무엇을 덜어내도 중요한 것을 잃지 않는지를 든다.[^research] 대표 논문 6은 모호한 질문에 답하는 검색 증강 생성 틀 DIVA를 제안했다.[^p6] Projects 페이지의 진행 중 과제에는 언어모델 기반 멀티-에이전트 시스템 요소기술 개발이 있다.[^projects]

### 5. 과학을 위한 AI

Research 페이지는 이 분야(AI for Science & Engineering)를 분자, 소재, 세포, 유체와 물리계, 회로를 위한 표현과 에이전트를 다루는 연구로 정의한다. 물성 예측부터 합성 계획과 시뮬레이션까지 다루고, 스펙트럼을 읽고 실험을 계획하며 과학 연구 과정의 일부를 수행하는 LLM 에이전트도 포함한다고 적는다. 국문 소개는 분자·소재·생물 시스템·물리 시뮬레이션의 학습 기반 모델링을 다룬다고 적는다. 연구 질문으로는 물성 예측과 합성 계획을 위해 원자 구조와 결정 구조를 어떻게 표현할지, 희소한 단일세포·단백질 데이터를 믿을 만하게 모델링할 수 있는지, 등변 모델과 물리를 넣은 모델이 유체 흐름, 메시, 그 바탕의 편미분 방정식 같은 3차원 물리계를 어떻게 모사하는지를 든다.[^research] 대표 논문 7은 짝이 되는 분자를 조건으로 핵심 부분 구조를 찾는 분자 관계 학습 틀 CGIB를,[^p7] 대표 논문 8은 무기물 역합성 계획(만들려는 물질을 어떤 원료 물질로 합성할지 거꾸로 찾는 일) 모델 Retrieval-Retro를 제안했다.[^p8] Projects 페이지의 진행 중 과제에는 금속 소재 파운데이션 모델, 복합소재 물성 예측, 3차원 편미분 방정식 풀이를 위한 신경 연산자 과제가 있다.[^projects]

### 6. 시계열·시공간 모델링

Research 페이지는 이 분야(Time-series & Spatio-temporal Modeling)를 교통·센서 데이터 흐름부터 LLM 프롬프트로 조정하는 시계열 파운데이션 모델까지, 비정상 시계열(평균이나 분산 같은 통계적 성질이 시간에 따라 바뀌는 시계열)을 예측하고 그 변화에 적응하는 연구로 정의한다. 연구 질문으로는 적은 매개변수로 시계열 파운데이션 모델을 새 분야에 미세 조정하는 법, 데이터 분포가 바뀔 때 예측 모델이 온라인으로 적응할 수 있는지, 교통·센서 망에서 공간 구조와 시간 변화를 어떻게 결합할지를 든다. 페이지는 이 분야의 대표 논문에 대표 논문 2(TGIB)도 넣었다.[^research]

## 대표 논문

랩 Publications 페이지의 2021–2026년 학회 논문 가운데 박찬영 교수가 마지막 저자인 논문을 Research 페이지의 다섯 연구 분야에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2022 | [Augmentation-Free Self-Supervised Learning on Graphs](https://doi.org/10.1609/aaai.v36i7.20700) · AAAI 2022 | 이미지에서 성공한 자기 지도 학습이 그래프 자료로 넓어지면서, 그래프를 일부러 변형(증강)한 관점들을 비교하는 대조 학습(같은 대상에서 나온 표현은 가깝게, 다른 대상의 표현은 멀게 배우는 방법)이 중심이 되었다. 그러나 신중하게 설계하지 않은 그래프 증강은 그래프의 뜻을 크게 바꿀 수 있어, 기존 방법의 성능은 증강 방식(증강 초매개변수와 증강 조합)을 무엇으로 고르느냐에 크게 좌우된다. 증강 없이 그래프를 자기 지도 학습하는 틀 AFGRL을 제안했다. 그래프 안에서 국소 구조 정보와 전역 의미를 함께 공유하는 노드(그래프의 점)를 찾아 그래프의 다른 관점을 만든다. 여러 실제 데이터셋의 노드 분류, 군집화, 유사도 검색에서 우수함을 보였다.[^p1] | 1저자 N. Lee, 마지막 저자 박찬영 |
| 2 | 2024 | [Self-Explainable Temporal Graph Networks based on Graph Information Bottleneck](https://doi.org/10.1145/3637528.3671962) · KDD 2024 | 시간 그래프 신경망(TGNN)은 그래프의 연결 구조와 시간에 따른 상호작용의 의존 관계를 함께 포착하지만, 과거 사건이 예측에 어떤 영향을 주는지 알기 어려워 예측을 설명할 필요가 커졌다. 정적 그래프용 설명 모델은 시간 의존성을 담지 못해 그대로 쓸 수 없고, 기존 시간 그래프 설명 모델은 예측과 설명에 별도 모델이 필요한 사후 설명 방식이라 설명의 효율과 정확도에 한계가 있다. 정보 병목 이론(예측에 필요한 정보만 남기고 나머지는 덜어 내도록 표현을 압축하는 원리)에 따라 각 시간 사건에 확률성을 넣어 사건 발생을 설명하는 내장형 설명 틀 TGIB를 제안했다. 링크 예측 성능과 설명 능력 모두에서 최신 방법보다 우수했고, 시간 그래프에서 예측과 설명을 처음부터 끝까지 한 번에(end-to-end) 함께 수행하는 첫 연구라고 적는다.[^p2] | 1저자 S. Seo, 마지막 저자 박찬영 |
| 3 | 2024 | [Large Language Models meet Collaborative Filtering: An Efficient All-round LLM-based Recommender System](https://doi.org/10.1145/3637528.3671931) · KDD 2024 | 협업 필터링 추천 시스템(CF-RecSys)은 사용자-아이템 상호작용이 드문 콜드 상황에서 약해, 최근에는 사전 학습된 모달리티 부호기와 대형 언어 모델로 사용자·아이템의 글·이미지 정보를 쓰는 전략이 나왔다. 그러나 이런 방법은 콜드 상황에서는 효과적이어도 협업 지식이 없어 웜 상황(상호작용 기록이 충분한 상황)에서는 단순한 전통 협업 필터링 모델보다 못했다. 사전 학습된 최신 CF-RecSys가 담은 협업 지식, 곧 이미 학습된 사용자·아이템 임베딩(사용자와 아이템을 나타내는 수치 벡터)을 대형 언어 모델이 직접 쓰게 해 콜드와 웜 상황 모두에서 뛰어난 A-LLMRec을 제안했다. 여러 기존 CF-RecSys와 결합할 수 있고, LLM 기반 추천에 보통 필요한 대규모 미세 조정이 필요 없다. 콜드·웜, 퓨샷, 콜드 사용자, 교차 도메인 상황의 실제 데이터셋에서 우수했고, 선호 장르 예측으로 협업 지식을 이해한 자연어 출력의 가능성도 보였다.[^p3] | 1저자 S. Kim, 마지막 저자 박찬영 |
| 4 | 2025 | [Lost in Sequence: Do Large Language Models Understand Sequential Recommendation?](https://doi.org/10.1145/3711896.3737035) · KDD 2025 | 대형 언어 모델은 글 이해 능력과 맥락 파악 능력 덕분에 추천 도구로 떠올랐고, LLM 기반 추천 모델(LLM4Rec)은 순차 추천 상황에서 학습·평가된다. 그러나 이 모델들이 사용자의 아이템 상호작용 순서에 담긴 순차 정보를 이해하는지는 거의 다뤄지지 않았다. 일련의 실험으로 기존 LLM4Rec 모델이 학습과 추론에서 순차 정보를 충분히 포착하지 못함을 보이고, 사전 학습된 순차 추천 모델(CF-SRec)에서 뽑은 사용자 표현을 LLM에 증류해 순차 정보를 통합하는 LLM-SRec을 제안했다. LLM-SRec은 사용자의 상호작용 순서를 이해하는 능력을 높여 추천 성능을 개선했고, LLM을 미세 조정해야 하는 기존 LLM4Rec 모델과 달리 가벼운 다층 퍼셉트론(MLP) 몇 개만 학습해 최고 수준(state-of-the-art) 성능을 냈다.[^p4] | 1저자 S. Kim, 마지막 저자 박찬영 |
| 5 | 2024 | [Adaptive Self-training Framework for Fine-grained Scene Graph Generation](https://openreview.net/pdf?id=WipsLtH77t) · ICLR 2024 | 장면 그래프 생성(SGG) 모델은 벤치마크 데이터셋의 관계(술어) 분포가 긴 꼬리 모양으로 치우친 문제와 주석이 빠진 문제를 겪는다. 주석이 없는 트리플렛(주어·술어·목적어 묶음)을 활용해 긴 꼬리 문제를 줄이려고, 주석 없는 트리플렛에 의사 라벨을 붙이고 이를 바탕으로 SGG 모델을 학습시키는 자기 학습 틀 ST-SGG를 제안했다. SGG는 의미의 모호함과 술어 클래스의 긴 꼬리 분포 때문에 이미지 인식보다 자기 학습 설계가 어려워, 어떤 SGG 모델에도 붙일 수 있는 의사 라벨 기법 CATM(Class-specific Adaptive Thresholding with Momentum)을 제안했고, 메시지 전달 신경망 기반 최신 SGG 모델에 자기 학습을 적용할 때 도움이 되는 그래프 구조 학습기(GSL)도 고안했다. 여러 SGG 모델에서, 특히 세분화된 술어 클래스의 성능을 높이는 효과를 확인했다.[^p5] | 1저자 K. Kim, 마지막 저자 박찬영 |
| 6 | 2025 | [Diversify-verify-adapt: Efficient and Robust Retrieval-Augmented Ambiguous Question Answering](https://doi.org/10.18653/v1/2025.naacl-long.56) · NAACL 2025 | 검색 증강 생성(RAG) 틀은 질의가 모호할 때 가능한 해석을 모두 담은 글을 찾아 그 글을 바탕으로 포괄적인 답을 만든다. 그러나 예비 연구에서 한 번의 검색은 가능한 해석을 다 담지 못해 결과 품질이 낮은 경우가 많았고, 이를 풀려고 제안된 반복 RAG는 효율이 크게 떨어진다. 이를 해결하려고 DIVA(diversify-verify-adapt) 틀을 제안했다. 먼저 검색한 글을 다양화해 여러 해석을 담고, 글의 품질을 검증한 뒤 그 품질에 맞는 가장 적합한 방식을 골라 적용한다. 모호한 질문에서 검색 품질이 낮은 문제를 다뤄 질의응답 시스템의 정확도와 강건성을 높이면서 효율도 높였다.[^p6] | 1저자 Y. In, 마지막 저자 박찬영 |
| 7 | 2023 | [Conditional Graph Information Bottleneck for Molecular Relational Learning](https://arxiv.org/abs/2305.01520) · ICML 2023 | 분자 관계 학습은 분자 쌍 사이의 상호작용 양상을 배우는 일로, 쓰임이 넓어 분자 과학에서 관심이 커졌다. 분자를 그래프로 보고 두 분자의 원자 수준 상호작용을 다루는 그래프 신경망이 성과를 거두었지만, 화합물이 고유한 화학 반응을 일으키는 작용기 같은 여러 부분 구조로 이뤄진다는 화학의 본성을 간과하는 경향이 있다. 그래프 쌍에서 핵심 부분 그래프를 찾아 상호작용 양상을 예측하는 관계 학습 틀 CGIB를 제안했다. 조건부 그래프 정보 병목 원리에 따라, 짝이 되는 그래프를 조건으로 주어진 과제에 필요한 최소한의 충분한 정보를 담은 부분 그래프를 한 그래프에서 찾는다. 분자의 핵심 부분 구조가 상호작용하는 상대 분자에 따라 달라지는 화학 반응의 본성을 모방한다고 주장하며, 실제 데이터셋의 여러 과제에서 최신 기준 방법보다 우수함을 보였다.[^p7] | 1저자 N. Lee, 마지막 저자 박찬영 |
| 8 | 2024 | [Retrieval-Retro: Retrieval-based Inorganic Retrosynthesis with Expert Knowledge](https://doi.org/10.52202/079017-0799) · NeurIPS 2024 | 무기물 역합성 계획은 화학에서 중요하지만, 유기물 역합성 계획에 비해 기계학습 적용이 적었다. 분야 전문 지식에 관한 지식 베이스에서 참조 물질을 검색하고 그 전구체(합성의 원료가 되는 물질) 정보를 암묵적으로 추출하는 Retrieval-Retro를 제안했다. 참조 물질의 전구체 정보를 그대로 쓰지 않고 여러 어텐션 층으로 암묵적으로 추출해 새로운 합성 레시피를 더 효과적으로 학습하게 했고, 검색할 때 목표 물질과 전구체 사이의 열역학적 관계를 고려했다. 이 관계는 여러 선택지 가운데 가장 가능성 높은 전구체 묶음을 찾는 데 필수인 분야 지식이다. 실험에서 역합성 계획, 특히 소재 발견에 중요한 새로운 합성 레시피 발견에서 우수함을 보였다.[^p8] | 1저자 H. Noh, 마지막 저자 박찬영 |

## 교수와 전문 분야

박찬영 교수는 서강대학교에서 Computer Science and Engineering 학사(2014), POSTECH에서 Computer Science and Engineering 박사(2019)를 받았고, 박사 학위 논문은 「Recommendation Framework via Matrix Factorization and Translation」이다.[^professor] 2017년 Microsoft Research(베이징) Social Computing Group과 NAVER Shopping에서 연구 인턴을 했고, 2019–2020년 University of Illinois Urbana-Champaign의 Computer Science에서 박사후연구원(Postdoctoral Research Fellow, host Prof. Jiawei Han)을 지냈다. KAIST에서는 2020–2025년 조교수(Assistant Professor), 2025년부터 부교수(Associate Professor)로 있고, 2025–2026년 University of California San Diego의 Computer Science and Engineering에서 방문 학자(Visiting Scholar, host Prof. Julian McAuley)로 있었다. 교수 페이지는 DSAIL 연구실장(Director)과 NanoForge AI 기술 자문(Technical Advisor)도 직함으로 적는다.[^professor]

안보과학기술대학원 교수 목록은 교수의 연구분야를 AI / Unmanned systems로, 세부 연구 분야를 AI와 Data Mining으로 적고,[^gst] 데이터사이언스대학원 구성원 페이지는 Focus Area를 데이터사이언스 방법론으로 적는다.[^gsds] 교수 페이지의 Academic service 칸은 KDD, ICLR, NeurIPS, ICML, AAAI의 Area Chair, Transactions on Machine Learning Research의 Action Editor(2026년부터), CIKM 2025 General Chair, CIKM 2023 Proceedings Chair, Korea AI4Science Gathering @ ICML 2026과 KDD 2026 Workshop on SciSoc Agents & LLMs의 조직을 적는다. Teaching 칸은 DS535 Recommender System and Machine Learning on Graphs, IE343 Statistical Machine Learning, DS503 Machine Learning for Data Science, KSE527 Deep Learning, CoE202 Basics of Artificial Intelligence를 적고, Selected talks 칸에는 진화하는 사기·악용을 위한 변화 인지 그래프 학습, 소재 발견을 위한 에이전트 AI, LLM 기반 멀티모달 시계열 분석, 인공지능 기반 scRNA-seq 데이터 분석, 그래프 학습과 생의학 데이터 응용, 그래프 신경망 기반 화학·소재 분야 연구 동향, 연속 학습 기반 범용 사용자 표현 학습, 그래프 표현 학습 같은 강연이 있다.[^professor]

교수 페이지 Awards 칸은 KAIST 부임 뒤의 항목으로 2026년 NVIDIA Academic Grant와 Google Research Award, KDD 2026 워크숍 두 곳의 Best Paper Award, 2025년 KAIST Impact Research Award (Achievement Award), 2024년 KAIST Song-Am Distinguished Research Award, 2024년 30th Samsung Humantech Paper Award Gold Prize, 2023년 KAIST 공과대학 Technology Innovation Award, NeurIPS 2023 Top Reviewer, ICML 2023 Workshop on Computational Biology Best Paper Award, KAIST Excellence in Teaching Award (2022), 산업및시스템공학과의 Best Academic Award(2024·2025)와 Best Teaching Award(2022) 등을 적는다. KAIST 부임 전 항목으로는 2018 ICDM Travel Award, 2017 Microsoft Research Asia Internship Program Award of Excellence, 2016 NAVER Ph.D. Fellowship, 2015 RecSys Challenge Top 1.1%가 있다.[^professor]

박사 학위 논문 제목이 보여 주듯 교수는 박사 과정에서 추천 시스템을 연구했다.[^professor] 논문으로 보면 지금의 전문 분야는 자기 지도 학습과 정보 병목으로 그래프 표현과 그 설명을 배우는 일(대표 논문 1·2),[^p1][^p2] 협업 필터링 추천 모델과 대형 언어 모델을 잇는 추천(대표 논문 3·4),[^p3][^p4] 장면 그래프 생성과 검색 증강 질의응답 같은 멀티모달·언어 모델 연구(대표 논문 5·6),[^p5][^p6] 그래프 학습을 분자 상호작용과 무기 소재 합성 계획에 쓰는 과학 AI(대표 논문 7·8)다.[^p7][^p8]

## 응용 분야

Research 페이지의 응용 칸(Applications & impact)은 연구실의 방법을 산업계, 스포츠, 과학 분야 협력자와 함께 적용한 영역으로 스포츠 분석(추적 데이터만으로 축구 경기 사건 탐지, 축구 수비 행동의 가치 평가, 사건 데이터와 추적 데이터의 동기화), 금융(거래 관계망으로 기업 부도 예측), 회로·EDA(대규모 넷리스트에서 하위 회로 찾기, 넷리스트와 글의 정렬), 교통·이동(연속 교통 예측, 교통 예측을 위한 시간 그래프 신경망), 소셜·온라인 미디어(사회적 관계를 고려한 사용자 표현 모델링, 시간 흐름을 고려한 가짜 뉴스 탐지), 의료(멀티모달 의료 데이터를 이종 그래프로 다루기, eRisk 우울증 조기 탐지 1위), 전자상거래·소매(클릭 기록으로 구매 예측, 이질적인 사용자 행동 예측), 검색·질의응답(모호한 질문을 위한 강건한 RAG, 차트 질의응답, 대화형 질의응답의 모호성 해소 조사)을 든다.[^research] Projects 페이지의 과제에는 금융상품 추천, 보험금 지급 예측, 거래 관계망 신용 평가, 전자상거래 사용자 행위 모델링, FDC Trace 센서 데이터 기반 이상 탐지, 납축전지 성능 예측, 사출성형 성능 예측, 설계 DB 안의 유사 회로 탐색, 다크팩토리 설계·구축, 근전도 추천 시스템 같은 산업·응용 과제가 있다.[^projects] Alumni 페이지가 적은 진로로는 LG AI Research, Genentech, Huawei Research, SK Hynix, Riiid, SkyLabs, UNC Chapel Hill 박사과정이 있고(방문 연구원 한 사람은 Meta), 석사 졸업생 23명 가운데 15명은 KAIST DSAIL 박사과정으로 적혀 있다.[^alumni]

## 구성원

2026년 10월 23일 랩 Team 페이지(메뉴 이름 Current) 기준이다. Ph.D. students 칸의 박사과정 17명, M.S. students 칸의 석사과정 9명, Undergraduate interns 칸의 학부 인턴 5명이다. 과정은 카드의 표기(Ph.D. student, Master student, Undergraduate intern)를 옮겼고, 학부 인턴의 괄호는 카드가 적은 학부 소속이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Sein Kim | 박사과정 | 3, 4 |
| Junseok Lee | 박사과정 | 1, 7 |
| Ki-Bum Kim | 박사과정 | 4, 5 |
| Yeonjun In | 박사과정 | 5, 6 |
| Yunhak Oh | 박사과정 |  |
| Sungwon Kim | 박사과정 | 2, 7 |
| Wonjoong Kim | 박사과정 |  |
| Seungyoon Choi | 박사과정 | 3 |
| Hyunsung Kim | 박사과정 |  |
| Yoonho Lee | 박사과정 | 2 |
| Junghoon Kim | 박사과정 |  |
| Heewoong Noh | 박사과정 | 8 |
| Gyoungseok Na | 박사과정 |  |
| Hyunchul Kim | 박사과정 |  |
| Jiwan Kim | 박사과정 | 4 |
| Hoyoung Choi | 박사과정 |  |
| Hongseok Kang | 박사과정 | 3, 4 |
| Sangwu Park | 석사과정 |  |
| Sangmin Park | 석사과정 |  |
| Yeonwoo Kim | 석사과정 |  |
| Chaehyun Kim | 석사과정 |  |
| Jaeryoung Ka | 석사과정 |  |
| Kunhee Lee | 석사과정 |  |
| Juho Song | 석사과정 |  |
| Geunha Jang | 석사과정 |  |
| Nayeon Lee | 석사과정 |  |
| Ilho Shin | 학부 인턴 (UG at KAIST ISE) |  |
| Jinhyeong Chun | 학부 인턴 (UG at Seoul National Univ. IE) |  |
| Yoonki Choi | 학부 인턴 (UG at Hanyang Univ. IE) |  |
| Gyuhwan Kim | 학부 인턴 (UG at KAIST CS) |  |
| HyoGeun You | 학부 인턴 (UG at KAIST ISE) |  |

## 졸업생과 이전 구성원

랩 Alumni 페이지의 124줄이다. Ph.D. 칸 3명, M.S. 칸 23명, Visitors 칸의 Visiting researcher 1명, Undergraduate interns 칸 97줄이며, 학부 인턴은 같은 사람이 여러 시기에 따로 적힌 경우가 있어 이름으로는 94명이다. 학위·과정과 시기(졸업 연·월, 인턴 학기)는 페이지의 표기이고, 진로는 페이지가 이름 옆에 적은 기관이다. 학부 인턴은 페이지가 적은 학부 소속을 과정 칸에 함께 적었다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Sangwoo Seo | Ph.D. (Aug. 2026) | LG AI Research, Republic of Korea |
| Namkyeong Lee | Ph.D. (Feb. 2026) | Genentech, USA |
| Kanghoon Yoon | Ph.D. (Aug. 2025) | Huawei Research, Singapore |
| Jimin Seo | M.S. (Aug. 2026) | SK Hynix |
| Hongseok Kang | M.S. (Aug. 2026) | KAIST (Ph.D. Student @ DSAIL) |
| Hyunchul Kim | M.S. (Feb. 2026) | KAIST (Ph.D. Student @ DSAIL) |
| Jiwan Kim | M.S. (Feb. 2026) | KAIST (Ph.D. Student @ DSAIL) |
| Hoyoung Choi | M.S. (Feb. 2026) | KAIST (Ph.D. Student @ DSAIL) |
| Yoonho Lee | M.S. (Feb. 2025) | KAIST (Ph.D. Student @ DSAIL) |
| Junghoon Kim | M.S. (Feb. 2025) | KAIST (Ph.D. Student @ DSAIL) |
| Heewoong Noh | M.S. (Feb. 2025) | KAIST (Ph.D. Student @ DSAIL) |
| Junmo Lee | M.S. (Feb. 2025) | KAIST (Ph.D Student @ Statistical Data Science Lab) |
| Jaehyeong Jeon | M.S. (Feb. 2025) | Riiid |
| Jihyeong Jung | M.S. (Aug. 2024) | SkyLabs |
| Seungyoon Choi | M.S. (Feb. 2024) | KAIST (Ph.D. Student @ DSAIL) |
| Wonjoong Kim | M.S. (Feb. 2024) | KAIST (Ph.D. Student @ DSAIL) |
| Sungwon Kim | M.S. (Feb. 2024) | KAIST (Ph.D. Student @ DSAIL) |
| Kibum Kim | M.S. (Aug. 2023) | KAIST (Ph.D. Student @ DSAIL) |
| Yeonjun In | M.S. (Aug. 2023) | KAIST (Ph.D. Student @ DSAIL) |
| Yunhak Oh | M.S. (Aug. 2023) | KAIST (Ph.D. Student @ DSAIL) |
| Sanghyun Lee | M.S. (Aug. 2023) |  |
| Junghurn Kim | M.S. (Aug. 2023) |  |
| Sukwon Yun | M.S. (Aug. 2023) | UNC Chapel Hill (Ph.D. Student) |
| Namkyeong Lee | M.S. (Feb. 2023) | KAIST (Ph.D. Student @ DSAIL) |
| Junseok Lee | M.S. (Feb. 2023) | KAIST (Ph.D. Student @ DSAIL) |
| Junyoung Ryu | M.S. (Feb. 2023) |  |
| Dongmin Hyun | Visiting researcher | Meta |
| Lazizbek Rajabboev | Undergraduate intern, UG at KAIST Math (Summer 2026) |  |
| Woojin Lee | Undergraduate intern, UG at Hanyang Univ. DS/IE (Summer 2026) |  |
| Inyoung Chae | Undergraduate intern, UG at Sungkyunkwan Univ. SME (Summer 2026) |  |
| Hyunseo Kim | Undergraduate intern, UG at KAIST ISE (Summer 2026) |  |
| Joonsuh Park | Undergraduate intern, UG at KAIST EE (Summer 2026) |  |
| Chaehyeon Chung | Undergraduate intern, UG at POSTECH CSE (Summer 2026) |  |
| Junwon Lee | Undergraduate intern, UG at Sogang Univ. MAE/CSE (Summer 2026) |  |
| Yunsung Nam | Undergraduate intern, UG at Korea Univ. IME (Summer 2026) |  |
| Jooho Son | Undergraduate intern, UG at KAIST ISE/CS (Winter 2025) |  |
| Beomjoon Ko | Undergraduate intern, UG at KAIST CS (Winter 2025) |  |
| Yuchan Lee | Undergraduate intern, UG at SKKU SME (Winter 2025) |  |
| Sihyun Lee | Undergraduate intern, UG at Korea Univ. IME/DS (Winter 2025) |  |
| Seungjoo Jung | Undergraduate intern, UG at Ajou Univ. IE (Winter 2025) |  |
| Jiyun Kim | Undergraduate intern, UG at Korea Univ. CS/BCS (Winter 2025) |  |
| Yoonki Choi | Undergraduate intern, UG at Hanyang Univ. IE (Winter 2025) |  |
| Kunhee Lee | Undergraduate intern, UG at KAIST ISE/CS (Winter 2025) |  |
| Juho Song | Undergraduate intern, UG at KAIST Math/CS (Winter 2025) |  |
| Chaehyun Kim | Undergraduate intern, UG at Yonsei Stat/CS (Winter 2025) |  |
| Seheon Kim | Undergraduate intern, UG at KAIST EE/ISE (Summer 2025) |  |
| Hyeonseong Park | Undergraduate intern, UG at KAIST ISE/CS (Summer 2025) |  |
| Yunseul Kim | Undergraduate intern, UG at KAIST ISE/CS (Summer 2025) |  |
| Nahyun Kwon | Undergraduate intern, UG at KAIST CS (Summer 2025) |  |
| Nayoung Ahn | Undergraduate intern, UG at SKKU Univ SME/Software (Summer 2025) |  |
| Minhee Hong | Undergraduate intern, UG at KAIST Math (Summer 2025) |  |
| Kangjin Lee | Undergraduate intern, UG at Hanyang Univ. IE/CS (Summer 2025) |  |
| Hayeon Park | Undergraduate intern, UG at SNU Animal Biotech/IE (Summer 2025) |  |
| Myeongjun Oh | Undergraduate intern, UG at Hanyang Univ. Chemical Engineering (Summer 2025) |  |
| Sangoh Kim | Undergraduate intern, UG at KAIST CS (Summer 2024 - Summer 2025) |  |
| Haneul Park | Undergraduate intern, UG at Yonsei ISE (Winter 2024) |  |
| Dojun Hwang | Undergraduate intern, UG at Korea CS/Stat (Winter 2024) |  |
| Youngmin Park | Undergraduate intern, UG at KAIST BCS (Winter 2024) |  |
| Yoonsol Jung | Undergraduate intern, UG at KAIST CS (Winter 2024) |  |
| Wontae Jeong | Undergraduate intern, UG at PNU Stat/Math (Winter 2024) |  |
| Chaehyun Kim | Undergraduate intern, UG at Yonsei Stat/CS (Winter 2024) |  |
| Minseok Kim | Undergraduate intern, UG at KAIST ISE (Winter 2024) |  |
| Sunwoo Hwang | Undergraduate intern, UG at SKKU AAI (Winter 2024) |  |
| Seunghyun Baek | Undergraduate intern, UG at UOS CS/Stat (Winter 2024) |  |
| Jaehyeon Shin | Undergraduate intern, UG at KHU AM/CSE (Winter 2024) |  |
| Sangoh Kim | Undergraduate intern, UG at KAIST CS (Winter 2024) |  |
| Soohwa Kwon | Undergraduate intern, UG at SKKU DS (Summer 2024) |  |
| Hyunkyu Kang | Undergraduate intern, UG at Korea Univ Statstics (Summer 2024) |  |
| Woocheol Shin | Undergraduate intern, UG at UNIST CSE (Summer 2024) |  |
| Yeonwoo Kim | Undergraduate intern, UG at POSTECH Math (Summer 2024) |  |
| Minjun Park | Undergraduate intern, UG at KAIST ISE (Summer 2024) |  |
| Woohyuk Kim | Undergraduate intern, UG at KAIST CS (Summer 2024) |  |
| Sejong Kim | Undergraduate intern, UG at KAIST ISE (Summer 2024) |  |
| Sangoh Kim | Undergraduate intern, UG at KAIST CS (Summer 2024) |  |
| Bonwoo Koo | Undergraduate intern, UG at KAIST ISE (Winter 2022 - Winter 2023) |  |
| Yeongmin Kim | Undergraduate intern, UG at KAIST CS (Winter 2022 - Winter 2023) |  |
| Hongseok Kang | Undergraduate intern, UG at KAIST CS (Winter 2022 - Winter 2023) |  |
| Eunhak Choi | Undergraduate intern, UG at Hanyang Univ IE (Winter 2023) |  |
| Jaemin Han | Undergraduate intern, UG at KAIST Mathsci (Winter 2023) |  |
| Seungan Jung | Undergraduate intern, UG at KAIST CS (Winter 2023) |  |
| Haejoon Lee | Undergraduate intern, UG at KAIST CS (Winter 2023) |  |
| Minseok Yun | Undergraduate intern, UG at SKKU AE (Winter 2023) |  |
| Jonggeun Lee | Undergraduate intern, UG at Korea Univ IME (Winter 2023) |  |
| Suchan Lee | Undergraduate intern, UG at POSTECH IME (Winter 2023) |  |
| Seokwon Han | Undergraduate intern, UG at KAIST CS (Winter 2023) |  |
| Junyoung Kim | Undergraduate intern (Winter 2023) |  |
| Jimin Seo | Undergraduate intern, UG at SNU CS (Winter 2023) |  |
| Chaemin Jang | Undergraduate intern, UG at KAIST CS (Winter 2022 - Summer 2023) |  |
| Sangwu Park | Undergraduate intern, UG at CAU Applied Statistics (Summer 2023) |  |
| Hyunchul Kim | Undergraduate intern, UG at Sogang Univ. CSE (Summer 2023) |  |
| Jiwan Kim | Undergraduate intern, SNU Stat/CS (Summer 2023) |  |
| Geonwoo Kim | Undergraduate intern, UG at KAIST EE (Summer 2023) |  |
| Seoung Choi | Undergraduate intern, UG at KAIST CS (Summer 2023) |  |
| Sangmin Park | Undergraduate intern, UG at KAIST CS (Summer 2023) |  |
| Hyewon Ryu | Undergraduate intern, UG at Korea Univ. IE (Summer 2023) |  |
| Jinhyeok Park | Undergraduate intern, UG at Hanyang Univ. IE (Summer 2023) |  |
| Inseon Ji | Undergraduate intern, UG at KAIST Math (Winter 2022) |  |
| Sanha Jang | Undergraduate intern, UG at KAIST College of Business (Winter 2022) |  |
| Jungwoo Lee | Undergraduate intern, UG at KAIST ISE (Winter 2022) |  |
| Jihwan Oh | Undergraduate intern, UG at UNIST IE (Winter 2022) |  |
| Taejun Yang | Undergraduate intern, UG at KAIST ISE (Winter 2022) |  |
| Joongchan An | Undergraduate intern, UG at Hanyang Univ. IE (Winter 2022) |  |
| Jihwan Bae | Undergraduate intern, UG at Korea IE (Winter 2022) |  |
| Yisak Kim | Undergraduate intern, UG at KAIST ISE (Winter 2022) |  |
| Seohyun Lim | Undergraduate intern, UG at SKKU GLD (Winter 2022) |  |
| Juheon Han | Undergraduate intern, UG at KAIST ISE (Summer 2022) |  |
| Seonghun Hong | Undergraduate intern, UG at KAIST ISE (Summer 2022) |  |
| Youngro Kim | Undergraduate intern, UG at KAIST ISE (Summer 2022) |  |
| Jinyoung Hong | Undergraduate intern, UG at KAIST ISE (Summer 2022) |  |
| Sangmin Lee | Undergraduate intern, UG at SNU IE (Summer 2022) |  |
| Kyuhyeok Seo | Undergraduate intern, UG at SNU IE (Summer 2022) |  |
| Jeehong Kim | Undergraduate intern, UG at Korea IE (Summer 2022) |  |
| Hoyoung Choi | Undergraduate intern, UG at KAIST ISE (Winter 2021) |  |
| Suyeon Lee | Undergraduate intern, UG at KAIST ISE (Winter 2021) |  |
| Daeyoung Kim | Undergraduate intern, UG at Korea IE (Winter 2021) |  |
| Jaewon Jung | Undergraduate intern, UG at Postech IE (Winter 2021) |  |
| Jongbok Lee | Undergraduate intern, UG at KAIST ISE (Winter 2021) |  |
| Han Kim | Undergraduate intern, UG at KAIST ISE (Winter 2021) |  |
| Jaeyoung Lee | Undergraduate intern, UG at KAIST Math (Summer 2021) |  |
| Sujin Kim | Undergraduate intern, UG at KAIST ISE (Summer 2021) |  |
| Hyemin Ju | Undergraduate intern, UG at KAIST ISE (Summer 2021) |  |
| Hanbit Lee | Undergraduate intern, UG at KAIST ISE (Summer 2021) |  |
| Hyojun Kim | Undergraduate intern, UG at Kyunghee Univ. IE (Summer 2021) |  |
| Jae-Hyun Nam | Undergraduate intern, UG at SNU IE/Math (Winter 2020 - Spring 2021) |  |

## 최근 논문 목록 (2021–2026)

랩 Publications 페이지의 2021–2026년 논문 148편 가운데 145편이다. 학회 본 논문(Main conference) 88편, 학술지 논문 6편, 워크숍 논문 44편, 사전 공개 논문(Preprint) 7편이며, 연도마다 학회 본 논문과 학술지 논문, 워크숍 논문, 사전 공개 논문 순서로 적었다. 제목·저자·학회와 학술지 표기는 페이지 그대로이고, 같은 연구가 다른 곳에도 실렸다는 페이지의 표시는 「also appeared in」으로 옮겼다. 2026년 구역의 NeurIPS 2026 본 논문 9편과 워크숍 논문 4편(AI4Science 1편, AI4Mat 3편)은 News 페이지가 2026년 9월에 채택을 알린 논문으로, 학회(2026년 12월 6–12일) 발표 전이라 「NeurIPS 2026 채택」을 붙여 출판 논문과 구분했다.[^pubs][^news][^neurips] CIKM 2026 논문 4편은 News 페이지가 2026년 8월에 채택을 알린 논문이고, NeurIPS 2026 Workshop (GenAI4Health)의 1편은 페이지에 학회 이름만 적혀 있다.[^pubs][^news] 교수는 2020년부터 KAIST에 있어 모두 KAIST 재직 시기의 논문이다.[^professor]

**2026**

- Gyoung S. Na, Chanyoung Park. "Complex-Valued Periodic Stochastic Processes for Retrieving Unknown Atomic Structures". *NeurIPS 2026 (NeurIPS 2026 채택) · also appeared in ICML 2026 AI for Science Workshop*.
- Sein Kim, Sangwu Park, HongSeok Kang, Wonjoong Kim, Jimin Seo, Yeonjun In, Kanghoon Yoon, Hyunsik Jeon, Chanyoung Park. "Self-EvolveRec: Self-Evolving Recommender Systems with LLM-based Directional Feedback". *NeurIPS 2026 (NeurIPS 2026 채택) · also appeared in KDD 2026 Workshop (Agentic SE), ICLR 2026 Workshop (RSI)*.
- Wonjoong Kim, Yeonjun In, Sangwu Park, Dongha Lee, Chanyoung Park. "PAIR: Prefix-Aware Internal Reward Model for Multi-Turn Agent Optimization". *NeurIPS 2026 (NeurIPS 2026 채택)*.
- Junghoon Kim, Seungyoon Choi, Hyunsung Kim, Chanyoung Park. "Chasing Label Shifters: A Change-Aware Framework for Dynamic Graph Node Classification". *NeurIPS 2026 (NeurIPS 2026 채택)*.
- Heewoong Noh, Gyoung S. Na, Namkyeong Lee, Chanyoung Park. "A Structured LLM Framework for Inorganic Material Synthesis Planning". *NeurIPS 2026 (NeurIPS 2026 채택) · also appeared in KDD 2026 Workshop (Agentic AI for Science), ICLR 2026 Workshop (AI4Mat, as MSP-LLM)*.
- Yeonjun In, Wonjoong Kim, Sangwu Park, Kanghoon Yoon, Chanyoung Park. "Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-Horizon Agents". *NeurIPS 2026 (NeurIPS 2026 채택) · also appeared in KDD 2026 Workshop (PILA, Best Paper Award)*.
- Yoonho Lee, Yunhak Oh, Hoyoung Choi, Chanyoung Park. "Screening Lipid Nanoparticles through Structure-Ratio Alignment". *NeurIPS 2026 (NeurIPS 2026 채택)*.
- Yunhak Oh, Yoonho Lee, Junseok Lee, Namkyeong Lee, Sang-Yeon Hwang, Yinhua Piao, Hyomin Kim, Seonghwan Kim, Jaechang Lim, Woo Youn Kim, Sungsoo Ahn, Chanyoung Park. "scTrilemma: Balancing Identity, Invariance, and Fidelity in Single-Cell Representation Learning". *NeurIPS 2026 (NeurIPS 2026 채택) · also appeared in NeurIPS 2026 Workshop (GenAI4Health)*.
- Sungho Park, Wonjoong Kim, Rongyuan Tan, Jue Zhang, Wook-Shin Han, Pengfei Gao, Chanyoung Park, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang. "AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces". *NeurIPS 2026 (NeurIPS 2026 채택)*.
- Seungyoon Choi, Hyunchul Kim, Jae-Gil Lee, Chanyoung Park. "Compositional Spectral Prompts for LLM-based Online Time Series Forecasting". *CIKM 2026 · also appeared in KDD 2026 Workshop (MiLeTS)*.
- Hyunsung Kim, Hoyoung Choi, Kunhee Lee, Sangwoo Seo, Tom Boomstra, Jinsung Yoon, Chanyoung Park. "ELASTIC: Trajectory-Based Synchronization of Event and Tracking Data in Soccer". *CIKM 2026 · also appeared in ECML-PKDD 2025 Workshop (MLSA, Oral)*.
- Junghoon Kim, Hyunsung Kim, Seungyoon Choi, Kyoungyong Park, Jihun Lee, Yonggu Ji, Chanyoung Park. "DefaultGNN: A Dual-Perspective GNN Framework for Predicting Corporate Default from Buyer-Seller Transaction Networks". *CIKM 2026 (Applied Research Track)*.
- Chaehyun Kim, Sein Kim, Hongseok Kang, Chanyoung Park. "A Behavioral Trait Leaks into Preferences: Diagnosing Trait Interference in LLM User Simulators". *CIKM 2026 (Short paper)*.
- Ilho Shin, Hyunchul Kim, Chanyoung Park. "HUGETIME at eRisk 2026: Bucket-wise Evidence Pruning for Contextualized Early Depression Detection". *CLEF 2026 (Ranked 1st, eRisk Task 2)*.
- Kibum Kim, Jiwan Kim, Kyle Min, Yueqi Wang, Jinyoung Moon, Julian McAuley, Chanyoung Park. "Sink-Token-Aware Pruning for Fine-Grained Video Understanding in Efficient Video LLMs". *ECCV 2026*.
- Jiwan Kim, Kibum Kim, Wonjoong Kim, Byung-Kwan Lee, Chanyoung Park. "Why and When Visual Token Pruning Fails? A Study on Relevant Visual Information Shift in MLLMs Decoding". *ECCV 2026 · also appeared in KDD 2026 Workshop (RelKD)*.
- Hyunsung Kim, Kunhee Lee, Sangwoo Seo, Sang-Ki Ko, Jinsung Yoon, Chanyoung Park. "PathCRF: Ball-Free Soccer Event Detection via Possession Path Inference from Player Trajectories". *KDD 2026*.
- Namkyeong Lee, Heewoong Noh, Gyoung S. Na, Jimeng Sun, Tianfan Fu, Marinka Zitnik, Chanyoung Park. "Learning Probabilistic Compositional Representation of Crystalline Materials". *KDD 2026 (AI for Science Track) · also appeared in NeurIPS 2023 AI4Science Workshop (as PolySRL)*.
- Sungwon Kim, Juho Song, Seungmin Shin, Guimok Cho, Sangkook Kim, Chanyoung Park. "EqGINO: Equivariant Geometry-Informed Fourier Neural Operators for 3D PDEs". *ICML 2026 · also appeared in ICLR 2026 Workshop AI4PDE (Oral)*.
- Wonjoong Kim, Sangwu Park, Yeonjun In, Sein Kim, Dongha Lee, Chanyoung Park. "Beyond the Final Answer: Evaluating the Reasoning Trajectories of Tool-Augmented Agents". *ICML 2026 · also appeared in KDD 2026 Workshop (Agentic AI Evaluation)*.
- Yinhua Piao, Hyomin Kim, Seonghwan Kim, Yunhak Oh, Junhyeok Jeon, Sang-Yeon Hwang, Jaechang Lim, Woo Youn Kim, Chanyoung Park, Sungsoo Ahn. "Learning Adaptive Perturbation-Conditioned Contexts for Robust Transcriptional Response Prediction". *ICML 2026 · also appeared in ICLR 2026 Workshop (GEM)*.
- Jihye Na, Patara Trirat, Chanyoung Park, Jae-Gil Lee. "Time-PEFT: Temporal and Multichannel Complexity-Based Fine-Tuning for Time-Series Foundation Models". *ICML 2026*.
- Kanghoon Yoon, Minsub Kim, Sungjae Lee, Joonhyung Lee, Sunghyeon Woo, Yeonjun In, Se Jung Kwon, Chanyoung Park, Dongsoo Lee. "SelfJudge: Faster Speculative Decoding via Self-Supervised Judge Verification". *ICML 2026*.
- Yeonjun In, Wonjoong Kim, Sangwu Park, Chanyoung Park. "Reasoning Structure Matters for Safety Alignment of Reasoning Models". *ACL 2026*.
- Heewoong Noh, Namkyeong Lee, Gyoung S. Na, Kibum Kim, Chanyoung Park. "IR-Agent: Expert-Inspired LLM Agents for Structure Elucidation from Infrared Spectra". *ICLR 2026*.
- Jiwan Kim, Kibum Kim, Sangwoo Seo, Chanyoung Park. "CompoDistill: Attention Distillation for Compositional Reasoning in Multimodal LLMs". *ICLR 2026*.
- Kibum Kim, Sein Kim, HongSeok Kang, Jiwan Kim, Heewoong Noh, Yeonjun In, Kanghoon Yoon, Jinoh Oh, Julian McAuley, Chanyoung Park. "Token-Efficient Item Representation via Images for LLM Recommender Systems". *ICLR 2026*.
- Hyunsung Kim, Sangwoo Seo, Hoyoung Choi, Tom Boomstra, Jinsung Yoon, Chanyoung Park. "Better Prevent than Tackle: Valuing Defense in Soccer Based on Graph Neural Networks". *SSAC 2026*.
- Doyun Choi, Cheonwoo Lee, Biniyam Aschalew Tolera, Taewook Ham, Chanyoung Park, Jaemin Yoo. "PULSE: Socially-Aware User Representation Modeling Toward Parameter-Efficient Graph Collaborative Filtering". *WWW 2026*.
- Yongjoon Choe, Sungwon Kim, Susan E. Burns, Chanyoung Park. "Physics-Embedded Graph Neural Operator for Interaction-Controlled Colloidal Aggregation". *Water Research 2026 · also appeared in KDD 2026 Workshop (RelSciFM, Best Paper Award)*.
- Junghoon Kim, Junmo Lee, Yeonjun In, Kanghoon Yoon, Chanyoung Park. "A New DAWN for Fake News Detection: Leveraging Engagement Earliness for Temporality-aware Evaluation". *ACM TIST 2026 · also appeared in WSDM 2025 (conference version)*.
- Gyoung S. Na, Chanyoung Park. "Machine Collective Intelligence with Canonical Syntax Representations for Explainable Scientific Discovery". *NeurIPS 2026 AI4Science Workshop (NeurIPS 2026 채택)*.
- Jaewon Bae, Seungyun Shin, Chanyoung Park. "Bridging Prediction and Planning: From Synthesis Temperature Distributions to Optimization-Guided Experiments". *NeurIPS 2026 Workshop (AI4Mat) (NeurIPS 2026 채택)*.
- Woojin Bae, Hyunsung Jang, Jaewon Bae, Chanyoung Park. "Combining Physical and Retrieved Empirical Priors for Solid-State Synthesis Condition Prediction". *NeurIPS 2026 Workshop (AI4Mat) (NeurIPS 2026 채택)*.
- Kunmin Jang, Dongin Kim, Woojin Bae, Jaewon Bae, Chanyoung Park. "A Structure-to-Density Model for Trajectory-Free Lithium Transport Screening". *NeurIPS 2026 Workshop (AI4Mat) (NeurIPS 2026 채택)*.
- Jimin Seo, HongSeok Kang, Sein Kim, Jiwan Kim, Chanyoung Park. "Revisiting CF-Integrated LLM Recommenders through Dimensional Collapse". *KDD 2026 Workshop (GSALO)*.
- Sein Kim, Sangwu Park, HongSeok Kang, Wonjoong Kim, Jimin Seo, Yeonjun In, Kanghoon Yoon, Hyunsik Jeon, Chanyoung Park. "Self-EvolveRec: Self-Evolving Recommender Systems with LLM-based Directional Feedback". *KDD 2026 Workshop (Agentic SE) · also appeared in ICLR 2026 Workshop (RSI), NeurIPS 2026 (conference version)*.
- Yeonjun In, Mehrab Tanjim, Jayakumar Subramanian, Sungchul Kim, Uttaran Bhattacharya, Wonjoong Kim, Sangwu Park, Somdeb Sarkhel, Chanyoung Park. "Rethinking Failure Attribution in Multi-Agent Systems: A Multi-Perspective Benchmark and Evaluation". *ICML 2026 Workshop (Failure Modes of Agentic AI) · also appeared in KDD 2026 Workshop (Agentic SE)*.
- Yeonjun In, Wonjoong Kim, Sangwu Park, Kanghoon Yoon, Chanyoung Park. "Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-Horizon Agents". *KDD 2026 Workshop (PILA) (Best Paper Award) · also appeared in NeurIPS 2026 (conference version)*.
- Heewoong Noh, Gyoung S. Na, Namkyeong Lee, Chanyoung Park. "A Structured LLM Framework for Inorganic Material Synthesis Planning". *KDD 2026 Workshop (Agentic AI for Science) · also appeared in NeurIPS 2026 (conference version)*.
- Sangwoo Seo, Hyunsung Kim, Jiwan Kim, Chanyoung Park. "Adaptive Graph Rewiring to Mitigate Over-Squashing in Mesh-Based GNNs for Fluid Dynamics Simulations". *KDD 2026 Workshop (RelSciFM)*.
- Sangwoo Seo, Hyunsung Kim, Hyunchul Kim, Byeonggon Kang, Rex Ying, Chanyoung Park. "Bridging Circuit Graphs and Language: A Cross-Modal Transformer for Netlist-to-Text Alignment and Generation". *KDD 2026 Workshop (Graph ML for Large Models)*.
- Junseok Lee, Yunhak Oh, Namkyeong Lee, Hyunchul Kim, Chanyoung Park. "Tokenizing Antibody-Antigen Complex Structures via Energy-Based Surrogates". *KDD 2026 Workshop (RelSciFM)*.
- Juhan Hong, Hyunsung Jang, Woojin Bae, Jaewon Bae, Chanyoung Park. "Retro-Forge: A Multi-Step Pairwise Retrosynthesis Framework for Solid-State Materials Synthesis". *ICML 2026 AI for Science Workshop*.
- Gyoung S. Na, Chanyoung Park. "Periodic Complex Stochastic Processes for Retrieving Atomic Structures of Unknown Matters". *ICML 2026 AI for Science Workshop · also appeared in NeurIPS 2026 (conference version)*.
- Sujong Lee, Jaewon Bae, Seungyun Shin, Heesung Choi, Chanyoung Park. "Density of States-Intermediated Crystal Generation for Material Inverse Design". *ICML 2026 AI for Science Workshop*.
- Sangwu Park, Wonjoong Kim, Yeonjun In, Sein Kim, Hongseok Kang, Chanyoung Park. "Test-Time Training for Visual Foresight Vision-Language-Action Models". *ICML 2026 Workshop (Continual Adaptation at Scale)*.
- Hyomin Kim, Sang-Yeon Hwang, Jaechang Lim, Yinhua Piao, Yunhak Oh, Woo Youn Kim, Chanyoung Park, Sungsoo Ahn, Junhyeok Jeon. "Progressive Multi-Agent Reasoning for Biological Perturbation Prediction". *ICML 2026 Workshop (GenBio)*.
- Heewoong Noh, Gyoung S. Na, Namkyeong Lee, Chanyoung Park. "MSP-LLM: A Unified Large Language Model Framework for Complete Material Synthesis Planning". *ICLR 2026 Workshop (AI4Mat) · also appeared in NeurIPS 2026 (conference version)*.
- Kunmin Jang, Dongik Park, Jaewon Bae, Chanyoung Park. "Synergistic Multi-Task Learning for Electronic Density of States Prediction". *ICLR 2026 Workshop (AI4Mat)*.
- Dongik Park, Kunmin Jang, Jaewon Bae, Dongin Kim, Chanyoung Park. "Learning k-Resolved Electronic Structure via Soft Energy Occupancy Prediction". *ICLR 2026 Workshop (AI4Mat)*.
- Seungyoon Choi, Hyunchul Kim, Jae-Gil Lee, Chanyoung Park. "Compositional Spectral Prompts for LLM-based Online Time Series Forecasting". *KDD 2026 Workshop (MiLeTS) · also appeared in CIKM 2026 (conference version)*.
- Jiwan Kim, Kibum Kim, Wonjoong Kim, Byung-Kwan Lee, Chanyoung Park. "Why and When Visual Token Pruning Fails? A Study on Relevant Visual Information Shift in MLLMs Decoding". *KDD 2026 Workshop (RelKD) · also appeared in ECCV 2026 (conference version)*.
- Sungwon Kim, Juho Song, Seungmin Shin, Guimok Cho, Sangkook Kim, Chanyoung Park. "EqGINO: Equivariant Geometry-Informed Fourier Neural Operators for 3D PDEs". *ICLR 2026 Workshop (AI4PDE) (Oral) · also appeared in ICML 2026 (conference version)*.
- Wonjoong Kim, Sangwu Park, Yeonjun In, Sein Kim, Dongha Lee, Chanyoung Park. "Beyond the Final Answer: Evaluating the Reasoning Trajectories of Tool-Augmented Agents". *KDD 2026 Workshop (Agentic AI Evaluation) · also appeared in ICML 2026 (conference version)*.
- Yinhua Piao, Hyomin Kim, Seonghwan Kim, Yunhak Oh, Junhyeok Jeon, Sang-Yeon Hwang, Jaechang Lim, Woo Youn Kim, Chanyoung Park, Sungsoo Ahn. "Learning Adaptive Perturbation-Conditioned Contexts for Robust Transcriptional Response Prediction". *ICLR 2026 Workshop (GEM) · also appeared in ICML 2026 (conference version)*.
- Yongjoon Choe, Sungwon Kim, Susan E. Burns, Chanyoung Park. "Physics-Embedded Graph Neural Operator for Interaction-Controlled Colloidal Aggregation". *KDD 2026 Workshop (RelSciFM) (Best Paper Award) · also appeared in Water Research 2026 (journal version)*.
- Sein Kim, Sangwu Park, HongSeok Kang, Wonjoong Kim, Jimin Seo, Yeonjun In, Kanghoon Yoon, Hyunsik Jeon, Chanyoung Park. "Self-EvolveRec: Self-Evolving Recommender Systems with LLM-based Directional Feedback". *ICLR 2026 Workshop (RSI) · also appeared in KDD 2026 Workshop (Agentic SE) (workshop version), NeurIPS 2026 (conference version)*.
- Yeonjun In, Mehrab Tanjim, Jayakumar Subramanian, Sungchul Kim, Uttaran Bhattacharya, Wonjoong Kim, Sangwu Park, Somdeb Sarkhel, Chanyoung Park. "Rethinking Failure Attribution in Multi-Agent Systems: A Multi-Perspective Benchmark and Evaluation". *KDD 2026 Workshop (Agentic SE) · also appeared in ICML 2026 Workshop (Failure Modes of Agentic AI) (workshop version)*.
- Yunhak Oh, Yoonho Lee, Junseok Lee, Namkyeong Lee, Sang-Yeon Hwang, Yinhua Piao, Hyomin Kim, Seonghwan Kim, Jaechang Lim, Woo Youn Kim, Sungsoo Ahn, Chanyoung Park. "scTrilemma: Balancing Identity, Invariance, and Fidelity in Single-Cell Representation Learning". *NeurIPS 2026 Workshop (GenAI4Health) · also appeared in NeurIPS 2026 (conference version)*.
- Sangwu Park, Wonjoong Kim, Yeonjun In, Chanyoung Park. "Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models". *Preprint(사전 공개본)*.
- Heewoong Noh, Gyoung S. Na, Elton Pan, Namkyeong Lee, Chanyoung Park. "CondMSP: Condition-Informed and Resource-Aware Inorganic Materials Synthesis Planning". *Preprint(사전 공개본)*.
- Sangwu Park, Yeonjun In, Wonjoong Kim, Sungwon Kim, Sein Kim, Chanyoung Park. "ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation". *Preprint(사전 공개본)*.
- Sungho Park, Wonjoong Kim, Jue Zhang, Wook-Shin Han, Pengfei Gao, Chanyoung Park, Yongqiang Yao, Rao Fu, Elsie Nallipogu, Qingwei Lin, Victor Rühle. "ActiveSaddler: Automated Curriculum Learning for Agent Harness Optimization". *Preprint(사전 공개본)*.
- Jeongeun Lee, Chanyoung Park, Dongha Lee. "Personalizing Embodied Multimodal Large Language Model Agents over Long-term User Interactions". *Preprint(사전 공개본)*.

**2025**

- Namkyeong Lee, Yunhak Oh, Heewoong Noh, Gyoung S. Na, Minkai Xu, Hanchen Wang, Tianfan Fu, Chanyoung Park. "3D Interaction Geometric Pre-training for Molecular Relational Learning". *NeurIPS 2025 (Spotlight) · also appeared in NeurIPS 2024 Workshop (AIDrugX)*.
- Yoonho Lee, Junseok Lee, Sangwoo Seo, Sungwon Kim, Yeongmin Kim, Chanyoung Park. "Disentangling Hyperedges through the Lens of Category Theory". *NeurIPS 2025 · also appeared in ICLR 2025 MLGenX Workshop*.
- Yeonjun In, Kanghoon Yoon, Sukwon Yun, Kibum Kim, Sungchul Kim, Chanyoung Park. "Training Robust Graph Neural Networks by Modeling Noise Dependencies". *NeurIPS 2025 · also appeared in WWW 2024 DCAI Workshop (Oral)*.
- Yeonjun In, Wonjoong Kim, Kanghoon Yoon, Sungchul Kim, Mehrab Tanjim, Kibum Kim, Chanyoung Park. "Is Safety Standard Same for Everyone? User-Specific Safety Evaluation of Large Language Models". *EMNLP 2025 (Findings) · also appeared in NeurIPS 2025 Workshop (Reliable ML)*.
- Md Mehrab Tanjim, Yeonjun In, Xiang Chen, Victor S. Bursztyn, Ryan A. Rossi, Sungchul Kim, Guang-Jie Ren, Vaishnavi Muppala, Shun Jiang, Yongsung Kim, Chanyoung Park. "Disambiguation in Conversational Question Answering in the Era of LLM: A Survey". *EMNLP 2025*.
- Sangwoo Seo, Jimin Seo, Yoonho Lee, Donghyeon Kim, Hyejin Shin, Banghyun Sung, Chanyoung Park. "Target Circuit Matching in Large-Scale Netlists using GNN-Based Region Prediction". *ICCAD 2025*.
- Sein Kim, Hongseok Kang, Kibum Kim, Jiwan Kim, Donghyun Kim, Minchul Yang, Kwangjin Oh, Julian McAuley, Chanyoung Park. "Lost in Sequence: Do Large Language Models Understand Sequential Recommendation?". *KDD 2025*.
- Sukwon Yun, Xin Liu, Yunhak Oh, Junseok Lee, Tianlong Chen, Tsuyoshi Murata, Chanyoung Park. "Oldie but Goodie: Re-illuminating Label Propagation on Graphs with Partially Observed Features". *KDD 2025*.
- Gyoung S. Na, Chanyoung Park. "Electron-Informed Coarse-Graining Molecular Representation Learning for Real-World Molecular Physics". *KDD 2025 · also appeared in NeurIPS 2023 AI4Science Workshop*.
- Hyeonsoo Jo, Hyunjin Hwang, Fanchen Bu, Soo Yong Lee, Chanyoung Park, Kijung Shin. "On Measuring Unnoticeability of Graph Adversarial Attacks: Observations, New Measure, and Applications". *KDD 2025*.
- Sungwon Kim, Namkyeong Lee, Yunyoung Doh, Seungmin Shin, Guimok Cho, Seung-Won Jeon, Sangkook Kim, Chanyoung Park. "Thickness-aware E(3)-Equivariant 3D Mesh Neural Networks". *ICML 2025*.
- Yunhak Oh, Junseok Lee, Yeongmin Kim, Sangwoo Seo, Namkyeong Lee, Chanyoung Park. "Global Context-aware Representation Learning for Spatially Resolved Transcriptomics". *ICML 2025*.
- Jiwan Kim, Hongseok Kang, Sein Kim, Kibum Kim, Chanyoung Park. "Disentangling and Generating Modalities for Recommendation in Missing Modality Scenarios". *SIGIR 2025*.
- Seungyoon Choi, Sein Kim, Hongseok Kang, Wonjoong Kim, Chanyoung Park. "Dynamic Time-aware Continual User Representation Learning". *SIGIR 2025*.
- Sungwon Kim, Yoonho Lee, Yunhak Oh, Namkyeong Lee, Sukwon Yun, Junseok Lee, Sein Kim, Carl Yang, Chanyoung Park. "Subgraph Federated Learning for Local Generalization". *ICLR 2025 (Oral) · also appeared in KDD 2024 FedKDD Workshop (Best Paper Award)*.
- Kibum Kim, Kanghoon Yoon, Yeonjun In, Jaehyeong Jeon, Jinyoung Moon, Donghyun Kim, Chanyoung Park. "Weakly Supervised Video Scene Graph Generation via Natural Language Supervision". *ICLR 2025*.
- Gyoung S. Na, Chanyoung Park. "Self-Supervised Diffusion Models for Electron-Aware Molecular Representation Learning". *ICLR 2025*.
- Yeonjun In, Sungchul Kim, Ryan A. Rossi, Mehrab Tanjim, Tong Yu, Ritwik Sinha, Chanyoung Park. "Diversify-verify-adapt: Efficient and Robust Retrieval-Augmented Ambiguous Question Answering". *NAACL 2025*.
- Wonjoong Kim, Sangwu Park, Yeonjun In, Seokwon Han, Chanyoung Park. "SIMPLOT: Enhancing Chart Question Answering by Distilling Essentials". *NAACL 2025 (Findings)*.
- Kanghoon Yoon, Kibum Kim, Jaehyeong Jeon, Yeonjun In, Donghyun Kim, Chanyoung Park. "RA-SGG: Retrieval-Augmented Scene Graph Generation Framework via Multi-Prototype Learning". *AAAI 2025*.
- Junghoon Kim, Junmo Lee, Yeonjun In, Kanghoon Yoon, Chanyoung Park. "Revisiting Fake News Detection: Towards Temporality-aware Evaluation by Leveraging Engagement Earliness". *WSDM 2025 (Oral) · also appeared in ACM TIST 2026 (journal version)*.
- Kibum Kim, Kyle Min, Chanyoung Park. "Data Scaling Isn't Enough: Towards Improving Compositional Reasoning in Video-Language Models". *NeurIPS 2025 Workshop (MAR) (Spotlight)*.
- Hyunsung Kim, Hoyoung Choi, Kunhee Lee, Sangwoo Seo, Tom Boomstra, Jinsung Yoon, Chanyoung Park. "ELASTIC: Trajectory-Based Synchronization of Event and Tracking Data in Soccer". *ECML-PKDD 2025 Workshop (MLSA) (Oral) · also appeared in CIKM 2026 (conference version)*.
- Yoonho Lee, Junseok Lee, Sangwoo Seo, Sungwon Kim, Yeongmin Kim, Chanyoung Park. "Disentangling Hyperedges through the Lens of Category Theory". *ICLR 2025 MLGenX Workshop · also appeared in NeurIPS 2025 (conference version)*.
- Yeonjun In, Wonjoong Kim, Kanghoon Yoon, Sungchul Kim, Mehrab Tanjim, Kibum Kim, Chanyoung Park. "Is Safety Standard Same for Everyone? User-Specific Safety Evaluation of Large Language Models". *NeurIPS 2025 Workshop (Reliable ML) · also appeared in EMNLP 2025 (conference version)*.

**2024**

- Heewoong Noh, Namkyeong Lee, Gyoung S. Na, Chanyoung Park. "Retrieval-Retro: Retrieval-based Inorganic Retrosynthesis with Expert Knowledge". *NeurIPS 2024*.
- Kanghoon Yoon, Yeonjun In, Namkyeong Lee, Kibum Kim, Chanyoung Park. "Debiased Graph Poisoning Attack via Contrastive Surrogate Objective". *CIKM 2024*.
- Namkyeong Lee, Siddhartha Laghuvarapu, Chanyoung Park, Jimeng Sun. "Vision Language Model is NOT All You Need: Augmentation Strategies for Molecule Language Models". *CIKM 2024 · also appeared in ACL 2024 Language+Molecules Workshop*.
- Jaehyeong Jeon, Kibum Kim, Kanghoon Yoon, Chanyoung Park. "Semantic Diversity-aware Prototype-based Learning for Unbiased Scene Graph Generation". *ECCV 2024*.
- Sukwon Yun, Jie Peng, Alexandro Trevino, Chanyoung Park, Tianlong Chen. "Mew: Multiplexed Immunofluorescence Image Analysis through an Efficient Multiplex Network". *ECCV 2024*.
- Sein Kim, Hongseok Kang, Seungyoon Choi, Donghyun Kim, Minchul Yang, Chanyoung Park. "Large Language Models meet Collaborative Filtering: An Efficient All-round LLM-based Recommender System". *KDD 2024*.
- Sangwoo Seo, Sungwon Kim, Jihyeong Jung, Yoonho Lee, Chanyoung Park. "Self-Explainable Temporal Graph Networks based on Graph Information Bottleneck". *KDD 2024*.
- Jihyeong Jung, Sangwoo Seo, Sungwon Kim, Chanyoung Park. "Unsupervised Episode Generation for Graph Meta-learning". *ICML 2024*.
- Kibum Kim, Kanghoon Yoon, Jaehyeong Jeon, Yeonjun In, Jinyoung Moon, Donghyun Kim, Chanyoung Park. "LLM4SGG: Large Language Models for Weakly Supervised Scene Graph Generation". *CVPR 2024*.
- Yeonjun In, Kanghoon Yoon, Kibum Kim, Kijung Shin, Chanyoung Park. "Self-guided Robust Graph Structure Refinement". *WWW 2024 (Oral)*.
- Seungyoon Choi, Wonjoong Kim, Sungwon Kim, Yeonjun In, Sein Kim, Chanyoung Park. "DSLR: Diversity Enhancement and Structure Learning for Rehearsal-based Graph Continual Learning". *WWW 2024 (Oral)*.
- Kibum Kim, Kanghoon Yoon, Yeonjun In, Jinyoung Moon, Donghyun Kim, Chanyoung Park. "Adaptive Self-training Framework for Fine-grained Scene Graph Generation". *ICLR 2024*.
- Baoyu Jing, Yuchen Yan, Kaize Ding, Chanyoung Park, Yada Zhu, Huan Liu, Hanghang Tong. "Sterling: Synergistic Representation Learning on Bipartite Graphs". *AAAI 2024 (Oral)*.
- Junseok Lee, Sukwon Yun, Yeongmin Kim, Tianlong Chen, Manolis Kellis, Chanyoung Park. "Single-cell RNA Sequencing Data Imputation Using Bi-level Feature Propagation". *Briefings in Bioinformatics 2024 (KAIST Graduate Student Outstanding Paper Award)*.
- Namkyeong Lee, Yunhak Oh, Heewoong Noh, Gyoung S. Na, Minkai Xu, Hanchen Wang, Tianfan Fu, Chanyoung Park. "3D Interaction Geometric Pre-training for Molecular Relational Learning". *NeurIPS 2024 Workshop (AIDrugX) · also appeared in NeurIPS 2025 (conference version)*.
- Yeonjun In, Kanghoon Yoon, Sukwon Yun, Kibum Kim, Sungchul Kim, Chanyoung Park. "Training Robust Graph Neural Networks by Modeling Noise Dependencies". *WWW 2024 DCAI Workshop (Oral) · also appeared in NeurIPS 2025 (conference version)*.
- Sungwon Kim, Yoonho Lee, Yunhak Oh, Namkyeong Lee, Sukwon Yun, Junseok Lee, Sein Kim, Carl Yang, Chanyoung Park. "Subgraph Federated Learning for Local Generalization". *KDD 2024 FedKDD Workshop (Best Paper Award) · also appeared in ICLR 2025 (conference version)*.
- Namkyeong Lee, Siddhartha Laghuvarapu, Chanyoung Park, Jimeng Sun. "Vision Language Model is NOT All You Need: Augmentation Strategies for Molecule Language Models". *ACL 2024 Language+Molecules Workshop · also appeared in CIKM 2024 (conference version)*.
- Sangwoo Seo, Sungwon Kim, Chanyoung Park. "Interpretable Prototype-based Graph Information Bottleneck". *KDD 2024 HIAI Workshop (Oral; Best Paper Award) · also appeared in NeurIPS 2023 (conference version)*.
- Sanghyun Lee, Chanyoung Park. "Continual Traffic Forecasting via Mixture of Experts". *Preprint(사전 공개본)*.
- Sanghyun Lee, Chanyoung Park. "Temporal Graph Learning Recurrent Neural Network for Traffic Forecasting". *Preprint(사전 공개본)*.

**2023**

- Sangwoo Seo, Sungwon Kim, Chanyoung Park. "Interpretable Prototype-based Graph Information Bottleneck". *NeurIPS 2023 (Gold Prize, Samsung Humantech) · also appeared in KDD 2024 HIAI Workshop (Oral, Best Paper Award)*.
- Namkyeong Lee, Heewoong Noh, Sungwon Kim, Dongmin Hyun, Gyoung S. Na, Chanyoung Park. "Density of States Prediction of Crystalline Materials via Prompt-guided Multi-Modal Transformer". *NeurIPS 2023 · also appeared in ICLR 2023 ML4Materials Workshop*.
- Yunhak Oh, Sukwon Yun, Dongmin Hyun, Sein Kim, Chanyoung Park. "MUSE: Music Recommender System with Shuffle Play Recommendation Enhancement". *CIKM 2023*.
- Junghoon Kim, Yeonjun In, Kanghoon Yoon, Junmo Lee, Chanyoung Park. "Class Label-aware Graph Anomaly Detection". *CIKM 2023 (Short paper)*.
- Junghurn Kim, Sukwon Yun, Chanyoung Park. "Structural Mixup for Graph Neural Networks". *CIKM 2023 (Short paper)*.
- Yeonjun In, Kanghoon Yoon, Chanyoung Park. "Similarity Preserving Adversarial Graph Contrastive Learning". *KDD 2023*.
- Namkyeong Lee, Kanghoon Yoon, Gyoung S. Na, Sein Kim, Chanyoung Park. "Shift-Robust Molecular Relational Learning with Causal Substructure". *KDD 2023*.
- Sungwon Kim, Junseok Lee, Namkyeong Lee, Wonjoong Kim, Seungyoon Choi, Chanyoung Park. "Task-Equivariant Graph Few-shot Learning". *KDD 2023*.
- Sein Kim, Namkyeong Lee, Donghyun Kim, Min-Chul Yang, Chanyoung Park. "Task Relation-aware Continual User Representation Learning". *KDD 2023*.
- Namkyeong Lee, Dongmin Hyun, Gyoung S. Na, Sungwon Kim, Junseok Lee, Chanyoung Park. "Conditional Graph Information Bottleneck for Molecular Relational Learning". *ICML 2023*.
- Kibum Kim, Dongmin Hyun, Sukwon Yun, Chanyoung Park. "MELT: Mutual Enhancement of Long-Tailed User and Item for Sequential Recommendation". *SIGIR 2023*.
- Sein Kim, Namkyeong Lee, Junseok Lee, Dongmin Hyun, Chanyoung Park. "Heterogeneous Graph Learning for Multi-modal Medical Data Analysis". *AAAI 2023 (Oral)*.
- Kanghoon Yoon, Kibum Kim, Jinyoung Moon, Chanyoung Park. "Unbiased Heterogeneous Scene Graph Generation with Relation-aware Message Passing Neural Network". *AAAI 2023*.
- Junseok Lee, Sungwon Kim, Dongmin Hyun, Namkyeong Lee, Yejin Kim, Chanyoung Park. "Deep single-cell RNA-seq data clustering with graph prototypical contrastive learning". *Bioinformatics 2023 · also appeared in ICML 2023 Workshop (CompBio)*.
- Sukwon Yun, Junseok Lee, Chanyoung Park. "Single-cell RNA-seq data imputation using Feature Propagation". *ICML 2023 Workshop (CompBio) (Contributed Talk, Best Paper Award)*.
- Namkyeong Lee, Heewoong Noh, Gyoung S. Na, Jimeng Sun, Tianfan Fu, Marinka Zitnik, Chanyoung Park. "Learning Probabilistic Compositional Representation of Crystalline Materials". *NeurIPS 2023 AI4Science Workshop (Earlier version, as PolySRL) · also appeared in KDD 2026 (conference version)*.
- Gyoung S. Na, Chanyoung Park. "Electron-Informed Coarse-Graining Molecular Representation Learning for Real-World Molecular Physics". *NeurIPS 2023 AI4Science Workshop · also appeared in KDD 2025 (conference version)*.
- Namkyeong Lee, Heewoong Noh, Sungwon Kim, Dongmin Hyun, Gyoung S. Na, Chanyoung Park. "Density of States Prediction of Crystalline Materials via Prompt-guided Multi-Modal Transformer". *ICLR 2023 ML4Materials Workshop · also appeared in NeurIPS 2023 (conference version)*.
- Junseok Lee, Sungwon Kim, Dongmin Hyun, Namkyeong Lee, Yejin Kim, Chanyoung Park. "Deep single-cell RNA-seq data clustering with graph prototypical contrastive learning". *ICML 2023 Workshop (CompBio) · also appeared in Bioinformatics 2023 (journal version)*.

**2022**

- Dongmin Hyun, Xiting Wang, Chanyoung Park, Xing Xie, Hwanjo Yu. "Generating Multiple-Length Summaries via Reinforcement Learning for Unsupervised Sentence Summarization". *EMNLP 2022 (Findings)*.
- Geon Lee, Chanyoung Park, Kijung Shin. "Set2Box: Similarity Preserving Representation Learning for Sets". *ICDM 2022*.
- Sukwon Yun, Kibum Kim, Kanghoon Yoon, Chanyoung Park. "LTE4G: Long-Tail Experts for Graph Neural Networks". *CIKM 2022*.
- Namkyeong Lee, Dongmin Hyun, Junseok Lee, Chanyoung Park. "Relational Self-Supervised Learning on Graphs". *CIKM 2022*.
- Dongmin Hyun, Chanyoung Park, Junsu Cho, Hwanjo Yu. "Beyond Learning from Next Item: Sequential Recommendation via Personalized Interest Sustainability". *CIKM 2022*.
- Gyoung S. Na, Chanyoung Park. "Nonlinearity Encoding for Extrapolation of Neural Networks". *KDD 2022*.
- Junseok Lee, Yunhak Oh, Yeonjun In, Namkyeong Lee, Dongmin Hyun, Chanyoung Park. "GraFN: Semi-Supervised Node Classification on Graph with Few Labels via Non-Parametric Distribution Assignment". *SIGIR 2022 (Short paper)*.
- Hyunjin Hwang, Seungwoo Lee, Chanyoung Park, Kijung Shin. "AHP: Learning to Negative Sample for Hyperedge Prediction". *SIGIR 2022 (Short paper)*.
- Namkyeong Lee, Junseok Lee, Chanyoung Park. "Augmentation-Free Self-Supervised Learning on Graphs". *AAAI 2022*.
- Namkyeong Lee, Junseok Lee, Chanyoung Park. "Self-Supervised Graph Representation Learning via Positive Mining". *Information Sciences 2022*.
- Qi Zhu, Chao Zhang, Chanyoung Park, Carl Yang, Jiawei Han. "Shift-Robust Node Classification via Graph Adversarial Clustering". *NeurIPS 2022 Workshop (GLFrontiers)*.

**2021**

- Dongha Lee, Su Kim, Seonghyeon Lee, Chanyoung Park, Hwanjo Yu. "Learnable Structural Semantic Readout for Graph Classification". *ICDM 2021*.
- Dongha Lee, Seongku Kang, Hyunjun Ju, Chanyoung Park, Hwanjo Yu. "Bootstrapping User and Item Representations for One-Class Collaborative Filtering". *SIGIR 2021*.
- Baoyu Jing, Chanyoung Park, Hanghang Tong. "HDMI: High-order Deep Multiplex Infomax". *WWW 2021*.
- Dongmin Hyun, Chanyoung Park, Junsu Cho, Hwanjo Yu. "Learning to Utilize Auxiliary Reviews for Recommendation". *Information Sciences 2021*.

## 과제

랩 Projects 페이지(Funded research projects and industry collaborations)의 42건이다. 진행 중(Ongoing) 21건과 종료(Completed) 21건이며, 페이지에는 과제 기간과 지원 기관이 적혀 있지 않아 날짜 없이 과제 이름과 진행 상태만 적었다.[^projects]

- 그래프 파운데이션 모델: 다양한 모달리티 및 도메인에적용 가능한 그래프 기반 기계 학습 (상태 진행 중)
- 그래프 빅데이터를 위한 파운데이션 모델 개발 (상태 진행 중)
- 강건하고 공정하며 확장 가능한 데이터 중심의 연속 학습 (상태 진행 중)
- 이종데이터기반 상식 추출, 이해, 추론을 위한 인공지능 기술개발 (상태 진행 중)
- 시각 데이터 기억을 위한 장면 그래프 생성 기술 연구 (상태 진행 중)
- 사람처럼 개념적으로 이해/추론이 가능한 복합인공지능 원천기술 연구 (상태 진행 중)
- 지식 체계 확장 가능한 AI 추론 모델 개발과 바이오의료응용 (상태 진행 중)
- FDC Trace 센서 데이터 기반 PM 이상탐지 AI 모델 고도화 (상태 진행 중)
- 자율행동체를 위한 온디바이스 자연어 처리 고속 작업 명세 생성 기술 개발 (상태 진행 중)
- 납축전지 성능 예측 AI 시스템 개발 (상태 진행 중)
- 금속 소재 거대 AI 파운데이션 개발 (소재 특화 파운데이션 모델의 최적화 및 경량화 기술 개발) (상태 진행 중)
- Coordinate-Invariant Neural Operators for Geometry-Transferable 3D PDE Solving (상태 진행 중)
- 컴파운드 레시피 개발 프로세스 혁신을 위한 Hierarchical Agentic Hybrid Optimization (상태 진행 중)
- AI기반 다크팩토리 설계-구축 솔루션 개발 (상태 진행 중)
- AI 기반 소재·소자 수명과학 연구센터 (상태 진행 중)
- 전이학습 기반 복합소재 물성 예측 AI 개발 및 최적화 (상태 진행 중)
- 멀티모달 복합 추론을 통한 재범 위험도 분석 및 추론 연구 (상태 진행 중)
- Geometry-Transferable Neural Operators for 3D PDE Solving (상태 진행 중)
- 언어모델 기반 멀티-에이전트 시스템 요소기술 개발 (상태 진행 중)
- 반도체 소재·소자 추론 모델 개발을 위한 Reward System 개발 (상태 진행 중)
- 근전도 시행자를 위한 근전도 추천 시스템 개발 및 검증 (상태 진행 중)
- 빅데이터 기반 범용 의사결정 지원 시스템 (상태 종료)
- 무기물의 역합성 과정을 예측하는 인공지능 모델 개발 (상태 종료)
- 그래프 마이닝 기법을 통한 전자상거래 플랫폼 사용자 행위 모델링 (상태 종료)
- 연속학습을 통한 사용자의 일반적인 표현 모델 연구개발 (상태 종료)
- 화학 물질간의 상호작용을 통한 물성 예측 인공지능 모델 개발 (상태 종료)
- 멀티 모달 데이터 기반 상품 카테고리 분류 체계 구축 및 확장 (상태 종료)
- 그래프 임베딩 기반 금융상품 추천시스템 (상태 종료)
- 인공지능 기반 보험금 지급 예측 모델 (상태 종료)
- 검색시스템을 위한 지식그래프 구축 (상태 종료)
- 시각 지식 그래프를 이용한 영상의 맥락 이해 (상태 종료)
- 소재 구조-물성 예측 인공지능 모델 개발 (상태 종료)
- 향상된 추천 시스템을 위한 대형언어모델 통합 연구개발 (상태 종료)
- 대형언어모델 및 OCR을 활용한 PDF 텍스트 마이닝 (상태 종료)
- 설계DB 내 유사회로 탐색을 위한 Circuit Recognition (상태 종료)
- 사출성형 성능예측을 위한 3D 형상 기반 Graph Networks 모델 개발 (상태 종료)
- AI를 활용한 거래 관계망 신용 평가 모형 개발 (상태 종료)
- 공학 시뮬레이션을 위한 3D 형상 기반 Graph Neural Networks 모델 개발 (상태 종료)
- 추천시스템을 위한 멀티모달 LLM 연구 (상태 종료)
- 복합소재 물성 예측 AI의 인공신경망 구조 최적화 (상태 종료)
- FDC Trace 센서데이터 기반 이상탐지 모델 개발 (상태 종료)
- 유동영역 3D AI Simulation 기술 개발 (상태 종료)

## 수상

랩 News 페이지에서 Award로 분류된 2021년 10월 이후 글 16건(2023년 1월–2026년 9월)이다. 날짜는 페이지의 연·월 표기이고, 문구는 페이지 그대로다. Samsung Humantech Paper Award 글에는 페이지가 바로 아래 줄에 적은 논문 제목을 괄호로 함께 적었다.[^news]

- 2026.09 · Our lab has been awarded an NVIDIA Academic Grant for our research on "Geometry-Transferable Neural Operators for 3D PDE Solving."
- 2026.08 · Our paper "Physics-Embedded Graph Neural Operator for Interaction-Controlled Colloidal Aggregation" received the Best Paper Award at KDD 2026 Workshop on Reliable Scientific Foundation Models.
- 2026.08 · Our paper "Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-Horizon Agents" received the Best Paper Award at KDD 2026 Workshop on Personal Intelligence in the Agentic AI Era (PILA).
- 2026.08 · Ilho Shin and Hyunchul Kim ranked 1st in Task 2: Contextualized Early Detection of Depression at CLEF eRisk 2026.
- 2026.04 · We won the 2026 Google Research award for our research "Coordinate-Invariant Neural Operators for Geometry-Transferable 3D PDE Solving."
- 2026.02 · Namkyeong Lee received the KAIST Presidential Best Ph.D. Thesis Award for his dissertation “Understanding Science through the Lens of AI.”
- 2025.12 · Prof. Park received the 2025 KAIST College of Engineering Impact Research Award.
- 2025.02 · Prof. Park has been honored with the Song-Am Distinguished Research Award, which recognizes assistant professors in the College of Engineering at KAIST with outstanding research achievements within their first five years of employment.
- 2024.10 · Junseok Lee received KAIST Graduate Student Outstanding Paper Award for his paper "Single-cell RNA Sequencing Data Imputation Using Bi-level Feature Propagation" published in Briefings in Bioinformatics.
- 2024.08 · Our paper "Subgraph Federated Learning for Local Generalization" received the Best Paper Award at KDD 2024 Workshop on Federated Learning for Data Mining and Graph Analytics (FedKDD).
- 2024.08 · Our paper "Interpretable Graph Model with Prototype-Based Graph Information Bottleneck" received the Best Paper Award at KDD 2024 Workshop on Human-Interpretable AI.
- 2024.01 · Sangwoo Seo and Sungwon Kim received Gold Prize at the 30th Samsung Humantech Paper Award (for their paper Interpretable Prototype-based Graph Information Bottleneck published in NeurIPS 2023).
- 2024.01 · Prof. Park received 2023 Technology Innovation Awards of College of Engineering, KAIST.
- 2023.07 · Our paper "Single-cell RNA-seq data imputation using Feature Propagation" received the Best Paper Award at ICML 2023 Workshop on Computational Biology.
- 2023.02 · Prof. Park received KAIST Excellence in Teaching Award of Year 2022.
- 2023.01 · Prof. Park received Best Teaching Award from ISysE, KAIST

## 소식

랩 News 페이지의 2021년 10월 이후 글 가운데 논문 소식 58건, 강연 2건, 학술 활동 2건으로 모두 62건이다. Award로 분류된 글은 위 「수상」에 두었다. 날짜는 페이지의 연·월 표기이고, 문구는 페이지 그대로다.[^news]

- 2026.10 · A paper got accepted at WACV 2027.
- 2026.09 · Nine papers got accepted at NeurIPS 2026.
- 2026.09 · Four papers got accepted at NeurIPS 2026 Workshop (1 x AI4Science, 3 x AI4Mat).
- 2026.08 · Four papers got accepted at CIKM 2026 (2 x Research Track, 1 x Applied Research Track, 1 x Short Paper Track).
- 2026.06 · Two papers got accepted at ECCV 2026.
- 2026.05 · Six papers got accepted at ICML 2026 Workshop (3 x AI for Science, 1 x CATS, 1 x FAGEN, 1 x GenBIO).
- 2026.05 · Two papers got accepted at KDD 2026 (1 x Research Track and 1 x AI for Science Track).
- 2026.05 · Five papers got accepted at ICML 2026.
- 2026.04 · A paper got accepted by ACM Transactions on Intelligent Systems and Technology.
- 2026.04 · A paper got accepted at ACL 2026 (Main).
- 2026.03 · Prof. Park will be organizing KDD'26 Workshop on SciSoc Agents & LLMs.
- 2026.03 · A paper got accepted by Water Research.
- 2026.03 · Six papers got accepted at ICLR 2026 Workshop (1 x AI and Partial Differential Equations (Oral), 3 x AI4Mat, 1 x AI with Recursive Self-Improvement, 1 x Generative and Experimental Perspectives for Biomolecular Design).
- 2026.01 · Three papers got accepted at ICLR 2026.
- 2026.01 · A paper got accepted at SSAC 2026 (MIT Sloan Sports Analytics Conference).
- 2026.01 · A paper got accepted at WWW 2026.
- 2025.11 · A paper got accepted at AAAI 2026.
- 2025.10 · Three papers got accepted at NeurIPS 2025 Workshop (Workshop on Efficient Reasoning, AI for Science, and Reliable ML from Unreliable Data).
- 2025.09 · Three papers got accepted at NeurIPS 2025 (including 1 Spotlight).
- 2025.08 · Two papers got accepted at EMNLP 2025 (1 Main and 1 Findings).
- 2025.07 · Prof. Park will serve as a General Co-Chair of CIKM 2025, which will be held in Seoul, Korea.
- 2025.06 · A paper got accepted at ICCAD 2025.
- 2025.05 · Two papers got accepted at KDD 2025 (February Cycle).
- 2025.05 · Two papers got accepted at ICML 2025.
- 2025.04 · Two papers got accepted at SIGIR 2025.
- 2025.03 · Two papers got accepted at ICLR 2025 Workshop on Machine Learning for Genomics Explorations (MLGenX) (including 1 Spotlight).
- 2025.01 · Three papers got accepted at ICLR 2025 (including 1 Oral).
- 2025.01 · Two papers got accepted at NAACL 2025 (1 Main and 1 Findings).
- 2024.12 · A paper got accepted at AAAI 2025.
- 2024.11 · Two papers got accepted at KDD 2025 (August Cycle).
- 2024.10 · A paper got accepted at WSDM 2025 (Oral).
- 2024.10 · A paper got accepted at NeurIPS 2024 Workshop on AI for New Drug Modalities (AIDrugX).
- 2024.09 · A paper got accepted at NeurIPS 2024.
- 2024.07 · Two papers got accepted at CIKM 2024.
- 2024.07 · Two papers got accepted at ECCV 2024.
- 2024.05 · Two papers got accepted at KDD 2024.
- 2024.05 · A paper got accepted at ICML 2024.
- 2024.04 · A paper got accepted at Briefings in Bioinformatics.
- 2024.02 · A paper got accepted at CVPR 2024.
- 2024.01 · Two papers got accepted at WWW 2024.
- 2024.01 · A paper got accepted at ICLR 2024.
- 2023.12 · A paper got accepted at AAAI 2024.
- 2023.10 · Two papers got accepted at NeurIPS 2023 workshop on AI for Scientific Discovery: From Theory to Practice (AI4Science).
- 2023.09 · Two papers got accepted at NeurIPS 2023.
- 2023.08 · Three papers (1 Long, 2 Short) got accepted at CIKM 2023.
- 2023.06 · Prof. Park gave a tutorial at 2023 KCC on 그래프 신경망 기반 화학/소재분야 연구 동향.
- 2023.06 · Two papers got accepted at ICML 2023 Workshop on Computational Biology.
- 2023.05 · A paper got accepted at Bioinformatics.
- 2023.05 · Four papers got accepted at KDD 2023.
- 2023.04 · A paper got accepted at ICML 2023.
- 2023.04 · A paper got accepted at SIGIR 2023.
- 2023.03 · A paper got accepted at WWW 2024 Workshop on Data-centric Artificial Intelligence (DCAI).
- 2023.03 · A paper got accepted at ICLR 2023 Workshop on Machine Learning for Materials (ML4Materials).
- 2022.11 · Two papers got accepted at AAAI 2023.
- 2022.11 · A paper got accepted at NeurIPS 2022 Workshop on New Frontiers in Graph Learning (GLFrontiers).
- 2022.10 · A paper got accepted at EMNLP 2022 (Findings).
- 2022.09 · A paper got accepted at ICDM 2022.
- 2022.08 · Prof. Park gave a tutorial at 2022 데이터베이스 소사이어티 여름학교.
- 2022.08 · Three papers got accepted at CIKM 2022.
- 2022.05 · A paper got accepted at KDD 2022.
- 2022.04 · Two papers got accepted at SIGIR 2022.
- 2021.12 · A paper got accepted at AAAI 2022.

## 연락과 위치

- 교수실: KAIST E2-2동 4104호(교수 페이지 표기)[^professor]
- 연구실: KAIST E2-2동 4124호(첫 화면 Contact 표기)[^home]
- 교수 이메일: cy.park@kaist.ac.kr[^gsds]
- 전화: 042-350-3137(교수 페이지), 042-350-3177(첫 화면 Contact)[^professor][^home]
- 주소: 291 Daehak-ro, Yuseong-gu, Daejeon, Republic of Korea[^home]
[^home]: 연구실 누리집 첫 화면 <https://dsail.kaist.ac.kr/> (표어와 소개, News 최근 글, Contact, 2026-10-23 열람)
[^professor]: Professor 페이지 <https://dsail.kaist.ac.kr/professor/> (직위·소속, Prospective students, Experience, Education, Awards, Teaching, Academic service, Selected talks, 연락처, 2026-10-23 열람)
[^members]: Team 페이지(메뉴 Current) <https://dsail.kaist.ac.kr/members/> (Ph.D. students, M.S. students, Undergraduate interns 칸의 구성원 카드, 2026-10-23 열람)
[^alumni]: Alumni 페이지 <https://dsail.kaist.ac.kr/alumni/> (Ph.D., M.S., Visitors, Undergraduate interns 칸, 2026-10-23 열람)
[^news]: News 페이지 <https://dsail.kaist.ac.kr/news> (연·월별 글과 Paper·People·Award·Talk·Service 분류, 2026-10-23 열람)
[^research]: Research 페이지 <https://dsail.kaist.ac.kr/research/> (Areas, Where these areas meet, Applications & impact; 페이지가 불러오는 자료 파일 <https://dsail.kaist.ac.kr/research/papers.json> 의 themes·convergence·applications 항목, 2026-10-12 갱신, 2026-10-23 열람)
[^pubs]: Publications 페이지 <https://dsail.kaist.ac.kr/publications/> (페이지가 불러오는 자료 파일 <https://dsail.kaist.ac.kr/research/papers.json> 의 papers 항목 170편과 분야 배정, 2026-10-12 갱신, 2026-10-23 열람)
[^projects]: Projects 페이지 <https://dsail.kaist.ac.kr/projects> (Ongoing 21건, Completed 21건, 2026-10-23 열람)
[^gst]: KAIST 안보과학기술대학원 교수 목록 2쪽 <https://gst.kaist.ac.kr/member/faculty/?page=2> (박찬영 항목: 소속학과, 연구분야, 세부 연구 분야, 연구실; 소속학과 선택 목록의 학과 이름, 2026-10-23 열람)
[^gsds]: KAIST 데이터사이언스대학원 구성원 페이지 <https://gsds.kaist.ac.kr/people> (박찬영 항목: Focus Area, E-mail, 2026-10-23 열람)
[^neurips]: NeurIPS 2026 학회 페이지 <https://neurips.cc/Conferences/2026> (Sydney 본 행사 Dec 6–12, 2026-10-23 열람)
[^p1]: N. Lee, J. Lee, C. Park, Proceedings of the AAAI Conference on Artificial Intelligence 36, 7372-7380 (온라인 2022-06-28). <https://doi.org/10.1609/aaai.v36i7.20700> 초록 기준.
[^p2]: S. Seo 외, C. Park, Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, 2572-2583 (온라인 2024-08-24). <https://doi.org/10.1145/3637528.3671962> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: S. Kim 외, C. Park, Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, 1395-1406 (온라인 2024-08-24). <https://doi.org/10.1145/3637528.3671931> 초록 기준(같은 제목의 arXiv 판 <https://arxiv.org/abs/2404.11343>).
[^p4]: S. Kim 외, C. Park, Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2, 1160-1171 (온라인 2025-08-03). <https://doi.org/10.1145/3711896.3737035> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: K. Kim 외, C. Park, International Conference on Learning Representations (ICLR 2024). <https://openreview.net/pdf?id=WipsLtH77t> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: Y. In 외, C. Park, Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), 1212-1233 (2025). <https://doi.org/10.18653/v1/2025.naacl-long.56> 초록 기준(같은 제목의 arXiv 판 <https://arxiv.org/abs/2409.02361>).
[^p7]: N. Lee 외, C. Park, International Conference on Machine Learning (ICML 2023). <https://arxiv.org/abs/2305.01520> 초록 기준(같은 제목의 arXiv 판).
[^p8]: H. Noh, N. Lee, G. S. Na, C. Park, Advances in Neural Information Processing Systems 37, 25375-25400 (2024). <https://doi.org/10.52202/079017-0799> 초록 기준(같은 제목의 arXiv 판 <https://arxiv.org/abs/2410.21341>).

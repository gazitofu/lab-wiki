# 인공지능 및 빅데이터 시스템 연구실 (AIDAS Lab)

**서울대학교 공과대학 전기·정보공학부, 협동과정 인공지능 전공 · 도재영 조교수**

- 분야: 생성형 AI, 대형 언어 모델의 가치 정렬과 추론 평가, 비전-언어 모델과 옴니모달 확산 모델, 의료 영상을 다루는 비전-언어 모델, 몸을 가진 인공지능(로봇 행동 생성), 벡터 데이터베이스, 대형 언어 모델 추론 효율, 빅데이터/AI 시스템
- 대분야: 컴퓨팅·AI
- 태그: 대형 언어 모델[^home][^p1][^p2], 멀티모달 AI[^home][^p3][^p4], 생성 인공지능[^home][^p4], AI 시스템·인프라[^home][^p8], 컴퓨터 비전[^p5], 월드 모델[^home][^p6], 의료 AI[^p5], 로봇 조작·파지[^p6]
- 홈페이지: <https://aidas.snu.ac.kr/>
- 근거와 출처: [AIDAS Lab 근거 페이지](aidas-sources.md)

> 인공지능 모델의 구조, 많은 데이터를 다루는 시스템, 몸을 가진 에이전트(로봇)를 함께 연구하는 연구실이다. 대형 언어 모델과 비전-언어 모델 같은 생성 인공지능 모델을 만들고, 이를 빠르고 효율적으로 돌리는 시스템을 설계하며, 의료·산업 분야에서 쓰이게 하는 데 무게를 둔다.[^home]

## 무엇을 연구하나

연구실은 서울대 전기·정보공학부 도재영 조교수가 이끄는 연구실이다.[^ece] 학과 연구실 소개는 영문 이름을 AIDAS Laboratory (AI, Big Data, and System)로, 연구 분야를 AI, 빅데이터, 시스템으로 적고,[^ecelab] 학과 연구실 목록은 이 연구실을 인공지능 및 머신러닝, 지능 및 로봇 공학, 차세대 컴퓨팅, 회로 및 시스템, 빅데이터 및 인공지능 플랫폼의 다섯 연구그룹에 올린다.[^ecelist] 교수는 2024년 2월 서울대에 부임했다.[^ece]

연구실 누리집은 연구의 초점을 기초 모델 구조(fundamental model architectures), 데이터를 많이 다루는 시스템(data-intensive systems), 몸을 가진 에이전트(embodied agents, 실제 물리 세계에서 보고 움직이는 인공지능)의 세 가지로 소개한다. 인공지능 모델 설계의 새 방법을 시스템 수준의 최적화와 실제 응용에 잇는 통합 접근을 연구실의 특징으로 들고, 실제 배치를 바탕에 두며 특히 의료와 산업 분야의 응용에 무게를 둔다고 적는다.[^home] 연구 기둥은 셋이다. Core AI는 대형 언어 모델(LLM, 많은 글을 학습해 글을 이해하고 만들어 내는 큰 인공지능 모델), 비전-언어 모델(VLM, 그림과 글을 함께 다루는 모델), 비전-언어-행동 모델(VLA, 카메라 영상과 말로 된 지시를 받아 로봇이 할 행동을 내놓는 모델) 같은 생성 인공지능 모델과 새 모델 구조·학습 방법을 연구한다. System AI는 소프트웨어와 하드웨어를 함께 설계해 인공지능 시스템의 확장성과 효율을 높이고, 여러 종류의 컴퓨터가 섞인 환경에서 대규모 데이터 처리와 인공지능의 학습·추론·배치를 빠르게 하는 일이다. Embodied AI는 변하는 물리 환경에서 스스로 지각하고 추론하고 행동하는 지능형 에이전트를 만드는 일로, 여러 감각을 함께 쓰는 지각, 행동 계획, 실시간 제어를 묶는다.[^home] 응용 분야로는 의료(영상·생체 신호·전자 건강 기록 같은 의료 자료를 해석해 진단, 치료 계획, 결과 예측을 돕는 모델)와 산업(예측 정비, 공정 최적화, 지능형 자동화 같은 제조 현장의 문제)을 든다.[^home]

누리집은 대표 프로젝트로 공개한 두 모델을 내세운다. dynin-omni는 글·그림·영상·소리 등 모든 종류의 자료를 한 구조 안에서 이해하고 만드는 생성 기반 모델이고, dynin-robotics는 행동 생성, 월드 모델링(행동에 따라 주변이 어떻게 바뀔지 예측하는 일), 목표 상태 예측, 과제 이해를 한 뼈대 모델에 묶은 옴니모달 확산 비전-언어-행동 모델이다.[^home] Robots 페이지는 몸을 가진 인공지능 연구에 쓰는 연구실 보유 로봇으로 매니퓰레이터(로봇 팔) SO-101 2대, Franka Research 3 2대, UR7e·WidowX AI (Stationary)·ALOHA Cobot Magic·R1-Lite 각 1대, 엔드 이펙터 DG-5F-M·Franka Hand 각 1대와 Robotiq 2F-85 2대, 원격 조종 장치 MetaGloves Pro Haptic·Franka Gello Duo 각 1대를 싣는다.[^robots]

첫째 갈래는 **대형 언어 모델의 가치 정렬과 추론 평가**다. 정렬은 모델의 출력이 사람의 의도와 가치에 맞도록 만드는 일이다. 대표 논문에서는 가치를 뽑아내고, 그 세기까지 재고, 정해진 세기로 모델을 이끄는 일을 한 틀로 묶은 VALUEFLOW를 내놓았고,[^p1] 답을 내기 전에 추론 과정을 글로 써 내는 대형 추론 모델이 적어 낸 추론이 실제로 답을 이끌었는지(추론 충실성)를 재는 벤치마크 RFEval을 만들었다.[^p2] 누리집 소식에 따르면 VALUEFLOW는 ICML 2026에 Spotlight로 채택된 뒤 구두 발표(oral presentation)로 뽑혔다.[^news] 최근 논문 목록에는 가치를 집단과 맥락에 따른 분포로 나타내는 연구(NeurIPS 2026 채택), 확산 언어 모델에서 고친 내용이 사라지지 않게 하는 연구(NeurIPS 2025), 표를 보고 질문에 답하는 다중 에이전트 틀 MATA(ACL 2026 Findings), 전문가 혼합(MoE) 모델을 압축한 뒤의 조정 방법을 비용 기준으로 비교한 연구(EMNLP 2026 채택)도 있다.[^pubs]

둘째 갈래는 **비전-언어 모델과 옴니모달 모델**이다. 옴니모달 모델은 글·그림·말소리·영상처럼 여러 종류의 자료를 한 모델에서 함께 다루는 모델이다. 대표 논문에서는 비전-언어 모델이 그림에 없는 물체를 있다고 말하는 물체 환각을, 여러 배율의 시각 정보를 골라 대조하는 디코딩으로 줄였고,[^p3] 글·그림·말소리의 이해와 생성, 영상 이해를 마스크 확산 방식 하나로 묶은 기반 모델 Dynin-Omni를 공개했다.[^p4] 의료 쪽으로는 의료 영상에서 병변을 찾고, 검사 사이의 변화를 추적하고, 판단 근거가 되는 부위를 열지도로 보여 주는 의료 비전-언어 모델 Medic-AD를 만들었다.[^p5] 누리집 소식에 따르면 Medic-AD는 CVPR 2026에서 구두 발표로 뽑혔고 상 후보(award candidate)에 올랐으며, 연구실 팀은 CVPR 2026의 5th PVUW Challenge MeViS-Audio Track에서 3위를 했다.[^news] 최근 논문 목록에는 멀티모달 개인화 벤치마크 MMPB(NeurIPS 2025), 영상의 시간·공간 분할을 위한 추론 도우미 VIRST(CVPR 2026), 여러 시점의 흉부 X선 영상을 이어 보는 추론 벤치마크 MI-CXR(ACL 2026 Findings), 영상 물체 분할 평가를 다시 살핀 연구(NeurIPS 2026 채택)도 있다.[^pubs]

셋째 갈래는 **로봇 행동을 만드는 몸을 가진 인공지능**이다. 대표 논문에서는 Dynin-Omni를 뼈대로 언어, 시각 관측, 목표, 행동을 모두 같은 종류의 토큰으로 나타내, 한 모델이 행동 예측, 행동에 따른 다음 장면 예측, 마지막 목표 상태 예측을 함께 배우게 한 Dynin-Robotics를 내놓았고, Franka Research 3 로봇에서 네 가지 조작 조건으로 실험했다.[^p6] Robots 페이지에 따르면 연구실은 Franka Research 3 2대를 가지고 있다.[^robots]

넷째 갈래는 **벡터 데이터베이스와 인공지능 시스템 효율**이다. 벡터 데이터베이스는 글·그림 같은 자료를 숫자 벡터로 바꿔 저장해 두고, 질문과 가까운 벡터를 빨리 찾아 주는 데이터베이스다. 대표 논문에서는 정형 조건을 함께 만족해야 하는 벡터 검색에서 널리 쓰이는 벤치마크가 난도 범위의 좁고 상대적으로 쉬운 부분에 몰려 있음을 보이고, 질의 난도를 재는 지표와 난도를 조절해 시험용 질의를 만드는 생성기를 내놓았다.[^p7] 또 대형 언어 모델의 가중치 일부를 덜어 내는 가지치기를 고정 방식과 입력에 따라 바뀌는 방식 모두 쓰도록 묶고, 이에 맞춘 압축 형식과 GPU 계산 프로그램을 함께 설계해 추론을 빠르게 했다.[^p8] 최근 논문 목록에는 서로 다른 여러 벡터 데이터베이스에 걸쳐 함께 검색하는 HVMap(VLDB 2027 채택), 그래프 기반 벡터 색인인 HNSW의 설정값을 제약 조건에 맞춰 효율적으로 고르는 연구(SIGMOD 2027), 최신 SSD로 벡터 데이터베이스를 빠르게 하는 연구(VLDB 2025), 대형 언어 모델 추론에서 계산 대신 플래시 저장장치를 쓰는 MatKV(ICDE 2026)도 있다.[^pubs]

## 주요 연구 주제

### 1. 대형 언어 모델의 가치 정렬과 추론 평가

모델이 드러내는 가치의 세기까지 재고 조절하는 정렬 틀(VALUEFLOW), 대형 추론 모델의 추론이 답을 실제로 이끄는지 재는 벤치마크(RFEval).[^p1][^p2] 대표 논문 1, 2.

### 2. 비전-언어 모델과 옴니모달 모델

비전-언어 모델의 물체 환각을 줄이는 디코딩(SECOND), 글·그림·말소리·영상을 한 모델로 다루는 마스크 확산 기반 모델(Dynin-Omni), 병변 검출과 변화 추적을 하는 의료 비전-언어 모델(Medic-AD).[^p3][^p4][^p5] 대표 논문 3–5.

### 3. 로봇 행동을 만드는 몸을 가진 인공지능

언어·관측·목표·행동을 한 모델에서 함께 예측하는 옴니모달 비전-언어-행동 모델(Dynin-Robotics).[^p6] 대표 논문 6.

### 4. 벡터 데이터베이스와 인공지능 시스템 효율

조건이 붙은 벡터 검색을 위한 난도 조절 벤치마크 생성기(HCBGen), 대형 언어 모델 추론을 빠르게 하는 고정·동적 가지치기 통합 틀(SPDP).[^p7][^p8] 대표 논문 7, 8.

## 대표 논문

도재영 교수가 서울대에 부임한 2024년 2월 뒤의 논문 가운데 교수가 마지막 저자이고 교신저자 표시(^)가 붙은 것에서 연구 갈래마다 한두 편씩 골랐고, 2026년 논문 일곱 편을 넣었다. 교수 개인 누리집의 논문 목록은 연구실 목록과 같은 표기를 쓰며 \*를 1저자, ^를 교신저자로 밝힌다.[^jydo] 대표 논문 4는 연구실 목록이 arXiv 사전 공개본으로 싣는 논문이고, 6은 NeurIPS 2026 발표를 앞둔 채택 논문이라 arXiv 판으로 적었다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in Large Language Models](https://arxiv.org/abs/2602.03160) · ICML 2026 (Oral) | 대형 언어 모델을 사람의 다양한 가치에 맞추는 일은 여전히 중심 과제이고, 사람이 더 낫다고 고른 답을 따르게 하는 선호 기반 방법은 더 깊은 동기의 원칙을 담지 못하는 때가 많다. 가치 기반 접근이 더 원칙적인 길이지만 세 가지 빈틈이 남아 있다. 가치를 뽑아낼 때 위계 구조를 무시하고, 평가할 때 가치가 있는지만 보고 그 세기는 재지 못하며, 정해진 세기로 모델을 이끄는 일(조종)이 얼마나 되는지 잘 알려지지 않았다. 연구진은 가치의 추출·평가·조종을 세기 조절까지 한 틀로 묶은 VALUEFLOW를 내놓았다. 틀은 세 부분이다. 가치 이론 안팎의 가치 구조를 담는 위계적 가치 임베딩 공간(HIVES, 개념을 숫자 벡터로 나타낸 공간), 순위를 모아 추정한 세기가 붙은 가치 표시 글의 대규모 자료(VIDB), 모델 출력을 VIDB의 기준 글 묶음과 견주어 순위를 매겨 일관된 세기 점수를 내는 평가기다. 이 틀로 모델 10개와 가치 이론 4개에 걸친 대규모 연구를 해, 조종 가능성의 비대칭과 여러 가치를 함께 조절할 때의 결합 법칙을 찾았다.[^p1] | 1저자 Woojin Kim, 마지막 저자 도재영(랩 표기 ^) |
| 2 | 2026 | [RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models](https://arxiv.org/abs/2602.17053) · ICLR 2026 | 대형 추론 모델(LRM, 답을 내기 전에 추론 과정을 글로 써 내는 언어 모델)은 성능이 좋지만, 그럴듯하게 들려도 실제 결정 과정을 반영하지 않는 추론을 자주 내놓아 신뢰를 떨어뜨린다. 연구진은 추론 충실성을 정확도와 떼어 놓고 두 가지 시험할 수 있는 조건으로 정의했다. 추론과 답이 같은 입장으로 이어지는지(입장 일관성), 그리고 출력에 개입했을 때 적힌 추론이 실제로 답을 이끄는지(인과적 영향)다. 이를 재려고 7개 과제의 7,186개 사례로 이뤄진 벤치마크 RFEval을 만들어, 출력 수준의 반사실적 개입(실제와 다른 내용으로 바꿔 넣고 결과가 어떻게 달라지는지 보는 시험)으로 충실성을 살폈다. 공개 대형 추론 모델 12개를 평가하니 출력의 49.7%가 충실하지 않았고, 대부분 입장 불일치에서 왔다. 실패는 수학·코드처럼 깨지기 쉽고 답이 하나로 모이는 분야에 몰렸고, 모델 크기보다 학습 뒤 단계의 방식과 더 관련이 있었다. 같은 계열 모델을 비교하면 지도 미세 조정 위에 지금의 강화학습식 목표를 더할 때 정확도는 유지돼도 충실성이 줄 수 있었다. 모델과 과제를 통제하면 정확도와 충실성의 관계는 약하고 통계적으로 유의하지 않아, 정확도는 충실성을 대신하는 충분하거나 믿을 만한 지표가 아니다.[^p2] | 1저자 Yunseok Han, 마지막 저자 도재영(랩 표기 ^) |
| 3 | 2025 | [SECOND: Mitigating Perceptual Hallucination in Vision-Language Models via Selective and Contrastive Decoding](https://arxiv.org/abs/2506.08391) · ICML 2025 | 비전-언어 모델(VLM)은 크게 발전했지만, 그림에 없는 물체를 있다고 말하는 물체 환각이 정확한 시각 이해를 가로막는다. 연구진은 VLM이 여러 배율의 시각 정보를 사람의 시각 지각에 가깝게 물체 중심으로 쓰도록 하는 디코딩(모델이 답의 낱말을 하나씩 골라 내는 과정) 방법 SECOND(Selective and Contrastive Decoding)를 제안했다. 여러 배율의 시각 정보를 차례로 골라 합쳐 그림을 더 정확히 해석하게 하고, 이 정보들을 되풀이해 대조해 지각 환각을 크게 줄였으며, 여러 벤치마크에서 기존 방법보다 나았다. 이론 분석과 실험은 배율 사이에 우선순위를 두고 대조하는 방식이 기존 방법보다 낫다는 점을 보이며, VLM에서 여러 배율을 쓰는 방법에 아직 많이 탐구되지 않은 가능성이 있음을 드러낸다.[^p3] | 1저자 Woohyeon Park, 마지막 저자 도재영(랩 표기 ^) |
| 4 | 2026 | [Dynin-Omni: Omnimodal Unified Large Diffusion Language Model](https://arxiv.org/abs/2604.00007) · arXiv 사전 공개본 | 글·그림·말소리의 이해와 생성, 그리고 영상 이해를 한 구조에 묶은 옴니모달 기반 모델이다. 여러 종류의 자료를 한 줄로 늘어놓고 앞에서부터 하나씩 이어 만드는(자기회귀) 통합 모델이나, 자료마다 따로 둔 외부 디코더(토큰을 그림·소리 같은 실제 자료로 되돌리는 부분)와 맞물려 돌려야 하는 조합형 통합 모델과 달리, 모든 자료가 함께 쓰는 이산 토큰(모델이 다루는 기호 단위) 공간 위의 마스크 확산(가려 둔 토큰을 여러 번에 걸쳐 채워 나가며 결과를 만드는 생성 방식)으로 옴니모달 모델링을 세워, 앞뒤 문맥을 함께 보며 결과를 되풀이해 다듬을 수 있게 했다. 모델 병합으로 다루는 자료 종류를 넓히는 여러 단계의 학습과 옴니모달 정렬을 거친다. 언어 추론, 그림 생성·편집, 영상 이해, 음성 인식·합성에 걸친 19개 멀티모달 벤치마크에서 GSM8K 87.6, MME-P 1733.6, VideoMME 61.4, GenEval 0.87, LibriSpeech test-clean 단어 오류율 2.1을 얻어, 기존 공개 통합 모델보다 꾸준히 나았고 자료별 전문 모델과도 겨룰 만했다. 연구진은 마스크 확산이 어떤 자료를 넣고 어떤 자료를 내놓든 쓸 수 있는 통합 틀이 될 수 있으며, 실시간 옴니모달 시스템, 자료 종류를 넘나드는 검색과 생성, 몸을 가진 멀티모달 에이전트의 바탕이 될 수 있다고 본다.[^p4] | 1저자 Jaeik Kim, 마지막 저자 도재영(랩 표기 ^) (11명) |
| 5 | 2026 | [Medic-AD: Towards Medical Vision-Language Model's Clinical Intelligence](https://arxiv.org/abs/2603.27176) · CVPR 2026 (Oral, Award Candidate) | 실제 의료 영상 분석의 중심은 병변 검출, 증상 추적, 시각적 설명인데, 지금의 의료 비전-언어 모델은 폭넓은 지식을 임상에서 바로 쓸 수 있는 출력으로 바꾸는 장치가 부족하다. 연구진은 단계별 틀로 이 세 능력을 키운 임상 지향 비전-언어 모델 MEDIC-AD를 내놓았다. 먼저 학습할 수 있는 이상 인식 토큰(Ano 토큰)이 모델을 비정상 부위에 집중시켜 병변 중심의 더 잘 구별되는 표현을 만들게 하고, 다음으로 영상 사이 차이 토큰(Diff 토큰)이 검사와 검사 사이의 시간 변화를 직접 담아 병의 악화·호전·유지를 가리게 한다. 마지막 설명 단계에서는 병변과 관련된 부위를 강조하는 열지도를 만들도록 학습시켜, 모델의 추론과 맞는 시각 증거를 보여 준다. 이 단계별 설계로 이상 검출, 증상 추적, 이상 부위 분할 성능이 꾸준히 올라 비공개 모델과 의료 특화 기준 모델보다 나은 결과를 얻었다. 실제 병원 업무에서 모은 종단 임상 자료(같은 환자를 시간에 따라 여러 번 검사한 자료)로 평가한 결과도 환자 관찰과 의사 결정 지원 업무에서 안정적인 예측과 임상에 충실한 설명을 보였다.[^p5] | 1저자 Woohyeon Park, 마지막 저자 도재영(랩 표기 ^) (10명) |
| 6 | 2026 | [Dynin-Robotics: Omnimodal Unified Diffusion Vision-Language-Action Model](https://arxiv.org/abs/2609.13053) · NeurIPS 2026 채택 | 시각적 목표와 장면 변화를 예측하면, 말로 지시를 받는 로봇 정책(상황마다 로봇이 할 행동을 정하는 규칙)에 도달할 결과와 행동에 따른 장면 변화의 표현을 함께 줄 수 있다. 연구진은 이런 예측을 하나의 공유 궤적 모델(행동과 관측이 시간 순서로 이어진 기록을 다루는 모델)로 행동 생성과 선택에 끌어들였다. Dynin-Robotics는 옴니모달 마스크 확산 뼈대 모델인 Dynin-Omni 위에 이를 구현해 언어, 시각 관측, 목표, 행동을 모두 이산 토큰으로 나타낸다. 조건으로 주는 부분과 맞힐 부분을 바꿔 가며, 같은 모델이 행동 예측, 행동을 조건으로 한 다음 관측 예측, 마지막 목표 상태 예측, 궤적에서 지시문을 되살리는 일을 배운다. 이 기능들로 실행 시점에 목표 예측, 행동 후보 평가, 행동과 미래 상태 예측의 공동 다듬기를 써서 계산을 더 들여 성능을 높일 수 있다. Open X-Embodiment의 48개 데이터셋에서 약 133만 개 궤적으로 이어서 사전 학습한 뒤 응용 분야마다 따로 맞췄다. VLABench 두 과제에서 로봇 사전 학습은 정해진 학습 단계 안에서 적응을 도왔고, 같은 디코더에서 학습 목표를 모두 섞으면 정책만 사후 학습할 때보다 바뀐 지시에서의 성공률이 높았다. 목표 안내와 행동·다음 상태의 공동 잡음 제거를 함께 쓰면 성공률이 행동만 만들 때보다 더 높아졌고, 그 이득은 예측을 어떻게 조합하느냐에 달렸다. LIBERO와 추가 학습 없이 평가한 LIBERO-Plus에서 경쟁력 있는 성능을 냈고, Franka Research 3 로봇에서 네 가지 조작 조건 평균 78.4%의 성공률을 얻었다. 최적화한 블록 병렬 구현은 보고된 측정 환경에서 모델 쪽 행동 생성을 기본 구현보다 최대 29.2배 빠르게 했다.[^p6] | 1저자 Hoeun Lee, 마지막 저자 도재영(랩 표기 ^) (7명) |
| 7 | 2026 | [Revisiting Filtered ANN Benchmarks: A Hardness-Controlled Benchmark Generator for Realistic Evaluation](https://doi.org/10.14778/3828612.3828630) · Proceedings of the VLDB Endowment (VLDB 2026, Oral) | 필터 조건이 붙은 근사 최근접 이웃 검색(FANN, 정형 조건을 만족하면서 비슷한 벡터를 근사적으로 찾는 검색)은 벡터 유사도와 정형 조건을 모두 만족해야 하는데, 실제 혼합 작업 부하(시스템이 처리해야 하는 질의와 작업의 묶음)는 공유되기 어렵고 기존 벤치마크는 임시방편의 합성·반합성 구성에 기대어 평가가 불안정하다. 연구진은 현실성이 실행에서 생기는 질의 난도에 달려 있다고 본다. 이른 단계의 필터링이 실패하면 후보를 더 가져와야 하고(과다 인출), 이것이 지연 시간·처리량·재현율(찾아야 할 답 가운데 실제로 찾은 비율)을 좌우한다. 이에 따라 과다 인출 배수로 조건부 실행 과정을 모형화하는 질의 단위 난도 지표 α-Hardness를 제안했다. 여러 데이터셋과 혼합 검색 전략에서 α-Hardness는 실제 성능과 강한 단조 관계(한쪽이 커지면 다른 쪽도 한 방향으로만 변하는 관계)를 보였지만, 선택도(조건을 만족하는 자료의 비율)나 속성-벡터 상관 같은 흔한 대리 지표는 자주 불안정하거나 전략마다 어긋났다. 또 α-Hardness를 제어 신호로 써서 대략의 치우침 방식에 따라 작업 부하를 합성하거나 목표 난도 분포에 맞추는 벤치마크 생성기 HCBGen을 내놓았다. 실험 결과 널리 쓰이는 벤치마크는 난도 범위의 좁고 상대적으로 쉬운 부분에 있어, 어려운 질의에서 드러나는 강건성 차이를 가린다. 끝으로 난도 분포를 맞추면 성능 경향을 가깝게 재현하면서 프라이버시를 지키는 대리 작업 부하를 만들 수 있어, 연구용 벤치마크와 실제 평가를 이을 수 있음을 보였다.[^p7] | 1저자 Mintaek Lim, 마지막 저자 도재영(랩 표기 ^) |
| 8 | 2026 | [Unified Static–Dynamic Pruning for Efficient LLM Inference](https://doi.org/10.14778/3836663.3836665) · Proceedings of the VLDB Endowment (VLDB 2026, Oral) | 대형 언어 모델을 쓰는 곳이 늘면서, 답을 토큰 하나씩 이어 만드는 자기회귀 디코딩의 계산·메모리 병목이 커졌다. 이 단계에서는 계산 밀도(메모리에서 읽은 데이터 하나당 하는 계산의 양)가 낮고 메모리 대역폭(정해진 시간에 메모리와 주고받을 수 있는 데이터 양)에 묶인 연산이 추론 비용을 좌우한다. 가중치 가지치기(모델의 가중치 일부를 덜어 내 계산을 줄이는 방법)가 해법이 될 수 있지만, 기존 방법은 쓸모없는 가중치를 영구히 지우되 입력에 맞춰 바뀌지 못하는 정적 가지치기(SP)와, 입력의 희소성(0인 값이 많은 성질)에 맞추지만 실행 중 불규칙성을 낳는 동적 가지치기(DP) 가운데 하나에 머문다. 연구진은 비정형 정적 가지치기와 입력 적응형 동적 가지치기를 합쳐 GPU에서 대형 언어 모델을 효율적으로 추론하는 희소 추론 틀 SPDP를 내놓았다. 새 압축 형식(Tiled-CBC)과 서로 보완하는 GPU 커널(GPU에서 돌아가는 계산 프로그램) 두 개를 함께 설계했는데, 하나는 실행 중 활성값(신경망 층을 지나며 계산된 중간 값)을 세밀하게 건너뛰는 CUDA 코어용 커널이고, 다른 하나는 입력 문맥을 한꺼번에 처리하는 단계(프리필)에 맞춘 텐서 코어용 커널이다. 형식과 커널을 함께 설계해 추론의 두 단계 모두에서 대역폭 효율이 좋은 메모리 접근과 높은 계산 밀도를 유지했다. 추론용 GPU에서 SpInfer 같은 최신 희소 추론 틀보다 평균 1.24–1.37배(최대 2.51배) 빨랐고, 희소도를 최대 25% 높이면서도 퍼플렉서티(언어 모델이 다음 낱말을 얼마나 잘 맞히는지 재는 지표)는 같은 수준을 유지했다.[^p8] | 1저자 Jinhyeok Kim, 마지막 저자 도재영(랩 표기 ^) |

## 교수와 전문 분야

도재영 교수(Jaeyoung Do)는 서울대 전기·정보공학부 조교수(Assistant Professor)이다.[^ece] 협동과정 인공지능 전공 교수진 목록에도 조교수로 올라 있고,[^ipai] 연구실 누리집의 교수 경력은 협동과정 인공지능에서의 직위를 Adjunct Professor(2024–현재)로 적는다.[^people] 자동화시스템공동연구소 참여교수 명단에도 이 연구실과 함께 올라 있다.[^asri] 학과 교수 소개의 분야는 생성형 AI, 머신러닝, 자연어 처리, 빅데이터/AI 시스템, 차세대 메모리다.[^ece]

KAIST 전산학 학사(2003–2007)를 받고, 미국 위스콘신대학교 매디슨(University of Wisconsin-Madison)에서 컴퓨터과학 석사(2007–2009)와 박사(2009–2012)를 받았다.[^ece] 박사 지도교수는 Jignesh M. Patel 교수다.[^jydo] 박사 뒤에는 Microsoft Database Lab의 Research Engineer(2012년 12월–2014년 2월), Microsoft Jim Gray Systems Lab(GSL)의 Senior Scientist(2014년 3월–2016년 9월), Microsoft Research(MSR)의 Senior Researcher(2016년 10월–2021년 2월), Amazon Alexa AI의 Senior Applied Scientist(2021년 3월–2023년 11월)로 일했고, 2024년 2월 서울대 전기정보공학부 조교수가 됐다.[^ece] 교수 개인 누리집은 서울대 부임 전(Pre 2024) Amazon과 Microsoft에서 인턴과 연구 조교 12명을 지도한 기록을 싣는다.[^jydo]

학과 교수 소개는 연구 관심을 다섯 가지로 적는다. 인공지능을 활용한 빅데이터 관리 시스템 최적화, 대형 언어 모델(LLM) 기반 생성형 AI와 대규모 딥러닝 훈련·추론, 멀티모달 AI를 통한 자연어·비전 처리, 기계학습·인공지능 응용을 위한 알고리즘·시스템 통합 설계, 차세대 메모리를 활용한 고성능 인공지능 데이터 분석·처리다.[^ece] 개인 누리집은 함께 연구할 학생을 찾는 주제로 이에 더해 물리적 상호작용과 로봇 행동 계획에 초점을 둔 에이전트·몸을 가진 인공지능, 의료·제조 산업을 위한 대규모 딥러닝 모델과 기반 시설을 든다.[^jydo]

교수 개인 누리집의 수상 목록은 DaMoN 2009 Best Paper Award, UW-Madison Computer Science Scholarship(2010), Samsung Scholarship for Graduate Study(2007–2012), KAIST Undergraduate Research Fellowship(2006), Ministry of Information and Communication Scholarship(2004), Korea Science and Engineering Foundation Scholarship(2003–2007)이다.[^jydo] 서울대에서 2024년 봄 Large Language Models - Applications and Use Cases, 2024년 가을 Data Structures를 강의했다.[^jydo]

논문으로 보면 전문 분야는 데이터베이스 시스템과 저장장치에서 출발해 대형 언어 모델·멀티모달 모델과 그 시스템 효율로 넓어졌다. 2009–2014년에는 플래시 메모리로 만든 저장장치(SSD)를 데이터베이스에 쓰는 연구가 중심이다. SSD로 데이터베이스 버퍼 풀(자주 쓰는 데이터를 메모리에 올려 두는 공간)을 키우는 연구(SIGMOD 2011, ICDE 2013)와 SSD 안에서 질의를 처리하는 스마트 SSD 연구(SIGMOD 2013)가 있다.[^pubs] 2019–2021년에는 저장장치 안에서 계산까지 하는 프로그래머블 SSD·계산 저장장치(Communications of the ACM 2019, The VLDB Journal 2021, CIDR 2021)와 학습형 인덱스 ALEX(SIGMOD 2020)를 다뤘다.[^pubs] Amazon 시기인 2022–2023년 논문에는 대화 시스템의 잘못된 행동 교정(ACL 2023), 문맥 속 지시의 평생 학습(ACL 2023), 이미지 분류기의 반사실적 설명을 글 개념 공간에 잇는 연구(CVPR 2023), 그래프 신경망 추천 시스템(CIKM 2022)이 있다.[^pubs] 서울대 시기에는 대형 언어 모델의 정렬과 추론 평가(대표 논문 1, 2), 비전-언어·옴니모달 모델(대표 논문 3–5), 로봇 행동 모델(대표 논문 6), 벡터 데이터베이스와 추론 효율(대표 논문 7, 8)로 이어진다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

연구실 누리집은 의료와 산업을 응용 분야로 든다. 의료에서는 영상·생체 신호·전자 건강 기록 같은 복잡한 의료 자료를 해석해 진단, 치료 계획, 결과 예측을 돕는 정확하고 해석할 수 있는 모델을, 산업에서는 예측 정비, 공정 최적화, 지능형 자동화를 목표로 한다.[^home] 대표 논문이 직접 든 쓰임은 다음과 같다. 의료 비전-언어 모델은 실제 병원 업무에서 모은 자료로 환자 관찰과 의사 결정 지원 업무에 쓰일 수 있는지 평가했고,[^p5] 옴니모달 모델은 실시간 옴니모달 시스템, 자료 종류를 넘나드는 검색과 생성, 몸을 가진 멀티모달 에이전트의 바탕으로 제시됐다.[^p4] 가지치기 틀은 대규모 대형 언어 모델 서비스의 처리량과 전력당 성능을 높일 수 있다고 보고,[^p8] 난도 조절 벤치마크는 프라이버시를 지키는 대리 작업 부하로 연구용 벤치마크와 실제 평가를 잇는다.[^p7]

최근 논문 목록에는 다른 의료 응용 논문도 있다. 극조산아(very preterm infants)의 조기 폐동맥 고혈압을 기계학습으로 예측하는 모델(ASPR 2026), 대형 언어 모델로 진료 기록을 관리해 의료진의 일을 돕는 시스템 AscleAI(CHI 2024)다. 수식이 든 말소리를 수식으로 바꾸는 MathSpeech(AAAI 2025)와 수학 문서를 읽어 주는 음성 합성 MathReader(ICASSP 2025)도 있다.[^pubs]

## 구성원

2026년 10월 23일 랩 People 페이지 기준이다. Ph.D. Students(1명), M.S./Ph.D. Students(14명), M.S. Students(6명), Interns(2명) 칸의 23명이며, 과정은 칸 이름을 옮겼다(M.S./Ph.D. Students는 석박사통합과정, Interns는 인턴). 연구 주제와 이메일은 카드 표기다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다. Hyeonggeun Kim은 대표 논문 4의 저자 목록에 Hyunggeun Kim으로 올라 있다.[^pubs]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Sunghwan Steve Cho | 박사과정 | Large Language Model | steve97@snu.ac.kr | 5 |
| Sieun Hyeon | 석박사통합과정 | LLM application, Multimodal LLM | zxc2692@snu.ac.kr | 1, 4 |
| Mintaek Lim | 석박사통합과정 | Vector DB, Data System | victorlim@snu.ac.kr | 4, 7 |
| Woohyeon Park | 석박사통합과정 | Vision-Language Model | woohyeon@snu.ac.kr | 3, 5 |
| Jaeik Kim | 석박사통합과정 | Physical AI | jake630@snu.ac.kr | 3, 4, 5, 6 |
| Yejoon Lee | 석박사통합과정 | Language Model | leeyejoon@snu.ac.kr | 2, 4, 8 |
| Jinhyeok Kim | 석박사통합과정 | Machine learning accelerator | jhkim00@snu.ac.kr | 6, 8 |
| Geon Choi | 석박사통합과정 | Vector DB, Physical AI | cds06126@snu.ac.kr | 6 |
| Woojin Kim | 석박사통합과정 | LLM Value Alignment, Diffusion Language Model | wjk9904@snu.ac.kr | 1, 3, 4 |
| Hoeun Lee | 석박사통합과정 | Physical AI | hoeunlee@snu.ac.kr | 4, 6 |
| Dogeun Kim | 석박사통합과정 | CXL, LLM Inference⋅Train | kdg6245@snu.ac.kr | 4, 7 |
| Yunseok Han | 석박사통합과정 | Generative Models | qicher@snu.ac.kr | 2, 4 |
| Jihwan Hong | 석박사통합과정 | Video Understanding, Video Generation | csjihwanh@snu.ac.kr | 4 |
| Seokjin Lee | 석박사통합과정 | World Model, Multimodal LLM |  |  |
| Minwoo Kim | 석박사통합과정 | Data Analytics, Machine Learning for Systems |  | 7 |
| Hanjun Lee | 석사과정 | LLM Agent, Planning in Mobile Environment | hj153lee@snu.ac.kr |  |
| Hyeonggeun Kim | 석사과정 | Robotics, Artificial Intelligence | khenrydragon@snu.ac.kr | 4, 6 |
| Jusang Oh | 석사과정 | Multimodal LLM | dhwntkd412@snu.ac.kr | 1, 6 |
| Yongha Lee | 석사과정 | Large Language Model, LLM Reasoning/Alignment, Multimodal LLM | finde159@snu.ac.kr |  |
| Phan Tri Nguyen | 석사과정 | Language Model |  |  |
| Jihoon Kwon | 석사과정 | Representation Learning, Multimodal Agent |  |  |
| Yuchan Lee | 인턴 | Efficient AI Systems, Multimodal AI | yuchan0321@snu.ac.kr |  |
| Jihwan Gong | 인턴 | Physical AI | gjh020717@snu.ac.kr |  |

## 최근 논문 목록 (2021–2027)

랩 Publications 페이지의 2021–2027년 연도 구역 40편과 arXiv 구역 2편, 모두 42편이다. 연도는 페이지의 연도 구역이고 arXiv 구역의 2편은 사전 공개 연도(2026)에 넣었다. 제목·저자·학회와 학술지 이름, 이름 뒤 괄호의 발표 형식 표시(Oral, Award Candidate)는 랩 표기 그대로다. 저자 이름 뒤 \*와 ^도 랩 표기다(교수 개인 누리집 범례: \* 1저자, ^ 교신저자).[^pubs][^jydo] 학회 일정이 2026년 10월 22일 뒤이고 누리집 소식이 채택을 알린 5편(NeurIPS 2026 3편, EMNLP 2026 1편, VLDB 2027 1편)에는 「채택」을 붙여 출판 논문과 구분했다.[^pubs][^news] 2027년 구역의 SIGMOD 2027 논문은 학회 발표 전에 학술지 Proceedings of the ACM on Management of Data 4권 4호(2026)에 실렸다.[^chat] 이 목록은 교수의 논문을 모은 목록이어서, 2021–2023년 구역의 12편은 교수가 서울대에 부임한 2024년 2월 전, Microsoft Research와 Amazon Alexa AI에 있던 때의 논문이다. 2024년 구역의 2편에도 지금 구성원 명단의 이름은 없다.[^pubs][^ece][^people]

**2027**

- Mintaek Lim\*, Sieun Hyeon, Geon Choi, Jaeyoung Do^. "Federated Vector Retrieval across Heterogeneous VectorDBs". *Proceedings of the 53rd International Conference on Very Large Data Bases (VLDB), 2027 (Oral) (VLDB 2027 채택)*.
- Geon Choi\*, Hoeun Lee, Jaeyoung Do^. "Exploiting Structural Properties for Efficient Constraint-Aware HNSW Hyperparameter Tuning". *ACM SIGMOD/PODS International Conference on Management of Data (SIGMOD), 2027 (Oral)*.

**2026**

- Woojin Kim\*, Jaeyoung Do^. "Values Are Not Single Labels: Distributional Value Profiling Across Groups and Contexts". *40th Annual Conference on Neural Information Processing Systems (NeurIPS), 2026 (NeurIPS 2026 채택)*.
- Hoeun Lee\*, Jaeik Kim, Jusang Oh, Jinhyeok Kim, Geon Choi, Hyeonggeun Kim, Jaeyoung Do^. "Dynin-Robotics: Omnimodal Unified Diffusion Vision-Language-Action Model". *40th Annual Conference on Neural Information Processing Systems (NeurIPS), 2026 (NeurIPS 2026 채택)*.
- Jihwan Hong\*, Woohyeon Park, Jaeik Kim, Jaeyoung Do^. "When Predicting Nothing Beats SAM 3: Revisiting Evaluation in Video Object Segmentation". *40th Annual Conference on Neural Information Processing Systems (NeurIPS), Evaluations and Datasets Track (E&D), 2026 (NeurIPS 2026 채택)*.
- Sieun Hyeon\*, Jaeyoung Do^. "Beyond Retraining-Free MoE Compression: A Cost-Normalized Study of Post-Compression Adjustment". *The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2026 (EMNLP 2026 채택)*.
- Baek Sup Shin\*, Ju Sun Heo, Yongha Lee, Sunghwan Steve Cho, Seh Hyun Kim, Seung Han Shin, Ee-Kyung Kim, Jaeyoung Do, Han-Suk Kim. "Machine Learning-Based Prediction Model for Early Pulmonary Hypertension in Very Preterm Infants". *The 19th Congress of the Asian Society for Pediatric Research (ASPR), 2026 (Oral)*.
- Sieun Hyeon\*, Yejoon Lee\*, Mintaek Lim, Woojin Kim, Jaeik Kim, Jaeyoung Do^. "What Comes Next? Omni-StoryBench for Evaluating Story-Grounded Omnimodal Generation". *arXiv preprint (2609.37317), 2026*.
- Jaeik Kim\*, Jaeyoung Do^. "SUM: Unified Geometric Surgery on Spatio-Temporal Adaptation Vectors for Federated Class Incremental Learning". *The 19th European Conference on Computer Vision (ECCV), 2026*.
- Jinhyeok Kim\*, Yejoon Lee, Jaeyoung Do^. "Unified Static–Dynamic Pruning for Efficient LLM Inference". *Proceedings of the 52nd International Conference on Very Large Data Bases (VLDB), 2026 (Oral)*.
- Mintaek Lim\*, Dogeun Kim, Minwoo Kim, Jaeyoung Do^. "Revisiting Filtered ANN Benchmarks: A Hardness-Controlled Benchmark Generator for Realistic Evaluation". *Proceedings of the 52nd International Conference on Very Large Data Bases (VLDB), 2026 (Oral)*.
- Jaeik Kim\*, Yoonjae Baek, Aecheon Jung, Hongyeob Kim, Soyun Choi, Youngeun Kim, Jaeyoung Do, Sungeun Hong^. "Dual Path Semantic Segmentation with Locality Guidance Tokens". *Neurocomputing, 2026*.
- Chang Liu\*, Henghui Ding\*, Nikhila Ravi\*, Yunchao Wei\*, Shuting He\*, Song Bai\*, Philip Torr\*, Leilei Cao\*, Jinrong Zhang, Deshui Miao, Xusheng He, Dengxian Gong, Zhiyu Wang, Mingqi Gao, Jihwan Hong, Canyang Wu, Weili Guan, Jianlong Wu, Liqiang Nie, Xingsen Huang, Yameng Gu, Xiaogang Yu, Xin Li, Ming-Hsuan Yang, Sijie Li, Jungong Han, Quanzhu Niu, Shihao Chen, Yuanzheng Wu, Yikang Zhou, Tao Zhang, Haobo Yuan, Lu Qi, Shunping Ji, Chao Yang, Chao Tian, Guoqing Zhu, Kai Yang, Zhifan Mo, Haijun Zhang, Xudong Kang, Shutao Li, Jaeyoung Do. "Report of the 5th PVUW Challenge: Towards More Diverse Modalities in Pixel-Level Understanding". *CVPR 2026 Workshop on Pixel-level Video Understanding in the Wild (PVUW) (CVPRW), 2026*.
- Woojin Kim\*, Sieun Hyeon, Jusang Oh, Jaeyoung Do^. "VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in Large Language Models". *Forty-Third International Conference on Machine Learning (ICML), 2026 (Oral)*.
- Sieun Hyeon\*, Jusang Oh, Sunghwan Steve Cho, Jaeyoung Do^. "MATA: Multi-Agent Framework for Reliable and Flexible Table Question Answering". *Findings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL Findings), 2026*.
- Sunghwan Steve Cho\*, Yunseok Han, Jaeyoung Do^. "MI-CXR: A Benchmark for Longitudinal Reasoning over Multi-Interval Chest X-rays". *Findings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL Findings), 2026*.
- Jaeik Kim\*, Woojin Kim, Jihwan Hong, Yejoon Lee, Sieun Hyeon, Mintaek Lim, Yunseok Han, Dogeun Kim, Hoeun Lee, Hyunggeun Kim, Jaeyoung Do^. "Dynin-Omni: Omnimodal Unified Large Diffusion Language Model". *arXiv preprint (2604.00007), 2026*.
- Woohyeon Park\*, Jaeik Kim, Sunghwan Steve Cho, Pa Hong, Woo Kyoung Jeong, Yoojin Nam, Nam-Joon Kim, Ginny Wong, Ka Chun Cheung, Jaeyoung Do^. "Medic-AD: Towards Medical Vision-Language Model's Clinical Intelligence". *The IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2026 (Oral, Award Candidate)*.
- Jihwan Hong\*, Jaeyoung Do^. "VIRST: Video-Instructed Reasoning Assistant for SpatioTemporal Segmentation". *The IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2026*.
- Yunseok Han\*, Yejoon Lee, Jaeyoung Do^. "RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models". *The Fourteenth International Conference on Learning Representations (ICLR), 2026*.
- Kun-Woo Shin\*, Jay H. Park, Moonwook Oh, Yohan Jo, Jaeyoung Do, Sang-Won Lee. "MatKV: Trading Compute for Flash Storage in LLM Inference". *42nd IEEE International Conference on Data Engineering (ICDE), 2026 (Oral)*.

**2025**

- Woojin Kim\*, Jaeyoung Do^. "Don’t Let It Fade: Preserving Edits in Diffusion Language Models via Token Timestep Allocation". *39th Annual Conference on Neural Information Processing Systems (NeurIPS), 2025*.
- Jaeik Kim\*, Jaeyoung Do^. "Exploring and Leveraging Class Vectors for Classifier Editing". *39th Annual Conference on Neural Information Processing Systems (NeurIPS), 2025*.
- Jaeik Kim\*, Woojin Kim, Woohyeon Park, Jaeyoung Do^. "MMPB: It’s Time for Multi-Modal Personalization". *39th Annual Conference on Neural Information Processing Systems (NeurIPS), Datasets and Benchmarks Track (D&B), 2025*.
- Joobo Shim\*, Jaewon Oh, Hongchan Roh, Jaeyoung Do^, Sang-Won Lee. "Turbocharging Vector Databases using Modern SSDs". *Proceedings of the 51st International Conference on Very Large Data Bases (VLDB), 2025 (Oral)*.
- Woohyeon Park\*, Woojin Kim, Jaeik Kim, Jaeyoung Do^. "SECOND: Mitigating Perceptual Hallucination in Vision-Language Models via Selective and Contrastive Decoding". *Forty-Second International Conference on Machine Learning (ICML), 2025*.
- Sieun Hyeon\*, Kyudan Jung, Nam-Joon Kim, Hyun Gon Ryu, Jaeyoung Do^. "MathReader: Text-to-Speech for Mathematical Documents". *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), 2025 (Oral)*.
- Sieun Hyeon\*, Kyudan Jung\*, Jaehee Won, Nam-Joon Kim, Hyun Gon Ryu, Hyuk-Jae Lee, Jaeyoung Do^. "MathSpeech: Leveraging Small LMs for Accurate Conversion in Mathematical Speech-to-Formula". *Proceedings of the 39th Annual AAAI Conference on Artificial Intelligence (AAAI), 2025*.

**2024**

- Dehong Xu, Liang Qiu, Minseok Kim, Faisal Ladhak, Jaeyoung Do. "Aligning Large Language Models via Fine-grained Supervision". *Proceedings of the Annual Meeting Of The Association For Computational Linguistics (ACL), 2024*.
- Jiyeon Han\*, Jimin Park\*, Jinyoung Huh, Uran Oh^, Daehee Kim, Jaeyoung Do^. "AscleAI: A LLM-based clinical note management system for enhancing clinician productivity". *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI), 2024*.

**2023**

- Jungbeom Lee, Sungjin Lee, Jinseok Nam, Seunghak Yu, Jaeyoung Do, Tara Taghavi. "Weakly supervised referring image segmentation with intra-chunk and inter-chunk consistency". *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2023*.
- Sarthak Ahuja, Mohammad Kachuee, Fatemeh Sheikholeslami, Weiqing Liu, Jaeyoung Do. "Scalable and Safe Remediation of Defective Actions in Self-Learning Conversational Systems". *Proceedings of the 61st Annual Meeting Of The Association For Computational Linguistics (ACL), 2023*.
- Jisoo Mok, Jaeyoung Do, Sungjin Lee, Tara Taghavi, Seunghak Yu, Sungroh Yoon. "Large-scale lifelong learning of in-context instructions and how to tackle it". *Proceedings of the 61st Annual Meeting Of The Association For Computational Linguistics (ACL), 2023*.
- Siwon Kim, Jinoh Oh, Sungjin Lee, Seunghak Yu, Jaeyoung Do, Tara Taghavi. "Grounding counterfactual explanation of image classifiers to textual concept space". *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2023*.
- Huaicheng Li, Martin L Putra, Ronald Shi, Fadhil I Kurnia, Xing Lin, Jaeyoung Do, Achmad Imam Kistijantoro, Gregory R Ganger, Haryadi S Gunawi. "Extending and programming the NVMe I/O determinism interface for Flash Arrays". *ACM Transactions on Storage (ToS), 2023*.
- Ji-Hoon Kim, Yeo-Reum Park, Jaeyoung Do, Soo-Young Ji, Joo-Young Kim. "Accelerating Large-Scale Graph-Based Nearest Neighbor Search on a Computational Storage Platform". *IEEE Transactions on Computers (ToC), 2023*.

**2022**

- Minseok Kim, Jinoh Oh, Jaeyoung Do, Sungjin Lee. "Debiasing neighbor aggregation for graph neural network in recommender systems". *Proceedings of the ACM International Conference on Information & Knowledge Management (CIKM), 2022*.
- Yeo-Reum Park, Ji-Hoon Kim, Jaeyoung Do, Joo-Young Kim. "A Dual-Mode Similarity Search Accelerator based on Embedding Compression for Online Cross-Modal Image-Text Retrieval". *IEEE 30th Annual International Symposium on Field-Programmable Custom Computing Machines (FCCM), 2022*.

**2021**

- Ji-Hoon Kim, Yeo-Reum Park, Jaeyoung Do, Soo-Young Ji, Joo-Young Kim. "Accelerating large-scale nearest neighbor search with computational storage device". *IEEE 29th Annual International Symposium on Field-Programmable Custom Computing Machines (FCCM), 2021*.
- Jaeyoung Do, Chen Luo, David Lomet. "Programming an SSD controller to support batched writes for variable-size pages". *IEEE 37th International Conference on Data Engineering (ICDE), 2021*.
- Jaeyoung Do, Ivan Luiz Picoli, David Lomet, Philippe Bonnet. "Better database cost/performance via batched I/O on programmable SSD". *The VLDB Journal (VLDB J.), 2021*.
- Antonio Barbalace, Jaeyoung Do. "Computational storage: Where are we today?". *11th Conference on Innovative Data Systems Research (CIDR), 2021*.

## 특허

교수 개인 누리집 논문 목록이 특허([P])로 표시한 5건 가운데 2021년 이후 항목 1건이다. 교수가 서울대에 부임하기 전의 항목이고, 이름·발명자·번호는 누리집 표기 그대로다.[^jydo]

- 2023 · Storage device and memory system (발명자 Soo Young Ji, Joo Young Kim, Ji Hoon Kim, Jaeyoung Do, Yeo Reum Park; 번호 US Patent (No: 17696586))

## 수상과 선정

랩 News 페이지에서 상 후보 선정과 대회 입상을 알린 글 2건이다. 날짜와 문구는 랩 표기 그대로다.[^news]

- May 26, 2026 · Medic-AD has been nominated as an award candidate at CVPR 2026!
- March 20, 2026 · 3rd place in PVUW MeViS-Audio Challenge at CVPR 2026!

## 소식

랩 News 페이지의 나머지 글 19건이다(2025년 2월–2026년 10월). 날짜와 문구는 랩 표기 그대로다.[^news] 누리집 Seminar 페이지는 2025년 여름의 확산 모델 튜토리얼(Diffusion Seminar, 2025년 7월 25일)과 에이전트 튜토리얼(Agents Seminar, 2025년 7월 31일), AIDAS Seminar(2026년 2월 13일)의 세 세미나 묶음을 싣는다.[^seminar]

- October 19, 2026 · 1 paper has been accepted to VLDB 2027!
- September 24, 2026 · 3 papers have been accepted to NeurIPS 2026!
- August 20, 2026 · 1 paper has been accepted to EMNLP 2026!
- July 2, 2026 · 2 papers have been accepted to VLDB 2026!
- June 18, 2026 · 1 paper has been accepted to ECCV 2026!
- June 13, 2026 · 1 paper has been accepted to SIGMOD 2027!
- May 26, 2026 · VALUEFLOW has been selected for an oral presentation at ICML 2026!
- May 1, 2026 · VALUEFLOW has been accepted to ICML 2026 as a Spotlight!
- April 9, 2026 · Medic-AD has been selected for an oral presentation at CVPR 2026!
- April 7, 2026 · 2 papers have been accepted to ACL 2026 Findings!
- February 23, 2026 · 2 papers got accepted to CVPR 2026!
- January 27, 2026 · 1 paper got accepted to ICLR 2026!
- January 4, 2026 · 1 paper got accepted to ICDE 2026!
- September 19, 2025 · 3 papers got accepted to NeurIPS 2025!
- August 1, 2025 · 1 paper got accepted to VLDB 2025!
- July 1, 2025 · 1 paper got accepted to ICML 2025!
- June 25, 2025 · Our new website is now live
- April 1, 2025 · 1 paper got accepted to ICASSP 2025!
- February 1, 2025 · 1 paper got accepted to AAAI 2025!

## 연락과 위치

- 주소: 1, Gwanak-ro, Gwanak-gu, Building #301, Office #808, Seoul 08826, Republic of Korea[^contact]
- 교수 연구실: 301동 808호(전기·정보공학부 교수 소개 표기)[^ece]
- 전화: 02-880-1782[^ece][^ipai]
- 교수 이메일: jaeyoung.do@snu.ac.kr[^contact]
- 누리집 바닥글이 연결한 연구실 계정: GitHub <https://github.com/AIDASLab>, Hugging Face <https://huggingface.co/snu-aidas>, YouTube <https://www.youtube.com/@AIDAS-Lab>[^home]
[^p1]: W. Kim, S. Hyeon, J. Oh, J. Do, ICML 2026(랩 표기 Forty-Third International Conference on Machine Learning, Oral), arXiv:2602.03160 (2026). <https://arxiv.org/abs/2602.03160> 초록 기준(arXiv 판).
[^p2]: Y. Han, Y. Lee, J. Do, ICLR 2026(랩 표기 The Fourteenth International Conference on Learning Representations), arXiv:2602.17053 (2026). <https://arxiv.org/abs/2602.17053> 초록 기준(arXiv 판).
[^p3]: W. Park, W. Kim, J. Kim, J. Do, ICML 2025(랩 표기 Forty-Second International Conference on Machine Learning), arXiv:2506.08391 (2025). <https://arxiv.org/abs/2506.08391> 초록 기준(arXiv 판).
[^p4]: J. Kim 외, J. Do, arXiv:2604.00007 (2026, 사전 공개본). <https://arxiv.org/abs/2604.00007> 초록 기준(arXiv 판).
[^p5]: W. Park 외, J. Do, CVPR 2026(랩 표기 The IEEE/CVF Conference on Computer Vision and Pattern Recognition, Oral, Award Candidate), arXiv:2603.27176 (2026). <https://arxiv.org/abs/2603.27176> 초록 기준(arXiv 판).
[^p6]: H. Lee 외, J. Do, NeurIPS 2026 채택(랩 표기 40th Annual Conference on Neural Information Processing Systems), arXiv:2609.13053 (2026). <https://arxiv.org/abs/2609.13053> 초록 기준(arXiv 판).
[^p7]: M. Lim, D. Kim, M. Kim, J. Do, Proceedings of the VLDB Endowment 19(10), 2763-2776 (온라인 2026-09-03). <https://doi.org/10.14778/3828612.3828630> 초록 기준.
[^p8]: J. Kim, Y. Lee, J. Do, Proceedings of the VLDB Endowment 19(11), 2950-2963 (온라인 2026-09-04). <https://doi.org/10.14778/3836663.3836665> 초록 기준.
[^home]: 연구실 누리집 첫 화면 <https://aidas.snu.ac.kr/> (소개문, Flagship Projects, Research Areas, 바닥글, 2026-10-23 열람)
[^people]: People 페이지 <https://aidas.snu.ac.kr/people/> (교수 카드, 구성원 카드, 2026-10-23 열람)
[^pubs]: Publications 페이지 <https://aidas.snu.ac.kr/publications/> (논문 목록, 2026-10-23 열람)
[^news]: News 페이지 <https://aidas.snu.ac.kr/news/> 와 글 21건 (2026-10-23 열람)
[^robots]: Robots 페이지 <https://aidas.snu.ac.kr/hardware/> (보유 로봇 목록, 2026-10-23 열람)
[^seminar]: Seminar 페이지 <https://aidas.snu.ac.kr/seminar/> (2026-10-23 열람)
[^contact]: Contact 페이지 <https://aidas.snu.ac.kr/contact/> (2026-10-23 열람)
[^jydo]: 교수 개인 누리집 <https://sites.google.com/view/jydo/home> (소개, 논문·특허 목록과 범례, 수상, 강의, 지도 기록, 2026-10-23 열람)
[^ece]: 서울대 전기·정보공학부 교수 소개(도재영) <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p901> (2026-10-23 열람)
[^ecelab]: 서울대 전기·정보공학부 연구실 소개(인공지능 및 빅데이터 시스템 연구실) <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=143> (2026-10-23 열람)
[^ecelist]: 서울대 전기·정보공학부 연구실 목록 <https://ece.snu.ac.kr/research-faculty/research/lab> (2026-10-23 열람)
[^ipai]: 서울대 협동과정 인공지능 전공 교수진 목록 <https://gsai.snu.ac.kr/%ea%b5%90%ec%88%98%ec%a7%84-%eb%aa%a9%eb%a1%9d/> (2026-10-23 열람)
[^asri]: 서울대 자동화시스템공동연구소 참여교수 <https://asri.snu.ac.kr/%ec%a1%b0%ec%a7%81/%ec%b0%b8%ec%97%ac%ea%b5%90%ec%88%98/> (2026-10-23 열람)
[^chat]: G. Choi, H. Lee, J. Do, Proceedings of the ACM on Management of Data 4(4), 1-26 (온라인 2026-09-29). <https://doi.org/10.1145/3837111>

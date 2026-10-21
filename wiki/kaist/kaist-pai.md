# 심리 인공지능 연구실 (KAIST Psychological AI Lab)

**KAIST 디지털인문사회과학부·뇌인지과학과·데이터사이언스대학원 · 이상호 교수**

- 분야: 계산 인지 모델링, 심리학과 인공지능의 접점, 역강화학습, 시각 주의와 억제 통제, 베이지안 적응형 실험 설계, 의사결정과 중독의 계산 지표
- 대분야: 인문·사회·경제, 컴퓨팅·AI
- 태그: 인지과학·의사결정[^home], 강화학습[^p1]
- 홈페이지: <https://sites.google.com/view/kaist-pai/home>
- 근거와 출처: [Psychological AI Lab 근거 페이지](kaist-pai-sources.md)

> 인공지능으로 사람의 행동과 개인차를 설명하고, 사람의 인지 원리를 본떠 인공지능을 더 낫게 만드는 연구실이다. 운전 과제처럼 실제에 가까운 상황의 행동을 인공지능 모형으로 분석하고, 주의·충동성·의사결정 같은 인지 특성을 수학 모형으로 재며, 적은 시행으로 믿을 만한 측정을 얻는 실험 설계를 연구한다.[^home][^p1][^p2][^p5]

## 무엇을 연구하나

연구실은 심리학과 인공지능이 서로에게 배울 수 있다는 데서 출발한다고 소개한다. 복잡한 자료를 예측하는 인공지능 모형은 복잡한 현실 속 사람의 행동을 설명하는 새 길을 열고, 사람의 마음을 이해하면 인공지능이 뇌의 처리 과정에서 영감을 얻은 효율적인 기능을 갖추고 사람처럼 행동하며 사람과 협업하게 도울 수 있다는 것이다. 이를 위해 "인공지능으로 사람의 행동을 어떻게 설명할 수 있나"(AI in Psychology)와 "사람의 인지 기능을 넣어 인공지능을 개선할 수 있나"(Psychology in AI) 두 질문을 던지고, 계산 인지 모델링, 딥러닝, (역)강화학습을 방법으로 쓴다.[^home]

AI in Psychology 갈래는 비디오 게임과 가상현실에서 사람의 복잡한 행동을 흉내 내는 인공지능 에이전트를 훈련하고 해석해 행동과 특성의 개인차를 설명하려 한다. Psychology in AI 갈래는 많은 정보를 빠르게 걸러 관련 자극에 집중하는 사람의 주의 기제처럼, 인지심리학 이론과 사람 실험 자료에 바탕한 설명 가능한 인공지능을 만들려 한다. 바탕이 되는 계산 인지 모델링은 행동과 뇌 활동 밑의 인지 과정을 설명하는 계산·수학 모형을 세우는 기법으로, 디지털 헬스케어와 인지 훈련에도 쓰인다고 적었다.[^home]

첫째 갈래는 **역강화학습으로 본 사람의 행동**이다. 실시간 운전 과제와 역강화학습(행동을 보고 그 사람이 무엇을 보상으로 여기는지 거꾸로 추정하는 방법)으로, 충동적인 사람이 위험한 상황에 높은 주관적 보상을 매긴다는 것을 보였다.[^p1]

둘째 갈래는 **시각 주의와 억제 통제의 측정**이다. 주의가 표적 주변을 억누르는 정도가 사람마다 다르고 작업 기억(정보를 잠시 붙들고 다루는 기억) 용량과 관련됨을 보였고,[^p2] 표적과 방해 자극의 거리를 바꾸는 플랭커 과제(가운데 표적 옆에 방해 자극을 두고 반응을 재는 과제)를 온라인으로 옮겨 실험실 판과 비슷한 결과를 얻었으며 일부 측정은 재검사 신뢰도가 좋았다.[^p3]

셋째 갈래는 **적응형 실험 설계와 계산 지표**다. 실험 설계를 시행마다 응답에 맞춰 최적화하는 베이지안 능동 학습으로 비기호 수 추정의 발달을 살폈고,[^p4] 이런 적응형 설계 최적화(ADO)가 인지 측정의 신뢰도와 효율을 높인다는 연구를 정리했으며,[^p5] 스마트폰 기반 짧은 의사결정 과제로 금연 치료 결과를 예측했다.[^p6]

## 주요 연구 주제

### 1. 역강화학습으로 본 사람의 행동

실시간 운전 과제의 주관적 보상 추정과 충동성.[^p1] 대표 논문 1.

### 2. 시각 주의와 억제 통제의 측정

주의 분포의 개인차, 온라인 간격 플랭커 과제.[^p2][^p3] 대표 논문 2, 3.

### 3. 적응형 실험 설계와 계산 지표

베이지안 능동 학습 수직선 과제, ADO 리뷰, 금연 예측 계산 지표.[^p4][^p5][^p6] 대표 논문 4–6.

## 대표 논문

랩 논문 목록의 2021–2026년 논문 가운데 이상호 교수가 1저자인 것과 2저자로 참여한 계산 정신의학 논문에서 연구 갈래를 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2024 | [Bridging the Gap Between Self-Report and Behavioral Laboratory Measures: A Real-Time Driving Task With Inverse Reinforcement Learning](https://doi.org/10.1177/09567976241228503) · Psychological Science | 충동성 같은 심리 특성을 잴 때 설문(자기 보고)과 행동 과제 점수가 서로 잘 맞지 않는 것이 큰 문제다. 실생활의 충동적 성향이 드러나는 실시간 운전 과제 "하이웨이 과제"를 만들었더니, 성인 47명(18–33세)에서 충동성 설문 점수가 이 과제 수행과는 강하게 상관했지만 기존 충동성 행동 과제와는 그렇지 않았다. 심층 신경망과 역강화학습을 합쳐 과제 중 주관적 보상의 변화를 추정했고, 충동적인 참가자는 비합리적이거나 위험한 상황에 높은 주관적 보상을 매겼다.[^p1] | 1저자 이상호, 마지막 저자 Woo-Young Ahn |
| 2 | 2022 | [Individual differences in selective attention reveal the nonmonotonicity of visual spatial attention and its association with working memory capacity](https://doi.org/10.1037/xge0000801) · Journal of Experimental Psychology: General | 시각 공간 주의는 흔히 주의 중심에서 멀어질수록 돕는 효과가 꾸준히 줄어든다고 여겨지지만, 표적 주변을 오히려 억누른다는 연구도 있다. 두 번의 플랭커 과제 실험에서, 주의 분포의 모양이 사람마다 다른 선택적 주의로 정해진다는 "주변 억제" 설명으로 이전 연구들의 엇갈림을 하나로 묶었다. 방해 자극의 간섭이 줄어드는 표적과의 거리는 사람마다 크게 달랐고 작업 기억 용량과 음의 상관을 보였다.[^p2] | 이상호(1저자)·Mark A. Pitt |
| 3 | 2024 | [Implementation of an online spacing flanker task and evaluation of its test–retest reliability using measures of inhibitory control and the distribution of spatial attention](https://doi.org/10.3758/s13428-023-02327-7) · Behavior Research Methods | 플랭커 과제는 시각 주의 연구에 널리 쓰인다. 표적과 방해 자극 사이 거리를 바꾸는 간격 플랭커 과제(SFT)는 공간에 걸친 주의 분포와 억제 통제를 함께 볼 수 있지만, 자극 크기와 보는 거리를 통제해야 해 온라인으로 하기 어렵다. 보정용 사전 검사 두 개를 넣은 온라인 SFT를 만들어 실험실 판과 비교했더니 모든 측정에서 비슷했고, 급내 상관계수(ICC, 반복 측정 결과가 일치하는 정도)로 볼 때 평균 플랭커 효과(ICC 0.745)와 거리별 불일치 시행 반응 시간(ICC 0.65–0.71)이 재검사 신뢰도가 좋은 측정이었다.[^p3] | 이상호(1저자)·Mark A. Pitt |
| 4 | 2022 | [A number-line task with a Bayesian active learning algorithm provides insights into the development of non-symbolic number estimation](https://doi.org/10.3758/s13423-021-02041-5) · Psychonomic Bulletin & Review | 수직선 과제는 0과 상한 수가 양 끝에 적힌 선 위에서 주어진 수의 위치를 짐작하게 해 수 표상을 살핀다. 아라비아 숫자 같은 기호 수와 점의 개수 같은 비기호 수의 추정이 같은 과정과 발달 경로를 따르는지 보려고, 실험 설계를 적응적으로 최적화하는 베이지안 능동 학습 알고리즘 GPAL(가우스 과정 능동 학습)을 썼다. 5–73세 참가자 238명의 비기호 수 추정에서 기호 수 추정의 특징 세 가지가 나타났다.[^p4] | 1저자 이상호, 마지막 저자 Jay I. Myung |
| 5 | 2023 | [Adaptive Design Optimization as a Promising Tool for Reliable and Efficient Computational Fingerprinting](https://doi.org/10.1016/j.bpsc.2022.12.003) · Biological Psychiatry: Cognitive Neuroscience and Neuroimaging | 정신 기능 이상은 원인과 양상이 사람마다 달라 여러 차원의 긴 검사가 필요하지만, 검사가 길어지면 피로와 산만함 때문에 개인차를 믿을 만하게 재기 어렵다. 시행마다 실험 설계를 바꿔 개인 특성 정보를 최대로 얻는 베이지안 적응형 설계 최적화(ADO)의 방법과, ADO가 잠재 신경인지 측정의 신뢰도와 효율을 높인다는 최근 연구를 정리한 리뷰다. 정신질환의 다양한 양상을 믿을 만하고 효율적으로 재는 ADO 기반 "계산 지문"을 제안했다.[^p5] | 1저자 Mina Kwon, 마지막 저자 Woo-Young Ahn(이상호는 2저자) |
| 6 | 2026 | [Rapid and reliable computational markers of decision-making for predicting daily smoking behavior and smoking cessation treatment outcomes](https://doi.org/10.1038/s41386-026-02448-5) · Neuropsychopharmacology | 중독에서는 감정과 가치에 따른 의사결정이 빠르게 바뀌어 금연을 방해하지만, 표준 의사결정 과제는 시행이 많이 필요해 일상에서 반복해 재기 어렵다. 스마트폰 일상 순간 평가(EMA)와 ADO를 합쳐 과제당 20–30회 시행으로 의사결정 변수를 추정하는 틀을 만들었다. 5–6주 금연 프로그램 참가자 79명에서 갈망·우울 증상·모호성 수용이 높으면 다음 날 흡연이 늘었고, 첫 주 자료만으로 치료 종료 시 금연 성공을 의미 있게 예측했다(예측이 얼마나 잘 맞는지 나타내는 AUC 평균 0.76).[^p6] | 1저자 Jeung-Hyun Lee, 마지막 저자 Woo-Young Ahn(이상호는 2저자) |

## 교수와 전문 분야

이상호 교수는 미국 오하이오주립대(The Ohio State University)에서 응용통계 석사(2020)와 인지심리학 박사(2021)를 받았고, 2024년부터 KAIST 조교수다. 소속은 디지털인문사회과학부, 뇌인지과학과, 데이터사이언스대학원이다.[^members] 데이터사이언스대학원 구성원 페이지는 연구 분야(Focus Area)를 바이오, 헬스케어, 뇌과학으로 적는다.[^gsds]

논문으로 보면 전문 분야는 세 갈래다.

- **역강화학습과 심층 신경망으로 실제에 가까운 과제의 행동과 개인차 설명**.[^p1]
- **시각 공간 주의와 억제 통제의 개인차 측정**.[^p2][^p3]
- **베이지안 능동 학습·적응형 설계로 적은 시행에서 믿을 만한 인지 측정**.[^p4][^p5][^p6]

## 응용 분야

누리집은 계산 인지 모델링이 디지털 헬스케어와 인지 훈련의 바탕이 된다고 적었고,[^home] Projects 페이지는 KAIST Center for Contemplative Science와 함께 인지 훈련·디지털 헬스케어용 가상현실 환경을 최적화하는 과제, FM Communications와 디지털 헬스케어 서비스의 감정 평가용 거대 언어 모형(LLM) 알고리즘을 만드는 산업체 과제를 든다.[^projects] 대표 논문으로 보면 충동성 같은 심리 특성의 측정, 정신질환의 계산 지표, 금연 치료 성공 예측에 닿아 있다.[^p1][^p5][^p6]

## 구성원

2026년 10월 20일 랩 Members 페이지 기준이다. 과정과 기간은 랩 표기다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Boyoung Kwon | 석박사통합과정 (2025.9 ~ Present) |  |
| Sihan Fu | 석사과정 (2025.9 ~ Present) |  |
| Junyup Kim | 석사과정 (2026.3 ~ Present) |  |
| Chaeho Lee | 석사과정 (2026.3 ~ Present) |  |
| Jiyoon Seo | 석사과정 (2026.3 ~ Present) |  |
| Young Min Jung | 입학 예정 석사과정 (2027.3 ~ Present) |  |
| Seo-Yeon Baek | 학부 연구생 |  |
| Sangjun Lee | 학부 연구생 |  |
| Sunghun Cho | 학부 연구생 |  |

## 최근 논문 목록 (2021–2026)

랩 Publications 페이지의 2021년 이후 논문이다. 2026년의 두 NeurIPS 논문은 랩이 게재 승인(accepted)으로 적은 것이다.[^papers]

**2026**

- Lee, C., Kim, J., Kim, W., Jung, Y. M., Lee, S. H. "Leveraging Psychophysical Attentional Distribution for Gaze-Augmented Reward Modeling". *Advances in Neural Information Processing Systems, 39 (NeurIPS 2026) (accepted)*.
- Kwon, B., Seo, J., Lee, S. H. "Discovering Structurally Plausible and Interpretable Cognitive Models with Large Language Models". *Advances in Neural Information Processing Systems, 39 (NeurIPS 2026) (accepted)*.
- Lee, J. H., Lee, S. H., Yang, J., Kim, H., Pitt, M., Park, H., ... & Ahn, W. Y. "Rapid and Reliable Computational Markers for Predicting Daily Smoking Behavior and Smoking Cessation Treatment Outcome". *Neuropsychoparmacology*.

**2024**

- Lee, S. H., Oh, M. H., & Ahn, W. Y. "Inverse reinforcement learning captures value representations in the reward circuit in a real-time driving task: a preliminary study". *Computational Cognitive Neuroscience*.
- Lee, S. H., Song, M. S., Oh, M. H., & Ahn, W. Y. "Bridging the gap between self-report and behavioral laboratory measures: A real-time driving task with inverse reinforcement learning". *Psychological Science, 35(4), 345-357*.
- Lee, S. H., & Pitt, M. A. "Implementation of an online spacing flanker task and evaluation of its test-retest reliability using measures of inhibitory control and the distribution of spatial attention". *Behavior Research Methods, 1-12*.

**2023**

- Kwon, M., Lee, S. H., Ahn, W. Y. "Adaptive design optimization as a promising tool for reliable and efficient computational fingerprinting". *Biological Psychiatry: Cognitive Neuroscience and Neuroimaging, 8(8), 798-804*.

**2022**

- Lee, S. H., Kim, D., Opfer, J., Pitt, M. A., & Myung, J. I. "A number-line task with a Bayesian active learning algorithm provides insights into the development of non-symbolic number estimation". *Psychonomic Bulletin & Review, 29(3), 1-14*.
- Lee, S. H., & Pitt, M. A. "Individual differences in selective attention reveal the non-monotonicity of visual spatial attention and its association with working memory capacity". *Journal of Experimental Psychology: General, 151(4), 749-762*.

## 연구 과제

랩 Projects 페이지에 적힌 과제다. 앞의 네 건은 연구실 자체 과제(In-Lab Projects), 뒤의 두 건은 공동 과제(Collaborative Projects)다.[^projects]

- Training AI agents that reflect human decision making and brain activity (type In-Lab Project)
- Developing AI models grounded in psychological theories of human attention (type In-Lab Project)
- Designing AI systems that generate and evaluate psychological models (type In-Lab Project)
- Building multi-agent AI systems that account for human individual differences (type In-Lab Project)
- (KAIST Center for Contemplative Science) Optimizing virtual reality environments for cognitive training and digital healthcare (type Collaborative Project)
- (Industry project with FM Communications) Developing LLM-based algorithms for emotion assessment in a digital healthcare service (type Collaborative Project)

## 연락과 위치

- 교수실: KAIST N4동 1311호, 디지털인문사회과학부[^contact]
- 교수 이메일: sangholee@kaist.ac.kr[^contact]

[^home]: 연구실 누리집 첫 화면 <https://sites.google.com/view/kaist-pai/home> (2026-10-20 열람)
[^members]: Members 페이지 <https://sites.google.com/view/kaist-pai/members> (2026-10-20 열람)
[^papers]: Publications 페이지 <https://sites.google.com/view/kaist-pai/publications> (2026-10-20 열람)
[^projects]: Projects 페이지 <https://sites.google.com/view/kaist-pai/projects> (2026-10-20 열람)
[^contact]: Contact 페이지 <https://sites.google.com/view/kaist-pai/contact> (2026-10-20 열람)
[^gsds]: KAIST 데이터사이언스대학원 구성원 페이지 <https://gsds.kaist.ac.kr/people> (2026-10-20 열람)
[^p1]: S. H. Lee, M. S. Song, M.-h. Oh, W.-Y. Ahn, Psychological Science 35, 345-357 (온라인 2024-02-26). <https://doi.org/10.1177/09567976241228503> 초록 기준.
[^p2]: S. H. Lee, M. A. Pitt, Journal of Experimental Psychology: General 151, 749-762 (2022). <https://doi.org/10.1037/xge0000801> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: S. H. Lee, M. A. Pitt, Behavior Research Methods 56, 5947-5958 (온라인 2024-01-16). <https://doi.org/10.3758/s13428-023-02327-7> 초록 기준.
[^p4]: S. H. Lee 외, J. I. Myung, Psychonomic Bulletin & Review 29, 971-984 (온라인 2021-12-16). <https://doi.org/10.3758/s13423-021-02041-5> 초록 기준(Europe PMC 등록 초록).
[^p5]: M. Kwon, S. H. Lee, W.-Y. Ahn, Biological Psychiatry: Cognitive Neuroscience and Neuroimaging 8, 798-804 (2023). <https://doi.org/10.1016/j.bpsc.2022.12.003> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: J.-H. Lee 외, W.-Y. Ahn, Neuropsychopharmacology 51, 1881-1890 (온라인 2026-05-29). <https://doi.org/10.1038/s41386-026-02448-5> 초록 기준.

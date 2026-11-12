# Computational Affective Neuroscience & Development Lab (CNDL)

**KAIST 의과학대학원 · 정범석 교수**

- 영문 이름: Laboratory for Computational affective Neuroscience and Development
- 분야: 지각·감정·행동 선택의 계산 모형, 몸 안 감각과 뇌 활동, 정서·생리 변화의 정량 관계[^research]
- 대분야: 기초생명·생물물리, 컴퓨팅·AI
- 태그: 계산신경과학[^research], 인지과학·의사결정[^research], 신경영상 분석·뇌 연결망[^research]
- 홈페이지: <https://drshrink.github.io/>
- 근거와 출처: [CNDL 근거 페이지](cndl-sources.md)

> 사람마다 느끼고 판단하는 방식이 다른 이유를 행동과 뇌 자료로 설명하는 계산 모형을 개발하는 연구실이다.

## 무엇을 연구하나

연구실은 행동 자료와 뇌 영상(뇌의 구조나 활동을 공간적으로 나타낸 자료)을 바탕으로, **사람마다 지각과 감정이 다른 이유, 정서 경험이 개인차를 형성하는 과정**을 설명하는 계산 모형(가정한 관계를 수학식과 계산 절차로 표현한 모형)을 개발한다.[^research] 감정 경험과 뇌 발달의 관계, 감정과 사회적 판단의 계산 모형, 청년기 정신 건강을 연구 관심으로 제시한다.[^home] 연구에 쓰는 자료로는 행동 자료와 뇌 영상 자료인 fMRI(뇌 활동에 따른 혈류 변화로 활동을 보는 영상), MRS(뇌 속 화학 물질의 양을 재는 분광법), DTI(물 분자의 퍼짐 방향으로 신경 다발의 구조를 보는 영상), EEG/MEG(뇌가 내는 전기·자기 신호의 기록) 등을 든다.[^research]

첫 갈래는 **자신이 결과에 영향을 준다는 믿음과 행동 선택**이다. 자신과 타인의 행동이 함께 결과에 영향을 줄 때, 각자의 행동과 결과 사이 관계를 결합해 통제력을 추론하는 베이지안 모형(사전의 믿음과 새 관찰을 결합해 가능한 설명의 확률을 갱신하는 모형)을 제안했다.[^p1] 다른 연구에서는 행동 선택에 대한 확신 정도를 이전 결과에 맞춰 조절하는 확률 모형을 만들고, 그 변화가 뇌 영역 사이의 활동 관계와 연결됨을 보였다.[^p2] 위험을 감수하는 선택에 대해서는 순차적으로 평가하는 방식과 미리 세운 평가를 함께 다루는 새 계산 틀을 제안했다.[^p3]

둘째 갈래는 **몸 안의 감각과 뇌의 정보 처리**다. 심박(심장이 뛰는 활동)을 의식적으로 알아차리는 것과 심박에 주의를 기울이는 것을 구분하고, 두 과정이 서로 다른 시점과 영역의 뇌 활동을 동반함을 보였다.[^p4] 심박 시점에 맞춰 뇌파(뇌의 전기적 활동을 기록한 신호)의 주파수(주기적 변화가 단위 시간 동안 반복되는 횟수) 성분이 어떻게 달라지는지 나타내는 방법도 제안했다. 신경망(연결된 계산 단위와 연결 강도로 입력과 출력의 관계를 학습하는 계산 모형) 가운데, 일정 범위의 입력에 같은 계산을 반복 적용해 부분적인 특징을 학습하는 합성곱 신경망을 이 표현에 맞춰 설계했다. 이를 이용해 사람이 몸 안 감각에 주의를 기울이는 상태를 분류했다.[^p5]

셋째 갈래는 **정서·월경 주기와 개인차의 정량 관계**다. 사회적 상호작용에서는 정서 경험과 경제적 선택이 상대방과 주고받는 맥락에 따라 어떻게 달라지는지 분석했다.[^p6] 월경 주기를 다룬 연구에서는 호르몬(몸의 특정 조직에서 만들어져 다른 조직의 활동을 조절하는 화학적 전달 물질) 변화와 뇌 상태를 전환하는 데 필요한 모형상의 비용 사이 관계를 분석했다. 인지 상태에 따라 전환 비용이 주기 중 다른 양상을 보인다고 보고했다.[^p7]

**신경 자극 기법의 공동연구**도 있다. 귀의 미주신경(뇌와 여러 몸속 기관 사이에서 정보를 주고받는 신경)을 특정 영역에서 비침습적으로, 즉 몸 안에 기구를 넣지 않고 자극하기 위해 밀리미터파를 이용하는 방법을 제안했다. 밀리미터파는 전기와 자기의 변화가 공간으로 퍼지는 파동 가운데 파장이 밀리미터 단위인 파동이며, 밀리미터는 미터의 천분의 일인 길이 단위다. 계산과 신경 반응 측정을 통해 국소 자극의 가능성을 보였다.[^p8]

## 주요 연구 주제

### 1. 행동 선택과 사회적 통제력의 계산 모형

자신과 타인의 행동·결과를 함께 반영하는 통제력 추론, 과거 결과에 따른 행동 선택의 확신 조절, 위험 선택의 순차 평가와 사전 평가를 다룬다.[^p1][^p2][^p3]

### 2. 심박 관련 감각과 신경 활동

심박의 의식적 자각과 몸 안 감각에 대한 주의를 구분하고, 심박에 시간을 맞춘 뇌 활동으로 주의 상태를 분류하는 방법을 연구한다.[^p4][^p5]

### 3. 정서·생리 변화와 개인차

사회적 맥락의 정서와 경제적 선택 사이 관계, 월경 주기(경구 피임약을 쓰지 않는 자연 주기)에 따른 뇌 상태 전환 비용의 변화를 정량적으로 분석한다.[^p6][^p7]

### 4. 국소 신경 자극

밀리미터파를 이용해 귀의 미주신경을 특정 영역에서 자극하는 비침습 기법의 가능성을 공동으로 연구했다.[^p8]

## 대표 논문

정범석 교수가 저자로 참여한 KAIST 재직 시기의 2021–2026년 연구 가운데 계산 모형, 심박 관련 측정 방법, 정서·생리의 정량 관계와 신경 자극 기법을 보여 주는 논문을 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. 사전 공개본은 학술지 논문과 구분해 표시한다.

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2021 | [Neurocomputational mechanism of controllability inference under a multi-agent setting](https://doi.org/10.1371/journal.pcbi.1009549) · PLoS Computational Biology | 여러 사람이 결과에 영향을 줄 때 자신의 통제력을 어떻게 판단하는지 설명하는 새 베이지안 모형을 제안했다. 자신의 행동·결과 관계와 타인의 행동·결과 관계를 함께 반영하는 모형이며, 이 추론에 관련된 뇌 활동도 분석했다. 자신에게 유리한 방향의 추론 편향은 통제력이 변하는 상황에서의 행동 적응과 관련됐다.[^p1] | 1저자 Jaejoong Kim, 마지막 저자·교신저자 Bumseok Jeong |
| 2 | 2025 | [Individual differences in policy precision: Links to suicidal risk and network dynamics](https://doi.org/10.1016/j.neuroimage.2025.121479) · NeuroImage | 이전 결과에 따라 행동 선택의 확신 정도를 조절하는 확률 모형을 개발했다. 내부 모형에 따른 예상과 직전 관찰 사이의 균형을 표현하며, 기존 강화학습(행동 결과로 받은 보상을 바탕으로 선택 규칙을 배우는 방법) 모형보다 개인별 선택 행동을 잘 설명했다. 확신 정도의 시간 변화를 반영하면 뇌 영역 간 활동 관계와 개인차를 설명하는 능력도 좋아졌다.[^p2] | 1저자 Dayoung Yoon, 마지막 저자 Bumseok Jeong |
| 3 | 2026 | [Policy precision reveals action-phase impulsivity in women with premenstrual syndrome during risk-taking](https://doi.org/10.64898/2026.03.12.711243) · bioRxiv, 사전 공개본 | 위험을 감수하는 행동에서 순차 평가와 사전 평가를 통합하고, 불확실성에 따른 정보 탐색을 설명하는 새 계산 틀을 제안했다. 행동 뒤 예상되는 불확실성과 선호 결과에서의 벗어남을 함께 다루는 기대 자유 에너지를 줄이는 틀이다. 기존 모형과 비교해 설명력이 좋았으며, 월경전증후군에 적용해 충동성을 학습 결함이 아니라 시행마다 이어지는 순차 평가에 대한 민감성(미리 세운 안정된 평가 대신)과 연결해 해석했다.[^p3] | 1저자 Dayoung Yoon, 마지막 저자 Bumseok Jeong |
| 4 | 2025 | [Conscious cardiac awareness and interoceptive attention differentially modulate heartbeat-evoked neural dynamics](https://doi.org/10.1016/j.neuroimage.2025.121606) · NeuroImage | 심장 박동을 의식적으로 알아차리는 과정과 박동에 주의를 기울이는 과정을 구분했다. 심박에 맞춰 나타나는 뇌 반응, 뇌 영역 간 활동의 연결, 짧은 시간 동안 유지되는 전기 활동의 공간적 양상을 분석해 두 과정이 서로 다른 뇌 활동을 동반함을 보였다.[^p4] | 1저자 Su Hyun Bong, 마지막 저자 Bumseok Jeong |
| 5 | 2024 | [Heartbeat-related spectral perturbation of electroencephalogram reflects dynamic interoceptive attention states in the trial-by-trial classification analysis](https://doi.org/10.1016/j.neuroimage.2024.120797) · NeuroImage | 심박을 기준으로 뇌파의 시간·주파수 성분을 나타내는 새 표현을 제안하고, 이 표현에 맞춘 합성곱 신경망으로 주의 상태를 분류했다. 새 참가자에게도 공통 분석 모형을 적용할 수 있음을 보였으며, 개인별 뇌파를 미리 모으지 않는 온라인 분류의 가능성을 제시했다.[^p5] | 1저자 Wooyong Lee, Bumseok Jeong은 6명 중 5번째 저자 |
| 6 | 2024 | [Prosocial emotions predict individual differences in economic decision-making during ultimatum game with dynamic reciprocal contexts](https://doi.org/10.1038/s41598-024-62203-y) · Scientific Reports | 사회적 정서를 자신과 타인에 대한 관련성, 감정에 대한 통제감 등 여러 차원으로 살폈다. 정서와 경제적 선택의 양상으로 사람들의 차이를 구분했고, 수락 행동과 정서가 외부 보상 구조를 따르는 상호적(reciprocal) 집단에서만 정서의 통제감에 대한 예상 오차와 선택이 연결됨을 보였다.[^p6] | 1저자 Jaewon Kim, 마지막 저자 Bumseok Jeong |
| 7 | 2026 | [Hormonal Modulation of Brain Control Energy Across the Menstrual Cycle: A Network Control Theory Study](https://doi.org/10.21203/rs.3.rs-11007587/v1) · Research Square, 사전 공개본 | 뇌의 구조적 연결과 기능적 상태를 함께 이용해, 월경 주기(자연 주기)에 따른 뇌 상태 전환 비용을 계산했다. 자연 주기의 호르몬 변화에 따라 일별 비용과 인지 상태 사이 전환 비용이 달라지는 양상을 보였다. 비용은 뇌 상태를 바꾸기 위한 수학 모형의 제어 비용을 뜻한다.[^p7] | 1저자 Hyun Soo Park, 마지막 저자 Bumseok Jeong |
| 8 | 2021 | [Feasibility study on transcutaneous auricular vagus nerve stimulation using millimeter waves](https://doi.org/10.1088/2057-1976/ac2c54) · Biomedical Physics & Engineering Express | 퍼져 나가는 전기 자극으로 목표 밖 신경까지 자극될 수 있다는 문제에서 출발해, 밀리미터파로 귀의 미주신경을 국소적으로 자극하는 방법을 개발했다. 수치 계산과 신경 반응 측정에서 자극 영역에 따른 반응 차이를 보였고, 선택적인 비침습 자극의 가능성을 제시했다.[^p8] | 1저자 Hi Yuen Song, Bumseok Jeong은 6명 중 5번째 저자 |

## 교수와 전문 분야

정범석(Bumseok Jeong) 교수는 KAIST 의과학대학원 교수이며, KAIST Clinic의 정신건강의학과에서도 일한다고 소개한다.[^home] 데이터사이언스대학원 교수 목록의 국문 이름은 「정범석」이고 연구 분야는 바이오·헬스케어·뇌과학이다.[^gsds]

논문에서 드러나는 전문 분야는 행동 선택과 통제력의 계산 모형, 심박과 뇌 활동 사이의 관계, 정서·생리 변화에 따른 개인차 분석이다. 통제력 추론 모형 연구에서는 마지막 저자이자 교신저자이고,[^affiliation][^p1] 행동 선택 모형과 심박 자각 연구에도 마지막 저자로 참여했다.[^p2][^p3][^p4] 심박 기반 분류 방법과 밀리미터파 신경 자극 연구에는 중간 저자로 참여했다.[^p5][^p8]

## 응용 분야

행동 모형은 개인별 선택 방식과 정신 건강 관련 개인차를 이해하는 데 연결되며,[^p2][^p3] 심박 관련 뇌 활동 분석은 몸 안 감각에 대한 주의 상태를 분류하는 데 연결된다.[^p5] 신경 자극 공동연구는 목표 신경을 국소적으로 자극하는 비침습 기법을 지향한다.[^p8]

## 구성원

2026년 11월 12일 연구실 Members 구획의 7명이다. 주제·업무는 카드 표기 그대로이며, 「대표 논문 참여」는 위 표의 번호다. 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^home]

| 이름 | 랩 게시 주제·업무 | 대표 논문 참여 |
|---|---|---|
| Dayoung Yoon (윤다영) | Compuational modeling; fMRI/fMRS | 2, 3, 4, 6 |
| Su Hyun Bong (봉수현) | Compuational modeling; fMRI, EEG/MEG | 2, 4, 6 |
| Jaewon Kim (김재원) | Compuational modeling; fMRI | 2, 4, 6 |
| Hyun Soo Park (박현수) | Compuational modeling; fMRI | 7 |
| Hyunjoon Ahn (안현준) | Compuational modeling; fMRI |  |
| Yourim Shin (신유림) | Compuational modeling; fMRI | 4 |
| Hyunjung Kim (김현정) | Enrollment and Evaluation; Caring |  |

## 졸업생과 이전 구성원

연구실 Alumni 구획의 15명이다. 카드에 진로가 적힌 6명과 연구 주제가 적힌 9명을 구분하며, 아래 연구 주제는 진로를 뜻하지 않는다.[^home]

| 이름 | 랩이 적은 진로 | 랩이 적은 연구 주제 |
|---|---|---|
| Sangwon Lee (이상원) | Kyungbuk Univ; Professor, Psychiatry |  |
| Jaehyun Yoo (유재현) | Catholic Univ; Professor, Psychiatry |  |
| Ko Woon Kim (김고운) | Chonbuk Univ; Professor, Neurology |  |
| Soohyun Cho (조수현) | Kangbuk SMC; Clinical psychologist, candidate |  |
| Dohyun Kim (김도현) | Danguk Univ. Hospital; Professor, Psychiatry |  |
| Dongwoo Shin (신동우) | Mokdong Hospital, Ewha University Medical Center; Professor, Neurology |  |
| Kyumin Park (박규민) |  | Emotional trauma; Emotion |
| Jaejoong Kim (김재중) |  | Computational Neuroscience; Interoception, Allostasis |
| Minseob Kim (김민섭) |  | Compuational modeling; Game theory,Machine learning |
| Minchul Kim (김민철) |  | Compuational modeling; DTI, EEG, Anxiety |
| Seokho Yoon (윤석호) |  | Compuational modeling; Noise, Entropy, Depression |
| Kyusung Choi (최규성) |  | Deep neural network; Neuroimaging |
| Junho Kim (김준호) |  | NeuroEconomics; Economics |
| Sunghwan Kim (김성환) |  | NeuroEconomics; Economics |
| Haeorm Park (박해오름) |  | NeuroEconomics; Economics |

## 최근 논문 목록 (2021–2026)

정범석 교수가 저자로 참여한 9편이다. 사전 공개본은 발표처 뒤에 표시한다.[^works]

**2026**

- Hyun Soo Park; Hoyeon Kim; Yerim Kwak; Bumseok Jeong. "Hormonal Modulation of Brain Control Energy Across the Menstrual Cycle: A Network Control Theory Study". *Research Square (사전 공개본)*. DOI: <https://doi.org/10.21203/rs.3.rs-11007587/v1>.
- Dayoung Yoon; Bumseok Jeong. "Policy precision reveals action-phase impulsivity in women with premenstrual syndrome during risk-taking". *bioRxiv (Cold Spring Harbor Laboratory) (사전 공개본)*. DOI: <https://doi.org/10.64898/2026.03.12.711243>.

**2025**

- Su Hyun Bong; Yourim Shin; Dayoung Yoon; Jaewon Kim; Hyunsoo Park; Bumseok Jeong. "Conscious cardiac awareness and interoceptive attention differentially modulate heartbeat-evoked neural dynamics". *NeuroImage*. DOI: <https://doi.org/10.1016/j.neuroimage.2025.121606>.
- Dayoung Yoon; Jaejoong Kim; Do Hyun Kim; Dong Woo Shin; Su Hyun Bong; Jaewon Kim; Hae‐Jeong Park; Hong Jin Jeon; Bumseok Jeong. "Individual differences in policy precision: Links to suicidal risk and network dynamics". *NeuroImage*. DOI: <https://doi.org/10.1016/j.neuroimage.2025.121479>.

**2024**

- Wooyong Lee; Euisun Kim; Jiyoung Park; Jinseok Eo; Bumseok Jeong; Hae‐Jeong Park. "Heartbeat-related spectral perturbation of electroencephalogram reflects dynamic interoceptive attention states in the trial-by-trial classification analysis". *NeuroImage*. DOI: <https://doi.org/10.1016/j.neuroimage.2024.120797>.
- Su Hyun Bong; Dayoung Yoon; Jaewon Kim; Bumseok Jeong. "Perceptual Attention and Subjective Belief about Risk Alters Heartbeat-evoked Response". *Research Square (사전 공개본)*. DOI: <https://doi.org/10.21203/rs.3.rs-4488979/v1>.
- Jaewon Kim; Su Hyun Bong; Dayoung Yoon; Bumseok Jeong. "Prosocial emotions predict individual differences in economic decision-making during ultimatum game with dynamic reciprocal contexts". *Scientific Reports*. DOI: <https://doi.org/10.1038/s41598-024-62203-y>.

**2021**

- Jaejoong Kim; Sang Wan Lee; Seokho Yoon; Haeorm Park; Bumseok Jeong. "Neurocomputational mechanism of controllability inference under a multi-agent setting". *PLoS Computational Biology*. DOI: <https://doi.org/10.1371/journal.pcbi.1009549>.
- Hi Yuen Song; Dong Woo Shin; Seung Mun Jung; Yong Jeong; Bumseok Jeong; Chul Soon Park. "Feasibility study on transcutaneous auricular vagus nerve stimulation using millimeter waves". *Biomedical Physics & Engineering Express*. DOI: <https://doi.org/10.1088/2057-1976/ac2c54>.

## 연락과 위치

- 연구실 주소: Laboratory for Computational affective Neuroscience and Development, Graduate School of Medical Science and Engineering, KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea[^home]
- 연구실 전화: (+82) 350 7160[^home]
- 교수 이메일: bs.jeong@kaist.ac.kr[^gsds]
- 교수 전화: 042-350-4245[^gsds]
[^research]: CNDL, Welcome의 연구 목표: 행동·뇌 영상 자료(예: fMRI/MRS, DTI, EEG/MEG)로 지각·감정의 개인차와 정서 경험의 기여를 설명하는 계산 모형 개발. <https://drshrink.github.io/> 관측 2026-11-12.
[^home]: CNDL, 연구실 소개·Research Interests·Professor·Members·연락처. <https://drshrink.github.io/> 관측 2026-11-12.
[^gsds]: KAIST 데이터사이언스대학원, 교수 목록의 정범석 항목. <https://gsds.kaist.ac.kr/people> 관측 2026-11-12.
[^works]: OpenAlex, Bumseok Jeong 저자 기록의 2021–2026년 논문 서지·초록. <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5001355433,publication_year:2021-2026> 관측 2026-11-12.
[^affiliation]: Jaejoong Kim 외, PLoS Computational Biology 17(11), e1009549 (2021-11-09), 저자·소속·교신 표시. <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009549> 관측 2026-11-12.
[^p1]: J. Kim 외, B. Jeong, PLoS Computational Biology 17, e1009549 (온라인 2021-11-09). <https://doi.org/10.1371/journal.pcbi.1009549> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5001355433,publication_year:2021-2026> 관측 2026-11-12.
[^p2]: D. Yoon 외, B. Jeong, NeuroImage (2025). <https://doi.org/10.1016/j.neuroimage.2025.121479> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5001355433,publication_year:2021-2026> 관측 2026-11-12.
[^p3]: D. Yoon, B. Jeong, bioRxiv (Cold Spring Harbor Laboratory) (2026). <https://doi.org/10.64898/2026.03.12.711243> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5001355433,publication_year:2021-2026> 관측 2026-11-12.
[^p4]: S. H. Bong 외, B. Jeong, NeuroImage (2025). <https://doi.org/10.1016/j.neuroimage.2025.121606> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5001355433,publication_year:2021-2026> 관측 2026-11-12.
[^p5]: W. Lee 외, H.-J. Park, NeuroImage (2024). <https://doi.org/10.1016/j.neuroimage.2024.120797> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5001355433,publication_year:2021-2026> 관측 2026-11-12.
[^p6]: J. Kim, S. H. Bong, D. Yoon, B. Jeong, Scientific Reports (2024). <https://doi.org/10.1038/s41598-024-62203-y> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5001355433,publication_year:2021-2026> 관측 2026-11-12.
[^p7]: H. S. Park, H. Kim, Y. Kwak, B. Jeong, Research Square (2026). <https://doi.org/10.21203/rs.3.rs-11007587/v1> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5001355433,publication_year:2021-2026> 관측 2026-11-12.
[^p8]: H. Y. Song 외, C. S. Park, Biomedical Physics & Engineering Express (2021). <https://doi.org/10.1088/2057-1976/ac2c54> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5001355433,publication_year:2021-2026> 관측 2026-11-12.

# 인터랙티브 컴퓨팅 연구실 (Interactive Computing Laboratory, ICLab)

**KAIST AI컴퓨팅학과·전산학부 · 이의진 교수, 석좌교수**

- 홈페이지: <https://ic.kaist.ac.kr/>
- 대분야: 컴퓨팅·AI
- 태그: 인간–컴퓨터 상호작용[^dept][^p7], 모바일·유비쿼터스 센싱[^home][^p1][^p2], 대형 언어 모델[^p1]
- [자료와 표기 근거](ic-sources.md)

> 스마트폰·착용 기기와 생활 공간에서 얻은 자료로 사람의 행동과 상태를 이해하고, 건강·안녕·일을 돕는 상호작용 시스템을 만드는 연구실이다.[^home][^dept]

## 무엇을 연구하나

인터랙티브 컴퓨팅 연구실은 인간–컴퓨터 상호작용(Human-Computer Interaction, HCI; 사람이 컴퓨터·기기를 사용하는 방식과 경험을 설계하고 평가하는 분야)을 연구한다. 스마트폰, 몸에 착용하는 기기, 생활 공간의 센서를 이용해 사람이 무엇을 하고 어떤 상황에 있는지 파악하고, 그 이해를 바탕으로 사용자에게 필요한 정보와 서비스를 제공한다. 연구실은 이 흐름을 관측 자료의 수집, 상태의 분석, 개인화된 지원(사용자의 특성과 반응에 맞춘 지원)으로 설명한다.[^home][^dept]

관측값을 모으는 것과 사람이 자신의 상태를 이해하는 것을 함께 다룬다. 모바일·유비쿼터스 센싱(mobile and ubiquitous sensing; 휴대·착용 기기나 일상 환경의 감지 기기로 사람·사물·상황을 알아내는 방법)을 바탕으로 일상 행동과 스트레스를 분석하고, 데이터 시각화(자료의 의미와 관계를 그림으로 표현하는 방법)를 통해 그 자료를 사용자가 살펴보도록 한다. 가족이 함께 감정·행동 자료를 해석하거나 사용자가 스트레스에 관련된 상황을 바꿀 대안을 찾는 시스템이 그 예다.[^dept][^p1][^p3][^p6]

분석 방법과 실제 서비스를 연결하는 소프트웨어도 만든다. 앱 안에서 반복되는 행동을 찾는 연구에서는 대형 언어 모델(Large Language Model, LLM; 많은 언어 자료를 학습해 글을 처리하고 생성하는 인공지능 모델)을 행동 설명에 활용한다. 착용 기기의 자료를 실시간으로 처리하는 AffectStream에서는 자료를 보내는 부분과 받는 부분을 분리한 구조를 사용해 감정 상태 분석을 응용 서비스와 잇는다.[^p1][^p2]

사용자가 시스템에 의사를 표현하고 해석에 참여하는 과정도 연구 대상이다. 사용자가 자신의 자료를 탐색하고 시간·장소에 따라 수집을 끌 수 있는 앱, 임상의가 면담 정보를 검토하는 화면, 제조 기계의 기록에서 작업자의 행동과 성과를 분석하는 방법을 다룬다. 생활 속 건강 지원에서 출발해 가족과 일터의 상호작용까지 연구 범위가 이어진다.[^p5][^p7][^p8]

## 주요 연구 주제

### 1. 일상 행동 감지와 분석 기반

스마트폰의 앱 사용을 단순한 사용 시간에 머물지 않고 앱 안에서 되풀이되는 행동으로 분석한다. SHIRBT-MMF(Smartphone Human Interaction-based Routine Behavior Task Mining, Modeling, and Feature Extraction)는 반복 행동의 순서를 찾고 언어 모델로 그 행동을 설명해 스트레스 분석에 쓰는 특징(분석 대상의 속성을 나타내는 값)을 추출한다. 이 연구는 행동 특징을 해석할 수 있고 시간이 지나도 분석에 활용할 수 있도록 하는 데 초점을 둔다.[^p1]

AffectStream은 착용 센서 자료를 연속해서 받아 감정 상태를 분석하는 공개 소프트웨어다. 여러 응용에서 자료를 받을 수 있도록 처리 구조를 구성하고, 자료량에 따라 처리 규모를 늘리는 확장성(처리 수요에 맞추어 시스템의 처리 능력을 조절하는 성질)과 일부 구성 요소에 문제가 생겨도 동작을 이어 가는 내결함성(구성 요소의 고장에도 서비스를 지속하도록 하는 성질)을 다룬다.[^p2]

### 2. 사용자 상황에 맞춘 행동 지원

CounterStress는 반사실적 설명(counterfactual explanation; 다른 결과를 얻으려면 어떤 입력 조건이 달라져야 하는지를 제시하는 설명)을 사용해 스트레스가 높은 상황에서 바꿀 수 있는 조건의 대안을 제안한다. 사용자가 대처 계획을 세우는 과정에 이 설명을 어떻게 활용하는지 살피는 연구다.[^p3]

FinerMe는 소셜미디어 사용을 앱 전체와 앱 안의 기능으로 나누어 살펴보고 조절하는 도구다. 자기 사용 기록을 돌아보는 기능과 사용을 제한하는 기능을 결합해, 어느 수준에서 조절하는지가 사용 행태와 성찰에 어떤 차이를 만드는지 연구한다. 정신 건강을 위한 도구 설계에서도 효과와 사용자 경험을 구분한다. 예를 들어 혐오 표현을 바꾸어 보여 주는 HateBuffer는 표현을 완화하는 시스템을 제안했지만, 실험에서 대조군보다 감정이 나아지거나 피로가 줄어드는 효과는 확인하지 못했다고 보고했다.[^p4][^hatebuffer]

### 3. 사람을 위한 정보 표현과 대화

가족 자료를 다룬 SELaD는 음성·영상 자료와 생리 센서(몸의 기능과 반응을 관측하는 센서)의 정보를 시각화해 가족이 대화와 감정의 흐름을 함께 돌아보도록 하는 시스템이다. 서로 다른 자료를 비교하고 해석하는 과정에서 가족이 관계를 성찰하는 방식을 연구한다.[^p6]

정신과 초진을 지원하는 AI Interviewer 연구는 제한된 시간 안에서 필요한 정보를 모으도록 질문의 흐름을 조절하고, 임상의가 내용을 살펴볼 검토 화면을 함께 설계한다. 초점은 대화의 유연성과 임상 업무에 맞는 정보 표현을 갖춘 시스템 설계에 있다.[^p5]

### 4. 데이터 수집과 사람·기계 협업

PriviAware는 사용자가 자신의 관측 자료를 살펴보고 시간·장소 조건으로 수집을 중단할 수 있게 하는 앱이다. 연구실은 자료 수집에 대한 동의를 한 번 받는 절차에서 나아가 사용자가 일상 상황에 맞추어 수집을 관리하는 인터페이스(사람과 기기가 정보를 주고받는 접점)를 설계·평가한다.[^p7]

제조 현장의 연구에서는 기계가 남긴 기록을 작업 상황과 연결하고 작업자의 행동과 성과를 분석하는 방법을 제안한다. 기계가 자동으로 동작하다가 사람이 개입해야 하는 반자동 생산 환경에서, 사람·기계의 상호작용과 작업 환경이 성과 차이를 어떻게 설명하는지 다룬다.[^p8]

## 대표 논문

KAIST 재직 시기의 2021–2026년 논문 중 연구 갈래를 고르게 보여 주고 초록을 읽을 수 있는 8편을 골랐다. 이의진 교수는 6편에서 마지막 교신저자, 1편에서 마지막 공동 책임저자, 1편에서 중간 저자다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다.[^prof]

| 번호 | 연도 | 논문 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2025 | [Leveraging Smartphone Human Interaction Routine Behavior Task Mining and Modeling for Daily Stress Monitoring](https://doi.org/10.1145/3770644) · IMWUT | 앱 안에서 되풀이되는 행동을 찾아 언어 모델로 설명하고, 이를 스트레스 추정에 쓰는 방법을 제안했다. 행동 특징의 해석 가능성과 시간에 따른 안정성을 함께 살폈다.[^p1] |
| 2 | 2025 | [AffectStream: Kafka-based real-time affect monitoring system using wearable sensors](https://doi.org/10.1016/j.softx.2025.102325) · SoftwareX | 착용 센서의 자료를 받아 응용 서비스에 전달하며 감정 상태를 실시간 분석하는 공개 시스템을 만들었다. 공개 자료집을 이용해 처리 성능을 평가했다.[^p2] |
| 3 | 2025 | [CounterStress: Enhancing Stress Coping Planning through Counterfactual Explanations in Personal Informatics](https://doi.org/10.1145/3706598.3713730) · CHI | 스트레스가 높은 상황에서 바꿀 수 있는 조건의 대안을 제시하는 시스템이다. 사용자가 실행할 대처 전략을 고르고 활용하는 과정을 살폈다.[^p3] |
| 4 | 2023 | [FinerMe: Examining App-level and Feature-level Interventions to Regulate Mobile Social Media Use](https://doi.org/10.1145/3610065) · CSCW | 소셜미디어 사용을 앱 전체 또는 앱 안의 기능 단위로 조절하는 도구를 만들었다. 기능 단위 조절이 기록을 돌아보는 방식과 실제 사용에 주는 차이를 비교했다.[^p4] |
| 5 | 2026 | [Toward Flexible Psychiatric History-Taking and Visualization: Exploring Clinician Perspectives with Large Language Models](https://doi.org/10.1145/3772318.3790970) · CHI | 필요한 정보와 시간 제약에 맞추어 질문 흐름을 조절하는 면담 시스템과 임상의 검토 화면을 제안했다. 대화의 유연성을 유지하며 핵심 정보를 모으는 설계 방향을 다뤘다.[^p5] |
| 6 | 2026 | [Why stressed, Mom?: Exploring Family Reflection on Social and Emotional Sensor Data through Family Informatics](https://doi.org/10.1145/3772318.3790745) · CHI | 가족의 일상 상호작용에서 얻은 여러 종류의 자료를 시각화하는 SELaD를 만들었다. 가족이 자료를 함께 해석하며 대화와 감정의 관계를 돌아보는 과정을 살폈다.[^p6] |
| 7 | 2024 | [PriviAware: Exploring Data Visualization and Dynamic Privacy Control Support for Data Collection in Mobile Sensing Research](https://doi.org/10.1145/3613904.3642815) · CHI | 사용자가 수집 자료를 탐색하고 시간·장소에 따라 수집을 끄는 앱을 제안했다. 세밀한 제어 기능을 사용자가 어떻게 활용하는지 살폈다.[^p7] |
| 8 | 2023 | [Charlie and the Semi-Automated Factory: Data-Driven Operator Behavior and Performance Modeling for Human-Machine Collaborative Systems](https://doi.org/10.1145/3544548.3581457) · CHI | 제조 기계가 남긴 기록을 상황에 맞게 정리하고 작업자 행동과 생산 성과를 연결하는 분석 방법을 제안했다. 상호작용과 작업 환경의 요인으로 성과 차이를 설명했다.[^p8] |

## 교수와 전문 분야

이의진 교수는 UCLA에서 전산학 박사학위를 받은 뒤 Bell Labs 선임연구원을 거쳐 2010년에 KAIST에 부임했다. AI컴퓨팅학과 교수진은 이의진 교수를 학과장·전임교수로 소개한다. 전산학부 교수 소개는 인간–컴퓨터 상호작용, 유비쿼터스 컴퓨팅(일상 환경 곳곳에서 컴퓨터가 서비스를 제공하는 방식), 센서 데이터 사이언스(관측 자료에서 패턴과 관계를 찾는 계산·분석 연구), 데이터 가시화를 주요 연구 분야로 적고, 산업및시스템공학과·지식서비스공학대학원·KI 건강과학연구소 참여를 함께 소개한다.[^prof][^ai-faculty]

최근 연구에서는 일상 행동을 분석하는 방법, 사용자에게 행동 변경 대안을 제시하는 도구, 자료를 함께 해석하는 화면, 임상 면담을 지원하는 대화 시스템을 다룬다. 사람의 상황을 감지하는 계산 방법과 사람이 그 결과를 이해하고 활용하는 상호작용 설계를 연결하는 것이 전문 분야의 공통 축이다.[^p1][^p3][^p5][^p6]

## 응용 분야

- 일상 건강·안녕 지원: 스마트폰 행동 분석, 스트레스 대처 계획, 소셜미디어 사용 조절.[^p1][^p3][^p4]
- 가족의 정보 활용: 가족이 대화·감정·행동 자료를 함께 해석하는 시각화 시스템.[^p6]
- 임상 업무 지원: 초진 정보 수집을 돕는 대화 시스템과 임상의 검토 화면.[^p5]
- 개인정보 관리와 제조 현장 분석: 상황에 맞춘 관측 자료 수집 제어, 작업자와 기계의 상호작용·성과 분석.[^p7][^p8]

## 구성원

구성원 페이지에 게시된 박사후연구원 2명, 박사과정 6명, 석사과정 10명이다. 과정과 연구 주제는 게시 표기다. 대표 논문 참여는 논문 전체 저자 목록에서 같은 이름을 확인한 경우에 표시했다.[^members]

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Seungwan Jin | 박사후연구원 | Longitudinal Personalization, Agent Memory |  |
| Yugyeong Jung | 박사후연구원 | Data visualization, Human-data interaction, Social robotics | 5, 7, 8 |
| Panyu Zhang | 박사과정 | Routine Computing, Affective Computing |  |
| Sueun Jang | 박사과정 | Human-Computer Interaction, Linguistic Interaction, Feedback, Meta-cognition | 6 |
| Hwindol Park | 박사과정 | Human-Computer Interaction, Healthcare, Time-series analysis |  |
| Chanhee Lee | 박사과정 | Human-Computer Interaction, Conversational Agents, Human-AI Interaction |  |
| Jinyoung Yoo | 박사과정 | Human-Computer Interaction, Mental Health |  |
| Somin Park | 박사과정 | Human-Computer Interaction, Healthcare, Mobile Sensing |  |
| Minseo Park | 석사과정 | Human-Computer Interaction, Domain Adaptation |  |
| Junmo Lee | 석사과정 | Human-Computer Interaction, Motivation |  |
| Rd Pradipta Gitaya Samiadji | 석사과정 | Device Sensing, Applied AI, Wellbeing Intervention |  |
| Bonwoo Koo | 석사과정 | Sensor Data Science, Foundation Model |  |
| Esther Kang | 석사과정 | Human-AI Interaction, Conversational Agents |  |
| Gyeongmin Na | 석사과정 | Human-Computer Interaction, Natural Language Processing & Linguistics, Sentiment Analysis |  |
| Jiwoo Kang | 석사과정 | Human-Computer Interaction, Digital Healthcare |  |
| In Woo | 석사과정 | Human-AI Interaction, Human-Computer Interaction |  |
| Renz Samuel Gutierrez | 석사과정 | Human-AI Interaction, Interactive Systems, User Modeling |  |
| Faraz Farangizadeh | 석사과정 | Human-AI Interaction, Ubiquitous Computing, Mobile & Wearable Sensing |  |

## 졸업생과 이전 구성원

구성원 페이지 Alumni 구역에 게시된 54명이다. 진로는 연구실 게시 표기다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jeongyun Heo |  | Professor at Kookmin Univ. |
| Eunhee Yi |  | LG Electronics |
| Minsam Ko |  | Assistant Professor at Hanyang Univ. ERICA |
| Youngchang Ko |  | Defense Rapid Acquisition Technology Research Institute |
| Jeungmin Oh |  | Hayan Mind |
| Joonwon Lee |  | DelightRoom |
| Sungjun Kang |  | KakaoPay |
| Daehee Shin |  | KakaoPay |
| Soobin Yang |  |  |
| Auk Kim |  | Assistant Professor at Kangwon National Univ. |
| Sangkeun Park |  | Assistant Professor at Kyung Hee Univ. |
| Jaejeung Kim |  | Assistant Professor at Chungnam National Univ. |
| Aejin Song |  |  |
| Joohyun Kim |  | IQVIA |
| Sergey Leksikov |  | Lablup Inc. |
| Hayeon Jeong |  | Hankook&Company |
| Sujin Kwon |  | Agency for Defense Development |
| Sungwook Moon |  | Swing Mobility Co. |
| Riheon Kim |  | Naver |
| Hayoung Jung |  | CJ Olivenetworks |
| Christine Balili |  |  |
| Jongwon Kim |  | KB Kookmin Bank |
| Duyeon Kim |  |  |
| Jemin Lee |  | Assistant Professor at Jeonbuk National Univ. |
| Soowon Kang |  | Samsung Electronics |
| Narae Cha |  | LibL |
| Hansoo Lee |  | Research Fellow at Imperial College London |
| Cheulyoung Park |  | Upstage |
| Eunji Park |  | Assistant Professor at Chung-Ang Univ. |
| Minhyoung Kim |  | Doeat |
| Juho Sun |  | Bucketplace |
| Gyuwon Jung |  | Post Doctoral Researcher at Aalto Univ. |
| Yongshin Kim |  | KPMG |
| Youwon Shin |  | Samsung Electronics |
| Eugene Lee |  |  |
| Youngji Koh |  |  |
| Woohyeok Choi |  | Assistant Professor at Kangwon National Univ. |
| Inyeop Kim |  | Samsung SDS |
| Jieun Lim |  | DB HiTek |
| Hei Yiu Law |  |  |
| Duri Lee |  |  |
| Yunjo Han |  | Samsung Research |
| Eunki Joung |  |  |
| Heejeong Lim |  |  |
| Hyesoo Park |  | Ph.D. Student at Georgia Institute of Technology |
| Joonyoung Park |  | BIONEVER |
| Hyunsoo Lee |  |  |
| Jeonghyun Kim |  | Hanwha Aerospace |
| Thu Vo |  |  |
| Gyuna Kim |  |  |
| Sangjun Park |  |  |
| Youngseok Seo |  |  |
| Jihoon Woo |  |  |
| Wonmo Koo |  | Assistant Professor at Pusan National University |

## 최근 논문 목록 (2021–2026)

스마트폰·착용 기기의 자료 처리, 생활 속 상호작용, 사용자 지원 시스템, 개인정보 관리 등을 다룬다. 연구실 Publications의 2021–2026년 구역에서 고른 71편이며, 연도는 연구실의 연도 구역을 따른다. 제목·저자·발표처는 연구실 게시 표기다. 논문 PDF에 게재 승인으로 적힌 학술지 항목은 이를 표시하고, 연도는 연구실의 2026년 구역을 따른다.[^pubs][^fusion]

**2026**

- Bonwoo Koo, Junmo Lee, and Uichin Lee. "CallSense: Sensing Call Engagement in Privacy-Constrained Call Center Environment with Commodity Smartwatches". *Companion of the 2026 ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp Companion '26)*.
- Junmo Lee, Rd Pradipta Gitaya Samiadji, and Uichin Lee. "An Open-Source Mobile and Wearable Sensing Platform for Bridging Passive Sensing and Active Sensing". *Companion of the 2026 ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp Companion '26)*.
- JinYoung Yoo, Somin Park, Sueun Jang, Seungwan Jin, and Uichin Lee. "Sonju: A Context-Aware Teachable Agent for Eliciting Older Adults' Situated Knowledge". *Companion of the 2026 ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp Companion '26)*.
- Esther Kang, Youngji Koh, Seungwan Jin, and Uichin Lee. "Designing Clinician Centered Explanations for Sensing-based Longitudinal Mental Health Monitoring". *XAI for U Workshop at UbiComp / ISWC 2026*.
- Seyoung Jin, Heewon Beak, Uichin Lee, and Hyoungshick Kim. "It Seems Like an Advertisement”: Attention, Interpretation, and Response to Mobile Antivirus Warnings". *Proceedings of the 29th International Symposium on Research in Attacks, Intrusions and Defenses (RAID 2026)*.
- Youngji Koh, Gyuna Kim, Chanhee Lee, Panyu Zhang, Yunhee Ku, Inhwan Choi, Jewoo Ryu, and Uichin Lee. "A Multimodal Sensor Fusion Approach for Mental Health Detection Using Mobile, Wearable, and IoT Sensors". *IEEE Journal of Biomedical and Health Informatics (게재 승인)*.
- Hyunsoo Lee, Reza Ghaiumy Anaraky, Oded Nov, and Uichin Lee. "OurData: Understanding Family Privacy in Sensor-Rich Homes". *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, Volume 10, Issue 2*.
- Hyunsoo Lee, Seyoung Jin, Hyoungshick Kim, and Uichin Lee. "Mind the SIM: Awareness and Mental Models in a South Korean Case Study". *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '26)*.
- Duri Lee, Heejeong Lim, Vedant Das Swain, and Uichin Lee. "Understanding Behind the Smile of Emotion Workers: Detecting After-Call Stress in Call Agents". *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '26)*.
- Yugyeong Jung, Thu Hoang Anh Vo, Hyun Seung Moon, Jae Young Choi, Hyangkyeong Oh, Ujin Lee, Eunjoo Kim, Tak Yeon Lee, and Uichin Lee. "Toward Flexible Psychiatric History-Taking and Visualization: Exploring Clinician Perspectives with Large Language Models". *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '26)*.
- Hyesoo Park, Sueun Jang, Hyunsoo Lee, Jennifer G Kim, and Uichin Lee. "Why stressed, Mom?: Exploring Family Reflection on Social and Emotional Sensor Data through Family Informatics". *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '26)*.

**2025**

- Hansoo Lee, Taehyeon Park, Youngji Koh, Jaegil Lee, and Uichin Lee. "Leveraging Smartphone Human Interaction Routine Behavior Task Mining and Modeling for Daily Stress Monitoring". *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, Volume 9, Issue 4*.
- Youngji Koh, Chanhee Lee, Eunki Joung, Hyunsoo Lee, and Uichin Lee. "Harnessing Home IoT for Self-tracking Emotional Wellbeing: Behavioral Patterns, Self-Reflection, and Privacy Concerns". *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, Volume 9, Issue 3*.
- Subin Park, Jeonghyun Kim, Jeanne Choi, Joseph Seering, Uichin Lee, and Sung-Ju Lee. "HateBuffer: Safeguarding Content Moderators' Mental Well-Being through Hate Speech Content Modification". *Proceedings of the ACM on Human-Computer Interaction, Volume 9, Issue 7*.
- Jeonghyun Kim, Duri Lee, and Uichin Lee. "AffectStream: Kafka-based real-time affect monitoring system using wearable sensors". *SoftwareX, Volume 31*.
- Eun-Yeol Ma, Uichin Lee, and Heeyoung Kim. "Simultaneous Treatment Effect Estimation and Variable Selection for Observational Data". *IISE Transactions, Volume 57, Issue 4*.
- Chanhee Lee, Eunki Joung, Youngji Koh, Esther Kim, Sohwi Son, Sunjung Kwon, and Uichin Lee. "'In That Small Space with Just the Two of Us': User Experiences with Cumpa in a Robotic Counseling Center". *Proceedings of the ACM on Human-Computer Interaction, Volume 9, Issue 7*.
- Gyuwon Jung, Heejeong Lim, Kyungsik Han, Hyungsook Kim, and Uichin Lee. "Designing a Visual Analytics Tool to Support Data Analysis Tasks of Digital Mental Health Interventions: Case Study". *JMIR Human Factors, Volume 12*.
- Sangjun Park, Dejiang Zheng, and Uichin Lee. "A PPG Signal Dataset Collected in Semi-Naturalistic Settings Using Galaxy Watch". *Scientific Data, Volume 12*.
- Gyuwon Jung and Uichin Lee. "CounterStress: Enhancing Stress Coping Planning through Counterfactual Explanations in Personal Informatics". *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '25)*.
- Sueun Jang, Youngseok Seo, Woohyeok Choi, and Uichin Lee. "Like Adding a Small Weight to a Scale About to Tip: Personalizing Micro-Financial Incentives for Digital Wellbeing". *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '25)*.
- Yugyeong Jung, Hei Yiu Law, Hadong Lee, Junmo Lee, Bongshin Lee, and Uichin Lee. "DataSentry: Building Missing Data Management System for In-the-Wild Mobile Sensor Data Collection through Multi-Year Iterative Design Approach". *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '25)*.
- Seyoung Jin, Heewon Baek, Uichin Lee, and Hyoungshick Kim. "I Was Told to Install the Antivirus App, but I'm Not Sure I Need It: Understanding Smartphone Antivirus Software Adoption and User Perceptions". *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '25)*.
- Panyu Zhang, Gyuwon Jung, Uzair Ahmed, and Uichin Lee. "CausalCFF: Causal Analysis between User Stress Level and Contextually Filtered Features Extracted from Mobile Sensor Data". *Extended Abstracts of the CHI Conference on Human Factors in Computing Systems (CHI LBW '25)*.

**2024**

- Yugyeong Jung and Uichin Lee. "Visual Analytics System for Monitoring Mobile and Wearable Sensing Data Collection Campaign". *Proceedings of the IEEE VIS Conference on Visualization (VIS) (VIS Poster '24)*.
- Panyu Zhang, Gyuwon Jung, Jumabek Alikhanov, Uzair Ahmed, and Uichin Lee. "A Reproducible Stress Prediction Pipeline with Mobile Sensor Data". *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, Volume 8, Issue 3*.
- Eunji Park, Duri Lee, Yunjo Han, James Diefendorff, and Uichin Lee. "Hide-and-seek: Detecting Workers' Emotional Workload in Emotional Labor Contexts Using Multimodal Sensing". *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, Volume 8, Issue 3*.
- Inyeop Kim and Uichin Lee. "Navigating User-System Gaps: Understanding User-Interactions in User-Centric Context-Aware Systems for Digital Well-being Intervention". *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24)*.
- Hansoo Lee, Auk Kim, SangWon Bae, and Uichin Lee. "S-ADL: Exploring Smartphone-based Activities of Daily Living to Detect Blood Alcohol Concentration in a Controlled Environment". *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24)*.
- Hyunsoo Lee, Yugyeong Jung, Hei Yiu Law, Seolyeong Bae, and Uichin Lee. "PriviAware: Exploring Data Visualization and Dynamic Privacy Control Support for Data Collection in Mobile Sensing Research". *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24)*.
- Gyuwon Jung, Sangjun Park, and Uichin Lee. "DeepStress: Supporting Stressful Context Sensemaking in Personal Informatics Systems Using a Quasi-experimental Approach". *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24)*.
- Minyeong Kim, Jiwook Lee, Youngji Koh, Chanhee Lee, Uichin Lee, and Auk Kim. "Interrupting for Microlearning: Understanding Perceptions and Interruptibility of Proactive Conversational Microlearning Services". *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24)*.
- Jieun Lim, Youngji Koh, Auk Kim, and Uichin Lee. "Exploring Context-Aware Mental Health Self-Tracking Using Multimodal Smart Speakers in Home Environments". *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24)*.
- Hyunsoo Lee, Yugyeong Jung, Youwon Shin, Hyesoo Park, Woohyeok Choi, and Uichin Lee. "FamilyScope: Visualizing Affective Aspects of Family Social Interactions using Passive Sensor Data". *Proceedings of the ACM on Human-Computer Interaction, Volume 8, Issue CSCW1*.
- Gyuwon Jung, Sangjun Park, Eun-Yeol Ma, Heeyoung Kim, and Uichin Lee. "Tutorial on Matching-based Causal Analysis of Human Behaviors Using Smartphone Sensor Data". *ACM Computing Surveys, Volume 56, Issue 9*.
- Kobiljon Toshnazarov, Uichin Lee, Byung Hyung Kim, Varun Mishra, Lismer Andres Caceres Najarro, and Youngtae Noh. "SOSW: Stress Sensing With Off-the-Shelf Smartwatches in the Wild". *IEEE Internet of Things Journal, Volume 11, Issue 12*.

**2023**

- Youngji Koh, Chanhee Lee, Yunhee Ku, and Uichin Lee. "Data Visualization for Mental Health Monitoring in Smart Home Environment: A Case Study". *2023 Workshop on Visual Analytics in Healthcare (VAHC)*.
- Yunjo Han, Kobiljon E. Toshnazarov, Byung Hyung Kim, Youngtae Noh, and Uichin Lee. "WatchPPG: An Open-Source Toolkit for PPG-based Stress Detection using Off-the-shelf Smartwatches". *Adjunct Proceedings of the 2023 ACM International Joint Conference on Pervasive and Ubiquitous Computing & the 2023 ACM International Symposium on Wearable Computing (UbiComp/ISWC '23)*.
- Sangjun Park, Eunji Park, Paul. H. Lee, and Uichin Lee. "Measuring Device-Specific Physical Activity Trackability in Multi-Device Environments". *2023 IEEE International Conference on Big Data and Smart Computing (BigComp)*.
- Adiba Orzikulova, Hyunsung Cho, Hye-Young Chung, Hwajung Hong, Uichin Lee, and Sung-Ju Lee. "FinerMe: Examining App-level and Feature-level Interventions to Regulate Mobile Social Media Use". *Proceedings of the ACM on Human-Computer Interaction, Volume 7, Issue CSCW2*.
- Jeongyun Heo and Uichin Lee. "Form to Flow: Exploring Challenges and Roles of Conversational UX Designers in Real-world, Multi-channel Service Environments". *Proceedings of the ACM on Human-Computer Interaction, Volume 7, Issue CSCW2*.
- Gyuwon Jung, Sangjun Park, Uichin Lee, Eun-Yeol Ma, and Heeyoung Kim. "Causal Analytic Process for Mobile Health Data". *2023 IEEE International Conference on Big Data and Smart Computing (BigComp)*.
- Uichin Lee, Gyuwon Jung, Sangjun Park, Eun-Yeol Ma, Heeyoung Kim, Yonggeon Lee, and Youngtae Noh. "Data-driven Digital Therapeutics Analytics". *2023 IEEE International Conference on Big Data and Smart Computing (BigComp)*.
- Yonggeon Lee, Youngtae Noh, and Uichin Lee. "Data Processing Pipeline of Short-Term Depression Detection with Large-Scale Dataset". *2023 IEEE International Conference on Big Data and Smart Computing (BigComp)*.
- Eunji Park, Yugyeong Jung, Inyeop Kim, and Uichin Lee. "Charlie and the Semi-Automated Factory: Data-Driven Operator Behavior and Performance Modeling for Human-Machine Collaborative Systems". *Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23)*.
- Sangjun Park, Chanhee Lee, Jieun Han, and Uichin Lee. "QuickRef: Should I Read Cited Papers for Understanding This Paper?". *Extended Abstracts of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23)*.
- Yugyeong Jung, Gyuwon Jung, Sooyeon Jeong, Chaewon Kim, Woontack Woo, Hwajung Hong, and Uichin Lee. "Enjoy, but Moderately!”: Designing a Social Companion Robot for Social Engagement and Behavior Moderation in Solitary Drinking Context". *Proceedings of the ACM on Human-Computer Interaction, Volume 7, Issue CSCW2*.
- Woohyeok Choi and Uichin Lee. "Loss-Framed Adaptive Microcontingency Management for Preventing Prolonged Sedentariness: Development and Feasibility Study". *JMIR mHealth and uHealth, Volume 11*.
- M. Sami Zitouni, Cheul Young Park, Uichin Lee, Leontios J. Hadjileontiadis, and Ahsan Khandoker. "LSTM-Modeling of Emotion Recognition Using Peripheral Physiological Signals in Naturalistic Conversations". *IEEE Journal of Biomedical and Health Informatics, Volume 27, Issue 2*.

**2022**

- Yunjo Han, Hyemin Lee, Kobiljon E. Toshnazarov, Youngtae Noh, and Uichin Lee. "StressBal: Personalized Just-in-time Stress Intervention with Wearable and Phone Sensing". *Proceedings of the 2022 ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp/ISWC '22)*.
- Ryuhaerang Choi, Chanwoo Yun, Hyunsung Cho, Hwajung Hong, Uichin Lee, and Sung-Ju Lee. "You Are Not Alone: How Trending Stress Topics Brought #Awareness and #Resonance on Campus". *Proceedings of the ACM on Human-Computer Interaction, Volume 6, Issue CSCW2*.
- Hansoo Lee, Sangwook Lee, Youngji Koh, and Uichin Lee. "LV-Linker: Supporting Fine-grained User Interaction Analyses by Linking Smartphone Log and Recorded Video Data". *Adjunct Proceedings of the 35th Annual ACM Symposium on User Interface Software and Technology (UIST '22)*.
- Ryuhaerang Choi, Chanwoo Yun, Hyunsung Cho, Hwajung Hong, Uichin Lee, and Sung-Ju Lee. "Facilitating instant interactions for stressful experiences sharing and peer support". *Proceedings of the 20th Annual International Conference on Mobile Systems, Applications and Services (MobiSys '22)*.
- Muhammad Salman, Jin-Ho Son, Dong-Wan Choi, Uichin Lee, and Youngtae Noh. "DARCAS: Dynamic Association Regulator Considering Airtime Over SDN-Enabled Framework". *IEEE Internet of Things Journal, Volume 9, Issue 20*.
- Inyeop Kim, Minsam Ko, Joonyoung Park, Sung Wook Moon, Gyuwon Jung, Youn-kyung Lim, and Uichin Lee. "Social-Spiritual Face: Designing Social Reading Support for Spiritual Well-being". *Proceedings of the ACM on Human-Computer Interaction, Volume 6, Issue CSCW2*.
- Hansoo Lee, Joonyoung Park, and Uichin Lee. "A Systematic Survey on Android API Usage for Data-driven Analytics with Smartphones". *ACM Computing Surveys, Volume 55, Issue 5*.
- Muhammad Salman, Nguyen Dao, Uichin Lee, and Youngtae Noh. "CSI:DeSpy: Enabling Effortless Spy Camera Detection via Passive Sensing of User Activities and Bitrate Variations". *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, Volume 6, Issue 2*.
- Gyuwon Jung, Youwon Shin, Jieun Lim, and Uichin Lee. "CareMouse: An Interactive Mouse System that Supports Wrist Stretching Exercises in the Workplace". *CHI Conference on Human Factors in Computing Systems Extended Abstracts (CHI '22)*.
- Dasom Choi, Uichin Lee, and Hwajung Hong. "It's not wrong, but I'm quite disappointed”: Toward an Inclusive Algorithmic Experience for Content Creators with Disabilities". *CHI Conference on Human Factors in Computing Systems (CHI '22)*.
- M. Sami Zitouni, Peter Lee, Uichin Lee, Leontios J. Hadjileontiadis, and Ahsan Khandoker. "Privacy Aware Affective State Recognition From Visual Data". *IEEE Access, Volume 10*.
- 신유원, 이현수, 최우혁, 김희평, 정용, and 이의진. "스마트홈 IoT 기술 및 프라이버시 최신 연구 동향". *한국정보과학회 학술발표논문집*.

**2021**

- Inyeop Kim, Hwarang Goh, Youngtae Noh, and Uichin Lee. "Poster: Exploring User Contexts and Needs for Context-aware Smartphone Distraction Management". *Adjunct Proceedings of the 2021 ACM International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2021 ACM International Symposium on Wearable Computers (UbiComp '21)*.
- Soowon Kang, Heepyung Kim, Youngtae Noh, and Uichin Lee. "Poster: Toward Context-aware Proactive Conversation for Smart Speakers". *Adjunct Proceedings of the 2021 ACM International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2021 ACM International Symposium on Wearable Computers (UbiComp '21)*.
- Sara A. Nasrat, Uichin Lee, M. Sami Zitouni, Ahsan H. Khandoker, Soowon Kang, and Herbert F. Jelinek. "Emotion Recognition in the Wild from Long-term Heart Rate Recording using Wearable Sensor and Deep Learning Ensemble Classification". *2021 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)*.
- M. Sami Zitouni, Cheul Young Park, Uichin Lee, Leontios Hadjileontiadis, and Ahsan Khandoker. "Arousal-Valence Classification from Peripheral Physiological Signals Using Long Short-Term Memory Networks". *2021 43rd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC)*.
- Hankyung Kim, Hoyeon Nam, Uichin Lee, and Youn-kyung Lim. "Utilitarian or Relational? Exploring Indicators of User Orientation Towards Intelligent Agents". *Communications in Computer and Information Science*.
- Gyuwon Jung, Jio Oh, Youjin Jung, Juho Sun, Ha-Kyung Kong, and Uichin Lee. "Good Enough!”: Flexible Goal Achievement with Margin-based Outcome Evaluation". *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems (CHI '21)*.
- Joonyoung Park, Hyunsoo Lee, Sangkeun Park, Kyong-Mee Chung, and Uichin Lee. "GoldenTime: Exploring System-Driven Timeboxing and Micro-Financial Incentives for Self-Regulated Phone Use". *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems (CHI '21)*.
- Minhyung Kim, Inyeop Kim, and Uichin Lee. "Beneficial Neglect: Instant Message Notification Handling Behaviors and Academic Performance". *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, Volume 5, Issue 1*.
- Yongshin Kim, Panyu Zhang, Gyuwon Jung, Heepyung Kim, and Uichin Lee. "Causal Analysis of Observational Mobile Sensor Data: A Comparative Study". *한국정보과학회 학술발표논문집*.
- 김채원, 정유경, 정규원, 우운택, and 이의진. "Cheersbot: 외로움 개선을 위한 물리적/청각적 상호작용을 제공하는 술친구 소셜 로봇". *한국 HCI 학회 학술대회*.

## 특허

연구실 목록에 게시된 3건이다. 출원일 또는 등록일이 2021-10-13–2026-10-13에 드는 항목이며, 번호와 날짜는 각 특허 기록에 따른다.[^pubs]

- Analysis system and method for causal inference of digital therapeutics based on mobile data [^pat1] (번호 US17/844,648; 출원일 2022-06-20; 발명자 Uichin Lee, Gyuwon Jung, Eun-Yeol Ma, Heeyoung Kim)
- Method and system for distraction management of context-aware rule-based smart device [^pat2] (번호 US11290590B2; 출원일 2020-11-27; 등록일 2022-03-29; 발명자 Uichin Lee, Inyeop Kim)
- Method and apparatus for context-adaptive personalized psychological state sampling for wearable device [^pat3] (번호 US11439334B2; 출원일 2019-05-21; 등록일 2022-09-13; 발명자 Uichin Lee, Cheulyoung Park, Soowon Kang, Auk Kim, Narae Cha)

## 소식

2021-10-13–2026-10-13 범위의 첫 화면 Lab News와 연구실 블로그 소식 2건이다.[^home][^blog53]

- 2026-05-26 · 정신과 초진 AI에 관한 언론 보도가 연구실 소식에 게시됐다.[^home]
- 2026-09-22 · 스마트폰·스마트워치 기반 건강·안녕 연구 플랫폼 EnPULSE(Enabling Platform for User Logging & Sensing Environment)의 구조와 기능을 소개했다.[^blog53]

## 연락과 위치

- 연구실: KAIST N1 721호, 대전광역시 유성구 대학로 291.[^home][^dept]
- 교수연구실: KAIST N1 706호.[^prof]
- 전화: 042-350-3544.[^dept]
- 교수 이메일: uclee@kaist.ac.kr.[^p1]

## 각주
[^p1]: H. Lee 외, U. Lee, Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies 9, 187 (2025). <https://doi.org/10.1145/3770644> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://ic.kaist.ac.kr/publications/papers/lee2025leveraging.pdf> (연구실 게시 논문 PDF의 초록, 관측일 2026-10-30).
[^p2]: J. Kim, D. Lee, U. Lee, SoftwareX 31, 102325 (온라인 2025-08-28). <https://doi.org/10.1016/j.softx.2025.102325> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://ic.kaist.ac.kr/publications/papers/kim2025affectstream.pdf> (연구실 게시 논문 PDF의 초록, 관측일 2026-10-30).
[^p3]: G. Jung, U. Lee, Proceedings of the CHI Conference on Human Factors in Computing Systems (2025). <https://doi.org/10.1145/3706598.3713730> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://ic.kaist.ac.kr/publications/papers/jung2025counterstress.pdf> (연구실 게시 논문 PDF의 초록, 관측일 2026-10-30).
[^p4]: A. Orzikulova 외, S.-J. Lee, Proceedings of the ACM on Human-Computer Interaction 7, 274 (2023). <https://doi.org/10.1145/3610065> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://ic.kaist.ac.kr/publications/papers/orzikulova2023finerme.pdf> (연구실 게시 논문 PDF의 초록, 관측일 2026-10-30).
[^p5]: Y. Jung 외, U. Lee, Proceedings of the CHI Conference on Human Factors in Computing Systems (2026). <https://doi.org/10.1145/3772318.3790970> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://ic.kaist.ac.kr/publications/papers/jung2026toward.pdf> (연구실 게시 논문 PDF의 초록, 관측일 2026-10-30).
[^p6]: H. Park 외, U. Lee, Proceedings of the CHI Conference on Human Factors in Computing Systems (2026). <https://doi.org/10.1145/3772318.3790745> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://ic.kaist.ac.kr/publications/papers/park2026why.pdf> (연구실 게시 논문 PDF의 초록, 관측일 2026-10-30).
[^p7]: H. Lee 외, U. Lee, Proceedings of the CHI Conference on Human Factors in Computing Systems (2024). <https://doi.org/10.1145/3613904.3642815> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://ic.kaist.ac.kr/publications/papers/lee2024priviaware.pdf> (연구실 게시 논문 PDF의 초록, 관측일 2026-10-30).
[^p8]: E. Park, Y. Jung, I. Kim, U. Lee, Proceedings of the CHI Conference on Human Factors in Computing Systems (2023). <https://doi.org/10.1145/3544548.3581457> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://ic.kaist.ac.kr/publications/papers/park2023charlie.pdf> (연구실 게시 논문 PDF의 초록, 관측일 2026-10-30).

[^home]: ICLab 첫 화면, Human-centered AI·Research Projects·Lab News·위치. <https://ic.kaist.ac.kr/> (관측일 2026-10-30).
[^dept]: KAIST 전산학부 연구실 소개, 인터랙티브 컴퓨팅 연구실, 연구 분야·위치·전화. <https://cs.kaist.ac.kr/research/labView?sn=112&menu=64> (관측일 2026-10-27).
[^prof]: KAIST 전산학부 교수 소개, 이의진, 직위·소속·참여·학위·경력·연구 분야. <https://cs.kaist.ac.kr/people/view?idx=617&kind=faculty&menu=160> (관측일 2026-10-30).
[^members]: ICLab, Members, 현재 구성원과 Alumni. <https://ic.kaist.ac.kr/members> (관측일 2026-10-30).
[^pubs]: ICLab, Publications, 2021–2026년 구역의 제목·저자·발표처·수상 표기. <https://ic.kaist.ac.kr/publications> (관측일 2026-10-30).
[^hatebuffer]: S. Park, J. Kim, J. Choi, J. Seering, U. Lee, S.-J. Lee, HateBuffer: Safeguarding Content Moderators' Mental Well-Being through Hate Speech Content Modification, Proceedings of the ACM on Human-Computer Interaction 9(7), CSCW428 (2025). <https://doi.org/10.1145/3757609> 초록 기준(연구실 게시 논문 PDF). 초록 원문 <https://ic.kaist.ac.kr/publications/papers/park2025hatebuffer.pdf> (관측일 2026-10-30).
[^pat1]: Google Patents, US20230268080A1, 서지와 초록. <https://patents.google.com/patent/US20230268080A1/en> (관측일 2026-10-30).
[^pat2]: Google Patents, US11290590B2, 서지와 초록. <https://patents.google.com/patent/US11290590B2/en> (관측일 2026-10-30).
[^pat3]: Google Patents, US11439334B2, 서지와 초록. <https://patents.google.com/patent/US11439334B2/en> (관측일 2026-10-30).

[^ai-faculty]: KAIST AI컴퓨팅학과, 교수진, 이의진 학과장·전임교수 및 교수연구실. <https://aicollege.kaist.ac.kr/aic/faculty> (관측일 2026-10-30).
[^fusion]: Y. Koh 외, U. Lee, A Multimodal Sensor Fusion Approach for Mental Health Detection Using Mobile, Wearable, and IoT Sensors, IEEE Journal of Biomedical and Health Informatics (게재 승인). <https://doi.org/10.1109/JBHI.2026.3733235> 초록 기준(연구실 게시 논문 PDF). 초록 원문 <https://ic.kaist.ac.kr/publications/papers/koh2026multimodal.pdf> (관측일 2026-10-30).
[^blog53]: KAIST ICLAB, Overview: EnPULSE, EnPULSE for Mobile & Wearable Computing, 2026-09-22. <https://brunch.co.kr/@kaisticlab/53> (관측일 2026-10-30).

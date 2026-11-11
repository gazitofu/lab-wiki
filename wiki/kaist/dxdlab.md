# DxD Lab (Design, Interaction, and Data)

**KAIST 산업디자인학과 · 홍화정 부교수**

- 분야: 인간–컴퓨터 상호작용, 사람과 인공지능의 협업, 정신 건강 기록 시스템, 포용적 설계
- 대분야: 컴퓨팅·AI
- 태그: 인간–컴퓨터 상호작용[^home], 재활·보조·접근성 기술[^accessibility], 책임 있는 AI·공정성[^alignment], 다중 에이전트 시스템·분산 의사결정[^collectives]
- 홈페이지: <https://dxd-lab.github.io/>
- 근거와 출처: [DxD Lab 근거 페이지](dxdlab-sources.md)

> 사람이 인공지능과 함께 글을 쓰고 자신을 돌아보며 서로 소통할 수 있도록, 사용자 경험과 상호작용 시스템을 설계하고 평가하는 연구실이다.[^home][^project]

## 무엇을 연구하나

DxD Lab은 사람과 컴퓨터 사이의 입력·출력과 사용 경험을 설계·평가하는 인간–컴퓨터 상호작용(HCI, Human–Computer Interaction) 연구실이다.[^home] 데이터에서 출발하고, 데이터와 함께하며, 데이터로 설계하는 방법을 탐구한다. 사람의 가치와 능력을 중심에 두는 인공지능(AI, Artificial Intelligence) 협업 시스템을 만들고 평가하며, 정신 건강과 신경다양성(사람마다 신경 발달과 인지 특성이 다양하다는 관점)을 주요 적용 대상으로 삼는다.[^home]

첫째 갈래는 **사람이 조정하는 인공지능 협업**이다. 연구실은 여러 에이전트(환경에서 정보를 받아 판단하고 행동하는 주체)의 구성·역할·관계를 사용자가 정하는 협업 방식을 연구한다.[^project] Google Multilab Project의 Collective Curation도 사용자가 인공지능 팀을 구성하고 감독하는 연구로 소개한다.[^collectives] CrafTeam에서는 설계자가 인공지능 팀을 만들고 함께 아이디어를 내도록 했다. 사용자 연구에서는 처음에 팀의 자율 작동을 시도하던 참여자들이 직접 에이전트들을 조정하는 구성을 채택했다.[^p1] 설계 교육용 Feed-O-Meter는 학습자가 지도자가 되고 인공지능이 피드백을 받는 학습자 역할을 맡도록 만든 시스템이다.[^p5]

둘째 갈래는 **기록을 통한 자기 이해**다. 연구실은 생성형 인공지능(학습한 자료의 특성을 바탕으로 글·그림 같은 새 내용을 만드는 인공지능)을 활용해 일기 공동 작성과 개인 데이터 성찰을 돕는 상호작용 방법을 개발한다.[^health] Moodialogue는 기록한 감정을 대화 가능한 대상으로 의인화했다. 참여자들은 이를 통해 기록 당시에 놓쳤던 맥락과 함께 존재하던 감정을 살폈다.[^p2] MindfulDiary는 대형 언어 모델(LLM, Large Language Model, 많은 글을 학습해 문장을 이해하고 생성하는 인공지능 모델)을 이용해 정신과 환자의 대화형 일기 작성을 돕는다. 전문가 지침을 대화 상태에 맞춰 따르면서 자유로운 대화도 이어 가도록 설계했다.[^p7] MindScope는 일상 활동으로 예측한 스트레스와 그 이유를 설명하여 사용자가 자신의 경험을 돌아보도록 했다.[^p8]

셋째 갈래는 **당사자와 함께 만드는 포용적 기술**이다. 연구실은 사용 당사자가 설계 과정에 함께 참여하는 참여형 설계에 바탕을 두고, 신경다양성이 있는 사람과 장애인의 생활·소통을 돕는 보조 기술을 개발한다.[^project] 접근성과 공정성을 높이기 위해 알고리즘(문제를 풀도록 정한 계산 절차) 기반 플랫폼을 조사하고 다시 설계하는 일도 다룬다.[^project] AACessTalk는 말로 표현하는 데 제약이 있는 자폐 아동과 부모의 대화를 위해, 부모에게는 대화 안내를 주고 아동에게는 맥락에 맞는 어휘 카드를 추천하는 시스템이다.[^p3] The Workplace Playbook VR은 가상현실(VR, Virtual Reality, 컴퓨터가 만든 가상 공간을 보고 조작하게 하는 기술)로 자폐인의 직장 내 사회적 의사소통을 지원하고 주변 지원망의 이해를 돕는 개념을 탐색한다.[^accessibility]

넷째 갈래는 **인공지능 평가와 사람의 가치**다. 연구실은 모델 능력을 재는 평가 문제와 기준을 새로 만들고, 학습 자료와 실제 사회적 영향을 함께 분석하여 인공지능이 사람의 가치에 맞게 작동하도록 하는 방법을 연구한다.[^project][^alignment] StereoHunter는 사용자가 언어 모델에서 고정관념을 드러내는 응답을 끌어내고 판단하도록 만든 연구 도구다. 참여자의 배경과 모델에 대한 생각에 따라 판단이 달라지는 점을 살피고, 다양한 사용자 관점을 공정성 평가에 반영할 방법을 논의했다.[^p4]

## 주요 연구 주제

### 사용자가 구성하는 인공지능 팀과 공동 집필

사람이 인공지능 팀의 구성과 역할을 정하고, 함께 아이디어를 만들며 그 과정을 돌아보는 도구를 설계한다.[^project][^p1] 연구 홍보용 문답 글을 함께 쓰는 AQUA에서는 작성 부담을 줄일 가능성과 함께, 작성자의 고유한 의도가 충분히 반영되지 않거나 답변을 세심하게 고치려는 노력이 줄어드는 문제도 살폈다.[^p6]

### 감정·일상 기록의 새로운 상호작용

감정 기록을 대화 대상으로 만들거나, 일상의 스트레스 예측에 설명을 붙여 자기 경험을 돌아보도록 한다.[^p2][^p8] 정신 건강 기록에서는 전문가 지침을 지키면서 자유로운 대화를 이어 가는 대화 구조를 다룬다.[^p7]

### 의사소통과 접근성을 위한 설계

신경다양성이 있는 사람과 장애인을 설계 과정에 참여시키고, 생활과 소통을 돕는 보조 시스템을 만든다.[^project] AACessTalk는 부모의 대화 방식과 아동의 표현 기회를 함께 지원하도록 서로 다른 안내 기능을 결합했다.[^p3]

### 사용자 관점의 인공지능 평가

모델의 기술적 능력을 재는 기준과 사회적 영향 조사를 함께 다룬다.[^project] 언어 모델의 고정관념을 사용자가 어떻게 발견하고 해석하는지 살피며, 그 관점 차이를 평가 설계에 연결한다.[^p4]

## 대표 논문

KAIST 재직 시기의 2022–2026년 논문 가운데 연구 갈래와 시스템을 고르게 보여 주는 여덟 편이다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 주요 저자와 교수 역할 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2026 | [Understanding Human-Multi-Agent Team Formation for Creative Work](https://doi.org/10.1145/3772318.3791166) · CHI | 1저자 Hyunseung Lim; 홍화정 공저자 | 설계자가 인공지능 팀을 구성하고 함께 아이디어를 내는 CrafTeam을 만들었다. 참여자들은 팀의 자율 작동을 시도하다가 자신이 직접 구성원들을 조정하는 방향으로 팀을 바꿨다.[^p1] |
| 2 | 2026 | [Moodialogue: Transforming Emotions into Personified, Conversational Agents](https://doi.org/10.1145/3772318.3790807) · CHI | 1저자 Sangsu Jang; 홍화정 공저자 | 감정을 기록한 뒤 그 감정을 의인화한 상대와 대화하게 했다. 참여자들은 놓쳤던 상황과 함께 있던 다른 감정을 돌아보고, 긍정적 감정을 음미하거나 부정적 감정을 다른 관점에서 해석했다고 보고했다.[^p2] |
| 3 | 2025 | [AACessTalk: Fostering Communication between Minimally Verbal Autistic Children and Parents with Contextual Guidance and Card Recommendation](https://doi.org/10.1145/3706598.3713792) · CHI | 1저자 Dasom Choi; 홍화정 공저자 | 부모에게는 대화를 이어 갈 안내를, 아동에게는 상황에 맞는 어휘 카드를 제공하는 태블릿 시스템을 만들었다. 사용 연구에서 대화와 차례 주고받기가 늘고, 부모의 상호작용 방식 탐색을 돕고 아동이 의사소통에서 더 큰 주도권을 갖도록 도왔다.[^p3] |
| 4 | 2025 | [How Do Users Identify and Perceive Stereotypes? Understanding User Perspectives on Stereotypical Biases in Large Language Models](https://doi.org/10.1145/3715275.3732207) · FAccT | 1저자 Hyunseung Lim; 홍화정 공저자 | StereoHunter라는 도구로 사용자가 언어 모델의 고정관념을 발견하고 판단하는 과정을 살폈다. 배경과 모델에 대한 생각에 따라 달라지는 판단을 공정성 평가에 어떻게 반영할지 논의했다.[^p4] |
| 5 | 2025 | [Feed-O-Meter: Investigating AI-Generated Mentee Personas as Interactive Agents for Scaffolding Design Feedback Practice](https://doi.org/10.1016/j.ijhcs.2025.103687) · International Journal of Human-Computer Studies | 1저자 Hyunseung Lim; 홍화정 공저자 | 학습자가 인공지능 학습자에게 설계 피드백을 주고, 그 피드백이 아이디어 발전에 미치는 영향을 돌아보게 했다. 역할 전환이 참여와 동기를 높이고 상대가 이해할 수 있는 피드백을 연습하도록 도왔다.[^p5] |
| 6 | 2024 | [Co-Creating Question-and-Answer Style Articles with Large Language Models for Research Promotion](https://doi.org/10.1145/3643834.3660705) · DIS | Hyunseung Lim·Ji Yong Cho에 누리집 표시 \*; 홍화정 공저자 | 연구자가 언어 모델과 함께 자신의 논문을 설명하는 문답 글을 쓰는 AQUA를 만들었다. 작성 부담을 덜고 독자 관점을 이해하는 데 도움을 주었지만, 작성자의 고유한 의도를 놓치거나 수정 노력을 줄이는 문제도 나타났다.[^p6] |
| 7 | 2024 | [MindfulDiary: Harnessing Large Language Model to Support Psychiatric Patients' Journaling](https://doi.org/10.1145/3613904.3642937) · CHI | 1저자 Taewan Kim; 홍화정 공저자 | 전문가 지침을 대화 상태에 맞춰 따르는 일기 앱을 만들었다. 환자가 일상 기록을 꾸준히 풍부하게 남기고, 임상의가 환자의 생각과 일상 맥락을 이해하도록 도왔다.[^p7] |
| 8 | 2022 | [Prediction for Retrospection: Integrating Algorithmic Stress Prediction into Personal Informatics Systems for College Students' Mental Health](https://doi.org/10.1145/3491102.3517701) · CHI | 1저자 Taewan Kim; 홍화정 공저자 | 스마트폰이 포착한 일상 활동으로 스트레스 수준을 예측하고 이유를 설명하는 MindScope를 만들었다. 사용자는 예측과 설명을 바탕으로 스트레스 패턴과 과거 경험을 돌아보고 대응을 계획했다.[^p8] |

## 교수와 전문 분야

홍화정은 KAIST 산업디자인학과 부교수이며 DxD Lab의 책임 교수다.[^faculty][^home] KAIST 공식 소식의 국문 표기는 홍화정이다.[^name]

KAIST 연구자 소개는 KAIST 부임 연도를 2021년으로 적으며, 그 이전인 2018–2021년에는 서울대학교에 재직했다고 밝힌다.[^career]

최근 연구에서 드러나는 전문 분야는 사람과 인공지능의 협업 도구 설계, 언어 모델을 이용한 설계 교육과 공동 집필, 감정·정신 건강 기록 시스템, 신경다양성을 고려한 의사소통 기술, 사용자 관점의 인공지능 편향 평가다.[^p1][^p3][^p4][^p5][^p6][^p7]

## 응용 분야

설계자의 창작 협업과 피드백 교육, 연구 홍보 글 작성, 개인의 감정·정신 건강 기록, 자폐 아동과 부모의 의사소통, 인공지능 서비스의 공정성 평가에 연결된다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7]

## 구성원

2026년 11월 11일 연구실 People에 게시된 구성원 16명이다. 시작은 소식에 적힌 연구실 합류 연월이고, 과정은 People의 표기다. 대표 논문 참여는 전체 저자 명단에서 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people][^news]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Hwajung Hong | 부교수 |  | Commons/Commoning; Community-Based Practice; Co-design | hwajung@kaist.ac.kr | 1, 2, 3, 4, 5, 6, 7, 8 |
| Yedam Ryu | 박사후연구원 | 2025-09 | Human-AI Interaction; Large Language Model; Design | ryd0728@kaist.ac.kr |  |
| Hyunseung Lim | 박사과정 | 2022-03 | Accessibility; Collaborative Learning; Educational Technology | charlie9807@kaist.ac.kr | 1, 4, 5, 6 |
| Jiazhou Wu | 박사과정 | 2024-09 | Human-AI Interaction; Multi-Modal Interaction; Accessibility | jzwu0629@kaist.ac.kr |  |
| Joonyoung Park | 박사과정 | 2025-03 | Inclusive Design; Life Transition; Speculative Design | joonyoung@kaist.ac.kr |  |
| Hyuna Jo | 박사과정 |  | Culturally Responsive AI; Inclusive Design; Human-AI Interaction | hyunajo@kaist.ac.kr |  |
| Jaein Kim | 박사과정 | 2026-09 | Human-AI Interaction; Self-reflection; Speculative Design | jaeinkim@kaist.ac.kr |  |
| Gahyeon Bae | 석사과정 | 2025-03 | Accessibility; Human-AI Interaction; Marginalized People | bghblue@kaist.ac.kr | 2 |
| Se Hee Kim | 석사과정 | 2025-09 | Human-AI Interaction; Agency; Personalization | seheekim@kaist.ac.kr |  |
| Eunchae Lee | 석사과정 | 2025-09 | Human-AI Interaction; Mental Health; Participatory Design; Responsible AI | chaelee@kaist.ac.kr |  |
| Sieun Kim | 석사과정 | 2026-03 | Human-AI Interaction; Creativity Support Tools; Speculative Design | sieunkim@kaist.ac.kr | 2 |
| Changhwi Park | 석사과정 | 2026-09 | Human-AI Interaction; Agency; AI-Mediated Communication | changhwipark@kaist.ac.kr |  |
| Hajun Kim | 인턴 |  | Accessibility; Marginalized People; Wearable Computing |  |  |
| Hyunji Huh | 학부 인턴 |  | Human-Human Interaction; Modern Loneliness; Design Intervention | hyunjihuh@kaist.ac.kr |  |
| Yu Min Choi | 학부 인턴 |  | Human-AI Interaction; Self-Reflection; Personal Informatics | yumin.choi@kaist.ac.kr |  |
| Sunmyeong Lee | 학부 인턴 |  |  | sunnie@sogang.ac.kr |  |

## 졸업생과 이전 구성원

People의 Alumni에 게시된 26명의 과정·직위와 진로다. 방문 학생과 인턴도 이 구획의 표기대로 포함한다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Bogoan Kim | Postdoctoral Researcher | assistant professor at Chungbuk National University |
| Sangsu Jang | Postdoctoral Researcher | assistant professor at Chung-Ang University |
| Taewan Kim | Ph.D. Student | research scientist at TwelveLabs |
| Dasom Choi | Ph.D. Student | assistant professor at National University of Singapore |
| Kwangyoung Lee | Ph.D. Student | researcher at Samsung Display |
| Peter Daish | Visiting Ph.D. Student | research assistant at Swansea University |
| Lucy Truong | Visiting Ph.D. Student | doctoral researcher at Aalto University |
| Chowon Kang | Master's Student | product manager at proby.io |
| Sooyeon Ahn | Master's Student | Ph.D. student at Royal College of Art |
| Yeohyun Jung | Master's Student | product manager at Elice |
| Jong-ok Hong | Master's Student | UX designer at CJ Olive Networks |
| Sooyohn Nam | Master's Student | software engineer at NH Investment & Securities |
| Jongik Jeon | Visiting Master's Student | Ph.D. student at Virginia Tech |
| Sungmin Na | Intern |  |
| Yubin Choi | Undergraduate Intern |  |
| Eunseo Oh | Undergraduate Intern |  |
| Seokyoung Park | Undergraduate Intern |  |
| Inhwa Song | Undergraduate Intern |  |
| Donggun Lee | Undergraduate Intern |  |
| Suyoun Lee | Undergraduate Intern |  |
| Junghoon Han | Undergraduate Intern |  |
| Jaehoon Park | Undergraduate Intern |  |
| Suyeon Seo | Undergraduate Intern |  |
| Enrique Jose Delgado Garcia | Undergraduate Intern |  |
| Eunji Shin | Undergraduate Intern |  |
| Kyuwon Cho | Undergraduate Intern |  |

## 최근 5년 논문 목록

연구실 Publications의 2021–2026년 구역에서 51편을 싣는다. 학회·학술지 논문뿐 아니라 워크숍·포스터·pictorial(설계 과정과 결과를 그림 중심으로 싣는 논문 형식)도 포함하며 제목·저자·발표처와 연도 구역은 연구실 표기다. 대표 논문 표의 연도는 출판 서지의 연도다. 저자 이름의 별표는 누리집 표시이며 역할로 풀지 않았다.[^publication] 홍화정은 2021년 KAIST에 부임했으며, 목록의 2022년 항목에는 서울대 재직 시기에 수행된 연구가 섞였을 수 있다.[^career]

**2026**

- Junyeong Park, Sowon Min, Euna Jang, Soobin Kim, Jiho Jin, Hyunseung Lim, Gahyeon Bae, Hwajung Hong. "Investigating Social Bias in Narrative Image Generation". *COLM 2026 GenAI4World Workshop*.
- Hyunseung Lim, Hwajung Hong. "Toward User-Orchestrated Human–Multi-Agent Teams for Co-Creation". *ICML Workshop 2026*.
- Jiazhou Wu, Dasom Choi, Bogoan Kim, Hwajung Hong. "When Special Education Meets LLMs: Investigating the use of LLM-based Conversational AI by Special Education Teachers for Autism in China". *DIS 2026 DOI: 10.1145/3800645.3812968*.
- Jong-ok Hong, Dasom Choi, Eunchae Lee, Hwajung Hong. "Who Sets the Norm?: Designing Communication Scaffolds for ADHD Romantic Relationships". *DIS 2026 DOI: 10.1145/3800645.3812917*.
- Sooyohn Nam, Yeohyun Jung, Kyuwon Cho, Hyunseung Lim, Hwajung Hong. "MindStock: Investigating How Principle-Anchored Feedback Supports Self-Reflection in Mobile Investment". *DIS 2026 DOI: 10.1145/3800645.3812925*.
- Jeanne Choi, Dasom Choi, Sejun Jeong, Hwajung Hong, Joseph Seering. "Situating the Development of Conversational Artificial Intelligence in the Social and Structural Contexts of People with Visual Impairments". *DIS 2026 DOI: 10.1145/3800645.3812959*.
- Yeohyun Jung, Sooyohn Nam, Junhyun An, Hwajung Hong. "Your Call-Keep or Wrap: Examining the Impact of Self-regulatory Intervention on Short-form Video Consumption Behavior". *CHI 2026 DOI: 10.1145/3772318.3791925*.
- Sieun Kim, Yeeun Jo, Sungmin Na, Hyunseung Lim, Eunchae Lee, Yu Min Choi, Soohyun Cho, Hwajung Hong. "Dark and Bright Side of Participatory Red-Teaming with Targets of Stereotyping for Eliciting Harmful Behaviors from Large Language Models". *CHI 2026 DOI: 10.1145/3772318.3790820*.
- Sung-In Kim\*, Joonyoung Park\*, Bogoan Kim, Hwajung Hong. "I Choose to Live, for Life Itself”: Understanding Agency of Home-Based Care Patients Through Information Practices and Relational Dynamics in Care Networks". *CHI 2026 DOI: 10.1145/3772318.3791154*.
- Hyunseung Lim, Dasom Choi, Sooyohn Nam, Bogoan Kim, Hwajung Hong. "Understanding Human-Multi-Agent Team Formation for Creative Work". *CHI 2026 DOI: 10.1145/3772318.3791166*.
- Sangsu Jang, Sieun Kim, Gahyeon Bae, Hwajung Hong. "Moodialogue: Transforming Emotions into Personified, Conversational Agents". *CHI 2026 DOI: 10.1145/3772318.3790807*.
- Youngji Koh, Jeonghyun Kim, Kwangyoung Lee, Yugyeong Jung, Hwajung Hong, Uichin Lee. "Exploring Data-Driven Approaches to Stress Management: A Systematic Review of Stress Tracking, Intervention, and System Evaluation Methods". *CHI 2026 DOI: 10.1145/3772318.3791194*.
- Junho Myung, Hyunseung Lim, Hana Oh, Hyoungwook Jin, Nayeon Kang, So-Yeon Ahn, Hwajung Hong, Alice Oh, Juho Kim. "When Scaffolding Breaks: Investigating Student Interaction with LLM-Based Writing Support in Real-Time K-12 EFL Classrooms". *CHI 2026 DOI: 10.1145/3772318.3791517*.
- Jackie Liu, Mehrnoosh Shivani, Hwajung Hong, Ig-Jae Kim, Dongwook Yoon. "Social Media Clones: Exploring the Impact of Social Delegation with AI Clones through a Design Workbook Study". *CSCW 2026 DOI: 10.1145/3788072*.
- Sung-In Kim, Joonyoung Park, Taewan Kim, Woosuk Seo, Taerim Kim, Won Chul Cha, Hwajung Hong. "Enhancing Patient Participation in Emergency Department through Patient-Friendly Clinical Notes Generated by Large Language Models". *Scientific Reports 16 DOI: 10.1038/s41598-025-31113-y*.
- Hyunseung Lim, Dasom Choi, DaEun Choi, Sooyohn Nam, Hwajung Hong. "Feed-O-Meter: Investigating AI-Generated Mentee Personas as Interactive Agents for Scaffolding Design Feedback Practice". *IJHCS Special Issue “AI-Generated Personas: Representing User Needs with Generative AI Models” DOI: 10.1016/j.ijhcs.2025.103687*.
- Donggun Lee, Suyoun Lee, Hyunseung Lim, Hwajung Hong. "Creating Text-Based AI Clones of Myself: Exploring Perceptions, Development Strategies, and Challenges". *IJHCS Special Issue “AI-Generated Personas: Representing User Needs with Generative AI Models” DOI: 10.1016/j.ijhcs.2025.103692*.

**2025**

- Hyunseung Lim, Sooyohn Nam, Sungmin Na, Ji Yong Cho, June Yong Yang, Hyungyu Shin, Yoonjoo Lee, Juho Kim, Moontae Lee, Hwajung Hong. "PANORAMA: A Dataset and Benchmarks Capturing Decision Trails and Rationales in Patent Examination". *NeurIPS 2025 Datasets and Benchmarks Track DOI: 10.52202/085713-1735*.
- Hyungyu Shin, Jingyu Tang, Yoonjoo Lee, Nayoung Kim, Hyunseung Lim, Ji Yong Cho, Hwajung Hong, Moontae Lee, Juho Kim. "Mind the Blind Spots: A Focus-Level Evaluation Framework for LLM Review". *EMNLP 2025 Main*.
- Hyewon Lee, Ihchae Ryu, Yumin Cho, Hyunseung Lim, Hwajung Hong. "RADI: A Design Framework for Relational and Adaptive Disclosure Interfaces". *UIST 2025 Poster DOI: 10.1145/3746058.3758404*.
- Sunjun Kweon, Sooyohn Nam, Hyunseung Lim, Hwajung Hong, Edward Choi. "A Large-Scale Real-World Evaluation of an LLM-Based Virtual Teaching Assistant". *ACL (Industry) 2025 DOI: 10.18653/v1/2025.acl-industry.60*.
- Yeohyun Jung, Suyeon Seo, Hwajung Hong. "Beyond the Scroll: Exploring the Design Space of Balanced Short-form Video Consumption through Everyday User Experiences". *DIS PWiP 2025 DOI: 10.1145/3715668.3736346*.
- Sooyohn Nam, Yeohyun Jung, Hwajung Hong. "From Impulsive Investment to Mindful Decisions: Exploring Design Opportunities of AI-Mediated Interventions for Emotionally Biased Investors". *DIS PWiP 2025 DOI: 10.1145/3715668.3736345*.
- Jong-ok Hong, Dasom Choi, Hwajung Hong. "Seeking Harmony in a Beautiful Mess: Designing for Romantic Relationship Navigation of ADHD-Neurotypical Couples". *DIS PWiP 2025 DOI: 10.1145/3715668.3736343*.
- Yeohyun Jung, Kwangyoung Lee, Hwajung Hong. "Thinking Outside the Data Box: Investigating the Potential of Data Manipulation for Self-Reflection on Personal Data". *DIS 2025 DOI: 10.1145/3715336.3735840*.
- Hyunseung Lim, Dasom Choi, Hwajung Hong. "How Do Users Identify and Perceive Stereotypes? Understanding User Perspectives on Stereotypical Biases in Large Language Models". *FAccT 2025 DOI: 10.1145/3715275.3732207*.
- Sooyeon Ahn, Wonkwang Son, Hui Yeong Baek, Hwajung Hong. "Designing OWN, The Inner World as a Virtual Space: By and For Introspection". *C&C Pictorial 2025 DOI: 10.1145/3698061.3726951*.
- Dasom Choi, SoHyun Park, Kyungah Lee, Hwajung Hong, Young-Ho Kim. "AACessTalk: Fostering Communication between Minimally Verbal Autistic Children and Parents with Contextual Guidance and Card Recommendation". *CHI 2025 DOI: 10.1145/3706598.3713792*.
- Gahyeon Bae, Seokyoung Park, Taewan Kim, Hwajung Hong. "Exploring Design Spaces to Facilitate Household Collaboration for Cohabiting Couples". *CHI 2025 DOI: 10.1145/3706598.3713383*.
- Kwangyoung Lee, Yeohyun Jung, Gyuwon Jung, Xi Lu, Hwajung Hong. "Peerspective: A Study on Reciprocal Tracking for Self-awareness and Relational Insight". *CHI 2025 DOI: 10.1145/3706598.3713404*.

**2024**

- Hyunseung Lim, Dasom Choi, Hwajung Hong. "Identify Design Problems Through Questioning: Exploring Role-playing Interactions with Large Language Models to Foster Design Questioning Skills". *CSCW Poster 2024 DOI: 10.1145/3678884.3681912*.
- Chowon Kang, Yoonseo Choi, Yongjae Sohn, Hyunseung Lim, Hwajung Hong. "Beyond Swipes and Scores: Investigating Practices, Challenges and User-Centered Values in Online Dating Algorithms". *CSCW 2024 DOI: 10.1145/3687025*.
- Hyunseung Lim\*, Ji Yong Cho\*, Taewan Kim, Jeongeon Park, Hyungyu Shin, Seulgi Choi, Sunghyun Park, Kyungjae Lee, Juho Kim, Moontae Lee, Hwajung Hong. "Co-Creating Question-and-Answer Style Articles with Large Language Models for Research Promotion". *DIS 2024 DOI: 10.1145/3643834.3660705*.
- Taewan Kim, Seolyeong Bae, Hyun AH Kim, Su-woo Lee, Hwajung Hong, Chanmo Yang, Young-Ho Kim. "MindfulDiary: Harnessing Large Language Model to Support Psychiatric Patients' Journaling". *CHI 2024 DOI: 10.1145/3613904.3642937*.
- Taewan Kim, Donghoon Shin, Young-Ho Kim, Hwajung Hong. "DiaryMate: Understanding User Perceptions and Experience in Human-AI Collaboration for Personal Journaling". *CHI 2024 DOI: 10.1145/3613904.3642693*.
- Dasom Choi, Sunok Lee, Sung-In Kim, Kyungah Lee, Hee Jeong Yoo, Sangsu Lee, Hwajung Hong. "Unlock Life with a Chat(GPT): Integrating Conversational AI with Large Language Models into Everyday Lives of Autistic Individuals". *CHI 2024 DOI: 10.1145/3613904.3641989*.

**2023**

- Yubin Choi, Dasom Choi, Hwajung Hong. "Together we turn uncertainty into action: understanding the role of artificial intelligence in supporting the financial concerns of older adults". *CSCW Poster 2023 DOI: 10.1145/3584931.3607018*.
- Jieun Han, Haneul Yoo, Yoonsu Kim, Junho Myung, Minsun Kim, Hyunseung Lim, Juho Kim, Tak Yeon Lee, Hwajung Hong, So-Yeon Ahn, Alice Oh. "RECIPE: How to Integrate ChatGPT into EFL Writing Education". *L@S WIP 2023 DOI: 10.1145/3573051.3596200*.
- Dasom Choi, Sung-In Kim, Sunok Lee, Hyunseung Lim, Hee Jeong Yoo, Hwajung Hong. "Love on the spectrum: Toward Inclusive online dating experience of autistic individuals". *CHI 2023 DOI: 10.1145/3544548.3581341*.
- Bogoan Kim, Sung-In Kim, Sangwon Park, Hee Jeong Yoo, Hwajung Hong, Kyungsik Han. "RoutineAid: Externalizing Key Design Elements to Support Daily Routines of Individuals with Autism". *CHI 2023 DOI: 10.1145/3544548.3581048*.
- Taewan Kim, Donghoon Shin, Young-Ho Kim, Hwajung Hong. "DiaryMate: Exploring the Roles of Large Language Models in Facilitating AI-mediated Journaling". *CHI Workshop 2023*.
- Hyeonjeong Im, Soobin Jeon, Haena Cho, Sungyong Shin, Dasom Choi, Hwajung Hong. "AI Story Relay: A Collaborative Writing of Design Fiction to Investigate Artificial Intelligence Design Considerations". *GROUP 2023 DOI: 10.1145/3565967.3570973*.

**2022**

- Ryuhaerang Choi, Chanwoo Yun, Hyunsung Cho, Hwajung Hong, Uichin Lee, Sung-Ju Lee. "You Are Not Alone: How Trending Stress Topics Brought #Awareness and #Resonance on Campus". *Proc. ACM on Human-Computer Interaction, CSCW 2022 DOI: 10.1145/3555612*.
- Xi Lu, Eunkyung Jo, Seora Park, Hwajung Hong, Yunan Chen, Daniel A. Epstein. "Understanding Cultural Influence on Perspectives Around Contact Tracing Strategies". *Proc. ACM on Human-Computer Interaction, CSCW 2022 DOI: 10.1145/3555569*.
- Jennifer G Kim, Taewan Kim, Sung-In Kim, So-youn Jang, Eun Bin (Stephanie) Lee, Heejeong Yoo, Kyungsik Han, Hwajung Hong. "The Workplace Playbook VR: Exploring the Design Space of Virtual Reality to Foster Understanding of and Support for Autistic People". *Proc. ACM on Human-Computer Interaction, CSCW 2022 DOI: 10.1145/3555082*.
- Dasom Choi, Uichin Lee, Hwajung Hong. "It's not wrong, but I'm quite disappointed: Toward an Inclusive Algorithmic Experience for Content Creators with Disabilities". *CHI 2022 DOI: 10.1145/3491102.3517574*.
- Mintra Ruensuk, Taewan Kim, Hwajung Hong, Ian Oakley. "Sad or just jealous? Using Experience Sampling to Understand and Detect Negative Affective Experiences on Instagram". *CHI 2022 DOI: 10.1145/3491102.3517561*.
- Taewan Kim, Haesoo Kim, Hayeon Lee, Hwarang Goh, Shakhboz Abdigapporov, Mingon Jeong, Hyunsung Cho, Kyungsik Han, Youngtae Noh, Sung-Ju Lee, Hwajung Hong. "Prediction for Retrospection: Integrating Algorithmic Stress Prediction into Personal Informatics Systems for College Students' Mental Health". *CHI 2022 DOI: 10.1145/3491102.3517701*.
- Hyun Suk Kim, Yoo Ji Suh, Eun-mee Kim, Eunryung Chong, Hwajung Hong, Boyoung Song, Yena Ko, Ji Soo Choi. "Fact-Checking and Audience Engagement: A Study of Content Analysis and Audience Behavioral Data of Fact-Checking Coverage from News Media". *Digital Journalism 10(5), 2022 DOI: 10.1080/21670811.2021.2006073*.
- Eunkyung Jo, Seora Park, Hyeonseok Bang, Youngeun Hong, Yeni Kim, Jungwon Choi, Bung Nyun Kim, Daniel A. Epstein, Hwajung Hong. "GeniAuti: Toward Data-Driven Interventions to Challenging Behaviors of Autistic Children through Caregivers' Tracking". *Proc. ACM on Human-Computer Interaction, Volume 6 Issue CSCW 1 DOI: 10.1145/3512939*.
- Donghoon Shin, Subeen Park, Esther Hehsun Kim, Soomin Kim, Jinwook Seo, Hwajung Hong. "Exploring the Effects of AI-assisted Emotional Support Processes in Online Mental Health Community". *CHI LBW 2022 DOI: 10.1145/3491101.3519854*.

## 수상과 선정

연구실 소식의 2024–2026년 수상 게시 항목 8건이다. 같은 게시 항목에 함께 적힌 사람은 한 항목으로 묶었다.[^news]

- 2026-03 · Yeohyun, Sieun, Joonyoung이 CHI 2026 Honorable Mention(입선)을 받았다.
- 2025-06 · Sooyeon이 C&C 2025 Honorable Mention(입선)을 받았다.
- 2025-06 · Yeohyun이 DIS 2025 Honorable Mention(입선)을 받았다.
- 2025-04 · Dasom이 CHI 2025 Best Paper Award를 받았다.
- 2024-12 · Donggun과 Suyoun이 URP Program Excellent Award를 받았다.
- 2024-12 · Yeohyun이 Q-Day Creativity and Talent Education Award를 받았다.
- 2024-09 · Yeohyun이 'Oxynizer'로 James Dyson Award 2024 (Domestic)를 받았다.
- 2024-02 · Jong-ok이 Outstanding Graduation Research Award 2024를 받았다.

## 소식

연구실 소식의 2023–2026년 논문 채택·게재 승인·발표·연구 소개 항목 13건이다. 학회 논문은 「채택」, 학술지 논문은 「게재 승인」으로 구분했다.[^news]

- 2026-04 · DIS 논문 네 편이 채택되었다.
- 2025-11 · IJHCS 특별호에 논문 두 편이 게재 승인되었다.
- 2025-09 · NeurIPS 논문 한 편이 채택되었다.
- 2025-05 · Dasom의 연구가 여러 TV 뉴스에 소개되었다.
- 2025-05 · C&C에 pictorial 한 편이 채택되었다.
- 2025-04 · FAccT 논문 한 편이 채택되었다.
- 2025-04 · DIS 논문 한 편과 포스터 세 편이 채택되었다.
- 2025-01 · CHI 논문 세 편이 채택되었다.
- 2024-11 · 연구실 구성원들이 CSCW에서 정규 논문을 발표했다.
- 2024-07 · 정규 논문 한 편과 포스터 한 편이 채택되었다.
- 2024-07 · Hyunseung이 DIS 2024에서 발표했다.
- 2024-05 · DIS 논문 한 편이 채택되었다.
- 2023-01 · CHI 논문 두 편이 채택되었다.

## 연락과 위치

- 교수 업무 이메일: hwajung@kaist.ac.kr.[^home][^faculty]
- 기관 전화: +82-42-350-4529.[^faculty]
- 연구실: KAIST N25 304호.[^home]
- 교수실: KAIST N25 305호.[^faculty]
- 주소: 대전광역시 유성구 대학로 291, KAIST, 우편번호 34141.[^home]

## 각주
[^home]: DxD Lab, 연구실 소개와 연락처. <https://dxd-lab.github.io/> 관측 2026-11-11.
[^project]: DxD Lab, 연구 갈래 소개. <https://dxd-lab.github.io/#/project> 관측 2026-11-11.
[^people]: DxD Lab, People·Alumni. <https://dxd-lab.github.io/#/people> 관측 2026-11-11.
[^publication]: DxD Lab, Publications. <https://dxd-lab.github.io/#/publication> 관측 2026-11-11.
[^news]: DxD Lab, News. <https://dxd-lab.github.io/#/news> 관측 2026-11-11.
[^faculty]: KAIST 산업디자인학과, Faculty. <https://id.kaist.ac.kr/people/Faculty> 관측 2026-11-11.
[^name]: KAIST 홍보실, 「KAIST의 발명적 사고와 재미있는 상상력을 DDP에서」(2022-12-15). <https://kaist.ac.kr/site/news/html/news/?GotoPage=1&mng_no=25770&mode=V&skey=keyword&sval=%EC%83%81%EC%83%81> 관측 2026-11-11.
[^career]: KAIST 연구자 소개, Hwajung Hong. <https://pure.kaist.ac.kr/en/persons/hwajung-hong/> 관측 2026-11-11.
[^health]: DxD Lab, Human-Centered AI for Health. <https://dxd-lab.github.io/#/project/health-ai> 관측 2026-11-11.
[^accessibility]: DxD Lab, Neurodiversity, Accessibility & Algorithmic Inclusion. <https://dxd-lab.github.io/#/project/accessibility> 관측 2026-11-11.
[^alignment]: DxD Lab, Socio-Technical Auditing for AI Alignment. <https://dxd-lab.github.io/#/project/alignment> 관측 2026-11-11.
[^collectives]: DxD Lab, Human-AI Agent Collectives. <https://dxd-lab.github.io/#/project/collectives> 관측 2026-11-11.
[^p1]: H. Lim 외, H. Hong, CHI Conference on Human Factors in Computing Systems (2026). <https://doi.org/10.1145/3772318.3791166> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5025649906,publication_year:2021-2026> 관측 2026-11-11.
[^p2]: S. Jang, S. Kim, G. Bae, H. Hong, CHI Conference on Human Factors in Computing Systems (2026). <https://doi.org/10.1145/3772318.3790807> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5025649906,publication_year:2021-2026> 관측 2026-11-11.
[^p3]: D. Choi 외, Y.-H. Kim, CHI Conference on Human Factors in Computing Systems (2025). <https://doi.org/10.1145/3706598.3713792> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5025649906,publication_year:2021-2026> 관측 2026-11-11.
[^p4]: H. Lim, D. Choi, H. Hong, ACM Conference on Fairness, Accountability, and Transparency (FAccT) (2025). <https://doi.org/10.1145/3715275.3732207> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5025649906,publication_year:2021-2026> 관측 2026-11-11.
[^p5]: H. Lim 외, H. Hong, International Journal of Human-Computer Studies (2025). <https://doi.org/10.1016/j.ijhcs.2025.103687> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5025649906,publication_year:2021-2026> 관측 2026-11-11.
[^p6]: H. Lim 외, H. Hong, Designing Interactive Systems Conference (2024). <https://doi.org/10.1145/3643834.3660705> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5025649906,publication_year:2021-2026> 관측 2026-11-11.
[^p7]: T. Kim 외, Y.-H. Kim, CHI Conference on Human Factors in Computing Systems (2024). <https://doi.org/10.1145/3613904.3642937> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5025649906,publication_year:2021-2026> 관측 2026-11-11.
[^p8]: T. Kim 외, H. Hong, CHI Conference on Human Factors in Computing Systems (2022). <https://doi.org/10.1145/3491102.3517701> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5025649906,publication_year:2021-2026> 관측 2026-11-11.

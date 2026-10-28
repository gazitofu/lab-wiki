# 협동 사회 기술 연구실 (Collaborative Social Technologies Lab, CSTL)

**KAIST 전산학부 · 시어링 조셉(Joseph Seering) 부교수**

- 분야: 인간–컴퓨터 상호작용, 온라인 공동체의 신뢰와 안전, 협업·토론 시스템, 사회적 AI와 언어 모델 평가
- 대분야: 컴퓨팅·AI
- 태그: 인간–컴퓨터 상호작용[^lab][^faculty], 대형 언어 모델[^p5][^p6], 책임 있는 AI·공정성[^p5]
- 홈페이지: <https://cstlab.org/>
- 근거와 출처: [CSTL 근거 페이지](cstlab-sources.md)

> 온라인 공동체에서 사람들이 안전하게 협력하고 소통하도록 도구를 설계하고, 사람 사이의 관계를 지원하는 인공지능과 대화 시스템을 연구한다.[^home][^lab]

## 무엇을 연구하나

CSTL은 KAIST 전산학부의 인간–컴퓨터 상호작용(Human-Computer Interaction, HCI: 사람이 컴퓨터를 사용하는 방식과 경험을 설계하고 평가하는 분야) 연구실이다. 온라인 플랫폼에서 나타나는 갈등과 협력의 사회적·조직적 관계를 이해하고, 이를 바탕으로 새로운 소셜 도구를 만든다.[^lab][^faculty] 연구실은 온라인 신뢰와 안전(온라인 서비스의 이용자를 유해한 행동과 콘텐츠로부터 보호하는 원칙과 활동)을 토대로, 디지털 환경에서의 협업·학습·여가를 지원하는 소셜 컴퓨팅(사람 사이의 사회적 활동을 컴퓨팅 기술로 지원하고 연구하는 분야)을 발전시키겠다고 소개한다.[^home]

첫째 축은 **온라인 공동체 운영과 안전**이다. 모더레이션(공동체의 규칙에 따라 콘텐츠와 이용자의 행동을 관리하는 활동)을 맡는 사람이 어떤 도구를 필요로 하는지 살핀다. ApoloBot 연구는 콘텐츠 삭제나 계정 차단을 넘어, 피해 회복과 당사자의 책임·관계 회복을 중시하는 회복적 정의의 관점을 온라인 도구 설계에 적용했다. Discord에서 사과를 돕는 봇(정해진 기능을 자동으로 수행하며 이용자와 상호작용하는 프로그램)을 만들고, 운영자 인터뷰를 통해 도입의 가능성과 어려움, 설계 시 고려할 점을 정리했다.[^p1] 청소년 Roblox 개발자 공동체 연구에서는 동료의 지원이 기술·사회적 관계·진로 성장에 자원이 되는 한편, 이용자 간 갈등과 공동체 운영 구조의 부족이 복잡한 문제에 대응하는 데 어려움을 준다고 보고했다.[^p2]

둘째 축은 **협업과 토론을 지원하는 시스템**이다. 온라인 게임 연구는 이용자가 게임 상황과 다른 사람에 대한 기대·규범에 따라 의사소통 기회를 판단하며, 소통 자체를 팀이 무너질 조짐으로 보는 경향이 있음을 관찰했다. 이를 바탕으로 이용자의 관점을 반영하는 게임 의사소통 설계를 제안한다.[^p3] 뉴스 댓글 연구는 서로 떨어진 개인 의견을 나열하는 방식 대신, 이용자가 역할을 나누어 댓글을 함께 구성하는 시스템을 만들었다. 평가에서는 관점의 균형과 감정적 중립성이 나타났지만 논거의 강도는 기존 댓글 시스템보다 낮아져, 참여의 포용성과 논의 깊이 사이의 상충 관계를 보여 주었다.[^p4]

셋째 축은 **사회적 AI와 언어 모델 평가**다. 연구실은 사람과 상호작용하는 사회적 AI 에이전트(상황을 바탕으로 행동을 선택하고 수행하는 인공지능 주체)와 시뮬레이션(현상이나 과정의 동작을 모형으로 재현하는 방법)을 발전시키려 한다.[^home] Evalet은 대형 언어 모델(Large Language Model, LLM: 많은 언어 자료를 학습하여 글을 이해하고 생성하는 인공지능 모델)이 다른 생성 결과를 평가할 때, 종합 점수에 가려지는 판단 근거를 드러내는 도구다. 출력물을 조각으로 나누고 각 조각이 평가 기준에서 하는 기능을 보여 주어, 사람이 평가의 어긋남을 검토하도록 돕는다.[^p5] TIDES는 영어·한국어 집단 대화를 담은 데이터셋(연구나 학습에 사용하도록 모아 정리한 자료)으로 팀의 사회적 관계 변화를 다룬다. 이 자료로 추가 학습한 모델은 다음 발화자 예측에서 개선을 보였다. 다만 저자들은 그 개선이 반드시 자연스럽고 일관된 발화 생성으로 이어지는 것은 아니며, 사람이 평가할 때는 기본 모델의 발화를 선호하는 경향이 있었다고 보고했다.[^p6]

## 주요 연구 주제

### 1. 온라인 공동체 운영과 안전

공동체 운영 도구를 설계하고 이용 경험을 살핀다. 사과와 관계 회복을 지원하는 ApoloBot, 청소년 게임 개발자의 동료 지원과 온라인 안전이 대표 대상이다.[^p1][^p2] 최근 논문에는 운영 결정에 대한 이의 제기 체계 연구도 있다.[^research] HateBuffer는 유해 콘텐츠를 다루는 운영자의 정신적 부담을 덜도록 설계한 도구다.[^hatebuffer]

### 2. 온라인 협업과 토론 설계

이용자가 게임 안에서 소통을 선택하는 이유를 이해하고, 뉴스 댓글에 역할 분담을 도입해 공동으로 논의를 구성하는 시스템을 연구한다. 이용자의 관계와 상황 판단을 인터페이스(사람과 시스템이 정보를 주고받고 조작하는 접점) 설계에 반영한다.[^p3][^p4]

### 3. 사회적 AI와 언어 모델 평가

언어 모델의 평가 결과를 조각별로 검토하는 Evalet과, 집단 대화의 발화자·관계 변화를 다루는 TIDES를 연구한다. 모델의 점수나 예측 성능과 사람이 느끼는 유용성·대화 품질을 함께 살피는 것이 주요 문제다.[^p5][^p6]

## 대표 논문

연구실의 2021–2026년 목록 가운데 Joseph Seering이 저자이고 KAIST 부임 뒤인 2025–2026년으로 게시된 논문 6편을 세 연구 갈래에 고르게 담았다. 연도와 발표처는 연구실 표기이며, 링크와 각주는 초록을 읽은 arXiv 판을 가리킨다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다. TIDES는 COLM 2026 채택으로 표시했다.[^research]

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [The Design Space for Online Restorative Justice Tools: A Case Study with ApoloBot](https://doi.org/10.48550/arXiv.2502.18861) · Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems | 온라인 공동체에서 피해가 생겼을 때 삭제와 차단 외에 피해자·가해자·공동체의 필요에 대응할 도구를 탐색했다. 사과를 돕는 Discord 봇 ApoloBot을 만들고 운영자 인터뷰를 통해 설계와 실제 도입에 관한 의견을 살폈다. 회복적 정의를 온라인 공동체에 적용할 때의 기회와 어려움, 후속 설계의 고려 사항을 제시했다.[^p1] | Bich Ngoc (Rubi) Doan, Joseph Seering(마지막 저자) |
| 2 | 2025 | [Leveling Up Together: Fostering Positive Growth and Safe Online Spaces for Teen Roblox Developers](https://doi.org/10.48550/arXiv.2502.18120) · Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems | Roblox에서 게임을 만드는 청소년이 온라인 개발자 공동체에서 얻는 도움과 겪는 어려움을 인터뷰로 살폈다. 공동체는 기술·사회적 관계·진로 성장에 자원이 되지만, 이용자 사이의 갈등과 운영 구조의 부족은 금융 사기 같은 복잡한 문제에 대응하기 어렵게 했다. 이를 바탕으로 청소년 창작자를 위한 긍정적이고 안전한 온라인 공간의 설계 방향을 제안했다.[^p2] | Yubin Choi, Jeanne Choi, Joseph Seering(마지막 저자) |
| 3 | 2025 | [Less Talk, More Trust: Understanding Players' In-game Assessment of Communication Processes in League of Legends](https://doi.org/10.48550/arXiv.2502.17935) · Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems | 온라인 팀 게임에서 이용자가 왜 소통을 선택하거나 경계하는지 관찰과 인터뷰로 살폈다. 이용자는 당장의 게임 상황과 기대·규범을 바탕으로 의사소통 기회를 판단했다. 소통의 내용과 관계없이 이를 팀이 무너질 조짐으로 보는 경향도 나타났다. 이러한 인식을 고려하는 이용자 중심의 게임 의사소통 설계가 필요하다고 제안했다.[^p3] | Juhoon Lee 외, Joseph Seering(마지막 저자) |
| 4 | 2026 | [Fostering Collective Discourse: A Distributed Role-Based Approach to Online News Commenting](https://doi.org/10.48550/arXiv.2510.02766) · Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems | 이용자들이 역할을 나누어 댓글을 함께 구성하는 뉴스 댓글 시스템을 만들었다. 평가에서 이용자는 쟁점 이해, 댓글의 공동 구성, 논의 형성으로 이어지는 참여를 보였다. 댓글의 관점은 균형을 띠고 논증은 감정적으로 중립적이었지만, 기존 방식에 비해 논거의 강도는 낮았다. 역할 분담 설계에서 포용성과 논의 깊이를 함께 고려해야 함을 보여 주었다.[^p4] | Yoojin Hong, Yersultan Doszhan, Joseph Seering(마지막 저자) |
| 5 | 2026 | [Evalet: Evaluating Large Language Models through Functional Fragmentation](https://doi.org/10.48550/arXiv.2509.11206) · Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems | 언어 모델로 생성 결과를 평가할 때 종합 점수만으로는 어떤 부분이 판단에 영향을 주었는지 알기 어렵다. 출력물을 조각으로 나누고 각 조각이 평가 기준에서 하는 기능을 해석하는 방법을 제안했다. 이를 시각화한 Evalet의 사용자 연구에서는 실무자가 평가의 어긋남을 찾아내고 언어 모델 평가에 대한 신뢰를 조정하는 데 도움을 받았다.[^p5] | Tae Soo Kim·Heechan Lee(동등 기여), Joseph Seering(5명 중 4번째), Juho Kim(마지막 저자) |
| 6 | 2026 | [TIDES: A Longitudinal Bilingual Dataset for Modeling Multi-Party Social Dynamics](https://doi.org/10.48550/arXiv.2608.01724) · The Third Annual Conference on Language Modelling (COLM 2026) (채택) | 실제 팀의 장기적인 사회적 관계 변화를 다루기 위해 영어·한국어 집단 대화 자료 TIDES를 만들었다. 상호작용 유형과 역할, 팀의 발달 단계에 관한 표시를 더해 팀의 변화를 분석할 수 있게 했다. 이 자료로 모델을 추가 학습하자 다음 발화자를 예측하는 성능은 개선되었다. 다만 사람의 평가에서는 기본 모델의 발화를 선호하는 경향이 나타났다. 저자들은 예측 성능의 개선이 반드시 자연스럽고 일관된 발화 생성으로 이어지는 것은 아니라며 추가 연구의 필요성을 제시했다.[^p6] | Heechan Lee·Jeonggyu Kang(동등 기여), Joseph Seering(마지막 저자) |

## 교수와 전문 분야

시어링 조셉(Joseph Seering)은 KAIST 전산학부 부교수로 CSTL을 이끈다. 학과는 전공을 Human-Computer Interaction과 Social Computing으로 적는다.[^roster][^faculty] 2020년 Carnegie Mellon University에서 인간–컴퓨터 상호작용 박사학위를 받았고, Stanford University 컴퓨터과학과 박사후연구원과 Stanford Human-Centered AI Institute 펠로우를 지냈다. KAIST 전산학부에는 2023년 8월 1일 부임했다.[^faculty][^appointment]

학과 소개에는 Yale University Social Media Governance Initiative의 affiliated fellow와 Trust and Safety Professionals Association 회원 활동도 올라 있다.[^faculty] 최근 논문을 바탕으로 보면 전문 분야는 공동체 운영과 관계 회복을 지원하는 도구 설계,[^p1][^p2] 게임·뉴스 플랫폼에서의 협업과 갈등을 고려하는 상호작용 설계,[^p3][^p4] 사회적 언어 모델과 그 평가를 사람이 검토하도록 돕는 시스템으로 이어진다.[^p5][^p6]

## 응용 분야

Discord 공동체의 사과와 갈등 대응,[^p1] 청소년 Roblox 개발자 공동체의 지원과 안전,[^p2] 온라인 팀 게임의 의사소통,[^p3] 뉴스 댓글의 공동 토론,[^p4] 언어 모델 평가를 검토하는 도구[^p5]와 집단 대화를 다루는 인공지능[^p6]이 구체적인 응용 대상이다. 연구실은 이러한 시스템을 통해 디지털 플랫폼에서의 협업·학습·여가를 지원하려 한다.[^home]

## 구성원

2026년 10월 27일 Members 페이지 기준으로 교수 외 현재 구성원 14명이다. 대학원생 9명(박사과정 2명·석사과정 7명), 학부 인턴 4명, Affiliated Member 1명이며 과정은 연구실 표기를 따른다. Affiliated Member Yoonseo Choi의 소속은 KAIST로 적혀 있다.[^team] "대표 논문 참여"는 위 표의 전체 저자 목록에 이름이 있는 구성원에게 표시했으며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Changgeon Ko | 박사과정 | pencaty@kaist.ac.kr |  |
| Juhoon Lee | 박사과정 | juhoonlee@kaist.ac.kr | 3 |
| Braahmi Padmakumar | 석사과정 | pjbrahmi@kaist.ac.kr |  |
| Hae Ri Lee | 석사과정 | harriet@kaist.ac.kr |  |
| Hayeon Doh | 석사과정 | hannahdoh@kaist.ac.kr |  |
| Heechan Lee | 석사과정 | hclee99@kaist.ac.kr | 5, 6 |
| Jeonggyu Kang | 석사과정 | jeonggyumarkk@kaist.ac.kr | 6 |
| Martina Di Paola | 석사과정 | martinadipaola@kaist.ac.kr |  |
| Minju Yoo | 석사과정 | minjuyoo@kaist.ac.kr |  |
| Enrique Jose Delgado Garcia | 학부 인턴 | enrdel070504@kaist.ac.kr |  |
| Jeeyun Choi | 학부 인턴 | jychoi00@kaist.ac.kr |  |
| Junyeop Lee | 학부 인턴 | leejunyeop@kaist.ac.kr |  |
| Soyeon Choi | 학부 인턴 |  |  |
| Yoonseo Choi | Affiliated Member |  |  |

## 졸업생과 이전 구성원

2026년 10월 27일 Members 페이지 Alumni 구역의 22명이다. Master’s Student 4명, Visiting Researcher 3명, Undergraduate Interns 15명으로 나뉜다. 괄호 안은 졸업 연도가 아니라 연구실이 적은 참여 기간이며, 소속·진로는 같은 페이지의 표기다.[^team]

| 이름 | 학위·과정 (연도) | 랩이 적은 소속·진로 |
|---|---|---|
| Jeanne Choi | Master’s Student (Spring 2024 - Spring 2026) | Now Ph.D. student @ Northwestern University |
| Jonghyun Jee | Master’s Student (Fall 2023 - Spring 2025) | Now Ph.D. student @ Northwestern University |
| Yoojin Hong | Master’s Student (Fall 2023 - Fall 2025) | Now working @ Celine |
| Yubin Choi | Master’s Student (Spring 2024 - Spring 2025) | Now Ph.D. student @ University of Michigan |
| Albert Kim | Visiting Researcher (Summer 2024) | Arizona State University |
| HwiJoon Lee | Visiting Researcher (Summer 2025) | Northeastern University |
| Nicholas Chew | Visiting Researcher (Summer 2024 - Fall 2024) | University of Waterloo |
| Adelia Putri | Undergraduate Interns (Fall 2025 - Winter 2025) |  |
| Alisher Ortikov | Undergraduate Interns (Winter 2025 - Spring 2026) | Undergraduate @ KAIST |
| Aribah Aizaz | Undergraduate Interns (Fall 2024 - Fall 2025) | Undergraduate @ KAIST |
| Bich Ngoc Doan | Undergraduate Interns (Winter 2024 - Fall 2024) | KAIST; Now Master's student @ EPFL |
| Dongjae Kang | Undergraduate Interns (Summer 2024 - Summer 2025) | KAIST; Now Master's student @ Columbia University |
| Jaywoong Jeong | Undergraduate Interns (Summer 2025) | Undergraduate @ KAIST |
| Jihoon Kang | Undergraduate Interns (Fall 2025) | Undergraduate @ KAIST |
| Mahnoor Shafiq | Undergraduate Interns (Winter 2025 - Spring 2025) | Undergraduate @ KAIST |
| Mai Nguyen | Undergraduate Interns (Winter 2025 - Spring 2025) | Undergraduate @ KAIST |
| Nguyen Quang Huy | Undergraduate Interns (Summer 2025) | Vietnam National University |
| Saetbyeol Leeyouk | Undergraduate Interns (Winter 2025) | Sogang University; Now Master's student @ MIT |
| Sejong Kim | Undergraduate Interns (Winter 2025 - Spring 2025) | Undergraduate @ KAIST |
| Sejun Jung | Undergraduate Interns (Winter 2025 - Spring 2025) | Undergraduate @ KAIST |
| Yersultan Doszhan | Undergraduate Interns (Summer 2024) | Undergraduate @ KAIST |
| Yujeong Han | Undergraduate Interns (Winter 2025 - Spring 2025) | Undergraduate @ KAIST |

## 최근 논문 목록 (2021–2026)

온라인 공동체의 운영·안전, 협업과 대화, 사회적 AI를 다룬다. 연구실 Research 페이지의 2021–2026년 목록 가운데 Joseph Seering이 저자인 20편으로, 2023년 8월 1일 KAIST 부임 전의 연구도 포함한다.[^research][^appointment] 제목·저자·발표처는 연구실 표기이며 별표는 연구실이 동등 기여로 밝힌 표시다. 연구실이 Workshop으로 분류한 Accuracy, Diversity, and Reflection 및 SLALOM과, Book Chapter로 분류한 Trust and Safety Tooling도 포함한다. TIDES는 COLM 2026 채택으로 표시했다.[^research][^p6]

**2026**

- Heechan Lee\*, Jeonggyu Kang\*, Junho Myung, Jaywoong Jeong, Juho Kim, Joseph Seering. "TIDES: A Longitudinal Bilingual Dataset for Modeling Multi-Party Social Dynamics". *The Third Annual Conference on Language Modelling (COLM 2026) (채택)*.
- Jeanne Choi, Dasom Choi, Sejun Jeong, Hwajung Hong, Joseph Seering. "Situating the Development of Conversational Artificial Intelligence in the Social and Structural Contexts of People with Visual Impairments". *Proceedings of the 2026 ACM Designing Interactive Systems Conference*.
- Heechan Lee, Joseph Seering. "Accuracy, Diversity, and Reflection: Purpose-driven Evaluation for Social Simulation". *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*.
- Juhoon Lee, Joseph Seering. "SLALOM: Simulation Lifecycle Analysis via Longitudinal Observation Metrics for Social Simulation". *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*.
- Yoojin Hong, Yersultan Doszhan, Joseph Seering. "Fostering Collective Discourse: A Distributed Role-Based Approach to Online News Commenting". *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*.
- Tae Soo Kim\*, Heechan Lee\*, Yoonjoo Lee, Joseph Seering, Juho Kim. "Evalet: Evaluating Large Language Models through Functional Fragmentation". *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*.
- Saetbyeol LeeYouk, Joseph Seering. "Deepfake, Real Harm: A Participatory Approach for Imagining Infrastructures to Combat Deepfake Sexual Abuse". *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*.

**2025**

- Subin Park, Jeonghyun Kim, Jeanne Choi, Joseph Seering, Uichin Lee, Sung-Ju Lee. "HateBuffer: Safeguarding Content Moderators' Mental Well-Being through Hate Speech Content Modification". *Proceedings of the ACM on Human-Computer Interaction*. <https://doi.org/10.1145/3757609>.
- Juhoon Lee, Bich Ngoc (Rubi) Doan, Jonghyun Jee, Joseph Seering. "Mapping Community Appeals Systems: Lessons for Community-led Moderation in Multi-Level Governance". *Proceedings of the ACM on Human-Computer Interaction*.
- Joseph Seering, Braahmi Padmakumar, Martina Di Paola. "Trust and Safety Tooling as a User Experience Challenge". *Trust, Safety, and the Internet We Share: Multistakeholder Insights*.
- Jina Yoon, Amy X. Zhang, Joseph Seering. ""It's Great Because It's Ran By Us": Empowering Teen Volunteer Discord Moderators to Design Healthy and Engaging Youth-Led Online Communities". *Proceedings of the ACM on Human-Computer Interaction*.
- Bich Ngoc (Rubi) Doan, Joseph Seering. "The Design Space for Online Restorative Justice Tools: A Case Study with ApoloBot". *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*.
- Juhoon Lee, Seoyoung Kim, Yeon Su Park, Juho Kim, Jeong-woo Jang, Joseph Seering. "Less Talk, More Trust: Understanding Players' In-game Assessment of Communication Processes in League of Legends". *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*.
- Yubin Choi, Jeanne Choi, Joseph Seering. "Leveling Up Together: Fostering Positive Growth and Safe Online Spaces for Teen Roblox Developers". *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*.

**2024**

- Joseph Seering, Manas Khadka, Nava Haghighi, Tanya Yang, Zachary Xi, Michael Bernstein. "Chillbot: Content Moderation in the Backchannel". *Proceedings of the ACM on Human-Computer Interaction*.

**2023**

- Catherine Han, Joseph Seering, Deepak Kumar, Jeffrey T. Hancock, Zakir Durumeric. "Hate Raids on Twitch: Echoes of the Past, New Modalities, and Implications for Platform Governance". *Proceedings of the ACM on Human-Computer Interaction*.

**2022**

- Joseph Seering, Sanjay R. Kairam. "Who Moderates on Twitch and What Do They Do?". *Proceedings of the ACM on Human-Computer Interaction*.
- Joon Sung Park, Joseph Seering, Michael S. Bernstein. "Measuring the Prevalence of Anti-Social Behavior in Online Communities". *Proceedings of the ACM on Human-Computer Interaction*.
- Joseph Seering, Brianna Dym, Geoff Kaufman, Michael Bernstein. "Pride and Professionalization in Volunteer Moderation: Lessons for Effective Platform-User Collaboration". *Journal of Online Trust and Safety*.

**2021**

- Soomin Kim, Jinsu Eun, Joseph Seering, Joonhwan Lee. "Moderator Chatbot for Deliberative Discussion". *Proceedings of the ACM on Human-Computer Interaction*.

## 수상

학과가 전한 수상 가운데 시기를 확인할 수 있는 2023년 항목이다. 괄호의 날짜는 학회 개최 기간이다.[^award]

- 2023 (학회 기간 10월 14–18일) · Joseph Seering과 Stanford University 공동연구진의 Hate Raids on Twitch 논문, ACM CSCW Best Paper Award 수상

## 소식

연구실 News 페이지의 2025년 연구 성과 소식이다. 두 글 모두 월·일 표기가 없다.[^news]

- 2025 (월·일 표기 없음) · CHI 2025에 정규 논문 3편 채택: Leveling Up Together, The Design Space for Online Restorative Justice Tools, Less Talk, More Trust
- 2025 (월·일 표기 없음) · CSCW 2025에 Mapping Community Appeals Systems 논문 채택

## 연락과 위치

- 연구실: KAIST N1 Kim Beang-Ho Kim Sam-Youl ITC Building 623호, 대전광역시 유성구 대학로 291[^home][^team]
- 교수 연구실: N1 604호[^lab][^faculty]
- 교수 이메일: seering@kaist.ac.kr[^team]
- 교수 전화: 042-350-3589[^lab]
[^home]: CSTL, 첫 화면의 연구실 소개와 위치. <https://cstlab.org/> 관측 2026-10-27.
[^lab]: KAIST 전산학부, 협동 사회 기술 연구실 소개. <https://cs.kaist.ac.kr/research/labView?sn=120&menu=64> 관측 2026-10-27.
[^roster]: KAIST 전산학부, 교수진 명단의 시어링 조셉 항목. <https://cs.kaist.ac.kr/people/faculty> 관측 2026-10-27.
[^faculty]: KAIST 전산학부, 시어링 조셉 교수 소개. <https://cs.kaist.ac.kr/people/view?idx=634&kind=faculty&menu=160> 관측 2026-10-27.
[^appointment]: KAIST 전산학부, 교수 소식의 「시어링 조셉 교수 임용안내」, 2023-08-01 부임. <https://cs.kaist.ac.kr/spotlights/faculty?menu=&page=3> 관측 2026-10-27.
[^research]: CSTL, Research의 Recent Works from Lab Members, 2021–2026년. <https://cstlab.org/research/> 관측 2026-10-27.
[^team]: CSTL, Members의 Faculty·Graduate Students·Undergraduate Interns·Affiliated Members·Alumni. <https://cstlab.org/team/> 관측 2026-10-27.
[^news]: CSTL, News의 2025년 CHI·CSCW 논문 채택 소식. <https://cstlab.org/news/> 관측 2026-10-27.
[^award]: KAIST 전산학부, 교수 소식의 「KAIST Professor Joseph Seering wins Best Paper Award」 항목. 학회 개최 기간 2023-10-14–18. <https://cs.kaist.ac.kr/spotlights/faculty?menu=&page=3> 관측 2026-10-27.
[^hatebuffer]: S. Park 외, J. Seering, Proceedings of the ACM on Human-Computer Interaction. <https://doi.org/10.1145/3757609> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=HateBuffer%3A%20Safeguarding%20Content%20Moderators%27%20Mental%20Well-Being%20through%20Hate%20Speech%20Content%20Modification> 관측일 2026-10-28.
[^p1]: B. N. Doan, J. Seering, arXiv (온라인 2025-02-26). <https://doi.org/10.48550/arXiv.2502.18861> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2502.18861>. arXiv 최초 제출일을 온라인 날짜로 적었으며, 읽은 판은 v1이다. 관측 2026-10-27.
[^p2]: Y. Choi, J. Choi, J. Seering, arXiv (온라인 2025-02-25). <https://doi.org/10.48550/arXiv.2502.18120> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2502.18120>. arXiv 최초 제출일을 온라인 날짜로 적었으며, 읽은 판은 v1이다. 관측 2026-10-27.
[^p3]: J. Lee 외, J. Seering, arXiv (온라인 2025-02-25). <https://doi.org/10.48550/arXiv.2502.17935> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2502.17935>. arXiv 최초 제출일을 온라인 날짜로 적었으며, 읽은 판은 v1이다. 관측 2026-10-27.
[^p4]: Y. Hong, Y. Doszhan, J. Seering, arXiv (온라인 2025-10-03). <https://doi.org/10.48550/arXiv.2510.02766> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2510.02766>. arXiv 최초 제출일을 온라인 날짜로 적었으며, 읽은 판은 v2, 2026-02-12이다. 관측 2026-10-27.
[^p5]: T. S. Kim 외, J. Kim, arXiv (온라인 2025-09-14). <https://doi.org/10.48550/arXiv.2509.11206> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2509.11206>. arXiv 최초 제출일을 온라인 날짜로 적었으며, 읽은 판은 v4, 2026-04-20이다. 관측 2026-10-27.
[^p6]: H. Lee 외, J. Seering, arXiv (온라인 2026-08-03). <https://doi.org/10.48550/arXiv.2608.01724> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2608.01724>. arXiv 최초 제출일을 온라인 날짜로 적었으며, 읽은 판은 v1이다. 관측 2026-10-27.

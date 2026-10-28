# 인터랙션 연구실 (KAIST Interaction Lab, KIXLAB)

**KAIST 전산학부 · 김주호 부교수**

- 분야: 인간–컴퓨터 상호작용, 인간-AI 상호작용, 온라인 학습과 협업, 창작 지원, 정보 탐색과 의사결정
- 대분야: 컴퓨팅·AI
- 태그: 인간–컴퓨터 상호작용[^home][^lab][^p8], 대형 언어 모델[^p1][^p2][^p3], 추천 시스템[^p6]
- 홈페이지: <https://www.kixlab.org/>
- 근거와 출처: [인터랙션 연구실 근거 페이지](kixlab-sources.md)

> 사람들이 온라인에서 배우고 협업하며 판단하는 과정을 돕는 시스템을 설계하고, 사람의 의도와 생각을 AI에 전달하는 방법을 연구하는 연구실이다.[^home][^p1][^p2]

## 무엇을 연구하나

KIXLAB은 KAIST 전산학부의 인간–컴퓨터 상호작용(Human-Computer Interaction, HCI: 사람과 컴퓨터가 정보를 주고받는 방식과 사용자 경험을 설계·평가하는 분야) 연구실이다. 온라인에서 사람들이 배우고, 협업하고, 토론하고, 의사결정을 내리고, 함께 행동하는 과정을 돕는 시스템을 만든다. 학과 소개는 크라우드소싱(여러 사람에게 공개적으로 참여를 요청해 과제를 수행하거나 자료를 모으는 방식), 온라인 교육, 시민 참여, 집단 의사결정, 상호작용을 통한 데이터 분석을 세부 연구로 든다.[^home][^lab]

최근 연구의 한 갈래는 **사람의 생각과 의도를 AI가 다루도록 하는 상호작용**이다. 대형 언어 모델(Large Language Model, LLM: 많은 글에서 언어의 패턴을 배워 글을 이해하고 생성하는 인공지능 모델)을 쓰는 작업에서, 사용자가 작업 도중 떠올린 생각을 어떻게 남기고 AI에 전달할지 다룬다. Contexty는 사용자가 짧은 메모를 모으고 검토·수정하면서 AI에 제공할 작업 맥락을 구성하게 한다. EvalLM은 프롬프트(AI가 결과를 만들도록 주는 지시나 입력)를 수정하는 사람에게 평가 도구를 제공한다. 사용자가 자연어(사람이 일상에서 사용하는 말과 글)로 평가 기준을 정하면 여러 생성 결과를 검토하고 수정 방향을 찾도록 돕는다.[^p1][^p2]

둘째 갈래는 **교육 도구와 영상 학습 환경을 설계하는 일**이다. TeachTune에서는 교사가 학생의 지식과 동기 특성을 지정하고, 그 특성을 모의하는 학생과 교육용 대화 도구의 대화를 관찰하며 도구를 점검한다. TeachYou에서는 학습자가 AI에게 알고리즘(문제를 해결하기 위한 절차)을 가르치며 배운다. 이때 AI가 모르는 내용이나 잘못 알고 있는 내용을 지정하고, AI가 왜 또는 어떻게라는 질문을 하게 해 학습자의 설명을 이끌어 낸다.[^p3][^p4] 수술 영상 학습을 위한 Surch는 사용자 인터페이스(사람이 시스템을 조작하고 결과를 확인하는 접점)를 설계한 연구다. 수술의 단계와 순서로 영상을 검색하고, 같은 단계에 맞춰 여러 영상을 비교하도록 한다. 앞선 시제품 연구에서도 영상의 구조 정보를 이용한 검색과 영상 간 재생 동기화(여러 영상의 진행을 서로 맞추는 기능)를 제안했다.[^p8][^surchearly]

셋째 갈래는 **창작과 정보 탐색을 돕는 도구**다. CreativeConnect는 참고 이미지에서 개념을 키워드로 찾아내고, 사용자가 선택한 키워드를 재조합한 아이디어를 그림 초안과 글로 제시한다. PaperWeaver는 추천 시스템(사용자의 기록과 항목 정보를 바탕으로 관심을 가질 만한 항목을 골라 제시하는 시스템)이 알려 주는 새 논문을 사용자가 모아 둔 논문과 연결해 설명한다. 사용자의 논문 수집 기록에서 관심사를 추론하고, 그 맥락에 맞는 관점으로 기존 논문과 추천 논문을 비교한다. 서로 다른 AI 답변을 접할 때 사람이 정보를 어떻게 이해하는지도 살핀다. One vs. Many는 여러 답변의 불일치가 AI 능력에 대한 평가와 정보 이해에 미치는 영향을 연구했다.[^p5][^p6][^p7] ReviewAid는 비전문가가 건강 뉴스를 평가하도록 돕는 웹 인터페이스다. 보도의 품질과 과학 연구 결과의 품질을 나누어 살피도록 안내하고, 평가 기준별 예시 의견을 제공한다.[^reviewaid]

## 주요 연구 주제

### 1. 작업 맥락과 사용자 기준을 반영하는 AI

작업 중 생각을 기록하고 사용자가 AI에 제공할 맥락을 직접 검토하는 도구, 사용자가 정한 기준으로 여러 AI 결과를 평가하는 도구를 설계한다. 사용자에게 작업의 통제권을 주는 상호작용과 반복적인 지시문 수정을 함께 다룬다.[^p1][^p2]

### 2. 교사·학습자를 위한 대화와 영상 도구

학생의 특성을 모의하는 대화를 통해 교사가 교육용 AI를 점검하게 하고, 학습자가 AI에게 설명하고 질문에 답하면서 알고리즘을 배우는 환경을 만든다. 교육용 AI의 학생 대응 방식과 학습 과정에 개입하는 질문을 연구한다.[^p3][^p4] 수술 영상에서는 절차의 단계와 순서를 이용해 검색·비교하는 시스템과 시제품을 설계한다.[^p8][^surchearly]

### 3. 참고 자료의 재조합과 창작 지원

생성형 AI(글이나 이미지 등 새로운 콘텐츠를 생성하는 인공지능)를 활용해 참고 이미지의 개념을 찾고 재조합한다. 디자이너가 선택한 키워드로 아이디어를 탐색하고 그림 초안과 설명을 확인하는 과정을 지원한다.[^p5]

### 4. 논문 탐색과 AI 정보의 비판적 이해

사용자가 모아 둔 논문을 바탕으로 추천 논문의 관련성을 설명하고, 서로 상충할 수 있는 AI 답변을 읽는 사람의 이해와 판단을 살핀다. 연구자의 정보 선별과 AI 결과의 한계를 드러내는 설계를 다룬다.[^p6][^p7] 건강 뉴스에서는 비전문가가 평가 기준을 기사에 적용하도록 안내와 예시 의견을 제공하는 인터페이스를 설계한다.[^reviewaid]

## 대표 논문

2021–2026년 논문 가운데 김주호 교수가 저자로 참여하고, 연구 갈래를 고르게 보여 주는 8편을 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다. 초록의 출처와 판본은 각주에 적었으며, Contexty의 학회 표기는 연구실 소식의 채택 기록을 따른다.

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 김주호 교수의 저자 위치 |
|---|---|---|---|---|
| 1 | 2026 | [Contexty: Capturing and Organizing In-situ Thoughts for Context-Aware AI Support](https://arxiv.org/abs/2604.11067) · UIST 2026 (채택) | 복잡한 작업 중 떠오르는 생각은 흩어지기 쉽고 AI에 전달하기 어렵다. 짧은 메모를 작업 중 남기고, 그 메모에 담긴 생각을 사용자가 검토·수정해 AI의 작업 맥락으로 쓰게 했다. 평가에서는 작업에 대한 인식, 생각의 구조화, 사용자의 저작 주도감과 통제감이 향상됐다고 보고했다.[^p1] | 마지막 저자 |
| 2 | 2024 | [EvalLM: Interactive Evaluation of Large Language Model Prompts on User-Defined Criteria](https://doi.org/10.1145/3613904.3642216) · CHI 2024 | AI용 지시문을 고칠 때 여러 결과를 읽으며 무엇이 문제인지 평가해야 한다. 사용자가 말과 글로 평가 기준을 정하면 언어 모델이 여러 결과를 그 기준으로 평가하고, 지시문을 개선할 단서를 제공하게 했다. 비교 연구에서는 평가 기준의 다양성, 검토한 결과의 수, 만족할 지시문에 도달하기까지의 수정 횟수에서 개선을 보고했다.[^p2] | 마지막 저자 |
| 3 | 2025 | [TeachTune: Reviewing Pedagogical Agents Against Diverse Student Profiles with Simulated Students](https://doi.org/10.1145/3706598.3714054) · CHI 2025 | 학생마다 아는 내용과 학습 동기가 달라 교육용 AI도 다양한 학생에게 맞는지 점검해야 한다. 교사가 학생 특성을 정하고 그 특성을 모의하는 AI와 교육용 AI의 자동 대화를 보며 점검하는 도구를 만들었다. 교사 평가에서는 작업 부담이 낮아지고 점검한 학생 특성의 범위가 넓어졌다고 보고했다.[^p3] | 마지막 저자 |
| 4 | 2024 | [Teach AI How to Code: Using Large Language Models as Teachable Agents for Programming Education](https://doi.org/10.1145/3613904.3642349) · CHI 2024 | 학습자가 AI에게 설명하며 프로그래밍을 배우는 환경 TeachYou를 만들었다. 학생 역할의 AI가 아는 내용과 오개념을 지정하고 왜 또는 어떻게라는 질문을 하게 했다. 기술 평가에서는 AI의 문제 해결 수준을 조절할 수 있었고, 초보 학습자 연구에서는 AI의 질문이 지식 내용을 담은 대화를 이끌어 냈다고 보고했다.[^p4] | 마지막 저자 |
| 5 | 2024 | [CreativeConnect: Supporting Reference Recombination for Graphic Design Ideation with Generative AI](https://doi.org/10.1145/3613904.3642794) · CHI 2024 | 디자이너가 참고 이미지를 보고 개념을 골라 새 아이디어로 조합하는 일을 돕는다. 이미지에서 키워드를 찾고 관련 키워드를 추천하며, 사용자가 고른 개념들의 조합을 그림 초안과 설명으로 보여 줬다. 사용자 연구에서는 아이디어의 수와 스스로 평가한 창의성이 기준 도구를 쓸 때보다 높았다고 보고했다.[^p5] | 마지막 저자 |
| 6 | 2024 | [PaperWeaver: Enriching Topical Paper Alerts by Contextualizing Recommended Papers with User-collected Papers](https://doi.org/10.1145/3613904.3642196) · CHI 2024 | 새 논문 알림의 제목과 초록만으로는 자기 연구와의 관계를 판단하기 어렵다. 사용자가 수집한 논문으로 관심사를 추론하고, 추천 논문과 기존 논문을 관련 관점에서 비교해 설명하는 도구를 만들었다. 사용자 연구에서는 추천 논문의 관련성을 이해하고 선별하는 데 도움이 됐다고 보고했다.[^p6] | 공저자 |
| 7 | 2024 | [One vs. Many: Comprehending Accurate Information from Multiple Erroneous and Inconsistent AI Generations](https://doi.org/10.1145/3630106.3662681) · FAccT 2024 | 같은 질문에 AI가 서로 다른 답을 내면 사람이 무엇을 믿고 이해하는지 살폈다. 여러 답변의 불일치는 참가자가 평가한 AI의 능력을 낮췄지만, 주어진 정보에 대한 이해는 높였다. 결과를 바탕으로 AI 답변의 불일치를 드러내 모델의 한계를 알리고 비판적 사용을 돕는 설계를 논의했다.[^p7] | 마지막 저자 |
| 8 | 2023 | [Surch: Enabling Structural Search and Comparison for Surgical Videos](https://doi.org/10.1145/3544548.3580772) · CHI 2023 | 수술 영상에서 단계의 구성과 순서를 파악하고 여러 영상을 비교하기는 어렵다. 절차의 구조를 표현한 그림으로 영상을 검색하고, 같은 수술 단계에 맞춰 여러 영상을 탐색하는 시스템을 만들었다. 평가에서는 절차를 묶는 방법의 효과와 해석 가능성을 확인했고, 사용자의 영상 검색·비교 경험과 과제 수행 효율이 개선됐다고 보고했다.[^p8] | 마지막 저자 |

## 교수와 전문 분야

김주호는 KAIST 전산학부 부교수다. 학과 교수 명단은 인간-컴퓨터 상호작용, 인간-AI 상호작용, 소셜 컴퓨팅(사람 사이의 소통과 사회적 활동을 다루는 컴퓨팅), 크라우드소싱, 온라인 교육을 전문 분야로 적는다. 랩 People 페이지의 영문 직위는 Associate Professor다.[^faculty][^people]

대표 논문에서 드러나는 전문성은 사람의 의도와 평가 기준을 AI 도구에 반영하는 상호작용 설계, 교사와 학습자를 위한 AI 학습 환경과 영상 검색·비교, 디자인 아이디어 생성, 연구 정보 탐색과 AI 답변의 해석이다. 실용 도구를 구현하고 사람이 그 도구를 사용하며 보이는 이해와 행동을 평가하는 연구를 함께 수행한다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

교육에서는 교사가 만든 AI 대화 도구의 검토와 알고리즘 학습, 창작에서는 그래픽 디자인 아이디어 탐색, 연구 활동에서는 새 논문 선별을 지원한다. 온라인 정보 이용에서는 여러 AI 답변의 불일치를 사용자가 이해하도록 하는 설계를 다룬다. 학과 소개는 온라인 협업과 학습, 시민 참여와 집단 의사결정도 연구의 활용 방향으로 밝힌다.[^p3][^p4][^p5][^p6][^p7][^lab] 의료 교육에서는 수술 영상을 구조에 따라 검색·비교하게 하고, 건강 뉴스 이용에서는 비전문가의 정보 평가 과정을 지원한다.[^p8][^surchearly][^reviewaid]

## 구성원

2026년 10월 28일 People 페이지 기준으로 박사후연구원 1명, 박사과정 10명, 석사과정 8명, 방문 연구자 2명, 인턴 15명이다. 과정과 소속 표기는 랩 게시 내용이고 학교 이메일을 함께 적었다.[^people] "대표 논문 참여"는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 | 랩이 적은 소속 |
|---|---|---|---|---|
| Zheng Wei | 박사후연구원 |  |  |  |
| DaEun Choi | 박사과정 | daeun.choi@kaist.ac.kr | 5, 8 |  |
| Yoonseo Choi | 박사과정 |  |  |  |
| Hyehyun Chu | 박사과정 | hyenchu@kaist.ac.kr |  |  |
| Kyungyoon Jung | 박사과정 | juliecandoit98@kaist.ac.kr |  |  |
| Yoonsu Kim | 박사과정 | yoonsu16@kaist.ac.kr | 1 |  |
| Junho Myung | 박사과정 | junho00211@kaist.ac.kr |  |  |
| Yeon Su Park | 박사과정 | yeonsupark@kaist.ac.kr |  |  |
| Kihoon Son | 박사과정 | kihoon.son@kaist.ac.kr | 1, 7 |  |
| Bekzat Tilekbay | 박사과정 |  |  |  |
| Jenny Yang | 박사과정 | jenny_yang@kaist.ac.kr |  |  |
| Nadia Arvi | 석사과정 | nadia.arvi@kaist.ac.kr |  |  |
| Eunhye Kim | 석사과정 | gracekim027@kaist.ac.kr |  |  |
| Sean Kim | 석사과정 | kimsean@kaist.ac.kr |  |  |
| Heechan Lee | 석사과정 | hclee99@kaist.ac.kr |  |  |
| Sehoon Lim | 석사과정 | sehoon1106@kaist.ac.kr |  |  |
| Junmin Park | 석사과정 | deanvilgel21@kaist.ac.kr |  |  |
| Minju Yoo | 석사과정 |  | 3 |  |
| Jaesang Yu | 석사과정 |  |  |  |
| Seongeun Jeon | 방문 연구원 |  |  |  |
| Daeseok Jeong | 방문 연구원 |  |  |  |
| Yumi Cho | 인턴 |  |  | CNU |
| Yuxuan Guo | 인턴 |  |  | UoE |
| Candace Hunzwi | 인턴 |  |  | CMU |
| Gahyun Kim | 인턴 |  |  | SKKU |
| Hyunmin Kim | 인턴 |  |  | KAIST |
| Jey Kim | 인턴 |  |  | SKKU |
| NamHee Kim | 인턴 |  |  | SNU |
| Yoonseo Kim | 인턴 |  |  | KAIST |
| Jaeyoung Kwon | 인턴 |  |  | SNU |
| Chaeyeon Lee | 인턴 |  |  | Ewha |
| Sumin Lee | 인턴 |  |  | SNU |
| Alex Noh | 인턴 |  |  | SFU |
| Chanyoung Park | 인턴 |  |  | SNU |
| Jiyeon Park | 인턴 | jeeyeon513@kaist.ac.kr |  | KAIST |
| Junyoung Park | 인턴 |  |  | SNU |

## 졸업생과 이전 구성원

2026년 10월 28일 People 페이지 Alumni의 187개 항목이다. Ph.D. / Postdoc 12개, M.S. Student 16개, Past Researcher 30개, Intern 129개로 나뉜다. 게시된 재직·참여 기간은 2016–2026년에 걸쳐 있고, 같은 이름이 다른 구획에 반복될 수 있다. 진로와 당시 소속, 학위 논문 링크의 이름은 랩 표기다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 | 당시 소속 |
|---|---|---|---|---|
| Hyunwoo Kim | Ph.D. (Spring 2017  - Summer 2026) | Senior Engineer at Samsung SDS | Ph.D. Thesis; M.S. Thesis |  |
| Seungju Kim | Postdoc (Fall 2024  - Spring 2026) | Researcher at the Korea Institute for Curriculum and Evaluation |  |  |
| Tae Soo Kim | Ph.D. (Winter 2017  - Winter 2026) | Postdoc Researcher at SkillBench | Ph.D. Thesis; M.S. Thesis |  |
| Eunyoung Ko | Ph.D. (Spring 2017  - Winter 2026) | Applied Scientist at SkillBench | Ph.D. Thesis |  |
| Hyungyu Shin | Ph.D. (Summer 2016  - Winter 2026) | CTO at AlgorithmLabs | M.S. Thesis |  |
| Saelyne Yang | Ph.D. (Summer 2018  - Winter 2026) | Postdoc Researcher at CMU | Ph.D. Thesis; M.S. Thesis |  |
| Yoonjoo Lee | Ph.D. (Spring 2020  - Summer 2025) | Postdoc Researcher at University of Michigan | Ph.D. Thesis |  |
| Dae Hyun Kim | Postdoc (Spring 2022  - Winter 2025) | Assistant Professor at Yonsei University |  |  |
| Seoyoung Kim | Ph.D. (Summer 2017  - Winter 2025) |  | Ph.D. Thesis; M.S. Thesis |  |
| Meng Xia | Postdoc (Winter 2021  - Fall 2021) | Assistant Professor at TAMU |  |  |
| Jean Young Song | Postdoc (Winter 2016  - Spring 2021) | Assistant Professor at Yonsei University |  |  |
| Minsuk Chang | Ph.D. (Summer 2016  - Winter 2021) | Research Scientist at Google Deepmind | Ph.D. Thesis |  |
| Daeheon Jeong | M.S. Student (Fall 2024  - Summer 2026) | Applied Scientist at SkillBench | M.S. Thesis |  |
| Hyoungwook Jin | M.S. Student (Winter 2018  - Summer 2025) | Ph.D. Student at University of Michigan | M.S. Thesis |  |
| Alex Suryapranata | M.S. Student (Fall 2022  - Summer 2025) | AI Software Developer at UTHealth Houston | M.S. Thesis |  |
| Jihyeong Hong | M.S. Student (Spring 2023  - Winter 2025) | Tech Manager at Naver | M.S. Thesis |  |
| Seulgi Choi | M.S. Student (Winter 2022  - Summer 2024) | IT Planning Specialist at Kakao Bank | M.S. Thesis |  |
| Juhoon Lee | M.S. Student (Spring 2022  - Winter 2024) | Ph.D. Student at CSTL KAIST | M.S. Thesis |  |
| Jeongeon Park | M.S. Student (Fall 2019  - Summer 2023) | Ph.D. Student at UC San Diego | M.S. Thesis |  |
| Haesoo Kim | M.S. Student (Summer 2019  - Winter 2023) | Ph.D. Student at Cornell University | M.S. Thesis |  |
| Jeongyeon Kim | M.S. Student (Summer 2019  - Winter 2022) | Ph.D. Student at Stanford University | M.S. Thesis |  |
| Kabdo Choi | M.S. Student (Spring 2019  - Summer 2021) | Software Engineer at Moloco | M.S. Thesis |  |
| Donghoon Han | M.S. Student (Summer 2018  - Winter 2021) | ML Engineer at Branch and Bound (CodeTree) | M.S. Thesis |  |
| Kyung Je Jo | M.S. Student (Spring 2018  - Winter 2021) | Software Engineer at Meta | M.S. Thesis |  |
| Jibon Naher | M.S. Student (Fall 2018  - Summer 2020) |  | M.S. Thesis |  |
| Mathias Sixten Pedersen | M.S. Student (Winter 2019  - Spring 2019) | Co-founder and CTO at NordInsight | M.S. Thesis |  |
| Hyeungshik Jung | M.S. Student (Summer 2016  - Winter 2019) | Software Engineer at Coupang | M.S. Thesis |  |
| Paul Grau | M.S. Student (Fall 2016  - Spring 2018) | Lead Frontend Engineer at Alvin | M.S. Thesis |  |
| Jiho Kim | Past Researcher (Fall 2025  - Summer 2026) | M.S. Student at Columbia University |  | SNU |
| Diana Kozachek | Past Researcher (Summer 2026) |  |  | University of St. Gallen |
| Oshan Mudannayake | Past Researcher (Summer 2026) |  |  | University of Moratuwa |
| Jihoon Chae | Past Researcher (Winter 2026  - Spring 2026) |  |  |  |
| Shujun Ju | Past Researcher (Summer 2025  - Spring 2026) |  |  | PolyU_HK |
| Thiemo Wambsganss | Past Researcher (Spring 2026) |  |  | Bern University of Applied Sciences |
| Sung-Chul Lee | Past Researcher (Summer 2016  - Winter 2026) |  |  |  |
| Emircan Gundogdu | Past Researcher (Summer 2025) |  |  | ETH Zurich |
| Chen Zhou | Past Researcher (Winter 2025  - Summer 2025) |  |  | NUS |
| Yu-Kai Hung | Past Researcher (Winter 2025  - Spring 2025) |  |  | National Taiwan University |
| Eunjoo Kim | Past Researcher (Fall 2024  - Winter 2025) |  |  | Yonsei University College of Medicine |
| Jiangnan Xu | Past Researcher (Winter 2024  - Fall 2024) |  |  | RIT |
| Vedad Misirlić | Past Researcher (Summer 2024) |  |  | Graz University of Technology |
| Sahar Admoni | Past Researcher (Winter 2024) |  |  | Technion |
| Haechan Kim | Past Researcher (Spring 2023  - Winter 2024) |  |  | Ringle |
| Yuewen Yang | Past Researcher (Winter 2024) |  |  | Cornell Tech |
| Gionnieve Lim | Past Researcher (Winter 2023  - Summer 2023) | Ph.D. Student at SUTD |  | SUTD |
| Hyung-Kwon Ko | Past Researcher (Summer 2022  - Fall 2022) | Ph.D. Student at Stanford University |  |  |
| Eun Jeong Kang | Past Researcher (Summer 2020  - Winter 2022) | Ph.D. Student at Cornell University |  | Sogang University |
| Mina Huh | Past Researcher (Winter 2020  - Summer 2021) | Ph.D. Student at University of Texas, Austin |  |  |
| Taewook Kim | Past Researcher (Summer 2020  - Summer 2021) | Ph.D. Student at Northwestern University |  |  |
| Jisoo Lee | Past Researcher (Summer 2019  - Spring 2020) | Co-founder at Beeble |  |  |
| Toni-Jan Keith Monserrat | Past Researcher (Summer 2019) | Ph.D. Researcher at UPLB |  | UPLB |
| Evey Huang | Past Researcher (Summer 2018  - Spring 2019) | Ph.D. Student at Northwestern University |  |  |
| Arti Thakur | Past Researcher (Fall 2017  - Spring 2019) | Ph.D. Student at UC Davis |  |  |
| Yi-Ching (Janet) Huang | Past Researcher (Summer 2018  - Fall 2018) | Assistant Professor at Eindhoven University of Technology |  |  |
| Simon Perrault | Past Researcher (Summer 2018  - Fall 2018) | Assistant Professor at Télécom Paris |  | SUTD |
| Ray Hong | Past Researcher (Summer 2017  - Summer 2018) | Assistant Professor at George Mason University |  | UW |
| John Joon Young Chung | Past Researcher (Spring 2017  - Spring 2018) | Research Scientist at Midjourney |  |  |
| Mercedes Huertas | Past Researcher (Winter 2018  - Spring 2018) | Ph.D. Researcher at University of Trento |  | University of Trento |
| Yuri Lee | Intern (Winter 2026  - Fall 2026) |  |  | POSTECH |
| Seoyeon Byun | Intern (Winter 2025  - Summer 2026) |  |  | Korea Univ |
| Haeri Lee | Intern (Winter 2026  - Summer 2026) |  |  | KAIST |
| Zeynab Mammar | Intern (Summer 2026) |  |  | Stony Brook University |
| Eugene Choi | Intern (Winter 2026  - Spring 2026) |  |  | SNU |
| Gosu Choi | Intern (Winter 2024  - Spring 2026) |  |  | KAIST |
| Juhyeon Choi | Intern (Winter 2026  - Spring 2026) |  |  | SNU |
| Hayeon Doh | Intern (Summer 2025  - Spring 2026) |  |  | Ewha |
| Hyunseok Hong | Intern (Winter 2026  - Spring 2026) |  |  | KAIST |
| Hyunjung Yi | Intern (Winter 2026  - Spring 2026) |  |  | Korea Univ |
| Mingyu Kim | Intern (Winter 2026) |  |  | UNIST |
| Yoshee Jain | Intern (Summer 2025  - Fall 2025) |  |  | UIUC |
| Daho Jung | Intern (Summer 2025  - Fall 2025) |  |  | KAIST |
| Minbeom Kim | Intern (Summer 2025  - Fall 2025) |  |  | KAIST |
| Chanbin Park | Intern (Summer 2025  - Fall 2025) |  |  | UC Berkeley |
| Samuel Dawit Assefa | Intern (Winter 2025  - Summer 2025) |  |  | KAIST |
| Heejin Bin | Intern (Winter 2025  - Spring 2025) |  |  | KAIST |
| Dong Yun Jung | Intern (Summer 2023  - Spring 2025) |  |  | KAIST |
| Hana Oh | Intern (Winter 2025  - Spring 2025) |  |  | SNU |
| Jingyu Tang | Intern (Winter 2025  - Spring 2025) |  |  | HUST |
| Sadat Shams Chowdhury | Intern (Summer 2024  - Winter 2025) | AI Researcher at Gudo Advisory Co. |  | KAIST |
| Shahnoza Yadgarova | Intern (Winter 2024  - Winter 2025) |  |  | KAIST |
| Haeseul Cha | Intern (Winter 2024  - Fall 2024) |  |  | KAIST |
| Chanyoung Kim | Intern (Winter 2024  - Fall 2024) | Engineer at SkillBench |  | KAIST |
| Nayoung Kim | Intern (Summer 2024  - Fall 2024) |  |  | DGIST |
| Sieun Kim | Intern (Summer 2024  - Fall 2024) | Ph.D. Student at University of Michigan |  | SNU |
| Yoonsang Lee | Intern (Summer 2024  - Fall 2024) | Ph.D. Student at Princeton University |  | SNU |
| Saetbyeol LeeYouk | Intern (Summer 2024  - Fall 2024) | M.S. Student at MIT |  | Sogang |
| Jihyun Yoo | Intern (Summer 2024  - Fall 2024) |  |  | KAIST |
| Brandon Chin | Intern (Summer 2024) |  |  | UC Berkeley |
| Jiho Kim | Intern (Summer 2024) |  |  | Calvin University |
| Yoonah Park | Intern (Winter 2024  - Summer 2024) |  |  | SNU |
| Taehyun Yang | Intern (Winter 2024  - Summer 2024) | Ph.D. Student at University of Maryland |  | SNU |
| Yumin Cho | Intern (Summer 2023  - Spring 2024) |  |  | KAIST |
| Sumin Hong | Intern (Summer 2023  - Winter 2024) | Ph.D. Student at University of Notre Dame |  | Seoultech |
| Jiwon Jang | Intern (Winter 2024) |  |  | SKKU |
| Jinhyeon Kwon | Intern (Winter 2024) |  |  | KAIST |
| Hyewon Lee | Intern (2023 Summer - 2023 Fall / 2025 Summer - 2026 Summer) |  |  | KAIST |
| Jueon Lee | Intern (Summer 2023  - Fall 2023) |  |  | SNU |
| Hai Nam | Intern (Summer 2023  - Fall 2023) |  |  | KAIST |
| Dakyeom Ahn | Intern (Summer 2022  - Summer 2023) |  |  | SNU |
| Jisu Kim | Intern (Winter 2023  - Summer 2023) | M.S. Student at Georgia Tech |  | KAIST |
| Khanh Duy Le | Intern (Summer 2023) | Researcher at HCMUT |  |  |
| Nicole Lee | Intern (Summer 2023) |  |  | KAIST |
| Yokyung Lee | Intern (Summer 2023) |  |  | KAIST |
| Michal Lewkowicz | Intern (Summer 2023) |  |  | Yale |
| Bryan Min | Intern (Summer 2023) | Ph.D. Student at UC San Diego |  | UC San Diego |
| Nathan Mekuria Haile | Intern (Winter 2023  - Spring 2023) |  |  | KAIST |
| Yoojin Hong | Intern (Winter 2022  - Spring 2023) | CRM at Celine |  | KAIST |
| Soyeong Min | Intern (Winter 2023) | M.S. Student at Next Interface Lab, KAIST |  | KAIST |
| Arghya Sarkar | Intern (Winter 2023) |  |  | NYU |
| Seungho Baek | Intern (Fall 2022) | Engineer at SkillBench |  | KAIST |
| Myeongkyun Cho | Intern (Summer 2022) |  |  | KAIST |
| Heeju Choi | Intern (Summer 2022) |  |  | KAIST |
| Sangkyung Kwak | Intern (Summer 2021  - Summer 2022) | M.S. Student at KAIST Graduate School of AI |  | KAIST |
| Honggi Lee | Intern (Summer 2022) |  |  | KAIST |
| Inhwa Song | Intern (Summer 2021  - Summer 2022) | Ph.D. student at Princeton University |  | KAIST |
| Yohan Yun | Intern (Fall 2021  - Summer 2022) | M.S. Student at HCI Lab, KAIST |  | KAIST |
| Subeen Park | Intern (Summer 2021  - Spring 2022) |  |  | SNU |
| Jung In Rhee | Intern (Winter 2022) | M.S. Student at KAIST |  | KAIST |
| JeongYoon Shin | Intern (Winter 2022) |  |  | KAIST |
| Jeanne Choi | Intern (Summer 2021  - Fall 2021) | Ph.D. student in Northwestern University |  | KAIST |
| Mehmet Hamza Erol | Intern (Summer 2021  - Fall 2021) |  |  | KAIST |
| Seokhun Jeong | Intern (Winter 2021  - Fall 2021) |  |  | KAIST |
| Elliot Jung | Intern (Summer 2021  - Fall 2021) | AI Product Manager atStudio XID |  | KAIST |
| Jaeryoung Ka | Intern (Winter 2021  - Fall 2021) |  |  | KAIST |
| Nurlykhan Kopenov | Intern (Summer 2021  - Fall 2021) |  |  | KAIST |
| June Suk Choi | Intern (Summer 2021) |  |  | KAIST |
| Yubin Choi | Intern (Winter 2021  - Summer 2021) | M.S. Student at CSTL KAIST |  | UNIST |
| Euicheon Lee | Intern (Winter 2021  - Summer 2021) |  |  | KAIST |
| Hyerim Lee | Intern (Summer 2020  - Summer 2021) |  |  | KAIST |
| Sanghyeon Lee | Intern (Winter 2021  - Summer 2021) |  |  | KAIST |
| Sangwook Lee | Intern (Fall 2020  - Summer 2021) | Ph.D. Student at Virginia Tech |  | POSTECH |
| Seong Hee Lee | Intern (Summer 2021) | M.S. Student at Stanford University |  | Cornell University |
| Nabila Sindi Listyo | Intern (Summer 2020  - Summer 2021) |  |  | KAIST |
| Jisu Yim | Intern (Winter 2021  - Summer 2021) | M.S. Student at HCI Lab, KAIST |  |  |
| Intizar Tashov | Intern (Spring 2021) |  |  | KAIST |
| Jisu Choi | Intern (Winter 2021) |  |  | KAIST |
| Youngjae Jang | Intern (Fall 2020  - Winter 2021) | Software Engineer at Toss |  | KAIST |
| Changgeon Ko | Intern (Fall 2020  - Winter 2021) |  |  | KAIST |
| Taehyeon An | Intern (Summer 2019  - Fall 2020) |  |  | KAIST |
| HyeonJeong Ha | Intern (Summer 2020  - Fall 2020) | Ph.D. Student at UIUC |  | KAIST |
| Anchit Tandon | Intern (Summer 2020  - Fall 2020) |  |  | IIT Delhi |
| Umar Taufiqulhakim | Intern (Fall 2020) |  |  | KAIST |
| Aitolkyn Baigutanova | Intern (Summer 2020) | Researcher at Wikimedia Foundation |  | KAIST |
| Eunseo Choi | Intern (Summer 2020) | M.S. student at MIT |  |  |
| Seungsu Kim | Intern (Summer 2020) |  |  | KAIST |
| Hyunchang Oh | Intern (Winter 2019  - Spring 2020) |  |  | KAIST |
| Sally Chen | Intern (Winter 2020) | M.S. Student at CMU |  | Brown University |
| Eric Doh | Intern (Winter 2020) |  |  | University of Sydney |
| Min A Kim | Intern (Winter 2020) | Software Engineer at Kakao |  | KAIST |
| Changyoon Lee | Intern (Summer 2018  - Winter 2020) | M.S. Student at U&I Lab, KAIST |  | KAIST |
| Nikhil Prakash | Intern (Summer 2019  - Winter 2020) | Ph.D. Student at Northeastern University |  | R V College of Engineering, India |
| Cheoljun Cho | Intern (Summer 2019) | Ph.D. Student at UC Berkeley |  | SNU |
| Yejun Kim | Intern (Summer 2019) | Software Engineer at Scatter Lab |  | KAIST |
| Yeonsu Kim | Intern (Summer 2019) | Ph.D. Student at HCI Lab, KAIST |  | KAIST |
| Nyoungwoo Lee | Intern (Summer 2018  - Summer 2019) | ML Researcher at Scatter Lab |  | KAIST |
| Jaeyoon Song | Intern (Winter 2019  - Summer 2019) | Ph.D. Student at MIT |  | SNU |
| Jimmy Wei | Intern (Summer 2019) | M.S. Student at Cornell Tech |  | Bucknell University |
| Hyeonggeun Yun | Intern (Winter 2019  - Summer 2019) | Co-founder & CTO at Companoid Labs |  | DGIST |
| Sunwoo Kwon | Intern (Winter 2019  - Spring 2019) | Researcher at Twelve Labs |  | CAU |
| Juan Lee | Intern (Winter 2019  - Spring 2019) |  |  | KAIST |
| Keon Lee | Intern (Winter 2019) | M.S. Student at KAIST |  | KAIST |
| Seongho Park | Intern (Summer 2018  - Fall 2018) |  |  | KAIST |
| Hyuntak Cha | Intern (Summer 2018) | CPO at Branch and Bound (CodeTree) |  | SNU |
| Rachel Kwak | Intern (Summer 2018) |  |  | MIT |
| Manav Rao | Intern (Summer 2018) |  |  | IIT Delhi |
| Jiyoun Ha | Intern (Winter 2018  - Spring 2018) | Software Engineer at Google |  | KAIST |
| Hyunjong Lee | Intern (Winter 2018  - Spring 2018) | M.S. Student at KAIST |  | KAIST |
| Seayeon Lee | Intern (Winter 2018) |  |  | KAIST |
| Jonghyuk Jung | Intern (Spring 2017  - Fall 2017) | UX Designer at Devisters |  | KAIST |
| Beomsu Kim | Intern (Summer 2017  - Fall 2017) |  |  | KAIST |
| Jooyoung Lee | Intern (Summer 2017  - Fall 2017) | Backend Engineer at Coupang |  | KAIST |
| Ina Ryu | Intern (Summer 2017  - Fall 2017) | Software Engineer at Pinterest |  | KAIST |
| Wookjae Byun | Intern (Summer 2017) |  |  | KAIST |
| Leonore Guillain | Intern (Summer 2017) | M.S. Student at EPFL |  | EPFL |
| Amy Han | Intern (Summer 2017) | Data Engineer at Capital One |  | Swarthmore College |
| Suhwan Jee | Intern (Summer 2017) | Backend Engineer at Rapport Labs |  | KAIST |
| Hyunsuk Shin | Intern (Summer 2017) |  |  | KAIST |
| Hyungwoo Kim | Intern (Spring 2017) |  |  | KAIST |
| Ching Liu | Intern (Fall 2016  - Spring 2017) | Engineer at SkillBench |  | NTHU |
| Hyunsung Cho | Intern (Fall 2016  - Winter 2017) | Ph.D. Student at CMU |  | KAIST |
| Jaesung Huh | Intern (Winter 2017) | Ph.D. Student at Oxford |  | SNU |
| Deokseong Kim | Intern (Winter 2017) |  |  | KAIST |
| Soya Park | Intern (Fall 2016  - Winter 2017) | Ph.D. Student at MIT |  | KAIST |
| Dongkwan Kim | Intern (Summer 2016  - Fall 2016) | Postdoc Researcher in Texas A&M |  | KAIST |
| Jiwoo Park | Intern (Summer 2016  - Fall 2016) | M.S. Student at KAIST Business School |  | KAIST |
| Juho Sun | Intern (Fall 2016) | Founder at Meanlt |  | KAIST |
| Taekyung Park | Intern (Summer 2016) |  |  | SNU |

## 최근 논문 목록 (2021–2026)

언어 모델과의 상호작용, 온라인 학습, 협업과 사회적 소통, 창작과 정보 탐색을 다룬 113개 게시 항목이다. 연도는 연구실 Publications의 연도 구역이며, 학술지·학회 정규 논문과 워크숍·포스터·데모·진행 중 연구 등을 함께 담았다. 제목·저자·발표처는 연구실 표기이며 별표는 누리집의 저자 표시다. 2026년 학회 항목 가운데 연구실 소식의 채택 기록을 기준으로 한 항목은 채택으로 표시했다.[^pubs][^news]

**2026**

- Daeheon Jeong, Yoonjoo Lee, Eugene Choi, Sinie van der Ben, Juho Kim. "Investigating Assistant Bias in LLM User Simulators Using a Role Vector". *EMNLP 2026 Findings (채택)*.
- Hyeon-Woo Nam, Yoonsu Kim, Kihoon Son, Juho Kim, Tae-Hyun Oh. "Hypothesize and Verify: Natural-Language Explanations of Vision Model Errors". *TMLR 2026*.
- Yoonsu Kim, Chanbin Park, Kihoon Son, Saelyne Yang, Juho Kim. "Contexty: Capturing and Organizing In-situ Thoughts for Context-Aware AI Support". *UIST 2026 (채택)*.
- Eunhye Kim, DaEun Choi, Bryan Min, Hyunjung Yi, Yue Jiang, Juho Kim. "Maru: Information Architecture as a Shared Language for Generating Aligned and Persistent User Interfaces". *UIST 2026 (채택)*.
- Hyehyun Chu, Yuri Lee, Yeon Su Park, Saelyne Yang, Juho Kim. "When AI "Works," When Does Help Begin?: Intergenerational Support Around Older Adults' LLM Usage". *CSCW 2026 Workshop on Growing Up (and Old) with AI*.
- Heechan Lee\*, Jeonggyu Kang\*, Junho Myung, Jaywoong Jeong, Juho Kim, Joseph Seering. "TIDES: A Longitudinal Bilingual Dataset for Modeling Multi-Party Social Dynamics". *COLM 2026 (채택)*.
- Yoonsu Kim, Hayeon Doh, Eunhye Kim, Jinho Son, Juho Kim. "STEPwise: Diagnosing Students' Math Problem-Solving Skills via LLM-Generated Stepwise Sub-Questions". *AIED 2026 on Interactive Events*.
- Yeon Su Park\*, Sieun Kim\*, Keighley Overbay, Seoyoung Kim, Sewook Wee, Daho Jung, Juho Kim. "Supporting Tutors in the Gig Economy with Automated Feedback: A Case Study on Ringle". *FoL 2026 Workshop on Pedagogical Evaluation of Automated Feedback*.
- Saelyne Yang, Jaesang Yu, Yi-Hao Peng, Kevin Qinghong Lin, Jae Won Cho, Yale Song, Juho Kim. "GUIDE: A Benchmark for Understanding and Assisting Users in Open-Ended GUI Tasks". *CVPR 2026 Workshop on Multi-Modal Reasoning for Agentic Intelligence*.
- Tae Soo Kim, Yoonjoo Lee, Jaesang Yu, John Joon Young Chung, Juho Kim. "DiscoverLLM: From Executing Intents to Discovering Them". *ICML 2026 (채택)*.
- Yoonsu Kim, Kihoon Son, Seoyoung Kim, Brandon Chin, Juho Kim. "[IntentFlow: Investigating Fluid Dynamics of Intent Communication in Generative AI](https://doi.org/10.1145/3800645.3812999)". *DIS 2026*.
- DaEun Choi, Kihoon Son, Jaesang Yu, Hyunjoon Jung, Juho Kim. "[IdeaBlocks: Expressing and Reusing Divergent Intents for Graphic Design Exploration using Generative AI](https://doi.org/10.1145/3800645.3813005)". *DIS 2026*.
- Yeon Su Park, Nadia Arvi, Seoyoung Kim, Juho Kim. "[Authorship Drift: How Self-Efficacy and Trust Evolve During LLM-Assisted Writing](https://doi.org/10.1145/3772318.3790276)". *CHI 2026*.
- Kihoon Son, DaEun Choi, Tae Soo Kim, Young-Ho Kim, Sangdoo Yun, Juho Kim. "[ClearFairy: Capturing Creative Workflows through Decision Structuring, In-Situ Questioning, and Rationale Inference](https://doi.org/10.1145/3772318.3791680)". *CHI 2026*.
- Jiangnan Xu, Haeseul Cha, Gosu Choi, Gyu-cheol Lee, Yeo-Jin Yoon, Zucheul Lee, Konstantinos Papangelis, Dae Hyun Kim, Juho Kim. "[DiaryPlay: AI-Assisted Authoring of Interactive Vignettes for Everyday Storytelling](https://doi.org/10.1145/3772318.3790572)". *CHI 2026*.
- Tae Soo Kim\*, Heechan Lee\*, Yoonjoo Lee, Joseph Seering, Juho Kim. "[Evalet: Evaluating Large Language Models by Fragmenting Outputs into Functions](https://doi.org/10.1145/3772318.3790285)". *CHI 2026*.
- Junho Myung, Hyunseung Lim\*, Hana Oh\*, Hyoungwook Jin, Nayeon Kang, So-Yeon Ahn, Hwajung Hong, Alice Oh, Juho Kim. "[When Scaffolding Breaks: Investigating Student Interaction with LLM-Based Writing Support in Real-Time K-12 EFL Classrooms](https://doi.org/10.1145/3772318.3791517)". *CHI 2026*.
- Saelyne Yang, Jaesang Yu, Yi-Hao Peng, Kevin Qinghong Lin, Jae Won Cho, Yale Song, Juho Kim. "GUIDE: A Benchmark for Understanding and Assisting Users in Open-Ended GUI Tasks". *CVPR 2026 (채택)*.
- Jeongeon Park, Bryan Min, Kihoon Son, Jean Y. Song, Xiaojuan Ma, Juho Kim. "[ChoiceMates: Supporting Unfamiliar Online Decision-Making with Multi-Agent Conversational Interactions](https://doi.org/10.1145/3742413.3789107)". *IUI 2026*.
- Daeheon Jeong\*, Seoyeon Byun\*, Kihoon Son, Dae Hyun Kim, Juho Kim. "CANVAS: A Benchmark for Vision-Language Models on Tool-Based User Interface Design". *AAAI 2026 (채택)*.

**2025**

- Gionnieve Lim, Juho Kim, Simon Perrault. "[Iffy-Or-Not: Critically Evaluating Potential Misinformation With Fallacy Detection and Socratic Questioning Using LLMs](https://doi.org/10.1145/3771935)". *TOCHI 2025*.
- Hyungyu Shin, Jingyu Tang, Yoonjoo Lee, Nayoung Kim, Hyunseung Lim, Ji Yong Cho, Hwajung Hong, Moontae Lee, Juho Kim. "Mind the Blind Spots: A Focus-Level Evaluation Framework for LLM Reviews". *EMNLP 2025 Main Track*.
- Hyunseung Lim, Sooyohn Nam, Sungmin Na, Ji Yong Cho, June Yong Yang, Hyungyu Shin, Yoonjoo Lee, Juho Kim, Moontae Lee, Hwajung Hong. "PANORAMA: A Dataset and Benchmark Tasks Capturing the Evaluation Trails and Rationales in Patent Examination". *NeurIPS 2025 Datasets & Benchmarks*.
- Jihyeong Hong, Eunyoung Ko, Juho Kim, Jeong-woo Jang. "[Why Social Media Users Press "Not Interested": Motivations, Anticipated Effects, and Result Interpretation](https://doi.org/10.1145/3757706)". *CSCW 2025*.
- Eun Jeong Kang, Haesoo Kim\*, Hyunwoo Kim\*, Susan R. Fussell, Juho Kim. "[Can Fans Build Parasocial Relationships through Idols' Simulated Voice Messages?: A Study of AI Private Call Users' Perceptions, Cognitions, and Behaviors](https://doi.org/10.1145/3711111)". *CSCW 2025*.
- Tae Soo Kim, Yoonjoo Lee, Yoonah Park, Jiho Kim, Young-Ho Kim, Juho Kim. "CUPID: Evaluating Personalized and Contextualized Alignment of LLMs from Interactions". *COLM 2025*.
- Yoonseo Choi, Eunhye Kim, Hyunwoo Kim, Donghyun Park, Honggu Lee, Jin Young Kim, Juho Kim. "[BloomIntent: Automating Search Evaluation with LLM-Generated Fine-Grained User Intents](https://doi.org/10.1145/3746059.3747677)". *UIST 2025*.
- DaEun Choi, Kihoon Son, Jaesang Yu, Hyunjoon Jung, Juho Kim. "[IdeaBlocks: Expressing and Reusing Exploratory Intents for Design Exploration with Generative AI](https://doi.org/10.1145/3746058.3759001)". *UIST 2025 Demos*.
- Yoonseo Choi, Eun Jeong Kang, Seulgi Choi, Min Kyung Lee, Juho Kim. "[Proxona: Supporting Creators' Sensemaking and Ideation with LLM-Powered Audience Personas](https://doi.org/10.1145/3706598.3714034)". *CHI 2025*.
- Hyoungwook Jin, Minju Yoo, Jeongeon Park, Yokyung Lee, Xu Wang, Juho Kim. "[TeachTune: Reviewing Pedagogical Agents Against Diverse Student Profiles with Simulated Students](https://doi.org/10.1145/3706598.3714054)". *CHI 2025*.
- Dae Hyun Kim\*, Daeheon Jeong\*, Shahnoza Yadgarova, Hyungyu Shin, Jinho Son, Hari Subramonyam, Juho Kim. "[PlanTogether: Facilitating AI Application Planning Using Information Graphs and Large Language Models](https://doi.org/10.1145/3706598.3714044)". *CHI 2025*.
- Juhoon Lee, Seoyoung Kim, Yeon Su Park, Juho Kim, Jeong-woo Jang, Joseph Seering. "[Less Talk, More Trust: Understanding Players' In-game Assessment of Communication Processes in League of Legends](https://doi.org/10.1145/3706598.3714226)". *CHI 2025*.
- Yoonsu Kim, Brandon Chin, Kihoon Son, Seoyoung Kim, Juho Kim. "[Applying the Gricean Maxims to a Human-LLM Interaction Cycle: Design Insights from a Participatory Approach](https://doi.org/10.1145/3706599.3719759)". *CHI 2025 Extended Abstracts (Late Breaking Work)*.
- DaEun Choi, Kihoon Son, Hyunjoon Jung, Juho Kim. "[Expandora: Broadening Design Exploration with Text-to-Image Model](https://doi.org/10.1145/3706599.3720189)". *CHI 2025 Extended Abstracts (Late Breaking Work)*.
- Saelyne Yang, Anh Truong, Juho Kim, Dingzeyu Li. "[VideoMix: Aggregating How-To Videos for Task-Oriented Learning](https://doi.org/10.1145/3708359.3712144)". *IUI 2025*.

**2024**

- Benjamin Newman\*, Yoonjoo Lee\*, Aakanksha Naik, Pao Siangliulue, Raymond Fok, Juho Kim, Daniel S. Weld, Joseph Chee Chang, Kyle Lo. "ARXIVDIGESTABLES: Synthesizing Scientific Literature into Tables using Language Models". *EMNLP 2024 Main Track*.
- Hyoungwook Jin\*, Haesoo Kim\*, Nathan Mekuria Haile, Soyeong Min, Juho Kim. "KUIZ: Encouraging Modular Learnersourcing of Multiple Choice Questions through LLM Interventions". *L@S 2024 Workshop on Learnersourcing: Student-generated Content @ Scale*.
- Hyoungwook Jin\*, Yoonsu Kim\*, Yeon Su Park, Bekzat Tilekbay, Juho Kim. "[Using Large Language Models To Diagnose Math Problem-solving Skills At Scale](https://doi.org/10.1145/3657604.3664697)". *L@S 2024 (Work-in-Progress)*.
- Steven Moore, Anjali Singh, Xinyi Lu, Hyoungwook Jin, Hassan Khosravi, Paul Denny, Christopher Brooks, Xu Wang, Juho Kim, John Stamper. "[Learnersourcing: Student-generated Content @ Scale: 2nd Annual Workshop](https://doi.org/10.1145/3657604.3664643)". *L@S 2024 Workshop Proposal*.
- Hyunwoo Kim\*, Yoonseo Choi\*, Taehyun Yang, Honggu Lee, Chaneon Park, Yongju Lee, Jin Young Kim, Juho Kim. "Using LLMs to Investigate Correlations of Conversational Follow-up Queries with User Satisfaction". *SIGIR 2024 Workshop on Large Language Models for Evaluation in Information Retrieval*.
- Saelyne Yang, Jaesang Yu, Jae Won Cho, Juho Kim. "Fine-Grained Action Understanding with Tools in Instructional Videos". *CVPR 2024 Workshop on Learning from Procedural Videos and Language*.
- Haechan Kim, Junho Myung, Seoyoung Kim, Sungpah Lee, Dongyeop Kang, Juho Kim. "LearnerVoice: A Dataset of Non-Native English Learners' Spontaneous Speech". *Interspeech 2024*.
- Jihyeong Hong, Yokyung Lee, Dae Hyun Kim, DaEun Choi, Yeo-Jin Yoon, Gyu-cheol Lee, Zucheul Lee, Juho Kim. "[A Context-Aware Onboarding Agent for Metaverse Powered by Large Language Models](https://doi.org/10.1145/3643834.3661579)". *DIS 2024*.
- Dae Hyun Kim, Hyungyu Shin, Shahnoza Yadgarova, Jinho Son, Hariharan Subramonyam, Juho Kim. "[AINeedsPlanner: A Workbook to Support Effective Collaboration Between AI Experts and Clients](https://doi.org/10.1145/3643834.3661577)". *DIS 2024*.
- Hyunseung Lim\*, Ji Yong Cho\*, Taewan Kim, Jeongeon Park, Hyungyu Shin, Seulgi Choi, Sunghyun Park, Kyungjae Lee, Juho Kim, Moontae Lee, Hwajung Hong. "[Co-Creating Question-and-Answer Style Articles with Large Language Models for Research Promotion](https://doi.org/10.1145/3643834.3660705)". *DIS 2024*.
- Nayeon Lee, Chani Jung\*, Junho Myung\*, Jiho Jin, Juho Kim, Alice Oh. "Exploring Cross-Cultural Differences in English Hate Speech Annotations: From Dataset Construction to Analysis". *NAACL 2024*.
- Yoonjoo Lee, Kihoon Son, Tae Soo Kim, Jisu Kim, John Joon Young Chung, Eytan Adar, Juho Kim. "[One vs. Many: Comprehending Accurate Information from Multiple Erroneous and Inconsistent AI Generations](https://doi.org/10.1145/3630106.3662681)". *FAccT 2024*.
- Yoonsu Kim, Kihoon Son, Seoyoung Kim, Juho Kim. "Beyond Prompts: Learning from Human Communication for Enhanced AI Intent Alignment". *CHI 2024 Workshop on Getting Back Together: HCI and Human Factors Joining Forces to Meet the AI Interaction Challenge*.
- Kihoon Son, Jinhyeon Kwon, DaEun Choi, Tae Soo Kim, Young-Ho Kim, Sangdoo Yun, Juho Kim. "Unveiling Disparities in Web Task Handling Between Human and Web Agent". *CHI 2024 Workshop on Computational Methodologies for Understanding, Automating, and Evaluating User Interfaces*.
- Jeongeon Park, Bryan Min, Jean Y. Song, Xiaojuan Ma, Juho Kim. "How do multiple LLM-powered conversational agents assist sensemaking and decision-making in an unfamiliar domain?". *CHI 2024 Workshop on Sensemaking: What is it today?*.
- Yoonjoo Lee, Tae Soo Kim, Juho Kim. "How to Reflect Diverse People's Perspectives in Large-Scale LLM-based Evaluations?". *CHI 2024 Workshop on Human Centered Evaluation and Auditing of Large Language Models*.
- Hyungyu Shin, Seulgi Choi, Ji Yong Cho, Sahar Admoni, Hyunseung Lim, Taewan Kim, Hwajung Hong, Moontae Lee, Juho Kim. "Towards an Evaluation of LLM-Generated Inspiration by Developing and Validating Inspiration Scale". *CHI 2024 Workshop on Human Centered Evaluation and Auditing of Large Language Models*.
- Jieun Han, Haneul Yoo, Junho Myung, Minsun Kim, Hyunseung Lim, Yoonsu Kim, Tak Yeon Lee, Hwajung Hong, Juho Kim, So-Yeon Ahn, Alice Oh. "LLM-as-a-tutor in EFL Writing Education: Focusing on Evaluation of Student-LLM Interaction". *EMNLP 2024 Workshop on Customizable NLP (CustomNLP4U)*.
- Jingchao Fang, Jeongeon Park, Juho Kim, Hao-Chuan Wang. "[EduLive: Re-Creating Cues for Instructor-Learner Interaction in Educational Live Streams with Learners’ Transcript-Based Annotations](https://doi.org/10.1145/3686960)". *CSCW 2024*.
- Seulgi Choi, Hyewon Lee, Yoonjoo Lee, Juho Kim. "[VIVID: Human-AI Collaborative Authoring of Vicarious Dialogues from Lecture Videos](https://doi.org/10.1145/3613904.3642867)". *CHI 2024*.
- Yoonjoo Lee, Hyeonsu B Kang, Matt Latzke, Juho Kim, Jonathan Bragg, Joseph Chee Chang, Pao Siangliulue. "[PaperWeaver: Enriching Topical Paper Alerts by Contextualizing Recommended Papers with User-collected Papers](https://doi.org/10.1145/3613904.3642196)". *CHI 2024*.
- DaEun Choi, Sumin Hong, Jeongeon Park, John Joon Young Chung, Juho Kim. "[CreativeConnect: Supporting Reference Recombination for Graphic Design Ideation with Generative AI](https://doi.org/10.1145/3613904.3642794)". *CHI 2024*.
- Kihoon Son, DaEun Choi, Tae Soo Kim, Young-Ho Kim, Juho Kim. "[GenQuery: Supporting Expressive Visual Search with Generative Models](https://doi.org/10.1145/3613904.3642847)". *CHI 2024*.
- Kihoon Son, DaEun Choi, Tae Soo Kim, Juho Kim. "[Demystifying Tacit Knowledge in Graphic Design: Characteristics, Instances, Approaches, and Guidelines](https://doi.org/10.1145/3613904.3642886)". *CHI 2024*.
- Hyoungwook Jin, Seong Hee Lee, Hyungyu Shin, Juho Kim. "[Teach AI How to Code: Using Large Language Models as Teachable Agents for Programming Education](https://doi.org/10.1145/3613904.3642349)". *CHI 2024*.
- Tae Soo Kim, Yoonjoo Lee, Jamin Shin, Young-Ho Kim, Juho Kim. "[EvalLM: Interactive Evaluation of Large Language Model Prompts on User-Defined Criteria](https://doi.org/10.1145/3613904.3642216)". *CHI 2024*.
- Hyung-Kwon Ko, Hyeon Jeon, Gwanmo Park, Dae Hyun Kim, Nam Wook Kim, Juho Kim, Jinwook Seo. "[Natural Language Dataset Generation Framework for Visualizations Powered by Large Language Models](https://doi.org/10.1145/3613904.3642943)". *CHI 2024*.
- Seonghyeon Ye\*, Doyoung Kim\*, Sungdong Kim, Hyeonbin Hwang, Seungone Kim, Yongrae Jo, James Thorne, Juho Kim, Minjoon Seo. "FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets". *ICLR 2024*.
- Yoonsu Kim, Jueon Lee, Seoyoung Kim, Jaehyuk Park, Juho Kim. "[Understanding Users' Dissatisfaction with ChatGPT Responses: Types, Resolving Tactics, and the Effect of Knowledge Level](https://doi.org/10.1145/3640543.3645148)". *IUI 2024*.
- Bekzat Tilekbay, Saelyne Yang, Michal Lewkowicz, Alex Suryapranata, Juho Kim. "[ExpressEdit: Video Editing with Natural Language and Sketching](https://doi.org/10.1145/3640543.3645164)". *IUI 2024*.
- Hyunwoo Kim, Khanh Duy Le, Gionnieve Lim, Dae Hyun Kim, Yoojin Hong, Juho Kim. "[DataDive: Supporting Readers' Contextualization of Statistical Statements with Data Exploration](https://doi.org/10.1145/3640543.3645155)". *IUI 2024*.
- Jeongeon Park, Eunyoung Ko, Yeon Su Park, Jinyeong Yim, Juho Kim. "[DynamicLabels: Supporting Informed Construction of Machine Learning Label Sets with Crowd Feedback](https://doi.org/10.1145/3640543.3645157)". *IUI 2024*.
- Seoyoung Kim, Yeon Su Park\*, Dakyeom Ahn\*, Jin Myung Kwak, Juho Kim. "[Is the Same Performance Really the Same?: Understanding How Listeners Perceive ASR Results Differently According to the Speaker’s Accent](https://doi.org/10.1145/3641008)". *CSCW 2024*.
- Hyoungwook Jin, Juho Kim. "[CodeTree: A System for Learnersourcing Subgoal Hierarchies in Code Examples](https://doi.org/10.1145/3637308)". *CSCW 2024*.
- Haesoo Kim, Juhoon Lee, Juho Kim, Jeong-woo Jang. "[Re:SPect: Enabling Active and Scalable Responses to Networked Online Harassment](https://doi.org/10.1145/3637394)". *CSCW 2024*.

**2023**

- Tae Soo Kim, Yoonjoo Lee, Minsuk Chang, Juho Kim. "[Cells, Generators, and Lenses: Design Framework for Object-Oriented Interaction with Large Language Models](https://doi.org/10.1145/3586183.3606833)". *UIST 2023*.
- Dae Hyun Kim, Seulgi Choi, Juho Kim, Vidya Setlur, Maneesh Agrawala. "EmphasisChecker: A Tool for Guiding Chart and Caption Emphasis". *IEEE VIS 2023*.
- Gionnieve Lim, Hyunwoo Kim, Yoonseo Choi, Toby Jia-Jun Li, Chinmay Kulkarni, Hariharan Subramonyam, Joseph Seering, Michael S. Bernstein, Amy X. Zhang, Elena L. Glassman, Simon Perrault, Juho Kim. "Designing for AI-Powered Social Computing Systems". *CSCW SIG*.
- Jieun Han\*, Haneul Yoo\*, Yoonsu Kim, Junho Myung, Minsun Kim, Hyunseung Lim, Juho Kim, Tak Yeon Lee, Hwajung Hong, So-Yeon Ahn, Alice Oh. "RECIPE: How to Integrate ChatGPT into EFL Writing Education". *L@S 2023 (Work-in-Progress)*.
- Juhoon Lee, Juho Kim, Jeong-woo Jang. "Look Upon Thyself: Understanding the Effect of Self-Reflection on Toxic Behavior in Online Gaming". *CHI 2023 Workshop on Combating Toxicity, Harassment, and Abuse in Online Social Spaces*.
- Haesoo Kim, Juhoon Lee, Juho Kim, Jeong-woo Jang. "Towards an Experience-Centric Paradigm of Online Harassment: Responding to Calling out and Networked Harassment". *CHI 2023 Workshop on Combating Toxicity, Harassment, and Abuse in Online Social Spaces*.
- Tae Soo Kim, Arghya Sarkar, Yoonjoo Lee, Minsuk Chang, Juho Kim. "LMCanvas: Object-Oriented Interaction to Personalize Large Language Model-Powered Writing Environments". *CHI 2023 Workshop on Generative AI and HCI*.
- Yoonseo Choi, Eun Jeong Kang, Min Kyung Lee, Juho Kim. "[Creator-friendly Algorithms: Behaviors, Challenges, and Design Opportunities in Algorithmic Platforms](https://doi.org/10.1145/3544548.3581386)". *CHI 2023*.
- Saelyne Yang, Sangkyung Kwak\*, Juhoon Lee\*, Juho Kim. "[Beyond Instructions: A Taxonomy of Information Types in How-to Videos](https://doi.org/10.1145/3544548.3581126)". *CHI 2023*.
- Seoyoung Kim, Donghoon Shin, Jeongyeon Kim, Soonwoo Kwon, Juho Kim. "[How Older Adults Use Online Videos for Learning](https://doi.org/10.1145/3544548.3580671)". *CHI 2023*.
- Yoonjoo Lee, Tae Soo Kim, Sungdong Kim, Yohan Yun, Juho Kim. "[DAPIE: Interactive Step-by-Step Explanatory Dialogues to Answer Children’s Why and How Questions](https://doi.org/10.1145/3544548.3581369)". *CHI 2023*.
- Jeongyeon Kim, DaEun Choi, Nicole Lee, Matt Beane, Juho Kim. "[Surch: Enabling Structural Search and Comparison for Surgical Videos](https://doi.org/10.1145/3544548.3580772)". *CHI 2023*.
- Jean Young Song\*, Sangwook Lee\*, Jisoo Lee, Min A Kim, Juho Kim. "[ModSandbox: Facilitating Online Community Moderation Through Error Prediction and Improvement of Automated Rules](https://doi.org/10.1145/3544548.3581057)". *CHI 2023*.
- Hyung-Kwon Ko, Gwanmo Park, Hyeon Jeon, Jaemin Jo, Juho Kim, Jinwook Seo. "[Large-scale Text-to-Image Generation Models for Visual Artists' Creative Works](https://doi.org/10.1145/3581641.3584078)". *IUI 2023*.

**2022**

- Haesoo Kim, Haeeun Kim, Juho Kim, Jeong-woo Jang. "[When Does it Become Harassment?: An Investigation of Online Criticism and Calling Out in Twitter](https://doi.org/10.1145/3555575)". *CSCW 2022*.
- Haesoo Kim, Inhwa Song, Juho Kim. "Learnersourcing Modular and Dynamic Multiple Choice Questions". *L@S 2022 Workshop on Learnersourcing: Student-generated Content @ Scale*.
- Hyoungwook Jin, Juho Kim. "Learnersourcing Subgoal Hierarchies of Code Examples". *L@S 2022 Workshop on Learnersourcing: Student-generated Content @ Scale*.
- Yoonjoo Lee, Tae Soo Kim, Minsuk Chang, Juho Kim. "Interactive Children’s Story Rewriting Through Parent-Children Interaction". *ACL 2022 Workshop on Intelligent and Interactive Writing Assistants*.
- Saelyne Yang, Sangkyung Kwak, Tae Soo Kim, Juho Kim. "Improving Video Interfaces by Presenting Informational Units of Videos". *CHI 2022 Workshop on Computational Approaches for Understanding, Generating, and Adapting User Interfaces*.
- Meng Xia, Yankun Zhao\*, Jihyeong Hong\*, Mehmet Hamza Erol\*, Taewook Kim, Juho Kim. "RLens: A Computer-aided Visualization System for Supporting Reflection on Language Learning under Distributed Tutorship". *Learning at Scale 2022*.
- Jeongyeon Kim, DaEun Choi, Matthew Beane, Juho Kim. "Techniques for Semantic Search and Comparison for Robotic Surgery Videos". *CHI 2022 Workshop on Integration of Human Factors in Surgery: Interdisciplinary Collaboration in Design, Development, and Evaluation of Surgical Technologies*.
- Eunyoung Ko, Yeonsu Kim, Juho Kim. "ReviewAid: A Scaffolded Approach to Supporting Readers’ Evaluation of Health News". *ICLS 2022*.
- Eunyoung Ko, Eunseo Choi, Jeong-woo Jang, Juho Kim. "[Capturing Diverse and Precise Reactions to a Comment with User-Generated Labels](https://doi.org/10.1145/3485447.3512243)". *TheWebConf 2022*.
- Meng Xia, Yankun Zhao, Mehmet Hamza Erol, Jihyeong Hong, Juho Kim. "[Understanding Distributed Tutorship in Online Language Tutoring](https://doi.org/10.1145/3485447.3512243)". *LAK 2022*.
- Saelyne Yang, Jisu Yim, Juho Kim, Hijung Valentina Shin. "[CatchLive: Real-time Summarization of Live Streams with Stream Content and Interaction Data](https://doi.org/10.1145/3491102.3517461)". *CHI 2022*.
- Kabdo Choi, Hyungyu Shin, Meng Xia, Juho Kim. "[AlgoSolve: Supporting Subgoal Learning in Algorithmic Problem-Solving with Learnersourced Microtasks](https://doi.org/10.1145/3491102.3501917)". *CHI 2022*.
- Mina Huh, Yunjung Lee, Dasom Choi, Haesoo Kim, Uran Oh, Juho Kim. "[Cocomix: Utilizing Comments to Improve Non-Visual Webtoon Accessibility](https://doi.org/10.1145/3491102.3502081)". *CHI 2022*.
- Yoonjoo Lee, John Joon Young Chung, Tae Soo Kim, Jean Young Song, Juho Kim. "[Promptiverse: Scalable Generation of Scaffolding Prompts through Human-AI Hybrid Knowledge Graph Annotation](https://doi.org/10.1145/3491102.3502087)". *CHI 2022*.
- Tae Soo Kim, DaEun Choi, Yoonseo Choi, Juho Kim. "[Stylette: Styling the Web with Natural Language](https://doi.org/10.1145/3491102.3501931)". *CHI 2022*.
- Jeongyeon Kim, Yubin Choi, Minsuk Kahng, Juho Kim. "[FitVid: Responsive and Flexible Video Content Adaptation](https://doi.org/10.1145/3491102.3501948)". *CHI 2022*.
- Jeongyeon Kim, Yubin Choi, Meng Xia, Juho Kim. "[Mobile-Friendly Content Design for MOOCs: Challenges, Requirements, and Design Opportunities](https://doi.org/10.1145/3491102.3502054)". *CHI 2022*.
- Saelyne Yang, Jisu Yim, Aitolkyn Baigutanova, Seoyoung Kim, Minsuk Chang, Juho Kim. "[SoftVideo: Improving the Learning Experience of Software Tutorial Videos with Collective Interaction Data](https://doi.org/10.1145/3490099.3511106)". *IUI 2022*.
- Hyungyu Shin, Nabila Sindi, Yoonjoo Lee, Jaeryoung Ka, Jean Young Song, Juho Kim. "[XDesign: Integrating Interface Design into Explainable AI Education](https://doi.org/10.1145/3478432.3499052)". *SIGCSE TS 2022 Posters*.

**2021**

- Yoonseo Choi, Eun Jeong Kang, Juho Kim. "How Does Netflix "Understand" Me?: Exploring End-user Needs to Design Human-centered Explanations". *NeurIPS 2021 Workshop on Human Centered AI*.
- Jeongeon Park, Eunyoung Ko, Donghoon Han, Jinyeong Yim, Juho Kim. "Supporting Dynamic Construction of Datasets through Crowd Suggestions". *HCOMP 2021 WiP (Works-in-Progress)*.
- Taewook Kim, Hyunwoo Kim, Juho Kim, Xiaojuan Ma. "Improving Readers’ Awareness of Divergent Viewpoints by Displaying Agendas of Comments in Online News Discussions". *CSCW 2021 Posters*.
- Tae Soo Kim, Nitesh Goyal, Jeongyeon Kim, Juho Kim, Sungsoo Ray Hong. "[Supporting Collaborative Sequencing of Small Groups through Visual Awareness](https://doi.org/10.1145/3449250)". *CSCW 2021*.
- Hyunwoo Kim, Haesoo Kim, Kyung Je Jo, Juho Kim. "[StarryThoughts: Facilitating Diverse Opinion Exploration on Social Issues](https://doi.org/10.1145/3449140)". *CSCW 2021*.
- Minsuk Chang, Mina Huh, Juho Kim. "[RubySlippers: Supporting Content-based Voice Navigation for How-to Videos](https://doi.org/10.1145/3411764.3445131)". *CHI 2021*.
- Yoonjoo Lee, John Joon Young Chung, Jean Young Song, Minsuk Chang, Juho Kim. "[Personalizing Ambience and Illusionary Presence: How People Use “Study with me” Videos to Create Effective Studying Environments](https://doi.org/10.1145/3411764.3445222)". *CHI 2021*.
- Tae Soo Kim, Seungsu Kim, Yoonseo Choi, Juho Kim. "[Winder: Linking Speech and Visual Objects to Support Communication in Asynchronous Collaboration](https://doi.org/10.1145/3411764.3445686)". *CHI 2021*.
- Jeongyeon Kim, Juho Kim. "[Guideline-Based Evaluation and Design Opportunities for Mobile Video-based Learning](https://doi.org/10.1145/3411763.3451725)". *CHI 2021 Extended Abstracts (Late Breaking Work)*.
- Jeongyeon Kim, Juho Kim. "FitVid: Towards Development of Responsive and Fluid Video Content Adaptation". *AAAI 2021 Workshop on Imagining Post-COVID Education with AI*.

## 수상과 선정

2021년 10월 13일부터 2026년 10월 13일까지 News에 게시된 수상·선정 기록이다. 날짜는 게시일이며, 같은 글이 여러 수상자를 알리기도 한다.[^news]

- 2026-05-12 · DaEun이 이끈 「IdeaBlocks」 논문이 DIS 2026 Honorable Mention Award(입선)를 받았다.
- 2026-03-09 · Junho가 이끈 「When Scaffolding Breaks」 논문은 CHI 2026 Best Paper Award를, Tae Soo와 Heechan이 함께 이끈 「Evalet」 논문은 Honorable Mention Award(입선)를 받았다.
- 2026-01-30 · Eunyoung, Tae Soo, Hyungyu, Saelyne, Yoonjoo, Yeon Su, Hyoungwook, Bekzat이 전산학부 우수학위논문상을 받았다.
- 2026-01-30 · 연구실이 2026 KAIST Globalization Excellence Lab으로 선정됐다.
- 2026-01-28 · Tae Soo가 「Disentangling Text for Interactive AI Alignment」로 공과대학 박사학위논문상을 받았다.
- 2025-10-17 · Jihyeong이 이끈 「Why Social Media Users Press "Not Interested"」 논문이 CSCW 2025 Honorable Mention Award(입선)를 받았다.
- 2025-02-11 · Seoyoung Kim이 전산학부 우수박사학위논문상을 받았다.
- 2024-01-25 · Yoonjoo Lee가 「DAPIE」 발표로 HCI Korea 2024 Outstanding Presentation Award를 받았다.
- 2023-11-02 · Jeongeon과 DaEun이 「AudiLens: Configurable LLM-Generated Audiences for Public Speech Practice」로 UIST 2023 Student Innovation Contest에서 Honorable Mention(입선)을 받았다.
- 2022-12-13 · Saelyne이 NAVER PhD Fellowship Award를 받았다.
- 2022-04-06 · 「Mobile-Friendly Content Design for MOOCs」 논문은 CHI 2022 Best Paper Award를, 「Stylette」 논문은 Honorable Mention Award(입선)를 받았다.
- 2022-02-11 · Haesoo가 2021년 가을 CS473 과목의 Education 4.0Q 우수 조교로 선정됐다고 알렸다.
- 2022-02-09 · Tae Soo와 Jeongyeon이 전산학부 우수석사학위논문상을 받았다.
- 2022-02-07 · Seoyoung, Seokhun Jeong, Seulgi Choi, Juhoon Lee가 「Data-Driven and Personalized Vocabulary Recommendation for English Learners」로 KSC 우수논문상을 받았다.

## 연구실 소식

2021년 10월 13일부터 2026년 10월 13일까지의 논문 채택·학술 활동·연구 소개·모집 공지다. 날짜는 News의 게시일이며 당시의 계획·채택·모집 상태를 담았다.[^news]

- 2026-10-07 · 2027년 석사과정 학생 모집 공지. 지원 마감일은 2026년 10월 13일이다.
- 2026-08-21 · 「Investigating Assistant Bias in LLM User Simulators Using a Role Vector」가 EMNLP 2026 Findings에 채택됐다.
- 2026-08-10 · 「Contexty」와 「Maru」 논문이 UIST 2026에 채택됐다.
- 2026-07-09 · 「TIDES: A Longitudinal Bilingual Dataset for Modeling Multi-Party Social Dynamics」가 COLM 2026에 채택됐다.
- 2026-05-01 · 「DiscoverLLM: From Executing Intents to Discovering Them」이 ICML 2026에 채택됐다.
- 2026-04-28 · 2026년 여름 학부 연구 인턴 모집 공지.
- 2026-04-10 · CHI 2026에 정규 논문 6편, 포스터 1편, 학생 연구 경진대회 논문 1편, 워크숍 논문 2편이 채택됐다고 알렸다.
- 2026-03-19 · 「IntentFlow」와 「IdeaBlocks」 논문이 DIS 2026에 채택됐다.
- 2026-02-21 · 「GUIDE: A Benchmark for Understanding and Assisting Users in Open-Ended GUI Tasks」가 CVPR 2026에 채택됐다.
- 2026-01-16 · CHI 2026 정규 논문 6편의 조건부 채택을 알렸다.
- 2025-12-14 · 「ChoiceMates: Supporting Unfamiliar Online Decision-Making with Multi-Agent Conversational Interactions」가 IUI 2026에 채택됐다.
- 2025-11-10 · 「CANVAS: A Benchmark for Vision-Language Models on Tool-Based User Interface Design」가 AAAI 2026에 채택됐다.
- 2025-10-28 · 2026년 겨울 학부 연구 인턴 모집 공지.
- 2025-10-20 · 공동연구진의 논문이 NeurIPS 2025와 EMNLP 2025에 채택됐다고 알렸다.
- 2025-08-13 · 「CUPID」 논문이 COLM 2025에 채택됐다.
- 2025-08-08 · UIST 2025에 정규 논문, 데모, 박사과정 심포지엄 논문이 각각 1편씩 채택됐다고 알렸다.
- 2025-08-06 · 「Why Social Media Users Press "Not Interested"」 논문이 CSCW 2025에 채택됐다.
- 2025-04-28 · CHI 2025에 정규 논문 4편, 진행 중 연구 논문 4편, 박사과정 심포지엄 논문 1편이 채택됐다고 알렸다.
- 2025-04-18 · 2025년 여름 학부 연구 인턴 모집 공지.
- 2025-01-17 · CHI 2025에 정규 논문 4편, 진행 중 연구 논문 4편, 박사과정 심포지엄 논문 1편의 채택을 알렸다.
- 2025-01-10 · 「VideoMix: Aggregating How-To Videos for Task-Oriented Learning」의 IUI 2025 조건부 채택을 알렸다.
- 2024-11-18 · CSCW 2024에서 연구실과 공동연구진의 논문 4편을 발표했고, 구성원 4명이 현장에 참석했다고 알렸다.
- 2024-10-07 · 2025년 봄 석사과정 학생 모집 공지. 지원 마감일은 2024년 10월 22일이다.
- 2024-09-24 · 「Can Fans Build Parasocial Relationships through Idols’ Simulated Voice Messages?」가 CSCW 2025에 채택됐다.
- 2024-07-04 · 2024년 가을 석사과정 학생 모집 공지. 지원 마감일은 2024년 7월 12일이다.
- 2024-06-04 · 연구실과 공동연구진의 논문이 Interspeech 2024에 채택됐다고 알렸다.
- 2024-06-01 · 연구실과 공동연구진의 논문 3편이 DIS 2024에 채택됐다고 알렸다.
- 2024-05-11 · CHI 2024에서 정규 논문 9편과 워크숍 논문 6편을 발표할 예정이며, 구성원 12명이 현장에 참석할 예정이라고 알렸다.
- 2024-04-18 · 2024년 여름 학부 연구 인턴 모집 공지.
- 2024-04-08 · 「One vs. Many: Comprehending Accurate Information from Multiple Erroneous and Inconsistent AI Generations」가 FAccT 2024에 채택됐다.
- 2024-04-01 · 「EduLive」 논문이 CSCW 2024에 채택됐다.
- 2024-01-19 · CHI 2024에 논문 8편이 조건부 채택됐다고 알렸다.
- 2023-12-18 · IUI 2024에 논문 4편이 채택됐다고 알렸다.
- 2023-10-22 · 2024년 겨울 학부 연구 인턴 모집 공지.
- 2023-10-13 · 2024년 봄 석사과정 학생 모집 공지. 지원 마감일은 2023년 10월 20일이다.
- 2023-09-26 · 「CodeTree」와 「Re:SPect」 논문이 CSCW 2024에 채택됐다.
- 2023-08-06 · 「Cells, Generators, and Lenses: Design Framework for Object-Oriented Interaction with Large Language Models」가 UIST 2023에 채택됐다.
- 2023-07-16 · 「EmphasisChecker: A Tool for Guiding Chart and Caption Emphasis」가 IEEE VIS 2023에 채택됐다.
- 2023-06-16 · 「Designing for AI-Powered Social Computing Systems」 주제의 CSCW 2023 특별관심그룹 제안이 채택됐다.
- 2023-04-24 · 2023년 여름 학부 연구 인턴 모집 공지.
- 2023-04-21 · CHI 2023에서 정규 논문 6편과 워크숍 논문 4편을 발표할 예정이며, 구성원 6명이 참석할 예정이라고 알렸다.
- 2023-03-15 · CHI 2023 워크숍에 논문 4편이 채택됐다고 알렸다.
- 2023-01-17 · CHI 2023에 논문 6편이 채택됐다고 알렸다.
- 2023-01-14 · 김주호 교수가 NeurIPS 2022에서 「Interaction-Centric AI」라는 제목의 기조강연을 했다고 알렸다.
- 2023-01-04 · 「Large-scale Text-to-Image Generation Models for Visual Artists' Creative Works」가 IUI 2023에 채택됐다.
- 2022-11-08 · 2023년 겨울 학부 연구 인턴 모집 공지.
- 2022-09-01 · 2022년 가을 학부 연구 인턴 모집 공지.
- 2022-05-25 · 「Learnersourcing Modular and Dynamic Multiple Choice Questions」와 「Learnersourcing Subgoal Hierarchies of Code Examples」가 L@S 2022 Learnersourcing 워크숍에 채택됐다.
- 2022-05-22 · 「When Does it Become Harassment?: An Investigation of Online Criticism and Calling Out in Twitter」가 CSCW 2022에 채택됐다.
- 2022-04-24 · 2022년 여름 학부 연구 인턴 모집 공지.
- 2022-04-20 · 「Interactive Children’s Story Rewriting Through Parent-Children Interaction」가 ACL 2022의 글쓰기 지원 도구 워크숍에 채택됐다.
- 2022-04-06 · Hyungyu와 김주호 교수의 AI 응용 설계 과정에 관한 글이 KAIST ILP 두 번째 호에 실렸다. RubySlippers, SolutionChat, Stylette를 소개했다.
- 2022-03-23 · 「RLens」 논문이 Learning at Scale 2022에 채택됐다.
- 2022-03-21 · 「Improving Video Interfaces by Presenting Informational Units of Videos」가 CHI 2022 워크숍에 채택됐다.
- 2022-03-21 · 「Techniques for Semantic Search and Comparison for Robotic Surgery Videos」가 CHI 2022의 수술 기술 설계·개발·평가 워크숍에 채택됐다.
- 2022-03-11 · 「ReviewAid: A Scaffolded Approach to Supporting Readers’ Evaluation of Health News」가 ICLS 2022에 채택됐다.
- 2022-02-08 · 「CatchLive: Real-time Summarization of Live Streams with Stream Content and Interaction Data」가 CHI 2022에 채택됐다.
- 2022-01-24 · 「Capturing Diverse and Precise Reactions to a Comment with User-Generated Labels」가 TheWebConf 2022에 채택됐다.
- 2021-12-21 · 「SoftVideo: Improving the Learning Experience of Software Tutorial Videos with Collective Interaction Data」가 IUI 2022에 채택됐다.
- 2021-12-04 · 전산학부를 대표해 연구를 소개하는 Open KAIST 영상이 공개됐다고 알렸다.
- 2021-12-03 · 「Understanding Distributed Tutorship in Online Language Tutoring」가 LAK 2022에 채택됐다.
- 2021-11-25 · 「How Does Netflix "Understand" Me?: Exploring End-user Needs to Design Human-centered Explanations」가 NeurIPS 2021 Human Centered AI 워크숍에 채택됐다.
- 2021-11-16 · CHI 2022에서 논문 6편이 소규모 수정 후 조건부 채택을, 2편이 수정 후 재심사 결정을 받았다고 알렸다.
- 2021-10-27 · 2022년 겨울 학부 연구 인턴 모집 공지.
- 2021-10-26 · 2022년 봄 석사과정 학생 모집 공지. 지원 마감일은 2021년 11월 2일이다.

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291 KAIST N1 624호, 우편번호 34141.[^home][^lab]
- 교수 사무실: N1 605호(학과 교수 명단 표기).[^faculty]
- 전화: 042-350-3570.[^lab]
- 교수 이메일: juhokim@kaist.ac.kr.[^people]
[^home]: KIXLAB, Home. <https://www.kixlab.org/> 2026-10-28 관측.
[^lab]: KAIST 전산학부, 「인터랙션 연구실」. <https://cs.kaist.ac.kr/research/labView?sn=101&menu=64> 2026-10-27 관측.
[^faculty]: KAIST 전산학부, 교수진 명단의 김주호 카드. <https://cs.kaist.ac.kr/people/faculty> 2026-10-27 관측.
[^people]: KIXLAB, People. <https://www.kixlab.org/people> 2026-10-28 관측.
[^pubs]: KIXLAB, Publications. <https://www.kixlab.org/publications> 2026-10-28 관측.
[^news]: KIXLAB, News. <https://www.kixlab.org/news> 2026-10-28 관측.
[^p1]: Y. Kim 외, J. Kim, UIST 2026 (채택) (2026). <https://arxiv.org/abs/2604.11067> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2604.11067> 2026-10-28 관측.
[^p2]: T. S. Kim 외, J. Kim, CHI 2024 (2024). <https://doi.org/10.1145/3613904.3642216> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2309.13633> 2026-10-28 관측.
[^p3]: H. Jin 외, J. Kim, CHI 2025 (2025). <https://doi.org/10.1145/3706598.3714054> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2410.04078> 2026-10-28 관측.
[^p4]: H. Jin, S. Lee, H. Shin, J. Kim, CHI 2024 (2024). <https://doi.org/10.1145/3613904.3642349> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2309.14534> 2026-10-28 관측.
[^p5]: D. Choi 외, J. Kim, CHI 2024 (2024). <https://doi.org/10.1145/3613904.3642794> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2312.11949> 2026-10-28 관측.
[^p6]: Y. Lee 외, P. Siangliulue, CHI 2024 (2024). <https://doi.org/10.1145/3613904.3642196> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2403.02939> 2026-10-28 관측.
[^p7]: Y. Lee 외, J. Kim, FAccT 2024 (2024). <https://doi.org/10.1145/3630106.3662681> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2405.05581> 2026-10-28 관측.
[^p8]: J. Kim 외, J. Kim, CHI 2023 (2023). <https://doi.org/10.1145/3544548.3580772> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1145/3544548.3580772> 2026-10-28 관측.
[^surchearly]: J. Kim, D. Choi, M. Beane, J. Kim, Techniques for Semantic Search and Comparison for Robotic Surgery Videos, CHI 2022 Workshop on Integration of Human Factors in Surgery: Interdisciplinary Collaboration in Design, Development, and Evaluation of Surgical Technologies (2022). <https://kixlab.github.io/website-files/2022/chi2022-workshop-Surch-paper.pdf> 초록 기준(연구실 게시 PDF 초록). 초록 원문 <https://kixlab.github.io/website-files/2022/chi2022-workshop-Surch-paper.pdf> 2026-10-28 관측.
[^reviewaid]: E.-Y. Ko, Y. Kim, J. Kim, ReviewAid: A Scaffolded Approach to Supporting Readers’ Evaluation of Health News, ICLS 2022 (2022). <https://kixlab.github.io/website-files/2022/icls2022-ReviewAid-paper.pdf> 초록 기준(연구실 게시 PDF 초록). 초록 원문 <https://kixlab.github.io/website-files/2022/icls2022-ReviewAid-paper.pdf> 2026-10-28 관측.

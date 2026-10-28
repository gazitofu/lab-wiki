# NC 연구실 (NCLab)

**KAIST 전산학부 · 송준화 교수**

- 분야: 모바일·사물인터넷 시스템, 인간–컴퓨터 상호작용, 소셜 컴퓨팅
- 대분야: 컴퓨팅·AI
- 태그: 인간–컴퓨터 상호작용[^p1][^p4][^p6], 모바일·유비쿼터스 센싱[^patent], 스마트홈·스마트빌딩[^p1][^patent], 고성능 컴퓨팅(HPC)[^p5]
- 홈페이지: <https://nclab.kaist.ac.kr/>
- 근거와 출처: [NC 연구실 근거 페이지](nclab-sources.md)

> 모바일 기기와 일상 공간의 기기를 사람의 필요와 연결하고, 여러 사람이 함께 쓰는 서비스와 시스템을 연구하는 연구실이다.[^faculty][^lab]

## 무엇을 연구하나

NC 연구실은 모바일·사물인터넷 시스템을 사람의 필요와 일상의 맥락에 맞게 설계한다. 사물인터넷(IoT, Internet of Things)은 사물이 통신망을 통해 정보를 주고받는 체계다. 학과 소개는 머신러닝(자료에서 규칙을 학습하는 계산 방법), 시스템, 인간–컴퓨터 상호작용(HCI, Human-Computer Interaction)을 융합하여 모바일·IoT 플랫폼과 응용을 개발한다고 설명한다. 인간–컴퓨터 상호작용은 사람과 컴퓨터·기기 사이의 사용 방식과 경험을 설계하고 평가하는 분야이고, 플랫폼은 다른 프로그램이나 서비스에 공통 기능을 제공하는 기반이다.[^faculty]

첫째 갈래는 여러 사람이 함께 쓰는 기기와 공간이다. Hivemind는 공공장소의 기기를 방문객들이 공동으로 제어하도록 하는 시스템과 설계 구조를 제안한다.[^p6] 뒤이은 연구는 기기 조작에 대한 선호가 충돌할 때의 투표·조작·소통 양상을 살폈다.[^p4] 소음이 나는 가전에서는 버튼을 누를 때 주변 사람의 상황과 예상 불편을 알려 주는 Socially-aware Button 개념과 TACT 시스템을 개발했다. 방해가 예상되면 작동을 잠시 미루고 사용 시점이나 방식을 바꾸도록 제안한다.[^p1] 관련 특허는 주변 소리와 원음의 시간적 상관관계(시간에 따른 두 신호의 변화가 서로 대응하는 정도)로 기기의 영향권에 있는지 판단하고, 참여자의 선호를 모아 냉난방·조명·스피커 등을 제어하는 구성을 기술한다.[^patent]

둘째 갈래는 짧은 원격 참여를 지속적인 돌봄과 교육으로 연결하는 서비스다. 지속적 원격 공동 돌봄(SRCC, Sustained Remote Collective Care)은 여러 자원봉사자의 짧은 원격 돌봄을 모아 지속적이고 빈번한 돌봄으로 조직하는 서비스 모형이다. 연구실은 참여 의지가 생활 상황에 따라 달라진다는 점에 주목해, 참여 기회를 먼저 제안하는 Nudge-to-Care 접근과 참여 알림 도구를 개발하고 참여 결정에 영향을 미치는 맥락을 살폈다.[^p2] CRAYON(Community-based RelAY Online educatioN)은 비전문 교사들이 모바일 기술로 번갈아 농촌 아동을 가르치는 교육 방법이다. 현장 적용에서 아동과 교사의 상호작용과 학습 참여를 지원하는 양상을 관찰했다.[^p3]

셋째 갈래는 여러 컴퓨터가 함께 계산할 때의 통신 부담을 줄이는 시스템 방법이다. 분산 메모리(각 컴퓨터가 실행 중인 프로그램과 자료의 저장 공간을 따로 갖는 방식)를 쓰는 클러스터(함께 계산하는 컴퓨터 묶음)에서 작업 배치를 연구했다. 공간 채움 곡선(영역의 모든 점을 지나도록 정의한 곡선)을 이용한 재배치로 통신하는 작업의 가까운 배치를 보존하고 작업 배치가 흩어지는 정도를 줄인다. 배치의 적합성을 분석하는 도구와 적용 여부를 실행 전에 예측하는 이진 분류기(입력을 두 범주 가운데 하나로 나누는 모형)도 제안했다.[^p5]

연구 메뉴에는 차세대 모바일·유비쿼터스 플랫폼, 아동 사이의 행동 관계, 상황을 고려하는 도시 컴퓨팅과 서비스, 일상 환경과 연결된 게임·플랫폼, 계산 저널리즘과 뉴미디어도 있다. 유비쿼터스 서비스는 일상 환경의 컴퓨팅 기기를 통해 여러 장소에서 이용하는 서비스이며, 계산 저널리즘은 자료와 계산 방법을 뉴스의 수집·분석·제작에 사용하는 분야다.[^research][^lab]

## 주요 연구 주제

### 1. 공용 기기의 공동 제어와 이웃을 고려하는 사용

공공장소 방문객의 기기 조작 참여, 선호가 충돌할 때의 조작 경험, 가전 사용이 이웃에게 미치는 영향을 알려 주는 상호작용을 연구한다. 기기를 함께 제어하는 구조와 이를 사용하는 사람들의 경험을 함께 다룬다.[^p1][^p4][^p6]

### 2. 원격 공동 돌봄과 지역사회 온라인 교육

짧은 자원봉사 참여를 이어 가는 서비스와 비전문 교사들이 번갈아 가르치는 모바일 교육 방법을 제안한다. 일상 맥락에 따른 참여 결정과, 교사·아동 사이의 상호작용을 살핀다.[^p2][^p3]

### 3. 병렬 응용의 작업 배치

여러 작업을 동시에 실행하는 병렬 응용에서 통신하는 작업의 배치를 조절한다. 공간 채움 곡선 기반 배치 틀, 성능 분석 도구, 실행 전 적용 여부 예측을 함께 개발했다.[^p5]

## 대표 논문

교수가 저자인 2021–2026년 KAIST 재직 시기 논문 가운데 공용 기기, 돌봄·교육, 병렬 시스템 갈래를 고르게 골랐다. 아래 여섯 편은 모두 송준화 교수가 마지막 저자다. ‘쉽게 말하면’ 칸은 각 논문의 등록 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 교수 역할 |
|---|---|---|---|---|
| 1 | 2026 | [Socially-appropriate Use of Noise-making Everyday Appliances in High-density Urban Housing](https://doi.org/10.1145/3831637) · IMWUT | 소음이 나는 가전을 사용할 때 주변 사람의 상황과 예상 불편을 알려 주는 Socially-aware Button 개념과 이를 구현한 TACT 시스템을 개발했다. 방해가 예상되면 작동을 잠시 늦추고 사용 시점이나 방식을 바꾸도록 제안한다. 비교 연구에서 기준 인터페이스보다 사용자 만족도와 설득력이 높았고, 실제 사용 환경에서 수용을 확인했다.[^p1] | 1저자 Youngjae Chang, 마지막 저자 송준화 |
| 2 | 2026 | [A Qualitative Exploration of Contextual Motivation Dynamics for Everyday Volunteering in Sustained Remote Collective Care](https://doi.org/10.1145/3831635) · IMWUT | 짧은 원격 자원봉사를 지속적인 돌봄으로 이어 가기 위해 참여 의지가 생길 만한 순간에 기회를 먼저 제안하는 Nudge-to-Care 접근을 구상했다. 아동의 영어 그림책 읽기를 돕는 VividRead 서비스와 함께 참여 알림 도구를 개발했다. 사용 기록·일기·인터뷰에서 참여 결정에 영향을 주는 생활 맥락과 알림에 대한 인식을 살펴 지속적 참여를 지원할 설계 고려사항을 제시했다.[^p2] | 1저자 Taegyeong Lee, 마지막 저자 송준화 |
| 3 | 2024 | [CRAYON: Exploration on Community-based Relayed Online Education Approach for Rural Children in South Korean EFL Context](https://doi.org/10.1145/3653684) · PACM HCI | 비전문 교사들이 모바일 기술로 번갈아 농촌 아동을 가르치는 지역사회 교육 방법 CRAYON을 제안했다. 현장 적용에서 아동과 교사의 상호작용 및 학습 참여를 이어 주는 지원 양상을 관찰했다. 기존 관계가 없는 교사와 학습자도 학습 환경에 포함할 가능성과, 교육기관의 지원 아래 경험이 적은 교사도 짧은 참여로 수업을 제공할 수 있다는 방향을 논의했다.[^p3] | 1저자 Seonghoon Kim, 마지막 저자 송준화 |
| 4 | 2024 | [Understanding Instant Social Control of Shared Devices in Public Spaces: A Field Trial](https://doi.org/10.1145/3678592) · IMWUT | 공공장소 방문객들이 기기를 즉석에서 공동으로 제어하는 접근을 제안하고, 조작 선호가 충돌할 때의 사용 경험을 연구했다. 탐색 도구를 현장에 배치해 사용 기록과 설문·인터뷰를 살폈다. 투표 전략, 기기를 시험하며 조작하는 양상, 다른 방문객과의 소통 시도, 타인의 불편 고려, 공동 제어의 수용과 유용성에 관한 결과를 얻었다.[^p4] | 1저자 Youngjae Chang, 마지막 저자 송준화 |
| 5 | 2022 | [Efficient task-mapping of parallel applications using a space-filling curve](https://doi.org/10.1145/3559009.3569657) · PACT | 통신이 많은 병렬 응용을 위해 공간 채움 곡선 기반 작업 재배치 틀을 제안했다. 통신하는 작업의 가까운 배치를 보존하고 배치의 흩어짐을 줄여 통신 부담을 줄인다. 성능 분석 도구와 적용 여부를 실행 전에 예측하는 이진 분류기도 개발했다. 작업 종류에 따라 기준 방법 대비 전체 성능이 약 30%에서 약 66% 개선되었다고 보고했다.[^p5] | 1저자 Oh-Kyoung Kwon, 마지막 저자 송준화 |
| 6 | 2021 | [Hivemind: Social Control-and-Use of IoT towards Democratization of Public Spaces](https://doi.org/10.1145/3458864.3466626) · MobiSys | 공공장소 기기의 공동 제어를 위한 설계 구조와 Hivemind 시스템을 제안했다. 방문객이 기기 조작에 함께 참여할 수 있게 하며, 기성 기기의 내부 구현을 바꾸지 않고도 시스템에 연결하도록 했다. 현장 적용에서 서비스가 다루는 범위와 방문객의 공동 제어 수용을 확인했다.[^p6] | 1저자 Wonjung Kim, 마지막 저자 송준화 |

## 교수와 전문 분야

송준화 교수는 1988년 서울대학교 전산학 학사, 1997년 미국 University of Maryland, College Park 전산학 박사를 받았다. IBM T. J. Watson Research Center 연구원을 거쳐 2000년 8월 KAIST 조교수로 부임했고, 2003년 9월 부교수, 2011년 9월 교수로 재직 이력을 적고 있다.[^prof] 전산학부 교수 소개는 2011년 KAIST지정 석좌교수 임명을 기재한다.[^faculty]

전산학부의 전공 표기는 운영체제(컴퓨터 자원과 프로그램 실행을 관리하는 기본 소프트웨어), 모바일, IoT시스템, 소셜 컴퓨팅이다. 대표 논문은 공용 기기의 공동 제어, 모바일 돌봄·교육, 병렬 응용의 작업 배치를 다룬다.[^p1][^p2][^p3][^p4][^p5][^p6] 교수 소개는 모바일·IoT·웨어러블 컴퓨팅(몸에 착용하는 기기를 이용하는 컴퓨팅), 돌봄 컴퓨팅과 플랫폼, 사회·문화 컴퓨팅, 유비쿼터스 서비스, 컴퓨터 시스템, 분산 시스템(여러 컴퓨터가 통신하며 기능을 수행하는 체계), 인터넷 뉴스·멀티미디어 시스템과 서비스를 관심 분야로 적는다.[^faculty][^prof]

## 응용 분야

대표 논문의 응용 대상은 공동 주거의 소음 가전, 공공장소의 공유 기기, 아동 영어 교육과 원격 자원봉사, 통신이 많은 병렬 응용이다.[^p1][^p2][^p3][^p4][^p5][^p6] 연구실 소개는 교통·위치 기반 서비스, 오락, 미디어·방송, 교육, 물류, 보안, 도시 서비스를 응용 대상으로 든다.[^lab] 특허 공개문헌의 구체적 대상은 냉난방·조명·스피커처럼 공용 공간의 이용 경험에 영향을 주는 기기다.[^patent]

## 구성원

2026년 10월 28일 연구실 구성원 자료에 게시된 박사후연구원 1명, 박사과정 10명, 석사과정 4명, 학부 연구생 3명이다. 과정·직위와 이메일은 연구실 게시 표기를 기준으로 했다.[^members] ‘대표 논문 참여’는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| 이승철 (Seungchul Lee) | 박사후연구원 | seungchul@nclab.kaist.ac.kr | 1, 3, 4, 5, 6 |
| 김성훈 (Seonghoon Kim) | 박사과정 | shkim@nclab.kaist.ac.kr | 2, 3 |
| Hailu Belay Kahsay | 박사과정 | bellay@nclab.kaist.ac.kr |  |
| 이태경 (Taegyeong Lee) | 박사과정 | tglee@nclab.kaist.ac.kr | 2, 6 |
| 장영재 (Youngjae Chang) | 박사과정 | yjchang@nclab.kaist.ac.kr | 1, 4, 6 |
| 원정호 (Jeongho Won) | 박사과정 | wonjeongho@nclab.kaist.ac.kr |  |
| 이현종 (Hyunjong Lee) | 박사과정 | hyunjong@nclab.kaist.ac.kr | 1, 3, 4 |
| 강성웅 (Seongwoong Kang) | 박사과정 | seongwoong@nclab.kaist.ac.kr | 3 |
| 한수경 (Sookyung Han) | 박사과정 | sookyung@nclab.kaist.ac.kr | 2, 4 |
| 백인선 (Insun Baek) | 박사과정 | insun@nclab.kaist.ac.kr | 2 |
| Selahaddin Honi | 박사과정 | honi@nclab.kaist.ac.kr |  |
| 남경민 (Kyungmin Nam) | 석사과정 | kyungmin@nclab.kaist.ac.kr |  |
| 전해광 (Haegwang Jeon) | 석사과정 | hgjeon@nclab.kaist.ac.kr |  |
| 이경주 (Gyeongju Lee) | 석사과정 | gjlee@nclab.kaist.ac.kr |  |
| 장영욱 (Yeonguk Jang) | 석사과정 | yeonguk@nclab.kaist.ac.kr |  |
| Dilnurakhon Tulanova | 학부 연구생 | dilnura@nclab.kaist.ac.kr |  |
| 유승엽 (Seungyeop Yoo) | 학부 연구생 |  |  |
| 양모중 (Mojung Yang) | 학부 연구생 |  |  |

## 최근 논문 목록 (2021–2026)

공용 기기의 사용, 온라인 교육과 참여, 병렬 응용의 작업 배치, 배터리 상태 예측을 다룬다. 연구실 논문 목록의 2021–2026년 구역에서 송준화 교수가 저자로 기재된 8편이며, 연도·제목·저자·발표처는 연구실 표기다. 별표와 공동 1저자 설명도 원문 표기다.[^pubs]

**2026**

- Taegyeong Lee, Seonghoon Kim, Insun Baek, Sookyung Han, Junehwa Song. "A Qualitative Exploration of Contextual Motivation Dynamics for Everyday Volunteering in Sustained Remote Collective Care". *Proceedings of the ACM IMWUT, Vol. 10, No. 3, Article 120. September 2026*.
- Youngjae Chang, Seungchul Lee, Hyunjong Lee, Wonjung Kim, Junehwa Song. "Socially-appropriate Use of Noise-making Everyday Appliances in High-density Urban Housing". *Proceedings of the ACM IMWUT, Vol. 10, No. 3, Article 84. September 2026*.
- Insun Baek\*, Sookyung Han\*, Hyunjong Lee, Seungchul Lee, Youngjae Chang, Seonghoon Kim, Junehwa Song. "Understanding in-situ participation-based development of non-professional tutors in short-relay teaching". *Proceedings of the ACM on Human-Computer Interaction, Volume 10, Issue 6 (CSCW108), October, 2026 (\* Co-primary authors.)*.

**2024**

- Seonghoon Kim\*, Hyunjong Lee\*, Seongwoong Kang, Michelle Goh, Wonjung Kim, Seungchul Lee, Souneil Park, So-Yeon Ahn, Junehwa Song. "CRAYON: Exploration on Community-based Relayed Online Education Approach for Rural Children in South Korean EFL Context". *Proceedings of the ACM on Human-Computer Interaction, Volume 8, Issue CSCW1, April, 2024 (\* Co-primary authors.)*.
- Youngjae Chang, Sookyung Han, Hyunjong Lee, Seungchul Lee,Wonjung Kim, Jinu Choi, Chloe Ann McCracken, Junehwa Song. "Understanding Instant Social Control of Shared Devices in Public Spaces: A Field Trial". *Proceedings of the ACM IMWUT, Vol. 8, No. 3, Article 93. September 2024*.

**2022**

- Oh-kyoung Kwon, Ji-hoon Kang, Seungchul Lee, Wonjung Kim, Junehwa Song. "Efficient task-mapping of parallel applications using a space-filling curve". *Proceedings of the International Conference on Parallel Architectures and Compilation Techniques (PACT '22), Chicago, IL, USA, October, 2022*.

**2021**

- Wonjung Kim, Seungchul Lee, Youngjae Chang, Taegyeong Lee, Inseok Hwang, Junehwa Song. "Hivemind: Social Control-and-Use of IoT towards Democratization of Public Spaces". *Proceedings of ACM MobiSys ’21, Virtual, June, 2021*.
- Mohammad A. Hoque, Petteri Nurmi, Arjun Kumar, Samu Varjonen, Junehwa Song, Michael G. Pecht, Sasu Tarkoma. "Data Driven Analysis of Lithium-ion Battery Internal Resistance Towards Reliable State of Health Prediction". *Journal of Power Sources, Vol. 513, Elsevier, November, 2021*.

## 특허

송준화 교수가 발명자로 기재되고 2021–2026년 범위에 출원된 미국 특허 공개문헌 1건이다. 공개번호는 등록번호와 구별한다.[^patent]

- SYSTEM AND METHOD OF SOCIAL CONTROL-AND-USE OF IoT DEVICE, CONTROL SERVER SUPPORTING SOCIAL CONTROL-AND-USE OF IoT DEVICE AND MOBILE DEVICE USED FOR SOCIAL CONTROL-AND-USE OF IoT DEVICE (출원번호 US17/562,137; 출원일 2021-12-27; 번호 US20230155903A1 (공개 2023-05-18); 발명자 Junehwa Song, Wonjung Kim, Seungchul Lee, Youngjae Chang, Taegyeong Lee, Inseok Hwang; 상태 Abandoned (Google Patents 표시))

## 수상

연구실의 2022년 11월 소식에 게시된 수상이다. 송준화 교수의 수상과 구분하여 이현종 공저 논문의 수상으로 적었다.[^news][^pubs]

- 2022/11 · 이현종 공저 논문 「Ultra-low Power DNN Accelerators for IoT: Resource Characterization of the MAX78000」가 AIChallengeIoT Best Paper Award를 받았다.

## 소식

2021년 10월 13일–2026년 10월 13일 범위의 연구실 소식 가운데 워크숍 주최·발표 3건과 논문 채택 2건이다. 날짜는 원문의 게시 연월이며, 수상은 위 절에 따로 실었다.[^news]

- 2025/07 · 제1회 Care and Computing Workshop을 주최하고, Chaperone 연구(발표: 장영재·이현종)와 CRAYON 연구(발표: 이승철)를 발표했다.
- 2025/07 · 부산에서 열린 제10회 A3 Foresight Program Workshop을 기획하고 주최했다.
- 2025/05 · 제9회 A3 Foresight Program Workshop에서 「Towards Inclusive IoT in Public Spaces: Rethinking Hivemind with Care Co-pilot」(남경민)과 「CRAYON x Sustained Volunteerism: Exploring Tutor Reflections on Collaborative Micro-Tutoring Efficacy」(Selahaddin HONI)를 발표했다.
- 2024/09 · 「Understanding Instant Social Control of Shared Devices in Public Spaces: A Field Trial」이 IMWUT Volume 8 (2024)에 채택되었다.
- 2024/04 · 「CRAYON: Exploration on Community-based Relayed Online Education Approach for Rural Children in South Korean EFL Context」가 CSCW 2024에 채택되었다.

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291 KAIST 전산학부 NCLab, 4438호[^home]
- 교수연구실: E3-1, 4435호[^faculty]
- 교수 이메일: junesong@kaist.ac.kr[^prof]
- 전화: +82-42-350-3546(교수), +82-42-350-7746(연구실)[^home]
- 팩스: +82-42-350-7846[^home]

## 각주
[^faculty]: KAIST 전산학부, 「송준화」. 소속·직급·전공·연구 소개·재직 이력·교수연구실. <https://cs.kaist.ac.kr/people/view?idx=13&kind=faculty&menu=160> (관측 2026-10-28).
[^lab]: KAIST 전산학부, 「NC 연구실」. 연구실명·지도교수·연구 소개. <https://cs.kaist.ac.kr/research/labView?sn=80&menu=64> (관측 2026-10-27).
[^prof]: NCLab, 「Junehwa Song」. 관심 분야·학력·재직 이력·교수 이메일. <https://nclab.kaist.ac.kr/professor_page.html> (관측 2026-10-28).
[^research]: NCLab, 연구 메뉴의 다섯 갈래. <http://nclab.kaist.ac.kr/data/research.json> (관측 2026-10-28).
[^members]: NCLab, 구성원 자료의 Postdoc·PHD Student·MS Student·Undergraduate Student 항목. <http://nclab.kaist.ac.kr/data/members.json> (관측 2026-10-28).
[^pubs]: NCLab, 논문 목록의 2021–2026년 항목. <http://nclab.kaist.ac.kr/data/publication.json> (관측 2026-10-28).
[^patent]: Google Patents, US20230155903A1, 출원 US17/562,137. 발명자·출원일·공개일·공용 기기 제어 시스템 설명. <https://patents.google.com/patent/US20230155903A1/en> (관측 2026-10-28).
[^home]: NCLab, 「Home」, Contact Information. <https://nclab.kaist.ac.kr/> (관측 2026-10-28).
[^news]: NCLab, 연구실 소식. <http://nclab.kaist.ac.kr/data/news.json> (관측 2026-10-28).
[^p1]: Y. Chang 외, J. Song, Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (2026). <https://doi.org/10.1145/3831637> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1145/3831637> (관측 2026-10-28).
[^p2]: T. Lee 외, J. Song, Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (2026). <https://doi.org/10.1145/3831635> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1145/3831635> (관측 2026-10-28).
[^p3]: S. Kim 외, J. Song, Proceedings of the ACM on Human-Computer Interaction (2024). <https://doi.org/10.1145/3653684> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1145/3653684> (관측 2026-10-28).
[^p4]: Y. Chang 외, J. Song, Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (2024). <https://doi.org/10.1145/3678592> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1145/3678592> (관측 2026-10-28).
[^p5]: O.-K. Kwon 외, J. Song, Proceedings of the International Conference on Parallel Architectures and Compilation Techniques (2022). <https://doi.org/10.1145/3559009.3569657> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1145/3458864.3466626|10.1145/3559009.3569657|10.1145/3653684|10.1145/3678592|10.1145/3831635|10.1145/3831637> (관측 2026-10-28).
[^p6]: W. Kim 외, J. Song, Proceedings of the 19th Annual International Conference on Mobile Systems, Applications, and Services (2021). <https://doi.org/10.1145/3458864.3466626> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1145/3458864.3466626|10.1145/3559009.3569657|10.1145/3653684|10.1145/3678592|10.1145/3831635|10.1145/3831637> (관측 2026-10-28).

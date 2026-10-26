# 웨어러블 로봇 연구실 (Wearable Robotics Laboratory)

**서울대학교 공과대학 전기·정보공학부 · 김진수 조교수**

- 분야: 착용형 로봇, 보행 보조, 생체역학, 로봇 제어와 보조 개인화
- 대분야: 기계·로봇·제조
- 태그: 착용형 로봇·외골격[^home], 재활·보조·접근성 기술[^home], 제어 이론·제어 공학[^research]
- 홈페이지: <https://sites.google.com/snu.ac.kr/jkim>
- 근거와 출처: [웨어러블 로봇 연구실 근거 페이지](wrl-sources.md)

> 사람 몸에 입는 로봇을 만들어 걷기와 달리기를 돕고, 착용자마다 보조 방법을 조정하며 이동 능력의 회복과 향상을 연구한다.

## 무엇을 연구하나

사람의 움직임을 돕는 착용형 로봇을 연구한다. 생체역학(생물의 몸에 작용하는 힘과 그 움직임을 다루는 학문)을 바탕으로, 외골격(몸 바깥에 착용해 움직임을 보조하는 구조)과 엑소수트(의복 형태로 몸에 착용하는 보조 로봇)를 개발한다. 신체 장애인의 건강·이동 능력·자립을 높이고 사람의 운동 수행 능력을 향상하는 것이 목표다.[^home]

연구 소개는 걷기와 달리기에 맞춘 로봇 제어, 사람마다 다른 보조 설정, 보행 장애에 대한 착용형 로봇 적용을 다룬다. 제어기(장치의 움직임이 목표에 맞도록 입력을 정하는 장치나 프로그램)를 설계하고, 착용자가 걷는지 달리는지를 판별해 보조 패턴을 바꾸는 방법을 연구한다.[^research]

개인화 연구에서는 대사율(몸이 단위 시간에 쓰는 에너지)을 추정하면서 보조 설정을 조정한다. 최적화(정해진 조건에서 목표에 가장 맞는 값을 찾는 과정)를 통해 어떤 보조 힘과 시점이 착용자의 에너지 소모를 줄이는지 조사한다. 같은 보조 설정에 대한 사람들의 반응이 다를 수 있다는 점이 출발점이다.[^research]

## 주요 연구 주제

### 걷기와 달리기에 맞춘 보조 제어

하나의 휴대형 로봇으로 걷기와 달리기를 돕기 위해, 두 동작을 구분하는 알고리즘(문제를 처리하기 위한 절차)을 만들고 동작에 맞는 보조 패턴을 적용한다. 연구 소개는 고관절 신전(엉덩관절을 펴는 움직임)을 돕는 엑소수트를 이용한 연구를 설명한다.[^research]

### 착용자별 보조 힘과 제어 방식 비교

김진수 교수의 부임 전 2022년 논문은 고관절 굴곡(엉덩관절을 굽히는 움직임) 보조를 개인별로 조정했다. 외부 장치와 연결된 엑소수트에서 얻은 결과를 바탕으로 휴대형 장치를 설계했으며, 휴대형 장치를 입지 않고 걸을 때와 비교해 에너지 소모 감소를 보였다.[^p2] 부임 전 2023년 사전 공개본은 한 사람을 대상으로 고관절의 좌우 방향 움직임을 돕는 두 제어 방식을 비교했다. 토크(물체를 회전시키려는 힘의 작용)를 조정하는 방식과 관절 위치를 조정하는 방식 모두에서, 최적화한 보조가 보조를 끈 상태보다 대사율을 줄이지 못했다.[^p3]

### 보행 장애에 대응하는 로봇 의복

부임 전 2024년 논문은 케이블로 힘을 전달하는 구동기(에너지를 움직임이나 힘으로 바꾸는 장치)와 센서로 고관절 굴곡을 돕는 로봇 의복을 제시했다. 파킨슨병 환자 한 사람에게서 보행 동결(걷는 도중 발을 앞으로 내딛지 못하는 현상)을 막을 수 있는지 시험한 개념 입증 연구다. 초록은 이 한 사람에게서 얻은 결과와 일상 환경에서 사용할 가능성을 설명한다.[^p1]

## 교수와 전문 분야

김진수 교수는 2024년 3월부터 서울대학교 전기·정보공학부 조교수로 재직한다. 하버드대학교에서 공학과학 전기공학 박사학위를 받았으며, 2022년 7월부터 2024년 1월까지 스탠포드대학교 기계공학부 박사후연구원으로 일했다. 2012년 3월부터 2022년 6월까지 한국과학기술연구원 의공학연구소 바이오닉스연구단 연구원 경력이 있다.[^faculty]

학과는 전문 분야를 로보틱스, 엑소스켈레톤, 생체역학, 제어, 웨어러블로 소개한다. 연구실 소개의 중심도 착용형 로봇 설계와 보조 제어의 개인화다.[^faculty][^research]

## 응용 분야

신체 장애인의 이동과 자립을 돕는 기기, 건강한 사람의 걷기·달리기 능력을 보조하는 착용형 로봇을 목표로 한다.[^home] 파킨슨병 보행 장애 연구는 로봇 의복의 적용 가능성을 탐색하는 단계이며, 부임 전 논문은 환자 한 사람을 대상으로 했다.[^p1]

## 구성원

2026년 10월 26일 Lab Members 페이지에 게시된 교수 외 21명이다. 대학원생 12명, 방문 학생 1명, 학부생·인턴 구획 8명으로 나뉜다. 과정은 누리집 표기를 따른다.[^members]

| 이름 | 과정 |
|---|---|
| Soonho Kwon (권순호) | 석박사통합과정 |
| Seungjoo Noh (노승주) | 석박사통합과정 |
| Junyeop Lee (이준엽) | 석박사통합과정 |
| Minjong Kim (김민종) | 석박사통합과정 |
| Sooyeon Choi (최수연) | 석박사통합과정 |
| Cheolhee Lee (이철희) | 석박사통합과정 |
| Seongmin Seo (서성민) | 석박사통합과정 |
| Yeonjae Jeong (정연재) | 석박사통합과정 |
| Minsu Kim (김민수) | 석박사통합과정 |
| Donghyun Kwon (권동현) | 박사과정 |
| Seonjeong Kim (김선정) | 석사과정 |
| Pranavi Arora | 석사과정 |
| Lilia Ould-Hammou | 방문 학생 (Massachusetts Institute of Technology (MIT), United States) |
| Sungyoon Kim (김승윤) | 학부생 / 인턴 |
| Chungman Kim (김충만) | 학부생 / 인턴 |
| Hyunsik Kim (김현식) | 학부생 / 인턴 |
| Minhong Park (박민홍) | 학부생 / 인턴 |
| Yoonho Shin (신윤호) | 학부생 / 인턴 |
| Jungmin Lim (임정민) | 학부생 / 인턴 |
| Hyeon Joon Jang (장현준) | 학부생 / 인턴 |
| Wonjae Ho (호원재) | 학부생 / 인턴 |

## 졸업생과 이전 구성원

Lab Alumni 페이지의 이전 방문 학생 1명과 학부생·인턴 5명이다. 학위 취득자 명단으로 한정한 표가 아니며, 연도는 게시되어 있지 않다. 진로는 누리집이 적은 학교와 과정을 따른다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hussein Harb | 방문 학생 | Ph.D. Student at the University of Technology of Tarbes (UTTOP), France |
| Hanbin Jang (장한빈) | 학부생 / 인턴 | PhD student at North Carolina State Univ. |
| Jinwoo Hwang (황진우) | 학부생 / 인턴 | MS student at CMU |
| Seungbin Kang (강승빈) | 학부생 / 인턴 |  |
| Sooho Yang (양수호) | 학부생 / 인턴 | MSc student at Univ. of Edinburgh |
| Jiook Chung (정지욱) | 학부생 / 인턴 | PhD student at Purdue Univ. |

## 최근 논문 목록 (2021–2026)

누리집 Selected Publications와 Additional Publications의 2021–2026년 항목 중 초록에서 공학 기여를 확인한 3편이다. 교수의 부임 전 항목이 포함된 목록으로, 아래 3편은 모두 2024년 3월 서울대 부임 전에 출판되었다. 학술지 논문 2편과 사전 공개본 1편을 구분해 적으며, 저자·서지·날짜는 누리집 표기다.[^pubs][^faculty][^p1][^p2][^p3]

**2024**

- Kim, J., Porciuncula, F., Yang, H.D. et al. Soft robotic apparel to avert freezing of gait in Parkinson’s disease. Nat Med 30, 177–185 (2024).

**2023**

- Jinsoo Kim, Michael Raitor, C. Karen Liu, Steven H. Collins, Frontal hip exoskeleton assistance does not appear promising for reducing the metabolic cost of walking: A preliminary experimental study. bioRxiv [Preprint.] Aug. 22, (2023).

**2022**

- Kim, J., Quinlivan, B.T., Deprey, LA. et al. Reducing the energy cost of walking with low assistance levels through optimized hip flexion assistance from a soft exosuit. Sci Rep 12, 11004 (2022).

## 수상과 장학

교수 개인의 Honors and Awards 목록 중 2021년 10월 22일부터 2026년 10월 22일까지에 해당하는 수상·장학 3건이다. 서울대 부임 전인 2022–2023년 항목이 포함되어 있다.[^pi]

- 2025 · 서울대학교 전기·정보공학부 Excellent Teaching Award
- 2025 · 제어·로봇·시스템학회(ICROS) Outstanding Early-Career Researcher Award
- 2022–2023 · Mogam Science Scholarship Foundation의 Mogam Scholarship

## 연락과 위치

- 연구실: 서울특별시 관악구 관악로 1 서울대학교 301동 753-1호, 자동화시스템공동연구소 133동 101·102호[^visit]
- 교수 사무실: 서울대학교 301동 705호[^faculty]
- 전화: 02-880-1823, 팩스: 02-871-5974[^members]
- 이메일: jinskim@snu.ac.kr[^members]

## 각주
[^home]: 연구실 첫 화면. 신체 장애인의 건강·이동·자립, 사람의 수행 능력, 생체역학과 외골격·엑소수트 개발을 연구 목표로 설명한다. <https://sites.google.com/snu.ac.kr/jkim/home> (2026-10-26 열람)
[^research]: 연구실 Research. 동작별 제어기 설계, 걷기·달리기 판별 알고리즘과 보조 패턴 적용, 실시간 대사 소모 추정과 제어 설정 갱신, 개인화 및 제어 방식 비교를 설명한다. <https://sites.google.com/snu.ac.kr/jkim/research> (2026-10-26 열람)
[^faculty]: 서울대학교 전기·정보공학부 김진수 전임교수 소개. 직위·소속, 학력·경력, 전공과 사무실. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p896> (2026-10-26 열람)
[^members]: 연구실 Lab Members. 교수·현재 구성원, 학교 이메일과 연구실 전화. <https://sites.google.com/snu.ac.kr/jkim/people/lab-members> (2026-10-26 열람)
[^alumni]: 연구실 Lab Alumni. 이전 방문 학생과 학부생·인턴, 게시 진로. <https://sites.google.com/snu.ac.kr/jkim/people/lab-members/lab-alumni> (2026-10-26 열람)
[^pubs]: 연구실 Publications. Selected Publications와 Additional Publications의 학술지·학회 논문, 발표와 책 장, 사전 공개본 목록. <https://sites.google.com/snu.ac.kr/jkim/publications> (2026-10-26 열람)
[^pi]: 연구실 Jinsoo Kim 소개. Career와 Honors and Awards. <https://sites.google.com/snu.ac.kr/jkim/people/lab-members/jinsoo-kim> (2026-10-26 열람)
[^visit]: 연구실 Visit the Lab. 두 연구실 공간의 주소. <https://sites.google.com/snu.ac.kr/jkim/contact/visit-the-lab> (2026-10-26 열람)
[^p1]: J. Kim 외, C. J. Walsh, Nature Medicine 30, 177–185 (온라인 2024-01-05). <https://doi.org/10.1038/s41591-023-02731-8> 초록 기준(PubMed 등록 초록). 초록 원문 <https://pubmed.ncbi.nlm.nih.gov/38182783/> (2026-10-26 열람)
[^p2]: J. Kim 외, C. J. Walsh, Scientific Reports 12, 11004 (온라인 2022-06-29). <https://doi.org/10.1038/s41598-022-14784-9> 초록 기준(PubMed 등록 초록). 초록 원문 <https://pubmed.ncbi.nlm.nih.gov/35768486/> (2026-10-26 열람)
[^p3]: J. Kim, M. Raitor, C. K. Liu, S. H. Collins, bioRxiv 사전 공개본 (온라인 2023-08-23). <https://doi.org/10.1101/2023.08.22.554212> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/373349173_Frontal_hip_exoskeleton_assistance_does_not_appear_promising_for_reducing_the_metabolic_cost_of_walking_A_preliminary_experimental_study> (2026-10-26 열람)

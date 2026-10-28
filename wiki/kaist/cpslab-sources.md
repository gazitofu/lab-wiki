# 사이버 물리 시스템 연구실 근거와 출처

## 읽은 자료

| 자료 | 주소 | 관측일 | 사용 범위 |
|---|---|---|---|
| KAIST 전산학부 연구실 소개 | <https://cs.kaist.ac.kr/research/labView?sn=71&menu=64> | 2026-10-27 | 연구실 한글명, 교수, 연구 방향, 전화와 위치 |
| KAIST 전산학부 교수 명단 | <https://cs.kaist.ac.kr/people/faculty> | 2026-10-27 | 신인식 교수의 직위, 전공, 교수연구실 |
| 신인식 교수 상세 소개 | <https://cs.kaist.ac.kr/people/view?idx=15&kind=faculty&menu=160> | 2026-10-27 | 2008년 부임, 학위 칸, 관심 연구 분야 |
| dblp Insik Shin 저자 목록 | <https://dblp.org/pid/45/4154.html> | 2026-10-27 | 2021–2026년 구역의 제목·전체 저자·발표처·DOI, ORCID와 소속 정보 |
| VeriSafe Agent arXiv 초록 | <https://arxiv.org/abs/2503.18492> | 2026-10-27 | 대표 논문 1의 초록 |
| VeriSafe Agent arXiv 본문 | <https://arxiv.org/html/2503.18492v2> | 2026-10-27 | 제목·학회판 DOI의 대응, 신인식 교수의 KAIST 전산학부 소속과 공동 교신저자 표시 |
| OpenAlex 저자 기록 | <https://api.openalex.org/authors?search=Insik%20Shin&per-page=10&select=id,display_name,orcid,works_count,last_known_institutions,affiliations> | 2026-10-27 | ORCID 확인. 여기의 소속 연도는 활동 판정에 쓰지 않았다 |
| OpenAlex ORCID별 논문·초록 | <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0002-9128-2415,publication_year:2021-2026> | 2026-10-27 | 대표 논문 2–8의 등록 초록과 개별 수록 판단. 최근 목록의 범위·연도·발표처에는 쓰지 않았다 |

대표 논문 초록의 개별 주소는 본문 각주에 적었다. OpenAlex 등록 초록은 원 논문의 출판사 게시 초록과 구분했다.

## 이름·직급·위치 표기 차이

학과 연구실 소개의 이름은 「사이버 물리 시스템 연구실」이고 소개 본문은 「CPSLAB」을 쓴다. 학과 소개에는 정식 영문 연구실 이름이 따로 적혀 있지 않아 제목에는 그 약칭을 병기했다. 본래 소속은 전산학부이며, 교수 명단과 상세 소개의 직위 「교수」를 머리 둘째 줄에 옮겼다. 읽은 두 소개에서 다른 학과·대학원의 겸무는 확인되지 않았다.

교수 명단은 교수연구실을 「E3-1, 4425」로, 연구실 소개는 사무실을 「E3-1 4425호」로 적는다. 전화는 연구실 소개의 「042-350-3524」를 썼다. 교수 상세 소개의 학위 칸은 「PhD, Univ of Pennsylvania, 2006」이고 한국어 약력 본문은 대학 이름을 다르게 적으므로, 본문은 학위 칸의 원문 표기를 인용했다.

연구실 소개의 독립 누리집 주소 <http://cps.kaist.ac.kr/>는 2026-10-27 도메인 이름이 해석되지 않았다. 본문 홈페이지에는 학과 연구실 소개 주소를 썼다. 교수 상세 소개가 가리키는 같은 도메인의 개인 페이지는 읽지 않았다.

## 현재 활동과 동일인 판단

교수 상세 소개는 2008년 KAIST 부임과 현재 재직을 적는다. 여기에 2025년 9월 11일 판 VeriSafe Agent 원문이 Insik Shin을 「School of Computing, KAIST, Republic of Korea」 소속이자 공동 교신저자로 명시하는 점을 함께 보아 연구 활동이 이어지는 것으로 판단했다. 교수 명단 등재만으로 활동을 판정하지 않았다.

dblp의 Insik Shin 저자 목록에는 KAIST 소속 분류와 ORCID 「0000-0002-9128-2415」가 보이고, OpenAlex에서 고른 저자 기록의 ORCID와 일치한다. Sunjae Lee·Sangeun Oh·Jinkyu Lee 등 공저자 연결도 같은 목록에서 확인했다. dblp는 소속 자료가 불완전하다고 안내한다. 소속 분류의 건수를 최근 KAIST 논문 수로 쓰지 않았다. 최근 목록은 이 교수의 KAIST 재직 기간에 해당하는 저자 기록이며, 각 논문의 전체 저자 소속을 모두 따로 대조한 목록은 아니다.

## 대표 논문을 고른 이유

| 번호 | 논문 | 선정 이유 | 초록 출처와 저자 역할 |
|---|---|---|---|
| 1 | VeriSafe Agent (2025) | 모바일 AI 동작의 실행 전 검증을 다루는 최신 논문 | arXiv 초록. 학회 DOI와 같은 제목·저자를 원문에서 확인. 마지막 저자이며 공동 교신저자 명시 |
| 2 | MobileGPT (2024) | 앱 작업 절차를 배우고 기억해 재사용하는 언어 모델 기반 자동화 | OpenAlex 등록 초록. dblp DOI 일치. 마지막 저자 |
| 3 | FLUID-IoT (2024) | 공유 기기의 화면 구성 요소별 접근 제어와 사용자 경험 | OpenAlex 등록 초록. dblp DOI 일치. 마지막 저자 |
| 4 | EarDVFS (2025) | 기기·주변 환경에 적응하는 강화학습 기반 전력 제어 | OpenAlex 등록 초록. dblp DOI 일치. 마지막 저자 |
| 5 | MixMax (2023) | 이종 배터리의 구성과 충방전 정책을 함께 최적화 | OpenAlex 등록 초록. dblp DOI 일치. 마지막 저자 |
| 6 | LaLaRAND (2021) | 신경망 층별 CPU·GPU 배분과 시간 보장 | OpenAlex 등록 초록. dblp DOI 일치. 전체 5명 중 4번째 저자 |
| 7 | RT-SDN (2022) | 경로와 우선순위를 함께 정하는 실시간 통신 | OpenAlex 등록 초록. dblp DOI 일치. 전체 3명 중 2번째 저자 |
| 8 | OZZ (2024) | 커널의 비순차 실행과 동시 실행이 결합한 오류 검사 | OpenAlex 등록 초록. dblp DOI 일치. 전체 5명 중 4번째 저자 |

대표 논문 8편의 초록 출처는 arXiv 1편, OpenAlex 등록 초록 7편이다. 1번을 제외한 교신저자 역할은 저자 순서로 추정하지 않았다. OpenAlex와 dblp 사이의 저자 철자 차이(Steve Ko와 Steven Y. Ko 등)는 최근 목록·대표 논문 서지를 dblp 표기로 유지해 구분했다. RT-SDN의 등록 초록 자료는 온라인 연도를 2021년으로 적지만, 목록과 대표 논문 표는 dblp 권호 연도인 2022년을 썼다.

S-UbiTap의 dblp 제목에는 수식 원문과 같은 이름의 문자 표기가 함께 보인다. 최근 목록은 그 제목 표기를 그대로 유지했다.

## 확인한 범위와 확인하지 못한 점

dblp 전체 저자 목록은 127개 기록을 표시한다. 2021–2026년 구역에는 2021년 6개, 2022년 7개, 2023년 9개, 2024년 5개, 2025년 6개로 총 33개 기록이 있고 2026년 항목은 없다. 학술지·학회 논문, 책 장, CoRR 사전 공개본을 모두 살폈다. 이 가운데 「Message from the Program, Track, and General Chairs」(RTSS 2023)는 등록 초록이 참가자를 환영하는 의장 인사말이므로 연구 논문 목록에서 제외했다. 최종 수록은 2021년 6개, 2022년 7개, 2023년 8개, 2024년 5개, 2025년 6개로 32개 기록이다. 유형별로는 학술지 6개, 학회 19개, 책 장 1개, 사전 공개본 6개다. 이는 판본을 통합한 고유 연구 수가 아니다.

사전 공개본 중 「mCardiacDx: Radar-Driven Contactless Monitoring and Diagnosis of Arrhythmia」는 같은 DOI의 등록 초록에서 반사 신호 위치 추정과 심장 맥파 복원 기법을 새로 제안하는 공학 기여를 확인해 포함했다. 「Machine Learning with Electronic Health Records is vulnerable to Backdoor Trigger Attacks」도 같은 DOI의 등록 초록에서 기계학습 모델의 취약성을 시험하는 새 공격 방법을 제시해 포함했다. 의생명 인접 항목에서 제외한 기록은 없다. 본문에 실험 대상자의 조건이나 공격 절차 세부는 옮기지 않았다.

OpenAlex의 ORCID별 자료는 2021–2026년 32개 기록과 초록 29개를 담지만, 이 수를 dblp 목록의 총수로 사용하지 않았다. 2026년 mCardiacDx 학술지판 등 dblp의 해당 연도 구역에 없는 기록은 최근 목록에 추가하지 않았다. 제목이 달라진 사전 공개본과 학술지판의 초록을 서로 바꾸어 쓰지 않았다. 대표 논문 1은 arXiv 본문에 학회판 제목·DOI가 함께 있고 저자도 일치한다.

연구실 소개의 Mobile Maestro·GreenBag·멀티코어 스케줄링 사례는 각각 2014년·2013년·2012년으로 적혀 있어 최근 성과 목록에 싣지 않았다. 교수 약력의 수상은 2019년 이전이므로 최근 수상 절을 만들지 않았다. 읽은 자료에서는 현재 구성원·졸업생 명단과 최근 과제·특허·수상·소식 목록을 확정할 자료를 얻지 못해 해당 절을 만들지 않았다. 논문 공저자라는 이유로 구성원으로 넣지 않았다.

학과 연구실 소개 원문, 교수 명단 원문, 교수 상세 소개의 본문에는 이메일 수집 거부 문장이 보이지 않았다. 연구실 소개의 이메일은 본문에 주소가 표시되지 않고 스크립트에 기호형으로 적혀 있어 싣지 않았다. 논문의 저자 연락처를 구성원 명단으로 옮기지도 않았다.

태그는 태그 어휘 1.7판(2026-10-27)의 이름을 썼다. 프로그램 분석·검증은 VeriSafe Agent와 OZZ의 검사 방법, 컴퓨터 구조·운영체제와 소프트웨어·시스템 보안은 OZZ 및 실시간 계산 자원 배분, 컴퓨터 네트워크는 RT-SDN, 인간–컴퓨터 상호작용은 FLUID-IoT의 화면 분배와 사용성 평가, 대형 언어 모델은 MobileGPT, 강화학습은 EarDVFS의 초록에 근거한다. 배터리 시스템을 연구한다는 이유로 배터리 소재 태그를 붙이지 않았다.

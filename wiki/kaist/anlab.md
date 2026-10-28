# 첨단 네트워킹 연구실 (Advanced Networking Laboratory, ANLAB)

**KAIST 전산학부 · 문수복 교수**

- 분야: 고속 네트워킹 소프트웨어, 분리형 데이터센터의 통신과 보안, 온라인 소셜 네트워크와 도덕 감정 분석
- 대분야: 컴퓨팅·AI, 인문·사회·경제
- 태그: 컴퓨터 네트워크[^home][^p3][^p5], 네트워크 보안·프라이버시[^p1], 계산 사회과학[^p2], 멀티모달 AI[^p2]
- 홈페이지: <https://an.kaist.ac.kr/>
- 근거와 출처: [ANLAB 근거 페이지](anlab-sources.md)

> 컴퓨터와 데이터센터의 통신을 맡는 소프트웨어·시스템을 연구하고, 온라인 소셜 네트워크에서는 도덕 감정과 혐오 표현, 이용자의 참여 행동을 분석하는 연구실이다.[^home][^p2]

## 무엇을 연구하나

문수복 교수의 첨단 네트워킹 연구실은 고속 네트워킹과 온라인 소셜 네트워크라는 두 갈래를 다룬다. 네트워킹은 컴퓨터 사이에서 데이터를 주고받게 하는 기술이며, 연구실은 오늘날과 미래 인터넷의 동작을 지배하는 원리를 밝히는 것을 지향한다. 학과 소개는 네트워크 플랫폼과 온라인 사용자 사이의 상호작용을 실험과 이론 양쪽에서 연구한다고 설명한다.[^home][^lab]

네트워킹 쪽에서는 **재사용 가능한 네트워크 스택**을 만든다. 네트워크 스택은 통신 규약을 여러 층으로 나누어 구현한 소프트웨어 묶음이다. NIC(Network Interface Card, 네트워크 인터페이스 카드)와 이를 다루는 개발 도구가 바뀔 때마다 소프트웨어를 새로 만드는 문제에 대응해, 핵심 기능을 유지하면서 새 장치에 맞추는 부분을 분리하는 구조를 지향한다. 프로그래밍 언어 Rust로 이를 구현하고 기존 C/C++ 구현과 경쟁할 수 있는 성능을 보이는 것이 연구 목표다.[^home] 호스트(통신에 참여하는 컴퓨터)의 패킷(전송을 위해 나눈 데이터 단위) 처리에서는 CPU 동작 주파수(단위 시간에 되풀이하는 동작의 횟수)가 성능과 전력 소비에 미치는 영향도 분석했다. CPU의 코어(프로그램 명령을 처리하는 부분)와 언코어(코어 밖에서 메모리 접근 등을 지원하는 부분)를 나누어 살폈고, 언코어 주파수를 제한하면 처리 성능 저하를 수반하면서 소비 전력을 줄일 수 있다고 보고했다.[^p3]

다른 축은 **분리형 데이터센터**다. 데이터센터는 서버와 통신·저장 장치를 모아 운영하는 시설이다. 연구실은 CPU(Central Processing Unit, 중앙처리장치), GPU(Graphics Processing Unit, 그래픽처리장치), 메모리(계산에 쓰는 자료와 명령을 저장하는 장치), 저장 장치를 각각 자원 묶음으로 구성하는 환경의 통신과 분산 시스템을 연구한다. 분산 시스템은 여러 컴퓨터가 연결되어 작업을 수행하는 시스템이다. 대표 논문에서는 RDMA(Remote Direct Memory Access, 원격 직접 메모리 접근) 통신에 암호화와 변조 확인 기능을 더하고, 암호 계산을 네트워크 카드에 맡기는 오프로딩(처리 작업을 다른 장치로 넘기는 것)의 조건을 살폈다. CPU 계산과 카드의 암호 계산을 겹쳐 수행하는 것이 성능상 이점을 얻는 데 중요하다고 보고했다.[^home][^p1] DiLOS는 라이브러리 운영체제(응용 프로그램에 필요한 운영체제 기능을 함께 구성하는 방식)로 원격 메모리 사용을 지원한다. 페이지 폴트(메모리의 해당 부분이 준비되지 않았거나 접근 권한에 문제가 있어 운영체제의 처리가 필요한 상황)를 다루는 경로와 메모리 관리를 바꾸고, 응용 프로그램의 특성을 활용할 수 있게 했다.[^p4] 클라우드용 메모리 분리 연구는 요청 일부가 오래 걸리는 꼬리 지연을 줄이기 위한 예비 해법을 제안했고,[^p6] RDMA를 왕복 시간(자료가 상대에게 갔다가 응답이 돌아오기까지의 시간)이 긴 통신 경로에서 쓰는 가능성도 분석했다.[^p5]

온라인 소셜 네트워크 쪽에서는 **대화 맥락에서 혐오 표현이 발생하는 계기**를 찾는다. 도덕과 감정이 혐오 표현 발생과 어떤 관계인지 분석하며, 이미지와 글 등 여러 종류의 자료를 함께 쓰는 멀티모달 분석과 이용할 자료가 부족한 언어도 연구 대상이다. 대표 논문은 유튜브 뉴스의 제목과 대표 이미지에 담긴 도덕 감정이 조회·좋아요·댓글과 어떤 관계인지 한국과 미국에서 분석했다. 글과 이미지를 함께 다루는 비전-언어 모델을 조정해 도덕 감정을 분류했으며, 타인을 도덕적으로 비난하는 분노 표현이 두 문화권에서 이용자 참여 증가와 연결된다는 결과를 제시했다.[^home][^p2]

## 주요 연구 주제

### 1. 재사용 가능한 네트워킹 소프트웨어

새 통신 장치가 도입되어도 핵심 통신 기능을 유지할 수 있는 소프트웨어 구조를 연구한다. NIC와 개발 도구에 맞추는 층을 분리하고, Rust 구현으로 성능을 검증하는 것이 목표다. 호스트 패킷 처리의 CPU 주파수와 전력 소비를 분석하고, RDMA를 왕복 시간이 긴 경로에서 사용하는 방법도 살핀다.[^home][^p3][^p5]

### 2. 분리형 데이터센터와 통신 보안

계산 장치와 메모리 등을 자원 묶음으로 구성하는 데이터센터의 네트워킹·분산 시스템 문제를 다룬다. RDMA 데이터 경로에서 기밀성(내용을 권한 없는 사람이 알 수 없게 하는 성질)과 무결성(자료가 부당하게 바뀌지 않은 성질)을 지키면서, CPU와 네트워크 카드 사이의 작업 분담을 설계한다. DiLOS의 원격 메모리 관리와 클라우드 응용의 꼬리 지연을 줄이는 예비 해법도 이 갈래에 속한다.[^home][^p1][^p4][^p6]

### 3. 온라인 도덕 감정과 이용자 행동

온라인 대화의 도덕·감정과 혐오 표현의 관계를 분석한다. 유튜브 뉴스 연구에서는 비전-언어 모델로 이미지와 제목을 함께 분류하고, 도덕적 분노와 조회·좋아요·댓글의 관계를 비교했다.[^home][^p2]

## 대표 논문

네트워킹 소프트웨어·분리형 데이터센터·온라인 소셜 네트워크 분석을 보여 주는 논문과 포스터 6편을 골랐다. '쉽게 말하면' 칸은 각 논문의 OpenAlex 등록 초록만을 근거로 썼다. 포스터는 제목의 표시를 유지했다.

| 번호 | 연도 | 논문 · 발표처 | 쉽게 말하면 | 교수 역할 |
|---|---|---|---|---|
| 1 | 2025 | [Secure and Efficient RDMA NIC Cryptography Offloading for Memory Disaggregation](https://doi.org/10.1145/3768991) · Proceedings of the ACM on Networking | 원격 메모리를 이용하는 RDMA 통신에서 데이터를 암호화하고 체크섬(자료 변경을 확인하기 위한 검사값)으로 변경을 확인하는 데이터 경로를 설계했다. 암호 계산을 네트워크 카드에 맡기면서 키 설정과 요청 묶음, 처리 상태의 재사용을 관리하는 방법을 더했다. 단순한 작업 이관은 성능을 떨어뜨릴 수 있으며, CPU 계산과 카드의 암호 계산을 겹쳐 수행해야 이점을 얻는다고 보고했다.[^p1] | 전체 저자 2명 중 2번째 |
| 2 | 2026 | [Moral Outrage Shapes Commitments Beyond Attention: Multimodal Moral Emotions on YouTube in Korea and the US](https://doi.org/10.1145/3774904.3792728) · WWW 2026 | 뉴스 채널의 유튜브 제목과 대표 이미지를 함께 읽는 도덕 감정 분류기를 만들고, 한국어와 영어 자료에서 감정 표현과 조회·좋아요·댓글의 관계를 분석했다. 타인을 도덕적으로 비난하는 분노 표현은 한국과 미국 모두에서 이용자 참여 증가와 연결되었다. 한국어·영어 분류기를 공개하고, 이런 표현이 집단 간 구분과 양극화를 심화시킬 가능성도 논의했다.[^p2] | 전체 저자 6명 중 5번째 |
| 3 | 2026 | [Fast but Wasteful: Power Analysis and Implications of Host Networking](https://doi.org/10.1145/3786287) · Proceedings of the ACM on Networking | 데이터센터 통신을 처리하는 컴퓨터의 CPU 주파수 조절이 통신 성능과 전력 소비에 미치는 영향을 분석했다. 리눅스 통신 소프트웨어와 RDMA를 살피고 코어와 언코어를 구분했다. 언코어가 높은 주파수로 동작하며 전력 소비에 상당히 기여하고, 코어 주파수 제어도 적절하지 않은 결정을 내릴 수 있음을 보였다. 언코어 주파수 제한으로 처리 성능 저하를 수반하면서 전력 소비를 줄였으며, RDMA에서도 언코어 전력 소비를 살펴야 한다고 보고했다.[^p3] | 전체 저자 2명 중 2번째 |
| 4 | 2023 | [DiLOS: Do Not Trade Compatibility for Performance in Memory Disaggregation](https://doi.org/10.1145/3552326.3567488) · EuroSys 2023 | 계산 장치와 메모리를 분리한 환경에서 기존 프로그램을 그대로 실행할 수 있는 페이지 방식의 성능 문제를 다룬다. 이를 위한 라이브러리 운영체제 DiLOS를 제안하고, 페이지 폴트 처리에서 스왑 캐시(교체한 메모리 페이지를 관리하는 임시 저장 구조)를 제거했다. 선반입(필요할 자료를 미리 가져오는 것), 메모리 관리, 통신 모듈도 손보고 응용 프로그램의 특성을 활용하는 기능을 제공했다. 실제 데이터 분석 작업에서 비교한 기존 시스템들보다 높은 성능을 보였다고 보고했다.[^p4] | 전체 저자 5명 중 4번째 |
| 5 | 2024 | [Poster: Pushing RDMA into Milliseconds RTT Communication](https://doi.org/10.1145/3680121.3699883) · CoNEXT (Short Papers) 2024 | RDMA가 데이터센터 안에서 제공하는 성능·효율의 이점을 왕복 시간이 긴 통신 경로에서도 유지할 수 있는지 묻는다. 왕복 시간이 긴 경로에서 RDMA 통신의 가능성을 살피기 위한 방법과 분석을 제시한 포스터다.[^p5] | 전체 저자 3명 중 3번째 |
| 6 | 2023 | [Poster: Designing a Memory Disaggregation System for Cloud](https://doi.org/10.1145/3603269.3610854) · SIGCOMM 2023 | 메모리 분리 시스템 내부의 처리 최적화만으로 클라우드 응용의 성능을 보장할 수 없고, 일부 요청이 오래 걸리는 꼬리 지연이 문제가 된다는 데서 출발한다. 기존 메모리 분리 시스템과 지연을 줄이는 시스템의 한계를 검토하고, 비동기 페이지 폴트 처리(요청의 완료를 기다리는 동안 다른 작업을 진행할 수 있게 하는 처리)와 요청 분류기를 예비 해법으로 제안했다. 모사 실험에서 비동기 처리가 동기 처리보다 꼬리 지연을 줄였다고 보고했다.[^p6] | 전체 저자 4명 중 3번째 |

## 교수와 전문 분야

문수복 교수는 서울대학교 컴퓨터공학 학사·석사, University of Massachusetts at Amherst 전산학 박사 학위를 받았으며 2003년 8월 KAIST에 부임했다. 학과는 전문 분야를 네트워크 플랫폼과 온라인 소셜 네트워크로 적고, 교수 소개는 네트워크 성능 측정·분석과 네트워크 시스템을 주요 연구 분야로 설명한다.[^faculty][^prof]

최근 논문에서 확인되는 전문 분야는 원격 메모리 통신의 보안·처리 구조, 호스트 네트워킹의 성능·전력 분석, 온라인 도덕 감정의 계산 분석이다. 네트워크 카드와 CPU의 역할 분담, 응용 프로그램을 고려한 메모리 관리, 여러 종류의 자료로 사회적 표현과 행동을 분석하는 방법을 함께 다룬다.[^p1][^p2][^p3][^p4]

## 응용 분야

연구 대상은 데이터센터의 고속 통신과 자원 분리 구조, 원격 메모리 통신의 데이터 보호, 온라인 혐오 표현의 맥락 분석과 뉴스 이용자의 참여 행동이다. 도덕 감정 연구는 타인 비난 표현이 집단 간 구분을 강화해 양극화를 심화시킬 가능성도 논의한다.[^home][^p1][^p2]

## 구성원

2026-10-27 누리집 Members의 Students 칸에 게시된 9명이다. 과정·연구 관심은 랩 표기이며, Seongkyu Lee는 Lab Leader로도 적혀 있다. 교수는 Sue Bok Moon, Lab Advisor로 게시되어 있다.[^members]

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Seongkyu Lee | 박사과정 | NPU |  |
| Minseok Kim | 박사과정 | TBD |  |
| Gangmin Lee | 박사과정 | NPU Scheduling |  |
| Junmo Chung | 석사과정 | QUIC |  |
| Seongjun Im | 석사과정 | RDMA |  |
| Junseo Yu | 석사과정 | Social Computing |  |
| Osman Berkay Artac | 석사과정 | NPU |  |
| MoonJung Kim | 석사과정 | SmartNIC |  |
| Kyoung Wan Min | 학부생 | TBD |  |

## 졸업생 진로

Members의 Alumni에 적힌 졸업생 가운데 학위 연도가 2021–2026년인 9명이다. 학위·연도·진로는 누리집 표기다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jisu Ok | Ph.D. (2026) |  |
| Wonsup Yoon | Ph.D. (2025) | Assistant Professor, Department of Computer Science, Hanyang University, South Korea |
| SoonHyeon Kwon | MS (2025) | KOG Corporation, South Korea |
| Keunhong Lee | Ph.D. (2025) | FuriosaAI, South Korea |
| DongHyeon Lee | MS (2024) | Toss Bank, South Korea |
| Byeongkeon Lee | MS (2023) | NHN Cloud, South Korea |
| Heeju Wi | MS (2022) | Kakao Corp., South Korea |
| Jiwan Jeong | Ph.D. (2021) | Tech Leader / Data Scientist, Naver Corp, South Korea |
| Jaeseok Huh | MS (2021) | Bear Robotics, South Korea |

## 최근 논문 목록 (2021–2026)

원격 메모리·데이터센터 통신, 네트워킹 자원 사용, 온라인 도덕 감정 등을 다룬 논문과 포스터다. dblp 교수 서지의 2021–2026년 항목 중 학술지 2편, 학회·워크숍 6편, 포스터 2편으로 총 10편이다. 연도·제목·저자·발표처는 해당 서지 표기다. 같은 논문의 arXiv 사전 공개본은 학회판과 한 줄로 합쳤다.[^dblp][^versions]

**2026**

- Jisu Ok , Sue Moon. "Fast but Wasteful: Power Analysis and Implications of Host Networking". *PACMNET 4(CoNEXT1) : 4:1-4:15 ( 2026 )*.
- Gangmin Lee , Wonsup Yoon , Sue Moon. "SwiftNPU: Scalable Shape-Flexible Allocation for Inter-Core Connected NPUs". *EuroMLSys@EuroSys 2026 : 23-30*.
- Seongchan Park , Jaehong Kim , Hyeonseung Kim , Heejin Bin , Sue Moon , Wonjae Lee. "Moral Outrage Shapes Commitments Beyond Attention: Multimodal Moral Emotions on YouTube in Korea and the US". *WWW 2026 : 7657-7668*.

**2025**

- Wonsup Yoon , Sue Moon. "Secure and Efficient RDMA NIC Cryptography Offloading for Memory Disaggregation". *Proc. ACM Netw. 3(CoNEXT4) : 1-13 ( 2025 )*.
- Wonsup Yoon , Jisu Ok , Sue Moon , Youngjin Kwon. "Adios to Busy-Waiting for Microsecond-scale Memory Disaggregation". *EuroSys 2025 : 870-885*.

**2024**

- Jisu Ok , Wonsup Yoon , Sue Moon. "Poster: Pushing RDMA into Milliseconds RTT Communication". *CoNEXT (Short Papers) 2024 : 19-20*.

**2023**

- Byeongkeon Lee , Donghyeon Lee , Jisu Ok , Wonsup Yoon , Sue Moon. "Host Efficient Networking Stack Utilizing NIC DRAM". *APNet 2023 : 8-14*.
- Wonsup Yoon , Jisu Ok , Jinyoung Oh , Sue Moon , Youngjin Kwon. "DiLOS: Do Not Trade Compatibility for Performance in Memory Disaggregation". *EuroSys 2023 : 266-282*.
- Wonsup Yoon , Jisu Ok , Sue Moon , Youngjin Kwon. "Poster: Designing a Memory Disaggregation System for Cloud". *SIGCOMM 2023 : 1099-1101*.

**2021**

- Wonsup Yoon , Jinyoung Oh , Jisu Ok , Sue B. Moon , Youngjin Kwon. "DiLOS: adding performance to paging-based memory disaggregation". *APSys 2021 : 70-78*.

## 수상과 선정

교수 누리집에 2022–2023년으로 게시된 수상·선정 3건이다.[^prof]

- 2023 · Best Paper Award at ACM SIGCOMM APNet
- 2022 · ACM SIGCOMM Internet Measurement Conference Test of Time Award
- 2022 · Full Member at National Academy of Engineering in Korea

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291 KAIST IT융합빌딩(N1) 621호, 교수 연구실 608호. 우편번호 34141.[^home][^contact]
- 연구실 전화: +82-42-350-7748.[^contact]
- 교수 전화: +82-42-350-3548.[^prof]
- 교수 이메일: sbmoon@kaist.edu.[^contact]
[^home]: ANLAB 첫 화면, 연구 소개와 위치. <https://an.kaist.ac.kr/> 관측일 2026-10-27.
[^lab]: KAIST 전산학부 첨단 네트워킹 연구실 소개. <https://cs.kaist.ac.kr/research/labView?sn=63&menu=64> 관측일 2026-10-27.
[^faculty]: KAIST 전산학부 문수복 교수 소개와 교수진 명단. <https://cs.kaist.ac.kr/people/view?idx=10&kind=faculty&menu=160> <https://cs.kaist.ac.kr/people/faculty> 관측일 2026-10-27.
[^prof]: Sue Bok Moon 교수 누리집, 약력·전문 분야·수상·연락처. <https://an.kaist.ac.kr/~sbmoon/> 관측일 2026-10-27.
[^members]: ANLAB Members, Professor·Students·Alumni. <https://an.kaist.ac.kr/members/> 관측일 2026-10-27.
[^contact]: ANLAB Contact, 연락처와 위치. <https://an.kaist.ac.kr/contact/> 관측일 2026-10-27.
[^dblp]: dblp Sue B. Moon, KAIST 소속·ORCID·저자 누리집 연결과 2021–2026년 전체 연도 구역. <https://dblp.org/pid/m/SueBMoon.html> 관측일 2026-10-27.
[^versions]: 같은 제목과 전체 저자 순서의 arXiv:2601.21815v2는 The Web Conference 2026 채택을 밝힌다. <https://arxiv.org/abs/2601.21815> 관측일 2026-10-27.
[^p1]: W. Yoon, S. Moon, Proceedings of the ACM on Networking 3, 1-13 (2025). <https://doi.org/10.1145/3768991> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0002-5692-1111,publication_year:2021-2026> 관측일 2026-10-27.
[^p2]: S. Park 외, W. Lee, WWW 2026, 7657-7668 (2026). <https://doi.org/10.1145/3774904.3792728> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0002-5692-1111,publication_year:2021-2026> 관측일 2026-10-27.
[^p3]: J. Ok, S. Moon, Proceedings of the ACM on Networking 4, 4:1-4:15 (2026). <https://doi.org/10.1145/3786287> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0002-5692-1111,publication_year:2021-2026> 관측일 2026-10-27.
[^p4]: W. Yoon 외, Y. Kwon, EuroSys 2023, 266-282 (2023). <https://doi.org/10.1145/3552326.3567488> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0002-5692-1111,publication_year:2021-2026> 관측일 2026-10-27.
[^p5]: J. Ok, W. Yoon, S. Moon, CoNEXT (Short Papers) 2024, 19-20 (2024). <https://doi.org/10.1145/3680121.3699883> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0002-5692-1111,publication_year:2021-2026> 관측일 2026-10-27.
[^p6]: W. Yoon, J. Ok, S. Moon, Y. Kwon, SIGCOMM 2023, 1099-1101 (2023). <https://doi.org/10.1145/3603269.3610854> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0002-5692-1111,publication_year:2021-2026> 관측일 2026-10-27.

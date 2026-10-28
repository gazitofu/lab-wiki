# 첨단 네트워킹 연구실 근거와 출처

## 읽은 자료

문서의 근거로 사용한 주소는 아래 10곳이다. 관측일은 한국 시각 2026-10-27이다.

| 자료 | 주소 | 본문에 쓴 범위 |
|---|---|---|
| ANLAB 첫 화면 | <https://an.kaist.ac.kr/> | 영문 이름, 통신 스택·분리형 데이터센터·혐오 표현 연구, 위치 |
| Members | <https://an.kaist.ac.kr/members/> | 교수, 학생, 졸업생의 이름·과정·연구 관심·진로 |
| Contact | <https://an.kaist.ac.kr/contact/> | 일반 주소로 게시된 학교 이메일, 주소·전화 |
| 교수 누리집 | <https://an.kaist.ac.kr/~sbmoon/> | 부임·학력·전문 분야, 수상·선정, 교수 전화 |
| 전산학부 연구실 소개 | <https://cs.kaist.ac.kr/research/labView?sn=63&menu=64> | 국문 이름, 소속·교수 연결, 연구 분야 |
| 전산학부 교수진 명단 | <https://cs.kaist.ac.kr/people/faculty> | 문수복 교수의 이름·직위·교수 연구실 |
| 전산학부 교수 소개 | <https://cs.kaist.ac.kr/people/view?idx=10&kind=faculty&menu=160> | 전공·학력·KAIST 부임 |
| dblp 교수 서지 | <https://dblp.org/pid/m/SueBMoon.html> | KAIST 소속·ORCID·저자 누리집 연결, 2021–2026년 연도 구역 |
| OpenAlex 등록 자료 | <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0002-5692-1111,publication_year:2021-2026> | 대표 논문 6편의 등록 초록 |
| arXiv 논문 페이지 | <https://arxiv.org/abs/2601.21815> | 동일 제목·전체 저자의 사전 공개본과 The Web Conference 2026 채택 관계 |

## 이름·직급·위치 표기 차이

학과 연구실 소개의 국문명은 「첨단 네트워킹 연구실」이고 누리집은 Advanced Networking Laboratory, ANLAB으로 적는다. 본문 제목에 두 이름을 함께 썼다. 교수의 국문 이름·직위는 학과 명단과 교수 소개의 「문수복 교수」를 따랐다. Members와 교수 누리집은 Sue Bok Moon으로, dblp는 Sue B. Moon과 Sue Moon을 같은 저자 페이지에 적는다. dblp가 KAIST 소속, ORCID 0000-0002-5692-1111, 연구실 도메인의 교수 누리집을 함께 제시하므로 같은 교수로 판단했다. OpenAlex의 저자 이름 표기를 본문 서지에 덮어쓰지 않고 dblp 저자 순서를 유지했다.

학과 연구실 소개는 N1 621호, 교수 소개는 N1 608호로 적는다. 첫 화면·Contact는 학생 연구실 621호와 교수 연구실 608호로 나누어 설명하므로 본문도 구분했다. 교수 누리집 연락처 본문에는 예전 우편번호 305-701이 있지만, 첫 화면·Contact·교수 누리집 하단에는 34141이므로 주소에는 34141을 썼다. 연구실 전화와 교수 전화도 구분했다.

첫 화면과 교수 누리집의 이메일은 기호형이라 싣지 않았다. Contact에 일반 주소로 게시된 학교 이메일만 사용했다. 첫 화면·Contact·교수 누리집·Members·학과 명단·학과 교수 소개·학과 연구실 소개를 페이지별로 살폈으며 이메일 무단 수집 거부 문장은 이 페이지들에서 발견되지 않았다. Members의 행정 직원은 구성원 표에서 제외했다.

## 대표 논문을 고른 이유

| 번호 | 논문 | 선정 이유와 교수 역할 |
|---|---|---|
| 1 | Secure and Efficient RDMA NIC Cryptography Offloading for Memory Disaggregation | 통신 보안과 원격 메모리 시스템의 작업 분담을 연결한다. 전체 저자 2명 중 마지막이다. |
| 2 | Moral Outrage Shapes Commitments Beyond Attention: Multimodal Moral Emotions on YouTube in Korea and the US | 온라인 도덕 감정·이용자 참여를 여러 종류의 자료로 분석한다. 전체 저자 6명 중 5번째다. |
| 3 | Fast but Wasteful: Power Analysis and Implications of Host Networking | 호스트 네트워킹의 성능과 전력 소비, CPU 주파수를 함께 분석한다. 전체 저자 2명 중 마지막이다. |
| 4 | DiLOS: Do Not Trade Compatibility for Performance in Memory Disaggregation | 응용 프로그램 호환성을 유지하는 원격 메모리 시스템 설계를 보여 준다. 전체 저자 5명 중 4번째다. |
| 5 | Poster: Pushing RDMA into Milliseconds RTT Communication | RDMA를 왕복 시간이 긴 경로로 확장할 가능성을 살피는 포스터다. 전체 저자 3명 중 마지막이다. |
| 6 | Poster: Designing a Memory Disaggregation System for Cloud | 클라우드 응용의 꼬리 지연을 줄이기 위한 예비 해법을 제안한 포스터다. 전체 저자 4명 중 3번째다. |

초록 출처는 6편 모두 OpenAlex 등록 초록이다. 제목이 dblp 행과 같은 항목을 사용했고, DOI의 시작 부분이 dblp에 표시된 DOI와 일치하는지도 대조했다. 전체 DOI 문자열은 등록 초록의 식별값을 사용했다. 학술지·학회 이름, 연도·쪽과 저자 순서는 dblp 기록을 따랐다. 교신·책임저자 여부는 저자 순서로 판정하지 않았다.

SwiftNPU, Adios, Host Efficient Networking Stack의 제공된 등록 초록은 배경과 기존 방식의 한계까지 설명한다. 이 부분만으로 제안 방식·결과를 덧붙이지 않았고, 대표 논문은 내용 설명이 가능한 다른 논문과 포스터로 골랐다. 이 세 편은 최근 서지 목록에는 포함한다.

## 확인한 범위와 확인하지 못한 점

현재 연구실 활동은 Members의 학생 게시, 첫 화면의 현재 연구 설명, 교수 소개의 현직 교수 표기로 확인했다. 문수복 교수는 2003년 8월 KAIST에 부임했으며 최근 서지 목록은 그 이후 연구다.

첫 화면의 Publications는 Google Scholar 교수 페이지를 가리킨다. 최근 논문 목록은 dblp 교수 서지를 기준으로 정했다. 이 목록이 국내외 전체 연구 성과를 망라한다는 뜻은 아니다.

dblp의 2021–2026년 표시 항목은 11건이다. 2026년 4건, 2025년 2건, 2024년 1건, 2023년 3건, 2021년 1건이며, 2023년 구역 다음에 2021년 구역이 이어진다. 학술지 2편, 학회·워크숍 6편, 포스터 2편, CoRR 사전 공개본 1건이다. 이 기간에 편집·위원회 기록과 교수가 저자가 아닌 기록은 없다. 페이지 하단 갱신 표시는 2026-09-29이며 이 기간 구역에 2027년 권호는 없다.

Moral Outrage의 학회판과 CoRR는 제목·전체 저자 순서가 일치한다. arXiv 페이지가 같은 논문의 The Web Conference 2026 채택을 밝히므로, 최근 목록에서는 학회판 한 줄로 합쳤다. 따라서 본문의 최근 논문은 10편이며 대표 논문도 학회판을 설명한다. 포스터 2편은 제목의 Poster 표시를 유지했다. 2021년 논문은 논문 목록의 연도 구역 기준으로 포함했다.

OpenAlex의 ORCID 기준 자료에는 17건이 있다. 같은 제목의 학회판·사전 공개본·소프트웨어 항목과 과거 학회 논문에 최근 등록 날짜가 붙은 항목이 섞여 있으므로, 이 자료는 초록 출처로만 사용했다. OpenAlex의 등록 연도로 논문 목록의 시기를 다시 정하지 않았다. 2022년 게임 로그 논문은 이 dblp 연도 구역에 나타나지 않아 본문의 dblp 기반 최근 목록에 추가하지 않았다. OpenAlex의 DiLOS 단축 제목 항목도 제목만으로 2021년 논문의 대표 설명에 연결하지 않았다.

Members의 Students는 박사과정 3명, 석사과정 5명, 학부생 1명으로 총 9명이다. 학부생에게 게시된 과정 이상의 연구 직위를 붙이지 않았다. Alumni의 연도가 있는 41명 중 2021–2026년 9명을 실었다. 2020년 이전 32명과 별도 Past members의 연도 없는 17명은 최근 졸업생 표에서 제외했다. 표는 관측일의 게시 내용이며 기준일 당시 명단을 소급 복원한 것은 아니다.

수상·선정은 교수 누리집의 2023년 Best Paper Award, 2022년 Test of Time Award와 한국공학한림원 정회원 선정으로 총 3건이다. 원문이 연도로 적어 월·일은 보태지 않았다. 2021년 이전 수상·선정, 강의·영상·기타 대외 활동과 2027년 봄학기 모집 안내는 최근 성과 목록에 싣지 않았다. 특허·과제·별도 소식 절은 만들지 않았다.

태그는 태그 어휘 1.7판(2026-10-27)을 사용했다. 컴퓨터 네트워크는 첫 화면의 통신 스택·데이터센터 연구와 대표 논문 3·5의 호스트 통신·RDMA 분석, 네트워크 보안·프라이버시는 대표 논문 1의 통신 기밀성·무결성 보호, 계산 사회과학과 멀티모달 AI는 대표 논문 2의 사회적 감정·참여 행동 분석과 이미지·제목 분류에 근거한다.

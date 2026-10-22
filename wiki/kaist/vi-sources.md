# 시각 지능 연구실 근거와 출처

본문: [시각 지능 연구실 (Visual Intelligence Lab, VILab)](vi.md) · 작성 2026-10-23

## 읽은 자료

| 자료 | 주소 | 열람일 | 본문에서 쓴 곳 |
|---|---|---|---|
| 연구실 누리집 첫 화면 | <https://vi.kaist.ac.kr/> | 2026-10-23 | 요약, 무엇을 연구하나, 태그 근거 |
| Research 페이지와 그 화면이 불러오는 자료 <https://vi.kaist.ac.kr/data/research.json> | <https://vi.kaist.ac.kr/pages/research/> | 2026-10-23 | 무엇을 연구하나, 주요 연구 주제 1–6, 태그 근거 |
| Faculty 페이지와 그 화면이 불러오는 자료 <https://vi.kaist.ac.kr/data/faculty.json> | <https://vi.kaist.ac.kr/pages/faculty/> | 2026-10-23 | 무엇을 연구하나, 교수와 전문 분야(학력, 경력, 직책, 자문, 학술·공공 활동, 수상), 대학원 지원 안내 |
| 교수 CV(PDF, People·Faculty 페이지의 CV 연결) | <https://vi.kaist.ac.kr/assets/docs/Prof_Kuk-Jin_Yoon_CV.pdf> | 2026-10-23 | 교수와 전문 분야의 연구 관심 |
| People 페이지와 그 화면이 불러오는 자료 <https://vi.kaist.ac.kr/data/people.json> | <https://vi.kaist.ac.kr/pages/people/> | 2026-10-23 | 구성원 33명, 졸업생 카드 74장 |
| Publications 페이지와 그 화면이 불러오는 자료 <https://vi.kaist.ac.kr/data/publications.json> | <https://vi.kaist.ac.kr/pages/publications/> | 2026-10-23 | 최근 논문 목록 146편, 특허 17건, 주요 연구 주제의 논문, 대표 논문 후보와 저자 순서 |
| Projects 페이지와 그 화면이 불러오는 자료 <https://vi.kaist.ac.kr/data/projects.json> | <https://vi.kaist.ac.kr/pages/projects/> | 2026-10-23 | 연구 과제 39건, 주요 연구 주제 1·2·6, 응용 분야 |
| News 페이지와 그 화면이 불러오는 자료 <https://vi.kaist.ac.kr/data/news.json> | <https://vi.kaist.ac.kr/pages/news/> | 2026-10-23 | 소식 36건, 수상 6건, NeurIPS 2026 채택 표시, 졸업생 석사 카드의 졸업 연월 |
| Contact 페이지 | <https://vi.kaist.ac.kr/pages/contact/> | 2026-10-23 | 연락과 위치 |
| 화면 스크립트(구성원·졸업생·논문·과제·소식을 그리는 방식) | <https://vi.kaist.ac.kr/js/data-manager.js> 와 같은 폴더의 people.js, publications.js, projects.js, news-list.js, research.js, faculty.js | 2026-10-23 | 각 목록에 무엇이 화면에 나오는지 확인(아래 「확인한 범위」) |
| KAIST 기계공학과 교수진 목록 1–3쪽 | <https://me.kaist.ac.kr/team/team_010100.html> 와 같은 목록의 2·3쪽 | 2026-10-23 | 교수 등재(2쪽), 학과 표기 연구실 이름, 연구분야, 최종학위, 교수 소개 페이지 주소 확인 |
| KAIST 기계공학과 교수 소개(윤국진) | <https://me.kaist.ac.kr/pop/team.html?uid=39&LANGUAGE_TYPE=kor> (같은 주소의 eng 판도 같은 내용) | 2026-10-23 | 직위, 최종학위, 연구분야, 연구실, 교수 이메일 |
| KAIST 기계공학과 연구분야 페이지 | <https://me.kaist.ac.kr/research/research_010100.html> (로보틱스/제어/모빌리티)와 010200·010300·010400 | 2026-10-23 | 핵심교수 등재(010100), 연구주제, 주요 응용 산업(모빌리티, 로보틱스) |
| Crossref 서지(대표 논문 후보 17편, 목록 확인 2편 조회) | <https://api.crossref.org/> | 2026-10-23 | 대표 논문 DOI·서지·저자 순서, 최근 논문 목록의 범위 판단(아래) |
| Semantic Scholar 등록 초록 | <https://api.semanticscholar.org/> | 2026-10-23 | 대표 논문 2, 3, 4, 6, 8 초록 |
| arXiv 논문 페이지 | <https://arxiv.org/abs/2510.23205> | 2026-10-23 | 대표 논문 1 초록 |
| CVF Open Access 논문 페이지 | <https://openaccess.thecvf.com/> 의 CVPR 2022·2023·2024, ICCV 2025 논문 페이지 5쪽 | 2026-10-23 | 대표 논문 5, 7 초록(대표 논문 6, 8은 같은 문구의 Semantic Scholar 초록을 썼다) |

## 이름·직급·위치 표기 차이

- **연구실 이름**: 누리집 제목은 "KAIST Visual Intelligence Lab | VILab"이고, 첫 화면은 "Visual Intelligence Lab (VILAB)"으로, 바닥글은 "KAIST VILab"과 "Visual Intelligence Lab"으로 적는다(People 페이지 바닥글은 "VIsual Intelligence Lab"으로 적는다). Faculty 페이지는 "Visual Intelligence Laboratory, Department of Mechanical Engineering, KAIST"로 적는다. 기계공학과 교수진 목록·교수 소개·연구분야 페이지는 「시각 지능 연구실」로 적는다. 본문 제목은 학과 표기 국문 이름과 누리집의 영문 이름을 함께 적었다. 조천식모빌리티대학원의 차량지능 연구실(Vehicular Intelligence Lab, VIL)과는 다른 연구실이다.
- **누리집 주소**: 기계공학과 교수 소개와 연구분야 페이지는 연구실 웹사이트를 http://vi.kaist.ac.kr/ 로 적고, 이 주소는 https://vi.kaist.ac.kr/ 로 넘어간다. 첫 화면은 GitHub 연결을 kaist-vilab으로, People 페이지 바닥글은 연락 메일을 contact@cvml.kaist.ac.kr, GitHub를 kaist-cvml로 연결한다. 본문에는 이 연결을 쓰지 않았다.
- **교수 이름과 직위**: 윤국진, Kuk-Jin Yoon(People·Faculty 페이지, 기계공학과 교수 소개의 국문 이름). Publications 목록은 "Kuk-Jin Yoon", 특허 목록은 "윤국진"과 "Kuk-Jin Yoon"으로 적는다. 기계공학과 교수 소개는 직위를 「교수」로, 연구분야 페이지는 로보틱스/제어/모빌리티 분야의 「핵심교수」로, Faculty 페이지는 "Professor"로 적는다.
- **경력 표기**: Faculty 페이지는 KAIST 기계공학과 경력을 Associate Professor(2018년 2월–2024년 2월)와 Professor(2024년 3월부터)로 나누고, GIST 경력을 Assistant Professor(2008년 8월–2014년 8월)와 Associate Professor(2014년 9월–2018년 2월)로 나눈다. 교수 CV는 KAIST 경력을 "Professor, Department of Mechanical Engineering"(2018년 2월부터) 한 줄로, GIST 경력을 "Assistant & Associate Professor"(2008년 8월–2018년 2월) 한 줄로 적는다. Faculty 페이지의 함께 소속된 곳에는 Department of AX가 있고 CV에는 없다. 본문은 Faculty 페이지를 따랐다.
- **학력**: 기계공학과 교수 소개의 최종학위는 "Ph.D., KAIST (2006)"이고, Faculty 페이지와 CV는 Ph.D. in Electrical Engineering and Computer Science, KAIST, Feb. 2006으로 적는다.
- **위치·전화·이메일**: Contact 페이지는 교수실을 N7-4 #6101, 연구실을 N7-4 #5123, 전화를 교수실 (042) 350 7319와 연구실 (042) 350 7359로 적는다. 기계공학과 교수 소개는 교수실을 「기계동(N7) 6101」, 전화를 「042-350- 7319」(누리집 표기 그대로)로 적는다. Contact 페이지의 학생 대표(Lab student leader)와 누리집 담당(Webpage) 이메일은 구성원 카드의 이메일과 같아 연락 절에는 교수 이메일만 적었다.
- **구성원**: People 페이지 Current Members 34명 가운데 Administrative Assistant 구역의 1명은 행정 직원이라 싣지 않았다. 카드의 Research Interests가 "TBD"인 21명은 연구 주제 칸이 비어 있다. 일부 카드가 적는 연구실 안 역할(2026 Lab Leader, Assistant Lab Leader)은 싣지 않았다. 박사과정 카드의 소속 "Mechanical Engineering (Part-time)"은 표에서 "Mechanical Engineering, Part-time"으로 적었다. 대표 논문 8의 누리집 저자 표기 "Inhcul Chung"은 Crossref에 "Inchul Chung"으로, 졸업생 카드에 "In-Chul Chung"으로 적혀 있다.
- **졸업생**: People 페이지의 Alumni 구역은 화면 스크립트가 카드를 세 무리로 그린다. 졸업생 명단의 카드에 더해, 졸업 소식(학위수여식 글)에 석사 졸업자로 적혔거나 석사 졸업 연월이 따로 적힌 사람 가운데 석사 과정 카드가 아닌 사람에게 진로를 "Continued to Ph.D. at VILab"으로 적은 석사 카드를 따로 만들고, 박사후연구원 기간이 끝난 사람에게 박사후연구원 카드를 따로 만든다. 표는 화면의 순서(Postdoc Alumni, Ph.D. Graduates, M.S. Graduates, 각 구역 안에서 최근 졸업순)를 따랐다. 진로가 "VUNO inc (Alternative military service)"로 적힌 1명은 병역 표기를 빼고 기관 이름만 남겼다. 진로가 비어 있는 카드 2장(Youngjin Oh, Yoonsu Kang)은 칸을 비웠다.

## 대표 논문을 고른 이유

Faculty 페이지에 따르면 교수는 2018년 2월부터 KAIST 기계공학과에 있어, 2021–2026년 논문은 모두 KAIST 재직 시기 논문이다. Publications 목록 2021–2026년 구역 146편 가운데 윤국진 교수가 마지막 저자인 논문은 120편이다. 이 가운데 첫 화면의 네 핵심 분야와 Research 페이지의 분야에 나눠 후보 17편을 고르고 Crossref·Semantic Scholar·논문 페이지로 초록을 찾았다. 여덟 편 모두 교수가 마지막 저자이고, 1저자는 People 페이지의 현재 구성원(박사후연구원 Hoonhee Cho·Youngho Yoon, 박사과정 Giwon Lee·Jae-Young Kang) 또는 졸업생(Yujeong Chae, Hyeokjun Kweon)이다. 누리집 목록은 일부 저자 이름 뒤에 *를 붙이지만 그 뜻을 적지 않아, 표에는 표시 사실만 적었다. 초록은 arXiv 1편(1), Semantic Scholar 5편(2, 3, 4, 6, 8), CVF Open Access 논문 페이지 2편(5, 7)이다.

1. 시점 변화에 강건한 종단간 자율주행 VR-Drive(NeurIPS 2025). 7명 중 마지막 저자. 핵심 분야 「종단간 자율주행」. Crossref 기록은 Advances in Neural Information Processing Systems 38권이고 초록이 없어, 누리집이 연결한 arXiv 페이지의 초록을 썼다.
2. 여러 주행 궤적 데이터셋을 병합하는 움직임 계획 IMMP(ICCV 2025, 누리집 표시 Highlight). 5명 중 마지막 저자. Research 페이지의 경로 예측과 계획.
3. 입체 흐름과 함께 배우는 이벤트 카메라의 시간적 스테레오 정합(IEEE TPAMI 48권, 2026). 3명 중 마지막 저자. 핵심 분야 「이벤트 기반 비전」. 같은 주제의 학회 논문(ECCV 2024)이 목록에 따로 있다.
4. 이벤트 카메라를 쓴 3차원 물체 검출 Ev-3DOD(CVPR 2025, 누리집 표시 Highlight). 4명 중 마지막 저자. 이벤트 기반 비전과 3차원 인지.
5. 여러 날씨에서 LiDAR와 4D 레이더를 융합하는 3차원 물체 검출(CVPR 2024). 3명 중 마지막 저자. Research 페이지의 멀티모달 학습(여러 센서). 1저자 Yujeong Chae는 2026년 2월 박사 졸업생이다.
6. 다시점 영상 초해상도와 방사장을 함께 최적화하는 고해상도 새 시점 합성(CVPR 2023). 2명 중 마지막 저자. 핵심 분야 「3차원 장면 복원과 이해」.
7. SAM의 지식을 클래스 활성화 지도로 옮기는 약지도 의미 분할 S2C(CVPR 2024, 누리집 표시 Oral). 2명 중 마지막 저자. Research 페이지의 2차원 인지. 1저자 Hyeokjun Kweon은 2025년 2월 박사 졸업생이다.
8. 연속 구면 영상 표현으로 하는 360도 영상 초해상도 SphereSR(CVPR 2022, 누리집 표시 Oral). 4명 중 마지막 저자. Research 페이지의 새로운 센서(360도 카메라)와 저수준 비전(초해상도). Semantic Scholar 초록은 "360°"를 수식 기호로 적는다.

고르지 않은 후보: 초록을 얻은 경로 예측의 테스트 시점 훈련 T4P(CVPR 2024), 단일 원천 영역 일반화를 위한 LiDAR 의미 분할(IEEE TPAMI, 2026), 노출 시간을 모르는 영상의 이벤트 기반 디블러링(ECCV 2022), 악천후 제거(ICCV 2025)는 같은 갈래에 고른 논문이 있어 넣지 않았다. 미래 관계 추론을 쓴 차량 경로 예측(ICLR 2023), EOMVS(IEEE Robotics and Automation Letters, 2021), 도플러를 고려한 LiDAR·레이더 융합(ICCV 2025), GeoNVS(ECCV 2026), 다중 작업 최적화의 작업 우선순위(CVPR 2024)는 Crossref와 Semantic Scholar에서 초록을 얻지 못했다(Semantic Scholar는 요청 제한 응답이 이어졌다).

## 확인한 범위와 확인하지 못한 점

- 누리집의 People, Research, Publications, Projects, News, Faculty 페이지는 화면이 열릴 때 같은 누리집의 자료 파일(data 폴더의 people.json, research.json, publications.json, projects.json, news.json, faculty.json)을 불러와 내용을 그린다. 문서는 이 자료 파일과, 화면 스크립트가 각 항목에서 실제로 보여 주는 칸을 기준으로 썼다. 자료 파일에 있어도 화면에 나오지 않는 칸(구성원·졸업생의 학위 논문 제목, 논문의 status 값 등)은 쓰지 않았다. Gallery 페이지는 읽지 않았다.
- 읽은 연구실 누리집 페이지·자료 파일·스크립트·CV와 기계공학과 페이지 9쪽(교수진 목록 1–3쪽, 교수 소개 국·영문, 연구분야 4쪽)의 원문 어디에도 「수집」이나 「거부」라는 말이 없다. 구성원 표의 이메일은 People 페이지 카드에 적힌 학교 주소이고, 본문 연락 절의 이메일은 Contact 페이지와 기계공학과 교수 소개에 함께 적힌 교수 주소다.
- 구성원 표는 Current Members 34명 가운데 행정 직원 1명을 뺀 33명(Postdocs 3, PhD Students 19, Masters Students 8, Interns 3)이다. 졸업생 표는 Alumni 구역 카드 74장 전부(Postdoc Alumni 1, Ph.D. Graduates 25, M.S. Graduates 48)이며, 그 가운데 2018년 2월 이전 졸업자도 있다.
- 논문 목록: Publications 자료에는 논문·워크숍 논문 220편과 특허 41건이 있다. 화면은 연도 2026–2021 구역과 -2020 구역으로 나누며, 2021–2026년 구역은 논문 146편(학회 113, 학술지 27, 워크숍 6; 2026년 40, 2025년 25, 2024년 28, 2023년 18, 2022년 19, 2021년 16)이고 -2020 구역은 74편(학회 31, 학술지 42, 워크숍 1)이다. 최근 논문 목록은 2021–2026년 구역의 146편 전부다. 2021년 구역에는 2021년 10월 13일 이전에 나온 논문도 있다.
- 자료 파일은 학술지 논문 9편에 accepted 상태를 적고, 화면 스크립트는 학술지의 상태를 보여 주지 않는다. 본문 목록은 이 9편에 「게재 승인, 누리집 자료 표기」를 붙였다. 그 가운데 TPAMI 2편은 News 페이지가 2025-12-05에 게재를 알렸고 Crossref 서지(48권 4098-4113쪽, 48권 6053-6070쪽, 2026)가 있어 함께 적었다. 2026-09-25 News가 채택을 알린 RA-L 논문(HEAT)은 Crossref에 DOI(10.1109/lra.2026.3746115)가 등록되어 있으나 권호가 없다. 나머지 6편의 현재 출판 상태는 따로 조회하지 않았다. NeurIPS 2026 논문 3편은 News 페이지의 채택 소식에 따라 「채택」으로 표시했다. 목록의 연도는 누리집 연도 구역 기준이다.
- 의생명 범위: 최근 논문 목록에서 생명과학 대상의 논문은 단백질 상 분리를 예측·조절하는 기계학습 틀(Nature Communications, 2026) 1편이다. 같은 제목·저자의 Crossref 기록(사전 공개본, DOI 10.64898/2025.12.28.696755) 초록은 핵심 기여를 단백질 언어 모델 임베딩과 환경 조건을 함께 쓰는 예측 틀 LLPSense의 개발로 적어, 위키의 의생명 수록 범위 기준(자연·공학과 직접 연계된 연구만 싣는다)에 맞는 알고리즘 개발 논문으로 보고 목록에 두었다. 가스 센서 논문들(ACS Sensors, ACS Nano, Light: Science & Applications, Advanced Science, Science Advances)은 센서·소자와 딥러닝 판별 연구다.
- 특허: Publications 자료의 특허 41건 가운데 화면의 연도 기준(등록일, 등록 전이면 출원일)이 2021년 10월 13일 이후인 17건을 실었다. 2021-10-13 출원 1건은 기준일 당일이다.
- 연구 과제: Projects 자료의 50건 가운데 진행 중이거나 기간 끝이 2021년 10월 이후인 39건을 실었다. 모든 과제의 설명(description)은 "TBD"로 적혀 있어 쓰지 않았고, 지원(Funding)이 "TBD"인 과제 8건은 지원 칸을 비웠다. 화면은 이 칸을 "TBD"로 보여 준다.
- 소식: News 자료 90건(2018-02-23부터) 가운데 2021년 10월 13일 이후는 60건이다. 그 가운데 award 6건은 수상 절에, publication 30건·service 5건·career 1건은 소식 절에 실었고, 새 학생 입학 환영 글(admission) 10건과 학위수여식 글(graduation) 8건은 연구실 생활 글이라 싣지 않았다. 학위수여식 글의 석사 졸업자 명단은 화면이 졸업생 석사 카드의 졸업 연월로 쓰므로, 졸업생 표에는 그 연월이 들어 있다.
- 교수 CV에는 논문·특허·과제의 자체 목록이 따로 있으나, 목록 절은 누리집 화면의 목록만 썼다. CV에서는 연구 관심 항목만 옮겼다.

# 로켓 연구실 (Rocket Lab KAIST, RLK)

**KAIST 항공우주공학과 · 진정근 교수**

- 분야: 우주 비행체의 궤도 기동을 위한 저독성 이원 추진제 추력기, 물리 해석 모형과 신경망을 결합한 고체 로켓 모터 자동 설계, 재사용 발사체용 메탄 엔진의 시스템 모델링과 엔진 사이클 분석, 발사체·위성 추진 시스템의 통합 설계
- 대분야: 기계·로봇·제조
- 태그: 과학·공학 AI[^research][^deptlab]
- 홈페이지: <https://rocketlab.kaist.ac.kr/>
- 근거와 출처: [로켓 연구실 근거 페이지](rocketlab-sources.md)

> 우주 발사와 궤도 기동을 위한 화학 추진 기술을 연구하는 연구실이다. 저독성·친환경 추진제를 쓰는 추력기, 물리 기반 해석과 최적화 기법을 쓰는 고체 추진기관 설계, 메탄 엔진, 추진 시스템 설계의 네 갈래를 두고, 기초 연소 물리와 실제 비행 적용을 잇는 실용적 추진 공학을 지향한다. 1996년 Sejin Kwon 교수가 세운 연구실을 2025년부터 진정근 교수가 이끈다.[^deptlab][^about][^home]

## 무엇을 연구하나

학과 연구실 소개는 로켓 연구실(Rocket Lab KAIST, RLK)이 우주 발사와 궤도 기동을 위한 화학 추진 기술을 연구한다고 적는다. 저독성·친환경 추진제를 이용한 추력기(thruster, 추진제를 태우거나 분해해 생긴 가스를 뿜어 우주 비행체의 자세나 궤도를 바꾸는 추진 장치) 기술과, 물리 기반 해석과 최적화 기법을 활용한 고체 추진기관의 최적 설계를 핵심 연구 분야로 들고, 기초 연소 물리와 실제 비행 적용을 연결하는 실용적 추진 공학을 지향한다고 적는다. 추진 시스템 아키텍처 연구로 임무 요구 조건에 맞는 추진 시스템 개발 방법론을 찾고, 이를 바탕으로 국가 우주 기술 발전에 기여하겠다고 적는다.[^deptlab] 학과 소개의 연구 분야 칸은 저독성·저장 가능한 자연 점화성 추력기, 기계학습을 이용한 고체 로켓 모터 설계 최적화, 우주 화학 추진 시스템을 든다.[^deptlab]

누리집 About 페이지는 화학 로켓 추진이 짧은 시간에 큰 추력을 내는 가장 성숙한 방식이라 발사체와 궤도 기동에 대체할 수 없는 기술이고, 전기 추진이나 원자력 추진에 비해 비추력이 낮아 심우주 탐사처럼 높은 효율이 필요한 임무에서는 한계가 될 수 있다고 설명한다. 연구실은 발사체, 궤도 전이 비행체(OTV, orbital transfer vehicle) 같은 우주와 국방 분야의 비행체에 쓰이는 로켓 추진 기술과 시스템을 연구하며, 부품 하나에만 집중하기보다 설계, 해석, 시험을 아우르는 체계로 실제 비행 적용을 위한 시스템 중심 연구를 한다고 적는다.[^about] 첫 화면은 Sejin Kwon 교수가 세운 연구 철학과 학문 전통을 이어받으면서, 쌓아 온 연구 역량과 새 연구 책임자의 실무 개발 경험을 묶어 뉴 스페이스 시대에 필요한 차세대 추진 기술 연구를 이끌겠다고 적는다.[^home]

About 페이지의 연혁에 따르면 연구실은 1996년 Sejin Kwon 교수가 Jet Propulsion Lab(JPL)으로 세웠고, Aerospace Propulsion Lab(2002년), Propulsion & Power System Lab(2004년)을 거쳐 2007년 Rocket Lab으로 이름을 바꾸었다. 2018년에는 하이브리드 추진 관측 로켓 「Wooreesae-2」의 발사에 성공했고, 2025년부터 진정근 교수가 연구실을 이끈다.[^about] 현재 진행 중인 과제는 과산화수소를 이용한 우주 추진기관 인젝터 기술 연구(2025년 10월–2028년 12월)이며, 교수가 연구책임자다.[^project]

## 주요 연구 주제

### 1. 우주 추진: 궤도 기동용 이원 추진제 추력기 (Space Propulsion)

Research 페이지는 여러 탑재물을 서로 다른 궤도에 올리고, 궤도를 옮기고, 궤도상 서비스(on-orbit servicing, 궤도에 있는 위성에 다가가 점검·수리·연료 보급 같은 작업을 하는 것)를 하려면 추력기로 높은 기동성을 갖춘 우주 플랫폼이 필요하다고 설명한다. 연구실은 이 요구에 맞춰, 추력 응답이 빠르고 저장할 수 있는 저독성 추진제 기반의 자연 점화성 이원 추진제 기술을 연구한다.[^research] 기존의 과산화수소 기반 촉매 점화 기술을 바탕으로 새 추진제 조합의 적용 가능성을 살피고, 액적 낙하 시험과 충돌형 인젝터 반응 시험 같은 기초 실험을 한다. 스월 인젝터와 핀틀 인젝터 설계, 막 냉각 연구, 자연 점화 반응 기구의 실험 분석으로 비행에 쓸 수 있는 추력기와 엔진 개발의 기술 기반을 갖추는 것이 목표라고 적는다.[^research] 진행 중인 과제의 제목도 과산화수소를 이용한 우주 추진기관 인젝터 기술 연구다.[^project]

### 2. 고체 로켓 모터: 물리 모형과 신경망을 결합한 자동 설계 (Solid Rocket Motor)

연구실은 고체 추진 시스템의 설계와 해석을 위한 핵심 소프트웨어를 자체 개발하고, 비용이 적게 들고 신뢰도가 높은 물리 해석 모형을 바탕으로 최적 설계 기법을 연구한다. 물리 모형을 신경망 이론과 최적화 기법에 결합해, 주어진 임무 요구 조건에 맞는 고체 로켓 모터를 자동으로 설계하고 최적화하는 기술을 개발한다고 적는다.[^research] About 페이지도 이 갈래를 물리 해석 모형과 신경망 이론을 융합해 임무 요구에 최적화된 고체 로켓 모터의 자동 설계 기술을 개발하는 연구로 요약한다.[^about]

### 3. 액체 로켓 엔진: 재사용 발사체용 메탄 엔진 (Liquid Rocket Engine)

Research 페이지는 우주 발사체의 추진 시스템이 기존의 케로신·액체산소(KeroLox)와 액체수소·액체산소(HydroLox) 조합에서 메탄·액체산소(MethaLox) 조합으로 옮겨 가고 있다고 설명한다. 메탄 엔진은 추진제를 공급하고 펌프의 동력을 얻는 구성에 따라 여러 엔진 사이클을 쓸 수 있어, 임무에 맞는 구성을 설계하는 것이 핵심이라고 적는다.[^research] 연구실은 메탄 엔진 구성에 대한 1차원 시스템 시뮬레이션 모형을 만들어 시스템 동특성과 시동 특성을 연구하고, 저장 가능한 산화제인 과산화수소를 쓰는 다단 연소 사이클 같은 차세대 추진 시스템도 연구한다.[^research]

### 4. 추진 시스템 설계와 통합 (System Design)

Research 페이지는 로켓 추진 시스템과 비행체가 여러 부품이 함께 임무를 수행하는 복잡한 통합 시스템이라고 보고, 추진제 공급 계통, 추력기, 밸브로 이루어진 추진 시스템 구성을 분석하는 일이 가볍고 성능이 최적화된 비행체 추진 시스템을 설계하는 데 핵심이라고 적는다. 연구실은 우주 추진 시스템, 로켓 엔진 조립체, 우주 발사체 하드웨어와 기초 시스템 설계 기술을 연구한다.[^research] About 페이지는 이 갈래를 발사체와 위성 추진 시스템의 무게를 줄이고 성능을 최적화하기 위한 시스템 통합 설계와 하드웨어 구성 기술로 요약한다.[^about]

## 교수와 전문 분야

진정근 교수(Jin, Jung-Kun)는 KAIST 항공우주공학과 부교수(Associate Professor)다.[^deptfac] KAIST 항공우주공학과에서 학사(2003년), 석사(2005년), 박사(2009년)를 받았고, 박사과정 지도 교수는 Se-Jin Kwon 교수다. 삼성중공업 선임연구원(Senior Research Engineer, 2010–2012년)과 국방과학연구소 책임연구원(Principal Researcher, 2012–2025년)으로 일했으며, 그 시기의 연구는 유도무기와 발사체의 로켓 추진 시스템, 그리고 비행체 통합 기술이었다고 Members 페이지 교수 카드는 적는다.[^members][^deptfac]

교수 카드와 학과 교수진 목록이 드는 연구 관심 분야는 고체 로켓 모터 설계·해석(내탄도), 액체 로켓 엔진, 우주 화학 추진, 자연 점화성 이원 추진제 추력기, 친환경 추진제, 반작용 제어 시스템, 발사체와 유도무기 시스템 설계 등이다.[^members][^deptfac] 누리집 Publication 페이지는 교수의 논문 18건(2004–2022년)을 싣는다. 초음속 이젝터 연구(2004–2005년), 촉매 연소와 과산화수소 단일 추진제 추력기 연구(2006–2011년), 선박 디젤 엔진의 폐열 회수 사이클 해석(2012년), 고체 로켓 모터의 핀틀 노즐·침식 연소·내열재 불균일 삭마 연구(2014–2020년), 고체 추진제 킥 모터의 개발 동향(2022년)이 있다.[^pubs]

Members 페이지는 연구실을 세운 Sejin Kwon 교수를 명예교수로 함께 싣는다. 카드는 그의 연구 관심 분야를 추력기 설계, 과산화수소 기반 로켓 추력기, 하이브리드와 단일·이원 추진제, 촉매 연구, 친환경 추진, 관측 로켓 시스템, 달 착륙선·지상 시험 비행체로 적는다.[^members]

## 구성원

누리집 Members 페이지의 학생 9명이다(박사과정 1명, 석사과정 2명, 학부생 6명). 과정 칸은 카드가 속한 분류(Ph.D. Students, M.S. Students, Undergraduate)를 옮긴 것이고, 괄호는 이름 뒤에 함께 적힌 표기(Part - Time, Collaborating Researcher)다. 시작은 카드의 이름 옆 표기(26S, 26F)를 그대로 옮긴 것이다. 연구 주제는 카드의 관심 분야를 영문 그대로 옮겼고, 이메일은 카드에 적힌 학교 주소다. Yoonchae Kim의 카드는 학력 칸에 아주대학교(Ajou-University) Dept. of Military Digital Convergence 학부 재학을 적는다.[^members]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 |
|---|---|---|---|---|
| Eunkwang Lee | 박사과정 (Part - Time) | 26F | Liquid Rocket Engine | space@kaist.ac.kr |
| Jaehyung Park | 석사과정 | 26S | Liquid Rocket, Rocket System Engineering, Injector | adrock@kaist.ac.kr |
| Tahani Musaed | 석사과정 | 26F | Liquid Rocket Propulsion, Injector, Cryogenic Propellant, Rocket System | tahani@kaist.ac.kr |
| Hyunwoo Kang | 학부 연구생 | 26S | Fuel Supply Rig Build, Plumbing and Instrument | hyunwoo5721@kaist.ac.kr |
| YunJae Rim | 학부 연구생 | 26S | Propulsion System Survey and Design | m0934013323@kaist.ac.kr |
| Yoonchae Kim | 학부 연구생 (Collaborating Researcher) | 26S | Scientific machine learning, Neural operators, Physics-informed learning, Inverse design | yoonchaekim@ajou.ac.kr |
| Sangjun Oh | 학부 연구생 | 26F | Propulsion System Architecture Design and Optimization | steven04@kaist.ac.kr |
| Jeongwoo Choi | 학부 연구생 | 26F | Liquid Rocket Engine, Combustion and Reactive Flow, Computational Fluid Dynamics (CFD) | woo23@kaist.ac.kr |
| Doyoon Yoo | 학부 연구생 | 26F | Solid Rocket Motor, SRM Grain Reverse Design, Ascent Trajectory Optimization | aiden0210@kaist.ac.kr |

## 최근 논문 목록 (2021–2026)

누리집 Publication 페이지는 진정근 교수의 논문 18건(2004–2022년; 국제 학술지 4건, 국내 학술지 13건, 국내 학회 1건)을 분류별로 싣는 교수 개인의 목록이다.[^pubs] 2021–2026년 항목은 아래 2022년 국내 학회 발표 1건뿐이며, 교수가 연구실을 맡은 2025년보다 앞서 나온 발표다.[^pubs][^about] 저자와 학회·쪽 표기는 누리집 그대로다.[^pubs]

**2022**

- Seokhyun Hong, Jungkun Jin. "Development Trends of Solid Propellant Kick Motor". *2022 KSPE Spring Conference, pp.301 - 311, 2022-05*.

## 연구 과제

누리집 Project 페이지의 진행 중 과제(Ongoing Research Projects)다. 끝난 과제(Completed Research Projects) 칸에는 항목이 없다. 기간, 지원 기관, 역할은 누리집 표기 그대로다.[^project]

- 과산화수소를 이용한 우주 추진기관 인젝터 기술 연구 (기간 2025.10.1–2028.12.31; 지원 KAIST; 역할 연구책임자; 상태 Ongoing)

## 연락과 위치

- 위치: KAIST N7-2동 3305호(교수실), 실험실 W10[^deptlab][^home]
- 주소: 대전광역시 유성구 대학로 291 KAIST 항공우주공학과 (Aerospace Engineering N7-2 KAIST, Daehak-ro, Yuseong-Gu, Daejeon)[^deptlab][^home]
- 전화: 042-350-3731[^deptlab][^deptfac]
- 교수 이메일: jungkunjin@kaist.ac.kr[^deptlab][^deptfac][^home]
[^home]: 연구실 누리집 첫 화면 <https://rocketlab.kaist.ac.kr/> (Welcome to Rocket Lab KAIST 소개, 연락처, 2026-10-23 열람)
[^about]: 연구실 누리집 About 페이지 <https://rocketlab.kaist.ac.kr/about> (Introduction, Research Area 네 갈래, History, 2026-10-23 열람)
[^research]: 연구실 누리집 Research 페이지 <https://rocketlab.kaist.ac.kr/research> (Space Propulsion, Solid Rocket Motor, Liquid Rocket Engine, System Design, 2026-10-23 열람)
[^members]: 연구실 누리집 Members 페이지 <https://rocketlab.kaist.ac.kr/members> (교수 카드 2장과 학생 카드 9장, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publication 페이지 <https://rocketlab.kaist.ac.kr/publication> (International Journal, Domestic Journal, Domestic Conference 18건, 2026-10-23 열람)
[^project]: 연구실 누리집 Project 페이지 <https://rocketlab.kaist.ac.kr/project> (Ongoing Research Projects 1건, 2026-10-23 열람)
[^deptlab]: KAIST 항공우주공학과 연구실 소개(로켓 연구실) <https://ae.kaist.ac.kr/boards/view/board_lab/13964> (연구실명, 교수, 연구실 소개, 웹사이트, 이메일, 전화, 위치, 연구 분야, 2026-02-03 게시, 2026-10-23 열람)
[^deptfac]: KAIST 항공우주공학과 교수진 목록 <https://ae.kaist.ac.kr/boards/lists/board_faculty/sc_category/1/> (진정근 직위, 학력, 전화, 웹사이트, 이메일, 연구 분야, 2026-10-23 열람)

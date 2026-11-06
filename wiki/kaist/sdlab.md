# 구조설계 연구실 (Structural Design Laboratory, SDLAB)

**KAIST 건설및환경공학과 · 곽효경 교수**

- 영문 이름: Hyo-Gyoung Kwak
- 분야: 콘크리트 구조물의 비선형 해석, 장기 변형, 충격 저항과 구조 설계[^dept]
- 대분야: 건설·도시·인프라, 기계·로봇·제조
- 태그: 전산역학·수치 해석[^methods], 고체역학·소성[^material], 설계 최적화(위상·형상 최적화)[^design]
- 홈페이지: <https://sdlab.kaist.ac.kr>
- 근거와 출처: [구조설계 연구실 근거 페이지](sdlab-sources.md)

> 콘크리트 구조물이 힘·시간·수분 변화에 따라 어떻게 변형하고 손상되는지 계산하고, 교량·고층 건물·수중 터널의 설계에 연결하는 연구실이다.[^dept][^home]

## 무엇을 연구하나

구조설계 연구실은 교량, 초고층 건물, 원자력 발전소 격납용기와 주차장 구조물을 대상으로 사용성과 안전성을 예측한다. 핵심은 콘크리트 구조물의 거동을 재현하는 수치해석모델(계산으로 대상의 상태와 변화를 근사하는 모형)을 개발하는 것이다.[^methods] 콘크리트가 굳기 시작하는 시기부터 큰 힘을 받아 견디는 한계에 이르는 상태까지 다룬다.[^dept]

첫 갈래는 재료가 힘을 받을 때의 비선형 거동(가한 힘과 변형이 일정한 비율로 대응하지 않는 거동)이다. 연구실은 콘크리트의 재료 모형을 개발하고, 철근과 콘크리트가 힘을 주고받는 경계에서 서로 미끄러지는 현상도 해석한다.[^material] 폭발이나 충격을 받은 구조물이 어떻게 변형하고 파손되는지도 이 갈래에 속한다.[^home][^dept]

둘째 갈래는 시간과 수분 변화가 만드는 변형이다. 콘크리트는 같은 힘이 지속되어도 변형이 시간에 따라 진행되는 크리프(일정한 힘을 받는 동안 시간에 따라 변형이 증가하는 현상)를 보일 수 있다. 연구실은 이런 장기 변화와 시공 순서가 구조물에 미치는 영향을 계산한다. 굳기 전 콘크리트 표면에서 빠져나오는 물과 증발하는 물을 함께 계산해 표면 건조와 균열 가능성을 판단하는 연구도 한다.[^dept][^p1]

셋째 갈래는 해석을 실제 구조물의 설계로 연결하는 일이다. 연구실은 최적화(제약 조건을 지키며 정해진 목표값을 최소화하거나 최대화하는 방법)와 자동화를 포함한 설계 방법을 개발한다.[^design] 수중 부유식 터널(부력과 지지 힘의 균형으로 수중 위치를 유지하는 터널)과 모듈식 저장 탱크를 적용 대상으로 제시한다.[^home]

## 주요 연구 주제

### 구조물의 힘과 변형을 계산하는 방법

철근콘크리트(철근과 콘크리트를 함께 사용해 힘을 견디도록 만든 재료)로 된 구조물을 유한요소법(연속된 대상을 작은 요소로 나누고 각 요소의 관계를 계산해 전체 거동을 구하는 방법)으로 해석한다. 반복해서 가해지는 힘, 철근과 콘크리트의 부착, 재료가 견딜 수 있는 한계를 계산에 반영한다.[^dept]

### 초기 건조와 장기 변형

수분 손실에 의한 초기 균열과 시간이 지나면서 누적되는 변형을 함께 연구한다. 콘크리트를 채운 강관(속이 빈 강철 관) 기둥에서는 크리프를 고려해 견딜 수 있는 힘을 계산하고, 고층 건물에서는 기둥마다 축소량(축 방향으로 길이가 감소한 양)이 달라지는 현상을 분석한다. 초기 설계 단계에서 기둥 단면을 정하는 데 쓸 수 있는 관계를 제안하는 연구다.[^p1][^p2][^p3]

### 폭발과 충격에 대한 구조물 해석

폭발 하중(폭발로 구조물에 가해지는 힘)을 받은 콘크리트 구조물의 변형과 손상을 해석한다.[^home] 충격으로 변형이 커지는 섬유 보강 시멘트 복합재료에는 서로 다른 계산 방법을 결합해 구조 반응을 예측하는 접근을 쓴다.[^p4]

### 수중 부유식 터널과 계류선

연구실은 수중 부유식 터널을 구조해석과 최적화의 대상으로 제시한다.[^home] 국제학술지 목록에는 계류선(물 위나 물속의 구조물을 정해진 위치에 붙잡아 두는 줄)을 둔 터널과 파도의 상호작용, 원형 콘크리트 터널의 설계 가능성을 다룬 논문이 실려 있다.[^intl-list]

## 대표 논문

KAIST 재직 시기의 연구실 학술지 목록에서 초록이 확인되는 논문을 골랐다. 표의 연도는 연구실 목록의 Date 칸이다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 주요 저자의 ‘마지막 저자’는 전체 저자 목록의 순서다.

| 번호 | 연도 | 논문·발표처 | 주요 저자 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2024 | A simplified but improved numerical approach to determine moisture balance for plastic shrinkage cracking in concrete · Case Studies in Construction Materials[^p1] | 1저자 Hyun-Kyoung Kim; 마지막 저자 Hyo‐Gyoung Kwak | 굳기 전 콘크리트 표면으로 나오는 물과 증발하는 물의 양을 계산해 표면 건조를 예측했다. 수분 균형을 초기 균열 가능성을 판단하는 지표로 삼고, 바람과 차풍막의 영향을 계산했다. |
| 2 | 2024 | 시간 의존적 거동을 고려한 CFT 기둥의 극한 하중 계산을 위한 수치 해석 모델 제안 · 한국전산구조공학회논문집[^p2] | 1저자 SeongHun Kim; 마지막 저자 Hyo‐Gyoung Kwak | 콘크리트를 채운 강관 기둥의 시간에 따른 변형과 힘을 없애도 남는 변형을 함께 계산했다. 기둥이 견딜 수 있는 힘과 단기·장기 거동을 평가하는 모형이다. |
| 3 | 2024 | Quantification of differential axial shortening in reinforced concrete and concrete filled steel tube based building structures · Journal of Asian Architecture and Building Engineering[^p3] | 1저자 SeongHun Kim; 마지막 저자 Hyo‐Gyoung Kwak | 고층 건물의 철근콘크리트 기둥과 콘크리트를 채운 강관 기둥에서 길이가 줄어드는 정도를 비교했다. 기둥 사이 축소량 차이와 건물 자체 무게가 차지하는 하중 비율의 관계를 제안해 초기 설계에 연결했다. |
| 4 | 2023 | Impact simulations for high-performance fiber-reinforced cement composites using a coupled finite element and smoothed particle Galerkin method · International Journal of Damage Mechanics[^p4] | 1저자 MinJoo Lee; 마지막 저자 Hyo‐Gyoung Kwak | 섬유 보강 시멘트 복합재료의 충격 해석을 위해 유한요소법과 입자 기반 계산법을 결합했다. 변형이 커지는 문제에서 결합 모형을 실험 자료 및 유한요소법만 쓴 결과와 비교했다. |

## 교수와 전문 분야

곽효경 교수는 서울대학교 학사(1985), KAIST 석사(1987)와 토목공학 박사(1990)를 받았으며, 1996년부터 KAIST 건설및환경공학과 교수로 재직하고 있다. 학과가 제시한 전문 분야는 구조물 최적설계, 교량 해석·설계, 재료 비선형 해석과 콘크리트의 시간 의존적 거동이다.[^dept]

최근 논문에서는 콘크리트의 초기 수분 변화, 기둥의 장기 변형, 충격에 대한 구조 반응을 다룬다.[^p1][^p2][^p4] 공개 경력에는 Computers and Concrete 편집장(2016~현재)이 적혀 있다.[^prof]

## 응용 분야

교량과 고층 건물의 사용성·안전성 평가, 콘크리트 구조물의 설계·시공 방법 개선이 주요 응용이다. 누리집은 긴장재(미리 당겨 구조물에 압축력을 주는 강재)를 구조물에 고정하는 정착부, 수중 부유식 터널과 모듈식 액화천연가스 저장 탱크를 실무 연구 대상으로 제시한다. 고온에 노출된 콘크리트 구조물의 해석도 연구 관심사다.[^dept][^home]

## 구성원

연구실 Students에 게시된 재학생 1명이다. 과정과 학교 이메일은 누리집 표기다.[^students]

| 이름 | 과정 | 이메일 |
|---|---|---|
| 정현승 (Hyunseung Chung) | 박사과정(Ph.D. Candidate) | hyunseungchung@kaist.ac.kr |

## 졸업생과 이전 구성원

연구실 Alumni에 게시된 54명이다. 기수는 누리집의 Class 표기이며 학위 연도가 아니다. 진로는 누리집이 적은 기관·부서 표기다.[^alumni]

| 이름 | 기수(누리집 Class) | 랩이 적은 진로 |
|---|---|---|
| 송종영 | 01st | 동승 엔지니어링 / BIM |
| 최준호 | 02nd | 미극동공병단 / 설계실 |
| 김재구 | 02nd | (주) 도화엔지니어링 / 철도부문 |
| 서영재 | 02nd | DL E&C / 토목기술지원팀 |
| 김지은 | 03rd | SK 에코플랜트 (구 SK건설) / 그린리노베이션 사업그룹 |
| 김도연 | 03rd | 한국전력기술 (주) / 원자력본부 토목환경기술실 |
| 배준모 | 04th | 현대건설 / 싱가폴 지하변전소 현장 |
| 김선필 | 04th | 한국원자력안전기술원 / 구조부지평가실 |
| 이광모 | 04th | (주)서린프릿지텍 |
| 신현기 | 05th | GS건설 / 인프라구조팀 |
| 김진국 | 05th | 서울과학기술대학교 / 건설시스템공학과 |
| 손제국 | 05th | 삼성물산 / 토목ENG팀 |
| 이병국 | 06th | 삼성물산 / 토목ENG팀 |
| 노상훈 | 06th | 한국수력원자력 / 중앙연구원 |
| 홍수미 | 07th | 방위사업청 |
| 하수준 | 07th | Texas Department of Transportation / Houston District Laboratory |
| 유상준 | 08th | 한국지역난방기술 / 토목엔지니어링그룹 |
| 김선용 | 08th | 원광대학교 / 토목환경공학과 |
| 김재홍 | 08th | 한국과학기술원 / 건설및환경공학과 |
| 나채국 | 09th | Rutgers University / RIME Laboratory |
| 양수은 | 09th | NH농협금융지주 / 리스크관리부 |
| 장형주 | 10th | 쌍용건설 / 토목견적팀 |
| 홍성진 | 10th | 삼성물산 / 토목전략그룹 |
| 이강욱 | 11th | 현대건설 / 별내선 3공구 현장 |
| 신동규 | 11th | 한국조선해양 / 미래기술연구원 에너지기술연구소 |
| 박준호 | 12th | 삼성물산 / 탕정제2지방산업단지 |
| 곽지현 | 12th | DL E&C / 토목핵심기술개발팀 |
| 황진욱 | 13th | 한국원자력안전기술원 |
| 임홍재 | 14th | 부산대학교 / 건설융합학부 토목공학과 |
| 권양수 | 15th | 한국수력원자력 / 중앙연구원 |
| 양규영 | 15th | DL E&C / 기술기획팀 |
| 권세형 | 15th | 롯데건설 / 기술연구원 토목연구팀 |
| Kien | 15th |  |
| 박선종 | 16th | 한국원자력안전기술원 / 검사총괄실 |
| 하상희 | 16th | 포스코 E&C / 토목ENG그룹 |
| 강한글 | 17th | 현대중공업 / 선박연구소 운항구조연구실 |
| 김언 | 19th | 한국조선해양 / 미래기술연구원 에너지기술연구소 |
| 박효범 | 21st | 국방시설본부 / 충청시설단 설계과 |
| 심민석 | 22nd | 마이다스아이티 / CIM 사업그룹 기술팀 |
| 황주영 | 19th | 동의대학교 / 건설공학부 토목공학과 |
| 박강규 | 19th | 국방과학연구소 / 4연구원 4부 2팀 |
| 김정래 | 20th | 까리용 (사내이사) |
| 이원호 | 21st | 한국조선해양 / 미래기술연구원 에너지기술연구소 |
| 김규진 |  | HD현대중공업 / 하중구조연구실 |
| 이상옥 |  | 국토교통부 |
| 이용훈 |  | 김앤장 법률사무소 |
| 주석준 |  | 삼성엔지니어링 |
| 신정호 |  |  |
| 문서영 |  |  |
| 박지연 |  |  |
| 이민주 |  | 국방과학연구소 / 4연구원 1부 1팀 |
| 김성훈 |  | HD한국조선해양 |
| 김현경 |  | HD현대중공업 |
| 원경환 |  |  |

## 최근 논문 목록 (2021–2026)

연구실 Research가 연결한 국제학술지 목록의 17편과 국내학술지 목록의 3편이다.[^intl-list][^domestic-list] 연·월은 목록의 Date 칸이고 제목·저자·발표처는 연구실 표기다. DOI가 있는 항목에는 함께 표시했다.[^bibliography]

### 국제학술지


**2026**

- Chung, Hyunseung, Kwak, Hyo-Gyoung. "A Simple yet Effective Approach to Generate P-I Diagrams for RC Beams". *INTERNATIONAL JOURNAL OF IMPACT ENGINEERING, v.207, pp.105490*. 연·월 2026.01. DOI: <https://doi.org/10.1016/j.ijimpeng.2025.105490>.

**2025**

- Kim, Hyun-Kyoung, Kwak, Hyo-Gyoung. "Quantification of resistance reduction of recycled aggregate concrete (RAC) members and compensatory section adjustment". *ENGINEERING STRUCTURES, v.342, pp.120943*. 연·월 2025.11. DOI: <https://doi.org/10.1016/j.engstruct.2025.120943>.

**2024**

- Kim, Hyun-Kyoung, Kwak, Hyo-Gyoung. "A simplified but improved numerical approach to determine moisture balance for plastic shrinkage cracking in concrete". *CASE STUDIES IN CONSTRUCTION MATERIALS, v21, pp.e03780*. 연·월 2024.12. DOI: <https://doi.org/10.1016/j.cscm.2024.e03780>.
- Chung, Hyunseung, Kwak, Hyo-Gyoung. "Hardware accelerated nonlinear FEA of RC beams using the ML-based material model". *COMPUTERS AND CONCRETE, v.34, no.6, pp.791-804*. 연·월 2024.12.
- Kim, Seong Hun, Kwak, Hyo-Gyoung. "Quantification of differential axial shortening in reinforced concrete and concrete filled steel tube based building structures". *JOURNAL OF ASIAN ARCHITECTURE AND BUILDING ENGINEERING, v23, no.6, pp.1841-1853*. 연·월 2024.11. DOI: <https://doi.org/10.1080/13467581.2023.2278459>.

**2023**

- Kim, Hyun-Kyoung, Kwak, Hyo-Gyoung, Hwang, Ju-Young. "Numerical data-driven machine learning model to predict the strength reduction of fire damaged RC columns". *COMPUTERS AND CONCRETE, v.32, no.6, pp.625-637*. 연·월 2023.12.
- Kim, Seong Hun, Kwak, Hyo-Gyoung. "Efficiency of CFT column plastic design approach for frame structures subjected to horizontal forces". *COMPUTERS AND CONCRETE, v.32, no.5, pp.527-541*. 연·월 2023.11.
- Kim, Sung-Jae, Jin, Chungkuk, Lee, Ikjae, Kim, Gyu-Jin, Kim, MooHyun, Kwak, Hyo-Gyoung. "Efficient time-domain approach for hydroelastic-structural analysis including hydrodynamic pressure distribution on a moored SFT". *MARINE STRUCTURES, v.90*. 연·월 2023.07. DOI: <https://doi.org/10.1016/j.marstruc.2023.103402>.
- Ju, SeokJun, Kwak, Hyo-Gyoung. "Analytical model for progressive collapse of RC frame structures subjected to blast loadings". *JOURNAL OF BUILDING ENGINEERING, v.71*. 연·월 2023.07. DOI: <https://doi.org/10.1016/j.jobe.2023.106474>.
- Lee, MinJoo, Kwak, Hyo-Gyoung, Kim, Sung-Wook, Park, Gang-Kyu. "Numerical study on RC and HPFRCC slabs exposed to TNT explosion near ground". *COMPUTERS AND CONCRETE, v.31, no.6, pp.561-570*. 연·월 2023.06.
- Lee, MinJoo, Kwak, Hyo-Gyoung. "Impact simulations for high-performance fiber-reinforced cement composites using a coupled finite element and smoothed particle Galerkin method". *INTERNATIONAL JOURNAL OF DAMAGE MECHANICS, v.32, no.3, pp.424-441*. 연·월 2023.03. DOI: <https://doi.org/10.1177/10567895221146578>.
- Jin, Chungkuk, Kim, Gyu-Jin, Kim, Sungjae, Kim, MooHyun, Kwak, Hyo-Gyoung. "Discrete-Module-Beam-Based Hydro-Elasticity Simulations for Moored Submerged Floating Tunnel under Regular and Random Wave Excitations". *ENGINEERING STRUCTURES, v.275, no.A*. 연·월 2023.01. DOI: <https://doi.org/10.1016/j.engstruct.2022.115198>.

**2022**

- Kim, Gyu-Jin, 이상민, Kim, Mujong, Kwak, Hyo-Gyoung, Hong, Jung-Wuk. "Characterization of single and dual SFT through a hydraulic experiment under regular and irregular waves". *OCEAN ENGINEERING, v.263*. 연·월 2022.11. DOI: <https://doi.org/10.1016/j.oceaneng.2022.112365>.
- Kim, Seong Hun, Kwak, Hyo-Gyoung. "Optimization of an RC frame structure based on a plastic analysis and direct search of a section database". *JOURNAL OF BUILDING ENGINEERING, v.48*. 연·월 2022.05. DOI: <https://doi.org/10.1016/j.jobe.2021.103959>.
- Ju, SeokJun, Kwak, Hyo-Gyoung. "A FE model to evaluate the resisting capacity of RC beams and columns under blast loading based on P-I diagram". *INTERNATIONAL JOURNAL OF IMPACT ENGINEERING, v.161*. 연·월 2022.03. DOI: <https://doi.org/10.1016/j.ijimpeng.2021.104113>.
- Kim, Gyu-Jin, Kwak, Hyo-Gyoung. "Feasibility Assessment for Design of a Circular One-Cell Concrete Submerged Floating Tunnel Structure". *OCEAN ENGINEERING, v.245*. 연·월 2022.02. DOI: <https://doi.org/10.1016/j.oceaneng.2021.110481>.
- Lee, MinJoo, Park, Gang-Kyu, Kim, Sung-Wook, Kwak, Hyo-Gyoung. "Damage characteristics of high-performance fiber-reinforced cement composites panels subjected to projectile impact". *INTERNATIONAL JOURNAL OF MECHANICAL SCIENCES, v.214, pp.106919*. 연·월 2022.01. DOI: <https://doi.org/10.1016/j.ijmecsci.2021.106919>.

### 국내학술지


**2024**

- 김성훈, 곽효경. "수평 하중을 받는 프레임 구조물에서 CFT 기둥의 소성 설계 접근법의 효율성 분석". *한국전산구조공학회논문집, v.37, no.6, pp.391-400*. 연·월 2024.12. DOI: <https://doi.org/10.7734/coseik.2024.37.6.391>.
- 김성훈, 곽효경. "시간 의존적 거동을 고려한 CFT 기둥의 극한 하중 계산을 위한 수치 해석 모델 제안". *한국전산구조공학회논문집, v.37, no.1, pp.25-31*. 연·월 2024.02. DOI: <https://doi.org/10.7734/coseik.2024.37.1.25>.

**2021**

- 주석준, 곽효경. "폭발하중을 받는 철근콘크리트 부재의 직접전단 파괴 및 휨 파괴 저항 성능 평가를 위한 수치 해석 모델 개발". *한국전산구조공학회논문집, v.34, no.6, pp.393-401*. 연·월 2021.12. DOI: <https://doi.org/10.7734/coseik.2021.34.6.393>.

## 과제와 사업

교수 소개에 사업책임자 경력으로 적힌 사업 1건이다. 수행 기간과 역할은 누리집 표기다.[^prof]

- 스마트시티 혁신인재육성사업 (기간 2019~현재; 역할 사업책임자)

## 연락과 위치

- 연구실 위치: 대전광역시 유성구 대학로 291, KAIST W1-2 응용공학동 3223호, 우편번호 34141[^home]
- 연구실 전화: +82-42-350-3661; 팩스: +82-42-350-5690[^home]
- 교수 소개에 게시된 업무 이메일·전화: kwakhg@kaist.ac.kr; +82-42-350-3661[^prof]
- 학과 교수 소개의 오피스·전화·이메일: W1-2동 3203호; 042-350-3621; khg@kaist.ac.kr[^dept]
[^home]: 구조설계 연구실, 첫 화면의 Research Interests와 연락처. <https://sdlab.kaist.ac.kr> (관측 2026-11-06).
[^dept]: KAIST 건설및환경공학과, 곽효경 교수 소개. <https://cee.kaist.ac.kr/boards/view/professor/34/sc_category/1> (관측 2026-11-06).
[^prof]: 구조설계 연구실, Professor. <https://sdlab.kaist.ac.kr/Professor> (관측 2026-11-06).
[^students]: 구조설계 연구실, Students. <https://sdlab.kaist.ac.kr/Students> (관측 2026-11-06).
[^alumni]: 구조설계 연구실, Alumni. <https://sdlab.kaist.ac.kr/Alumni> (관측 2026-11-06).
[^methods]: KAIST 건설및환경공학과, 곽효경 교수 연구 소개의 수치해석모델 개발 설명. <https://cee.kaist.ac.kr/boards/view/professor/34/sc_category/1> (관측 2026-11-06).
[^material]: 구조설계 연구실, Research Interests의 재료 비선형 모형과 경계 미끄러짐 해석. <https://sdlab.kaist.ac.kr> (관측 2026-11-06).
[^design]: KAIST 건설및환경공학과, 곽효경 교수 연구 소개의 최적화·자동화를 포함한 설계 방법 개발 설명. <https://cee.kaist.ac.kr/boards/view/professor/34/sc_category/1> (관측 2026-11-06).
[^bibliography]: OpenAlex, Hyo‐Gyoung Kwak(A5061799928)의 2021–2026년 논문 서지·전체 저자 목록. <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5061799928,publication_year:2021-2026> (관측 2026-11-06).
[^intl-list]: 구조설계 연구실, Research가 연결한 SDLAB 국제학술지 목록 표. <https://docs.google.com/spreadsheets/d/1Pfjq-pxIlEqOlKPHHOZmUnSp7ohtmsFXfeMelz54-10/export?format=csv> (관측 2026-11-06).
[^domestic-list]: 구조설계 연구실, Research가 연결한 SDLAB 국내학술지 목록 표. <https://docs.google.com/spreadsheets/d/1bVuBYXutKgwyQAt-Cpd9-LlDfd-GrhqLiISiM_J1gjw/export?format=csv> (관측 2026-11-06).

[^p1]: H.-K. Kim, H.-G. Kwak, Case Studies in Construction Materials 21, e03780 (2024). <https://doi.org/10.1016/j.cscm.2024.e03780> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5061799928,publication_year:2021-2026> (관측 2026-11-06).
[^p2]: S. Kim, H.-G. Kwak, Journal of the Computational Structural Engineering Institute of Korea 37, 25-31 (2024). <https://doi.org/10.7734/coseik.2024.37.1.25> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5061799928,publication_year:2021-2026> (관측 2026-11-06).
[^p3]: S. Kim, H.-G. Kwak, Journal of Asian Architecture and Building Engineering 23, 1841-1853 (2024). <https://doi.org/10.1080/13467581.2023.2278459> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5061799928,publication_year:2021-2026> (관측 2026-11-06).
[^p4]: M. Lee, H.-G. Kwak, International Journal of Damage Mechanics 32, 424-441 (2023). <https://doi.org/10.1177/10567895221146578> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5061799928,publication_year:2021-2026> (관측 2026-11-06).

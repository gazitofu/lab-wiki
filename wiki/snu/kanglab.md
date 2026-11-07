# KANG LAB

**서울대학교 공과대학 기계공학부 · 강준호 조교수**

- 국문 이름: 정밀 생체계측 연구실
- 영문 이름: Precision Bioinstrumentation Lab
- 분야: 정밀 생체계측, 세포·조직 물리학, 미세유체·광학 장치
- 대분야: 기계·로봇·제조, 기초생명·생물물리
- 태그: 미세유체[^home][^research], 광학 영상·현미경[^research], 바이오정보학·계산생물학[^research]
- 홈페이지: <https://kanglab.snu.ac.kr/>
- 근거와 출처: [KANG LAB 근거 페이지](kanglab-sources.md)

> 살아 있는 세포를 재는 장치를 만들고, 세포의 물리적 특성과 시간에 따른 변화를 설명하는 계산 모형을 연구한다.

## 무엇을 연구하나

KANG LAB은 생체계측(생물의 상태를 물리량으로 재는 일)을 연구한다. 세포(생명체의 구조와 기능을 이루는 기본 단위)의 질량(물질의 양을 나타내는 물리량), 부피(차지하는 공간의 크기), 강성(힘에 따른 변형에 저항하는 정도), 모양을 재는 장치를 만들고, 이 값들이 세포의 활동과 어떻게 연결되는지 분석한다. 연구의 출발점은 세포를 관찰하는 데 필요한 측정 도구를 직접 만드는 것이다.[^home][^research]

첫째는 **진동하는 구조로 세포 하나의 물리적 특성을 재는 일**이다. 진동은 일정한 상태를 중심으로 반복해서 변하는 현상이다. 연구실은 미세유체(가느다란 통로에서 적은 양의 액체를 흘리고 섞고 나누는 기술) 통로를 공진기(특정한 주기적 자극에서 진동 응답이 커지는 장치) 안에 넣은 계측 시스템을 다룬다. 세포가 통로를 지나갈 때 주파수(단위 시간당 진동의 반복 횟수)가 바뀌는 정도로 부력 질량을 읽는다. 부력 질량은 물체의 질량에서 같은 부피의 주변 유체 질량을 뺀 값이다. 흐름을 조절하고 빛을 이용한 측정을 결합해 세포의 부피와 강성 등도 살핀다.[^research]

둘째는 **살아 있는 세포층의 입체 모양을 계속 관찰하는 일**이다. 연구실은 광학(빛의 발생·전파와 물질과의 상호작용을 다루는 분야)과 미세유체 구조를 결합한 자체 바이오칩(생물학적 반응이나 측정·분석 기능을 작은 구조 안에 모은 장치)을 개발한다.[^home][^research] 표면에 붙어 있는 세포와 조직(여러 세포가 모여 일정한 구조와 기능을 이루는 단위)을 이루는 세포층이 대상이다. 세포의 모양을 영상으로 기록하는 새 장치를 만들어 집단적인 구조 변화를 연구한다.[^research]

셋째는 **측정값에서 세포의 변화를 설명하고 예측하는 계산 방법**이다. 연구실은 기계학습(자료에서 규칙을 학습해 새 자료를 분석하거나 예측하는 계산 방법)과 물리 기반 모형을 개발해 세포의 물리적 상태가 시간에 따라 바뀌는 모습을 분석한다. 개별 세포를 분류하는 자체 모형도 개발하며, 같은 집단 안에서 나타나는 세포 사이 차이를 연구한다.[^research]

## 주요 연구 주제

### 단일 세포 계측과 생장 변동

세포 하나를 반복해서 재면 집단의 평균값에 가려진 변화를 살필 수 있다. 대표 논문 1은 백혈병 세포의 질량 증가를 세포 계보를 따라 측정하고, 생장률의 무작위 변동이 세포 크기나 분열과 별개로 세포 사이 생장 차이를 만든다고 분석했다. 여기서 세포 계보는 세포가 분열해 이어지는 부모·자식 관계다. 세포 생장 변동의 정량 관계를 다룬 연구다.[^p1]

### 세포층의 높이와 모양을 재는 광학 장치

대표 논문 2의 사전 공개본은 여러 층의 미세 기둥과 음성 염색 광학을 결합한 장치를 제시했다. 음성 염색은 관찰 대상을 제외한 주변에 색이나 밝기 차이를 주어 대상의 윤곽을 드러내는 방법이다. 형광(물질이 빛을 흡수한 뒤 빛을 내며 자극이 사라지면 발광도 곧 사라지는 현상) 배제 영상과 장치 안의 기준 공간을 이용해 세포층의 높이를 연속적으로 재고, 수평 방향과 높이 방향의 변화가 서로 다른 양상을 보임을 분석했다.[^p2]

### 세포 분열과 상태 변화를 나누는 계산 모형

대표 논문 3의 사전 공개본은 여러 시점에 얻은 세포 집단의 분포(각 값이나 범주에 해당하는 정도가 나타나는 양상)에서 세포 상태의 시간 변화를 추론하는 방법을 제시했다. 개별 세포를 계속 따라가지 않고도 세포 안에서 진행되는 상태 변화와 세포 분열로 집단 구성이 바뀌는 효과를 분리한다. 부피, 면적, 세포가 가진 유전 물질의 양에 적용해 시간에 따른 변화를 분석했다.[^p3]

## 대표 논문

서울대 재직 시기에 발표한 연구 가운데 세포 생장, 입체 형상 계측, 집단 자료의 계산 분석, 세포와 나노구조의 상호작용을 다룬 논문을 골랐다. 사전 공개본은 학술지 논문과 구분했다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문 | 주요 저자와 강준호 교수의 참여 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2026 | [Stochasticity in mammalian cell growth rates drives cell-to-cell variability independently of cell size and divisions](https://doi.org/10.1073/pnas.2516372123)[^p1] | 공동 1저자 Ethan Levien·Joon Ho Kang, 마지막 저자 Teemu P. Miettinen[^papers] | 백혈병 세포의 질량 증가를 계보를 따라 측정했다. 세포 크기·분열과 독립적인 짧은 시간의 생장 변동이 세포 사이 생장률 차이와 장기적인 생장 양상을 만든다는 정량적 틀을 제시했다. |
| 2 | 2026 | [Continuous, high-speed 3D topographic profiling of living tissue monolayers](https://doi.org/10.64898/2026.07.23.740215)[^p2] · bioRxiv 사전 공개본 | 1저자 Daeeun Shin, 마지막 저자 Joon Ho Kang | 미세 기둥 구조와 빛을 이용한 영상을 결합해 살아 있는 세포층의 높이를 연속해서 재는 장치를 개발했다. 세포층의 높이 변화와 수평 방향 변화가 서로 다른 시간 양상을 보임을 밝혔다. |
| 3 | 2026 | [Division-resolved inference of flow and trajectories in proliferating cell populations](https://doi.org/10.64898/2026.09.03.747958)[^p3] · bioRxiv 사전 공개본 | 1저자 Geunwoo Shin, 마지막 저자 Joon Ho Kang | 여러 시점의 집단 자료에서 세포 상태의 진행과 세포 분열의 영향을 분리하는 계산 방법을 개발했다. 개별 세포를 계속 추적하기 어려운 경우에도 부피·면적 등의 시간 변화를 추론하는 방법이다. |
| 4 | 2025 | [Cellular Nanointerface of Vertical Nanostructures: Impact of Size‐Modulated Nanopillar Arrays on Neuronal Morphology, Maturation, and Synapse Formation](https://doi.org/10.1002/sstr.202400314)[^p4] | 1저자 Younghak Cho, 공저자 Joon Ho Kang, 마지막 저자 Hyejeong Seong | 기둥 배열에서 기둥 간격과 지름의 비가 신경세포의 모양·성숙·연결 형성에 미치는 영향을 분석했다. 이 비가 작아지면 신경세포의 돌기 성장과 성숙은 촉진되지만 세포 사이 연결의 밀도는 낮아지는 관계를 보였다. |

## 교수와 전문 분야

강준호 교수는 Columbia University에서 물리학 학사학위(2012), MIT에서 물리학 박사학위(2019)를 받았다. KIST 뇌과학연구소에서 위촉연구원(2019년 8월–2021년 6월), 선임연구원(2021년 7월–2023년 8월)으로 일했으며, 연구실은 2023년 9월 서울대에서 출범했다.[^prof][^home]

학과가 적은 연구 분야는 정밀 생체계측 및 센싱, 세포·조직 물리학, 바이오마이크로시스템 및 미세유체학, 인공지능 및 계산 기반 생물물리 분석이다. 센싱은 대상의 상태를 감지해 측정값으로 바꾸는 일이며, 생물물리는 생명 현상을 물리학의 원리와 정량 방법으로 연구하는 분야다.[^prof] 대표 논문에서는 세포의 물리량을 재는 장치 개발과, 그 측정값으로 생장 및 세포 집단의 시간 변화를 설명하는 계산 분석이 전문 분야로 이어진다.[^p1][^p2][^p3]

## 응용 분야

연구실은 기초 세포생물학과 의료 응용을 위해 단일 세포 계측 도구를 개발한다. 표면에 붙어 있는 세포의 모양을 관찰하고, 세포의 건강 상태를 나타낼 수 있는 물리적 특징을 찾는 것을 목표로 한다.[^research] 대표 연구의 장치와 계산 방법은 살아 있는 세포층의 형태 변화 관찰과, 장기간 개별 세포를 추적하기 어려운 집단의 상태 변화 분석을 다룬다.[^p2][^p3]

## 구성원

구성원 페이지의 대학원생과 학부·학부 졸업 후 연구생 구획을 옮겼다. 첫 합류는 인턴·학부 연구 참여를 포함한 소식의 시작 연월이며 대학원 입학 연월을 뜻하지 않는다. BS/MS/PhD program과 BS/MS program은 게시된 과정명을 그대로 표시했다. 대표 논문 참여는 전체 저자 목록과 이름 철자·순서가 일치하는 경우에 표시했다.[^members][^home]

| 이름 | 과정 | 첫 합류 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Daeeun Shin | 석박사통합과정 | 2023.09 | d.shin@snu.ac.kr | 2 |
| Hyunju Ham | 석박사통합과정 | 2023.09 | hyunju@snu.ac.kr | 4 |
| Geunwoo Shin | 석박사통합과정 | 2024.07 | sgw0628@snu.ac.kr | 3 |
| Sechan Park | 석사과정 | 2024.09 | sechan104@snu.ac.kr |  |
| Jiyul Kim | 석사과정 | 2024.09 | kjywldbf@snu.ac.kr |  |
| Minsu Park | 석박사통합과정 | 2025.04 | rkqslant920@snu.ac.kr |  |
| Junggwon Kim | 석박사통합과정 | 2025.01 | junggwon23@snu.ac.kr |  |
| Junyong Um | BS/MS/PhD program | 2024.08 | jyeom10@snu.ac.kr |  |
| Jimin Park | BS/MS program | 2024.07 | hawkshaw0110@snu.ac.kr | 2 |
| Induk Um | 석박사통합과정 | 2026.01 | induk.um@snu.ac.kr |  |
| Jihye Ahn | 석박사통합과정 | 2026.02 | dkswlgp66@snu.ac.kr | 2 |
| Hyunsu Go | Undergraduate & Post-undergraduate students | 2024.07 |  |  |

## 졸업생과 이전 구성원

구성원 페이지 Alumni의 박사후연구원과 학부 연구생 구획을 옮겼다. 진로와 프로그램은 연구실이 적은 표기다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 랩이 적은 프로그램 |
|---|---|---|---|
| Andrew Choi | 박사후연구원 | Assistant professor of Mechanical engineering in Hanyang University |  |
| Seokyoung Song | 박사후연구원 | Research professor in Seoul National University Hospital |  |
| Seoyeong Kim | 학부 연구생 |  | Internship program |
| Yului Jeong | 학부 연구생 |  | Internship program |
| Jaeyoung Hwang | 학부 연구생 |  | UROP program |
| Hojeong Sun | 학부 연구생 |  | UROP program |
| Geonmoo Lee | 학부 연구생 |  | UROP program |
| Jinyoung Lee | 학부 연구생 |  | Intership program |
| Byungkyu Kim | 학부 연구생 |  | Intership program |
| Jiwoo Eun | 학부 연구생 |  | UROP program |
| Seunghoon Lee | 학부 연구생 |  | UROP program |

## 최근 5년 논문 목록

연구실 Publications의 제목·저자·발표처를 옮겼다. 이 목록에는 2023년 9월 서울대 부임 전 강준호 교수의 연구도 포함되어 있다. 별표는 공동 1저자, 더하기는 공동 교신저자라는 누리집의 표시다. 사전 공개본 두 편은 bioRxiv로 구분하고 연구실의 in revision·submitted 상태를 함께 표시했다.[^papers]

**2026**

- E Levien\*, JH Kang\*, K Biswas, SR Manalis, A Amir, TP Miettinen. "Stochasticity in mammalian cell growth rates drives cell-to-cell variability independently of cell size and divisions". *Proceedings of the National Academy of Sciences*. <https://doi.org/10.1073/pnas.2516372123>
- D Shin, J Park, J Ahn, A Choi, JH Kang. "Continuous, high-speed 3D topographic profiling of living tissue monolayers". *in revision*. <https://doi.org/10.64898/2026.07.23.740215> bioRxiv 사전 공개본.
- G Shin, TP Miettinen, JH Kang. "Division-resolved inference of flow and trajectories in proliferating cell populations". *submitted*. <https://doi.org/10.64898/2026.09.03.747958> bioRxiv 사전 공개본.

**2025**

- Y Cho, S Kim, HJ Cho, H Ham, KE Lee, HW Kang, YW Jeong, JH Ahn, N Choi, JH Kang, AJ Chung, H Seong. "Cellular nanointerface of vertical nanostructures: impact of size‐modulated nanopillar arrays on neuronal morphology, maturation, and synapse formation". *Small Structures*. <https://doi.org/10.1002/sstr.202400314>

**2021**

- J Lengefeld, CW Cheng, P Maretich, M Blair, H Hagen, MR McReynolds, E Sullivan, K Majors, C Roberts, JH Kang, JD Steiner, TP Miettinen, SR Manalis, A Antebi, SJ Morrison, JA Lees, LA Boyer, ÖH Yilmaz, A Amon. "Cell size is a determinant of stem cell potential during aging". *Science Advances*. <https://doi.org/10.1126/sciadv.abk0271>

## 연락과 위치

- 교수 이메일: joonhokang@snu.ac.kr.[^contact]
- 교수 기관 전화: 02-880-1594.[^prof]
- 주소: 서울특별시 관악구 관악로 1 서울대학교 301동, 우편번호 08826.[^contact]
- 교수 사무실: 301동 1506호.[^prof][^members][^contact]
- 연구실: 301동 220호.[^prof][^contact]
- 구성원 페이지의 대학원생 사무공간: 301동 1201호.[^members]
[^home]: KANG LAB, HOME. <https://kanglab.snu.ac.kr/home> 관측일 2026-11-07.
[^research]: KANG LAB, RESEARCH의 Mechanical Biosensors·Optical Biochip·AI & Computational Modeling 설명. <https://kanglab.snu.ac.kr/research> 관측일 2026-11-07.
[^members]: KANG LAB, MEMBERS. <https://kanglab.snu.ac.kr/members> 관측일 2026-11-07.
[^papers]: KANG LAB, PUBLICATIONS와 공동저자 기호 설명. <https://kanglab.snu.ac.kr/publications> 관측일 2026-11-07.
[^contact]: KANG LAB, CONTACT. <https://kanglab.snu.ac.kr/contact> 관측일 2026-11-07.
[^prof]: 서울대학교 기계공학부, 강준호 교수 상세의 직급·학력·경력·연구 분야·전화·위치. <https://me.snu.ac.kr/snu__professor/%ea%b0%95%ec%a4%80%ed%98%b8-kang-joon-ho/> 관측일 2026-11-07.
[^p1]: E. Levien 외, T. P. Miettinen, Proceedings of the National Academy of Sciences (출판일 2026-03-03). <https://doi.org/10.1073/pnas.2516372123> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5050311132,publication_year:2021-2026> 관측일 2026-11-07.
[^p2]: D. Shin 외, J. H. Kang, bioRxiv (Cold Spring Harbor Laboratory) (출판일 2026-07-26). <https://doi.org/10.64898/2026.07.23.740215> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5050311132,publication_year:2021-2026> 관측일 2026-11-07.
[^p3]: G. Shin, T. P. Miettinen, J. H. Kang, bioRxiv (Cold Spring Harbor Laboratory) (출판일 2026-09-03). <https://doi.org/10.64898/2026.09.03.747958> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5050311132,publication_year:2021-2026> 관측일 2026-11-07.
[^p4]: Y. Cho 외, H. Seong, Small Structures (출판일 2024-09-23). <https://doi.org/10.1002/sstr.202400314> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5050311132,publication_year:2021-2026> 관측일 2026-11-07.

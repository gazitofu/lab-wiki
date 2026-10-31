# OSML (Optical Structures & Materials Lab)

**서울대학교 공과대학 재료공학부 · 이명재 부교수**

- 분야: 빛과 물질의 상호작용, 광학 구조·재료 설계, 빛의 전파와 광소자 집적
- 대분야: 전기전자·반도체·광학, 소재
- 태그: 광집적회로[^p2], 광검출기[^p2], 레이저 광원[^p3], 소자 설계 시뮬레이션[^laserdesign], 메타물질·메타광학[^p4]
- 홈페이지: <https://osml.snu.ac.kr/home>
- 근거와 출처: [OSML 근거 페이지](osml-sources.md)

> 빛이 가는 길과 재료의 구조를 함께 설계해, 빛을 안내하고 검출하고 만들어 내며 색에 따라 나누는 광학 부품과 그 결합 방법을 연구한다.[^home][^p1][^p2][^p3][^p4]

## 무엇을 연구하나

OSML은 빛과 물질이 서로 영향을 주는 방식을 조절하는 연구실이다. 연구 방향은 광학 구조(빛의 진행과 반응을 조절하도록 만든 재료의 모양과 배열) 설계, 재료의 전자기적·광전기적 특성 분석, 다음 세대 광학 소자(빛에 관련된 기능을 수행하는 부품) 개발로 이어진다. 전자기적 특성은 전기와 자기에 반응하는 성질이며, 광전기적 특성은 빛과 전기 사이의 변환에 관련된 성질이다.[^home]

연구 전략은 재료 자체의 반응과 그 안팎에서 빛이 움직이는 방식을 함께 설계하는 것이다. 원자(원소의 화학적 성질을 나타내는 물질의 구성 단위)·분자(원자가 화학적 결합으로 연결된 독립된 입자)의 배열을 다루는 한편, 빛의 파동(공간과 시간을 따라 진동이나 변화가 전달되는 현상)이 진행하는 구조도 설계한다. 빛의 파장(파동이 공간에서 반복되는 간격)보다 짧은 간격의 구조를 이용하며, 연구 소개는 재료의 공간 배치와 내부 배열을 함께 다루는 전략을 차세대 광학 재료와 소자 개발로 연결한다.[^research]

최근 연구의 한 갈래는 **광도파로(빛을 정해진 경로로 안내하는 구조)**와 다른 광학 부품의 결합이다. 산화하프늄(하프늄과 산소가 결합한 물질)을 빛의 안내층으로 쓰는 연구는 안내층의 두께와 주변층의 굴절률(진공에서의 빛의 속도를 물질 안에서의 빛의 속도로 나눈 값)·두께가 빛의 전파에 미치는 영향을 살핀다. 다른 연구는 이황화몰리브데넘(몰리브데넘과 황이 결합한 층상 물질) 막의 주변으로 퍼지는 빛을 이용해, 막 표면의 광검출기(빛을 전기 신호로 바꾸는 소자)가 안내되는 빛과 상호작용하도록 만든다. 이들은 빛을 보내는 부품과 감지하는 부품을 결합하는 집적 기술로 이어진다.[^p1][^p2]

다른 갈래는 **빛을 만드는 구조와 제작 공정**이다. 광결정(굴절률이 공간에서 주기적으로 반복되는 구조)을 이용하는 레이저(빛을 증폭해 내보내는 광원)를 다루며, 광결정 구조가 있는 면에 수직으로 빛을 내보내는 소자의 제작법을 연구했다. 반도체 레이저의 기본 층 구조에 깊은 공기 구멍을 만드는 방법을 제시하고, 그 소자가 단일 모드(파동의 공간 분포와 진동 형태가 한 종류로 정해진 상태)로 발진(소자에서 진동이 지속적으로 생기는 현상)하는 것을 보였다.[^p3]

빛의 방향과 색을 나누는 설계도 다룬다. 메타표면(빛을 조절하도록 파장보다 짧은 간격의 구조를 배열한 표면)을 설계해 빨강·초록·파랑 빛을 정해진 검출 영역으로 보낸다. 이 연구는 원하는 빛의 분포에서 출발해 구조를 찾는 역설계(목표로 하는 반응이나 결과에 맞추어 구조·재료를 찾는 설계 방식)를 사용한다.[^p4] 다른 논문은 콜로이드 양자점(주변 물질에 흩어진 상태로 다룰 수 있고 전자 등의 움직임이 모든 방향에서 제한되는 입자형 재료)을 광결정에 넣어 발광(물질이 빛을 내는 현상)의 방향을 제어하고, 방출되는 빛의 파장과 각도에 대한 선택성을 다룬다.[^p5]

## 주요 연구 주제

### 광도파로와 주변 재료의 공동 설계

빛을 안내하는 층뿐 아니라 그 층을 둘러싼 재료도 설계 대상으로 삼는다. 산화하프늄 광도파로 연구에서는 산화규소(규소와 산소가 결합한 물질) 주변층의 위아래 대칭성, 굴절률과 두께가 빛을 안내하는 조건을 정한다는 점을 분석하고, 다른 산화물 안내층에도 같은 접근을 살폈다. CMOS(Complementary Metal–Oxide–Semiconductor, 서로 보완적으로 전류를 제어하는 소자들을 짝지어 쓰는 반도체 회로 기술) 공정과 양립하는 제작 방법을 제시했다.[^p1] 앞선 δ 광도파로 연구는 이황화몰리브데넘 단일층을 이용해 빛이 막을 따라 전파하면서 막에 수직인 방향으로는 갇히게 했고, 빛을 모으는 기능, 격자와 부품 상호 연결, 빛의 세기 조절을 보였다.[^p6]

### 빛을 안내하는 구조와 검출 소자의 집적

광집적회로(빛을 보내고 나누고 바꾸는 부품을 한 칩에 모은 회로)를 위해, 광도파로의 표면에 놓인 소자가 안내되는 빛과 상호작용하도록 만든다. 이황화몰리브데넘 광도파로에 이셀레늄화텅스텐(텅스텐과 셀레늄이 결합한 층상 물질) 광검출기를 직접 결합하고, 빛을 전기로 감지하는 기능을 보였다. 전기장(전기를 띤 입자에 힘이 작용하는 공간의 상태)의 진동 방향과 그 시간 변화를 뜻하는 편광에 따른 선택성도 보였다.[^p2]

### 광결정 레이저의 구조와 공정

광결정 레이저에서는 빛이 생기는 영역과 공기 구멍 배열이 만나는 구조를 설계하고 제작한다. 기존 반도체 레이저의 층 구조를 바탕으로, 한 번의 건식 식각(액체 용액 대신 기체나 입자를 이용해 재료를 제거하는 공정)으로 깊은 구멍 배열을 만드는 방법을 제시했다. 구조를 설계하는 단계에서는 컴퓨터 계산으로 구멍 깊이에 따른 빛의 분포를 분석했다.[^p3][^laserdesign]

### 메타표면 역설계와 발광 방향 제어

메타표면 설계에서는 계산으로 구한 빛의 분포를 신경망(연결된 계산 단위들이 정보를 변환하고 전달하는 계산 모형)에 학습시킨다. 그 모형이 후보 구조를 지나는 빛의 분포를 예측하도록 하고, 유전 알고리즘(후보의 선택·조합·변형을 반복해 조건에 맞는 답을 찾는 계산법)으로 구조를 탐색한다. 목표는 색에 따라 빛을 지정된 위치로 보내는 것이며, 검출 영역의 배치가 바뀌어도 같은 학습 모형을 다시 사용할 수 있음을 보였다.[^p4] 광결정과 콜로이드 양자점을 결합한 연구에서는 구조 안에서 전파하는 빛을 바깥으로 방출하는 조건을 맞추어, 좁은 각도 범위의 방향성 있는 발광을 구현했다.[^p5]

## 대표 논문

2021–2026년 게시 논문 가운데 서울대 재직 시기에 출판되었고, 논문 저자 소속에 서울대학교가 명시된 6편을 골랐다. 광도파로 제작과 광소자 결합, 광결정 광원과 발광 방향 제어, 메타표면 역설계를 나누어 보여 준다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 공동 기여와 교신저자는 논문 본문의 명시적 표시를 따르고, 나머지 저자 역할은 전체 저자 순서대로 적었다.[^p1][^p2][^p3][^p4][^p5][^p6][^suppaff]

| # | 연도 | 논문·학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [CMOS-compatible ultra-thin HfO2 waveguides with tailored cladding symmetry for millimeter-scale light propagation](https://doi.org/10.1063/5.0281182) · APL Photonics | 산화하프늄 안내층을 산화규소 주변층으로 감싸는 광도파로를 CMOS 공정으로 만들었다. 안내층 두께가 빛의 전파에 미치는 영향을 살피고, 주변층의 굴절률과 두께 대칭성을 조절하는 것이 중요함을 보였다. 다른 산화물 안내층에도 이 설계를 적용할 수 있는지 살폈다.[^p1] | 1저자 Hwan Kim·Seungju Kwon(공동 기여), 교신저자 이명재 |
| 2 | 2025 | [Evanescent-field-guiding 2D ultrathin waveguides for seamlessly integrated devices](https://doi.org/10.1021/acs.nanolett.5c03190) · Nano Letters | 이황화몰리브데넘 막 바깥으로 퍼진 빛을 이용해 표면에 놓인 소자와 빛이 상호작용하도록 했다. 이셀레늄화텅스텐 광검출기를 광도파로에 직접 결합하고, 빛을 감지하는 기능과 편광에 따른 선택성을 보였다.[^p2] | 1저자 Samuel Kim·Chengyun Hong(공동 기여), 교신저자 이명재 |
| 3 | 2025 | [1,550-nm photonic crystal surface-emitting laser diode fabricated by single deep air-hole etch](https://doi.org/10.1515/nanoph-2024-0760) · Nanophotonics | 기존 반도체 레이저의 층 구조에서 한 번의 건식 식각으로 깊은 공기 구멍 배열을 만들어, 표면에 수직으로 빛을 내보내는 광결정 레이저를 제작하는 방법을 제시했다. 이 방법으로 만든 소자가 단일 모드로 발진했다.[^p3] | 1저자 Myeongeun Kim, 교신저자 이명재·Heonsu Jeon |
| 4 | 2026 | [Metasurface color routers inverse-designed with a deep learning accelerated genetic algorithm for high efficiency imaging](https://doi.org/10.1088/1361-6633/ae9e8c) · Reports on Progress in Physics | 빛의 분포를 계산한 자료로 신경망을 학습시키고, 그 모형이 후보 구조를 지나는 빛의 분포를 예측하도록 해 유전 알고리즘의 설계 탐색에 사용했다. 빨강·초록·파랑 빛을 정해진 검출 영역으로 보내는 메타표면에 적용했으며, 검출 영역 배치가 달라져도 새 학습 자료나 재학습 없이 같은 모형을 사용할 수 있음을 보였다.[^p4] | 1저자 Hyoseok Park, 마지막 저자 이명재 |
| 5 | 2025 | [Tailoring directional emission of colloidal quantum dots via mode coupling with photonic crystals](https://doi.org/10.1039/D5NR02616D) · Nanoscale | 콜로이드 양자점을 넣은 광결정에서, 구조 안을 따라 전파하는 빛을 바깥으로 방출하는 조건을 맞추어 방향성 있는 빛이 좁은 각도 범위로 나오게 했다. 방출되는 빛의 파장과 각도에 대한 선택성을 함께 높였다.[^p5] | 1저자 Youngjun Chung, 마지막 저자 이명재 |
| 6 | 2023 | [Wafer-scale δ waveguides for integrated two-dimensional photonics](https://doi.org/10.1126/science.adi2322) · Science | 이황화몰리브데넘 단일층으로 빛을 안내하는 δ 광도파로를 만들었다. 빛은 막을 따라 전파하고, 막에 수직인 방향으로는 갇힌다. 광학 부품을 결합해 빛의 진행 방향을 바꾸고 모으는 기능, 격자 기능, 상호 연결과 빛의 세기 조절을 보였다.[^p6] | 1저자 이명재, 마지막 저자 Jiwoong Park |

## 교수와 전문 분야

이명재 부교수는 서울대학교 재료공학부 소속이다. 연구실 People은 서울대 물리학 학사(2006–2011)와 박사(2011–2018), 서울대 기초과학연구원 박사후연구원(2018–2019), 시카고대학교 James Franck Institute 박사후연구원(2019–2022) 경력을 적는다. 서울대에서는 2022–2026년 조교수, 2026년부터 부교수로 적는다.[^people] 학과 교수 소개는 현재 직급을 부교수로 적고, 빛의 진행을 제어하는 구조 설계·제작, 빛과 물질의 상호작용, 재료의 광전기적 특성과 광학 기능 집적을 연구 분야로 소개한다.[^faculty]

최근 논문에서는 광도파로의 재료와 주변층을 함께 설계하는 일, 빛을 검출하는 소자와 광도파로를 결합하는 일, 광결정 레이저의 제작 공정이 전문 분야를 구체적으로 보여 준다.[^p1][^p2][^p3] 광결정의 발광 방향 제어와 학습 모형을 이용한 메타표면 역설계도 다룬다.[^p4][^p5]

## 응용 분야

연구실은 광학 기능을 한 플랫폼에 모으는 집적 기술과 다음 세대 광학 소자 개발을 지향한다.[^faculty][^home] 대표 논문은 빛을 안내하는 부품과 검출 부품의 결합, 반도체 공정과 양립하는 광도파로, 광결정 레이저 제작 방법을 다룬다.[^p1][^p2][^p3] 색에 따라 빛을 검출 영역으로 보내는 설계와, 빛의 방출 방향을 정하는 구조도 연구한다.[^p4][^p5]

## 구성원

2026-10-31 People 페이지에 게시된 교수 외 구성원 15명이다. Post-Doc 1명, Graduate Members 11명, Undergraduate Interns 3명이며, 대학원생의 세부 학위과정 대신 누리집의 구획을 따른다. 권승주는 Lab Manager로도 적혀 있다. 연구 주제는 랩 표기이고, 같은 이름의 저자를 같은 사람으로 보아 대표 논문 참여를 표시했다.[^people]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 강경남 (Kang, Kyungnam) | 박사후연구원 | Optical modeling of optoelectronic devices | knkang@snu.ac.kr |  |
| 백규인 (Baek, Gyuin) | Graduate Members | 3D lithography | qorrbdls2175@snu.ac.kr | 1, 2, 5 |
| 민종관 (Min, Jonggwan) | Graduate Members | Meta-structure design | jonggwanmin@snu.ac.kr | 5 |
| 김사무엘 (Kim, Samuel) | Graduate Members | Optical devices | kimsa127@snu.ac.kr | 1, 2, 4 |
| 권승주 (Kwon, Seungju) | Graduate Members | Optical waveguides | 1207tmdwn@snu.ac.kr | 1, 2 |
| 우선우 (Woo, Sunwoo) | Graduate Members | Photonic integrated circuits | wsw_98@snu.ac.kr | 2, 5 |
| 정영준 (Chung, Youngjun) | Graduate Members | Optical metamaterials | junner9@snu.ac.kr | 1, 2, 5 |
| 김은선 (Kim, Eunsun) | Graduate Members | Photonic Crystals | karen1218@snu.ac.kr | 2 |
| 박세현 (Park, Sehyeon) | Graduate Members | 3D Lithography | clairesp7@snu.ac.kr | 2, 5 |
| 안은영 (Ahn, Eunyoung) | Graduate Members | 3D Lithography | aey9488@snu.ac.kr |  |
| 주인휘 (Joo, Yinhyui) | Graduate Members | Metasurface inverse design | yinhyui98@snu.ac.kr |  |
| 이상호 (Lee, Sangho) | Graduate Members | 3D Lithography | shlee1030@snu.ac.kr |  |
| 류도현 (Ryu, Dohyun) | 학부 인턴 | Thin-film waveguides | rdh831@snu.ac.kr |  |
| 조석형 (Cho, Seokhyeong) | 학부 인턴 | Photonic integrated circuits |  |  |
| 이상민 (Lee, Sangmin) | 학부 인턴 | Optical structure design | leeesm04@snu.ac.kr |  |

## 졸업생과 이전 구성원

People의 Alumni에 게시된 2명이다. 학위·과정과 기간, 진로는 누리집 표기이며, 김환의 학위 논문 제목도 함께 적는다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| 김환 (Hwan Kim) | Master of Engineering (March 2023 – August 2025) | SK hynix | Propagating mode characteristics of ultra-thin waveguides with engineered core-cladding conditions |
| 홍성윤 (Chengyun Hong) | Postdoctoral associate (March 2024 – August 2024) | POSTECH |  |

## 최근 논문 목록 (2021–2026)

Publications의 Journal Articles에 게시된 2021–2026년 논문 13편(12–24번)이다. 2026년 2편, 2025년 5편, 2024년 1편, 2023년 1편, 2022년 3편, 2021년 1편이다. 연도는 각 항목의 학술지 서지에 적힌 연도이고 제목·저자·학술지 표기는 누리집을 따른다. 이명재 교수는 2022년 서울대에 부임했으며, 이 목록에는 부임 전 항목도 포함되어 있다. 저자의 별표와 †는 누리집 표시다.[^pubs][^people]

**2026**

- H. Park†, S. Kim†, D.-Y. Choi, Y. Park\*, and M. Lee\*. "Metasurface color routers inverse-designed with a deep learning accelerated genetic algorithm for high efficiency imaging". *Reports on Progress in Physics, 89, 097901 (2026)*.
- M. Park†, J. Jeong†, C. Lee, J. Jang, M. Lee\*, and Y. Park\*. "The design of metasurface-integrated photonic crystal surface emitting lasers for simultaneous beam shaping and polarization control". *Current Applied Physics, 90, 46-55 (2026)*.

**2025**

- H. Kim†, S. Kwon†, S. Kim, G. Baek, Y. Chung, and M. Lee\*. "CMOS-compatible ultra-thin HfO2 waveguides with tailored cladding symmetry for millimeter-scale light propagation". *APL Photonics, 10, 106109 (2025)*.
- K. Kang, Y. Chung, G. Baek, and M. Lee\*. "Intrinsic chirality in two-dimensional dimer photonic crystals enabled by cross-polarization-suppressed bound states in the continuum". *Current Applied Physics, 80, 169-175 (2025)*.
- S. Kim†, C. Hong†, Y. Chung, S. Kwon, S. Park, G. Baek, S. Woo, E. Kim, and M. Lee\*. "Evanescent-field-guiding 2D ultrathin waveguides for seamlessly integrated devices". *Nano Letters, 25(38), 14066-14073 (2025)*.
- Y. Chung, G. Baek, J. Min, S. Park, S. Woo, and M. Lee\*. "Tailoring directional emission of colloidal quantum dots via mode coupling with photonic crystals". *Nanoscale, 17, 20880-20888 (2025)*.
- M. Kim, Y. Song, L. Jeong,  T. Lee,  H. Choi,  I. Kim,  M. Lee\*, and H. Jeon\*. "1,550-nm photonic crystal surface-emitting laser diode fabricated by single deep air-hole etch". *Nanophotonics, 14(4), 515-522 (2025)*.

**2024**

- J. Kim, M. Lee, M. H. Park, and T.-W. Lee\*. "A case study on the establishment of a CQI System: focused on the department of materials science and engineering at seoul national university". *Journal of Engineering Education Research, 27(6), 14-27 (2024)*.

**2023**

- M. Lee†, H. Hong†, J. Yu, F. Mujid, A. Ye, C. Liang, and J. Park\*. "Wafer-scale δ waveguides for integrated two-dimensional photonics". *Science, 381(6658), 648-653 (2023)*.

**2022**

- J. Yu, C. Liang, M. Lee, S. Das, A. Ye, F. Mujid, P. Poddar, B. Cheng, N. Abbott, and J. Park\*. "Two-dimensional mechanics of atomically thin solids on water". *Nano Letters, 22, 7180-7186 (2022)*.
- A. J. Mannix†, A. Ye†, S. H. Sung, A. Ray, F. Mujid, C. Park, M. Lee, J.-H. Kang, R. Shreiner, A. A. High, D. A. Muller, R. Hovden, and J. Park\*. "Robotic four-dimensional pixel assembly of van der Waals solids". *Nature Nanotechnology, 17, 361-366 (2022)*.
- P. Poddar†, Y. Zhong†, A. Mannix, F. Mujid, J. Yu, C. Liang, J.-H. Kang, M. Lee, S. Xie, and J. Park\*. "Resist-free lithography for monolayer transition metal dichalcogenides". *Nano Letters, 22, 726-732 (2022)*.

**2021**

- M. Lee†, J.-H. Kang†, F. Mujid, J. Suh, A. Ray, C. Park, D. A. Muller, and J. Park\*. "Atomically thin, optically isotropic films with 3D nanotopography". *Nano Letters, 21, 7291-7297 (2021)*.

## 수상과 선정

News & Updates에 게시된 수상 6건이다. 날짜는 누리집 표기이며, 2021-10-22–2026-10-22에 해당하는 항목을 싣는다. 박세현의 한 학생 포스터 발표상 기간은 시작 연도가 종료 연도보다 뒤인 ‘2026.04.28~2025.04.30’으로 게시되어 있어 그 표기를 그대로 둔다.[^news]

- 2026.07.09~2026.07.11 · 김사무엘, Student Poster Presentation Award(학생 포스터 발표상) 수상
- 2026.6.18 · 정영준, Grand Quest Forum에서 수상
- 2026.5.31~2026.6.04 · 안은영, Student Poster Presentation Award(학생 포스터 발표상) 수상
- 2026.04.28~2025.04.30 · 박세현, Student Poster Presentation Award(학생 포스터 발표상) 수상
- 2026.2.3~2026.2.06 · 안은영, Student Oral Presentation Award(학생 구두 발표상) 수상
- 2025.10.29 · 박세현, Student Poster Presentation Award(학생 포스터 발표상) 수상

## 연락과 위치

- 주소: 서울특별시 관악구 관악로 1, 서울대학교 재료공학부, 우편번호 08826[^home]
- 교수 연구실: 33동 318호, 전화 +82-2-880-5819[^people]
- 실험실: 131동 411호·201호·207호, 전화 +82-2-880-7197[^home]
- 교수 이메일: myungjae@snu.ac.kr[^home][^people]
[^p1]: H. Kim 외, M. Lee, APL Photonics 10, 106109 (온라인 2025-10-10). <https://doi.org/10.1063/5.0281182> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/396402762_CMOS-compatible_ultra-thin_HfO2_waveguides_with_tailored_cladding_symmetry_for_millimeter-scale_light_propagation> (2026-10-31 열람).
[^p2]: S. Kim 외, M. Lee, Nano Letters 25, 14066–14073 (온라인 2025-09-10). <https://doi.org/10.1021/acs.nanolett.5c03190> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/395399019_Evanescent-Field-Guiding_2D_Ultrathin_Waveguides_for_Seamlessly_Integrated_Devices> (2026-10-31 열람).
[^p3]: M. Kim 외, H. Jeon, Nanophotonics 14, 515–522 (2025). <https://doi.org/10.1515/nanoph-2024-0760> 초록 기준(출판사 논문 페이지). 초록 원문 <https://onlinelibrary.wiley.com/doi/full/10.1515/nanoph-2024-0760> (2026-10-31 열람).
[^p4]: H. Park 외, M. Lee, Reports on Progress in Physics 89, 097901 (2026). <https://doi.org/10.1088/1361-6633/ae9e8c> 초록 기준(Crossref 등록 초록). OpenAlex 등록 출판일 2026-08-25. 초록 원문 <https://api.crossref.org/works/10.1088/1361-6633/ae9e8c> (2026-10-31 열람).
[^p5]: Y. Chung 외, M. Lee, Nanoscale 17, 20880–20888 (2025). <https://doi.org/10.1039/D5NR02616D> 초록 기준(Crossref 등록 초록). OpenAlex 등록 출판일 2025. 초록 원문 <https://api.crossref.org/works/10.1039/D5NR02616D> (2026-10-31 열람).
[^p6]: M. Lee 외, J. Park, Science 381, 648–653 (2023). <https://doi.org/10.1126/science.adi2322> 초록 기준(Crossref 등록 초록). OpenAlex 등록 출판일 2023-08-10. 초록 원문 <https://api.crossref.org/works/10.1126/science.adi2322> (2026-10-31 열람).
[^home]: OSML, Home, 연구 방향과 연락처. <https://osml.snu.ac.kr/home> (2026-10-31 열람).
[^research]: OSML, Research, Vision & Strategy. <https://osml.snu.ac.kr/research> (2026-10-31 열람).
[^people]: OSML, People, 교수 경력·구성원·Alumni. <https://osml.snu.ac.kr/people> (2026-10-31 열람).
[^faculty]: 서울대학교 재료공학부, 이명재 교수 소개, 소속·경력·연구 관심 분야. <https://mse.snu.ac.kr/lee-myungjae/> (2026-10-31 열람).
[^pubs]: OSML, Publications, Journal Articles. <https://osml.snu.ac.kr/publications> (2026-10-31 열람).
[^news]: OSML, News & Updates, 수상 게시 항목. <https://osml.snu.ac.kr/news-updates> (2026-10-31 열람).
[^laserdesign]: Myeongeun Kim 외, 1,550-nm photonic crystal surface-emitting laser diode fabricated by single deep air-hole etch, Nanophotonics 14(4), 515–522 (2025), §2 Design of device structure의 구조 최적화와 유한차분 시간영역 계산. <https://onlinelibrary.wiley.com/doi/full/10.1515/nanoph-2024-0760> (2026-10-31 열람).
[^suppaff]: OpenAlex 등록 서지, 대표 후보 5편의 원저자 이름·저자 소속·등록 출판일. <https://api.openalex.org/works?per-page=10&select=doi,title,publication_date,authorships&filter=doi:10.1088/1361-6633/ae9e8c%7C10.1016/j.cap.2026.06.015%7C10.1016/j.cap.2025.09.015%7C10.1039/d5nr02616d%7C10.1126/science.adi2322> (2026-10-31 열람).

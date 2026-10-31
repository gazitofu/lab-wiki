# 나노역학&멀티 피직스 재료모사 실험실 (N3M, Nanomechanics & Multiphysics Materials Modeling Lab)

**서울대학교 공과대학 재료공학부 · 류일 조교수**

- 분야: 재료의 변형·파괴, 결함 동역학과 다중 규모·다중 물리 모사, 나노구조 금속 설계와 신뢰성 해석
- 대분야: 소재, 기계·로봇·제조
- 태그: 고체역학·소성[^mechanics], 전산역학·수치 해석[^model], 결함 공학[^defects], 합금 설계·금속 구조 소재[^metals], 과학·공학 AI[^design], 설계 최적화(위상·형상 최적화)[^design], 이차전지 소재[^battery]
- 홈페이지: <https://n3m.snu.ac.kr/>
- 근거와 출처: [N3M 근거 페이지](n3m-sources.md)

> 금속 내부 결함의 움직임을 계산해 구멍·격자 구조와 첨가 원소가 재료의 변형에 미치는 영향을 밝히고, 충격을 받는 금속의 변형과 전지·전자소자의 신뢰성을 연구하는 연구실이다.[^p1][^p2][^p3][^p4][^research]

## 무엇을 연구하나

류일 조교수가 이끄는 N3M은 재료가 힘을 받을 때 어떻게 변형하고 파손되는지를 이론과 계산 모형으로 연구한다. 실제 재료의 거동을 컴퓨터에서 재현하는 모사를 이용하고, 이를 위한 계산 모형 자체도 개발한다. 다양한 환경에서 재료의 변형과 파손을 이해하고 예측해 공학 재료의 설계에 활용하는 것이 목표다.[^home][^professor]

핵심은 재료 내부의 결함이다. 결정은 원자가 규칙적으로 배열된 고체 구조이고, 결함은 그 규칙적인 배열에서 벗어난 부분이다. 연구실은 전위(결정에서 원자 배열이 어긋난 선 형태의 결함)의 움직임으로 소성 변형(힘을 없앤 뒤에도 남는 변형)을 설명한다. 전위가 결정립계(원자 배열의 방향이 다른 결정 영역 사이의 경계)에서 생성되거나 사라지는 과정과, 경계와의 상호작용이 재료 전체의 기계적 거동에 어떻게 이어지는지를 연구한다.[^mechanics][^metals]

계산에서는 다중 규모 모형(서로 다른 공간·시간 규모의 현상을 연결하는 모형)을 개발해 결함의 세부 움직임과 재료 전체의 변형을 함께 다룬다. 다중 물리 모형은 서로 영향을 주는 물리 현상을 함께 다루는 모형이다. 연구실은 이런 모형으로 극한 온도, 빠른 변형, 수소와 방사선 등의 환경에서 금속의 변형과 파손을 살피며, 결함 구조에 바탕을 둔 손상 모형도 연구한다.[^model][^research]

응용 대상에는 전지 전극과 전자소자가 있다. 전극은 전기 회로와 전지 내부 반응을 연결하는 부분이다. 연구실은 충전과 방전을 반복할 때 전지 소재가 변형하고 파손되는 과정을 역학과 다른 물리 현상을 결합해 계산하려 한다. 전자소자에서는 결함의 미세구조(재료 내부의 결정 영역과 결함 등이 이루는 구조)를 고려해 재료와 구조의 변형·파손을 예측하고, 안정적으로 작동하는 설계를 돕는 신뢰성 해석을 연구한다.[^battery][^reliability]

재료의 설계에는 기계학습(자료에서 규칙을 학습해 예측과 판단에 쓰는 계산 방법)도 활용한다. 연구실은 힘을 받아 끊어질 때까지 변형되는 성질인 연성과, 파괴에 저항하며 에너지를 흡수하는 성질인 인성을 함께 고려한다. 결함의 미세구조를 설계 대상으로 삼고, 여러 설계 목표를 함께 다루는 다목적 최적화로 그 구조를 찾는 접근을 소개한다.[^design]

## 주요 연구 주제

### 1. 결함의 움직임과 재료 전체의 변형 연결

전위 동역학(전위의 움직임과 상호작용을 시간에 따라 계산하는 방법)을 통해 소성 변형의 원인을 밝힌다. 결함의 움직임을 다루는 모형과 재료 전체의 힘·변형 관계를 연결하고, 서로 영향을 주는 물리 현상까지 함께 계산하는 모형을 개발한다. 결정 재료의 결함 구조를 바탕으로 파손 과정도 해석한다.[^mechanics][^model]

### 2. 나노구조 금속과 결정 경계

나노구조는 나노미터 단위의 특징적인 구조를 갖는 재료 구조를 뜻한다. 연구실은 나노구조 금속의 기계적 성질을 이해하기 위해 전위와 결정립계의 상호작용을 연구한다. 결정립계는 전위가 생기는 곳이나 사라지는 곳으로 작용하기도 하며, 이런 차이가 재료 전체의 기계적 반응에 영향을 준다고 설명한다. 개별 결함과 경계의 작용을 모형에 담아 금속의 성질을 조사하는 접근이다.[^metals]

### 3. 극한 환경, 전지와 전자소자의 파손

극한 온도, 빠른 변형, 수소와 방사선의 영향을 받는 재료가 연구 대상이다. 수소 취성은 수소의 영향으로 재료가 부서지기 쉬워지는 현상이다. 연구실은 이런 조건에서의 소성 변형과 결정 재료의 손상을 모형화한다. 전지에서는 전극 소재의 충방전에 따른 변형·파손을, 전자소자에서는 결함 구조를 고려한 기계적 신뢰성을 다룬다.[^research][^battery][^reliability]

### 4. 결함 미세구조의 데이터 기반 설계

연구실은 미세구조의 다양한 구성과 자료를 처리하는 기계학습을 결합해 연성과 인성을 함께 고려하는 재료 설계를 연구한다. 여러 목표를 동시에 고려하는 최적화로 결함 미세구조를 설계하는 것이 이 갈래의 중심이다.[^design]

## 대표 논문

류일 교수의 서울대 소속이 확인된 논문 가운데 다공성 금속, 첨가 원소에 따른 변형, 나노격자, 충격 변형을 다루는 4편을 골랐다. 표의 연도는 출판사 권호 연도를 우선하고, 출판사 권호 연도를 따로 확인하지 않은 두 편은 등록 서지의 출판 연도를 썼다. 1번은 2025년에 온라인으로 공개되고 2026년 권호에 실렸으며, 2번은 2024년에 온라인으로 공개되고 2025년 권호에 실렸다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다.[^p1][^p2][^p3][^p4]

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Dislocation plasticity in porous micropillars under uniaxial loading](https://doi.org/10.1016/j.jmst.2025.08.058) · Journal of Materials Science & Technology | 구멍이 있는 알루미늄 금속 기둥의 변형을 전위 동역학과 유한요소법(대상을 부분으로 나눠 각 부분의 관계식을 풀고 전체 거동을 계산하는 방법)을 결합해 조사했다. 구멍의 크기·형상과 재료 밀도가 강도(힘에 의한 변형과 파손을 견디는 정도)에 미치는 영향을 살폈다. 구멍이 전위를 만들어 내는 구조의 길이를 줄이고 전위 이동을 방해해 강도를 높일 수 있는 과정을 설명했고, 모형의 결과는 관련 실험 결과와 잘 맞았다.[^p1] | 1저자 Phu Cuong Nguyen; 교신 표시 \* Ill Ryu |
| 2 | 2025 | [Incipient plasticity of potassium-doped tungsten under nanoindentation: A comparison between experiments and defect dynamics simulations](https://doi.org/10.1016/j.jmst.2024.10.036) · Journal of Materials Science & Technology | 칼륨을 첨가한 텅스텐을 나노압입(탐침으로 재료 표면을 눌러 힘과 변형을 조사하는 시험)으로 분석하고 결함 동역학 모사와 비교했다. 재료 내부의 칼륨 기포 주변에 응력(재료 내부의 어떤 면을 통해 단위 면적당 전달되는 힘)이 집중되면서 전위가 생기고 소성 변형이 촉진되는 과정을 설명했다. 모사에서는 이 과정으로 소성 변형이 시작되는 데 필요한 응력이 낮아졌고, 실험과 잘 맞았다.[^p2] | 1저자 Guensik Min·Jeongseok Kim·Phu Cuong Nguyen(공동 기여); 교신 표시 \* Ill Ryu·Heung Nam Han |
| 3 | 2024 | [Size dependent scaling law of plastic flow in FCC nanolattices: A dislocation dynamics study](https://doi.org/10.1016/j.actamat.2024.120022) · Acta Materialia | 면심입방(FCC, Face-Centered Cubic, 단위 결정의 꼭짓점과 각 면 중심에 원자가 놓이는 배열) 구조인 알루미늄의 나노격자를 연구했다. 나노격자는 나노미터 규모의 부재가 이어진 격자 구조다. 전위 동역학과 유한요소법을 결합해 구조 내부의 전위 움직임과 변형을 계산했다. 격자를 이루는 부재가 가늘어질 때 강도가 커지는 관계와, 격자 형상의 영향을 조사해 구조 설계의 기초를 제시했다.[^p3] | 1저자 Phu Cuong Nguyen; 마지막 저자 Ill Ryu(OpenAlex에 교신 저자로 등록) |
| 4 | 2024 | [Understanding dislocation plasticity of single crystalline Ta micropillars under dynamic loading](https://doi.org/10.1016/j.jmrt.2024.05.009) · Journal of Materials Research and Technology | 충격을 받는 탄탈럼 단결정(전체에 걸쳐 원자 배열의 방향이 이어진 결정)의 변형을 조사했다. 전위 동역학과 유한요소법을 결합해 충격 중의 전위 움직임과 상호작용을 추적하고, 결정 방향과 온도 등 조건의 영향을 살폈다. 모사 결과는 실험 관찰과 잘 맞았으며, 충격으로 변형된 형상을 이해하는 데 필요한 힘의 작용도 분석했다.[^p4] | 1저자 Nicole K. Aragon; 마지막 저자 Ill Ryu(OpenAlex에 교신 저자로 등록) |

## 교수와 전문 분야

류일 조교수는 서울대학교 재료공학부에서 학사(2005)와 석사(2007), Stanford University에서 박사(2013) 학위를 받았다. 2013–2016년 Brown University에서 박사후연구원으로, 2016–2024년 The University of Texas at Dallas 기계공학과에서 조교수로 일했고, 2024년 서울대학교 재료공학부 조교수로 부임했다. 학과 소개는 Research Institute of Advanced Materials의 겸임 연구원(Adjunct Researcher)도 함께 적는다.[^professor][^department]

교수가 직접 소개한 전문 분야는 재료의 소성 변형과 파괴, 전위와 결정 경계·균열의 상호작용, 다중 규모 결함 모형, 나노구조의 설계, 전지와 전자소자의 파손 해석이다. 학과 소개는 나노 격자 구조와 구멍을 포함한 금속 기둥의 소성 변형도 주요 연구 관심으로 든다.[^professor][^department]

## 응용 분야

연구실은 결함 구조와 기계적 성질을 연결해 재료 설계에 활용하고자 한다. 전지에서는 전극 소재가 충방전 중 겪는 변형과 파손을, 전자소자에서는 재료·제조 공정·구조를 고려한 기계적 신뢰성을 연구한다. 교수 소개는 리튬이온전지의 실리콘 음극이 충방전 중 부풀고 파손되는 현상과 전자소자의 금속 박막을 구체적인 대상으로 적는다. 음극은 전지가 방전할 때 전자를 외부 회로로 내보내는 전극이고, 박막은 얇은 막 형태의 재료다.[^research][^professor]

## 구성원

2026년 10월 30일 Members 쪽에 게시된 교수 외 구성원 14명이다. 대학원생 구획 9명, 학부 인턴 구획 2명, 공동 지도 구획 3명으로 나뉜다. 과정과 학교 이메일은 게시 표기이며, 시작은 개인 소개의 Since 또는 과정 이력에 적힌 시점이다. 안응규·이호영의 2025년은 석사과정 시작 연도다. 심규장의 Ph.D. Candidates는 박사과정으로 옮기고, 과정이 따로 적히지 않은 공동 지도 학생은 Co-advised Student 표기를 유지했다. 「대표 논문 참여」는 대표 논문 저자의 전체 이름과 일치할 때 표시하는 번호다.[^members][^member-details]

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 연경미 (Kyeongmi Yeon) | 박사과정 | 2024.09~ | kyeongmxi@snu.ac.kr |  |
| 안응규 (Eungkyu Ahn) | 석사과정 | 2025 – present | aeg1006@snu.ac.kr |  |
| 성준호 (Junho Seong) | 박사과정 | 2025.03~ | wnswjswk1@snu.ac.kr |  |
| 이호영 (Hoyeong Lee) | 석사과정 | 2025 – present | ghdud7150@snu.ac.kr |  |
| 신찬재 (Chanjae Shin) | 석사과정 | 2025.03~ | as13562@snu.ac.kr |  |
| 윤성진 (Seongjin Yun) | 박사과정 | 2025.03~ | mayo6426@snu.ac.kr |  |
| 윤도현 (Dohyeon Yun) | 박사과정 | 2026.03 ~ | dokyeng01@snu.ac.kr |  |
| 이동훈 (Lee Donghoon) | 박사과정 | 2026.03 ~ | sandwing@snu.ac.kr |  |
| 김동욱 (Kim Dong Wook) | 박사과정 | 2026.03 ~ | eastshark@snu.ac.kr |  |
| 노창균 (Changgyun Ro) | 학부 인턴 | 2025.03~ | rcg0419@snu.ac.kr |  |
| 정다은 (Daeun Jeong) | 학부 인턴 |  | jeongdaeun0512@snu.ac.kr |  |
| 심규장 (Gyujang Sim) | 박사과정 |  | gyujang95@snu.ac.kr |  |
| 이다영 (Lee dayoung) | Co-advised Student | 2025.03~ | dy_92.lee@snu.ac.kr |  |
| 최재영 (Jaeyoung Choi) | Co-advised Student | 2025.03~ | ch7694@snu.ac.kr |  |

### 별도 소개에 게시된 학부 인턴

Members의 위 명단과 별도로 개인 소개에 학부 인턴으로 게시된 5명이다. 시작은 개인 소개의 Since 표기다.[^additional]

| 이름 | 게시 역할 | 시작 | 학교 이메일 |
|---|---|---|---|
| 백우준 (BAEK WOOJOON) | 학부 인턴 | 2025.03~ | andy0119@snu.ac.kr |
| 김찬중 (Chanjung Kim) | 학부 인턴 | 2025.03~ | chanjungkim@snu.ac.kr |
| 서준영 (Junyeong Seo) | 학부 인턴 |  | jun97000@snu.ac.kr |
| 김유민 (Yumin Kim) | 학부 인턴 |  | cngray@inha.edu |
| 김민수 (Minsoo Kim) | 학부 인턴 |  | skywhale@snu.ac.kr |

## 졸업생과 이전 구성원

Members의 Alumni 구획에 손재희 1명이 게시되어 있다. 학위 취득 연도와 진로가 별도로 적히지 않은 이전 구성원 명단이며, Co-advised Student는 학위명이 아닌 게시 역할이다.[^members][^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 손재희 (Jaehee Sohn) | Co-advised Student |  |

## 최근 논문 목록 (2021–2026)

누리집 논문 상세 33쪽 가운데 2021–2026년으로 게시된 12편이다. 류일 교수의 서울대 부임 전인 The University of Texas at Dallas 재직 시기 항목이 포함되어 있다. 연도·제목·저자·학술지는 누리집의 출간연도와 서지 표기다. 제목에서 확인되는 대상은 금속 기둥과 격자 구조의 소성 변형, 결정 경계와 전위의 상호작용, 나노압입에 따른 변형이다. 나노압입은 탐침으로 재료 표면을 눌러 힘과 변형을 조사하는 시험이다.[^publication-details][^professor]

**2025**

- Phu Cuong Nguyen, Nicole Aragon, Ill Ryu. "Defect dynamics modeling of mesoscale plasticity". *International Journal of Solids and Structures*.
- Phu Cuong Nguyen, Seungjoon Lee, Ill Ryu. "Dislocation plasticity in porous micropillars under uniaxial loading". *Journal of Materials Science & Technology*.
- Guensik Min, Jeongseok Kim, Phu Cuong Nguyen, Sungmin Lee, Yeonju Oh, Hwangsun Kim, Hyoung Chan Kim, Ill Ryu, Heung Nam Han. "Incipient plasticity of potassium-doped tungsten under nanoindentation: A comparison between experiments and defect dynamics simulations". *Journal of Materials Science & Technology*.

**2024**

- Phu Cuong Nguyen, Ill Ryu. "Size dependent scaling law of plastic flow in FCC nanolattices: A dislocation dynamics study". *Acta Materialia*.
- Nicole K. Aragon, Hojun Lim, Phu Cuong Nguyen, Ill Ryu. "Understanding dislocation plasticity of single crystalline Ta micropillars under dynamic loading". *Journal of Materials Research and Technology*.

**2023**

- Jamie D. Gravell, Jaehyun Cho, Seungjoon Lee, Sylvie Aubry, Ill Ryu. "Prediction of dislocation – grain boundary interactions in FCC aluminum bicrystals using a modified continuum criterion and machine learning methods". *Materialia*.
- Nicole K. Aragon, Ye-eun Na, Phu Cuong Nguyen, Dongchan Jang, Ill Ryu. "Micro-beam bending of FCC bicrystals: A comparison between defect dynamics simulations and experiments". *Materialia*.
- Phu Cuong Nguyen, Ill Ryu. "Mesoscale dislocation dynamics modeling of incipient plasticity under nanoindentation". *Materialia*.

**2022**

- Nicole K. Aragon, Jamie D. Gravell, Ill Ryu. "Dislocation interactions at the grain boundary in FCC bicrystals: An atomistically-informed dislocation dynamics study". *Acta Materialia*.

**2021**

- Nicole K. Aragon, Sheng Yin, Hojun Lim, Ill Ryu. "Temperature dependent plasticity in BCC micropillars". *Materialia*.
- Jamie.D. Gravell, Sangryun Lee, Seunghwa Ryu, Ill Ryu. "Effect of size and orientation on stability of dislocation networks upon torsion loading and unloading in FCC metallic micropillars". *Acta Materialia*.
- Gyuho Song, Nicole K. Aragon, Ill Ryu, Seok‐Woo Lee. "Low‐temperature failure mechanism of [001] niobium micropillars under uniaxial tension". *Journal of Materials Research*.

## 학회와 세미나 발표

누리집 학회·세미나 발표 상세 52쪽 중 기간의 시작일이 2021년 10월 22일–2026년 10월 22일에 드는 26건이다. 류일 교수의 서울대 부임 전인 The University of Texas at Dallas 재직 시기 발표가 포함되어 있다. 기간·참가자·대회명은 게시 표기이며, 참가자가 발표자 한 사람 또는 일부 학생으로 적힌 항목도 있다. 두 자리 연도 표기는 누리집의 표기를 유지했다.[^conferences][^professor]

| 누리집 기재 기간 | 제목 | 대회·세미나 | 참가자 |
|---|---|---|---|
| 25/12/04 | Defect-driven plasticity and failure in heterogeneous nanomaterials | 2025_Unist_Seminar | 류일 |
| 25/11/30 ~ 25/12/5 | Dislocation Dynamics Model of Strain Gradient Plasticity under Inhomogeneous Loading Condition | MRS 2025 Fall | Jaehee Sohn, Ill Ryu |
| 25/11/17 ~ 25/11/19 | Finite-Element Analysis of Thermal Stresses Driven by Internal Temperature Fields in Thermal Barrier Coating | ATSC 2025 – 14th Asian Thermal Spray Conference & Expo | 안응규 |
| 25/11/10 ~ 25/11/14 | The role of dislocation-plasticity in nano-architectured metals | 2025_Dislocations - THE 7th DISLOCATIONS CONFERENCE | Ill Ryu |
| 25/11/04 ~ 25/11/07 | Dislocation Plasticity in Thin-Films under Inhomogeneous Loading for Semiconductor Packaging Reliability | The 23rd International Symposium on Microelectronics and Packaging (ISMP 2025) | 연경미 |
| 25/10/29 ~ 25/10/31 | Defect dynamics modeling of mesoscale plasticity | 2025 금속재료학회 추계학술대회 | 연경미, 성준호 |
| 25/10/29 ~ 25/10/31 | 코어-쉘 구조에서의 전위 상호작용에 대한 모델링 | 2025 금속재료학회 추계학술대회 | 이호영 |
| 25/06/20 | Computational material design via defect engineering | 2025_KAIST Mechanics of Materials Workshop | 류일 |
| 25/06/20 | Nanomechanical modeling of defect-driven plasticity and failure in Metallic Nanostructures | 2025_인하대_seminar | 류일 |
| 25/06/02 ~ 25/06/06 | Mesoscale modeling of dislocation interaction with nanoprecipitates | The 20th International Conference on Strength of Materials | 연경미 |
| 25/04/22 | 나노 석출물과 전위 상호작용의 마이크로 범위 모델링 | 금속재료학회 춘계학술대회 | 연경미 |
| 25/04/22 | 결함 동역학 모델을 활용한 파단의 메커니즘에 관한 연구 | 2025 금속재료학회 춘계학술대회 | 성준호 |
| 25/04/15 - 25/04/19 | Nanomechanical Modeling of Fracture and Plasticity in Metallic Multilayers During Thermal Cycles | ICEP 2025 - 2025 International Conference on Elecctronics Packaging and iMAPS All Asia Conference | 류일 |
| 25/03/23 ~ 25/03/27 | Computational material design based on dislocation plasticity | TMS 2025 - 154th Annual Meeting & Exhibtion | Gyu Jang Sim, and Ill Ryu |
| 2024/4/11 | Nanomechanical modeling and its applications to Defect Engineering (Invited) | Department of Material Science and Engineering Seminar, Kookmin University, South Korea | Ill Ryu |
| 2024/3/2 - 2024/3/8 | Defect-based damage model via a mesoscale defect dynamics modeling | The Minerals Metals & Materials Society (TMS) 2024, San Diego, CA, USA | Phu Cuong Nguyen |
| 2023/9/1 - 2023/9/9 | Microscopic damage model via a multi-scale defect dynamics | The international conference on Computational Plasticity (Complas 2023), Barcelona, Spain | Ill Ryu |
| 2023/5/20 - 2023/5/25 | Multi-scale modeling of dislocation plasticity in nano-architectected metals | The 7th World Congress on Integrated Computational Materials Engineering (ICME 2023), Orlando, FL, USA | Cuong P. Nguyen, Ill Ryu |
| 2023/1/5 - 2023/1/9 | Multiscale and Multiphysical Modeling of Defect Driven Plasticity and its Applications (Keynote) | International Conference on Plasticity, Damage and Fracture (ICPDF) 2023, Punta Cana, Dominican Republic | Ill Ryu |
| 2022/11/4 - 2022/11/11 | Defect-driven plasticity in nanostructural metals (Invited) | The 70th InternationalConference on Electronic Materials and Nanotechnology for Green Environment (ENGE2022) Jeju, South Korea | Ill Ryu |
| 2022/10/09 - 2022/10/12 | Multi-scale and multi-physical model of defect-driven plasticity in nanostructural metals | The Materials Science & Technology (MS&T) 2022 , Baltimore, MD, USA | Ill Ryu |
| 2022/10/2 - 2022/10/5 | Investigating the behavior of BCC tantalum single crystals during Taylor impact testing using a coupled dislocation dynamics and finite element model | The 10th International Conference on Multiscale Materials Modeling (MMM10), Baltimore, MD, USA | Nicole K. Aragon, Hojun Lim, Ill Ryu |
| 2022/10/2 - 2022/10/5 | Investigating defect-controlled plastic deformation mechanisms of nano-porous metals using Defect Dynamics Element Method | The 10th International Conference on Multiscale Materials Modeling (MMM10), Baltimore, MD, USA | Cuong P. Nguyen, Ill Ryu |
| 2022/10/2 - 2022/10/5 | Defect dynamics element models for defect-controlled plasticity in nanostructures | The 10th International Conference on Multiscale Materials Modeling (MMM10), Baltimore, MD, USA | Ill Ryu |
| 2022/06/26 - 2022/07/1 | Defects Dynamics Element Models for Nanoindentation: Effect of Indenter Radius, Initial Density and Crystal Orientation on Incipient Plasticity | The 17th International Conference on Strength of Materials (ICSMA17), Metz, France | Ill Ryu |
| 2022/05/08 - 2022/05/13 | Multiscale modeling of size dependent plasticity (Invited) | Material Research Society (MRS) 2022 Spring, Honolulu, HI, USA | Ill Ryu |

## 연락과 위치

- 주소: 08826 서울특별시 관악구 관악로 1 서울대학교[^contact]
- 교수 연구실: 33동 309호[^home]
- 학생 연구실: 37동 207/208/210호[^home]
- 기관 전화: 02-880-7167[^home][^professor]
- 교수 업무 이메일: ryuill@snu.ac.kr[^professor][^contact]
[^home]: N3M 첫 화면, 2026-10-30 관측. <https://n3m.snu.ac.kr/> 연구실 국·영문명, 이론·계산 모형의 개발, 변형·파손의 이해와 설계, 연락과 위치를 게시한다.

[^research]: N3M Research, 2026-10-30 관측. <https://n3m.snu.ac.kr/research/> Small Scale Plasticity, Fracture and Damage, Reliability Analysis, Material Design의 연구 소개.

[^mechanics]: N3M Research의 Dislocation Plasticity와 Micromechanical Damage Model, 2026-10-30 관측. <https://n3m.snu.ac.kr/research/> 전위 동역학 모형으로 소성 변형의 물리적 원인을 이해하고, 결함 미세구조에 바탕을 두어 결정 재료의 파손을 연구한다고 적는다.

[^model]: N3M Research의 Concurrently-coupled Defect Dynamics와 Mesoscale plasticity in Polycrystals, 2026-10-30 관측. <https://n3m.snu.ac.kr/research/> 결함의 세부 움직임과 재료 전체의 힘·변형 관계를 연결하는 다중 규모 모형을 개발하고, 복합 물리 현상과 결정립계의 상호작용을 모형화한다고 적는다.

[^defects]: 서울대학교 재료공학부 류일 소개의 Lab Overview, 2026-10-30 관측. <https://mse.snu.ac.kr/ryu-ill/> 원자 규모에서 결함 미세구조를 조절해 재료 전체의 성질을 설계하는 것을 핵심 전략으로 밝힌다.

[^metals]: N3M Research의 Mechanical Properties of Nanostructures와 Dislocation Interaction with Grain Boundaries, 2026-10-30 관측. <https://n3m.snu.ac.kr/research/> 나노구조 금속의 기계적 성질과 변형 원리를 연구하며, 전위와 결정립계의 상호작용이 재료 전체의 기계적 반응에 미치는 영향을 설명한다.

[^design]: N3M Research의 Data-Driven Property Optimization, 2026-10-30 관측. <https://n3m.snu.ac.kr/research/> 연성과 인성을 함께 고려하는 재료 설계를 위해 미세구조의 구성 공간과 기계학습을 결합하고, 기계학습 알고리즘이 이끄는 다목적 최적화로 결함 미세구조를 설계한다고 적는다.

[^battery]: N3M Research의 High Performance Energy Storage Design, 2026-10-30 관측. <https://n3m.snu.ac.kr/research/> 에너지 저장용 양극·음극 소재를 대상으로 역학을 결합한 다중 물리 접근으로 충방전 중의 변형과 파손을 연구한다고 적는다.

[^reliability]: N3M Research의 Reliability Analysis in Microelectronics, 2026-10-30 관측. <https://n3m.snu.ac.kr/research/> 전자소자의 설계를 위해 결함 미세구조를 고려하는 다중 규모·다중 물리 모형으로 변형과 파손을 조사한다고 적는다.

[^professor]: N3M 교수 소개 류일(Ryu, Ill), 2026-10-30 관측. <https://n3m.snu.ac.kr/member/illryu/> 학력·Career·Research Interests와 기관 전화·이메일.

[^department]: 서울대학교 재료공학부 류일 교수 소개, 2026-10-30 관측. <https://mse.snu.ac.kr/ryu-ill/> Assistant Professor, 2024년 부임, 이전 소속과 학력, 연구 관심, Research Institute of Advanced Materials의 Adjunct Researcher 표기.

[^members]: N3M Members, 2026-10-30 관측. <https://n3m.snu.ac.kr/members/> 교수, Graduate Students 9명, Undergraduate Students 2명, Co-advised Students 3명, Alumni 1명을 구분해 게시한다.

[^member-details]: N3M 개인 구성원 소개, 각각 2026-10-30 관측. [연경미](https://n3m.snu.ac.kr/member/yeon-kyeongmi/) · [안응규](https://n3m.snu.ac.kr/member/%ec%95%88%ec%9d%91%ea%b7%9c/) · [성준호](https://n3m.snu.ac.kr/member/%ec%84%b1%ec%a4%80%ed%98%b8/) · [이호영](https://n3m.snu.ac.kr/member/%ec%9d%b4%ed%98%b8%ec%98%81/) · [신찬재](https://n3m.snu.ac.kr/member/%ec%8b%a0%ec%b0%ac%ec%9e%ac/) · [윤성진](https://n3m.snu.ac.kr/member/%ec%9c%a4%ec%84%b1%ec%a7%84/) · [윤도현](https://n3m.snu.ac.kr/member/%ec%9c%a4%eb%8f%84%ed%98%84/) · [이동훈](https://n3m.snu.ac.kr/member/%ec%9d%b4%eb%8f%99%ed%9b%88/) · [김동욱](https://n3m.snu.ac.kr/member/%ea%b9%80%eb%8f%99%ec%9a%b1/) · [노창균](https://n3m.snu.ac.kr/member/%eb%85%b8%ec%b0%bd%ea%b7%a0/) · [정다은](https://n3m.snu.ac.kr/member/%ec%a0%95%eb%8b%a4%ec%9d%80/) · [심규장](https://n3m.snu.ac.kr/member/gyujang-sim/) · [이다영](https://n3m.snu.ac.kr/member/%ec%9d%b4%eb%8b%a4%ec%98%81/) · [최재영](https://n3m.snu.ac.kr/member/%ec%b5%9c%ec%9e%ac%ec%98%81/). 과정 이력 또는 Since 표기와 학교 이메일의 근거다.

[^additional]: N3M의 별도 학부 인턴 소개, 각각 2026-10-30 관측. [백우준](https://n3m.snu.ac.kr/member/%eb%b0%b1%ec%9a%b0%ec%a4%80/) · [김찬중](https://n3m.snu.ac.kr/member/%ea%b9%80%ec%b0%ac%ec%a4%91/) · [서준영](https://n3m.snu.ac.kr/member/%ec%84%9c%ec%a4%80%ec%98%81/) · [김유민](https://n3m.snu.ac.kr/member/%ea%b9%80%ec%9c%a0%eb%af%bc/) · [김민수](https://n3m.snu.ac.kr/member/%ea%b9%80%eb%af%bc%ec%88%98/).

[^alumni]: N3M 손재희 개인 소개, 2026-10-30 관측. <https://n3m.snu.ac.kr/member/%ec%86%90%ec%9e%ac%ed%9d%ac/> Alumni 구획, 이름과 Co-advised Student 역할을 게시한다.

[^publication-details]: N3M 논문 상세 33쪽의 서지·출간연도, 각각 2026-10-30 관측. 최근 목록에 실은 12편의 원문: [Size dependent scaling law of plastic flow in FCC nanolattices: A dislocation dynamics study](https://n3m.snu.ac.kr/publication/size-dependent-scaling-law-of-plastic-flow-in-fcc-nanolattices-a-dislocation-dynamics-study/) · [Understanding dislocation plasticity of single crystalline Ta micropillars under dynamic loading](https://n3m.snu.ac.kr/publication/understanding-dislocation-plasticity-of-single-crystalline-ta-micropillars-under-dynamic-loading/) · [Prediction of dislocation - grain boundary interactions in FCC aluminum bicrystals using a modified continuum criterion and machine learning methods](https://n3m.snu.ac.kr/publication/prediction-of-dislocation-grain-boundary-interactions-in-fcc-aluminum-bicrystals-using-a-modified-continuum-criterion-and-machine-learning-methods/) · [Micro-beam bending of FCC bicrystals: A comparison between defect dynamics simulations and experiments](https://n3m.snu.ac.kr/publication/micro-beam-bending-of-fcc-bicrystals-a-comparison-between-defect-dynamics-simulations-and-experiments/) · [Mesoscale dislocation dynamics modeling of incipient plasticity under nanoindentation](https://n3m.snu.ac.kr/publication/mesoscale-dislocation-dynamics-modeling-of-incipient-plasticity-under-nanoindentation/) · [Dislocation interactions at the grain boundary in FCC bicrystals: An atomistically-informed dislocation dynamics study](https://n3m.snu.ac.kr/publication/dislocation-interactions-at-the-grain-boundary-in-fcc-bicrystals-an-atomistically-informed-dislocation-dynamics-study/) · [Temperature dependent plasticity in BCC micropillars](https://n3m.snu.ac.kr/publication/temperature-dependent-plasticity-in-bcc-micropillars/) · [Effect of size and orientation on stability of dislocation networks upon torsion loading and unloading in FCC metallic micropillars](https://n3m.snu.ac.kr/publication/effect-of-size-and-orientation-on-stability-of-dislocation-networks-upon-torsion-loading-and-unloading-in-fcc-metallic-micropillars/) · [Low‐temperature failure mechanism of [001] niobium micropillars under uniaxial tension](https://n3m.snu.ac.kr/publication/low%e2%80%90temperature-failure-mechanism-of-001-niobium-micropillars-under-uniaxial-tension/) · [Defect dynamics modeling of mesoscale plasticity](https://n3m.snu.ac.kr/publication/defect-dynamics-modeling-of-mesoscale-plasticity/) · [Dislocation plasticity in porous micropillars under uniaxial loading](https://n3m.snu.ac.kr/publication/dislocation-plasticity-in-porous-micropillars-under-uniaxial-loading/) · [Incipient plasticity of potassium-doped tungsten under nanoindentation: A comparison between experiments and defect dynamics simulations](https://n3m.snu.ac.kr/publication/incipient-plasticity-of-potassium-doped-tungsten-under-nanoindentation-a-comparison-between-experiments-and-defect-dynamics-simulations/).

[^conferences]: N3M Conferences와 발표 상세 52쪽, 각각 2026-10-30 관측. <https://n3m.snu.ac.kr/conferences/> 발표 상세의 기간·참가자·대회명을 기준으로 했다. 기간 안 26건의 원문은 근거 페이지의 읽은 자료 표에 개별 주소로 적었다.

[^contact]: N3M 찾아오시는길, 2026-10-30 관측. <https://n3m.snu.ac.kr/%ec%b0%be%ec%95%84%ec%98%a4%ec%8b%9c%eb%8a%94%ea%b8%b8/> 기관 주소·전화와 교수 업무 이메일.

[^p1]: P. C. Nguyen, S. Lee, I. Ryu, Journal of Materials Science & Technology 258, 12-21 (온라인 2025-09-26). <https://doi.org/10.1016/j.jmst.2025.08.058> 초록 기준(출판사 논문 페이지). 초록 원문 <https://www.jmst.org/EN/10.1016/j.jmst.2025.08.058> 권호 연도 2026. 저자 소속·교신 표기: 출판사 논문 페이지.

[^p2]: G. Min 외, H. N. Han, Journal of Materials Science & Technology 223, 264-274 (온라인 2024-11-26). <https://doi.org/10.1016/j.jmst.2024.10.036> 초록 기준(출판사 논문 페이지). 초록 원문 <https://www.jmst.org/EN/10.1016/j.jmst.2024.10.036> 권호 연도 2025. 저자 소속·교신 표기: 출판사 논문 페이지.

[^p3]: P. C. Nguyen, I. Ryu, Acta Materialia 274, 120022 (2024). <https://doi.org/10.1016/j.actamat.2024.120022> 초록 기준(누리집 논문 페이지 게시 초록). 초록 원문 <https://n3m.snu.ac.kr/publication/size-dependent-scaling-law-of-plastic-flow-in-fcc-nanolattices-a-dislocation-dynamics-study/> 서지·저자 소속·교신 등록: OpenAlex 등록 서지 <https://api.openalex.org/works?per-page=10&filter=doi:10.1016/j.ijsolstr.2024.113132%7C10.1016/j.jmst.2025.08.058%7C10.1016/j.jmst.2024.10.036%7C10.1016/j.actamat.2024.120022%7C10.1016/j.jmrt.2024.05.009>.

[^p4]: N. K. Aragon, H. Lim, P. C. Nguyen, I. Ryu, Journal of Materials Research and Technology 30, 6265-6277 (2024). <https://doi.org/10.1016/j.jmrt.2024.05.009> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index,authorships&filter=doi:10.1016/j.actamat.2024.120022%7C10.1016/j.jmrt.2024.05.009%7C10.1016/j.jmst.2024.10.036%7C10.1016/j.jmst.2025.08.058%7C10.2139/ssrn.4620597> 서지·저자 소속·교신 등록: OpenAlex 등록 서지 <https://api.openalex.org/works?per-page=10&filter=doi:10.1016/j.ijsolstr.2024.113132%7C10.1016/j.jmst.2025.08.058%7C10.1016/j.jmst.2024.10.036%7C10.1016/j.actamat.2024.120022%7C10.1016/j.jmrt.2024.05.009>.

# 분리막·소재·머신 인텔리전스 연구실 (Membranes, Materials, Machine Intelligence Laboratory, MMML)

**KAIST 생명화학공학과 · 고동연 교수**

- 분야: 분리막(멤브레인)과 흡착제를 이용한 분자 분리, 원유·유기 용매 분리, 수소 정제, 공기 중 이산화탄소 직접 포집(DAC)과 해양 탄소 제거, 베이지안 최적화와 자율 실험실
- 홈페이지: <https://mmml.kaist.ac.kr/>
- 근거와 출처: [MMML 근거 페이지](mmml-sources.md)

> 원유를 증류 앞 단계에서 얇은 막으로 걸러 성분별로 미리 나누는 기술, 공기에서는 흡착 장치로, 바닷물에서는 전기화학 장치로 이산화탄소를 뽑아내는 기술처럼 에너지를 덜 쓰는 분리 기술을 만드는 연구실이다. 실험실에서 만든 새 소재를 실제 공정 규모의 장치로 키우고, 인공지능으로 실험과 공정 설계를 빠르게 한다.[^home][^about][^p1]

## 무엇을 연구하나

연구실은 실험실에서 개발한 첨단 소재를 실제 현장의 분리 공정으로 연결하는 플랫폼 기술을 만드는 것을 목표로 하며, 소재 발굴부터 모듈·시스템 구현과 공정 적용까지의 전 과정을 자율 실험실(로봇과 인공지능이 실험을 스스로 계획하고 수행하는 실험실)과 머신 인텔리전스로 앞당긴다고 소개한다.[^about] 물질을 분자 수준에서 분리하는 기술은 깨끗한 물과 공기, 정유, 석유화학, 바이오 정제, 의약품, 기후 기술에 두루 쓰여, 지금보다 에너지와 탄소를 덜 쓰는 분리 기술이 나오면 막대한 에너지를 아낄 수 있다는 것이 연구실의 문제의식이다.[^about]

첫 번째 갈래는 **분리막**이다. 원유, 합성연료(e-fuel), 바이오디젤 같은 복잡한 액체 혼합물과 수소·경질 탄화수소 기체를 분리하는 막을 만들고, 이를 키운 모듈과 공정까지 설계한다.[^about] 값싼 다공성 고분자막으로 원유를 가벼운 성분과 무거운 성분으로 나눠 기존 상압 증류보다 에너지를 크게 줄일 수 있음을 보였고,[^p1] 플라스마나 전자빔으로 탄소 분자체 막(열분해한 탄소로 만든 아주 작은 구멍의 막)의 구멍 크기를 조절해 수소를 고르게 걸러 냈다.[^p2][^p4] 수십 나노미터 두께의 막으로 크기가 비슷한 의약품 분자를 갈라내기도 했다.[^p3]

두 번째 갈래는 **흡착 소재와 탄소 제거 시스템**이다. 공기 중 이산화탄소를 직접 포집(DAC)하는 섬유형 흡착제와 전기로 데워 재생하는 시스템, 바닷물 속 탄소를 전기화학적으로 제거하는 시스템(e-DOC), 초고순도 수소 생산, 이산화탄소를 활용하는 막 반응기를 연구한다.[^about] 흡착 섬유를 구리선과 함께 짜 넣은 포집 장치는 기존 적층형보다 기체가 잘 통하고 압력 손실이 작았고,[^p5] MIT 연구진과 함께 바닷물 속 탄소를 광물로 바꾸는 소형 중공사(속이 빈 섬유) 전극 장치를 만들었다.[^p6]

세 번째 갈래는 **머신 인텔리전스**다. 베이지안 최적화(적은 실험으로 최적 조건을 찾아가는 통계 방법)와 자율 실험실 기술(EARL-BO, BOOST)로 실험과 공정 개발을 앞당긴다.[^about][^preprints] 공기 중 이산화탄소 포집 공정의 운전 조건,[^p7] 폐수에서 이소프로필 알코올을 회수하는 막 증류 공정을 베이지안 최적화로 찾았다.[^p8]

## 주요 연구 주제

### 1. 원유·용매·기체 분리막

원유 분획 막, 탄소 분자체 수소 분리막, 유기 용매 나노여과막(나노미터 크기 구멍으로 분자를 거르는 막).[^p1][^p2][^p3][^p4] 대표 논문 1–4.

### 2. 공기·해양 탄소 제거 시스템

직조형 섬유 흡착 장치, 전기화학 해양 탄소 제거.[^p5][^p6] 대표 논문 5, 6.

### 3. 베이지안 최적화와 자율 실험

포집 공정 최적화, 막 증류 최적화.[^p7][^p8][^preprints] 대표 논문 7, 8.

## 대표 논문

고동연 교수가 저자로 참여한 2021–2026년 학술지 논문과 연구실 소식에 소개된 논문 가운데 교수가 마지막 저자인 것에서 주제별로 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^crossref] |
|---|---|---|---|---|
| 1 | 2026 | [Crude oil fractionation by means of mesoporous polyacrylonitrile membranes](https://doi.org/10.1038/s41586-026-10677-3) · Nature | 보통 지지층으로 쓰는 다공성 폴리아크릴로니트릴 막이 원유를 성분별로 나눌 수 있음을 보였다. 무거운 탄화수소가 약 15 nm 구멍에 쌓이며 구멍을 2 nm 이하로 좁혀 가벼운 성분(나프타·등유)을 골라 통과시켰고, 4주 동안 안정적이었다. 공정 계산상 상압 증류보다 에너지를 31.6%, 이산화탄소를 37.6% 줄일 수 있다.[^p1] | 1저자 Jihoon Choi, 마지막 저자 고동연 |
| 2 | 2026 | [Plasma engineered carbon molecular sieve membranes for precise and stable hydrogen permeation](https://doi.org/10.1126/sciadv.aee7783) · Science Advances | 탄소 분자체 막에 질소·아르곤 플라스마를 쬐어 미세 구멍 구조를 바꾸자, 이산화탄소·메탄보다 수소를 훨씬 잘 골라 통과시켰고 1년 넘는 노화에도 구조가 안정했다.[^p2] | 1저자 Banseok Oh, 마지막 저자 고동연 |
| 3 | 2024 | [Ultrathin organosiloxane membrane for precision organic solvent nanofiltration](https://doi.org/10.1038/s41467-024-47115-9) · Nature Communications | 기체를 이용한 코팅(개시제 화학 기상 증착)으로 29 nm 두께의 유기실록산 고분자 막을 만들어, 분자량 150–300 범위의 용질을 크기별로 정밀하게 갈랐다. 분자량 차이가 100도 안 되는 헤르페스 치료제 성분 두 가지도 분리했다.[^p3] | 1저자 Jihoon Choi, 마지막 저자 고동연 |
| 4 | 2022 | [Electron-mediated control of nanoporosity for targeted molecular separation in carbon membranes](https://doi.org/10.1038/s41467-022-32703-4) · Nature Communications | 전자빔을 쬐는 양으로 탄소 분자체 막의 구멍 크기를 0.05 nm 이하 차이까지 조절했다. 적게 쬐면 에틸렌·에탄을, 많이 쬐면 수소·이산화탄소를 잘 분리했고 노화에 따른 성능 저하도 줄었다.[^p4] | 1저자 Banseok Oh, 마지막 저자 고동연 |
| 5 | 2026 | [Joule-Heated Woven Fiber Contactors for Direct Air Capture](https://doi.org/10.1021/acs.energyfuels.6c03763) · Energy & Fuels | 제올라이트(구멍이 규칙적인 광물성 흡착 소재) 흡착 섬유를 구리선과 함께 엮은 공기 중 이산화탄소 포집 장치. 섬유를 쌓은 방식보다 기체와 흡착제의 접촉이 효율적이었고, 압력 손실은 7–18배 작았다.[^p5] | 1저자 Banseok Oh, 마지막 저자 고동연 |
| 6 | 2026 | [A Compact Hollow Fiber Electrode Assembly Architecture for Continuous Electrochemical Marine Carbon Dioxide Removal](https://doi.org/10.1002/aenm.71205) · Advanced Energy Materials | 바닷물 속 탄소를 전기화학적으로 없애는 장치를, 다공성 스테인리스 중공사 안에 분리막과 반대 전극을 넣은 동축 구조로 만들었다. 전극 사이를 약 1 mm로 좁혀 저항 손실을 줄이고 탄소를 광물로 계속 바꿀 수 있게 했다.[^p6] | 1저자 Inhwan Park, 마지막 저자 고동연(T. Alan Hatton 공저) |
| 7 | 2025 | [Accelerating process design for direct air capture: Bayesian optimization of temperature-vacuum swing adsorption with fiber sorbents](https://doi.org/10.1016/j.ccst.2025.100526) · Carbon Capture Science & Technology | 금속유기골격체(금속과 유기 분자로 짠 구멍 많은 결정 소재) 섬유 흡착제를 쓴 공기 중 이산화탄소 포집 공정(온도·진공 순환 흡착)에서, 포집량·운영비·탄소 배출이라는 엇갈리는 목표를 베이지안 최적화로 맞추는 운전 조건을 실험으로 찾았다.[^p7] | 1저자 Jinhong Jeong, 마지막 저자 고동연 |
| 8 | 2024 | [Sustainable Isopropyl Alcohol Recovery via Data-Driven, Active-Learning Optimization of Vacuum Membrane Distillation](https://doi.org/10.1021/acssuschemeng.4c01285) · ACS Sustainable Chemistry & Engineering | 폐수에서 이소프로필 알코올을 되찾는 진공 막 증류 공정을, 데이터가 적을 때도 쓸 수 있는 능동 학습 기반 베이지안 최적화로 최적화해 필요한 실험 수를 줄였다.[^p8] | 1저자 Jimin Park, 마지막 저자 고동연 |

## 교수와 전문 분야

고동연 교수는 고려대 학사(2007)와 KAIST 박사(2013)를 받고, KAIST 응용과학연구소(2013–2014)와 미국 조지아공대 화학생물공학과(2014–2017) 박사후연구원을 거쳤다. 2021년부터 KAIST 생명화학공학과 부교수이며 사우디 아람코–KAIST 이산화탄소 관리 센터 부센터장(2023–)을 맡고 있다. 기업 Sorv의 공동 창업자·과학 자문(2023–2025)이었고, 2026년부터 M3I Labs의 공동 창업자·수석 과학자다. Journal of Environmental Chemical Engineering 편집자(2021–2024), Chemical Engineering Journal 편집위원(2024–)을 지냈다.[^team]

논문으로 보면 전문 분야는 세 갈래다.

- **분자 분리막 소재와 공정**: 원유, 용매, 수소.[^p1][^p2][^p3][^p4]
- **탄소 포집·제거 장치**: 섬유 흡착제, 해양 탄소 제거.[^p5][^p6]
- **데이터 기반 공정 최적화**: 베이지안 최적화.[^p7][^p8]

## 응용 분야

대표 논문과 연구 소개로 보면 정유·석유화학 공정의 에너지 절감, 수소 생산·정제, 공기·해양 탄소 제거, 반도체 폐수 처리와 용매 재활용, 의약품 정제에 닿아 있다.[^p1][^p2][^p6][^p8][^about][^team] 연구실은 공기 중 이산화탄소 포집용 전기 가열 섬유 흡착제, 이산화탄소 포집용 금속유기골격체 섬유, 유기 용매 정삼투(농도 차이로 용매를 막 너머로 끌어내는 분리 방식) 시스템 등의 특허를 국내외에 출원·등록했다.[^patents]

## 구성원

2026년 10월 19일 랩 팀 페이지 기준이다. "시작"은 랩이 적은 합류 학기다.[^team] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| Jeong-Un Jang (장정운) | 박사후연구원 | Spring 2020 |  |
| Min-Jun Jang (장민준) | 박사과정 | Spring 2021 | 1 |
| Huiryung Heo (허희령) | 박사과정 | Spring 2022 |  |
| Min Hyung Lee (이민형) | 박사과정 | Spring 2023 |  |
| Jeongsu Wi (위정수) | 박사과정 | Spring 2023 | 2 |
| Si Eun Kim (김시은) | 박사과정 | Spring 2024 |  |
| Hyojin Cho (조효진) | 석사과정 | Spring 2025 |  |
| Gunwoo Roh (노건우) | 석사과정 | Spring 2026 |  |
| Injun Park (박인준) | 박사과정 | Fall 2023 | 5 |
| Juyeon Kang (강주연) | 석사과정 | Spring 2025 |  |
| Inhwan Park (박인환) | 박사과정 | Fall 2023 | 6 |
| Junseong Kim (김준성) | 석사과정 | Spring 2025 |  |
| Jaemin Choi (최재민) | 석사과정 | Spring 2025 | 1 |
| Karoline L. Hebisch (카롤리네 헤비쉬) | 박사후연구원 | Spring 2025 |  |
| Mujin Cheon (천무진) | 박사후연구원 | Spring 2023 | 7, 8 |
| Oh-Hyuk Kwon (권오혁) | 석사과정 | Spring 2026 |  |

## 졸업생 진로와 학위 논문

랩 팀 페이지의 졸업생과 학위 논문 제목이다. 진로는 적혀 있지 않다.[^team]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Sunggyu Lee (이성규) | Ph.D. (Spring) (2026) |  | Engineering Copper-Based Sorbent Systems for the Selective Adsorption of Unsaturated Carbon Species |
| Jeong-Un Jang (장정운) | Ph.D. (Spring) (2026) |  | Catalytic Performance Enhancement via Water Management: Membrane Reactors |
| Young-Eun Hwang (황영은) | Ph.D. (Spring) (2026) |  | A study on the Selective Separation and Modeling of CO2 in a Membrane-based Continuous Solid Carbonation process |
| Mujin Cheon (천무진) | Ph.D. (Fall) (2025) |  | Bayesian Optimization Methods: From Process Engineering Applications to Non-myopic and Scalable Reinforcement Learning Approaches |
| Jimin Park (박지민) | Ph.D. (Fall) (2025) |  | Design of Membrane-based Separation Processes for Wastewater Treatment in the Semiconductor Industry |
| Jihoon Choi (최지훈) | Ph.D. (Spring) (2025) |  | Separation and Fractionation of Organic Solvent-Based Mixtures with Polymer Nanofiltration Membranes |
| Banseok Oh (오반석) | Ph.D. (Spring) (2025) |  | Designing tunable carbon molecular sieve membranes for versatile separation applications |
| YongSung Kwon (권용성) | Ph.D. (Spring) (2025) |  | Structural Modification of Pervaporation Membranes for Organic Solvent Separation |
| Kyunam Kim (김규남) | Ph.D. (Spring) (2025) |  | Design and Development of Fiber Sorbent based Direct Air Capture Systems |
| Jinhong Jeong (정진홍) | Ph.D. (Spring) (2025) |  | Optimization of Temperature-Vacuum Swing Adsorption Cycles for Direct Air Capture |
| Taehoon Hyun (현태훈) | Ph.D. (Spring) (2024) |  | Design of Functional Porous Materials for Adsorption-based Separation of Light Hydrocarbons |
| Hyeokjun Seo (서혁준) | Ph.D. (Spring) (2024) |  | Designing Membrane Systems for the Direct Separation of Multicomponent Organic Solvent Mixtures |
| Ari Chae (채아리) | Ph.D. (Spring) (2023) |  | Investigation of Oxidation Mechanism of MXene for Improving Oxidation Stability |
| Young Hun Lee (이영훈) | Ph.D. (Spring) (2023) |  | Structure Design of Fiber Sorbents for Maximizing Direct Air Capture Efficiency |
| Joon-Hyun Park (박준현) | M.S. (2026) |  |  |
| Song-Ik Lim (임송익) | M.S. (2023) |  |  |
| Hwajin Choi (최화진) | M.S. (2022) |  |  |
| Dalsu Choi (최달수) | Postdoc (2019) |  |  |

## 최근 논문 목록 (2021–2026)

고동연 교수(Dong-Yeun Koh)가 저자로 참여한 2021년 이후 학술지 논문과 연구실 소식에 소개된 논문 43편이다.[^crossref][^home]

**2026**

- Banseok Oh, Injun Park, Dong-Yeun Koh. "Joule-Heated Woven Fiber Contactors for Direct Air Capture". *Energy & Fuels*.
- Banseok Oh, Hyeokjun Seo, Jeongsu Wi, Dong-Yeun Koh. "Plasma engineered carbon molecular sieve membranes for precise and stable hydrogen permeation". *Science Advances*.
- Huiryung Heo, Jeong-Un Jang, Jungseob So, Dong-Yeun Koh. "Interface Engineering of Cu/CeO 2 –Al 2 O 3 for Mixed-Oxide Interface-Driven Associative CO2 Activation in RWGS". *ACS Catalysis*.
- Jimin Park, Joon-Hyun Park, Young-Eun Hwang, Dong-Yeun Koh. "Overcoming water co-transport in PIM-1/PVDF composite membranes for sustainable ammonia recovery from wastewater". *Separation and Purification Technology*.
- Injun Park, Sieun Kim, Karoline L. Hebisch, Inhwan Park, Minhyung Lee, Dong-Yeun Koh. "Scale-bridging solid adsorbents for direct air capture: integrating material chemistry, structured contactors, and advanced regeneration processes". *Journal of Materials Chemistry A*.
- Sunggyu Lee, Jungseob So, Hyunjung Kim, Huiryung Heo, Jae W. Lee, Dong-Yeun Koh. "A Scalable and Cost-Effective Zeolite-Polymer Fiber Sorbent Enabled by Vapor-Induced Cu(I) Activation for Selective Acetylene Capture". *ACS Applied Materials & Interfaces*.
- Banseok Oh, YongSung Kwon, Young-Eun Hwang, You-In Park, Seung-Eun Nam, Dong-Yeun Koh. "Dehydration of Ethylene Glycol Using Sodium-Mediated Hydrophilic Carbon Molecular Sieve Membranes". *Industrial & Engineering Chemistry Research*.
- Injun Park, Sunwoo Kim, Byeongju Jeon, Huiryung Heo, Siyoung Q. Choi, Jay H. Lee, Dong-Yeun Koh. "Additive manufacturing of architected Ca(OH)2 monoliths for accelerated CO2 mineralization". *Carbon Capture Science & Technology*.
- Daeuk Kang, Huiryung Heo, Euna Jeong, Hee-Man Yang, Dong-Yeun Koh, Chan Woo Park, Hyung-Ju Kim. "Hydrophobic block-structured PDMS/Pt mesoporous silica catalysts for sustainable water–hydrogen isotope exchange". *Materials Advances*.
- Injun Park, Kyunam Kim, Mujin Cheon, Jinhong Jeong, Karoline L. Hebisch, Matthew J. Realff, Ryan P. Lively, Dong-Yeun Koh. "Sub-hour Rapid Cycling of Direct Air Capture Enabled by Engineered Hollow Fiber Sorbents". *ACS Sustainable Chemistry & Engineering*.
- Yugyeong Sung, Ingyu Park, Miseong Kim, Yunseok Lee, Yeonwook Kim, Seungin Lee, Dong-Yeun Koh, Ah-Hyung Alissa Park, Youngjune Park. "Impregnation of liquid-like nanoparticle organic hybrid materials in mesoporous fiber sorbent with hierarchical structures for scalable direct air capture". *Chemical Engineering Journal*.
- Jihoon Choi, Hyeokjun Seo, Minyong Lee, Woong-Chul Shin, Jaemin Choi, Keonwoo Choi, Min-Jun Jang, Sung Gap Im, Jae W. Lee, Ryan P. Lively, Dong-Yeun Koh. "Crude oil fractionation by means of mesoporous polyacrylonitrile membranes". *Nature*.
- Inhwan Park, Young Hun Lee, Jung Hun Lee, Seung‐Jeong Oh, T. Alan Hatton, Dong‐Yeun Koh. "A Compact Hollow Fiber Electrode Assembly Architecture for Continuous Electrochemical Marine Carbon Dioxide Removal". *Advanced Energy Materials*.

**2025**

- Sunggyu Lee, Dong-Yeun Koh. "Solution-Processable Redox-Active Polyimides: Synthesis and CO<sub>2</sub> Responsive Properties". *Membrane Journal*.
- YongSung Kwon, Daehun Kim, Injun Park, YouIn Park, SeungEun Nam, Dong-Yeun Koh. "Facile membrane upscaling via in-situ synthesis of PVA hydrogel for harsh solvent separation: From transport study to industrial application". *Chemical Engineering Journal*.
- Sunggyu Lee, Huiryung Heo, Hyunjung Kim, Jungseob So, Jae W. Lee, Dong-Yeun Koh. "CuI-Embedded fiber sorbent with CO selective adsorption for High-Purity H2 recovery". *Chemical Engineering Journal*.
- Howoun Jung, Kyunam Kim, Jinhong Jeong, Aqil Jamal, Dong-Yeun Koh, Jay H. Lee. "Exploring the impact of hourly variability of air condition on the efficiency of direct air capture". *Chemical Engineering Journal*.
- Jinhong Jeong, Mujin Cheon, Banseok Oh, Aqil Jamal, Jay H. Lee, Dong-Yeun Koh. "Accelerating process design for direct air capture: Bayesian optimization of temperature-vacuum swing adsorption with fiber sorbents". *Carbon Capture Science & Technology*.
- Min-Jun Jang, Yu Chen, Jihoon Choi, Hyeokjun Seo, Yongchul G. Chung, Dong-Yeun Koh. "Enhancing interchain interactions in spirobifluorene-based microporous polyimides for high-performance organic solvent nanofiltration". *Journal of Membrane Science*.
- Jihoon Choi, Woong-Chul Shin, Hyeokjun Seo, Huiryung Heo, Min-Jun Jang, Dong-Yeun Koh. "Tailoring MnO2 nanodomains in organic-inorganic hybrid interfaces toward tunable hydrocarbon separation". *Journal of Membrane Science*.
- Baekmin Q. Kim, Jaehong Lee, Hanul Kim, Subeen Kim, Kyoungmun Lee, Dong-Yeun Koh, Siyoung Q. Choi. "Dual path biphasic column for highly selective and ultrafast organic solvent membrane extraction". *Nature Communications*.
- Jeong-Un Jang, Jungseob So, Huiryung Heo, Chun-Jae Yoo, Young Woo You, Young Jin Kim, Dong-Yeun Koh. "Atomically dispersed silver on nanosheet-stacked amorphous alumina for enhanced NOx reduction". *Chemical Engineering Journal*.
- Jihoon Choi, Daehun Kim, Keonwoo Choi, Hyeokjun Seo, Min-Jun Jang, Hyoseok So, Sung Gap Im, Youngmin Yoo, Dong-Yeun Koh. "A strategic design of iCVD copolymers for high-performance organic solvent nanofiltration membranes with tunable permeance and selectivity". *Chemical Engineering Journal*.

**2024**

- Hyeokjun Seo, Dong-Yeun Koh. "Controlled organic solvent transport in ultramicroporous carbon membranes". *Journal of Membrane Science*.
- Min-Jun Jang, Hyeokjun Seo, Dong-Yeun Koh. "Separation of Liquid Xylene Isomers Using Thin-Film Composite Carbon Molecular Sieve Hollow Fiber Membranes". *Industrial & Engineering Chemistry Research*.
- Jimin Park, Mujin Cheon, Sanghyeon Park, Jay H. Lee, Dong-Yeun Koh. "Sustainable Isopropyl Alcohol Recovery via Data-Driven, Active-Learning Optimization of Vacuum Membrane Distillation". *ACS Sustainable Chemistry & Engineering*.
- Jihoon Choi, Keonwoo Choi, YongSung Kwon, Daehun Kim, Youngmin Yoo, Sung Gap Im, Dong-Yeun Koh. "Ultrathin organosiloxane membrane for precision organic solvent nanofiltration". *Nature Communications*.
- Jisung Lee, Wooseok Lee, Seungho Back, Seung Yeop Yi, Seonggyu Lee, Seongseop Kim, Joonhee Moon, Dong-Yeun Koh, Kyeounghak Kim, Seoin Back, Jinwoo Lee. "Activating iodine redox by enabling single-atom coordination to dormant nitrogen sites to realize durable zinc–iodine batteries". *EES Catalysis*.

**2023**

- Jimin Park, Young-Eun Hwang, Dong-Yeun Koh. "Interfacial synthesis: a scalable fabrication method of two-dimensional membranes". *Current Opinion in Chemical Engineering*.
- Banseok Oh, Kyunam Kim, YongSung Kwon, You-In Park, Hosik Park, Dong-Yeun Koh. "Pervaporation dehydration of ethylene glycol/water mixture via hydrophilic polymer of intrinsic microporosity (PIM) derivatives". *Journal of Membrane Science*.
- Chaehoon Kim, Dong-Yeun Koh, Yongjin Lee, Jihoon Choi, Hae Sung Cho, Minkee Choi. "Bottom-up synthesis of two-dimensional carbon with vertically aligned ordered micropores for ultrafast nanofiltration". *Science Advances*.

**2022**

- Hyeokjun Seo, Dong-Yeun Koh. "Refining petroleum with membranes". *Science*.
- Hwa-Jin Choi, Dong-Yeun Koh. "Homochiral Metal-Organic Framework Based Mixed Matrix Membrane for Chiral Resolution". *Membranes*.
- Suk Lee, Yun-Ho Ahn, Dong-Yeun Koh. "Sustainable building materials employing solid diamines as CO2 sorbents". *Korean Journal of Chemical Engineering*.
- Banseok Oh, Hyeokjun Seo, Jihoon Choi, Sunggyu Lee, Dong-Yeun Koh. "Electron-mediated control of nanoporosity for targeted molecular separation in carbon membranes". *Nature Communications*.
- Kyunam Kim, Young-Eun Hwang, Young Hun Lee, Seong-Jun Park, Daeok Kim, Dong-Yeun Koh. "All-Nanoporous fiber sorbent with a Non-Sacrificial polymer of intrinsic microporosity (PIM) matrix". *Separation and Purification Technology*.
- Sunggyu Lee, Ilia Kevlishvili, Heather J. Kulik, Hee-Tak Kim, Yongchul G. Chung, Dong-Yeun Koh. "Highly efficient bromine capture and storage using N-containing porous organic cages". *Journal of Materials Chemistry A*.
- Ari Chae, Sehyun Doo, Daesin Kim, Tae Yun Ko, Taegon Oh, Seon Joon Kim, Dong-Yeun Koh, Chong Min Koo. "Tunable Ti 3 C 2 T x MXene-Derived TiO 2 Nanocrystals at Controlled pH and Temperature". *Langmuir*.

**2021**

- Hwa-Jin Choi, Yun-Ho Ahn, Dong-Yeun Koh. "Enantioselective Mixed Matrix Membranes for Chiral Resolution". *Membranes*.
- Bong Lim Suh, Taehoon Hyun, Dong-Yeun Koh, Jihan Kim. "Rational Tuning of Ultramicropore Dimensions in MOF-74 for Size-Selective Separation of Light Hydrocarbons". *Chemistry of Materials*.
- Ari Chae, Gwanwon Lee, Dong-Yeun Koh, Cheol-Min Yang, Sungho Lee, Young-Kwan Kim. "Polyacrylonitrile-based carbon nanofibers as a matrix for laser desorption/ionization time-of-flight mass spectrometric analysis of small molecules under both positive and negative ionization modes". *Analytical and Bioanalytical Chemistry*.
- Young Hun Lee, YongSung Kwon, Chaehoon Kim, Young-Eun Hwang, Minkee Choi, YouIn Park, Aqil Jamal, Dong-Yeun Koh. "Controlled Synthesis of Metal–Organic Frameworks in Scalable Open-Porous Contactor for Maximizing Carbon Capture Efficiency". *JACS Au*.
- Sehyun Doo, Ari Chae, Daesin Kim, Taegon Oh, Tae Yun Ko, Seon Joon Kim, Dong-Yeun Koh, Chong Min Koo. "Mechanism and Kinetics of Oxidation Reaction of Aqueous Ti3C2Tx Suspensions at Different pHs and Temperatures". *ACS Applied Materials & Interfaces*.

## 특허

랩 특허 페이지의 등록 특허 11건과 출원 3건이다.[^patents]

- Manufacturing Method of Electrified Fiber Sorbent for Electric and Electromagnetic Swing Adsorption Process (발명자 D.-Y. Koh, Y. Lee, A. Jamal, K. Kim, J. Jeong; 번호 KR 10-2022-0131234; 상태 등록)
- Manufacturing Method of Electrified Fiber Sorbent for Electric and Electromagnetic Swing Adsorption Process (발명자 D.-Y. Koh, Y. Lee, A. Jamal, K. Kim, J. Jeong; 번호 WO 2023068651, AU 2022368476, CN 202280070939.8, EP 22883874.4, JP 2024-524376, SA 1120242080, US 18/703,341; 상태 등록)
- Organic Solvent Forward Osmosis System (발명자 D.-Y. Koh, H. Seo; 번호 KR 10-2537132-0000; 상태 등록)
- Structured MOF fiber sorbent for capturing carbon dioxide and method of manufacturing the same (발명자 D.-Y. Koh, Y. Lee, A. Jamal; 번호 KR 10-2275948-0000; 상태 등록)
- Structured MOF fiber sorbent for capturing carbon dioxide and method of manufacturing the same (발명자 D.-Y. Koh, Y. Lee, A. Jamal; 번호 WO 2020256450, CN 114375224, EP 03988205, US 20220401915; 상태 등록)
- Mineral Carbonation Systems and Mineral Carbonation Methods Using the Same (발명자 D.-Y. Koh, Y. E. Hwang, K. Kim; 번호 KR 10-2171098-0000; 상태 등록)
- Reverse Osmosis Membranes and Separations (발명자 B. A. McCool, H. Deckman, R. P. Lively, D.-Y. Koh, R. Partridge; 번호 US10486107B2; 상태 등록)
- Reverse Osmosis Membranes and Separations (발명자 B. A. McCool, H. Deckman, R. P. Lively, D.-Y. Koh, R. Partridge; 번호 EP 16798361.8, CN 201680066357.7, AU 2016352994, CA 3005215; 상태 등록)
- Hydrocarbon Reverse Osmosis Membranes and Separations (발명자 B. A. McCool, H. Deckman, R. P. Lively, D.-Y. Koh, R. Partridge; 번호 US 10456747B2; 상태 등록)
- Hydrocarbon Reverse Osmosis Membranes and Separations (발명자 B. A. McCool, H. Deckman, R. P. Lively, D.-Y. Koh, R. Partridge; 번호 EP 16798360.0, AU 2016352989, CA 3005205, RU 2018121221; 상태 등록)
- Hollow Fiber Membranes for Solubilizing a Gas into a Liquid, Devices for same, and Processes of same (발명자 R. P. Lively, A. T. Giorges, D.-Y. Koh, R. Wallace; 번호 US 20180147544A1; 상태 등록)
- 이산화탄소의 전기 스윙 흡착을 위한 파이버 흡착제 (Fiber adsorbent for electric swing adsorption of carbon dioxide) (상태 출원; 출원번호 KR 10-2021-0141816, PCT)
- 메조포러스 세라믹 지지체의 제조방법 (Method for manufacturing mesoporous ceramic support) (상태 출원; 출원번호 KR 10-2022-0017299, PCT)
- 유기용매 정삼투 시스템 (Organic Solvent Forward Osmosis System) (상태 출원; 출원번호 KR 10-2021-0048282)

## 연락

- 교수 이메일: dongyeunkoh@kaist.ac.kr[^team][^about]
- 주소: KAIST, 대전 유성구 대학로 291[^about]

[^home]: MMML 누리집 첫 화면(연구 소개·소식) <https://mmml.kaist.ac.kr/> (2026-10-19 열람)
[^about]: MMML What We Do 페이지 <https://mmml.kaist.ac.kr/what-we-do> (2026-10-19 열람)
[^team]: MMML 팀 페이지 <https://mmml.kaist.ac.kr/team> (2026-10-19 열람)
[^patents]: MMML 특허 페이지 <https://mmml.kaist.ac.kr/patents> (2026-10-19 열람)
[^preprints]: MMML 사전 공개·기고 페이지 <https://mmml.kaist.ac.kr/patents-1> (2026-10-19 열람)
[^crossref]: Crossref 저자 검색(Dong-Yeun Koh, 2021년 이후 학술지)과 논문별 서지 <https://api.crossref.org/works?query.author=Dong-Yeun+Koh> (2026-10-20 조회)
[^p1]: J. Choi 외, D.-Y. Koh, Nature 654, 955-962 (온라인 2026-06-24). <https://doi.org/10.1038/s41586-026-10677-3> 초록 기준(출판사 논문 페이지).
[^p2]: B. Oh, H. Seo, J. Wi, D.-Y. Koh, Science Advances 12, eaee7783 (2026). <https://doi.org/10.1126/sciadv.aee7783> 초록 기준.
[^p3]: J. Choi 외, D.-Y. Koh, Nature Communications 15, 2800 (온라인 2024-03-30). <https://doi.org/10.1038/s41467-024-47115-9> 초록 기준.
[^p4]: B. Oh 외, D.-Y. Koh, Nature Communications 13, 4972 (온라인 2022-08-24). <https://doi.org/10.1038/s41467-022-32703-4> 초록 기준.
[^p5]: B. Oh, I. Park, D.-Y. Koh, Energy & Fuels (온라인 2026-10-13). <https://doi.org/10.1021/acs.energyfuels.6c03763> 초록 기준.
[^p6]: I. Park 외, D.-Y. Koh, Advanced Energy Materials, e71205 (온라인 2026-06-19). <https://doi.org/10.1002/aenm.71205> 초록 기준.
[^p7]: J. Jeong 외, D.-Y. Koh, Carbon Capture Science & Technology 17, 100526 (2025). <https://doi.org/10.1016/j.ccst.2025.100526> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p8]: J. Park 외, D.-Y. Koh, ACS Sustainable Chemistry & Engineering 12, 11510-11519 (온라인 2024-07-21). <https://doi.org/10.1021/acssuschemeng.4c01285> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).

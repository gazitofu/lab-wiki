# 자율화학실험실 (Self-Driving Chemistry Laboratory)

**서울대학교 자연과학대학 화학부 · 한상수 교수**

- 홈페이지: <http://sdcl.snu.ac.kr/>
- 분야: 계산화학, 자율 화학 실험, 인공지능 소재 설계[^faculty][^intro]
- 대분야: 화학, 컴퓨팅·AI
- 태그: 자율 실험실·AI 실험 설계[^sdl], 과학·공학 AI[^intro][^inverse], 분자 동역학 시뮬레이션[^reax]
- 근거와 출처: [자율화학실험실 근거 페이지](sdcl-sources.md)

> 로봇과 인공지능으로 화학 실험을 이어 가고, 원하는 성질의 재료와 반응 조건을 계산으로 찾아 설계하는 연구실이다.

## 무엇을 연구하나

실험에서 얻은 결과를 인공지능(Artificial Intelligence, AI)이 분석하고, 그 결과에 따라 다음 실험을 정하는 자율 실험실을 개발한다. 실험 계획, 장비 실행, 결과 분석이 다시 다음 계획으로 이어지는 폐쇄 고리(결과를 다음 동작의 결정에 되돌려 쓰는 연결)를 만드는 것이 중심이다.[^intro][^sdl]

또 다른 갈래는 원하는 재료의 성질에서 출발해 그 성질을 낼 구조와 만드는 조건을 찾는 역설계다. 계산으로 예측한 내용과 실제 실험에서 관찰한 내용을 연결하는 인공지능 방법을 개발하고, 실험 결과를 계산 모형의 수정과 다음 설계에 활용한다.[^intro][^research][^inverse]

재료의 구조와 반응이 어떻게 연결되는지도 계산으로 연구한다. 반응을 설명하는 계산, 목표 성질에 맞춘 설계, 자동 실험을 이어 붙여 화학 현상을 이해하는 일과 원하는 화학 체계를 만드는 일을 함께 다룬다.[^research]

## 주요 연구 주제

### 로봇 실험과 다음 실험의 자동 선택

로봇이 합성(화학 반응으로 물질을 만드는 일), 물질 취급, 특성 분석(물질의 구조와 성질을 알아보는 측정·해석)을 수행한다. 인공지능은 실험 결과를 학습해 다음에 살펴볼 조건을 고른다. 실험 운영 조정 시스템은 로봇·측정 장비·데이터의 흐름을 맞추어 개별 작업을 연속된 실험 과정으로 연결한다.[^sdl]

### 목표 성질에서 재료 구조와 제조 조건 찾기

원자(화학 원소의 성질을 지닌 물질의 기본 입자)의 배열과 물질의 성질 사이 관계를 인공지능으로 학습하고, 목표 성질에 맞는 재료 구조 후보를 생성·탐색한다. 전자(음의 전기를 띠는 물질의 구성 입자)가 가질 수 있는 상태를 바탕으로 구조와 성질의 관계를 다룬다. 예를 들어 전자 상태 밀도(Density of States, DOS; 전자가 가질 수 있는 상태가 에너지별로 얼마나 있는지 나타내는 양)를 이용한다. 에너지는 물리적 변화를 일으킬 수 있는 능력을 나타내는 양이다. 역설계의 대상을 재료 구조뿐 아니라 합성 경로와 가공 조건으로도 확장한다.[^inverse]

### 촉매의 구조·조성·반응 경로 설계

촉매(반응 후 재생되면서 화학 반응 속도를 높이는 물질)의 원자 배열, 조성(재료를 이루는 성분과 그 비율), 반응 환경이 성능에 미치는 영향을 연구한다. 양자역학(물질과 빛의 상태를 여러 가능한 상태의 결합으로 나타내고 측정 결과의 확률을 계산하는 물리 이론)과 분자(원자들이 결합하여 이루는 입자) 수준의 계산을 연결해 반응이 거치는 중간 상태와 경로를 분석하고, 후보 재료를 계산으로 선별한다. 밀도범함수이론(Density Functional Theory, DFT; 전자 밀도를 바탕으로 물질의 전자 상태를 계산하는 이론) 계산과 분자 동역학(Molecular Dynamics, MD; 입자 사이에 작용하는 힘으로 시간에 따른 움직임을 계산하는 방법)을 이용한다.[^research][^catalyst]

### 결합이 생기고 끊어지는 반응의 계산

반응성 힘장(Reactive Force Field, ReaxFF; 원자 사이의 결합 생성과 끊어짐을 포함해 힘과 에너지를 계산하는 모형)을 개발하고 검증한다. 양자역학 계산 자료를 기준으로 모형의 매개변수(모형의 작동을 정하는 값)를 정하고, 분자 동역학으로 반응 과정의 구조 변화와 재료가 맞닿는 경계에서 일어나는 반응을 계산한다. 원자가 움직인 기록을 분석해 화학 반응과 촉매 반응의 경로를 알아본다.[^reax]

## 교수와 전문 분야

한상수 교수의 전문 분야는 계산화학, 인공지능, 자율 실험실이다. 2026년 9월부터 서울대학교 화학부 교수로 재직하고 있다. 그 전에는 한국과학기술연구원(Korea Institute of Science and Technology, KIST)에서 2013년 6월부터 2026년 8월까지 선임·책임연구원, 2020년 9월부터 2026년 8월까지 계산과학연구센터장을 맡았다.[^people]

한양대학교 재료공학 분야 학사(1999년 2월)·석사(2001년 2월), KAIST 재료공학 분야 박사(2005년 2월) 학위를 받았다. KAIST 응용과학연구소 박사후연구원(2005년 3월–2006년 11월), California Institute of Technology 화학과 방문·박사후연구원(2005년 10월–2009년 1월), 한국표준과학연구원 선임연구원(2009년 2월–2013년 5월) 경력이 있다.[^people]

## 구성원

2026년 11월 5일 누리집 명단 기준으로 박사후연구원 3명, 박사과정 5명, 석사과정 2명, 인턴 연구원 2명이다. 연구 주제 뒤의 「Now」와 기관명은 누리집이 각 사람에게 붙인 표기다.[^people]

| 이름 | 과정·직위 | 연구 주제·Now 표기 | 이메일 |
|---|---|---|---|
| Dr. Soonsung So | 박사후연구원 | Computational Materials Science · Electrocatalysis · Thermal Transport / Now Korea Institute of Science and Technology |  |
| Dr. Seok Ho Lee | 박사후연구원 | Self-Driving Laboratory · Computational Chemistry · Catalysis Engineering / Now Korea Institute of Science and Technology |  |
| Dr. Gyu Seong Yi | 박사후연구원 | Self-Driving Laboratory · Electrocatalysis / Now Seoul National University | gyusyi@snu.ac.kr |
| Heeseung Lee | 박사과정 | Self-Driving Lab, Electrochemistry / Now Korea Institute of Science and Technology |  |
| Daeho Kim | 박사과정 | Self-Driving Lab · Electrochemistry / Now Korea Institute of Science and Technology |  |
| Hyesu Jang | 박사과정 | Self-Driving Lab / Now Korea Institute of Science and Technology |  |
| Hyeondeok Kang | 박사과정 | Self-Driving Lab / Now Seoul National University | khdchlrh@snu.ac.kr |
| Heemin Kim | 박사과정 | Self-Driving Lab / Now Seoul National University | hmkim308@snu.ac.kr |
| Seongjin Bang | 석사과정 | Self-Driving Lab / Now Korea Institute of Science and Technology |  |
| Hyunjung Na | 석사과정 | MD, LLM / Now Korea Institute of Science and Technology |  |
| Byeongho Park | 인턴 연구원 | Self-Driving Lab / Now Seoul National University | byeongho@snu.ac.kr |
| Yunkyung Park | 인턴 연구원 | DFT, MLIP / Now Seoul National University |  |

## 졸업생과 이전 구성원

누리집 Alumni에 적힌 23명으로, 교수의 이전 소속인 한국과학기술연구원(KIST) 시기 구성원을 포함한다. 기간은 누리집의 참여 기간이고, 학위·과정 칸의 역할과 진로는 게시 표기다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Dr. Jeongae Kim | Postdoctoral Researcher (2026.03–2026.09) | Postdoctoral Researcher, DGIST E-MatAX, Korea |
| Dr. Nayeon Kim | Ph.D. Student (2021.03–2026.08) | Senior Researcher, POSCO Holdings Co., Ltd. |
| Dr. Jungwoo Choi | Postdoctoral Researcher (2024.03–2026.08) | Assistant Professor, Dankook University |
| Dr. Doosun Hong | Postdoctoral Researcher (2025.04–2025.08) | Assistant Professor, University of Seoul |
| Dr. Dongyup Shin | Postdoctoral Researcher (2022.09–2025.08) | Assistant Professor, Kangwon National University |
| Dr. Hyuk Jun Yoo | Ph.D. Student & Postdoctoral Researcher (2020.03–2025.06) | Postdoctoral Researcher, University of California, Berkeley, USA |
| Dr. Chen-Hui Chan | Postdoctoral Researcher (2021.01–2024.12) | Assistant Professor, Xiamen University Malaysia |
| Dr. Sooyeon Kim | Postdoctoral Researcher (2021.09–2024.07) | Assistant Professor, Myongji University |
| Dr. Kihoon Bang | Postdoctoral Researcher (2020.10–2024.07) | Principal Researcher, Samsung SDI Co., Ltd. |
| Dr. Hong Woo Lee | Ph.D. Student & Postdoctoral Researcher (2017.03–2023.01) | Senior Researcher, POSCO Holdings Co., Ltd. |
| Ms. Ga-Un Jeong | Intern Researcher (2020.03–2021.08) | Research Scientist, TEL Tokyo Electron Ltd., USA |
| Dr. Mosab Banisalman | Postdoctoral Researcher (2019.09–2021.12) | Staff Scientist, Virtual Lab Co. |
| Dr. Jeongrae Kim | Postdoctoral Researcher (2019.03–2021.08) | Assistant Professor, Korea Polytechnics Chuncheon Campus |
| Dr. Min-Cheol Kim | Postdoctoral Researcher (2018.09–2021.08) | Assistant Professor, Sookmyung Women's University |
| Dr. Byung Chul Yeo | Ph.D. Student & Postdoctoral Researcher (2014.03–2019.04) | Associate Professor, Pukyong National University |
| Dr. Sungjin Pai | Postdoctoral Researcher (2014.09–2018.08) | Chief Researcher, DRB Industrial Co., Ltd. |
| Dr. Sung-Yup Kim | Postdoctoral Researcher (2016.09–2018.08) | Researcher, The Ohio State University, USA |
| Dr. Xiaolong Liu | Visiting Researcher (2017.05–2018.08) | Staff Scientist, China National Petroleum Corporation |
| Dr. Kang-Seop Yun | Ph.D. Student (2015.03–2018.02) | Staff Scientist, SEMES Co., Ltd. |
| Prof. Xiuying Liu | Visiting Researcher (2016.03–2017.02) | Associate Professor, Henan University of Technology, China |
| Dr. Donghun Kim | Postdoctoral Researcher (2015.08–2017.04) | Associate Professor, KAIST |
| Dr. K.P.S.S. Hembram | Postdoctoral Researcher (2013.06–2015.12) | KIST |
| Dr. Li-Ming Yang | Postdoctoral Researcher (2013.06–2014.05) | Associate Professor, Huazhong University of Science and Technology, China |

## 최근 논문 목록 (2021–2026)

누리집의 2021–2026년 구역에 게시된 출판 논문 43편 가운데 Crossref 등록 서지의 출판 날짜 또는 DOI 등록일로 기간 밖으로 판정한 6편을 제외한 37편이다. 교수의 이전 소속인 한국과학기술연구원(KIST) 시기 성과를 포함한다. 2021년 구역에서는 1편을 담았다. Applied Surface Science 562의 150031 논문은 등록 출판 시기가 2021년 10월로 일자가 없으며, DOI 등록일이 2021년 5월 7일이므로 2021년 10월 22일 전 항목으로 판정해 제외했다. 저자 기호 *는 교신저자, †는 공동 기여를 뜻한다. 제목에서 확인되는 연구 대상은 자동 실험과 소재 설계, 촉매 반응, 과산화수소·암모니아 합성, 에너지 소재다.[^pubs][^dates]

**2026**

- H. Lee, D. Kim, H. Lee, N. Gwak, N. Kim, H. J. Yoo, T. Yu, N. Oh, S. S. Sohn\*, and S. S. Han\*. "A Fully Adaptive Automated System for Nanoparticle Washing Enabled by Vision and Language AI". *Chemical Engineering Journal, 543 (2026) 178469*.
- I.-S. Kim†, J. Choi†, S. Lee, J. E. Park, C. Lee, J. Seo, J. H. Kwon, G. Doo, H. Park, D. Lee, W.-C. Cho, C. Kim, N. V. Myung, S. S. Han, B.-S. An\*, M. J. Kim\*, and H.-S. Cho\*. "Engineering MnNiPx Cathode via Dual Role of Mn: Simultaneous Enhancement of Activity and Intermittent Operation Durability". *Advanced Functional Materials, (2026): e76622*.
- N. Kim†, H. J. Yoo†, D. Kim, H. Lee, C. S. Hong, and S. S. Han\*. "SPACESHIP: Autonomous Mapping of Hardware-dependent Synthesizable Space in Solution-Phase Gold Nanomaterials". *Journal of the American Chemical Society, (2026) 148 (18): 19170–19185*.
- H. Lee†, H. J. Yoo†, H. S. Jang, B. Park, Y. J. Park\*, and S. S. Han\*. "Toward Self-Driving Laboratory 2.0 for Chemistry and Materials Discovery". *Materials Horizons, (2026) 13 (10): 4712–4739*.
- J.-G. Lee†, J. W. Choi†, S. Kim†, W. Zhang, H. Shin, J.-H. Kim, E. H. Sargent, S. S. Han\*, J. M. Kim\*, and M.-J. Choi\*. "Ligand-Driven Tuning of Adsorption Energy in Nanocrystals for High-Performance H2O2 Electrosynthesis". *Journal of the American Chemical Society, 148 (2026) 9268*.
- M. Kim†, D. Shin†, M. J. Kim, S. Bae, I. S. Kim, S. S. Han\*, J. G. Kang\*. "Epitaxy-Boosted Oxygen Evolution Reaction in Mesostructured Cobalt Ferrite Electrocatalysts". *Applied Catalysis B: Environment and Energy, 385 (2026) 126245*.

**2025**

- Y. H. Yun†, J. Choi†, Y. Park, H. Park, G. Doo, M. Kim, S. S. Han, J. H. Park\*, S. Lee\*, C. Lee\*, H.-S. Cho\*. "Optimizing Hybrid-phase IrO2 Catalysts with Ti for Enhanced Oxygen Evolution Reaction for Proton Exchange Membrane Water Electrolysis". *Small, 21 (2025) 2503601*.
- Y. Kim†, H. Doo†, D. Shin†, S. Y. Lee†, Y. Roh†, S. Park†, H. Song, Y. Jung, H. J. Yoo, S. S. Han, J. W. Kim, M. O. Besenhard\*, Y. S. Lee\*, J. Na\*. "Self-driving laboratories with artificial intelligence: An overview of process systems engineering perspective". *Computer and Chemical Engineering, 203 (2025) 109266*.
- C.-H. Chan†, C.-K. Hwang†, N. Tamir†, H. Nam†, S. Y. Paek, J. Lim, B. Ulambayar, K. H. Chae, W. Sun, S. Akhade, G. Bucci, S. Y. Lee\*, J. M. Kim\*, S.-H. Cho\*, and S. S. Han\*. "Overcoming Barriers in Electrochemical Toluene Hydrogenation for Efficient Hydrogen Storage by Pt3Au Alloy Catalysts". *ACS Catalysis, 15 (2025) 13667*.
- J. S. Lee†, S. Kim†, S.-H. Kim, J.-H. Baek, C. Li, R. Guan, B.-J. Jang, G.-F. Han\*, S. S. Han\*, and J.-B. Baek\*. "Mechanochemical Ammonia Synthesis Enhanced by Silicon Nitride as a Defect-Inducing Physical Promoter". *Nature Communications, 16 (2025) 5703*.
- D. Shin and S. S. Han\*. "Unlocking Design Strategies for Oxygen Evolution Reaction Catalysts: Insights from a Kinetic Perspective via Constrained Ab Initio Molecular Dynamics Simulations". *Chemical Engineering Journal, 512 (2025) 162357*.
- J. Yoo†, C.-H. Chan†, S. Choi, D. Hong, S. Y. Paek, K. Bang, J. M. Kim, D. Kim\*, S. S. Han\*, and H. M. Lee\*. "Simultaneous Enhancement of Activity and Durability of Oxygen Reduction Reaction Via Pd3Mo@Pt/C Catalysts". *ACS Applied Materials & Interfaces, 17 (2025) 22498*.
- J. W. Choi†, A. Byeon†, S. Kim†, C.-K. Hwang, W. Zhang, J. Lee, W. C. Yun, S. Y. Paek, J. H. Kim, G. Jeong, S. Y. Lee, J. Moon\*, S. S. Han\*, J. W. Lee\*, and J. M. Kim\*. "Mesoporous Boron-Doped Carbon with Curved B4C Active Sites for Highly Efficient H2O2 Electrosynthesis in Neutral Media and Air-Supplied Environments". *Advanced Materials, 37 (2025) 2415712*.
- G. H. Yi†, J. Choi†, H. Song, O. Miano, J. Choi, K. Bang, B. Lee, S. S. Sohn, D. Buttler, A. Hiszpanski\*, S. S. Han\*, and D. Kim\*. "MaTableGPT: GPT-based Table Data Extractor from Materials Science Literature". *Advanced Science, 12 (2025) 2408221*.
- W. Zhang†, T. T. Le†, D. Shin†, S. Nandy, J. W. Choi, S. Y. Paek, C.-K. Hwang, J. H. Kim, H. Suh, K. H. Chae, S. Y. Lee, S. S. Han\*, S. H. Kim\*, and J. M. Kim\*. "Higher-Valent Nickel Oxides with Enhanced Two-Electron Oxygen Reduction in Advanced Electro-Fenton System for Organic Pollutants Degradation". *Applied Catalysis B: Environment and Energy, 361 (2025) 124666*.

**2024**

- H. J. Yoo, K.-Y. Lee\*, D. Kim\*, and S. S. Han\*. "OCTOPUS: Operation Control System for Task Optimization and Job Parallelization via User-Optimal Scheduler". *Nature Communications, 15 (2024) 9669*.
- S. P. Stier\*, C. Kreisbeck, H. Ihssen, M. A. Popp, J. Hauch, K. Malek, M. Reynaud, T. P. M. Goumans, J. Carlsson, I. Todorov, L. Gold, A. Räder, W. Wenzel, S. T. Bandesha, P. Jacques, F. Garcia-Moreno, O. Arcelus, P. Friederich, S. Clark, M. Maglione, A. Laukkanen, I. E. Castelli, J. Carrasco, M. C. Cabanas, H. S. Stein, O. Ozcan, D. Elbert, K. Reuter, C. Sheurer, M. Demura, S. S. Han, T. Vegge, S. Nakamae, M. Fabrizio, and M. Kozdras. "Materials Acceleration Platforms (MAPs): Accelerating Materials Research and Development to Meet Urgent Societal Challenges". *Advanced Materials, 36 (2024) 2407791*.
- S. Choi†, D. Hong†, H. W. Yang, J. Roh, J. Yoo, C. Lee, M. Kim, Y. H. Yun, K. Bang, J. M. Kim, E. A. Cho, S. S. Han\*, D. Kim\*, and H. M. Lee\*. "Enhancing Fuel Cell Durability with Heteroenergetic TaOx-Carbon Support". *ACS Energy Letters, 9 (2024) 4265-4272*.
- C.-K. Hwang†, S. Kim†, K. R. Yoon†, T. T. Le, C. V. Hoang, J. W. Choi, W. Zhang, S. Y. Paek, C. H. Lee, J. H. Lee, K. H. Chae, S. Jeong, S. Y. Lee, B.-K. Ju, S. H. Kim\*, S. S. Han\*, and J. M. Kim\*. "Arc Plasma Deposited Co Single Atom Catalysts Supported on Aligned Carbon Nanofiber for Hydrogen Peroxide Electrosynthesis and an Electro-Fenton Process". *Carbon Energy, 6 (2024) e582*.
- H. J. Yoo†, N. Kim†, H. Lee, D. Kim, L. T. C. Ow, H. Nam, C. Kim, S. Y. Lee, K.-Y. Lee\*, D. Kim\*, and S. S. Han\*. "Bespoke Metal Nanoparticle Synthesis at Room Temperature and Discovery of Chemical Knowledge on Nanoparticle Growth Via Autonomous Experiments". *Advanced Functional Materials, 34 (2024) 2312561*.
- K. Bang†, J. Kim†, D. Hong†, D. Kim\*, and S. S. Han\*. "Inverse Design for Materials Discovery from Multidimensional Electronic Density of States". *Journal of Materials Chemistry A, 12 (2024) 6004-6013*.
- J. Kim, M.-C. Kim, S. S. Han, and K. Cho\*. "Accessible Ni-Fe-Oxalate Framework for Electrochemical Urea Oxidation with Radically Enhanced Kinetics". *Advanced Functional Materials, 34 (2024) 2315625*.
- L. C. O. Tiong†, H. J. Yoo†, N. Kim, C. S. Hong, K.-Y. Lee\*, S. S. Han\*, and D. Kim\*. "Machine Vision-Based Detections of Transparent Chemical Vessels Toward the Safe Automation of Materials Synthesis". *npj Computational Materials, 10 (2024) 42*.
- S. Venkateswalu†, S. Kim†, M. Balamurugan, Y. Son, S.-I. Choi, M. Yoon, K. T. Nam, S. S. Han\*, and M. J. Kim\*. "Boron Nitride Nanotubes Supported Icosahedral Pd Nanoparticles: Enabling Ultrahigh Current Density-Superior Hydrogen Evolution Activity and Theoretical Insights". *Applied Catalysis B: Environmental, 345 (2024) 123609*.
- S. Kim†, Y. Lee†, K. Kim, B. C. Wood\*, S. S. Han\*, and S. Yu\*. "Fluorine-Substituted Lithium Chloride Solid Electrolytes for High-Voltage All-Solid-State Lithium-Ion Batteries". *ACS Energy Letters, 9 (2024) 38-47*.

**2023**

- S. Kim†, M.-C. Kim†, B. C. Yeo, and S. S. Han\*. "High-Throughput Design of Bimetallic Core-Shell Catalysts for Electrochemical Nitrogen Reduction Reaction". *Journal of Materials Chemistry A, 11 (2023) 24686-24697*.
- Y. Park†, C.-K. Hwang†, K. Bang, D. Hong, H. Nam, S. Kwon, B. C. Yeo, D. Go, J. An, B.-K. Ju, S. H. Kim, J. Y. Byun, S. Y. Lee, J. M. Kim\*, D. Kim\*, S. S. Han\*, and H. M. Lee\*. "Machine Learning Filters Out Efficient Electrocatalysts in the Massive Ternary Alloy Space for Fuel Cells". *Applied Catalysis B: Environmental, 339 (2023) 123128*.
- J. Choi†, K. Bang†, S. Jang, J. W. Choi, J. Ordonez, D. Buttler, A. Hiszpanski, T. Yong-Jin Han, S. S. Sohn, B. Lee, K.-R. Lee, S. S. Han\*, and D. Kim\*. "Deep Learning of Electrochemical CO2 Conversion Literature Reveals Research Trends and Directions". *Journal of Materials Chemistry A, 11 (2023) 17628*.
- K. Bang, D. Hong, Y. Park, D. Kim\*, S. S. Han\*, and H. M. Lee\*. "Machine Learning-Enabled Exploration of the Electrochemical Stability of Real-Scale Metallic Nanoparticles". *Nature Communications, 14 (2023) 3004*.
- C.-H. Chan, S. Y. Lee, and S. S. Han\*. "Origin of Enhanced Toluene Hydrogenation by Pt-Ru Catalysts for an Efficient Liquid Organic Hydrogen Carrier". *International Journal of Hydrogen Energy, 48 (2023) 33590-33598*.
- W. Zhang†, J. W. Choi†, S. Kim†, T. T. Le, S. Nandy, C.-K. Hwang, S. Y. Paek, A. Byeon, K. H. Chae, S. Y. Lee, S. H. Kim, H. Song, J. Kim, J. Oh, J. W. Lee, S. S. Han\*, and J. M. Kim\*. "Penta Nitrogen Coordinated Cobalt Single Atom Catalysts with Oxygenated Carbon Black for Electrochemical H2O2 Production". *Applied Catalysis B: Environmental, 331 (2023) 122712*.
- A. Byeon†, J. W. Choi†, H. W. Lee†, W. C. Yun, W. Zhang, C.-K. Hwang, S. Y. Lee, S. S. Han\*, J. M. Kim\*, and J. W. Lee\*. "CO2-Derived Edge-Boron-Doped Hierarchical Porous Carbon Catalysts for Highly Effective Electrochemical H2O2 Production". *Applied Catalysis B: Environmental, 329 (2023) 122557*.
- M.-C. Kim†, J. Chung†, T.-Y. An†, J. Lee, M.-K. Han, S. S. Han\*, U. Sim\*, and T. Yu\*. "Paradox of Thiourea: A False-Positive and Promoter for Electrochemical Nitrogen Reduction on Nickel Sulfide Catalysts". *Applied Catalysis B: Environmental, 328 (2023) 122485*.
- S. Phyo, S. Kim, H. Lee, S. S. Han, Y. Oh\*, and J. Lee\*. "Adsorption Enhancement of Hazardous Odor Gas Using Controlled Thermal Oxidation of Activated Carbon". *Journal of Cleaner Production, 393 (2023) 136261*.
- H. W. Lee†, G.-U. Jeong†, M. C. Kim, D. Kim\*, S. Kim\*, and S. S. Han\*. "Atomistic Origin of Mechanochemical NH3 Synthesis on Fe Catalysts". *International Journal of Hydrogen Energy, 48 (2023) 2931-2941*.

**2022**

- M. Banisalman, M.-C. Kim\*, and S. S. Han\*. "Origin of Enhanced Ammonia Synthesis on Ru-Co Catalysts Unraveled by Density Functional Theory". *ACS Catalysis 12 (2022) 1090-1097*.

**2021**

- H. W. Lee†, E. Jung†, G.-H. Han†, M.-C. Kim, D. Kim, K.-Y. Lee\*, S. S. Han\*, and T. Yu\*. "Three-in-One Strategy to Improve Both Catalytic Activity and Selectivity: Nonconcentric Pd-Au Nanoparticles". *Journal of Physical Chemistry Letters, 12 (2021) 11098-11105*.

## 심사 중 논문

누리집 Submitted 구획의 6편이며 출판 논문과 구분한다. 교수의 이전 소속인 한국과학기술연구원(KIST) 시기 연구를 포함하는 목록이다. 제출 날짜가 게시되지 않아 특정 연도 구역에 두지 않는다.[^pubs]

- J. Kim†, S. So†, J. S. Lim†, J. G. Lee, J. Kim, S. Kim, S.-P. Cho, C. H. Choi\*, B. Seo\*, S. S. Han\*, and S. H. Joo\*. "Multi-Descriptor Screening Reveals d0 Alloying as a Design Strategy for Stable Ruthenium Oxide Catalysts for Acidic Oxygen Evolution". 심사 중.
- J. S. Lee†, S. So†, S.-H. Kim†, S. J. Lee, C. Li, R. Guan, Y. Shao, J. Li, S. S. Han\*, and J.-B. Baek\*. "Orthogonal K-Ba Co-promotion for Kinetically Matched Mechanochemical Ammonia Synthesis". 심사 중.
- Y. J. Jang†, J. Choi†, Y. Kim†, J. S. Myeong, S.-C. Kim, J. Manassa, R. Hovden, M.-H. Jung, J. H. Moon, S. S. Han\*, B. C. Park\*, and Y. K. Kim\*. "Adaptive Fe-Site Reconstruction for Efficient Water Oxidation". 심사 중.
- D. Kim†, H. Nam†, S. Y. Paek†, N. Kim, H. Lee, H. J. Yoo, S. K. Kwak\*, J. M. Kim\*, S. Y. Lee\*, and S. S. Han\*. "Overcoming the Trade-off Between the Activity, Stability, and Cost of OER Catalysts for PEM Water Electrolysis in a Self-Driving Laboratory". 심사 중.
- H. Lee†, T. K. Lee†, D. Shin†, Z. Tao, J. Kim, S. Oh, W.-S. Kim\*, S. S. Han\*, S. J. Yoo\*, and T. Yu\*. "Scalable Synthesis of Ultrathin NiFe-LDH Using Couette-Taylor Reactor for Efficient Oxygen Evolution Reaction". 심사 중. DOI: 10.1149/MA2026-01361798mtgabs.
- H. J. Yoo†, D. Kim†, S. Yim, and S. S. Han\*. "NanoChef: AI Framework for Simultaneous Optimization of Synthesis Sequences and Reaction Conditions at Autonomous Laboratories". 심사 중. DOI: 10.26434/chemrxiv-2025-96bmc.

## 수상과 선정

2021년 10월 22일–2026년 10월 22일에 드는 수상 소식 5건이다. 교수의 이전 소속인 한국과학기술연구원(KIST) 시기 성과를 포함한다.[^awards]

- 2024-10-29 · 한상수, 대한금속재료학회 제1회 첨단소재학술상 수상
- 2023-07-05 · 유혁준 박사과정 학생, 2023년도 Nanokorea 국제학술대회에서 우수 포스터 발표상 수상
- 2023-04-28 · 유혁준 박사과정 학생, 대한금속재료학회 춘계학술대회 우수 구두 발표상 수상
- 2022-11-06 · 유혁준 박사과정 학생, ENGE 국제학술대회 우수 포스터 발표상 수상
- 2021-10-27 · 이홍우 박사과정 학생, 한국화학공학회 가을 총회 및 국제학술대회 우수 구두 발표상 수상

## 연락과 위치

- 주소: 서울특별시 관악구 관악로 1 서울대학교 화학부 503동[^contact]
- 교수실: 503동 3층 322호, 02-880-1456[^contact]
- 학생실: 503동 3층 330호, 02-880-4367[^contact]
- 실험실: 503동 3층 302호·303호[^contact]
- 교수 이메일: sangsoo@snu.ac.kr[^contact]
[^faculty]: 서울대학교 화학부 [전임교수 목록](https://chem.snu.ac.kr/research-faculty/faculty/fulltime)과 [한상수 교수 소개](https://chem.snu.ac.kr/research-faculty/faculty/fulltime?mode=view&profidx=100&sc=y). 교수 소개의 연구실 이름은 「자율화학실험실」이며 직급은 교수다. 연구 분야는 물리화학, 고분자/재료화학, 이론/계산, 에너지/환경으로 적혀 있다. 관측일 2026-11-05.
[^intro]: 연구실 [첫 화면](http://sdcl.snu.ac.kr/). 인공지능·자동화·분자 계산을 통합하고, 실험을 스스로 설계·수행·분석하는 자율 실험실과 실험 관찰·이론 예측을 연결하는 인공지능 방법을 개발한다고 소개한다. 관측일 2026-11-05.
[^research]: 연구실 [Research](http://sdcl.snu.ac.kr/research.html). 계산·인공지능·자율 실험을 연결하며, 촉매 설계에 밀도범함수이론과 분자 동역학을 사용하고 실험 결과로 계산 모형을 수정한다고 소개한다. 관측일 2026-11-05.
[^sdl]: 연구실 [Self-Driving Laboratory](http://sdcl.snu.ac.kr/research01.html). 로봇의 합성·취급·특성 분석, 실험 결과에서 다음 조건을 선택하는 인공지능, 로봇·장비·데이터 흐름을 조정하는 실험 운영 시스템을 연구한다고 소개한다. 관측일 2026-11-05.
[^inverse]: 연구실 [Inverse Design by AI](http://sdcl.snu.ac.kr/research02.html). 목표 성질에서 재료 구조를 생성·탐색하고, 전자 상태 밀도 등의 정보로 구조·성질 관계를 학습하며 합성·가공 조건까지 역설계한다고 소개한다. 관측일 2026-11-05.
[^catalyst]: 연구실 [Catalyst Design](http://sdcl.snu.ac.kr/research03.html). 원자 구조·조성·반응 환경과 촉매 성능의 관계, 여러 규모를 연결하는 계산, 반응 경로와 중간 상태 분석, 후보 촉매의 계산 선별을 연구한다고 소개한다. 관측일 2026-11-05.
[^reax]: 연구실 [ReaxFF](http://sdcl.snu.ac.kr/research04.html). 양자역학 자료를 기준으로 반응성 힘장 매개변수를 개발·검증하며, 결합 생성·해리와 구조 변화를 분자 동역학으로 계산하고 원자 이동 기록에서 반응 경로를 분석한다고 소개한다. 관측일 2026-11-05.
[^people]: 연구실 [Members](http://sdcl.snu.ac.kr/members.html). 교수 학력·경력, 박사후연구원·박사과정·석사과정·인턴 연구원 명단과 연구 주제·현재 기관·학교 이메일, Alumni의 기간·역할·진로 표기. 관측일 2026-11-05.
[^pubs]: 연구실 [Publication](http://sdcl.snu.ac.kr/publications.html)과 [논문 목록 자료](http://sdcl.snu.ac.kr/publications.json). 연도 구역과 Submitted 구획, 저자·제목·학술지·권·쪽·DOI를 연구실 게시 표기로 옮겼다. Publication의 기호 설명은 * 교신저자, † 공동 기여다. 관측일 2026-11-05.
[^dates]: Crossref 등록 서지의 출판 날짜. [Acta Materialia 205, 116563](https://api.crossref.org/works/10.1016/j.actamat.2020.116563)은 2021년 2월호, [ACS Applied Materials & Interfaces 13, 17577–17585](https://api.crossref.org/works/10.1021/acsami.1c01947)는 온라인 2021-04-09, [Journal of Physical Chemistry Letters 12, 4490–4495](https://api.crossref.org/works/10.1021/acs.jpclett.1c01223)는 온라인 2021-05-06, [Scientific Reports 11, 11604](https://api.crossref.org/works/10.1038/s41598-021-91068-8)는 온라인 2021-06-02, [Journal of Physical Chemistry Letters 12, 8376–8383](https://api.crossref.org/works/10.1021/acs.jpclett.1c02305)는 온라인 2021-08-26이다. [Applied Surface Science 562, 150031](https://api.crossref.org/works/10.1016/j.apsusc.2021.150031)은 출판 시기가 2021년 10월로 일자 없이 등록되어 있으며 DOI 등록일(created)은 2021-05-07이고, [Journal of Physical Chemistry Letters 12, 11098–11105](https://api.crossref.org/works/10.1021/acs.jpclett.1c03256)는 온라인 2021-11-09다. 열람일 2026-11-06.
[^awards]: 연구실 [News](http://sdcl.snu.ac.kr/news.html)와 [소식 목록 자료](http://sdcl.snu.ac.kr/news.json)의 Award 구분. 수상 날짜와 수상자를 해당 글의 표기로 옮겼다. 관측일 2026-11-05.
[^contact]: 연구실 [Contact](http://sdcl.snu.ac.kr/about.html)의 교수실·학생실·실험실·전화·교수 이메일 표기. 관측일 2026-11-05.

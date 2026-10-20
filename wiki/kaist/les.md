# 에너지·지속가능성 연구실 (Laboratory for Energy and Sustainability, LE&S)

**KAIST 신소재공학과 · 오지훈 교수**

- 분야: 전기화학적 이산화탄소 전환(전극 촉매, 전해 시스템, 이론), 질산염 환원 암모니아 생산, 글리세롤 등 바이오매스 고부가화, AI 기반 자율 전기화학 실험
- 홈페이지: <https://les.kaist.ac.kr/>
- 근거와 출처: [LE&S 근거 페이지](les-sources.md)

> 전기를 써서 이산화탄소, 폐수 속 질산염, 바이오디젤 부산물 같은 버려지는 물질을 쓸모 있는 화학물질로 바꾸는 연구실이다. 반응을 잘 일으키는 촉매 소재를 설계하고, 그 촉매가 왜 잘 듣는지 계산으로 따지며, 실제로 돌릴 수 있는 전해 장치까지 만든다.[^home][^research]

## 무엇을 연구하나

연구실의 중심 주제는 **전기화학적 이산화탄소 환원**이다. 이산화탄소를 전기로 일산화탄소, 에틸렌, 에탄올 같은 쓸모 있는 물질로 바꾸면 화석연료로 같은 물질을 만들 때보다 탄소 배출을 줄일 수 있고, 재생에너지 전기로 돌리면 배출이 마이너스가 될 수도 있다고 연구실은 설명한다. 이를 위해 촉매(반응을 빠르게 하지만 자신은 소모되지 않는 물질), 시스템, 이론을 함께 연구한다.[^research]

촉매 연구에서는 어떤 물질 성질이 촉매 성능을 결정하는지 찾는 데 공을 들인다. 이런 성질을 기술자(descriptor)라고 부르는데, 대표적인 것이 d-밴드 중심(금속 속 전자 에너지 분포의 중심으로, 분자가 금속 표면에 붙는 세기와 관련된 값)이다.[^p1][^p2] 대표 논문에서는 구리 합금의 d-밴드 중심이 생성물 종류를 가른다는 것을 보였고,[^p2] 반대로 구리가 아닌 합금에서는 이 기술자가 맞지 않는다는 한계도 밝혔다.[^p1] 구리와 세륨산화물을 섞은 촉매에서 구리 원자가 반응 중 작은 덩어리로 모이며 탄소 원자가 둘 이상인 생성물(C2+)이 늘어나는 과정도 추적했다.[^p3]

시스템 연구에서는 이산화탄소를 포집한 용액을 바로 전기분해하는 장치를 만든다.[^papers] 대표 논문에서는 바이폴라막(물을 수소 이온과 수산화 이온으로 나누는 막) 전해조로 포집 용액에서 합성가스(수소와 일산화탄소의 혼합 기체)를 낮은 전압으로 만들었다.[^p5]

이산화탄소 밖으로도 넓힌다. 농업·산업 폐수에 쌓이는 질산염을 온화한 조건에서 전기로 암모니아로 바꾸면, 에너지와 탄소를 많이 쓰는 기존 하버-보슈 공정(질소와 수소로 암모니아를 만드는 공업 공정)을 대신할 수 있다고 본다.[^research] 대표 논문에서는 코발트와 구리를 원자·초미세 덩어리 형태로 함께 붙인 촉매로 질산염을 암모니아로 바꿨다.[^p6] 바이오디젤을 만들 때 남아도는 글리세롤을 전기로 산화해 값나가는 화학물질로 바꾸면서 반대쪽 전극에서 수소도 얻는 연구도 한다.[^research]

최근에는 **AI 기반 자율 전기화학 연구**를 내세운다. 문헌·데이터로 가설을 세우고 실험 조건을 최적화하는 실험 설계, 로봇으로 전기화학 실험을 돌리는 자동 실험, AI 에이전트로 데이터를 처리하는 자동 분석, AI를 곁들인 양자역학 계산(DFT)으로 반응 원리를 찾는 시뮬레이션을 하나의 순환 흐름으로 묶는다고 소개한다.[^research]

## 주요 연구 주제

### 1. 이산화탄소 환원 촉매와 기술자

구리 합금·비구리 합금의 전자 구조 기술자, 구리-세륨산화물 계면, 구리-아연 합금.[^p1][^p2][^p3][^p4] 대표 논문 1–4.

### 2. 탄소 포집과 전환을 잇는 전해 시스템

바이폴라막 전해로 포집 용액에서 합성가스 생산.[^p5] 대표 논문 5.

### 3. 질산염 환원 암모니아 생산

코발트-구리 복합 촉매의 연속 반응.[^p6] 대표 논문 6.

## 대표 논문

랩 논문 목록의 2021–2026년 논문 가운데 오지훈 교수가 교신저자(랩 표기 *)인 것에서 연구 주제를 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2026 | [Peaks and pitfalls of electrocatalytic CO2 reduction descriptor models](https://doi.org/10.1038/s41929-026-01526-7) · Nature Catalysis | 금, 은, 팔라듐 합금의 조성을 바꿔 d-밴드 중심과 일함수(전자를 금속 밖으로 떼어 내는 데 드는 에너지)를 연속으로 조절하며 이산화탄소 환원을 조사했다. 일산화탄소 생성은 d-밴드 중심이 결정했지만, 구리와 같은 기술자 값을 가진 비구리 합금은 C2+ 생성물을 전혀 만들지 못했다. 계산으로 표면의 불균일성 때문이라고 설명하며, 기존 기술자 모델을 복잡한 소재와 여러 단계 반응에 그대로 옮기기 어렵다는 점을 보였다.[^p1] | 공동 1저자 B. Kim·S. Han·S. Wang, 교신 S. Ringe·오지훈 |
| 2 | 2025 | [Understanding Electrochemical CO2 Reduction Selectivity of Cu Binary Alloys from Electronic Structure Descriptors](https://doi.org/10.1021/jacs.5c14093) · Journal of the American Chemical Society | 구리에 니켈, 팔라듐, 은, 금, 아연, 크롬을 섞은 합금으로 실험과 계산을 함께 해, d-밴드 중심이 생성물 분포를 가르는 핵심 기술자임을 보였다. d-밴드 중심이 높을수록 일산화탄소가 많아졌고 에틸렌·에탄올은 산 모양(화산형) 경향을 보였으며, 에틸렌과 에탄올 사이의 선택성을 맞추는 설계 지침을 제시했다.[^p2] | 공동 1저자 Y. Jung·H. G. Abbas·S. Kim·B. Kim, 교신 C. H. Choi·S. Ringe·오지훈 |
| 3 | 2023 | [Tuning the C1/C2 Selectivity of Electrochemical CO2 Reduction on Cu-CeO2 Nanorods by Oxidation State Control](https://doi.org/10.1002/adma.202208996) · Advanced Materials | 세륨산화물 나노막대에 구리를 넣은 촉매에 환원 전압을 걸면, 흩어져 있던 구리 이온이 갑자기 작은 구리 덩어리로 모인다는 것을 반응 중 분석과 계산으로 확인했다. 흩어진 구리는 탄소 하나짜리 생성물을 주로 만들지만, 이 덩어리는 탄소끼리 잇는 반응을 쉽게 해 C2+ 탄화수소를 선택적으로 만들었고, 구리 무게당 C2+ 생산 전류가 구리-탄소 촉매의 27배였다.[^p3] | 공동 1저자 S. Hong·H. G. Abbas·K. Jang, 교신 P.-P. Choi·S. Ringe·오지훈 |
| 4 | 2022 | [Electrochemical Carbon Dioxide Reduction on Copper-Zinc Alloys: Ethanol and Ethylene Selectivity Analysis](https://doi.org/10.1039/d1ta10345h) · Journal of Materials Chemistry A | 구리-아연 합금에서 원자가 놓인 방식이 이산화탄소 환원의 에탄올 선택성을 높인다는 것을 보이고, 양자역학 계산(DFT)으로 뒷받침했다.[^p4] | 공동 1저자 Yeji Baek·Hakhyeon Song·Deokgi Hong, 교신 Young-Chang Joo·Gun-Do Lee·오지훈 |
| 5 | 2026 | [Low-voltage syngas synthesis via BPM electrolysis of CO2 capture and aldehyde solution](https://doi.org/10.1039/d5ee07845h) · Energy & Environmental Science | 이산화탄소를 포집한 중탄산염(탄산수소염) 용액의 전기분해와 포름알데하이드(가장 간단한 알데하이드 화합물) 산화를 하나의 바이폴라막 전해조에 묶어, 수소와 일산화탄소가 1대 1인 합성가스를 1.7 V, 200 mA/cm²에서 바로 만들었다. 두 반응의 패러데이 효율(흘린 전기 가운데 원하는 생성물에 쓰인 비율)을 합치면 200%였다.[^p5] | 공동 1저자 P. Huang·H. Choi, 교신 오지훈·H. Song·M. C. Hatzell |
| 6 | 2024 | [Tandem Electroreduction of Nitrate to Ammonia Using a Cobalt–Copper Mixed Single-Atom/Cluster Catalyst with Synergistic Effects](https://doi.org/10.1002/advs.202407250) · Advanced Science | 탄소 위에 코발트와 구리를 원자 하나 또는 아주 작은 덩어리로 흩어 붙인 촉매에서, 구리가 질산염을 아질산염(질산 이온에서 산소 하나가 빠진 이온)으로, 코발트가 아질산염을 암모니아로 바꾸는 연속 반응이 일어나 낮은 전압에서 암모니아 패러데이 효율 91.2%를 얻었다. 바이폴라막 전해 장치에서 32시간 안정적으로 돌려 1 M(리터당 1몰) 넘는 농도의 암모니아를 만들고 고순도 염화암모늄으로 바꿨다.[^p6] | 공동 1저자 J. Suh·H. Choi, 교신 오지훈 |

## 교수와 전문 분야

오지훈 교수는 포항공대 신소재공학 학사(2000), 서울대 재료공학 석사(2002), 미국 MIT 재료공학 박사(2010)를 받았다. 석사 뒤 한국전자통신연구원(ETRI) 나노전자소자팀 연구원(2002–2004)으로 일했고, 박사 뒤 미국 국립재생에너지연구소(NREL) 태양광센터 박사후연구원(2010–2013)으로 태양전지와 태양광 연료 생산용 나노 구조 실리콘 소재를 연구했다. 2013년 KAIST EEWS대학원 조교수로 부임해 2018년 신소재공학과로 옮겼고, 2024년부터 신소재공학과와 녹색성장지속가능대학원 교수다.[^prof]

논문으로 보면 전문 분야는 세 갈래다.

- **이산화탄소 환원 전극 촉매 설계와 촉매 기술자 분석**.[^p1][^p2][^p3][^p4]
- **탄소 포집과 연계한 전해 공정**.[^p5]
- **질산염 환원 등 질소 화합물 전기화학 전환**.[^p6]

## 응용 분야

대표 논문과 연구 소개로 보면 이산화탄소를 원료로 쓰는 화학물질 생산, 탄소 포집과 전환의 결합, 폐수 질산염을 이용한 암모니아 생산, 바이오디젤 부산물 활용에 닿아 있다.[^p3][^p5][^p6][^research] 랩 특허 목록에는 2021년 이후 이산화탄소 환원 촉매·전해셀, 암모니아 합성, 단일 원자 촉매 제조 등 특허가 17건 있고, 2025년 최현욱 박사과정 학생의 특허가 기술이전됐다고 랩 소식이 적는다.[^patents][^news] 졸업생은 삼성전자, SK하이닉스, 한국에너지기술연구원 등과 홋카이도대·KIST·조지아공대·MIT 박사후연구원으로 진출했고, 연구교수 출신 두 명은 규슈대와 경기대 조교수가 됐다.[^alumni]

## 구성원

2026년 10월 20일 랩 Member 페이지 기준이다. 이름은 랩 표기(성, 이름)를 따랐고, 연구 주제와 이메일은 랩이 적은 것이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Choi, Hyeonuk | 박사후연구원 | Electrochemical CO2 Reduction | gkdis4285@kaist.ac.kr | 5, 6 |
| Ha, Taehyeon | 박사후연구원 | Electrochemical CO2 Reduction | taehyeonha@kaist.ac.kr |  |
| Wang, Sun Eon | 박사과정 | Electrochemical CO2 Reduction | wsunun@kaist.ac.kr | 1, 4 |
| An, Eunui | 박사과정 | Electrochemical Glycerol Oxidation | euni11@kaist.ac.kr |  |
| Suh, Jungwon | 박사과정 | Nitrate Reduction for Ammonia Production | alstonida7@kaist.ac.kr | 6 |
| Lee, Chung Hyeon | 박사과정 | Biomass upgrading | ing03042@kaist.ac.kr |  |
| Kim, Soeun | 박사과정 | Electrochemical CO2 Reduction | soeun@kaist.ac.kr | 2 |
| Jang, Youngboo | 박사과정 | Electrochemical CO2 reduction | wkd2102@kaist.ac.kr |  |
| Kim, Jiwon | 박사과정 | Electrochemical CO2 reduction | kimxjw@kaist.ac.kr |  |
| Kim, Yekyong | 박사과정 | Electrochemical CO2 reduction | kimekyong@kaist.ac.kr |  |
| Lee, Hakseong | 박사과정 | Electrochemical NO3 reduction | hak7918@kaist.ac.kr |  |
| Suh, Beomseok | 박사과정 | Electrochemical CO2 reduction | tjqjatjr0424@kaist.ac.kr |  |
| Byeun, Hyejin | 석사과정 | Electrochemical CO2 Reduction | dirhkdtor1@kaist.ac.kr |  |
| Lee, Junhyeok | 석사과정 | Electrochemical CO2 Reduction | ljh0711@kaist.ac.kr |  |
| Kim, Seungchan | 석사과정 | Electrochemical CO2 Reduction | starlight311@kaist.ac.kr |  |

## 졸업생

랩 Alumni 게시판의 이름, 과정, 랩이 적은 현재 소속이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Lee, Seulyi | 박사후연구원 | Postdoctoral fellow at Jeonbuk National University |
| Kong, Yujin | 박사 | Postdoctoral fellow at Institute for Catalysis, Hokkaido University |
| Kim, Dohee | 박사 | Postdoctoral fellow at Korea Institute of Science and Technology (KIST) |
| Kang, Mihyun | 석사 | SK hynix |
| Kim, Beomil | 박사 | Samsung Electronics |
| Kim, Yoon Young | 박사후연구원 | Postdoctoral fellow at Korea Institute of Energy Research |
| Lee, JuHo | 박사 | Samsung Electronics |
| Hong, SeungWon | 박사 | Samsung Electronics |
| Kim, Jaehoon | 박사후연구원 | Hyundai |
| Song, Hakhyeon | 박사 | Postdoctoral fellow at Georgia Tech |
| Song, Jun Tae | 연구교수 | Assistant Professor, Kyushu university (2019 ~ ) |
| Ryu, Sangwoo | 연구교수 | Assistant Professor, Kyonggi University (2018 ~ present) |
| Tan, Ying Chuan | 박사후연구원 | Institute of Materials Research and Engineering, A\*STAR |
| Patra, Kshirodra Kumar | 박사후연구원 |  |
| Kim, Namwoon | 박사 | Samsung Electro-Mechanics |
| Park, Bo-In | 박사 | Post-doctoral Associate at MIT |
| Lee, Yonghwan | 박사 | Korea Electronics Technology Institute |
| Park, Sanghyun | 박사 | Samsung Electronics |
| Cho, Minhyung | 박사 | Samsung Electronics |
| Oh, Seungtaeg | 박사 | SK hynix |
| Kim, Young Eun | 박사 | Korea Institute of Energy Research |
| Choi, Byeonguk | 박사 | Samsung Engineering |
| Jeong, ByongJoo | 석사 | SK hynix |
| Lee, BermRye | 석사 | 한국유미코아 |
| Baek, Yeji | 박사 | Samsung electronics |
| Jung, YuJin | 석사 | SK Hynix |

## 최근 논문 목록 (2021–2026)

랩 Journals 게시판의 2021년 이후 논문이다. ‡는 공동 1저자, *는 교신저자를 뜻하는 랩 표기이고, 괄호 안 표지 선정은 랩 표기다.[^papers]

**2026**

- H. J. Choi, H. Song, M. Tahmid, H. Choi, J. Oh, M. C. Hatzell. "Integrated Bipolar Membrane Electrodialysis and Electrolysis for CO2 Capture and Conversion". *Advanced Energy Materials*.
- H. C. Kim, H. Lee, J. Park, W. H. Lee, H. Choi, J. Oh, M. H. Han, C. Oh, M. G. Ha, E. Kang, W. Kim, K. B. Lee, J.-Y. Choi, U. Lee\*, Y.-J. Ko\*, H.-S. Oh\*. "Sunken-Serpentine Flow-Field Engineering Unlocks Ampere-Level CO2 Electrolysis via Local CO2 Enrichment and Water Management". *ACS Energy Letters*.
- E. Dentzer, H. Kim, Y. Zhu, H. Song, N. Callen, C. A. R. Torres, H. Choi, J. Oh, M. C. Hatzell\*, K. B. Hatzell\*. "Impact of Interposer Microstructure on Ionic Transport in Liquid-Phase Bicarbonate Electrolysis". *ACS Electrochemistry*.
- B. Kim‡, S. Han‡, S. Wang‡, S. Ringe\*, J. Oh\*. "Peaks and pitfalls of electrocatalytic CO2 reduction descriptor models". *Nature Catalysis*.
- P. Huang‡, H. Choi‡, A. Venkataraman, O. Vulpin, C. A. R. Torres, D. A. C. Haro, Yaguang Zhu, E.R. Yamazaki, K. B. Hatzell, S W. Boettcher, S. Nair, J. Oh\*, H. Song\*, M.C. Hatzell\*. "Low-voltage syngas synthesis via BPM electrolysis of CO2 capture and aldehyde solution". *Energy & Environmental Science*.
- Y. Kong‡, D. Kwon‡, J. Son‡, W. Kim, H. Shin, J. Oh. "Interfacial water dynamics on an inverse Cu–CeO2 catalyst for enhanced electrochemical ammonia production". *Applied Catalysis B: Environment and Energy*.

**2025**

- Y. Jung‡, H. G. Abbas‡, S. Kim‡, B. Kim‡, J. Cho, S. Han, H. Song, Y. Takaoka, J. T. Song, T. Ishihara, C. H. Choi\*, S. Ringe\*, J. Oh\*. "Understanding Electrochemical CO2 Reduction Selectivity of Cu Binary Alloys from Electronic Structure Descriptors". *Journal of the American Chemical Society*.
- V. V. Burungale.‡, M. A. Gaikwad.‡, H. Bae., P. Mane., J. Heo., C. Seong., J.H. Kim., J. Oh, J.-S. Ha. "Advances in gas diffusion electrode technology for electrochemical CO2 reduction: Innovations, challenges, and future directions". *Materials Science & Engineering R 166 (2025) 101064*.
- D. Kim.‡, H. Choi.‡, H. Lee., E. An., Y. Kim., Y. Kwon., J. Oh. "Integration of biomass valorization and bicarbonate electrolysis for low-voltage production of value-added chemicals". *Appl. Surf. Sci. Adv. 2025, 28, 100798*.
- Y. Jung.‡, J. Lee., J. Jun., J. Yang., I. Oh., S. Seo., H. Yoon., J. Woo., B.-U. Choi., S. Ryu., J. Oh., S. Lee\*. "Highly (211)-Oriented CuBi2O4/TiO2 Heterojunction for Bifunctional Photoelectrochemical Water Splitting". *Solar RRL, 2025, 9, 15*.
- J.Suh.‡, J.Lee.‡, J.Kim., M.Cho., J.Kim., J.M.Oh., H.Han., H.S.Lee., J.Oh.\*. "High Aspect Ratio Silicon Nanohole Arrays via Electric-Field-Incorporated Metal-Assisted Chemical Etching". *ACS Appl. Mater. Interfaces 2025, 17, 21, 31212–31220 (Highlighted on Supplementary Cover)*.

**2024**

- J. Suh.‡, H. Choi.‡, Y. Kong., J. Oh.\*. "Tandem Electroreduction of Nitrate to Ammonia Using a Cobalt–Copper Mixed Single-Atom/Cluster Catalyst with Synergistic Effects". *Adv. Sci. 2024, 11, 2407250*.
- T. H. Ha‡, J. Kim.‡, H.Choi, and J. Oh\*. "Selective Zero-Gap CO2 Reduction in Acid". *ACS Energy Lett. 2024, 9, 10, 4835−4842 (Highlighted on Supplementary Cover)*.
- S.Wang.‡, H.D. Jung‡, H.Choi., J.Kim., S.Back.\*, J.Oh.\*. "Delicate control of a gold-copper oxide tandem structure enables the efficient production of high-value chemicals by electrochemical carbon dioxide reduction". *Nano Energy 130 (2024) 110176*.
- H. Choi.‡, M. G. Ha.‡, J. Suh., C. Lim., B. Kim., S. E. Wang., J. Y. Lee., H.-S. Oh.\*, J. Oh.\*. "Effect of the nitrogen/carbon ratio in the organic ligand of a nickel single-atom catalyst on its electrochemical activity in CO2 reduction". *Applied Catalysis B: Environment and Energy 355 (2024) 124192*.
- D. Kim.‡, C. D. Van.‡, M. S. Lee., M. Kim.\*, M. H. Lee.\*, and J. Oh.\*. "Selective Formic Acid Production in Ni and NiFe Layered Hydroxides via Glycerol Electro-Oxidation". *ACS Catal. 2024, 14, 10, 7717–7725*.
- H. Song.‡, C. A. Fernández.‡, H. Choi.‡, P.-W. Huang., J. Oh., and M. C. Hatzell. "Integrated carbon capture and CO production from bicarbonates through bipolar membrane electrolysis". *Energy Environ. Sci., 2024, Advance Article*.
- S. Hong., K. K. Patra., J. Oh.\*. "Morphology Evolution of CuO Supported on CeO2 and Its Role in Electrochemical CO2 Reduction". *JOM (2024)*.

**2023**

- J. Lee., B. Kim., C. Kim., M.-H. Lee., I. Kozakci., S. Cho., B. Kim., S. Y. Lee., J. Kim., J. Oh., and J.-Y. Lee.\*. "Unlocking the Potential of Colloidal Quantum Dot/Organic Hybrid Solar Cells: Band Tunable Interfacial Layer Approach". *ACS Appl. Mater. Interfaces 2023, 15, 33, 39408–39416*.
- J. Kim., S. Lee., S. Kim., C.-Y. Park., J. Kim., K. B. Lee, J. Oh., and J. Lee.\*. "Anode-less Hybrid Na−CO2 Battery with Sodium Harvesting from Seawater for Both Electricity Storage and Various Chemical Production". *ACS Energy Lett. 2023, 8, 12, 5079–5087*.
- J. Kim.‡, T. H. Ha‡, J. Kim.‡, G. H. Jeong., S. O. Kim, W. Chung., K. Roh.\*, J. H. Lee\*, and J. Oh\*. "Design principles for selective and economical CO2 electrolysis in acids". *Applied Catalysis B: Environmental 339 (2023) 123160*.
- B. Kim.‡, Y. C. Tan.‡, Y. Ryu.‡, K. Jang., H. G. Abbas., T. Kang., H. Choi., K.-S. Lee, S. Park, W. Kim, P.-P. Choi\*, S. Ringe\*, and J. Oh\*. "Trace-Level Cobalt Dopants Enhance CO2 Electroreduction and Ethylene Formation on Copper". *ACS Energy Letters, 2023, 8, 3356−3364 (Highlighted on Supplementary Cover)*.
- W. Zhang‡, J. W. Choi‡, S. Kim‡, T. T. Le, S. Nandy, C.-K. Hwang, S. Y. Paek, A. Byeon, K. H. Chae, S. Y. Lee, S. H. Kim, H. Song, J. Kim, J. Oh, J. W. Lee, S. S. Han\*, J. M. Kim\*. "Penta nitrogen coordinated cobalt single atom catalysts with oxygenated carbon black for electrochemical H2O2 production". *Applied Catalysis B: Environmental, 2023, 331, 122712*.
- Y. Kim., B. Kim., H. Choi., S. Kim., Y. Yun., J. Oh. "Modulating the electronic structure of Au using a heterostructure for efficient electrochemical CO2 reduction". *Chemical Engineering Journal, 461, 142126*.

**2022**

- S. Hong‡, H. G. Abbas‡, K. Jang‡, K. K. Patra, B. Kim, B.-U. Choi, H. Song, K.-S. Lee, P.-P Choi\*, S. Ringe\*, J. Oh\*. "Tuning the C1/C2 Selectivity of Electrochemical CO2 Reduction on Cu-CeO2 Nanorods by Oxidation State Control". *Advanced Material, 2023, 35, 8 (Highlighted on Front Cover)*.
- Y. E. Kim, W. Lee, Y. N. Ko, J. E. Park, D. Tan, J. Hong, Y. E. Jeon, J. Oh,\* and K. T. Park\*. "Role of Binder in Cu2O Gas Diffusion Electrodes for CO2 Reduction to C2+ Products". *ACS Sustainable Chem. Eng. 2022, 10, 11710−11718*.
- J. Lee, J. Oh\*. "Nanopixelated Cuprous Oxide Photocathodes for Durable Photoelectrochemical Water Splitting". *ACS Energy Lett. 2022, 7, 10, 3244–3250 (Highlighted on Supplementary Cover)*.
- K. K. Patra‡, Z. Liu‡, H. Lee‡, S. Hong, H. Song, H. G. Abbas, Y. Kwon\*, S. Ringe\*, J. Oh\*. "Boosting Electrochemical CO2 Reduction to Methane via Tuning Oxygen Vacancy Concentration and Surface Termination on a Copper/Ceria Catalyst". *ACS Catal. (2022) 12, 17, 10973-10893*.
- Nam Woon Kim, Hyunung Yu\*, Jihun Oh\*. "Mesoporous K-doped NiCo2O4 derived from a Prussian blue analog: high-yielding synthesis and assessment as oxygen evolution reaction catalyst". *RSC Advances (2022) 12, 12371-12376*.
- Ying Chuan Tan, Wei Kang Quek, Beomil Kim, Sigit Sugiarto, Jihun Oh\*, and Dan Kai\*. "Pitfalls and Protocols: Evaluating Catalysts for CO2 Reduction in Electrolyzers Based on Gas Diffusion Electrodes". *ACS Energy Letters (2022) 7, 6, 2012–2023*.
- Yonghwan Lee, Bikesh Gupta, Hark Hoe Tan, Chennupati Jagadish, Jihun Oh, Siva Karuturi\*. "Ultrathin transparent metal capping layer on metal oxide carrier-selective contacts for Si solar cells". *The European Physical Journal Special Topics (2022)*.
- Yeji Baek‡, Hakhyeon Song‡, Deokgi Hong‡, Suneon Wang, Sungwoo Lee, Young-Chang Joo\*, Gun-Do Lee\*, and Jihun Oh\*. "Electrochemical Carbon Dioxide Reduction on Copper-Zinc Alloys: Ethanol and Ethylene Selectivity Analysis". *Journal of Materials Chemistry A (2022) 10, 9393 (Highlighted on Back Cover)*.
- Yonghwan Lee, Bikesh Gupta, Hark H Tan, Chennupati Jagadish, Jihun Oh, Siva Karuturi\*. "Protocol on the fabrication of monocrystalline thin semiconductor via crack-assisted layer exfoliation technique for photoelectrochemical water-splitting". *STAR Protocols (2022) Volume 3, Issue 1, 101015*.
- Rohini Subhash Kanase, Kelvin Berm Lee, Maheswari Arunachalam, Ramesh Poonchi Sivasankaran, Jihun Oh, Soon Hyung Kang\*. "Nanostructure engineering of Cu electrocatalyst for the selective C2+ hydrocarbons in electrochemical CO2 reduction". *Applied Surface Science (2022) Volume 584, 152518*.

**2021**

- J.-E. Hong, Y. Lee, S.-I. Mo, H.-S. Jeong, J.-H. An, H.-E. Song, J. Oh, J. Bang, J.-H. Oh, K.-H. Kim\*. "Epitaxial growth of crystalline silicon wafer using a self-releasing seed layer". *AFORE (2021) 10th Asia-Pacific Forum on Renewable Energy*.
- D. Kim, L. S. Oh, Y. C. Tan, H. Song, H. J. Kim\*, and J. Oh\*. "Enhancing Glycerol Conversion and Selectivity toward Glycolic Acid via Precise Nanostructuring of Electrocatalysts". *ACS Catalysis (2021) 11, 24, 14926–14931 (Highlighted on Supplementary Cover)*.
- H. Song, Y. C. Tan, B. Kim, S. Ringe, J. Oh. "Tunable Product Selectivity in Electrochemical CO2 Reduction on Well-Mixed Ni–Cu Alloys". *ACS Applied Materials & Interfaces (2021) 13, 46, 55272–55280*.
- J.-E. Hong, Y. Lee, S.-I. Mo, H.-S. Jeong, J.-H. An, H.-E. Song, J. Oh, J. Bang, J.-H. Oh\*, K.-H. Kim\*. "Fully Bottom-Up Waste-Free Growth of Ultrathin Silicon Wafer via Self-Releasing Seed Layer". *Advanced Materials 2103708 (2021) (Highlighted on Back Cover)*.
- Y. H. Lee, B. Gupta, H. H. Tan, C. Jagadish, J. Oh, S. Karuturi\*. "Thin silicon via crack-assisted layer exfoliation for photoelectrochemical water splitting". *iScience 24, 102921, August 20, (2021)*.
- G. H. Jeong‡, Y. C. Tan‡, J. T. Song, G.-Y. Lee, H. J. Lee, J. Lim, H. Y. Jeong, S. Won, Jihun Oh\*, Sang Ouk Kim\*. "Synthetic multiscale design of nanostructured Ni single atom catalyst for superior CO2 electroreduction". *Chemical Engineering Journal vol 426, 131063, (2021)*.
- J.-Y. Kim, D. Hong, J.-C. Lee, H. G. Kim, S. Lee, S. Shin, B. Kim, H. Lee, M. Kim, J. Oh, G.-D. Lee\*, D.-H. Nam\*, Y.-C. Joo\*. "Quasi-graphitic carbon shell-induced Cu confinement promotes electrocatalytic CO2 reduction toward C2+ products". *Nature communications volume 12 (1), 1-11 (2021)*.
- B.-U. Choi‡, Y. C. Tan‡, H. Song, K. B. Lee, and J. Oh\*. "System Design Considerations for Enhancing Electroproduction of Formate from Simulated Flue Gas". *ACS Sustainable Chemistry & Engineering, (2021)*.

## 특허

랩 Patent 게시판의 2021년 이후 특허다. 등록·출원 상태는 랩 표기다.[^patents]

- 2026 · 단일 원자 촉매 제조방법 및 이에 의해 제조된 단일 원자촉매 (발명자 J. Oh, H. Choi, J. Nam; 번호 KR Patent, 10-2992680; 상태 등록)
- 2026 · 니켈 붕화물 촉매 합성 및 촉매 기반 전기화학적 피셔-트롭쉬 반응 (발명자 J. Oh, B. Suh; 번호 KR Patent, 10-2026-0108671; 상태 출원)
- 2026 · 수소 양이온 공급제가 도입된 이산화탄소 전환용 전기화학셀 (발명자 J. Oh, T. Ha, J. Kim; 번호 KR Patent, 10-2026-0087993; 상태 출원)
- 2026 · 전기 이중층 제어를 통한 전기화학적 CO2 환원 반응의 알코올 선택도 및 안정성 향상 기술 (발명자 J. Oh, Y. Kim, S. Lee, S. Wang; 번호 KR Patent, 10-2026-0047199; 상태 출원)
- 2026 · 역구조 구리-세륨산화물 촉매 및 이를 이용한 암모니아 제조 방법 (발명자 J. Oh, Y. Kong; 번호 KR Patent, 10-2026-0011409; 상태 출원)
- 2026 · 암모니아/수소 생산을 위한 에너지 자립형 전기화학 시스템 (발명자 J. Oh, J. Suh; 번호 KR Patent, 10-2026-0023956; 상태 출원)
- 2026 · 암모니아 합성 시스템 및 이를 이용한 암모니아 합성 방법 (발명자 J. Oh, H. Lee; 번호 KR Patent, 10-2026-0034315; 상태 출원)
- 2025 · 이산화탄소 환원용 막전극 접합체 및 이의 제조방법 (발명자 J. Oh, T. Ha; 번호 KR Patent, 10-2025-0200446; 상태 출원)
- 2025 · 전기화학적 이산화탄소 환원용 촉매 및 이의 제조방법 (발명자 J. Oh, B. Kim; 번호 KR Patent, 10-2799797; 상태 등록)
- 2024 · 광전기화학전지용 전극, 이의 제조방법 및 이를 포함하는 광전기화학전지 (발명자 J. Oh., J. Lee; 번호 KR patent, 10-2701306; 상태 등록)
- 2024 · Concurrent conversion system for carbonate and biomass, and concurrent conversion method using the same (발명자 J. Oh., H. Choi., E. An., D. Kim.; 번호 KR Patent, 10-2024-0029845; 상태 출원)
- 2024 · Electrochemical cell (발명자 J. Oh., Y. Kim., H. Choi., K. H. Kim., T. G. Noh., S. Kim., Y. Han., H. Lim.; 번호 KR Patent, 10-2024-0010272; 상태 출원)
- 2024 · Carbon dioxide reduction membrane electrode assembly and manufacturing method thereof (발명자 T. H. Ha, J. H. Kim, 10-2024-0032802; 상태 출원)
- 2023 · Manufacturing method of single atom catalyst and the single atom catalyst manufactured by the method (발명자 J. Oh., H. Choi., J. Nam; 번호 10-2023-0000683; 상태 출원)
- 2022 · Electrode for photoelectrochemical cell, method of manufacturing the same and photoelectrochemical cell comprising the same (발명자 J. Oh., J. Lee.; 번호 Korea Patent Application, No. 10-2022-0052239, Korea)
- 2022 · Efficient black silicon photovoltaic devices with enhanced blue response (발명자 J. Oh, H. M. Branz, H.-C. Yuan; 번호 US20220123158A1)
- 2021 · Reduction apparatus of carbon dioxide and reducing method of carbon dioxide using the same (발명자 J. Oh, B. Kim, J. Kim, D. Lee, H.-E. Song, K. Kwak; 번호 Korea Patent Application, No. 10-2304316, Korea; 상태 등록)

## 소식

랩 News 게시판의 소식이다.[^news]

- 2026-08-12 · Nano Korea 2026 컨퍼런스 김소은 박사과정 학생 Best Poster Awards 수상
- 2026-05-14 · 2026년도 한국전기화학회 춘계총회 및 학술발표회 서정원, 안은의 박사과정 학생 대상, 우수상 수상
- 2026-04-27 · 왕순언 박사과정 학생의 논문이 출판되었습니다!
- 2026-04-13 · 최현욱 박사후연구원의 장영실 펠로우 프로그램 선정을 축하합니다!
- 2026-04-13 · 최현욱 박사후연구원의 논문이 출판되었습니다!
- 2026-02-09 · 공유진 박사과정 학생의 논문이 출판되었습니다!
- 2026-02-09 · 정유진 졸업생, 김소은 박사과정 학생, 김범일 졸업생의 논문이 출판되었습니다!
- 2025-07-09 · 김도희 졸업생, 최현욱 박사과정 학생의 논문이 출판되었습니다!
- 2025-07-09 · 최현욱 박사과정 학생의 특허 기술 이전을 축하합니다!
- 2025-07-07 · Nano Korea 2025 컨퍼런스 하태현 박사과정 학생, Best Poster Awards 수상
- 2025-05-12 · 서정원 박사과정 학생의 논문 Accept과 Supplementary journal cover 선정을 축하합니다!
- 2025-05-09 · 2025년도 대한금속재료학회 춘계학술대회 하태현, 서정원 박사과정 학생, 구두 발표 우수상 수상
- 2025-01-14 · 신소재공학과 BK21 사업, 최현욱 박사과정 학생 우수 연구포상
- 2024-09-11 · MCARE 2024 서정원 박사과정 학생, Bronze Poster Award 수상
- 2024-09-11 · 서정원 박사과정 학생의 논문 Accept을 축하합니다!
- 2024-09-04 · 하태현 박사과정 학생의 논문이 Accept 및 Supplementary journal cover로 선정되었습니다!
- 2024-09-04 · 왕순언 박사과정 학생의 논문이 출판되었습니다!
- 2024-05-29 · 김도희 박사 과정 학생의 디펜스 통과를 축하드립니다!
- 2024-05-29 · 2024 한국전기화학회 김도희 박사과정 학생, 우수 포스터상 수상
- 2024-05-29 · 최현욱 박사과정 학생의 논문이 출판되었습니다!
- 2024-05-29 · 김도희 박사과정 학생의 논문이 출판되었습니다!
- 2024-05-29 · 송학현 박사&최현욱 박사과정 학생의 논문이 출판되었습니다!

## 연락과 위치

- 교수실: KAIST W1-1 2406호[^prof]
- 연구실: KAIST W8(교육지원동) 1112호[^contact]
- 교수 이메일: jihun.oh@kaist.ac.kr[^prof]

[^home]: LE&S 누리집 첫 화면 <https://les.kaist.ac.kr/> (2026-10-20 열람)
[^research]: LE&S Research 페이지(이산화탄소 환원, 질산염 환원, 바이오매스 고부가화, AI 기반 전기화학 연구) <https://les.kaist.ac.kr/sub1_1.php>, /sub1_2.php, /sub1_3.php, /sub1_4.php (2026-10-20 열람)
[^prof]: LE&S Professor 페이지 <https://les.kaist.ac.kr/sub2_1.php> (2026-10-20 열람)
[^members]: LE&S Member 게시판 <https://les.kaist.ac.kr/bbs/board.php?bo_table=sub2_2> (2026-10-20 열람)
[^alumni]: LE&S Alumni 게시판 <https://les.kaist.ac.kr/bbs/board.php?bo_table=sub2_3> (2026-10-20 열람)
[^papers]: LE&S Journals 게시판 1–4쪽 <https://les.kaist.ac.kr/bbs/board.php?bo_table=sub3_1> (2026-10-20 열람)
[^patents]: LE&S Patent 게시판과 특허별 상세 페이지 <https://les.kaist.ac.kr/bbs/board.php?bo_table=sub3_2> (2026-10-20 열람)
[^news]: LE&S News 게시판 1–2쪽 <https://les.kaist.ac.kr/bbs/board.php?bo_table=sub4_1> (2026-10-20 열람)
[^contact]: LE&S Contact 페이지 <https://les.kaist.ac.kr/sub5_1.php> (2026-10-20 열람)
[^p1]: B. Kim 외, J. Oh, Nature Catalysis 9, 471-481 (온라인 2026-04-13). <https://doi.org/10.1038/s41929-026-01526-7> 초록 기준(출판사 논문 페이지).
[^p2]: Y. Jung 외, J. Oh, Journal of the American Chemical Society 147, 39796-39804 (온라인 2025-10-20). <https://doi.org/10.1021/jacs.5c14093> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: S. Hong 외, J. Oh, Advanced Materials 35, 2208996 (온라인 2022-12-20). <https://doi.org/10.1002/adma.202208996> 초록 기준.
[^p4]: Y. Baek 외, J. Oh, Journal of Materials Chemistry A 10, 9393-9401 (2022). <https://doi.org/10.1039/d1ta10345h> 초록 기준.
[^p5]: P.-W. Huang 외, M. C. Hatzell, Energy & Environmental Science 19, 2658-2667 (2026). <https://doi.org/10.1039/d5ee07845h> 초록 기준.
[^p6]: J. Suh, H. Choi, Y. Kong, J. Oh, Advanced Science 11, 2407250 (온라인 2024-09-19). <https://doi.org/10.1002/advs.202407250> 초록 기준.

# Multiscale Biomedical Engineering Laboratory (MBEL)

**서울대학교 공과대학 기계공학부 · 전누리 교수**

- 분야: 장기 칩, 미세유체 기반 세포 배양 장치, 미세제작과 생물 영상 분석
- 대분야: 기계·로봇·제조, 화학공정·바이오공학
- 태그: 미세유체[^organ][^micro], 장기 칩·체외 질병 모델[^organ], 생체재료·조직 공학[^micro], 생물 영상 분석[^analysis]
- 홈페이지: <https://mbel.snu.ac.kr/>
- 근거와 출처: [MBEL 근거 페이지](mbel-sources.md)

> 몸 밖에서 세포와 혈관을 함께 키우는 장치를 만들고, 액체를 원하는 자리에 배치하는 제작 기술과 살아 있는 세포의 변화를 읽는 영상 분석법을 연구한다.[^organ][^micro][^analysis]

## 무엇을 연구하나

MBEL은 전누리 교수가 이끄는 연구실로, 기계공학의 설계·제작 방법을 생체 실험에 연결한다. 중심 대상은 장기 칩이다. 장기 칩은 세포(생명체의 구조와 기능을 이루는 기본 단위)를 칩 안에서 키워 장기 기능의 일부를 몸 밖에서 재현한 모형이다. 연구실은 이를 통해 미세생리시스템(Microphysiological System, MPS, 세포와 조직의 일부 생리 기능을 몸 밖에서 재현하는 실험계)을 만든다. 혈관이 있는 종양 모형, 면역 반응 모형, 신경 조직 모형, 공기와 액체가 만나는 조직 모형을 개발한다.[^research][^organ]

첫째 축은 **세포가 놓이는 자리와 주변 흐름을 설계하는 일**이다. 세포 배양(세포가 자랄 수 있는 환경을 몸 밖에서 유지하는 일)에 미세유체(가는 통로 안에서 적은 양의 액체를 다루는 기술)를 이용한다. 세포와 하이드로젤(물과 친화적인 긴 사슬 물질의 그물 구조가 물을 머금은 젤)을 정해진 위치에 놓고, 서로 다른 세포 집단 사이에 혈관이 형성되도록 한다. 혈관을 이루는 세포, 주변 조직을 지지하는 세포, 암세포를 함께 배치해 약물 반응과 혈관 변화를 살핀다. 면역세포가 종양과 만나는 과정을 재현하는 배양 모형도 개발한다.[^organ]

둘째 축은 **장치를 반복해서 만들고 같은 조건으로 실험하는 제작 기술**이다. 연구실은 사출성형(유동성 있는 재료를 압력으로 틀 안에 주입한 뒤 굳혀 제품을 만드는 제조 방법), 입체 프린팅(Three-dimensional Printing, 재료를 층별로 쌓아 입체 물체를 만드는 방법), 전기방사(전기적 힘을 이용해 액체 재료를 가는 섬유로 뽑는 방법)를 다룬다. 세포·조직과 맞닿아 쓰는 섬유막을 개발하고, 막의 기계적 강도와 물질 통과 특성을 조절하려 한다. 입체 프린팅과 미세구조를 이용해 배양 장치의 형상을 설계하는 것도 주요 갈래다.[^micro]

셋째 축은 **세포와 혈관의 변화를 영상에서 정량화하는 일**이다. 연구실은 컴퓨터 비전(사진과 영상에서 대상이나 구조를 찾아 정보를 얻는 기술)과 딥러닝(여러 층의 신경망을 통해 자료의 표현을 단계적으로 학습하는 기계학습 분야)을 이용한 생물 영상 분석을 연구한다. 신경망은 서로 연결된 계산 단위들이 입력을 변환하며 결과를 만드는 학습 모형이다. 기계학습은 자료에서 규칙을 학습해 새 자료를 분석하거나 예측하는 계산 방법이다. 가상 염색(계산으로 영상에 염색된 모습에 해당하는 정보를 만드는 방법), 살아 있는 세포의 이동·형태 추적, 여러 초점의 평면 영상에서 입체 구조를 재구성하는 방법을 다룬다. 세포를 고정해 활동을 멈추는 과정 없이 시간에 따른 변화를 관찰하는 것이 한 목표다.[^analysis]

## 주요 연구 주제

### 혈관을 포함한 조직·면역 모형

연구실은 혈관이 들어 있는 종양 미세환경(종양과 주변 세포·물질·물리 조건이 이루는 국소 환경)을 칩에 재현한다. 혈관을 통한 물질 이동과 면역세포의 움직임을 함께 살펴 약물 반응을 평가하는 실험계를 개발한다. 신경 조직과 폐·장·피부처럼 공기 또는 액체와 맞닿는 조직도 대상으로 든다.[^organ] 대표 논문 2는 면역 기능을 갖춘 미세생리시스템을 설계할 때 필요한 세포 구성, 세포 위치, 액체 흐름, 주변 재료가 힘을 받을 때 변형되는 성질을 정리한 리뷰다.[^p2]

정적인 배양뿐 아니라 조직 사이를 지나는 액체 흐름도 제어한다. 대표 논문 4의 Flow-IMPACT는 구불구불한 통로와 배양액 높이, 젤 농도를 이용해 외부 펌프 없이 흐름을 조절하는 사출성형 장치다. 초록은 흐름이 혈관 길이와 가지 형성, 새 혈관의 방향에 미치는 영향을 분석했다고 설명한다.[^p4]

### 액체 배치와 장기 칩의 제작

연구실은 미세통로 안에 세포를 담은 재료를 배치하는 방법과 장치의 제조 방식을 함께 연구한다.[^micro] 대표 논문 1은 모세관 현상(액체와 표면 사이의 힘으로 좁은 틈에서 액체가 이동하거나 머무는 현상)을 이용한 하이드로젤 배치 방법을 분석한다. 폐쇄형·반개방형·개방형 미세유체 장치에서 재료를 놓는 원리와 각 방법의 장점을 정리했다.[^p1]

대표 논문 6의 U-IMPACT는 여러 세포와 세포 덩어리를 같은 형식의 장치에서 배양하는 범용 칩이다. 표면과 액체가 만나는 성질을 이용해 재료를 선택적으로 배치하는 새 방법을 제시했다.[^p6] 대표 논문 7은 빛을 이용한 입체 프린팅으로 만든 그물 구조에 하이드로젤을 차례로 배치하는 방법이다. 그물의 크기와 형상에 따라 액체가 경계를 넘어가는 압력이 어떻게 달라지는지 계산과 실험으로 분석했다.[^p7]

### 혈관 영상과 세포 내부 움직임의 정량 분석

연구실은 생물 구조를 영상으로 찾아내고 측정하는 분석 방법을 개발한다.[^analysis] 대표 논문 5의 Angio-Net은 명시야 영상(시료를 통과하거나 반사된 조명광이 밝은 배경을 이루고, 시료와 배경의 밝기 차이로 대상을 구분하는 영상)을 가상 형광 영상으로 바꾼다. 형광은 물질이 빛을 흡수한 뒤 빛을 내며 자극이 사라지면 발광도 곧 사라지는 현상이다. 이 방법은 실제 형광 표지를 붙이는 과정을 대신하면서 혈관의 형태를 자동으로 측정하도록 설계되었다.[^p5]

정상 세포의 작동 원리를 관찰하는 연구도 있다. 대표 논문 8은 신경세포의 축삭(다른 세포 쪽으로 신호를 전달하는 길게 뻗은 부분)에서 베타액틴(세포 내부 구조와 움직임에 관여하는 섬유를 이루는 단백질)의 제작 정보를 담은 물질이 어떻게 이동하고 자리를 잡는지 추적했다. 세포 안의 액틴 섬유망이 그 물질의 위치 조절을 돕는다는 결과를 제시하고, 신경세포 가지 형성과의 연관 가능성을 설명했다.[^p8]

### 유연한 이식형 약물 이송 장치

대표 논문 3은 유연한 필름 탐침(대상에 넣거나 접촉해 자극·측정·물질 전달을 수행하는 기구)에 섬유를 넣은 미세 이송 통로를 통합했다. 섬유 다발 주변 틈과 섬유 내부의 모세관 이동을 이용해 액체를 전달하고, 전기 자극·기록 기능과 약물 전달 기능을 결합한다. 가열해 재료를 붙이는 공정을 개발했으며, 동물 뇌에 넣은 장치에서 화학물질 전달을 실험으로 보였다.[^p3]

## 대표 논문

서울대 재직 시기의 논문 중 장기 칩의 설계·제작, 동적 배양, 영상 분석, 유연한 이송 장치, 정상 세포의 정량 관찰을 고르게 골랐다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2026 | [From flow to form: structuring and patterning hydrogels using microfluidic approaches](https://doi.org/10.1039/d6lc00386a)[^p1] | 좁은 통로의 모세관 흐름으로 세포 배양용 젤을 원하는 위치에 놓는 방법을 정리한 리뷰다. 액체가 경계에서 멈추는 현상과 흡인을 이용한 배치를 설명하고, 폐쇄형·반개방형·개방형 장치에 적용되는 방법을 분석했다. |
| 2 | 2026 | [Immune Microphysiological Systems for Human Innate Immunity](https://doi.org/10.1002/admt.71051)[^p2] | 몸 밖에서 면역 기능을 재현하는 장치의 설계 조건을 정리한 리뷰다. 세포의 위치, 흐름, 세포를 유도하는 물질의 농도 변화, 주변 재료의 성질을 제어하는 전략과 각 면역세포를 다루는 응용을 설명한다. |
| 3 | 2025 | [Targeted Local Delivery via Fiber-Embedded Flexible Microchannels Integrated with Film-Based Implantable Probes](https://doi.org/10.1002/admt.202401470)[^p3] | 섬유를 넣은 미세 통로를 유연한 탐침에 함께 만들어 전기 자극·기록과 국소 약물 전달을 결합했다. 가열 접합 공정으로 장치를 제작하고, 액체 전달 특성과 동물 뇌에서의 전달을 확인했다. |
| 4 | 2025 | [Flow-IMPACT: A Pumpless, High-Throughput 3D Cell Culture Platform for Investigation of Synergistic Angiogenic Effects](https://doi.org/10.1002/admt.202401526)[^p4] | 외부 펌프 없이 조직 사이 액체 흐름을 조절하는 입체 배양 장치다. 통로의 유동 저항과 젤 농도, 배양액 높이를 이용해 흐름을 제어하고 혈관 형성에 미치는 영향을 분석했다. |
| 5 | 2024 | [Angio-Net: deep learning-based label-free detection and morphometric analysis of in vitro angiogenesis](https://doi.org/10.1039/d3lc00935a)[^p5] | 일반적인 밝기 영상에서 가상 형광 영상을 만들고 혈관 형태를 자동으로 측정하는 방법이다. 세포를 고정하거나 실제 형광 표지를 붙이지 않고 혈관 형성을 정량 분석하도록 설계했다. |
| 6 | 2022 | [U-IMPACT: a universal 3D microfluidic cell culture platform](https://doi.org/10.1038/s41378-022-00431-w)[^p6] | 여러 종류의 세포·세포 덩어리·혈관 조직을 같은 형식으로 배양하는 사출성형 장치다. 모세관 작용과 재료 표면의 성질을 이용하는 새 배치 방법을 개발하고 종양 환경과 신경세포 덩어리의 배양을 보였다. |
| 7 | 2022 | [3D micromesh-based hybrid bioprinting: multidimensional liquid patterning for 3D microtissue engineering](https://doi.org/10.1038/s41427-022-00355-x)[^p7] | 입체 그물 구조에 세포를 담은 젤을 순서대로 배치하는 프린팅 방법이다. 그물 크기와 모양에 따른 액체 경계의 압력 조건을 분석해 설계 규칙을 세우고 혈관이 있는 종양 세포 덩어리를 만들었다. |
| 8 | 2022 | [Dynamics of axonal β-actin mRNA in live hippocampal neurons](https://doi.org/10.1111/tra.12865)[^p8] | 살아 있는 신경세포에서 베타액틴 단백질의 제작 정보를 담은 물질의 움직임을 추적했다. 이동하던 물질이 액틴이 밀집한 영역에 머무는 경향을 관찰해, 세포 내부 망이 그 위치 조절을 돕는다는 결과를 제시했다. |

## 교수와 전문 분야

전누리 교수는 Northwestern University에서 재료공학 학사(1991), University of Illinois, Urbana-Champaign에서 재료공학 박사(1997)를 받았다. Harvard University 화학과와 Harvard Medical School에서 박사후연구원으로 일했고, University of California, Irvine에서 조교수·부교수로 재직했다. 연구실 교수 소개는 서울대학교 기계공학 부교수 재직을 2009–2012년, 교수 재직을 2013년부터로 적는다.[^prof]

학과는 연구 분야를 의기계 임플란트(몸 안에 넣어 기능을 보조하거나 대체하는 공학 장치), 바이오멤스(미세한 기계 구조와 전기적 기능을 결합해 생물학적 대상을 다루는 장치), 미세 유체공학으로 소개한다.[^dept] 연구실 소개와 최근 논문으로 보면, 여러 세포가 함께 자라는 체외 실험계의 설계, 미세유체 장치의 제작과 액체 배치, 생물 영상의 정량 분석이 전문 분야다.[^micro][^analysis][^p4][^p5][^p6]

## 응용 분야

연구실은 혈관을 포함한 종양 모형과 면역 반응 모형을 이용한 약물 평가, 신경 질환과 손상 모형, 폐·장·피부 모형을 응용 대상으로 든다. 환자별 종양 환경의 차이를 반영하는 실험계와 반복 실험이 가능한 장기 칩의 개발을 목표로 한다.[^organ] 대표 논문은 배양 장치 제조와 혈관 영상 분석 외에, 이식형 장치에서의 국소 약물 전달과 정상 신경세포 내부의 물질 이동도 다룬다.[^p3][^p5][^p8]

## 구성원

2026년 11월 7일 연구실이 현재 구성원으로 게시한 21명이다. 연구교수 2명, 박사후연구원 2명, 연구원 1명, 박사과정 12명, 석사과정 4명이며 과정·직위와 학교 이메일은 랩의 게시 표기를 따른다. ‘대표 논문 참여’는 위 논문 표의 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| 강민진 (Minjin Kang) | 연구교수 | kmj1210@snu.ac.kr |  |
| 오영선 (Yeong Seon Oh) | 연구교수 |  |  |
| Shruthy Kuttappan | 박사후연구원 |  |  |
| Stefania Martini | 박사후연구원 | martinis@snu.ac.kr |  |
| 김선기 (Seon Kim) | 연구원 |  |  |
| 김솔빈 (Solbin Kim) | 박사과정 | solbin28@snu.ac.kr |  |
| 김솔희 (Solhee Kim) | 박사과정 | sol_ution@snu.ac.kr |  |
| 김애련 (Ailian Jin) | 박사과정 | arkim95@snu.ac.kr |  |
| 김해윤 (Hae-Yoon Kim) | 박사과정 | khaeyoon1998@snu.ac.kr |  |
| 박승혁 (Seonghyuk Park) | 박사과정 |  | 4, 5, 6, 7 |
| 이영균 (Younggyun Lee) | 박사과정 |  |  |
| 이유진 (Yujin Lee) | 박사과정 | yj_lee@snu.ac.kr |  |
| 정성훈 (Sunghun Cheong) | 박사과정 | shcheong@snu.ac.kr |  |
| 조윤경 (Yunkyeong Cho) | 박사과정 | whdbsrud1216@snu.ac.kr |  |
| 조현수 (Hyeonsu Jo) | 박사과정 |  |  |
| 최선빈 (Sunbeen Choi) | 박사과정 | sunbeen116@snu.ac.kr | 5 |
| 최혜리 (Hyeri Choi) | 박사과정 | hchoi615@snu.ac.kr | 2 |
| 김범주 (Beomjoo Kim) | 석사과정 |  |  |
| 신윤찬 (Yunchan Shin) | 석사과정 | yunchan1006@snu.ac.kr |  |
| 이재은 (Jae Eun Lee) | 석사과정 | jeun.lee@snu.ac.kr |  |
| 이재준 (Jaejune Lee) | 석사과정 | aktnfths1106@snu.ac.kr |  |

## 졸업생 진로

연구실이 졸업생으로 게시한 55명의 학위·연도·진로·학위 논문이다. 연도는 2010–2026년이며 진로는 랩이 게시한 시점의 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Yerim, Park | M.S. (2026) |  |  |
| Dr. Sangmin Jung | Ph.D. (2026) |  |  |
| Goeun, Son | M.S. (2026) |  |  |
| Gaeun, Han | M.S. (2026) |  |  |
| Yoonho, Lee | M.S. (2026) |  |  |
| Mikang, Shim | M.S. (2025) |  |  |
| Taeseung, Lee | M.S. (2025) |  |  |
| Jongho, Hong | M.S. (2025) | Korean Air |  |
| Seon, Kim | M.S. (2025) | Histo Link |  |
| Dr. Jiho, Kim | Ph.D. (2025) | Qureator |  |
| Stephen, Rhee | M.S. (2023) | Boston Micro Fabrication(BMF) | 3D Microfluidic Skin-on-a-chip for Drug and Skin Cosmetics Screening |
| Sofia, Madrigal Gamboa | M.S. (2022) |  | Microfluidic Platform With Suspended Biological Membranes For Tissue Barriers-on-Chips Applications |
| Dr. Jungeun, Lim | Ph.D. (2022) | Post Doc. at University of California San Diego(UCSD) | Engineering a Brain Tumor Microenvironment with Controlled Physical Features |
| Dr. Suryong, Kim | Ph.D. (2022) | QUREATOR | High-Throughput Vascularized Tumor Model and Image Analysis via Deep Learning |
| Dr. Youngtaek, Kim | Ph.D. (2022) | Korea Institute of Science and Technology(KIST) | All-in-One High-throughput Microfluidic Platform: From Spheroid Formation to Vasularized Spheroids |
| Tri Tho, NGUYEN | M.S. (2022) | INSTITUT PASTEUR | Development of an aspiration-based open microfluidic platform using micropillars to recreate the lung cellular microenvironment |
| Dr. Seung-Ryeol, Lee | Ph.D. (2021) | Samsung Electronics | Brain-in-a-Well: High-Throughput Microfluidic Platform for In Virtro Nervous System Model |
| Habin, Kang | M.S. (2021) | COSMAX | Reconstruction of 3D Human Lymphatic Vessel Network for Oncoimmunological Research |
| Dr. Jiyoung, Song | Ph.D. (2021) | Korea Institute of Science and Technology(KIST) | Microfluidic in vitro model of 3D Tumor Vascular Networks for Cancer Immunotherapy Screening |
| Dr. Jihoon, Ko | Ph.D. (2021) | Professor of Gachon University | Engineering of Vascularized Microtissue for Disease Modeling and Drug Screening |
| Dr. Somin, Lee | Ph.D. (2021) | Post Doc. at Harvard University | Modeling 3D Angiogenesis Using Microphysiological System for Preclinical Research |
| Dr. Dohyun, Park | Ph.D. (2020) | Post Doc. at Massachusetts Institute of Technology(MIT) | Capillarity Guided Patterning Based High-throughput 3D Immune Cell Cytotoxicity Assay |
| James, Yu | M.S. (2020) | University of Southern California | High Throughput 3D Vascular Assays on an injection molded Flow-induced Angiogenic Tissue Engineering (FATE) Platform |
| Dr. Jungho, Ahn | Ph.D. (2020) | Professor of Sungkyunkwan University | Microfluidic model of vascularized tumor microenvironment : PDMS and injection-molded plastic 3D culture platforms |
| Munseok, Choi | M.S. (2019) | MiCo BioMed | Development of isothermal digital PCR platform for quantification of circulating tumor DNA |
| Dr. Sang-Min, Paik | Ph.D. (2018) | GC LabCell | Biomass Enhancement in Chlamydomonas reinhardtii using Steady C/N Ratio Microfluidic Perfusion Bioreactor, Vibrational Stress Priming, and Malate Synthase Expression |
| Youngguyn, Lee | M.S. (2018) | Samsung Electronics | Injection-Molded Plastic Array for 3D Culture Tissue (IMPACT) Platform |
| Kyungmin, Son | M.S. (2018) | Ph.D. Candidate at SNU | Microfluidic In Vitro Model of Lymphatic Metastasis |
| Jungmin, Ha | M.S. (2018) | Ph.D. Candidate at Georgia Tech | Plastic Masters from 3D Printed Models for Microfluidics |
| Dr. Seokyoung, Bang | Ph.D. (2018) | Professor of Dongguk University | Brain-on-a-Chip: Neural Circuit and Blood-Brain Barrier on Microfluidic Platform |
| Dr. Byungjun, Lee | Ph.D. (2018) | QUREATOR | Multiscale design and fabrication of porous structure for multicellular co-culture system |
| Dr. Dongha, Tahk | Ph.D. (2018) | Post Doc. at Max Planck Institute | Engineering and Validation of Open Microfluidic Platform for Organ on a Chip |
| Dr. Kyungwon, Yun | Ph.D. (2018) | Samsung Electronics | Predicting Cellular Branching with Inverse Cellular Automata via Recurrent Neural Network |
| Dr. Norhana, Jusoh | Ph.D. (2018) | Professor at Universiti Teknologi Malaysia | Design and Validation of Vascularized Organ on Chip for Skin and Bone Toxicity Testing |
| Dr. Minhwan, Chung | Ph.D. (2017) | Post Doc. at Yale University | Eye on a Chip : Microfluidic In Vitro Model of Blood-Retinal Barrier |
| Dr. Sangcheol, Na | Ph.D. (2017) | Samsung Electronics | Novel microneedle design and fabrication for improved drug delivery |
| Dr. Soojung, Oh | Ph.D. (2016) | Amore Pacific | Design and applications of multiscale double-layered microfluidic device for multi-cellular co-culture |
| Dr. Hyunryul, Ryu | Ph.D. (2015) | Cepheid, Inc | Investigation of real-time single-cell MAPK kinetics using integrated platform with FRET biosensor and microfluidics |
| Dr. Hyunjae, Lee | Ph.D. (2015) | Samsung Electronics | Engineering of geometrically organized blood vessels for quantitative assays on a microfluidic chip |
| Dr. Jae Myung, Jang | Ph.D. (2015) | Korea Brain Research Institute(KBRI) | Optical activation of cultured neurons using ultra-short pulse laser |
| Dr. Jae Woo, Park | Ph.D. (2015) | Defense Agency for Technology and Quality | Microfluidic platform for quantitative characterization of biodiesel formation in microalgae |
| Dr. Minsung, Kim | Ph.D. (2015) | Samsung Electronics | Development of multiscale 2D/3D fabrication methods for tissue engineering |
| Dr. Myeongwoo, Kang | Ph.D. (2015) | Medytox Venture Investment | Capillarity Guided Patterning of Microliquids |
| Dr. Do Hyun, Kang | Ph.D. (2014) | Korea Institute of Machinery & Materials(KIMM) | Multiscale and bioinspired design of polydiacetylene-based biosensor systems |
| Dr. Sudong, Kim | Ph.D. (2014) | Post Doc. at Boston University | 미세환경 제어를 통한 혈관/림프관 생성 플랫폼의 개발과 응용 |
| Dr. Hong Nam, Kim | Ph.D. (2014) | Korea Institute of Science and Technology(KIST) | Engineering of cellular behaviors with multiscale surface patterns |
| Dr. Jae Hwan, Byun | Ph.D. (2014) | LG Display | Fiber-based pumpless flexible drug delivery system for implantable prosthesis |
| Dr. Won Gyu, Bae | Ph.D. (2014) | Professor at Soongsil University | Rational engineering of composite micro structures for advanced dry adhesion system |
| Thanh Qua, Nguyen | M.S. (2014) | Ph.D. Candidate at Seoultech | High-throughput microfluidic platform for real-time investigation of lipid droplet accumulation in microalgae |
| Woohyun, Park | M.S. (2014) | Ph.D. Candidate at Duke Univeristy | Rapid liquid patterning and biological applications |
| Jaerim, Kim | M.S. (2014) | Ph.D. Candidate at SNU | Engineering and characterization of pericyte covered blood vessel in vitro |
| Si Hoai Trung, Tran | M.S. (2014) | Ph.D. Candidate at LUND Univ. | Gel alignment in 3d microfluidic neuronal culture systems |
| Minseo, Kim | M.S. (2012) | Donghoon Investment | Engineering and characterization of pericyte covered blood vessel in vitro |
| Yekyung, Cho | M.S. (2011) | LG Household & Health Care | Multi-dimensional Patterning for Investigating Cell Motility |
| Qing Ping, Hu | M.S. (2010) |  | Microfluidic platform for investigating angiogenesis |

## 최근 5년 논문 목록

2021–2026년 구역 중 34편이다. 저자·제목·발표처·연도는 연구실 논문 상세의 표기를 따르고 DOI를 함께 적었다. bioRxiv에 게시된 항목은 사전 공개본으로 표시했다.[^journals]

**2026**

- Ailian Jin, Sang Wook Shim, Mikang Shim, Yoon Kyung Lee, Jongho Hong, Dahee Roh, Sujin Hyung\*, Seog Bae Oh\*, Noo Li Jeon\*. "A Microfluidic Cell Culture Platform for Modeling Aligned Peripheral Nerve Bundle, Connection, and Myelination". *Advanced Healthcare Materials · DOI: 10.1002/adhm.202504121[^a48]*.
- Sujin Kim, Yoonho Lee, Eunseo Park, Minseo Byeon, Hyeri Choi, Seokyoung Bang, Noo Li Jeon\*, Jihoon Ko\*. "Immune Microphysiological Systems for Human Innate Immunity". *Advanced Materials Technologies · DOI: 10.1002/admt.71051*.
- Jungseub Lee, Wooju Park, Sujin Hyung, Sangmin Jung, Kyungho Lee, Junseok Jeon, Noo Li Jeon\*, Jeeyun Lee\*, Hye Ryoun Jang\*, Jihoon Ko\*. "High-Throughput Digital Decoding of Vascular Heterogeneity in Patient-Specific Tumor Microenvironments". *Advanced Healthcare Materials · DOI: 10.1002/adhm.202505866[^a51]*.
- Harshita Sharma, Jungeun Lim, Woochan Kim, Yeon Ju Kim, Dream Kim, Shinyull Lee, Chaeyeon Park, Stephen Rhee, Shruthy Kuttapan, Jungho Ha, Sang Wook Park, Kyunghoon Kim, Noo Li Jeon, Sunho Park\*, Yun-Hoon Choung\*, Jangho Kim\*. "Engineering Pluripotent Stem Cells-Derived Inner Ear Organoids With Enhanced Maturation and Reproducibility by Micro-Topographical Cues". *Advanced Materials · DOI: 10.1002/adma.74560[^a52]*.
- Ella E. Bouker, Lauren G. Brown, Emilie Newsham Novak, Ariel Lin, Jamison M. Whitten, Asha R. Viswanathan, Laura A. Milton; M. Yunos Alizai, Siwan Park, Jungseub Lee, Liam A. Knudsen, Sophie R. Cook, Yi-Chin Toh, Jean Berthier, Amanda J. Haack, Noo Li Jeon\*, Erwin Berthier\*, Ashleigh B. Theberge\*. "From flow to form: structuring and patterning hydrogels using microfluidic approaches Open Access". *Lab on a chip · DOI: 10.1039/d6lc00386a*.
- Sebastian Naranjo, Madison E. Fletcher, Noo Li Jeon, Joyce Y. Wong\*, Catherine Klapperich\*. "A perfusable first-generation endometrial microvascular model to study human spiral artery remodeling in pregnancy". *Lab on a Chip · DOI: 10.1039/d6lc00513f[^a54]*.

**2025**

- Seonghyuk Park, Youngtaek Kim, Jungseub Lee, Sangmin Jung, Jongho Hong, Suryong Kim, Seung-Ryeol Lee, Jiyoung Song, Siwan Park, Young Sun Oh, Jihoon Ko, Noo Li Jeon\*. "Flow-IMPACT: A Pumpless, High-Throughput 3D Cell Culture Platform for Investigation of Synergistic Angiogenic Effects". *Advanced Materials Technologies, 2401526 · DOI: 10.1002/admt.202401526*.
- Dohyun Park, Inae Park, Bohwa Han, Yujin Baek, Dowon Moon, Noo Li Jeon\* and Junsang Doh\*. "Cytotoxic Chemotherapy in a 3D Microfluidic Device Induces Dendritic Cell Recruitment and Trogocytosis of Cancer Cells". *Cancer Immunology Research · DOI: 10.1158/2326-6066.cir-24-0263*.
- Shruthy Kuttappan, Sivashanmugam Amirthalingam, Perrine M’Pemba Hennebert, Yoonho Lee, Kyung Min Ryu, Arun Kumar Rajendran, Jung Hun Kim, Kyoung-Ha So, Nathaniel S Hwang\* and Noo Li Jeon\*. "Engineering a Whitlockite-Containing Macroporous Composite Cryogel with Silica Hybrid for Enhanced Vascularized Bone Regeneration". *ACS Applied Materials & Interfaces · DOI: 10.1021/acsami.4c20589*.
- Hyeonsu Jo, Somin Lee, Inae Park, Mikang Shim, James Yu, Young Sun Oh, Junsang Doh, Young-Kwon Hong, Noo Li Jeon. "A 3D Microfluidic Model of Initial Lymphatic Vessels for Investigating Dendritic Cell Chemotaxis Under Inflammatory Condition". *BioChip Journal · DOI: 10.1007/s13206-025-00227-w[^a46]*.
- Hyeongjin Ahn, Jaehong Min, Wooju Park, Sanghyeok Park, Younggyun Lee, Jungseub Lee, Wonsuk Shin, Noo Li Jeon, Seokyoung Bang, Jihoon Ko\*, Jungho Ahn\*. "A Microelectrode-Integrated Perfusable Vessel-on-a-Chip Enabling Simultaneous Measurement of Transendothelial Electrical Resistance and Vascular Permeability". *Advanced Materials Technologies · DOI: 10.1002/admt.202502113[^a47]*.
- Jaehwan Byun, Jungseub Lee, Hyun Ryul Ryu, Geun Jae Lee, Sung Eun Lee, Sung June Kim, Noo Li Jeon\*. "Targeted Local Delivery via Fiber-Embedded Flexible Microchannels Integrated with Film-Based Implantable Probes". *Advanced Materials Technologies · DOI: 10.1002/admt.202401470*.

**2024**

- Jihoon Ko1, Sujin Hyung1, You Jeong Heo, Sangmin Jung, Seung Tae Kim, Se Hoon Park, Jung Yong Hong, Sung Hee Lim, Kyoung-Mee Kim, Sanghee Yoo, Noo Li Jeon\*, Jeeyun Lee\*. "Patient-derived tumor spheroid-induced angiogenesis preclinical platform for exploring therapeutic vulnerabilities in cancer". *Biomaterials 306, 122504 · DOI: 10.1016/j.biomaterials.2024.122504[^a33]*.
- Jungseub Lee1, Sangmin Jung1, Hye Kyoung Hong1, Hyeonsu Jo, Stephen Rhee, Ye-Lin Jeong, Jihoon Ko, Yong Beom Cho\*, Noo Li Jeon\*. "Vascularized tissue on mesh-assisted platform (VT-MAP): a novel approach for diverse organoid size culture and tailored cancer drug response analysis". *Lab on a Chip, 24, 2208-2223 · DOI: 10.1039/d3lc01055d[^a34]*.
- Jihoon Ko1, Sujin Hyung1, Sunghun Cheong, Yoojin Chung, Noo Li Jeon\*. "Revealing the clinical potential of high-resolution organoids". *Advanced Drug Delivery Reviews, 207, 115202 · DOI: 10.1016/j.addr.2024.115202[^a35]*.
- Suryong Kim1, Jungseub Lee1, Jihoon Ko1, Seonghyuk Park, Seung-Ryeol Lee, Youngtaek Kim, Taeseung Lee, Sunbeen Choi, Jiho Kim, Wonbae Kim, Yoojin Chung, Oh-Heum Kwon, Noo Li Jeon\*. "Angio-Net: deep learning-based label-free detection and morphometric analysis of in vitro angiogenesis". *Lab on a Chip, 24, 751-763 · DOI: 10.1039/d3lc00935a*.
- Somin Lee1, Hyunkyung Kim1, Bum Suk Kim1, Sehyun Chae1, Sangmin Jung1, Jung Seub Lee, James Yu, Kyungmin Son, Minhwan Chung, Jong Kyong Kim\*, Daehee Hwang\*, Sung Hee Baek\*, Noo Li Jeon\*. "Angiogenesis-on-a-chip coupled with single-cell RNA sequencing reveals spatially differential activations of autophagy along angiogenic sprouts". *Nature Communications, 15, 230 · DOI: 10.1038/s41467-023-44427-0[^a37]*.
- Yujin Lee, Jaehong Min, Solbin Kim, Wooju Park, Jihoon Ko\*, Noo Li Jeon\*. "Recapitulating the Cancer-Immunity Cycle on a Chip". *Advanced Healthcare Materials, 14 (1), 2401927 · DOI: 10.1002/adhm.202401927*.
- Sangmin Jung, Sunghun Cheong, Yoonho Lee, Jungseub Lee, Jihye Lee, Min-Seok Kwon, Young Sun Oh, Taewan Kim, Sungjae Ha, Sung Jae Kim, Dong Hyun Jo, Jihoon Ko\*, Noo Li Jeon\*. "Integrating Vascular Phenotypic and Proteomic Analysis in an Open Microfluidic Platform". *ACS Nano, 18 (36), 24909–24928 · DOI: 10.1021/acsnano.4c05537*.
- Jiho Kim, Youngsook Song, Amber L. Jolly, Taeseon Hwang, Suryong Kim, Byungjun Lee, Jinhwan Jang, Dong Hyun Jo, Kyusuk Baek, Tsung-Li Liu, Sanghee Yoo\*, Noo Li Jeon\*. "High‐Throughput Microfluidic 3D Outer Blood‐Retinal Barrier Model in a 96‐Well Format: Analysis of Cellular Interactions and Barrier Function in Retinal Health and Disease". *Advanced Materials Technologies, 9, 2400634 · DOI: 10.1002/admt.202400634*.

**2023**

- Jiyoung Song1, Jihoon Ko1, Nakwon Choi\*, Noo Li Jeon\*, Hong Nam Kim\*. "Tumor spheroid-based and microtumor-based vascularized models for replicating the vascularized tumor microenvironment". *Organoid · DOI: 10.51335/organoid.2023.3.e6*.
- Jungeun Lim, Stephen Rhee, Hyeri Choi, Jungseub Lee, Shruthy Kuttappan, Tri Tho Yves Nguyen, Sunbeen Choi, YongTae Kim, Noo Li Jeon\*. "Engineering choroid plexus-on-a-chip with oscillatory flow for modeling brain metastasis". *Materials Today Bio, 22 · DOI: 10.1016/j.mtbio.2023.100773*.
- Jonhny Lam, James Yu, Byungjun Lee, Courtney Campagna, Sanghee Yoo, Kyusuk Baek, Noo Li Jeon, Kyung E. Sung\*. "Characterizing On-Chip Angiogenesis Induction in a Microphysiological System as a Functional Measure of Mesenchymal Stromal Cell Bioactivity". *Advanced Biology · DOI: 10.1002/adbi.202300094*.
- Jiho Kim, Youngsook Song, Amber Jolly, Taeseon Hwang, Suryong Kim, Byungjun Lee, Jinhwan Jang, Kyusuk Baek, Tsung-Li Liu, Sanghee Yoo, Noo Li Jeon\*. "Design and validation of a high-throughput in vitro model of the outer Blood-Retinal Barrier (oBRB) using the Curiochips Microphysiological System". *bioRxiv · DOI: 10.1101/2023.12.01.569537 (사전 공개본)[^a41]*.

**2022**

- Seung-Ryeol Lee1, Youngtaek Kim1, Suryong Kim1, Jiho Kim, Seonghyuk Park, Stephen Rhee, Dohyun Park, Byungjun Lee, Kyusuk Baek, Ho-Young Kim, Noo Li Jeon\*. "U-IMPACT: a universal 3D microfluidic cell culture platform". *Microsystems & Nanoengineering, 8 (1), 1-12 · DOI: 10.1038/s41378-022-00431-w*.
- Jungho Ahn1, Da-Hyun Kim1, Dong-Jun Koo1, Jungeun Lim, Tae-Eun Park, Jungseub Lee, Jihoon Ko, Seongchan Kim, Minjae Kim, Kyung-Sun Kang, Dal-Hee Min, Sung-Yon Kim\*, YongTae Kim\*, Noo Li Jeon\*. "3D microengineered vascularized tumor spheroids for drug delivery and efficacy testing". *Acta Biomaterialia · DOI: 10.1016/j.actbio.2022.10.009[^a5]*.
- Youngtaek Kim1, Jihoon Ko1, Nari Shin, Seonghyuk Park, Seung-Ryeol Lee, Suryong Kim, Jiyoung Song, Seokjun Lee, Kyung-Sun Kang, Jeeyun Lee\*, Noo Li Jeon\*. "All‐in‐one microfluidic design to integrate vascularized tumor spheroid into high‐throughput platform". *Biotechnology and Bioengineering, 1-16 · DOI: 10.1002/bit.28221*.
- Jihoon Ko1, Dohyun Park1, Somin Lee1, Burcu Gumuscu, Noo Li Jeon\*. "Engineering Organ-on-a-Chip to Accelerate Translational Research". *Micromachines, 13 (8), 1200 · DOI: 10.3390/mi13081200[^a7]*.
- Nari Shin1, Youngtaek Kim1, Jihoon Ko, Soon Won Choi, Sujin Hyung, Seung-Eun Lee, Seunghyuk Park, Jiyoung Song, Noo Li Jeon\*, Kyung-Sun Kang\*. "Vascularization of iNSC spheroid in a 3D spheroid-on-a-chip platform enhances neural maturation". *Biotechnology and Bioengineering, 119 (2), 566-574 · DOI: 10.1002/bit.27978*.
- Byungjun Lee1, Suryong Kim1, Jihoon Ko, Seung-Ryeol Lee, Youngtaek Kim, Seonghyuk Park, Jiho Kim, Sujin Hyung, Ho-Young Kim, Noo Li jeon\*. "3D micromesh-based hybrid bioprinting: multidimensional liquid patterning for 3D microtissue engineering". *NPG Asia Materials, 14 (1), 1-10 · DOI: 10.1038/s41427-022-00355-x*.
- ​Johnny Lam, Byungjun Lee, James Yu, Brian J Kwee, Yangji Kim, Jiho Kim, Yeongmin Choi, Jun Sung Yoon, Youngsoo Kim, Kyusuk Baek, Noo Li Jeon, Kyung E Sung\*. "A microphysiological system-based potency bioassay for the functional quality assessment of mesenchymal stromal cells targeting vasculogenesis". *Biomaterials, 121826 · DOI: 10.1016/j.biomaterials.2022.121826*.
- Byung Hun Lee, Seokyoung Bang, Seung-Ryeol Lee, Noo Li Jeon, Hye Yoon Park\*. "Dynamics of axonal β-actin mRNA in live hippocampal neurons". *Traffic, 23, 496-505 · DOI: 10.1111/tra.12865*.
- James Yu, Somin Lee, Jiyoung Song, Seung-Ryeol Lee, Suryong Kim, Hyeri Choi, Habin Kang, Yunchan Hwang, Young-Kwon Hong, Noo Li Jeon\*. "Perfusable micro-vascularized 3D tissue array for high-throughput vascular phenotypic screening". *Nano Convergence, 9 (1), 1-11 · DOI: 10.1186/s40580-022-00306-w*.
- Dongwon Choi, Eunkyung Park, Roy P. Yu, Michael N. Cooper, Il-Taeg Cho, Joshua Choi, James Yu, Luping Zhao, Ji-Eun Irene Yum, Jin Suh Yu, Brandon Nakashima, Sunju Lee, Young Jin Seong, Wan Jiao, Chester J. Koh, Peter Baluk, Donald M. McDonald, Sindhu Saraswathy, Jong Y Lee, Noo Li Jeon, Zhenqian Zhang, Alex S Huang, Bin Zhou, Alex K. Wong, Young-Kwon Hong\*. "Piezo1-Regulated Mechanotransduction Controls Flow-Activated Lymphatic Expansion". *Circulation Research, 131 (2), 2-21 · DOI: 10.1161/circresaha.121.320565*.

## 수상과 선정

연구실 소식에 게시된 2022년 4월 22일–2026년 4월 23일의 수상 8건이다. 날짜는 글 제목이나 본문에 적힌 수상일이다.

- 2022-04-22 · 이정섭 박사, 대한기계학회 바이오공학부문 춘계학술대회 우수 논문상[^n601]
- 2023-04-28 · 정상민 박사과정생, 대한기계학회 바이오공학부문 우수 논문상[^n602]
- 2023-11-10 · 전누리 교수, 바이오 산업 분야 발전 유공자로 과학기술정보통신부 장관 표창장[^n603]
- 2023-11-16 · 정성훈 박사과정생, 한국바이오칩학회 최우수 포스터 발표상[^n604]
- 2023-11-16 · 전누리 교수, 한국바이오칩학회 산학 협력 공로상(금상)[^n605]
- 2024-05-24 · 김솔빈 석사과정생, 한국바이오칩학회 최우수 포스터 발표상[^n607]
- 2025-05-15 · 전누리 교수, 한국정밀공학회 춘계학술대회 학회 발전 공로 감사장[^n608]
- 2026-04-23 · 정상민 박사, 대한기계학회 바이오공학부문 우수학위논문상[^n612]

## 소식

연구실이 알린 연구 성과의 보도 소식이다. 날짜는 글 제목의 표기를 따른다.

- 2024-01-23 · 혈관신생 중 선택적 자가포식 조절 원리를 밝힌 연구가 신문에 소개되었다.[^n606]

## 연락과 위치

- 교수 업무 이메일: njeon@snu.ac.kr.[^prof][^contact]
- 연구실 전화: 02-880-1646, 02-880-7119.[^contact]
- 연구실 누리집의 Office: 서울대학교 312동 401호.[^contact]
- 연구실 누리집의 Laboratory: 서울대학교 302동 415-2호.[^contact]
- 학과 교수 소개의 사무실: 서울대학교 301동 1416호, 전화 02-880-7111.[^dept]
- 학과 교수 소개의 연구실: 서울대학교 312동 401호(02-880-1646), 302동 415-1호(02-880-7119).[^dept]
- 주소: 08826 서울특별시 관악구 관악로 1 서울대학교.[^contact]

## 각주
[^research]: 연구실 연구 소개. <https://mbel.snu.ac.kr/research/> 관측일 2026-11-07.
[^organ]: 연구실 Organ on a chip. <https://mbel.snu.ac.kr/organ-on-a-chip/> 관측일 2026-11-07.
[^micro]: 연구실 Microfabrication. <https://mbel.snu.ac.kr/microfabrication/> 관측일 2026-11-07.
[^analysis]: 연구실 Analysis. <https://mbel.snu.ac.kr/analysis/> 관측일 2026-11-07.
[^prof]: 연구실 Professor. <https://mbel.snu.ac.kr/?member=%ec%a0%84%eb%88%84%eb%a6%ac> 관측일 2026-11-07.
[^dept]: 서울대학교 기계공학부 전누리 교수 소개. <https://me.snu.ac.kr/snu__professor/%ec%a0%84%eb%88%84%eb%a6%ac-jeon-noo-li/> 관측일 2026-11-07.
[^contact]: 연구실 Contact. <https://mbel.snu.ac.kr/%ec%b0%be%ec%95%84%ec%98%a4%ec%8b%9c%eb%8a%94%ea%b8%b8/> 관측일 2026-11-07.
[^members]: 연구실 Current members와 현재 구성원 상세 21쪽. <https://mbel.snu.ac.kr/%ea%b5%ac%ec%84%b1%ec%9b%90_1-2/%ea%b5%ac%ec%84%b1%ec%9b%90_1/> <https://mbel.snu.ac.kr/member/ailian-jin/> <https://mbel.snu.ac.kr/member/%ec%b5%9c%ed%98%9c%eb%a6%ac/> <https://mbel.snu.ac.kr/member/hyeonsu-jo/> <https://mbel.snu.ac.kr/member/seonghyuk-park/> <https://mbel.snu.ac.kr/member/sunghun-cheong/> <https://mbel.snu.ac.kr/member/yujin-lee/> <https://mbel.snu.ac.kr/member/%ea%b9%80%ed%95%b4%ec%9c%a4/> <https://mbel.snu.ac.kr/member/stefania-martini/> <https://mbel.snu.ac.kr/member/%ec%9d%b4%ec%9e%ac%ec%a4%80/> <https://mbel.snu.ac.kr/member/%ec%8b%a0%ec%9c%a4%ec%b0%ac/> <https://mbel.snu.ac.kr/member/%ec%9d%b4%ec%9e%ac%ec%9d%80/> <https://mbel.snu.ac.kr/member/%ea%b9%80%ec%86%94%eb%b9%88/> <https://mbel.snu.ac.kr/member/%ec%9d%b4%ec%98%81%ea%b7%a0/> <https://mbel.snu.ac.kr/member/%ea%b9%80%ec%86%94%ed%9d%ac/> <https://mbel.snu.ac.kr/member/%ec%a1%b0%ec%9c%a4/> <https://mbel.snu.ac.kr/member/shruthy-kuttappan/> <https://mbel.snu.ac.kr/member/%ea%b9%80%ec%84%a0%ea%b8%b0/> <https://mbel.snu.ac.kr/member/%ec%98%a4%ec%98%81%ec%84%a0/> <https://mbel.snu.ac.kr/member/%ea%b9%80%eb%b2%94%ec%a3%bc/> <https://mbel.snu.ac.kr/member/9255/> <https://mbel.snu.ac.kr/member/sunbeen-choi/> 관측일 2026-11-07.
[^alumni]: 연구실 Alumni와 졸업생 상세 55쪽. <https://mbel.snu.ac.kr/%ea%b5%ac%ec%84%b1%ec%9b%90-2-2/> <https://mbel.snu.ac.kr/member/sofia-madrigal-gamboa-2022/> <https://mbel.snu.ac.kr/member/dr-jungeun-lim-2022/> <https://mbel.snu.ac.kr/member/dr-suryong-kim-2022/> <https://mbel.snu.ac.kr/member/dr-seung-ryeol-lee-2021/> <https://mbel.snu.ac.kr/member/habin-kang-2021/> <https://mbel.snu.ac.kr/member/dr-jiyoung-song-2021/> <https://mbel.snu.ac.kr/member/dr-dohyun-park-2020/> <https://mbel.snu.ac.kr/member/james-yu-2020/> <https://mbel.snu.ac.kr/member/munseok-choi-2019/> <https://mbel.snu.ac.kr/member/dr-sang-min-paik-2018/> <https://mbel.snu.ac.kr/member/youngguyn-lee-2018/> <https://mbel.snu.ac.kr/member/kyungmin-son-2018/> <https://mbel.snu.ac.kr/member/jungmin-ha-2018/> <https://mbel.snu.ac.kr/member/dr-seokyoung-bang-2018/> <https://mbel.snu.ac.kr/member/dr-byungjun-lee-2018/> <https://mbel.snu.ac.kr/member/dr-dongha-tahk-2018/> <https://mbel.snu.ac.kr/member/dr-kyungwon-yun-2018/> <https://mbel.snu.ac.kr/member/dr-norhana-jusoh-2018/> <https://mbel.snu.ac.kr/member/dr-minhwan-chung-2017/> <https://mbel.snu.ac.kr/member/dr-sangcheol-na-2017/> <https://mbel.snu.ac.kr/member/dr-soojung-oh-2016/> <https://mbel.snu.ac.kr/member/dr-hyunryul-ryu-2015/> <https://mbel.snu.ac.kr/member/dr-hyunjae-lee-2015/> <https://mbel.snu.ac.kr/member/dr-jae-myung-jang-2015/> <https://mbel.snu.ac.kr/member/dr-jae-woo-park-2015/> <https://mbel.snu.ac.kr/member/dr-minsung-kim-2015/> <https://mbel.snu.ac.kr/member/dr-do-hyun-kang-2014/> <https://mbel.snu.ac.kr/member/dr-sudong-kim-2014/> <https://mbel.snu.ac.kr/member/dr-hong-nam-kim-2014/> <https://mbel.snu.ac.kr/member/dr-jae-hwan-byun-2014/> <https://mbel.snu.ac.kr/member/dr-won-gyu-bae-2014/> <https://mbel.snu.ac.kr/member/thanh-qua-nguyen-2014/> <https://mbel.snu.ac.kr/member/woohyun-park-2014/> <https://mbel.snu.ac.kr/member/jaerim-kim-2014/> <https://mbel.snu.ac.kr/member/si-hoai-trung-tran-2014/> <https://mbel.snu.ac.kr/member/minseo-kim-2012/> <https://mbel.snu.ac.kr/member/yekyung-cho-2011/> <https://mbel.snu.ac.kr/member/qing-ping-hu-2010/> <https://mbel.snu.ac.kr/member/dr-myeongwoo-kang-2015/> <https://mbel.snu.ac.kr/member/dr-jungho-ahn-2020/> <https://mbel.snu.ac.kr/member/%ec%8b%ac%eb%af%b8%ea%b0%95/> <https://mbel.snu.ac.kr/member/%eb%b0%95%ec%98%88%eb%a6%bc/> <https://mbel.snu.ac.kr/member/%ec%9d%b4%ed%83%9c%ec%8a%b9/> <https://mbel.snu.ac.kr/member/dr-youngtaek-kim-2022/> <https://mbel.snu.ac.kr/member/%ed%99%8d%ec%a2%85%ed%98%b8/> <https://mbel.snu.ac.kr/member/%ea%b9%80%ec%84%a0/> <https://mbel.snu.ac.kr/member/%ec%a0%95%ec%83%81%eb%af%bc/> <https://mbel.snu.ac.kr/member/stephen-rhee-2023/> <https://mbel.snu.ac.kr/member/tri-tho-nguyen-2022/> <https://mbel.snu.ac.kr/member/%ea%b9%80%ec%a7%80%ed%98%b8/> <https://mbel.snu.ac.kr/member/%ec%86%90%ea%b3%a0%ec%9d%80/> <https://mbel.snu.ac.kr/member/%ed%95%9c%ea%b0%80%ec%9d%80/> <https://mbel.snu.ac.kr/member/%ec%9d%b4%ec%9c%a4%ed%98%b8/> <https://mbel.snu.ac.kr/member/dr-jihoon-ko-2021/> <https://mbel.snu.ac.kr/member/dr-somin-lee-2021/> 관측일 2026-11-07.
[^journals]: 연구실 Journals와 해당 논문 상세. <https://mbel.snu.ac.kr/%eb%85%bc%eb%ac%b8/> <https://mbel.snu.ac.kr/publication/flow-impact-a-pumpless-high-throughput-3d-cell-culture-platform-for-investigation-of-synergistic-angiogenic-effects/> <https://mbel.snu.ac.kr/publication/tumor-spheroid-based-and-microtumor-based-vascularized-models-for-replicating-the-vascularized-tumor-microenvironment/> <https://mbel.snu.ac.kr/publication/u-impact-a-universal-3d-microfluidic-cell-culture-platform/> <https://mbel.snu.ac.kr/publication/3d-microengineered-vascularized-tumor-spheroids-for-drug-delivery-and-efficacy-testing/> <https://mbel.snu.ac.kr/publication/all%e2%80%90in%e2%80%90one-microfluidic-design-to-integrate-vascularized-tumor-spheroid-into-high%e2%80%90throughput-platform/> <https://mbel.snu.ac.kr/publication/engineering-organ-on-a-chip-to-accelerate-translational-research/> <https://mbel.snu.ac.kr/publication/vascularization-of-insc-spheroid-in-a-3d-spheroid-on-a-chip-platform-enhances-neural-maturation/> <https://mbel.snu.ac.kr/publication/3d-micromesh-based-hybrid-bioprinting-multidimensional-liquid-patterning-for-3d-microtissue-engineering/> <https://mbel.snu.ac.kr/publication/engineering-choroid-plexus-on-a-chip-with-oscillatory-flow-for-modeling-brain-metastasis/> <https://mbel.snu.ac.kr/publication/characterizing-on-chip-angiogenesis-induction-in-a-microphysiological-system-as-a-functional-measure-of-mesenchymal-stromal-cell-bioactivity/> <https://mbel.snu.ac.kr/publication/a-microphysiological-system-based-potency-bioassay-for-the-functional-quality-assessment-of-mesenchymal-stromal-cells-targeting-vasculogenesis/> <https://mbel.snu.ac.kr/publication/dynamics-of-axonal-%ce%b2-actin-mrna-in-live-hippocampal-neurons/> <https://mbel.snu.ac.kr/publication/perfusable-micro-vascularized-3d-tissue-array-for-high-throughput-vascular-phenotypic-screening/> <https://mbel.snu.ac.kr/publication/piezo1-regulated-mechanotransduction-controls-flow-activated-lymphatic-expansion/> <https://mbel.snu.ac.kr/publication/patient-derived-tumor-spheroid-induced-angiogenesis-preclinical-platform-for-exploring-therapeutic-vulnerabilities-in-cancer/> <https://mbel.snu.ac.kr/publication/vascularized-tissue-on-mesh-assisted-platform-vt-map-a-novel-approach-for-diverse-organoid-size-culture-and-tailored-cancer-drug-response-analysis/> <https://mbel.snu.ac.kr/publication/revealing-the-clinical-potential-of-high-resolution-organoids/> <https://mbel.snu.ac.kr/publication/angio-net-deep-learning-based-label-free-detection-and-morphometric-analysis-of-in-vitro-angiogenesis/> <https://mbel.snu.ac.kr/publication/angiogenesis-on-a-chip-coupled-with-single-cell-rna-sequencing-reveals-spatially-differential-activations-of-autophagy-along-angiogenic-sprouts/> <https://mbel.snu.ac.kr/publication/recapitulating-the-cancer-immunity-cycle-on-a-chip/> <https://mbel.snu.ac.kr/publication/integrating-vascular-phenotypic-and-proteomic-analysis-in-an-open-microfluidic-platform/> <https://mbel.snu.ac.kr/publication/design-and-validation-of-a-high-throughput-in-vitro-model-of-the-outer-blood-retinal-barrier-obrb-using-the-curiochips-microphysiological-system/> <https://mbel.snu.ac.kr/publication/high%e2%80%90throughput-microfluidic-3d-outer-blood%e2%80%90retinal-barrier-model-in-a-96%e2%80%90well-format-analysis-of-cellular-interactions-and-barrier-function-in-retinal-health-and-disease/> <https://mbel.snu.ac.kr/publication/cytotoxic-chemotherapy-in-a-3d-microfluidic-device-induces-dendritic-cell-recruitment-and-trogocytosis-of-cancer-cells/> <https://mbel.snu.ac.kr/publication/engineering-a-whitlockite-containing-macroporous-composite-cryogel-with-silica-hybrid-for-enhanced-vascularized-bone-regeneration/> <https://mbel.snu.ac.kr/publication/a-3d-microfluidic-model-of-initial-lymphatic-vessels-for-investigating-dendritic-cell-chemotaxis-under-inflammatory-condition/> <https://mbel.snu.ac.kr/publication/a-microelectrode-integrated-perfusable-vessel-on-a-chip-enabling-simultaneous-measurement-of-transendothelial-electrical-resistance-and-vascular-permeability/> <https://mbel.snu.ac.kr/publication/a-microfluidic-cell-culture-platform-for-modeling-aligned-peripheral-nerve-bundle-connection-and-myelination/> <https://mbel.snu.ac.kr/publication/targeted-local-delivery-via-fiber-embedded-flexible-microchannels-integrated-with-film-based-implantable-probes/> <https://mbel.snu.ac.kr/publication/immune-microphysiological-systems-for-human-innate-immunity/> <https://mbel.snu.ac.kr/publication/high-throughput-digital-decoding-of-vascular-heterogeneity-in-patient-specific-tumor-microenvironments/> <https://mbel.snu.ac.kr/publication/engineering-pluripotent-stem-cells-derived-inner-ear-organoids-with-enhanced-maturation-and-reproducibility-by-micro-topographical-cues/> <https://mbel.snu.ac.kr/publication/from-flow-to-form-structuring-and-patterning-hydrogels-using-microfluidic-approaches-open-access/> <https://mbel.snu.ac.kr/publication/a-perfusable-first-generation-endometrial-microvascular-model-to-study-human-spiral-artery-remodeling-in-pregnancy/> 관측일 2026-11-07.
[^n601]: 연구실 소식, 2022년 4월, 이정섭 박사 대한기계학회 바이오공학부문 2022년 춘계학술대회 우수 논문상 수상(2022/04/22). <https://mbel.snu.ac.kr/news-2/document/82/> 관측일 2026-11-07.
[^n602]: 연구실 소식, 2023년 4월, 정상민 박사과정생 2023 대한기계학회 바이오공학부문 우수 논문상 수상(2023/04/28). <https://mbel.snu.ac.kr/news-2/document/83/> 관측일 2026-11-07.
[^n603]: 연구실 소식, 2023년 11월, 전누리 교수님 과학기술정보통신부 장관 표창장 수상(2023/11/10). <https://mbel.snu.ac.kr/news-2/document/84/> 관측일 2026-11-07.
[^n604]: 연구실 소식, 2023년 11월, 정성훈 박사과정생 2023 한국바이오칩학회 최우수 포스터 발표상 수상(2023/11/16). <https://mbel.snu.ac.kr/news-2/document/85/> 관측일 2026-11-07.
[^n605]: 연구실 소식, 2023년 11월, 전누리 교수님 한국바이오칩 학회 산학협력공로상 수상(2023/11/16). <https://mbel.snu.ac.kr/news-2/document/86/> 관측일 2026-11-07.
[^n606]: 연구실 소식, Our new technology is reported in the newspaper.(2024/01/23). <https://mbel.snu.ac.kr/news-2/document/100/> 관측일 2026-11-07.
[^n607]: 연구실 소식, 2024년 05월, 김솔빈 석사과정생 2024 한국바이오칩학회 최우수 포스터 발표상 수상(2024/05/24). <https://mbel.snu.ac.kr/news-2/document/101/> 관측일 2026-11-07.
[^n608]: 연구실 소식, 2025년 전누리 교수님 한국정밀공학회 춘계학술대회 감사장 수상 (2025/05/15). <https://mbel.snu.ac.kr/news-2/document/103/> 관측일 2026-11-07.
[^n612]: 연구실 소식, 2026년 4월, 정상민 박사 2026 대한기계학회 바이오공학부문 우수학위논문상 수상 (2026/04/23). <https://mbel.snu.ac.kr/news-2/document/112/> 관측일 2026-11-07.
[^p1]: E. E. Bouker 외, A. B. Theberge, Lab on a Chip (2026). <https://doi.org/10.1039/d6lc00386a> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5051796736,publication_year:2021-2026> 서지·전체 저자 순서는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/from-flow-to-form-structuring-and-patterning-hydrogels-using-microfluidic-approaches-open-access/>. 관측일 2026-11-07.
[^p2]: S. Kim 외, J. Ko, Advanced Materials Technologies (2026). <https://doi.org/10.1002/admt.71051> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5051796736,publication_year:2021-2026> 서지·전체 저자 순서는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/immune-microphysiological-systems-for-human-innate-immunity/>. 관측일 2026-11-07.
[^p3]: J. Byun 외, N. L. Jeon, Advanced Materials Technologies (2025). <https://doi.org/10.1002/admt.202401470> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5051796736,publication_year:2021-2026> 서지·전체 저자 순서는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/targeted-local-delivery-via-fiber-embedded-flexible-microchannels-integrated-with-film-based-implantable-probes/>. 관측일 2026-11-07.
[^p4]: S. Park 외, N. L. Jeon, Advanced Materials Technologies (2025). <https://doi.org/10.1002/admt.202401526> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5051796736,publication_year:2021-2026> 서지·전체 저자 순서는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/flow-impact-a-pumpless-high-throughput-3d-cell-culture-platform-for-investigation-of-synergistic-angiogenic-effects/>. 관측일 2026-11-07.
[^p5]: S. Kim 외, N. L. Jeon, Lab on a Chip (2024). <https://doi.org/10.1039/d3lc00935a> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5051796736,publication_year:2021-2026> 서지·전체 저자 순서는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/angio-net-deep-learning-based-label-free-detection-and-morphometric-analysis-of-in-vitro-angiogenesis/>. 관측일 2026-11-07.
[^p6]: S.-R. Lee 외, N. L. Jeon, Microsystems & Nanoengineering (2022). <https://doi.org/10.1038/s41378-022-00431-w> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5051796736,publication_year:2021-2026> 서지·전체 저자 순서는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/u-impact-a-universal-3d-microfluidic-cell-culture-platform/>. 관측일 2026-11-07.
[^p7]: B. Lee 외, N. L. Jeon, NPG Asia Materials (2022). <https://doi.org/10.1038/s41427-022-00355-x> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5051796736,publication_year:2021-2026> 서지·전체 저자 순서는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/3d-micromesh-based-hybrid-bioprinting-multidimensional-liquid-patterning-for-3d-microtissue-engineering/>. 관측일 2026-11-07.
[^p8]: B. H. Lee 외, H. Y. Park, Traffic (2022). <https://doi.org/10.1111/tra.12865> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5051796736,publication_year:2021-2026> 서지·전체 저자 순서는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/dynamics-of-axonal-%ce%b2-actin-mrna-in-live-hippocampal-neurons/>. 관측일 2026-11-07.
[^a5]: Jungho Ahn1, Da-Hyun Kim1, Dong-Jun Koo1, Jungeun Lim, Tae-Eun Park, Jungseub Lee, Jihoon Ko, Seongchan Kim, Minjae Kim, Kyung-Sun Kang, Dal-Hee Min, Sung-Yon Kim\*, YongTae Kim\*, Noo Li Jeon\*. 3D microengineered vascularized tumor spheroids for drug delivery and efficacy testing. Acta Biomaterialia (2022). <https://doi.org/10.1016/j.actbio.2022.10.009> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.actbio.2022.10.009%22>. 목록의 저자·제목·발표처·연도는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/3d-microengineered-vascularized-tumor-spheroids-for-drug-delivery-and-efficacy-testing/>. 관측일 2026-11-07.
[^a7]: Jihoon Ko1, Dohyun Park1, Somin Lee1, Burcu Gumuscu, Noo Li Jeon\*. Engineering Organ-on-a-Chip to Accelerate Translational Research. Micromachines, 13 (8), 1200 (2022). <https://doi.org/10.3390/mi13081200> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=Engineering%20Organ-on-a-Chip%20to%20Accelerate%20Translational%20Research>. 목록의 저자·제목·발표처·연도는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/engineering-organ-on-a-chip-to-accelerate-translational-research/>. 관측일 2026-11-07.
[^a33]: Jihoon Ko1, Sujin Hyung1, You Jeong Heo, Sangmin Jung, Seung Tae Kim, Se Hoon Park, Jung Yong Hong, Sung Hee Lim, Kyoung-Mee Kim, Sanghee Yoo, Noo Li Jeon\*, Jeeyun Lee\*. Patient-derived tumor spheroid-induced angiogenesis preclinical platform for exploring therapeutic vulnerabilities in cancer. Biomaterials 306, 122504 (2024). <https://doi.org/10.1016/j.biomaterials.2024.122504> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.biomaterials.2024.122504%22>. 목록의 저자·제목·발표처·연도는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/patient-derived-tumor-spheroid-induced-angiogenesis-preclinical-platform-for-exploring-therapeutic-vulnerabilities-in-cancer/>. 관측일 2026-11-07.
[^a34]: Jungseub Lee1, Sangmin Jung1, Hye Kyoung Hong1, Hyeonsu Jo, Stephen Rhee, Ye-Lin Jeong, Jihoon Ko, Yong Beom Cho\*, Noo Li Jeon\*. Vascularized tissue on mesh-assisted platform (VT-MAP): a novel approach for diverse organoid size culture and tailored cancer drug response analysis. Lab on a Chip, 24, 2208-2223 (2024). <https://doi.org/10.1039/d3lc01055d> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1039/d3lc01055d%22>. 목록의 저자·제목·발표처·연도는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/vascularized-tissue-on-mesh-assisted-platform-vt-map-a-novel-approach-for-diverse-organoid-size-culture-and-tailored-cancer-drug-response-analysis/>. 관측일 2026-11-07.
[^a35]: Jihoon Ko1, Sujin Hyung1, Sunghun Cheong, Yoojin Chung, Noo Li Jeon\*. Revealing the clinical potential of high-resolution organoids. Advanced Drug Delivery Reviews, 207, 115202 (2024). <https://doi.org/10.1016/j.addr.2024.115202> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.addr.2024.115202%22>. 목록의 저자·제목·발표처·연도는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/revealing-the-clinical-potential-of-high-resolution-organoids/>. 관측일 2026-11-07.
[^a37]: Somin Lee1, Hyunkyung Kim1, Bum Suk Kim1, Sehyun Chae1, Sangmin Jung1, Jung Seub Lee, James Yu, Kyungmin Son, Minhwan Chung, Jong Kyong Kim\*, Daehee Hwang\*, Sung Hee Baek\*, Noo Li Jeon\*. Angiogenesis-on-a-chip coupled with single-cell RNA sequencing reveals spatially differential activations of autophagy along angiogenic sprouts. Nature Communications, 15, 230 (2024). <https://doi.org/10.1038/s41467-023-44427-0> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=Angiogenesis-on-a-chip%20coupled%20with%20single-cell%20RNA%20sequencing%20reveals%20spatially%20differential%20activations%20of%20autophagy%20along%20angiogenic%20sprouts>. 목록의 저자·제목·발표처·연도는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/angiogenesis-on-a-chip-coupled-with-single-cell-rna-sequencing-reveals-spatially-differential-activations-of-autophagy-along-angiogenic-sprouts/>. 관측일 2026-11-07.
[^a41]: Jiho Kim, Youngsook Song, Amber Jolly, Taeseon Hwang, Suryong Kim, Byungjun Lee, Jinhwan Jang, Kyusuk Baek, Tsung-Li Liu, Sanghee Yoo, Noo Li Jeon\*. Design and validation of a high-throughput in vitro model of the outer Blood-Retinal Barrier (oBRB) using the Curiochips Microphysiological System. bioRxiv (2023). bioRxiv 사전 공개본. <https://doi.org/10.1101/2023.12.01.569537> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1101/2023.12.01.569537>. 목록의 저자·제목·발표처·연도는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/design-and-validation-of-a-high-throughput-in-vitro-model-of-the-outer-blood-retinal-barrier-obrb-using-the-curiochips-microphysiological-system/>. 관측일 2026-11-07.
[^a46]: Hyeonsu Jo, Somin Lee, Inae Park, Mikang Shim, James Yu, Young Sun Oh, Junsang Doh, Young-Kwon Hong, Noo Li Jeon. A 3D Microfluidic Model of Initial Lymphatic Vessels for Investigating Dendritic Cell Chemotaxis Under Inflammatory Condition. BioChip Journal (2025). <https://doi.org/10.1007/s13206-025-00227-w> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1007/s13206-025-00227-w>. 목록의 저자·제목·발표처·연도는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/a-3d-microfluidic-model-of-initial-lymphatic-vessels-for-investigating-dendritic-cell-chemotaxis-under-inflammatory-condition/>. 관측일 2026-11-07.
[^a47]: Hyeongjin Ahn, Jaehong Min, Wooju Park, Sanghyeok Park, Younggyun Lee, Jungseub Lee, Wonsuk Shin, Noo Li Jeon, Seokyoung Bang, Jihoon Ko\*, Jungho Ahn\*. A Microelectrode-Integrated Perfusable Vessel-on-a-Chip Enabling Simultaneous Measurement of Transendothelial Electrical Resistance and Vascular Permeability. Advanced Materials Technologies (2025). <https://doi.org/10.1002/admt.202502113> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1002/admt.202502113>. 목록의 저자·제목·발표처·연도는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/a-microelectrode-integrated-perfusable-vessel-on-a-chip-enabling-simultaneous-measurement-of-transendothelial-electrical-resistance-and-vascular-permeability/>. 관측일 2026-11-07.
[^a48]: Ailian Jin, Sang Wook Shim, Mikang Shim, Yoon Kyung Lee, Jongho Hong, Dahee Roh, Sujin Hyung\*, Seog Bae Oh\*, Noo Li Jeon\*. A Microfluidic Cell Culture Platform for Modeling Aligned Peripheral Nerve Bundle, Connection, and Myelination. Advanced Healthcare Materials (2026). <https://doi.org/10.1002/adhm.202504121> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1002/adhm.202504121>. 목록의 저자·제목·발표처·연도는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/a-microfluidic-cell-culture-platform-for-modeling-aligned-peripheral-nerve-bundle-connection-and-myelination/>. 관측일 2026-11-07.
[^a51]: Jungseub Lee, Wooju Park, Sujin Hyung, Sangmin Jung, Kyungho Lee, Junseok Jeon, Noo Li Jeon\*, Jeeyun Lee\*, Hye Ryoun Jang\*, Jihoon Ko\*. High-Throughput Digital Decoding of Vascular Heterogeneity in Patient-Specific Tumor Microenvironments. Advanced Healthcare Materials (2026). <https://doi.org/10.1002/adhm.202505866> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1002/adhm.202505866>. 목록의 저자·제목·발표처·연도는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/high-throughput-digital-decoding-of-vascular-heterogeneity-in-patient-specific-tumor-microenvironments/>. 관측일 2026-11-07.
[^a52]: Harshita Sharma, Jungeun Lim, Woochan Kim, Yeon Ju Kim, Dream Kim, Shinyull Lee, Chaeyeon Park, Stephen Rhee, Shruthy Kuttapan, Jungho Ha, Sang Wook Park, Kyunghoon Kim, Noo Li Jeon, Sunho Park\*, Yun-Hoon Choung\*, Jangho Kim\*. Engineering Pluripotent Stem Cells-Derived Inner Ear Organoids With Enhanced Maturation and Reproducibility by Micro-Topographical Cues. Advanced Materials (2026). <https://doi.org/10.1002/adma.74560> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1002/adma.74560>. 목록의 저자·제목·발표처·연도는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/engineering-pluripotent-stem-cells-derived-inner-ear-organoids-with-enhanced-maturation-and-reproducibility-by-micro-topographical-cues/>. 관측일 2026-11-07.
[^a54]: Sebastian Naranjo, Madison E. Fletcher, Noo Li Jeon, Joyce Y. Wong\*, Catherine Klapperich\*. A perfusable first-generation endometrial microvascular model to study human spiral artery remodeling in pregnancy. Lab on a Chip (2026). <https://doi.org/10.1039/d6lc00513f> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1039/d6lc00513f%22>. 목록의 저자·제목·발표처·연도는 연구실 논문 상세 <https://mbel.snu.ac.kr/publication/a-perfusable-first-generation-endometrial-microvascular-model-to-study-human-spiral-artery-remodeling-in-pregnancy/>. 관측일 2026-11-07.

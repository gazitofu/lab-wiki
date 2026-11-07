# Biomedical Optics Laboratory (BMOL)

**KAIST 물리학과 · 박용근 교수**

- 분야: 광학 영상, 정량 측정, 광학 소자 내부 구조 분석[^dept][^research]
- 대분야: 물리·양자, 전기전자·반도체·광학
- 태그: 광학 영상·현미경[^methods], 홀로그래피·라이트필드 3차원 영상[^holo], 반도체 계측·검사[^industry]
- 홈페이지: <https://bmol.kaist.ac.kr/>
- 근거와 출처: [Biomedical Optics Laboratory 근거 페이지](bmol-sources.md)

> 빛을 측정하고 제어하는 장치와 계산 방법을 개발해 살아 있는 세포와 광학 소자의 내부 구조를 입체적으로 정량화한다.[^research]

## 무엇을 연구하나

BMOL의 공통 연구 기반은 빛을 측정하고 조절해 물체의 내부 구조를 수치로 알아내는 것이다. 광학계(빛을 발생·조절·전달·검출하도록 구성한 장치 체계), 조명 방식, 영상 복원 계산을 함께 설계한다. 빛의 위상(파동이 반복되는 주기 안에서 진행한 단계)을 측정하는 정량 위상 영상(Quantitative Phase Imaging, QPI)을 개발하며, 살아 있는 세포를 염료로 표지하지 않고 관찰하는 방법이 주요 갈래다.[^methods]

이때 중요한 물성은 굴절률(물질이 없는 공간에서의 빛의 속도를 해당 물질 속 빛의 속도로 나눈 값)이다. 홀로토모그래피(빛의 파동 정보를 여러 방향에서 측정해 내부 굴절률의 입체 분포를 복원하는 방법)로 세포의 모양과 내부 구조를 기록하고, 건조 질량(물의 질량을 제외한 물질의 질량)과 그 시간 변화를 정량화한다. 연구실은 두꺼운 세포 집합과 조직까지 관찰하도록 영상의 깊이·획득 속도·복원 정확도를 높이는 광학·계산 방법을 개발한다.[^methods]

물체가 두꺼워지면 빛의 산란(빛이 물질과 상호작용하며 진행 방향이 바뀌는 현상)이 반복되어 내부 구조를 복원하기 어려워진다. 연구실은 이런 측정에서 생기는 역문제(관측된 결과로부터 원인이나 내부 상태를 구하는 문제)를 푸는 계산법을 연구한다.[^methods] 또한 홀로그래피(빛의 진폭과 위상 정보를 기록하거나 계산해 파면을 재구성하는 기술)를 개발한다.[^holo] 진폭은 파동이 기준 상태에서 벗어나는 최대 크기이며, 파면은 같은 위상을 가진 지점들을 이은 면이다.

같은 측정 기반을 생명과학과 산업으로 넓힌다. 생명과학에서는 세포·조직을 훼손하지 않는 연속 영상과 기계학습(자료에서 규칙을 학습해 예측·분류 등에 사용하는 계산 방법)을 결합한다.[^research] 산업에서는 반도체와 디스플레이의 투명한 구조·층 사이 접합면을 측정하고 결함을 찾는 방법을 개발 중이다.[^industry] 난자·정자·배아를 손상 없이 정량 평가하는 영상 방법도 연구 목표로 제시한다.[^research]

## 주요 연구 주제

### 1. 빛의 파동 정보로 만드는 입체 영상

정량 위상 영상과 홀로토모그래피의 광학 장치·조명·복원 계산을 함께 개발한다. 참조광(측정하려는 빛과 비교하기 위해 별도로 준비한 빛) 없이 한 장의 세기 영상에서 물체의 빛 정보를 복원하는 홀로그래픽 카메라가 한 예다. 이 연구는 빛의 세기뿐 아니라 진폭과 위상을 구해 입체 물체를 촬영하는 영상 센서(빛을 감지해 영상 자료로 바꾸는 소자)를 제시했다.[^methods][^p1]

### 2. 방향에 따라 다른 재료와 산업 소자의 내부 측정

재료의 이방성(방향에 따라 물리적 성질이 달라지는 특성)을 입체적으로 측정한다. 분자(원자들이 화학 결합으로 연결된 입자)의 방향 배열을 살피며, 액정(흐르는 성질과 구성 분자 배열의 방향 질서를 함께 지닌 물질 상태)의 내부 구조를 산란 이론으로 복원한다. 홀로그래픽 광학 소자(홀로그래피 원리로 빛의 방향을 바꾸거나 모으는 소자) 내부에 기록된 분자 배열도 직접 시각화한다.[^p2][^p4] 산업 측정에서는 유리 기판(다른 구조를 만들거나 지지하는 바탕 재료)의 균열·빈 공간·내부 통로 형상과 접합면의 결함을 정량화하는 방법을 개발한다.[^industry] 반도체·디스플레이 전용 검사 연구는 개발 중인 방향으로 제시되어 있다.[^industry]

### 3. 살아 있는 세포와 조직의 정량 영상

오가노이드(세포를 입체적으로 배양해 장기의 일부 구조와 기능을 재현한 모형)와 조직의 연속 영상을 얻고 구조 변화를 정량화한다. 가상 염색(염료를 처리해 얻는 모습에 대응하는 영상을 계산으로 만드는 기술)도 개발 방향이다.[^research] 대표 논문 5는 염색하지 않은 두꺼운 암 조직의 굴절률 영상에서 입체 가상 염색 영상을 만드는 방법을 제시했다. 대표 논문 6은 세포의 모양과 세포가 주변에 가하는 힘을 함께 재는 현미경을 개발했다.[^p5][^p6]

### 4. 정량 측정으로 밝히는 생물물리와 빛을 이용한 계산

세포 안의 응축체(막 없이 특정 생체분자들이 선택적으로 모여 주변과 구분되는 구조)의 질량 밀도(단위 부피당 질량)를 측정해 형성 원리를 연구한다. 대표 논문 7은 일부 응축체의 전체 질량 농도가 주변과 비슷할 수 있고 RNA가 그 밀도를 조절한다는 결과를 제시했다. RNA는 Ribonucleic Acid(리보핵산)의 줄임말이다.[^p7] 별도로, 빛이 산란하는 장치를 저장소 계산(입력의 시간 이력을 장치 내부의 동적 상태에 반영하고 그 상태를 읽어 출력을 학습하는 계산 방식)에 사용해 장치의 제어 변수와 계산 성능 사이의 관계를 정량화했다.[^p8]

## 대표 논문

KAIST 재직 시기의 2021–2026년 논문에서 광학 측정·산란 이론·소자 계측·생물물리·물리 계산의 갈래를 고르게 골랐다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 교수 역할은 저자 순서이며 교신저자 표시를 뜻하지 않는다.

| 번호 | 연도 | 논문 | 쉽게 말하면 | 주요 저자·교수 역할 |
|---|---|---|---|---|
| 1 | 2023 | [Non-interferometric stand-alone single-shot holographic camera using reciprocal diffractive imaging](https://doi.org/10.1038/s41467-023-40019-0)[^p1] | 한 장의 빛 세기 영상에서 산란한 빛의 진폭과 위상을 복원하는 센서를 제시하고, 물체가 멈추거나 움직이는 조건에서 입체 영상을 보였다. | 첫 저자 Jeonghun Oh, 박용근 마지막 저자 |
| 2 | 2025 | [Extending Rytov approximation to vector waves for tomography of anisotropic materials](https://doi.org/10.1103/physrevlett.134.068101)[^p2] | 빛의 방향 성분을 다루도록 산란 이론을 확장해 액정 내부의 입체 배열과 결함 구조를 시각화했다. | 첫 저자 ChulMin Oh, 박용근 마지막 저자 |
| 3 | 2026 | [Speckle-based X-ray microtomography via preconditioned Wirtinger flow](https://doi.org/10.1038/s41377-025-02118-z)[^p3] | 빛의 불규칙한 무늬를 이용하는 X선 단층 측정에 물리 모형과 기울기 기반 복원 계산을 결합해, 추가 측정이나 시료에 대한 가정 없이 정량 위상을 구하는 방법을 제시했다. | 첫 저자 KyeoReh Lee, 박용근 마지막 저자 |
| 4 | 2024 | [Visualizing Three-Dimensional Anisotropic Molecular Orientation in Polarization Holographic Optical Elements via Dielectric Tensor Tomography](https://doi.org/10.1002/adom.202302346)[^p4] | 편광 홀로그래픽 소자 내부에서 분자 방향이 어떻게 반복해서 바뀌는지 입체적으로 복원하고 제작 조건에 따른 기록 무늬의 균일성을 살폈다. 편광은 빛의 진동 방향이 특정한 규칙을 갖는 성질이다. | 첫 저자 Juheon Lee, 박용근 마지막 저자 |
| 5 | 2025 | [Revealing 3D microanatomical structures of unlabeled thick tissues from cancer patients using holotomography and virtual H&E staining via deep learning](https://doi.org/10.1038/s41467-025-59820-0)[^p5] | 두꺼운 대장암 조직의 굴절률 입체 영상을 계산으로 가상 염색 영상으로 바꾸고, 화학 염색과 비교했다. 위암 조직에서도 반복성과 확장성을 평가했다. H&E는 Hematoxylin and Eosin으로, 헤마톡실린과 에오신을 사용하는 조직 염색이다. | 첫 저자 Juyeon Park, 박용근 마지막 저자 |
| 6 | 2024 | [High-resolution assessment of multidimensional cellular mechanics using label-free refractive-index traction force microscopy](https://doi.org/10.1038/s42003-024-05788-4)[^p6] | 세포의 모양·건조 질량과 표면을 따라 또는 표면에 수직으로 작용하는 힘을 동시에 재는 무표지 입체 측정법을 개발했다. | 첫 저자 Moosung Lee, 박용근 마지막 저자 |
| 7 | 2023 | [RNA-mediated demixing transition of low-density condensates](https://doi.org/10.1038/s41467-023-38118-z)[^p7] | 세포 안 응축체가 주변보다 전체 질량 농도가 높지 않아도 형성될 수 있음을 측정하고, RNA와 주변 세포 구조가 응축체의 밀도·형태에 미치는 영향을 밝혔다. | 첫 저자 Taehyun Kim, 박용근 6명 중 5번째 저자 |
| 8 | 2026 | [Design principles for light-scattering reservoir computing at the edge of chaos](https://doi.org/10.1002/adco.70012)[^p8] | 빛 산란 계산 장치의 동적 변화, 입력과 장치의 결합, 내부 연결을 조절하며 계산 성능이 좋아지는 조건을 찾고 시계열(시간 순서대로 기록한 자료) 예측과 음성 분류로 시험했다. | 첫 저자 Peter Geon Kim, 박용근 마지막 저자 |

## 교수와 전문 분야

박용근 교수는 서울대학교 기계공학 학사(2004), MIT 기계공학 석사(2007), Harvard-MIT Health Science & Technology의 의학물리·의공학 박사(2010) 학위를 받았으며, 2010년부터 KAIST에서 조교수·부교수·교수로 재직했다.[^dept] 연구실 교수 소개는 KAIST 물리학과 기금석좌교수, Virtual 3D Biology Center 소장, Optica Fellow·SPIE Fellow, Tomocube 공동창업자·CEO와 TheWaveTalk 공동창업자·고문으로 적는다.[^people]

최근 논문에서 드러나는 전문 분야는 빛의 진폭·위상을 복원하는 영상 장치,[^p1] 방향에 따라 성질이 다른 재료의 산란 이론과 입체 계측,[^p2][^p4] 세포·조직의 정량 영상 및 힘 측정,[^p5][^p6] 세포 응축체의 생물물리 분석,[^p7] 빛의 산란을 이용한 물리 계산이다.[^p8]

## 응용 분야

연구실은 세포·오가노이드의 장기 관찰, 병리 조직의 입체 가상 염색, 생식세포와 배아의 비침습적 평가를 응용 방향으로 든다. 비침습적 평가는 대상을 절개하거나 내부에 기구를 넣는 등의 손상 없이 평가하는 것을 뜻한다.[^research] 산업에서는 투명한 유리 구조와 반도체 접합면의 결함 검사, 광학 소자 내부에 기록된 분자 배열 측정을 목표로 한다.[^industry][^p4]

## 구성원

2026년 11월 7일 연구실 People 기준으로 박사후연구원 4명, 대학원생 16명, 학부생 7명이다. 시작은 누리집의 계절·연도 표기이며 대학원생은 석사·박사 과정을 나누지 않은 게시 구분을 따른다.[^people] ‘대표 논문 참여’는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| WeiSun Park | 박사후연구원 | Fall 2017 |  |
| Geon Kim | 박사후연구원 | Spring 2023 | 5 |
| Hervé Hugonnet | 박사후연구원 | Spring 2024 |  |
| ChungHa Lee | 박사후연구원 | Fall 2024 |  |
| Dohyeon Lee | 대학원생 | Spring 2021 |  |
| Juyeon Park | 대학원생 | Spring 2021 | 5 |
| Juheon Lee | 대학원생 | Fall 2021 | 2, 4 |
| Chulmin Oh | 대학원생 | Fall 2022 |  |
| Minwook Kim | 대학원생 | Spring 2024 |  |
| Jupyo Hong | 대학원생 | Spring 2024 |  |
| Jimin Cho | 대학원생 | Fall 2024 |  |
| Sehyeon Lee | 대학원생 | Spring 2025 |  |
| MinSu Kim | 대학원생 | Spring 2025 |  |
| Siwon Jeong | 대학원생 | Spring 2025 |  |
| Sangmin Lee | 대학원생 | Spring 2025 |  |
| Yung Kang | 대학원생 | Fall 2025 |  |
| Seungbaek Lim | 대학원생 | Spring 2026 |  |
| Chanhee Park | 대학원생 | Spring 2026 |  |
| Hajin Kim | 대학원생 | Spring 2026 |  |
| Taejung Moon | 대학원생 | Fall 2026 |  |
| Kyuree Kim | 학부 연구생 |  |  |
| Samuel Dawit Assefa | 학부 연구생 |  |  |
| Arian Ahmed | 학부 연구생 |  |  |
| Geonwoo Lee | 학부 연구생 |  |  |
| Donggeon Lee | 학부 연구생 |  |  |
| Hyunseo Han | 학부 연구생 |  |  |
| Mamo Abel Demlie | 학부 연구생 |  |  |

## 졸업생과 과거 구성원

연구실 People의 Alumni에 적힌 70명이다. 연구교수·박사후연구원·대학원생·연구보조원·학부생과 Undergraduate Students의 Others 구획을 포함한다. 학위·과정 칸은 당시 구획 이름이며 개별 학위 취득을 뜻하지 않는다. 괄호 안 기간과 진로는 누리집 표기다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| HyunJoo Park | 연구교수 (2013 Spring – 2015 Spring) | KB Investment, Korea |
| Eun Seok Choi | 연구교수 (2021 Fall – 2022 Winter) | Areumteunteun Orthopedic Clinic, Korea |
| Sanjit Debnath | 박사후연구원 (2011 Spring – 2012 Spring) | Visiting Scientist, Raja Ramanna Centre for Advanced Technology (RRCAT), India |
| Youngchan Kim | 박사후연구원 (2011 Summer – 2013 Summer) | Lecturer in Quantum Biology, University of Surrey, UK |
| Jaeduck Jang | 박사후연구원 (2011 Fall – 2013 Spring) | Senior Researcher, Samsung Advanced Institute of Technology (SAIT), Korea |
| Chungil Ha | 박사후연구원 (2013 Spring – 2014 Spring) | Postdoc, Department of Physics, UNIST, Korea |
| Jonghee Yoon | 박사후연구원 (2014 Spring – 2016 Spring) | Associate Professor, Department of Physics, Ajou University, Korea |
| YoonSeok Baek | 박사후연구원 (2014 Summer – 2021 Summer) | Researcher, Laboratoire Kastler Brossel, Paris |
| Seungwoo Shin | 박사후연구원 (2014 Summer – 2022 Spring) | Group Leader (from 2027), Max Planck Institute for Dynamics and Self-Organization (MPI-DS), Germany |
| KyeoReh Lee | 박사후연구원 (2018 Spring – 2024 Spring) | Research Staff, Department of Physics, Yale University, USA |
| Jung Hoon Park | 대학원생 (2011 Spring – 2014 Spring) | Professor, Biomedical Engineering (Bio-Optics Lab), UNIST, Korea |
| GwangSik Park | 대학원생 (2015 Summer – 2016 Winter) | Samsung Electronics, Korea |
| Kyoohyun Kim | 대학원생 (2011 Summer – 2017 Spring) | Head, Core Microscopy Facility, Max-Planck-Zentrum für Physik und Medizin, Germany |
| Hyeonseung Yu | 대학원생 (2011 Summer – 2017 Spring) | Professor, Electronic and Electrical Engineering, Sungkyunkwan University, Korea |
| JunTaek Oh | 대학원생 (2016 Summer – 2018 Spring) | Samsung Electronics, Korea |
| Jaehwang Jeong | 대학원생 (2012 Summer – 2018 Spring) | Samsung Electronics, Korea |
| Jongchan Park | 대학원생 (2013 Summer – 2019 Spring) | Staff Research Scientist, UCLA, USA |
| SangYun Lee | 대학원생 (2013 Summer – 2019 Summer) | Samsung Advanced Institute of Technology (SAIT), Korea |
| Taean Chang | 대학원생 (2018 Spring – 2020 Spring) |  |
| Moosung Lee | 대학원생 (2016 Fall – 2023 Spring) | Postdoc, University of Stuttgart, Germany |
| Jeonghun Oh | 대학원생 (2018 Spring – 2024 Spring) | Samsung Electronics, Korea |
| Chansuk Park | 대학원생 (2017 Spring – 2024 Spring) | Samsung Electro-Mechanics, Korea |
| Jeapil Jo | 대학원생 (2022 Spring – 2024 Spring) | Samsung Electronics, Korea |
| Youngmoon Cho | 대학원생 (2021 Fall – 2022 Summer) |  |
| Mahn Jae Lee | 대학원생 (2019 Spring – 2024 Fall) | Professor, Biochemistry, Chungnam National University Hospital (CNUH), Korea |
| Tal Lifshitz | 대학원생 (2023 Fall – 2026 Summer) | Ph.D. student, Biophysics, Cornell University, USA |
| Donghun Ryu | 연구보조원 | Ph.D. Candidate, EECS, MIT, USA |
| Hansol Yoon | 연구보조원 | Ph.D. Candidate, ECE, Georgia Tech, USA |
| Sangyeon Cho | 학부생 | Assistant Professor, Bioengineering, Rice University, USA |
| YoungJu Jo | 학부생 | Assistant Professor, EECS, UC Berkeley, USA |
| Minho Choe | 학부생 | Assistant Professor, Electrical Engineering, UNIST, Korea |
| Seo Eun Lee | 학부생 | Eli Lilly and Company, USA |
| Seong Ha Park | Undergraduate Students / Others |  |
| Joonseok Hur | Undergraduate Students / Others |  |
| KyungDuk Kim | Undergraduate Students / Others |  |
| Jinyeop Song | Undergraduate Students / Others |  |
| Ariel J. Lee | Undergraduate Students / Others |  |
| SeungYoon Han | Undergraduate Students / Others |  |
| Dao Khoi | Undergraduate Students / Others |  |
| Heesoo Byun | Undergraduate Students / Others |  |
| Soomin Kim | Undergraduate Students / Others |  |
| Yunhun Jang | Undergraduate Students / Others |  |
| Hye-Ok Yoon | Undergraduate Students / Others |  |
| Jeeun Lee | Undergraduate Students / Others |  |
| Gyu Young Chang | Undergraduate Students / Others |  |
| Ji Han Heo | Undergraduate Students / Others |  |
| Seolhui Jeon | Undergraduate Students / Others |  |
| Sanghyun Kim | Undergraduate Students / Others |  |
| Shinhwa Lee | Undergraduate Students / Others |  |
| JaeHyeon Park | Undergraduate Students / Others |  |
| Su-A Yang | Undergraduate Students / Others |  |
| Gwang-su Kim | Undergraduate Students / Others |  |
| In-Hyuck Choi | Undergraduate Students / Others |  |
| Doyeon Kim | Undergraduate Students / Others |  |
| Gyuwon Lee | Undergraduate Students / Others |  |
| Haechan Kwak | Undergraduate Students / Others |  |
| Chanwoo Song | Undergraduate Students / Others |  |
| Yeongjin Yu | Undergraduate Students / Others |  |
| Jaehyu Shim | Undergraduate Students / Others |  |
| Hayeon Cho | Undergraduate Students / Others |  |
| Young Seo Kim | Undergraduate Students / Others |  |
| Abbas Abbasli | Undergraduate Students / Others |  |
| HyunJun Han | Undergraduate Students / Others |  |
| Kaleb Mesfin Asfaw | Undergraduate Students / Others |  |
| Benedict Reve Delmo | Undergraduate Students / Others |  |
| Biruk Zewdu | Undergraduate Students / Others |  |
| Yoonjae Chung | Undergraduate Students / Others |  |
| Minseok Lee | Undergraduate Students / Others |  |
| Jinyoung Kim | Undergraduate Students / Others |  |
| Siraj Yahyazade | Undergraduate Students / Others |  |

## 최근 5년 논문 목록

연구실 Publications의 2021–2026년 구역에서 옮긴 66편이다. 제목·저자·발표처와 연도 구역은 누리집 표기를 따르며 ‘연구실 기재’는 해당 목록의 arXiv·bioRxiv 표기다. DOI 또는 게시 링크를 함께 적었다.[^pubs]

**2026**

- D. M. Ryu, J. H. Roh, W. S. Lee, H. Yoon, H. S. Min, and Y. K. Park. "Numerical-aperture transfer in holotomography with a deterministic diffusion prior". *arXiv , 2026 (연구실 기재)*.
- M. Kim, C. Lee, J. Do, T. Shin, D. Iliev, K. H. Choi, S. Y. Shin, J. Ko, T. Popa, C. Hickman, J. H. Kim, and Y. K. Park. "Holotomography reveals biophysical remodeling of mouse oocytes during post-ovulatory aging". *bioRxiv , 2026 (연구실 기재) · https://doi.org/10.64898/2026.06.18.733271 [^supp-b01]*.
- H. Hugonnet, J. Choi, G. H. Kim, C. Oh, J. Cho, C. Lee, S. J. Shin, S. Park, B. K. Koo, W. Y. Oh, P. Kim, and Y. K. Park. "Programmable spatial coherence tomography: diffraction-limited three-dimensional reflection imaging under modulated monochromatic illumination". *arXiv , 2026 (연구실 기재) · https://arxiv.org/abs/2605.05747*.
- Y. Chung, S. Lee, H. Hugonnet, C. Oh, W. Park, Y. W. Kim, S.-M. Hong, and Y. K. Park. "Quantitative three-dimensional absorption imaging in standard brightfield microscopes". *arXiv , 2026 (연구실 기재) · https://arxiv.org/abs/2601.15925*.
- Y. K. Park. "Holotomography in 2025: From Morphometric Imaging to AI-Driven Multimodal Phenotyping". *arXiv , 2026 (연구실 기재) · https://arxiv.org/abs/2601.02611*.
- G. Kim and Y. K. Park. "Design principles for light-scattering reservoir computing at the edge of chaos". *Advanced Computing , 2026 · https://doi.org/10.1002/adco.70012*.
- J. Cho, H. Lee, C. Oh, J. Park, S. Park, B. K. Koo, and Y. K. Park. "Label-Free 4D Holotomography with Depth-Adaptive Segmentation for Quantitative Analysis of Lipid Droplet Dynamics in Hepatic Organoids". *Biophotonics Discovery , 2026 · https://doi.org/10.1117/1.BIOS.3.3.035005*.
- M. Kim, C. Park, C. Oh, K. R. Lee, H. Hugonnet, and Y. K. Park. "Video-rate wavefront capture and replay via single-shot reference-free measurement: toward holographic telepresence". *Opto-Electronic Advances , 2026 · https://doi.org/10.29026/oea.2026.260001*.
- D. Lee, J. Park, J. Lee, C. Lee, and Y. K. Park. "Compression benchmarking of holotomography data using the OME-Zarr storage format". *PLoS ONE , 2026 · https://doi.org/10.1371/journal.pone.0351560*.
- M. Lee, T. Lifshitz, Y. K. Lee, G. Kim, S. Y. Park, H. Lee, J. Park, E. K. Lee, and Y. K. Park. "Refractive index-correlated pseudocoloring for adaptive color fusion in holotomographic cytology". *Cytometry Part A , 2026 · https://doi.org/10.1002/cyto.a.70041*.
- C. M. Oh, J. Cho, J. Park, H. Lee, and Y. K. Park. "Morphology-Preserving Holotomography: Quantitative Analysis of 3D Organoid Dynamics". *IEEE Transactions on Medical Imaging , 2026 · https://doi.org/10.1109/tmi.2026.3698497*.
- J. Lee, Y. W. Kim, H. Chang, H. Hugonnet, C. Oh, S. Lee, S.-M. Hong, S. Jeon, and Y. K. Park. "Incoherent dielectric tensor tomography for quantitative 3D measurement of biaxial anisotropy". *Nature Photonics , 2026 · https://doi.org/10.1038/s41566-026-01897-0*.
- K. R. Lee, H. Hugonnet, J.-H. Lim, and Y. K. Park. "Speckle-based X-ray microtomography via preconditioned Wirtinger flow". *Light: Science & Applications , 2026 · https://doi.org/10.1038/s41377-025-02118-z*.

**2025**

- H. Hugonnet, K. R. Lee, S. Jo, J. Lim, and Y. K. Park. "Quantitative X-ray Schlieren Nanotomography for Hyperspectral Phase and Absorption Imaging". *arXiv , 2025 (연구실 기재) · https://arxiv.org/abs/2504.20537*.
- D. Lee, H. S. Lee, M. Lee, M. Kang, G. Kim, T. Y. Kim, N. Y. Lee, and Y. K. Park. "Advances in imaging techniques for the study of individual bacteria and their pathophysiology". *arXiv , 2025 (연구실 기재) · https://arxiv.org/abs/2501.01592*.
- H. Yu, M. Kim, and Y. K. Park. "Synthetic aperture enhances virtual reality displays". *Nature Photonics , 2025 · https://doi.org/10.1038/s41566-025-01721-1*.
- T. Zhong, H. Huang, H. Li, Y. K. Park, and P. Lai. "Redefining frontiers of computational imaging with deep learning". *Photonics Insights , 2025 · https://doi.org/10.3788/pi.2025.c04*.
- T. Lifshitz, S.-J. Shin, J. Park, K. S. Lee, and Y. K. Park. "Label-Free 3D Virtual Staining of Urine Cytology Using Holotomography and GAN-Based Deep Learning". *In Proceeding of Digital Medicine and Image Processing , 2025 · https://doi.org/10.1145/3785443.3785444*.
- J. Hong, H. Hugonnet, C. M. Oh, W. S. Park, C. Lee, C. Lee, Y. W. Kim, W. Heo, S.-M. Hong, and Y. K. Park. "High-speed holotomography of live cells and tissues using multi-pattern sparse axial scanning". *Optics Express , 2025 · https://doi.org/10.1364/oe.577207*.
- K. PD, L. KR, H. Y, S. S, L. S, H. DS, and P. YK. "3D Fourier transformation light scattering for reconstructing extend angled resolved light scattering of individual particles". *Current Optics and Photonics , 2025 · https://arxiv.org/abs/2102.04021*.
- J. Oh, H. Hugonnet, W. Park, and Y. K. Park. "Generalized reciprocal diffractive imaging for stand-alone, reference-free, fast-measurable quantitative phase microscopy". *Communications Physics , 2025 · https://doi.org/10.1038/s42005-025-02292-x*.
- H. Hugonnet, C. M. Oh, J. Park, and Y. K. Park. "Pupil phase series: a fast, accurate, and energy-conserving model for forward and inverse light scattering in thick biological samples". *Optics Express , 2025 · https://doi.org/10.1364/oe.568019*.
- C. Lee, J. Yu, J. Shin, J. Yu, Y. Heo, M. Lee, D. Yu, Y. K. Park, and W. D. Heo. "Optogenetic storage and release of protein and mRNA in live cells and animals". *Nature Communications , 2025 · https://doi.org/10.1038/s41467-025-61322-y*.
- J. Cho, M. J. Lee, J. Park, J. Lee, S. Lee, C. Chung, B. K. Koo, and Y. K. Park. "Label-free, High-Resolution, and 3D Imaging and Analysis of Intestinal Organoids using Low-Coherence Holotomography with Machine Learning". *Journal of Visualized Experiments , 2025 · https://doi.org/10.3791/68529 [^supp-b06]*.
- J. Park. "Revealing 3D microanatomical structures of unlabeled thick tissues from cancer patients using holotomography and virtual H&E staining via deep learning". *Nature Communications , 2025 · https://doi.org/10.1038/s41467-025-59820-0*.
- C. M. Oh, H. Hugonnet, J. Lee, and Y. K. Park. "Extending Rytov approximation to vector waves for tomography of anisotropic materials". *Physical Review Letters , 2025 · https://doi.org/10.1103/PhysRevLett.134.068101*.
- C. M. Oh, H. Hugonnet, M. Lee, and Y. K. Park. "Digital aberration correction for enhanced thick tissue imaging exploiting aberration matrix and tilt-tilt correlation in optical memory effect". *Nature Communications , 2025 · https://doi.org/10.1038/s41467-025-56865-z*.
- J. Jo, H. Hugonnet, M. J. Lee, and Y. K. Park. "Digital cytometry: extraction of forward and side scattering signals from holotomography". *Journal of Biophotonics , 2025 · https://doi.org/10.1002/jbio.202400387*.
- D. Lee, M. Lee, B. Yerezhep, M. Kim, H. Hugonnet, S. Jeon, J. Shin, and Y. K. Park. "Fast free-form phase mask design for three-dimensional photolithography using convergent Born series". *ACS Photonics , 2025 · https://doi.org/10.1021/acsphotonics.4c01201*.

**2024**

- E. Y. Jeong, H. J. Kim, S. Lee, Y. K. Park, and Y. M. Kim. "Three-dimensional Label-Free Measurements of Adipocyte Differentiation and Lipid Droplet Dynamics". *Journal of the Optical Society of America A , 2024 · https://doi.org/10.1364/josaa.528703*.
- S. K. Kang, K. Kim, J. Jeong, S. Hong, Y. K. Park, and J. Shin. "In silico full-angle high–dynamic range scattering of microscopic objects exploiting holotomography". *Biomedical Optics Express , 2024 · https://doi.org/10.1364/boe.528698*.
- J. Rosen. "Roadmap on Computational Methods in Optical Imaging and Holography". *Applied Physics B , 2024 · https://doi.org/10.1007/s00340-024-08280-3 [^roadmap]*.
- J. Lee, B. G. Chae, H. Kim, M. S. Yoon, H. Hugonnet, and Y. K. Park. "High-precision and low-noise dielectric tensor tomography using a micro-electromechanical system mirror". *Optics Express , 2024 · https://doi.org/10.1364/oe.525489*.
- Y. Chung, H. Hugonnet, S.-M. Hong, and Y. K. Park. "Fourier space aberration correction for high resolution refractive index imaging using incoherent light". *Optics Express , 2024 · https://doi.org/10.1364/oe.518479*.
- J. Jo, D. Baek, H. Hugonnet, K. Kim, H. Ji, Y. Lim, T. Kim, S. Lee, and Y. K. Park. "Three-dimensional measurements and characterizations of refractive index distributions of volume holographic gratings using low-coherence holotomography". *Advanced Optical Materials , 2024 · https://doi.org/10.1002/adom.202302048*.
- J. Lee, H. Son, S. J. Hong, H. Hugonnet, J. Bang, S. Lee, and Y. K. Park. "Visualizing Three-Dimensional Anisotropic Molecular Orientation in Polarization Holographic Optical Elements via Dielectric Tensor Tomography". *Advanced Optical Materials , 2024 · https://doi.org/10.1002/adom.202302346*.
- H. Kim, S. Oh, S. Lee, K. S. Lee, and Y. K. Park. "Recent advances in label-free imaging and quantification techniques for the study of lipid droplets in cells". *Current Opinion in Cell Biology , 2024 · https://doi.org/10.1016/j.ceb.2024.102342 [^supp-b09]*.
- M. Lee, H. Jeong, C. Lee, M. J. Lee, B. R. Delmo, W. D. Heo, J. H. Shin, and Y. K. Park. "High-resolution assessment of multidimensional cellular mechanics using label-free refractive-index traction force microscopy". *Communications Biology , 2024 · https://doi.org/10.1038/s42003-024-05788-4*.

**2023**

- H. H, H. HJ, P. W, and P. YK. "Improving specificity and axial spatial resolution of refractive index imaging by exploiting uncorrelated subcellular dynamics". *ACS Photonics , 2023 · https://doi.org/10.1021/acsphotonics.3c01236*.
- J. Park, B. Bai, D. H. Ryu, T. Liu, C. Lee, Y. Luo, M. J. Lee, L. Huang, J. Shin, Y. Zhang, D. Ryu, Y. Li, G. Kim, H.-S. Min, A. Ozcan, and Y. K. Park. "Artificial intelligence-enabled quantitative phase imaging methods for life sciences". *Nature Methods , 2023 · https://doi.org/10.1038/s41592-023-02041-4 [^supp-b12]*.
- H. Hugonnet, M. Lee, S. Shin, and Y. K. Park. "Vectorial inverse scattering for dielectric tensor tomography: overcoming challenges of reconstruction of highly scattering birefringent samples". *Optics Express , 2023 · https://doi.org/10.1364/oe.494773*.
- J. Oh, H. Hugonnet, and Y. K. Park. "Non-interferometric stand-alone single-shot holographic camera using reciprocal diffractive imaging". *Nature Communications , 2023 · https://doi.org/10.1038/s41467-023-40019-0*.
- A. J. Lee, H. Hugonnet, Y. S. Kim, J.-G. Kim, M. Lee, T. Ku, and Y. K. Park. "Volumetric refractive index measurement and quantitative density analysis of mouse brain tissue with sub-micrometer spatial resolution". *Advanced Photonics Research , 2023 · https://doi.org/10.1002/adpr.202300112*.
- J. Lee, M. Lee, Y. K. Park, C. Ophus, and Y. Yang. "Multislice electron tomography using four-dimensional scanning transmission electron microscopy". *Physical Review Applied , 2023 · https://doi.org/10.1103/PhysRevApplied.19.054062*.
- T. Kim, J. Yoo, S. Do, D. S. Hwang, Y. K. Park, and Y. Shin. "RNA-mediated demixing transition of low-density condensates". *Nature Communications , 2023 · https://doi.org/10.1038/s41467-023-38118-z*.
- J. Oh, H. Hugonnet, and Y. K. Park. "Quantitative phase imaging via the holomorphic property of complex optical fields". *Physical Review Research , 2023 · https://doi.org/10.1103/PhysRevResearch.5.L022014*.
- C. Lee, H. Hugonnet, J. Park, M. J. Lee, W. Park, and Y. K. Park. "Single-shot refractive index slice imaging using spectrally multiplexed optical transfer function reshaping". *Optics Express , 2023 · https://doi.org/10.1364/oe.485559*.
- K. R. Lee, J. Lim, S. Y. Lee, and Y. K. Park. "Direct high-resolution X-ray imaging exploiting pseudorandomness". *Light: Science & Applications , 2023 · https://doi.org/10.1038/s41377-023-01124-3*.
- K. R. Lee, J. Lim, and Y. K. Park. "Full-field quantitative X-ray phase nanotomography via space-domain Kramers–Kronig relations". *Optica , 2023 · https://doi.org/10.1364/optica.481451*.
- K. R. Lee, J. Lim, and Y. K. Park. "Pulse-to-pulse field characterization at X-ray free-electron lasers using a speckle-correlation scattering matrix". *Optica , 2023 · https://doi.org/10.1364/optica.483836*.
- M. Lee, H. Hugonnet, M. J. Lee, Y. Cho, and Y. K. Park. "Optical trapping with holographically structured light for single-cell studies". *Biophysics Reviews , 2023 · https://doi.org/10.1063/5.0111104*.
- H. H, S. S, and P. YK. "Regularization of dielectric tensor tomography using total variation". *Optics Express , 2023 · https://doi.org/10.1364/oe.478260*.
- J. Shin, G. Kim, J. Park, M. Lee, and Y. K. Park. "Long-term label-free assessments of individual bacteria using three-dimensional quantitative phase imaging and hydrogel-based immobilization". *Scientific Reports , 2023 · https://doi.org/10.1038/s41598-022-27158-y*.

**2022**

- C. M. Oh, H. J. Ma, K. R. Lee, D. K. Kim, and Y. K. Park. "Non-resonant lasing in a deep-hole scattering cavity". *Optics Express , 2022 · https://doi.org/10.1364/oe.475610*.
- L. J, S. S, H. H, and P. YK. "Spatially multiplexed dielectric tensor tomography". *Optics Letters , 2022 · https://doi.org/10.1364/ol.474969*.
- Z. Yu, H. Li, T. Zhong, J.-H. Park, S. Cheng, C. M. Woo, Q. Zhao, J. Yao, Y. Zhou, X. Huang, W. Pang, H. Yoon, Y. Shen, H. Liu, Y. Zheng, Y. K. Park, L. V. Wang, and P. Lai. "Wavefront shaping: a versatile tool to conquer multiple scattering in multidisciplinary fields". *The Innovation , 2022 · https://doi.org/10.1016/j.xinn.2022.100292*.
- H. Hugonnet, M. J. Lee, and Y. K. Park. "Quantitative phase and refractive index imaging of 3D objects via optical transfer function reshaping". *Optics Express , 2022 · https://doi.org/10.1364/oe.454533*.
- Y. Choi, M. K. Kim, C. H. Park, J. Park, Y. K. Park, and Y.-H. Cho. "Wide-field super-resolution optical fluctuation imaging through dynamic near-field speckle illumination". *Nano Letters , 2022 · https://doi.org/10.1021/acs.nanolett.1c03691*.
- J. Rosen, H. B. Aguiar, V. Anand, Y. S. Baek, S. Gigan, R. Horisaki, H. Hugonnet, S. Juodkazis, K. R. Lee, H. Liang, Y. Liu, S. Ludwig, W. Osten, Y. K. Park, G. Pedrini, T. Sarkar, J. Schindler, A. K. Singh, R. K. Singh, G. Situ, M. Takeda, X. Xie, W. Yang, and J. Zhou. "Roadmap on chaos-inspired imaging technologies (CI2-Tech)". *Applied Physics B , 2022 · https://doi.org/10.1007/s00340-021-07729-z*.
- S. Shin, J. Eun, S. S. Lee, C. Lee, H. Hugonnet, D. K. Yoon, S.-H. Kim, J. Jeong, and Y. K. Park. "Tomographic measurements of dielectric tensors at optical frequency". *Nature Materials , 2022 · https://doi.org/10.1038/s41563-022-01202-8*.
- C. Lee, Y. Baek, H. Hugonnet, and Y. K. Park. "Single-shot wide-field topography measurement using spectrally multiplexed reflection intensity holography via space-domain Kramers-Kronig relations". *Optics Letters , 2022 · https://doi.org/10.1364/ol.446159*.
- M. Lee, H. Hugonnet, and Y. K. Park. "Inverse problem solver for multiple light scattering using modified Born series". *Optica , 2022 · https://doi.org/10.1364/optica.446511*.

**2021**

- M. Son, Y. S. Lee, M. J. Lee, Y. K. Park, H.-R. Bae, S. Y. Lee, M.-G. Shin, and S. Yang. "Effects of osmolality and solutes on the morphology of red blood cells according to three-dimensional refractive index tomography". *PLOS ONE , 2021 · https://doi.org/10.1371/journal.pone.0262106*.
- J. Oh, K. R. Lee, and Y. K. Park. "Single-Shot Reference-Free Holographic Imaging using a Liquid Crystal Geometric Phase Diffuser". *Laser & Photonics Reviews , 2021 · https://doi.org/10.1002/lpor.202100559*.
- B. V, K. M, A. C, A. V, C. CJ, D. C, H. N, J. S, K. J, K. A, L. M, M. P, M. P, N. SH, R. J, P. YK, and Z. M. "Roadmap on Digital Holography-Based Quantitative Phase Imaging". *Journal of Imaging , 2021 · https://doi.org/10.3390/jimaging7120252*.
- Y. J. Jo, H. Cho, W. S. Park, G. Kim, D. H. Ryu, Y. S. Kim, M. Lee, S. Park, M. J. Lee, H. Joo, H. H. Jo, S. Lee, S. Lee, H.-S. Min, W. D. Heo, and Y. K. Park. "Label-free multiplexed microtomography of endogenous subcellular dynamics using generalizable deep learning". *Nature Cell Biology , 2021 · https://doi.org/10.1038/s41556-021-00802-x [^supp-b16]*.

## 수상과 선정

2021년 10월 13일–2026년 10월 13일의 연구실 News에 적힌 수상 1건이다.[^news]

- 2022-09-06 · Youngju Jo가 일반화 가능한 딥러닝을 이용한 무표지 다중 미세 단층영상 연구로 2022 Agarwal Award를 받았다.

## 소식

같은 기간의 연구실 News에 적힌 논문 게재·게재 승인 소식 5건이다.[^news]

- 2026-10-07 · Geon Kim·YongKeun Park의 빛 산란 기반 저장소 계산 설계 원리 논문이 Advanced Computing 게재 승인을 받았다.
- 2026-08-13 · 단일 측정으로 파면을 영상 속도로 기록·재생하는 홀로그래피 논문이 Opto-Electronic Advances에 게재되었다.
- 2023-10-24 · 생명과학용 정량 위상 영상과 인공지능의 결합을 다룬 관점 글(perspective)이 Nature Methods에 게재되었다.
- 2022-03-08 · 광학 주파수에서 유전율 텐서를 단층 측정하는 논문이 Nature Materials에 게재되었다.
- 2022-02-22 · 단일 측정으로 넓은 영역의 표면 높이를 재는 논문이 Optics Letters에 게재되었다.

## 연락과 위치

- 교수 전화: +82-42-350-2514.[^dept][^people]
- 교수 사무실: E6-6 #305.[^dept]
- 주소: 대전광역시 유성구 대학로 291, KAIST 물리학과, 우편번호 34141.[^dept]
[^dept]: KAIST 물리학과, Park, YongKeun (박용근) 교수 소개, Position·Educations·Experiences·LAB·Office·Tel. <https://physics.kaist.ac.kr/index.php?document_srl=314&mid=p_people1> 관측일 2026-11-07.
[^research]: Biomedical Optics Laboratory, Research, 연구 소개와 네 연구 영역. <https://bmol.kaist.ac.kr/research/> 관측일 2026-11-07.
[^methods]: Biomedical Optics Laboratory, Research, “Label-Free 3D Imaging of Living Matter”, 광학계·조명·재구성 방법 개발과 정량 위상 영상. <https://bmol.kaist.ac.kr/research/> 관측일 2026-11-07.
[^holo]: Biomedical Optics Laboratory, Research, “Seeing Inside What Manufacturing Builds”, 복소 광학장 복원·파면 제어·굴절률 입체 구조와 계산 영상 개발. <https://bmol.kaist.ac.kr/research/> 관측일 2026-11-07.
[^industry]: Biomedical Optics Laboratory, Research, “Seeing Inside What Manufacturing Builds”, 반도체·디스플레이 구조와 접합면을 위한 광학 측정·공동 복원 방법 개발. <https://bmol.kaist.ac.kr/research/> 관측일 2026-11-07.
[^people]: Biomedical Optics Laboratory, People, 교수·현재 구성원·Alumni. <https://bmol.kaist.ac.kr/people/> 관측일 2026-11-07.
[^pubs]: Biomedical Optics Laboratory, Publications, 2021–2026년 연도 구역. <https://bmol.kaist.ac.kr/publications/> 관측일 2026-11-07.
[^news]: Biomedical Optics Laboratory, News, 논문 게재·수상 소식. <https://bmol.kaist.ac.kr/news/> 관측일 2026-11-07.
[^p1]: J. Oh, H. J. Hugonnet, Y. Park, Nature Communications (2023). <https://doi.org/10.1038/s41467-023-40019-0> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5057256024,publication_year:2021-2026> 관측일 2026-11-07.
[^p2]: C. Oh, H. J. Hugonnet, J. Lee, Y. Park, Physical Review Letters (2025). <https://doi.org/10.1103/physrevlett.134.068101> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5057256024,publication_year:2021-2026> 관측일 2026-11-07.
[^p3]: K. Lee, H. J. Hugonnet, J.-H. Lim, Y. Park, Light Science & Applications (2026). <https://doi.org/10.1038/s41377-025-02118-z> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5057256024,publication_year:2021-2026> 관측일 2026-11-07.
[^p4]: J. Lee 외, Y. Park, Advanced Optical Materials (2024). <https://doi.org/10.1002/adom.202302346> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5057256024,publication_year:2021-2026> 관측일 2026-11-07.
[^p5]: J. Park 외, Y. Park, Nature Communications (2025). <https://doi.org/10.1038/s41467-025-59820-0> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5057256024,publication_year:2021-2026> 관측일 2026-11-07.
[^p6]: M. Lee 외, Y. Park, Communications Biology (2024). <https://doi.org/10.1038/s42003-024-05788-4> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5057256024,publication_year:2021-2026> 관측일 2026-11-07.
[^p7]: T. Kim 외, Y. Shin, Nature Communications (2023). <https://doi.org/10.1038/s41467-023-38118-z> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5057256024,publication_year:2021-2026> 관측일 2026-11-07.
[^p8]: P. G. Kim, Y. Park, Advanced Computing (2026). <https://doi.org/10.1002/adco.70012> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5057256024,publication_year:2021-2026> 관측일 2026-11-07.
[^roadmap]: J. Rosen 외, Roadmap on computational methods in optical imaging and holography [invited], Applied Physics B 130, 166 (온라인 2024-08-29). Crossref 전체 저자 83명 중 YongKeun Park는 54번째 저자다. <https://api.crossref.org/works/10.1007/s00340-024-08280-3> 관측일 2026-11-07.
[^supp-b01]: Minsu Kim 외, YongKeun Park, bioRxiv, 2026. Holotomography reveals biophysical remodeling of mouse oocytes during post-ovulatory aging. <https://doi.org/10.64898/2026.06.18.733271> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=Holotomography%20reveals%20biophysical%20remodeling%20of%20mouse%20oocytes%20during%20post-ovulatory%20aging> 관측일 2026-11-07.
[^supp-b06]: Jimin Cho 외, YongKeun Park, Journal of Visualized Experiments, 2025. Label-free, High-Resolution, and 3D Imaging and Analysis of Intestinal Organoids using Low-Coherence Holotomography with Machine Learning. <https://doi.org/10.3791/68529> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.ceb.2024.102342%7C10.1038/s41380-025-03176-w%7C10.1038/s41556-021-00802-x%7C10.1038/s41592-023-02041-4%7C10.1038/s41598-024-75168-9%7C10.1038/s43586-024-00338-y%7C10.1080/1040841x.2026.2756947%7C10.1101/2022.05.18.492426%7C10.1101/2023.06.18.545499%7C10.1101/2023.08.21.554226%7C10.1101/2023.09.16.558039%7C10.3791/68529%7C10.64898/2026.06.18.733271> 관측일 2026-11-07.
[^supp-b09]: Hyeonwoo Kim 외, YongKeun Park, Current Opinion in Cell Biology, 2024. Recent advances in label-free imaging and quantification techniques for the study of lipid droplets in cells. <https://doi.org/10.1016/j.ceb.2024.102342> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.ceb.2024.102342%22> 관측일 2026-11-07.
[^supp-b12]: Juyeon Park 외, YongKeun Park, Nature Methods, 2023. Artificial intelligence-enabled quantitative phase imaging methods for life sciences. <https://doi.org/10.1038/s41592-023-02041-4> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1038/s41592-023-02041-4%22> 관측일 2026-11-07.
[^supp-b16]: YoungJu Jo 외, YongKeun Park, Nature Cell Biology, 2021. Label-free multiplexed microtomography of endogenous subcellular dynamics using generalizable deep learning. <https://doi.org/10.1038/s41556-021-00802-x> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1038/s41556-021-00802-x%22> 관측일 2026-11-07.

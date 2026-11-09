# 뇌역공학과 영상연구실 (Brain Reverse Engineering & Imaging Lab, BREIL)

**KAIST 전기및전자공학부 · 김대식 교수**

- 분야: 시각·언어 인공지능, 언어 모델 지시문 최적화, 영상 분할, 지식 증류, 환경 변화 적응, 3차원 표면 생성·편집, 뇌 영상 해석
- 대분야: 컴퓨팅·AI
- 태그: 컴퓨터 비전[^research], 멀티모달 AI[^research], 대형 언어 모델[^research], 모델 경량화·양자화[^research], 컴퓨터 그래픽스·기하 처리[^research], 생성 인공지능[^research], 신경영상 분석·뇌 연결망[^research]
- 홈페이지: <https://brain.kaist.ac.kr/>
- 근거와 출처: [뇌역공학과 영상연구실 근거 페이지](breil-sources.md)

> 사진 속 장면을 이해하고 그 판단을 글로 설명하는 인공지능을 연구하며, 모델을 작게 만드는 방법과 환경 변화에 적응하는 영상 처리, 뇌 영상과 언어를 연결하는 방법을 개발한다.[^home][^research]

## 무엇을 연구하나

BREIL은 김대식 교수가 이끄는 KAIST 전기및전자공학부 연구실이다. 계산을 통한 신경계 연구와 뇌 영상 연구에서 출발했으며, 현재 중심은 컴퓨터 비전(사진·영상에서 대상과 장면을 알아보고 화질을 복원하는 인공지능 분야)과 대형 언어 모델(Large Language Models, 많은 글을 학습해 언어를 이해하고 생성하는 인공지능 모델)을 연결하는 일이다. 연구실은 장면을 보고, 그 내용에 관해 추론하고, 판단을 언어로 설명하는 시스템을 만든다고 소개한다.[^home]

첫째로, 이미지와 글을 함께 다루는 멀티모달 인공지능(종류가 다른 자료를 함께 이해하고 처리하는 인공지능)을 개발한다.[^research] 사진과 문장이 가리키는 대상을 연결하고, 사진에 대한 설명문을 생성하며, 질문이 가리키는 영역을 나누는 영상 분할(영상의 각 위치를 대상이나 의미에 따라 구분하는 작업)을 연구한다.[^research] 하나의 질문이 여러 물체나 물체의 부분·전체를 가리킬 때 모델을 평가하는 자료를 만들고, 언어 모델이 자신의 지시문을 반복해서 개선하는 방법도 다룬다.[^research]

둘째로, 시각·언어 모델의 능력을 유지하면서 크기를 줄이는 지식 증류(교사 모델이 배운 정보를 학생 모델에 전달하는 학습 방법)를 개발한다.[^research] 표본의 난이도와 개별 자료의 특성에 맞추어 정보를 전달하는 방법이 여기에 속한다. 도메인 적응(학습 자료와 실제 적용 자료의 성질이 달라질 때 모델을 적응시키는 방법)도 주요 갈래다. 맑은 날에 학습한 영상 분할 모델이 안개 등 다른 날씨에서도 작동하게 하며, 조명과 영상 센서의 차이에 적응하는 방법을 연구한다.[^research]

셋째로, 문장에서 3차원 물체의 텍스처(표면의 색과 무늬를 나타내는 자료)를 생성하고, 여러 시점에서 보아도 색이 일관되게 바뀌는 장면 편집을 연구한다.[^research] 뇌 영상에서는 기능적 자기공명영상(functional Magnetic Resonance Imaging, fMRI, 혈액의 자기공명 신호 변화 등을 이용해 뇌 활동을 간접 측정하는 영상)을 언어와 연결하는 방법을 개발한다. 자기공명영상(Magnetic Resonance Imaging, MRI)은 자기장과 전자기파에 대한 원자핵의 반응을 이용해 몸속 정보를 영상으로 나타내는 기술이며, 신호는 관측하거나 전달하려는 정보를 나타내는 물리량이다. 연구실의 뇌 영상 설명문 생성 연구는 뇌 활동과 대응 문장을 함께 학습하고, 출력 단어에 어느 뇌 영역이 기여했는지 살펴보는 방법을 제시한다.[^research]

## 주요 연구 주제

### 1. 시각·언어 연결과 지시문 최적화

이미지 속 여러 대상과 부분·전체 수준을 함께 묻는 분할 평가 자료를 개발한다. MMR(Multi-target and Multi-granularity Reasoning) 연구는 모델이 여러 대상에 대한 질문에서 불필요한 영역을 추가하거나 부분과 전체를 혼동하는 문제를 분석한다. AIPO(Automatic Instruction Prompt Optimization) 연구는 언어 모델에 줄 자연어 지시문을 바꾸고 평가하는 과정을 반복해 지시문을 자동으로 개선한다.[^research]

### 2. 모델 경량화와 환경 변화 적응

교사 모델의 정보를 학생 모델에 전달하는 증류 방법을 개발하고, 날씨·조명·센서가 달라지는 환경에서 시각 모델이 작동하도록 학습 방법을 설계한다. 대표 논문에서는 모델 출력 사이의 관계를 비교하는 거리와 모델 연결을 제거하는 방법을 결합한 증류를 제안했으며, 중간 날씨 자료를 추가하지 않고 맑은 날 영상에서 실제 안개 영상으로 적응하는 방법도 제안했다.[^research][^p6][^p7]

### 3. 3차원 표면 생성과 색 편집

TexTailor 연구는 문장을 바탕으로 3차원 물체 표면의 색과 무늬를 생성하며, 물체 표면의 위치를 고려해 자료를 다시 뽑는 방법으로 시점 간 일관성을 다룬다. ICE-NeRF 연구는 신경 복사장(Neural Radiance Fields, 위치와 관찰 방향에 따른 빛의 정보를 신경망으로 표현하는 장면 모형)의 색을 사용자가 선택해 바꾸는 방법이다. 신경망은 서로 연결된 계산 단위와 그 연결의 조절값으로 입력과 출력의 관계를 학습하는 모형이다.[^research][^p8]

### 4. 뇌 활동을 문장으로 설명하기

뇌 활동 영상과 그때의 시각 자극을 설명하는 문장을 공통 표현 공간에서 연결하는 방법을 개발한다. 서로 대응하는 영상과 문장의 표현이 가까워지도록 학습하고, 새 뇌 영상으로부터 문장을 생성한다. 연구실은 생성한 단어별로 기여한 뇌 영역을 살펴보는 방법도 제시한다.[^research]

## 대표 논문

KAIST 재직 시기의 연구 가운데 시각·언어 연결, 모델 경량화, 환경 적응, 3차원 생성·편집, 뇌 영상 해석을 보여 주는 논문을 골랐다. 「쉽게 말하면」은 각 논문의 등록 초록 또는 각주에 밝힌 연구실의 개별 설명을 근거로 썼다. 연도와 발표처는 연구실 표기다.[^papers]

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [AIPO: Automatic Instruction Prompt Optimization by Model Itself with "Gradient Ascent"](https://doi.org/10.1016/j.csl.2025.101889) · Computer Speech & Language | 모델이 자신의 응답을 평가하고 자연어 지시문 수정안을 제안하는 과정을 반복해 지시문을 자동으로 다듬는다.[^p1] | Kyeonghye Park, Dae-Shik Kim |
| 2 | 2025 | MMR: A Large-scale Benchmark Dataset for Multi-target and Multi-granularity Reasoning Segmentation · ICLR | 하나의 장면에서 여러 대상과 부분·전체 수준을 함께 가리키는 질문으로 분할 모델을 평가하는 자료를 만들고, 모델의 오류와 기준 방법을 제시한다.[^p2] | Donggon Jang·Yucheol Cho(연구실 공동 기여 표기), Suin Lee, Taehyeon Kim, Dae-Shik Kim |
| 3 | 2025 | TexTailor: Customized Text-aligned Texturing via Effective Resampling · ICLR | 문장으로 3차원 물체 표면의 무늬를 만들면서 표면 위치를 고려해 자료를 다시 뽑아, 시점 사이 이음새와 표현 차이를 다룬다.[^p3] | Suin Lee, Dae-Shik Kim |
| 4 | 2025 | [Interpretable fMRI Captioning via Contrastive Learning](https://doi.org/10.1007/978-3-032-05185-1_29) · MICCAI | 뇌 활동 영상과 대응 문장을 함께 학습해 영상에서 설명문을 생성하고, 각 출력 단어에 기여한 뇌 영역을 살핀다.[^p4] | Vyacheslav Shen, Kassymzhomart Kunanbayev, Donggon Jang, Dae-Shik Kim |
| 5 | 2025 | [Multi-View Prototypical Transport for Unsupervised Domain Adaptation](https://doi.org/10.1109/access.2025.3528054) · IEEE Access | 모델의 여러 층에 담긴 일반적인 정보를 함께 이용해, 정답 표시가 없는 새 환경의 자료에 모델을 적응시키는 방법을 제안했다.[^p5] | Sunhyeok Lee, Dae-Shik Kim |
| 6 | 2024 | [Energy-based Domain Adaptation without Intermediate Domain Dataset for Foggy Scene Segmentation](https://doi.org/10.1109/tip.2024.3483566) · IEEE Transactions on Image Processing | 중간 날씨 자료와 여러 단계 학습 없이 실제 안개 환경으로 적응하며, 영상의 각 위치에 대한 점수를 이용해 임시 정답의 과도한 확신을 줄이는 방법을 제안했다.[^p6] | Donggon Jang, Sunhyeok Lee, Gyuwon Choi, Yejin Lee, Sanghyeok Son, Dae-Shik Kim |
| 7 | 2024 | [Robustness-Reinforced Knowledge Distillation with Correlation Distance and Network Pruning](https://doi.org/10.1109/tkde.2024.3438074) · IEEE TKDE | 교사 모델과 학생 모델의 출력 관계를 비교하는 거리와 모델 연결 제거를 결합해, 학습 자료를 변형해 늘리는 방법을 증류에 활용하도록 했다.[^p7] | Seonghak Kim·Gyeongdo Ham·Yucheol Cho(연구실 공동 기여 표기), Dae-Shik Kim |
| 8 | 2023 | [ICE-NeRF: Interactive Color Editing of NeRFs via Decomposition-Aware Weight Optimization](https://doi.org/10.1109/iccv51070.2023.00323) · ICCV | 학습된 장면 모형과 사용자가 표시한 대략적인 영역을 입력받아 색을 바꾸며, 원치 않는 영역의 색 변화와 시점별 불일치를 줄였다.[^p8] | Jae-Hyeok Lee, Dae-Shik Kim |

## 교수와 전문 분야

김대식 교수는 1994년 독일 막스플랑크 뇌연구소에서 박사학위를 받았고, 1994–1996년 MIT 박사후연구원, 1996–1998년 RIKEN 연구원, 1999–2003년 미네소타대학교 조교수, 2003–2009년 보스턴대학교 부교수와 생체영상센터장을 거쳤다. 연구실 경력은 2009년부터 KAIST 전기및전자공학부 정교수로 적는다.[^people]

교수 소개의 관심 분야는 시각 인공지능과 멀티모달 학습, 대형 언어 모델, 계산·인지 신경과학, 인간 뇌 기능·연결 지도, 의료 영상 계산이다.[^people] 현재 연구와 대표 논문으로 보면 시각·언어를 연결하는 모델과 지시문 최적화, 모델의 학습 정보 전달과 환경 적응, 3차원 장면의 표현과 편집, 뇌 영상의 언어 해석이 전문 분야다.[^research][^p5][^p7][^p8]

## 응용 분야

시각·언어 연구는 장면 설명문 생성과 질문에 따른 대상 영역 찾기, 언어 모델 지시문 자동 개선에 연결된다. 3차원 연구는 문장에 맞는 물체 표면 생성과 장면 색 편집을 다룬다.[^research] 안개 장면 분할 논문은 자율주행의 영상 인식을 적용 대상으로 제시한다.[^p6] 뇌 영상 연구는 관측한 뇌 활동을 문장으로 설명하고 그 출력에 기여한 영역을 분석하는 방법을 다룬다.[^p4]

## 구성원

2026년 11월 9일 연구실 구성원 페이지 기준으로 박사과정 6명, 석사과정 2명, 학부 연구생 2명이다. 과정과 연구 주제는 연구실 게시 표기를 따른다.[^people] 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Romain Renard | 박사과정 | Neuromorphic Group |  |  |
| Sanghyeok Son | 박사과정 | Visual Intelligence | ssh816@kaist.ac.kr | 6 |
| Jinwoo Jeon | 박사과정 | Visual Intelligence | jjw0514@kaist.ac.kr |  |
| Minchan Kang | 박사과정 | Visual Intelligence | mc.kang@kaist.ac.kr |  |
| Kyeonghye Park | 박사과정 | Visual Intelligence | pkhpjhs@kaist.ac.kr | 1 |
| Gyuwon Choi | 박사과정 | Visual Intelligence | gyuwonchoi@kaist.ac.kr | 6 |
| Seoyoung Cho | 석사과정 | Large Language Model, Ad Prediction Model | 52tjdud@kaist.ac.kr |  |
| Junhee Lee | 석사과정 | Visual Intelligence | bedro1210@kaist.ac.kr |  |
| Joonghui Cho (조중휘) | 학부 연구생 | Large Language Model | paul26@kaist.ac.kr |  |
| Chanyong Shim (심찬용) | 학부 연구생 | visual intelligence | chanyong1@kaist.ac.kr |  |

## 외부 협력자

연구실이 외부 협력자로 게시한 교수와 소속이다.[^people]

| 이름 | 직위 | 소속 |
|---|---|---|
| Itamar Ronen | Prof. | Leiden University Medical Center |
| Jin Hyung Lee | Prof. | Stanford University, EE |
| Jun Tani | Prof. | OIST |
| Soo-Young Lee | Prof. | KAIST, EE |
| Takashi Ikegami | Prof. | University of Tokyo |
| Hae-Jeong Park | Prof. | Yonsei University, BME |
| Joohan Kim | Prof. | Yonsei University, Communication |
| Eun Joo Kim | Prof. | Yonsei University, Education |

## 졸업생과 이전 구성원

연구실의 Alumni 목록 159개 게시 항목이다. 박사 졸업 11건, 석사 졸업 44건, 이전 연구원 17건, 이전 학부 연구생 85건, 연구부교수 1건, 박사후연구원 1건을 담았다. 같은 사람이 학위나 참여 기간별로 거듭 나타날 수 있으며, 진로는 연구실이 게시한 당시 표기다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Kassymzhomart Kunanbayev | Ph.D. (2026) |  |
| Donggon Jang | Ph.D. (2026) | NOW RESEARCHER @ SAMSUNG ELECTRONICS MOBILE EXPERIENCE |
| Sunhyeok Lee | Ph.D. (2025) | NOW RESEARCHER @ HD HYUNDAI GLOBAL R&D CENTER |
| Yucheol Cho | Ph.D. (2025) | NOW ASSISTANT PROFESSOR @ HANBAT NATIONAL UNIVERSITY |
| Jae-Hyeok Lee | Ph.D. (2024) | NOW RESEARCHER @ ETRI |
| Gyeongdo Ham | Ph.D. (2024) | NOW RESEARCHER @ SAMSUNG ELECTRONICS S.LSI |
| Jung Hyuk Im | Ph.D. (2022) | NOW CEO @ INNERVERZ |
| Kiuk Gwak | Ph.D. (2021) | NOW CEO @ BHAPTICS |
| Seungkyu Nam | Ph.D. (2018) | RESEARCHER @ HYUNDAI MOTOR COMPANY |
| Jun-Cheol Park | Ph.D. (2017) | NOW CTO @ OMNIOUS |
| Jungsoo Lee | Ph.D. (2017) | NOW ASSISTANT PROFESSOR @ KUMOH NATIONAL INSTITUTE OF TECHNOLOGY |
| Seongmin Park | M.S. (2026) | now Researcher @ GraphAI |
| Taehyeon Kim | M.S. (2026) | now Researcher @ LIG Defense&Aerospace |
| Suin Lee | M.S. (2025) | now Ph.D. student @ KAIST |
| Shen Vyacheslav | M.S. (2025) | now Researcher @ Cerebra.ai |
| Sehui Jang | M.S. (2024) | now Researcher @ Viewworks |
| Seonghak Kim | M.S. (2024) | now Researcher @ ADD |
| Yejin Lee | M.S. (2024) | now Researcher @ HDC Labs |
| Jeongwon Lee | M.S. (2024) | now Researcher @ SK Hynix |
| Woojin Jeong | M.S. (2023) | now Researcher @ Samsung Advanced Institute of Technology |
| Bomi Kim | M.S. (2022) | now Researcher @ Samsung Research |
| Nahyun Kim | M.S. (2022) | now Researcher @ Samsung Research |
| Wooyeong Cho | M.S. (2022) | now Ph.D. student @ UCLA |
| Gyeongman Kim | M.S. (2021) | now Ph.D. student @ KAIST |
| Dongho Lim | M.S. (2021) | now Researcher @ TmaxSoft |
| Jungwon Choi | M.S. (2021) | now Ph.D. student @ KAIST |
| Geondo Park | M.S. (2020) | now Ph.D. student @ KAIST |
| Deokyun Kim | M.S. (2020) | now Researcher @ ETRI |
| Seho Cho | M.S. (2020) | now Researcher @ Samsung Electronics |
| Gihyun Kwon | M.S. (2020) | now Ph.D. student @ KAIST |
| Minseon Kim | M.S. (2020) | now Ph.D. student @ KAIST |
| Chihye Han | M.S. (2019) | now Ph.D. student @ Johns Hopkins University |
| Andriy Serdega | M.S. (2019) |  |
| Tetiana Parshakova | M.S. (2019) | now Ph.D student @ Stanford Univ. |
| Vasyl Maksymchuk | M.S. (2019) | now Researcher @ RealTimeTech |
| Jeongho Kim | M.S. (2019) | now Researcher @ Samsung Electronics |
| Wonjun Yoon | M.S. (2019) | now Researcher @ Lunit Inc. |
| Jisuk Park | M.S. (2019) | now Researcher @ LG Electronics |
| Jaesung Bae | M.S. (2019) | now Researcher @ NCSOFT AI Research |
| Jung Hyuk Im | M.S. (2018) | now Ph.D. student @ BREIL |
| Kang Un Cho | M.S. (2018) | now Researcher @ KAI |
| Jinwoo Jeon | M.S. (2017) | now Researcher @ ETRI |
| Changmo Nam | M.S. (2017) |  |
| Youngjoo Jo | M.S. (2016) | now Researcher @ ETRI |
| Hyoungwon Choi | M.S. (2015) | now Ph.D. student @ KAIST |
| Yunhun Jang | M.S. (2015) | now Ph.D. student @ KAIST |
| Young Jae Jin | M.S. (2014) | now Engineer @ DRAM Development Division, SK Hynix |
| Hyerin Lim | M.S. (2014) | now Researcher @ Hyundai Motor Company |
| Juhyeon Lee | M.S. (2014) | now Researcher @ LG CTO |
| Jae Hyun Lim | M.S. (2014) | now Researcher @ ETRI |
| Jaeheon Yoo | M.S. (2013) | now Researcher @ Samsung Electronics DMC Research Institute |
| Misun Kim | M.S. (2013) | now Ph.D student @ Wellcom Trust Centre for Neuroimaging, UCL |
| Seungkyu Nam | M.S. (2013) | now Ph.D student @ BREIL |
| Sun Mi Park | M.S. (2012) | now Ph.D student @ BREIL |
| Jungsoo Lee | M.S. (2012) | now Ph.D student @ BREIL |
| Hayeon Lee | Researcher (09. 2018 ~ 01. 2019) |  |
| Jin Myung Kwak | Researcher (01. 2018 ~ 06. 2018) |  |
| Jaeyoung Jun | Researcher (01. 2011 ~ 08. 2015) |  |
| Romain RENARD | Researcher (02. 2015 ~ 08. 2015) | Ingenieurs Specialises en Microelectronique et Informatique (ISMIN), Ecole des Mines de Saint-Etienne, France |
| Hyoungwon Choi | Researcher (03. 2015 ~ 08. 2015) |  |
| Yunhun Jang | Researcher (03. 2015 ~ 08. 2015) |  |
| Audrey WALTER | Researcher (04. 2015 ~ 08. 2015) | Engineering - Specialization Health and Technologies, ECE Graduate School of Engineering in Paris, France |
| Hyerin Lim | Researcher (03. 2014 ~ 08. 2014, 12. 2014 ~ 10. 2015) |  |
| Sihyeon Seong | Researcher (03. 2013 ~ 09. 2014) |  |
| Selim RABOUDI | Researcher (09. 2013 ~ 07. 2014) | Telecom Bretagne, France |
| Hyojung Kim | Researcher (08. 2012 ~ 09. 2012) |  |
| Fayyaz Ahmad | Researcher (09. 2010 ~ 02. 2012) |  |
| Jihyuck Jo | Researcher (03.2012) |  |
| Minsu Jang | Researcher (09. 2011 ~ 12. 2011) |  |
| Sung Kyun Lee | Researcher (03. 2011 ~ 07. 2011) |  |
| Seungkyu Nam | Researcher (10. 2010 ~ 01. 2011) |  |
| Dong Hyun Lee | Researcher (04. 2010 ~ 10. 2010) |  |
| Gyeongman Kim | Undergraduate Student (09. 2018 ~ 12.2018 ) |  |
| Min Hoo Kang | Undergraduate Student (09. 2018 ~ 12.2018 ) |  |
| Su Min Hu | Undergraduate Student (03. 2018 ~ 06. 2018) |  |
| Hee Jun Lee | Undergraduate Student (03. 2018 ~ 06. 2018) |  |
| Hyo Gyeong Choe | Undergraduate Student (06. 2018 ~ 08. 2018) |  |
| Gyeong Jun Kim | Undergraduate Student (01. 2018 ~ 02. 2018) |  |
| Hee Jun Lee | Undergraduate Student (01. 2018 ~ 02. 2018) |  |
| Seenyoung Kang | Undergraduate Student (01. 2018 ~ 02. 2018, EE Co-op program with Kakao) |  |
| Kum Seok Nam | Undergraduate Student (01. 2018 ~ 02. 2018, EE Co-op program with Kakao) |  |
| Gyeongman Kim | Undergraduate Student (01. 2018 ~ 02. 2018, EE Co-op program with Naver) |  |
| Minseon Kim | Undergraduate Student (06. 2017 ~ 12. 2017) |  |
| Kyeongha Rho | Undergraduate Student (07. 2017 ~ 08. 2017) |  |
| Min A Kim | Undergraduate Student (05. 2017 ~ 08. 2017) |  |
| Wonjun Yoon | Undergraduate Student (01. 2017 ~ 02. 2017) |  |
| Jeongho Kim | Undergraduate Student (01. 2017 ~ 02. 2017) |  |
| Vasyl MAKSYMCHUK | Undergraduate Student (07. 2016 ~ 02. 2017) |  |
| Tetiana PARSHAKOVA | Undergraduate Student (01. 2016 ~ 02. 2017) |  |
| Yue REN | Undergraduate Student (01. 2016 ~ 06. 2016) |  |
| Minsun Kim | Undergraduate Student (01. 2016 ~ 03. 2016) |  |
| Jihye Lee | Undergraduate Student (03. 2015 ~ 06. 2015) |  |
| Jin Suk Lim | Undergraduate Student (06. 2015 ~ 08. 2015) |  |
| Seungjin Jung | Undergraduate Student (03. 2015 ~ 06. 2015) |  |
| Bogyeng Kim | Undergraduate Student (01. 2015 ~ 02. 2015) |  |
| Matheus VERVLOET | Undergraduate Student (01. 2015 ~ 02. 2015) | Computer Engineering, Universidade Federal de Sao Carlos (UFSCar), Brazil |
| Sanggyu Han | Undergraduate Student (01. 2015 ~ 02. 2015) |  |
| Juhyung Han | Undergraduate Student (07. 2014 ~ 12. 2014) |  |
| Haeil Lee | Undergraduate Student (07. 2014 ~ 12. 2014 ) |  |
| Yeo Reum Choi | Undergraduate Student (09. 2014 ~ 10. 2014) |  |
| Jinhun Jung | Undergraduate Student (06. 2014 ~ 08. 2014) |  |
| Benjamin HALIMI | Undergraduate Student (04. 2014 ~ 08. 2014) |  |
| Kang Un Cho | Undergraduate Student (01. 2014 ~ 08. 2014) |  |
| Luiz Felipe VECCHIETTI | Undergraduate Student (01. 2014 ~ 02. 2014) |  |
| Sung Hun Kang | Undergraduate Student (01. 2013 ~ 01. 2014) |  |
| Jun Young Kim | Undergraduate Student (06. 2013~ 12. 2013) |  |
| JungAh Hong | Undergraduate Student (09. 2013 ~ 12. 2013) |  |
| Woo Hyuck Song | Undergraduate Student (09. 2013 ~ 12. 2013) |  |
| Seong Seop Shin | Undergraduate Student (09. 2013 ~ 12. 2013) |  |
| Yoseph Hwang | Undergraduate Student (09. 2013 ~ 12. 2013) |  |
| Beung Jin Choi | Undergraduate Student (09. 2013 ~ 12. 2013) |  |
| Young Seok Park | Undergraduate Student (06. 2013 ~ 08. 2013) | Carnegie Mellon University(CMU), Pittsburgh, US |
| Jennifer Lee | Undergraduate Student (11. 2012 ~ 02. 2013) | Department of Arts, University of Sydney |
| Junho Lyoo | Undergraduate Student (06. 2012 ~ 12. 2012) |  |
| Won Hee Lee | Undergraduate Student (06. 2012 ~ 12. 2012) |  |
| Hyungwon Choi | Undergraduate Student (06. 2012 ~ 12. 2012, 2012 Fall/Winter URP) |  |
| Yunhun Jang | Undergraduate Student (02. 2012 ~ 09. 2012) |  |
| Sihyeon Sung | Undergraduate Student (06. 2011 ~ 01. 2013, 2012 Fall/Winter URP) |  |
| Yuhyeon Jun | Undergraduate Student (04. 2012 ~ 10. 2012) |  |
| Juheon Lee | Undergraduate Student (01. 2012 ~ 05. 2012) |  |
| Jinyong Jung | Undergraduate Student (11. 2011 ~ 08. 2012) |  |
| Kyuyeol Lee | Undergraduate Student (06. 2011 ~ 08. 2011, 06. 2012 ~ 08. 2012) |  |
| Jae Sung Cho | Undergraduate Student (05. 2012 ~ 08. 2012) | Department of Biomedical Engineering, Georgia Institute of Technology & Emory University School of Medicine |
| HyeongChan Jo | Undergraduate Student (02. 2012 ~ 05. 2012) |  |
| Tae Ho Kim | Undergraduate Student (02. 2011 ~ 05. 2011, 01. 2012 ~ 05. 2012 ) |  |
| Seokkyu Sun | Undergraduate Student (06. 2011 ~ 12. 2011, 02. 2012~ 03. 2012) |  |
| Gangjae Yu | Undergraduate Student (02. 2011 ~ 03. 2012) |  |
| Su Yeong Lee | Undergraduate Student (12. 2011 ~ 01. 2012) |  |
| Gwang Ryeol Lee | Undergraduate Student (11. 2011 ~ 07. 2012) |  |
| Soomin Lee | Undergraduate Student (11. 2011 ~ 01. 2012) |  |
| Hwaran Lee | Undergraduate Student (09. 2011 ~ 01. 2012) |  |
| Minju Jung | Undergraduate Student (09. 2011 ~ 01. 2012) |  |
| Ji Hyuck Jo | Undergraduate Student (08. 2011 ~ 01. 2012) |  |
| Soyoung Ahn | Undergraduate Student (06. 2011 ~ 12. 2011) |  |
| Ha Jin Jang | Undergraduate Student (05. 2011 ~ 12. 2011, EE undergraduate researcher) |  |
| Jihye Kim | Undergraduate Student (06. 2011 ~ 12. 2011, EE undergraduate researcher) |  |
| Jungkyu Han | Undergraduate Student (06. 2011 ~ 12. 2011, EE undergraduate researcher) |  |
| Jee Won Hwang | Undergraduate Student (05. 2011 ~ 12. 2011) |  |
| Charles Hwang | Undergraduate Student (10. 2011 ~ 12. 2011) |  |
| Seungjin Jung | Undergraduate Student (05. 2011 ~ 12. 2011) |  |
| Jeongyun Choi | Undergraduate Student (08. 2011 ~ 09. 2011) |  |
| Minhye Kim | Undergraduate Student (06. 2010 ~ 08. 2011) |  |
| Hyeyun Go | Undergraduate Student (02. 2011 ~) |  |
| Minsu Jang | Undergraduate Student (09. 2010 ~ 08. 2011, 2011 Spring/Summer URP) |  |
| Arvin Omran | Undergraduate Student (02. 2011 ~ 05. 2011) |  |
| Jae Eon Lee | Undergraduate Student (02. 2011 ~ 05. 2011) |  |
| Jooyeon Chung | Undergraduate Student (09. 2010 ~ 03. 2011) |  |
| Sun Jeong Park | Undergraduate Student (01. 2011) |  |
| Yong Min Son | Undergraduate Student (06. 2010 ~ 01. 2011) |  |
| YuJung Nam | Undergraduate Student (01. 2011) |  |
| SuJin Hwang | Undergraduate Student (04. 2010 ~ 01. 2011, 2010 Fall/Winter URP) |  |
| Jae Man An | Undergraduate Student (05. 2010 ~ 09. 2010) |  |
| Younoh Bae | Undergraduate Student (12. 2009 ~ 08. 2010) |  |
| Yungsoo Kim | Undergraduate Student (06. 2010) |  |
| Youree Kwon | Undergraduate Student (02. 2010 ~ 05. 2010) |  |
| Hyunsoo Yoo | Undergraduate Student (12. 2009 ~ 06. 2010) |  |
| HyoWon Suh | Undergraduate Student (12. 2009 ~ 06. 2010, 2010 Spring/Summer URP) |  |
| Dongpyo Lee | Research Associate Professor (03. 2013 ~ 02. 2014) | now @ Yonsei Severance Hospital |
| Hansol Choi | Post Doctor (09. 2011 ~ 08. 2014) | now Research Associate @ Freiburg University |

## 최근 5년 논문 목록

2021–2026년 연구실 Papers 목록의 학술지·학회·워크숍 논문 30편이다. 저자·제목·발표처·연도는 연구실 표기이고, 별표와 공동 기여 문구도 게시 표기를 따른다.[^papers]

CCN 2022의 해마(기억 형성 등에 관여하는 뇌의 구조) 분할 논문 두 편은 정답 표시 없는 자료로 먼저 학습한 정보를, 정답 표시가 적은 자료의 영상 분할 학습으로 옮기는 학습 틀을 개발했다.[^ccn1075][^ccn1074]

**2026**

- Kyeonghye Park, Dae-Shik Kim. “AIPO: Automatic Instruction Prompt Optimization by Model Itself with "Gradient Ascent"”. *COMPUTER SPEECH & LANGUAGE, ELSEVIER, Feb 2026*. DOI <https://doi.org/10.1016/j.csl.2025.101889>.

**2025**

- Seonghak Kim, Gyeongdo Ham, Suin Lee, Dae-Shik Kim. “Teach sample-specific knowledge: Separated distillation based on samples”. *EAAI, Engineering Applications of AI (ELSEVIER), Dec 2025*. DOI <https://doi.org/10.1016/j.engappai.2025.112696>.
- Vyacheslav Shen, Kassymzhomart Kunanbayev, Donggon Jang, Dae-Shik Kim. “Interpretable fMRI Captioning via Contrastive Learning”. *MICCAI, Daejeon, Sep 23 to 27, 2025*. DOI <https://doi.org/10.1007/978-3-032-05185-1_29>.
- Donggon Jang\*, Yucheol Cho\*, Suin Lee, Taehyeon Kim, Dae-Shik Kim. “MMR: A Large-scale Benchmark Dataset for Multi-target and Multi-granularity Reasoning Segmentation”. *ICLR, Singapore, Apr 24 to 28, 2025 (\*Equal contribution)*.
- Suin Lee, Dae-Shik Kim. “TexTailor: Customized Text-aligned Texturing via Effective Resampling”. *ICLR, Singapore, Apr 24 to 28, 2025*.
- Yucheol Cho, Jae-Hyeok Lee, Gyeongdo Ham, Donggon Jang, Dae-Shik Kim. “Generality-aware Self-supervised Transformer for Multivariate Time Series Anomaly Detection”. *APPLIED INTELLIGENCE, Springer, Mar 2025*. DOI <https://doi.org/10.1007/s10489-025-06481-7>.
- Sunhyeok Lee, Dae-Shik Kim. “Multi-View Prototypical Transport for Unsupervised Domain Adaptation”. *IEEE ACCESS, Jan 2025*. DOI <https://doi.org/10.1109/access.2025.3528054>.

**2024**

- Donggon Jang, Sunhyeok Lee, Gyuwon Choi, Yejin Lee, Sanghyeok Son, Dae-Shik Kim. “Energy-based Domain Adaptation without Intermediate Domain Dataset for Foggy Scene Segmentation”. *IEEE TIP, IEEE Transactions on Image Processing, Oct 2024*. DOI <https://doi.org/10.1109/tip.2024.3483566>.
- Minchan Kang, Sanghyeok Son, Dae-Shik Kim. “Adaptive class token knowledge distillation for efficient vision transformer”. *KBS, Knowledge-Based Systems, Nov 2024*. DOI <https://doi.org/10.1016/j.knosys.2024.112531>.
- Gyeongdo Ham\*, Yucheol Cho\*, Jae-Hyeok Lee, Minchan Kang, Gyuwon Choi, Dae-Shik Kim. “Difficulty Level-based Knowledge Distillation”. *NEUROCOMPUTING, Nov 2024 (\*Equal contribution)*. DOI <https://doi.org/10.1016/j.neucom.2024.128375>.
- Yucheol Cho\*, Guenseok Choi\*, Gyeongdo Ham, Mincheol Shin, Dae-Shik Kim. “SemiH: DFT Hamiltonian Neural Network Training with Semi-supervised Learning”. *MLST, Machine Learning: Science and Technology, Sep 2024*. DOI <https://doi.org/10.1088/2632-2153/ad7227>.
- Seonghak Kim\*, Gyeongdo Ham\*, Yucheol Cho\*, Dae-Shik Kim. “Robustness-Reinforced Knowledge Distillation with Correlation Distance and Network Pruning”. *IEEE TKDE, IEEE TKDE, Aug 2024 (\*Equal contribution)*. DOI <https://doi.org/10.1109/tkde.2024.3438074>.
- Seonghak Kim\*, Gyeongdo Ham\*, Suin Lee, Donggon Jang, Dae-Shik Kim. “Maximizing discrimination capability of knowledge distillation with energy function”. *KBS, Knowledge-Based Systems, Jul 2024 (\*Equal contribution)*. DOI <https://doi.org/10.1016/j.knosys.2024.111911>.
- Ji-Man Yu\*, Gyeong-Do Ham\*, Seong-Yeon Kim, Jin-Ki Kim, Joon-Kyu Han, Seong-Yun Yun, Seong-Hak Kim, Sang-Won Lee, Seung-Bae Jeon, Dae-Shik Kim, Yang-Kyu Choi. “Self-Curable Synaptor with Tri-node Charge Trap FinFET for Semi-Supervised Learning”. *IEEE EDL, IEEE Electron Device Letters, Jan 2024 (\*Equal contribution)*. DOI <https://doi.org/10.1109/led.2024.3359600>.
- Suin Lee, Jae-Hyeok Lee, Dae-Shik Kim. “Geometry and Depth-Informed Texture Compositing for Realistic Texture Synthesis”. *CVPR WORKSHOP, C3DV, Seattle, Jun 2024*.
- Joonhyeok Jang\*, Sunhyeok Lee\*, Seonghak Kim, Jung-un Kim, Seonghyun Kim, Dae-Shik Kim. “Robust Unsupervised Domain Adaptation Through Negative-View Regularization”. *WACV, Jan 4 to 8, 2024 (\*Equal contribution)*. DOI <https://doi.org/10.1109/wacv57701.2024.00245>.

**2023**

- Yucheol Cho\*, Guenseok Choi\*, Gyeongdo Ham, Mincheol Shin, Dae-Shik Kim. “DFT Hamiltonian Neural Network Training with Semi-supervised Learning”. *NEURIPS WORKSHOP, ML4PS, New Orleans, Dec 2023 (\*Equal contribution)*.
- Minchan Kang\*, Woojin Jeong\*, Sanghyeok Son, Gyeongdo Ham, Dae-Shik Kim. “Burst Super-Resolution with Adaptive Feature Refinement and Enhanced Group Up-sampling”. *APPLIED INTELLIGENCE, Springer, Nov 2023 (\*Equal contribution)*. DOI <https://doi.org/10.1007/s10489-023-05127-w>.
- Jae-Hyeok Lee, Dae-Shik Kim. “ICE-NeRF: Interactive Color Editing of NeRFs via Decomposition-Aware Weight Optimization”. *ICCV, Paris, Oct 2 to 6, 2023*. DOI <https://doi.org/10.1109/iccv51070.2023.00323>.
- Gyuwon Choi\*, Yejin Lee\*, Donggon Jang, Dae-Shik Kim. “A Subdomain-Specific Knowledge Distillation for Unsupervised Domain Adaptation in Adverse Weather Conditions”. *ICCV WORKSHOP, Oct 2023 (\*Equal contribution)*.
- Sunhyeok Lee, Donggon Jang, Dae-Shik Kim. “Temporally Averaged Regression for Semi-Supervised Low-Light Image Enhancement”. *CVPR WORKSHOP, Jun 2023*. DOI <https://doi.org/10.1109/cvprw59228.2023.00443>.
- Yucheol Cho, Gyeongdo Ham, Dae-Shik Kim. “First-principles Study on As Antisites in InGaAs Alloys, GaAs and InAs”. *IWCN, Barcelona, Jun 12 to 16, 2023*.
- Yucheol Cho\*, Gyeongdo Ham\*, Jae-Hyeok Lee, Dae-Shik Kim. “Ambiguity-aware Robust Teacher (ART): Enhanced Self-knowledge Distillation Framework with Pruned Teacher Network”. *PATTERN RECOGNITION, Vol. 140C, 109541, Mar 2023 (\*Equal contribution)*. DOI <https://doi.org/10.1016/j.patcog.2023.109541>.

**2022**

- Gyeongdo Ham\*, Yucheol Cho\*, Jae-Hyeok Lee, Dae-Shik Kim. “P-PseudoLabel: Enhanced Pseudo-Labeling Framework with Network Pruning in Semi-Supervised Learning”. *IEEE ACCESS, Vol. 10, 115652-115662, Oct 2022 (\*Equal contribution)*. DOI <https://doi.org/10.1109/access.2022.3218161>.
- Kassymzhomart Kunanbayev, Donggon Jang, Jeongwon Lee, Dae-Shik Kim. “Variance-Invariance-Covariance Regularization with Local Self-Supervised Learning Improves Hippocampus Segmentation with Fewer Labels”. *CCN, San Francisco, Aug 25 to 28, 2022*. DOI <https://doi.org/10.32470/ccn.2022.1075-0>.
- Kassymzhomart Kunanbayev, Donggon Jang, Jeongwon Lee, Dae-Shik Kim. “Towards Precise and Robust Hippocampus Segmentation using Self-Supervised Contrastive Learning”. *CCN, San Francisco, Aug 25 to 28, 2022*. DOI <https://doi.org/10.32470/ccn.2022.1074-0>.
- Donggon Jang\*, Sanghyeok Son\*, Dae-Shik Kim. “Strengthening the Transferability of Adversarial Examples Using Advanced Looking Ahead and Self-CutMix”. *CVPR WORKSHOP, New Orleans, Jun 2022 (\*Equal contribution)*. DOI <https://doi.org/10.1109/cvprw56347.2022.00026>.
- Ji-Man Yu\*, Gyeongdo Ham\*, Chungryeol Lee, Jae-Hyeok Lee, Joon-Kyu Han, Jin-Ki Kim, Donggon Jang, Nahyun Kim, Moon-Seok Kim, Sung Gap Im, Dae-Shik Kim, Yang-Kyu Choi. “A Multiple-State Ion Synaptic Transistor Applicable to Abnormal Car Detection with Transfer Learning”. *ADV. INTELLIGENT SYSTEMS, Vol. 4 Issue 6, Jun 2022 (\*Equal contribution)*. DOI <https://doi.org/10.1002/aisy.202100231>.
- Bomi Kim\*, Sunhyeok Lee\*, Nahyun Kim, Donggon Jang, Dae-Shik Kim. “Learning Color Representations for Low-Light Image Enhancement”. *WACV, Waikoloa, Jan 2022 (\*Equal contribution)*. DOI <https://doi.org/10.1109/wacv51458.2022.00098>.

**2021**

- Nahyun Kim\*, Donggon Jang\*, Sunhyeok Lee, Bomi Kim, Dae-Shik Kim. “Unsupervised Image Denoising with Frequency Domain Knowledge”. *BMVC, Oral presentation, Nov 2021 (\*Equal contribution)*. DOI <https://doi.org/10.5244/c.35.326>.

## 특허

연구실 Patents 목록에서 등록일 또는 출원일이 2021-10-13–2026-10-13에 드는 등록 1건과 출원 3건이다. 제목·발명자·번호·날짜·상태는 연구실 게시 표기다.[^patents]

- 단일 이미지 빗물 제거를 위한 유효성 인식 기반 빗물 제거 방법 (발명자 김대식, 이선혁, 장동곤, 김보미, 김나현; 상태 등록; 등록일 2022.05.24; 출원일 2021.03.03; 등록번호 제 10-2402749호)
- System and method for face swapping with single/multiple source images using attention mechanism (발명자 김대식, 이재혁; 상태 출원; 출원일 2023.02.14; 출원번호 18/109,519; 국가 미국)
- 딥러닝에 기반한 이미지 초해상화 방법 및 시스템 (발명자 김대식, 강민찬, 정우진, 손상혁, 함경도; 상태 출원; 출원일 2023.02.09; 출원번호 10-2023-0017258)
- 주의 알고리즘 기반의 단일/다중 소스 이미지를 활용 가능한 고선명도 얼굴 교체 시스템 및 방법 (발명자 김대식, 이재혁; 상태 출원; 출원일 2022.02.15; 출원번호 10-2022-0019582)

## 저서

연구실이 Books에 게시한 저서·공저·편집·기획자문·서문 참여 목록 44건이다. 2003–2026년 목록으로 KAIST 부임 전 항목도 포함하며, 저자와 역할은 연구실 표기다.[^books]

- 2026.05.08 · 김대식 교수의 어린이를 위한 AI수업. 김대식. 동아시아 · ISBN 9791191644227.
- 2026.03.27 · AI가 너보다 일을 잘할 때. 김대식, 김혜연. 창비 · ISBN 9788936481247.
- 2025.08.18 · 사이 인간-AI시대 문명과 문명 사이에 놓인 새로운 미래. 김대식. 문학동네 · ISBN 9791141611231.
- 2025.08.18 · AGI, 천사인가 악마인가. 김대식. 동아시아 · ISBN 9788962626667.
- 2024.11.01 · 존재하지 않는 영화. 김대식, 김태용, 김혜연, 임다솔. 쌤앤파커스 · ISBN 9791194246305.
- 2024.09.30 · 생각의 탄생9 에너지와 환경. 김향자, 김대식 (기획자문). 아울북 · ISBN 9791171177950.
- 2024.08.30 · 원더랜드 작품집: MOVIE ARTBOOK. 김태용, 김대식. 김영사 · ISBN 9788934967712.
- 2024.07.19 · 생각의 탄생8 스포츠와 올림픽. 장지원, 김대식 (기획자문). 아울북 · ISBN 9791171176724.
- 2024.07.09 · 위대한 인도. 한상호, 강성용, 김대식. 문학동네 · ISBN 9791141606572.
- 2024.02.14 · 생각의 탄생7 인공지능과 미래. 김형자, 김대식 (기획자문). 아울북 · ISBN 9791171173433.
- 2023.11.20 · 생각의 탄생6 진화와 유전. 이은희, 김대식 (기획자문). 아울북 · ISBN 9791171171651.
- 2023.08.21 · 생각의 탄생5 문자와 생활. 유현주, 김대식 (기획자문). 아울북 · ISBN 9791171170142.
- 2023.06.19 · 생각의 탄생4 지도와 탐험. 김향금, 김대식 (기획자문). 아울북 · ISBN 9788950922122.
- 2023.05.22 · AI 이후의 세계-챗GPT는 시작일 뿐이다, 세계질서 대전환에 대비하라. Henry A. Kissinger, Eric Schmidt, Daniel Huttenlocher, 김대식 (서문). 윌북 · ISBN 9791155816066.
- 2023.05.18 · THE AGE OF GENERATIVE ART-챗GPT가 말하고 DALL·E가 그리는 인공지능 시대의 예술. 김대식. 동아시아 · ISBN 9788962624960.
- 2023.04.17 · 생각의 탄생3 화폐와 경제. 장세현, 김대식 (기획자문). 아울북 · ISBN 9788950910907.
- 2023.03.08 · 김대식 교수의 어린이를 위한 인공지능: 메타버스부터 챗GPT까지. 김대식. 동아시아 · ISBN 9791191644081.
- 2023.02.28 · 챗GPT에게 묻는 인류의 미래-김대식 교수와 생성인공지능의 대화. 김대식. 동아시아 · ISBN 9788962624847.
- 2023.02.01 · 12세 전에 완성하는 뇌과학 독서법. 김대식. 비룡소 · ISBN 9788949135083.
- 2022.12.21 · 생각의 탄생2 시간과 시계. 고석규, 김대식 (기획자문). 아울북 · ISBN 9788950942762.
- 2022.10.04 · 생각의 탄생1 감염병과 백신. 예병일, 김대식 (기획자문). 아울북 · ISBN 9788950940669.
- 2022.01.21 · 메타버스 사피엔스. 김대식. 동아시아 · ISBN 9788962624151.
- 2021.11.30 · 매거진G: 4호[2021] 다시 시작할 수 있을까?. 김대식, 안수향 외 18명. 김영사 · ISBN 9788934974901 · p.7-9, p.132-139.
- 2021.08.30 · 매거진G: 3호[2021] 우리는 왜 여행하는가?. 김대식, 김원영 외 23명. 김영사 · ISBN 9788934980001 · p.7-9, p.116-121.
- 2021.05.31 · 매거진G: 2호[2021] 적의 적은 내 친구인가?: 네 편 혹은 내 편. 김대식, Richard Dawkins 외 19명. 김영사 · ISBN 9788934988991 · p.7-9, p.76-82.
- 2021.02.17 · 김대식의 키워드-미래를 여는 34가지 질문. 김대식. 김영사 · ISBN 9788934991359.
- 2020.12.15 · 매거진G: 1호[2020] 나란 무엇인가?. 김대식, Jared Diamond 외 19명. 김영사 · ISBN 9788934989011 · p.2-5, p.138-152.
- 2020.12.08 · 초가속-새로운 시대가 대한민국에 던지는 질문들. 김대식, 김동재, 장덕진, 주경철, 함준호. 동아시아 · ISBN 9788962623567.
- 2020.09.18 · 인간을 위한 미래. 김도현, 이재열, 김홍중, 김도년, 김대식, 강형구, 정유신, 김재인. 클라우드나인 · ISBN 9791189430870.
- 2019.07.22 · 당신의 뇌, 미래의 뇌. 김대식. 해나무 · ISBN 9791164050352.
- 2019.06.12 · 그들은 어떻게 세상의 중심이 되었는가: 김대식의 로마 제국 특강. 김대식. 21세기북스 · ISBN 9788950981372.
- 2018.09.17 · 지혜의 시대-4차 산업혁명에서 살아남기. 김대식. 창비 · ISBN 9788936476724.
- 2017.04.12 · 창조력은 어떻게 인류를 구원하는가. 김대식, 다니엘 바이스. 중앙북스 · ISBN 9788927808480.
- 2017.03.13 · 인간을 읽어내는 과학. 김대식. ㈜북이십일 · ISBN 9788950969103.
- 2017.03.05 · 어떻게 질문할 것인가. 김대식. 민음사 · ISBN 9788937434068.
- 2016.04.12 · 김대식의 인간 vs 기계: 인공지능이란 무엇인가. 김대식. 동아시아 · ISBN 9788962621358.
- 2015.06.18 · 이상한 나라의 뇌과학. 김대식. 문학동네 · ISBN 9788954636667.
- 2014.12.12 · 문화의 안과 밖 4: 과학적 사유와 인간 이해. 윤정로, 김대식, 장대익, 김경렬, 김상환. 민음사 · ISBN 9788937457241.
- 2014.12.03 · 김대식의 빅퀘스천. 김대식. 동아시아 · ISBN 9788962620887.
- 2014.06.18 · 내 머릿속에선 무슨 일이 벌어지고 있을까: 카이스트 김대식 교수의 말랑말랑 뇌과학. 김대식. 문학동네 · ISBN 9788954625043.
- 2013.04.19 · 진심은 어떻게 전해지는가. 김은성, 김도훈, 김대식. 21세기북스 · ISBN 9788950948252.
- 2009.03.23 · Diffusion Tensor Imaging in Developmental Clinical Neuroscience (Chapter 19, pp. 314-325). Dae-Shik Kim. Cambridge University Press, ed. Judith Rumsey & Monique Ernst · ISBN 9780521883573.
- 2008.03.17 · Principles and Advanced Methods in Medical Imaging and Image Analysis. Atam P. Dhawan, H.K. Huang, Dae-Shik Kim (Eds.). World Scientific Publishing Company · ISBN 9812705341.
- 2003.04.18 · 공부혁명. Dae-Shik Kim. EduChosun Press · ISBN 8989551781.

## 연락과 위치

- 교수 이메일: daeshik@kaist.ac.kr[^people]
- 주소: School of Electrical Engineering, KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Korea.[^home]
[^p1]: K. Park, D.-S. Kim, COMPUTER SPEECH & LANGUAGE, ELSEVIER, Feb 2026 (2026). <https://doi.org/10.1016/j.csl.2025.101889> 연구실 게시 개별 설명 기준. 개별 설명 원문 <https://brain.kaist.ac.kr/research> (관측 2026-11-09).
[^p2]: D. Jang 외, D.-S. Kim, ICLR, Singapore, Apr 24 to 28, 2025 (*Equal contribution) (2025). <https://brain.kaist.ac.kr/research> 연구실 게시 개별 설명 기준. 개별 설명 원문 <https://brain.kaist.ac.kr/research> (관측 2026-11-09).
[^p3]: S. Lee, D.-S. Kim, ICLR, Singapore, Apr 24 to 28, 2025 (2025). <https://brain.kaist.ac.kr/research> 연구실 게시 개별 설명 기준. 개별 설명 원문 <https://brain.kaist.ac.kr/research> (관측 2026-11-09).
[^p4]: V. Shen, K. Kunanbayev, D. Jang, D.-S. Kim, MICCAI, Daejeon, Sep 23 to 27, 2025 (2025). <https://doi.org/10.1007/978-3-032-05185-1_29> 연구실 게시 개별 설명 기준. 개별 설명 원문 <https://brain.kaist.ac.kr/research> (관측 2026-11-09).
[^p5]: S. Lee, D.-S. Kim, IEEE Access (2025). <https://doi.org/10.1109/access.2025.3528054> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5103221173,publication_year:2021-2026> (관측 2026-11-09).
[^p6]: D. Jang 외, D.-S. Kim, IEEE Transactions on Image Processing (2024). <https://doi.org/10.1109/tip.2024.3483566> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5103221173,publication_year:2021-2026> (관측 2026-11-09).
[^p7]: S. Kim, G. Ham, Y. Cho, D.-S. Kim, IEEE Transactions on Knowledge and Data Engineering (2024). <https://doi.org/10.1109/tkde.2024.3438074> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5103221173,publication_year:2021-2026> (관측 2026-11-09).
[^p8]: J.-H. Lee, D.-S. Kim, IEEE/CVF International Conference on Computer Vision (ICCV) (2023). <https://doi.org/10.1109/iccv51070.2023.00323> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5103221173,publication_year:2021-2026> (관측 2026-11-09).
[^home]: BREIL, 연구실 소개. <https://brain.kaist.ac.kr/> (관측 2026-11-09).
[^research]: BREIL, 연구 소개와 개별 논문 설명. <https://brain.kaist.ac.kr/research> (관측 2026-11-09).
[^people]: BREIL, People. <https://brain.kaist.ac.kr/people> (관측 2026-11-09).
[^papers]: BREIL, Publications: Papers. <https://brain.kaist.ac.kr/publications> (관측 2026-11-09).
[^books]: BREIL, Publications: Books. <https://brain.kaist.ac.kr/publications?tab=books> (관측 2026-11-09).
[^patents]: BREIL, Publications: Patents. <https://brain.kaist.ac.kr/publications?tab=patents> (관측 2026-11-09).
[^ccn1075]: K. Kunanbayev, D. Jang, J. Lee, D.-S. Kim, Variance-Invariance-Covariance Regularization with Local Self-Supervised Learning Improves Hippocampus Segmentation with Fewer Labels, CCN 2022, DOI 10.32470/ccn.2022.1075-0. 원문 Abstract. <https://2022.ccneuro.org/proceedings/0000087.pdf> (관측 2026-11-09).
[^ccn1074]: K. Kunanbayev, D. Jang, J. Lee, D.-S. Kim, Towards Precise and Robust Hippocampus Segmentation using Self-Supervised Contrastive Learning, CCN 2022, DOI 10.32470/ccn.2022.1074-0. 원문 Abstract. <https://2022.ccneuro.org/proceedings/0000629.pdf> (관측 2026-11-09).

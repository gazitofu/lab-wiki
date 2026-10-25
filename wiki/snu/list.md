# 영상과학 연구실 (Laboratory for Imaging Science and Technology, LIST)

**서울대학교 공과대학 전기·정보공학부, 첨단융합학부 디지털헬스케어(겸무) · 이종호 교수**

- 분야: 자기공명 영상의 획득·재구성·정량 분석, 물리 법칙을 반영한 딥러닝, 인공지능을 이용한 촬영 설계, 뇌의 철·수초 영상
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: 컴퓨터 비전[^p2][^p3][^p8], 강화학습[^p1], 멀티모달 AI[^strong]
- 홈페이지: <https://list.snu.ac.kr/>
- 근거와 출처: [LIST 근거 페이지](list-sources.md)

> 몸속을 영상으로 측정하는 방법과 그 영상을 만드는 계산을 함께 연구한다. 영상 획득·재구성·후처리 방법을 개발하고, 물리 법칙과 인공지능을 결합해 촬영 소프트웨어·하드웨어를 설계한다.[^research]

## 무엇을 연구하나

LIST는 의료영상과 의료 데이터를 위한 인공지능, 영상 획득·재구성 방법, 뇌의 생물물리적 특성을 연구한다. 재구성은 측정한 신호로부터 영상을 계산하는 일이다. 연구 소개는 물리 법칙을 따르는 딥러닝(여러 계산층으로 자료의 특징을 학습하는 방법) 알고리즘과 인공지능을 이용한 촬영 소프트웨어·하드웨어 설계를 주요 갈래로 든다.[^research] 연구실은 2010년 10월 펜실베이니아대학교 영상의학과 연구 그룹으로 시작했고 2014년 3월 서울대학교 전기·정보공학부로 옮겼다.[^home]

첫 갈래는 **인공지능으로 촬영을 설계하는 일**이다. 자기공명영상(Magnetic Resonance Imaging, MRI; 자기장과 전파에 반응하는 신호로 몸속을 영상화하는 방법)에서는 라디오주파수(Radiofrequency, RF) 펄스가 촬영 과정에 쓰인다. DeepRF는 강화학습(행동의 결과로 얻은 보상을 바탕으로 행동 방식을 학습하는 방법)으로 RF 파형을 만들었다. 네 종류의 펄스에서 설계 조건을 만족하면서 에너지 사용을 줄였고, 자화를 조절하는 새로운 방식을 확인했다고 보고했다.[^p1] Omni-QALAS(Optimized Myelin & Neurometric Imaging)는 자기지도학습(자료 자체에서 학습 목표를 구성하는 방법)으로 촬영 매개변수를 함께 최적화한다. T1·T2는 자화의 이완을 나타내는 시간 상수다. 이 방법은 T1·T2와 수초 수분량을 함께 측정하는 촬영을 다룬다.[^p5]

둘째는 **뇌 속 성분을 구분해 측정하는 영상**이다. 자기 감수율(외부 자기장에 대한 자화 반응을 나타내는 물성)을 위치마다 수치로 나타내는 기법을 정량 자기 감수율 지도화(Quantitative Susceptibility Mapping, QSM)라 한다. χ-separation은 철과 수초의 분포를 구분해 추정한다. 수초는 신경세포의 신호 전달 부분을 둘러싸는 층이다. 연구진은 고자기장 자료에 필요한 정보를 신경망(연결된 계산 단위들의 값을 학습하는 모형)으로 변환해 7T(T는 자기장 세기의 단위인 테슬라) MRI에서 χ-separation 지도를 얻는 방법을 개발했다.[^p3] 3차원 ViSTa(Direct Visualization of Short Transverse Relaxation Time Component)는 수초에 연관된 물의 신호에 민감한 영상을 뇌 전체에서 얻는 촬영 방법이고,[^p4] sandwichNM은 공간 포화 펄스(공간적으로 정한 영역의 자화에 작용하는 전파 펄스)를 이용해 뉴로멜라닌(Neuromelanin; 일부 신경세포에 축적되는 색소)에 민감한 영상을 만든다.[^p7] 건강한 뇌의 철·수초 분포를 정리한 표준 지도도 구축했다.[^atlas]

셋째는 **서로 다른 촬영 조건에서도 작동하는 재구성**이다. 학습할 때와 다른 공간 해상도(영상이 공간적 차이를 구분하는 정도)의 입력이 들어와도 기존 신경망을 사용할 수 있도록, 측정 자료를 다시 표본화하고 결과를 결합·보정하는 파이프라인을 제안했다.[^p2] 압축 센싱(희소성을 이용해 제한된 측정으로 신호를 복원하는 방법)에서는 입력마다 표본화 위치와 재구성 신경망을 고르는 방법을 연구했다.[^p8] MIMOSA(Multi-parametric Imaging using Multiple-echoes with Optimized Simultaneous Acquisition)는 영상 획득과 자기지도 재구성을 결합해 여러 정량 지도(위치마다 물리량을 수치로 나타낸 영상)를 함께 만들며, 반복 촬영에서 측정 결과의 재현성을 평가했다.[^p6]

넷째는 **의료 데이터와 여러 종류의 자료를 다루는 모델**이다. 연구 소개는 의료영상·의료 데이터를 위한 파운데이션 모델(여러 작업에 활용하도록 학습하는 기반 모델) 개발을 주요 주제로 둔다.[^research] 최근 공동연구에서는 이미지·동영상·오디오와 언어를 함께 다루는 모델 사이에서 정보의 대응 관계를 옮기는 DCAT(Directional Cross-modal Alignment Transfer)를 제안했다. 한 종류의 자료에 잘 맞춰진 모델의 정렬 정보를 다른 종류를 다루는 모델로 옮기며, 추가 미세조정 없이 성능을 높이는 방법이다.[^strong]

## 주요 연구 주제

### 1. 인공지능을 이용한 영상 획득·촬영 설계

강화학습으로 RF 파형을 설계하고, 자기지도학습으로 촬영 매개변수를 최적화한다. 여러 정량 지도를 함께 얻는 영상 획득 시퀀스(촬영을 위한 전파·자기장·신호 측정의 순서)도 개발한다.[^p1][^p5][^p6]

### 2. 뇌 미세구조의 자기 감수율·수초 영상

철·수초 분포의 분리 추정, 고자기장 χ-separation, 뇌 전체의 3차원 수초 민감 영상, 뉴로멜라닌 민감 영상과 표준 지도를 연구한다.[^p3][^p4][^p7][^atlas]

### 3. 영상 재구성·일반화와 표본화

기존 신경망을 다른 해상도의 입력에 적용하고, 입력마다 측정할 위치와 재구성망을 선택한다. 영상의 획득과 재구성을 함께 설계하는 접근이다.[^p2][^p8]

### 4. 의료 기반 모델과 멀티모달 학습

의료영상·의료 데이터를 위한 기반 모델을 개발하고, 영상·음성·언어처럼 종류가 다른 자료 사이의 대응 관계를 모델 사이에 전달하는 방법을 연구한다.[^research][^strong]

## 대표 논문

촬영 설계, 자기 감수율·수초 영상, 재구성·표본화 갈래를 고르게 담고 최근 방법 개발 논문을 포함했다. 모두 이종호 교수의 서울대 재직 시기 논문이다. '쉽게 말하면' 칸은 각 논문의 초록만을 근거로 썼다. 1·8번은 arXiv 판 초록이며, 6번은 2025년 온라인 공개·2026년 권호 논문이다.[^home]

| 번호 | 연도 | 논문 | 쉽게 말하면 | 교수 역할 |
|---|---|---|---|---|
| 1 | 2021 | [Deep reinforcement learning-designed radiofrequency waveform in MRI](https://doi.org/10.1038/s42256-021-00411-1) · Nature Machine Intelligence | RF 파형 설계는 정해진 답을 일반적으로 구하기 어려운 문제다. DeepRF는 심층 강화학습의 자기 학습으로 새 RF 펄스를 만들었다. 네 종류의 펄스에서 설계 기준을 만족하며 에너지 사용을 줄였고, 자화를 조절하는 새로운 방식을 보여 주었다.[^p1] | 마지막 저자 |
| 2 | 2025 | [Resolution generalization of deep learning-based dipole inversion networks for QSM](https://doi.org/10.1016/j.neuroimage.2025.121598) · NeuroImage | 학습 해상도와 입력 해상도가 다르면 자기 감수율을 계산하는 신경망의 성능이 떨어진다. 입력을 여러 위치에서 다시 표본화하고 기존 신경망으로 처리한 뒤 결과를 결합·보정하는 방법을 제안했다. 신경망 구조나 매개변수를 바꾸지 않고 해상도가 다른 자료에 적용하며, 비교한 두 처리 방식보다 우수한 결과를 보고했다.[^p2] | 4명 중 3번째 저자 |
| 3 | 2025 | [In-vivo high-resolution χ-separation at 7T](https://doi.org/10.1016/j.neuroimage.2025.121060) · NeuroImage | 고자기장 MRI에서 철과 수초의 분포를 구분하려면 필요한 자료의 획득과 촬영 시간 등에 어려움이 있다. 연구진은 7T에서 얻은 이완 관련 지도를 3T에서 필요한 지도로 변환하는 신경망과 새 처리 흐름을 만들었다. 여러 에코의 자료로 고해상도 χ-separation 영상을 만들고 다른 처리 흐름 및 3T 영상과 비교했다.[^p3] | 마지막 저자 |
| 4 | 2025 | [Three-Dimensional Efficient Myelin-Weighted Imaging Utilizing Direct Visualization of Short Transverse Relaxation Time Component (ViSTa)](https://doi.org/10.1002/hbm.70307) · Human Brain Mapping | 기존 2차원 ViSTa의 단일 단면 촬영 한계를 다루기 위해 뇌 전체를 덮는 3차원 촬영 방법을 제안했다. 단면 선택적 반전 RF 펄스를 촬영 순서에 결합했다. 기존 수초 수분 영상과 공간적 분포를 비교했고, 절대 정량화가 필요하지 않은 경우의 활용 가능성을 제시했다.[^p4] | 마지막 저자 |
| 5 | 2026 | [Omni-QALAS: Optimized Multiparametric Imaging for Simultaneous T1, T2 and Myelin Water Mapping](https://doi.org/10.1109/TBME.2026.3731202) · IEEE Transactions on Biomedical Engineering | 수초 수분량과 T1·T2를 함께 측정하는 촬영의 정확도와 시간을 개선하려고 촬영 각도, 준비 시간, 회복 간격을 함께 최적화했다. 전체 촬영 시간의 제약 아래 자기지도 신경망을 학습하고 재구성 방법과 결합했다. 시뮬레이션·모형·생체 실험에서 뇌 전체 정량 측정을 검증했다.[^p5] | 16명 중 11번째 저자 |
| 6 | 2026 | [MIMOSA: Multi-Parametric Imaging Using Multiple-Echoes With Optimized Simultaneous Acquisition for Highly-Efficient Quantitative MRI](https://doi.org/10.1002/mrm.70143) · Magnetic Resonance in Medicine | T1·T2·T2*, 양성자 밀도와 자기 감수율의 성분 분리 지도를 함께 얻는 새 촬영 시퀀스다. 두 영상 획득 모듈을 결합하고 자기지도학습으로 재구성했다. 모형과 생체 실험에서 기준 기법과 비교하고, 촬영을 반복해 정량 지도의 재현성을 평가했다.[^p6] | 11명 중 6번째 저자 |
| 7 | 2022 | [Sandwich spatial saturation for neuromelanin-sensitive MRI: Development and multi-center trial](https://doi.org/10.1016/j.neuroimage.2022.119706) · NeuroImage | 촬영 영역의 위와 아래에 공간 포화 펄스를 배치해 뉴로멜라닌에 민감한 영상을 만드는 sandwichNM을 제안했다. 촬영 매개변수를 맞춰 기존 방법과 비교하고 여러 제조사의 장비에서 대비의 일관성을 평가했다. 기존 촬영 시퀀스를 변경하지 않고 활용할 가능성을 보였다.[^p7] | 마지막 저자 |
| 8 | 2024 | [Adaptive Selection of Sampling-Reconstruction in Fourier Compressed Sensing](https://arxiv.org/abs/2409.11738) · ECCV 2024, arXiv 판 | 입력마다 가장 적합한 표본화 위치와 재구성 신경망을 선택하는 틀을 제안했다. 서로 다른 표본화 방식에 별도의 재구성망을 쓰고 입력의 고주파 정보에 대한 확률적 불확실성으로 선택을 돕는다. 관련 이론을 제시하고 여러 푸리에 압축 센싱 문제에서 비교 방법보다 개선된 결과를 보고했다.[^p8] | 4명 중 3번째 저자 |

## 교수와 전문 분야

이종호(Jongho Lee) 교수는 서울대학교 전기공학부에서 1998년 학사, 스탠퍼드대학교 전기공학부에서 2004년 석사와 2007년 박사를 받았다. 학과 소개는 심리학 박사부전공도 적는다. 미국 국립보건원 연구원과 펜실베이니아대학교 영상의학과 조교수를 거쳤다.[^deptprof] 연구실 누리집은 현재 전기·정보공학부 교수와 첨단융합학부 Digital Healthcare 겸무를 적는다.[^prof] 연구실은 2014년 3월 서울대로 이전했다.[^home]

학과는 전문 분야를 영상과학, 영상신호처리, 바이오메디컬 영상학 및 AI로 소개한다.[^deptprof] 최근 논문으로 보면, 촬영 물리와 인공지능을 결합하는 설계,[^p1][^p5] MRI 정량 지도의 획득·재구성,[^p2][^p6] 철·수초·뉴로멜라닌에 민감한 영상 방법[^p3][^p4][^p7]이 전문 분야다. 2026년 연구실 수상 목록은 자기 감수율 영상 연구에 대한 공로로 ISMRM(International Society for Magnetic Resonance in Medicine) Fellow에 선정됐다고 적는다.[^awards]

## 응용 분야

새 영상 방법을 과학·산업·임상 연구에 적용하는 것을 목표로 한다.[^research] 대표 논문들은 뇌 미세구조의 정량 측정과 촬영·재구성 방법 개발을 다루며, 장비나 촬영 조건의 차이에 대응하는 계산 방법을 제안한다.[^p2][^p3][^p6][^p7] 소프트웨어 페이지는 학술 연구용 제공과 상업·임상 사용의 구분을 명시하고, 상업적 이용에는 서울대학교를 통한 사용 허가가 필요하다고 안내한다.[^software]

## 구성원

2026년 10월 25일 누리집 Lab Members의 교수 외 연구 구성원 12명이다. 과정과 역할은 카드의 표기다. '대표 논문 참여'는 위 표의 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Byeongpil Moon | 석박사통합과정 |  |
| Chungseok Oh | 박사후연구원 | 1, 3 |
| Hangyeol Park | 연구원 |  |
| Hyunwoo Kim | 석박사통합과정 |  |
| Jaehyeon Koo | 석박사통합과정 |  |
| Jinah Lee, M.S | Research specialist |  |
| Jiye Kim | 박사후연구원 | 1, 3, 5, 6 |
| Jeongbeen Lee | 석박사통합과정 |  |
| Jonghyo Youn | 석박사통합과정 |  |
| Minjun Kim | 석박사통합과정 | 2, 3 |
| Rokgi Hong | 석박사통합과정 |  |
| Taechang Kim | 석박사통합과정 |  |

## 졸업생과 이전 구성원

누리집 Former Members에 적힌 연구 관련 이전 구성원이다. 학위·과정과 기간은 게시 표기이며, 서울대 이전 전 펜실베이니아대학교 시기의 구성원도 포함한다. 진로는 누리집에 적힌 곳이다.[^members][^home]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Gawon Lee | Post-doctoral scholar (2025-2026) | Research @ Seoul National University Hospital |
| Juhyung Park | Ph.D Degree (2020-2026) | AI Engineer @ LG CNS |
| Jaewoo Choi | M.S Degree (2023-2026) |  |
| Rohitkumar Datchanamourty | M.S Degree (2023-2025) | Machine Learning Engineer @ Raidium |
| Joonhyeok Yoon | Ph.D Degree (2021-2025) | Military Officer @ Republic of Korea Army |
| Hayeon Lee | M.S Degree (2023-2025) | Research Engineer @ SK Hynix |
| Hwihun Jeong | Ph.D Degree (2020-2024, Postdoc, 2024) | Postdoctoral Scholar @ Harvard University |
| Kyeongseon Min | Ph.D Degree (2017-2024) | Postdoctoral Scholar @ National Institutes of Health |
| Sooyeon Ji | Ph.D Degree (2017-2022, Postdoc, 2022-2024) | Assistant Professor @ D ivision of Computer Engineering, Hankuk University of Foreign Studies |
| Hongjun An | Ph.D Candidate (2019-) | CEO @ Wessist |
| Subin Lee | Post-doctoral scholar (2021-2022) | Research Staff @ Samsung Electronics |
| Eun-Jung Choi | Research specialist (2017-2022) | Researcher @ YBRAIN |
| Hyeong-Geol Shin | Ph.D Degree (2015-2022) | Assistant P rofessor @ Johns Hopkins University |
| Myung-Kyun Woo | Researcher (2014-2015, Postdoc, 2021-2022) | A ssociate Professor @ Department of BioMedical Engineering, Hankuk University of Foreign Studies |
| Dongmyung Shin | Ph.D Degree (2017-2022) | C E O @ OmixAI |
| Woojin Jung | Ph.D Degree (2015-2020) | Scientist @ AIRS M edical |
| Joohyun Lee | M.S Degree (2018-2020) | Staff @ Financial Security Institute |
| Jieun Lee | M.S Degree (2018-2020) | Doctor of Medicine |
| Mi-Hyun Kim | Radiological Technologist (2019-2020) |  |
| Hyunsung Eun | M.S Degree (2017-2019) | Engineer @ Motional |
| Joon Yul Choi | Research Assistant/Ph.D Degree (2013-2019) | Ass ociate Professor @ Department of Biomedical Engineering, Yonsei University |
| Jae Yeon Yoon | M.S Candidate (2017-) | Founder @ AIRS Medical |
| Doohee Lee | Ph.D Candidate (2016-) | Founder @ AIRS Medical |
| Jingyu Ko | Ph.D Candidate (2017-) | Founder @ AIRS Medical |
| Jingu Lee | Ph.D Candidate (2015-) | Former CEO & Founder @ AIRS Medical |
| Benjin Kim | M.S Candidate (2017-2018) | CEO @ Avocado Lab |
| Taehyun Hwang | MS Degree (2016-2018) | Engineer @ AIRS Medical |
| Minju Jo | M.S Degree (2016-2018) | Attorney @ Kakaomobility |
| Jini Jeong | M.S Degree (2015-2017) | Research Staff @ Samsung Electronics |
| Jee Hun Kim | M.S Degree (2015-2017) | Postdoctoral scholar @ Cleveland clinic |
| Ji-Won Baek | Research Assistant (2015-2016) |  |
| Yoonho Nam | Postdoc (2014-2015) | Ass ociate Professor @ Department of BioMedical Engineering, Hankuk University of Foreign Studies |
| Jiwon Nam | Research Specialist (2014-2015) | Research Staff @ Johnson & Johnson |
| Sung Suk Oh | Visiting Student/Postdoc (2012-2014) | Research Staff @ Daegu Gyeongbuk Medical Innovation Foundation |
| Hyo Min. Lee | M.S. Student (2013-2014) | Pos tdoctoral Scholar @ NIH |
| Sudipto Dolui | Postdoc (2013-2014) | Research Assistant Professor @ University of Pennsylvania |
| Heather Liu | Postdoc (2012-2013) | Associate Professor @ Taipei Medical Univesrsity |
| Daeun Kim | Research Assistant (2012-2013) | Engineer @ Apple |
| Randall Stafford | Postdoc (2011-2013) | Scientist @ Circle Medical |
| Se-Hong Oh | Postdoc (2011-2013) | Professor @ Department of BioMedical Engineering, Hankuk University of Foreign Studies |

## 최근 논문 목록 (2021–2026)

누리집 Journal Publications의 2021–2026년 항목 중 영상·알고리즘 개발 또는 일반 생물물리 연구에 해당하는 논문이다. 학회 논문도 이 구획에 함께 게시돼 있다. 연도·저자·서지는 누리집 표기를 따르며, 2021년 항목은 연도 구역 기준이다. 날짜 없이 게재 승인을 적은 항목은 게시 연도를 따르고 '게재 승인'으로 구분했다. 2026년 NeurIPS 항목은 '채택'으로, 학회 이름·연도만 적힌 ECCV 항목은 확인한 arXiv 판으로 표시했다.[^pubs][^strong][^p8]

**2026**

- Seo H, Lee  BH, Kim M, Mah D, Lee J, Chun SY. "Strong Helps Weak: Directional Cross-Modal Alignment Transfer in Multi-modal LLM". *NeurIPS, 2026, 채택; arXiv:2610.04580 사전 공개본*.
- Drenthen GS, Backes WH, Stalls J, van Dinther M, Voorter PHM, Lee J, Koehler S, Jansen WJ, Jansen JFA. "An improved combination of T1-weighted and FLAIR contrasts for myelin water imaging". *NeuroImage, 2026, 게재 승인*.
- Li S, Gallastegi UD, Fujita S, Chen Y, Xu P, Chan KS, Choi Y, Kim J, Piredda GF, Hilbert T, Lee J, Ye H, Gagoski B, Liu H, Bilgic B, Jun Y. "Omni-QALAS: Optimized Multiparametric Imaging for Simultaneous T1 , T2 and Myelin Water Mapping". *IEEE TBE, 2026, 게재 승인*.
- Moss HG, Sugarman MA, Lee J, Chen AA, Jensen JH, Benitez A. "The association of apparent myelin water fraction with diffusional kurtosis and biophysical modeling parameters". *NMR Biomed, 2026, 39 (10), e70377*.

**2025**

- Ji S, Kim M, Lee J\*, Shin HG\*. "Resolution Generalization of Deep Learning-based Dipole Inversion Networks for QSM". *NeuroImage, 2025, 323, 121598*.
- Chen Y, Jun Y, Heydari A, Yong X, Kim J, Lee J, Liu H, Ye H, Gagoski B, Fujita S, Bilgic B. "MIMOSA: Multi-parametric Imaging using Multiple-echoes with Optimized Simultaneous Acquisition for highly-efficient quantitative MRI". *Magn Res Med, 2025 게재 승인*.
- Oh SH, Lee GW, Lee J\*. "Three-Dimensional Efficient Myelin-weighted Imaging Utilizing Direct Visualization of Short Transverse Relaxation Time Component (ViSTa)". *Human Brain Mapping, 2025, 46 (12), e70307*.
- Shin H, Kim T, Lee J, Chun SY, Cho S, Shin  D. "Fast and accurate sparse-view CBCT reconstruction using meta-learned neural attenuation field and hash-encoding regularization". *Computers in Biology and Medicine, 2025, 189, 109900*.
- Kim J, Kim M, Ji S, Min K, Jeong H, Shin HG, Oh C, Fox RC, Sakaie KE, Lowe MJ, Oh SH, Straub S, Kim SG, Lee J\*. "In-vivo high-resolution χ-separation at 7T". *NeuroImage 2025, 308, 121060*.

**2024**

- Hong S, Bae JH, Lee J\*, Chun SY\*. "Adaptive Selection of Sampling-Reconstruction in Fourier Compressed Sensing". *European Conference on Computer Vision (ECCV), 2024; arXiv:2409.11738 판*.
- Min K, Sohn B, Kim WJ, Park CJ, Song S, Shin DH, Chang KW, Shin NY, Kim M, Shin HG, Lee PH, Lee J\*. "A human brain atlas of chi-separation for normative iron and myelin distributions". *NMR Biomed 2024, 37(12):e5226*.

**2023**

- Shin H, Kim T, Park J, Raj H, Jabbar MS, Abebaw ZD, Lee J, Van CC, Kim H, Shin D. "Pulmonary abnormality screening on chest x-rays from different machine specifications: a generalized AI-based image manipulation pipeline". *Eur Radiol Exp 2023, 7:68*.
- Lee S, Shin HG, Kim M, Lee J\*. "Depth-wise profiles of iron and myelin in the cortex and white matter". *NeuroImage 2023 273:120058*.

**2022**

- Ji S, Choi EJ, Sohn B, Baik K, Shin NY, Moon WJ, Park S, Song S, Lee PH, Shin DH, Oh SH, Kim EY, Lee J\*. "Sandwich spatial saturation for neuromelanin-sensitive MRI: Development and multi-center trial". *NeuroImage 2022 261:119706*.

**2021**

- Shin D, Kim Y, Oh C, An H, Park J, Kim J, Lee J\*. "Deep reinforcement learning-designed radiofrequency waveform in MRI". *Nature Machine Intelligence 2021 3:985-994*.

## 수상과 선정

누리집 Awards의 2022–2026년 항목과 교수 소개의 2022·2023년 수상·선정이다. 날짜는 누리집의 연도 구획이며, 학회명·수상 등급·발표 제목은 게시 표기다.[^awards][^prof]

- 2026 · Trainee Award, Best Oral Presentation in QSM: Dr Jiye Kim, "In vivo 250 μm isotropic COSMOS QSM at 7T using prospective motion correction and self-supervised learning”
- 2026 · Fellow: Professor Jongho Lee for his pioneering work in susceptibility imaging, including studying the origins of magnetic susceptibility in white matter and development of advanced susceptibility imaging methods.
- 2026 · Summa Cum Laude: Minjun Kim et al., "Harmonization for a Black-box Model using Disentanglement-based Generator and Bayesian Optimization"
- 2026 · Summa Cum Laude: Juhyung Park et al., "BrainMR Specialist: A Foundation Model of Brain MRI for Diverse Downstream Applications"
- 2026 · Magna Cum Laude: Taechang Kim et al., "Refining relaxometric constant in susceptibility source separation"
- 2026 · Magna Cum Laude: Jiye Kim et al., "Simultaneous reconstruction of longitudinal QSM data (Longitudinal-QSM)"
- 2026 · Magna Cum Laude: Jaehyeon Koo et al., "Contrast Synthesis Network Guided by Scan Parameters"
- 2026 · Our paper "A human brain atlas of χ-separation for normative iron and myelin distributions" in NMR in Biomedicine has been awarded for Top Viewed Article of 2025
- 2026 · Our paper " Recommended implementation of quantitative susceptibility mapping for clinical research in the brain: A consensus of the ISMRM electro-magnetic tissue properties study group" in Magnetic Resonance in Medicine has been awarded for Top Viewed Article of 2025
- 2026 · Our paper "Comparison between R2′-based and R2-based χ-separation methods: A clinical evaluation in individuals with multiple sclerosis" in NMR in Biomedicine has been awarded for Top Cited Article of 2025
- 2026 · Our paper " Recommended implementation of quantitative susceptibility mapping for clinical research in the brain: A consensus of the ISMRM electro-magnetic tissue properties study group" in Magnetic Resonance in Medicine has been awarded for Top Cited Article of 2025
- 2025 · Summa Cum Laude & AMPC Select: Minjun Kim et al., “Harmonization for a black-box deep learning model”
- 2025 · Summa Cum Laude: Byeongpil Moon et al., “Superior diagnostic value of susceptibility mapping over ADC in differentiating multiple system atrophy from Parkinson’s disease”
- 2025 · Magna Cum Laude: Jiye Kim et al., “Visualization of in-vivo brainstem myeloarchitecture via χ-separation at 7T”
- 2025 · Abstract award 1st place in QSM methods, Electro-Magnetic Tissue Properties Study Group Award: Taechang Kim et al., "Vessel segmentation toolbox for susceptibility imaging: Region growing and deep learning"
- 2025 · Abstract award 2nd place in QSM methods, Electro-Magnetic Tissue Properties Study Group Award: Byeongpil Moon et al., “Superior diagnostic value of susceptibility mapping over ADC in differentiating multiple system atrophy from Parkinson’s disease”
- 2025 · Abstract award 3rd place in QSM applications, Electro-Magnetic Tissue Properties Study Group Award: Jaehyeon Koo et al., "Development of x-separation (chi-separation) pipeline for UK Biobank dataset"
- 2024 · Magna Cum Laude: Hwihun Jeong et al., “MOST: MR reconstruction Optimization for multiple downStream Tasks via continual learning”
- 2024 · Magna Cum Laude: Kyeongseon Min et al., "“A human brain atlas of x-separation (chi-separation) for normative iron and myelin distributions"
- 2024 · Abstract award 1st place in QSM methods, Electro-Magnetic Tissue Properties Study Group Award: Kyeongseon Min et al., “A human brain atlas of x-separation (chi-separation) for normative iron and myelin distributions”
- 2024 · Best poster 1st place award, White Matter Study Group Award: Hayeon Lee et al., “Patterns of Popular Artifacts in QSM and chi-separation”
- 2024 · Best oral 2nd place award, White Matter Study Group Award: Kyeongseon Min et al., “A human brain atlas of x-separation (chi-separation) for normative iron and myelin distributions”
- 2024 · Abstract award 3rd place in QSM methods, Electro-Magnetic Tissue Properties Study Group Award: Byeongpil Moon et al., “Investigation and validation for cortical laminar structure of myelin and iron using x-separation (chi-separation)”
- 2024 · Best trainee poster presentation award: Chungseok Oh
- 2023 · Summa Cum Laude: Hongjun An et al., “Active dictionary learning: fast and adaptive parameter mapping for dynamic MRI”
- 2023 · Abstract award 1st place in QSM applications, Electro-Magnetic Tissue Properties Study Group Award: Sooyeon Ji et al., “In-vivo delineation of fine structures in the human brain using high resolution deep learning-powered χ-separation”
- 2023 · Best oral presentation 2nd place award, White Matter Study Group Award: Sooyeon Ji et al., “In-vivo delineation of fine structures in the human brain using high resolution deep learning-powered χ-separation”
- 2023 · Our paper "Overview of quantitative susceptibility mapping using deep learning: Current status,challenges and opportunities" in NMR in Biomedicine has been awarded for Top Cited Article of 2022
- 2022 · Summa Cum Laude: Hyeong-Geol Shin et al., “Imaging multiple sclerosis histopathology using susceptibility source separation: a postmortem brain study”
- 2022 · Best trainee abstract 2nd place, Electro-Magnetic Tissue Properties Study Group Award: Hyeong-Geol Shin et al., “Imaging multiple sclerosis histopathology using susceptibility source separation: a postmortem brain study”
- 2022 · Best trainee abstract 4th place, Electro-Magnetic Tissue Properties Study Group Award: Subin Lee et al., “Laminar profiling in advanced susceptibility imaging reveals variations in iron and myelin concentrations”
- 2022 · Best trainee abstract 2nd place, White Matter Study Group Award: Hyeong-Geol Shin et al., “Imaging multiple sclerosis histopathology using susceptibility source separation: a postmortem brain study”
- 2023 · 이종호, Gold Medal, Korean Society of Magnetic Resonance in Medicine
- 2022 · 이종호, 과학기술정보통신부 국가연구개발 우수성과 선정: Development of AI-design technology for MRI data acquisition

## 연락과 위치

- 연구실 주소: 서울특별시 관악구 관악로 1, 서울대학교 301동 1053-2호.[^home]
- 교수 연구실: 301동 1008호, 전화 02-880-7310.[^deptprof]
- 학과 연구실 상세의 전화: 02-880-4147.[^deptlab]
- 연구실 연락 이메일: jinah.lee@snu.ac.kr.[^home]
[^home]: 연구실 HOME <https://list.snu.ac.kr/> (Overview, History, Contact Information, 2026-10-25 열람).
[^research]: 연구실 RESEARCH <https://list.snu.ac.kr/research> (Primary Research Topics, 2026-10-25 열람).
[^members]: 연구실 MEMBERS <https://list.snu.ac.kr/members> (Lab Members, Former Members, 2026-10-25 열람).
[^pubs]: 연구실 PUBLICATIONS <https://list.snu.ac.kr/publications> (Journal Publications, 2021–2026년 항목, 2026-10-25 열람).
[^prof]: 연구실 Jongho Lee 소개 <https://list.snu.ac.kr/jongho-lee> (Current appointments, Previous appointments, Education, Honors and awards, 2026-10-25 열람).
[^awards]: 연구실 AWARDS <https://list.snu.ac.kr/awards> (2022–2026년 구획, 2026-10-25 열람).
[^software]: 연구실 SOFTWARE <https://list.snu.ac.kr/software> (Notice와 소프트웨어 목록, 2026-10-25 열람).
[^deptprof]: 서울대학교 전기·정보공학부 이종호 (B) 교수 소개 <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p077> (학위, 연구 분야, 주요 경력, 위치·전화, 2026-10-25 열람).
[^deptlab]: 서울대학교 전기·정보공학부 영상과학 연구실 상세 <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=94> (국·영문 연구실 이름, 지도교수, 연구 분야, 누리집, 전화, 2026-10-25 열람).
[^strong]: H. Seo, B. H. Lee, M. Kim, D. Mah, J. Lee, S. Y. Chun, “Strong Helps Weak: Directional Cross-Modal Alignment Transfer in Multi-modal LLMs”, arXiv:2610.04580 <https://arxiv.org/abs/2610.04580> (2026-10-03 사전 공개본 초록, 2026-10-25 열람).
[^atlas]: K. Min 외, J. Lee, “A human brain atlas of χ-separation for normative iron and myelin distributions”, NMR in Biomedicine 37(12), e5226, 온라인 2024-08-20. <https://pubmed.ncbi.nlm.nih.gov/39162295/> (PubMed 논문 페이지의 초록, 2026-10-25 열람).
[^p1]: D. Shin 외, J. Lee, Nature Machine Intelligence 3, 985–994 (2021). <https://doi.org/10.1038/s42256-021-00411-1> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2105.03061> (학술지 관련 DOI가 표시된 arXiv v2). (2026-10-25 열람)
[^p2]: S. Ji, M. Kim, J. Lee, H.-G. Shin, NeuroImage 324, 121598 (온라인 2025-11-20). <https://doi.org/10.1016/j.neuroimage.2025.121598> 초록 기준(PubMed 등록 초록). 초록 원문 <https://pubmed.ncbi.nlm.nih.gov/41274367/>. (2026-10-25 열람)
[^p3]: J. Kim 외, J. Lee, NeuroImage 308, 121060 (온라인 2025-01-28). <https://doi.org/10.1016/j.neuroimage.2025.121060> 초록 기준(PubMed 등록 초록). 초록 원문 <https://pubmed.ncbi.nlm.nih.gov/39884410/>. (2026-10-25 열람)
[^p4]: S.-H. Oh, G. Lee, J. Lee, Human Brain Mapping 46, e70307 (온라인 2025-08-15). <https://doi.org/10.1002/hbm.70307> 초록 기준(PubMed 등록 초록). 초록 원문 <https://pubmed.ncbi.nlm.nih.gov/40844197/>. (2026-10-25 열람)
[^p5]: S. Li 외, Y. Jun, IEEE Transactions on Biomedical Engineering (온라인 2026-09-07). <https://doi.org/10.1109/TBME.2026.3731202> 초록 기준(PubMed 등록 초록). 초록 원문 <https://pubmed.ncbi.nlm.nih.gov/42704793/>. (2026-10-25 열람)
[^p6]: Y. Chen 외, B. Bilgic, Magnetic Resonance in Medicine 95, 1528–1544 (온라인 2025-10-14). <https://doi.org/10.1002/mrm.70143> 초록 기준(PubMed 등록 초록). 초록 원문 <https://pubmed.ncbi.nlm.nih.gov/41088533/>. (2026-10-25 열람)
[^p7]: S. Ji 외, J. Lee, NeuroImage 264, 119706 (온라인 2022-10-28). <https://doi.org/10.1016/j.neuroimage.2022.119706> 초록 기준(PubMed 등록 초록). 초록 원문 <https://pubmed.ncbi.nlm.nih.gov/36349597/>. (2026-10-25 열람)
[^p8]: S. Hong, J. Bae, J. Lee, S. Y. Chun, ECCV 2024, arXiv 판 (2024). <https://arxiv.org/abs/2409.11738> 초록 기준(arXiv 판). ECCV 2024 채택 표기가 있는 arXiv v2. (2026-10-25 열람)

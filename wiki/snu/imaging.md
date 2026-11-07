# Imaging Intelligence Laboratory

**서울대학교 공과대학 기계공학부 · 이승아 부교수**

- 분야: 계산 광학, 렌즈리스 카메라, 광학 현미경, 생체 영상과 상호작용
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 광학 영상·현미경[^mask][^fp], 컴퓨터 비전[^deep], 의료 AI[^restain]
- 홈페이지: <https://imaging.snu.ac.kr/>
- 근거와 출처: [Imaging Intelligence Laboratory 근거 페이지](imaging-sources.md)

> 빛을 기록하는 장치와 영상을 복원하는 계산 방법을 함께 설계해, 카메라·현미경을 작게 만들고 생체의 구조와 움직임을 영상으로 알아보는 연구실이다.[^research][^mask][^fp]

## 무엇을 연구하나

Imaging Intelligence Laboratory는 이승아 교수가 이끄는 연구실이다. 연구의 중심은 **광학 장치와 영상 계산을 함께 설계하는 계산 영상**이다. 렌즈리스 카메라(상을 맺는 렌즈 대신 빛을 변형하는 부품과 계산으로 영상을 얻는 카메라), 현미경, 생체 영상과 사람의 상호작용을 연구한다. 이 교수와 연구실은 2025년 3월 연세대학교에서 서울대학교 기계공학부로 옮겼다.[^research][^home][^team]

일반 카메라의 렌즈를 대신하는 부품으로 **위상 마스크**를 설계·제작한다. 위상은 주기적으로 반복되는 파동이 한 주기 안에서 놓인 위치이고, 위상 마스크는 위치마다 빛의 위상을 다르게 바꾸는 부품이다. 빛을 받는 영상 센서에 기록된 무늬와 장면의 관계를 계산해 원래 장면을 복원한다. 연구실은 원하는 점 퍼짐 함수(한 점에서 나온 빛이 영상에 퍼지는 모양)를 만드는 마스크와, 센서 위에 마스크를 직접 만드는 제작 방법을 개발한다.[^mask][^imprint]

현미경에서는 **조명과 복원 방법을 함께 바꾼다**. 푸리에 타이코그래피(Fourier Ptychography)는 조명 방향 등을 바꾸며 얻은 영상들의 공간 주파수 정보를 겹쳐 결합해 대상의 진폭과 위상을 복원하는 방법이다. 진폭은 주기적으로 변하는 양이 기준값에서 가장 크게 벗어나는 정도이며, 공간 주파수는 단위 거리당 무늬가 반복되는 횟수다. 연구실은 스마트폰 화면을 조명으로 쓰는 현미경과, 세포(생명체의 구조와 기능을 이루는 기본 단위)를 배양하는 장치 안에서 살아 있는 세포를 관찰하는 소형 현미경을 개발한다.[^fp][^live]

또 다른 축은 **학습 기반 복원과 생체 영상**이다. 딥러닝은 여러 층의 신경망으로 자료의 표현을 단계적으로 학습하는 기계학습 분야이며, 기계학습은 자료에서 규칙을 학습해 새 자료를 분석하거나 예측하는 계산 방법이다. 연구실은 딥러닝을 이용해 렌즈리스 카메라의 측정값에서 장면을 복원하는 신경망 구조를 개발한다. 신경망은 연결된 계산 단위들이 입력을 변환하며 결과를 만드는 학습 모형이다.[^deep] 근적외선은 가시광선의 붉은빛에 인접한 적외선 영역이며, 적외선은 가시광선과 전파 사이 파장 영역의 전자기파다. 조직에 색을 입히는 염색을 계산으로 재현하는 가상 염색에서는, 근적외선 영상의 위상 정보를 색 영상으로 바꾸는 방법을 개발한다.[^restain]

## 주요 연구 주제

### 1. 렌즈리스 카메라의 광학 부품과 복원

마스크의 표면 모양을 빛 전파 계산으로 설계하고, 한 번의 노광(빛을 쬐어 빛에 반응하는 재료나 센서에 변화를 기록하는 과정)으로 제작하는 방법을 연구한다. 또한 자외선으로 굳는 재료에 틀의 모양을 옮겨 센서 위에 마스크를 만드는 방법을 개발한다. 센서의 측정값을 영상으로 바꾸는 과정에는 학습할 값을 가진 반복 계산 구조도 도입한다.[^mask][^imprint][^deep]

### 2. 편광·파장 정보를 함께 얻는 영상

편광은 빛을 이루는 전기장 진동 방향의 성질이다. 연구실은 편광별 빛을 구분하는 입구와 위상 마스크를 조합해 한 번의 촬영으로 선형·원형 편광 정보를 복원하는 카메라를 개발한다. 초분광 영상(여러 좁은 파장 구간의 영상을 모아 위치별 빛의 스펙트럼을 얻는 기술)에서는 위치에 따라 통과하는 파장이 달라지는 필터와 렌즈리스 카메라를 결합해 한 번의 측정으로 여러 파장 영상을 복원한다. 스펙트럼은 빛 등의 성분이 파장이나 주파수(단위 시간에 주기적 변화가 반복되는 횟수)에 따라 분포하는 모습이다.[^polar][^hyper]

### 3. 생체 구조와 혈류를 측정하는 광학·계산 방법

생체 조직의 가상 재염색에서는 화학 염색이 바랜 조직의 위상 영상과 색 영상을 짝지어 학습하고, 조직을 다시 물리적으로 염색하는 대신 색 영상을 계산한다.[^restain] 혈류 측정에서는 스펙클(빛이 산란·간섭하며 만드는 알갱이 모양 밝기 무늬)의 시간 변화를 이용한다. 롤링 셔터(영상 센서의 행을 서로 다른 시각에 순서대로 읽는 방식)의 행 사이 시간차를 이용한 측정 모형과, 그 물리 모형을 반영한 신경망을 연구한다.[^p4]

### 4. 살아 있는 미생물과 사람의 상호작용

연구 소개에는 미생물에 빛 무늬를 비추고 움직임을 보여 주는 상호작용 장치도 있다. MicroAquarium은 2020년 CHI 작업으로, 손동작을 빛 무늬로 바꾸고 실제 세포의 모습을 화면에 보여 준다. Trap it! 소개는 연세대학교 소속으로 적혀 있으며, 화면에 그린 무늬를 미생물에 비추는 과학관 전시를 다룬다. ReMember는 2021년 SIGGRAPH 작업으로, 반려동물의 심장 박동 기록을 시청각 효과와 연결한 설치물이다. 칩 크기 현미경 소개는 이 교수의 2009–2013년 작업으로 표시되어 있다.[^micro][^trap][^remember][^chip]

## 대표 논문

서울대 재직 시기인 2025년 3월 이후 출판된 논문에서 광학 설계, 편광 현미경, 가상 염색, 혈류 측정과 생체 영상 부품을 골랐다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 주요 저자는 등록 저자 순서에 따른 1저자와 이 교수의 위치를 표시한다.

| 번호 | 연도 | 논문 | 주요 저자 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2026 | [Geometry-aware phase compensation for sampling-efficient angular spectrum method](https://doi.org/10.1364/oe.586512)[^p1] | 1저자 Yong Guk Kang · 마지막 저자 Seung Ah Lee | 두꺼운 광학 부품을 지나는 빛을 계산할 때, 부품의 모양에 따라 빛의 경로가 달라지는 영향을 보정하는 방법을 제안했다. 원하는 성능에 맞는 렌즈 모양을 찾는 설계와 렌즈리스 카메라용 마스크의 제작·영상 복원으로 방법을 검증했다. |
| 2 | 2025 | [Pupil Plane Multiplexing for Vectorial Fourier Ptychography](https://doi.org/10.1002/lpor.202502183)[^p2] | 1저자 Hyesuk Chae · 마지막 저자 Seung Ah Lee | 현미경 안에서 빛이 통과하는 면을 구역별로 나누어 파장·편광별 정보를 기록하고 계산으로 분리하는 방법이다. 편광을 나누는 필터와 단색 센서로 복굴절(편광 방향에 따라 굴절 특성이 달라지는 현상)을 가진 대상의 진폭·위상을 복원했다. |
| 3 | 2025 | [Semi-supervised virtual staining using learned-illumination Fourier ptychography for high-speed label-free histopathology](https://doi.org/10.1088/2515-7647/ae270f)[^p3] | 1저자 Kyung Chul Lee · 마지막 저자 Seung Ah Lee | 조명 무늬를 학습하는 현미경과 일부 정답이 있는 자료를 이용하는 반지도 학습을 함께 설계했다. 위상 복원과 색 입히기를 분리하고 조직 고유 특징에 집중하도록 학습해, 염색하지 않은 조직 영상에서 가상 염색 영상을 만든다. |
| 4 | 2026 | [Physics-guided neural network for single-shot real-time dynamic speckle imaging](https://doi.org/10.1088/2515-7647/ae99ba)[^p4] | 1저자 Sangjun Byun · 마지막 저자 Seung Ah Lee | 스펙클 무늬의 국소 변화를 처리하는 신경망에 측정의 물리 모형을 함께 넣었다. 충분히 많은 측정값을 얻지 못할 때 생기는 잡음(측정하려는 정보에 섞이는 불필요한 변동)을 억제하고, 다양한 흐름 조건에서 실시간 혈류 지도를 얻도록 개발했다. |
| 5 | 2025 | [Beneath the surface: revealing deep-tissue blood flow in human subjects with massively parallelized diffuse correlation spectroscopy](https://doi.org/10.1117/1.nph.12.2.025007)[^p5] | 1저자 Lucas A. Kreiss · 공저자 Seung Ah Lee | 많은 빛 검출기를 병렬로 이용하고 독립적인 측정값을 평균내어 조직 속 혈류 측정의 잡음을 줄이는 장치를 제시했다. 성인에서 뇌·근육 조직의 맥동성 혈류를 측정했다. |
| 6 | 2026 | [Disposable Endoscope Cap Maintaining Clear Surgical Visualization under Fogging and Fouling](https://doi.org/10.1021/acsami.6c04312)[^p6] | 1저자 Kayoung Son · 공저자 Seung Ah Lee | 표면에 안정된 액체 사이 경계를 만드는 일회용 내시경 캡을 개발했다. 투명성을 유지하며 혈액·점액의 부착을 억제하고, 윤활액을 보충해 표면 기능을 회복하는 설계다. |

## 교수와 전문 분야

이승아 교수의 학과 직급은 부교수이며, 학과가 적은 연구 분야는 광학 이미징, 생체광학, 계산 영상 및 인공지능이다. 서울대학교 전기공학 학사(2007)·석사(2009), Caltech 전기공학 박사(2014)를 받았다.[^dept] Stanford University 박사후연구원(2014–2015), Google X 박사후연구원(2015–2016), Verily Life Sciences 연구원(2016–2018)을 거쳤다. 연구실 소개는 연세대학교 조교수(2018–2023)·부교수(2023–2025) 경력을 적고 있다.[^team]

전문 분야는 광학 부품·조명 설계와 영상 복원 알고리즘(입력 자료를 원하는 결과로 바꾸는 계산 절차)을 함께 다루는 계산 광학이다. 연구실의 카메라·현미경 연구는 장치를 작게 만드는 제작 기술, 한 번에 여러 광학 정보를 기록하는 측정 설계, 학습 기반 영상 복원을 연결한다.[^mask][^hyper][^deep]

## 응용 분야

연구실은 소형 카메라, 휴대형 현미경, 세포의 장시간 관찰과 조직 영상의 가상 염색을 연구한다. 스마트폰 현미경은 화면을 조명으로, 카메라를 영상 취득 장치로 사용하고 스마트폰 안에서 계산과 표시를 수행한다.[^fp][^live][^restain] 혈류를 영상으로 측정하는 방법과 내시경 시야를 유지하는 부품도 공동 연구한다.[^p4][^p5][^p6]

## 구성원

2026년 11월 7일 연구실 Team에 게시된 교수 외 구성원 16명이다. 과정·시작 연도·연구 주제는 게시 표기를 따르며, ‘대표 논문 참여’는 위 논문 표의 번호다. 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^team]

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Yong Guk Kang | 연구교수 | 2025 - | Computational Imaging, Interferometric Imaging, Biomedical Imaging | 1, 2, 3, 4 |
| Changyoon Yi | 박사후연구원 | 2026 - | Laser Speckle Imaging, Biomedical Imaging | 4 |
| Jaewoo Jung | 석박사통합과정 | 2020 - | Deep Learning, Lensless Imaging | 1 |
| Taeyoung Kim | 석박사통합과정 | 2021 - | Lensless Imaging, Computational Imaging, Optimization |  |
| Hyesuk Chae | 석박사통합과정 | 2022 - | Lensless Imaging, Computational Imaging | 2, 3 |
| Sangjun Byun | 박사과정 | 2026 - | Laser Speckle Imaging | 1, 4 |
| Joonsik Park | 석박사통합과정 | 2024 - | Lensless Imaging, Computational Imaging | 1 |
| Hyeonyong Lee | 석사과정 | 2024 - | Computational Imaging, Lensless Imaging | 1 |
| Donggeon Bae | 석박사통합과정 | 2024 - | Deep Learning, Biomedical Imaging | 1, 4 |
| Hyo Jun Ahn | 석박사통합과정 | 2024 - | Computational Imaging, Lensless Imaging, Laser Speckle Imaging |  |
| Jongho Kim | 석박사통합과정 | 2024 - | Deep Learning, Computational Imaging | 3, 4 |
| Hojin Chang | 석박사통합과정 | 2025 - | Computational Imaging, Lensless Imaging, Laser Speckle Imaging | 1, 4 |
| Doyeon Yoon | 학부 인턴 | 2026 - | Computational Imaging, Deep Learning |  |
| Yena Cho | 학부 인턴 | 2026 - | Computational Imaging, Lensless Imaging |  |
| Jeongmin Lee | 학부 인턴 | 2026 - | Computational Imaging, Lensless Imaging |  |
| Sangjoon Lee | 학부 인턴 | 2026 - | Computational Imaging, Deep Learning |  |

## 졸업생 진로

연구실 Alumni에 게시된 7명이다. 학위·과정과 진로는 연구실 표기를 따른다.[^team]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Kyung Chul Lee | Ph.D. in EE, Yonsei University (2025) | Postdoctoral Fellow, University of Michigan BME |
| Kyungwon Lee | Ph.D. in EE, Yonsei University (2025) | Curiosis Inc. |
| Nakkyu Baek | Ph.D. in EE, Yonsei University (2026) | Visiting Researcher, Imaging Intelligence Lab |
| Namhoon Kim | Undergraduate Intern (2023 - 2024); B.S. in EE, Yonsei University (2024) | Ph.D. Candidate, Georgia Tech ECE |
| Hansol Yoon | Researcher (2023 - 2024) | Ph.D. Candidate, Georgia Tech ECE |
| Yujin Lee | Undergraduate Intern (2021 - 2024); B.S. in EE, Yonsei University (2024) | Ph.D. Candidate, Cornell CS |
| Se Hee Lee | Undergraduate Intern (2020); B.S. in CS, Yonsei University (2020) | Line Corp. |

## 최근 5년 논문 목록

연구실 Publications의 Peer-reviewed Articles 중 2021년 10월 22일–2026년 구간에 해당하는 25편이다. 이승아 교수의 2025년 3월 서울대 부임 전 연세대 시절 논문이 함께 들어 있다. 연도·저자·발표처는 연구실 표기를 따르며, ECCV 2026 논문은 소식에서 발표한 ‘채택’으로 표시했다.[^pubs][^home]

**2026**

- Bae, D., Jung, J., Kang, Y.G., Lee, K.C., Kim, T., Kim, J., Byun, S., Park, J., and Lee, S.A. (2026). Integrated Forward–Inverse Network for Lensless Image Reconstruction. European Conference on Computer Vision 2026 (채택). <https://doi.org/10.1007/978-3-032-37517-9_35>
- Son, K., Lee, Y., Lee, K., Jo, Y., Lee, Y., Lee, S.H., Seo, M.Y., Lee, J.S., Lee, S.A., Hong, S.N., Lee, S.H.\*, Seo, J.\* (2026). Disposable Endoscope Cap Maintaining Clear Surgical Visualization under Fogging and Fouling. ACS Applied Materials & Interfaces. am-2026-043126 <https://doi.org/10.1021/acsami.6c04312>
- Kang, Y.G., Bae, D., Jung, J., Byun, S., Ahn, H.J., Chang, H., Park, J., Lee, H., & Lee, S.A. (2026). Geometry-aware phase compensation for sampling-efficient angular spectrum method. Optics Express 34, 8, 15244. <https://doi.org/10.1364/oe.586512>
- Kang, Y.G., Chae, H. and Lee, S.A. (2026). Computational space-bandwidth product expansion via multiscale aperture synthesis and wavefront engineering, Advanced Imaging, 3(3), p. 033001. [Commentary] <https://doi.org/10.3788/ai.2026.30001>

**2025**

- Chae, H., Lee, K., Kang, Y. G., Yoon, H., Lee, K. C., & Lee, S. A. (2025). Pupil Plane Multiplexing for Vectorial Fourier Ptychography. Laser & Photonics Reviews, e02183. <https://doi.org/10.1002/lpor.202502183>
- Lee, K. C., Chae, H., Kim, J., Kreiß, L., Kim, H., Kang, Y. G., ... & Lee, S. A. (2025). Semi-supervised virtual staining using learned-illumination Fourier ptychography for high-speed label-free histopathology. Journal of Physics: Photonics, 8(015025) <https://doi.org/10.1088/2515-7647/ae270f>
- Lee, H., Mun, D. J., Lee, H., Lee, K. C., Hong, S., Kim, G., Lee, S. A., Chun, S. Y. (2025). Fidelity-preserving zero-shot diffusion models for highly ill-posed inverse problems in lensless imaging. Image and Vision Computing, 105786. <https://doi.org/10.1016/j.imavis.2025.105786>
- Kreiss, L., Wu, M., Wayne, M., Xu, S., McKee, P., Dwamena, D., Kim, K., Lee, K. C., Cowdrick, K. R., Liu, W., Arin Ülkü, Harfouche, M., Yang, X., Cook, C., Lee, S. A., Buckley, E., Bruschini, C., Charbon, E. Huettel, S., & Horstmeyer, R. (2025). Beneath the surface: revealing deep-tissue blood flow in human subjects with massively parallelized diffuse correlation spectroscopy. Neurophotonics, 12(2). <https://doi.org/10.1117/1.nph.12.2.025007>
- Yoon, H., Chae, H., Lee, K. C., Lee, K., & Lee, S. A. (2025). Single-shot Fourier ptychography using polarization-encoded illumination. Applied Physics Letters, 126(12). <https://doi.org/10.1063/5.0248101>
- Jang, J., Hong, J. P., Kim, S. J., Ahn, J., Yu, B. S., Han, J., Lee, K., Ha, A., Yoon, E., Kim, W., Jo, S., Ko, H. W., Yoon, S. K., Taniguchi, T., Watanabe, K., Baek, H., Kim, D. Y., Lee, K., Mun, S., Lee, K. H., Park, S., Kim, K., Song, Y. J., Lee, S. A., Kim, H. J., Shim, J. W., Wang, G., Kang, J. H., Park, M. C., & Hwang, D. K. (2025). Conductive-bridge interlayer contacts for two-dimensional optoelectronic devices. Nature Electronics, 8, 298-308. <https://doi.org/10.1038/s41928-025-01339-9>

**2024**

- Chae, H., Kim, J., Jeon, J., Lee, K., Lee, K. C., Choi, J. U., Kang, S., Choi, S., Bang, G., Lee, J. H., Park, E., Cho, N. H., & Lee, S. A. (2024). Restoring H&E stain in faded slides via phase-to-color virtual staining in near-infrared. APL Photonics, 9(10). <https://doi.org/10.1063/5.0226277>
- Lee, K. C., Chae, H., Xu, S., Lee, K., Horstmeyer, R., Lee, S. A., & Hong, B. W. (2024). Anisotropic regularization for sparsely sampled and noise-robust Fourier ptychography. Optics Express, 32(14), 25343-25361. <https://doi.org/10.1364/oe.529023>
- Lee, K., Lee, K. C., Jung, J., Chae, H., & Lee, S. A. (2024). High-resolution display screen as programmable illumination for Fourier ptychography. Optics and Lasers in Engineering, 177, 108121. <https://doi.org/10.1016/j.optlaseng.2024.108121>
- Zhou, K. C., Harfouche, M., Zheng, M., Jönsson, J., Lee, K. C., Kim, K., Appel, R., Reamey, P., Doman, T., Saliu, V., Horstmeyer, G., Lee, S. A., & Horstmeyer, R. (2024). Computational 3D topographic microscopy from terabytes of data per sample. Journal of Big Data, 11(1), 62. <https://doi.org/10.1186/s40537-024-00901-0>
- Lee, Y., Byun, S., Yi, C., Jung, J., & Lee, S. A. (2024). Rolling shutter speckle plethysmography for quantitative cardiovascular monitoring. Biomedical Optics Express, 15(3), 1540-1552. <https://doi.org/10.1364/boe.511755>
- Xu, S., Yang, X., Ritter, P., Dai, X., Lee, K. C., Kreiss, L., Zhou, K. C., Kim, K., Chaware, A., Neff, J., Glass, C., Lee, S. A., Friedrich, O., & Horstmeyer, R. (2024). Tensorial tomographic Fourier ptychography with applications to muscle tissue imaging. Advanced Photonics, 6(2), 026004-026004. <https://doi.org/10.1117/1.ap.6.2.026004>
- Yi, C., Byun, S., Lee, Y., & Lee, S. A. (2024). Improvements and validation of spatiotemporal speckle correlation model for rolling shutter speckle imaging. Biomedical Optics Express, 15(2), 1253-1267. <https://doi.org/10.1364/boe.514497>

**2023**

- Kreiss, L., Jiang, S., Li, X., Xu, S., Zhou, K. C., Lee, K. C., Mühlberg, A., Kim, K., Chaware, A., Ando, M., Barisoni, L., Lee, S. A., Zheng, G., Lafata, K. J., Friedrich, O., & Horstmeyer, R. (2023). Digital staining in optical microscopy using deep learning - a review. PhotoniX, 4, 34. <https://doi.org/10.1186/s43074-023-00113-4>
- Kim, T., Lee, K. C., Baek, N., Chae, H., & Lee, S. A. (2023). Aperture-encoded snapshot hyperspectral imaging with a lensless camera. APL Photonics, 8, 066109. <https://doi.org/10.1063/5.0150797>
- Lee, K. C., Bae, J., Baek, N., Jung, J., Park, W., & Lee, S. A. (2023). Design and single-shot fabrication of lensless cameras with arbitrary point spread functions. Optica, 10(1), 72-80. <https://doi.org/10.1364/optica.466072>

**2022**

- Yi, C., Jung, J., Im, J., Lee, K. C., Chung, E., & Lee, S. A. (2022). Single-shot temporal speckle correlation imaging using rolling shutter image sensors. Optica, 9(11), 1227-1237. <https://doi.org/10.1364/optica.465361>
- Baek, N., Lee, Y., Kim, T., Jung, J., & Lee, S. A. (2022). Lensless polarization camera for single-shot full-Stokes imaging. APL Photonics, 7, 116107. <https://doi.org/10.1063/5.0120465>
- Lee, K., Jang, Y. K., Jung, J., Kim, D. H., Lee, H. J., & Lee, S. A. (2022, October). EuglPollock: Rethinking Interspecies Collaboration through Art Making. In Proceedings of the 30th ACM International Conference on Multimedia (pp. 1077-1084). <https://doi.org/10.1145/3503161.3548151>
- Lee, S. A., & Riedel-Kruse, I. H. (2022). Micro-HBI: Human-Biology Interaction With Living Cells, Viruses, and Molecules, Frontiers in Computer Science, 4, 849887. <https://doi.org/10.3389/fcomp.2022.849887>
- Lee, Y., Chae, H., Lee, K. C., Baek, N., Kim, T., Jung, J., & Lee, S. A. (2022). Fabrication of Integrated Lensless Cameras via UV-Imprint Lithography, IEEE Photonics Journal, 14(2), 1-8. <https://doi.org/10.1109/jphot.2022.3157373>

## 과제

연구실이 게시한 지원 기간이 최근 5년 구간과 겹치는 과제 1건이다. 2025년 3월 서울대 부임 전 연세대 시절 선정된 과제다.[^home]

- NRF Outstanding Young Scientist Grant (기간 2021년 3월 소식에서 향후 5년 지원으로 게시; 지원 NRF)

## 특허

연구실이 게시한 특허 중 출원일·등록일 가운데 하나라도 2021년 10월 22일–2026년 10월 22일에 해당하는 4건이다. 이승아 교수의 2025년 3월 서울대 부임 전 출원·등록된 특허를 함께 담았다. 누리집이 출원 공개로 적은 항목은 공개번호와 같은 출원의 등록번호·등록일을 함께 적었다.[^pubs][^patent][^patent-eye][^patent-phone][^patent-flow]

- Methods for manufacturing phase masks and lens-less camera module (발명자 SA Lee, H Chae, Y Lee, KC Lee, N Baek, T Kim, J Jung; 출원번호 US18/168,887; 출원일 2023-02-14; 등록번호 US12108134B2; 등록일 2024-10-01; 국가 US)
- Apparatus and Method for Measuring Eye Movement (발명자 SA Lee, T Kim, K Lee, N Baek, J Jung; 출원번호 US18/052,192; 출원일 2022-11-02; 등록번호 US12062190B2; 등록일 2024-08-13; 국가 US)
- Smartphone for obtaining Fourier ptychography image and method for obtaining Fourier ptychography image using smartphone (발명자 SA Lee, KC Lee, K Lee, SH Lee, J Jung; 출원번호 US17/671,513; 출원일 2022-02-14; 등록번호 US11880965B2; 등록일 2024-01-23; 국가 US)
- Light sheet imaging flow cytometer (누리집 US Patent Application, 공개번호 US20200182793A1) (발명자 CH Wu, BM Rabkin, S Sinha, JD Perreault, C Belthangady, J Higbie, SA Lee; 출원번호 US16/788,730; 출원일 2020-02-12; 등록번호 US11428633B2; 등록일 2022-08-30; 국가 US)

## 수상과 선정

연구실 Home 소식의 2022년 2월–2025년 11월 수상·선정 게시 항목 17건이다. 2025년 3월 서울대 부임 전 연세대 시절 소식이 함께 들어 있다. 인명 약칭과 상 이름의 등급은 원문 표기를 따르고, 날짜는 소식의 연월이다.[^home]

- 2025-11 · SA가 KSPE Young Engineer’s Award를 수상했다.
- 2025-10 · SPIE ABC 2025에서 HS가 Young Investigator Award, JW가 Best Poster Award를 수상했다.
- 2025-03 · NK가 SPIE Photonics West 2025 BiOS Computational Optical Imaging and AI에서 best oral presentation award를 수상했다.
- 2024-11 · HS·HJA가 OSK ABC 2024 best poster awards를 수상했다.
- 2024-05 · HS가 2024 SPIE scholarship에 선정되었다.
- 2024-04 · SA가 2023 Yonsei Teaching Excellence Award를 수상했다고 알렸다.
- 2024-03 · HS가 SPIE Photonics West 2024 BiOS Computational Optical Imaging and AI에서 best oral presentation award를 수상했다.
- 2023-11 · SPIE ABC 2023에서 TY가 Young Investigator Award, CY가 best poster award를 수상했다.
- 2023-09 · KC가 한국연구재단 차세대 연구자 fellowship에 선정되었다.
- 2023-08 · DG·HS·NK가 OSK OPC 2023 best poster awards를 수상했다.
- 2023-07 · YJ의 논문이 Optica Imaging Congress best student paper finalists에 선정되었다.
- 2023-03 · SA의 Micro-HBI 미니 리뷰 논문이 FCOMP Outstanding Article award를 수상했다.
- 2022-11 · KC가 제14회 Electronics Times Paper Awards excellence prize를 수상했다.
- 2022-11 · OSK ABC 2022에서 CY가 best presentation award, JW가 best poster award를 수상했다.
- 2022-10 · CY가 ABC 2022 Young Investigator Award를 수상했다.
- 2022-07 · Muhyeon이 OSK OPC 2022 best poster award를 수상했다.
- 2022-02 · KC가 Samsung Humantech Paper Awards silver prize를 수상했다.

## 소식

연구실 Home의 2021년 11월–2026년 6월 연구·운영 소식 23건이다. 2025년 3월 서울대 부임 전 연세대 시절 소식이 함께 들어 있으며, 날짜는 게시된 연월이다.[^home]

- 2026-06 · DG의 Integrated Forward–Inverse Network for Lensless Image Reconstruction 논문이 ECCV에 채택되었다.
- 2026-04 · YG의 Geometry-aware phase compensation for sampling-efficient angular spectrum method 논문이 출판되었다.
- 2026-03 · YG·HS의 계산 영상 관련 Commentary가 출판되었다.
- 2025-12 · HS·KC의 푸리에 타이코그래피 논문들이 게재 승인되었다.
- 2025-04 · 서울대학교 302동 411A호에서 연구실 운영을 시작했다.
- 2025-03 · 단일 촬영 푸리에 타이코그래피 논문이 출판되었다.
- 2025-02 · 2025년 3월부터 서울대학교 기계공학부로 연구실을 옮긴다고 알렸다.
- 2024-10 · HS의 가상 염색 논문이 APL Photonics에 출판되었다.
- 2024-07 · KC의 정규화 푸리에 타이코그래피 논문이 Optics Express에 출판되었다.
- 2024-02 · TY의 렌즈리스 눈 움직임 추적기 논문이 SPIE에 출판되었다.
- 2024-02 · KW의 화면 조명 기반 푸리에 타이코그래피 논문이 Optics and Lasers in Engineering에 출판되었다.
- 2024-02 · YJ·SJ의 스펙클 맥파 측정 논문이 Biomedical Optics Express에 출판되었다.
- 2024-02 · CY의 롤링 셔터 스펙클 영상 논문이 Biomedical Optics Express에 출판되었다.
- 2023-06 · TY의 렌즈리스 초분광 영상 논문이 APL Photonics에 출판되었다.
- 2023-04 · 연구실이 LG Electronics의 Target Lab으로 선정되었다.
- 2023-03 · CY의 연구가 한국연구재단 누리집에 소개되었다.
- 2023-01 · CES 2023에서 스마트폰 푸리에 타이코그래피 현미경을 선보였다.
- 2022-11 · KC의 위상 마스크 설계·제작 논문이 Optica 게재 승인되었다.
- 2022-10 · NK의 렌즈리스 편광 카메라 논문이 APL Photonics 게재 승인되었다.
- 2022-10 · CY의 롤링 셔터 스펙클 영상 논문이 Optica 게재 승인되었다.
- 2022-07 · KW의 논문이 ACM Multimedia 2022 구두 발표에 채택되었다.
- 2022-03 · YJ·HS의 렌즈리스 카메라 논문이 IEEE Photonics Journal에 출판되었다.
- 2021-11 · SPIE Photonics West 2022에 구두 발표·포스터가 채택되었다.

## 연락과 위치

- 교수 업무 이메일: seungahlee@snu.ac.kr.[^team]
- 교수 기관 전화: 02-880-7153.[^team][^dept]
- 교수 사무실: 서울대학교 301동 1503호.[^team][^dept]
- 연구실·구성원 사무실: 서울대학교 302동 411A호.[^home][^team]

## 각주
[^research]: Imaging Intelligence Laboratory, 「Research」. <https://imaging.snu.ac.kr/research> 관측 2026-11-07.
[^home]: Imaging Intelligence Laboratory, 「Home」. <https://imaging.snu.ac.kr/home> 관측 2026-11-07.
[^team]: Imaging Intelligence Laboratory, 「Team」. <https://imaging.snu.ac.kr/team> 관측 2026-11-07.
[^pubs]: Imaging Intelligence Laboratory, 「Publications」. <https://imaging.snu.ac.kr/publications> 관측 2026-11-07.
[^mask]: Imaging Intelligence Laboratory, 「Design and fabrication of custom lensless cameras」. <https://imaging.snu.ac.kr/research/phase-mask> 관측 2026-11-07.
[^imprint]: Imaging Intelligence Laboratory, 「Fabrication of Integrated Lensless Camera via UV-Imprint Lithography」. <https://imaging.snu.ac.kr/research/uv-imprint> 관측 2026-11-07.
[^fp]: Imaging Intelligence Laboratory, 「A Smartphone-Based Fourier Ptychographic Microscope Using the Display Screen for Illumination」. <https://imaging.snu.ac.kr/research/smartphone-fpm> 관측 2026-11-07.
[^live]: Imaging Intelligence Laboratory, 「Miniaturized System for Live-Cell Label-free Imaging Based on Fourier Ptychographic Microscopy」. <https://imaging.snu.ac.kr/research/live-cell-fpm> 관측 2026-11-07.
[^deep]: Imaging Intelligence Laboratory, 「Deep Learning-based Lensless Image Reconstruction」. <https://imaging.snu.ac.kr/research/deep-learning> 관측 2026-11-07.
[^restain]: Imaging Intelligence Laboratory, 「Restoring H&E stain in faded slides via phase-to-color virtual staining in near-infrared」. <https://imaging.snu.ac.kr/research/nir-virtual-re-staining> 관측 2026-11-07.
[^polar]: Imaging Intelligence Laboratory, 「Lensless polarization camera for single-shot full-Stokes imaging」. <https://imaging.snu.ac.kr/research/polarization> 관측 2026-11-07.
[^hyper]: Imaging Intelligence Laboratory, 「Snapshot Hyperspectral Imaging with a Computational Lensless Camera」. <https://imaging.snu.ac.kr/research/hyperspectral> 관측 2026-11-07.
[^micro]: Imaging Intelligence Laboratory, 「MicroAquarium: An Immersive and Interactive Installation with Living Microorganisms」. <https://imaging.snu.ac.kr/research/microaquarium> 관측 2026-11-07.
[^trap]: Imaging Intelligence Laboratory, 「Tangible Interactive Microbiology」. <https://imaging.snu.ac.kr/research/trapit> 관측 2026-11-07.
[^remember]: Imaging Intelligence Laboratory, 「Recalling Companion Animals with an Interactive Installation」. <https://imaging.snu.ac.kr/research/remember> 관측 2026-11-07.
[^chip]: Imaging Intelligence Laboratory, 「Chip-scale Microscopy for Biological Imaging」. <https://imaging.snu.ac.kr/research/copy-of-chipscale-microscopy> 관측 2026-11-07.
[^dept]: 서울대학교 기계공학부, 「이승아 (Lee, Seung Ah)」 교수 상세. <https://me.snu.ac.kr/snu__professor/%ec%9d%b4%ec%8a%b9%ec%95%84-lee-seung-ah/> 관측 2026-11-07.
[^patent]: Google Patents, 「Methods for manufacturing phase masks and lens-less camera module」, US12108134B2, 출원 2023-02-14·등록 2024-10-01. <https://patents.google.com/patent/US12108134B2/en> 관측 2026-11-07.
[^patent-eye]: Google Patents 등록 서지, 「Apparatus and method for measuring eye movement」, US12062190B2, 출원 2022-11-02·등록 2024-08-13. <https://patents.google.com/patent/US12062190B2/en> 관측 2026-11-07.
[^patent-phone]: Google Patents 등록 서지, 「Smartphone for obtaining Fourier ptychography image and method for obtaining Fourier ptychography image using smartphone」, US11880965B2, 출원 2022-02-14·등록 2024-01-23. <https://patents.google.com/patent/US11880965B2/en> 관측 2026-11-07.
[^patent-flow]: Google Patents 등록 서지, 「Light sheet imaging flow cytometer」, 출원 US16/788,730 (2020-02-12), 공개 US20200182793A1 (2020-06-11), 같은 출원의 등록 US11428633B2 (2022-08-30). <https://patents.google.com/patent/US20200182793A1/en> 관측 2026-11-07.
[^p1]: Y. G. Kang 외, S. A. Lee, Optics Express (2026). <https://doi.org/10.1364/oe.586512> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5089298785,publication_year:2021-2026> 중 해당 DOI. 관측 2026-11-07.
[^p2]: H. Chae 외, S. A. Lee, Laser & Photonics Review (2025). <https://doi.org/10.1002/lpor.202502183> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5089298785,publication_year:2021-2026> 중 해당 DOI. 관측 2026-11-07.
[^p3]: K. C. Lee 외, S. A. Lee, Journal of Physics Photonics (2025). <https://doi.org/10.1088/2515-7647/ae270f> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5089298785,publication_year:2021-2026> 중 해당 DOI. 관측 2026-11-07.
[^p4]: S. Byun 외, S. A. Lee, Journal of Physics Photonics (2026). <https://doi.org/10.1088/2515-7647/ae99ba> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5089298785,publication_year:2021-2026> 중 해당 DOI. 관측 2026-11-07.
[^p5]: L. A. Kreiss 외, R. W. Horstmeyer, Neurophotonics (2025). <https://doi.org/10.1117/1.nph.12.2.025007> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5089298785,publication_year:2021-2026> 중 해당 DOI. 관측 2026-11-07.
[^p6]: K. Son 외, J. Seo, ACS Applied Materials & Interfaces (2026). <https://doi.org/10.1021/acsami.6c04312> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5089298785,publication_year:2021-2026> 중 해당 DOI. 관측 2026-11-07.

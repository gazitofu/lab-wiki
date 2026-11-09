# 영상 및 이미지 컴퓨팅 연구실 (VIC Lab)

**KAIST 전기및전자공학부 · 김문철 교수**

- 분야: 사진·동영상의 입체 장면 복원, 영상 생성·편집, 화질 개선, 위성·항공 영상 분석, 영상 압축[^home][^prof][^dept][^ij]
- 대분야: 컴퓨팅·AI
- 태그: 컴퓨터 비전[^vision], 3차원 복원·인식[^reconstruction], 컴퓨터 그래픽스·기하 처리[^graphics], 생성 인공지능[^generation], 위성 원격탐사[^remote]
- 홈페이지: <https://www.viclab.kaist.ac.kr/>
- 근거와 출처: [영상 및 이미지 컴퓨팅 연구실 근거 페이지](viclab-sources.md)

> 사진과 동영상에서 입체 장면과 움직임을 알아내고, 새로운 시점의 영상과 편집 영상을 만들며, 화질 개선과 위성 영상 분석 방법을 연구한다.[^home]

## 무엇을 연구하나

VIC Lab은 사진·동영상에서 장면을 알아보고 원하는 영상을 만들어 내는 컴퓨터 비전(시각 자료에서 대상과 장면을 알아내거나 화질을 복원하는 기술)을 연구한다.[^vision] 연구실이 내세우는 현재 갈래는 입체 장면 복원, 영상 생성과 편집, 화질 복원, 드론·위성 영상 분석이다. 김문철 교수는 영상의 움직임, 카메라 위치와 방향, 영상 압축도 연구 분야로 적는다.[^home][^prof][^dept]

입체 장면 복원에서는 카메라가 촬영한 사진과 동영상으로 공간의 모양과 시간에 따른 변화를 알아내고, 촬영하지 않은 위치에서 보이는 영상을 합성하는 방법을 개발한다.[^reconstruction][^graphics] 광학 흐름(연속 영상에서 같은 지점이 화면상으로 이동한 양), 카메라의 위치·방향 추정, 신경 방사장과 가우시안 스플래팅을 연구한다. 신경 방사장은 Neural Radiance Field의 번역이며, 연구실은 이를 NeRF로도 적는다. 정지 장면뿐 아니라 움직이는 장면의 표현과 학습을 함께 다룬다.[^home][^prof]

영상 생성과 편집에서는 인공지능으로 새로운 사진·동영상을 만들고, 물체 단위의 편집, 영상에 들어 있는 글자의 수정, 표현 양식 변경을 연구한다.[^generation] 화질 복원에서는 초해상화(입력 영상으로부터 공간 해상도가 높은 영상을 추정하는 기술), 프레임 보간(동영상의 기존 화면 사이 시점에 해당하는 화면을 만드는 기술), 움직임에 의한 흐림 제거, 깊이 추정(영상의 각 지점이 카메라에서 떨어진 거리를 알아내는 기술), 비·안개 제거와 빈 영역 채우기를 다룬다. 해상도는 영상이 공간적으로 구별해 표현할 수 있는 세밀함을 말한다.[^home][^prof]

위성 원격탐사(위성이나 항공기에서 지표·대기를 관측하고 그 자료를 분석하는 기술)에서는 서로 다른 관측 방식으로 얻은 영상을 융합하거나 변환하고, 물체를 탐지·분류하는 인공지능 방법을 연구한다.[^remote] 광학 위성 영상의 화질을 높이고 구름에 가린 부분을 복원하는 방법, 합성개구레이더 영상의 물체 분석과 광학 영상으로의 변환이 여기에 속한다. 합성개구레이더는 Synthetic Aperture Radar의 번역이며, 연구실은 이를 SAR로 적는다. 광학 영상은 Electro-Optical의 약어인 EO로도 적는다.[^home][^prof]

## 주요 연구 주제

### 입체 장면과 새로운 시점의 영상

단일 카메라 동영상이나 여러 시점의 사진으로 장면을 복원하고, 시간에 따라 움직이는 공간을 표현한다. SplineGS는 스플라인으로 움직임을 표현하고, 카메라 값과 장면 표현을 함께 조정해 새 시점 영상을 만든다. One Look is Enough는 고해상도 사진을 나눈 조각의 깊이 추정 결과가 경계에서 어긋나는 문제를 다룬다.[^home][^p2][^p3]

### 물체별 영상 편집

영상 전체 또는 물체 하나의 수정에서 나아가, 여러 물체를 각각 원하는 영역 안에서 편집하는 문제를 연구한다. PRIMEdit는 한 물체의 편집이 다른 물체에 번지는 현상을 줄이는 구성과 평가용 자료를 제안한다. 이는 연구실이 내세운 물체 수준의 사진·동영상 편집 갈래에 해당한다.[^home][^p1]

### 화질 복원과 영상 압축

화질을 높이는 방법과 동영상에서 빠진 중간 화면을 만드는 방법을 연구한다. BiM-VFI는 가속·감속이나 방향 전환이 있는 장면의 움직임을 표현해 중간 화면을 만든다. 영상 압축에서는 사진을 여러 공간 크기로 복원할 수 있도록, 압축 자료를 여러 층으로 구성하는 COMPASS를 제안했다.[^home][^p4][^p7]

### 위성 영상 융합과 항공 물체 탐지

PAN(Panchromatic) sharpening은 공간적으로 세밀한 흑백 영상과 여러 파장대의 색 정보를 담은 영상을 결합하는 기술이다. PAN-Crafter는 두 영상의 위치가 어긋나도 색과 구조를 맞추는 방법을 연구한다. C-DiffSET는 레이더 영상에서 광학 영상을 생성할 때 관측 시점 차이로 생기는 물체 불일치를 다루며, ABBSPO는 항공 영상에 있는 물체의 위치와 방향을 추정한다.[^home][^p5][^p6][^p8]

## 대표 논문

KAIST 재직 시기의 2021–2026년 논문 가운데 연구 갈래와 최근 연구를 함께 보여 주는 8편이다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 주요 저자의 교신 표시는 연구실 논문 목록에 적힌 역할을 따른다.

| 번호 | 연도 | 논문 | 주요 저자·교수 역할 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2026 | [PRIMEdit: Probability Redistribution for Instance-Aware Multi-Object Video Editing With a New Benchmark Dataset](https://doi.org/10.1109/tpami.2026.3722239) | 1저자 Samuel Teodoro·Agus Gunawan(공동 기여), 공동 교신저자 Jihyong Oh·Munchurl Kim | 여러 물체를 각자의 영역 안에서 편집하고, 한 물체의 수정이 다른 물체로 번지는 문제를 줄이는 두 구성을 제안한다. 물체별 편집을 평가할 자료와 지표도 제시했다.[^p1] |
| 2 | 2025 | [SplineGS: Robust Motion-Adaptive Spline for Real-Time Dynamic 3D Gaussians from Monocular Video](https://doi.org/10.1109/cvpr52734.2025.02502) | 1저자 Jongmin Park·Minh-Quan Viet Bui(공동 기여), 공동 교신저자 Jihyong Oh·Munchurl Kim | 단일 카메라 동영상에서 움직이는 입체 장면을 만들기 위해 움직임을 곡선으로 표현한다. 카메라 값과 장면 표현을 함께 조정해 새로운 시점의 영상을 만든다.[^p2] |
| 3 | 2025 | [One Look is Enough: Seamless Patchwise Refinement for Zero-Shot Monocular Depth Estimation on High-Resolution Images](https://doi.org/10.1109/iccv51701.2025.00757) | 1저자 Byeongjun Kwon, 교신저자 Munchurl Kim | 큰 사진을 조각내어 깊이를 추정할 때 경계가 어긋나는 문제를 다룬다. 겹치는 조각을 함께 학습하고 학습 자료에만 맞는 편향을 줄여 기존 깊이 추정 모델에 결합할 수 있게 했다.[^p3] |
| 4 | 2025 | [BiM-VFI: Bidirectional Motion Field-Guided Frame Interpolation for Video with Non-uniform Motions](https://doi.org/10.1109/cvpr52734.2025.00679) | 1저자 Wonyong Seo, 공동 교신저자 Jihyong Oh·Munchurl Kim | 물체의 속도나 방향이 바뀌는 동영상에서 중간 화면을 만드는 방법이다. 양방향 움직임 표현과 화면 생성에 맞춘 움직임 학습을 결합해 생성 화면의 흐림을 줄였다.[^p4] |
| 5 | 2025 | [PAN-Crafter: Learning Modality-Consistent Alignment for Pan-Sharpening](https://doi.org/10.1109/iccv51701.2025.00404) | 1저자 Jeonghyeok Do, 공동 교신저자 Jaehyup Lee·Munchurl Kim | 위치가 어긋난 흑백 위성 영상과 다중 파장대 영상을 정렬하면서 결합한다. 두 영상의 구조와 색 정보가 서로 맞도록 학습해 화질을 높였다.[^p5] |
| 6 | 2026 | [C-DiffSET: Leveraging Latent Diffusion for SAR-to-EO Image Translation With Confidence-Guided Reliable Object Generation](https://doi.org/10.1109/tcsvt.2026.3701447) | 1저자 Jeonghyeok Do, Munchurl Kim 저자 참여 | 미리 학습한 영상 생성 모델을 레이더 영상의 광학 영상 변환에 적용한다. 두 관측의 시간 차이로 물체가 나타나거나 사라진 영역에서는 학습의 벌점을 낮춰 영상 구조를 보존하도록 했다.[^p6] |
| 7 | 2023 | [COMPASS: High-Efficiency Deep Image Compression with Arbitrary-scale Spatial Scalability](https://doi.org/10.1109/iccv51070.2023.01178) | 1저자 Jongmin Park, Munchurl Kim 저자 참여 | 사진을 여러 층으로 압축하고, 복원할 때 층 수와 각 층의 크기 비율을 정할 수 있게 한다. 이웃 층 사이에서 반복되는 정보를 줄이는 예측 방법을 결합했다.[^p7] |
| 8 | 2025 | [ABBSPO: Adaptive Bounding Box Scaling and Symmetric Prior based Orientation Prediction for Detecting Aerial Image Objects](https://doi.org/10.1109/cvpr52734.2025.00827) | 1저자 Woojin Lee·Hyugjae Chang(공동 기여), 공동 교신저자 Jaehyup Lee·Munchurl Kim | 수평 사각형으로 표시한 학습 자료에서 물체의 기울어진 방향까지 알아내는 방법이다. 사각형 크기를 조정하고 항공 영상 물체의 대칭성을 학습에 이용한다.[^p8] |

## 교수와 전문 분야

김문철 교수는 1996년 8월 미국 플로리다대학교에서 전기·컴퓨터공학 박사학위를 받았다. 한국전자통신연구원에서 영상 기술을 연구했으며, KAIST 경력은 2009년 3월 부교수, 2013년 9월 교수로 적혀 있다.[^prof] 최근 논문과 연구 소개를 함께 보면, 사진·동영상에서 입체 장면과 움직임을 추정하는 방법, 영상의 생성·편집과 복원, 위성 영상 처리, 학습 기반 영상 압축이 전문 분야다.[^prof][^p1][^p2][^p4][^p5][^p7]

## 응용 분야

촬영하지 않은 방향의 장면을 보여 주는 영상 합성, 물체별 사진·동영상 편집, 화질 개선과 중간 화면 생성에 응용한다. 드론·위성 영상에서는 구름 제거, 영상 융합, 레이더·광학 영상 변환과 물체 탐지·분류를 목표로 한다.[^home][^prof]

## 구성원

구성원 쪽에 게시된 박사후연구원 1명, 박사과정 20명, 석사과정 4명이다. 이름·과정·연구 주제·학교 이메일은 연구실 표기를 따랐다. 「대표 논문 참여」의 숫자는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^students][^faculties]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Geunhyuk Youk | 박사후연구원 | Deep Learning and Machine Learning; Image/Video Restoration; Optimization for Computer Vision | rmsgurkjg@kaist.ac.kr | 5 |
| Dayeon Kim | 박사과정 | Deep learning and Machine learning; Image/Video Processing; Super-Resolution | dyk4501@kaist.ac.kr |  |
| Samuel Teodoro | 박사과정 | Deep learning and Machine learning; Computer Vision | sateodoro@kaist.ac.kr | 1 |
| Wonyong Seo | 박사과정 | Deep learning and Machine learning; Frame Interpolation | wyong0122@kaist.ac.kr | 4 |
| Bogil Seo | 박사과정 | Deep learning and Machine learning; Computer Vision, Object Tracking/Detection | bogilsmart@kaist.ac.kr |  |
| Donghyun Kim | 박사과정 | Computer Vision, Video Compression; Deep Learning and Machine Learning | happyhyun94@kaist.ac.kr |  |
| Byeongjun Kwon | 박사과정 | Deep learning and Machine learning; Computer Vision, Image/Video Processing | byeongjun.kwon@kaist.ac.kr | 3 |
| Sungpyo Kim | 박사과정 | Deep learning and Machine learning; Computer Vision, Image/Video Processing | ksp04204@kaist.ac.kr | 5 |
| Yun Chen | 박사과정 | Deep Learning and Machine Learning; Computer Vision | cyruby@kaist.ac.kr |  |
| Hyugjae Chang | 박사과정 | Generative Models, Foundation Models; Segmentation/Detection | hmnc97@kaist.ac.kr | 8 |
| Semyeong Yu | 박사과정 | Deap learning and Machine learning; Computer Vision, Novel View Synthesis, 3D/4DGS | semyu01@kaist.ac.kr |  |
| Seohyun Ryu | 박사과정 | Deep learning and Machine learning; Computer Vision, Image/Video Processing | seohyun.ryu@kaist.ac.kr |  |
| Jaeho Moon | 박사과정 | Novel View Synthesis; 3D geometry understanding | jaeho.moon@kaist.ac.kr |  |
| Quan Bui | 박사과정 | Computer Vision, Depth estimation; Novel View Synthesis, NeRF, 3D/4DGS | bvmquan@kaist.ac.kr |  |
| Taehwan Kim | 박사과정 | Deep learning and Machine learning; Generative Models, Image/Video Restoration | taehwankim@kaist.ac.kr |  |
| Taewoo Suh | 박사과정 | Deep learning and Machine learning; Computer Vision, Depth estimation | twsuh@kaist.ac.kr |  |
| Woojin Lee | 박사과정 | Computer Vision, Deep Learning; Vision-Language Models, Object detection | woojin412@kaist.ac.kr | 8 |
| Byoungwoo Kim | 박사과정 | Deep learning and Machine learning; Computer vision, Super-Resolution | quddn826@kaist.ac.kr |  |
| Jaehyun Kim | 박사과정 | Deep learning, Depth estimation; Generative Models, View Synthesis | jaehyun.kim@kaist.ac.kr |  |
| Jeonghwan Yun | 박사과정 | Computer Vision, Deep Learning; NeRF, 3D/4D Gaussian Splating | opotence12@kaist.ac.kr |  |
| Luke Chen | 박사과정 | Image Processing, 3D Computer Vision; Diffusion Models, 3D/4D Gaussian Splatting | lchen64@kaist.ac.kr |  |
| Youngjun Cho | 석사과정 | Deap learning and Machine learning; Computer Vision, Image/Video Processing | cho.yj@kaist.ac.kr |  |
| Hansung Jeong | 석사과정 | Deap learning and Machine learning; Computer Vision, 3D/4D Gaussian Splatting | hsung2942@kaist.ac.kr |  |
| Hyunseo Lee | 석사과정 | Diffusion / Flow based Generative Models; Foundation, World Models | heart2002101@kaist.ac.kr |  |
| Hiep Nguyen | 석사과정 | 3D Computer Vision, Deep Learning; 3D Representation, 3D/4D Gaussian Splatting | hiepnguyen@kaist.ac.kr |  |

## 졸업생 진로

연구실 졸업생 쪽의 69행이다. 학위·과정과 졸업 연월, 연구실이 적은 진로를 함께 적었다. 이전 연구원 쪽에 같은 이름으로 게시한 직위·연구기간도 해당 행에 병기했다.[^alumni][^faculties]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jeongyeon Lim | Ph. D. (Feb. 2007) | Vice President, SK Telecom AIX Center |
| Bumshik Lee | Ph. D.; Post Doc Researcher (연구기간 2014. 01 - 2015. 03) (Feb. 2012) | Full Prof., Dept. of Energy Engineering, KENTECH |
| Yongjun Chang | Ph. D.; Research Assistant Professor (연구기간 2015. 06 - 2016. 03) (Aug. 2012) | Professor, Dept. of AI Technology, Cheju Halla University |
| Jaeil Kim | Ph. D.; Post Doc Researcher (연구기간 2015. 01 - 2015. 06) (Feb. 2015) | SK Telecom AIX Center |
| Seunghyun Cho | Ph. D. (Aug. 2015) | Researcher, Agency for Defense Development |
| Shinjee Pyo | Ph. D. (Aug. 2016) | SK Telecom AIX Center |
| Jin Jeon | Ph. D. (Feb. 2019) | SK Telecom AIX Center |
| Dae-Eun Kim | Ph. D. (Feb. 2020) | Samsung Electronics Visual Display Business Division |
| Myung Han Hyeon | Ph. D. (Feb. 2021) | Assistant Professor, Depart. of Control and Robot Engineering, Gyeongsang National University |
| Woonsung Park | Ph. D. (Feb. 2021) | Samsung Electronics Visual Display Business Division |
| Soo Ye Kim | Ph. D. (Aug. 2022) | Senior Research Scientist, Adobe Research, San Jose, CA, USA. |
| Juan Luis Gonzalez Bello | Ph. D.; Post Doc Researcher (연구기간 2023. 09 - 2024. 07) (Aug. 2023) | Research Scientist, Flawless AI, Santa Monica, CA, USA |
| Jooyoung Lee | Ph. D. (Aug. 2024) | Princapal Researcher, Electronics and Telecommunications Research Institute |
| Sangwoon Kwak | Ph. D. (Feb. 2026) | Princapal Researcher, Electronics and Telecommunications Research Institute (ETRI) |
| Agus Gunawan | Ph. D. (Feb. 2026) | Princapal Researcher, Razer, Singapore |
| Hendry | Ph. D. (Aug. 2011) | LG Electronics San Diego, USA |
| Houari Sabirin | Ph. D. (Aug. 2012) | KDDI, Japan |
| Taeyoung Na | Ph. D. (Feb. 2014) | Team Leader, SK Telecom AIX Center |
| Eunhui Kim | Ph. D. (Aug. 2015) | Researcher, Korea Institute of Science and Technology Information (KISTI) |
| Sangsoo Ahn | Ph. D. (Feb. 2016) | Korea Technology Finance Corp. (KIBO) |
| Sung-Ho Bae | Ph. D. (Aug. 2016) | Assoc. Prof., Kyung Hee Univ. |
| Yongwoo Kim | Ph. D. (Feb. 2019) | Assoc. Prof., Sang Myung Univ. |
| Jae-Seok Choi | Ph. D. (Feb. 2020) | Samsung Advanced Institute of Technology |
| Sehwan Ki | Ph. D. (Feb. 2021) | Samsung Advanced Institute of Technology |
| Hyeonjun Sim | Ph. D. (Aug. 2022) | Research Engineer, Google, Mountain View, CA, USA. |
| Jihyong Oh | Ph. D.; Post Doc Researcher (연구기간 2023. 03 - 2023. 08) (Feb. 2023) | Assiatant Prof., Chung Ang Univ. |
| Jaehyup Lee | Ph. D. (Feb. 2024) | Assistant Prof., School of Computer Science and Engineering, Kyungpook National Univ. |
| Jeonghyeok Do | Ph. D.; Post Doc Researcher (Aug. 2025) | Postdoc, KAIST |
| Hyunho Kim | Ph. D. (Feb. 2026) | Princapal Researcher, Korea Aerospace Research Institute (KARI) |
| Soomin Seo | Ph. D. (Aug. 2026) |  |
| Geunhyuk Youk | Ph. D. (Aug. 2026) | Postdoc, VIC Lab, KAIST |
| Jongmin Park | Ph. D. (Aug. 2026) | Postdoc, SNU |
| Jeewong Ryu | Master (Jul. 2003) | National IT Industry Promotion Agency |
| Yumi Sohn | Master (Feb. 2004) | Samsung Research, Samsung Electronics |
| Qonita M Shahab | Master (Aug. 2005) | Eindhoven Institute of Science Technology, Ph.D |
| Chanseok Yang | Master (Feb. 2006) | Samsung Electronics |
| Danu Pranantha | Master (Feb. 2007) | Sepuluh Nopember Institute of Technology, Indonesia |
| Peng Chen | Master (Aug. 2007) | Samsung Electronics, Beijing, China |
| Wonsang You | Master (Aug. 2008) | Assist. Prof., Depart. of Info. and Comm. Engr., Sun Moon University |
| Jihan Jung | Master (Feb. 2010) | Telecommunications Technology Association (TTA) |
| Yousun Lee | Master (Feb. 2010) | Seocho R&D Center, LG Electronicis |
| Eunkyung Park | Master (Feb. 2011) | NHN Business Platform Corp. |
| Hyuksoo Kim | Master (Feb. 2014) | Korea Institute of Science and Technology (KIST) |
| Seohyun Ryu | Master (Feb. 2015) | Defence Agency for Technology and Quality |
| Gwang-Young Youm | Master (Aug. 2017) | TmaxSoft |
| Hyunho Kim | Master (Feb. 2018) | Korea Aerospace Research Institute (KARI) |
| Jeonghun Kim | Master (Feb. 2020) | Samsung Electronics |
| Saehun Kim | Master (Aug. 2020) | Naver |
| Seongjoon Park | Master (Feb. 2004) | Incheon International Airport Corp. (IIAC) |
| Hyun Jeong | Master (Feb. 2005) | Bioinformatics Analyst II, Leidos Biomedical Research Inc. |
| Munjo Kim | Master (Feb. 2006) | Samsung Research, Samsung Electronics |
| Agus Syawal Yudhistira | Master (Feb. 2007) | Flight Focus Pte Ltd |
| Jihye Lyu | Master (Feb. 2007) | Qoniac |
| Nguyen Xuan Ha | Master (Aug. 2007) | Univ. of Saskatchewa, Canada, Ph.D |
| Changhee Kim | Master (Feb. 2009) | Seocho R&D Center, LG Electronicis |
| Yunsik Jung | Master (Feb. 2010) | Seocho R&D Center, LG Electronicis |
| Inkyung Park | Master (Feb. 2011) | Seocho R&D Center, LG Electronicis |
| Kwangsung Ha | Master (Feb. 2011) | Multimedia Process Part, Daum-Kakao |
| Leonard Yoon | Master (Feb. 2014) | KAIST, Ph.D |
| Jaehong Jung | Master (Feb. 2015) | WILUS Institute of Standards and Technology |
| Sung-Jun Yoon | Master (Feb. 2018) | LG |
| Taimoor Tariq | Master (Aug. 2019) | University of Lugano, Ph.D. |
| Dinh Vu Nam | Master (Feb. 2020) | Vietnam Posts and Telecommunications Group |
| Dac Tung Vu | Master (Feb. 2021) |  |
| Chaeyeon Son | Master (Feb. 2023) | Samsung Electronics |
| Hyebin Cho | Master (Feb. 2024) | Boeing Korea |
| Moohyun Lee | Master (Feb. 2025) |  |
| Inje Hwang | Master (Aug. 2025) |  |
| Ismail Marzuki | Post Doc.; Post Doc Researcher (연구기간 2021. 03 - 2023. 02) (Dec. 2022) | InterDigital |

## 최근 5년 논문 목록

연구실이 게시한 2021–2026년 논문 중 국제 학술지 23편, 국제 학회 36편, 국내 학술지 4편, 국내 학회 50편이다. 제목·저자·발표처는 연구실 표기를 따랐다. 학술지의 출판 전 승인은 「게재 승인」으로, 소식에서 채택을 알린 NeurIPS 2026 논문은 「채택」으로 표시했다. 학술지 논문의 2026년 권호와 게재 승인 논문을 함께 싣는다.[^ij][^ic][^dj][^dc][^neurips]

**2026**

- Jeonghyeok Do, Seungchul Lee, and Munchurl Kim, "ReFlowSET: Representation-Aligned Latent Flow Matching for SAR-to-EO Image Translation," IEEE Geoscience and Remote Sensing Letters, 게재 승인, Nov. 2026.[^ij]
- Hyun-ho Kim, and Munchurl Kim, "Electro-Optical Response-Aware Learning for PAN-Sharpening of Satellite Images," IEEE Transactions on Geoscience and Remote Sensing, Vol. 64, Article No. 5408915, Sept. 22, 2026. (DOI: 10.1109/TGRS.2026.3736376)[^ij]
- Donghyun Kim, Sung-Chang Lim, Jin Soo Choi, and Munchurl Kim, "Intra Prediction-Based OBMC Extension for Inter-Intra Boundaries," IEEE Transactions on Circuits and Systems for Video Technology, 게재 승인, Aug. 25, 2026. (DOI: 10.1109/TCSVT.2026.3729182)[^ij]
- Samuel Teodoro\*, Agus Gunawan\*, Soo Ye Kim, Jihyong Oh\*\*, and Munchurl Kim\*\*, "PRIMEdit: Probability Redistribution for Instance-aware Multi-object Video Editing with a New Benchmark Dataset," IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol. 48, Issue 11, pp. 15571-15588, Nov. 2026. (\* Co-first authors) (\*\* Co-corresponding authors) (DOI: 10.1109/TPAMI.2026.3722239)[^ij]
- Jeonghyeok Do, Jaehyup Lee, Seungchul Lee, and Munchurl Kim, "C-DiffSET: Leveraging Latent Diffusion for SAR-to-EO Image Translation with Confidence-Guided Reliable Object Generation," IEEE Transactions on Circuits and Systems for Video Technology, Vol. 36, Issue 10, pp. 14604-14620, Oct. 2026. (DOI: 10.1109/TCSVT.2026.3701447)[^ij]
- Jaeho Moon, Jeonghwan Yun, Jaehyun Kim, Jaehyup Lee, and Munchurl Kim, "Diffusion-based Data Augmentation and Knowledge Distillation with Generated Soft Labels for Oil Spill Segmentation Learning on Satellite SAR Images," IEEE Transactions on Circuits and Systems for Video Technology, vol. 36, Issue 9, pp. 12978-12993, Sept. 2026. (DOI: 10.1109/TCSVT.2026.3701691)[^ij]
- Jaehyun Kim, Wonyong Seo, and Munchurl Kim, "FS-SegDiff: Mitigating Intra-class Variation and Attention Leakage for Robust Diffusion-based Few-shot Semantic Segmentation," IEEE ACCESS, Vol. 14, pp. 13053-13069, Jan. 19, 2026. (DOI: 10.1109/ACCESS.2026.3655413)[^ij]
- Jooyoung Lee, Se Yoon Jeong, and Munchurl Kim, "DeepHQ: Learned Hierarchical Quantizer for Progressive Deep Image Coding," ACM Transactions on Multimedia Computing Communications and Applications, Vol. 22, Issue 1, Article No. 18, pp. 1-24, Jan. 12, (DOI: 10.1145/3773994).[^ij]
- Samuel Teodoro, Yun Chen, Agus Gunawan, Soo Ye Kim, Jihyong Oh††, and Munchurl Kim††, "MotionGrounder: Grounded Multi-Object Motion Transfer via Diffusion Transformer", The Fortieth Annual Conference on Neural Information Processing Systems (NeurIPS), International Convention Centre Sydney (ICC Sydney), Australia, Dec. 5-12, 2026. (††: Co-corresponding authors) (채택)[^ic]
- Jongmin Park†, Jeonghwan Yun†, Minh-Quan Viet Bui, and Munchurl Kim, "WebSpline: Structure-Informed Splines for Real-Time 3D Gaussians from Monocular Videos", The Fortieth Annual Conference on Neural Information Processing Systems (NeurIPS), International Convention Centre Sydney (ICC Sydney), Australia, Dec. 5-12, 2026. (†: Equal Contribution) (채택)[^ic]
- Jeonghyeok Do and Munchurl Kim, "GeoCore-9B: Towards Geo-Aware Generative Foundation Models in Earth Observation", The Fortieth Annual Conference on Neural Information Processing Systems (NeurIPS), International Convention Centre Sydney (ICC Sydney), Australia, Dec. 5-12, 2026. (채택) DOI: 10.48550/arxiv.2608.01896[^ic]
- Jeonghyeok Do, Yun Chen, Geunhyuk Youk, and Munchurl Kim, "Less is More: Compact-Token Masked Feature Learning for Skeleton Representation Learning", The Fortieth Annual Conference on Neural Information Processing Systems (NeurIPS), International Convention Centre Sydney (ICC Sydney), Australia, Dec. 5-12, 2026. (채택)[^ic]
- Minh-Quan Viet Bui, Jaeho Moon and Munchurl Kim, "AirSplat: Alignment and Rating for Robust Feed-Forward 3D Gaussian Splatting", European Conference on Computer Vision (ECCV), Sept. 8-12, 2026, Malmö, Sweden. DOI: 10.1007/978-3-032-37174-4_31[^ic]
- Byoungwoo Kim and Munchurl Kim, "ProSR: Semantic-Prototype-Guided Discrete Modeling for Physically Consistent SAR Super-Resolution", European Conference on Computer Vision (ECCV), Sept. 8-12, 2026, Malmö, Sweden. DOI: 10.1007/978-3-032-37261-1_30[^ic]
- Geunhyuk Youk, Jihyong Oh, and Munchurl Kim, "AVSR-Diff: Scale-Agnostic Diffusion Priors for Temporally Consistent Arbitrary-Scale Video Super-Resolution", European Conference on Computer Vision (ECCV), Sept. 8-12, 2026, Malmö, Sweden.[^ic]
- Geunhyuk Youk, Jihyong Oh, and Munchurl Kim, "FMA-Net++: Motion- and Exposure-Aware Joint Video Super-Resolution and Deblurring", European Conference on Computer Vision (ECCV), Sept. 8-12, 2026, Malmö, Sweden. DOI: 10.1007/978-3-032-37035-8_35[^ic]
- Hyunho Kim, Jaehyup Lee, and Munchurl Kim, "Video Can Teach PAN-Sharpening: PSF-Aware Cross-Domain Supervision", European Conference on Computer Vision (ECCV), Sept. 8-12, 2026, Malmö, Sweden. DOI: 10.1007/978-3-032-36987-1_9[^ic]
- Wonyong Seo, Jaeho Moon, Jaehyup Lee, Soo Ye Kim, Munchurl Kim, "PropFly: Learning to Propagate via On-the-Fly Supervision from Pre-trained Video Diffusion Models", Computer Vision and Pattern Recognition (CVPR), June 3-7, 2026, Colorado, Denver, USA.[^ic]
- Minh-Quan Viet Bui, Jongmin Park, Juan Luis Gonzalez, Jaeho Moon, Jihyong Oh, Munchurl Kim, "EcoSplat: Efficiency-controllable Feed-forward 3D Gaussian Splatting from Multi-view Images", Computer Vision and Pattern Recognition (CVPR), June 3-7, 2026, Colorado, Denver, USA.[^ic]
- Agus Gunawan, Samuel Teodoro, Yun Chen, Soo Ye Kim, Jihyong Oh, Munchurl Kim, "A Training-Free Generalist for Controllable Text-Image Manipulation", International Conference on Learning Representations (ICLR), April 23-27, 2026, Riocentro Convention and Event Center, Rio de Janeiro, Brazil.[^ic]
- Minh-Quan Viet Bui†, Jongmin Park†, Juan Luis Gonzalez, Jaeho Moon, Jihyong Oh††, Munchurl Kim††, "MoBGS: Motion Deblurring Dynamic 3D Gaussian Splatting for Blurry Monocular Video", The 40th Annual AAAI Conference on Artificial Intelligence (AAAI), Vol. 40 No. 4: AAAI-26 Technical Tracks 4, Jan. 20-27, 2026, Singapore EXPO, Singapore. (†: Equal Contribution, ††: Co-corresponding authors) DOI: 10.1609/aaai.v40i4.37234[^ic]
- Jongmin Park and Munchurl Kim, "Dynamic Deblurring 3D Gaussian Splatting for Blurry Monocular Video", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- Minh-Quan Viet Bui and Munchurl Kim, "EcoSplat: Efficiency Controllable Feed-Forward 3D Gaussian Splatting from Multi View Images", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- Taewoo Suh, Sungpyo Kim, Jongmin Park and Munchurl Kim, "AA-Splat: Anti-Aliased Feed-forward 3D Gaussian Splatting", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- 유세명, 김문철, "다양한 3D 어노테이션을 활용한 신규 시점 이미지 생성", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- Jeonghwan Yun, Jongmin Park and Munchurl Kim, "Joint Camera Bundle Adjustment and Spline-based Motion Modeling for Monocular Dynamic 3D Gaussians", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- Sungpyo Kim and Munchurl Kim, "Generalizable Arbitrary-Scale 3D Reconstruction via Super-Resolution Neural Operators", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- 서수민, 김문철, "SAR-EO 멀티모달 상호보완적 마스크 가이드 교차 어텐션을 이용한 위성 영상에서의 구름 제거", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- 도정혁, 이승철, 김문철, "확산 모델을 이용한 고정밀 SAR 영상의 광학 도메인 변환 및 활용 전략", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- 육근혁, 김문철, "확산 모델 기반의 임의 스케일 비디오 초해상화를 위한 연속적 디코딩 기법", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- 김다연, 김문철, "이차 비디오 프레임 보간을 위한 플로우 그래디언트 신뢰도 기반 운동학적 조건 추출 기법", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- 김병우, 김문철, "자기지도 학습 모델을 활용한 의미적 정렬 기반 SAR 영상 초해상화", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- 김재현, 김문철, "SAM3 모델을 활용한 시간 규모별 움직임 인식 기반 참조 영상 객체 분할", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- 김태환, 김성표, 서태우, 김문철, "저조도 원시 영상에 대한 디모자이킹, 디노이징, 초해상화 및 톤 매핑 통합 파이프라인", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- 이우진, 장혁재, 김문철, "ABBSPO: 항공 영상 객체 탐지를 위한 적응형 바운딩 박스 스케일링 및 대칭 사전 지식 기반 방향 예측 기법", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- Jaeho Moon, Wonyong Seo and Munchurl Kim, "Propagation-based Video Editing using Pre-trained Video Diffusion Models", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- Wonyong Seo, \*Jihyong Oh and Munchurl Kim, "BiM-VFI: Bidirectional Motion Field-Guided Frame Interpolation for Video with Non-uniform Motions", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일. DOI: 10.1109/cvpr52734.2025.00679[^dc]
- Yun Chen, Jeonghyeok Do and Munchurl Kim, "Skeleton-aware augmentation for Skeleton Representation Learning", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- Samuel Teodoro and Munchurl Kim, "Improving Motion Transfer in Diffusion Transformers via Temporal Weighting", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]
- Hyugjae Chang, Woojin Lee and Munchurl Kim, "CT-FSOD: CLIP-Based Text-Guided Few-Shot Object Detection", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일. DOI: 10.1109/access.2025.3604521[^dc]
- Byeongjun Kwon, Taewoo Suh and Munchurl Kim, "Score Distillation Sampling for Image Colorization", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. , 롯데호텔 제주, 2026년 06월 18일 ~ 2026년 06월 20일.[^dc]

**2025**

- Hyun-ho Kim, and Munchurl Kim, "A Dual-Decoder-VAE Based Latent Diffusion Model for PAN-sharpening," IEEE Geoscience and Remote Sensing Letters, Vol.22, pp.1-5, Article No. 5002905 Sept. 2025. (DOI: 10.1109/LGRS.2025.3615226)[^ij]
- Hyugjae Chang\*, Woojin Lee\*, and Munchurl Kim, "CT-FSOD: CLIP-based Text-guided Few-Shot Object Detection," IEEE ACCESS, Vol. 13, pp. 158250-158265, Sept.15, 2025. (DOI: 10.1109/ACCESS.2025.3604521) (\* Co-first author) (DOI: 10.1109/ACCESS.2025.3604521)[^ij]
- Minh-Quan Viet Bui\*, Jongmin Park\*, Jihyong Oh†, and Munchurl Kim†, "MoBluRF: Motion Deblurring Neural Radiance Fields for Blurry Monocular Video," IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol. 47, Issue 9, pp. 7752-7770, Sept. 2025. (\*: equal contribution, †: co-corresponding authors) (DOI: 10.1109/TPAMI.2025.3574644)[^ij]
- Hyun-ho Kim, and Munchurl Kim, "FBS-PS: Fully Band-Separable PAN-Sharpening Considering the Physical Characteristics of Electro-Optical Sensors," IEEE Transactions on Geoscience and Remote Sensing, Vol. 63, Article No. 5400420, Jan. 8, 2025. (DOI: 10.1109/TGRS.2024.3523865)[^ij]
- Jeonghyeok Do, Munchurl Kim†, "Bridging the Skeleton-Text Modality Gap: Diffusion-Powered Modality Alignment for Zero-shot Skeleton-based Action Recognition", International Conference on Computer Vision (ICCV), Oct. 19-23, 2025, Honolulu, Hawaii, USA. (†: Corresponding author)[^ic]
- Jeonghyeok Do, Sungpyo Kim, Geunhyuk Youk, Jaehyup Lee†, Munchurl Kim†, "PAN-Crafter: Learning Modality-Consistent Alignment for PAN-Sharpening", International Conference on Computer Vision (ICCV), pp. 4242-4252, Oct. 19-23, 2025, Honolulu, Hawaii, USA. (†: Co-corresponding authors) DOI: 10.1109/iccv51701.2025.00404[^ic]
- Byeongjun Kwon, Munchurl Kim†, "One Look is Enough: Seamless Patchwise Refinement for Zero-Shot Monocular Depth Estimation on High-Resolution Images", Internal Conference on Computer Vision (ICCV), Oct. 19-23, 2025, Honolulu, Hawaii, USA. (†: Corresponding author) DOI: 10.1109/iccv51701.2025.00757[^ic]
- Jongmin Park†, Minh-Quan Viet Bui†, Juan Luis Gonzalez, Jaeho Moon, Jihyong Oh††, Munchurl Kim††, "SplineGS: Robust Motion-Adaptive Spline for Real-Time Dynamic 3D Gaussians from Monocular Video", Computer Vision and Pattern Recognition (CVPR), June 11-15, 2025, the Music City Center, Nashville, Tennessee (TN), USA. (†: Equal Contribution, ††: Co-corresponding authors) DOI: 10.1109/cvpr52734.2025.02502[^ic]
- Wonyong Seo, Jihyong Oh†, Munchurl Kim†, "BiM-VFI: Bidirectional Motion Field-Guided Frame Interpolation for Video with Non-uniform Motions," Computer Vision and Pattern Recognition (CVPR), June 11-15, 2025, the Music City Center, Nashville, Tennessee (TN), USA. (†: Co-corresponding authors) DOI: 10.1109/cvpr52734.2025.00679[^ic]
- Sungpyo Kim, Jeonghyeok Do, Jaehyup Lee†, Munchurl Kim†, "U-Know-DiffPAN: An Uncertainty-aware Knowledge Distillation Diffusion Framework with Details Enhancement for PAN-Sharpening," Computer Vision and Pattern Recognition (CVPR), pp. 23069-23079, June 11-15, 2025, the Music City Center, Nashville, Tennessee (TN), USA. (†: Co-corresponding authors) DOI: 10.1109/cvpr52734.2025.02148[^ic]
- Woojin Lee†, Hyugjae Chang†, Jaeho Moon, Jaehyup Lee††, Munchurl Kim††, "Adaptive Bounding Box Scaling and Symmetric Prior based Orientation Prediction for Detecting Aerial Image Objects," Computer Vision and Pattern Recognition (CVPR), June 11-15, 2025, the Music City Center, Nashville, Tennessee (TN), USA. (†: Equal Contribution, ††: Co-corresponding authors)[^ic]
- Sangwoon Kwak, Joonsoo Kim, Jun Young Jeong, Won-Sik Cheong, Jihyong Oh†, Munchurl Kim†, "MoDec-GS: Global-to-Local Motion Decomposition and Temporal Interval Adjustment for Compact Dynamic 3D Gaussian Splatting," Computer Vision and Pattern Recognition (CVPR), June 11-15, 2025, the Music City Center, Nashville, Tennessee (TN), USA. (†: Co-corresponding authors) DOI: 10.1109/cvpr52734.2025.01059[^ic]
- Samuel Teodoro, Yun Chen, Munchurl Kim, "Attention Modulation for Improved Textual Alignment in Motion Transfer", 한국방송·미디어공학회 동계학술대회 발표 논문집, pp. 335-336, 강원도 휘닉스파크, 2025.12.29-30.[^dc]
- 김다연, 김문철, "시공간 비디오 동시 초해상화를 위한 흐름 인식 상호 시공간 어텐션과 암시적 신경 표현", 한국방송·미디어공학회 동계학술대회 발표 논문집, pp. 337-338, 강원도 휘닉스파크, 2025.12.29-30.[^dc]
- 김병우, 김문철, "과제 적합 손실을 활용한 SAR 영상 초해상화", 한국방송·미디어공학회 동계학술대회 발표 논문집, pp. 339-340, 강원도 휘닉스파크, 2025.12.29-30.[^dc]
- 김재현, 김문철, "가우시안 블러를 이용한 Diffusion 기반 Few-shot 의미 분할", 한국방송·미디어공학회 동계학술대회 발표 논문집, pp. 341-342, 강원도 휘닉스파크, 2025.12.29-30.[^dc]
- 김태환, 김병우, 김문철, "잠재 확산 모델 기반 SAR 영상 초해상화를 통한 SAR 영상 객체 탐지 향상", 한국방송·미디어공학회 동계학술대회 발표 논문집, pp. 343-344, 강원도 휘닉스파크, 2025.12.29-30.[^dc]
- Jeonghyeok Do, Munchurl Kim, "Beyond Fixed Partitions: Learning Dynamic Joint Grouping for Skeleton-based Action Recognition", 한국방송·미디어공학회 동계학술대회 발표 논문집, pp. 345-346, 강원도 휘닉스파크, 2025.12.29-30.[^dc]
- 서수민, 김문철, "SAR 정보를 활용한 잠재 확산 모델 기반 EO Cloud Removal 및 복원", 한국방송·미디어공학회 동계학술대회 발표 논문집, pp. 347-348, 강원도 휘닉스파크, 2025.12.29-30.[^dc]
- Taewoo Suh, Munchurl Kim, "DIFT-Flow: Diffusion Model Features for Optical Flow Estimation", 한국방송·미디어공학회 동계학술대회 발표 논문집, pp. 349-350, 강원도 휘닉스파크, 2025.12.29-30.[^dc]
- 유세명, 김문철, "비동기 다중 시점 비디오 입력을 이용한 동적 3D 장면 재구성", 한국방송·미디어공학회 동계학술대회 발표 논문집, pp. 351-352, 강원도 휘닉스파크, 2025.12.29-30.[^dc]
- 윤정환, 김문철, "효율적인 뷰 합성을 위한 다중 해상도 텐서 방사 필드", 한국방송·미디어공학회 동계학술대회 발표 논문집, pp. 353-354, 강원도 휘닉스파크, 2025.12.29-30.[^dc]
- 이우진, 장혁재, 김문철, "CLIP 기반 텍스트 가이드 프로토타입 초기화를 이용한 Few-Shot 객체 탐지", 한국방송·미디어공학회 동계학술대회 발표 논문집, pp. 355-356, 강원도 휘닉스파크, 2025.12.29-30.[^dc]

**2024**

- Juan Luis Gonzalez Bello\*, Minh-Quan Viet Bui\*, and Munchurl Kim, "ProNeRF: Learning Efficient Projection-Aware Ray Sampling for Fine-Grained Implicit Neural Radiance Fields," IEEE ACCESS, vol. 12, pp. 56799-56814, April 15, 2024. (DOI: 10.1109/ACCESS.2024.3390753) (\* Co-first author)[^ij]
- Wonyong Seo, Woonsung Park and Munchurl Kim, "Lightweight Optical Flow Estimation using 1D Matching," IEEE ACCESS, vol. 12, pp. 45560– 45571, Mar. 2024. (DOI: 10.1109/ACCESS.2024.3380917)[^ij]
- Hyun-ho Kim, and Munchurl Kim, "Deep Spectral Blending Network for Color Bleeding Reduction in Pan-sharpening Images," IEEE Transactions on Geoscience and Remote Sensing, vol. 62, pp. Mar. 2024. (DOI: 10.1109/TGRS.2024.3378158)[^ij]
- Juan Luis Gonzalez Bello, Jaeho Moon, and Munchurl Kim, "Self-Supervised Monocular Depth Estimation with Positional Shift Depth Variance and Adaptive Disparity Quantization," IEEE Transactions on Image Processing, vol. 33, pp. 2074 - 2089, 12 March 2024. (DOI: 10.1109/TIP.2024.3374045).[^ij]
- Myung Han Hyun, Bumshik Lee, and Munchurl Kim, "A VVC Intra Rate Control with Small Bit Fluctuations Using a Lagrange Multiplier Adjustment," IEEE Transactions on Multimedia, vol. 26, pp. 6811-6821, Jan. 2024. (DOI:10.1109/TMM.2024.3355633).[^ij]
- Jooyoung Lee, Seunghyun Cho, and Munchurl Kim, “An End-to-End Joint-learning Scheme of Image Compression and Quality Enhancement with Improved Entropy Minimization”, J. Lee, S. Cho, and M.Kim, An end-to-end joint learning scheme of imagecompression and quality enhancement withimproved entropy minimization, ETRI Journal, vol. 46, issue 6, pp. 935–949, Dec. 2024. (DOI: 10.4218/etrij.2023-0275).[^ij]
- Jaehyup Lee, Hyun-Ho Kim, Doochun Seo, and Munchurl Kim, "Segmentation-Guided Context Learning Using EO Object Labels for Stable SAR-to-EO Translation," IEEE Geoscience and Remote Sensing Letters, vol. 21, article number 4001305, pp. 1-5, Jan. 2024. (DOI: 10.1109/LGRS.2023.3344804)[^ij]
- Jeonghyeok Do and Munchurl Kim, "SkateFormer: Skeletal-Temporal Transformer for Human Action Recognition", European Conference on Computer Vision (ECCV), Milano, Italy, Sept. 29- Oc. 4, 2024. DOI: 10.1007/978-3-031-72940-9_23[^ic]
- Geunhyuk Youk, Jihyong Oh†, and Munchurl Kim†, "FMA-Net: Flow Guided Dynamic Filtering and Iterative Feature Refinement with Multi-Attention for Joint Video Super-Resolution and Deblurring," Computer Vision and Pattern Recognition (CVPR), Seattle, Washington, USA, June 17-21, 2024. (†: Co-corresponding authors) DOI: 10.1109/cvpr52733.2024.00013[^ic]
- Jaeho Moon, Juan Luis Gonzalez, Byeongjun Kwon, and Munchurl Kim, "From-Ground-To-Objects: Coarse-to-Fine Self-supervised Monocular Depth Estimation of Dynamic Objects with Ground Contact Prior," Computer Vision and Pattern Recognition (CVPR), Seattle, Washington, USA, June 17-21, 2024. DOI: 10.1109/cvpr52733.2024.01001[^ic]
- Juan Luis Gonzalez and Munchurl Kim, "Novel View Synthesis with View-Dependent Effects from a Single Image," Computer Vision and Pattern Recognition (CVPR), Seattle, Washington, USA, June 17-21, 2024. DOI: 10.1109/cvpr52733.2024.00991[^ic]
- 황인제, 이우진, 김문철, "임의 스케일 이미지 초해상화를 위한 효율적 확산 모델 기반 이미지 프라이어 활용 암시적 이미지 함수 학습", 방송공학회논문지 제29권 제6호, pp. 981-998, 2024년 11월. (DOI: https://doi.org/10.5909/JBE.2024.29.6.981)[^dj]
- 김태환, 김문철, "혼합 열화 영상 복원을 위한 2단계 U-Net 트랜스포머", 방송공학회논문지 제29권 제6호, pp. 888-905, 2024년 11월. (DOI: https://doi.org/10.5909/JBE.2024.29.6.888)[^dj]
- 권병준, 김문철, "비정렬 열화상 이미지와 RGB 이미지에 대한 상호 참조 및 융합을 통한 듀얼 모달 깊이 추정", 방송공학회논문지 제29권 제6호, pp. 866-878, 2024년 11월. (DOI: https://doi.org/10.5909/JBE.2024.29.6.866)[^dj]
- 황인제, 김다연, 김문철, "SAR 이종 참조 영상 활용 EO 위성 영상 초해상화 트랜스포머 연구", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. 1,174-1,177, 메종글래드 제주 호텔, 2024.06.25-28.[^dc]
- 이우진, 황인제, 김문철, "효율적 트랜스포머 네트워크를 이용한 임의의 배율로의 영상 초해상화에 관한 연구", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. 1,170-1,173, 메종글래드 제주 호텔, 2024.06.25-28.[^dc]
- 김재현, 김성표, 이무현, 김문철, "효율적인 디퓨전 모델 기반 초해상화 연구", 한국방송·미디어공학회 하계학술대회발표 논문집, pp. 1,166-1,169, 메종글래드 제주 호텔, 2024.06.25-28.[^dc]
- Sungpyo Kim and Munchurl Kim, "Pan-sharpening using Denoising Diffusion model", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. 995-997, 메종글래드 제주 호텔, 2024.06.25-28.[^dc]
- Taehwan Kim and Munchurl Kim, "TUT: Two-stage U-Net-based Transformer for Image Restoration with Mixed Degradation", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. 991-994, 메종글래드 제주 호텔, 2024.06.25-28.[^dc]
- 이우진, 장혁재, 김문철, "효율적 트랜스포머를 이용한 SAR 영상 내 선박 탐지 및 식별에 관한 연구", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. 988-990, 메종글래드 제주 호텔, 2024.06.25-28.[^dc]
- 윤정환, 문재호, 김문철, "트랜스포머 기반 네트워크를 활용한 SAR 유류 유출 탐지 전이 학습 기법", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. 964-967, 메종글래드 제주 호텔, 2024.06.25-28.[^dc]
- Taewoo Suh and Munchurl Kim, "Segmentation-Guided Masked Autoencoder Pretraining for Optical Flow Estimation", 한국방송·미디어공학회 하계학술대회발표 논문집, pp. 920-923, 메종글래드 제주 호텔, 2024.06.25-28.[^dc]
- Agus Gunawan and Munchurl Kim, "CCLNet: Cross Content Laplacian Network for Modernizing Cultural Heritage Images", 한국방송·미디어공학회 하계학술대회발표 논문집, pp. 916-919, 메종글래드 제주 호텔, 2024.06.25-28.[^dc]
- Byeongjun Kwon and Munchurl Kim, "Multi-modal Depth Estimation from Misaligned Thermal and RGB Images", 한국방송·미디어공학회 하계학술대회 발표 논문집, pp. 912-913, 메종글래드 제주 호텔, 2024.06.25-28.[^dc]

**2023**

- Jaehyup Lee, Hyebin Cho, Doochun Seo, Hyun-ho Kim, Jaeheon Jeong, and Munchurl Kim, "CFCA-SET: Coarse-to-Fine Context-Aware SAR-to-EO Translation with Auxiliary Learning of SAR-to-NIR Translation," IEEE Transactions on Geoscience and Remote Sensing, vol. 61, article no. 5217118, pp. 1-18, Sept. 2023. (DOI: 10.1109/TGRS.2023.3318980)[^ij]
- Geunhyuk Youk and Munchurl Kim, "Transformer-based Synthetic-to-Measured SAR Image Translation via Learning of Representational Features," IEEE Transactions on Geoscience and Remote Sensing, vol. 61, article no. 5206318, pp. 1-18, April 2023. (DOI: 10.1109/TGRS.2023.3267480)[^ij]
- Agus Gunawan, Soo Ye Kim, Hyeonjun Sim, Jae-Ho Lee, Munchurl Kim, "Modernizing Old Photos Using Multiple References via Photorealistic Style Transfer," Computer Vision and Pattern Recognition (CVPR), Vancouver, Canada, June 18-22, 2023.[^ic]
- Jongmin Park, Jooyoung Lee and Munchurl Kim, "COMPASS: High-Efficiency Deep Image Compression with Arbitrary-scale Spatial Scalability," International Conference on Computer Vision (ICCV), Paris, France, Oct. 2-6, 2023. DOI: 10.1109/iccv51070.2023.01178[^ic]
- Sangwoon Kwak, Joungil Yun, Hyon-Gon Choo, and Munchurl Kim, "Feature-Guided Machine-Centric Image Coding for Downstream Tasks," 2023 IEEE International Conference on Multimedia and Expo Workshops (ICMEW), pp. 176-181, July 10 2023 to July 14 2023, Brisbane, Australia. DOI: 10.1109/icmew59549.2023.00037[^ic]
- Dayeon Kim, Munchurl Kim, "SGSR: A Saliency-Guided Image Super-Resolution Network," International Conference on Image Processing (ICIP), Kuala Lumpur, Malaysia, Oct. 8 -11, 2023. DOI: 10.1109/icip49359.2023.10222146[^ic]
- Juan Luis Gonzalez, Munchurl Kim, "Optical-Flow-Aided Self-Supervised Single View Depth Estimation from Monocular Videos", IEEE Visual Communications and Image Processing (VCIP), Dec. 4-7, Jeju, Korea. DOI: 10.1109/vcip59821.2023.10402650[^ic]
- Jeonghyeok Do, Munchurl Kim, "MorphVAD: Efficient Video Anomaly Detection Using Morphological Transformation", IEEE Visual Communications and Image Processing (VCIP), Dec. 4-7, Jeju, Korea. DOI: 10.1109/vcip59821.2023.10402652[^ic]
- Juan Luis Gonzalez Bello, 김문철, “Boosting Self-Supervised Depth Estimation with Optical Flow Pseudo-Labels,” 한국방송·미디어공학회 하계학술대회, 메종글래드 제주 호텔, 2023.06.28-30.[^dc]
- 박종민, 김문철, “트랜스포머 기반 해상도 스케일러블 이미지 압축 프레임워크,” 한국방송·미디어공학회 하계학술대회, 메종글래드 제주 호텔, 2023.06.28-30.[^dc]
- 서원용, 김문철, “셔플 트랜스포머를 이용한 저복잡도 광학 흐름 예측 연구,” 한국방송·미디어공학회 하계학술대회, 메종글래드 제주 호텔, 2023.06.28-30.[^dc]
- 육근혁, 김문철, “시공간 열화 커널 예측에 기반한 효율적인 비디오 초해상화 및 흐림 제거 연구,” 한국방송·미디어공학회 하계학술대회, 메종글래드 제주 호텔, 2023.06.28-30.[^dc]
- Samuel Teodoro, 김문철, “A Lightweight RAFT for Optical Flow Estimation,” 한국방송·미디어공학회 하계학술대회, 메종글래드 제주 호텔, 2023.06.28-30.[^dc]
- 도정혁, 김문철, “Priors on Bone Length Consistency for Skeleton-based Action Recognition,” 한국방송·미디어공학회 하계학술대회, 메종글래드 제주 호텔, 2023.06.28-30.[^dc]
- 이재협, 김문철, “SET-Net: SAR-to-EO image Translation Network,” 한국방송·미디어공학회 하계학술대회, 메종글래드 제주 호텔, 2023.06.28-30.[^dc]
- 김다연, 김문철, “영상 내 중요 물체 검출 및 유표도 점수맵 예측을 위한 U-Net 기반 채널공간 어텐션 네트워크 설계,” 한국방송·미디어공학회 하계학술대회, 메종글래드 제주 호텔, 2023.06.28-30.[^dc]
- 서수민, 김문철, “Video deinterlacing network based on residual dense block and coordinate attention,” 한국방송·미디어공학회 하계학술대회, 메종글래드 제주 호텔, 2023.06.28-30.[^dc]

**2022**

- Juan Luis Gonzalez Bello and Munchurl Kim, "Self-Supervised Deep Monocular Depth Estimation with Ambiguity Boosting," IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 44, no. 12, pp. 9131-9149, Dec. 2022. (DOI: 10.1109/TPAMI.2021.3124079)[^ij]
- Jooyoung Lee, Seyoon Jeong, Munchurl Kim, "Selective compression learning of latent representations for variable-rate image compression," Thirty-Sixth Conference on Neural Information Processing Systems (NeurIPS), New Orleans, Louisiana, USA, Nov. 28 ~ Dec. 9 2022 .[^ic]
- Jihyong Oh and Munchurl Kim, "DeMFI: Deep Joint Deblurring and Multi-Frame Interpolation with Flow-Guided Attentive Correlation and Recursive Boosting," European Conference on Computer Vision (ECCV), Tel Aviv Israil, Oct. 23-27, 2022 . DOI: 10.1007/978-3-031-20071-7_12[^ic]
- Soo Ye Kim, Jianming Zhang, Simon Niklaus, Yifei Fan, Simon Chen, Zhe Lin, and Munchurl Kim, "Layered Depth Refinement with Mask Guidance," IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pp. 3855-3865, New Orleans, USA, 2022 . DOI: 10.1109/cvpr52688.2022.00383[^ic]
- Soo Ye Kim, Kfir Aberman, Nori Kanazawa, Rahul Garg, Neal Wadhwa, Huiwen Chang, Nikhil Karnad, Munchurl Kim, Orly Liba, "Zoom-to-Inpaint: Image Inpainting with High Frequency Details," IEEE Conference on Computer Vision and Pattern Recognition Workshops (CVPRW), June 19-24, pp. 477-487, New Orleans, USA, 2022 . DOI: 10.1109/cvprw56347.2022.00063[^ic]
- 박종민, 육근혁, 김문철, "어텐션 적용 YOLOv4 기반 SAR 영상 표적 탐지 및 인식," 한국군사과학기술학회지(Journal of the KIMST), vol. 25, no. 5, pp. 443-461, 2022. (DOI: https://doi.org/10.9766/KIMST.2022.25.5.443)[^dj]

**2021**

- Seonghyeon Kang, Seong Dae Kim, and Munchurl Kim,"Structural-Information-based Robust Corner Point Extraction for Camera Calibration under Lens Distortions and Compression Artifacts," IEEE ACCESS, vol. 9, pp. 151037-151048, Nov. 2021. (DOI: 10.1109/ACCESS.2021.3126570)[^ij]
- Hyeonjun Sim\*, Jihyong Oh\* and Munchurl Kim, "XVFI: eXtreme Video Frame Interpolation," International Conference on Computer Vision (ICCV), Virtual Conference, pp. 14489-14498, Oct. 11-17, 2021 (\*: equal contribution) . DOI: 10.1109/iccv48922.2021.01422[^ic]

## 과제

연구실 과제 목록의 2021–2026년 구역 35행이다. 연도는 누리집의 연도 구역 표기이고 날짜는 게시되어 있지 않다. 과제 쪽은 연도별 연차만 적어 2021·2026년 구역도 연도 목록대로 실었다. 같은 과제의 연차별 항목은 각 연도 표기대로 적었다.[^projects]

- 2026 · Learning Neural Radiance Fields of Images and Videos from Single-View Cameras and Multiview Cameras (5th Year)
- 2026 · AI-based Computer Vision Study for Satellite Image Processing and Analysis (3rd Year)
- 2026 · Diffusion-based High-Resolution SAR-to-EO Image Translation (2nd Year)
- 2026 · Video Frame Interpolation and Video Motion Deblurring (2nd Year)
- 2025 · Learning Neural Radiance Fields of Images and Videos from Single-View Cameras and Multiview Cameras (4th Year)
- 2025 · Deep-learning-based Illegal Ship and Contaminant Detection in Ocean SAR Imagery (3rd year)
- 2025 · AI-based Computer Vision Study for Satellite Image Processing and Analysis (2nd Year)
- 2025 · Diffusion-based High-Resolution SAR-to-EO Image Translation (1st Year)
- 2025 · Video Frame Interpolation and Video Motion Deblurring (1st Year)
- 2024 · Intelligent High Realistic Visual Processing for Smart Broadcasting Media (8th Year)
- 2024 · Learning Neural Radiance Fields of Images and Videos from Single-View Cameras and Multiview Cameras (3rd Year)
- 2024 · Deep-learning-based Illegal Ship and Contaminant Detection in Ocean SAR Imagery (2nd year)
- 2024 · SAR-to-EO Image Translation
- 2024 · AI-based Computer Vision Study for Satellite Image Processing and Analysis (1st Year)
- 2023 · Intelligent High Realistic Visual Processing for Smart Broadcasting Media (7th Year)
- 2023 · Learning Neural Radiance Fields of Images and Videos from Single-View Cameras and Multiview Cameras (2nd Year)
- 2023 · Optical Flow (OF) Estimation with a Lightweight Transformer and OF-based Depth Estimation
- 2023 · Motion Trajectory aware Transformer for Video Restoration
- 2023 · Deep-learning-based Illegal Ship and Contaminant Detection in Ocean SAR Imagery (1st year)
- 2023 · Compressing NERF networks
- 2023 · Deep Learning based Image/Video Quality Restoration (3rd Year)
- 2022 · GAN-based Satellite Image Restoration (Deep SAR Image Colorization) - 2nd year
- 2022 · Deep Learning based Simulated SAR Image Restoration and Target Detection/Recognition (3rd Year)
- 2022 · Intelligent High Realistic Visual Processing for Smart Broadcasting Media (6th Year)
- 2022 · Deep Learning based Image/Video Quality Restoration (2nd Year)
- 2022 · Heritage Image Restoration (2nd Year)
- 2022 · Learning Neural Radiance Fields of Images and Videos from Single-View Cameras and Multiview Cameras (1st Year)
- 2021 · Abnormal Behavior Detection and Understanding for Group People (2nd Year)
- 2021 · GAN-based Satellite Image Restoration (Deep SAR Image Colorization)
- 2021 · Deep Video Depth Estimation
- 2021 · Deep Learning based Simulated SAR Image Restoration and Target Detection/Recognition (2nd Year)
- 2021 · Intelligent High Realistic Visual Processing for Smart Broadcasting Media (5th Year) (Object-Saliency-Oriented Super-Resolution, Extreme Video Frame Interpolation, Video/Image Colorization)
- 2021 · Deep Learning based Image/Video Quality Restoration (1st Year)
- 2021 · Heritage Image Restoration
- 2021 · Video Frame Prediction for Abnormality Detection with Semiconductor Applications

## 수상과 선정

국내 학회 논문 목록의 수상 6건과 누리집 글 목록 피드의 졸업생 수상 1건이다. 학회 수상의 날짜 범위는 해당 학회 개최 기간이다.[^dc][^feed]

- 2026-06-18–2026-06-20 · EcoSplat: Efficiency Controllable Feed-Forward 3D Gaussian Splatting from Multi View Images · 최우수 논문상[^dc]
- 2026-06-18–2026-06-20 · Score Distillation Sampling for Image Colorization · 우수 포스터 논문상[^dc]
- 2024-06-25–2024-06-28 · TUT: Two-stage U-Net-based Transformer for Image Restoration with Mixed Degradation · 논문 대상[^dc]
- 2024-06-25–2024-06-28 · Multi-modal Depth Estimation from Misaligned Thermal and RGB Images · 우수 논문상[^dc]
- 2023-06-28–2023-06-30 · Boosting Self-Supervised Depth Estimation with Optical Flow Pseudo-Labels · 논문 대상[^dc]
- 2023-06-28–2023-06-30 · 트랜스포머 기반 해상도 스케일러블 이미지 압축 프레임워크 · 우수 논문상[^dc]
- 2026-09-20 · 김수예 박사 · Adobe Tech Excellence Award 수상[^feed]

## 소식

누리집 글 목록 피드에 게시된 2025년 9월–2026년 9월의 논문 게재 승인·학회 채택·연구성과 소개 14건이다. 날짜는 게시 시각의 한국 날짜다.[^feed]

- 2026-09-27 · 연구실 논문 4편이 NeurIPS 2026에 채택되었다.[^neurips]
- 2026-08-26 · Donghyun Kim이 참여한 「Intra Prediction-Based OBMC Extension for Inter-Intra Boundaries」가 IEEE Transactions on Circuits and Systems for Video Technology에 게재 승인되었다.[^feed]
- 2026-08-07 · Samuel Teodoro가 참여한 「PRIMEdit」가 IEEE Transactions on Pattern Analysis and Machine Intelligence에 게재 승인되었다.[^feed]
- 2026-06-18 · 연구실 논문 5편이 ECCV 2026에 채택되었다.[^feed]
- 2026-06-02 · 「C-DiffSET」 등 논문 2편이 IEEE Transactions on Circuits and Systems for Video Technology에 게재 승인되었다.[^feed]
- 2026-02-24 · 「EcoSplat」 등 연구실 논문 2편이 CVPR 2026에 채택되었다.[^feed]
- 2026-01-27 · 이미지 속 글자 조작을 다룬 「OmniText」 논문이 ICLR 2026에 채택되었다.[^feed]
- 2026-01-15 · 「FS-SegDiff」 논문이 IEEE ACCESS에 게재 승인되었다.[^feed]
- 2025-11-08 · 「MoBGS」 논문이 AAAI 2026에 채택되었다.[^feed]
- 2025-10-26 · 「DeepHQ」 등 논문 3편이 학술지 게재 승인되었다.[^feed]
- 2025-09-06 · 골격 정보와 글자 설명을 연결하는 행동 인식 논문을 ICCV 2025 연구성과로 소개했다.[^feed]
- 2025-09-06 · 고해상도 영상의 단일 카메라 깊이 추정 논문 「One Look is Enough」를 ICCV 2025 연구성과로 소개했다.[^feed]
- 2025-09-06 · 위성 영상 융합 논문 「PAN-Crafter」를 ICCV 2025 연구성과로 소개했다.[^feed]
- 2025-09-01 · 위성 영상 융합 논문 「U-Know-DiffPAN」을 CVPR 2025 연구성과로 소개했다.[^feed]

## 연락과 위치

- 교수 이메일: mkimee@kaist.ac.kr[^prof]
- 교수 전화: +82-42-350-7419, 팩스 +82-42-350-7619[^prof]
- 교수실: KAIST LG이노베이션홀(N24) 1107호[^dept]
- 연구실 사무실(Office): KAIST LG이노베이션홀(N24) 1106호[^contact]
- 연구실 전화: 042-350-7198, 팩스 042-350-7619[^contact]
- 연구실 주소: 335 Gwahak-ro, Yusong-Gu, Daejeon, 305-701, Korea[^contact]

## 각주
[^home]: VIC Lab 첫 화면, 연구 소개·소식. <https://www.viclab.kaist.ac.kr/> 관측일 2026-11-09.
[^prof]: Professor. <https://www.viclab.kaist.ac.kr/professor> 관측일 2026-11-09.
[^students]: Students. <https://www.viclab.kaist.ac.kr/students> 관측일 2026-11-09.
[^faculties]: Faculties. <https://www.viclab.kaist.ac.kr/faculties> 관측일 2026-11-09.
[^alumni]: Alumni. <https://www.viclab.kaist.ac.kr/alumni> 관측일 2026-11-09.
[^projects]: Projects. <https://www.viclab.kaist.ac.kr/projects> 관측일 2026-11-09.
[^ij]: International Journals. <https://www.viclab.kaist.ac.kr/international-journals> 관측일 2026-11-09.
[^ic]: International Conferences. <https://www.viclab.kaist.ac.kr/international-conferences> 관측일 2026-11-09.
[^dj]: Domestic Journals. <https://www.viclab.kaist.ac.kr/domestic-journals> 관측일 2026-11-09.
[^dc]: Domestic Conferences. <https://www.viclab.kaist.ac.kr/domestic-conferences> 관측일 2026-11-09.
[^contact]: Contact, 연구실 사무실·교수실·주소·전화. <https://www.viclab.kaist.ac.kr/contact> 관측일 2026-11-09.
[^neurips]: NeurIPS 2026 논문 4편 채택 소식. <https://www.viclab.kaist.ac.kr/single-post/neurips-2026-4-papers-accepted> 관측일 2026-11-09.
[^feed]: 누리집 글 목록 피드의 최근 20건, 제목·게시일·본문 요약. <https://www.viclab.kaist.ac.kr/blog-feed.xml> 관측일 2026-11-09.
[^dept]: KAIST 전기및전자공학부 김문철 교수 소개. <https://ee.kaist.ac.kr/professor/12142/> 관측일 2026-11-09.
[^vision]: VIC Lab 연구 소개, Computer Vision 연구와 화질 복원. <https://www.viclab.kaist.ac.kr/> 관측일 2026-11-09.
[^reconstruction]: VIC Lab 연구 소개, 3D/4D 장면 복원과 카메라 위치·방향 추정. <https://www.viclab.kaist.ac.kr/> 관측일 2026-11-09.
[^graphics]: VIC Lab 연구 소개, 신경 방사장·가우시안 스플래팅을 통한 새 시점 영상 합성. <https://www.viclab.kaist.ac.kr/> 관측일 2026-11-09.
[^generation]: VIC Lab 연구 소개, Image/Video Generation and Editing AIs. <https://www.viclab.kaist.ac.kr/> 관측일 2026-11-09.
[^remote]: VIC Lab 연구 소개, 드론·위성 영상 처리와 분석. <https://www.viclab.kaist.ac.kr/> 관측일 2026-11-09.
[^p1]: S. Teodoro 외, M. Kim, IEEE Transactions on Pattern Analysis and Machine Intelligence (2026). <https://doi.org/10.1109/tpami.2026.3722239> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5027012300,publication_year:2021-2026> 관측일 2026-11-09.
[^p2]: J. Park 외, M. Kim, IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (2025). <https://doi.org/10.1109/cvpr52734.2025.02502> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5027012300,publication_year:2021-2026> 관측일 2026-11-09.
[^p3]: B. Kwon, M. Kim, IEEE/CVF International Conference on Computer Vision (ICCV) (2025). <https://doi.org/10.1109/iccv51701.2025.00757> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5027012300,publication_year:2021-2026> 관측일 2026-11-09.
[^p4]: W. Seo, J. Oh, M. Kim, IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (2025). <https://doi.org/10.1109/cvpr52734.2025.00679> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5027012300,publication_year:2021-2026> 관측일 2026-11-09.
[^p5]: J. Do 외, M. Kim, IEEE/CVF International Conference on Computer Vision (ICCV) (2025). <https://doi.org/10.1109/iccv51701.2025.00404> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5027012300,publication_year:2021-2026> 관측일 2026-11-09.
[^p6]: J. Do, J. Lee, S. Lee, M. Kim, IEEE Transactions on Circuits and Systems for Video Technology (2026). <https://doi.org/10.1109/tcsvt.2026.3701447> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5027012300,publication_year:2021-2026> 관측일 2026-11-09.
[^p7]: J.-M. Park, J. Lee, M. Kim, IEEE/CVF International Conference on Computer Vision (ICCV) (2023). <https://doi.org/10.1109/iccv51070.2023.01178> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5027012300,publication_year:2021-2026> 관측일 2026-11-09.
[^p8]: W. Lee 외, M. Kim, IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (2025). <https://doi.org/10.1109/cvpr52734.2025.00827> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5027012300,publication_year:2021-2026> 관측일 2026-11-09.

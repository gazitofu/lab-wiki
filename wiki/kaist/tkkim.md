# 컴퓨터 비전 및 머신 러닝 랩 (KAIST Computer Vision and Learning Lab, KCVL)

**KAIST 전산학부 · 김태균 교수**

- 분야: 3차원 컴퓨터 비전, 기계(심층) 학습, 손과 몸의 3차원 복원, 6D 물체 자세 추정, 확산 모형 기반 생성 인공지능, 물리를 반영한 인공지능, 로봇 비전
- 홈페이지: <https://sites.google.com/view/tkkim>
- 근거와 출처: [KCVL 근거 페이지](tkkim-sources.md)

> 사진이나 깊이 영상에서 사람의 손과 몸, 물체의 3차원 모양과 자세를 알아내고, 확산 모형 같은 생성 인공지능으로 손 동작이나 고해상도 이미지를 새로 만들어 내는 컴퓨터 비전·기계학습 연구실이다.[^home][^p1][^p2][^p4][^p5]

## 무엇을 연구하나

김태균 교수의 연구 관심사는 3차원 컴퓨터 비전을 위한 기계(심층) 학습, 생성 인공지능, 물리를 반영한 인공지능, 사람-기계 인터페이스, 로봇이다. 누리집은 구체적으로 관절이 있는 3차원 손·몸 복원, 얼굴 분석과 인식, 6D 물체 자세 추정, 행동 인식, 물체 검출·추적, 능동 로봇 비전을 들고, 이것이 새로운 능동적·상호작용형 시각 감지로 이어진다고 적었다.[^home] 박사후연구원 모집 공고는 연구 분야로 물리 인공지능, 생성 인공지능, 세계 모형(영상·3차원 생성, 확산·흐름 모형, 체화 인공지능, 과학을 위한 인공지능)을 든다.[^home]

첫째 갈래는 **두 손과 손-물체 상호작용의 3차원 복원**이다. 대표 논문에서는 서로 맞닿은 두 손의 세밀한 3차원 모양을 신경망 암시 표현(공간의 각 점이 물체 안인지 밖인지를 신경망으로 나타내는 방법)으로 복원했고,[^p1] 두 손이 맞닿거나 물체를 함께 잡은 모양을 확산 모형(잡음에서 시작해 점점 그럴듯한 데이터를 만들어 내는 생성 모형)으로 생성했으며,[^p2] 사진 한 장에서 두 손의 피부 질감까지 복원했다.[^p3]

둘째 갈래는 **물체 자세 추정과 이미지 생성**이다. 깊이 영상으로 물체의 3차원 위치와 방향(6D 자세)을 확산 모형으로 추정하는 방법을 더 빠르고 정확하게 만들었고,[^p4] 임의의 배율로 이미지를 키우거나 새로 만드는 잠재 확산 모형을 제안했다.[^p5]

셋째 갈래로, 현미경 영상 속 살아 있는 세포의 윤곽을 점 단위로 따라가는 비지도 학습 추적기도 만들었다.[^p6]

## 주요 연구 주제

### 1. 두 손과 손-물체 상호작용의 3차원 복원

두 손 신경망 암시 표현, 두 손 상호작용 생성 확산 모형, 두 손 질감 복원.[^p1][^p2][^p3] 대표 논문 1–3.

### 2. 6D 물체 자세 추정과 확산 모형 이미지 생성

자세 회귀와 확산을 함께 학습하는 6D 자세 추정, 임의 배율 이미지 생성.[^p4][^p5] 대표 논문 4, 5.

### 3. 생물 영상 분석

살아 있는 세포의 윤곽 추적.[^p6] 대표 논문 6.

## 대표 논문

랩 논문 목록의 2021–2026년 논문 가운데 김태균 교수가 마지막 저자인 KAIST 시기 학회 논문에서 연구 갈래를 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2023 | [Im2Hands: Learning Attentive Implicit Representation of Interacting Two-Hand Shapes](https://doi.org/10.1109/cvpr52729.2023.02028) · CVPR 2023 | 서로 맞닿은 두 손을 처음으로 신경망 암시 표현으로 나타낸 방법이다. 손 매개변수 모형이나 저해상도 메시에 기대던 기존 방법과 달리, RGB 사진과 대략의 3차원 관절점을 입력으로 두 손이 차지하는 공간을 두 단계 주의(attention) 모듈로 추정하고 다듬어, 두 손끼리와 사진과 잘 맞는 세밀한 모양을 만든다. 예측한 관절점만으로도 사진 한 장에서 두 손 모양을 안정적으로 얻는 관절점 보정 모듈도 더했고, 두 손 복원에서 비교 방법보다 좋은 결과를 냈다.[^p1] | 1저자 Jihyun Lee, 마지막 저자 김태균 |
| 2 | 2024 | [InterHandGen: Two-Hand Interaction Generation via Cascaded Reverse Diffusion](https://doi.org/10.1109/cvpr52733.2024.00057) · CVPR 2024 | 두 손이 가까이 맞닿은(물체가 있든 없든) 그럴듯하고 다양한 모양을 만들어 내는 생성 사전 지식을 학습하는 틀이다. 여러 개체의 결합 분포를 직접 배우면 경우의 수 때문에 어렵다는 점에 착안해, 한 손의 분포와 다른 손이 주어졌을 때의 분포로 나눠 확산 모형으로 배우고, 손끼리 파고들지 않게 하는 안내를 더해 생성한다. 두 손 합성 평가 기준을 세웠고, 이 사전 지식으로 실제 사진 한 장에서 두 손을 복원하는 정확도도 높였다.[^p2] | 1저자 Jihyun Lee, 마지막 저자 김태균 |
| 3 | 2024 | [BiTT: Bi-directional Texture Reconstruction of Interacting Two Hands from a Single Image](https://doi.org/10.1109/cvpr52733.2024.01020) · CVPR 2024 | AR/VR에서 개인 맞춤 손 아바타를 만들려면 손의 모양뿐 아니라 피부 질감도 필요하지만, 기존 방법은 보이는 쪽 화소만 잡아 여러 장의 사진이 필요했다. 사진 한 장으로 맞닿은 두 손의 질감을 조명을 바꿔도 쓸 수 있게 복원하는 첫 종단간 학습 방법으로, 왼손·오른손 질감의 대칭을 이용한 양방향 복원, 질감 매개변수 모형, 단계적 정밀화를 쓴다. InterHand2.6M과 RGB2Hands 자료에서 기존 손 질감 복원 방법보다 크게 나았다.[^p3] | Minje Kim(1저자)·김태균(마지막 저자) |
| 4 | 2025 | [Joint Learning of Pose Regression and Denoising Diffusion with Score Scaling Sampling for Category-level 6D Pose Estimation](https://doi.org/10.1109/iccv51701.2025.00545) · ICCV 2025 | 깊이 영상으로 물체의 6D 자세(3차원 위치와 방향)를 확산 모형으로 추정하는 기존 방법은 학습이 느리고, 뽑은 자세 후보를 거르는 별도 신경망이 필요했다. 인코더를 직접 자세 회귀로 먼저 학습한 뒤 회귀와 확산을 함께 학습해 학습을 크게 빠르게 하면서 정확도를 높였고, 시간에 따라 점수 크기를 조절하는 표본 추출 안내로 별도 평가 신경망을 없앴다. REAL275·HouseCat6D·ROPE에서 자세 하나만 추론해도 최고 수준의 정확도를 냈고 학습과 추론이 더 효율적이었다.[^p4] | Seunghyun Lee(1저자)·김태균(마지막 저자) |
| 5 | 2024 | [Arbitrary-Scale Image Generation and Upsampling using Latent Diffusion Model and Implicit Neural Decoder](https://doi.org/10.1109/cvpr52733.2024.00879) · CVPR 2024 | 대부분의 초해상도(저해상도 이미지를 고해상도로 키우는 일)·이미지 생성 방법은 정해진 배율로만 만들고 결과가 뭉개지거나 잡티가 생긴다. 미리 학습한 오토인코더, 잠재 공간의 확산 모형, 임의 배율로 출력하는 암시 신경 복호기로 된 방법을 제안해, 입력 이미지를 원하는 배율로 키우거나 무작위 잡음에서 새 이미지를 원하는 배율로 만든다. 확산을 잠재 공간에서 해 효율적이고, 잡음 제거와 정렬 손실을 함께 학습해 출력 품질을 높였다.[^p5] | Jinseok Kim(1저자)·김태균(마지막 저자) |
| 6 | 2023 | [Unsupervised Contour Tracking of Live Cells by Mechanical and Cycle Consistency Losses](https://doi.org/10.1109/cvpr52729.2023.00030) · CVPR 2023 | 줄기세포나 전이 암세포 같은 살아 있는 세포의 기능을 알려면 영상 매 장면에서 잘 변형되는 세포 윤곽의 모든 점을 따라가야 한다. 두 윤곽 사이의 조밀한 표현을 교차 주의로 합쳐 점 대응까지 찾는, 딥러닝 기반 세포 윤곽 추적을 처음 제안했다. 점을 손으로 표시하기 어려워, 점이 윤곽에 수직으로 움직이게 하는 역학 손실과 순환 일관성 손실로 정답 표시 없이 학습(비지도 학습)했고, 위상차·공초점 형광 현미경 자료에서 비교 방법보다 나았다.[^p6] | 1저자 Junbong Jang, 마지막 저자 김태균 |

## 교수와 전문 분야

김태균 교수는 KAIST에서 학사(1998)와 석사(2000)를 받고 삼성종합기술원(Samsung AIT)에서 일했으며(2000–2004), 영국 케임브리지대에서 박사학위(2008)를 받고 시드니서식스칼리지 Junior Research Fellow(2007–2010)를 지냈다. 영국 임페리얼칼리지런던에서 Lecturer·Senior Lecturer로 Computer Vision and Learning Lab을 이끌었고(2010–2020), Reader(2020–2024)를 지냈으며, 2020년부터 KAIST 전산학부 교수다.[^home] 120편이 넘는 논문을 함께 썼고, CVPR·ICCV·ECCV와 함께 열린 HANDS 워크숍과 6D Object Pose 워크숍을 공동 창립했으며(2015–2020), BMVC 2017 대회장과 BMVC 2023 프로그램 공동 위원장을 맡았다. IEEE Trans. on PAMI, Pattern Recognition, Image and Vision Computing의 부편집장(Associate Editor)이다.[^home] 누리집에 적힌 수상으로는 ICRA 2014 KUKA best service robotics paper award, ASCE Journal of Computing 2016 best paper award, CVPR 2020 best paper finalist가 있고, 함께 만든 얼굴 영상 표현 알고리즘이 MPEG-7 ISO/IEC 국제 표준이 됐다.[^home]

소속은 전산학부, 김재철AI대학원, Department of AI Computing, Robotics Graduate Program, Metaverse Graduate Program이고, 누리집은 Head, Director of KAIST AGI Research Institute, Head of InnoCORE AI Meta-Scientist Research Center, Samsung AI Center(영국 케임브리지)와 GBSoft의 Advisory Consultant를 함께 적는다.[^home] Grants 페이지는 IITP, InnoCORE, 한국콘텐츠진흥원(KOCCA), LG전자, ETRI, KISTI, 삼성디스플레이, 현대자동차, Huawei, 삼성리서치, Microsoft Azure Research Award, EPSRC, 유럽연합 FP7 등 여러 후원 기관을 든다.[^grants]

논문으로 보면 전문 분야는 세 갈래다.

- **두 손의 3차원 모양·질감 복원과 생성**.[^p1][^p2][^p3]
- **확산 모형을 이용한 6D 자세 추정과 이미지 생성**.[^p4][^p5]
- **변형되는 대상(살아 있는 세포)의 추적**.[^p6]

## 응용 분야

누리집은 연구가 새로운 능동적·상호작용형 시각 감지로 이어진다고 적었다.[^home] 대표 논문으로 보면 AR/VR용 개인 맞춤 손 아바타,[^p3] 사진 속 두 손 복원,[^p1][^p2] 로봇이 다룰 물체의 자세 추정,[^p4] 고해상도 이미지 생성,[^p5] 세포 생물학 영상 분석에 닿아 있다.[^p6] 졸업생과 이전 구성원은 영국 셰필드대·애버딘대·버밍엄대·퀸메리런던대, UNIST, 홍콩과기대 교수와 Meta Reality Labs, Qualcomm, Google, Niantic, Huawei 등으로 진출했다.[^students]

## 구성원

2026년 10월 20일 랩 Students 페이지 기준이다. 과정은 랩 칸 이름(PhD students, MSc students, Interns)이고, 괄호 속 소속은 이름 뒤 "@"에 적힌 학과 표기다.[^students] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Hangil Park | 박사과정 (SoC, KAIST) |  |
| Taeyun Woo | 박사과정 (SoC, KAIST) |  |
| HyunKyu Jung | 박사과정 (SoC, KAIST) |  |
| Donghwan Kim | 박사과정 (SoC, KAIST) |  |
| Minje Kim | 박사과정 (SoC, KAIST) | 3 |
| Seungheon Kim | 박사과정 (Metaverse Grad School, KAIST) |  |
| Changmin Lee | 박사과정 (SoC, KAIST) |  |
| Sanghyeok Nam | 박사과정 (SoC, KAIST) |  |
| Beomjun Goo | 박사과정 (SoC, KAIST) |  |
| Kunhee Kim | 박사과정 (Grad School of AI, KAIST) |  |
| Wonjune Kim | 박사과정 (Dept. of AI Computing, KAIST) |  |
| Byoungjun Kim | 박사과정 (SoC, KAIST) |  |
| Yunho Kim | 석사과정 (SoC, KAIST) |  |
| Hwidong Kim | 석사과정 (SoC, KAIST) |  |
| Sungyup Kim | 석사과정 (KT-AI Program, KAIST) |  |
| Seoyoung Hwang | 석사과정 (SoC, KAIST) |  |
| Gunyoung Kang | 석사과정 (SoC, KAIST) |  |
| Minsoo Lee | 석사과정 (Metaverse Grad School, KAIST) |  |
| Myungjo Kwak | 석사과정 (Metaverse Grad School, KAIST) |  |
| Jungyu Park | 석사과정 (SoC, KAIST) |  |
| Jaesoon Kim | 석사과정 (Dept. of AI Computing, KAIST) |  |
| Soyun Lee | 석사과정 (Metaverse Grad School, KAIST) |  |
| Jaehyeong Kim | 인턴 (SoC, KAIST) |  |

## 졸업생과 이전 구성원

랩 Students 페이지 Alumni 칸(In Academia, In Industry)의 이름, 기간·과정, 랩이 적은 현재 자리다. 김태균 교수가 영국 임페리얼칼리지런던에서 이끈 시절의 구성원도 함께 적혀 있다.[^students]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Dr. Zhixiang Chen | 2019-2022 postdoc | Assistant professor(lecturer), Univ. of Sheffield, UK |
| Dr. Binod Bhattarai | 2017-2021 postdoc | Assistant professor (lecturer), Aberdeen Univ., UK |
| Dr. Hyung Jin Chang | 2013-2014, postdoc | Associate professor, Univ. of Birmingham, UK |
| Dr. SeungRyul Baek | 2015-2019, PhD | Associate professor, UNIST, Korea |
| Dr. Caner Sahin | 2014-2018, PhD | Lecturer, Istanbul Medeniyet University, Turkey |
| Dr. Shanxin Yuan | 2014-2018, PhD | Assistant professor, Queen Mary Univ. of London, UK |
| Dr. Qi Ye | 2014-2018, PhD | Assistant professor, Zhejiang Univ., China |
| Dr. Wenhan Luo | 2012-2016, PhD | Associate professor, HKUST, Hong Kong |
| Dr. Lin Wang | 2019-2021, visiting phd student | Assistant professor, NTU, Singapore |
| Dr. Hamidreza Kasaei | 2017, visiting phd student | Assistant professor, Univ. of Groningen, Netherlands |
| Dr. Yuru Pei | 2012, visiting scholar | Associate professor, Peking University, China |
| Dr. Oscar Suarez | 2014, visiting scholar | Full professor, Univ. of Castilla-La Mancha, Spain |
| Dr. Giovanni Farinella | 2013, visiting scholar | Associate professor, University of Catania, Italy |
| Dr. Jihyun Lee | 2020-2025, phd | Meta Reality Labs, Pittsburgh, USA |
| Dr. Xuepeng Shi | 2020-2024, phd | Qualcomm Research, Austria |
| Dr. Guillermo Garcia | 2013-2017, phd and 2017-2021, postdoc | Niantic, London, UK |
| Dr. Anil Armagan | 2018-2021, postdoc | Huawei, London, UK |
| Dr. Rigas Kouskouridas | 2013-2016, postdoc | Scape, London, UK |
| Dr. Zhiyuan Patrick Shi | 2015-2017, postdoc | Onfido, London, UK |
| Dr. Xiaowei Zhao | 2013-2015, postdoc | Alibaba, China |
| Dr. Andreas Doumanoglou | 2012-2016, phd | Google, Zurich, Switzerland |
| Dr. Danhang Tang | 2011-2015, phd | Google, USA |
| Dr. Yang Liu | 2011-2016, phd | AIG, London, UK |
| Alykhan Tejani | 2012-2014, MPhil | Twitter, London, UK |
| Dr. Changkyu Choi | 2013-2014, visiting scholar | Senior vice-president, Samsung AIT, Korea |

## 최근 논문 목록 (2021–2027)

랩 Publications 페이지의 2021년 이후 논문이다. 연도는 페이지의 연도 구역이고, 2027년 구역에는 게재가 정해진 학회 논문이 있다. 저자 이름 뒤 *는 공동 1저자를 뜻하는 랩 표기다.[^papers]

**2027**

- S. Hwang and T-K. Kim, ETA-Motion: Efficient Topology-Agnostic Motion Diffusion via Sparse Joint Learning, Winter Conference on Applications of Computer Vision (WACV), Disney Springs, Buena Vista, FL, 2027

**2026**

- M. Kim, Y. Noh, J. Kim, T-K. Kim, DySurface: Consistent 4D Surface Reconstruction via Bridging Explicit Gaussians and Implicit Functions, Proc. of The Fortieth Annual Conference on Neural Information Processing Systems (NeurIPS), Sydney, 2026
- Y. Noh, M. Kim, T-K. Kim, Sparse-GS2Mesh: 3D Gaussian Splatting Guided by Novel Stereo Views and 2DGS for Sparse View Surface Reconstruction, Proc. of NeurIPS'26 workshop on Physical World AI: Geometry, Characteristics, and Multimodal Sensing, Sydney, 2026
- H. Kim, M. Kim, T-K. Kim, CoIn: Comprehensive 2D-3D Inpainting with Gaussian Splatting Guidance, Proc. of European Conference on Computer Vision (ECCV), Malmö, Sweden, 2026
- T. Woo, J. Park, T-K. Kim, Cascaded Diffusion Framework for Probabilistic Coarse-to-Fine Hand Pose Estimation, Proc. of ECCV'26 workshop on Observing and Acting as Dexterous Hands, Malmö, Sweden, 2026
- J. Lee\*, C. Lee\*, D. Kim, T-K. Kim, PhysHanDI: Physics-Based Reconstruction of Hand-Deformable Object Interactions, Proc. of Forty-third International Conference on Machine Learning (ICML), Seoul, Jul 2026 (\*: co-first authors)
- D. Kim, T-K. Kim, Learning Instance-Adaptive Low-Rank Orthogonal Subspaces for Clothes-Changing Person Re-Identification, Proc. of ICML'26 workshop on CoLoRAI - the 2nd workshop on connecting low-rank representations in AI, Seoul, Jul 2026
- S. Nam\*, B. Kim\*, D. Park, T-K. Kim, Dynamic Full-body Motion Agent with Object Interaction via Blending Pre-trained Modular Controllers, Proc. of IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR Findings Track), Denver, Colorado, Jun 2026 (\*: co-first authors)
- L. F. Vecchietti, M. Lee, B. Hangeldiyev, B. N. Wijaya, H. Jung, H. Park, T-K. Kim, M. Cha, H. Kim, Interpretable Machine Learning for Protein Science: Structure, Function, and Interactions, ACM Computing Surveys, Mar 2026
- T. Kong and T-K. Kim, Learning Adaptive Pseudo-Label Selection for Semi-Supervised 3D Object Detection, IEEE Int. Conf. on Robotics and Automation (ICRA), Vienna, Austria, 2026

**2025**

- C. Lee, J. Lee, T-K. Kim, MPMAvatar: Learning 3D Gaussian Avatars with Accurate and Robust Physics-Based Dynamics, Proc. of Thirty-Ninth Annual Conf. on Neural Information Processing Systems (NeurIPS), San Diego, US, 2025
- M. Kim, T-K. Kim, SRHand: Super-Resolving Hand Images and 3D Shapes via View/Pose-aware Neural Image Representations and Explicit Meshes, Proc. of Thirty-Ninth Annual Conf. on Neural Information Processing Systems (NeurIPS), San Diego, US, 2025
- S. Lee, T-K. Kim, Joint Learning of Pose Regression and Denoising Diffusion with Score Scaling Sampling for Category-level 6D Pose Estimation, Proc. of IEEE Int. Conf. on Computer Vision (ICCV), Honolulu, Hawai'i, 2025
- S. Cho, T-K. Kim, Body-Hand Modality Expertized Networks with Cross-attention for Fine-grained Skeleton Action Recognition, Proc. of IEEE/RSJ Int. Conf. on Intelligent Robots and Systems (IROS), Hangzhou, China, 2025
- J. Lee, W. Xu, A. Richard, S. Wei, S. Saito, S. Bai, T. Wang, M. Sung, T-K. Kim, J. Saragih, Egocentric Whole-Body Motion Diffusion with Exemplar-Based Identity Conditioning, Proc. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Nashville TN, USA, 2025
- R. Li, S. Katsigiannis, T-K. Kim, H. Shum, BP-SGCN: Behavioral Pseudo-Label Informed Sparse Graph Convolution Network for Pedestrian and Heterogeneous Trajectory Prediction, To appear in IEEE Trans. on Neural Networks and Learning Systems, 2025.
- T, Wang, K. Zhang, Y. Zhang, W. Luo, B. Stenger, T. Lu, T-K. Kim, W. Liu, LLDiffusion: Learning Degradation Representations in Diffusion Models for Low-Light Image Enhancement, Pattern Recognition, to appear, 2025

**2024**

- D. Kim, T-K. Kim, Multi-hypotheses Conditioned Point Cloud Diffusion for 3D Human Reconstruction from Occluded Images, Proc. of Thirty-Eighth Annual Conf. on Neural Information Processing Systems (NeurIPS), Vancouver, Canada, 2024.
- W. Cho, J. Lee, M. Yi, M. Kim, T. Woo, D. Kim, T. Ha, H. Lee, J-H. Ryu, W. Woo, T-K. Kim, Dense Hand-Object(HO) GraspNet with Full Grasping Taxonomy and Dynamics, Proc. of European Conference on Computer Vision (ECCV), Milan, Italy, 2024.
- W. Cho, T. Ha, I. Jeon, J. Jeon, T-K. Kim, W. Woo, Temporally enhanced graph convolutional network for hand tracking from an egocentric camera. Virtual Real. 28(3): 143, 2024
- T. Woo, T-K. Kim, J. Park, Hand-Object Reconstruction via Interaction-aware Graph Attention Mechanism, Proc. of IEEE Int. Conference on Image Processing (ICIP), Abu Dhabi, UAE, 2024
- M. Kang, T. Kong, T-K. Kim, Semi-Supervised 3D Object Detection with Chanel Augmentation using Transformation Equivariance, Proc. of IEEE Int. Conference on Image Processing (ICIP), Abu Dhabi, UAE, 2024
- J. Zhu, Z. Hu, T-K. Kim, L. Wang, Energy-based Domain-Adaptive Segmentation with Depth Guidance, IEEE Robotics and Automation Letters (RA-L), 9(8):7126-7133, Aug 2024.
- J. Lee, S. Saito, G. Nam, M. Sung, T-K. Kim, InterHandGen: Two-Hand Interaction Generation via Cascaded Reverse Diffusion, Proc. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Seattle WA, USA, 2024
- R. Bodur, B. Bhattarai, T-K. Kim, Prompt Augmentation for Self-supervised Text-guided Image Manipulation, Proc. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Seattle WA, USA, 2024
- J. Kim, T-K. Kim, Arbitrary-Scale Image Generation and Upsampling using Latent Diffusion Model and Implicit Neural Decoder, Proc. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Seattle WA, USA, 2024
- M. Kim, T-K. Kim, BiTT: Bi-directional Texture Reconstruction of Interacting Two Hands from a Single Image, Proc. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Seattle WA, USA, 2024
- R. Bodur, E. Gundogdu, B. Bhattarai, T-K. Kim, M. Donoser, L. Bazzani, iEdit: Localised Text-guided Image Editing with Weak Supervision, Prof. of IEEE CVPR Workshop on Generative Models for Computer Vision, Seattle, WA, USA, 2024
- T. Wang, K. Zhang, Z. Shao, W. Luo, B. Stenger, T. Lu, T-K. Kim, W. Liu, H. Li , GridFormer: Residual Dense Transformer with Grid Structure for Image Restoration in Adverse Weather Conditions, International Journal of Computer Vision (IJCV), Vol.132, pages 4541–4563, 2024
- H. Ai, Z. Cao, H. Lu, C. Chen, J. Ma, P. Zhou, T-K. Kim, P. Hui, L. Wang, Dream360: Diverse and Immersive Outdoor Virtual Scene Creation via Transformer-Based 360 Image Outpainting, Proc. of IEEE Virtual Reality (VR), Orlando, Florida, USA, 2024 (full paper, also in IEEE Trans. on Visualization and Computer Graphics, 30(5): 2734-2744, 2024)

**2023**

- J. Lee, J. Jang, D. Kim, M. Sung, T-K. Kim, FourierHandFlow: Neural 4D Hand Representation Using Fourier Query Flow, Thirty-seventh Conference on Neural Information Processing Systems (NeurIPS), New Orleans, USA, 2023
- P. Castro, T-K. Kim, PoseMatcher: One-shot Model Free Pose Estimation by Deep Feature Matching, Proc. of 8th International Workshop on Recovering 6D Object Pose at ICCV, Paris, France, 2023
- J. Sun, Z. Chen, T-K. Kim, MAPConNet: Self-supervised 3D Pose Transfer with Mesh and Point Contrastive Learning, Proc. of IEEE Int. Conf. on Computer Vision (ICCV), Paris, France, 2023
- X. Shi, G. Dikov, G. Reitmayr, T-K. Kim, M. Ghafoorian, 3D Distillation: Improving Self-Supervised Monocular Depth Estimation on Reflective Surfaces, Proc. of IEEE Int. Conf. on Computer Vision (ICCV), Paris, France, 2023
- H. Park\*, J. Lee\*, Y. Seo, T. Min, J. Yun, J. Kim, T-K. Kim (\* equal contributions), Contrastive Knowledge Distillation for Anomaly Detection in Multi-Illumination/Focus Display Images, Proc. of IAPR Int. Conference on Machine Vision Applications (MVA), Hamamatsu, Japan, 2023 (oral)
- J. Lee, M. Sung, H. Choi, T-K. Kim, Im2Hands: Learning Attentive Implicit Representation of Interacting Two-Hand Shapes, Proc. of IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Vancouver, CANADA, 2023.
- J. Jang, K. Lee, T-K. Kim, Unsupervised Contour Tracking of Live Cells by Mechanical and Cycle Consistency Losses, Proc. of IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Vancouver, CANADA, 2023.
- R. Bodur, B. Bhattarai, T-K. Kim, Joint Training of Hierarchical GANs and Semantic Segmentation for Expression Translation, Proc. of International Conference on Acoustics, Speech, and Signal Processing (ICASSP), Rhodes Island, Greece, 2023

**2022**

- X. Shi, Z. Chen, T-K. Kim, Multivariate Probabilistic Monocular 3D Object Detection, Proc. of IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), Waikoloa, Hawaii, Jan 2023.
- P. Castro, T-K. Kim, CRT6D : Fast 6D Object Pose Estimation with Cascaded Refinement Transformers, Proc. of IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), Waikoloa, Hawaii, Jan 2023.
- H. Choi, Z. Chen, X. Shi, T-K. Kim, Semi-Supervised Object Detection with Object-wise Contrastive Learning and Regression Uncertainty, Proc. of The 33rd British Machine Vision Conference (BMVC), London, UK, 2022.
- R. Caramalau, B. Bhattarai, D. Stoyanov T-K. Kim, MoBYv2: Self-supervised Active Learning for Image Classification. Proc. of The 33rd British Machine Vision Conference (BMVC), London, UK, 2022.
- J. Wang, Y. Zhang, Y. Gu, T-K. Kim, SHAQ: Incorporating Shapley Value Theory into Multi-Agent Q-Learning, Proc. of Thirty-sixth Conference on Neural Information Processing Systems (NeurIPS), New Orleans, Louisiana, USA, 2022.
- J. Lee\*, M. Sung\*, H. Kim, T-K. Kim, Pop-Out Motion: 3D-Aware Image Deformation via Learning the Shape Laplacian, Proc. of IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), New Orleans, USA, 2022.
- D. Antotsiou, C. Ciliberto, T-K Kim, Modular Adaptive Policy Selection for Multi-Task Imitation Learning through Task Division, Proc. of Int. Conf. on Robotics and Automation (ICRA), Philadelphia, USA, 2022.
- J. Sun, B. Bhattarai, Z. Chen T-K. Kim, SeCGAN: Parallel Conditional Generative Adversarial Networks for Face Editing via Semantic Consistency, Proc. of AI for Content Creation Workshop at CVPR, New Orleans, USA, 2022.
- S. Sapkota, B. Khanal, B. Bhattarai\*, B. Khanal, T-K. Kim, Label Geometry Aware Discriminator for Conditional Generative Networks, Prof. of 26th International Conference on Pattern Recognition (ICPR), Montréal, Québec, 2022.
- T. Kim, J. Wang, D. Antotsiou, T-K. Kim, Learning Policy from Suboptimal Demonstrations under Transition Dynamic Mismatch, ICML Workshop on Adaptive Experimental Design and Active Learning, Baltimore, USA, 2022.

**2021**

- L. Wang, Y. Chae, S. Yoon, T-K. Kim, K-J. Yoon, EvDistill: Asynchronous Events to End-task Learning via Bidirectional Reconstruction-guided Cross-modal Knowledge Distillation, Proc. of IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2021.
- W. Luo, J. Xing, A. Milan, X. Zhang, W. Liu, T-K. Kim, Multiple object tracking: A literature review, Journal of Artificial Intelligence, 293:103448, 2021.
- L. Wang, T-K. Kim, K. Yoon, Joint Framework for Single Image Reconstruction and Super-resolution with an Event Camera, IEEE Trans on PAMI (TPAMI), (01):1-1, 1 Sep 2021.
- X. Shi, Q. Ye, X. Chen, C. Chen, Z. Chen, T-K. Kim, Geometry-based Distance Decomposition for Monocular 3D Object Detection, Proc. of IEEE Int. Conf. on Computer Vision (ICCV), 2021.
- Z. Chen, T-K. Kim, Learning Feature Aggregation for Deep 3D Morphable Models, Proc. of IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2021.
- R. Caramalau, B. Bhattarai, T-K. Kim, Sequential Graph Convolutional Network for Active Learning, Proc. of IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2021.
- J. Wang, Y. Zhang, T-K. Kim, Y. Gu, Modelling hierarchical structure between dialogue policy and natural language generator with option framework for task-oriented dialogue system, Proc. of Ninth International Conference on Learning Representation (ICLR), 2021.
- D. Antotsiou, C. Ciliberto, T-K Kim, Adversarial Imitation Learning with Trajectorial Augmentation and Correction, Proc. of Int. Conf. on Robotics and Automation (ICRA), Xi’an, China, 2021.
- J. Lee, B. Bhattarai, T-K. Kim, Face Parsing from RGB and Depth Using Cross-Domain Mutual Learning, Proc. of CVPR Workshop on Analysis and Modeling of Faces, 2021.
- R. Bodur, B. Bhattarai, T-K. Kim, 3D Dense Geometry-Guided Facial Expression Synthesis by Adversarial Learning, Proc. of Winter Conference on Applications of Computer Vision (WACV), Virtual Hawaii, US, 2021.
- R. Caramalau, B. Bhattarai, T-K. Kim, Active Learning for Bayesian 3D Hand Pose Estimation, Proc. of Winter Conference on Applications of Computer Vision (WACV), Virtual Hawaii, US, 2021.

## 학술 활동

랩 Activities 페이지(Professional Activities and Talks)의 2021년 이후 항목이다. 연도와 글은 페이지 표기 그대로다.[^activities]

- 2027 · Keynote, BMVA Symposium on Motion Intelligence, British Computer Society (BCS), London, UK
- 2026 · General Chair, the 3rd Int, Conf, on Artificial Intelligence, Deep Learning and Neural Networks (AIDLNN 2026), Dec 18-20, Edingburgh, UK
- 2026 · Keynote, Korea Software Congress 2026, Korea
- 2026 · Invited talk, Conf. for the 52nd Anniversary of the Korean Scientists and Engineers Association in the UK (KSEA-UK), London, UK
- 2026 · Invited talk, Toshiba Cambridge Research Laboratory, Cambridge, UK
- 2026 · Invited talk, Queen Mary University of London, Oct, UK
- 2026 · Invited talk, Huawei Darwin Research Center, King’s Cross, London, UK
- 2026 · Keynote, 3rd International Conference on Robotics, AI & Machine Learning (ICRAML 2026), Nov 18-20, 2026, Osaka, Japan
- 2026 · Keynote, 10th International Conference on Vision, Image and Signal Processing (ICVISP 2026), Dec 11-13, 2026, Haikou, China
- 2026 · Invited talk, Advanced Intellectual Property Strategy (AIP) CEO Program, KAIST
- 2026 · Invited talk, Army Innovation 4.0 Senior Policy Decision-Making Program, KAIST
- 2026 · Keynote, Summer Annual Conference of Korea Data Mining Society, Korea
- 2026 · Invited talk, AC Workshop at European Conf. on Computer Vision (ECCV), Malmö, Sweden
- 2026 · Invited lectures, Seocho AI College, KAIST
- 2027 · Area Chair of The IEEE / CVF Computer Vision and Pattern Recognition Conference (CVPR), Denver, Colorado, USA
- 2027 · Area Chair for The Fifteenth International Conference on Learning Representations (ICLR), San Francisco, California, USA
- 2027 · Area chair of 41st AAAI Conference on Artificial Intelligence (AAAI), Montréal, Canada
- 2027 · Area Chair, IEEE/CVF Winter Conference on Applications of Computer Vision (WACV 2027)
- 2027 · Keynote speaker, 3rd Int. Conf. on Generative Artificial Intelligence and Digital Media (GADM 2027), Kunming, China
- 2027 · General co-chair, 3rd Int. Conf. on Generative Artificial Intelligence and Digital Media (GADM 2027), Kunming, China
- 2026 · Invited talk, KAIST Convergence CEO Program (AMP), Seoul
- 2026 · Board Member of Korean Institute of Information Scientists and Engineers (KIISE)
- 2026 · General co-chair, the 2026 2nd Int. Conf. on Computer Vision and Image Computing (CVIC 2026), Hong Kong
- 2026 · General Chair, Int. Conf. on Optical Imaging and Deep Learning (OIDL 2026), June, Jeju Island, Republic of Korea
- 2026 · General co-chair, the 2nd Int. Symposium on Machine Learning and Social Computing (MLSC 2026), October, Bangkok, Thailand
- 2027 · General co-chair, 9th Int. Conf. on Image, Video and Signal Processing (IVSP 2025), Sapporo, Japan
- 2027 · General co-chair, 8th Int. Conf. on Machine Learning and Human-Computer Interaction (MLHMI 2025), Sapporo, Japan
- 2026 · Area Chair, Asian Conference on Computer Vision (ACCV), Osaka, Japan
- 2026 · Area Chair, The Fortieth Annual Conference on Neural Information Processing Systems (NeurIPS), Sydney, Australia
- 2026 · Senior Area Chair, European Conf. on Computer Vision (ECCV), Malmö, Sweden
- 2026 · Technical Program Committee Chair, 2nd Int. Conf. on Generative AI and Digital Media Arts (GAIDMA 2026), Guilin, China
- 2026-current · Associate Editor of ACM Transactions on Autonomous and Adaptive Systems (TAAS)
- 2026 · Honorary Chair, International Conference on Robotics and Learning (ICRL 2026), Yili, China, July 2026.
- 2026 · Keynote speaker, 4th International Conference on Advanced Sensing and Intelligent Systems (ICASIS 2026), May 16-18, 2026, Hong Kong
- 2026 · General Chair of International Conference on Computer Vision and Neural Networks(CVNN 2026), Chengdu, China
- 2025 · Panelist, National Assembly Policy Debate on "Strategies and Challenges for Sovereign AGI", 9 Dec
- 2025-current · Associate Editor of IEEE Trans on PAMI (TPAMI)
- 2026 · Area Chair of the Forty-Third International Conference on Machine Learning (ICML), Seoul
- 2026 · Area Chair of the Fourteenth International Conference on Learning Representations (ICLR), Rio de Janeiro, Brazil
- 2026 · Area Chair of Winter Conference on Applications of Computer Vision (WACV), Tucson, Arizona, US
- 2026 · Area chair of 40th AAAI Conference on Artificial Intelligence (AAAI), Singapore
- 2026 · General chair, 2nd Int. Conf. on Computer Vision and Augmented Reality (CVAR 2026), Changsha, China
- 2026 · Keynote speaker, 8th Int. Conf. on Image, Video and Signal Processing (IVSP 2026), Tokyo, Japan, Mar
- 2026 · Keynote speaker, 7th Int. Conf. on Machine Learning and Human-Computer Interaction (MLHMI 2026), Tokyo, Japan, Mar
- 2025 · Invited talk, KAIST Convergence CEO Program (AMP), Seoul
- 2025 · Invited talk, Army Innovation 4.0 Senior Policy Decision-Making Program, KAIST
- 2025 · Invited talk, Advanced Intellectual Property Strategy (AIP) CEO Program, KAIST
- 2025 · Keynote speaker, Int. Conf.on Machine Vision, Intelligent Imaging and Pattern Recognition (MVIIPR 2025), Singapore, November
- 2025 · Keynote, at the Affective and Behavior Analysis in-the-wild (ABAW) Workshop (in conjunction with ICCV 2025), Honolulu, Hawaii, Oct
- 2025 · General chair, Int. Conference on Computer Vision and Image Computing (CVIC 2025), Hongkong, China
- 2025 · Area chair of 16th Asian Conference on Machine Learning (ACML), Taipei, Taiwan
- 2025 · Area chair of IEEE/CVF Int. Conference on Computer Vision (ICCV), Honolulu, Hawai'i
- 2025 · General chair, 8th International Conference on Computer Information Science and Application Technology (CISAT 2025), Kunming, China
- 2025 · Keynote speaker, 7th Int. Conf. on Image, Video Processing and Artificial Intelligence (IVPAI), Bangkok, Thailand, 18-20, May
- 2025-current · Future Strategy Committee Chair, SoC, KAIST
- 2025-current · Division Chair in Visual and Social Computing, SoC, KAIST
- 2025 · Invited seminar, Colloquium of Software Graduate School – KTAI, KAIST, Korea, 26 May
- 2025 · Invited talk, Winter workshop of Korean Artificial Intelligence Association, Seoul AI-Hub, Korea
- 2025 · Invited seminar, Colloquium of Metaverse Graduate School, KAIST, Korea, 22 May
- 2025 · Keynote speaker, IEEE Int. Conf. on Pattern Recognition, Machine Vision and Artificial Intelligence (PRMVAI 2025), Loudi, China, 20-22, Jun
- 2025 · General chair of 8th Int. Conference on Machine Learning and Natural Language Processing (MLNLP 2025), Hangzhou, China
- 2024-current · Advisory board member, ELSP journal of Robot Learning
- 2025 · General co-chair and keynote speaker, Int. Conf. on Computer Vision, Pattern Recognition and Detection (ICVPRD 2025), Chongqing, China, 25-26 Oct
- 2025 · Program chair of 3rd Asia Conf. on Computer Vision, Image Processing and Pattern Recognition (CVIPPR 2025), Xiamen, China
- 2025 · General co-chair and keynote speaker, 7th Int. Conf. on Image, Video and Signal Processing (IVSP 2025), Kawasaki, Japan
- 2025 · General co-chair and keynote speaker, 6th Int. Conf. on Machine Learning and Human-Computer Interaction (MLHMI 2025), Kawasaki, Japan
- 2025 · Area chair of 39th AAAI Conference on Artificial Intelligence (AAAI), Philadelphia, Pennsylvania, US
- 2024 · Year 2024 College of Engineering Impact Research Award, KAIST
- 2024 · Technology Innovation Award, College of Engineering, KAIST
- 2024 · General co-chair, Int. Conf. on Intelligent Communication and Machine Learning (ICML 2024), Tokyo, Japan
- 2024 · Invited talk, ASPIRE Forum 2024, Tsinghua University, Beijing, China
- 2024 · Invited seminar, Colloquium of Software Graduate School – KTAI, KAIST, Korea
- 2024 · Area chair of Asian Conf. on Machine Learning (ACML), Hanoi, Vietnam
- 2024 · Area chair of Asian Conf. on Computer Vision (ACCV), Hanoi, Vietnam
- 2024 · Lead Area chair of European Conf. on Computer Vision (ECCV), Milano, Italy
- 2024 · Area chair of IEEE Conf. on Computer Vision and Pattern Recognition (CVPR), Seattle, Washington, US
- 2024 · Area chair of 38th AAAI Conference on Artificial Intelligence (AAAI), Vancouver, Canada
- 2023 · Program chair of British Machine Vision Conference (BMVC), Aberdeen, UK
- 2023 · Invited lecture, the 10th International Gran Canaria School on Deep Learning (DeepLearn 2023 Summer), Las Palmas de Gran Canaria, Spain
- 2023 · Invited talk, AI Thrust Seminar Series of Department of Computer Science, HKUST, Hongkong
- 2023 · Invited talk, Rakuten, Japan
- 2023 · Invited talk, Seminar series of Department of Computer Science, Durham university, UK
- 2023 · Invited AI lectures, Daewoo Shipbuilding & Marine Engineering Co., Ltd, Korea
- 2023 · Area chair of IEEE/CVF Int. Conference on Computer Vision (ICCV), Paris, France
- 2023-current · Consultancy chair for KAIST Science Gifted Education Center
- 2023-current · Committee of KAIST C2 (Creative Challenge) research project evaluation
- 2023 · Invited talk and forum panelist, Samsung Display AI Challenge Fair, Korea
- 2023 · Invited talk, Fall Colloquium of Graduate School of Metaverse, KAIST
- 2023 · Invited talk, Korea Conf. on Computer Vision, Seoul, Korea
- 2023 · Invited talk, Samsung Display – KAIST Equipment AI and Diagnostics Forum, Korea
- Nov 2023 · Program Chair of 7th Int. Conf. on Vision, Image and Signal Processing (ICVISP), Dali, China
- 2023 · Invited seminar, Colloquium of Software Graduate School – KTAI, KAIST, Korea
- 2023-current · Technical Consultant for K-Water
- 2023 · National Defense R&D AI forum panellist
- 2022 · Year 2022 College of Engineering Impact Research Award, KAIST
- 2022 · Invited AI lectures, Statistics Korea
- 2022 · Invited talk, AI Jump Up Seminar Series of Samsung Display Co.
- 2022 · Invited talk, Colloquium of KAIST Software Graduate School
- 2022-current · Technical Consultant for GB SOFT Co.
- 2023 · Area chair of 37th AAAI Conference on Artificial Intelligence (AAAI)
- 2023 · Workshops/tutorials chair of IEEE Int. Conf. on Automatic Face and Gesture Recognition (FG), Buenos Aires, Argentina
- 2023 · Area chair of IEEE Int. Conf. on Automatic Face and Gesture Recognition (FG), Buenos Aires, Argentina
- 2022 · Area chair of IEEE Conf. on Computer Vision and Pattern Recognition (CVPR)
- 2022 · Area chair of European Conf. on Computer Vision (ECCV)
- 2022 · Area chair of Thirty-Sixth AAAI Conference on Artificial Intelligence (AAAI)
- 2022 · General co-chair of IEEE/CVF 6th workshop on observing and understanding hands in action (HANDS), (in conjunction with ECCV), Tel-Aviv, Israel
- 2022-current · AJOU Global Fellow
- 2022-current · Steering committee, SW education center IT academy, KAIST
- 2021-current · International Cooperation Committee Chair, SoC, KAIST
- 2021 · Invited AI lectures, Daewoo Shipbuilding & Marine Engineering Co., Ltd
- 2021 · Invited AI lectures, Statistics Korea
- 2021 · Invited AI lectures, KT Corporation/Korea Shipbuilding & Offshore Engineering Co., Ltd

## 연락과 위치

- 교수실: KAIST 전산학부동(E3-5) 202호[^home]
- 교수 이메일: kimtaekyun@kaist.ac.kr[^home]

[^home]: 연구실 누리집 첫 화면 <https://sites.google.com/view/tkkim> (2026-10-20 열람)
[^students]: Students 페이지 <https://sites.google.com/view/tkkim/students> (2026-10-20 열람)
[^papers]: Publications 페이지 <https://sites.google.com/view/tkkim/publications> (2026-10-20 열람)
[^activities]: Activities 페이지 <https://sites.google.com/view/tkkim/activities> (2026-10-20 열람)
[^grants]: Grants 페이지 <https://sites.google.com/view/tkkim/grants> (2026-10-20 열람)
[^p1]: J. Lee, M. Sung, H. Choi, T.-K. Kim, 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 21169-21178 (2023). <https://doi.org/10.1109/cvpr52729.2023.02028> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J. Lee 외, T.-K. Kim, 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 527-537 (2024). <https://doi.org/10.1109/cvpr52733.2024.00057> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: M. Kim, T.-K. Kim, 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 10726-10735 (2024). <https://doi.org/10.1109/cvpr52733.2024.01020> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: S. Lee, T.-K. Kim, 2025 IEEE/CVF International Conference on Computer Vision (ICCV), 5757-5768 (2025). <https://doi.org/10.1109/iccv51701.2025.00545> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. Kim, T.-K. Kim, 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 9202-9211 (2024). <https://doi.org/10.1109/cvpr52733.2024.00879> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: J. Jang, K. Lee, T.-K. Kim, 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 227-236 (2023). <https://doi.org/10.1109/cvpr52729.2023.00030> 초록 기준(Semantic Scholar 등록 초록).

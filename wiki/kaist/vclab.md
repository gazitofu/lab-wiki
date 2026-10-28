# 비주얼 컴퓨팅 연구실 (Visual Computing Laboratory, VCLAB)

**KAIST 전산학부 · 김민혁 교수, 석좌교수(Endowed Chair Professor)**

- 분야: 컴퓨터 그래픽스와 비전, 계산 영상, 초분광·3차원 영상, 재질 반사 측정, 색과 시각 인지
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: 컴퓨터 비전[^research][^p6], 컴퓨터 그래픽스·기하 처리[^research][^p3], 3차원 복원·인식[^p4][^p5], 광학 영상·현미경[^research][^p8], 의료 영상 기기·재구성[^p1]
- 홈페이지: <http://vclab.kaist.ac.kr/>
- 근거와 출처: [VCLAB 근거 페이지](vclab-sources.md)

> 카메라와 계산 방법을 함께 설계해 빛에서 물체의 모양·색·재질 정보를 얻고, 그 정보를 바탕으로 실제 장면을 복원하거나 컴퓨터 영상으로 재현하는 연구실이다.[^research][^dept]

## 무엇을 연구하나

김민혁 교수가 이끄는 VCLAB은 컴퓨터 그래픽스(컴퓨터로 모양과 장면을 만들고 영상으로 표현하는 기술)와 컴퓨터 비전(사진·영상에서 대상과 장면의 정보를 알아내는 기술)을 함께 연구한다. 광원에서 나온 빛이 물체의 표면을 지나 사람의 시각에 도달하기까지의 현상에 관심을 두며, 빛·색·모양과 이들 사이의 관계를 계산으로 다룬다. 연구의 대상에는 물체의 재질이 보이는 방식, 파장(파동의 같은 진동 상태가 공간적으로 되풀이되는 간격)에 따른 빛의 정보, 사람이 색을 느끼는 방식이 들어간다.[^research]

한 축은 계산 영상(computational imaging, 광학 장치와 계산 방법을 함께 이용해 영상을 얻고 복원하는 기술)이다. 여러 좁은 파장 구간별로 빛의 세기를 기록하는 초분광 영상, 물체의 입체적인 모양을 재는 3차원 영상, 밝기의 넓은 범위를 기록·표현하는 HDR(High Dynamic Range) 영상을 연구한다. 영상 센서가 기록한 자료를 복원하는 계산과 빛을 기록하는 장치의 설계를 연결한다. 대표적으로 회절(파동이 장애물이나 구멍을 지나며 퍼져 진행하는 현상)을 이용한 광학 소자와 신경망(연결된 계산 단위와 연결의 세기로 입력을 출력으로 바꾸는 계산 모형)을 함께 설계해, 한 번 촬영한 영상에서 파장별 정보와 깊이를 얻었다. 최근에는 X선의 파장별 흡수를 고려한 단층 영상 복원도 다룬다.[^research][^p8][^p1]

다른 축은 측정한 영상에서 장면의 모양과 재질을 알아내고, 그 장면이 어떻게 보일지 계산하는 일이다. 전방향 영상에서 주변 공간의 표면을 복원하거나, 벽에 반사되어 돌아온 빛으로 직접 보이지 않는 대상을 복원한다. 이때 렌더링(장면과 빛의 모형에서 영상을 계산하는 과정)을 측정 자료와 연결해, 계산 결과가 실제 관측과 맞도록 장면의 표현과 촬영 관련 변수를 조정한다. 전방향 장면을 다룬 OmniSDF와 가려진 장면을 다룬 비가시선 영상 연구가 이 갈래에 해당한다.[^p4][^p5]

연구실은 색과 재질이 사람에게 보이는 방식도 연구한다. 편광(빛을 이루는 파동의 진동 방향과 시간에 따른 진동 양상에 관한 성질)을 포함한 빛의 반사를 계산하고, 원하는 반사색이 나오도록 표면 구조를 설계·제작한다. 또 HDR 화면에서 주변의 밝기를 고려해 사람이 명암 차이를 구별하는 민감도를 예측한다. 물체에서 나오는 빛의 물리적 정보와 사람이 느끼는 영상의 차이를 함께 다루는 것이다.[^research][^p2][^p3][^p7]

## 주요 연구 주제

### 계산 영상과 초분광 촬영

촬영 장치의 광학 소자와 영상 복원 알고리즘(문제를 풀기 위한 계산 절차)을 함께 설계한다. 초분광·깊이 영상 연구는 빛이 퍼지는 방식이 파장과 깊이에 따라 달라지도록 소자를 설계하고, 그 결과를 영상에서 되찾도록 학습한다. 학습 자료를 만들기 위한 측정 장치도 제작했다. X선 CT(computed tomography, 여러 방향의 투과 측정으로 물체 내부 구조를 영상화하는 기술) 연구에서는 여러 파장의 X선, 재료별 흡수, 촬영 시스템의 응답을 함께 모델링해 금속이 만드는 영상 왜곡을 줄인다.[^p8][^p1]

### 편광·재질과 물리 기반 렌더링

물리 기반 렌더링은 빛과 물체가 상호작용하는 법칙을 바탕으로 영상을 계산하는 방법이다. BRDF(Bidirectional Reflectance Distribution Function)는 빛이 들어오는 방향과 나가는 방향에 따른 표면의 반사 특성을 나타내는 함수다. 연구실은 파동광학(빛의 파동 성질로 빛의 진행과 상호작용을 설명하는 광학)을 이용해 반사광의 방향과 색을 함께 설계하고 실제 표면을 제작했다. 편광 렌더링에서는 방향별 편광을 표현하고 계산하는 방법을 새로 만들어, 편광을 가진 주변 조명 아래에서 실시간 영상을 계산했다.[^research][^p2][^p3]

### 3차원 장면·가려진 대상 복원

OmniSDF는 전방향 카메라를 원을 따라 움직여 촬영한 영상에서 정적인 장면의 모양과 겉모습을 복원한다. 공간을 나누어 표현하는 자료 구조를 장면에 맞춰 세분화해, 표면의 세부 형태와 계산에 필요한 저장 공간을 함께 고려한다. NLOS(Non-Line-of-Sight) 영상은 빛의 간접 경로에서 얻은 측정으로 직접 보이지 않는 장면을 복원하는 기술이다. 연구실은 측정한 반사광과 시뮬레이션의 차이를 줄이도록 촬영 관련 변수를 자동 보정하고, 가려진 물체의 표면 위치·방향과 빛을 반사하는 성질을 추정한다.[^p4][^p5]

### HDR 영상과 시각 인지

한 번의 촬영으로 HDR 영상을 얻기 위해 센서의 위치별 노출 시간을 달리하고, 색 정보 복원과 움직이는 물체가 겹쳐 보이는 흔적의 제거를 함께 다룬다. 시각 인지 연구에서는 대비 민감도(밝기 차이가 있는 무늬를 구별하는 시각의 민감도)를 주변 밝기까지 고려해 예측한다. 이 모형을 HDR 동영상 압축, 화면의 밝기 범위에 맞춰 영상 값을 바꾸는 톤 매핑, 두 영상의 시각적 차이 예측에 적용했다.[^p6][^p7]

## 대표 논문

계산 영상, 편광·재질 표현, 3차원 복원, HDR·시각 인지를 고르게 보여 주는 2021–2026년 논문 8편을 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다. 저자 역할은 논문 페이지의 전체 저자 순서에 따른다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 교수의 역할 |
|---|---|---|---|---|
| 1 | 2026 | [Splat-based Metal Artifact Reduction in Cone-Beam CT via Polychromatic Modeling](https://vclab.kaist.ac.kr/eg2026/index.html) · Computer Graphics Forum, Eurographics 2026 | CT 영상에서 금속 때문에 생기는 왜곡을 줄이는 복원 방법을 제안했다. X선의 파장별 성질, 재료에 따른 흡수와 장치의 응답을 부피 표현에 결합했다. 금속 영역을 사람이 따로 지정하지 않고 영상과 X선 특성을 함께 조정하며, 합성·실측 자료에서 왜곡 억제와 복원 정확도가 개선되었다.[^p1] | 1저자 Kiseok Choi, 마지막 저자 김민혁 |
| 2 | 2025 | [Designing and Fabricating Color BRDFs with Differentiable Wave Optics](https://vclab.kaist.ac.kr/siggraphasia2025p1/index.html) · ACM Transactions on Graphics, SIGGRAPH Asia 2025 | 빛의 파동 성질을 계산해 표면이 어느 방향으로 어떤 색의 빛을 반사할지 설계했다. 표면 구조를 조정하는 계산과 실제 제작을 연결해, 반사 세기와 색을 함께 조절하는 표면을 만들었다. 구조에 따라 나타나는 색과 보는 방향에 따라 변하는 색 등 서로 다른 반사 효과를 구현했다.[^p2] | 1저자 Yixin Zeng, 마지막 저자 김민혁 |
| 3 | 2024 | [Spin-Weighted Spherical Harmonics for Polarized Light Transport](https://vclab.kaist.ac.kr/siggraph2024/index.html) · ACM Transactions on Graphics, SIGGRAPH 2024 | 편광을 포함한 빛의 반사를 효율적으로 계산하도록 방향별 빛의 상태를 표현하는 방법을 제안했다. 회전에도 일관되는 표현과 빛의 전달 계산을 결합하고, 편광을 가진 주변 조명과 부드러운 그림자가 있는 장면에서 실시간 편광 렌더링을 보였다.[^p3] | 1저자 Shinyoung Yi, 마지막 저자 김민혁 |
| 4 | 2024 | [OmniSDF: Scene Reconstruction using Omnidirectional Signed Distance Functions and Adaptive Binoctrees](https://vclab.kaist.ac.kr/cvpr2024p2/index.html) · CVPR 2024 | 전방향 카메라를 작은 원을 따라 움직여 찍은 영상으로 실내·실외의 정적인 장면을 복원했다. 카메라 배치에 맞는 공간 표현을 쓰고 필요한 부분을 계산 중에 세분화했다. 비교 방법들에 비해 평균적인 모양 오차와 장면을 표현하는 데 필요한 공간 단위 수를 줄였다.[^p4] | 1저자 Hakyeong Kim, 마지막 저자 김민혁 |
| 5 | 2023 | [Self-Calibrating, Fully Differentiable NLOS Inverse Rendering](https://vclab.kaist.ac.kr/siggraphasia2023/index.html) · ACM SIGGRAPH Asia 2023 | 보이는 벽을 거쳐 돌아온 빛으로 가려진 장면을 복원한다. 시간에 따른 빛의 측정과 빛의 전달 계산을 맞추면서 촬영 관련 변수를 자동 보정했다. 잡음이 있는 조건에서도 물체의 모양과 빛을 반사하는 성질을 복원했다.[^p5] | 1저자 Kiseok Choi, 마지막 저자 김민혁 |
| 6 | 2023 | [Joint Demosaicing and Deghosting of Time-Varying Exposures for Single-Shot HDR Imaging](https://vclab.kaist.ac.kr/iccv2023/index.html) · ICCV 2023 | 한 센서에서 위치별로 노출 시간을 달리한 자료로 HDR 영상을 만든다. 노출 시간의 차이 때문에 움직이는 장면에 생기는 흔적과 센서의 색 정보 복원을 함께 해결하는 학습 방법을 제안했다. 합성·실측 자료에서 비교 대상 HDR 복원 방법보다 좋은 결과를 보였다.[^p6] | 1저자 Jungwoo Kim, 마지막 저자 김민혁 |
| 7 | 2022 | [Modelling Surround-aware Contrast Sensitivity for HDR Displays](https://vclab.kaist.ac.kr/cgf2022/index.html) · Computer Graphics Forum | HDR 화면을 보는 사람의 대비 민감도를 주변 밝기까지 고려해 예측하는 모형을 만들었다. 관측 자료에서 모형을 도출하고 기존 응용에 연결할 수 있는 실용형도 제시했다. HDR 영상 압축, 톤 매핑과 두 영상의 시각적 차이 예측에 적용한 예를 보였다.[^p7] | 1저자 Shinyoung Yi, 마지막 저자 김민혁 |
| 8 | 2021 | [Single-shot Hyperspectral-Depth Imaging with Learned Diffractive Optics](https://vclab.kaist.ac.kr/iccv2021/index.html) · ICCV 2021 | 회절을 이용한 광학 소자와 신경망 복원을 함께 설계해, 한 번 촬영한 영상에서 초분광 정보와 깊이를 동시에 얻었다. 빛이 퍼지는 모양이 파장과 깊이에 따라 달라지도록 하고 그 정보를 계산으로 복원했다. 학습용 측정 장치와 실험용 시제품을 만들고 합성·실측 실험으로 평가했다.[^p8] | 1저자 Seung-Hwan Baek, 마지막 저자 김민혁 |

## 교수와 전문 분야

김민혁 교수는 2010년 영국 University College London(UCL)에서 컴퓨터과학 박사학위를 받았고, 미국 Yale University의 박사후연구원을 거쳐 2012년 KAIST에 부임했다. 전산학부 교수 소개는 전공을 컴퓨터그래픽스·컴퓨터비전·머신러닝으로 적는다. 교수진 명단의 직위는 「교수, 석좌교수(Endowed Chair Professor)」이며, 개인 소개는 KAIST ICT-Endowed Chair Professor로 적는다.[^faculty][^roster][^prof]

전문 분야는 촬영 하드웨어와 계산을 결합하는 영상 기술, 3차원 형상과 재질의 측정, 물리적 빛의 전달과 영상 합성으로 이어진다. 최근 논문에서는 금속으로 인한 CT 영상 왜곡을 보정하는 방법과 표면의 반사색 설계가 나타나며, 편광 렌더링·전방향 장면 복원·초분광 촬영으로도 연결된다.[^p1][^p2][^p3][^p4][^p8] 시각 인지 쪽에서는 주변 밝기를 반영하는 HDR 대비 민감도 모형을 연구했다.[^p7]

교수 소개에 따르면 Eurographics 2022 Technical Paper Chair, SIGGRAPH Asia 2022 Course Chair, Pacific Graphics 2023 Program Co-Chair를 맡았다. 학술지 부편집장 경력에는 IEEE TPAMI(2024년부터), IEEE TVCG(2022년부터), ACM TOG(2014–2017), ACM TAP(2016–2023), IEEE TCI(2020–2022)가 적혀 있다.[^prof]

## 응용 분야

연구 소개는 3차원 그래픽스의 재질·색 표현과 실제 물체의 물리적 정보 측정을 연결한다.[^research] 대표 논문의 응용에는 CT 영상 재구성,[^p1] 구조에 따른 발색·제품 디자인·보안 인쇄,[^p2] 편광을 가진 조명 아래의 영상 합성,[^p3] 전방향 영상 기반 장면 복원,[^p4] 직접 보이지 않는 대상의 영상화,[^p5] HDR 촬영과 화면에 표시할 영상의 처리[^p6][^p7]가 있다. 반사색 설계 논문은 제품 디자인과 보안 인쇄 등에 쓸 가능성을 제시한다.[^p2]

## 구성원

2026년 10월 28일 People 페이지 기준으로 박사후연구원 1명, 박사과정 11명, 석사과정 4명이다. 과정은 누리집 표기다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Kiseok Choi (최기석) | 박사후연구원 | 1, 2, 5 |
| Inseung Hwang (황인승) | 박사과정 |  |
| Hakyeong Kim (김하경) | 박사과정 | 4 |
| Donggun Kim (김동건) | 박사과정 | 3 |
| Jiwoong Na (나지웅) | 박사과정 | 3 |
| Inchul Kim (김인철) | 박사과정 | 1, 5 |
| Hyeongjun Cho (조형준) | 박사과정 | 1 |
| Jaemin Cho (조재민) | 박사과정 | 1 |
| Dongyoung Choi (최동영) | 박사과정 | 5 |
| Seungmin Hwang (황승민) | 박사과정 |  |
| Sanghyeon Lee (이상현) | 박사과정 |  |
| Seeha Lee (이시하) | 박사과정 |  |
| Harin Kim (김하린) | 석사과정 |  |
| Jong Mo Park (박종모) | 석사과정 |  |
| Seung Chan Hwang (황승찬) | 석사과정 |  |
| Sejun Park (박세준) | 석사과정 |  |

## 졸업생과 이전 구성원

People 페이지 Alumni에 게시된 박사 10명(2019–2026년)과 석사 10명(2015–2026년)이다. 학위·연도·진로는 누리집 표기다. 최기석은 2026년 박사 졸업생과 현재 박사후연구원으로 함께 올라 있다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Kiseok Choi (최기석) | PhD (2026) | Postdoc Researcher, KAIST, Korea |
| Shinyoung Yi (이신영) | PhD (2025) | Professor of Computer Science, Kyung Hee University, Korea |
| Hyeonjoong Jang (장현중) | PhD (2025) | Reserach Institute Team Leader, Hypergram Inc., Korea |
| Hyunho Ha (하현호) | PhD (2025) | Research Scientist, Naver Labs, Korea |
| Andreas Meuleman | PhD (2023) | Postdoctoral Researcher, INRIA Sophia-Antipolis, France |
| Daniel S. Jeon (전석준) | PhD (2023) | Research Institute Director, Hypergram Inc., Korea |
| Joo Ho Lee (이주호) | PhD (2020) | Professor of Computer Science, Sogang University, Korea |
| Seung-Hwan Baek (백승환) | PhD (2019) | Professor of Computer Science, POSTECH, Korea |
| Giljoo Nam (남길주) | PhD (2019) | Research Scientist, Meta, United States |
| Inchang Choi (최인창) | PhD (2019) | Research Scientist, Apple, Cupertino, CA, United States |
| Woohyun Kang (강우현) | MS (2026) |  |
| Yejoon Kwon (권예준) | MS (2026) |  |
| Yeonwoo Lim (임연우) | MS (2026) |  |
| Jungwoo Kim (김정우) | MS (2023) |  |
| Mustafa Yaldiz | MS (2022) |  |
| Dahyun Kang (강다현) | MS (2021) |  |
| Hyun Jin Ku (구현진) | MS (2021) |  |
| Mingyun Kang (강민균) | MS (2018) |  |
| Yeong Beum Lee (이영범) | MS (2018) |  |
| Haebom Lee (이해봄) | MS (2015) |  |

## 최근 논문 목록 (2021–2026)

초분광·HDR 촬영, 편광과 재질 표현, 3차원 장면 복원, CT 영상 재구성 등을 다룬다. Publications의 2021–2026년 연도 구역 48편이며, 제목·저자·발표처와 그에 붙은 날짜는 연구실 게시 표기다. 2021년 구역은 해당 연도 전체를 포함한다.[^pubs]

**2026**

- Kiseok Choi, Jaemin Cho, Inchul Kim, Min H. Kim. "Splat-Based Metal Artifact Reduction in Cone-Beam CT via Compact Attenuation Modeling". *Proc. IEEE/CVF Computer Vision and Pattern Recognition (CVPR) 2026 Denver, Colorado, United States, Jun. 3--7, 2026*.
- Kiseok Choi, Hyeongjun Cho, Inchul Kim, Min H. Kim. "Revisiting Pose Sensitivity in Splat-based Computed Tomography under Sparse-view Reconstruction". *Proc. IEEE/CVF Computer Vision and Pattern Recognition (CVPR) 2026 Denver, Colorado, United States, Jun. 3--7, 2026*.
- Hakyeong Kim, Ruicheng Wang, Chengtang Yao, Jiaolong Yang, Min H. Kim. "Dense Metric Depth Completion from Sparse Direct Time-of-Flight Sensors". *Proc. IEEE/CVF Computer Vision and Pattern Recognition (CVPR) 2026 Denver, Colorado, United States, Jun. 3--7, 2026*.
- Hyeongjun Cho, Min H. Kim. "Joint Static Calibration for Multiview Phase-Measuring Profilometry". *Springer Nature Computer Science 2026, 7(6), published on June 18, 2026*.
- Jae-Myeong Kwon, Yejoon Kwon, Young-Gil Cha, Dong Hyun Han, Hyun-Kyung Kim, Je-Kyun Park, Min H. Kim, Ki-Hun Jeong. "Biologically inspired microlens array camera for high-resolution wide field-of-view imaging". *Nature Communications 2026 Mar. 23, 2026*.
- Kiseok Choi, Inchul Kim, Jaemin Cho, Hyeongjun Cho, Min H. Kim. "Splat-based Metal Artifact Reduction in Cone-Beam CT via Polychromatic Modeling". *Computer Graphics Forum (CGF), presented at Eurographics 2026 Aachen, Germany, May. 4--8, 2026*.
- Dongyoung Choi, Jaemin Cho, Woohyun Kang, Hyunho Ha, James Tompkin, Min H. Kim. "Splat-based Gradient-domain Fusion for Seamless View Transition". *Proc. Int. Conf. 3D Vision (3DV) 2026, Vancouver, BC, Canada, Mar. 20--23, 2026*.
- Sanghyeon Lee, Donghun Kang, Min H. Kim. "Consistent Multi-Lane Tracking with Temporally Recursive Spline Modeling". *Proc. Int. Conf. Computer Vision, Theory and Applications (VISAPP) 2026, Marbella, Spain, Mar. 9 -- 11, 2026*.
- Seeha Lee, Dongyoung Choi, Min H. Kim. "Diffusion-Based HDR Reconstruction from Mosaiced Exposure Images". *Proc. Int. Conf. Computer Vision, Theory and Applications (VISAPP) 2026, Marbella, Spain, Mar. 9 -- 11, 2026*.

**2025**

- Yixin Zeng, Kiseok Choi, Hadi Amata, Kaizhang Kang, Wolfgang Heidrich, Hongzhi Wu, Min H. Kim. "Designing and Fabricating Color BRDFs with Differentiable Wave Optics". *ACM Transactions on Graphics (TOG), presented at SIGGRAPH Asia 2025, 44(6), Dec. 15 – 18. 2025*.
- Shinyoung Yi, Jiwoong Na, Seungmin Hwang, Inseung Hwang, Min H. Kim. "Frame-Free Representation of Polarized Light for Resolving Stokes Vector Singularities". *ACM Transactions on Graphics (TOG), presented at SIGGRAPH Asia 2025, 44(6), Dec. 15 – 18. 2025*.
- Yunseong Moon, Ryota Maeda, Suhyun Shin, Inseung Hwang, Youngchan Kim, Min H. Kim, Seung-Hwan Baek. "Hyperspectral Polarimetric BRDFs of Real-world Materials". *Proc. ACM SIGGRAPH Asia 2025, Hong Kong, China, Dec. 15 – 18. 2025*.
- Hyeonjoong Jang, Dongyoung Choi, Donggun Kim, Woohyun Kang, Min H. Kim. "Splat-based 3D Scene Reconstruction with Extreme Motion-blur". *Proc. IEEE/CVF International Conference on Computer Vision (ICCV) 2025 Honolulu, HI, United States, Oct. 19 – 23, 2025*.
- Inseung Hwang, Kiseok Choi, Hyunho Ha, Min H. Kim. "Benchmarking Burst Super-Resolution for Polarization Images: Noise Dataset and Analysis". *Proc. IEEE/CVF International Conference on Computer Vision (ICCV) 2025 Honolulu, HI, United States, Oct. 19 – 23, 2025*.
- Hyunho Ha, Lei Xiao, Christian Richardt, Thu Nguyen-Phuoc, Changil Kim, Min H. Kim, Douglas Lanman, Numair Khan. "Geometry-guided Online 3D Video Synthesis with Multi-View Temporal Consistency". *Proc. IEEE/CVF Computer Vision and Pattern Recognition (CVPR) 2025 Nashville, TN, United States, Jun. 11--15, 2025*.
- Hyun-Kyung Kim, Young-Gil Cha, Jae-Myeong Kwon, Sang-In Bae, Kisoo Kim, Kyung-Won Jang, Yong-Jin Jo, Min H. Kim, Ki-Hun Jeong. "Biologically-inspired Microlens Array Camera for High-speed and High-sensitivity Imaging". *AAAS Science Advances, Jan. 1, 2025*.
- Jaemin Cho, Dongyoung Choi, Dahyun Kang, Gun Bang, Min H. Kim. "Editing Scene Illumination and Material Appearance of Light-Field Images". *Proc. International Conference on Computer Vision Theory and Applications (VISAPP 2025), Porto, Portugal, Feb. 26--28, 2025*.
- Hyeongjun Cho, Min H. Kim. "Joint Calibration of Cameras and Projectors for Multiview Phase Measuring Profilometry". *Proc. International Conference on Computer Vision Theory and Applications (VISAPP 2025), Porto, Portugal, Feb. 26--28, 2025*.

**2024**

- Hyunho Ha, Inseung Hwang, Nestor Monzon, Jaemin Cho, Donggun Kim, Seung-Hwan Baek, Adolfo Muñoz, Diego Gutierrez, Min H. Kim. "Polarimetric BSSRDF Acquisition of Dynamic Faces". *ACM Transactions on Graphics (TOG), presented at SIGGRAPH Asia 2024, 43(6), Dec. 3 -- 6, 2024*.
- Shinyoung Yi, Donggun Kim, Jiwoong Na, Xin Tong, Min H. Kim. "Spin-Weighted Spherical Harmonics for Polarized Light Transport". *ACM Transactions on Graphics (TOG), presented at SIGGRAPH 2024, 43(4), Jul. 28 - Aug. 1, 2024*.
- Dongyoung Choi, Hyeonjoong Jang, Min H. Kim. "OmniLocalRF: Omnidirectional Local Radiance Fields from Dynamic Videos". *Proc. IEEE/CVF Computer Vision and Pattern Recognition (CVPR 2024) Seattle, United States, Jun. 17 – 21, 2024*.
- Hakyeong Kim, Andreas Meuleman, Hyeonjoong Jang, James Tompkin, Min H. Kim. "OmniSDF: Scene Reconstruction using Omnidirectional Signed Distance Functions and Adaptive Binoctrees". *Proc. IEEE/CVF Computer Vision and Pattern Recognition (CVPR 2024) Seattle, United States, Jun. 17 – 21, 2024*.
- Numair Khan, Min H. Kim, James Tompkin. "Are Multi-view Edges Incomplete for Depth Estimation?". *International Journal of Computer Vision (IJCV) Published in 2024*.

**2023**

- Kiseok Choi, Inchul Kim, Dongyoung Choi, Julio Marco, Diego Gutierrez, Min H. Kim. "Self-Calibrating, Fully Differentiable NLOS Inverse Rendering". *Proc. ACM SIGGRAPH Asia 2023 Sydney, NSW, Australia, December 12 -- 15, 2023*.
- Jungwoo Kim, Min H. Kim. "Joint Demosaicing and Deghosting of Time-Varying Exposures for Single-Shot HDR Imaging". *Proc. IEEE/CVF International Conference on Computer Vision (ICCV 2023) Paris, France, Oct. 4 -- 6, 2023*.
- Young-Gil Cha, Jiwoong Na, Hyun-Kyung Kim, Jae-Myeong Kwon, Seok-Haeng Huh, Seung-Un Jo, Chang-Hwan Kim, Min H. Kim, Ki-Hun Jeong. "Microlens array camera with variable apertures for single-shot high dynamic range (HDR) imaging". *Optics Express (OE) Vol. 31, Issue 18, pp. 29589-29595 (2023)*.
- Donggun Kim, Hyeonjoong Jang, Inchul Kim, Min H. Kim. "Spatio-Focal Bidirectional Disparity Estimation from a Dual-Pixel Image". *Proc. IEEE/CVF Computer Vision and Pattern Recognition (CVPR 2023) Vancouver, Canada, Jun. 18 - 22, 2023*.
- Daniel S. Jeon, Andreas Meuleman, Seung-Hwan Baek, Min H. Kim. "Polarimetric iToF: Measuring High-Fidelity Depth through Scattering Media". *Proc. IEEE/CVF Computer Vision and Pattern Recognition (CVPR 2023) Vancouver, Canada, Jun. 18 - 22, 2023*.
- Andreas Meuleman, Yu-Lun Liu, Chen Gao, Jia-Bin Huang, Changil Kim, Min H. Kim, Johannes Kopf. "Progressively Optimized Local Radiance Fields for Robust View Synthesis". *Proc. IEEE/CVF Computer Vision and Pattern Recognition (CVPR 2023) Vancouver, Canada, Jun. 18 - 22, 2023*.
- Hyeonjoong Jang, Sanghoon Cho, Daniel S. Jeon, Dahyun Kang, Myeongho Song, Changhyun Park, Jaewon Kim, Min H. Kim. "Automated Visual Inspection of Defects in Transparent Display Layers using Light-Field 3D Imaging". *IEEE Transactions on Semiconductor Manufacturing (TSM) Published on May 26, 2023*.
- Myeong-Su Ahn, Jaehun Jeon, Charles Soon Hong Hwang, Daniel S. Jeon, Min H. Kim, Ki-Hun Jeong. "Actively Tunable Spectral Filter for Compact Hyperspectral Camera using Angle-Sensitive Plasmonic Structures". *Advanced Materials Technologies 2201482, published on April 4, 2023*.

**2022**

- Inseung Hwang, Daniel S. Jeon, Adolfo Muñoz, Diego Gutierrez, Xin Tong, Min H. Kim. "Sparse Ellipsometry: Portable Acquisition of Polarimetric SVBRDF and Shape with Unstructured Flash Photography". *ACM Transactions on Graphics (TOG), presented at SIGGRAPH 2022, 41(4), Aug. 8 - Aug. 11, 2022*.
- Hyeonjoong Jang, Andréas Meuleman, Dahyun Kang, Donggun Kim, Christian Richardt, Min H. Kim. "Egocentric Scene Reconstruction From an Omnidirectional Video". *ACM Transactions on Graphics (TOG), presented at SIGGRAPH 2022 41(4), Aug. 8 - Aug. 11, 2022*.
- Andreas Meuleman, Hakyeong Kim, James Tompkin, Min H. Kim. "FloatingFusion: Depth from ToF and Image-stabilized Stereo Cameras". *Proc. European Conference on Computer Vision (ECCV 2022) Tel Aviv, Oct. 23 – 27, 2022*.
- Donghun Kang, Hyeonjoong Jang, Jungeon Lee, Chong-Min Kyung, Min H. Kim. "Uniform Subdivision of Omnidirectional Camera Space for Efficient Spherical Stereo Matching". *Proc. IEEE Computer Vision and Pattern Recognition (CVPR 2022) New Orleans, USA, Jun. 19 - 24, 2022*.
- Hyun Jin Ku, Hyunho Ha, Joo Ho Lee, Dahyun Kang, James Tompkin, Min H. Kim. "Differentiable Appearance Acquisition from a Flash/No-flash RGB-D Pair". *Proc. IEEE International Conference on Computational Photography (ICCP 2022) Caltech, Pasadena, August 1-3, 2022*.
- Lingfei Song, Lizhi Wang, Min H. Kim, Hua Huang. "High-Accuracy Image Formation Model for Coded Aperture Snapshot Spectral Imaging". *IEEE Transactions on Computational Imaging (TCI) published in February, 2022*.
- Shinyoung Yi, Daniel S. Jeon, Ana Serrano, Se-Yoon Jeong, Hui-Yong Kim, Diego Gutierrez, Min H. Kim. "Modelling Surround-aware Contrast Sensitivity for HDR Displays". *Computer Graphics Forum (CGF) published in January, 2022*.

**2021**

- Numair Khan, Min H. Kim, James Tompkin. "Edge-aware Bi-directional Diffusion for Dense Depth Estimation from Light Fields". *Proc. British Machine Vision Conference (BMVC) 2021 Virtual, November 22nd - 25th, 2021*.
- Shinyoung Yi, Donggun Kim, Kiseok Choi, Adrian Jarabo, Diego Gutierrez, Min H. Kim. "Differentiable Transient Rendering". *ACM Transactions on Graphics (TOG), presented at SIGGRAPH Asia 2021 40(6), Dec. 14 - Dec. 17, 2021*.
- Mustafa B. Yaldiz, Andreas Meuleman, Hyeonjoong Jang, Hyunho Ha, Min H. Kim. "DeepFormableTag: End-to-end Generation and Recognition of Deformable Fiducial Markers". *ACM Transactions on Graphics (TOG), presented at SIGGRAPH 2021 40(4), Aug. 9 - Aug. 13, 2021*.
- Seung-Hwan Baek, Hayato Ikoma, Daniel S. Jeon, Yuqi Li, Wolfgang Heidrich, Gordon Wetzstein, Min H. Kim. "Single-shot Hyperspectral-Depth Imaging with Learned Diffractive Optics". *Proc. IEEE International Conference on Computer Vision (ICCV) 2021 Montreal, Canada & Virtual, Oct 11, 2021 – Oct 17, 2021*.
- Shinyoung Yi, Daniel S. Jeon, Ana Serrano, Se-Yoon Jeong, Hui-Yong Kim, Diego Gutierrez, Min H. Kim. "Modeling Surround-aware Contrast Sensitivity". *Proc. Eurographics Symposium on Rendering (EGSR) 2021 Saarbrucken, Germany & Virtual, June 29 - July 2, 2021*.
- Andreas Meuleman, Hyeonjoong Jang, Daniel S. Jeon, Min H. Kim. "Real-Time Sphere Sweeping Stereo from Multiview Fisheye Images". *Proc. IEEE Computer Vision and Pattern Recognition (CVPR 2021, Oral) Nashville, Tennessee, USA, June 19--25, 2021*.
- Hakyeong Kim, Andreas Meuleman, Daniel S. Jeon, Min H. Kim. "High-Quality Stereo Image Restoration from Double Refraction". *Proc. IEEE Computer Vision and Pattern Recognition (CVPR 2021) Nashville, Tennessee, USA, June 19--25, 2021*.
- Hyunho Ha, Joo Ho Lee, Andreas Meuleman, Min H. Kim. "NormalFusion: Real-Time Acquisition of Surface Normals for High-Resolution RGB-D Scanning". *Proc. IEEE Computer Vision and Pattern Recognition (CVPR 2021) Nashville, Tennessee, USA, June 19--25, 2021*.
- Numair Khan, Min H. Kim, James Tompkin. "Differentiable Diffusion for Dense Depth Estimation from Multi-view Images". *Proc. IEEE Computer Vision and Pattern Recognition (CVPR 2021) Nashville, Tennessee, USA, June 19--25, 2021*.
- Dahyun Kang, Daniel S. Jeon, Hakyeong Kim, Hyeonjoong Jang, Min H. Kim. "View-dependent Scene Appearance Synthesis using Inverse Rendering from Light Fields". *Proc. IEEE International Conference on Computational Photography (ICCP 2021) Haifa, Israel, May 23--25, 2021*.

## 수상·선정

2021년 10월 13일–2026년 10월 13일 범위의 연구·교수 수상과 회원 선정 5건이다. 월이 적힌 항목은 그 월을, 연도만 적힌 항목은 연도를 적었다.[^home][^news][^prof]

- 2026년 5월 · 「Splat-based Metal Artifact Reduction in Cone-Beam CT via Polychromatic Modeling」이 Eurographics 2026 Best Paper Award를 받았다.
- 2025년 · 김민혁 교수가 한국공학한림원 일반회원으로 선정되었다.
- 2024년 · SK-Hynix Excellence Award of Outstanding Inventions in Industry-Academic Research: 비행시간 영상의 깊이 정확도 향상 연구.
- 2022년 · SK-Hynix Grand Prize of Outstanding Inventions in Industry-Academic Research: 비행시간 영상의 잡음 제거 연구.
- 2022년 7월 · 「Sparse Ellipsometry: Portable Acquisition of Polarimetric SVBRDF and Shape」이 SIGGRAPH Technical Paper Award Honorable Mention(입선)으로 선정되었다.

## 연구 소식

News Archives에 게시된 2022년 3월–2026년 3월의 논문 채택 소식 22건이다. 조건부 채택과 채택은 원문의 구분을 따른다.[^news]

- 2026년 3월 · 3차원 영상 논문이 CVPR 2026에 채택되었다.
- 2026년 3월 · CT 영상 논문이 CVPR 2026에 채택되었다.
- 2026년 3월 · CT 보정 논문이 CVPR 2026에 채택되었다.
- 2025년 8월 · BRDF 제작 논문이 SIGGRAPH Asia 2025에 조건부 채택되었다.
- 2025년 8월 · 초분광 영상 논문이 SIGGRAPH Asia 2025에 조건부 채택되었다.
- 2025년 8월 · 편광 논문이 SIGGRAPH Asia 2025에 조건부 채택되었다.
- 2025년 7월 · 편광 영상 논문이 ICCV 2025에 채택되었다.
- 2025년 7월 · 3차원 영상 논문이 ICCV 2025에 채택되었다.
- 2025년 3월 · 시점 합성 논문이 CVPR 2025에 채택되었다.
- 2024년 8월 · 얼굴 측정 논문이 SIGGRAPH Asia 2024에 조건부 채택되었다.
- 2024년 3월 · 편광 렌더링 논문이 SIGGRAPH 2024에 조건부 채택되었다.
- 2024년 3월 · 신경망을 이용한 새 시점 합성 논문이 CVPR 2024에 채택되었다.
- 2024년 3월 · 신경망을 이용한 3차원 복원 논문이 CVPR 2024에 채택되었다.
- 2023년 10월 · 비가시선 영상 논문이 SIGGRAPH Asia 2023에 채택되었다.
- 2023년 7월 · 단일 촬영 HDR 논문이 ICCV 2023에 채택되었다.
- 2023년 3월 · 신경망 기반 렌더링 논문이 CVPR 2023에 채택되었다.
- 2023년 3월 · 빛의 비행시간을 이용한 영상 논문이 CVPR 2023에 채택되었다.
- 2023년 3월 · 듀얼 픽셀 논문이 CVPR 2023에 채택되었다.
- 2022년 7월 · 센서 융합 논문이 ECCV 2022에 채택되었다.
- 2022년 3월 · 전방향 3차원 복원 논문이 SIGGRAPH 2022에 조건부 채택되었다.
- 2022년 3월 · 편광을 이용한 3차원 복원 논문이 SIGGRAPH 2022에 조건부 채택되었다.
- 2022년 3월 · 전방향 스테레오 논문이 CVPR 2022에 채택되었다.

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291, KAIST 전산학부 E3-1 2418호, 우편번호 34141[^about]
- 구성원 공간: People 페이지는 박사후연구원과 일부 박사과정의 방을 2418호, 다른 학생들의 방을 2402호로 적는다.[^people]
- 교수 연구실: E3-1 2403호[^faculty][^roster]
- 연구실 전화: +82-42-350-7864, 대표 전화: +82-42-350-7807[^about]
- 학과 연구실 소개의 전화: 042-350-3564[^dept]

## 각주
[^home]: VCLAB 누리집 첫 화면, Latest News와 연구실 이름. <http://vclab.kaist.ac.kr/> 관측 2026-10-27.
[^research]: VCLAB, Research Areas: Computer Graphics & Vision. <http://vclab.kaist.ac.kr/researchareas.html> 관측 2026-10-28.
[^people]: VCLAB, People, 현재 구성원과 Alumni. <http://vclab.kaist.ac.kr/people.html> 관측 2026-10-28.
[^pubs]: VCLAB, Publications, 2021–2026년 연도 구역의 논문 목록과 게시 초록. <http://vclab.kaist.ac.kr/publications.html> 관측 2026-10-28.
[^about]: VCLAB, About Us, 소속과 연락·위치 안내. <http://vclab.kaist.ac.kr/aboutus.html> 관측 2026-10-28.
[^news]: VCLAB, News Archives, 2021–2026년 구역. <http://vclab.kaist.ac.kr/news.html> 관측 2026-10-28.
[^dept]: KAIST 전산학부, 비주얼 컴퓨팅 연구실 소개, 지도교수·소속·세부 연구·위치. <https://cs.kaist.ac.kr/research/labView?sn=62&menu=64> 관측 2026-10-27.
[^roster]: KAIST 전산학부 교수진 명단, 김민혁 항목, 직위·전공·교수연구실. <https://cs.kaist.ac.kr/people/faculty> 관측 2026-10-27.
[^faculty]: KAIST 전산학부, 김민혁 교수 소개, 학위·부임 시기·전공·교수연구실. <https://cs.kaist.ac.kr/people/view?idx=460&kind=faculty&menu=160> 관측 2026-10-28.
[^prof]: Min H. Kim 개인 소개, 연구 관심·직위·수상·학술 활동. <https://vclab.kaist.ac.kr/minhkim/index.html> 관측 2026-10-28.

[^p1]: K. Choi 외, M. H. Kim, Computer Graphics Forum (Proc. EUROGRAPHICS 2026) 45 (2026). <https://vclab.kaist.ac.kr/eg2026/index.html> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://vclab.kaist.ac.kr/eg2026/index.html> 관측 2026-10-28.
[^p2]: Y. Zeng 외, M. H. Kim, ACM Transactions on Graphics (Proc. SIGGRAPH Asia 2025) 44 (2025). <https://vclab.kaist.ac.kr/siggraphasia2025p1/index.html> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://vclab.kaist.ac.kr/siggraphasia2025p1/index.html> 관측 2026-10-28.
[^p3]: S. Yi 외, M. H. Kim, ACM Transactions on Graphics (Proc. SIGGRAPH 2024) 43 (2024). <https://vclab.kaist.ac.kr/siggraph2024/index.html> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://vclab.kaist.ac.kr/siggraph2024/index.html> 관측 2026-10-28.
[^p4]: H. Kim 외, M. H. Kim, IEEE Conference on Computer Vision and Pattern Recognition (CVPR) (2024). <https://vclab.kaist.ac.kr/cvpr2024p2/index.html> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://vclab.kaist.ac.kr/cvpr2024p2/index.html> 관측 2026-10-28.
[^p5]: K. Choi 외, M. H. Kim, Proceedings of ACM SIGGRAPH Asia 2023 (2023). <https://vclab.kaist.ac.kr/siggraphasia2023/index.html> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://vclab.kaist.ac.kr/siggraphasia2023/index.html> 관측 2026-10-28.
[^p6]: J. Kim, M. H. Kim, Proc. IEEE/CVF International Conference on Computer Vision (ICCV 2023) (2023). <https://vclab.kaist.ac.kr/iccv2023/index.html> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://vclab.kaist.ac.kr/iccv2023/index.html> 관측 2026-10-28.
[^p7]: S. Yi 외, M. H. Kim, Computer Graphics Forum (CGF) (2022). <https://vclab.kaist.ac.kr/cgf2022/index.html> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://vclab.kaist.ac.kr/cgf2022/index.html> 관측 2026-10-28.
[^p8]: S.-H. Baek 외, M. H. Kim, Proc. IEEE International Conference on Computer Vision (ICCV) (2021). <https://vclab.kaist.ac.kr/iccv2021/index.html> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://vclab.kaist.ac.kr/iccv2021/index.html> 관측 2026-10-28.

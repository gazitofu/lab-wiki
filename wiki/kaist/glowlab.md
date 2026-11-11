# GLOW Lab (Generative Learning of Worlds)

**KAIST 김재철AI대학원 · 김승욱 조교수**

- 분야: 시각적 월드 모델, 영상 생성과 환경 예측, 학습 기반 시뮬레이션, 행동 계획, 영상의 압축 표현[^home][^dept]
- 대분야: 컴퓨팅·AI
- 태그: 생성 인공지능[^home], 월드 모델[^home]
- 홈페이지: <https://glow-lab-kaist.github.io/>
- 근거와 출처: [GLOW Lab 근거 페이지](glowlab-sources.md)

> 행동에 따라 주변 환경이 어떻게 변하는지 배우는 인공지능을 만들어, 실제 환경을 대신하는 모의실험과 행동 계획에 연결하는 연구실이다.[^home]

## 무엇을 연구하나

GLOW Lab은 월드 모델(행동이나 조건에 따라 다음 장면이나 상태가 어떻게 바뀔지 배우는 인공지능 모형)을 연구한다.[^home] 연구의 출발점은 현실적인 그림이나 영상을 만드는 데서 나아가, 환경이 시간에 따라 변하고 행동에 반응하는 방식을 배우는 것이다. 연구실은 이런 시각적 월드 모델을 현실을 대신하는 시뮬레이터(대상의 움직임이나 변화를 모의하는 장치나 프로그램)와 행동을 정하는 모형이라는 두 역할로 다룬다.[^home]

첫 번째 역할에서는 행동 조건에 맞는 영상을 만드는 생성 인공지능(학습 자료의 성질을 바탕으로 새 영상·글 같은 자료를 만드는 인공지능)을 연구한다.[^home] 신경망(서로 연결된 계산 단위 사이의 연결 세기를 자료에서 배우는 계산 모형)을 이용하는 게임·로봇 시뮬레이터와, 원하는 조건에 맞게 조절할 수 있는 영상 생성을 연구한다. 두 번째 역할에서는 월드 모델이 예측한 변화를 행동 계획에 사용한다. 정책(관측이나 상태에 따라 행동을 정하는 규칙)을 만드는 모형의 바탕으로 월드 모델을 쓰고, 영상으로 정책을 나타내는 방법과 상태 변화에서 필요한 행동을 거꾸로 찾는 방법을 다룬다.[^home]

이 두 역할을 받치는 자료의 표현 방식도 연구 대상이다. 연구실은 잠재 공간(관측 자료를 직접 드러나지 않는 특징의 값으로 나타내는 공간)이 환경 예측과 제어(대상이 원하는 상태로 움직이도록 입력을 정하는 일)에 적합하려면 어떤 성질을 가져야 하는지 묻는다. 영상을 압축해 나타내는 방식, 예측을 통해 자료의 특징을 배우는 방식, 환경의 변화가 잘 드러나는 내부 표현을 연구한다. 월드 모델을 현실 환경을 감지하고 그 안에서 행동하는 시스템을 위한 물리적 인공지능의 바탕으로 본다.[^home]

## 주요 연구 주제

### 1. 환경을 대신하는 영상·월드 시뮬레이터

행동을 조건으로 주었을 때 뒤따르는 장면을 예측하고, 그 예측을 게임과 로봇의 모의 환경에 사용하는 연구다. 생성한 영상의 변화를 조절할 수 있게 하는 것도 이 갈래에 포함된다.[^home]

### 2. 월드 모델에 기반한 행동 계획

학습한 환경의 변화 규칙을 이용해 행동을 계획한다. 앞으로의 영상을 행동 정책으로 사용하는 접근과, 원하는 상태 변화에 필요한 행동을 찾는 역동역학(상태 변화로부터 그 변화를 일으킬 행동을 구하는 관계)을 연구한다.[^home]

### 3. 예측과 제어에 적합한 내부 표현

영상의 압축 표현과 잠재 공간의 설계, 예측을 통한 표현 학습(주어진 자료의 유용한 특징을 학습으로 얻는 방법)을 다룬다. 환경의 움직임을 담는 표현이 예측과 행동 선택을 어떻게 받칠 수 있는지가 연구 질문이다.[^home]

## 대표 논문

김승욱 교수가 2026년 8월 KAIST에 부임한 뒤의 연구 가운데, 저자 소속이 KAIST AI로 명시된 논문 한 편이다. EMNLP 2026 채택이 명시된 arXiv 사전 공개본을 설명한다. 「쉽게 말하면」 칸은 이 논문의 초록만을 근거로 썼다.[^cv][^affiliation][^p1]

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [Compositional SVG Generation via VLM-Driven Hierarchical Semantic Parsing](https://doi.org/10.48550/arXiv.2609.14657) · EMNLP 2026 (채택, arXiv 사전 공개본) | 시각·언어 모형(Vision-Language Model, 영상과 언어를 함께 다루는 모형)을 이용해 SVG(Scalable Vector Graphics, 도형과 경로로 그림을 나타내는 형식)를 의미 있는 부분별로 나누어 생성하는 방법이다. 장면을 큰 구성에서 작은 구성으로 나누고, 각 부분의 의미를 실제 영상 위치에 연결하며 가려진 형태를 복원한다. 부분의 묶음과 편집 가능성을 평가하는 자료와 지표도 제안했다. 기존의 평면적인 경로 묶음 생성 방법과 비교해 부분을 묶는 품질과 편집 가능성이 개선되었다고 보고한다.[^p1] | 1저자 Sehwan Park·Taehoon Kim(공동 기여), 공저자 김승욱 |

## 교수와 전문 분야

김승욱 교수(Seung Wook Kim)는 KAIST 김재철AI대학원 조교수이며 GLOW Lab을 이끈다. 교수 이력서에 따르면 2026년 8월 KAIST에 부임했으며, 첫 화면 소식은 같은 달 연구실이 문을 열었다고 알린다. 그전에는 NVIDIA에서 Research Scientist(2020–2023)와 Senior Research Scientist(2023–2026)로 일하며 시뮬레이션과 물리적 인공지능을 위한 생성 모형을 연구했다.[^cv][^people][^home][^dept]

토론토대학교에서 학사·석사·박사 학위를 받았으며, 박사 지도교수는 Sanja Fidler다. 교수 소개가 제시하는 전문 분야는 월드 모델과 신경망 기반 시뮬레이션, 영상과 입체·시간 변화 장면의 생성, 이를 받치는 내부 표현이다. 이전 연구의 예로 GameGAN·DriveGAN·Cosmos·OmniDreams, Video LDM·NeuralField-LDM·Align Your Gaussians를 든다.[^people]

## 응용 분야

연구실은 게임·로봇 환경을 학습한 모형으로 모의하고, 미래 장면의 예측을 행동 계획에 쓰는 것을 연구한다. 원하는 조건으로 영상을 생성하는 것도 주요 응용이다.[^home] 대표 논문은 그림을 의미 있는 부분으로 나누어 생성하고 편집하는 그래픽 제작을 다룬다.[^p1]

## 구성원

누리집 People의 Students 구획에 게시된 6명이다. MS Student는 석사과정으로, Research Intern은 게시된 직위 그대로 적었다. 시작 시점은 첫 화면의 합류 소식에 적힌 연월이다. 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people][^home]

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Seoyeon Byun | 석사과정 | August 2026 | seooyxx@kaist.ac.kr |  |
| Wonjun Jang | Research Intern | August 2026 |  |  |
| Sanghyeop Kim | Research Intern | August 2026 |  |  |
| Ye Thu | Research Intern | August 2026 | kyawyethu@kaist.ac.kr |  |
| Minseo Kim | Research Intern | August 2026 |  |  |
| Yeonwoo Shin | Research Intern | August 2026 |  |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications의 2021–2026년 연도 구역에 게시된 논문 가운데 최근 5년(2021-10-13–2026-10-13)에 해당하는 22편이다. 연도·저자·발표처는 연구실 게시 표기를 따른다. 2026년 8월 KAIST 부임 전의 연구가 포함되어 있으며, 특히 2021–2025년 항목은 부임 전 연구다. 저자를 NVIDIA로만 적은 기술보고서는 그 게시 표기를 유지했다. 별표는 누리집이 밝힌 공동 기여 표시다.[^pubs][^cv]

Compositional SVG 논문의 「채택」은 arXiv가 명시한 학회 채택 상태다. Compositional SVG 논문, Instant NuRec, OmniDreams, EditGAN에 연결한 DOI는 arXiv 사전 공개본의 주소이며, 학회명은 연구실 게시 표기와 함께 구분해 적었다.[^p1][^editgan]

**2026**

- Sehwan Park\*, Taehoon Kim\*, Geonhee Han, Dohyun Kim, Seung Wook Kim, Paul Hongsuck Seo. "Compositional SVG Generation via VLM-Driven Hierarchical Semantic Parsing". *EMNLP 2026*. <https://doi.org/10.48550/arXiv.2609.14657> (채택, arXiv 사전 공개본)[^p1]
- NVIDIA. "Instant NuRec: Feed-Forward 3D Gaussian Reconstruction for Driving Scene Simulation". *NVIDIA Technical Report 2026*. <https://doi.org/10.48550/arXiv.2607.14203>
- NVIDIA. "NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation". *NVIDIA Technical Report 2026*. <https://doi.org/10.48550/arXiv.2606.03159>
- Dohyun Kim, Seungwoo Lyu, Seung Wook Kim, Paul Hongsuck Seo. "Direct Diffusion Score Preference Optimization via Stepwise Contrastive Policy-Pair Supervision". *ECCV 2026*. <https://doi.org/10.1007/978-3-032-37517-9_36>
- Huiling Liu, Eunnam Cho, Soyun Choi, Aecheon Jung, Seung Wook Kim, Sungeun Hong. "Connecting the Objects: Relational Occlusion Graphs for Amodal Segmentation". *Pattern Recognition Letters 2026*. <https://doi.org/10.1016/j.patrec.2026.06.021>

**2025**

- Xuanchi Ren\*, Yifan Lu\*, Tianshi Cao\*, Ruiyuan Gao\*, Shengyu Huang, Amirmojtaba Sabour, Tianchang Shen, Tobias Pfaff, Jay Zhangjie Wu, Runjian Chen, Seung Wook Kim, Jun Gao, Laura Leal-Taixe, Mike Chen, Sanja Fidler, Huan Ling. "Cosmos-Drive-Dreams: Scalable Synthetic Driving Data Generation with World Foundation Models". *NVIDIA Technical Report 2025*.
- Dohyun Kim\*, Sehwan Park\*, Geonhee Han, Seung Wook Kim, Paul Hongsuck Seo. "Random Conditioning with Distillation for Data-Efficient Diffusion Model Compression". *CVPR 2025*. <https://doi.org/10.1109/cvpr52734.2025.01734>
- NVIDIA. "Cosmos World Foundation Model Platform for Physical AI". *NVIDIA Technical Report 2025*.

**2024**

- Jiawei Ren, Kevin Xie, Ashkan Mirzaei, Hanxue Liang, Xiaohui Zeng, Karsten Kreis, Ziwei Liu, Antonio Torralba, Sanja Fidler, Seung Wook Kim, Huan Ling. "L4GM: Large 4D Gaussian Reconstruction Model". *NeurIPS 2024*.
- Letian Wang, Seung Wook Kim, Jiawei Yang, Cunjun Yu, Boris Ivanovic, Steven Waslander, Yue Wang, Sanja Fidler, Marco Pavone, Peter Karkus. "DistillNeRF: Perceiving 3D Scenes from Single-Glance Images by Distilling Neural Fields". *NeurIPS 2024*.
- Anita Hu, Nishkrit Desai, Hassan Abu Alhaija, Seung Wook Kim, Masha Shugrina. "Diffusion Texture Painting". *SIGGRAPH 2024*. <https://doi.org/10.1145/3641519.3657458>
- Huan Ling\*, Seung Wook Kim\*, Antonio Torralba, Sanja Fidler, Karsten Kreis. "Align Your Gaussians: Text-to-4D with Dynamic 3D Gaussians and Composed Diffusion Models". *CVPR 2024*.
- Koichi Namekata, Amirmojtaba Sabour, Sanja Fidler, Seung Wook Kim. "EmerDiff: Emerging Pixel-level Semantic Knowledge in Diffusion Models". *ICLR 2024*.
- Jiawei Yang, Boris Ivanovic, Or Litany, Xinshuo Weng, Seung Wook Kim, Boyi Li, Tong Che, Danfei Xu, Sanja Fidler, Marco Pavone, Yue Wang. "EmerNeRF: Emergent Spatial-Temporal Scene Decomposition via Self-Supervision". *ICLR 2024*.
- Katja Schwarz, Seung Wook Kim, Jun Gao, Sanja Fidler, Andreas Geiger, Karsten Kreis. "WildFusion: Learning 3D-Aware Latent Diffusion Models in View Space". *ICLR 2024*.

**2023**

- Daiqing Li\*, Huan Ling\*, Amlan Kar, David Acuna, Seung Wook Kim, Karsten Kreis, Antonio Torralba, Sanja Fidler. "DreamTeacher: Pretraining Image Backbones with Deep Generative Models". *ICCV 2023*.
- Seung Wook Kim\*, Bradley Brown\*, Kangxue Yin, Karsten Kreis, Katja Schwarz, Daiqing Li, Robin Rombach, Antonio Torralba, Sanja Fidler. "NeuralField-LDM: Scene Generation with Hierarchical Latent Diffusion Models". *CVPR 2023*.
- Andreas Blattmann\*, Robin Rombach\*, Huan Ling\*, Tim Dockhorn\*, Seung Wook Kim, Sanja Fidler, Karsten Kreis. "Align your Latents: High-Resolution Video Synthesis with Latent Diffusion Models". *CVPR 2023*.

**2022**

- Seung Wook Kim, Karsten Kreis, Daiqing Li, Antonio Torralba, Sanja Fidler. "PolymorphicGAN: Generating Aligned Samples Across Multiple Domains With Learned Morph Maps". *CVPR 2022*.
- Daiqing Li, Huan Ling, Seung Wook Kim, Karsten Kreis, Adela Barriuso, Sanja Fidler, Antonio Torralba. "BigDatasetGAN: Synthesizing ImageNet with Pixel-wise Annotations". *CVPR 2022*.
- Chetan L. Srinidhi, Seung Wook Kim, Fu-Der Chen, Anne L. Martel. "Self-Supervised Driven Consistency Training for Annotation Efficient Histopathology Image Analysis". *Medical Image Analysis 2022*. <https://doi.org/10.1016/j.media.2021.102256>

**2021**

- Huan Ling, Karsten Kreis, Daiqing Li, Seung Wook Kim, Antonio Torralba, Sanja Fidler. "EditGAN: High-Precision Semantic Image Editing". *NeurIPS 2021*. <https://doi.org/10.48550/arXiv.2111.03186> (연구실 기재: NeurIPS 2021, 연결 주소는 arXiv 사전 공개본)[^editgan]

## 소식

첫 화면 소식에 게시된 연구실 개소 소식이다. 날짜는 누리집에 적힌 연월이다.[^home]

- 2026년 8월 · KAIST 김재철AI대학원에서 GLOW Lab이 문을 열었다.

## 연락과 위치

- 교수 이메일: seungwookk@kaist.ac.kr[^people][^join]
- 교수 사무실: 양재캠퍼스 6층 604호[^dept]
- 연구실 주소: Seoul AI HUB, 108 Taebong-ro, Seocho-gu, Seoul 06764, Republic of Korea[^people]
[^home]: GLOW Lab, 연구실 소개·세 연구 갈래·소식. <https://glow-lab-kaist.github.io/> (관측 2026-11-09).
[^people]: GLOW Lab, People의 교수 소개·경력·Students·연락처와 주소. <https://glow-lab-kaist.github.io/people.html> (관측 2026-11-09).
[^cv]: 김승욱, 이력서 EMPLOYMENT의 2026년 8월 KAIST 김재철AI대학원 조교수 부임. <https://glow-lab-kaist.github.io/assets/CV-SeungWookKim.pdf> (관측 2026-11-11).
[^pubs]: GLOW Lab, Publications의 연도별 논문과 공동 기여 표기. <https://glow-lab-kaist.github.io/publications.html> (관측 2026-11-09).
[^dept]: KAIST 김재철AI대학원, 구성원 전임교수 구획의 김승욱 조교수·연구분야·사무실. <https://gsai.kaist.ac.kr/people-2/?lang=ko> (관측 2026-11-09).
[^join]: GLOW Lab, Join Us의 교수 업무 이메일과 연구실 주소. <https://glow-lab-kaist.github.io/join.html> (관측 2026-11-11).
[^affiliation]: S. Park 외, P. H. Seo, Compositional SVG Generation via VLM-Driven Hierarchical Semantic Parsing, arXiv 사전 공개본의 저자 소속 Seung Wook Kim, KAIST AI. <https://arxiv.org/html/2609.14657v1> (관측 2026-11-11).
[^editgan]: H. Ling 외, S. Fidler, EditGAN: High-Precision Semantic Image Editing, arXiv 사전 공개본, 2021-11-04. <https://arxiv.org/abs/2111.03186> (관측 2026-11-11).
[^p1]: S. Park 외, P. H. Seo, arXiv (EMNLP 2026 Main 채택) (온라인 2026-09-13). <https://doi.org/10.48550/arXiv.2609.14657> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2609.14657> (관측 2026-11-11).

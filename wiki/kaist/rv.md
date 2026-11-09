# KAIST Robotics and Vision Lab (RVLab)

**KAIST 문화기술대학원 · 임성훈 부교수**

- 분야: 컴퓨터 비전, 로봇 학습, 3차원 장면 이해·복원, 다중 자료 이해와 이미지·영상 생성
- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 컴퓨터 비전[^home][^contact], 3차원 복원·인식[^home][^contact], 멀티모달 AI[^home][^contact], 생성 인공지능[^home][^contact]
- 홈페이지: <https://rv.kaist.ac.kr/>
- 근거와 출처: [KAIST Robotics and Vision Lab 근거 페이지](rv-sources.md)

> 영상으로 공간을 이해하고, 글과 영상으로 새 장면을 만들며, 로봇이 실제 환경에서 행동을 배우게 하는 연구실이다.[^home]

## 무엇을 연구하나

임성훈 부교수가 이끄는 연구실은 컴퓨터 비전(사진·영상으로 물체와 장면의 정보를 알아내는 기술), 로봇 학습, 멀티모달 인공지능(영상·글처럼 종류가 다른 자료를 함께 이해하고 다루는 인공지능)을 연구한다. 인공지능은 학습·추론 같은 지적 작업을 컴퓨터로 수행하게 하는 기술이며, 영문은 Artificial Intelligence, 약칭은 AI다. 연구실은 실제 세계에서 지각하고 판단하며 행동하는 기계를 위한 피지컬 인공지능(로봇처럼 실제 물리 환경에서 지각하고 행동하는 기계에 쓰는 인공지능)을 목표로, 3차원 지각과 장면 이해부터 로봇·자율 시스템의 시각·언어·행동 모델까지 연구한다고 소개한다.[^home]

공간을 이해하는 갈래에서는 여러 시점의 영상에서 물체의 모양과 위치를 알아내는 3차원 복원·인식을 다룬다. 또 생성 인공지능(학습한 자료를 바탕으로 새 이미지·영상·글 등을 만드는 인공지능)으로 이미지와 영상을 생성·편집하며, 서로 다른 종류의 자료를 연결해 해석한다.[^home][^contact] 예를 들어 EviSplat은 글로 물체를 찾을 때 필요한 시점별 시각 정보를 미리 하나로 합쳐 버리지 않고 남겨 두었다가, 질문에 맞는 정보를 선택해 3차원 장면의 물체 영역을 찾는다.[^p2]

로봇 학습의 목표는 실제 환경에서 로봇의 행동 규칙을 배우고 계획하는 것이다.[^contact] CANTABILE은 피아노 건반을 누르는 음과 시점뿐 아니라 강약까지 학습 대상으로 삼고,[^p1] RAIN은 작업을 행동 종류와 목표 영역으로 나눈 작은 작업들의 순서로 나타내어, 배운 기술을 새 물체나 배치에 재사용하도록 한다.[^p5] 여기서 정책은 로봇이 관측한 정보에서 다음 행동을 정하는 규칙이다.

## 주요 연구 주제

### 1. 로봇의 정교한 조작과 작업 일반화

피아노 연주 로봇에서는 건반을 누르는 강약을 목표로 주고, 음을 빼먹지 않으면서 그 목표를 맞추도록 보상(행동의 바람직함을 평가해 학습에 사용하는 값)을 설계한다. RAIN에서는 목표 물체의 영역과 여러 시점의 영상을 함께 이용하고, 작은 작업의 완료 여부를 추정해 다음 작업으로 넘어간다. 일반화는 학습에 쓰지 않은 자료나 환경에서도 배운 규칙을 적용하는 성질이다.[^p1][^p5]

### 2. 글로 검색할 수 있는 3차원 장면

EviSplat은 물체·부분·배경 영역에 대해 개별 관측의 특징을 보존하고, 글 질의와 관련된 관측을 골라 장면의 영역을 나눈다. 장면을 표현하는 각 요소에 대해서도 어떤 관측이 근거가 되는지 함께 고려한다.[^p2]

### 3. 시간대가 바뀐 도로 장면의 표현

PAM-ToD는 미리 학습한 도로의 3차원 장면 표현을 고정하고, 소수의 목표 시간대 이미지에서 색 보정만 배운다. 장면 전체·위치·개별 표현 요소에 따라 보정을 달리하고, 가로등이 켜질 때처럼 밝기가 추가되는 변화도 다룬다. 표면이 빛을 반사하는 비율(알베도)과 조명을 각각 추정하지 않고 시간대 사이의 외관 변화를 배운다.[^p3]

### 4. 참조 대상의 모습을 유지하는 이미지 생성

CRAFT는 참조 이미지 속 사람이나 물체를 새 장면에서도 같은 대상으로 알아볼 수 있도록 하는 이미지 개인화를 연구한다. 참조 대상이 새 장면에 놓인 정답 합성 이미지를 학습 자료로 요구하지 않고, 참조 이미지와 대상 영역 표시만으로 모델을 조정한다. 주의 기제(입력 정보 사이의 관련성에 따라 반영 비중을 정하는 계산 방식)를 학습 보상과 연결해, 생성 과정이 올바른 참조 대상을 보도록 한다.[^p4]

## 대표 논문

임성훈 교수가 2026년 7월 KAIST에 부임한 뒤 공개된 논문 가운데, KAIST 저자 소속과 초록을 확인한 다섯 편을 로봇 학습·3차원 장면·이미지 생성 갈래에서 골랐다. 아래는 모두 arXiv 사전 공개본 기준이며, “쉽게 말하면” 칸은 각 논문의 초록만을 근거로 썼다.[^prof]

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [CANTABILE: Learning Expressive Dynamics for Robotic Piano Performance](https://doi.org/10.48550/arXiv.2609.18213) · arXiv 사전 공개본 | 로봇 피아노 연주에서 어떤 음을 언제 누르는지와 함께 타건 강약을 학습한다. 예정된 강약 목표를 행동 규칙에 주고 강약 일치 보상과 음을 빠뜨리지 않도록 하는 보상을 결합한다. 기본 연주 규칙은 고정한 채 손가락의 추가 움직임을 조정하며, 다시 학습하지 않고 실행 중 연주 강도를 조절하는 방법도 제시한다.[^p1] | 1저자 Woosik Kim, 마지막 저자 임성훈 |
| 2 | 2026 | [EviSplat: Preserving Multi-View Evidence in 3D Gaussian Splatting for Open-Vocabulary Segmentation](https://doi.org/10.48550/arXiv.2609.34853) · arXiv 사전 공개본 | 자유로운 글 질문으로 3차원 장면의 물체 위치와 영역을 찾는다. 같은 물체를 여러 방향에서 본 관측을 질문 전에 하나의 요약으로 합치지 않고 보존한다. 질문에 관련된 관측을 고르고, 개별 장면 요소가 실제로 뒷받침하는 근거와 관측의 신뢰도를 결합해 영역을 정한다.[^p2] | 1저자 Sungho Moon, 마지막 저자 임성훈 |
| 3 | 2026 | [PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://doi.org/10.48550/arXiv.2610.11572) · arXiv 사전 공개본 | 이미 만든 도로 장면을 다른 시간대처럼 보이게 바꾸는 추가 모듈(일정 기능을 맡도록 나누어 만든 구성 부분)이다. 원래 장면 표현을 고정하고 소수의 목표 시간대 이미지로 색과 밝기 보정을 배운다. 장면 전체·위치·개별 요소의 변화를 나누어 다루며, 평가에서는 비교 방법보다 이미지 품질 지표가 개선되었다.[^p3] | 1저자 Kota Shimomura, 임성훈은 끝에서 두 번째 저자 |
| 4 | 2026 | [CRAFT: Constrained Reward via Attention Fine-Tuning for Subject Personalization without Composed Targets](https://doi.org/10.48550/arXiv.2608.14403) · arXiv 사전 공개본 | 참조 속 대상을 같은 대상으로 알아볼 수 있도록 하면서 새 장면을 생성하도록 모델을 조정한다. 참조와 정답 합성 장면의 짝 대신 참조 이미지와 대상 영역 표시를 사용한다. 생성 과정이 참조 대상의 어느 부분을 보는지에 보상을 주고, 같은 대상을 유지하는 이미지 보상과 맞춘다. 다른 참조 입력형 모델에도 적용해 성능 개선을 보였다.[^p4] | 1저자 Jihun Park, 마지막 저자 임성훈, Yan Zhang과 공동 교신저자 |
| 5 | 2026 | [RAIN: Robotic Task Generalization with Region-Aware Interaction Networks](https://doi.org/10.48550/arXiv.2610.14039) · arXiv 사전 공개본 | 작업을 행동 종류와 목표 영역으로 정한 작은 작업들의 순서로 표현한다. 목표 영역에 맞춰 여러 시점의 정보를 교환하고 움직임과 행동을 예측하며, 완료 여부를 추정해 다음 작업으로 넘어간다. 기록한 움직임에서 다른 목표 영역으로 접근하는 경로를 추가 자료 수집 없이 만든다. 작업을 이렇게 나눠 표현하므로 배운 기술을 다른 물체·배치에서 재사용하고 학습에 없던 작업 순서로 조합할 수 있다.[^p5] | 1저자 Seunghun Lee, 임성훈은 끝에서 두 번째 저자 |

## 교수와 전문 분야

임성훈 교수(Sunghoon Im)는 KAIST 문화기술대학원 부교수이며, 2026년 7월 부임했다. 2019년 9월 DGIST 조교수로 시작해 2023년 3월 부교수, 2024년 9월 DGIST Distinguished Professor가 되었고, 2025년 1월부터 2026년 5월까지 DGIST 슈퍼컴퓨팅·인공지능 교육연구센터장을 맡았다.[^dept][^prof] 서강대학교 전자공학 학사(2014), KAIST 전기및전자공학 석사(2016)와 박사(2019)를 받았으며, 카네기멜런대학교 방문연구와 Microsoft Research Asia 연구 인턴 경력이 있다.[^prof]

교수 소개의 연구 관심은 로봇 학습, 3차원 비전, 생성 인공지능이다. 구체적으로 로봇의 이동·조작, 장면 복원과 지각, 글 기반 이미지 편집·생성, 영상 생성 모델을 든다.[^prof] 대표 논문에서 드러나는 전문성은 로봇 행동 학습의 목표·보상 설계, 시각 관측과 글을 연결한 장면 이해, 관측 조건 변화에 맞춘 장면 표현, 참조 대상을 보존하는 이미지 생성이다.[^p1][^p2][^p3][^p4][^p5]

## 응용 분야

연구실은 로봇·자율 시스템의 시각 인지와 행동 학습, 이미지·영상 생성 및 편집을 응용 목표로 제시한다.[^home][^contact] 대표 논문은 피아노 연주 로봇, 글로 물체를 찾는 3차원 장면, 시간대가 달라지는 도로 장면, 참조 대상을 유지하는 시각 콘텐츠 생성, 새 배치에서의 탁상 로봇 작업을 다룬다.[^p1][^p2][^p3][^p4][^p5]

## 구성원

구성원 목록과 연구 그룹 목록의 비행정 구성원 27명이다. 상세 소개나 졸업생 진로에 소속이 적힌 경우 과정 옆 괄호에 함께 적었다. 일부 학생은 DGIST 재학으로 게시되어 있으며, KAIST 소속으로 표시된 사람과 함께 연구실 명단에 올라 있다. 소개 머리와 학력란의 과정이 다른 세 명은 두 표기를 병기했다. Yujin Han은 인턴이며 학력란에는 2027년 2월 KAIST 석사과정 예정으로 적혀 있다. 시작은 상세 소개의 과정 시작 표기이며 연구실 합류 시점과 구별된다. “대표 논문 참여”는 위 표의 번호이고, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members][^groups][^alumni][^member-details][^member-supp]

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Kyumin Hwang | 박사후연구원 (KAIST) |  | 3D Vision & Physical AI |  |
| Tianyi Zheng | 박사후연구원 |  | Multimodal & Generative AI |  |
| Jeonghoon Kim | 석박사통합과정 (DGIST) | Mar 2019 | Multimodal & Generative AI; Representation Learning; Data-efficient Learning |  |
| Sungho Moon | 박사과정 |  | Multimodal & Generative AI | 2, 3 |
| Jinhwoi Kim | 과정 표기 병기 (소개 머리: 박사과정; 학력란: DGIST 석사과정) |  | 3D Vision & Physical AI; Indoor 3D Reconstruction; Physically-based Realistic Rendering |  |
| Hyeon Kang | 박사과정 (DGIST) | Sep 2022 | Multimodal & Generative AI; Domain Adaptation; Meta Learning |  |
| Donghyeon Kim | 과정 표기 병기 (소개 머리: 박사과정; 학력란: DGIST 석박사통합과정) |  | Multimodal & Generative AI; Video Object Segmentation |  |
| Minwoo Choi | 석박사통합과정 (DGIST) | Mar 2022 | 3D Vision & Physical AI; Generative Adversarial Networks; Style Transfer; Neural Architecture |  |
| Wonhyeok Choi | 박사과정 |  | 3D Vision & Physical AI | 1, 2 |
| Sungmin Ha | 석박사통합과정 (DGIST) | Mar 2022 | 3D Vision & Physical AI; Multi-task Learning; Continual Learning |  |
| Jaekeun Lee | 박사과정 (DGIST) |  | 3D Vision & Physical AI; LiDAR Object Detection & Tracking; Semi/self-supervised Learning; Autonomous Driving |  |
| Jihun Park | 박사과정 |  | Multimodal & Generative AI | 4 |
| Jongmin Gim | 박사과정 (KAIST 문화기술대학원) |  | Multimodal & Generative AI | 4 |
| Kyoungmin Lee | 박사과정 (KAIST 문화기술대학원) |  | Multimodal & Generative AI | 4 |
| Yohan Lim | 석박사통합과정 (KAIST 문화기술대학원) | Mar 2023 | 3D Vision & Physical AI; Physical AI; 3D Representation; 3D Understanding |  |
| Siwon Kim | 과정 표기 병기 (소개 머리: 박사과정; 학력란: DGIST 석사과정) |  | 3D Vision & Physical AI; Vision Language Action, Vision-Language Model; Referring Video Object Segmentation; Domain Generalization, Object detection |  |
| Junwoo Park | 석사과정 (DGIST) | Mar 2025 | 3D Vision & Physical AI; 3D Computer Vision; 3D Reconstruction | 2 |
| Gihyun Baek | 석사과정 |  | 3D Vision & Physical AI |  |
| Jinhyung Lee | 석사과정 |  | 3D Vision & Physical AI |  |
| Haeun Yun | 석사과정 (DGIST) |  | 3D Vision & Physical AI; Vision Language Action, Vision-Language Model; Efficient Learning; Domain Generalization, Referring Video Object Segmentation |  |
| Hyeonseo Jo | 석사과정 |  | Multimodal & Generative AI | 4 |
| Minseok Oh | 석사과정 |  | Multimodal & Generative AI |  |
| Minjae Kim | 석사과정 (DGIST) |  | 3D Vision & Physical AI; Robotics; Vision-Language Action Models |  |
| Woosik Kim | 석사과정 |  | 3D Vision & Physical AI | 1 |
| Jaehoon Lee | 석사과정 |  | 3D Vision & Physical AI |  |
| Jiwon Jang | 석사과정 (KAIST 문화기술대학원) |  | 3D Vision & Physical AI; Vision-Language Model; Reinforcement Learning |  |
| Yujin Han | 인턴 (학력란: KAIST 문화기술대학원 석사과정, 2027년 2월 예정) |  | Multimodal & Generative AI; Multimodal AI; Generative AI |  |

## 졸업생과 이후 진로

누리집 Alumni에 게시된 박사후연구원 3행, 박사 4행, 석사 11행의 이력이다. 학위 기간은 임성훈 교수의 2026년 7월 KAIST 부임 전 DGIST 시기를 포함한다. 학위 과정 뒤 같은 연구실의 박사과정이나 박사후연구원으로 이어진 사람도 포함한다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Soyeop Yoo | Postdoctoral Researcher (2025.10 ~ 2026.08) | AIST, Japan |
| Hao Ni | Postdoctoral Researcher (2025.09 ~ 2025.12) | Research Scientist, Bytedance, China |
| Sehyun Hwang | Postdoctoral Researcher (2025.08 ~ 2025.10) | Research Scientist, Meta, USA |
| Seunghun Lee | Ph.D.(2019.03 ~ 2026.02), Postdoc(2026.02 ~ 2026.05) | Research Scientist, Huawei, Singapore |
| Jaeyeul Kim | Ph.D.(2021.09 ~ 2026.02), Postdoc(2026.02 ~ 2026.08) | Assistant Professor, Pukyong National University |
| Jungwan Woo | Ph.D.(2019.03 ~ 2026.08) | Research Scientist, ETRI |
| Kyumin Hwang | Ph.D.(2022.03 ~ 2026.08) | KAIST Postdoc |
| Seungjun Hyun | M.S.(2024.08 ~ 2026.08) | Dabeeo |
| Sanggyun Ma | M.S.(2024.03 ~ 2026.02) | KETI |
| Jiwan Seo | M.S.(2024.03 ~ 2026.02) | KETI |
| Wonjoon Choi | M.S.(2024.03 ~ 2026.02) | KETI |
| Kyoungmin Lee | M.S.(2023.09 ~ 2025.08) | Ph.D. Student, GSCT, KAIST |
| Kiljoon Han | M.S.(2023.03 ~ 2025.08) | DGIST |
| Jongmin Gim | M.S.(2023.03 ~ 2025.02) | Ph.D. Student, GSCT, KAIST |
| Mingyu Shin | M.S.(2022.09 ~ 2024.08) | Samsung Research |
| Changjae Kim | M.S. (2021.03 ~ 2023.02) | LG Electronics |
| Hojin Kim | M.S. (2021.03 ~ 2023.02) | SIA |
| Jinwoo Bae | M.S. (2021.03 ~ 2023.02) | Hyundai Motor Group |

## 최근 5년 논문 목록

논문 목록의 2021–2026년 구역과 별도 arXiv 구역에 게시된 56항목이다. 임성훈 교수의 2026년 7월 KAIST 부임 전 DGIST 등에서 수행한 연구가 함께 포함되어 있다. 연도·제목·저자·발표처는 누리집 표기를 따른다. arXiv 구역은 사전 공개본이고, 날짜 없이 Accepted로 적힌 학술지 항목은 “게재 승인”으로 표시했다. 소식에서 학회 채택을 알린 H-GenPO와 CRAFT는 “채택”으로 표시했다. 저자 옆 별표·십자 기호는 누리집 표시다.[^pubs][^prof][^news]

**2026**

- Sungho Moon , Kota Shimomura, Junwoo Park , Wonhyeok Choi , Seunghun Lee , Takayoshi Yamashita, Sunghoon Im. "EviSplat: Preserving Multi-View Evidence in 3D Gaussian Splatting for Open-Vocabulary Segmentation". *arXiv preprint ( arXiv ), 2026 · DOI 10.48550/arxiv.2609.34853*.
- Kota Shimomura, Sungho Moon , Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im , Hironobu Fujiyoshi. "PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting". *arXiv preprint ( arXiv ), 2026 · DOI 10.48550/arXiv.2610.11572*.
- Woosik Kim , Wonhyeok Choi , Sunghoon Im. "CANTABILE: Learning Expressive Dynamics for Robotic Piano Performance". *arXiv preprint ( arXiv ), 2026 · DOI 10.48550/arxiv.2609.18213*.
- Jinhyung Lee , Haeun Yun , Siwon Kim , Gihyun Baek , Sungho Moon , Sehyun Hwang , Sunghoon Im †. "RobOralScan: Learning Active Intraoral Scanning for Robotic Dental Reconstruction". *arXiv preprint ( arXiv ), 2026 · DOI 10.48550/arXiv.2606.26955*.
- Jihun Park\* , Jongmin Gim\* , Kyoungmin Lee\* , Minseok Oh , Minwoo Choi , Jaeyeul Kim , Woo Chool Park, Sunghoon Im †. "A Training-Free Style-aligned Image Generation with Scale-wise Autoregressive Model". *arXiv preprint ( arXiv ), 2026 · DOI 10.48550/arxiv.2504.06144*.
- Seunghun Lee\* , Jiwan Seo\* , Jeonghoon Kim\* , Sungho Moon\* , Siwon Kim , Haeun Yun , Hyogyeong Jeon, Wonhyeok Choi , Jaehoon Jeong, Zane Durante, Sang Hyun Park, Sunghoon Im †. "Temporal Grounding as a Learning Signal for Referring Video Object Segmentation". *arXiv preprint ( arXiv ), 2026 · DOI 10.48550/arxiv.2508.11955*.
- Wonhyeok Choi , Shutong Ding, Minwoo Choi , Jungwan Woo , Kyumin Hwang , Jaeyeul Kim , Ye Shi † , Sunghoon Im †. "A Review of Online Diffusion Policy RL Algorithms for Scalable Robotic Control". *arXiv preprint ( arXiv ), 2026*.
- Wonhyeok Choi , Minwoo Choi , Jaeyeul Kim , Kyumin Hwang , Jongmin Gim , Sunghoon Im †. "H-GenPO: Hierarchical Generative Policy Optimization via the Option-Critic Framework". *Neural Information Processing Systems ( NeurIPS ), 2026 (채택)*.
- Seunghun Lee \* , Kyuhwan Shim \* , Yeogyeong Song \* , Sihaeng Lee, Seung Hwan Kim, Byoung-Tak Zhang, Sunghoon Im † , Gunhee Lee †. "RAIN: Robotic Task Generalization with Region-Aware Interaction Networks". *European Conference on Computer Vision Workshop ( ECCV Workshop X-Reason ), 2026*.
- Kiljoon Han , Kyumin Hwang , Wonhyeok Choi , Jeonghoon Kim , Sunghoon Im †. "DEQ-Stereo: Deep Equilibrium Video Stereo Matching via Adaptive Convergence". *Asian Conference on Computer Vision ( ACCV ), 2026*.
- Sungho Moon\* , Jaeyeul Kim\* , Wonhyeok Choi , Jihun Park , Ukcheol Shin † , Sunghoon Im †. "Object-Centric LiDAR-to-Radar Distillation for 3D Object Detection". *IEEE Signal Processing Letters ( SPL ), 2026 · DOI 10.1109/lsp.2026.3722159*.
- Jihun Park , Kyoungmin Lee , Jongmin Gim , Hyeonseo Jo , Jaeyeul Kim , Han Zou, Zhenpeng Zhan, Yan Zhang † , Sunghoon Im †. "CRAFT: Constrained Reward via Attention Fine-Tuning for Subject Personalization without Composed Targets". *ACM SIGGRAPH Conference and Exhibition on Computer Graphics and Interactive Techniques in Asia ( SIGGRAPH Asia ), 2026 (채택)*.
- Byeonghun Lee, Hyunmin Cho, Sunghoon Im † , and Kyong Hwan Jin †. "ReAL: Reference-to-Image (R2I) Aware Latent Diffusion for Image Super-Resolution". *European Conference on Computer Vision ( ECCV ), 2026*.
- Jeonghoon Kim \* , Hyeon Kang \* , Jihun Park , Jinhwoi Kim , Jaeyeul Kim , Sunghoon Im †. "Mitigating Noisy Correspondence in Video-Text Retrieval via Noise-mined Adaptive Self-Labeling". *ACM Transactions on Multimedia Computing, Communications, and Applications ( TOMM ) , 2026 · DOI 10.1145/3827612*.
- SoYeop Yoo , Sunghoon Im †. "Learning to Forget: Emotional Salience as a Compression Mechanism for Long-Term AI Memory". *ACM SIGKDD Conference on Knowledge Discovery and Data Mining ( KDD ), 2026 · DOI 10.1145/3770855.3818653*.
- Kyumin Hwang\* , Wonhyeok Choi\* , Jaeyeul Kim , Jihun Park , Daehee Park † , Sunghoon Im †. "CascadeOcc: Rethinking 3D Occupancy World Models with Cascaded VQ Representations". *IEEE Signal Processing Letters ( SPL ), 2026 · DOI 10.1109/lsp.2026.3680426*.
- Wonhyeok Choi , Kyumin Hwang , Jihun Park , Kyoungmin Lee , Seunghun Lee , Jaeyeul Kim , Minwoo Choi , Sunghoon Im †. "TaskForce: Cooperative Multi-agent Reinforcement Learning for Multi-task Optimization". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2026*.
- Sungho Moon\* , Seunghun Lee\* , Jiwan Seo , Sunghoon Im †. "CVA: Context-aware Video-text Alignment for Video Temporal Grounding". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2026*.
- Kyoungmin Lee\* , Jihun Park\* , Jongmin Gim\* , Wonhyeok Choi , Kyumin Hwang , Jaeyeul Kim , Sunghoon Im †. "A Training-Free Style-Personalization via SVD-Based Feature Decomposition". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2026*.
- Minseok Oh\* , Jihun Park\* , Jongmin Gim , Minwoo Choi , Kyoungmin Lee , Ferdinando Fioretto † , Sunghoon Im †. "FREESTYLE: An Anchor-Free Mechanism for Training-Free Style-Aligned Image Generation". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ) Findings, 2026 · DOI 10.1109/cvprf71909.2026.00366*.
- Mingyu Choi, Woo Kyoung Han, Sunghoon Im † , Kyong Hwan Jin †. "Linear Recurrent Unit with Semantic Modulation for Image Super-Resolution". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ) Findings, 2026*.
- Kyumin Hwang\* , Wonhyeok Choi\* , Kiljoon Han , Wonjoon Choi , Minwoo Choi , Yongcheon Na, Minwoo Park, Sunghoon Im †. "Scale-invariant and View-relational Representation Learning for Full Surround Monocular Depth". *IEEE Robotics and Automation Letters ( RA-L ), 2026 · DOI 10.1109/lra.2025.3635451*.
- Jihun Park\* , Kyoungmin Lee\* , Jongmin Gim\* , Hyeonseo Jo , Minseok Oh , Wonhyeok Choi , Kyumin Hwang , Jaeyeul Kim , Minwoo Choi , Sunghoon Im †. "Infinite-Story: A Training-Free Consistent Text-to-Image Generation". *The Association for the Advancement of Artificial Intelligence ( AAAI ), 2026 ( Oral ) · DOI 10.1609/aaai.v40i10.37776*.
- Sanggyun Ma\* , Wonjoon Choi\* , Jihun Park , Jaeyeul Kim , Sunghoon Im †. "Semantic-Enhanced Monocular Depth Estimation via Fusion and Distillation of Foundation Models". *International Conference on Electronics, Information, and Communication ( ICEIC ), 2026; IEEE International Conference on Computer Vision Workshop ( ICCVw ), 2025 · DOI 10.1109/iceic69189.2026.11385908*.
- Sanggyun Ma , Wonjoon Choi , Jihun Park , Jaeyeul Kim , Seunghun Lee , Jiwan Seo , Sunghoon Im †. "Bridging Geometric and Semantic Foundation Models for Generalized Monocular Depth Estimation". *International Conference on Electronics, Information, and Communication ( ICEIC ), 2026 · DOI 10.1109/iceic69189.2026.11386238*.

**2025**

- Seunghun Lee\* , Jiwan Seo\* , Kiljoon Han , Minwoo Choi , Sunghoon Im †. "CAVIS: Context-Aware Video Instance Segmentation". *IEEE International Conference on Computer Vision ( ICCV ), 2025 · DOI 10.1109/iccv51701.2025.00429*.
- Seunghun Lee , Jiwan Seo , Minwoo Choi , Kiljoon Han , Jaehoon Jeong, Zane Durante, Ehsan Adeli † , Sang Hyun Park, Sunghoon Im †. "Latest Object Memory Management for Temporally Consistent Video Instance Segmentation". *IEEE International Conference on Computer Vision ( ICCV ), 2025*.
- Woo Kyoung Han, Yongjun Lee, Byeonghun Lee, Sang Hyun Park, Sunghoon Im † , Kyong Hwan Jin †. "JPEG Processing Neural Operator for Backward-Compatible Coding". *IEEE International Conference on Computer Vision ( ICCV ), 2025 · DOI 10.1109/iccv51701.2025.01813*.
- Jihun Park\* , Jongmin Gim\* , Kyoungmin Lee\* , Seunghun Lee , Sunghoon Im †. "Style-Editor: Text-driven object-centric style editing". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2025 ( Highlight ) · DOI 10.1109/cvpr52734.2025.01704*.
- Woo Kyoung Han, Byeonghun Lee, Hyunmin Cho, Sunghoon Im † , Kyong Hwan Jin †. "Towards Lossless Implicit Neural Representation via Bit Plane Decomposition". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2025 · DOI 10.1109/cvpr52734.2025.00217*.
- Jaeyeul Kim , Jungwan Woo , Ukcheol Shin, Jean Oh, Sunghoon Im †. "Flow4D: Leveraging 4D Voxel Network for LiDAR Scene Flow Estimation". *IEEE Robotics and Automation Letters ( RA-L ), 2025 · DOI 10.1109/lra.2025.3542327*.
- Wonhyeok Choi\* , Kyumin Hwang\* , Minwoo Choi , Kiljoon Han , Wonjoon Choi , Mingyu Shin , Sunghoon Im †. "Intrinsic Image Decomposition for Robust Self-supervised Monocular Depth Estimation on Reflective Surfaces". *The Association for the Advancement of Artificial Intelligence ( AAAI ), 2025 · DOI 10.1609/aaai.v39i3.32258*.
- Wonhyeok Choi\* , Kyumin Hwang\* , Wei Peng, Minwoo Choi , Sunghoon Im †. "Self-supervised Monocular Depth Estimation Robust to Reflective Surface Leveraged by Triplet Mining". *International Conference on Learning Representations ( ICLR ), 2025*.

**2024**

- Jongmin Gim\* , Jihun Park\* , Kyoungmin Lee\* , Sunghoon Im †. "Content-Adaptive Style Transfer: A Training-Free Approach with VQ Autoencoders". *Asian Conference on Computer Vision ( ACCV ), 2024 · DOI 10.1007/978-981-96-0917-8_11*.
- Jaeyeul Kim\* , Jungwan Woo\* , Jeonghoon Kim , Sunghoon Im †. "Rethinking LiDAR Domain Generalization: Single Source as Multiple Density Domains". *European Conference on Computer Vision ( ECCV ), 2024 · DOI 10.1007/978-3-031-72661-3_18*.
- EungGu Kang, Byeonghun Lee, Sunghoon Im † , Kyong Hwan Jin †. "BurstM: Deep Burst Multi-scale SR using Fourier Space with Optical Flow". *European Conference on Computer Vision ( ECCV ), 2024 · DOI 10.1007/978-3-031-72946-1_26*.
- Jaeyeul Kim\* , Jungwan Woo\* , Ukcheol Shin, Jean Oh, Sunghoon Im †. "Density-aware Domain Generalization for LiDAR Semantic Segmentation". *IEEE/RSJ International Conference on Intelligent Robots and Systems ( IROS ), 2024 · DOI 10.1109/iros58592.2024.10801829*.
- Woo Kyoung Han, Sunghoon Im , Jaedeok Kim, Kyong Hwan Jin †. "JDEC: JPEG Decoding via Enhanced Continuous Cosine Coefficients". *IEEE Conference on Computer Vision and Pattern Recognition ( CVPR ), 2024 · DOI 10.1109/cvpr52733.2024.00269*.
- Wonhyeok Choi\* , Mingyu Shin\* , Hyukzae Lee, Jaehoon Cho, Jaehyeon Park, Sunghoon Im †. "Multi-task Learning for Real-time Autonomous Driving Leveraging Task-adaptive Attention Generator". *IEEE International Conference on Robotics and Automation ( ICRA ), 2024 · DOI 10.1109/icra57147.2024.10610716*.
- Jinwoo Bae, Kyumin Hwang, Sunghoon Im †. "A Study on the Generality of Neural Network Structures for Monocular Depth Estimation". *IEEE Transactions on Pattern Analysis and Machine Intelligence ( TPAMI ), 게재 승인 · DOI 10.1109/tpami.2023.3332407*.
- Minsu Kim, Jaewon Lee, Byeonghun Lee, Sunghoon Im , Kyeonghwan Jin †. "Implicit Neural Image Stitching With Enhanced and Blended Feature Reconstruction". *IEEE/CVF Winter Conference on Applications of Computer Vision ( WACV ), 2024 · DOI 10.1109/wacv57701.2024.00404*.
- Hojin Kim, Seunghun Lee, Hyeon Kang, Sunghoon Im †. "Offline-to-Online Knowledge Distillation for Video Instance Segmentation". *IEEE/CVF Winter Conference on Applications of Computer Vision ( WACV ), 2024 ( Oral ) · DOI 10.1109/wacv57701.2024.00023*.

**2023**

- Wonhyeok Choi\*, Mingyu Shin\*, Sunghoon Im †. "Depth-discriminative Metric Learning for Monocular 3D Object Detection". *Neural Information Processing Systems ( NeurIPS ), 2023 · DOI 10.52202/075280-3512*.
- Changjae Kim , Seunghun Lee , Sunghoon Im †. "Multi-Target Domain Adaptation with Class-Wise Attribute Transfer in Semantic Segmentation". *The 34th British Machine Vision Conference ( BMVC ), 2023*.
- Sungho Moon , Jinwoo Bae , Sunghoon Im †. "Rotation Matters: Generalized Monocular 3D Object Detection for Various Camera System". *IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops ( CVPRw ), 2023*.
- Wonhyeok Choi , Sunghoon Im †. "Dynamic Neural Network for Multi-Task Learning Searching across Diverse Network Topologies". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2023 · DOI 10.1109/cvpr52729.2023.00368*.
- Jinwoo Bae , Sungho Moon , Sunghoon Im †. "Deep Digging into the Generalization of Self-supervised Monocular Depth Estimation". *Association for the Advancement of Artificial Intelligence ( AAAI ), 2023 · DOI 10.1609/aaai.v37i1.25090*.

**2022**

- Jungwan Woo \*, Jaeyeul Kim \*, Sunghoon Im †. "LiDAR 3D Object Detection via Self-Training and Knowledge Distillation". *ECCV workshop on 3D Perception for Autonomous Driving ( ECCVw ), Oct 2022*.
- Jeonghoon Kim , Sunghoon Im , Sunghyun Cho †. "ProFeat: Unsupervised Image Clustering via Progressive Feature Refinement". *Pattern Recognition Letters ( PRL ), 2022 · DOI 10.1016/j.patrec.2022.10.029*.
- Seunghun Lee , Wonhyeok Choi , Changjae Kim , Minwoo Choi , Sunghoon Im †. "ADAS: A Direct Adaptation Strategy for Multi-Target Domain Adaptive Semantic Segmentation". *IEEE Conference on Computer Vision and Pattern Recognition ( CVPR ), 2022 · DOI 10.1109/cvpr52688.2022.01860*.
- Hae-Gon Jeon, Sunghoon Im , Jaesung Choe, Minjun Kang, Joon-Young Lee, Martial Hebert. "CMSNet: Deep Color and Monochrome Stereo". *International Journal of Computer Vision ( IJCV ), Jan 2022 · DOI 10.1007/s11263-021-01565-6*.
- Minjun Kang, Jaesung Choe, Hyowon Ha, Hae-Gon Jeon, Sunghoon Im , In So Kweon and Kuk-Jin Yoon. "Facial Depth and Normal Estimation using Single Dual-Pixel Camera". *European Conference on Computer Vision ( ECCV ), Oct 2022 · DOI 10.1007/978-3-031-20074-8_11*.
- Jaeyeul Kim\*, Jungwan Woo\*, Sunghoon Im †. "RVMOS: Range-View Moving Object Segmentation Leveraged by Semantic and Motion Features". *IEEE Robotics and Automation Letters ( RAL ), 2022 · DOI 10.1109/lra.2022.3186080*.
- Seokju Lee, Francois Rameau, Sunghoon Im , In So Kweon. "Self-supervised Monocular Depth and Motion Learning in Dynamic Scenes: Semantic Prior to Rescue". *International Journal of Computer Vision ( IJCV ), 2022 · DOI 10.1007/s11263-022-01641-5*.

**2021**

- Dahoon Park, Kon-Woo Kwon, Sunghoon Im , Jaeha Kung †. "ZeBRA: Precisely Destroying Neural Networks with Zero-Data Based Repeated Bit Flip Attack". *British Machine Vision Conference ( BMVC ), 2021 · DOI 10.5244/c.35.184*.
- Jaesung Choe, Sunghoon Im , François Rameau, Minjun Kang, In So Kweon. "VolumeFusion: Deep Depth Fusion for 3D Scene Reconstruction". *IEEE International Conference on Computer Vision ( ICCV ), 2021 · DOI 10.1109/iccv48922.2021.01578*.

## 과제와 연구비

연구실이 게시한 과제 가운데 수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 47건이다. 임성훈 교수의 2026년 7월 KAIST 부임 전 시작하거나 끝난 DGIST 시기 과제도 포함한다. 지원 기관·사업·수행 기간·분야는 누리집 표기다.[^projects][^prof]

- LiDAR 기반 계측 알고리즘 성능 향상 기술 개발 (지원: 산학과제 – HD한국조선해양; 기간 2026.07.01-2026.12.31; 분야 3D reconstruction / Registration)
- 5D AI 로보틱스 연구단 (지원: 과학기술정보통신부, InnoCORE연구단; 기간 2026.05.01-2030.12.31; 분야 Physical AI)
- 피지컬 AI 기반 고정밀 손기술 창작 및 서비스 기술 개발 (지원: Kocca – 문화콘텐츠 IP 기획·창작 기술개발; 기간 2026.04.01-2028.12.31; 분야 Robotics, Physical AI)
- Living 3D Space: 실시간 현실 동기화 기반 자율진화형 공간지능 인프라 플랫폼 (지원: KEIT – 미래 판기술 프로젝트; 기간 2026.04.01-2033.12.31; 분야 Physical AI)
- 물리적 암묵 상식을 이해하는 협동 로봇의 적응형 정책 학습 기술 개발 (지원: NRF – 기초연구사업 핵심연구(유형C); 기간 2026.03.01-2029.02.28; 분야 Robotics, Physical AI)
- 물리적 암묵 상식을 이해하는 적응형 정책 학습 연구용 정교한 조작 협동 로봇 플랫폼 구축 (지원: NRF – 신진연구자인프라지원사업; 기간 2026.03.01-2027.02.28; 분야 Robotics, Physical AI)
- 인류 확장 로보틱스 연구소 (지원: NRF – 글로컬랩; 기간 2025.09.01-2034.08.31; 분야 Physical AI)
- Physical AI 분야의 거대 생성모델 기술 선도를 위한 LG AI STAR 인재양성 사업 (지원: 과학기술정보통신부 – 생성AI선도인재양성; 기간 2025.07.01-2028.12.31; 분야 Physical AI / Generative AI / Multi-modal AI)
- 초 거대 언어 모델 혁신 연구단 (지원: 과학기술정보통신부, InnoCORE연구단; 기간 2025.06.01-2029.12.31; 분야 LLM, Multi-Modal AI)
- AI스타펠로우십지원사업(DGIST) (지원: IITP – AI스타펠로우십지원사업; 기간 2025.04.01-2030.12.31; 분야 Physical AI)
- 자율행동체의 이동 임무 수행을 위한 온디바이스 VLM 및 실시간 이동 지능 기술 개발 (지원: IITP – 자율행동체 온디바이스; 기간 2025.04.01-2029.12.31; 분야 Robotics, Physical AI)
- 비학습 공간에서의 동적 환경 이해를 위한 시각언어모델(VLM) 기반 시각정보 활용 내비게이션 기술 개발 (지원: KETI – 기계로봇장비분야 산업기술개발사업; 기간 2024.07.01-2027.12.31; 분야 Multi-modal AI / Navigation)
- 대규모 언어모델(LLM) 및 3D 포인트 클라우드 기반 AI 데이터 융합 혁신기술 개발 (지원: 정보통신산업진흥원 – 혁신거점 인공지능 데이터 융합과제; 기간 2024.07.01-2026.12.31; 분야 Generative AI / Multi-modal AI)
- 지능형 전장 인식/판단에 활용되는 다중센서 기반 3차원 전장정보 구축 및 분석 기술 연구 (지원: KRIT – 방산혁신기업100 전용R&D 지원사업; 기간 2023.12.20~2028.12.19; 분야 3D reconstruction)
- 물리 법칙을 따르는 추론 과정(Chain-Of-Thought) 기반 비디오 생성 모델 (지원: 엔비디아 – 학술연구 지원사업; 기간 2026.01.01-2026.06.30; 분야 Generation Models, Physical AI)
- 바이오체화형 피지컬AI연구단 (지원: 과학기술정보통신부, InnoCORE연구단; 기간 2025.06.01-2026.04.30; 분야 Physical AI)
- 환경변화에 강인한 다중카메라기반 다중 시각인지 작업 학습 연구 (지원: 과학기술정보통신부 – 신진연구자사업, 우수신진연구; 기간 2023.03.01-2026.02.28; 분야 Scene understanding / Generalization / Autonomous Driving)
- 고난이도 AX 연구지원 플랫폼 구축사업 (지원: 과학기술정보통신부 – 고난이도 AX 연구지원 플랫폼 구축사업; 기간 2025.09.01-2025.12.31; 분야 Physical AI)
- 입체적 시야각 분석을 통한 산불 발화 위치 추정 및 동적 확산 예측 시스템 구축 (지원: 과학기술정보통신부 – 산학 R&BD협업 프로젝트; 기간 2025.05.01-2025.12.31; 분야 3D reconstruction, Scene Understanding)
- 드론기반 선체 블록 계측 자동화 기술 개발 (지원: 산학과제 – (주)한국조선해양; 기간 2025.1.1-2025.12.31; 분야 3D reconstruction)
- 사고의 연쇄를 활용한 물리 법칙 준수 비디오 생성 모델 연구 (지원: 과학기술정보통신부 – HRHR; 기간 2025.07.01-2025.12.31; 분야 Generative AI / Multimodal AI)
- 실시간 카메라 기반 지속가능한 Detection 소프트웨어 개발 (지원: 산학과제 – (주)기**자; 기간 2025.03.01-2025.08.31; 분야 Scene understanding)
- 보안 및 안전분야 객체 탐지 인공지능 모델 개발 및 강건성 향상을 위한 연구 (지원: 산학과제 – **스페이스; 기간 2025.04.01-2025.06.30; 분야 General AI / Scene understanding)
- 멀티 카메라 기반 깊이 추정 기술 개발 (지원: 산학과제 – 현대NGV (현대자동차); 기간 2024.06.10-2025.06.09; 분야 3D reconstruction / Generalization / Autonomous Driving)
- 인공지능 객체 인식 기반의 물류 산업용 비전 피킹 시스템 개발 (지원: 대구디지털혁신진흥원 – 산학 R&BD협업 상용화 과제; 기간 2023.07.01-2024.12.31; 분야 Scene understanding / 3D Localization / Generalization)
- 정제약품 3차원 자세 추정 및 형상 복원 프로그램 시작품 제작 (지원: 과학기술정보통신부 – ETRI; 기간 2024.10.14-2024.11.30; 분야 3D Perception / 3D Reconstruction)
- 스테레오 카메라의 이미지 처리 자동화를 위한 알고리즘 개발 (지원: 산학과제 – HD한국조선해양; 기간 2024.04.01-2024.09.30; 분야 3D reconstruction / Localization)
- 다중카메라 기반 Depth 생성 소프트웨어 개발 (지원: 산학과제 – (주)기**자; 기간 2024.01.15~2024.07.14; 분야 3D reconstruction)
- 딥러닝 및 파운데이션 모델 기반 CCTV 이벤트 검지 모듈 개발 및 성능 비교 분석 (지원: 과학기술정보통신부 – ETRI; 기간 2023.11.01~2024.02.28; 분야 Scene understanding)
- 메타버스 스트리밍 서비스를 위한 객체 식별 SW 개발 (지원: 과학기술정보통신부 – KETI; 기간 2023.09.19~2023.12.31; 분야 Scene understanding)
- 비디오 입력 요소 영상에서의 시간축 일관성 유지 객체 분리 알고리즘 성능 테스트를 위한 GUI모듈 개발 (지원: 과학기술정보통신부 – ETRI; 기간 2023.05.09-2023.11.30; 분야 Scene understanding / Generalization)
- 영상 분석 및 영상 검색 기술 연구 (지원: 산학과제 – (주)일만백만; 기간 2023.02.01-2023.07.31; 분야 Scene understanding / Data hungry / Multi-modal)
- 멀티 태스킹 러닝 기반 네트워크 선행연구 (지원: 산학과제 – 현대NGV (현대자동차); 기간 2022.11.07-2023.11.06; 분야 Scene understanding / Generalization / Autonomous Driving)
- 실시간 대규모 영상 데이터 이해·예측을 위한 고성능 비주얼 디스커버리 플랫폼 개발 (지원: 과학기술정보통신부 – 정보통신기획평가원(IITP); 기간 2021.03.01-2023.12.31; 분야 Scene understanding)
- 신경망 및 스테레오 매칭 기반 깊이영상 획득방안 연구 (지원: 과학기술정보통신부 – ETRI; 기간 2021.03.01-2023.12.31; 분야 3D reconstruction / View synthesis / AR/VR)
- 5G 엣지클라우드 기반 VR·AR 저지연 스트리밍 기술 개발 (지원: IITP 정보통신.방송 기술개발사업; 기간 2020.04.01-2023.12.31; 분야 3D reconstruction / View synthesis / AR/VR)
- 다분광 스테레오 기반 동적 상황 인지 기술 (지원: 과학기술정보통신부 신진연구자사업, 신진연구; 기간 2020.03.01-2023.02.28 (종료); 분야 Scene understanding / Data hungry / Autonomous Driving)
- 협력적 AI 기반의 고신뢰 원격 자율주행 클라우드 모빌리티 서비스 시스템 (지원: 과학기술정보통신부 DGIST일반사업, P-COE; 기간 2020.05.01-2022.12.31 (종료); 분야 Scene understanding / Generalization / Autonomous Driving)
- 다중시점 항공 영상을 이용한 3차원 복원 연구 (지원: 산학과제 – (주)다비오; 기간 2022.02.01-2022.12.31; 분야 3D reconstruction / View synthesis / AR/VR)
- 자율주행용 라이다를 대체할 수 있는 멀티카메라기반 3D 주행환경 인식 기술 개발 (지원: 중소벤처기업부 – 중소기업기술정보진흥원; 기간 2022.05.01-2022.12.31; 분야 3D reconstruction / Generalization / Autonomous Driving)
- 도로 객체 위치 및 속도 추정 모듈 개발 (지원: 과학기술정보통신부 – ETRI; 기간 2022.09.13-2022.11.30 (종료); 분야 Scene understanding)
- 이종 광학계 캘리브레이션 파라메터 계산 모듈 및 테스트 GUI 개발 (지원: 과학기술정보통신부 – ETRI; 기간 2022.05.26-2022.11.30 (종료); 분야 3D reconstruction / Camera calibration)
- 투명 용기 3D bin-picking을 위한 3D 로봇 비전 프로그램 시제품 제작 (지원: 과학기술정보통신부 – ETRI; 기간 2022.04.28-2022.11.30 (종료); 분야 3D reconstruction / 3D Perception)
- 딥러닝 기반 지리 데이터 구축 시스템 고도화 및 다중 객체 추적 요소 기술 개발 (지원: 산학과제 – (주)다비오; 기간 2021.07.01-2021.12.31 (종료); 분야 Scene understanding / Data hungry)
- Domain Adaptation기반 객체 검출을 위한 데이터셋 관리 및 성능평가 GUI 개발 (지원: 과학기술정보통신부 – ETRI; 기간 2021.06.28-2021.11.30 (종료); 분야 Scene understanding / Generalization)
- 도메인 적응 기법을 활용한 가상 학습 데이터 생성 시스템 개발 (지원: 과학기술정보통신부 – ETRI; 기간 2021.06.21-2021.11.30 (종료); 분야 Scene understanding / Generalization / Autonomous Driving)
- 다시점 카메라 적용 비지도 3D 객체 검출 보정시스템 개발 (지원: 산학과제 – 현대NGV (현대자동차); 기간 2021.04.15-2022.04.14 (종료); 분야 Scene understanding / Generalization / Autonomous Driving)

## 수상과 선정

2021년 10월 13일–2026년 10월 13일에 게시된 수상·선정 23항목이다. 임성훈 교수의 2026년 7월 KAIST 부임 전 DGIST 시기 성과가 포함된다. 날짜는 소식의 게시일이며, 한 게시 글에 여러 수상자가 함께 적힌 경우 한 항목으로 옮겼다.[^news][^prof]

- 2026-02-12 · 박지훈·이경민·김종민·조현서가 제32회 삼성휴먼테크논문대상 Computer Science and Engineering 분과 장려상(Encouragement Prize)을 받았다.
- 2025-11-03 · 박지훈이 DGIST EECS & AI Student Conference 2025 구두 발표 부문 Best Presentation Award를 받았다.
- 2025-09-16 · 문성호·이승훈·전효경이 ICCV 2025 RetailVision 워크숍 GroceryVision Challenge의 Track 1 TAL·STAL 부문에서 우승했다.
- 2025-08-28 · 임성훈 교수가 한국이공학진흥원 산학공동연구교수상을, 김재열이 차세대 공학연구자 최우수상을 받았다.
- 2025-05-19 · 임성훈 교수가 CVPR 2025 Outstanding Reviewer로 선정되었다.
- 2025-02-07 · 김재열·우정완·김정훈·임성훈 교수가 제37회 영상처리 및 이해 워크숍 논문 발표 동상을 받았다.
- 2025-01-02 · 임성훈 교수가 2024년도 DGIST Visionary Award 연구혁신상을 받았다.
- 2024-11-19 · 최원혁·황규민·최민우가 제16회 전자신문 ICT논문 공모대제전 최우수상을 받았다.
- 2024-10-17 · 임성훈 교수가 대한전자공학회 인공지능신호처리소사이어티 우수신진연구자상을 받았다.
- 2024-09-30 · 최원준 소속 팀이 2024 춘천 AWS 딥레이서 챔피언십 대상을 받았다.
- 2024-06-14 · 임성훈 교수가 CVPR 2024 Outstanding Reviewer로 선정되었다.
- 2024-06-14 · 신민규가 CVPR 2024 자율주행 워크숍 Argoverse Challenge의 4D Occupancy Forecasting 부문 2위를 차지했다.
- 2024-06-14 · 김재열·우정완이 CVPR 2024 자율주행 워크숍 Argoverse Challenge의 LiDAR Scene Flow 부문 1위를 차지했다.
- 2024-01-29 · 제30회 삼성휴먼테크논문대상 Signal Processing 분과에서 최원혁·신민규가 동상을, 박지훈·김종민·이경민·이승훈이 장려상을 받았다.
- 2023-12-12 · 최원혁·신민규가 제15회 전자신문 ICT논문 공모대제전 우수상을 받았다.
- 2023-10-30 · 우정완·김정훈·김재열·최원혁·신민규가 국토교통부 자율주행 인공지능 알고리즘 개발 챌린지 2023 최우수상을 받았다.
- 2023-06-27 · 연구팀이 CVPR 2023 자율주행 워크숍에서 Honorable Mention(입선)을 받았다. 게시 설명에는 챌린지 2위로 적혀 있다.
- 2023-02-17 · 우정완·김재열의 LiDAR 3차원 물체 검출 도메인 적응 연구가 제18회 한국로봇종합학술대회 AFCV Best Robot Vision Paper Award를 받았다.
- 2022-11-15 · 우정완·김재열·김정훈이 국토교통부 자율주행 인공지능 알고리즘 개발 챌린지 2022 우수상을 받았다.
- 2022-10-24 · 연구팀이 ECCV 2022 워크숍 LiDAR 자기지도학습 챌린지에서 3위를 차지했다.
- 2022-02-16 · 이승훈·최원혁·김창재·최민우가 제28회 삼성휴먼테크논문대상 Signal Processing 분과 장려상을 받았다.
- 2022-01-20 · 배진우·최민우가 한국 도시 3차원 영상 데이터 인공지능 학습용 데이터 해커톤 우수상을 받았다.
- 2021-12-21 · 이승훈이 제13회 ICT논문 공모 대제전 우수상을 받았다.

## 소식

2021년 10월 13일–2026년 10월 13일의 논문 채택·게재 승인, 연구비 지원, 연구 결과 전시 소식 42건이다. 임성훈 교수의 2026년 7월 KAIST 부임 전 DGIST 시기 소식도 포함한다. 날짜는 게시일이고, 학술지의 게재 승인과 학회의 채택을 구별해 적었다.[^news][^prof]

- 2026-09-25 · H-GenPO 논문이 NeurIPS 2026에 채택되었다.
- 2026-07-20 · CRAFT 논문이 SIGGRAPH Asia 2026에 채택되었다.
- 2026-07-04 · ReAL 논문이 ECCV 2026에 채택되었다.
- 2026-05-20 · Learning to Forget 논문이 KDD 2026에 채택되었다.
- 2026-03-17 · 한국연구재단 핵심연구 유형 C 과제로 협동 로봇의 물리적 암묵 상식 이해를 위한 적응형 정책 학습 연구가 선정되었다.
- 2026-03-09 · 신진연구자 인프라 지원사업에 선정되어 휴머노이드 로봇을 도입할 계획을 알렸다.
- 2026-03-09 · NVIDIA Academic Grant에 물리 법칙을 따르는 추론 과정 기반 비디오 생성 모델 과제가 선정되어 GPU 서버 사용을 지원받는다고 알렸다.
- 2026-02-23 · NVIDIA Academic Grant로 물리 법칙을 따르는 비디오 생성 모델 연구를 위한 계산 자원을 지원받는다고 알렸다.
- 2026-02-23 · 인공지능으로 신윤복의 미인도를 서양 화가의 화풍으로 재해석한 작품을 대구간송미술관에서 전시한다고 알렸다.
- 2026-02-23 · CVPR 2026 및 Findings에 논문 다섯 편이 채택되었다.
- 2025-11-21 · 박지훈·김종민·이경민이 제작한 인공지능 작품을 DGIST 도서관 갤러리에서 전시한다고 알렸다.
- 2025-11-10 · Scale-invariant and View-relational Representation Learning for Full Surround Monocular Depth 논문이 RA-L에 게재 승인되었다.
- 2025-11-08 · Infinite-Story 논문이 AAAI 2026에 구두 발표로 채택되었다.
- 2025-09-16 · ICCV 워크숍에 논문 세 편이 채택되었다.
- 2025-09-10 · 교육부 글로컬랩 사업으로 인류 확장 로보틱스 연구가 지원받는다고 알렸다.
- 2025-07-31 · 과학기술정보통신부의 LG AI 연구그룹 지원으로 피지컬 인공지능 응용을 위한 대규모 생성 모델 연구를 수행한다고 알렸다.
- 2025-06-26 · CAVIS, Latest Object Memory Management for Temporally Consistent Video Instance Segmentation, JPEG Processing Neural Operator for Backward-Compatible Coding 논문이 ICCV 2025에 채택되었다.
- 2025-06-10 · 과학기술정보통신부 AI Star Fellowship으로 인간 중심 공생형 체화 인공지능 시스템 연구가 지원받는다고 알렸다.
- 2025-06-10 · 과학기술정보통신부 InnoCORE 연구단에서 대규모 언어 모델의 추론·분야 특화·다중 자료 확장·신뢰성 연구를 지원받는다고 알렸다.
- 2025-02-27 · Style-Editor와 Towards Lossless Implicit Neural Representation via Bit Plane Decomposition 논문이 CVPR 2025에 채택되었다.
- 2025-01-27 · Flow4D 논문이 RA-L에 게재 승인되었다.
- 2025-01-23 · Self-supervised Monocular Depth Estimation Robust to Reflective Surface Leveraged by Triplet Mining 논문이 ICLR 2025에 채택되었다.
- 2024-12-10 · Intrinsic Image Decomposition for Robust Self-supervised Monocular Depth Estimation on Reflective Surfaces 논문이 AAAI 2025에 채택되었다.
- 2024-09-20 · Content-Adaptive Style Transfer 논문이 ACCV 2024에 채택되었다.
- 2024-07-02 · Density-aware Domain Generalization for LiDAR Semantic Segmentation 논문이 IROS 2024에 채택되었다.
- 2024-07-02 · Rethinking LiDAR Domain Generalization과 BurstM 논문이 ECCV 2024에 채택되었다.
- 2024-02-28 · JDEC 논문이 CVPR 2024에 채택되었다.
- 2024-01-29 · Multi-task Learning for Real-time Autonomous Driving Leveraging Task-adaptive Attention Generator 논문이 ICRA 2024에 채택되었다.
- 2023-11-04 · A Study on the Generality of Neural Network Structures for Monocular Depth Estimation 논문이 TPAMI에 게재 승인되었다.
- 2023-10-24 · Implicit Neural Image Stitching과 Offline-to-Online Knowledge Distillation for Video Instance Segmentation 논문이 WACV 2024에 채택되었다.
- 2023-09-22 · Depth-discriminative Metric Learning for Monocular 3D Object Detection 논문이 NeurIPS 2023에 채택되었다.
- 2023-08-22 · Multi-Target Domain Adaptation with Class-Wise Attribute Transfer in Semantic Segmentation 논문이 BMVC 2023에 채택되었다.
- 2023-05-22 · Rotation Matters 논문이 CVPR 워크숍 2023에 채택되었다.
- 2023-02-28 · Dynamic Neural Network for Multi-Task Learning Searching across Diverse Network Topologies 논문이 CVPR 2023에 채택되었다.
- 2022-11-20 · Deep Digging into the Generalization of Self-supervised Monocular Depth Estimation 논문이 AAAI 2023에 채택되었다.
- 2022-11-01 · ProFeat 논문이 Pattern Recognition Letters에 게재 승인되었다.
- 2022-07-04 · Facial Depth and Normal Estimation using Single Dual-Pixel Camera 논문이 ECCV 2022에 채택되었다.
- 2022-06-15 · RVMOS 논문이 RA-L에 게재 승인되고 IROS 2022에서 발표될 예정임을 알렸다.
- 2022-05-31 · Self-supervised Monocular Depth and Motion Learning in Dynamic Scenes 논문이 IJCV에 게재 승인되었다.
- 2022-03-02 · ADAS 논문이 CVPR 2022에 채택되었다.
- 2021-11-27 · CMSNet 논문이 IJCV에 게재 승인되었다.
- 2021-10-18 · ZeBRA 논문이 BMVC 2021에 채택되었다.

## 연락과 위치

- 연구실 이메일: rvlab@kaist.ac.kr.[^contact]
- 위치: KAIST N5, 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Korea.[^contact]
[^home]: KAIST Robotics and Vision Lab, Home의 Welcome. <https://rv.kaist.ac.kr/> (관측일 2026-11-07).
[^dept]: KAIST 문화기술대학원, 교수 목록의 임성훈 부교수 항목. <https://ct.kaist.ac.kr/boards/lists/faculty_board> (관측일 2026-11-07).
[^prof]: Sunghoon Im, About·Research Interests·Experience·Education. <https://rv.kaist.ac.kr/professor/index.html> (관측일 2026-11-07).
[^members]: KAIST Robotics and Vision Lab, Members의 과정별 명단. <https://rv.kaist.ac.kr/members.html> (관측일 2026-11-07).
[^groups]: KAIST Robotics and Vision Lab, Members by Research Group. <https://rv.kaist.ac.kr/members-research.html> (관측일 2026-11-07).
[^alumni]: KAIST Robotics and Vision Lab, Alumni. <https://rv.kaist.ac.kr/members-alumni.html> (관측일 2026-11-07).
[^member-details]: KAIST Robotics and Vision Lab, Jeonghoon Kim·Minwoo Choi·Hyeon Kang·Sungmin Ha·Yohan Lim·Junwoo Park의 연구 관심·학력. <https://rv.kaist.ac.kr/member-jeonghoon-kim.html>, <https://rv.kaist.ac.kr/member-minwoo-choi.html>, <https://rv.kaist.ac.kr/member-hyeon-kang.html>, <https://rv.kaist.ac.kr/member-sungmin-ha.html>, <https://rv.kaist.ac.kr/member-yohan-lim.html>, <https://rv.kaist.ac.kr/member-junwoo-park.html> (관측일 2026-11-07).
[^member-supp]: KAIST Robotics and Vision Lab, Jiwon Jang·Yujin Han·Minjae Kim·Siwon Kim·Jinhwoi Kim·Haeun Yun·Donghyeon Kim·Jaekeun Lee의 과정·연구 관심·학력. <https://rv.kaist.ac.kr/member-jiwon-jang.html>, <https://rv.kaist.ac.kr/member-yujin-han.html>, <https://rv.kaist.ac.kr/member-minjae-kim.html>, <https://rv.kaist.ac.kr/member-siwon-kim.html>, <https://rv.kaist.ac.kr/member-jinhwoi-kim.html>, <https://rv.kaist.ac.kr/member-haeun-yun.html>, <https://rv.kaist.ac.kr/member-donghyeon-kim.html>, <https://rv.kaist.ac.kr/member-jaekeun-lee.html> (관측일 2026-11-07).
[^pubs]: KAIST Robotics and Vision Lab, Publications의 연도별 논문 목록. <https://rv.kaist.ac.kr/publications.html> (관측일 2026-11-07).
[^projects]: KAIST Robotics and Vision Lab, Projects의 On-going projects·Completed projects. <https://rv.kaist.ac.kr/projects.html> (관측일 2026-11-07).
[^news]: KAIST Robotics and Vision Lab, News의 게시일·제목·설명. <https://rv.kaist.ac.kr/news.html> (관측일 2026-11-07).
[^contact]: KAIST Robotics and Vision Lab, Contact의 Research Areas·Email·Location. <https://rv.kaist.ac.kr/contact.html> (관측일 2026-11-07).

[^p1]: W. Kim, W. Choi, S. Im, arXiv 사전 공개본 (온라인 2026-09-16). <https://doi.org/10.48550/arXiv.2609.18213> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/html/2609.18213v1> (관측일 2026-11-07).
[^p2]: S. Moon 외, S. Im, arXiv 사전 공개본 (온라인 2026-09-28). <https://doi.org/10.48550/arXiv.2609.34853> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/html/2609.34853v1> (관측일 2026-11-07).
[^p3]: K. Shimomura 외, H. Fujiyoshi, arXiv 사전 공개본 (온라인 2026-10-08). <https://doi.org/10.48550/arXiv.2610.11572> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/html/2610.11572v1> (관측일 2026-11-07).
[^p4]: J. Park 외, S. Im, arXiv 사전 공개본 (온라인 2026-08-14). <https://doi.org/10.48550/arXiv.2608.14403> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/html/2608.14403v1> (관측일 2026-11-07).
[^p5]: S. Lee 외, G. Lee, arXiv 사전 공개본 (온라인 2026-10-02). <https://doi.org/10.48550/arXiv.2610.14039> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/html/2610.14039v1> (관측일 2026-11-07).

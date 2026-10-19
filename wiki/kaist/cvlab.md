# 컴퓨터 비전 연구실 (CVLAB, Computer Vision Lab.)

**KAIST 김재철AI대학원 · 김승룡 교수**

- 분야: 3차원·4차원 컴퓨터 비전, 영상 생성과 월드 모델, 멀티모달(이미지·영상·언어) 모델, 데이터 효율 학습
- 홈페이지: <https://cvlab.kaist.ac.kr/>
- 근거와 출처: [CVLAB 근거 페이지](cvlab-sources.md)

> 컴퓨터가 사진과 영상을 보고 3차원 공간을 복원하고, 움직임을 이해하고, 새로운 영상을 만들어 내게 하는 인공지능을 연구한다. 몇 장의 사진만으로 3차원 장면을 재구성하는 모델, 1분 넘는 영상을 실시간으로 이어 만드는 기법, 여러 사람이 함께 움직이는 장면을 예측하는 월드 모델이 대표 성과다.[^home][^faculty][^p1][^p2][^p3]

## 무엇을 연구하나

컴퓨터 비전은 카메라로 들어온 이미지·영상을 컴퓨터가 이해하게 하는 분야다. 이 연구실은 컴퓨터 비전, 여러 종류의 데이터를 함께 다루는 멀티모달 학습, 시각 컴퓨팅을 연구하며 자율주행, 지능형 감시, 휴머노이드 로봇, AR/VR, 메타버스, 헬스케어를 응용 분야로 든다.[^home] 최근 관심은 3·4차원 컴퓨터 비전, 영상 월드 모델, 멀티모달 모델, 적은 데이터로 배우는 자기지도 표현 학습이다.[^home]

첫 번째 갈래는 **3차원 장면 복원**이다. 카메라 위치를 모르는 사진 몇 장만으로 3차원 장면을 한 번에 복원하는 모델(피드포워드 모델, 장면마다 따로 최적화하지 않고 신경망을 한 번 통과시켜 결과를 내는 방식)에서, 장면을 작은 입체 점(가우시안) 2,000개 정도로 압축해 표현해도 고품질 복원과 장면 이해가 가능함을 보였다.[^p3] 화질이 떨어진(열화된) 실제 사진에서도 3차원 형상을 정확히 복원하는 방법도 내놓았다.[^p4]

두 번째 갈래는 **영상 생성과 월드 모델**이다. 월드 모델은 어떤 행동을 했을 때 다음 장면이 어떻게 보일지 예측하는 모델이다. 연구실은 여러 행위자가 같은 공간에서 세밀한 동작으로 상호작용하는 장면을 각자의 1인칭 시점에서 동시에 만들어 내는 모델을 제안했고,[^p1] 짧은 영상으로 학습한 생성 모델이 추가 학습 없이 12배 넘게 긴(5초 학습으로 60초 이상) 영상을 실시간으로 이어 만들게 했다.[^p2] 영상 생성 모델이 내부에서 프레임 사이 대응 관계를 어떻게 잡는지도 분석했다.[^p5]

세 번째 갈래는 **멀티모달 모델**이다. 이미지와 글을 함께 다루는 대형 언어 모델(MLLM)이 물건 개수 세기나 공간 추론에 약한 이유를 시각 정보 손실로 보고 이를 보완했고,[^p6] 영상 속에서 "A가 B에게 던진다"처럼 상호작용하는 두 대상을 나눠 찾는 과제와 12만 7천 개 표현의 데이터셋을 만들었다.[^p7] 글로부터 이미지를 만드는 생성 모델의 출발 분포를 조건에 맞게 학습하는 방법도 연구한다.[^p8]

## 주요 연구 주제

### 1. 피드포워드 3차원 복원

카메라 정보 없이 적은 사진으로 3차원 장면을 한 번에 복원하고, 열화된 사진에서도 견고하게 만든다.[^p3][^p4] 대표 논문 3, 4.

### 2. 영상 생성과 월드 모델

다중 행위자 월드 모델, 긴 영상의 실시간 생성, 영상 확산 모델의 내부 분석.[^p1][^p2][^p5] 대표 논문 1, 2, 5.

### 3. 멀티모달 이해

멀티모달 언어 모델의 시각 정보 보존, 상호작용 인식 영상 분할.[^p6][^p7] 대표 논문 6, 7.

### 4. 생성 모델 학습 방법

텍스트–이미지 생성의 흐름 정합(flow matching) 개선.[^p8] 대표 논문 8.

## 대표 논문

최근 5년 논문 중 교수가 마지막 저자(연구 책임)인 것에서 주제별로 골랐다. 컴퓨터 비전 분야는 주로 학회에 발표한다. "쉽게 말하면" 칸은 각 논문의 초록(arXiv 판 또는 랩 프로젝트 페이지 게시본)만을 근거로 썼다.

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2026 | [Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction](https://cvlab-kaist.github.io/ME-World/) · 랩 게시(2026) | 여러 사람이 같은 공간에서 세밀한 손동작으로 상호작용하는 장면을 각자의 1인칭 시점 영상으로 동시에 생성하는 월드 모델(ME-World). 공간 일관성·행동 제어·인물 유지·영상 품질이 기존 방법보다 나았다.[^p1] | 1저자 Dahyun Chung, 책임 김승룡 |
| 2 | 2026 | [Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression](https://arxiv.org/abs/2512.05081) · ICML | 추가 학습 없이 영상 생성 모델의 기억(KV 캐시)을 관리하는 두 가지 방법으로, 5초 영상으로 학습한 모델이 60초 넘는 영상을 실시간으로 만들게 했다(12배 이상 확장).[^p2] | 1저자 Jung Yi, 책임 김승룡 |
| 3 | 2026 | [C3G: Learning Compact 3D Representations with 2K Gaussians](https://arxiv.org/abs/2512.04021) · CVPR | 카메라 위치를 모르는 사진 몇 장에서, 꼭 필요한 위치에만 3차원 가우시안을 두어 압축된 장면 표현을 만든다. 적은 표현으로도 새 시점 영상과 3차원 물체 분할이 잘 됐다.[^p3] | 공동 1저자 Honggyu An·Jaewoo Jung, 책임 김승룡 |
| 4 | 2026 | [GARD: Geometry-Aware Representation Denoising for Robust Multi-view 3D Reconstruction](https://arxiv.org/abs/2605.26230) · NeurIPS | 화질이 떨어진(열화된) 실제 사진에서도 3차원 복원이 잘 되도록, 3차원 복원 모델의 내부 특징 공간에서 확산 모델(잡음을 단계적으로 걷어 내며 데이터를 만드는 생성 모델)로 열화를 걷어 낸다. 형상과 깨끗한 이미지를 함께 복원한다.[^p4] | 공동 1저자 Jin Hyeon Kim·Jaeeun Lee, 책임 김승룡 |
| 5 | 2025 | [Emergent Temporal Correspondences from Video Diffusion Transformers](https://arxiv.org/abs/2506.17220) · NeurIPS | 영상 생성 모델(DiT)이 프레임 사이 대응을 어디서 잡는지 처음으로 정량 분석하는 틀(DiffTrack)을 만들고, 이를 학습 없는 점 추적과 움직임이 더 자연스러운 영상 생성에 썼다.[^p5] | 공동 1저자 Jisu Nam·Soowon Son, 책임 김승룡 |
| 6 | 2026 | [VIRAL: Visual Representation Alignment for Multimodal Large Language Models](https://arxiv.org/abs/2509.07979) · ICLR 워크숍 | 멀티모달 언어 모델이 학습 중 세밀한 시각 정보를 잃는 문제를, 내부 시각 표현을 사전학습된 시각 모델의 표현에 맞추는 간단한 규제로 줄여 여러 벤치마크에서 성능을 높였다.[^p6] | 공동 1저자 Heeji Yoon·Jaewoo Jung·Junwan Kim, 책임 김승룡 |
| 7 | 2026 | [InterRVOS: Interaction-aware Referring Video Object Segmentation](https://cvlab-kaist.github.io/InterRVOS/) · CVPR | 문장으로 지목한 영상 속 대상을 찾을 때 행위자와 상대 대상을 나눠 분할하는 새 과제와 평가 방식, 12만 7천 개 표현의 데이터셋(InterRVOS-127K)을 제안했다.[^p7] | 1저자 Woojeong Jin, 책임 김승룡 |
| 8 | 2026 | [Better Source, Better Flow: Learning Condition-Dependent Source Distribution for Flow Matching](https://arxiv.org/abs/2602.05951) · NeurIPS | 텍스트–이미지 생성의 흐름 정합 모델에서 출발점이 되는 분포를 조건(문장)에 맞게 학습하는 방법. 안정적으로 학습하는 조건을 밝히고 여러 벤치마크에서 꾸준히 개선했다.[^p8] | 공동 1저자 Junwan Kim·Jiho Park, 책임 김승룡 |

## 교수와 전문 분야

김승룡 교수는 연세대 전기전자공학과에서 학사(2012, 우등 졸업)와 박사(2018)를 받았다.[^faculty] 마이크로소프트 리서치 아시아 연구 인턴(2015–2016), 연세대 박사후연구원(2018–2019), 스위스 로잔공대(EPFL) 박사후연구원(2019–2020)을 거쳐 고려대 조교수·부교수(2020–2024)로 일했고, 2024년 8월 KAIST 김재철AI대학원 부교수로 옮겼다.[^faculty]

교수는 연구 관심을 컴퓨터 비전, 계산 사진학, 기계학습·딥러닝, 특히 표현 학습과 시각 장면의 복원·이해로 소개한다.[^faculty] 논문으로 보면 전문 분야는 세 갈래다.

- **3차원 비전과 시각 대응**: 사진 사이 대응점 찾기(시각 대응)와 피드포워드 3차원 복원.[^p3][^p4][^p5][^students]
- **생성 모델**: 영상 확산 모델, 월드 모델, 흐름 정합.[^p1][^p2][^p8]
- **멀티모달 학습**: 이미지·영상과 언어를 함께 다루는 모델.[^p6][^p7]

## 응용 분야

연구실은 자율주행, 지능형 감시, 휴머노이드 로봇, AR/VR, 메타버스, 헬스케어를 응용 분야로 든다.[^home] 대표 논문으로 보면 로봇·체화 AI용 월드 모델, 실시간 영상 생성, 3차원 재구성, 멀티모달 AI 어시스턴트에 닿아 있다.[^p1][^p2][^p3][^p6] 학생들은 메타·구글·어도비·소니·네이버 등에서 인턴을 했고,[^home] 졸업생은 삼성전자·LG전자·LG AI연구원·SK텔레콤·현대자동차와 해외 대학원(칼텍·UC 버클리·워싱턴대)으로 진출했다.[^students]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다. 연구 주제와 이메일은 랩 표기를 옮겼다(이메일은 게시된 사람만).[^students] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Yeji Choi | 박사후연구원 | Image Generation & Editing, Diffusion Models | yejichoi@kaist.ac.kr | 4 |
| Seok Yeong Lee | 박사후연구원 | 3D Reconstruction, 3D Detection, Image-based Rendering |  |  |
| WonJun Moon | 박사후연구원 | Video Understanding, Multi-modal Learning |  |  |
| Jongmin Lee | 박사후연구원 | 3D Reconstruction, Image Matching, Visual Localization |  |  |
| Seokju Cho | 석박사통합과정 | Visual Correspondence, Diffusion Models, NeRF | seokju.cho@kaist.ac.kr |  |
| Minseop Kwak | 석박사통합과정 | 3D Reconstruction, NeRF | minseop.kwak@kaist.ac.kr |  |
| Junyoung Seo | 석박사통합과정 | Diffusion Models, Visual Correspondence, Video/3D | junyoung.seo@kaist.ac.kr | 1 |
| Jisu Nam | 석박사통합과정 | Visual Correspondence, Diffusion Models | jisunam@kaist.ac.kr | 2, 5 |
| Wooseok Jang | 석박사통합과정 | Diffusion Models, Video/3D | jws1997@kaist.ac.kr | 2 |
| Heeseong Shin | 석박사통합과정 | Computer Vision, Image Segmentation | hsshin98@kaist.ac.kr | 6 |
| Jin Hyeon Kim | 박사과정 | Object Detection, 3D Vision, Explainable AI | msjchr@korea.ac.kr | 4 |
| Jaewoo Jung | 석박사통합과정 | 3D Vision | jaewoo.jung@kaist.ac.kr | 3, 6 |
| Sangbeom Lim | 석박사통합과정 | Multi-modal Video Segmentation | limsbeom@korea.ac.kr | 6 |
| Jini Yang | 박사과정 | Event-based Vision, Video Diffusion Models | jini.yang@kaist.ac.kr |  |
| Honggyu An | 석박사통합과정 | Depth estimation, 3D Vision | honggyu@kaist.ac.kr | 1, 3, 6 |
| Jisang Han | 석박사통합과정 | 3D Vision, Robotics | onground@kaist.ac.kr | 3, 6 |
| Jisoo Kim | 박사과정 | Video/Motion Generation, Robotics | jisookim@kaist.ac.kr |  |
| Siyoon Jin | 석박사통합과정 | Diffusion Models, Video Models | siyun515@kaist.ac.kr | 1, 5 |
| Soowon Son | 석박사통합과정 | Visual Correspondence, Video Diffusion Models | soowon.son@kaist.ac.kr | 5 |
| Heeji Yoon | 석박사통합과정 | Segmentation, MLLM | hjyoon@kaist.ac.kr | 2, 6 |
| Woojeong Jin | 박사과정 | Video Understanding, Multimodal Large Language Models | wooj0216@kaist.ac.kr | 7 |
| Seongchan Kim | 석박사통합과정 | NeRF, Video, Multimodal | star._.overflow@kaist.ac.kr | 7 |
| Gyuseong Lee | 박사과정 | Video Generation/Understanding, Action Prediction | gyuseong.lee@kaist.ac.kr |  |
| SoHee Kim | 박사과정 | VLA, IL, Robotics | soheekim@kaist.ac.kr |  |
| Hyogun Lee | 박사과정 | Video understanding, Video-text retrieval | hyogun@kaist.ac.kr |  |
| Jaewon Min | 석박사통합과정 | Diffusion Models, Multi-modal Learning | m.jaewon@kaist.ac.kr | 4 |
| Chaehyun Kim | 석박사통합과정 | Computer Vision, Robot Learning, Explainability | kchyun@kaist.ac.kr | 3, 6 |
| Jiwon Kang | 석박사통합과정 | Image Generation, Diffusion Models, Flow Matching | jiwon7258@kaist.ac.kr |  |
| Joungbin Lee | 석박사통합과정 | 3D/4D Generation, Reconstruction | joungbinlee@kaist.ac.kr |  |
| Jiyoung Kim | 석박사통합과정 | Image/Video Generation & Editing | kplove01@kaist.ac.kr | 5 |
| Jung Yi | 석사과정 | Efficient World Model | jungyi9906@kaist.ac.kr | 2 |
| Hyunkoo Lee | 석사과정 | Diffusion Models, Multimodal | guu980@kaist.ac.kr |  |
| Minkyung Kwon | 석사과정 | 3D Vision, Diffusion Models | minkyung.kwon@kaist.ac.kr |  |
| Eunbeen Hong | 석박사통합과정 | Diffusion Models, Segmentation | eunbeen.hong@kaist.ac.kr |  |
| Jinhyeok Choi | 석박사통합과정 | 3D Vision, Diffusion Models, Visual Correspondence | wlsguur@kaist.ac.kr |  |
| Junghyun Park | 석박사통합과정 | Video Understanding, Visual Correspondence | junghyun.park@kaist.ac.kr |  |
| Jaeho Lee | 석박사통합과정 | Diffusion Models, Multimodal | jeffy1234@kaist.ac.kr | 7 |
| Jinhyuk Jang | 석사과정 | 3D Vision | jhjangbot@kaist.ac.kr |  |
| Jahyeok Koo | 석박사통합과정 | Visual Correspondence, 4D Vision | jahyeok.koo@kaist.ac.kr |  |
| Paul Hyunbin Cho | 석사과정 | Multimodal Learning, Generative Models | paulh.cho@kaist.ac.kr | 2, 4 |
| Mungyeom Kim | 석박사통합과정 | 3D Vision, 3D/4D Reconstruction | mungyeom011@kaist.ac.kr | 3 |
| Sanghyun Lee | 석박사통합과정 | Generative models | lsh83210@kaist.ac.kr |  |
| Seonghu Jeon | 석사과정 | 3D/4D Vision, Representation Learning, Generative Models | seonghu.jeon@kaist.ac.kr | 8 |
| Dahyun Chung | 석박사통합과정 | Video Diffusion Models | dahyun1016@kaist.ac.kr | 1, 5 |
| Hyunwook Choi | 석박사통합과정 | Video Generation | hyunwook@kaist.ac.kr | 1 |
| Jiho Park | 석사과정 | Representation Learning, 3D Vision | jihop00@kaist.ac.kr | 8 |
| Jaeyeong Kim | 석박사통합과정 | 3D Vision, Visual Correspondence | jy9394@kaist.ac.kr |  |
| Minkyeong Jeon | 석사과정 | 3D Vision, MLLM | minkyeong.jeon@kaist.ac.kr | 3 |
| Eunju Yang | 석사과정 | Multimodal Learning | eunju.yang@kaist.ac.kr |  |
| Hyunah Ko | 석사과정 | 3D/4D vision, VLA | hyunahko@kaist.ac.kr |  |
| Sangoh Kim | 석사과정 | Video Generation, VLA | tkddh1109@kaist.ac.kr |  |
| Youngjin Shin | 석사과정 | Representative learning, 3D and 4D generation | shinstar1214@kaist.ac.kr |  |
| Hyeonseo Yu | 석사과정 | 3D/4D Vision, Multimodal Learning, Robotics | hyeonseo.yu@kaist.ac.kr |  |
| Tongmin Kim | 석사과정 | 3D/4D Vision, World Models | tmkim0718@kaist.ac.kr |  |
| Wonjin Nam | 석사과정 | Generative Modeling, Reinforcement Learning | wjnam6525@kaist.ac.kr |  |
| Minjae Kim | 학부 연구생 | Diffusion Models, Text/Image-to-3D |  |  |
| Jaewoo Yu | 학부 연구생 | Diffusion Models | wodnjack@kaist.ac.kr |  |
| Kyungjin Oh | 학부 연구생 | Image & Video Restoration | 2364ohkj@yonsei.ac.kr |  |
| Junsu Kim | 학부 연구생 | 3D Vision | sam9732@kaist.ac.kr | 3 |
| Kohyun Kim | 학부 연구생 | Image and Video Restoration | kim3386@purdue.edu |  |
| Jaewoon Lee | 학부 연구생 | 3D Vision | theolee72@snu.ac.kr |  |
| Hyunsung Kim | 학부 연구생 | 3D/4D Vision, Diffusion Models | khs2001v@kaist.ac.kr | 1 |
| Seungho Jang | 학부 연구생 | 3D Vision | hoosong0235@kaist.ac.kr |  |
| Donghwan Shin | 학부 연구생 | 3DGS, 3D Foundation Model | david_shin@kaist.ac.kr |  |
| Junhwan Heo | 학부 연구생 | Computer Vision, Diffusion Models | junhwan26@korea.ac.kr |  |
| Kaeun Han | 학부 연구생 | 3D Vision, Diffusion Models | esther_han@i.ewha.ac.kr |  |
| Kyehong Park | 학부 연구생 | Dynamic Mesh Generation | mirax47@korea.ac.kr |  |
| Jooho Son | 학부 연구생 | 4D | durei1@kaist.ac.kr |  |
| Yoonchan Kim | 학부 연구생 | Vision-Language-Action, World Models | yoonchan.kim@yonsei.ac.kr |  |
| Hyeonbeen Jeon | 학부 연구생 | Video Diffusion Models, Discrete Diffusion | justbecoz@yonsei.ac.kr |  |

## 졸업생 진로

랩 구성원 페이지의 졸업생 목록이다. 교수는 2024년 8월 KAIST로 옮기기 전 고려대에 있었다.[^students][^faculty]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Inès Hyeonsu Kim | M.S. in 2026 (2026) | Ph.D. candidate @ California Institute of Technology |
| Jaeeun Lee | Undergraduate Research Intern | Master's Student @ Georgia Institute of Technology |
| Sangwon Jung | Postdoc in 2026 (2026) | Trillion Labs |
| Sunghwan Hong | Ph.D. in 2025 (2025) | Postdoc @ ETH Zurich |
| Donghoon Ahn | Undergraduate Research Intern | Ph.D. candidate @ UC Berkeley |
| Junwan Kim | Undergraduate Research Intern | Master's Student @ New York University |
| Hyoungwon Cho | M.S. in 2025 (2025) | Samsung Electronics |
| Kyusun Cho | M.S. in 2025 (2025) | Plantynet |
| Seyeon Kim | M.S. in 2024 (2024) | Samsung Electronics |
| Jaehoon Ko | M.S. in 2024 (2024) | Samsung Electronics |
| Seungjun An | M.S. in 2024 (2024) | Samsung Electronics |
| Seonghoon Park | M.S. in 2024 (2024) | Samsung Electronics |
| Gyeongnyeon Kim | M.S. in 2024 (2024) | SK Telecom |
| Gyuseong Lee | M.S. in 2024 (2024) | LG Electronics |
| Jihye Park | M.S. in 2024 (2024) | Samsung Electronics |
| Jiuhn Song | M.S. in 2024 (2024) | Hyundai Motors |
| Susung Hong | Undergraduate Research Intern | Ph.D. candidate @ University of Washington |
| Mira Kim | M.S. in 2023 (2023) |  |
| Soohyun Kim | M.S. in 2023 (2023) | LG Electronics |
| Sunwoo Kim | M.S. in 2023 (2023) | LG Electronics |
| Jongbeom Baek | M.S. in 2023 (2023) | LG Electronics |
| Kwangrok Ryoo | M.S. in 2023 (2023) | LG AI Research |
| Gijae Lee | M.S. in 2022 (2022) |  |
| Jiwon Kim | M.S. in 2022 (2022) | LG AI Research |
| Yunsung Lee | M.S. in 2022 (2022) | Head of Research @ Maum AI, Adjunct Professor @ DGIST |
| Daehwan Kim | Visiting Researcher | Samsung Electro-Mechanics |

## 최근 논문 목록 (2021–2026)

랩 논문 목록에 실린 2021–2026년 논문 178편이다.[^papers] 대표 논문은 위 표에서 쉬운 설명을 붙였다.

**2026**

- Hyunwook Choi, Seungryong Kim, Dongyoon Han, Sangdoo Yun. "Speculative Forcing for Efficient Autoregressive Video Generation". **.
- Jahyeok Koo, Hyeonseo Yu, Seungho Jang, Jaewoo Jung, Jiwon Kang, Seokju Cho, Seungryong Kim. "Can Learning to Answer Spatial Questions Improve Novel-View Generation?". **.
- Dahyun Chung, Siyoon Jin, Hyunwook Choi, Honggyu An, Junyoung Seo, Hyunsung Kim, Seung Wook Kim, Seungryong Kim. "Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction". **.
- Jiyoung Kim, Paul Hyunbin Cho, Jisu Nam, Donghoon Lee, Hyunsung Go, Yeonkyeong Lee, Hansaem Kim, Seungryong Kim. "GRACE: Generation-aware latent compression for efficient video generation". **.
- Jaeyeong Kim, Jinhyuk Jang, Jongmin Lee, Kyehong Park, Seungryong Kim. "Tetris3D: 3D Scene Generation with Objects That Fit Together". **.
- Hyunwook Choi, Dahyun Chung, Hyunsung Kim, Siyoon Jin, Jinhyeok Choi, Junyoung Seo, Seungryong Kim. "World Observer: Joint Actor-Observer Generation for Persistent World Modeling". **.
- Yeji Choi, Jinhyeok Choi, Jaewon Min, Minkyung Kwon, Jin Hyeon Kim, Seungryong Kim. "GeoFace: Consistent Multi-View Face Generation with Geometry-Constrained Diffusion". **.
- Haina Jiang, Liam Wang, Peng-Chen Chen, Min Seop Kwak, Seungryong Kim, Brian Bell, Jeong Joon Park. "Error-Conditioned Neural Solvers". **.
- JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira, Kazumi Fukuda, Jahyeok Koo, Jisang Han, Yuki Mitsufuji, Seungryong Kim. "MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation". **.
- Paul Hyunbin Cho\*, Jinhyuk Jang\*, SeokYoung Lee, Joungbin Lee, Siyoon Jin, Heeseong Shin, Jung Yi, Yunjin Park, Chulmin Park, Seungryong Kim. "Lip Forcing: Few-Step Autoregressive Diffusion for Real-time Lip Synchronization". **.
- Minkyung Kwon\*, Jinhyeok Choi\*, Youngjin Shin, Jaeyeong Kim, JongMin Lee, Seungryong Kim. "MORPHOS: Autoregressive 4D Generation with Temporal Structured Latents". **.
- Mungyeom Kim\*, Minkyeong Jeon\*, Honggyu An\*, Jaewoo Jung, Hyuna Ko, Jisang Han, Hyeonseo Yu, Donghwan Shin, Sunghwan Hong, Takuya Narihira, Kazumi Fukuda, Yuki Mitsufuji, Seungryong Kim. "C4G: Learning Global Motion with Compact Gaussians for Feed-Forward 4D Reconstruction". **.
- Jung Yi, Minjae Kim, Paul Hyunbin Cho, Wooseok Jang, Sangdoo Yun, Seungryong Kim. "WorldKV: Efficient World Memory with World Retrieval and Compression". **.
- Jaewon Min, Jaeeun Lee, Yeji Choi, Paul Hyunbin Cho, Jin Hyeon Kim, Tae-Young Lee, Jongsik Ahn, Hwayeong Lee, Seonghyun Park, Seungryong Kim. "Degradation-Aware Optical Flow with Diffusion Models". **.
- Woojeong Jin\*, Jaeho Lee\*, Heeseong Shin, Seungho Jang, Junhwan Heo, Seungryong Kim. "AgentRVOS: Reasoning over Object Tracks for Zero-Shot Referring Video Object Segmentation". **.
- Minseop Kwak\*, Minkyung Kwon\*, Jinhyeok Choi\*, Jiho Park, Seungryong Kim. "ReNoV: Projected Representation Conditioning for High-fidelity Novel View Synthesis". **.
- Yonglak Son, Suhyeok Kim, Seungryong Kim, Young Geun Kim. "CorGi: Contribution-Guided Block-Wise Interval Caching for Training-Free Acceleration of Diffusion Transformers". **.
- Chaehyun Kim, Chi-Pin Huang, Jisoo Kim, Min-Hung Chen, Yu-Chiang Frank Wang, Seungryong Kim, Fu-En Yang. "ThinkWorld: World Imagination Reinforces Embodied Action Reasoning". *Workshop on Robot Learning with World Models: Capabilities, Frontiers, and Challenges @ NeurIPS (NeurIPSW) Oral, 2026. Workshop on PTA: From Pretrained Representations to Acting Agents @ NeurIPS (NeurIPSW), 2026*.
- Soowon Son, Heeseong Shin, Jihwan Eom, Jaeyeol Jeon, Sunghun Kang, Woo-Young Kang, Seungryong Kim, Byungseok Roh. "Video Token Compression via Formation and Selection Distillation in Large Vision Language Models". *Workshop on On-Device Intelligence: Foundation Models under Real-World Constraints @ NeurIPS (NeurIPSW), 2026. Workshop on Long Context Foundation Models @ NeurIPS (NeurIPSW), 2026*.
- Seongchan Kim, Soowon Son, Sangoh Kim, Hyunah Ko, Eunbeen Hong, Hyunkoo Lee, Sanghyun Lee, WonJun Moon, Kihong Kim, Dongyeon Son, Woongchan Nam, Seungryong Kim. "One Loss Is Not Enough: Cross-Objective Structured Pruning for Reasoning Vision–Language–Action Models". *Workshop on Grounded and Faithful Vision-Language Models for Real-World Deployment @ NeurIPS (NeurIPSW), 2026. Workshop on On-Device Intelligence: Foundation Models under Real-World Constraints @ NeurIPS (NeurIPSW), 2026. Workshop on PTA: From Pretrained Representations to Acting Agents @ NeurIPS (NeurIPSW), 2026*.
- Junwan Kim\*, Jiho Park\*, Seonghu Jeon, Seungryong Kim. "Better Source, Better Flow: Learning Condition-Dependent Source Distribution for Flow Matching". *Neural Information Processing Systems (NeurIPS), 2026*.
- Youngdong Jang, Gyeongrok Oh, Jong Wook Kim, Hyunju Ryu, Hyung-gun Chi, SeungHyeon Kim, Seungryong Kim, Jonghyun Choi, Sangpil Kim. "Motion Cues from Image-based Point Tracking for LiDAR Scene Flow Estimation". *Neural Information Processing Systems (NeurIPS), 2026*.
- Seokju Cho, Ryo Hachiuma, Abhishek Badki, Hang Su, Byung-Kwan Lee, Chan Hee Song, Sifei Liu, Subhashree Radhakrishnan, Seungryong Kim, Yu-Chiang Frank Wang, Min-Hung Chen. "SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning". *Neural Information Processing Systems (NeurIPS), 2026*.
- Jisu Nam, Jahyeok Koo, Soowon Son, Jaewoo Jung, Honggyu An, Junhwa Hur, Seungryong Kim. "TrackCraft3R: Repurposing Video Diffusion Transformers for Dense 3D Tracking". *Neural Information Processing Systems (NeurIPS), 2026*.
- Jiyoung Kim, Youngjin Shin, Siyoon Jin, Dahyun Chung, Jisu Nam, Tongmin Kim, Jongjae Park, Hyeonwoo Kang, Seungryong Kim. "CORAL: Correspondence Alignment for Improved Virtual Try-On". *Neural Information Processing Systems (NeurIPS), 2026*.
- Sangbeom Lim, Seoung Wug Oh, Heeji Yoon, Seungryong Kim, Joon-Young Lee. "VideoMaMa++: Temporally Consistent Video Matting via Preserve-and-Refine Tokens". *Neural Information Processing Systems (NeurIPS), 2026*.
- Jaewoo Jung, Hyeonseo Yu, Honggyu An, Jisang Han, Mungyeom Kim, Minkyeong Jeon, Heeseong Shin, WonJun Moon, Federico Tombari, Daniel Barath, Marc Pollefeys, Seungryong Kim, Sunghwan Hong. "Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering". *Neural Information Processing Systems (NeurIPS), 2026. Workshop on 3D in the Era of World Models @ ECCV (ECCVW), 2026*.
- Siyoon Jin\*, Dahyun Chung\*, Honggyu An, Sangbeom Lim, Wonjin Nam, Jaewoo Jung, WonJun Moon, Seungryong Kim. "Repurposing Video Diffusion Transformers for Cross-View Temporal Object Correspondence". *Neural Information Processing Systems (NeurIPS), 2026*.
- Jaeyeong Kim, Ines Kim, Jahyeok Koo, Seungryong Kim. "T2Mo: Controllable Dynamic 3D Shape Generation via 3D Trajectories and Text". *Neural Information Processing Systems (NeurIPS), 2026*.
- Jin Hyeon Kim\*, Jaeeun Lee\*, Claire Kim, Kyoungjin Oh, Paul Hyunbin Cho, Jaewon Min, Yeji Choi, Jihye Park, Hyunhee Park, Minkyu Park, Seungryong Kim. "GARD: Geometry-Aware Representation Denoising for Robust Multi-view 3D Reconstruction". *Neural Information Processing Systems (NeurIPS), 2026*.
- Sanghyun Lee, Chunsan Hong, Seungryong Kim, Jonghyun Lee, Jongho Park, Dongmin Park. "Looped Diffusion Language Models". *Neural Information Processing Systems (NeurIPS), 2026. Workshop on Non-Autoregressive Language Models for Fast & Flexible Text Generation @ COLM (COLMW), 2026. (Spotlight)*.
- Jisoo Kim, Jungbin Cho, Sanghyeok Chu, Ananya Bal, Jinhyung Kim, Gunhee Lee, Sihaeng Lee, Seung Hwan Kim, Bohyung Han, Hyunmin Lee, Laszlo A. Jeni, Seungryong Kim. "Pri4R: Learning World Dynamics for Vision-Language-Action Models with Privileged 4D Representation". *The Conference on Robot Learning (CoRL), 2026*.
- Jaewoo Jung\*, Jisang Han\*, Honggyu An\*, Jiwon Kang\*, Seonghoon Park\*, Seungryong Kim. "RAIN-GS: Relaxing Accurate Initialization Constraint for 3D Gaussian Splatting". *Workshop on Wild 3D: 3D Modeling, Reconstruction, and Generation in the Wild @ ECCV (ECCVW), 2026*.
- Jisang Han\*, Seonghu Jeon\*, Jaewoo Jung, René Zurbrügg, Honggyu An, Tifanny Portela, Marco Hutter, Marc Pollefeys, Seungryong Kim, Sunghwan Hong. "GAM: Geometric Action Model for Robot Policy Learning". *Workshop on 3D in the Era of World Models @ ECCV (ECCVW), 2026*.
- Seokyeong Lee, Sithu Aung, Junyong Choi, Seungryong Kim, Ig-Jae Kim, Junghyun Cho. "PLOT: Pseudo-Labeling via Object Tracking for Scalable Monocular 3D Object Detection". *European Conference on Computer Vision (ECCV), 2026*.
- Marcel Gröpl\*, Jaewoo Jung\*, Seungryong Kim, Marc Pollefeys, Sunghwan Hong. "Entropy-Gradient Grounding: Training-Free Evidence Retrieval in Vision-Language Models". *European Conference on Computer Vision (ECCV), 2026*.
- Jiwon Kang\*, Heeji Yoon\*, Jaewoo Jung, Jaewon Min, Minkyeong Jeon, Biyeon Hwang, Sangwon Jung, Seungryong Kim. "Transferability Between Understanding and Generation in Unified Multimodal Models". *European Conference on Computer Vision (ECCV), 2026*.
- Jini Yang\*, Eunbeen Hong\*, Soowon Son, Hyunkoo Lee, Sunghwan Hong, Sunok Kim, Seungryong Kim. "TETO: Tracking Events with Teacher Observation for Real-World Motion Understanding". *European Conference on Computer Vision (ECCV), 2026*.
- Wooseok Jang, Seonghu Jeon, Jisang Han, Jinhyeok Choi, Minkyung Kwon, Seungryong Kim, Saining Xie, Sainan Liu. "Geometric Latent Diffusion: Repurposing Geometric Foundation Models for Multi-view Diffusion". *European Conference on Computer Vision (ECCV), 2026. (Oral Presentation)*.
- Junyoung Seo\*, Hyunwook Choi\*, Minkyung Kwon, Jinhyeok Choi, Siyoon Jin, Gayoung Lee, Junho Kim, JoungBin Lee, Geonmo Gu, Dongyoon Han, Sangdoo Yun, Seungryong Kim, Jin-Hwa Kim. "Seoul World Model: Grounding World Simulation Models in a Real-World Metropolis". *European Conference on Computer Vision (ECCV), 2026. (Spotlight) Workshop on F2S: Toward Reliable, Controllable and Trustworthy Long-Horizon Video Generation @ ICML (ICMLW), 2026. (Spotlight)*.
- Seongchan Kim\*, Woojeong Jin\*, Sangbeom Lim\*, Heeji Yoon\*, HyunWook Choi, Seungryong Kim. "Referring Video Object Segmentation via Language-aligned Track Selection". *Workshop on Resource-Adaptive Foundation Model Inference @ ICML (ICMLW), 2026*.
- Chunsan Hong, Sanghyun Lee, Chieh-Hsin Lai, Satoshi Hayakawa, Yuhta Takida, Yuki Mitsufuji, Seungryong Kim, Jong Chul Ye. "Understanding and Accelerating the Training of Masked Diffusion Language Models". *Workshop on Structured Probabilistic Inference & Generative Modeling @ ICML (ICMLW), 2026*.
- Sanghyun Lee, Sunwoo Kim, Seungryong Kim, Jongho Park, Dongmin Park. "Effective Test-Time Scaling of Discrete Diffusion through Iterative Refinement". *Workshop on Structured Probabilistic Inference & Generative Modeling @ ICML (ICMLW), 2026*.
- Jung Yi, Wooseok Jang, Paul Hyunbin Cho, Jisu Nam, Heeji Yoon, Seungryong Kim. "Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression". *International Conference on Machine Learning (ICML), 2026*.
- Sanghyun Lee , Seungryong Kim , Jongho Park , Dongmin Park. "Lookahead Unmasking Elicits Accurate Decoding in Diffusion Language Models". *International Conference on Machine Learning (ICML), 2026*.
- Hyunmin Cho, Donghoon Ahn, Susung Hong, Jee Eun Kim, Seungryong Kim, Kyong Hwan Jin. "TAG: Tangential Amplifying Guidance for Hallucination-Resistant Diffusion Sampling". *International Conference on Machine Learning (ICML), 2026*.
- Jisu Nam, Yicong Hong, Chun-Hao Paul Huang, Feng Liu, JoungBin Lee, Jiyoung Kim, Siyoon Jin, Yunsung Lee, Jaeyoon Jung, Suhwan Choi, Seungryong Kim, Yang Zhou. "WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation". *Workshop on Video World Model: Interaction, Memory, and Efficiency @ CVPR (CVPRW), 2026*.
- Heeseong Shin, Byeongho Heo, Dongyoon Han, Seungryong Kim, Taekyung Kim. "Exploring Conditions for Diffusion models in Robotic Control". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2026*.
- Jisang Han, Sunghwan Hong, Jaewoo Jung, Wooseok Jang, Honggyu An, Qianqian Wang, Seungryong Kim, Chen Feng. "RobustVGGT: Emergent Outlier View Rejection in Visual Geometry Grounded Transformers". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2026*.
- Honggyu An\*, Jaewoo Jung\*, Mungyeom Kim, Sunghwan Hong, Chaehyun Kim, Kazumi Fukuda, Minkyeong Jeon, Jisang Han, Takuya Narihira, Hyuna Ko, Junsu Kim, Yuki Mitsufuji, Seungryong Kim. "C3G: Learning Compact 3D Representations with 2K Gaussians". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2026. Workshop on Open-World 3D Scene Understanding and Representations @ CVPR (CVPRW), 2026*.
- Minkyung Kwon\*, Jinhyeok Choi\*, Jiho Park\*, Seonghu Jeon, Jinhyuk Jang, Junyoung Seo, Minseop Kwak, Jin-Hwa Kim, Seungryong Kim. "CAMEO: Correspondence-Attention Alignment for Multi-View Diffusion Models". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2026*.
- Jahyeok Koo\*, Inès Hyeonsu Kim\*, Mungyeom Kim, Junghyun Park, Seohyeon Park, Jaeyeong Kim, Jung Yi, Seokju Cho, Seungryong Kim. "MV-TAP: Tracking Any Point in Multi-View Videos". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2026*.
- Inès Hyeonsu Kim\*, Seokju Cho\*, Jahyeok Koo, Junghyun Park, Jiahui Huang, Honglak Lee, Joon-Young Lee, Seungryong Kim. "AnthroTAP: Learning Point Tracking with Real-World Motion". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2026*.
- Jiwon Kang\*, Yeji Choi\*, JoungBin Lee, Wooseok Jang, Jinhyeok Choi, Taekeun Kang, Yongjae Park, Myungin Kim, Seungryong Kim. "APPLE: Attribute-Preserving Pseudo-Labeling for Diffusion-Based Face Swapping". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2026*.
- Sangbeom Lim, Seoung Wug Oh, Jiahui Huang, Heeji Yoon, Seungryong Kim, Joon-Young Lee. "VideoMaMa: Mask-Guided Video Matting via Generative Prior". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2026*.
- Seokju Cho, Abhishek Badki, Hang Su, Jindong Jiang, Ziyao Zeng, Seungryong Kim, Sifei Liu, Orazio Gallo. "4DP-QA: Scalable QA for 4D Perception in Vision Language Models". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2026*.
- Woojeong Jin, Seongchan Kim, Jaeho Lee, and Seungryong Kim. "InterRVOS: Interaction-aware Referring Video Object Segmentation". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2026*.
- Utae Jeong, Sumin In, Hyunju Ryu, Jaewan Choi, Feng Yang, Jongheon Jeong, Seungryong Kim, Sangpil Kim. "WaTeRFlow: Watermark Temporal Robustness via Flow Consistency". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2026*.
- Inès Hyeonsu Kim\*, Woojeong Jin\*, Soowon Son, Junyoung Seo, Seokju Cho, JeongYeol Baek, Byeongwon Lee, JoungBin Lee, Seungryong Kim. "Pose-Diversified Augmentation with Diffusion Model for Person Re-Identification". *IEEE Conf. Computer Vision Pattern Recognition (CVPR) Findings, 2026*.
- Heeji Yoon\*, Jaewoo Jung\*, Junwan Kim\*, Hyungyu Choi, Heeseong Shin, Sangbeom Lim, Honggyu An, Chaehyun Kim, Jisang Han, Donghyun Kim, Chanho Eom, Sunghwan Hong, Seungryong Kim. "VIRAL: Visual Representation Alignment for Multimodal Large Language Models". *Workshop on Multimodal Intelligence: Next Token Prediction & Beyond @ ICLR (ICLRW), 2026*.
- Min-Seop Kwak, Junho Kim, Sangdoo Yun, Dongyoon Han, Taekyoung Kim, Seungryong Kim, Jin-Hwa Kim. "MoAI: Aligned Novel View Image and Geometry Synthesis via Cross-modal Attention Instillation". *International Conference on Learning Representations (ICLR), 2026*.
- Joungbin Lee\*, Jaewoo Jung\*, Jisang Han\*, Takuya Narihira, Kazumi Fukuda, Junyoung Seo, Sunghwan Hong, Yuki Mitsufuji, Seungryong Kim. "3D Scene Prompting for Scene-Consistent Camera-Controllable Video Generation". *International Conference on Learning Representations (ICLR), 2026*.
- Siyoon Jin, Seongchan Kim, Dahyun Chung, Jaeho Lee, Hyunwook Choi, Jisu Nam, Jiyoung Kim, Seungryong Kim. "MATRIX: Mask Track Alignment for Interaction-aware Video Generation". *International Conference on Learning Representations (ICLR), 2026*.
- Jaewon Min\*, Jin Hyeon Kim\*, Paul Hyunbin Cho, Jaeeun Lee, Jihye Park, Minkyu Park, Sangpil Kim, Hyunhee Park, Seungryong Kim. "TAIR: Text-Aware Image Restoration with Diffusion Models". *International Conference on Learning Representations (ICLR), 2026*.
- Donghoon Ahn\*, Jiwon Kang\*, Sanghyun Lee, Jaewon Min, Wooseok Jang, Minjae Kim, Hyungwon Cho, Sayak Paul, SeonHwa Kim, Eunju Cha, Kyong Hwan Jin, Seungryong Kim. "A Noise is Worth Diffusion Guidance". *International Conference on Learning Representations (ICLR), 2026*.
- Junyoung Seo\*, Jisang Han\*, Jaewoo Jung\*, Siyoon Jin, Joungbin Lee, Takuya Narihira, Kazumi Fukuda, Takashi Shibuya, Donghoon Ahn, Shoukang Hu, Seungryong Kim, Yuki Mitsufuji. "Vid-CamEdit: Video Camera Trajectory Editing with Generative Rendering from Estimated Geometry". *AAAI Conference on Artificial Intelligence (AAAI), 2026*.
- JoungBin Lee\*, Hyunkoo Lee\*, Jini Yang\*, Chaehyun Kim, Jung Yi, Seok Hwangbo, Hyeoncheol Lee, Minho Chun, Eunjo Jeong, Seungryong Kim. "CHIMERA: Controllable High-quality Image-Mask Extraction for Reliable Diffusion-Based Anomaly Synthesis". *AAAI Conference on Artificial Intelligence (AAAI), 2026*.

**2025**

- Soowon Son, Honggyu An, Chaehyun Kim, Hyunah Ko, Jisu Nam, Dahyun Chung, Siyoon Jin, Jung Yi, Jaewon Min, Junhwa Hur, Seungryong Kim. "DiTracker: Repurposing Video Diffusion Transformers for Robust Point Tracking". **.
- Hyunkoo Lee, Wooseok Jang, Jini Yang, Taehwan Kim, Sangoh Kim, Sangwon Jung, Seungryong Kim. "V-Warper: Appearance-Consistent Video Diffusion Personalization via Value Warping". **.
- Jin Hyeon Kim, Paul Hyunbin Cho, Claire Kim, Jaewon Min, Jaeeun Lee, Jihye Park, Yeji Choi, Seungryong Kim. "UniT: Unified Diffusion Transformer for High-fidelity Text-Aware Image Restoration". **.
- Junyoung Seo, Rodrigo Mira, Alexandros Haliassos, Stella Bounareli, Honglie Chen, Linh Tran, Seungryong Kim, Zoe Landgraf, Jie Shen. "Lookahead Anchoring: Preserving Character Identity in Audio-Driven Human Animation". **.
- Jini Yang, Beomseok Oh, Seungryong Kim, Sunok Kim. "SpikeMatch: Semi-Supervised Learning with Temporal Dynamics of Spiking Neural Networks". **.
- Sangbeom Lim\*, Junwan Kim\*, Heeji Yoon, Jaewoo Jung, Seungryong Kim. "URECA: Unique Region Caption Anything". **.
- Jisu Nam\*, Soowon Son\*, Dahyun Chung, Jiyoung Kim, Siyoon Jin, Junhwa Hur, Seungryong Kim. "Emergent Temporal Correspondences from Video Diffusion Transformers". *Neural Information Processing Systems (NeurIPS), 2025. [pdf] [project]*.
- Chaehyun Kim, Heeseong Shin, Eunbeen Hong, Heeji Yoon, Anurag Arnab, Paul Hongsuck Seo, Sunghwan Hong, Seungryong Kim. "Seg4Diff: Unveiling Open-Vocabulary Semantic Segmentation in Text-to-Image Diffusion Transformers". *Neural Information Processing Systems (NeurIPS), 2025. [pdf] [project]*.
- Jisang Han\*, Honggyu An\*, Jaewoo Jung\*, Takuya Narihira, Junyoung Seo, Kazumi Fukuda, Chaehyun Kim, Sunghwan Hong, Yuki Mitsufuji, Seungryong Kim. "D2USt3R: Enhancing 3D Reconstruction with 4D Point Maps for Dynamic Scenes". *Neural Information Processing Systems (NeurIPS), 2025. [pdf] [project]*.
- Donghoon Ahn\*, Jiwon Kang\*, Sanghyun Lee, Minjae Kim, Jaewon Min, Wooseok Jang, Saungwu Lee, Sayak Paul, Susung Hong, Seungryong Kim. "Where and How to Perturb: On the Design of Perturbation Guidance in Diffusion and Flow Models". *Neural Information Processing Systems (NeurIPS), 2025. Workshop on ReALM-GEN: Post-training and Inference-time Alignment for Generative Models @ ICLR (ICLRW), 2026. [pdf] [project]*.
- Heeju Ko, Sungjune Kim, Gyeongrok Oh, Jeongyoon Yoon, Honglak Lee, Sujin Jang, Seungryong Kim, Sangpil Kim. "Active Test-time Vision-Language Navigation". *Neural Information Processing Systems (NeurIPS), 2025. [pdf]*.
- Gyudong Kim, Hyukju Na, Jin Hyeon Kim, Hyunsung Jang, Jaemin Park, Jaegi Hwang, Namkoo Ha, Seungryong Kim, Young Geun Kim. "First Attentions Last: Better Exploiting First Attentions for Efficient Parallel Training". *Neural Information Processing Systems (NeurIPS), 2025. [pdf] [project]*.
- Seokyeong Lee, Junyong Choi, Seungryong Kim, Ig-Jae Kim, Junghyun Cho. "Leveraging Intrinsic Components for Few-Shot Neural Radiance Fields in Unconstrained Illumination". *IEEE Access, 2025. [pdf]*.
- Jaewoo Jung\*, Jisang Han\*, Jiwon Kang\*, Seongchan Kim, Min-Seop Kwak, Seungryong Kim. "Self-Evolving Neural Radiance Fields". *Workshop on Wild 3D: 3D Modeling, Reconstruction, and Generation in the Wild @ ICCV (ICCVW), 2025. [pdf] [project]*.
- Chaoran Zhu, Junyoung Seo, Aliyasin Ayouch, Emmanuel Senft, Seungryong Kim, Changjae Oh. "DiffPort: Adapting Pre-trained Diffusion Models for Generalizable Robot Manipulation". *Benchmarking via Competitions in Robotic Grasping and Manipulation @ IROS (IROSW), 2025. [project]*.
- Jaehoon Ko, Kyusun Cho, Joungbin Lee, Heeji Yoon, and Seungryong Kim. "Talk3D: High-Fidelity Talking Portrait Synthesis via Personalized 3D Generative Prior". *1st Workshop on Generative AI for Audio-Visual Content Creation @ ICCV (ICCVW), 2025. [pdf] [project]*.
- Siyoon Jin, Jisu Nam, Jiyoung Kim, Dahyun Chung, Yeong-Seok Kim, Joonhyung Park, Heonjeong Chu, Seungryong Kim. "AM-Adapter: Appearance Matching Adapter for Exemplar-based Semantic Image Synthesis". *IEEE International Conference on Computer Vision (ICCV), 2025. [pdf] [project]*.
- Heeji Yoon\*, Heeseong Shin\*, Eunbeen Hong, Hyunwook Choi, Hansang Cho, Daun Chung, Seungryong Kim. "S4M: Boosting Semi-Supervised Instance Segmentation with SAM". *IEEE International Conference on Computer Vision (ICCV), 2025. [pdf] [project]*.
- Seonghu Jeon, Jinhyeok Choi, Junghyun Hwang, Seungryong Kim. "ReMoTE: A Benchmark for Object Motion Transfer". *International Technical Conference on Circuits/Systems, Computers, and Communications (ITC-CSCC), 2025*.
- Sunghwan Hong\*, Jaewoo Jung\*, Heeseong Shin, Jisang Han, Jiaolong Yang†, Chong Luo†, Seungryong Kim†. "PF3plat : Pose-Free Feed-Forward 3D Gaussian Splatting". *International Conference on Machine Learning (ICML), 2025. [pdf] [project]*.
- Joonhyung Park, Joonhyung_Park , Yeong-Seok Kim, HeonJeong Chu, Hye-Rin Kim, Seungryong Kim. "ReSIT: A more Realistic Synthetic Driving Dataset for Multi-Domain Image-to-Image Translation". *Synthetic Data for Computer Vision Workshop @ CVPR (CVPRW), 2025. [pdf]*.
- Jisu Nam, Soowon Son, Zhan Xu, Jing Shi, Difan Liu, Feng Liu, Seungryong Kim, Yang Zhou. "Visual Persona: Foundation Model for Full-Body Human Customization". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2025. [pdf] [project]*.
- Seokju Cho, Jiahui Huang, Seungryong Kim, Joon-Young Lee. "Seurat: From Moving Points to Depth". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2025. (Highlight) [pdf] [project]*.
- Honggyu An\*, Jin Hyeon Kim\*, Seonghoon Park, Jaewoo Jung, Jisang Han, Sunghwan Hong†, Seungryong Kim†. "Cross-View Completion Models are Zero-shot Correspondence Estimators". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2025. (Highlight) [pdf] [project]*.
- Inès Hyeonsu Kim\*, Seokju Cho\*, Jiahui Huang, Jung Yi, Joon-Young Lee, Seungryong Kim. "Exploring Temporally-Aware Features for Point Tracking". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2025. [pdf] [project]*.
- SeonHwa Kim, Jiwon Kim, Soobin Park, Donghoon Ahn, Jiwon Kang, Seungryong Kim, Kyong Hwan Jin, Eunju Cha. "Identity-preserving Distillation Sampling by Fixed-Point Iterator". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2025. [pdf] [project]*.
- Wooseok Jang, Youngjun Hong, Geonho Cha, Seungryong Kim. "ControlFace: Harnessing Facial Parametric Control for Face Rigging". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2025. [pdf] [project]*.
- Minsu Kim, Seungryong Kim, Kwanghoon Sohn. "Mixture of Submodule for Domain Adaptive Person Search". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2025. [pdf]*.
- Kihong Kim\*, Yunho Kim\*, Seokju Cho, Junyoung Seo, Jisu Nam, Kychul Lee, Seungryong Kim†, and KwangHee Lee†. "DiffFace: Diffusion-based Face Swapping with Facial Guidance". *Pattern Recognition (PR), 2025. [pdf] [project]*.
- Sieun Kim, Jaehwan Jeong, Sumin In, Seung Hyun Lee, Seungryong Kim, Saerom Kim, Wooyeol Baek, Sang Ho Yoon, Eugenio Culurciello, Sangpil Kim. "Semantically Complex Audio to Video Generation with Audio Source Separation". *Engineering Applications of Artificial Intelligence (EAAI), 2025*.
- Sangbeom Lim\*, Seongchan Kim\*, Seungjun An\* Seokju Cho, Paul Hongsuck Seo†, Seungryong Kim†. "Multi-Granularity Video Object Segmentation". *AAAI Conference on Artificial Intelligence (AAAI), 2025. [pdf] [project]*.
- Seyeon Kim\*, Siyoon Jin\*, Jihye Park\*, Kihong Kim, Jiyoung Kim, Jisu Nam, Seungryong Kim. "MoDiTalker: Motion-Disentangled Diffusion Model for High-Fidelity Talking Head Generation". *AAAI Conference on Artificial Intelligence (AAAI), 2025. [pdf] [project]*.
- Gyuseong Lee, Wooseok Jang, Jin Hyeon Kim, Jaewoo Jung, and Seungryong Kim. "Domain Generalization Using Large Pretrained Models with Mixture-of-Adapters". *Winter Conference on Applications of Computer Vision (WACV), 2025. [pdf] [project]*.

**2024**

- Min-Seop Kwak, Donghoon Ahn, Inès Hyeonsu Kim, Jin-Hwa Kim, Seungryong Kim. "GSD: Geometry-Aware Score Distillation via 3D Consistent Noising and Gradient Consistency Modeling". **.
- Heeseong Shin, Chaehyun Kim, Sunghwan Hong, Seokju Cho, Anurag Arnab†, Paul Hongsuck Seo†, Seungryong Kim†. "PixelCLIP: Towards Open-Vocabulary Semantic Segmentation Without Semantic Labels". *Neural Information Processing Systems (NeurIPS), 2024. [pdf] [project]*.
- Junyoung Seo, Kazumi Fukuda, Takashi Shibuya, Takuya Narihira, Naoki Murata, Shoukang Hu, Chieh-Hsin Lai, Seungryong Kim†, Yuki Mitsufuji†. "GenWarp: Single Image to Novel Views with Semantic-Preserving Generative Warping". *Neural Information Processing Systems (NeurIPS), 2024. [pdf] [project]*.
- Jiwon Kim, Byeongho Heo, Sangdoo Yun, Seungryong Kim, Dongyoon Han. "Match me if you can: Semantic Correspondence Learning with Unpaired Images". *Asian Conference on Computer Vision (ACCV), 2024. [pdf]*.
- Kyusun Cho\*, Joungbin Lee\*, Heeji Yoon\*, Yeobin Hong, Jaehoon Ko, Sangjun Ahn, and Seungryong Kim. "GaussianTalker: Real-Time High-Fidelity Talking Head Synthesis with Audio-Driven 3D Gaussian Splatting". *ACM Multimedia (MM), 2024 [pdf] [project]*.
- Daehwan Kim\*, Kwangrok Ryoo\*, Hansang Cho, and Seungryong Kim. "SplitNet: Learnable Clean-Noisy Label Splitting for Learning with Noisy Labels". *International Journal of Computer Vision (IJCV), 2024. [pdf] [project]*.
- Donghoon Ahn\*, Hyoungwon Cho\*, Jaewon Min, Wooseok Jang, Jungwoo Kim, SeonHwa Kim, Hyun Hee Park, Kyong Hwan Jin†, Seungryong Kim†. "Self-Rectifying Diffusion Sampling with Perturbed-Attention Guidance". *European Conference on Computer Vision (ECCV), 2024. [pdf] [project]*.
- Seokju Cho, Jiahui Huang, Jisu Nam, Honggyu An, Seungryong Kim†, Joon-Young Lee†. "Local All-Pair Correspondence for Point Tracking". *European Conference on Computer Vision (ECCV), 2024. [pdf] [project]*.
- Kihong Kim, Haneol Lee, Jihye Park, Seyeon Kim, Kwanghee Lee, Seungryong Kim†, Jaejun Yoo†. "Hybrid Video Diffusion Models with 2D Triplane and 3D Wavelet Representation". *European Conference on Computer Vision (ECCV), 2024. [pdf] [project]*.
- Jongbeom Baek\*, Gyeongnyeon Kim\*, Seonghoon Park\*, Honggyu An, Matteo Poggi, and Seungryong Kim. "MaskingDepth: Masked Consistency Regularization for Semi-supervised Monocular Depth Estimation". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2024. [pdf] [project]*.
- Jiyoung Lee, Seungryong Kim, Sunok Kim, Kwanghoon Sohn. "Discriminative Action Tubelet Detector for Weakly-supervised Action Detection". *Pattern Recognition (PR), 2024. [pdf]*.
- Susung Hong, Junyoung Seo, Sunghwan Hong, Heeseong Shin, and Seungryong Kim. "Large Language Models are Frame-level Directors for Zero-shot Text-to-Video Generation". *First Workshop on Controllable Video Generation at ICML (ICMLW), 2024. [pdf] [project]*.
- Junyoung Seo, Susung Hong, Wooseok Jang, Inès Hyeonsu Kim, Minseop Kwak, Doyup Lee, Seungryong Kim. "ReDream: Retrieval-Augmented Score Distillation for Text-to-3D Generation". *International Conference on Machine Learning (ICML), 2024. [pdf] [project]*.
- Gyeongnyeon Kim\*, Wooseok Jang\*, Gyuseong Lee\*, Susung Hong, Junyoung Seo, and Seungryong Kim. "Depth-Aware Guidance with Self-Estimated Depth Representations of Diffusion Models". *Pattern Recognition (PR), 2024. [pdf]*.
- Seokju Cho\*, Heeseong Shin\*, Sunghwan Hong, Anurag Arnab, Paul Hongsuck Seo, and Seungryong Kim. "CAT-Seg: Cost Aggregation for Open-Vocabulary Semantic Segmentation". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2024. (Highlight) [pdf] [project]*.
- Jisu Nam, Heesu Kim, DongJae Lee, Siyoon Jin, Seungryong Kim\*, Seunggyu Chang\*. "DreamMatcher: Appearance Matching Self-Attention for Semantically-Consistent Text-to-Image Personalization". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2024. [pdf] [project]*.
- Sunghwan Hong, Jaewoo Jung, Heeseong Shin, Jiaolong Yang, Seungryong Kim, Chong Luo. "Unifying Correspondence, Pose and NeRF for Pose-Free Novel View Synthesis from Stereo Pairs". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2024. (Highlight) [pdf] [project]*.
- Seokju Cho, Jiahui Huang, Seungryong Kim, Joon-Young Lee. "FlowTrack: Revisiting Optical Flow for Long-Range Dense Tracking". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2024. [pdf]*.
- Gyudong Kim, Mehdi Ghasemi, Soroush Heidari, Seungryong Kim, Young Geun Kim, Sarma Vrudhula, Carole-Jean Wu. "HeteroSwitch: Characterizing and Taming System-Induced Data Heterogeneity in Federated Learning". *Annual Conference on Machine Learning and Systems (MLSys), 2024*.
- Jisu Nam, Gyuseong Lee, Sunwoo Kim, Hyeonsu Kim, Hyoungwon Cho, Seyeon Kim, and Seungryong Kim. "DiffMatch: Diffusion Model for Dense Matching". *International Conference on Learning Representations (ICLR), 2024. (Oral Presentation) [pdf] [project]*.
- Sunghwan Hong\*, Seokju Cho\*, Seungryong Kim, and Stephen Lin. "Unifying Feature and Cost Aggregation with Transformers for Dense Correspondence". *International Conference on Learning Representations (ICLR), 2024. [pdf] [project]*.
- Junyoung Seo\*, Wooseok Jang\*, Min-Seop Kwak\*, Hyeonsu Kim, Jaehoon Ko, Junho Kim, Jin-Hwa Kim\*\*, Jiyoung Lee\*\*, and Seungryong Kim\*\*. "Let 2D Diffusion Model Know 3D-Consistency for Robust Text-to-3D Generation". *International Conference on Learning Representations (ICLR), 2024. [pdf] [project]*.
- Seungjun An\*, Seonghoon Park\*, Gyeongnyeon Kim\*, Jeongyeol Baek, Byeongwon Lee, Seungryong Kim. "Context Enhanced Transformer for Single Image Object Detection". *AAAI Conference on Artificial Intelligence (AAAI), 2024. [pdf] [project]*.
- SeokYeong Lee, JunYong Choi, Seungryong Kim, Ig-Jae Kim, and Junghyun Cho. "Few-Shot Neural Radiance Fields Under Unconstrained Illumination". *AAAI Conference on Artificial Intelligence (AAAI), 2024. [pdf] [project]*.

**2023**

- Changho Choi, Minho Kim, Junhyeok Lee, Hyoung-Kyu Song, Younggeun Kim, Seungryong Kim. "LatentSwap: An Efficient Latent Code Mapping Framework for Face Swapping". **.
- Sunwoo Kim, Wooseok Jang, Hyunsu Kim, Junho Kim, Yunjey Choi, Seungryong Kim, and Gayeong Lee. "User-friendly Image Editing with Minimal Text Input: Leveraging Captioning and Injection Techniques". **.
- Soohyun Kim, Junho Kim, Taekyung Kim, Hwan Heo, Seungryong Kim\*, Jiyoung Lee\*, Jin-Hwa Kim\*. "Panoramic Image-to-Image Translation". **.
- Kwangrok Ryoo, Yeonsik Jo, Seungjun Lee, Mira Kim, Ahra Jo, Seung Hwan Kim, Seungryong Kim, Soonyoung Lee. "Universal Noise Annotation: Unveiling the Impact of Noisy annotation on Object Detection". *Neural Information Processing Systems Workshop (NeurIPSW): Medical Imaging Meets NeurIPS, 2023. [pdf] [project]*.
- Jiuhn Song\*, Seonghoon Park\*, Honggyu An\*, Seokju Cho, Min-Seop Kwak, Sungjin Cho, and Seungryong Kim. "DäRF: Boosting Radiance Fields from Sparse Inputs with Monocular Depth Adaptation". *Neural Information Processing Systems (NeurIPS), 2023. [pdf] [project]*.
- Susung Hong\*, Donghoon Ahn\*, and Seungryong Kim. "Debasing Scores and Prompts of 2D Diffusion for View-consistent Text-to-3D Generation". *Neural Information Processing Systems (NeurIPS), 2023. [pdf] [project]*.
- Sunwoo Kim, Youngjo Min, Younghun Jung, and Seungryong Kim. "Controllable Style Transfer via Test-time Training of Implicit Neural Representation". *Pattern Recognition (PR), 2023. [pdf] [project]*.
- Caroline Karmann, Bahar Aydemir, Kynthia Chamilothori, Seungryong Kim, Sabine Süsstrunk, Marilyne Andersen. "Saliency prediction in 360° architectural scenes: Performance and impact of daylight variations". *Journal of Environmental Psychology (JEP), 2023. [pdf]*.
- Susung Hong, Gyuseong Lee, Wooseok Jang, and Seungryong Kim. "Improving Sample Quality of Diffusion Model Using Self-Attention Guidance". *IEEE International Conference on Computer Vision (ICCV), 2023. [pdf] [project]*.
- Soohyun Kim, Jongbeom Baek, Jihye Park, Eunjae Ha, Homin Jung, Taeyoung Lee, and Seungryong Kim. "InstaFormer++: Multi-Domain Instance-Aware Image-to-Image Translation with Transformer". *International Journal of Computer Vision (IJCV), 2023*.
- Minseop Kwak\*, Jiuhn Song\*, and Seungryong Kim. "GeCoNeRF: Few-shot Neural Radiance Fields via Geometric Consistency". *International Conference on Machine Learning (ICML), 2023. [pdf] [project]*.
- Gyeongnyeon Kim\*, Wooseok Jang\*, Gyuseong Lee\*, Susung Hong, Junyoung Seo, and Seungryong Kim. "Self-Predicted Depth-Aware Guidance with Diffusion Models". *IEEE CVPR Workshop- Generative Models for Computer Vision (CVPRW), 2023. [pdf] [project]*.
- Susung Hong\*, Donghoon Ahn\*, and Seungryong Kim. "Debiasing Scores and Prompts of 2D Diffusion for Robust Text-to-3D Generation". *IEEE CVPR Workshop- Generative Models for Computer Vision (CVPRW), 2023. [pdf] [project]*.
- Jihye Park\*, Sunwoo Kim\*, Soohyun Kim\*, Seokju Cho, Jaejun Yoo, Youngjung Uh, and Seungryong Kim. "LANIT: Language-Driven Image-to-Image Translation for Unlabeled Data". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2023. [pdf] [project]*.
- Minsu Kim, Seungryong Kim, Jungin Park, Seongheon Park, and Kwanghoon Sohn. "PartMix: Regularization Strategy to Learn Part Discovery for Visible-Infrared Person Re-identification". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2023*.
- Gijae Lee, Junsik Kim, Seungryong Kim, and Kanggeom Kim. "6D Object Pose Estimation Using a Particle Filter with Better Initialization". *IEEE Access, 2023*.
- Junyoung Seo\*, Gyuseong Lee\*, Seokju Cho, Jiyoung Lee, and Seungryong Kim. "MIDMs: Matching Interleaved Diffusion Models for Exemplar-based Image Translation". *AAAI Conference on Artificial Intelligence (AAAI), 2023. [pdf] [project]*.
- Jaehoon Ko\*, Kyusun Cho\*, Daewon Choi, Kwangrok Ryoo, and Seungryong Kim. "3D GAN Inversion with Pose Optimization". *Winter Conference on Applications of Computer Vision (WACV), 2023. [pdf] [project]*.

**2022**

- Bahar Aydemir, Deblina Bhattacharjee, Tong Zhang, Seungryong Kim, Mathieu Salzmann, and Sabine Süsstrunk. "Modeling Object Dissimilarity for Deep Saliency Prediction". *Transactions on Machine Learning Research (TMLR), 2022. [pdf] [project]*.
- Seokju Cho\*, Sunghwan Hong\*, and Seungryong Kim. "CATs++: Boosting Cost Aggregation with Convolutions and Transformers". *IEEE Trans. on Pattern Analysis and Machine Intelligence (TPAMI), 2022. [pdf] [project]*.
- Jungwoo Lim, Myugnhoon Kang, Yuna Hur, Seung Won Jeong, Jinsung Kim, Yoonna Jang, Dongyub Lee, Hyesung Ji, DongHoon Shin, Seungryong Kim, and Heuiseok Lim. "You Truly Understand What I Need : Intellectual and Friendly Dialog Agents grounding Persona and Knowledge". *The Conference on Empirical Methods in Natural Language Processing (EMNLP)- Findings, 2022*.
- Sunghwan Hong, Jisu Nam, Seokju Cho, Susung Hong, Sangryul Jeon, Dongbo Min, and Seungryong Kim. "Neural Matching Fields: Implicit Representation of Matching Fields for Visual Correspondence". *Neural Information Processing Systems (NeurIPS), 2022. [pdf] [project]*.
- Seungjun Lee, Seungjun An, Sunghwan Hong, Seokju Cho, Jisu Nam, Susung Hong, and Seungryong Kim. "Cost Aggregation with Transformers for Sparse Correspondence". *IEEE Conf. on Consumer Electronics Asia (ICCE-Asia), 2022*.
- Yoojin Kim and Seungryong Kim. "Text-Driven In-The-Wild Car Image Manipulation Using Object Localization and Optimized Encoder Inversion". *IEEE Conf. on Consumer Electronics Asia (ICCE-Asia), 2022*.
- Sunok Kim, Seungryong Kim, Dongbo Min, Pascal Frossard, and Kwanghoon Sohn. "Stereo Confidence Estimation via Locally Adaptive Fusion and Knowledge Distillation". *IEEE Trans. on Pattern Analysis and Machine Intelligence (TPAMI), 2022. [pdf]*.
- Matteo Poggi, Seungryong Kim, Fabio Tosi, Sunok Kim, Filippo Aleotti, Dongbo Min, Kwanghoon Sohn, and Stefano Mattoccia. "On the Confidence of Stereo Matching in a Deep-Learning Era: a Quantitative Evaluation". *IEEE Trans. on Pattern Analysis and Machine Intelligence (TPAMI), vol. 44, no. 9, pp. 5293-5313, Sep. 2022. [pdf]*.
- Yunsung Lee\*, Gyuseong Lee\*, Kwangrok Ryoo\*, Hyojun Go\*, Jihye Park\*, and Seungryong Kim. "Towards Flexible Inductive Bias via Progressive Reparameterization Scheduling". *ECCV 2022 Workshop: 3rd Visual Inductive Priors for Data-Efficient Deep Learning Workshop (ECCVW), 2022*.
- Jiwon Kim\*, Youngjo Min\*, Daehwan Kim\*, Gyuseong Lee, Junyoung Seo, Kwangrok Ryoo, and Seungryong Kim. "ConMatch: Semi-Supervised Learning with Confidence-Guided Consistency Regularization". *European Conference on Computer Vision (ECCV), 2022. [pdf] [project]*.
- Sunghwan Hong\*, Seokju Cho\*, Jisu Nam, Stephen Lin, and Seungryong Kim. "Cost Aggregation with 4D Convolutional Swin Transformer for Few-Shot Segmentation". *European Conference on Computer Vision (ECCV), 2022. [pdf] [project]*.
- Mira Kim, Youngjo Min, Jiwon Kim, and Seungryong Kim. "Meta-learned Initialization for 3D Human Recovery". *IEEE International Conference on Image Processing (ICIP), 2022*.
- Jaehoon Cho, Seungryong Kim, and Kwanghoon Sohn. "Memory-guided Image De-raining Using Time-Lapse Data". *IEEE Trans. on Image Processing (TIP), 2022. [pdf]*.
- Soohyun Kim, Jongbeom Baek, Jihye Park, Gyeongnyeon Kim, and Seungryong Kim. "InstaFormer: Instance-Aware Image-to-Image Translation with Transformer". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2022. [pdf] [project]*.
- Jiwon Kim\*, Kwangrok Ryoo\*, Junyoung Seo\*, Gyuseong Lee\*, Daehwan Kim, Hansang Cho, and Seungryong Kim. "Semi-Supervised Learning of Semantic Correspondence with Pseudo-Labels". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2022. [pdf]*.
- Daehwan Kim, Daun Jeong, Hyungmin Kim, Kibong Chong, Seungryong Kim, and Hansang Cho. "Spatial Contrastive Learning for Anomaly Detection and Localization". *IEEE Access, 2022. [pdf]*.
- Jongbeom Baek\*, Gyeongnyeon Kim\*, and Seungryong Kim. "Semi-Supervised Learning with Mutual Distillation for Monocular Depth Estimation". *IEEE International Conference on Robotics and Automation (ICRA), 2022. [pdf]*.
- Seungryong Kim\*, Matteo Poggi\*, Sunok Kim, Kwanghoon Sohn, and Stefano Mattoccia. "Meta-Confidence Estimation for Stereo Matching". *IEEE International Conference on Robotics and Automation (ICRA), 2022*.
- Jiwon Kim, Youngjo Min, Mira Kim, and Seungryong Kim. "Joint Learning of Feature Extraction and Cost Aggregation for Semantic Correspondence". *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), 2022. [pdf]*.
- Sunwoo Kim\*, Soohyun Kim\*, and Seungryong Kim. "Deep Translation Prior: Test-time Training for Photorealistic Style Transfer". *AAAI Conference on Artificial Intelligence (AAAI), 2022. [pdf] [project]*.
- Yoonna Jang\*, Jungwoo Lim\*, Yuna Hur\*, Dongsuk Oh, Suhyune Son, Yeonsoo Lee, Donghoon Shin, Seungryong Kim\*\*, and Heuiseok Lim\*\*. "Call for Customized Conversation: Customized Conversation Grounding Persona and Knowledge". *AAAI Conference on Artificial Intelligence (AAAI), 2022. [pdf]*.

**2021**

- Mira Kim\*, Jaehoon Ko\*, Kyusun Cho, Junmyeong Choi, Daewon Choi, and Seungryong Kim. "AE-NeRF: Auto-Encoding Neural Radiance Fields for 3D-Aware Object Manipulation". **.
- Jiwon Kim\*, Kwangrok Ryoo\*, Gyuseong Lee, Seokju Cho, Junyoung Seo, Daehwan Kim, Hansang Cho, and Seungryong Kim. "AggMatch: Aggregating Pseudo Labels for Semi-Supervised Learning". **.
- Hojoon Lee, Dongyoon Hwang, Sunghwan Hong, Changyeon Kim, Seungryong Kim, and Jaegul Choo. "MOI-Mixer: Improving MLP-Mixer with Multi Order Interactions in Sequential Recommendation". **.
- Sangryul Jeon, Seungryong Kim, Dongbo Min, and Kwanghoon Sohn. "Pyramidal Semantic Correspondence Networks". *IEEE Trans. on Pattern Analysis and Machine Intelligence (TPAMI), 2021. [pdf]*.
- Seokju Cho\*, Sunghwan Hong\*, Sangryul Jeon, Yunsung Lee, Kwanghoon Sohn, and Seungryong Kim. "CATs: Cost Aggregation Transformers for Visual Correspondence". *Neural Information Processing Systems (NeurIPS), 2021. [pdf] [project]*.
- Sunok Kim, Dongbo Min, Seungryong Kim, and Kwanghoon Sohn. "Learning Adversarial Confidence Measures for Robust Stereo Matching". *IEEE Trans. on Intelligent Transportation Systems (TITS), 2021. [pdf]*.
- Sunghwan Hong and Seungryong Kim. "Deep Matching Prior: Test-Time Optimization for Dense Correspondence". *IEEE International Conference on Computer Vision (ICCV), 2021. [pdf] [project]*.
- Sunghun Joung, Seungryong Kim, Minsu Kim, Ig-Jae Kim, and Kwanghoon Sohn. "Learning Canonical 3D Object Representation for Fine-grained Recognition". *IEEE International Conference on Computer Vision (ICCV), 2021. [pdf]*.
- Hyesong Choi, Hansang Lee, Sunkyung Kim, Sunok Kim, Seungryong Kim, Kwanghoon Sohn, and Dongbo Min. "Adaptive Confidence Thresholding for Monocular Depth Estimation". *IEEE International Conference on Computer Vision (ICCV), 2021. [pdf]*.
- Yunsung Lee, Teakgyu Hong, Han-Cheol Cho, Junbum Cha, and Seungryong Kim. "Hough Contrastive Learning: Hough Voting to Find Better Positive Pairs in Dense Self-supervised Representation Learning". *ICML 2021 Workshop: Self-Supervised Learning for Reasoning and Perception (ICMLW), 2021 [pdf]*.
- Seungryong Kim, Dongbo Min, Stephen Lin, and Kwanghoon Sohn. "Dense Cross-Modal Correspondence Estimation with the Deep Self-Correlation Descriptor". *IEEE Trans. on Pattern Analysis and Machine Intelligence (TPAMI), vol. 43, no. 7, pp. 2345-2359, Jul. 2021. [pdf] [project]*.
- Sangryul Jeon, Dongbo Min, Seungryong Kim, and Kwanghoon Sohn. "Mining Better Samples for Contrastive Learning of Temporal Correspondence". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2021. [pdf]*.
- Sungha Choi, Sanghun Jung, Huiwon Yun, Joanne Kim, Seungryong Kim, and Jaegul Choo. "RobustNet: Improving Domain Generalization in Urban-Scene Segmentation via Instance Selective Whitening". *IEEE Conf. Computer Vision Pattern Recognition (CVPR), 2021. (Oral Presentation) [pdf]*.
- Yunsung Lee, Teakgyu Hong, and Seungryong Kim. "Data Augmentations for Document Images". *AAAI Workshop- The AAAI-21 Workshop on Scientific Document Understanding (AAAIW), 2021. [pdf]*.
- Minsu Kim, Sunghun Joung, Seungryong Kim, JungIn Park, Ig-Jae Kim, and Kwanghoon Sohn. "Cross-Domain Grouping and Alignment for Domain Adaptive Semantic Segmentation". *AAAI Conference on Artificial Intelligence (AAAI), 2021. [pdf]*.

## 수상과 소식

- 학생 수상(랩 표기): 구글 PhD 펠로십(2023년 Sunghwan Hong, 2026년 Jisu Nam), 퀄컴 이노베이션 펠로십(2024년 Jisu Nam), 대통령과학장학금(2026년 Hyeonsu Kim), 영상처리·이해 워크숍(IPIU) 금상(2025·2026) 등.[^home]
- 지원(랩 표기): NVIDIA Academic Grant(2026년 1월), Google Research GCP 크레딧(2022·2023년 각 3만 달러).[^home]
- 교수 수상(랩 표기): 대한전자공학회 신호처리소사이어티 젊은연구자상(2022), 고려대 석탑강의상·우수강좌(2021–2024), 교육부장관상(2021) 등.[^faculty][^home]

랩 홈페이지 소식란(원문)은 다음과 같다. 논문 채택, 학생의 해외 인턴·방문 연구, 수상 소식이 실린다.[^home]

- 2026.09 · Our eleven papers were accepted to NeurIPS 2026. Congratulations!
- 2026.09 · Jisu Nam (M.S./Ph.D Integrated Student) received the 2026 Google PhD Fellowship.
- 2026.09 · Junyoung Seo (M.S./Ph.D Integrated Student) started an internship at Meta, Honggyu An (M.S./Ph.D Integrated Student) started an internship at Sony, Jung Yi (M.S. Student) started an internship at Reactor, and Jisoo Kim (Ph.D Student) started an internship at Samsung Research America.
- 2026.09 · Our paper on VLA is accepted to CoRL 2026. Congratulations!
- 2026.08 · Jaewoo Jung (M.S./Ph.D Integrated Student) started an internship at Adobe Research, and Jiho Park (M.S. Student) joined Carnegie Mellon University as a visiting student.
- 2026.07 · Hyunwook Choi (M.S./Ph.D Integrated Student) started an internship at Naver AI Lab, and JinHyeon Kim (Ph.D Student), Hyunkoo Lee (M.S. Student), Seonghu Jeon (M.S. Student), and Tongmin Kim (M.S. Student) started an internship at Maum.AI.
- 2026.06 · Our six papers (1 oral, 1 spotlight, and 4 posters) were accepted to ECCV 2026. Congratulations!
- 2026.06 · Jisu Nam (M.S./Ph.D Integrated Student) started an internship at Meta, and Heeseong Shin (M.S./Ph.D Integrated Student) started an internship at Google DeepMind.
- 2026.05 · Jini Yang (Ph.D Student) joined Queen Mary University of London, and Jaewon Min (M.S./Ph.D Integrated Student) joined NYU as a visiting researcher.
- 2026.05 · Our three papers were accepted to ICML 2026. Congratulations!
- 2026.05 · Siyoon Jin (M.S./Ph.D Integrated Student) started an internship at Naver Labs, Woojeong Jin (M.S. Student) started an internship at Naver Cloud, Chaehyun Kim (M.S./Ph.D Integrated Student) started an internship at NVIDIA, Jisang Han (M.S./Ph.D Integrated Student) started an internship at Google DeepMind, Minkyung Kwon (M.S. Student) started an internship at Naver Labs.
- 2026.04 · Jaewoo Jung (M.S./Ph.D Integrated Student) started an internship at ETHZ, and Sangbeom Lim (M.S./Ph.D Integrated Student) started an internship at Adobe Research.
- 2026.03 · Junyoung Seo (M.S./Ph.D Integrated) started an internship at NVIDIA, and Jisu Nam, Heeseong Shin, Soowon Son, Heeji Yoon, Jiwon Kang, Jiyoung Kim (M.S./Ph.D Integrated), and Jung Yi, Paul Hyunbin Cho (M.S. Student) started an internship at KAKAO, and Wooseok Jang (M.S./Ph.D Integrated) started an internship at MSRA.
- 2026.02 · Our twelve papers (including one Findings) were accepted to CVPR 2026. Congratulations!
- 2026.02 · We received the Gold Award at 2026 Workshop of Image Processing and Image Understanding (IPIU).
- 2026.01 · Our five papers were accepted to ICLR 2026. Congratulations!
- 2026.01 · Seokju Cho (M.S./Ph.D Integrated Student) started an internship at NVIDIA.
- 2026.01 · Hyeonsu Kim (M.S./Ph.D Integrated Student) received the Presidential Science Scholarship (Graduate Track, Top-Ranked Recipient).
- 2026.01 · We received NVIDIA Academic Grant.
- 2025.12 · We released the codes for DiTracker, MATRIX, 3DScenePrompt, UniT, C3G, RobustVGGT, MV-TAP, CAMEO, MoAI, InterRVOS for new arxiv papers.
- 2025.12 · We released the codes for DDUSt3R, HeadHunter, Seg4Diff, DiffTrack for NeurIPS 2025.
- 2025.10 · Chaehyun Kim (M.S./Ph.D Integrated Student) started an internship at Naver Cloud.
- 2025.10 · Prof. Seungryong Kim will serve as a Lead Area Chair for CVPR 2026.
- 2025.09 · Our six papers were accepted to NeurIPS 2025. Congratulations!
- 2025.07 · Prof. Seungryong Kim will deliver tutorial at the International Technical Conference on Circuits/Systems, Computers, and Communications (ITC-CSCC), 2025.
- 2025.06 · Dr. Sunghwan Hong has started his postdoctoral research at ETH Zurich, Switzerland.
- 2025.06 · Our two papers (AM-Adapter, S⁴M) were accepted to ICCV 2025. Congratulations!
- 2025.06 · Prof. Seungryong Kim will deliver keynote speech at the 8th Workshop and Competition on Affective & Behavioral Analysis in-the-wild (ABAW), held at CVPR 2025.
- 2025.05 · Seokju Cho (M.S./Ph.D Integrated Student) started an internship at NVIDIA.
- 2025.05 · Jisu Nam (M.S./Ph.D Integrated Student) and Sangbeom Lim (M.S./Ph.D Integrated Student) started internships at Adobe Research.
- 2025.05 · Jisang Han (M.S./Ph.D Integrated Student) and Wooseok Jang (M.S./Ph.D Integrated Student) started internships at NYU, and Hyeonsu Kim (M.S./Ph.D Integrated Student) started an internship at University of Michigan.
- 2025.05 · Our paper on feed-forward 3D Gaussian splatting was accepted to ICML 2025. Congratulations!
- 2025.04 · Our two CVPR papers (out of seven) have been selected as highlights. Congratulations!
- 2025.03 · Junyoung Seo (M.S./Ph.D Integrated Student) started an internship at Reality Lab, Meta.
- 2025.02 · Our seven papers were accepted to CVPR 2025. Congratulations!
- 2025.02 · Sunghwan Hong (M.S./Ph.D Integrated Student) received the 2024 KU Achievement Award.
- 2025.02 · we received Gold Award, Bronze Award and Two Outstanding Poster Presentation Award at 2025 Workshop of Image Processing and Image Understanding (IPIU).
- 2024.12 · Heeseong Shin (M.S./Ph.D Integrated Student) started an internship at NAVER AI Lab.
- 2024.12 · Prof. Seungryong Kim will serve as an Area Chair for ICML 2025.
- 2024.12 · Our two papers on talking face synthesis and video object segmentation were accepted to AAAI 2025. Congratulations!
- 2024.12 · Jisu Nam (M.S./Ph.D Integrated Student) received the Qualcomm Innovation Fellowship 2024. Congratulations!
- 2024.11 · Our paper on domain generalization was accepted to WACV 2025. Congratulations!
- 2024.09 · Sunghwan Hong (M.S./Ph.D Integrated Student) started an internship at ETHZ.
- 2024.09 · Our two papers were accepted to NeurIPS 2024. Congratulations!
- 2024.09 · Prof. Seungryong Kim will serve as an Area Chair for CVPR 2025 and ICLR 2025.
- 2024.08 · After four and a half wonderful years at Korea University, we moved to the Kim Jaechul Graduate School of AI at KAIST (KAIST 김재철 AI 대학원).
- 2024.07 · Minseop Kwak (M.S./Ph.D Integrated Student) started an internship at NAVER AI Lab.
- 2024.07 · Kyusun Cho (M.S./Ph.D Integrated Student) started an internship at Queen Mary University of London.
- 2024.07 · Our paper on 3D talking face synthesis was accepted to ACM MM 2024. Congratulations!
- 2024.07 · Our paper on learning with noisy labels was accepted to IJCV. Congratulations!
- 2024.07 · Our three papers were accepted to ECCV 2024. Congratulations!
- 2024.06 · Diffusers officially supports our PAG (ECCV'24). Congratulations!
- 2024.06 · Our paper on monocular depth estimation was accepted to IROS 2024. Congratulations!
- 2024.06 · Jisu Nam (M.S./Ph.D Integrated Student) and Seokju Cho (M.S./Ph.D Integrated Student) started an internship at Adobe Research.
- 2024.06 · Our paper on video action detection was accepted to Pattern Recognition. Congratulations!
- 2024.06 · Prof. Seungryong Kim received an outstanding lecture award (우수강좌) at Korea University with COSE474 Deep Learning (2023 Fall) lecture.
- 2024.05 · Our paper on retrieval-augmented Text-to-3D was accepted to ICML 2024. Congratulations!
- 2024.04 · Prof. Seungryong Kim served as a panelist at NSF-NRF Early Career Workshop in ICASSP 2024.
- 2024.04 · Our PAG (Diffusion Sampling Guidance, ECCV'24) has been reimplemented at SD WebUI extension, ComfyUI / SD WebUI Forge node, Diffusers pipeline.
- 2024.04 · Our two CVPR papers (out of four) have been selected as highlights. Congratulations!
- 2024.04 · Our paper on diffusion guidance was accepted to Pattern Recognition (IF: 8.0). Congratulations!
- 2024.03 · Our 3DFuse (Text-to-3D Generative Model, ICLR'24) has been integrated into Threestudio. Congratulations!
- 2024.02 · Seonghoon Park (M.S. Student) received the Outstanding Paper Award (우수논문상) at Korea University. Congratulations!
- 2024.02 · Our four papers (collaboration with Google Research, Adobe Research, Microsoft Research Asia, and NAVER Cloud) were accepted to CVPR 2024. Congratulations!
- 2024.02 · Our paper was accepted to MLSys 2024. Congratulations!
- 2024.01 · Our three (1 oral and 2 poster) papers were accepted to ICLR 2024. Congratulations!
- 2023.12 · Our two papers were accepted to AAAI 2024. Congratulations!
- 2023.12 · Junyoung Seo (M.S./Ph.D Integrated Student) started an internship at Sony Research.
- 2023.12 · Wooseok Jang (M.S./Ph.D Integrated Student) started an internship at NAVER Cloud.
- 2023.11 · Prof. Seungryong Kim received an outstanding lecture award (우수강좌) at Korea University with COSE111 Linear Algebra (2023 Spring) lecture.
- 2023.10 · Sunghwan Hong (M.S./Ph.D Integrated Student) received the 2023 Google PhD Fellowship.
- 2023.09 · Prof. Seungryong Kim will serve as an Area Chair for CVPR 2024.
- 2023.09 · Our two papers were accepted to NeurIPS 2023. Congratulations!
- 2023.09 · Our paper on style transfer was accepted to Pattern Recognition (IF: 8.0). Congratulations!
- 2023.07 · Our paper on self-attention guidance for diffusion model was accepted to ICCV 2023. Congratulations!
- 2023.06 · Our paper on image-to-image translation was accepted to IJCV (IF: 13.369). Congratulations!
- 2023.06 · Prof. Seungryong Kim will serve as an Area Chair for NeurIPS 2023.
- 2023.06 · Junyoung Seo (M.S./Ph.D Integrated Student) started an internship at Queen Mary University of London.
- 2023.06 · Seokju Cho (M.S./Ph.D Integrated Student) started an internship at Adobe Research.
- 2023.05 · Jisu Nam (M.S./Ph.D Integrated Student) started an internship at NAVER Cloud.
- 2023.05 · Prof. Seungryong Kim received the best lecture award (석탑강의상) at Korea University with COSE474 Deep Learning (2022 Fall) lecture.
- 2023.05 · We received GCP Credit Award ($30,000) by Google Research.
- 2023.04 · Our paper on few-shot NeRF was accepted to ICML 2023. Congratulations!
- 2023.02 · Our two papers were accepted to CVPR 2023. Congratulations!
- 2023.02 · Jiuhn Song (M.S. Student) and Minseop Kwak (M.S./Ph.D Integrated Student) received Prize at Outstanding Poster Presentation Award in 2023 Workshop of Image Processing and Image Understanding (IPIU).
- 2022.12 · Prof. Seungryong Kim served as an Program Chair for Korea AI Summit 2022.
- 2022.12 · Prof. Seungryong Kim received the best lecture award (석탑강의상) at Korea University with COSE111 Linear Algebra (2022 Spring) lecture.
- 2022.12 · Our paper on exemplar-based image translation was accepted to AAAI 2023. Congratulations!
- 2022.11 · Our paper on saliency prediction was accepted to TMLR. Congratulations!
- 2022.10 · Sunghwan Hong (M.S./Ph.D Integrated Student) started an internship at Microsoft Research Asia (MSRA).
- 2022.10 · Our paper on visual correspondence was accepted to IEEE TPAMI (IF: 24.314).
- 2022.10 · We co-organized The 1st Workshop on Customized Chat Grounding Persona and Knowledge at COLING 2022.
- 2022.10 · Our paper on 3D GAN inversion was accepted to WACV 2023.
- 2022.09 · Prof. Seungryong Kim received Outstanding Young Researcher Award from Signal Processing Society of IEIE.
- 2022.09 · Susung Hong (Research Intern), Gyuseong Lee (M.S. Student), and Wooseok Jang (M.S. Student) received Outstanding Paper Award in 2022 Signal Processing Joint Conference of IEIE.
- 2022.09 · Our paper on neural matching fields was accepted to NeurIPS 2022.
- 2022.09 · Prof. Seungryong Kim will serve as an Area Chair for CVPR 2023.
- 2022.09 · Our paper on stereo confidence estimation was accepted to IEEE TPAMI (IF: 24.314).
- 2022.09 · We started a joint collaboration project with Google Research, "Relational Language-Driven Zero-Shot Segmentation".
- 2022.09 · Kwangrok Ryoo (M.S. Student) started an internship at LG AI LAB.
- 2022.07 · Prof. Seungryong Kim was interviewed by EIRIC- link.
- 2022.07 · Our two papers were accepted to ECCV 2022.
- 2022.07 · Mira Kim (M.S. Student) started an internship at Korea Institute of Science and Technology (KIST).
- 2022.06 · Soohyun Kim (M.S. Student) started an internship at NAVER AI LAB.
- 2022.06 · Kwangrok Ryoo (M.S. Student) received Outstanding Paper Award by NAVER in Summer Annual Conference of IEIE, 2022.
- 2022.06 · We started a joint collaboration project with Microsoft Research Asia (MSRA), "Language-Driven Image-to-Video Generation with Generative Neural Radiance Fields".
- 2022.06 · Our one paper was accepted to ICIP 2022.
- 2022.06 · Jiwon Kim (M.S. Student) and Sunwoo Kim (M.S./Ph.D Integrated Student) started an internship at NAVER AI LAB.
- 2022.05 · Our paper on image deraining was accepted to IEEE TIP (IF: 10.856).
- 2022.05 · We received GCP Credit Award ($30,000) by Google Research.
- 2022.04 · Prof. Seungryong Kim will serve as an Area Chair for 3DV 2022.
- 2022.03 · Our two papers were accepted to CVPR 2022.
- 2022.02 · Soohyun Kim (M.S. Student) and Jihye Park (M.S./Ph.D Integrated Student) received Silver Prize at Outstanding Paper Award in 2022 Workshop of Image Processing and Image Understanding (IPIU).
- 2022.02 · Sunghwan Hong (M.S./Ph.D Integrated Student) received BK21 Future Talent Fellowship (BK21 미래인재 펠로우십).
- 2022.01 · Our two papers were accepted to ICRA 2022.
- 2022.01 · Our one paper was accepted to ICASSP 2022.
- 2021.12 · Our two papers were accepted to AAAI 2022.
- 2021.11 · Prof. Seungryong Kim received an outstanding lecture award (우수강좌) at Korea University with COSE111 Linear Algebra (2021 Spring) lecture.
- 2021.10 · Our paper on semantic correspondence was accepted to IEEE TPAMI (IF: 17.861).
- 2021.09 · Our paper on semantic correspondence was accepted to NeurIPS 2021.
- 2021.07 · Our three papers were accepted to ICCV 2021.
- 2021.04 · Prof. Seungryong Kim received an outstanding lecture award (우수강좌) at Korea University with COSE474 Deep Learning (2020 Fall) lecture.
- 2021.03 · Our paper on stereo confidence estimation was accepted to IEEE TPAMI (IF: 17.861).
- 2021.03 · Our two papers were accepted to CVPR 2021.
- 2021.02 · Prof. Seungryong Kim presented at Korean Computer Vision Forum.
- 2021.01 · Prof. Seungryong Kim received an award certification by Korean Ministry of Education (교육부 장관상).

교수 페이지의 수상 목록(원문)은 다음과 같다.[^faculty]

- Outstanding Lecture Award, Korea University, 2021, 2022, 2023
- Silver, Bronze Prize, Outstanding Paper Award, Workshop of Image Processing and Image Understanding (IPIU), 2024
- Outstanding Poster Presentation Award, Workshop of Image Processing and Image Understanding (IPIU), 2023
- Outstanding Young Researcher Award, Signal Processing Society of IEIE, 2022
- Outstanding Paper Award, Signal Processing Joint Conference of IEIE, 2022.
- Outstanding Paper Award, NAVER Award in Summer Annual Conference of IEIE, 2022.
- Silver Prize, Outstanding Paper Award, Workshop of Image Processing and Image Understanding (IPIU), 2022
- Outstanding Lecture Aware at Korea University, 2021, 2022
- Award Certification by Korean Ministry of Education, 2021
- Chun-Gang Outstanding Research Award, Chun-Gang Memorial Foundation, 2018
- Doctoral Consortium Award, IEEE ICCV, 2017
- Honorable Mention Award, Outstanding Research Award, Yonsei University, 2017
- Microsoft Research Asia Fellowship Nomination Award, 2016
- Runner-up Award, Hackatone Competition, HYUNDAI Motor Group, 2016
- Bronze Award, IEEE Student Paper Contest, IEEE Seoul Section, 2012
- Volunteer Award, IEEE Broadcast Technology Society, 2012
- Honor Graduation Award, Yonsei University, 2012
- Best Award, COEX 2011 Capstone Design Symposium, 2011
- Best Award, Capstone Design Symposium, Korea University, 2011
- Best Award, Creative Research Competition, Yonsei University, 2011

## 연락과 위치

- 이메일: seungryong.kim@kaist.ac.kr[^faculty]
- 소속: KAIST 김재철AI대학원(서울)[^faculty]

[^home]: 랩 첫 화면(연구 관심·소식) <https://cvlab.kaist.ac.kr/> (2026-10-19 열람)
[^faculty]: 랩 교수 페이지 <https://cvlab.kaist.ac.kr/members/faculty> (2026-10-19 열람)
[^students]: 랩 학생 페이지 <https://cvlab.kaist.ac.kr/members/students> (2026-10-19 열람)
[^papers]: 랩 논문 목록 <https://cvlab.kaist.ac.kr/publication> (2026-10-19 열람)
[^p1]: D. Chung 외, S. Kim, "Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction", 2026년 랩 게시. 랩 프로젝트 페이지 <https://cvlab-kaist.github.io/ME-World/> 게시 초록 기준.
[^p2]: J. Yi 외, S. Kim, "Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression", ICML 2026(랩 표기). arXiv:2512.05081 <https://arxiv.org/abs/2512.05081> 초록 기준(arXiv 판).
[^p3]: H. An 외, S. Kim, "C3G: Learning Compact 3D Representations with 2K Gaussians", CVPR 2026(랩 표기). arXiv:2512.04021 <https://arxiv.org/abs/2512.04021> 초록 기준(arXiv 판).
[^p4]: J. H. Kim 외, S. Kim, "GARD: Geometry-Aware Representation Denoising for Robust Multi-view 3D Reconstruction", NeurIPS 2026(랩 표기). arXiv:2605.26230 <https://arxiv.org/abs/2605.26230> 초록 기준(arXiv 판).
[^p5]: J. Nam 외, S. Kim, "Emergent Temporal Correspondences from Video Diffusion Transformers", NeurIPS 2025(랩 표기). arXiv:2506.17220 <https://arxiv.org/abs/2506.17220> 초록 기준(arXiv 판).
[^p6]: H. Yoon 외, S. Kim, "VIRAL: Visual Representation Alignment for Multimodal Large Language Models", ICLR 2026 워크숍(랩 표기). arXiv:2509.07979 <https://arxiv.org/abs/2509.07979> 초록 기준(arXiv 판).
[^p7]: W. Jin 외, S. Kim, "InterRVOS: Interaction-aware Referring Video Object Segmentation", CVPR 2026(랩 표기). 랩 프로젝트 페이지 <https://cvlab-kaist.github.io/InterRVOS/> 게시 초록 기준.
[^p8]: J. Kim 외, S. Kim, "Better Source, Better Flow: Learning Condition-Dependent Source Distribution for Flow Matching", NeurIPS 2026(랩 표기). arXiv:2602.05951 <https://arxiv.org/abs/2602.05951> 초록 기준(arXiv 판).

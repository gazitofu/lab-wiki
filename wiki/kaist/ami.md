# 기계 지능 연구실 (Advanced Machine Intelligence Lab, AMI Lab)

**KAIST 전산학부·메타버스대학원 · 오태현 부교수**

- 분야: 시각·언어·소리의 통합 이해, 사람과 공간의 3차원 복원, 아바타와 소리 생성, 데이터 효율 학습
- 대분야: 컴퓨팅·AI
- 태그: 컴퓨터 비전[^about], 멀티모달 AI[^home], 생성 인공지능[^p3][^p4], 3차원 복원·인식[^p4][^p5], 컴퓨터 그래픽스·기하 처리[^p4][^p5], 디지털 휴먼·아바타[^p4]
- 홈페이지: <https://ami.kaist.ac.kr/>
- 근거와 출처: [기계 지능 연구실 근거 페이지](ami-sources.md)

> 사진·영상·소리·글을 함께 이해하고, 그 정보로 사람과 공간을 입체로 복원하거나 새 영상·소리를 만드는 기계 지능을 연구한다.[^home][^about]

## 무엇을 연구하나

오태현 부교수가 이끄는 AMI Lab은 사람의 지각 능력을 이해해 기계가 현실 세계를 알아보는 능력을 개발하는 연구실이다. 연구실은 컴퓨터 비전(사진·영상에서 대상과 장면에 관한 정보를 알아내는 분야)과 기계 학습(자료에서 규칙이나 입출력 관계를 배우는 계산 방법)을 연구하며, 감지와 효율적인 학습을 중요한 기반으로 본다. 사람과 기계를 연결하는 사람 중심 연구를 우선한다고 소개한다.[^about]

연구 계획은 세 축을 제시한다. 첫째는 시각을 중심에 둔 멀티모달 지각(영상·소리·글처럼 종류가 다른 자료를 함께 이용해 대상을 이해하는 일)이다. 소리와 영상, 시각과 언어를 함께 이해하고 다른 센서의 자료도 결합한다. 둘째는 공간과 물리 정보를 이해하는 체화 에이전트(환경을 감지하고 행동하는 몸이나 장치를 가진 인공지능)다. 사람과 장면의 입체 표현을 만들며 이해하는 접근을 든다. 셋째는 합성 데이터 생성(계산으로 학습·평가 자료를 만드는 일)이다.[^home]

최근 논문은 이러한 방향을 구체적인 문제로 나눈다. 이미지에서 질문에 필요한 부분을 보더라도 정답을 내지 못하는 문제, 사용자의 관심에 맞게 이미지 검색 기준을 바꾸는 문제, 물체의 움직임과 물리 정보를 반영해 영상에 소리를 붙이는 문제를 다룬다.[^p1][^p2][^p3] 또 영상에서 머리 아바타(사람의 머리 모습과 움직임을 컴퓨터 속에 재현한 표현)를 만들고, 장면의 밝기와 움직임을 복원하며, 새로운 시점의 영상을 만들어 공간에 관한 질문에 답하는 연구를 한다.[^p4][^p5][^p6]

이 연구들에는 이미 배운 모델을 활용하는 방법이 자주 등장한다. 사전 학습(다른 과제에 활용할 바탕을 미리 자료로 학습하는 과정)을 거친 모델에서 필요한 정보를 꺼내거나, 추론(학습된 모델에 입력을 주어 출력을 계산하는 과정) 중 정보 전달을 바꾸는 방식이다.[^p1][^p2] 신경망(연결된 계산 단위와 가중치로 입출력 관계를 나타내는 모형)의 학습 설정을 찾는 비용과, 생성 모델(자료가 나타나는 양상을 배워 새 자료를 만드는 모형)로 복원 문제를 풀 때의 안정성도 연구한다.[^p7][^p8]

## 주요 연구 주제

### 시각·언어 이해와 조건부 검색

비전-언어 모델(Vision-Language Model, VLM)은 이미지와 글을 함께 처리하는 모델이다. AIF(Adaptive Information Flow, 적응형 정보 흐름) 연구는 질문과 무관한 이미지 부분에 정보 처리가 쏠리는 현상을 살피고, 답을 계산하는 도중 시각 토큰(모델이 이미지 정보를 나누어 처리하는 단위)의 중요도를 판단해 정보 흐름을 조절한다. 시각 질의응답, 물체 위치 찾기, 글자 읽기 등의 과제에서 성능 개선을 보고했다.[^p1]

CLAY는 임베딩(대상의 성질과 관계를 수치 벡터로 표현하는 방법) 공간에서 글로 지정한 조건에 따라 이미지 사이 유사도를 계산한다. 이미 계산한 이미지 표현을 유지하면서 조건을 주는 과정과 이미지 정보를 뽑는 과정을 분리하며, 추가 학습 없이 여러 조건을 반영한 검색을 수행한다. 연구진은 조건부 검색을 평가할 합성 자료 CLAY-EVAL도 만들었다.[^p2]

### 영상과 소리를 연결하는 생성

PAVAS(Physics-Aware Video-to-Audio Synthesis, 물리 정보를 반영한 영상 기반 소리 생성)는 영상에서 소리를 만드는 Video-to-Audio 생성에 물리 정보를 반영한다. 물체의 질량과 속도에 관한 추정 정보를 확산 모델(자료에 잡음을 더하는 과정과 그 역방향 확률 과정을 배워 자료를 만드는 모형)에 전달하는 구성 요소를 제안했다. 연구진은 물체 간 상호작용에 관한 평가 자료와 물리 속성·소리 속성의 일관성을 재는 지표를 만들고, 생성한 소리가 물리 조건에 맞는지를 평가했다.[^p3]

연구실의 다른 최근 소식은 소리로 시각 장면을 만드는 Sound2Vision, 소리가 나는 대상의 위치와 관계를 함께 추론하는 연구, 움직이는 음원의 시간·공간 정보를 언어 모델과 연결하는 연구를 소개한다. 모두 소리나 영상 한 종류의 자료만 다루는 데서 나아가 서로 다른 신호가 제공하는 정보를 연결하는 문제다.[^nijcv][^nneurips][^nemnlp]

### 사람·공간의 입체 복원과 시점 추론

ELITE는 단일 카메라 영상으로 움직일 수 있는 머리 아바타를 만든다. 3차원 가우시안 스플래팅(위치·모양·투명도를 가진 정규 분포를 모아 입체 장면을 그리는 방법) 표현을 빠르게 초기화하고, 실제 영상과 합성 영상을 이용해 입력 대상에 맞춘다. 영상 생성 모델을 이용한 보정으로 관측 영상에서 빠진 외형 정보를 채운다.[^p4]

HDR-NSFF(High Dynamic Range Neural Scene Flow Fields)는 밝고 어두운 부분의 범위가 넓은 HDR(High Dynamic Range) 영상을 공간과 시간의 연속적인 표현으로 복원한다. 노출을 바꿔 촬영한 단일 카메라 영상에서 장면의 밝기·모양·움직임을 함께 모델링하고, 새로운 시점과 시각의 영상을 만드는 문제를 다룬다.[^p5] SplatReasoner는 공간 질문에 필요한 관측을 찾아 새로운 시점의 영상을 합성한다. 기존 관측에서 가려졌거나 화면 밖에 있던 증거를 드러내어 장면 추론과 대상의 입체 위치 찾기를 돕는다.[^p6]

### 효율적인 학습과 생성 모델의 안정화

LoRA(Low-Rank Adaptation)는 모델 전체를 다시 학습하는 대신 일부 행렬의 변화량을 낮은 차원의 곱으로 표현해 조정하는 방법이다. 관련 논문은 학습 전에 정하는 하이퍼파라미터(학습률이나 모델 구성처럼 학습 절차를 정하는 설정)를 찾기 위해 언어 모델의 지식을 활용한다. 베이지안 최적화(관측 자료로 확률 모형을 갱신하며 다음 탐색 지점을 고르는 방법)를 수행할 공간에 설정과 그 관계를 옮기고, 일부 학습 자료로 평가하는 방식도 사용한다.[^p7]

MCLC(Measurement-Consistent Langevin Corrector)는 측정 자료로 원래 대상을 추정하는 역문제를 풀 때 확산 모델의 계산을 안정시키는 보정 모듈이다. 잠재 공간(자료의 특징을 벡터로 나타내는 내부 표현 공간)에서 문제를 푸는 계산과 모델이 배운 역방향 확산 과정의 차이를 분석하고, 측정 자료와의 일관성을 반영하는 갱신을 제안한다. 생성 모델을 복원에 이용할 때 계산이 불안정해지는 문제를 다룬다는 점에서 학습 설정 탐색과 구별된다.[^p8]

## 대표 논문

KAIST 재직 시기에 공개된 논문 중 연구 갈래를 나누어 볼 수 있고 초록이 공개된 8편이다. 학회와 연도는 연구실 목록 표기이며, 아래 설명은 같은 제목의 arXiv 사전 공개본 초록을 근거로 썼다. 각주의 온라인 날짜는 arXiv 최초 제출일이다. 저자 역할은 전체 저자 목록의 순서이며 교신저자 역할을 뜻하지 않는다.[^piprofile][^pubs]

| 번호 | 연도 | 논문·학회 | 쉽게 말하면 | 교수 역할 |
|---|---|---|---|---|
| 1 | 2026 | Aligning What Vision-Language Models See and Perceive with Adaptive Information Flow · CVPR 2026 | 이미지의 알맞은 부분을 찾고도 틀린 답을 하는 원인을 모델 내부 정보 흐름에서 분석했다. 답을 만드는 단계마다 활성화 양상이 달라지는 시각 토큰을 중요하게 보고, 무관한 이미지 영역의 간섭을 줄이는 방법을 제안했다. 여러 시각 질의응답·위치 찾기·계수·글자 읽기 과제에서 기존 모델의 성능이 향상됐다.[^p1] | 마지막 저자 |
| 2 | 2026 | CLAY: Conditional Visual Similarity Modulation in Vision-Language Embedding Space · CVPR 2026 | 사용자가 무엇을 중요하게 보는지에 따라 이미지의 유사도를 바꾸는 방법이다. 미리 학습한 시각·언어 표현을 추가 학습 없이 글 조건에 맞춘 유사도 공간으로 사용한다. 조건 처리와 이미지 특징 추출을 분리했으며, 조건부 검색 평가 자료를 만들어 정확도와 계산 효율을 평가했다.[^p2] | 마지막 저자 |
| 3 | 2026 | PAVAS: Physics-Aware Video-to-Audio Synthesis · CVPR 2026 | 영상 속 대상의 겉모습과 소리 사이의 관계에 더해 물리 정보를 소리 생성에 넣었다. 시각·언어 모델로 질량을 추정하고 입체 움직임 복원으로 속도 정보를 얻어 소리 생성 모델에 전달한다. 물체 간 상호작용 평가 자료와 물리·청각 속성의 일관성 지표를 제안했고, 기존 방법보다 물리적으로 타당하고 지각적으로 일관된 소리를 보고했다.[^p3] | 5명 중 4번째 저자 |
| 4 | 2026 | ELITE: Efficient Gaussian Head Avatar from a Monocular Video via Learned Initialization and TEst-time Generative Adaptation · CVPR 2026 | 한 대의 카메라로 찍은 영상에서 움직이는 머리 아바타를 만든다. 입체 자료에서 배운 초기 표현과 이미지 생성 모델의 정보를 함께 활용하고, 실제·합성 영상으로 입력 대상에 맞춘다. 아바타를 그린 결과를 바탕으로 한 단계의 생성 보정을 수행해 빠진 외형 정보를 복원한다. 연구진은 여러 표정에서 아바타 품질과 생성 속도를 평가했다.[^p4] | 마지막 저자 |
| 5 | 2026 | HDR-NSFF: High Dynamic Range Neural Scene Flow Fields · ICLR 2026 | 노출을 번갈아 바꾼 단일 카메라 영상에서 밝기 범위가 넓은 움직이는 장면을 복원한다. 화면끼리 합치는 대신 공간·시간에 따른 밝기, 형태, 움직임을 함께 나타낸다. 관측이 부족하거나 밝기가 포화되어 잃은 정보는 생성 모델의 사전 지식으로 보완하며, 실제 촬영 평가 자료에서 새 시점·시각의 영상 합성을 검증했다.[^p5] | 마지막 저자 |
| 6 | 2026 | SplatReasoner: Enhancing Embodied Reasoning and Grounding by Novel View Synthesis · ECCV 2026 | 공간에 관한 질문에 답하는 데 필요한 시점을 새로 만들어 보는 방법이다. 질문과 관련된 기존 관측을 찾고 입체 장면 표현에서 질문에 맞는 영상을 합성한다. 고정된 시점의 기억이나 언어 정보를 입힌 입체 표현만 쓰는 비교 방법보다 장면 추론과 대상의 입체 위치 찾기가 개선됐다.[^p6] | 마지막 저자 |
| 7 | 2026 | A Language-Guided Bayesian Optimization for Efficient LoRA Hyperparameter Search · ICML 2026 | 언어 모델을 조정하는 학습 설정을 찾을 때, 언어 모델이 아는 설정의 역할과 관계를 활용한다. 이를 글로 설명해 연속적인 수치 공간으로 옮긴 뒤 탐색하고, 글로 표현하기 어려운 정보는 추가 학습 요소로 보충한다. 전체 자료 대신 일부 자료로 학습·평가하는 방식도 이용해 탐색 효율을 높였다.[^p7] | 마지막 저자 |
| 8 | 2026 | Measurement-Consistent Langevin Corrector for Stabilizing Latent Diffusion Inverse Problem Solvers · ICML 2026 | 생성 모델을 이용해 측정 자료에서 원래 대상을 복원할 때 계산이 불안정해지는 문제를 다뤘다. 문제 풀이의 계산과 모델이 배운 역방향 확산 과정 사이의 차이를 줄이면 안정성이 좋아짐을 분석했다. 이를 바탕으로 측정 자료와의 일관성을 반영하는 갱신을 기존 문제 풀이에 덧붙이는 모듈을 제안했다.[^p8] | 마지막 저자 |

## 교수와 전문 분야

오태현(Tae-Hyun Oh)은 KAIST 전산학부 부교수이며, 메타버스대학원 교수진에는 Joint로 올라 있다. 교수 상세는 2025년부터 KAIST 전산학부 부교수라고 소개한다. 이전 POSTECH 전기전자공학과에서 2020년 조교수로 부임하고 2023년 부교수가 됐으며, 2021–2023년 POSCO-RIST 오픈랩 연구소장을 겸했다. 2017년 KAIST 전기전자공학부에서 박사 학위를 받았으며, MIT CSAIL과 Facebook AI Research에서 박사후연구원으로 일했다.[^piprofile][^prof][^metaprof]

전산학부가 적은 전문 분야는 컴퓨터 비전, 머신 러닝, 컴퓨터 그래픽스, 데이터 시각화다. 최근 관심사는 생성형 기계 지각 시스템과 알고리즘, 멀티모달 학습에 걸쳐 있다. 학술 활동으로 CVPR·ICCV·NeurIPS·ICLR·ACCV의 Area Chair, AAAI의 Senior program chair와 IJCV·ICRA의 Associate Editor 활동을 소개한다.[^prof] 대표 논문에서 드러나는 전문 분야는 시각·언어 모델의 정보 처리와 검색, 소리·영상 생성, 사람·공간의 입체 표현, 학습과 복원의 효율·안정화다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

연구에서 직접 다루는 쓰임은 글로 조건을 지정하는 이미지 검색, 영상의 물리 정보를 반영한 소리 생성, 단일 카메라 영상에서 움직이는 머리 아바타 만들기, 노출이 다른 영상에서 입체 장면을 복원해 새로운 시점의 영상을 그리기다.[^p2][^p3][^p4][^p5] 공간 질문에 맞는 관측을 생성해 체화 에이전트의 장면 이해를 돕는 연구도 수행한다.[^p6]

## 구성원

2026년 10월 26일 Members의 현재 연구 구성원 28명이다. 박사후연구원 1명, 박사과정 7명, 석박사통합과정 9명, 석사과정 11명이며 과정과 주제는 연구실 표기다. Kyeongseon Ella Kim은 연구실 대표로 적혀 있다. 대표 논문 참여는 전체 저자 목록에서 이름을 대조한 번호이며, 같은 이름과 이름 순서만 다른 표기를 같은 사람으로 보았다.[^members]

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Chengxin Liu | 박사후연구원 | Visual Perception; Data-efficient Learning; Multi-modal Learning | 1 |
| Kwon Byung-Ki | 박사과정 | Synthetic Data Generation; Meta Learning; Motion Understanding; LiDAR | 5 |
| Kim Youwang | 석박사통합과정 | Digital Twins; World Models; Generative Models | 4 |
| Kim Sung-Bin | 박사과정 | Multi-modal Learning; Generative Models | 7 |
| Kim Jun-Seong | 석박사통합과정 | 3D Reconstruction | 5, 6 |
| Kim Ji-Yeon | 석박사통합과정 | 3D Mesh Reconstruction; 3D Human & Scene Interaction |  |
| Hyunwoo Ha | 박사과정 | Embodied AI |  |
| Kim Yu-Ji | 석박사통합과정 | 3D Scene Understanding; Embodied AI; 3D Reconstruction | 6 |
| Oh Hyun-Bin | 석박사통합과정 | Multi-modal Learning; Audio-visual; Video Understanding; Motion Understanding | 3 |
| Wonjun Jo | 석박사통합과정 | Embodied AI; Self-supervised Learning; Multi-modal Learning; Robot Learning |  |
| Kyeongseon Ella Kim (Lab representative) | 박사과정 | Multi-modal Learning; Data Issues in Deep Learning |  |
| GeonU Kim | 석박사통합과정 | 3D Reconstruction; Generative Models | 6 |
| Wonseok Choi | 석박사통합과정 | Synthetic Data Generation; Data-efficient Learning; Meta Learning; Multi-modal Learning; Generative Models | 1 |
| Dahye Lee | 석박사통합과정 | Generative Models; 3D Reconstruction | 6 |
| Shin Dong-Yeon | 박사과정 | 3D/4D Reconstruction; 3D Content Creation | 5 |
| Lee Jung-Mok | 박사과정 | Multi-modal Learning; Agent System; XAI | 7 |
| Baek Seong-Eun | 박사과정 | Video Understanding; Embodied AI; Multi-modal Learning | 7 |
| Sohwi Lim | 석사과정 | Multi-modal Learning; Generative Models | 2, 8 |
| Kim Ohn | 석사과정 | 3D Scene Understanding; Embodied AI |  |
| Joohyun Chang | 석사과정 | Multi-modal Learning; Video Understanding; Audio-visual |  |
| Jin-Woo Kong | 석사과정 | 3D Reconstruction; 3D Scene Understanding; Neural Rendering |  |
| Minsung Kim | 석사과정 | Multi-modal Learning; Synthetic Data Generation; Visual Perception |  |
| Kim Hyung-Min | 석사과정 | 3D Human & Scene Interaction; 3D Human Motion; Embodied AI |  |
| Hyeyeon Kim | 석사과정 | Multi-modal Learning; Audio-visual; 3D Human & Scene Interaction |  |
| Yohan Park | 석사과정 | 3D Scene Understanding; Vision-Language Planning; Policy Learning; Agent System |  |
| Jiyeon Son | 석사과정 | Agent System; Multi-modal Learning |  |
| Yejin Yeo | 석사과정 | Multi-modal Learning; Agent System |  |
| Subin Park | 석사과정 | 3D Human Reconstruction; 3D Reconstruction; 3D Talking Head; Generative Models | 4 |

## 졸업생과 이전 구성원

Members의 박사 졸업 2개, 석사 졸업 12개, Visiting 20개 항목이다. 2020–2026년 학위·방문·이전 구성원 기록이며 같은 사람이 학위나 역할별로 다시 등장한다. 오태현 교수의 KAIST 부임 전 POSTECH 시절 구성원과 진로도 함께 실려 있다.[^members][^prof]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Moon Ye-Bin | Ph.D. (2026.08) |  |
| Nam Hyeon Woo | Ph.D. (2026.08) | Qualcomm as researcher |
| Baek Seong-Eun | MS (2026.08) | KAIST as Ph.D. student |
| Shin Dong-Yeon | MS (2026.02) | KAIST as Ph.D. student |
| Lee Jung-Mok | MS (2026.02) | KAIST as Ph.D. student |
| Lee Chae-Yeon | MS (2026.02) | Seoul Nat’l Univ. as Ph.D. student |
| Han EunGi | MS (2025.08) | Krafton as research engineer |
| Lee Hyoseok | MS (2025.08) | NC AI as research engineer |
| Lee Hyun | MS (2024) | Samsung Advanced Institute of Technology (SAIT) as research engineer |
| Hyunwoo Ha | MS (2023) | POSTECH as Ph.D. student |
| Kim Sung-Bin | MS (2023) | POSTECH as Ph.D. student |
| Kwon Byung-Ki | MS (2023) | POSTECH as Ph.D. student |
| Moon Ye-Bin | MS (2022) | POSTECH as Ph.D. student |
| Nam Hyeon-Woo | MS (2022) | POSTECH as Ph.D. student |
| Youngmi Jin | Research Professor (2026) |  |
| Chenshuang Zhang | Postdoc (2026) |  |
| Jungjoon Park | Postdoc (2026) | IBS Center as researcher |
| Junuk Cha | Postdoc (2026) |  |
| Sungnyun Kim | Postdoc (2026) | KAIST AI as postdoctoral researcher |
| Inmo Yeon | Postdoc (2025) | ETRI as senior researcher |
| Seungmin Lee | Undergrad. Intern (2024-2025) |  |
| Kim Yewon | Researcher (2024) | UNIST as Ph.D. student |
| Corentin Nivelet Etcheberry | Visiting M.S. student (2024) | Bordeaux INP as M.S. student |
| Avilasha Mandal | Undergrad. (Foreign) Intern (2024) | IIT Delhi as undergrad. student |
| Do Huu Dat | Undergrad. (Foreign) Intern (2024) | Vin Univ. as undergrad. student |
| Lee Chae-Yeon | Researcher (2023) | Seoul Nat’l Univ. as researcher |
| Jisoo Kim | Undergrad. Intern (2023) | Columbia Univ. as master student |
| Lee Hyun | Researcher (2022) | Samsung Advanced Institute of Technology (SAIT) |
| Kim Ji-Yun | Researcher (2022) | Krafton as infra engineer |
| Han Byeol-Yi | Visiting Ph.D. student (2021) | Georgia Tech as Ph.D. student |
| Kim Sung-Bin | Researcher (2021) | POSTECH as Ph.D. student |
| Junhyeong Cho | Undergrad. Intern (2021) | Cornell Univ. as Ph.D. student |
| Jieun Lee | Postdoc (2020) | KERIS as researcher |
| Kyungdon Joo | Postdoc (2020) | UNIST as assistant professor |

## 최근 논문 목록 (2021–2026)

영상·소리·언어의 이해와 생성, 사람과 공간의 입체 복원, 효율적 학습에 관한 논문 목록이다. 국제 학회·학술지·워크숍·사전 공개본 123개와 국내 학회·학술지 54개를 합한 177개 항목이다. 2021–2026년 연도 구역을 따르며, 오태현 교수의 2025년 KAIST 부임 이전 POSTECH 시절 논문과 부임 연도의 논문이 함께 있다. 학회·학술지명과 연도는 연구실 표기이며 arXiv preprint는 사전 공개본이다. 연구실 소식에서 채택을 확인한 학회 항목은 채택으로 표시했다. 저자 뒤 기호와 그 의미를 적은 괄호는 연구실 표기다.[^pubs][^domestic][^prof]

**2026**

- Kim Sung-Bin, Lee Jung-Mok, Jinwoo Jung, Oh Hyun-Bin, Hyeonggon Ryu, David Harwath, Tae-Hyun Oh. "Hear, Localize, and Reason: Spatially Aware Scene Understanding for Audio-visual LLMs". *NeurIPS 2026 (채택)*.
- Kim Sung-Bin, Joohyun Chang, David Harwath, Tae-Hyun Oh. "FacEDiT: Unified Talking Face Editing and Generation via Facial Motion Infilling". *NeurIPS 2026 (채택)*.
- Kwon Byung-Ki, Sohwi Lim, Nam Hyeon-Woo, Moon Ye-Bin, Tae-Hyun Oh. "Early Failure Detection and Intervention in Video Diffusion Models". *NeurIPS 2026 (채택)*.
- Jin-Woo Kong, GeonU Kim, Tae-Hyun Oh. "Assessing Inter-Object Reflection Consistency for Photorealistic Virtual 3D Object Insertion". *SIGGRAPH Asia Posters 2026 (채택)*.
- Kyeongseon Kim\*, Jiyeon Son\*, Tae-Hyun Oh. "IGG: A Benchmark for Interactive GUI Grounding under Visibility Constraints". *EMNLP 2026 (채택)*.
- Oh Hyun-Bin, Kazuki Shimada, Yuhta Takida, Kim Sung-Bin, Toshimitsu Uesaka, Takashi Shibuya, Kyeongyoon Lee, Tae-Hyun Oh†, Yuki Mitsufuji†. "Spatio-Temporal Audio Language Modeling for Dynamic Sound Sources". *EMNLP 2026 (채택)*.
- Junwoo Kim, Hyunuk Kim, Hyun-Bin Oh, Jeonggoo Kang†, Tae-Hyun Oh†, Seungmoon Choi†. "CineHaptic: Context-Aware Real-Time Audiovisual-to-Haptic Rendering System for In-Vehicle 4D Cinematic Experiences". *The ACM Symposium on User Interface Software and Technology (UIST) 2026*.
- Kim Yu-Ji, Dahye Lee, Kim Jun-Seong, Nam Hyeon-Woo, GeonU Kim, Yongjin Kwon, Yu-Chiang Frank Wang, Jaesung Choe, Tae-Hyun Oh. "SplatReasoner: Enhancing Embodied Reasoning and Grounding by Novel View Synthesis". *European Conference on Computer Vision (ECCV) 2026*.
- GeonU Kim, Shin Dong-Yeon, Tae-Hyun Oh. "Reflection-aware Generative Novel View Synthesis". *European Conference on Computer Vision (ECCV) 2026*.
- Kim Jun-Seong, Tae-Hyun Oh, Eduardo Pérez-Pellitero, Youngkyoon Jang. "SA-ResGS: Self-Augmented Residual 3D Gaussian Splatting for Next Best View Selection". *European Conference on Computer Vision (ECCV) 2026*.
- Kyeongrae Kim, Kim Sung-Bin, Oh Hyun-Bin, Tae-Hyun Oh. "Physics-Aware Deepfake Detection via Distance–Speech Consistency". *INTERSPEECH 2026*.
- Baek Seong-Eun, Lee Jung-Mok, Kim Sung-Bin, Tae-Hyun Oh. "A Language-Guided Bayesian Optimization for Efficient LoRA Hyperparameter Search". *International Conference on Machine Learning (ICML) 2026*.
- Lee Hyoseok, Sohwi Lim, Eunju Cha, Tae-Hyun Oh. "Measurement-Consistent Langevin Corrector for Stabilizing Latent Diffusion Inverse Problem Solvers". *International Conference on Machine Learning (ICML) 2026*.
- Nam Hyeon-Woo, Moon Ye-Bin, Sohwi Lim, Kwon Byung-Ki, Tae-Hyun Oh. "Zero-Shot Rankability: Revealing Latent Ordinal Structure in Multimodal Large Language Models via Language". *International Conference on Machine Learning (ICML) 2026*.
- Lee Jung-Mok, Kim Sung-Bin, Joohyun Chang, Lee Hyun, Tae-Hyun Oh. "SMILE-Next: Teaching Large Language Models to Detect, Classify, and Reason about Laughter". *Annual Meetings of the Association for Computational Linguistics (ACL) 2026*.
- Chenshuang Zhang, Kyeong Seon Kim, Chengxin Liu, Tae-Hyun Oh. "SVHalluc: Benchmarking Speech–Vision Hallucination in Audio-Visual Large Language Models". *IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2026*.
- Oh Hyun-Bin, Yuhta Takida, Toshimitsu Uesaka, Tae-Hyun Oh, Yuki Mitsufuji. "PAVAS: Physics-Aware Video-to-Audio Synthesis". *IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2026*.
- Chengxin Liu, Wonseok Choi, Chenshuang Zhang, Tae-Hyun Oh. "Aligning What Vision-Language Models See and Perceive with Adaptive Information Flow". *IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2026*.
- Sohwi Lim, Lee Hyoseok, Jungjoon Park, Tae-Hyun Oh. "CLAY: Conditional Visual Similarity Modulation in Vision-Language Embedding Space". *IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2026*.
- Arda Senocak\*, Sooyoung Park\*, Tae-Hyun Oh, Joon Son Chung. "How Far Can We Go With Synthetic Data for Audio-Visual Sound Source Localization?". *IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2026*.
- Kim Youwang, Lee Hyoseok, Park Subin, Gerard Pons-Moll, Tae-Hyun Oh. "ELITE: Efficient Gaussian Head Avatar from a Monocular Video via Learned Initialization and TEst-time Generative Adaptation". *IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2026*.
- Shin Dong-Yeon, Kim Jun-Seong, Kwon Byung-Ki, Tae-Hyun Oh. "HDR-NSFF: High Dynamic Range Neural Scene Flow Fields". *International Conference on Learning Representations (ICLR) 2026*.
- Wonseok Choi, Sohwi Lim, Nam Hyeon-Woo, Moon Ye-Bin, Dong-ju Jeong, Jinyoung Hwang, Tae-Hyun Oh. "Patch-wise Retrieval: A Bag of Practical Techniques for Instance-level Matching". *Winter Conference on Applications of Computer Vision (WACV) 2026*.
- Jaehun Bang, Moon Ye-Bin, Kyungdon Joo, Tae-Hyun Oh. "Beyond the Highlights: Video Retrieval with Salient and Surrounding Contexts". *Winter Conference on Applications of Computer Vision (WACV) 2026*.
- Kyeongseon Kim, Baek Seong-Eun, Lee Jung-Mok, Tae-Hyun Oh. "Training-free Multimodal Embedding for Structure-Aware Retrieval of Scalable Vector Graphics and Images". *Winter Conference on Applications of Computer Vision (WACV) 2026*.
- Moon Ye-Bin, Roy Miles, Tae-Hyun Oh, Ismail Elezi, Jiankang Deng. "RetouchLLM: Training-free Code-based Image Retouching with Vision Language Models". *arXiv preprint*.
- Moon Ye-Bin, Nam Hyeon-Woo, Baek Seong-Eun, Yejin Yeo, Tae-Hyun Oh. "TRAP: Benchmark for Task-completion and Resistance to Active Privacy-extraction". *arXiv preprint*.
- Kim Youwang, Zhengyu Yang, Liuhao Ge, Yu Rong, Timur Bagautdinov, Su Zhaoen, Nir Sopher, Jovan Popović, Teng Deng, Tae-Hyun Oh, Chen Cao. "FiCA: Feed-forward instant Gaussian Codec Avatars from a Single Portrait Image". *arXiv preprint*.
- Kim Youwang, Jon Hasselgren, Peter Kocsis, Andrea Weidlich, Tae-Hyun Oh, Jacob Munkberg. "Extracting Neural Materials from Multi-view Images". *arXiv preprint*.
- Chengxin Liu, Moon Ye-Bin, Tae-Hyun Oh. "When GUI Grounding Fails: Entropy-Based Analysis and Training-Free Refinement". *International Conference on Machine Learning Workshop (ICMLW) 2026 (Workshop on Compositional Learning: Safety, Interpretability, and Agents)*.
- Moon Ye-Bin, Jiyeon Son, Tae-Hyun Oh. "Spatially Stable GUI Grounding via Zoom Consistency Loss". *International Conference on Machine Learning Workshop (ICMLW) 2026 (Workshop on Compositional Learning: Safety, Interpretability, and Agents)*.
- Nam Hyeon-Woo, Tae-Hyun Oh, Zeynep Akata, Stephan Alaniz. "From Numbers to Narratives: Goal-Oriented Summarization of Machine Learning Model Differences". *International Conference on Machine Learning Workshop (ICMLW) 2026 (Workshop on Compositional Learning: Safety, Interpretability, and Agents)*.
- Joohyun Chang, Minsung Kim, Kim Sung-Bin, Chenshuang Zhang, Tae-Hyun Oh. "SMART: Selective Multimodal Aggregation and Refinement over Time for Video Summarization". *International Conference on Machine Learning Workshop (ICMLW) 2026 (Workshop on SCALE: Scalable Learning and Optimization for Efficient Multimodal AI Agents)*.
- Nam Hyeon-Woo, Yoonsu Kim, Kihoon Son, Juho Kim, Tae-Hyun Oh. "Hypothesize and Verify: Natural-Language Explanations of Vision Model Errors". *Transactions on Machine Learning Research (TMLR)*.
- Hyunwoo Ha\*, Oh Hyun-Bin\*, Kim Jun-Seong, Kwon Byung-Ki, Kim Sung-Bin, Linh-Tam Tran, Ji-Yun Kim, Sung-Ho Bae, Tae-Hyun Oh. "Revisiting Learning-based Video Motion Magnification for Real-time Processing". *Transactions on Machine Learning Research (TMLR), 2026*.
- Kim Youwang\*, Taehyun Byun\*, Kim Ji-Yeon, Sungjoon Choi, Tae-Hyun Oh. "CLIP-Actor-X: Text-driven 4D Human Avatar Generation via Cross-modal Synthesis-through-Optimization". *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 2026*.
- GeonU Kim, Kim Youwang, Lee Hyoseok, Tae-Hyun Oh. "FPGS: Feed-Forward Semantic-aware Photorealistic Style Transfer of Large-Scale Gaussian Splatting". *International Journal of Computer Vision (IJCV) 2026*.
- Kim Sung-Bin, Arda Senocak, Hyunwoo Ha, Tae-Hyun Oh. "Sound2Vision: Generating Diverse Visuals from Audio through Cross-modal Latent Alignment". *International Journal of Computer Vision (IJCV), 2026*.
- Yohan Park, Hyunwoo Ha, Wonjun Jo, Tae-Hyun Oh. "저조도 체화 환경에서의 시각 질의응답 성능 분석". *KICS Summer Conference 2026*.
- Joohyun Chang, Minsung Kim, Kim Sung-Bin, Chenshuang Zhang, Wonpyo Hong, Yeonsu Lee, Tae-Hyun Oh. "비디오 요약을 위한 선택적 다중모달 집계 및 시간적 정제 프레임워크". *KICS Summer Conference 2026*.
- Yejin Yeo, Baek Seong-Eun, Shin Dong-Yeon, Lee Jung-Mok, Tae-Hyun Oh. "질문 맞춤형 관광 가이드 에이전트를 위한 GPS-aware 랜드마크 인식 및 도구 증강 설명 생성". *Summer Annual Conference of The Institute of Electronics and Information Engineers (IEIE) 2026*.
- Kim Hyung-Min, Junuk Cha, Kim Ji-Yeon, Tae-Hyun Oh. "서로 다른 휴먼 모션 간 자연스러운 연결을 위한 프레임워크". *Summer Annual Conference of The Institute of Electronics and Information Engineers (IEIE) 2026*.
- Yejin Yeo, Baek Seong-Eun, Lee Jung-Mok, Shin Dong-Yeon, Tae-Hyun Oh. "A Simple yet Effective Defense Against Typographic Attacks". *Workshop on Image Processing and Image Understanding (IPIU) 2026*.
- Kim Ohn, Kim Youwang, Junuk Cha, Tae-Hyun Oh. "Self-supervised Robot Pose Estimation In-the-Wild via Differentiable Robot Appearance Modeling". *Workshop on Image Processing and Image Understanding (IPIU) 2026*.
- Joohyun Chang, Lee Jung-Mok, Kim Sung-Bin, Inmo Yeon, Wonpyo Hong, Sanghyun Park, Tae-Hyun Oh. "HENS: Hard and Easy Negative Sampling for Noisy-Label Laughter Detection". *Workshop on Image Processing and Image Understanding (IPIU) 2026*.
- Yohan Park, Hyunwoo Ha, Tae-Hyun Oh. "장면 메모리를 활용한 체화 에이전트용 깊이맵 기반 시맨틱 레이블 전이 시스템". *Workshop on Image Processing and Image Understanding (IPIU) 2026*.
- Kim Hyung-Min, Kim Ji-Yeon, Tae-Hyun Oh. "Shape-Aware Discrete Motion Modeling for 3D Human–Object Interaction". *Workshop on Image Processing and Image Understanding (IPIU) 2026*.
- Sohwi Lim, Lee Hyoseok, Jungjoon Park, Tae-Hyun Oh. "시각-언어 모델을 활용한 조건부 시각적 유사도 변조". *Workshop on Image Processing and Image Understanding (IPIU) 2026*.
- Daeen Kabir, Kim Yu-Ji, Tae-Hyun Oh. "Training-Free Consistent Novel View Synthesis: A Reimplementation of 3D Epipolar Attention". *Workshop on Image Processing and Image Understanding (IPIU) 2026*.

**2025**

- Lee Jung-Mok, Nam Hyeon-Woo, Moon Ye-Bin, Junhyun Nam, Tae-Hyun Oh. "Automated Model Discovery via Multi-modal & Multi-step Pipeline". *Conference on Neural Information Processing Systems (NeurIPS) 2025*.
- Lee Chae-Yeon, Nam Hyeon-Woo, Tae-Hyun Oh. "Learning Correlation-aware Aleatoric Uncertainty for 3D Hand Pose Estimation". *British Machine Vision Conference (BMVC) 2025*.
- Jeongsoo Choi, Ji-Hoon Kim, Kim Sung-Bin, Tae-Hyun Oh, Joon Son Chung. "AlignDiT: Multimodal Aligned Diffusion Transformer for Synchronized Speech Generation". *ACM International Conference on Multimedia (MM) 2025*.
- Kwon Byung-Ki, Qi Dai, Lee Hyoseok, Chong Luo, Tae-Hyun Oh. "JointDiT: Enhancing RGB-Depth Joint Modeling with Diffusion Transformers". *IEEE International Conference on Computer Vision (ICCV) 2025*.
- Kim Sung-Bin, Jeongsoo Choi, Puyuan Peng, Joon Son Chung, Tae-Hyun Oh, David Harwath. "VoiceCraft-Dub: Automated Video Dubbing with Neural Codec Language Models". *IEEE International Conference on Computer Vision (ICCV) 2025*.
- Do Huu Dat, Nam Hyeon-Woo, Po-Yuan Mao, Tae-Hyun Oh. "VSC: Visual Search Compositional Text-to-Image Diffusion Model". *IEEE International Conference on Computer Vision (ICCV) 2025*.
- Jungbin Cho, Junwan Kim, Jisoo Kim, Minseo Kim, Mingu Kang, Sungeun Hong, Tae Hyun Oh, Youngjae Yu. "DisCoRD: Discrete Tokens to Continuous Motion via Rectified Flow Decoding". *IEEE International Conference on Computer Vision (ICCV) 2025*.
- Kim Jun-Seong, GeonU Kim, Kim Yu-Ji, Yu-Chiang Frank Wang, Jaesung Choe, Tae-Hyun Oh. "Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration". *IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2025*.
- Lee Chae-Yeon\*, Oh Hyun-Bin\*, Han EunGi, Kim Sung-Bin, Suekyeong Nam, Tae-Hyun Oh. "Perceptually Accurate 3D Talking Head Generation: New Definitions, Speech-Mesh Representation, and Evaluation Metrics". *IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2025*.
- Junhyeong Cho, Kim Youwang, Hunmin Yang, Tae-Hyun Oh. "Robust 3D Shape Reconstruction in Zero-Shot from a Single Image in the Wild". *IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2025*.
- Kim Sung-Bin\*, Oh Hyun-Bin\*, JungMok Lee, Arda Senocak, Joon Son Chung, Tae-Hyun Oh. "AVHBench: A Cross-Modal Hallucination Benchmark for Audio-Visual Large Language Models". *International Conference on Learning Representations (ICLR) 2025*.
- Lee Hyoseok, Kyeong Seon Kim, Kwon Byung-Ki, Tae-Hyun Oh. "Zero-shot Depth Completion via Test-time Alignment with Affine-invariant Depth Prior". *AAAI Conference on Artificial Intelligence (AAAI) 2025*.
- Kim Sung-Bin, Kim Jun-Seong, Junseok Ko, Yewon Kim, Tae-Hyun Oh. "SoundBrush: Sound as a Brush for Visual Scene Editing". *AAAI Conference on Artificial Intelligence (AAAI) 2025*.
- (Workshop on Wild3D: 3D Modeling, Reconstruction, and Generation in the Wild) Wonjun Jo, Hyunwoo Ha, Kim Ji-Yeon, Hawook Jeong, Tae-Hyun Oh. "Self-Supervised Collaborative Distillation: Enhancing Lighting Robustness and 3D Awareness". *IEEE International Conference on Computer Vision Workshop (ICCVW) 2025*.
- Baek Seong-Eun, Nam Hyeon-Woo, Lee Jung-Mok, Tae-Hyun Oh. "ViMP : Visual Motion Prompting". *IEEE International Conference on Computer Vision Workshop (ICCVW) 2025 (Workshop on SVU: Short-Form Video Understanding)*.
- Kim Youwang, Lee Hyoseok, Gerard Pons-Moll, Tae-Hyun Oh. "Dress-up: Generating Animatable Clothed 3D Humans via Latent Modeling of 3D Gaussian Texture Maps". *IEEE International Conference on Computer Vision Workshop (ICCVW) 2025 (Workshop on Computer Vision for Fashion, Art, and Design)*.
- Dahye Lee, Kim Yu-Ji, GeonU Kim, Jaesung Choe, Tae-Hyun Oh. "Text-Embedded 3DGS as Enhanced Language Embeddings". *IEEE International Conference on Computer Vision Workshop (ICCVW) 2025 (Workshop on Open-World 3D Scene Understanding with Foundation Models (OpenSUN3D))*.
- Arda Senocak, Hyeonggon Ryu, Junsik Kim, Tae-Hyun Oh, Hanspeter Pfister, Joon Son Chung. "Toward Interactive Sound Source Localization: Better Align Sight and Sound!". *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 2025*.
- Kim Jun-Seong\*, Mingyu Kim\*, GeonU Kim, Tae-Hyun Oh†, Jin-Hwa Kim† \* Presented in IEEE International Conference on Robotics and Automation (ICRA), 2025. "Factorized Multi-Resolution HashGrid for Efficient Neural Radiance Fields: Execution on Edge-Devices". *IEEE Robotics and Automation Letters (RA-L)*.
- Moon Ye-Bin\*, Nam Hyeon-Woo\*, Wonseok Choi, Nayeong Kim, Suha Kwak, Tae-Hyun Oh. "SYNAuG: Exploiting Synthetic Data for Data Imbalance Problems". *Pattern Recognition Letters (PRL), 2025*.
- Nam Hyeon-Woo, Moon Ye-Bin, Wonseok Choi, Lee Hyun, Tae-Hyun Oh. "VLM’s Eye Examination: Instruct and Inspect Visual Competency of Vision Language Models". *Transactions on Machine Learning Research (TMLR), 2025*.
- Chunsan Hong, Tae-Hyun Oh\*, Minhyuk Sung\*. "MemBench: Memorized Image Trigger Prompt Dataset for Diffusion Models". *Transactions on Machine Learning Research (TMLR), 2025*.
- Muhamad Dwisnanto Putro, Agung Sutrisno, Indri Shelovita Manembu, Il Yong Chun, Tae-Hyun Oh. "STAR: Sea Turtle Basic Activity Recognizer Network Via Efficient Transformer". *IEEE Access, 2025*.
- Dahye Lee, Kim Yu-Ji, GeonU Kim, Jaesung Choe, Tae-Hyun Oh. "Text-Embedded 3DGS as Enhanced Language Embeddings". *Autumn Annual Conference of The Institute of Electronics and Information Engineers (IEIE) 2025*.
- Jin Woo Kong, GeonU Kim, Tae-Hyun Oh. "A Benchmark for Virtual Object Insertion Considering Reflections from Nearby Objects". *Autumn Annual Conference of The Institute of Electronics and Information Engineers (IEIE) 2025*.
- GeonU Kim, Kim Youwang, Lee Hyoseok, Tae-Hyun Oh. "장면의 의미론적 정보를 이용한 Gaussian Splatting 기반 실사적 스타일화 기법". *Summer Annual Conference of The Institute of Electronics and Information Engineers (IEIE) 2025*.
- Sohwi Lim, Lee Hyoseok, Tae-Hyun Oh. "Controllable Image Retrieval with text condition via Vision-Language Models". *Summer Annual Conference of The Institute of Electronics and Information Engineers (IEIE) 2025*.
- Jisu Jeon, Hyunwoo Ha, Tae-Hyun Oh. "Reimplementation of 3D-aware Stable Diffusion via Novel View Synthesis". *Workshop on Image Processing and Image Understanding (IPIU) 2025*.
- Lee Jung-Mok, Nam Hyeon-Woo, Moon Ye-Bin, Tae-Hyun Oh. "Discovering Interpretable Model for Time-Series with Vision-Language Models". *Workshop on Image Processing and Image Understanding (IPIU) 2025*.
- Shin Dong-Yeon, Kim Jun-Seong, Kwon Byung-Ki, Tae-Hyun Oh. "HDR-NSFF: High Dynamic Range Neural Scene Flow Fields". *Workshop on Image Processing and Image Understanding (IPIU) 2025*.
- Kyeongseon Kim, Tae-Hyun Oh. "VEGAS: Vector Graphics Automatic-generation System with Visual Question Drawing (VQD)". *Workshop on Image Processing and Image Understanding (IPIU) 2025*.
- Lee Chae-Yeon, Oh Hyun-Bin, Han EunGi, Kim Sung-Bin, Suekyeong Nam, Tae-Hyun Oh. "지각적으로 정확한 3D 토킹 헤드 생성을 위한 정의, 동기화된 음성-메쉬 표현, 및 평가 지표". *Workshop on Image Processing and Image Understanding (IPIU) 2025*.
- Wonseok Choi, Lee Jung-Mok, Tae-Hyun Oh. "GOAT: Goal-Oriented Adaptive Token pruning for Large Vision-Language Models". *Workshop on Image Processing and Image Understanding (IPIU) 2025*.
- Baek Seong-Eun, Nam Hyeon-Woo, Tae-Hyun Oh. "Can Red Arrow Enhance Fine-Grained Video Understanding?". *Workshop on Image Processing and Image Understanding (IPIU) 2025*.
- Baek Seong-Eun, Moon Ye-Bin, Nam Hyeon-Woo, Tae-Hyun Oh. "교통사고 예방을 위한 검색 증강 생성(RAG) 시스템". *Korea Robotics Society Annual Conference (KRoC) 2025*.
- Lee Hyoseok, Kyeong Seon Kim, Kwon Byung-Ki, Tae-Hyun Oh. "Generalizable Depth Completion via Test-time Alignment with Affine-invariant Depth Prior". *Korea Robotics Society Annual Conference (KRoC) 2025*.

**2024**

- Wonjun Jo, Kwon Byung-Ki, Kim Ji-Yeon, Hawook Jeong, Kyungdon Joo, Tae-Hyun Oh. "The Devil is in the Details: Simple Remedies for Image-to-LiDAR Representation Learning". *Asian Conference on Computer Vision (ACCV), 2024*.
- Kim Yu-Ji, Hyunwoo Ha, Kim Youwang, Jaeheung Surh, Hyowon Ha†, Tae-Hyun Oh† († corresponding authors). "MeTTA: Single-View to 3D Textured Mesh Reconstruction with Test-Time Adaptation". *British Machine Vision Conference (BMVC) 2024*.
- Kwon Byung-Ki, Oh Hyun-Bin, Kim Jun-Seong, Hyunwoo Ha, Tae-Hyun Oh. "Learning-based Axial Video Motion Magnification". *European Conference on Computer Vision (ECCV) 2024*.
- Moon Ye-Bin\*, Nam Hyeon-Woo\*, Wonseok Choi, Tae-Hyun Oh (\*equal contribution). "BEAF: Observing Before-AFter Changes to Evaluate Hallucination in Vision-language Models". *European Conference on Computer Vision (ECCV) 2024*.
- Kim Sung-Bin\*, Lee Chae-Yeon\*, Gihun Son\*, Oh Hyun-Bin, Janghoon Ju, Suekyeong Nam, Tae-Hyun Oh (\*equal contribution). "MultiTalk: Enhancing 3D Talking Head Generation Across Languages with Multilingual Video Dataset". *INTERSPEECH 2024*.
- Han EunGi\*, Oh Hyun-Bin\*, Kim Sung-Bin, Corentin Nivelet Etcheberry, Suekyeong Nam, Janghoon Ju, Tae-Hyun Oh (\*equal contribution). "Enhancing Speech-Driven 3D Facial Animation with Audio-Visual Guidance from Lip Reading Expert". *INTERSPEECH 2024*.
- Lee Hyun\*, Kim Sung-Bin\*, Seungju Han, Youngjae Yu, Tae-Hyun Oh (\*equal contribution). "SMILE: Multimodal Dataset for Understanding Laughter in Video with Language Models". *Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL) Findings 2024*.
- Kim Youwang, Tae-Hyun Oh, Gerard Pons-Moll. "🎨 Paint-it: Text-to-Texture Synthesis via Deep Convolutional Texture Map Optimization and Physically-Based Rendering". *IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2024*.
- Chunsan Hong, ByungHee Cha, Tae-Hyun Oh. "CAS: A Probability-Based Approach for Universal Condition Alignment Score". *International Conference on Learning Representations (ICLR) 2024*.
- Hansam Cho, Jonghyun Lee, Seoung Bum Kim, Tae-Hyun Oh\*, Yonghyun Jeong\*. "Noise Map Guidance: Inversion with Spatial Context for Real Image Editing". *International Conference on Learning Representations (ICLR) 2024*.
- GeonU Kim, Kim Youwang, Tae-Hyun Oh. "FPRF: Feed-Forward Photorealistic Style Transfer of Large-Scale 3D Neural Radiance Fields". *AAAI Conference on Artificial Intelligence (AAAI) 2024*.
- Kim Sung-Bin, Lee Hyun, Da hye Hong, Suekyeong Nam, Janghoon Ju, Tae-Hyun Oh. "LaughTalk: Expressive 3D Talking Head Generation with Laughter". *IEEE Winter Conference on Applications of Computer Vision (WACV) 2024*.
- Junhyeong Cho, Kim Youwang, Hunmin Yang, Tae-Hyun Oh. "Object-Centric Domain Randomization for 3D Shape Reconstruction in the Wild". *IEEE Conference on Computer Vision and Pattern Recognition Workshop (CVPRW) 2024 (Workshop on Foundation Models)*.
- Muhamad Dwisnanto Putro, Dirko Ruindungan, Tae-Hyun Oh, Ilyong Chun, Syahputra Rendy, Vecky Poekoel. "An Efficient and Effective Sea Turtle Detection Using Positioning Enhancement Module". *The International Workshop on Intelligent Systems 2024*.
- Beichen Li, Bolei Deng, Wan Shou, Tae-Hyun Oh, Yuanming Hu, Yiyue Luo, Liang Shi, Wojciech Matusik. "Computational Discovery of Microstructured Composites with Optimal Strength-Toughness Trade-Offs". *Science Advances, 2024*.
- Kim Youwang, Lee Hyun\*, Kim Sung-Bin\*, Suekyeong Nam, Janghoon Ju, Tae-Hyun Oh. "A Large-Scale 3D Face Mesh Video Dataset via Neural Re-parameterized Optimization". *Transactions on Machine Learning Research (TMLR)*.
- Kim Ji-Yeon, Oh Hyun-Bin, Kwon Byung-Ki, Dahun Kim, Yongjin Kwon, Tae-Hyun Oh. "Uni-DVPS: Unified Model for Depth-Aware Video Panoptic Segmentation". *IEEE Robotics and Automation Letters (RA-L)*.
- Boeun Kim, Jungho Kim, Hyung Jin Chang, Tae-Hyun Oh. "A Unified Framework for Unsupervised Action Learning via Global-to-local Motion Transformer". *Pattern Recognition, 2024*.
- Dong-Jin Kim, Tae-Hyun Oh, Jinsoo Choi, In So Kweon. "Semi-Supervised Image Captioning by Adversarially Propagating Labeled Data". *IEEE Access, 2024*.
- Jae-Min Park, Won-Jun Jang, Tae-Hyun Oh, Si-Hyeon Lee. "Overcoming Client Data Deficiency in Federated Learning by Exploiting Unlabeled Data on the Server". *IEEE Access, 2024*.
- Kwon Byung-Ki, Kim Sung-Bin, Tae-Hyun Oh. "The Devil in the Details: Simple and Effective Optical Flow Synthetic Data Generation". *The Visual Computer, 2024*.
- Moon Ye-bin, Tae-Hyun Oh. "Label Efficient Learning Methods for Computer Vision Applications". *IEIE Transactions on Smart Processing & Computing (TSPC), 2024 (Invited paper)*.
- Moon Ye-Bin, Dongmin Choi, Yongjin Kwon, Junsik Kim, Tae-Hyun Oh. "ENInst: Enhancing Weakly-supervised Low-shot Instance Segmentation". *Pattern Recognition (PR), 2024*.
- Kim Youwang, Tae-Hyun Oh. "Text-to-4D Avatar 생성의 발전과 그 응용". *[Journal] 전자공학회 학회지 2024*.
- Nam Hyeon-Woo\*, Moon Ye-Bin\*, Wonseok Choi, Lee Hyun, Tae-Hyun Oh (\*equal contribution). "Evaluation of Vision Language Models on Matching Problems". *Workshop on Image Processing and Image Understanding (IPIU) 2024*.
- Lee Hyoseok, Kim Jun-Seong, Kim Ji-Yeon, Tae-Hyun Oh. "Feature Embedded 3D Gaussians for 3D Cognitive Map". *Workshop on Image Processing and Image Understanding (IPIU) 2024*.
- GeonU Kim, Kim Youwang, Tae-Hyun Oh. "이중 Neural Feature Field를 이용한 대규모 3D 장면 Feed-forward Photorealistic Style Transfer". *Workshop on Image Processing and Image Understanding (IPIU) 2024*.
- Chang-Yeon Kim\*, Seung-min Lee\*, Ye-rin So\*, GeonU Kim, Tae-Hyun Oh (\*equal contribution). "Mask-NeRF2NeRF: Editing 3D Scenes with Text-guided Masks". *Workshop on Image Processing and Image Understanding (IPIU) 2024*.
- Han EunGi, Kim Sung-Bin, Lee Hyun, Kim Youwang, Tae-Hyun Oh. "3D Face Mesh Reconstruction with Transformer". *Workshop on Image Processing and Image Understanding (IPIU) 2024*.
- Kim Yu-Ji, Hyunwoo Ha, Kim Youwang, Jaeheung Surh, Hyowon Ha†, Tae-Hyun Oh† (†corresponding authors). "단일 이미지로부터 3차원 텍스처 메시 복원". *Korea Robotics Society Annual Conference (KRoC) 2024*.
- Kim Sung-Bin, Lee Hyun, Da Hye Hong, Suekyeong Nam, Janghoon Ju, Tae-Hyun Oh. "사용자 조작이 가능한 3차원 토킹 헤드 아바타 생성". *Korea Robotics Society Annual Conference (KRoC) 2024*.
- Kim Ji-Yeon, Oh Hyun-Bin, Kwon Byung-Ki, Dahun Kim, Youngjin Kwon, Tae-Hyun Oh. "통합적 장면 이해를 위한 깊이 기반 비디오 전역 분할 모델". *Korea Robotics Society Annual Conference (KRoC) 2024*.

**2023**

- Moon Ye-bin, Jisoo Kim, Hongyeob Kim, Kilho Son, Tae-Hyun Oh. "TextManiA: Enriching Visual Feature by Text-driven Manifold Augmentation". *IEEE International Conference on Computer Vision (ICCV) 2023*.
- Nam Hyeon-Woo, Kim Yu-Ji, Byeongho Heo, Dongyoon Han, Seong Joon Oh, Tae-Hyun Oh. "Scratching Visual Transformer's Back with Uniform Attention". *IEEE International Conference on Computer Vision (ICCV) 2023*.
- Arda Senocak, Hyeonggon Ryu, Junsik Kim, Tae-Hyun Oh, Hanspeter Pfister, Joon Son Chung. "Sound Source Localization is All about Cross-Modal Alignment". *IEEE International Conference on Computer Vision (ICCV) 2023*.
- Kim Sung-Bin, Arda Senocak, Hyunwoo Ha, Andrew Owens, Tae-Hyun Oh. "Sound to Visual Scene Generation by Audio-to-Visual Latent Alignment". *IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2023*.
- Kwon Byung-Ki, Nam Hyeon-Woo, Kim Ji-Yun, Tae-Hyun Oh. "DFlow: Learning to Synthesize Better Optical Flow Datasets via a Differentiable Pipeline". *International Conference on Learning Representations (ICLR) 2023*.
- Haena Song, Jongho Yoon, Dohun Kim, Eunji Kwon, Tae-Hyun Oh, Seokhyeong Kang. "FPGA-Based Accelerator for Rank-Enhanced and Highly-Pruned Block-Circulant Neural Networks". *Design Automation and Test in Europe (DATE) 2023*.
- Byeolyi Han, Tae-Hyun Oh. "Learning Few-shot Segmentation from Bounding Box Annotations". *IEEE Winter Conference on Applications of Computer Vision (WACV) 2023*.
- Arda Senocak, Junsik Kim, Tae-Hyun Oh, Dingzeyu Li, In So Kweon. "Event-Specific Audio-Visual Fusion Layers: A Simple and New Perspective on Video Understanding". *IEEE Winter Conference on Applications of Computer Vision (WACV) 2023*.
- Minkyu Kim\*, Kim Sung-Bin\*, Tae-Hyun Oh (\*equal contribution). "Prefix Tuning for Automated Audio Captioning". *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP) 2023*.
- Seongyeon Park\*, Myungseo Song\*, Bohyung Kim, Tae-Hyun Oh. "Unsupervised Pre-training for Data-Efficient Text-to-Speech on Low Resource Languages". *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP) 2023*.
- Seongyeon Park, Bohyung Kim, Tae-Hyun Oh. "Automatic Tuning of Loss Trade-offs without Hyper-parameter Search in End-to-End Zero-Shot Speech Synthesis". *Interspeech 2023*.
- Hyunwoo Ha, Tae-Hyun Oh. "Mask-KLT: Sub-pixel Accurate Directional Motion Estimation by Stripe Masking". *IEEE International Conference on Visual Communications and Image Processing (VCIP) 2023*.
- Kim Youwang, Tae-Hyun Oh. "Text-driven Human Avatar Generation by Neural Re-parameterized Texture Optimization". *IEEE International Conference on Computer Vision Workshop (ICCV workshop) 2023 (Workshop on AI for 3D Content Creation)*.
- Lee Hyun, Kim Sung-Bin, Seungju Han, Yougjae Yu, Tae-Hyun Oh. "Multimodal Laughter Reasoning with Language Models". *IEEE International Conference on Computer Vision Workshop (ICCV workshop) 2023 (Workshop on Multi-Modal Foundation Models)*.
- Moon Ye-Bin\*, Nam Hyeon-Woo\*, Wonseok Choi, Nayeong Kim, Suha Kwak, Tae-Hyun Oh. "Exploiting Synthetic Data for Data Imbalance Problems: Baselines from a Data Perspective". *IEEE International Conference on Computer Vision Workshop (ICCV workshop) 2023 (Workshop on Multi-Modal Foundation Models)*.
- Chunsan Hong, ByungHee Cha, Bohyung Kim, Tae-Hyun Oh. "Enhancing Classification Accuracy on Limited Data via Unconditional GAN". *IEEE International Conference on Computer Vision Workshop (ICCV workshop) 2023 (Workshop on Representation Learning with Very Limited Images)*.
- Kim Youwang, Lee Hyun\*, Kim Sung-Bin\*, Suekyeong Nam, Janghoon Ju, Tae-Hyun Oh. "Spatio-Temporally Consistent Face Mesh Reconstruction on Videos". *IEEE Conference on Computer Vision and Pattern Recognition Workshop (CVPR workshop) 2023 (Workshop on 3DMV: Learning 3D with Multi-View Supervision)*.
- Hyunwoo Ha\*, Oh Hyun-Bin\*, Kim Jun-Seong, Kwon Byung-Ki, Kim Sung-Bin, Ji-Yun Kim, Sung-Ho Bae, Tae-Hyun Oh. "Revisiting Deep Video Motion Magnification for Real-time applications". *IEEE Conference on Computer Vision and Pattern Recognition Workshop (CVPR workshop) 2023 (Workshop on Vision-based InduStrial InspectiON)*.
- Kim Ji-Yeon, Oh Hyun-Bin, Dahun Kim, Tae-Hyun Oh. "MinDVPS: Minimal Model for Depth-aware Video Panoptic Segmentation". *IEEE Conference on Computer Vision and Pattern Recognition Workshop (CVPR workshop) 2023 (Workshop on Vision Centric Autonomous Driving)*.
- Minkyung Kim, Jongmin Yu, Junsik Kim, Tae-Hyun Oh, Jun Kyun Choi. "An Iterative Method for Unsupervised Robust Anomaly Detection under Data Contamination". *IEEE Transactions on Neural Networks and Learning Systems (TNNLS), 2023*.
- Dong Hun Ryou, Kim Youwang, Tae-Hyun Oh. "Multi-stage Adaptive Rank Statistic Pruning for Lightweight Human 3D Mesh Recovery Model". *The Visual Computer Journal (TVCJ), Springer, 2023*.
- Jinsoo Choi, Tae-Hyun Oh. "Joint Video Super-Resolution and Frame Interpolation via Permutation Invariance". *Sensors, MDPI, 2023*.
- Oh Hyun-Bin\*, Hyunwoo Ha\*, Kim Jun-Seong, Kwon Byung-Ki, Ji-Yun Kim, Sung-Ho Bae, Tae-Hyun Oh (\*equal contribution). "실시간 Full-HD 영상 모션 증폭 모델". *Workshop on Image Processing and Image Understanding (IPIU) 2023*.
- Kim Yu-Ji\*, Moon Ye-Bin\*, Tae-Hyun Oh (\*equal contribution). "도메인 적응 객체 탐지에 효과적인 데이터 증강 기법". *Workshop on Image Processing and Image Understanding (IPIU) 2023*.

**2022**

- Kim Youwang\*, Kim Ji-Yeon\*, Tae-Hyun Oh (\*equal contribution). "CLIP-Actor: Text-Driven Recommendation and Stylization for Animating Human Meshes". *European Conference on Computer Vision (ECCV) 2022*.
- Kim Jun-Seong\*, Kim Yu-Ji\*, Moon Ye-Bin, Tae-Hyun Oh (\*equal contribution). "HDR-Plenoxels: Self-Calibrating High Dynamic Range Radiance Fields". *European Conference on Computer Vision (ECCV) 2022*.
- Junhyeong Cho, Kim Youwang, Tae-Hyun Oh. "Cross-Attention of Disentangled Modalities for 3D Human Mesh Recovery with Transformers". *European Conference on Computer Vision (ECCV) 2022*.
- Nam Hyeon-Woo, Moon Ye-Bin, Tae-Hyun Oh. "FedPara: Low-Rank Hadamard Product For Communication-Efficient Federated Learning". *International Conference on Learning Representations (ICLR) 2022*.
- Myungseo Song, Seongyeon Park, Bohyung Kim, Tae-Hyun Oh. "Speech De-warping: Unsupervised Pre-training for Data-Efficient Text-to-Speech on Low Resource Languages". *International Conference on Machine Learning Workshop (ICML workshop) 2022 (Workshop on Machine Learning for Audio Synthesis)*.
- Yonghyun Jeong, Jooyoung Choi, Sungwon Kim, Youngmin Ro, Tae-Hyun Oh, Doyeon Kim, Heonseok Ha, Sungroh Yoon. "FICGAN: Facial Identity Controllable GAN for De-identification". *arXiv preprint 2022*.
- Dong-Jin Kim, Tae-Hyun Oh, Jinsoo Choi, In So Kweon. "Dense Relational Image Captioning via Multi-task Triple-Stream Networks". *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 2022*.
- Kyungdon Joo, Hongdong Li, Tae-Hyun Oh, In So Kweon. "Robust and Efficient Estimation of Relative Pose for Cameras on Selfie Sticks". *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 2022*.
- Dongyoon Lee, Gibeom Shin, Seunghoon Lee, Kyunghwan Kim, Tae-Hyun Oh, Ho-Jin Song. "Neural-Network-Based Automated Synthesis of Transformer Matching Circuits for RF Amplifier Design". *IEEE Transactions on Microwave Theory and Techniques, 2022*.
- Dong-Yeop Woo, Kyung-Hoon Kim, Si-Hyeon Ha, Tae-Hyun Oh. "소셜 영상 플랫폼 플레이리스트를 이용한 청각-시각 감정 분석". *Summer Annual Conference of The Institute of Electronics and Information Engineers (IEIE) 2022 [Project page]*.
- Kwon Byung-Ki, Tae-Hyun Oh. "잔여 광학흐름 측정을 통한 광학흐름 네트워크 준지도 학습 방법". *Workshop on Image Processing and Image Understanding (IPIU) 2022*.
- Kim Sung-Bin\*, Ha Hyunwoo\*, Tae-Hyun Oh (\*equal contribution). "이진 레이블을 활용한 연속적인 메트릭 공간 학습법". *Workshop on Image Processing and Image Understanding (IPIU) 2022*.
- Kim Youwang, Tae-Hyun Oh. "가려짐이 있는 사람 메쉬의 생성 모델링을 통한 완성". *Workshop on Image Processing and Image Understanding (IPIU) 2022*.
- Kim Jun-Seong, Kim Yu-Ji, Tae-Hyun Oh. "측광 보정을 통한 방사 필드 신경망 학습". *Workshop on Image Processing and Image Understanding (IPIU) 2022*.
- Kim Ji-Yeon, Tae-Hyun Oh. "3D 환경을 고려한 행동 기반 사람 자세 생성". *Workshop on Image Processing and Image Understanding (IPIU) 2022*.
- Nam Hyeon-Woo, Kim Yu-Ji, Tae-Hyun Oh. "효율적인 지역적 공간-채널 어텐션 블록". *Workshop on Image Processing and Image Understanding (IPIU) 2022*.
- Dongmin Choi\*, Moon Ye-Bin\*, Yongjin Kwon, Junsik Kim, Tae-Hyun Oh (\*equal contribution). "약지도 퓨샷 객체 분할을 위한 완전 컨볼루션 네트워크". *Workshop on Image Processing and Image Understanding (IPIU) 2022*.
- Ha Hyunwoo, Tae-Hyun Oh. "영상 기반 모션 추적을 위한 패턴 마스킹 기법". *Workshop on Image Processing and Image Understanding (IPIU) 2022*.

**2021**

- Kim Youwang, Kim Ji-Yeon, Kyungdon Joo, Tae-Hyun Oh. "Unified 3D Mesh Recovery of Humans and Animals by Learning Animal Exercise". *British Machine Vision Conference (BMVC) 2021*.
- Donghyun Kim, Kuniaki Saito, Tae-Hyun Oh, Bryan Plummer, Stan Sclaroff, Kate Saenko. "CDS: Cross-Domain Self-supervised Pre-training". *International Conference on Computer Vision (ICCV) 2021*.
- Youmin Kim, Jinbae Park, YounHo Jang, Muhammad Ali, Tae-Hyun Oh, Sung-Ho Bae. "Distilling Global and Local Logits with Densely Connected Relations". *International Conference on Computer Vision (ICCV) 2021*.
- Mallikarjun B R, Ayush Tewari, Tae-Hyun Oh, Tim Weyrich, Bernd Bickel, Hans-Peter Seidel, Hanspeter Pfister, Wojciech Matusik, Mohamed Elgharib, Christian Theobalt. "Monocular Reconstruction of Neural Face Reflectance Fields". *IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2021*.
- Sunghoon Kim, Hyunjeong Kwon, Eunji Kwon, Youngchang Choi, Tae-Hyun Oh, Seokhyeong Kang. "MDARTS: Multi-objective Differentiable Neural Architecture Search". *Design Automation and Test in Europe (DATE) 2021*.
- Yang Wang, Gedas Bertasius, Tae-Hyun Oh, Abhinav Gupta, Minh Hoai Nguyen, Lorenzo Torresani. "Supervoxel Attention Graphs for Long-Range Video Modeling". *Winter Conference on Applications of Computer Vision (WACV) 2021*.
- Jieun Lee\*, Kim Sung-Bin\*, Seokhyeong Kang, Tae-Hyun Oh (\*equal contribution). "Lightweight Speaker Recognition in Poincaré Spaces". *IEEE Signal Processing Letters (SPL) 2021*.
- Arda Senocak, Tae-Hyun Oh, Junsik Kim, Ming-Hsuan Yang, In So Kweon. "Learning to Localize Sound Sources in Visual Scenes: Analysis and Applications". *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI) 2021*.
- Kim Jun-Seong, Tae-Hyun Oh. "다중 카메라를 이용한 3차원 신체 표현 및 BEV 위치 추정". *Summer Annual Conference of The Institute of Electronics and Information Engineers (IEIE) 2021*.
- Nam Hyeon-Woo, Moon Ye-Bin, Tae-Hyun Oh. "연합 학습을 위한 로우 랭크 분해 모델". *Summer Annual Conference of The Institute of Electronics and Information Engineers (IEIE) 2021*.
- Kim Youwang, Kim Ji-Yeon, Kyungdon Joo, Tae-Hyun Oh. "사람-동물 3차원 자세 및 형상 추정을 위한 단일 통합 모델". *Summer Annual Conference of The Institute of Electronics and Information Engineers (IEIE) 2021*.
- Ha Hyunwoo\*, Kim Sung-Bin\*, Arda Senocak, Tae-Hyun Oh (\*equal contribution). "오토 인코더 기반 소리-이미지 복원 신경망 모델 구현". *Summer Annual Conference of The Institute of Electronics and Information Engineers (IEIE) 2021*.
- Tae-Hyun Oh. "컴퓨터비전을 위한 레이블 효율적 기계학습". *[Journal] 한국정보과학회 정보과학회지 제 39권 제1호(통권 제380호) 37 - 44 (8 pages)*.
- Kwon Byung-Ki, Tae-Hyun Oh. "비디오를 이용한 위상 기반 진동 분석 알고리즘". *Workshop on Image Processing and Image Understanding (IPIU) 2021*.
- Nam Hyeon-Woo, Moon Ye-Bin, Tae-Hyun Oh. "Grad-CAM Separability for Image Retrieval". *Workshop on Image Processing and Image Understanding (IPIU) 2021*.
- Kim You-Wang, Tae-Hyun Oh. "SMPL Human Instance Segmentation (SMPL-HIS)". *Workshop on Image Processing and Image Understanding (IPIU) 2021*.
- Kim Sung-Bin, Tae-Hyun Oh. "딥러닝을 활용한 사진 읽어주는 시스템 구현". *Workshop on Image Processing and Image Understanding (IPIU) 2021*.
- Moon Ye-Bin, Tae-Hyun Oh. "Self-supervised Few-shot Learning by Episodic Instance Discrimination". *Workshop on Image Processing and Image Understanding (IPIU) 2021*.

## 수상과 선정

2026년 8월 19일과 10월 9일에 게시된 수상·선정 두 건이다.[^naward][^nreview]

- 2026-10-09 · 오태현 교수가 NeurIPS 2026 Top Area Chair로, Hyun-Bin Oh와 Lee Jung-Mok이 Top Reviewer로 선정됐다.[^nreview]
- 2026-08-19 · Sohwi Lim, Lee Hyoseok, Jungjoon Park, 오태현 교수가 CLAY 논문으로 삼성전자 DS 산학협력 교류회 우수 논문상을 받았다.[^naward]

## 소식

2026년 8월 21일–10월 7일의 논문 채택·게재 승인과 학술 활동 소식 여섯 건이다. 날짜는 연구실 게시일이다.[^nijcv][^nneurips][^nchairs][^nposter][^nemnlp][^ntmlr]

- 2026-10-07 · IJCV에 Sound2Vision 논문이 게재 승인됐다.[^nijcv]
- 2026-09-25 · NeurIPS 2026에 Early Failure Detection and Intervention in Video Diffusion Models, FacEDiT, Hear, Localize, and Reason 논문 세 편이 채택됐다.[^nneurips]
- 2026-09-15 · Kim Youwang과 Kwon Byung-Ki가 CVPR 2027의 Area Chair를 맡을 예정이라고 알렸다.[^nchairs]
- 2026-09-09 · 가상 3차원 물체 삽입의 물체 간 반사 일관성을 평가하는 포스터가 SIGGRAPH Asia 2026에 채택됐다.[^nposter]
- 2026-08-21 · IGG와 Spatio-Temporal Audio Language Modeling for Dynamic Sound Sources 두 논문이 EMNLP 2026 본 학회에 채택됐다.[^nemnlp]
- 2026-08-21 · 영상 움직임 확대와 시각 모델 오류의 자연어 설명을 다룬 두 논문이 TMLR에 게재 승인됐다.[^ntmlr]

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291, KAIST 크래프톤 빌딩 E3-5 608·609호.[^home]
- 교수연구실: E3-5 607호.[^prof]
[^home]: 연구실 첫 화면의 Research Agenda·주소. <https://ami.kaist.ac.kr/> (관측 2026-10-26).
[^about]: 연구실 About의 연구 목표. <https://ami.kaist.ac.kr/about> (관측 2026-10-26).
[^members]: 연구실 Members의 현재 구성원·Alumni·Visiting. <https://ami.kaist.ac.kr/members> (관측 2026-10-26).
[^pubs]: 연구실 Publications의 국제 학회·학술지·워크숍·사전 공개본 목록. <https://ami.kaist.ac.kr/publications> (관측 2026-10-26).
[^domestic]: 연구실 Domestic Conference & Journal. <https://ami.kaist.ac.kr/publications/domestic> (관측 2026-10-27).
[^prof]: 전산학부 오태현 부교수 소개. <https://cs.kaist.ac.kr/people/view?idx=651&kind=faculty&menu=160> (관측 2026-10-27).
[^piprofile]: 연구실 교수 상세의 KAIST·POSTECH 재직 이력. <https://ami.kaist.ac.kr/c5b4f03d-aeaa-494c-8dd2-39d84422c33c> (관측 2026-10-27).
[^metaprof]: 메타버스대학원 Faculty의 Joint 표기. <https://meta.kaist.ac.kr/professors/> (관측 2026-10-27).
[^nijcv]: 연구실 IJCV 게재 승인 소식, 2026-10-07. <https://ami.kaist.ac.kr/3f9fdae6-c854-8001-87e4-e20bb767a312> (관측 2026-10-27).
[^nneurips]: 연구실 NeurIPS 논문 세 편 채택 소식, 2026-09-25. <https://ami.kaist.ac.kr/3e7fdae6-c854-8074-8166-de836a449a90> (관측 2026-10-27).
[^nchairs]: 연구실 CVPR 2027 Area Chair 소식, 2026-09-15. <https://ami.kaist.ac.kr/3dcfdae6-c854-8023-afe7-d6e705d36baf> (관측 2026-10-27).
[^nposter]: 연구실 SIGGRAPH Asia 포스터 채택 소식, 2026-09-09. <https://ami.kaist.ac.kr/3d8fdae6-c854-80a0-9f87-e71432ccfb97> (관측 2026-10-27).
[^nemnlp]: 연구실 EMNLP 논문 두 편 채택 소식, 2026-08-21. <https://ami.kaist.ac.kr/3c4fdae6-c854-8000-8995-c8b5de4ac4db> (관측 2026-10-27).
[^ntmlr]: 연구실 TMLR 논문 두 편 게재 승인 소식, 2026-08-21. <https://ami.kaist.ac.kr/3cdfdae6-c854-805f-9519-d3ecf92f9578> (관측 2026-10-27).
[^nreview]: 연구실 NeurIPS 심사 활동 선정 소식, 2026-10-09. <https://ami.kaist.ac.kr/3f5fdae6-c854-805d-aa58-dcb433ae2461> (관측 2026-10-27).
[^naward]: 연구실 삼성전자 DS 교류회 우수 논문상 소식, 2026-08-19. <https://ami.kaist.ac.kr/3b3fdae6-c854-8098-bc52-e847485c234c> (관측 2026-10-27).
[^p1]: Chengxin Liu, Wonseok Choi, Chenshuang Zhang, Tae-Hyun Oh, arXiv 사전 공개본; 연구실 기재 CVPR 2026 (온라인 2026-04-17). <https://doi.org/10.48550/arXiv.2604.15809> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2604.15809> (관측 2026-10-27).
[^p2]: Sohwi Lim, Lee Hyoseok, Jungjoon Park, Tae-Hyun Oh, arXiv 사전 공개본; 연구실 기재 CVPR 2026 (온라인 2026-04-13). <https://doi.org/10.48550/arXiv.2604.11539> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2604.11539> (관측 2026-10-27).
[^p3]: Oh Hyun-Bin, Yuhta Takida, Toshimitsu Uesaka, Tae-Hyun Oh, Yuki Mitsufuji, arXiv 사전 공개본; 연구실 기재 CVPR 2026 (온라인 2025-12-09). <https://doi.org/10.48550/arXiv.2512.08282> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2512.08282> (관측 2026-10-27).
[^p4]: Kim Youwang, Lee Hyoseok, Subin Park, Gerard Pons-Moll, Tae-Hyun Oh, arXiv 사전 공개본; 연구실 기재 CVPR 2026 (온라인 2026-01-15). <https://doi.org/10.48550/arXiv.2601.10200> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2601.10200> (관측 2026-10-27).
[^p5]: Shin Dong-Yeon, Kim Jun-Seong, Kwon Byung-Ki, Tae-Hyun Oh, arXiv 사전 공개본; 연구실 기재 ICLR 2026 (온라인 2026-03-09). <https://doi.org/10.48550/arXiv.2603.08313> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2603.08313> (관측 2026-10-27).
[^p6]: Kim Yu-Ji, Dahye Lee, Kim Jun-Seong, Nam Hyeon-Woo, GeonU Kim, Yongjin Kwon, Yu-Chiang Frank Wang, Jaesung Choe, Tae-Hyun Oh, arXiv 사전 공개본; 연구실 기재 ECCV 2026 (온라인 2026-01-19). <https://doi.org/10.48550/arXiv.2601.13132> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2601.13132> (관측 2026-10-27).
[^p7]: Baek Seong-Eun, Lee Jung-Mok, Kim Sung-Bin, Tae-Hyun Oh, arXiv 사전 공개본; 연구실 기재 ICML 2026 (온라인 2026-01-19). <https://doi.org/10.48550/arXiv.2602.11171> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2602.11171> (관측 2026-10-27).
[^p8]: Lee Hyoseok, Sohwi Lim, Eunju Cha, Tae-Hyun Oh, arXiv 사전 공개본; 연구실 기재 ICML 2026 (온라인 2026-01-08). <https://doi.org/10.48550/arXiv.2601.04791> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2601.04791> (관측 2026-10-27).

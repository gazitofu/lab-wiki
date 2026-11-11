# SNU Robot Vision Lab

**서울대학교 공과대학 기계공학부 · 임종우 교수**

- 분야: 영상 기반 로봇 위치·이동 추정, 전방위 깊이 추정과 3차원 장면 인식, 자율주행 도로 인식[^home][^dept]
- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 컴퓨터 비전[^home][^research], 로봇 항법·SLAM[^home][^dept], 자율주행[^home]
- 홈페이지: <https://sites.google.com/view/snu-rvlab>
- 근거와 출처: [SNU Robot Vision Lab 근거 페이지](snu-rvlab-sources.md)

> 카메라로 주변의 모양과 의미를 파악하고, 로봇과 차량이 어디에 있으며 어떻게 움직이는지 알아내는 방법을 연구한다.[^home][^dept]

## 무엇을 연구하나

서울대학교 기계공학부 임종우 교수가 이끄는 로봇비전 연구실이다. 컴퓨터 비전(사진과 영상에서 물체·장면의 구조와 의미를 알아내는 계산 기술)을 기하와 의미의 두 측면에서 연구한다. 기하 비전은 물체와 카메라 사이의 공간 관계를 알아내는 일이고, 의미 비전은 장면 속 대상이 무엇인지 구분하는 일이다. 연구실은 기계학습(자료에서 패턴을 배워 예측·분류 알고리즘을 만드는 계산 분야)도 함께 연구하며, 이동 로봇·차량·가상현실(컴퓨터가 만든 공간을 보고 상호작용하는 기술)·증강현실(현실에 가상 정보를 겹쳐 보여 주는 기술)을 응용 대상으로 든다.[^home][^research]

첫째 질문은 **움직이는 카메라가 어디에 있는가**다. 영상으로 자기 위치와 주변 지도를 함께 구하는 SLAM(Simultaneous Localization and Mapping, 동시 위치 추정과 지도 작성), 영상과 관성 센서(가속도와 회전 속도를 측정하는 센서)의 관측을 합치는 시각 관성 주행계를 다룬다. 학과 연구 소개는 영상 기반 환경 인식과 로봇 항법을 주요 분야로 들고, 카메라를 다른 센서와 결합하는 연구도 소개한다.[^home][^dept] 최근 LiRS 논문은 추적을 시작하기 전에 영상 속 상대 이동을 실제 길이와 연결하는 초기화(계산의 시작 상태를 정하는 과정)를 다룬다. 여러 시점의 상대적인 크기 관계를 선형 제약(미지수들이 일차식으로 만족해야 하는 조건)으로 정리하고, 구해야 할 상태의 수가 관측 시점 수에 따라 늘어나지 않도록 구성한다.[^p1]

둘째 질문은 **주변 물체가 얼마나 멀리 있으며 어떤 모양인가**다. 여러 카메라의 관측으로 깊이 지도(각 영상 화소가 가리키는 장면 지점까지의 거리를 나타낸 지도)를 구하고, 3차원 복원(영상이나 센서 관측으로 대상의 공간 좌표와 모양을 알아내는 일)을 연구한다.[^home][^research] OmniDS는 넓은 범위를 보는 여러 어안 카메라(넓은 시야를 곡선으로 왜곡해 한 영상에 담는 카메라)에서 같은 물체의 서로 다른 면이 보이거나 일부가 가려지는 문제를 다룬다. 세부 모양과 의미 정보를 처리하는 두 흐름을 결합하고, 카메라 사이 관측의 일치 정도를 이용해 깊이를 반복적으로 보정한다.[^p3]

셋째 질문은 **장면 속에서 무엇을 찾아야 하는가**다. 연구실은 단일·다중 물체 추적(연속 영상에서 같은 대상의 위치를 이어 찾는 일), 의미 분할(영상의 각 화소를 물체나 영역의 종류로 나누는 일), 자율주행차의 장면 이해를 주요 연구로 내세운다.[^home] PanoGrounder는 글로 지시한 대상을 3차원 장면에서 찾기 위해 파노라마(넓은 방향의 시야를 이어 표현한 영상)와 사전 학습된 비전·언어 모델(영상과 글의 관계를 함께 다루는 학습 모델)을 연결한다.[^p4] 도로 인식에서는 HeightLane과 SC-Lane이 도로의 높이와 기울기를 추정해 입체적인 차선 위치를 찾는다.[^p5][^p6]

## 주요 연구 주제

### 1. 위치와 이동 경로 추정

LiRS는 카메라 한 대와 관성 관측을 쓰는 주행계의 초기화 계산을 줄이는 연구다. PathLift는 영상 기반 항법 모델이 제시한 단위 없는 경로를 깊이 관측과 결합해 로봇이 따라갈 실제 길이의 경로로 바꾼다. 경로의 각 지점에서 진행 거리와 옆 방향의 보정을 따로 학습하고, 모의 환경과 실제 바퀴형 로봇에서 시험했다.[^p1][^p2]

### 2. 전방위 깊이와 공간 표현

OmniDS는 카메라별로 보이는 부분이 다를 때도 주변의 깊이를 구하는 연구다. 신경망(계산 단위들을 가중치로 연결해 자료의 관계를 학습하는 모형)에서 세부 모양과 의미 정보를 함께 처리하고, 학습한 표현을 단일 인코더(입력 자료를 계산에 쓸 표현으로 바꾸는 부분)로 옮겨 실행 효율도 고려한다.[^p3] PanoGrounder는 파노라마에 공간의 모양과 의미 정보를 더하고, 글로 찾은 대상의 위치를 3차원 공간으로 합치는 접근이다.[^p4]

### 3. 자율주행을 위한 노면과 차선 인식

HeightLane은 도로를 하나의 평면으로 가정할 때 생기는 한계를 줄이기 위해 여러 기울기를 고려한 높이 지도를 예측한다. SC-Lane은 영상 단서에 맞춰 기울기별 정보를 결합하고, 연속 영상 사이의 높이 추정이 일관되도록 한다. 두 연구는 전방 영상을 위에서 내려다본 공간 표현으로 연결해 차선을 찾는 문제를 다룬다.[^p5][^p6]

## 대표 논문

서울대 재직 시기의 논문에서 위치·경로 추정, 전방위 깊이, 언어와 공간 인식, 도로 인식 갈래를 고르게 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. 학회 논문 5편은 연구실 목록이 연결한 arXiv 사전 공개본의 초록이며, 발표처는 연구실 표기다. PathLift는 CoRL 2026 「채택」으로 표시했다.[^pubs][^p2]

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [LiRS: Linear Relative Scale Constraints for Compact Parameterization of Monocular Visual-Inertial Initialization](https://doi.org/10.1109/lra.2026.3710045) · IEEE Robotics and Automation Letters | 영상과 관성 관측으로 로봇의 움직임을 추적하려면 먼저 실제 길이 비율과 시작 상태를 정해야 한다. LiRS는 여러 시점 사이의 상대 비율을 선형식으로 묶어 경로의 기하를 구하고, 실제 길이 비율·초기 속도·중력·가속도계 편향을 고정된 크기의 상태로 계산한다. 공개 시험 자료에서 길이 비율과 속도 오차가 비교 방법보다 약 30% 줄었다고 보고했다.[^p1] | 1저자 Yeongin Yoon, 마지막 저자 Jongwoo Lim |
| 2 | 2026 | [PathLift: Depth-Conditioned Metric Lifting for Visual-Navigation Priors](https://doi.org/10.48550/arxiv.2610.16103) · CoRL 2026 (채택), arXiv 사전 공개본 | 범용 영상 항법 모델이 알려 주는 경로는 진행 방향은 있어도 실제 이동 길이가 없을 수 있다. PathLift는 미리 학습한 모델의 경로에 별도 깊이 센서 관측을 결합하고, 경로 지점마다 거리와 옆 방향을 보정한다. 시험 중 반복 최적화 없이 경로를 만들며, 서로 다른 항법 모델을 쓴 모의 환경과 실제 바퀴형 로봇에서 항법 성공을 개선했다.[^p2] | 1저자 Gwanjun Shin, 마지막 저자 Jongwoo Lim |
| 3 | 2026 | [OmniDS: Dual-Stream Context Fusion for Omnidirectional Depth from Fisheye Cameras](https://doi.org/10.48550/arxiv.2607.03038) · ECCV 2026, arXiv 사전 공개본 | 카메라 사이 간격이 넓으면 같은 물체의 다른 면이 보이고 가림도 달라져, 관측을 단순히 합칠 때 깊이가 모호해진다. OmniDS는 세부 모양과 의미를 처리하는 두 흐름, 카메라 관측 사이의 일치 정도를 함께 이용해 깊이를 보정한다. 실행 효율을 위해 두 흐름의 표현을 하나의 모형으로 옮기고, 세 전방위 영상 시험 자료에서 깊이 추정 성능을 평가했다.[^p3] | 1저자 Chaesong Park, 마지막 저자 Jongwoo Lim |
| 4 | 2026 | [PanoGrounder: Bridging 2D and 3D with Panoramic Scene Representations for VLM-based 3D Visual Grounding](https://doi.org/10.48550/arxiv.2512.20907) · ECCV 2026, arXiv 사전 공개본 | 글로 설명한 물체를 입체 공간에서 찾는 문제다. 공간의 배치와 모양을 고려해 파노라마 시점을 정하고, 각 영상에서 비전·언어 모델로 지시 대상을 찾은 다음, 결과를 하나의 3차원 경계 상자로 합친다. 학습 때 보지 못한 공간 자료와 달리 표현한 지시문으로도 일반화 성능을 시험했다.[^p4] | 1저자 Seongmin Jung, 마지막 저자 Jongwoo Lim |
| 5 | 2025 | [HeightLane: BEV Heightmap guided 3D Lane Detection](https://doi.org/10.48550/arxiv.2408.08270) · WACV 2025, arXiv 사전 공개본 | 카메라 한 대의 영상에서 경사진 도로의 입체 차선을 찾는다. 여러 기울기를 가정해 도로 높이 지도를 예측하고, 그 높이를 이용해 전방 영상의 특징을 BEV(Bird's Eye View, 위에서 내려다본 시점) 공간으로 옮긴다. 학습에 필요한 노면 높이는 누적한 라이다(빛을 쏘고 돌아오는 정보를 이용해 거리를 재는 센서) 관측으로 만들었고, 차선 검출 성능을 시험했다.[^p5] | 1저자 Chaesong Park, 마지막 저자 Jongwoo Lim |
| 6 | 2025 | [SC-Lane: Slope-aware and Consistent Road Height Estimation Framework for 3D Lane Detection](https://doi.org/10.48550/arxiv.2508.10411) · ICCV 2025, arXiv 사전 공개본 | 도로 높이를 추정할 때 영상에 맞춰 여러 기울기 정보의 비중을 조절하고, 연속 영상에서 추정 결과가 일관되도록 하는 모형이다. 노면 높이와 차선 검출을 함께 평가했으며, OpenLane 시험 자료에서 차선 검출 F-score(찾아낸 대상이 맞는 비율과 실제 대상을 찾아낸 비율의 조화 평균) 64.3%를 보고했다.[^p6] | 1저자 Chaesong Park, 마지막 저자 Jongwoo Lim |

## 교수와 전문 분야

임종우 교수는 1997년 서울대학교에서 학사, 2003년 미국 University of Illinois at Urbana-Champaign에서 컴퓨터과학 석사, 2005년 같은 대학에서 컴퓨터과학 박사를 받았다. Honda Research Institute USA의 Senior Scientist, Google의 Software Engineer를 거쳐 2012년 3월부터 2023년 8월까지 한양대학교 교수로 재직했고, 2023년 9월 서울대학교 기계공학부 교수로 부임했다.[^pi][^dept] 학과 경력에는 「2020.3 – 현재 : (주)멀티플아이 대표이사」가 적혀 있다.[^dept]

학과가 제시한 전문 분야는 영상 기반 3차원 환경 인식과 로봇 항법, 여러 종류의 센서를 결합한 환경 인식, 물체 추적과 행동 인식이다.[^dept] 최근 논문에서는 주행계의 초기 상태를 구하는 수학적 구성, 주변 거리와 도로 높이를 알아내는 학습 방법, 영상과 언어를 결합한 공간 인식으로 이어진다.[^p1][^p3][^p4][^p5][^p6]

## 응용 분야

연구실은 이동 로봇과 차량, 가상현실·증강현실을 응용 대상으로 명시한다.[^home][^research] 최근 연구의 구체적 대상은 바퀴형 로봇이 따라갈 이동 경로, 카메라 주변의 전방위 거리, 글로 지시한 공간 내 대상, 자율주행에 쓰이는 입체 차선과 노면 높이다.[^p2][^p3][^p4][^p5][^p6]

## 구성원

2026년 11월 9일 People의 Graduate Students에 게시된 대학원생 19명이다. 과정은 박사과정 6명, 석박사통합과정 9명, 석사과정 4명이다. 시작 칸의 HYU·SNU, 연도와 a·b, 괄호의 기관명은 누리집 표기다. 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| 양상헌 (Sangheon Yang) | 박사과정 | HYU 21a | Visual SLAM, 3D Scene Modeling |  | 1 |
| 박채송 (Chaesong Park) | 박사과정 | SNU 21b | Autonomous driving | chase121@snu.ac.kr | 3, 5, 6 |
| 신관준 (Gwanjun Shin) | 박사과정 | SNU 22b | Autonomous driving | shinkansan@snu.ac.kr | 2 |
| 윤영인 (Yeongin Yoon) | 박사과정 | SNU 22b | Visual Geometry · Motion Estimation | yoonyi2017@snu.ac.kr | 1 |
| 최진혁 (Jinhyuk Choi) | 박사과정 | SNU 24a, 삼성전자 | TBD | jinh2.choi@snu.ac.kr |  |
| 김지엽 (Jiyeop Kim) | 석박사통합과정 | SNU 24a | 3D Scene Modeling | 99edward@snu.ac.kr |  |
| 정홍모 (Hongmo Jung) | 석박사통합과정 | SNU 24a | Visual SLAM | jjhm2910@snu.ac.kr | 2 |
| 서형석 (Hyeongseok Suh) | 박사과정 | SNU 26a | Lidar SLAM | hyeongaa@snu.ac.kr | 2 |
| 송영보 (Youngbo Song) | 석박사통합과정 | SNU 24b | 6dof Pose Estimation | syb6245@snu.ac.kr |  |
| 최병걸 (Byeonggyeol Choi) | 석박사통합과정 | SNU 24b | 6dof Pose Estimation | skymap33@snu.ac.kr |  |
| 예수민 (Sumin Ye) | 석박사통합과정 | SNU 25a | 3D Scene Modeling | ysm3868@snu.ac.kr |  |
| 전건우 (Gunwoo Jeon) | 석박사통합과정 | SNU 25a | Autonomous Driving | gunw0@snu.ac.kr | 4 |
| 황지현 (Jihyeon Hwang) | 석박사통합과정 | SNU 25a | Depth Estimation | zhyeon@snu.ac.kr | 3, 6 |
| 김장원 (Jangwon Kim) | 석사과정 | SNU 25a | 3D Scene Modeling | jangwons9@snu.ac.kr |  |
| 성무열 (Muyeol Sung) | 석사과정 | SNU 25a | Model Optimization | smy4024169@snu.ac.kr | 3 |
| 조성종 (Seongjong Cho) | 석사과정 | SNU 25b, Avikus | TBD | joseongjong@snu.ac.kr |  |
| 서재형 (JaeHyeong Seo) | 석박사통합과정 | SNU 26a | TBD | fghjvbnm1@snu.ac.kr |  |
| 정호찬 (Hochan Jeong) | 석박사통합과정 | SNU 26a | TBD | jhchnewage114@snu.ac.kr |  |
| 이재원 (Jaewon Lee) | 석사과정 | SNU 26b, RLWRLD | TBD | rigel9058@snu.ac.kr |  |

## 졸업생과 이전 구성원

People의 Alumni에 게시된 56명이다. 누리집의 구획 순서대로 박사후연구원 1명, 한양대 Computer Vision Lab의 박사 구획 6명과 석사 구획 38명, 서울대 Robot Vision Lab의 석사 구획 7명, 학부생·방문자 구획 4명을 담았다. 한양대 시절 이력이 함께 들어 있으며, PhD cand.는 누리집이 적은 과정 표기다. 학위·과정, 연도, 진로는 게시 표기를 따른다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 유종빈 (Jongbin Ryu) | PostDoc HYU (2017~2020) | 아주대학교 조교수 |
| 홍은태 | PhD (2020) | LG전자 |
| 배주한 | PhD cand. | SK Telecom |
| 석호창 | PhD (2021) | Naver Labs |
| 원창희 | PhD (2022) | Uvify |
| 정제현 | PhD cand. | 금융결제원 |
| 오진선 | PhD cand. |  |
| 김상준 | MS (2014) | 한화탈레스 |
| 방가희 | MS (2015) | 서울로보틱스 |
| 공성익 | MS (2016) | KETI |
| 김영성 | MS (2016) | 서울로보틱스 |
| 강한솔 | MS (2016) | 현대자동차 |
| 정현선 | MS (2017) | 롯데정보통신 |
| 이건창 | MS (2017) | 현대자동차 |
| 이경민 | MS (2018) | LG전자 |
| 최병헌 | MS (2019) | LG전자 |
| 이학진 | MS (2020) | Satrec Initiative |
| 황대현 | MS (2020) | Uvify |
| 윤동주 | MS (2021) | Tmax Soft |
| 권기택 | MS (2021) | VUNO |
| 배지운 | MS (2021) | NC Soft |
| 한예린 | MS (2021) | 삼성전자 |
| 이원명 | MS (2021) | 현대자동차 |
| 조범진 | MS (2022) | LG전자 |
| 성진 | MS (2022) | ETRI |
| 하석민 | MS (2022) | 현대로템 |
| 박원준 | MS (2022) | LG전자 |
| 조동희 | MS (2022) | 포스코 |
| 오동훈 | MS (2023) | 로보티즈 |
| 성창호 | MS (2023) | 리디 |
| 이홍범 | MS (2023) | 삼성전자 |
| 송찬선 | MS (2023) | 현대자동차 |
| 임현정 | MS (2023) | LG전자 |
| 민채린 | MS (2023) | Brown Univ. PhD student |
| 박소희 | MS (2023) | 휴톰 |
| Cao Din Duc | MS (2023) | MAXST |
| 차세현 | MS (2024) | LG전자 |
| 최성진 | MS (2024) | LG전자 |
| 주민범 | MS (2024) | LG전자 |
| 남연하 | MS (2024) | LX Semicon |
| 이찬우 | MS (2024) | Uvify |
| 박현우 | MS (2024) | LG전자 |
| 강소영 | MS (2025) | emx |
| 구근모 | MS (2025) | 씨어스랩 |
| 김범수 | MS (2025) | 한화에어로스페이스 |
| 서은빈 | MS (2025) | 현대자동차 |
| 이영준 | MS (2026) | 삼성전자 |
| 김청수 | MS (2026) | 현대로템 |
| 서형석 | MS (2026) | RVLab 박사 진학 |
| 오우진 | MS (2026) | 한화시스템 |
| 최성호 | MS (2026) | 현대자동차 |
| 정성민 | MS (2026) | 현대자동차 |
| 이남훈 (Namhoon Lee) | UG HYU (2013~2014) | 포항공대 조교수 |
| 이우인 | UG HYU (2013~2014) | 카카오브레인 |
| 정윤희 | UG HYU (2015~2017) | PHD Student at DKFZ German Cancer Research Center |
| PoChen Wu | Visiting HYU (2015) | Facebook Reality Labs |

## 최근 논문 목록 (2021–2026)

연구실 Publications의 학술지 2편과 학회 9편, 모두 11편이다. 임종우 교수의 2023년 9월 서울대 부임 전 한양대 시절 논문도 섞여 있다. 연도는 누리집의 연도 구역이며, 제목·저자·발표처는 게시 표기를 따른다. PathLift는 CoRL 2026 채택과 연결된 arXiv 사전 공개본을 함께 표시했다.[^pubs][^pi][^p2]

**2026**

- Yeongin Yoon, Sangheon Yang and Jongwoo Lim. LiRS: Linear Relative Scale Constraints for Compact Parameterization of Monocular Visual-Inertial Initialization. RA-L 2026, DOI: 10.1109/lra.2026.3710045.
- Gwanjun Shin, Hyeongseok Suh, Hongmo Jung, Jongwoo Lim. PathLift: Depth-Conditioned Metric Lifting for Visual-Navigation Priors. CoRL 2026 (채택), arXiv:2610.16103 사전 공개본.
- Seongmin Jung, Seongho Choi, Gunwoo Jeon, Minsu Cho, Jongwoo Lim. PanoGrounder: Bridging 2D and 3D with Panoramic Scene Representations for VLM-based 3D Visual Grounding. ECCV 2026, DOI: 10.1007/978-3-032-37574-2_11.
- Chaesong Park, Jihyeon Hwang, Muyeol Sung, Jongwoo Lim. OmniDS: Dual-Stream Context Fusion for Omnidirectional Depth from Fisheye Cameras. ECCV 2026, DOI: 10.1007/978-3-032-37152-2_18.

**2025**

- Chaesong Park, Eunbin Seo, Jongwoo Lim. HeightLane: BEV heightmap guided 3D lane detection. WACV 2025,
- Chaesong Park, Eunbin Seo, Jihyeon Hwang, Jongwoo Lim. Sc-lane: Slope-aware and consistent road height estimation framework for 3d lane detection. ICCV2025,

**2023**

- Cao Dinh Duc, Jongwoo Lim, X-PDNet: Accurate Joint Plane Instance Segmentation and Monocular Depth Estimation with Cross-Task Distillation and Boundary Correction, in BMVC 2023,
- Jongbin Ryu, Dongyoon Han, and Jongwoo Lim, Gramian Attention Heads are Strong yet Efficient Vision Learners, in ICCV 2023,
- Chaerin Min, Taehyun Kim, and Jongwoo Lim, Meta-Learning for Adaptation of Deep Optical Flow Networks, in WACV 2023, DOI: 10.1109/wacv56688.2023.00218.

**2022**

- Bo-kyeong Kang, Yelin Han, Jaehoon Oh, Jongwoo Lim, Jongbin Ryu, Myeong Seong Yoon, Juncheol Lee, Soorack Ryu, Automatic Segmentation for Favourable Delineation of Ten Wrist Bones on Wrist Radiographs Using Convolutional Neural Network, Journal of Personalized Medicine, Vol. 12, Issue: 5, Page 776, 2022, DOI: 10.3390/jpm12050776.
- Sangheon Yang, Jongwoo Lim, Online Extrinsic Correction of Multi-Camera Systems by Low-Dimensional Parameterization of Physical Deformation, in IROS 2022,

## 수상과 선정

교수 개인의 수상 이력이며, 서울대 부임 이전 소속 시절의 연구에 대한 수상도 함께 소개한다. 연도는 누리집의 표기다. 연도는 누리집의 연도 구역 표기이고 날짜는 게시되어 있지 않다.[^pi]

- 2023 · 임종우 교수, CVPR Longuet-Higgins Prize 수상. 대상 논문은 2013년 발표한 「Online Object Tracking: A Benchmark」.

## 연락과 위치

- 교수 이메일: jongwoo.lim@snu.ac.kr[^pi]
- 교수 전화: 02-880-1639[^pi][^dept]
- 교수 사무실: 서울특별시 관악구 관악로 1 서울대학교 301동 1402호[^pi][^dept]
- 연구실: 학과 교수 소개는 301동 1201호, 연구실 누리집의 Lab Address는 301동 213호로 적는다.[^dept][^home]
[^home]: SNU Robot Vision Lab, Home. <https://sites.google.com/view/snu-rvlab/home> 관측 2026-11-09.
[^research]: SNU Robot Vision Lab, Research. <https://sites.google.com/view/snu-rvlab/research> 관측 2026-11-09.
[^people]: SNU Robot Vision Lab, People. <https://sites.google.com/view/snu-rvlab/people> 관측 2026-11-09.
[^pi]: SNU Robot Vision Lab, Jongwoo Lim 교수 소개. <https://sites.google.com/view/snu-rvlab/people/jwlim> 관측 2026-11-09.
[^dept]: 서울대학교 기계공학부, 임종우 교수 소개. <https://me.snu.ac.kr/snu__professor/%ec%9e%84%ec%a2%85%ec%9a%b0-lim-jongwoo/> 관측 2026-11-09.
[^pubs]: SNU Robot Vision Lab, Publications. <https://sites.google.com/view/snu-rvlab/publications> 관측 2026-11-09.
[^p1]: Y. Yoon, S. Yang, J. Lim, IEEE Robotics and Automation Letters (2026). <https://doi.org/10.1109/lra.2026.3710045> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5061007351> 관측 2026-11-09.
[^p2]: G. Shin, H. Suh, H. Jung, J. Lim, CoRL 2026 (채택), arXiv 사전 공개본 (온라인 2026-10-12). <https://doi.org/10.48550/arxiv.2610.16103> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2610.16103> 관측 2026-11-09.
[^p3]: C. Park, J. Hwang, M. Sung, J. Lim, ECCV 2026, arXiv 사전 공개본 (온라인 2026-07-03). <https://doi.org/10.48550/arxiv.2607.03038> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2607.03038> 관측 2026-11-09.
[^p4]: S. Jung 외, J. Lim, ECCV 2026, arXiv 사전 공개본 (온라인 2025-12-24). <https://doi.org/10.48550/arxiv.2512.20907> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2512.20907> 관측 2026-11-09.
[^p5]: C. Park, E. Seo, J. Lim, WACV 2025, arXiv 사전 공개본 (온라인 2024-08-15). <https://doi.org/10.48550/arxiv.2408.08270> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2408.08270> 관측 2026-11-09.
[^p6]: C. Park, E. Seo, J. Hwang, J. Lim, ICCV 2025, arXiv 사전 공개본 (온라인 2025-08-14). <https://doi.org/10.48550/arxiv.2508.10411> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2508.10411> 관측 2026-11-09.

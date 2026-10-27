# 피지컬 인공지능 연구실 (SNU Physical AI Laboratory)

**서울대학교 공과대학 전기·정보공학부, 협동과정 인공지능 전공, 학부대학 · 최준원 교수**

- 분야: 자율주행과 로봇을 위한 피지컬 인공지능(카메라·라이다·레이더를 합치는 3차원 인식, 센서 입력에서 바로 주행 계획을 내는 종단간 주행과 안전 판단, 오프로드 주행 가능 영역 예측과 학습 데이터 자동 구축, 언어 지시에 따른 로봇 파지), 영상 속 사람의 행동과 사람-물체 상호작용 인식
- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 자율주행[^home][^p1][^p4], 3차원 복원·인식[^p1][^p2][^p3], 멀티모달 AI[^p1][^p7][^p8], 컴퓨터 비전[^p7][^p8], 월드 모델[^research][^p4], 로봇 항법·SLAM[^research][^p5], 로봇 조작·파지[^p6], 데이터 중심 AI·데이터 효율 학습[^p5]
- 홈페이지: <https://adr.snu.ac.kr>
- 근거와 출처: [피지컬 인공지능 연구실 근거 페이지](adr-sources.md)

> 자율주행차와 로봇이 실제 세계에서 주변을 알아보고 움직임을 정하는 인공지능을 연구하는 연구실이다. 연구를 인식, 계획, 데이터 엔지니어링 세 갈래로 나누고, 카메라·라이다·레이더 자료를 합친 3차원 인식, 센서 입력에서 바로 주행 결정을 내는 종단간 주행의 안전 판단, 오프로드에서 지나갈 수 있는 영역의 예측과 그 학습 데이터의 자동 구축을 다룬다.[^home][^research][^p1][^p2][^p4][^p5]

## 무엇을 연구하나

연구실은 서울대학교 전기·정보공학부 최준원 교수가 이끄는 연구실이다.[^ecelabv][^faculty] 학부 연구실 상세는 이름을 「피지컬 인공지능 연구실」(Physical AI LAB)로, 연구 분야를 인공지능, 로봇인지, 자율주행, 센서신호처리로 적고,[^ecelabv] 누리집은 SNU Physical AI Laboratory라는 이름을 쓴다.[^home] 학부 연구실 목록은 이 연구실을 멀티미디어 신호처리, 스마트 자동차, 인공지능 및 머신러닝, 지능 및 로봇 공학의 네 연구그룹에 함께 올린다.[^ecelab] 누리집 첫 화면은 연구실을 자율주행과 로봇 분야에서 피지컬 인공지능(로봇·차량처럼 실제 세계에서 감지하고 움직이는 기계를 위한 인공지능)의 한계를 넓히는 데 힘쓰는 연구 그룹으로 소개한다.[^home] 협동과정 인공지능 전공 교수진 목록은 교수의 전공을 로봇인지, 모빌리티, 자율주행, 주행 예측/판단으로 적는다.[^gsai]

누리집 연구 페이지는 연구를 세 갈래로 나누고 갈래마다 연구 항목의 이름만 적는다.[^research] 인식(Perception) 갈래에는 여러 센서의 자료를 합치는 센서 융합(Sensor Fusion), 여러 인식 과제를 한 모델로 함께 푸는 3차원 인식(Multi-Task 3D Perception), 강인한 인식(Robust Perception), 계획을 고려한 장면 표현(Planning-Aware Scene Representation), 규모를 키우고 새 환경에도 통하는 인식(Scalable and Generalizable Perception), 지나갈 수 있는 영역의 예측(Traversability Prediction)이 있다. 계획(Planning) 갈래에는 종단간 주행(End-to-End Driving), 안전을 고려한 계획(Safety-Aware Planning), 비전-언어-행동 모델(Vision-Language-Action Models, 영상과 언어 지시를 받아 행동을 내는 인공지능 모델), 폐루프 시뮬레이션과 평가(Closed-loop Simulation and Evaluation), 강화학습을 쓰는 후속 학습(Post-Reinforcement Learning), 오프로드 자율주행(Off-road Autonomous Driving)이 있다. 데이터 엔지니어링(Data Engineering) 갈래에는 학습용 정답 표시를 자동으로 다는 자동 주석 모델(Auto-Annotation Models), 주행 기록에서 필요한 장면을 찾아내는 시나리오 발굴(Scenario Mining), 안전에 중요한 시나리오 생성(Safety-Critical Scenario Generation), 월드 모델과 뉴럴 렌더링(World Model & Neural Rendering), 데이터 선별(Data Curation), 장면 편집(Scene Editing)이 있다.[^research]

교수 소개는 교수의 연구 관심을 인공지능, 자율주행, 로보틱스, 3차원 비전과 인식, 지능형 모빌리티로 적는다.[^faculty] 교수는 2024년 한양대학교에서 서울대학교로 옮겼고,[^faculty] 아래 네 갈래 설명의 대표 논문은 모두 그 뒤인 2025–2026년에 발표된 논문이다.[^pubs]

첫째 갈래는 **센서 융합과 3차원 인식**이다. 자율주행차의 인식 시스템은 라이다(레이저를 쏘아 물체까지의 거리를 재는 센서)와 카메라처럼 서로 보완하는 여러 센서를 함께 쓴다.[^p1] 대표 논문에서는 라이다나 카메라가 고장 나거나 가려져도 성능이 덜 떨어지도록, 카메라만·라이다만·둘을 함께 쓰는 세 전문가 디코더 가운데 하나를 물체 후보마다 골라 쓰는 3차원 물체 검출기 MoME를 만들었다.[^p1] 레이더(전파를 쏘아 되돌아오는 신호로 물체의 거리와 움직임을 재는 센서)와 카메라를 합치는 3차원 물체 검출에서는 라이다 특징이 가진 지식을 옮겨 배우게 하는 지식 증류(성능 좋은 모델의 지식을 다른 모델에 옮겨 학습시키는 방법) 방법 RCTDistill을 제안했고,[^p2] 3차원 공간을 일정한 크기의 정육면체 칸(복셀)으로 나눠 칸마다 무엇이 차 있는지 예측하는 3차원 점유 예측 모델 ProtoOcc를 만들었다.[^p3] 최근 논문 목록에는 여러 카메라로 3차원 인식을 할 때 조감도(BEV, 위에서 내려다본 평면) 표현을 시간에 따라 되풀이해 합치는 연구(OnlineBEV, IEEE Transactions on Intelligent Transportation Systems, 2025), 여러 3차원 인식 과제를 함께 푸는 모델에서 과제에 맞는 특징은 살리고 나머지는 누르는 연구(MAESTRO, ICCV 2025), 센서 융합 모델의 예측을 센서별로 나눠 해석하는 연구(NeurIPS 2025), 먼 거리 인식을 위한 레이더·카메라 융합 연구(Horizon3D, ECCV 2026 게재 승인)도 있다.[^pubs]

둘째 갈래는 **종단간 주행 계획과 안전 판단**이다. 종단간(End-to-End, E2E) 주행은 센서 입력을 바로 주행 결정으로 바꾸는 방식이다.[^p4] 대표 논문에서는 주행 궤적에 따라 주요 움직이는 대상과 도로 요소의 미래를 모의하는 희소 월드 모델(장면 전체가 아니라 주요 대상만으로 다음 상황을 예측하는 모델)을 두고, 대상별 충돌 위험과 주행 가능 영역을 지키는지를 따져 안전에 중요한 사건을 찾아내는 E2E 계획 틀 SafeDrive를 만들었다.[^p4] 최근 논문 목록에는 지역 지도들을 서로의 연결을 고려해 합쳐 넓은 범위의 벡터 지도를 만드는 연구(ReVMap, NeurIPS 2026)와 동적인 장면을 알아보며 상황에 맞추는 주행 계획 연구(CarPLAN, 심사 중으로 적힘)도 있다.[^pubs]

셋째 갈래는 **로봇 인지: 오프로드 주행 가능 영역과 언어 지시 파지**다. 대표 논문에서는 포장되지 않은 길을 다니는 로봇을 위해 라이다·카메라·레이더를 함께 단 대규모 데이터셋 STONE을 내놓았는데, 지나갈 수 있는 영역의 정답 지도를 사람의 표시 작업 없이 자동으로 만드는 과정을 함께 만들었다.[^p5] 또 사람이 말로 지시한 물체를 로봇 팔이 집도록, 매개변수를 적게 쓰면서 실시간으로 집는 자세를 찾는 InstructGrasp를 만들어 실제 로봇에서 시험했다.[^p6] 최근 논문 목록에는 의미·기하 정보로 자동으로 단 정답으로 3차원 오프로드 주행 가능 영역을 배우는 연구(Geo3TP, IEEE Robotics and Automation Letters 게재 승인)도 있다.[^pubs]

넷째 갈래는 **영상 속 사람의 행동과 상호작용 이해**다. 연구 페이지의 세 갈래에는 없지만 최근 논문 목록의 2024–2026년 구역에 여러 편 있는 주제다.[^research][^pubs] 대표 논문에서는 영상 속 사람의 행동을 찾고 분류할 때 영상과 소리에 이미지 설명 생성 모델이 쓴 장면 설명까지 합치는 JoVALE를 제안했고,[^p7] 사진 한 장에서 사람과 물체의 짝을 찾아 그 상호작용을 분류할 때 비전-언어 모델(이미지와 글을 함께 다루는 인공지능 모델)에서 뽑은 맥락 정보를 개체별 특징과 합치는 InCoM-Net을 제안했다.[^p8] 최근 논문 목록에는 영상 기반 철도 운영 안전 안내 에이전트(RAISA, IEEE Open Journal of Intelligent Transportation Systems, 2026)와 여러 종류의 자료로 사람 행동을 알아보는 연구(Neurocomputing, 2025)도 있다.[^pubs]

## 주요 연구 주제

### 1. 센서 융합과 3차원 인식

센서 고장에 강한 라이다·카메라 융합(MoME), 라이다 지식을 옮겨 배우는 레이더·카메라 3차원 물체 검출(RCTDistill), 복셀 단위 3차원 점유 예측(ProtoOcc).[^p1][^p2][^p3] 대표 논문 1–3.

### 2. 종단간 주행 계획과 안전 판단

희소 월드 모델로 미래를 모의하고 충돌 위험을 따지는 종단간 주행 계획(SafeDrive).[^p4] 대표 논문 4.

### 3. 로봇 인지: 오프로드 주행 가능 영역과 언어 지시 파지

자동으로 정답을 단 오프로드 3차원 주행 가능 영역 데이터셋(STONE), 언어 지시에 따른 실시간 로봇 파지(InstructGrasp).[^p5][^p6] 대표 논문 5, 6.

### 4. 영상 속 사람의 행동과 상호작용 이해

소리·영상·장면 설명을 함께 쓰는 영상 행동 검출(JoVALE), 비전-언어 모델의 맥락을 쓰는 사람-물체 상호작용 검출(InCoM-Net).[^p7][^p8] 대표 논문 7, 8.

## 대표 논문

랩 Publications 페이지의 2021–2026년 구역 가운데 교수가 서울대학교로 온 2024년 뒤인 2025–2026년 논문에서, 최준원 교수가 마지막 저자이자 교신저자(*)인 학회·학술지 논문을 네 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2025 | [Resilient Sensor Fusion under Adverse Sensor Failures via Multi-Modal Expert Fusion](https://doi.org/10.1109/cvpr52734.2025.00630) · CVPR 2025 | 요즘 자율주행 인식 시스템은 라이다와 카메라처럼 서로 보완하는 여러 센서를 함께 쓴다. 센서 융합 구조는 어려운 환경에서 성능을 높이지만, 라이다 빔 수 감소, 라이다 꺼짐, 좁아진 시야, 카메라 꺼짐, 가림 같은 심한 센서 고장에서는 성능이 크게 떨어진다. 그 원인은 지금의 센서 융합 틀에서 센서끼리 서로 기대기 때문이다. 이 논문은 여러 전문가 모델을 두고 골라 쓰는 방식(mixture of experts)으로 강인한 성능을 내는 라이다·카메라 3차원 물체 검출기 MoME를 제안했다. 카메라 특징만, 라이다 특징만, 둘을 함께 써서 물체 후보(질의)를 풀어내는 세 전문가 디코더를 나란히 두어 센서 사이의 의존을 완전히 끊었다. 각 질의는 세 디코더 가운데 하나로만 풀며(MED), 적응형 질의 라우터(AQR)가 카메라와 라이다 특징의 질을 보고 질의마다 가장 알맞은 디코더를 고른다. nuScenes-R 벤치마크에서 평가해, 궂은 날씨와 센서 고장 조건에서 최고 수준의 성능을 냈고 여러 센서 고장 상황에서 기존 모델들보다 크게 나았다.[^p1] | 1저자 K. Park, 마지막 저자 최준원 |
| 2 | 2025 | [RCTDistill: Cross-Modal Knowledge Distillation Framework for Radar-Camera 3D Object Detection with Temporal Fusion](https://doi.org/10.1109/iccv51701.2025.02348) · ICCV 2025 | 레이더와 카메라를 합치는 3차원 물체 검출은 비용이 적게 드는 방법이지만, 성능은 라이다 기반 방법에 아직 못 미친다. 최근 연구는 여러 시점의 자료를 합치는 시간 융합과 지식 증류로 이 한계를 넘으려 했지만, 물체의 움직임이나 레이더·카메라 센서 고유의 오차에서 오는 불확실성을 충분히 고려하지 않았다. 이 논문은 시간 융합에 바탕을 둔 센서 간 지식 증류 방법 RCTDistill을 제안했다. 거리와 방위각(수평 방향의 각도) 방향의 오차를 고려해 라이다 특징의 지식을 옮겨 부정확한 조감도(BEV) 표현을 다듬는 RAKD, 움직이는 물체 때문에 생기는 시간 어긋남을 줄이려고 과거의 레이더·카메라 BEV 특징을 현재의 라이다 표현에 맞추는 TKD, 교사 모델(지식을 주는 모델)의 관계 지식을 옮겨 학생 모델이 물체(전경)와 배경의 특징을 가려내게 하는 RDKD의 세 모듈로 이뤄진다. nuScenes와 View-of-Delft(VoD) 데이터셋에서 레이더·카메라 융합 방법 가운데 최고 수준의 성능을 냈고, 추론 속도는 초당 26.2프레임으로 가장 빨랐다.[^p2] | 1저자 G. Bang, 마지막 저자 최준원 |
| 3 | 2025 | [ProtoOcc: Accurate, Efficient 3D Occupancy Prediction Using Dual Branch Encoder-Prototype Query Decoder](https://doi.org/10.1609/aaai.v39i4.32450) · AAAI 2025 | 장면의 의미를 깊이 이해해 3차원 복셀마다 차 있는지와 그 종류(의미 범주)를 예측하는 3차원 점유 예측 모델 ProtoOcc를 제안했다. 이중 분기 인코더(DBE)는 넓은 범위를 한 번에 보는 BEV 표현과 공간 해상도가 높은 복셀 표현을 여러 크기에서 합쳐 새로운 3차원 복셀 표현을 만들고, 이로써 성능과 계산 효율을 함께 높였다. 원형 질의 디코더(PQD)는 두 종류의 원형(prototype, 범주를 대표하는 특징) 기반 질의로 트랜스포머(자료 조각 사이의 관계에 주의를 기울여 학습하는 신경망 구조)의 디코딩을 빠르게 한다. 입력 장면의 복셀 특징에서 만드는 장면 적응형 원형과, 학습하는 동안 장면 적응형 원형의 지수 이동 평균(최근 값에 더 큰 무게를 두며 계속 갱신하는 평균)으로 갱신하는 장면 무관 원형을 쓰며, 이 질의로 트랜스포머 디코딩을 되풀이하지 않고 한 번에 3차원 점유를 예측한다. 원형을 만들 때 잡음을 넣고 이를 없애도록 학습시키는 강인한 원형 학습도 제안해 원형 특징의 질이 나빠져도 버티게 했다. Occ3D-nuScenes 벤치마크에서 mIoU(예측 영역과 정답 영역이 겹치는 정도를 범주별로 평균한 지표) 45.02%로 최고 수준의 성능을 냈고, 한 프레임만 쓰는 방식으로는 NVIDIA RTX 3090에서 초당 12.83프레임으로 mIoU 39.56%를 얻었다.[^p3] | 1저자 J. Kim, 마지막 저자 최준원 |
| 4 | 2026 | [SafeDrive: Fine-Grained Safety Reasoning for End-to-End Driving in a Sparse World](https://arxiv.org/abs/2602.18887) · CVPR 2026 | 센서 입력을 바로 주행 결정으로 바꾸는 종단간(E2E) 방식은 하나의 모델로 다루고 규모를 키우기 쉬워 최근 주목받지만, 이 통합된 틀에서 안전을 보장하는 일은 가장 중요한 과제 가운데 하나로 남아 있다. 이 논문은 주행 궤적을 조건으로 하는 희소 월드 모델로 안전 추론을 드러나게, 해석할 수 있게 하는 E2E 계획 틀 SafeDrive를 제안했다. SafeDrive는 서로 보완하는 두 신경망으로 이뤄진다. SWNet은 주요 움직이는 대상과 도로 요소의 미래 행동을 모의하는 궤적 조건부 희소 세계를 만들어 상호작용 중심의 표현을 넘겨주고, FRNet은 대상별 충돌 위험과 시간에 따라 주행 가능 영역을 지키는지를 평가해 앞으로의 시간 단계에서 안전에 중요한 사건을 정확히 찾아낸다. 개루프(기록된 자료로 예측만 평가)와 폐루프(모델의 결정이 다음 상황에 반영되는 모의 주행으로 평가) 벤치마크 모두에서 최고 수준의 성능을 냈다. NAVSIM에서 평가 점수 PDMS 91.6, EPDMS 87.5를 기록했고 12,146개 시나리오 가운데 충돌은 61건(0.5%)이었으며, Bench2Drive에서는 주행 점수 66.8%를 얻었다.[^p4] | 1저자 J. Kim, 마지막 저자 최준원 |
| 5 | 2026 | [STONE Dataset: A Scalable Multi-Modal Surround-View 3D Traversability Dataset for Off-Road Robot Navigation](https://doi.org/10.1109/icra57385.2026.11695784) · ICRA 2026 | 오프로드에서 믿을 만하게 다니려면 지나갈 수 있는 영역을 정확히 추정하고, 여러 지형과 감지 조건에서도 강인하게 인식해야 한다. 그러나 기존 데이터셋은 규모를 키우기 어렵고 센서 종류도 다양하지 않아 3차원 주행 가능 영역 예측의 발전을 제한해 왔다. 이 논문은 오프로드 주행을 위한 대규모 멀티모달 데이터셋 STONE을 내놓았다. STONE은 (1) 사람의 표시 작업 없이 완전히 자동화된 과정으로 로봇이 지나간 궤적을 바탕으로 만든 3차원 주행 가능 영역 지도와 (2) 128채널 라이다, RGB 카메라 6대, 4D 이미징 레이더 3대를 동기화한 전방위 감지 자료를 제공한다. 낮과 밤, 초원, 농지, 공사장, 호수 등 여러 환경과 조건을 담았다. 자동 표시 과정은 라이다 스캔으로 지형 표면을 촘촘히 복원하고 경사·높이·거칠기 같은 기하 속성을 뽑은 뒤, 마할라노비스 거리(자료가 퍼진 정도를 고려해 잰 거리) 기준으로 로봇이 지나간 궤적 밖까지 주행 가능 여부를 붙인다. 이렇게 사람 손 없이 기하를 고려한 정답 자료를 규모 있게 만들 수 있게 했고, 복셀 단위 3차원 주행 가능 영역 예측 벤치마크와 센서 하나만 쓰는 경우와 여러 센서를 쓰는 경우의 기준 모델을 함께 제시했다.[^p5] | 1저자 K. Park, 마지막 저자 최준원 |
| 6 | 2026 | [InstructGrasp: A Real-Time Language-Guided Grasp Pose Detection for Robotic Manipulation](https://doi.org/10.1109/lra.2026.3731854) · IEEE Robotics and Automation Letters | 언어 지시에 따라 로봇이 물체를 집는 기술은 정돈되지 않은 환경에서 사람과 로봇이 직관적으로 상호작용하게 하는 핵심 기술이다. 지금의 최고 수준 방법들은 말이 가리키는 대상을 영상에서 찾아내는 정확도가 높지만 매개변수가 수억 개인 비전-언어 모델(VLM)에 점점 더 기대어, 자원이 제한된 로봇 내장 장치에서 실시간으로 돌리기 어렵다. 이 논문은 언어 지시에 따른 파지 자세를 실시간으로 찾는, 매개변수를 적게 쓰는 틀 InstructGrasp를 내놓았다. QGQF와 지시 조절 디코더(IMD)로 영상과 의미를 정밀하게 맞춘다. Jacquard에서 학습 때 본 물체 95.0%, 처음 보는 물체 92.0%, Grasp-Anything++에서 처음 보는 물체 58.0%의 최고 수준 성공률을 얻었다. OCID-VLG에서는 본 물체 91.08%, 처음 보는 물체 86.49%(그 물체로 학습하지 않은 제로샷 조건)의 성공률로, 매개변수가 1억 4,700만–2억 4,000만 개인 완전 지도 학습 대형 모델 OGRG(본 물체 90.81%)와 LAVT(본 물체 87.55%)와 같거나 나은 결과를 냈는데, 매개변수는 전체 9,830만 개(학습하는 것은 3,231만 개)였다. 처리 시간은 31.04밀리초로 실시간 추론 속도를 지켰다. 실제 Franka Emika Panda 로봇에서도 검증해, 물체가 어지럽게 놓인 곳에서 시각만으로 집기 77%, 지시에 따라 집기 43%의 성공률로 비교한 모든 기준 방법보다 나았다.[^p6] | 1저자 K. O. Yang, 마지막 저자 최준원 |
| 7 | 2025 | [JoVALE: Detecting Human Actions in Video Using Audiovisual and Language Contexts](https://doi.org/10.1609/aaai.v39i7.32745) · AAAI 2025 | 영상 행동 검출(VAD)은 영상 속 행동이 어디서 일어나는지 찾고 무슨 행동인지 분류하는 일로, 영상에는 소리, 시각 단서, 주변 장면 맥락 같은 여러 정보원이 들어 있다. 이 멀티모달 정보를 잘 쓰려면 모델이 행동과 관련된 단서를 정확히 골라내야 해 어렵다. 이 논문은 행위자 중심으로 시각·소리·언어를 함께 다루는 인코더 JoVALE를 제안했고, 소리와 시각 특징에 대용량 이미지 설명 생성(캡셔닝) 모델에서 얻은 장면 설명 맥락까지 합친 첫 VAD 방법이라고 밝혔다. 핵심은 소리·시각·장면 설명 정보를 행위자(행동하는 사람)를 중심으로 모아, 각 행위자의 행동을 알아보는 데 중요한 특징을 상황에 맞게 합치는 것이다. 행위자들과 그 멀티모달 맥락 사이에서 변해 가는 상호작용을 잡아내도록 트랜스포머 기반의 행위자 중심 멀티모달 융합망을 만들었다. 대표적인 세 VAD 벤치마크 AVA, UCF101-24, JHMDB51-21에서 멀티모달 정보를 넣으면 성능이 크게 오르는 것을 보였고, 새로운 최고 성능을 세웠다.[^p7] | 1저자 T. Son, 마지막 저자 최준원 |
| 8 | 2026 | [Mining Instance-Centric Vision–Language Contexts for Human–Object Interaction Detection](https://arxiv.org/abs/2604.02071) · CVPR 2026 | 사람-물체 상호작용(HOI) 검출은 사진 한 장에서 사람과 물체의 짝을 찾아 그 둘의 상호작용을 분류하는 일로, 강한 시각 이해와 섬세한 맥락 추론이 필요하다. 최근 방법들은 비전-언어 모델(VLM)로 의미에 관한 사전 지식을 넣어 HOI 검출 성능을 크게 높였지만, 장면 전체에 흩어진 여러 맥락 단서를 충분히 쓰지 못하는 경우가 많다. 이 논문은 VLM에서 뽑은 풍부한 의미 지식과 물체 검출기가 내는 개체별 특징을 합치는 InCoM-Net을 제안했다. 검출된 각 개체 안의 관계뿐 아니라 개체 사이, 그리고 주변 장면 맥락과의 관계까지 모델링해 상호작용을 더 깊이 추론하게 했다. 핵심 부품은 VLM에서 얻은 특징에서 개체 안, 개체 사이, 장면 전체의 맥락 단서를 따로 뽑는 ICR과, 이 여러 맥락 특징을 개체 수준의 검출기 특징과 단계적으로 되풀이해 합치는 ProCA다. HICO-DET와 V-COCO 벤치마크에서 이전 HOI 검출 방법들을 넘는 최고 수준의 성능을 냈다.[^p8] | 1저자 S. W. Seo, 마지막 저자 최준원 |

## 교수와 전문 분야

최준원 교수(Jun Won Choi)는 서울대학교 전기·정보공학부 교수다.[^ecelist][^eceprof] 학부 전임교수 목록은 학부대학 겸무로 적고,[^ecelist] 누리집 교수 소개는 소속을 Department of Electrical and Computer Engineering, Interdisciplinary Program In Artificial Intelligence, SNU College, College of Liberal Studies로 적는다.[^faculty] 협동과정 인공지능 전공 교수진 목록은 직위를 부교수로 적는다.[^gsai] 학부 교수 소개는 학력을 서울대학교 전기공학부 학사, 서울대학교 전기및컴퓨터공학부 석사, 어바나-샴페인 일리노이 주립대 전기및컴퓨터공학부 박사로 적고,[^eceprof] 누리집 교수 소개는 박사 지도교수를 Andrew C. Singer, 석사 지도교수를 Nam Ik Cho로 적는다.[^faculty]

누리집 교수 소개에 따르면 교수는 2010–2013년 미국 샌디에이고의 Qualcomm에서 Senior Engineer로 일했고, 2013년 한양대학교에 부임해 2024년까지 Department of Electrical Engineering 교원으로 있었다(경력 칸 표기는 "Assistant, Associate, Full Professor, Hanyang University (2013-2024)"). 2022년 4월–2023년 2월에는 샌디에이고의 Qualcomm Corp R&D에서 방문 연구원으로 있었다(경력 칸 표기 Visiting Scientist, 활동 칸 표기 Visiting Researcher). 2024년 서울대학교로 와서 전기·정보공학부의 정년 보장 교수(tenured Professor)로 있으며 Physical AI Lab을 이끈다고 적고, 경력 칸은 "Associate Professor, Seoul National University (2024-)"로 적는다. 교수 소개는 이 분야의 주요 학술지와 학회에 70편이 넘는 논문을 냈다고 적는다.[^faculty]

교수 소개는 교수가 Qualcomm Distinguished Faculty Award와 "Commendation from the Minister of Trade, Industry and Energy of Korea"를 받았다고 적고, 활동 칸은 Distinguished Qualcomm Faculty Awards를 2020, 2021, 2025년으로, 「산업통산부 AI 미래차 M.AX 얼라이언스 공동위원장 (장관표창 수여)」을 적는다.[^faculty] 학술 활동으로는 IEEE Transactions on Vehicular Technology(2019년부터)와 IEEE Transactions on Intelligent Transportation Systems(2019년부터), International Journal of Automotive Technology(2020년부터)의 Associate Editor(부편집장), 2024년 IEEE Intelligent Vehicles Symposium(IV)의 Workshop Chair, NeurIPS 2026 Evaluations and Datasets Track의 Area Chair, AAAI의 Senior Program Committee(활동 칸 표기 "2026, 2007")를 적는다.[^faculty] 학교 안팎의 직책으로는 서울대학교 미래모빌리티기술센터(FMTC) 부센터장(2026년 1월부터), 서울대학교 AI 연구원 AICEO과정 부주임(2026년 4월부터), 자율주행자동차사고조사위원회(2025.12.24–2027.12.23), 제3기 서울시 자율주행자동차 시범운행지구 운영위원회 위원(2025.10.1–2027.9.30), 고영향AI 전문위원(2026.3.19–2028.3.18), 한국자동차공학회 자율주행전장부문 부회장(2024년 1월부터)·사업이사(2024년 1월–2025년 12월)·선임직이사(2026년 1월부터), 현대자동차 End-to-End 자율주행 기술 자문(2025년)과 자율주행 기술 자문(2018년)을 적는다.[^faculty] 학부 교수 소개의 주요경력 칸은 자동차공학회 전기전자시스템부문·융합SW & AI부문 부문이사와 통신학회 융합무인이동체분과 집행이사도 적는다.[^eceprof]

랩 Publications 페이지의 목록을 시기별로 보면, 2001–2014년 논문은 통신과 신호 처리를 다루며, 여러 안테나를 쓰는 통신(MIMO)의 신호 검출, 터보 등화(검출과 복호를 번갈아 되풀이하며 채널이 일그러뜨린 신호를 바로잡는 방법), 수중 음향 통신, 저전력 디지털 필터가 주된 주제다. 2015–2020년 논문은 압축 센싱(적은 측정으로 희소한 신호를 복원하는 방법)과 희소 신호 복원, 대규모 MIMO의 검출·채널 추정, 밀리미터파 통신의 빔 추적을 다루고, 2016년부터는 심층 신경망을 쓴 연구가 나타나 변조 방식 자동 분류(2016–2017년), 차량 궤적 예측과 심층 강화학습을 쓴 자동 제동(2017년), 카메라·라이다 센서 융합(2018년), 3차원 물체 검출(2019–2020년)을 다룬다.[^pubs] 교수가 한양대학교에 있던 2021–2023년 구역에는 주변 차량과 보행자의 미래 궤적 예측(LaPred, R-Pred, SiT Dataset)과 카메라·라이다·레이더 자료를 쓰는 3차원 물체 검출·추적(MGTANet, D-Align 등)이 많고, 밀리미터파 빔 추적 같은 통신 연구와 녹내장 진단 같은 의료 영상 연구도 있다.[^pubs]

서울대학교로 온 뒤의 논문으로 보면 지금의 전문 분야는 네 갈래다. 첫째, 라이다·카메라·레이더를 합쳐 주변 물체와 공간을 3차원으로 알아보는 자율주행 인식이다(대표 논문 1–3).[^p1][^p2][^p3] 둘째, 센서 입력에서 바로 주행 계획을 내는 종단간 주행의 안전 판단이다(대표 논문 4).[^p4] 셋째, 오프로드를 다니는 로봇의 주행 가능 영역 인식과 데이터 자동 구축, 언어 지시에 따른 로봇 파지다(대표 논문 5, 6).[^p5][^p6] 넷째, 영상과 사진 속 사람의 행동과 사람-물체 상호작용 인식이다(대표 논문 7, 8).[^p7][^p8]

## 응용 분야

누리집 첫 화면은 연구의 대상 분야를 자율주행과 로봇으로 적는다.[^home] 대표 논문은 센서가 고장 나거나 날씨가 궂은 조건의 자율주행 인식,[^p1] 비용이 적은 레이더·카메라 인식,[^p2] 자율주행의 주행 계획과 충돌 위험 판단,[^p4] 오프로드 로봇 주행,[^p5] 실제 로봇 팔의 물체 집기[^p6]를 대상으로 한다. 최근 논문 목록에는 철도 운영의 안전 안내(RAISA, 2026)와 한쪽 성대 마비를 진단하는 딥러닝 모델(Scientific Reports, 2025) 연구도 있다.[^pubs] 졸업생의 진로로 랩이 적은 곳에는 Samsung Electronics, Hyundai Motors, Hanwha Aerospace, LG Electronics, Hyundai Rotem, Qualcomm Korea, Naver, Korean Institute of Science and Technology, Sungkyul University(박사 졸업생), LG Innotek, LIG NEX1, 42dot, Continental, LG U+(석사 졸업생) 등이 있다.[^members]

## 구성원

2026년 10월 23일 누리집 Members 페이지 기준이다. Ph.D / Joint M.S. Ph.D. Students 칸의 37명과 M.S. Students 칸의 1명이며, 과정은 카드의 표기(Ph. D. Candidate, M. S. Candidate)를 옮겼다. Ph.D / Joint M.S. Ph.D. Students 칸에는 M. S. Candidate로 적힌 11명이 함께 있고, 같은 칸의 마지막 6명은 과정 대신 소속 기관과 Part Time을 적었다. 이메일은 카드의 Contact 표기다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Seokhwan Lee | 박사과정 | shlee@spa.hanyang.ac.kr | 7 |
| Junho Lee | 박사과정 | junhlee@spa.hanyang.ac.kr |  |
| Yunsik Shin | 박사과정 | ysshin@spa.hanyang.ac.kr |  |
| Inyoung Yoon | 박사과정 | inyoungyoon@spa.hanyang.ac.kr |  |
| Junyong Yun | 박사과정 | jyyun@spa.hanyang.ac.kr |  |
| Konyul Park | 박사과정 | kypark@adr.snu.ac.kr | 1, 5 |
| Geonho Bang | 박사과정 | ghbang@adr.snu.ac.kr | 2 |
| Jungho Kim | 박사과정 | jhkim@adr.snu.ac.kr | 3, 4, 5 |
| Soowon Seo | 박사과정 | swseo@adr.snu.ac.kr | 7, 8 |
| Kyungchae Lee | 박사과정 | kclee@adr.snu.ac.kr | 8 |
| Hongjae Shin | 박사과정 | hjshin@adr.snu.ac.kr | 4, 5 |
| Jaehyun Park | 박사과정 | jhpark@adr.snu.ac.kr | 5 |
| Daehun Kim | 박사과정 | dhkim@adr.snu.ac.kr | 1, 5 |
| Dongyoung Lee | 박사과정 | dylee@adr.snu.ac.kr | 3 |
| Haesung Oh | 박사과정 | hsoh@adr.snu.ac.kr |  |
| Eunho Lee | 박사과정 | ehlee@adr.snu.ac.kr |  |
| Junseo Park | 박사과정 | jspark@adr.snu.ac.kr | 5 |
| Geunju baek | 박사과정 | gjbaek@adr.snu.ac.kr | 2 |
| Chanhee Chung | 박사과정 | chchung@adr.snu.ac.kr |  |
| Heecheol Yoo | 박사과정 | hcyoo@adr.snu.ac.kr |  |
| Hyungchan Cho | 석사과정 | hccho@adr.snu.ac.kr | 5, 8 |
| DongHyuk Kwak | 석사과정 | dhkwak@adr.snu.ac.kr | 4 |
| Jiyong Oh | 석사과정 | jyoh@adr.snu.ac.kr | 4, 5 |
| Seunghoon Yu | 석사과정 | shyu@adr.snu.ac.kr | 4, 5 |
| Wonjun Jeong | 석사과정 | wjjeong@adr.snu.ac.kr |  |
| Seunghyeop Nam | 석사과정 | shnam@adr.snu.ac.kr |  |
| Myeongjun Kim | 석사과정 | mjkim@adr.snu.ac.kr |  |
| Minhyuck Kim | 석사과정 | mhkim@adr.snu.ac.kr |  |
| Hyunju Kim | 석사과정 | hjkim@adr.snu.ac.kr |  |
| Dongwook Kim | 석사과정 | dwkim@adr.snu.ac.kr |  |
| Joonwon Choi | 석사과정 | jwchoi@adr.snu.ac.kr |  |
| Kyungho Kang | Seoul Metro (Part Time) | khkang@spa.hanyang.ac.kr |  |
| Gyuhee Park | SK Telecom (Part Time) | ghpark@spa.hanyang.ac.kr |  |
| Jongbum Park | KETI (Part Time) | active76@hanyang.ac.kr |  |
| Jeeseong Kim | STRAD VISION (Part Time) | jeeseongkim@adr.snu.ac.kr |  |
| Changsik Lee | Korea Institute of Industrial Technology (Part Time) | cslee21@adr.snu.ac.kr |  |
| Jiwon Lee | Samsung Electronics (Part Time) | jwlee@adr.snu.ac.kr |  |
| Jeeon Bae | 석사과정 | jebae@adr.snu.ac.kr |  |

## 졸업생과 이전 구성원

누리집 Members 페이지 Alumni (Ph. D.) 칸의 16명과 Alumni (M. S.) 칸의 25명이다. 박사 졸업생 칸은 이름 옆 괄호에 졸업 학기와 진로를 적고, 석사 졸업생 칸은 졸업 시기 없이 진로만 적으며 3명은 진로도 적지 않았다. 학기와 진로는 랩 표기 그대로다. 졸업 학기가 2022–2023년인 박사 졸업생 6명은 교수가 한양대학교에 있던 때(2013–2024) 졸업했다.[^members][^faculty]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Minjae Seong | Ph.D. (2025fall) | LG Electronics |
| Changwon Kang | Ph.D. (2025fall) | Hanwha Aerospace |
| Jangho Kwon | Ph.D. (2025fall) | Korean Institute of Science and Technology |
| Kyungok Yang | Ph.D. (2025spring) | Sungkyul University |
| Jisong Kim | Ph.D. (2025spring) | Samsung Electronics |
| Taein Son | Ph.D. (2025spring) | Samsung Electronics |
| Yecheol Kim | Ph.D. (2024fall) | Samsung Electronics |
| Sehwan Choi | Ph.D. (2024fall) | Hanwha Aerospace |
| Jaesoon Baik | Ph.D. (2024fall) | Samsung Electronics |
| Younji Shin | Ph.D. (2024spring) | Hyundai Rotem |
| Junho Koh | Ph.D. (2023fall) | Hyundai Motors |
| Byeongdo Kim | Ph.D. (2023spring) | Naver |
| Sun Hong Lim | Ph.D. (2023spring) | Samsung Electronics |
| Jin Hyeok Yoo | Ph.D. (2022fall) | Qualcomm Korea |
| Jae Kyum Kim | Ph.D. (2022fall) | Samsung Electronics |
| Syed Ali Irtaza | Ph.D. (2022spring) | Institute of Space Technology |
| Jeongseon Choi | M.S. |  |
| Chanhyeok Kim | M.S. | Hyundai Rotem |
| Byunghyun Lee | M.S. |  |
| Byungwoo Park | M.S. |  |
| Kunhoon Kim | M.S. | Ph. D. at Hanyang Univ. |
| Jungoo Ji | M.S. | 생산기술연구소 |
| Jisu Yoon | M.S. | LIG NEX1 |
| Youngwoo Lee | M.S. | Samsung Electronics |
| Kwangjin Choi | M.S. | LG Innotek |
| Chanwoo Lee | M.S. | Uvify |
| Chanik Jang | M.S. | Hyundai Motors |
| Jongwook Bae | M.S. | Dubai Future Lab |
| JunHyung Lee | M.S. | Hyundai Motors |
| Minwook Kim | M.S. | 42dot |
| Sherzodbek Tojimahammatov | M.S. | Chowis |
| Elbek Khoshimjonov | M.S. | Atomic Invest |
| TaeHwan Hwang | M.S. | LG Electronics |
| Heejin Song | M.S. | in USA |
| Seong Hyeon Park | M.S. | Aju University |
| Junghoon Seo | M.S. | Samsung Electronics |
| Jinwan Lee | M.S. | Silicon Works |
| Yubin Ahn | M.S. | Samsung Elec. |
| Junghwan Lee | M.S. | Continental |
| Jisu Bae | M.S. | LG U+ |
| Sucheol Shin | M.S. | ShinGuang |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지 International Journals / Highlighted Conference Papers 칸의 2021–2026년 구역 51편(2026년 11, 2025년 10, 2024년 11, 2023년 10, 2022년 4, 2021년 5)이다. 연도는 페이지의 연도 구역이고, 각 줄은 페이지 표기 그대로다(앞 대괄호는 학회·학술지 약칭과 연도, *는 교신저자). 교수는 2024년에 한양대학교에서 서울대학교로 옮겼으므로 2021–2023년 구역은 교수가 한양대학교에 있던 때의 논문이고 2024년 구역에도 그때의 논문이 섞여 있을 수 있어, 모두 현재 서울대학교 연구실의 성과로 묶지 않는다.[^pubs][^faculty] 줄 끝의 〔 〕는 출판 상태를 따로 표시한 것이다. 〔게재 승인〕은 페이지가 게재 승인(accepted)으로만 적고 권·쪽이나 발표 월을 적지 않은 논문, 〔학회 발표 전〕은 2026년 12월 학회(NeurIPS 2026) 논문으로 적힌 논문, 〔심사 중〕은 심사 중(Submitted)으로 적힌 논문, 〔arXiv 사전 공개본〕은 학술지·학회 이름 없이 arXiv 번호만 적힌 논문이며, 모두 페이지가 둔 연도 구역에 그대로 두었다.[^pubs]

**2026**

- [RA-L26] Daehun Kim, Konyul Park, Joonwon Choi, Junseo Park, Jaehyun Park, and Jun Won Choi\*, "Geo3TP: Learning 3D Off-Road Traversability from Semantic-Geometric Automatic Annotation," accepted to IEEE Robotics and Automation Letters. 〔게재 승인〕
- [NeurIPS26] Hongjae Shin, Jungho Kim, Donghyuk Kwak, Myeongjun Kim, Seunghoon Yu, Jiyong Oh, and Jun Won Choi\*, "ReVMap: Vectorized Global Mapping via Connectivity-Aware Local Map Fusion," Neural Information Processing Systems (NeurIPS), Dec. 2026. 〔학회 발표 전〕
- [RA-L26] Kyoung Ok Yang, Changwon Kang, Younjae Go, Jun Moon, and Jun Won Choi\*, "InstructGrasp: A Real-time Language-Guided Grasp Pose Detection for Robotic Manipulation," accepted to IEEE Robotics and Automation Letters. 〔게재 승인〕
- [ECCV26] Geonho Bang, Geunju Baek, Dongyoung Lee, Wonjun Jeong, and Jun Won Choi\* "Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving", accepted to European Conference on Computer Vision (ECCV) 2026. 〔게재 승인〕
- [CVPR26] Jungho Kim, Jiyong Oh, Seunghoon Yu, Hongjae Shin, Donghyuk Kwak, and Jun Won Choi\*, "SafeDrive: Fine-Grained Safety Reasoning for End-to-End Driving in a Sparse World," IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Highlight Presentation, June 2026.
- [CVPR26] Soo Won Seo, KyungChae Lee, Hyungchan Cho, Taein Son, Nam Ik Cho, and Jun Won Choi\*, "Mining Instance-Centric Vision–Language Contexts for Human–Object Interaction Detection," IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), June 2026.
- [ICRA26] Konyul Park, Daehun Kim, Jiyong Oh, Seunghoon Yu, Junseo Park, Jaehyun Park, Hongjae Shin, Hyungchan Cho, Jungho Kim, and Jun Won Choi\*, "STONE Dataset: Scalable 3D Traversability Dataset with Multi-sensor Surround-View for Off-road Robot Navigation," IEEE International Conference on Robotics & Automation (ICRA), June 2026.
- [NC26] Junho Lee, Jisu Yoon, Jisong Kim, and Jun Won Choi\*, "Image-text driven style randomization for domain generalized semantic segmentation," Neurocomputing, vol. 676, May 2026.
- [OJ-ITS26] Kyungho Kang, Kyungok Yang, and Jun Won Choi\*, "RAISA: A Vision-based Intelligent Safety Guidance Agent for Railway Operations via Modular Prompt-Orchestrated Reasoning," IEEE Open Journal of Intelligent Transportation Systems, vol. 7, pp. 600-614, Feb. 2026.
- [PrePrint] Junyong Yun, Jungho Kim, ByungHyun Lee, Dongyoung Lee, Sehwan Choi, and Jun Won Choi "CarPLAN: Context-Adaptive and Robust Planning with Dynamic Scene Awareness for Autonomous Driving" Submitted 〔심사 중〕
- [PrePrint] Minjae Seong, Jisong Kim, Geonho Bang, Hawook Jeong, Jun Won Choi\*, "MR-Occ: Efficient Camera-LiDAR 3D Semantic Occupancy Prediction Using Hierarchical Multi-Resolution Voxel Representation," arXiv:2412.20480 〔arXiv 사전 공개본〕

**2025**

- [NeurIPS25] Park Jae Hyun, Konyul Park, Daehun Kim, Junseo Park, Jun Won Choi\*, "Layer-Wise Modality Decomposition for Interpretable Multimodal Sensor Fusion," Neural Information Processing Systems (NeurIPS), Dec. 2025.
- [ICCV25] Geonho Bang, Minjae Seong, Jisong Kim, Geunju Baek, Daye Oh, Junhyung Kim, Junho Koh, and Jun Won Choi\*, "RCTDistill: Cross-Modal Knowledge Distillation Framework for Radar-Camera 3D Object Detection with Temporal Fusion," International Conference on Computer Vision (ICCV) 2025.
- [ICCV25] Changwon Kang, Jisong Kim, Hongjae Shin, Junseo Park, and Jun Won Choi\*, "MAESTRO: Task-Relevant Optimization via Adaptive Feature Enhancement and Suppression for Multi-task 3D Perception," International Conference on Computer Vision (ICCV) 2025.
- [TITS25] Junho Koh, Youngwoo Lee, Jungho Kim, Dongyoung Lee, and Jun Won Choi\*, "OnlineBEV: Recurrent Temporal Fusion in Bird's Eye View Representations for Multi-Camera 3D Perception," IEEE Trans. Intelligent Transportation Systems, vol 26, no 11, pp. 20618 - 20627, Nov. 2025.
- [NC25] Kyoung Ok Yang, Junho Koh, and Jun Won Choi\*, "Unified Contrastive Fusion Transformer for Multimodal Human Action Recognition," Neurocomputing, vol. 655, pp. 1-12, Nov. 2025.
- [SR25] Kyungok Yang, So Young Kim, Chang Won Kang, Jeong Seon Choi, Yong Bae Ji, Kyung Tae, Jun Won Choi\*, and Changmyeon Song\*, "Diagnosis of Unilateral Vocal Fold Paralysis using Auto-diagnostic Deep Learning Model" Scientific Reports, vol. 15, pp. 1-10, July 2025.
- [CVPR25] Konyul Park, Yecheol Kim, Daehun Kim, and Jun Won Choi\*, "Resilient Sensor Fusion under Adverse Sensor Failures via Multi-Modal Expert Fusion," IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), June 2025.
- [AAAI25] Jungho Kim, Changwon Kang, Dongyoung Lee, Sehwan Choi, and Jun Won Choi\*, "ProtoOcc: Accurate, Efficient 3D Occupancy Prediction Using Dual Branch Encoder-Prototype Query Decoder," AAAI Conference on Artificial Intelligence, Feb. 2025.
- [AAAI25] Taein Son, Soo Won Seo, Jisong Kim, Seok Hwan Lee, and Jun Won Choi\*, "JoVALE: Detecting Human Actions in Video Using Audiovisual and Language Contexts," AAAI Conference on Artificial Intelligence, Feb. 2025.
- [T-IV24] Yecheol Kim, Junho Lee, Changsoo Park, Hyoung won Kim, Inho Lim, Christopher Chang, and Jun Won Choi\*, "Semi-Supervised Domain Adaptation Using Target-Oriented Domain Augmentation for 3D Object Detection" IEEE Trans. Intelligent Vehicles, vol. 10, pp. 562-752, Jan. 2025.

**2024**

- [NeurIPS24] Jisong Kim, Minjae Seong, and Jun Won Choi\*, "CRT-Fusion: Camera, Radar, Temporal Fusion Using Motion Information for 3D Object Detection," Neural Information Processing Systems (NeurIPS), Dec. 2024.
- [NC24] Seok Hwan Lee, Taein Son, Soo Won Seo, Jisong Kim, and Jun Won Choi\*, "JARViS: Detecting Actions in Video Using Unified Actor-Scene Context Relation Modeling," NeuroComputing, vol. 610, pp. 128616, Dec. 2024.
- [ECCV24] (Oral presentation) Sehwan Choi, Jungho Kim, Hongjae Shin, and Jun Won Choi\*, "Mask2Map: Vectorized HD Map Construction Using Bird's Eye View Segmentation Masks," European Conference on Computer Vision (ECCV), Sept. 2024.
- [ECCV24] Jae Soon Baik, In Young Yoon, Kun Hoon Kim, and Jun Won Choi\*, "Distribution-Aware Robust Learning from Long-Tailed Data with Noisy Labels," European Conference on Computer Vision (ECCV), Setp. 2024.
- [CVPR24] Geonho Bang, Kwangjin Choi, Jisong Kim, Dongsuk Kum, and Jun Won Choi\*, "RadarDistill: Boosting Radar-based Object Detection Performance via Knowledge Distillation from LiDAR Features," IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), June 2024.
- [ICRA24] Jisong Kim, Minjae Seong, Geonho Bang, Dongsuk Kum, and Jun Won Choi\*, "RCM-Fusion: Radar-Camera Multi-Level Fusion for 3D Object Detection," IEEE International Conference on Robotics and Automation (ICRA), May 2024.
- [ICRA24] Konyul Park, Yecheol Kim, Junho Koh, Byungwoo Park, and Jun Won Choi\*, "Fine-Grained Pillar Feature Encoding Via Spatio-Temporal Virtual Grid for 3D Object Detection," IEEE International Conference on Robotics and Automation (ICRA), May 2024.
- [ICRA24] Jisong Kim, Geonho Bang, Kwangjin Choi, Minjae Seong, Jaechang Yoo, Eunjong Pyo, and Jun Won Choi\*, "PillarGen: Enhancing Radar Point Cloud Density and Quality via Pillar-based Point Generation Network," IEEE International Conference on Robotics and Automation (ICRA), May 2024. (Joint work with HL Klemove)
- [HPCA24] Minjae Lee, Seongmin Park, Hyungmin Kim, Minyong Yoon, Janghwan Lee, Jun Won Choi, Nam Sung Kim, Mingu Kang, Jungwook Choi\*, "SPADE: Sparse Pillar-based 3D Object Detection Accelerator for Autonomous Driving" IEEE International Symposium on High-Performance Computer Architecture (HPCA), March 2024.
- [PR24] Jae Soon Baik, In Young Yoon, and Jun Won Choi\*, "DBN-Mix: Training Dual Branch Network Using Bilateral Mixup Augmentation for Long-tailed Visual Recognition," Pattern Recognition, vol. 147, March 2024.
- [PrePrint] Yecheol Kim, Konyul Park, Minwook Kim, Dongsuk Kum, and Jun Won Choi\* "3D Dual-Fusion: Dual-Domain Dual-Query Camera-LiDAR Fusion for 3D Object Detection," arXiv:2211.13529. 〔arXiv 사전 공개본〕

**2023**

- [NeurIPS23] Jong Wook Bae, Jungho Kim, Junyong Yun, Changwon Kang, Jeongseon Choi, Chanhyeok Kim, Junho Lee, Jungwook Choi, and Jun Won Choi\*, "SiT Dataset: Socially Interactive Pedestrian Trajectory Dataset for Social Navigation Robots," Neural Information Processing Systems (NeurIPS) Dataset and Benchmarks Track 2023.
- [ICCV23] Sehwan Choi, Jungho Kim, Junyong Yun, and Jun Won Choi\*, "R-Pred: Two-Stage Motion Prediction Via Tube-Query Attention-Based Trajectory Refinement," International Conference on Computer Vision (ICCV) 2023.
- [ICCV23] Youngseok Kim, Juyeb Shin, Sanmin Kim, In-Jae Lee, Jun Won Choi, and Dongsuk Kum\*, "CRN: Camera Radar Net for Accurate, Robust, Efficient 3D Perception," International Conference on Computer Vision (ICCV) 2023.
- [AAAI23] Junho Koh, Junhyung Lee, Youngwoo Lee, Jaekyum Kim, and Jun Won Choi\*, "MGTANet: Encoding Sequential LiDAR Points Using Long Short-Term Motion-Guided Temporal Attention for 3D Object Detection," AAAI Conference on Artificial Intelligence 2023, 37(1), 1179-1187. (code available: https://github.com/HYjhkoh/MGTANet.git)
- [AAAI23] Youngseok Kim, Sanmin Kim, Jun Won Choi, and Dongsuk Kum\*, "CRAFT: Camera-Radar 3D Object Detection with Spatio-Contextual Fusion Transformer," AAAI Conference on Artificial Intelligence 2023, 37(1), 1160-1168.
- [ICRA23] Junhyung Lee, Junho Koh, Youngwoo Lee, and Jun Won Choi\*, "D-Align: Dual Query Co-attention Network for 3D Object Detection Based on Multi-frame Point Cloud Sequence," IEEE International Conference on Robotics and Automation (ICRA), London, UK, 2023, pp. 9238-9244. (code available: https://github.com/junhyung-SPALab/D-Align)
- [TWC23] Hyunwoo Park, Jeongwan Kang, Sangwoo Lee, Jun Won Choi, and Sun Woo Kim\*, "Deep Q-Network Based Beam Tracking for Mobile Millimeter-Wave Communications," IEEE Trans. Wireless Communications, vol. 22, no. 2, pp. 961-971, Feb. 2023.
- [RAL23] Sanmin Kim, Hyeongseok Jeon, Junwon Choi, and Dongsuk Kum\*, "Diverse Multiple Trajectory Prediction Using a Two-stage Prediction Network Trained with Lane Loss," IEEE Robotics and Automation Letters," vol. 8, no. 4, pp. 2038-2045, April. 2023.
- [T-ITS23] Youngseok Kim, Sanmin Kim, Sangmin Sim, Jun Won Choi, and Dongsuk Kum\*, "Boosting Monocular 3D Object Detection with Object-Centric Auxiliary Depth Supervision," IEEE Trans. Intelligent Transportation Systems, vol. 24, no. 2, pp. 1801-1813, Feb. 2023.
- [T-ITS23] Hyeongseok Jeon, Sanmin Kim, Kibeom Lee, Daejun Kang, Jun Won Choi, and Dongsuk Kum\*, "Are Reactions to Ego Vehicles Predictable Without Data?: A Semi-Supervised Approach," IEEE Trans. Intelligent Transportation Systems, vol. 24, no. 6, pp. 6477-6490, June 2023.

**2022**

- [AAAI22] Junho Koh, Jaekyum Kim, Jinhyuk Yoo, Yecheol Kim, Dongsuk Kum, and Jun Won Choi\*, "Joint 3D Object Detection and Tracking Using Spatio-Temporal Representation of Camera Image and LiDAR Point Clouds," AAAI Conference on Artificial Intelligence, 36(1), 1210-1218.
- [ACCV22] Jae Soon Baik, In Young Yoon, and Jun Won Choi\*, "ST-CoNAL: Consistency-Based Acquisition Criterion Using Temporal Self-ensemble for Active Learning," Asian Conference on Computer Vision (ACCV) 2022, pp. 3274-3290.
- Jun Ho Lee, Jae Soon Baik, Tae Hwan Hwang, and Jun Won Choi\*, "Learning from data with noisy labels using temporal self-ensemble," arXiv:2207.10354. 〔arXiv 사전 공개본〕
- 배종욱, 이영우, 고준호, 이재영, 최준원, "카메라-라이다 센서 융합을 위한 캘리브레이션 기법 소개," 한국자동차공학회 논문집 제30권 제10호

**2021**

- [CVPR21] ByeoungDo Kim, Seong Hyeon Park, Seokhwan Lee, Elbek Khoshimjonov, Dongsuk Kum, Junsoo Kim, Jeong Soo Kim, and Jun Won Choi\*, “LaPred: Lane-Aware Prediction of Multi-Modal Future Trajectories of Dynamic Agents,” IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) 2021, Nashville, TN, USA, 2021, pp. 14631-14640. (code available: https://github.com/bdokim/LaPred)
- [ICRA21] Junho Koh, Jaekyum Kim, Younji Shin, Byeongwon Lee, Seungji Yang, and Jun Won Choi\*, "Joint Representation of Temporal Image Sequences and Object Motion for Video Object Detection," IEEE International Conference on Robotics and Automation (ICRA) 2021, pp. 13370-13376.
- [JG21] Younji Shin, Hyunsoo Cho, Hyo Chan Jeong, Mincheol Seong, and Jun-Won Choi\*, Won June Lee\*, "Deep Learning-based Diagnosis of Glaucoma Using Wide-field Optical Coherence Tomography Images," Journal of Glaucoma, vol. 30(9), pp. 803-812, Sep 2021.
- [T-COM21] Sun Hong Lim, Sunwoo Kim, Byonghyo Shim, and Jun Won Choi\*, "Deep Learning-Based Beam Tracking for Millimeter-Wave Communications Under Mobility," IEEE Trans. on Communications, vol. 69, no. 11, pp. 7458-7469, Nov. 2021.
- [ACCESS21] Jangho Kwon, Jihyeon Ha, Da-Hye Kim, Jun Won Choi, and Laehyun Kim\*, "Emotion Recognition Using a Glasses-Type Wearable Device via Multi-Channel Facial Responses," IEEE Access, vol. 9, pp. 146392-146403, Oct. 2021.

## 연락과 위치

- 교수 연구실: 서울시 관악구 서울대학교 220동 318호[^faculty][^eceprof]
- 교수 전화: 02-880-9527[^faculty][^eceprof]
- 교수 이메일: junwchoi@snu.ac.kr[^faculty]
- 학부생 인턴십: 누리집 첫 화면은 여름·겨울 학부생 인턴십 지원을 받으며 문의는 junwchoi@snu.ac.kr로 하라고 적는다.[^home]
- 학부 주소: 08826 서울특별시 관악구 관악로 1 서울대학교 전기·정보공학부[^ecelabv]
[^home]: 연구실 누리집 첫 화면 <https://adr.snu.ac.kr/> (연구실 소개, 학부생 인턴십 안내, 2026-10-23 열람)
[^faculty]: 누리집 Faculty 페이지 <https://adr.snu.ac.kr/faculty> (Contact, Biography, Education, Experience, Activity 칸, 2026-10-23 열람)
[^members]: 누리집 Members 페이지 <https://adr.snu.ac.kr/members> (Ph.D / Joint M.S. Ph.D. Students, M.S. Students, Alumni (Ph. D.), Alumni (M. S.) 칸, 2026-10-23 열람)
[^research]: 누리집 Research 페이지 <https://adr.snu.ac.kr/research> (Perception, Planning, Data Engineering 칸, 2026-10-23 열람)
[^pubs]: 누리집 Publications 페이지 <https://adr.snu.ac.kr/publications> (International Journals / Highlighted Conference Papers 칸과 International Conferences 칸, 2026-10-23 열람)
[^ecelab]: 서울대학교 전기·정보공학부 연구실 목록 <https://ece.snu.ac.kr/research-faculty/research/lab> (연구그룹별 연구실, 2026-10-23 열람)
[^ecelabv]: 서울대학교 전기·정보공학부 연구실 상세(피지컬 인공지능 연구실) <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=144> (2026-10-23 열람)
[^ecelist]: 서울대학교 전기·정보공학부 전임교수 목록 <https://ece.snu.ac.kr/research-faculty/faculty/full-time> (2026-10-23 열람)
[^eceprof]: 서울대학교 전기·정보공학부 교수 상세(최준원) <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p902> (분야, 학력, 주요경력, 2026-10-23 열람)
[^gsai]: 서울대학교 협동과정 인공지능 전공 교수진 목록 <https://gsai.snu.ac.kr/%ea%b5%90%ec%88%98%ec%a7%84-%eb%aa%a9%eb%a1%9d/> (2026-10-23 열람)
[^p1]: K. Park, Y. Kim, D. Kim, J. W. Choi, 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 6720-6729 (2025). <https://doi.org/10.1109/cvpr52734.2025.00630> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: G. Bang 외, J. W. Choi, 2025 IEEE/CVF International Conference on Computer Vision (ICCV), 25315-25324 (2025). <https://doi.org/10.1109/iccv51701.2025.02348> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Kim 외, J. W. Choi, Proceedings of the AAAI Conference on Artificial Intelligence 39, 4284-4292 (온라인 2025-04-11). <https://doi.org/10.1609/aaai.v39i4.32450> 초록 기준.
[^p4]: J. Kim 외, J. W. Choi, IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) 2026, arXiv:2602.18887. <https://arxiv.org/abs/2602.18887> 초록 기준(arXiv 판).
[^p5]: K. Park 외, J. W. Choi, 2026 IEEE International Conference on Robotics and Automation (ICRA), 2370-2377 (2026). <https://doi.org/10.1109/icra57385.2026.11695784> 초록 기준(arXiv 판, arXiv:2603.09175).
[^p6]: K. O. Yang 외, J. W. Choi, IEEE Robotics and Automation Letters 11, 12480-12486 (2026). <https://doi.org/10.1109/lra.2026.3731854> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: T. Son 외, J. W. Choi, Proceedings of the AAAI Conference on Artificial Intelligence 39, 6940-6949 (온라인 2025-04-11). <https://doi.org/10.1609/aaai.v39i7.32745> 초록 기준.
[^p8]: S. W. Seo 외, J. W. Choi, IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) 2026, arXiv:2604.02071. <https://arxiv.org/abs/2604.02071> 초록 기준(arXiv 판).

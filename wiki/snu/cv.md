# 컴퓨터비젼 연구실 (Computer Vision Laboratory, CVLab)

**서울대학교 공과대학 전기·정보공학부 · 이경무 교수, 한보형 교수**

- 분야: 컴퓨터 비전(영상 복원과 초해상화, 사진에서 3차원 사람·손 복원, 3차원·4차원 장면 복원), 생성 모델(확산 모델로 하는 동영상 생성과 빠른 표본 추출), 기계학습(신경망 양자화·가지치기, 연합 학습·점진 학습, 동영상·멀티모달 이해)
- 대분야: 컴퓨팅·AI
- 태그: 컴퓨터 비전[^home][^p1][^p2], 3차원 복원·인식[^home][^p3][^p5], 생성 인공지능[^p7][^p8]
- 홈페이지: <https://cv.snu.ac.kr/> (이경무 교수 페이지 <https://cv.snu.ac.kr/index.php/~kmlee/>, 한보형 교수 페이지 <https://cv.snu.ac.kr/index.php/~bhhan/>)
- 근거와 출처: [Computer Vision Laboratory 근거 페이지](cv-sources.md)

> 누리집이 이경무 교수와 한보형 교수를 함께 올리는 컴퓨터 비전 연구실이다. 디지털 영상에서 물체와 사람, 3차원 환경의 정보를 뽑아내고 되살리고 알아보는 일을 연구해 왔고, 최근 논문은 잡음이 끼거나 해상도가 낮은 영상의 복원, 신경망을 가볍게 만드는 방법, 사진에서 3차원 사람·손 모양을 되살리는 복원, 3차원·4차원 장면 복원, 확산 모델로 동영상을 만들고 표본 추출을 빠르게 하는 생성 연구에 걸쳐 있다.[^faculty][^home][^p1][^p2][^p3][^p5][^p6][^p7]

## 무엇을 연구하나

연구실 누리집의 Faculty 페이지는 서울대학교 전기·정보공학부 이경무 교수와 한보형 교수를 함께 올린다.[^faculty][^ecefac] 누리집 첫 화면에 따르면 컴퓨터 비전 연구실(Computer Vision Laboratory)은 2003년 서울대에 세워졌고, 이경무 교수의 지도 아래 컴퓨터 비전(컴퓨터가 사진·영상 속 내용을 알아보게 하는 분야)의 여러 주제를 연구하고 개발해 왔다. 연구실은 사람에 가까운 인공지능을 갖추도록 디지털 영상에서 물체와 사람, 3차원 환경의 정보를 뽑아내고, 되살리고, 알아보는 일에 주로 힘쓴다고 적는다. 최근의 주요 관심사로는 딥러닝, 영상 복원, 영상 검색, 장면 이해, 물체 추적·분할, 사람 자세 추정, 의료 영상, 3차원 비전을 든다.[^home] 학부 교수 상세는 두 교수의 연구실을 모두 「컴퓨터비젼 연구실」로 적고, 학부 연구실 목록은 이 누리집을 연결한 「컴퓨터비젼 연구실」을 한보형 교수 이름으로 올린다.[^eceprof][^ecehan][^ecelab][^ecelabv] 학부 교수 상세는 이경무 교수의 분야를 컴퓨터 비젼, 인공지능, 머신러닝, 영상처리로, 한보형 교수의 분야를 Computer Vision, Machine Learning, Deep Learning으로 적는다.[^eceprof][^ecehan] 누리집의 논문 목록과 소식은 두 교수의 것을 한데 싣는다.[^pubs][^news] 아래 네 갈래 가운데 첫째와 둘째는 주로 이경무 교수의 논문, 넷째는 한보형 교수의 논문에서 나오고, 셋째에는 두 교수의 논문이 함께 있다.

첫째 갈래는 **영상 복원·초해상화와 가벼운 신경망**이다. 잡음이 끼거나 흐리거나 해상도가 낮은 영상을 깨끗하고 선명한 영상으로 되살리는 연구로, 초해상화는 해상도가 낮은 영상에서 해상도가 높은 영상을 만들어 내는 일이다. 대표 논문에서는 미리 학습된 확산 모델(잡음을 조금씩 걷어 내며 영상을 만들어 내는 생성 모델)을 고치지 않고 저해상도 입력을 그 모델이 학습한 분포에 맞게 옮겨 한 단계만으로 초해상화하는 DM-SR을 제안했고,[^p1] 초해상화 신경망을 양자화(신경망의 값을 적은 비트 수로 나타내 계산을 줄이는 방법)할 때 입력 영상의 국소 내용에 따라 영역과 층마다 비트 수를 바꾸는 CADyQ를 내놓았다.[^p2] 최근 논문 목록에는 이경무 교수의 논문으로 임의의 기하 변환 아래의 초해상화 SRWarp(CVPR 2021), 실제 잡음을 흉내 내는 생성 모형 C2N(ICCV 2021), 실제 사진의 자기 지도 잡음 제거 AP-BSN(CVPR 2022), 동적 장면의 흐림 제거(ICLR 2022), 사실적인 초해상화를 위한 내용 인식 국소 GAN(ICCV 2023), 3차원 장면으로 만든 흐림 제거 데이터셋 GS-Blur(NeurIPS 2024), 확산 모델의 사전 지식을 쓰는 과제 중심 영상 복원(ICCV 2025), 복원을 위해 손상을 배우는 방법과 초해상화 신경망 WARP(이상 ECCV 2026)가 있다. 한보형 교수의 논문으로는 적대적 주파수 섞기로 하는 튼튼한 잡음 제거(CVPR 2024), 정답 영상을 넘어서는 감독 신호로 하는 영상 복원(CVPR 2026), 잡음을 변환하도록 배워 하는 튼튼한 잡음 제거(CVPR 2026 Findings), 공간마다 다른 특징 변환으로 하는 가변 압축률 영상 압축(ICCV 2021)이 있다.[^pubs] 신경망을 가볍게 만드는 쪽으로는 초해상화 신경망의 채널별 분포 인식 양자화 DAQ와 배치 정규화로 중요한 필터를 가려내는 연구(이상 WACV 2022), 영상 복원을 위한 세밀한 구조적 희소성(CVPR 2022), 초해상화 신경망의 비트 수를 그때그때 정하는 AdaBM(CVPR 2024), 학습 자료 없이 하는 동적 양자화(WACV 2025), 가지치기로 찾은 희소 신경망의 부호 정보를 다룬 연구(ICLR 2025)가 이경무 교수의 논문이고, 지식 증류(큰 신경망이 배운 것을 작은 신경망에 옮겨 가르치는 일)에서 학생 신경망이 배우기 쉬운 교사 신경망을 학습하는 연구(NeurIPS 2021), 영상을 래스터 주사 순서로 읽는 작은 모델 RaSNet(CVPR 2021), 생성 모델 압축(NeurIPS 2022), 전문가 혼합(MoE, Mixture-of-Experts) 모델의 전문화(CVPR 2026)가 한보형 교수의 논문이다. 이경무 교수는 메타학습(여러 과제를 겪으며 새 과제를 빨리 배우는 방법 자체를 배우는 일)으로 소수 예시 학습의 손실 함수를 과제에 맞춰 바꾸는 연구(ICCV 2021 ORAL)와 소수 예시 점진 학습을 위한 표현 학습 CLOSER(ECCV 2024)도 냈다.[^pubs]

둘째 갈래는 **사진 한 장에서 3차원 사람·손 복원**이다. 사진이나 동영상에서 사람 몸과 손, 사람이 다루는 물체의 3차원 모양과 자세를 알아내는 이경무 교수 쪽 연구다. 대표 논문에서는 물체에 가려진 손의 3차원 메시(삼각형 면을 이어 만든 3차원 모형)를 추정할 때 가려진 영역의 정보를 오히려 활용하는 HandOccNet을 제안했고,[^p3] 사진 한 장에서 사람과 물체를 함께 3차원으로 복원할 때 접촉 정보에 더해 상호작용을 설명한 글과 겉모습 단서를 맞추는 TeHOR를 내놓았다.[^p4] 최근 논문 목록에는 동영상에서 시간적으로 일관된 3차원 사람 자세·형태 추정(CVPR 2021), 붐비는 실제 장면의 3차원 사람 메시 추정(CVPR 2022), 실제 환경의 옷 입은 사람 3차원 복원(ECCV 2022), 흐린 사진 한 장에서 3차원 손 메시 시퀀스 복원(CVPR 2023), 접촉 기반 정제 트랜스포머로 사람과 물체를 함께 복원하는 연구(CVPR 2024), 흐린 영상과 이벤트 스트림으로 하는 3차원 손 시퀀스 복원(ECCV 2024), 옷과 몸을 나눠 복원하는 DeClotH(CVPR 2025), 부위 안내 텍스처로 하는 3차원 사람 복원 PARTE(ICCV 2025), 손 접촉 추정(NeurIPS 2025), 발 접촉 추정(CVPR 2026)이 있다.[^pubs] 사람 동작과 수어 쪽으로는 여러 행동 이름으로 긴 3차원 동작을 만드는 연구(AAAI 2023 ORAL), 수어 인식을 위한 신체 부위별 3차원 동작 맥락 학습(ICCV 2023), 여러 문장으로 긴 3차원 동작을 만드는 T2LM(CVPR 2024 워크숍), 수어 생성 SIGNER(ECCV 2026)가 있다.[^pubs]

셋째 갈래는 **3차원·4차원 장면 복원**이다. 여러 장의 사진이나 동영상으로 3차원 장면을 되살리고, 시간에 따라 움직이는 장면까지 다루는 연구로 두 교수의 논문이 함께 있다. 대표 논문에서 이경무 교수 연구진은 주위 360°를 한 장에 담는 전방위 영상에 맞춘 3D 가우시안 스플래팅 렌더링 과정 ODGS를 제안했고,[^p5] 한보형 교수 연구진은 카메라 하나로 찍은 일상 동영상에서 움직이는 장면을 되살리는 4D 가우시안 스플래팅에, 관측이 적은 영역에만 사전 지식을 더하는 불확실성 인식 정규화를 넣었다.[^p6] 최근 논문 목록에는 이경무 교수의 논문으로 움직임 흐림이 심한 영상에서 신경 방사장을 학습하는 ExBluRF(ICCV 2023), 적은 수의 사진으로 하는 3D 가우시안 스플래팅의 깊이 정규화(CVPR 2024 워크숍), 특정 분야에 매이지 않는 3D 가우시안 스플래팅 장면 생성 LucidDreamer(IEEE TVCG 2025), 전방위 영상용 OmniSplat(CVPR 2025), 분할 지도를 조건으로 글에서 3차원 세계를 만드는 Map2World(ECCV 2026)가 있다. 한보형 교수의 논문으로는 적은 수의 사진으로 하는 신경 방사장 렌더링 InfoNeRF(CVPR 2022), 신경 암시 함수를 섞어 만드는 생성 신경장(NeurIPS 2023), 가우스 과정으로 하는 확률적 4D 가우시안 스플래팅 GP-4DGS와 물체 여러 개의 물리적 상호작용을 담은 동적 새 시점 합성 벤치마크 PhysGaia(이상 CVPR 2026)가 있다.[^pubs] 3차원 형상과 점구름(3차원 공간 속 점들의 모음) 쪽으로는 이경무 교수의 암시적 대수 곡면 3차원 형상 복원 3DIAS(ICCV 2021), 자기 지도 점구름 완성 ACL-SPC(CVPR 2023), CNC 가공 작업을 위한 자기 지도 학습 CNC-Net(CVPR 2024), 점마다 표면 방향 정보가 붙어 있지 않은 점구름에서 3D 프린팅 G-code를 만드는 PrintAnything(ECCV 2026)이 있다.[^pubs]

넷째 갈래는 **확산 모델로 하는 생성과 빠른 표본 추출**이다. 잡음에서 출발해 조금씩 잡음을 걷어 내며 영상을 만드는 확산 모델로 새 영상과 동영상을 만들고, 그 생성 과정을 더 적은 계산으로 정확하게 하는 한보형 교수 쪽 연구다. 대표 논문에서는 미리 학습된 글-동영상 확산 모델로 추가 학습 없이 끝없이 긴 동영상을 만드는 추론 기법 FIFO-Diffusion을 제안했고,[^p7] 중간 단계의 여러 풀이를 외삽해 계산 횟수를 늘리지 않고 표본의 정확도를 높이는 표본 추출 방법 RX-DPM을 내놓았다.[^p8] 최근 논문 목록에는 관측으로 이끄는 확산 확률 모델(CVPR 2024), 글로 지시하는 영상 변환을 위한 조건부 점수 안내(NeurIPS 2023), 프롬프트 보간으로 잡음을 고치는 확산 기반 영상 변환(ECCV 2024), 저해상도 편집으로 하는 고해상도 편집(CVPR 2026), 동적 선호로 확산 표본 추출기를 최적화하는 연구(ECCV 2026), 일정한 메모리로 하는 비마르코프 표본 추출기 Score-Repellent Monte Carlo(ICML 2026)가 있고, 여러 판별자를 쓰는 GAN인 MCL-GAN과 국소 계층 자기회귀 영상 생성(이상 NeurIPS 2022), 비지도 글-영상 생성(CVPR 2023), 벡터 그래픽과 배치를 만드는 무한 정밀도 자기회귀 모델(ICML 2026)도 있다.[^pubs] 이경무 교수의 논문으로는 영상 확산 모델로 실시간 대화형 콘텐츠를 만드는 SemanticDraw(CVPR 2025)가 있다.[^pubs]

이 밖에 한보형 교수의 최근 논문 목록에는 동영상과 글을 함께 다루는 연구로 동영상 대형 언어 모델 안의 정보 흐름을 밝히는 Map the Flow(ICLR 2026), 장면 그래프를 모아 하는 세밀한 동영상 설명문 생성(ICML 2025), 문자 인식 없이 하는 문서 이해(NeurIPS 2024), 시간 맥락을 쓰는 동영상 행동 인식(ECCV 2024), 글 기반 부드러운 마스크로 하는 멀티모달 표현 학습(CVPR 2023)이 있다. 여러 기기가 자료를 모으지 않고 함께 모델을 학습하는 연합 학습 쪽으로는 다층 분기 정규화(ICML 2022), 클라이언트 기울기를 가속하는 통신 효율 연합 학습과 완화된 대조 학습(이상 CVPR 2024), 이질적인 연합 일반화 범주 발견 FedLPA(NeurIPS 2025)가 있고, 새 범주를 차례로 더 배우는 범주 점진 학습(CVPR 2022, CVPR 2023, AAAI 2024)과 머신 언러닝(학습한 모델에서 특정 자료의 영향을 지우는 일, WACV 2025) 논문도 있다.[^pubs] 이경무 교수의 최근 논문 목록에는 의료 영상 논문으로 혈관 연결 예측으로 망막 동맥과 정맥을 가리는 방법(Applied Sciences 2021), 초음파 영상에서 간 병변을 함께 분할·분류하는 딥러닝(European Radiology 2021), 정상 영상 생성으로 흉부 X선의 이상을 찾는 방법(IEEE Access 2023)이 있고, 자기회귀 변환으로 하는 영상 정렬(ICCV 2025)과 미분 가능한 영상 벡터화 Vector Scaffolding(ECCV 2026)도 있다.[^pubs] 국내 학회로는 이경무 교수 연구진이 영상처리 및 이해에 관한 워크샵에 2021–2023년 9편을 냈다.[^dompubs]

## 주요 연구 주제

### 1. 영상 복원·초해상화와 가벼운 신경망

미리 학습된 확산 모델을 고치지 않고 쓰는 초해상화(DM-SR), 초해상화 신경망의 내용 인식 동적 양자화(CADyQ), 잡음 제거와 흐림 제거, 신경망 가지치기와 지식 증류.[^p1][^p2][^pubs] 대표 논문 1, 2.

### 2. 사진 한 장에서 3차원 사람·손 복원

가려진 손의 3차원 메시 추정(HandOccNet), 글 설명을 쓰는 사람·물체 3차원 복원(TeHOR), 사람 동작 생성과 수어 인식·생성.[^p3][^p4][^pubs] 대표 논문 3, 4.

### 3. 3차원·4차원 장면 복원

전방위 영상의 3D 가우시안 스플래팅 복원(ODGS), 일상 동영상에서 움직이는 장면을 되살리는 4D 가우시안 스플래팅, 신경 방사장, 3차원 장면 생성과 점구름.[^p5][^p6][^pubs] 대표 논문 5, 6.

### 4. 확산 모델로 하는 생성과 빠른 표본 추출

추가 학습 없이 끝없이 긴 동영상 생성(FIFO-Diffusion), 계산 횟수를 늘리지 않는 정확한 표본 추출(RX-DPM), 확산 모델로 하는 영상 변환과 편집.[^p7][^p8][^pubs] 대표 논문 7, 8.

## 대표 논문

누리집 International Publications 페이지의 2021–2026년 논문 가운데 이경무 교수나 한보형 교수가 마지막 저자인 논문을 네 연구 갈래에서 두 편씩 골랐다(이경무 교수 5편, 한보형 교수 3편). 2026년 논문 두 편을 넣었다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [Bridging the Distribution Gap to Harness Pretrained Diffusion Priors for Super-Resolution](https://openreview.net/forum?id=66Ad0i78lW) · International Conference on Learning Representations (ICLR) 2026 | 확산 모델은 영상이 어떤 모습인지에 관한 사전 지식이 강한 생성 모델로 알려져 있어, 최근 초해상화에 점점 더 많이 쓰인다. 그러나 확산 모델은 가우스 잡음이 섞인 자연 영상으로 학습하므로, 저해상도 입력과 모델의 학습 분포 사이의 차이 때문에 바로 추론에 쓰기 어렵다. 이전 연구는 저해상도 영상을 조건으로 넣어 이 문제를 다뤘지만, 그 미세 조정이 생성 능력을 약하게 만들고 잡음 제거 단계를 여러 번 거쳐야 하는 경우가 많았다. 연구진은 미리 학습된 확산 모델을 고치지 않고 이 차이를 메우는 틀 DM-SR을 내놓았다. 저해상도 입력을 확산 모델의 학습 공간에 맞춘 잠재 분포로 옮기는 영상 인코더를 학습해 모델의 생성 능력을 그대로 살리고, 입력마다 손상 정도에 따라 알맞은 잡음 수준을 스스로 예측해 확산 모델의 시점별 분포에 맞춘다. 실험에서 한 단계의 확산 과정만으로 지각 품질(사람 눈에 보이는 품질)이 뛰어난 초해상화를 보였다.[^p1] | 1저자 Joonkyu Park, 마지막 저자 이경무 (2명) |
| 2 | 2022 | [CADyQ: Content-Aware Dynamic Quantization for Image Super-Resolution](https://doi.org/10.1007/978-3-031-20071-7_22) · Computer Vision – ECCV 2022 (Lecture Notes in Computer Science) | 합성곱 신경망(CNN, 영상의 이웃 화소 묶음마다 같은 필터를 적용해 특징을 뽑는 신경망)으로 영상 초해상화는 크게 발전했지만, 초해상화 신경망은 계산량이 많아 아직 널리 쓰이지 못한다. 양자화가 유망한 해법이지만, 기존 방법은 모든 곳에 같은 비트 수를 쓰는 탓에 8비트보다 적은 비트로 줄이면 정확도가 크게 떨어진다. 연구진은 정확도 손실을 줄이면서 평균 비트 수를 크게 낮추려고, 입력 영상의 국소 내용에 따라 영역과 층마다 알맞은 비트 수를 적응적으로 나눠 주는 내용 인식 동적 양자화 CADyQ를 제안했다. 이를 위해 층과 영상 조각마다 비트 수와 양자화 수준을 정하는 학습 가능한 비트 선택 모듈을 넣었다. 이 모듈은 조각의 영상 기울기(이웃 화소 사이의 밝기 차이) 평균 크기와 그 층에 들어오는 특징의 표준편차로 추정한 양자화 민감도에 따라 움직인다. 여러 초해상화 신경망과 여러 표준 벤치마크에서 계산량을 크게 줄이면서 복원 정확도를 높였다.[^p2] | 1저자 Cheeun Hong, 마지막 저자 이경무 |
| 3 | 2022 | [HandOccNet: Occlusion-Robust 3D Hand Mesh Estimation Network](https://doi.org/10.1109/cvpr52688.2022.00155) · 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | 손은 물체에 심하게 가려지는 일이 많아 3차원 손 메시 추정이 어렵다. 이전 연구는 가려진 영역의 정보를 흔히 무시했지만, 연구진은 가려진 영역이 손과 강하게 관련돼 있어 온전한 3차원 손 메시 추정에 큰 도움이 되는 정보를 줄 수 있다고 보았다. 그래서 가려진 영역의 정보를 영상 특징을 보강하는 보조 수단으로 충분히 활용하는 3차원 손 메시 추정 신경망 HandOccNet을 제안했다. 이를 위해 트랜스포머(자료의 각 부분이 다른 부분을 얼마나 참고할지 계산해 표현을 고치는 신경망 구조) 기반 모듈 두 개를 잇달아 설계했다. FIT(feature injecting transformer)는 손과 가려진 영역의 상관을 고려해 가려진 영역에 손 정보를 넣고, SET(self-enhancing transformer)는 자기 주의(self-attention) 메커니즘으로 FIT의 출력을 다듬는다. 가려진 영역에 손 정보를 넣은 결과, 손과 물체가 서로 가리는 어려운 장면을 담은 3차원 손 메시 벤치마크에서 최고 수준의 성능을 냈다.[^p3] | 1저자 Joonkyu Park(Joonkyu Park, Yeonguk Oh, Gyeongsik Moon에게 누리집 표시 \*), 마지막 저자 이경무 |
| 4 | 2026 | [TeHOR: Text-Guided 3D Human and Object Reconstruction with Textures](https://openaccess.thecvf.com/content/CVPR2026/html/Nam_TeHOR_Text-Guided_3D_Human_and_Object_Reconstruction_with_Textures_CVPR_2026_paper.html) · Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) 2026 | 사진 한 장에서 사람과 물체를 함께 3차원으로 복원하는 연구는 활발하며, 로봇과 디지털 콘텐츠 제작에 중요한 쓰임이 있다. 그러나 기존 방법에는 두 가지 근본적인 한계가 있다. 첫째, 복원이 물리적 접촉 정보에 크게 기대므로 물체를 바라보거나 가리키는 것처럼 닿지 않는 상호작용을 본래 담지 못한다. 둘째, 복원 과정이 주로 국소적인 기하적 가까움에 따라 움직여, 상호작용 전체를 이해하는 데 중요한 전역 맥락을 주는 사람과 물체의 겉모습을 소홀히 한다. 연구진은 두 가지 핵심 설계로 된 틀 TeHOR를 내놓았다. 하나는 접촉 정보에 더해 사람과 물체의 상호작용을 설명한 글을 써서 3차원 복원 결과가 글의 단서와 의미상 맞도록 하는 것으로, 닿지 않는 경우를 포함한 더 넓은 상호작용을 추론하게 한다. 다른 하나는 3차원 사람과 물체의 겉모습 단서를 이 맞춤 과정에 넣어 전체 맥락을 담고, 눈으로 보기에 그럴듯한 복원을 얻는 것이다. 그 결과 정확하고 의미가 일관된 복원을 얻어 최고 수준의 성능을 냈다.[^p4] | 1저자 Hyeongjin Nam, 마지막 저자 이경무 |
| 5 | 2024 | [ODGS: 3D Scene Reconstruction from Omnidirectional Images with 3D Gaussian Splattings](https://doi.org/10.52202/079017-1818) · Advances in Neural Information Processing Systems 37 (NeurIPS 2024) | 전방위 영상(360° 영상)은 한 장으로 장면 전체를 그려 낼 수 있어 3차원 응용에 점점 더 많이 쓰인다. 신경 방사장(NeRF, 여러 방향에서 찍은 사진으로 공간 각 점의 색과 밀도를 신경망이 배워 새 시점의 영상을 그려 내는 방법)에 기반한 기존 연구는 1인칭 시점 영상에서 좋은 3차원 복원 품질을 보였지만 학습과 렌더링(3차원 장면을 화면의 영상으로 그려 내는 일)에 오래 걸린다. 최근 3D 가우시안 스플래팅(가우스 분포 모양의 입자 여러 개로 장면을 나타내고 화면에 투영해 그리는 방법)이 빠른 최적화와 실시간 렌더링으로 주목받지만, 보통 카메라용 래스터화기(3차원 요소를 화면의 화소로 투영해 그리는 계산 과정)를 전방위 영상에 바로 쓰면 두 영상의 광학적 성질이 달라 심하게 일그러진다. 연구진은 기하적 해석을 갖춘 전방위 영상용 래스터화 과정 ODGS를 제안했다. 가우시안마다 단위 구에 접하고 가우시안 중심을 향하는 광선에 수직인 접평면을 정하고, 보통 카메라용 래스터화기로 가우시안을 그 접평면에 투영한 뒤, 투영한 가우시안을 변환·결합해 전방위 영상을 완성한다. 이 해석은 과정에 숨은 가정을 드러내며, 연구진은 이를 수학적으로 증명했다. 전체 과정을 CUDA(그래픽 처리 장치에서 병렬 계산을 하게 하는 프로그래밍 환경)로 병렬화해 NeRF 기반 방법보다 최적화와 렌더링이 100배 빠르다. 여러 데이터셋에서 가장 좋은 복원 품질과 지각 품질을 냈고, 넓은 3차원 장면을 복원할 때도 세밀한 부분을 잘 되살렸다.[^p5] | 1저자 Suyoung Lee(Suyoung Lee, Jaeyoung Chung에게 누리집 표시 \*), 마지막 저자 이경무 |
| 6 | 2024 | [4D Gaussian Splatting in the Wild with Uncertainty-Aware Regularization](https://doi.org/10.52202/079017-4104) · Advances in Neural Information Processing Systems 37 (NeurIPS 2024) | 움직이는 장면을 찍지 않은 새 시점에서 본 모습으로 그려 내는 새 시점 합성(novel view synthesis)은 증강현실과 가상현실을 비롯한 여러 응용에서 중요해지고 있다. 연구진은 카메라 하나로 일상에서 찍은 동영상으로부터 움직이는 장면을 되살리는 4D 가우시안 스플래팅(4DGS, 시간에 따라 움직이는 입자 여러 개로 움직이는 장면을 나타내는 방법) 알고리즘을 제안했다. 이런 실제 동영상에서 기존 연구가 학습 자료에만 지나치게 맞춰지는 과적합 문제를 넘으려고, 관측이 적어 불확실한 영역을 찾아 그 영역에만 확산 모델에 기반한 사전 지식과 깊이의 매끄러움 조건을 더하는 불확실성 인식 정규화를 도입했다. 이 방법은 새 시점 합성 성능과 학습 영상 복원 품질을 함께 높인다. 또 빠르게 움직이는 영역에서는 SfM(Structure from Motion, 여러 사진에서 카메라 위치와 장면의 3차원 점을 함께 구하는 방법)이 믿을 만한 3차원 기준점을 주지 못해 4DGS의 초기화가 어렵다는 문제를 짚었고, 추정한 깊이 지도와 장면 흐름(장면의 각 점이 움직이는 방향과 크기)으로 그런 영역에 가우시안 입자를 채워 넣는 동적 영역 조밀화 방법을 내놓았다. 실험에서 손에 든 단안 카메라(렌즈가 하나인 카메라)로 찍은 동영상의 4DGS 복원 성능이 좋아졌고, 적은 수의 사진으로 하는 정지 장면 복원에서도 가능성 있는 결과를 보였다.[^p6] | 1저자 Mijeong Kim, 마지막 저자 한보형 |
| 7 | 2024 | [FIFO-Diffusion: Generating Infinite Videos from Text without Training](https://doi.org/10.52202/079017-2853) · Advances in Neural Information Processing Systems 37 (NeurIPS 2024) | 미리 학습된 확산 모델을 바탕으로, 글을 조건으로 동영상을 만드는 새 추론 기법 FIFO-Diffusion을 제안했다. 개념상 추가 학습 없이 끝없이 긴 동영상을 만들 수 있다. 잡음 수준이 차례로 높아지는 연속 프레임 여러 장을 대기열(queue)에 넣어 한꺼번에 처리하는 대각선 잡음 제거를 되풀이하며, 잡음이 다 걷힌 프레임을 대기열 앞에서 꺼내고 새 무작위 잡음 프레임을 뒤에 넣는다. 다만 대각선 잡음 제거에는 장단점이 있다. 뒤쪽 프레임이 앞쪽의 더 깨끗한 프레임을 참고할 수 있는 대신, 학습과 추론 사이에 차이가 생긴다. 그래서 학습과 추론의 차이를 줄이는 잠재 분할(latent partitioning)과 앞쪽 프레임을 참고하는 이점을 살리는 미리 보기 잡음 제거(lookahead denoising)를 도입했다. 기준 모델이 주어지면 만들 동영상의 길이와 상관없이 일정한 양의 메모리만 쓰고, 여러 GPU(그래픽 처리 장치)에서 나눠 추론하기에도 알맞다. 기존 글-동영상 생성 모델들에서 제안한 방법이 유망한 결과를 내고 효과가 있음을 보였다.[^p7] | 1저자 Jihwan Kim(Jihwan Kim, Junoh Kang에게 누리집 표시 \*), 마지막 저자 한보형 |
| 8 | 2025 | [Enhanced Diffusion Sampling via Extrapolation with Multiple ODE Solutions](https://openreview.net/forum?id=rCGleSgNBK) · International Conference on Learning Representations (ICLR) 2025 | 확산 확률 모델(DPM, diffusion probabilistic model)은 품질 높은 표본을 만들지만, 표본을 만드는 과정을 여러 번 되풀이해야 해 계산 비용이 크다. 연구진은 리처드슨 외삽(간격을 달리해 구한 근삿값 여러 개를 조합해 오차를 줄이는 수치 계산법)에서 착안해, 수치 오차를 줄이고 수렴 속도를 높이는 상미분방정식(ODE, Ordinary Differential Equation) 기반 표본 추출 방법 RX-DPM을 제안했다. 중간 시점에서 구한 여러 ODE 풀이로 잡음을 걷어 낸 예측값을 외삽해, 모델 계산 횟수(NFE, Number of Function Evaluations)를 늘리지 않고 최종 표본의 추정 정확도를 크게 높인다. 시간 격자를 고르게 나눈다고 가정하는 표준 리처드슨 외삽과 달리, 기준이 되는 표본 추출 방법에서 얻은 국소 절단 오차(한 단계 계산에서 생기는 오차)를 길잡이로 삼아 임의의 시점 배치에 맞춘 더 일반적인 식을 세웠다. 방법이 단순해 계산 부담을 크게 늘리지 않고 수치 해를 정확히 추정하며, 여러 DPM과 풀이 방법에 손쉽게 붙여 쓸 수 있다. 또 명시적인 오차 추정치를 주어, 주된 오차 항의 차수가 높아질수록 더 빨리 수렴함을 보였다. 실험에서 표본 추출 반복 횟수를 늘리지 않고 생성 표본의 품질을 높였다.[^p8] | 1저자 Jinyoung Choi, 마지막 저자 한보형 |

## 교수와 전문 분야

이경무 교수(Kyoung Mu Lee)는 서울대학교 전기·정보공학부 교수다.[^ecefac][^eceprof] 연구실 소식에 따르면 2022년 9월 1일 서울대학교 석좌교수(Chair-Professor)로 임명됐다.[^news] 서울대학교 제어계측공학과에서 학사(1984)와 석사(1986)를, 미국 University of Southern California에서 전기공학 박사(1993)를 받았다.[^eceprof][^kmlee] 학부 교수 상세의 주요경력은 USC Signal & Image Processing Institute 연구원(Research Associate, 1993–1994), 홍익대학교 전자전기공학부 조교수/부교수(1995–2013년으로 적힘), 2003년부터의 서울대학교 전기정보공학부 교수, 서울대학교 공과대학 부학장(2009–2011), 자동화시스템 공동연구소 소장(2012–2014), 2020년부터의 서울대학교 대학원 협동과정 인공지능전공 주임교수다.[^eceprof] 누리집 교수 소개는 University of California, San Diego의 방문 과학자(visiting scientist, 2011–2012) 경력도 적는다.[^kmlee]

학부 교수 상세는 이경무 교수의 전공을 컴퓨터 비젼, 인공지능, 머신러닝, 영상처리로, Research Interest를 Computer Vision, Artificial Intelligence, Machine Learning, Robot Vision, Image and Video Processing, Multimedia로 적는다.[^eceprof] 누리집 교수 소개는 교수의 연구 관심이 컴퓨터 비전과 기계학습의 넓은 영역에 걸치며 저수준 비전(low-level vision, 잡음 제거나 초해상화처럼 화소 단위로 영상의 질을 다루는 문제), 시각 추적과 항법, 3차원 복원, 사람 자세·형태 추정, 동영상 분석을 포함한다고 적고, 교수가 70편이 넘는 학술지 논문과 180편이 넘는 학회 논문의 공저자라고 적는다.[^kmlee] 같은 소개에 따르면 교수는 영상 복원용 심층 합성곱 신경망을 설계할 때 전역 건너뛰기 연결(global skip (residual)-connection, 입력을 출력 쪽에 바로 더해 주는 연결)을 쓰는 생각을 내놓았고, 이 생각은 VDSR(Very Deep Super-Resolution) 알고리즘(CVPR 2016)에 처음 쓰였다. 누리집은 이 건너뛰기 연결 개념이 저수준 비전 문제를 푸는 CNN 방법의 사실상 표준 기법이 됐다고 적는다. 교수는 이어 더 깊은 신경망 EDSR(Enhanced Deep Super-Resolution)을 개발해 NTIRE 2017 단일 영상 초해상화 챌린지에서 우승했고, 최근에는 3차원 손 자세와 여러 사람의 3차원 자세 추정 문제를 연구하고 있으며, 2017 3D Hand Pose Estimation Challenge와 First 3D Poses in the Wild Challenge 2020에서 우승했다고 소개한다.[^kmlee]

이경무 교수 페이지의 Selected Awards and Honors 칸은 The 63th Samil Prize(The Samil Foundation, 2022)를 첫 줄로 적고, Excellence in Research Award(서울대학교, 2020), Medal of Merit(Korean Government, 2020), Korean Scientist and Engineer of the Month Award(과학기술정보통신부, 2018), MSRA Grant Award(Microsoft Research Asia, 2016), IAPR MVA의 Most Influential Paper over the Decade Award(2009), ACCV 2007 Honorable Mention Award(입선) 등을 적는다.[^kmlee] 연구실 소식은 2022년 2월 교수가 삼일재단(Samil Foundation)의 제63회 Samil Prize 기술·공학 부문 수상자로 뽑혔다고 알렸다.[^news] 교수 페이지의 Professional Activities 칸은 IEEE Fellow(2021 – present), 한국과학기술한림원(KAST) 회원(2020 – Present), 한국공학한림원(NAEK) 회원(2020 – Present)을 적고, 학부 교수 상세는 IEEE Fellow와 한국과학기술한림원 정회원을 2021년부터, 한국공학한림원 회원을 2020년부터로 적는다.[^kmlee][^eceprof] 교수는 학술지 IEEE Transactions on Pattern Analysis and Machine Intelligence(TPAMI)의 편집장(Editor in Chief, 교수 페이지 표기 2021.01 – Present)이며, 앞서 같은 학술지의 부편집장(Associate Editor in Chief, 2014–2019)을 지냈다.[^kmlee][^eceprof] 학회 활동으로는 ICCV 2019, ACM MM 2018, ACCV 2018의 General Chair, ACCV 2012의 Program Chair를 맡았고, CVPR 2021·2022, ICCV 2021, ECCV 2020의 Area Chair와 ICCV 2021 Marr Prize 수상 위원회, CVPR 2021 Best Paper Award 위원회 위원을 지냈다. 컴퓨터 비전 재단(CVF)의 Advisory Board Member(2016–2020)와 한국컴퓨터비전학회(KCVS) 회장(2018–2021)도 지냈다.[^kmlee]

한보형 교수(Bohyung Han)는 서울대학교 전기·정보공학부 교수다.[^ecefac][^ecehan] 누리집 교수 페이지는 소속을 전기·정보공학부와 AI대학원(Graduate School of AI)으로 적고, 삼성전자 DS 부문 AX/PI Center의 Fellow로도 적는다.[^bhhan] 서울대학교에서 컴퓨터공학(Computer Engineering) 학사(1997)와 석사(2000)를, 미국 University of Maryland에서 컴퓨터과학(Computer Science) 박사(2005)를 받았다.[^ecehan][^bhhan] 교수 페이지의 Employment 칸에 따르면 Mobileye Vision Technologies의 Research Staff(2008–2009), UNIST 조교수(2010), POSTECH 조교수(2010–2014)와 부교수(2014–2018)를 지냈고, 2018년 3월 서울대학교 전기·정보공학부 부교수가 되어 2021년 3월부터 교수다. Google Research(2016–2017)와 Google DeepMind(2024–2025)의 Visiting Faculty Researcher, Snap Research의 Staff Research Scientist(2018)를 지냈고, 2026년 8월부터 삼성전자 Fellow(EVP)다.[^bhhan] 학부 교수 상세는 한보형 교수의 분야와 Research Interest를 Computer Vision, Machine Learning, Deep Learning으로 적는다.[^ecehan]

한보형 교수 페이지의 소식 칸은 2025년에 한국정보과학회(KIISE)의 Gaheon Academy Award를 받았고, 한국과학기술한림원(KAST) Fellow로 뽑혔으며, 2025년 10월 한국연구재단(NRF)의 Scientist of the Month Award를 받았다고 적는다.[^bhhan] 학회 활동으로는 ICCV 2025와 BMVC 2026의 Program Chair, ACCV 2022의 General Chair를 맡았고, CVPR(2023, 2024), NeurIPS(2022, 2024, 2025), ICLR(2022–2026), ICML(2025, 2026)의 Senior Area Chair를 지냈으며, 학술지 IEEE TPAMI의 Associate Editor(2018–present)다.[^bhhan] 교수 페이지가 연결한 Publication 페이지는 2023년부터 「2010 or Earlier」 구역까지의 논문을 싣는다. 2020년 이전 논문은 시각 추적이 많아, 다중 도메인 합성곱 신경망으로 하는 물체 추적(CVPR 2016, 페이지 표기 The winner of VOT2015 challenge)과 실시간 물체 추적 Real-Time MDNet(ECCV 2018)이 있고, 영상 분할을 위한 역합성곱 신경망(ICCV 2015), 영상 질의응답(CVPR 2016), 동영상과 글로 하는 시간 구간 찾기(CVPR 2020) 같은 논문도 있다.[^bhpubs]

이경무 교수 페이지의 Recent Publications (Selected) 칸에는 2019–2021년의 논문으로 사진 한 장에서 3차원 사람 자세와 메시를 추정하는 Pose2Mesh와 I2L-MeshNet, 손 자세 데이터셋 InterHand2.6M(이상 ECCV 2020), 메타학습(NeurIPS 2020, CVPR 2020), 동영상 프레임 보간(CVPR 2020, AAAI 2020), 시각 추적(ICCV 2019, ACCV 2020) 논문이 있다.[^kmlee] 누리집 논문 목록은 1993년의 학술지 논문([J1], 광도 스테레오 영상으로 표면을 되살리는 연구)부터 싣는다.[^pubs]

논문으로 보면 두 교수의 지금 전문 분야는 네 갈래다. 첫째, 확산 모델을 쓰는 초해상화와 초해상화 신경망의 양자화처럼 영상을 되살리고 그 신경망을 가볍게 만드는 연구다(대표 논문 1, 2, 이경무 교수).[^p1][^p2] 둘째, 사진에서 손과 사람, 사람이 다루는 물체의 3차원 모양을 되살리는 복원이다(대표 논문 3, 4, 이경무 교수).[^p3][^p4] 셋째, 전방위 영상과 일상 동영상으로 3차원·4차원 장면을 되살리는 연구다(대표 논문 5는 이경무 교수, 6은 한보형 교수).[^p5][^p6] 넷째, 확산 모델로 긴 동영상을 만들고 표본 추출을 빠르고 정확하게 하는 생성 연구다(대표 논문 7, 8, 한보형 교수).[^p7][^p8]

## 응용 분야

대표 논문이 직접 든 쓰임은 다음과 같다. 사람과 물체를 함께 3차원으로 복원하는 연구는 로봇과 디지털 콘텐츠 제작에 쓰임이 있다고 적고,[^p4] 전방위 영상의 3차원 복원은 한 장으로 장면 전체를 그려 내는 3차원 응용을 겨냥한다.[^p5] 움직이는 장면의 새 시점 합성은 증강현실과 가상현실을 비롯한 여러 응용에서 중요해지고 있다고 적는다.[^p6] 초해상화 신경망의 양자화는 계산량 때문에 널리 쓰이지 못하는 초해상화를 쓰기 쉽게 하려는 연구이고,[^p2] 끝없이 긴 동영상 생성은 기준 모델이 주어지면 동영상 길이와 상관없이 일정한 메모리만 쓰고 여러 GPU에서 나눠 추론하기에 알맞다.[^p7] 최근 논문 목록에는 CNC 가공 작업(CNC-Net, CVPR 2024)과 3D 프린팅 G-code 생성(PrintAnything, ECCV 2026), 망막·간 초음파·흉부 X선 영상 분석, 시각-언어-행동 모델의 세계 동역학 학습(Pri4R, CoRL 2026), 문자 인식 없이 하는 문서 이해(NeurIPS 2024) 같은 쓰임 쪽 논문도 있다.[^pubs] 수상 소식에는 운전 영상으로 사고 위험을 미리 내다보는 대회(CVPR 2026 AUTOPILOT Workshop의 Zero-Shot Accident Anticipation Challenge)의 1위도 있다.[^news]

## 구성원

2026년 10월 23일 누리집 Students 페이지 기준이다. PostDoc. 칸 3명, Ph.D. Courses 칸 33명, M.S. Courses 칸 4명이며, 과정은 칸 이름을 옮겼고 연구 주제는 카드의 Research Interests 줄이다. Students 페이지는 학생마다 지도교수를 적지 않아 표는 그 명단 전체를 옮긴 것이다.[^students] 한보형 교수 페이지의 Advising 칸은 그 교수가 지도하는 박사후연구원과 학생 이름을 따로 적는다.[^bhhan] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Sungho Park | 박사후연구원 | Deep Learning, Computer Vision |  |
| Mohsen Yavartanoo | 박사후연구원 | Computer Vision |  |
| Reyhaneh Neshatavar | 박사후연구원 | Computer Vision |  |
| Jihong Kang | 박사과정 | Image Restoration, Object Recognition |  |
| Bee Lim | 박사과정 | Image Restoration |  |
| Jaeyoung Chung | 박사과정 | 3D Object Recognition | 5 |
| Yeonguk Oh | 박사과정 | Deep Learning | 3 |
| Mijeong Kim | 박사과정 | Deep Learning | 6 |
| Hyunjin Son | 박사과정 | Deep Learning |  |
| Sanghyeok Chu | 박사과정 | Deep Learning |  |
| Sangmin Hong | 박사과정 | Computer Vision |  |
| Seoyeon Stella Yang | 박사과정 | 3D Vision, NeRF, Visual localization |  |
| Heewon Kim | 박사과정 | Computer Vision, Deep Learning |  |
| Minji Kim | 박사과정 | Deep learning, visual tracking, vision and language |  |
| Dongwan Kim | 박사과정 | Deep Learning |  |
| Wooseok Lee | 박사과정 | Deep Learning |  |
| Dohee Cho | 박사과정 | Deep Learning |  |
| Hyeongjin Nam | 박사과정 | Computer Vision, Deep Learning | 4 |
| Taeryung Lee | 박사과정 | Deep Learning |  |
| JoonKyu Park | 박사과정 | Deep Learning | 1, 3 |
| Jinkyu Kim | 박사과정 | Deep Learning |  |
| Jaerin Lee | 박사과정 | Deep Learning |  |
| Sungsu Hur | 박사과정 | Domain Adaptation |  |
| Sungho Jung (Daniel) | 박사과정 | 3D Human Mesh Recovery, 3D Scene Reconstruction | 4 |
| Donghwan Kim | 박사과정 | 3D Vision |  |
| Jeongtaek Oh | 박사과정 | 3D Scene Reconsturction, Neural Fields |  |
| Junoh Kang | 박사과정 | Deep Learning, Machine Learning | 7, 8 |
| Eunjae Hong | 박사과정 | Computer Vision |  |
| Jaeyoo Huh | 박사과정 | Computer Vision, Deep Learning | 5 |
| Donghun Ryou | 박사과정 | Computer Vision, Deep Learning |  |
| Namgi Kim | 박사과정 | Deep Learning, Computer Vision |  |
| Jungyoon Choi | 박사과정 | Computer Vision, Deep Learning |  |
| Suho Park | 박사과정 | Computer Vision, Deep Learning |  |
| JinYoung Choi | 박사과정 | Deep Learning, Computer Vision |  |
| Wonjae Roh | 박사과정 | Deep Learning, Computer Vision |  |
| Inju Ha | 박사과정 | Computer Vision, Deep Learning |  |
| Mingu Kang | 석사과정 | Deep Learning |  |
| Jihwan Kim | 석사과정 | Computer Vision, Diffusion Models | 7 |
| Kyujin Lim | 석사과정 | Computer Vision, Deep Learning |  |
| Junha Park | 석사과정 | Computer Vision, Deep Learning |  |

## 졸업생과 이전 구성원

누리집 Alumni 페이지의 103명이다. 이름 옆 괄호의 표기로 Ph.D. 46명(Ph.D 표기 2명 포함), M.S. 52명(MS 표기 4명 포함), Postdoc Researcher 4명, Ph.D. Candidate 1명이다. 학위·과정 칸은 그 괄호의 표기와 시기이고, 진로 칸은 카드에서 학력 줄 다음에 적힌 소속·직위 줄을 적힌 차례대로 옮겼다(세미콜론으로 구분). 카드는 이 줄에 따로 칸 이름을 붙이지 않는다. 페이지 끝 「Co-advised with Professor S. U. Lee」 칸 아래의 11명은 학위·과정 칸에 그 표기를 붙였다. 이 페이지도 지도교수를 사람마다 적지 않는다.[^alumni] 한보형 교수 페이지의 Alumni 칸은 그 교수가 지도한 졸업생과 현재 소속을 따로 적는다.[^bhhan]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jaeyoo Park | Ph.D. (Aug. 2026) |  |
| Geeho Kim | Ph.D. (Aug. 2026) |  |
| Suyoung Lee | Ph.D. (Aug. 2026) |  |
| Kanggeon Lee | Ph.D. (Aug. 2026) |  |
| Jaeha Kim | Ph.D. (Aug. 2026) | Samsung Electronics |
| Cheeun Hong | Ph.D. (Aug. 2026) |  |
| Junghun Oh | Ph.D. (Aug. 2026) |  |
| Insoo Kim | Postdoc Researcher | Incheon Univ., Assistant Professor |
| Daeul Park | M.S. (Aug. 2026) | Samsung Electronics |
| Hyungseo Ahn | M.S. (Aug. 2026) | Naver |
| Jinyoung Choi | Ph.D. (Aug. 2025) | ECE, Seoul National Univ., Postdoc Researcher |
| Dongwoo Lee | Ph.D. (Feb. 2025) | Samsung Research |
| Seonguk Seo | Ph.D. (Aug. 2024) |  |
| Hyewon Yoo | M.S. (Aug. 2024) |  |
| Seungmin Lee | M.S. (Aug. 2024) |  |
| Taehoon Kim | M.S. (Aug. 2024) |  |
| Tackgeun You | Ph.D. (Feb. 2024) | KIST |
| Minsoo Kang | Ph.D. (Feb. 2024) | SAIT |
| Euyoung Kim | Ph.D. (Aug. 2023) |  |
| Sanghyun Son | Ph.D. (Aug. 2023) | SAIT |
| Donghwan Jang | M.S. (Aug. 2023) |  |
| Jonathan Samuel Lumentut | Postdoc Researcher |  |
| Heewon Kim | Ph.D. (Feb. 2023) | Soongsil Univ., Assistant Professor |
| Seon Jong Hyeon | M.S. (Feb. 2023) | SK telecom |
| Jaehyoung Yoo | M.S. (Aug. 2022) | Samsung Electronics |
| Ilchae Jung | Ph.D. (Feb. 2022) | Naver CLOVA |
| Sungyong Baik | Ph.D. (Feb. 2022) | Hanyang Univ., Assistant Professor |
| Hongsuk Choi | M.S. (Feb. 2022) |  |
| Seungjun Nah | Ph.D. (Aug. 2021) | ECE, Seoul National Univ., Postdoc Researcher; NVIDIA, Research Scientist |
| Jaedong Hwang | M.S. (Aug. 2021) | EECS, MIT, Ph.D. Candidate |
| Gyeongsik Moon | Ph.D. (Feb. 2021) | ECE, Seoul National Univ., Postdoc Researcher |
| Janghoon Choi | Ph.D. (Feb. 2021) | ECE, Seoul National Univ., Postdoc Researcher; Kookmin Univ., Assistant Professor |
| Gwangmo Song | Ph.D. (Feb. 2021) | LG AI Research |
| Myungsub Choi | Ph.D. (Feb. 2021) | Google Korea; Samsung (SAIT) |
| Geonwoon Jang | M.S. (Feb. 2021) | Lunit |
| Junha Kim | M.S. (Feb. 2021) |  |
| Daniel Kim | M.S. (Aug. 2020) |  |
| Seohyun Kim | M.S. (Aug. 2020) |  |
| Jonghwan Mun | Ph.D. (Feb. 2020) | Kakao Brain |
| Paul Hongsuck Seo | Ph.D. (Feb. 2020) | Google France |
| Sunwoo Oh | M.S. (Feb. 2020) | NVIDIA |
| Seungyeon Shin | Ph.D. (Aug. 2019) | National Institutes of Health (NIH) |
| Yumin Suh | Ph.D. (Feb. 2019) | NEC Labs America |
| Hyeonwoo Noh | Ph.D. (Aug. 2019) | Samsung Electronics; Open AI |
| Mohammad Amin Shabani | M.S. (Aug. 2019) | Simon Fraser Univ., Ph.D. Candidate |
| Jeany Son | Postdoc Researcher | Electronics and Telecommunications Research Institute (ETRI) |
| Junhyung Kwak | M.S. (Feb. 2019) | NALBI Inc.; HDXWILL |
| Dongmin Park | M.S. (Feb. 2019) | Samsung Electronics |
| Wonseok Lee | MS (Feb. 2019) | Lunit |
| Woojae Chang | MS (Feb. 2019) | Samsung (SAIT) |
| Mooyeol Baek | MS (Sep. 2018) | Naver Labs |
| Heesoo Myeong | Ph.D. (Feb. 2017) | Qualcomm Korea |
| Haesol Park | Ph.D. (Feb. 2017) | KIST |
| Jungkwon Lee | M.S. (Feb. 2017) | Superb AI |
| Jungmin Lee | Ph.D. (Aug. 2016) | Samsung Research |
| Tae Hyun Kim | Ph.D. (Aug. 2016) | Macro Image Technology, Inc.; LG Electronics, Inc.; Max Planck Institute; Hanyang Univ., Assistant Professor |
| Kamil Adamczewski | M.S. (Aug. 2015) | Samsung Electronics; Max Planck Institute; ETH Zürich |
| Sergei Liubich | M.S. (Feb. 2015) | Samsung Electronics; NEO SPCC |
| Dong Woo Park | M.S. (Feb. 2006) | LG Electronics |
| Young Min Shin | Ph.D. (Feb. 2014) | Hyundai Heavy Industrial; Samsung SDS; Noul Inc. |
| Wonsik Kim | Ph.D. (Feb. 2014) | Samsung Advanced Institute of Technology |
| Byeongjoo Ahn | M.S. (Feb. 2014) | KIST; Carnegie Mellon Univ., Ph.D. Candidate |
| Hee Seok Lee | Ph.D. (Aug. 2013) | Qualcomm Korea; NVIDIA Korea |
| Junseok Kwon | Ph.D. (Feb. 2013) | Kiryung Elec. co., Ltd.; Chung-Ang Univ., Associate Professor |
| Junha Roh | M.S. (Feb. 2013) | KIST; Univ. of Washington, Ph.D. Candidate |
| Sangdon Park | M.S. (Aug. 2012) |  |
| Minsu Cho | Ph.D. (Mar. 2012) | Netdus Co., Ltd.; INRIA/ENS; POSTECH, Associate Professor |
| Hyojin Kim | M.S. (Feb. 2012) | Facebook Reality Labs. |
| Hyo-Chan Son | M.S. (Aug. 2011) | Doosan Heavy Industries & Construction; EECS, Seoul National Univ., M.S.; Samsung Engineering |
| Junghyun Kwon | Postdoc Researcher | TeleSecurity Sciences, Inc.; NVIDIA |
| Young Ki Baik | Ph.D. (Aug. 2010) | Qualcomm Korea |
| Stepan Tulyakov | M.S. (Aug. 2010) | Samsung Electronics |
| Ivan Koryakovskiy | M.S. (Aug. 2010) | Samsung Electronics |
| Moon Bin Lee | M.S. (Feb. 2010) |  |
| Jonghyun Choi | MS (Aug. 2008) | GIST, Assistant Professor |
| Joonyoung Park | M.S. (Feb. 2007) | LG Electronics |
| Woo Yeon Jeong | Ph.D (Aug. 2006) | Samsung Advanced Institute of Technology |
| Yoonkyung Kim | M.S. (Feb. 2006) | Samsung Advanced Institute of Technology |
| Hyun-Mook Cho | Ph.D. Candidate (Feb. 2005) | Doosan Heavy Industries & Construction; EECS, Seoul National Univ., M.S.; Qualcomm Korea |
| San Ko | M.S. (Aug. 2005) | Samsung Advanced Institute of Technology |
| Sung Won Park | M.S. (Aug. 2005) |  |
| Cheol Ki Hong | M.S. (Feb. 2003) | LG Electronics |
| Kwang Soo Lim | M.S. (Feb. 2003) | LG Electronics |
| Seung Hwan Choi | M.S. (Feb. 2003) | Samsung Electronics |
| Won Ho Seo | M.S. (Sep. 2002) | Pantech & Curitel |
| Sang Woo Seok | M.S. (Feb. 2002) | Pantech & Curitel |
| Hyoung Jin Kim | M.S. (Feb. 2002) | LIG Nex1 |
| Sung Min Jo | M.S. (Feb. 2001) | Samsung Electronics |
| Jae Sung Han | M.S. (Sep. 2000) | Samsung Electronics |
| Hyoung Lim Kim | M.S. (Feb. 2000) |  |
| Hanmin Ryu | M.S. (Feb. 1999) | Telson Electronics |
| Sang Hyup Lee | M.S. (Feb. 1998) | Mobile Works |
| Yong Seok Heo | Ph.D., Co-advised with Professor S. U. Lee (Aug. 2012) | Samsung Electronics; Ajou Uni., Associate Professor |
| Tae Hoon Kim | Ph.D., Co-advised with Professor S. U. Lee (Aug. 2012) | Samsung Electronics |
| Hoyub Jung | Ph.D., Co-advised with Professor S. U. Lee (Mar. 2012) | Samsung Electronics; Chosun Uni., Assistant Professor |
| Soochahn Lee | Ph.D., Co-advised with Professor S. U. Lee (Feb. 2011) | Kookmin Univ., Assistant Professor |
| Ju Yong Chang | Ph.D., BK21 Contract Professor, Co-advised with Professor S. U. Lee (Feb. 2008) | Mitsubishi Electric Research Lab.; Electronics and Telecommunications Research Institute (ETRI); Samsung Electronics; Kwangwoon Univ., Associate Professor |
| Dong hyuk Lee | Ph.D., Co-advised with Professor S. U. Lee (Feb. 2008) |  |
| Yoon Phil Eo | Ph.D, Co-advised with Professor S. U. Lee (Aug. 2007) | Samsung Electronics |
| Taeyoung Kim | M.S., Co-advised with Professor S. U. Lee (2005) |  |
| Bogeon Park | Ph.D., Co-advised with Professor S. U. Lee (2004) |  |
| HyunJun Oh | M.S., Co-advised with Professor S. U. Lee (2004) |  |
| Jaechul Kim | M.S., Co-advised with Professor S. U. Lee (Feb. 2002) | Amazon |

## 최근 논문 목록 (2021–2026)

누리집 International Publications 페이지의 2021–2026년 연도 구역 143항목 가운데 이경무 교수나 한보형 교수가 저자로 오른 142편이다(2026년 28편, 2025년 17편, 2024년 23편, 2023년 22편, 2022년 24편, 2021년 28편). 이경무 교수가 저자인 논문이 78편, 한보형 교수가 저자인 논문이 65편이고, 그 가운데 한 편은 두 교수가 함께 저자다. 저자 순서와 제목·학술지·학회 표기는 누리집 그대로이고, 누리집이 붙인 발표 형식 표기(ORAL presentation)도 옮겼다. 이름 뒤의 \*는 누리집 표시이며 누리집은 그 뜻을 적지 않는다. 연도는 누리집의 연도 구역 기준이다. 2021년 구역의 IEEE TPAMI 논문 세 편은 누리집이 연도 없이 게재 승인(accepted)으로 적은 줄이고, 같은 구역의 「Clean Images are Hard to Reblur: A New Clue for Deblurring」은 누리집이 arXiv 사전 공개본으로 적은 줄이다. 두 경우 모두 누리집이 둔 2021년 구역에 그대로 두었다. 2026년 구역의 학회 논문 가운데 학회 논문집 기록을 찾지 못한 다섯 편은 학회 표기 뒤 괄호에 확인한 판본(OpenReview의 채택 기록 4편, arXiv 사전 공개본 1편)을 적었고, 기록과 판본을 모두 찾지 못한 두 편은 괄호에 「누리집 표기」로 표시했다.[^pubs][^checked]

**2026**

- Geeho Kim, Minsik Choi, Kyle Min, Young Geun Kim, and Bohyung Han. "Merging RLVR-Trained Experts via Policy-Shift-Guided Spectral Alignment". *Advances in Neural Information Processing Systems (NeurIPS), 2026 (누리집 표기)*.
- Junoh Kang, Kiseop Lee, and Bohyung Han. "Probabilistic Signature Inversion: Learning Conditional Distributions from Truncated Signatures". *Advances in Neural Information Processing Systems (NeurIPS), 2026 (확인한 판본 arXiv 2606.15332 사전 공개본)*.
- Jaeyoo Park and Bohyung Han. "Structural Self-Teaching for Compositional Generation in Unified Multimodal Models". *Advances in Neural Information Processing Systems (NeurIPS), 2026 (누리집 표기)*.
- Jisoo Kim\*, Jungbin Cho\*, Sanghyeok Chu, Ananya Bal, Jinhyung Kim, Gunhee Lee, Sihaeng Lee, Seung Hwan Kim, Bohyung Han, Hyunmin Lee, Laszlo A. Jeni, and Seungryong Kim. "Pri4R: Learning World Dynamics for Vision-Language-Action Models with Privileged 4D Representation". *Proc. Conference on Robot Learning (CoRL), 2026 (확인한 판본 OpenReview 기록 CoRL 2026 Poster)*.
- Jiwon Kim and Kyoung Mu Lee. "WARP: Wide Attention with Rich Projections for Image Super-Resolution". *Proc. European Conference on Computer Vision (ECCV), 2026*.
- Jaerin Lee, Kanggeon Lee, and Kyoung Mu Lee. "Vector Scaffolding: Inter-Scale Orchestration for Differentiable Image Vectorization". *Proc. European Conference on Computer Vision (ECCV), 2026*.
- Sangmin Hong, Daniel Sungho Jung, Heewon Kim, and Kyoung Mu Lee. "PrintAnything: Learning Geometric Plan Map for 3D Printing G-code Generation from Unoriented Point Clouds". *Proc. European Conference on Computer Vision (ECCV), 2026*.
- Taeryung Lee, Hyeongjin Nam, Gyeongsik Moon, and Kyoung Mu Lee. "SIGNER: Temporally Grounded Sign Language Generation via Time-Resolved Conditioning". *Proc. European Conference on Computer Vision (ECCV), 2026*.
- Jaeyoung Chung\*, Suyoung Lee\*, Jianfeng Xiang, Jialong Yang, and Kyoung Mu Lee. "Map2World: Segment Map Conditioned Text to 3D World Generation". *Proc. European Conference on Computer Vision (ECCV), 2026*.
- Joonkyu Park, Wooseok Lee, Jaeha Kim, Sehoon Kim, Bokyeung Lee, and Kyoung Mu Lee. "Learning to Corrupt for Better Restoration". *Proc. European Conference on Computer Vision (ECCV), 2026*.
- Jinkyu Kim\*, Jinyoung Choi\*, and Bohyung Han. "Optimizing Diffusion Samplers via Dynamic Preference". *Proc. European Conference on Computer Vision (ECCV), 2026*.
- Sangmin Hong\*, Suyoung Lee\*, and Kyoung Mu Lee. "StarryGazer: Leveraging Monocular Depth Estimation Models for Domain-Agnostic Single Depth Image Completion". *Signal, Image and Video Processing (SIVP), 2026*.
- Yeonsang Shin, Insoo Kim, Bongkeun Kim, Keonwoo Bae, and Bohyung Han. "Infinite-Precision Autoregressive Modeling for Vector Graphics and Layouts". *Proc. International Conference on Machine Learning (ICML), 2026 (확인한 판본 OpenReview 기록 ICML 2026 regular)*.
- Jie Hu, Lingyun Chen, Geeho Kim, Jinyoung Choi, Bohyung Han, and Do Young Eun. "Score-Repellent Monte Carlo: Toward Efficient Non-Markovian Sampler with Constant Memory in General State Spaces". *Proc. International Conference on Machine Learning (ICML), 2026 (확인한 판본 OpenReview 기록 ICML 2026 spotlight)*.
- Joy Dhar, Manish Kumar Pandey, Behzad Bozorgtabar, Nayyar Zaidi, Wenyu Zhang, Wei-Hong Li, Tingting Mu, Dwarikanath Mahapatra, Mahsa Baktashmotlagh, Trung Le, Chen Chen, Sajib Mistry, Camila Gonzalez, Samira Ebrahimi Kahou, Lina Yao, Piotr Koniusz, Robert Burns Fisher, Dinh Phung, Bohyung Han, Nuno Vasconcelos, and Pietro Lio. "Does a Hybrid Space-Aware Randomized Defense Improve Empirical and Certified Adversarial Robustness?". *Proc. International Conference on Machine Learning (ICML), 2026 (확인한 판본 OpenReview 기록 ICML 2026 regular)*.
- Hyeongjin Nam, Daniel Sungho Jung, and Kyoung Mu Lee. "TeHOR: Text-Guided 3D Human and Object Reconstruction with Textures". *Proc. Computer Vision and Pattern Recognition (CVPR), 2026*.
- Daniel Sungho Jung and Kyoung Mu Lee. "Shoe Style-Invariant and Ground-Aware Learning for Dense Foot Contact Estimation". *Proc. Computer Vision and Pattern Recognition (CVPR), 2026*.
- Mijeong Kim, Jungtaek Kim, and Bohyung Han. "GP-4DGS: Probabilistic 4D Gaussian Splatting from Monocular Video via Variational Gaussian Processes". *Proc. Computer Vision and Pattern Recognition (CVPR), 2026*.
- Mijeong Kim\*, Gunhee Kim\*, Jungyoon Choi, Wonjae Roh, and Bohyung Han. "PhysGaia: A Physics-aware Benchmark with Multi-Body Interactions for Dynamic Novel View Synthesis". *Proc. Computer Vision and Pattern Recognition (CVPR), 2026*.
- Sanghyeok Chu, Pyunghwan Ahn, Gwangmo Song, Seung Hwan Kim, Honglak Lee, and Bohyung Han. "Enhancing Mixture-of-Experts Specialization via Cluster-Aware Upcycling". *Proc. Computer Vision and Pattern Recognition (CVPR), 2026*.
- Donghun Ryou\*, Inju Ha\*, Sanghyeok Chu, and Bohyung Han. "Beyond the Ground Truth: Enhanced Supervision for Image Restoration". *Proc. Computer Vision and Pattern Recognition (CVPR), 2026*.
- Junsung Lee\*, Hyunsoo Lee\*, Yong Jae Lee, and Bohyung Han. "Low-Resolution Editing is All You Need for High-Resolution Editing". *Proc. Computer Vision and Pattern Recognition (CVPR), 2026*.
- Fu-Yun Wang, Hao Zhou, Liangzhe Yuan, Sanghyun Woo, Boqing Gong, Bohyung Han, Ming-Hsuan Yang, Han Zhang, Yukun Zhu, Ting Liu, and Long Zhao. "Image Diffusion Preview with Consistency Solver". *Proc. Computer Vision and Pattern Recognition (CVPR), 2026*.
- Bingyi Cao, Koert Chen, Kevis-kokitsi Maninis, Kaifeng Chen, Arjun Karpur, Ye Xia, Sahil Dua, Tanmaya Shekhar Dabral, Guangxing Han, Bohyung Han, Joshua Ainslie, Alex Bewley, Mithun George Jacob, René Wagner, Washington Ramos, Krzysztof Marcin Choromanski, Mojtaba Seyedhosseini, Howard Zhou, and Andre Araujo. "TIPSv2: Advancing Vision-Language Pretraining with Enhanced Patch-Text Alignment". *Proc. Computer Vision and Pattern Recognition (CVPR), 2026*.
- Inju Ha\*, Donghun Ryou\*, Seonguk Seo, and Bohyung Han. "Learning to Translate Noise for Robust Image Denoising". *Proc. Computer Vision and Pattern Recognition (CVPR), Findings Track, 2026*.
- Mijeong Kim, Namgi Kim, and Bohyung Han. "HyperPose: Hyper-pose Embeddings for 3D-Aware Generative Models with Self-Supervised Disentangling of Pose and Scene". *Winter Conference on Applications of Computer Vision (WACV), 2026*.
- Joonkyu Park and Kyoung Mu Lee. "Bridging the Distribution Gap to Harness Pretrained Diffusion Priors for Super-Resolution". *International Conference on Learning Representations (ICLR), 2026*.
- Minji Kim\*, Taekyung Kim\*, and Bohyung Han. "Map the Flow: Revealing Hidden Pathways of Information in VideoLLMs". *International Conference on Learning Representations (ICLR), 2026*.

**2025**

- Jaeyoung Chung\*, Suyoung Lee\*, Hyeongjin Nam, Jaerin Lee, and Kyoung Mu Lee. "LucidDreamer: Domain-free Generation of 3D Gaussian Splatting Scenes". *IEEE Transactions on Visualization and Computer Graphics (TVCG), 2025*.
- Daniel Sungho Jung and Kyoung Mu Lee. "Learning Dense Hand Contact Estimation from Imbalanced Data". *Advances in Neural Information Processing Systems (NeurIPS), 2025*.
- Geeho Kim, Jinu Lee, and Bohyung Han. "FedLPA: Local Prior Alignment for Heterogeneous Federated Generalized Category Discovery". *Advances in Neural Information Processing Systems (NeurIPS), 2025*.
- Kanggeon Lee, Soochahn Lee, and Kyoung Mu Lee. "Auto-regressive transformation for image alignment". *Proc. International Conference on Computer Vision (ICCV), 2025*.
- Hyeongjin Nam\*, Donghwan Kim\*, Gyeongsik Moon, and Kyoung Mu Lee. "PARTE: Part-Guided Texturing for 3D Human Reconstruction from a Single Image". *Proc. International Conference on Computer Vision (ICCV), 2025*.
- Jaeha Kim, Junghun Oh, and Kyoung Mu Lee. "Exploiting Diffusion Prior for Task-driven Image Restoration". *Proc. International Conference on Computer Vision (ICCV), 2025*.
- Jaeyoung Chung, Kanggeon Lee, Sungyong Baik, and Kyoung Mu Lee. "MEIL-NeRF: Memory-Efficient Incremental Learning of Neural Radiance Fields". *IEEE Access , 2025*.
- Sanghyeok Chu, Seonguk Seo, and Bohyung Han. "Fine-Grained Video Captioning through Scene Graph Consolidation". *Proc. International Conference on Machine Learning (ICML), 2025*.
- Suyoung Lee\*, Jaeyoung Chung\*, Kihoon Kim, Jaeyoo Huh, Gunhee Lee, Minsoo Lee, and Kyoung Mu Lee. "OmniSplat: Taming Feed-Forward 3D Gaussian Splatting for Omnidirectional Images with Editable Capabilities". *Proc. Computer Vision and Pattern Recognition (CVPR), 2025*.
- Hyeongjin Nam, Donghwan Kim, Jeongtaek Oh, and Kyoung Mu Lee. "DeClotH: Decomposable 3D Cloth and Human Body Reconstruction from a Single Image". *Proc. Computer Vision and Pattern Recognition (CVPR), 2025*.
- Jaerin Lee, Daniel Sungho Jung, Kanggeon Lee, Kyoung Mu Lee. "SemanticDraw: Towards Real-Time Interactive Content Creation from Image Diffusion Models". *Proc. Computer Vision and Pattern Recognition (CVPR), 2025*.
- Jinyoung Choi, Junoh Kang, and Bohyung Han. "Enhanced Diffusion Sampling via Extrapolation with Multiple ODE Solutions". *International Conference on Learning Representations (ICLR), 2025*.
- Junghun Oh, Sungyong Baik, and Kyoung Mu Lee. "Find A Winning Sign: Sign Is All We Need to Win the Lottery". *International Conference on Learning Representations (ICLR), 2025*.
- Seonguk Seo, Dongwan Kim, Bohyung Han. "Revisiting Machine Unlearning with Dimensional Alignment". *Winter Conference on Applications of Computer Vision (WACV), 2025*.
- Seonguk Seo, Gokhan Uzunbas, Bohyung Han, Sara Cao, Ser-Nam Lim. "Metric Compatible Training for Online Backfilling in Large-Scale Retrieval". *Winter Conference on Applications of Computer Vision (WACV), 2025*.
- Seonguk Seo and Bohyung Han. "Re-evaluating Group Robustness via Adaptive Class-Specific Scaling". *Winter Conference on Applications of Computer Vision (WACV), 2025*.
- Cheeun Hong\*, Sungyong Baik\*, Junghun Oh, and Kyoung Mu Lee. "Difficulty, Diversity, and Plausibility: Dynamic Data-Free Quantization". *Winter Conference on Applications of Computer Vision (WACV), 2025*.

**2024**

- Dongwoo Lee, Joonkyu Park, and Kyoung Mu Lee. "GS-Blur: A 3D Scene-Based Dataset for Realistic Image Deblurring". *Advances in Neural Information Processing Systems (NeurIPS), 2024*.
- Suyoung Lee\*, Jaeyoung Chung\*, Jaeyoo Huh, and Kyoung Mu Lee. "ODGS: 3D Scene Reconstruction from Omnidirectional Images with 3D Gaussian Splattings". *Advances in Neural Information Processing Systems (NeurIPS), 2024*.
- Jihwan Kim\*, Junoh Kang\*, Jinyoung Choi, and Bohyung Han. "FIFO-Diffusion: Generating Infinite Videos from Text without Training". *Advances in Neural Information Processing Systems (NeurIPS), 2024*.
- Jaeyoo Park, Jinyoung Choi, Jeonghyung Park, and Bohyung Han. "Hierarchical Visual Feature Aggregation for OCR-Free Document Understanding". *Advances in Neural Information Processing Systems (NeurIPS), 2024*.
- Mijeong Kim, Jongwoo Lim, and Bohyung Han. "4D Gaussian Splatting in the Wild with Uncertainty-Aware Regularization". *Advances in Neural Information Processing Systems (NeurIPS), 2024*.
- Joonkyu Park, Gyeongsik Moon, Weipeng Xu, Evan Kaseman, Takaaki Shiratori, and Kyoung Mu Lee. "3D Hand Sequence Recovery from Real Blurry Images and Event Stream". *Proc. European Conference on Computer Vision (ECCV), 2024*.
- Junghun Oh\*, Sungyong Baik\*, and Kyoung Mu Lee. "CLOSER: Towards Better Representation Learning for Few-Shot Class-Incremental Learning". *Proc. European Conference on Computer Vision (ECCV), 2024*.
- Cheeun Hong and Kyoung Mu Lee. "Overcoming Distribution Mismatch in Quantizing Image Super-Resolution Networks". *Proc. European Conference on Computer Vision (ECCV), 2024*.
- Junsung Lee, Minsoo Kang, and Bohyung Han. "Diffusion-Based Image-to-Image Translation by Noise Correction via Prompt Interpolation". *Proc. European Conference on Computer Vision (ECCV), 2024*.
- Minji Kim, Dongyoon Han, Taekyung Kim, Bohyung Han. "Leveraging temporal contextualization for video action recognition". *Proc. European Conference on Computer Vision (ECCV), 2024*.
- Jaeyoung Chung, Jeongtaek Oh, and Kyoung Mu Lee. "Depth-Regularized Optimization for 3D Gaussian Splatting in Few-Shot Images". *Proc. Computer Vision and Pattern Recognition Workshops (CVPRW), 2024*.
- Taeryung Lee, Fabien Baradel, Thomas Lucas, Kyoung Mu Lee and Gregory Rogez. "T2LM: Long-Term 3D Human Motion Generation from Multiple Sentences". *Proc. Computer Vision and Pattern Recognition Workshops (CVPRW), 2024*.
- Jaeha Kim, Junghun Oh, and Kyoung Mu Lee. "Beyond Image Super-Resolution for Image Recognition with Task-Driven Perceptual Loss". *Proc. Computer Vision and Pattern Recognition (CVPR), 2024*.
- Mohsen Yavartanoo\*, Sangmin Hong\*, Reyhaneh Neshatavar\*, and Kyoung Mu Lee. "CNC-Net: Self-Supervised Learning for CNC Machining Operations". *Proc. Computer Vision and Pattern Recognition (CVPR), 2024*.
- Cheeun Hong and Kyoung Mu Lee. "AdaBM: On-the-Fly Adaptive Bit Mapping for Image Super-Resolution". *Proc. Computer Vision and Pattern Recognition (CVPR), 2024*.
- Hyeongjin Nam\*, Daniel Sungho Jung\*, Gyeongsik Moon, and Kyoung Mu Lee. "Joint Reconstruction of 3D Human and Object via Contact-Based Refinement Transformer". *Proc. Computer Vision and Pattern Recognition (CVPR), 2024*.
- Donghun Ryou, Inju Ha, Hyewon Yoo, Dongwan Kim, and Bohyung Han. "Robust Image Denoising through Adversarial Frequency Mixup". *Proc. Computer Vision and Pattern Recognition (CVPR), 2024*.
- Geeho Kim\*, Jinkyu Kim\*, and Bohyung Han. "Communication-Efficient Federated Learning with Accelerated Client Gradient". *Proc. Computer Vision and Pattern Recognition (CVPR), 2024*.
- Junoh Kang\*, Jinyoung Choi\*, Sungik Choi, and Bohyung Han. "Observation-Guided Diffusion Probabilistic Models". *Proc. Computer Vision and Pattern Recognition (CVPR), 2024*.
- Seonguk Seo\*, Jinkyu Kim\*, Geeho Kim\*, and Bohyung Han. "Relaxed Contrastive Learning for Federated Learning". *Proc. Computer Vision and Pattern Recognition (CVPR), 2024*.
- Taehoon Kim, Jaeyoo Park, and Bohyung Han. "Cross-Class Feature Augmentation for Class Incremental Learning". *Association for the Advancement of Artificial Intelligence (AAAI), 2024*.
- Taehoon Kim and Bohyung Han. "Randomized Adversarial Style Perturbations for Domain Generalization". *Winter Conference on Applications of Computer Vision (WACV), 2024*.
- Reyhaneh Neshatavar\*, Mohsen Yavartanoo\*, Sanghyun Son, and Kyoung Mu Lee. "ICF-SRSR: Invertible scale-Conditional Function for Self-Supervised Real-world Single Image Super-Resolution". *Winter Conference on Applications of Computer Vision (WACV), 2024*.

**2023**

- Jonathan Samuel Lumentut and Kyoung Mu Lee. "3DHR-Co: A Collaborative Test-Time Refinement Framework for In-the-Wild 3D Human-Body Reconstruction Task". *IEEE Access , 2023*.
- Joonkyu Park, Cheeun Hong, Sungyong Baik, and Kyoung Mu Lee. "CoLaNet: Adaptive Context and Latent Information Blending for Face Image Inpainting". *IEEE Signal Processing Letters (SPL), Dec. 2023*.
- Hyunsoo Lee\*, Minsoo Kang\*, and Bohyung Han. "Conditional Score Guidance for Text-Driven Image-to-Image Translation". *Advances in Neural Information Processing Systems (NeurIPS), 2023*.
- Tackgeun You, Jungtaek Kim, Mijeong Kim, and Bohyung Han. "Generative Neural Fields by Mixtures of Neural Implicit Functions". *Advances in Neural Information Processing Systems (NeurIPS), 2023*.
- Zunzhi You, Daochang Liu, Bohyung Han, and Chang Xu. "Beyond Pretrained Features: Noisy Image Modeling Provides Adversarial Defense". *Advances in Neural Information Processing Systems (NeurIPS), 2023*.
- Euyoung Kim, Soochahn Lee, and Kyoung Mu Lee. "Abnormality Detection in Chest X-Ray via Residual-Saliency From Normal Generation". *IEEE Access , 2023*.
- Joonkyu Park\*, Daniel Sungho Jung\*, Gyeongsik Moon\*, and Kyoung Mu Lee. "Extract-and-Adaptation Network for 3D Interacting Hand Mesh Recovery". *Proc. International Conference on Computer Vision Workshops (ICCVW), 2023. (ORAL presentation)*.
- Dongwoo Lee, Jeongtaek Oh, Jaesung Rim, Sunghyun Cho, and Kyoung Mu Lee. "ExBluRF: Efficient Radiance Fields for Extreme Motion Blurred Images". *Proc. International Conference on Computer Vision (ICCV), 2023*.
- Hyeongjin Nam, Daniel Sungho Jung, Yeonguk Oh, and Kyoung Mu Lee. "Cyclic Test-Time Adaptation on Monocular Video for 3D Human Mesh Reconstruction". *Proc. International Conference on Computer Vision (ICCV), 2023*.
- Taeryung Lee, Yeonguk Oh, and Kyoung Mu Lee. "Human Part-wise 3D Motion Context Learning for Sign Language Recognition". *Proc. International Conference on Computer Vision (ICCV), 2023*.
- Joonkyu Park, Sanghyun Son, and Kyoung Mu Lee. "Content-Aware Local GAN for Photo-Realistic Super-Resolution". *Proc. International Conference on Computer Vision (ICCV), 2023*.
- Dongwoo Lee and Kyoung Mu Lee. "Dense Depth-Guided Generalizable NeRF". *IEEE Signal Processing Letters (SPL), Jan. 2023*.
- Sangmin Hong\*, Mohsen Yavartanoo\*, Reyhaneh Neshatavar, and Kyoung Mu Lee. "ACL-SPC: Adaptive Closed-Loop system for Self-Supervised Point Cloud Completion". *Proc. Computer Vision and Pattern Recognition (CVPR), 2023*.
- Yeonguk Oh\*, Joonkyu Park\*, Jaeha Kim\*, Gyeongsik Moon, and Kyoung Mu Lee. "Recovering 3D Hand Mesh Sequence from a Single Blurry Image: A New Dataset and Temporal Unfolding". *Proc. Computer Vision and Pattern Recognition (CVPR), 2023*.
- Dongwan Kim and Bohyung Han. "On the Stability-Plasticity Dilemma of Class-Incremental Learning". *Proc. Computer Vision and Pattern Recognition (CVPR), 2023*.
- Jaeyoo Park and Bohyung Han. "Multi-Modal Representation Learning with Text-Driven Soft Masks". *Proc. Computer Vision and Pattern Recognition (CVPR), 2023*.
- Geeho Kim, Junoh Kang, and Bohyung Han. "Open-Set Representation Learning through Combinatorial Embedding". *Proc. Computer Vision and Pattern Recognition (CVPR), 2023*.
- Minsoo Kang, Doyup Lee, Jiseob Kim, Saehoon Kim, and Bohyung Han. "Variational Distribution Learning for Unsupervised Text-to-Image Generation". *Proc. Computer Vision and Pattern Recognition (CVPR), 2023*.
- Heewon Kim and Kyoung Mu Lee. "NERDS: A General Framework to Train Camera Denoisers from Raw-RGB Noisy Image Pairs". *International Conference on Learning Representations (ICLR), 2023*.
- Hongsuk Choi\*, Hyeongjin Nam\*, Taeryung Lee, Gyeongsik Moon, Kyoung Mu Lee. "Empirical Study of Pre-training a Backbone for 3D Human Pose and Shape Estimation". *International Conference on Learning Representations (ICLR), 2023*.
- Taeryung Lee\*, Gyeongsik Moon\*, and Kyoung Mu Lee. "Long-Term 3D Human Motion Generation from Multiple Action Labels". *AAAI Conference on Artificial Intelligence, 2023. (ORAL presentation)*.
- Jonghyeon Seon, Jaedong Hwang, Jonghwan Mun and Bohyung Han. "Stop or Forward: Dynamic Layer Skipping for Efficient Action Recognition". *Winter Conference on Applications of Computer Vision (WACV), 2023*.

**2022**

- Heewon Kim, Seokil Hong, Bohyung Han, Heesoo Myeong, and Kyoung Mu Lee. "Fine-Grained Neural Architecture Search for Image Super-Resolution". *Journal of Visual Communication and Image Representation (JVCI), 2022*.
- Jinyoung Choi and Bohyung Han. "MCL-GAN: Generative Adversarial Networks with Multiple Specialized Discriminators". *Advances in Neural Information Processing Systems (NeurIPS), 2022*.
- Minsoo Kang, Hyewon Yoo, Eunhee Kang, Sehwan Ki, Hyong-Euk Lee, and Bohyung Han. "Information-Theoretic Generative Model Compression with Variational Energy-based Model". *Advances in Neural Information Processing Systems (NeurIPS), 2022*.
- Tackgeun You, Saehoon Kim, Chiheon Kim, Doyup Lee, and Bohyung Han. "Locally Hierarchical Auto-Regressive Modeling for Image Generation". *Advances in Neural Information Processing Systems (NeurIPS), 2022*.
- Cheeun Hong, Sungyong Baik, Heewon Kim, Seungjun Nah, and Kyoung Mu Lee. "CADyQ: Content-Aware Dynamic Quantization for Image Super Resolution". *Proc. European Conference on Computer Vision (ECCV), 2022*.
- Gyeongsik Moon\*, Hyeongjin Nam\*, Takaaki Shiratori, and Kyoung Mu Lee. "3D Clothed Human Reconstruction in the Wild". *Proc. European Conference on Computer Vision (ECCV), 2022*.
- Minji Kim\*, Seungkwan Lee\*, Jungseul Ok, Bohyung Han, and Minsu Cho. "Towards Sequence-Level Training for Visual Tracking". *Proc. European Conference on Computer Vision (ECCV), 2022*.
- Dongwan Kim, Yi-Hsuan Tsai, Yumin Suh, Masoud Faraki, Sparsh Garg, Manmohan Chandraker, and Bohyung Han. "Learning Semantic Segmentation from Multiple Datasets with Label Shifts". *Proc. European Conference on Computer Vision (ECCV), 2022*.
- Jinkyu Kim\*, Geeho Kim\*, and Bohyung Han. "Multi-Level Branched Regularization for Federated Learning". *Proc. International Conference on Machine Learning (ICML), 2022*.
- Ilchae Jung, Minji Kim, Eunhyeok Park, and Bohyung Han. "Online Hybrid Lightweight Representations Learning: Its Application to Visual Tracking". *Proc. International Joint Conference on Artificial Intelligence (IJCAI), 2022*.
- Junghun Oh, Heewon Kim, Seungjun Nah, Cheeun Hong, Jonghyun Choi, and Kyoung Mu Lee. "Attentive Fine-Grained Structured Sparsity for Image Restoration". *Proc. Computer Vision and Pattern Recognition (CVPR), 2022*.
- Hongsuk Choi, Gyeongsik Moon, JoonKyu Park, and Kyoung Mu Lee. "Learning to Estimate Robust 3D Human Mesh from In-the-Wild Crowded Scenes". *Proc. Computer Vision and Pattern Recognition (CVPR), 2022*.
- Wooseok Lee, Sanghyun Son, and Kyoung Mu Lee. "AP-BSN: Self-Supervised Denoising for Real-World Images via Asymmetric PD and Blind-Spot Network". *Proc. Computer Vision and Pattern Recognition (CVPR), 2022*.
- Joonkyu Park\*, Yeonguk Oh\*, Gyeongsik Moon\*, Hongsuk Choi, and Kyoung Mu Lee. "HandOccNet: Occlusion-Robust 3D Hand Mesh Estimation Network". *Proc. Computer Vision and Pattern Recognition (CVPR), 2022*.
- Reyhaneh Neshatavar\*, Mohsen Yavartanoo\*, Sanghyun Son, and Kyoung Mu Lee. "CVF-SID: Cyclic multi-Variate Function for Self-Supervised Image Denoising by Disentangling Noise from Image". *Proc. Computer Vision and Pattern Recognition (CVPR), 2022*.
- Dong-Hwan Jang, Sanghyeok Chu, Joonhyuk Kim, and Bohyung Han. "Pooling Revisited: Your Receptive Field is Sub-optimal". *Proc. Computer Vision and Pattern Recognition (CVPR), 2022*.
- Minsoo Kang, Jaeyoo Park, and Bohyung Han. "Class-Incremental Learning by Knowledge Distillation with Adaptive Feature Consolidation". *Proc. Computer Vision and Pattern Recognition (CVPR), 2022*.
- Seonguk Seo, Joon-Young Lee, and Bohyung Han. "Unsupervised Learning of Debiased Representations with Pseudo-Attributes". *Proc. Computer Vision and Pattern Recognition (CVPR), 2022*.
- Mijeong Kim, Seonguk Seo, and Bohyung Han. "InfoNeRF: Ray Entropy Minimization for Few-Shot Neural Volume Rendering". *Proc. Computer Vision and Pattern Recognition (CVPR), 2022*.
- Minsu Ko\*, Eunju Cha\*, Sungjoo Suh, Huijin Lee, Jae-Joon Han, Jinwoo Shin, and Bohyung Han. "Self-Supervised Dense Consistency Regularization for Image-to-Image Translation". *Proc. Computer Vision and Pattern Recognition (CVPR), 2022*.
- Seungjun Nah, Sanghyun Son, Jaerin Lee, and Kyoung Mu Lee. "Clean Images are Hard to Reblur: Exploiting the Ill-Posed Inverse Task for Dynamic Scene Deblurring". *International Conference on Learning Representations (ICLR), 2022*.
- Seonguk Seo, Joon-Young Lee, and Bohyung Han. "Information-Theoretic Bias Reduction via Causal View of Spurious Correlation". *AAAI Conference on Artificial Intelligence, 2022*.
- Cheeun Hong\*, Heewon Kim\*, Sungyong Baik, Junghun Oh, and Kyoung Mu Lee. "DAQ: Channel-Wise Distribution-Aware Quantization for Deep Image Super-Resolution Networks". *Winter Conference on Applications of Computer Vision (WACV), 2022*.
- Junghun Oh, Heewon Kim, Sungyong Baik, Cheeun Hong, and Kyoung Mu Lee. "Batch Normalization Tells You Which Filter is Important". *Winter Conference on Applications of Computer Vision (WACV), 2022*.

**2021**

- Myungsub Choi, Janghoon Choi, Sungyong Baik, Tae Hyun Kim, and Kyoung Mu Lee. "Test-Time Adaptation for Video Frame Interpolation via Meta-Learning". *IEEE Trans. Pattern Analysis and Machine Intelligence (TPAMI), accepted*.
- Mohsen Yavartanoo, Shih-Hsuan Hung, Reyhaneh Neshatavar, Yue Zhang, and Kyoung Mu Lee. "PolyNet: Polynomial Neural Network for 3D Shape Recognition with PolyShape Representation". *International Conference on 3D Vision (3DV), 2021*.
- Joonkyu Park, Seungjun Nah, and Kyoung Mu Lee. "Recurrence-in-Recurrence Networks for Video Deblurring". *Proc. British Machine Vision Conference (BMVC), 2021*.
- Dae Young Park, Moon-Hyun Cha, Changwook Jeong, Daesin Kim, and Bohyung Han. "Learning Student-Friendly Teacher Networks for Knowledge Distillation". *Advances in Neural Information Processing Systems (NeurIPS), 2021*.
- Sanghyeok Chu, Dongwan Kim, and Bohyung Han. "Learning Debiased and Disentangled Representations for Semantic Segmentation". *Advances in Neural Information Processing Systems (NeurIPS), 2021*.
- Sanghyun Son\*, Jaeha Kim\*, Wei-Sheng Lai, Ming-Hsuan Yang, and Kyoung Mu Lee. "Toward Real-World Super-Resolution via Adaptive Downsampling Models". *IEEE Trans. Pattern Analysis and Machine Intelligence (TPAMI), accepted*.
- Myungseo Song, Jinyoung Choi, and Bohyung Han. "Variable-Rate Deep Image Compression through Spatially-Adaptive Feature Transform". *Proc. International Conference on Computer Vision (ICCV), 2021*.
- Sungyong Baik, Janghoon Choi, Heewon Kim, Dohee Cho, Jaesik Min, and Kyoung Mu Lee. "Meta-Learning with Task-Adaptive Loss Function for Few-Shot Learning". *Proc. International Conference on Computer Vision (ICCV), 2021. (ORAL presentation)*.
- Myungsub Choi, Suyoung Lee, Heewon Kim, and Kyoung Mu Lee. "Motion-Aware Dynamic Architecture for Efficient Frame Interpolation". *Proc. International Conference on Computer Vision (ICCV), 2021*.
- Heewon Kim, Sungyong Baik, Myungsub Choi, Janghoon Choi, and Kyoung Mu Lee. "Searching for Controllable Image Restoration Networks". *Proc. International Conference on Computer Vision (ICCV), 2021*.
- Geonwoon Jang\*, Wooseok Lee\*, Sanghyun Son, and Kyoungmu Lee. "C2N: Practical Generative Noise Modeling for Real-World Denoising". *Proc. International Conference on Computer Vision (ICCV), 2021*.
- Mohsen Yavartanoo\*, Jaeyoung Chung\*, Reyhaneh Neshatavar, and Kyoung Mu Lee. "3DIAS: 3D Shape Reconstruction with Implicit Algebraic Surfaces". *Proc. International Conference on Computer Vision (ICCV), 2021*.
- Jaeyoo Park, Minsoo Kang, and Bohyung Han. "Class-Incremental Learning for Action Recognition in Videos". *Proc. International Conference on Computer Vision (ICCV), 2021*.
- Sungyong Baik, Junghoon Oh, Seokil Hong, and Kyoung Mu Lee. "Learning to Forget for Meta-Learning via Task-and-Layer-Wise Attenuation". *IEEE Trans. Pattern Analysis and Machine Intelligence (TPAMI), accepted*.
- Jaerin Lee, and Kyoung Mu Lee. "Structure-Resonant Discriminator for Image Super-Resolution". *Proc. of Int'l Conf. on Multimedia and Exposition (ICME), 2021*.
- Seungjun Nah, Sanghyun Son, Jaerin Lee, and Kyoung Mu Lee. "Clean Images are Hard to Reblur: A New Clue for Deblurring". *arXiv preprint arXiv:2104.12665, 2021*.
- Hwaseong Ryu, Seung Yeon Shin, Jae Young Lee, Kyoung Mu Lee, Hyo-jin Kang, and Jonghyon Yi. "Joint segmentation and classification of hepatic lesions in ultrasound images using deep learning". *European Radiology, 2021*.
- Seungjun Nah, Sanghyun Son, Suyoung Lee, Radu Timofte, Kyoung Mu Lee. "NTIRE 2021 challenge on image deblurring". *Proc. Computer Vision and Pattern Recognition Workshops (CVPRW), 2021*.
- Sanghyun Son, Suyoung Lee, Seungjun Nah, Radu Timofte, Kyoung Mu Lee. "NTIRE 2021 challenge on video super-resolution". *Proc. Computer Vision and Pattern Recognition Workshops (CVPRW), 2021*.
- Seung Yeon Shin, Soochahn Lee, Il Dong Yun, and Kyoung Mu Lee. "Topology-Aware Retinal Artery–Vein Classification via Deep Vascular Connectivity Prediction". *Applied Sciences, 2021*.
- Gyeongsik Moon\*, Heeseung Kwon\*, Kyoung Mu Lee, and Minsu Cho. "IntegralAction: Pose-driven Feature Integration for Robust Human Action Recognition in Videos". *Proc. Computer Vision and Pattern Recognition Workshops (CVPRW), 2021. (ORAL presentation)*.
- Jaehyoung Yoo, Dongwook Lee, Changyong Son, Sangil Jung, ByungIn Yoo, Changkyu Choi, Jae-Joon Han, and Bohyung Han. "RaSNet: Learning Tiny Models by Raster-Scanning Images". *Proc. Computer Vision and Pattern Recognition (CVPR), 2021*.
- Sanghyun Son and Kyoung Mu Lee. "SRWarp: Generalized Image Super-Resolution under Arbitrary Transformation". *Proc. Computer Vision and Pattern Recognition (CVPR), 2021*.
- Hongsuk Choi, Gyeongsik Moon, Ju Yong Chang, and Kyoung Mu Lee. "Beyond Static Features for Temporally Consistent 3D Human Pose and Shape from a Video". *Proc. Computer Vision and Pattern Recognition (CVPR), 2021*.
- Seungmin Lee\*, Dongwan Kim\*, Bohyung Han. "CoSMo: Content-Style Modulation for Image Retrieval with Text Feedback". *Proc. Computer Vision and Pattern Recognition (CVPR), 2021*.
- Jaedong Hwang, Seoung Wug Oh, Joon-Young Lee, and Bohyung Han. "Exemplar-Based Open-Set Panoptic Segmentation Network". *Proc. Computer Vision and Pattern Recognition (CVPR), 2021*.
- Jaedong Hwang\*, Seohyun Kim\*, Jeany Son, and Bohyung Han. "Weakly Supervised Instance Segmentation by Community Learning". *Winter Conference on Applications of Computer Vision (WACV), 2021*.
- Suyoung Lee\*, Myungsub Choi\*, and Kyoung Mu Lee. "DynaVSR: Dynamic Adaptive Blind Video Super-Resolution". *Winter Conference on Applications of Computer Vision (WACV), 2021*.

## 국내 학회 논문 (2021–2023)

누리집 Domestic Publications 페이지에서 2021–2026년에 발표한 9편([128]–[136])이다. 모두 이경무 교수가 저자인 영상처리 및 이해에 관한 워크샵(제33–35회) 발표이고, 번호와 표기는 누리집 그대로다.[^dompubs]

- [136] 오정택, 정재영, 이경무, "영상 초해상화 기반 신경 방사장", 제35회 영상처리 및 이해에 관한 워크샵, 2023년 2월
- [135] 김동환, 이경무, "적응형 Positional Embedding을 활용한 Neural Radiance Fields의 성능 개선", 제35회 영상처리 및 이해에 관한 워크샵, 2023년 2월
- [134] 정성호, 남형진, 이경무, "비디오 인체 메쉬 추정에서 공간-시간 편향 완화를 위한 트랜스포머 기반 인코딩 네트워크", 제35회 영상처리 및 이해에 관한 워크샵, 2023년 2월
- [133] 강지훈, 이경무, "트랜스포머를 이용한 래스터 이미지 벡터화 자기 지도학습", 제34회 영상처리 및 이해에 관한 워크샵, 2022년 2월
- [132] 남형진, 이경무, "트랜스포머 기반의 시간적 일관성을 유지하는 3차원 인체 메쉬 추정", 제34회 영상처리 및 이해에 관한 워크샵, 2022년 2월
- [131] 손현진, 이경무, "색깔 임베딩을 포함한 발전된 동적 인공 신경 방사장", 제34회 영상처리 및 이해에 관한 워크샵, 2022년 2월
- [130] 오정훈, 김희원, 백성용, 홍채은, 이경무, "배치 정규화 파라미터를 이용한 채널 프루닝", 제33회 영상처리 및 이해에 관한 워크샵, 2021년 2월
- [129] 홍채은, 김희원, 오정훈, 이경무, "딥러닝 기반 이미지 초해상화 네트워크의 경량화 분포-인지 양자화 기법", 제33회 영상처리 및 이해에 관한 워크샵, 2021년 2월
- [128] 정재영, 야바타누 모흐센, 네스하타바르 레이하네, 이경무, "다변수 사차 다항 곡면 집합을 이용한 삼차원 형상 재구성", 제33회 영상처리 및 이해에 관한 워크샵, 2021년 2월

## 수상

누리집 News 페이지에서 Award로 분류한 글 가운데 2021년 10월 22일–2026년 10월 22일의 8건이다. 날짜와 제목은 글 표기 그대로다.[^news]

- Jun 29, 2026 · Sangmin Hong won the 1st place in Zero-Shot Accident Anticipation Challenge at CVPR 2026 AUTOPILOT Workshop
- Sep 2, 2024 · Mohsen Yavartanoo and Seonguk Seo have awarded Distinguished Dissertation Award
- Jun 21, 2023 · Our lab members won the 1st place in the first RHOBIN challenge at CVPR 2023
- Mar 2, 2022 · Sungyong Baik and Hongsuk Choi have been awarded ‘Distinguished Dissertation Award’
- Feb 14, 2022 · Seoyeon Yang and Jaeyoung Jung have been received 2nd place award in Huggingface & Google Jax global sprint
- Feb 14, 2022 · Seoyeon Yang won the Hyundai ChungMong-Koo Foundation scholarship 2021
- Feb 3, 2022 · Prof. Kyoung Mu Lee has been selected as the recipient of the ’63th Samil Prize’
- Dec 28, 2021 · Sanghyun Son and Geeho Kim won the ‘Qualcomm Innovation Fellowship Korea 2021’

## 소식

누리집 News 페이지에서 Award로 분류하지 않은 2021년 10월 22일–2026년 10월 22일의 글 21건이다. 날짜와 제목은 글 표기 그대로이고, 논문 채택 글은 글 첫 줄의 지도교수 표기(Under the supervision of …)를 괄호에 옮겼다.[^news]

- Jun 29, 2026 · 7 papers got accepted to ECCV 2026! (Under the supervision of Prof. Kyoung Mu Lee and Bohyung Han)
- May 20, 2026 · 3 papers got accepted to ICML 2026! (Under the supervision of Prof. Bohyung Han)
- Feb 23, 2026 · 10 papers got accepted to CVPR 2026! (Under the supervision of Prof. Kyoung Mu Lee and Prof. Bohyung Han)
- Feb 6, 2026 · 2 papers got accepted to ICLR 2026! (Under the supervision of Prof. Kyoung Mu Lee and Prof. Bohyung Han)
- Sep 23, 2025 · 2 papers got accepted to NeurIPS 2025! (Under the supervision of Prof. Kyoung Mu Lee and Bohyung Han)
- Jun 30, 2025 · 3 papers got accepted to ICCV 2025! (Under the supervision of Prof. Kyoung Mu Lee)
- Mar 4, 2025 · 3 papers got accepted to CVPR 2025! (Under the supervision of Prof. Kyoung Mu Lee)
- Feb 10, 2025 · 2 papers got accepted to ICLR 2025! (Under the supervision of Prof. Kyoung Mu Lee and Prof. Bohyung Han)
- Sep 30, 2024 · 5 papers got accepted to NeurIPS 2024! (Under the supervision of Prof. Kyoung Mu Lee and Bohyung Han)
- Jul 2, 2024 · 5 papers got accepted to ECCV 2024! (Under the supervision of Prof. Kyoung Mu Lee and Bohyung Han)
- Apr 25, 2024 · Prof. Jitendra Malik at SNU CVLab
- Feb 27, 2024 · 8 papers got accepted to CVPR 2024! (Under the supervision of Prof. Kyoung Mu Lee and Bohyung Han)
- Oct 17, 2023 · 3 papers got accepted to NeurIPS 2023! (Under the supervision of Prof.Bohyung Han)
- Jul 17, 2023 · 4 papers got accepted to ICCV 2023! (Under the supervision of Prof. Kyoung Mu Lee)
- Feb 28, 2023 · 6 papers got accepted to CVPR 2023! (Under the supervision of Prof. Kyoung Mu Lee and Bohyung Han)
- Jan 28, 2023 · 2 papers got accepted to ICLR 2023! (Under the supervision of Prof. Kyoung Mu Lee)
- Dec 2, 2022 · 1 paper got accepted to AAAI 2023! (Under the supervision of Prof. Kyoung Mu Lee)
- Oct 13, 2022 · 3 papers got accepted to NeurIPS 2022! (Under the supervision of Prof.Bohyung Han)
- Sep 14, 2022 · Prof. Kyoung Mu Lee has been appointed as a Chair-Professor of Seoul National University
- Jul 7, 2022 · 4 papers got accepted to ECCV 2022! (Under the supervision of Prof. Kyoung Mu Lee and Bohyung Han)
- Mar 2, 2022 · 10 papers got accepted to CVPR 2022! (Under the supervision of Prof. Kyoung Mu Lee and Bohyung Han)

## 연락과 위치

- 이경무 교수 전화: 02-880-8885, 02-880-1743(누리집 교수 페이지 표기 +82 02-880-8885 or 02-880-1743)[^kmlee][^faculty]
- 이경무 교수 사무실: 133동 501호(학부 교수 상세 표기)[^eceprof]
- 한보형 교수 전화: 02-880-4154(누리집 표기 +82-2-880-4154)[^faculty][^bhhan]
- 한보형 교수 사무실: 301동 907호(학부 교수 상세 표기)[^ecehan]
- 연구실: 서울대학교 133동 508호(누리집 꼬리말 표기 #508 Bldg. 133, 1 Gwanak-ro, Gwanak-gu, Seoul, Republic of Korea)[^home]
- 학생실 전화: 02-880-6490(누리집 꼬리말 표기 Student Office: +82-2-880-6490)[^home]
- 주소: 08826 서울특별시 관악구 관악로 1 서울대학교 전기·정보공학부[^eceprof]
[^home]: 연구실 누리집 첫 화면 <https://cv.snu.ac.kr/> (Welcome to the SNU Computer Vision Laboratory 칸, 꼬리말의 연구실 이름·위치·전화, 2026-10-23 열람)
[^kmlee]: 누리집 이경무 교수 페이지 <https://cv.snu.ac.kr/index.php/~kmlee/> (직위·연락처, Biography, Professional Activities, Selected Awards and Honors, Recent Publications (Selected) 칸, 2026-10-23 열람)
[^bhhan]: 누리집 한보형 교수 페이지 <https://cv.snu.ac.kr/index.php/~bhhan/> (직위·소속·연락처, News, Education, Employment, Advising, Alumni, Professional Service 칸, 2026-10-23 열람)
[^bhpubs]: 누리집 한보형 교수 Publication 페이지 <https://cv.snu.ac.kr/index.php/~bhhan/publication-bhhan/> (2023년부터 2010 or Earlier까지의 연도 구역, 2026-10-23 열람)
[^faculty]: 누리집 Faculty 페이지 <https://cv.snu.ac.kr/index.php/faculty/> (교수 두 명의 직위·연락처, 2026-10-23 열람)
[^pubs]: 누리집 International Publications 페이지 <https://cv.snu.ac.kr/index.php/publication-international/> (2026년부터 ~2000까지의 연도 구역, 2026-10-23 열람)
[^students]: 누리집 Students 페이지 <https://cv.snu.ac.kr/index.php/students/> (PostDoc., Ph.D. Courses, M.S. Courses 칸, 2026-10-23 열람)
[^alumni]: 누리집 Alumni 페이지 <https://cv.snu.ac.kr/index.php/alumni/> (Co-advised with Professor S. U. Lee 칸 포함, 2026-10-23 열람)
[^dompubs]: 누리집 Domestic Publications 페이지 <https://cv.snu.ac.kr/index.php/domestic-publications/> ([1]–[136], 2026-10-23 열람)
[^news]: 누리집 News 페이지 <https://cv.snu.ac.kr/index.php/news/>와 이전 글 2–4쪽 <https://cv.snu.ac.kr/index.php/news/page/2/>, <https://cv.snu.ac.kr/index.php/news/page/3/>, <https://cv.snu.ac.kr/index.php/news/page/4/> (글 제목·날짜·분류·첫머리, 2026-10-23 열람)
[^ecefac]: 서울대학교 전기·정보공학부 전임교수 목록 <https://ece.snu.ac.kr/research-faculty/faculty/full-time> (2026-10-23 열람)
[^eceprof]: 서울대학교 전기·정보공학부 교수 상세(이경무) <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p061> (직위, 연구실 이름, 전화·사무실, 학위·전공·분야, 학력, 주요경력, Research Interest, 꼬리말 주소, 2026-10-23 열람)
[^ecehan]: 서울대학교 전기·정보공학부 교수 상세(한보형) <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p825> (직위, 연구실 이름, 전화·사무실, 학위·분야, 학력, 주요경력, Research Interest, 2026-10-23 열람)
[^ecelab]: 서울대학교 전기·정보공학부 연구실 목록 <https://ece.snu.ac.kr/research-faculty/research/lab> (연구그룹별 연구실 이름과 교수, 2026-10-23 열람)
[^ecelabv]: 서울대학교 전기·정보공학부 연구실 상세(컴퓨터비젼 연구실) <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=74> (영문 이름, 지도·연구·WEBSITE 줄, 2026-10-23 열람)
[^checked]: OpenReview 기록 <https://openreview.net/forum?id=8YqfXYof0Y> (Pri4R, CoRL 2026 Poster), <https://openreview.net/forum?id=E8m9sL7N0d> (Infinite-Precision Autoregressive Modeling, ICML 2026 regular), <https://openreview.net/forum?id=PN8EiOzMuT> (Score-Repellent Monte Carlo, ICML 2026 spotlight), <https://openreview.net/forum?id=Alelgxnwgs> (Hybrid Space-Aware Randomized Defense, ICML 2026 regular), <https://openreview.net/forum?id=kJqsh7H8f7> (Probabilistic Signature Inversion, CoRR 2026, arXiv 2606.15332) (OpenReview 검색 API 응답, 2026-10-23 열람)
[^p1]: J. Park, K. M. Lee, International Conference on Learning Representations (ICLR) 2026(OpenReview 기록 표기 ICLR 2026 Poster). <https://openreview.net/forum?id=66Ad0i78lW> 초록 기준(OpenReview 게시 초록).
[^p2]: C. Hong 외, K. M. Lee, Computer Vision – ECCV 2022(Lecture Notes in Computer Science), 367-383 (온라인 2022-11-13). <https://doi.org/10.1007/978-3-031-20071-7_22> 초록 기준(arXiv 판, <https://arxiv.org/abs/2207.10345>).
[^p3]: J. Park 외, K. M. Lee, 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 1486-1495 (2022). <https://doi.org/10.1109/cvpr52688.2022.00155> 초록 기준(CVF Open Access 논문 페이지 게시 초록, <https://openaccess.thecvf.com/content/CVPR2022/html/Park_HandOccNet_Occlusion-Robust_3D_Hand_Mesh_Estimation_Network_CVPR_2022_paper.html>).
[^p4]: H. Nam, D. S. Jung, K. M. Lee, Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 7100-7110 (2026). <https://openaccess.thecvf.com/content/CVPR2026/html/Nam_TeHOR_Text-Guided_3D_Human_and_Object_Reconstruction_with_Textures_CVPR_2026_paper.html> 초록 기준(CVF Open Access 논문 페이지 게시 초록).
[^p5]: S. Lee, J. Chung, J. Huh, K. M. Lee, Advances in Neural Information Processing Systems 37, 57050-57075 (2024). <https://doi.org/10.52202/079017-1818> 초록 기준(OpenReview 게시 초록, <https://openreview.net/forum?id=z4WcP0SmGc>).
[^p6]: M. Kim, J. Lim, B. Han, Advances in Neural Information Processing Systems 37, 129209-129226 (2024). <https://doi.org/10.52202/079017-4104> 초록 기준(OpenReview 게시 초록, <https://openreview.net/forum?id=0sycTGl4In>).
[^p7]: J. Kim, J. Kang, J. Choi, B. Han, Advances in Neural Information Processing Systems 37, 89834-89868 (2024). <https://doi.org/10.52202/079017-2853> 초록 기준(OpenReview 게시 초록, <https://openreview.net/forum?id=uikhNa4wam>).
[^p8]: J. Choi, J. Kang, B. Han, International Conference on Learning Representations (ICLR) 2025(OpenReview 기록 표기 ICLR 2025 Poster). <https://openreview.net/forum?id=rCGleSgNBK> 초록 기준(OpenReview 게시 초록).

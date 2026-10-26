# 대용량 그래픽스, 비젼, 로보틱스 연구실 (Scalable Graphics, Vision & Robotics Lab, SGVR Lab)

**KAIST 전산학부·안보과학기술대학원 · 윤성의 교수**

- 분야: 렌더링(대용량 모델 렌더링, 몬테카를로 렌더링 잡음 제거)과 3차원 장면 복원·생성, 로봇의 경로 계획과 이동(매니퓰레이터 궤적 최적화, 사족 보행 로봇의 자세 적응 이동, 음원 위치 추정), 대규모 이미지 검색과 시각 장소 인식, 인공지능 모델의 적대적 강건성과 이미지·3차원 자산 보호
- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 컴퓨터 그래픽스·기하 처리[^cslab][^p1][^p2], 3차원 복원·인식[^p2][^share][^glint], 컴퓨터 비전[^cslab][^p5][^p6], 로봇 항법·SLAM[^cslab][^p4], 보행·휴머노이드 로봇[^p4], 강화학습[^acm][^p3], AI·기계학습 보안·프라이버시[^p7]
- 홈페이지: 전산학부 연구실 소개 페이지 <https://cs.kaist.ac.kr/research/labView?sn=61&menu=64>
- 근거와 출처: [SGVR Lab 근거 페이지](sglab-sources.md)

> 컴퓨터 그래픽스, 로봇 경로 생성, 이미지 검색에 쓰이는 대용량 데이터를 효율적으로 다루는 일을 공통 목표로 삼아 온 전산학부 연구실로,[^cslab] 최근에는 3차원 장면 복원, 사족 보행 로봇의 이동, 인공지능 모델의 강건성과 보호도 연구한다.[^p2][^p4][^p7][^p8]

## 무엇을 연구하나

연구실은 KAIST 전산학부 윤성의 교수가 이끄는 연구실이다.[^csprof][^cslab] 전산학부 연구실 소개는 이름을 「대용량 그래픽스, 비젼, 로보틱스 연구실」과 영문 Scalable Graphics, Vision & Robotics Lab(SGVR Lab)으로 적고,[^cslab] 안보과학기술대학원 교수 명단은 같은 연구실을 Scalable Graphics, Vision & Robotics Lab.으로 올리며 교수의 소속학과를 전산학부, 연구분야를 인공지능/무인체계, 세부 연구 분야를 로보틱스·컴퓨터비전·컴퓨터 그래픽스·보안 기술로 적는다.[^gst] 연구실 소개에 따르면 연구실은 영화, 이미지 검색, 무인자동차 등에 쓰이는 차세대 기술인 컴퓨터 그래픽스, 모션 플래닝(motion planning, 로봇 같은 움직이는 대상이 시작 상태에서 목표 상태까지 장애물에 부딪치지 않고 움직일 경로를 계산하는 일), 이미지 검색 분야를 다루며, 각 기술에 쓰이는 대용량 데이터를 효율적으로 다루는 연구를 공통 목표로 한다.[^cslab] 영화와 게임의 컴퓨터 그래픽이 고화질·고품질이 되고 스마트 기기 보급으로 많은 이미지 데이터가 생겨나면서 대량의 데이터를 빠르게 렌더링하고 검색·처리하는 기술이 필요해졌다고 보고, 세부 연구 주제로 대용량 렌더링(scalable rendering), 충돌 검사(collision detection, 물체끼리 부딪치는지를 계산으로 판정하는 일), 모션 플래닝, 이미지 검색(image retrieval)을 든다.[^cslab] 2026년 3월 전산학부 소식에 따르면 윤성의 교수(연구책임자) 연구팀이 물리 지능(Physical Intelligence) 기반 차세대 인공지능을 연구하는 정보통신기획평가원 과제에 선정됐고,[^iitp] 교수는 같은 해 9월 출범한 KAIST AGI 연구소에 참여한다.[^agi]

첫째 갈래는 **렌더링과 3차원 장면 복원**이다. 연구실 소개는 대용량 모델을 실시간으로 렌더링하려고 CPU와 GPU처럼 형태가 다른 연산 장치를 함께 쓰는 새 프레임워크를 제안하는 연구와, 실사 렌더링 효과를 위한 필터링 방법을 연구한다고 적는다.[^cslab] 2025년 전산학부 소식은 교수의 연구 분야를 대용량 3D 모델을 빠르고 효율적으로 처리하는 스케일러블 렌더링(scalable rendering), 물리 기반 시뮬레이션과 데이터 생성, AI·컴퓨터 비전에서 쓰는 여러 학습 기법으로 소개하고, KAIST 부임 뒤의 연구 주제로 물리 기반 렌더링을 든다.[^acm] 대표 논문에서는 몬테카를로 렌더링(화소에 들어오는 빛의 양을 무작위로 뽑은 표본 계산들의 평균으로 어림하는 렌더링 방법)이 만든 잡음 낀 이미지를 다듬을 때, 화소마다 기하 정보와 빛 경로 정보 가운데 어느 보조 특징을 우세하게 쓸지 안내하는 잡음 제거 틀을 내놓았고,[^p1] 정밀한 카메라 자세 정보 없이 3D 가우시안 스플래팅(장면을 여러 개의 3차원 가우시안 함수로 나타내고, 이를 화면에 투영해 이미지를 그리는 방법) 장면을 복원하는 SHARE를 만들었다.[^p2] 전산학부 소식은 SHARE가 일반 사진 2~3장만으로 현실 환경을 3차원 공간으로 복원한다고 소개한다.[^share] 같은 소식 게시판에 따르면 유리창·진열장처럼 투명한 물체가 있는 장면에서 유리 표면에서 반사되는 빛과 유리를 통과하는 빛을 나눠 모델링하는 GLINT가 CVPR 2026의 구두 발표 논문이자 수상 후보(Award Candidate)로 뽑혔다.[^glint] 최근 논문 목록에는 역 몬테카를로 렌더링을 위한 이미지 잡음 제거(ACM Transactions on Graphics, 2024), 의미 정보를 담은 3차원 장면 생성(SemCity, CVPR 2024), 적은 수의 시점 사진으로 표면을 복원하는 연구(UFORecon, CVPR 2024), 움직이는 장면의 방사장(공간의 위치와 보는 방향에 따라 빛의 색과 부피 밀도를 내주는 함수로 장면을 나타낸 표현)을 운동학 장으로 규제하는 연구(ECCV 2024), 영상 속 관절 물체의 3차원 동작을 옮기는 연구(MorphGS, ECCV 2026)도 있다.[^pubs]

둘째 갈래는 **로봇의 경로 계획과 이동**이다. 연구실 소개는 로봇 경로 생성이 로봇과 환경 사이의 충돌 없는 경로 생성은 물론, 무인자동차처럼 사람의 제어를 거치지 않고 스스로 환경을 인지하고 움직임을 만드는 실용적인 예에 이른다고 설명하고, 최적 경로의 생성과 그 수렴성, 불확실성 등을 고려하는 파생 연구도 비중 있게 한다고 적는다.[^cslab] 2022년 전산학부 소식은 연구실이 2012년부터 해 온 전기및전자공학부 심현철 교수와의 무인차 연구, 전산학부 조성호 교수·기계공학부 오준호 명예교수와의 휴머노이드 과제, 전기및전자공학부 명현 교수와의 드론 과제, 기계공학부 박해원 교수와의 사족 로봇 과제에서 여러 로봇 경로 생성 연구를 하고 있다고 적는다.[^icra22] 2025년 전산학부 소식은 로봇 경로 계획과 강화학습을 교수의 연구 주제로 든다.[^acm] 대표 논문에서는 여분 자유도 매니퓰레이터(작업에 필요한 수를 넘는 관절 자유도를 가진 로봇 팔)가 정해진 손끝 경로를 따라가는 관절 궤적을 최적화할 때 강화학습으로 좋은 초기 궤적을 짧은 시간에 만들어 주는 방법을 내놓았고,[^p3] 사족 보행 로봇이 로봇에 달린 깊이 영상(화소마다 카메라에서 물체까지의 거리를 담은 영상)을 바로 써서 목표를 향해 가고, 높이가 낮은 좁은 공간에서는 몸 자세를 바꿔 지나가는 계층적 이동 틀 HiPAN을 만들었다.[^p4] 2023년 6월 전산학부 소식은 윤성의 교수 연구팀의 「리던던트 로봇 매니퓰레이터를 사용한 최적화 기반의 경로 추종 문제에 대한 학습 기반 초기화 기술」 연구가 ICRA 2023에서 Outstanding Planning Paper Award를 수상했다고 적는다.[^icra23] 최근 논문 목록에는 사족 보행 로봇이 다리로 물체를 다루는 연구(International Journal of Control, Automation and Systems, 2025)와 스케이트보드를 타는 연구(ICRA 2026), 옮길 수 있는 장애물 사이를 지나는 이동 매니퓰레이터 주행(IROS 2025), CCTV 정보를 쓰는 붐비는 실내의 로봇 주행(IEEE Robotics and Automation Letters, 2024), 회절과 반사를 고려한 여러 음원의 위치 추정(IEEE Transactions on Robotics, 2022)도 있다.[^pubs] 2025년 전산학부 소식은 윤성의 교수의 지도로 KAIST 박사 학위를 받은 안인규 박사가 3차원 공간에서 소리의 위치를 추적하는 기술을 개발했다고 적는다.[^al-ahn]

셋째 갈래는 **대규모 영상 검색과 장소 인식**이다. 연구실 소개는 수천만에서 수억 개에 이르는 이미지 데이터베이스에서 비슷한 이미지를 높은 정확도와 효율로 찾는 대규모 이미지 검색을 연구하며, 많은 시각 정보를 간략하게 나타내는 압축 기법과 압축한 데이터로 빠르게 유사도를 검색하면서도 정확하게 찾게 하는 일을 주된 연구 방향으로 삼고, 최근에는 이미지 검색 밖의 다른 컴퓨터 비전 분야에도 유사도 검색 기술을 적용한다고 적는다.[^cslab] 대표 논문에서는 미세 조정(이미 학습한 모델을 특정 자료로 추가 학습시키는 일)에 쓸 자료가 없을 때 검색된 이미지가 같은 물체를 담았는지 특징점 사이의 위상 관계로 검증하는 방법을 내놓았고,[^p5] 질의 이미지가 찍힌 장소를 알아내는 시각 장소 인식에서 장기간에 걸친 극단적인 외관 변화에도 견디도록 학습 목표를 바꿨다.[^p6] 최근 논문 목록에는 화소 단위 이미지 검색(ICCV 2023), 서로 다른 카메라에 찍힌 같은 사람을 찾는 사람 재식별(CVPR 2022, NeurIPS 2024), 질문 의도에 맞는 영상 구간을 찾는 영상 질의응답(ECCV 2026), 여러 시점의 다중 물체 추적을 위한 무인기 실측 데이터셋(IEEE Robotics and Automation Letters, 2026)도 있다.[^pubs] 2025년에는 이화여대 노준혁 교수 연구팀과 함께 만든 영상 질의응답 틀 CORTEX로 ICCV 2025 인지 테스트 대회 GVQA 트랙에서 23개 팀 가운데 1위를 했다.[^cortex]

넷째 갈래는 **인공지능 모델의 강건성과 보호**다. 강건성은 입력에 잡음이나 변화, 공격이 더해져도 모델이 성능을 유지하는 성질을 말한다. 안보과학기술대학원 교수 명단은 교수의 세부 연구 분야에 보안 기술을 든다.[^gst] 대표 논문에서는 적대적 공격(모델이 틀린 답을 내도록 입력을 의도적으로 조작하는 공격)을 받을 때 잘못된 예측을 일으키는 신경망 특징을 나눠 다시 보정해 강건성을 높이는 FSR을 내놓았고,[^p7] 확산 모델(데이터에 잡음을 단계적으로 더하는 과정을 거꾸로 되돌리도록 학습해 새 데이터를 만드는 생성 모델)로 사진 일부를 허락 없이 바꿔 그리는 인페인팅 악용을 막으려고, 이미지에 적대적 섭동을 넣어 그 작업을 방해하는 방어 틀 AdvPaint를 만들었다.[^p8] 최근 논문 목록에는 방사장과 3D 가우시안 스플래팅으로 만든 3차원 자산을 지키는 연구(AegisRF, SplatShield), 완전히 다시 생성된 이미지에서 변조된 위치를 찾는 연구(APT, ECCV 2026), 여러 종류의 적대적 섭동에 강건한 모델 구조(RoME, ECCV 2026), 로봇의 시각 운동 정책이 가진 취약점을 살피는 연구(ICRA 2026)도 있다.[^pubs]

## 주요 연구 주제

### 1. 렌더링과 3차원 장면 복원

대용량 모델 렌더링, 몬테카를로 렌더링의 잡음 제거, 카메라 자세 정보 없는 3D 가우시안 스플래팅 복원, 투명한 물체가 있는 장면의 복원.[^cslab][^p1][^p2][^glint]

### 2. 로봇의 경로 계획과 이동

충돌 없는 경로 생성, 여분 자유도 매니퓰레이터의 궤적 최적화를 위한 학습 기반 초기화, 사족 보행 로봇의 자세 적응 이동.[^cslab][^p3][^p4]

### 3. 대규모 영상 검색과 장소 인식

압축 기반 대규모 이미지 검색, 미세 조정 없는 검색 결과 검증, 극단적인 외관 변화 아래의 시각 장소 인식.[^cslab][^p5][^p6]

### 4. 인공지능 모델의 강건성과 보호

적대적 공격에 강건한 특징 보정, 확산 모델 인페인팅 악용을 막는 이미지 보호.[^gst][^p7][^p8]

## 대표 논문

교수 이름으로 등록된 2021–2026년 공개 서지 가운데 윤성의 교수가 마지막 저자인 논문을 네 연구 갈래에 두 편씩 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2023 | [Pixel-wise Guidance for Utilizing Auxiliary Features in Monte Carlo Denoising](https://doi.org/10.1145/3585505) · Proceedings of the ACM on Computer Graphics and Interactive Techniques | 화소마다 장면의 기하 정보를 담은 G-버퍼(geometric buffers)와 빛의 경로를 요약한 P-버퍼(path descriptors) 같은 보조 특징은 몬테카를로(MC) 렌더링 이미지의 잡음 제거를 크게 개선한다고 알려져 있다. 그러나 최근 방법들은 보조 특징을 쓰는 법을 암묵적으로 배우므로 종류마다 보조 특징을 충분히 쓰지 못할 수 있다. 이를 풀려고 보조 특징 활용을 화소 단위로 명시적으로 안내하는 잡음 제거 틀을 제안했다. 먼저 G-버퍼와 P-버퍼로 각각 학습한 잡음 제거기 두 개를 만들고, 화소마다 어느 보조 특징이 우세해야 하는지를 나타내는 가중치 지도를 얻는 앙상블(여러 모델의 결과를 합치는 방법) 신경망을 설계해 두 잡음 제거 결과를 합쳤다. 잡음 제거기와 앙상블 신경망을 함께 학습시켜, 잡음 제거기가 G-버퍼나 P-버퍼가 상대적으로 중요한 영역에 집중하도록 이끌었다. G-버퍼와 P-버퍼를 모두 쓰는 기준 잡음 제거 모델보다 잡음 제거 성능이 상당히 나아졌다.[^p1] | 1저자 K. B. Han, 마지막 저자 윤성의 |
| 2 | 2025 | [Pose-Free 3D Gaussian Splatting via Shape-Ray Estimation](https://doi.org/10.1109/icip55913.2025.11084718) · ICIP 2025 | 일반화 가능한 3D 가우시안 스플래팅은 처음 보는 장면도 효율적으로 고품질로 그려 내지만, 정확한 기하를 얻으려면 정밀한 카메라 자세(위치와 방향)에 크게 의존한다. 실제 환경에서는 정확한 자세를 얻기 어려워 자세 추정에 잡음이 끼고 기하가 어긋난다. 이를 풀려고 모양과 카메라 광선을 함께 추정해 이런 모호함을 극복하는, 자세 정보가 필요 없는 피드포워드(입력에서 출력 쪽으로 한 방향으로만 계산하는) 방식의 가우시안 스플래팅 틀 SHARE를 내놓았다. 명시적인 3차원 변환에 기대지 않고 여러 시점의 정보를 합치는 자세 인식 기준 볼륨 표현을 만들어, 부정확한 자세 추정에서 오는 어긋남을 줄였다. 또 거친 기준점(앵커) 주변의 국소 기하를 다듬는 앵커 정렬 가우시안 예측으로 가우시안을 더 정확한 자리에 놓아 장면 복원을 개선했다. 여러 실제 환경 데이터셋 실험에서 자세 정보 없는 일반화 가우시안 스플래팅에서 강건한 성능을 보였다.[^p2] | 공동 1저자 나영주·김태연[^share], 마지막 저자 윤성의 |
| 3 | 2023 | [Learning-based Initialization of Trajectory Optimization for Path-following Problems of Redundant Manipulators](https://doi.org/10.1109/icra48891.2023.10161426) · ICRA 2023 | 궤적 최적화(TO, 정해진 조건 안에서 비용을 가장 작게 하는 움직임 경로를 수치 계산으로 찾는 방법)는 여분 자유도 매니퓰레이터가 6차원 직교 좌표 경로(로봇 손끝의 위치와 방향을 함께 정한 경로)를 따라가는 관절 궤적을 만드는 효율적인 도구다. 최적화 성능은 초기 궤적의 질에 크게 좌우되는데, 해가 되는 궤적의 공간이 매우 크고 관절 공간에서 작업 제약에 대한 사전 지식이 없어 좋은 초기 궤적을 고르기는 쉽지 않고 시간도 많이 든다. 이를 덜려고 예시가 이끄는 강화학습으로 짧은 시간 안에 좋은 초기 궤적을 만드는 학습 기반 방법을 내놓았다. 또 전문가 시연에 담긴 기구학적으로 실행 가능한 동작을 효율적으로 배우도록, 영공간(손끝의 위치와 방향을 바꾸지 않는 관절 움직임들의 집합) 제약을 고려하는 영공간 투영 모방 보상을 제안했다. 시뮬레이션의 통계 평가에서 이 방법의 결과를 궤적 최적화에 넣으면 다른 세 기준 방법보다 최적성, 효율, 적용 범위가 나아졌고, 7자유도 매니퓰레이터로 한 실제 실험에서도 성능 향상과 실현 가능성을 보였다.[^p3] | 1저자 M. Yoon, 마지막 저자 윤성의 |
| 4 | 2026 | [HiPAN: Hierarchical Posture-Adaptive Navigation for Quadruped Robots in Unstructured 3D Environments](https://doi.org/10.1109/lra.2026.3692054) · IEEE Robotics and Automation Letters | 구조가 정돈되지 않은 3차원 환경에서 사족 보행 로봇을 이동시키려면 목표를 향한 움직임, 국소 최소점(가까운 주변에서는 비용이 가장 낮지만 전체에서 가장 낮지는 않은 지점)에서 빠져나오는 탐색, 높이가 제한된 좁은 공간을 지나기 위한 자세 조정이 필요하다. 기존 방법은 지도 작성과 경로 계획을 차례로 하는 처리 과정을 쓰지만, 인식 오류가 쌓이고 계산 부담이 커서 계산 자원이 제한된 로봇에서 쓰기 어렵다. 이를 풀려고 실제로 쓸 때 로봇에 달린 깊이 영상을 바로 쓰는 계층적 자세 적응 이동 틀 HiPAN을 내놓았다. 상위 정책(상황에 따라 어떤 행동을 할지 정하는 규칙)이 평면 속도와 몸 자세라는 이동 명령을 만들면, 하위의 자세 적응 보행 제어기가 이를 실행한다. 근시안적인 행동을 줄이고 먼 거리 이동을 돕도록, 이동 범위를 반응형 장애물 회피에서 전략적 이동으로 점차 넓히는 경로 유도 커리큘럼 학습(쉬운 과제에서 어려운 과제 순서로 학습시키는 방법)을 도입했다. 시뮬레이션에서 고전적인 반응형 계획기와 종단간(입력에서 출력까지 하나의 모델로 바로 학습하는) 기준 방법보다 이동 성공률과 경로 효율이 높았고, 실제 실험으로 여러 비정형 3차원 환경에서 쓸 수 있음을 확인했다.[^p4] | 1저자 J. Jeong, 마지막 저자 윤성의 |
| 5 | 2023 | [Topological RANSAC for instance verification and retrieval without fine-tuning](https://doi.org/10.52202/075280-2788) · NeurIPS 2023 | 미세 조정에 쓸 자료가 없는 상황에서 설명 가능한 이미지 검색을 개선하는 방법을 내놓았다. 널리 쓰이는 공간 검증(SP) 방법은 효과적이지만, 공간 모형과 가설 검정 전략으로 같은 물체를 알아보기 때문에 평면 구조를 가정하고 특징점 사이의 위상 관계(점들이 서로 어떻게 이웃하고 이어져 있는지의 관계)를 무시하는 한계가 있다. 이를 풀려고 RANSAC(무작위로 고른 일부 자료로 모형을 세우고 그 모형에 들어맞는 자료가 가장 많은 모형을 고르는 일을 되풀이하는 추정 방법) 과정 안의 공간 모형을 위상 모형으로 바꾸었다. 생물에서 착안한 단속 운동(saccade, 시선을 한 점에서 다른 점으로 빠르게 옮기는 눈 운동)·중심와(fovea, 망막 가운데의 또렷하게 보는 부분) 함수로 특징 사이의 위상 일관성을 검증해 공간 모형의 문제를 피했다. 실험에서 SP보다 성능이 크게 좋았고 미세 조정 없는 검색에서 최고 수준(state-of-the-art)의 성능을 냈으며, 미세 조정한 특징과 함께 써도 성능을 높일 수 있었다. 설명 가능성이 높고 가벼워 여러 실제 응용에 맞춰 쓸 수 있는 방법이라고 적는다.[^p5] | 1저자 G. An, 마지막 저자 윤성의 |
| 6 | 2026 | [Class-Relational Approach for Visual Place Recognition under Extreme Appearance Changes](https://doi.org/10.1109/lra.2026.3669068) · IEEE Robotics and Automation Letters | 시각 장소 인식(VPR)은 질의 이미지가 찍힌 위치를 추정하는 과제로, 주로 위치 정보가 붙은 기준 이미지 데이터베이스에서 학습한 전역 기술자(이미지 전체를 요약한 특징 벡터)로 이미지를 검색해 수행한다. 최근에는 분류 손실(분류가 틀린 정도를 재는 학습 목표)을 대리 과제로 써서 VPR 학습의 규모를 키우려 했지만, 이 목표는 특징 공간을 서로 다른 클래스 영역으로 나눠 클래스 사이의 시각적 차이를 놓치는 경우가 많다. 이렇게 나뉘면 장기간에 걸친 변화(lifelong variations) 같은 극단적인 시각 변화에 특히 약해진다. 이를 바로잡으려고 클래스 사이 관계의 시각 정보를 고려해 원-핫 레이블(정답 클래스 하나만 켜 둔 정답 표시)을 소프트 레이블(여러 클래스에 확률을 나눠 준 정답 표시)로 바꾸는 클래스 관계 목표(CRO)를 제안했다. 또 클래스 안정성의 지표가 되는 클래스 가중치 크기에 따라 CRO의 영향을 동적으로 조절해 방법을 강화했고, 이 지표를 미분 분석으로 뒷받침했다. 일반적인 시각 변화부터 극단적인 장기 변화까지 여러 벤치마크 실험에서 기존 방법보다 나았다.[^p6] | 1저자 J. Kim, 마지막 저자 윤성의 |
| 7 | 2023 | [Feature Separation and Recalibration for Adversarial Robustness](https://doi.org/10.1109/cvpr52729.2023.00791) · CVPR 2023 | 심층 신경망은 특징 수준에서 섭동(입력이나 특징에 더해진 변화)이 쌓여 적대적 공격에 취약하고, 많은 연구가 잘못된 예측을 일으키는 강건하지 않은 특징 활성화를 꺼서 모델의 강건성을 높여 왔다. 연구팀은 이런 활성화에도 구별에 쓸 단서가 남아 있어 다시 보정하면 올바른 예측에 쓸 정보를 더 얻을 수 있다고 보았다. 이를 위해 강건하지 않은 활성화를 다시 보정해 더 강건한 특징 지도를 얻는, 쉽게 끼워 쓸 수 있는 방법 FSR(Feature Separation and Recalibration)을 제안했다. 분리 단계는 입력 특징 지도를 올바른 예측을 돕는 강건한 특징과 적대적 공격을 받으면 오예측을 일으키는 강건하지 않은 특징으로 나누고, 재보정 단계는 강건하지 않은 활성화를 조정해 예측에 쓸모 있을 수 있는 단서를 되살린다. 실험에서 기존의 활성화 끄기 기법보다 우수했고, 적은 계산 부담으로 기존 적대적 학습(공격받은 예시를 함께 써서 모델을 학습시키는 방법) 방법의 강건성을 최대 8.57% 높였다.[^p7] | 1저자 W. J. Kim, 마지막 저자 윤성의 |
| 8 | 2025 | [AdvPaint: Protecting Images from Inpainting Manipulation via Adversarial Attention Disruption](https://doi.org/10.48550/arxiv.2503.10081) · arXiv 사전 공개본(arXiv 저자 메모 「Accepted to ICLR 2025」) | 확산 모델의 고품질 이미지 생성 능력은 악용될 때 큰 위협이 된다. 특히 특정 영역을 유명인으로 바꾸는 것처럼 확산 모델을 인페인팅(이미지의 일부 영역을 새로 채워 그리는 작업)에 악용하는 공격자를 가정했다. 확산 기반 생성 모델의 조작에서 이미지를 보호하는 기존 방법은 주로 이미지에서 이미지를, 글에서 이미지를 만드는 작업에 집중했고, 허락받지 않은 인페인팅을 막는 문제는 거의 다뤄지지 않아 보호 성능이 충분하지 않은 경우가 많았다. 인페인팅 악용을 줄이려고 공격자의 인페인팅 작업을 효과적으로 방해하는 적대적 섭동을 만드는 방어 틀 ADVPAINT를 제안했다. ADVPAINT는 대상 확산 인페인팅 모델의 자기 주의·교차 주의 블록(한 입력 안의 위치끼리, 서로 다른 두 입력 사이의 관련성을 계산하는 신경망 부분)을 겨냥해 이미지 생성 중의 의미 이해와 프롬프트(모델에 글로 준 지시) 상호작용을 흐트러뜨린다. 또 물체를 둘러싼 확대한 경계 상자를 기준으로 섭동 영역을 나누는 2단계 섭동 전략으로, 모양과 크기가 다양한 마스크에서도 강건하게 했다. 실험에서 ADVPAINT의 섭동은 공격자의 인페인팅을 효과적으로 방해해 기존 방법보다 나았고, FID(생성 이미지와 실제 이미지의 특징 분포 사이 거리를 재는 지표)가 100포인트 넘게 늘고 정밀도가 크게 줄었다.[^p8] | 1저자 J. Jeon, 마지막 저자 윤성의 |

## 교수와 전문 분야

윤성의 교수는 KAIST 전산학부 교수이며, 전산학부 교수진 목록과 교수 소개는 직위를 「교수, Endowed Professor」로 적는다.[^cslist][^csprof] 교수 소개의 연구분야는 비주얼 컴퓨팅, 인공지능·정보서비스, 인터랙티브 컴퓨팅이고 전공은 컴퓨터그래픽스, 컴퓨터비젼, 로보틱스다.[^csprof] 서울대학교에서 전산학 학사와 석사를, 미국 노스캐롤라이나 대학교 채플힐(University of North Carolina at Chapel Hill)에서 전산학 박사 학위(2005)를 받았고, 미국 로렌스 리버모어 국립연구소(Lawrence Livermore National Laboratory)에서 박사후연구원으로 컴퓨터 그래픽스와 대규모 데이터 처리 기술을 연구했다.[^csprof][^acm] 2007년 KAIST 전산학부에 부임했다.[^acm] 안보과학기술대학원 교수 명단에도 소속학과 전산학부로 올라 있다.[^gst]

교수 소개는 교수가 렌더링, 로봇 경로 생성, 이미지 검색 분야를 연구하며 관련 학회와 학술지에 여러 논문을 발표했고, ACM SIGGRAPH와 IEEE CVPR 같은 학회에서 초청 강연을 많이 했으며, distinguished paper, journal invitations, national-wide recognition을 받았고, IEEE와 ACM의 senior member라고 적는다.[^csprof] 2025년 12월 전산학부 소식에 따르면 교수는 미국 컴퓨터학회(ACM)의 Distinguished Member(특훈회원)로 선정됐다. 이 소식은 교수의 연구가 ACM SIGGRAPH, IEEE CVPR, ICRA 등의 학회에서 강연으로 소개됐고 Test-of-Time Award, Best Paper Award, 저널 초청 논문 등으로 인정받았다고 적는다.[^acm] 2026년 9월 소식에 따르면 교수는 같은 달 출범한 KAIST AGI 연구소에 참여하는 전산학부 교수 5명 가운데 한 명이다.[^agi]

논문으로 보면 지금의 전문 분야는 네 갈래다. 첫째, 몬테카를로 렌더링의 잡음 제거와 3D 가우시안 스플래팅 기반 장면 복원이다(대표 논문 1, 2).[^p1][^p2] 둘째, 여분 자유도 매니퓰레이터의 궤적 최적화와 사족 보행 로봇의 이동처럼 학습을 곁들인 로봇 경로 계획이다(대표 논문 3, 4).[^p3][^p4] 셋째, 미세 조정 없는 이미지 검색 검증과 시각 장소 인식이다(대표 논문 5, 6).[^p5][^p6] 넷째, 적대적 공격에 대한 신경망의 강건성과 생성 모델 악용에서 이미지를 지키는 방어다(대표 논문 7, 8).[^p7][^p8] 2021–2026년 논문 목록에는 이 밖에 음원 위치 추정과 실내 음향 재질 추정, 시계열 분류, 광 신경망 같은 주제의 논문도 있다.[^pubs]

## 응용 분야

연구실 소개는 연구실이 다루는 컴퓨터 그래픽스, 모션 플래닝, 이미지 검색을 영화, 이미지 검색, 무인자동차 등에 쓰이는 차세대 기술로 소개하고, 로봇 경로 생성이 무인자동차처럼 스스로 환경을 인지하고 움직임을 만드는 실용적인 예에 이른다고 적는다.[^cslab] 2025년 전산학부 소식은 교수의 연구 기술이 3D 그래픽스, 로보틱스, 자율주행, 시뮬레이션 기반 AI 등의 핵심 기반 기술로 쓰인다고 적는다.[^acm] 연구 소식들은 GLINT를 로봇, 자율주행, 디지털 트윈, 증강현실(AR), 혼합현실(MR)에,[^glint] 매니퓰레이터 경로 추종 연구를 협동 로봇과 수술 로봇처럼 자유도가 높은 매니퓰레이터 동작이 필요한 상황에,[^icra23] CORTEX를 자율주행차, 보안 감시, 지능형 로봇, 미디어 콘텐츠 분석에 쓸 수 있다고 적는다.[^cortex] 2022년 인터뷰 소식은 로봇 카메라로 사람의 행동을 파악해 돕는 로봇 소셜 인터랙션 기술을 조성호 교수와 함께 연구했고 KT와 서비스 로봇을 연구한다고 적는다.[^kt] 2026년 과제 소식은 물리 지능 기반 인공지능 연구의 성과가 로보틱스, 자율주행, 산업 자동화 등에 쓰일 것으로 기대한다고 적는다.[^iitp] 대표 논문 8은 확산 모델을 이용한 허락받지 않은 인페인팅에서 이미지를 지키는 일을 목표로 한다.[^p8]

## 졸업생과 이전 구성원

KAIST 전산학부 소식 글이 지도교수를 윤성의 교수로 적은 졸업생과, 그 글이 적은 진로다. 연구실 졸업생 전체의 명단이 아니고, 진로는 각 글이 게시된 때의 표기다.

- 문보창: 전산과 석사·박사. Disney Research에서 박사후과정을 거쳐 2016년 9월 광주과학기술원(GIST) 조교수로 임용됐다(2016-09-06 게시).[^al-moon]
- 허재필: 박사(2015). ETRI 연구원을 거쳐 성균관대 조교수로 임용됐다(2017-03-06 게시).[^al-heo]
- 김덕수: 박사(2014). KISTI 연구원을 거쳐 한국기술교육대(KOREATECH) 조교수로 임용됐고(2018-04-16 게시), 2023년 9월 글은 한국기술교육대학교 컴퓨터공학부에 재직 중이라고 적는다.[^al-kim1][^al-kim2]
- 이정인: 석사. 2022년 7월 글은 의료 인공지능 기업 루닛의 창업 멤버이자 CTO로 적는다.[^al-lee]
- 안인규: 박사. 한국전자통신연구원(ETRI) 연구원을 거쳐 2025년 2월 국민대학교 소프트웨어융합학과 조교수로 임용됐다(2025-03-10 게시).[^al-ahn]

## 최근 논문 목록 (2021–2026)

교수의 공개 서지에서 윤성의 교수가 저자로 확인되는 2021–2026년 논문 85편이다(2021년 9편, 2022년 12편, 2023년 12편, 2024년 17편, 2025년 11편, 2026년 24편).[^pubs] 공개 서지는 출판사 등록 서지(Crossref)의 교수 ORCID 기록과 이름 검색 기록, OpenAlex 저자 기록이다. 연도는 출판사 등록 서지의 발행 연도이고, 출판사 등록 서지가 없는 논문은 OpenAlex 기록의 출판 연도다. 2026년 항목은 2026년 10월 13일까지 출판·공개된 것이다. 제목·저자·학술지와 학회 이름은 서지 기록의 표기다. 출판 기록이 없는 18편은 학술지·학회 자리에 arXiv 번호나 SSRN 원고임을 밝히고 「사전 공개본」으로 표시했으며, arXiv 논문 페이지의 저자 메모(Comments)에 학회 이름이 있으면 「arXiv 저자 메모」로 원문을 붙였다.

**2026**

- Sangmin Lee, Youngju Na, Chanmi Lee, Sung-eui Yoon. "Multi-Agent Coordination via Support-Preserving Distillation". *arXiv:2610.10087 (사전 공개본, 2026; arXiv 저자 메모 「NeurIPS 2026」)*.
- T. Yang, Youngju Na, Yoonki Cho, Sung-Eui Yoon. "Same Scene, Different Task: Skill Alignment for Compositional Generalization in VLAs". *arXiv:2610.00524 (사전 공개본, 2026)*.
- Sejin Oh, Suhyeon Ha, Joonsung Jeon, Sung-Eui Yoon. "SplatShield: Adversarial Protection for 3D Gaussian Splatting Against Instruction-Guided Editing". *2026 IEEE International Conference on Image Processing (ICIP), 1-6 (2026)*.
- Junsik Jung, Seokryun Choi, Yoonki Cho, Woo Jae Kim, Andrew Jeong, Sung-Eui Yoon. "EvBS: Event-guided Blur Synthesis for Domain-adaptive Motion Deblurring". *arXiv:2608.08066 (사전 공개본, 2026; arXiv 저자 메모 「Accepted to ACM Multimedia 2026 (ACM MM 2026)」)*.
- Chungsu Jang, Youngjung Kim, Sebin Lee, Wonsuk Kwon, Taehyun Kim, Yong-Duk Kim, Sung-Eui Yoon. "CrossTrack-UAV: A Real-World Dataset and Baseline for Cross-View Multi-Object Tracking Using Fixed-Wing UAVs". *IEEE Robotics and Automation Letters 11, 7948-7955 (2026)*.
- Jeil Jeong, Minsung Yoon, Seokryun Choi, Heechan Shin, Taegeun Yang, Sung-eui Yoon. "HiPAN: Hierarchical Posture-Adaptive Navigation for Quadruped Robots in Unstructured 3D Environments". *IEEE Robotics and Automation Letters 11, 7980-7987 (2026)*.
- C W Park, Minsung Yoon, Andrew Jeong, Sung-Eui Yoon. "Distilling Collaborative Dynamics into Latent Space for Implicit Coordination in Decentralized Multi-Agent Manipulation". *arXiv:2606.22982 (사전 공개본, 2026; arXiv 저자 메모 「Accepted to IROS 2026」)*.
- Minsung Yoon, Jeil Jeong, Sung-Eui Yoon. "Phase-Aware Policy Learning for Skateboard Riding of Quadruped Robots via Feature-wise Linear Modulation". *2026 IEEE International Conference on Robotics and Automation (ICRA), 2378-2384 (2026)*.
- Jiwoo Hwang, Taegeun Yang, Jeil Jeong, Minsung Yoon, Sung-Eui Yoon. "Uncertainty-Aware Non-Prehensile Manipulation with Mobile Manipulators under Object-Induced Occlusion". *2026 IEEE International Conference on Robotics and Automation (ICRA), 14305-14312 (2026)*.
- Chanmi Lee, Minsung Yoon, Woojae Kim, Sebin Lee, Sung-eui Yoon. "Beyond the Patch: Exploring Vulnerabilities of Visuomotor Policies via Viewpoint-Consistent 3D Adversarial Object". *2026 IEEE International Conference on Robotics and Automation (ICRA), 14377-14384 (2026)*.
- Jaeyoon Kim, Yoonki Cho, Sung-Eui Yoon. "Class-Relational Approach for Visual Place Recognition under Extreme Appearance Changes". *IEEE Robotics and Automation Letters 11, 4881-4888 (2026)*.
- Andrew Jeong, Jaemin Kim, Sebin Lee, Sung-Eui Yoon. "CLaD: Planning with Grounded Foresight via Cross-Modal Latent Dynamics". *arXiv:2603.29409 (사전 공개본, 2026)*.
- Youngju Na, Jaeseong Yun, Soohyun Ryu, Hyunsu Kim, Sung-Eui Yoon, Suyong Yeon. "GLINT: Modeling Scene-Scale Transparency via Gaussian Radiance Transport". *arXiv:2603.26181 (사전 공개본, 2026; arXiv 저자 메모 「CVPR 2026」)*.
- Sebin Lee, Jumin Lee, Taeyeon Kim, Younju Na, Woobin Im, Sung-Eui Yoon. "Visual-RRT: Finding Paths toward Visual-Goals via Differentiable Rendering". *arXiv:2604.16388 (사전 공개본, 2026)*.
- Jumin Lee, Siyeong Lee, Namil Kim, Sung-Eui Yoon. "VERIA: Verification-Centric Multimodal Instance Augmentation for Long-Tailed 3D Object Detection". *arXiv:2603.24294 (사전 공개본, 2026)*.
- Xiangchen Liu, Hanghan Zheng, Jeil Jeong, Minsung Yoon, Lin Zhao, Zhide Zhong, Haoang Li, Sung-Eui Yoon. "DyGeoVLN: Infusing Dynamic Geometry Foundation Model into Vision-Language Navigation". *arXiv:2603.21269 (사전 공개본, 2026)*.
- Jaeyoon Kim, Yoonki Cho, Sung-Eui Yoon. "Towards Test-time Efficient Visual Place Recognition via Asymmetric Query Processing". *Proceedings of the AAAI Conference on Artificial Intelligence 40, 5673-5681 (2026)*.
- Kyu Beom Han, Jaeyoon Kim, Woo Jae Kim, Jinhwan Seo, Sung-Eui Yoon. "Radiometrically Consistent Gaussian Surfels for Inverse Rendering". *arXiv:2603.01491 (사전 공개본, 2026; arXiv 저자 메모 「ICLR 2026 Oral paper」)*.
- Joonsung Jeon, Woo Jae Kim, Suhyeon Ha, Sooel Son, Sung-Eui Yoon. "No Caption, No Problem: Caption-Free Membership Inference via Model-Fitted Embeddings". *arXiv:2602.22689 (사전 공개본, 2026; arXiv 저자 메모 「Accepted to ICLR 2026」)*.
- Jinhwan Seo, Kyubeom Han, Jumin Lee, Junhyug Noh, Sung-eui Yoon. "What You Ask Is What You Ground: Bridging Question Intent to Temporal Evidence for Grounded VideoQA". *ECCV 2026, Lecture Notes in Computer Science, 549-566 (2026)*.
- Suhyeon Ha, Woo Jae Kim, Joonsung Jeon, Sooel Son, Sung-eui Yoon. "APT: Anchor-aligned Perturbations for Tamper Localization in Fully Regenerated Images". *ECCV 2026, Lecture Notes in Computer Science, 373-389 (2026)*.
- Taeyeon Kim, Youngju Na, Jumin Lee, Sebin Lee, Minhyuk Sung, Sung-Eui Yoon. "MorphGS: Morphology-Adaptive Articulated 3D Motion Transfer from Videos". *ECCV 2026, Lecture Notes in Computer Science, 210-229 (2026)*.
- Woo Jae Kim, Kyle Min, Suhyeon Ha, Joonsung Jeon, Sung-eui Yoon. "RoME: Robust Mixture of Low-Rank Experts Against Multiple Adversarial Perturbations". *ECCV 2026, Lecture Notes in Computer Science, 152-171 (2026)*.
- Jeremy C.H. Ong, Minsung Yoon, Hee Chan Shin, Sung Eui Yoon, Mohd Zulhilmi Ismadi, Xin Wang. "Metaheuristic asphalt crack sealing path planning based on discrete grey wolf optimiser". *International Journal of Hydromechatronics 9, 57-90 (2026)*.

**2025**

- Heechan Shin, Minsung Yoon, Jeil Jeong, Sung-eui Yoon. "Robust Pedipulation on Quadruped Robots via Gravitational-moment Minimization". *International Journal of Control, Automation and Systems 23, 3525-3535 (2025)*.
- Jinhwan Seo, Yoonki Cho, Junhyug Noh, Sung-Eui Yoon. "Pinpointing Trigger Moment for Grounded Video QA: Enhancing Spatio-temporal Grounding in Multimodal Large Language Models". *arXiv:2511.02182 (사전 공개본, 2025; arXiv 저자 메모 「1st place winner of Grounded Videoqa track at the ICCV2025 Perception Test」)*.
- Woo Jae Kim, Kyu Beom Han, Yoonki Cho, Youngju Na, Junsik Jung, Sooel Son, Sung-Eui Yoon. "AegisRF: Adversarial Perturbations Guided with Sensitivity for Protecting Intellectual Property of Neural Radiance Fields". *arXiv:2510.19371 (사전 공개본, 2025; arXiv 저자 메모 「BMVC 2025」)*.
- Woojung Son, Yoonki Cho, Guoyuan An, Chanmi Lee, Sung-Eui Yoon. "Towards Robustness of Person Search Against Corruptions". *2025 IEEE/CVF International Conference on Computer Vision (ICCV), 23408-23418 (2025)*.
- Taegeun Yang, Jiwoo Hwang, Jeil Jeong, Minsung Yoon, Sung-Eui Yoon. "Efficient Navigation Among Movable Obstacles using a Mobile Manipulator via Hierarchical Policy Learning". *2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 17130-17137 (2025)*.
- Jaeyoon Kim, Yoonki Cho, Taeyoung Kim, Sung-Eui Yoon. "Enhancing Visual Re-Ranking Through Denoising Nearest Neighbor Graph via Continuous CRF". *2025 IEEE International Conference on Image Processing (ICIP), 55-60 (2025)*.
- Youngju Na, Taeyeon Kim, Jumin Lee, Kyu Beom Han, Woo Jae Kim, Sung-Eui Yoon. "Pose-Free 3D Gaussian Splatting via Shape-Ray Estimation". *2025 IEEE International Conference on Image Processing (ICIP), 2348-2353 (2025)*.
- Minsung Yoon, Sung-Eui Yoon. "Enhancing Navigation Efficiency of Quadruped Robots via Leveraging Personal Transportation Platforms". *2025 IEEE International Conference on Robotics and Automation (ICRA), 11184-11190 (2025)*.
- Yin Xu, Min-Sung Yoon, Yuchi Huo, Kang Zhang, Sung-Eui Yoon. "LangPert: Detecting and Handling Task-level Perturbations for Robust Object Rearrangement". *arXiv:2504.09893 (사전 공개본, 2025)*.
- Joonsung Jeon, Woo Jae Kim, Suhyeon Ha, Sooel Son, Sung-Eui Yoon. "AdvPaint: Protecting Images from Inpainting Manipulation via Adversarial Attention Disruption". *arXiv:2503.10081 (사전 공개본, 2025; arXiv 저자 메모 「Accepted to ICLR 2025」)*.
- Xu Yin, Fei Pan, Guoyuan An, Yuchi Huo, Zixuan Xie, Sung-Eui Yoon. "OpenSlot: Mixed Open-Set Recognition With Object-Centric Learning". *IEEE Transactions on Multimedia 27, 6019-6030 (2025)*.

**2024**

- Minh-Tuan Tran, Xuan-May Le, Van-Nam Huynh, Sung-Eui Yoon. "PISD: A linear complexity distance beats dynamic time warping on time series classification and clustering". *Engineering Applications of Artificial Intelligence 138, 109222 (2024)*.
- Xu Yin, Woobin Im, Dongbo Min, Yuchi Huo, Fei Pan, Sung-Eui Yoon. "Fine-Grained Background Representation for Weakly Supervised Semantic Segmentation". *IEEE Transactions on Circuits and Systems for Video Technology 34, 11739-11750 (2024)*.
- Juhyeong Seon, Woobin Im, Sebin Lee, Jumin Lee, Sung-Eui Yoon. "Extending Segment Anything Model into Auditory and Temporal Dimensions for Audio-Visual Segmentation". *2024 IEEE International Conference on Image Processing (ICIP), 2480-2486 (2024)*.
- SeongJoo Moon, Sebin Lee, Dong He, Sung-Eui Yoon. "LiDAR-camera Online Calibration by Representing Local Feature and Global Spatial Context". *2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 9447-9454 (2024)*.
- Minsung Yoon, Heechan Shin, Jeil Jeong, Sung-Eui Yoon. "Learning-based Adaptive Control of Quadruped Robots for Active Stabilization on Moving Platforms". *2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 701-708 (2024)*.
- Woobin Im, Geonho Cha, Sebin Lee, Jumin Lee, Juhyeong Seon, Dongyoon Wee, Sung-Eui Yoon. "Regularizing Dynamic Radiance Fields with Kinematic Fields". *ECCV 2024, Lecture Notes in Computer Science, 312-328 (2024)*.
- Pei Wang, Yu Zhu, Danna Xue, Qingsen Yan, Jinqiu Sun, Sung-eui Yoon, Yanning Zhang. "Take a prior from other tasks for severe blur removal". *Computer Vision and Image Understanding 245, 104027 (2024)*.
- Jeongmin Gu, Jonghee Back, Sung-Eui Yoon, Bochang Moon. "Target-Aware Image Denoising for Inverse Monte Carlo Rendering". *ACM Transactions on Graphics 43, 1-11 (2024)*.
- Fei Pan, Xu Yin, Seokju Lee, Axi Niu, Sungeui Yoon, In So Kweon. "MoDA: Leveraging Motion Priors from Videos for Advancing Unsupervised Domain Adaptation in Semantic Segmentation". *2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW), 2649-2658 (2024)*.
- Guoyuan An, Yuchi Huo, Sung-Eui Yoon. "Accurate and Fast Pixel Retrieval with Spatial and Uncertainty Aware Hypergraph Diffusion". *arXiv:2406.11242 (사전 공개본, 2024)*.
- Youngju Na, Woo Jae Kim, Kyu Beom Han, Suhyeon Ha, Sung-Eui Yoon. "UFORecon: Generalizable Sparse-View Surface Reconstruction from Arbitrary and Unfavorable Sets". *2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 5094-5104 (2024)*.
- Jumin Lee, Sebin Lee, Changho Jo, Woobin Im, Juhyeong Seon, Sung-Eui Yoon. "SemCity: Semantic Scene Generation with Triplane Diffusion". *2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 28337-28347 (2024)*.
- Minsung Yoon, Taegeun Yang, Chanmi Lee, Hyunsik Son, Sung-Eui Yoon. "Analysis of Terrain-Aware Optimal Path Planning Methods for Stable Off-Road Navigation". *2024 IEEE Intelligent Vehicle Symposium (IV), 206-210 (2024)*.
- Mincheul Kim, Youngsun Kwon, Sebin Lee, Sung-eui Yoon. "CCTV-Informed Human-Aware Robot Navigation in Crowded Indoor Environments". *IEEE Robotics and Automation Letters 9, 5767-5774 (2024)*.
- Inkyu An, Guoyuan An, Taeyoung Kim, Sung-eui Yoon. "Microphone Pair Training for Robust Sound Source Localization With Diverse Array Configurations". *IEEE Robotics and Automation Letters 9, 319-326 (2024)*.
- Jaeyoon Kim, Yoonki Cho, Taeyong Kim, Sung-eui Yoon. "Denoising Nearest Neighbor Graph Via Continuous CRF for Visual Instance Retrieval". *SSRN 원고 (사전 공개본, 2024)*.
- Yoonki Cho, Jaeyoon Kim, Woo Kim, Junsik Jung, Sung-Eui Yoon. "Generalizable Person Re-identification via Balancing Alignment and Uniformity". *Advances in Neural Information Processing Systems 37, 47069-47093 (2024)*.

**2023**

- Sebin Lee, Woobin Im, Sung-Eui Yoon. "Multi-resolution distillation for self-supervised monocular depth estimation". *Pattern Recognition Letters 176, 215-222 (2023)*.
- Juhyeong Seon, Jaeyoon Kim, Joo-Young Kim, Young-Joo Lee, Hyekyung Han, Sung-Eui Yoon. "Class-Aware Contrastive Learning for Improving Performance of Sound Source Localization Model in Videos". *KIISE Transactions on Computing Practices 29, 518-524 (2023)*.
- Guoyuan An, Woo Jae Kim, Saelyne Yang, Rong Li, Yuchi Huo, Sung-Eui Yoon. "Towards Content-based Pixel Retrieval in Revisited Oxford and Paris". *2023 IEEE/CVF International Conference on Computer Vision (ICCV), 20450-20461 (2023)*.
- Inwoo Ha, Hyun Sung Chang, Minjung Son, Sung-eui Yoon. "Learning to disentangle latent physical factors of deformable faces". *The Visual Computer 39, 3481-3494 (2023)*.
- Woo Jae Kim, Yoonki Cho, Junsik Jung, Sung-Eui Yoon. "Feature Separation and Recalibration for Adversarial Robustness". *2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 8183-8192 (2023)*.
- Mincheul Kang, Minsung Yoon, Sung-Eui Yoon. "Towards Safe Remote Manipulation: User Command Adjustment based on Risk Prediction for Dynamic Obstacles". *2023 IEEE International Conference on Robotics and Automation (ICRA), 11994-12000 (2023)*.
- Minsung Yoon, Mincheul Kang, Daehyung Park, Sung-Eui Yoon. "Learning-based Initialization of Trajectory Optimization for Path-following Problems of Redundant Manipulators". *2023 IEEE International Conference on Robotics and Automation (ICRA), 9686-9692 (2023)*.
- Kyu Beom Han, Olivia G. Odenthal, Woo Jae Kim, Sung-Eui Yoon. "Pixel-wise Guidance for Utilizing Auxiliary Features in Monte Carlo Denoising". *Proceedings of the ACM on Computer Graphics and Interactive Techniques 6, 1-19 (2023)*.
- Yuchi Huo, Hujun Bao, Yifan Peng, Chen Gao, Wei Hua, Qing Yang, Haifeng Li, Rui Wang, Sung-Eui Yoon. "Optical neural network via loose neuron array and functional learning". *Nature Communications 14, 2535 (2023)*.
- Jumin Lee, Woobin Im, Sebin Lee, Sung-Eui Yoon. "Diffusion Probabilistic Models for Scene-Scale 3D Categorical Data". *arXiv:2301.00527 (사전 공개본, 2023)*.
- Xu Yin, Dongbo Min, Yuchi Huo, Sung-Eui Yoon. "Contour-Aware Equipotential Learning for Semantic Segmentation". *IEEE Transactions on Multimedia 25, 6146-6156 (2023)*.
- Guoyuan An, Ju-Hyeong Seon, Inkyu An, Yuchi Huo, Sung-Eui Yoon. "Topological RANSAC for instance verification and retrieval without fine-tuning". *Advances in Neural Information Processing Systems 36, 63835-63846 (2023)*.

**2022**

- Taeyoung Kim, Inkyu An, Sung-eui Yoon. "Inexpensive indoor acoustic material estimation for realistic sound propagation". *Computer Animation and Virtual Worlds 34, e2131 (2022)*.
- Jinwon Kim, Heechan Shin, Sung-Eui Yoon. "Collision-Backpropagation based Obstacle Avoidance Method for a Legged Robot Expressed as a Simplified Dynamics Model". *2022 22nd International Conference on Control, Automation and Systems (ICCAS), 328-332 (2022)*.
- Mincheul Kim, Youngsun Kwon, Sung-Eui Yoon. "Group Estimation for Social Robot Navigation in Crowded Environments". *2022 22nd International Conference on Control, Automation and Systems (ICCAS), 1421-1425 (2022)*.
- Woo Jae Kim, Seunghoon Hong, Sung-Eui Yoon. "Diverse Generative Perturbations on Attention Space for Transferable Adversarial Attacks". *2022 IEEE International Conference on Image Processing (ICIP), 281-285 (2022)*.
- Yoonki Cho, Woo Jae Kim, Seunghoon Hong, Sung-Eui Yoon. "Part-based Pseudo Label Refinement for Unsupervised Person Re-identification". *2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 7298-7308 (2022)*.
- Inkyu An, Youngsun Kwon, Sung-eui Yoon. "Diffraction- and Reflection-Aware Multiple Sound Source Localization". *IEEE Transactions on Robotics 38, 1925-1944 (2022)*.
- Kyuyeon Kim, Junsik Jung, Woo Jae Kim, Sung-Eui Yoon. "Deep Video Inpainting Guided by Audio-Visual Self-Supervision". *ICASSP 2022 - 2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 1970-1974 (2022)*.
- Youngsun Kwon, Minhyuk Sung, Sung-Eui Yoon. "Implicit LiDAR Network: LiDAR Super-Resolution via Interpolation Weight Prediction". *2022 IEEE International Conference on Robotics and Automation (ICRA), 8424-8430 (2022)*.
- Hyeongyeol Ryu, Minsung Yoon, Daehyung Park, Sung-Eui Yoon. "Confidence-Based Robot Navigation Under Sensor Occlusion with Deep Reinforcement Learning". *2022 IEEE International Conference on Robotics and Automation (ICRA), 8231-8237 (2022)*.
- Mincheul Kang, Sung-Eui Yoon. "Analysis and acceleration of TORM: optimization-based planning for path-wise inverse kinematics". *Autonomous Robots 46, 599-615 (2022)*.
- Mincheul Kang, Yoonki Cho, Sung-Eui Yoon. "RCIK: Real-Time Collision-Free Inverse Kinematics Using a Collision-Cost Prediction Network". *IEEE Robotics and Automation Letters 7, 610-617 (2022)*.
- Woobin Im, Sebin Lee, Sung-Eui Yoon. "Semi-supervised Learning of Optical Flow by Flow Supervisor". *ECCV 2022, Lecture Notes in Computer Science, 302-318 (2022)*.

**2021**

- Kyuyeon Kim, Sung-Eui Yoon. "Image-Bridged Multimodal Half-Supervised Learning". *KIISE Transactions on Computing Practices 27, 578-583 (2021)*.
- Guoyuan An, Yuchi Huo, Sung-Eui Yoon. "Hypergraph Propagation and Community Selection for Objects Retrieval". *Neural Information Processing Systems (2021)*.
- Moonyoung Lee, Youngsun Kwon, Sebin Lee, JongHun Choe, Junyong Park, Hyobin Jeong, Yujin Heo, Min-Su Kim, Jo Sungho, Sung-Eui Yoon, Jun-Ho Oh. "Dynamic Humanoid Locomotion Over Rough Terrain With Streamlined Perception-Control Pipeline". *2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 4111-4117 (2021)*.
- In-Young Cho, Yuchi Huo, Sung-Eui Yoon. "Weakly-supervised contrastive learning in path manifold for Monte Carlo image reconstruction". *ACM Transactions on Graphics 40, 1-14 (2021)*.
- Yuchi Huo, Sung-eui Yoon. "A survey on deep learning-based Monte Carlo denoising". *Computational Visual Media 7, 169-185 (2021)*.
- Jinwoo Park, Ik-Beom Jeon, Sung-Eui Yoon, Woontack Woo. "Instant Panoramic Texture Mapping with Semantic Object Matching for Large-Scale Urban Scene Reproduction". *IEEE Transactions on Visualization and Computer Graphics 27, 2746-2756 (2021)*.
- Guo Yuan An, Sung Eui Yoon, Jae Yoon Kim, Lin Wang, Myoung Ho Kim. "GraphShop: Graph-based Approach for Shop-type Recommendation". *Proceedings of the 2021 SIAM International Conference on Data Mining (SDM), 55-63 (2021)*.
- Hunmin Park, Yuchi Huo, Sung-Eui Yoon. "MeshChain: Secure 3D Model and Intellectual Property management Powered by Blockchain Technology". *Advances in Computer Graphics, Lecture Notes in Computer Science, 519-534 (2021)*.
- Changho Jo, Woobin Im, Sungeui Yoon. "In-N-Out: Towards Good Initialization for Inpainting and Outpainting". *British Machine Vision Conference 2021, 322 (2021)*.

목록의 「GLINT: Modeling Scene-Scale Transparency via Gaussian Radiance Transport」(arXiv 사전 공개본)는 전산학부 소식이 CVPR 2026의 구두 발표 논문이자 수상 후보(Award Candidate)로 적는 논문이고,[^glint] ICIP 2025 논문 「Pose-Free 3D Gaussian Splatting via Shape-Ray Estimation」은 ICIP 2025 최우수 학생논문상(Best Student Paper Award)을 받았다.[^icip]

## 과제

KAIST 전산학부 소식 게시판에 실린 과제다. 날짜는 소식 글의 게시일이다.

- 2026-03-23 · 정보통신기획평가원(IITP) 연구과제 선정: 물리 지능(Physical Intelligence) 기반 차세대 인공지능 연구. 공동연구자 김태균·성민혁·오태현 교수(전산학부)와 명현 교수(전기및전자공학부), 산업체 협력기관 홀리데이로보틱스[^iitp] (역할 윤성의 교수 연구책임자; 기간 3년; 연구비 연간 약 10억 원 규모)

## 수상

2021년 10월 13일부터 2026년 10월 13일까지 KAIST 전산학부 소식 게시판에 실린 연구실과 교수의 수상이다. 날짜는 소식 글의 게시일이고, 상 이름은 소식 글의 표기다.

- 2022-06-02 · ICRA 2022 Outstanding Navigation Award Finalist 선정: 「Confidence-Based Robot Navigation Under Sensor Occlusion with Deep Reinforcement Learning」(Hyeongyeol Ryu, Minsung Yoon, Daehyung Park, and Sung-Eui Yoon), 석사졸업생 유형열(지도교수 윤성의)의 석사논문[^icra22]
- 2022-07-26 · KCC2022 학부생 논문 경진대회 입상자 우수상(분야: 인공지능): 「배경이 이미지 유사도 학습에 미치는 영향 분석」(선주형·안국원·윤성의(KAIST))[^kcc22]
- 2023-06-29 · ICRA 2023 Outstanding Planning Paper Award 수상: 윤성의 교수 연구팀의 「리던던트 로봇 매니퓰레이터를 사용한 최적화 기반의 경로 추종 문제에 대한 학습 기반 초기화 기술」 연구[^icra23]
- 2023-12-21 · KCC2023 우수논문상 입상자(분야: 인공지능): 「도메인 일반화에서 스타일 매니폴드를 고려한 공분산 기반 스타일 증강기법」(손우정·조윤기·윤성의(한국과학기술원))[^kcc23]
- 2025-09-29 · ICIP 2025 최우수 학생논문상(Best Student Paper Award) 수상: 윤성의 교수 연구실 박사과정 나영주, 석사과정 김태연 학생, 수상 논문 「Pose-free 3D Gaussian Splatting via Shape-Ray Estimation」[^icip]
- 2025-12-01 · ICCV 2025 인지 테스트 대회 GVQA 트랙 1위: 윤성의 교수 연구팀이 이화여대 노준혁 교수 연구팀과 공동으로 개발한 CORTEX(Chain-of-Reasoning for Trigger Moment Extraction)[^cortex]
- 2025-12-11 · 윤성의 교수, 2025 ACM Distinguished Member(특훈회원) 선정[^acm]
- 2026-07-06 · CVPR 2026 수상 후보 논문(Award Candidate) 선정: 윤성의 교수 연구팀의 「GLINT: Modeling Scene-Scale Transparency via Gaussian Radiance Transport」(구두 발표 논문으로도 선정)[^glint]

## 소식

같은 기간 KAIST 전산학부 소식 게시판에 실린 연구실 연구 관련 글이다. 날짜는 게시일이다. 수상이나 과제 선정만을 알린 글은 위 수상·과제 절에 적었다.

- 2022-04-22 · 윤성의·조성호 교수 인터뷰: 로봇 카메라로 사람의 행동을 파악해 돕는 로봇 소셜 인터랙션 기술과 KT와의 서비스 로봇 연구[^kt]
- 2023-06-29 · 리던던트 로봇 매니퓰레이터를 사용한 최적화 기반의 경로 추종 문제에 대한 학습 기반 초기화 기술 개발(ICRA 2023 발표)[^icra23]
- 2025-11-10 · 사진 2∼3장으로 3차원 장면을 복원하는 기술 SHARE 개발(과학기술정보통신부 SW스타랩 사업 지원)[^share]
- 2026-09-22 · KAIST AGI 연구소 출범(9월 18일), 윤성의 교수 등 전산학부 교수 5명 참여[^agi]

## 연락과 위치

- 교수연구실: KAIST E3-1, 3432, 전화 3531(전산학부 교수 소개 표기)[^csprof]
- 연구실 사무실: E3-1 3443호, 전화 042-350-3531[^cslab]
- 주소: 34141 대전광역시 유성구 대학로 291 한국과학기술원(KAIST) 전산학부[^csprof]
[^csprof]: KAIST 전산학부 교수 소개(윤성의) <https://cs.kaist.ac.kr/people/view?idx=20&kind=faculty&menu=160> (직위, 연구분야, 전공, 학위, 웹사이트, 전화, 교수연구실, 소개문, 2026-10-25 열람)
[^cslist]: KAIST 전산학부 교수진 목록 <https://cs.kaist.ac.kr/people/faculty> (윤성의 항목, 2026-10-25 열람)
[^cslab]: KAIST 전산학부 연구실 소개(대용량 그래픽스, 비젼, 로보틱스 연구실) <https://cs.kaist.ac.kr/research/labView?sn=61&menu=64> (연구실 이름, 연구 소개, 대용량 모델 렌더링·로봇경로생성·컴퓨터 비전 칸, 웹사이트, 전화, 사무실, 2026-10-25 열람)
[^gst]: KAIST 안보과학기술대학원 교수 명단 4쪽 <https://gst.kaist.ac.kr/member/faculty/?page=4> (윤성의 항목의 소속학과, 연구분야, 세부 연구 분야, 연구실, 2026-10-25 열람)
[^acm]: KAIST 전산학부 소식 「윤성의 교수, 2025 ACM Distinguished Member 선정」(2025-12-11 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&bbs_sn=11697&menu=83> (2026-10-25 열람)
[^glint]: KAIST 전산학부 소식 「KAIST 윤성의 교수팀 ‘GLINT’, CVPR 2026 수상 후보 선정」(2026-07-06 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&bbs_sn=11867&menu=83> (2026-10-25 열람)
[^share]: KAIST 전산학부 소식 「사진 2∼3장만으로 고품질 3D 복원… KAIST, 새로운 영상 처리 기술 ＇SHARE＇ 개발」(2025-11-10 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&menu=83&bbs_sn=11646> (2026-10-25 열람)
[^icip]: KAIST 전산학부 소식 「KAIST 전산학부 나영주·김태연, ICIP 2025 최우수 학생논문상 수상」(2025-09-29 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&menu=83&bbs_sn=11583> (2026-10-25 열람)
[^cortex]: KAIST 전산학부 소식 「KAIST 전산학부, 영상 기반 AI 기술로 ICCV 2025 챌린지 1위」(2025-12-01 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&menu=83&bbs_sn=11685> (2026-10-25 열람)
[^icra23]: KAIST 전산학부 소식 「리던던트 로봇 매니퓰레이터를 사용한 최적화 기반의 경로 추종 문제에 대한 학습 기반 초기화 기술 개발」(2023-06-29 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&menu=83&bbs_sn=10778> (2026-10-25 열람)
[^icra22]: KAIST 전산학부 소식 「ICRA 2022 졸업생 유형열(지도교수 윤성의) 석사논문 발표」(2022-06-02 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&menu=83&bbs_sn=10291> (2026-10-25 열람)
[^kt]: KAIST 전산학부 소식 「AI로 사람 감정 읽는 서비스로봇 만든다」(2022-04-22 게시, 윤성의·조성호 교수 인터뷰) <https://cs.kaist.ac.kr/board/view?bbs_id=news&menu=83&bbs_sn=10205> (2026-10-25 열람)
[^kcc22]: KAIST 전산학부 소식 「KCC2022 수상」(2022-07-26 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&menu=83&bbs_sn=10366> (2026-10-25 열람)
[^kcc23]: KAIST 전산학부 소식 「KCC 2023 수상자 명단 안내」(2023-12-21 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&menu=83&bbs_sn=10970> (2026-10-25 열람)
[^iitp]: KAIST 전산학부 소식 「[연구과제 선정] 물리 지능 기반 차세대 AI 연구 수행」(2026-03-23 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&menu=83&bbs_sn=11778> (2026-10-25 열람)
[^agi]: KAIST 전산학부 소식 「김태균 교수, KAIST AGI 연구소 초대 소장…전산학부 교수 5명 참여」(2026-09-22 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&menu=83&bbs_sn=11905> (2026-10-25 열람)
[^al-moon]: KAIST 전산학부 소식 「문보창 박사 광주과기원(GIST) 조교수 임용」(2016-09-06 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&menu=83&bbs_sn=7237> (2026-10-25 열람)
[^al-heo]: KAIST 전산학부 소식 「전산학부 허재필 박사 성균관대 조교수 임용」(2017-03-06 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&menu=83&bbs_sn=7460> (2026-10-25 열람)
[^al-kim1]: KAIST 전산학부 소식 「김덕수 박사 한국기술교육대 (KOREATEC) 조교수로 임용」(2018-04-16 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&menu=83&bbs_sn=8183> (2026-10-25 열람)
[^al-kim2]: KAIST 전산학부 소식 「CUDA 기반 GPU 병렬 처리 프로그래밍 저서 발간」(2023-09-20 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&menu=83&bbs_sn=10859> (2026-10-25 열람)
[^al-lee]: KAIST 전산학부 소식 「의료 인공지능(AI) 기업 루닛 코스닥 상장」(2022-07-22 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&menu=83&bbs_sn=10359> (2026-10-25 열람)
[^al-ahn]: KAIST 전산학부 소식 「안인규 박사, 국민대 소프트웨어융합학과 조교수 임용」(2025-03-10 게시) <https://cs.kaist.ac.kr/board/view?bbs_id=news&menu=83&bbs_sn=11394> (2026-10-25 열람)
[^pubs]: 교수의 2021–2026년 공개 서지: Crossref 서지 기록(교수 ORCID 0000-0002-7123-1119가 붙은 기록과 교수 이름 검색 기록) <https://api.crossref.org/>, OpenAlex 저자 기록 <https://api.openalex.org/>, arXiv 논문 페이지 <https://arxiv.org/> (2026-10-25 확인)
[^p1]: K. B. Han, O. G. Odenthal, W. J. Kim, S.-E. Yoon, Proceedings of the ACM on Computer Graphics and Interactive Techniques 6, 1-19 (온라인 2023-05-16). <https://doi.org/10.1145/3585505> 초록 기준.
[^p2]: Y. Na 외, S.-E. Yoon, 2025 IEEE International Conference on Image Processing (ICIP), 2348-2353 (2025). <https://doi.org/10.1109/icip55913.2025.11084718> 초록 기준(OpenAlex 등록 초록).
[^p3]: M. Yoon, M. Kang, D. Park, S.-E. Yoon, 2023 IEEE International Conference on Robotics and Automation (ICRA), 9686-9692 (2023). <https://doi.org/10.1109/icra48891.2023.10161426> 초록 기준(OpenAlex 등록 초록).
[^p4]: J. Jeong 외, S.-E. Yoon, IEEE Robotics and Automation Letters 11, 7980-7987 (2026). <https://doi.org/10.1109/lra.2026.3692054> 초록 기준(OpenAlex 등록 초록).
[^p5]: G. An 외, S.-E. Yoon, Advances in Neural Information Processing Systems 36, 63835-63846 (2023). <https://doi.org/10.52202/075280-2788> 초록 기준(OpenAlex 등록 초록).
[^p6]: J. Kim, Y. Cho, S.-E. Yoon, IEEE Robotics and Automation Letters 11, 4881-4888 (2026). <https://doi.org/10.1109/lra.2026.3669068> 초록 기준(OpenAlex 등록 초록).
[^p7]: W. J. Kim, Y. Cho, J. Jung, S.-E. Yoon, 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 8183-8192 (2023). <https://doi.org/10.1109/cvpr52729.2023.00791> 초록 기준(OpenAlex 등록 초록).
[^p8]: J. Jeon 외, S.-E. Yoon, arXiv:2503.10081 (사전 공개본, 2025-03-13 공개, arXiv 저자 메모 「Accepted to ICLR 2025」). <https://doi.org/10.48550/arxiv.2503.10081> 초록 기준(arXiv 판).

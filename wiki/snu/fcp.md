# Robotics Laboratory

**서울대학교 공과대학 기계공학부 · 박종우 교수**

- 영문 교수명: Frank Chongwoo Park
- 분야: 로봇의 모델링·식별·제어, 물체 파지·조작과 동작 계획, 로봇 학습, 수학적 데이터 과학[^home][^faculty]
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 로봇 조작·파지[^home][^p1][^p2], 컴퓨터 비전[^faculty][^p1][^p2], 3차원 복원·인식[^p1][^p2]
- 홈페이지: <https://sites.google.com/robotics.snu.ac.kr/fcp/>
- 근거와 출처: [Robotics Laboratory 근거 페이지](fcp-sources.md)

> 로봇이 물체를 알아보고 잡고 움직이는 방법을 연구하며, 실제 로봇의 물리적 성질과 자료에서 배우는 방법을 수학으로 연결하는 연구실이다.[^home][^p1][^p5][^p6]

## 무엇을 연구하나

서울대학교 기계공학부의 박종우 교수가 이끄는 연구실이다. 연구실은 현재 연구를 로봇의 모델링(대상의 성질과 변화를 수학으로 나타내는 일)·식별(관측 자료에서 모형이나 모형의 값을 구하는 일)·제어(시스템이 원하는 상태가 되도록 입력을 정하는 일), 물체를 잡고 다루는 일과 동작 계획(목표와 주변 제약에 맞게 움직일 경로와 자세를 정하는 일), 로봇 학습, 기계학습(자료에서 규칙을 배워 예측이나 판단을 수행하는 계산 방법)과 수학적 데이터 과학으로 소개한다.[^home][^faculty]

물체를 잡는 연구에서는 일부가 가려진 물체의 전체 모양을 알아내는 일과 로봇 손이 그 물체를 잡는 일을 함께 다룬다. 대표 논문 1은 적은 수의 부분 영상에서 장면의 보이지 않는 부분을 추정해 입체 모양을 복원하고 물체들을 구분한다. 학습한 자료를 바탕으로 새 영상을 만드는 생성 모형을 활용하며, 복원 결과를 물체 정리와 목표 물체 꺼내기에 연결했다. 대표 논문 2는 관측된 물체 표면의 점들에서 전체 모양을 추정하고, 로봇 손의 구조와 움직일 수 있는 범위를 고려해 잡는 자세를 정한다.[^p1][^p2]

동작을 만드는 연구는 과제에 맞는 움직임을 생성하는 방법과 충돌을 피하기 위해 거리를 계산하는 방법으로 이어진다. 대표 논문 3은 언어 등으로 주어진 과제 조건과 움직임 사이의 복잡한 관계를 다루기 위해, 여러 동작에 공통된 표현을 배우는 과정과 과제별 동작의 분포(가능한 값이나 상태의 범위에 발생 확률을 대응시킨 관계)를 배우는 과정을 분리했다. 대표 논문 4는 여러 팔을 가진 로봇의 충돌 거리를 학습하면서, 학습 자료 수를 고정한 채 충돌이 일어나는 경계 근처의 자료 비중을 늘리는 방법을 제안했다.[^p3][^p4]

로봇의 물리적 성질을 반영하는 모형과 자료의 수학적 구조도 연구한다. 대표 논문 5는 로봇 팔의 연결된 부품인 링크의 실제 모양이 모형에 반영되도록 하여, 로봇 형태와 움직임을 함께 설계한다. 대표 논문 6은 자료에서 로봇 모형을 얻는 연구를 물리 지식과 기하적 구조(점 사이의 거리와 각도, 공간의 형태에 관한 관계)라는 관점에서 정리한 리뷰다. 데이터 학습에서는 대표 논문 7이 자료를 단계적으로 바꾸어 새 표본(확률 분포에서 뽑은 값이나 값의 묶음)을 만드는 확산 모형과, 자료마다 값을 부여해 그럴듯함을 나타내는 에너지 기반 모형을 함께 학습한다. 대표 논문 8은 자료를 압축했다가 복원하는 오토인코더가 자료 사이 관계의 기하를 보존하도록 학습하는 방법을 제안했다.[^p5][^p6][^p7][^p8]

## 주요 연구 주제

### 물체 인식과 파지

파지는 로봇 손 등으로 물체를 잡는 일이다. 일부만 관측한 물체의 입체 모양을 복원하고, 가려진 장면에서도 물체를 구분하며 잡는 자세를 계산하는 연구를 한다. 물체를 알아보는 계산을 실제 정리·꺼내기 작업과 연결한다.[^home][^p1][^p2]

### 동작 생성과 충돌 거리

과제 조건에 따라 여러 움직임을 생성하는 방법과, 관절이 많은 로봇의 동작 계획에 필요한 충돌 거리를 학습하는 방법을 다룬다.[^home][^p3][^p4]

### 물리적 일관성이 있는 로봇 모델

로봇 부품의 실제 형태가 모형의 물리적 값과 맞도록 표현하고, 이를 형태 설계와 동작 설계에 함께 사용한다. 자료에서 로봇 모형을 구하는 문제를 다룰 때도 물리 지식을 포함하는 접근을 검토한다.[^p5][^p6]

### 수학적 데이터 학습

확산 모형의 표본 생성과 에너지 기반 모형의 학습을 함께 설계하고, 자료 사이 관계를 보존하는 압축 표현을 연구한다. 대표 논문 8은 자료를 점으로, 점 사이의 유사성을 선으로 표현한 그래프에서 얻은 구조를 압축 표현에 반영한다.[^faculty][^p7][^p8]

## 대표 논문

서울대 재직 시기의 2021–2026년 논문에서 연구 갈래를 나누어 8편을 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. 주요 저자는 전체 저자 명단의 순서로 표시했다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Zero-Shot Scene Geometry Recognition From Sparse Partial-View Images: Leveraging Generative Diffusion Models for Robotic Manipulation Tasks](https://doi.org/10.1109/lra.2026.3732999) · IEEE Robotics and Automation Letters | 적은 수의 부분 영상에서 보이지 않는 장면을 추정하는 DreamGrasp를 제안했다. 입체 복원, 물체별 구분, 글로 지시하는 물체별 수정을 결합했다. 복원 결과로 물체를 차례로 정리하고 목표 물체를 꺼내는 작업도 수행했다.[^p1] | 1저자 Young Hun Kim, 마지막 저자 Frank C. Park |
| 2 | 2022 | [DSQNet: A Deformable Model-Based Supervised Learning Algorithm for Grasping Unknown Occluded Objects](https://doi.org/10.1109/tase.2022.3184873) · IEEE Transactions on Automation Science and Engineering | 일부가 가려진 물체의 표면 자료에서 전체 모양을 알아낸 뒤, 로봇 손의 구조와 움직임을 고려해 잡는 방법을 제안했다. 모양을 변형할 수 있는 기본 도형과 학습 방법을 결합했다. 생활 물체 실험에서 평균 파지 성공률은 93%였고 비교 방법은 86%였다.[^p2] | 1저자 Seungyeon Kim, 마지막 저자 Frank C. Park |
| 3 | 2025 | [Motion Manifold Flow Primitives for Task-Conditioned Trajectory Generation Under Complex Task-Motion Dependencies](https://doi.org/10.1109/lra.2025.3575313) · IEEE Robotics and Automation Letters | 과제 조건이 달라질 때 움직임의 분포가 크게 바뀌는 문제를 다뤘다. 움직임의 압축 표현을 배우는 과정과 과제 조건별 분포를 배우는 과정을 나누고, 압축된 좌표 공간에서 생성 모형으로 동작 분포를 학습했다. 언어로 지시한 동작 생성 과제로 평가했다.[^p3] | 1저자 Yonghyeon Lee, 마지막 저자 Frank C. Park |
| 4 | 2024 | [Active learning of the collision distance function for high-DOF multi-arm robot systems](https://doi.org/10.1017/s0263574723001790) · Robotica | 여러 팔을 가진 로봇의 충돌 거리를 배우는 새 방법을 제안했다. 학습 자료 수를 고정한 채 학습이 진행될수록 충돌 경계 부근의 자료를 늘리고, 각 링크의 공간적 배치를 표현하는 공간에서 거리를 계산했다. 여러 팔 로봇으로 기존 학습 방법과 성능을 비교했다.[^p4] | 1저자 Jihwan Kim, 마지막 저자 Frank C. Park |
| 5 | 2022 | [Physically Consistent Lie Group Mesh Models for Robot Design and Motion Co-Optimization](https://doi.org/10.1109/lra.2022.3189806) · IEEE Robotics and Automation Letters | 로봇의 형태와 동작을 함께 설계할 때, 모형의 물리적 값이 실제 링크 모양과 맞지 않으면 큰 오차가 생길 수 있음을 확인했다. 다양한 링크 모양을 표현하고 모양 변화의 미분값을 직접 구할 수 있는 모형을 제안했다. 미분은 어떤 양의 변화에 따른 다른 양의 순간적인 변화율을 구하는 연산이다. 수치 실험과 인쇄 제작한 로봇으로 방법을 검증했다.[^p5] | 1저자 Jaewoon Kwon, 마지막 저자 Frank C. Park |
| 6 | 2023 | [Robot Model Identification and Learning: A Modern Perspective](https://doi.org/10.1146/annurev-control-061523-102310) · Annual Review of Control, Robotics, and Autonomous Systems | 자료에서 로봇 모형을 얻는 연구를 하나의 관점으로 정리한 리뷰다. 식별 문제의 기하적 구조와 물리 지식을 활용한 최근 진전을 중심으로, 전통적인 결과와 최근의 모형 학습 연구를 연결해 설명한다.[^p6] | 1저자 Taeyoon Lee, 마지막 저자 Frank C. Park |
| 7 | 2024 | [Maximum Entropy Inverse Reinforcement Learning of Diffusion Models with Energy-Based Models](https://doi.org/10.52202/079017-0776) · Conference on Neural Information Processing Systems | 확산 모형과 에너지 기반 모형을 함께 학습해 생성 표본의 품질을 높이는 방법을 제안했다. 자료에서 학습한 확률의 값을 바탕으로 확산 모형을 학습하고, 두 모형이 자료의 분포에 도달하도록 학습 문제를 구성했다. 적은 생성 단계에서도 표본을 만들 수 있음을 보였고 이상 탐지 성능도 개선했다.[^p7] | 1저자 Sangwoong Yoon, 마지막 저자 Frank C. Park |
| 8 | 2024 | [Graph Geometry-Preserving Autoencoders](https://sites.google.com/robotics.snu.ac.kr/fcp/publications/articles/abstract/2024/2024_graph_geometry-preserving_autoencoders) · International Conference on Machine Learning | 자료 사이 유사성을 나타내는 그래프가 자료의 구조를 담는다는 관점에서 오토인코더 학습 방법을 제안했다. 그래프에서 얻은 기하적 구조가 압축 표현에도 보존되도록 학습 조건을 추가했다. 실험에서 그래프 구조를 보존하는 표현과 압축된 공간에서의 동역학 학습에 효과를 보였다. 동역학은 힘과 운동의 관계를 다루는 분야다.[^p8] | 1저자 Jungbin Lim, 마지막 저자 Frank C. Park |

## 교수와 전문 분야

박종우 교수는 미국 MIT에서 1985년 전기·컴퓨터과학 학사를, Harvard University에서 1991년 응용수학 박사를 받았다. 1991–1994년 University of California, Irvine의 기계항공공학과 조교수를 거쳐 1995년부터 서울대학교 기계공학부 교수로 재직하고 있다. 학과 경력은 2017년부터 「(주) Saige Research 대표」, 2022년부터 서울대학교 데이터사이언스대학원 부원장으로 적는다.[^dept]

연구 관심은 로봇 역학·계획·제어, 수학적 시스템 이론, 기계학습과 수학적 데이터 과학, 컴퓨터 비전과 관련 응용수학이다. 컴퓨터 비전은 영상에서 물체와 장면의 정보를 알아내는 계산 기술이다. IEEE 석학회원이며 IEEE Transactions on Robotics 편집장과 IEEE Robotics and Automation Society 회장을 역임했다. Kevin Lynch와 함께 쓴 교재 Modern Robotics: Mechanics, Planning, and Control은 2017년 출판되었으며, 연구실은 이 책을 바탕으로 한 Robot Mechanics and Control 강의도 소개한다.[^faculty][^books]

최근 논문은 물체를 알아보고 잡는 학습 방법, 동작 생성과 충돌 거리, 물리적 일관성이 있는 로봇 모형, 자료의 수학적 구조를 반영한 학습으로 전문 분야를 보여 준다.[^p1][^p3][^p5][^p8]

## 응용 분야

일부가 가려진 생활 물체의 인식과 파지, 물체가 섞여 있는 장면의 정리와 목표 물체 꺼내기, 언어로 조건을 주는 로봇 동작 생성, 여러 팔 로봇의 동작 계획, 로봇 형태와 움직임의 공동 설계에 연결된다.[^p1][^p2][^p3][^p4][^p5]

## 구성원

2026년 11월 8일 연구실 People과 Researchers의 게시 명단을 합친 교수 외 27명이다. 박사후연구원 1명, 박사과정 15명, 석사과정 11명이며, 과정은 누리집의 Candidate와 Post Doc Researcher 표기다. 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people][^researchers]

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Daniel Huczala | 박사후연구원 | daniel.huczala@robotics.snu.ac.kr |  |
| 김진규 (Jinkyu Kim) | 박사과정 | jkkim@robotics.snu.ac.kr |  |
| 홍영석 (Youngsuk Hong) | 박사과정 | yshong@robotics.snu.ac.kr |  |
| 김승현 (Seunghyeon Kim) | 박사과정 | ksh@robotics.snu.ac.kr |  |
| Sukho Yoon | 박사과정 |  |  |
| 박진혁 (Jinhyuk Park) | 박사과정 | jhpark@robotics.snu.ac.kr |  |
| Gyuhyun Park | 박사과정 |  |  |
| Keunjun Choi | 박사과정 |  |  |
| 박제상 (Che-Sang Park) | 박사과정 | cspark@robotics.snu.ac.kr |  |
| 임병도 (Byeongdo Lim) | 박사과정 | bdlim@robotics.snu.ac.kr |  |
| 김종민 (Jongmin Kim) | 박사과정 | jmkim@robotics.snu.ac.kr |  |
| 임중빈 (Jungbin Lim) | 박사과정 | jblim97@robotics.snu.ac.kr | 8 |
| 하준수 (Junsu Ha) | 박사과정 | hajunsu@robotics.snu.ac.kr |  |
| 황힘찬 (Himchan Hwang) | 박사과정 | himchan07@robotics.snu.ac.kr | 7 |
| 송지환 (Jihwan Song) | 박사과정 | jhsong@robotics.snu.ac.kr |  |
| 권세희 (Sehee Kwon) | 박사과정 | seram7@robotics.snu.ac.kr |  |
| 송민창 (Minchang Song) | 석사과정 | smc@robotics.snu.ac.kr |  |
| 류가은 (Gaeun Ryu) | 석사과정 | ryugaeun@robotics.snu.ac.kr |  |
| 정혁주 (Hyeokju Jeong) | 석사과정 | hjjeong@robotics.snu.ac.kr |  |
| 노성호 (Seongho Noh) | 석사과정 | seonghonoh@robotics.snu.ac.kr |  |
| 강동환 (Donghwan Kang) | 석사과정 | dhkang@robotics.snu.ac.kr |  |
| 김호빈 (Hobeen Kim) | 석사과정 | hobeenkim@robotics.snu.ac.kr |  |
| 이민우 (Minu Lee) | 석사과정 | lminu@robotics.snu.ac.kr |  |
| 이아청 (Acheong Lee) | 석사과정 | achung@robotics.snu.ac.kr |  |
| 이정호 (Jungho Lee) | 석사과정 | jhlee@robotics.snu.ac.kr |  |
| 김승윤 (Sungyoon Kim) | 석사과정 | sykim@robotics.snu.ac.kr |  |
| 차민호 (Cha Minho) | 석사과정 | mhcha@robotics.snu.ac.kr |  |

## 졸업생 진로

연구실 Alumni의 1997–2026년 학위·기간 표기 103명이다. 학위·과정과 진로는 게시 표기를 따른다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 박규현 (Gyuhyun Park) | Ph.D. (2026) |  |
| 윤석호 (Sukho Yoon) | Ph.D. (2026) |  |
| 최석진 (SeokJin Choi) | Ph.D. (2026) | Samsung Research |
| 김영훈 (Young Hun Kim) | Ph.D. (2026) | Samsung Electronics |
| 김지환 (Jihwan Kim) | Ph.D. (2025) | Samsung Research |
| 이병호 (Byeongho Lee) | Ph.D. (2025) | Samsung Electronics |
| 김승연 (Seungyeon Kim) | Ph.D. (2024) | Postdoctoral Researcher, Geometric Robot Learning Lab, KTH |
| 윤상웅 (Sangwoong Yoon) | Ph.D. (2023) | Assistant professor, Graduate School of AI, UNIST |
| 이용현 (Yonghyeon Lee) | Ph.D. (2023) | Postdoctoral Associate, Biomimetic Robotics Lab, MIT |
| 권재운 (Jaewoon Kwon) | Ph.D. (2022) | Contoro Robotics |
| 박규민 (Kyumin Park) | Ph.D. (2022) | Assistant professor, Intelligent Mechatronics Engineering, Sejong University |
| 홍성일 (Seongil Hong) | Ph.D. (2021) | Agency for Defense Development |
| 윤알찬 (Alchan Yun) | Ph.D. (2020) | Samsung Research |
| 장청재 (Cheongjae Jang) | Ph.D. (2019) | Research Assistant Professor, A.I. Institute, Hanyang University |
| 김우영 (Wooyoung Kim) | Ph.D. (2019) | Naver Labs |
| 이태윤 (Taeyoon Lee) | Ph.D. (2019) | Research Scientist, Robotics and AI Institute |
| 노영균 (Dr. Yungkyun Noh) | (2011-2018) | Associate Professor, Department of Computer Science, Hanyang University |
| 홍지수 (Jisoo Hong) | Ph.D. (2018) | Samsung Electronics |
| 강동훈 (Donghoon Kang) | Ph.D. (2018) | Senior Researcher, KIST |
| 안병철 (Byungchul An) | Ph.D. (2017) | Senior Engineer, Doosan Robotics |
| 정은석 (Eunsuk Chong) | Ph.D. (2016) | Senior Software Engineer, Zoox |
| 하준형 (Junhyoung Ha) | Ph.D. (2015) | Assistant Professor, Department of Mechanical Engineering, UNIST |
| 강혁 (Hyuk Kang) | Ph.D. (2015) | Samsung Electronics  : Managing Director (MD) |
| 고인영 (Inyoung Ko) | Ph.D. (2014) | Samsung Electronics |
| 한재영 (Jaeyoung Han) | Ph.D. (2013) | Telesecurity Sciences (USA) |
| 한민연 (Minyeon Han) | Ph.D. (2013) | Samsung Fire and Marine Insurance |
| 이소희 (Sohee Lee) | Ph.D. (2011) | Samsung Electronics |
| 권정현 (Junghyun Kwon) | Ph.D. (2008) | Samsung Electronics : VP / Head of Robot Intelligence Team |
| 임복만 (Bokman Lim) | Ph.D. (2008) | Robot Motion Group, Fundamental Technology Team, Mechatronics & Manufacturing Technology Center, Samsung Electronics |
| 이석 (Seok Lee) | Ph.D. (2007) | KoreaTech |
| 김중곤 (Junggon Kim) | Ph.D. (2007) | Jet Propulsion Laboratory, NASA (USA) |
| 전창묵 (Changmook Chun) | Ph.D. 2005, MS. 1999 | Telesecurity Sciences (USA) |
| 정주노 (Dr. Joono Cheong) | (2003) | Professor, Control & Instrumentation Engineering, Korea University Sejong Campus, Korea |
| 김진욱 (Jinwook Kim) | Ph.D. 2002, MS. 1997 | Media Research Center, Korea Inst. of Science and Technology |
| Dr. Katja Mombaur | (2001-2002) | Professor, Canada Excellence Research Chair in Human-Centred Robotics and Machine Intelligence, University of Waterloo |
| 김정윤 (Jungyun Kim) | Ph.D. (2001) | Professor, Department of Mechanical and Automotive Engineering, Catholic University of Daegu |
| Cornel Iurascu | Ph.D. (2000) | YP Lee Patent Attorneys |
| 정진 (Gene Chung) | MS. (2026) | Saige Research |
| 임유민 (Yumin Lim) | MS. (2025) | Dynamic Robotics System Lab |
| 이상빈 (Sangbin Lee) | MS. (2025) | Saige Research |
| 권세희 (Sehee Kweon) | MS. (2024) | Saige Research |
| 권혁준 (Hyeokjun Kwon) | MS. (2022) | Saige Research |
| 손민준 (Minjun Son) | MS. (2022) | Graduate Student, School of Dentistry, Seoul National University |
| 진영욱 (Eric Young-Uk Jin) | MS. (2021) | Samsung Mechatronics R&D center |
| 김석현 (Seokhyeon Kim) | MS. (2021) | Graduate Student, School of Dentistry, Seoul National University |
| 안태균 (Taegyun Ahn) | MS. (2021) | Saige Research |
| 최진원 (Jinwon Choi) | MS. (2020) | Kakao Enterprise |
| 김승현 (Seunghyun Kim) | MS. (2020) | Robotics Lab |
| 최현웅 (Hyunwoong Choi) | MS. (2020) | Samsung Mechatronics R&D center |
| 이동익 (Bryan Dongik Lee) | MS. (2020) | Saige Research |
| 백종혁 (Jonghyuk Baek) | MS. (2020) | Saige Research |
| 정성재 (Seongjae Jeong) | MS. (2020) | Saige Research |
| 박성균 (Seonggyun Park) | MS. (2019) |  |
| Pubest Detdee | MS. (2019) |  |
| 김병헌 (Byungheon Kim) | MS. (2019) | SNU School of Dentistry |
| 노수철 (Soocheol Noh) | MS. (2017) |  |
| 송지훈 (Jihoon Song) | MS. (2017) | Samsung Electronics |
| 최근준 (Keunjun Choi) | MS. (2016) | Naver Labs |
| 박규현 (Kyuhyun Park) | MS. (2014) | Agency for Defense Development |
| 이지은 (Jeeeun Lee) | MS. (2014) | PhD student, University of Texas at Austin |
| 서기범 (Kibum Suh) | MS. (2013) | LIGNex1 |
| 이정석 (Jeongseok Lee) | MS. (2013) |  |
| 김민규 (Minkyu Kim) | MS. (2012) | Amazon |
| 김동현 (Donghyun Kim) | MS. (2012) | University of Massachusetts Amherst (Dept. CS) |
| 서찬수 (Chansoo Suh) | MS. (2011) | EPFL |
| 유태근 (Taekeun You) | MS. (2010) | Medical school student at Yonsei University, College of Medicine |
| 강지연 (Jiyeon Kang) | MS. (2010) | SUNY Buffalo (Mechanical Eng) |
| 엄태웅 (Taewoon Um) | MS. (2010) | ART Lab |
| 최한철 (Hancheol Choi) | MS. (2009) | Instructor, Aerospace Engineering, Korea Airforce Academy |
| 김정동 (Jungdong Kim) | MS. (2008) | MS student, Yonsei Law School |
| 김아영 (Ayoung Kim) | MS. (2007) | Associate Professor, Department of Mechanical Engineering, Seoul National University |
| 최민석 (Minseok Choi) | MS. (2007) | PhD student, Applied Mathematics, Brown University |
| 윤용은 (Yongeun Yoon) | MS. (2007) | Agency for Defense Development |
| 연경수 (Kyungsu Yeon) | MS. (2007) |  |
| 박진균 (Jingyun Park) | MS. (2007) | Hyundai Heavy Industries |
| 최진혁 (Jinhyeok Choi) | MS. (2006) | Equipment Engineering Group(TSP), Samsung Electronics |
| 김순겸 (Soonkyum Kim) | MS. (2006) | PhD student, Mechanical Engineering and Applied Mechanics, University of Pennsylvania |
| 박주용 (Juyong Park) | MS. (2006) | Display & Image Processing Lab, Samsung Advanced Institute of Technology |
| 나성권 (Syungkwon Ra) | MS. (2005) | Intelligent Robotics Research Center, Korea Inst. of Science & Technology (KIST) |
| 김성재 (Sung Jae Kim ) | MS. (2004) | Samsung Electro-mechanics |
| 이수엽 (Sooyeup Lee) | MS. (2004) | Hyundai Motors |
| 조규상 (Kyoo Sang Jo) | MS. (2004) | Mechatronics Research Center, Samsung Electronics |
| 박병수 (Byoungsoo Park) | MS. (2003) | Mechatronics Research Center, Samsung Electronics |
| 최준혁 (Joonhyuk Choi) | MS. (2003) | Samsung Techwin |
| 유승준 (Seungjoon Yu) | MS. (2003) | Daewoo Electronics |
| 박우람 (Wooram Park) | MS. (2003) | Department of Mechanical Engineering, Johns Hopkins University (PhD Program) |
| 신용우 (Yongwoo Shin) | MS. (2002) | Strategic Planning group, Mechatronics & Manufacturing Technology Center, Samsung Electronics |
| 정유한 (Yuhan Jeong) | MS. (2002) | Intelligent Inspection Lab, Mechatronics & Manufacturing Technology Center, Samsung Electronics |
| 곽승웅 (Seungwoong Gwak) | MS. (2001) | Bain & Company |
| 한철우 (Chulwoo Han) | MS. (2001) | Capital Markets & Portfolio Research, Inc. |
| 여상훈 (Sanghoon Yeo) | MS. (2001) | Lecturer, University of Birmingham |
| 김형민 (Hyungmin Kim) | MS. (2001) | PhD student, Institute for Surgical Technology and Biomechanics, University of Bern |
| 백종현 (Jonghyun Baek) | MS. (2000) | Senior Research Engineer, Control Engineering Team, CARNES |
| 이성희 (Sunghee Lee) | MS. (2000) | PhD student, Computer Science, UCLA |
| 한찬희 (Chanhee Hahn) | MS. (2000) | Mechatronics Research Center, Samsung Electronics |
| 유정현 (Junghyun Yu) | MS. (2000) | Samsung Electronics |
| 염한준 (Hanjun Yeom) | MS. (2000) | Sena Technologies |
| 이용훈 (Younghoon Lee) | MS. (1999) | Industrial Technology Cooperation Division, Ministry of Commerce, Industry & Energy |
| 임산 (San Lim) | MS. (1999) | Robot Motion Group, Fundamental Technology Team, Mechatronics & Manufacturing Technology Center, Samsung Electronics |
| 강인규 (Ingyu Kang) | MS. (1998) | TmaxSoft, Inc. |
| 박창범 (Changbeom Park) | MS. (1998) | PhD student, Mechanical Engineering, University of Texas at Austin |
| 최지현 (Jihyeon Choi) | MS. (1997) | Hyundai Motors Research Center |
| 한민섭 (Min Sup Han) | BS. (2002) | PhD Student, Department of Industrial Engineering and Operations Research, Columbia University |

## 최근 논문 목록 (2021–2026)

연구실 Articles의 2021–2026년 구역에 실린 논문 35편이다. 연도는 누리집의 연도 구역이며, 제목·저자·발표처는 연구실 표기다. 연도 구역 아래에 게재 예정으로 적은 1편은 「게재 승인」으로 구분했다. 학회판의 상태 대신 누리집 발표처만 따르는 4편은 「연구실 기재」로 표시했다. 별표는 누리집의 저자 표시다.[^articles]

**2026**

- Kyungseo Park\*, Byeongdo Lim, Jungbin Lim, Minseok Choi, Frank C. Park. "Constraint-Decomposed Impedance Control from Generative Policy for Articulated Object Manipulation". Conference on Robot Learning (CoRL) 2026 (연구실 기재).
- Jongmin Kim\*, Junsu Ha\*, Che-Sang Park\*, Minchang Song, Hyeokju Jeong, Himchan Hwang, Jianlong Fu, Frank C. Park. "CompVLA: A Variable Compliance Vision-Language-Action Model for Contact-rich Manipulation". Conference on Robot Learning (CoRL) 2026 (연구실 기재).
- Jungho Lee\*, Yonghee Lee, Haeseong Lee, Frank C. Park, Jaeheung Park. "Stable Abduction-Adduction Estimation for Dexterous Hand Teleoperation via Orientation Conditioning". International Journal of Precision Engineering and Manufacturing (게재 승인, 누리집의 게재 예정 표기).
- Young Hun Kim\*, Seungyeon Kim, Yonghyeon Lee, Frank C. Park. "Zero-Shot Scene Geometry Recognition From Sparse Partial-View Images: Leveraging Generative Diffusion Models for Robotic Manipulation Tasks". DOI: <https://doi.org/10.1109/lra.2026.3732999>.
- Hesheng Wang, Michael Wang, Frank Park, Lijun Han, Huichan Zhao, XingXing Wang, Andra Keay, Shigeki Sugano, Yi Guo, Tamim Asfour, Yu Sun, Ken Goldberg. "“Humanoids will soon replace most human workers”: A debate". Science Roboics 2026. DOI: <https://doi.org/10.1126/scirobotics.aeh6422>.
- Nancy M. Amat, Seth Hutchinson, Animesh Garg, Aude Billard, Daniela Rus, Russ Tedrake, Frank Park, Ken Goldberg. "“Data will solve robotics and automation: True or false?”: A debate". Science Robotics 2026. DOI: <https://doi.org/10.1126/scirobotics.aea7897>.
- Himchan Hwang\*, Hyeokju Jeong\*, Dong Kyu Shin\*, Che-Sang Park, Sehee Kweon, Sangwoong Yoon, Frank C. Park. "Value Gradient Sampler: Learning Invariant Value Functions for Equivariant Diffusion Sampling". Conference on Artificial Intelligence and Statistics (AISTATS) 2026 (연구실 기재).

**2025**

- Byeongho Lee\*, Yonghyeon Lee\*, Junsu Ha\*, Frank C. Park. "Behavior-Controllable Stable Dynamics Models on Riemannian Configuration Manifolds". IEEE Transactions on Robotics (T-RO) 2025.
- Seungyeon Kim, Junsu Ha, Young Hun Kim, Yonghyeon Lee, Frank C. Park. "ScrewSplat: An End-to-End Method for Articulated Object Recognition". Conference on Robot Learning (CoRL) 2025 (연구실 기재).
- Yonghyeon Lee, Byeongho Lee, Seungyeon Kim, Frank C. Park. "Motion Manifold Flow Primitives for Task-Conditioned Trajectory Generation under Complex Task-Motion Dependencies". IEEE Robotics and Autonomation Letters (RA-L) 2025. DOI: <https://doi.org/10.1109/lra.2025.3575313>.
- Seokjin Choi\*, Yonghyeon Lee\*, Seungyeon Kim, Che-Sang Park, Himchan Hwang, Frank C. Park. "Diverse Policy Learning Via Random Obstacle Deployment for Zero-Shot Adaptation". IEEE Robotics and Autonomation Letters (RA-L) 2025. DOI: <https://doi.org/10.1109/lra.2025.3532162>.

**2024**

- Sangwoong Yoon, Himchan Hwang, Dohyun Kwon, Yung-Kyun Noh, Frank C. Park. "Maximum Entropy Inverse Reinforcement Learning of Diffusion Models with Energy-Based Models". Conference on Neural Information Processing Systems (NeurIPS) 2024 (Oral). DOI: <https://doi.org/10.52202/079017-0776>.
- Young Hun Kim\*, Seungyeon Kim\*, Yonghyeon Lee, Frank C Park. "T²SQNet: A Recognition Model for Manipulating Partially Observed Transparent Tableware Objects". Conference on Robot Learning (CoRL) 2024.
- Byeongdo Lim\*, Jongmin Kim\*, Jihwan Kim, Yonghyeon Lee, Frank C Park. "EquiGraspFlow: SE(3)-Equivariant 6-DoF Grasp Pose Generative Flows". Conference on Robot Learning (CoRL) 2024.
- Jungbin Lim\*, Jihwan Kim\*, Yonghyeon Lee, Cheongjae Jang, Frank C. Park. "Graph Geometry-Preserving Autoencoders". International Conference on Machine Learning (ICML) 2024.
- Taeyoon Lee, Jaewoon Kwon, Patrick M. Wensing, and Frank C. Park. "Robot Model Identification and Learning: A Modern Perspective". Annual Review of Control, Robotics, and Autonomous Systems 2024. DOI: <https://doi.org/10.1146/annurev-control-061523-102310>.
- Jihwan Kim, and Frank C. Park. "Active learning of the collision distance function for high-DOF multi-arm robot systems". Robotica 2024. DOI: <https://doi.org/10.1017/s0263574723001790>.

**2023**

- Sangwoong Yoon, Young-Uk Jin, Yung-Kyun Noh, and Frank C. Park. "Energy-Based Models for Anomaly Detection: A Manifold Diffusion Recovery Approach". Conference on Neural Information Processing Systems (NeurIPS) 2023. DOI: <https://doi.org/10.52202/075280-2152>.
- Sangwoong Yoon, Frank C. Park, Gunsu YUN, Iljung Kim, and Yung-Kyun Noh. "Variational Weighting for Kernel Density Ratios". Conference on Neural Information Processing Systems (NeurIPS) 2023. DOI: <https://doi.org/10.52202/075280-0222>.
- Frank C. Park. "Robotics and Automation Practice". IEEE Robotics & Automation Magazine (RAM) 2023.
- Seungyeon Kim\*, Young Hun Kim\*, Yonghyeon Lee, and Frank C. Park. "Leveraging 3D Reconstruction for Mechanical Search on Cluttered Shelves". Conference on Robot Learning (CoRL) 2023.
- Byeongho Lee\*, Yonghyeon Lee\*, Seungyeon Kim, MinJun Son, and Frank C. Park. "Equivariant Motion Manifold Primitives". Conference on Robot Learning (CoRL) 2023.
- Jihwan Kim and Frank C. Park. "PairwiseNet: Pairwise Collision Distance Learning for High-dof Robot Systems". Conference on Robot Learning (CoRL) 2023.
- Howon Jin, Sangwoong Yoon, Frank C. Park, and Kyung Hyun Ahn. "Data-driven constitutive model of complex fluids using recurrent neural networks". Rheologica Acta 2023. DOI: <https://doi.org/10.1007/s00397-023-01405-z>.
- Frank C. Park. "The Education of a Roboticist". IEEE Robotics & Automation Magazine (RAM) 2023.
- Cheongjae Jang, Yongheon Lee, Yung-Kyun Noh, and Frank C. Park. "Geometrically Regularized Autoencoders for Non-Euclidean Data". International Conference on Learning Representations (ICLR) 2023.

**2022**

- Seungyeon Kim, Byeongdo Lim, Yonghyeon Lee, and Frank C. Park. "SE(2)-Equivariant Pushing Dynamics Models for Tabletop Object Manipulations". Conference on Robot Learning (CoRL) 2022.
- Cheongjae Jang, Sungyoon Lee, Frank C. Park, and Yung-Kyun Noh. "Reparametrization-Invariant Sharpness Measure Based on Information Geometry". Advances in Neural Information Processing Systems (NeurIPS) 2022.
- Jaewoon Kwon, Seunghyun Kim and Frank C. Park. "Physically Consistent Lie Group Mesh Models for Robot Design and Motion Co-Optimization". IEEE Robotics and Autonomation Letters (RA-L) 2022. DOI: <https://doi.org/10.1109/lra.2022.3189806>.
- Yonghyeon Lee\*, Seungyeon Kim\*, Jinwon Choi, and Frank C. Park. "A Statistical Manifold Framework for Point Cloud Data". International Conference on Machine Learning (ICML) 2022.
- Seungyeon Kim\*, Taegyun Ahn\*, Yonghyeon Lee, Jihwan Kim, Michael Yu Wang, and Frank C. Park. "DSQNet: A Deformable Model-Based Supervised Learning Algorithm for Grasping Unknown Occluded Objects". IEEE Transactions on Automation Science and Engineering (T-ASE) 2022. DOI: <https://doi.org/10.1109/tase.2022.3184873>.
- Yonghyeon Lee, Sangwoong Yoon, Minjun Son, and Frank C. Park. "Regularized autoencoders for isometric representation learning". International Conference on Learning Representations (ICLR) 2022.

**2021**

- Youngsuk Hong, Ramy Rashad, Soocheol Noh, Taeyoon Lee, Stefano Stramigioli, and Frank C. Park. "A geometric formulation of multirotor aerial vehicle dynamics". Nonlinear Dynamics 2021. DOI: <https://doi.org/10.1007/s11071-021-07042-6>.
- Kyu Min Park, Younghyo Park, Sangwoong Yoon, and Frank C. Park. "Collision detection for robot manipulators using unsupervised anomaly detection algorithms". IEEE/ASME Transactions on Mechatronics (TMECH) 2021. DOI: <https://doi.org/10.1109/tmech.2021.3119057>.
- Yonghyeon Lee, Hyeokjun Kwon, and Frank C. Park. "Neighborhood reconstructing autoencoders". Advances in Neural Information Processing Systems (NeurIPS) 2021.

## 최근 저서

연구실 Books가 2021–2026년으로 적은 저서와 번역서 3권이다.[^books]

- Frank C. Park and Kyumin Park, Dynamics of Mechanical Systems: A Modern Introduction to Three-Dimensional Rigid Body Dynamics, Cambridge University Press, 2025.
- 케빈 M. 린치, 박종우 공저, 모던 로보틱스: 역학, 계획 및 제어, 에이콘, 2023.
- Kyumin Park and Frank C. Park, Collision Detection for Robot Manipulators: Methods and Algorithms, Springer, 2023.

## 연락과 위치

- 연구실: 서울특별시 관악구 관악로 1 서울대학교 302동 413호[^home][^dept]
- 연구실 전화·연락 이메일: 02-880-7149, dhkang@robotics.snu.ac.kr[^home]
- 교수 사무실: 서울대학교 301동 1408호[^faculty][^dept]
- 교수 이메일·전화: fcp@snu.ac.kr, 02-880-7133[^faculty]
- 팩스: 02-883-1513[^faculty]
[^home]: Robotics Laboratory, Home. <https://sites.google.com/robotics.snu.ac.kr/fcp/home> 관측일 2026-11-08.

[^faculty]: Robotics Laboratory, Faculty. <https://sites.google.com/robotics.snu.ac.kr/fcp/people/faculty> 관측일 2026-11-08.

[^people]: Robotics Laboratory, People. <https://sites.google.com/robotics.snu.ac.kr/fcp/people> 관측일 2026-11-08.

[^researchers]: Robotics Laboratory, Researchers. <https://sites.google.com/robotics.snu.ac.kr/fcp/people/researchers> 관측일 2026-11-08.

[^alumni]: Robotics Laboratory, Alumni. <https://sites.google.com/robotics.snu.ac.kr/fcp/people/alumni> 관측일 2026-11-08.

[^articles]: Robotics Laboratory, Articles. <https://sites.google.com/robotics.snu.ac.kr/fcp/publications/articles> 관측일 2026-11-08.

[^books]: Robotics Laboratory, Books. <https://sites.google.com/robotics.snu.ac.kr/fcp/publications/books> 관측일 2026-11-08.

[^dept]: 서울대학교 기계공학부, 박종우 교수 소개. <https://me.snu.ac.kr/snu__professor/%eb%b0%95%ec%a2%85%ec%9a%b0-park-frank-chongwoo/> 관측일 2026-11-08.

[^p1]: Y. H. Kim, S. Kim, Y. Lee, F. C. Park, IEEE Robotics and Automation Letters. <https://doi.org/10.1109/lra.2026.3732999> 초록 기준(OpenAlex 등록 초록). 출판일(OpenAlex publication_date) 2026-09-10. 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5009036246,publication_year:2021-2026> 관측일 2026-11-08.

[^p2]: S. Kim 외, F. C. Park, IEEE Transactions on Automation Science and Engineering. <https://doi.org/10.1109/tase.2022.3184873> 초록 기준(OpenAlex 등록 초록). 출판일(OpenAlex publication_date) 2022-06-21. 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5009036246,publication_year:2021-2026> 관측일 2026-11-08.

[^p3]: Y. Lee, B. Lee, S. Kim, F. C. Park, IEEE Robotics and Automation Letters. <https://doi.org/10.1109/lra.2025.3575313> 초록 기준(OpenAlex 등록 초록). 출판일(OpenAlex publication_date) 2025-05-30. 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5009036246,publication_year:2021-2026> 관측일 2026-11-08.

[^p4]: J. Kim, F. C. Park, Robotica. <https://doi.org/10.1017/s0263574723001790> 초록 기준(OpenAlex 등록 초록). 출판일(OpenAlex publication_date) 2024-01-12. 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5009036246,publication_year:2021-2026> 관측일 2026-11-08.

[^p5]: J. Kwon, S. Kim, F. C. Park, IEEE Robotics and Automation Letters. <https://doi.org/10.1109/lra.2022.3189806> 초록 기준(OpenAlex 등록 초록). 출판일(OpenAlex publication_date) 2022-07-11. 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5009036246,publication_year:2021-2026> 관측일 2026-11-08.

[^p6]: T. Lee, J. Kwon, P. M. Wensing, F. C. Park, Annual Review of Control Robotics and Autonomous Systems. <https://doi.org/10.1146/annurev-control-061523-102310> 초록 기준(OpenAlex 등록 초록). 출판일(OpenAlex publication_date) 2023-10-20. 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5009036246,publication_year:2021-2026> 관측일 2026-11-08.

[^p7]: S. Yoon 외, F. C. Park, neural information processing systems. <https://doi.org/10.52202/079017-0776> 초록 기준(OpenAlex 등록 초록). 출판 연도 2024. 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5009036246,publication_year:2021-2026> 관측일 2026-11-08.

[^p8]: J. Lim 외, F. C. Park, International Conference on Machine Learning (2024). <https://sites.google.com/robotics.snu.ac.kr/fcp/publications/articles/abstract/2024/2024_graph_geometry-preserving_autoencoders> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://sites.google.com/robotics.snu.ac.kr/fcp/publications/articles/abstract/2024/2024_graph_geometry-preserving_autoencoders> 관측일 2026-11-08.

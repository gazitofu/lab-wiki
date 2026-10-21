# 의사결정 뇌동역학 연구실 (Decision Brain Dynamics Laboratory)

**KAIST 뇌인지과학과 · 정재승 교수**

- 분야: 뇌 동역학(뇌파·fMRI의 시공간 패턴), 의사결정 신경과학(사회적 의사결정, 신경경제학, 자살 같은 손상된 의사결정, 신경건축학), 계산 신경정신의학, 커넥톰(뇌 연결망), 뇌-컴퓨터 인터페이스, 뇌를 본뜬 인공지능
- 대분야: 기초생명·생물물리, 컴퓨팅·AI
- 태그: 인지과학·의사결정[^research], 계산신경과학[^research][^p3], 신경 인터페이스·뇌-컴퓨터 인터페이스[^research][^p4], 뇌 모방 인공지능[^research]
- 홈페이지: <https://raphe.kaist.ac.kr/>
- 근거와 출처: [Decision Brain Dynamics Lab 근거 페이지](raphe-sources.md)

> 사람이 어떻게 결정을 내리고 다른 사람과 어울리는지, 그 과정이 정신질환에서 어떻게 달라지는지를 뇌의 움직임으로 이해하려는 뇌과학 연구실이다. 뇌파·뇌영상 분석과 수학적 모델, 인공지능을 함께 써서 정신질환 진단을 돕는 방법과 생각만으로 기계를 움직이는 뇌-컴퓨터 인터페이스도 연구한다.[^home][^goal][^research]

## 무엇을 연구하나

연구실은 의사결정과 사회 인지의 복잡한 뇌 기전, 그리고 신경정신질환에서 그것이 손상되는 과정을 이해하려 한다고 소개한다. 계산 신경과학과 신경 신호 분석을 결합해 여러 규모에서 뇌의 신경 기반을 설명하는 모델을 만들고, 신경정신질환을 더 잘 이해하고 진단하며, 뇌 기능과 인지의 수수께끼를 밝히는 데 기여하는 것을 목표로 둔다.[^home] 목표 페이지는 뇌전도(EEG), 구조·기능 자기공명영상, 확산 자기공명영상, PET 같은 여러 뇌 측정 방법을 유전학, 계산 모델, 인공지능과 결합하며, 연구가 의사결정·사회 인지·의식, 건강한 노화와 뇌 회복력·신경퇴행·신경정신질환 등에 걸친다고 적는다.[^goal]

연구 영역은 여섯 가지다.[^research] **뇌 동역학**에서는 뇌파 같은 신경 활동의 시공간 구조와 대규모 신경망의 진동·동기화를 분석하고 딥러닝으로 자료에서 모델을 찾는다. 대표 논문에서는 ABIDE(Autism Brain Imaging Data Exchange) 자료 849명의 휴지기 fMRI에 동적 모드 분해(반복되는 시공간 패턴을 찾는 자료 기반 방법)를 적용해, 뒤쪽 시각-두정-측두 영역 패턴의 진동 시점이 다르다는 것을 찾았다.[^p1]

**의사결정 신경과학**은 사회적 의사결정, 신경경제학, 자살 같은 해로운 행동으로 이어지는 손상된 의사결정, 그리고 환경과 건축이 사람의 행동·생각·감정에 주는 영향을 다루는 신경건축학을 포함한다.[^research] 대표 논문에서는 사람들이 어떤 경우에 제3자의 소문을 퍼뜨리는지 실험으로 분석했고,[^p6] 쥐 사이의 서열 관계가 상대의 공포에 공감하는 정도를 바꾼다는 것을 보였으며,[^p7] 문·창문·계단 같은 건축 요소를 보기만 해도 그 요소가 요구하는 동작이 뇌에서 미리 시뮬레이션된다는 것을 fMRI로 보였다.[^p8]

**계산 신경정신의학**은 뇌영상·행동·유전 자료를 함께 분석해 정신질환의 원인을 이해하고 치료 방법을 제안한다.[^research] 대표 논문에서는 이마 쪽 전극 두 개의 뇌파와 기계학습으로 공황장애와 주요우울장애를 구별하는 방법을 시험했다.[^p2] **커넥톰** 연구에서는 신경계의 연결이 어떻게 만들어지고 행동 차이로 이어지는지 연구하며,[^research] 예쁜꼬마선충의 좌우 짝 신경세포가 연결이 다르더라도 연결망에서 비슷한 역할을 나눠 맡는다는 것을 보였다.[^p3] **뇌-컴퓨터 인터페이스**는 의료 진단과 로봇·외골격 제어를 위해 뇌 상태를 읽어 내는 방법을 개발하며,[^research] 상상한 손 움직임의 궤적을 뇌 표면 전극 신호에서 읽어 냈고,[^p4] 가상현실 멀미가 생길 때의 뇌파 상태를 분석했다.[^p5] 이 밖에 동물의 호기심과 계획 방식에서 착안한 강화학습 같은 **뇌를 본뜬 인공지능**도 연구 영역으로 든다.[^research]

## 주요 연구 주제

### 1. 뇌 동역학과 신경정신질환

자폐 스펙트럼 장애의 동적 모드 분석, 두 채널 뇌파 기반 공황장애·우울장애 진단.[^p1][^p2] 대표 논문 1, 2.

### 2. 커넥톰

예쁜꼬마선충 좌우 짝 신경세포의 연결망 역할.[^p3] 대표 논문 3.

### 3. 뇌-컴퓨터 인터페이스

상상한 손 움직임 궤적 해독, 가상현실 멀미의 뇌파 상태.[^p4][^p5] 대표 논문 4, 5.

### 4. 사회적 의사결정과 신경건축학

소문 전파의 조건, 서열 관계와 공감, 건축 요소의 행동 시뮬레이션.[^p6][^p7][^p8] 대표 논문 6–8.

## 대표 논문

랩 논문 목록의 2021–2026년 논문 가운데 정재승 교수가 마지막 저자인 것에서 연구 영역을 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2026 | [Dynamic mode decomposition analysis of brain dynamics in autism spectrum disorder patients](https://doi.org/10.1016/j.neuroimage.2026.122044) · NeuroImage | 자폐 스펙트럼 장애 연구는 대부분 뇌 영역 사이의 고정된 연결만 보았다. 849명의 휴지기 fMRI에 동적 모드 분해를 적용해 시간에 따라 되풀이되는 뇌 활동 패턴을 찾았고, 자폐군에서 뒤쪽 시각-두정-측두 패턴의 진동 시점이 달랐으며 나이에 따른 변화도 정형 발달군과 달랐다. 자폐군 안에서는 이 특징이 지능지수의 개인차와도 관련됐다.[^p1] | 1저자 Mir Jeong, 마지막 저자 정재승 |
| 2 | 2023 | [Two-channel EEG based diagnosis of panic disorder and major depressive disorder using machine learning and non-linear dynamical methods](https://doi.org/10.1016/j.pscychresns.2023.111641) · Psychiatry Research: Neuroimaging | 이마 쪽 전극 두 개(Fp1, Fp2)로 잰 149명의 뇌파에서 비선형 복잡도 지표를 뽑아 서포트 벡터 머신으로 공황장애·주요우울장애 환자와 건강한 사람을 구별했다. 두 환자군 모두 왼쪽 뇌의 복잡도가 낮았고, 우울장애 환자와 건강한 사람을 90%, 공황장애 환자와 대조군을 68% 정확도로 구별했다.[^p2] | 1저자 Adedoyin Aderinwale, 교신 Han Young Yu·정재승 |
| 3 | 2026 | [Bilateral Neuron Pairs Share Redundant Network Roles Despite Incomplete Connection Symmetry in C. elegans](https://doi.org/10.1111/ejn.70629) · European Journal of Neuroscience | 예쁜꼬마선충의 좌우 짝 신경세포는 각자의 연결이 꽤 다르다. 성체 자웅동체와 수컷의 커넥톰을 세 가지 그래프 지표로 분석하자, 짝 신경세포가 다른 신경세포 쌍보다 연결망에서 겹치는 역할을 더 많이 맡았고, 이는 좌우 대칭만으로는 생기지 않는 패턴이었다. 자웅동체에서는 이런 겹침이 감각 신경세포보다 중간 신경세포에서 더 뚜렷했다.[^p3] | 1저자 Pyeong Soo Kim, 마지막 저자 정재승 |
| 4 | 2022 | [Decoding trajectories of imagined hand movement using electrocorticograms for brain–machine interface](https://doi.org/10.1088/1741-2552/ac8b37) · Journal of Neural Engineering | 손을 움직이지 못하는 환자를 위한 뇌-기계 인터페이스에는 상상만 한 손 움직임을 읽어 내는 기술이 필요하다. 뇌전증 환자 18명이 손을 뻗어 쥐는 동작을 실제로 하거나 상상할 때의 뇌 표면 전극 신호(ECoG)를 기계학습으로 분석해, 상상한 손의 궤적을 우연 수준보다 유의하게 예측했다.[^p4] | 1저자 Sang Jin Jang, 교신 정재승 |
| 5 | 2022 | [Electroencephalogram microstates and functional connectivity of cybersickness](https://doi.org/10.3389/fnhum.2022.857768) · Frontiers in Human Neuroscience | 가상현실 멀미는 감각 신호와 뇌의 내부 예측이 어긋나서 생긴다는 이론이 널리 받아들여진다. 남성 40명이 가상현실 영상을 10분 보는 동안의 뇌파를 잠시 안정된 상태들(미세 상태)로 나누고 영역 사이 기능 연결을 분석해, 멀미가 생길 때의 뇌 상태를 살폈다.[^p5] | 1저자 Sungu Nam, 교신 Hyun Kyoon Lim·정재승 |
| 6 | 2022 | [How ‘who someone is’ and ‘what they did’ influences gossiping about them](https://doi.org/10.1371/journal.pone.0269812) · PLOS ONE | 사람들이 언제 그 자리에 없는 제3자의 이야기를 퍼뜨리는지 알아보려고, 대상(내집단·외집단·유명인), 좋고 나쁨, 내용을 바꾼 소문 시나리오를 제시했다. 유명인과 내집단 사람에 대한 소문을, 나쁜 일에 대한 소문을, 도덕적 주제를 더 많이 퍼뜨렸고, 내집단 사람에 대해서는 좋은 소문을 더 퍼뜨렸다.[^p6] | 1저자 Jeungmin Lee, 교신 Jerald D. Kralik·정재승 |
| 7 | 2022 | [Experience of a hierarchical relationship between a pair of mice specifically influences their affective empathy toward each other](https://doi.org/10.1111/gbb.12810) · Genes, Brain and Behavior | 서열 경험이 공감의 기본 형태인 감정 전염에 영향을 준다는 것은 알려졌지만, 개체의 성향이 바뀌어서인지 두 개체 사이의 관계 때문인지는 몰랐다. 네 마리 쥐 무리의 서열을 정한 뒤 관찰 공포 학습을 시키자, 같은 우리에서 지낸 상대일 때만 서열에 따라 공포 반응이 달랐고 서열 차이가 클수록 반응이 컸다. 두 개체 사이의 서열 관계가 감정 전염에 결정적이었다.[^p7] | 1저자 Jungjoon Park, 교신 Hee-Sup Shin·정재승 |
| 8 | 2026 | [Neural Basis of Action Simulation in Architectural Perception: A Multi-voxel Pattern Analysis Study](https://doi.org/10.1162/jocn.a.2486) · Journal of Cognitive Neuroscience | 문·창문·계단처럼 직접 다뤄야 하는 건축 요소를 그냥 보기만 해도 뇌가 그에 맞는 동작을 미리 떠올리는지 알아보려고 31명의 fMRI를 다중 복셀 패턴 분석했다. 요소를 보기만 해도 그 요소의 주된 기능에 맞는 신경 패턴과 필요한 상호작용의 감각운동 표상이 나타났고, 전운동피질과 등쪽 시각 경로 같은 운동 관련 영역이 활성화됐다.[^p8] | 1저자 Wooree Shin, 마지막 저자 정재승 |

## 교수와 전문 분야

정재승 교수는 KAIST 물리학과에서 학사(1994), 석사(1996), 박사(1999)를 받았다. 미국 예일대 의대 소아정신과 연구원(1999–2001), 고려대 물리학과 연구교수(2001–2004)를 거쳐 2004년 KAIST 바이오및뇌공학과 조교수로 부임했고, 2005–2008년 미국 컬럼비아대 정신과 겸임 조교수를 지냈다. 2021년부터 KAIST 융합인재학부장, 2022년부터 뇌인지과학과장이며, 2025년부터 뇌과학연구센터장과 대교-KAIST 인지향상 연구센터장을 맡고 있다.[^prof] 랩 소식에는 2026년 유네스코 본부 패널 행사 발표 등의 글이 있다.[^news]

논문으로 보면 전문 분야는 세 갈래다.

- **뇌 동역학 분석과 계산 신경정신의학**.[^p1][^p2]
- **커넥톰과 뇌-컴퓨터 인터페이스**.[^p3][^p4][^p5]
- **사회적 의사결정과 신경건축학**.[^p6][^p7][^p8]

## 응용 분야

대표 논문과 연구 소개로 보면 정신질환의 빠른 진단 보조, 손 운동 장애 환자를 위한 뇌-기계 인터페이스, 가상현실 콘텐츠의 멀미 관리, 사람에게 더 나은 건축·공간 설계에 닿아 있다.[^p2][^p4][^p5][^p8][^research] 랩 History 페이지에는 국방과학연구소, 과학기술정보통신부, 코웨이, 현대엔지비 등이 지원한 과제가 적혀 있다.[^history]

## 구성원

2026년 10월 20일 랩 Research Scientists·Students 페이지 기준이다. 연구 주제는 랩이 적은 것이다.[^scientists][^students] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Muhammad Zubair | 연구원 (Ph.D.) | Affective computing, Biomedical signal processing, Deep learning, Representation learning, Explainable AI (XAI), Neurodegenerative Disorders |  |
| 이정민 Jeongmin Lee | 연구원 (Ph.D.) | Social communication, Social interactions, gossip, Cognitive neurosience, fMRI | 6 |
| 장상진 Sang Jin Jang | 연구원 (Ph.D.) | Brain-computer interface (BCI), Brain-machine interface (BMI), Robotic arm, Trajectory, EEG, Imagined movement | 4 |
| 김평수 Pyeong Soo Kim | 연구원 (Ph.D.) | Connectome, Caenorhabditis elegans, Complex network, Graph theory, Asymmetry, fMR | 3 |
| 남선구 Sungu Nam | 연구원 (Ph.D.) | VR Perception, AR Perception, BCI, EEG, Cybersickness | 5 |
| 김선일 Sunil Kim | 연구원 (Ph.D.) | Data-Driven Science, Dynamical Systems, EEG, The General Theory of Brain Dynamics, Statistical Physics, Subjective Probability Theory |  |
| 신우리 Wooree Shin | 연구원 (Ph.D.) | Neuroarchitecture, Affordance, Architectural affordance, Cognitive neuroscience | 8 |
| Adedoyin Aderinwale | 연구원 (Ph.D.) | Social Curiosity, Social Decision making, fMRI, Suicide, Mental disorders, Machine Learning Applications | 2 |
| 김신 Sin Kim | 박사과정 | Neuropsychiatry, Adolescent development, Genetics, Machine learning |  |
| 정미르 Mir Jeong | 박사과정 | Neuropsychiatric disorder, Graph theory | 1 |
| 정준하 Rachel Jung | 박사과정 | Brain-Computer Interface, EEG Analysis, Machine Learning, Deep Learning |  |
| 박재빈 Jaebin Park | 박사과정 | Resilience, Suicide, Psychological Pain, Mental Disorders |  |
| 오홍석 Hong Suk Oh | 박사과정 | neuropolitics, political neuroscience, political decision making, political polarization, political ideology |  |
| 조형진 HyungJin Cho | 박사과정 | Decision Science, Choice Architecture, Behavioral Economics, Neuroeconomics |  |
| 김지온 Zion Kim | 박사과정 | BCI Brain Wave EEG Medical Engineering Robotics Brain Disease |  |
| 안성호 Seong-Ho Ahn | 박사과정 | Spontaneous thought, Computational semantic modeling, Neural dynamics, Machine learning, Meditation |  |
| Gulnara Gimadeeva | 박사과정 | early-life stress and neurodevelopment, stress-related conditions, PTSD, amygdala, neuroinflammation in psychiatric disorder |  |
| Gulim Nurgazina | 박사과정 | aging, schizophrenia, neurodevelopment, neuroimaging, computational psychiatry |  |
| 강재영 Jaeyoung Kang | 박사과정 | Brain Resilience, Neurodegenerative Diseases with Aging, Multimodal Imaging, Genetics, Computational Network Neuroscience, AI-based Modelling |  |
| 손서은 Seoeun Son | 박사과정 | Neurodegenerative disease, Alzheimer's disease, Aging, Cognitive reserve |  |
| Dharren Sandhi Goutama | 박사과정 | brain-computer interface, speech reconstruction, semantic decoding, deep learning |  |

## 졸업생과 이전 구성원

랩 Alumni 페이지의 이름, 과정, 랩이 적은 현재 소속이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 이채원 Rowen Lee | Undergraduate Researcher | Graduate Student @ University of Waterloo |
| 전성원 Sungwon Jeon | NEURO Intern |  |
| 강태희 Taehee Kang | NEURO Intern |  |
| 강창아 Changa Kang | NEURO Intern |  |
| 윤수근 Sugeun Yun | Masters |  |
| Adedoyin Aderinwale | PhD. | Post Doc. Researcher |
| 류가은 Gaeun Ryu | Masters |  |
| 최병혁 Byung Hyug Choi | PhD. | Researcher at Emocog |
| 정석진 Seokjin Jeong | Masters |  |
| Iuliia Kleimenova | Masters |  |
| 오승윤 Julie Oh | Masters |  |
| 신우리 Wooree Shin | PhD. | Post Doc. Researcher |
| 김선일 Sunil Kim | PhD. | Post Doc. Researcher |
| 남선구 Sungu Nam | PhD. | Post Doc. Researcher |
| 김평수 Pyeong Soo Kim | PhD. | Post Doc. Researcher |
| 김재현 Jaehyun Kim | PhD. |  |
| 장상진 Sang Jin Jang | PhD. | Post Doc. Researcher |
| 이정민 Jeongmin Lee | PhD. | Post Doc. Researcher |
| Pouya Ghasemlou | Masters |  |
| 박정준 Jungjoon Park | PhD. | 액티노바: COO/Research Director |
| Gemechu Bekele Tolossa | Masters | PhD Candidate - Washington University in St. Louis |
| 임세웅 Sewong Kim | PhD. |  |
| 정동화 Dong-Hwa Jeong | PhD. | Professor at the Catholic University of Korea |
| 윤상섭 Sangsub Yoon | PhD. |  |
| 권재형 Jaehyung kwon | PhD. |  |
| 장재환 Jaehwan Jang | PhD |  |
| 김훈희 Hoon He Kim | PhD | Assistant Professor at Pukyong National University |
| 백진희 Jinje Baek | PhD. |  |
| CHRISTIANUS FREDERICK HOTAMA | Masters |  |
| 이정원 Jungwon Lee | PhD. |  |

## 최근 논문 목록 (2021–2026)

랩 Journal articles 페이지 1–3쪽의 2021년 이후 논문이다.[^papers]

**2026**

- Choi, Yun Ho; Kim, Sunil; Jeong, Jaeseung; Kim, Seonghoon] Ryu, Dong-Woo; Kim, Woojun Jung, Yu Jin. "A Deep Learning Approach for Classifying Rapid Eye Movement Sleep Behavior Disorder Using EEGNet". *JOURNAL OF CLINICAL NEUROLOGY*.
- Wooree Shin, Youngjo Song, Jaeseung Jeong. "Neural Basis of Action Simulation in Architectural Perception: A Multi-voxel Pattern Analysis Study". *Journal of Cognitive Neuroscience*.
- Mir Jeong, Youngjo Song, Jaeseung Jeong. "Dynamic Mode Decomposition Analysis of Brain Dynamics in Autism Spectrum Disorder Patients". *NeuroImage*.
- Pyeong Soo Kim, Youngjo Song, Jerald D. Kralik, Jaeseung Jeong. "Bilateral neuron pairs share redundant network roles despite incomplete connection symmetry in Caenorhabditis elegans". *EUROPEAN JOURNAL OF NEUROSCIENCE*.

**2025**

- Babiloni, C; Arakaki, X; Baez, S; Barry, RJ; Benussi, A; Blinowska, K; Bonanni, L; Borroni, B; Bayard, JB; Bruno, G; Cacciotti, A; Carducci, F; Carino, J; Carpi, M; Conte, A; Cruzat, J; D'Antonio, F; Della Penna, S; Del Percio, C; De Sanctis, P; Escudero, J; Fabbrini, G; Farina, FR; Fraga, FJ; Fuhr. "Alpha rhythm and Alzheimer's disease: Has Hans Berger's dream come true?". *CLINICAL NEUROPHYSIOLOGY*.
- Hotama, Christianus F.; Kralik, Jerald D.; Jeong, Jaeseung. "Critical Regions and Connections Form Pathways and Clusters in the Mouse Brain". *EUROPEAN JOURNAL OF NEUROSCIENCE*.
- Jung, YJ; Kim, S; Choi, YH; Ryu, DW; Kim, W; Kim, S; Jeong, J. "Deep-Learning-Based Automated REM Sleep Detection in Patients With REM Sleep Behavior Disorder: Is It Reliable?". *JOURNAL OF CLINICAL NEUROLOGY*.

**2024**

- Hyungjoon Soh, Joo Hyung Hong, Jaeseung Jeong and Hawoong Jeong. "Long-term memory on popularity dynamics: insights from the Billboard Hot 100 chart". *JOURNAL OF STATISTICAL MECHANICS-THEORY AND EXPERIMENT*.

**2023**

- Song, Youngjo; Shin, Wooree; Kim, Pyeongsoo; Jeong, Jaeseung. "Neural representations for multi-context visuomotor adaptation and the impact of common representation on multi-task performance: a multivariate decoding approach". *FRONTIERS IN HUMAN NEUROSCIENCE*.
- Adedoyin Aderinwale, Gemechu Bekele Tolossa, Ah Young Kim, Eun Hye Jang, Yong-il Lee, Hong Jin Jeon, Hyewon Kim, Han Young Yu\*, Jaeseung Jeong\*. "Two-channel EEG based diagnosis of panic disorder and major depressive disorder using machine learning and non-linear dynamical methods". *Psychiatry Research: Neuroimaging, 332, 111641*.

**2022**

- Sang Jin Jang\*, Yu Jin Yang, Seokyun Ryun, June Sic Kim, Chun Kee Chung and Jaeseung Jeong\*. "Decoding trajectories of imagined hand movement using electrocorticograms for brain–machine interface". *Journal of Neural Engineering, 19(5), 056011*.
- Sungu Nam, Kyoung-Mi Jang, Moonyoung Kwon, Hyun Kyoon Lim\*, Jaeseung Jeong\*. "Electroencephalogram microstates and functional connectivity of cybersickness". *Frontiers in Human Neuroscience, 16*.
- Jeungmin Lee, Jerald D. Kralik\*, Jaehyung Kwon & Jaeseung Jeong\*. "How "who someone is" and "what they did" influences gossiping about them". *PloS one, 17(7), e0269812*.
- Jungjoon Park, Seungshin Ha, Hee‐Sup Shin\*, Jaeseung Jeong\*. "Experience of a hierarchical relationship between a pair of mice specifically influences their affective empathy toward each other". *Genes, Brain and Behavior, 21(5), e12810*.
- Hoon-Hee Kim, Jaeseung Jeong\*. "An electrocorticographic decoder for arm movement for brain–machine interface using an echo state network and Gaussian readout". *Applied Soft Computing, 117, 108393*.

**2021**

- Dongjae Kim, Jaeseung Jeong, Sang Wan Lee\*. "Prefrontal solution to the bias-variance tradeoff during reinforcement learning". *Cell Reports, 37(13), 110185*.
- Babiloni Claudio\*, [….], Jaeseung Jeong, et al. "Measures of resting state EEG rhythms for clinical trials in Alzheimer"s disease Recommendations of an expert panel". *Alzheimer"s & Dementia, 17(9), 1528-1553*.
- Babiloni Claudio\*, [….], Jaeseung Jeong, et al. "EEG measures for clinical research in major vascular cognitive impairment: recommendations by an expert panel". *Neurobiology of Aging, 103, 78-97*.

## 연구 과제

랩 History 페이지에 적힌 2021년 이후 시작 과제와 기간, 지원 기관, 사업명, 랩이 적은 총 연구비다.[^history]

- Innovative Rehabilitation Engineering Technology to Overcome Neurological Disorders (기간 2023.01 – 2023.11; 지원 한국과학기술원; 사업 KAIST기본사업1(정부); 연구비 5억)
- Identification of the social control mechanism by the neuromodulator TRH (기간 2022.09 – 2026.12; 지원 한국과학기술원; 사업 KAIST자체연구사업(비정산); 연구비 2억)
- Research on non-invasive BCI-based video target recognition technology (기간 2022.07 – 2023.03; 지원 국방과학연구소; 사업 미래도전국방기술 연구개발사업; 연구비 1.5억)
- Research on non-invasive BCI-based still image target recognition technology (기간 2022.07 – 2023.03; 지원 국방과학연구소; 사업 미래도전국방기술 연구개발사업; 연구비 1.5억)
- Development of artificial intelligence-based false statement precision discrimination system using EEG-fMRI (기간 2022.03 – 2023.12; 지원 과학기술사업화진흥원&(재)과학기술일자리진흥원; 사업 과학치안 공공연구성과 실용화 촉진 시범사업; 연구비 7.9억)
- Establishment of human-centered SF manufacturing philosophy (기간 2021.04 – 2021.09; 지원 현대엔지비(주); 사업 산업체연구개발사업; 연구비 1.3억)
- Verification of the effectiveness of the Brain Refresh Chair's therapy function on the body (brain function) (기간 2021.04 – 2021.12; 지원 코웨이(주); 사업 산업체연구개발사업; 연구비 1.5억)
- The Future of Web Novels: Development of Evaluation Indicators for Industrial Expansion of Original Web Novels - Focusing on Korean Romance Web Novels (기간 2021.04 – 2021.12; 지원 한국과학기술원; 사업 KAIST자체연구사업; 연구비 0.04억)

## 소식

랩 News 게시판 1–2쪽의 2021년 이후 소식이다(새 구성원 환영 글 제외). 게시판 목록에서 말줄임표로 줄어든 제목은 그대로 두었다.[^news]

- 2026-07-20 · Publication - Dr. Pyeong Soo Kim's paper was published in the Euro...
- 2026-07-01 · Publication - Dr. Wooree Shin's paper was published in the Journal...
- 2026-06-09 · Defence - Sugeun Yun (Masters course) has successfully defended!
- 2026-06-08 · Publication - Mir Jeong and Dr. Youngjo Song's (graduate from our ...
- 2026-03-27 · Panel Event - Professor Jaeseung Jeong speaks at UNESCO headquarte...
- 2026-03-04 · Publication - Dr. Sunil Kim and Professor Jaeseung Jeong's paper w...
- 2026-02-25 · Dr. Sungu Nam presents at BCI 2026
- 2026-02-23 · Graduation - Congrats to Byeonghyug Choi, Julie Oh, Seokjin Jeong,...
- 2026-02-01 · Graduation - Congrats to Dr. Adedoyin Aderinwale in completing his...
- 2025-12-10 · Celebration - Daekyo and KAIST create the Center for Cognitive Enh...
- 2025-09-15 · Panel Event - Professor Jaeseung Jeong speaks with Dongjin Seo, th...
- 2025-09-13 · Panel Event - Professor Jaeseung Jeong speaks at the grand opening...
- 2025-03-06 · DBDL Lab Structure: 2025
- 2025-02-25 · Publication - Professor Jerald Kralik Professor Jaeseung Jeong's p...
- 2025-02-09 · Publication - Professor Jaeseung Jeong publishes in Clinical Neuro...
- 2022-09-01 · Celebration - Graduate Dr. Hoon-Hee Kim becomes an Assistant Profe...

## 연락과 위치

- 연구실: KAIST 메타융합관(W13) 402호[^contact]

[^home]: 연구실 누리집 첫 화면 <https://raphe.kaist.ac.kr/> (2026-10-20 열람)
[^goal]: Goal 페이지 <https://raphe.kaist.ac.kr/ourgoal> (2026-10-20 열람)
[^research]: Research areas 페이지 <https://raphe.kaist.ac.kr/research_areas> (2026-10-20 열람)
[^prof]: Lab Director 페이지 <https://raphe.kaist.ac.kr/lab-director> (2026-10-20 열람)
[^scientists]: Research Scientists 페이지 <https://raphe.kaist.ac.kr/research-scientists> (2026-10-20 열람)
[^students]: Students 페이지 <https://raphe.kaist.ac.kr/students> (2026-10-20 열람)
[^alumni]: Alumni 페이지 <https://raphe.kaist.ac.kr/alumni> (2026-10-20 열람)
[^papers]: Journal articles 페이지 1–3쪽 <https://raphe.kaist.ac.kr/all> (2026-10-20 열람)
[^history]: History 페이지 <https://raphe.kaist.ac.kr/history> (2026-10-20 열람)
[^news]: News 게시판 1–2쪽 <https://raphe.kaist.ac.kr/news> (2026-10-20 열람)
[^contact]: Contact us 페이지 <https://raphe.kaist.ac.kr/contactus> (2026-10-20 열람)
[^p1]: M. Jeong, Y. Song, J. Jeong, NeuroImage 338, 122044 (2026). <https://doi.org/10.1016/j.neuroimage.2026.122044> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: A. Aderinwale 외, J. Jeong, Psychiatry Research: Neuroimaging 332, 111641 (2023). <https://doi.org/10.1016/j.pscychresns.2023.111641> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: P. S. Kim, Y. Song, J. D. Kralik, J. Jeong, European Journal of Neuroscience 64, e70629 (온라인 2026-07-20). <https://doi.org/10.1111/ejn.70629> 초록 기준.
[^p4]: S. J. Jang 외, J. Jeong, Journal of Neural Engineering 19, 056011 (온라인 2022-09-07). <https://doi.org/10.1088/1741-2552/ac8b37> 초록 기준.
[^p5]: S. Nam 외, J. Jeong, Frontiers in Human Neuroscience 16, 857768 (온라인 2022-08-22). <https://doi.org/10.3389/fnhum.2022.857768> 초록 기준.
[^p6]: J. Lee, J. D. Kralik, J. Kwon, J. Jeong, PLOS ONE 17, e0269812 (온라인 2022-07-06). <https://doi.org/10.1371/journal.pone.0269812> 초록 기준.
[^p7]: J. Park, S. Ha, H.-S. Shin, J. Jeong, Genes, Brain and Behavior 21, e12810 (온라인 2022-04-22). <https://doi.org/10.1111/gbb.12810> 초록 기준.
[^p8]: W. Shin, Y. Song, J. Jeong, Journal of Cognitive Neuroscience 38, 1484-1500 (온라인 2026-07-01). <https://doi.org/10.1162/jocn.a.2486> 초록 기준.

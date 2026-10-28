# 협동 분산 시스템 및 네트워크 연구실 (Collaborative Distributed Systems and Networks Laboratory, CDSN)

**KAIST 전산학부 · 이동만 KAIST교수**

- 분야: 지능형 엣지 컴퓨팅, 분산 시스템, 사람 행동 인식, 사물인터넷 서비스의 자율 협업, 도시 활동과 공간 변화 분석
- 대분야: 컴퓨팅·AI
- 태그: 엣지 컴퓨팅·엣지 AI[^lab][^edge], 강화학습[^lab][^edge], 연합학습·분산 학습[^lab][^p2], 멀티모달 AI[^p4], 다중 에이전트 시스템·분산 의사결정[^research][^iot], 교통·도시 계획[^p6], 모바일·유비쿼터스 센싱[^p4][^p5]
- 홈페이지: <https://cds.kaist.ac.kr/>
- 근거와 출처: [CDSN 근거 페이지](cdsn-sources.md)

> 사람의 활동과 도시의 변화를 알아내고, 주변 기기와 서버가 계산·서비스를 나눠 수행하도록 만드는 연구실이다. 사용자의 의도를 파악하는 인공지능과 사물인터넷의 자율 협업을 연결해 상황에 맞는 공간 서비스를 연구한다.[^research][^lab]

## 무엇을 연구하나

KAIST 전산학부 이동만 교수가 이끄는 CDSN은 사물인터넷(IoT, Internet of Things: 사물이 통신망을 통해 정보를 주고받는 체계)을 이루는 기기들이 함께 작동해 사람에게 필요한 서비스를 제공하는 방법을 연구한다. 목표는 사용자의 의도와 공간의 상태를 알아내고, 그에 맞춰 서비스를 구성하는 Urban Space Robot 플랫폼이다. Urban Space Robot은 도시 공간 안의 기기와 서비스를 조정하는 컴퓨팅 플랫폼으로 소개된다.[^research][^lab]

첫째 갈래는 **엣지 컴퓨팅과 계산 자원 배분**이다. 엣지 컴퓨팅은 자료가 발생하는 기기나 그 가까운 장치에서 계산하는 방식이다. 연구실은 네트워크 상태, 기기의 계산 능력, 사용자가 요구하는 정확도와 지연 시간을 함께 고려해 서비스를 배치한다. 강화학습(행동에 따른 보상을 바탕으로 행동 방법을 학습하는 기계학습)을 이용한 서비스 설정과, 환경 변화에 맞춘 실시간 자원 재구성을 연구한다.[^edge][^lab] OCTOPINF는 영상 분석 작업을 기기와 서버에 나누고 작업 일정을 조정하며, AdaS-LoRA는 여러 기기가 자료를 나눠 가진 채 모델을 함께 학습하는 연합학습에서 계산과 통신 자원을 구분해 배분한다.[^p1][^p2] 차량이 서로 인지 정보를 나누는 FadeLead는 배경의 문맥을 전경(영상의 주요 대상으로 구분한 부분) 표현에 담아 전송하는 방법을 다룬다.[^p3]

둘째는 **사람 행동과 선호를 이해하는 사물인터넷 자동화**다. 연구실은 사람의 행동, 기기와의 상호작용, 개인별 생활 패턴을 분석해 조명·온도·가전의 작동을 상황에 맞게 조절하는 체계를 연구한다. 여러 에이전트(상태를 받아 판단하고 행동하는 주체)가 충돌을 피하면서 함께 서비스를 제공하는 방법과, 사용자의 개입과 자동화 사이의 조정도 연구 과제다.[^iot] DETACH는 외부 시점 영상과 공간에 설치한 센서 자료를 연결해 행동을 인식하고, CLAN은 시간·주파수(단위 시간 동안 변화가 반복되는 횟수) 관점을 함께 학습해 훈련 자료에 없던 새로운 행동을 탐지한다.[^p4][^p5]

셋째는 **도시 활동과 공간 변화 예측**이다. 연구실은 장소에 대한 사회적 자료와 사람의 이동·활동 자료를 분석해 공간의 의미와 변화 양상을 다룬다.[^lab] 대형 언어 모델(LLM, Large Language Model: 대규모 언어 자료로 학습해 언어를 처리하고 생성하는 모델) 기반 도시 연구에서는 인구 이동, 교통 패턴, 건물 이용 등 여러 종류의 자료를 결합해 시간과 공간에 따른 변화를 예측하려 한다.[^urbanllm] 지역별 Airbnb 추세 예측 논문은 숙소·접근성·이동 자료를 언어 모델로 표현한 뒤 시계열(시간 순서로 기록한 자료) 예측에 연결하고, 교통 예측 논문은 사람의 활동 빈도 자료로 교통 패턴과의 관계를 반영한다.[^p6][^p7]

이 세 갈래는 사람과 공간을 이해하는 분석, 여러 기기에 계산을 나누는 분산 시스템, 실제 서비스의 재구성으로 이어진다. 연구실은 사용자의 의도가 달라지거나 도시의 조건이 변할 때 IoT 서비스를 다시 구성하고, 사용자의 반응에서 선호를 학습하는 공간 지능을 목표로 제시한다.[^research] 영상 분석의 작업 처리, 센서 기반 행동 이해, 도시 변화 예측이 이 목표를 서로 다른 자료와 규모에서 다룬다.[^p1][^p4][^p6]

## 주요 연구 주제

### 1. 엣지 자원 배분과 협력 인지

영상 분석의 작업 배치·스케줄링(작업 순서와 실행 시점을 정하는 과정)과 연합학습의 계산·통신 자원 배분을 연구하며, 통신 제약을 고려한 차량 간 협력 인지도 다룬다. OCTOPINF, AdaS-LoRA, FadeLead가 이 갈래의 대표 논문이다.[^p1][^p2][^p3]

### 2. 사람 행동 인식과 새로운 행동 탐지

영상과 주변 센서의 서로 다른 자료를 정렬하고, 시간·주파수 특성으로 행동을 학습해 새로운 행동을 탐지한다. IoT 기기의 상호운용성(서로 다른 시스템이 정보를 주고받으며 함께 작동하는 성질)과 선호 학습을 이용한 상황 맞춤 서비스도 연구한다.[^p4][^p5][^iot]

### 3. 도시 활동과 공간 변화 예측

사람의 이동·활동, 접근성, 숙소 등 공간에 관한 자료를 결합한다. 언어 모델의 임베딩(자료의 특성을 수치 벡터로 나타낸 표현)을 이용한 지역 추세 예측과 활동 자료를 결합한 교통 예측으로 도시 정책과 공간 이해를 지원하는 방법을 다룬다.[^p6][^p7][^urbanllm]

## 대표 논문

2021–2026년 연구실 논문 가운데 세 연구 갈래를 담도록 7편을 골랐다. 이동만 교수는 모두 마지막 저자다. FadeLead는 arXiv 사전 공개본을 기준으로 설명했다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.[^pubs]

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [OCTOPINF: Workload-Aware Inference Serving for Edge Video Analytics](https://doi.org/10.1109/PerCom64205.2025.00032) · PerCom | 영상 분석에 필요한 계산을 주변 기기와 서버에서 처리할 때, 작업량과 네트워크 상태가 변하고 같은 계산 자원을 두고 작업들이 경쟁하는 문제가 생긴다. OCTOPINF는 자원을 세분해 배분하고, 작업을 묶는 방식과 기기·서버 사이의 작업량을 조정한다. 계산 작업의 시간·공간 배치도 함께 정해 지연 시간 요구를 지키며 처리량을 높이는 시스템이다.[^p1] | Thanh-Tung Nguyen, Lucas Liebe, Nhat-Quang Tau, Yuheng Wu, Jinghan Cheng, Dongman Lee |
| 2 | 2026 | [ADAS-LORA: Efficient Federated LLM Tuning in Edge Systems by Decoupling Compute and Network](https://doi.org/10.1109/ICDCSW72724.2026.00056) · ICDCSW | 기기마다 계산 능력이 다르고 무선 통신 자원은 함께 나눠 써야 한다. 이 두 제약을 하나의 설정으로 맞추면 통신 병목이 생긴다는 문제에서 출발했다. AdaS-LoRA는 언어 모델을 각 기기에서 조정할 때 계산용 설정과 통신용 설정을 나누고, 필요한 학습 요소와 통신 자원을 배분해 정확도를 유지하면서 통신 부담을 줄인다.[^p2] | Pablo Espinosa-Campos, Lucas Liebe, Thanh-Tung Nguyen, Nhat-Quang Tau, Yuheng Wu, Dongman Lee |
| 3 | 2025 | [Background Fades, Foreground Leads: Curriculum-Guided Background Pruning for Efficient Foreground-Centric Collaborative Perception](https://doi.org/10.48550/arXiv.2510.19250) · arXiv 사전 공개본 | 차량들이 주변을 인식한 정보를 공유하면 각 차량이 혼자 보기 어려운 상황을 보완할 수 있지만 전송량에 제약이 있다. 배경 정보를 버리고 전경만 보내는 기존 방식의 한계를 다루기 위해, FadeLead는 훈련 초기에 배경 단서를 활용하고 점차 제거하면서 배경 문맥이 전경 표현에 담기게 한다. 배경 자체를 전송하지 않으면서 그 문맥을 활용하는 협력 인지 방법이다.[^p3] | Yuheng Wu, Xiangbo Gao, Quang Tau, Zhengzhong Tu, Dongman Lee |
| 4 | 2026 | [DETACH : Decomposed Spatio-Temporal Alignment for Exocentric Video and Ambient Sensors with Staged Learning](https://cds.kaist.ac.kr/publications/) · CVPR | 몸에 착용한 센서 대신 공간의 센서와 외부에서 찍은 영상을 함께 활용해 행동을 인식하려는 연구다. DETACH는 두 종류의 자료를 공간·시간 성분으로 나누고, 영상의 세부 움직임과 센서의 공간적 관계를 연결한다. 이를 바탕으로 자료 사이의 시간적 대응을 학습해 행동 인식을 개선한다.[^p4] | Junho Yoon, Jaemo Jeong, Hyunju Kim, Dongman Lee |
| 5 | 2025 | [Self-supervised Dual-view Framework with Tailored Negative Sampling for New Activity Detection](https://doi.org/10.1145/3746252.3761163) · CIKM | 실제 공간에서는 훈련 자료에 없던 행동이 나타난다. CLAN은 센서 자료를 시간과 주파수라는 두 관점에서 표현하고, 알려진 행동의 자료를 변형해 새로운 행동과 구별하는 특징을 학습한다. 자료별 특성에 맞는 변형 방법도 선택해 여러 센서 환경에서 새로운 행동을 탐지한다.[^p5] | Hyunju Kim, Dongman Lee |
| 6 | 2025 | [Enhancing Regional Airbnb Trend Forecasting Using LLM-Based Embeddings of Accessibility and Human Mobility](https://doi.org/10.1007/978-3-032-13513-1_30) · ASONAM | 개별 숙소가 아니라 지역 단위로 Airbnb의 수입·예약 일수·예약 건수 변화를 예측한다. 숙소 특성에 도시 접근성과 사람 이동 자료를 더하고, 표 형태 자료를 언어 모델의 입력으로 바꿔 지역의 특징을 표현한다. 그 표현을 시간에 따른 변화 예측 모델에 넣어 지역별 추세와 공급 과잉을 살피고 도시 정책 판단을 지원하려는 방법이다.[^p6] | Hongju Lee, Youngjun Park, Jisun An, Dongman Lee |
| 7 | 2023 | [Enhancing Spatio-temporal Traffic Prediction through Urban Human Activity Analysis](https://doi.org/10.1145/3583780.3614867) · CIKM | 교통 센서 자료만으로는 실제 도로 이용과 도시 활동에서 생기는 교통 패턴을 충분히 설명하기 어렵다는 문제를 다뤘다. 사람의 활동 빈도 자료를 결합해 활동과 교통의 관계를 반영하는 그래프 기반 예측 방법을 제안한다. 기존 예측 구조를 조정해 추가 계산 부담을 억제하면서 교통 예측 성능을 높였다.[^p7] | Sumin Han, Youngjun Park, Minji Lee, Jisun An, Dongman Lee |

## 교수와 전문 분야

이동만 교수는 서울대학교 컴퓨터공학 학사(1982), KAIST 전산학 석사(1984)·박사(1987) 학위를 받았다. 교수 소개는 Hewlett-Packard 선임연구원(1988–1997), KAIST 전산학부 부교수(1997–2003), 교수(2003–현재) 경력을 적는다. 연구 관심은 지능형 엣지 컴퓨팅, 분산 컴퓨팅, 어반 컴퓨팅, 소셜 컴퓨팅이다.[^pi] 구성원 쪽은 2025년 3월부터 KEPCO Chair Professor라고 소개하며, 전산학부 교수 명단의 직위 표기는 「KAIST교수」다.[^people][^faculty]

교수 소개에 게시된 최근 보직은 공과대학장(2021년 3월–2023년 2월), 교학부총장(Vice President for Academic Affairs, 2023년 3월–2024년 2월)이다. 연구에서는 분산 인프라의 자원 배분과 서비스 운영, 사람·기기의 상호작용 이해, 도시 활동 분석을 연결한다.[^pi][^p1][^p4][^p7]

## 응용 분야

- 스마트 공간: 사람 행동과 선호에 맞춰 조명·온도·가전 서비스를 조절하는 자동화.[^iot]
- 실시간 영상 분석과 모빌리티: 엣지 기기·서버의 영상 처리와 차량 간 협력 인지.[^p1][^p3]
- 도시 분석과 정책: 지역별 단기 임대시장 추세와 사람 활동을 반영한 교통 예측.[^p6][^p7]
- 공간 서비스: 환경 센서 자료를 자연어로 표현해 건물 운영과 이용자 서비스를 지원하는 연구.[^future]

## 구성원

2026년 10월 27일 People 페이지의 Researchers and Students에 게시된 8명이다. 과정과 연구 주제는 연구실 표기다. 대표 논문 참여는 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Thanh-Tung Nguyen | 박사과정 | Edge computing, AI Workload Distribution and Scheduling | 1, 2 |
| Lucas Liebe | 박사과정 | Edge Computing, Adaptive-Self-Learning Systems, Resource Allocation | 1, 2 |
| Yuheng Wu | 박사과정 | Edge Computing, Future Mobility Systems | 1, 2, 3 |
| Nhat Quang Tau | 석박사통합과정 | Edge-Cloud System, Foundation Model Serving | 1, 2, 3 |
| Chaemin Jang | 석사과정 | Large Language Models, Economics |  |
| Pablo Espinosa Campos | 석사과정 | Edge Networking, Federated Learning | 2 |
| Jaemo Jeong | 석사과정 | Multi-Modality Foundation Models, Human Activity Recognition | 4 |
| Junho Lee | 석사과정 | Contextual Marketing Analysis |  |

## 졸업생과 이전 구성원

Alumni 페이지의 박사 18행과 석사 58행이다. 학위별 재학 기간과 진로는 연구실 표기이며, 서로 다른 학위에 같은 이름이 반복될 수 있다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Wonyong Yoon | Ph.D. (1998 ~ 2002) | Dong-A University (Professor) |
| Dukyun Nam | Ph.D. (1999 ~ 2001 (M.S.); 2001 ~ 2006 (Ph.D.)) | KISTI |
| Yoo Chul Chung | Ph.D. (2005 ~ 2010.02) | Google Inc. (US) |
| Gonzalo Huerta-Canepa | Ph.D. (2004 ~ 2012.08) | Universidad Adolfo Ibáñez |
| In-kyung Choi | Ph.D. (2015.03 ~ 2018.02) | Hanyang University |
| Si Young Jang | Ph.D. (2016.03 ~ 2022.02) | Nokia Bell Labs (Cambridge, UK) |
| Mingyu Lim | Ph.D. (2000 ~ 2005) | Konkuk University (Professor) |
| Seunghyun Han | Ph.D. (2001 ~ 2008.02) | MIRALab, University of Geneva; LG Electronics |
| Kyungmin Lee | Ph.D. (2004 ~ 2010.02) | (주)프로그래머블텍스트 |
| Byoung-oh Kim | Ph.D. (2006.02 ~ 2008.08 (M.S); 2008.09 ~ 2015.02 (Ph.D)) | Samsung Electronics |
| Byoungheon Shin | Ph.D. (2010.03 ~ 2018.08) | Samsung Electronics |
| Sumin Han | Ph.D. (2018.03 ~ 2025.02) |  |
| Namgoong Han | Ph.D. (2000 ~ 2006) | ETRI |
| Seungik Lee | Ph.D. (2000 ~ 2002 (M.S); 2002 ~ 2009 (Ph.D)) | ETRI |
| Yangwoo Ko | Ph.D. (2004 ~ 2010.08) | (주)와이솔 |
| Soojeon Lee | Ph.D. (2012.03 ~ 2017.2) | ETRI |
| Heesuk Son | Ph.D. (2011.03 ~ 2019.02) | MIT (post-doc); Meta (Bellevue, WA) |
| Hyunju Kim | Ph.D. (2025.09 ~ 2018.02 (M.S.); 2018.03 ~ 2025.02 (Ph.D.)) | Kings College London (Post-Doc) |
| Jeonghwa Yang | M.S. (1998 ~ 2000) |  |
| Dongseon Park | M.S. (1999 ~ 2001) | LG Electronics (Senior Principal) |
| Sungju Park | M.S. (2000 ~ 2002) |  |
| Jeyoung Yu | M.S. (2001 ~ 2003) |  |
| Sunghoon Kim | M.S. (2002 ~ 2004) |  |
| Jaeik Lee | M.S. (2003 ~ 2006) |  |
| Sang Chul Moon | M.S. (2005 ~ 2007) | NHN |
| Jongmin Park | M.S. (2005 ~ 2007) |  |
| Jisun An | M.S. (2007 ~ 2009) | Cambridge University (Ph.D); Qatar Computing Research Institute; Singapore Management University |
| Hyunho Park | M.S. (2009 ~ 2011) |  |
| Alexander Boettcher | M.S. (2010 ~ 2012) |  |
| Namyong Kang | M.S. (2014 – 2016) | Samsung Electronics |
| Amine Lotfi Bourbia | M.S. (2014 – 2016) |  |
| Yoonhyung Lee | M.S. (2016 ~ 2018) | Samsung Electronics; Google Korea |
| Daekeun Lee | M.S. (2016 – 2018) | Satreci (쎄트렉아이) |
| Jeongwook Park | M.S. (2017 ~ 2019) | SkelterLabs (스캘터랩스) |
| Boyan Kostadinov | M.S. (2019 ~ 2021) | NetLight (Germany) |
| Sonia Sabir | M.S. (2022 ~ 2024) |  |
| Bae Hyeongchan | M.S. (2023 ~ 2025) |  |
| Hongju Lee | M.S. (2024 ~ 2026) |  |
| Bumho Kim | M.S. (2000 ~ 2001) |  |
| Eunhee Lee | M.S. (2000 ~ 2002) |  |
| Hyewon Shin | M.S. (2000 ~ 2003) |  |
| Mijin Choi | M.S. (2001 ~ 2003) |  |
| Soojeon Lee | M.S. (2003 ~ 2005) | ETRI |
| Haejun Lee | M.S. (2004 ~ 2006) |  |
| YoungRock Cha | M.S. (2005 ~ 2007) | LG Electronics |
| Sungil Kim | M.S. (2006 ~ 2008) | MagnaLAB |
| Kyungman Kwak | M.S. (2007 ~ 2009) | Camp Mobile (formerly NHN) |
| Ho Namkoong | M.S. (2009 ~ 2011) | S-Core |
| Seungwook Han | M.S. (2011 ~ 2013) | Korea Bank |
| Bjorn Tegelund | M.S. (2014 – 2016) | AWS (Canada) |
| Jiyoon Kang | M.S. (2015 – 2017) | KT |
| Hayoung Choi | M.S. (2017 – 2018) | 금융결제원 |
| Bumjin Kwak | M.S. (2016 – 2018) | TmaxSoft |
| Kinam Park | M.S. (2018 ~ 2020) | TmaxSoft (티맥스소프트); NHN |
| Sangwoo Kim | M.S. (2020 ~ 2022) | UpStage |
| Youngrae Kim | M.S. (2022 ~ 2024) | University of Southern California |
| Jinghan Cheng | M.S. (2023 ~ 2025) |  |
| Heejeong Kim | M.S. (1998 ~ 2001) |  |
| Sebon Ku | M.S. (2000 ~ 2002) |  |
| Euisuk Hong | M.S. (2001 ~ 2003) |  |
| Eunyoung Cho | M.S. (2001 ~ 2003) |  |
| Munseok Kim | M.S. (2002 ~ 2005) |  |
| Dong-un Yi | M.S. (2005 ~ 2007) | NHN |
| Myeong-a Yang | M.S. (2005 ~ 2007) | NHN |
| Hyunseok Jin | M.S. (2006 ~ 2008) | TTA |
| Jaesung Ku | M.S. (2008 ~ 2010) | Samsung Electronics |
| Taehyun Kim | M.S. (2010 ~ 2012) | Korea Bank |
| Thanh Nguyen | M.S. (2011 ~ 2013) |  |
| Jalil Abdullayev | M.S. (2013 ~ 2016) | AWS (Canada) |
| Junsung Lim | M.S. (2015 – 2017) | Amazon (Canada) |
| Hongmin Yang | M.S. (2017 ~ 2019) | Common Computer (커먼컴퓨터) |
| Minsang Yu | M.S. (2017 ~ 2019) |  |
| Dongmin Kim | M.S. (2018 ~ 2020) | Samsung Electronics |
| Kisoo Kim | M.S. (2020 ~ 2022) | LG Electronics |
| Younggeol Cho | M.S. (2022 ~ 2024) | Seoul National University |
| Junho Yoon | M.S. (2024 ~ 2026) |  |

## 최근 논문 목록 (2021–2026)

영상 분석의 분산 처리, 사람 행동 이해, 도시 활동과 공간 변화 예측을 다룬다. Publications의 2021–2026년 구역에서 40편을 싣는다. 연도는 연구실 연도 구역이며 제목·저자·발표처는 연구실 표기다. Forthcoming은 발표 예정, arXiv preprint는 사전 공개본 표기다.[^pubs]

**2026**

- Liebe, Lucas; Nguyen, Thanh-Tung; Tau, Nhat-Quang; Lee, Dongman. "CHEIS: Distributed Pipeline Optimization in Real-Time Inference Serving at the Edge". *In: ACM/IEEE Symposium on Edge Computing 2026, Forthcoming*.
- Woojin Park Chaemin Jang, Hyeok Yun. "In-Context Examples Suppress Scientific Knowledge Recall in LLMs". *In: Proceedings of the Conference on Language Modeling (COLM 2026), Forthcoming*.
- Tau, Nhat-Quang; Khai, Nguyen Do Pham; Nguyen, Thanh-Tung; Liebe, Lucas; Wu, Yuheng; Lee, Dongman. "INDUS: Efficient Long Video Reasoning using Context-aware Graph-based Knowledge Retrieval". *In: European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases (ECML-PKDD), Forthcoming*.
- Park, Youngjun; Na, Jihye; Jang, Keonhee; Lee, Dongman; Kwon, Changhyun; Yoon, Yoonjin. "Food Deserts in Context: How Site-Specific Factors Reshape Food Deserts Discussion". *In: npj Urban Sustainability, 2026 , ISSN: 2661-8001*.
- Espinosa-Campos, Pablo; Liebe, Lucas; Nguyen, Thanh-Tung; Tau, Nhat-Quang; Wu, Yuheng; Dongman, Lee. "ADAS-LORA: Efficient Federated LLM Tuning in Edge Systems by Decoupling Compute and Network". *In: 2026 IEEE 46th International Conference on Distributed Computing Systems Workshops (ICDCSW), pp. 1-6, IEEE, 2026 , ISBN: 979-8-3195-3647-1 , (Federated Foundation Models at the Edge Workshop)*.
- Yoon, Junho; Jeong, Jaemo; Kim, Hyunju; Lee, Dongman. "DETACH : Decomposed Spatio-Temporal Alignment for Exocentric Video and Ambient Sensors with Staged Learning". *In: jaemo jeong, (Ed.): Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 12860–12870, 2026*.
- Wu, Yuheng; Gao, Xiangbo; Tau, Quang; Tu, Zhengzhong; Lee, Dongman. "Background Fades, Foreground Leads: Curriculum-Guided Background Pruning for Efficient Foreground-Centric Collaborative Perception". *In: IEEE International Conference on Robotics & Automation, 2026*.

**2025**

- Cheng, Jinghan; Nguyen, Thanh-Tung; Liebe, Lucas; Wu, Yuheng; Tau, Nhat-Quang; Espinosa, Pablo; Lee, Dongman. "OctoCross: Workload-Aware Request Offloading Scheduling in Cross-Camera Collaboration". *In: Service-Oriented Computing, pp. 365–380, Springer Nature Singapore, 2025 , ISBN: 978-981-95-5012-8*.
- Kim, Hyunju; Lee, Dongman. "Self-supervised Dual-view Framework with Tailored Negative Sampling for New Activity Detection". *In: Proceedings of the 34th ACM International Conference on Information and Knowledge Management, pp. 1313–1323, Association for Computing Machinery, New York, NY, USA, 2025 , ISBN: 9798400720406*.
- Wu, Yuheng; Nguyen, Thanh-Tung; Liebe, Lucas; Tau, Nhat-Quang; Campos, Pablo Espinosa; Cheng, Jinghan; Lee, Dongman. "How2Compress: Scalable and Efficient Edge Video Analytics via Adaptive Granular Video Compression". *In: Proceedings of the 33rd ACM International Conference on Multimedia, pp. 12006–12015, Association for Computing Machinery, New York, NY, USA, 2025 , ISBN: 9798400720352*.
- Lee, S.; Park, S.; Yang, J.; Lee, Dongman; Kim, J.; Cha, M. "Slum Detection Beyond Labels: A Decade of Poverty Mapping Using Satellite Imagery and Minimal Ground Truth Data". *In: Proceedings of the 2025 International Conference on Information Technology for Social Good, pp. 41–46, Association for Computing Machinery, New York, NY, USA, 2025 , ISBN: 9798400720895*.
- Lee, S.; Kim, H.; Ahn, D.; Lee, D. G.; Kim, J.; Yun, H.; Jang, Chaemin; Jung, W.; Lee, Dongman. "Tracking Economic Disparities in North Korea: Satellite Imagery Analysis Using AI with Policy Insights". *In: Proceedings of the 2025 International Conference on Information Technology for Social Good, pp. 155–163, Association for Computing Machinery, New York, NY, USA, 2025 , ISBN: 9798400720895*.
- Lee, Hongju; Park, Youngjun; An, Jisun; Lee, Dongman. "Enhancing Regional Airbnb Trend Forecasting Using LLM-Based Embeddings of Accessibility and Human Mobility". *In: International Conference on Advances in Social Networks Analysis and Mining (ASONAM 2025), pp. 376–390, Springer Nature Switzerland, 2025 , ISBN: 978-3-032-13513-1*.
- Park, Sae Hyong; Shin, Seungjae; Ko, Namseok; Kim, Taeyeon; Lee, Dongman. "GymProxy: A lightweight Python wrapper for seamless integration of standalone simulators into Gymnasium environments". *In: Computers and Electrical Engineering, vol. 127, pp. 110634, 2025 , ISSN: 0045-7906*.
- Hong, Dasom; Han, Sumin; Park, Youngjun; An, Jisun; Lee, Dongman. "Measuring capital with spatial media: How online popularity on Instagram shapes land value patterns in Seoul". *In: Area, pp. e70037, 2025 , ISSN: 0004-0894*.
- Park, Youngjun; Bae, Hyungchan; An, Jisun; Lee, Dongman. "A Model for Monthly, Local-Level Airbnb Changes Using Public Dataset". *In: Proceedings of the 8th International Conference on Tourism Research, pp. 214-223, Academic Conferences International Ltd., 2025 , ISSN: 2516-3604*.
- Nguyen, Thanh-Tung; Liebe, Lucas; Tau, Nhat-Quang; Wu, Yuheng; Cheng, Jinghan; Lee, Dongman. "OCTOPINF: Workload-Aware Inference Serving for Edge Video Analytics". *In: The 23rd International Conference on Pervasive Computing and Communications (PerCom 2025), IEEE 2025*.

**2024**

- Kim, Youngrae; Cho, Younggeol; Nguyen, Thanh-Tung; Hong, Seunghoon; Lee, Dongman. "MetaWeather: Few-Shot Weather-Degraded Image Restoration". *In: European Conference on Computer Vision, pp. 206–222, Springer 2024 , ISBN: 978-3-031-73464-9*.
- Cho, Younggeol; Kim, Youngrae; Yoon, Junho; Hong, Seunghoon; Lee, Dongman. "Feature Augmentation based Test-Time Adaptation". *In: arXiv preprint arXiv:2410.14178, 2024*.
- Kim, Hyunju; Son, Heesuk; Lee, Dongman. "Causality-Aware Pattern Mining Scheme for Group Activity Recognition". *In: 2024 IEEE 48th Annual Computers, Software, and Applications Conference (COMPSAC), pp. 908–917, IEEE 2024 , ISSN: 2836-3795*.
- Park, Youngjun; Han, Sumin; Park, Doyoon; Bae, Hyeongchan; Thanh-Tung, Nguyen; Lee, Dongman. "Integrative Geospatial Visualization for Urban Mobility Analysis". *In: 한국정보과학회 학술발표논문집, pp. 402–404, 2024*.
- Elmoursi, Ahmad; Han, Sumin; Bae, Hyungchan; Park, Youngjun; Thanh-Tung, Nguyen; Lee, Dongman. "Enhancing Geospatial Recommendations through Natural Language Processing with Large Language Models". *In: 한국정보과학회 학술발표논문집, pp. 2215–2217, 2024*.
- Kim, Hyunju; Kim, Geon; Jain, Akanksha; Lee, Dongman. "Mobile Robot based Personalized Thermal Comfort Scheme". *In: 2024 21st International Conference on Ubiquitous Robots (UR), pp. 84–91, IEEE 2024 , ISBN: 979-8-3503-6107-0*.
- Kim, Hyunju; Kim, Geon; Lee, Taehoon; Kim, Kisoo; Lee, Dongman. "A dataset of ambient sensors in a meeting room for activity recognition". *In: Scientific Data, vol. 11, no. 1, pp. 516, 2024 , ISSN: 2052-4463*.

**2023**

- Cho, Younggeol; Kim, Youngrae; Lee, Dongman. "Beyond Entropy: Style Transfer Guided Single Image Continual Test-Time Adaptation". *In: arXiv preprint arXiv:2311.18270, 2023*.
- Han, Sumin; Park, Youngjun; Lee, Minji; An, Jisun; Lee, Dongman. "Enhancing Spatio-temporal Traffic Prediction through Urban Human Activity Analysis". *In: Proceedings of the 32nd ACM International Conference on Information and Knowledge Management, pp. 689–698, Association for Computing Machinery, New York, NY, USA, 2023 , ISBN: 9798400701245*.
- Kim, Geon; Kim, Hyunju; Kim, Youngjae; Lee, Dongman. "Exploring Technical Challenges for Thermal Sensation Estimation in Mobile Robot Driven Personalized Thermal Control". *In: 2023 20th International Conference on Ubiquitous Robots (UR), pp. 997–1002, IEEE 2023 , ISBN: 979-8-3503-3517-0*.
- Lee, Tae-Hoon; Kim, Hyunju; Lee, Dongman. "Transformer Based Early Classification for Real-Time Human Activity Recognition in Smart Homes". *In: Proceedings of the 38th ACM/SIGAPP Symposium on Applied Computing, pp. 410–417, Association for Computing Machinery, New York, NY, USA, 2023 , ISBN: 9781450395175*.
- Kim, Geon; Kim, Hyunju; Lee, Dongman. "Towards deployment of mobile robot driven preference learning for user-state-specific thermal control in a real-world smart space". *In: Proceedings of the 38th ACM/SIGAPP Symposium on Applied Computing, pp. 724–731, Association for Computing Machinery, New York, NY, USA, 2023 , ISBN: 9781450395175*.
- Nguyen, Thanh-Tung; Jang, Si Young; Kostadinov, Boyan; Lee, Dongman. "PreActo: Efficient Cross-Camera Object Tracking System in Video Analytics Edge Computing". *In: 2023 IEEE International Conference on Pervasive Computing and Communications (PerCom), pp. 101–110, IEEE 2023 , ISSN: 2474-249X*.
- Kim, Youngrae; Lim, Jinsu; Cho, Hoonhee; Lee, Minji; Lee, Dongman; Yoon, Kuk-Jin; Choi, Ho-Jin. "Efficient reference-based video super-resolution (ervsr): Single reference image is all you need". *In: 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), pp. 1828–1837, IEEE 2023 , ISSN: 2642-9381*.

**2022**

- Jang, Si Young; Park, Sung Kyu; Cho, Jin Hee; Lee, Dongman. "CARES: Context-aware trust estimation for realtime crowdsensing services in vehicular edge networks". *In: ACM Transactions on Internet Technology, vol. 22, no. 4, pp. 1–24, 2022 , ISSN: 1533-5399*.
- Kim, Kisoo; Kim, Hyunju; Lee, Dongman. "A Correlation-based Real-time Segmentation Scheme for Multi-user Collaborative Activities". *In: 2022 IEEE 46th Annual Computers, Software, and Applications Conference (COMPSAC), pp. 972–981, IEEE 2022 , ISBN: 978-1-6654-8810-5*.

**2021**

- Cho, Eunho; Yoon, Juyeon; Baek, Daehyeon; Lee, Dongman; Bae, Doo-Hwan. "Dnn model deployment on distributed edges". *In: International Conference on Web Engineering, pp. 15–26, Springer 2021 , ISBN: 978-3-030-92230-6*.
- Son, Heesuk; Lee, Dongman. "An Efficient Interaction Protocol Inference Scheme for Incompatible Updates in IoT Environments". *In: ACM Transactions on Internet Technology (TOIT), vol. 22, no. 2, pp. 1–25, 2021 , ISSN: 1533-5399*.
- Kim, Hyunju; Lee, Dongman. "ADELA: attention based deep ensemble learning for activity recognition in smart collaborative environments". *In: Proceedings of the 36th Annual ACM Symposium on Applied Computing, pp. 436–444, 2021 , ISBN: 9781450381048*.
- Lee, Seungho; Jang, Si Young; Hyun, Soon J; Lee, Dongman. "DQN-based coverage maximization for mobile video camera networks". *In: 2021 IEEE 18th Annual Consumer Communications & Networking Conference (CCNC), pp. 01–02, IEEE 2021 , ISBN: 978-1-7281-9794-4*.
- Jang, Si Young; Kostadinov, Boyan; Lee, Dongman. "Microservice-based edge device architecture for video analytics". *In: 2021 IEEE/ACM Symposium on Edge Computing (SEC), pp. 165–177, IEEE Computer Society 2021 , ISBN: 978-1-4503-8390-5*.
- Kim, Hyunju; Dongman. "AR-T: Temporal relation embedded transformer for the real world activity recognition". *In: International Conference on Mobile and Ubiquitous Systems: Computing, Networking, and Services, pp. 617–633, Springer 2021 , ISBN: 978-3-030-94821-4*.
- Kim, Hyunju; Lee, Dongman. "TAP: A Transformer based Activity Prediction Exploiting Temporal Relations in Collaborative Tasks". *In: 2021 IEEE International Conference on Pervasive Computing and Communications Workshops and other Affiliated Events (PerCom Workshops), IEEE 2021 , ISBN: 978-1-6654-0424-2*.

## 과제

2021년 10월 13일–2026년 10월 13일과 수행 기간이 겹치는 과제 5건이다. 기간과 지원기관은 연구실의 상세 과제 소개 표기다.[^starlab][^future][^urbanllm][^mobility][^drug]

- Self-Learning Based Core Technology Research for Autonomic IoT Edge Computing (기간 2019.04 ~ 2026.12 (8 years); 지원 MSIT (과학기술정보통신부))
- IoT Collaboration with Urban Spatiotemporal Context-Awareness (기간 2024.09-2027.12 (3 years); 지원 GS Construction & Engineering Co.)
- LLM-based Multimodal Spatiotemporal Urban Change Prediction (기간 2024.09-2026.08 (2 years); 지원 Ministry of Education of the Republic of Korea; National Research Foundation of Korea)
- Innovative Mobility and Planning for Advanced Connectivity and Traffic safety (기간 2023.12- ongoing (2+ years); 지원 PARTRON, Penta Systems Technology Inc., MQNIC, HL Klemove Corporation, & Hyundai NGV Tech Co., Ltd.)
- Drug Detection based on Human Action Recognition (기간 2024.07-2027.12 (4 years); 지원 Ministry of Science and ICT(MSIT))

## 수상과 선정

교수 소개에 게시된 해당 기간의 수상·선정 2건이다.[^pi]

- 2024-05 · KAIST 미래선도기술 연구성과 선정
- 2024-05 · KAIST Education Innovation Award

## 연락과 위치

- 교수 연구실: KAIST N1 IT Convergence Building 803호, 전화 +82-42-350-3559.[^people][^faculty]
- 연구원·학생 사무실: N1 IT Convergence Building 823호.[^people]
[^lab]: KAIST 전산학부, 「협동 분산 시스템 및 네트워크 연구실」. 스마트 객체 협업, 장소 의미·사용자 의도 파악, 강화학습·연합학습 기반 자원 재구성·배분·스케줄링을 연구한다고 적는다. <https://cs.kaist.ac.kr/research/labView?sn=64&menu=64> (관측 2026-10-27).
[^faculty]: KAIST 전산학부 교수 명단, 이동만 「KAIST교수」, N1 803, 에지컴퓨팅·어반컴퓨팅·유비쿼터스컴퓨팅. <https://cs.kaist.ac.kr/people/faculty> (관측 2026-10-27).
[^research]: CDSN, Research. Urban Space Robot은 사용자 의도에 맞춰 분산 IoT 에이전트의 협업을 조정하고 서비스를 재구성하며 사용자 선호를 학습하는 플랫폼이라고 설명한다. <https://cds.kaist.ac.kr/research/> (관측 2026-10-27).
[^edge]: CDSN, Context-Aware & Intelligent Systems For Edge Computing. 강화학습을 통한 엣지 서비스 설정 최적화, 상황 변화에 대한 실시간 적응, 경량 가상화를 연구 방향으로 제시한다. <https://cds.kaist.ac.kr/portfolio/service-aware-iot-virtualization-for-edge-computing/> (관측 2026-10-27).
[^iot]: CDSN, IoT-Based Self-Evolving Intelligent Automation System. 사람 행동과 선호에 맞춘 자동화, 다중 에이전트 조정과 분산 협력 학습, 기기 통합, 실시간 서비스를 연구한다고 설명한다. <https://cds.kaist.ac.kr/portfolio/template-research-area-iot/> (관측 2026-10-27).
[^people]: CDSN, People. 교수 소개와 Researchers and Students 8명, 과정·연구 주제·사무실. <https://cds.kaist.ac.kr/people/> (관측 2026-10-27).
[^alumni]: CDSN, Alumni. PhD Alumni 18행, Master Alumni 58행의 학위별 기간과 진로. <https://cds.kaist.ac.kr/people/alumni/> (관측 2026-10-27).
[^pi]: CDSN, Dongman Lee. 학력·경력·전문 분야·보직과 수상. <https://cds.kaist.ac.kr/people/dongmanlee/> (관측 2026-10-27).
[^pubs]: CDSN, Publications. 2021–2026년 연도 구역의 저자·제목·발표처와 게시 초록·BibTeX. <https://cds.kaist.ac.kr/publications/> (관측 2026-10-27).
[^starlab]: CDSN, Self-Learning based Autonomic IoT Edge Computing. 지원·기간·연구 목적. <https://cds.kaist.ac.kr/portfolio/starlab-2019/> (관측 2026-10-27).
[^future]: CDSN, GS & KAIST Future Urban AI Technology Research. 환경 센서에서 도시 문맥을 자연어로 추출하는 미들웨어 연구. <https://cds.kaist.ac.kr/portfolio/future-urban-ai-technology/> (관측 2026-10-27).
[^urbanllm]: CDSN, Urban Large Language Models (LLM). 인구 이동·교통 패턴·건물 이용을 포함한 여러 종류의 시공간 자료로 도시 변화를 예측하는 소프트웨어 연구. <https://cds.kaist.ac.kr/portfolio/urban-llm/> (관측 2026-10-27).
[^mobility]: CDSN, Deep Mobility Consortium. 과제 주제·지원기관·기간. <https://cds.kaist.ac.kr/portfolio/deep-mobility-consortium/> (관측 2026-10-27).
[^drug]: CDSN, Drug detection Project. Human Action Recognition 기반 Drug Detection 과제의 지원기관·기간. <https://cds.kaist.ac.kr/portfolio/drug-detection-project/> (관측 2026-10-27).
[^p1]: T.-T. Nguyen 외, D. Lee, The 23rd International Conference on Pervasive Computing and Communications (PerCom 2025) (2025). <https://doi.org/10.1109/PerCom64205.2025.00032> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://cds.kaist.ac.kr/publications/> (관측 2026-10-27).
[^p2]: P. Espinosa-Campos 외, D. Lee, 2026 IEEE 46th International Conference on Distributed Computing Systems Workshops (ICDCSW), 1-6 (2026). <https://doi.org/10.1109/ICDCSW72724.2026.00056> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://cds.kaist.ac.kr/publications/> (관측 2026-10-27).
[^p3]: Y. Wu 외, D. Lee, arXiv (2025). <https://doi.org/10.48550/arXiv.2510.19250> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2510.19250> (관측 2026-10-27).
[^p4]: J. Yoon, J. Jeong, H. Kim, D. Lee, Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 12860--12870 (2026). <https://openaccess.thecvf.com/content/CVPR2026/html/Yoon_DETACH__Decomposed_Spatio-Temporal_Alignment_for_Exocentric_Video_and_Ambient_CVPR_2026_paper.html> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://cds.kaist.ac.kr/publications/> (관측 2026-10-27).
[^p5]: H. Kim, D. Lee, Proceedings of the 34th ACM International Conference on Information and Knowledge Management, 1313–1323 (2025). <https://doi.org/10.1145/3746252.3761163> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://cds.kaist.ac.kr/publications/> (관측 2026-10-27).
[^p6]: H. Lee, Y. Park, J. An, D. Lee, International Conference on Advances in Social Networks Analysis and Mining (ASONAM 2025) 16322, 376--390 (2025). <https://doi.org/10.1007/978-3-032-13513-1_30> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://cds.kaist.ac.kr/publications/> (관측 2026-10-27).
[^p7]: S. Han 외, D. Lee, Proceedings of the 32nd ACM International Conference on Information and Knowledge Management, 689–698 (2023). <https://doi.org/10.1145/3583780.3614867> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://cds.kaist.ac.kr/publications/> (관측 2026-10-27).

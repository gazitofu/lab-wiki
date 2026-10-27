# 고급지능시스템 연구실 (Advanced Intelligent Systems Lab, AiSLab)

**서울대학교 공과대학 전기·정보공학부 · 양현종 부교수**

- 분야: 무선·이동통신과 인공지능의 결합(AI 네이티브 무선 접속망, 채널 정보의 학습 기반 압축·예측, 언어 모델을 쓰는 통신), 무선 에지의 분산 학습과 계산 오프로딩, 통신과 센싱의 통합(ISAC), 네트워크로 연결된 다중 로봇 협업
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 무선·이동통신[^prof][^p1][^p6], 대형 언어 모델[^ecelabv][^p3], 네트워크 보안·프라이버시[^research][^p7], 다중 로봇 협업·물류 자동화[^research][^p8], 엣지 컴퓨팅·엣지 AI[^research], 연합학습·분산 학습[^research], 다중 에이전트 시스템·분산 의사결정[^research]
- 홈페이지: <https://aislab.snu.ac.kr/>
- 근거와 출처: [AiSLab 근거 페이지](aislab-sources.md)

> 6G 무선 통신과 인공지능, 로보틱스를 함께 다뤄, 인공지능으로 움직이는 무선 접속망, 무선 에지의 분산 학습, 통신과 센싱의 통합, 네트워크로 연결된 로봇의 협업을 연구하는 연구실이다.[^research][^ecelabv]

## 무엇을 연구하나

연구실은 서울대학교 전기·정보공학부 양현종 부교수가 이끄는 연구실이다.[^ecefac][^eceprof] 학부 연구실 목록은 이름을 「고급지능시스템 연구실」로 적고, 인공지능 및 머신러닝, 통신 네트워크, 통신 시스템 세 연구그룹에 함께 올린다.[^ecelab] 누리집은 Advanced Intelligent Systems Lab(AiSLab)으로 적는다.[^home] 교수 소개는 연구실이 무선 통신과 인공지능의 결합에 초점을 두며, 핵심 관심사로 AI 네이티브 무선 접속망(AI-RAN, 설계 단계부터 인공지능을 넣어 운영하는 무선 접속망), 통신-센싱 통합(ISAC, 같은 전파와 장비로 데이터를 주고받으면서 주변 물체의 위치·속도 같은 정보도 감지하는 기술), 로봇처럼 네트워크로 연결된 시스템을 위한 분산 기계학습을 든다고 적는다.[^prof] 무선 접속망(RAN)은 휴대폰 같은 단말과 기지국 사이를 전파로 잇는 이동통신망의 부분이다. Research 페이지는 6G(5G 다음 세대의 이동통신) 무선 통신, 인공지능, 로보틱스를 하나로 묶어 미래의 지능형 인프라를 만드는 것을 목표로 내세운다.[^research]

연구실은 2014년 9월 UNIST에서 시작해 2020년 7월 POSTECH으로, 2024년 9월 서울대 전기·정보공학부로 옮겼고, 2025년 8월에는 서울대 뉴미디어통신공동연구소(NMRI)에도 소속을 두었다.[^events][^cv] 학부 연구실 상세 페이지는 연구실을 「지능형 통신 및 시스템 연구실(AISLab)」로 소개하며, 차세대 통신 시스템과 지능형 연결 시스템의 혁신을 목표로 이론과 실제 구현을 함께 다룬다고 적는다.[^ecelabv]

첫째 갈래는 **AI 네이티브 무선 접속망과 무선 파운데이션 모델**이다. Research 페이지는 사람이 높은 수준에서 밝힌 의도(intent)를 실시간 네트워크 동작으로 바꾸는 무선 접속망 지능을 설계한다고 적는다. 의도를 해석하는 대형 멀티모달 모델(Intent LMM, 글뿐 아니라 여러 종류의 자료를 함께 다루는 큰 인공지능 모델)이 운영자 입력을 해석해 O-RAN(무선 접속망의 구성 요소와 연결 방식을 공개 규격으로 정한 구조)의 RIC(무선 접속망을 소프트웨어 앱으로 감시하고 제어하는 장치) 위 제어 앱들을 조율하고, 자연어를 구조화된 네트워크 정책으로 바꾸며, 수요가 몰리기 전에 자원을 미리 나누고, NVIDIA Sionna와 Aerial 같은 GPU(많은 계산을 동시에 처리하는 그래픽 처리 장치) 가속 도구로 신뢰성 높은 서비스를 만든다고 소개한다.[^research] 학부 연구실 상세 페이지는 디지털 트윈(실제 환경을 컴퓨터 안에 재현한 모형)과 실제 채널 데이터를 합쳐 전파 환경을 예측하는 무선 파운데이션 모델(많은 데이터로 미리 학습해 여러 과제에 고쳐 쓰는 큰 인공지능 모델)을 개발하고, 대규모 언어 모델(LLM)을 통신 계층에 접목해 스스로 최적화하는 통신 구조를 연구한다고 적는다.[^ecelabv] 대표 논문에서는 시간에 따라 변하는 채널을 예측해 채널 상태 정보(CSI, 송신기와 수신기 사이 전파 경로가 신호를 어떻게 바꾸는지 나타낸 정보) 피드백 없이 참조 신호(수신 측이 채널을 추정하도록 미리 약속해 보내는 신호) 배치를 정하는 방법을 제안했고,[^p1] 환경이 바뀐 직후 단말이 새 표본으로 압축용 코드북을 다시 만들어 기지국에 한 번에 알리는 CSI 피드백 방법을 만들었으며,[^p2] 글의 일부 글자만 보내고 빠진 글자를 수신 측의 대형 언어 모델이 되살리는 글 전송 방법을 제안했다.[^p3]

둘째 갈래는 **분산 학습과 무선 에지 지능**이다. Research 페이지는 배터리가 한정된 무선 에지(사용자 가까이 있는 기지국·서버 같은 망 가장자리) 시스템을 위한 분산 학습을 연구한다고 적는다. 기기들이 자기 데이터로 가벼운 모델을 갱신하고 프라이버시를 지키는 매개변수만 중앙 서버와 나누며, 신경망 계산을 기기와 에지 서버가 나눠 맡는 분할 컴퓨팅(split computing)에서 두 쪽의 계산 능력을 함께 최적화하고, 실시간 채널 상태에 따라 작업을 넘기며, 원래 데이터를 나누지 않고 모델을 안전하게 갱신한다고 소개한다.[^research] 학부 연구실 상세 페이지는 이 갈래에서 연산 오프로딩(기기가 할 계산을 가까운 서버에 넘겨 처리하게 하는 일)과 통신 효율을 높이는 연합 학습(기기들이 데이터를 내보내지 않고 각자 학습한 모델 갱신만 서버와 나눠 함께 모델을 만드는 방법)에 집중한다고 적는다.[^ecelabv] 대표 논문에서는 통신 신호가 공중에서 겹쳐 더해지는 성질을 쓰는 연합 학습에서 기기가 보내는 값을 몇 개의 숫자로 줄이는 방법 Fed-ZOE를 제안했고,[^p4] 모바일 에지 컴퓨팅에서 통신 지연, 계산 지연, 배터리 사용을 함께 줄이도록 작업 오프로딩과 자원 할당, 사용자 연결을 분산 방식으로 정하는 방법을 만들었다.[^p5]

셋째 갈래는 **통신과 센싱의 통합(ISAC)**이다. 학부 연구실 상세 페이지는 무선 통신 신호로 주변 환경을 정밀하게 감지하는 센싱 기술과 통신 기능을 하나의 시스템으로 묶는 연구를 하며, 이를 6G 시대 자율주행과 환경 인지의 핵심 기술로 본다고 적는다.[^ecelabv] 교수 CV는 6G 무선 통신 연구의 초점으로 초고속 연결, 지능형 반사 표면(IRS, 전파의 반사를 조절하도록 설정을 바꿀 수 있는 표면), 새 주파수 기술, ISAC를 든다.[^cv] 대표 논문에서는 송수신기나 표적이 움직일 때 전파의 주파수가 바뀌는 도플러 효과가 OFDM(데이터를 여러 주파수에 나눠 싣는 전송 방식) 센싱 신호를 흐리는 문제를 물리 모형에서 끌어낸 보정 필터와 신경망으로 줄이는 DCFNet을 제안했고,[^p6] 전파를 반사하면서 동시에 통과시키도록 설정을 바꾸는 표면(STAR-RIS) 여러 개를 써서 표적 감지 조건과 기밀 정보 누출 한도를 지키며 통신 전송률을 높이는 빔포밍(여러 안테나의 신호를 조절해 전파를 원하는 방향으로 모으는 기술) 설계를 내놓았다.[^p7]

넷째 갈래는 **네트워크로 연결된 협력 로봇**이다. Research 페이지는 로봇이 즉각적인 안전을 위해 기기 안에서 빠른 제어를 하고, 에지 서버의 대형 멀티모달 모델(Edge LMM)이 여러 로봇의 원격 측정 자료를 모아 전체 계획을 세우는 두 단계 지능 구조를 구현한다고 적는다. 이 모델이 로봇 무리 전체의 혼잡과 경로 충돌을 그때그때 풀어, 규모가 큰 로봇 무리를 효율적이고 믿을 만하게 조율한다고 소개한다.[^research] 학부 연구실 상세 페이지는 6G 통신을 바탕으로 수십 대의 로봇이 실시간으로 정보를 주고받으며 협력하는 시스템을 만들고, 에지 서버의 큰 모델로 로봇 군집의 이동 경로를 최적화하고 혼잡을 관리하는 기술에 집중한다고 적는다.[^ecelabv] 교수가 1저자인 개관 논문은 멀티모달 대형 언어 모델의 안내 아래 센싱, 통신, 계산을 함께 설계해 여러 로봇의 협업을 이루는 방법을 정리하고 네 가지 시연을 보였다.[^p8]

Information 페이지는 연구실이 쓰는 도구로, GPU 가속 광선 추적(전파가 퍼지는 경로를 따라가며 반사와 가림을 계산하는 모의 방법)으로 도시 환경을 3차원으로 재현해 전파가 건물에 반사되고 장애물에 가리는 모습을 실시간으로 모의하는 NVIDIA Aerial Digital Twin(AoDT), 복잡한 물리를 미분 가능한 코드로 바꿔 딥러닝과 통신 이론을 잇는 오픈소스 라이브러리 NVIDIA Sionna, NVIDIA GPU에서 도는 소프트웨어 정의 라디오(SDR, 송수신 신호 처리를 전용 회로 대신 소프트웨어로 하는 무선 장치) 스택 cuPHY·cuMAC, 여러 로봇이 6G 네트워크로 정보를 나누도록 돕는 로봇 운영 체제 ROS 2를 든다.[^info] 연구실 자체 교육 과정은 신호와 시스템·통신 시스템, 수학적 최적화 이론, 강화학습·그래프 신경망·대형 언어 모델을 포함한 최신 딥러닝과 AI 네이티브 통신으로 이루어지며, 진행 중인 과제와 실제 구현에 바로 쓰도록 짰다고 적는다.[^info]

## 주요 연구 주제

### 1. AI 네이티브 무선 접속망과 언어 모델

의도를 해석하는 대형 멀티모달 모델로 무선 접속망을 제어하는 구조, 채널 예측 기반 참조 신호 배치, 환경 변화에 바로 맞추는 CSI 피드백 압축, 대형 언어 모델로 빠진 글자를 되살리는 글 전송.[^research][^p1][^p2][^p3] 대표 논문 1–3.

### 2. 분산 학습과 에지 지능

공중에서 신호가 겹쳐 더해지는 성질을 쓰는 연합 학습의 통신량 줄이기(Fed-ZOE), 지연과 배터리를 함께 고려하는 에지 작업 오프로딩, 프라이버시를 지키는 모델 갱신.[^research][^p4][^p5] 대표 논문 4, 5.

### 3. 통신과 센싱의 통합(ISAC)

다중 사용자 MIMO-OFDM 시스템의 도플러 간섭 보정(DCFNet), 여러 STAR-RIS로 돕는 보안 ISAC 빔포밍.[^ecelabv][^p6][^p7] 대표 논문 6, 7.

### 4. 네트워크로 연결된 협력 로봇

에지 서버의 대형 멀티모달 모델로 로봇 무리의 경로와 혼잡을 조율하는 두 단계 구조, 센싱·통신·계산을 함께 설계하는 다중 로봇 네트워크.[^research][^p8] 대표 논문 8.

## 대표 논문

양현종 교수가 서울대에 부임한 2024년 9월 뒤 학술지에 실린 논문 가운데 교수가 교신저자(랩 목록의 * 표시)이거나 1저자이고 초록을 구할 수 있는 논문을 네 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [Standards-Compliant DM-RS Allocation via Temporal Channel Prediction for Massive MIMO Systems](https://doi.org/10.1109/tvt.2026.3654149) · IEEE Transactions on Vehicular Technology | 5G 다음 세대 네트워크에서는 채널 상태 정보(CSI)를 단말이 기지국에 알려 주는 피드백 부담을 줄이는 일이 중요한 과제다. 기지국에 많은 안테나를 다는 대규모 MIMO에서는 안테나 수가 늘면서, 올림과 내림 통신에 다른 주파수를 쓰는 FDD 방식의 CSI 피드백 요구가 크게 늘었다. 신경망 기반 CSI 압축·예측 연구가 활발하고 3GPP(이동통신 국제 표준 단체) 5G-Advanced 표준 반영도 검토되지만, 이런 제약 아래의 참조 신호 배치는 상대적으로 덜 연구되었다. 그래서 채널 예측과 DM-RS(데이터를 풀어내는 데 쓰는 참조 신호) 배치를 함께 최적화해 CSI 피드백 없이 데이터 처리량을 높이는 개념 CPRS를 내놓고, 시간에 따라 변하는 CSI 행렬을 이미지처럼 이어진 자료로 다루는 ViViT/CNN 기반의 표준 호환 구조로 구현했다. NVIDIA Sionna의 광선 추적 기반 모의실험에서 비교 전략보다 처리량을 최대 36.60% 높였다.[^p1] | 1저자 Sehyun Ryu, 교신저자 양현종 |
| 2 | 2026 | [Compressed-CSI Feedback With Near Real-Time Domain Adaptation](https://doi.org/10.1109/tcomm.2026.3698862) · IEEE Transactions on Communications | 채널이 시간에 따라 바뀌는 조건에서 쓰는, 미리 학습할 필요가 없는 가벼운 압축 CSI 피드백 방법을 제안했다. 기존 딥러닝 방법은 환경이 바뀌면 성능이 떨어지고 단말에서 다시 학습하는 데 비용이 크다. 제안 방법에서는 환경이 바뀐 직후 짧은 구간에 모은 새 CSI 표본으로 단말이 성긴 선형 코드북(신호를 압축해 나타내는 기준 벡터 모음)을 스스로 다시 만들고, 이를 적은 신호 부담으로 한 번에 기지국에 보낸다. 여러 평가에서 대표적인 환경 변화 뒤의 CSI 불일치를 크게 줄이고 스펙트럼 효율을 회복했으며, 몇몇 대표 운영 조건에서는 완전한 CSI를 가정한 기준에 가깝게 동작했다. CSI 불일치가 실제 처리량에 주는 영향은 운영 모드에 따라 크게 달라, 복원 오차만이 아니라 시스템 수준 평가가 필요하다는 점도 보였다.[^p2] | 공동 1저자 Hosung Joo·Seungmin Choi, 교신저자 양현종 |
| 3 | 2026 | [Robust Transmission of Punctured Text With Large Language Model-Based Recovery](https://doi.org/10.1109/tvt.2025.3595593) · IEEE Transactions on Vehicular Technology | 딥러닝의 발전으로 과제에 필요한 특징만 보내는 의미 통신이 빠르게 떠올랐지만, 특징 추출이 학습 모델에 기대므로 성능이 학습 데이터나 과제에 좌우된다. 실제 상황에는 데이터나 과제와 관계없이 고르게 동작하는 모델이 필요하다. 그래서 글에서 일부 글자만 골라 보내고 빠진 글자는 수신 측의 대형 언어 모델(LLM)이 되살리는 새 글 전송 모델과, LLM의 복원 성능이 좋아지도록 보낼 글자를 고르는 중요 글자 추출기 ICE를 제안했다. 모의실험에서 ICE가 고른 글자는 무작위로 고른 글자보다 나은 결과를 냈고, 제안 모델은 여러 데이터와 과제에서 고른 성능을 보였으며 신호 대 잡음비가 낮은 조건에서 기존 통신 방식보다 나았다.[^p3] | 1저자 Sojeong Park, 교신저자 양현종 |
| 4 | 2026 | [Fed-ZOE: Communication-Efficient Over-the-Air Federated Learning via Zeroth-Order Estimation](https://doi.org/10.1109/jsac.2026.3739217) · IEEE Journal on Selected Areas in Communications | 6G 이후 네트워크가 복잡해지면서, 흩어진 에지 데이터를 안전하고 효율적으로 인공지능에 쓰는 연합 학습이 꼭 필요한 방식으로 떠오른다. 통신 신호가 겹쳐 더해지는 성질을 쓰는 공중 합산 연합 학습(OtA-FL)은 기기 수와 관계없이 통신 부담이 일정하지만, 보내는 심볼(전파에 실어 보내는 신호 단위) 수가 학습할 매개변수 수와 같아 신경망 학습에는 여전히 통신 비용이 크다. 기울기(학습에서 모델을 고칠 방향을 알려 주는 값)를 압축하거나 일부만 보내는 방법은 겹쳐 더해지는 성질을 깨뜨려 OtA-FL과 맞지 않는다. 0차 최적화(기울기를 직접 계산하지 않고 함숫값으로 추정하는 최적화)의 무작위 기울기 추정(RGE)에서 착안한 Fed-ZOE에서는, 기기가 보통의 연합 학습처럼 자기 모델을 갱신한 뒤 전체 기울기 벡터 대신 모델 갱신 벡터와 무작위 벡터의 내적 몇 개만 보내고, 매개변수 서버가 이 값으로 기울기를 재구성한다. 겹쳐 더해지는 성질을 지키면서 부담을 크게 줄이는 방식이다. ResNet-18로 CIFAR-10, Tiny-ImageNet, SVHN, CIFAR-100, Brain-CT 데이터셋에서 평가해 기존 OtA-FL과 비슷한 성능을 내면서 통신·계산 부담을 기존 방식의 9%까지 줄였다.[^p4] | 1저자 Jonggyu Jang, 교신저자 양현종 |
| 5 | 2024 | [Distributed Task Offloading and Resource Allocation for Latency Minimization in Mobile Edge Computing Networks](https://doi.org/10.1109/tmc.2024.3458185) · IEEE Transactions on Mobile Computing | 인공지능 기술이 커지면서 모바일 에지 컴퓨팅(MEC)에서 서비스 지연을 줄이는 작업 오프로딩이 관심을 끌고, 기기 배터리가 한정된 문제도 함께 생긴다. 이 논문은 사용자 연결, 자원 할당, 작업 전체의 오프로딩, 기기 배터리를 함께 고려하는 지연 인지 분산 작업 오프로딩 최적화를 다뤘다. 통신 지연, 계산 지연, 배터리 사용을 모두 목적 함수에 넣은 NP-난해(정확한 해를 효율적으로 구하는 방법이 알려지지 않은 문제 계열) 조합 최적화 문제를 세우고, 자원 할당의 닫힌 형태 해(식으로 바로 계산되는 해)와 가격 기반 분산 사용자 연결 해를 냈다. 여러 자원 집약 작업으로 모의실험한 결과 제안 방법은 비교 방법들을 파레토 우위(어느 기준에서도 뒤지지 않으면서 적어도 한 기준에서 앞섬)로 앞섰고, 지연은 1.62배 짧고 에너지 소비는 41.2% 적었다.[^p5] | 공동 1저자 Minwoo Kim·Jonggyu Jang, 교신저자 양현종 |
| 6 | 2026 | [DCFNet: Doppler Correction Filter Network for Integrated Sensing and Communication in Multi-User MIMO–OFDM Systems](https://doi.org/10.1109/twc.2026.3687605) · IEEE Transactions on Wireless Communications | 통신-센싱 통합(ISAC)은 다가올 IMT-2030과 6G의 대표 기능이지만, 기존 OFDM 계열 안에서 쓸 구체적 해법은 아직 열린 문제다. 도플러 효과로 생기는 부반송파(OFDM에서 데이터를 나눠 싣는 각 주파수) 간 간섭(ICI)이 OFDM 센싱 신호의 부반송파 직교성(서로 간섭하지 않는 성질)을 깨뜨려 거리-속도 지도를 흐리고 센싱 정확도를 떨어뜨린다. 다중 사용자 MIMO-OFDM 시스템에서 센싱 성능 조건을 지키며 다중 사용자 통신 합 전송률이 가장 커지도록 송수신 빔포밍을 함께 최적화하고 도플러 간섭을 줄이는 모델 기반 ISAC 틀을 세웠다. 그 핵심인 AI 네이티브 ISAC 모델 DCFNet에서는 도플러 물리에서 끌어낸 보정 필터 묶음이 주된 간섭 성분을 옮기고 억제한 뒤, 심층 신경망이 남은 간섭을 지워 깨끗한 레이더 센싱 영상을 만든다. 기존 프레임 구조를 바꾸지 않고 적은 복잡도로 세밀한 거리-속도 추정을 한다. 일반화 우도비 검정(GLRT)으로 표적 추정을 격자 한 칸보다 세밀하게 다듬는 DCFNet-LR도 제안했다. 모의실험에서 DCFNet-LR은 최대우도 탐색보다 143배 빨랐고, 기존 검출 방법보다 거리·속도 추정 오차를 줄여 성능이 크게 앞섰다.[^p6] | 1저자 Hyeonho Noh, 교신저자 양현종 |
| 7 | 2026 | [Multiple Active STAR-RIS-Assisted Secure Integrated Sensing and Communication via Cooperative Beamforming](https://doi.org/10.1109/jiot.2026.3719367) · IEEE Internet of Things Journal | 여러 개의 능동형 STAR-RIS가 돕는 통신-센싱 통합 사물인터넷(IoT) 망을 다뤘다. 기지국이 여러 IoT 기기에 내림 통신을 하면서 동시에 표적 하나를 센싱한다. 센싱 신호 대 간섭·잡음비(SINR) 요구, 기밀 정보가 새는 양의 상한, 기지국과 STAR-RIS의 하드웨어·전체 전력 제약을 지키면서 통신 합 전송률이 가장 커지도록 기지국의 송신 빔포밍과 각 STAR-RIS의 반사·투과 계수를 함께 최적화했다. 매우 비볼록한 이 문제를 교대 최적화 틀로 풀었는데, 문제를 다루기 쉬운 같은 꼴로 바꿔 나눈 뒤, 기지국 빔포밍은 KKT 조건(최적해가 만족해야 하는 수학 조건)으로 닫힌 형태로 갱신하고 STAR-RIS의 반사·투과 벡터는 연속 볼록 근사(SCA)와 반정치 완화(SDR)로 다듬는다. 모의실험에서 수동형 RIS와 STAR-RIS 하나만 쓰는 기준보다 합 전송률을 크게 높이면서 센싱·보안 조건을 지켰다.[^p7] | 1저자 Hyeonho Noh, 교신저자 양현종 |
| 8 | 2026 | [Advancing Multi-Robot Networks via MLLM-Driven Sensing, Communication, and Computation: A Comprehensive Survey](https://doi.org/10.1109/comst.2026.3683120) · IEEE Communications Surveys & Tutorials | 멀티모달 대형 언어 모델(MLLM)로 움직이는 로봇이 자기 센서뿐 아니라 이웃 드론·자율주행차·수중 이동체의 센싱 자료까지 실시간으로 해석하는 가까운 미래를 내다본다. 실제 임무에는 여러 로봇의 전체 조율이 필요하고 방대한 센서 정보를 나눠 해석해야 하므로 통신이 꼭 필요하지만, 수십·수백 대 로봇의 센서 자료를 모두 보내면 망이 감당하기 어렵다. 자연어로 받은 높은 수준의 지시에서 목표를 이해하면 필요한 센싱만 켜고 통신 대역을 배분하며 계산 위치를 정할 수 있다는 「의도에서 자원으로」 연결을 핵심 동기로 삼는다. 이 개관 논문은 라이다부터 초분광 영상까지의 센싱 방식과 의미·부분 압축, 저지연 프로토콜·에지 기반 조율·적응형 자원 할당 같은 통신 전략, 분산·혼합·중앙 집중 계산 방식을 차례로 살핀다. 디지털 트윈 창고 주행, 지연된 피드백 아래의 이동성 기반 MCS(변조 방식과 부호율의 조합) 제어, 와이파이 위에서 실용적인 의미 센싱 전환을 쓰는 실제 FollowMe 로봇, 실제 하드웨어로 한 열린 어휘 쓰레기 분류 네 가지 시연도 보였다.[^p8] | 1저자 양현종 |

## 교수와 전문 분야

양현종 교수(Hyun Jong Yang)는 서울대학교 전기·정보공학부 부교수이다.[^ecefac][^eceprof] 누리집 교수 소개는 소속을 Advanced Intelligent Systems Lab, New Media Communications Research Institute(NMRI), Department of Electrical and Computer Engineering으로 적는다.[^prof] KAIST 전기 및 전자공학과에서 학사(2004), 석사(2006), 박사(2010) 학위를 받았다.[^eceprof] CV는 석사 논문을 「Symbol Detection Under Channel Uncertainties for MIMO Systems」로, 박사 논문을 「Development and Performance Analysis of Algorithms for Wireless Relay and Limited-Feedback Communications Systems」로 적는다.[^cv]

CV의 경력은 Stanford University 전기공학과(Dept. of Electrical Engineering) 방문 대학원생(2009년 9월–2010년 3월), Korea Research Institute of Ships and Ocean Engineering(KRISO) 박사후연구원(2010년 9월–2011년 11월, CV 표기 Military Duty Service), Stanford University 전기공학과 박사후연구원(2011년 12월–2012년 10월), 미국 Broadcom Corp.의 Staff II, Systems Design Engineer(2012년 10월–2013년 9월), UNIST 조교수·부교수(2013년 9월–2020년 7월), POSTECH 부교수(2020년 7월–2024년 8월), 서울대 전기·정보공학부 부교수(2024년 9월–)다.[^cv] Broadcom에서는 물리 계층(신호를 전파에 싣고 받는 일을 맡는 통신의 가장 아래 층) 알고리즘 설계를 이끌고 3GPP RAN1(3GPP의 물리 계층 작업반) 대표로 참여했으며,[^prof] 2012–2013년의 3GPP 기고 세 건이 연구실 목록에 있다.[^pubs] 2016년 9월–2020년 7월에는 EgoVid Inc.를 세워 대표·기술 책임자로서 인공지능으로 제어하는 주사전자현미경(SEM)과 프라이버시를 지키는 딥러닝 기술을 개발했다고 CV는 적는다.[^cv] 학부 교수 소개는 같은 경력을 스탠포드 대학교 박사 후 연구원(2011), 브로드컴 시스템 엔지니어(2012~2013), 울산과학기술원 전기전자컴퓨터공학부 조교수·부교수(2013~2020), 포항공과대학교 전자전기공학과 부교수(2020~2024), 서울대학교 전기정보공학부 부교수(2024~현재)로 적는다.[^eceprof]

교수는 IEEE Senior Member이다.[^prof] CV에 따르면 IEEE Transactions on Vehicular Technology와 IEEE Transactions on Communications의 Editor(2026–), IEEE Internet of Things Journal의 Editor(2024년 10월–), IEEE Wireless Communications Letters의 Editor(2023년 1월–)를 맡고 있고, 한국통신학회 논문지(J-KICS) Associate Editor-in-Chief(2023–2024), EURASIP Journal on Advances in Signal Processing의 Guest Editor(2021), Journal of Communications and Networks(JCN)의 AI-RAN 특집호 Guest Editor-in-Chief(2026)를 맡았다.[^cv] 학회 활동으로는 IEEE ComSoc Asia Pacific Board의 Information Services Committee Vice Chair(2026년 1월–2027년 12월), 6G 포럼 서비스위원회 위원(2025–2026), 한국통신학회(KICS) Executive Director를 적고, 학술대회 쪽으로는 ICEIC 2027의 Technical Program Committee Co-Chair, IEEE ITW 2027과 IEEE ISIT 2028의 Local Arrangements Co-Chair, IEEE CCNC의 Program Track Chair(2023–2027), ICCE-Asia 2025의 Organizing Committee Co-Chair를 적는다.[^cv] 서울대에서는 3차원모빌리티통신센터 소장(2026년 5월–2028년 12월)을 맡고, 한국연구재단 국책연구본부 정보·융합기술분야 전문위원(2024년 9월–2026년 8월, CV 표기 그 뒤 임기 연장)이다.[^cv] 서울대에서 새로 만든 과목으로 확률신호론(Probability and Random Processes)과 Modern Neural Networks for Communications를 든다.[^cv] 연구실 소식에 따르면 2026년 2월 IEEE Transactions on Communications, 3월 IEEE Transactions on Vehicular Technology의 Editor로 임명되었다.[^home] CV의 수상은 2021년 이전의 Excellent Research Performance Award(KAIST, 2007)와 Outstanding Faculty Award(UNIST, 2019), 그 뒤 지도 학생과 함께 받은 상(아래 「수상」 절)과 ICTC 2025의 Distinguished TPC Award다.[^cv]

학부 교수 소개는 전공을 통신 시스템, 병렬 신호처리, 분산 학습 시스템으로, 분야를 통신 시스템, 분산 학습 시스템, 커넥티드 로보틱스로, 연구 관심을 유무선 통신 시스템, 분산 학습 시스템, 커넥티드 로봇 시스템으로 적는다.[^eceprof] CV의 현재 연구 관심은 AI-RAN, 6G 무선 통신(지능형 반사 표면, 새 주파수 기술, ISAC), 분산 학습과 모바일 에지 컴퓨팅(지연을 고려한 작업 오프로딩, 가격 기반의 사용자 연결·자원 할당, 배터리가 한정된 기기의 에너지 효율 자원 관리), 커넥티드 로보틱스(네트워크로 연결된 로봇의 통신-제어 공동 설계)다.[^cv] 연구실 목록의 Journals & Top Conferences(J) 칸 논문을 시기별로 보면, 2010–2017년에는 다중 안테나(MIMO, 여러 안테나로 동시에 신호를 주고받는 방식) 중계 통신과 간섭 정렬(수신기에서 간섭 신호들을 신호 공간의 한 부분으로 겹쳐 모아 나머지를 깨끗하게 쓰는 기법) 같은 무선 통신 이론을, 2017–2019년에는 비면허 대역(허가 없이 쓰는 주파수)을 함께 쓰는 LTE(LTE-LAA)와 Wi-Fi의 공존, 극저해상도 영상으로 사생활을 지키는 행동 인식을 다룬다. 2020–2022년에는 심층 강화학습과 딥러닝을 쓰는 셀 사이 자원 할당·사용자 연결·전력 제어가 많고, 2023년 이후에는 통신-센싱 통합, CSI 피드백, 언어 모델을 쓰는 통신, 연합 학습과 차분 프라이버시(개별 자료가 결과에 주는 영향을 숨기도록 잡음을 더하는 프라이버시 기준)가 자주 나온다.[^pubs]

논문으로 보면 지금의 전문 분야는 네 갈래다. 첫째, 학습 기반 채널 예측·CSI 압축과 언어 모델로 무선 접속망의 전송을 다루는 AI 네이티브 무선 통신이다(대표 논문 1–3).[^p1][^p2][^p3] 둘째, 무선 에지에서 통신 효율을 높이는 연합 학습과 작업 오프로딩 최적화다(대표 논문 4, 5).[^p4][^p5] 셋째, 다중 사용자 MIMO-OFDM과 재구성 표면을 쓰는 통신-센싱 통합 설계다(대표 논문 6, 7).[^p6][^p7] 넷째, 센싱·통신·계산을 함께 설계하는 다중 로봇 네트워크다(대표 논문 8).[^p8]

## 응용 분야

학부 연구실 상세 페이지는 통신-센싱 통합을 6G 시대의 자율주행과 환경 인지를 위한 핵심 기술로 보고,[^ecelabv] Research 페이지는 협력 로봇 연구가 규모가 큰 로봇 무리의 효율적이고 믿을 만한 조율을 다룬다고 적는다.[^research] CV는 「에지 네트워크 기반의 분산 신경망 제어 방법」 특허를 2025년 12월 삼성전자에 기술 이전(이전 금액 50,000,000 KRW)했다고 적는다.[^cv] 과제 목록(아래 「과제」 절)에는 캠퍼스 AI 네트워크 실증, AI-RAN과 적응형 RAN/RIC 기술, 5G-A 가상화 무선 접속망(vRAN) 연구 플랫폼, 도심 항공 모빌리티(UAM) 고밀도 운항을 위한 URAN 설계, 다중 무인기 기지국 통신, 차세대 무선랜, 수중 무선 인지 네트워크, 컨테이너 위험화물 탐지, 인공지능 레이다 데이터 분석이 있다.[^cv] 졸업생 진로로는 충남대학교·한밭대학교·금오공과대학교 교수, 삼성전자, 한국항공우주연구원(KARI), Synopsys, 한화에어로스페이스, 해외 대학원 박사과정(The University of Edinburgh, Stanford University)이 있다.[^people]

## 구성원

2026년 10월 23일 랩 People 페이지 기준이다. Post-doc 칸 1명, Graduate Students 칸 8명, Current Intern Students 칸 학부 인턴 6명이다. 과정은 카드 표기(Post-Doctoral Researcher, Ph.D. Course, M.S.-Ph.D. Course, M.S. Course, Undergrad Intern)를 옮겼고, 괄호 안은 카드가 함께 적은 소속 표기다. 시작 칸은 카드가 현재 과정·직위에 적은 시작 시점과 학교이며, POSTECH으로 적힌 학생은 카드가 그 과정을 POSTECH 과정으로 적은 경우다. 연구 주제는 카드의 관심 주제 줄과 인턴의 Research Focus다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Hyeonsu Lyu | 박사후연구원 | Mar 2026 (SNU) | Wireless x AI x Robotics, AI-Powered Remote Control, 6G Wireless Networks | 4, 6, 7 |
| Hosung Joo | 박사과정 | 2021/09 (POSTECH) | Communications, Sensing, Machine Learning | 2 |
| Sojeong Park | 석박사통합과정 | 2021/09 (POSTECH) | Semantic Communications | 3 |
| Minwoo Kim | 석박사통합과정 | 2022/09 (POSTECH) | Intelligent Wireless Systems, User Association & Resource Allocation | 5 |
| Sehyun Ryu | 석박사통합과정 | 2023/02 (POSTECH) | CSI Compression, Connected Robotics | 1, 2, 8 |
| Jaehyun Choi | 석박사통합과정 | 2025/03 (SNU) | AI-RAN, Connected Robotics | 8 |
| Yumin Kim | 석박사통합과정 | 2025/03 (SNU) | AI-RAN, ISAC |  |
| Minjae Lee | 석박사통합과정 | 2025/09 (SNU) | AI-RAN, ISAC |  |
| Seunghyun Lee | 석사과정 (Affiliated with Samsung) | 2026/03 (SNU) | AI-RAN, O-RAN |  |
| Wonil Kim | 학부 인턴 (BS-ing @SNU) |  | Inner and Outer bound in ISAC |  |
| Jeonghyun Ahn | 학부 인턴 (BS-ing @SNU) |  | Cell-Free Warehouse Network |  |
| Sunhong Ahn | 학부 인턴 (BS-ing @SNU) |  | Split Inference |  |
| Jaewon Ham | 학부 인턴 (BS-ing @Yonsei Univ.) |  | Proactive Resource Allocation |  |
| Jooyong Shin | 학부 인턴 (BS-ing @SNU) |  | Wireless Foundation Model |  |
| Minkyu Cho | 학부 인턴 (BS-ing @SNU) |  | ISAC in NLOS Environments |  |

## 졸업생과 이전 구성원

랩 People 페이지 Alumni & Long-term Interns 칸의 12명(박사 6, 석사 4, 장기 인턴 2)이다. 학위·과정 칸은 괄호 안의 학위와 학교(장기 인턴은 Intern 표기와 학교), 연도 칸은 괄호 안의 연도이고, 진로 칸은 랩이 화살표(➔)로 이어 적은 경로 그대로다. 「Postdoc @ AiSLab」은 이 연구실의 박사후연구원 경력이다. 2020년 7월 이전은 연구실이 UNIST에, 2020년 7월–2024년 8월은 POSTECH에 있던 때다.[^people][^events]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jonggyu Jang | Ph.D., UNIST (2021) | Postdoc @ AiSLab ➔ Visiting Scholar @ Purdue ➔ Professor @ Chungnam National University |
| Hyeonho Noh | Ph.D., POSTECH (2024) | Postdoc @ AiSLab ➔ Professor @ Hanbat National University |
| Yeongjun Kim | Ph.D., UNIST (2022) | Postdoc @ AiSLab ➔ System Engineer @ Samsung Electronics (S.LSI) |
| Youjin Kim | Ph.D., UNIST (2021) | Postdoc @ AiSLab ➔ System Engineer @ Samsung Electronics (MX) |
| Myeung Un Kim | Ph.D., UNIST (2019) | Senior Research Engineer @ KARI (Korea Aerospace Research Institute) |
| Harim Lee | Ph.D., UNIST (2020) | Postdoc @ AiSLab ➔ Professor @ Kumoh National Institute of Technology |
| Jungyeon Koh | M.S., POSTECH (2026) | Ph.D. Student @ .... University |
| Yein Heo | M.S., POSTECH (2022) | Researcher @ Samsung Electronics (S.LSI) |
| Woojin Park | M.S., UNIST (2017) | Software Engineer @ Synopsys |
| Hyeonmyung Oh | M.S., UNIST (2017) | Researcher @ Hanwha Aerospace |
| Kiyoon Kim | Intern @UNIST (2021-2023) | Ph.D. Student @ The University of Edinburgh |
| Seungmin Choi | Intern @SNU (2024-2026) | Ph.D. Student @ Stanford University |

## 최근 논문 목록 (2021–2026)

랩 Publication 페이지의 2021–2026년 연도 구역에 실린 Journals & Top Conferences(J) 38편(J32–J69)과 Book Chapters(B) 1건이다. 랩은 NeurIPS, ICML, AAAI 같은 학회 논문도 J 칸에 함께 올린다고 밝힌다. 연도는 페이지의 연도 구역이고, 저자·제목·학술지와 학회 이름, accepted(게재 승인)·early access(온라인 선공개)·forthcoming(출간 예정) 같은 상태 표기는 랩 표기 그대로다. 게재 승인(accepted)으로 적힌 2편과 출간 예정(forthcoming)인 책 속 장 1건은 랩이 둔 2026년 구역에 그대로 있고, 줄 안의 상태 표기로 출판된 논문과 구분된다. 저자 이름 뒤 *는 교신저자, (=)는 공동 기여 표시다. 교수는 2024년 9월 서울대에 부임했고, 2021년–2024년 8월에 나온 논문은 연구실이 POSTECH에 있던 때의 논문이다.[^pubs][^events]

**2026**

- Hosung Joo and Hyun Jong Yang\*. "Heterogeneity-Aware Compression-Ratio Orchestration for Multi-User CSI Feedback in AI-RAN". *accepted, Journal of Communications and Networks (JCN), 2026*.
- Jonggyu Jang, Hyeonsu Lyu, David J. Love, and Hyun Jong Yang\*. "Fed-ZOE: Communication-Efficient Over-the-Air Federated Learning via Zeroth-Order Estimation". *IEEE Journal on Selected Areas in Communications (JSAC), vol. 44, pp. 5856–5871, 2026*.
- Hyeonsu Lyu, Jonggyu Jang, Sehyun Ryu, and Hyun Jong Yang\*. "Generalized Influence Functions for Better Model Change Estimates". *accepted, Advances in Neural Information Processing Systems (NeurIPS), 2026*.
- Hyeonsu Lyu(=), Yumin Kim(=), and Hyun Jong Yang\*. "End-to-End Secure Connection Probability in Multi-Layer Networks with Heterogeneous Rician Fading". *IEEE Transactions on Vehicular Technology (TVT), early access, 2026*.
- Jungyeon Koh, Hyeonho Noh, and Hyun Jong Yang\*. "Group-wise Semantic Splitting Multiple Access for Multi-User Semantic Communication". *IEEE Wireless Communications Letters (WCL), vol. 15, pp. 5194–5198, 2026*.
- Hyeonho Noh, Hyeonsu Lyu, and Hyun Jong Yang\*. "Multiple Active STAR-RIS-Assisted Secure Integrated Sensing and Communication via Cooperative Beamforming". *IEEE Internet of Things Journal (IoTJ), early access, 2026*.
- Minjae Lee, Sehyun Ryu, Hosung Joo, Seungmin Choi, and Hyun Jong Yang\*. "Importance-Aware CSI Feedback with Adaptive Latent Truncation". *IEEE Transactions on Vehicular Technology (TVT), early access, 2026*.
- Jonggyu Jang, Hyeonsu Lyu, David J. Love, and Hyun Jong Yang\*. "Joint Optimization of User Association and Resource Allocation for Load Balancing With Heterogeneous Fairness". *IEEE Transactions on Communications (TCOM), vol. 74, pp. 12037–12051, 2026*.
- Sojeong Park, Yeongjun Kim, and Hyun Jong Yang\*. "User-Centric Stream Sensing for Grant-Free Access: Deep Learning With Covariance Differencing". *IEEE Wireless Communications Letters (WCL), vol. 15, pp. 3486–3490, 2026*.
- Hosung Joo(=), Seungmin Choi(=), Sehyun Ryu, and Hyun Jong Yang\*. "Compressed-CSI Feedback with Near Real-time Domain Adaptation". *IEEE Transactions on Communications (TCOM), early access, 2026*.
- Hyeonho Noh, Hyeonsu Lyu, Moe Z. Win, and Hyun Jong Yang\*. "DCFNet: Doppler Correction Filter Network for Integrated Sensing and Communication in Multi-User MIMO-OFDM Systems". *IEEE Transactions on Wireless Communications (TWC), vol. 25, pp. 16778–16794, 2026*.
- Hyun Jong Yang, Howon Lee, Kyuhong Shim, Jeongho Kwak, Hyunsoo Kim, Donghoon Kim, Khoa Anh Ngo, Sehyun Ryu, Jaehyun Choi, Youbin Kim, Chanjun Moon, Michael Ryoo, and Byonghyo Shim. "Advancing Multi-Robot Networks via MLLM-Driven Sensing, Communication, and Computation: A Comprehensive Survey". *IEEE Communications Surveys & Tutorials (COMST), vol. 28, no. 4, pp. 5833–5871, 2026*.
- Sehyun Ryu and Hyun Jong Yang\*. "Standards-Compliant DM-RS Allocation via Temporal Channel Prediction for Massive MIMO Systems". *IEEE Transactions on Vehicular Technology (TVT), vol. 75, no. 7, pp. 15171–15175, July 2026*.
- Jeongjun Park, Sunwook Hwang\*, Hyeonho Noh, Jin Mo Yang, Hyun Jong Yang, and Saewoong Bahk\*. "ALERT Open Dataset and Input-Size-Agnostic Vision Transformer for Driver Activity Recognition Using IR-UWB". *IEEE Access, vol. 14, pp. 28654–28674, 2026*.
- Sojeong Park, Hyeonho Noh, and Hyun Jong Yang\*. "Robust Transmission of Punctured Text With Large Language Model-Based Recovery". *IEEE Transactions on Vehicular Technology (TVT), vol. 75, no. 1, pp. 1737–1742, Jan. 2026*.
- Seungmin Choi(=), Hosung Joo(=), Sehyun Ryu, Tommaso Melodia, and Hyun Jong Yang\*. "Performance-Guaranteed CSI Feedback via Model-Agnostic Incremental Residual Compression Framework". *IEEE Wireless Communications Letters (WCL), vol. 15, pp. 880–884, 2026*.
- Hyun Jong Yang and Arogyaswami Paulraj. "Design Principles and Theoretical Insights in MIMO and Relay Networks". *in Mathematical Engineering and the Information Sciences, Chapter 16, edited by Ali H. Sayed and José M. F. Moura, Emerald Publishing, 2026 (forthcoming)*.

**2025**

- Hyun Jong Yang, Hyunsoo Kim, Hyeonho Noh, Seungnyun Kim, and Byonghyo Shim. "Large Multimodal Model-Empowered Task-Oriented Autonomous Communications: Design Methodology and Implementation Challenges". *IEEE Vehicular Technology Magazine (VTM), early access, Nov. 2025*.
- Hyeonsu Lyu(=), Jonggyu Jang(=), Harim Lee, and Hyun Jong Yang\*. "Non-iterative Optimization of Trajectory and Radio Resource for Aerial Network". *IEEE Transactions on Wireless Communications (TWC), vol. 24, no. 2, pp. 1555–1567, Feb. 2025*.
- Minwoo Kim, Youngchol Choi, Yeongjun Kim, Eojin Seo, and Hyun Jong Yang\*. "Joint Spectrum Sensing and Resource Allocation for OFDMA-Based Underwater Acoustic Communications". *IEEE Communications Letters (CL), vol. 29, no. 6, pp. 1300–1304, June 2025*.
- Jonggyu Jang, Hyeonsu Lyu, Seongjin Hwang, and Hyun Jong Yang\*. "Unveiling Hidden Visual Information: A Reconstruction Attack Against Adversarial Visual Information Hiding". *IEEE Transactions on Neural Networks and Learning Systems (TNNLS), vol. 36, no. 9, pp. 17154–17168, Sept. 2025*.
- Hyeonho Noh, Byonghyo Shim, and Hyun Jong Yang\*. "Adaptive Resource Allocation Optimization Using Large Language Models in Dynamic Wireless Environments". *IEEE Transactions on Vehicular Technology (TVT), vol. 74, no. 10, pp. 16630–16635, Oct. 2025*.
- Youjin Kim, Jonggyu Jang, and Hyun Jong Yang\*. "Enhancing Sum-Rate Performance in Constrained Multicell Networks: A Low-Information Exchange Approach". *IEEE Communications Letters (CL), vol. 29, no. 1, pp. 125–129, Jan. 2025*.

**2024**

- Minwoo Kim(=), Jonggyu Jang(=), Youngchol Choi, and Hyun Jong Yang\*. "Distributed Task Offloading and Resource Allocation for Latency Minimization in Mobile Edge Computing Networks". *IEEE Transactions on Mobile Computing (TMC), vol. 23, no. 12, pp. 15149–15166, Dec. 2024*.
- Sehyun Ryu(=), Jonggyu Jang(=), and Hyun Jong Yang\*. "Noise Variance Optimization in Differential Privacy: A Game-Theoretic Approach Through Per-Instance Differential Privacy". *IEEE Access, vol. 12, pp. 103104–103118, 2024*.
- Jonggyu Jang, Seongjin Hwang, and Hyun Jong Yang\*. "Rethinking DP-SGD in Discrete Domain: Exploring Logistic Distribution in the Realm of signSGD". *Proceedings of the 41st International Conference on Machine Learning (ICML), vol. 235, pp. 21241–21265, July 2024*.
- Hyeonho Noh, Harim Lee, and Hyun Jong Yang\*. "Joint Optimization on Uplink OFDMA and MU-MIMO for IEEE 802.11ax: Deep Hierarchical Reinforcement Learning Approach". *IEEE Communications Letters (CL), vol. 28, no. 8, pp. 1800–1804, Aug. 2024*.
- Yeongjun Kim, Jonggyu Jang\*, and Hyun Jong Yang\*. "Distributed Resource Allocation and User Association for Max-Min Fairness in HetNets". *IEEE Transactions on Vehicular Technology (TVT), vol. 73, no. 2, pp. 2983–2988, Feb. 2024*.

**2023**

- Jonggyu Jang, Sangwoo Oh, Youjin Kim, Dongmin Seo, Youngchol Choi, and Hyun Jong Yang\*. "M2SODAI: Multi-Modal Maritime Object Detection Dataset With RGB and Hyperspectral Image Sensors". *Proceedings of the 37th International Conference on Neural Information Processing Systems (NeurIPS), pp. 53831–53843, Dec. 2023*.
- Yeongjun Kim, Youngchol Choi, and Hyun Jong Yang\*. "Spectrum Sensing for Underwater Cognitive Radio With Limited Sensing Time". *IEEE Communications Letters (CL), vol. 27, no. 8, pp. 2014–2018, Aug. 2023*.
- Hyeonho Noh, Harim Lee, and Hyun Jong Yang\*. "ICI-Robust Transceiver Design for Integration of MIMO-OFDM Radar and MU-MIMO Communication". *IEEE Transactions on Vehicular Technology (TVT), vol. 72, no. 1, pp. 821–838, Jan. 2023*.
- Hyun Jong Yang and Jun Moon. "A sufficient condition for optimal control problem of fully coupled forward-backward stochastic systems with jumps: A state-constrained control approach". *Optimal Control Applications and Methods, vol. 44, no. 4, pp. 1936–1971, July/Aug. 2023*.

**2022**

- Jonggyu Jang and Hyun Jong Yang\*. "Recurrent Neural Network-Based User Association and Power Control in Dynamic HetNets". *IEEE Transactions on Vehicular Technology (TVT), vol. 71, no. 9, pp. 9674–9689, Sept. 2022*.
- Jonggyu Jang and Hyun Jong Yang\*. "α-Fairness-Maximizing User Association in Energy-Constrained Small Cell Networks". *IEEE Transactions on Wireless Communications (TWC), vol. 21, no. 9, pp. 7443–7459, Sept. 2022*.
- Jonggyu Jang and Hyun Jong Yang\*. "Deep Learning-Aided User Association and Power Control With Renewable Energy Sources". *IEEE Transactions on Communications (TCOM), vol. 70, no. 4, pp. 2387–2403, April 2022*.
- Harim Lee and Hyun Jong Yang\*. "Downlink MU-MIMO LTE-LAA for Coexistence With Asymmetric Hidden Wi-Fi APs". *IEEE Transactions on Mobile Computing (TMC), vol. 21, no. 1, pp. 93–109, Jan. 2022*.
- Yeongjun Kim, Harim Lee, Maximilian Matthe, Gerhard Fettweis, and Hyun Jong Yang\*. "GFDM-Based Asynchronous Grant-Free Multiple-Access". *IEEE Access, vol. 10, pp. 31012–31030, 2022*.

**2021**

- Harim Lee, Myeung Un Kim, Yeongjun Kim, Hyeonsu Lyu, and Hyun Jong Yang\*. "Development of a Privacy-Preserving UAV System With Deep Learning-Based Face Anonymization". *IEEE Access, vol. 9, pp. 132652–132662, 2021*.
- Jun Moon and Hyun Jong Yang\*. "Linear-Quadratic Time-Inconsistent Mean-Field Type Stackelberg Differential Games: Time-Consistent Open-Loop Solutions". *IEEE Transactions on Automatic Control (TAC), vol. 66, no. 1, pp. 375–382, Jan. 2021*.

## 국제 학회 발표 (2021–2026)

랩 Publication 페이지 2021–2026년 연도 구역의 International Conferences(C) 22건(C38–C59)이다. 워크숍 발표와 학생 초록·포스터 발표도 랩 분류대로 들어 있고, 2026년 구역의 5건(C55–C59)은 to appear(발표 예정)로 적혀 있고 이 표기는 랩 표기 그대로다. 2024년 8월까지의 발표는 연구실이 POSTECH에 있던 때의 것이다.[^pubs]

**2026**

- Sehyun Ryu and Hyun Jong Yang. "Blockage-Aware Multi-RIS Sensing and Optimization for mmWave Smart Radio Environments". *to appear in Proc. 2026 IEEE Global Communications Conference (GLOBECOM), SAC: RISSE, Macau, China, Dec. 7–11, 2026*.
- Hyeonsu Lyu, Minwoo Kim, Sojeong Park, and Hyun Jong Yang. "SceneBaker: Radio-Ready Scene Generation for Sionna Ray-Tracing". *to appear in Proc. 2026 IEEE Global Communications Conference (GLOBECOM) Workshops, 3rd Workshop on Digital Twins over NextG Wireless Networks, Macau, China, Dec. 2026*.
- Minwoo Kim and Hyun Jong Yang. "Split LDPC Decoding for Latency-Constrained Relay Networks". *to appear in Proc. 17th International Conference on ICT Convergence (ICTC), Jeju Island, Korea, Oct. 14–16, 2026*.
- Minjae Lee and Hyun Jong Yang. "Reliability-Constrained Early-Exit Handover Prediction for LEO Satellite Networks". *to appear in Proc. 17th International Conference on ICT Convergence (ICTC), Jeju Island, Korea, Oct. 14–16, 2026*.
- S. Ahn, Minjae Lee, and Hyun Jong Yang. "Joint Split Inference and Sequential Scheduling for Soft-Deadline-Aware Heterogeneous Edge Inference". *to appear in Proc. 17th International Conference on ICT Convergence (ICTC), Jeju Island, Korea, Oct. 14–16, 2026*.
- Sojeong Park and Hyun Jong Yang\*. "Semantic Pilot Design for Data-Aided Channel Estimation Using a Large Language Model". *Proc. IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), Barcelona, Spain, May 2026, pp. 21531–21535*.

**2025**

- Yumin Kim, Hyeonsu Lyu, Minjae Lee, and Hyun Jong Yang. "Accuracy-Delay Trade-Off in LLM Offloading via Token-Level Uncertainty". *IEEE Global Communications Conference (GLOBECOM) Workshops, Taipei, Taiwan, Dec. 12, 2025*.
- Minjae Lee, SeongJin Hwang, and Hyun Jong Yang. "GPU-based Pricing Scheduler for Joint User Association and Resource Allocation in MU-MIMO". *Proc. 2025 IEEE/IEIE International Conference on Consumer Electronics-Asia (ICCE-Asia), Busan, Korea, Republic of, October 29, 2025, pp. 1–6*.
- Minwoo Kim and Hyun Jong Yang. "Error Correction Code Acceleration in Future RAN: Challenges and Opportunities". *Proc. 2025 IEEE/IEIE International Conference on Consumer Electronics-Asia (ICCE-Asia), Busan, Korea, Republic of, October 29, 2025, pp. 1–4*.
- Jaehyun Choi, Sehyun Ryu, Seungmin Choi, and Hyun Jong Yang. "RT-AUGGAN: Robust Fingerprint Positioning under Environmental Variations via Ray Tracing-Assisted GAN Augmentation". *Proc. 2025 IEEE/IEIE International Conference on Consumer Electronics-Asia (ICCE-Asia), Busan, Korea, Republic of, October 29, 2025, pp. 1–6*.
- Sojeong Park and Hyun Jong Yang. "A Survey of Learning-Based Channel Decoders and Parallelization Strategies for AI-RAN". *Proc. International Conference on ICT Convergence (ICTC), Jeju Island, Korea, Republic of, October 16, 2025*.
- SeongJin Hwang, Seungmin Choi, and Hyun Jong Yang. "T-TransNet: Ternary Attention Network for CSI Feedback in FDD Massive MIMO System". *Proc. International Conference on ICT Convergence (ICTC), Jeju Island, Korea, Republic of, October 16, 2025*.
- Hyeonsu Lyu, Yumin Kim, and Hyun Jong Yang. "On the Secure Connection Probability of Multi-Hop Relaying in Multi-Layer Networks". *Proc. International Conference on ICT Convergence (ICTC), Jeju Island, Korea, Republic of, October 17, 2025*.

**2024**

- Hyeonho Noh, Sojeong Park, and Hyun Jong Yang. "Deep Reinforcement Learning-based Resource Allocation and Mode Selection for Semantic Communication". *WiOpt Workshop on Modeling and Optimization for Semantic Communications (MOSC), Seoul, South Korea, October 21, 2024*.
- Hyeonho Noh, Seong-Ryeol Park, Wonmin Cho, Kyung-Tae Kim, and Hyun Jong Yang. "Leveraging Multiple PRF Radar for Target Detection and Sea Clutter Suppression with Deep Learning Network". *Proc. 2024 15th International Conference on Information and Communication Technology Convergence (ICTC), Jeju Island, Korea, Republic of, October 17, 2024, pp. 898–902*.
- Jungyeon Koh, Hyeonsu Lyu, Jonggyu Jang, and Hyun Jong Yang. "Faithful and Fast Influence Function via Advanced Sampling". *Mechanistic Interpretability (MI) Workshop @ ICML, Vienna, Austria, July 2024*.
- Sehyun Ryu, Hosung Joo, Jonggyu Jang, and Hyun Jong Yang. "Instance-wise Laplace Mechanism via Deep Reinforcement Learning". *AAAI Conference on Artificial Intelligence (AAAI) Student Abstract and Poster Program, Vancouver, BC, Canada, Feb. 2024*.

**2023**

- Hyeonsu Lyu and Hyun Jong Yang. "Maneuver by Airstreams for Stratospheric Balloon Base Stations". *Proc. International Conference on ICT Convergence (ICTC), Jeju Island, South Korea, Oct. 2023*.

**2022**

- Hyeonsu Lyu, SeongJin Hwang, and Hyun Jong Yang. "Multi-Agent Reinforcement Learning-Based Coverage Maximization for Fixed-Wing Base Stations". *Proc. International Conference on ICT Convergence (ICTC), Jeju Island, South Korea, Oct. 2022*.
- Hosung Joo, Youngchol Choi, Jongwon Park, Chang Hwy Lim, and Hyun Jong Yang. "Connecting Quality Metrics to Deep Learning Accuracy for Image Fusion Methods". *Proc. International Conference on ICT Convergence (ICTC), Jeju Island, South Korea, Oct. 2022*.
- Myoung Hoon Lee, Hyun Jong Yang, and Jun Moon. "Network-Based Goal Selection for Multi-Goal Reinforcement Learning Based on Maximum Entropy Framework". *International Conference on Control, Automation and Systems (ICCAS), Busan, South Korea, Nov. 2022*.
- Myoung Hoon Lee, Jun Moon, and Hyun Jong Yang. "MEGN: A maximum entropy goal selection method for multi-goal reinforcement learning". *Proc. Asian Control Conference (ASCC), Jeju Island, South Korea, May 2022*.

## 국내 학회·학술지 논문 (2021–2026)

랩 Publication 페이지 2021–2026년 연도 구역의 Domestic Papers(D) 40건(D11–D50)이다. 국내 학술대회 발표와 국내 학술지·학회지 논문이 함께 들어 있고, 제목은 랩 표기(국문·영문) 그대로다. 2024년 8월까지의 항목은 연구실이 POSTECH에 있던 때의 것이다.[^pubs]

**2026**

- Yumin Kim and Hyun Jong Yang. "UAV 중심 ISAC-DT 융합 네트워크 기술 동향: 디지털 트윈 기반 항공 지능형 교통 및 표적 추적". *Proc. 2026 KICS Summer Conference, Jeju, Korea, June 18, 2026*.
- Sehyun Ryu, Jaehyun Choi, and Hyun Jong Yang. "Communication-Aware Multi-Agent Path Finding for Wi-Fi 6 Warehouse Robot Coordination". *Proc. 2026 KICS Summer Conference, Jeju, Korea, June 18, 2026*.
- Hyeonho Noh, Hyeonsu Lyu, and Hyun Jong Yang. "딥러닝 기반 OFDM ISAC 간섭 제거". *Proc. 36th Joint Conference on Communications and Information (JCCI), Yeosu, Korea, Apr. 16, 2026*.
- Minwoo Kim and Hyun Jong Yang. "Spatio-Temporal Learning-based Channel Prediction for High-Speed Mobility in mmWave bands". *Proc. 36th Joint Conference on Communications and Information (JCCI), Yeosu, Korea, Apr. 16, 2026*.
- Hyeonsu Lyu, Minwoo Kim, Sehyun Ryu, and Hyun Jong Yang. "Towards Building a Ray-Tracing-Compatible Digital Twin Scene for Wireless-Aware Physical AI Systems". *Proc. 36th Joint Conference on Communications and Information (JCCI), Yeosu, Korea, Apr. 15, 2026*.
- Sehyun Ryu and Hyun Jong Yang. "A Survey of the Application of Ray-Tracing-Based Channel Modeling for Digital Twin Environments". *Proc. 2026 KICS Winter Conference, Pyeongchang, Korea, Republic of, February 4, 2026*.
- Hyun Jong Yang. "AI-RAN 기술 및 연구 동향: AI-native RAN과 Physical AI 응용 (AI-RAN Technology and Research Trends: AI-native RAN and Physical AI Applications)". *Information & Communications Magazine (KICS), vol. 43, no. 1, pp. 39–49, Feb. 2026*.

**2025**

- Hyun Jong Yang, Yumin Kim, Jaehyun Choi, and Hyunji Lee. "AI-RAN 기술 동향 (Trends in AI-RAN)". *Proc. KICS Summer Conference, June 2025, pp. 317–319*.

**2024**

- Jonggyu Jang, Minwoo Kim, and Hyun Jong Yang. "주파수 자원 관리를 통한 6G 무선 통신망의 인공지능 서비스 오프로딩 최적화 기술에 관한 연구 (Research on AI Service Offloading Optimization for 6G Wireless Networks via Frequency Resource Management)". *Proc. KICS Summer Conference, June 2024*.
- Sehyun Ryu and Hyun Jong Yang. "무선 통신을 위한 생성형 모델 활용에 대한 동향 (Survey on the Trends of Generative Models for Wireless Communications)". *Information & Communications Magazine (KICS), vol. 41, no. 5, pp. 29–37, May 2024*.
- Hyeonsu Lyu and Hyun Jong Yang. "A Survey on High-Altitude Balloon UAVs for Vertical Heterogeneous Networks". *The Journal of Korean Institute of Communications and Information Sciences (J-KICS), vol. 49, no. 5, pp. 582–592, May 2024*.
- Hosung Joo and Hyun Jong Yang. "Development of an Algorithm for Passive Detecting the Movement of Unidentified-Flying-Objects OFDM Sources in an Air Surveillance System". *Proc. KICS Winter Conference, Feb. 2024*.

**2023**

- Sojeong Park, Yeongjun Kim, Jonggyu Jang, and Hyun Jong Yang. "Massive MIMO 환경에서의 Grant-Free Access를 위한 학습기반 채널 추정 기법 연구 (A Learning-Based Channel Estimation Method with Non-Orthogonal Pilots for Grant-Free Multiple Access in Massive MIMO Systems)". *The Journal of Korean Institute of Communications and Information Sciences (J-KICS), vol. 48, no. 7, pp. 838–847, July 2023*.
- Seongjin Hwang and Hyun Jong Yang. "이미지 스테가노그래피의 동향 및 한계". *Proc. KICS Fall Conference, Nov. 2023*.
- Hosung Joo, Youngchol Choi, Jongwon Park, Chang Hwy Lim, and Hyun Jong Yang. "A study on X-ray-based Tomography Reconstruction on Port Container Using Dictionary Learning and Belief Propagation". *Proc. KICS Fall Conference, Nov. 2023*.
- Hosung Joo, Youngchol Choi, Jongwon Park, Chang Hwy Lim, and Hyun Jong Yang. "Few-View Scans Into Synthesis: Information Fusion of Computed Tomography for Port Container X-ray Images". *Proc. KSNT Fall Conference (Special Session), Nov. 2023*.
- Hyeonsu Lyu and Hyun Jong Yang. "Stratolite: Breakthrough For UAV Communications". *Proc. KICS Summer Conference, June 2023*.
- Sehyun Ryu and Hyun Jong Yang. "Additive Machine Unlearning Algorithm Using Orthogonality". *Proc. KICS Summer Conference, June 2023*.
- Hosung Joo, Youngchol Choi, Jongwon Park, Chang Hwy Lim, and Hyun Jong Yang. "A Survey on Multimodal Sensing of X-ray and Image Fusion Using Photon Backscatter and Transmission Images for Cargo Inspections". *Proc. KICS Summer Conference, June 2023*.
- Minwoo Kim, Yeongjun Kim, Youngchol Choi, and Hyun Jong Yang. "Rate Control을 이용한 비동기 수중 OFDMA 인지 네트워크". *Proc. 34th Joint Conference on Communications and Information (JCCI), Apr. 2023*.
- Hosung Joo and Hyun Jong Yang. "Dictionary Learning Applications for Semantic Communication". *Proc. 34th Joint Conference on Communications and Information (JCCI), Apr. 2023*.
- Sojeong Park, Yeongjun Kim, Jonggyu Jang, and Hyun Jong Yang. "Massive MIMO 환경에서의 Grant-Free Access를 위한 학습기반 채널 추정 기법 연구". *Proc. KICS Winter Conference, Feb. 2023. (Best Paper Award)*.
- Hyeonsu Lyu and Hyun Jong Yang. "Machine Unlearning: A Survey on Principles and Challenges". *Proc. KICS Winter Conference, Feb. 2023*.
- Jonggyu Jang and Hyun Jong Yang. "Privacy Attacks on Machine Learning Models: A Survey on Open Problems and Future Directions". *Proc. KICS Winter Conference, Feb. 2023*.

**2022**

- Hyeonsu Lyu, Jonggyu Jang, and Hyun Jong Yang. "일반화된 고속 Water-Filling 알고리즘". *Proc. KICS Fall Conference, Nov. 2022*.
- Hosung Joo and Hyun Jong Yang. "A study on Deep Learning-based Image Fusion Methods for Reducing Communication Overhead". *Proc. KICS Fall Conference, Nov. 2022*.
- Sojeong Park, Hosung Joo, Jonggyu Jang, and Hyun Jong Yang. "A survey on Semantic Communications: Opportunities and Challenges". *Proc. KICS Fall Conference, Nov. 2022*.
- Seongjin Hwang and Hyun Jong Yang. "프라이버시를 보호하는 인공지능 기법에 대한 조사". *Proc. 3rd Korea Artificial Intelligence Conference, Sept. 2022*.
- Hyeonsu Lyu, Jonggyu Jang, Harim Lee, and Hyun Jong Yang. "Trajectory-planning and resource allocation of UAV base station with user QoS constraints". *Proc. KICS Summer Conference, June 2022*.
- Jonggyu Jang, Youjin Kim, Sangwoo Oh, Dongmin Seo, Youngchol Choi, and Hyun Jong Yang. "초 분광 이미지 기반 컴퓨터 비전 및 기계 학습 기술 동향". *Proc. KICS Summer Conference, June 2022*.
- Jonggyu Jang and Hyun Jong Yang. "AI 기반 자원 관리 학습 기술 동향". *Proc. Joint Conference on Communications and Information (JCCI), Apr. 2022*.
- Sojeong Park, Hyeonsu Lyu, and Hyun Jong Yang. "완전 합성곱 신경망을 이용한 가변 Deep Q-Network 설계". *Proc. KICS Winter Conference, Feb. 2022*.
- Hyeonho Noh and Hyun Jong Yang. "IEEE 802.11ax 상향 링크를 위한 학습 기반 유저 선택 및 자원 할당". *Proc. KICS Winter Conference, Feb. 2022*.

**2021**

- Hyeonho Noh, Dongmin Seo, Moonjin Lee, and Hyun Jong Yang. "HNS 해양배출 영상학적 현상 연구". *Proc. Conference of KOSMEE, Oct. 2021*.
- Yeongjun Kim, Young Chol Choi, and Hyun Jong Yang. "수중 음향 인지 네트워크를 위한 학습기반 다중 사용자 다중 접속 센싱 기법에 관한 연구". *Proc. KICS Fall Conference, Nov. 2021*.
- Jonggyu Jang, Youjin Kim, Sangwoo Oh, Dongmin Seo, and Hyun Jong Yang. "딥 러닝을 활용한 초 분광 영상 속 해상 선박 및 부유물 탐지 및 식별에 관한 연구". *Proc. KICS Fall Conference, Nov. 2021*.
- Hyeonsu Lyu, Harim Lee, Yeongjun Kim, and Hyun Jong Yang. "비행 시간을 최대화하는 드론의 최적 부품 선정 알고리즘에 대한 연구". *Proc. KICS Summer Conference, June 2021*.
- Jonggyu Jang, Hyun Jong Yang, and Seulgi Kim. "강화학습 기반 무선 사용자 연결 기법에 관한 연구". *Proc. KICS Winter Conference, Feb. 2021*.
- Hyeonsu Lyu and Hyun Jong Yang. "무인항공기 강화학습을 위한 테스트베드 구축 기법에 관한 연구". *Proc. KICS Winter Conference, Feb. 2021*.
- Tae Woo Park and Hyun Jong Yang. "비대칭 데이터셋 기반 딥러닝을 위한 적응적 학습률 조절 기법". *Proc. KICS Winter Conference, Feb. 2021*.

## 특허와 표준

랩 Publication 페이지 2021–2026년 연도 구역의 Patents & Standards(P) 20건(P36–P55)이다. 제목, 번호, filed(출원) 표기는 랩 표기 그대로이고, 발명자 칸은 랩이 적은 이름이다. 2024년 8월까지의 항목은 교수가 POSTECH에 있던 때의 것이다. CV는 이 가운데 2023년 구역의 「에지 네트워크 기반의 분산 신경망 제어 방법」을 2025년 12월 삼성전자에 기술 이전했다고 적는다.[^pubs][^cv]

- 2026 · Apparatus and Method for 3D Scene Transformation (3차원 장면 변환 장치 및 방법) (발명자 Hyun Jong Yang; 번호 KR 10-2026-0156534; 상태 filed)
- 2026 · Apparatus and Method for Doppler-Induced Inter-Carrier Interference Mitigation and Target Detection Using a Doppler Correction Filter Network in Multi-User MIMO-OFDM Integrated Sensing and Communication Systems (다중 사용자 MIMO-OFDM 기반 통합 센싱 및 통신 시스템에서 도플러 보정 필터 네트워크를 이용한 도플러 유발 부반송파 간 간섭 완화 및 표적 탐지 장치 및 방법) (발명자 Hyun Jong Yang; 번호 KR 10-2026-0108835; 상태 filed)
- 2026 · Data Augmentation Method For Indoor Positioning Based on Wireless Channel State Information And Computer Device Thereof (무선 채널 상태정보 기반 실내 위치 인식을 위한 데이터 증강 방법 및 이를 위한 컴퓨터 장치) (발명자 Hyun Jong Yang; 번호 KR 10-2026-0012777; 상태 filed)
- 2025 · Method for Performing Multi-hop Based Secure Communication in Integrated Network (통합 네트워크에서 다중 홉 기반의 보안 통신을 수행하는 방법 및 이를 위한 컴퓨터 장치) (발명자 Hyun Jong Yang; 번호 KR 10-2025-0213513; 상태 filed)
- 2025 · Method and Apparatus for Channel Prediction-based Reference Signal Allocation in Massive MIMO Wireless Communication System (다중 안테나 무선 통신 시스템에서 채널 예측 기반 참조신호 배치 방법 및 이를 위한 장치) (발명자 Hyun Jong Yang; 번호 KR 10-2025-0214422; 상태 filed)
- 2025 · Resource Allocation Method for Underwater Acoustic Communication Networks and Apparatus Therefor (수중 음향 통신 네트워크의 자원 할당 방법 및 이를 위한 장치) (발명자 Hyun Jong Yang; 번호 KR 10-2025-0209653; 상태 filed)
- 2025 · Method for Channel State Information (CSI) Feedback Using Multi-stage Residual Compression and User Equipment Performing the Same (다단 잔차 압축을 이용한 채널 상태 정보(CSI) 피드백 방법 및 이를 수행하는 단말) (발명자 Hyun Jong Yang; 번호 KR 10-2025-0202288; 상태 filed)
- 2025 · System and Method for Autonomous Task Execution with Deep Learning-Based Cooperation among Multiple Autonomous Agents, and Non-transitory Recording Medium for Performing the Same (딥러닝을 기반으로 다중 자율 에이전트가 협력하는 자율 태스크 수행 시스템 및 방법, 이를 수행하기 위한 비일시적 기록 매체) (발명자 Hyun Jong Yang; 번호 KR 10-2025-0063423; 상태 filed)
- 2024 · Apparatus and Method for Determining Privacy Information Leakage Possibility by Generating Restored Image Set (인공지능 모델의 학습 이미지셋에 대응되는 복원 이미지셋을 생성하여 개인정보 유출 가능성 유무를 판단하는 장치 및 방법) (발명자 Hyun Jong Yang; 번호 KR 10-2024-0161882; 상태 filed)
- 2024 · Apparatus and Method for Providing Statistical Data (통계적 데이터 제공 장치 및 방법) (발명자 Hyun Jong Yang; 번호 KR 10-2024-0143784; 상태 filed)
- 2024 · Device and Method for AI Model Unlearning (인공 지능 모델 언러닝 장치 및 방법) (발명자 Hyun Jong Yang; 번호 KR 10-2024-0134631; 상태 filed)
- 2024 · Text Transformation Device and Method (텍스트 변환 장치 및 방법) (발명자 Hyun Jong Yang; 번호 KR 10-2024-0134973; 상태 filed)
- 2024 · Method and Device for Communication Channel Estimation in Multi-Antenna Systems (다중 안테나의 통신 채널 추정 방법 및 그 장치) (발명자 Hyun Jong Yang; 번호 KR 10-2024-0014181; 상태 filed)
- 2023 · Distributed Neural Network Control Method based on Edge Network (에지 네트워크 기반의 분산 신경망 제어 방법) (발명자 Hyun Jong Yang; 번호 KR 10-2023-0061304)
- 2022 · Tree Search-based Path Planning and Resource Management for UAV Base Stations (무인항공기 기지국의 트리 탐색 기반 경로 계획 및 자원 관리 방법 및 장치) (발명자 Hyun Jong Yang; 번호 US 18/319,369 & KR 10-2022-0186323)
- 2022 · RL-based User Selection for Uplink in Wireless Systems (무선 통신 시스템에서 상향링크 통신을 위한 강화학습 기반 사용자 선택 방법 및 장치) (발명자 Hyun Jong Yang; 번호 KR 10-2022-0083124)
- 2022 · Base Station Control in Information-Constrained Networks using RL (강화학습을 이용한 채널 정보가 제한된 네트워크에서의 기지국 제어 방법 및 장치) (발명자 Hyun Jong Yang; 번호 KR 10-2022-0064364)
- 2021 · Power-Limited Base Station Control using RL (강화학습을 이용한 전력 한정 기지국 제어 방법 및 장치) (발명자 Hyun Jong Yang; 번호 KR 10-2021-0169868)
- 2021 · Detection Method for Asynchronously Received OFDM Signals (비동기적으로 수신된 OFDM 신호 검파 방법 및 장치) (발명자 Hyun Jong Yang; 번호 KR 10-2021-0186361)
- 2021 · Transceiver Beamforming for Joint Radar-Communication Systems (레이더-통신 결합 시스템을 위한 송수신 빔포밍 방법 및 장치) (발명자 Hyun Jong Yang; 번호 KR 10-2021-0186361)

## 과제

교수 CV(2026년 9월판) Research Projects 칸 38건 가운데 끝난 달이 2021년 11월 이후인 23건이다. 과제 이름(영문과 국문), 기간, 역할, 지원 기관, 연구비는 CV 표기 그대로다. 교수 개인 경력의 과제 목록이라 2024년 8월까지의 기간은 교수가 POSTECH에 있던 때이며, 연구비 표기는 과제마다 총액(Total Funding), 한 해 금액(Funding (FY2026)), 서울대 기간 금액(Funding at SNU)으로 기준이 다르다.[^cv]

- 2026 Campus AI Network Testbed Demonstration (2026년 캠퍼스 AI 네트워크 실증) (기간 Aug 2026 – Dec 2026; 역할 Participating Institution Principal Investigator; 지원 National Information Society Agency (NIA); 연구비 Total Funding: KRW 150.0M (approx. USD 115.4K))
- AI-RAN Global Leadership Project (에이아이-란 글로벌 선도 프로젝트) (기간 Apr 2026 – Dec 2028; 역할 Participating Institution Principal Investigator; 지원 Institute of Information & Communications Technology Planning & Evaluation (IITP); 연구비 Funding (FY2026): KRW 100.0M (approx. USD 76.9K))
- Development of Reliability-Guaranteed Adaptive RAN/RIC Technologies (응용성능 보장 적응형 RAN/RIC 기술 개발) (기간 Apr 2026 – Dec 2028; 역할 Participating Institution Principal Investigator; 지원 Institute of Information & Communications Technology Planning & Evaluation (IITP); 연구비 Funding (FY2026): KRW 460.0M (approx. USD 353.8K))
- Establishment of an International Collaborative Research Platform for the Institute of New Media and Communications (국제협력연구 플랫폼 구축, 뉴미디어통신공동연구소) (기간 Feb 2026 – Feb 2027; 역할 Co-investigator; 지원 Seoul National University; 연구비 Total Funding: KRW 50.0M (approx. USD 38.5K))
- Optimization Technologies for Ultra-Large Multimodal AI-Based Communication Systems (초거대 멀티모달 인공지능 기반 통신 시스템 최적화 기술 개발) (기간 Oct 2024 – Sep 2026; 역할 Principal Investigator (PI); 지원 Seoul National University; 연구비 Total Funding: KRW 100.0M (approx. USD 76.9K))
- 6G Cloud Leadership Open Hub for Education and Research (6G-클라우드 리더십구축을 위한 교육·연구 오픈 허브) (기간 Sep 2024 – Dec 2026; 역할 Participating Institution Principal Investigator; 지원 Institute of Information & Communications Technology Planning & Evaluation (IITP); 연구비 Total Funding (Sep 2024 – Dec 2026): KRW 268.749M (approx. USD 206.7K))
- Development of 5G-A vRAN Research Platform (5G-A vRAN 연구플랫폼 개발) (기간 Apr 2024 – Dec 2026; 역할 Participating Professor (Apr 2024 – Dec 2025), Participating Institution Principal Investigator (Jan 2026 – Dec 2026); 지원 Institute of Information & Communications Technology Planning & Evaluation (IITP); 연구비 Funding (FY2026): KRW 120.0M (approx. USD 92.3K))
- Development of URAN Design and Core Technologies for High-Density UAM Operations (UAM 고밀도 운항을 위한 URAN 설계 및 원천기술 개발) (기간 Jul 2021 – Dec 2026; 역할 Participating Professor (Jul 2021 – Dec 2025), Principal Investigator (PI) (Jan 2026 – Dec 2026); 지원 Institute of Information & Communications Technology Planning & Evaluation (IITP), University IT Research Center (ITRC) Program; 연구비 Funding (FY2026): KRW 858.660M (approx. USD 660.5K))
- Research on scalable learning-based multi-UAV BS communication technologies for practical multi-UAV BS systems (현실적인 다중 UAV 기지국 시스템을 위한 확장 가능한 학습 모델 기반 UAV 기지국 통신 기술) (기간 Jun 2023 – Feb 2026; 역할 Principal Investigator (PI); 지원 National Research Foundation of Korea (NRF); 연구비 Funding at SNU (Sep 2024 – Feb 2026): KRW 113.110M (approx. USD 87.0K))
- Research on hyper-connect wideband MIMO transceiver (초연결 초대역 MIMO 송수신 기술 연구) (기간 Apr 2021 – Dec 2025; 역할 Participating Professor (Apr 2021 – Aug 2024), Participating Institution Principal Investigator (Sep 2024 – Dec 2025); 지원 Institute of Information & Communications Technology Planning & Evaluation (IITP); 연구비 Funding (Sep 2024 – Dec 2025): KRW 120.569M (approx. USD 92.7K))
- Development of a new radio wave monitoring platform based on big data and AI (빅데이터·AI 기반의 新 전파 모니터링 플랫폼 개발) (기간 Apr 2023 – Dec 2024; 역할 Principal Investigator (PI, 위탁과제); 지원 Institute of Information & Communications Technology Planning & Evaluation (IITP))
- Technology Analysis and Research Direction for AI-Native Networks for ETRI Open Planning (ETRI 개방형 기획을 위한 AI-Native 네트워크 분야 기술분석 및 연구추진방향 도출) (기간 Jul 2023 – Nov 2023; 역할 Participating Professor; 지원 Electronics and Telecommunications Research Institute (ETRI))
- Data processing methods and simulated signal generation for artificial intelligence radar data analysis (인공지능 레이다 데이터 분석을 위한 데이터 처리 방법 및 모의 신호 생성) (기간 Nov 2022 – Dec 2024; 역할 Participating Professor; 지원 Agency for Defense Development (ADD))
- Development of full-duplex and adjacent channel interference removal techniques for next generation wireless LANs (차세대 무선랜을 위한 Full-Duplex 및 인접채널 간섭제거기법 개발) (기간 Sep 2022 – Dec 2024; 역할 Co-Principal Investigator (Co-PI); 지원 Samsung Electronics)
- Technology Analysis and Research Advancement Directions Derived for Open-Plan, Boundaryless Hyper-Space Networking (개방형 기획을 위한 무경계 초공간 네트워킹 분야 기술분석 및 연구추진방향 도출) (기간 Jun 2022 – Nov 2022; 역할 Participant; 지원 Electronics and Telecommunications Research Institute (ETRI))
- Development of marine object detection machine learning techniques based on optical images (광학영상 기반의 해상물체 탐지 머신러닝 기법 개발) (기간 Mar 2022 – Nov 2022; 역할 Principal Investigator (PI); 지원 Korea Research Institute of Ships and Ocean Engineering (KRISO))
- Development of impact assessment and management technology for hazardous substances in marine industrial facilities (해양산업시설 배출 위험유해물질 영향평가 및 관리기술 개발) (기간 Apr 2021 – Dec 2021; 역할 Co-Principal Investigator (Co-PI); 지원 Korea Research Institute of Ships and Ocean Engineering (KRISO))
- Development of automatic container dangerous cargo detection and complex detection system (컨테이너 위험화물 자동검색 및 복합탐지 시스템 개발) (기간 Jan 2021 – Dec 2024; 역할 Principal Investigator (PI, 위탁연구); 지원 Korea Research Institute of Ships and Ocean Engineering (KRISO))
- Research on on-path computing for 6G massive high performance neural network services (대규모 고성능 신경망 서비스가 가능한 6G 실현을 위한 on-path computing 기술 개발) (기간 Sep 2020 – Aug 2022; 역할 Participating Professor; 지원 Samsung Research Funding & Incubation Center for Future Technology)
- Low-latency next-gen WLAN for extreme high resolution VR/AR/MR (초고해상도 초저지연 VR/AR/MR 실현을 위한 차세대 무선랜 원천기술 연구) (기간 Sep 2020 – May 2022; 역할 Participating Professor; 지원 Samsung Research Funding & Incubation Center for Future Technology)
- Research on learning-based underwater wireless cognitive network technologies (학습기반 수중 무선 인지 네트워크 기술 연구) (기간 Mar 2020 – Nov 2024; 역할 Principal Investigator (PI, 위탁연구); 지원 Korea Research Institute of Ships and Ocean Engineering (KRISO))
- Display integrated antennas and beam synthesis (디스플레이 집적 안테나 및 빔 조향 기술) (기간 Mar 2019 – Feb 2022; 역할 Participating Professor; 지원 Samsung Display)
- Electrical/mechanical drone beamforming based on target detection and position control (타겟 감지 및 정밀 자세 제어를 이용한 전기적/기계적 드론 빔포밍 기술 개발) (기간 Jul 2018 – Dec 2022; 역할 Principal Investigator (PI); 지원 Institute of Information & Communications Technology Planning & Evaluation (IITP))

## 수상

교수 CV(2026년 9월판) Awards and Honors 칸 10건 가운데 2021년 이후 7건이다. 상 이름과 날짜, 괄호 안의 공동 수상자 표기(mentored student는 교수가 지도한 학생)는 CV 표기 그대로다. 2022년과 2023년 수상은 교수가 POSTECH에 있던 때의 것이다.[^cv]

- Feb. 2026 · Encouragement Award, The 32nd Humantech Paper Awards, Samsung Electronics (Co-recipient: Hyeonsu Lyu (mentored student))
- Oct. 2025 · Best Poster Award, IEEE/IEIE International Conference on Consumer Electronics-Asia (ICCE-Asia) (Co-recipient: Seungmin Choi (mentored student))
- 2025 · Distinguished TPC Award, International Conference on Information and Communication Technology Convergence (ICTC)
- Sep. 2025 · Best Paper Award, International Conference on Information and Communication Technology Convergence (ICTC) (Co-recipient: Hyeonsu Lyu (mentored student))
- Aug. 2023 · President's Award of IITP (Institute of Information & Communications Technology Planning & Evaluation), KICS (Co-recipient: Hyeonsu Lyu (mentored student))
- Feb. 2023 · Best Paper Award, KICS Winter Conference (Co-recipients: Sojeong Park, Yeongjun Kim, and Jonggyu Jang (mentored students))
- Nov. 2022 · Korea Aerospace Industries (KAI) Paper Award (Co-recipient: Hyeonsu Lyu (mentored student))

## 소식

누리집 첫 화면 Recent News·Old News 칸과 Events 페이지 Lab Footprints 칸의 2021년 이후 글 15건이다. 날짜와 문구는 페이지 표기 그대로이고, 2024년 8월까지의 글은 연구실이 POSTECH에 있던 때의 글이다.[^home][^events]

- Aug 2026 - Jan 2027 · Sehyun Ryu will join Prof. John Cioffi’s lab at Stanford University as a visiting student.
- May 2026 · Minwoo Kim, Sojeong Park, and Sehyun Ryu will present their Ph.D. proposals.
- Apr 2026 · Hyeonsu Lyu will receive the Encouragement Award at the 32nd Samsung Humantech Paper Awards.
- Mar 2026 · Prof. Hyun Jong Yang has been appointed as an Editor for IEEE Transactions on Vehicular Technology (TVT).
- Feb 2026 · Prof. Hyun Jong Yang has been appointed as an Editor for IEEE Transactions on Communications (TCOM).
- Feb 2026 · The AiSLab website has been completely renewed and successfully moved to our new Seoul National University domain.
- Feb 2026 · Hyeonsu Lyu successfully returned from his visiting student program at UT Austin, hosted by Prof. Kaushik Chowdhury.
- Feb 2026 · Hyeonsu Lyu successfully receives his Ph.D. degree from POSTECH.
- Dec 2025 - Feb 2026 · Successfully hosted Winter Research Interns and Graduation Project students: Won-il Kim, Sunhong Ahn, Seungmin Choi, Jooyong Shin, Junghyun Ahn, Minkyu Cho, and Jaewon Ham.
- Sep 2025 · Hyeonho Noh joins Hanbat National University as a tenure-track faculty.
- Aug 2025 · Jonggyu Jang joins Chungnam National University as a tenure-track faculty.
- Aug 2025 · Lab became affiliated with the New Media Communications Research Institute (NMRI), SNU.
- Sep 2024 · The lab successfully relocated to Seoul National University (SNU), Department of Electrical and Computer Engineering.
- Feb 2024 · Yeongjun Kim hired by Samsung Electronics (S.LSI) as a Researcher.
- Sep 2023 · Officially recognized and selected as a “Healthy Laboratory” by POSTECH.

## 연락과 위치

- 교수 이메일: hjyang@snu.ac.kr[^prof]
- 교수 전화: +82-2-880-1789(학부 교수 소개 표기 02-880-1789)[^prof][^eceprof]
- 교수 연구실: 서울대학교 302동 528호(Room 528, Bldg. 302). CV는 132동 209호(Rm. 209, Bldg. 132)도 함께 적는다.[^prof][^eceprof][^cv]
- 주소: 08826 서울특별시 관악구 관악로 1 서울대학교 전기·정보공학부[^ecelabv]
[^home]: 연구실 누리집 첫 화면 <https://aislab.snu.ac.kr/> (연구실 이름, Recent News·Old News 칸, 2026-10-23 열람)
[^prof]: 누리집 Professor 페이지 <https://aislab.snu.ac.kr/professor/> (직위·소속, 이메일·전화·사무실, Short Bio, 2026-10-23 열람)
[^people]: 누리집 People 페이지 <https://aislab.snu.ac.kr/current-researchers/> (Post-doc, Graduate Students, Current Intern Students, Alumni & Long-term Interns 칸, 2026-10-23 열람)
[^research]: 누리집 Research 페이지 <https://aislab.snu.ac.kr/%ec%9d%b8%ec%82%ac%eb%a7%90-3/> (Core Research Areas: AI-Native RAN, Distributed Intelligence, Connected Robotics, 2026-10-23 열람)
[^pubs]: 누리집 Publication 페이지 <https://aislab.snu.ac.kr/%eb%85%bc%eb%ac%b8/> (Submitted 구역과 2026–2020년·Before 2020 연도 구역, Last updated: Oct 2026 표기, 2026-10-23 열람)
[^info]: 누리집 Information 페이지 <https://aislab.snu.ac.kr/information/> (연구 도구와 자체 교육 과정, 2026-10-23 열람)
[^events]: 누리집 Events 페이지 <https://aislab.snu.ac.kr/events/> (Lab Footprints 칸, 2026-10-23 열람)
[^cv]: 교수 CV(Curriculum Vitae, 2026년 9월판 PDF, 누리집 Professor 페이지 연결) <https://aislab.snu.ac.kr/wp-content/uploads/sites/229/2026/09/CV_202609.pdf> (Current Research Interest, Education, Experiences, Awards and Honors, Professional Activities, Research Projects, Patents, Standards, and Technology Transfers, Courses Taught, Supervised Students, 2026-10-23 열람)
[^ecelab]: 서울대학교 전기·정보공학부 연구실 목록 <https://ece.snu.ac.kr/research-faculty/research/lab> (연구그룹별 연구실 이름과 교수, 2026-10-23 열람)
[^ecelabv]: 서울대학교 전기·정보공학부 연구실 상세(고급지능시스템 연구실) <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=145> (연구실 소개 및 연구분야, 최근 관심분야 및 주요 연구과제, 주소, 2026-10-23 열람)
[^ecefac]: 서울대학교 전기·정보공학부 전임교수 목록 <https://ece.snu.ac.kr/research-faculty/faculty/full-time> (2026-10-23 열람)
[^eceprof]: 서울대학교 전기·정보공학부 교수 상세(양현종) <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p903> (직위, 학력, 주요경력, 전공·분야, Research Interest, 2026-10-23 열람)
[^p1]: S. Ryu, H. J. Yang, IEEE Transactions on Vehicular Technology 75, 15171-15175 (2026). <https://doi.org/10.1109/tvt.2026.3654149> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: H. Joo, S. Choi, S. Ryu, H. J. Yang, IEEE Transactions on Communications 74, 11048-11061 (2026). <https://doi.org/10.1109/tcomm.2026.3698862> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: S. Park, H. Noh, H. J. Yang, IEEE Transactions on Vehicular Technology 75, 1737-1742 (2026). <https://doi.org/10.1109/tvt.2025.3595593> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: J. Jang, H. Lyu, D. J. Love, H. J. Yang, IEEE Journal on Selected Areas in Communications 44, 5856-5871 (2026). <https://doi.org/10.1109/jsac.2026.3739217> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: M. Kim, J. Jang, Y. Choi, H. J. Yang, IEEE Transactions on Mobile Computing 23, 15149-15166 (2024). <https://doi.org/10.1109/tmc.2024.3458185> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: H. Noh, H. Lyu, M. Z. Win, H. J. Yang, IEEE Transactions on Wireless Communications 25, 16778-16794 (2026). <https://doi.org/10.1109/twc.2026.3687605> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: H. Noh, H. Lyu, H. J. Yang, IEEE Internet of Things Journal 13, 47191-47207 (2026). <https://doi.org/10.1109/jiot.2026.3719367> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: H. J. Yang 외, B. Shim, IEEE Communications Surveys & Tutorials 28, 5833-5871 (2026). <https://doi.org/10.1109/comst.2026.3683120> 초록 기준(Semantic Scholar 등록 초록).

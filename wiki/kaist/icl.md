# 지능형 통신시스템 연구실 (Intelligent Communication Systems Lab., ICL)

**KAIST 전기및전자공학부 · 최준일 교수**

- 분야: 6세대(6G) 이후를 겨냥한 무선통신 시스템의 설계와 분석. 재구성 지능형 표면(RIS), 위성·비지상 네트워크, 기계학습 기반 통신, 가시광 통신, 테라헤르츠·밀리미터파 통신, 다중 접속·무인 항공기 통신·통합 센싱 통신
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 무선·이동통신[^home][^eeprof][^p3], 광통신[^vlc][^p7], 네트워크 보안·프라이버시[^vlc][^other][^p4], 대형 언어 모델[^p6]
- 홈페이지: <https://www.icl.kaist.ac.kr/>
- 근거와 출처: [ICL 근거 페이지](icl-sources.md)

> 6G 이동통신과 그 이후의 핵심 기술이 될 새로운 무선통신 시스템을 연구하고, 신호처리·확률론·최적화·랜덤 행렬 이론·압축 센싱·기계학습을 분석 도구로 쓰는 연구실이다.[^home]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 최준일 교수가 이끄는 연구실이다.[^home][^eeprof] 누리집은 이름을 Intelligent Communication Systems Lab.(지능형 통신시스템 연구실), 줄여서 ICL로 적는다.[^home] 전기및전자공학부 교수 소개는 교수의 주요 연구를 "무선통신 / 차량간 통신"으로, 디비전을 Communication으로, 소속 연구실을 「지능형 통신 연구실」로 적고, 반도체시스템공학과 교수 목록과 연구실 목록에도 같은 이름과 누리집 주소로 올라 있다.[^eeprof][^sse][^sselab]

누리집 첫 화면은 연구실이 새로운 무선통신 시스템을 연구한다고 소개한다. 예로 드는 것은 대규모 MIMO(기지국에 많은 수의 안테나를 달아 여러 사용자와 동시에 신호를 주고받는 다중 안테나 기술), 밀리미터파 통신(파장이 밀리미터 단위인 높은 주파수 대역의 전파를 쓰는 통신), 차량-사물 통신(V2X, 차량이 다른 차량·도로 시설·사람 등과 주고받는 통신), 분산 통신(사물인터넷을 위한 기기 간 직접 통신)이며, 이 기술들이 6G 이동통신과 그 이후의 핵심 기술이 될 것이라고 적는다.[^home] 연구 방법으로는 신호처리, 확률론, 최적화, 랜덤 행렬 이론(무작위 값으로 채운 큰 행렬의 성질을 다루는 수학), 압축 센싱(드문드문한 구조를 가진 신호를 적은 수의 측정값으로 되살리는 방법), 기계학습을 든다.[^home] 연구 분야는 재구성 지능형 표면, 비지상 네트워크, 기계학습 기반 통신, 가시광 통신, 테라헤르츠·밀리미터파 통신, 그 밖의 주제(다중 접속, 무인 항공기, 통합 센싱·통신)의 여섯 칸으로 나뉜다.[^areas]

첫째 갈래는 **재구성 지능형 표면(RIS)**이다. 연구 페이지는 RIS를 전파를 흩뜨리는 수동 소자들로 이루어진 메타물질(인공 구조를 배열해 자연 물질에 없는 전자기 성질을 내는 물질)의 넓은 2차원 표면으로 설명한다. 소자마다 들어오는 신호를 반사할 때의 위상 변화 같은 전자기 성질을 조절해 더 나은 통신 채널(신호가 송신기에서 수신기까지 거치는 경로와 그 영향)을 만든다.[^ris] 밀리미터파 통신이 5G와 그 뒤의 표준이 되어 가는데 밀리미터파는 전파 경로 손실이 크고 가로막히기 쉬워 RIS의 역할이 더 커질 것이라고 보고, RIS가 에너지 효율과 여러 응용 때문에 유망하지만 송신기–RIS–수신기로 이어진 채널 때문에 시스템 설계가 복잡해진다고 적는다.[^ris] 연구 주제로는 기지국의 능동 빔포밍(여러 안테나의 신호 세기와 위상을 맞춰 전파를 원하는 방향으로 모으는 기술)과 RIS의 수동 빔포밍을 함께 설계하는 일, 반사된 신호의 채널 추정(수신 신호로 채널 상태를 알아내는 일), 여러 RIS를 배치하는 일을 든다.[^ris] 대표 논문에서는 RIS 일부 소자가 신호를 받아 감지할 수도 있을 때 상향 훈련 신호만으로 모든 연결의 채널을 추정하는 베이즈 추정기를 만들었고,[^p1] 여러 접속점이 함께 사용자를 맡는 셀 없는 대규모 MIMO에 RIS를 더한 시스템의 주파수 효율을 닫힌 식으로 분석했다.[^p2] 연구실은 무선통신용 광선 추적 모의실험기(전파가 퍼지는 경로를 광선으로 보고 반사 등을 계산해 무선 채널을 재현하는 프로그램) WiThRay를 만들었고, 관련 논문을 IEEE Access(2023)에 실었다.[^withray]

둘째 갈래는 **위성·비지상 네트워크(NTN)**다. 비지상 네트워크는 위성처럼 땅 위가 아닌 곳에 있는 통신 장치를 쓰는 망이다. 연구 페이지는 위성이 우주 공간을 통해 데이터·음성·멀티미디어를 전하며 국제 전화, 외딴 지역의 고속 인터넷 접속, 과학 연구용 실시간 자료 전달을 가능하게 한다고 소개하고, 물리 계층(통신 단계 가운데 신호를 전파로 실제 주고받는 단계)에서는 신호 감쇠, 간섭, 잡음을 다뤄야 자료가 온전하고 늦지 않게 닿는다고 적는다.[^ntn] 대표 논문에서는 저궤도 거대 위성군에서 여러 위성이 무리를 이뤄 협력하는 위성 클러스터 네트워크의 커버리지 확률을 확률 기하(점들이 무작위로 흩어진 모양을 확률 모형으로 다루는 수학) 방법으로 분석했고,[^p3] 여러 고도에 흩어진 도청 위성이 지상 단말의 상향 신호를 엿들을 때의 보안 성능을 닫힌 식으로 구했다.[^p4] 연구 과제 목록에는 3차원 공간 위성통신 기술 개발, 이종 위성군 우주 감시정찰 기술 특화연구센터, 저궤도 통신위성 코어 네트워크 가상화, 저궤도 위성 기반 VSAT(소형 위성 지구국)용 3GPP(이동통신 표준을 만드는 국제 협력 단체) NTN 기술 연구가 있다.[^projects]

셋째 갈래는 **기계학습 기반 통신**이다. 연구 페이지는 기계학습 기반 통신 시스템을 6G 이후의 유망 기술로 보고, 충분한 자료가 있으면 기계학습이 무선 시스템의 선형·비선형 특성을 찾아낼 수 있다고 적는다. 무선 시스템 구조가 복잡해지며 최적의 채널 추정기와 심볼 검출기(받은 신호에서 보낸 기호를 판정하는 장치)를 설계하기가 어려운데, 심층 신경망이 거의 최적에 가까운 채널 추정·심볼 검출 성능을 낼 수 있음이 보였다고 소개한다.[^aiml] 무선통신을 바탕으로 한 기계학습 틀로 무선 연합 학습(over-the-air federated learning, 여러 기기가 자료를 보내지 않고 학습 결과만 전파로 모아 함께 학습하는 방식) 같은 새 시스템도 들고, 실용화하려면 큰 훈련 부담과 과적합(학습 자료에만 지나치게 맞춰지는 현상)을 풀어야 한다고 적는다.[^aiml] 비트를 정확히 주고받는 기존 방식 대신 자료의 의미를 주고받아 전송 속도를 높이려는 의미 통신(semantic communication)에도 관심을 두며, DeepJSCC(심층 신경망으로 압축과 오류 대비 부호화를 함께 하는 방식), 강화학습, 생성 AI 모델로 의미 통신과 AI 기반 통신 시스템을 구현하려 한다고 적는다.[^aiml] 대표 논문에서는 메타 학습으로 새 환경에서도 적은 자료로 빨리 적응하는 대규모 MIMO 채널 예측 기법을 만들었고,[^p5] 대형 언어 모델(LLM)이 매체 접근 제어 신호를 만들어 망 환경 변화에 견디게 하는 토큰 기반 프로토콜을 제안했다.[^p6]

넷째 갈래는 **가시광 통신(VLC)**이다. 연구 페이지는 미래 무선통신이 낮은 지연, 빠른 전송 속도, 높은 신뢰성을 요구하면서도 쓸 수 있는 주파수가 제한된다고 보고, 가까운 거리 통신의 해법으로 보통 발광 다이오드(LED)를 송신기로, 광다이오드(빛을 받아 전류로 바꾸는 소자)를 수신기로 쓰는 가시광 통신을 든다. 가시광 통신은 400–790 THz 사이의 넓은 가시광 대역을 쓰고, 신호가 방향성이 있고 물체를 뚫고 지나가지 않아 무선 주파수(RF) 시스템보다 안전하며, 이것이 물리 계층 보안(암호 대신 신호의 물리적 성질로 도청을 막는 방법)을 높인다고 적는다. 기존 기반시설을 활용해 낮은 비용으로 구현할 수 있고, LED로 조명과 통신을 함께 하면서 전력 소모가 적다는 점도 든다.[^vlc] 대표 논문에서는 차량 전조등의 LED들 사이 채널이 서로 닮아 생기는 문제를 금 나노입자로 줄이고, 여러 사용자를 위한 프리코더(보내기 전에 신호를 안테나나 광원별로 미리 가공하는 장치)와 LED의 빨강·초록·파랑 광원 비율을 함께 최적화했다.[^p7] 연구 과제 목록에는 가시광 변환 집적화를 위한 바이오 나노 소자 과제(국방과학연구소)가 있다.[^projects]

다섯째 갈래는 **테라헤르츠·밀리미터파 통신과 다중 접속**이다. 연구 페이지는 테라헤르츠·밀리미터파 통신을 6G의 데이터 전송 속도를 크게 끌어올릴 핵심 요소로 보고, 테라헤르츠 대역에 아직 쓰지 않은 넓은 대역폭이 있어 초당 수 기가비트에서 테라비트까지의 전송을 지원할 수 있다고 적는다. 그 대신 전파 손실이 크고, 하드웨어 제약이 있으며, 가로막힘에 약하다는 어려움이 있어 협력 통신, RIS, 하이브리드 빔포밍(아날로그 회로와 디지털 처리로 빔포밍을 나눠 맡는 방식) 같은 생각을 쓴다고 적는다.[^thz] 그 밖의 주제로는 여러 사용자가 통신 자원을 함께 쓰게 하는 다중 접속 기술(NOMA, SDMA, RSMA)과, 고도를 바꿔 여러 지형에서 기지국 역할을 하는 무인 항공기(UAV) 통신, 센싱 기능을 통신 시스템에 녹여 넣는 통합 센싱·통신(ISAC)을 든다.[^other] 무인 항공기 통신에서는 보안 통신과 비행 시간을 늘리는 에너지 효율 향상을 다룬다고 적는다.[^other] 대표 논문에서는 테라헤르츠 통신의 커버리지를 늘리려고 협력 전송률 분할 방식을 새로 만들고 그에 맞는 테라헤르츠 협력 채널 모델과 채널 추정 기법을 제안했다.[^p8]

## 주요 연구 주제

### 1. 재구성 지능형 표면(RIS)

반사 소자 일부가 감지할 수 있는 RIS의 베이즈 채널 추정, RIS를 더한 셀 없는 대규모 MIMO의 성능 분석, 기지국·RIS 빔포밍 공동 설계, 광선 추적 모의실험기 WiThRay.[^p1][^p2][^ris][^withray] 대표 논문 1, 2.

### 2. 위성·비지상 네트워크

저궤도 위성 클러스터 네트워크의 커버리지 분석, 도청 위성이 있을 때의 위성 상향 통신 보안 분석.[^p3][^p4][^ntn] 대표 논문 3, 4.

### 3. 기계학습 기반 통신

메타 학습을 쓴 대규모 MIMO 채널 예측, 대형 언어 모델을 쓴 토큰 기반 매체 접근 제어 프로토콜, 의미 통신.[^p5][^p6][^aiml] 대표 논문 5, 6.

### 4. 가시광 통신

금 나노입자로 LED 사이 상관을 줄인 차량 가시광 통신의 다중 사용자 프리코딩, 가시광 통신의 물리 계층 보안.[^p7][^vlc] 대표 논문 7.

### 5. 테라헤르츠·밀리미터파 통신과 다중 접속

테라헤르츠 커버리지를 늘리는 협력 전송률 분할, 다중 접속(NOMA·SDMA·RSMA), 무인 항공기 통신, 통합 센싱·통신.[^p8][^thz][^other] 대표 논문 8.

## 대표 논문

랩 Journal Papers 페이지의 2021–2026년 학술지 논문 가운데 최준일 교수가 교신저자(*)로 표시된 논문을 다섯 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^journals] |
|---|---|---|---|---|
| 1 | 2023 | [Bayesian Channel Estimation for Intelligent Reflecting Surface-Aided mmWave Massive MIMO Systems With Semi-Passive Elements](https://doi.org/10.1109/twc.2023.3273284) · IEEE Transactions on Wireless Communications | 지능형 반사 표면(IRS)을 쓰는 밀리미터파 대규모 MIMO 시스템에서, 표면의 일부 소자가 능동 감지 모드로 신호를 받을 수 있는 반수동 소자일 때 쓰는 베이즈 채널 추정기를 제안했다. 기지국이 받은 신호와 표면의 소수 능동 센서가 얻은 정보로 채널 추정 오차를 줄이는 것이 목표다. 단말–표면과 표면–기지국 연결을 추정하려고 상향·하향 훈련 신호를 모두 써야 했던 기존 반수동 소자 연구와 달리, 상향 훈련 신호만으로 모든 연결을 추정한다. 평균 제곱 오차를 최소로 하는 추정값을 구하려고, 희소 베이즈 학습 틀 안에서 변분 추론(다루기 어려운 확률 분포를 다루기 쉬운 분포로 근사하는 방법)으로 채널의 사후 분포를 근사하는 VI-SBL 추정기를 만들었다. 모의실험에서 VI-SBL은 수동 반사 소자만 쓰는 기존 기준 방법들보다 추정 정확도와 훈련 부담에서 나았고, 반수동 소자를 쓴 VI-SBL이 기준 방법들보다 주파수 효율과 에너지 효율도 높았다.[^p1] | 1저자 I. Kim, 마지막 저자·교신 최준일 |
| 2 | 2026 | [RIS-Aided Cell-Free Massive MIMO Systems With Spatially Correlated Rician Fading](https://doi.org/10.1109/twc.2026.3653805) · IEEE Transactions on Wireless Communications | 셀 없는 대규모 MIMO(여러 곳에 흩어진 접속점이 셀 경계 없이 함께 사용자에게 신호를 보내는 구조) 시스템에 재구성 지능형 표면(RIS)을 더한 구성을 다뤘다. 직접 보이는 경로가 강하고 접속점 안테나와 표면 소자의 배열 구조를 반영하려고, 채널을 공간 상관 라이시안 페이딩(직접 경로와 흩어진 경로가 섞인 신호 세기 변동 모형)으로 모델링했다. 채널 추정과 데이터 전송을 분석해 합쳐진 채널과 신호의 통계를 구하고, 이 통계적 채널 정보로 상향·하향 주파수 효율의 닫힌 식을 유도했다. 모의실험으로 분석 식이 수치 실험과 맞음을 확인했고, 모든 연결이 있는 경우, 직접 연결이 없는 경우, 상관 레일리 페이딩 같은 여러 채널 상황에서 많은 시스템 변수의 영향과 RIS 위상 최적화의 쓸모를 살폈다.[^p2] | 1저자 J. Cha, 마지막 저자·교신 최준일 |
| 3 | 2025 | [Analyzing Downlink Coverage in Clustered Low Earth Orbit Satellite Constellations: A Stochastic Geometry Approach](https://doi.org/10.1109/tcomm.2025.3562517) · IEEE Transactions on Communications | 위성망은 5G 이후 전 지구 연결의 해법으로 떠오르고 있다. SpaceX, OneWeb, Amazon 같은 회사가 저궤도에 많은 위성을 쏘아 올리려 하면서, 거대 위성군 안의 위성 간 간섭이 커지는 문제가 중요해졌다. 이를 풀려고 한 무리 안의 여러 위성이 협력해 망 성능을 높이는 위성 클러스터 네트워크 개념이 나왔고, 이 논문은 그 성능을 수학적으로 분석했다. 위성과 사용자의 위치를 푸아송 점 과정(점들이 서로 상관없이 무작위로 흩어진 모양을 나타내는 확률 모형)으로 모델링하는 확률 기하 분석으로, 위성 밀도, 위성 고도, 클러스터 넓이, 경로 손실 지수, 나카가미 변수에 따른 커버리지 확률(사용자가 정해 둔 품질 이상의 신호를 받을 확률)의 하한과 상한을 구했다. 분석 식을 모의실험 결과와 비교해 확인했고, 이 분석은 시스템 변수가 커버리지에 주는 영향을 추정해 믿을 만한 위성 클러스터 네트워크를 설계하는 데 쓸 수 있다.[^p3] | 1저자 M. Lee, 마지막 저자·교신 최준일 |
| 4 | 2022 | [When Satellites Work as Eavesdroppers](https://doi.org/10.1109/tifs.2022.3188150) · IEEE Transactions on Information Forensics and Security | 지상 단말이 자신을 맡은 위성으로 신호를 올려 보내는 상향 위성통신에서, 여러 고도에 무작위로 흩어진 도청 위성들이 그 신호를 엿듣는 상황을 다뤘다. 도청 위성들은 서로 협력하지 않고 받은 신호를 각자 해독하며, 고정 빔 안테나나 방향을 바꾸는 빔 안테나로 지향성 빔포밍을 쓴다고 보았다. 도청 위성이 놓일 수 있는 경우와 단말–위성 거리의 분포를 분석하고, 맡은 위성과 가장 해로운 도청 위성에서의 신호 대 잡음비 분포를 닫힌 식으로 구했다. 이를 써서 평균 보안 용량과 중단 보안 용량(도청자가 알아낼 수 없게 보낼 수 있는 정보량), 보안 중단 확률을 유도했고, 푸아송 극한 정리로 더 간단한 근사식을, 신호 대 잡음비가 높은 영역에서는 점근 분석을 내놓았다. 몬테카를로 모의실험으로 결과를 확인했으며, 이 결과는 악의적 도청 위성의 위협을 고려해 보안 성능을 평가하고 안전한 위성군을 설계하는 데 쓰일 것으로 기대한다.[^p4] | 1저자 D.-H. Jung, 마지막 저자·교신 최준일 |
| 5 | 2023 | [Massive MIMO Channel Prediction Via Meta-Learning and Deep Denoising: Is a Small Dataset Enough?](https://doi.org/10.1109/twc.2023.3269643) · IEEE Transactions on Wireless Communications | 대규모 MIMO에서는 정확한 채널 정보가 중요해 채널 예측이 필요하다. 기계학습 채널 예측은 유망하지만 훈련 부담이 커서 환경이 바뀔 때 적응하는 데 한계가 있다. 새 환경에서도 적은 훈련 부담으로 채널을 정확히 예측하려고, 메타 학습 알고리즘 MAML(여러 과제로 미리 학습해 새 과제에 적은 자료로 빨리 맞추게 하는 방법)로 정답이 붙은 적은 자료만으로 빨리 적응하는 채널 예측 기법을 제안했다. 예측 정확도를 높이려고 심층 이미지 사전(DIP, 신경망 구조 자체를 이용해 잡음을 걸러 내는 방법)으로 훈련 자료의 잡음을 줄였다. 수치 결과에서 MAML 기반 예측기는 여러 상황에서 소수의 미세 조정 표본만으로 예측 정확도를 높였고, DIP 잡음 제거는 특히 신호 대 잡음비가 낮은 영역에서 추가 이득을 주었다.[^p5] | 1저자 H. Kim, 교신 최준일(3명 중 2번째) |
| 6 | 2026 | [Resilient LLM-Driven Token-Based MAC Protocols via Zero-Shot Adaptation and Knowledge Distillation](https://doi.org/10.1109/jsac.2025.3644282) · IEEE Journal on Selected Areas in Communications | 신경망 기반 매체 접근 제어(MAC, 여러 단말이 통신 자원을 언제 어떻게 나눠 쓸지 정하는 규칙) 프로토콜 모델(NPM)은 현장에 맞춘 동작으로 실제 전달량(goodput)을 높이지만, 단말 수 변화처럼 학습 때와 다른 망 환경을 만나면 전달량이 크게 떨어진다. 이런 변화에 견디도록 대형 언어 모델(LLM)을 쓰는 토큰 기반 MAC 프로토콜 틀 세 가지를 제안했다. 먼저 LLM이 MAC 신호 메시지를 만드는 TPM은 LLM 지시 문구를 고쳐 곧바로 적응하고 LLM 기반 자동 문구 최적화기 TextGrad로 더 나아질 수 있지만, 바뀐 환경과 실제로 주고받지 않아 결과가 거칠고 LLM이 커서 계산이 많다. 이를 보완하려고 지식 증류(큰 모델의 지식을 작은 모델에 옮겨 배우게 하는 방법)로 TPM의 지식을 NPM에 옮기는 T2NPM을 만들고, 초기에는 TPM을, 나중에는 T2NPM을 쓰는 T3NPM을 제안했다. 전환 시점을 정하려고 환경이 바뀐 뒤 알 수 없는 목표 전달량에 대한 회복력을 재는 메타 회복력 지표를 설계했고, 모의실험에서 T3NPM은 NPM보다 메타 회복력이 20.56% 높았으며 계산량(FLOPs)은 TPM보다 19.8배 적었다.[^p6] | 1저자 Y. Kim, 마지막 저자 최준일(교신 J. Park·최준일) |
| 7 | 2025 | [Multi-User SLNR-Based Precoding With Gold Nanoparticles in Vehicular VLC Systems](https://doi.org/10.1109/tcomm.2025.3591158) · IEEE Transactions on Communications | 가시광 대역은 차량 환경의 연결성과 안전을 높일 무선통신의 새 영역으로 떠오르고 있다. 차량 가시광 통신(VVLC)은 기존 기반시설을 활용할 수 있지만, 전조등 하나 안의 발광 다이오드(LED)들 사이 간격이 좁아 채널들 사이의 상관이 높고, 그래서 공간 다중화(여러 신호를 공간으로 나눠 동시에 보내는 방법)로 전송 속도를 높이기 어렵다. 새로 합성된 금 나노입자(GNP)가 들어오는 빛의 방위각에 따라 흡수 정도가 다른 광학 성질(chiroptical properties)을 써서 LED 사이의 상관을 줄였고, 여러 사용자를 지원하려고 신호 대 누설·잡음비(SLNR) 기반 프리코더를 썼다. 금 나노입자가 파장마다 다르게 흡수해 빛의 색을 바꿀 수 있어, 조명용 흰빛 조건을 지키면서 SLNR 합을 최대로 하도록 각 LED의 빨강·초록·파랑(RGB) 광원 비율도 최적화했다. 모의실험에서 최적화한 RGB 비율과 SLNR 프리코더가 여러 사용자 차량 환경의 합 전송률과 도청 상황의 보안 전송률을 크게 높였고, LED 사이 상관 줄이기와 RGB 비율 최적화가 차량 가시광 통신 성능에 꼭 필요함을 보였다.[^p7] | 1저자 G. Han, 마지막 저자·교신 최준일 |
| 8 | 2023 | [Coverage Increase at THz Frequencies: A Cooperative Rate-Splitting Approach](https://doi.org/10.1109/twc.2023.3273720) · IEEE Transactions on Wireless Communications | 많은 연구가 테라헤르츠(THz) 통신을 6세대 무선통신의 핵심 요소로 보지만, 큰 전파 손실, 하드웨어 제약, 가로막힘에 약한 점 때문에 커버리지가 줄어드는 문제가 있다. 테라헤르츠 통신의 커버리지를 늘리려고 협력 통신을 다시 살폈고, 협력 전송률 분할(CRS)의 새 형태인 추출 기반 협력 전송률 분할(eCRS)을 제안했다. 전송률 분할은 보낼 데이터를 여러 사용자가 함께 푸는 공통 부분과 각자 푸는 개별 부분으로 나눠 보내는 다중 접속 방식이다. eCRS의 두 극단인 동일 eCRS와 구별 eCRS를 살피고, 이 틀을 위해 테라헤르츠 통신의 고유한 특성을 고려한 새 협력 채널 모델을 설계했다. 수학적 유도와 볼록 최적화 기법으로 두 경우의 국소 최적해와 특정 상황에서의 전역 최적 닫힌 해를 구했고, 협력하는 각 단말에서 오는 채널 값과 그 시간 지연까지 함께 알아내는 채널 추정 기법을 제안했다. 모의실험으로 제안한 두 경우와 채널 추정 기법의 타당성을 확인했다.[^p8] | 1저자 H. Cho, 마지막 저자·교신 최준일 |

## 교수와 전문 분야

최준일 교수는 서울대학교에서 전기공학 학사(2005, 우등)와 석사(2007)를, 미국 Purdue University에서 전기·컴퓨터공학 박사(2015)를 받았다.[^prof][^eeprof] 2007–2011년 삼성종합기술원(SAIT)과 삼성전자에서 연구원(member of technical staff)으로 일하며 3GPP LTE/LTE-Advanced와 IEEE 802.16m 표준의 코드북(송신기와 수신기가 미리 나눠 가진 빔포밍 방식의 목록)과 피드백 구조 설계에 참여했다.[^prof] 2015–2016년 미국 The University of Texas at Austin 박사후연구원, 2016–2019년 POSTECH 조교수를 거쳐 2019년 8월 KAIST에 왔다. KAIST에서 조교수(2019.8–2021.8), 부교수(2021.9–2024.2)를 거쳐 2024년 3월부터 정년 보장 부교수(Tenured Associate Professor)다.[^prof][^home] 누리집 소식은 교수가 2021년 3월 Ewon Assistant Professor(endowed outstanding young faculty), 2021년 9월 Ewon Associate Professor로 임용되었고 2025년 3월부터 KAIST 석좌교수(KAIST Endowed Chair Professor)라고 적는다.[^home] 전기및전자공학부 교수 소개는 직위를 "부교수 (디비젼 체어, KAIST 석좌교수)"로, 주요 연구분야를 AI & Machine Learning, Information, Communication & Coding, Security, RF/mmWave Devices & Systems로 적는다.[^eeprof] 교수 소개가 적는 연구 관심은 대규모 MIMO, 밀리미터파 통신, 위성통신, 가시광 통신, 기계학습 기법을 쓰는 통신 시스템의 설계와 분석이다.[^prof]

교수 소개에 따르면 교수는 2022 IEEE Vehicular Technology Society Best Vehicular Electronics Paper Award, 2021 IEEE Vehicular Technology Society Neal Shepherd Memorial Best Propagation Award, 2019 IEEE Communications Society Stephen O. Rice Prize, 2015 IEEE Signal Processing Society Best Paper Award, 2013 GLOBECOM Signal Processing for Communications Symposium Best Paper Award의 공동 수상자(co-recipient)다.[^prof] 랩 학술지 목록은 이 가운데 앞의 네 상을 2014–2018년에 발표한 논문(KAIST 부임 전) 옆에 적는다.[^journals] 개인 수상으로는 Purdue University의 Michael and Katherine Birck Fellowship(2011), Korean Government Scholarship Program for Study Overseas(2011–2013), Purdue ECE GSA Outstanding Graduate Student Award(2013), Purdue College of Engineering Outstanding Student Research Award(2014), IEEE ComSoc AP Region Outstanding Young Researcher Award(2017), NSF Korea and Elsevier Young Researcher Award(2018), 한국통신학회(KICS) Haedong Young Researcher Award(2019), IEEE Communications Society Communication Theory Technical Committee Early Achievement Award(2021)를 적는다.[^prof] 누리집 소식에는 KAIST의 2020 Technology Innovation Excellence Award, Spring 2023 Excellence in Lecture Award(우수강의상), Y-KAST(the Young Korean Academy of Science and Technology) 회원 선출, S-OIL Science and Culture Foundation의 6th Next-Generation Scientist Award도 있다.[^home] 교수는 IEEE Vehicular Technology Society Distinguished Lecturer(2023–2025)이고, IEEE Open Journal of the Communications Society Area Editor, IEEE Transactions on Wireless Communications와 IEEE Transactions on Communications의 Associate Editor를 맡으며, 2026년 8월부터 IEEE TGCN의 Area Editor를 맡았다.[^prof][^home]

랩 학술지 목록을 시기별로 보면, 2018년 이전 논문은 FDD(상향과 하향 통신에 서로 다른 주파수를 쓰는 방식) 대규모 MIMO의 하향 훈련과 피드백·코드북 설계, 1비트 ADC(아날로그 신호를 1비트로만 디지털화하는 변환기)를 쓰는 대규모 MIMO, 밀리미터파 차량 통신과 빔 정렬이 많다. 2021년 이후 논문은 지능형 반사 표면, 위성 네트워크, 기계학습 기반 채널 예측·추정, 전송률 분할 다중 접속, 가시광 통신이 중심이다.[^journals] 랩 특허 목록의 미국 특허 29건 가운데 26건은 2008–2014년에 출원했고 다중 안테나(MIMO) 코드북과 채널 정보 피드백에 관한 것이 많다. 2021년에 출원한 1건은 지능형 반사 표면의 소자 할당과 빔포밍을 함께 하는 방법이다.[^patents]

논문으로 보면 지금의 전문 분야는 다섯 갈래다. 첫째, 재구성 지능형 표면의 채널 추정과 시스템 분석이다(대표 논문 1, 2).[^p1][^p2] 둘째, 저궤도 위성망의 확률 기하 분석과 보안이다(대표 논문 3, 4).[^p3][^p4] 셋째, 채널 예측과 매체 접근 제어에 기계학습과 대형 언어 모델을 쓰는 연구다(대표 논문 5, 6).[^p5][^p6] 넷째, 차량 가시광 통신이다(대표 논문 7).[^p7] 다섯째, 테라헤르츠 통신의 커버리지를 늘리는 협력 전송률 분할이다(대표 논문 8).[^p8]

## 응용 분야

누리집은 연구하는 무선통신 기술이 6G 이동통신과 그 이후의 핵심 기술이 될 것이라고 적는다.[^home] 비지상 네트워크 페이지는 위성통신의 쓰임으로 국제 전화, 외딴 지역의 고속 인터넷 접속, 과학 연구용 실시간 자료 전달을 들고,[^ntn] 그 밖의 주제 페이지는 무인 항공기 기지국이 지형 제약을 줄이고 비상 상황에서 빠르게 대응하게 하며, 통합 센싱·통신이 환경 감시, 감시(surveillance), 의료 모니터링, 지능형 기반시설 관리 같은 응용을 가능하게 한다고 적는다.[^other] 대표 논문은 차량 전조등을 쓰는 가시광 통신,[^p7] 안전한 위성군 설계,[^p4] 위성 클러스터 네트워크 설계[^p3]를 대상으로 한다. 연구 과제 목록에는 삼성전자(네트워크 사업부, S.LSI, 종합기술원), LG전자, 한화시스템, SpaceTelecom과의 산학 과제와 정보통신기획평가원, 한국전자통신연구원, 국방기술진흥연구소, 국방과학연구소, 한국산업기술진흥원, 한국연구재단 과제가 있다.[^projects] 박사 졸업생의 진로로는 Qualcomm, 한국전자통신연구원(ETRI), 국방과학연구소(ADD), 한국항공우주연구원(KARI), LG전자, 삼성전자, FuriosaAI와 경북대학교·이화여자대학교·숭실대학교·인하대학교·한국외국어대학교 조교수가 있다.[^alumni]

## 구성원

2026년 10월 22일 랩 Postdocs & Students 페이지 기준이다. Postdocs 칸 1명, Ph.D. Students 칸 15명, M.S. Students 칸 4명이다. 과정과 시작 연월은 카드의 표기(Ph.D. Program, M.S. + Ph.D. Program, M.S. Program)를 옮겼고, M.S. + Ph.D. Program은 석박사통합과정으로 적었다. 연구 주제는 카드의 Research interest이고, TBD로 적힌 칸은 미정(TBD)으로 옮겼다. Ph.D. Students 칸 6명의 카드에는 소속 기관(ADD, Samsung Electronics, ETRI, KETI)과 그 시작 연월도 적혀 있다.[^students] 연구 주제 칸의 약어 NTN은 비지상 네트워크, RIS는 재구성 지능형 표면, RSMA는 전송률 분할 다중 접속, ISAC는 통합 센싱·통신, VLC는 가시광 통신, AI/ML은 인공지능·기계학습이다. Visitors 페이지는 방문 연구자 2명(Mathieu Ardissone, ENSEA, 2025년 봄; Hyeon Seok Rou 류현석, Constructor University, 2023년 가을)을 적는다.[^visitors] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Beomsoo Ko (고범수) | 박사후연구원 |  | AI/ML | kobs0318@kaist.ac.kr | 8 |
| Miyeon Lee (이미연) | 석박사통합과정 | Sep. 2021~ | NTN | mylee0031@kaist.ac.kr | 3 |
| Taehong Min (민태홍) | 박사과정 | Sep. 2023~ | 미정(TBD) | mth1210@kaist.ac.kr |  |
| Kwonyeol Park (박권열) | 박사과정 | Sep. 2023~ | AI/ML, 6G MODEM | kwon10.park@kaist.ac.kr |  |
| Gwonhan Moon (문권한) | 박사과정 | Sep. 2024~ | 미정(TBD) | gh.mun@kaist.ac.kr |  |
| Jeonghyun Moon (문정현) | 박사과정 (Student representative) | Sep. 2024~ | RIS, RSMA | jh0908@kaist.ac.kr |  |
| Yongjun Kim (김용준) | 박사과정 | Mar. 2025~ | AI/ML | yongjunkim@kaist.ac.kr | 6 |
| Hyeongjun Park (박형준) | 박사과정 | Mar. 2025~ | NTN | mika0303@kaist.ac.kr |  |
| Jinho Yang (양진호) | 박사과정 | Mar. 2025~ | RIS, ISAC | dwplo3479@kaist.ac.kr |  |
| Juhyoung Sung (성주형) | 박사과정 | Sep. 2025~ | RIS, AI/ML | jhsung91@kaist.ac.kr |  |
| Seunggi Lee (이승기) | 박사과정 | Sep. 2025~ | VLC, NTN | seunggilee@kaist.ac.kr |  |
| Yeonjoon Choi (최연준) | 박사과정 | Sep. 2025~ | 미정(TBD) | yeonjoon.choi@kaist.ac.kr |  |
| Jinwoo An (안진우) | 석박사통합과정 | Sep. 2025~ | AI/ML | freddy1@kaist.ac.kr |  |
| Taekwan Lee (이태관) | 박사과정 | Mar. 2026~ | RIS | taekwan@kaist.ac.kr |  |
| Wooseok Cha (차우석) | 박사과정 | Mar. 2026~ | NTN | wscha@kaist.ac.kr |  |
| Sunwoo Park (박선우) | 석박사통합과정 | Sep. 2026~ | 미정(TBD) | sunwoo0428@kaist.ac.kr |  |
| Geonhee Lee (이건희) | 석사과정 | Mar. 2025~ | 미정(TBD) | peppermint01@kaist.ac.kr |  |
| Gyutae Lee (이규태) | 석사과정 | Mar. 2025~ | 미정(TBD) | kratio0440@kaist.ac.kr |  |
| Honghoon Cho (조홍훈) | 석사과정 | Mar. 2025~ | 미정(TBD) | johong1@kaist.ac.kr |  |
| Sieun Kim (김시은) | 석사과정 | Sep. 2026~ | 미정(TBD) | tldmsieun@kaist.ac.kr |  |

## 졸업생과 이전 구성원

랩 Alumni 페이지의 박사 졸업생 17명(2022년 8월–2026년 8월)과 석사 졸업생 3명(2023년 2월–2026년 2월)이다. 학위 연월과 학위 논문 제목은 랩 표기이고, 진로는 랩이 Affiliation 칸에 적은 곳을 차례대로 옮겼다. (Current)는 랩이 현재 소속으로 적은 표시다. Beomsoo Ko는 박사 졸업생이면서 지금 박사후연구원으로 구성원 표에도 있다.[^alumni][^students]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| In-soo Kim (김인수) | Ph.D. (Aug. 2022) | Qualcomm San Diego | Signal Processing Techniques for Low-Resolution ADC-Based Energy-Efficient Wireless Communications |
| Hwanjin Kim (김환진) | Ph.D. (Aug. 2022) | Postdoc at KAIST; Postdoc at Purdue University; (Current) Assistant Professor at Kyungpook National University | Massive MIMO Channel Prediction Via Adaptive Machine Learning |
| Taegyun Noh (노태균) | Ph.D. (Aug. 2022) | ETRI | IRS-Aided Cell-Free MIMO Systems |
| Sucheol Kim (김수철) | Ph.D. (Feb. 2023) | ETRI | Low Complexity Beam Designs for Practical Wireless Communication Systems |
| Hyeongtaek Lee (이형택) | Ph.D. (Aug. 2023) | Postdoc at KAIST; (Current) Assistant Professor at Ewha Womans University | Practical Communication System Design and Deployment Techniques |
| Dong-Hyun Jung (정동현) | Ph.D. (Feb. 2024) | ETRI; (Current) Assistant Professor at Soongsil University | Modeling and Analysis of Satellite Communication System Using Point Processes |
| Hyesang Cho (조혜상) | Ph.D. (Feb. 2024) | Postdoc at KAIST; (Current) Assistant Professor at Inha University | Advanced Beamformer Design Technique for Multi-User Wireless Communication System |
| Hyuckjin Choi (최혁진) | Ph.D. (Feb. 2024) | Postdoc at KAIST; Postdoc at University of California, Irvine; (Current) LG Electronics | Generating and Exploiting Realistic Channel Data for Future Wireless Communication Systems |
| Sung Hyuck Hong (홍성혁) | Ph.D. (Feb. 2024) | FuriosaAI; (Current) Qualcomm San Diego | Statistical and Machine Learning-Based Methods for Wireless Communication Systems with Channel Sparsity |
| Jaecheol Park (박재철) | Ph.D. (Aug. 2024) | ETRI | Low-Complexity Resource Allocation Algorithms for UAV Wireless Networks |
| Jihoon Cha (차지훈) | Ph.D. (Feb. 2025) | Postdoc at KAIST; (Current) ETRI | Statistical Signal Processing and Application for Future Wireless Communication Systems |
| Geonho Han (한건호) | Ph.D. (Feb. 2025) | ETRI; (Current) Samsung Electronics | Design of Visible Light Communication System Empowered by Chiroptical Properties |
| Jaeha Ahn (안재하) | Ph.D. (Aug. 2025) | ADD | Two-Timescale Precoder Design for RIS-Assisted Multiple Service Provider Systems |
| Beomsoo Ko (고범수) | Ph.D. (Feb. 2026) | Postdoc at KAIST | Data-Efficient Deep Learning-Based Channel Acquisition for Next-Generation Wireless Systems |
| Minje Kim (김민제) | Ph.D. (Feb. 2026) | ETRI | Design and Analysis of the Physical Layer in Dense Satellite Communication Systems |
| Gyoseung Lee (이교승) | Ph.D. (Feb. 2026) | LG Electronics; (Current) Assistant Professor at Hankuk University of Foreign Studies | Channel Estimation and Beamforming Designs for RIS-Aided Wireless Communication Systems |
| Saehan Song (송새한) | Ph.D. (Aug. 2026) | KARI | Beamforming Design for Practical Rate-splitting Systems with Hardware Impairment |
| Namhyun Kim (김남현) | M.S. (Feb. 2023) | SK telecom; (Current) Ph. D. at Arizona State University | Location-Aware Downlink Beamforming with Marginal Training Overhead for MmWave FDD Massive MIMO Systems |
| Hongjae Nam (남홍재) | M.S. (Aug. 2023) | Ph.D. at Purdue University | Practical Radio Resource Allocation Technique in LEO and GEO Satellite Systems |
| Jinyoung Kim (김진영) | M.S. (Feb. 2026) | LG U+; (Current) Samsung Electronics | Robust Beamforming Under Beam Split and Angular Uncertainty in Terahertz Communications |

## 최근 논문 목록 (2021–2026)

랩 Journal Papers 페이지의 2021–2026년 구역 학술지 논문 69편과 Accepted 칸의 게재 승인 논문 6편, Conference Papers 페이지의 2021–2026년 구역 학회 논문 39편으로 모두 114편이다. 게재 승인 6편은 랩이 적은 승인 연월(2026년 3·9·10월)에 따라 2026년에 두었고, 2026년 학회 논문 가운데 6편도 발표 승인(accepted to)으로 적혀 있다. 연도마다 학술지 논문을 먼저 적었다. 저자 순서와 제목·학술지·학회 표기는 랩 표기 그대로이며, 학술지 논문의 *는 랩이 교신저자로 적은 표시다.[^journals][^confs]

**2026**

- H. Cho, D. J. Love\*, and J. Choi\*. "Minimum Rate Maximization in RIS-aided Hybrid Precoding Systems via Group Rate-Splitting". *accepted to IEEE Transactions on Wireless Communications (TWC), Oct. 2026*.
- H. Cho, S. Lee, D.-H. Jung, D. J. Love\*, and J. Choi\*. "Leveraging Beam Squint for Increased LEO Coverage: An Optimization Approach". *accepted to IEEE Transactions on Wireless Communications (TWC), Oct. 2026*.
- G. Han, G. Lee, K. Park, H. V. Poor\*, and J. Choi\*. "Hybrid Beamforming in I2V Near-Field ISAC Systems for HRLLC". *accepted to IEEE Transactions on Wireless Communications (TWC), Oct. 2026*.
- M. Kim, H. Nam, B. Ko, H. Park, S. Lee, H. Kim, D.-H. Jung, and J. Choi\*. "Analysis of Beam Misalignment Effect in Inter-Satellite FSO Links". *accepted to IEEE Transactions on Communications (TCOM), Sep. 2026*.
- N. T. Nguyen\*, M. Ma, N. Shlezinger, J. Choi, Y. C. Eldar, A. L. Swindlehurst, and M. Juntti. "Knowledge Distillation for Collaborative Learning in Distributed Communications and Sensing". *accepted to IEEE Communications Magazine (COMMAG), Mar. 2026*.
- H. Kim, J. Choi\*, and D. J. Love\*. "Machine-Learning Techniques for Wireless Channel Prediction: Insights and Practical Guidance". *accepted to IEEE Wireless Communications (WCM), Mar. 2026*.
- W. Cha, K. Kim, S. Kim, J. Choi\*, and J. P. Choi\*. "Demand-Aware Cooperative Transmission Design for Energy-Efficient LEO Satellite Networks". *IEEE Transactions on Wireless Communications (TWC), vol. 25, pp. 22588-22604, Aug. 2026*.
- J. Moon, H. Cho, B. Clerckx, and J. Choi\*. "Subband Precoding Optimization in OFDM-RSMA". *IEEE Transactions on Wireless Communications (TWC), vol. 25, pp. 22371-22385, Aug. 2026*.
- J. Yang, H. Lee, and J. Choi\*. "Beam Training for RIS-Aided ISAC Systems". *IEEE Transactions on Wireless Communications (TWC), vol. 25, pp. 21199-21212, Aug. 2026*.
- Y. Kim, H. Park, H. Kim, and J. Choi\*. "Hybrid Federated Learning for Noise-Robust Training". *IEEE Wireless Communications Letters (WCL), vol. 15, pp. 4110-4114, Jul. 2026*.
- K. Park, H. Choi, G. Han, G. Lee, Y. Choi, S. Park, and J. Choi\*. "Evolution of UE in Massive MIMO for 6G: From Passive to Active". *IEEE Communications Magazine (COMMAG), vol. 64, no. 7, pp. 40-46, Jul. 2026*.
- S. Song, J. Jee, H. Cho, and J. Choi\*. "Sum Rate Maximization for Distortion-Aware RSMA System via Accelerated Gradient-Based Precoding With Near-Optimal Power Scaling". *IEEE Transactions on Communications (TCOM), vol. 74, pp. 8885-8899, May 2026*.
- J. Kim, H. Cho, and J. Choi\*. "Robust Beamforming Under Beam Split and Angular Uncertainty in Terahertz Communications". *IEEE Wireless Communications Letters (WCL), vol. 15, pp. 2649 - 2653, Apr. 2026*.
- B. Ko, G. Lee, Y. Kim, and J. Choi\*. "Channel Estimation for mmWave Systems via Deep Generative Compressed Sensing". *IEEE Transactions on Wireless Communications (TWC), vol. 25, pp. 15611-15627, Apr. 2026*.
- T. Lee, G. Lee, H. Lee, and J. Choi\*. "Weighted Sum-Rate Maximization for STAR-RIS-Aided FDD Communication Systems". *IEEE Wireless Communications Letters (WCL), vol. 15, pp. 2458-2462, Apr. 2026*.
- J. Park, J. Moon, and J. Choi\*. "Implementation and Evaluation of Hierarchical Beam Selection Algorithm for mmWave WPT Systems". *IEEE Access, vol. 14, pp. 47614-47625, Apr. 2026*.
- Y. Kim, J. Park\*, M. Bennis, and J. Choi\*. "Resilient LLM-Driven Token-Based MAC Protocols via Zero-Shot Adaptation and Knowledge Distillation". *IEEE Journal on Selected Areas in Communications (JSAC), vol. 44, pp. 2701-2717, Feb. 2026*.
- J. Cha and J. Choi\*. "RIS-Aided Cell-Free Massive MIMO Systems with Spatially Correlated Rician Fading". *IEEE Transactions on Wireless Communications (TWC), vol. 25, pp. 10635-10651, Jan. 2026*.
- G. Lee, I. Kim, Y. C. Eldar, A. L. Swindlehurst\*, H. Lee, M. Kim, and J. Choi\*. "Task-Based Quantization for Channel Estimation in RIS Empowered MmWave Systems". *IEEE Transactions on Communications (TCOM), vol. 74, pp. 106-122, Jan. 2026*.
- K. Park, G. Lee, H. Lee, H. Kim, and J. Choi\*. "Downlink Channel Estimation for mmWave Systems with Impulsive Interference". *IEEE Wireless Communication Letters (WCL), vol. 15, pp. 330-334, Jan. 2026*.
- M. Kim, H. Park, G. Lee, D.-H. Jung, G. Im, J.-G. Ryu, and J. Choi. "Geometry-Aware Pointing Error Channel Modeling for Optical Inter-Satellite Links". *accepted to IEEE Vehicular Technology Conference (VTC), Jun. 2026*.
- J. Sung, J. Kang, and J. Choi. "Deep Learning based Hybrid Beamforming for ISAC with Aligned Communication and Sensing Objectives". *accepted to IEEE International Workshop on Signal Processing and Artificial Intelligence for Wireless Communications (SPAWC), Jun. 2026*.
- S. Lee, G. Han, H. Cho, H. Choi, and J. Choi. "Physical Layer Security of UAV-based FSO Communications Using Gold Nanoparticles". *accepted to IEEE International Workshop on Signal Processing and Artificial Intelligence for Wireless Communications (SPAWC), Jun. 2026*.
- Y. Kim, A. Dhananjay, S. Rangan, S. Shetty, C. N. Barati, M. Zappe, K. Gold, and J. Choi. "A Self-Calibrating SDR for High Fidelity Beam-and Null-forming Arrays". *accepted to IEEE International Workshop on Signal Processing and Artificial Intelligence for Wireless Communications (SPAWC), Jun. 2026*.
- W. Cha, K. Kim, S. Kim, J. P. Choi, and J. Choi. "Energy-Efficient Resource Optimization for Traffic-Driven Cell-Free LEO Satellite Communications". *accepted to Asia-Pacific International Symposium on Aerospace Technology (APISAT), Jun. 2026*.
- H. Park, M. Kim, H. Choi, J. Yang, and J. Choi. "Physical-Layer Security Design Using Channel Distribution for Integrated Satellite-Terrestrial Networks". *accepted to Asia-Pacific International Symposium on Aerospace Technology (APISAT), Jun. 2026*.
- G. Lee, I. Kim, B. Ko, K. Park, H. V. Poor, and J. Choi. "Advanced Bayesian Channel Estimation for Semi-Passive RIS-Empowered mmWave Systems". *in Proc. of IEEE International Conference on Communications (ICC), May 2026*.
- R. Bomfin, A. Rasteh, M. Kim, H. Park, H. Guo, H. Lee, M. Mezzavila, S. Rangan, J. Choi, and M. Chafii. "Multi-Band Integrated Sensing and Communication Channel Measurements in the FR3". *in Proc. of IEEE International Conference on Communications (ICC), May 2026*.
- B. Ko, G. Lee, Y. Kim, and J. Choi. "Generative Model-Based Compressed Sensing for mmWave Channel Estimation through Sequential Path Reconstruction". *in Proc. of IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), May 2026*.
- S.-H. Hong and J. Choi. "Joint Channel Estimation and Beamforming for Reconfigurable Intelligent Surface Aided MIMO Systems: Sparsity-Based Approach". *in Proc. of International Conference on Computing, Networking and Communications (ICNC), Feb. 2026*.

**2025**

- G. Han, H. Choi, H. Cho, J.-H. Han, K.-T. Nam, and J. Choi\*. "Multi-User SLNR-Based Precoding With Gold Nanoparticles in Vehicular VLC Systems". *IEEE Transactions on Communications (TCOM), vol. 73, no. 12, pp. 14653-14667, Dec. 2025*.
- J. Cha, H. Kim, and J. Choi\*. "Meta-Learning-Based People Counting and Localization Models Employing CSI from Commodity WiFi NICs". *IEEE Internet of Things Journal (IOTJ), vol. 12, no. 23, pp. 51224-51239, Dec. 2025*.
- M. Lee, S. Kim, M. Kim, D.-H. Jung, and J. Choi\*. "Analyzing Downlink Coverage in Clustered Low Earth Orbit Satellite Constellations: A Stochastic Geometry Approach". *IEEE Transactions on Communications (TCOM), vol. 73, no. 11, pp. 12174-12188, Nov. 2025*.
- L. V. Nguyen, J. Choi, B. Ottersten, and A. L. Swindlehurst. "Channel-Coded Precoding for Multi-User MISO Systems". *IEEE Transactions on Wireless Communications (TWC), vol. 24, no. 11, pp. 9201-9216, Nov. 2025*.
- G. Lee and J. Choi\*. "A Bayesian Framework For Cascaded Channel Estimation in RIS-Aided mmWave Systems". *IEEE Wireless Communications Letters (WCL), vol. 14, no. 11, pp. 3799-3803, Nov. 2025*.
- G. Joseph\*, V. Gandikota, A. Bhandari, J. Choi, I. Kim, G. Lee, M. Matthaiou, C. R. Murthy, H. Q. Ngo, P. Varshney, T. Wimalajeewa, W. Yi, Y. Yuan, and G. Zhang. "Low-Resolution Compressed Sensing and Beyond for Communications and Sensing: Trends and Opportunities". *Signal Processing, vol. 235, Oct. 2025*.
- D.-H. Jung, H. Nam, J. Choi\*, and D. J. Love. "Modeling and Analysis of Hybrid GEO-LEO Satellite Networks". *IEEE Communications Letters (COMML), vol. 29, no. 9, pp. 2053-2057, Sep. 2025*.
- J. Park, M. Kim, K. Kang, J. Moon, and J. Choi\*. "Low-Complexity Algorithm for Minimum Rate Maximization in UAV-Enabled OFDMA Networks". *IEEE Wireless Communications Letters (WCL), vol. 14, no. 10, pp. 3359-3363, Oct. 2025*.
- H. Cho and J. Choi\*. "Sum Rate Maximization with Rate-Splitting Multiple Access for Hybrid Precoding Systems". *IEEE Transactions on Communications (TCOM), vol. 73, no. 9, pp. 7874-7886, Sep. 2025*.
- J. Yang, H. Lee, and J.Choi\*. "Robust Transmission Design for Active RIS-Aided Systems". *IEEE Transactions on Vehicular Technology (TVT), vol. 74, no. 7, pp. 11591-11596, Jul. 2025*.
- J. Moon, H. Cho, and J. Choi\*. "Sum Rate Maximization Via STAR-RIS Element Allocation in OFDM Systems". *IEEE Transactions on Vehicular Technology (TVT), vol. 74, no. 3, pp. 5199-5204, Mar. 2025*.
- K. Park, H. Choi, B. Ko, M. Kim, G. Lee, D. Kwon, H. Park, B. Kim, M. Shin, and J. Choi\*. "Anomaly Detection-Based UE-Centric Inter-Cell Interference Suppression". *IEEE Open Journal of the Communications Society (OJCOMS), vol. 6, pp. 1512-1527, Feb. 2025*.
- C.-S. Choi\*, J. Kim, and J. Choi. "Stochastic Geometry Analysis of RIS-Assisted Cellular Networks with Reflective Intelligent Surfaces on Roads". *IEEE Transactions on Communications (TCOM), vol. 73, no. 2, pp. 859-873, Feb. 2025*.
- H. Lee and J. Choi\*. "RIS-Enabled Cellular Systems Operated by Multiple Service Providers". *IEEE Transactions on Vehicular Technology (TVT), vol. 74, no. 2, pp. 3451-3456, Feb. 2025*.
- M. Kim, H. Nam, B. Ko, H. Park, H. Kim, D.-H. Jung, and J. Choi. "Statistical Characterization of Misaligned FSO Links in SWaP-Limited CubeSat Constellations". *presented to Asia-Pacific International Symposium on Aerospace Technology (APISAT), Oct. 2025*.
- S. Lee, G. Han, M. Lee, and J. Choi. "Secure HAPS Based FSO Communications Using Metamaterials". *in Proc. of International Conference on Information and Communication Technology Convergence (ICTC), Oct. 2025*.
- K. Park, H. Choi, B. Ko, M. Kim, G. Lee, B. Kim, M. Shin, and J. Choi. "UE-Centric Inter-Cell Interference Mitigation: An Anomaly Detection Approach". *in Proc. of IEEE International Workshop on Signal Processing and Artificial Intelligence for Wireless Communications (SPAWC), Jul. 2025*.
- B. Ko, H. Kim, M. Kim, and J. Choi. "Machine Learning-Based Channel Prediction with Reduced Training Overhead for Massive MIMO-OFDM Systems". *in Proc. of IEEE Wireless Communications and Networking Conference (WCNC), Mar. 2025*.
- H. Cho, J. Moon, and J. Choi. "Minimum Rate Maximization With RIS Element Allocation in OFDM Systems". *in Proc. of IEEE Wireless Communications and Networking Conference (WCNC), Mar. 2025*.

**2024**

- D.-H. Jung, H. Nam, J. Choi\*, and D. J. Love. "Modeling and Analysis of GEO Satellite Networks". *IEEE Transactions on Wireless Communications (TWC), vol. 23, no. 11, pp. 16757-16770, Nov. 2024*.
- H. Rou, G. Abreu, J. Choi, M. Kountouris, Y. L. Guan, and O. Gonsa. "From OTFS to AFDM: A Comparative Study of Next-Generation Waveforms for ISAC in Doubly-Dispersive Channels". *IEEE Signal Processing Magazine (SPM), vol. 41, no. 5, pp. 71-86, Nov. 2024*.
- H. Cho, J. Moon, and J. Choi\*. "Low Complexity RIS Update in OFDM Systems via RIS Element Allocation". *IEEE Transactions on Wireless Communications (TWC), vol. 23, no. 10, pp. 15142-15154, Oct. 2024*.
- J. Lv, J. H. Han, G. Han, S. An, S. J. Kim, R. M. Kim, J.-E. Ryu, R. Oh, H. Choi, I.H. Ha, Y. H. Lee, M. Kim, G.-S. Park, H. W. Jang, J. Doh, J. Choi\*, and K.T. Nam\*. "Spatiotemporally modulating full-polarized light emission for multiplexed optical encryption". *Nature Communications, 15, 8257, Sep. 2024*.
- M. Kim, I.Kim, and J. Choi\*. "Meta-Heuristic Fronthaul Bit Allocation for Cell-free Massive MIMO Systems". *IEEE Transactions on Wireless Communications (TWC), vol. 23, no. 9, pp. 11737-11752, Sep. 2024*.
- H. Cho and J. Choi\*. "Smart Resource Allocation at mmWave/THz Frequencies with Cooperative Rate-Splitting". *IEEE Transactions on Wireless Communications (TWC), vol. 23, no. 9, pp. 11030-11042, Sep. 2024*.
- B. Ko, H. Kim, M. Kim, and J. Choi\*. "Machine Learning-based Channel Prediction in Wideband Massive MIMO Systems with Small Overhead for Adaptive Online Training". *IEEE Open Journal of the Communications Society (OJCOMS), vol. 5, pp. 5289-5305, Sep. 2024*.
- H. Choi, A. L. Swindlehurst, and J. Choi\*. "WMMSE-Based Rate Maximization for RIS-Assisted MU-MIMO Systems". *IEEE Transactions on Communications (TCOM), vol. 72, no. 8, pp. 5194-5208, Aug. 2024*.
- H. Lee, S. Moon, Y. Lee, J. Oh, J. Chung, and J. Choi\*. "Multi-Group Multicasting Systems Using Multiple RISs". *IEEE Transactions on Wireless Communications (TWC), vol. 23, no. 8, pp. 9488-9501, Aug. 2024*.
- G. Lee, H. Lee, D. Kim, J. Chung, A. L. Swindlehurst, and J. Choi\*. "Joint Downlink and Uplink Optimization for RIS-Aided FDD MIMO Communication Systems". *IEEE Transactions on Wireless Communications (TWC), vol. 23, no. 8, pp. 9059-9071, Aug. 2024*.
- G. Han, H. Choi, R. Kim, K. Nam, J. Choi\* and T. A. Tsiftsis. "On the Physical Layer Security of Visible Light Communications Empowered by Gold Nanoparticles". *Journal of Optical Communications and Networking (JOCN), vol. 16, no. 7, pp. 750-763, Jun. 2024*.
- J. Park, B. Lee, J. Choi, H. Lee, N. Lee, S. Park, K. Lee, J. Choi, S. H. Chae, S. Jeon, K. S. Kwak, B. Clerckx, and W. Shin. "Rate-Splitting Multiple Access for 6G Networks: Ten Promising Scenarios and Applications". *IEEE Network, vol. 38, no. 3, pp. 128-136, Jun. 2024*.
- J. Park, S.-W. Ko, J. Choi, S.-L. Kim, J. Choi, and M. Bennis. "Towards Semantic MAC Protocols for 6G: From Protocol Learning to Language-Oriented Approaches". *accepted to IEEE BITS the Information Theory Magazine, vol. 4, no. 1, pp. 59-72, Mar. 2024*.
- D.-H. Jung, J. Ryu, and J. Choi\*. "Satellite Clustering for Non-Terrestrial Networks: Orbital Configuration-Dependent Outage Analysis". *IEEE Wireless Communications Letters (WCL), vol. 13, no. 2, pp. 550-554, Feb. 2024*.
- J. Park, K. Kang, and J. Choi\*. "K-Means Clustering-Aided Power Control for UAV-Enabled OFDM Networks". *IEEE Access, vol.12, pp. 15549-15560, Jan. 2024*.
- D.-H. Jung, S. Kim, M. Lee, J.-G. Ryu, and J.Choi. "UV-plane Beam Mapping for Non-Terrestrial Networks in 3GPP System-Level Simulations". *in Proc. of IEEE Asia Pacific Conference on Communications (APCC), Nov. 2024*.
- J. Cha, H. Kim, and J. Choi. "Adaptive People Counting and Localization Based on Meta Learning with WiFi NICs". *in Proc. of Asilomar Conference on Signals, Systems, and Computers, Oct. 2024*.
- H. Park, M. Kim, and J. Choi. "Physical Layer Security of AF-Based Hybrid Satellite-Terrestrial Networks". *in Proc. of International Conference on Information and Communication Technology Convergence (ICTC), Oct. 2024*.
- S. Kim, D.-H. Jung, M. Lee, J-G. Ryu, and J. Choi. "Conversion of Coordinate System in 3GPP Channel Model". *in Proc. of International Conference on Information and Communication Technology Convergence (ICTC), Oct. 2024*.
- D.-H. Jung, H. Nam, and J. Choi. "Coverage analysis of GEO satellite networks". *in Proc. of International Symposium on Modeling and Optimization in Mobile, Ad hoc, and Wireless Networks (WiOpt), Oct. 2024*.
- M. Lee, S. Kim, M. Kim, D.-H. Jung, and J. Choi. "Performance Analysis of Satellite Cluster system in Mega-Constellations". *in Proc. of IEEE International Symposium of Personal, Indoor and Mobile Radio Communications (PIMRC), Sep. 2024*.
- M. Kim, I. Kim, and J. Choi. "Harmony Search-Based Quantization Bit Allocation on Cell-Free Massive MIMO Systems". *in Proc. of European Conference on Signal Processing (EUSIPCO), Aug. 2024*.
- G. Lee, I. Kim, Y. C. Eldar, A. L. Swindlehurst, and J. Choi. "Channel Estimation for RIS-Aided Communication Systems: A Task-Based Quantization Approach". *in Proc. of International Symposium on Wireless Communication Systems (ISWCS), Jul. 2024*.
- H. Choi, V. L. Nguyen, J. Choi, and A. L. Swindlehurst. "A Deep Reinforcement Learning Approach for Autonomous Reconfigurable Intelligent Surfaces". *in Proc. of IEEE International Conference on Communications Workshops (ICC), Jun. 2024*.
- Y. Kim, S. Seo, J. Park, M. Bennis, S. L. Kim, and J. Choi. "Knowledge Distillation from Language-Oriented to Emergent Communication for Multi-Agent Remote Control". *in Proc. of IEEE International Conference on Communications (ICC), Jun. 2024*.
- G. Lee, H. Lee, A. L. Swindlehurst, and J. Choi. "Two-way Optimization for RIS Empowered FDD MIMO Communication Systems". *in Proc. of IEEE Wireless Communications and Networking Conference (WCNC), Apr. 2024*.

**2023**

- H. Cho, B. Ko, B. Clerckx, and J. Choi\*. "Coverage Increase at THz Frequencies: A Cooperative Rate-Splitting Approach". *IEEE Transactions on Wireless Communications (TWC), vol. 22, no. 12, pp. 9821-9834, Dec. 2023*.
- I. Kim, M. Bennis, J. Oh, J. Chung, and J. Choi\*. "Bayesian Channel Estimation for Intelligent Reflecting Surface-Aided mmWave Massive MIMO Systems with Semi-Passive Elements". *IEEE Transactions on Wireless Communications (TWC), vol. 22, no. 12, pp. 9732-9745, Dec. 2023*.
- H. Kim, J. Choi\*, and D. J. Love. "Massive MIMO Channel Prediction Via Meta-Learning and Deep Denoising: Is a Small Dataset Enough?". *IEEE Transactions on Wireless Communications (TWC), vol. 22, no. 12, pp. 9278-9290, Dec. 2023*.
- D.-H. Jung, G. Im, J. Ryu, S. Park, H. Yu, and J. Choi\*. "Satellite Clustering for Non-Terrestrial Networks: Concept, Architectures, and Applications". *IEEE Vehicular Technology Magazine (VTM), vol. 18, no. 3, pp. 29-37, Sep. 2023*.
- H. Choi, J. Oh, J. Chung, G. C. Alexandropoulos, and J. Choi\*. "WiThRay: A Versatile Ray-Tracing Simulator for Smart Wireless Environments". *IEEE Access, vol. 11, pp. 56822-56845, Jun. 2023*.
- G. Lee, H. Lee, J. Oh, J. Chung, and J. Choi\*. "Channel Estimation for Reconfigurable Intelligent Surface with a few Active Elements". *IEEE Transactions on Vehicular Technology (TVT), vol. 72, no. 6, pp. 8170-8174, Jun. 2023*.
- S. Kim, H. Lee, H. Kim, Y. Choi, and J. Choi\*. "Complete Power Reallocation for MU-MIMO under Per-Antenna Power Constraint". *IEEE Transactions on Communications (TCOM), vol. 71, no. 4, pp. 2087-2103, Apr. 2023*.
- J. Lee, J. Choi, and J. Kang\*. "Harmony Search-Based Optimization for Multi-RISs MU-MISO OFDMA Systems". *IEEE Wireless Communications Letters (WCL), vol. 12, no. 2, pp. 257-261, Feb. 2023*.
- S. Kim, H. Lee, H. Kim, and J. Choi. "Multi-User Beamforming under Per-Antenna Power Constraint". *in Proc. of International Conference on Information and Communication Technology Convergence (ICTC), Oct. 2023*.
- H. Cho, B. Ko, B. Clerckx, and J. Choi. "Cooperative Rate-Splitting for Enhanced THz Frequency Coverage". *in Proc. of IEEE International Symposium of Personal, Indoor and Mobile Radio Communications (PIMRC), Sep. 2023*.
- H. Ryu and J. Choi. "EMC2-Net: Joint Equalization and Modulation Classification Based on Constellation Network". *in Proc. of IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Jun. 2023*.

**2022**

- H. Cho and J. Choi\*. "Energy Minimization for UAV Communication Systems Assisted with Multiple IRSs". *Journal of Communications and Networks (JCN), vol. 24, no. 5, pp. 566-578, Oct. 2022*.
- G. Han, J. Choi\*, and R. W. Heath Jr. "Radar Imaging Based on IEEE 802.11ad Waveform in V2I Communications". *IEEE Transactions on Signal Processing (TSP), vol. 70, pp. 4981 - 4996, Oct. 2022*.
- I. Kim, M. Bennis, and J. Choi\*. "Cell-Free MmWave Massive MIMO Systems with Low-Capacity Fronthaul Links and Low-Resolution ADC/DACs". *IEEE Transactions on Vehicular Technology (TVT), vol. 71, no. 10, pp. 10512-10526, Oct. 2022*.
- S. Hong, J. Park, S. Kim, and J. Choi\*. "Hybrid Beamforming for Intelligent Reflecting Surface Aided Millimeter Wave MIMO Systems". *IEEE Transactions on Wireless Communications (TWC), vol. 21, no. 9, pp. 7343 - 7357, Sep. 2022*.
- S. Kim, H. Lee, J. Cha, S. Kim, J. Park, and J. Choi\*. "Practical Channel Estimation and Phase Shift Design for Intelligent Reflecting Surface Empowered MIMO Systems". *IEEE Transactions on Wireless Communications (TWC), vol. 21, no.8, pp. 6226 - 6241, Aug. 2022*.
- D.-H. Jung, J. Ryu, and J. Choi\*. "When Satellites Work as Eavesdroppers". *IEEE Transactions on Information Forensics and Security (TIFS), vol. 17, pp. 2784-2799, Jul. 2022*.
- J. Cha, J. Choi\*, and D. J. Love. "Practical Distributed Reception for Wireless Body Area Networks Using Supervised Learning". *IEEE Transactions on Wireless Communications (TWC), vol. 21, no.7, pp. 4898-4908, Jul. 2022*.
- S. Moon, H. Lee, J. Choi, and Y. Lee\*. "Low-Complexity Beamforming Optimization for IRS-Aided MU-MIMO Wireless Systems". *IEEE Transactions on Vehicular Technology (TVT), vol. 71, no. 5, pp. 5587-5592, May 2022*.
- D.-H. Jung, J. Ryu, W. Byun, and J. Choi\*. "Performance Analysis of Satellite Communication System Under the Shadowed-Rician Fading: A Stochastic Geometry Approach". *IEEE Transactions on Communications (TCOM), vol. 70, no. 4, pp. 2707-2721, Apr. 2022*.
- T. Noh and J. Choi\*. "Cell-Free MIMO Systems Powered by Intelligent Reflecting Surfaces". *IEEE Communications Letters (COMML), vol. 26, no. 5, pp. 1076 - 1080, Feb. 2022*.
- S. Kim, H.Lee, J. Cha, and J. Choi. "Channel Estimation for Intelligent Reflecting Surface Assisted MmWave Systems Using Analog Feedback". *in Proc. of IEEE Sensor Array and Multichannel Signal Processing Workshop (SAM), Jun. 2022*.
- S. Kim, H.Lee, J. Cha, and J. Choi. "Parameter-Based Channel Estimation for Intelligent Reflecting Surface Aided MIMO Systems". *in Proc. of IEEE Wireless Communications and Networking Conference (WCNC), Apr. 2022*.
- H. Cho and J. Choi. "Energy Efficient UAV Communication via Multiple Intelligent Reflecting Surfaces". *in Proc. of IEEE Wireless Communications and Networking Conference Workshop (WCNC), Apr. 2022*.

**2021**

- J. Park, K. Kang, and J. Choi\*. "Low-Complexity Algorithm for Outage Optimal Resource Allocation in Energy Harvesting-Based UAV Identification Networks". *IEEE Communications Letters (COMML), vol. 25, no. 11, pp. 3639-3643, Nov. 2021*.
- H. Lee, H. Choi, H. Kim, S. Kim, C. Jang, Y. Choi, and J. Choi\*. "Downlink Channel Reconstruction for Spatial Multiplexing in Massive MIMO Systems". *IEEE Transactions on Wireless Communications (TWC), vol. 20, no. 9, pp. 6154-6166, Sep. 2021*.
- J. Kang, J. Choi, and W. Choi\*. "Multi-user Energy Beamforming for Different Energy Requests". *IEEE Wireless Communications Letters (WCL), vol. 10, no. 8, Aug. 2021*.
- I. Kim and J. Choi\*. "Spatial Wideband Channel Estimation for MmWave Massive MIMO Systems with Hybrid Architectures and Low-Resolution ADCs". *IEEE Transactions on Wireless Communications (TWC), vol. 20, no. 6, pp. 4016-4029, Jun. 2021*.
- H. Cho and J. Choi\*. "Alternating Beamforming with Intelligent Reflecting Surface Element Allocation". *IEEE Wireless Communications Letters (WCL), vol. 10, no. 6, pp. 1232-1236, Jun. 2021*.
- H. Cho and J. Choi\*. "Sum Rate Maximization through Intelligent Reflecting Surface Element Allocation". *The Journal of Korean Institute of Communications and Information Sciences (J-KICS), vol. 46, no. 4, pp. 750-756, Apr. 2021*.
- S. Hong, S. Kim, J. Choi\*, and W. Choi. "Polar-Cap Codebook Design for MISO Rician Fading Channels with Limited Feedback". *IEEE Wireless Communications Letters (WCL), vol. 10, no. 4, pp. 730-734, Apr. 2021*.
- H. Kim, S. Kim, H. Lee, C. Jang, Y. Choi, and J. Choi\*. "Massive MIMO Channel Prediction: Kalman Filtering Vs. Machine Learning". *IEEE Transactions on Communications (TCOM), vol. 69, no. 1, pp. 518-528, Jan. 2021*.
- S. Hong and J. Choi. "Phase Shift Design for Intelligent Reflecting Surface Aided mmWave MIMO Systems". *in Proc. of IEEE Global Communications Conference Workshop (GLOBECOM), Dec. 2021*.
- B. Ko, H. Kim, and J. Choi. "Machine Learning-Based Channel Prediction Exploiting Frequency Correlation in Massive MIMO Wideband Systems". *in Proc. of International Conference on Information and Communication Technology Convergence (ICTC), Oct. 2021*.
- H. Choi and J. Choi. "WiThRay: Versatile 3D Simulator for Intelligent Reflecting Surface-aided MmWave Systems". *in Proc. of IEEE international Symposium on Antennas and Propagation (ISAP), Oct. 2021*.
- I. Kim and J. Choi. "Gridless Channel Estimation for mmWave Hybrid Massive MIMO Systems with Low-Resolution ADCs". *in Proc. of IEEE Statistical Signal Processing Workshop (SSP), Jul. 2021*.
- H. Lee, H. Choi, H. Kim, S. Kim, and J. Choi. "Downlink Channel Reconstruction for Massive MIMO Spatial Multiplexing". *in Proc. of IEEE International Conference on Communications (ICC), Jun. 2021*.
- G. Han, S. Kim, and J. Choi. "Multi-Vehicle Velocity Estimation Using IEEE 802.11 ad Waveform". *in Proc. of IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Jun. 2021*.
- I. Kim and J. Choi. "Performance of Cell-Free MmWave Massive MIMO Systems with Fronthaul Compression and DAC Quantization". *in Proc. of IEEE Wireless Communications and Networking Conference Workshops (WCNC), Mar. 2021*.

## 특허

랩 Patents 페이지의 미국 특허 29건 가운데 출원일이 2021년인 1건이다. 나머지 28건의 출원일은 2008–2019년이다. 제목·번호·발명자는 랩 표기 그대로다.[^patents]

- Integrated Beamforming Method with Intelligent Reflecting Surface Element Allocation and System Therefore (국가 US Patent; 번호 11,515,918 B2; 발명자 J. Choi and H. Cho; 출원일 Feb. 18, 2021)

## 연구 과제

랩 Projects 페이지의 과제 32건(Ongoing 10, Finished 22) 가운데 수행 기간이 2021년 10월–2026년 10월과 겹치는 23건(Ongoing 10, Finished 13)이다. 기간과 지원 기관·과제명은 랩 표기 그대로다. 이 가운데 1건(한국연구재단, Beyond 5G 무선통신 시스템을 위한 A-COMM 시스템 연구, 2019년 3월–2022년 2월)은 교수의 KAIST 부임(2019년 8월) 전에 시작했다.[^projects][^prof]

- Jun. 2026 ~ Apr. 2027 · 삼성전자 네트워크 사업부 - 6G 융합 네트워크를 위한 ISAC 및 위성통신 핵심 기술 개발 (상태 Ongoing)
- Jun. 2026 ~ May 2028 · 한화시스템 - LEO 통신위성 코어 네트워크 NFV/SDN 기반 가상화 인프라 구축 연구 (상태 Ongoing)
- May 2026 ~ Oct. 2027 · SpaceTelecom - LEO 위성 기반 VSAT 용 3GPP NTN 기술 연구 (상태 Ongoing)
- Oct. 2025 ~ Sep. 2030 · 삼성전자 S.LSI 전략산학과제 - AI기반 무선통신 알고리즘 및 표준 framework 연구 (상태 Ongoing)
- Jul. 2025 ~ Dec. 2029 · 한국과학기술원 (KAIST) - 항공우주 AI전환 연구단 (상태 Ongoing)
- Jan. 2025 ~ Dec. 2028 · 정보통신기획평가원 (IITP) - Upper-mid Band를 지원하는 Cloud virtualized RAN (vRAN) 시스템 기술 개발 (상태 Ongoing)
- Jul. 2024 ~ Dec. 2028 · 정보통신기획평가원 (IITP) - 오픈랜인력양성프로그램 (카이스트-서울대) (상태 Ongoing)
- Jul. 2024 ~ Dec. 2028 · 정보통신기획평가원 (IITP) - 차세대통신클라우드리더십 구축 (상태 Ongoing)
- Dec. 2022 ~ Dec. 2028 · 국방기술진흥연구소 (KRIT) - 이종 위성군 우주 감시정찰 기술 특화연구센터 (상태 Ongoing)
- Jul. 2020 ~ Dec. 2027 · 대학ICT연구센터육성지원사업 (ITRC) - 초지능 서비스를 위한 통신/컴퓨팅 융합혁신기술 개발 (상태 Ongoing)
- Feb. 2024 ~ May 2026 · 삼성전자 S.LSI 기술산학과제 - 머신러닝 기반 5G/6G 통신 알고리즘 및 표준 framework 연구 (상태 Finished)
- Mar. 2025 ~ Dec. 2025 · 사이버안보연구소 - 비지상 네트워크(NTN) 통신 신호체계 (상태 Finished)
- Apr. 2021 ~ Dec. 2025 · 정보통신기획평가원 (IITP) - 6세대 Tbps급 데이터 전송율을 지원하는 sub-THz 대역 무선 전송 및 접속 요소 기술 개발 (상태 Finished)
- Apr. 2021 ~ Dec. 2025 · 한국전자통신연구원 (ETRI) - 3차원 공간 위성통신 기술 개발 (상태 Finished)
- Nov. 2024 ~ Nov. 2025 · LG전자 - 6G 통신 기술: 서비스 구현을 위한 다목적 지능형 반사 표면 개발 (상태 Finished)
- Nov. 2020 ~ Oct. 2025 · 국방과학연구소 (ADD) - 가시광 변환 집적화를 위한 바이오 나노 소자 (상태 Finished)
- Dec. 2023 ~ Oct. 2024 · 삼성전자 종합기술원 (SAIT) - Ray Tracing 기반 True-Real 시스템 레벨 모델 시뮬레이터 개발 (상태 Finished)
- Nov. 2022 ~ Oct. 2024 · 한국산업기술진흥원 (KIAT) - 미래 무선 통신을 위한 인공지능 기반 지능형 재구성 반사체 기술 개발 (AI-powered Reconfigurable Intelligent Surfaces) (상태 Finished)
- Sep. 2020 ~ Sep. 2023 · 삼성전자 - 거대 다중 안테나 시스템에서 극소수 학습을 통한 저복잡도 채널 예측 기법 (상태 Finished)
- Jul. 2020 ~ Dec. 2022 · 정보통신기획평가원 (IITP) - WiFi 미세전력 무선신호 센싱 기반 건물 내 위험상황인지 플랫폼 개발 (상태 Finished)
- Oct. 2021 ~ Oct. 2022 · LG전자 - 6G 통신 기술: 지능형 반사 표면 기반 통신 시스템에서의 실질적 응용 기법 제안 및 검증 (상태 Finished)
- Mar. 2019 ~ Feb. 2022 · 한국연구재단 (NRF) - Beyond 5G 무선통신 시스템을 위한 A-COMM 시스템 연구 (상태 Finished)
- Jul. 2020 ~ Nov. 2021 · 한국연구재단 (NRF) - 실시간 고해상도 In-Vivo Imaging을 위한 초고속 체내 데이터 전송기술 연구실 (상태 Finished)

## 소식

랩 첫 화면 Recent News 칸의 72줄 가운데, 2021년 9월 Ewon Associate Professor 승진 소식보다 뒤에 올라온 56줄이다. 최근 글이 위에 오는 게시 순서 그대로 옮겼다. 대부분의 글에는 날짜가 적혀 있지 않아, 글 안에 적힌 연월만 있다. 글은 랩 표기 그대로다.[^home]

- Taekwan received NRF Research Subsidies for Ph.D. Candidates.
- Junil has started serving IEEE TGCN as the Area Editor from Aug. 2026.
- Gyoseung joined Hankuk University of Foreign Studies as an Assistant Professor in Sep. 2026.
- Saehan successfully finished his Ph.D. defense in Jun. 2026.
- Hyesang received the KICS Winter Conference 2026 Best Paper Award.
- Gyoseung received the 2026 KAIST College of Engineering Ph.D. Dissertation Award.
- Hyesang joined Inha University as an Assistant Professor in Mar. 2026.
- Beomsoo, Gyoseung, and Minje successfully finished their Ph.D. defense in Dec. 2025.
- Jinyoung and Taekwan successfully finished their M.S. defense in Dec. 2025.
- Jaeha successfully finished his Ph.D. defense in Jun. 2025.
- Seunggi successfully finished his M.S. defense in Jun. 2025.
- Geonho received the 2025 KAIST EE Best Ph.D. Dissertation Award in Apr. 2025.
- Junil has been appointed as a KAIST Endowed Chair Professor from Mar. 2025.
- Dong-Hyun joined Soongsil University as an Assistant Professor in Mar. 2025.
- Hyeongtaek joined Ewha Womans University as an Assistant Professor in Mar. 2025.
- Geonho and Jihoon successfully finished their Ph.D. defense in Dec. 2024.
- Hyeongjun, Jinho, and Yongjun successfully finished their M.S. defenses in Dec. 2024.
- Junil received the 6th Next-Generation Scientist Award the S-OIL Science and Culture Foundation.
- Dong-Hyun received the 2024 Haedong Young Researcher Award from KICS.
- Gyoseung received the 2024 KAIST Graduate Student Outstanding Paper Award.
- Jinwoo received the Kwon. Youngse scholarship.
- Hwanjin joined Kyungpook National University as an Assistant Professor in Sep. 2024.
- Jeonghyun successfully finished her M.S. defense in Jun. 2024.
- Jaecheol successfully finished his Ph.D. defense in May 2024.
- Junil has been appointed as a Tenured Associate Professor from Mar. 2024.
- Hyuckjin received the 2023 KAIST EE Best Research Achievement Award (Kim Choong-Ki Award).
- Junil has started serving IEEE OJCOMS Signal Processing for Communications as the Area Editor from Jan. 2024.
- Hyuckjin and Sung Hyuck successfully finished their Ph.D. defense in Dec. 2023.
- Junil elected as a new Y-KAST (the Young Korean Academy of Science and Technology) member.
- Minje received the Excellence Prize at the '23 15th ICT Academic Paper Competition.
- Dong-Hyun and Hyesang successfully finished their Ph.D. defenses in Nov. 2023.
- Seunggi received the Kwon. Youngse scholarship.
- Junil received the Spring 2023 Excellence in Lecture Award.
- Beomsoo received the Spring 2023 Excellence in Teaching Assistant Award.
- Gyoseung received NRF Research Subsidies for Ph.D. Candidates.
- Hongjae successfully finished his M.S. defense in Jun. 2023.
- Hyeongtaek successfully finished his Ph.D. defense in May 2023.
- Hwanjin has been selected for the 2023 NRF Post-Doctoral Overseas Training (with Prof. David J. Love at Purdue) in May 2023.
- Yongjun received the 2022 Fall KAIST CoE Leadership Award in Apr. 2023.
- Junil has been selected as a 2023-2025 Distinguished Lecturer by the IEEE Vehicular Technology Society
- Hwanjin received the 2022 KAIST EE Best Ph.D. Dissertation Award in Apr. 2023.
- Beomsoo, Gyoseung, and Namhyun successfully finished their M.S. defenses in Dec. 2022.
- Sucheol successfully finished his Ph.D. defense in Dec. 2022.
- Hyesang and Beomsoo received the Excellence Prize at the '22 14th ICT Academic Paper Competition.
- Junil received the 2021 IEEE ComSoc CTTC Early Achievement Award in the 2022 IEEE Communication Theory Workshop (CTW)
- Junil received the 2022 IEEE Vehicular Technology Society Best Vehicular Electronics Paper Award.
- Miyeon participated in the 2022 Qualcomm IT Tour visiting HQ in San Diego in Aug. 2022.
- Junil has started serving IEEE Transactions on Wireless Communications as an Associate Editor from Aug. 2022.
- Junil has started serving IEEE Transactions on Communications as an Associate Editor from Aug. 2022.
- In-soo, Hwanjin and Taegyun successfully finished their Ph.D. defenses in Jun. 2022.
- Hwanjin received the 2022 KAIST Global Leadership Award (Creativity).
- Sunghyuck received the 13th ICT Excellence Award.
- Hwanjin received the Silver Prize at the IEEE Seoul Section Student Paper Contest 2021.
- In-soo and Minje received the IITP Presidential Award at the ICT Colloquium 2021 Creative Capstone Project.
- Sucheol, Hyeongtaek and Jihoon received the best paper award at the KICS Fall Conference 2021.
- Junil received the 2021 IEEE Vehicular Technology Society Neal Shepherd Memorial Best Propagation Award.

## 연락과 위치

- 연구실: [34141] 대전광역시 유성구 대학로 291 한국과학기술원(KAIST) IT 융합빌딩[^home]
- 교수 사무실: IT융합빌딩(N1) 716호[^eeprof][^sselab]
- 연구실 전화: +82-42-350-7560[^home]
- 교수 전화와 이메일: 042-350-7460, junil@kaist.ac.kr[^sse][^prof]
[^home]: 연구실 누리집 첫 화면 <https://www.icl.kaist.ac.kr/> (연구실 소개, Research Areas, Recent News, 주소·전화, 2026-10-22 열람)
[^prof]: Professor 페이지 <https://www.icl.kaist.ac.kr/people/professor> (Bio., Work Experiences, NEWS until 2017, 2026-10-22 열람)
[^students]: Postdocs & Students 페이지 <https://www.icl.kaist.ac.kr/people/postdocs-students> (2026-10-22 열람)
[^alumni]: Alumni 페이지 <https://www.icl.kaist.ac.kr/people/alumni> (Ph.D. Alumni, M.S. Alumni, 2026-10-22 열람)
[^visitors]: Visitors 페이지 <https://www.icl.kaist.ac.kr/people/visitors> (2026-10-22 열람)
[^areas]: Research Areas 페이지 <https://www.icl.kaist.ac.kr/research/research-areas> (2026-10-22 열람)
[^ris]: Research Areas · Reconfigurable Intelligent Surface 페이지 <https://www.icl.kaist.ac.kr/research/research-areas/reconfigurable-intelligent-surface> (2026-10-22 열람)
[^ntn]: Research Areas · Non-Terrestrial Networks 페이지 <https://www.icl.kaist.ac.kr/research/research-areas/non-terrestrial-networks> (2026-10-22 열람)
[^aiml]: Research Areas · AI/ML-based Communications 페이지 <https://www.icl.kaist.ac.kr/research/research-areas/aiml-based-communications> (2026-10-22 열람)
[^vlc]: Research Areas · Visible Light Communications 페이지 <https://www.icl.kaist.ac.kr/research/research-areas/visible-light-communications> (2026-10-22 열람)
[^thz]: Research Areas · THz & mmWave Communications 페이지 <https://www.icl.kaist.ac.kr/research/research-areas/thz-mmwave-communications> (2026-10-22 열람)
[^other]: Research Areas · Other Topics 페이지 <https://www.icl.kaist.ac.kr/research/research-areas/other-topics> (Multiple access, UAV, ISAC, 2026-10-22 열람)
[^projects]: Projects 페이지 <https://www.icl.kaist.ac.kr/research/projects> (Ongoing Projects, Finished Projects, 2026-10-22 열람)
[^withray]: WiThRay 페이지 <https://www.icl.kaist.ac.kr/research/withray> (2026-10-22 열람)
[^journals]: Journal Papers 페이지 <https://www.icl.kaist.ac.kr/publications/journal-papers> (2026-10-22 열람)
[^confs]: Conference Papers 페이지 <https://www.icl.kaist.ac.kr/publications/conference-papers> (2026-10-22 열람)
[^patents]: Patents 페이지 <https://www.icl.kaist.ac.kr/publications/patents> (2026-10-22 열람)
[^eeprof]: KAIST 전기및전자공학부 교수 상세 소개(최준일) <https://ee.kaist.ac.kr/professor/16714/> (2026-10-22 열람)
[^sse]: KAIST 반도체시스템공학과 교수 목록 <https://sse.kaist.ac.kr/professor/> (2026-10-22 열람)
[^sselab]: KAIST 반도체시스템공학과 연구실 목록 <https://sse.kaist.ac.kr/research-laboratory/> (2026-10-22 열람)
[^p1]: I.-S. Kim 외, J. Choi, IEEE Transactions on Wireless Communications 22, 9732-9745 (2023). <https://doi.org/10.1109/twc.2023.3273284> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J. Cha, J. Choi, IEEE Transactions on Wireless Communications 25, 10635-10651 (2026). <https://doi.org/10.1109/twc.2026.3653805> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: M. Lee 외, J. Choi, IEEE Transactions on Communications 73, 12174-12188 (2025). <https://doi.org/10.1109/tcomm.2025.3562517> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: D.-H. Jung, J.-G. Ryu, J. Choi, IEEE Transactions on Information Forensics and Security 17, 2784-2799 (2022). <https://doi.org/10.1109/tifs.2022.3188150> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: H. Kim, J. Choi, D. J. Love, IEEE Transactions on Wireless Communications 22, 9278-9290 (2023). <https://doi.org/10.1109/twc.2023.3269643> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: Y. Kim, J. Park, M. Bennis, J. Choi, IEEE Journal on Selected Areas in Communications 44, 2701-2717 (2026). <https://doi.org/10.1109/jsac.2025.3644282> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: G. Han 외, J. Choi, IEEE Transactions on Communications 73, 14653-14667 (2025). <https://doi.org/10.1109/tcomm.2025.3591158> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: H. Cho, B. Ko, B. Clerckx, J. Choi, IEEE Transactions on Wireless Communications 22, 9821-9834 (2023). <https://doi.org/10.1109/twc.2023.3273720> 초록 기준(Semantic Scholar 등록 초록).

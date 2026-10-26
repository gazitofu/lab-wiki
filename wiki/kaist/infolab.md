# 정보 및 통신 연구실 (InfoLab)

**KAIST 전기및전자공학부 · 이시현 교수**

- 분야: 정보 이론, 무선 통신, 보안 통신, 기계학습
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 무선·이동통신[^research][^p1][^p3], 네트워크 보안·프라이버시[^research][^p4], 통계적 추론·검정[^research][^p6], 생성 인공지능[^research][^p8], 양자 정보·얽힘[^p6], 엣지 컴퓨팅·엣지 AI[^research], 연합학습·분산 학습[^p7], 드론·무인 항공기[^p3]
- 홈페이지: <https://sites.google.com/view/kaist-infolab>
- 근거와 출처: [정보 및 통신 연구실 근거 페이지](infolab-sources.md)

> 차세대 무선 통신과 데이터 처리 시스템의 근본 한계와 효율적인 알고리즘을 연구하는 연구실이다. 통신과 센싱을 합친 무선 시스템, 전파를 조절하는 지능형 표면, 위성·무인 항공기 통신, 도청과 방해 전파에 맞서는 보안 통신을 한 갈래로, 개인 데이터를 지키는 통계 추론, 연합학습, 생성 모델 응용을 다른 갈래로 연구한다.[^home][^research]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 이시현 교수가 이끄는 연구실이다.[^home][^ee] 누리집 첫 화면은 통신, 통계적 추론(관측한 자료로 그 뒤의 알 수 없는 값이나 가설을 판단하는 방법), 기계학습 분야에서 기초 이론 연구와 실제 시스템의 설계·최적화를 함께 한다고 소개한다.[^home] 연구 페이지는 연구의 초점을 차세대 통신·정보 시스템의 이론적 토대와 실제 설계에 두고, 특히 무선 네트워크, 정보 처리, 데이터 기반 시스템의 근본 한계와 효율적인 알고리즘을 연구한다고 적는다.[^research] 전기및전자공학부 교수 소개는 주요 연구를 정보 이론(정보를 얼마나 줄여 담고 전달할 수 있는지 그 한계를 수학으로 다루는 이론), 무선 통신, 보안 통신, 기계학습으로 적고,[^ee] 반도체시스템공학과 연구실 목록도 이 연구실의 분야를 정보 이론, 무선 통신, 기계학습으로 적는다.[^sselab]

연구 페이지는 연구를 두 갈래로 나눈다. 첫 갈래 「차세대 통신」은 앞으로의 무선 네트워크가 단순한 데이터 전달을 넘어 통신·센싱·계산을 한데 묶고 전 지구적 연결을 주는 지능형 플랫폼으로 바뀌어 간다고 보고, 그런 시스템을 가능하게 할 기본 원리와 시스템 설계를 연구한다. 최근 주제로 통합 센싱·통신(ISAC), 재구성 지능형 표면(RIS), 비지상 네트워크(NTN), 엣지 컴퓨팅, 물리계층 보안(PLS)을 든다.[^research] 둘째 갈래 「통계적 추론과 기계학습」은 크고 복잡한 데이터에서 의미 있는 정보를 뽑아내는 문제를 다루며, 데이터를 안전하고 효율적이며 믿을 수 있게 처리하는 추론·학습 방법을 연구한다. 최근 주제로 차분 프라이버시(DP), 생성 모델, 연합학습, 의미 통신(원래 데이터 전체 대신 과제에 필요한 정보만 골라 보내는 학습 기반 통신 방식)을 든다.[^research]

대표 논문으로 보면, 첫 갈래에는 셀 프리 다중 안테나 시스템에서 센싱과 통신을 시간으로 나누는 ISAC(대표 논문 1), 여러 겹으로 쌓은 메타표면으로 전파가 지나는 동안 신호를 가공하는 RIS 연구(대표 논문 2), 셀룰러 망에 연결된 무인 항공기의 경로 계획(대표 논문 3), 무선 애드혹 네트워크에서 방해 전파를 쏘는 재머와 사용자 사이의 게임(대표 논문 4)이 있다.[^p1][^p2][^p3][^p4] 둘째 갈래에는 국소 차분 프라이버시 아래에서 분포를 추정하는 정확한 최적 방식(대표 논문 5), 양자 장치로 프라이버시를 지키는 가설 검정(대표 논문 6), 연합학습에서 여러 기기의 예측을 모으는 가중치 방법(대표 논문 7), 확산 모델로 이미지 속에 정보를 숨기는 방법(대표 논문 8)이 있다.[^p5][^p6][^p7][^p8]

누리집 논문 목록에는 연구 페이지가 따로 설명하지 않는 [Quantum] 표시 논문도 있다. 송신기 사이의 양자 협력으로 합 용량을 높이는 연구(IEEE JSAC 2026), 다중 접속 채널의 네트워크 부호화에서 비국소·양자 이점을 다룬 연구(Physical Review A 2026), 분산 압축에서 비국소 협력의 이점이 없음을 보인 연구(ITW 2024)이며, 앞의 두 편은 대표 논문 6과 함께 J. Bae가 공저자다. 베이즈 통계 결정 문제의 최적 후회(가장 좋은 결정과 비교해 생기는 손실의 차이) 지수를 다룬 통계적 결정 이론 논문(IEEE Signal Processing Letters 2026)도 있다.[^pubs]

## 주요 연구 주제

### 1. 통합 센싱·통신(ISAC)

무선 통신과 주변 환경 센싱을 한 시스템 안에 합쳐, 정보를 보내면서 동시에 주변을 감지하는 네트워크를 만드는 방식이다.[^research] 셀 프리 다중 안테나 시스템에서 센싱 단계와 통신 단계를 시간으로 나누는 근거리장 ISAC의 강건 빔포밍과 시간 배분(대표 논문 1), 같은 틀에서 위치 정보로 채널을 구성하는 학회 논문(WiOpt 2026)이 있다.[^p1][^pubs] 대표 논문 1.

### 2. 재구성 지능형 표면과 다중 안테나 전송

RIS는 프로그래밍할 수 있는 전자기 표면으로 무선 전파 환경을 바꿔, 적은 에너지로 서비스 범위를 넓히고 신뢰도를 높이는 기술이다.[^research] 소자끼리 연결한 RIS 층을 여러 겹 쌓은 메타표면으로 다중 사용자 MIMO의 프리코딩을 전파 영역에서 하는 연구(대표 논문 2), 전파를 반사하면서 동시에 투과시키는 RIS(STAR-RIS)를 여러 기지국이 함께 신호를 보내는 협력 전송(JP-CoMP)에 쓰는 효과 분석(IEEE WCL 2026), 전송률 분할 다중 접속(RSMA)으로 XR 데이터를 에너지 효율적으로 보내는 연구(IEEE WCL 2025)가 있다.[^p2][^pubs] 대표 논문 2.

### 3. 비지상 네트워크와 엣지 컴퓨팅

비지상 네트워크는 위성, 고고도 플랫폼, 공중 노드를 써서 지상 기반 시설 너머로 연결을 넓히는 우주·공중·지상 통합 통신 시스템이고, 엣지 컴퓨팅은 계산과 지능을 네트워크 가장자리에 두어 지연이 짧은 서비스와 데이터가 많은 AI 응용을 돕는 분산 계산 틀이다.[^research] 셀룰러 망에 연결된 무인 항공기가 기지국 연결과 배터리 제약을 지키며 화물을 나르는 최적 경로(대표 논문 3), 같은 무인 항공기의 경로와 핸드오버 전략을 함께 최적화한 연구(IEEE Access 2025), 도청자에 맞서 무인 항공기를 다시 배치하는 경로·전력 최적화(IEEE Communications Letters 2024), 촘촘한 저궤도 위성 엣지 컴퓨팅에서 예측에 기반한 작업 오프로딩(IEEE TMC 2026)이 있다.[^p3][^pubs] 대표 논문 3.

### 4. 물리계층 보안과 은밀 통신

물리계층 보안은 통신의 물리 계층에서 기밀성을 보장해 도청과 악의적인 간섭을 막는 기법이다.[^research] 여러 주파수 대역을 쓰는 무선 애드혹 네트워크에서 사용자와 재머 사이의 재밍 방지 게임(대표 논문 4), 알려진 재밍 공격의 분류와 처음 보는 공격의 검출을 함께 하는 재밍 검출 알고리즘(IEEE Communications Letters 2023)이 있다.[^p4][^pubs] 통신한다는 사실 자체를 감시자가 알아채지 못하게 하는 은밀 통신 연구도 이어 왔다. 여러 사용자의 협력과 채널 상관이 은밀 통신에 주는 영향(IEEE TIFS 2023·2024, ICC 2024), 피드백이 있는 가우스 다중 접속 채널의 은밀 통신(IEEE WCL 2022), 이동성을 이용한 은밀 통신과 간섭 채널의 은밀 통신(IEEE TIFS 2021)이 논문 목록에 있다.[^pubs] 수신기의 아날로그-디지털 변환기(ADC)가 유한 해상도인 가우스 도청 채널의 비밀 용량을 다룬 연구(IEEE Transactions on Information Theory 2022)도 있다.[^pubs] 대표 논문 4.

### 5. 국소 차분 프라이버시와 분포 추정

차분 프라이버시는 개인 데이터의 프라이버시를 엄밀히 지키면서 통계 분석과 기계학습을 할 수 있게 하는 수학적 틀과 알고리즘이다.[^research] 공유 난수를 쓸 때 낮은 통신 비용으로 정확히 최적인 프라이버시-효용 득실을 이루는 분포 추정 방식(대표 논문 5), 국소 차분 프라이버시 아래 표본 추출의 최소최대 최적 방식(NeurIPS 2024), 1비트 통신으로 하는 프라이버시 보호 이산 분포 추정(IEEE TIFS 2024), 블록 설계에 기반한 통신 효율적인 프라이버시 보호 추정(IEEE JSAIT 2024), 효용을 최적화한 국소 차분 프라이버시 아래 분포 추정의 근본 한계(IEEE TIFS 2026)가 있다.[^p5][^pubs] 대표 논문 5.

### 6. 양자 자원을 쓰는 추론과 통신

고전 데이터 표본을 프라이버시 보호 장치로 가린 상태에서 가설을 검정할 때, 양자 프라이버시 장치가 고전 장치보다 나은 프라이버시-효용 득실을 내는 경우를 보인 연구(대표 논문 6)와 프라이버시를 지키는 여러 가설 검정에서 양자 이점을 다룬 연구(ISIT 2025)가 있다.[^p6][^pubs] 송신기 사이 양자·비신호 협력으로 합 용량을 높이는 연구(IEEE JSAC 2026), 다중 접속 채널의 네트워크 부호화에서 비국소·양자 이점(Physical Review A 2026), 분산 압축에서 비국소 협력의 이점이 없음을 보인 연구(ITW 2024)도 같은 갈래다.[^pubs] 대표 논문 6.

### 7. 연합학습

연합학습은 여러 기기나 기관이 원래 데이터를 나누지 않고 함께 기계학습 모델을 학습하는 분산 학습 기법이다.[^research] 기기마다 데이터가 다를 때 서버가 여러 기기의 예측에 가중치를 주어 가짜 레이블을 만드는 방법(대표 논문 7), 서버의 레이블 없는 데이터를 이용해 기기의 데이터 부족을 극복하는 방법(IEEE Access 2024), 낸드 플래시 메모리의 신뢰성을 예측하는 연합학습 알고리즘(IEEE OJIES 2026)이 있다.[^p7][^pubs] 대표 논문 7.

### 8. 생성 모델 응용

연구 페이지는 데이터 생성과 표현을 위한 학습 기반 모델을 연구하며, 특히 효과적인 잡음 설계, 인과 추론, 정보 숨기기 같은 응용에 관심을 둔다고 적는다.[^research] 학습 없이 확산 모델로 여러 이미지를 숨기고 사용자마다 접근을 제어하는 이미지 스테가노그래피(대표 논문 8), 확산 모델의 샘플링을 효율적으로 하는 저주파 고유 잡음 형성 방법 LENS(arXiv 사전 공개본, 누리집 학회 표기 NeurIPS 2026)가 있다.[^p8][^pubs] 대표 논문 8.

## 대표 논문

최근 5년 논문 가운데 이시현 교수가 저자인 것에서 연구 갈래마다 고르게 골랐다. 8편 가운데 7편은 교수가 마지막 저자이고, 대표 논문 6은 교수가 4명 가운데 셋째 저자다(마지막 저자 J. Bae). 누리집 목록은 교신저자를 따로 표시하지 않는다.[^pubs] "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [Robust Beamforming and Time Allocation for Time-Division Cell-Free Near-Field ISAC](https://doi.org/10.1109/twc.2026.3730662) · IEEE Transactions on Wireless Communications | 셀 프리 다중 안테나(MIMO) 시스템에서 센싱과 내려받기 통신을 시간으로 나누는 근거리장 통합 센싱·통신(ISAC) 틀을 제안했다. 센싱 단계에서 사용자 위치를 추정해 위치를 반영한 채널을 만들고, 뒤따르는 통신 단계에서 이 채널을 쓴다. 센싱에서 생긴 위치 오차와 채널 추정 오차가 얽히는 관계를 모델로 나타내, 센싱 정확도와 통신 스펙트럼 효율(SE, 주어진 주파수 폭으로 보내는 데이터 양) 사이의 득실을 따졌다. 이 모델로 시간 배분 비율, 센싱 신호의 공분산 행렬, 채널 정보가 불완전해도 견디는 내려받기 빔포밍을 함께 최적화했고, 볼록하지 않은 이 문제를 반정부호 계획법(SDP) 기반으로 바꿔 번갈아 최적화하는 틀에서 풀었다. 계산량을 줄인 준최적 설계 두 가지(전력 배분 방식, 오차를 무시하는 방식)도 제안했다. 모의실험에서 제안 방식은 원거리장 구성과 한 기지국이 송수신을 함께 하는 센싱 구성보다 위치 추정 정확도를 크게 높여 채널 추정 오차를 줄이고 결국 SE를 높였다. 전력 배분 방식은 빔포밍 손실이 조금 있지만 시간 배분 비율을 바꿔 넓은 범위의 센싱 요구에서 견고했고, 오차를 무시하는 방식은 센싱 요구가 엄격할 때 잘 동작했다.[^p1] | 1저자 C. Son, 2명 중 마지막 저자 이시현 |
| 2 | 2026 | [Wave-Domain Precoding for MU-MIMO Systems via Beyond-Diagonal Stacked Intelligent Metasurfaces](https://doi.org/10.1109/lwc.2026.3714502) · IEEE Wireless Communications Letters | 여러 사용자에게 동시에 내려보내는 다중 사용자 MIMO에서, 여러 겹으로 쌓은 지능형 메타표면(SIM)으로 전파 영역 프리코딩을 하는 방법을 연구했다. 소자끼리 연결한 RIS(BD-RIS) 층을 쌓은 BD-SIM은 필요한 층 수를 줄이고, SIM에서 층을 지날 때마다 쌓이는 감쇠를 덜어 준다. 정규화 제로포싱(RZF, 사용자 사이 간섭을 줄이도록 신호를 미리 가공하는 방식) 프리코딩을 구현하려고 근사 정확도와 실효 채널 이득을 각각 강조하는 두 설계를 두고, 서로 얽힌 볼록하지 않은 문제를 층마다 번갈아 최적화해 풀었다(Takagi 분해와 다양체 위의 경사 하강법 사용). 수치 결과에서 BD-SIM은 SIM과 BD-RIS 기준 방식보다 성능이 좋았다. 간섭이 성능을 제한하는 영역에서는 근사 정확도가, 잡음이 제한하는 영역에서는 실효 채널 이득이 더 중요했다.[^p2] | 1저자 Y. Kim(누리집은 Y. Kim·C. Son 공동 기여로 표시), 3명 중 마지막 저자 이시현 |
| 3 | 2025 | [Trajectory Optimization for Cellular-Enabled UAV With Connectivity and Battery Constraints](https://doi.org/10.1109/tvt.2025.3579005) · IEEE Transactions on Vehicular Technology | 셀룰러 망에 연결된 무인 항공기(UAV)의 경로 계획을 기지국 연결과 배터리 제약을 함께 두고 다뤘다. UAV는 화물을 출발점에서 도착점까지 빨리 나르되 기지국과 계속 연결돼 있어야 하고 배터리 한도를 지켜야 하며, 충전소에서 다 쓴 배터리를 완충된 배터리로 바꿀 수 있다. 연구진은 이 문제를 동등한 두 단계 그래프 최단 경로 탐색 문제로 바꿔, 다항 시간(입력이 커질 때 계산량이 입력 크기의 다항식으로 늘어나는 시간) 안에 최적 경로를 내는 알고리즘을 제안했다. 기존 여러 알고리즘과 성능·계산 복잡도를 비교해, 다항 시간 안에 최적 경로를 내는 것은 이 알고리즘뿐임을 보였다. 에너지 소비를 줄이거나 실을 수 있는 화물 무게를 늘리는 다른 목표에 대해서도 다항 시간 안에 최적 경로를 내는 알고리즘을 제안했다.[^p3] | 1저자 H.-S. Im, 3명 중 마지막 저자 이시현 |
| 4 | 2023 | [Anti-Jamming Games in Multi-Band Wireless Ad Hoc Networks](https://doi.org/10.1109/tifs.2022.3227422) · IEEE Transactions on Information Forensics and Security | 여러 주파수 대역을 쓰는 무선 애드혹 네트워크에서 여러 사용자와 방해 전파를 쏘는 재머 사이의 재밍 방지 게임을 연구했다. 사용자는 통신 속도, 주파수를 옮기는 비용, 재밍으로 잃는 손실을 따진 기대 보상을 높이려 하고 재머는 이를 낮추려 한다. 양쪽이 번갈아 전략을 바꾸는 군비 경쟁을 분석해, 각 단계의 최적 주파수 도약 정책을 마르코프 결정 과정(MDP, 현재 상태만 보고 다음 행동을 고르는 순차 결정 모형)으로 구했다. 군비 경쟁이 몇 차례 뒤에 평형에 이른다는 것을 해석적으로 보이고, 평형에서의 주파수 도약 정책과 재밍 전략을 밝혔다. 한 주파수 대역에서 한 사용자만 통신하게 하는 충돌 회피 프로토콜 두 가지를 제안했고, 보상 변수와 충돌 회피 프로토콜이 평형의 최적 정책과 기대 보상에 주는 영향을 수치로 보였다. 재머가 예측하기 어려운 재밍 전략을 쓰는 경우의 평형도 논의했다.[^p4] | 1저자 H.-S. Im, 2명 중 마지막 저자 이시현 |
| 5 | 2024 | [Achieving the Exactly Optimal Privacy-Utility Trade-Off With Low Communication Cost via Shared Randomness](https://doi.org/10.1109/tit.2024.3448475) · IEEE Transactions on Information Theory | 공유 난수(데이터를 보내는 쪽과 받는 쪽이 함께 갖는 무작위 값)가 있을 때, 국소 차분 프라이버시(LDP) 조건에서 이산 분포를 추정하는 문제를 다뤘다. 통신 비용이 입력 데이터 크기 이하이면서 프라이버시와 효용 사이의 득실(PUT)을 정확히 최적으로 이루는 새 LDP 방식들을 제안했다. 따름정리로, 입력 데이터 크기가 짝수이면 프라이버시 보호가 강한 영역에서 1비트 통신만으로 정확히 최적인 PUT를 이룰 수 있음을 보였다. 핵심은 Park 등(2023)의 블록 설계 방식을 분해(resolution)라는 조합론 개념으로 쪼개는 것이다. 이렇게 만든 분해는 통신 비용이 원래 방식 이하이고, 원래 방식이 정확히 최적이면 분해도 정확히 최적이다. Ye와 Barg(2018)가 제안한 정확히 최적인 부분집합 선택 방식에 대해 Baranyai 분해와 순환 이동 분해 두 가지를 제시했다. Baranyai 분해는 정확히 최적인 블록 설계 분해들 가운데 최소 통신 비용을 이루지만 일반적으로 구체적인 구조를 모르고, 순환 이동 분해는 구조가 구체적이지만 통신 비용이 더 클 수 있다. 이를 보완해, 일부 입력 크기와 프라이버시 예산에서 최소 통신 비용과 구체적 구조를 함께 갖는 다른 블록 설계 방식의 분해도 제안했다.[^p5] | 1저자 S.-H. Nam, 3명 중 마지막 저자 이시현 |
| 6 | 2026 | [Quantum Advantage in Locally Differentially Private Hypothesis Testing](https://doi.org/10.1109/jsac.2026.3709807) · IEEE Journal on Selected Areas in Communications | 고전 데이터 표본으로 가설을 검정하되 프라이버시를 지켜야 하는 상황을 대칭·비대칭 검정 모두에서 다뤘다. 효용은 오류 지수(표본이 늘 때 오류 확률이 줄어드는 속도), 곧 체르노프 정보와 상대 엔트로피로 쟀고, 프라이버시는 고전 또는 양자 국소 차분 프라이버시로 쟀다. 이 상황에서 일부 경우에 최적 프라이버시-효용 득실(PUT)에 양자 이점이 있음을 보였다. 가설로는 매끄럽게 만든 점 질량 분포와 균등 분포를 두고, 고전 프라이버시 장치가 이룰 수 있는 최적 PUT의 상한을 구했으며 특정 경우에는 이 상한이 실제 최적값과 같다. 양자 이점을 보이려고 이 상한보다 나은 PUT를 이루는 양자 프라이버시 장치를 제안했고, 프라이버시 제약이 엄격하고 이산 데이터의 값 종류가 3–9개로 작을 때 대칭·비대칭 검정 모두에서 상한보다 나은 결과를 냈다. 제안 장치는 대칭 정보 완비(SIC) 양자 상태를 준비하는 고전-양자 채널 뒤에 탈분극 채널을 이은 구조다.[^p6] | 1저자 S.-H. Nam, 4명 중 셋째 저자 이시현, 마지막 저자 J. Bae |
| 7 | 2025 | [Provably Near-Optimal Federated Ensemble Distillation with Negligible Overhead](https://icml.cc/virtual/2025/poster/46350) · ICML 2025 | 연합 앙상블 증류는 각 기기(클라이언트)의 예측을 모아 서버의 레이블 없는 데이터에 가짜 레이블을 붙이고 그 데이터로 서버 모델을 학습해, 기기마다 데이터가 다른 문제에 대응한다. 서버 데이터는 미리 있을 수도 있고 데이터 없이 만들어 낼 수도 있다. 이 방식의 효과는 가짜 레이블을 만들 때 기기 예측에 가중치를 어떻게 주느냐에 크게 달려 있고, 기기 사이 차이가 클 때 특히 그렇다. 연구진은 생성적 적대 신경망(GAN)의 이론 결과에서 착안해, 서버가 나눠 준 생성기와 각 기기의 데이터로 학습한 기기별 판별기를 이용하는 가중치 방법을 제안하고 거의 최적임을 증명했다. 여러 이미지 분류 실험에서 기준 방법보다 성능이 크게 좋았고, 이 방법이 더하는 통신 비용, 기기 쪽 프라이버시 유출, 기기 쪽 계산 부담은 서버 데이터가 미리 있든 없든 무시할 만한 수준이었다.[^p7] | 1저자 W.-J. Jang, 3명 중 마지막 저자 이시현 |
| 8 | 2026 | [Training-Free Coverless Multi-Image Steganography with Access Control](https://icml.cc/virtual/2026/poster/65970) · ICML 2026 | 커버리스 이미지 스테가노그래피(CIS)는 덮개 이미지를 직접 고치지 않고 정보를 숨겨 들키기 어렵고 숨김 탐지 분석에도 강하지만, 기존 방법 대부분은 권한이 있는 사용자마다 다른 숨긴 내용을 골라 보여 주는 접근 제어가 부족하다. 이런 접근 제어는 여러 사용자가 있는 환경에서 정보 숨기기를 확장하고 프라이버시를 지키는 데 중요하다. 연구진은 추가 학습 없이 확산 모델을 쓰는 CIS 틀 MIDAS를 제안했다. MIDAS는 잠재 공간(모델이 이미지를 압축해 나타내는 내부 표현 공간)에서 이미지를 합쳐 여러 이미지를 숨기고 사용자별로 접근을 제어한다. 남은 구조 정보를 억누르는 무작위 기저 장치와 정보 유출의 이론 분석, 합친 잠재 벡터를 확산 과정에 더 잘 맞게 바꾸는 잠재 벡터 융합 모듈을 넣었다. 실험에서 MIDAS는 기존의 학습 없는 CIS 기준 방법보다 접근 제어 기능, 숨긴 이미지의 품질과 다양성, 잡음에 대한 견고성, 숨김 탐지 분석에 대한 저항에서 꾸준히 앞섰다.[^p8] | 1저자 M. Bae, 2명 중 마지막 저자 이시현 |

## 교수와 전문 분야

이시현 교수(Si-Hyeon Lee)는 KAIST 전기및전자공학부 부교수(Associate Professor)다.[^prof][^ee] 전기및전자공학부 교수 소개는 디비전을 Communication과 Computer로, 주요 연구분야를 AI & Machine Learning, Information, Communication & Coding, Security, Quantum Science & Engineering으로, 주요 연구를 Information Theory, Wireless Communications, Secure Communications, Machine Learning으로 적고,[^ee] 교수 목록은 겸임학과를 AI시스템학과로 적는다.[^eelist] 반도체시스템공학과 교수 명단에도 같은 연구 분야로 올라 있다.[^sse]

교수는 KAIST 전기공학 학사(2007, summa cum laude)와 박사(2013) 학위를 받았다. 2014년부터 2016년까지 캐나다 University of Toronto 전기·컴퓨터공학과(Department of Electrical and Computer Engineering)에서 박사후연구원(Postdoctoral Fellow)으로 일했고, KAIST 전기및전자공학부에 오기 전에는 POSTECH 전기공학과(Department of Electrical Engineering) 조교수였다.[^prof][^team]

누리집 Professor 페이지는 수상과 영예로 KAIST 전기및전자공학부 Outstanding Lecture Award(2026), IEEE 정보이론학회(Information Theory Society) Distinguished Lecturer(2024–25), KAIST Technical Innovation Award(2022), IEEE Senior Member(2021), KAIST Research Highlights(2021)를 적는다.[^prof] 편집 활동으로 IEEE Transactions on Information Theory 부편집장(Associate Editor, 2025년 3월부터), IEEE Transactions on Communications 부편집장(2025년 12월부터), IEEE Journal of Selected Areas in Communications 특집호(미래 지능형 무선 네트워크의 보안 통신·센싱·계산) 객원 편집자(Guest Editor)를 맡았다. 학회 활동으로 IEEE ITW 2024의 TPC(프로그램 위원회) 위원장, WiOpt 2026 ISAC 워크숍 위원장, IEEE ICC 2027 여행 지원금 위원장(Travel Grant Chair), IEEE ISIT 2028과 IEEE ITW 2030의 튜토리얼 위원장을 적는다.[^prof]

초청 강연으로는 IEEE ISIT 2025(미국 Ann Arbor) 튜토리얼 「A Unified Framework for Network Information Theory」, 2025년 Croucher Summer Course in Information Theory(홍콩)에서 차분 프라이버시를 쓰는 프라이버시 보호 통계 추론과 기계학습 강의, 2025년 Women in Information and Coding Theory Workshop(스웨덴 Linköping) 기조연설, 2024년 IEEE European School of Information Theory(네덜란드 Eindhoven) 초청 세미나를 적는다.[^prof] 강의로는 Information and Coding Theory, Signals and Systems, Introduction to Information Theory and Coding, Probability and Introductory Random Processes, Engineering Random Processes가 있다.[^prof]

논문으로 보면 전문 분야는 정보 이론을 바탕으로 한 두 갈래다. 하나는 ISAC, RIS, 비지상 네트워크, 물리계층 보안과 은밀 통신 같은 무선 통신 시스템의 설계와 근본 한계이고(대표 논문 1–4), 다른 하나는 국소 차분 프라이버시 아래의 분포 추정과 가설 검정, 연합학습, 생성 모델 응용 같은 통계적 추론과 기계학습이다(대표 논문 5–8).[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8] 2019년까지의 논문에는 무선 애드혹 네트워크의 용량 스케일링, 중계 채널과 다이아몬드 도청 채널, 스트리밍 데이터 전송의 점근 성능, 스마트 미터의 정보 이론적 프라이버시, 은밀 통신 같은 네트워크 정보 이론 주제가 있다.[^pubs]

## 응용 분야

대표 논문과 논문 목록이 든 쓰임은 다음과 같다. 대표 논문 1은 셀 프리 다중 안테나 시스템에서 사용자 위치 추정과 내려받기 통신을, 대표 논문 3은 기지국 연결과 배터리 교체 조건에서 화물을 나르는 무인 항공기를 다룬다.[^p1][^p3] 대표 논문 8은 여러 사용자가 있는 환경에서 사용자마다 볼 수 있는 숨긴 이미지를 달리하는 정보 숨기기를 다룬다.[^p8] 논문 목록에는 낸드 플래시 메모리의 신뢰성 예측에 연합학습을 쓴 연구(IEEE OJIES 2026), 발바닥 압력 센서 깔창 자료로 파킨슨병 환자의 보행 동결을 검출하는 시간 합성곱 신경망 연구(Frontiers in Aging Neuroscience 2024), 확장현실(XR) 데이터 전송 연구(IEEE WCL 2025)도 있다.[^pubs]

## 구성원

2026년 10월 23일 연구실 누리집 Team 페이지 기준이다. Team 페이지 첫머리는 2026년 가을 학기 연구실 현황을 박사후연구원 1명, 대학원생 16명(박사 11명, 석사 5명)으로 적는다. 과정·시작 시점·이메일은 누리집 표기를 옮겼고, 석박사통합과정은 누리집의 「Joint MS&PhD course」다.[^team] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| HyunYoung Park (박현영) | 박사후연구원 | 2026. 3- | phy811@kaist.ac.kr | 5, 6 |
| Jaemin Park (박재민) | 박사과정 | 2021. 9- | jaemin.park@kaist.ac.kr |  |
| Wonjun Jang (장원준) | 박사과정 | 2023. 9- | wonjun_jang@kaist.ac.kr | 7 |
| Kyuyeong Kim (김규영) | 박사과정 (Student Representative) | 2024. 2- | kimyou283@kaist.ac.kr | 3 |
| Hyeonseo Park (박현서) | 석박사통합과정 (Joint MS&PhD course) | 2023. 2- | phseo2000@kaist.ac.kr | 7 |
| Jaein Lee (이재인) | 석박사통합과정 (Joint MS&PhD course) | 2023. 2- | wodls929@kaist.ac.kr |  |
| Jiho Jung (정지호) | 석박사통합과정 (Joint MS&PhD course) | 2023. 8- | mkll321@kaist.ac.kr |  |
| Jungsik Ahn (안정식) | 박사과정 | 2024. 9- | jungsik@kaist.ac.kr |  |
| Gwankyo Nam (남관교) | 박사과정 | 2025.2- | gwankyo@kaist.ac.kr |  |
| Minyeol Bae (배민열) | 석박사통합과정 (Joint MS&PhD course) | 2024. 2- | willy3690@kaist.ac.kr | 8 |
| Chaedam Son (손채담) | 박사과정 | 2026. 2- | scd5929@kaist.ac.kr | 1, 2 |
| Sun-Moon Yoon (윤선문) | 석박사통합과정 (Joint MS&PhD course) | 2025.2- | ysm4078@kaist.ac.kr |  |
| Haewon Jeon (전해원) | 석사과정 | 2025. 2- | haewon@kaist.ac.kr |  |
| Jonghyuk Hong (홍종혁) | 석사과정 | 2025. 2- | jonghyukm41@kaist.ac.kr |  |
| Hyeongsun Moon (문형선) | 석사과정 | 2025. 9- | hsmoon@kaist.ac.kr |  |
| Juho Lee (이주호) | 석사과정 | 2026.2- | juho8128@kaist.ac.kr |  |
| Heongjin Jo (조형진) | 석사과정 | 2026.2- | jhj2002good@kaist.ac.kr |  |

## 졸업생과 이전 구성원

누리집 Team 페이지 Alumni 칸의 48줄이다. 박사후연구원 1줄, 박사 4줄, 석사 14줄과 학부 개별연구(Individual study) 참여 29줄이다. 학위 연월·학위 논문 제목·진로는 누리집 표기이고, 학부 개별연구는 누리집이 적은 참여 학기다. 누리집은 학위를 받은 학교를 따로 적지 않는다. 같은 사람이 여러 줄에 나오며(Seung Hyun Nam은 석사·박사·박사후연구원 세 줄), Jaemin Park·Wonjun Jang·Kyuyeong Kim·Gwankyo Nam·Chaedam Son은 석사 학위 뒤, Hyun-Young Park은 박사 학위 뒤 이 연구실 구성원으로 위 표에도 있다. 학부 개별연구 참여자 가운데 박현서·정지호·윤선문·이주호·조형진도 위 구성원 표에 있다.[^team]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Seung Hyun Nam (남승현) | Postdoc (Aug. 2026) | Postdoc@University of Jyväskylä |  |
| Kang-Hee Cho (조강희) | PhD (Feb. 2024) | Samsung Research | Study on the fundamental limits of covert communication over multi-user networks |
| Seung Hyun Nam (남승현) | PhD (Aug. 2024) | Postdoc@InfoLab&QITLab | Research on the communication-efficient private distribution estimation |
| Hyeonseong Im (임현성) | PhD (Aug. 2024) | LIG Nex1 (LIG넥스원) | Research on anti-jamming strategies and cellular-enabled UAV trajectory optimization |
| Hyun-Young Park (박현영) | PhD (Feb. 2026) | Postdoc@InfoLab | Research on fundamental limits of privacy-preserving statistical inference and sampling |
| Seung Hyun Nam (남승현) | MS (Feb. 2020) | PhD@InfoLab |  |
| Kang-Hee Cho (조강희) | MS (Feb. 2020) | PhD@InfoLab |  |
| Hyeonseong Im (임현성) | MS (Aug. 2020) | PhD@InfoLab |  |
| Jisoo Park (박지수) | MS (Aug. 2020) | PhD@DGIST |  |
| Jaemin Park (박재민) | MS (Feb. 2021) | PhD@InfoLab |  |
| Seunghye Lee (이승혜) | MS (Feb. 2023) | Google Korea |  |
| Seokhwa Hong (홍석화) | MS (Feb. 2023) | ADD (국방과학연구소) |  |
| Wonjun Jang (장원준) | MS (Aug. 2023) | PhD@InfoLab |  |
| Kyuyeong Kim (김규영) | MS (Feb. 2024) | PhD@InfoLab |  |
| Jungwon Hur (허정원) | MS (Feb. 2024) | ADD (국방과학연구소) |  |
| Junyeong Kim (김준영) | MS (Feb. 2025) | ADD (국방과학연구소) |  |
| Gwankyo Nam (남관교) | MS (Feb. 2025) | PhD@InfoLab |  |
| Chaedam Son (손채담) | MS (Feb. 2026) | PhD@InfoLab |  |
| Yukyum Kim (김유겸) | MS (Feb. 2026) | KAI (한국항공우주산업) |  |
| 조민서 | Undergraduate, Individual study (Winter 2021) |  |  |
| 박현서 | Undergraduate, Individual study (Winter 2021, Spring 2022) |  |  |
| 이진 | Undergraduate, Individual study (Winter 2021, Spring 2022) |  |  |
| 조홍훈 | Undergraduate, Individual study (Winter 2021) |  |  |
| 서민성 | Undergraduate, Individual study (Winter 2022) |  |  |
| 이다영 | Undergraduate, Individual study (Winter 2022, Spring 2023) |  |  |
| 이준원 | Undergraduate, Individual study (Winter 2022) |  |  |
| 정지호 | Undergraduate, Individual study (Winter 2022, Spring 2023) |  |  |
| 황의현 | Undergraduate, Individual study (Winter 2022) |  |  |
| 이재헌 | Undergraduate, Individual study (Spring 2023) |  |  |
| 배민성 | Undergraduate, Individual study (Spring 2023) |  |  |
| 성지원 | Undergraduate, Individual study (Spring 2023) |  |  |
| 문정욱 | Undergraduate, Individual study (Summer 2023) |  |  |
| 윤선문 | Undergraduate, Individual study (Summer 2023-Summer 2024) |  |  |
| 이찬렬 | Undergraduate, Individual study (Summer 2023) |  |  |
| 원태연 | Undergraduate, Individual study (Summer 2023, Fall 2023) |  |  |
| 이주호 | Undergraduate, Individual study (Winter 2023, Summer-Fall 2025) |  |  |
| 조유민 | Undergraduate, Individual study (Winter 2023, Spring 2024) |  |  |
| 김동현 | Undergraduate, Individual study (Winter 2023) |  |  |
| 이수윤 | Undergraduate, Individual study (Winter 2023) |  |  |
| 고채현 | Undergraduate, Individual study (Summer 2024) |  |  |
| 이승연 | Undergraduate, Individual study (Summer 2024) |  |  |
| 변승의 | Undergraduate, Individual study (Winter 2024) |  |  |
| 이시준 | Undergraduate, Individual study (Winter 2024) |  |  |
| 조형진 | Undergraduate, Individual study (Fall 2025) |  |  |
| 김태연 | Undergraduate, Individual study (Winter 2025) |  |  |
| 노욱진 | Undergraduate, Individual study (Winter 2025) |  |  |
| 조용빈 | Undergraduate, Individual study (Spring 2026) |  |  |
| 윤태우 | Undergraduate, Individual study (Spring 2026) |  |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지 「Published/Accepted」 절의 2021–2026년 연도 구역 41편이다. 누리집이 J(학술지 또는 컴퓨터과학 주요 학회 논문)로 표시한 33편과 C(국제 학회 논문)로 표시한 8편이다. 저자·제목·학술지·학회 표기는 누리집 그대로이고, 줄 끝 대괄호는 누리집이 붙인 연구 주제 표시다. 누리집은 출판 논문과 게재 승인 논문을 「Published/Accepted」 한 절에 함께 적는다. 2026년의 NeurIPS 2026 논문 한 편은 누리집이 학회 논문집이 아닌 arXiv 사전 공개본으로 연결한 항목이라 「arXiv 사전 공개본」으로 표시했다.[^pubs]

**2026**

- H. Jeon and S.-H. Lee. "LENS: Low-frequency eigen noise shaping for efficient diffusion sampling". *Neural Information Processing Systems (NeurIPS) 2026. [Generative Model]* (arXiv 사전 공개본, 누리집 학회 표기: NeurIPS 2026).
- W.-J. Jang, J.-Y. Yoon, J.-M. Park, and S.-H. Lee. "Federated learning algorithm for predicting the reliability of NAND flash memory". *IEEE Open Journal of the Industrial Electronics Society (OJIES), 2026. [Federated Learning]*.
- C. Son and S.-H. Lee. "Robust beamforming and time allocation for time-division cell-free near-field ISAC". *IEEE Transactions on Wireless Communications (TWC), 2026. [ISAC]*.
- S.-H. Nam, H.-Y. Park, J. Yun, A. Rai, S.-H. Lee, and J. Bae. "Enhancing sum capacity via quantum and no-signaling cooperation between transmitters". *IEEE Journal of Selected Areas in Communications (JSAC), 2026. [Quantum]*.
- G. Nam and S.-H. Lee. "Prediction-based task offloading for ultra-dense LEO satellite edge computing". *IEEE Transactions on Mobile Computing (TMC), 2026. [Edge Computing, NTN]*.
- H.-Y. Park and S.-H. Lee. "Optimal regret exponents for Bayesian statistical decision problems". *IEEE Signal Processing Letters (SPL), July 2026. [Statistical Inference]*.
- Y. Kim, C. Son, and S.-H. Lee. "Wave-domain precoding for MU-MIMO systems via beyond-diagonal stacked intelligent metasurfaces". *IEEE Wireless Communications Letters (WCL), pp. 4155-4159, July 2026. [RIS] (Y. Kim and C. Son equally contributed to this work)*.
- S.-H. Nam, H.-Y. Park, S.-H. Lee, and J. Bae. "Quantum advantage in locally differentially private hypothesis testing". *IEEE Journal of Selected Areas in Communications (JSAC), pp. 5253-5266, July 2026. [Quantum, DP]*.
- S.-M. Yoon, H.-Y. Park, S.-H. Nam, and S.-H. Lee. "Fundamental limit of discrete distribution estimation under utility-optimized local differential privacy". *IEEE Transactions on Information Forensics and Security (TIFS), pp. 5312-5327, May 2026. [DP]*.
- J. Lee and S. -H. Lee. "Effectiveness of STAR-RIS-assisted JP-CoMP: Minimum-rate and sum-rate perspectives". *IEEE Wireless Communications Letters (WCL), pp. 3014-3018, May 2026. [RIS]*.
- M. Bae and S.-H. Lee. "Training-free coverless multi-image steganography with access control". *International Conference on Machine Learning (ICML) 2026, Seoul, South Korea, July 2026. [Generative Model]*.
- C. Son and S.-H. Lee. "Time-division near-field cell-free ISAC with location-based channel construction". *International Symposium on Modeling and Optimization in Mobile, Ad hoc, and Wireless Networks (WiOpt) 2026, Columbus, USA, June 2026. [ISAC]*.
- J. Yun, S.-H. Nam, H.-Y. Park, A. Rai, S.-H. Lee, and J. Bae. "Non-local and quantum advantages in network coding for multiple access channels". *Physical Review A, 042624, April 2026. [Quantum]*.
- R. Liu, B. Zheng, J. Lee, S.-H. Lee, G. Kaddoum, O. Gunlu, and D. Gunduz. "Secure communications, sensing and computing towards next generation networks". *IEEE Journal of Selected Areas in Communications (JSAC), pp. 4444-4470, Mar. 2026. [PLS]*.

**2025**

- C. Son and S.-H. Lee. "Group-aware rate-splitting multiple access for energy-efficient XR data transmission". *IEEE Wireless Communications Letters (WCL), pp. 815-819, Dec. 2025. [RSMA]*.
- H.-S. Im, K. Kim, J. Chung, and S.-H. Lee. "Joint optimization of trajectory and handover strategy for cellular-enabled UAV". *IEEE Access, pp. 136970-136984, Aug. 2025. [NTN]*.
- H.-S. Im, K. Kim, and S.-H. Lee. "Trajectory optimization for cellular-enabled UAV with connectivity and battery constraints". *IEEE Transactions on Vehicular Technology (TVT), pp. 1-16, June 2025. [NTN]*.
- W.-J. Jang, H. Park, and S.-H. Lee. "Provably near-optimal federated ensemble distillation with negligible overhead". *International Conference on Machine Learning (ICML) 2025, Vancouver, Canada, July, 2025. [Federated learning]*.
- S.-H. Nam, H.-Y. Park, J. Bae, and S.-H. Lee. "Quantum advantage in private multiple hypothesis testing". *in Proc. IEEE International Symposium on Information Theory (ISIT), Ann Arbor, USA, June 2025. (S.-H. Nam and H.-Y. Park equally contributed to this work) [Quantum, DP]*.

**2024**

- H.-Y. Park, S. Asoodeh, and S.-H. Lee. "Exactly minimax-optimal locally differentially private sampling". *Neural Information Processing Systems (NeurIPS) 2024, Vancouver, Canada, Dec. 2024. [DP]*.
- J.-M. Park, W.-J. Jang, T.-H. Oh, and S.-H. Lee. "Overcoming client data deficiency in federated learning by exploiting unlabeled data on the server". *IEEE Access, vol. 12, pp. 130007-130021, Sept. 2024. [Federated learning]*.
- S.-H. Nam, H.-Y. Park, and S.-H. Lee. "Achieving the exactly optimal privacy-utility trade-off with low communication cost via shared randomness". *IEEE Transactions on Information Theory (TIT), vol. 70, pp. 7447-7462, Oct. 2024. [DP]*.
- H.-Y. Park, S.-H. Nam, and S.-H. Lee. "No advantage of non-local cooperation in distributed compression of classical sources". *in Proc. IEEE Information Theory Workshop (ITW), Shenzhen, China, Nov. 2024. [Quantum]*.
- J. Hur and S.-H. Lee. "Joint trajectory and power optimization for UAV redeployment against an eavesdropper under consistent fairness constraint". *IEEE Communications Letters (CL), vol. 28, 2024. [NTN, PLS]*.
- J.-M. Park, C.-W. Moon ,B. C. Lee, E. Oh, J. Lee, W.-J. Jang, K. H. Cho and S.-H. Lee. "Detection of freezing of gait in Parkinson's disease from foot-pressure sensing insoles using a temporal convolutional neural network". *Frontiers in Aging Neuroscience, vol. 16, 2024. [ML Application]*.
- S.-H. Nam, V. Y. F. Tan, and S.-H. Lee. "Optimal private discrete distribution estimation with 1-bit communication". *IEEE Transactions on Information Forensics and Security (TIFS), vol. 19, pp.6514-6528, 2024. [DP]*.
- S.-H. Nam, V. Y. F. Tan, and S.-H. Lee. "Optimal private discrete distribution estimation with one-bit communication". *in Proc. IEEE International Symposium on Information Theory (ISIT), Athens, Greece, July 2024. [DP]*.
- S.-H. Nam, H.-Y. Park, and S.-H.Lee. "Achieving the exactly optimal privacy-utility trade-off with low communication cost via shared randomness". *in Proc. IEEE International Symposium on Information Theory (ISIT), Athens, Greece, July 2024. (S.-H. Nam and H.-Y. Park equally contributed to this work) [DP]*.
- H.-Y. Park, S.-H. Nam, and S.-H.Lee. "Exactly optimal and communication-efficient private estimation via block designs". *IEEE Journal on Selected Areas in Information Theory (JSAIT), vol. 5, pp. 123-134, 2024. [DP]*.
- H. Yeom, J. Lee, S.-H. Lee, and J. Ha. "Covert communication with multi-users cooperation at unequal distances". *IEEE International Conference on Communications (ICC), Denver, USA, June. 2024. [PLS]*.
- J. Lee, H. Yeom, S.-H. Lee, and J. Ha. "Channel correlation in multi-user covert communication: Friend or foe?". *IEEE Transactions on Information Forensics and Security (TIFS), vol. 19, pp.1469-1482, 2024. [PLS]*.

**2023**

- H.-S. Im, K. Kim, and S.-H. Lee. "Trajectory optimization for cellular-enabled UAV with connectivity and battery constraints". *in Proc. IEEE Vehicular Technology Conference (VTC), Oct. 2023. [NTN]*.
- H.-Y. Park, S.-H. Nam, and S.-H. Lee. "Block design-based local differential privacy mechanisms". *in Proc. IEEE International Symposium on Information Theory (ISIT), June 2023. [DP]*.
- J. Lee, D. T. Dinh, H. Yeom, S.-H. Lee, and J. Ha. "Multi-user cooperation for covert communication under quasi-static fading". *IEEE Transactions on Information Forensics and Security (TIFS), vol. 18, pp. 4625-4639, 2023. [PLS]*.
- S. Hong, K. Kim, and S.-H. Lee. "A hybrid jamming detection algorithm for wireless communications: Simultaneous classification of known attacks and detection of unknown attacks". *IEEE Communications Letters (CL), vol. 27, pp. 1769-1773, July 2023. [PLS]*.
- H.-S. Im and S.-H. Lee. "Anti-jamming games in multi-band wireless ad hoc networks". *IEEE Transactions on Information Forensics and Security (TIFS), vol. 18, pp. 872-887, 2023. [PLS]*.

**2022**

- S.-H. Nam and S.-H. Lee. "A tighter converse for the locally differentially private discrete distribution estimation under the one-bit communication constraint". *IEEE Signal Processing Letters, vol. 29, pp. 1923-1927, 2022*.
- K.-H. Cho and S.-H. Lee. "Covert communication over Gaussian multiple-access channels with feedback". *IEEE Wireless Communications Letters, vol. 11, no. 9, pp. 1985-1989, Sept. 2022*.
- S.-H. Nam and S.-H. Lee. "Secrecy capacity of a Gaussian wiretap channel with ADCs is always positive". *IEEE Transactions on Information Theory, vol. 68, pp. 1186-1196, Feb. 2022*.

**2021**

- H.-S. Im and S.-H. Lee. "Mobility-assisted covert communication over wireless ad hoc networks". *IEEE Transactions on Information Forensics and Security., vol. 16, pp. 1768-1781, 2021*.
- K.-H. Cho and S.-H. Lee. "Treating interference as noise is optimal for covert communication over interference channels". *IEEE Transactions on Information Forensics and Security, vol. 16, pp. 322-332, 2021*.

## 연락과 위치

- 교수연구실: KAIST IT융합빌딩(N1) 712호, 전화 042-350-7463[^ee][^sse]
- 교수 이메일: sihyeon@kaist.ac.kr[^home][^prof][^ee]
- 누리집 첫 화면은 학부 연구나 대학원 진학에 관심 있는 학생에게 교수에게 직접 연락하라고 안내한다.[^home]
[^p1]: C. Son, S.-H. Lee, IEEE Transactions on Wireless Communications 25, 22928-22940 (2026). <https://doi.org/10.1109/twc.2026.3730662> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: Y. Kim, C. Son, S.-H. Lee, IEEE Wireless Communications Letters 15, 4155-4159 (2026). <https://doi.org/10.1109/lwc.2026.3714502> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: H.-S. Im, K.-Y. Kim, S.-H. Lee, IEEE Transactions on Vehicular Technology 74, 17812-17828 (2025). <https://doi.org/10.1109/tvt.2025.3579005> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: H.-S. Im, S.-H. Lee, IEEE Transactions on Information Forensics and Security 18, 872-887 (2023). <https://doi.org/10.1109/tifs.2022.3227422> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: S.-H. Nam, H.-Y. Park, S.-H. Lee, IEEE Transactions on Information Theory 70, 7447-7462 (2024). <https://doi.org/10.1109/tit.2024.3448475> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: S.-H. Nam, H.-Y. Park, S.-H. Lee, J. Bae, IEEE Journal on Selected Areas in Communications 44, 5253-5266 (2026). <https://doi.org/10.1109/jsac.2026.3709807> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: W.-J. Jang, H.-S. Park, S.-H. Lee, International Conference on Machine Learning (ICML) 2025 (2025). <https://icml.cc/virtual/2025/poster/46350> 초록 기준(ICML 논문 페이지 게시 초록).
[^p8]: M. Bae, S.-H. Lee, International Conference on Machine Learning (ICML) 2026 (2026). <https://icml.cc/virtual/2026/poster/65970> 초록 기준(ICML 논문 페이지 게시 초록).
[^home]: 연구실 누리집 첫 화면 <https://sites.google.com/view/kaist-infolab> (연구실 소개, 학생 모집 안내, 교수 이메일, 2026-10-23 열람)
[^research]: 연구실 누리집 Research 페이지 <https://sites.google.com/view/kaist-infolab/research> (연구 초점, Next-Generation Communications·Statistical Inference and Machine Learning 두 갈래와 세부 주제 설명, 2026-10-23 열람)
[^team]: 연구실 누리집 Team 페이지 <https://sites.google.com/view/kaist-infolab/team> (연구실 현황, 교수 학위, Postdocs, Graduate Students, Alumni, 2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <https://sites.google.com/view/kaist-infolab/professor> (Short bio, Editorial Service, Selected Awards and Honors, Selected Conference Service, Selected Invited Talks, Teaching, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publications 페이지 <https://sites.google.com/view/kaist-infolab/publications> (논문 목록과 연구 주제 표시, 2026-10-23 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(이시현) <https://ee.kaist.ac.kr/professor/17632/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 디비전, 학위, 2026-10-23 열람)
[^eelist]: KAIST 전기및전자공학부 교수 목록 3쪽 <https://ee.kaist.ac.kr/professor-s1/?page=3> (겸임학과, 2026-10-23 열람)
[^sse]: KAIST 반도체시스템공학과 교수 <https://sse.kaist.ac.kr/professor/> (연구분야, 전화, 2026-10-23 열람)
[^sselab]: KAIST 반도체시스템공학과 연구실 <https://sse.kaist.ac.kr/research-laboratory/> (연구실 이름, 분야, 호실, 2026-10-23 열람)

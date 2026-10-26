# 신호 정보 통신 연구실 (Signal, Information & Communications for Everything, SIC-X LAB)

**KAIST 전기및전자공학부·안보과학기술대학원 · 최진석 교수**

- 분야: 저해상도 데이터 변환기와 확장 가능한 빔포밍을 쓰는 전력·계산 효율 다중 안테나(MIMO) 통신, 통합 센싱·통신(ISAC), 지상·비지상(위성) 통신망, 물리계층 보안 프리코딩, 통신을 위한 AI와 AI를 위한 통신
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 무선·이동통신[^home][^research][^p6], 네트워크 보안·프라이버시[^gst][^p7], 강화학습[^research], 디지털 트윈[^research], 모델 경량화·양자화[^research], 연합학습·분산 학습[^research]
- 홈페이지: <https://sic-x.kaist.ac.kr/>
- 근거와 출처: [신호 정보 통신 연구실 근거 페이지](sic-x-sources.md)

> 양자화 비트, 계산량, 용량, 파일럿처럼 자원이 제한될 때도 최적에 가까운 성능을 내는 신호 처리·학습 알고리즘을 설계하는 연구실로, 다중 안테나 통신, 통합 센싱·통신, 지상·비지상 통합망, 셀 프리 시스템과 통신 효율적인 AI를 연구한다.[^home][^research]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 최진석 교수의 연구실이다. 누리집 첫 화면은 연구실 이름을 SIC-X LAB, 「SIGNAL, INFORMATION & COMMUNICATIONS for EVERYTHING」, 「신호 정보 통신 연구실 (식스 랩)」으로 적는다.[^home] 전기및전자공학부 교수 소개는 소속연구실을 Signal, Information, and Communications Lab.으로, 주요 연구를 Wireless Communication Technology and System Development로 적고,[^ee] 안보과학기술대학원 교수 명단은 교수의 소속학과를 전기및전자공학부로, 세부 연구 분야를 물리계층보안통신·저전력통신·다중안테나통신·저궤도위성통신으로 적는다.[^gst]

누리집 첫 화면의 소개(ABOUT US)에 따르면 연구실은 양자화(연속적인 신호 값을 정해진 몇 개의 값 가운데 하나로 바꾸어 나타내는 일) 비트, 계산량, 용량, 파일럿(송신기와 수신기가 미리 알고 있어 채널 추정에 쓰는 기준 신호), 관측할 수 있는 정보처럼 자원이 근본적으로 제한될 때도 최적에 가까운 성능을 내는 신호 처리·학습 알고리즘을 설계한다. 최적화 이론과 추정 이론에 바탕을 두고, 연구는 MIMO(multiple-input multiple-output, 송신기와 수신기가 여러 안테나로 신호를 주고받는 방식), 통합 센싱·통신(ISAC, 같은 무선 장비와 신호로 통신과 센싱을 함께 하는 기술), 지상–비지상 통합망, 셀 프리(cell-free) 시스템에 걸친다. 같은 원리를 AI에도 가져와, 차세대 무선 시스템을 위해 통신 효율적이고 낮은 비트로 동작하며 강건한 학습 틀을 만든다고 적는다.[^home]

Research Areas 페이지는 연구를 MIMO 네 갈래와 AI/ML 세 갈래로 나눈다. MIMO 1(전력·계산 효율 통신)은 저해상도 ADC(아날로그 신호를 디지털 값으로 바꾸는 변환기)·DAC(디지털 값을 아날로그 신호로 바꾸는 변환기)를 송수신기에 써서 하드웨어 전력 소모를 줄이면서 통신 성능을 지키는 MIMO 시스템 설계와, 계산량이 안테나 수에 선형으로 늘어나는 확장 가능한 빔포밍(여러 안테나 신호의 크기와 위상을 조절해 특정 방향으로 신호를 모아 보내거나 받는 기술) 알고리즘이다. MIMO 2는 공유한 무선 인프라로 센싱과 다중 사용자 통신을 함께 하는 MIMO 통합 센싱·통신이고, 센싱과 통신이 파형과 빔 패턴 설계에 서로 맞서는 목표를 둔다는 점을 과제로 든다. MIMO 3은 지상 기지국과 정지궤도(GEO)·저궤도(LEO) 위성 시스템을 함께 설계하는 지상·비지상 통신 시스템 설계다. MIMO 4는 분산된 접속점(access point)들이 중앙 처리로 함께 송수신하는 프런트홀 용량 제약 셀 프리 통신과, 각 접속점이 국소 처리 뒤 압축한 측위 정보를 보내 중앙에서 합치는 분산 측위다.[^research]

AI/ML 1(통신을 위한 AI)은 부분 관측에서 숨은 시스템 상태를 추론하는 학습 에이전트로 무선 자원을 할당하는 심층 강화학습, 적은 파일럿과 빠르게 변하는 환경에서 학습 모델로 채널을 추정하는 AI 기반 채널 추정·예측 빔포밍, 드문 파일럿 측정에서 장소별 채널 지도(전력, 도달 시간, 각도)를 복원하는 디지털 트윈 기반 채널 추정이다. 디지털 트윈 갈래는 측정하지 않은 위치의 채널 특징을 학습 기반 보간으로 되살리고, 위상 오차를 바탕으로 지도를 보정해 기하·재질의 불일치를 보상한다고 적는다. AI/ML 2(AI를 위한 통신)는 원자료를 나누지 않고 무선 기기들이 로컬 모델 갱신만 주고받아 하나의 모델을 함께 학습하는 연합학습의 송수신기 설계와, 원자료 대신 작업에 필요한 의미 정보를 보내는 시맨틱 채널의 송수신기 설계다. AI/ML 3은 이진 신경망과 낮은 비트 양자화로 모델 크기와 추론 계산을 줄이는 AI 모델 압축이다.[^research]

## 주요 연구 주제

### 1. 저해상도 데이터 변환기를 쓰는 다중 안테나 시스템

Research Areas 페이지의 MIMO 1-A는 저해상도 ADC·DAC를 송수신기의 에너지 효율 부품으로 써서 하드웨어 전력 소모를 줄이면서 통신 성능을 지키는 MIMO 시스템 설계이고, 저해상도 변환기가 만드는 양자화 왜곡이 검출과 추정의 정확도를 떨어뜨리는 점을 과제로 든다.[^research] 대표 논문 1은 같은 주파수에서 동시에 보내고 받는 전이중 다중 사용자 시스템에서 안정적인 동작에 필요한 ADC 비트 수의 범위를 분석하고, 남은 자기 간섭과 양자화 왜곡을 줄이는 빔포밍을 설계했다.[^p1] 대표 논문 2는 해상도를 정하지 않은 DAC를 쓰는 RSMA 시스템에서 프리코딩·안테나 선택·전력 제어를 함께 정했고,[^p2] 대표 논문 3은 1비트 양자화 수신기의 채널 추정에 디더링을 썼다.[^p3] 최근 논문 목록에는 시간 교차 ADC(time-interleaved ADC, 여러 ADC가 차례로 번갈아 표본을 잡아 하나의 변환기처럼 동작하는 구조)의 불일치 문제를 추적 기반 혼합 보정으로 다루는 논문(IEEE Signal Processing Letters, 2025)도 있다.[^journal] 교수 페이지는 교수가 받은 IEEE ComSoc AP Outstanding Young Researcher Award(2023)가 에너지 효율 통신에 대한 기여를 기린 것이라고 적는다.[^prof]

### 2. 확장 가능한 대규모 MIMO 빔포밍

MIMO 1-B는 대규모 MIMO의 스펙트럼 효율과 에너지 효율을 살리기 위해, 계산량이 안테나 수에 선형으로 늘어나는 저복잡도 빔포밍 알고리즘을 설계하는 일이다.[^research] 대표 논문 4는 일반화 거듭제곱 반복 기반 프리코딩(GPIP)에서 역행렬 계산 때문에 안테나 수의 세제곱으로 늘던 계산량을, 행렬 구조를 이용한 두 가지 저복잡도 역행렬 계산으로 안테나 수의 제곱 차수로 낮췄다.[^p4] 최근 논문 목록에는 여러 RIS(재구성 지능형 표면, 반사 소자의 위상을 조절해 반사되는 전파의 방향을 바꿀 수 있는 표면)를 쓰는 다중 사용자 MIMO의 확장 가능한 빔포밍 논문과, 저차원 부분공간 관점으로 하이브리드 프리코딩을 다시 본 논문(두 편 모두 early access)도 있다.[^journal]

### 3. 통합 센싱·통신(ISAC)

MIMO 2는 센싱과 통신 기능을 함께 지원하는 다중 안테나 파형과 빔포밍 전략을 설계하는 일이다.[^research] 대표 논문 5는 채널 정보가 불완전한 다중 사용자·다중 표적 ISAC 시스템에서 원하는 레이더 성능을 보장하면서 합 스펙트럼 효율을 최대화하는 통신·레이더 공동 빔포밍 틀이다.[^p5] 교수 페이지에 따르면 교수는 이 논문으로 KAIST 2025 Future-Leading Technology Research Achievement Award(2026)를 받았다.[^prof] 최근 논문 목록에는 바이스태틱(송신기와 수신기가 서로 떨어진 곳에 있는 구성) ISAC 시스템에서 트랜스포머로 빔을 미리 정하는 예측 빔포밍 학회 논문(ICTC 2025, EUSIPCO 2026 채택)도 있다.[^conf]

### 4. 위성 통신과 지상·비지상 통합망

MIMO 3은 지상 기지국과 GEO·LEO 위성 시스템이 협력해 송수신하도록 함께 설계해 전 지구 통신 범위를 넓히는 일로, GEO 위성, LEO 위성, 지상 기지국 사이의 시스템 간·빔 간 간섭을 과제로 든다.[^research] 대표 논문 6은 지상의 가림 때문에 가시선과 비가시선 전파가 섞이는 LEO 위성망의 하향링크 커버리지 확률을 확률 기하로 분석해, 위성 밀도·고도·지상 환경이 서로 얽혀 있음을 보였다.[^p6] 최근 논문 목록에는 다중 빔 위성 통신의 대규모 MIMO 점근 성능 분석, LEO 위성망과 지상망의 주파수 공유, LEO 위성 통신의 시공간 빔포밍 논문도 있다.[^journal] 진행 중 과제에는 국방특화연구센터 과제 「이종 위성군 지원을 위한 통신 아키텍처 설계」가 있다.[^projects]

### 5. 물리계층 보안

안보과학기술대학원 교수 명단은 교수의 세부 연구 분야로 물리계층보안통신을 든다.[^gst] 물리계층 보안(무선 채널의 잡음·페이딩 같은 물리적 성질을 이용해 도청자가 정보를 얻지 못하게 하는 보안 기술) 연구에서 대표 논문 7은 여러 도청자가 결탁하는 다중 사용자 MIMO 시스템에서 프리코더와 인공 잡음을 함께 최적화하는 최대-최소 공정성 보안 프리코딩 알고리즘을 내놓고, 도청자 채널 정보를 일부만 아는 경우로 넓혔다.[^p7] 최근 논문 목록에는 유한 블록 길이에서 보안과 신뢰성을 함께 최적화하는 논문(IEEE Transactions on Wireless Communications, 2023), 부분 채널 정보 아래의 최대-최소 공정성 보안 프리코딩 논문(IEEE Wireless Communications Letters, 2023), 저해상도 양자화 아래의 보안 프리코딩과 안테나 선택 논문(IEEE Transactions on Vehicular Technology, 2026)도 있다.[^journal] 진행 중 과제에는 국방특화연구실 과제 「지능형 보안 수중 통신 (InSeCT) 특화연구실」이 있다.[^projects]

### 6. 통신을 위한 AI와 AI를 위한 통신

Research Areas 페이지의 AI/ML 갈래는 통신을 위한 AI(심층 강화학습 자원 할당, AI 기반 채널 추정·예측 빔포밍, 디지털 트윈 기반 채널 추정), AI를 위한 통신(연합학습·시맨틱 채널의 송수신기 설계), AI 모델 압축(이진 신경망)이다.[^research] 대표 논문 8은 1비트 ADC를 쓰는 상향링크 대규모 MIMO 시스템에서 양자화 출력의 횟수를 세어 우도를 학습해 명시적 채널 추정 없이 최대 우도 검출을 하고, 디더링과 심층 신경망 기반 신호 대 잡음비 추정으로 학습 부담을 줄였다.[^p8] 최근 논문 목록에는 레이트레이싱 디지털 트윈에서 재질을 강건하게 추정하는 학회 논문(ICTC 2026 채택)과, 불완전한 채널 정보 아래 NOMA 자원 할당을 위한 심층 강화학습 국내 학회 논문(2026)도 있다.[^conf][^domestic]

## 대표 논문

최진석 교수가 KAIST에 부임한 2023년 2월 뒤에 나온 학술지 논문 가운데, 여섯 연구 갈래(저해상도 데이터 변환기를 쓰는 다중 안테나 시스템, 확장 가능한 빔포밍, 통합 센싱·통신, 위성 통신망, 물리계층 보안, 학습 기반 검출)에서 초록을 확인할 수 있는 여덟 편을 골랐다. 대표 논문 5는 교수가 1저자이고, 나머지 일곱 편은 누리집이 교수를 교신저자(\*)로 표시한다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Full-Duplex Multiuser MISO Under Coarse Quantization: Per-Antenna SQNR Analysis and Beamforming Design](https://doi.org/10.1109/tcomm.2026.3698918) · IEEE Transactions on Communications | 전이중(full-duplex, 같은 주파수에서 동시에 보내고 받는 방식) 다중 사용자 MISO(기지국은 여러 안테나, 각 사용자는 안테나 하나를 쓰는 구성) 시스템에서 저해상도 ADC가 자기 간섭(self-interference, 자기가 보내는 신호가 자기 수신기로 섞여 들어오는 것)에 주는 영향을 밝히고, 양자화와 자기 간섭을 고려한 빔포밍 방법을 만들었다. 먼저 기존 선형 빔포머의 안테나별 신호 대 양자화 잡음비(SQNR)를 분석해, 안정적인 전이중 동작에 필요한 ADC 비트 수의 범위를 제시했다. 이를 바탕으로 남은 자기 간섭과 양자화 왜곡을 줄이는 빔포밍을 제안했다. 스펙트럼 효율(단위 시간·단위 대역폭당 보내는 데이터 양) 최대화 문제를 프리코더(송신 전에 여러 안테나로 보낼 신호를 미리 가공하는 행렬) 설계와 컴바이너(여러 안테나의 수신 신호를 합치는 필터) 설계 두 부분 문제로 나눠 번갈아 풀었다. 프리코더는 일반화 고유값 문제로 바꿔 거듭제곱 반복(power iteration)으로, 컴바이너는 양자화를 고려한 최소 평균 제곱 오차(MMSE) 필터로 구했다. 수치 실험에서 제안 방법에 필요한 ADC 비트 수는 유도한 이론 범위 안에 들었고, 비교 방법들 가운데 스펙트럼 효율이 가장 높았다.[^p1] | 1저자 S. Yoo, 마지막·교신 저자 최진석 (6명) |
| 2 | 2026 | [Power-Constrained and Quantized MIMO-RSMA Systems with Imperfect CSIT: Joint Precoding, Antenna Selection, and Power Control](https://doi.org/10.1109/twc.2026.3689604) · IEEE Transactions on Wireless Communications | 기지국에 주어진 전체 전력 예산을 다 쓰기 위해 프리코딩, 안테나 선택, 송신 전력 제어를 함께 정하는 알고리즘을 제안했다. 해상도를 정하지 않은(임의 해상도) DAC를 쓰는 하향링크 다중 사용자 MIMO RSMA(rate-splitting multiple access, 사용자에게 보낼 메시지를 공통 부분과 개별 부분으로 나눠 보내는 다중 접속 방식) 시스템에서 합 스펙트럼 효율을 최대화하는 문제를 세웠다. 송신기의 채널 정보(CSIT)가 불완전한 점은 조건부 평균 전송률 방법으로 정의한 에르고딕 합 스펙트럼 효율(채널 변화에 대해 평균한 합 스펙트럼 효율)로 다루고, 근사 기법으로 문제를 풀기 쉽게 바꿨다. 문제를 프리코딩 방향과 전력 제어 두 부분 문제로 나눠, 앞의 것은 더 나은 제약 조건을 반영한 최적화 식의 정류점(기울기가 0이 되는 후보 해)을 찾아, 뒤의 것은 경사 하강법으로 풀었다. 대규모 MIMO에 맞게 계산량을 줄이는 방법도 냈다. 모의실험은 알고리즘을 검증했고, 기지국 전력 예산을 다 쓸 때는 8∼11비트의 중간 해상도 DAC가 저해상도 DAC보다 실제로 전력 효율이 좋을 수 있음을 보였다.[^p2] | 1저자 J. Sung, 마지막·교신 저자 최진석 (3명) |
| 3 | 2026 | [Channel Estimation for One-Bit Quantized MIMO Systems: Dithering-Aided Approach](https://doi.org/10.1109/lwc.2026.3682511) · IEEE Wireless Communications Letters | 수신기가 1비트 양자화를 쓰는 MIMO 시스템의 채널 추정 방법이다. 1비트 양자화의 심한 비선형 왜곡 때문에 신호 대 잡음비가 중간 이상일 때 추정 정확도가 떨어지며, 초록은 그 원인으로 확률 공명 효과(stochastic resonance, 잡음이 비선형 시스템의 약한 신호 검출을 돕는 현상)를 든다. 이를 풀기 위해 양자화 전에 가우스 디더링(양자화하기 전에 신호에 일부러 잡음을 더하는 기법)을 넣고, 양자화된 디더 신호를 통계적으로 같은 선형 모형으로 다시 썼다. 이어서 선형화한 디더 몫을 지우고 연판정 정보(soft information)를 뽑은 뒤 선형 최소 평균 제곱 오차(LMMSE) 추정을 하는 양자화 인지 잡음 제거 기법을 개발했다. 평균 제곱 오차(MSE)를 유도해 이를 최소로 하는 디더 전력을 구했다. 모의실험에서 이 방법은 선형 추정의 계산 효율을 유지하면서 기존 방법보다 성능이 좋았다.[^p3] | 1저자 J. Kang, 마지막·교신 저자 최진석 (2명) |
| 4 | 2026 | [Generalized Power Iteration-based Precoding with Low-Complexity Matrix Inversion Approaches for Massive MIMO Systems](https://doi.org/10.1109/tvt.2025.3644169) · IEEE Transactions on Vehicular Technology | 일반화 거듭제곱 반복 기반 프리코딩(GPIP)은 다중 안테나 통신의 스펙트럼 효율 최대화에서 성능이 뛰어나지만, 역행렬 계산 때문에 계산량이 안테나 수의 세제곱으로 늘어 안테나가 많아지면 쓰기 어렵다. 이 논문은 채널 정보가 불완전한 상황에서 효율적인 GPIP 방법을 제안했다. GPIP 행렬의 구조를 이용해 두 가지 저복잡도 역행렬 계산법, 곧 역행렬 보조정리(matrix inversion lemma)에 바탕을 둔 저차원 역행렬 계산과 가우스-자이델 반복을 썼고, 계산량의 차수를 안테나 수의 제곱으로 낮췄다. 모의실험에서 성능을 유지하면서 계산 효율을 확인했다.[^p4] | 1저자 M. Oh, 마지막·교신 저자 최진석 (4명) |
| 5 | 2024 | [Joint and Robust Beamforming Framework for Integrated Sensing and Communication Systems](https://doi.org/10.1109/twc.2024.3454987) · IEEE Transactions on Wireless Communications | 통합 센싱·통신은 미래 무선 통신의 기반 기술로 널리 인정받는다. 이 논문은 다중 사용자·다중 표적 ISAC 시스템에서 채널 상태 정보(CSI)가 불완전할 때, 원하는 레이더 성능을 보장하면서 합 스펙트럼 효율을 최대화하는 통신·레이더 공동 빔포밍 틀을 내놓았다. 레이더 성능 제약으로는 레이더 송신 빔의 평균 제곱 오차(MSE)나 수신 신호 대 클러터·잡음비(SCNR, 클러터는 표적이 아닌 물체에서 돌아온 반사파) 가운데 하나를 쓴다. 비볼록성(최적화 문제가 볼록 문제의 조건을 만족하지 않는 성질)과 불완전한 CSI 문제를 풀기 위해 문제를 다시 세우고 공동 빔포머의 1차 최적성 조건을 구했다. 이 조건을 고유벡터에 의존하는 비선형 고유값 문제(NEPv)로 바꿔, 빔포머는 거듭제곱 반복으로, 라그랑주 승수는 이진 탐색으로 찾는 교대 방법을 개발했다. 이 틀은 두 레이더 지표를 모두 다루고, 낮은 계산량으로 채널 추정 오차에 강건하다. 모의실험에서 MSE 제약과 SCNR 제약은 동작 환경에 따라 서로 보완적인 성능을 보였다.[^p5] | 1저자 최진석, 마지막 저자 A. Alkhateeb (4명) |
| 6 | 2026 | [Low-Earth Orbit Satellite Network Analysis with Random LOS and NLOS Channels](https://doi.org/10.1109/tvt.2026.3698332) · IEEE Transactions on Vehicular Technology | 저궤도(LEO) 위성망의 성능은 지상의 가림 때문에 가시선(LOS, 송신기와 수신기 사이가 막히지 않은 경로)과 비가시선(NLOS) 전파가 섞여 정확히 나타내기 어렵다. 이 논문은 확률적 가림(shadowing) 아래 LEO 위성망의 하향링크 커버리지 확률(수신 신호 대 간섭비가 정해진 기준을 넘을 확률)을 분석하는 확률 기하(stochastic geometry, 기지국이나 위성의 위치를 무작위 점 배치로 모형화해 망 성능을 분석하는 수학 방법) 틀을 만들었다. 균일한 전파와 가장 가까운 위성 연결을 가정한 앞선 연구와 달리, 가장 센 신호의 위성에 연결하는 규칙을 쓰고 서로 다른 경로 손실과 페이딩 통계를 반영했다. 간섭이 성능을 좌우하는 영역에서 커버리지 확률의 정확한 해석식과 상·하한을 유도했고, 단순화한 가림·빔 이득 모형에서는 닫힌 꼴 근사식을 얻었다. 분석 결과 바람직한 위성 배치 밀도는 지상 전파 환경에도 달려 있고, 위성 밀도·고도·지상 환경이 서로 얽혀 있었다. 지상 환경이 더 조밀하면 간섭이 효과적으로 줄어 더 높은 위성 밀도를 감당할 수 있고, 고도가 낮으면 대체로 커버리지가 높지만 밀도 선택에 더 민감했다.[^p6] | 1저자 J. Lee, 마지막·교신 저자 최진석 (5명) |
| 7 | 2025 | [Artificial Noise-aided Max-Min Fairness Secrecy Precoding with Partial Wiretap Channel Knowledge](https://doi.org/10.1109/tvt.2025.3525836) · IEEE Transactions on Vehicular Technology | 인공 잡음(artificial noise, 도청자의 수신을 방해하려고 송신기가 일부러 함께 보내는 잡음 신호)을 쓰는 최대-최소 공정성(max-min fairness, 사용자들 가운데 가장 낮은 성능을 최대로 만드는 기준) 보안 프리코딩 알고리즘을 제안했다. 여러 도청자가 결탁하는 다중 사용자 MIMO 시스템에서 프리코더와 인공 잡음 공분산 행렬을 번갈아 풀지 않고 함께 최적화한다. 문제는 비볼록하고 매끄럽지 않으며 최적화 변수가 얽혀 있고, 송신기가 도청자 채널 정보를 일부만 안다는 어려움이 있다. 먼저 도청자 채널을 완전히 안다고 보고 문제를 매끄러운 문제로 근사한 뒤, 1차 최적성 조건을 유도해 비선형 고유값 문제로 해석하고 거듭제곱 반복으로 풀었다. 도청자 채널 정보가 일부뿐인 경우로 넓히기 위해 도청 전송률의 근사 하한을 유도해 평균 도청 전송률로 문제를 다시 세웠고, 이로써 일부 채널 지식을 활용하는 알고리즘을 제안했다. 모의실험으로 방법을 검증했다.[^p7] | 1저자 S. Kim, 마지막·교신 저자 최진석 (4명) |
| 8 | 2024 | [Learning-Based One-Bit Maximum Likelihood Detection for Massive MIMO Systems: Dithering-Aided Adaptive Approach](https://doi.org/10.1109/tvt.2024.3381757) · IEEE Transactions on Vehicular Technology | 1비트 ADC를 쓰는 상향링크 대규모 MIMO 시스템의 학습 기반 검출 틀을 제안했다. 이 검출은 각 안테나에서 양자화 출력 +1과 −1이 나온 횟수만 세어 우도 확률을 추정하므로, 1비트 양자화 시스템의 주요 난제였던 명시적 채널 추정 없이 최대 우도 검출(받은 신호가 나올 확률을 가장 크게 만드는 송신 신호를 고르는 검출)을 할 수 있다. 그러나 신호 대 잡음비가 높으면 수신이 거의 결정적이어서 1비트 관측이 +1이나 −1 한쪽으로 치우치고, 작은 우도 확률을 추정하려면 학습이 지나치게 많이 필요하다. 이를 해결하려고 디더링 신호를 더해 신호 대 잡음비를 인위적으로 낮춘 뒤, 오프라인으로 학습한 심층 신경망 기반 추정기가 내놓은 신호 대 잡음비 추정값으로 양자화된 디더 신호에서 우도 함수를 추론하는 「디더 후 학습」 기법을 제안했다. 양자화된 디더 신호의 패턴에 따라 디더링 전력을 갱신하는 적응형 방법으로 넓혔고, 다듬은 우도 확률로 비트별·사용자별 로그 우도비를 계산해 채널 부호화된 MIMO 시스템에도 적용했다. 모의실험으로 부호화하지 않은 시스템과 부호화한 시스템 모두에서 성능을 검증했다.[^p8] | 1저자 Y. Cho, 교신 저자 최진석 (3명) |

## 교수와 전문 분야

최진석 교수(Choi, Jinseok)는 KAIST 전기및전자공학부 부교수다. 학과 교수 소개는 직위를 부교수로, 주요 연구분야를 AI & Machine Learning, Information, Communication & Coding, Security, RF/mmWave Devices & Systems로, 학위를 Ph.D. (2019) Univ. of Texas at Austin으로 적는다.[^ee] 누리집 교수 페이지에 따르면 교수는 연세대학교에서 전기전자공학 학사와 경영학 학사(복수 학위)를 2014년에 받았고, The University of Texas at Austin에서 전기·컴퓨터공학 석사(2016)와 박사(2019)를 받았다. Qualcomm 무선 R&D의 Senior System Engineer(2019년 11월–2020년 9월), UNIST 조교수(2020년 10월–2023년 2월)를 거쳐 2023년 2월 KAIST 전기및전자공학부 조교수가 됐고, 2025년 3월부터 부교수다.[^prof]

교수 페이지의 경력 칸은 GST 겸임교수(2023년 7월–2027년 7월), G-School 겸임교수(2023년 6월–2025년 12월), LG-KAIST 6G Research Center 겸임교수(2023년 6월–2026년 6월), 뉴욕대학교(NYU) 겸임교수(2025년 8월–2027년 1월)를 적고, 짧은 소개는 KAIST의 Institute for Security Convergence, G-School, LG-KAIST 6G Research Center 겸임교수직을 든다. 학술지 편집 활동으로 IEEE Transactions on Wireless Communications(2024년 10월부터)와 IEEE Open Journal of the Communications Society(2024년 1월부터)의 Associate Editor를 적는다. 수상으로는 에너지 효율 통신에 대한 기여로 받은 IEEE ComSoc AP Outstanding Young Researcher Award(2023), 대표 논문 5로 받은 KAIST 2025 Future-Leading Technology Research Achievement Award(2026), KAIST 2025 Best Lecture Award(2026), KAIST Excellence in Technological Innovation Award(2023) 등을 적는다.[^prof] Teaching 페이지는 KAIST에서 맡은 과목으로 대학원 통신이론(EE50022)과 학부 최적화개론(EE40024), 통신공학(EE321), 정보이론 및 부호화 개론(EE326)을 적는다.[^teaching]

교수 페이지의 짧은 소개는 교수의 연구가 에너지 효율 통신, 새로운 다중 접속 기술, 사물인터넷(IoT) 통신, 위성 통신을 포함한 미래 무선 통신 시스템의 개발과 분석에 초점을 둔다고 적는다.[^prof] 이 소개와 2021–2026년 논문 목록을 함께 보면, 교수의 전문 분야는 다중 안테나 무선 통신 시스템의 최적화와 신호 처리이며, 특히 저해상도 데이터 변환기를 쓰는 에너지 효율 통신, RSMA 같은 새 다중 접속 방식, 위성 통신망 분석, 통합 센싱·통신과 물리계층 보안을 위한 빔포밍·프리코딩 설계다.[^prof][^journal]

## 응용 분야

누리집 첫 화면 소개는 연구실의 학습 틀이 차세대 무선 시스템을 위한 것이라고 적는다.[^home] 진행 중 과제의 이름과 사업명은 응용 대상으로 차세대네트워크(6G) 사업의 AI-Native 무선 인터페이스, 퓨처 모빌리티 서비스를 위한 AI 통신 센싱 융합, 차세대 센싱 V2X(차량이 다른 차량·도로 시설 등과 정보를 주고받는 통신) 기반 자율주행을 위한 저전력 고신뢰 센싱·통신 통합 시스템, Upper-mid Band를 지원하는 Cloud virtualized RAN(vRAN) 시스템, 국방 분야의 지능형 보안 수중 통신과 이종 위성군 통신 아키텍처를 든다.[^projects]

## 구성원

누리집 Researchers 페이지의 PhD STUDENT 칸 5명, MS STUDENT 칸 7명, INTERN 칸 2명, INDIVIDUAL RESEARCH 칸 1명, 모두 15명이다. 「과정」은 각 카드의 KAIST 줄(PhD, MS, MS-PhD Combined)을 따랐고, 학사 줄만 적힌 MS STUDENT 칸의 두 카드(남동현, 권우섭)는 칸 이름을 따랐다. 첫 화면 소식은 두 사람이 2026년 8월 석사과정으로 합류했다고 적는다. 「시작」은 카드의 소속·과정·시작 연월 줄 그대로이고, 「연구 주제」는 카드에 적힌 주제다.[^researchers][^home] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| 박석준(Seokjun Park) | 박사과정 | KAIST (PhD 2023.09 ~ ) | MIMO, Sat-Comm, ISAC | 1, 2 |
| 최은성(Eunsung Choi) | 박사과정 | KAIST (PhD 2024.03 ~ ) | MIMO, ISAC | 7 |
| 유승형(Seunghyeong Yoo) | 박사과정 | KAIST (PhD 2024.09 ~ ) | MIMO, Full Duplex | 1, 4 |
| 김선규(Sungyu Kim) | 석사과정 | KAIST (MS 2024.09 ~ ) | MIMO, Federated Learning, Compression | 7 |
| 강준(Jun Kang) | 석박사통합과정 (Lab. Leader) | KAIST (MS-PhD Combined 2024.09 ~ ) | Low-Power TRX, ISAC | 3 |
| 김세현(Sehyeon Kim) | 석사과정 | KAIST (MS 2025.03 ~ ) | Positioning, AI-Decoder |  |
| 정유라(Yura Jung) | 석사과정 | KAIST (MS 2025.03 ~ ) | AI-MIMO, Activity Detection |  |
| 양승부(Seungbu Yang) | 석사과정 | KAIST (MS 2025.03 ~ ) | Digital Twin, Channel Prediction |  |
| 배수민(Soomin Bae) | 석박사통합과정 | KAIST (MS-PhD Combined 2025.09 ~ ) | MIMO, ISAC |  |
| 한진호(Jinho Han) | 석사과정 | KAIST (MS 2025.09 ~ ) | AI Model Compression, Cell Clustering |  |
| 남동현(Donghyeon Nam) | 석사과정 | Yonsei Univ. (BS 2020.03 ~ ) | SATCOM, RL |  |
| 권우섭(Woosub Kwon) | 석사과정 | KAIST (BS 2019.03 ~ ) | Cell-free, Compression |  |
| 최우석(Woosuk Choi) | 인턴 | Chung-Ang Univ. (BS 2023.03 ~ ) | Cell-free, Compression |  |
| 최민우(Minwoo Choi) | 인턴 | KAIST (BS 2023.03 ~ ) | CSI Compression, Semantic |  |
| 김도윤(Doyoon Kim) | Individual Research | KAIST (BS 2025.03 ~ ) | AI-Beamformer |  |

## 졸업생

누리집 Researchers 페이지 ALUMNI 칸의 박사(PhD Degree) 1명, 석사(MS Degree) 4명, 학사(BS Degree) 2명, 모두 7명이다. 학위·학교·연월은 각 줄의 표기이고, 진로는 Next Position·New Position 칸, 학위 논문 칸은 Dissertation Title·Thesis Title이다. 학사 졸업생 2명의 학위 논문 칸은 Research Topic 칸이다.[^researchers]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| 오민택(Mintaek Oh) | PhD, KAIST (2026.08) | Post-doctoral Researcher at University of Toronto (Prof. Wei Yu's group) | Towards Next-Generation Precoding for MU-MIMO Systems under Practical Constraints |
| 김재현(Jaehyun Kim) | MS, KAIST (2026.08) |  | Ergodic Rate Analysis in Full-Duplex MISO Systems Under Coarse Quantization |
| 성지원(Jiwon Sung) | MS, KAIST (2026.02) | PhD Student at Stanford University | Tracking Algorithm for Hybrid Calibration of Time-Interleaved ADCs |
| 문찬호(Chanho Moon) | MS, KAIST (2026.02) | Captain at ROK Army | Probabilistic‑State‑Aware DRL for Fairness-based NOMA Resource Allocation with Partial Observability |
| 이상민(Sangmin Lee) | MS, UNIST (2024.08) |  | Toward Fair and Efficient Communication with Physical Layer Security |
| 박민규(Mingyu Park) | BS, Yonsei Univ. (2025.08) | MS Student at POSTECH (Prof. Namyoon Lee) | Research Topic: Sparse Recovery-based OFDM PAPR Reduction |
| 이준원(Junwon Lee) | BS, KAIST (2025.02) | Samsung Electronics | Research Topic: Stochastic Geometry-based Shadowed LEO Satellite Network Analysis |

## 최근 논문 목록 (2021–2026)

누리집 Publications 메뉴의 Journal, Conference, Domestic 페이지에 오른 2021–2026년 항목이다. 국제 학술지 35편(Journal 페이지 [PUBLISHED/ACCEPTED] 칸의 10–44번), 국제 학술대회 34편(Conference 페이지 C9–C42), 국내 학술지 3편(Domestic 페이지 DJ1–DJ3), 국내 학술대회 34편(DC1–DC34), 모두 106편이다. 저자·제목·학술지와 학회 표기는 누리집 그대로이고, 저자 뒤 \*는 누리집이 밝힌 교신저자 표시다. 이 목록은 교수의 논문 목록이라, 교수가 KAIST에 부임한 2023년 2월 전(UNIST 재직 시기 등)에 나온 논문도 들어 있다.[^journal][^conf][^domestic][^prof]

연도는 서지에 적힌 연도다. 학술지 서지가 early access로만 적힌 3편(42–44번)은 연도가 없고, 첫 화면 소식이 2026년 6월과 8월에 게재 승인(accepted)을 알려 2026년에 두었다.[^journal][^home] 학회 이름 뒤에 누리집이 accepted로 적은 국제 학술대회 6편은 「채택」으로 표시했다. 국내 학술지 3편은 누리집이 게재 승인(accepted)만 적고 연도를 적지 않아 「연도 표기 없음」에 두었다. 학회 날짜가 열람일(2026-10-23) 뒤인 국내 학술대회 2편(DC33, DC34)은 누리집에 적힌 날짜임을 표시했다.[^conf][^domestic]

**2026**

- M. Oh, and J. Choi\*. "Scalable Beamforming Design for Multi-RIS-Aided MU-MIMO Systems with Imperfect CSIT". *IEEE Transactions on Wireless Communications (TWC), early access (학술지)*.
- M. Oh and J. Choi\*. "Hybrid Precoding Revisited: Low-Dimensional Subspace Perspective for MU-MIMO Systems". *IEEE Transactions on Vehicular Technology (TVT), early access (학술지)*.
- J. Lee, J. Park, J. Lee, N. Lee, and J. Choi\*. "Low-Earth Orbit Satellite Network Analysis with Random LOS and NLOS Channels". *IEEE Transactions on Vehicular Technology (TVT), early access (학술지)*.
- S. Yoo, J. Kim, S. Park, M. Oh, N. Lee, and J. Choi\*. "Full-Duplex Multiuser MISO Under Coarse Quantization: Per-Antenna SQNR Analysis and Beamforming Design". *IEEE Transactions on Communications (TCOM), vol. 74, pp. 9742-9757, Jun. 2026 (학술지)*.
- J. Sung, S. Park, and J. Choi\*. "Power-Constrained and Quantized MIMO-RSMA Systems with Imperfect CSIT: Joint Precoding, Antenna Selection, and Power Control". *IEEE Transactions on Wireless Communications (TWC), vol. 25, pp. 17634-17648, May, 2026 (학술지)*.
- J. Kang and J. Choi\*. "Channel Estimation for One-Bit Quantized MIMO Systems: Dithering-Aided Approach". *IEEE Wireless Communications Letters (WCL), vol. 15, pp. 2604-2608, Apr., 2026 (학술지)*.
- J. Yim, J. Choi, J. Park, I. O. Roberts, and N. Lee. "Space-Time Beamforming for LEO Satellite Communications: Enabling Extremely Narrow Beams". *IEEE Transactions on Wireless Communications (TWC), vol. 25, pp. 12725-12739, Feb., 2026 (학술지)*.
- D. Kim, J. Park, J. Choi, and N. Lee. "Spectrum Sharing Between Low Earth Orbit Satellite and Terrestrial Networks: A Stochastic Geometry Perspective Analysis". *IEEE Transactions on Wireless Communications (TWC), vol. 25, pp. 8905-8921, 2026 (학술지)*.
- M. Oh, S. Yoo, N. Lee, and J. Choi\*. "Generalized Power Iteration-based Precoding with Low-Complexity Matrix Inversion Approaches for Massive MIMO Systems". *IEEE Transactions on Vehicular Technology (TVT), vol. 75, pp. 11908 - 11913, no. 6, Jun., 2026 (학술지)*.
- S. Bae, S. Yoo, S. Lee, and J. Choi\*. "Joint Secure Max-Min Fairness Precoding and Antenna Selection under Coarse Quantization". *IEEE Transactions on Vehicular Technology (TVT), vol. 75, no. 4, pp. 6899-6903, April, 2026 (학술지)*.
- N. Kim, J. Han, A. Alkhateeb, J. Choi, C.-B. Chae, and J. Park. "Integrated Sensing and Communications in Downlink FDD MIMO without CSI Feedback". *IEEE Transactions on Wireless Communications (TWC), vol. 25, pp. 2984-3000, Aug. 2026 (학술지)*.
- J. Kim and J. Choi. "SQNR Analysis for Coarse-Quantized Full-Duplex MU-MISO". *ICTC 2026, Jeju Island, Korea (국제 학회, 채택: 누리집 표기 accepted)*.
- S. Yang and J. Choi. "Order-Dependent Phase Reliability for Robust Material Estimation in Ray-Tracing Digital Twins". *ICTC 2026, Jeju Island, Korea (국제 학회, 채택: 누리집 표기 accepted)*.
- H. Kim, S. Lee, J. Choi, and N. Lee. "Robust Wideband Beamforming for MIMO-OFDM Integrated Sensing and Communication Systems". *IEEE Global Conf. on Commun. (GLOBECOM) 2026 (국제 학회, 채택: 누리집 표기 accepted)*.
- M. Park, J. Choi, and N. Lee. "Peak Isolation and Compressive Recovery: A CS-Based PAPR Reduction Framework for OFDM". *IEEE Global Commun. Conf. (GLOBECOM) 2026 (국제 학회, 채택: 누리집 표기 accepted)*.
- S. Park and J. Choi. "Cross-Attention Transformer Architecture for Predictive Beamforming in Bistatic ISAC Systems with Quantized Feedback". *IEEE Int. Conf. on Acoustics, Speech and Signal Process. (EUSIPCO) 2026 (국제 학회, 채택: 누리집 표기 accepted)*.
- Y. Yang, D. Zhang, J. Choi, and B. Gu. "Leakage Failure Probability Optimization for Secured xURLLC in Mission Critical Applications". *IEEE Int. Symp. on Inform. Theory (ISIT), 2026 (국제 학회)*.
- S. Bae and J. Choi. "Mutual Coherence-Aware Subcarrier Pattern Selection for CS-Based OFDM-ISAC Sensing". *IEEE WiOpt Workshops on Integrated Sensing and Communications, 2026 (국제 학회)*.
- 김선규, 이남윤, 최진석. "ITU-R P.2001-6 기반 VHF 대역 장거리 통신 성능 분석". *한국통신학회 추계종합학술대회 (KICS), Nov., 19-20, 2026, 강원도 홍천 (국내 학회, 누리집 기재 날짜)*.
- 박석준, 최진석. "저분해능 DAC 환경의 백홀 기반 지상-비지상 통합망 빔포밍 기법". *항공우주학회 추계종합학술대회 (KSAS), Nov., 10-13, 2026, 하이원 (국내 학회, 누리집 기재 날짜)*.
- 양승부, 최진석. "다중 재질 디지털 트윈을 위한 반사 차수별 위상 오차 추정 기반 레이트레이싱 보정". *한국통신학회 하계종합학술대회 (KICS), June, 17-19, 2026, 제주 (국내 학회)*.
- 양승부, 문찬호, 최진석. "IDW 보간 및 GAT 기반 RF 맵 구축". *통신 정보 합동 학술대회 (JCCI), Apr. 15-17, 2026, 여수 (국내 학회)*.
- 문찬호, 오민택, 최진석. "불완전한 CSI 환경에서의 NOMA 자원 할당을 위한 심층 강화학습 기법". *한국통신학회 동계종합학술대회 (KICS), Feb. 4-6, 2026, 용평 (국내 학회)*.

**2025**

- J. Sung, and J. Choi\*. "A New Interpretation of the Time-Interleaved ADC Mismatch Problem: A Tracking-Based Hybrid Calibration Approach". *IEEE Signal Processing Letters (SPL), vol. 32, pp. 3710-3714, Sep. 2025 (학술지)*.
- S. Kim, J. Choi, W. Shin, N. Lee, and J. Park. "Multibeam Satellite Communications with Massive MIMO: Asymptotic Performance Analysis and Design Insights". *IEEE Transactions on Wireless Communications (TWC), vol. 24, no. 11, pp. 9449-9464, Nov. 2025 (학술지)*.
- S. Park, J. Choi\*, J. Park, N. Lee, and B. Clerckx. "Optimizing Spectral and Energy Efficiency of Quantized Multiuser MISO-RSMA Systems with Imperfect CSIT". *IEEE Transactions on Communications (TCOM), vol. 73, no. 10, pp. 9536-9552, Oct. 2025 (학술지)*.
- H. Lee, J. Kim, G. Choi, I. P. Roberts, J. Choi, and N. Lee. "Nonlinear Self-Interference Cancellation With Learnable Orthonormal Polynomials for Full-Duplex Wireless Systems". *IEEE Transactions on Wireless Communications (TWC), vol. 24, no. 7, pp. 5796-5810, Jul. 2025 (학술지)*.
- S. Kim, E. Choi, M. Oh, and J. Choi\*. "Artificial Noise-aided Max-Min Fairness Secrecy Precoding with Partial Wiretap Channel Knowledge". *IEEE Transactions on Vehicular Technology (TVT), vol. 74, no. 5, pp. 8390-8395, May 2025 (학술지)*.
- J. Kim, J. Choi, J. Park, A. Alkhateeb, and N. Lee. "FDD Massive MIMO: How to Optimally Combine UL Pilot and Limited DL CSI Feedback?". *IEEE Transactions on Wireless Communications (TWC), vol. 24, no. 2, pp. 926 - 939, Feb. 2025 (학술지)*.
- S. Park and J. Choi. "Echo-aware Transformer-based Predictive Beamforming in Bistatic Integrated Sensing and Communication Systems". *ICTC 2025, Jeju Island, Korea (국제 학회)*.
- M. Park and J. Choi. "Survey on PAPR Reduction: from Signal Processing to Machine Learning-based Techniques". *ICTC 2025, Jeju Island, Korea (국제 학회)*.
- J. Yim, J. Choi, and N. Lee. "Space-Time Beamforming for Uplink Direct-to-Cell Connectivity in Dense LEO Satellite Networks". *IEEE Military Commun. Conf. (MILCOM), 2025 (국제 학회, 채택: 누리집 표기 accepted)*.
- J. Sung, S. Park, and J. Choi. "Joint Optimization for Power-Constrained MIMO Systems: Is Low-Resolution DAC Still Optimal?". *IEEE Vehicular Technology Conference (VTC), 2025 (국제 학회)*.
- 박석준, 최진석. "바이스태틱 센싱-통신 통합 시스템을 위한 트랜스포머 활용 예측 빔포밍 (Best Paper Award)". *한국통신학회 추계종합학술대회 (KICS), Nov. 19-21, 2025, 경주 (국내 학회)*.
- 문찬호, 오민택, 최진석. "트랜스포머 기반 강화학습을 활용한 ISM대역 채널 할당 및 전력 제어 기법". *한국통신학회 하계종합학술대회 (KICS), June, 18-21, 2025, 제주 (국내 학회)*.
- 성지원, 최진석. "초광대역 위성간 통신을 위한 시간 교차 ADC 시스템". *통신 정보 합동 학술대회 (JCCI), Apr. 23-25, 2025, 속초 (국내 학회)*.
- 김재현, 최진석. "저해상도 ADC 를 고려한 상향 링크 다중 유저/안테나 전송률 분석". *통신 정보 합동 학술대회 (JCCI), Apr. 23-25, 2025, 속초 (국내 학회)*.

**2024**

- J. Choi, J. Park, N. Lee, and A. Alkhateeb. "Joint and Robust Beamforming Framework for Integrated Sensing and Communication Systems". *IEEE Transactions on Wireless Communications (TWC), vol. 23, no. 11, pp. 17602 - 17618, Nov. 2024 (학술지)*.
- Y. Cho, J. Choi\*, and B. L. Evans. "Learning-Based One-Bit Maximum Likelihood Detection for Massive MIMO Systems: Dithering-Aided Adaptive Approach". *IEEE Transactions on Vehicular Communications (TVT), vol. 73, no. 8, pp. 11680 - 11693, Aug. 2024 (학술지)*.
- J. Kim, H. Lee, H. Do, J. Choi, J. Park, W. Shin, Y. C. Eldar, and N. Lee. "On the Learning of Digital Self-Interference Cancellation in Full-Duplex Radios". *IEEE Wireless Communications, vol. 31, no. 4, pp. 184 - 191, Aug. 2024 (학술지)*.
- Y. Cho, J. Choi\*, and B. L. Evans. "Coordinated Per-Antenna Power Minimization for Multicell Massive MIMO Systems with Low-Resolution Data Converters". *IEEE Transactions on Communications (TCOM), vol. 72, no. 2, pp. 1119 - 1134, Feb. 2024 (학술지)*.
- J. Park, B. Lee, J. Choi, H. Lee, N. Lee, S. Park, K. Lee, J. Choi, S. H. Chae, S. Jeon, K. S. Kwak, B. Clerckx, and W. Shin. "Rate-Splitting Multiple Access for 6G: Ten Promising Scenarios and Applications". *IEEE Network, vol. 38, no. 3, pp. 128 - 136, May, 2024 (학술지)*.
- E. Choi, S. Park, J. Choi, J. Park, and N. Lee. "Beamforming Optimization for Integrated Sensing and Communication Systems with SCNR Consideration". *IEEE WiOpt Workshops on Integrated Sensing and Communications, 2024 (국제 학회)*.
- M. Oh, J. Choi, S. Kim, and J. Park. "Wideband Channel Tracking with Quantization Distortion". *ICTC, Oct. 16-18, 2024 Jeju Island, Korea (국제 학회)*.
- J. Lee and J. Choi. "Stochastic Geometry-Based Coverage Analysis of Satellite Networks with Shadowing and Beam Gain Considerations". *ICTC, Oct. 16-18, 2024, Jeju Island, Korea (국제 학회)*.
- S. Bae, S. Lee, S. Yoo, and J. Choi. "Max-Min Fairness Precoding with Low Resolution DACs". *ICTC, Oct. 16-18, 2024, Jeju Island, Korea (국제 학회)*.
- S. Bae and J. Choi. "Joint Precoding and Antenna Selection for Sum Spectral Efficiency Maximization (Best Paper Award)". *ICTC, Oct. 16-18, 2024, Jeju Island, Korea (국제 학회)*.
- J. Kim, J. Choi, J. Park, A. Alkhateeb, and N. Lee. "FDD Massive MIMO: How to Optimally Combine UL Pilot and Limited DL CSI Feedback?". *IEEE Global Conf. on Commun. (GLOBECOM), Dec. 8–12, 2024, Cape Town, South Africa (국제 학회)*.
- S. Park, J. Sung, J. Choi, J. Park, and W. Shin. "Maximizing Energy and Spectral Efficiency Tradeoff in MIMO-RSMA Systems under Coarse Quantization". *European Signal Processing Conference (EUSIPCO), Aug. 26-30, 2024, Lyon, France (국제 학회)*.
- S. Park, J. Choi, J. Park, W. Shin, and B. Clerckx. "Rate-Splitting Multiple Access Precoding Optimization for MIMO Communications under Coarse Quantization". *IEEE Int. Conf. on Commun. (ICC), 9-14 June 2024, Denver, CO, USA (국제 학회)*.
- 박석준, 최은성, 최진석. "SCNR 및 MSE 값 조정을 통한 센싱-통신 통합 시스템 (Best Paper Award)". *한국통신학회 추계종합학술대회 (KICS), Nov. 20-22, 2024, 경주 (국내 학회)*.
- 박석준, 최은성, 최진석, 박정훈, 이남윤. "통신 중심의 빔포밍을 이용한 통합 센싱 및 통신 (Haedong Best Paper Award)". *한국통신학회 하계종합학술대회 (KICS), Jun. 19-22, 2024, 제주 (국내 학회)*.
- 오민택, 최진석. "다중 RIS 기반 mmWave 통신 시스템을 위한 전송 기법 설계". *한국통신학회 하계종합학술대회 (KICS), Jun. 19-22, 2024, 제주 (국내 학회)*.
- 최은성, 최진석. "피드 별 파워 제약 기반 위성 빔 형성 최적화". *한국통신학회 하계종합학술대회 (KICS), Jun. 19-22, 2024, 제주 (국내 학회)*.
- 유승형, 박석준, 오민택, 최진석. "저해상도 양자화기를 고려한 Full-Duplex 시스템의 성능 분석 실험". *통신 정보 합동 학술대회 (JCCI), Apr. 24-26, 2024, 부산 (국내 학회)*.
- 성지원, 박석준, 최진석. "양자화기 기반 전송률분할 다중접속 프리코더 및 전송 전력 최적화". *통신 정보 합동 학술대회 (JCCI), Apr. 24-26, 2024, 부산 (국내 학회)*.
- 최은성, 유승형, 김선규, 최준일, 최진석. "저궤도 위성 네트워크 커버리지 분석 서베이". *한국한공우주학회 춘계학술대회 (KSAS), Apr. 3-5, 2024, 제주 (국내 학회)*.
- 배수민, 유승형, 이상민, 최진석. "저해상도 DAC 시스템에서 공정 데이터율을 위한 빔포밍". *한국통신학회 동계종합학술대회 (KICS), Jan. 31-Feb. 2, 2024, 용평 (국내 학회)*.
- 김선규, 최은성, 오민택, 최진석. "보수적인 보안 통신 및 공정 데이터율을 위한 인공 잡음 기반 보안 프리코딩 디자인". *한국통신학회 동계종합학술대회 (KICS), Jan. 31-Feb. 2, 2024, 용평 (국내 학회)*.
- 오민택, 박정훈, 최진석. "저지연 보안 통신 시스템을 위한 전송 기법 설계 (Best Paper Award)". *한국통신학회 동계종합학술대회 (KICS), Jan. 31-Feb. 2, 2024, 용평 (국내 학회)*.

**2023**

- S. Lee, E. Choi, and J. Choi\*. "Max-Min Fairness Precoding for Physical Layer Security with Partial Channel Knowledge". *IEEE Wireless Communications Letters (WCL), vol. 12, no. 9, pp. 1637-1641, Sep. 2023 (학술지)*.
- M. Oh, J. Park, and J. Choi\*. "Joint Optimization for Secure and Reliable Communications in Finite Blocklength Regime". *IEEE Transactions on Wireless Communications (TWC), vol. 22, no. 12, pp. 9457-9472, Dec. 2023 (학술지)*.
- S. Park, J. Choi\*, J. Park, W. Shin, and B. Clerckx. "Rate-Splitting Multiple Access for Quantized Multiuser MIMO Communications". *IEEE Transactions on Wireless Communications (TWC), vol. 22, no. 11, pp 7696-7711, Nov. 2023 (학술지)*.
- S. Kim, J. Choi, and J. Park. "Downlink NOMA for Short-Packet Internet-of-Things Communications with Low-Resolution ADCs". *IEEE Internet of Things Journal (IoTJ), vol. 10, no. 7, pp. 6126 - 6139, Apr. 2023 (학술지)*.
- E. Choi, M. Oh, J. Choi\*, J. Park, N. Lee, and N. Al-Dhahir. "Joint Precoding and Artificial Noise Design for MU-MIMO Wiretap Channels". *IEEE Transactions on Communications (TCOM), vol. 71, no. 3, pp. 1564 - 1578, Mar. 2023 (학술지)*.
- D. Kim, J. Choi, J. Park, and D. K. Kim. "Max-Min Fairness Beamforming with Rate-Splitting: Optimization without Toolbox". *IEEE Wireless Communications Letters (WCL), vol. 12, no. 3, pp. 232 - 236, Feb. 2023 (학술지)*.
- J. Park, J. Choi, N. Lee, W. Shin, and H. V. Poor. "Rate-Splitting Multiple Access for Downlink MIMO: A Generalized Power Iteration Approach". *IEEE Transactions on Wireless Communications (TWC), vol. 22, no. 3, pp. 1588 - 1603, Mar. 2023 (학술지)*.
- J. Park, J. Choi, and N. Lee. "A Tractable Approach to Coverage Analysis in Downlink Satellite Network". *IEEE Transactions on Wireless Communications (TWC), vol. 22, no. 2, pp. 793 - 807, Feb. 2023 (학술지)*.
- S. Lee, E. Choi, and J. Choi. "Max-Min Fairness Precoding for Enhanced Security with Partial Channel Knowledge". *ICTC, 2023, Jeju Island, Korea (국제 학회)*.
- S. Kim, S. Yoo, and J. Choi. "Downlink Satellite Network Analysis with Beam Gain in Shadowing Channel". *ICTC, 2023, Jeju Island, Korea (국제 학회)*.
- S. Kim, J. Park, M. Oh, and J. Choi. "OFDM Simulator for Underwater Acoustic Communications". *ICTC, 2023, Jeju Island, Korea (국제 학회)*.
- M. Oh, J. Choi, S. Yoo, S. Kim, S. Kim, and J. Park. "A Survey on Statistical Channel Modeling for Underwater Acoustic Communications". *ICTC, 2023, Jeju Island, Korea (국제 학회)*.
- E. Choi, M. Oh, J. Choi, J. Park , N. Lee, and N. Al-Dhahir. "Joint and Simultaneous Optimization of Artificial Noise-aided Precoding for Secure Communications". *IEEE Global Conf. on Commun. (GLOBECOM), 2023, Kuala Lumpur, Malaysia (국제 학회)*.
- S. Yoo, S. Park, and J. Choi. "Joint Precoding and Combining for Quantized Full-Duplex MU-MIMO Systems". *IEEE Veh. Technol. Conf. Workshop (VTC), 2023, Florence, Italy (국제 학회)*.
- S. Lee, S. Park, J. Park, and J. Choi. "Rate-Splitting Multiple Access Precoding for Selective Security". *IEEE Veh. Technol. Conf. Workshop (VTC), 2023, Florence, Italy (국제 학회)*.
- J. Choi, J. Park, J. Lee, and N. Lee. "Coverage Analysis for Downlink Satellite Networks: Effect of Shadowing". *IEEE Int. Conf. on Commun. (ICC), 28 May–01 June 2023, Rome, Italy (국제 학회)*.
- 김선규, 유승형, 최진석. "빔 이득을 고려한 쉐도잉 채널에서의 다운링크 위성 네트워크 분석". *한국통신학회 추계종합학술대회 (KICS), Nov. 22-24, 2023, 경주 (국내 학회)*.
- 이상민, 최은성, 최진석. "부분적인 채널 지식 하에서의 보안 통신을 위한 최대-최소 공정성 빔포밍". *한국통신학회 추계종합학술대회 (KICS), Nov. 22-24, 2023, 경주 (국내 학회)*.
- 박정훈, 최진석, 이남윤. "랜덤한 고도를 가지는 저궤도 인공위성 네트워크의 모델링 및 분석 기법". *통신 정보 합동 학술대회 (JCCI), Apr. 26-28, 2023, 여수 (국내 학회)*.
- 최은성, 최진석, 박정훈, 이준세, 이남윤. "다운링크 위성 네트워크에서의 쉐도잉을 고려한 커버리지 분석". *통신 정보 합동 학술대회 (JCCI), Apr. 26-28, 2023, 여수 (국내 학회)*.
- 김대은, 박정훈, 최진석, 이남윤. "동적 협력 빔포밍을 고려한 다운링크 위성 네트워크의 커버리지 분석". *통신 정보 합동 학술대회 (JCCI), Apr. 26-28, 2023, 여수 (국내 학회)*.
- 김도선, 최진석, 박정훈, 김동구. "전송률 분할 다중 접속 기술에서 서비스 품질 향상을 위한 최대 최소 공정성 빔포밍 설계에 관한 연구". *한국통신학회 동계종합학술대회 (KICS), Feb. 8-10, 2023, 용평 (국내 학회)*.
- 박석준, 최진석, 박정훈, 신원재. "저해상도 데이터변환 기반 다중 안테나 시스템을 위한 전송률 분할 기반 다중접속 프리코딩 최적화 기법". *한국통신학회 동계종합학술대회 (KICS), Feb. 8-10, 2023, 용평 (국내 학회)*.
- 유승형, 박석준, 최진석. "양자화된 전이중 다중 사용자 및 다중 안테나 시스템에 대한 프리코더 설계". *한국통신학회 동계종합학술대회 (KICS), Feb. 8-10, 2023, 용평 (국내 학회)*.
- 이상민, 최진석. "전송률분할 기반 다중접속 네트워크의 물리계층 보안을 위한 프레임워크". *한국통신학회 동계종합학술대회 (KICS), Feb. 8-10, 2023, 용평 (국내 학회)*.

**2022**

- K. Lee, J. Choi, D. K. Kim, and J. Park. "Secure Transmission for Hierarchical Information Accessibility in Downlink MU-MIMO". *IEEE Transactions on Communications (TCOM), vol. 70, no. 9, pp. 6181 - 6195, Sep. 2022 (학술지)*.
- J. Choi, J. Park, and N. Lee. "Energy Efficiency Maximization Precoding for Quantized Massive MIMO Systems". *IEEE Transactions on Wireless Communications (TWC), vol. 21, no. 9, pp. 6803 - 6817, Sep. 2022 (학술지)*.
- M. Oh, J. Park, and J. Choi. "Secure Internet-of-Things Communications: Joint Precoding and Power Control". *IEEE Int. Conf. on Commun. (ICC), 16–20 May 2022, Seoul, South Korea (국제 학회)*.
- Y. Cho, J. Choi, and B. L. Evans. "Coordinated Beamforming in Quantized Massive MIMO Systems with Per-Antenna Constraints". *IEEE Wireless Commun. and Networking Conf. (WCNC), 10–13 Apr. 2022, Austin, TX, USA (국제 학회)*.
- M. Oh, J. Park, N. Lee, and J. Choi. "Energy-Efficient Precoding for Massive MIMO Systems with Low-Resolution Quantizers". *IEEE Wireless Commun. and Networking Conf. (WCNC),10–13 Apr. 2022, Austin, TX, USA (국제 학회)*.
- 오민택, 최진석, 박정훈. "딥러닝을 활용한 블라인드 칼만 필터 설계 (Best Paper Award)". *한국통신학회 추계종합학술대회 (KICS), Nov. 11.16-18, 2022, 경주 (국내 학회)*.
- 최건, 최진석, 박정훈, 이남윤. "Deep-Learning 을 이용한 Kalman Filter 의 성능 향상 방안". *한국통신학회 하계종합학술대회 (KICS), Jun. 22-24, 2022, 제주 (국내 학회)*.
- 최은성, 오민택, 최진석. "보안 커뮤니케이션을 위한 프리코딩 및 인공 노이즈의 공동 디자인 프레임워크 (Best Paper Award)". *한국통신학회 하계종합학술대회 (KICS), Jun. 22-24, 2022, 제주 (국내 학회)*.
- 오민택, 박정훈, 최진석. "양자화된 다중 안테나 시스템에서 에너지 효율을 극대화하는 프리코딩 기법". *한국통신학회 동계종합학술대회 (KICS), Feb. 9-11, 2022, 평창 (국내 학회)*.

**2021**

- J. Choi and J. Park. "MIMO Design for Internet-of-Things: Joint Optimization of Spectral Efficiency and Error Probability in Finite Blocklength Regime". *IEEE Internet of Things Journal (IoTJ), vol. 80, no. 20, pp.15512-15521, Oct. 2021 (학술지)*.
- J. Choi, Y. Cho, and B. L. Evans. "Quantized Massive MIMO Systems with Multicell Coordinated Beamforming and Power Control". *IEEE Transactions on Communications (TCOM), vol. 69, no. 2, pp. 946-961, Feb., 2021 (학술지)*.
- J. Choi and J. Park. "Sum Secrecy Spectral Efficiency Maximization in Downlink MU-MIMO: Colluding Eavesdroppers". *IEEE Transactions on Vehicular Technology (TVT), vol. 70, no. 1, pp. 1051-1056, Jan., 2021 (학술지)*.
- J. Park, J. Choi, W. Shin, and N. Lee. "Block Orthogonal Sparse Superposition Codes". *IEEE Global Commun. Conf. (GLOBECOM), 7-11 Dec. 2021, Madrid, Spain (국제 학회)*.
- K. Lee, J. Choi, D. K. Kim, J. Park. "Hierarchical Information Accessibility in Downlink MIMO Systems". *IEEE Global Commun. Conf. (GLOBECOM), 7-11 Dec. 2021, Madrid, Spain (국제 학회)*.
- Y. Choi, J. Choi, and B. L. Evans. "Coordinated Multicell Beamforming and Power Allocation for Massive MIMO with low-resolution ADC/DAC". *IEEE Int. Conf. on Commun. (ICC), 14-23 Jun. 2021, Montreal (국제 학회)*.
- J. Park, J. Choi, N. Lee, W. Shin, and H. V. Poor. "Sum Spectral Efficiency Optimization for Rate Splitting in Downlink MU-MISO: A Generalized Power Iteration Approach". *IEEE Wireless Commun. and Networking Conf. (WCNC) Workshops, 29 Mar-1 Apr. 2021, Nanjing, China (국제 학회)*.
- 이강욱, 최진석, 김동구, 박정훈. "하향링크 다중 안테나 시스템의 계층적 정보 접근성에 관한 연구". *한국통신학회 추계종합학술대회 (KICS), Nov. 2021, 경주 (국내 학회)*.
- 오민택, 최진석. "장치 간 보안 통신을 위한 프리코딩과 스케줄링의 공동 설계". *통신 정보 합동 학술대회 (JCCI), Apr. 28-30, 2021, 부산 (국내 학회)*.

**연도 표기 없음**

- S. Park, E. Choi, and J. Choi\*. "송신 빔패턴 레이더 성능 제약 하에서의 통합 센싱 및 통신 빔포밍 기법". *The Journal of Korean Institute of Communications and Information Sciences (국내 학술지, 게재 승인: 누리집 표기 accepted, 연도 표기 없음)*.
- E. Choi, and J. Choi\*. "제한된 채널 정보를 활용한 다중 도청 환경에서의 보안 프리코딩 최적화". *The Journal of Korean Institute of Communications and Information Sciences (국내 학술지, 게재 승인: 누리집 표기 accepted, 연도 표기 없음)*.
- H. Lee, et al. "수중 음향 통신을 위한 채널 모델링과 송수신 기법 연구 동향". *The Journal of Korean Institute of Communications and Information Sciences (국내 학술지, 게재 승인: 누리집 표기 accepted, 연도 표기 없음)*.

## 연구 과제

누리집 Projects 페이지의 과제 가운데 진행 중(ONGOING) 10건과 종료(COMPLETED) 7건이다. 과제 이름·기간·사업명·지원기관은 누리집 표기 그대로다. 이 목록은 교수의 과제 목록이라, 교수가 KAIST에 부임한 2023년 2월 전에 UNIST에서 시작한 과제도 들어 있다(지원기관이 울산과학기술원(UNIST)인 신임교수 정착과제 등).[^projects][^prof]

- 수신신호 품질 향상을 위한 다이버시티 및 간섭신호 제거 연구 (상태 Ongoing; 기간 May 2026 - Nov. 2026; 사업 통신신호연구회 위탁과제; 지원 한국통신학회 (KICS))
- AI-Native 응용서비스 지원 AI-Native 무선 인터페이스 기술 개발 (상태 Ongoing; 기간 Apr. 2026 - Dec. 2028; 사업 차세대네트워크(6G)산업기술개발; 지원 정보통신기획평가원 (IITP))
- 퓨처 모빌리티 서비스를 위한 AI 통신 센싱 융합 핵심기술 개발 (상태 Ongoing; 기간 Jul. 2023 - Dec. 2030; 사업 대학ICT 연구센터 (ITRC); 지원 정보통신기획평가원 (IITP))
- 6G Wireless Communications System Development (상태 Ongoing; 기간 Mar. 2024 - Feb. 2028; 사업 KAIST-Samsung Electronics DS Research Fund; 지원 Samsung Electronics)
- Upper-mid Band를 지원하는 Cloud virtualized RAN(vRAN) 시스템 기술 개발 (상태 Ongoing; 기간 Jan. 2025 - Dec. 2028; 사업 방송통신산업기술개발 (6G R&D); 지원 정보통신기획평가원 (IITP))
- 지능형 보안 수중 통신 (InSeCT) 특화연구실 (상태 Ongoing; 기간 Dec. 2022 - Dec. 2028; 사업 국방특화연구실; 지원 국방기술진흥연구소 (KRIT))
- 이종 위성군 지원을 위한 통신 아키텍처 설계 (상태 Ongoing; 기간 Dec. 2022 - Dec. 2028; 사업 국방특화연구센터; 지원 국방기술진흥연구소 (KRIT))
- 차세대 센싱 V2X 기반 자율주행을 위한 저전력 고신뢰 센싱 및 통신 통합 시스템 개발 (상태 Ongoing; 기간 Sep. 2025 - Aug. 2028; 사업 국가아젠다과제; 지원 한국연구재단 (NRF))
- Ultra-low Power and Ultra-Wideband Communication System Development (상태 Ongoing; 기간 Sep. 2024 - Feb. 2027; 사업 KAIST-NYU Open Call; 지원 KAIST, NYU)
- 양자화 된 대규모 다중 안테나 저해상 데이터 컨버터 및 안테나 전력 소모를 고려한 멀티셀 빔포밍 (상태 Ongoing; 기간 Feb. 2023 - Dec. 2026; 사업 신임교수 정착과제; 지원 한국과학기술원 (KAIST))
- DC Microgrid를 위한 복수의 기능을 갖는 고신뢰성 전력변환시스템 (상태 Completed; 기간 Jun. 2023 - Feb. 2026; 사업 기초연구실 (BRL); 지원 한국연구재단 (NRF))
- 차세대 저궤도 위성통신을 위한 3GPP-NTN 표준 기반의 채널 특성 및 이에 최적화된 송수신 방법 조사 (상태 Completed; 기간 May 2025 - Nov. 2025; 사업 ETRI 용역사업; 지원 ETRI)
- 밀리미터파 MIMO OFDM 레이다-통신의 신호 생성기 및 빔포밍 알고리즘 연구 (상태 Completed; 기간 Oct. 2023 - Oct. 2025; 사업 KAIST-LG Research Center; 지원 LG Electronics)
- 사물인터넷을 위한 고급 무선 통신 시스템 연구 (상태 Completed; 기간 Mar. 2021 - Feb. 2025; 사업 우수신진연구; 지원 한국연구재단 (NRF))
- 양자화 된 대규모 다중 안테나 시스템의 조정 된 빔포밍: 안테나 별 제약 (상태 Completed; 기간 Nov. 2020 - Oct. 2023; 사업 신임교수 정착과제; 지원 울산과학기술원 (UNIST))
- 자가충전형 초소형 전국단위 위치추적 시스템 원천기술 개발 (상태 Completed; 기간 Jan. 2021 - Dec. 2022; 사업 대학ICT 연구센터 (ITRC); 지원 정보통신기획평가원 (IITP))
- 원거리 고속이동체 통신신호 수신을 위한 추적안테나 기술 연구 (상태 Completed; 기간 Mar. 2022 - Nov. 2022; 사업 통신신호연구회 위탁 연구과제; 지원 한국통신학회 (KICS))

## 수상

누리집 Professor 페이지 HONORS & CERTIFICATES 칸의 2022–2026년 항목 8건, 첫 화면 소식의 수상·선정 글 4건, Conference·Domestic 페이지가 논문 항목 끝에 Best Paper Award로 표시한 6건이다. 첫 화면 소식의 2026년 2월 수상 글 2건은 Professor 페이지의 같은 이름 항목과 한 줄로 두었다. 날짜는 Professor 페이지 항목의 연도(학기), 소식 글의 연월, 학회 날짜다. 2023년 2월 전의 수상(2022년 항목 3건)은 교수가 UNIST에 있던 때의 일이다.[^prof][^home][^conf][^domestic]

- 2026 · KAIST 2025 Future-Leading Technology Research Achievement Award, KAIST (Joint and Robust Beamforming Framework for Integrated Sensing and Communication Systems)
- 2026 · KAIST 2025 Best Lecture Award, KAIST
- 2025-12 · Seokjun Park's in ITRC project research team has been selected as an Outstanding Creative Autonomous Project Team, ITRC
- 2025-12 · Sungyu Kim, has won the Graduate Excellence Scholarship in Science and Engineering from Korea Student Aid Foundation (KOSAF) 한국장학재단 - 석사우수장학금(이공계).
- 2025-11 · 한국통신학회 추계종합학술대회 (KICS) Best Paper Award: 바이스태틱 센싱-통신 통합 시스템을 위한 트랜스포머 활용 예측 빔포밍 (박석준, 최진석)
- 2025-09 · Seokjun Park, has been selected as IPESK Next-generation Engineering Researcher (IPESK차세대 공학(연구)자) from the Institute for Promotion of Engineering and Science of Korea (IPESK)
- 2025-07 · Seokjun Park, has won the Presidential Science Scholarship from the Korea Student Aid Foundation
- Fall 2024 · KAIST Electrical Engineering Best Lecture Award (EE50022 Communications Theory), EE KAIST
- 2024-11 · 한국통신학회 추계종합학술대회 (KICS) Best Paper Award: SCNR 및 MSE 값 조정을 통한 센싱-통신 통합 시스템 (박석준, 최은성, 최진석)
- 2024-10 · ICTC 2024 Best Paper Award: Joint Precoding and Antenna Selection for Sum Spectral Efficiency Maximization (S. Bae, J. Choi)
- 2024 · KICS Haedong Best Paper Award (한국통신학회 해동우수논문 우수상), KICS
- 2024 · IEEE Seoul Section Student Paper Contest Silver Award (Mintaek Oh, PhD Student), IEEE
- 2024-01 · 한국통신학회 동계종합학술대회 (KICS) Best Paper Award: 저지연 보안 통신 시스템을 위한 전송 기법 설계 (오민택, 박정훈, 최진석)
- 2023 · KAIST Excellence in Technological Innovation Award, KAIST
- 2023 · IEEE ComSoc AP Outstanding Young Researcher Award, IEEE (For Contribution to Energy-Efficient Communications)
- 2022-11 · 한국통신학회 추계종합학술대회 (KICS) Best Paper Award: 딥러닝을 활용한 블라인드 칼만 필터 설계 (오민택, 최진석, 박정훈)
- 2022-06 · 한국통신학회 하계종합학술대회 (KICS) Best Paper Award: 보안 커뮤니케이션을 위한 프리코딩 및 인공 노이즈의 공동 디자인 프레임워크 (최은성, 오민택, 최진석)
- 2022 · IEEE Exemplary Reviewer of Wireless Communications Letters, IEEE

## 소식

첫 화면 NEWS의 2025년 7월–2026년 8월 글 가운데 논문의 게재 승인(accepted)을 알리는 10건이다(수상·선정 글은 위 「수상」 절에 있다). 날짜는 글머리의 연월이고 문구는 누리집 표기 그대로다.[^home]

- 2026-08 · Congratulations! Our paper (1st: Mintaek Oh), "Scalable Beamforming Design for Multi-RIS-Aided MU-MIMO Systems with Imperfect CSIT," has been accepted to IEEE TWC
- 2026-08 · Congratulations! Our paper (1st: Mingyu Park), "Peak Isolation and Compressive Recovery: A CS-Based PAPR Reduction Framework for OFDM," has been accepted to IEEE Globecom 2027
- 2026-06 · Congratulations! Our paper (1st: Mintaek Oh), "Hybrid Precoding Revisited: Low-Dimensional Subspace Perspective for MU-MIMO Systems," has been accepted to IEEE TVT
- 2026-06 · Congratulations! Our paper (1st: Junwon Lee), "Low-Earth Orbit Satellite Network Analysis with Random LOS and NLOS Channels," has been accepted to IEEE TVT
- 2026-05 · Congratulations! Our paper (1st: Seunghyeong Yoo, Jaehyun Kim), "Full-Duplex MU-MIMO Systems with Coarse Quantization: How Many Bits Do We Need?," has been accepted to IEEE TCOM
- 2026-04 · Congratulations! Our paper (1st: Jiwon Sung), "Power-Constrained and Quantized MIMO-RSMA Systems with Imperfect CSIT: Joint Precoding, Antenna Selection, and Power Control," has been accepted to IEEE TWC
- 2026-04 · Congratulations! Our paper (1st: Jun Kang), "Channel Estimation for One-Bit Quantized MIMO Systems: Dithering-Aided Approach," has been accepted to IEEE WCL
- 2025-11 · Congratulations! Our paper (1st: Mintaek Oh), "Generalized Power Iteration-based Precoding with Low-Complexity Matrix Inversion Approaches for Massive MIMO Systems," has been accepted to IEEE TVT
- 2025-09 · Congratulations! Our paper (1st: Soomin Bae), "Joint Secure Max-Min Fairness Precoding and Antenna Selection under Coarse Quantization," has been accepted to IEEE TVT
- 2025-09 · Congratulations! Our paper (1st: Jiwon Sung), "A New Interpretation of the Time-Interleaved ADC Mismatch Problem: A Tracking-Based Hybrid Calibration Approach," has been accepted to IEEE SPL

## 연락과 위치

- 교수 연구실: KAIST Bldg. N1, Rm. 615(카이스트 IT융합빌딩 (N1) 615호)[^prof][^ee]
- 학생 연구실: KAIST Bldg. N1, Rm. 618[^researchers]
- 교수 연락처(학과 교수 소개 표기): 7473[^ee]
- 교수 이메일: jinseok@kaist.ac.kr[^home][^ee]
[^p1]: S. Yoo 외, J. Choi, IEEE Transactions on Communications 74, 9742-9757 (2026). <https://doi.org/10.1109/tcomm.2026.3698918> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J. Sung, S. Park, J. Choi, IEEE Transactions on Wireless Communications 25, 17634-17648 (2026). <https://doi.org/10.1109/twc.2026.3689604> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Kang, J. Choi, IEEE Wireless Communications Letters 15, 2604-2608 (2026). <https://doi.org/10.1109/lwc.2026.3682511> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: M. Oh, S. Yoo, N. Lee, J. Choi, IEEE Transactions on Vehicular Technology 75, 11908-11913 (2026). <https://doi.org/10.1109/tvt.2025.3644169> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. Choi, J. Park, N. Lee, A. Alkhateeb, IEEE Transactions on Wireless Communications 23, 17602-17618 (2024). <https://doi.org/10.1109/twc.2024.3454987> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: J. Lee 외, J. Choi, IEEE Transactions on Vehicular Technology 75, 23279-23292 (2026). <https://doi.org/10.1109/tvt.2026.3698332> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: S. Kim, E. Choi, M. Oh, J. Choi, IEEE Transactions on Vehicular Technology 74, 8390-8395 (2025). <https://doi.org/10.1109/tvt.2025.3525836> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: Y. Cho, J. Choi, B. L. Evans, IEEE Transactions on Vehicular Technology 73, 11680-11693 (2024). <https://doi.org/10.1109/tvt.2024.3381757> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 연구실 누리집 첫 화면 <https://sic-x.kaist.ac.kr/> (SIC-X LAB, ABOUT US, NEWS 2025년 7월–2026년 8월, 2026-10-23 열람)
[^research]: 연구실 누리집 Research Areas 페이지 <https://sic-x.kaist.ac.kr/research> (MIMO 1–4, AI/ML 1–3, 2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <https://sic-x.kaist.ac.kr/professor> (SHORT BIO, EDUCATION, PROFESSIONAL EXPERIENCE, HONORS & CERTIFICATES, PROFESSIONAL/COMMUNITY SERVICE, 2026-10-23 열람)
[^researchers]: 연구실 누리집 Researchers 페이지 <https://sic-x.kaist.ac.kr/researchers> (PhD STUDENT, MS STUDENT, INTERN, INDIVIDUAL RESEARCH, ALUMNI, 2026-10-23 열람)
[^teaching]: 연구실 누리집 Teaching 페이지 <https://sic-x.kaist.ac.kr/teaching> (GRADUATE COURCES, UNDERGRADUATE COURSES, 2026-10-23 열람)
[^projects]: 연구실 누리집 Projects 페이지 <https://sic-x.kaist.ac.kr/projects> (ONGOING, COMPLETED, 2026-10-23 열람)
[^journal]: 연구실 누리집 Publications > Journal 페이지 <https://sic-x.kaist.ac.kr/publications/journal> ([PUBLISHED/ACCEPTED] 1–44번, 2026-10-23 열람)
[^conf]: 연구실 누리집 Publications > Conference 페이지 <https://sic-x.kaist.ac.kr/publications/conference> (C1–C42, 2026-10-23 열람)
[^domestic]: 연구실 누리집 Publications > Domestic 페이지 <https://sic-x.kaist.ac.kr/publications/domestic> (JOURNAL DJ1–DJ3, CONFERENCE DC1–DC34, 2026-10-23 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(최진석) <https://ee.kaist.ac.kr/professor/%ec%b5%9c%ec%a7%84%ec%84%9d/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 학위, 2026-10-23 열람)
[^gst]: KAIST 안보과학기술대학원 교수 명단 5쪽 <https://gst.kaist.ac.kr/member/faculty/?page=5> (최진석 항목의 소속학과, 세부 연구 분야, 연구실, 2026-10-23 열람)

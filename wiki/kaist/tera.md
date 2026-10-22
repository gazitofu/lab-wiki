# 테라바이트 인터커넥션 및 패키지 연구실 (TERALAB, Terabyte Interconnection and Package Laboratory)

**KAIST 전기및전자공학부 · 김정호 교수**

- 분야: 고대역폭 메모리(HBM)와 2.5D/3D 반도체 패키지의 신호·전력·열 설계, 인공지능 기반 패키지·인터커넥트 설계, HBM 기반 근메모리 계산 구조, 전자파 적합성, 무선 전력 전송
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 전자파 적합성·신호 무결성[^home][^sipi][^p2], 첨단 반도체 패키징[^pkg][^p1][^p2], 열전달·열관리[^home][^p1], 강화학습[^aisipi][^p3][^p5], 메모리 내 연산[^nmc][^p7], AI 반도체·가속기[^nmc][^home], 무선 전력 전송[^sipi]
- 홈페이지: <https://tera.kaist.ac.kr/>
- 근거와 출처: [테라바이트 인터커넥션 및 패키지 연구실 근거 페이지](tera-sources.md)

> 여러 칩을 한 패키지 안에 쌓고 이어 붙이는 반도체 패키지에서 신호·전원·열이 제대로 전달되도록 설계하는 연구실이다. 인공지능 반도체에 쓰이는 고대역폭 메모리(HBM)의 인터포저·관통 전극 설계와 차세대 HBM 구조를 연구하고, 이 설계를 강화학습과 생성 모델 같은 인공지능으로 자동화하는 방법을 개발한다.[^home][^pkg][^aisipi]

## 무엇을 연구하나

연구실 누리집은 연구의 핵심 분야를 신호 무결성(SI, 칩과 기판 사이 배선에서 신호가 일그러지지 않고 전달되는 정도), 전력 무결성(PI, 칩에 공급되는 전원 전압이 흔들리지 않는 정도), 열 무결성(TI, 칩과 패키지의 온도가 성능을 해치지 않도록 낮고 고르게 유지되는 정도), 전자파 간섭(EMI), 인공지능(AI)의 다섯 가지로 적는다.[^home] 전기및전자공학부 교수 소개는 교수의 주요 연구를 Signal Integrity, EMI/EMC, Interconnection, SiP/PCB Design으로 적는다.[^eeprof]

연구의 중심 대상은 고대역폭 메모리(HBM, DRAM 칩 여러 장을 수직으로 쌓아 수많은 입출력 통로로 데이터를 빠르게 주고받게 만든 메모리)다. Research 페이지는 HBM이 실리콘 관통 전극(TSV, 실리콘 칩을 위아래로 뚫어 쌓은 칩끼리 잇는 수직 배선)과 미세 피치 인터포저(여러 칩을 나란히 올려 그 사이를 촘촘한 배선으로 잇는 중간 기판) 기술로 만든 3차원 적층 메모리이며, 인터포저 위에 수천 개의 입출력 채널을 깔아 초당 테라바이트급 대역폭을 낸다고 설명한다. 채널 성능이 인터포저에서 주로 정해지므로 인터포저의 신호·전력 무결성 설계와 분석을 먼저 꼼꼼히 해야 전체 시스템 성능을 보장할 수 있다고 적는다.[^pkg] 연구실의 첨단 패키지 그룹은 HBM용 실리콘 인터포저의 메모리 채널과 고속 직렬 링크를 설계·분석하고, TSV와 재배선층(RDL, 칩 위에 덧입혀 배선 위치를 다시 잡는 얇은 배선층) 비아를 포함한 전력 분배망(PDN, 전원을 칩 곳곳에 나눠 보내는 배선망)을 메인보드부터 칩까지 계층적으로 분석한다.[^pkg]

둘째 축은 이 설계를 인공지능으로 빠르고 정확하게 하는 일이다. Research 페이지는 2.5D/3D 집적회로(여러 칩을 인터포저 위에 나란히 놓거나 위로 쌓아 하나로 묶은 회로) 설계가 복잡해지고 출시 기간은 짧아져, 시간 효율이 높고 정확한 최적 설계가 필요하다고 설명한다. 기계학습 기반 SI/PI 설계 그룹은 심층 신경망(DNN, 여러 층의 인공 신경으로 입력과 출력 사이의 관계를 배우는 모델)으로 아이 다이어그램(디지털 신호 파형을 겹쳐 그려 신호가 얼마나 깨끗한지 보는 그림)과 전원·접지 잡음, TSV 모델을 기존 전자기·회로 모의실험보다 적은 시간과 비용으로 추정하고, 강화학습(시행착오와 보상으로 가장 좋은 선택을 배우는 기계학습 방법)으로 목표 사양을 만족하는 배치 설계 지침을 배우게 한다.[^aisipi] 첫 화면은 생성 모델(학습한 자료와 비슷한 새 자료를 만들어 내는 인공지능 모델)로 아이 다이어그램을 추정하거나 TSV 배열 배치를 찾는 연구, 설명 가능한 강화학습으로 디커플링 커패시터(전원 잡음을 줄이려 전원선과 접지 사이에 붙이는 커패시터) 배치를 정하는 연구를 함께 소개한다.[^home]

셋째 축은 HBM 안이나 가까이에서 계산하는 컴퓨터 구조다. Research 페이지는 인공지능 계산 수요가 늘면서 가속기의 코어 수가 늘어 메모리 대역폭이 모자라고 배선 에너지가 커지는 문제를 들고, 처리 장치를 메모리와 함께 묶는 메모리 내 처리(PIM, Processing-In-Memory) 구조를 HBM 같은 3차원 적층 메모리로 구현할 수 있다고 설명한다. 연구실의 AI 하드웨어 그룹은 신호·전력 무결성을 고려해 PIM-HBM의 구조와 인터커넥션을 최적화하고, ReRAM 교차 배열(저항이 바뀌는 메모리 소자를 격자 모양으로 엮어 벡터-행렬 곱셈을 바로 계산하는 배열)로 만든 뉴로모픽 칩(신경망 계산을 흉내 내는 칩)의 배열 크기와 잡음 문제를 분석해 설계 지침을 낸다.[^nmc] 첫 화면은 근메모리 계산(NMC, 메모리 바로 옆에 계산 장치를 두는 방식) HBM, 쌍둥이 탑(Twin Tower) HBM, 대형 언어 모델을 위한 L3 캐시 내장 GPU-HBM 인터포저, 생성형 인공지능용 3차원 적층 NPU-SoC, 실리콘 브리지를 쓴 대형 칩렛(기능별로 나눠 만든 작은 칩) 패키지, 웨이퍼 한 장 크기 칩의 계층적 PDN 연구를 그림과 함께 소개한다.[^home]

연구실은 HBM의 발전 방향도 제시한다. Research 페이지는 연구실이 제안한 차세대 HBM3·4·5 로드맵에서 나선형 TSV, 작은 신호 진폭 인터페이스, 적층 DRAM의 부하를 보완하는 버퍼 층, 로직 층의 PIM 구조, 등화기와 전압 조정기를 넣은 능동 인터포저, 미세 유로·TSV를 쓰는 액체 냉각이 도입될 것으로 내다본다. 또 3차원 집적회로의 적층 수가 약 2년마다 두 배가 된다는 관찰을 교수의 이름을 따 「Kim's Law」로 소개하고, 교수가 2017년 신문 기사로 처음 발표했다고 적는다.[^roadmap] 첫 화면에는 2025년 HBM 로드맵, 2026년 HBF 워크로드와 로드맵, HBM·HBF·HBS의 미래를 다룬 자료가 올라 있다.[^home]

대표 논문으로 보면 연구는 세 갈래다. 첫째, HBM 모듈의 냉각 구조와 유리 인터포저 같은 패키지의 신호·전력·열 설계다(대표 논문 1, 2).[^p1][^p2] 둘째, 강화학습·트랜스포머·그래프 학습·생성적 적대 신경망으로 디커플링 커패시터 배치, 핀 배치, 아이 다이어그램 추정을 자동화하는 설계다(대표 논문 3, 4, 5, 6).[^p3][^p4][^p5][^p6] 셋째, HBM 로직 층에 처리 장치를 넣는 PIM-HBM과 멤리스터 교차 배열 뉴로모픽 시스템의 신호 무결성이다(대표 논문 7, 8).[^p7][^p8]

## 주요 연구 주제

### 1. HBM과 2.5D/3D 패키지의 신호·전력·열 설계

HBM용 실리콘 인터포저의 메모리 채널과 고속 직렬 링크, TSV와 재배선층 비아를 포함한 전력 분배망을 설계·분석한다.[^pkg] 다른 패키지 형태도 다룬다. 유기·유리 기판과 재배선층 공정으로 칩을 옆과 위로 촘촘히 잇는 팬아웃 웨이퍼 레벨 패키지(FoWLP)의 배선과 전원망, 실리콘보다 싸고 고주파 손실이 낮은 유리 기판을 인터포저로 쓰는 유리 인터포저와 그 관통 전극(TGV)의 잡음 결합·차폐, 시험 장비가 칩의 신호·전원 전달에 영향을 주지 않도록 하는 시험용 인터포저와 소켓 설계가 있다.[^pkg] 3D X-Point 메모리 배열의 스니크 전류(sneak current, 원하지 않는 경로로 돌아 흐르는 전류)와 누화(옆 배선의 신호가 새어 들어오는 잡음) 같은 신호 무결성 문제도 분석한다.[^pkg] HBM 모듈 안으로 유체를 돌리는 내장 냉각 구조와 열을 옆으로 퍼뜨리는 열 전송선을 함께 써서 온도를 낮추고 신호 품질을 높인 연구,[^p1] 유리 인터포저에서 신호 TGV 사이 잡음 결합을 측정하고 차폐 구조를 낸 연구가 있다.[^p2] 대표 논문 1, 2.

### 2. 인공지능으로 하는 신호·전력 무결성 설계

전자기·회로 모의실험 대신 심층 신경망으로 아이 다이어그램과 전원 잡음을 추정하고, 강화학습으로 디커플링 커패시터 배치 같은 설계를 최적화한다.[^aisipi] 트랜스포머 신경망(입력 사이의 관계를 어텐션으로 계산하는 신경망 구조) 기반 강화학습으로 HBM 전력 분배망의 디커플링 커패시터 배치를 정했고,[^p3] 적은 학습 자료로도 하드웨어 맥락을 배우는 트랜스포머 구조 DevFormer를 같은 배치 문제에 적용했다.[^p4] 핀을 그래프로 나타내 학습한 강화학습으로 마이크로범프(칩과 기판을 잇는 아주 작은 돌기 모양 접점) 패키지의 핀 배치를 최적화했고,[^p5] 생성적 적대 신경망(GAN, 진짜 같은 자료를 만드는 신경망과 진짜·가짜를 가리는 신경망을 경쟁시켜 학습하는 모델)으로 전원 잡음이 겹친 고속 채널의 아이 다이어그램을 빠르게 추정했다.[^p6] 최근 논문 목록에는 칩렛 배치·배선 최적화, 다층 전력 분배망의 임피던스를 추정하는 트랜스포머 모델, 대형 언어 모델로 디커플링 커패시터 배치를 최적화하는 연구도 있다.[^pubs] 대표 논문 3, 4, 5, 6.

### 3. 근메모리 계산과 AI 하드웨어 구조

HBM의 로직 층에 처리 장치를 넣는 PIM-HBM을 신호 무결성과 시스템 성능을 함께 따져 설계했고,[^p7] 멤리스터(걸린 전압의 이력에 따라 저항이 바뀌어 그 값을 기억하는 소자) 교차 배열로 심층 신경망을 계산하는 뉴로모픽 시스템에서 배선 잡음과 소자 비선형성이 계산 정확도에 주는 영향을 분석했다.[^p8] Research 페이지는 PIM 코어를 늘리면 로직 다이 면적이 더 필요하고, 인터포저 채널이 길어져 호스트 프로세서가 쓰는 메모리 대역폭이 줄어들므로, PIM-HBM 로직 다이와 인터포저 채널을 함께 최적화해야 한다고 설명한다.[^nmc] 최근 논문 목록에는 3차원 근메모리 계산 HBM 구조, SRAM 브리지를 넣은 GPU-HBM 구조, 여러 HBM을 잇는 네트워크 스위치와 메모리 풀링 구조 연구도 있다.[^pubs] 대표 논문 7, 8.

### 4. 무선 전력 전송과 회로

Research 페이지는 자동차 전장 시스템을 위해 신호·전력 무결성 문제에 강한 아날로그-디지털 변환기(ADC) 같은 아날로그 칩을 설계하고, 자동차 충전에 쓰일 무선 전력 전송 시스템의 자기장이 회로 성능에 주는 영향을 분석한다고 적는다. 프로세서와 같은 칩에 넣는 전압 조정기(IVR)를 실리콘 인터포저의 능동 영역에 CMOS 공정으로 구현하는 일과, 무선 전력 전송용 풀브리지 정류기·LDO(입력과 출력의 전압 차이가 작아도 동작하는 선형 전압 조정기)·DC/DC 변환기 같은 CMOS 회로의 설계·측정도 소개한다.[^sipi] 연구교수 한 명의 연구 분야도 무선 전력 전송, 신호·전력 무결성, 전자파 적합성, 전기차로 적혀 있다.[^rprof]

## 대표 논문

김정호 교수가 저자인 랩 Publications 목록의 2021–2026년 논문 가운데 초록을 확인할 수 있는 여덟 편을 세 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2022 | [Thermal and Signal Integrity Co-Design and Verification of Embedded Cooling Structure With Thermal Transmission Line for High Bandwidth Memory Module](https://doi.org/10.1109/tcpmt.2022.3201673) · IEEE Transactions on Components, Packaging and Manufacturing Technology | HBM 모듈의 열 무결성과 신호 무결성을 함께 높이려고, 열 저항을 낮추는 내장 냉각 구조(ECS)와 열을 수평 방향으로 옮겨 온도 분포를 고르게 하는 열 전송선(TTL)을 묶은 계층형 냉각 구조 ECS-TTL을 제안했다. ECS는 계산 모듈 부품 안으로 유체를 돌려 칩을 식힌다. 3차원 전산 유체 해석으로 모듈의 최고 온도와 온도 균일도를 평가하고, 그 온도 분포를 넣은 3차원 전자기 해석으로 실리콘 인터포저·TSV 채널·3차원 클럭 분배망의 아이 다이어그램과 스큐(신호가 도착하는 시각의 어긋남)를 평가했다. 기존 냉각 구조보다 온도가 낮고 고르게 분포했고 아이 다이어그램과 스큐도 나아졌다. | 1저자 K. Son, 마지막 저자 김정호 (12명) |
| 2 | 2021 | [Measurement and Analysis of Through Glass Via Noise Coupling and Shielding Structures in a Glass Interposer](https://doi.org/10.1109/temc.2021.3059846) · IEEE Transactions on Electromagnetic Compatibility | 유리 인터포저에서 신호용 유리 관통 전극(TGV) 사이의 잡음 결합과 차폐 구조의 효과를 측정했다. 유리 인터포저 시험 기판을 만들어 신호 TGV 사이의 잡음 전달 함수를 재고 등가 회로 모델로 분석했다. 신호 TGV 간격, 접지된 차폐 TGV의 수, 접지 패드, 가드 링을 바꾼 차폐 구조를 제안해 20 GHz까지 주파수 영역 측정으로 확인했고, 이 구조로 5 GHz에서 잡음 전달 함수가 9.4 dB 줄었다. 1 GHz 클럭 신호의 시간 영역 모의실험에서 가드 링은 신호 TGV 간격이 300 μm, 900 μm일 때 결합 잡음을 각각 60.5%, 69.2% 줄였다. | 1저자 G. Park, 마지막 저자 김정호 (12명) |
| 3 | 2022 | [Transformer Network-Based Reinforcement Learning Method for Power Distribution Network (PDN) Optimization of High Bandwidth Memory (HBM)](https://doi.org/10.1109/tmtt.2022.3202221) · IEEE Transactions on Microwave Theory and Techniques | HBM 전력 분배망을 최적화하는 트랜스포머 신경망 기반 강화학습 방법을 제안했다. 여러 포트에서 본 PDN의 자기·전달 임피던스를 최대한 줄이는 디커플링 커패시터 배치를 찾는다. 어텐션 기반 트랜스포머가 배치 정책을 직접 나타내 방대한 배치 조합을 탐색하고, 측정 포트 위치 같은 맥락을 담는 임베딩 덕분에 같은 신경망을 다시 쓸 수 있어 최적화 시간이 줄었다. 무작위로 만든 자료로 학습해 학습 시간과 자료 비용을 줄였고, 추가 학습 없이 더 큰 문제에도 적용된다. 유전 알고리즘·무작위 탐색·이전 강화학습 방법과 비교해 최적화 성능, 계산 시간, 자료 효율에서 모두 앞섰다. | 1저자 H. Park, 마지막 저자 김정호 (12명) |
| 4 | 2023 | [DevFormer: A Symmetric Transformer for Context-Aware Device Placement](https://proceedings.mlr.press/v202/kim23h.html) · ICML 2023 | 하드웨어 설계 최적화 문제를 위한 트랜스포머 기반 구조 DevFormer를 내놓았다. 하드웨어 설계는 미리 모아 둔 학습 자료(오프라인 자료)가 적어 트랜스포머를 쓰기 어려웠는데, 상대 위치 임베딩과 행동 순서 대칭성 같은 강한 귀납 편향(모델에 미리 넣어 두는 가정)을 넣어 적은 자료로도 하드웨어 맥락을 잡게 했다. 디커플링 커패시터 배치 문제에 적용해 모의 하드웨어와 실제 하드웨어 모두에서 기존 최신 방법보다 성능이 좋았고 부품 수를 30% 넘게 줄였다. 다른 오프라인 맥락 학습 기반 조합 최적화 문제에서도 좋은 결과를 보였다. | 1저자 H. Kim, 5명 중 넷째 저자 김정호, 마지막 저자 J. Park |
| 5 | 2024 | [Pin-Opt: Graph Representation Learning for Large-Scale Pin Assignment Optimization of Microbumps Considering Signal and Power Integrity](https://doi.org/10.1109/tcpmt.2024.3381342) · IEEE Transactions on Components, Packaging and Manufacturing Technology | 마이크로범프 패키지에서 신호·전력 무결성 저하를 최소화하도록 핀 배치를 최적화하는 심층 강화학습 틀 Pin-opt를 제안했다. 기존 메타휴리스틱 방법(경험 규칙으로 좋은 해를 찾는 탐색 방법)은 정사각형 핀 배열에만 맞는 문제별 해를 냈지만, Pin-opt는 학습 중 핀을 그래프로 나타내 어떤 모양의 핀 배치와 핀 수가 아주 많은 문제에도 쓸 수 있는 재사용 가능한 해법을 만든다. 유전 알고리즘과 성능, 계산 비용, 재사용성, 확장성을 비교했고, HBM의 핀 배치에도 적용했다. | 1저자 J. Park, 마지막 저자 김정호 (12명) |
| 6 | 2025 | [Generative Adversarial Learning Based Power Noise Induced Eye Diagram Estimation Method for High-Speed Channel Design](https://doi.org/10.1109/temc.2025.3610342) · IEEE Transactions on Electromagnetic Compatibility | 전원 잡음이 겹친 고속 채널의 아이 다이어그램을 생성적 적대 신경망으로 추정하는 AGSI-GAN을 제안했다. 단일 비트 응답, 원단 누화, 동시 스위칭 잡음(여러 출력이 한꺼번에 바뀔 때 전원에 생기는 잡음)을 모듈처럼 묶어 그림으로 바꾸는 AGSI 틀을 U-Net 생성기의 조건 그림으로 넣어, 신호·전력 무결성이 얽힌 설계 상황에서도 아이 다이어그램을 정확하고 빠르게 추정한다. 학습한 AGSI-GAN은 전체 과도 해석 모의실험보다 실행 시간을 88.6% 줄이면서 누적 면적을 포함한 모든 아이 다이어그램 지표에서 평균 절대 백분율 오차가 3% 아래였다. | 1저자 J. Lee, 마지막 저자 김정호 (11명) |
| 7 | 2021 | [Signal Integrity and Computing Performance Analysis of a Processing-In-Memory of High Bandwidth Memory (PIM-HBM) Scheme](https://doi.org/10.1109/tcpmt.2021.3117071) · IEEE Transactions on Components, Packaging and Manufacturing Technology | HBM의 로직 층에 처리 장치를 넣어 남는 DRAM 대역폭을 쓰는 PIM-HBM 방식의 시스템 구조와 하드웨어 구조를 제안했다. DRAM 채널을 병렬화하고 고속 TSV 구조를 써서 PIM이 쓰는 DRAM 대역폭을 늘렸고, 배선이 짧아지고 정전용량을 줄인 채널 구조로 전체 에너지 소비를 줄였다. TSV와 실리콘 인터포저 채널을 신호 무결성을 고려해 설계·분석하고, SPICE 모의실험으로 배선 에너지와 지연을, 사이클 단위 구조 모의실험으로 시스템 성능을 평가했다. 메모리 사용이 많은 응용에서 기존 GPU-HBM보다 계산 성능이 평균 53%, 에너지 효율이 평균 10.4% 나아졌다. | 1저자 S. Kim, 마지막 저자 김정호 (12명) |
| 8 | 2021 | [Signal Integrity Modeling and Analysis of Large-Scale Memristor Crossbar Array in a High-Speed Neuromorphic System for Deep Neural Network](https://doi.org/10.1109/tcpmt.2021.3092740) · IEEE Transactions on Components, Packaging and Manufacturing Technology | 심층 신경망을 하드웨어로 계산하는 뉴로모픽 시스템의 대규모 멤리스터 교차 배열을 신호 무결성을 고려해 모델링·분석·평가했다. 멤리스터 교차 배열로 만든 하드웨어 신경망은 아날로그로 동작해 배선, 구동 회로, 비선형 메모리 소자 때문에 신뢰성 문제가 크다. 3차원 전자기 해석으로 칩 위 신호선과 전원·접지 망을 회로 변수로 모델링하고 멤리스터의 비선형 특성을 넣어 512×512 배열을 구성한 뒤, 부품 단계와 배열 전체 단계의 신호 무결성과 비선형성을 분석하고 심층 신경망 회귀로 검증했다. 입력 전압이 낮을수록 정확도에 미치는 영향은 멤리스터 비선형성보다 신호 무결성 쪽이 커졌고, 배선 크기에 따라 IR 강하(배선 저항으로 생기는 전압 강하)와 누화 사이에 맞바꿈 관계가 있음을 확인했다. | 1저자 T. Shin, 마지막 저자 김정호 (12명) |

## 교수와 전문 분야

김정호 교수는 KAIST 전기및전자공학부 교수다. 전기및전자공학부 교수 소개는 직위를 「KAIST교수 (IEEE 석학회원, KAIST ICT 석좌교수)」, 디비전을 Wave로 적고, 주요 연구분야를 AI & Machine Learning, Computer Architecture, Integrated Circuits & Semiconductor Systems로 적는다.[^eeprof] 연구실 교수 소개는 주요 연구 분야를 차세대 인공지능 반도체 HBM 설계와 인공지능 강화학습 기반 HBM 설계로 적고, 교수가 'Father of HBM'으로 널리 알려져 있다고 쓴다.[^prof]

연구실 교수 소개 페이지에 따르면 교수는 서울대학교 전기공학과(Electrical Engineering)에서 학사(1984)와 석사(1986)를, University of Michigan에서 박사(1993)를 받았다. Picometrix(미국) Research Engineer(1993–1994), 삼성전자 Memory DRAM Team Principal Engineer(1994–1996)를 거쳐 1996년부터 KAIST 전기및전자공학부 교수(Professor, KAIST Dept. of Electrical Engineering)다. KAIST에서 Department Chair(2011–2012), Dean at KAIST Office of Research(2017–2019), Chair Professor, KAIST ICT(2017–2020), Executive Vice President for Industry-Academic Cooperation(2021–2023)를 지냈고, 2024년부터 Head Professor, KAIST System Architect를 맡고 있다. 2016년부터 IEEE Fellow이고, IEEE Transactions on Electromagnetic Compatibility의 Associated Editor(2001–2016)와 IEEE WPTC(2014)·IEEE EDAPS(2015)·APEMC(2016, 2017) 학술대회 Chair를 지냈다. SK hynix의 3D Semiconductor Research Center Head(2012–2016), KAIST-Samsung Electronics Industry-University Cooperation Center Director(2018–), KAIST-Hanwha Defense AI Convergence Research Center Director(2018–2024)도 적혀 있다.[^prof] 같은 페이지는 Private Member of the 1st Presidential National AI Committee(2024–2025.09), Chair of the National AI Education Curriculum Committee(2025.03–), Chair of the Semiconductor Subcommittee, Strategic Economic Advisory Council, Ministry of Finance and Economy(2026.03–) 같은 정부 위원회 활동도 적는다.[^prof]

교수 소개 페이지는 교수가 국제 학술지와 IEEE 학술대회에 논문 732편을 냈고(2026년 3월 기준), 석·박사 졸업생 123명을 지도했으며 2026년 3월 기준 대학원생 24명이 연구실에 있다고 적는다. 졸업생은 삼성전자, SK하이닉스, NVIDIA, Google, Tesla, Qualcomm, Apple, Microsoft, Rambus와 학계로 진출했다고 쓴다. 100건이 넘는 산학협력 과제를 수행하며 연간 연구비가 100억 원(2025년 기준 삼성전자 75억 원, 인텔 30억 원)이라고 적고, Tesla·Qualcomm·Apple·Rambus·NVIDIA·Google, Georgia Tech, Missouri S&T, 싱가포르 DSO National Laboratories와 협력한다고 적는다.[^prof] 저서로 「Electrical Design of Through Silicon Via (TSV)」(Springer, 2014)와 「The Future of Engineering」(2021)이 있고, 2019년부터 조선일보에 「김정호의 AI 시대 전략」 칼럼을 쓰고 있다(2026년 1월 기준 71회).[^prof]

교수 소개 페이지의 Awards 칸은 KAIST Academic Award(2006), Industry-Academic Cooperation Award, Ministry of Education(2009), Technology Achievement Award, IEEE EMC Society(2010), KAIST International Cooperation Award(2010), Distinguished Lecture Award, IEEE EMC Society(2011), KAIST Research Grand Prize(2008, 2014), Sejong Book Award(Liberal Arts: The Future of Engineering, Ministry of Culture, Sports and Tourism, 2021)를 적고, 학생과 함께 받은 여러 국제 학술대회의 Best Paper Award가 모두 34건이라고 쓴다. 2022년 이후의 수상과 Excellent Teaching Award는 아래 「수상」 목록에 있다.[^prof]

논문으로 보면 KAIST에서 최근의 전문 분야는 세 갈래다. HBM과 유리 인터포저 같은 반도체 패키지의 신호·전력·열 설계(대표 논문 1, 2),[^p1][^p2] 강화학습·트랜스포머·생성 모델로 하는 신호·전력 무결성 설계 자동화(대표 논문 3, 4, 5, 6),[^p3][^p4][^p5][^p6] PIM-HBM과 뉴로모픽 하드웨어의 신호 무결성과 구조 설계(대표 논문 7, 8)다.[^p7][^p8]

## 응용 분야

연구의 주된 응용은 GPU·NPU 같은 인공지능 계산 장치와 HBM을 한 패키지에 묶는 인공지능 반도체·고성능 컴퓨팅이다. Research 페이지는 HBM 인터포저를 고성능 컴퓨팅 그래픽 모듈의 대역폭 병목을 푸는 핵심으로 보고, 팬아웃 웨이퍼 레벨 패키지를 모바일 응용 프로세서에, 3D X-Point 메모리 신호 무결성을 SSD·DIMM 같은 메모리 응용에 연결한다.[^pkg] 자동차 전장 아날로그 칩과 자동차 충전용 무선 전력 전송도 다룬다.[^sipi] 대표 논문으로는 HBM 모듈 냉각(대표 논문 1), HBM 전력 분배망 최적화(대표 논문 3), HBM 핀 배치(대표 논문 5), GPU-HBM보다 계산 성능을 높인 PIM-HBM(대표 논문 7)이 있다.[^p1][^p3][^p5][^p7]

Funded Projects 페이지는 2023년 과제로 SK Hynix, Samsung Electronics(2건), Hanwha System(2건), LG Electronics, KET(Electronics, EV 2건), National Research Foundation of Korea 과제를 학생 책임자와 함께 적는다.[^proj] Industry Collaboration Partners 페이지는 SK Hynix, Samsung Electronics, LG Electronics, Korea Electric Terminal, TODOC, Gigalane을, International Collaboration Partners 페이지는 Google, Apple, Tesla, NVIDIA, Rambus, Invecas, Ansys, GaTech Packaging Research Center, Missouri S&T, NARA Institute of Science and Technology를 적는다.[^partners] 첫 화면은 2024년 7월 Naver-Intel-KAIST AI Research Center 출범 워크숍과 2022년 1월 KAIST Cross-Generation Collaborative Lab 개소식을 알린다.[^home]

## 구성원

연구실 누리집 Members 메뉴의 연구교수 1명, 박사과정 10명, 석사과정 9명이다(Post Doc. Researcher 페이지는 비어 있다).[^rprof][^phd][^ms] 과정 칸의 괄호는 페이지가 적은 학년이고, 박사과정 한 명은 학생 대표(Student Representative)로 적혀 있다. 연구 주제와 이메일은 페이지 표기 그대로다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Jonghoon Kim | 연구교수 | WPT, SI, PI, EMI/EMC/EMF, Electric Vehicle | jonghoon@kaist.ac.kr |  |
| Seyoung Jo | 박사과정 (Ph.D 4) | SI, PI, EMC/EMI | seyoung.jo@kaist.ac.kr |  |
| Sungeun Lee | 박사과정 (Ph.D 3) | SI, PI, EMC/EMI | sungeun.lee@kaist.ac.kr |  |
| Jiwon Yoon | 박사과정 (Ph.D 3) | Signal Integrity Design and Analysis of Processing-in-Memory Architecture based on High Bandwidth Memory | jiwon.yoon@kaist.ac.kr | 5, 6 |
| Junghyun Lee | 박사과정 (Ph.D 3) | SI, PI, EMI/EMC | junghyunlee@kaist.ac.kr | 5, 6 |
| Haeseok Suh | 박사과정 (Ph.D. 2, Student Representative) | AI-based GPU-HBM Architecture Design Considering SI, PI, and AI Workload | haeseoksuh@kaist.ac.kr | 6 |
| Hyunjun An | 박사과정 (Ph.D. 2) | SI, PI, EMI/EMC | anhyunjun@kaist.ac.kr | 6 |
| Byeongmok Kim | 박사과정 (Ph.D 1) | SI, PI, EMI/EMC | byeongmok@kaist.ac.kr |  |
| Junho Park | 박사과정 (Ph.D 1) | SI, PI, EMI/EMC | parkjunho@kaist.ac.kr |  |
| Jaegeun Bae | 박사과정 (Ph.D 1) | SI, PI, EMI/EMC | jaegeunbae@kaist.ac.kr |  |
| Youngsu Yoon | 박사과정 (Ph.D 1) | SI, PI, EMI/EMC | youngsuyoon@kaist.ac.kr |  |
| Hyuni Lee | 석사과정 (M.S. 2) | SI, PI, AI System Architecture | hyuniee@kaist.ac.kr |  |
| Chaemin Yang | 석사과정 (M.S. 2) | SI, PI, EMI/EMC, AI | chaeminyang@kaist.ac.kr |  |
| Gwantaek Lee | 석사과정 (M.S. 2) | SI, PI, EMC/EMI, TI, AI | gwantaek@kaist.ac.kr |  |
| Seungjae Lee | 석사과정 (M.S. 2) | SI, PI, EMC/EMI | seungjae@kaist.ac.kr |  |
| Sangcheol Choi | 석사과정 (M.S. 1) | SI, PI, EMC/EMI | choisangcheol@kaist.ac.kr |  |
| Youngjun Seog | 석사과정 (M.S. 1) | SI, PI | youngjun.seog@kaist.ac.kr |  |
| Taehyun Kim | 석사과정 (M.S. 1) | SI, PI, EMC/EMI | taehyunkim@kaist.ac.kr |  |
| Hakyum Shin | 석사과정 (M.S. 1) | SI, PI, EMI, AI | shinhakyum@kaist.ac.kr |  |
| Yujeong Koh | 석사과정 (M.S. 1) | SI, PI, EMC/EMI | yujeongkoh@kaist.ac.kr |  |

## 졸업생

누리집 Alumni 페이지의 박사 졸업생 71명과 석사 졸업생 59명 전부다(페이지 표기 「Ph. D Alumni (71)」, 「M.S. Alumni (59)」). 졸업 연도는 박사 2001–2026년, 석사 1999–2026년이고, 소속(Affiliation)은 누리집 표기 그대로다. 소속 칸이 비어 있는 행은 비워 두었다. 박사 졸업생 Jonghoon Kim(2003)은 현재 연구교수로 올라 있다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Woonghwan Ryu | 박사 (2001) | CEO of Korea Venture Investment Corp. |
| Jongjoo Lee | 박사 (2002) | MEK |
| Heeseok Lee | 박사 (2002) | Samsung |
| Jonghoon Kim | 박사 (2003) | KAIST Teralab |
| Myunghee Sung | 박사 (2004) | Samsung |
| Hyungsoo Kim | 박사 (2005) | SK Hynix |
| Jun So Pak | 박사 (2005) | Samsung |
| Seungyoung Ahn | 박사 (2005) | Prof. at KAIST |
| Junwoo Lee | 박사 (2005) | Tesla |
| Seungyong Brian Baek | 박사 (2006) | Apple |
| Youchul Jung | 박사 (2006) | Apple |
| Junho Lee | 박사 (2006) | Microsoft |
| Jingook Kim | 박사 (2006) | Prof. at UNIST |
| Donggun Gam | 박사 (2006) | Qualcomm |
| Daehyun Chung | 박사 (2006) | Nvidia |
| Chunghyun Ryu | 박사 (2008) | Samsung |
| Jongbae Park | 박사 (2008) | Apple |
| Hyunjung Park | 박사 (2009) | Qualcomm |
| Jaemin Kim | 박사 (2010) | Apple |
| Jongjoo Shim | 박사 (2010) | Apple |
| Gawon Kim | 박사 (2010) | Google |
| Eakhwan Song | 박사 (2010) | Prof. at Kwangwoon Univ. |
| Jeonghyeon Cho | 박사 (2011) | Samsung |
| Woojin Lee | 박사 (2011) | SK Hynix |
| Changwook Yoon | 박사 (2010) | Apple |
| Yujeong Shim | 박사 (2011) | Google |
| Myunghoi Kim | 박사 (2012) | Prof. at Hankyong National Univ. |
| Minchul Shin | 박사 (2012) | SK Hynix |
| Chulsoon Hwang | 박사 (2012) | Prof. at Missouri S&T |
| Kyoungchoul Koo | 박사 (2012) | Apple |
| Jonghyun Cho | 박사 (2013) | Apple |
| Joohee Kim | 박사 (2013) | Rambus |
| Eunseok Song | 박사 (2014) | Samsung |
| Bumhee Bae | 박사 (2014) | Samsung |
| Heegon Kim | 박사 (2015) | Apple |
| Kiyeong Kim | 박사 (2015) | Apple |
| Sukjin Kim | 박사 (2016) | Samsung |
| Jonghoon Kim | 박사 (2017) | Samsung |
| Hongseok Kim | 박사 (2017) | CPS Tech, Inc. |
| Manho Lee | 박사 (2017) |  |
| Sunkyu Kong | 박사 (2018) | SK Hynix |
| Yeonje Cho | 박사 (2018) | Samsung Display |
| Chiuk Song | 박사 (2018) | Hyundai Mobis |
| Sumin Choi | 박사 (2018) | Google |
| Donghyun Kim | 박사 (2018) | Google |
| Jinwook Song | 박사 (2018) | Samsung |
| Youngwoo Kim | 박사 (2018) | Prof. at Sejong Univ. |
| Hyunsuk Jung | 박사 (2018) | Samsung |
| Jaemin Lim | 박사 (2019) | SK Hynix |
| Kyungjun Cho | 박사 (2019) | Google |
| Junyong Park | 박사 (2019) | Prof. at Kyunghee Univ |
| Hyesoo Kim | 박사 (2020) | SK Hynix |
| Seungtaek Jeong | 박사 (2020) | Google |
| Seongsoo Lee | 박사 (2021) | Tesla |
| Subin Kim | 박사 (2021) | Samsung |
| Shinyoung Park | 박사 (2021) | Rambus |
| Gapyeol Park | 박사 (2021) | Nvidia |
| Kyungjune Son | 박사 (2022) | Apple |
| Seokwoo Hong | 박사 (2022) | Samsung |
| Hyunwook Park | 박사 (2022) | Cisco |
| Daehwan Lho | 박사 (2023) | SK Hynix |
| Boogyo Sim | 박사 (2024) | Apple |
| Seongguk Kim | 박사 (2024) | Samsung |
| Taein Shin | 박사 (2024) | Groq |
| Hyungmin Kang | 박사 (2025) | SK Hynix |
| Keeyoung Son | 박사 (2024) | Qualcomm |
| Keunwoo Kim | 박사 (2025) | SK Hynix |
| Haeyeon Kim | 박사 (2025) | SK Hynix |
| Jihun Kim | 박사 (2026) | Samsung |
| Joonsang Park | 박사 (2026) | Apple |
| Seonguk Choi | 박사 (2026) | Samsung |
| Jaehoon Lee | 석사 (1999) | Prof. at Korea Univ. |
| Woopoung Kim | 석사 (2000) | Samsung DSA |
| Jaeyoung Ryu | 석사 (2000) | Samsung |
| Namhoon Kim | 석사 (2001) | OpenAI |
| Baekkyu Choi | 석사 (2001) | Apple |
| Taehong Kim | 석사 (2003) | Apple |
| Bongchel Park | 석사 (2003) | Kyungsung Univ. Legal Affairs Team |
| Suna Choi | 석사 (2004) | ETRI |
| Youngwon Kim | 석사 (2007) | Samsung |
| Jiwang Lee | 석사 (2007) | Nvidia |
| Myunghyun Ha | 석사 (2007) | Apple |
| Hyein Lee | 석사 (2008) | Samsung CNT Legal Affairs Team |
| Jiwoon Park | 석사 (2008) | Samsung |
| Jeongsik Yoo | 석사 (2004) | Samsung |
| Jiwoo Pak | 석사 (2009) | Cadence |
| Taigon Song | 석사 (2009) | Prof. at Kyungpook National Univ. |
| Sangrok Lee | 석사 (2010) | Korea Aerospace Research Institute |
| Kihyun Yoon | 석사 (2010) | Apple |
| Woojin Ahn | 석사 (2010) | Todoc |
| Hajin Sung | 석사 (2011) | MKE |
| Dayoung Kim | 석사 (2012) | Univ. of N.C |
| Changhyun Cho | 석사 (2013) | Samsung |
| Hyunsuk Lee | 석사 (2015) |  |
| Eunjung Lee | 석사 (2015) | Samsung |
| Yonghwan Kwack | 석사 (2015) | LG Electronics |
| Minkang Moon | 석사 (2015) | ADD |
| Hyunwoo Shim | 석사 (2016) | Hyundai Mobis |
| Insu Hwang | 석사 (2016) | ADD |
| Jihye Kim | 석사 (2016) | Ministry of Science and ICT, ROK. |
| Kibum Yoon | 석사 (2016) | ADD |
| Yeseul Jeon | 석사 (2017) | Post Doc. at MIT |
| Huijin Song | 석사 (2018) |  |
| Gyeyong Park | 석사 (2018) | Ph.D at KAIST |
| Kyunghwan Song | 석사 (2018) | Samsung |
| Mumpy Das | 석사 (2019) | Ph. D at University of Twente |
| Gaurau Kumar | 석사 (2020) |  |
| Intae Hwang | 석사 (2021) | SK Hynix |
| Kyubong Kong | 석사 (2021) | Nvidia |
| Minsu Kim | 석사 (2022) | Ph.D at KAIST |
| Hwijo Jeong | 석사 (2023) | SK Hynix |
| Dongyoon Ka | 석사 (2023) | SK Hynix |
| Donghyun Kim | 석사 (2023) | SK Hynix |
| Taewon Kim | 석사 (2023) | SK Hynix |
| Juneyoung Kim | 석사 (2024) | Samsung |
| Hyunwoo Kim | 석사 (2024) | Ph.D at KAIST |
| Jonghyun Hong | 석사 (2024) | Samsung |
| Kyungmook Kim | 석사 (2025) | SK Hynix |
| Jungmin Ahn | 석사 (2025) | Samsung |
| Hyunah Park | 석사 (2025) | Ph.D at KAIST |
| Taesoo Kim | 석사 (2025) | Ph.D at Georgia Tech |
| Sieon Kim | 석사 (2026) | SK Hynix |
| Jaein Lee | 석사 (2026) | SK Hynix |
| Duksoo Kim | 석사 (2026) | SK Hynix |
| Hyungho Cho | 석사 (2026) | SK Hynix |
| Changhyun Jung | 석사 (2026) | SK Hynix |
| Hyunseo Uhm | 석사 (2026) | SK Hynix |
| Inyoung Choi | 석사 (2026) | Samsung |
| Eunji Seo | 석사 (2026) | SK Hynix |
| Hyowon An | 석사 (2026) | Samsung |

## 최근 논문 목록 (2021–2026)

누리집 Publications 메뉴의 2021–2026년 연도 구역 논문 106편이다. International Journals 18편(2021–2026년), International Conferences 83편(2021–2025년, 2026년 구역은 없다), Domestic Journals 1편(2022년), Domestic Conferences 4편(2022–2023년)이고, 연도마다 이 순서로 적었다. 저자 순서와 제목·학술지·학회 표기는 누리집 그대로이며, 교수가 저자로 없는 국내 학회 논문 2편도 목록대로 실었다. 2026년 학술지 4편은 누리집이 권·호·쪽 없이 적은 항목이라 누리집의 연도 구역을 따랐다.[^pubs]

**2026**

- Haeseok Suh, Jiwon Yoon, Hyunjun An, Keunwoo Kim, Taein Shin, Keeyoung Son, Seonguk Choi, Junghyun Lee, Youngsu Yoon, Junho Park, Youngwoo Kim, and Joungho Kim. "Signal/Power Integrity Aware Design and Computing Performance Analysis of SRAM-Bridge Embedded-GPU-HBM Architecture". *IEEE Transactions on Computer-Aided Design of Integrated Circuits & Systems*.
- Jiwon Yoon, Seongguk Kim, Keeyoung Son, Seonguk Choi, Junghyun Lee, Haeyeon Kim, Taein Shin, Joonsang Park, Haeseok Suh, Hyunjun An, Youngwoo Kim, Joungho Kim. "3D NMC-HBM: Design of 3D Near Memory Computing Architecture in High Bandwidth Memory considering Signal/Power Integrity and Computing Performance". *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*.
- Hyunjun An, Junghyun Lee, Haeseok Suh, Jiwon Yoon, Byeongmok Kim, Junho Park, Youngsu Yoon, Jaegeun Bae, Keeyoung Son, Youngwoo Kim, Joungho Kim. "PDNFormer: Fast, Accurate and Scalable Impedance Estimator for Grid-Type Multi-Layered Power Distribution Networks with Multi-Power Domains". *IEEE Transactions on Components, Packaging and Manufacturing Technology*.
- Sung-Eun Lee, Junghyun Lee, Jiwon Yoon, Hyunjun An, Haeseok Suh, Youngwoo Kim, Joungho Kim. "Robust and Explainable Physics-Informed Transformer-Based Thermal Parameter Identification of Lithium-Ion Battery Systems". *IEEE Transactions on Transportation Electrification*.

**2025**

- Junghyun Lee, Seonguk Choi, Keeyoung Son, Haeyeon Kim, Joonsang Park, Jiwon Yoon, Keunwoo Kim, Hyunjun An, Haeseok Suh, Youngwoo Kim, and Joungho Kim. "Generative Adversarial Learning Based Power Noise Induced Eye Diagram Estimation Method for High-Speed Channel Design". *IEEE Transactions on Electromagnetic Compatibility*.
- Haeyeon Kim, Junghyun Lee, Seonguk Choi, Federico Berto, Taein Shin, Joonsang Park, Jihun Kim, Jiwon Yoon,Byeongmok Kim, Youngwoo Kim, Joungho Kim. "Advanced Chiplet Placement and Routing Optimization considering Signal Integrity". *IEEE Transactions on Components, Packaging and Manufacturing Technology*.
- Jiwon Yoon, Junghyun Lee, Haeseok Suh, Youngsu Yoon, Byeongmok Kim, Junho Park, Eunji Seo, Inyoung Choi and Joungho Kim. "Signal Integrity Design and Analysis of Inter-Stack Crosslink for 3D-Heterogeneous Integrated High Bandwidth Memory (3D-HI-HBM) Module". *in Proceedings of the 2025 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Haeseok Suh, Jiwon Yoon, Taesoo Kim, Hyunjun An, Byeongmok Kim, Junho Park, Youngsu Yoon, Jaegeun Bae, Hyunseo Uhm, Inyoung Choi, Eunji Seo and Joungho Kim. "Signal Integrity Analysis of Chiplet Channel With Interposer Trace and Hybrid Bonding Pad". *in Proceedings of the 2025 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Taesoo Kim, Youngsu Yoon, Haeseok Suh, Hyunjun An, Jiwon Yoon, Junho Park, Jaegeun Bae, Byeongmok Kim, Inyoung Choi, Eunji Seo, Jayoon Koo and Joungho Kim. "Quad Tower High Bandwidth Memory (QT-HBM) with Glass Substrate and Local Silicon Bridge". *in Proceedings of the 2025 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Hyunjun An, Junho Park, Seonguk Choi, Taein Shin, Inyoung Choi, Jiwon Yoon, Haeseok Suh, Taesoo Kim, Byeongmok Kim, Youngsu Yoon, Jaegeun Bae and Joungho Kim. "Stochastic S-Parameter Generation Using Denoising Regression for High-Speed Link Design". *in Proceedings of the 2025 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Byeongmok Kim, Haeyeon Kim, Junghyun Lee, Haeseok Suh, Hyunjun An, Junho Park, Jaegeun Bae, Youngsu Yoon, Eunji Seo, Hyunseo Uhm, Inyoung Choi and Joungho Kim. "Mamba-based Reinforcement Learning Method for HBM Power Distribution Network (PDN) Optimization with Probing Port-Agnostic Policy". *in Proceedings of the 2025 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Junho Park, Keeyoung Son, Junghyun Lee, Jiwon Yoon, Haeseok Suh, Hyunjun An, Jaegeun Bae, Byeongmok Kim, Youngsu Yoon, Hyunseo Uhm, Inyoung Choi, Eunji Seo and Joungho Kim. "Power Integrity Design and Analysis of High Bandwidth Memory-centric Memory Pooling Computing Architecture". *in Proceedings of the 2025 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Youngsu Yoon, Jiwon Yoon, Haeseok Suh, Junghyun Lee, Byeongmok Kim, Junho Park, Jaegeun Bae, Hyunseo Uhm, Inyoung Choi, Eunji Seo and Joungho Kim. "High-Bandwidth Memory (HBM) Network Switch Architecture Design with Low Latency and Efficient Energy Consumption for HBM Centric Computing". *in Proceedings of the 2025 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Eunji Seo, Haeyeon Kim, Junghyun Lee, Haeseok Suh, Jiwon Yoon, Byeongmok Kim, Junho Park, Jaegeun Bae, Youngsu Yoon, Inyoung Choi, Hyunseo Uhm and Joungho Kim. "Design and Analysis of Power/Ground TSVs considering Static IR Drop for Next-generation HBM". *in Proceedings of the 2025 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Inyoung Choi, Keeyoung Son, Junghyun Lee, Jiwon Yoon, Haeseok Suh, Jaegeun Bae, Junho Park, Byeongmok Kim, Youngsu Yoon, Hyunseo Uhm, Eunji Seo and Joungho Kim. "Design and Analysis of Scalable On-Package Memory Expansion Architectures for GPU-HBM System Considering Signal Integrity". *in Proceedings of the 2025 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Taein Shin, Keunwoo Kim, Junghyun Lee, Seonguk Choi, Haeseok Suh, Hyunah Park, Hyunwoo Kim, Jinwook Song, Seokwoo Hong, Youngjun Ko, Joungho Kim. "Fast and Simple Pre-Design of Decoupling Capacitors Using Reinforcement Learning". *in Proceedings of the IEEE International Symposium on Electromagnetic Compatibility, Signal & Power Integrity*.
- Keunwoo Kim, Taein Shin, Hyunwook Park, Seonguk Choi, Haeyeon Kim, Junghyun Lee, Hyunjun An, Keeyoung Son, Haeseok Suh, Wooshin Choi, Joungho Kim. "Large Language Model-Based Decoupling Capacitor Placement Optimization". *in Proceedings of the IEEE International Symposium on Electromagnetic Compatibility, Signal & Power Integrity*.
- Kyungmook Kim, Haeyeon Kim, Junghyun Lee, Jiwon Yoon, Joonsang Park, Keunwoo Kim, and Joungho Kim. "Homogeneous Multi-Chip PDN Optimization for DDR Memory Architecture Using RL". *in Proceedings of the IEEE International Symposium on Electromagnetic Compatibility, Signal & Power Integrity*.
- Taesoo Kim, Taein Shin, Keunwoo Kim, Haeseok Suh, Hyunjun An, Joungho Kim. "UCIe-A Mimic Channel Design and Verification for Early on-Chip System Validation". *in Proceedings of the 2025 IEEE 75th Electronic Components and Technology Conference (ECTC)*.
- Haeseok Suh, Hyunjun An, Haeyeon Kim, Seonguk Choi, Taesoo Kim, Keeyoung Son, Keunwoo Kim, Jiwon Yoon, Byeongmok Kim, Youngsu Yoon, Jaegeun Bae, Joungho Kim. "Multi-Chiplet Power Delivery Network (PDN) Co-Optimization Considering Current Spectrum by Deep Reinforcement Learning-Based Decoupling Capacitor Placement". *in Proceedings of the 2025 IEEE 75th Electronic Components and Technology Conference (ECTC)*.
- Hyunjun An, Haeseok Suh, Keeyoung Son, Haeyeon Kin, Keunwoo Kim, Taein Shin, Seonguk Choi, Taesoo Kim, Junho Park, Inyoung Choi, Joungho Kim. "Generative Model Based Multi-Layer PDN Impedance Estimation with Multi-Power Domain". *in Proceedings of the 2025 IEEE 75th Electronic Components and Technology Conference (ECTC)*.
- Hyunjun An, Haeyeon Kim, Junghyun Lee, Taein Shin, and Joungho Kim. "Flow Model Can Give You Optimal and Diverse Design Guidance for TSV Array Placement in HBM". *in Proceeding of the 2025 DesignCon*.
- Haeyeon Kim, Federico Berto, Junghyun Lee, Hyunjun An, Taein Shin, Chuabo Hua, Jinkyoo Park, Youngwoo Kim, and Joungho Kim. "Accelerating Chiplet Placement and Routing Optimization with Machine Learning". *in Proceeding of the 2025 DesignCon*.
- Keeyoung Son, and Joungho kim. "A Novel ThermoFlow Uniformizer applied Immersion Cooling System (TFU-ICS) for Highly-dense Multi-GPU-HBM based Compute Module for AI Supercomputer". *in Proceeding of the 2025 DesignCon*.
- Taein Shin, Hyunwook Park, Boogyo Sim, Keunwoo Kim, Keeyoung Son, Joonsang Park, Jiwon Yoon, Haeyeon Kim, Hyunjun An, and Joungho Kim. "PSIJ based Integrated Power Integrity Design for HBM using Reinforcement Learning: Beyond the Target Impedance". *in Proceeding of the 2025 DesignCon*.

**2024**

- Joonsang Park, Seonguk Choi, Keeyoung Son, Junghyun Lee, Taein Shin, Keunwoo Kim, Boogyo Sim, Seongguk Kim, Jihun Kim, Jiwon Yoon, Youngwoo Kim, and Joungho Kim. "Pin-Opt: Graph Representation Learning for Large-Scale Pin Assignment Optimization of Microbumps Considering Signal and Power Integrity". *IEEE Transactions on Components, Packaging and Manufacturing Technology, Vol. 14, No. 4, pp. 681-692*.
- Keunwoo Kim , Hyunwook Park, Seongguk Kim, Youngwoo Kim, Kyungjune Son, Keeyoung Son, Taein Shin, Boogyo Sim, Joonsang Park, Shinyoung Park, and Joungho Kim. "Policy-based Reinforcement Learning (RL) for Through Silicon Via (TSV) Array Design in High Bandwidth Memory (HBM) considering Signal Integrity (SI)". *IEEE Transactions on Electromagnetic Compatibility, Vol. 66, No. 1, pp. 256-269*.
- Taesoo Kim, Jiwon Yoon, Seonguk Choi, Haeyeon Kim, Haeseok Suh, Jungmin Ahn, Hyunah Park, and Joungho Kim. "Design and Analysis of Twin Tower High Bandwidth Memory (HBM) Architecture for Large Memory Capacity and High Bandwidth System". *in Proceedings of the 2024 IEEE Electrical Design of Advanced Packaging and Systems*.
- Haeyeon Kim, Federico Berto, Chuanbo Hua,  Minsu Kim, Joungho Kim and Jinkyoo Park. "Chiplet Placement and Routing Optimization: A Novel Benchmark and Neural Solver". *in Machine Learning for Systems Workshop at Neural Information Processing and Systems (NeurIPS) 2024*.
- Haeyeon Kim, Joonsang Park, Hyunah Park, Keeyoung Son, Hyunsik Kim, Taeil Bae, Haekang Jung, and Joungho Kim. "Design and Analysis of High-Density Silicon Interposer Channel and Power Distribution Network". *in Proceedings of the 2024 IEEE Electrical Design of Advanced Packaging and Systems*.
- Keeyoung Son,  Seonguk Choi, Keunwoo Kim, Jiwon Yoon, Junghyun Lee, Haeseok Suh, Hyunjun An and Joungho Kim. "High-speed Interconnect Design of Silicon Interposer based Heterogeneous Integration for AI Computing". *in Proceedings of the 2024 IEEE Electrical Design of Advanced Packaging and Systems*.
- Hyunjun An, Junghyun Lee, Keeyoung Son, Seonguk Choi, Taein Shin, Keunwoo Kim, Jiwon Yoon, Taesoo Kim, Jungmin Ahn, Hyunah Park, Haeseok Suh and Joungho Kim. "Eye-Diagram Edge Estimation (EEE) Network for Through Silicon Via Design in Next-Generation High Bandwidth Memory". *in Proceedings of the 2024 IEEE Electrical Design of Advanced Packaging and Systems*.
- Jungmin Ahn, Seonguk Choi, Taein Shin, Junghyun Lee, Jiwon Yoon, Keunwoo Kim, Keeyoung Son, Haeseok Suh, Taesoo Kim, Hyunah Park, Hyunjun An, Jinwook Song, and Joungho Kim. "Design and Analysis of Ultra High Bandwidth (UHB) Interconnection-based GPU-Ring for the AI Superchip Module". *in Proceedings of the 2024 IEEE Electrical Design of Advanced Packaging and Systems*.
- Haeseok Suh, Jiwon Yoon, Keeyoung Son, Seonguk Choi, Keunwoo Kim, Junghyun Lee, Taein Shin, Hyunjun An, Taesoo Kim, Jungmin Ahn, Hyunah Park, Hyunsik Kim, Taeil Bae, Haekang Jung and Joungho Kim. "Design and Analysis of L3 Cache Embedded GPU-High Bandwidth Memory Architecture with Reduced Energy and Latency for AI Computing". *in Proceedings of the 2024 IEEE Electrical Design of Advanced Packaging and Systems*.
- Hyunah Park, Seonguk Choi, Haeyeon Kim, Taein Shin, Keeyoung Son, Jiwon Yoon, Junghyun Lee, Haeseok Suh, Taesoo Kim, Jungmin Ahn, Hyunjun An, and Joungho Kim. "Design and Analysis of Extended Scale Cache (ESC) Stacked-GPU-HBM Module Architecture Considering Power Integrity (PI)". *in Proceedings of the 2024 IEEE Electrical Design of Advanced Packaging and Systems*.
- Junghyun Lee, Keeyoug Son, Junho Park, Keunwoo Kim, Hyunjun An, Seonguk Choi, Jihun Kim, Hyunah Park, Sumi Choi, Sanghyuk Son, and Joungho Kim. "Signal Integrity Analysis of PCIe Channel with Floating Board-to-Board Connectors in Automotive Infotainment System". *in Proceedings of the 2024 IEEE Electrical Design of Advanced Packaging and Systems*.
- Keunwoo Kim, Hyunwook Park, Keeyoung Son, Seonguk Choi, Taein Shin, Junghyun Lee, Jiwon Yoon, Hyunjun An, Haeyeon Kim, Wooshin Choi, Jung-Hwan Choi and Joungho Kim. "Explainable Reinforcement Learning(XRL)-based Decap Placement Optimization for High-Bandwidth Memory (HBM)". *in Proceedings of the 2024 IEEE Electrical Design of Advanced Packaging and Systems*.
- Taein Shin, Seonguk Choi, Jungmin Ahn, Keunwoo Kim, Junghyun Lee, Haeseok Suh, Hyunah Park, Haeyeon Kim, Hyunjun An, Jinwook Song and Joungho Kim. "PSIJ based Optimal PDN Design for Cost-Effective SSD using Reinforcement Learning". *in Proceedings of the 2024 IEEE Electrical Design of Advanced Packaging and Systems*.
- Seonguk Choi, Seonguk Choi, Jihun Kim, Taein Shin, Jungmin Ahn, Keunwoo Kim, Keeyoung Son, Joonsang Park, Jinwook Song, Kyungsuk Kim, Sunghoon Chun, and Joungho Kim. "Imitation Learning-based Fast Optimization of SSD Interface for PCIe 6.0 considering Signal Integrity". *in Proceedings of the IEEE International Symposium on Electromagnetic Compatibility, Signal Integrity and Power Integrity*.
- Jiwon Yoon, Youngsu Kwon, Hyunwoo Kim, Juhyeon Lee, Joungho Kim, Sungjin Kim, Heejun Jang, Kyun Ahn, Jinhan Kim, Taekyeong Hwang, Yi-Gyeong Kim, Minseok Choi. "The Energy-Efficient 10-Chiplet AI Hyperscale NPU on Large-Scale Advanced Package". *2024 IEEE 74th Electronic Components and Technology Conference (ECTC), Denver, CO, USA, 2024*.

**2023**

- Seonguk Choi, Keeyoung Son, Hyunwook Park, Seongguk Kim, Boogyo Sim, Jihun Kim, Joonsang Park, Minsu Kim, Haeyeon Kim, Jinwook Song, Youngwoo Kim, and Joungho Kim. "Deep Reinforcement Learning-based Optimal and Fast Hybrid Equalizer Design Method for High Bandwidth Memory (HBM) Module". *IEEE Transactions on Components, Packaging and Manufacturing Technology*.
- Jihun Kim, Minsu Kim, Haeyeon Kim, Hyunwook Park, Seonguk Choi, Joonsang Park, Boogyo Sim, Keeyoung Son, Seongguk Kim, Jinwook Song, Youngwoo Kim, and Joungho Kim. "Bayesian Exploration Imitation Learning-Based Contextural via Design Optimization Method of PAM-4 Based High-Speed Serial Link". *IEEE Transactions on Electromagnetic Compatibility*.
- Boogyo Sim, Taein Shin, Hyunwook Park, Keeyoung Son, Keunwoo Kim, Daehwan Lho, Seongguk Kim, Jiwon Yoon, Hyunwoo Kim, Junghyun Lee, Jungyoung Kim, and Joungho Kim. "Fast and Accurate Computation of Wireless Power Transfer System Optimal Design Using Particle Swarm Optimization Method". *IEEE Transactions on Electromagnetic Compatibility*.
- Jihun Kim, Seonguk Choi, Taein Shin, Keeyoung Son, Boogyo Sim, Seongguk Kim, Haeyeon Kim, Joonsang Park, Jinwook Song, Kyungsuk Kim, Jonggyu Park and Joungho Kim. "Imitation Learning-based Equalizer Design Optimization Method on PCIe 6.0". *in Proceedings of the 2023 IEEE Electrical Design of Advanced Packaging and Systems*.
- Seongguk Kim,  Keeyoung Son, Jiwon Yoon, Taein Shin, Keunwoo kim, Boogyo Sim, Hyunwook Park, Joonsang Park, Seonguk Cho, Jihun Kim, Haeyeon Kim and Joungho Kim. "Signal Integrity Analysis of High-speed PCIe Channel with Board-to-Board Interconnect for High-Performance Server". *in Proceedings of the 2023 IEEE Electrical Design of Advanced Packaging and Systems*.
- Taein Shin, Keunwoo Kim, Hyunwook Park, Boogyo Sim, Seongguk Kim, Jihun Kim, Seonguk Choi, Joonsang Park, Jinwook Song, Jaehyup Kim, Joung Won Park, Daehyun Kang, and Joungho Kim. "Signal Integrity Design and Analysis of Universal Chiplet Interconnect Express (UCIe) Channel in Silicon Interposer for Advanced Package". *in Proceedings of the 2023 IEEE Electrical Design of Advanced Packaging and Systems*.
- Keeyoung Son, Joonsang Park, Seongguk Kim, Boogyo Sim, Keunwoo Kim, Seonguk Choi, Hyunsik Kim, and Joungho Kim. "Thermal Analysis of High Bandwidth Memory (HBM) -GPU Module considering Power Consumption". *in Proceedings of the 2023 IEEE Electrical Design of Advanced Packaging and Systems*.
- Keeyoung Son, Keunwoo Kim, Seonguk Choi, Jiwon Yoon, Jihun Kim, Jonghyun Hong, Hyunwoo Kim, Junghyun Lee, and Joungho Kim. "The Significance of Thermal-Aware Universal Chiplet Interconnect Express (UCIe) Interface Design in 2.5D/3D ICs". *in Proceedings of the 2023 IEEE Electrical Design of Advanced Packaging and Systems*.
- Taein Shin, Hyunwook Park, Daehwan Lho, Keunwoo Kim, Boogyo Sim, Seongguk Kim, Jihun Kim, Seonguk Choi, Jiwon Yoon, Jinwook Song, Sunghoon Chun, and Joungho Kim. "SI/PI Co-Design of 12.8 Gbps HBM I/O Interface using Bayesian Optimization for PSIJ Reduction". *in Proceedings of the IEEE International Symposium on Electromagnetic Compatibility, Signal Integrity and Power Integrity*.
- Hyunwook Park, Taein Shin, Seongguk Kim, Keeyoung Son, Keunwoo Kim, Boogyo Sim, Hyungmin Kang, Seonguk Choi, Jiwon Yoon, Hyunwoo Kim, Chulsoon Hwang, and Joungho Kim. "Power Supply Induced Jitter (PSIJ) Modeling, Analysis, and Optimization of High Bandwidth Memory (HBM) I/O Interface". *in Proceedings of the IEEE International Symposium on Electromagnetic Compatibility, Signal Integrity and Power Integrity*.
- Jiwon Yoon, Hyunwoo Kim, Boogyo Sim, Hyunwook Park, Yigyeong Kim, Sujin Park, Youngsu Kwon and Joungho Kim. "Multi-Stripline Redistribution Layer Interposer Channel Design for High Bandwidth Memory Module Considering Via Interconnect". *in Proceedings of the The 20th International SoC Conference*.
- Junghyun Lee, Seonguk Choi, Keeyoung Son, Joonsang Park, Hyunwoo Kim, Keunwoo Kim, Taein Shin, Boogyo Sim, Jonghyun Hong, Jiwon Yoon, Juneyoung Kim and Joungho Kim. "Adaptive Gramian-Angular-Field Segmentation Integration Based Generative Adversarial Network (AGSI-GAN) for Eye Diagram Estimation of  High Bandwidth Memory (HBM) Interposer". *in Proceedings of the 2023 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Jonghyun Hong, Jiwon Yoon, Hyunwoo Kim, Keeyoung Son, Seonguk Choi, Junghyun Lee, Keunwoo Kim, Joonsang Park, Seongguk Kim, Boogyo Sim and Joungho Kim. "Signal Integrity Design and Analysis of Redistribution Layer Interposer Channel with Diagonal Meshed Ground in Memory Interface of High Bandwidth Memory". *in Proceedings of the 2023 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Hyunwoo Kim, Seonguk Choi, Joonsang Park, Haeyeon Kim, Keeyoung Son, Junghyun Lee, Jiwon Yoon, Jonghyun Hong, Boogyo Sim, Keunwoo Kim, Taein Shin, and Joungho Kim. "Modeling and Analysis of Simultaneous Switching Noise for Full Wafer Scale Chip Core". *in Proceedings of the 2023 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Juneyoung Kim, Seonguk Choi, Seongguk Kim, Jihun Kim, Boogyo Sim, Junghyun Lee, Taein Shin, Hyunwoo Kim, Jonghyun Hong, Haeyeon Kim, Joonsang Park , and Joungho Kim. "Crosstalk Mitigated On-chip Interconnect Design for High-speed Network-on-Chip (NoC) of Full Wafer Scale Chip (FWSC)". *in Proceedings of the 2023 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Joonsang Park, Seongguk Kim, Keeyoung Son, Haeyeon Kim, Hyunwoo Kim, Hyunsik Kim, Seonguk Choi, Jihun Kim, and Joungho Kim. "Design and Analysis of an Irregular-Shaped Power Distribution Network (PDN) for High Bandwidth Memory (HBM) Interposer". *in Proceedings of the 2023 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Jiwon Yoon, Hyunwook Park, Hyunwoo Kim, Boogyo Sim, Jonghyun Hong, Seongguk Kim, Keeyoung Son, Keunwoo Kim, Yigyeong Kim, Sujin Park, Youngsu Kwon and Joungho Kim. "Design and Analysis of Redistribution Layer Interposer Channel Considering Signal Integrity for High Bandwidth Module". *in Proceedings of the 2023 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Hyunah Park, Haeyeon Kim, Hyunwoo Kim, Joonsang Park, Seonguk Choi, Jihun Kim, Keeyoung Son, Haeseok Suh, Taesoo Kim, Jungmin Ahn and Joungho Kim. "Versatile Genetic Algorithm-Bayesian Optimization(GA-BO) Bi-Level Optimization for Decoupling Capacitor Placement". *in Proceedings of the 2023 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Boogyo Sim, Taein Shin, Hyunwook Park, Keeyoung Son, Keunwoo Kim, Daehwan Lho, Hyungmin Kang, Joonsang Park, Haeyeon Kim, Jihun Kim, Seonguk Choi and Joungho Kim. "Bayesian Optimization based Fast and Accurate Wireless Power Transfer System Coil Optimization for High Efficiency". *2023 IEEE Wireless Power Technology Conference and Expo (WPTCE), San Diego, CA, USA, 2023, pp. 1-5, doi: 10.1109/WPTCE56855.2023.10215668*.
- Haeyeon Kim, Minsu Kim, Federico Berto, Joungho Kim and Jinkyoo Park. "DevFormer: A Symmetric Transformer for Context-Aware Device Placement". *in Proceedings of the 40th International Conference on Machine Learning (ICML) PMLR 202:16541-16566, 2023*.
- Seonguk Choi, Jihun Kim, Minsu Kim, Haeyeon Kim, Joonsang Park, Keeyoung Son, Seongguk Kim, Taein Shin, Keunwoo Kim, Jiwon Yoon, Jinwook Song, Kyungsuk Kim, Jonggyu Park and Joungho Kim. "Extremely Fast Dynamic Link Equalization for PCIe based on Imitation Learning". *in Proceedings of the 2023 DesignCon*.
- Haeyeon Kim, Minsu Kim, Seonguk Choi, Jihun Kim, Joonsang Park, Keeyoung Son, Taein Shin, Hyunwook Park, Jinkyoo Park and Joungho Kim. "Learning Beyond Low-Quality Data Distribution: An Application to Optimal Decap Placement". *in Proceedings of the 2023 DesignCon*.
- 홍종현, 김종훈,김지훈,박준상,박홍태,연영명,최도현,신윤섭,김정호. "고전압 릴레이의 운동 상태 분석을 위한 전자기 및 기계적 통합 시뮬레이션 구축". *2023년도 한국전자파학회 하계종합학술대회 논문집, 강원도, Vol. 10, No.1*.
- 박준상, 홍석우, 김성국, 박홍태, 연영명, 이준호. "고전압 릴레이 요크 흡입력 개선을 위한 요크 자석 배치 설계". *2023년도 한국전자파학회 하계종합학술대회 논문집, 강원도, Vol. 10, No.1*.
- 박준상, 홍석우, 김성국, 박홍태, 연영명, 이준호. "고전압 릴레이 아크 소호를 위한 영구자석 배치 설계". *2023년도 한국전자파학회 하계종합학술대회 논문집, 강원도, Vol. 10, No.1*.

**2022**

- Keeyoung Son, Seongguk Kim, Hyunwook Park, Taein Shin, Keunwoo Kim, Minsu Kim, Boogyo Sim, Subin Kim, Gapyeol Park, Shinyoung Park, Seungtaek Jeong, and Joungho Kim. "Thermal and Signal Integrity Co-Design and Verification of Embedded Cooling Structure with Thermal Transmission Line (ECS-TTL) for High Bandwidth Memory Module". *IEEE Transactions on Components, Packaging and Manufacturing Technology, Vol. 12, No. 9, pp. 1542-1556, August 25, 2022*.
- Hyunwook Park, Minsu Kim, Seongguk Kim, Keunwoo Kim, Haeyeon Kim, Taein Shin, Keeyoung Son, Boogyo Sim, Subin Kim, Seungtaek Jeong, Chulsoon Hwang, Joungho Kim. "Transformer Network-Based Reinforcement Learning Method for Power Distribution Network (PDN) Optimization of High Bandwidth Memory (HBM)". *IEEE Transactions on Microwave Theory and Techniques 70.11 (2022): 4772-4786*.
- Haeyeon Kim, Minsu Kim, Joungho Kim and Jinkyoo Park. "Collaborative Symmetricity Exploitation for Offline Learning of Hardware Design Solver". *in Offline Reinforcement Learning Workshop at Neural Information Processing and Systems (NeurIPS) 2022*.
- Hyunwoo Kim, Haeyeon Kim, Joonsang Park, Keeyoung Son, Hyunwook Park, Taein Shin, Keunwoo Kim, Jiwon Yoon, Junghyun Lee, Jonghyun Hong, Juneyoung Kim and Joungho Kim. "Design and Analysis of Hierarchical Power Distribution Network (PDN) for Full Wafer Scale Chip (FWSC) Module". *in Proceedings of the 2022 IEEE Electrical Design of Advanced Packaging and Systems*.
- Keeyoung Son, Daehwan Lho, Keunwoo Kim, Seonguk Choi, Haeyeon Kim, Hyunwook Park, Boogyo Sim, Hyunwoo Kim, Taein Shin and Joungho Kim. "Power Distribution Network Impedance Analysis considering Thermal Distribution". *in Proceedings of the 2022 IEEE Electrical Design of Advanced Packaging and Systems*.
- Keeyoung Son, Daehwan Lho, Seongguk Kim, Joonsang Park, Keunwoo Kim, Namhyeon Choi, Hyunsik Kim and Joungho Kim. "Thermal Analysis of DDR5 DIMM with Forced Air Cooling Method". *in Proceedings of the 2022 IEEE Electrical Design of Advanced Packaging and Systems*.
- Kyungjune Son, Keunwoo Kim, Gapyeol Park, Daehwan Lho, Hyunwook Park, Boogyo Sim, Taein Shin, Joonsang Park, Haeyeon Kim, Kyubong Gong and Joungho Kim. "Signal Integrity and Power Leakage Optimization for 3D X-Point Memory Operation using Reinforcement Learning". *in Proceedings of the 2022 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Keunwoo Kim, Junghyun Lee, Seokwoo Hong, Hyunwoo Kim, Boogyo Sim, Kyungjune Son, Taein Shin, Keeyoung Son, Jinyoung Kim, Kyubong Kong, and Joungho Kim. "Low EMI Board-to-board Connector Design for 5G mmWave and High-speed Signaling". *in Proceedings of the 2022 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Hyunwook Park, Taein Shin, Seongguk Kim, Daehwan Lho, Boogyo Sim, Jinwook Song, Kyubong Kong and Joungho Kim. "Scalable Transformer Network-based Reinforcement Learning Method for PSIJ Optimization in HBM". *in Proceedings of the 2022 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Boogyo Sim, Keunwoo Kim, Taein Shin, Hyunwook Park, Seongguk Kim, Daehwan Lho, Keeyoung Son,Kyubong Kong, Seungtaek Jeong, Seonguk Choi, Jihun Kim and Joungho Kim. "Intra-pair Skew Impact Analysis of High-speed Cables for HDMI Interface". *in Proceedings of the 2022 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Daehwan Lho, Hyunwook Park, Keunwoo Kim, Seongguk Kim, Boogyo Sim, Kyungjune Son, Keeyoung Son, Jihun Kim, Seonguk Choi, Joonsang Park, Haeyeon Kim, Kyubong Kong and Joungho Kim. "Deterministic Policy Gradient-based Reinforcement Learning for DDR5 Memory Signaling Architecture Optimization considering Signal Integrity". *in Proceedings of the 2022 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Jihun Kim, Minsu Kim, Hyunwook Park, Jiwon Yoon, Seonguk Choi, Joonsang Park, Haeyeon Kim, Keeyoung Son, Seongguk Kim, Daehwan Lho, Keunwoo Kim, Jinwook Song, Kyungsuk Kim, Jonggyu Park and Joungho Kim. "Imitation Learning with Bayesian Exploration (IL-BE) for Signal Integrity (SI) of PAM-4 based High-speed Serial Link: PCIe 6.0". *in Proceedings of the 2022 DesignCon*.
- Joonsang Park, Minsu Kim, Seonguk Choi, Jihun Kim, Haeyeon Kim, Hyunwook Park, Seongguk Kim, Taein Shin and Joungho Kim. "Learning Super-scale Microbump Pin Assignment Optimization for Real-world PCB Design with Graph Representation". *in Proceedings of the 2022 DesignCon*.
- Seonguk Choi, Minsu Kim, Hyunwook Park, Haeyeon Kim, Joonsang Park, Jihun Kim, Keeyoung Son, Seongguk Kim, Keunwoo Kim, Daehwan Lho, Jiwon Yoon, Jinwook Song, Kyungsuk Kim, Jonggyu Park and Joungho Kim. "Deep Reinforcement Learning-based Channel-flexible Equalization Scheme: An Application to High Bandwidth Memory". *in Proceedings of the 2022 DesignCon*.
- Seongguk Kim, Hyunwook Park, Taein Shin, Daehwan Lho, Keeyoung Son, Keunwoo Kim, Minsu Kim, Joonsang Park, and Joungho Kim. "A Processing-In-Memory on High Bandwidth Memory (PIM-HBM): Impact of interconnect Channels on System Performance in 2.5D/3D IC". *in Proceedings of the 2022 DesignCon*.
- Keeyoung Son, Seongguk Kim, Keunwoo Kim, Hyunwook Park, Minsu Kim, Taein Shin, Seonguk Choi, Joonsang Park, Jihun Kim, Haeyeon Rachel Kim and Joungho Kim. "Thermal Transmission Line: Smoothing Thermal Gradients and Lowering Temperature for Signal Integrity Improvement of HBM and 2.5D ICs". *in Proceedings of the 2022 DesignCon*.
- Haeyeon Kim, Minsu Kim, Seonguk Choi, Jihun Kim, Joonsang Park, Keeyoung Son, Hyunwook Park, Subin Kim and Joungho Kim. "Imitate Expert Policy and Learn Beyond: A Practical PDN Optimizer by Imitation Learning". *in Proceedings of the 2022 DesignCon*.
- Taein Shin,  Hyunwook Park, Seongguk Kim, Keunwoo Kim, Keeyoung Son, and Joungho Kim. "A New Challenge for Neuromorphic Computing System: from Off-chip Interconnects to On-chip Interconnects". *in Proceedings of the 2022 DesignCon*.
- 손기영, 김성국, 윤지원, 진소연, 황재민, 김상민, 이우신, 김정호. "지능형 전장인식을 위한 엣지 컴퓨팅 기반 인공지능 가속기 성능 분석". *전자공학회논문지 59.7 (2022): 41-49*.
- 김지훈, 홍석우, 박준상, 박홍태, 연영명, 이준호, 최도현, 김정호. "고전압 릴레이 구동력 상승을 위한 액츄에이터 상단부 물질 설계". *2024년도 한국전자파학회 하계종합학술대회 논문집, 제주도, Vol. 10, No.1*.

**2021**

- Kyungjune Son, Minsu Kim, Hyunwook Park, Daehwan Lho, Keeyoung Son, Keunwoo Kim, Seongsoo Lee, Seungtaek Jeong, Shinyoung Park, Seokwoo Hong, Gapyeol Park, and Joungho Kim. "Reinforcement-learning-based Signal Integrity Optimization and Analysis of a Scalable 3D X-Point Array Structure". *IEEE Transactions on Components, Packaging and Manufacturing Technology, Vol. 12, No. 1, pp. 100-110, November 19, 2021*.
- Seongguk Kim, Subin Kim, Kyungjun Cho,  Taein Shin, Hyunwook Park, Daehwan Lho, Shinyoung Park, Kyungjune Son, Gapyeol Park, Seungtaek Jeong, Youngwoo Kim, and Joungho Kim. "Signal Integrity and Computing Performance Analysis of a Processing-In-Memory of High Bandwidth Memory (PIM-HBM) Scheme". *IEEE Transactions on Components, Packaging and Manufacturing Technology, Vol. 11, No. 11, pp. 1955-1970, October 1, 2021*.
- Daehwan Lho, Hyunwook Park, Shinyoung Park, Subin Kim, Hyungmin Kang, Boogyo Sim, Seongguk Kim, Junyong Park, Kyungjun Cho, Jinwook Song, Youngwoo Kim, and Joungho Kim. "Channel Characteristic-Based Deep Neural Network Models for Accurate Eye Diagram Estimation in High Bandwidth Memory (HBM) Silicon Interposer". *IEEE Transactions on Electromagnetic Compatibility, Vol. 64, No. 1, pp. 196-208, July 8, 2021*.
- Taein Shin, Shinyoung Park, Seongguk Kim, Subin Kim, Kyungjune Son, Hyunwook Park, Daehwan Lho, Kyungjun Cho, Gapyeol Park, Kyubong Gong, Seongtaek Jung, and Joungho Kim. "Signal Integrity Modeling and Analysis of Large-Scale Memristor Crossbar Array in a High-Speed Neuromorphic System for Deep Neural Network". *IEEE Transactions on Components, Packaging and Manufacturing Technology, Vol. 11, No. 7, pp. 1122-1136, June 28, 2021*.
- Gapyeol Park, Youngwoo Kim, Kyungjun Cho, Junyong Park, Insu Hwang, Jihye Kim, Kyungjune Son, Hyunwook Park, Atom O. Watanabe, Pulugurtha Markondeya Raj, Rao R. Tummala, and Joungho Kim. "Measurement and Analysis of Through Glass Via Noise Coupling and Shielding Structures in a Glass Interposer". *IEEE Transactions on Electromagnetic Compatibility, Vol. 63, No. 5, pp. 1562-1573, March 17, 2021*.
- Minsu Kim, Jinkyu Park,and Joungho Kim. "Learning Collarative Policies to Solve NP-hard Routing Problems". *in Proceedings of the 2021 Conference on Neural Information Processing Systiems*.
- Seongguk Kim, Taein Shin, Hyunwook Park, Daehwan Lho, Keeyoung Son, Keunwoo kim, Joonsang Park, Seonguk Choi,Jihun Kim, Haeyeon Kim and Joungho Kim. "Signal Integrity Design and Analysis of a Spiral Through-Silicon Via (TSV) Array Channel for High Bandwidth Memory (HBM)". *in Proceedings of the 2021 IEEE Electrical Design of Advanced Packaging and Systems*.
- Taein Shin, Hyunwook Park, Keunwoo Kim, Seongguk Kim, Keeyoung Son, Kyungjune Son, Gapyeol Park, Joonsang Park, Seonguk Choi, and Joungho Kim. "Modeling and Analysis of System-Level Power Supply Noise Induced Jitter (PSIJ) for 4 Gbps High Bandwidth Memory (HBM) I/O Interface". *in Proceedings of the 2021 IEEE Electrical Design of Advanced Packaging and Systems*.
- Hyunwook Park, Joonsang Park, Gapyeol Park, Daehwan Lho, Boogyo Sim, Hyungmin Kang, Taein Shin, Seongguk Kim, Seonguk Choi, Seongmin Choi, Jinyoung Kim, and Joungho Kim. "Signal Integrity Design and Analysis of a HDMI 2.1 Connector for Improved Electrical Characteristics". *in Proceedings of the 2021 IEEE Electrical Design of Advanced Packaging and Systems*.
- Keunwoo Kim, Keeyoung Son, Seokwoo Hong, Joungho Kim, and Jinyoung Kim. "A Novel Spire Clip-type Pogo Connector Design with High Electrical and Thermal Reliability". *in Proceedings of the 2021 IEEE Electrical Design of Advanced Packaging and Systems*.
- Jihun Kim, Hyunwook Park, Minsu Kim, Seongguk Kim, Seonguk Choi, Keeyoung Son, Joonsang Park, Haeyeon Kim, Jinwook Song, Youngmin Ku, Jonggyu Park and Joungho Kim. "PAM-4 based PCIe 6.0 Channel Design Optimization Method using Bayesian Optimization". *in Proceedings of the 2021 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Minsu Kim, Hyunwook Park, Keeyoung Son, Seongguk Kim, Haeyeon Kim, Jihun Kim, Jinwook Song, Youngmin Ku, Jounggyu Park and Joungho Kim. "Imitation Learning for Simultaneous Escape Routing". *in Proceedings of the 2021 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Joonsang Park, Minsu Kim, Seongguk Kim, Keeyoung Son, Taein Shin, Hyunwook Park, Jihun Kim,Seonguk Choi, Haeyeon Kim, Keunwoo Kim,and Joungho Kim. "Deep Reinforcement Learning-based Pin Assignment Optimization of BGA Packages considering Signal Integrity with Graph Representation". *in Proceedings of the 2021 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Seonguk Choi, Minsu Kim, Hyunwook Park, Keeyoung Son, Seongguk Kim, Jihun Kim, Joonsang Park, Haeyeon Kim, Taein Shin, Keunwoo Kim,and Joungho Kim. "Sequential Policy Network-based Optimal Passive Equalizer Design for an Arbitrary Channel of High Bandwidth Memory using Advantage Actor Critic". *in Proceedings of the 2021 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Haeyeon Kim, Hyunwook Park, Minsu Kim, Seonguk Choi, Jihun Kim, Joonsang Park, Seongguk Kim, Subin Kim,and Joungho Kim. "Deep Reinforcement Learning Framework for Optimal Decoupling Capacitor Placement on General PDN with an Arbitrary Probing Port". *in Proceedings of the 2021 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Keeyoung Son, Seongguk Kim, Minsu Kim, Daehwan Lho, Keunwoo Kim, Hyunwook Park, Gapyeol Park,and Joungho Kim. "Signal Integrity Analysis of High Speed Channel considering Thermal Distribution". *in Proceedings of the 2021 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Hyunwook Park, Jihun Kim, Minsu Kim, Keunwoo Kim, Boogyo Sim, Daehwan Lho, Taein Shin, Keeyoung Son, Jinwook Song, Youngmin Ku, Jonggyu Park,and Joungho Kim. "Crosstalk-included PAM-4 Worst Eye Diagram Estimation Method for High-speed Serial Links". *in Proceedings of the 2021 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Daehwan lho, Hyunwook Park, Gapyeol Park, Joonsang Park, Kyungjune Son, Boogyo Sim, Hyungmin Kang, Seongguk Kim,Taein Shin, Keunwoo Kim, Keeyoung Son, Jinyoung Kim and Joungho Kim. "Design and Analysis of HDMI 2.1 Connector for Crosstalk Reduction using Tabs and Inverse Tabs". *in Proceedings of the 2021 IEEE Electrical Performance of Electronic Packaging and Systems*.
- Subin Kim, Seongguk Kim,Seungtaek Jeong,Gapyeol Park,Hyunwook Park, and Joungho Kim. "Wireless Memory Test: a Breakthrough Solution for Highly Reliable High Bandwidth Memory". *in Proceedings of the DesignCon 2021*.
- Minsu Kim, Hyunwook Park,Seonguk Choi, Haeyeon Rachel Kim, Seongguk Kim,Keeyoung Son,Keunwoo Kim,Daehwan Lho,Kyunjune Son,Subin Kim, and Joungho Kim. "Neural Language Model Enables Extremely Fast and Robust Routing on Interposer". *in Proceedings of the DesignCon 2021*.
- Kyubong Kong, Hyunwook Park, Kyungjun Cho, Boogyo Sim, Subin Kim, Seungtaek Jeong, JunSang Yun, Daesub Shin, Hyewon Kim, Sooyoung Jang, Jinwook Kim, Kyuyoung Kim, Jihyo Kang, Daehan Kwon, Keeyoung Son, Minsu Kim, and Joungho Kim. "A New Design Method Using Reinforcement Learning for GDDR6 WCK over 20Gbps". *in Proceedings of the DesignCon 2021*.

## 과제

Funded Projects 페이지의 2023년 과제 9건이다. 페이지는 과제를 지원 기관 이름과 학생 책임자(Leader)로만 적고 과제 이름과 기간은 적지 않는다.[^proj]

- 2023 · SK Hynix (Leader: Joonsang Park)
- 2023 · Samsung Electronics 1 (Leader: Keunwoo Kim)
- 2023 · Samsung Electronics 2 (Leader: Seonguk Choi)
- 2023 · Hanwha System 1 (Leader: Seongguk Kim)
- 2023 · Hanwha System 2 (Leader: Hyeongmin Kang)
- 2023 · LG Electronics (Leader: Hyunwoo Kim)
- 2023 · KET (Electronics) (Leader: Taein Shin)
- 2023 · KET (EV) (Leader: Jihun Kim)
- 2023 · National Research Foundation of Korea (Leader: Jiwon Yoon)

## 수상

2022년 이후의 수상이다. 교수 수상 4건은 Professor 페이지 Awards 칸의 연월이고, 학생·연구원 수상 6건은 첫 화면 Recent Updates 글이다. 첫 화면 글은 날짜를 따로 적지 않아, 앞의 연도는 글 제목의 행사 연도다. 문장은 게시된 그대로다.[^prof][^home]

- 2025.12 · Top Contribution Award for Institutional Research Funding, KAIST (교수)
- 2025.09 · 7th Hanyang Paiknam Prize, Paiknam Memorial Foundation / Hanyang University (교수)
- 2025.02 · 8th Dawon Kahng Award (Circuits & Systems), Korean Conference on Semiconductors (KCS) (교수)
- 2024 · Excellent Teaching Award, KAIST, School of Electrical Engineering (교수, 누리집 표기 2024/2022/2015, 3-time recipient)
- 2025 · IEEE EDAPS 2025 Best Student Award: Master student Jaegeun Bae received the Best Student Award at EDAPS 2025.
- 2025 · DesignCon 2025 Best Paper Award: Dr. Taein Shin received the Best Paper Award at DesignCon 2025.
- 2024 · IEEE EDAPS 2024 Best Paper Award: Master student Taesoo Kim received the Best Paper Award at EDAPS 2024.
- 2022 · DesignCon 2022 Best Paper Awards: Four Ph.D students, Seongguk Kim, Taein Shin, Seonguk Choi, and Haeyeon Kim, received Best Paper Awards on Feburary 1st, 2023.
- 2022 · IEEE EDAPS 2022 Best Poster Award: Hyunwoo Kim, a master student, received Best Poster Paper Award.
- 2022 · IEEE EPEPS 2022 Best Poster Award: Doctor Hyunwook Park received Best Poster Award.

## 소식

첫 화면에 오른 2022년 이후의 글과 자료 안내 15건이다. 첫 화면은 글마다 게시 날짜를 적지 않아, 앞의 연도는 제목이나 본문에 적힌 연도이고 연월일은 본문이 적은 날짜다. 문장은 게시된 그대로다.[^home]

- 2026 · 2026 TeraLab Openclaw Workshop for Semiconductor Design
- 2026 · 2026 TeraLab Future of HBM, HBF and HBS
- 2026 · 2026 HBF Workload and Roadmap
- 2026 · Technical Seminar on SI/PI/TI Analysis for Next Generation HBM ／ 2026 EE745
- 2025 · 2025 Teralab Next-Gen. HBM Roadmap
- 2025 · Agent AI for Engineering Applications ／ 2025 EE847 Student Project Presentation
- 2025 · 2025 Teralab Next-Gen. HBM Roadmap Seminar
- 2025 · 2025 Teralab DeepSeek Workshop: Slides on DeepSeek Technical Review Workshop by Teralab
- 2025 · DesignCon 2025 Acceptance: Four papers by Dr. Taein Shin, Ph.D students Keeyoung Son, Haeyeon Kim, and a master student, Hyunjun An, got accepted to DesignCon 2025.
- 2024 · IEEE EPEPS 2024 Acceptance: 9 papers by Dr. Taein Shin, Ph.D students, Keunwoo Kim, Keeyoung Son, Haeyeon Kim, Junghyun Lee, and master students, Hyunah Park, Haeseok Suh, Jungmin Ahn and Huynjun An, got accepted to EPEPS 2023.
- 2024-07-04 · Naver-Intel-KAIST AI Research Center: NIK AI research center kick-off workshop held in Daejeon on July 4, 2024.
- 2023 · ICML 2023 Acceptance: Ph.D student, Haeyeon Kim's first authored paper "DevFormer: A Symmetric Transformer for Context-Award Device Placement" got accepted to ICML 2023.
- 2022-01-12 · KAIST Cross-Generation Collaborative Lab: Opening ceremony for KAIST cross-generation collaborative lab was held on January 12, 2022.
- 2022 · Teralab Missouri S&T and Georgia Tech Visiting Seminar 2022
- 2022 · KAIST & SK Hynix Invited Seminar on AI-based Design 2022

## 연락과 위치

- 위치: S112 (1F), NanoFab (E19), KAIST Daejeon Campus[^contact]
- 전화: 연구실 +82-42-350-5458, +82-42-350-9866~9878, 팩스 +82-42-350-8058[^contact], 교수 +82-42-350-3458[^prof]
- 교수 이메일: joungho@kaist.ac.kr[^prof][^eeprof]
- 연구실 대표 연락: Haeseok Suh (haeseoksuh@kaist.ac.kr)[^contact]
- Contact & Location 페이지는 「27년도 봄학기 반도체공학대학원 석사과정 모집 중」이라고 안내한다.[^contact]
[^p1]: K. Son 외, J. Kim, IEEE Transactions on Components, Packaging and Manufacturing Technology 12, 1542-1556 (2022). <https://doi.org/10.1109/tcpmt.2022.3201673> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: G. Park 외, J. Kim, IEEE Transactions on Electromagnetic Compatibility 63, 1562-1573 (2021). <https://doi.org/10.1109/temc.2021.3059846> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: H. Park 외, J. Kim, IEEE Transactions on Microwave Theory and Techniques 70, 4772-4786 (2022). <https://doi.org/10.1109/tmtt.2022.3202221> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: H. Kim, M. Kim, F. Berto, J. Kim, J. Park, Proceedings of the 40th International Conference on Machine Learning (ICML), PMLR 202, 16541-16566 (2023). <https://proceedings.mlr.press/v202/kim23h.html> 초록 기준(학회 논문집 페이지 게시 초록).
[^p5]: J. Park 외, J. Kim, IEEE Transactions on Components, Packaging and Manufacturing Technology 14, 681-692 (2024). <https://doi.org/10.1109/tcpmt.2024.3381342> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: J. Lee 외, J. Kim, IEEE Transactions on Electromagnetic Compatibility 67, 1781-1795 (2025). <https://doi.org/10.1109/temc.2025.3610342> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: S. Kim 외, J. Kim, IEEE Transactions on Components, Packaging and Manufacturing Technology 11, 1955-1970 (2021). <https://doi.org/10.1109/tcpmt.2021.3117071> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: T. Shin 외, J. Kim, IEEE Transactions on Components, Packaging and Manufacturing Technology 11, 1122-1136 (2021). <https://doi.org/10.1109/tcpmt.2021.3092740> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 연구실 누리집 첫 화면 <https://tera.kaist.ac.kr/> (Teralab Research Overview, Recent Updates, 로드맵·워크숍 자료 안내, 2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <https://tera.kaist.ac.kr/members/professor> (연락처, Education, Key Research, Education, and Professional Contributions, Career, Awards, 2026-10-23 열람)
[^rprof]: 연구실 누리집 Research Professor 페이지 <https://tera.kaist.ac.kr/members/research-professor> (2026-10-23 열람)
[^phd]: 연구실 누리집 Ph.D. Students 페이지 <https://tera.kaist.ac.kr/members/ph-d-students> (2026-10-23 열람)
[^ms]: 연구실 누리집 Master Students 페이지 <https://tera.kaist.ac.kr/members/master-students> (2026-10-23 열람)
[^alumni]: 연구실 누리집 Alumni 페이지 <https://tera.kaist.ac.kr/members/alumni> (Ph. D Alumni, M.S. Alumni, 2026-10-23 열람)
[^roadmap]: 연구실 누리집 Teralab HBM Milestone and Roadmap 페이지 <https://tera.kaist.ac.kr/researches/teralab-hbm-milestone-and-roadmap> (Kim's Law, HBM Milestone, HBM3–5 로드맵, 2026-10-23 열람)
[^pkg]: 연구실 누리집 Advanced Package Design 페이지 <https://tera.kaist.ac.kr/researches/advanced-package-design> (HBM, X-point Memory, Fan-out Wafer Level Package, Glass Interposer, Semiconductor Testing, 2026-10-23 열람)
[^aisipi]: 연구실 누리집 AI-based Optimal SI/PI Design in 3D ICs 페이지 <https://tera.kaist.ac.kr/researches/ai-based-optimal-sipi-design-in-3d-ics> (2026-10-23 열람)
[^nmc]: 연구실 누리집 Near Memory Computing in 3D ICs 페이지 <https://tera.kaist.ac.kr/researches/near-memory-computing-in-3d-ics> (Processing in Memory, Neuromorphic Chip, 2026-10-23 열람)
[^sipi]: 연구실 누리집 SI/PI/GI in 3D ICs 페이지 <https://tera.kaist.ac.kr/researches/sipigi-in-3d-ics> (TSV, Signal Integrity, Power Integrity and Ground Integrity, Circuit Design, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publications 메뉴: International Journals <https://tera.kaist.ac.kr/publications/international-journals>, International Conferences <https://tera.kaist.ac.kr/publications/international-conferences>, Domestic Journals <https://tera.kaist.ac.kr/publications/domestic-journals>, Domestic Conferences <https://tera.kaist.ac.kr/publications/domestic-conferences> (2026-10-23 열람)
[^proj]: 연구실 누리집 Funded Projects 페이지 <https://tera.kaist.ac.kr/projects/funded-projects> (2026-10-23 열람)
[^partners]: 연구실 누리집 Industry Collaboration Partners <https://tera.kaist.ac.kr/projects/industry-collaboration-partners>, International Collaboration Partners <https://tera.kaist.ac.kr/projects/international-collaboration-partners> 페이지 (2026-10-23 열람)
[^contact]: 연구실 누리집 Contact & Location 페이지 <https://tera.kaist.ac.kr/introduction/contact-location> (2026-10-23 열람)
[^eeprof]: KAIST 전기및전자공학부 교수 소개(김정호) <https://ee.kaist.ac.kr/professor/12152/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 이메일, 디비전, 2026-10-23 열람)

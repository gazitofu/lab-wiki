# 집적회로 및 시스템 연구실 (Integrated Circuits and Systems for Computing and Communication lab., IC3 Lab)

**서울대학교 공과대학 전기·정보공학부 · 최우석 부교수**

- 분야: 고속 메모리 연결 회로, 저전력 클럭 회로, 인공지능 계산 하드웨어, 암호화된 기계학습
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 집적회로 설계[^research][^p1], 고속 유선 인터페이스[^research][^p1][^p4], 메모리 내 연산[^research], AI 반도체·가속기[^research][^p5], 회로·설계 자동화(EDA)[^research], AI·기계학습 보안·프라이버시[^research][^p7][^p8]
- 누리집: [IC3 Lab](https://sites.google.com/view/ic3-snu/home), [최우석 교수](https://sites.google.com/view/wschoi)
- 근거와 출처: [읽은 자료와 확인 범위](ic3-sources.md)

> 칩과 메모리가 데이터를 주고받는 회로, 인공지능 계산용 회로, 데이터를 암호화한 상태로 계산하는 시스템을 연구한다.

## 무엇을 연구하나

IC3 Lab은 집적회로(전자 부품과 연결을 한 반도체 칩에 모은 회로)를 설계한다. 한쪽에서는 칩과 메모리(정보를 저장하는 장치) 사이의 데이터 전송을 다루고, 다른 쪽에서는 인공지능 계산을 수행하는 회로와 데이터를 드러내지 않는 계산 방법을 연구한다.[^home][^research]

고속 연결에서는 데이터를 촘촘한 배선으로 보내면서 생기는 누화(인접 전송로의 신호가 다른 전송로에 간섭하는 현상)를 줄이고, 수신한 데이터와 클럭(회로의 동작 시점을 맞추는 주기 신호)을 복원한다. 신호는 정보를 전달하는 물리량의 변화다. 서로 이웃한 배선의 간섭을 줄이는 신호 방식과 여러 전송로가 함께 쓰는 클럭 분배 회로가 대표적인 연구다.[^p1][^p2]

인공지능 쪽에서는 신경망(연결된 계산 단위들의 관계를 학습해 정보를 처리하는 모형)을 구현하는 회로와 동형 암호(Homomorphic Encryption, HE)를 연구한다. 동형 암호는 암호문을 해독하지 않고 계산해, 해독했을 때 원래 자료에 같은 계산을 한 결과를 얻는 암호 방식이다. 이를 이용해 입력 자료를 드러내지 않는 추론(학습한 모형으로 새 입력의 결과를 계산하는 과정) 시스템을 만든다.[^research][^p5][^p7]

## 주요 연구 주제

### 고밀도 메모리 연결

고대역폭 메모리(High Bandwidth Memory, HBM) 인터페이스(장치 사이에서 정보를 주고받는 연결 회로)를 연구한다. 대역폭은 통신 문맥에서 단위 시간에 전달할 수 있는 데이터의 양을 뜻한다. 데이터 패턴에 따른 잡음(원하는 정보와 무관한 신호의 변동)을 줄이는 부호화(정보를 정해진 기호나 신호 형태로 바꾸는 방법)와 전력(단위 시간에 소비하거나 전달하는 에너지의 양) 소비를 줄이는 기술을 다룬다. XMAS(Xtalk Minimizing Affine Signaling)는 촘촘한 연결에서 누화를 줄이는 신호 방식이다.[^research][^p1]

### 메모리 가까이에서 하는 계산

DRAM(Dynamic Random-Access Memory, 저장 내용을 유지하려면 주기적으로 다시 써야 하는 메모리)을 이용한 메모리 내 연산(Processing-In-Memory, PIM)을 연구한다. 메모리 내 연산은 자료를 저장한 곳이나 그 가까이에서 계산하는 방식이다. 전송 경로와 연결 회로를 설계해 인공지능과 대규모 자료 분석에 쓰이는 시스템의 처리 속도와 에너지 효율(사용한 에너지에 비해 유효한 일을 수행한 정도)을 개선하려 한다.[^research]

### 연결 회로의 성능 예측과 설계 자동화

송수신 회로의 성능을 모형으로 표현하고, 기계학습(자료에서 규칙을 배워 새 자료에 적용하는 계산 방법)을 이용해 성능을 예측한다. 연구실은 설계의 자동화와 최적화(정한 조건에서 목표에 맞는 설계 값을 찾는 과정)를 위한 틀도 개발한다.[^research]

### 클럭과 데이터 복원

클럭·데이터 복원(Clock and Data Recovery, CDR)은 받은 신호에서 데이터를 읽을 시점과 데이터 값을 찾는 과정이다. 여러 전송로에 클럭을 나누어 주는 회로와 수신 시점을 조절하는 방법을 설계한다. 확률적으로 외부 입력을 주입하는 발진기(반복되는 신호를 만드는 회로)의 잡음을 분석하는 연구도 한다.[^research][^p2][^p3]

### 인공지능 하드웨어

시스템 온 칩(System on Chip, SoC, 여러 시스템 기능을 한 칩에 모은 것)에서 인공지능 계산을 담당하는 모듈(특정 기능을 맡는 구성 단위)을 설계한다. 스파이킹 신경망(Spiking Neural Network, SNN)은 개별 펄스의 발생으로 정보를 처리하는 신경망이다. 펄스는 일정 시간 동안 나타나는 신호의 변화다. 시간으로 정보를 나타내는 인공 뉴런(신경세포의 정보 처리를 모형화한 계산 단위) 회로를 설계하고, 회로의 오차가 계산 결과에 미치는 영향과 보정 방법을 연구한다.[^research][^p5]

### 암호화된 신경망 계산

동형 암호를 이용하는 딥러닝(여러 단계의 계산 표현을 학습하는 신경망 기반 방법)의 추론·학습 절차를 설계하고 평가한다. 범용 계산 장치에서의 가속과 전용 집적회로 설계를 함께 연구한다. 합성곱은 입력의 위치를 옮겨 가며 정해진 가중치(입력이 결과에 기여하는 정도를 정하는 값)를 적용하고 합하는 연산이다. 이 연산을 암호문에 수행하는 방법, 참여자끼리 자료를 드러내지 않고 계산 결과를 얻는 절차가 대표적이다.[^research][^p6][^p7][^p8]

### 신경망으로 유선 신호 복원

유선 통신의 등화기(전송 과정에서 생긴 신호의 왜곡을 보상하는 처리 장치)를 신경망으로 설계한다. NeuralEQ는 수신 자료의 앞뒤 관계를 이용해 보낸 값을 추정하는 순방향·역방향 알고리즘을 모방한다. 실제 전송로를 이용한 모의실험(대상의 동작을 계산으로 재현하는 실험)으로 기존 등화 방법과 비교했다.[^research][^p4]

## 대표 논문

최우석 교수가 저자로 참여한 서울대 재직 시기의 연구에서 회로·클럭·신경망 하드웨어·암호화 계산 갈래를 골랐다. 아래의 연도와 판본은 표에 표시한 출처 기준이며, arXiv는 논문을 정식 출판 전에 공개하거나 수정본을 올리는 저장소다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문 | 쉽게 말하면 | 교수의 저자 위치 |
|---|---|---|---|---|
| 1 | 2024 | [A 0.65-pJ/bit 3.6-TB/s/mm I/O Interface with XTalk Minimizing Affine Signaling for Next-Generation HBM with High Interconnect Density](https://arxiv.org/abs/2404.05119) · arXiv 사전 공개본 | 촘촘한 칩 간 연결에서 이웃 배선의 간섭을 줄이는 XMAS 신호 방식을 제안했다. 작동 원리를 분석하고 수치 실험으로 비교했으며, 실제 송수신 회로를 제작해 누화와 여러 회로가 동시에 동작하며 생기는 잡음에 대한 특성을 검증했다.[^p1] | 8명 중 마지막 저자 |
| 2 | 2024 | [A 4x32Gb/s 1.8pJ/bit Collaborative Baud-Rate CDR with Background Eye-Climbing Algorithm and Low-Power Global Clock Distribution](https://arxiv.org/abs/2404.07021) · arXiv 사전 공개본 | 여러 전송로를 가진 수신기의 전력을 줄이는 클럭 분배 구조와, 데이터를 읽는 시점을 동작 중 조정하는 알고리즘을 제안했다. 실제 제작한 수신기에서 클럭의 주파수 차이를 보상하고 데이터 판별에 쓸 수 있는 여유를 늘렸다. 주파수는 신호가 일정 시간에 반복되는 횟수다.[^p2] | 8명 중 마지막 저자 |
| 3 | 2023 | [Phase Noise Analysis for Stochastically Injected Oscillators](https://doi.org/10.1109/TCSII.2023.3253558) · IEEE Transactions on Circuits and Systems II: Express Briefs | 클럭 생성 회로가 확률적으로 입력을 주입할 때 생기는 위상 잡음을 분석했다. 위상은 반복 신호가 한 주기의 어느 지점에 있는지를 나타낸다. 각 상태가 나타날 확률과 시간에 따른 신호의 상관관계를 이용해 잡음을 계산하고, 시간 영역 모의실험과 비교해 추정의 정확성을 확인했다.[^p3] | 2명 중 마지막 저자 |
| 4 | 2023 | [NeuralEQ: Neural-Network-Based Equalizer for High-Speed Wireline Communication](https://arxiv.org/abs/2308.02133) · arXiv 사전 공개본 | 신호 손실이 있는 유선 전송로에서 보낸 데이터를 복원하는 신경망을 제안했다. 순방향·역방향 알고리즘을 모방해 기존 등화기보다 비트 오류율을 개선하면서 그 알고리즘의 계산 복잡도를 줄였다. 비트는 정보를 나타내는 이진 자리이며, 비트 오류율은 전송한 비트 가운데 잘못 판별한 비트의 비율이다. 실제 전송로를 이용한 모의실험으로 평가했다.[^p4] | 5명 중 마지막 저자 |
| 5 | 2022 | [Energy-Efficient High-Accuracy Spiking Neural Network Inference Using Time-Domain Neurons](https://arxiv.org/abs/2202.02015) · AICAS 2022 채택을 밝힌 arXiv 판 | 스파이킹 신경망을 구현하는 인공 뉴런 회로를 제안했다. 입력을 누적한 뒤 조건에 따라 펄스를 내보내는 동작을 시간 영역에서 구현한다. 회로를 설계하고 모의실험해 추론의 오류율과 전력 소비를 평가했으며, 비교 대상인 기존 구현들에 비해 오류율과 전력 소비의 개선을 보고했다.[^p5] | 4명 중 마지막 저자 |
| 6 | 2024 | [Hyena: Optimizing Homomorphically Encrypted Convolution for Private CNN Inference](https://doi.org/10.1145/3676536.3676832) · ICCAD 2024 | 합성곱 신경망(Convolutional Neural Network, CNN)의 암호화된 추론에서 많은 시간을 차지하는 합성곱 계산을 개선했다. 가중치 저장과 여러 출력의 묶음 처리를 함께 고려한 곱셈 방법, 암호 설정 값 선택과 나머지 연산을 늦추는 최적화를 제안했다. 영상 분류 모형에서 전체 처리 시간, 메모리 사용량, 통신량을 줄였다.[^p6] | 2명 중 마지막 저자 |
| 7 | 2024 | [Flash: A Hybrid Private Inference Protocol for Deep CNNs with High Accuracy and Low Latency on CPU](https://arxiv.org/abs/2401.16732) · arXiv 확장판, 2025년 수정 | 동형 암호와 안전한 두 참여자 계산(Secure Two-Party Computation, 두 참여자가 서로의 입력을 드러내지 않고 결과를 계산하는 방식)을 결합했다. 자료 배치와 합성곱 계산을 개선하고 신경망의 활성화 함수(계산 단위의 입력을 출력으로 바꾸는 함수)를 다항식으로 바꾼 뒤 그에 맞춰 학습한다. 중앙 처리 장치(Central Processing Unit, CPU)에서 깊은 신경망의 비공개 추론 시간을 줄였다.[^p7] | 6명 중 마지막 저자 |
| 8 | 2026 | [Jaguar: Fast Private CNN Inference with Power-of-Two Homomorphic Arithmetic](https://arxiv.org/abs/2606.11827) · arXiv 사전 공개본 | 암호문 계산에 쓰는 수 체계를 바꾸어 합성곱과 계산 정밀도(계산에서 값의 자릿수를 구분하는 정도) 조절을 함께 개선했다. 합성곱의 곱셈 방법을 바꾸고, 암호문에서 값의 자릿수를 조절해 활성화 함수 뒤의 별도 절차를 없앴다. 영상 분류 신경망에서 기존 비공개 추론 시스템들과 처리 시간·통신량을 비교했다.[^p8] | 4명 중 마지막 저자 |

## 교수와 전문 분야

최우석 교수는 서울대학교에서 학사(2008)와 석사(2010)를, University of Illinois at Urbana-Champaign에서 전기·컴퓨터공학 박사(2017)를 받았다. 같은 대학에서 2017–2018년, Harvard University에서 2018–2020년 박사후연구원을 지냈고 2020년 3월 서울대에 부임했다. 연구실 소개는 2020–2024년 조교수, 2024년부터 부교수로 적는다.[^faculty][^people]

최근 연구에서 읽히는 전문 분야는 고밀도 유선 송수신 회로와 클럭 설계,[^p1][^p2] 회로 잡음의 수학적 분석,[^p3] 통신에 쓰이는 신경망과 신경망을 구현하는 회로,[^p4][^p5] 암호문을 이용한 신경망 계산의 알고리즘과 시스템이다.[^p6][^p7][^p8] 이 구분은 위 대표 논문 주제에 근거한 설명이다.

## 응용 분야

고속 메모리와 칩 간 통신, 인공지능·대규모 자료 분석을 위한 메모리 내 연산, 자료의 내용을 드러내지 않는 기계학습 시스템을 목표로 한다.[^research] 대표 논문은 고밀도 연결의 송수신 회로,[^p1] 여러 전송로를 가진 수신기,[^p2] 영상 분류 모형의 암호화된 추론[^p6][^p7][^p8]을 다룬다.

## 구성원

2026년 10월 27일 교수 누리집 Group과 연구실 PEOPLE에 게시된 박사후연구원·대학원생이다. 시작 학기와 연구 주제는 두 페이지의 표기를 따르며, 빈 칸은 게시된 값이 없는 칸이다.[^group][^people] 「대표 논문 참여」는 위 표의 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Kahyun Kim | 박사후연구원 | Spring 2026 | D2D interface, memory interface | cankkh0101@snu.ac.kr | 2 |
| Hyun-Seok Ahn | 박사과정 | Fall 2023 |  |  |  |
| Ha-Jung Park | 박사과정 | Fall 2022 | High Bandwidth Memory Interface | hajung.park@snu.ac.kr | 2 |
| Daehoon Na | 박사과정 | Spring 2023 | High-speed links | artrance@snu.ac.kr |  |
| Jeongeun Song | 박사과정 | Spring 2023 | Memory Interface | je3song@snu.ac.kr |  |
| Jia Park | 박사과정 | Spring 2022 | Energy Efficient CDR, AI Accelerator | jiariapark@snu.ac.kr | 2 |
| Yoona Lee | 박사과정 | Fall 2024 | Digital Signal Processing, Die-to-Die Interface | dbskeowkd@snu.ac.kr |  |
| Hyun-Seok Choi | 박사과정 | Spring 2023 | High-Speed Chiplet Interface | tonyc1541@snu.ac.kr | 4 |
| Jinhoon Hyun | 박사과정 | Spring 2025 | Memory Interface | hyun0750@snu.ac.kr |  |
| Jaesung Lee | 박사과정 | Fall 2023 | SNN, PIM Architecture | jslee0122@snu.ac.kr |  |
| Seunggu Jeon | 박사과정 | Spring 2024 | Edge Device NN Accelerator | seunggujeon@snu.ac.kr |  |
| Jusung Lee | 박사과정 | Spring 2023 | High-Speed Interface, Memory Interface | jusung@snu.ac.kr |  |
| Kwangyeon Lee | 박사과정 | Fall 2021 | High-Speed Interface | bill0401@snu.ac.kr |  |
| Giyeong Heo | 박사과정 | Spring 2022 | Memory Interface | kk6563@snu.ac.kr |  |
| Hankyoung Lee | 박사과정 | Spring 2024 | High-Speed Clocking Circuits | lhk4514@snu.ac.kr |  |
| Yewon Jeong | 박사과정 | Fall 2024 | Privacy-Preserving Machine Learning, Hardware Acceleration | yellowon518@snu.ac.kr | 8 |
| Yoochang Kim | 박사과정 | Fall 2026 | High-Density D2D Interface, Analog Circuit | yoochang@snu.ac.kr |  |
| Ilhuan Choi | 박사과정 | Spring 2025 | Analog Computing | idisian@snu.ac.kr |  |
| Yuna Hwang | 박사과정 | Spring 2025 | Low-Jitter & Energy-Efficient Clocking | dbsk5057@snu.ac.kr |  |
| Nayoung Jung | 박사과정 | Spring 2025 | privacy-preserving machine learning | 18170lanige@snu.ac.kr | 8 |
| Junhyung Kim | 석사과정 | Fall 2025 | D2D interface, memory interface | junhyung@snu.ac.kr |  |
| Jae Yeop Wang | 석사과정 | Fall 2025 | Digital Signal Processing | woduqakstp@snu.ac.kr |  |
| Jiwoo Jang | 석사과정 | Spring 2026 | High-Speed Interface | wkdwldn033107@snu.ac.kr |  |
| Hanhee Jung | 석사과정 | Spring 2026 | Analog CIM, Mixed-Signal IC Design | junghh_tb@snu.ac.kr |  |
| Jiwon Yoo | 석사과정 | Spring 2026 | Compute-in-Memory(CIM), AI Accelerator | jiwonyoo@snu.ac.kr |  |
| Sedong Han | 석사과정 | Fall 2026 | Low-power/noise clocking | tpehdwkd@snu.ac.kr |  |

구성원 개인의 선정·지원 기록으로 Jeongeun Song의 ADF Rising Stars(2023), Ilhuan Choi의 NRF Research Fellowship(2025)이 있다. Kahyun Kim은 Samsung Humantech Paper Award(2025)와 Outstanding PhD Dissertation Award(2026)를 받았다.[^group][^people]

## 졸업생과 연수 종료 구성원

교수 누리집의 Alumni 구획에 적힌 박사후연구원, 박사·석사 졸업생, 학부 연구생 기록이다. 한 사람이 여러 과정에 있으면 과정별로 별도 행이다. 기간은 서울대 부임 전인 2020년보다 앞선 시작 연도도 포함한다. 진로와 개인 수상·지원 표시는 누리집 표기다.[^group][^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 랩이 적은 수상 |
|---|---|---|---|
| Hyeri Roh | 박사후연구원 (2025-2026) | Samsung (Memory) |  |
| Sanghee Lee | 박사후연구원 (2023-2024) | SK hynix |  |
| Jin-Seok Heo | 박사 (2022-2026) | Samsung (Memory) |  |
| Shinhyun Jeong | 박사 (2019-2026) | SK hynix |  |
| Jaeyoon Kim | 박사 (2020-2026) | Samsung (Memory) |  |
| Kahyun Kim | 박사 (2023-2026) | SNU IC3 PostDoc | 개인 수상·지원: Samsung Humantech Paper Award, Outstanding PhD Dissertation Award |
| Hyunjun Park | 박사 (2020-2026) | Samsung (S.LSI) | 개인 수상·지원: SSSP Best Paper Award |
| Sanghyuk Seo | 박사 (2018-2026) | SK hynix |  |
| Hanseok Kim | 박사 (2021-2025) | Samsung (Foundry) |  |
| Jihee Kim | 박사 (2022-2025) | SK hynix | 개인 수상·지원: Samsung Humantech Paper Award, Outstanding PhD Dissertation Award |
| Hyeri Roh | 박사 (2020-2025) | SNU IC3 PostDoc | 개인 수상·지원: CEDA/ICCAD Travel Grant |
| Taehoon Kim | 박사 (2021-2025) | SK hynix |  |
| Sunki Cho | 석사 (2023-2025) | SK hynix |  |
| Minjeong Kim | 석사 (2023-2025) | SK hynix |  |
| Ung Seong Kim | 석사 (2023-2025) | Samsung |  |
| Haengbeom Shin | 석사 (2023-2025) | SK hynix |  |
| Jinsu Yeo | 석사 (2023-2025) | Samsung Research |  |
| Honggyoo Ahn | 석사 (2022-2024) | SK hynix |  |
| Yoona Lee | 석사 (2022-2024) | SNU IC3 PhD |  |
| Hyeok-Joon Choi | 석사 (2022-2024) | Samsung (Memory) |  |
| Inwoo Nam | 석사 (2021-2023) | Samsung (Memory) |  |
| Jiwon Shin | 석사 (2021-2023) | Georgia Tech PhD |  |
| Joonghyun Song | 석사 (2021-2023) | FADU |  |
| Sihyun Lee | 학부 연구생 (2024-2025) | MIT PhD |  |
| Jiho Yeon | 학부 연구생 (2021-2022) |  |  |
| Yeonsoo Jeon | 학부 연구생 (2020-2021) | UT Austin PhD |  |

## 최근 논문 목록

연구실 목록의 2021–2026년 연도 구역이다. 학술지·학회 이름은 누리집의 약칭이며, arXiv 줄은 사전 공개본이다. 같은 제목의 arXiv 판과 학술지판은 각각의 게시 기록으로 구분한다. 학회 이름과 연도만 있는 줄은 누리집 표기이고, 정식 출판이나 발표 상태를 뜻하지 않는다. Jaguar는 확인한 arXiv 판을 함께 적고, Flash는 누리집이 밝힌 arXiv 확장판을 표시했다. 저자 이름의 별표는 누리집 표시다.[^pubs][^p7][^p8]

**2026**

- Yewon Jeong\*, Nayoung Jung\*, Hyeri Roh, Woo-Seok Choi. "Jaguar: Fast private CNN inference with power-of-two homomorphic arithmetic". *NeurIPS（누리집 표기）, arXiv:2606.11827 사전 공개본*.
- Yoona Lee, Kahyun Kim, Jin-Seok Heo, Daehoon Na, Jeongeun Song, Woo-Seok Choi. "A 52-Gb/s/pin 0.337-pJ/bit capacitively driven PAM-4 transceiver for coupling-variation-tolerant die-to-die Interfaces". *TCAS-II*.
- Jusung Lee, Sanghyuk Seo, Jaeyoon Kim, Suhwan Kim, Jaekwang Yun, Woo-Seok Choi. "A 19.8-Gb/s/wire single-ended PAM-3/NRZ simultaneous bidirectional transceiver with shared ZQ/hybrid calibration for memory interfaces". *TCAS-I*.
- Ilhuan Choi, Jiwon Yoo, Yoona Lee, Yewon Jeong, Jason Jaesung Lee, Woo-Seok Choi. "HARP: Hadamard-domain write-and-verify for noise-robust RRAM programming". *ICCAD*.
- Jin-Seok Heo, Yoona Lee, Kahyun Kim, Woo-Seok Choi. "A timing-relaxed split-phase decision-feedback equalizer with overlap-free boundary handling". *TCAS-II*.
- Sanghyuk Seo, Suhwan Kim, Giyeong Heo, Jaeyoon Kim, Hankyu Chi, Hyunkyu Park, Gyeongha Ryu, Jaekwang Yun, Woo-Seok Choi, Yong-Un Jeong. "A 0.53-pJ/bit 5x10Gb/s/pin single-ended transceiver with reconfigurable 4-aggressor crosstalk cancellation for HBM interfaces". *TCAS-I*.
- Jin-Seok Heo, Yoona Lee, Woo-Seok Choi. "A 0.093pJ/b/dB 20Gb/s ADC-based PAM4 receiver with 33dB loss compensation using time-interleaved charge-based subranging ADC". *TCAS-I*.
- Kahyun Kim, Yoona Lee, Daehoon Na, Ha-Jung Park, Jeongeun Song, Woo-Seok Choi. "A 0.292pJ/bit 56Gb/s/wire capacitively driven simultaneous bidirectional transceiver with PVT/mismatch tracking for XSR and D2D interfaces in 28nm CMOS". *ISSCC*.
- Kahyun Kim, Daehoon Na, Jeongeun Song, Ha-Jung Park, Jin-Seok Heo, Hyunjun Park, Jihee Kim, Hanseok Kim, Hyeri Roh, Jung-Hun Park, Woo-Seok Choi. "A 42Gb/s noise-tolerant single-ended clock-referenced PAM3 transceiver for chiplet interfaces". *JSSC*.

**2025**

- Hyunjun Park, Jiwon Shin, Hanseok Kim, Jihee Kim, Haengbeom Shin, Taehoon Kim, Hyeri Roh, Jung-Hun Park, Woo-Seok Choi. "A 0.65-pJ/bit 3.6-TB/s/mm I/O interface with XTalk minimizing affine signaling for next-generation HBM with high interconnect density". *TCAS-I*.
- Jihee Kim, Yunhee Lee, Hyun-Seok Choi, Yoona Lee, Sanghee Lee, Woo-Seok Choi. "A 2.5-48Gb/s 16.6ns turn-on time NRZ/PAM4 pulse-based rapid-on/off baud-rate CDR for mobile interfaces". *TCAS-II*.
- Jihee Kim, Jia Park, Jiwon Shin, Hanseok Kim, Kahyun Kim, Haengbeom Shin, Ha-Jung Park, Woo-Seok Choi. "A 4x32Gb/s 1.8pJ/bit collaborative baud-rate CDR with background eye-climbing algorithm and low-power global clock distribution". *JSSC*.
- Hyun-Seok Choi, Sunki Cho, Sanghee Lee, Hyeri Roh, Jeong-Eun Song, Honggyoo Ahn, Jihee Kim, Minchang Kim, Hankyu Chi, Deog-Kyoon Jeong, Woo-Seok Choi. "A 3ns idle-exit latency 0.28-28Gb/s/pin single-ended NRZ die-to-die interface with energy-efficient receiver and background noise compensation". *CICC*.
- Taehoon Kim, Minjeong Kim, Hankyu Chi, Byungjun Kang, Eunji Song, Woo-Seok Choi. "ML-based fast and accurate performance modeling and prediction for high-speed memory interfaces across different technologies". *DATE*.
- Hyeri Roh, Jinsu Yeo, Yeongil Ko, Gu-Yeon Wei, David Brooks, Woo-Seok Choi. "Flash: A hybrid private inference protocol for deep CNNs with high accuracy and low latency on CPU". *PPAI（누리집 표기）, arXiv 확장판*.
- Boram Kim, Hankyu Chi, Hyeongjun Ko, Sangyeon Byeon, Sungkwon Lee, Changhyun Pyo, Seulgi Kim, Byungjun Kang, Eunji Song, Kwangjin Na, Jinyoup Cha, Hyesoo Kim, Shinyoung Park, Woo-Seok Choi, Kyunghoon Kim, Hae-Kang Jung, Joohwan Cho, Jonghwan Kim. "A 42Gb/s single-ended hybrid-DFE PAM-3 receiver for GDDR7 memory interfaces". *ISSCC*.
- Kahyun Kim, Jung-Hun Park, Ha-Jung Park, Jia Park, Jihee Kim, Woo-Seok Choi. "A 0.275pJ/b 42Gb/s/pin clock-referenced PAM3 transceiver tolerant to supply noise, reference offset, and crosstalk for chiplets and short-reach memory interfaces". *ISSCC*.

**2024**

- Hyeri Roh, Woo-Seok Choi. "Hyena: Optimizing homomorphically encrypted convolution for private CNN inference". *ICCAD*.
- Jia Park, Jihee Kim, Sanghee Lee, Kahyun Kim, Ha-Jung Park, Woo-Seok Choi. "An 8GHz 9bit phase-rotating ILCM with DTC range reduction for high-speed serial links". *ESSERC*.
- Daehoon Na, Woo-Seok Choi, Seon-Kyoo Lee. "A 20-Gb/s 4-tap time-domain DFE with pulse width modulation for a DQ-DQS matched parallel receiver". *EL*.
- Jihee Kim, Jia Park, Jiwon Shin, Hanseok Kim, Kahyun Kim, Haengbeom Shin, Ha-Jung Park, Woo-Seok Choi. "A 4x32Gb/s 1.8pJ/bit collaborative baud-rate CDR with background eye-climbing algorithm and low-power global clock distribution". *arXiv*.
- Hyunjun Park, Jiwon Shin, Hanseok Kim, Jihee Kim, Haengbeom Shin, Taehoon Kim, Jung-Hun Park, Woo-Seok Choi. "A 0.65-pJ/bit 3.6-TB/s/mm I/O interface with XTalk minimizing affine signaling for next-generation HBM with high interconnect density". *arXiv*.

**2023**

- Hanseok Kim, Jae Hyung Ju, Hyun Seok Choi, Hyeri Roh, Woo-Seok Choi. "NeuralEQ: Neural-network-based equalizer for high-speed wireline communication". *arXiv*.
- Daeho Yun, Minsu Park, Kahyun Kim, Kyungmin Baek, Eonhui Lee, Woo-Seok Choi, Deog-Kyoon Jeong. "A PAM4 level mismatch adjustment scheme for 48-Gb/s PAM4 memory tester bridge". *A-SSCC*.
- Kwang-Hoon Lee, Jung-Hun Park, Yongjae Lee, Yeonggeun Song, Seungha Roh, Minkyo Shim, Yoonho Song, Woosong Jung, Young-Ha Hwang, Jonghyun Oh, Woo-Seok Choi, Deog-Kyoon Jeong. "A 0.99-pJ/b 10-Gb/s receiver with fast recovery from sleep mode under voltage drift". *TCAS-II*.
- Jiwon Shin, Joonghyun Song, Jihee Kim, Woo-Seok Choi. "A near-threshold ring-oscillator-based ILCM with edge-selective error detector achieving -64dBc reference-spur and -239dB FOM". *ESSCIRC*.
- Hyeri Roh, Woo-Seok Choi. "A context-aware readout system for sparse touch sensing array using ultra-low-power always-on event detection". *TCAS-II*.
- Jiwon Shin, Woo-Seok Choi. "Phase noise analysis for stochastically injected oscillators". *TCAS-II*.
- Kahyun Kim, Daeho Yun, Kyungmin Baek, Woo-Seok Choi, Deog-Kyoon Jeong. "A 48-Gb/s single-ended PAM-4 receiver with adaptive nonlinearity compensation". *ISCAS*.
- Taehoon Kim, Yoona Lee, Woo-Seok Choi. "Fast performance evaluation methodology for high-speed memory interfaces". *DATE*.

**2022**

- Hyun Jun Park, Woo-Seok Choi. "Performance variability modeling of analog circuits using improved orthogonal matching pursuit". *ISOCC*.
- Woo-Seok Choi, Brandon Reagen, Gu-Yeon Wei, David Brooks. "Impala: Low-latency communication-efficient private deep learning inference". *arXiv*.
- Daeho Yun, Eonhui Lee, Woosong Jung, Kahyun Kim, Kyungmin Baek, Jihee Kim, Hyunbae Lee, Byungsun Ko, Woo-Seok Choi, Deog-Kyoon Jeong. "A 32-Gb/s PAM4-binary bridge with sampler offset cancellation for memory testing". *TCAS-II*.
- Young-Ha Hwang, Jonghyun Oh, Woo-Seok Choi, Deog-Kyoon Jeong, Jun-Eun Park. "A residue-current-locked hybrid low-dropout regulator supporting ultralow dropout of sub-50mV with fast settling time below 10ns". *JSSC*.
- Yunhee Lee, Woonghee Lee, Minkyo Shim, Soyeong Shin, Woo-Seok Choi, Deog-Kyoon Jeong. "0.41-pJ/b/dB asymmetric simultaneous bidirectional transceivers with PAM-4 forward and PAM-2 back channels for 5-m automotive camera link". *VLSI*.
- Joonghyun Song, Jiwon Shin, Hanseok Kim, Woo-Seok Choi. "Energy-efficient high-accuracy spiking neural network inference using time-domain neurons". *AICAS*.
- Hyojun Kim, Woosong Jung, Kwandong Kim, Sungwoo Kim, Woo-Seok Choi, Deog-Kyoon Jeong. "A low-jitter 8-GHz RO-based ADPLL with PVT-robust replica-based analog closed loop for supply noise compensation". *JSSC*.
- Moon-Chul Choi, Sanghee Lee, Seungha Roh, Kwangho Lee, Jonghyun Oh, Sungwoo Kim, Kwandong Kim, Woo-Seok Choi, Jaeha Kim, Deog-Kyoon Jeong. "A 2.5 - 32 Gb/s Gen 5-PCIe receiver with multi-rate CDR engine and hybrid DFE". *TCAS-II*.
- Hanseok Kim, Woo-Seok Choi. "Improving spiking neural network accuracy using time-based neurons". *ISCAS*.
- Woonghee Lee, Minkyo Shim, Yunhee Lee, Heejin Yang, Soyeong Shin, Woo-Seok Choi, Deog-Kyoon Jeong. "Area and power efficient 10B6Q PAM-4 DC balance coder for automotive camera link". *TCAS-II*.

**2021**

- Woonghee Lee, Minkyo Shim, Yunhee Lee, Heejin Yang, Han-Gon Ko, Woo-Seok Choi, Deog-Kyoon Jeong. "0.37-pJ/bit/dB PAM-4 transmitter and adaptive receiver with fixed data and threshold levels for 12-m automotive camera link". *ESSCIRC*.
- Brandon Reagen\*, Woo-Seok Choi\*, Yeongil Ko, Vincent T. Lee, Hsien-Hsin S. Lee, Gu-Yeon Wei, David Brooks. "Cheetah: Optimizing and accelerating homomorphic encryption for private inference". *HPCA*.

## 논문 수상

아래 연도는 누리집 논문 목록의 연도 구역 표기이고 수상 날짜는 게시되어 있지 않다. 2022년 구역의 두 논문 수상이며, 졸업생 표에 있는 개인 수상과 별도로 적는다.[^pubs]

- 2022 · ISOCC Best Paper Award(최우수 논문상): Performance variability modeling of analog circuits using improved orthogonal matching pursuit
- 2022 · AICAS Best Paper Award(최우수 논문상): Energy-efficient high-accuracy spiking neural network inference using time-domain neurons

## 연락과 위치

- 교수 이메일: wooseokchoi@snu.ac.kr.[^profhome][^people]
- 연구실: 서울특별시 관악구 관악로 1, 서울대학교 반도체공동연구소 설계연구관 104-1동 216호.[^home][^people]
- 교수 연구실: 서울대학교 301동 806호.[^faculty]

## 각주
[^home]: IC3 Lab, HOME. <https://sites.google.com/view/ic3-snu/home> 연구 주제와 연구실 위치.
[^profhome]: Woo-Seok Choi, 교수 누리집 첫 화면. <https://sites.google.com/view/wschoi> 부교수 직위, 연구 관심, 교수 이메일.
[^research]: IC3 Lab, RESEARCH. <https://sites.google.com/view/ic3-snu/research> 메모리 연결 회로, 메모리 내 연산의 전송 경로·회로, 성능 모형과 설계 자동화, 클럭·데이터 복원, 인공지능 가속 모듈·전용 회로, 동형 암호 기반 추론·학습 절차, 신경망 등화기 연구 소개.
[^people]: IC3 Lab, PEOPLE. <https://sites.google.com/view/ic3-snu/people> 교수의 경력, 구성원·개인 수상과 학교 이메일, 졸업생과 연구실 위치.
[^group]: Woo-Seok Choi, Group. <https://sites.google.com/view/wschoi/group> 과정별 현재 구성원과 시작 학기, 졸업·연수 종료 기록과 개인 수상·진로.
[^pubs]: IC3 Lab, PUBLICATION. <https://sites.google.com/view/ic3-snu/publication> 연도별 논문 목록과 논문 수상 표기.
[^faculty]: 서울대학교 전기·정보공학부, 최우석 부교수 소개. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p840> 학력·경력·전공·교수 연구실.

[^p1]: H. Park 외, W.-S. Choi, arXiv:2404.05119 (온라인 2024-04-08). <https://arxiv.org/abs/2404.05119> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2404.05119>.
[^p2]: J. Kim 외, W.-S. Choi, arXiv:2404.07021 (온라인 2024-04-10). <https://arxiv.org/abs/2404.07021> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2404.07021>.
[^p3]: J. Shin, W.-S. Choi, IEEE Transactions on Circuits and Systems II: Express Briefs PP, 1-1 (2023). <https://doi.org/10.1109/TCSII.2023.3253558> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/369073253_Phase_Noise_Analysis_for_Stochastically_Injected_Oscillators>. 권·쪽은 등록 페이지의 임시 표기다.
[^p4]: H. Kim 외, W.-S. Choi, arXiv:2308.02133 (온라인 2023-08-04). <https://arxiv.org/abs/2308.02133> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2308.02133>.
[^p5]: J. Song, J. Shin, H. Kim, W.-S. Choi, arXiv:2202.02015 (온라인 2022-02-04). <https://arxiv.org/abs/2202.02015> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2202.02015>.
[^p6]: H. Roh, W.-S. Choi, IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2024) (온라인 2023-11-21). <https://doi.org/10.1145/3676536.3676832> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2311.12519>. 온라인 날짜는 arXiv 최초 공개일이며, 같은 페이지가 ICCAD 2024 판과 그 DOI를 밝힌다.
[^p7]: H. Roh 외, W.-S. Choi, arXiv:2401.16732 (온라인 2024-01-30). <https://arxiv.org/abs/2401.16732> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2401.16732>.
[^p8]: Y. Jeong, N. Jung, H. Roh, W.-S. Choi, arXiv:2606.11827 (온라인 2026-06-10). <https://arxiv.org/abs/2606.11827> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2606.11827>.

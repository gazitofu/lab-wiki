# 전력변환시스템 연구실 (Power Conversion Systems Laboratory, PCSL)

**서울대학교 공과대학 전기·정보공학부 · 최성휘 부교수**

- 대분야: 전기전자·반도체·광학, 에너지·환경·지구
- 태그: 제어 이론·제어 공학[^p1][^p2][^p7], 전기차[^home], 열전달·열관리[^p6][^home], 전력전자 변환기·전력 변환 시스템[^p4], 전동기·발전기 설계·구동 제어[^p7]
- 홈페이지: <https://pcsl.snu.ac.kr/>
- 교수 이메일: cuish@snu.ac.kr[^team]

> 전력망과 전기차·선박·가전 사이에서 전기를 바꾸어 전달하는 회로와 제어 방법을 연구한다. 고장이 나도 전력을 전달하는 다단 변환기, 전력망의 전압을 만드는 제어, 직류 변환기의 효율과 모터 구동이 주요 주제다.

## 무엇을 연구하나

PCSL은 전력 변환기(전압·전류 또는 전기의 형태를 바꾸는 회로)의 구조와 제어를 연구한다. 교류(전류의 방향과 크기가 주기적으로 변하는 전기)와 직류(전류가 한 방향으로 흐르는 전기)를 서로 바꾸거나 직류 전압을 바꾸어, 전력망·재생에너지 설비·에너지 저장 장치와 연결한다. 학과 소개는 스마트 빌딩과 데이터 센터의 전력 전달, 전기차와 전기 추진 선박의 구동을 응용 대상으로 든다.[^home][^lab]

전력망 쪽에서는 모듈형 다단 변환기(MMC, Modular Multilevel Converter, 여러 회로 단위를 연결해 여러 단계의 전압을 만드는 변환기)와 그리드 포밍(GFM, Grid-Forming, 변환기가 전력망의 전압과 주파수 기준을 형성하는 제어)을 다룬다. 예를 들어 양극성 직류망(기준점에 대해 양·음 전압을 함께 사용하는 전력망)의 한쪽에 고장이 나도 다른 쪽을 제어하는 방법을 제안한다. 전류를 제한하는 동안 전압을 형성하는 기능을 유지하고, 전력망에 문제가 생긴 뒤에도 안정적으로 운전하는 제어가 연구 대상이다.[^p1][^p2]

직류 변환기에서는 듀얼 액티브 브리지(DAB, Dual-Active Bridge, 변압기 양쪽의 능동 스위치 회로로 전력을 주고받는 변환기)의 효율과 동특성(시간에 따라 입력이나 부하가 변할 때 나타나는 반응)을 연구한다. 전력 반도체가 켜지고 꺼지는 순간의 손실을 줄이는 제어와, 전달할 전력이 급변할 때 변압기 내부의 자속(자기장이 면을 통과하는 정도를 나타내는 양)을 제어하는 방법을 함께 다룬다. 서로 다른 변조(원하는 전압·전류를 만들기 위해 스위치 동작을 정하는 방법)를 같은 제어 법칙으로 연결하는 것도 주요 과제다.[^p4][^p5]

모터 구동과 전력 반도체의 운전도 연구한다. 첫 화면은 전기차 모터의 센서리스 제어(직접 측정하는 센서 없이 필요한 상태를 추정해 제어하는 방법), 운전 범위 확장, 인버터(직류를 교류로 바꾸는 회로)의 능동 열관리를 연구 주제로 올린다. WBG(Wide-Band-Gap, 전자가 전도에 참여하려면 넘어야 하는 에너지 간격이 넓은 반도체) 소자를 쓰는 변환기와 구동 회로, 온도 추정, 상태 감시와 신뢰성도 다룬다. 대표 논문에서는 소자 사이의 열 불균형을 줄이면서 변압기 자속 포화(자기장을 증가시켜도 자속의 증가가 제한되는 현상)를 피하는 운전을 제안했다.[^home][^p6]

## 주요 연구 주제

### 전력망을 형성하는 변환기의 안정성

전력망에 연결된 변환기는 고장 때 전류를 제한하면서도 그리드 포밍 기능을 유지해야 한다. 대표 논문 2는 전압 제어기의 이득(입력 변화에 대한 출력 변화의 비율)을 조절해 가상 임피던스(제어로 구현한 교류 전압·전류 사이의 관계)를 바꾸는 방법을 제안했다. 전류 제한 중의 과도 안정성(고장 같은 큰 변화 뒤에도 운전 상태가 유지되거나 회복되는 성질)과 전압 형성 기능을 개선하고 실험으로 검증했다.[^p2]

가상 임피던스 자체가 불안정을 만들 수 있는 조건도 분석한다. 대표 논문 3은 미분 항을 생략한 구현에서 역상 성분(세 상의 정상적인 회전 순서와 반대인 전압·전류 성분)이 어떤 영향을 받는지 조사했다. 이 성분에서 용량성 거동(전하를 저장하는 요소가 갖는 전압·전류 관계)이 나타나 특정 공진 주파수 부근의 고조파(기본 주파수의 정수배인 성분) 전류가 커질 수 있고, 제어 지연이 불안정을 일으킬 수 있음을 분석하고 실험했다.[^p3]

### 직류 변환기의 효율과 동특성

대표 논문 4는 영전압 스위칭(ZVS, Zero-Voltage Switching, 스위치 양단 전압이 영인 상태에서 전환하는 동작)을 만족시키면서 전류의 실효값을 최소화하는 변조를 제안했다. MOSFET(Metal-Oxide-Semiconductor Field-Effect Transistor, 절연된 전극의 전압으로 전류를 조절하는 트랜지스터)의 기생 용량(회로가 의도하지 않아도 구조상 생기는 전하 저장 성질)과 전환 중 회로의 변화를 반영해 동작 조건을 계산한다. SiC(Silicon Carbide, 탄화규소) 소자를 쓴 변환기를 제작해 방법을 검증했다.[^p4]

전달 전력이 급변할 때에는 효율을 정하는 변조와 동적 제어를 함께 맞춰야 한다. 대표 논문 5는 순간 펄스 패턴 제어(IPPC, Instantaneous Pulse Pattern Control, 스위치에 인가하는 펄스 배열을 순간적으로 정하는 제어)를 제안했다. 두 변조 방식을 자속 제어 문제로 표현해 하나의 제어 법칙으로 연결했고, 변조 방식과 관계없이 과도 시간을 스위칭 주기의 6분의 1까지 줄였다고 보고했다. 이 결과는 시뮬레이션(대상의 동작을 계산 모형으로 재현하는 시험)과 실험으로 확인했다.[^p5]

### 다단 변환기와 디지털 제어

대표 논문 1은 지그재그 변압기를 쓰는 MMC에서 양·음 극을 독립적으로 제어하는 방법이다. 위·아래 암(회로 단위들을 연결한 변환기의 가지)의 전류와 에너지 균형 제어를 나누고, 한 극의 고장 때 제어 모드를 전환한다. 제어기와 계산 모형을 연결하는 시험, 축소 변환기·변압기 실험으로 한쪽 극 차단과 교류 접지 고장 조건의 동작을 검증했다.[^p1]

대표 논문 8은 샘플링(일정한 시점마다 신호 값을 읽는 과정) 간격이 달라지는 제어의 디지털 필터(읽은 신호에서 필요한 성분을 골라내는 계산 방법)를 다룬다. 현재 간격뿐 아니라 이전 측정 간격이 필터 응답에 미치는 영향도 반영하는 이산화(연속적인 수학식을 시간 간격별 계산식으로 바꾸는 과정)를 제안했다. 주파수 응답 분석과 단상 교류·직류 변환기 실험으로 기존 방식과 비교했다.[^p8]

### 모터 구동과 소자 열 균형

영구자석 동기 전동기(회전자의 자석과 회전 자기장이 같은 속도로 회전하는 모터)는 운전 조건에 따라 서로 다른 전압 생성 방식을 사용한다. 대표 논문 7은 공간 벡터 변조(세 상의 전압을 벡터로 나타내 스위치 동작을 정하는 방법)와 6스텝 운전(한 전기적 회전 주기를 여섯 구간으로 나누어 스위치를 동작시키는 방식)을 연결하는 모델 예측 제어(MPC, Model Predictive Control, 모형으로 미래 반응을 계산해 입력을 정하는 제어)를 제안했다. 계산 방법을 바꾸어 연산 부담을 줄이고 시뮬레이션과 실험으로 검증했다.[^p7]

변환기의 스위치에 걸리는 열 부담도 균등하게 만든다. 대표 논문 6은 삼상 DAB에서 위·아래 스위치의 전류를 교환해 열 균형을 맞출 때 변압기 자속 포화가 생길 수 있다는 문제를 다뤘다. 스위치 구동 신호의 반전과 각 상 전압을 적용하는 순서의 반전을 함께 사용해, 열 균형을 맞추면서 자속 포화를 피하는 방법을 제안하고 실험했다.[^p6]

## 대표 논문

교수가 저자이고 서울대 부임 뒤인 2023–2026년의 연구 가운데 위 네 갈래를 보여 주는 8편을 골랐다. 연도는 랩 논문 목록과 대조했으며, 8번의 2024년은 랩 목록의 연도 구역이다. "쉽게 말하면" 칸은 각 논문의 ResearchGate 등록 초록만을 근거로 썼다. 저자 역할은 순서에 근거하며, 교신저자 표기는 랩이 이를 명시한 7번에만 붙였다.[^team][^ij]

| 번호 | 연도 | 논문 | 쉽게 말하면 | 교수 역할 |
|---|---|---|---|---|
| 1 | 2026 | [Fault-Tolerant Independent Pole Control Scheme of Zigzag MMC for Bipolar MVDC Distribution Systems](https://doi.org/10.1109/TPEL.2026.3655014) · IEEE Transactions on Power Electronics | 양·음 극으로 전력을 보내는 직류 배전망에서 한쪽 고장이 다른 쪽의 운전에 번지는 문제를 다룬다. MMC의 위·아래 가지에 있는 전류 제어와 에너지 균형 제어를 분리하고, 고장 때 기준값 계산을 바꾸어 제어 모드를 전환한다. 제어기와 모형을 연결한 시험과 축소 장치 실험으로 한쪽 극 차단·접지 고장 조건에서 검증했다.[^p1] | 마지막 저자 |
| 2 | 2025 | [Adjustable Virtual Impedance via Anti-windup Method for Enhancing Transient Stability and Grid-Forming Capability Under Current Limiting Conditions](https://doi.org/10.1109/TPEL.2025.3525649) · IEEE Transactions on Power Electronics | 전력망 고장으로 전류를 제한할 때에도 변환기가 전압을 형성하도록 제어한다. 전압 제어기의 두 겹 제어와 적분값의 누적을 억제하는 방법을 결합하고, 조절 가능한 이득으로 가상 임피던스의 성질을 바꾼다. 정상·이상 상태 사이의 운전을 연결하면서 안정성과 전력망 형성 능력을 높이는 방법을 제안하고 실험했다.[^p2] | 4명 중 세 번째 저자 |
| 3 | 2025 | [Identification of Resonance and Instability From Algebraic Virtual Impedance of Grid-Forming Control in the Perspective of Negative Sequence](https://doi.org/10.1109/TPEL.2025.3571387) · IEEE Transactions on Power Electronics | 가상 임피던스를 미분 항 없이 구현했을 때 생기는 문제를 분석한다. 역상 성분에서 용량성 거동이 나타나 특정 공진 주파수 근처에서 고조파 전류가 커질 수 있음을 밝혔다. 제어 지연 때문에 불안정해질 수 있는 조건도 분석하고 실험으로 이론을 검증했다.[^p3] | 마지막 저자 |
| 4 | 2025 | [ZVS-Enhanced and RMS-Current-Minimized Optimal Modulation Scheme of Dual-Active Bridge Converter With Comprehensive ZVS Analysis](https://doi.org/10.1109/TPEL.2025.3541847) · IEEE Transactions on Power Electronics | DAB에서 불필요하게 순환하는 전류를 줄이면서 스위치가 영전압에서 전환하도록 한다. 소자의 기생 용량이 전압에 따라 달라지는 특성과 스위치 전환 중 회로 변화를 반영해 조건을 계산하고 최적화했다. 제작한 SiC 기반 변환기에서 최대 효율 98.8%를 보고했다.[^p4] | 마지막 저자 |
| 5 | 2025 | [Instantaneous Pulse Pattern Control for Optimized Dynamic Performance of Three-Phase Dual-Active Bridge Converter](https://doi.org/10.1109/TPEL.2025.3543493) · IEEE Transactions on Power Electronics | 삼상 DAB에서 전력이나 전압이 바뀔 때의 반응을 제어한다. 기존 방식은 변조 전환 종류에 따라 다른 법칙을 사용했지만, 제안한 IPPC는 두 변조 방식을 자속 제어 문제로 묶어 같은 법칙을 적용한다. 변조 방식과 관계없이 과도 시간을 스위칭 주기의 6분의 1까지 줄였고 시뮬레이션과 실험으로 검증했다.[^p5] | 3명 중 두 번째 저자 |
| 6 | 2025 | [Enhanced Active Thermal Balancing Strategy for Three-Phase Dual-Active Bridge Converter Suppressing Transformer Flux Saturation](https://doi.org/10.1109/TPEL.2024.3517534) · IEEE Transactions on Power Electronics | 적은 전력을 전달하는 삼상 DAB의 변조에서는 스위치 사이에 열 불균형이 생길 수 있다. 기존 열 균형 제어가 변압기의 자속 최댓값을 높이는 문제를 다루고, 구동 신호뿐 아니라 상 전압을 적용하는 순서도 번갈아 뒤집는 방법을 제안했다. 자속 포화를 피하면서 열 균형을 맞추는 동작을 실험으로 검증했다.[^p6] | 마지막 저자 |
| 7 | 2023 | [Model Predictive Control for Six-Step Operation of PMSM Based on Adapted Fast Gradient Method](https://doi.org/10.1109/TPEL.2023.3240510) · IEEE Transactions on Power Electronics | 영구자석 동기 전동기가 공간 벡터 변조와 6스텝 운전 사이를 연속적으로 전환하도록 모델 예측 제어를 설계했다. 자속의 추정값과 기준 궤적에 따라 최적화 문제를 만들고 계산 방법을 바꿨다. 기존 방식과 비교해 기울기 계산 시간은 52%, 제약 조건에 맞추는 계산 시간은 9.1% 줄였다고 보고했다.[^p7] | 교신저자, 저자 순서는 4명 중 세 번째 |
| 8 | 2024(랩 연도 구역) | [Time-Step-Adaptive Filter Discretization for Variable Sampling Frequency Control of Power Converters](https://doi.org/10.1109/TPEL.2024.3465040) · IEEE Transactions on Power Electronics | 측정 간격을 바꾸면서 전력 변환기를 제어하면 디지털 필터도 그 변화에 맞춰야 한다. 이전 측정 간격이 현재 필터 응답에 미치는 영향을 반영하는 계산식을 제안했다. 주파수 응답과 단상 변환기 제어 실험에서 기존 이산화 방법과 비교했고, 가변 측정 주파수의 변환기·전동기 제어에 활용할 가능성을 제시했다.[^p8] | 마지막 저자 |

## 교수와 전문 분야

최성휘(Shenghui Cui) 부교수는 2012년 칭화대학교 전기공학 학사, 2014년 서울대학교 전기·정보공학부 석사, 2019년 아헨 공과대학교 전기공학 박사 학위를 받았다. 아헨 공과대학교에서 2015–2019년 Research Associate, 2019–2021년 Senior Scientist로 일했다. 학과 교수 소개는 서울대 부임을 2021년 9월로 적고, 랩 Team은 2021–2025년 조교수, 2025년부터 부교수로 적는다.[^prof][^team]

학과가 제시하는 관심 분야는 교류·직류 전력 계통용 변환기, 모터 구동, 전력망과 변환기의 연계, 재생에너지 변환과 에너지 저장 장치, 전력 반도체 소자 응용 기술이다.[^prof] 대표 논문으로 보면 전문 분야는 다단 변환기의 고장 대응과 디지털 제어, 전력망 형성 제어의 안정성 분석, 직류 변환기의 변조·자속·열 균형 제어, 영구자석 모터의 운전 제어로 이어진다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

랩은 고전압 직류 송전과 중·저전압 직류 배전, 선박 전력 시스템, 재생에너지·에너지 저장 장치용 변환기, 급속 충전소와 대규모 데이터 센터의 반도체 변압기(반도체 전력 변환 회로를 결합해 전력을 변환·제어하는 장치)를 연구 대상으로 든다. 전기차 모터의 운전 범위와 열관리, 가전용 전력 변환 회로도 응용 분야다.[^home][^lab]

산업 협력 사례로는 HD KSOE·경북대 ECSL과의 선박 전기 추진용 다단 변환기 구동 시스템, 삼성전자가 지원한 역률 보정(교류에서 공급 전력을 유효하게 사용하는 비율을 조절하는 기술) 변환기 개발, 차세대 직류망 시험을 위한 QAB(Quad-Active-Bridge, 변압기에 연결된 네 능동 스위치 회로 사이에서 전력을 주고받는 변환기) 시운전이 있다. 2024년에는 GaN(Gallium Nitride, 질화갈륨) 변환기의 액체 질소 내 동작을 알렸다.[^news]

## 구성원

2026년 10월 26일 Team 게시 기준으로 박사과정 후보 7명과 석사과정 후보 5명이다. 과정·시작 학기·연구 관심은 카드 표기이며, 학기 속 숫자의 띄어쓰기도 원문에 따른다. "대표 논문 참여"는 위 표 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^team]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Jisun Ham | 박사과정 | Fall(21' -) | Power Semiconductor Physics; AC-DC Converter; Cryogenic Power Electronics | wltjs917@snu.ac.kr |  |
| Jaeyeon Park | 박사과정 | Fall(23' -) | Motor Drive; Optimization and Control Theory; Modular Multilevel Converter | ok6530@snu.ac.kr | 1 |
| Dongjoon Kim | 박사과정 | Spring(22' -) | Modular Multilevel Converter; Grid Forming Control | totorokdj@snu.ac.kr | 1 |
| Junyeol Maeng | 박사과정 | Spring(22' -) | Grid Forming Control; Fault Circuit Interrupter; Cryogenic Power Electronics | junyul7@snu.ac.kr | 3 |
| Jaekeun Lee | 박사과정 | Spring(2 3' -) | AC-DC Converter; Grid Forming Control; Multi-Active Bridge Converter | jaek709@snu.ac.kr | 3 |
| Jiyu Lee | 박사과정 | Spring(2 4' -) | Grid Forming Control; Motor Drive | jiyu0805@snu.ac.kr |  |
| Seungjun Lee | 박사과정 | Spring(2 4' -) | Modular Multilevel Converter; Grid Forming Control | sj3mo@snu.ac.kr |  |
| Jin Yoo | 석사과정 | Fall(24' -) | 3-phase PFC rectifier; DC-DC converter | sb05111@snu.ac.kr |  |
| Jaesang Yoo | 석사과정 | Spring(2 5' -) | Modular Multilevel Converter; DC-DC Converter | js.yoo@snu.ac.kr |  |
| Yechan Eom | 석사과정 | Fall(25' -) | Modular Multilevel Converter; DC-DC Converter | dpcks0429@snu.ac.kr |  |
| Hyeongmin Kim | 석사과정 | Spring(2 6' -) | Modular Multilevel Converter; Grid Forming Control | hyeongmin.kim@snu.ac.kr |  |
| Minwoo Jeong | 석사과정 | Spring(2 6' -) | Grid Forming Control; Modular Multilevel Converter | minnwoo@snu.ac.kr |  |

## 졸업생과 이전 구성원

Team의 Alumni 3명과 Research Associates 구획의 이전 구성원 3명이다. 앞의 세 사람은 학위 취득 연월이며, 뒤의 세 사람은 랩이 게시한 참여 기간이다. 학위논문 제목은 Thesis and Dissertation 게시 목록을 연결했다.[^team][^thesis]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Seongmin Moon | M.S. (2026.02) |  | Implementation of Accelerated Simulation for MVDC Shipboard Power Systems in Fuel Cell based Electric Propulsion Ship |
| Gayoung Park | M.S. (2025.02) | Doctoral Program in Massachusetts Institute of Technology | Optimization of Modulation Scheme and Transformer Design of Dual-Active Bridge Converter for Improved Efficiency |
| Jonghun Yun | Ph.D (2024.08) | Postdoctoral Researcher in Karlsruhe Institute of Technology | Modulation Scheme and Dynamic Control for Improved Light-Load Operation of Three-Phase Multi-Active Bridge Converter |
| Younggi Lee | Ph.D · Research Associates (2025.04–2025.08) | HD Korea Shipbuilding & Offshore Engineering Inc |  |
| Hwigon Kim | Ph.D · Research Associates (2023.08–2024.05) | RIVIAN Automotive Inc. |  |
| Inhwi Hwang | M.S. · Research Associates (2022.03–2023.06) | Ph.D Course in University of Michigan |  |

## 최근 논문 목록 (2021–2026)

랩의 연도 구역 기준 국제 학술지 35편, 국제 학회 42편, 국내 학술지·학회지 6편, 국내 학회 14편으로 모두 97편이다. 2021년 구역에는 교수의 서울대 부임(2021년 9월) 전 논문이 섞여 있으므로 현재 서울대 랩에서 수행한 성과만을 뜻하지 않는다. 연도는 구역 기준이며 각 항목의 서지 연도와 다를 수 있다. 아래 목록은 랩이 게시한 저자·제목·서지이고, 국제 학회의 `et al.` 표기는 전체 저자 목록이 아니다.[^ij][^ic][^dj][^dc][^prof]

**2026**

- [국제 학술지] D. -J. Kim, J. Park, A. Junyent-Ferré and S. Cui, "Small-Signal Stability Analysis on Energy-Balancing Control of Modular Multilevel Converter Under Instantaneous Optimal Zero-Sequence Voltage Injection," in IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2026.3745827.
- [국제 학술지] J. Maeng, J. Ham, Y. Kim, J. Baek and S. Cui, "Selective Common-Mode Leakage Current Bypass for Mitigating GFCI Nuisance Tripping in Household Variable-Frequency Drives," in IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2026.3739226.
- [국제 학술지] S. -Y. Lee, J. Park, D. Kim, S. -K. Sul, S. Cui and J. -J. Jung, "Megawatt-Scale Partial PHIL Arm-Current Emulation for Submodule-Level Verification of MMC-Based Drives," in IEEE Journal of Emerging and Selected Topics in Power Electronics, doi: 10.1109/JESTPE.2026.3719385.
- [국제 학술지] J. Lee, Y. Lee, J. Yun, J. Lee,  H. Wu, J. -J. Jung and S. Cui, "Accelerated Transformer Energization Sequence for Black-Start by Grid-Forming Inverters With Active Flux Trajectory Shaping in the Stationary Reference Frame," in IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2026.3695564.
- [국제 학술지] J. Lee, S. Zhao, C. Jeong, K. Park and S. Cui, "Selective Active Zero-State Pulse-Width Modulation (AZSPWM) for Reduction of Common-Mode Voltage (CMV) of Three-Phase Inverter Considering Saturation of Filter Inductor," in IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2026.3684903.
- [국제 학술지] J. Park, D. -j. Kim, S. Lee and S. Cui, "Improved Decoupled Control of Modular Multilevel Converter under Constraint of Nearest Level Modulation via Disturbance Observer Design," in IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2026.3684833.
- [국제 학술지] S. Kim, K. -H. Kim, S. Cui and J. -J. Jung, "Transient Stability Analysis of Grid-Forming Converters with an Elliptical Current Limiter under Asymmetrical Grid Faults," in IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2026.3674342.
- [국제 학술지] J. Yun, J. Lee, G. D. Carne and S. Cui, "Instantaneous Pulse Pattern Control of Three-Phase Multi-Active Bridge DC-DC Converters," in IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2026.3670163.
- [국제 학술지] Giovanni De Carne, Georg Lauss, Salvatore D’Arco, Srdjan Srdic, Friedrich Wiegel, Giampaolo Buticchi, Panos Kotsampopoulos, Fargah Ashrafidehkordi, Felix Wald, Karl Schoder, Sebastian Hubschneider, Antonello Monti, Andrea Benigni, Alexandros Paspatis, Shenghui Cui, Jae-Jung Jung, Moazzam Nazir, Robert Cox, Kai Strunz, Veit Hagenmeyer, and Johan Enslin, "Power Hardware-In-the-Loop for Electrical Systems: from Research Experience to Guidelines for Industrial Testing", in IEEE Open Journal of Power Electronics, doi: 10.1109/OJPEL.2026.3666762.
- [국제 학술지] D. -J. Kim, J. Park, Y. Hong and S. Cui, "Fault-Tolerant Independent Pole Control Scheme of Zigzag MMC for Bipolar MVDC Distribution Systems," in IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2026.3655014.
- [국제 학회] J. Park and S. Cui, "Multicore Simulation for Large-Scale Power Electronics Circuits in PLECS," 2026 IEEE 27th Workshop on Control and Modeling for Power Electronics (COMPEL), Cambridge, United Kingdom, 2026
- [국제 학회] J. Lee, Y. Li, X. Wang, J. -J. Jung and S. Cui, "Simplified Virtual Impedance Implementation Without Sequence Decomposition for Independent Positive/Negative-Sequence Shaping in Grid-Forming Converters," 2026 International Power Electronics Conference (IPEC-Nagasaki 2026 - ECCE Asia), Nagasaki, Japan, 2026, pp. 1-6, doi: 10.23919/IPEC-Nagasaki2026-EC64663.2026.11597152.
- [국제 학회] J. Lee, J. -J. Jung and S. Cui, "Fast Black Start of Grid-Forming Inverters in Multi-Transformer Feeders via Simultaneous Accelerated Soft-Magnetization," 2026 International Power Electronics Conference (IPEC-Nagasaki 2026 - ECCE Asia), Nagasaki, Japan, 2026, pp. 1-6, doi: 10.23919/IPEC-Nagasaki2026-EC64663.2026.11597171.
- [국제 학회] J. Yoo, J. Ham and S. Cui, "Compensation Method for Current Asymmetry Induced by a DC-link Capacitor at Active 3rd-order Harmonic Injection Rectifier," 2026 International Power Electronics Conference (IPEC-Nagasaki 2026 - ECCE Asia), Nagasaki, Japan, 2026, pp. 1-6, doi: 10.23919/IPEC-Nagasaki2026-EC64663.2026.11596833.
- [국제 학회] J. Yun, J. Lee, G. De Carne and S. Cui, "Simplified Soft-Switching Constraints for High-Power Multi-Active Bridge Converters," 2026 International Power Electronics Conference (IPEC-Nagasaki 2026 - ECCE Asia), Nagasaki, Japan, 2026, pp. 1-6, doi: 10.23919/IPEC-Nagasaki2026-EC64663.2026.11596854.

**2025**

- [국제 학술지] Ki-Hyun Kim, Seongyeon Kim, Heng Wu, Shenghui Cui, Jae-Jung Jung,  "A fast IVS controller for grid-forming converters: Reducing the current-limiting period to enhance transient stability", in International Journal of Electrical Power & Energy Systems,  Volume 174,  2026,  111496,  ISSN 0142-0615,  https://doi.org/10.1016/j.ijepes.2025.111496.
- [국제 학술지] J. Park, D. Kim, S. Lee, J. -J. Jung, S. -K. Sul and S. Cui, "Partial Power-Hardware-in-the-Loop Test for In-Situ Dynamic and Steady-State Validation of a Single Submodule in a Megawatt-Scale MMC," in IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2025.3642797.
- [국제 학술지] Y. He, W. Zou, J. Hu, L. Zhang, and S. Cui and R. W. De Doncker,  "A Family of Symmetrical Integrated Synchronizations for Grid-Following and Grid-Forming Inverters," in IEEE Transactions on Power Electronics, doi:10.1109/TPEL.2025.3632840.
- [국제 학술지] J. Ham, H. Kim, J. Maeng and S. Cui, "Inverter Loss Reduction Method of Air Conditioners with Adjustable DC-link Voltage Control and Six-Step Operation," in IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2025.3627960.
- [국제 학술지] S. Zhao, J. Lee, S. Cui and J. -I. Ha, "Analysis of the Power Output Capabilities of Grid-Forming Inverters under Reactive Power Control Mode in Ultra-Weak Grid," in IEEE Journal of Emerging and Selected Topics in Power Electronics, doi: 10.1109/JESTPE.2025.3625922.
- [국제 학술지] J. -M. Kim, S. Cui and J. -J. J. Jung, "A New E-STATCOM Topology Based on Single-Star Multilevel Converter with Centralized Energy Storage and Zigzag Transformer," in IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2025.3618963.
- [국제 학술지] Junyeol Maeng, Jisun Ham, Gayoung Park, Jaeyeon Park, Heng Wu, Jae-Jung Jung, Shenghui Cui, "A supercapacitor size minimization and energy management strategy for E-STATCOM connected to weak grid", International Journal of Electrical Power & Energy Systems, Volume 172, 2025, 111174, ISSN 0142-0615, https://doi.org/10.1016/j.ijepes.2025.111174.
- [국제 학술지] J. Park, J. Ham, J. Maeng, C. Im, D. Seo, S. Hahn, and  S. Cui, "Equivalent Circuit Extraction of MI-HTS Coil including High-Frequency Region for Electromagnetic Transient Simulation with Voltage-Source Converter," in IEEE Transactions on Applied Superconductivity, doi: 10.1109/TASC.2025.3587992.
- [국제 학술지] J. Lee, J. Maeng, J. -J. Jung and S. Cui, "Identification of Resonance and Instability from Algebraic Virtual Impedance of Grid-Forming Control in the Perspective of Negative Sequence," in IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2025.3571387.
- [국제 학술지] S. Kim, K. -H. Kim, S. Cui and J. -J. Jung, "Adjustable Virtual Impedance via Anti-Windup Method for Enhancing Transient Stability and Grid Forming Capability Under Current Limiting Conditions," in IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2025.3525649.
- [국제 학술지] J. Yun, S. Cui and S. -K. Sul, "Instantaneous Pulse Pattern Control for Optimized Dynamic Performance of Three-Phase Dual-Active Bridge Converter," in IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2025.3543493.
- [국제 학술지] G. Park, H. Kim, B. -G. Cho and S. Cui, "ZVS-Enhanced and RMS-Current-Minimized Optimal Modulation Scheme of Dual-Active Bridge Converter With Comprehensive ZVS Analysis," in IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2025.3541847.
- [국제 학술지] J. Yun and S. Cui, "Enhanced Active Thermal Balancing Strategy for Three-Phase Dual-Active Bridge Converter Suppressing Transformer Flux Saturation," in IEEE Transactions on Power Electronics, vol. 40, no. 4, pp. 5014-5024, April 2025, doi: 10.1109/TPEL.2024.3517534.
- [국제 학회] J. Lee, J. Yun, J. Ham, J. Maeng, J. -J. Jung and S. Cui, "Enhanced Fault Current Supply Capability of Grid-Forming Converters Using Variable DC-Link Six-Step Operation," 2025 IEEE Energy Conversion Conference Congress and Exposition (ECCE), Philadelphia, PA, USA, 2025, pp. 1-5, doi: 10.1109/ECCE58356.2025.11260200.
- [국제 학회] S. Lee, J. Park, D. Kim and S. Cui, "Optimal Nearest-Level Modulation of MVDC-MMC with Decoupled Control for Lower Phase Current Total Harmonic Distortion," 2025 IEEE Energy Conversion Conference Congress and Exposition (ECCE), Philadelphia, PA, USA, 2025, pp. 1-5, doi: 10.1109/ECCE58356.2025.11259672.
- [국제 학회] J. Lee, J. Maeng, J. -J. Jung and S. Cui, "Integral-Proportional Grid-Forming Control with Adaptive SPC Strategy for Enhanced Active-Power Provision During Grid Disturbances," 2025 10th IEEE Workshop on the Electronic Grid (eGRID), Glasgow, United Kingdom, 2025, pp. 1-6, doi: 10.1109/eGRID63452.2025.11255213.
- [국제 학회] S. Moon, J. Park, D. Kim and S. Cui, "Generator Operation Strategy for Naval Vessels with MVDC Distribution in Combat Situations," 2025 IEEE Electric Ship Technologies Symposium (ESTS), Alexandria, VA, USA, 2025, pp. 149-153, doi: 10.1109/ESTS62818.2025.11152412.
- [국제 학회] J. Park et al., "MMC-Based High-Power Motor Emulator for Testing of Electrical Propulsion System," 2025 IEEE Electric Ship Technologies Symposium (ESTS), Alexandria, VA, USA, 2025, pp. 162-169, doi: 10.1109/ESTS62818.2025.11152450.
- [국제 학회] J. Yun, J. Park, S. Moon, G. De Carne and S. Cui, "Resource-Efficient Real-Time Simulation of Multi-Active Bridge Converters Using Modular Programming," 2025 IEEE Kiel PowerTech, Kiel, Germany, 2025, pp. 1-6, doi: 10.1109/PowerTech59965.2025.11180564.
- [국제 학회] J. Lee, J. Yun, J. Lee, H. Wu, J. -J. Jung and S. Cui, "Ultra-Fast Black-Start Method of the Grid-Forming Converter for Electronic Power Grids with Transformer Soft Magnetization," 2025 IEEE 16th International Symposium on Power Electronics for Distributed Generation Systems (PEDG), Nanjing, China, 2025, pp. 562-566, doi: 10.1109/PEDG62294.2025.11060300.
- [국제 학회] S. Kim, K. -H. Kim, S. Cui and J. -J. Jung, "Comparison of Equivalent Circuit Models of Circular Current Limiter According to Anti-Windup Methods in Grid-Forming Converter," 2025 IEEE 16th International Symposium on Power Electronics for Distributed Generation Systems (PEDG), Nanjing, China, 2025, pp. 545-549, doi: 10.1109/PEDG62294.2025.11060427.
- [국제 학회] J. Lee, J. -J. Jung and S. Cui, "Equivalent Virtual Inductance Method Without Differential Operation for Current-Limiting Control of Grid-Forming Converters," 2025 IEEE 16th International Symposium on Power Electronics for Distributed Generation Systems (PEDG), Nanjing, China, 2025, pp. 1-6, doi: 10.1109/PEDG62294.2025.11060241.
- [국제 학회] Junyeol Maeng, Shenghui Cui. Enhanced Current-Limiting Strategy of Grid-Forming Converter Considering Grid-forming Capability. The 26th European Conference on Power Electronics and Applications, GDR SEEDS France & EPE Association, Mar 2025, Paris, France. ⟨10.34746/epe2025-0167⟩. ⟨hal-05108344⟩
- [국제 학회] Jisun Ham, Junyeol Maeng, Chaemin Im, Dongsu Seo, Jaheum Koo, Shenghui Cui, et al.. Design Considerations and Validation of a GaN e-HEMT-Based Cryogenic Power Converter. The 26th European Conference on Power Electronics and Applications, GDR SEEDS France & EPE Association, Mar 2025, Paris, France. ⟨10.34746/epe2025-0166⟩. ⟨hal-05108337⟩
- [국내 학술지·학회지] 유진, 함지선, 맹준열 and 최성휘, "계통 전류의 고조파 저감을 위한 정류기 설계, 제어 방법 및 검증" 전력전자학회논문지, vol. 31, no. 1, pp. 44-48, 2026, doi: 10.6113/TKPE.2026.31.1.44.
- [국내 학술지·학회지] 맹준열, 정재정 and 최성휘, "E-STATCOM 기술 및 해외사례 소개" 전력전자학회지, vol. 30, no. 4, pp. 58-63, 2025
- [국내 학회] 이승준, 박재연, 김동준, 이승용, 정재정 and 최성휘, "EtherCAT MMC 제어 시스템 기반 유도기 가변속 드라이브 HILS 구현" in 전력전자학회 학술대회 논문집, 전력전자학회, 2025, pp. 64-66.
- [국내 학회] 문성민, 유재상, 윤종훈, 이지유 and 최성휘, "Input-Series Output-Parallel 쿼드-액티브 브릿지 컨버터의 균형 제어" in 전력전자학회 학술대회 논문집, 전력전자학회, 2025, pp. 249-251.
- [국내 학회] 유진, 함지선, 맹준열 and 최성휘, "계통 전류의 고조파 저감을 위한 정류기 제어 방법 및 검증" in 전력전자학회 학술대회 논문집, 전력전자학회, 2025, pp. 97-99.
- [국내 학회] 유재상, 문성민, 윤종훈, 유진 and 최성휘, "쿼드-액티브 브릿지 컨버터의 단순화된 전력 제어" in 전력전자학회 학술대회 논문집, 전력전자학회, 2025, pp. 359-361.

**2024**

- [국제 학술지] I. Hwang, J. Lee and S. Cui, "Time-Step-Adaptive Filter Discretization for Variable Sampling Frequency Control of Power Converters," in IEEE Transactions on Power Electronics, Sep. 2024, doi: 10.1109/TPEL.2024.3465040.
- [국제 학술지] K. -H. Kim, S. Cui and J. -J. Jung, "Current-Oriented Phase-Locked Loop Method for Robust Control of Grid-Connected Converter in Extremely Weak Grid," in IEEE Transactions on Power Electronics, June. 2024, doi: 10.1109/TPEL.2024.3419445.
- [국제 학술지] G. S. Song, S. Cui and M. J. -J. Jung, "Technique for Mitigating Voltage Ripple of DC-Link Capacitors in a Three-Level NPC Utilizing a Zigzag Transformer," in IEEE Transactions on Power Electronics, May. 2024, doi: 10.1109/TPEL.2024.3407954.
- [국제 학술지] C. Im, J. Ham, J. Maeng, G. Kim, S.-H. Park, J. Kim, J. Lee, G. Park, J. -T. Lee, K. Choi, U. Bong, S. Cui, S. Hahn, S. Lee, "Nonlinear Characteristics of Metal-Insulated REBCO Magnet Under Various Switching Frequencies of Half-Bridge Inverter Circuit," in IEEE Transactions on Applied Superconductivity, vol. 3 4, no. 5, pp. 1-6, Aug. 202 4, doi: 10.1109/TASC.2024.3370092.
- [국제 학회] Y. Chung, J. Lee, C. Lee, H. Kim, D. Kim and S. Cui, "Bipolar DC/DC Converter for HVDC to MVDC Connection with MMC and Zig-Zag Transformer," 2024 International Conference on HVDC (HVDC), Urumqi, China, 2024, pp. 129-133, doi: 10.1109/HVDC62448.2024.10723010.
- [국제 학회] J. Maeng, J. -J. Jung and S. Cui, "Enhanced Current-limiting Method for Grid-forming Converters based on Virtual Admittance Matrix," 2024 9th IEEE Workshop on the Electronic Grid (eGRID), Santa Fe, NM, USA, 2024, pp. 1-6, doi: 10.1109/eGRID62045.2024.10842930.
- [국제 학회] K. -H. Kim, S. Cui and J. -J. Jung, "A Novel Voltage based Synchronization Method for Maximum Power Factor Injection of Grid-Tied Converter in Extremely Weak Grid," 2024 9th IEEE Workshop on the Electronic Grid (eGRID), Santa Fe, NM, USA, 2024, pp. 1-5, doi: 10.1109/eGRID62045.2024.10842776.
- [국제 학회] J. Lee, J. Yun, H. Kim and S. Cui, "High-Fidelity FEA-Based Circuit Simulation for Multi-Active Bridge Converter," 2024 IEEE Energy Conversion Congress and Exposition (ECCE), Phoenix, AZ, USA, 2024, pp. 3765-3770, doi: 10.1109/ECCE55643.2024.10861206.
- [국제 학회] G. Park, H. Kim and S. Cui, "Optimization of Transformer Design Parameters of a 20kW SiC-Based Dual-Active Bridge Converter for Enhanced Efficiency," 2024 IEEE Energy Conversion Congress and Exposition (ECCE), Phoenix, AZ, USA, 2024, pp. 3034-3039, doi: 10.1109/ECCE55643.2024.10861215.
- [국제 학회] S. K o, S. Cui, and S.-K. Sul, “Instantaneous Optimal Zero-Sequence Voltage Injection of Modular Multilevel Converter for Maximum Output Voltage Synthesis”, 2024 IEEE International Power Electronics and Motion Control Conference (IPEMC 2024 - ECCE Asia) , Chengdu, China, 2024, doi : 10.1109/IPEMC-ECCEAsia60879.2024.10567192
- [국제 학회] D. Kim, S.-K. Sul, and S. Cui, “Indirect-Modulated MMC Current Control with Voltage Disturbance Estimation and Compensation”, 2024 IEEE International Power Electronics and Motion Control Conference (IPEMC 2024 - ECCE Asia) , Chengdu, China, 2024, doi : 10.1109/IPEMC-ECCEAsia60879.2024.10567926
- [국제 학회] Y. Kim, S. Cui and J. -J. Jung, "Balancing Control of Cluster Energy in Star-Connected Multilevel Power Conversion System Using Zigzag Transformer," 2024 IEEE Applied Power Electronics Conference and Exposition (APEC), Long Beach, CA, USA, 2024, pp. 1434-1440, doi: 10.1109/APEC48139.2024.10509341
- [국제 학회] J. Maeng, and S. Cui, “Enhanced Fault Ride-Through of Grid-Forming Converter with Extra Internal Voltage Source Rotation”, 2024 IEEE Applied Power Electronics Conference and Exposition (APEC) , Long Beach, CA, USA, 2024, doi : 10.1109/APEC48139.2024.10509523
- [국제 학회] G. Park, J. Park, S. Cui, and S.-K. Sul, “Nonlinear Optimization-Based Power-Voltage Control of Grid-Connected Converter in Weak Grid”, 2024 IEEE Applied Power Electronics Conference and Exposition (APEC) , Long Beach, CA, USA, 2024, doi: 10.1109/APEC48139.2024.10509166
- [국제 학회] J. Yun, S. Cui, and S.-K. Sul, “Generalized Instantaneous Dual Flux Control for Three-Phase Dual-Active Bridge Converter”, 2024 IEEE Applied Power Electronics Conference and Exposition (APEC) , Long Beach, CA, USA, 2024, doi: 10.1109/APEC48139.2024.10509056
- [국제 학회] J. Ham, H. Kim, J. Maeng, and S. Cui, “Vector Control of AC Motor in Six-Step Operation Based on Variable DC-Link Voltage”, 2024 IEEE Applied Power Electronics Conference and Exposition (APEC) , Long Beach, CA, USA, 2024, doi: 10.1109/APEC48139.2024.10509231
- [국제 학회] I. Hwang, J. Lee, and S. Cui, “Grid Voltage Sensorless Control of 3.2kW Bridgeless Totem-Pole PFC Converter with Pre-estimation and Seamless Mode-Transition”, 2024 IEEE Applied Power Electronics Conference and Exposition (APEC) , Long Beach, CA, USA, 2024, doi: 10.1109/APEC48139.2024.10509019
- [국제 학회] J. -M. Kim, S. Cui and J. -J. Jung, "A Star-Connected Multilevel Converter with Zigzag Transformer for E-STATCOM," 2024 Energy Conversion Congress & Expo Europe (ECCE Europe), Darmstadt, Germany, 2024, pp. 1-6, doi: 10.1109/ECCEEurope62508.2024.10751832
- [국제 학회] S. Kim, K. -H. Kim, S. Cui and J. -J. Jung, "Enhancement Methods for Transient Stability of Grid-Forming Converters with Low Damping," 2024 Energy Conversion Congress & Expo Europe (ECCE Europe), Darmstadt, Germany, 2024, pp. 1-7, doi: 10.1109/ECCEEurope62508.2024.10751947.
- [국내 학술지·학회지] 이재근, 황인휘 and 최성휘, "가변 스위칭 주파수를 활용한 단상 PFC의 전류 THD 최소화 PWM 기법" 전력전자학회논문지, vol. 29, no. 1, pp. 67-73, 2024, doi: 10.6113/TKPE.2024.29.1.67.
- [국내 학술지·학회지] 맹준열, 최성휘, "계통 연계형 그리드 포밍 컨버터의 Soft Start-up 기법" 전력전자학회논문지, vol. 29, no. 2, pp. 92-98, 2026, doi: 10.6113/TKPE.2024.29.2.92
- [국내 학술지·학회지] 함지선, 최성휘, "켈빈 소스를 포함하는 SiC MOSFET의 가전용 전력변환시스템 적용을 위한 부트스트랩 회로 설계" 전력전자학회논문지, vol. 29, no. 2, pp. 132-137, 2024, doi: 10.6113/TKPE.2024.29.2.132
- [국내 학회] 이승준(Seungjun Lee), 김동준(Dongjoon Kim), 박재연(Jaeyeon Park), 이승용(Seungyong Lee), 정재정(Jae-Jung Jung), 최성휘(Shenghui Cui), "Star형 EtherCAT 통신 구조 기반 MMC 제어 시스템 구현" in 전력전자학회 학술대회 논문집, 2024, pp. 2 23-2 25.
- [국내 학회] 이지유(Jiyu Lee), 맹준열(Junyeon Maeng), 최성휘(Shenghui Cui), "소신호 안정도 분석을 통한 그리드 포밍 컨버터의 유효 전력 제어기 설계 방법" in 전력전자학회 학술대회 논문집, 202 4, pp. 214-216.

**2023**

- [국제 학술지] J. -S. Hong, J. -I. Ha, S. Cui and J. Hu, "Topology and Control of an Enhanced Dual-Active Bridge Converter With Inherent Bipolar Operation Capability for LVDC Distribution Systems," in IEEE Transactions on Power Electronics, vol. 38, no. 10, pp. 12774-12789, Oct. 2023, doi: 10.1109/TPEL.2023.3297389. (Corresponding Author)
- [국제 학술지] J. Yun, J. Yoo, S. Cui and S. -K. Sul, "Model Predictive Control for Six-Step Operation of PMSM Based on Adapted Fast Gradient Method," in IEEE Transactions on Power Electronics, vol. 38, no. 5, pp. 5952-5962, May 2023, doi: 10.1109/TPEL.2023.3240510. (Corresponding Author)
- [국제 학회] J. Yun, S. Cui and S. -K. Sul, "Instantaneous Dual Flux Control for Three-Phase Dual-Active Bridge," 2023 IEEE Energy Conversion Congress and Exposition (ECCE), Nashville, TN, USA, 2023, pp. 2747-2751, doi: 10.1109/ECCE53617.2023.10361971.
- [국제 학회] I. Hwang, J. Lee and S. Cui, "Time-Step-Adaptive-Bilinear (TSAB) Second-Order Digital Filter Design for Variable Sampling Frequency Control of Power Converter," 2023 IEEE Energy Conversion Congress and Exposition (ECCE), Nashville, TN, USA, 2023, pp. 6571-6573, doi: 10.1109/ECCE53617.2023.10362719.
- [국제 학회] J. Hu, S. Cui and Y. He, "Universal Flux Balancing Control to Suppress Transient DC-Bias of Phase-Shift Modulated Multi-Active-Bridge Converters," 2023 11th International Conference on Power Electronics and ECCE Asia (ICPE 2023 - ECCE Asia), Jeju Island, Korea, Republic of, 2023, pp. 1898-1905, doi: 10.23919/ICPE2023-ECCEAsia54778.2023.10213677.
- [국제 학회] S. -Y. Lee, S. Cui and J. -J. Jung, "Enhanced Voltage Injection Control for Capacitor Voltage Balancing of MMC Under Low-Frequency Operation," 2023 11th International Conference on Power Electronics and ECCE Asia (ICPE 2023 - ECCE Asia), Jeju Island, Korea, Republic of, 2023, pp. 2643-2648, doi: 10.23919/ICPE2023-ECCEAsia54778.2023.10213656.
- [국제 학회] G. S. Song, S. Cui and J. -J. Jung, "Split Capacitor Ripple Reduction Method of 3-Level NPC Converter Using Zigzag Transformer," 2023 11th International Conference on Power Electronics and ECCE Asia (ICPE 2023 - ECCE Asia), Jeju Island, Korea, Republic of, 2023, pp. 1906-1911, doi: 10.23919/ICPE2023-ECCEAsia54778.2023.10213597.
- [국내 학술지·학회지] 맹준열, 정재정 and 최성휘, "관성, 댐핑 및 드룹계수 관점에서의 GFM 제어방식 고찰" 전력전자학회지, vol. 28, no. 1, pp. 28-33, 2023.
- [국내 학회] 함지선(Jisun Ham), 최성휘(Shenghui Cui), "실리콘 카바이드 모스펫의 가전용 전력변환시스템 적용을 위한 부트스트랩 회로 설계," in 전력전자학회 학술대회 논문집, 2023, pp. 303-306.
- [국내 학회] 맹준열(Junyeol Maeng), 최성휘(Shenghui Cui), "그리드 포밍 컨버터의 Soft Start-Up 기능 구현," in 전력전자학회 학술대회 논문집, 2023, pp. 70-73.
- [국내 학회] 김동준(Dongjoon Kim), 박재연(Jaeyeon Park), 최성휘(Shenghui Cui), "EtherCAT 제어 시스템 기반 MMC 유도전동기 드라이브," in 전력전자학회 학술대회 논문집, 2023, pp. 219-221.
- [국내 학회] 박가영(Gayoung Park), 최성휘(Shenghui Cui), "그리드 포밍 컨버터의 전류 제한을 통한 FRT 제어 전략," in 전력전자학회 학술대회 논문집, 2023, pp. 74-76.
- [국내 학회] 이재근(Jaekeun Lee), 황인휘(Inhwi Hwang), 최성휘(Shenghui Cui), "가변 샘플링 주파수를 활용한 단상 PFC의 전류 THD 최소화 PWM 기법," in 전력전자학회 학술대회 논문집, 2023, pp. 267-269.

**2022**

- [국제 학술지] J. Hu, S. Cui and R. W. De Doncker, "Natural Boundary Transition and Inherent Dynamic Control of a Hybrid-Mode-Modulated Dual-Active-Bridge Converter," in IEEE Transactions on Power Electronics, vol. 37, no. 4, pp. 3865-3877, April 2022, doi: 10.1109/TPEL.2021.3119903. (Corresponding Author)
- [국제 학술지] S. Zhao, Y. Chen, S. Cui and J. Hu, "Modular Multilevel DC-DC Converter With Inherent Bipolar Operation Capability for Resilient Bipolar MVDC Grids," in CPSS Transactions on Power Electronics and Applications, vol. 7, no. 1, pp. 37-48, March 2022, doi: 10.24295/CPSSTPEA.2022.00004.
- [국제 학회] J. Yun, J. Yoo, S. Cui and S. -K. Sul, "Fast Gradient Method Based on Dynamic Programming in Model Predictive Control for PMSM Drives," 2022 IEEE Energy Conversion Congress and Exposition (ECCE), Detroit, MI, USA, 2022, pp. 1-7, doi: 10.1109/ECCE50734.2022.9947839.
- [국내 학회] 함지선(Jisun Ham),황인휘(Inhwi Hwang), 최성휘(Shenghui Cui), "실리콘 카바이드 모스펫 바디 다이오드의 광학 특성을 이용한 실시간 온도 추정의 한계와 의의," in 전력전자학회 학술대회 논문집, 2022, pp. 236-239.
- [국내 학회] 맹준열(Junyeol Maeng),황인휘(Inhwi Hwang), 최성휘(Shenghui Cui), "전력계통의 강도에 따른 그리드 포밍 컨버터의 무효 전력 제어 특성 분석과 제어 절환 기법 제안," in 전력전자학회 학술대회 논문집, 2022, 128-130.
- [국내 학회] 김동준(Dongjoon Kim),박재연(Jaeyeon Park), 최성휘(Shenghui Cui), "EtherCAT 통신 기반 제어 시스템을 사용한 컨버터 병렬 제어," in 전력전자학회 학술대회 논문집, 2022, 348-350.

**2021**

- [국제 학술지] J. Hu, S. Cui and R. W. De Doncker, "Closed-Loop Black Start-Up of Dual-Active-Bridge Converter With Boosted Dynamics and Soft-Switching Operation," in I EEE Transactions on Power Electronics, vol. 36, no. 10, pp. 11009-11013, Oct. 2021, doi: 10.1109/TPEL.2021.3071578.  (Corresponding Author)
- [국제 학술지] J. Hu, Z. Yang, S. Cui and R. W. De Doncker, "Closed-Form Asymmetrical Duty-Cycle Control to Extend the Soft-Switching Range of Three-Phase Dual-Active-Bridge Converters," in IEEE Transactions on Power Electronics, vol. 36, no. 8, pp. 9609-9622, Aug. 2021, doi: 10.1109/TPEL.2021.3055369.  (Corresponding Author)
- [국제 학술지] S. Zhao, Y. Chen, S. Cui, B. J. Mortimer and R. W. De Doncker, "Three-Port Bidirectional Operation Scheme of Modular-Multilevel DC–DC Converters Interconnecting MVDC and LVDC Grids," in IEEE Transactions on Power Electronics, vol. 36, no. 7, pp. 7342-7348, July 2021, doi: 10.1109/TPEL.2020.3041721.
- [국제 학술지] J. Hu, S. Cui, D. v. d. Hoff and R. W. De Doncker, "Generic Dynamic Phase-Shift Control for Bidirectional Dual-Active Bridge Converters," in IEEE Transactions on Power Electronics, vol. 36, no. 6, pp. 6197-6202, June 2021, doi: 10.1109/TPEL.2020.3039348.  (Corresponding Author)
- [국제 학회] Y. -R. Kim, S. -Y. Lee, S. Cui and J. -J. Jung, "Improvement of DC Voltage Control Dynamics with Bipolar DC Circuits Using a Zigzag Transformer," 2021 24th International Conference on Electrical Machines and Systems (ICEMS), Gyeongju, Korea, Republic of, 2021, pp. 2060-2064, doi: 10.23919/ICEMS52562.2021.9634640.
- [국제 학회] S. Zhao, S. Cui, J. Hu and Y. Chen, "Bipolar Operation Scheme of Modular Multilevel DC-DC Converter (MMDC) for Resilient MVDC Distribution Systems," 2021 IEEE 1st International Power Electronics and Application Symposium (PEAS), Shanghai, China, 2021, pp. 1-7, doi: 10.1109/PEAS53589.2021.9628426.
- [국제 학회] S. Cui, J. Hu and S. Zhao, "Enhanced Dual-Active Bridge Converter with Inherent Bipolar Operation Capability for LVDC Distribution Systems," 2021 IEEE 1st International Power Electronics and Application Symposium (PEAS), Shanghai, China, 2021, pp. 1-6, doi: 10.1109/PEAS53589.2021.9628858.
- [국제 학회] M. Jia, S. Cui, P. Joebges and R. W. D. Doncker, "A Modular Multilevel Converter as a Grid Emulator in Balanced and Unbalanced Scenarios Using a Delta-Wye Transformer," 2021 IEEE Energy Conversion Congress and Exposition (ECCE), Vancouver, BC, Canada, 2021, pp. 2950-2957, doi: 10.1109/ECCE47101.2021.9595175.
- [국제 학회] M. Jia, S. Cui, K. Hetzenecker, J. Hu and R. W. De Doncker, "Control of a Three-Phase Four-Wire Modular Multilevel Converter as a Grid Emulator in Fault Scenarios," 2021 IEEE Energy Conversion Congress and Exposition (ECCE), Vancouver, BC, Canada, 2021, pp. 624-631, doi: 10.1109/ECCE47101.2021.9595592.

## 학위논문

학술지·학회 논문과 구분한 랩의 학위논문 게시 목록 3편이다.[^thesis]

- Seongmin Moon. 「Implementation of Accelerated Simulation for MVDC Shipboard Power Systems in Fuel Cell based Electric Propulsion Ship」. 서울대학교 전기·정보공학부 석사학위논문, 2026년 2월.
- Gayoung Park. 「Optimization of Modulation Scheme and Transformer Design of Dual-Active Bridge Converter for Improved Efficiency」. 서울대학교 전기·정보공학부 석사학위논문, 2025년 2월.
- Jonghun Yun. 「Modulation Scheme and Dynamic Control for Improved Light-Load Operation of Three-Phase Multi-Active Bridge Converter」. 서울대학교 전기·정보공학부 박사학위논문, 2024년 8월.

## 과제와 개발 프로젝트

2021년 10월 22일–2026년 10월 22일 안의 날짜로 News가 개발을 설명한 프로젝트 3건이다. 날짜는 해당 공지의 표기이고, 명시한 기간은 그대로 옮겼다.[^news]

- 2025.01 · Development of Korea's First MMC-Based MV Drive System with HD KSOE (협력 기관 ECSL in Kyungpook National University; HD KSOE; 기간 three years)
- 2024.11 · Successful Commissioning of QAB-Based SST for DC-Grid Applications
- 2022.12 · Development of 99% Efficiency PFC with Samsung Electronics (지원 Samsung Electronics)

## 수상과 선정

최근 5년 안의 날짜가 붙은 수상·장학금·연구실 선정 7건이다. 이름과 수상 당시 과정은 News의 표기에 따른다.[^news]

- 2026.08.25 · Jaekeun Lee · 한국에너지기술평가원 원장상(KETEP President Award)
- 2026.01.02 · Jin Yoo · 과학기술정보통신부 석사우수장학금(이공계)
- 2025.06.22 · Jiyu Lee, Jonghun Yun, Jaekeun Lee 연구팀(지도 Shenghui Cui) · IEEE PEDG 2025 Best Paper Award
- 2023.11 · PCSL · HD KSOE Outstanding Collaborative Research Laboratory 선정
- 2023.07 · Gayoung Park · SBS Culture Foundation Scholarship Award
- 2023.07 · Junyeol Maeng · 전력전자학회 Best Paper Awards
- 2023.03 · Dongjoon Kim · 서울대학교 공과대학 Best Teaching Assistant Awards

## 연구실 소식

2021년 10월 22일–2026년 10월 22일의 연구·개발·산학협력 및 연구실 개설 공지 9건이다. 날짜는 게시 글이 적은 날짜이며 일자가 없으면 월까지만 적었다.[^news]

- 2026.07.03 · HD현대일렉트릭 산학협력 연구실 지정
- 2025.06.14 · 경북대 ECSL·HD KSOE와 선박 전기 추진용 MMC 구동 시스템의 육상 시험 수행
- 2025.03 · Imperix가 Jonghun Yun의 Quad-Active-Bridge 프로젝트를 산업 적용 사례로 소개
- 2025.01 · HD KSOE·경북대 ECSL과 중전압 MMC 구동 시스템 개발, PCSL은 EtherCAT 기반 제어 시스템과 모터 구동 제어 알고리즘 설계
- 2024.11 · 직류 전력망 시험 장치용 QAB 기반 반도체 변압기 시운전
- 2024.08 · Jisun Ham의 GaN 변환기가 액체 질소에서 동작
- 2023.02 · Dongjoon Kim·Jaeyeon Park의 EtherCAT 제어 시스템과 MMC 시제품을 결합한 모터 구동 인버터 시운전
- 2022.12 · 삼성전자 지원으로 계통 연계형 역률 보정 변환기 개발
- 2022.09 · PCSL 개설 및 모듈형 다단 변환기·계통 연계 변환기·전력 반도체 연구 소개

## 연락과 위치

- 연구실: 서울특별시 관악구 관악로 1 서울대학교 301동 602호[^home]
- 교수 연구실: 301동 609호, 전화 02-880-7303[^prof]
- 교수 이메일: cuish@snu.ac.kr[^team]
[^p1]: D.-J. Kim, J. Park, Y. Hong, S. Cui, IEEE Transactions on Power Electronics 41, 10324-10342 (2026). <https://doi.org/10.1109/TPEL.2026.3655014> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/399854762_Fault-Tolerant_Independent_Pole_Control_Scheme_of_Zigzag_MMC_for_Bipolar_MVDC_Distribution_Systems>.
[^p2]: S. Kim, K.-H. Kim, S. Cui, J.-J. Jung, IEEE Transactions on Power Electronics 40, 6423-6428 (2025). <https://doi.org/10.1109/TPEL.2025.3525649> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/387780476_Adjustable_Virtual_Impedance_via_Anti-windup_Method_for_Enhancing_Transient_Stability_and_Grid-Forming_Capability_Under_Current_Limiting_Conditions>.
[^p3]: J. Lee, J. Maeng, J.-J. Jung, S. Cui, IEEE Transactions on Power Electronics 40, 14235-14240 (2025). <https://doi.org/10.1109/TPEL.2025.3571387> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/391892218_Identification_of_Resonance_and_Instability_from_Algebraic_Virtual_Impedance_of_Grid-Forming_Control_in_the_Perspective_of_Negative_Sequence>.
[^p4]: G. Park, H. Kim, B.-G. Cho, S. Cui, IEEE Transactions on Power Electronics 40, 9004-9018 (2025). <https://doi.org/10.1109/TPEL.2025.3541847> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/388962013_ZVS-Enhanced_and_RMS-Current-Minimized_Optimal_Modulation_Scheme_of_Dual-Active_Bridge_Converter_With_Comprehensive_ZVS_Analysis>.
[^p5]: J. Yun, S. Cui, S.-K. Sul, IEEE Transactions on Power Electronics 40, 9019-9033 (2025). <https://doi.org/10.1109/TPEL.2025.3543493> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/389120330_Instantaneous_Pulse_Pattern_Control_for_Optimized_Dynamic_Performance_of_Three-Phase_Dual-Active_Bridge_Converter>.
[^p6]: J. Yun, S. Cui, IEEE Transactions on Power Electronics 40, 5014-5024 (2025). <https://doi.org/10.1109/TPEL.2024.3517534> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/387102890_Enhanced_Active_Thermal_Balancing_Strategy_for_Three-Phase_Dual-Active_Bridge_Converter_Suppressing_Transformer_Flux_Saturation>.
[^p7]: J. Yun, J. Yoo, S. Cui, S.-K. Sul, IEEE Transactions on Power Electronics 38, 5952-5962 (2023). <https://doi.org/10.1109/TPEL.2023.3240510> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/367564434_Model_Predictive_Control_for_Six-Step_Operation_of_PMSM_Based_on_Adapted_Fast_Gradient_Method>.
[^p8]: I. Hwang, J. Lee, S. Cui, IEEE Transactions on Power Electronics 40, 574-587 (랩 목록 2024년 구역). <https://doi.org/10.1109/TPEL.2024.3465040> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/384212606_Time-Step-Adaptive_Filter_Discretization_for_Variable_Sampling_Frequency_Control_of_Power_Converters>.
[^home]: PCSL 첫 화면, 연구 분야와 응용 대상, 위치. <https://pcsl.snu.ac.kr/> 관측일 2026-10-26.
[^team]: Team, 교수 학력·경력, 현재·이전 구성원, 학교 이메일. <https://pcsl.snu.ac.kr/team> 관측일 2026-10-26.
[^lab]: 전기·정보공학부 연구실 소개, 국·영문 이름과 연구 내용. <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=115> 관측일 2026-10-26.
[^prof]: 전기·정보공학부 최성휘 부교수 소개, 학력·경력·관심 분야·교수 연구실. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p871> 관측일 2026-10-26.
[^ij]: International Journals 전체 목록과 2021–2026년 구역. <https://pcsl.snu.ac.kr/publications/international-journals> 관측일 2026-10-26.
[^ic]: International Conferences 전체 목록과 2021–2026년 구역. <https://pcsl.snu.ac.kr/publications/international-conferences> 관측일 2026-10-26.
[^dj]: Domestic Journals 전체 목록. <https://pcsl.snu.ac.kr/publications/domestic-journals> 관측일 2026-10-26.
[^dc]: Domestic Conferences 전체 목록. <https://pcsl.snu.ac.kr/publications/domestic-conferences> 관측일 2026-10-26.
[^thesis]: Thesis and Dissertation, 학위논문 3편. <https://pcsl.snu.ac.kr/publications/thesis-and-dissertation> 관측일 2026-10-26.
[^news]: News, 날짜가 붙은 연구·개발·산학협력·수상·구성원 공지. <https://pcsl.snu.ac.kr/news> 관측일 2026-10-26.

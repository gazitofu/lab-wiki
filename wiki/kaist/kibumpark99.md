# 교통 전동화 및 재생 에너지 통합 시스템 연구실 (TETRIS Lab, Transportation Electrification and Grid Integration Systems Lab)

**KAIST 조천식모빌리티대학원·녹색성장지속가능대학원 · 박기범 부교수**

- 대분야: 전기전자·반도체·광학, 에너지·환경·지구
- 태그: 전력전자 변환기·전력 변환 시스템[^p5][^p6], 전동기·발전기 설계·구동 제어[^p3][^p4], 무선 전력 전송[^p1][^p2], 스마트 그리드·전력 관리[^p7], 전기차[^topics][^p3]
- 홈페이지: <https://sites.google.com/site/kibumpark99/home>
- 교수 소개: <https://sites.google.com/site/kibumpark99/member/professor>

> 전기차와 전기 추진 선박의 구동·충전 장치, 재생에너지를 전력망에 연결하는 전력 변환 회로와 제어를 연구하는 연구실이다.[^topics][^department]

## 무엇을 연구하나

이 연구실의 중심 분야는 전력전자(반도체 스위치로 전력 흐름과 전기의 형태를 조절하는 기술)다. 전기차와 전기로 추진하는 선박, 재생에너지를 연결하는 전력망을 대상으로 전력 변환 장치의 설계와 제어를 연구한다. 연구 소개는 효율과 소형화를 목표로 제시한다.[^topics][^department]

교통수단 쪽에서는 모터(전기 에너지를 회전이나 이동의 기계 에너지로 바꾸는 장치)의 제어, 인버터(직류를 교류로 바꾸는 전력 변환 장치)의 설계, 배터리 충전 시스템을 다룬다. 충전 방식에는 차량에 탑재한 충전기와 차량·전력망 사이의 전력 교환, 무선 충전(전선 연결 없이 자기장이나 전자기파로 에너지를 전달하는 방식)을 함께 적고 있다.[^topics]

에너지 쪽에서는 계통 연계(발전·저장 장치 등을 전력망에 연결해 전기를 주고받게 하는 일)를 연구한다. 전력 조절 시스템, 에너지 저장 시스템, 반도체 변압기(Solid State Transformer, 전력전자 회로를 이용해 변압 기능과 전력 흐름 제어를 수행하는 장치)를 연구 대상으로 제시한다. 박기범의 학과 소개도 전기차 충전 인프라, 재생에너지 계통 연계, 전력전자 최적화(정한 조건 아래 목적에 맞는 설계나 운전 값을 찾는 일)를 연구 관심사로 적는다.[^topics][^department] 논문에서는 태양광 발전량과 전기 수요를 예측하고 전력망 사이의 전력 거래를 조정하는 운영 방법도 다룬다.[^p7]

## 주요 연구 주제

### 무선 충전의 수신부와 회로

전기차 무선 충전에서는 송신부와 수신부가 어긋날 때도 전력을 전달할 수 있어야 한다. 대표 논문 1은 수신 코일(전력을 받는 쪽에서 자기장을 통한 에너지 전달을 맡는 감은 도선)을 설계해 부품에 걸리는 전기적 부담과 효율 변동을 줄이고, 별도의 출력 조절 회로 없이 충전 시스템을 구성하는 방법을 제안했다. 제작한 충전 시스템으로 성능을 비교했다.[^p1]

대표 논문 2는 서로 다른 주파수(반복 현상이 단위 시간에 일어나는 횟수) 대역의 무선 충전에 대응하는 정류기(교류를 직류로 바꾸는 회로)를 제안했다. 입력 신호의 주파수에 따라 회로의 동작 방식이 자동으로 바뀌며, 추가 감지 회로나 외부 제어 신호 없이 두 충전 방식을 지원한다. 시제품으로 동작을 확인했다.[^p2]

### 전동기의 구동 제어

차량의 모터를 제어할 때는 원하는 토크(회전축에 대해 힘이 만드는 회전 작용의 크기와 방향을 나타내는 양)를 내면서 전압(전하량당 두 지점의 전기적 위치 에너지 차이)과 전류(단위 시간에 전달되는 전기의 양)의 제한을 지켜야 한다. 대표 논문 3은 모델 예측 제어(매 시점 시스템의 미래 상태를 계산해 목표와 제한 조건에 맞는 입력을 고르는 방법)를 사용해 토크 오차와 손실 등의 목표를 함께 다룬다. 차량 구동에 쓰는 동기 전동기(움직이는 부분과 이를 구동하는 자기장이 같은 속도로 움직이는 전동기)를 대상으로 수치 계산과 실험으로 제어 방법을 확인했다.[^p3]

대표 논문 4는 전기 추진 선박에서 고장 상황에도 운전을 이어 가는 속도 제어를 다룬다. 최대 전류, 토크 변화율, 직류 연결부 전압의 제한을 한 최적화 문제에 넣었으며, 제안한 방법의 효과는 시뮬레이션(모형으로 시스템의 동작을 계산해 재현하는 방법)으로 확인했다.[^p4]

### 계통 연계 변환기와 전력망 운영

대표 논문 5는 저장 장치의 충전·방전을 조절하는 양방향 직류·직류 변환기(전력 전달 방향을 바꿀 수 있고 직류 전압을 다른 직류 전압으로 바꾸는 장치)를 다룬다. 확장 상태 관측기(입력과 측정값으로 시스템 내부 상태와 모델에 담기지 않은 영향을 함께 추정하는 계산 방법)를 제안해 모델 오차와 측정 잡음, 입력 전압과 전기 소비 조건 변화에 대응했다. 효과는 양방향 변환기 실험으로 확인했다.[^p5]

대표 논문 7은 태양광 발전이 있는 전력망 묶음 사이에서 남는 전기를 거래하고, 각 전력망의 전력 소비와 사용 일정을 함께 조정한다. 수요와 발전량 예측을 운영에 반영하고, 판매자와 구매자의 이익을 함께 고려하는 거래 모형을 제안했다.[^p7] 대표 논문 8은 마이크로그리드(발전·소비 설비를 하나의 제어 단위로 묶어 외부 전력망과 연계하거나 분리해 운전할 수 있는 국소 전력망)의 계통 연계 변환기에 쓰는 제어 방법들을 검토한 논문이다. 모델 예측 제어와 자료 기반 제어 등 여러 방법의 설계·성능 특성을 비교하고 전력망과의 안정적인 연결 운전, 공급 전기가 요구 조건을 충족하는 정도, 전력망 지원 문제를 정리한다.[^p8]

### 자료를 이용한 전력 변환 장치 설계

대표 논문 6은 다중 권선 변압기(입력이나 출력의 전기 연결부를 여럿 두도록 도선을 감은 부분을 구성한 변압기)의 설계를 다룬다. 군집화(자료의 유사성을 기준으로 자료를 여러 묶음으로 나누는 방법)로 초기 설계를 정하고, 인공 신경망(연결된 계산 요소의 매개변수를 조정해 입력과 출력 사이 관계를 학습하는 모형)으로 성능을 예측한 뒤 결과를 반영해 설계를 반복 조정한다. 시뮬레이션과 실험으로 설계 방법을 확인했다.[^p6]

## 대표 논문

KAIST 재직 시기의 2021–2026년 논문에서 연구 갈래를 나누고 초록을 읽을 수 있는 8편을 골랐다. 연도는 등록 서지의 출판 권호·학회 연도이며, 「쉽게 말하면」은 각 논문의 등록 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2026 | [Optimization of Receiver Coil With Minimized Coupling Coefficient Variation and High Coil Inductance for High Efficiency 2-Stage WPT System of EVs Based on SAE-J2954](https://doi.org/10.1109/access.2025.3647509) · IEEE Access | 수신 코일을 설계해 송수신부가 어긋날 때의 효율 변동과 부품의 전기적 부담을 줄였다. 제작한 충전 시스템으로 성능을 비교했다.[^p1] |
| 2 | 2025 | [Dual-Band Rectifier Using Coupled Inductor for Wireless Power Transfer Receivers](https://doi.org/10.1109/tpel.2024.3521362) · IEEE Transactions on Power Electronics | 입력 주파수에 따라 정류기의 동작 방식이 자동으로 바뀌는 무선 전력 수신 회로다. 추가 감지 회로나 외부 제어 신호 없이 두 주파수 대역에 대응하며 시제품으로 확인했다.[^p2] |
| 3 | 2025 | [Generalized Model Predictive Torque Control of Synchronous Machines](https://doi.org/10.1109/tmech.2024.3461209) · IEEE/ASME Transactions on Mechatronics | 차량용 동기 전동기에서 토크 오차와 손실 등의 목표를 전압·전류 제한과 함께 다루는 제어 방법이다. 수치 계산과 실험으로 효과를 확인했다.[^p3] |
| 4 | 2024 | [MW-rated Induction Motor Control equipped with Fault-Ride-Through Capability for an Electric Propulsion Ship using Model Predictive Control](https://doi.org/10.1109/ecce55643.2024.10861477) · 2024 IEEE Energy Conversion Congress and Exposition (ECCE) | 고장 상황에도 운전을 이어 가도록 전기 추진 선박의 속도를 제어하는 방법이다. 전류·토크 변화율·직류 연결부 전압의 제한을 함께 고려하며 시뮬레이션으로 확인했다.[^p4] |
| 5 | 2024 | [Bidirectional DC-DC converters for distributed energy resources: Robust predictive control with structurally-adaptive extended state observers](https://doi.org/10.1016/j.ijepes.2024.109913) · International Journal of Electrical Power & Energy Systems | 저장 장치의 충전·방전을 조절하는 양방향 변환기에서 모델 오차와 측정 잡음, 외부 변화에 대응하도록 상태와 교란 영향을 추정하는 계산 방법을 제안했다. 변환기 실험으로 확인했다.[^p5] |
| 6 | 2025 | [Hierarchical Data-Driven Multi-Winding Transformer Design Framework](https://doi.org/10.1109/ecce58356.2025.11260229) · 2025 IEEE Energy Conversion Conference Congress and Exposition (ECCE) | 군집화로 초기 설계를 정하고 인공 신경망으로 성능을 예측한 뒤 반복 조정하는 다중 권선 변압기 설계 방법이다. 시뮬레이션과 실험으로 확인했다.[^p6] |
| 7 | 2021 | [Cooperative decentralized peer‐to‐peer electricity trading of nanogrid clusters based on predictions of load demand and PV power generation using a gated recurrent unit model](https://doi.org/10.1049/rpg2.12195) · IET Renewable Power Generation | 태양광 발전이 있는 전력망 묶음 사이의 전력 거래와 각 전력망의 소비·사용 일정을 함께 조정한다. 수요·발전량 예측과 판매자·구매자의 이익을 고려하는 거래 모형을 연결했다.[^p7] |
| 8 | 2025 | [Advanced Control of Grid-Connected Microgrids: Challenges, Advances, and Trends](https://doi.org/10.1109/tpel.2025.3526246) · IEEE Transactions on Power Electronics | 계통 연계 변환기에 쓰는 비선형 제어 방법들을 검토하고 설계·성능 특성을 비교한 논문이다. 전력망 연결 운전, 전력 품질, 전력망 지원 문제와 향후 방향을 정리했다.[^p8] |

## 교수와 전문 분야

박기범은 KAIST에서 전기공학 학사(2003), 석사(2005), 박사(2010) 학위를 받았다. 박사학위 논문 제목은 회로 부품에 걸리는 전압을 줄이는 직류·직류 변환기 회로 구조에 관한 연구다. 2010년 3월부터 2011년 2월까지 KAIST 박사후연구원, 2011년 3월부터 2020년 3월까지 ABB Switzerland 연구원으로 근무했으며, 누리집은 2020년 4월부터 KAIST 부교수로 적는다.[^professor]

학과 교수 소개가 밝힌 전문 분야는 전기차 충전 인프라, 재생에너지 계통 연계, 전력전자 최적화다. 연구실 소개의 모터 제어·인버터 설계·충전 시스템·에너지 시스템과 연결되는 범위다.[^department][^topics] 녹색성장지속가능대학원은 박기범을 겸임교수 구획에 두고, 본래 소속으로 조천식모빌리티대학원을 함께 적는다.[^gggs]

누리집은 IEEE Transactions on Transportation Electrification, IEEE Transactions on Industrial Electronics, IEEE Transactions on Power Electronics, MDPI Electronics와 전력전자학회 학술지의 Associate Editor, PCIM-Europe 자문위원, IEEE Power Electronics Society의 한국 국제연락 담당, 전력전자학회 국제이사를 적고 있다. IEEE Access의 Guest Associate Editor는 2022년 이력으로 구분한다.[^professor]

## 응용 분야

연구 소개가 직접 제시한 응용은 전기차와 전기 추진 선박의 구동 장치, 배터리 충전 시스템, 재생에너지를 전력망과 연결하는 시스템이다.[^topics] 게시 과제에는 전기차 온보드 충전기, 전기 추진 선박, 전기 트랙터, 로봇 무선 충전, 직류 배전 장치와 데이터센터 전력 완충 시스템도 포함되어 있다.[^projects]

## 구성원

2026년 10월 26일 누리집의 Ph.D. Students와 M.S. Students 게시 명단 기준이다. 박사과정 쪽의 9명 중 Hongcheng Zhu는 Visiting student로 표시되어 있어 방문 학생으로 구분했다. 나머지는 박사과정 8명과 석사과정 5명이다. 이름의 대소문자와 연구 주제는 원문 표기를 따랐으며, 시작 연월은 별도 표기하지 않는다.[^phd][^masters] 「대표 논문 참여」는 대표 논문 표의 번호이며, 전체 저자 목록에서 같은 이름을 확인한 사람에게 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| chang-Yeob Chu | 박사과정 (LAB LEADER) | Wireless Power Transfer | jjangyeob@kaist.ac.kr | 1 |
| Jongseok Kim | 박사과정 | Optimal Control | jason.kim@kaist.ac.kr | 3, 4 |
| YoungSeok Lee | 박사과정 | Motor control | youngseok0929@kaist.ac.kr | 1 |
| Jiho SOng | 박사과정 | Charging System, DC Grid System | jiho.song@kaist.ac.kr | 6 |
| Hamza Ahmad | 박사과정 | DC/DC converter, Integrated Magnetics | hamza@kaist.ac.kr |  |
| dongwoo hyun | 박사과정 | Grid system, Wireless charging system | dongwoo.hyun@kaist.ac.kr |  |
| Jiho Kwak | 박사과정 | DC-DC Converter, EIS implementation | ghokwak@kaist.ac.kr |  |
| Kun Wang | 박사과정 (Website manager) | AI-assisted Control & Design | walkerwang@kaist.ac.kr | 6 |
| Hongcheng Zhu | 방문 학생 | Cyber Security in Power System | hongcheng@kaist.ac.kr |  |
| wonhyeok you | 석사과정 |  | wonhyeok.you@kaist.ac.kr |  |
| Seongmin lee | 석사과정 |  | seongmin.lee@kaist.ac.kr |  |
| Euichan Jeong | 석사과정 |  | euichanj@kaist.ac.kr |  |
| YERIM KIM | 석사과정 |  | fion1010@kaist.ac.kr |  |
| Seong Woo Son | 석사과정 |  | tjddn543@kaist.ac.kr |  |

## 졸업생과 이전 구성원

2026년 10월 26일 누리집 Alumni에 게시된 8명이다. 석사 학위 7명과 박사후연구원 1명으로, 연도와 진로는 랩 표기를 따랐다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Seunghun you | Master degree (2026) |  |
| Yeongho Jeon | Master degree (2026) | KAIST |
| JEOng Bae Park | Master degree (2026) | Agency for Defense Development (ADD) |
| Jun Gwon | Master degree (2026) | Hanwha Systems |
| Byungju Lee | Master degree (2026) | LS Electric |
| Jaehyun lee | Master degree (2026) |  |
| Xinliang Yang | Master degree (2023) | Virginia Tech |
| Oluleke babayomi | Postdoc (2024) | Kumoh National Institute of Technology |

## 최근 논문 목록 (2021–2026)

누리집의 세 목록에서 2021–2026년으로 적힌 98편을 실었다. 학술지 9편(31–39번), 국제 학회 34편(60–93번), 국내 학회 55편(1–55번)이며, 제목·저자·발표처는 누리집 표기를 유지하고, 제목과 저자 등을 대조한 19편에 DOI를 더했다. 전기차 무선 충전과 전동기 구동, 전력 변환 회로·제어, 전력망 운영을 다룬 논문이 포함된다. 이 목록은 박기범의 2020년 4월 KAIST 부임 뒤 연도로 적힌 항목들이다. 논문 목록에는 연도 범위를 적용하므로 2021년의 10월 13일 이전 발표도 포함한다.[^journal][^conference][^domestic][^professor]

**2026**

- Y. Lee, C. Chu, S. Woo, S. Ahn, and K.-B. Park. "Radiated EMI suppression in wireless power transfer systems via multilevel Tx-voltage shaping". *ECCE-NA, 2026*.
- J. Kim and K.-B. Park. "Bandwidth-Guided Augmented Lagrangian Penalty Parameter Design for Model Predictive Torque Control of IPMSM Drives". *ECCE-NA, 2026*.
- H. Ahmad, S. Hong, J.-B. Lee, J. Byun, and K.-B. Park. "Optimal design of high leakage inductance integrated planar transformer with interleaved winding". *PCIM-Europe, 2026*.
- H. Ahmad, J. Song, J.-B. Lee, J. Byun, and K.-B. Park. "4D design space based unified magnetic and circuit design optimization framework for CLLC converter". *PCIM-Europe, 2026*.
- C.-Y. Chu, D. Kim, Y. Lee, and K.-B. Park. "Dual-transmitter coil-based series-stacked class E inverter with optimal operating strategy for high-frequency WPT system". *ECCE-Asia, 2026; DOI: 10.23919/ipec-nagasaki2026-ec64663.2026.11597443*.
- C.-Y. Chu, S. Huh, D.-I. Lee, Y. Lee, H.-S. Youn, and K.-B. Park. "Optimization of receiver coil with minimized coupling coefficient variation and high coil inductance for high efficiency 2-stage WPT system of EVs based on SAE-J2954". *IEEE Access, vol. 14, pp. 2800-2814, 2026; DOI: 10.1109/access.2025.3647509*.
- 김동빈, 박재형, 이영석, 유원혁, 전영호, 박기범, 김용훈. "상용 BESS-PCS 운전 로그 기반 등가 LC 사전정보를 활용한 Full-Order Grid-Following 디지털 트윈". *ICROS Conference, 2026*.
- 홍성용, 박종완, 변종은, 박기범, 이재범. "DAB 기반 10.9 kW EV OBC용 평면 변압기의 전기적 설계 변수에 따른 손실 특성 분석". *KIPE Summer Conference, 2026*.
- 박종완, 홍성용, 변종은, 박기범, 이재범. "선형화 모델을 통한 10.9 kW DAB 기반 전기차 OBC의 적응형 DPS 제어 및 효율 최적화". *KIPE Summer Conference, 2026*.
- S. You and K.-B. Park. "입력전류 THD 개선을 위한 Unipolar Modulation 기반 인터리브드 토템폴 PFC 제어 기법". *KIPE Summer Conference, 2026*.
- D.-W. Hyun, S. Han, K.-B. Park. "배터리 진단용 전력 변환 장치에서 PFC 컨버터의 DC 링크 전압 리플 저감을 위한 제어 기법". *KIEE Summer Conference, 2026*.
- J. Kim and K.-B. Park. "매입형 영구자석 동기 전동기의 전 운전 영역을 위한 인덕턴스 및 자속 적응형 예측 토크 제어". *KIPE Summer Conference, 2026*.
- E. Jeong, J. Song, H. Ahmad, Ye R. Kim and K. -B. Park. "Single-Stage DAB 기반 AC-DC 컨버터의 SPS 및 입출력 전압비 적응형 EPS 변조에 따른 손실 비교 분석". *KIPE Summer Conference, 2026*.
- W. You, K.-B. Park. "3-레벨 계통연계형 인버터의 전 변조 영역 공통모드전압 저감을 위한 캐리어 기반 적응형 DPWM 기법". *KIEE Summer Conference, 2026*.
- C.-Y. Chu, D. Kim, Y. Lee, and K.-B. Park. "6.78 MHz WPT 시스템을 위한 최적 동작 방안을 갖는 다중 송신 코일 기반 Class E 인버터". *KIEE Summer Conference, 2026*.
- S. Son, K.-B. Park. "스위치 개방 고장 및 계통 불평형 상황에서의 3상 인버터 손실 분석". *KIEE Summer Conference, 2026*.
- Ye R. Kim, H. Ahmad, J. Song, E. Jeong and K.-B. Park. "전기차 온보드충전기 DAB 컨버터용 인덕터 통합 평면 변압기의 프린징 효과 및 손실 특성 해석". *KIPE Summer Conference, 2026*.
- S. Lee, J. Kwak and K.-B. Park. "우주 환경을 고려한 포워드 컨버터의 전자기-열 연성해석 및 동작 온도 분석". *KIPE Summer Conference, 2026*.
- H. Ahmad, J. Song and K.-B. Park. "고효율 11-kW CLLC 공진 컨버터 설계 최적화". *KIPE Summer Conference, 2026*.
- J. Song, H. Ahmad and K.-B. Park. "전기차 양방향 온보드충전기 설계를 위한 DAB 및 CLLC 비교분석". *KIEE Summer Conference, 2026*.

**2025**

- J. Park, J. Song and K.-B. Park. "Comparative efficiency analysis of DPS and EPS modulation using ANN-LUT control for GaN-based dual active bridge converters in wide voltage range". *ICEMS, 2025; DOI: 10.23919/icems66262.2025.11317301*.
- J. Gwon and K.-B. Park. "An analysis of sub-cycle phasor estimation algorithm for digital relays". *ICEMS, 2025; DOI: 10.23919/icems66262.2025.11316973*.
- D.-W. Hyun and K.-B. Park. "DC-link voltage ripple reduction in OBC-based EIS measurement using a frequency-selective feedforward compensation for PFC converters". *ICEMS, 2025. (Best Paper Award); DOI: 10.23919/icems66262.2025.11316970*.
- Y. Jeon and K.-B. Park. "A lightweight deep learning approach for real-time and fast fault diagnosis in power systems". *ICEMS, 2025; DOI: 10.23919/icems66262.2025.11317530*.
- J. Song and K.-B. Park. "Power flow analysis of dual active bridge converter with series capacitors for topology morphing". *ECCE, 2025; DOI: 10.1109/ecce58356.2025.11259692*.
- K. Wang, J. Song, and K.-B. Park. "Hierarchical data-driven multi-winding transformer design framework". *ECCE, 2025; DOI: 10.1109/ecce58356.2025.11260229*.
- K. Wang, J. Song, and K.-B. Park. "From images to inductance: modeling transformers with Vision Transformer". *ECCE, 2025*.
- O. Babayomi, Y. Li, Z. Zhang, and K.-B. Park. "Advanced control of grid-connected microgrids: challenges, advances and trends". *IEEE Trans. Power Electronics, vol. 40, no. 6, pp. 7681-7708, Jun. 2025; DOI: 10.1109/tpel.2025.3526246*.
- D. Kim, J. Chae, K.-B. Park, and G.-W. Moon. "Dual-band rectifier using coupled inductor for wireless power transfer receivers". *IEEE Trans. Power Electronics, vol. 40, no. 5, pp. 7488-7499, May 2025; DOI: 10.1109/tpel.2024.3521362*.
- K. Choi, J. Kim, and K.-B. Park. "Generalized model predictive torque control of synchronous machines". *IEEE/ASME Trans. Mechatronics, vol. 30, no. 4, pp. 2643-2653, Aug. 2025; DOI: 10.1109/tmech.2024.3461209*.
- S. Lee, J. Kwak and K.-B. Park. "극한 우주 환경의 DC-DC 컨버터를 위한 스위칭 소자의 열적 특성 분석". *KIPE Autumn Conference, 2025*.
- W. You and K.-B. Park, “전기차 급속충전기의 공통모드 전류 저감을 위한 필터 클램핑 구조 분석,“ KSAE Autumn Conference, 2025.
- Y. Jeon and K.-B. Park, “전기차용 충전 시스템을 위한 딥러닝 기반 고장 진단 알고리즘 연구,“ KSAE Autumn Conference, 2025.
- J. Park, J. Song, and K.-B. Park, “Analysis and control of extended phase shift modulation using an ANN-loss map for efficiency improvement of a GaN-based DAB converter in OBCs,“ KIEE Summer Conference, 2025.
- J. Gwon and K.-B. Park, “Model-free predictive current control for IPMSM with online ultra-local model update,“ KIEE Summer Conference, 2025.
- 홍성용, 오형석, 이원정, 박기범, 변종은, 이재범, “Switching frequency modulation for light-load efficiency enhancement in a DAB converter applied to an on-board charger,“ KIPE Summer Conference, 2025.
- 오형석, 홍성용, 이원정, 박기범, 변종은, 이재범, “Analysis on structural loss factor and design guidelines for a planar transformer in 10.9kW 400V EV OBC with DAB topology,“ KIPE Summer Conference, 2025.
- W. You and K.-B. Park, “Leakage current reduction and loss comparison using an LCL filter clamping structure in PCS for ESS,“ KIPE Summer Conference, 2025.
- Y. Jeon and K.-B. Park, “전력계통의 실시간 고속 고장 진단을 위한 경량 딥러닝 연구,“ KIPE Summer Conference, 2025.
- S. You and K.-B. Park, “인터리브드 토템폴 PFC 회로의 경부하 효율 향상 기법,“ KIPE Summer Conference, 2025.
- J.-H. Seong and K.-B. Park, “슬라이딩모드 제어를 활용한 디커플링 행렬 기반 QAB 컨버터 제어 분석,“ KIPE Summer Conference, 2025.
- D.-W. Hyun, C.-Y. Chu, and K.-B. Park, “Design and analysis for reducing 120Hz battery current ripple in bidirectional wireless charging system for electric vehicles,“ KSAE Spring Conference, 2025.

**2024**

- J. Kim, S. Kim, D.-S. Lee, H. Ahn, and K.-B. Park. "MW-rated induction motor control equipped with fault-ride-through capability for an electric propulsion ship using model predictive control". *ECCE, 2024. (IEEE IAS IDC, 3rd Prize Paper Award); DOI: 10.1109/ecce55643.2024.10861477*.
- O. Babayomi, J. Kim, and K.-B. Park. "Disturbance observer-based control with sensor noise suppression for DAB converters". *ECCE, 2024; DOI: 10.1109/ecce55643.2024.10861037*.
- S. Qzai, L. Baumann, K.-B. Park, F. Canaales, and T. Soeiro. "A hybrid Si-SiC flyback converter for auxiliary power supplies in DC ship grids". *APEC, 2024; DOI: 10.1109/apec48139.2024.10509323*.
- O. Babayomi, Z. Zhang, Z. Li, and K.-B. Park. "Bidirectional DC-DC converters for distributed energy resources: robust predictive control with structurally-adaptive extended state observers". *Internal Journal of Electrical Power and Energy Systems, vol. 158, Jul. 2024; DOI: 10.1016/j.ijepes.2024.109913*.
- D.-W. Hyun, C.-Y. Chu, and K.-B. Park, “3단 무선 충전시스템에서 DC 링크 커패시터에 대한 Post-regulator의 제어 특성 분석,“ KIEES Autumn Conference, 2024.
- D.-W. Hyun, C.-Y. Chu, and K.-B. Park, “Design analysis of 22 kW IPT converter for EVs according to high-order compensation network based on J2954,“ KIPE Autumn Conference, 2024.
- J. Gwon, J. Kim, O. Babayomi, Y. Lee and K.-B. Park, “A comparative analysis of performance between FCS-MPC and FCS-model free predictive control techniques for IPMSM control in accordance with prediction horizon length and parameter mismatch,“ KIPE Summer Conference, 2024.
- J.-B. Park, J. Song, K. Wang, and K.-B. Park, “Analysis of double phase shift modulation technique in DAB converter using a loss map,“ KIPE Summer Conference, 2024.
- D.-W. Hyun, C.-Y. Chu, Y. Lee, and K.-B. Park, “Design analysis of 3.3 kW wireless charging system for EV considering coefficient and 120 Hz charging current ripple based on J2954,“ KIPE Summer Conference, 2024.
- B.-J. Lee, Y.-D. Lee, K. Lee, and K.-B. Park, “A reconfigurable wireless charging pad for high interoperability and wide range of XY alignment,“ KIPE Summer Conference, 2024.
- O. Babayomi and K.-B. Park, “Data-driven control of solid-state transformer,“ KIPE Summer Conference, 2024.
- O. Babayomi and K.-B. Park, “Grid-forming solid-state transformer for solar PV integration into distribution grid,“ KIPE Summer Conference, 2024.
- O. Babayomi and K.-B. Park, “Model-free predictive control of multileve converters for MVDC grids,“ KIPE Summer Conference, 2024.

**2023**

- K. Choi and K.-B. Park. "Model predictive torque control of synchronous machines without a current or stator flux reference generator". *ISIE, 2023*.
- H. Ahmad, I. Sami, T.-K. Vu, D.-H. Lim, and K.-B. Park. "HILS validation of integral super twisting sliding mode control for induction motor drive with thermal coupling". *ICPE, 2023*.
- J. Song, C.-Y. Chu, Y. Lee, D.-I. Lee, H.-S. Youn, and K.-B. Park. "Parameter optimization of spread spectrum modulation to minimize EMI filter for interleaved totem-pole PFC". *ICPE, 2023*.
- J. Kim, Y. Lee, K. Choi, J. Song, and K.-B. Park. "Performance comparison of long-horizon FCS-MPC for IPMSM considering THDi and inverter loss". *ICPE, 2023*.
- J. Kwak, K.-B. Park, and I.-G. Jang. "Overcurrent protection of topology morphing LLC converters by diode clamping applicable to 400V/800V output EV". *ICPE, 2023*.
- K. Wang, X. Yang, S. Cheng, and K.-B. Park. "FCS-MPC based dual-module ANN controller for three-level converter". *ICPE, 2023*.
- C.-Y. Chu, Y. Lee, S. Huh, S. Moon, and K.-B. Park. "A study of non-isolated resonant converter as post-regulator of wireless power transfer with charging current control". *ICPE, 2023*.
- Y. Lee, J. Kim, C. Chu, and K.-B. Park. "A robust DC-link voltage control of motor drive for electric vehicle". *ICESI, 2023*.
- J. Kwak, K.-B. Park, and I.-G. Jang. "Investigation of the overcurrent protection method from LLC resonant converters applicable to MVDC solid state transformers". *ICESI, 2023*.
- D. Kim, J. Chae, K.-B. Park, and G.-W. Moon. "A self-oscillated feedback network for push-pull resonant power converters". *IEEE Trans. Power Electronics, vol. 38, no. 11, pp. 14249-14261, Nov. 2023; DOI: 10.1109/tpel.2023.3303649*.
- J.-E, Park, J.-K. Han, K.-B. Park, B.-H. Lee, and G.-W. Moon. "A new direct charging control for electric power systems in low earth orbit satellites". *IEEE Trans. Aerospace and Electronic Systems, vol. 50, no. 3, pp. 2566 – 2578, Jun. 2023; DOI: 10.1109/taes.2022.3218495*.
- B.-J. Lee, Y.-D. Lee, K. Lee, and K.-B. Park, “A reconfigurable wireless charging pad for high interoperability and high efficiency,“ KIPE Autumn Conference, 2023.
- X, Liang. K. Wang, and K.-B. Park, “A model-free control for grid-tied three-level NPC power converters from deep Q-learning to SARSA,“ KIPE Summer Conference, 2023.
- J. Kwak, K.-B. Park, and I.-G. Jang, “Fault clearing time performance investigation in diode clamping overcurrent protection method of MVDC solid-state transformer,“ KIPE Summer Conference, 2023.
- J. Song and K.-B. Park. "Comparative analysis of switching device for optimal design of on-board charger DC-DC stage in 800-V electric vehicle". *KIPE Summer Conference, 2023*.
- C.-Y. Chu, Y. Lee, and K.-B. Park. "Design analysis of 3.3kW wireless charging system according to 2-level/3-level configuration based on J2954". *KIPE Summer Conference, 2023*.
- K. Wang, X. Liang, and K.-B. Park. "Computational efficient FCS-MPC assisted by ANN for three-level conerter". *KIPE Summer Conference, 2023*.
- J. Kim and K.-B. Park. "FCS-MPC based inverter control method for IPMSM for high efficiency and high reliability inverter operation". *KIPE Summer Conference, 2023*.
- H. Ahmad, and K.-B. Park. "Achieving electrical-thremal coupling in an induction motor drive to enhabce reliability of sliding mode based controllers". *KIPE Summer Conference, 2023*.
- Y. Lee, J. Kim, and K.-B. Park, “Model predictive control of DC-DC boost converter for EV motor drive,“ KIEE Spring Conference, 2023.
- J. Kwak, K.-B. Park, and I.-G. Jang, “Review of diode clamping overcurrent protection methods of LLC converter based solid state transformer,“ KIEE Spring Conference, 2023.

**2022**

- J. Song, J. Kim, S. Kim, Y. Cho, and K.-B. Park. "Analysis on effect of increasing motor voltage from 690-V to 1000-V on 1.5-MW motor drive design for large-scale electric propulsion ship". *PEMC, 2022*.
- J. Kim, J. Song, K. Choi, and K.-B. Park. "A comparison of DPWM and inverter loss energy based FCS-MPC for IPMSM". *PEMC, 2022*.
- X. Yang, K. Wang, U. Kim, Z. Zhang, and K.-B. Park. "A weighting factor design approach for FCS-MPC based on PSO and K-means algorithm". *ECCE, 2022*.
- X. Yang, K. Wang, U. Kim, Z. Zhang, and K.-B. Park. "A computationally efficient FCS-MPC imitator for grid-tied three-level NPC power converters based on sequential artificial neural network". *ECCE, 2022*.
- X. Yang, K. Wang, Y. Lyu, and K.-B. Park. "A shallow neural network based FCS-MPC imitator for three-level NPC converters". *ICESI, 2022*.
- K. Wang, X. Yang, and K.-B. Park. "FPGA-based spread spectrum modulation for grid-connected photovoltaic inverter". *ICESI, 2022*.
- J. Kim, J. Song, K, Choi, and K.-B. Park. "Comparative analysis of inverter efficiency and WTHD based on PI-SVPWM and FCS-MPC with a strictly fixed switching frequency". *ICESI, 2022*.
- J. Song, J. Kim, and K.-B. Park. "Comparative analysis of inverter topologies for 800-V electric vehicle propulsion system". *ICESI, 2022*.
- X. Yang, K. Wang, J. Kim, K.-B. Park. "Artificial neural network-based FCS-MPC for three-level inverters". *Journal of Power Electronics, vol. 22, no. 12, pp. 2158-2165, Dec. 2022; DOI: 10.1007/s43236-022-00535-6*.
- J. Kwak, K.-B. Park, and I.-G. Jang. "Comparison and analysis of overload protection strategies of SST applicable to power system in underground city considering overload". *KIPE Summer Conference, 2022*.
- J. Song, J. Kim, S. Kim, Y. Cho, and K.-B. Park. "Performance analysis of motor drive according to increasing motor voltage of large-scale electric propulsion ship". *KIPE Summer Conference, 2022*.
- J. Kim, J. Song, S. Kim, Y. Cho, and K.-B. Park. "Analysis of grid tied converter and LCL filter characteristics according to grid voltage and dc link voltage for 1.5 MW electric propulsion vessels". *KIPE Summer Conference, 2022*.
- X. Yang, K. Wang, J. Kim, and K.-B. Park. "Artificial neural network based FCS-MPC for 3-level inverters". *KIPE Summer Conference, 2022*.
- Y. Lee, K. Wang, X. Yang, and K.-B. Park. "A FPGA-based spread spectrum modulation method for harmonic performance improvement in photovoltaic inverter". *KIPE Summer Conference, 2022*.
- J. Kim, J. Song, and K.-B. Park. "Lifetime evaluation of electric powertrain inveters". *KIEE Spring Conference, 2022*.
- J. Song, J. Kim, S. Kim, Y. Cho, and K.-B. Park. "Performance analysis of inverter for large-scale electric propulsion ship according to switching devices". *KIEE Spring Conference, 2022*.

**2021**

- C.-Y. Chu, S. Huh, S. Choi, J.-H. Park, S. Ahn, S.-G. Lee, K.-B. Park. "Wireless power transfer system design for electric vehicle charging considering a wide range of coupling coefficient variation depending on the coil misalignment". *in Proc. ICEMS, 2021*.
- K.-B. Park, and S. Pettersson. "Three-phase peak current control with LCL filter". *in Proc. ECCE-Asia, 2021*.
- S. Lee, H. Jin, L. F. Vecchietti, J. Hong, K.-B. Park, P. N. Son, and D. Har. "Cooperative decentralized peer-to-peer electricity trading of nanogrid clusters based on predictions of load demand and PV power generation using a gate recurrent unit model". *IET Renewable Power Generation, vol. 15, no. 15, pp. 3505-3523, Nov. 2021; DOI: 10.1049/rpg2.12195*.
- J. Kim, K. Choi, J. Song, and K.-B. Park. "Comparative analysis of inverter for IPMSM of hybrid electric propulsion system: PI-SVPWM vs. FCS-MPC". *KIEE Summer Conference, 2021*.
- J. Song, J. Kim, and K.-B. Park. "Performance comparison of 3-level 800V inverter based on 650-V IGBT and 2-level 800V inverer based on 1200-V SiC MOSFET for 800-V electric probulsion systems". *KIEE Summer Conference, 2021*.
- J.-H. Park, C.-Y. Chu, and K.-B. Park. "A study on optimal compensastion circuit for wireless EV charging system considering ZPA condition and coupling coefficient variation". *KIEE Summer Conference, 2021*.

### 연도 표기 없는 학술지 항목

누리집 Journal Article 목록의 다음 두 항목은 연도·권·쪽과 게재 상태를 별도로 적지 않는다.[^journal]

- C.-Y. Chu, D. Kim, Y. Lee, and K.-B. Park. "Series-stacked class E inverter with topology morphing strategy for enhanced light-load efficiency in MHz WPT system." *IEEE Trans. Industrial Electronics*.
- J. Kim, K. Choi, Y. Lee, and K.-B. Park. "Model-Adaptive Predictive Torque Control of IPMSMs for Online Optimal Operation: A Lookup-Table-Free Approach." *IEEE Trans. Transportation Electrification*.

## 과제

누리집 Project에 게시된 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 27건이다. 기간은 연도 단위 게시값이며 실제 시작·종료일이나 완료 여부를 뜻하지 않는다. 2020–2022년 과제도 포함하지만 박기범의 2020년 4월 KAIST 부임 전 착수인지는 연도만으로 구분하지 않는다.[^projects][^professor]

- 차세대 연료전지시스템 전력변환장치 (기간 2026 - 2027; 지원 현대자동차)
- 배전망-철도급전계통 연계를 위한 전력전자시스템 연구 (기간 2026 - 2027; 지원 디투이엔지)
- 글로컬랩 사업 - 미래 모빌리티 핵심기술 개발 및 글로벌 연구 플랫폼 구축 (기간 2026 - 2035; 지원 교육부, 한국연구재단)
- BESS-Enabled Power Buffering for AI Data Centers (기간 2026 - 2027; 지원 Saudi Aramco-KAIST 이산화탄소연구센터)
- 고속 사고 판단 알고리즘 개발 (기간 2026 - 2027; 지원 LS일렉트릭)
- DC 배전용 반도체 차단기 (기간 2026 - 2027; 지원 LS일렉트릭)
- 에너지분야 차세대리더 육성 사업 (기간 2026 - 2030; 지원 기후에너지환경부)
- 고신뢰성 UPS 제어 알고리즘 개발 (기간 2026; 지원 에어포인트)
- 전기차 OBC 통합 평면 변압기 최적화 연구 (기간 2025 - 2026; 지원 현대자동차)
- ESS용 전력변환시스템 신뢰성 고도화 연구 (기간 2025 - 2026; 지원 LS일렉트릭)
- 반도체 변압기 시뮬레이션 플랫폼 개발 (기간 2025; 지원 LS일렉트릭)
- 우주항공용 내방사선 GaN기반 DC-DC 컨버터 개발 (기간 2025 - 2029; 지원 한국전자통신연구원)
- 고속 고장 검출 및 분류 알고리즘 개발 (기간 2025; 지원 동우일렉트릭)
- ESS용 3레벨 인버터 기반 PCS 최적 설계 (기간 2024 - 2025; 지원 에코캡)
- 고접압 전기차 배터리 전력제어 기술 개발 (기간 2024 - 2025; 지원 셀포인트)
- 전기추진선박 모터 구동 HILS 모델 개발 (기간 2023; 지원 현대일렉트릭)
- 수소 연료전지 기반 전기트렉터 개발 (기간 2023; 지원 농림축산식품부)
- GaN 기반 전기차 온보드 충전기 최적 회로 연구 (기간 2023 - 2026; 지원 현대자동차)
- 특고압 직류 수전용 2MW 모듈형 컨버터스테이션 기술 개발 (기간 2022 - 2026; 지원 산업통상자원부)
- 로봇향 3.3kW 군집 무선충전 핵심기술 개발 (기간 2022 - 2025; 지원 과학기술정보통신부)
- 20kW 급 전기구동 트랙터 상용화 기술 개발 (기간 2022 - 2024; 지원 농림축산식품부)
- 지하도시 고밀도 전력인프라 구현을 위한 핵심 기술 개발 (기간 2022 - 2023; 지원 KAIST)
- PMIC 소형화를 위한 회로 및 제어 기법 연구 (기간 2022; 지원 삼성전자)
- e-모빌리티 업사이클링 핵심 기술 개발 (기간 2021 - 2022; 지원 KAIST)
- 양방향 무선전력전송 SiC 기반 고효율 전력변환모듈 개발 (기간 2021 - 2022; 지원 전력연구원)
- 400kW급 충전시스템이 적용된 멀티충전 지능형 주차장 (기간 2021 - 2022; 지원 국토교통부)
- 차세대 고밀도 전기차 급속충전소에 관한 연구 (기간 2020 - 2022; 지원 KAIST)

## 수상

교수 소개의 Awards and honors에서 2024–2025년으로 적힌 수상 4건이다. 연도와 상의 등급은 누리집 표기를 따랐다.[^professor]

- 2025 · Best Paper Award, ICEMS
- 2025 · Outstanding paper award, KIPE Annual Conference
- 2024 · IEEE IAS IDC, 3rd Prize Paper Award, ECCE
- 2024 · Outstanding paper award, KIPE Annual Conference

## 연락과 위치

- 교수실: 대전광역시 유성구 문지로 193 KAIST 문지캠퍼스 Faculty Wing F305[^professor][^department]
- 학생 연구실: KAIST 문지캠퍼스 F443[^phd][^masters]
- 교수 이메일: ki-bum.park@kaist.ac.kr[^professor]
- 교수실 전화: +82-42-350-1261[^professor]

[근거와 확인 범위](kibumpark99-sources.md)
[^topics]: 연구실 누리집 Topics. <https://sites.google.com/site/kibumpark99/research/topics> 2026-10-26 열람.
[^department]: KAIST 조천식모빌리티대학원 박기범 교수 소개. <https://mo.kaist.ac.kr/professor/%EB%B0%95%EA%B8%B0%EB%B2%94/> 2026-10-27 열람.
[^professor]: 연구실 누리집 Professor. <https://sites.google.com/site/kibumpark99/member/professor> 2026-10-26 열람.
[^phd]: 연구실 누리집 Ph.D. Students. <https://sites.google.com/site/kibumpark99/member/ph-d-students> 2026-10-26 열람.
[^masters]: 연구실 누리집 M.S. Students. <https://sites.google.com/site/kibumpark99/member/m-s-students> 2026-10-26 열람.
[^alumni]: 연구실 누리집 Alumni. <https://sites.google.com/site/kibumpark99/member/alumni> 2026-10-26 열람.
[^journal]: 연구실 누리집 Journal Article. <https://sites.google.com/site/kibumpark99/Journal-Article/journal-article> 2026-10-26 열람.
[^conference]: 연구실 누리집 Conference Proceeding. <https://sites.google.com/site/kibumpark99/Journal-Article/conference-proceeding> 2026-10-26 열람.
[^domestic]: 연구실 누리집 Domestic Conference. <https://sites.google.com/site/kibumpark99/Journal-Article/domestic-conference> 2026-10-26 열람.
[^projects]: 연구실 누리집 Project. <https://sites.google.com/site/kibumpark99/project> 2026-10-26 열람.
[^gggs]: 녹색성장지속가능대학원 전체 교수진, 겸임교수 구획의 박기범. <https://gggs.kaist.ac.kr/all-professor> 2026-10-27 열람.
[^p1]: C.-Y. Chu 외, K.-B. Park, IEEE Access 14, 2800-2814 (2026). <https://doi.org/10.1109/access.2025.3647509> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s43236-022-00535-6|10.1016/j.ijepes.2024.109913|10.1109/access.2025.3647509|10.1109/tmech.2024.3461209|10.1109/tpel.2024.3521362|10.1109/tpel.2025.3526246>. 2026-10-27 열람.
[^p2]: D. Kim, J. Chae, K.-B. Park, G.-W. Moon, IEEE Transactions on Power Electronics 40, 7488-7499 (2025). <https://doi.org/10.1109/tpel.2024.3521362> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s43236-022-00535-6|10.1016/j.ijepes.2024.109913|10.1109/access.2025.3647509|10.1109/tmech.2024.3461209|10.1109/tpel.2024.3521362|10.1109/tpel.2025.3526246>. 2026-10-27 열람.
[^p3]: K. Choi, J. Kim, K.-B. Park, IEEE/ASME Transactions on Mechatronics 30, 2643-2653 (2025). <https://doi.org/10.1109/tmech.2024.3461209> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s43236-022-00535-6|10.1016/j.ijepes.2024.109913|10.1109/access.2025.3647509|10.1109/tmech.2024.3461209|10.1109/tpel.2024.3521362|10.1109/tpel.2025.3526246>. 2026-10-27 열람.
[^p4]: J. Kim 외, K.-B. Park, 2024 IEEE Energy Conversion Congress and Exposition (ECCE), 6285-6292 (2024). <https://doi.org/10.1109/ecce55643.2024.10861477> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s43236-022-00535-6|10.1016/j.ijepes.2024.109913|10.1049/rpg2.12195|10.1109/access.2025.3647509|10.1109/apec48139.2024.10509323|10.1109/ecce55643.2024.10861037|10.1109/ecce55643.2024.10861477|10.1109/ecce58356.2025.11259692|10.1109/ecce58356.2025.11260229|10.1109/taes.2022.3218495|10.1109/tmech.2024.3461209|10.1109/tpel.2023.3303649|10.1109/tpel.2024.3521362|10.1109/tpel.2025.3526246|10.23919/icems66262.2025.11316970|10.23919/icems66262.2025.11316973|10.23919/icems66262.2025.11317301|10.23919/icems66262.2025.11317530|10.23919/ipec-nagasaki2026-ec64663.2026.11597443>. 2026-10-27 열람.
[^p5]: O. O. Babayomi, Z. Zhang, Z. Li, K.-B. Park, International Journal of Electrical Power & Energy Systems 158, 109913 (2024). <https://doi.org/10.1016/j.ijepes.2024.109913> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s43236-022-00535-6|10.1016/j.ijepes.2024.109913|10.1109/access.2025.3647509|10.1109/tmech.2024.3461209|10.1109/tpel.2024.3521362|10.1109/tpel.2025.3526246>. 2026-10-27 열람.
[^p6]: K. Wang, J. Song, K.-B. Park, 2025 IEEE Energy Conversion Conference Congress and Exposition (ECCE), 1-6 (2025). <https://doi.org/10.1109/ecce58356.2025.11260229> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s43236-022-00535-6|10.1016/j.ijepes.2024.109913|10.1049/rpg2.12195|10.1109/access.2025.3647509|10.1109/apec48139.2024.10509323|10.1109/ecce55643.2024.10861037|10.1109/ecce55643.2024.10861477|10.1109/ecce58356.2025.11259692|10.1109/ecce58356.2025.11260229|10.1109/taes.2022.3218495|10.1109/tmech.2024.3461209|10.1109/tpel.2023.3303649|10.1109/tpel.2024.3521362|10.1109/tpel.2025.3526246|10.23919/icems66262.2025.11316970|10.23919/icems66262.2025.11316973|10.23919/icems66262.2025.11317301|10.23919/icems66262.2025.11317530|10.23919/ipec-nagasaki2026-ec64663.2026.11597443>. 2026-10-27 열람.
[^p7]: S. Lee 외, D. Har, IET Renewable Power Generation 15, 3505-3523 (온라인 2021-09-03). <https://doi.org/10.1049/rpg2.12195> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=Cooperative%20decentralized%20peer-to-peer%20electricity%20trading%20of%20nanogrid%20clusters%20based%20on%20predictions%20of%20load%20demand%20and%20PV%20power%20generation%20using%20a%20gate%20recurrent%20unit%20model>. 2026-10-27 열람.
[^p8]: O. Babayomi, Y. Li, Z. Zhang, K.-B. Park, IEEE Transactions on Power Electronics 40, 7681-7708 (2025). <https://doi.org/10.1109/tpel.2025.3526246> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s43236-022-00535-6|10.1016/j.ijepes.2024.109913|10.1109/access.2025.3647509|10.1109/tmech.2024.3461209|10.1109/tpel.2024.3521362|10.1109/tpel.2025.3526246>. 2026-10-27 열람.

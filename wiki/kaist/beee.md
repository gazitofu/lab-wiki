# 바이오 전자시스템 연구실 (Biomedical Energy-Efficient Electronics Laboratory, BEEE Lab)

**KAIST 바이오및뇌공학과 · 김철 교수**

- 분야: 무선 뇌-몸-기계 인터페이스를 위한 저전력 집적회로와 시스템(신경 기록과 자극, 무선 전력 전달과 자료 통신, 뇌파·심전도 착용형 센서 시스템, 신호 처리 하드웨어), 초소형 이식 시스템
- 대분야: 전기전자·반도체·광학
- 태그: 집적회로 설계[^home][^p1][^p3], 신경 인터페이스·뇌-컴퓨터 인터페이스[^home][^p1][^p2], 이식형·생체 전자 기기[^home][^p1][^p2], 무선 전력 전송[^home][^p3][^p4], 착용형 생체 센서[^home][^members][^p7], AI 반도체·가속기[^home][^p8], 전력 관리 집적회로[^p5], 엣지 컴퓨팅·엣지 AI[^p8]
- 홈페이지: <https://beee.kaist.ac.kr/>
- 근거와 출처: [BEEE Lab 근거 페이지](beee-sources.md)

> 집적회로 기술로 몸에 넣는 초소형 신경 인터페이스, 무선 전력 전송, 생체 신호를 재는 착용형 장치를 만들어 진단·치료용 의료 기기의 뇌-기계 인터페이스를 구현하려는 바이오및뇌공학과 연구실이다.[^home][^members]

## 무엇을 연구하나

연구실은 KAIST 바이오및뇌공학과 김철 교수가 이끄는 바이오 전자시스템 연구실(Biomedical Energy-Efficient Electronics Laboratory)이고, 누리집은 이름을 BEEE Lab으로 줄여 적는다.[^bbeprof][^home] 누리집은 연구실의 목표를 집적회로(IC, 여러 전자 부품을 반도체 칩 하나에 모아 만든 회로) 기술로 진단·치료용 의료 기기에 쓰일 눈에 띄지 않는(invisible) 뇌-기계 인터페이스와 인공 망막을 구현하고 발전시키는 것이라고 적는다.[^home] 핵심 연구 관심으로는 초소형 무선 신경 인터페이스 마이크로시스템과, 몸에 거슬리지 않는 에너지 효율이 높은 뇌·몸 영역 센서 네트워크를 든다.[^home] 연구 과제로는 초소형 이식 장치, 폐루프 자극(측정한 신경 신호에 맞춰 자극을 바꾸는 방식), 무선 전력 전송, AI 하드웨어, 생체 전위(몸에서 생기는 전기 신호) 기록·처리용 착용형 장치를 든다.[^home]

교수 소개는 연구 관심을 무선 뇌-몸-기계 인터페이스를 위한 에너지 효율이 높은 집적회로와 시스템으로 적고, 그 안에 신경 인터페이스(신경 기록과 자극), 여러 방식의 무선 전력 전달과 자료 통신, 착용형 기기(뇌파·심전도 센서 시스템), 신호 처리 하드웨어를 든다.[^members] 바이오및뇌공학과 교수 소개는 연구분야를 브레인-바디-머신 인터페이스, 고효율저전력 바이오센서, 초소형 이식 시스템으로 적는다.[^bbeprof][^bbelist]

누리집의 연구 페이지 두 쪽은 날짜 없이 칩 성과를 소개한다. Miniaturized Neural Interfaces 페이지는 3 mm3 미만의 부피에 16채널 신경 기록과 자극을 넣은 완전 집적 피질 뇌-기계 인터페이스 칩 ENIAC(Fully Encapsulated Neural Interface and Acquisition Chip)과, 채널당 마이크로와트 미만의 전력과 마이크로볼트 미만의 잡음, 92 dB 동적 범위를 가진 16채널 신경 기록 칩, 13.56 MHz 단일 유도 결합 연결 하나로 무선 전력과 자료를 함께 보내는 방식을 소개한다.[^mni] Wireless Body-area Networks 페이지는 여러 안테나 신호를 분리·분류하는 4채널 MIMO 기저대역 수신기(65 dB 고조파 제거, 48.5 dB 신호 분리)와, 에너지 효율 RF(무선 주파수) 송신기용 하이브리드 공급 변조기(65 nm 표준 CMOS, 소신호 3 dB 대역폭(작은 입력 신호에 대한 주파수 응답 범위) 500 MHz, 최고 효율 87.7%)를 소개한다.[^wban] 이 수치 가운데 65 dB·48.5 dB, 92 dB, 500 MHz 대역폭은 Publications 목록의 2016–2018년 논문 제목에 적힌 수치와 같고, 이 논문들은 교수가 KAIST에 부임한 2019년 전에 나온 논문이다.[^pubs][^bbeprof]

KAIST 시기의 연구는 세 갈래로 나뉜다. 첫째 갈래는 **초소형 신경 인터페이스와 신경 자극**이다. 대표 논문에서는 전기 자극을 주는 동안 자극 잡음(자극 때문에 기록 신호에 섞이는 진폭이 큰 신호)과 시간·주파수 모두 겹친 신경 신호를 미리 보정하지 않고 실시간으로 되살리는 전용 칩(ASIC)을 넣은 신경 조절 시스템을 만들었고,[^p1] 사용자 상태에 맞춰 자동으로 신경을 자극하는 초소형 무선 폐루프 신경 인터페이스의 회로 설계 과제와 최근 집적회로 해법을 정리했다.[^p2] 최근 논문 목록에는 소형 전자약을 위한 무선 단열 자극기 시스템(ISSCC 2025)이 있고,[^pubs] 소식은 16채널 단열 전하 추적 자극기 논문의 CICC 2026 채택과 발표를 알렸다.[^news]

둘째 갈래는 **무선 전력 전송과 데이터 통신**이다. 대표 논문에서는 거리가 바뀌어도 하나의 무선 전력 연결로 두 부하에 전력을 보내면서 받는 쪽 자료를 끊김 없이 올려 보내는 시스템 DiTTO를 만들었고,[^p3] 사육장 안에서 자유롭게 움직이는 여러 동물에 몸을 통로로 삼는 정전 결합 방식으로 전력을 보냈으며,[^p4] 13.56 MHz에서 연결 거리와 부하가 크게 바뀌어도 안정된 직류 전압을 만드는 무선 전력 전송 칩을 만들었다.[^p5] 최근 논문 목록에는 주파수 분할 특성을 쓰는 신경 보철용 무선 전력·자료 전송 칩(IEEE TBioCAS, 2021), 몸을 거쳐 전력을 보내는 체내(Intra-Body) 전력 전송 시스템(IEEE TBioCAS, 2022), 초음파로 전력과 자료를 보내는 패치형 초음파 변환기(Microsystems & Nanoengineering, 2025)도 있다.[^pubs]

셋째 갈래는 **착용형 생체 신호 측정과 신호 처리 하드웨어**다. 대표 논문에서는 침대에 넣은 비접촉 시스템으로 옷을 입은 사람의 심전도와 심박 변이도를 몸에 닿지 않고 재는 측정 시스템을 만들었고,[^p6] 산모 복부에서 잰 심전도에서 태아와 산모의 심박을 기기 안에서 바로 뽑아내는 신호 처리 구조를 제안했으며,[^p7] 뇌파를 기기 쪽에서 분류하는 신경망 분류기를 FPGA(회로 구성을 프로그램으로 바꿀 수 있는 칩)에 구현했다.[^p8] 최근 논문 목록에는 착용형 뇌파 시스템의 소형화(Biomedical Engineering Letters, 2022)와 착용형 뇌파·광혈류(PPG) 센서의 움직임 잡음 제거 기법(Frontiers in Electronics, 2021)을 정리한 논문, 지능형 디지털 의류용 섬유 전극 공동 연구(Nature Communications, 2025)도 있다.[^pubs] 구성원 카드의 연구 주제에는 하드웨어 스파이크 분류, 귀 안 뇌파, PPG 움직임 잡음 제거, 태아 심전도, 다채널 ADC, DC-DC 변환기가 있다.[^members]

## 주요 연구 주제

### 1. 초소형 신경 인터페이스와 신경 자극

자극 잡음과 겹친 신경 신호의 실시간 복원 칩, 초소형 무선 폐루프 신경 인터페이스의 회로 과제와 해법.[^p1][^p2] 대표 논문 1, 2.

### 2. 무선 전력 전송과 데이터 통신

거리 적응형 무선 전력 전송과 상향 자료 전송(DiTTO), 움직이는 동물을 위한 몸 채널 정전 결합 무선 전력 전송, 넓은 거리·부하 범위의 13.56 MHz 무선 전력 전송.[^p3][^p4][^p5] 대표 논문 3–5.

### 3. 착용형 생체 신호 측정과 신호 처리 하드웨어

침대 속 비접촉 심전도·심박 변이도 측정, 기기 안 태아 심전도 추출, FPGA 뇌파 분류기.[^p6][^p7][^p8] 대표 논문 6–8.

## 대표 논문

랩 Publications 페이지의 2021–2026년 논문 가운데 김철 교수가 마지막 저자인 학술지·학회 논문을 세 갈래에서 고르게 골랐다. 대표 논문 2는 총설(review)이다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [A Neuromodulation System With Real-Time Neural Signals Recovery Overlapped Temporally and Spectrally With Stimulation Artifacts](https://doi.org/10.1109/tbcas.2026.3654961) · IEEE Transactions on Biomedical Circuits and Systems | 신경 조절(전기 자극으로 신경 활동을 바꾸는 것)에서는 전기 자극을 주는 동안에도 신경 신호를 계속 받아야 하지만, 진폭이 큰 자극 잡음(SA)이 이를 자주 가로막는다. 이 연구는 시간과 주파수 양쪽에서 자극 잡음과 완전히 겹친 신경 신호를 미리 보정하지 않고 실시간으로 되살리는 전용 집적회로(ASIC)를 넣은 신경 조절 시스템을 제시했다. 칩 안의 잡음 제거 회로는 곱셈기를 쓰지 않아 계산이 적은 적응형 IIR 기반 템플릿 빼기 방식(잡음의 본을 만들어 빼는 방식)으로, 고정 변수 방식보다 2.9배 빠르게 적응하고 시간에 따라 바뀌는 자극 잡음에서도 본을 빠르고 정확하게 맞추면서 면적과 전력 효율을 최적화했다. 자극기는 자극 주파수를 조금씩 흔드는 방식으로 자극 주파수와 그 배수 주파수에서 신경 신호를 잃는 것을 줄였다. 시험관과 생체 실험에서 국소 전기장 전위(LFP)와 활동 전위(AP)를 기록하며 자극 잡음 성분을 40 dB 줄이고 신경 신호를 보존했다. TSMC 65 nm CMOS 공정으로 만든 칩의 전체 면적은 1 mm2이고, 칩 안 메모리를 포함한 잡음 제거 회로는 0.15 mm2에 1.3 µW를 쓴다.[^p1] | 1저자 G. Seong(성근창), 마지막 저자 김철 |
| 2 | 2021 | [Energy-Efficient Integrated Circuit Solutions Toward Miniaturized Closed-Loop Neural Interface Systems](https://doi.org/10.3389/fnins.2021.667447) · Frontiers in Neuroscience | 몸에 넣는 초소형 장치는 말초·중추 신경계의 신경 활동을 재고 조절하는 신경 인터페이스에서 중요한 역할을 한다. 사용자의 상태에 맞춰 자동으로 신경을 자극하는 소형 무선 폐루프 시스템은 개루프 자극 시스템에 비해 전력 소모와, 계속 자극하는 데서 오는 부작용을 함께 줄이는 장점이 있다. 에너지를 적게 쓰는 소형 무선 장치는 몸의 이물 반응과 잦은 수술의 위험도 덜어 준다. 그러나 이런 시스템을 작게 만들려면 강한 자극 잡음 속에서 신경 활동을 기록하고, 자극 잡음을 실시간으로 없애고, 에너지 효율이 높은 무선 전력 전달을 해내야 하는 회로 설계 과제가 따른다. 이 논문은 집적회로(IC) 기법으로 초소형 폐루프 신경 인터페이스 시스템에 다가간 최근 연구를 정리한 총설이다.[^p2] | 1저자 J. Cho(조재욱), 마지막 저자 김철 |
| 3 | 2024 | [DiTTO: A Distance Adaptive Over 100-mW Wireless Power Transfer System With 1.695-Mb/s Uplink Telemetry and a Shared Inductor Two-Output Regulating Rectification](https://doi.org/10.1109/jssc.2024.3372418) · IEEE Journal of Solid-State Circuits | 무선 전력 전송(WPT) 연결 하나로, 거리가 바뀌어도 받는 쪽에서 보내는 쪽으로 자료를 끊김 없이 올려 보내는 상향 원격 측정과, 인덕터 하나를 나눠 쓰는 두 출력 조정 정류(SIDO-RR)를 동시에 해내는 시스템을 제시했다. 새 상향 자료 변조 방법 DCK(double charging keying)와 동적 ZOOM 제어로 부하에 전달하는 전력과 상향 자료 사이의 맞바꿈 관계를 깨, 빠른 상향 자료 전송이 더는 전달 전력의 양을 제한하지 않게 했다. DCK는 상향 자료 전송과 조정 정류를 동시에 하는 설계의 어려움도 덜어 준다. 동적 ZOOM 기반 디지털 제어 알고리즘은 거리가 바뀌어도 상향 자료 전송이 믿을 만하고, 델타-시그마 루프 두 개를 가진 SIDO-RR이 빠르게 반응하도록 한다. 단일 연결 거리 10–42 mm에서 독립된 두 부하에 최대 108 mW를 보내면서 1.695 Mb/s의 상향 자료 속도를 얻었다. 표준 65 nm CMOS로 만든 칩의 능동 면적은 0.2 mm2이고, 생체 실험으로 성능을 확인했다.[^p3] | 1저자 H. Kim(Hongkyun Kim), 마지막 저자 김철 |
| 4 | 2022 | [Seamless Capacitive Body Channel Wireless Power Transmission Toward Freely Moving Multiple Animals in an Animal Cage](https://doi.org/10.1109/tbcas.2022.3199455) · IEEE Transactions on Biomedical Circuits and Systems | 사육장 안의 살아 있는 여러 동물에 무선 전력을 안정적으로 보내기 어렵다는 점은 전임상 연구에서 장기간 실시간 신경 측정을 하는 데 큰 걸림돌이다. 이 연구는 표준 65 nm CMOS 공정으로 SCB(seamless capacitive body channel) 무선 전력 전송과 전력 관리 집적회로(PMIC)를 설계했다. SCB 무선 전력 전송은 600 mm×600 mm×120 mm 크기 사육장에서 자유롭게 움직이는 동물에 붙인 35 mm×20 mm×2 mm 크기 수신기 여러 개에 안정적으로 전력을 보낸다. 사육장과 수신기 사이의 무선 전력 연결에 가장자리 전기장 정전용량과 몸 채널을 이용해, 20 mW 부하에서 여러 상황의 전력 효율 측정값 사이 최대 차이가 6.66%에 그쳤다. 수신기가 사육장에 대해 90° 돌아간 경우에도 전력 효율은 17.76%였다. 줄로 묶지 않은 쥐 세 마리로 한 생체 실험에서 실제 상황의 장기간 연속 전력 공급을 보였다.[^p4] | 1저자 Y. Chang(Yonghee Chang), 마지막 저자 김철 |
| 5 | 2022 | [A 13.56-MHz Wireless Power Transfer System With a Wide Operating Distance and Load Range for Biometric Smartcards](https://doi.org/10.1109/tpel.2022.3232609) · IEEE Transactions on Power Electronics | 연결 거리와 부하의 변화 폭을 넓히고 송신 전력을 조절할 수 있는 범위를 넓힌 무선 전력 전송 시스템을 제시했다. 연결 거리와 부하가 크게 바뀌어도 수신기의 LC 탱크(코일과 축전기로 된 공진 회로)에 걸린 13.56 MHz 사인파에서 정류와 전압 조정을 한 단계로 해 안정된 3 V 직류 전압을 만든다. 끝에서 끝까지의 전력 전송 효율을 높이고 연결과 부하가 바뀌어도 안정적으로 동작하도록, 수신기에서 송신기로 되비치는 임피던스로 송신 전력을 조절한다. 이 조절 범위를 넓히려고 품질 계수가 높은 안테나와 직렬로 연결한 수신기 LC 탱크 구조를 썼다. 필요할 때만 동작하는 상승 에지 검출기와 델타-시그마 기반 하강 에지 검출기로 적은 전력으로 정확하게 영전류를 검출하고, 디지털 델타-시그마 기반 전압 조정 제어기로 과도 응답이 빠른 안정된 직류 전원을 만든다. 표준 65 nm CMOS 공정으로 만든 칩의 능동 실리콘 면적은 0.14 mm2이고, 30–185 mm의 연결 거리와 10000×(60 Ω–600 kΩ)의 부하 범위에서 동작한다.[^p5] | 1저자 H. Kim(Hongkyun Kim), 마지막 저자 김철 |
| 6 | 2025 | [A homecare in-bed hardware system for precise real-time ECG and HRV monitoring with layered clothing](https://doi.org/10.1016/j.bios.2025.117838) · Biosensors and Bioelectronics | 심장 활동, 특히 심전도(ECG) 파형과 심박 변이도(HRV)를 계속 살피는 일은 심장 질환을 일찍 찾는 데 꼭 필요하다. 기존 착용형 심전도 시스템은 피부에 직접 닿아야 하고 신호를 얻고 분석하는 데 외부 소프트웨어가 필요해, 편안함과 장기 사용에 한계가 있다. 이 연구는 사용자가 옷을 벗지 않고도 몸에 아무것도 차지 않은 채 심전도와 HRV를 편하고 정밀하게 재는, 침대에 넣은 비접촉 시스템을 제시했다. 유연한 능동 전극은 이중 능동 차폐로 잡음을 64 dB 줄여 신호를 잘 얻고 잡음에 강하다. 아날로그 앞단 회로의 입력 환산 잡음은 QRS 대역에서 0.49 μVrms이고, 비접촉 우측 다리 구동(driven-right-leg)으로 잡음을 27.5 dB 더 줄였다. 실시간 잡음 제거, R파 꼭짓점 검출, HRV 계산은 정상 웨이블릿 변환과 적응형 문턱값을 돌리는 FPGA에서 하드웨어로 처리한다. 두꺼운 옷을 입은 사용자도 5분 측정에서 R파 검출 정밀도가 70%를 초과했고, 사용자가 조금 움직일 때도 R파를 검출했다.[^p6] | 1저자 M. Kim(Minjae Kim), 마지막 저자 김철 |
| 7 | 2025 | [On-Device Fetal ECG Extraction Using NEO-Based Adaptive Predictor for Prenatal Healthcare](https://doi.org/10.1109/biocas67066.2025.00050) · 2025 IEEE Biomedical Circuits and Systems Conference (BioCAS) | 기존의 비침습 태아 심전도(FECG) 시스템은 무선 연결로 외부 계산에 기대는 경우가 많아 배터리로 오래 쓰기 어렵다. 이 한계를 넘으려고 태아와 산모의 심박수를 기기 안에서 모두 뽑아내는, 하드웨어 효율이 높은 신호 처리 구조를 제안했다. 산모·태아 대역 통과 필터를 나란히 두고, 비선형 에너지 연산자(NEO) 기반 적응 예측기로 산모와 태아의 R파 꼭짓점을 실시간으로 안정적으로 찾는다. 공개된 복부 심전도 자료로 평가한 결과 태아 R파 검출의 평균 F1 점수는 98.6%(PPV 98.7%, SEN 98.5%, ACC 97.3%)였다. 원 신호 대신 태아와 산모의 RR 간격 같은 처리 결과만 내보내 자료 전송량 감소 폭이 원 신호 전송 대비 99.5%를 초과했다. 고속 무선 전송이 필요 없는 이 방식으로 착용형 태아 심전도를 계속 살피는 일을 실제로 할 수 있음을 보였다.[^p7] | 1저자 D. Park(Daehyeok Park), 마지막 저자 김철 |
| 8 | 2022 | [Zero-Weight aware LSTM Architecture for Edge-Level EEG Classification](https://doi.org/10.1109/biocas54905.2022.9948628) · 2022 IEEE Biomedical Circuits and Systems Conference (BioCAS) | 뇌파(EEG) 뇌-컴퓨터 인터페이스 분야에서 신경망으로 뇌파 신호를 분류하는 연구가 새로 떠오르고 있지만, 이전 연구는 주로 알맞은 신경망을 고르고 소프트웨어로 구현하는 데 머물렀다. 이 논문은 기기 쪽(엣지)에서 뇌파를 분류하려고, FPGA에 구현한 ZW(Zero-Weight) 인지 LSTM(시간 순서가 있는 자료를 다루는 신경망) 기반 뇌파 분류기를 제안했다. 이 신경망은 LSTM 층 자체의 희소한 가중치(대부분이 0인 가중치)뿐 아니라 뒤따르는 층의 희소한 가중치까지 고려해 행렬-벡터 곱셈을 최적화한다. 공개된 BCI 대회 자료로 평가한 결과, 하드웨어로 구현한 분류기는 3.40 GHz CPU에서 돌린 소프트웨어 분류기에 비해 9.53배 빨랐고 정확도는 최대 81%였다.[^p8] | 1저자 S. Yoo(Seungjae Yoo), 마지막 저자 김철 |

## 교수와 전문 분야

김철 교수는 KNU에서 EECS 학사, KAIST에서 전기공학(Electrical engineering) 석사, UC San Diego에서 생명공학(Bioengineering) 박사(2017)를 받았다.[^members][^bbeprof] 2009–2012년에 SK Hynix 연구원으로 일했고, 2017–2019년 UC San Diego 생명공학과 박사후연구원을 거쳐 2019년 KAIST 바이오및뇌공학과 조교수가 되었으며 2023년 9월부터 부교수다.[^bbeprof] 바이오및뇌공학과 교수진 목록은 학사과정 주임교수를 함께 적는다.[^bbelist] 연구실 Members 페이지는 소속을 바이오및뇌공학과와 뇌인지공학프로그램으로 적고, 전기및전자공학부·KAIST 헬스사이언스연구소·반도체시스템공학과 겸임교수(Adjunct Professor)를 함께 적는다.[^members]

학술 활동으로는 IEEE Transactions on Biomedical Circuits and Systems(TBioCAS)의 부편집장(2020년부터), IEEE CICC(Custom Integrated Circuits Conference) 신기술(Emerging Technology) 분과 공동 위원장, TBioCAS의 ISCAS 2020 특별호 객원 편집자를 맡았고, IEEE Senior Member다.[^members][^bbeprof] 교수 소개의 수상 칸은 IEEE Solid-State Circuits Society의 Predoctoral Achievement Award(2017–2018), UC San Diego Bioengineering Department의 Shunichi Usami Ph.D. Thesis Design Award(2017–2018), Samsung Electronics 16th Human-Tech Thesis Prize Contest의 Gold Prize를 적는다.[^members][^bbeprof] KAIST 시기 소식에는 The Korean Society of Medical and Biological Engineering 2023 62th Autumn Conference의 Best Paper Award(2023년 11월), KAIST Global Research Cooperation Awards(2023년 12월), IEEE TBCAS의 2023년 Best Reviewers 세 명 가운데 한 명(2024년 4월), 2025 KAIST Institutes integrative research award(2025년 12월)가 있고,[^news] 학과 첫 화면 소식은 2026년 봄학기 우수강의상 수상을 알린다.[^bbe] 2023–2025년 소식에는 PowerMEMS School 2023, NYU-KAIST Brain science & Engineering, NAEK(National Academy of Engineering of Korea)가 「AI × BCI」를 주제로 연 Academy Roundtable Discussion, Samsung Electronics Semiconductor Research Institute Symposium 초청 강연이 있다.[^news]

랩 Publications 목록을 시기별로 보면, 2008–2014년 논문에는 전력 증폭기용 공급 변조기와 증폭기, 저전압 강하 조정기(LDO, 입력과 출력의 전압 차이가 작아도 일정한 전압을 내는 전원 회로), 메모리용 지연 고정 루프(DLL), RF 혼합기, 비침습 생리 신호 측정용 회로와 전극 인터페이스가 있고, 2014–2019년 논문은 주로 하나의 유도 결합 연결로 전력과 자료를 함께 보내는 원격 측정 회로, mm 크기 이식 장치용 무선 전력 수신기와 조정 정류기, 신경 기록 ADC, 고밀도 피질 신경 인터페이스, MIMO 기저대역 수신기를 다룬다.[^pubs] 논문으로 보면 지금의 전문 분야는 세 갈래다. 첫째, 자극 잡음을 실시간으로 지우며 신경을 기록하고 자극하는 초소형 신경 인터페이스 회로다(대표 논문 1, 2).[^p1][^p2] 둘째, 무선 전력 전송과 자료 통신 칩이다(대표 논문 3–5).[^p3][^p4][^p5] 셋째, 심전도·뇌파를 재고 기기 안에서 처리하는 착용형·비접촉 측정 시스템과 신호 처리 하드웨어다(대표 논문 6–8).[^p6][^p7][^p8]

## 응용 분야

누리집은 연구 목표를 진단·치료용 의료 기기에 쓰일 뇌-기계 인터페이스와 인공 망막으로 적는다.[^home] 대표 논문은 전임상 연구에서 동물의 신경을 장기간 실시간으로 재는 일,[^p4] 심장 질환을 일찍 찾기 위한 가정의 심전도·심박 변이도 측정,[^p6] 착용형 태아 심전도 측정,[^p7] 뇌파 뇌-컴퓨터 인터페이스[^p8]를 대상으로 하고, 신경 조절 시스템과 무선 전력 전송 칩은 생체 실험으로 확인했다.[^p1][^p3] 소식에는 LGE-KAIST 디지털 헬스케어 연구센터 연례 워크숍의 연구 시연(2023년 10월, 2024년 10월)과 KI 시제품 과제 시연(2025년 12월)이 있다.[^news] 졸업생의 진로로는 Synopsys, Samsung Research, Samsung Electronics, SK Hynix, KIST, Rice University, Slowave, KAIST가 있다.[^members]

## 구성원

2026년 10월 23일 Members 페이지 기준 28명이다. 박사후연구원 1명, 박사과정 칸 9명(그중 1명은 카드에 Integrated MS and PhD로 적힘), 석사과정 7명, 연구원 1명, 학부생 10명이다. 시작은 연구원·학부생 카드의 「Joined in」 표기이고, 연구 주제는 카드의 Research Area, 과정 칸 괄호는 연구원·학부생 카드의 학교·학과 표기, 이메일은 카드의 학교·기관 주소다.[^members] 박사과정과 석사과정에 같은 이름 Minjae Kim(김민재)이 한 명씩 있고 대표 논문 저자 Minjae Kim이 어느 사람인지 가릴 수 없어, 두 행에는 참여 번호를 붙이지 않았다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Jaeouk Cho (조재욱) | 박사후연구원 |  | Wireless Communication System, Multi-channel Neural Recording | jjo2883@kaist.ac.kr | 1, 2, 3, 4, 7 |
| Geunchang Seong (성근창) | 박사과정 |  | Simulation artifact Removal, Real time Signal Processing | sks96007@kaist.ac.kr | 1, 2, 6, 7, 8 |
| Dongyeol Seok (석동열) | 박사과정 |  | Biopotential, Wearable, Motion artifact removal hardware | sukd10@kaist.ac.kr | 1, 6 |
| Minjae Kim (김민재) | 박사과정 |  | In-ear EEG, Wearable sensor | kscimjbravo@kaist.ac.kr |  |
| Jaeseong Park (박재성) | 석박사통합과정 |  | Hardware Spike Sorting, Real time Signal Processing | wotjd0715@kaist.ac.kr | 7, 8 |
| Eojin Kim (김어진) | 박사과정 |  | Energy-Efficient Biomedical System, Neural Stimulator | eojin@kaist.ac.kr |  |
| Sanghyun Lee (이상현) | 박사과정 |  | Motion artifact removal PPG | hyun15@kaist.ac.kr |  |
| Seongjae Moon (문성재) | 박사과정 |  | Power management, Wireless power & data transmission | anstjdwo98@kaist.ac.kr |  |
| Heeyoung Jung (정희영) | 박사과정 |  | Simulation artifact Removal, Real time Signal Processing |  | 1 |
| Daehyeok Park (박대혁) | 박사과정 |  | Non-contact Stimulator, Wearable Device | qkreogur159@kaist.ac.kr | 6, 7 |
| Hyejun Koh (고혜준) | 석사과정 |  | ECG, Wearable device | hyejun171@kaist.ac.kr |  |
| Heegyun Ahn (안희균) | 석사과정 |  | Power management, Wireless power & data transmission | ahqq0315@kaist.ac.kr |  |
| DuHyeong Lee (이두형) | 석사과정 |  | Fetal ECG | dlenguddl@kaist.ac.kr |  |
| HyeonJun Lee (이현준) | 석사과정 |  | In-Ear system | cozy2jun52@kaist.ac.kr |  |
| Hyungwoo Kim (김형우) | 석사과정 |  | Neural Stimulator | albertkim@kaist.ac.kr |  |
| Hyeondong Choi (최현동) | 석사과정 |  | Multi channel ADC | hdchoi403@kaist.ac.kr |  |
| Minjae Kim (김민재) | 석사과정 |  | DC-DC Converter | nicemj9919@kaist.ac.kr |  |
| Na-young Jo (조나영) | 연구원 (Hanyang Electrical Engineering) | November,2025 |  |  |  |
| Junwoo Park (박준우) | 학부 연구생 (KAIST Bio&Brain Engineering) | January,2025 |  | danielpark@kaist.ac.kr |  |
| Chungpil Lee (이충필) | 학부 연구생 (KAIST Electrical Engineering) | Jan,2026 |  | lcp020620@kaist.ac.kr |  |
| Jinhwa Kim (김진화) | 학부 연구생 (KAIST Bio&Brain Engineering) | May,2026 |  | evolkim@kaist.ac.kr |  |
| Lee Damin (이다민) | 학부 연구생 (KAIST Bio&Brain Engineering) | May,2026 |  | vitamindamin@kaist.ac.kr |  |
| Chaejun Kim (김채준) | 학부 연구생 (KAIST Bio&Brain Engineering) | May,2026 |  | chaejungim678@kaist.ac.kr |  |
| Suha Lee (이수하) | 학부 연구생 | May,2026 |  | gogosuha@kaist.ac.kr |  |
| MoonSu Kim (김문수) | 학부 연구생 (KAIST Bio&Brain Engineering) | July,2026 |  | moonsukim03@kaist.ac.kr |  |
| Je Hyung Han (한제형) | 학부 연구생 (New York University Abu Dhabi Electrical Engineering) | July,2026 |  | jh8773@nyu.edu |  |
| Joonseo Park (박준서) | 학부 연구생 (KAIST Bio&Brain Engineering) | July,2026 |  | pvx._.amel@kaist.ac.kr |  |
| Seoyeon Baek (백서연) | 학부 연구생 (Korea University HES & BCS) | July,2026 |  | 22202bsy@korea.ac.kr |  |

## 졸업생과 이전 구성원

Members 페이지 Alumni 칸의 Ph.D 4명과 M.S. 17명이다. 학위 연도는 적혀 있지 않고, 진로는 이름 뒤에 적힌 곳이다. Jaeouk Cho는 Ph.D와 M.S. 칸에 모두 있고 지금 박사후연구원으로도 적혀 있으며, 진로가 「KAIST, Ph.D」인 M.S. 졸업생 가운데 여러 명은 지금 박사과정 구성원이다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Yechan Park | Ph.D | KAIST |
| Hongkyun Kim | Ph.D | Synopsys |
| Jaeouk Cho | Ph.D | KAIST |
| Minseok Park | Ph.D |  |
| Jaeouk Cho | M.S. | KAIST, Ph.D |
| Sanghyun Lee | M.S. | KAIST, Ph.D |
| Geunchang Seong | M.S. | KAIST, Ph.D |
| Yonghee Chang | M.S. | Rice University |
| Dongyeol Seok | M.S. | KAIST, Ph.D |
| Juntae Jang | M.S. | Samsung Research |
| Minjae Kim | M.S. | KAIST, Ph.D |
| Seungjae Yoo | M.S. | KAIST, Ph.D |
| Janghwan Kim | M.S. | Samsung Electronics |
| Hyeongsub Lim | M.S. |  |
| Jiaying Shao | M.S. |  |
| Charnmin Park | M.S. | Slowave |
| Premravee Teeravichayangoon | M.S. | KIST |
| Seongjae Moon | M.S. | KAIST, Ph.D |
| Heeyoung Jung | M.S. | KAIST, Ph.D |
| Daehyeok Park | M.S. | KAIST, Ph.D |
| Yujun Bae | M.S. | SK Hynix |

## 최근 논문 목록 (2021–2026)

Publications 페이지 International Journals의 2021–2026년 구역 18편(2026년 3, 2025년 3, 2024년 2, 2023년 1, 2022년 4, 2021년 5)과, International Conferences 목록에서 줄에 적힌 연도가 2021–2025년인 발표 13건(2025년 3, 2022년 3, 2021년 7)이다. 연도마다 학술지, 학회 순서로 적고, 저자·제목·학술지와 학회 표기는 페이지 그대로다. 학회 목록에 두 번 적힌 같은 ISSCC 2021 발표(33.7)는 한 번만 실었다. 2021년 구역에는 TBioCAS의 ISCAS 2020 특별호 객원 편집자 글(Guest Editorial) 1편이 있다. 학회 목록에는 2026년 항목이 없고, 2026년 CICC 발표 논문은 소식에만 있다.[^pubs][^news]

**2026**

- J. Cho, D. Park, J. Park, M. Kim, G. Seong, Y. Bae, and C. Kim. "On-Device Maternal-Fetal Heart Monitoring from Abdominal ECG Using a NEO-Based Adaptive Predictor". *IEEE Transactions on Biomedical Circuits and Systems*.
- J. Wang, O. Olajide, A. Paul, D. Zhang, J. Wu, Y. Xu, Y. Zou, C. Kim, and G. Cauwenberghs. "A 1024-Channel Hybrid Voltage/Current-Clamp Neural Interface System-on-Chip with Dynamic Incremental SAR Acquisition". *IEEE Transactions on Biomedical Circuits and Systems*.
- G. Seong, J. Cho, H. Jung, M. Kim, D. Seok, S. Jeon, S. Jang, C. Sung, U. Han, S. Park, Y. Cho, and C. Kim. "A Neuromodulation System with Real-Time Neural Signals Recovery Overlapped Temporally and Spectrally with Stimulation Artifacts". *IEEE Transactions on Biomedical Circuits and Systems*.

**2025**

- M. Kim, P. Teeravichayangoan, D. Park, J. Shao, G. Seong, D. Seok and C. Kim. "A Homecare In-Bed Hardware System for Precise Real-Time ECG and HRV Monitoring With Layered Clothing". *Biosensors and Bioelectronics, Aug. 2025*.
- C. Oh, Y.-M. Kim, T. Lee, S.-M. Lee, J. Jung, H.-M. Bae, C. Kim and H. J. Lee. "Patch-Type Capacitive Micromachined Ultrasonic Transducer for Ultrasonic Power and Data Transfer". *Microsystems & Nanoengineering, Jun. 2025*.
- G.-H. Lee, Y. Lee, H. Seo, K. Jo, J. Yeo, S. Kim, J.-Y. Bae, C. Kim, C. Majidi, J. Kang, S.-K. Kang, S. Ryu and S. Park. "Meter-Scale Heterostructure Printing for High-Toughness Fiber Electrodes in Intelligent Digital Apparel". *Nature Communications, May 2025*.
- D. Park, J. Cho, J. Park, M. Kim, G. Seong and C. Kim. "On-Device Fetal ECG Extraction Using NEO-Based Adaptive Predictor for Prenatal Healthcare". *2025 IEEE Biomedical Circuits and Systems Conference (BioCAS), Abu Dhabi, United Arab Emirates, 2025*.
- Y. Park, C. Kim and M. Je. "A Wireless Adiabatic Stimulator System with Current-Mode Power Reception and Stimulus Current Regulation Achieving Precise Charge Delivery and Electrode Scalability for Miniaturized Electroceuticals". *2025 IEEE International Solid-State Circuits Conference (ISSCC), San Francisco, CA, USA, 2025*.
- Y. Park, P. D. Hung, D. Youn, D. Kwon, C. Kim and M. Je. "An Enhanced-Frequency-Splitting-Based Wireless Power and Data Transfer System Achieving 60.2% End-to-End Efficiency and 1 Mb/s Data Rate with a Sub-cm RX Coil for Miniaturized Implants". *2025 IEEE International Solid-State Circuits Conference (ISSCC), San Francisco, CA, USA, 2025*.

**2024**

- J. Wang, R. Liu, Y. Tchoe, A. P. Buccino, A. Paul, D. Pre, A. D’Antonio-Chronowska, F. A. Kelly, A. G. Bang, C. Kim, S. Dayeh and G. Cauwenberghs. "Low-Power Fully Integrated 256-Channel Nanowire Electrode-on-Chip Neural Interface for Intracellular Electrophysiology". *IEEE Transactions on Biomedical Circuits and Systems, Jul. 2024*.
- H. Kim, Y. Park, C. Sung, J. Cho, S. Park and C. Kim. "DiTTO: A Distance Adaptive Over 100-mW Wireless Power Transfer System With 1.695-Mb/s Uplink Telemetry and a Shared Inductor Two-Output Regulating Rectification". *IEEE Journal of Solid-State Circuits, Mar. 2024*.

**2023**

- D. Cho, H. Cho, S. Oh, Y. Jung, S. Ha, C. Kim and M. Je. "A High-Efficiency Single-Mode Dual-Path Buck-Boost Converter With Reduced Inductor Current". *IEEE Journal of Solid-State Circuits, Jan. 2023*.

**2022**

- H. Kim, Y. Park and C. Kim. "A 13.56-MHz Wireless Power Transfer System With a Wide Operating Distance and Load Range for Biometric Smartcards". *IEEE Transactions on Power Electronics, Dec. 2022*.
- Y. Chang, J. Jang, J. Cho, J. Lee, Y. Son, S. Park and C. Kim. "Seamless Capacitive Body Channel Wireless Power Transmission Toward Freely Moving Multiple Animals in an Animal Cage". *IEEE Transactions on Biomedical Circuits and Systems, Aug. 2022*.
- M. Kim, S. Yoo and C. Kim. "Miniaturization for Wearable EEG Systems: Recording Hardware and Data Processing". *Biomedical Engineering Letters, Aug. 2022*.
- H. Cho, J.-H. Suh, C. Kim, S. Ha and M. Je. "An Intra-Body Power Transfer System With >1-mW Power Delivered to the Load and 3.3-V DC Output at 160-cm of On-Body Distance". *IEEE Transactions on Biomedical Circuits and Systems, Jul. 2022*.
- S. Yoo, G. Seong, J. Park and C. Kim. "Zero-Weight aware LSTM Architecture for Edge-Level EEG Classification". *2022 IEEE Biomedical Circuits and Systems Conference (BioCAS), Taipei, Taiwan, 2022*.
- P. D. Hung, H. Shin, Y. Park, N. K. Hoang, D. Cho, S. Ha, C. Kim and M. Je. "A 96.5%-Power-Efficiency Hybrid Buck-Boost Photovoltaic Energy Harvester Employing Adaptive FOCV MPPT Control for >98% MPPT Efficiency Across a 10,000× Dynamic Range". *2022 IEEE Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits), Honolulu, HI, USA, 2022*.
- D Cho, H Cho, S Oh, Y Jung, S Ha, C Kim and M Je. "A Single-Mode Dual-Path Buck-Boost Converter with Reduced Inductor Current Across All Duty Cases Achieving 95.58% Efficiency at 1A in Boost Operation". *2022 IEEE Custom Integrated Circuits Conference (CICC), Newport Beach, CA, USA, 2022*.

**2021**

- Y. Park, S.-T. Koh, J. Lee, H. Kim, J. Choi, S. Ha, C. Kim and M. Je. "A Wireless Power and Data Transfer IC for Neural Prostheses Using a Single Inductive Link With Frequency-Splitting Characteristic". *IEEE Transactions on Biomedical Circuits and Systems, Dec. 2021*.
- A. Akinin, J. M. Ford, J. Wu, C. Kim, H. D. Thacker, P. P. Mercier and G. Cauwenberghs. "An Optically Addressed Nanowire-Based Retinal Prosthesis With Wireless Stimulation Waveform Control and Charge Telemetry". *IEEE Journal of Solid-State Circuits, Oct. 2021*.
- H. Heidari, N. Mcfarlane and C. Kim. "Guest Editorial Special Issue on Selected Papers From IEEE ISCAS 2020". *IEEE Transactions on Biomedical Circuits and Systems, Aug. 2021*.
- J. Cho, G. Seong, Y. Chang and C. Kim. "Energy-Efficient Integrated Circuit Solutions Toward Miniaturized Closed-Loop Neural Interface Systems". *Frontiers in Neuroscience, May. 2021*.
- D. Seok, S. Lee, M. Kim, J. Cho and C. Kim. "Motion Artifact Removal Techniques for Wearable EEG and PPG Sensor Systems". *Frontiers in Electronics, May. 2021*.
- J. Wang, R. Liu, Y. Tchoe, A. P. Buccino, A. Paul, A. D'Antonio-Chronowska, K. A. Frazer, C. Kim, S. Dayeh and G. Cauwenberghs. "Low-Power 256-Channel Nanowire Electrode-on-Chip Neural Interface for Intracellular Electrophysiology". *2021 IEEE Biomedical Circuits and Systems Conference (BioCAS), Berlin, Germany, 2021*.
- D. Cho, H. Shin, H. Park, S. Oh, T. Lee, S. Ha, C. Kim and M. Je. "A Load-Current-Regulating OLED Lamp Driver Using a Hybrid Step-Up Converter with 93.21% Efficiency at a High Conversion Ratio of 4.1". *ESSCIRC 2021 - IEEE 47th European Solid State Circuits Conference (ESSCIRC), Grenoble, France, 2021*.
- P. D. Hung, Y. Park, S. Kweon, T. Lee, H. Jeon, S. Koh, I. Cho, J. Yoon, I. Park, C. Kim, S. Ha and M. Je. "A Self-Powered Wireless Gas Sensor Node Based on Photovoltaic Energy Harvesting". *2021 Symposium on VLSI Circuits, Kyoto, Japan, 2021*.
- H. Shin, D. Jang, G. Kang, J. Kim, C. Kim, S. Ha and M. Je. "A 96.6%-Efficiency Continuous-Input-Current Hybrid Dual-Path Buck-Boost Converter with Single-Mode Operation and Non-Stopping Output Current Delivery". *2021 Symposium on VLSI Circuits, Kyoto, Japan, 2021*.
- Y. Park, S. Koh, J. Lee, H. Kim, J. Choi, S. Ha, C. Kim and M. Je. "33.7 A Frequency-Splitting-Based Wireless Power and Data Transfer IC for Neural Prostheses with Simultaneous 115mW Power and 2.5Mb/s Forward Data Delivery". *2021 IEEE International Solid-State Circuits Conference (ISSCC), San Francisco, CA, USA, 2021*.
- J. Choi, Y. Park, J. Oh, J. Kim, J. Hwang, S. Ha, C. Kim and M. Je. "34.4 An Energy-Replenishing Ultrasound Pulser with 0.25CV2f Dynamic Power Consumption". *2021 IEEE International Solid-State Circuits Conference (ISSCC), San Francisco, CA, USA, 2021*.
- A. Akinin, J. M. Ford, J. Wu, C. Kim, H. D. Thacker, P. P. Mercier and G. Cauwenberghs. "18.1 An Optically-Addressed Nanowire-Based Retinal Prosthesis with 73% RF-to-Stimulation Power Efficiency and 20nC-to-3μC Wireless Charge Telemetering". *2021 IEEE International Solid-State Circuits Conference (ISSCC), San Francisco, CA, USA, 2021*.

## 수상

News 페이지의 2021년 10월 13일 이후 수상 소식 9건(2023년 4월–2026년 5월)이다. 교수 수상 4건과 구성원 수상 5건이며, 날짜는 글머리의 연월이고 문구는 페이지 표기 그대로다.[^news]

- 2026-05 · Hyungwoo received the Outstanding Prize at the 2026 KAIST AI Future Challenge Award
- 2026-04 · Eojin presented our paper at IEEE CICC 2026 and received the Outstanding Student Paper Award.
- 2025-12 · Prof. Kim received a 2025 KAIST Institutes integrative research award.
- 2025-07 · Daehyeok and Eojin received the award at the 2025 Chip Designed Contest.
- 2024-04 · Prof. Kim became an one of the three Best Reviewers of 2023 for IEEE TBCAS
- 2023-12 · Prof. Kim received a KAIST Global Research Cooperation Awards
- 2023-11 · Prof. Kim received a Best Paper Award at the 2023 62th Autumn Conference from The Korean Society of Medical and Biological Engineering (proxy attendance Minjae)
- 2023-10 · Hongkyun received Best Poster Award at the 2023 ISOCC Chip Design Contest
- 2023-04 · Jaeouk received a Best Poster Award at the 30th Korean Conference on Semiconductors 2023

## 소식

News 페이지의 2021년 10월 13일 이후 글 가운데 수상 소식과 새 구성원 합류 글, 학위 취득 축하 글을 뺀 24건(2022년 8월–2026년 4월)이다. 날짜는 글머리의 연월이고 문구는 페이지 표기 그대로다. 고등학생 연구 프로그램(R&E, Pre-srp)의 수상 소식 2건은 연구실 학생이 조교(TA)를 맡은 프로그램 소식이다.[^news]

- 2026-04 · A new paper, "On-Device Maternal-Fetal Heart Monitoring from Abdominal ECG Using a NEO-Based Adaptive Predictor" has been accepted on IEEE Transactions on Biomedical Circuits and Systems (TBioCAS). Congratulations!
- 2026-02 · Dongyeol gave a presentation on The Korean Society for Brain and Neural Sciences.
- 2026-02 · Highschool researchers in R&E program Samsung Humantech Paper Awards (TA: Daehyeok Park, Yujun Bae). Well done!
- 2026-01 · A new paper, "A Simultaneous 16-Channel Adiabatic Charge-Tracking Stimulator with 87.4% Stimulator Efficiency and Low Load Sensitivity" has been accepted on IEEE Custom Integrated Circuits Conference (CICC). Congratulations!
- 2026-01 · Highschool researchers in Pre-srp program won the best prize (TA: Hyejun Koh, DuHyeong Lee ). Well done!
- 2026-01 · New paper, "A Neuromodulation System with Real-Time Neural Signals Recovery Overlapped Temporally and Spectrally with Stimulation Artifacts" has been accepted on IEEE Transactions on Biomedical Circuits and Systems (TBioCAS). Congratulations!
- 2025-12 · Prof. Kim successfully gave a demonstration of the KI prototype project with the students
- 2025-11 · Prof. Kim was invited to give a talk at the recent Samsung Electronics Semiconductor Research Institute Symposium
- 2025-11 · Prof. Kim was invited to give a talk on “Intelligent Low-Power Integrated Circuit Systems for Brain Interfaces” at the Academy Roundtable Discussion. The event was organized by the National Academy of Engineering of Korea (NAEK) and focused on the theme of “AI × BCI.” link: AIxBCI: 뇌와 인공지능의 미래 연결
- 2025-09 · A new conference paper, "On-Device Fetal ECG Extraction Using NEO-Based Adaptive Predictor for Prenatal Healthcare" has been accepted to '2025 IEEE Biomedical Circuits and Systems'.
- 2025-08 · A new paper "A Homecare In-Bed Hardware System for Precise Real-Time ECG and HRV Monitoring With Layered Clothing" has published in Biosensors and Bioelectronics.
- 2024-10 · Prof. Kim was invited to perform a research demonstration at LGE-KAIST Digital Healthcare Research Center Annual Workshop
- 2024-03 · A new paper "DiTTO: A Distance Adaptive Over 100-mW Wireless Power Transfer System With 1.695-Mb/s Uplink Telemetry and a Shared Inductor Two-Output Regulating Rectification" has published in IEEE JSSC.
- 2023-12 · Prof. Kim was invited to give a talk at PowerMEMS School 2023 (Abu Dhabi, UAE)
- 2023-10 · Minjae was invited to give a research demonstration at LGE-KAIST Digital Healthcare Research Center Annual Workshop
- 2023-10 · Prof. Kim was invited to give a talk at NYU-KAIST Brain science & Engineering (NY, USA)
- 2023-06 · Prof. Kim was invited to give a talk at the 7th KAST-Leopldina Bilateral Symposium
- 2023-05 · Prof. Kim was invited to give a talk at the 한국제약바이오헬스케어연합회
- 2023-04 · A new paper, "A 13.56 MHz Wireless Power Transfer System with a Wide Operating Distance and Load Range for Biometric Smartcards" has been published in the IEEE Transactions on Power Electronics (TPE).
- 2023-02 · BEEE members had participated ISSCC 2023, San Francisco, CA
- 2022-10 · BEEE members had participated ISOCC 2022, Gangneung, Korea
- 2022-10 · Seungjae had participated BioCAS 2022, Taipei, Taiwan
- 2022-08 · A new paper, "Zero-Weight aware LSTM Architecture for Edge-Level EEG Classification" will be published in BioCAS
- 2022-08 · A new paper, "Seamless Capacitive Body Channel Wireless Power Transmission Toward Freely Moving Multiple Animals in an Animal Cage" will be published in TBioCAS

## 연락과 위치

- 연구실: 291 Daehak-ro, E16-1 room 508, Yuseong-gu, Daejeon, South Korea 34141(누리집), 바이오및뇌공학과 교수 소개는 연구실을 E16-1 504호로 적는다[^home][^bbeprof]
- 전화: +82-42-350-7345(누리집), 교수 +82-42-350-7305[^home][^members][^bbeprof]
- 교수 이메일: kimchul@kaist.ac.kr[^members][^bbeprof]
[^home]: 연구실 누리집 첫 화면 <https://beee.kaist.ac.kr/> (연구실 소개, 연구 과제, 주소·전화, 2026-10-23 열람)
[^members]: Members 페이지 <https://beee.kaist.ac.kr/home/members> (Principal Investigator, 구성원, Alumni 칸, 2026-10-23 열람)
[^pubs]: Publications 페이지 <https://beee.kaist.ac.kr/home/publications> (International Journals, International Conferences, 2026-10-23 열람)
[^news]: News 페이지 <https://beee.kaist.ac.kr/home/news> (2026-10-23 열람)
[^mni]: Miniaturized Neural Interfaces 페이지 <https://beee.kaist.ac.kr/home/miniaturized-neural-interfaces> (2026-10-23 열람)
[^wban]: Wireless Body-area Networks 페이지 <https://beee.kaist.ac.kr/home/wireless-body-area-networks> (2026-10-23 열람)
[^bbe]: KAIST 바이오및뇌공학과 첫 화면 학과뉴스 <https://bioeng.kaist.ac.kr/> (2026-10-23 열람)
[^bbelist]: KAIST 바이오및뇌공학과 교수진 목록 <https://bioeng.kaist.ac.kr/index.php?mid=bio_03_01&category=8951> (2026-10-23 열람)
[^bbeprof]: KAIST 바이오및뇌공학과 교수 소개(김철) <https://bioeng.kaist.ac.kr/index.php?document_srl=12213&mid=bio_03_01> (직위, 연구실명, 최종학위, 연구분야, 경력, 대외활동, 수상 경력, 2026-10-23 열람)
[^p1]: G. Seong 외, C. Kim, IEEE Transactions on Biomedical Circuits and Systems 20, 446-457 (2026). <https://doi.org/10.1109/tbcas.2026.3654961> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J. Cho, G. Seong, Y. Chang, C. Kim, Frontiers in Neuroscience 15, 667447 (온라인 2021-05-31). <https://doi.org/10.3389/fnins.2021.667447> 초록 기준.
[^p3]: H. Kim 외, C. Kim, IEEE Journal of Solid-State Circuits 59, 2568-2580 (2024). <https://doi.org/10.1109/jssc.2024.3372418> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: Y. Chang 외, C. Kim, IEEE Transactions on Biomedical Circuits and Systems 16, 714-725 (2022). <https://doi.org/10.1109/tbcas.2022.3199455> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: H. Kim, Y. Park, C. Kim, IEEE Transactions on Power Electronics 38, 5576-5585 (2023). <https://doi.org/10.1109/tpel.2022.3232609> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: M. Kim 외, C. Kim, Biosensors and Bioelectronics 289, 117838 (2025). <https://doi.org/10.1016/j.bios.2025.117838> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: D. Park 외, C. Kim, 2025 IEEE Biomedical Circuits and Systems Conference (BioCAS), 190-194 (2025). <https://doi.org/10.1109/biocas67066.2025.00050> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: S. Yoo, G. Seong, J. Park, C. Kim, 2022 IEEE Biomedical Circuits and Systems Conference (BioCAS), 472-476 (2022). <https://doi.org/10.1109/biocas54905.2022.9948628> 초록 기준(Semantic Scholar 등록 초록).

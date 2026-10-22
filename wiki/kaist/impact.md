# 집적 회로 및 마이크로 시스템 연구실 (IMPACT Lab)

**KAIST 전기및전자공학부 · 제민규 교수**

- 분야: 센서 인터페이스 집적 회로, 무선 통신 집적 회로, 마이크로 시스템 융합(의료기기, 사물인터넷, 웨어러블 응용)
- 대분야: 전기전자·반도체·광학
- 태그: 집적회로 설계[^research][^eeprof][^p1], 신경 인터페이스·뇌-컴퓨터 인터페이스[^sensor][^p2][^p8], 이식형·생체 전자 기기[^system][^p4][^p5], 무선 전력 전송[^energy][^p5], 무선·이동통신[^wireless], 정밀 타이밍·시간 주파수 전송[^timing][^p7], 메모리 내 연산[^computing][^p8], AI 반도체·가속기[^computing][^p8]
- 홈페이지: <https://impact.kaist.ac.kr/>
- 근거와 출처: [집적 회로 및 마이크로 시스템 연구실 근거 페이지](impact-sources.md)

> 센서 신호를 읽는 회로, 무선 통신 회로, 전력을 공급하는 회로, 시간을 재는 회로, 계산하는 회로를 집적회로로 설계하고, 이를 모아 몸에 넣는 의료 기기·무선 센서 노드·모바일 기기 같은 작은 마이크로시스템을 만드는 연구실이다.[^research][^eeprof]

## 무엇을 연구하나

연구실은 차세대 집적회로 기술을 바탕으로 삼아 작게 만든 지능형 의료 기기, 곳곳에 두는 무선 센서 노드, 미래의 모바일 기기 같은 마이크로시스템(센서·회로·전원·통신을 작은 크기로 한데 묶은 시스템)을 만드는 것을 목표로 한다고 소개한다.[^research] 연구 페이지는 이런 시스템에서 집적회로가 맡는 일로 여러 센서·구동기와 매끄럽게 잇는 인터페이스, 여러 에너지원(특히 재생 가능한 에너지원)으로 높은 효율을 내는 동작, 높은 집적과 소형화, 내장 지능, 통신 연결을 든다.[^research] 첫 화면 소개는 2016년 KAIST에서 시작한 연구실로, 새 회로 설계 기법을 만드는 데 그치지 않고 센서·에너지·통신·패키징·의료 기기·IT 응용 분야의 전문가와 국제 협력 연구망으로 함께 일한다고 적는다.[^home]

연구 페이지는 연구를 여섯 묶음으로 나눈다. 센서 인터페이스 IC, 시스템 통합과 응용, 무선 통신 IC, 에너지 공급·관리 IC, 타이밍 IC, 컴퓨팅 IC다.[^research] 전기및전자공학부 교수 소개는 교수의 주요 연구를 센서 인터페이스 집적회로, 무선 통신 집적회로, 의료 기기·사물인터넷·웨어러블 응용을 위한 마이크로시스템 융합으로 적는다.[^eeprof]

시스템 통합 쪽에서는 이렇게 만든 회로로 사물인터넷 센서 노드, 모바일·웨어러블 기기, 몸 안에 넣거나 찔러 넣는 감지 기기, 신경 인터페이스, 수술 내비게이션 도구 같은 마이크로시스템을 만들어 왔고, 그 과정에서 다른 분야 연구진과 가깝게 협력했다고 연구 페이지는 적는다.[^system] 2021–2026년 학술지 목록에도 캡슐 내시경용 초음파 송수신 칩과 무선 송신기, 인공와우용 신경 자극 칩, 복강경 수술에서 병변 위치를 찾는 자기 센서 시스템, 휠체어 환자의 압력·온도·수분을 재는 무선 센서가 있다.[^journals]

대표 논문으로 보면 연구는 다섯 갈래다. 첫째, 몸의 전기 임피던스와 신경 신호, 초음파 신호를 읽는 센서 인터페이스 칩이다(대표 논문 1, 2, 3).[^p1][^p2][^p3] 둘째, 몸을 통로로 삼아 데이터를 보내는 인체 채널 통신이다(대표 논문 4).[^p4] 셋째, 몸에 넣는 기기에 전력과 데이터를 함께 보내는 무선 전력 전송과, 배터리로 움직이는 기기의 DC-DC 변환기(직류 전압을 다른 직류 전압으로 바꾸는 회로)다(대표 논문 5, 6).[^p5][^p6] 넷째, 적은 전력으로 시간을 재는 칩 안 타이머다(대표 논문 7).[^p7] 다섯째, 메모리 안에서 계산하는 회로로 뇌 신경 신호를 분류하는 칩이다(대표 논문 8).[^p8]

## 주요 연구 주제

### 1. 센서 인터페이스 IC

센서 인터페이스 IC는 현실 세계의 정보를 얻는 수단으로, 연구실은 생체 의료·무선 센서망을 위한 초저전력 설계, 산업 감시·항법·가전을 위한 고정밀 감지, 자동차·항공우주·석유가스 산업을 위한 고온 동작을 연구 관심으로 든다.[^sensor] 이를 위해 아날로그 전단(AFE, 센서 신호를 처음 받아 키우고 거르는 회로)과 데이터 변환 회로를 새로 설계해 MEMS·CMOS·나노·바이오·광 센서와 묶는다.[^sensor] 세부 갈래는 양방향 폐루프 신경 인터페이스(뇌 신호를 읽고 그 결과에 따라 자극하는 장치)를 위한 신경 자극·기록 칩, 압전 트랜스듀서(PZT)와 정전용량형 미세가공 초음파 트랜스듀서(CMUT)에 잇는 초음파 송수신기, 분자·세포·조직의 정보를 얻는 임피던스 측정 칩이다.[^sensor] 대표 논문으로는 위상이 크게 어긋난 생체 임피던스에서도 잡음을 지우는 판독 칩, 입력 크기에 따라 이득을 스스로 바꾸는 신경 신호 기록 칩, 초음파 캡슐 내시경용 송수신 칩이 있다.[^p1][^p2][^p3] 대표 논문 1, 2, 3.

### 2. 무선 통신 IC와 인체 채널 통신

개인 영역 무선망(WPAN), 몸 주변 무선망(WBAN), 무선 센서망(WSN)을 위한 차세대 무선 칩을 만든다. 낮은 전력으로 여러 채널을 다루고, 영상·배열 기록에 필요한 높은 데이터 속도를 좁은 대역폭으로 내며, 몸 안에서 1 GHz 아래 넓은 대역으로 통신하는 것 등을 과제로 든다.[^wireless] 캡슐 내시경의 고해상도 영상이나 이식형 신경 기록 장치의 많은 데이터를 보내는 저전력 송신기, 생체 의료·사물인터넷용 저전력 수신기와 웨이크업 수신기(기기를 필요할 때만 깨우는 신호를 받는 수신기)를 설계한다.[^wireless] 몸을 신호 통로로 쓰는 인체 채널 통신(BCC)은 큰 전력의 송수신기와 부피 큰 안테나 없이 몸 주변 기기를 잇는 방법으로 다룬다.[^wireless] 대표 논문 4는 인공 팔다리를 조종하려고 몸에 넣은 여러 칩이 갈바닉 결합 인체 채널 통신으로 동시에 데이터를 보내게 했다.[^p4] 석유·가스 시추관을 따라 음파로 데이터를 보내는 음향 원격 측정 칩도 연구 항목에 있다.[^wireless] 대표 논문 4.

### 3. 에너지 공급·관리 IC

기기의 에너지원은 배터리, 무선 전력 전송, 에너지 하베스팅(주변의 움직임·열·빛에서 작은 전력을 모으는 기술)으로 다양하며, 연구실은 이 세 가지 에너지원 모두에 맞는 에너지 공급·관리 칩을 만들어 왔다고 적는다.[^energy] 무선 전력 전송 칩은 생체 의료 시스템에 넣어 보여 왔고, DC-DC 변환기는 벅(강압)·벅부스트·하이브리드 구조로 빠른 응답, 넓은 입력 전압 범위, 높은 전력 효율을 노린다.[^energy] 최근에는 몸에 걸친 기기가 전원과 떨어져 있어도 몸을 통해 전력을 보내는 체내 전력 전송(IBPT) 칩도 연구한다.[^energy] 대표 논문으로는 작은 코일 한 쌍으로 이식 기기에 전력과 데이터를 함께 보내는 시스템과, 리튬이온 배터리 기기용 벅부스트 변환기가 있다.[^p5][^p6] 대표 논문 5, 6.

### 4. 타이밍 IC와 컴퓨팅 IC

타이밍 IC는 디지털 동작의 시스템 클럭, 샘플링 클럭, 주파수 합성의 기준 클럭, 기기가 쉬는 동안 시간을 재는 슬립 타이머로 쓰인다. 연구실은 무선 센서 노드와 이식형 의료 기기 같은 작은 칩에 필요한 저전력·고정밀 CMOS 발진기를 연구하며, RC 이완 발진기(축전기를 충전·방전하는 시간으로 주기를 만드는 발진기)에서 비교기의 오프셋을 스스로 지우는 방식을 내놓았다.[^timing] 대표 논문 7은 공정이 미세해져도 적은 전력으로 동작하는 칩 안 슬립 타이머다.[^p7] 컴퓨팅 IC에서는 데이터를 메모리와 프로세서 사이로 옮기지 않고 메모리 안에서 계산하는 메모리 내 연산(CIM) 회로를 SRAM·임베디드 플래시 등 여러 메모리로 만들고, 신경 신호의 스파이크 분류, 발작 검출·분류, 신경망 검증 엔진 같은 특정 용도 가속기 칩과 알고리즘·하드웨어 공동 설계를 연구한다.[^computing] 대표 논문 8은 아날로그 메모리 내 연산으로 뇌 신경 신호를 분류하는 칩이다.[^p8] 대표 논문 7, 8.

## 대표 논문

랩 International Journals 목록의 2021–2026년 학술지 논문 가운데 제민규 교수가 마지막 저자인 논문을, 다섯 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^journals] |
|---|---|---|---|---|
| 1 | 2024 | [A Bio-Impedance Readout IC With Complex-Domain Noise-Correlated Baseline Cancellation](https://doi.org/10.1109/jssc.2024.3439865) · IEEE Journal of Solid-State Circuits (JSSC) | 몸에 약한 전류를 흘려 생기는 전압으로 생체 임피던스(bioZ)를 재는 판독 칩이다. 큰 기본값(기준선)을 빼고 작은 변화만 키워 읽는 기존 기준선 제거는 전류원 잡음의 상관을 실수 영역에서만 다뤄, 전류원의 전류와 몸에 걸리는 전압 사이 위상이 크게 어긋나면 한계가 있었다. 이 연구는 크기와 위상을 모두 몸의 임피던스에 맞추도록 조절하는 기준 임피던스(TRI)를 두고, 같은 전류를 두 쪽에 흘려 두 쪽의 전류원 잡음이 함께 움직이게 했다. 그래서 위상이 크게 어긋나도 기준선을 뺀 뒤 전류원 잡음을 지울 수 있다. 기준선을 빼는 데 쓰는, 전력이 적고 입력 범위가 넓은 계측 증폭기(DD-CBIA)도 내놓았다. 측정에서 위상 30°와 60°인 임피던스의 잡음 성능이 각각 2.47배, 4.88배 좋아졌고, 신호 대 잡음비 101.5 dB를 얻었다. 가슴과 손목에 전극 두 개를 붙인 사람 대상 실험으로 효과를 확인했다.[^p1] | 공동 1저자 H. Choi·S.-I. Cheon(†), 마지막 저자 제민규 (7명) |
| 2 | 2022 | [A Wide-Dynamic-Range Neural-Recording IC With Automatic-Gain-Controlled AFE and CT Dynamic-Zoom ΔΣ ADC for Saturation-Free Closed-Loop Neural Interfaces](https://doi.org/10.1109/jssc.2022.3188626) · IEEE Journal of Solid-State Circuits (JSSC) | 입력 신호 크기에 따라 증폭 정도(이득)를 자동으로 바꾸는 신경 신호 기록 칩이다. 자동 이득 조절로 기록할 수 있는 신호 크기의 범위(동적 범위)를 30 dB 넘게 넓히고, 앞단에서 증폭하는 방식과 바로 디지털로 바꾸는 방식의 장점을 함께 얻는다. 아날로그 전단의 이득을 상황에 맞게 바꿔 넓은 동적 범위를 지키면서 전체 잡음을 크게 줄였다. 두 단계로 디지털 값을 만드는 연속 시간 동적 줌 델타시그마 ADC를 쓰는데, 거친 변환 결과는 이득 조절에 다시 쓰고 정밀 변환의 해상도는 이득에 맞춰 바꾼다. 5 kHz 대역에서 동적 범위 99.5 dB, 입력 환산 잡음 6.1 μVrms, 유효 비트 수 11.4비트를 얻었고, 차동 전압 1.6 Vpp까지의 아티팩트(신호에 섞여 드는 큰 방해 신호)를 견딘다. 펄스 모양 아티팩트를 넣은 측정과 생체 내 실험으로 폐루프 신경 인터페이스에 쓸 수 있음을 확인했다.[^p2] | 1저자 Y. Jung, 마지막 저자 제민규 (9명) |
| 3 | 2023 | [A Wide-Bandwidth Ultrasound Receiver and On-Chip Ultrasound Transmitter for Ultrasound Capsule Endoscopy](https://doi.org/10.1109/jssc.2023.3276130) · IEEE Journal of Solid-State Circuits (JSSC) | 초음파 캡슐 내시경을 위해 전력 효율이 높은 초음파 수신기와 고전압 송신기를 한 칩에 담았다. 캡슐은 이 칩, 압전 트랜스듀서 하나, 기계적으로 도는 반사판으로 위장관을 지나가며 장벽을 360° 훑는다. 작은 배터리로 움직이므로 전력 효율이 중요하다. 그래서 빠르고 전력을 많이 쓰는 ADC 대신, 들어오는 초음파와 위상을 맞춘 신호로 초음파의 겉모양(포락선)만 아날로그로 뽑아 회로 경로 하나로 처리하는 수신기 구조를 내놓았다. 해상도를 높이면서 전력을 적게 쓰는 핑퐁 잡음 성형 SAR ADC를 쓰고, 칩 안 전하 펌프로 압전 소자를 울릴 고전압 펄스를 만든다. 0.18 μm BCD 공정으로 만든 칩에서 수신기는 2.3 mW를 쓰고 ADC의 신호 대 잡음·왜곡비는 53.71 dB였으며, 송신기는 폭 25 ns의 25 V 펄스를 낸다. 이 칩을 쓴 시제품 캡슐로 물탱크와 맞춤 팬텀(인체 조직 대신 쓰는 시험체)의 초음파 B 모드 영상을 얻었다.[^p3] | 1저자 K. Jeong, 마지막 저자 제민규 (8명) |
| 4 | 2025 | [An Implantable Peripheral Nerve Interface System With Simultaneous Multi-Site Data Transmission via Galvanically Coupled Body-Channel Communication for Next-Generation Prosthetic Limbs](https://doi.org/10.1109/ojsscs.2025.3642787) · IEEE Open Journal of the Solid-State Circuits Society (OJ-SSCS) | 인공 팔다리를 섬세하고 늦지 않게 조종하려고, 몸에 넣은 여러 칩이 동시에 데이터를 보낼 수 있게 한 신경 이식 시스템이다. 몸을 전류 통로로 쓰는 갈바닉 결합 인체 채널 통신(GC-BCC)을 쓴다. 초음파나 무선 주파수로 데이터를 올려 보내는 방식은 여러 이식 기기 사이 충돌을 피하려고 다중 접속 방식이 필요하고, 정전 결합 방식 인체 채널 통신은 움직임에 따라 바뀌는 작은 귀환 경로 때문에 신호가 약해진다. GC-BCC는 송신기와 수신기 쌍마다 전용 종단으로 닫힌 전류 경로를 만들어, 다중 접속 방식 없이 여러 쌍이 동시에 보낼 수 있다. 180 nm CMOS 공정으로 16채널 신경 기록 전단, GC-BCC 송수신기, LDO 레귤레이터를 한 시스템에 넣었다. 돼지 조직 15 mm를 사이에 두고 20 Mb/s에서 비트 오류율 1.3×10⁻⁵ 아래를 유지했고, 1.6 cm 이상 떨어진 송수신기 두 쌍이 동시에 동작해도 서로 간섭이 무시할 만했다. 비트당 에너지는 송신기 20.35 pJ, 수신기 467.4 pJ이었다.[^p4] | 공동 1저자 D.-H. Choi·D. Lee(†), 마지막 저자 제민규 (9명) |
| 5 | 2025 | [A Wireless Power and Data Transfer System for Medical Implants Using a Miniaturized Inductive Link With Frequency-Splitting Enhancement](https://doi.org/10.1109/jssc.2025.3611278) · IEEE Journal of Solid-State Circuits (JSSC) | 몸에 넣는 의료 기기에 작은 코일 한 쌍(유도 결합 링크)으로 전력과 데이터를 동시에 보내는 시스템이다. 데이터는 주파수 분리 현상을 키워 만든 주파수 편이 변조(FSK, 주파수를 바꿔 0과 1을 보내는 방식)로 보내고, 이를 위해 공진하는 동안 부하를 잠시 떼어 내는 동적 링크-부하 분리와 시간을 나눠 번갈아 쓰는 LC 공진을 쓴다. 이렇게 해서 부하에 전달하는 전력, 데이터 속도, 전력 전송 효율 사이의 기존 맞바꿈 관계를 풀었다. 부하 분리는 출력 전압을 높이고 조절하는 준공진 승압 변환기로 구현했고, 링크 조건이 바뀌어도 정점 시점을 정확히 잡는 검출기와, 포락선 차이를 키워 작은 링크에서도 데이터를 안정적으로 읽게 하는 주파수-진폭 변환기를 넣었다. 180 nm BCD 공정으로 만든 칩은 1 cm보다 작은 수신 코일로 전체 전력 전송 효율 60.2%, 부하 전력 43.4 mW, 데이터 속도 1 Mb/s를 함께 얻었다. 전력 전달 성능 지수는 코일 한 쌍만 쓰는 이전 최신 시스템보다 2.5배 좋아졌다.[^p5] | 1저자 Y. Park, 마지막 저자 제민규 (6명) |
| 6 | 2023 | [A High-Efficiency Single-Mode Dual-Path Buck-Boost Converter With Reduced Inductor Current](https://doi.org/10.1109/jssc.2022.3230424) · IEEE Journal of Solid-State Circuits (JSSC) | 리튬이온 배터리로 움직이는 모바일 기기를 위한 단일 모드 이중 경로 벅부스트(전압을 낮추기도 높이기도 하는) 변환기(SDBBC)다. 플라잉 커패시터(스위치로 연결을 바꿔 가며 쓰는 축전기) 두 개와 인덕터 하나로 된 하이브리드 구조로, 강압과 승압을 회로 구성 전환 없이 한 가지 모드로 이어서 처리한다. 두 커패시터가 만드는 두 번째 경로로 인덕터를 늘 부하에 이어 두어, 모든 변환 비율에서 인덕터 평균 전류가 부하 전류보다 작아 전도 손실과 스위치 전환 손실이 적다. 그래서 변환 범위 전체에서 끊김 없이 높은 효율을 낸다. 직류 저항 175 mΩ인 인덕터로도 최고 효율 94.8%를, 직류 저항 19 mΩ인 큰 인덕터로는 부하 전류 1 A의 승압 동작에서 효율 95.58%를 얻었다.[^p6] | 1저자 D. Cho, 마지막 저자 제민규 (7명) |
| 7 | 2023 | [A Process-Scalable Ultra-Low-Voltage Sleep Timer With a Time-Domain Amplifier and a Switch-Less Resistance Multiplier](https://doi.org/10.1109/jssc.2023.3290357) · IEEE Journal of Solid-State Circuits (JSSC) | 칩 안에 넣는 슬립 타이머(기기가 쉬는 동안 깨어날 때를 재는 회로)다. 조회 표(LUT)와 전용 온도 센서로 온도에 따른 정확도를 높일 수 있지만, 공정이 미세해지고 온도가 오르면 누설 전류가 크게 늘어 에너지 효율을 지키기 어렵다. 이 연구는 초저전압(ULV) 주파수 고정 루프(FLL) 구조, 시간 영역 증폭기, 게이트 누설 전류를 이용해 스위치 없이 저항 값을 키우는 저항 배율기로 이 한계를 넘었다. 65 nm CMOS 공정으로 만든 칩은 0.4 V 전원에서 63 nW만 쓰며 180 kHz 주파수를 내고, 조회 표 보정으로 온도 의존도 2.73 ppm/°C를 얻었다.[^p7] | 1저자 C. Jung, 마지막 저자 제민규 (5명) |
| 8 | 2026 | [A Spike Sorting SoC With Δ-Based Spike Detection and End-to-End Implementation of Autoencoder Feature Extraction Using Analog CIM](https://doi.org/10.1109/jssc.2025.3589523) · IEEE Journal of Solid-State Circuits (JSSC) | 폐루프 뇌-컴퓨터 인터페이스가 제때 반응하려면, 칩이 기록한 많은 신경 신호를 짧은 지연으로 처리하는 스파이크 분류 칩이 필요하다. 이 연구는 변화량(Δ) 기반 스파이크 검출과, 아날로그 메모리 내 연산(CIM)으로 만든 이진 오토인코더 신경망(B-AENN) 특징 추출을 칩 하나에 처음부터 끝까지 넣어 계산 에너지를 줄이면서 정확도를 지켰다. Δ 신호는 잡음에 강하고 특징 추출의 바탕도 좋게 해 정확도를 높이며, 신경망으로 특징을 뽑으면 미리 정한 방법보다 서로 닮은 스파이크도 유연하게 가린다. 검출과 특징 추출을 아날로그 영역으로 옮겨, 채널이 빽빽해질수록 커지는 ADC 변환 병목을 피했다. 65 nm CMOS 공정으로 만든 칩은 계산 지연 5.1 μs, 분류 정확도 94.54%를 보였고 채널당 3.11 μW를 썼다.[^p8] | 공동 1저자 V. Lukito·E. J. Choi(†), 마지막 저자 제민규 (5명) |

## 교수와 전문 분야

제민규 교수는 KAIST 전기및전자공학부 교수이고 Circuit 디비전에 속한다.[^eelist][^eeprof] 반도체시스템공학과 교수진에도 연구분야 「반도체 시스템 및 집적회로」, 연구실 「집적 회로 및 마이크로 시스템 연구실」로 올라 있다.[^ssep] 전기및전자공학부 교수 소개의 주요 연구분야는 AI & Machine Learning, Multimedia Signal Processing, Human Computer Interaction, Integrated Circuits & Semiconductor Systems, Semiconductor Devices & Nanotechnology, Biomedical Engineering, RF/mmWave Devices & Systems다.[^eeprof]

연구실 PI 페이지에 따르면 교수는 KAIST에서 전기및전자공학(EECS) 석사(1998)와 박사(2003)를 받았다.[^pi] 2003년 삼성전자(기흥)에 Senior Engineer로 들어가 GSM/GPRS/EDGE/WCDMA 표준용 다중 모드·다중 대역 RF 송수신 SoC를 개발했고, 2006–2013년 싱가포르 A*STAR의 Institute of Microelectronics(IME)에서 Senior Research Engineer, Member of Technical Staff, Senior Scientist, Deputy Director를 거쳤다.[^pi] IME에서는 2011–2013년 Integrated Circuits and Systems Laboratory를 Department Head로 이끌며 의료용 동작 감지를 위한 3차원 가속도계 ASIC, DNA·RNA와 단백질 바이오마커를 찾는 나노와이어 바이오센서 배열 판독 ASIC, 실시간 무선 건강 감시용 초저전력 센서 노드 SoC, 무선 이식형 센서 ASIC 등의 과제를 맡았다.[^pi] 같은 시기 A*STAR Science and Engineering Research Council의 NeuroDevices Program Director(2011–2013)와 National University of Singapore 겸임 조교수(2010–2013)를 지냈다. 2014–2015년 DGIST Department of Information and Communication Engineering 부교수를 거쳐 2016년부터 KAIST 전기및전자공학부에 있다.[^pi]

PI 페이지 소개 글은 교수가 책 1권을 엮고 책 속 장 6편을 썼으며, 센서 인터페이스 IC, 무선 IC, 생체 의료 마이크로시스템, 3차원 IC, 소자 모델링, 나노전자 분야에서 360편이 넘는 국제 학회·학술지 논문과 70건이 넘는 등록·출원 특허를 냈다고 적는다.[^pi] ISSCC, A-SSCC, VLSI 회로 심포지엄(SOVC) 등 국제 학회의 기술 프로그램 위원회와 조직 위원회에서 활동했고, 2020–2022년 IEEE Circuits and Systems Society Distinguished Lecturer였다.[^pi] 연구실 수상 목록은 교수가 The Institute of Semiconductor Engineers(ISE)의 해동반도체공학상(2022년 12월)과 KAIST 교수혁신상(2025년 5월)을 받았다고 적는다.[^awards] 전기및전자공학부 교수 소개가 대표 업적으로 드는 다섯 편은 2013–2016년 논문(신경 기록 칩, 인체 채널 통신 송수신기, 머리뼈 안 다중 감시 SoC, 기준 클럭 발진기, 전기 자극용 무선 전력 관리·데이터 원격 측정 칩)이고, 그 가운데 2013–2015년 네 편은 KAIST 부임 전 시기의 연구다.[^eeprof]

논문으로 보면 KAIST에서의 전문 분야는 생체 임피던스·신경 신호·초음파를 읽는 센서 인터페이스 회로(대표 논문 1, 2, 3),[^p1][^p2][^p3] 인체 채널 통신(대표 논문 4),[^p4] 이식 기기용 무선 전력·데이터 전송과 DC-DC 변환기(대표 논문 5, 6),[^p5][^p6] 저전력 타이머(대표 논문 7),[^p7] 아날로그 메모리 내 연산 칩(대표 논문 8)이다.[^p8]

## 응용 분야

대표 논문들은 사람의 가슴·손목에서 재는 생체 임피던스(대표 논문 1), 폐루프 신경 인터페이스(대표 논문 2), 초음파 캡슐 내시경(대표 논문 3), 인공 팔다리를 조종하는 신경 이식 장치(대표 논문 4), 몸에 넣는 의료 기기의 전력·데이터 공급(대표 논문 5), 리튬이온 배터리로 움직이는 모바일 기기의 전원(대표 논문 6), 폐루프 뇌-컴퓨터 인터페이스의 스파이크 분류(대표 논문 8)를 겨냥한다.[^p1][^p2][^p3][^p4][^p5][^p6][^p8] 연구 페이지는 이 밖에 산업 감시·항법용 고정밀 센서와 원자력 발전소 사고를 일찍 알리는 방사선 센서 칩, 석유·가스 시추관의 음향 데이터 통신, 몸을 통한 전력 전송, 수술 내비게이션을 연구 항목으로 든다.[^sensor][^wireless][^energy][^system]

## 구성원

연구실 누리집 Researchers 페이지의 박사후연구원 6명, Ph.D. Students 페이지의 21명(석박사통합과정 5명 포함), M.S. Students 페이지의 20명이다.[^researchers][^phd][^ms] 과정과 시작 시점은 각 사람의 학력 칸에서 「~」로 이어진 현재 과정 줄의 표기이고, 이 줄이 없는 사람은 카드의 과정 표기를 따랐다. 연구 주제는 Research interest 칸이 있는 사람만 적었다. 정기 방문 교수(Regular Visiting Professor) 페이지에는 New York University Abu Dhabi의 Sohmyung Ha 조교수가 올라 있다.[^visiting] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Hyunwoo Park | 박사후연구원 |  |  | hwpark15@kaist.ac.kr |  |
| Yechan Park | 박사후연구원 |  |  | yechan.park@kaist.ac.kr | 5 |
| Donghyeon Yi | 박사후연구원 |  | Compute-in-Memory (CiM) Circuits and Architectures with Analog-Mixed-Signal (AMS) Processing Techniques | yicoreen@kaist.ac.kr |  |
| Yegeun Kim | 박사후연구원 |  |  | ygkim1997@kaist.ac.kr |  |
| Gichan Yun | 박사후연구원 |  | Ultrasound Imaging System; Sensor Interface IC Design; Mixed-signal IC Design | ygc980215@kaist.ac.kr | 1, 3, 4 |
| Daehyeon Kwon | 박사후연구원 |  | Frequency synthesizer; IC design for Low-Power wireless Communication | eogus47@kaist.ac.kr | 5 |
| Young-Han Kim | 박사과정 |  | Emerging low-power RF/analog integrated circuit design; Wireless communication, wireless power transfer and RF application system | ekmyph@kaist.ac.kr |  |
| Changhun Seok | 박사과정 | 2021.3 | Sensor Interface IC Design; Biomedical System Design | schun0302@kaist.ac.kr |  |
| Christopher Santos | 박사과정 | 2021.9 |  | christopher.santos@kaist.ac.kr |  |
| Vincent Lukito | 석박사통합과정 | 2021.3 |  | lukitov@kaist.ac.kr | 8 |
| Haidam Choi | 박사과정 | 2022.9 |  | haidam97@kaist.ac.kr | 1 |
| Kim Hoang Nguyen | 박사과정 | 2022.9 |  | nkhoang@kaist.ac.kr | 4 |
| Dong-Hwi Choi | 박사과정 | 2022.9 |  | dhchoi@kaist.ac.kr | 4 |
| Heewon Choee | 박사과정 | 2022.3 |  | choee97@kaist.ac.kr |  |
| Jimin Koo | 박사과정 | 2023.3 |  | jimin_koo@kaist.ac.kr | 2 |
| Hyunyeop Lee | 박사과정 | 2023.3 | Body channel communication | hyl@kaist.ac.kr | 4 |
| Yunchul Chung | 박사과정 | 2023.9 |  | ytony357@kaist.ac.kr | 4 |
| Byeongseon Choi | 석박사통합과정 | 2022.3 |  | cbs5394@kaist.ac.kr | 4 |
| Woongro Youn | 박사과정 | 2024.3 |  | voogi3925@kaist.ac.kr |  |
| Dongyoon Lee | 석박사통합과정 | 2022.9 | Body Channel Communication (BCC); Human Body Communication (HBC) | dongyoon.lee@kaist.ac.kr | 4 |
| Hyunah Park | 박사과정 | 2025.3 |  | hyunah.park@kaist.ac.kr |  |
| Thi Quynh Trang Nguyen | 석박사통합과정 | 2024.3 |  | quynhtrangnguyen@kaist.ac.kr |  |
| Jongho Kim | 박사과정 | 2025.9 |  | jongho@kaist.ac.kr |  |
| Joowon Kim | 박사과정 | 2025.9 |  | ssjazzss@kaist.ac.kr |  |
| Hyeongju lee | 박사과정 | 2026.3 |  | leehj@kaist.ac.kr |  |
| Hyeonbin Park | 박사과정 | 2026.9 |  | hyeonbin@kaist.ac.kr |  |
| Dogyun Bae | 석박사통합과정 | 2025.3 |  | dogyunbae@kaist.ac.kr |  |
| Dongyeob Ra | 석사과정 | 2021.3 |  | rastatine38@kaist.ac.kr |  |
| Minjeong Kang | 석사과정 | 2024.3 |  | mjkang@kaist.ac.kr |  |
| Dohee Kim | 석사과정 | 2025.3 |  | paigeekim@kaist.ac.kr |  |
| Seungjun Park | 석사과정 | 2025.3 |  | soonpark1128@kaist.ac.kr |  |
| Jaejun Lee | 석사과정 | 2025.3 |  | jj.lee@kaist.ac.kr |  |
| Hoyoung Gong | 석사과정 | 2025.9 |  | hoyoung3921@kaist.ac.kr |  |
| Ungju Na | 석사과정 | 2025.9 |  | ungju.na@kaist.ac.kr |  |
| Yoonjung Choi | 석사과정 | 2025.9 |  | yoonjchoi@kaist.ac.kr |  |
| Raiyan Hasan | 석사과정 | 2025.9 |  | raiyan@kaist.ac.kr |  |
| Changseok Lee | 석사과정 | 2026.2 |  | dlckdtjr0907@kaist.ac.kr |  |
| Jinwoo Lee | 석사과정 | 2026.2 |  | jinwoo.lee@kaist.ac.kr |  |
| Jaegeun Lee | 석사과정 | 2026.2 |  | ljg2231@kaist.ac.kr |  |
| Jeongeun Kim | 석사과정 | 2026.2 |  | estherkje@kaist.ac.kr |  |
| Hyunjin Park | 석사과정 | 2026.2 |  | hyunjin.park@kaist.ac.kr |  |
| Juhyeong Kim | 석사과정 | 2026.8 |  | juhyeong.kim@kaist.ac.kr |  |
| Sanghyun Kim | 석사과정 | 2026.8 |  | sanghyun.kim@kaist.ac.kr |  |
| Jaegeon Lee | 석사과정 | 2026.8 |  | jg.lee@kaist.ac.kr |  |
| Gaeun Lee | 석사과정 | 2026.8 |  | inchillkr@kaist.ac.kr |  |
| Minh Nguyen Duy | 석사과정 | 2026.8 |  | minh.nd@kaist.ac.kr |  |
| Yeri Kim | 석사과정 | 2026.8 |  | yeriyeri807@kaist.ac.kr |  |

## 졸업생과 이전 구성원

누리집 Alumni 페이지의 박사 26명(학위 표기 M.S./Ph.D. 2명 포함)과 석사 27명, Researchers 페이지 Previous Researchers 칸의 이전 연구원 9명(Postdoc. 6명, Postmast. 3명)이다.[^alumni][^researchers] 학위 연월과 진로는 누리집 표기이고, 이전 연구원 9명에는 연도가 적혀 있지 않다. 이전 연구원 가운데 Taeju Lee, Ji-Hoon Suh, Yoontae Jung은 박사 졸업생 행에도 있고, 진로가 「Postdoc. at KAIST」인 박사 졸업생들은 위 구성원 표에도 박사후연구원으로 있다.

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hyuntak Jeon | Ph.D. (2021.2) | Prof. at Chungbuk National University |
| Yeseul Jeon | Ph.D. (2021.2) | Qualcomm |
| Taeju Lee | Ph.D. (2021.2) | Postdoc. at Columbia University |
| Jaesuk Choi | Ph.D. (2022.2) | Analog Devices (France) |
| Hongseok Shin | Ph.D. (2022.2) | Samsung Electronics |
| Donghee Cho | Ph.D. (2022.2) | Samsung Electronics |
| Kyeongwon Jeong | Ph.D. (2023.2) | Prof. at Yonsei University |
| Unbong Lee | Ph.D. (2023.2) | Silicon Mitus |
| Woojin Ahn | Ph.D. (2023.8) | Director of TODOC |
| Injun Choi | Ph.D. (2023.8) | Samsung Electronics |
| Hung Phan Dang | Ph.D. (2023.8) | Samsung Electronics |
| Hyunwoo Park | Ph.D. (2024.2) | Postdoc. at KAIST |
| Chongsoo Jung | Ph.D. (2024.2) | CTO of AENTS |
| Ji-Hoon Suh | Ph.D. (2024.2) | Postdoc. at UC San Diego |
| Hoyong Seong | Ph.D. (2024.2) | SK Hynix |
| Yoontae Jung | Ph.D. (2024.2) | Prof. at Kyung Hee University |
| Hyungjoo Cho | Ph.D. (2024.8) | SK Hynix |
| Yechan Park | Ph.D. (2025.2) | Postdoc. at KAIST |
| Sein Oh | Ph.D. (2025.2) | Alphacore |
| Edward Jongyoon Choi | Ph.D. (2025.2) | Prof. at Ewha Womans University |
| Donghyeon Yi | M.S./Ph.D. (2025.8) | Postdoc. at KAIST |
| Yegeun Kim | M.S./Ph.D. (2025.8) | Samsung Electronics |
| Song-I Cheon | Ph.D. (2025.8) | Samsung Electronics |
| Donghyun Youn | Ph.D. (2026.2) | Samsung Electronics |
| Daehyeon Kwon | Ph.D. (2026.2) | Postdoc. at KAIST |
| Gichan Yun | Ph.D. (2026.2) | Postdoc. at KAIST |
| Jehoon Kim | M.S. (2018.8) | Samsung Electronics |
| CheolJun Park | M.S. (2019.2) | Prof. at Kyung Hee University |
| Miryeong Seol | M.S. (2020.2) | Samsung Electronics |
| Jeongeun Lee | M.S. (2020.2) | Samsung Electronics |
| Yilu Kim | M.S. (2020.2) | MEK-ICS |
| Jongmyeong Lee | M.S. (2021.2) | SK Hynix |
| Seong Wook Lee | M.S. (2021.2) | Samsung Electronics |
| Jinuk Kim | M.S. (2020.8) | Law School, Seoul National University |
| Sunghoon Choi | M.S. (2022.8) | Samsung Electronics |
| YoungBeom Kim | M.S. (2023.2) | LG Energy Solution |
| Seunga Park | M.S. (2023.8) | Samsung Electronics |
| Sunglim Han | M.S. (2024.2) | Ph.D. at UC San Diego |
| Chan Park | M.S. (2024.8) | Samsung Electronics |
| Wonseok Heo | M.S. (2024.8) | Samsung Electronics |
| Jiho Chun | M.S. (2025.2) | Ph.D. at Cornell University |
| Seonghyun Park | M.S. (2025.2) | Samsung Electronics |
| Jiho Myung | M.S. (2025.2) | SK Hynix |
| Seoyoung Lee | M.S. (2025.8) | IMEC |
| Thai Trinh Van | M.S. (2025.8) | Haechitech |
| Donghwan Kwon | M.S. (2026.2) | SK Hynix |
| Shinyu Park | M.S. (2026.2) | SK Hynix |
| Minseong Jang | M.S. (2026.2) | Samsung Electronics |
| Yoonsang Cho | M.S. (2026.2) | DB HiTek |
| Junyoung Kim | M.S. (2026.8) |  |
| Seonwoo Park | M.S. (2026.8) | SK Hynix |
| Radithya Arisaputra | M.S. (2026.8) | Samsung Electronics |
| Thi Hong Anh Nguyen | M.S. (2026.8) | Samsung Electronics |
| Soon-Jae Kweon | 이전 연구원 (Postdoc.) | Prof. at The Catholic University of Korea |
| Hongkyun Kim | 이전 연구원 (Postmast.) |  |
| Youngin Kim | 이전 연구원 (Postmast.) |  |
| Taeju Lee | 이전 연구원 (Postdoc.) |  |
| Seok-Tae Koh | 이전 연구원 (Postdoc.) |  |
| Seungho Jhung | 이전 연구원 (Postdoc.) |  |
| Ji-Hoon Suh | 이전 연구원 (Postdoc.) |  |
| Yoontae Jung | 이전 연구원 (Postdoc.) |  |
| Sunglim Han | 이전 연구원 (Postmast.) |  |

## 최근 논문 목록 (2021–2026)

누리집 International Journals·International Conferences·Books & Book Chapters 목록의 2021–2026년 구역 155편이다. 학술지 57편(arXiv 사전 공개 논문 1편 포함), 국제 학회 논문 97편, 책 속 장 1편이며, 연도마다 학술지 논문을 먼저 적었다. 저자 순서와 제목·학술지·학회 표기는 누리집 그대로이고, †는 누리집이 공동 기여 저자로 적은 표시다. 2026년 학술지 8편 가운데 5편은 Early Access(권·호가 정해지기 전 온라인으로 먼저 낸 논문)로, 2026년 학회 논문 16편 가운데 5편은 발표 예정(Accepted to be presented)으로 적혀 있어 정식 출판된 논문과 구분해 읽어야 한다. 교수가 마지막 저자가 아닌 공동연구 논문도 누리집 목록대로 실었다.[^journals][^confs][^books]

**2026**

- Jiho Chun, Byeongseon Choi, Edward Jongyoon Choi, Sohmyung Ha, Ik-Joon Chang, and Minkyu Je. "A Two-Step Time-Domain Logic-Compatible Embedded-Flash Computing-in-Memory Macro for On-Device AI". *IEEE Journal of Solid-State Circuits (JSSC), Early Access*.
- Edward Jongyoon Choi, Byeongseon Choi, Jiho Chun, Minkyu Je, and Bongjin Kim. "Verifica: Near-Memory Symbolic Interval Computing Formal Neural Network Verification Accelerator". *IEEE Journal of Solid-State Circuits (JSSC), Early Access*.
- Seonghyun Park, Song-I Cheon, Haidam Choi, Sein Oh, Sohmyung Ha, and Minkyu Je. "A Bio-impedance Readout IC with Phase-locked Sampling for Real-time Electrical Impedance Spectroscopy". *IEEE Journal of Solid-State Circuits (JSSC), Early Access*.
- Donghyun Youn†, Gichan Yun†, Yoontae Jung, Hoyong Seong, Sohmyung Ha and Minkyu Je. "Capacitance-to-Digital Converters: Recent Advances and Evolving Trends from Circuit-Level Performances to System Requirements". *IEEE Open Journal of the Solid-State Circuits Society (OJ-SSCS), Early Access*.
- Daehyeon Kwon, Donghyun Youn, Sohmyung Ha, and Minkyu Je. "A Multi-band Low-supply-voltage 16-QAM Transmitter Based on a Digital Fractional-N PLL with TDC Calibration for Capsule Endoscopy". *IEEE Transactions on Biomedical Circuits and Systems (TBCAS), Early Access*.
- Christopher Santos†, Dong-Hwi Choi†, Sohmyung Ha, and Minkyu Je. "A Neural Recording IC for 64-Channel Time-Multiplexed MEA with 3.3-GΩ Total Input Impedance Using Dual Positive Feedback Loop ZIN-Boosting". *IEEE Transactions on Biomedical Circuits and Systems (TBCAS), Apr. 2026*.
- Vincent Lukito†, Edward Jongyoon Choi†, Ik-Joon Chang, Sohmyung Ha, and Minkyu Je. "A Spike Sorting SoC With Δ-Based Spike Detection and End-to-End Implementation of Autoencoder Feature Extraction Using Analog CIM". *IEEE Journal of Solid-State Circuits (JSSC), Apr. 2026*.
- Song-I Cheon†, Dongyoon Lee†, Hyungjoo Cho, Seonghyun Park, Sohmyung Ha, and Minkyu Je. "Human Limb ExG Monitoring System Using Four-Node Body Channel Communication With Adaptive Gain Control". *IEEE Journal of Solid-State Circuits (JSSC), Mar. 2026*.
- Changhun Seok, Soon-Jae Kweon, Sohmyung Ha, and Minkyu Je. "Heartbeat-Locked Edge Processing for Low-SNR Ear-ECG Heart-Rate Estimation". *in Proc. IEEE Biomedical Circuits and Systems Conference (BioCAS), Oct. 2026*.
- Jungwoo Oh†, Hyunyeop Lee†, Sohmyung Ha, and Minkyu Je. "A Demodulation-Free Relay IR-UWB Transmitter for Fully Untethered Neural Implants". *in Proc. IEEE Biomedical Circuits and Systems Conference (BioCAS), Oct. 2026*.
- Joowon Kim, Jimin Koo, Christopher Santos, Sohmyung Ha, Soon-Jae Kweon, and Minkyu Je, "A Common-Mode-Interference-Tolerant 2.84-Nef Closed-Loop Series-Parallel Floating-Inverter Amplifier for Biopotential Recording, in Proc. IEEE Biomedical Circuits and Systems Conference (BioCAS), Oct. 2026.
- Hong-Anh Nguyen Thi, Kim Hoang Nguyen, Thanh-Tung Vu, Sohmyung Ha, and Minkyu Je. "A Four-Output Regulated Rectifier for Wireless Neural Stimulation with Simultaneous Per-Channel Dynamic Voltage Scaling in 0.18-μm CMOS". *in Proc. IEEE Biomedical Circuits and Systems Conference (BioCAS), Oct. 2026*.
- Radithya Arisaputra, Jongho Kim, Vincent Lukito, Sohmyung Ha, Ik Joon Chang, and Minkyu Je. "Multibit Time-Domain Compute-in-Memory Utilizing Multiline RC Delay and Digital Counter TDC". *in Proc. IEEE Biomedical Circuits and Systems Conference (BioCAS), Oct. 2026*.
- Byeongseon Choi, Edward Jongyoon Choi, Jiho Chun, Shin-Uk Kang, Dongyoon Kim, Bongjin Kim, and Minkyu Je. "SYMBA: A Symbolic Interval Accelerator for Adversarial Example Generation in Online Adversarial Fine-Tuning for Robust Edge AI". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), Accepted to be presented in Nov. 2026*.
- Heewon Choee, Yegeun Kim, Sein Oh, Sohmyung Ha, and Minkyu Je. "A 12.7-ENOB 2.97-GΩ-Input-Impedance NS-SAR-nested Third-Order DT-DSM with Active SNC for Biopotential Recording". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), Accepted to be presented in Nov. 2026*.
- Phan Dang Hung†, Trinh Van Thai†, Yechan Park, Jiho Lee, Daeguen Lim, Nguyen Quynh Trang, Sohmyung Ha, Chul Kim, and Minkyu Je. "A Buck-Conversion-Embedded Pile-Up Resonance Piezoelectric Energy Harvester with 32.2× Periodic- and 15.7× Shock-Power-Extraction Improvement". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), Accepted to be presented in Nov. 2026*.
- Donghyeon Yi, Donghwan Kwon, Yoontae Jung, Ik-Joon Chang, and Minkyu Je. "IMC-Diff: An Activation-Centric IMC Architecture for True Integer-Only Diffusion Inference". *in Proc. ACM/IEEE International Conference on Computer-Aided Design (ICCAD), Nov. 2026*.
- Hoyong Seong, Donghyun Youn, Sohmyung Ha, and Minkyu Je. "A 0.77mK-Resolution 78fJ·K²-FoM Resistor-Based Temperature Sensor Utilizing a Multi-Phase Slope-Boost Frequency-Locked Loop". *in Proc. IEEE European Solid-State Electronics Research Conference (ESSERC), Accepted to be presented in Sep. 2026*.
- Joowon Kim, Jimin Koo, Christopher Santos, Haidam Choi, Yegeun Kim, Chang-Hoon Seok, Yoontae Jung, Sohmyung Ha, Soon-Jae Kweon, and Minkyu Je. "A 1.64-Nef Discrete-Time Closed-Loop Series-Parallel Amplifier for Biopotential Recording with 139-VPP Common-Mode Interference Tolerance". *in Proc. IEEE European Solid-State Electronics Research Conference (ESSERC), Accepted to be presented in Sep. 2026*.
- Kim-Hoang Nguyen, Quang Nguyen, Duy-Minh Nguyen, Soon-Jae Kweon, Loan Pham-Nguyen, Hanh-Phuc Le, and Minkyu Je. "Design of a Wireless Power and Data Transfer System with Multi-Output Adaptive Rectifier and Harmonic Communication for Cochlear Implants". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May. 2026*.
- Quynh-Trang Nguyen, Duy-Minh Nguyen, Kim-Hoang Nguyen, Xuan-Khanh Nguyen, Dang Duy Tung, Loan Pham-Nguyen, and Minkyu Je. "A Flexible 128-Channel Neural Stimulator with Dynamic Voltage Scaling and Synchronous Charge Balancing for Visual Cortical Prosthesis". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May. 2026*.
- Quynh-Trang Nguyen†, Kim-Hoang Nguyen†, Duy-Minh Nguyen, Xuan-Khanh Nguyen, Loan-Pham Nguyen, and Minkyu Je. "A Pulse-Width-Modulated Temporal Interference Stimulator IC with Local and Global Charge Balancing for Selective Peripheral Nerve Stimulation". *in Proc. IEEE Custom Integrated Circuits Conference (CICC), Apr. 2026*.
- Hyunah Park, Taein Shin, Haeseok Suh, Donghyeon Yi, Minkyu Je, and Joungho Kim. "Beyond Off-chip Bandwidth Limits: PI-aware Extended Scale Cache (ESC) Stacked-GPU-HBM Module for Transformer-scale AI Computing". *in Proc. DesignCon, Feb. 2026*.
- Haidam Choi†, Gichan Yun†, Ji-Hoon Suh, Seonwoo Park, Donghyeon Yi, Sohmyung Ha, and Minkyu Je. "A 43.8-to-662.0μW 27.5-to-878.9fps Frame-Rate-Scalable Duty-Cycled Electrical Impedance Tomography System with MIMO Current-Balancing IA". *in Proc. IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2026*.

**2025**

- Donghyun Youn, Daehyeon Kwon, and Minkyu Je. "A 75-pJ/bit 435-MHz 16-QAM Modulator With 20-ns Startup Time and Symbol-Level Duty Cycling for Capsule Endoscopy". *IEEE Open Journal of the Solid-State Circuits Society (OJ-SSCS), Dec. 2025*.
- Dong-Hwi Choi†, Dongyoon Lee†, Yunchul Chung, Hyunyeop Lee, Kim-Hoang Nguyen, Byeongseon Choi, Gichan Yun, Sohmyung Ha, and Minkyu Je. "An Implantable Peripheral Nerve Interface System With Simultaneous Multi-Site Data Transmission via Galvanically Coupled Body-Channel Communication for Next-Generation Prosthetic Limbs". *IEEE Open Journal of the Solid-State Circuits Society (OJ-SSCS), Dec. 2025*.
- Yechan Park, Phan Dang Hung, Donghyun Youn, Daehyeon Kwon, Chul Kim, Minkyu Je. "A Wireless Power and Data Transfer System for Medical Implants Using a Miniaturized Inductive Link With Frequency-Splitting Enhancement". *IEEE Journal of Solid-State Circuits (JSSC), Nov. 2025*.
- Gichan Yun†, Sein Oh†, Heewon Choee, Haidam Choi, Sohmyung Ha and Minkyu Je. "A 2.0-mW 70.1-dB SNDR 7.8-MHz BW Continuous-Time Noise-Shaping SAR ADC Using Fully Parallelized Quantization". *IEEE Transactions on Circuits and Systems II: Express Briefs (TCAS-Ⅱ), Nov. 2025*.
- Woojin Ahn, Kim-Hoang Nguyen, Hoseung Lee, Kyou Sik Min, Sohmyung Ha, and Minkyu Je. "An Energy-Efficient Stimulation System Based on Adaptive Dynamic Voltage Switching Control for Cochlear Implants". *IEEE Transactions on Biomedical Circuits and Systems (TBCAS), Aug. 2025*.
- Sunglim Han, Hoyong Seong, Sein Oh, Jimin Koo, Hanbit Jin, Hye Jin Kim, Sohmyung Ha, and Minkyu Je. "A Time-domain Multi-channel Resistive-sensor Interface IC with High Energy Efficiency and Wide Input Range". *IEEE Transactions on Biomedical Circuits and Systems (TBCAS), Apr. 2025*.
- Yegeun Kim†, Changhun Seok†, Yoontae Jung, Soon-Jae Kweon, Sohmyung Ha, and Minkyu Je. "A Motion-Artifact-Tolerant Biopotential-Recording IC with a Digital-Assisted Loop". *IEEE Transactions on Biomedical Circuits and Systems (TBCAS), Apr. 2025*.
- Edward Jongyoon Choi, Chaeyun Shim, Byeongseon Choi, Jiho Chun, Minkyu Je, and Bongjin Kim. "Verifica: a 65nm In-Memory Symbolic Interval Computing Accelerator for a Formal Neural Network Verification". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), Nov. 2025*.
- Seonghyun Park, Song-I Cheon, Haidam Choi, Sein Oh, Sohmyung Ha, and Minkyu Je. "A High-accuracy and High-throughput Bio-impedance Measurement IC with Phase-locked Sampling for Realtime Electrical Impedance Spectroscopy". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), Nov. 2025*.
- Heewon Choee†, Sein Oh†, Yegeun Kim, Changhun Seok, Sohmyung Ha, and Minkyu Je. "A Total-CMRR-Boosting Technique Using Common-Mode Signal Replication for Biopotential Recording". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), Nov. 2025*.
- Seyeong Kim†, Hoyoung Gong†, Haidam Choi, Dong-Hwi Choi, Song-I Cheon, and Minkyu Je. "A Two-electrode Bio-impedance Readout IC with Current Mismatch Cancellation and 60-Hz CMI Rejection Loop". *in Proc. IEEE Biomedical Circuits and Systems Conference (BioCAS), Oct. 2025*.
- Hyunyeop Lee†, Dongyoon Lee†, Yunchul Chung, Sohmyung Ha, and Minkyu Je. "A 100-Mb/s Current-to-Current Galvanic-Coupling-Communication TX/RX Achieving 0.94-pJ/b TX Energy Efficiency for Neural Implant Systems". *in Proc. IEEE European Solid-State Electronics Research Conference (ESSERC), Sep. 2025*.
- Vincent Lukito, Edward Jongyoon Choi, Seoyoung Lee, Jimin Koo, Ik-Joon Chang, Sohmyung Ha, and Minkyu Je. "A No-Patient-Data Seizure Classifier SoC for Real-Time Classification of Seven Seizure Types Using Feature Fusion and Near-Memory Computing". *in Proc. IEEE Symposium on VLSI Technology and Circuits (SOVC), Jun. 2025*.
- Woongro Youn, Donghyun Youn, Hoyong Seong, Sohmyung Ha, and Minkyu Je. "A Temperature-Insensitive PM Capacitance-to-Digital Converter with DLL-Based Comparator Delay Compensation Achieving 53.5ppm/°C Without Calibration". *in Proc. IEEE Symposium on VLSI Technology and Circuits (SOVC), Jun. 2025*.
- Dongyoon Lee†, Song-I Cheon†, Dong-Hwi Choi†, Yoonsang Cho, Seonghyun Park, Christopher Santos, Hyungjoo Cho, Sohmyung Ha, and Minkyu Je. "A 16-QAM-based Multi-node BCC System with Bias-Electrode-Free Multi-channel ExG Readout ICs". *in Proc. IEEE Symposium on VLSI Technology and Circuits (SOVC), Jun. 2025*.
- Christopher Santos†, Dong-Hwi Choi†, Sohmyung Ha, and Minkyu Je. "A 64-channel Time-multiplexed Neural Recording IC with Dual Positive Feedback Loop ZIN-Boosting". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May. 2025*.
- Yunchul Chung†, Hyunyeop Lee†, Dongyoon Lee, Sohmyung Ha, and Minkyu Je. "Implantable Galvanic-Coupled Body Channel Communication Transceiver with Serpentine Electrodes for Joint Replacement". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May. 2025*.
- Heewon Choee, Yegeun Kim, Sein Oh, Sohmyung Ha, and Minkyu Je. "A Low-Noise Dynamic Comparator with Charge-Pump Pre-Amplifier". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May. 2025*.
- Jiho Myung, Gichan Yun, Heewon Choee, Yegeun Kim, Sohmyung Ha, and Minkyu Je. "A 99.8-nV/√Hz ∆Σ Modulator with an Input-Impedance-Boosted kT/C-Noise-Cancellation Integrator for Biopotential-Signal Acquisition". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May. 2025*.
- Thai Trinh Van, Hung Phan Dang, Yunchul Chung, Kim Hoang Nguyen, Sohmyung Ha, and Minkyu Je. "A Self-Powered Pressure Sensor System Based on Triboelectric Energy Harvesting for Knee Implants". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May. 2025*.
- Seoyoung Lee, Donghyeon Yi, Edward Jongyoon Choi, Vincent Lukito, Jongho Kim, Ryan G. L. Koh, Ik-Joon Chang, Sohmyung Ha, and Minkyu Je. "A 94.76 %-accuracy, < 16μs/classification-Latency STT-MRAM CiM-Based Classifier for Closed-Loop Peripheral Nerve Modulation Implants". *in Proc. IEEE International Conference on Artificial Intelligence Circuits and Systems (AICAS), Apr. 2025*.
- Jimin Koo, Sein Oh, Yoontae Jung, Vincent Lukito, Sohmyung Ha, and Minkyu Je. "A 6μW ECG-Recording ΔΣ Modulator with Internal-Capacitor-Flipping Technique for 34Vpp Common-Mode-Interference (CMI) Tolerance and 1Vpp Input Range". *in Proc. IEEE Custom Integrated Circuits Conference (CICC), Apr. 2025*.
- Gichan Yun, Haidam Choi, Yoontae Jung, Jiho Myung, Sein Oh, Sohmyung Ha, and Minkyu Je. "A 189.3 dB-FOMS 14.5fJ/Conversion-Step Continuous-Time Noise-Shaping SAR Capacitance-to-Digital Converter". *in Proc. IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2025*.
- Donghyun Youn, Kyeongwon Jeong, Woongro Youn, Hoyong Seong, Yechan Park, Sohmyung Ha, and Minkyu Je. "An 18.5 nF-Input-Range PM-SAR Hybrid Capacitance-to-Digital Converter Achieving 6.1 μs Conversion Time at 18.1 pF Input Capacitance". *in Proc. IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2025*.
- Yechan Park, Phan Dang Hung, Donghyun Youn, Daehyeon Kwon, Chul Kim, and Minkyu Je. "An Enhanced-Frequency-Splitting-Based Wireless Power and Data Transfer System Achieving 60.2 % End-to-End Efficiency and 1Mb/s Data Rate with a Sub-cm RX Coil for Miniaturized Implants". *in Proc. IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2025*.
- Yechan Park, Chul Kim, and Minkyu Je. "A Wireless Adiabatic Stimulator System with Current-Mode Power Reception and Stimulus Current Regulation Achieving Precise Charge Delivery and Electrode Scalability for Miniaturized Electroceuticals". *in Proc. IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2025*.

**2024**

- Haidam Choi†, Song-I Cheon†, Gichan Yun, Sein Oh, Ji-Hoon Suh, Sohmyung Ha, and Minkyu Je. "A Bio-Impedance Readout IC With Complex-Domain Noise-Correlated Baseline Cancellation". *IEEE Journal of Solid-State Circuits (JSSC), Nov. 2024*.
- Kim-Hoang Nguyen, Quyet Nguyen, Quynh-Trang Nguyen, Thanh-Tung Vu, Woojin Ahn, Loan Pham-Nguyen, Hanh-Phuc Le, and Minkyu Je. "A Fully Integrated Dynamic-Voltage-Scaling Stimulator IC for Cochlear Implants". *IEEE Solid-State Circuits Letters (SSCL), Sep. 2024*.
- Sein Oh and Minkyu Je. "Process-Scalable and Low-Power Amplifiers: Progress and Prospects in Dynamic Amplifier Research". *IEEE Solid-State Circuits Magazine (SSCM), Summer 2024*.
- Hyeonseok Han, Hyunwoo Park, Seokjoo Cho, Sung-Uk Lee, Jungrak Choi, Ji-Hwan Ha, Jaeho Park, Young Jung, Hyunjin Kim, Junseong Ahn, Yeong Jae Kwon, Yong Suk Oh, Minkyu Je, and Inkyu Park. "Battery-Free, Wireless Multi-Modal Sensor, and Actuator Array System for Pressure Injury Prevention". *Small, Aug. 2024*.
- Donghyun Youn†, Youngin Kim†, Injun Choi, Yoontae Jung, Hyuntak Jeon, Kyungtae Lee, Soon-Jae Kweon, Sohmyung Ha, and Minkyu Je. "A Wide-Dynamic-Range, DC-Coupled, Time-Based Neural-Recording IC with Optimized CCO Frequency". *IEEE Access, Jul. 2024*.
- Donghyeon Yi, Seoyoung Lee, Injun Choi, Gichan Yun, Edward Jongyoon Choi, Jonghee Park, Jonghoon Kwak, Sung-Joon Jang, Sohmyung Ha, Ik-Joon Chang, and Minkyu Je. "Skew-CIM: Process-Variation-Resilient and Energy-Efficient Computation-in-Memory Design Technique With Skewed Weights". *IEEE Transactions on Circuits and Systems I: Regular papers (TCAS-I), May 2024*.
- Yoontae Jung†, Sein Oh†, Sohmyung Ha, and Minkyu Je. "A 187-dB FoMS Power-Efficient Second-Order Highpass ΔΣ Capacitance-to-Digital Converter". *IEEE Journal of Solid-State Circuits (JSSC), Apr. 2024*.
- Gichan Yun, Kyeongwon Jeong, Haidam Choi, Seunghyun Nam, Chaerin Oh, Hyunjoo Jenny Lee, Sohmyung Ha, and Minkyu Je. "An Ultrasound Receiver with Bandwidth-enhanced Current Conveyor and Element-level Ultrasound Transmitter for Ultrasound Imaging Systems". *IEEE Solid-State Circuits Letters (SSCL), Feb. 2024*.
- Song-I Cheon†, Haidam Choi†, Hyoju Kang, Ji-Hoon Suh, Seonghyun Park, Soon-Jae Kweon, Minkyu Je, and Sohmyung Ha. "Impedance-Readout Integrated Circuits for Electrical Impedance Spectroscopy: Methodological Review". *IEEE Transactions on Biomedical Circuits and Systems (TBCAS), Feb. 2024*.
- Kyeongwon Jeong, Sohmyung Ha, and Minkyu Je. "A 15.4-ENOB, Fourth-Order Truncation-Error-Shaping NS-SAR-Nested ΔΣ Modulator With Boosted Input Impedance and Range for Biosignal Acquisition". *IEEE Journal of Solid-State Circuits (JSSC), Feb. 2024*.
- Jiho Chun, Edward Jongyoon Choi, Byeongseon Choi, Donghyeon Yi, Sohmyung Ha, Ik-Joon Chang, and Minkyu Je. "A 639.38 GOPS Hybrid-Domain Logic-Compatible Multi-Level Embedded Flash Computing-in-Memory Macro with Spike-Edge Computation". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), Nov. 2024*.
- Dongyoon Lee†, Song-I Cheon†, Hyungjoo Cho, Seonghyun Park, Jiho Chun, Haidam Choi, Gichan Yun, Yoonsang Cho, Sohmyung Ha, and Minkyu Je. "A Multi-Node Body-Channel-Communication System Using Adaptive Gain Control with ExG Readout ICs for Moving VR Users". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), Nov. 2024*.
- Jimin Koo†, Haidam Choi†, Yoontae Jung†, Ji-Hoon Suh, Sein Oh, Changhun Seok, Yegeun Kim, Injun Choi, Heewon Choee, Sunglim Han, Jiho Chun, Hoyong Seong, Sohmyung Ha, and Minkyu Je. "A 1.27-mW Battery-Powered Multimodal Biosensor Interface IC for Wireless Motion Intention Recognition in Wearable Robots". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), Nov. 2024*.
- Sein Oh†, Gichan Yun†, Heewon Choee, Yoontae Jung, Jimin Koo, Sohmyung Ha, and Minkyu Je. "A 1.3 mW 10 MHz-BW 71 dB-SNDR Two-Step TDC-Assisted Continuous-Time Noise-Shaping SAR ADC". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), Nov. 2024*.
- Byeongseon Choi, Edward Jongyoon Choi, Donghyeon Yi, Jiho Chun, Sohmyung Ha, Ik-Joon Chang, and Minkyu Je. "AR-CIM: a 460.22TOPS/W SRAM-Based Analog Reconfigurable Computing-in-Memory Macro with 1/2/4/8-Bit Variable Precision". *in Proc. IEEE European Solid-State Electronics Research Conference (ESSERC), Sep. 2024*.
- Yegeun Kim, Changhun Seok, Kyeongwon Jeong, Haidam Choi, Heewon Choee, Sohmyung Ha, and Minkyu Je. "A 5.3-μW 80.8-dB SNDR LNA-Embedded EF-CIFF Third-Order Noise-Shaping SAR ADC for Closed-Loop Neural Recording". *in Proc. IEEE European Solid-State Electronics Research Conference (ESSERC), Sep. 2024*.
- Chan Park, Sohmyung Ha, and Minkyu Je. "A High-Efficiency High-Data-Rate Wireless Power and Data Transfer IC Using Orthogonal Codes for Miniaturized Multi-Channel Neural Interface Systems". *in Proc. International SoC Design Conference (ISOCC), Aug. 2024*.
- Wonseok Heo, Hoyong Seong, Donghyun Youn, Sohmyung Ha, and Minkyu Je. "An Energy Efficient Period-modulation-based Current-to-digital Converter for FET-type Sensors". *in Proc. International SoC Design Conference (ISOCC), Aug. 2024*.
- Edward Jongyoon Choi†, Jiho Chun†, Byeongseon Choi, Sohmyung Ha, Ik-Joon Chang, and Minkyu Je. "An SRAM-based Error-Free Time Domain Pulse Train Computing-In-Memory Macro achieving 226.14 TOPS/W and 5.782 TOPS/mm²". *in Proc. International SoC Design Conference (ISOCC), Aug. 2024*.
- Haidam Choi, Gichan Yun, Ji-Hoon Suh, Sein Oh, Song-I Cheon, Yoontae Jung, Sohmyung Ha, and Minkyu Je. "A Fully Dynamic 1st-Order 1st-Order Δ-ΔΣ Modulator with a 468 mVpp Input Range for Electrical Impedance Tomography Systems". *in Proc. IEEE Symposium on VLSI Technology and Circuits (SOVC), Jun. 2024*.
- Edward Jongyoon Choi†, Vincent Lukito†, Injun Choi, Seoyoung Lee, Ik-Joon Chang, Sohmyung Ha, and Minkyu Je. "A Δ-Based Spike Sorting SoC with End-to-End Implementation of Event-Driven Binary Autoencoder Neural Network in Analog CIM Achieving 94.54 % Accuracy and 3.11 µW/ch". *in Proc. IEEE Symposium on VLSI Technology and Circuits (SOVC), Jun. 2024*.
- Hyungjoo Cho, Dongyoon Lee, Hoyong Seong, Heewon Choee, Ji-Hoon Suh, Injun Choi, Donghee Cho, Sohmyung Ha, and Minkyu Je. "An Intra-Body-Power-Transfer System Energized by an Electromagnetic Energy Harvester for Powering Wearable Sensor Nodes". *in Proc. IEEE Symposium on VLSI Technology and Circuits (SOVC), Jun. 2024*.
- Ji-Hoon Suh, Haidam Choi, Yoontae Jung, Sohmyung Ha, and Minkyu Je. "A 5.7 kfps Fast Neural Electrical Impedance Tomography IC Based on Incremental Zoom Structure with Baseline Cancellation for Peripheral Nerve Monitoring Systems". *in Proc. IEEE Symposium on VLSI Technology and Circuits (SOVC), Jun. 2024*.
- Aida Aberra, Muhammad Abrar Akram, Soon-Jae Kweon, Jongmin Kim, Kim-Hoang Nguyen, Gichan Yun, Yong-Ak Song, Minkyu Je, and Sohmyung Ha. "A Hybrid High-voltage Regulating Charge Pump for Electrokinetic Concentration". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May 2024*.
- Karam Ellahi, Soon-Jae Kweon, Asra Malik, Muhammad Abrar Akram, Song-I Cheon, Yoontae Jung, Minkyu Je, Hammad M. Cheema, and Sohmyung Ha. "A High-Throughput Impedance Measurement IC Using Synchronous Cyclic Integration Technique". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May 2024*.
- Asra Malik, Soon-Jae Kweon, Karam Ellahi, Muhammad Abrar Akram, Song-I Cheon, Yoontae Jung, Minkyu Je, Hammad M. Cheema, and Sohmyung Ha. "A High-Throughput Impedance Measurement IC with Baseline-Canceling Peak Detector". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May 2024*.
- Sohyeon Kim, Injun Choi, Minkyu Je, and Ji-Hoon Kim. "Dynamic Resource Management in Reconfigurable SoC for Multi-Tenancy Support". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May 2024*.
- Sunyoung Park, Wooseok Byun, Minkyu Je, and Ji-Hoon Kim. "Algorithm-Hardware Co-Design for Wearable BCIs: An Evolution from Linear Algebra to Transformers". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May 2024*.
- Sunglim Han, Hoyong Seong, Sein Oh, Jimin Koo, Hanbit Jin, Hye Jin Kim, Sohmyung Ha, and Minkyu Je. "A 72-Channel Resistive-Sensor Interface IC with High Energy Efficiency and a Wide Input Range". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May 2024*.
- Jimin Koo, Yoontae Jung, Sein Oh, Sunglim Han, Sohmyung Ha, and Minkyu Je. "A Reconfigurable Multimodal Sensor Interface IC Based on Direct-Conversion ΔΣ Modulator Structure". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May 2024*.
- Haidam Choi, Ji-Hoon Suh, Gichan Yun, Sein Oh, Sohmyung Ha, and Minkyu Je. "A Low-Power ∆-∆Σ-Based Bio-Impedance Readout IC with Capacitive-Feedback Baseline Cancellation". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May 2024*.
- Song-I Cheon, Seonghyun Park, Haidam Choi, Yebin Choi, Minho Seok, Young-Ho Cho, Sohmyung Ha, and Minkyu Je. "Ultrahigh-G Accelerometer Readout IC with Adaptive Gain Path for Shock Resilience". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May 2024*.
- Yegeun Kim, Changhun Seok, Yoontae Jung, Sohmyung Ha, and Minkyu Je. "A Biopotential Recording IC with <10-ms-Settling Hybrid DC Servo Loop". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May 2024*.
- Woobean Lee†, Yoontae Jung†, Hyuntak Jeon, Jimin Koo, Sein Oh, and Minkyu Je. "An Area-Efficient, DC-Coupled VCO-Based CT ∆ΣM with Input-TR-DAC for Neural Recording". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May 2024*.
- Kim-Hoang Nguyen, Quyet Nguyen, Quynh-Trang Nguyen, Thanh-Tung Vu, Woojin Ahn, Loan Pham-Nguyen, Hanh-Phuc Le, and Minkyu Je. "A Fully Integrated Dynamic-Voltage-Scaling Stimulator IC with Miniaturized Reconfigurable Supply Modulator and Channel Drivers for Cochlear Implants". *in Proc. IEEE Custom Integrated Circuits Conference (CICC), Apr. 2024*.
- Yebin Choi, Minho Seok, Song-I Cheon, Minkyu Je, Young-Ho Cho, Sehwan Song, Sang-Hee Yoon, Kilyug Kim, Won-Young Uhm, Junyong Jang, Yongjun Cho, and Myung-Suk Jung. "Robust High-G Microaccelerometers with Mechanical Low-Pass Filters and Electrical ROIC". *in Proc. IEEE International Symposium on Inertial Sensors and Systems (INERTIAL), Mar. 2024*.
- Song-I Cheon†, Haidam Choi†, Gichan Yun, Sein Oh, Ji-Hoon Suh, Sohmyung Ha, and Minkyu Je. "A Two-Electrode Bio-Impedance Readout IC with Complex-Domain Noise-Correlated Baseline Cancellation Supporting Sinusoidal Excitation". *in Proc. IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2024*.
- Haidam Choi†, Song-I Cheon†, Hyoju Kang, Ji-Hoon Suh, Seonghyun Park, Soon-Jae Kweon, Sohmyung Ha, and Minkyu Je. "Advancing Electrical Impedance Spectroscopy (EIS): Low-power, High-accuracy, Wide-dynamic-range, and High-throughput Impedance Measurement Circuits and Architectures". *in a book titled "Low-cost Diagnostics: Fabrication, Materials, and Applications", Royal Society of Chemistry (London, UK), Dec. 2024*.

**2023**

- Chongsoo Jung, Hoyong Seong, Injun Choi, Sohmyung Ha and Minkyu Je. "A Process-Scalable Ultra-Low-Voltage Sleep Timer With a Time-Domain Amplifier and a Switch-Less Resistance Multiplier". *IEEE Journal of Solid-State Circuits (JSSC), Oct. 2023*.
- Hyunwoo Park, Kyuyoung Kim, Soon-Jae Kweon, Osman Gul, Jungrak Choi, Yong Suk Oh, Inkyu Park, and Minkyu Je. "A Wireless and Wearable Body-Pressure-Monitoring System for the Prevention of Pressure-Induced Skin Injuries". *IEEE Transactions on Biomedical Circuits and Systems (TBCAS), Jun. 2023*.
- Kyeongwon Jeong, Gichan Yun, Jaesuk Choi, Injun Choi, Jeehoon Son, Jae Youn Hwang, Sohmyung Ha, and Minkyu Je. "A Wide-Bandwidth Ultrasound Receiver and On-Chip Ultrasound Transmitter for Ultrasound Capsule Endoscopy". *IEEE Journal of Solid-State Circuits (JSSC), Oct. 2023*.
- Taeju Lee, and Minkyu Je. "Trend Investigation of Biopotential Recording Front-End Channels for Invasive and Non-Invasive Applications". *arXiv:2305.13463, May 2023*.
- Hyungjoo Cho, Ji-Hoon Suh, Gichan Yun, Sohmyung Ha, and Minkyu Je. "An Intra-Body Power Transfer System with Continuous Maximum Resonant Power Tracking". *IEEE Solid-State Circuits Letters (SSCL), Apr. 2023*.
- Ji-Hoon Suh, Haidam Choi, Yoontae Jung, Sein Oh, Hyungjoo Cho, Nahmil Koo, Seong Joong Kim, Chisung Bae, Sohmyung Ha, and Minkyu Je. "A 16-channel Impedance-Readout IC with Synchronous Sampling and Baseline Cancellation for Fast Neural Electrical Impedance Tomography". *IEEE Solid-State Circuits Letters (SSCL), Apr. 2023*.
- Seokjoo Cho, Hyeonseok Han, Hyunwoo Park, Sung-Uk Lee, Jae-Hwan Kim, Sung Woo Jeon, Mengqiu Wang, Raudel Avila, Zhaoqian Xi, Kabseok Ko, Minsu Park, Jungyup Lee, Myungwoo Choi, Je-Sang Lee, Weon Gi Min, Byeong-Ju Lee, Soyeong Lee, Jungrak Choi, Jimin Gu, Jaeho Park, Min Seong Kim, Junseong Ahn, Osman Gul, Chankyu Han, Gihun Lee, Seunghwan Kim, Kyuyoung Kim, Jeonghyun Kim, Chang-Mo Kang, Jahyun Koo, Sung Soo Kwak, Sungbong Kim, Dong Yun Choi, Seokwoo Jeon, Hyung Jin Sung, Yong Bae Park, Minkyu Je, Young Tae Cho, Yong Suk Oh, Inkyu Park. "Wireless, multimodal sensors for continuous measurement of pressure, temperature, and hydration of patients in wheelchair". *nature partner journal (npj) Flexible Electronics, Feb. 2023*.
- Donghee Cho, Hyungjoo Cho, Sein Oh, Yoontae Jung, Sohmyung Ha, Chul Kim, and Minkyu Je. "A High-Efficiency Single-Mode Dual-Path Buck-Boost Converter With Reduced Inductor Current". *IEEE Journal of Solid-State Circuits (JSSC), Mar. 2023*.
- Gichan Yun, Kyeongwon Jeong, Haidam Choi, Seunghyeon Nam, Chaerin Oh, Hyunjoo Jenny Lee, Sohmyung Ha, and Minkyu Je. "A 2pA/√Hz Current-Conveyor-Assisted Ultrasound Receiver with 25pF CMUT Parasitic Capacitance". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), Nov. 2023*.
- Kim-Hoang Nguyen, Woojin Ahn, Minkyu Je, Quyet Nguyen, Quynh-Trang Nguyen, Thanh-Tung Vu, and Loan Pham-Nguyen. "A Neural Stimulator IC with Dynamic Voltage Scaling Supply and Energy Recycling for Cochlear Implant in Standard 180 nm CMOS Process". *in Proc. International SoC Design Conference (ISOCC), Oct. 2023*.
- Yoontae Jung† , Sein Oh† , Jimin Koo, Seunga Park, Ji-Hoon Suh, Donghee Cho, Sohmyung Ha, and Minkyu Je. "A 187dB FoMS 46fJ/Conv. 2nd-order Highpass Delta-Sigma Capacitance-to-Digital Converter". *in Proc. IEEE Symposium on VLSI Technology and Circuits (SOVC), Jun., 2023*.
- Sein Oh, Seunga Park, Yoontae Jung, Jimin Koo, Donghee Cho, Sohmyung Ha, and Minkyu Je. "A 2.5mW 12MHz-BW 69dB SNDR Passive Bandpass Delta-Sigma ADC with Highpass Noise-Shaping SAR Quantizers". *in Proc. IEEE Symposium on VLSI Technology and Circuits (SOVC), Jun. 2023*.
- Yoontae Jung, Soon-Jae Kweon, Hyuntak Jeon, Jeongeun Lee, Youngin Kim, Sein Oh, Jimin Koo, and Minkyu Je. "A Sub-aF Super-High-Resolution Capacitance-to-Digital Converter with a Bandpass ΔΣ ADC". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May 2023*.
- Woojin Ahn, Kim-Hoang Nguyen, Jungwoo Lim (TODOC), Kyou Sik Min(TODOC), Hoseung Lee(TODOC), Sohmyung Ha, and Minkyu Je. "An Energy-Efficient, Scalable Neural Stimulation IC with Adaptive Dynamic Voltage Switching for Cochlear Implant System". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May 2023*.
- Ji-Hoon Suh, Hyungjoo Cho, Yeseul Jeon, and Minkyu Je. "A Batteryless Electrochemical Sensing System IC Based on Intra-Body Power and Data Transfer Towards Miniaturized Wearable Sensor Nodes". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May 2023*.
- Edward Choi, Injun Choi, Vincent Lukito, Dong-Hwi Choi, Donghyeon Yi, Ik-Joon Chang, Sohmyung Ha, and Minkyu Je. "A 333 TOPS/W Logic-Compatible Multi-Level Embedded Flash Compute-In-Memory Macro with Dual-Slope Computation". *in Proc. IEEE Custom Integrated Circuits Conference (CICC), Apr. 2023*.
- Hoyong Seong, Donghyun Youn, Injun Choi, Junghyup Lee, Sohmyung Ha, and Minkyu Je. "A 0.9V 2MHz 6.4x-Slope-Boosted Quadrature-Phase Relaxation Oscillator with 164.2dBc/Hz FoM and 62.5ppm Period Jitter in 0.18μm CMOS". *in Proc. IEEE Custom Integrated Circuits Conference (CICC), Apr. 2023*.
- Yoontae Jung, Jimin Koo, Sein Oh, Seunga Park, Ji-Hoon Suh, Donghee Cho, and Minkyu Je. "A 56fJ/Conversion-Step 178dB-FoMS Third-Order Hybrid CT-DT ΔΣ Capacitance-to-Digital Converter". *in Proc. IEEE Custom Integrated Circuits Conference (CICC), Apr., 2023*.

**2022**

- Song-I Cheon, Soon-Jae Kweon, Aida Aberra, Minkyu Je, and Sohmyung Ha. "Optimal Parameter Design of DAC-based Sinusoidal Signal Generators for Electrical Impedance Spectroscopy". *IEEE Transaction on Instrumentation and Measurement (TIM), Dec. 2022*.
- Hyungjoo Cho, Ji-Hoon Suh, Chul Kim, Sohmyung Ha, and Minkyu Je. "An Intra-Body Power Transfer System With >1-mW Power Delivered to the Load and 3.3-V DC Output at 160-cm of on-Body Distance". *IEEE Transactions on Biomedical Circuits and Systems (TBCAS), Oct. 2022*.
- Edward Jongyoon Choi, Injun Choi, Chanhee Jeon, Gichan Yun, Donghyeon Yi, Sohmyung Ha, Ik-Joon Chang, and Minkyu Je. "SRAM-Based Computing-in-Memory Macro With Fully Parallel One-Step Multibit Computation". *IEEE Solid-State Circuits Letters (SSCL), Sep. 2022*.
- Wooseok Byun, Minkyu Je and Ji-Hoon Kim. "An Energy-Efficient Domain-Specific Reconfigurable Array Processor With Heterogeneous PEs for Wearable Brain–Computer Interface SoCs". *IEEE Transactions on Circuits and Systems I: Regular papers (TCAS-I), Aug. 2022*.
- Unbong Lee, Wanyeong Jung, Sohmyung Ha, Minkyu Je. "An Auto-reconfigurable Multi-output Regulating Switched-capacitor DC-DC Converter for Wireless Power Reception and Distribution in Multi-unit Implantable Devices". *IEEE Open Journal of the Solid-State Circuits Society (OJ-SSCS), Aug. 2022*.
- Yoontae Jung, Soon-Jae Kweon, Hyuntak Jeon, Injun Choi, Jimin Koo, Mi kyung Kim, Hyunjoo Jenny Lee, Sohmyung Ha, and Minkyu Je. "A Wide-Dynamic-Range Neural-Recording IC With Automatic-Gain-Controlled AFE and CT Dynamic-Zoom ΔΣ ADC for Saturation-Free Closed-Loop Neural Interfaces". *IEEE Journal of Solid-State Circuits (JSSC), Jul. 2022*.
- Kyeongwon Jeong, Yoontae Jung, Gichan Yun, Donghyun Youn, Yehhyun Jo, Hyunjoo Jenny Lee, Sohmyung Ha and Minkyu Je. "A PVT-Robust AFE-Embedded Error-Feedback Noise-Shaping SAR ADC with Chopper-Based Passive High-Pass IIR Filtering for Direct Neural Recording". *IEEE Transactions on Biomedical Circuits and Systems (TBCAS), Jul. 2022*.
- Woojin Ahn, Doohee Kim, Jonghyeok Park, Joeng Hoan Park, Taeju Lee, Kyeongwon Jeong, Kyou Sik Min, Hoseung Lee and Minkyu Je. "A Reconfigurable Neural Stimulation IC with a High-Resolution Strength Control and In-Situ Neural Recording Function for Cochlear Implant Systems". *IEEE Solid-State Circuits Letters (SSCL), May 2022*.
- Wooseok Byun, Minkyu Je and Ji-Hoon Kim. "Advances in Wearable Brain-Computer Interfaces from an Algorithm-Hardware Co-Design Perspective". *IEEE Transactions on Circuits and Systems II: Express Briefs (TCAS-II), Jul. 2022*.
- Yoontae Jung, Soon-Jae Kweon, Taeju Lee, Kyeongwon Jeong, Sohmyung Ha and Minkyu Je. "Dynamic-Range-Enhancement Techniques for Artifact-Tolerant Biopotential-Acquisition ICs". *IEEE Transactions on Circuits and Systems II: Express Briefs (TCAS-II), May 2022*.
- Soon-Jae Kweon, Ayesha Kajol Rafi, Song-I Cheon, Minkyu Je and Sohmyung Ha. "On-chip Sinusoidal Signal Generators for Electrical Impedance Spectroscopy: Methodological Review". *IEEE Transactions on Biomedical Circuits and Systems (TBCAS), Apr. 2022*.
- Injun Choi, Edward Jongyoon Choi, Donghyeon Yi, Yoontae Jung, Hoyong Seong, Hyuntak Jeon, Soon-Jae Kweon, Ik-Joon Chang, Sohmyung Ha and Minkyu Je. "An SRAM-Based Hybrid Computation-in-Memory Macro Using Current-Reused Differential CCO". *IEEE Journal on Emerging and Selected Topics in Circuits and Systems (JETCAS), Apr. 2022*.
- Song-I Cheon, Soon-Jae Kweon, Youngin Kim, Jimin Koo, Sohmyung Ha and Minkyu Je. "An Impedance Readout IC with Ratio-Based Measurement Techniques for Electrical Impedance Spectroscopy". *Sensors, Feb. 2022*.
- Taeju Lee, Mi Kyung Kim, Hyunjoo Jenny Lee and Minkyu Je. "A multimodal neural-recording IC with reconfigurable analog front-ends for improved availability and usability for recording channels". *IEEE Transactions on Biomedical Circuits and Systems (TBCAS), Jan. 2022*.
- Kyeongwon Jeong, Jaesuk Choi, Gichan Yun, Injun Choi, Jeehoon Son, Jae Youn Hwang, Sohmyung Ha, and Minkyu Je. "20-MHz 2.3-mW Receiver and a 25-V Transmitter for Ultrasound Capsule Endoscopy". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), Nov. 2022*.
- Ji-Hoon Suh, Haidam Choi, Yoontae Jung, Sein Oh, Hyungjoo Cho, Nahmil Koo, Seong Joong Kim, Chisung Bae, Sohmyung Ha, and Minkyu Je. "A Synchronous-Sampling Impedance-Readout IC with Baseline-Cancellation-Based Two-Step Conversion for Fast Neural Electrical Impedance Tomography". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), Nov. 2022*.
- Hyungjoo Cho, Ji-Hoon Suh, Gichan Yun, Sohmyung Ha, and Minkyu Je. "An Intra-Body-Power-Transfer System with a PLL-based Continuous Maximum Resonant Power Tracking Loop at TX and 1.8V DC Output Voltage at RX". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), Nov. 2022*.
- Hoyong Seong, Chongsoo Jung, Donghyun Youn, Junghyup Lee, Sohmyung Ha, and Minkyu Je. "A 118.6fJ/Conversion-Step Two-Step Time-Domain RC-to-Digital Converter With 33nF/10MΩ Range and 53aFrms Resolution". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), Nov. 2022*.
- Chongsoo Jung, Hoyong Seong, Injun Choi, Sohmyung Ha, and Minkyu Je. "A Process-Scalable Ultra-Low-Voltage 180kHz Sleep Timer with a Time-Domain Amplifier and a Switch-less Resistance Multiplier". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), Nov. 2022*.
- Phan Dang Hung, Hongseok Shin, Yechan Park, Nguyen Kim Hoang, Donghee Cho, Sohmyung Ha, Chul Kim and Minkyu Je. "A 96.5%-Power-Efficiency Hybrid Buck-Boost Photovoltaic Energy Harvester Employing Adaptive FOCV MPPT Control for> 98% MPPT Efficiency Across a 10,000× Dynamic Range". *in Proc. IEEE Symposium on VLSI Technology and Circuits (SOVC). July. 2022*.
- Kyeongwon Jeong, Gichan Yun, Sohmyung Ha and Minkyu Je. "A 600mV PP-Input-Range 94.5 dB-SNDR NS-SAR-Nested DSM with 4 th-Order Truncation-Error Shaping and Input-Impedance Boosting for Biosignal Acquisition". *in Proc. IEEE Symposium on VLSI Technology and Circuits (SOVC). July. 2022*.
- Edward Choi, Injun Choi, Chanhee Jeon, Gichan Yun, Donghyeon Yi, Sohmyung Ha, Ik-Joon Chang and Minkyu Je. "A 133.6 TOPS/W Compute-In-Memory SRAM Macro with Fully Parallel One-Step Multi-Bit Computation". *in Proc. IEEE Custom Integrated Circuits Conference (CICC). April. 2022*.
- Donghee Cho, Hyungjoo Cho, Sein Oh, Yoontae Jung, Sohmyung Ha, Chul Kim and Minkyu Je. "A Single-Mode Dual-Path Buck-Boost Converter with Reduced Inductor Current Across All Duty Cases Achieving 95.58% Efficiency at 1A in Boost Operation". *in Proc. IEEE Custom Integrated Circuits Conference (CICC). April. 2022*.
- Sehwan Lee, Yoonsung Choi, Geunha Kim, Seungyeob Baik, Taeryoung Seol, Homin Jang, Doyoung Lee, Minkyu Je, Ji-Woong Choi, Arup K George and Junghyup Lee. "A 0.7 V 17fJ/Step-FOM W 178.1 dB-FOM SNDR 10kHz-BW 560mV PP True-ExG Biopotential Acquisition System with Parasitic-Insensitive 421MΩ Input Impedance in 0.18 μm CMOS". *in Proc. IEEE International Solid-State Circuits Conference (ISSCC). Feb. 2022*.

**2021**

- Arup K George, Wooyoon Shim, Jaeha Kung, Ji-Hoon Kim, Minkyu Je and Junghyup Lee. "A 46-nF/10-MΩ Range 114-aF/0.37-Ω Resolution Parasitic-and Temperature-Insensitive Reconfigurable RC-to-Digital Converter in 0.18-μm CMOS". *IEEE Transactions on Circuits and Systems I: Regular Papers (TCAS-I), Dec. 2021*.
- Yechan Park, Seok-Tae Koh, Jeongeun Lee, Hongkyun Kim, Jaesuk Choi, Sohmyung Ha, Chul Kim and Minkyu Je. "A Wireless Power and Data Transfer IC for Neural Prostheses Using a Single Inductive Link With Frequency-Splitting Characteristic". *IEEE Transactions on Biomedical Circuits and Systems (TBCAS), Dec. 2021*.
- Song-I Cheon, Soon-Jae Kweon, Youngin Kim, Jimin Koo, Sohmyung Ha and Minkyu Je. "A Polar-demodulation-based Impedance-measurement IC Using Frequency-shift Technique with Low Power Consumption and Wide Frequency Range". *IEEE Transactions on Biomedical Circuits and Systems (TBCAS), Dec. 2021*.
- Soon-Jae Kweon, Woojin Yun, Hyunwoo Park, Jeong-Ho Park, Jung Hoon Lee, Jin Lee, Minkyu Je, Sohmyung Ha and Choul-Young Kim. "A Precise Lesion Localization System Using a Magnetometer With Real-Time Baseline Cancellation for Laparoscopic Surgery". *IEEE Access, Sep. 2021*.
- Xu Liu, Juzhe Li, Tao Chen, Wensi Wang and Minkyu Je. "A Neural Recording and Stimulation Chip with Artifact Suppression for Biomedical Devices". *Journal of Healthcare Engineering, Aug. 2021*.
- Taeju Lee, Jee-Ho Park, Namsun Chou, Seong-Jin Kim and Minkyu Je. "A multimodal neural activity readout integrated circuit for recording fluorescence and electrical signals". *IEEE Access, Aug. 2021*.
- Kyungsoo Kim, Seung-Jun Yoo, So Yeon Kim, Taeju Lee, Sung-Ho Lim, Jae-Eun Jang, Minkyu Je, Cheil Moon and Ji-Woong Choi. "Subthreshold electrical stimulation as a low power electrical treatment for stroke rehabilitation". *Scientific Reports, Jul. 2021*.
- Moojune Song, Min Gyu Park, San Ko, Sung Kyu Jang, Minkyu Je and Kab-Jin Kim. "Logic Device Based on Skyrmion Annihilation". *IEEE Transactions on Electron Devices (T-ED), Apr. 2021*.
- Taeju Lee and Minkyu Je. "Multimodal Neural Interface Circuits for Diverse Interaction With Neuronal Cell Population in Human Brain". *IEEE Transactions on Circuits and Systems II: Express Briefs (TCAS-II), Feb. 2021*.
- Jaesuk Choi, Sangyeon Youn, Jae Youn Hwang, Sohmyung Ha, Chul Kim and Minkyu Je. "Energy-Efficient High-Voltage Pulsers for Ultrasound Transducers". *IEEE Transactions on Circuits and Systems II: Express Briefs (TCAS-II), Jan. 2021*.
- Yoontae Jung, Soon-Jae Kweon, Hyuntak Jeon, Taeju Lee, Injun Choi, Kyeongwon Jeong, Mi Kyung Kim, Hyunjoo Jenny Lee, Sohmyung Ha, and Minkyu Je. "A 99.5dB-DR 5kHz-BW Closed-Loop Neural-Recording IC Based on Continuous-Time Dynamic-Zoom ΔΣADC with Automatic AFE-Gain Control". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), pp. 1-2, Nov. 2021*.
- Woojin Ahn, Doohee Kim, Jonghyeok Park, Jeong Hoan Park, Taeju Lee, Kyeongwon Jeong, Kyou Sik Min, Hoseung Lee, and Minkyu Je. "A Neural Stimulation IC Based on a Reconfigurable Current DAC with In-Situ Neural Recording Function for Cochlear Implant Systems". *in Proc. IEEE Asian Solid-State Circuits Conference (A-SSCC), pp. 1-2, Nov. 2021*.
- Jinuk Kim, Hongseok Shin, Soon-Jae Kweon, Seongwook Lee, Sohmyung Ha and Minkyu Je. "A Scalable Readout IC Based on Wideband Noise Cancelling for Full-Rate Scanning of High-Density Microelectrode Arrays". *in Proc. 43rd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC). pp. 7344-7347. Dec. 2021*.
- Donghee Cho, Hongseok Shin, Hyunwoo Park, Sein Oh, Taeju Lee, Sohmyung Ha, Chul Kim and Minkyu Je. "A Load-Current-Regulating OLED Lamp Driver Using a Hybrid Step-Up Converter with 93.21% Efficiency at a High Conversion Ratio of 4.1". *in Proc. IEEE 47th European Solid State Circuits Conference (ESSCIRC), pp. 315 - 318, Sep. 2021*.
- Taeju Lee and Minkyu Je. "A High-Precision Single-Ended-Current-to-Differential-Voltage Converter for Reconfigurable Neural Recording Front-Ends". *in Proc. IEEE International Midwest Symposium on Circuits and Systems (MWSCAS). pp. 32-35. Aug. 2021*.
- Hongseok Shin, Doojin Jang, Gyeong-Gu Kang, Jinuk Kim, Chul Kim, Sohmyung Ha and Minkyu Je. "A 96.6%-Efficiency Continuous-Input-Current Hybrid Dual-Path Buck-Boost Converter with Single-Mode Operation and Non-Stopping Output Current Delivery". *in Proc. Symposium on VLSI Circuits (SOVC), pp. 1-2, July. 2021*.
- Soon-Jae Kweon, Joonho Gil, Chulhyun Park, Sein Oh, Yoontae Jung, Injun Choi, Song-i Cheon, Hung Phan Dang, Ja-Hyuck Koo, Geunhoe Kim, Sohmyung Ha and Minkyu Je. "An 8MHz 31.25kS/s Impedance-Monitoring IC Based on IF-Sampling Architecture with a Band-Pass Delta-Sigma ADC". *in Proc. Symposium on VLSI Circuits (SOVC), pp. 1-2, July. 2021*.
- Phan Dang Hung, Yechan Park, Soon-Jae Kweon, Taeju Lee, Hyuntak Jeon, Seok-Tae Koh, Incheol Cho, Jun-Bo Yoon, Inkyu Park, Chul Kim, Sohmyung Ha and Minkyu Je. "A Self-Powered Wireless Gas Sensor Node Based on Photovoltaic Energy Harvesting". *in Proc. Symposium on VLSI Circuits (SOVC), pp. 1-2, July. 2021*.
- Hyuntak Jeon, Injun Choi, Young-Han Kim, Se-Un Shin, Minkyu Je. "A SiPM Readout IC Embedded in a Boost Converter for Mobile Dosimeters". *in Proc. Symposium on VLSI Circuits (SOVC), pp. 1-2, July. 2021*.
- Sujin Kim, Hoyong Seong, Sohyeon Kim and Minkyu Je. "ML-Based Humidity and Temperature Calibration System for Heterogeneous MOx Sensor Array in ppm-Level BTEX Monitoring". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS). April. 2021*.
- Taeju Lee, Mi Kyung Kim, Hyunjoo Jenny Lee and Minkyu Je. "A 5.7µW/Channel Folded-Current-Mirror-Based Reconfigurable Multimodal Neural Recording IC with Improved Hardware Availability". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), pp. 1-4, April. 2021*.
- Song-i Cheon, Soon-Jae Kweon, Youngin Kim, Sohmyung Ha, and Minkyu Je. "A Power-efficient, Wide-frequency-range Impedance Measurement IC Using Frequency-shift Technique". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May 2021*.
- Donghyun Youn and Minkyu Je. "A 67-pJ/bit 435-MHz 16-QAM Modulator for Capsule Endoscopy System with 18-ns Start-Up Using Transient DC Error Correction". *in Proc. IEEE International Symposium on Circuits and Systems (ISCAS), May 2021*.
- Yechan Park, Seok-Tae Koh, Jeongeun Lee, Hongkyun Kim, Jaesuk Choi, Sohmyung Ha, Chul Kim, and Minkyu Je. "A Frequency-Splitting-Based Wireless Power and Data Transfer IC for Neural Prostheses with Simultaneous 115mW Power and 2.5Mb/s Forward Data Delivery". *in Proc. International Solid-State Circuits Conference (ISSCC), Feb. 2021*.
- Jaesuk Choi, Yechan Park, Jung Bum Oh, Jun-Young Kim, Jae Youn Hwang, Sohmyung Ha, Chul Kim, and Minkyu Je. "An Energy-Replenishing Ultrasound Pulser with 0.25CV2f Dynamic Power Consumption". *in Proc. International Solid-State Circuits Conference (ISSCC), Feb. 2021*.

## 특허

누리집 Patents 페이지의 국내·국제 등록·출원 표 가운데 날짜가 2021–2026년인 68건이다(국내 등록 24, 국내 출원 20, 국제 등록 10, 국제 출원 14). 날짜와 번호는 등록 표의 Date / Publication Number 칸, 출원 표의 Date / Application Number 칸 표기이고, 제목과 발명자는 표 그대로다. 같은 발명이 출원 표와 등록 표에 함께 오른 경우가 있다.[^patents]

- 2026-04-26 · NOISE-SHAPING SAR-NESTED DSM FOR WIDE INPUT SIGNAL RANGE AND INPUT IMPEDANCE BOOSTING FOR BIO-SIGNAL RECORDING (상태 국제 출원; 발명자 Minkyu Je, Kyeongwon Jeong, Gichan Yun, Sein Oh, Yoontae Jung, Dongyoun Lee; 출원번호 US 19/639,465)
- 2026-03-26 · DIGITAL CONVERTER AND METHOD OF OPERATING THE SAME (상태 국제 출원; 발명자 Minkyu Je, Donghyun Youn, Woongro Youn, Yechan Park; 출원번호 US 19/630,285)
- 2026-03-18 · 아날로그 혼성 신호 기반 인-메모리 연산기 내 동작 및 PVT 변이에 의한 연산 오차 보상 기법 (상태 국내 등록; 발명자 제민규, 이동현, 장익준; 등록번호 10-2942870)
- 2026-01-29 · 재구성 가능한 어레이 프로세서 및 시스템 온 칩과 알고리즘의 설계 방법 (상태 국내 등록; 발명자 제민규, 변우석, 김지훈; 등록번호 10-2922214)
- 2026-01-29 · 재구성 가능한 어레이 프로세서 및 시스템 온 칩과 알고리즘의 설계 방법 (상태 국내 출원; 발명자 제민규, 변우석, 김지훈; 출원번호 10-2026-0018352)
- 2026-01-14 · CIM을 위한 메모리 장치 (상태 국내 등록; 발명자 제민규, 최종윤, 최인준, 하소명, 장익준; 등록번호 10-2914475)
- 2025-12-31 · 무선 전자약 치료 시스템 및 제어 방법 (상태 국내 출원; 발명자 제민규, 정재웅, 최해담, 김희수, 이향운, 김영구, 김솔아, 이은화; 출원번호 10-2025-0216928)
- 2025-12-30 · 복소 임피던스 측정 회로에서의 잡음 감소 방법 및 시스템 (상태 국내 등록; 발명자 제민규, 최해담, 천송이, 하소명; 등록번호 10-2907813)
- 2025-12-30 · METHOD AND DEVICE OF BIT-LEVEL-SPARSITY-BASED ANALOG-MIXED-SIGNAL IN-MEMORY MATRIX-VECTOR MULTIPLICATION WITH ROBUST ERROR CHARACTERISTICS, HIGH ENERGY EFFICIENCY, AND HIGH COMPUTATIONAL SPEED (상태 국제 출원; 발명자 Minkyu Je, Donghyeon Yi, SeoYoung Lee, Jongho Kim, Junyoung Kim, Ik-Joon Chang; 출원번호 US 19/436826)
- 2025-12-30 · METHOD AND DEVICE OF VARIABLE DYNAMIC RANGE-SOFTMAX PROCESSING FOR ENSURING HIGH ACCURACY AND ENERGY EFFICIENCY AS REPLACEMENT FOR FLOATING-POINT-BASED DEVICES (상태 국제 출원; 발명자 Minkyu Je, Donghyeon Yi, SeoYoung Lee, Jongho Kim, Junyoung Kim, Ik-Joon Chang; 출원번호 US 19/437021)
- 2025-12-30 · METHOD AND DEVICE OF BIT-SHIFT AND PARSING-BASED QUANTIZATION FOR ELIMINATING FLOATING-POINT AND DIVISION OPERATIONS FOR EFFICIENT POST-TRAINING QUANTIZATION (상태 국제 출원; 발명자 Minkyu Je, Donghyeon Yi, SeoYoung Lee, Jongho Kim, Junyoung Kim, Ik-Joon Chang; 출원번호 US 19/437051)
- 2025-12-02 · 효율적 학습 후 양자화를 위한 부동소수점 및 나눗셈 처리를 없앤 비트-시프트 및 파싱 기반 양자화 방법 및 장치 (상태 국내 출원; 발명자 제민규, 이동현, 이서영, 김종호, 김준영, 장익준; 출원번호 10-2025-0188124)
- 2025-12-02 · 부동소수점 처리 기반 디바이스 대체 가능한 높은 정확도와 에너지 효율을 보장하는 가변 범위 지원 소프트맥스 처리 및 장치 (상태 국내 출원; 발명자 제민규, 이동현, 이서영, 김준영, 김종호, 장익준; 출원번호 10-2025-0188125)
- 2025-12-02 · 강인한 에러 특성, 높은 에너지 효율, 및 높은 연산 속도를 갖는 비트-레벨 희소성 기반 아날로그 혼성 신호 인-메모리 행렬-벡터 곱셈 방법 및 장치 (상태 국내 출원; 발명자 제민규, 이동현, 김종호, 김준영, 이서영, 장익준; 출원번호 10-2025-0188123)
- 2025-11-11 · 인공와우 시스템을 위한 신경 자극기 (상태 국내 등록; 발명자 제민규, 안우진, 민규식, 이호승; 등록번호 10-2886503)
- 2025-09-16 · METHOD AND APPARATUS WITH IMPEDANCE MEASURING (상태 국제 등록; 발명자 Nahm-il Koo, Minkyu Je, Ji-Hoon Suh, Haidam Choi; 등록번호 US 12416650)
- 2025-06-30 · 연속적인 최대 공진 전력 추적 기능을 제공하는 인체 전력 전송 방법 및 시스템 (상태 국내 등록; 발명자 제민규, 서지훈, 조형주, 윤기찬, 성호용, 하소명; 등록번호 10-2829-2630000)
- 2025-05-16 · 메모리 장치를 제어하기 위한 방법 및 이를 수행하는 장치 (상태 국내 등록; 발명자 제민규, 최인준, 최종윤, 장익준, 하소명; 등록번호 10-2810-5520000)
- 2025-04-02 · 전기 임피던스 단층 촬영을 위한 넓은 입력 범위 기반 임피던스 측정 방법 및 시스템 (상태 국내 출원; 발명자 제민규, 최해담, 윤기찬, 하소명; 출원번호 10-2025-0043030)
- 2025-04-02 · 정전용량 측정을 위한 연속 시간 잡음 형성 연속 근사 레지스터 정전용량-디지털 변환기 및 그 동작 방법 (상태 국내 출원; 발명자 제민규, 윤기찬, 최해담, 하소명; 출원번호 10-2025-0043029)
- 2024-12-05 · LOAD DRIVING DEVICE (상태 국제 출원; 발명자 Minkyu Je, Donghee Cho, Chul Kim; 출원번호 US 2024/0405672 A1)
- 2024-11-18 · 초음파 펄서 및 커패시터브 부하 구동 장치 (상태 국내 등록; 발명자 제민규, 최재석, 김철; 등록번호 10-2731-6670000)
- 2024-11-13 · 신경 신호 기록 회로 (상태 국내 등록; 발명자 제민규, 권순재, 김영인, 최인준; 등록번호 10-2731-6680000)
- 2024-10-28 · 전류 컨베이어 기반 초음파 수신 장치 및 이를 포함하는 초음파 이미징 장치 (상태 국내 출원; 발명자 제민규, 윤기찬, 정경원, 최해담, 명지호; 출원번호 10-2024-0142950)
- 2024-10-24 · Continuous-time noise-shaping sar adc without excess loop delay (상태 국제 출원; 발명자 Sein Oh, Minkyu Je, Gichan Yun; 출원번호 US 2024/0356559 A1)
- 2024-09-20 · 임피던스 측정 장치 (상태 국내 등록; 발명자 권순재, 제민규, 하소명, 이정은, 천송이, 최인준, 최재석, 박예찬; 등록번호 10-2710-0060000)
- 2024-09-03 · 초음파 신호 처리 회로 (상태 국내 등록; 발명자 제민규, 정경원, 윤기찬; 등록번호 10-2704-3230000)
- 2024-08-29 · METHOD FOR IMPROVING EFFECTIVE DYNAMIC RANGE OF NEURAL STIMULATION FOR ARTIFICIAL COCHLEAR SYSTEM, AND RECONFIGURABLE CURRENT DAC-BASED NEURAL STIMULATION IC CHIP THEREFOR (상태 국제 출원; 발명자 Woojin Ahn, Minkyu Je, Kyousik Min, Hoseung Lee; 출원번호 US 2024/0292162 A1)
- 2024-08-28 · 부하 구동 장치 (상태 국내 등록; 발명자 제민규, 조동희, 김철; 등록번호 10-2701-6680000)
- 2024-07-09 · Wireless power and data transmission and reception apparatus (상태 국제 등록; 발명자 Minkyu Je, Yechan Park, Chul Kim, Seoktae Koh, Jeongeun Lee, Hongkyun Kim, Jaesuk Choi; 등록번호 US 12,034,314 B2)
- 2024-05-02 · Processing element and method of operating the same (상태 국제 출원; 발명자 Donghyeon Yi, Minkyu Je; 출원번호 US 2024/0143950 A1)
- 2024-05-01 · Processing element and method of operating the same (상태 국제 출원; 발명자 Donghyeon Yi, Minkyu Je; 출원번호 EP 4361794 A1)
- 2024-04-11 · Method and device with impedance measuring (상태 국제 출원; 발명자 Nahmil Koo, Minkyu Je, Ji-Hoon Suh, Haidam Choi; 출원번호 US 2024/0118323 A1)
- 2024-03-22 · 임피던스 측정 장치 및 임피던스 측정 방법 (상태 국내 등록; 발명자 제민규, 권순재, 길준호, 박철현, 김근회, 하소명, 정윤태, 오세인, 최인준; 등록번호 10-2651-9090000)
- 2024-02-27 · 다중 위상 기반 완화 발진 장치 및 그 제어 방법 (상태 국내 출원; 발명자 제민규, 성호용; 출원번호 10-2024-0028234)
- 2024-01-17 · 가중치의 이진 표현 분포 변화에 따른 아날로그 인공신경망 가속기의 연산오차 감소를 위한 가중치 및 편향 재학습 방법 및 시스템 (상태 국내 출원; 발명자 제민규, 이동현, 장익준; 출원번호 10-2024-0007585)
- 2024-01-17 · 비대칭 아핀 양자화 정수형 가중치 및 자유로운 배치 정규화와 양자화 기술을 포함하는 네트워크 처리를 위한 아날로그-믹스드-시그널 인-메모리-컴퓨팅 방법 및 시스템 (상태 국내 출원; 발명자 제민규, 이동현, 장익준; 출원번호 10-2024-0007586)
- 2024-01-08 · 프리차지 방법 및 이를 이용하는 프리차지 회로 (상태 국내 등록; 발명자 제민규, 윤동현, 이병석, 김근회, 구자혁, 심훈기; 등록번호 10-2624-1920000)
- 2023-10-16 · 무선 전력 및 데이터 송수신 장치 (상태 국내 등록; 발명자 제민규, 박예찬, 김철, 고석태, 이정은, 김홍균, 최재석; 등록번호 10-2591-3800000)
- 2023-10-11 · 뇌 신경 신호 기록 시스템을 위한 PVT 변화에 둔감한 노이즈 쉐이핑 SAR 수신부 집적 회로 (상태 국내 출원; 발명자 제민규, 정경원, 정윤태, 윤기찬, 윤동현, 김예근; 출원번호 10-2023-0134955)
- 2023-10-04 · 생체 신호 기록을 위한 넓은 입력 신호 범위와 입력 임피던스 증폭을 위한 노이즈 쉐이핑 SAR 기반의 델타시그마 모듈레이터 (상태 국내 출원; 발명자 제민규, 정경원, 윤기찬, 오세인, 정윤태, 이동윤; 출원번호 10-2023-0131853)
- 2023-08-30 · 정전용량 측정을 위한 전력 효율적 연속-이산 시간 하이브리드 델타시그마 정전용량-디지털 변환기 (상태 국내 출원; 발명자 제민규, 정윤태, 구지민, 오세인; 출원번호 10-2023-0114327)
- 2023-06-22 · 아날로그-디지털 컨버터 및 이의 동작 방법 (상태 국내 출원; 발명자 오세인, 제민규, 윤기찬; 출원번호 10-2023-0080650)
- 2023-04-20 · 연속 시간 잡음 형성 연속 근사 레지스터 아날로그 디지털 변환기 (상태 국내 출원; 발명자 오세인, 제민규, 윤기찬; 출원번호 10-2023-0052230)
- 2023-04-06 · 패싱 주파수 대역의 조절이 가능한 밴드 패스 모듈레이터 (상태 국내 등록; 발명자 길준호, 박철현, 구자혁, 하소명, 권순재, 정윤태, 전현탁, 제민규; 등록번호 10-2520-5120000)
- 2023-03-23 · 적응형 이득 조절 뇌 신경 신호 검출 회로 (상태 국내 등록; 발명자 정윤태, 제민규, 권순재, 전현탁, 정경원; 등록번호 10-2515-1760000)
- 2023-02-14 · 프로세싱 엘리먼트 및 이의 동작 방법 (상태 국내 출원; 발명자 이동현, 제민규; 출원번호 10-2023-0019546)
- 2023-02-01 · Amplifying device and radiation detection apparatus including the same (상태 국제 등록; 발명자 Inyong Kwon, Changyeop Lee, Hyuntak Jeon, Gyuseong Cho, Minkyu Je, Duckhyun Kim, Seungho Jhung, Dongseong Shin; 등록번호 UK GB2591166B)
- 2023-01-10 · Body channel communication method and apparatus for performing the same (상태 국제 등록; 발명자 Minkyu Je, Yesul Jeon, Chongsoo Jung; 등록번호 US 11,552,715 B2)
- 2023-01-03 · Impedance measuring apparatus (상태 국제 등록; 발명자 Wonseok Lee, Ji - Hoon Suh, Minkyu Je, Sang Joon Kim; 등록번호 US 11,543,443 B2)
- 2022-12-22 · 입력 신호 처리 회로 및 이를 이용하는 신경 신호 기록 회로 (상태 국내 등록; 발명자 제민규, 전현탁, 이태주, 권순재; 등록번호 10-2481-6250000)
- 2022-10-07 · 임피던스 측정 방법 및 장치 (상태 국내 출원; 발명자 구남일, 제민규, 서지훈, 최해담; 출원번호 10-2022-0128848)
- 2022-08-18 · 센싱 정확도를 향상시키는 캐패시턴스 센싱 디바이스 (상태 국내 등록; 발명자 구자혁, 길준호, 제민규, 권순재, 이정은; 등록번호 10-2435-4950000)
- 2022-07-27 · Smart screw (상태 국제 등록; 발명자 Shinyoon Kim, Junyoung Kim, Anna Seo, Jaeyoun Hwang, Sangyeon Youn, Jaesuk Choi, Minkyu Je; 등록번호 EP 3552567B1)
- 2022-07-21 · Epilepsy monitoring device and epilepsy monitoring system (상태 국제 출원; 발명자 Hyangwoon lee, Jewon Kang, Jihoon Kim, Minkyu Je, Seungkyun Kang; 출원번호 US 2022/0225926 A1)
- 2022-07-12 · Surgical navigation system (상태 국제 등록; 발명자 Junyoung Kim, Minkyu Je, Anna Seo, Shinyoon Kim, Duckhyun Kim, Hyunmun Kim; 등록번호 US 11,382,698 B2)
- 2022-01-25 · Smart screw (상태 국제 등록; 발명자 Shinyoon Kim, Junyoung Kim, Anna Seo, Jaeyoun Hwang, Sangyeon Youn, Jaesuk Choi, Minkyu Je; 등록번호 US 11,231,395 B2)
- 2022-01-14 · 체내 통신을 이용한 인공와우 시스템 (상태 국내 등록; 발명자 민규식, 제민규, 전예슬, 이호승, 안우진; 등록번호 10-2353-1570000)
- 2021-11-05 · 인체 채널 통신 방법 및 이를 수행하는 장치 (상태 국내 등록; 발명자 제민규, 전예슬, 정종수; 등록번호 10-2324-9910000)
- 2021-11-04 · 인공와우 시스템을 위한 신경 자극의 유효 동적 범위 개선 방법 및 이를 위한 재구성 가능한 전류 DAC 기반 신경 자극 IC 칩 (상태 국내 출원; 발명자 안우진, 민규식, 이호승, 제민규; 출원번호 10-2021-0150449)
- 2021-09-01 · Amplifying device and radiation detection apparatus including the same (상태 국제 등록; 발명자 Inyong Kwon, Changyeop Lee, Hyuntak Jeon, Gyuseong Cho, Minkyu Je, Duckhyun Kim, Seungho Jhung, Dongseong Shin; 등록번호 UK GB 2579444 B)
- 2021-08-02 · 유도 기전력 측정 방법, 유도 기전력을 이용한 마커의 위치 추적 방법, 및 이를 수행하는 장치들 (상태 국내 등록; 발명자 김현문, 반재경, 허재일, 임종화, 박용택, 제민규, 박철준, 박현우, 김준영; 등록번호 10-2287-1900000)
- 2021-07-20 · 인체 채널을 활용한 통신 및 충전 방법과 이를 수행하는 장치 (상태 국내 등록; 발명자 송용원, 김진석, 이현정, 제민규, 서지훈, 전예슬; 등록번호 10-2281-4420000)
- 2021-07-14 · 라이너 마모도 모니터링이 가능한 스마트 인공 고관절 (상태 국내 출원; 발명자 제민규, 최재석, 박예찬, 정경원, 정승호, 윤기찬, 황재윤, 김일환, 이만석, 안혜경, 이문환, 윤상연, 김동현, 김철환, 박용택, 김준영, 최창혁, 진소진; 출원번호 10-2021-0092344)
- 2021-06-10 · 뇌전증 측정기기 및 뇌전증 측정 시스템 (상태 국내 등록; 발명자 이향운, 강제원, 김지훈, 제민규, 강승균; 등록번호 10-2265-9010000)
- 2021-04-08 · Surgical Navigation System For Registering Coordinates of Patient-Customized Tool (상태 국제 출원; 발명자 Junyoung Kim, Shinyoon Kim, Anna Seo, Hyunmun Kim, Hyundeok Kim, Minkyu Je, Jaessuk Choi; 출원번호 US 2021/0100621 A1)
- 2021-02-25 · Method for data communication and power charging using human body channel, and device for performing the same (상태 국제 출원; 발명자 Yongwon Song, Jinseok Kim, Hyunjung Yi, Ji-hoon Suh, Yeseul Jeon; 출원번호 US 2021/0058164 A1)
- 2021-02-23 · Position indicating apparatus and bone fixation apparatus including the same (상태 국제 등록; 발명자 Jeyoun Hwang, Junyoung Kim, Jihun Kim, Jaesuk Choi, Minkyu Je; 등록번호 US 10,925,686 B2)

## 수상

누리집 Award & Granted 페이지에 오른 2021년 10월 이후 44건이다. 학생과 연구실의 수상, 교수의 수상, 학회 참가 지원(Travel Grant)·박사과정 연구 지원(Pre-doctoral Grant)이 함께 실려 있다. 날짜는 페이지가 적은 달이고, 상 이름과 수상자 표기는 페이지 문장 그대로다.[^awards]

- May 2026 · Dong-Hwi Choi, IEEE Circuits and Systems Society (CASS) Pre-doctoral Grant 2026
- May 2026 · Kim Hoang Nguyen, International Symposium on Circuits and Systems (ISCAS) Student Travel Grant 2026
- Feb. 2026 · Gichan Yun, Solid-State Circuits Society (SSCS) Pre-doctoral Achievement Award 2025-2026
- Oct. 2025 · Gichan Yun, IEEE Circuits and Systems Society (CASS) Student Travel Grant 2025 (ISICAS)
- Jul. 2025 · Dongyoon Lee, Grand Prize, Center for Biomedical System Semiconductor Chip Design Contest (CDC)
- Jul. 2025 · Seungjun Park, Encouragement Prize, Center for Biomedical System Semiconductor Chip Design Contest (CDC)
- Jul. 2025 · Dogyun Bae, Encouragement Prize, Center for Biomedical System Semiconductor Chip Design Contest (CDC)
- June. 2025 · Dong-Hwi Choi, Symposium on VLSI Technology and Circuits (SOVC) Student Travel Assistance
- May. 2025 · Minkyu Je, 교수혁신상, Korea Advanced Institute of Science and Technology (KAIST)
- May. 2025 · Song-I Cheon, IEEE Circuits and Systems Society (CASS) Pre-Doctoral Grant
- May. 2025 · Yunchul Chung and Hyunyeop Lee, YP Best Paper Award, IEEE International Symposium on Circuits and Systems (ISCAS) for presenting "Implantable Galvanic-Coupled Body Channel Communication Transceiver with Serpentine-Interconnection Electrode Pair for Post-Operative Monitoring of Joint Replacement"
- May. 2025 · Christopher Santos and Dong-Hwi Choi, Best Paper Award Runner-up in the Biomedical and Life Science Circuits and Systems (BioCAS) Track, IEEE International Symposium on Circuits and Systems (ISCAS)
- April. 2025 · Seoyoung Lee, Best Student Paper Award, IEEE International Conference on Artificial Intelligence Circuits and Systems (AICAS), for a paper entitled “A 94.76 %-accuracy, < 16μs/classification-Latency STT-MRAM CiM-Based Classifier for Closed-Loop Peripheral Nerve Modulation Implants”
- Feb. 2025 · Donghyun Youn, Woongro Youn, Yechan Park, Bronze Prize, the 31st Samsung Humantech Paper Award, for a paper entitled “A PM-SAR Hybrid Capacitance-to-Digital Converter with pF-to-nF Input and μs-to-ms Sensing for Wide Application”
- Mar. 2025 · Jongyoon Choi, Best Research Achievement Award, 2024 Kim Choong-Ki Award
- Feb. 2025 · Yechan Park, KAIST Global Leadership Award (Challenge)
- Feb. 2025 · Yechan Park, Solid-State Circuits Society (SSCS) Pre-doctoral Achievement Award 2024-2025
- Oct. 2024 · Edward Jongyoon Choi and Vincent Lukito, Corporate Special Award (Telechips), the 25th Korea Semiconductor Design Challenge, for a design entry entitled "Spike Sorting SoC with Delta-based Detection and Analog CIM-based Autoencoder Neural Network Feature Extraction Achieving 94.54% Accuracy"
- Aug. 2024 · Hyungjoo Cho, Special Prize (IEEE-SSCS Seoul Chapter), 2024 IDEC Congress Chip Design Contest (CDC), for a paper entitled "An Electromagnetic Energy Harvester with Single Passive Component Tuning Duty-Modulated Maximum-Power-Point-Tracking"
- Jul. 2024 · Edward Jongyoon Choi and Vincent Lukito, Best Paper Award, ISE 2024 Summer Annual Conference, for a paper entitled “Spike Sorting SoC using Analog CIM Autoencoder Neural Network Feature Extraction and Delta Spike Detection”
- Jul. 2024 · Song-I Cheon and Haidam Choi, Best Design Award, 2024 IDEC Congress Chip Design Contest (CDC), for a paper entitled "A Two-Electrode Bio-Impedance Readout IC with Complex-Domain Noise-Correlated Baseline Cancellation"
- May 2024 · Sunglim Han, Best Paper Award in the Biomedical and Life Science Circuits and Systems (BioCAS) Track, IEEE International Symposium on Circuits and Systems (ISCAS), for a paper entitled “A 72-Channel Resistive-Sensor Interface IC with High Energy Efficiency and a Wide Input Range”
- May 2024 · Jimin Koo, IEEE International Symposium on Circuits and Systems (ISCAS) Student Travel Grant 2024
- May 2024 · Haidam Choi, IEEE Circuits and Systems Society (CASS) Student Travel Grant 2024 (ISCAS)
- Apr. 2024 · Yoontae Jung, Best Research Achievement Award, 2023 Kim Choong-Ki Award
- Feb. 2024 · Song-I Cheon, IEEE International Solid-State Circuits Conference (ISSCC) Student Travel Grant 2024
- Feb. 2024 · Yoontae Jung, IEEE Solid-State Circuits Society (SSCS) Pre-Doctoral Achievement Award 2023-2024
- Jan. 2024 · Donghyun Youn, CDC Best Design Award, the 31st Korean Conference on Semiconductors, for a paper entitled "Design Points of Period-modulation Capacitance-to-digital Converter for Continuous Glucose Monitoring System"
- Jan. 2024 · Donghyun Youn, Best Paper Award in the S. Chip Design Contest Track, for a paper entitled "Design Points of Period-modulation Capacitance-to-digital Converter for Continuous Glucose Monitoring System"
- Sep. 2023 · Gichan Yun, Best Paper Award, the 23rd RF/Analog Circuit Workshop, for a paper entitled “A 2pA/√Hz Current Conveyor-assisted Ultrasound Receiver with 25-pF CMUT Parasitic Capacitance”
- Sep. 2023 · Best Laboratory Award, the 23rd RF/Analog Circuit Workshop
- Aug. 2023 · Seoyoung Lee, Encouragement Prize, Center for Biomedical System Semiconductor Chip Design Contest (CDC)
- Aug. 2023 · Dong-Hwi Choi, Encouragement Prize, Center for Biomedical System Semiconductor Chip Design Contest (CDC)
- Aug. 2023 · Gichan Yun, Encouragement Prize, Center for Biomedical System Semiconductor Chip Design Contest (CDC)
- Aug. 2023 · Haidam Choi, Excellence Prize, Center for Biomedical System Semiconductor Chip Design Contest (CDC)
- Jul. 2023 · Yoontae Jung, IEEE Circuits and Systems Society (CASS) Student Travel Grant 2023 (ISCAS)
- Dec. 2022 · Minkyu Je, 해동반도체공학상, The Institute of Semiconductor Engineers (ISE)
- Dec. 2022 · Edward Jongyoon Choi, IEEE CASS Paper Award, the 5th Annual Conference of ISE
- Sep. 2022 · Best Laboratory Award, the 22nd RF/Analog Circuit Workshop
- Sep. 2022 · Ji-Hoon Suh, Best Student Paper Award (Winner), the 22nd RF/Analog Circuit Workshop, for a paper entitled “A Battery-less Electrochemical Sensing System Based on Intra-Body Power Transfer”
- Sep. 2022 · Injun Choi, Sponsor Company Award (Point2Tehcnology), the 22nd RF/Analog Circuit Workshop, 2022, for a paper entitled “An eFlash-Based Computation-in-Memory for Edge Computing”
- Sep. 2022 · Edward Jongyoon Choi, Workshop Organizer Award (Kangwon University), the 22nd RF/Analog Circuit Workshop, 2022, for a paper entitled “Bit-Configurable Pulse Train SRAM IMC Macro for Edge devices”
- Sep. 2022 · Haidam Choi, Workshop Organizer Award (Qualitas Semiconductor), the 22nd RF/Analog Circuit Workshop, 2022, for a paper entitled “A ∆-∆∑-Based Bio-Impedance Readout IC with Baseline Cancellation”
- Jul. 2022 · Kyeongwon Jeong, Best Design Award, IDEC Chip Design Contest (CDC), for a paper entitled "A 20-MHz 2.3-MW Ultrasound Receiver and a High-voltage Transmitter for Ultrasound Capsule Endoscopy"

## 소식

누리집 첫 화면 Latest News의 2026년 8–9월 글 5건이다. 날짜는 게시된 연·월이고 문장은 게시된 영어 글이다.[^home]

- 2026/09 · Yeri, Minh, Gaeun, Jaegeon, Sanghyun, and Juhyeong have joined IMPACT Lab since this fall semester. Welcome!
- 2026/08 · Great news! Changhun, Hyunyeop, Joowon, Hong-Anh, Radithya's works have been accepted to BioCAS 2026.
- 2026/08 · Great news! Jiho's work of JSSC 2026 is now available as early access.
- 2026/08 · Great news! Byeongseon, Heewon, Hung & Thai's works have been accepted to A-SSCC 2026.
- 2026/08 · Great news! Donghyeon's works have been accepted to ICCAD 2026.

## 연락과 위치

- 주소: #316, NanoFab Center (E19), KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon 34141[^contact]
- 연구실 전화: (+82) 042-350-7637[^contact]
- 교수 연락처: 전화 +82 42 350 7437, 이메일 mkje@kaist.ac.kr[^pi][^eeprof]
- 교수 사무실: 연구실 PI 페이지는 나노종합기술원(NanoFab Center, E19) 316호, 전기및전자공학부 교수 소개와 반도체시스템공학과 페이지는 같은 건물 317호로 적는다.[^pi][^eeprof][^ssep]
- Contact 페이지는 학부생과 연구원의 합류를 받는다며 관심 있으면 교수에게 이메일로 문의하라고 안내하고, 센서 인터페이스·뇌-기계 인터페이스 IC, 메모리 내 처리 IC, 전력 관리 IC 분야별 추천 과목을 적는다(페이지 갱신 표기 2022-10-25).[^contact]
[^p1]: H. Choi 외, M. Je, IEEE Journal of Solid-State Circuits 59, 3538-3548 (2024). <https://doi.org/10.1109/jssc.2024.3439865> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: Y. Jung 외, M. Je, IEEE Journal of Solid-State Circuits 57, 3071-3082 (2022). <https://doi.org/10.1109/jssc.2022.3188626> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: K. Jeong 외, M. Je, IEEE Journal of Solid-State Circuits 58, 2778-2789 (2023). <https://doi.org/10.1109/jssc.2023.3276130> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: D.-H. Choi 외, M. Je, IEEE Open Journal of the Solid-State Circuits Society 5, 324-334 (2025). <https://doi.org/10.1109/ojsscs.2025.3642787> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: Y. Park 외, M. Je, IEEE Journal of Solid-State Circuits 60, 3966-3984 (2025). <https://doi.org/10.1109/jssc.2025.3611278> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: D. Cho 외, M. Je, IEEE Journal of Solid-State Circuits 58, 720-731 (2023). <https://doi.org/10.1109/jssc.2022.3230424> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: C. Jung 외, M. Je, IEEE Journal of Solid-State Circuits 58, 2675-2684 (2023). <https://doi.org/10.1109/jssc.2023.3290357> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: V. Lukito 외, M. Je, IEEE Journal of Solid-State Circuits 61, 1710-1721 (2026). <https://doi.org/10.1109/jssc.2025.3589523> 초록 기준(Semantic Scholar 등록 초록).
[^home]: IMPACT Lab 누리집 첫 화면 <https://impact.kaist.ac.kr/> (Introduction, Latest News, 2026-10-23 열람)
[^research]: IMPACT Lab 누리집 Research 페이지 <https://impact.kaist.ac.kr/research> (Microsystem Integration & Convergence-Ready Integrated Circuit Technology Platform, 2026-10-23 열람)
[^sensor]: IMPACT Lab 누리집 Research 「1. Sensor Interface ICs」 <https://impact.kaist.ac.kr/research/1-sensor-interface-ics> (2026-10-23 열람)
[^system]: IMPACT Lab 누리집 Research 「2. System Integration and Application」 <https://impact.kaist.ac.kr/research/2-system-integration-and-application> (2026-10-23 열람)
[^wireless]: IMPACT Lab 누리집 Research 「3. Wireless Communication ICs」 <https://impact.kaist.ac.kr/research/3-wireless-communication-ics> (2026-10-23 열람)
[^energy]: IMPACT Lab 누리집 Research 「4. Energy Supply and Management ICs」 <https://impact.kaist.ac.kr/research/4-energy-supply-and-management-ics> (2026-10-23 열람)
[^timing]: IMPACT Lab 누리집 Research 「5. Timing ICs」 <https://impact.kaist.ac.kr/research/5-timing-ics> (2026-10-23 열람)
[^computing]: IMPACT Lab 누리집 Research 「6. Computing ICs」 <https://impact.kaist.ac.kr/research/6-computing-ics> (2026-10-23 열람)
[^pi]: IMPACT Lab 누리집 Members 「1. Principal Investigator (PI)」 <https://impact.kaist.ac.kr/members/1-principal-investigator-pi> (2026-10-23 열람)
[^visiting]: IMPACT Lab 누리집 Members 「2. Regular Visiting Professor」 <https://impact.kaist.ac.kr/members/2-regular-visiting-professor> (2026-10-23 열람)
[^researchers]: IMPACT Lab 누리집 Members 「3. Researchers」 <https://impact.kaist.ac.kr/members/3-researchers> (Researchers, Previous Researchers, 2026-10-23 열람)
[^phd]: IMPACT Lab 누리집 Members 「4. Ph.D. Students」 <https://impact.kaist.ac.kr/members/4-ph-d-students> (2026-10-23 열람)
[^ms]: IMPACT Lab 누리집 Members 「5. M.S. Students」 <https://impact.kaist.ac.kr/members/5-m-s-students> (2026-10-23 열람)
[^alumni]: IMPACT Lab 누리집 Members 「6. Alumni」 <https://impact.kaist.ac.kr/members/6-alumni> (Ph.D. Degree, Master's Degree, 2026-10-23 열람)
[^journals]: IMPACT Lab 누리집 Publications 「1. International Journals」 <https://impact.kaist.ac.kr/publications/1-international-journals> (목록 범위는 근거 페이지, 2026-10-23 열람)
[^confs]: IMPACT Lab 누리집 Publications 「2. International Conferences」 <https://impact.kaist.ac.kr/publications/2-international-conferences> (목록 범위는 근거 페이지, 2026-10-23 열람)
[^books]: IMPACT Lab 누리집 Publications 「3. Books & Book Chapters」 <https://impact.kaist.ac.kr/publications/3-books-book-chapters> (2026-10-23 열람)
[^patents]: IMPACT Lab 누리집 Publications 「4. Patents」 <https://impact.kaist.ac.kr/publications/4-patents> (Domestic Patents, International Patents 표, 2026-10-23 열람)
[^awards]: IMPACT Lab 누리집 Publications 「5. Award & Granted」 <https://impact.kaist.ac.kr/publications/5-award-granted> (2026-10-23 열람)
[^contact]: IMPACT Lab 누리집 Contact 페이지 <https://impact.kaist.ac.kr/contact> (2026-10-23 열람)
[^eeprof]: KAIST 전기및전자공학부 교수 소개(제민규) <https://ee.kaist.ac.kr/professor/12964/> (주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 디비전, 학위, 대표업적, 2026-10-23 열람)
[^eelist]: KAIST 전기및전자공학부 전임교수 목록 3쪽 <https://ee.kaist.ac.kr/professor-s1/?page=3> (제민규 항목: 직위, 사무실, 디비전, 2026-10-23 열람)
[^ssep]: KAIST 반도체시스템공학과 교수진 <https://sse.kaist.ac.kr/professor/> (제민규 교수 항목, 2026-10-23 열람)

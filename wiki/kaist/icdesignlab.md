# 회로설계 연구실 (Circuit Lab)

**KAIST 전기및전자공학부 · 김현식 교수**

- 분야: 아날로그 집적회로 설계, 디스플레이 구동회로, 전력변환회로, 검출회로
- 대분야: 전기전자·반도체·광학
- 태그: 집적회로 설계[^home][^eeprof][^p1], 디스플레이·발광 소자[^research], 마이크로 LED[^research], 에너지 하베스팅[^research][^p8], 배터리 관리 시스템[^research], 전력 관리 집적회로[^p3], 센서 인터페이스·판독 집적회로[^research], 데이터 변환기(ADC·DAC)[^p1]
- 홈페이지: <https://www.icdesignlab.net>
- 근거와 출처: [회로설계 연구실 근거 페이지](icdesignlab-sources.md)

> 화면을 움직이는 디스플레이 구동 칩, 전자 기기에 맞는 전압을 만들어 공급하는 전력 관리 칩, 센서 신호를 읽어 내는 판독 칩을 아날로그 집적회로로 설계하고, 이 지식을 모아 완전한 시스템 온 칩을 만들려는 연구실이다.[^home][^research]

## 무엇을 연구하나

연구실은 아날로그 신호 처리 회로, 센서 판독 회로, 전력 관리 회로(PMIC, 전자 기기 안에서 전압을 바꾸고 조절해 각 부분에 전력을 나눠 주는 칩), 디스플레이 구동 회로(DDI, 화면의 화소에 밝기 신호를 보내는 칩)의 집적회로 설계에 집중하고, 궁극적으로 이 분야들의 지식을 모아 완전한 시스템 온 칩(SoC, 여러 기능의 회로를 칩 하나에 모은 것) 해법을 만들 계획이라고 소개한다.[^home] 전기및전자공학부 교수 소개와 반도체시스템공학과 연구실 목록은 주요 연구를 아날로그 집적회로 설계, 디스플레이 구동회로, 전력변환회로, 검출회로로 적는다.[^eeprof][^ssel] Research 페이지가 꼽는 핵심어는 아날로그 회로, 에너지 효율이 높은 증폭기, 전력 변환기, 전압 레귤레이터(입력 전압이 흔들려도 일정한 출력 전압을 내는 회로), 디스플레이 구동기, 저잡음 판독 회로, 광자 계수 검출기, 스위치드 커패시터·스위치드 전류 회로다.[^research]

Research 페이지의 첫째 주제는 OLED(유기 발광 다이오드)·LCD(액정 디스플레이) 화면용 디스플레이 구동 IC다. 감마 보정을 넣으면서 면적을 적게 차지하는 고해상도 디지털-아날로그 변환기(DAC, 디지털 숫자를 전압 같은 아날로그 신호로 바꾸는 회로), 빠른 출력 구동 증폭기, OLED 수명을 늘리려고 열 단위 채널 안에 넣은 화소 판독 회로, 마이크로 LED 화면을 위한 웨이퍼 수준의 완전 집적 CMOS 백플레인(화소를 하나하나 켜고 끄는 회로가 깔린 화면 뒤판)을 연구 항목으로 둔다.[^research]

둘째 주제는 전력 변환·관리 IC다. 인덕터(코일)·커패시터(축전기)와 이 둘을 섞은 하이브리드 방식의 스위칭 전력 변환기, 에너지 하베스팅(주변의 움직임·열·빛에서 작은 전력을 모으는 기술) 회로와 시스템, 전원 잡음을 잘 막는 LDO 레귤레이터(입력과 출력의 전압 차이가 작아도 동작하는 선형 전압 레귤레이터), 배터리 관리·충전 IC, 전력 제어·관리 회로를 연구 항목으로 든다.[^research]

셋째 주제는 센서 인터페이스와 판독 IC다. 영상용 배열 판독 IC, 저선량 X선 검출기와 박막 트랜지스터(TFT) 판독 IC, 광자 계수 검출기(PCD, 들어오는 X선 광자를 하나씩 세는 검출기), 터치 감지 기능을 갖춘 화면, 유리·플라스틱 기판 위에 다결정 실리콘(poly-Si)·비정질 실리콘(a-Si:H) TFT로 만든 대면적 전자 소자를 둔다.[^research]

대표 논문으로 보면 연구는 네 갈래다. 첫째, 모바일 OLED 화면의 소스 드라이버와 화면을 켠 채 화소 전류를 읽는 구동 칩이다(대표 논문 1, 2).[^p1][^p2] 둘째, 배터리 전압을 바꾸거나 모바일 프로세서에 전원을 공급하는 하이브리드 DC-DC 변환기(직류 전압을 다른 직류 전압으로 바꾸는 회로)다(대표 논문 3, 4).[^p3][^p4] 셋째, 칩 안에 넣는 전압 레귤레이터와 LDO, 칩 위에 흩어 놓아 전력을 고르게 나눠 주는 디지털 LDO다(대표 논문 5, 6, 7).[^p5][^p6][^p7] 넷째, 마찰전기 나노발전기에서 전력을 모으는 하베스팅 칩이다(대표 논문 8).[^p8] 여덟 편 모두 칩을 실제 반도체 공정으로 만들어 측정한 결과를 보고한다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 주요 연구 주제

### 1. 모바일 OLED 화면의 구동 칩

화면의 각 열에 밝기 전압을 보내는 10비트 소스 드라이버 IC에서, 면적을 아끼면서도 한 줄을 그리는 시간을 늘리지 않으려고 주 출력을 내보내는 동안 전압을 보간하는 전하를 함께 넣는 전하 변조 DAC를 만들었다.[^p1] 화면을 켠 채로 화소 전류를 읽는 회로를 열마다 나란히 넣은 OLED 구동 IC도 만들어, 전류를 민감하게 재는 적분기와 패널 잡음을 걸러 내는 필터를 갖췄다.[^p2] 대표 논문 1, 2.

### 2. 하이브리드 DC-DC 변환기

배터리 전압을 3.4 V로 바꾸며 강압과 승압을 한 가지 모드로 끊김 없이 오가는 좌우 대칭 하이브리드 벅부스트 변환기와,[^p3] 모바일 응용 프로세서에 0.4–1.5 V를 공급하면서 플라잉 커패시터의 돌입 전류를 줄인 3레벨 이중 경로 벅 변환기를 만들었다.[^p4] 대표 논문 3, 4.

### 3. 칩 안 전압 레귤레이터와 전력 공급

플라잉 커패시터 하나로 두 위상의 인덕터 전류 균형을 스스로 맞추는 완전 집적 전압 레귤레이터,[^p5] 작은 온칩 커패시터만으로 넓은 주파수 범위에서 전원 잡음을 막는 LDO,[^p6] 작은 디지털 LDO 단위 36개를 칩 위에 흩어 놓고 이웃끼리 전류를 나눠 맡게 한 분산 LDO 패브릭을 만들었다.[^p7] 교수는 IEEE Solid-State Circuits Magazine에 에너지 효율이 높은 LDO 레귤레이터 설계에 관한 해설 글을 2023년과 2026년에 실었다.[^pubs][^home] 대표 논문 5, 6, 7.

### 4. 에너지 하베스팅 칩

마찰전기 나노발전기의 높은 전압을 다루려고 칩 여러 개를 쌓아 에너지를 뽑아내고, 이어 붙인 칩 사이 제어 신호를 맞추는 하베스팅 인터페이스 칩 시스템을 만들었다.[^p8] 대표 논문 8.

## 대표 논문

랩 Journals 목록의 2021–2026년 학술지 논문 가운데 김현식 교수가 마지막 저자이자 교신저자(\*)인 논문을, 네 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2024 | [A 10-Bit Source-Driver IC With Charge-Modulation DAC for Enhanced Frame-Rate Mobile OLED Displays](https://doi.org/10.1109/jssc.2024.3442248) · IEEE Journal of Solid-State Circuits (JSSC) | 모바일 화면용 10비트 소스 드라이버 IC(화면의 각 열에 밝기 전압을 보내는 칩)를 만들었다. 면적을 아끼는 기존 설계는 디지털-아날로그 변환 속도를 희생해, 화면 한 줄을 그리는 데 쓰는 시간(1-H 시간)이 늘어났다. 이 연구는 주 출력을 내보내는 동안 전압을 보간하는 전하를 나란히 넣어 면적 효율과 속도를 함께 얻으려 했다. 그 중심인 전하 변조(QM) DAC는 면적 효율이 높고, 직류 전압을 그대로 보간해 선형성을 확보한다. 전압을 전하로 바꿀 때 생기는 오차를 상쇄하는 상관 이중 적분(CDI) 기법과, 버퍼 증폭기의 출력 전압이 바뀌는 속도(슬루율)를 적은 부담으로 높이는 방법도 내놓았다. 180nm CMOS 공정으로 만든 600채널 시제품은 채널당 면적 3315 μm², 1-H 시간 1.5 μs였고, 100 pF 부하에서 슬루율 22 V/μs를 얻었다. 출력 전압 편차(DVO)는 최대 11.5 mV였다.[^p1] | 1저자 Y. Park, 마지막·교신 저자 김현식 (7명) |
| 2 | 2025 | [A Column-Parallel On-Programming Pixel-Current Readout Embedded in an OLED Display Driver IC](https://doi.org/10.1109/jssc.2025.3538075) · IEEE Journal of Solid-State Circuits (JSSC) | 화면이 실제로 동작하는 동안 화소 전류를 재는 회로를 열마다 나란히 넣은 OLED 구동 IC다. 전류를 민감하게 재면서 잴 수 있는 범위(동적 범위)를 넓히는 접는 적분기(FI)를 쓰고, 화소에 화면 데이터를 써 넣는 동안 전류를 잴 수 있도록 소스 구동 화소와 아날로그 전단(AFE)을 합친 전압 구동기(ACD)를 두었다. 여러 채널에 함께 끼는 패널 잡음은 채널들이 같이 쓰는 공통 모드 잡음 제거 필터(CMRF)로 억제했다. 180nm CMOS 공정으로 만든 16채널 시제품에서 FI는 80 mV/nA의 감도와 16배 넓어진 동적 범위를 보였고, CMRF는 잡음을 최대 63 dB 줄였다. 11비트 전류 판독의 신호 대 잡음비는 60.3 dB였고, LED로 한 실제 시연에서 화소 전류 감지 기능과 성능을 확인했다.[^p2] | 1저자 G.-W. Lim, 마지막·교신 저자 김현식 (10명) |
| 3 | 2024 | [A Power-Efficient Single-Mode Buck-Boost DC–DC Converter With Bilaterally Symmetrical Hybrid Topology](https://doi.org/10.1109/jssc.2024.3452238) · IEEE Journal of Solid-State Circuits (JSSC) | 배터리 전압을 3.4 V로 바꾸는 좌우 대칭 하이브리드 벅부스트(전압을 낮추기도 높이기도 하는) 변환기 BS-HBB다. 기존 벅부스트 변환기는 부하 전류에 비해 인덕터 전류가 커서 전도 손실이 컸다. 플라잉 커패시터(스위치로 연결을 바꿔 가며 쓰는 축전기)를 더한 하이브리드 설계들이 인덕터 전류를 줄이려 했지만, 모드 사이 전환이 매끄럽지 않거나, 강압과 승압 구간 중 한쪽에서는 전류를 줄이지 못하거나, 켜졌을 때 저항이 큰 고전압 스위치를 써야 했다. BS-HBB 구조는 전체 전압 변환 범위에서 한 가지 모드로 끊김 없이 동작하고, 강압·승압 구간 모두에서 인덕터 전류를 줄이며, 켜졌을 때 저항이 낮은 저전압 CMOS 스위치를 써서 전력 효율을 높인다. 180nm CMOS 공정으로 만든 칩은 2.7–4.2 V 입력에서 3.4 V를 최대 1 A까지 내보내고, 직류 저항 9 mΩ 인덕터로 최고 효율 96.9%(250 mΩ 인덕터로 95.5%)를 얻었다. 입력 전압이 계속 흔들리는 조건에서도 흐트러짐 없는 출력 전압을 보여 한 가지 모드 동작을 확인했다.[^p3] | 1저자 D.-H. Kim, 마지막·교신 저자 김현식 (2명) |
| 4 | 2026 | [A Three-Level Dual-Path Hybrid Buck Converter With Mitigated Capacitive Current and Seamless DVS Across a Wide Output Voltage Range](https://doi.org/10.1109/jssc.2026.3710310) · IEEE Journal of Solid-State Circuits (JSSC) | 모바일 응용 프로세서(AP)에 맞춰 1.8 V 입력을 0.4–1.5 V로 낮추는 3레벨 이중 경로(TLDP) 벅(강압) 변환기다. 기존 벅 변환기와 다중 레벨 벅 변환기는 부하 전류가 커지면 작은 인덕터의 직류 저항 손실이 감당하기 어려울 만큼 커진다. 플라잉 커패시터로 출력 전력 일부를 보내 인덕터 직류 전류를 줄이려 한 다중 경로 벅 설계들은 전압 변환 비율(VCR) 범위가 좁고, 특정 비율에서 커패시터로 몰려드는 돌입 전류 때문에 효율이 크게 떨어졌다. TLDP 벅 변환기는 0–1의 전체 VCR 범위에서 끊김 없이 동작하면서 돌입 전류의 급증을 억제한다. 대표적인 공급 전압 0.9 V에서 인덕터 전류를 최적으로 줄이고 인덕터 전류의 출렁임을 0에 가깝게 해, 작은 인덕터에서 생기는 손실을 줄였다. 28nm CMOS 공정으로 만든 칩은 전체 면적 3.38 mm²에서 최대 2.5 A를 공급하고, 부피 1 mm³ 인덕터로 최고 효율 96.5%를 얻었다.[^p4] | 1저자 J.-H. Kim, 마지막·교신 저자 김현식 (4명) |
| 5 | 2024 | [A Fully Integrated Multi-Phase Voltage Regulator With Flying-Capacitor-Based Inter-Inductor Current Self-Balancing Scheme and Charge-Recycling Gate Driver](https://doi.org/10.1109/jssc.2024.3360708) · IEEE Journal of Solid-State Circuits (JSSC) | 전압 조절 회로를 인덕터까지 칩 안에 넣은 완전 집적 전압 레귤레이터(FIVR)다. 높은 전력 밀도, 빠른 동적 전압 조절(DVS, 처리할 일의 양에 맞춰 공급 전압을 바꾸는 것), 인덕터 전류의 자체 균형을 갖췄다. 제안한 2상 2L1C 벅 변환기 구조는 기존 2상 3레벨 변환기보다 전력 스위치와 플라잉 커패시터 수를 절반으로 줄이면서 낮은 스위칭 전압의 이점은 그대로 얻는다. 핵심 기여는 추가 부담 없이 플라잉 커패시터 하나로 인덕터 전류의 균형을 스스로 맞추는 방식이다. 이 구조를 여러 위상으로 넓힐 수 있게 하는 채널 간 균형(ICB) 방식과 스위칭 전력 손실을 줄이는 전하 재활용 게이트 구동기도 내놓았다. 2 nH 온칩 나선형 인덕터를 쓴 2상 칩을 55nm CMOS 공정으로 만들었고, 위상당 200 MHz에서 DVS 속도 45 V/μs, 전력 밀도 0.9 W/mm², 최고 효율 79.1%를 얻었다. 최대 2 W를 공급하는 4상 칩으로 ICB 방식을 확인했다.[^p5] | 1저자 J.-H. Cho, 마지막·교신 저자 김현식 (6명) |
| 6 | 2024 | [A Fully Integrated, Domino-Like-Buffered LDO Regulator With High Power-Supply Rejection Across the Full Frequency Spectrum](https://doi.org/10.1109/jssc.2024.3445127) · IEEE Journal of Solid-State Circuits (JSSC) | 넓은 주파수 범위 전체에서 전원 잡음 제거비(PSR, 입력 전원의 흔들림이 출력으로 새어 나가지 않게 막는 정도)가 높은 완전 집적 LDO 레귤레이터다. 제안한 도미노형 버퍼(DLB) 설계는 여러 단으로 이어진 버퍼가 잘게 나눈 출력 트랜지스터를 차례로 구동해, 작은 출력 커패시터 때문에 생기는 안정성 문제에 대응한다. 그래서 출력단이 주파수 응답을 좌우하도록 설계한(OPD) LDO가 본래 가진 높은 PSR의 장점을 작은 온칩 커패시터로도 살릴 수 있다. 같은 위상 여유(회로가 안정하게 동작하는 여유를 나타내는 값)를 지키는 데 필요한 출력 커패시터 요구를 기존 LDO 설계보다 2.4배 완화한다. 28nm CMOS 공정으로 만든 칩은 입력·출력 전압 차이 200 mV에서 최대 10 mA를 공급한다. 50 pF의 작은 온칩 커패시터만으로 10 Hz–1 GHz 전 구간에서 최악의 경우에도 PSR –28 dB를 보였고, 온칩 커패시터를 포함한 면적은 0.012 mm²다.[^p6] | 1저자 J.-G. Lee, 마지막·교신 저자 김현식 (2명) |
| 7 | 2026 | [A Fully Synthesizable, Fine-Grained Distributed Digital-LDO Fabric Featuring Freely Linkable Current-Sharing Network for Scalable On-Chip Power Delivery](https://doi.org/10.1109/jssc.2025.3648866) · IEEE Journal of Solid-State Circuits (JSSC) | 작은 LDO 단위를 칩 위에 6×6으로 흩어 놓고 서로 자유롭게 잇는 완전 디지털 분산 LDO 패브릭이다. 중앙 제어기 없이 단위를 이어 붙일 수 있어, 큰 시스템 온 칩(SoC)의 전원 영역까지 늘려도 IR 강하(배선 저항 때문에 전압이 떨어지는 현상)가 작다. 자유 연결 전류 공유(FLCS) 망은 이웃한 LDO끼리 디지털 출력 전류 값만 주고받아 칩 전체를 잇는 배선의 병목을 없애고, 여러 연결 방식에서 부하를 고르게 나눈다. 이렇게 이웃끼리만 주고받는 방식으로 0.8 mm² 전원망에서 900 mA 부하일 때 최대 IR 강하를 4 mV 아래로 묶었다. 28nm CMOS 공정에서 기본 디지털 셀로 합성한 각 마이크로 LDO는 720 μm²를 차지하고 최대 25 mA를 공급해 전류 밀도 34.7 A/mm²를 얻었다. 36개 LDO 패브릭의 전류 공유 부정확도는 이전 분산 LDO 시스템보다 10배 줄었고, 입력·출력 전압 차이 50 mV에서 최고 전류 효율 91.3%를 보였다.[^p7] | 1저자 Y.-J. Lee, 마지막·교신 저자 김현식 (3명) |
| 8 | 2022 | [A Triboelectric Energy-Harvesting Interface With Scalable Multi-Chip-Stacked Bias-Flip and Daisy-Chained Synchronous Signaling Techniques](https://doi.org/10.1109/jssc.2022.3193738) · IEEE Journal of Solid-State Circuits (JSSC) | 마찰전기 나노발전기(TENG, 두 물질이 닿았다 떨어질 때 옮겨 가는 전하로 움직임을 전기로 바꾸는 장치)에서 에너지를 모으는 인터페이스 칩 시스템이다. TENG는 개방 전압이 높고 기생 커패시턴스(의도하지 않게 생기는 축전 성분)가 커서 하베스팅 집적회로를 설계하기 어렵다. 이 연구는 칩을 여러 개 쌓아 LDMOS 트랜지스터의 전압 한계(약 70 V)를 넘는 높은 추출 전압으로 에너지를 모으는 다중 칩 적층 바이어스 플립(MCS-BF) 기법을 내놓았다. 직렬 인덕터로 기생 커패시턴스 때문에 생기는 에너지 손실을 없애고, 칩 여러 개를 차례로 이어 연결해도 과전압 부담 없이 칩 사이 제어 신호를 맞추는 방법도 제시했다. 0.18 μm BCD 공정으로 만든 칩으로 실제 바람 TENG 실험에서 칩 두 개로 130 V, 세 개로 195 V의 추출 전압을 보였다. 칩 두 개 구성에서 TENG 면적당 모은 전력은 96.4 μW/cm²로 이전 최신 TENG 하베스팅 칩보다 4배 높았고, 정류한 입력을 배터리 전압 출력으로 바꾸는 효율은 최고 70.7%였다.[^p8] | 1저자 J. Lee, 마지막·교신 저자 김현식 (6명) |

## 교수와 전문 분야

김현식 교수는 KAIST 전기및전자공학부 부교수이고 Circuit 디비전에 속하며, 전기및전자공학부 교수 소개는 직위 옆에 「디비젼 체어」를 적는다.[^eeprof] 반도체시스템공학과 교수진에도 연구분야 「반도체 시스템 및 집적회로」, 연구실 「회로설계 연구실」로 올라 있다.[^ssep] 전기및전자공학부 교수 소개의 주요 연구분야는 Robotics & Control, Integrated Circuits & Semiconductor Systems, Display Sciences & Engineering, Biomedical Engineering이다.[^eeprof]

연구실 Professor 페이지에 따르면 교수는 한양대학교에서 전자공학 학사(2005–2009, Campus Valedictorian으로 졸업)를, KAIST에서 전기공학 석사(2009–2011)와 박사(2011–2014)를 받았고, 석·박사 지도교수는 Gyu-Hyeong Cho였다.[^prof] 삼성디스플레이에서 Senior Researcher(2014-03–2015-08, OLED TV 개발·OLED 모듈·LCD 수율 개선)로 일한 뒤, 단국대학교 디스플레이공학과 조교수(2015-09–2019-02)를 거쳐 2019년 3월 KAIST 전기및전자공학부 조교수로 부임했고 2022년 3월 부교수가 됐다.[^prof] 연구 관심사는 CMOS 아날로그 집적회로 설계, 화면 불균일을 능동 보정하는 LCD·OLED 디스플레이 구동 IC, 전력 관리 IC(LDO 레귤레이터, 스위칭 DC-DC 변환기, 에너지 하베스팅 인터페이스), 저잡음·고신호대잡음비 CMOS 판독 IC, 의료용(X선·CT) CMOS 이미지 센서와 광자 계수 검출기, 유리·플라스틱 기판 위 다결정·비정질 실리콘 TFT로 만든 대면적 전자 소자다.[^prof]

교수는 IEEE Senior Member(Solid-State Circuits Society)이고, IEEE Solid-State Circuits Society Distinguished Lecturer(2024–2026)로 활동한다.[^prof] IEEE Solid-State Circuits Letters의 ISSCC 2024 특집호와 IEEE Open Journal of the Solid-State Circuits Society의 PMIC 특집호 객원 편집자, IEEE Journal of Emerging and Selected Topics in Power Electronics 객원 부편집자를 맡았다. 2025년 International Workshop on Power Supply on Chip(PwrSoC) 프로그램 위원장과 2021–2025년 CICC 기술 프로그램 위원(2024년 전력 관리 분과 공동 위원장, 2025년 위원장)을 지냈고, 2023년부터 ISSCC 국제 기술 프로그램 위원, 2017년부터 A-SSCC 기술 프로그램 위원을 맡고 있다.[^prof] 2026년 2월 ISSCC에서 에너지 효율이 높은 LDO 레귤레이터 설계 기초를 주제로 튜토리얼 강연을 했다.[^prof][^home]

KAIST 부임 뒤 받은 상으로 Professor 페이지는 Samsung Electronics' Best Patent Award(삼성전자 Device Solution, 2024년 8월), KAIST 공과대학 Technology Innovation Award(2022년 12월), 전기및전자공학부 Best Teaching Award(EE571, 2022년 10월; EE403, 2024년 4월), IC Design Education Center의 IDEC Best Lecture Award(2021년 6월)를 적는다.[^prof] 그보다 앞서 단국대학교 Best Teaching Award(2017년 2월)를 받았고, 박사과정 시절에는 IEEE Solid-State Circuits Society Predoctoral Achievement Award(2013–2014), IEEE SSCS 서울 챕터의 IEEE Journal of Solid-State Circuits Best Student Paper Award(2014년 5월), 삼성휴먼테크 논문대상 Gold Medal(제19회, 2013년 2월; 제18회, 2012년 2월)과 Bronze Medal(제17회, 2011년 2월)을 받았다.[^prof] 전기및전자공학부 교수 소개가 대표 업적으로 드는 다섯 편은 2011–2018년 학술지 논문(AMOLED 구동 칩, 정전식 멀티터치 감지, 모바일 LCD 열 구동 칩, X선 광자 계수 검출기, AMOLED용 DAC)으로, KAIST 부임 전 시기의 연구다.[^eeprof]

논문으로 보면 KAIST에서의 전문 분야는 네 갈래다. 모바일 OLED 화면의 구동 칩(대표 논문 1, 2),[^p1][^p2] 하이브리드 DC-DC 변환기(대표 논문 3, 4),[^p3][^p4] 칩 안 전압 레귤레이터와 LDO(대표 논문 5, 6, 7),[^p5][^p6][^p7] 에너지 하베스팅 칩(대표 논문 8)이다.[^p8]

## 응용 분야

대표 논문들은 모바일 OLED 화면의 소스 드라이버(대표 논문 1)와 화면이 동작하는 동안 화소 전류를 재는 OLED 구동 칩(대표 논문 2)을 다룬다.[^p1][^p2] 전원 쪽에서는 배터리 전압을 3.4 V로 바꾸는 변환기(대표 논문 3), 모바일 응용 프로세서용 강압 변환기(대표 논문 4), 디지털 SoC의 칩 안 전력 공급을 겨냥한 분산 LDO(대표 논문 7)를 내놓았다.[^p3][^p4][^p7] 대표 논문 8은 실제 바람으로 움직이는 마찰전기 나노발전기로 하베스팅 칩을 시험했다.[^p8] Research 페이지는 이 밖에 배터리 관리·충전 IC, 영상용 배열 판독 IC와 저선량 X선 검출기 판독 IC, 터치 감지 화면을 연구 항목으로 든다.[^research]

## 구성원

연구실 누리집 Students 페이지의 박사과정 9명, 석사과정 7명, 석박사통합과정 1명이다.[^students] 과정과 연구 주제는 페이지 표기이고, 박사과정 한 명은 학생 대표(랩장)로 적혀 있다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| SeungHwa Shin | 박사과정 | Display Driver IC & LDO | 1, 2 |
| JunSang Yoo | 박사과정 | Power Management IC |  |
| Suyun Chae | 박사과정 | High-Speed Amplifier |  |
| Jaewoo Song | 박사과정 | Integrated VR for SoCs |  |
| Hyeong-Joon Kim | 박사과정 | Display Driver IC |  |
| Kihyun Kim | 박사과정 | Mixed-Signal & Micro-Display | 2 |
| Jun-Gi Lee | 박사과정 (Student Representative, 랩장) | Analog LDO & Integrated VR | 4, 6, 7 |
| Yongha Lee | 박사과정 | Power Management IC |  |
| Hyunwook Choi | 박사과정 | Power Management IC |  |
| Taewoong Kim | 석사과정 | Power Management IC |  |
| Jeongdu Yoo | 석사과정 | Power Management IC |  |
| Junghyun Park | 석박사통합과정 | Power Management IC |  |
| Jehyung Lee | 석사과정 | Display Driver IC |  |
| Hamin Jeong | 석사과정 | Power Management IC |  |
| Jeeyeon Eom | 석사과정 | Display Driver IC |  |
| Taehyeon Jung | 석사과정 | Display Driver & Mixed-Signal |  |
| Gwanwoo Kim | 석사과정 | Display Driver IC |  |

## 졸업생과 이전 구성원

누리집 Alumni 페이지의 박사 17명과 석사 13명이다. 학위 연도와 학위 논문 제목, 진로는 누리집 표기이고, 학위 칸의 괄호(in DKU, co-advised with Prof. Cho)도 누리집이 적은 그대로다. 교수는 KAIST 부임 전 단국대학교(Dankook University) 디스플레이공학과 조교수였다.[^alumni][^prof]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Yousung Park | Ph.D. (2026/08) | SK Hynix | Advanced Circuit Techniques for High Frame-Rate & High Uniformity Displays |
| Sueon Park | Ph.D. (2026/08) | ETRI | Single-Mode DC-DC Converter for Positive/Negative Supply Rails of OLEDs |
| Heejun Lee | Ph.D. (2026/08) | KERI | Multi-Input Single-Output Power Combine-and-Regulate Hybrid Converter |
| Jae-Hyun Kim | Ph.D. (2025/08) | SK Hynix | Multilevel Designs of Hybrid DC-DC Converters |
| Gyu-Wan Lim | Ph.D. (2025/02) | SK Hynix | Driver and Readout Circuits for OLED Displays |
| Jiho Lee | Ph.D. (2025/02) | MX Division, Samsung Electronics | Kinetic Energy-Harvesting Power Management Circuits |
| Yongjin Lee | Ph.D. (2025/02) | System LSI, Samsung Electronics | Distributed Digital LDOs and On-Chip Power Delivery |
| Dae-Hyun Kim | Ph.D. (2024/08) | SK Hynix | Hybrid DC-DC Converters Seamlessly Covering Various VCRs |
| Woojin Jang | Ph.D. (2024/08) | System LSI, Samsung Electronics | Design of SC Circuits for High Accuracy Data Converters |
| Jeong-Hyun Cho | Ph.D. (2024/02) | System LSI, Samsung Electronics | Multi-Phase Fully Integrated Voltage Regulator (FIVR) |
| Hyunki Han | Ph.D. (2024/02) | System LSI, Samsung Electronics | 48V-to-1V Point-of-Load Converter and Hybrid Converter Design Methodology |
| Hong-Hyun Bae | Ph.D. (2024/02) | Memory Division, Samsung Electronics | Fast-DVS-Enabled Power Management Unit (PMU) for Energy-Efficient SoCs |
| Gyeong-Gu Kang | Ph.D. (2023/08) | MPS (Monolithic Power Systems, USA) | Area- and Power-Efficient Mobile Display Driver |
| Seok-Tae Koh | Ph.D. (2022/02) | Chungbuk National University (Assistant Professor) | Energy-Efficient Ultra-Fast Analog Amplifier |
| Min-Woo Ko | Ph.D. (2022/02) | Apple (USA) | Switched-Capacitor-Hybrid Power Converters |
| Ji-Hun Lee | Ph.D. (co-advised with Prof. Cho) (2021/02) | System LSI, Samsung Electronics | High-Fidelity Energy-Efficient Audio Amplifiers |
| Dong-Kyu Kim | Ph.D. (in DKU) (2021/02) | Samsung Display | Low-Noise Analog Front-End (AFE) and LDO for Imaging Sensors |
| Shieun Chung | M.S. (2026/08) | SK Hynix | Dual-CF-based Inverting Buck-Boost Converter for Negative Supply |
| Sungyeon Jang | M.S. (2025/08) | SK Hynix | Design Methodology of Optimized Hybrid DC-DC Converter Topology |
| Soo-Im Kang | M.S. (2025/02) | MX Division, Samsung Electronics | Energy-Efficient LDO Regulator |
| Minsik Choi | M.S. (2024/02) | Anapass, Inc. | 24V-to-1V Always-Quad-Path Point-of-Load (PoL) Converter |
| Doyoung Kwon | M.S. (2023/08) | SK Hynix | Multi-Path Boost Converter for OLED Displays |
| Ji-Heon Lee | M.S. (2022/08) | SK Hynix | GHz-PSR LDO Regulator |
| Chan-Hyu Jeon | M.S. (2022/02) | Synopsys | Hysteretic 3-Level Buck Converter for Battery-Charger IC |
| Tae-Gyun Song | M.S. (in DKU) (2020/02) | System LSI, Samsung Electronics | User-Recognizable Touch Readout IC |
| Younghwan Choo | M.S. (co-advised with Prof. Cho) (2020/02) | Broadcom | Wide-BW Hybrid DC-DC Converter for Digital RF PAs |
| Jae-Young Ko | M.S. (co-advised with Prof. Cho) (2020/02) | Ph.D. student in UCSD | Power-Efficient Multi-Path Hybrid Buck Converter |
| Uh-Ho Shin | M.S. (in DKU) (2019/02) |  | Electrical Inspection Circuit for AM-TFT Panel Manufacturing Process |
| Woonsung Kang | M.S. (in DKU) (2019/02) | Wellang Co., Ltd. | Single-Transformer Dual-Output Step-Up DC-DC Converter |
| Sun-Kyu Lee | M.S. (in DKU) (2018/02) | STI Co., Ltd. | Driving Circuit and System for BLDC Motor Position Control |

## 최근 논문 목록 (2021–2026)

누리집 Journals·Conferences 목록의 2021–2026년 논문 64편이다. 학술지 25편(IEEE Solid-State Circuits Magazine 해설 글 2편 포함)과 학회 논문 39편이며, 연도마다 학술지 논문을 먼저 적었다. 저자 순서와 제목·학술지·학회 표기는 누리집 그대로이고, *는 누리집이 교신저자로 적은 표시다. 2026년 구역의 IEEE Journal of Solid-State Circuits 논문 두 편은 논문 목록에 발표 연월 없이 게재 승인(accepted for publication)으로만 적혀 있어, 첫 화면의 2026년 7월·9월 승인 소식을 기준으로 2026년 구역에 두었다. 교수가 교신저자가 아닌 공동연구 논문도 누리집 목록대로 실었다.[^pubs][^home]

**2026**

- Kihyun Kim, Jun-Gi Lee, and Hyun-Sik Kim\*. "A 4042-PPI 10-bit Shared Memory-in-Pixel Digital-PWM CMOS Backplane with On-Chip BIST for 240-Hz Micro-LED-on-Silicon Displays". *IEEE Journal of Solid-State Circuits (JSSC), accepted for publication, doi: 10.1109/JSSC.2026.3736101*.
- Jae-Hyun Kim, Jun-Gi Lee, Hyunki Han, and Hyun-Sik Kim\*. "A Three-Level Dual-Path Hybrid Buck Converter With Mitigated Capacitive Current and Seamless DVS Across a Wide Output Voltage Range". *IEEE Journal of Solid-State Circuits (JSSC), accepted for publication, doi: 10.1109/JSSC.2026.3710310*.
- Hyun-Sik Kim\*. "Fundamentals of Energy-Efficient LDO Regulator Design: from dropout optimization to wide-bandwidth and high-PSR techniques". *IEEE Solid-State Circuits Magazine (SSC-M), vol. 18, no. 3, pp. 55-72, Summer 2026*.
- Yong-Jin Lee, Jun-Gi Lee, and Hyun-Sik Kim\*. "A Fully Synthesizable, Fine-Grained Distributed Digital-LDO Fabric Featuring Freely Linkable Current-Sharing Network for Scalable On-Chip Power Delivery". *IEEE Journal of Solid-State Circuits (JSSC), vol. 61, no. 7, pp. 3688-3703, July 2026*.
- Sungyeon Jang, Jae-Hyun Kim, Heejun Lee, and Hyun-Sik Kim\*. "A 92.3%-Efficiency 12V-to-1V HOT-12 Converter: Reframing Hybrid Design via the Dual-Output SC-Driven Parameterized HOT-X Framework". *IEEE European Solid-State Electronics Research Conference (ESSERC), pp. 886-889, Sept. 2026*.
- Sungyeon Jang, Jae-Hyun Kim, Hyunwook Choi, Kyung-Hwan Lee, Se-Won Wang, Hangseok Choi, and Hyun-Sik Kim\*. "A 5V–21V Input, 42W, 95.7%-Efficient Full-Range Extended DSD (e-DSD) Converter for Fast-Charging Battery Chargers". *IEEE European Solid-State Electronics Research Conference (ESSERC), pp. 113-116, Sept. 2026*.
- Suyun Chae, Taeksu Kwon, Yousung Park, Insuk Kim, Yeongmin Kim, Siwoo Kim, and Hyun-Sik Kim\*. "A 3200×2880, 120Hz OLED Display Driver IC with Miller-Charge Cancellation (MCC) Achieving a 13.3V/μs Slew Rate under Worst-Case Full-Channel Load". *IEEE Symposium on VLSI Technology & Circuits (VLSI-C), June 2026*.
- Yousung Park, Hyeong-Joon Kim, Suyun Chae, Jeeyeon Eom, and Hyun-Sik Kim\*. "A 10-Bit Source-Driver IC with Mismatch-Resilient Cross-Point DAC Achieving 1223μm2/Channel and 4.3mV DVO for Mobile OLED Displays". *IEEE Symposium on VLSI Technology & Circuits (VLSI-C), June 2026*.
- Sueon Park, Jun-Gi Lee, Jae-Hyun Kim, Dong-Kyu Kim, Sung-Chun Park, Yongjae Lee, and Hyun-Sik Kim\*. "A 97.1%-Efficient Single-Mode Fine-Multilevel Buck-Boost (SMFL-BB) Converter Achieving Sub-8mV Ripple with a 1mm3-Volume Inductor for Flicker-Free Mobile OLED Displays". *IEEE Custom Integrated Circuits Conference (CICC), April 2026*.
- Kihyun Kim, Jun-Gi Lee, and Hyun-Sik Kim\*. "A 4042-PPI 10b 240Hz Digital-PWM CMOS Backplane for Micro-LED-on-Silicon Displays with a Shared, Unified Memory-in-Pixel Architecture". *IEEE International Solid-State Circuits Conference (ISSCC), pp. 412-413, Feb. 2026*.
- Yousung Park, Gyu-Wan Lim, and Hyun-Sik Kim\*. "A 512ch 10b Source-Driver IC with Current-Mode Auto-Zeroing Scheme Achieving 1.4mV DVO and 600ns 1-Horizontal Time for Mobile OLED Displays". *IEEE International Solid-State Circuits Conference (ISSCC), pp. 416-417, Feb. 2026*.
- Hyeong-Joon Kim, Yousung Park, Kihyun Kim, Seunghwa Shin, and Hyun-Sik Kim\*. "A 10b Display Driver IC with a Pivoting Translinear-Loop DAC-in-Buffer Enabling 1μs 1-H Scan Time and 1722μm2 per Channel". *IEEE International Solid-State Circuits Conference (ISSCC), pp. 418-419, Feb. 2026*.

**2025**

- Gyu-Wan Lim, Dong-Kyu Kim, Gyeong-Gu Kang, Seunghwa Shin, Kihyun Kim, Yousung Park, Won Kim, Young-Bok Kim, Hyun-Kyu Jeon, and Hyun-Sik Kim\*. "A Column-Parallel On-Programming Pixel Current Readout Embedded in an OLED Display Driver IC". *IEEE Journal of Solid-State Circuits (JSSC), vol. 60, no. 4, pp. 1174-1189, April 2025*.
- Jae-Hyun Kim, Yousung Park, Doyoung Kwon, Dae-Hyeon Kim, Dong-Kyu Kim, Sung-Chun Park, Yongjae Lee, Jung-Bong Lee, and Hyun-Sik Kim\*. "A Single-Duty-Cycled Buck-Boost Converter Achieving Low Output Ripple and Seamless Mode Transition". *IEEE Journal of Solid-State Circuits (JSSC), vol. 60, no. 4, pp. 1248-1264, April 2025*.
- Jae-Hyun Kim, Se-Hong Park, Jiho Lee, Jeong-Hyun Cho, Gyu-Hyeong Cho, and Hyun-Sik Kim\*. "A Floating Voltage Source-Based Turn-Off Snubber for a Nonisolated Multilevel SiC DC-DC Converter". *IEEE Transactions on Industrial Electronics (TIE), vol. 72, no. 1, pp. 390-400, Jan. 2025*.
- Yeon-Woo Jeong, Seung-Ju Lee, Jong-Hun Kim, Mun-Jung Cho, Min-Sik Kim, Myeong-Ho Kim, Hyun-Sik Kim, and Se-Un Shin\*. "A Fast Start-Up Dual Energy Harvesting IC with Battery-Independent Synchronous Accumulated Electric Charge Extraction (SAECE) Achieving 660% FoMavg for Piezoelectric Energy Harvesting". *IEEE Asian Solid-State Circuits (A-SSCC), Nov. 2025*.
- Jeong-Hyun Cho and Hyun-Sik Kim\*. "A Boosted 3.5W, -81.6dB THD+N, 92.6% Total Efficiency, Battery-Powered Class-D Audio Amplifier with True-Zero-Switching Achieving Quiescent Current of 0.9mA". *IEEE Symposium on VLSI Technology & Circuits (VLSI-C), June 2025*.
- Heejun Lee, Junsang Yoo, Jiho Lee, Kyoungho Lee, Wonseob Lim, Sang-Hwa Yi, and Hyun-Sik Kim\*. "A Multi-Rectenna, Single-Output, Power Combine-and-Regulate Boost Converter for 5.8GHz Wireless Power Receiver Achieving 3.1W over 50m-Distance". *IEEE Symposium on VLSI Technology & Circuits (VLSI-C), June 2025*.
- Jae-Hyun Kim, Jun-Gi Lee, Hyunki Han, and Hyun-Sik Kim\*. "A 1.8V Input, 96.5% Efficiency, 4.05A/mm2 FoM, Three-Level Dual-Path Hybrid Buck Converter with Mitigated Capacitive Inrush Current and Seamless DVS Across a Wide 0.4-to-1.5V Output Range". *IEEE Custom Integrated Circuits Conference (CICC), April 2025*.
- Gyeong-Gu Kang, Minjie Chen, and Hyun-Sik Kim\*. "A 5V-Input, 12.5-to-45V-Output Reconfigurable Hybrid Boost Converter with an SC-Based Parallel Auxiliary Cell Achieving 96.8% Peak Efficiency". *IEEE Custom Integrated Circuits Conference (CICC), April 2025*.
- Jiho Lee and Hyun-Sik Kim\*. "A Biased-SECE Interface for Piezoelectric Energy Harvesting with Geometric-Mean-Computational MPPT Achieving 99.9% MPPT Efficiency, 8.75 Cycles/ΔVOC Tracking, and 9.3x Energy Extraction". *IEEE International Solid-State Circuits Conference (ISSCC), pp. 520-521, Feb. 2025*.

**2024**

- Dae-Hyeon Kim and Hyun-Sik Kim\*. "A Power-Efficient Single-Mode Buck-Boost DC-DC Converter with Bilaterally Symmetrical Hybrid Topology". *IEEE Journal of Solid-State Circuits (JSSC), vol. 59, no. 12, pp. 4137-4149, Dec. 2024*.
- Jun-Gi Lee and Hyun-Sik Kim\*. "A Fully Integrated, Domino-Like-Buffered LDO Regulator With High Power-Supply Rejection Across the Full Frequency Spectrum". *IEEE Journal of Solid-State Circuits (JSSC), vol. 59, no. 12, pp. 4088-4100, Dec. 2024*.
- Yousung Park, Gyeong-Gu Kang, Gyu-Wan Lim, Seunghwa Shin, Yong-Sung Ahn, Wonyoun Kim, and Hyun-Sik Kim\*. "A 10-Bit Source-Driver IC With Charge-Modulation DAC for Enhanced Frame-Rate Mobile OLED Displays". *IEEE Journal of Solid-State Circuits (JSSC), vol. 59, no. 11, pp. 3511-3524, Nov. 2024*.
- Jeong-Hyun Cho, Hong-Hyun Bae, Gyu-Wan Lim, Tae-Hwang Kong, Jun-Hyeok Yang, and Hyun-Sik Kim\*. "A Fully Integrated Multi-Phase Voltage Regulator with Flying-Capacitor-Based Inter-Inductor Current Self-Balancing Scheme and Charge-Recycling Gate Driver". *IEEE Journal of Solid-State Circuits (JSSC), vol. 59, no. 8, pp. 2529-2544, Aug. 2024*.
- Seunghwa Shin, Gyeong-Gu Kang, Gyu-Wan Lim, and Hyun-Sik Kim\*. "A Display Source-Driver IC Featuring Multistage-Cascaded 10-Bit DAC and True-DC-Interpolative Super-OTA Buffer". *IEEE Journal of Solid-State Circuits (JSSC), vol. 59, no. 4, pp. 1050-1066, April 2024*.
- Dae-Hyeon Kim, Jeong-Hyun Cho, Hyunki Han, and Hyun-Sik Kim\*. "A 1.8V-Input 0.2-to-1.5V-Output 2.5A 930mA/mm3 Always-Balanced Dual-Path Hybrid Buck Converter with Seamlessly All-VCR-Coverable Tri-Mode Operation". *IEEE Symposium on VLSI Technology & Circuits (VLSI-C), June 2024*.
- Jae-Hyun Kim, Yousung Park, Doyoung Kwon, Dong-Kyu Kim, Sung-Chun Park, Yongjae Lee, Jung-Bong Lee, and Hyun-Sik Kim\*. "A 96.4%-Efficiency Single-Duty-Cycled Buck-Boost Converter Achieving 1.9mV Ripple and 2.1mV Mode-Change Fluctuation for Mobile OLED Displays". *IEEE Symposium on VLSI Technology & Circuits (VLSI-C), June 2024*.
- Gyu-Wan Lim, Gyeong-Gu Kang, Seunghwa Shin, Kihyun Kim, Yousung Park, Won Kim, Young-Bok Kim, Hyun-Kyu Jeon, and Hyun-Sik Kim\*. "An OLED Display Driver IC Embedding -63dB CMR, 80mV/nA Sensitivity, 390pA Detectable, and Column-Parallel Pixel Current Readout for Real-Time Non-Uniformity Compensation". *IEEE Symposium on VLSI Technology & Circuits (VLSI-C), June 2024*.
- Hong-Hyun Bae, Jeong-Hyun Cho, Kihyun Kim, Seunghwa Shin, Doojin Jang, Jun-Hyeok Yang, and Hyun-Sik Kim\*. "A 7V/μs-DVS Class-G Digital-Shunt-Aided Buck Voltage Regulator Achieving a 7% Dynamic-Efficiency Drop at a 600kHz DVS Occurrence Frequency in 28nm CMOS". *IEEE Custom Integrated Circuits Conference (CICC), April 2024*.
- Dae-Hyeon Kim and Hyun-Sik Kim\*. "A 96.9%-Peak-Efficiency Bilaterally-Symmetrical Hybrid Buck-Boost Converter Featuring Seamless Single-Mode Operation, Always-Reduced Inductor Current, and the Use of All CMOS Switches". *IEEE International Solid-State Circuits Conference (ISSCC), pp. 146-147, Feb. 2024*.
- Yong-Jin Lee, Woojin Jang, Hong-Hyun Bae, Jeong-Hyun Cho, and Hyun-Sik Kim\*. "34.7A/mm2 Scalable Distributed All-Digital 6×6 Dot-LDOs Featuring Freely Linkable Current-Sharing Network: A Fine-Grained On-Chip Power Delivery Solution in 28nm CMOS". *IEEE International Solid-State Circuits Conference (ISSCC), pp. 272-273, Feb. 2024*.
- Hyunki Han, Jeong-Hyun Cho, Woojin Jang, Yousung Park, Jiho Lee, and Hyun-Sik Kim\*. "A 94.1%-Efficiency Parallel-SC Hybrid Buck Converter Designed Using VCR-Aware Topology Optimizer for a 4.2A/mm2 Current-Density FoM". *IEEE International Solid-State Circuits Conference (ISSCC), pp. 464-465, Feb. 2024*.
- Jun-Gi Lee, Hong-Hyun Bae, Seunghyun Jang, and Hyun-Sik Kim\*. "A Fully Integrated, Domino-Like-Buffered Analog LDO Achieving -28dB Worst-Case Power-Supply Rejection across the Frequency Spectrum from 10Hz to 1GHz with 50pF On-Chip Capacitance". *IEEE International Solid-State Circuits Conference (ISSCC), pp. 456-457, Feb. 2024*.
- Yousung Park, Gyeong-Gu Kang, Gyu-Wan Lim, Seunghwa Shin, Yong-Sung Ahn, Wonyoun Kim, and Hyun-Sik Kim\*. "A 600ch 10b Source-Driver IC with a Charge-Modulation DAC Achieving 1-Horizontal Time of 1.5μs Suitable for 240Hz-Frame-Rate Mobile Displays". *IEEE International Solid-State Circuits Conference (ISSCC), pp. 432-433, Feb. 2024*.

**2023**

- Gyu-Wan Lim, Gyeong-Gu Kang, Hyunggun Ma, Moonjae Jeong, and Hyun-Sik Kim\*. "An Area-Efficient 10-Bit Source-Driver IC with LSB-Stacked LV-to-HV-Amplify DAC for Mobile OLED Displays". *IEEE Journal of Solid-State Circuits (JSSC), vol. 58, no. 11, pp. 3164-3178, Nov. 2023*.
- Heejun Lee, Hyunki Han, and Hyun-Sik Kim\*. "A 4-to-42 V Input 3.3 V Output Self-Biased DC-DC Buck Converter Featuring Leakage-Emulated Bootstrap Voltage Refresher and Anti-Deadlock". *IEEE Solid-State Circuits Letters (SSC-L), vol. 6, pp. 261-264, Oct. 2023*.
- Hyun-Sik Kim\*. "Exploring Ways to Minimize Dropout Voltage for Energy-Efficient Low-Dropout Regulators: Viable approaches that preserve performance". *IEEE Solid-State Circuits Magazine (SSC-M), vol. 15, no. 2, pp. 59-68, Spring 2023*.
- Min-Woo Ko, Hyunki Han, and Hyun-Sik Kim\*. "A Bipolar-Output Switched-Capacitor DC-DC Boost Converter with Residual-Energy-Recycling Regulation and Low Dropout Post-Filtering Techniques". *IEEE Journal of Solid-State Circuits (JSSC), vol. 58, no. 5, pp. 1400-1413, May 2023*.
- Seunghwa Shin, Gyeong-Gu Kang, Gyu-Wan Lim, and Hyun-Sik Kim\*. "A Mobile OLED Source-Driver IC featuring Ultra-Compact 3-Stage-Cascaded 10-Bit DAC and 42V/μs-Slew-Rate True-DC-Interpolative Super-OTA Buffer". *IEEE Symposium on VLSI Technology & Circuits (VLSI-C), June 2023*.
- Heejun Lee, Hyunki Han, and Hyun-Sik Kim\*. "A 4-to-42V Input, 95.5% Efficiency, 3.2μA-IQ, DC-DC Buck Converter Featuring a Leakage-Emulated Bootstrap Refresher and Anti-Deadlock Self-Bias Supply for Battery-Powered Automotive Uses". *IEEE Custom Integrated Circuits Conference (CICC), April 2023*.

**2022**

- Gyeong-Gu Kang, Ji-Hun Lee, Se-Un Shin, Gyu-Hyeong Cho, and Hyun-Sik Kim\*. "A Boost-Oriented SIDO (BO-SIDO) Step-Up/Down DC-DC Converter Embedding Buck Conversion with an Energy-Balancing Capacitor". *IEEE Solid-State Circuits Letters (SSC-L), vol. 5, pp. 296-299, Dec. 2022*.
- Hong-Hyun Bae, Jeong-Hyun Cho, Gyeong-Gu Kang, Yousung Park, and Hyun-Sik Kim\*. "A Power-Efficient 1–2-MHz Hysteretic Buck Converter With High DVS Rate Enabled by Isosceles-Triangular Shunt Current Push–Pull Technique". *IEEE Solid-State Circuits Letters (SSC-L), vol. 5, pp. 280-283, Nov. 2022*.
- Jeong-Hyun Cho, Dong-Kyu Kim, Hong-Hyun Bae, Yong-Jin Lee, Seok-Tae Koh, Younghwan Choo, Ji-Seon Paek, and Hyun-Sik Kim\*. "A Fully Integrated Multi-Phase Buck Converter with On-Chip Capacitor Dynamic Re-Allocation and Fine-Grained Phase-Shedding Techniques". *IEEE Journal of Solid-State Circuits (JSSC), vol. 57, no. 12, pp. 3840-3852, Dec. 2022*.
- Jiho Lee, Sang-Han Lee, Gyeong-Gu Kang, Jae-Hyun Kim, Gyu-Hyeong Cho, and Hyun-Sik Kim\*. "A Triboelectric Energy-Harvesting Interface with Scalable Multi-Chip-Stacked Bias-Flip and Daisy-Chained Synchronous Signaling Techniques". *IEEE Journal of Solid-State Circuits (JSSC), vol. 57, no. 12, pp. 3825-3839, Dec. 2022*.
- Young-Seok Noh, Jeong-Il Seo, Hyun-Sik Kim, and Sang-Gug Lee\*. "A Reconfigurable DC-DC Converter for Maximum Thermoelectric Energy Harvesting in a Battery-Powered Duty-Cycling Wireless Sensor Node". *IEEE Journal of Solid-State Circuits (JSSC), vol. 57, no. 9, pp. 2719-2730, Sept. 2022*.
- Woojin Jang, Gyeong-Gu Kang, Yong Lim, and Hyun-Sik Kim\*. "A Pipeline ADC with Negative C-assisted SC Amplifier Canceling Gain Error and Nonlinearity". *IEEE European Solid-State Circuits Conference (ESSCIRC), pp. 317-320, Sept. 2022*.
- Hyunki Han, Min-Woo Ko, Jeong-Hyun Cho, Gyeong-Gu Kang, Seok-Tae Koh, Hong-Hyun Bae, and Hyun-Sik Kim\*. "A Monolithic 48V-to-1V 10A Quadruple Step-Down DC-DC Converter with Hysteretic Copied On-Time 4-Phase Control and 2× Slew Rate All-Hysteretic Mode". *IEEE Symposium on VLSI Technology & Circuits (VLSI-C), pp. 182-183, June 2022*.
- Hong-Hyun Bae, Jeong-Hyun Cho, Gyeong-Gu Kang, Yousung Park, and Hyun-Sik Kim\*. "A 97.6%-Efficient 1-2MHz Hysteretic Buck Converter with 7V/μs DVS-Rate Enabled by Isosceles-Triangular Shunt Current Push-Pull Technique". *IEEE Symposium on VLSI Technology & Circuits (VLSI-C), pp. 194-195, June 2022*.
- Jeong-Hyun Cho, Hong-Hyun Bae, Gyu-Wan Lim, Tae-Hwang Kong, Jun-Hyeok Yang, and Hyun-Sik Kim\*. "A Fully-Integrated 0.9W/mm2 79.1%-Efficiency 200MHz Multi-Phase Buck Converter with Flying-Capacitor-Based Inter-Inductor Current Balancing Technique". *IEEE Symposium on VLSI Technology & Circuits (VLSI-C), pp. 196-197, June 2022*.
- Gyeong-Gu Kang, Ji-Hun Lee, Se-Un Shin, Gyu-Hyeong Cho, and Hyun-Sik Kim\*. "A 5.6W-Power 96.6%-Efficiency Boost-Oriented SIDO Step-Up/Down DC-DC Converter Embedding Buck Conversion with an Energy-Balancing Capacitor". *IEEE Symposium on VLSI Technology & Circuits (VLSI-C), pp. 180-181, June 2022*.
- Jeong-Hyun Cho, Dong-Kyu Kim, Hong-Hyun Bae, Yong-Jin Lee, Seok-Tae Koh, Younghwan Choo, Ji-Seon Paek, and Hyun-Sik Kim\*. "A 1.23W/mm2 83.7%-Efficiency 400MHz 6-Phase Fully-Integrated Buck Converter in 28nm CMOS with On-Chip Capacitor Dynamic Re-Allocation for Inter-Inductor Current Balancing and Fast DVS of 75mV/ns". *IEEE International Solid-State Circuits Conference (ISSCC), pp. 298-299, Feb. 2022*.
- Gyu-Wan Lim, Gyeong-Gu Kang, Hyunggun Ma, Moonjae Jeong, and Hyun-Sik Kim\*. "A 10b Source-Driver IC with LSB-Stacked LV-to-HV-Amplify DAC Achieving 2688μm2/channel and 4.8mV DVO for Mobile OLED Displays". *IEEE International Solid-State Circuits Conference (ISSCC), pp. 110-111, Feb. 2022*.
- Jiho Lee, Sang-Han Lee, Gyeong-Gu Kang, Jae-Hyun Kim, Gyu-Hyeong Cho, and Hyun-Sik Kim\*. "A 130V Triboelectric Energy-Harvesting Interface in 180nm BCD with Scalable Multi-Chip-Stacked Bias-Flip and Daisy-Chained Synchronous Signaling Technique". *IEEE International Solid-State Circuits Conference (ISSCC), pp. 474-475, Feb. 2022*.

**2021**

- Seok-Tae Koh, Ji-Hun Lee, Gyeong-Gu Kang, Hyunki Han, and Hyun-Sik Kim\*. "A 5-V Dynamic Class-C Paralleled Single-Stage Amplifier with Near-Zero Dead-Zone Control and Current-Redistributive Rail-to-Rail Gm-Boosting Technique". *IEEE Journal of Solid-State Circuits (JSSC), vol. 56, no. 12, pp. 3593-3607, Dec. 2021*.
- Tae-Gyun Song, Dong-Kyu Kim, Jeong-Hyun Cho, Ji-Hun Lee, and Hyun-Sik Kim\*. "A 50.7-dB-DR Finger-Resistance Extracting Multi-Touch Sensor IC for Soft Classification of Fingers Contacted on 6.7-inch Capacitive Touch Screen Panel". *IEEE Journal of Solid-State Circuits (JSSC), vol. 56, no. 11, pp. 3470-3485, Nov. 2021*.
- Ji-Hun Lee and Hyun-Sik Kim\*. "An Energy-Efficient 2×VBAT-Swing Switched-Mode Audio Amplifier with Fully-Differential Single-Inductor Linear Buck-Boost Power Topology". *IEEE Solid-State Circuits Letters (SSC-L), vol. 4, pp. 186-189, Oct. 2021*.
- Kye-Seok Yoon, Seungchul Jung, Ji-Hun Lee, Sang Joon Kim, Hyun-Sik Kim\*, and Gyu-Hyeong Cho. "A Single-Inductor Multiple-Output (SIMO) 0.8-V/1.8-V/12-V Step-Up/Down Converter with Low Quiescent Current for Implantable Electroceutical SoCs". *IEEE Solid-State Circuits Letters (SSC-L), vol. 4, pp. 182-185, Oct. 2021*.
- Gyeong-Gu Kang, Seok-Tae Koh, Woojin Jang, Jiho Lee, Seongjoo Lee, Ohjo Kwon, Keumdong Jung, and Hyun-Sik Kim\*. "A 12-Bit Mobile OLED/μLED Display Driver IC with Cascaded Loading-Free Capacitive Interpolation DAC and 6.24V/μs-Slew-Rate Buffer Amplifier". *IEEE Symposium on VLSI Circuits (VLSI-C), June 2021*.
- Ji-Hun Lee and Hyun-Sik Kim\*. "An 8Ω, 5.5W, 0.006% THD+N, 2×VBAT-Swing Switched-Mode Audio Amplifier with Fully-Differential Linear Buck-Boost Topology Achieving Total Efficiency of 87%". *IEEE Symposium on VLSI Circuits (VLSI-C), June 2021*.
- Jae-Young Ko, Yeunhee Huh, Min-Woo Ko, Gyeong-Gu Kang, Gyu-Hyeong Cho, and Hyun-Sik Kim\*. "A 4.5V-Input 0.3-to-1.7V-Output Step-Down Always-Dual-Path DC-DC Converter Achieving 91.5%-Efficiency with 250mΩ-DCR Inductor for Low-Voltage SoCs". *IEEE Symposium on VLSI Circuits (VLSI-C), June 2021*.
- Seok-Tae Koh, Ji-Hun Lee, Gyeong-Gu Kang, Hyunki Han, and Hyun-Sik Kim\*. "A 5V Dynamic Class-C Paralleled Single-Stage Amplifier with Near-Zero Dead-Zone Control and Current-Redistributive Rail-to-Rail Gm-Boosting Technique". *IEEE International Solid-State Circuits Conference (ISSCC), pp. 86-87, Feb. 2021*.
- Min-Woo Ko, Hyunki Han, and Hyun-Sik Kim\*. "A 90.5%-Efficiency 28.7μVRMS-Noise Bipolar-Output High Step-Up SC DC-DC Converter with Energy-Recycled Regulation and Post-Filtering for ±15V TFT-Based LAE Sensors". *IEEE International Solid-State Circuits Conference (ISSCC), pp. 270-271, Feb. 2021*.
- Young-Seok Noh, Jeong-Il Seo, Won-Jong Choi, Ji-Hwan Kim, Hoang Van Phuoc, Hyun-Sik Kim, and Sang-Gug Lee\*. "A Reconfigurable DC-DC Converter for Maximum TEG Energy Harvesting in a Battery-Powered Wireless Sensor Node". *IEEE International Solid-State Circuits Conference (ISSCC), pp. 266-267, Feb. 2021*.

## 수상

누리집 Awards 페이지에 오른 구성원 학생의 수상 가운데 2021년 10월 이후 13건이다. 날짜는 페이지가 적은 달이고, 상 이름과 수상자 표기는 페이지의 제목 줄과 국문 이름 줄 그대로다.[^awards] 교수의 수상은 「교수와 전문 분야」에 있다.

- Feb. 2026 · 제32회 삼성휴먼테크 논문대상 - 회로설계부문 금상 (박사과정 박유성)
- Sept. 2025 · PwrSoC 2025 - Best Student Poster Award (3rd place) (박사과정 유준상)
- Oct. 2024 · 2024 삼성디스플레이 산학협력 기술논문대회 - 금상 (박사과정 김재현)
- Oct. 2024 · 제25회 대한민국 반도체설계대전 - 특허청장상 (박사과정 임규완)
- Feb. 2024 · 제30회 삼성휴먼테크 논문대상 - 회로설계부문 장려상 (박사과정 한현기)
- Oct. 2022 · 2022 삼성디스플레이 산학협력 기술논문대회 - 금상 (박사과정 강경구)
- Oct. 2022 · 2022 삼성디스플레이 산학협력 기술논문대회 - 은상 (박사과정 임규완)
- Oct. 2022 · 제23회 대한민국 반도체설계대전 - 국무총리상 (박사과정 임규완)
- July 2022 · IDEC Congress 2022 - Chip Design Contest (CDC) Best Design Award (DB Hitek 특별상) (박사과정 임규완)
- Feb. 2022 · 제28회 삼성휴먼테크 논문대상 - 회로설계부문 동상 (박사과정 조정현)
- Jan. 2022 · 제29회 한국반도체학술대회 Chip Design Contest (CDC) - IEEE-SSCS 서울챕터 특별상 (박사과정 배홍현)
- Nov. 2021 · 과학기술정보통신부 주최 ICT Colloquium 2021 학생 창의 자율 과제 - IITP 원장상 (박사과정 배홍현)
- Oct. 2021 · 2021 삼성디스플레이 산학협력 기술논문대회 - 금상 (박사과정 고석태)

## 소식

누리집 첫 화면 Latest News의 2021년 10월–2026년 9월 글 56건이다. 날짜는 게시된 연·월이고 문장은 게시된 그대로다.[^home]

- 2026/09 · Kihyun's work on Micro-LED-on-Silicon Backplane has been accepted to IEEE JSSC (special issue on ISSCC 2026)
- 2026/08 · Prof. Kim's tutorial article on LDO has been published in IEEE Solid-State Circuits Magazine
- 2026/07 · Jae-Hyun's work on Multi-Level Dual-Path Converter has been accepted to IEEE JSSC
- 2026/06 · Sungyeon's work on HOT-X Hybrid Converter Design Methodology has been accepted to ESSCERC 2026
- 2026/06 · Sungyeon's work on e-DSD Converter (Battery Charger) has been accepted to ESSCERC 2026
- 2026/03 · Suyun's work on Mobile Display Driver IC has been accepted to Symp. VLSI Circuits (VLSIC) 2026
- 2026/03 · Yousung's work on Mismatch-Resilient XP-DAC has been accepted to Symp. VLSI Circuits (VLSIC) 2026
- 2026/02 · Prof. Kim gave a Tutorial Lecture on Energy-Efficient LDO Regulator Designs in ISSCC 2026
- 2026/01 · Yousung won Gold Medal (1st place) of the 32nd Samsung Humantech Paper Award (삼성휴먼테크 금상 수상)
- 2026/01 · Sueon's work on Single-Mode Fine-Level Buck-Boost Converter has been accepted to CICC 2026
- 2025/12 · Yong-Jin's work on Digital Distributed LDO Fabric has been accepted to IEEE JSSC
- 2025/11 · Kihyun's work on CMOS micro-LED-on-Silicon Backplane has been accepted to ISSCC 2026
- 2025/11 · Yousung's work on Current-Mode Auto-Zeroing Technique has been accepted to ISSCC 2026
- 2025/11 · Hyeong-Joon's work on PTL-DAC-in-Buffer has been accepted to ISSCC 2026
- 2025/03 · Jeong-Hyun's work on Class-D Audio Amplifier has been accepted to Symp. VLSI Circuits (VLSIC) 2025
- 2025/03 · Heejun's work on PMIC for 5.8GHz Power Beaming Rx has been accepted to Symp. VLSI Circuits (VLSIC) 2025
- 2025/01 · Gyu-Wan's work on Display Readout & Driver IC has been accepted to IEEE JSSC (special issue on VLSIC 2024)
- 2025/01 · Jae-Hyun's work on Multi-Level Dual-Path Converter has been accepted to CICC 2025
- 2025/01 · Gyeong-Gu's work on Hybrid Boost Converter has been accepted to CICC 2025
- 2025/01 · Prof. Kim's invited talk at Circuit Insights 2024 has been publicized on YouTube
- 2024/12 · Jae-Hyun's work on Seamless Buck-Boost Converter has been accepted to IEEE JSSC (special issue on VLSIC 2024)
- 2024/10 · Jiho's work on Piezoelectric Energy-Harvesting IC has been accepted to ISSCC 2025
- 2024/08 · Dae-Hyeon's work on Hybrid Buck-Boost Converter has been accepted to IEEE JSSC (special issue on ISSCC 2024)
- 2024/08 · Jun-Gi's work on Domino LDO has been accepted to IEEE JSSC (special issue on ISSCC 2024)
- 2024/08 · Yousung's work on Display Driver IC has been accepted to IEEE JSSC (special issue on ISSCC 2024)
- 2024/06 · Jae-Hyun's work on Multilevel SiC DC-DC Converter has been accepted to IEEE T. Industrial Electronics
- 2024/04 · Dae-Hyeon's work on All-VCR-Coverable Hybrid Buck has been accepted to Symp. VLSI Circuits (VLSIC) 2024
- 2024/04 · Jae-Hyun's work on SDC Buck-Boost Converter has been accepted to Symp. VLSI Circuits (VLSIC) 2024
- 2024/04 · Gyu-Wan's work on Display Readout & Driver IC has been accepted to Symp. VLSI Circuits (VLSIC) 2024
- 2024/03 · Prof. Kim has been appointed as Distinguished Lecturer (DL) in IEEE Solid-State Circuits Society (SSCS)
- 2024/01 · Jeong-Hyun's work on Fully Integrated Voltage Regulator (FIVR) has been accepted to IEEE JSSC
- 2024/01 · Hong-Hyun's work on Hybrid Voltage Regulator has been accepted to CICC 2024
- 2024/01 · Seunghwa's work on Display Driver IC has been accepted to IEEE JSSC (special issue on VLSIC 2023)
- 2023/10 · Yong-Jin's work on Digital Distributed LDO has been accepted to ISSCC 2024
- 2023/10 · Hyunki's work on Hybrid Buck Converter has been accepted to ISSCC 2024
- 2023/10 · Dae-Hyeon's work on Hybrid Buck-Boost Converter has been accepted to ISSCC 2024
- 2023/10 · Yousung's work on Display Driver IC has been accepted to ISSCC 2024
- 2023/10 · Jun-Gi's work on High-PSR Analog LDO has been accepted to ISSCC 2024
- 2023/09 · Heejun's work on Automotive DC-DC has been accepted to IEEE SSC-L (special issue on CICC 2023)
- 2023/06 · Gyu-Wan's work on Display Driver IC has been accepted to IEEE JSSC
- 2023/06 · Prof. Kim's tutorial article on LDO has been published in IEEE Solid-State Circuits Magazine (SSC-M)
- 2023/03 · Seunghwa's work on Display Driver IC has been accepted to Symp. VLSI Circuits (VLSIC) 2023
- 2023/01 · Heejun's work on Automotive High-Voltage DC-DC has been accepted to CICC 2023
- 2022/12 · Gyeong-Gu's work on BO-SIDO Converter has been accepted to IEEE SSC-L (special issue on VLSIC 2022)
- 2022/11 · Honghyun's work on Fast-DVS Buck Converter has been accepted to IEEE SSC-L (special issue on VLSIC 2022)
- 2022/09 · Min-Woo's work on SC-LDO-Hybrid Low-Noise Boost Converter has been accepted to IEEE JSSC
- 2022/07 · Jeong-Hyun's work on Multi-Phase FIVR has been accepted to IEEE JSSC (special issue on ISSCC 2022)
- 2022/07 · Jiho's work on TENG Energy-Harvesting IC has been accepted to IEEE JSSC (special issue on ISSCC 2022)
- 2022/06 · Woojin's work on Pipelined ADC has been accepted to ESSCIRC 2022
- 2022/04 · Hyunki's work on 48-to-1V Point-of-Load Converter has been accepted to Symp. VLSI Circuits (VLSIC) 2022
- 2022/04 · Jeong-Hyun's work on Fully-Integrated Voltage Regulator has been accepted to Symp. VLSI Circuits (VLSIC) 2022
- 2022/04 · Honghyun's work on Fast-DVS Buck Converter has been accepted to Symp. VLSI Circuits (VLSIC) 2022
- 2022/04 · Gyeong-Gu's work on Boost-Oriented SIDO Converter has been accepted to Symp. VLSI Circuits (VLSIC) 2022
- 2021/10 · Gyu-Wan's work on Display Driver IC has been accepted to ISSCC 2022
- 2021/10 · Jeong-Hyun's work on Fully-Integrated Fast Buck Converter has been accepted to ISSCC 2022
- 2021/10 · Jiho's work on TENG Energy-Harvesting IC has been accepted to ISSCC 2022

## 연락과 위치

- 주소: Building E3-2, School of Electrical Engineering, KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon 34141[^contact]
- 교수 연구실: E3-2동 4223호, 학생실 4226호[^contact]
- 전화: +82-42-350-7457 (교수 연구실)[^contact]
- 교수 이메일: hyunskim@kaist.ac.kr[^eeprof]
- 첫 화면 Openings는 2027년 봄학기 석사 신입생 접수가 끝났고 2026년 겨울학기 개별연구는 접수 일정을 추후 알린다고 적는다. 석사 신입생은 해마다 평균 국비 정원 2명과 AI반도체대학원 1명을 뽑고, 학부 성적과 약 1시간의 회로 해석 시험(화이트보드 토론)을 본다고 안내한다.[^home]
[^p1]: Y. Park 외, H.-S. Kim, IEEE Journal of Solid-State Circuits 59, 3511-3524 (2024). <https://doi.org/10.1109/jssc.2024.3442248> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: G.-W. Lim 외, H.-S. Kim, IEEE Journal of Solid-State Circuits 60, 1174-1189 (2025). <https://doi.org/10.1109/jssc.2025.3538075> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: D.-H. Kim, H.-S. Kim, IEEE Journal of Solid-State Circuits 59, 4137-4149 (2024). <https://doi.org/10.1109/jssc.2024.3452238> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: J.-H. Kim, J.-G. Lee, H. Han, H.-S. Kim, IEEE Journal of Solid-State Circuits 61, 5838-5852 (2026). <https://doi.org/10.1109/jssc.2026.3710310> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J.-H. Cho 외, H.-S. Kim, IEEE Journal of Solid-State Circuits 59, 2529-2544 (2024). <https://doi.org/10.1109/jssc.2024.3360708> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: J.-G. Lee, H.-S. Kim, IEEE Journal of Solid-State Circuits 59, 4088-4100 (2024). <https://doi.org/10.1109/jssc.2024.3445127> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: Y.-J. Lee, J.-G. Lee, H.-S. Kim, IEEE Journal of Solid-State Circuits 61, 3688-3703 (2026). <https://doi.org/10.1109/jssc.2025.3648866> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: J. Lee 외, H.-S. Kim, IEEE Journal of Solid-State Circuits 57, 3825-3839 (2022). <https://doi.org/10.1109/jssc.2022.3193738> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 회로설계 연구실 누리집 첫 화면 <https://www.icdesignlab.net/> (연구실 소개, Openings, Latest News, 2026-10-22 열람)
[^research]: 회로설계 연구실 누리집 RESEARCH 페이지 <https://www.icdesignlab.net/research> (Keywords, Topic 01–03, 2026-10-22 열람)
[^prof]: 회로설계 연구실 누리집 Professor 페이지 <https://www.icdesignlab.net/professor> (Research Interests, Education, Professional Experience, Awards & Honors, Academic Activities, Selected Talks, 2026-10-22 열람)
[^students]: 회로설계 연구실 누리집 Students 페이지 <https://www.icdesignlab.net/students> (2026-10-22 열람)
[^alumni]: 회로설계 연구실 누리집 Alumni 페이지 <https://www.icdesignlab.net/alumni> (Ph.D. Alumni, M.S. Alumni, 2026-10-22 열람)
[^pubs]: 회로설계 연구실 누리집 PUBLICATIONS 메뉴: Journals <https://www.icdesignlab.net/journals>, Conferences <https://www.icdesignlab.net/conferences> (목록 범위는 근거 페이지, 2026-10-22 열람)
[^awards]: 회로설계 연구실 누리집 Awards 페이지 <https://www.icdesignlab.net/awards> (2026-10-22 열람)
[^contact]: 회로설계 연구실 누리집 CONTACT 페이지 <https://www.icdesignlab.net/contact> (2026-10-22 열람)
[^eeprof]: KAIST 전기및전자공학부 교수 소개(김현식) <https://ee.kaist.ac.kr/professor/16609/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 이메일, 디비전, 대표업적, 2026-10-22 열람)
[^ssel]: KAIST 반도체시스템공학과 연구실 목록 <https://sse.kaist.ac.kr/research-laboratory/> (회로설계 연구실 항목, 2026-10-22 열람)
[^ssep]: KAIST 반도체시스템공학과 교수진 <https://sse.kaist.ac.kr/professor/> (김현식 교수 항목, 2026-10-22 열람)

# 혼성신호 집적회로 연구실 (Mixed Signal Integrated Circuits Lab, MSICL)

**KAIST 전기및전자공학부 · 류승탁 교수**

- 분야: 아날로그·혼성 신호 집적회로, 데이터 변환기(ADC·DAC), 델타-시그마 변조기와 증분형 ADC, 파이프라인·SAR ADC, 시간 인터리브 고속 ADC, 위성용 방사선 내성 회로, 메모리·센서 판독 회로
- 대분야: 전기전자·반도체·광학
- 태그: 집적회로 설계[^research][^eeprof][^p1]
- 홈페이지: <https://msicl.kaist.ac.kr/>
- 근거와 출처: [혼성신호 집적회로 연구실 근거 페이지](msicl-sources.md)

> 아날로그 신호와 디지털 신호를 서로 바꾸는 데이터 변환기를 중심으로 아날로그·혼성 신호 집적회로를 설계하는 연구실이다. 델타-시그마 변조기와 증분형 ADC, 파이프라인·SAR 혼성 ADC, 고속 시간 인터리브 ADC와 DAC를 칩으로 만들고, 위성용 방사선 내성 회로와 메모리 판독 회로도 연구한다.[^research][^pubs]

## 무엇을 연구하나

연구실 Research Area 페이지는 연구실이 아날로그·혼성 신호 회로(아날로그 회로와 디지털 회로를 한 칩에 함께 쓰는 회로) 설계를 연구하며, 주된 연구 주제가 아날로그 신호를 디지털 신호로, 또는 그 반대로 바꾸는 데이터 변환기라고 소개한다.[^research] 아날로그 신호를 디지털 값으로 바꾸는 변환기를 ADC, 디지털 값을 아날로그 신호로 바꾸는 변환기를 DAC라고 부른다. 같은 페이지는 계산 능력이 크고 전력을 적게 쓰는 디지털 회로가 널리 쓰일수록 사람 생활과 관련된 자연의 신호가 모두 아날로그 신호이므로 그 신호를 디지털 시스템으로 넘겨주는 아날로그 회로가 꼭 필요한 부품이 된다고 설명한다.[^research] 이와 함께 차세대 메모리인 PC-RAM(상변화 메모리, 물질의 결정 상태에 따라 달라지는 저항으로 정보를 저장하는 메모리), 건강 관리용 바이오센서, CMOS 이미지 센서(빛을 받아 영상을 만드는 반도체 센서) 같은 여러 응용을 위한 판독 회로(센서나 메모리 셀이 내는 신호를 읽어 내는 회로)도 연구한다고 적는다.[^research]

연구실 Professor 페이지는 교수의 주요 연구 분야를 데이터 변환기에 무게를 둔 아날로그·혼성 신호 집적회로 설계로 적고, 그 안에 저전력 아날로그-디지털 변환 기법, 고속 데이터 변환기 구조와 회로, 오류를 견디는 동작을 위한 설계 기법(오류 정정과 교정), 합성 가능한 데이터 변환기의 설계 방법론을 든다.[^prof] 전기및전자공학부 교수 소개는 주요 연구를 「Analog/Mixed-mode Integrated Circuit Design」으로 적는다.[^eeprof]

Achievements 페이지는 연구실의 주요 연구 성과를 갈래별로 나열한다.[^achv] 파이프라인 ADC(여러 단을 잇대어 단마다 몇 비트씩 변환하고, 변환하고 남은 오차인 잔차를 키워 다음 단에 넘기는 ADC)에서는 잔차를 키우는 증폭기의 커패시터를 배경에서 조정하는 기법, 연산증폭기를 다시 쓰는 저전력 기법, 기준 전압이 필요 없는 구조를 든다. SAR ADC(비교를 되풀이하며 이진 탐색으로 한 비트씩 값을 정하는 ADC)에서는 속도를 높인 SAR ADC의 디지털 오류 정정, 비이진 다중 비트 구조, 플래시 보조·SAR 보조 시간 인터리브 구조를, 플래시 ADC(비교기 여러 개로 값을 한 번에 정하는 ADC)에서는 보간으로 비교기 수를 줄이는 기법을 든다.[^achv] 이 밖에 작은 크기의 DAC, 시간 인터리브 구조(여러 ADC가 차례로 돌아가며 입력을 표본화해 전체 변환 속도를 높이는 구조)에서 채널 사이 표본화 시점 차이인 타이밍 스큐를 교정하는 기법, 고해상도 SAR ADC의 디지털 선형성 교정, 저항성 메모리 판독 회로, 영상의 성질을 이용해 전력을 줄인 CMOS 이미지 센서를 든다.[^achv] 이 페이지는 성과의 연도를 적지 않는다.

대표 논문으로 보면 최근 연구는 다섯 갈래다. 첫째, 델타-시그마 변조기와 증분형 ADC다(대표 논문 1, 2).[^p1][^p2] 둘째, 파이프라인 ADC와 SAR ADC를 섞은 혼성 ADC다(대표 논문 3, 4).[^p3][^p4] 셋째, 여러 ADC를 번갈아 쓰는 시간 인터리브 ADC의 교정과 고속 DAC다(대표 논문 5, 6).[^p5][^p6] 넷째, 위성용 회로의 방사선 내성 설계다(대표 논문 7).[^p7] 다섯째, 상변화 메모리 판독 회로다(대표 논문 8).[^p8] 2021–2026년 논문 목록에는 이 밖에 양자화한 합성곱 신경망을 값싸게 설계하는 전략 MixedNet(IEEE Access 2021)과 링 증폭기(ringamp)로 잡음이 적은 바이어스 전압을 만드는 기법(IEEE ISCAS 2026)도 있다.[^pubs]

## 주요 연구 주제

### 1. 델타-시그마 변조기와 증분형 ADC

델타-시그마 변조기(신호 대역보다 높은 속도로 표본화하고 양자화 잡음을 신호 대역 밖으로 밀어내는 잡음 성형으로 해상도를 높이는 변환기)에서는 잡음 결합(noise coupling, 양자화 오차를 루프에 되먹여 잡음 성형의 차수를 높이는 기법)과 SAR 양자화기를 함께 쓴다. 대표 논문 1은 연산증폭기 하나로 만든 4차 연속시간 델타-시그마 변조기에 SAR 양자화기의 도움을 받는 3차 디지털 잡음 결합을 더해, 루프 필터의 신호 처리 대부분을 디지털로 옮겼다.[^p1] 증분형 ADC(변환할 때마다 회로를 초기화해 입력 하나를 정해진 시간 안에 변환하는 델타-시그마 계열 ADC)에서는 연속시간·이산시간 변조기와 잡음 성형 SAR ADC를 두 단계로 묶고, 잔차 크기에 따라 단 사이 이득을 고르는 기법을 넣었다.[^p2] 논문 목록에는 하이브리드 잡음 결합 4차 연속시간 변조기(IEEE TCAS-II 2022), SAR 보조 연속시간 1-0 MASH 변조기(MASH는 변조기 여러 단을 잇대어 앞 단의 양자화 오차를 뒷단이 다시 변환하는 구조, IEEE JSSC 2024), 완전 동적 이산시간 변조기(IEEE JSSC 2026), 디지털 영역 잡음 누설 성형을 쓴 M-0 MASH 변조기(IEEE OJCAS 2026), 추적 줌(tracking-zoom) 증분형 ADC(IEEE VLSI Symposium 2024)도 있다.[^pubs] 구성원의 연구 주제에는 연속시간 대역 통과 델타-시그마 변조기가 있다.[^ms] 대표 논문 1, 2.

### 2. 파이프라인·SAR 혼성 ADC

파이프라인 ADC와 SAR ADC를 섞어 효율과 해상도를 함께 높인다. 대표 논문 3은 두 개의 잔차를 쓰는 파이프라인 SAR ADC의 뒷단에 잡음 성형 기능을 갖춘 커패시터 보간 SAR ADC를 넣어 교정 없이 SNDR(신호 대 잡음·왜곡 비, 신호 세기를 잡음과 왜곡을 합친 세기와 비교한 값) 81.2 dB를 얻었다.[^p3] 대표 논문 4는 두 단으로 된 고이득 동적 증폭기를 잔차 증폭기로 쓴 12비트 600 MS/s 파이프라인 ADC다.[^p4] 논문 목록에는 잡음 성형 SAR ADC(IEEE A-SSCC 2024, IEEE CICC 2026), 디더링으로 SAR 보조 다단 ADC의 선형성을 배경 교정하는 기법(IEEE OJCAS 2024), SAR 보조 혼성 ADC를 정리한 초청 논문(IEEE OJ-SSCS 2024), 표본 유지 회로를 함께 쓰는 7비트 2단계 플래시 ADC(IEEE JSSC 2022)도 있다.[^pubs] 대표 논문 3, 4.

### 3. 시간 인터리브 고속 ADC와 DAC

시간 인터리브 ADC에서는 채널 사이의 표본화 시점 차이인 타이밍 스큐를 칩 안에서 교정한다. 대표 논문 5는 상대 소수 회전으로 타이밍 스큐 오차를 동시에 뽑아내는 배경 교정 기법을 8(+1)채널 10비트 1.1 GS/s 시간 인터리브 SAR ADC로 보였다.[^p5] DAC 쪽에서는 고속 전류 조향 DAC(전류원 여러 개의 전류를 출력 쪽으로 돌리거나 막아 아날로그 값을 만드는 DAC)의 배경 교정에서 생기는 글리치를 짝지은 전류원으로 상쇄하는 기법을 내놓았다.[^p6] 논문 목록에는 상대 소수 시간 인터리브 서브레인징 SAR ADC(IEEE JSSC 2021)와 같은 원리의 칩 안 스큐 교정(IEEE VLSI Symposium 2022)도 있다.[^pubs] 구성원의 연구 주제에는 고속 ADC와 고속·고선형성 DAC가 있다.[^phd] 대표 논문 5, 6.

### 4. 위성용 방사선 내성 회로

위성처럼 방사선을 받는 환경에서 쓰는 데이터 변환기를 방사선에 견디도록 설계한다. 대표 논문 7은 총 이온화 선량(TID, Total Ionizing Dose, 소자가 누적해서 흡수한 이온화 방사선량)과 단일 사건 효과(SEE, 입자 하나가 부딪혀 신호가 뒤집히는 등의 순간적 오류)에 대비한 12비트 고전압 DAC를 설계하고 방사선 조사 시험으로 확인했다.[^p7] 논문 목록에는 위성용 고전압 ADC를 위한 TID 내성 비교기와 표본화 회로(IEEE A-SSCC 2024, IEEE TNS 2026)도 있다.[^pubs] 구성원의 연구 주제에는 방사선 내성 데이터 변환기가 있다.[^phd] 대표 논문 7.

### 5. 메모리·센서 판독 회로

Research Area 페이지가 드는 PC-RAM, 바이오센서, CMOS 이미지 센서용 판독 회로 연구의 최근 논문으로, 여러 단계의 저항 값을 저장하는 다단계 상변화 메모리 셀을 연산증폭기 없이 기존 전압 구동기와 비슷한 속도로, 더 적은 전력으로 읽는 회로를 내놓았다.[^research][^p8] 구성원의 연구 주제에는 열마다 둔 판독 ADC(column-parallel readout ADC), 터치 판독 ADC, ADC 설계 자동화가 있다.[^phd][^ms] 대표 논문 8.

## 대표 논문

류승탁 교수가 마지막 저자인 2021–2026년 논문 가운데 초록을 확인할 수 있는 여덟 편을 다섯 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다. 연도는 출판사 서지의 출판 연도다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2025 | [A 0.38-mW 200-kHz-BW Digital-Intensive Single-Opamp Fourth-Order Continuous-Time Delta-Sigma Modulator With Third-Order Digital Noise Coupling in 28-nm CMOS](https://doi.org/10.1109/jssc.2024.3513442) · IEEE Journal of Solid-State Circuits (JSSC) | 디지털 처리 비중을 높이고 연산증폭기를 하나만 쓴 4차 연속시간 델타-시그마 변조기다. SAR 양자화기의 도움을 받는 간단하고 전력이 적은 3차 디지털 잡음 결합을 썼다. 고차 잡음 결합에서는 안정하게 받을 수 있는 최대 입력 크기(MSA)가 제한되는데, 디지털 후단 적분기로 양자화기 입력의 큰 신호를 억제해 한 루프로 잡음 성형을 강하게 하면서도 MSA −1.6 dBFS를 얻었다. 3차 잡음 결합 필터의 덧셈은 디지털 덧셈기 없이 SAR 양자화기의 커패시터 DAC로 전하 영역에서 바로 한다. 28 nm CMOS 시제품은 루프 필터 신호 처리 대부분을 디지털로 옮겨 아날로그 부담을 줄인 고차 변조기를 만들 수 있음을 보였고, 200 kHz 대역에서 최고 SNDR 89.0 dB, SNR 89.2 dB, 동적 범위(DR) 92.1 dB를 1.1 V 전원 0.38 mW로 얻었다. Schreier 성능 지수는 179.3 dB, Walden 성능 지수는 41.2 fJ/conv.-step이다.[^p1] | 1저자 K. E. Lozada(Kent Edrian Lozada), 마지막 저자 류승탁 (6명) |
| 2 | 2026 | [A 96.7-dB-SNDR Two-Step SAR-Assisted Hybrid 2-1 MASH Incremental ADC With Automatic Inter-Stage Gain Selection](https://doi.org/10.1109/jssc.2026.3706374) · IEEE Journal of Solid-State Circuits (JSSC) | 두 단계로 동작하는 SAR 보조 하이브리드 2-1 MASH 증분형 ADC다. 연속시간·이산시간을 섞은 델타-시그마 변조기와 잡음 성형 SAR ADC를 합쳤다. 두 번째 단계에서는 연속시간 단을 꺼서 전력 효율을 높이고, 4비트 SAR 양자화기를 두 단이 함께 써 작게 구현했다. 잔차 크기에 따라 단 사이 이득을 자동으로 고르는 기법(AIGS)으로 둘째 단을 포화시키지 않고 큰 이득을 써서 양자화 잡음에 대한 신호 비(SQNR)를 높였다. 첫 단계 변환에서 2차, 둘째 단계 변환에서 1차 잡음 성형을 더한다. 65 nm CMOS 시제품은 160 kHz 대역에서 SNDR 96.7 dB, DR 100.7 dB를 얻었고, 1.5 V 전원과 표본화 주파수 16.64 MHz에서 1.61 mW를 썼다. Schreier 성능 지수는 176.7 dB다.[^p2] | 1저자 K.-H. Song(Kwan-Hoon Song), 마지막 저자 류승탁 (5명) |
| 3 | 2024 | [A 1.5-MHz BW 81.2-dB SNDR Dual-Residue Pipeline ADC With a Fully Dynamic Noise-Shaping Interpolating-SAR ADC](https://doi.org/10.1109/jssc.2024.3360944) · IEEE Journal of Solid-State Circuits (JSSC) | 에너지 효율이 높은 고해상도 이중 잔차(D-R) 파이프라인 SAR ADC로, 뒷단에 잡음 성형 기능을 갖춘 커패시터 보간 SAR ADC를 넣었다. 잔차를 증폭기가 미리 증폭해 kT/C 잡음(표본화 커패시터에 생기는 열잡음)을 상쇄하므로 잔차 증폭기 설계가 단순해진다. 나눠 만든 DAC 구조로 커패시터 보간에서 기생 커패시턴스가 거는 한계를 넘어, 이중 잔차 구조의 이득 오차가 없는 장점과 함께 해상도를 높였다. 180 nm CMOS 시제품은 교정 없이 1.5 MHz 대역, 과표본화 비율 8에서 SNDR 81.2 dB, SFDR(스퓨리어스 없는 동적 범위) 89.9 dB, SNDR 기준 Schreier 성능 지수 170.4 dB를 얻었다.[^p3] | 1저자 J.-H. Chung(Jae-Hyun Chung), 마지막 저자 류승탁 (7명) |
| 4 | 2026 | [A 12-Bit 600-MS/s Pipelined ADC With Two-Stage High-Gain Dynamic Amplifier in 28-nm CMOS](https://doi.org/10.1109/tcsi.2025.3618298) · IEEE Transactions on Circuits and Systems I: Regular Papers (TCAS-I) | 두 단으로 된 고이득 동적 증폭기를 쓴 12비트 파이프라인 ADC다. 첫 단은 이득을 끌어올린 플로팅 인버터 증폭기(GB-FIA)로 높은 직류 이득과 전력 효율을 얻고, 둘째 단은 전류로 조절하는 지연 셀과 입력 동적 바이어스를 쓴 부분 FIA(P-FIA)로 잔차 증폭기에 안정성, 빠른 출력 변화, 전력 효율을 준다. 시동 속도를 높인 부트스트랩 스위치로 MDAC가 겹치지 않는 구간에서 생기는 표본 의존 비선형성을 줄였다. 28 nm CMOS 시제품은 표본화 속도 600 MS/s, 나이퀴스트 주파수 입력에서 SNDR 58.9 dB를 얻었고, 0.9 V 전원에서 15.6 mW를 써 Schreier 성능 지수 161.8 dB를 보였다. 이득 교정 없이도 나이퀴스트 대역 전체에서 SFDR 77 dB를 넘겼는데, 초록은 이를 충분한 루프 이득, 넓은 출력 범위, 전용 리셋 구간 덕분으로 설명한다.[^p4] | 1저자 B. Gao(Bo Gao), 마지막 저자 류승탁 (8명) |
| 5 | 2026 | [A Time-Interleaved ADC With a Single-Step Relative-Prime-Rotation-Based Background Timing-Skew Calibration Using MAD-Averaging](https://doi.org/10.1109/ojsscs.2026.3666164) · IEEE Open Journal of the Solid-State Circuits Society (OJ-SSCS) | 상대 소수 회전(RPR)을 바탕으로 한 칩 안 배경 타이밍 스큐 교정 기법으로, 채널들의 타이밍 스큐 오차를 동시에 뽑아낸다. 여러 단계로 나눈 교정을 없애고 남은 스큐가 쌓이지 않게 해 빠르고 정확하게 수렴한다. 기준 역할을 하는 ADC와 이웃 채널 사이의 평균 절대 차(MAD)를 써서 적용 대역을 나이퀴스트 주파수까지 넓히고, 채널 수에는 제한을 두지 않는다. 28 nm CMOS로 만든 8(+1)채널 10비트 1.1 GS/s 시간 인터리브 SAR ADC 시제품은 면적 0.16 mm²를 차지하고 1 V 전원에서 9.5 mW를 쓰며, 나이퀴스트 근처 입력에서 SNDR 49.7 dB, SFDR 61.4 dB를 얻었다. Walden 성능 지수는 34.7 fJ/conversion-step이고, 칩 안 교정 회로는 전체 전력의 17%만 쓴다.[^p5] | 1저자 R. Mabilangan(Raymond Mabilangan), 마지막 저자 류승탁 (9명) |
| 6 | 2026 | [A 12-bit 1-GS/s Current-Steering DAC With Paired Current Source Switching Background Mismatch Calibration](https://doi.org/10.1109/jssc.2026.3668788) · IEEE Journal of Solid-State Circuits (JSSC) | 고속 전류 조향 DAC의 배경 교정에서 생기는 스퍼(신호와 상관없이 나타나는 불필요한 주파수 성분)를 억제하는 기법이다. 기존 배경 교정에서는 전류원을 교정 모드로 넣고 뺄 때마다 원치 않는 글리치(짧은 순간의 전압 튐)가 생겨 스퍼로 나타난다. 이 기법은 짝지은 전류원이 차동 출력에 크기가 같고 방향이 반대인 전류를 흘리는 중간 공통 상태를 거쳐 교정에 드나들게 해, 스위칭 때 생기는 글리치를 공통 모드 제거로 상쇄한다. 신호 전력을 줄이거나 잡음을 늘리지 않는다. 28 nm FDSOI 공정으로 만든 12비트 1 GS/s DAC는 직류 근처에서 SFDR 81 dBc, 286 MHz까지 70 dBc 이상을 얻었고 INL·DNL도 좋아졌다. 시제품은 33 mW를 써 성능 지수 28.4 fJ/conversion-step을 보였다.[^p6] | 1저자 C.-U. Park(Chang-Un Park), 마지막 저자 류승탁 (6명) |
| 7 | 2025 | [12-bit High-Voltage Current-Steering-Assisted R-2R DAC With RCM and Parallel Switch for Satellite Applications](https://doi.org/10.1109/tns.2024.3488852) · IEEE Transactions on Nuclear Science (TNS) | 위성 응용을 겨냥한 12비트 고전압 DAC에 설계 단계에서 방사선 내성을 넣은(RHBD) 연구다. 전류 조향의 도움을 받는 R-2R 저항 사다리에 공통 레벨 제어 저항과 병렬 스위치를 더했다. 전류원으로 기존 R-2R 사다리의 스위치 저항이 총 이온화 선량에 민감한 문제를 줄이고, PMOS 전류원과 폴리실리콘 R-2R 망으로 총 이온화 선량 때문에 생기는 누설을 피했다. 공통 레벨 제어 저항으로 전류원의 전압 여유를 늘리고, 단일 사건 효과로 제어 신호 비트가 뒤집히는 것을 줄이려 단위 전류원마다 병렬 스위치를 두었다. 0.35 μm 고전압 CMOS로 만든 칩(2.97 mm²)은 코발트-60 선원으로 116·226 krad(Si)까지 두 단계 시험을 거쳐, 116 krad(Si)에서 INL 저하가 2 LSB보다 작았고 상온 24시간 어닐링 뒤에는 조사 전보다 116·226 krad(Si)에서 각각 1·1.5 LSB 안으로 돌아왔다. 100 MeV 양성자를 20분 쬔 단일 사건 효과 시험에서는 DAC 출력에 비트 뒤집힘이나 흔들림이 보이지 않았다.[^p7] | 1저자 C. Tahar(Charlie Tahar), 마지막 저자 류승탁 (5명) |
| 8 | 2024 | [An M-Metric Readout Circuit for MLC Phase-Change Memory With a Comparator-Based Push-Pull Bit-Line Driver](https://doi.org/10.1109/tcsii.2024.3465888) · IEEE Transactions on Circuits and Systems II: Express Briefs (TCAS-II) | 셀 하나에 여러 단계 값을 저장하는 상변화 메모리(PCM)의 판독 회로로, 입력 범위가 본래 넓은 M-metric 판독 방식을 그대로 구현했다. 기본 M-metric 방식은 큰 비트라인 커패시턴스를 거쳐 PCM 셀에 작은 전류를 흘리고 전압을 재야 해서 판독 속도가 느리다. 이를 넘으려고 연산증폭기 없이 비교기 기반 푸시풀 구동기(CPPD)로 비트라인을 축차 근사 방식으로 구동하는 판독 회로를 제안했다. 비트라인 구동 속도는 기존 전압 구동기와 비슷하지만, 전력을 많이 쓰는 연산증폭기가 없어 전력 소비가 크게 줄었다. 시제품 설계는 6비트 전체 선형성과 245 μW 전력, 270 ns 판독 속도를 얻었다.[^p8] | 1저자 J.-W. Kwon(Ji-Wook Kwon), 마지막 저자 류승탁 (4명) |

## 교수와 전문 분야

류승탁 교수는 KAIST 전기및전자공학부 교수이고 Circuit 디비전에 속한다.[^eeprof][^eelist] 연구실 Professor 페이지는 직함을 전기및전자공학부 Professor로, 소속 연구 그룹을 CS(Circuits and Systems)로 적고, IEEE Senior Member(2013년부터)라고 적는다.[^prof]

Professor 페이지에 따르면 교수는 Kyungpook National University에서 전기공학 학사(1997)를, KAIST에서 전기공학 석사(1999)와 박사(2004)를 받았다.[^prof] 2001–2002년에는 BK21 사업 지원으로 미국 University of California, San Diego에서 방문 연구원으로 있었고, 2004년 삼성전자(기흥)에 들어가 혼성 신호 IP 설계를 맡았다. 2007–2009년 Information and Communications University(ICU) 조교수를 거쳐 2009년부터 KAIST 전기및전자공학부에 있다.[^prof] 누리집 바닥글은 연구실을 "Since 2007"로 적는다.[^home] 같은 페이지는 교수의 연구 관심을 데이터 변환기에 무게를 둔 아날로그·혼성 신호 집적회로 설계로 적는다.[^prof] 전기및전자공학부 교수 소개가 대표업적으로 드는 것은 2013년의 시간 인터리브 2b/cycle SAR ADC(ISSCC), 시간 영역 래치 보간 플래시 ADC(JSSC), 복제 구동 기법(TCASII) 논문과, SAR ADC의 디지털 오류 정정에 관한 미국 특허(2009)·국내 특허(2008)다.[^eeprof]

학계 활동으로 Professor 페이지는 IEEE Solid-State Circuits Society Distinguished Lecturer(2021–2022), IEEE Solid-State Circuits Letters 부편집장(2018–2023), IEEE Open Journal of Circuits and Systems 부편집장(2024–현재), IEEE Open Journal of Solid-State Circuits Society 부편집장(2025–현재), IEEE Journal of Solid-State Circuits 객원 편집자(2017, 2018, 2025)를 적는다. 학회 프로그램 위원으로는 ISSCC 데이터 변환기 분과(2013–2018, 2024–현재), A-SSCC 아날로그·데이터 변환기 분과(2011–현재), CICC 데이터 변환기 분과(2019–2024), ESSCIRC(2020–현재)를, 국내 활동으로 IC Design Education Center(IDEC) 운영위원(2011–현재)과 Korea Semiconductor Conference 프로그램 위원(2009–현재)을 적는다.[^prof] 수상은 다음과 같이 적는다: Educator Award, School of Electrical Engineering, KAIST(2025년 5월), IDEC Teaching Award(2015년 9월), SK Hynix Patent Award(2015년 3월), IDEC Excellent Activity Award(2014년 9월, 2020년 7월, 2023년 7월), Teaching Award, Dept. of Electrical Engineering, KAIST(2012년 8월), Best Teaching Award, School of Engineering, ICU(2007년 12월).[^prof]

논문으로 보면 KAIST에서의 전문 분야는 데이터 변환기 설계다. 델타-시그마 변조기와 증분형 ADC(대표 논문 1, 2),[^p1][^p2] 파이프라인·SAR 혼성 ADC(대표 논문 3, 4),[^p3][^p4] 시간 인터리브 ADC 교정과 고속 DAC(대표 논문 5, 6),[^p5][^p6] 위성용 방사선 내성 DAC(대표 논문 7),[^p7] 메모리 판독 회로(대표 논문 8)에 걸친다.[^p8]

## 응용 분야

Research Area 페이지는 연구실의 판독 회로가 겨냥하는 응용으로 차세대 메모리인 PC-RAM, 건강 관리용 바이오센서, CMOS 이미지 센서를 든다.[^research] 대표 논문 7은 위성 응용을 위한 고전압 DAC이고, 논문 목록의 TID 내성 비교기도 위성용 고전압 ADC를 겨냥한다.[^p7][^pubs] 대표 논문 8은 다단계 상변화 메모리의 판독 회로다.[^p8] 구성원의 연구 주제에는 터치 판독 ADC가 있다.[^ms]

## 구성원

연구실 누리집 Members 메뉴의 Ph.D. Students 페이지 9명(박사과정 6, 석박사통합과정 3)과 M.S. Students 페이지 4명, 모두 13명이다.[^phd][^ms] Ph.D. Students 페이지에는 박사후연구원(Post Doc.) 칸이 있으나 비어 있다.[^phd] Members 첫 페이지도 2026년 가을 학기 현황을 박사과정 9명, 석사과정 4명으로 적는다.[^members] 과정은 각 카드에서 "Present"로 끝나는 학력 줄의 과정 표기이고, 「시작」은 그 줄의 시작 연월, 연구 주제는 카드의 표기다. 박사과정 두 명의 카드에는 랩 대표(Lab Representative)와 부대표(Lab Vice Representative) 표기가 있다.[^phd] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| 이창엽 (Changyeop Lee) | 박사과정 | Feb. 2019 | High-Speed ADC | 7 |
| 박건우 (Kunwoo Park) | 박사과정 | Feb. 2022 | Noise-Shaping SAR ADC | 2, 3 |
| Charlie Tahar | 석박사통합과정 | Aug. 2020 | Radiation-Tolerant Data Converters | 5, 6, 7 |
| 김형진 (Hyeong Jin Kim) | 박사과정 | Aug. 2022 | ADC Design Automation |  |
| 신현우 (Hyun Woo Shin) | 박사과정 | Feb. 2023 | High-Speed ADC | 6 |
| 문영훈 (Moon, Younghun) | 박사과정 (Lab Representative) | Feb. 2024 | High-Resolution ADC | 2 |
| Long Vu Hoang | 석박사통합과정 | Feb. 2024 | High-Speed & High-Linearity DACs |  |
| 김지용 (Ji Yong Kim) | 박사과정 (Lab Vice Representative) | Feb. 2026 | High-Speed ADC |  |
| 김형표 (Hyungpyo Kim) | 석박사통합과정 | Feb. 2025 | High-Speed ADC |  |
| 김현진 (Hyeonjin Kim) | 석사과정 | Feb. 2025 | Column-Parallel Readout ADC |  |
| 박찬연 (Chanyeon Park) | 석사과정 | Feb. 2025 | Touch Readout ADC |  |
| 장재우 (Jaewoo Jang) | 석사과정 | Sep. 2025 | Continuous-Time Bandpass Delta-Sigma Modulator |  |
| 오정환 (Jeonghwan Oh) | 석사과정 | Sep. 2026 | TBD |  |

## 졸업생

누리집 Alumni 페이지의 59명 전부다(박사 24, 석박사통합과정 4, 석사 31, 학위 연도 2010–2026). 학위와 연도, 진로는 누리집 표기이며, 학위 칸은 각 졸업생의 학력 가운데 맨 위 줄이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Raymond Mabiliangan | Integrated M.S & Ph.D. Electrical Engineering, KAIST (2026) | Prof. at University of the Philippines Los Baños |
| Krishnakanth R | M.S. Electrical Engineering, KAIST (2026) | Astera Labs |
| Sangwon Lee | M.S. Electrical Engineering, KAIST (2026) |  |
| Chang Un Park | Ph.D. Electrical Engineering, KAIST (2026) | Samsung Electronics @ S. LSI Business |
| Bo Gao | Ph.D. Electrical Engineering, KAIST (2026) | China Electronics Technology Group Corporation |
| Kwanhoon Song | Ph.D. Electrical Engineering, KAIST (2026) | ABOV Semiconductor |
| In Sung Heo | M.S. Electrical Engineering, KAIST (2026) | Baum Design Systems |
| Kent Edrian Lozada | Integrated M.S & Ph.D. Electrical Engineering, KAIST (2025) | AAC Technologies |
| Sung Ho Kim | M.S. Electrical Engineering, KAIST (2025) | Samsung Electronics @ Memory Business |
| Ji Hoo Kim | M.S. Electrical Engineering, KAIST (2025) | Samsung Electronics @ Memory Business |
| Jong Hyeon Baek | M.S. Electrical Engineering, KAIST (2025) | Samsung Electronics @ Memory Business |
| Ye Dam Kim | Ph.D. Electrical Engineering, KAIST (2024) | Samsung Electronics @ S. LSI Business |
| Kyeong Min Chae | M.S. Electrical Engineering, KAIST (2024) | SK Hynix |
| Seong Min Lee | M.S. Electrical Engineering, KAIST (2024) | SK Hynix |
| Ji Un Hong | M.S. Electrical Engineering, KAIST (2024) | Samsung Electronics @ Memory Business |
| Jae Hyun Chung | Integrated M.S & Ph.D. Electrical Engineering, KAIST (2023) | Samsung Electronics @ S. LSI Business |
| Un Shi An | M.S. Electrical Engineering, KAIST (2023) | Samsung Electronics @ S. LSI Business |
| Dong Hun Lee | M.S. Electrical Engineering, KAIST (2023) | SK Hynix |
| Hyeong Jin Yoo | M.S. Electrical Engineering, KAIST (2022) | Samsung Electronics @ Memory Business |
| Trang Dang Khoa | M.S. Electrical Engineering, KAIST (2022) | Inria |
| Seung Yong Lim | M.S. Electrical Engineering, KAIST (2021) | Samsung Electronics @ Memory Business |
| Eun Ji An | M.S. Electrical Engineering, KAIST (2021) | Samsung Electronics @ Memory Business |
| Yi Ju Roh | Ph.D. Electrical Engineering, KAIST (2020) | Apple |
| Gyeom-Je Bae | M.S. Electrical Engineering, KAIST (2020) | Samsung Electronics @ S. LSI Business |
| Won-Mook Lim | M.S. Electrical Engineering, KAIST (2020) | Samsung Electronics |
| Dong-Jin Chang | Ph.D. Electrical Engineering, KAIST (2019) | Prof. at Chungnam National University |
| Dong-Ryeol Oh | Integrated M.S & Ph.D. Electrical Engineering, KAIST (2019) | Prof. at Jeju National University |
| Woo-Cheol Kim | Ph.D. Electrical Engineering, KAIST (2019) | Samsung Electronics |
| Kyoung-Jun Moon | Ph.D. Electrical Engineering, KAIST (2019) | Samsung Electronics @ S. LSI Business |
| Jae-Hyeok Baek | M.S. Electrical Engineering, KAIST (2019) | Samsung Electronics @ Memory Business |
| Min-Jae Seo | Ph.D. Electrical Engineering, KAIST (2019) | Prof. at University of Seoul |
| Dong-Shin Jo | Ph.D. Electrical Engineering, KAIST (2019) | Samsung Electronics America |
| Sun-Il Hwang | Ph.D. Electrical Engineering, KAIST (2019) | SK Hynix |
| Dong Hwan Jin | Ph.D. Electrical Engineering, KAIST (2019) | SK Hynix |
| Tae Yun Kim | M.S. Electrical Engineering, KAIST (2019) | Samsung Electronics |
| Hyun-Wook Kang | Ph.D. Electrical Engineering, KAIST (2018) | Samsung Electronics America |
| Il-Hoon Jang | Ph.D. Electrical Engineering, KAIST (2018) | Samsung Electronics @ S. LSI Business |
| Kyoungjun Roh | M.S. Electrical Engineering, KAIST (2018) | Samsung Electronics / Agency for Defense Development |
| Si-Nai Kim | Ph.D. Electrical Engineering, KAIST (2017) | Phychips |
| Hyeon-June Kim | Ph.D. Electrical Engineering, KAIST (2017) | SK Hynix |
| Eun-Seong Choi | M.S. Electrical Engineering, KAIST (2017) | Samsung Electronics |
| Mi Young Kim | M.S. Electrical Engineering, KAIST (2017) | Veritas International Patent Office |
| Ba Ro Saim Sung | Ph.D. Electrical Engineering, KAIST (2016) | Samsung Electronics |
| Ji-Wook Kwon | Ph.D. Electrical Engineering, KAIST (2016) | Samsung Electronics |
| Hyeok-Ki Hong | Ph.D. Electrical Engineering, KAIST (2016) | Samsung Electronics @ SAIT |
| Wan Kim | Ph.D. Electrical Engineering, KAIST (2016) | Samsung Electronics @ S. LSI Business |
| Kihoon Seo | M.S. Electrical Engineering, KAIST (2016) | Agency for Defense Development |
| Jingwang Kim | M.S. Electrical Engineering, KAIST (2016) | Korea Aerospace Research Institute |
| Jong-In Kim | Ph.D Electrical Engineering, KAIST (2015) | Broadcom |
| Ghil-Geun Oh | Ph.D. Electrical Engineering, KAIST (2015) | Samsung Electronics @ Foundry Business |
| Jae Keun Lee | M.S. Electrical Engineering, KAIST (2014) | Samsung Electronics |
| Yeong-Jae Choi | M.S. Electrical Engineering, KAIST (2014) | SK Hynix |
| Ki-Jeong Min | M.S. Electrical Engineering, KAIST (2014) | Samsung Electronics |
| Chang-Kyo Lee | Ph.D. Electrical Engineering, KAIST (2013) | AMD |
| Jae-Kyum Lee | M.S. Electrical Engineering, KAIST (2013) | Tyndall National Institute |
| Mee Ran Kim | M.S. Electrical Engineering, KAIST (2013) | Samsung Electronics |
| Seung-Yeob Baek | M.S. Electrical Engineering, KAIST (2012) | Samsung Electronics |
| Hun-Do Shin | M.S. Electrical Engineering, KAIST (2011) | Apple |
| Sang Hyun Cho | Ph.D. Electrical Engineering, KAIST (2010) | Samsung Electronics @ S. LSI Business |

## 최근 논문 목록 (2021–2026)

누리집 Publications 메뉴의 2021–2026년 논문 40편이다. Journals 페이지의 학술지 18편과 Conferences 페이지의 학회 논문 22편이며, 연도마다 학술지 논문을 먼저 적었다. 저자 순서와 제목·학술지·학회 표기는 누리집 그대로이고, 저자 이름 뒤 *는 누리집이 공동 기여(ECAs)로 표시한 저자다. 2026년 구역의 ESSERC 논문 두 편은 첫 화면이 2026년 5월에 채택을 알린 논문으로, 「ESSERC 2026 채택」을 붙여 출판 논문과 구분했다.[^pubs][^home]

**2026**

- Young-Hun Moon, Kun-Woo Park, Krishnakanth R, Kyunghoon Kim, Minho Kwon, Min-Jae Seo, and Seung-Tak Ryu. "A 0.2-mW 250-kHz-BW Fully Dynamic kT/C Noise-Shaping Discrete-Time Delta-Sigma Modulator With SAR-Assisted Input Feedforward and Digital Noise Coupling". *IEEE JSSC, 2026*.
- Charlie Tahar, Changyeop Lee, Kun-Woo Park, Kent Edrian Lozada, Hyojun Kim, Ki-Ho Kwon, and Seung-Tak Ryu. "TID-Tolerant StrongARM Comparator and Sampling Network for Satellite Application High-Voltage ADCs". *IEEE TNS, 2026*.
- Kwanhoon Song, Young-Hun Moon, Kun-Woo Park, Kent Edrian Lozada, and Seung-Tak Ryu. "A 96.7 dB-SNDR Two-Step SAR-Assisted Hybrid 2-1 MASH Incremental ADC with Automatic Inter-Stage Gain Selection". *IEEE JSSC, 2026*.
- Chang-Un Park, Jae-Hyun Chung, Chunsuk Kim, Hyun-Woo Shin, Charlie Tahar, and Seung-Tak Ryu. "A 12-bit 1-GS/s Current-Steering DAC with Paired Current Source Switching Background Mismatch Calibration". *IEEE JSSC, 2026*.
- Raymond Mabilangan, Bo Gao, Charlie Tahar, Woong-Taek Lim, Kyung-Hoon Lee, Michael Choi, Kent Edrian Lozada, Dong-Jin Chang, and Seung-Tak Ryu. "A Time-Interleaved ADC with a Single-Step Relative-Prime-Rotation- Based Background Timing-Skew Calibration Using MAD-Averaging". *IEEE OJ-SSCS, 2026*.
- Kent Edrian Lozada, Bo Gao, Raymond Mabilangan, Charlie Tahar, Kun-Woo Park, Young-Hun Moon, Kwan-Hoon Song, and Seung-Tak Ryu. "A SAR-Assisted Continuous-Time M-0 MASH Delta-Sigma Modulator with Digital-Domain Noise Leakage Shaping". *IEEE OJCAS, 2026*.
- Kent Edrian Lozada, Raymond Mabilangan, Charlie Tahar, Young-Hun Moon, Hyun-Woo Shin, Hyeongjin Kim, Bo Gao, Kwan-Hoon Song, Woong-Taek Lim, Kyung-Hoon Lee, Michael Choi, and Seung-Tak Ryu. "A 0.36-mW 500-kHz-BW 182.2-dB-FoMs 3rd-order DNC-Based Sturdy MASH CT DSM". *IEEE ESSERC, 2026 (ESSERC 2026 채택)*.
- Hyun-Woo Shin, Chang-Un Park, Changyeop Lee, Ji-Yong Kim, Charlie Tahar, Kent Edrian Lozada, Dong-Ryeol Oh, and Seung-Tak Ryu. "A 7-bit 900-MS/s SAR-TDC Hybrid ADC with PVT Robust VTC/TDC and Offsets Compensation". *IEEE ESSERC, 2026 (ESSERC 2026 채택)*.
- Krishnakanth R, Raymond Mabilangan, Hyungpyo Kim, Kent Edrian Lozada, and Seung-Tak Ryu. "A Ringamp-Based Low-Noise Bias Generation Technique". *IEEE ISCAS, 2026*.
- Kun-Woo Park, Young-Hun Moon, Charlie Tahar, Hyeongjin Kim, Kwan-Hoon Song, and Seung-Tak Ryu. "An 80.1dB-SNDR 1.5MHz-BW 3rd-Order Noise Shaping SAR ADC with Idle-free Residue Processing". *IEEE CICC, 2026*.

**2025**

- Bo Gao, Raymond Mabilangan, Chang-Un Park, Kent Edrian Lozada, Ho-Jin Kim, Youngjae Cho, Michael Choi, and Seung-Tak Ryu. "A 12-bit 600-MS/s Pipelined ADC With Two-Stage High-Gain Dynamic Amplifier in 28-nm CMOS". *IEEE TCAS-I, 2025*.
- Young-Hun Moon, Kun-Woo Park, Kyunghoon Kim, Minho Kwon, Min-Jae Seo, and Seung-Tak Ryu. "A 250kHz-BW 86.2dB-SNDR 176.7dB-FoMS Fully Dynamic kT/C Noise-Canceled DT DSM with SAR-Assisted Input FF and DNC". *IEEE ASSCC, 2025*.
- Kwan-Hoon Song, Young-Hun Moon, Kun-Woo Park, Kent Edrian Lozada, and Seung-Tak Ryu. "A 160kHz-BW 96.7dB-SNDR Two-Step 2-1 MASH Hybrid Incremental ΔΣ ADC with Automatic Inter-Stage Gain Selection". *IEEE ASSCC, 2025*.
- Young-Hun Moon, Kun-Woo Park, Kwan-Hoon Song, Kent Edrian Lozada, Min-Jae Seo, and Seung-Tak Ryu. "A 184dB-FoMS 25kHz-BW 98.6dB-SNDR Fully Dynamic Discrete-Time Delta-Sigma Modulator with Digital Noise Coupling". *IEEE MWSCAS, 2025*.
- Kwan-Hoon Song, Kun-Woo Park, Young-Hun Moon, Kent Edrian Lozada, and Seung-Tak Ryu. "A 10-kHz BW 97-dB SNDR 3rd-Order Incremental Delta-Sigma ADC with Hybrid CT/DT Loop Filter". *IEEE MWSCAS, 2025*.
- Kent Edrian Lozada, Ye-Dam Kim, Il-Hoon Jang, and Seung-Tak Ryu. "Continuous-Time Delta-Sigma Modulator with SAR-Assisted Digital Noise Coupling". *IEEE CICC, 2025*.

**2024**

- Kent Edrian Lozada, Ye-Dam Kim, Ho-Jin Kim, Youngjae Cho, Michael Choi, and Seung-Tak Ryu. "A 0.38-mW 200-kHz-BW Digital-Intensive Single-Opamp Fourth-Order Continuous-Time Delta-Sigma Modulator With Third-Order Digital Noise Coupling in 28-nm CMOS". *IEEE JSSC, 2024*.
- Charlie Tahar, Changyeop Lee, Hyojun Kim, and Seung-Tak Ryu. "12-bit High-Voltage Current-Steering-Assisted R-2R DAC with RCM and Parallel Switch for Satellite-Applications". *IEEE TNS, 2024*.
- Ji-Wook Kwon, Dong-Hwan Jin, Min-Jae Seo, and Seung-Tak Ryu. "An M-Metric Readout Circuit for MLC Phase-Change Memory With a Comparator-Based Push-Pull Bit-Line Driver". *IEEE TCAS-II, 2024*.
- Lizhen Zhang, Bo Gao, Kun-Woo Park, Kent Edrian Lozada, Raymond Mabilangan, Hyeongjin Kim, Jianhui Wu, Seung-Tak Ryu. "DR Loss-Free Dithering-Based Digital Background Linearity Calibration for SAR-Assisted Multi-Stage ADCs with Digital Input-Interference Cancellation". *IEEE OJCAS, 2024*.
- Kent Edrian Lozada, Dong-Jin Chang, Dong-Ryeol Oh, Min-Jae Seo, Seung-Tak Ryu. "SAR-Assisted Energy-Efficient Hybrid ADCs". *IEEE OJ-SSCS, 2024*.
- Dong-Hun Lee\*, Kent Edrian Lozada\*, Ye-Dam Kim, Ho-Jin Kim, Youngjae Cho, Michael Choi, and Seung-Tak Ryu. "A 25-kHz-BW 97.4-dB-SNDR SAR-Assisted Continuous-Time 1-0 MASH Delta-Sigma Modulator With Digital Noise Coupling". *IEEE JSSC, 2024*.
- Jae-Hyun Chung, Ye-Dam Kim, Chang-Un Park, Kun-Woo Park, Min-Jae Seo, Dong-Ryeol Oh, and Seung-Tak Ryu. "A 1.5-MHz BW 81.2-dB SNDR Dual-Residue Pipeline ADC With a Fully Dynamic Noise-Shaping Interpolating-SAR ADC". *IEEE JSSC, 2024*.
- Charlie Tahar, Changyeop Lee, Kun-Woo Park, Kent Edrian Lozada, Hyojun Kim, Ki-Ho Kwon, and Seung-Tak Ryu. "TID-Tolerant StrongARM Comparator and Sampling Network for Satellite Application High-Voltage ADCs". *IEEE ASSCC, 2024*.
- Bo Gao, Lizhen Zhang, Raymond Mabilangan, Chang-Un Park, Kent Edrian Lozada, Ho-Jin Kim, Youngjae Cho, Michael Choi, and Seung-Tak Ryu. "A 28nm CMOS 12-bit-600-MS/s 15.6mW Pipelined ADC with Two-Stage Gainboosting FIA-based RA". *IEEE ASSCC, 2024*.
- Lizhen Zhang, Bo Gao, Kun-Woo Park, Hyeongjin Kim, Kent Edrian Lozada, Ye-Dam Kim, Juanhui Wu, and Seung-Tak Ryu. "A 5x OSR 1MHz-BW 81dB-SNDR 5th-Order Noise-Shaping SAR ADC with Zero-Optimized 3rd-Order Integrator". *IEEE ASSCC, 2024*.
- Charlie Tahar, Changyeop Lee, Hyojun Kim, Ki-Ho Kwon, and Seung-Tak Ryu. "12-bit High-Voltage Current-Steering-Assisted R-2R DAC with RCM and Parallel Switch for Satellite-Applications". *IEEE Nuclear & Space Radiation Effects Conference, 2024*.
- Ye-Dam Kim, Jae-Hyun Chung, Kent Edrian Lozada, Chang-Un Park, Kun-Woo Park, Kwan-Hoon Song, Young-Hun Moon, Min-Jae Seo, and Seung-Tak Ryu. "A 100kHz-BW 99dB-DR Continuous-Time Tracking-Zoom Incremental ADC with Residue-Gain Switching and Digital NC-FF". *IEEE Symposium on VLSI Technology and Circuits, 2024*.
- Kent Edrian Lozada, Ye-Dam Kim, Ho-Jin Kim, Youngjae Cho, Michael Choi, and Seung-Tak Ryu. "A 0.38mW 200kHz-BW 92.1dB-DR Single-Opamp 4th-order Continuous-Time Delta-Sigma Modulator with 3rd-order Noise Coupling". *IEEE Symposium on VLSI Technology and Circuits, 2024*.

**2023**

- Kent Edrian Lozada\*, Dong-Hun Lee\*, Ye-Dam Kim, Ho-Jin Kim, Youngjae Cho, Michael Choi, and Seung-Tak Ryu. "A 25kHz-BW 97.4dB-SNDR 100.2dB-DR 3rd-order SAR-Assisted CT DSM with 1-0 MASH and DNC". *IEEE ASSCC, 2023*.
- Jae-Hyun Chung, Ye-Dam Kim, Chang-Un Park, Kun-Woo Park, Min-Jae Seo, and Seung-Tak Ryu. "An 81.2dB-SNDR Dual-Residue Pipeline ADC with a 2nd-Order Noise-Shaping Interpolating SAR ADC". *IEEE CICC, 2023*.
- Chang-Un Park, Jae-Hyun Chung, and Seung-Tak Ryu. "A 12-bit 1GS/s Current-Steering DAC with Paired Current Source Switching Background Mismatch Calibration". *IEEE CICC, 2023*.

**2022**

- Kent Edrian Lozada, Il-Hoon Jang, Gyeom-Je Bae, Dong-Hun Lee, Ye-Dam Kim, Hankyu Lee, Seong Joong Kim, and Seung-Tak Ryu. "A 4th-Order Continuous-Time Delta-Sigma Modulator with Hybrid Noise-Coupling". *IEEE TCAS-II, 2022*.
- Dong-Ryeol Oh, Min-Jae Seo, and Seung-Tak Ryu. "A 7-bit Two-Step Flash ADC With Sample-and-Hold Sharing Technique". *IEEE JSSC, 2022*.
- Kent Edrian Lozada, Il-Hoon Jang, Gyeom-Je Bae, Dong-Hun Lee, Ye-Dam Kim, Hankyu Lee, Seong Joong Kim, and Seung-Tak Ryu. "A 4th-Order Continuous-Time Delta-Sigma Modulator with Hybrid Noise-Coupling". *IEEE MWSCAS, 2022*.
- Dong-Jin Chang, and Seung-Tak Ryu. "A Relative-Prime Rotation Based Fully On-Chip Background Skew Calibration for Time-Interleaved ADCs". *IEEE VLSI Symposium on Technology and Circuits, 2022*.

**2021**

- Dong-Jin Chang, Byeong-Gyu Nam, and Seung-Tak Ryu. "MixedNet: Network Design Strategies For Cost-Effective Quantized CNNs". *IEEE Access, 2021*.
- Dong-Jin Chang, Michael Choi, and Seung-Tak Ryu. "A 28-nm 10-b 2.2-GS/s 18.2-mW Relative-Prime Time-Interleaved Sub-ranging SAR ADC with On-Chip Background Skew Calibration". *IEEE JSSC, 2021*.
- Ye-Dam Kim, Jae-Hyun Chung, Kent Edrian Lozada, Dong-Jin Chang, and Seung-Tak Ryu. "A 4th-Order CT I-DSM with Digital Noise Coupling and Input Pre-Conversion Method for Initialization". *IEEE ASSCC, 2021*.
- Seungyong Lim, Raymond Mabilangan, Dong-Jin Chang, Youngjae Cho, Michael Choi, and Seung-Tak Ryu. "An Input-Buffer Embedding Dual-Residue Pipelined-SAR ADC with Nonbinary Capacitive Interpolation". *IEEE ASSCC, 2021*.

## 소식

누리집 첫 화면 NEWS의 2021년 10월 이후 소식 56건(2021년 12월–2026년 9월)이다. 날짜는 누리집의 연·월 표기이고 문구는 누리집 그대로이며, 논문 채택 소식에는 바로 아래 줄에 적힌 논문 제목을 함께 적었다.[^home]

- 2026.09 · Young-Hun Moon's paper has been accepted to JSSC. "A 0.2-mW 250-kHz-BW Fully Dynamic kT/C Noise-Shaping Discrete-Time Delta-Sigma Modulator With SAR-Assisted Input Feedforward and Digital Noise Coupling."
- 2026.06 · Charlie Tahar's paper has been accepted to IEEE Transactions on Nuclear Science. "TID-Tolerant StrongARM Comparator and Sampling Network for Satellite Application High-Voltage ADCs."
- 2026.06 · Kwanhoon Song's paper has been accepted to JSSC. "A 96.7-dB SNDR Two-Step SAR-Assisted Hybrid 2-1 MASH Incremental ADC with Automatic Inter-Stage Gain Selection."
- 2026.05 · Kent Edrian Lozada's paper has been accepted to IEEE European Solid-State Electronics Research Conference 2026. "A 0.36-mW 500-kHz-BW 182.2-dB-FoMs 3rd-order DNC-Based Sturdy MASH CT DSM."
- 2026.05 · Hyun-Woo Shin's paper has been accepted to IEEE European Solid-State Electronics Research Conference 2026. "A 7-bit 900-MS/s SAR-TDC Hybrid ADC with PVT Robust VTC/TDC and Offsets Compensation."
- 2026.05 · Our alumnus, Dr. Min-Jae Seo (Associate Professor at the University of Seoul), has received the 2026 IEIE-IEEE Joint Award for Young Scientist and Engineer.
- 2026.04 · Bo Gao's TCAS-I paper entitled “A 12-Bit 600-MS/s Pipelined ADC With Two-Stage High-Gain Dynamic Amplifier in 28-nm CMOS” has been selected as the Highlight paper of the TCAS-I April 2026 issue.
- 2026.03 · Kent Edrian Lozada's paper received the Outstanding Invited Paper Award in 2025 IEEE CICC.
- 2026.02 · Chang-Un Park's paper has been accepted to JSSC. "A 12-bit 1-GS/s Current-Steering DAC with Paired Current Source Switching Background Mismatch Calibration."
- 2026.02 · Raymond Mabilangan's paper has been accepted to IEEE Open Journal of the Solid-State Circuits Society 2026. "A Time-Interleaved ADC with a Single-Step Relative-Prime-Rotation- Based Background Timing-Skew Calibration Using MAD-Averaging."
- 2026.02 · Kent Edrian Lozada's paper has been accepted to IEEE Open Journal of Circuit and Systems 2026. "A SAR-Assisted Continuous-Time M-0 MASH Delta-Sigma Modulator with Digital-Domain Noise Leakage Shaping."
- 2026.01 · Krishnakanth R's paper has been accepted to the IEEE International Symposium on Circuits and Systems 2026. "A Ringamp-Based Low-Noise Bias Generation Technique."
- 2026.01 · Kun-Woo Park's paper has been accepted to the IEEE Custom Integrated Circuits Conference 2026. "An 80.1dB-SNDR 1.5MHz-BW 3rd-Order Noise Shaping SAR ADC with Idle-free Residue Processing."
- 2025.11 · Kwan-Hoon Song's paper has been invited to JSSC, on the Special Issue on A-SSCC 2025.
- 2025.11 · Young-Hun Moon received the A-SSCC 2025 Student Design Contest Best Design Award.
- 2025.10 · Bo Gao's paper has been accepted to the TCAS-I. "A 12-bit 600-MS/s Pipelined ADC With Two-Stage High-Gain Dynamic Amplifier in 28-nm CMOS."
- 2025.08 · Kwan-Hoon Song's paper has been accepted to the IEEE Asian Solid-State Circuits Conference 2025. "A 160kHz-BW 96.7dB-SNDR Two-Step 2-1 MASH Hybrid Incremental ΔΣ ADC with Automatic Inter-Stage Gain Selection ."
- 2025.08 · Young-Hun Moon's paper has been accepted to the IEEE Asian Solid-State Circuits Conference 2025. "A 250kHz-BW 86.2dB-SNDR 176.7dB-FoMS Fully Dynamic kT/C Noise-Canceled DT DSM with SAR-Assisted Input FF and DNC ."
- 2025.08 · Young-Hun Moon received the MWSCAS Best Paper Award.
- 2025.07 · Kwan-Hoon Song received the award at the IDEC Congress Chip Design Contest.
- 2025.05 · Prof. Ryu has been awarded the KAIST Educator Award.
- 2025.05 · Young-Hun Moon's paper has been accepted to the 2025 IEEE International Midwest Symposium on Circuits and Systems. "A 184dB-FoMS 25kHz-BW 98.6dB-SNDR Fully Dynamic Discrete-Time Delta-Sigma Modulator with Digital Noise Coupling."
- 2025.05 · Kwan-Hoon Song's paper has been accepted to the 2025 IEEE International Midwest Symposium on Circuits and Systems. "A 10-kHz BW 97-dB SNDR 3rd-Order Incremental Delta-Sigma ADC with Hybrid CT/DT Loop Filter."
- 2025.02 · Kent Edrian Lozada has been selected for the prestigious 2025 KAIST Jang Young Sil Fellow Program.
- 2025.02 · Kent Edrian Lozada has been honored with the prestigious Ph.D. Dissertation Award from the KAIST College of Engineering.
- 2025.01 · Kent Edrian Lozada's paper has been invited and accepted to 2025 IEEE Custom Integrated Circuits Conference (CICC). "Continuous-Time Delta-Sigma Modulator with SAR-Assisted Digital Noise Coupling"
- 2024.12 · Kent Edrian Lozada's paper has been accepted to JSSC, on the Special Issue on VLSI Symposium 2024. "A 0.38-mW 200-kHz-BW Digital-Intensive Single-Opamp Fourth-Order Continuous-Time Delta-Sigma Modulator With Third-Order Digital Noise Coupling in 28-nm CMOS"
- 2024.10 · Ji-Wook Kwon's paper has been accepted to TCAS-II. "An M-Metric Readout Circuit for MLC Phase-Change Memory with a Comparator-Based Push-Pull Bit-Line Driver."
- 2024.10 · Charlie Tahar's paper has been accepted to IEEE Transactions on Nuclear Science, on the Special Issue on NSREC 2024. "12-bit High-Voltage Current-Steering-Assisted R-2R DAC with RCM and Parallel Switch for Satellite-Applications ."
- 2024.10 · Lizhen Zhang's paper has been accepted to IEEE Open Journal of Circuits and Systems 2024. "DR Loss-Free Dithering-Based Digital Background Linearity Calibration for SAR-Assisted Multi-Stage ADCs with Digital Input-Interference Cancellation ."
- 2024.09 · Kent Edrian Lozada's paper has been invited and accepted to IEEE Open Journal of the Solid-State Circuits Society 2024. "SAR-Assisted Energy-Efficient Hybrid ADCs ."
- 2024.08 · Charlie Tahar's paper has been accepted to IEEE Asian Solid-State Circuits Conference 2024. "TID-Tolerant StrongARM Comparator and Sampling Network for Satellite Application High-Voltage ADCs ."
- 2024.08 · Bo Gao's paper has been accepted to IEEE Asian Solid-State Circuits Conference 2024. "A 28nm CMOS 12-bit-600-MS/s 15.6mW Pipelined ADC with Two-Stage Gainboosting FIA-based RA ."
- 2024.08 · Lizhen Zhang's paper has been accepted to IEEE Asian Solid-State Circuits Conference 2024. "A 5x OSR 1MHz-BW 81dB-SNDR 5th-Order Noise-Shaping SAR ADC with Zero-Optimized 3rd-Order Integrator ."
- 2024.07 · Kent Edrian Lozada's paper has been invited to JSSC, on the Special Issue on VLSI Circuits Symposium 2024.
- 2024.05 · Charlie Tahar received the 2024 IEEE NSREC Early Career Travel Grant Award.
- 2024.04 · Kent Edrian Lozada and Dong-Hun Lee's paper has been accepted to JSSC, on the Special Issue on A-SSCC 2023. "A 25kHz-BW 97.4dB-SNDR SAR-Assisted Continuous-Time 1-0 MASH Delta-Sigma Modulator with Digital Noise Coupling."
- 2024.04 · Ye-Dam Kim's paper has been accepted to the 2024 IEEE VLSI Symposium on Technology and Circuits. "A 100kHz-BW 99dB-DR Continuous-Time Tracking-Zoom Incremental ADC with Residue-Gain Switching and Digital NC-FF ."
- 2024.04 · Kent Edrian Lozada's paper has been accepted to the 2024 IEEE VLSI Symposium on Technology and Circuits. "A 0.38mW 200kHz-BW 92.1dB-DR Single-Opamp 4th-order Continuous-Time Delta-Sigma Modulator with 3rd-order Noise Coupling ."
- 2024.03 · Charlie Tahar's abstract has been accepted to IEEE Nuclear & Space Radiation Effects Conference 2024.
- 2024.03 · Kent Edrian Lozada's presentation at the 2023 A-SSCC has been invited for a Special Session at 2024 IEEE Custom Integrated Circuits Conference.
- 2024.01 · Jae-Hyun Chung's paper has been accepted to JSSC. "A 1.5-MHz BW 81.2-dB SNDR Dual-Residue Pipeline ADC With a Fully Dynamic Noise-Shaping Interpolating-SAR ADC ."
- 2023.11 · Kent Edrian Lozada and Dong-Hun Lee's paper has been invited to JSSC, on the Special Issue on A-SSCC 2023.
- 2023.11 · Kent Edrian Lozada and Dong-Hun Lee received the Distinguished Design Award at the Student Design Contest of the 2023 IEEE Asian Solid-State Circuits Conference.
- 2023.08 · Kent Edrian Lozada and Dong-Hun Lee's paper has been accepted to the 2023 IEEE Asian Solid-State Circuits Conference. "A 25kHz-BW 97.4dB-SNDR 100.2dB-DR 3rd-order SAR-Assisted CT DSM with 1-0 MASH and DNC."
- 2023.06 · Our alumnus Dr. Dong-Jin Chang joins Chungnam National University as an assistant professor. Congratulations!
- 2023.03 · Our alumnus Dr. Dong-Ryeol Oh joins Jeju National University as an assistant professor. Congratulations!
- 2023.02 · Jae-Hyun Chung received the Special Award (IEEE SSCS Seoul Chapter) at the 30th Korean Conference on Semiconductors (KCS).
- 2023.01 · Jae-Hyun Chung's paper has been accepted to the 2023 IEEE Custom Integrated Circuits Conference. " An 81.2dB-SNDR Dual-Residue Pipeline ADC with a 2nd-Order Noise-Shaping Interpolating SAR ADC ."
- 2023.01 · Chang-Un Park's paper has been accepted to the 2023 IEEE Custom Integrated Circuits Conference. " A 12-bit 1GS/s Current-Steering DAC with Paired Current Source Switching Background Mismatch Calibration ."
- 2022.06 · Kent Edrian Lozada's paper has been invited and accepted to the TCAS-II for the Special Issue on MWSCAS 2022. " A 4th-Order Continuous-Time Delta-Sigma Modulator with Hybrid Noise-Coupling ."
- 2022.05 · Kent Edrian Lozada's paper has been accepted to the 2022 IEEE International Midwest Symposium on Circuits and Systems. " A 4th-Order Continuous-Time Delta-Sigma Modulator with Hybrid Noise-Coupling ."
- 2022.04 · Dong-Jin Chang's paper has been accepted to the 2022 IEEE VLSI Symposium on Technology and Circuits. " A Relative-Prime Rotation Based Fully On-Chip Background Skew Calibration for Time-Interleaved ADCs ."
- 2022.03 · Dong-Ryeol Oh's paper has been accepted to JSSC. " A 7-bit Two-Step Flash ADC With Sample-and-Hold Sharing Technique ."
- 2022.02 · Our alumnus Dr. Min-Jae Seo joins Gachon University (Department of Electronic Engineering) as an assistant professor. Congratulations!
- 2021.12 · Ye-Dam Kim and Kent Edrian Lozada received the Excellence Award at IITP-ITRC AISS Workshop.

## 연락과 위치

- 주소: 대전 유성구 대학로 291 (한국과학기술원), 전기및전자공학부(E3-2) 동측 4층 #4230/#4224/#4225(교수)[^home]
- 전화: 학생실 +82-42-350-7625 / +82-42-350-7525, 교수실 +82-42-350-7425[^home]
- 교수 이메일: stryu@kaist.ac.kr[^eeprof]
[^p1]: K. E. Lozada 외, S.-T. Ryu, IEEE Journal of Solid-State Circuits 60, 1236-1247 (2025). <https://doi.org/10.1109/jssc.2024.3513442> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: K.-H. Song 외, S.-T. Ryu, IEEE Journal of Solid-State Circuits 61, 5472-5484 (2026). <https://doi.org/10.1109/jssc.2026.3706374> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J.-H. Chung 외, S.-T. Ryu, IEEE Journal of Solid-State Circuits 59, 2481-2491 (2024). <https://doi.org/10.1109/jssc.2024.3360944> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: B. Gao 외, S.-T. Ryu, IEEE Transactions on Circuits and Systems I: Regular Papers 73, 2371-2382 (2026). <https://doi.org/10.1109/tcsi.2025.3618298> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: R. Mabilangan 외, S.-T. Ryu, IEEE Open Journal of the Solid-State Circuits Society 6, 164-177 (2026). <https://doi.org/10.1109/ojsscs.2026.3666164> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: C.-U. Park 외, S.-T. Ryu, IEEE Journal of Solid-State Circuits 61, 4182-4192 (2026). <https://doi.org/10.1109/jssc.2026.3668788> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: C. Tahar 외, S.-T. Ryu, IEEE Transactions on Nuclear Science 72, 1425-1432 (2025). <https://doi.org/10.1109/tns.2024.3488852> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: J.-W. Kwon, D.-H. Jin, M.-J. Seo, S.-T. Ryu, IEEE Transactions on Circuits and Systems II: Express Briefs 71, 4658-4662 (2024). <https://doi.org/10.1109/tcsii.2024.3465888> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 혼성신호 집적회로 연구실 누리집 첫 화면 <https://msicl.kaist.ac.kr/> (LATEST NEWS, 연도별 NEWS, CONTACT US, 2026-10-23 열람)
[^research]: 연구실 누리집 Research Area 페이지 <https://sites.google.com/view/msicl/research_1/research-area> (2026-10-23 열람)
[^achv]: 연구실 누리집 Achievements 페이지 <https://sites.google.com/view/msicl/research_1/achievements> (Major Research Achievements, 2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <https://sites.google.com/view/msicl/members/professor> (직함, Education, Research Group, Major Research Area, Biography, Awards, Activities, 2026-10-23 열람)
[^members]: 연구실 누리집 Members 페이지 <https://sites.google.com/view/msicl/members> (Members Overview, 2026 Fall Semester 현황, 2026-10-23 열람)
[^phd]: 연구실 누리집 Ph.D. Students 페이지 <https://sites.google.com/view/msicl/members/ph-d-students> (2026-10-23 열람)
[^ms]: 연구실 누리집 M.S. Students 페이지 <https://sites.google.com/view/msicl/members/m-s-students> (2026-10-23 열람)
[^alumni]: 연구실 누리집 Alumni 페이지 <https://sites.google.com/view/msicl/members/alumni> (2026-10-23 열람)
[^pubs]: 연구실 누리집 Publications 메뉴: Journals <https://sites.google.com/view/msicl/publications_1/journals>, Conferences <https://sites.google.com/view/msicl/publications_1/conferences> (목록 범위는 근거 페이지, 2026-10-23 열람)
[^eeprof]: KAIST 전기및전자공학부 교수 소개(류승탁) <https://ee.kaist.ac.kr/professor/12172/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 이메일, 웹사이트, 디비전, 학위, 대표업적, 2026-10-23 열람)
[^eelist]: KAIST 전기및전자공학부 교수(전임교수) 목록 1쪽 <https://ee.kaist.ac.kr/professor-s1/> (류승탁 항목의 직위·디비전·웹사이트, 2026-10-23 열람)

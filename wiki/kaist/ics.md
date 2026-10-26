# 집적 컴퓨터 시스템 연구실 (ICSL, Integrated Computer Systems Lab.)

**KAIST 전기및전자공학부 · 박인철 교수**

- 분야: 디지털 회로 설계, 디지털 VLSI 설계와 CAD
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 집적회로 설계[^home][^eeprof][^p8], 오류 정정 부호[^home][^research][^p1], AI 반도체·가속기[^home][^ai][^p4], 컴퓨터 구조·운영체제[^home][^soc], 메모리 내 연산[^home][^ai], 무선·이동통신[^home][^p1], FPGA·재구성형 하드웨어[^p7]
- 홈페이지: <https://ics.kaist.ac.kr/>
- 근거와 출처: [집적 컴퓨터 시스템 연구실 근거 페이지](ics-sources.md)

> 컴퓨터 구조와 임베디드 프로세서, 그리고 통신 시스템의 오류 정정과 인공지능 연산 등 계산이 많은 디지털 기능 블록의 칩 내부 회로 구조를 설계하는 연구실이다.[^home]

## 무엇을 연구하나

연구실은 컴퓨터 구조, 임베디드 프로세서(기기 안에 넣어 정해진 일을 맡는 프로세서), 그리고 계산이 많은 기능 블록의 VLSI 구조(수많은 트랜지스터를 칩 하나에 모은 대규모 집적회로의 내부 구성)에 집중한다고 소개한다. 기능 블록의 예로는 멀티미디어 신호 처리, 통신 시스템의 신호 검출과 오류 정정, 인공지능을 위한 딥러닝 구조를 든다.[^home] 첫 화면이 꼽는 현재 연구 주제는 기계학습과 인공지능을 위한 프로그래밍 가능한 학습 하드웨어 구조, LDPC 부호와 폴라 부호를 위한 오류 정정 하드웨어 구조, SSD 플랫폼 설계, 5G 통신 시스템을 위한 MIMO 심볼 검출이다.[^home] 전기및전자공학부 교수 소개와 반도체시스템공학과 연구실 목록은 주요 연구를 디지털 회로 설계, 디지털 VLSI 설계와 CAD(컴퓨터로 회로 설계를 돕는 설계 자동화)로 적는다.[^eeprof][^ssel]

Research 페이지는 연구 분야를 일곱 갈래로 나눈다. 신경망용 VLSI(CNN·RNN 같은 신경망 하드웨어 가속기, 딥러닝 전용 명령어 집합 프로세서, 메모리 안에서 계산하는 PIM), 통신용 VLSI(MIMO 심볼 검출기, 폴라·BCH·터보·LDPC 복호기, FFT 프로세서, OFDM 수신기의 디지털 기저대역 동기화), SoC 설계(범용 프로세서, 멀티코어·멀티칩 프로세서 시스템, 캐시 제어기와 메모리 관리 장치, 칩 안 연결망, 운영체제·컴파일러 같은 시스템 소프트웨어), 고속 디지털 회로(카운터), 멀티미디어 응용 VLSI(움직임 추정, JPEG2000·JPEG-XR 정지 영상 처리), 아날로그·혼성 신호 IC(델타-시그마 변조기, 전 디지털 PLL, AD 변환기), CAD(필터 합성, 상위 수준 합성)다.[^research]

인공지능 하드웨어를 다룬 Research 하위 페이지는 네 가지 작업을 소개한다. 합성곱을 점진적으로 계산해 데이터 재사용을 늘린 딥러닝 전용 명령어 집합 프로세서(DSIP), 곱셈기 없이 연산하도록 가중치를 양자화하는 에너지 효율적 컴퓨터 산술, RISC 프로세서와 신경망 처리 장치(NPU)가 일을 나눠 맡는 FPGA 위의 고성능 물체 검출 시스템, 그리고 메모리 안에서 행 단위로 CNN 추론을 처리해 기존 메모리 인터페이스와 호환되는 PIM 구조다.[^ai] SoC 하위 페이지는 사물인터넷 응용을 위한 범용 프로세서·멀티코어 시스템과 함께, 실시간 제어용 전자 제어 장치(ECU)를 소개한다. 이 ECU는 고장을 견디는 Core-A 프로세서와 메모리 시스템, 단방향 링 이더넷 연결망을 갖추고 실시간 운영체제 FreeRTOS를 옮겨 실었다.[^soc]

연구실은 자체 명령어 집합을 가진 32비트 RISC 프로세서 Core-A를 국내 기술만으로 개발한 일을 성과로 들고, 시스템 통합을 위해 칩 안 버스 Core-Bus와 컴파일러·디버거 같은 소프트웨어 묶음도 만들었다고 소개한다.[^home] 연혁에는 2007년 Core-A 프로세서, 2010년 Core-A2G 프로세서, 2011년 Multi-Core-A2G 프로세서, 2017년 딥러닝 전용 명령어 집합 프로세서(DSIP) 개발이 적혀 있다.[^intro] Chip Gallery는 1999–2020년에 만든 칩 33개를 싣는데, 가장 최근 것은 2020년 28nm CMOS 공정의 칩 안 연결망(NoC) 멀티코어 시스템, 2019년 행 단위 처리 메모리, 2018년 IDMA 수신기와 딥러닝 전용 명령어 집합 프로세서다.[^chip]

대표 논문으로 보면 최근 연구는 네 갈래다. 첫째, 5G 이동통신의 LDPC 부호, 폴라 부호, 고대역폭 메모리(HBM)의 리드-솔로몬 부호처럼 전송·저장 중 생긴 오류를 고치는 부호의 복호기 하드웨어다(대표 논문 1, 2, 3).[^p1][^p2][^p3] 둘째, 신경망의 SoftMax 함수 연산기와 FPGA 위의 CNN 추론 가속기다(대표 논문 4, 5).[^p4][^p5] 셋째, 정규분포를 따르는 잡음을 여러 개 만들어 내는 하드웨어와 LDPC 복호 성능을 평가하는 FPGA 기반 시뮬레이션 플랫폼이다(대표 논문 6, 7).[^p6][^p7] 넷째, 고속 디지털 카운터다(대표 논문 8).[^p8]

## 주요 연구 주제

### 1. 오류 정정 부호 복호기 하드웨어

5G New-Radio 표준이 정한 모든 리프팅 크기(기본 검사 행렬의 각 칸을 몇 칸짜리 블록으로 키울지 정하는 값)를 지원하면서 최대 처리량 요구를 채우는 QC-LDPC 복호기를 만들었다. 완전 병렬 구조 대신 부분 병렬 구조로 하드웨어 복잡도를 줄이고, 새 메모리 접근 스케줄링으로 데이터 접근·정렬 문제를 풀었다.[^p1] 폴라 부호의 연속 제거 리스트(SCL) 복호에서는 오류 확률이 낮은 노드로 경계를 만들어 경로가 갈라지는 횟수와 복호 사이클을 줄였고,[^p2] HBM3 메모리 표준이 정한 단일 심볼 오류 정정 리드-솔로몬 부호의 복호기는 갈루아 체 역원 표를 쓰지 않는 구조로 면적을 줄였다.[^p3] 논문 목록에는 BCH 부호의 부호화기와 신드롬 계산 구조, 해밍 부호의 부호화·복호 구조, LDPC 부호의 비트 반전 복호를 다룬 논문도 있다.[^pubs] 대표 논문 1, 2, 3.

### 2. 인공지능 연산 하드웨어

신경망의 SoftMax 함수를 하드웨어로 만들 때 최댓값 대신 다른 값을 빼고, 지수 합의 역수를 구해 나눗셈을 곱셈으로 바꾼 가속기를 설계했다.[^p4] 고해상도 이미지를 다루는 스타일 변환 CNN을 위해, 네트워크·데이터 압축과 층 연결 기법으로 칩 밖 메모리와 주고받는 데이터를 줄인 FPGA 추론 가속기도 만들었다.[^p5] 논문 목록에는 Swish 활성화 함수의 하드웨어 근사(2024)와 여러 매끄러운 활성화 함수를 한 구조로 근사하는 방법(2026)도 있다.[^pubs] 대표 논문 4, 5.

### 3. 잡음 생성과 복호 성능 평가 하드웨어

정규분포를 따르는 양자화된 잡음을 여러 개 만들어 내는 두 가지 하드웨어 구조를 내놓았고,[^p6] LDPC 복호 알고리즘과 설계 선택을 바꿔 가며 성능을 평가할 수 있도록 프로그래밍할 수 있는 FPGA 기반 범용 QC-LDPC 프로세서를 만들었다.[^p7] 논문 목록에는 몬테카를로 시뮬레이션용 표본 생성 구조 두 편(2026)과 대수적 부호의 비트 오류율을 적은 계산으로 평가하는 방법(2025)도 있다.[^pubs] 대표 논문 6, 7.

### 4. 고속 디지털 카운터

LFSR 카운터의 상태를 하나 늘리는 상태 확장과 두 하위 카운터 구성으로, 세는 속도가 카운터 크기와 거의 상관없는 고속 카운터를 설계했다.[^p8] 논문 목록에는 최소 클록 주기로 일정 시간에 세는 동기식 이진 카운터(2021)와 세는 속도가 일정한 고속 CMOS 동기식 이진 카운터(2025)도 있다.[^pubs] 대표 논문 8.

## 대표 논문

랩 International Journal 목록의 2021–2026년 학술지 논문 가운데 박인철 교수가 마지막 저자 또는 1저자인 논문을, 네 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2022 | [Multi-Mode QC-LDPC Decoding Architecture With Novel Memory Access Scheduling for 5G New-Radio Standard](https://doi.org/10.1109/tcsi.2022.3150022) · IEEE Transactions on Circuits and Systems I: Regular Papers | LDPC 부호(저밀도 패리티 검사 부호)는 오류를 고치는 성능이 강하고 처리량을 높게 낼 수 있어 여러 분야에 쓰이며, 최근 5G New-Radio 통신 표준의 채널 부호화 방식으로 채택됐다. 5G의 LDPC 부호는 다른 LDPC 부호와 달리 여러 길이의 메시지를 지원하려고 불규칙한 여러 리프팅 크기를 둔다. 5G 표준의 까다로운 요구를 맞추려는 해법이 여럿 나왔지만 모두 실용적이지 않거나 요구 조건을 다 채우지 못했다. 이 논문은 5G 표준의 최대 처리량 요구를 채우면서 표준이 정한 모든 리프팅 크기를 지원하는, 면적 효율이 높은 QC-LDPC 복호기를 처음 제안한다고 밝힌다. 이전 연구처럼 완전 병렬 구조에 기대지 않고 부분 병렬 구조를 써 하드웨어 복잡도를 낮췄다. 부분 병렬 구조 때문에 생기는 데이터 접근·정렬 문제는 새 메모리 접근 스케줄링 방법으로 풀어 모든 리프팅 크기를 지원했다. 65nm CMOS 공정으로 구현한 복호기는 복호 처리량이 20Gbps를 넘고 면적은 기존 복호기보다 작았다.[^p1] | 1저자 S. Lee, 마지막 저자 박인철 (4명) |
| 2 | 2025 | [Multi-Bit Successive Cancellation List Decoding of Polar Codes Using One-Bit Error Boundary](https://doi.org/10.1109/lcomm.2025.3561246) · IEEE Communications Letters | 폴라 부호의 연속 제거 리스트(SCL) 복호에서 경로가 갈라지는 횟수를 줄이는 방법을 제안한 짧은 논문(레터)이다. SC 복호 트리 안에서 오류 확률이 낮은 단일 비트 노드와 다중 비트 노드로 경계를 만들고, 경계 위의 노드에서는 자식 노드로 내려가지 않고 경로마다 후보를 두 개만 따진다. 경계를 정하려고 SC 복호 트리에 있는 다중 비트 노드의 오류 확률을 분석했다. 제안한 방법은 기존 SCL 복호와 거의 같은 오류 정정 성능을 지키면서 전체 복호 사이클을 약 70% 줄였다.[^p2] | 1저자 박인철 (5명) |
| 3 | 2026 | [A Hardware-Efficient Reed–Solomon Decoding Architecture for Single-Symbol Error Correcting in High-Bandwidth Memory](https://doi.org/10.1109/tvlsi.2026.3692208) · IEEE Transactions on Very Large Scale Integration (VLSI) Systems | JEDEC HBM3 표준은 16비트 심볼을 쓰는 (19, 17) 단일 심볼 오류 정정(SSEC) 리드-솔로몬 부호를 반드시 쓰도록 정해, 하드웨어 구현이 면적과 지연의 엄격한 제약을 맞춰야 한다. SSEC 복호는 여러 심볼을 고치는 일반 복호보다 단순하지만, 기존 구조는 여전히 갈루아 체(GF) 역원 연산에 기대어 룩업 테이블(LUT) 부담이 컸다. 이 짧은 논문(브리프)은 HBM 환경에 맞춘, 면적 효율이 높고 빠른 SSEC 리드-솔로몬 복호 구조를 제안한다. (19, 17) 부호의 메시지가 짧다는 점을 이용해 복호 연산을 제한된 GF 원소로 좁혀 비싼 GF 역원 LUT를 없앴고, 오류 위치와 크기는 비교 기반 탐색과 상수 GF 곱셈으로 정한다. 28nm CMOS 공정 합성 결과, 기존 복호기 구현보다 면적을 최대 97% 줄였고 알고리즘 기준선보다 동작 속도를 최대 81% 높였다.[^p3] | 1저자 J. Kwon, 마지막 저자 박인철 (5명) |
| 4 | 2024 | [Hardware-Efficient SoftMax Architecture With Bit-Wise Exponentiation and Reciprocal Calculation](https://doi.org/10.1109/tcsi.2024.3443270) · IEEE Transactions on Circuits and Systems I: Regular Papers | SoftMax 함수는 심층 신경망(DNN)에서 입력 값을 0과 1 사이로 정규화하는 활성화 함수의 하나다. 트랜스포머 같은 DNN 모델이 나오면서 SoftMax를 쓰는 연산이 주목받았고, 이를 하드웨어로 효율적으로 구현하는 일이 중요한 문제가 됐다. SoftMax 구현에는 지수 연산과 나눗셈이 들어가 하드웨어 비용과 성능의 병목이 될 수 있다. 이전 연구 대부분은 수치 안정성을 위해 모든 입력에서 최댓값을 뺐는데, 이 논문은 최댓값 대신 다른 값을 빼 수치 안정성을 지키면서 하드웨어 복잡도를 줄인다. 지수 연산은 항목이 하나뿐인 단순한 룩업 테이블(LUT)로 비트 단위로 계산하고, 지수 합의 역수를 구해 나눗셈을 곱셈으로 바꿨다. 이전의 log-sum-exp 방식보다 계산 복잡도를 크게 줄였고, 제안한 8비트 SoftMax 가속기는 3.12GHz의 동작 주파수와 25G inputs/s의 처리량을 냈다. 면적 효율과 전력 소모는 적어도 2배 개선했고, 정확도는 이전 연구와 비슷하거나 더 좋았다.[^p4] | 1저자 J. Kim, 마지막 저자 박인철 (4명) |
| 5 | 2023 | [A CNN Inference Accelerator on FPGA With Compression and Layer-Chaining Techniques for Style Transfer Applications](https://doi.org/10.1109/tcsi.2023.3234640) · IEEE Transactions on Circuits and Systems I: Regular Papers | 합성곱 신경망(CNN)은 최근 내용 이미지의 스타일을 스타일 이미지의 스타일로 바꾸는 스타일 변환 같은 컴퓨터 비전 응용에 활발히 쓰인다. 스타일 변환 CNN은 인코더-디코더 구조이고 요즘 주류가 된 고해상도 이미지를 다뤄야 해, 계산량과 특징 맵 크기가 매우 커서 FPGA에 구현하기 어렵다. 이 논문은 네트워크 압축과 층 연결(layer-chaining) 기법을 쓰는 스타일 변환용 CNN 추론 가속기를 제안한다. 네트워크 압축은 스타일 변환 CNN의 계산량과 파라미터 수를 줄이고, 효율적인 데이터 압축 방법으로 특징 맵 크기를 줄인다. 층 연결 기법은 적은 하드웨어 자원을 들여 칩 밖 메모리와 주고받는 데이터를 줄이고 처리량을 높인다. 두 기법을 고려해 신경망 처리 장치(NPU)를 설계했고, FPGA 보드에 구현한 시제품 가속기는 인코더-디코더 CNN용으로 개발된 최신 가속기와 견줄 만한 처리량을 냈다.[^p5] | 1저자 S. Kim, 마지막 저자 박인철 (6명) |
| 6 | 2025 | [Hardware-Efficient Architecture for Multiple Quantized Gaussian Noise Generation](https://doi.org/10.1109/tcsi.2024.3524591) · IEEE Transactions on Circuits and Systems I: Regular Papers | 양자화된 가우스 잡음(정규분포를 따르는 무작위 값을 정해진 단계의 값으로 나타낸 것)을 여러 개 만드는 새 하드웨어 구조 두 가지를 제안한다. 첫째 구조는 균일 분할을 통한 역변환을 이용하는데, 룩업 테이블(LUT)을 균일하게 나누는 기법으로 가우스 잡음의 꼬리(드물게 나오는 큰 값 쪽) 품질을 적절히 지키면서 양자화된 잡음을 효율적으로 만든다. 둘째 구조는 계층 분할을 통한 역변환과 확률에 따라 LUT를 고르는 방식으로 전체 LUT 크기를 크게 줄이면서 꼬리 품질을 지킨다. 두 설계 모두 조합 회로를 이어 붙여 균일 난수 여러 개를 만들어, 기존의 선형 되먹임 시프트 레지스터(LFSR) 방식보다 가우스 잡음 생성 효율을 높였다. 계층 분할 역변환에 기반한 이전 구조와 비교하면, FPGA에 구현했을 때 구성 가능 논리 블록(CLB)당 처리량이 균일 분할 구조는 6.02배, 계층 분할 구조는 2.71배 좋아졌다.[^p6] | 1저자 K. Choi, 마지막 저자 박인철 (2명) |
| 7 | 2026 | [General-Purpose QC-LDPC Processor for Error-Correction Performance Evaluation](https://doi.org/10.1109/tcsi.2026.3652226) · IEEE Transactions on Circuits and Systems I: Regular Papers | LDPC 복호 성능을 평가하려고 만든 범용 QC-LDPC 프로세서(GPLP)로, 유연하고 프로그래밍할 수 있는 FPGA 기반 시뮬레이션 플랫폼이다. 시뮬레이션하고 검증할 복호 알고리즘과 설계 선택에 따라 LDPC 복호 과정을 구성할 수 있다. 정해진 데이터 흐름에 기대는 기존 FPGA 방식과 달리, 여러 설계 구성에 맞춰 프로그래밍할 수 있는 프로세서 형태의 재구성 환경을 준다. 논문은 QC-LDPC 복호에 꼭 필요한 기본 연산을 정의하고, 이 연산들을 벡터 단위로 처리하는 GPLP 구조를 제안한다. GPLP는 CPU 기반 시뮬레이션보다 220–574배 빠르게 시뮬레이션했다.[^p7] | 1저자 K. Choi, 마지막 저자 박인철 (3명) |
| 8 | 2022 | [High-Speed Counter with Novel LFSR State Extension](https://doi.org/10.1109/tc.2022.3187343) · IEEE Transactions on Computers | 새 LFSR 상태 확장을 쓰는 고속 카운터 구조다. 상태 확장으로, 상태가 2^m−1개인 m비트 LFSR 카운터가 세는 속도를 떨어뜨리지 않고 2^m개 상태를 모두 쓰게 했다. 낮은 자리 비트만 자주 바뀐다는 성질을 이용해 카운터를 두 하위 카운터로 나눠, 세는 속도를 높이고 LFSR 상태를 이진수로 바꾸는 데 드는 하드웨어 복잡도를 줄였다. 낮은 자리 하위 카운터는 제안한 LFSR 카운터로, 높은 자리 하위 카운터는 기존 동기식 이진 카운터로 만들었다. 높은 자리 하위 카운터의 큰 팬아웃(한 신호가 이어진 입력의 수) 때문에 생기는 속도 저하도 고려했다. 표준 셀로 설계한 카운터는 65nm CMOS 공정에서 2.08GHz로 동작하고, 세는 속도는 카운터 크기와 거의 상관없었다.[^p8] | 1저자 H. Bae, 마지막 저자 박인철 (8명) |

## 교수와 전문 분야

박인철 교수는 KAIST 전기및전자공학부 교수이고 Circuit·Communication 디비전에 속한다.[^eeprof][^eelist] 전기및전자공학부 교수 소개의 주요 연구분야는 Information, Communication & Coding, Computer Architecture, Software Systems & Networking, Integrated Circuits & Semiconductor Systems이고, 주요 연구는 Digital Circuit Design, Digital VLSI Design and CAD다.[^eeprof] 반도체시스템공학과 교수진에도 연구분야 「반도체 시스템 및 집적회로」, 연구실 「집적 컴퓨터 시스템 연구실」로 올라 있다.[^ssep]

연구실 Professor 페이지에 따르면 교수는 서울대학교에서 전자공학 학사(1986)를, KAIST에서 전기공학 석사(1988)와 박사(1992)를 받았다. KAIST에 오기 전 1995년 5월–1996년 5월 미국 뉴욕주 Yorktown의 IBM T.J. Watson Research Center에서 고속 회로 설계를 연구했고, 1996년 6월 KAIST 조교수가 됐다.[^prof] 연구실 연혁은 교수가 1996년 KAIST에 와 경종민(Chong-Min Kyung) 교수와 VLSI systems Laboratory를 시작했고, 2000년 집적 컴퓨터 시스템 연구실이 세워졌으며, 교수가 2005년 11월 정교수가 됐다고 적는다.[^intro] Professor 페이지는 교수가 ICCD에서 best paper award(1999)를, ASP-DAC에서 best design award(1997)를 받았고 IEEE Senior Member라고 적고, 연구 관심사를 상위 수준 합성(동작 설명으로부터 회로 구조를 자동으로 만드는 설계 단계)을 위한 CAD 알고리즘과 범용 마이크로프로세서의 VLSI 구조로 적는다.[^prof] 연혁에는 연구실 팀이 Altera Design Contest에서 2014년과 2015년 The 1st Place, 2016년 The Excellence Award를 받은 일도 있다.[^intro]

전기및전자공학부 교수 소개가 대표업적으로 드는 세 편은 임베디드 DSP 소프트웨어를 위한 응용 특화 명령어 합성(1999), 지연과 덧셈기 수를 줄이는 FIR 필터 합성 알고리즘(2001), LDPC 부호의 메모리 기반 복호 구조(2006)로, 모두 2021년 이전 논문이다.[^eeprof] Class 페이지에 따르면 교수는 2021–2026년에 회로이론(EE201), 디지털 시스템 설계(EE303), 전산기 구조(EE511), 디지털 컴퓨터 연산(EE675)을 가르쳤다.[^class]

논문으로 보면 최근의 전문 분야는 네 갈래다. 5G 통신 부호와 메모리 오류 정정 부호의 복호기 VLSI 구조(대표 논문 1, 2, 3),[^p1][^p2][^p3] 신경망 연산 하드웨어(대표 논문 4, 5),[^p4][^p5] 잡음 생성과 복호 성능 평가 하드웨어(대표 논문 6, 7),[^p6][^p7] 고속 디지털 회로(대표 논문 8)다.[^p8]

## 응용 분야

대표 논문들은 5G New-Radio 통신 표준의 LDPC 복호기(대표 논문 1), JEDEC HBM3 메모리 표준의 오류 정정 복호기(대표 논문 3), 트랜스포머 같은 심층 신경망에 쓰이는 SoftMax 연산기(대표 논문 4), 고해상도 이미지의 스타일 변환 가속기(대표 논문 5)를 다룬다.[^p1][^p3][^p4][^p5] LDPC 복호 성능 평가용 시뮬레이션 플랫폼(대표 논문 7)은 복호 성능을 빠르게 평가하고 최적화하는 도구로 제안됐다.[^p7] 첫 화면은 SSD 플랫폼 설계와 5G 통신 시스템을 위한 MIMO 심볼 검출을 현재 연구 주제로 들고,[^home] SoC 하위 페이지는 실시간 제어용 전자 제어 장치(ECU)를 소개한다.[^soc] Projects 페이지가 진행 중으로 적은 과제는 비대면·인공지능 사회를 위한 반도체/시스템 융합혁신기술 개발과 오류 정정 부복호 하드웨어 가속기를 생성하는 전문가 시스템이다.[^projects]

## 구성원

연구실 누리집 Members 페이지의 박사과정 3명과 석사과정 11명이다.[^members] 과정과 시작 연월, 이메일은 페이지 표기다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 김성호(Kim, Sungho) | 박사과정 | 2025.03~ | shkim@ics.kaist.ac.kr | 4 |
| 김정민(Kim, Jeongmin) | 박사과정 | 2025.03~ | jmkim@ics.kaist.ac.kr | 3, 4 |
| 최강준(Choi, Kangjoon) | 박사과정 | 2025.09~ | kjchoi@ics.kaist.ac.kr | 4, 6, 7 |
| 윤정현(Yoon, Jeonghyeon) | 석사과정 | 2025.03~ | jhyoon@ics.kaist.ac.kr | 3 |
| 이가은(Lee, Gaeun) | 석사과정 | 2025.03~ | gelee@ics.kaist.ac.kr |  |
| 문형석(Moon, Hyeongseok) | 석사과정 | 2025.03~ | hsmoon@ics.kaist.ac.kr |  |
| 안용현(Ahn, Yonghyeon) | 석사과정 | 2025.03~ | yhahn@ics.kaist.ac.kr |  |
| 박성용(Park, Seongyong) | 석사과정 | 2025.09~ | sypark@ics.kaist.ac.kr |  |
| 이규호(Lee, Gyuho) | 석사과정 | 2025.09~ | ghlee@ics.kaist.ac.kr |  |
| 이수훈(Lee, Soohoon) | 석사과정 | 2025.09~ | shlee@ics.kaist.ac.kr |  |
| 박성호(Park, Sungho) | 석사과정 | 2026.03~ | shpark@ics.kaist.ac.kr |  |
| 김미리(Kim, Miri) | 석사과정 | 2026.03~ | mrkim@ics.kaist.ac.kr |  |
| 이준휘(Lee, Junhwi) | 석사과정 | 2026.03~ | junhwilee@ics.kaist.ac.kr |  |
| 최상원(Choi, Sangwon) | 석사과정 | 2026.03~ | swchoi@ics.kaist.ac.kr |  |

## 졸업생과 이전 구성원

누리집 Members 페이지의 Ph.D. ALUMNI 24명(1999–2023년)과 M.S. ALUMNI 75명(1998–2026년)이다. 연도와 진로는 페이지 표기이고, 진로가 적히지 않은 석사 졸업생이 4명 있다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 최훈 | Ph.D. (1999) | Silicon Image |
| 김한수 | Ph.D. (2001) | LG전자 |
| 이종열 | Ph.D. (2002) | 전북대학교 |
| 신명철 | Ph.D. (2004) | 삼성전자 |
| 강형주 | Ph.D. (2005) | 한국기술교육대학교 |
| 심재훈 | Ph.D. (2005) | 경북대학교 |
| 이성원 | Ph.D. (2005) | 삼성전자 |
| 배영돈 | Ph.D. (2005) | Apple |
| 박성일 | Ph.D. (2006) | 삼성전자 |
| 강세현 | Ph.D. (2007) | 삼성전자 |
| 이용석 | Ph.D. (2007) | Qualcomm |
| 이현용 | Ph.D. (2008) | 삼성전자 |
| 김지훈 | Ph.D. (2009) | 한양대학교 |
| 한정호 | Ph.D. (2010) | Rebellions |
| 김태환 | Ph.D. (2010) | 한국항공대학교 |
| 송진욱 | Ph.D. (2012) | 삼성전자 |
| 이영주 | Ph.D. (2014) | KAIST |
| 김봉진 | Ph.D. (2014) | 삼성전자 |
| 유호영 | Ph.D. (2016) | 충남대학교 |
| 유인재 | Ph.D. (2017) | 부산대학교 |
| 공병용 | Ph.D. (2017) | 공주대학교 |
| 정재환 | Ph.D. (2018) | FuriosaAI |
| 조지혁 | Ph.D. (2018) | Meta |
| 김수창 | Ph.D. (2023) | 충북대학교 |
| 김준우 | M.S. (1998) | ETRI |
| 김용수 | M.S. (1999) | TLI |
| 김윤환 | M.S. (1999) | 삼성전자 |
| 이승왕 | M.S. (1999) |  |
| 김태민 | M.S. (2000) | GCT Research |
| 김선영 | M.S. (2001) |  |
| 김진석 | M.S. (2002) | LG전자 |
| 서보익 | M.S. (2002) | KAIST |
| 문상철 | M.S. (2003) | LG전자 |
| 김정욱 | M.S. (2004) | ARM |
| 이동수 | M.S. (2004) | IBM T.J. Watson Research Center |
| 최용우 | M.S. (2004) | LG디스플레이 |
| 김기모 | M.S. (2005) | 삼성전자 |
| 김충효 | M.S. (2005) | 한국전력공사 |
| Shahid Rizwan | M.S. (2005) | Ericsson |
| 최혜미 | M.S. (2005) |  |
| 김범돌 | M.S. (2007) | SK Hynix |
| 전해수 | M.S. (2007) | 서울대학교 치의학전문대학원 |
| 권기석 | M.S. (2008) | 삼성종합기술원 |
| 이석호 | M.S. (2008) | LG전자 |
| 조원경 | M.S. (2008) | 삼성전자 |
| 배은주 | M.S. (2008) | 산업통상자원부 |
| 김성진 | M.S. (2009) | 서울대학교 치의학전문대학원 |
| 이정섭 | M.S. (2009) | TLI |
| 손원희 | M.S. (2009) | Timefolio |
| 유덕현 | M.S. (2009) | ETRI |
| Hasan Ahmed | M.S. (2009) | 삼성전자 |
| Avci, Celal | M.S. (2009) | Analog Devices |
| 유민수 | M.S. (2009) | KAIST |
| 박강우 | M.S. (2010) | SK Hynix |
| 심혜련 | M.S. (2010) | 삼성전자 |
| 김은찬 | M.S. (2011) | Marvell |
| 이재봉 | M.S. (2011) | 삼성전자 |
| 임고은 | M.S. (2011) | 부산대학교 치의학전문대학원 |
| 김창현 | M.S. (2012) | SK Hynix |
| 윤동준 | M.S. (2013) | SK Hynix |
| 장지원 | M.S. (2014) | 삼성전자 |
| 황미나 | M.S. (2014) | 삼성전자 |
| 김수현 | M.S. (2014) | 삼성전자 |
| 차소영 | M.S. (2014) |  |
| 전다현 | M.S. (2015) | 국방과학연구소 |
| 서영진 | M.S. (2015) | 삼성전자 |
| Charfi, Karim | M.S. (2015) | Healthrian |
| 이주승 | M.S. (2016) | 삼성전자 |
| 이진환 | M.S. (2016) | 카카오 |
| 여새동 | M.S. (2016) | 국방과학연구소 |
| 주영진 | M.S. (2017) | 삼성전자 |
| 최재준 | M.S. (2017) | 삼성전자 |
| 김현호 | M.S. (2018) | 삼성전자 |
| 노다영 | M.S. (2018) | 현대자동차 |
| 김대성 | M.S. (2018) | SK Hynix |
| 정혜원 | M.S. (2019) | 삼성전자 |
| 나승호 | M.S. (2020) | 아나패스 |
| 김우영 | M.S. (2020) | 티맥스소프트 |
| 박재현 | M.S. (2020) | 삼성전자 |
| 최재웅 | M.S. (2021) | SK Hynix |
| 이경필 | M.S. (2021) | SK Telecom |
| 이성진 | M.S. (2021) | DEEPX |
| 최수영 | M.S. (2021) | SK Hynix |
| 박상범 | M.S. (2022) | SK Hynix |
| 양병규 | M.S. (2022) | SK Hynix |
| 박상수 | M.S. (2022) | SK Hynix |
| 현유진 | M.S. (2022) | SK Hynix |
| 배형준 | M.S. (2022) | KAIST |
| 이재영 | M.S. (2023) | 삼성전자 |
| 장보선 | M.S. (2023) | SK Hynix |
| 장혜정 | M.S. (2024) | 삼성전자 |
| 정석현 | M.S. (2024) | KAIST |
| 권재훈 | M.S. (2026) | SK Hynix |
| 백종민 | M.S. (2026) | 삼성전자 |
| 박민하 | M.S. (2026) | 삼성전자 |
| 우승주 | M.S. (2026) | SK Hynix |
| 윤지원 | M.S. (2026) | 모빌린트 |
| 정한솔 | M.S. (2026) | SK Hynix |
| 곽수훈 | M.S. (2026) | SK Hynix |

## 최근 논문 목록 (2021–2026)

누리집 International Journal 목록의 2021–2026년 학술지 논문 29편이다. 저자 순서와 제목·학술지 표기, 연도 구역은 누리집 그대로다. 2026년 구역의 두 편은 권·호 없이 Early Access(정식 호에 실리기 전 온라인으로 먼저 공개된 상태)로 적혀 있다. 누리집의 International Conference 목록은 2019년, Domestic Conference 목록은 2015년 항목까지 있어 이 기간의 학회 논문은 목록에 없다.[^pubs]

**2026**

- Hyeongseok Moon and In-Cheol Park. "Low-Complexity QC-LDPC Decoding Architecture with Dynamic-Range Compensation for Bitwidth Reduction". *IEEE Transactions on Circuits and Systems II: Express Briefs, Early Access*.
- Hansol Jeong, Jeongmin Kim, Jaehoon Kwon and In-Cheol Park. "High-Throughput and Area-Efficient Parallel Multimode BCH Encoder". *IEEE Transactions on Very Large Scale Integration (VLSI) Systems, Early Access*.
- Suhun Kwak and In-Cheol Park. "Lookahead Bit Flipping Decoding for Low-density Parity-check Codes". *IEEE Communications Letters, vol.30, no.1, pp.2929-2933*.
- Kangjoon Choi and In-Cheol Park. "Stratified Gaussian Sample Generation Architecture for Monte Carlo Simulation". *IEEE Transactions on Very Large Scale Integration (VLSI) Systems, vol.34, issue 10, pp.3254 - 3267, Oct. 2026*.
- Sungho Kim and In-Cheol Park. "Effective Bit Aware OEB-SCL Decoding of Polar Codes With Boundary-Consistent Multi-Bit Decoding". *IEEE Wireless Communications Letters, Vol.15 pp.4623 - 4627, Aug. 2026*.
- Jaehoon Kwon, Jeongmin Kim, Jeonghyeon Yoon, Hansol Jeong and In-Cheol Park. "A Hardware-Efficient Reed–Solomon Decoding Architecture for Single-Symbol Error Correcting in High-Bandwidth Memory". *IEEE Transactions on Very Large Scale Integration (VLSI) Systems, vol.34, issue 8, pp.2666 - 2670, Aug. 2026*.
- Hansol Jeong, Jeongmin Kim, Jaehoon Kwon and In-Cheol Park. "Area-efficient word-serial architecture for Hamming encoding and decoding". *Microprocessors and Microsystems, vol.122, no.105274, Jun. 2026*.
- Hyeongseok Moon and In-Cheol Park. "Hardware-Efficient QC-LDPC Decoding Architecture with Reduced Bit-Width and Saturation Management". *IEEE Transactions on Circuits and Systems II: Express Briefs, vol.73, issue 5, pp.553 - 557, May. 2026*.
- Kangjoon Choi and In-Cheol Park. "Enhanced-Throughput Antithetic Sample Generation Architecture for Monte Carlo Simulation". *IEEE Transactions on Very Large Scale Integration (VLSI) Systems, vol.34, issue 5, pp.1682 - 1686, May. 2026*.
- Jeongmin Kim, Kangjoon Choi, and In-Cheol Park. "Hardware-Efficient Unified Approximation for Implementing Diverse Smooth Activation Functions". *IEEE Transactions on Computers, vol.75, issue 5, pp.2106 - 2113, May. 2026*.
- Kangjoon Choi, Jongmin Baek, and In-Cheol Park. "General-Purpose QC-LDPC Processor for Error-Correction Performance Evaluation". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol.73, issue 7, pp.4888 - 4901, July. 2026*.

**2025**

- Jaehoon Kwon, Hansol Jeong, Jeongmin Kim, and In-Cheol Park. "Low-Complexity Bit-Error Rate Evaluation of Algebraic Codes". *IEEE Communications Letters, vol.30, no.1, pp.110-114*.
- Seungju Woo, Sungho Kim, Minha Park, and In-Cheol Park. "Error Probability of Multi-Bit Nodes in Polar Codes Considering Effective Bit Count". *IEEE Communications Letters, vol.29, no.11, pp.2646-2650, Nov. 2025*.
- Jeongmin Kim, Jaehoon Kwon, Hansol Jeong, and In-Cheol Park. "Energy-Efficient Syndrome Calculation Architecture for BCH Decoders". *IEEE Transactions on Very Large Scale Integration (VLSI) Systems, vol. 33, no. 9, pp.2488 - 2496, Jul. 2025*.
- In-Cheol Park, Kangjoon Choi, Hyejung Jang, and Jongmin Baek. "Multiple-Resolution Decoding Architecture for QC-LDPC Codes". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol.72, no.11 pp.7211-7224, Nov. 2025*.
- In-Cheol Park, Seungju Woo, Jaeyoung Lee, Minha Park and Sangbeom Park. "Multi-Bit Successive Cancellation List Decoding of Polar Codes Using One-Bit Error Boundary". *IEEE Communications Letters, vol. 29, pp.1350-1354, Jun. 2025*.
- Sungho Kim, Jeongmin Kim and In-Cheol Park. "High-Speed CMOS Synchronous Binary Counter with Constant Counting Rate". *IEEE Access, vol. 13, pp. 53347-53355, Mar. 2025*.
- Kangjoon Choi and In-Cheol Park. "Hardware-Efficient Architecture for Multiple Quantized Gaussian Noise Generation". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 72, no. 8, pp.4064 - 4076, Jan. 2025*.

**2024**

- Jeongmin Kim, Sungho Kim, Kangjoon Choi, and In-Cheol Park. "Hardware-Efficient SoftMax Architecture With Bit-Wise Exponentiation and Reciprocal Calculation". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 71, no. 10, pp.4574-4585, Oct. 2024*.
- Kangjoon Choi, Sungho Kim, Jeongmin Kim, and In-Cheol Park. "Hardware-Friendly Approximation for Swish Activation and Its Implementation". *IEEE Transactions on Circuits and Systems II: Express Briefs, vol. 71, no. 10, pp.4516-4520, Oct. 2024*.
- Boseon Jang, Hyejung Jang, Sungho Kim, Kangjoon Choi, and In-Cheol Park. "Area-Efficient QC-LDPC Decoding Architecture With Thermometer Code-Based Sorting and Relative Quasi-Cyclic Shifting". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 71, no. 6, pp.2897-2910, Apr. 2024*.

**2023**

- Suchang Kim, Boseon Jang, Jaeyoung Lee, Hyungjoon Bae, Hyejung Jang, and In-Cheol Park. "A CNN Inference Accelerator on FPGA With Compression and Layer-Chaining Techniques for Style Transfer Applications". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 70, no. 4, pp.1591-1604, Jan. 2023*.

**2022**

- Jaehyeon Park, Jaeyoung Lee, and In-Cheol Park. "In Situ Multi-Bit Decision for Successive Cancellation List Decoding of Polar Codes". *IEEE Access, vol. 10, pp. 86943-86952, Aug 2022*.
- Hyungjoon Bae, Yujin Hyun, Suchang Kim, Sangsoo Park, Jaeyoung Lee, Boseon Jang, Suyoung Choi, and In-Cheol Park. "High-Speed Counter With Novel LFSR State Extension". *IEEE Transactions on Computers, vol. 72, no. 3, pp.893-899, Jun. 2022*.
- Seongjin Lee, Sangsoo Park, Boseon Jang, and In-Cheol Park. "Multi-Mode QC-LDPC Decoding Architecture with Novel Memory Access Scheduling for 5G New-Radio Standard". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 69, no. 5, pp.2035-2048, Feb. 2022*.

**2021**

- Wooyoung Kim, Yujin Hyun, Jaeyoung Lee, and In-Cheol Park. "Interleaved Local Sorting for Successive Cancellation List Decoding of Polar Codes". *IEEE Access, vol. 9, pp. 128623-128632, September 2021*.
- Yujin Hyun and In-Cheol Park. "Constant-time Synchronous Binary Counter with Minimal Clock Period". *IEEE Transactions on Circuits and Systems II: Express Briefs, vol. 68, no. 7, pp. 2645-2649, July 2021*.
- Suchang Kim, Seungho Na, Byeong Yong Kong, Jaewoong Choi, and In-Cheol Park. "Real-time SSDLite Object Detection on FPGA". *IEEE Transactions on Very Large Scale Integration (VLSI) Systems, vol. 29, no. 6, pp. 1192-1205, June 2021*.
- Suchang Kim, Jihyuck Jo, and In-Cheol Park. "Hybrid Convolution Architecture for Energy-Efficient Deep Neural Network Processing". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 68, no. 5, pp. 2017-2029, May 2021*.

## 과제

누리집 Projects 페이지가 진행 중(Current Projects)으로 적은 과제 2건이다. 수행 기간은 적혀 있지 않고, 괄호는 페이지가 적은 사업·지원 기관이다.[^projects] 같은 페이지의 Previous Projects에는 삼성전자의 Processing in Memory (PIM) Hardware Accelerator, 한국연구재단의 확장 가능한 저전력 멀티 모드 인공지능 프로세서 개발 등 27건이 기간 없이 적혀 있다.[^projects]

- 비대면·인공지능 사회를 위한 반도체/시스템 융합혁신기술 개발 (대학정보통신연구센터)
- 오류 정정 부복호 하드웨어 가속기를 생성하는 전문가 시스템 (한국연구재단)

## 소식

누리집 첫 화면 ICSL News의 5건(2026년 8–9월)이다. 날짜는 게시된 연·월이고 문장은 게시된 그대로다.[^home]

- 2026.09 · Hyeongseok Moon's paper is accepted by IEEE Transactions on Circuits and Systems II: Express Briefs.
- 2026.08 · Hansol Jeong's paper is accepted by IEEE Transactions on Very Large Scale Integration (VLSI) Systems.
- 2026.08 · Suhun Kwak's paper is accepted by IEEE Communications Letters.
- 2026.08 · Kangjoon Choi's paper is accepted by IEEE Transactions on Very Large Scale Integration (VLSI) Systems.
- 2026.08 · Sungho Kim's paper is accepted by IEEE Wireless Communications Letters.

## 연락과 위치

- 주소: Nano SoC #316, KAIST 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea[^contact]
- 위치: 나노종합기술원 (E19) 316호[^eeprof]
- 전화: +82-42-350-3461[^contact]
- 교수 이메일: icpark@kaist.edu[^contact][^eeprof]
- 연구실 대표(Lab Representative) 이메일: jmkim@ics.kaist.ac.kr[^contact]
[^p1]: S. Lee, S. Park, B. Jang, I.-C. Park, IEEE Transactions on Circuits and Systems I: Regular Papers 69, 2035-2048 (2022). <https://doi.org/10.1109/tcsi.2022.3150022> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: I.-C. Park 외, S. Park, IEEE Communications Letters 29, 1350-1354 (2025). <https://doi.org/10.1109/lcomm.2025.3561246> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Kwon 외, I.-C. Park, IEEE Transactions on Very Large Scale Integration (VLSI) Systems 34, 2666-2670 (2026). <https://doi.org/10.1109/tvlsi.2026.3692208> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: J. Kim, S. Kim, K. Choi, I.-C. Park, IEEE Transactions on Circuits and Systems I: Regular Papers 71, 4574-4585 (2024). <https://doi.org/10.1109/tcsi.2024.3443270> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: S. Kim 외, I.-C. Park, IEEE Transactions on Circuits and Systems I: Regular Papers 70, 1591-1604 (2023). <https://doi.org/10.1109/tcsi.2023.3234640> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: K. Choi, I.-C. Park, IEEE Transactions on Circuits and Systems I: Regular Papers 72, 4064-4076 (2025). <https://doi.org/10.1109/tcsi.2024.3524591> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: K. Choi, J. Baek, I.-C. Park, IEEE Transactions on Circuits and Systems I: Regular Papers 73, 4888-4901 (2026). <https://doi.org/10.1109/tcsi.2026.3652226> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: H. Bae 외, I.-C. Park, IEEE Transactions on Computers, 1-8 (2022). <https://doi.org/10.1109/tc.2022.3187343> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 집적 컴퓨터 시스템 연구실 누리집 첫 화면 <https://ics.kaist.ac.kr/> (연구실 소개, 연구 분야, ICSL News, 2026-10-22 열람)
[^intro]: 집적 컴퓨터 시스템 연구실 누리집 Introduction 페이지 <https://ics.kaist.ac.kr/introduction.php> (History, 2026-10-22 열람)
[^research]: 집적 컴퓨터 시스템 연구실 누리집 Research 페이지 <https://ics.kaist.ac.kr/research.php> (연구 분야 일곱 갈래, 2026-10-22 열람)
[^ai]: 집적 컴퓨터 시스템 연구실 누리집 Research 하위 페이지(AI Processor) <https://ics.kaist.ac.kr/research_ai.php> (2026-10-22 열람)
[^soc]: 집적 컴퓨터 시스템 연구실 누리집 Research 하위 페이지(Embedded SoC) <https://ics.kaist.ac.kr/research_soc.php> (2026-10-22 열람)
[^chip]: 집적 컴퓨터 시스템 연구실 누리집 Chip Gallery 페이지 <https://ics.kaist.ac.kr/chip.php> (2026-10-22 열람)
[^projects]: 집적 컴퓨터 시스템 연구실 누리집 Projects 페이지 <https://ics.kaist.ac.kr/project.php> (Current Projects, Previous Projects, 2026-10-22 열람)
[^pubs]: 집적 컴퓨터 시스템 연구실 누리집 Publications 메뉴: International Journal <https://ics.kaist.ac.kr/paper_intj.php>, International Conference <https://ics.kaist.ac.kr/paper_intc.php>, Domestic Conference <https://ics.kaist.ac.kr/paper_domc.php> (목록 범위는 근거 페이지, 2026-10-22 열람)
[^members]: 집적 컴퓨터 시스템 연구실 누리집 Members 페이지 <https://ics.kaist.ac.kr/members_2023.php> (Ph.D. Course, M.S. Course, Ph.D. Alumni, M.S. Alumni, 2026-10-22 열람)
[^prof]: 집적 컴퓨터 시스템 연구실 누리집 교수 페이지 <https://ics.kaist.ac.kr/member_icpark.php> (Personal Data, Background, 2026-10-22 열람)
[^class]: 집적 컴퓨터 시스템 연구실 누리집 Class 페이지 <https://ics.kaist.ac.kr/class.php> (2026-10-22 열람)
[^contact]: 집적 컴퓨터 시스템 연구실 누리집 Contact 페이지 <https://ics.kaist.ac.kr/contact.php> (2026-10-22 열람)
[^eeprof]: KAIST 전기및전자공학부 교수 소개(박인철) <https://ee.kaist.ac.kr/professor/12192/> (주요 연구분야, 주요 연구, 소속연구실, 위치, 이메일, 디비전, 학위, 대표업적, 2026-10-22 열람)
[^eelist]: KAIST 전기및전자공학부 교수진 목록 <https://ee.kaist.ac.kr/professor-s1/> (박인철 항목의 직위, 2026-10-22 열람)
[^ssel]: KAIST 반도체시스템공학과 연구실 목록 <https://sse.kaist.ac.kr/research-laboratory/> (집적 컴퓨터 시스템 연구실 항목, 2026-10-22 열람)
[^ssep]: KAIST 반도체시스템공학과 교수진 <https://sse.kaist.ac.kr/professor/> (박인철 교수 항목, 2026-10-22 열람)

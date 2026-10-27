# VLSI 연구실 (KAIST VLSI Research Lab)

**KAIST 전기및전자공학부·반도체시스템공학과·AI시스템학과 · 김봉진 교수**

- 분야: VLSI 회로 및 칩 설계, 차세대 컴퓨팅 및 통신회로 설계, 도메인·용도 특화 하드웨어 가속기 설계, 물리 영감 계산(이징 머신·볼츠만 머신·확률 컴퓨팅), 신경망 형식 검증 가속기, 유선 통신 회로, 메모리·칩렛 링크, 대규모 메모리 내 연산
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 집적회로 설계[^home][^ee][^p1], AI 반도체·가속기[^home][^p2], 확률 컴퓨팅[^home][^news], 메모리 내 연산[^home][^p2], 고속 유선 인터페이스[^home][^prof], 이징 머신·물리 기반 계산[^p1]
- 홈페이지: <http://bongjin.com> (Google Sites 누리집 <https://sites.google.com/view/mslab>로 이어짐)
- 근거와 출처: [KAIST VLSI Research Lab 근거 페이지](bongjin-sources.md)

> 계산과 통신을 맡는 집적회로와 시스템을 칩으로 설계해 만드는 연구실이다. 물리 현상에서 착안해 최적화 문제를 푸는 이징 칩, 신경망을 검증하거나 특정 계산을 빠르게 하는 전용 가속기, 칩과 메모리를 잇는 유선 통신 회로, 메모리 안에서 계산하는 구조를 연구한다.[^home][^prof]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 김봉진 부교수가 이끄는 VLSI(초고집적 회로, 트랜지스터를 칩 하나에 높은 밀도로 모아 넣는 회로) 설계 연구실이다.[^ee][^prof] 전기및전자공학부 교수 소개는 소속 연구실을 VLSI Research Lab으로, 주요 연구를 VLSI 회로 및 칩 설계, 차세대 컴퓨팅 및 통신회로 설계, 도메인·용도 특화(Domain/Application-Specific) 하드웨어 가속기 설계로 적는다.[^ee] 반도체시스템공학과 연구실 목록에도 같은 이름과 주요 연구로 올라 있다.[^ssel] 교수는 2025년 1월 KAIST에 부임했고, 그 전에는 미국 UC Santa Barbara(2021–2024)와 싱가포르 난양공대(NTU, 2017–2020)의 조교수였다.[^prof] 누리집 소식은 UC Santa Barbara의 Kim Circuit Research Lab이 2025년 1월 KAIST 전기및전자공학부로 옮겨 온다고 알렸고, KAIST에서는 연구실을 KAIST VLSI Lab으로 부른다.[^news]

누리집은 연구를 계산과 통신을 맡는 최첨단(cutting-edge) 집적회로·시스템 연구로 소개하고 여섯 갈래를 든다.[^home] 첫째는 에너지 기반 AI 모델을 쓰는 물리 영감 계산(Physics-Inspired Computing)으로, 이징 머신(두 값 가운데 하나를 갖는 '스핀' 여럿이 서로 주고받는 영향을 계산해 전체 에너지가 가장 낮아지는 배치를 찾는 방식으로 문제를 푸는 계산기)·볼츠만 머신(확률에 따라 상태를 바꾸는 단위들이 서로 이어진 신경망 모형)·확률 컴퓨팅과 그 응용이다. 둘째는 도메인 특화 AI 하드웨어 가속기(특정 계산을 빠르고 적은 전력으로 하도록 만든 전용 칩)로, 단백질 나노 구조 예측·설계, 물리 AI(Physical AI), AI·기계학습의 형식 검증(수학적으로 올바름을 보증하는 검사)과 모델 강건성을 다룬다. 셋째는 유선 통신 회로·구조·시스템 설계 기법이고, 넷째는 2.5·3차원 이종 집적(서로 다른 칩을 나란히 놓거나 쌓아 하나로 묶는 기술)과 고대역폭 메모리(HBM, 메모리 칩을 쌓아 한 번에 많은 데이터를 주고받게 만든 메모리)를 위한 메모리·칩렛(하나의 칩이 할 기능을 나눠 맡도록 따로 만든 칩 조각) 링크다. 다섯째는 칩 설계 자동화(EDA, 회로 설계를 소프트웨어로 돕는 도구)를 위한 AI, 여섯째는 대규모 메모리 내 연산(PIM, 데이터를 메모리 밖으로 옮기지 않고 메모리 안이나 가까이에서 계산하는 방식)이다.[^home]

KAIST로 옮긴 뒤의 소식을 보면 연구실은 칩을 계속 설계해 만들고 있다. 2025년 9월 KAIST에서의 첫 시험 칩(통산 32번째)을 28나노미터 FD-SOI(절연막 위에 얹은 실리콘층에 트랜지스터를 만드는 공정 방식) 공정용으로 설계했고, 2026년 7월에는 계산과 메모리에 쓰는 진짜 확률적(true probabilistic) 인공 뉴런 1,000개가 넘게 들어간 37번째 칩을, 2026년 8월에는 단백질 나노 구조를 예측하는 AI 하드웨어 가속기로는 연구실의 첫 칩인 38번째 칩을 테이프아웃(설계를 마쳐 제조 공정에 넘김)했다.[^news] 연구비로는 확장 가능한 응용 특화 물리 영감 이징 프로세서 개발(한국연구재단 우수신진, 2025), 매우 효율적인 대규모 이징 파운데이션 모델 개발(한국연구재단 기초연구실, 2025), ETRI(Electronics and Telecommunications Research Institute)와 함께하는 대규모 조합 최적화 문제용 차세대 CMOS+X(기존 CMOS 회로에 새로운 소자·기술을 더한 방식) 확률 컴퓨팅 칩 개발(글로벌 TOP 전략연구단, 2025), 기계학습 학습용 새 ASIC(특정 용도 전용 칩) 가속기 개발(C2 연구과제, 2025), 초대형 데이터센터의 AI 처리를 위한 메모리 중심 ASIC 가속기 개발(Panmnesia가 이끄는 IITP 과제, 2026)을 알렸다.[^news]

대표 논문으로 보면 KAIST 시기의 연구는 세 갈래로 모인다. 첫째, 스핀 하나가 다른 스핀 56개와 이어지는 디지털 이징 칩으로 무선 통신의 신호 검출 같은 조합 최적화 문제를 푼다(대표 논문 1).[^p1] 둘째, 신경망이 입력의 작은 변화에도 판단을 유지하는지를 수학적으로 검증하는 일을 전용 칩으로 처리하는 가속기를 만든다(대표 논문 2).[^p2] 셋째, 격자 모양으로 놓인 처리 소자들이 이웃과 데이터를 주고받으며 계산하는 그래프 가속기로 영상의 잡음과 그림자를 걷어 낸다(대표 논문 3).[^p3] 교수가 UC Santa Barbara에 있던 2021–2024년 논문 목록에는 CMOS 이징 머신과 불 만족 가능성(SAT, 참·거짓 조건식들을 모두 만족시키는 값이 있는지 묻는 문제) 풀이 칩, SRAM(칩에 함께 넣는 빠른 메모리) 기반 메모리 내 연산 매크로(칩 안에 넣는 회로 블록), 편미분방정식(공간과 시간에 따라 바뀌는 양을 다루는 방정식)을 푸는 비트 직렬(수를 한 비트씩 차례로 처리하는 방식) 계산 가속기가 주로 올라 있다.[^pubs]

## 주요 연구 주제

### 1. 물리 영감 계산: 이징 머신 칩

조합 최적화 문제(여러 선택지의 조합 가운데 가장 좋은 것을 고르는 문제)를 칩 위의 스핀 배치 문제로 바꿔 빠르게 푸는 이징 칩을 만든다. KAIST 시기에는 스핀 하나가 56개와 이어지고 연결 세기를 8비트로 나타내는 디지털 이징 칩(COBI)을 발표했다.[^p1] 누리집 소식은 2025년 VLSI 심포지엄에서 3차원 스핀 연결망 구조의 디지털 이징 칩(m-Zephyr)을 발표했다고 적는다.[^news][^pubs] 대표 논문 1.

### 2. 신경망 형식 검증 가속기

기호 구간 계산(입력이 가질 수 있는 범위를 기호로 놓고 출력이 가질 수 있는 범위를 계산하는 방법)으로 신경망의 강건성을 검증하는 전용 칩(Verifica)을 만들었다.[^p2] 누리집 소식은 기호 구간 계산을 쓴 두 번째 신경망 형식 검증 가속기(SYMBA)가 2026년 A-SSCC 발표로 채택됐다고 알렸다.[^news] 대표 논문 2.

### 3. 그래프·비트 직렬 계산 가속기

격자 모양 처리 소자 배열이 이웃끼리 데이터를 나눠 쓰며 계산하고, 필요한 정밀도만큼 비트를 하나씩 처리하는(비트 직렬) 가속기로 영상 보정 모형을 풀었다.[^p3] 대표 논문 3.

### 4. 메모리·칩렛 링크와 유선 통신 회로

누리집이 연구 범위로 드는 유선 통신 회로·구조·시스템 설계 기법과, 2.5·3차원 이종 집적과 고대역폭 메모리를 위한 메모리·칩렛 링크다.[^home] 교수 소개는 이를 2.5·3차원 이종 집적과 고대역폭 메모리를 위한 차세대 링크로 적는다.[^prof]

## 대표 논문

김봉진 교수가 KAIST에 부임한 2025년 1월 뒤 출판된 논문 가운데 교수가 마지막 저자이고 초록을 구할 수 있는 논문 세 편을 연구 갈래마다 한 편씩 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [COBI: A Degree-of-56 Column-Bipartite Densely Connected Digital Ising Chip with 8b Spin Coefficients](https://doi.org/10.1109/isscc49663.2026.11409141) · IEEE International Solid-State Circuits Conference (ISSCC) 2026 | 계산량이 많은 조합 최적화 문제를 칩에 옮겨 풀기 위한 65나노미터 디지털 이징 칩이다. 개선된 연결 구조(column-bipartite topology)로 스핀을 촘촘하게 이어, 스핀 하나가 56개 스핀과 연결되고 연결 세기(계수)를 8비트로 나타낸다. 스핀 처리 소자 64개를 넣고 스핀 계수를 유연하게 쓸 수 있는 내장 SRAM에 담은 시험 칩을 만들어, 무선 통신망의 MIMO 검출(여러 안테나로 주고받은 신호에서 보낸 데이터를 가려내는 일) 같은 실제 문제를 72나노초보다 짧은 시간에 풀어 보였다.[^p1] | 1저자 Y. Wu, 마지막 저자 김봉진 |
| 2 | 2026 | [Verifica: Near-Memory Symbolic Interval Computing Formal Neural Network Verification Accelerator](https://doi.org/10.1109/jssc.2026.3707324) · IEEE Journal of Solid-State Circuits | 안전이 중요한 곳에 기계학습을 쓰려면 신경망의 강건성(입력이 조금 바뀌어도 판단이 흔들리지 않는 성질)을 형식적으로 검증해야 하지만, 기존 검증 틀은 대부분 소프트웨어여서 계산 비용과 실행 시간이 지나치게 커 규모를 키우거나 실제로 쓰기 어렵다. 기호 구간 분석은 규모를 키울 수 있지만, ReLU(음수를 0으로 바꾸는 함수) 같은 비선형 활성화 함수 때문에 범위를 지나치게 넓게 잡고, 기존 컴퓨터에서는 데이터 이동이 비효율적이다. 연구진은 알고리즘과 하드웨어를 함께 설계해 기호 구간 기반 강건성 검증을 하는 첫 ASIC(특정 용도 전용 칩) 신경망 검증 가속기를 내놓았다. 신경망 출력을 입력 변수들의 기호 선형 결합으로 나타내고 계수를 전파해 범위를 좁게 계산하며, ReLU로 생기는 과대 근사는 조절 가능한 매개변수를 둔 선형 완화로 줄인다. 강건성을 바로 인증하지 못하면 ReLU 상태를 반복해 다듬어 적대적 예시(판단을 틀리게 만드는 입력)를 효율적으로 찾는다. 65나노미터 CMOS 공정에서 행·열 두 방향으로 접근할 수 있는 10T SRAM 기반 근접 메모리 계산 구조로 구현해, 데이터 이동을 최소로 하며 구간 연산과 계수 전파를 했다. 측정 결과 97%가 넘는 검증 가능률, 검증 한 번에 0.05–1.22 ms의 지연과 0.09–2.14 μJ의 에너지를 보였다.[^p2] | 1저자 E. J. Choi, 마지막 저자 김봉진 |
| 3 | 2025 | [A Graph-Based Accelerator of Retinex Model With Bit-Serial Computing for Image Enhancements](https://doi.org/10.1109/tcsi.2025.3525653) · IEEE Transactions on Circuits and Systems I: Regular Papers | 영상 보정에 쓰는 레티넥스 모형(사람이 보는 밝기를 빛의 세기와 물체 표면의 반사 성질로 나누어 설명하는 영상 모형)을 푸아송 방정식(어떤 양의 공간 분포를 그 원천으로부터 구하는 편미분방정식)으로 세우고, 격자 그래프 모양 처리 소자(PE) 배열에서 유한 차분 갱신(이웃 값과의 차이로 값을 조금씩 고쳐 가는 계산)을 하는 저전력 그래프 하드웨어 가속기로 풀었다. 알고리즘을 그래프 하드웨어 구조에 담아 처리 소자의 실제 배치를 살린 국소적인 데이터 흐름으로 데이터 이동을 줄이고 재사용을 늘렸다. 이웃 처리 소자끼리 데이터를 나누고 다시 쓰는 칩 안 데이터 흐름은 외부 제어 신호 두 개로 각 소자 안에서 만들어진다. 비트 직렬 계산용 누산기(값을 계속 더해 담아 두는 회로)를 따로 설계해 필요한 만큼의 정밀도와 칩 안 데이터 재사용을 적은 면적 부담으로 얻었고, 20×20 영상 조각 하나를 외부 메모리 접근 없이 한 번에 처리한다. 사용자가 정하는 갱신 횟수를 늘리면 영상의 잡음과 그림자가 점점 없어지지만 영상의 세부도 피할 수 없이 사라진다. 65나노미터 공정으로 만든 시험 칩은 코어 면적 0.2955mm²이고, 1V·25.6MHz에서 2.191mW를 쓰며 10비트나 14비트 정밀도로 바꿔 쓸 수 있다.[^p3] | 1저자 Z. Wei, 마지막 저자 김봉진 |

## 교수와 전문 분야

김봉진 교수(Bongjin Kim)는 KAIST 전기및전자공학부 부교수이다.[^ee] 누리집 교수 소개는 2025년 1월 KAIST에 부임해 전기및전자공학부(EE), AI시스템학과(AIS), 반도체시스템공학과(SSE)의 부교수(Associate Professor)로 있다고 적는다.[^prof] 전기및전자공학부 교수 소개의 디비전은 Circuit과 Computer이고,[^ee] 반도체시스템공학과 교수진 목록은 연구분야를 반도체 시스템 및 집적회로로,[^ssep] AI시스템학과 교수진 목록은 직위를 겸임교수로 적는다.[^ais]

포항공과대학교(POSTECH) 전기전자공학에서 학사(2004)와 석사(2006)를 받았고, 삼성전자 시스템LSI 사업부에서 설계 엔지니어로 일한 뒤(2006–2010), 미국 미네소타대학교에서 전기·컴퓨터공학 박사를 받았다(2014).[^prof][^ee] 박사과정 중 Rambus, IBM TJ Watson Research, Texas Instruments에서 연구 인턴을 했고, 박사 뒤에는 Rambus(Senior Member of Technical Staff II, 2015–2016)와 스탠퍼드대학교(박사후연구원, 2016–2017)에서 통신 회로와 마이크로아키텍처의 설계 기법을 연구했다.[^prof] 이어 싱가포르 난양공대 전기전자공학부 조교수(2017–2020)와 UC Santa Barbara 전기·컴퓨터공학과 조교수(2021–2024)를 지냈다.[^prof]

교수 소개는 연구 성과가 ISSCC, VLSI 심포지엄, CICC, ESSERC 같은 주요 학회와 IEEE Journal of Solid-State Circuits(JSSC) 등 동료 심사 학회·학술지에 70편 넘게 실렸다고 적는다.[^prof] 미국 국립과학재단(NSF)의 CAREER Award, 한국연구재단 우수신진 연구비(Outstanding Young Scientist Grant), 미네소타대학교 박사논문 펠로십(Doctoral Dissertation Fellowship), ISLPED International Low Power Design Contest Award를 받았다.[^prof] 누리집 수상 목록에는 2025년 KAIST 글로벌 연구 협력상 최우수상(Grand Prize)과 2026년 QAIST 창의도전연구상도 있다.[^awards] 학계 활동으로는 IEEE Solid-State Circuits Letters 부편집장(Associate Editor, 2024–), IEEE Open Journal of the Solid-State Circuits Society 객원 편집장(2025), ISSCC 기술 프로그램 위원(메모리 분과, 2026–)과 학생 연구 프리뷰 위원(2025–26), A-SSCC·ESSERC 기술 프로그램 위원(2025–), CICC 기술 프로그램 위원(2022–26)을 맡았고, A-SSCC 2026의 교육 프로그램 공동 의장을 맡았다.[^prof] IEEE Senior Member다.[^prof]

논문으로 보면 전문 분야는 시기에 따라 넓어졌다. 2011–2018년 논문은 위상 고정 루프(PLL, 기준 신호에 맞춰 일정한 주파수의 신호를 만드는 회로), 시간-디지털 변환기(TDC, 시간 간격을 디지털 값으로 바꾸는 회로), 아날로그-디지털 변환기(ADC, 아날로그 신호를 디지털 값으로 바꾸는 회로) 같은 클록·데이터 변환 회로가 중심이다.[^pubs] 2019–2024년에는 SRAM 기반 메모리 내 연산 매크로, CMOS 이징 머신과 어닐링 프로세서(무작위성을 점차 줄여 가며 에너지가 낮은 상태를 찾는 계산기), 편미분방정식을 푸는 비트 직렬 계산 가속기로 옮겨 왔다.[^pubs] KAIST 시기에는 디지털 이징 칩과 신경망 형식 검증 가속기, 그래프 가속기 연구가 이어진다(대표 논문 1–3).[^p1][^p2][^p3]

## 응용 분야

대표 논문이 직접 든 쓰임은 다음과 같다. 이징 칩으로 무선 통신망의 MIMO 검출 같은 실제 문제를 푸는 일,[^p1] 안전이 중요한 곳에 쓰는 기계학습 시스템의 강건성을 빠르고 적은 에너지로 형식 검증하는 일,[^p2] 영상의 잡음과 그림자를 걷어 내는 영상 보정이다.[^p3] 누리집은 가속기의 응용으로 단백질 나노 구조 예측·설계와 물리 AI를 들고,[^home] 2026년 8월에 단백질 나노 구조를 예측하는 가속기 칩을 테이프아웃했다고 알렸다.[^news]

누리집 소식에는 산업·창업과의 연결도 보인다. 파네시아가 이끄는 IITP 과제로 UALink 같은 고대역폭·저지연 개방형 고속 연결 기술을 쓰는 초대형 데이터센터용 메모리 중심 ASIC 가속기를 개발하고, KAIST Institute for IT Convergence의 지원으로 차세대 AI 반도체를 위한 비전통 컴퓨팅(Unconventional Computing) 기반 창업을 목표로 하는 연구 과제를 시작했으며, 같은 연구소의 예비창업 프로그램으로 비전통 메모리를 개발한다고 적는다.[^news] 연구비 목록에는 삼성전자 시스템LSI 사업부(2025–)와 SK하이닉스 DRAM PE(2026–)의 산학 연구비가 있다.[^awards] UC Santa Barbara 시기에는 미국 SLAC National Accelerator Laboratory와 함께 시험 칩을 설계하고 CMOS 기반 시뮬레이션 이징 머신으로 입자 궤적 추적 문제를 다룬 발표를 했다.[^news][^pubs]

## 구성원

누리집 MEMBERS 페이지의 KAIST 박사과정(PhD Students)·석사과정(MS Students)·인턴(Researcher & Undergraduate Interns) 칸과 UC Santa Barbara 대학원생(Graduate Students (UCSB)) 칸의 구성원이다. 과정·시작 시점·연구 주제는 페이지 표기 그대로다.[^members] 시작이 2027년 2월로 적힌 10명은 누리집 소식이 2027년 봄학기에 들어오는 학생으로 알린 사람이다.[^news] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Yeonjung Hwang (황연중) | 박사과정 | Feb. 2025- | Ising Processor Core Design, Probabilistic Computing with Energy-based AI Models |  |
| Shin-Uk Kang (강신욱) | 박사과정 | Feb. 2026- | Large-Scale Processing-in-Memory (PIM) & AI/ML Verification Accelerators |  |
| Seunghun Shin (신승헌) | 박사과정 | Feb. 2027- | Probabilistic Computing for Wireless Comm, MIMO Detection/Channel Estimation | 1 |
| Hyun Woo Seong (성현우) | 석박사통합과정 | Feb. 2025- | Chiplet & Memory Interface, Simultaneous Bidirectional Link Circuits/Architecture |  |
| Jiho Shin (신지호) | 석박사통합과정 | Aug. 2025- | Unconventional Memory Algorithm, Architecture, and Circuit Co-Design |  |
| Sang-Hyeok Boo (부상혁) | 석박사통합과정 | Feb. 2026- | AI/ML Hardware Accelerators for Protein Nanostructure Predictions & Design |  |
| Yechan Lee (이예찬) | 석박사통합과정 | Feb. 2027- | Physics-Inspired Computing & Unconventional Memory |  |
| Yujin Byeon (변유진) | 석사과정 | Feb. 2025- | CMOS Latch-based Random Number Generators & Probabilistic Computing Units |  |
| Hyoung Gyu Park (박형규) | 석사과정 | Feb. 2025- | Chiplet & Memory Interface, ATE Signal Integrity, ML-based Wireline Techniques |  |
| Yumin Na (나유민) | 석사과정 | Feb. 2025- | Chiplet & Memory Interface, ATE Interface, Wireline Clock Data Compensation |  |
| Hyeonjoong Kim (김현중) | 석사과정 | Aug. 2025- | Ising Processor Core Design, AI/ML Hardware Accelerators for Video Generation |  |
| Jae Hyun Ryu (류재현) | 석사과정 | Aug. 2025- | CMOS Latch-based Probabilistic Computing Units & Ising Processing Core |  |
| Dongjun Jeon (전동준) | 석사과정 | Aug. 2025- | Next-Generation Circuits/Architecture for Memory Links Under Resonant Noise |  |
| Woojun Nam (남우준) | 석사과정 | Aug. 2025- | Gaussian Random Number Generations & Probabilistic Computing Units |  |
| Jaehyung Park (박재형) | 석사과정 | Aug. 2025- | Chiplet & Memory Interface, Simultaneous Bidirectional Link w/ ML Techniques |  |
| Seongwon Lee (이성원) | 석사과정 | Feb. 2026- | Next-Generation Memory Link Circuits/Architecture, HBM Interface Circuits |  |
| Gyuil Lim (임규일) | 석사과정 | Feb. 2026- | AI for Custom IC Design (Design Automation) and Ising Processor Architecture |  |
| Minseo Kim (김민서) | 석사과정 | Feb. 2026- | Chiplet & Memory Interface, Simultaneous Bidirectional Link Circuits/Architecture |  |
| Serim Yang (양세림) | 석사과정 | Feb. 2026- | Unconventional Memory Algorithm, Architecture, and Circuit Co-Design |  |
| Seohyun Jung (정서현) | 석사과정 | Feb. 2026- | Next-Gen DRAM Interface Circuits/Architecture, Signal-Integrity & I/O Co-Design |  |
| Jaehyun Ahn (안재현) | 석사과정 | Feb. 2026- | CMOS Latch-based Probabilistic Computing Units & Ising Processing Core |  |
| Youngseo Kim (김영서) | 석사과정 | Aug. 2026- | Ising Machine and Probabilistic Computing & Unconventional Memory |  |
| Taejung Kim (김태정) | 석사과정 | Aug. 2026- | AI for Custom IC Design (Design Automation for Memory & Chiplet Links) |  |
| Minwook Choi (최민욱) | 석사과정 | Aug. 2026- | Large-Scale Processing-in-Memory (PIM) & AI/ML Hardware Accelerators |  |
| Minseo Kim (김민서) | 석사과정 | Feb. 2027- |  |  |
| Yeon Ho No (노연호) | 석사과정 | Feb. 2027- |  |  |
| Hongjun Joo (주홍준) | 석사과정 | Feb. 2027- |  |  |
| Euichan Shin (신의찬) | 석사과정 | Feb. 2027- |  |  |
| Yeji Ryu (류예지) | 석사과정 | Feb. 2027- |  |  |
| Hyebin Ju (주혜빈) | 석사과정 | Feb. 2027- |  |  |
| Gwanhong Park (박관홍) | 석사과정 | Feb. 2027- |  |  |
| Jinho Yang (양진호) | 석사과정 | Feb. 2027- |  |  |
| Alex Yunsoo Berlocher | 인턴 | Aug. 2026- | Ising Model for Quantum Error Correction (Ising Calibration & Ising Decoding) |  |
| Yang Woo Lee (이양우) | 인턴 | Aug. 2026- | Chiplet & Memory Interface, Simultaneous Bidirectional Link w/ ML Techniques |  |
| Geonwoo Kim (김건우) | 인턴 | Aug. 2026- | AI for Circuit/Chip Design: Using Agent for Circuit and Chip Designs |  |
| Gunyong Lee (이건용) | 인턴 | Aug. 2026- | Unconventional Memory Algorithm, Architecture, and Circuit Co-Design |  |
| Yihao Wu | 박사과정 (UCSB) | Sep. 2023- | Ising/Potts Machine, ASIC Hardware Accelerator | 1 |

## 졸업생과 이전 구성원

누리집 MEMBERS 페이지의 두 졸업생 칸(Lab Alumni (Postdoc, PhD, and MS)와 Lab Alumni (Undergrad Interns, Researcher, Visiting Scholar))의 27명이다. 학위·과정 칸은 과정 표기와 그 과정을 밟은 곳(NTU, Singapore·UC Santa Barbara, CA·KAIST), 괄호 안은 기간이고, 진로 칸은 페이지 표기 그대로다. 진로 칸이 "from"으로 시작하면 들어오기 전의 소속을 적은 것이다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hyunjoon Kim (김현준) | PhD, NTU, Singapore (2018 - 22) | Staff Engineer, SLAC National Accelerator Lab at Stanford University, CA |
| Junjie Mu | PhD, NTU, Singapore (2018 - 22) | Architecture Engineer, Huawei Technologies, China |
| Yuqi Su | PhD, NTU, Singapore (2019 - 23) | Assistant Professor, Peking University (북경대), China |
| Chengshuo Yu | PhD, NTU, Singapore (2019 - 24) | Research Staff, Zhangjiang Lab, Chinese Academy of Science, China |
| Nabeel Najeeb | MS, NTU, Singapore (2019-20) | Advanced Micro Devices (AMD), Singapore |
| Shicheng Lyu | MS, NTU, Singapore (2019-20) | Huawei Technologies, Shanghai, China |
| Jooyoung Bae (배주영) | PhD, UC Santa Barbara, CA (2021 - 25) | Assistant Professor, Kwangwoon University (광운대), South Korea |
| Jonghyun Park (박종현) | MS, UC Santa Barbara, CA (2022-24) | from SK Hynix, South Korea |
| Beomseok Hah (하범석) | MS, UC Santa Barbara, CA (2023-25) | from SK Hynix, South Korea |
| Hyosik Kim (김효식) | MS, UC Santa Barbara, CA (2023-25) | from SK Hynix, South Korea |
| Chanwho Park (박찬후) | MS, UC Santa Barbara, CA (2023-25) | PhD Student, Georgia Institute of Technology, GA |
| Jisu Kwon (권지수) | Postdoc, KAIST (2025-26) | Assistant Professor, Korea National University of Transportation (국립한국교통대) |
| Samuel Ng | Undergrad, NTU, Singapore (2018) | Micron Technology, Singapore |
| Jaeho Lee (이재호) | Researcher, NTU, Singapore (2019-20) | PhD student, Georgia Institute of Technology, GA |
| Prof. Ilku Nam (남일구) | Visiting, UC Santa Barbara, CA (2022-23) | from Pusan National University (부산대) EE |
| Edward Choi (최종윤) | Visiting, UC Santa Barbara, CA (2023-24) | Assistant Professor, Ewha Womans University (이화여대), South Korea |
| Doeun Sim (심도은) | Visiting, UC Santa Barbara, CA (2024) | Samsung Electronics, South Korea |
| Sanghyun Lee (이상현) | Undergrad, KAIST (2025) | MS Student, KAIST EE |
| Seungjae Lee (이승재) | Undergrad, KAIST (2025) | MS Student, KAIST EE |
| Jeonghun Lee (이정훈) | Undergrad, KAIST (2025) | from KAIST EE |
| Junyoung Park (박준영) | Undergrad, KAIST (2025) | from KAIST EE |
| Sijae Park (박시재) | Undergrad, KAIST (2026) | from KAIST EE |
| Seyeong Kim (김세영) | Undergrad, KAIST (2026) | from KAIST SSE |
| Yee Wan Teh | G-EPSS Intern, KAIST (2025) | from University of Technology Malaysia, Malaysia |
| Jaeyoon Lim (임재윤) | Researcher, KAIST (2025) | MS student, Yonsei University EEE |
| Anton Senerpida | Visiting, KAIST (2025) | from University of Michigan, Ann Arbor |
| Dongyoon Kim (김동윤) | Researcher, KAIST (2025-26) | PhD student, Purdue University, West Lafayette, IN |

## 최근 논문 목록 (2021–2026)

누리집 PUBLICATIONS 페이지의 2021–2026년 연도 구역 45편, Books & Chapters 구역의 2022년 책과 책 속 장 4건, Design Contests, Workshops, & Demo/Poster Presentations 구역의 2025년 발표 1건이다. 연도는 페이지의 연도 구역이고 각 줄은 페이지 표기 그대로다(앞 대괄호는 학회·학술지 약칭과 연도). 2026년의 두 편은 게재 승인(accepted) 상태로 적혀 있다. 2021–2024년 항목은 교수가 UC Santa Barbara에 있던 때(2021–2024)의 논문이다.[^pubs][^prof]

**2026**

- [TCAS-I'26] Z. Wei, Y. Su, B. Dong, C. Wang, B. Kim, T. Kim, and Y. Zheng, "DexLattice: A 280 μm2/Vertex Programmable Random-Access Lattice Graph Accelerator for In-Situ Partial Differential Equation Edge Processing," IEEE Transactions on Circuits and Systems I: Regular Papers, 2026 (accepted)
- [A-SSCC'26] B. Choi, E. Choi, J. Chun, S. Kang, D. Kim, B. Kim, and M. Je, "SYMBA: A Symbolic Interval Accelerator for Adversarial Example Generation in Online Adversarial Fine-Tuning for Robust Edge AI," IEEE Asian Solid-State Circuits Conference, Nov. 2026 (accepted)
- [JSSC'26] E. Choi, B. Choi, J. Chun, M. Je, and B. Kim, "Verifica: Near-Memory Symbolic Interval Computing Formal Neural Network Verification Accelerator," IEEE Journal of Solid-State Circuits, 2026 [Invited: A-SSCC 2025 Special Issue]
- [ISSCC'26] Y. Wu, J. Bae, S. Shin, and B. Kim, "COBI: A Degree-of-56 Column-Bipartite Densely Connected Digital Ising Chip with 8b Spin Coefficients," IEEE International Solid-State Circuits Conference, Feb. 2026

**2025**

- [A-SSCC'25] E. Choi, C. Shim, B. Choi, J. Chun, M. Je, and B. Kim, "Verifica: A 65nm In-Memory Symbolic Interval Computing Accelerator for a Formal Neural Network Verification," IEEE Asian Solid-State Circuits Conference, Nov. 2025 [Invited to JSSC Special Issue]
- [VLSI'25] Y. Wu, J. Bae, C. Shim, and B. Kim, "m-Zephyr: A Digital In-Memory Ising Chip with 240 Spins Featuring Enhanced Connectivity Based on a Modified 3D Zephyr Topology," Symposia on VLSI Technology and Circuits, Jun. 2025
- [TCAS-I'25] Z. Wei, J. Mu, Y. Zheng, T. Kim, and B. Kim, "A Graph-Based Accelerator of Retinex Model With Bit-Serial Computing for Image Enhancements," IEEE Transactions on Circuits and Systems I: Regular Papers, Mar. 2025
- [ISSCC'25 SRP] Y. Wu, J. Bae, C. Shim, and B. Kim, "m-Zephyr: a Digital In-Memory Ising Chip with 240 Spins with Improved Connectivity with a Modified Zephyr Topology," IEEE International Solid-State Circuits Conference (ISSCC) 2025 Student Research Preview (SRP), San Francisco, USA, Feb. 2025 (Short-Presentation/Poster)

**2024**

- [CPAD'24] H. Kim, J. Bae, R. Bartoldus, A. Dragone, B. Kim, L. Rota, and A. Schwartzman, "Tackling Particle Tracking Problems Using CMOS-based Simulated Ising Machines," Coordinating Panel for Advanced Detectors Workshop, Nov. 2024
- [A-SSCC'24] Y. Su, A. Do, T. Kim, and B. Kim, "ROC-Spin: A 28nm 2,000 Ring-Oscillator-Collapse Spins for Solving Combinatorial Optimization Problems," IEEE Asian Solid-State Circuits Conference, Nov. 2024
- [SRC'24] C. Shim, C. Park, and B. Kim, "Design of Efficient Integer/Floating-Point Digital Compute-in-Memory Macro for Edge/Cloud Deep Learning with Reconfigurable Computing Precisions and Precision-Adaptive Approximation," SRC TECHCON, Sep. 2024
- [TCAS-I'24] C. Yu, H. Jiang, J. Mu, K. Chai, T. Kim, and B. Kim, "A Dual 7T SRAM-Based Zero-Skipping Compute-In-Memory Macro with 1-6b Binary Searching ADCs for Processing Quantized Neural Networks," IEEE Transactions on Circuits and Systems I: Regular Papers, Aug. 2024
- [JSSC'24] J. Mu, C. Yu, T. Kim, and B. Kim, "A Scalable and Reconfigurable Bit-Serial Compute-Near-Memory Hardware Accelerator for Solving 2D/3D Partial Differential Equations," IEEE Journal of Solid-State Circuits, Aug. 2024
- [JSSC'24] Y. Su, T. Kim, and B. Kim, "FlexSpin: A CMOS Ising Machine with 256 Flexible Spin Processing Elements with 8b Coefficients for Solving Combinatorial Optimization Problems," IEEE Journal of Solid-State Circuits, Aug. 2024
- [NICE'24] S. Bezugam, Y. Wu, J. Yoo, D. Strukov, and B. Kim, "Quantized Context Based LIF Neurons for Recurrent Spiking Neural Networks in 45nm," Neuro-Inspired Computational Elements Conference, Apr. 2024 [Arxiv]
- [ISSCC'24] C. Shim, J. Bae, and B. Kim, “VIP-Sat: A Boolean Satisfiability Solver Featuring 5x12 Variable In-Memory Processing Elements with 98% Solvability for 50 Variables 218 Clauses 3-SAT Problems,” IEEE International Solid-State Circuits Conference, Feb. 2024
- [ISSCC'24] J. Bae, C. Shim, and B. Kim, “e-Chimera: A Scalable SRAM-based Ising Macro with Enhanced Chimera Topology for Solving Combinatorial Optimization Problems Within Memory,” IEEE International Solid-State Circuits Conference, Feb. 2024
- [ISSCC'24] J. Bae\*, J. Koo\*, C. Shim\*, and B. Kim, “LISA: A 576x4 All-in-One Replica Spins Continuous-Time Latch-based Ising Computer Using Massively Parallel Random Number Generations and Replica Equalizations,” IEEE International Solid-State Circuits Conference, Feb. 2024 (\*equal contribution)
- [JSSC'24] J. Bae\*, W. Oh\*, J. Koo, C. Yu, and B. Kim, "CTLE-Ising: A Continuous-Time Latch-Based Ising Machine Featuring One-Shot Fully-Parallel Spin Updates and Equalization of Spin States," IEEE Journal of Solid-State Circuits, Jan. 2024 (\*equal contribution) [Invited: ISSCC 2023 Special Issue]

**2023**

- [SSCL'23] Y. Su, T. Kim, and B. Kim, "A Reconfigurable CMOS Ising Machine with Three-Body Spin Interactions for Solving Boolean Satisfiability with Direct Mapping," IEEE Solid-State Circuits Letter, Aug. 2023 [Invited: CICC 2023 Special Issue]
- [JSSC'23] C. Yu, J. Mu, Y.Su, K. Chai, T. Kim, and B. Kim, "A Time-Domain Wavefront Computing Accelerator with a 32×32 Reconfigurable PE Array," IEEE Journal of Solid-State Circuits, Aug. 2023
- [VLSI'23] J. Mu, C. Yu, T. Kim, and B. Kim, "A Bit-Serial Computing Accelerator for Solving Coupled Partial Differential Equations," Symposia on VLSI Technology and Circuits, Jun. 2023
- [ISCAS'23] Z. Wei, J. Mu, Y. Zheng, T. Kim, and B. Kim, "A Graph-Based Accelerator of Retinex Model with Bit-Serial Computing for Image Processing," IEEE International Symposium on Circuits and Systems, May 2023
- [ISCAS'23] Q. Zang, W. Goh, L. Lu, C. Yu, J. Mu, T. Kim, B. Kim, A. Mani, and A. Do, "282-to-607 TOPS/W, 7T-SRAM Based CiM with Reconfigurable Column SAR ADC for Neural Network Processing," IEEE International Symposium on Circuits and Systems, May 2023
- [CICC'23] Y. Su, T. Kim, and B. Kim, "A Reconfigurable Ising Machine for Boolean Satisfiability Problems Featuring Many-Body Spin Interactions," IEEE Custom Integrated Circuits Conference, Apr. 2023 [Invited to SSCL Special Issue]
- [CICC'23] C. Yu, J. Mu, K. Chai, T. Kim, and B. Kim, "A Continuous-Time Ising Machine Using Coupled Inverter Chains Featuring Fully-Parallel One-Shot Spin Updates," IEEE Custom Integrated Circuits Conference, Apr. 2023
- [TCAS-I'23] H. Kim, J. Mu, C. Yu, T. Kim, and B. Kim, "A 1-16b Reconfigurable 80Kb 7T SRAM-Based Digital Near-Memory Computing Macro for Processing Neural Networks," IEEE Transactions on Circuits and Systems I: Regular Papers, Apr. 2023
- [ISSCC'23] J. Bae\*, W. Oh\*, J. Koo, and B. Kim, "CTLE-Ising: A 1,440 Spins Continuous-Time Latch-based Ising Machine with One-Shot Fully-Parallel Spin Updates Featuring Equalization of Spin States," IEEE International Solid-State Circuits Conference, Feb. 2023 (\*equal contribution) [Invited to JSSC Special Issue]
- [JSSC'23] J. Mu and B. Kim, "A Dynamic-Precision Bit-Serial Computing Hardware Accelerator for Solving Partial Differential Equations Using Finite Difference Method," IEEE Journal of Solid-State Circuits, Feb. 2023
- [JSSC'23] F. Tu, Y. Wang, Z. Wu, L. Liang, Y. Ding, B. Kim, L. Liu, S. Wei, Y. Xie, and S. Yin, "ReDCIM: Reconfigurable Digital Computing-In-Memory Processor with Unified FP/INT Pipeline for Cloud AI Acceleration," IEEE Journal of Solid-State Circuits, Jan. 2023

**2022**

- [JSSC'22] C. Yu, T. Yoo, K. Chai, T. Kim, and B. Kim, "A 65nm 8T SRAM Compute-In-Memory Macro with Column ADCs for Processing Neural Networks," IEEE Journal of Solid-State Circuits, Nov. 2022
- [ESSCIRC'22] J. Mu, C. Yu, T. Kim, and B. Kim, "A Scalable Bit-Serial Computing Hardware Accelerator for Solving 2D/3D Partial Differential Equations Using Finite Difference Method," IEEE European Solid-State Circuits Conference, Sep. 2022
- [JSSC'22] Y. Su, H. Kim, and B. Kim, "CIM-Spin: A Scalable CMOS Annealing Processor with Digital In-Memory Spin Operators and Register Spins for Combinatorial Optimization Problems," IEEE Journal of Solid-State Circuits, Jul. 2022
- [JETCAS'22] D. Kim, C. Yu, S. Xie, Y. Chen, J.-Y. Kim, B. Kim, J. Kulkarni, and T. Kim, "An Overview of Processing-in-Memory Circuits for Artificial Intelligence and Machine Learning," IEEE Journal on Emerging and Selected Topics in Circuits and Systems, Jun. 2022
- [TCAS-I'22] J. Mu, H. Kim, and B. Kim, "SRAM-Based In-Memory Computing Macro Featuring Voltage-Mode Accumulator and Row-by-Row ADC for Processing Neural Networks," IEEE Transactions on Circuits and Systems I: Regular Papers, Jun. 2022
- [JSSC'22] Y. Su, J. Mu, H. Kim, and B. Kim, "A Scalable CMOS Ising Computer Featuring Sparse and Reconfigurable Spin Interconnects for Solving Combinatorial Optimization Problems," IEEE Journal of Solid-State Circuits, Mar. 2022 [Invited: CICC 2021 Special Issue]
- [ISSCC'22] Y. Su, T. Kim, and B. Kim, "FlexSpin: A Scalable CMOS Ising Machine with 256 Flexible Spin Processing Elements for Solving Complex Combinatorial Optimization Problems," IEEE International Solid-State Circuits Conference, Feb. 2022
- [ISSCC'22] F. Tu, Y. Wang, Z. Wu, L. Liang, Y. Ding, B. Kim, L. Liu, S. Wei, Y. Xie, and S. Yin, "A 28nm 29.2TFLOPS/W BF16 and 36.5TOPS/W INT8 Reconfigurable Digital CIM Processor with Unified FP/INT Pipeline and Bitwise in-Memory Booth Multiplication for Cloud Deep Learning Acceleration," IEEE International Solid-State Circuits Conference, Feb. 2022
- [Springer'22] "Processing-in-Memory for AI: From Circuits to Systems," edited by J.-Y. Kim, B. Kim, and T. Kim, Springer, Jul. 2022 [Book]
- [Chapter 2] C. Yu, H. Kim, B. Kim, and T. Kim, "Backgrounds," in Processing-in-Memory for AI: From Circuits to Systems edited by J.-Y. Kim, B. Kim, and T. Kim, pp. 15-40, Jul. 2022 [Chapter]
- [Chapter 3] H. Kim, C. Yu, and B. Kim, "SRAM-Based Processing-in-Memory (PIM)," in Processing-in-Memory for AI: From Circuits to Systems edited by J.-Y. Kim, B. Kim, and T. Kim, pp. 15-40, Jul. 2022 [Chapter]
- [Chapter 8] J.-Y. Kim, B. Kim, and T. Kim, "Conclusion," in Processing-in-Memory for AI: From Circuits to Systems edited by J.-Y. Kim, B. Kim, and T. Kim, pp. 15-40, Jul. 2022 [Chapter]

**2021**

- [ESSCIRC'21] C. Yu, K. Chai, T. Kim, and B. Kim, "A Zero-Skipping Reconfigurable SRAM In-Memory Computing Macro with Binary-Searching ADC," IEEE European Solid-State Circuits Conference, Sep. 2021
- [JSSC'21] H. Kim, T. Yoo, T. Kim, and B. Kim, "Colonnade: A Reconfigurable SRAM-Based Digital Bit-Serial Compute-In-Memory Macro for Processing Neural Networks," IEEE Journal of Solid-State Circuits, Jul. 2021
- [VLSI'21] J. Mu, Y. Su, and B. Kim, "A 20x28 Spins Hybrid In-Memory Annealing Computer Featuring Voltage-Mode Analog Spin Operator for Solving Combinatorial Optimization Problems," Symposia on VLSI Technology and Circuits, Jun. 2021
- [CICC'21] C. Yu, Y. Su, J. Lee, K. Chai, and B. Kim, "A 32x32 Time-Domain Wavefront Computing Accelerator for Path Planning and Scientific Simulations," IEEE Custom Integrated Circuits Conference, Apr. 2021
- [CICC'21] Y. Su, J. Mu, H. Kim, and B. Kim, "A 252 Spins Scalable CMOS Ising Chip Featuring Sparse and Reconfigurable Spin Interconnects for Combinatorial Optimization Problems," IEEE Custom Integrated Circuits Conference, Apr. 2021 [Best Student Paper Candidate] [Invited to JSSC Special Issue]
- [OJCAS'21] Y. Chen, L. Lu, B. Kim, and T. Kim, "A Reconfigurable 4T2R ReRAM Computing In-Memory Macro for Efficient Edge Applications," IEEE Open Journal of Circuits and Systems, Feb. 2021
- [TCAS-I'21] C. Yu, T. Yoo, H. Kim, T. Kim, K. Chai, and B. Kim, "A Logic-Compatible eDRAM Compute-In-Memory with Embedded ADCs for Processing Neural Networks," IEEE Transactions on Circuits and Systems I: Regular Papers, Feb. 2021
- [ISSCC'21] J. Mu and B. Kim, "A 21x21 Dynamic-Precision Bit-Serial Computing Graph Accelerator for Solving Partial Differential Equations Using Finite Difference Method," IEEE International Solid-State Circuits Conference, Feb. 2021

## 연구비

누리집 AWARDS 페이지에서 연구비(Grant·연구과제)를 적은 2022년 이후 항목 10건이다. 이름과 연도는 페이지 표기 그대로다. 2022년 Samsung Electronics (Memory Business) 항목과 2023–25년 SRC 항목은 교수가 UC Santa Barbara에 있던 때 시작됐다.[^awards][^prof]

- 2026- · IITP Research Grant (K-Cloud Technology Development Project)
- 2026- · KAIST AI Semiconductor Startup Program Grant (인공지능반도체 스타트업 발굴 프로그램)
- 2026- · SK Hynix (DRAM PE) Research Grant (KAIST 클러스터 산학과제)
- 2025- · Samsung Electronics (System LSI Business) Research Grant (삼성전자 KAIST 신진산학과제)
- 2025- · Global Top Strategic Research Group (글로벌탑 초거대계산 반도체 전략연구단) Research Grant
- 2025- · National Research Foundation (NRF) Basic Research Lab (기초연구실) Research Grant
- 2025 · C2 (Creative and Challenging) Research Project Grant (C2 연구과제)
- 2025- · National Research Foundation (NRF) Outstanding Young Scientist (우수신진) Research Grant
- 2023-25 · Semiconductor Research Corporation (SRC) GRC AI Hardware Grant
- 2022 · Samsung Electronics (Memory Business) Research Grant

## 수상

누리집 AWARDS 페이지의 수상·선정 항목 가운데 2022년 이후 14건이다. 이름과 연도는 페이지 표기 그대로이고, "Advisee"는 교수가 지도한 학생의 수상이다. 2022–2024년 항목은 교수가 UC Santa Barbara에 있던 때의 것이다.[^awards][^prof]

- 2026 · QAIST Creative Challenge Research Award (창의도전연구상)
- 2026 · IEEE Solid-State Circuits Society (SSCS) Outstanding Reviewer
- 2025 · KAIST Global Research Cooperation Award Grand Prize (KAIST 글로벌 연구 협력상 최우수상)
- 2025 · Hyunsong-KAIST Research Upscaling Support Program Award (현송-카이스트 장비프로그램)
- 2025 · IEEE Solid-State Circuits Society (SSCS) Pre-Doctoral Achievement Award: Advisee – Jooyoung Bae
- 2024 · Invitation to JSSC Special Issue, IEEE Asian Solid-State Circuits Conference (A-SSCC)
- 2024 · National Science Foundation (NSF) Career Award
- 2024 · IEEE Solid-State Circuits Society (SSCS) Outstanding Reviewer
- 2024 · IEEE Solid-State Circuits Society (SSCS) Rising Star Award: Advisee – Yuqi Su
- 2024 · IEEE Solid-State Circuits Society (SSCS) Pre-Doctoral Achievement Award: Advisee – Chengshuo Yu
- 2023 · Women in Engineering, Science, and Technology Development Grant Award: Advisee – Junjie Mu
- 2023 · Invitation to SSCL Special Issue, IEEE Custom-Integrated Circuits Conference (CICC)
- 2023 · Invitation to JSSC Special Issue, IEEE International Solid-State Circuits Conference (ISSCC)
- 2022 · IEEE Solid-State Circuits Society (SSCS) Pre-Doctoral Achievement Award: Advisee – Yuqi Su

## 소식

누리집 첫 화면 소식 가운데 2021년 10월–2026년 10월 글 142건이다. 날짜는 글의 연월이고 문구는 누리집 표기 그대로다. 2024년 12월까지의 글은 교수가 UC Santa Barbara에 있던 때의 글이다.[^news][^prof]

- 2026-10 · Prof. Kim gave an invited talk "Physics-Inspired and Probabilistic Unconventional Computing and Memory" at the Special Session of "Korea-Japan Special Session for Advanced IC Designs" of the 23rd International SoC Conference, Incheon, South Korea on Oct. 12, 2026.
- 2026-09 · KAIST VLSI Lab will have another record number of 11 incoming PhD and MS graduate students in Spring 2027! Three PhD (including two MS+PhD) students: 신승헌/부상혁/이예찬 and eight MS students (including six EE, one AI-System, and one V-KEPSI program): 김민서/노연호/주홍준/신의찬/류예지/주혜빈/박관홍/양진호. Congratulations!
- 2026-08 · We have completed 38th chip tape-out using 28nm FD-SOI technology. This is our very first AI hardware accelerator chip that predicts a protein nanostructure.
- 2026-08 · Prof. Kim will co-chair a technical session of "Domain-Specific Accelerators" at 2026 IEEE Asian Solid-State Circuits Conference (A-SSCC) on Monday, Nov. 2, 2026.
- 2026-08 · Our 2nd formal neural network verification hardware accelerator work (SYMBA) based on symbolic interval computing method has been accepted for presentation at the 2026 IEEE Asian Solid-State Circuits Conference (A-SSCC), November 1-4, 2026, in Taichung, Taiwan! Congrats, Byeongseon!!
- 2026-07 · Prof. Kim will give an invited talk at a Special Session of "Korea-Japan Special Session for Advanced IC Designs" at the 23rd International SoC Conference to be held in Incheon, South Korea from Oct. 11 to 14, 2026.
- 2026-07 · Our Pre-Startup (예비창업) Program research on the development of Unconventional Memory has been featured at Electronic Times (전자신문). See the article here.
- 2026-07 · Prof. Kim gave an invited talk on "Physics-Inspired Unconventional Computing and Memory" at Panmnesia as one of the 2026 Panmnesia Distinguished Lecture series.
- 2026-07 · Prof. Kim will serve as an Educational Program Co-Chair (together with Prof. Seung-Tak Ryu) of IEEE A-SSCC 2026 to be held in Taichung, Taiwan from Nov. 1 to 4, 2026.
- 2026-07 · Jisu Kwon (Postdoc) will begin his academic career as a tenure-track assistant professor at Korea National University of Transportation in Aug. 2026. Congratulations!!
- 2026-07 · KAIST VLSI Lab will have 4 incoming graduate students (MS/PhD: 신지호, MS: 김영서/김태정/최민욱) in Fall 2026. Welcome!
- 2026-07 · We have completed 37th chip tape-out using 28nm LPP technology. We have integrated >1,000 true probabilistic artificial neurons for computing & memory purposes.
- 2026-06 · Our 14th Journal of Solid-State Circuits (JSSC) paper entitled "Verifica: Near-Memory Symbolic Interval Computing Formal Neural Network Verification Accelerator" has been published and is now available in IEEE Xplore Early Access.
- 2026-06 · Our research work on a symbolic interval computing hardware accelerator for neural network verification (Verifica) has been accepted for publication in the IEEE Journal of Solid-State Circuits (JSSC)! Congrats, Edward!!
- 2026-05 · We have completed the design of our 36th test chip using 28nm LPP technology. This tape-out is supported by Samsung Electronics Research Grant (삼성신진산학).
- 2026-04 · The inaugural Pre-Startup (예비창업) Program supported by KAIST Institute for IT Convergence has been kicked off [Announcement]!
- 2026-04 · The 1st international joint workshop supported by NRF Basic Research Lab (BRL) and JST ASPIRE Program with participants from KAIST (Prof. Bongjin Kim), University of Tokyo (Prof. Atsutake Kosuge & Prof. Ken Takeuchi), Institute of Science Tokyo (Prof. Masato Motomura & Prof. Daichi Fujiki), and Waseda University (Prof. Kazushi Kawamura) has been successfully held at University of Tokyo, Japan in April, 2026. We look forward to the next workshop to be held at KAIST, Spring 2027!
- 2026-04 · We have completed the design of our 35th test chip using 65nm LP technology. This chip will become a major milestone for our Physics-Inspired Computing research.
- 2026-04 · A competitive collaborative IITP research proposal (led by Panmnesia) has been selected! In this project, we will develop memory-centric ASIC hardware accelerators for AI processing at hyperscale datacenters using high-bandwidth low-latency open-standard high-speed interconnect technology including UALink [News Article].
- 2026-03 · Prof. Kim has been selected as a recipient of QAIST Creative Challenge Research Award (창의도전연구상) to be awarded at 2026 KAIST Research Day.
- 2026-03 · We will start a KAIST-Startup Research Project that aims to build a Startup based on Unconventional Computing for Next-Generation AI Semiconductor supported by KAIST Institute for IT Convergence.
- 2026-03 · We have completed the design of our 34th test chip, which will be fabricated using 28nm FD-SOI technology.
- 2026-02 · Two of our group alumni, Jooyoung Bae (PhD graduate) and Edward Choi (visiting PhD student) will begin their academic career as tenure-track assistant professors at Kwangwoon University and Ewha Womans University starting in March 2026. Congratulations and good luck with your future career!
- 2026-02 · Yihao has successfully presented our research work on a densely connected digital Ising chip (Session 10. Digital Processing & Circuit Techniques) at IEEE ISSCC 2026.
- 2026-01 · Prof. Kim has earned the distinction of Outstanding Reviewer by the IEEE Solid-State Circuits Society (SSCS).
- 2026-01 · We have completed the design of our 33rd test chip (the 2nd test chip @ KAIST) with four design cores integrated, which will be fabricated using 28nm LPP technology.
- 2025-12 · Our A-SSCC'25 paper (Verifica: A 65nm In-Memory Symbolic Interval Computing Accelerator for a Formal Neural Network Verification) has been invited to the IEEE Journal of Solid-State Circuits (JSSC), Special Issue of A-SSCC 2025!
- 2025-11 · Prof. Kim has been selected as one of the five 2025 KAIST Global Research Cooperation Award Grand Prize (글로벌 연구협력 최우수상) winners.
- 2025-11 · Our work on a densely-connected digital Ising chip has been accepted for regular presentation at the IEEE International Solid-State Circuits Conference (ISSCC) 2026, Feb. 15-19, 2026, in San Francisco, CA!!! Congratulations, Yihao!
- 2025-11 · Prof. Kim will serve as a co-chair of the technical session, "Memory Interface" at the IEEE ISSCC 2026 to be held in San Francisco, CA, from Feb. 15-19, 2026.
- 2025-11 · Edward Choi successfully presented our research work on the first-of-its-kind formal neural network verification hardware accelerator (Verifica) at the 2025 IEEE Asian Solid-State Circuits Conference (A-SSCC).
- 2025-10 · KAIST VLSI Lab will have a record number of incoming PhD and MS graduate students in Spring 2026! Two PhD (including one MS+PhD) students: 성현우/강신욱, and seven MS students: 이성원/부상혁/양세림/안재현/김민서/임규일/정서현. Congratulations! We are looking forward to meeting and working with you all!
- 2025-10 · Prof. Kim will serve as the chair of a technical session, "Session 15. Techniques for Emerging Hardware Accelerators," at the IEEE Asian Solid-State Circuits Conference (A-SSCC) to be held in Daejeon, South Korea, from November 2 to 5.
- 2025-09 · A Call for Papers has been announced for a Special Issue on Advanced Circuits, Architectures, and Systems for Next-Generation AI Processors (Submission Due: Dec. 14, 2025). Prof. Kim serves as a Guest Editor together with Prof. Kea-Tiong Tang (NTHU, Taiwan) and Prof. Francesco Conti (U of Bologna, Italy).
- 2025-09 · We have completed the design of our 32nd test chip (also, the 1st test chip @ KAIST), which will be fabricated using 28nm FD-SOI technology.
- 2025-09 · Jooyoung Bae (5th PhD alumnus) will join the Korea Institute of Science and Technology (KIST) as a postdoctoral researcher. Best wishes for your new role!
- 2025-08 · Dr. Jisu Kwon will join the KAIST VLSI group as a postdoctoral researcher on September 1st. Welcome!!
- 2025-08 · Prof. Kim will serve as a Guest Editor of the IEEE Open Journal of the Solid-State Circuits Society (OJ-SSCS) for the special section on AI Processors.
- 2025-08 · Our research work on the first-of-its-kind formal neural network verification hardware accelerator (Verifica) has been accepted for presentation at the 2025 IEEE Asian Solid-State Circuits Conference (A-SSCC), November 2-5, 2025, in Daejeon, South Korea! Congrats, Edward!!
- 2025-07 · We have 6 new graduate students (see the full list of group members) who will join the group in Aug. 2025. Welcome to KAIST VLSI Lab!
- 2025-06 · We are now a part of the Global TOP Strategic Research Group (글로벌 TOP 전략연구단), working together with ETRI (Electronics and Telecommunications Research Institute) for developing the next-generation CMOS+X probabilistic computing chip for solving large-scale combinatorial optimization problems.
- 2025-06 · Yihao Wu successfully presented our research work on a digital Ising chip with a 3D spin network topology at the 2025 Symposia on VLSI Technology and Circuits (VLSI).
- 2025-05 · Prof. Kim will serve as the chair of a technical session, "Large-scale In-memory Computing Chips," at the 51st IEEE European Solid-State Electronics Research Conference (ESSERC) to be held in Munich, Germany, from September 8 to 11.
- 2025-05 · Prof. Kim and his team have been selected as a highly competitive Basic Research Lab (기초연구실) for developing an extremely efficient large-scale Ising Foundation Model, which will be supported by the National Research Foundation (NRF)!
- 2025-03 · Our work on a new digital Ising chip with a 3-dimensional spin network topology has been accepted for presentation at the 2025 Symposia on VLSI Technology and Circuits (VLSI), June 8-12, 2025, in Kyoto, Japan!!! Congrats, Yihao!!
- 2025-03 · Prof. Kim currently serves as a Technical Program Committee (TPC) member of the IEEE International Solid-State Circuits Conference (ISSCC), IEEE Asian Solid-State Circuits Conference (A-SSCC), IEEE European Solid-State Electronics Research Conference (ESSERC), and IEEE Custom Integrated Circuits Conference (CICC).
- 2025-03 · We will start a C2 (Creative and Challenging) research project on developing a novel ASIC accelerator for ML training.
- 2025-03 · Jooyoung has successfully passed her Ph.D. defense at UCSB! Congratulations, (soon to be) Dr. Bae!!
- 2025-03 · Prof. Kim has been selected as a recipient of the Outstanding Young Scientist Grant (우수신진) from the National Research Foundation (NRF) for developing a scalable application-specific physics-inspired Ising processor.
- 2025-02 · Prof. Kim has been selected as a recipient of the Hyunsong-KAIST Research Upscaling Support Program. We appreciate the generous support of the Hyunsong Education and Culture Foundation, which will establish the advanced equipment setup for our AI hardware research.
- 2025-02 · Jooyoung received a prestigious 2024-25 SSCS Predoctoral Achievement Award and Yihao presented his research work at the Student Research Preview (SRP) session during the Sunday Evening Event at ISSCC 2025 (Feb. 16, 2025), San Francisco, CA.
- 2025-02 · Prof. Kim serves on the Organizing Committee of the 2025 IEEE Asian Solid-State Circuits Conference (A-SSCC) to be held in Daejeon, South Korea, in November 2025.
- 2025-01 · A TCAS-I paper entitled "A Graph-Based Accelerator of Retinex Model With Bit-Serial Computing for Image Enhancements" has been published and is now available in IEEE Xplore Early Access.
- 2025-01 · Prof. Kim joined KAIST as an Associate Professor in the School of Electrical Engineering (EE). We will have 12 new members (6 graduate and 6 undergrad. students) who will join the group in Feb. 2025. Welcome to KAIST VLSI Lab!
- 2024-12 · Our A-SSCC paper (ROC-Spin: A 28nm 2,000 Ring-Oscillator-Collapse Spins for Solving Combinatorial Optimization Problems) has been invited to the IEEE Journal of Solid-State Circuits (JSSC), Special Issue of A-SSCC 2024! Congrats, Yuqi!!
- 2024-12 · Jooyoung has been selected as a recipient of the prestigious 2024-2025 SSCS Predoctoral Achievement Award! Congrats, Jooyoung!!
- 2024-11 · Yuqi Su successfully presented our research work on a new type of mixed-signal Ising machine based on ring-oscillator-collapse circuits at the 2024 IEEE Asian Solid-State Circuits Conference (A-SSCC).
- 2024-10 · Prof. Kim will co-chair Session 2 (ML, Cryogenic, and Ising Machine) of ISSCC 2025 Student Research Preview (SRP), which will be held in San Francisco, CA, on Sunday, Feb. 16, 2025.
- 2024-10 · Yihao Wu will present a preview of his research work on Digital Ising Computing in ISSCC 2025 Student Research Preview (SRP).
- 2024-09 · Kim Circuit Research Lab will move to the School of Electrical Engineering (EE) of Korea Advanced Institute of Science and Technology (KAIST), Daejeon, South Korea, in January 2025.
- 2024-08 · Prof. Kim will give a tutorial on "ASIC Hardware Solvers for Compute-Intensive Optimization Problems" at the 2024 IEEE Asian Solid-State Circuits Conference (A-SSCC), Nov. 18-21, 2024, in Hiroshima, Japan. Here's the link to the tutorial webpage.
- 2024-08 · Prof. Kim has been invited to serve as a Student Research Preview (SRP) committee member of the 2025 IEEE International Solid-State Circuits Conference (ISSCC), which will be held in San Francisco, CA, on Feb. 2025.
- 2024-08 · Our work on a new type of mixed-signal Ising machine (ROC-Spin) using a novel Ring-Oscillator-Collapse spin circuit has been accepted for presentation at the 2024 IEEE Asian Solid-State Circuits Conference (A-SSCC), November 18-21, 2024, in Hiroshima, Japan!! Congrats, Yuqi!
- 2024-08 · We have completed the design of our 31st test chip (in collaboration with SLAC), which will be fabricated using 28nm technology.
- 2024-07 · Prof. Kim has been invited and will serve as a Technical Program Committee (TPC) member of the IEEE European Solid-State Electronics Research Conference (ESSERC) 2025, which will be held in Munich, Germany, on Sep. 2025.
- 2024-06 · Junjie Mu will join Huawei Technologies in Shanghai, China, as an Architecture Engineer in July 2024. Congratulations, Dr. Mu!
- 2024-06 · A TCAS-I paper entitled, "A Dual 7T SRAM-Based Zero-Skipping Compute-In-Memory Macro With 1-6b Binary Searching ADCs for Processing Quantized Neural Networks" has been published and is now available in IEEE Xplore Early Access.
- 2024-06 · Our work on a dual 7T analog SRAM-based Compute-in-Memory macro for quantized neural networks has been accepted for publication in IEEE Transactions on Circuits and Systems I: Regular Papers (TCAS-I)! Congratulations, Chengshuo!!
- 2024-05 · We have submitted the 30th test chip (MAY) for fabrication using 65nm technology.
- 2024-05 · Chengshuo Yu passed his final oral Ph.D. defense! Congratulations!! Dr. Yu will join the Zhangjiang Lab of the Chinese Academy of Science in Shanghai, China.
- 2024-04 · We have submitted the 29th test chip (ONE) for fabrication using 65nm technology.
- 2024-03 · Yuqi Su has been selected as one of the IEEE SSCS Rising Stars 2024.
- 2024-02 · A paper on Quantized Context-based Neurons for Recurrent Spiking Neural Networks has been accepted for presentation at the NICE (Neuro-Inspired Computational Elements) Conference 2024, Apr. 23-26, 2024, to be held in La Jolla, CA. This work is an outcome of the ECE 224A (VLSI Project Design) class I taught in the Fall quarter of 2023. Congrats, Sai and other co-authors!
- 2024-02 · Jooyoung and Chaeyun have successfully presented our research works on Ising Computing (Session 15. Embedded Memories & Ising Computing) and a Boolean Satisfiability Solver (Session 30. Domain-Specific Computing & Digital Accelerators) at IEEE ISSCC 2024.
- 2024-02 · Yuqi Su has joined the School of Electronic and Computer Engineering at Peking University as a Tenure-Track Assistant Professor. Many Congratulations, Professor Su!!!
- 2024-02 · A JSSC paper entitled "A Scalable and Reconfigurable Bit-Serial Compute-Near-Memory Hardware Accelerator for Solving 2-D/3-D Partial Differential Equations" has been published and is now available in IEEE Xplore Early Access.
- 2024-01 · Our work on a bit-serial compute-near-memory hardware accelerator for solving 2D/3D PDEs has been accepted for publication in the IEEE Journal of Solid-State Circuits (JSSC)! Congrats, Junjie!! This marks our 10th JSSC paper since we published our first JSSC paper in July 2021. JSSC is considered the foremost journal in the IEEE Solid-State Circuits Society (SSCS). We are proud of our previous/current group members!
- 2024-01 · A JSSC paper entitled "FlexSpin: A CMOS Ising Machine with 256 Flexible Spin Processing Elements with 8b Coefficients for Solving Combinatorial Optimization Problems" has been published and is now available in IEEE Xplore Early Access.
- 2024-01 · Prof. Kim has received the recognition of an Outstanding Reviewer by the IEEE Solid-State Circuits Society (SSCS).
- 2024-01 · Our work on a reconfigurable Ising machine (FlexSpin) has been accepted for publication in the IEEE Journal of Solid-State Circuits (JSSC)! Congrats, Yuqi!!
- 2024-01 · We have an incoming group member, Doeun Sim, a visiting MS student from EE, POSTECH, South Korea. Welcome to Santa Barbara!
- 2023-12 · Prof. Kim has received a prestigious NSF CAREER Award. We will develop unconventional ASIC hardware accelerators for scalable Ising computing to solve computationally intensive problems.
- 2023-12 · Prof. Kim has visited the ARTIC lab (Prof. Masato Motomura) at the Tokyo Institute of Technology (Tokyo Tech) and the Kuroda lab (Prof. Tadahiro Kuroda) at the University of Tokyo for research discussions and presentations.
- 2023-12 · Chengshuo has been awarded a prestigious IEEE SSCS Pre-Doctoral Achievement Award for 2024! Congratulations, Chengshuo!!
- 2023-11 · Prof. Kim has been invited and will serve as the Associate Editor of the IEEE Solid-State Circuits Letters (SSCL) starting Jan. 1, 2024.
- 2023-10 · Three papers (VIP-Sat, e-Chimera, and LISA) have been accepted for presentation at IEEE International Solid-State Circuits Conference (ISSCC) 2024, Feb. 18-22, 2024 in San Francisco, CA!!! Congratulations, Jooyoung, Chaeyun, and Jahyun!
- 2023-10 · An invited JSSC paper (ISSCC 2023 Special Issue), entitled "CTLE-Ising: A Continuous-Time Latch-Based Ising Machine Featuring One-Shot Fully Parallel Spin Updates and Equalization of Spin States," has been published and is now available in IEEE Xplore Early Access.
- 2023-09 · Our invited paper on the Continuous-Time Latch-based Ising Machine (CTLE-Ising) has been accepted for publication at the IEEE Journal of Solid-State Circuits (JSSC), Special Issue of ISSCC 2023! Congratulations, Jooyoung!!
- 2023-08 · Yuqi has successfully passed his Ph.D. defense! Congratulations, Dr. Su!!
- 2023-08 · An SSCL paper, "A Reconfigurable CMOS Ising Machine with ThreeBody Spin Interactions for Solving Boolean Satisfiability with Direct Mapping," has been published and is now available in IEEE Xplore Early Access.
- 2023-08 · Our invited paper on the Reconfigurable Ising machine for solving Boolean Satisfiability (SAT) Problems has been accepted for publication at IEEE Solid-State Circuits Letter (SSCL)! Congratulations, Yuqi!!
- 2023-06 · Junjie has successfully presented our work on Bit-Serial Coupled PDE Solver (Circuits Session 7. Digital Systems) at the 2023 Symposium on VLSI Technology and Circuits (VLSI) in Kyoto, Japan.
- 2023-06 · We have many incoming group members in Summer/Fall 2023 quarter. Yihao Wu (Ph.D. student), Chanwho Park, Beomseok Hah, Hyosik Kim (MS student), Edward Choi (Visiting Ph.D. student from KAIST) who will join in Fall, as well as Yudong Zhou (Remote intern, Zhejiang University), Jaebum Yoo (UCSB with MS degree), Ryan Hsieh, Haechan Park (UCSB BS students) who will work with us starting this Summer. Welcome everyone!
- 2023-06 · Our CICC paper (Reconfigurable Ising Machine for Boolean Satisfiability Problems) has been invited to the IEEE Solid-State Circuits Letters (SSCL), Special Issue of CICC 2023!
- 2023-05 · Chaeyun has received the Outstanding ECE Teaching Assistant Award for Spring 2022 - Winter 2023! Great job, Chaeyun!!
- 2023-05 · Hyunjoon and Junjie have successfully passed their Ph.D. defenses! Congratulations, Dr. Kim and Dr. Mu!!!
- 2023-04 · Our CTLE-Ising paper presented at the ISSCC 2023 has been featured as one of the highlighted papers in the IEEE Computer magazine article "Semiconductor Architectures Enable Compute in Memory." Read the article here.
- 2023-04 · Prof. Kim presented a special seminar on "Mixed-Signal/Digital Memory-Centric Computing" hosted by KAIST AI PIM Research Center.
- 2023-04 · We have successfully presented two quantum-inspired Ising machine papers (reconfigurable digital and continuous-time analog) at the IEEE CICC 2023 in San Antonio, TX.
- 2023-04 · Our ISSCC paper (CTLE-Ising: A Continuous-Time Latch-based Ising Machine) has been invited to the IEEE Journal of Solid-State Circuits (JSSC), Special Issue of ISSCC 2023!
- 2023-03 · Our work on bit-serial computing coupled PDE solver has been accepted for presentation at 2023 Symposia on VLSI Technology and Circuits (VLSI), June 11-16, 2023, in Kyoto, Japan!!! Congrats, Junjie and Chengshuo!!
- 2023-03 · Prof. Kim will chair Session 7 (Compute in Memory and Ising Machines) together with Prof. Yongpan Liu from Tsinghua University at the upcoming IEEE Custom Integrated Circuits Conference (CICC) 2023 on Apr. 24 (Monday), 2023, in San Antonio, TX. See the detailed schedule for the session here.
- 2023-03 · We have submitted 27th and 28th test-chips for fabrication on memory-centric/quantum-inspired computing using 65nm technology.
- 2023-02 · Jooyoung has successfully presented our work on CTLE-Ising: A Continuous-Time Latch-based Ising Machine (Session 7. SRAM Compute-in-Memory) at IEEE ISSCC 2023 in San Francisco, CA. The paper is selected as one of the top papers of ISSCC 2023 by the Memory Subcommittee.
- 2023-01 · A JSSC paper entitled, "A Time-Domain Wavefront Computing Accelerator With a 32x32 Reconfigurable PE Array," has been published and is now available in IEEE Xplore Early Access.
- 2023-01 · Two papers (SAT solver and Ising machine) have been accepted for lecture presentations at the IEEE Custom Integrated Circuits Conference (CICC) 2023, Apr. 23-26, 2023, in San Antonio, TX. Congratulations, Yuqi, Chengshuo, and all other co-authors!!
- 2023-01 · A TCAS-I paper entitled, "A 1-16b Reconfigurable 80Kb 7T SRAM-Based Digital Near-Memory Computing Macro for Processing Neural Networks," has been published and is now available in IEEE Xplore Early Access.
- 2023-01 · Our work on a time-domain wavefront computing accelerator has been accepted for publication in the IEEE Journal of Solid-State Circuits (JSSC)! Congrats, Chengshuo!!
- 2022-12 · Yuqi has been awarded a prestigious IEEE SSCS pre-doctoral achievement award for 2023! Congratulations, Yuqi!!!
- 2022-12 · Our work on SRAM-based digital near-memory computing macro has been accepted for publication at IEEE Transactions on Circuits and Systems I: Regular Papers (TCAS-I)! Congrats, Hyunjoon!!
- 2022-12 · Yuqi (PhD) started working at IME (Institute of Microelectronics), A\*STAR, Singapore as a full-time researcher. Congratulations, and wish you all the best in your new journey!
- 2022-11 · We are going to work on a new research project on DRAM interface circuits for AI/ML applications supported by Samsung Electronics.
- 2022-10 · Our SRC AI Hardware proposal has been selected for funding for 3 years! We are going to work on a research project on the design of a reconfigurable digital compute-in-memory macro/processor for edge/cloud DL acceleration.
- 2022-10 · Our work on a continuous-time latch-based Ising machine has been accepted for regular presentation at the IEEE International Solid-State Circuits Conference (ISSCC) 2023, Feb. 19-23, 2023 in San Francisco, CA!!! Congratulations, Jooyoung, Wonsik, and Jahyun!
- 2022-09 · Chengshuo has successfully presented our research work on Bit-Serial Computing Accelerator for Solving 2D/3D PDEs based on Numerical Methods at IEEE ESSCIRC 2022.
- 2022-09 · Hyunjoon (PhD) will join SLAC National Accelerator Lab at Stanford University (CA) as a full-time researcher, and Junjie (PhD) will work as a postdoc at Nanyang Technological University (Singapore). Congratulations, and wish you all the best for your next journey!
- 2022-07 · We have submitted our 26th test chip with IME (Institute of Microelectronics), A\*STAR, Singapore, using 28nm technology.
- 2022-07 · Prof. Kim's co-edited book, "Processing-in-Memory for AI: From Circuits to Systems" has been published and is currently available at Springer and other online bookstores including Amazon. The front book cover is available here.
- 2022-06 · We have 3 incoming group members in the Fall 2022 quarter at the UCSB. Chaeyun Shim (Ph.D. student), Jong Hyun Park (MS student), and Aditya Ramakrishnan (Undergraduate Project student). Look forward to working with our new group members!
- 2022-06 · A Special Issue on Revolution of AI and Machine Learning with Processing-in-Memory (PIM): from Systems, Architectures, to Circuits of the IEEE Journal on Emerging and Selected Topics in Circuits and Systems (JETCAS) has been published. Prof. Kim has served as a Guest Editor for the Special Issue. Guest Editorial is available here.
- 2022-05 · Our work on a scalable bit-serial computing hardware accelerator for solving 2D/3D partial differential equations has been accepted for presentation at IEEE European Solid-State Circuits Conference (ESSCIRC), September 19-22, 2022 in Milan, Italy! Congrats, Junjie!!
- 2022-05 · A JSSC paper entitled, "A Dynamic-Precision Bit-Serial Computing Hardware Accelerator for Solving Partial Differential Equations Using Finite Difference Method," has been published and is now available in IEEE Xplore Early Access.
- 2022-05 · Our work on Bit-Serial Computing Hardware Accelerator for solving Partial Differential Equations has been accepted for publication at IEEE Journal of Solid-State Circuits (JSSC)! Congrats, Junjie!! This year, we have four JSSC papers published/accepted, so far!
- 2022-05 · Jooyoung Bae (PhD student, UCSB) joined Kim Circuit Research Group. Welcome!
- 2022-04 · Prof. Kim will chair the Educational Session 1 (Analog Automation Techniques) at the upcoming IEEE Custom Integrated Circuits Conference (CICC) 2022. The Educational session will be held in a hybrid model (both in-person and online) on Apr. 24 (Sunday), 2022 in Newport Beach, CA. See the detailed schedule for the session here.
- 2022-04 · We have submitted the 24th/25th test chips on in-memory computing and analog Ising machine for fabrication using 65nm technology.
- 2022-04 · We have submitted the 22nd/23rd test chips on quantum-inspired computing for fabrication using 65nm technology.
- 2022-04 · A JSSC paper entitled, "A 65nm 8T SRAM Compute-in-Memory Macro With Column ADCs for Processing Neural Networks," has been published and is now available in IEEE Xplore Early Access.
- 2022-03 · Our work on 8T SRAM Compute-In-Memory Macro with Column ADCs has been accepted for publication at IEEE Journal of Solid-State Circuits (JSSC)! Congrats, Chengshuo!!
- 2022-03 · A JETCAS paper entitled, "An Overview of Processing-in-Memory Circuits for Artificial Intelligence and Machine Learning," has been published and is now available in IEEE Xplore Early Access.
- 2022-03 · A TCAS-I paper entitled, "SRAM-Based In-Memory Computing Macro Featuring Voltage-Mode Accumulator and Row-by-Row ADC for Processing Neural Networks," has been published and is now available in IEEE Xplore Early Access.
- 2022-02 · Yuqi has successfully presented our research work on FlexSpin: Scalable CMOS Ising Machine with Flexible Spin Processing Elements at IEEE ISSCC 2022. The recorded presentation video is currently available for your watching on the virtual ISSCC platform if you're registered.
- 2022-02 · We have submitted the 20th/21st test chips on the Maxwell equation solver and Ising machine for fabrication using 65nm.
- 2022-02 · Our work on SRAM-based voltage-mode in-memory computing has been accepted for publication at IEEE Transactions on Circuits and Systems I: Regular Papers (TCAS-I)! Congrats, Junjie!!
- 2022-01 · An invited JSSC paper (CICC 2021 Special Issue) entitled, "A Scalable CMOS Ising Computer Featuring Sparse and Reconfigurable Spin Interconnects for Solving Combinatorial Optimization Problems," has been published and is now available in IEEE Xplore Early Access.
- 2022-01 · A JSSC paper entitled, "CIM-Spin: A Scalable CMOS Annealing Processor with Digital In-Memory Spin Operators and Register Spins for Combinatorial Optimization Problems," has been published and is now available in IEEE Xplore Early Access.
- 2022-01 · Our invited paper on Sparse and Reconfigurable Ising machine has been accepted for publication at IEEE Journal of Solid-State Circuits (JSSC) in March, the Special Issue of CICC 2021! Congratulations, Yuqi!!
- 2021-12 · Our work on CIM-Spin: CMOS Ising machine (annealing processor) has been accepted for publication at IEEE Journal of Solid-State Circuits (JSSC)! Congrats, Yuqi!!
- 2021-12 · Prof. Kim serves as a Track Chair for New Memory Technology and Processing in Memory for AI at IEEE International Conference on Artificial Intelligence Circuits and Systems (AICAS) 2022, Jun. 13-15, 2022 in Incheon, South Korea.
- 2021-11 · We have submitted our 19th (ISA) test chip for fabrication using 65nm technology. Great efforts, Jinesh and Jahyun!
- 2021-10 · Two papers (including one collaborative work) have been accepted for regular presentation at IEEE International Solid-State Circuits Conference (ISSCC) 2022, Feb. 20-24, 2022 in San Francisco, CA!!!
- 2021-10 · Prof. Kim will co-chair an Educational Session on Analog Automation Techniques at IEEE Custom Integrated Circuits Conference (CICC) 2022, Apr. 24-27, 2022 in Newport Beach, CA.

## 연락과 위치

- 주소: E3-2 Building, KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon, Republic of Korea 34141[^contact]
- 교수 연구실: E3-2 Building 5228호, 학생 공간 5227호, 측정실(Measurement Lab) 5226호[^contact]
- 전화: +82-42-350-7479[^contact]
- 교수 이메일: bongjin@kaist.ac.kr[^ee]
[^p1]: Y. Wu, J. Bae, S. Shin, B. Kim, 2026 IEEE International Solid-State Circuits Conference (ISSCC), 182-184 (2026). <https://doi.org/10.1109/isscc49663.2026.11409141> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: E. J. Choi 외, B. Kim, IEEE Journal of Solid-State Circuits 61, 5282-5295 (2026). <https://doi.org/10.1109/jssc.2026.3707324> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: Z. Wei 외, B. Kim, IEEE Transactions on Circuits and Systems I: Regular Papers 72, 1346-1357 (2025). <https://doi.org/10.1109/tcsi.2025.3525653> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 연구실 누리집 첫 화면과 RESEARCH 페이지 <https://sites.google.com/view/mslab> , <https://sites.google.com/view/mslab/research> (연구 소개문, 2026-10-22 열람)
[^news]: 연구실 누리집 첫 화면의 연도별 소식 <https://sites.google.com/view/mslab> (2017–2026년 글 224건, 2026-10-22 열람)
[^prof]: 연구실 누리집 PROFESSOR 페이지 <https://sites.google.com/view/mslab/professor> (소개문, 경력, 학력, 학계 활동, 2026-10-22 열람)
[^members]: 연구실 누리집 MEMBERS 페이지 <https://sites.google.com/view/mslab/members> (구성원, 졸업생, 2026-10-22 열람)
[^pubs]: 연구실 누리집 PUBLICATIONS 페이지 <https://sites.google.com/view/mslab/publications> (논문 목록, 2026-10-22 열람)
[^awards]: 연구실 누리집 AWARDS 페이지 <https://sites.google.com/view/mslab/awards> (수상·연구비·학계 활동 목록, 2026-10-22 열람)
[^contact]: 연구실 누리집 CONTACT 페이지 <https://sites.google.com/view/mslab/contact> (2026-10-22 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(김봉진) <https://ee.kaist.ac.kr/professor/%ea%b9%80%eb%b4%89%ec%a7%84/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 이메일, 디비전, 학위, 2026-10-22 열람)
[^ssel]: KAIST 반도체시스템공학과 연구실 목록 <https://sse.kaist.ac.kr/research-laboratory/> (2026-10-22 열람)
[^ssep]: KAIST 반도체시스템공학과 교수진 <https://sse.kaist.ac.kr/professor/> (2026-10-22 열람)
[^ais]: KAIST AI시스템학과 교수진 <https://aicollege.kaist.ac.kr/ais/faculty/index/page/2> (2026-10-22 열람)

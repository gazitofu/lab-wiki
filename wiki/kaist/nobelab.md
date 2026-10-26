# Nano-Oriented Bio-Electronics Lab

**KAIST 전기및전자공학부·반도체공학대학원 · 최양규 교수**

- 분야: 신경망 모사 소자와 시스템, 반도체 소자의 특성 분석, 새로운 메모리, 마찰전기 발전, 보안 소자
- 대분야: 전기전자·반도체·광학
- 태그: 뉴로모픽 소자[^research], 메모리 반도체 소자[^research], 하드웨어 보안[^research], 에너지 하베스팅[^research]
- 홈페이지: <https://sites.google.com/view/nobelab/>
- 근거와 출처: [Nano-Oriented Bio-Electronics Lab 근거 페이지](nobelab-sources.md)

> 반도체 소자로 신경세포의 정보 처리를 구현하고, 정보를 저장하는 메모리와 기기를 식별하는 보안 소자, 주변의 움직임에서 전기를 얻는 장치를 연구하는 연구실이다.[^research]

## 무엇을 연구하나

최양규 교수가 이끄는 연구실은 반도체 소자와 그 소자를 연결한 시스템을 함께 연구한다.[^professor] 뉴로모픽 하드웨어(신경세포의 동작을 본떠 정보를 처리하는 장치)를 위해 인공 뉴런(신호를 받아 처리하고 출력하는 신경세포의 기능을 구현한 소자)과 인공 시냅스(신경세포 사이의 신호 전달과 연결 강도의 변화를 구현한 소자)를 개발한다. 트랜지스터(전기 신호를 조절하거나 증폭하는 반도체 소자)의 구조와 재료를 달리하고, 이들을 신경망(연결된 처리 단위들이 신호를 주고받으며 계산하는 모형)으로 연결하는 연구다.[^research] 대표 논문에서는 주기적인 전기 신호를 만드는 발진기를 서로 연결해 신경망을 구현한다. 발진기의 주파수(주기 현상이 단위 시간에 반복되는 횟수)를 조절해 패턴을 비교하고 시간에 따라 변하는 신호를 분류했다.[^p2] 다른 논문에서는 두 안정 저항 상태를 갖는 바이리스터로 발진기를 만들고, 진동 사이의 위상(주기 안에서 진행된 위치) 차이에 정보를 담아 영상의 경계를 검출하고 그래프의 정점에 색을 배정했다.[^p5]

반도체 소자의 전기적 특성과 열에 따른 동작을 시뮬레이션(대상의 동작을 모형으로 재현해 조사하는 방법)과 모델링(대상의 성질과 관계를 수식이나 구조로 나타내는 일)으로 분석한다. CMOS(상보형 금속 산화물 반도체, Complementary Metal-Oxide-Semiconductor)는 서로 보완하는 두 종류의 트랜지스터를 사용하는 기술이다. 연구실은 이 기술에 쓰이는 소자와 메모리(정보를 저장하는 장치)를 다룬다. 새로운 메모리 갈래에는 축전기(전하를 모아 전기 에너지를 저장하는 부품) 없이 동작하는 바이리스터(biristor)와, 한 트랜지스터에서 동적 메모리와 비휘발성 메모리(전원을 꺼도 정보를 유지하는 메모리)의 기능을 구현하는 unified-RAM이 있다.[^research] 대표 논문의 트라이리스터(triristor)는 전류가 갑자기 바뀌는 두 번의 전이를 이용해 세 안정 상태를 구현한 소자다. 연구진은 이 소자가 세 값으로 계산하는 논리와 여러 값을 저장하는 메모리에 쓰일 수 있다고 설명한다.[^p3]

에너지 하베스팅(주변의 빛·열·움직임 등에서 사용 가능한 에너지를 얻는 기술)에서는 마찰전기(물체의 접촉과 분리 등으로 전하가 옮겨 생기는 전기 현상)를 이용하는 발전기를 다룬다. 전하의 배치가 주변 전하의 분포에 영향을 주는 정전 유도도 이용한다. 연구 소개는 이런 전원을 사물인터넷(Internet of Things, 기기들이 통신망으로 연결되어 정보를 주고받는 체계)의 센서에 사용할 가능성을 설명한다.[^research] 마찰전기 재료 논문에서는 구성 재료가 서로 보완하도록 하는 합성 전략을 개발해 늘어나는 마찰전기 재료를 만들었다.[^p4]

보안 소자에서는 물리 현상의 예측하기 어려운 변화를 디지털 정보로 바꾸는 난수 발생기(Random Number Generator, RNG)와 기기를 식별하는 물리적 복제 방지 함수(Physically Unclonable Function, PUF)를 연구한다. 바람의 불규칙성을 이용한 난수 발생 기술과 플래시 메모리(전원을 꺼도 정보를 유지하며 블록 단위로 지우고 다시 쓰는 반도체 메모리)를 이용한 기기 인증 기술을 소개한다.[^research] 대표 논문에서는 다결정 실리콘(여러 결정이 모여 이루어진 실리콘)의 불규칙한 진동으로 난수를 만들었다.[^p1] 다른 논문에서는 암호용 트랜지스터의 예측하기 어려운 동작과 잡음을 결합하는 신호 변환기를 함께 개발해, 반복 작동과 온도 변화에 대한 난수 발생기의 동작을 살폈다.[^p6]

## 주요 연구 주제

### 1. 신경망을 구현하는 소자와 시스템

인공 뉴런·시냅스의 구조와 재료, 이 소자들을 연결한 뉴로모픽 시스템을 연구한다.[^research]

발진기의 주파수 조절과 위상 차이를 이용한 신경망을 구현한다.[^p2][^p5]

### 2. 반도체 특성 분석과 새로운 메모리

반도체의 전기·열 특성을 분석하고, 축전기 없는 메모리와 한 소자에 여러 저장 기능을 담는 메모리를 연구한다.[^research]

세 안정 상태를 갖는 트라이리스터의 다중 값 논리·메모리 응용 가능성을 다룬다.[^p3]

### 3. 주변의 움직임에서 전기를 얻는 장치

마찰전기와 정전 유도를 이용하는 발전기 및 센서용 에너지원의 가능성을 다룬다.[^research]

구성 재료를 상호 보완하는 합성 전략으로 신축성 마찰전기 재료를 개발한다.[^p4]

### 4. 물리적 성질을 이용하는 하드웨어 보안

불규칙한 물리 현상을 쓰는 난수 발생과 반도체 소자를 이용한 기기 인증을 연구한다.[^research]

실리콘 소자의 불규칙한 진동과 암호용 트랜지스터를 이용한 난수 발생기를 개발한다.[^p1][^p6]

## 대표 논문

누리집의 2021–2026년 논문 가운데 최양규 교수가 마지막 저자로 적힌 6편을 골랐다. 교수의 KAIST 재직 시기에 발표된 논문이며, 신경망 소자·진동 신경망 2편, 하드웨어 보안 2편, 다중 상태 소자 1편, 마찰전기 재료 1편을 담았다. 연도는 누리집 구역을 따랐다. "쉽게 말하면" 칸은 각 논문의 등록 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [A Polycrystalline Silicon Thin-Film Transistor with Grain-Induced Stochasticity for an Energy-Efficient True Random Number Generator](https://doi.org/10.1021/acsnano.6c02362) · ACS Nano | 다결정 실리콘 박막(두께가 얇은 막)으로 만든 트랜지스터에서 예측하기 어려운 진동을 구현하고, 이를 진성 난수 발생기(물리 현상의 불규칙성을 이용해 난수를 만드는 장치)에 이용했다. 재료를 쌓고 열처리하는 조건과 불순물 농도를 조절해 전류가 갑자기 바뀌는 동작과 진동을 구현했다. 결정 사이의 경계에서 전기를 운반하는 입자가 붙잡혔다 풀리는 현상이 진동의 불규칙성을 키웠다. 난수성 검사 15종을 통과했으며 반복 작동과 주변 온도 변화에도 안정적으로 동작했다. 이 방식은 기존 회로 위에 소자를 입체적으로 쌓는 집적을 지원한다.[^p1] | 1저자 Seung-Il Kim, 마지막 저자 최양규 |
| 2 | 2025 | [Oscillatory Neural Network with Tunable Frequency for Brain-Inspired Neuromorphic Computing](https://doi.org/10.1021/acs.nanolett.5c00376) · Nano Letters | 주파수 조절이 가능한 실리콘 트랜지스터 발진기(Silicon transistor-based Oscillator with Frequency Tunability, SOFT)를 제안했다. 한 트랜지스터는 발진기로, 다른 트랜지스터는 전원을 꺼도 상태를 유지하며 전류가 흐르는 정도를 조절하는 저항 소자로 작동한다. 두 소자는 구조가 같아 같은 웨이퍼(반도체 소자를 만드는 얇은 판)에 함께 집적했다. SOFT 두 개를 저항으로 연결해 입력과 기준 패턴을 비교했고, 네 개에는 외부 신호에 진동을 맞추는 방식을 적용해 시간에 따라 변하는 신호를 분류했다. 연구진은 이 구조가 에너지 효율과 집적도 확장에 잠재력이 있다고 보았다.[^p2] | 1저자 Ye-Seong Chung, 마지막 저자 최양규 |
| 3 | 2025 | [A Triristor With Tri-Stable States Using Double Latches](https://doi.org/10.1109/led.2025.3580096) · IEEE Electron Device Letters | 실리콘 웨이퍼에 만든 트랜지스터와 같은 구조에서 두 번의 래치(전류가 급격히 바뀌고 바뀐 상태를 유지하는 동작)를 이용해 세 안정 상태를 갖는 트라이리스터를 구현했다. 두 래치는 서로 다른 위치와 전압에서 일어나며 각각 전류 수준을 급격히 바꾼다. 이 두 전이가 세 안정 상태를 만들어, 세 값으로 계산하는 논리와 여러 값을 저장하는 메모리에 적용할 수 있다고 설명한다.[^p3] | 1저자 Hyun-Bin Noh, 마지막 저자 최양규 |
| 4 | 2025 | [Synthesis of stretchable triboelectric material with strain-compensating ability using gradient interpenetrating polymer networks](https://doi.org/10.1039/d4ee03110e) · Energy & Environmental Science | 구성 재료가 서로 보완하도록 하는 합성 전략을 개발해 신축성 마찰전기 재료를 만들었다. 고체 사이의 접촉 대전을 이용하는 마찰전기 발전기에서 높은 출력을 얻었다.[^p4] | 1저자 Do-Wan Kim, 마지막 저자 최양규 |
| 5 | 2024 | [A Nanoscale Bistable Resistor for an Oscillatory Neural Network](https://doi.org/10.1021/acs.nanolett.3c04539) · Nano Letters | 게이트 전극(소자의 전기적 상태를 조절하는 전극)이 없는 바이리스터로 발진기를 만들었다. 단일 트랜지스터의 래치 현상으로 짧은 펄스 형태의 전압 신호가 반복된다. 두 발진기를 축전기로 연결하자 위상 차이가 180°인 동기화가 나타났다. 연구진은 발진기 사이의 위상 차이에 정보를 담아 영상의 경계 검출과 그래프의 정점 색칠(연결된 점에 서로 다른 색을 배정하는 문제)을 수행했다. 반도체 공정과의 호환성, 소비 전력, 차지하는 면적 측면의 장점을 설명한다.[^p5] | 1저자 Seong-Yun Yun, 마지막 저자 최양규 |
| 6 | 2024 | [Cryptographic transistor for true random number generator with low power consumption](https://doi.org/10.1126/sciadv.adk6042) · Science Advances | 암호용 트랜지스터가 작동하면서 보이는 불규칙하고 예측하기 어려운 변화를 난수의 원천으로 이용했다. 잡음을 결합하는 아날로그·디지털 변환기(연속적인 신호를 구별되는 값으로 바꾸는 회로)를 개발해 전기 신호를 이진 난수로 바꾸면서 난수성도 높였다. 트랜지스터에서는 전기를 운반하는 입자가 불규칙하게 늘어나고 빠져나가는 과정이 입력 전류가 공급되는 동안 반복된다. 난수 발생기는 난수성 검사 15종을 통과했고 반복 작동과 주변 온도 변화에도 안정적으로 동작했다. 연구진은 적은 소비 전력과 차지하는 면적을 근거로 사물인터넷 보안에 활용할 가능성을 제시했다.[^p6] | 1저자 Seung-Il Kim, 마지막 저자 최양규 |

## 교수와 전문 분야

최양규(Yang-Kyu Choi)는 KAIST 전기및전자공학부 교수이며 KT 석좌교수다. 반도체공학대학원 연구실 목록에도 같은 이름과 누리집으로 올라 있다.[^ee][^semicon] 랩 교수 소개는 2004–2006년 KAIST 조교수, 2006–2010년 부교수, 2011년부터 교수로 적는다. 서울대학교 물리교육 학사(1989), 물리학 석사(1991), University of California, Berkeley 전기·컴퓨터과학 석사(1999)와 박사(2001)를 취득했다. 1991–1997년 현대전자·하이닉스 경력과 2001–2003년 Berkeley 박사후연구 경력을 적고 있다.[^professor]

교수 소개가 밝힌 전문 분야는 반도체 소자, 나노 크기 트랜지스터, 뉴로모픽 소자·시스템, 보안 소자, 나노가공과 마찰전기 발전기다.[^professor] 전기및전자공학부는 주요 연구를 Nano CMOS와 Nanofabrication Technology로 적는다.[^ee]

## 응용 분야

- 인공 뉴런과 시냅스를 연결한 신경망 하드웨어[^research]
- 정보를 저장하는 반도체 메모리[^research]
- 난수 생성과 반도체 기기의 인증[^research]
- 주변의 움직임에서 에너지를 얻는 센서 전원[^research]

## 구성원

2026년 10월 26일 누리집의 Ph. D. Candidate 페이지에 게시된 17명, M.S. Candidate 페이지의 6명, Post Doc. & Staff 페이지의 박사후연구원 1명으로 합계 24명이다. 과정·시작 표기·연구 주제는 각 카드의 표기를 따른다.[^phd][^ms][^postdoc] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Seong-Yun Yun | 박사과정 | 21, Spring | Neuromorphic Devices | syyun@nobelab.kaist.ac.kr | 2, 3, 4, 5 |
| Joon-Ha Son | 박사과정 | 21, Spring | Neuromorphic Devices | jhson@nobelab.kaist.ac.kr | 3 |
| Sang-Won Lee | 박사과정 | 21, Spring | Nano CMOS; Neuromorphic device & system; TCAD simulation (Synopsys Sentaurus, Silvaco) | sanglee@nobelab.kaist.ac.kr | 1, 3 |
| Hae-Yeon Kim | 박사과정 | 2 2, Spring | Neuromorphic Hardware | hykim@nobelab.kaist.ac.kr | 3 |
| Jeong-A Han | 박사과정 | 22, Fall | Neuromorphic Devices; Trap characterization | jahan@nobelab.kaist.ac.kr | 1, 4 |
| Ho-Young Maeng | 박사과정 | 23, Spring | Probabilistic computing; Neuromorphic Devices | hymaeng@nobelab.kaist.ac.kr |  |
| Tae-Goon Lee | 박사과정 | 23, Spirng | Advanced Electronics | tglee@nobelab.kaist.ac.kr | 4 |
| Ye-Seong Chung | 박사과정 | 23, Fall | Neuromorphic Devices and System |  | 2 |
| Min-Jae Choi | 박사과정 | 23, Fall | Ferroelectric Devices; Neuromorphic Devices | mjchoi@nobelab.kaist.ac.kr |  |
| Han-Sol Chin | 박사과정 | 23, Fall | Nano CMOS; Neuromorphic Devices; Liquid Metal | hschin@nobelab.kaist.ac.kr |  |
| Seong-Jae Byeon | 박사과정 | 25, Fall | Novel Memory Devices; InGaZnO TFTs |  |  |
| Ji-Woo Park | 박사과정 | 25, Fall | Flexible oxide TFTs; Textile-based wearable device; Neuromorphic Devices |  |  |
| Su-Jin Sung | 박사과정 | 26, Spring | Neuromorphic Devices; RRAM | sjsung@nobelab.kaist.ac.kr |  |
| In-Ki Hong | 박사과정 | 24, Spring | Neuromorphic Devices and System | ikhong@nobelab.kaist.ac.kr | 1 |
| Hyun-Bin Noh | 박사과정 | 24, Spring | Neuromorphic Devices and System; Capacitorless DRAM | hbnoh@nobelab.kaist.ac.kr | 3 |
| Yi-Hyun Kim | 박사과정 | 24, Spring | P oly-Si TFTs; Neuromorphic Devices | yhkim@nobelab.kaist.ac.kr | 3 |
| Soo-Min Kim | 박사과정 | 26, Fall | Novel Memory Devices; InGaZnO TFTs |  |  |
| Jin-Ho Kim | 석사과정 | 25, Spring | Neuromorphic Devices and System | jinkim@nobelab.kaist.ac.kr |  |
| Jun-Seok Kim | 석사과정 | 25, Spring | Neuromorphic Devices and System | jskim@nobelab.kaist.ac.kr |  |
| Kyung-Jun Ji | 석사과정 | 25, Fall | Neuromorphic Devices and System | kjji@nobelab.kaist.ac.kr |  |
| Jung-Woo Park | 석사과정 | 26, Spring | Neuromorphic Devices and System | jungpark@nobelab.kaist.ac.kr |  |
| Yeon-Jun Jung | 석사과정 | 26, Spring | Neuromorphic Devices and System | yjjung@nobelab.kaist.ac.kr |  |
| Jun-Hyoung Park | 석사과정 | 26, Spring | Neuromorphic Devices and System; Device Physics and Modeling; TCAD Simulation | jhpark@nobelab.kaist.ac.kr | 3 |
| Do-Wan Kim | 박사후연구원 |  | Triboelecticity; Energy Harvesting; Magnetoelasticity | dokim@nobelab.kaist.ac.kr | 4 |

## 졸업생과 이전 구성원

누리집 Alumni의 98개 인물 항목이다. Post Doc. 5명, Ph.D 39명, M.S. 54명이며 기간과 진로는 누리집 표기다. 박사후연구원 항목은 기간이 적혀 있지 않으며, 학위과정 항목의 괄호는 졸업 연도 하나가 아니라 게시된 재학 기간이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Xingjiu Huang | Post Doc. | Professor, Chinese Academy of Sciences |
| Jianxin Geng | Post Doc. |  |
| Zheng Guo | Post Doc. |  |
| Wu Kang Kim | Post Doc. | IBM |
| Da-Jin Kim | Post Doc. | Samsung Electronics |
| Hyun-Jin Lee | Ph.D (Mar. 2003 - Aug. 2007) | SK Hynix |
| Seong-Wan Ryu | Ph.D (Mar. 2006 - Aug. 2009) | SK Hynix |
| Oktay Yarimaga | Ph.D (Mar. 2005 - Feb. 2010) | Izmir Institute of Technology, Turkey |
| Maesoon Im | Ph.D (Mar. 2005 - May. 2010) | KIST (Korea Institute of Science and Technology) / Professor, University of Science & Technology |
| Jin-Woo Han | Ph.D (Mar. 2006 - May. 2010) | Executive Vice President of Samsung Electronics |
| Ju-Hyun Kim | Ph.D (Mar. 2006 - Jan. 2011) | Samsung Electronics |
| Sungho Kim | Ph.D (Mar. 2006 - Jan. 2012) | Professor, Sejong University |
| Chungjin Kim | Ph.D (Mar. 2006 - Jan. 2012) | Samsung Electronics |
| Sung-Jin Choi | Ph.D (Feb. 2007 - Jan. 2012) | Professor, Kookmin University |
| Jaehyuk Ahn | Ph.D (Feb. 2007 - Feb. 2013) | Professor, Chungnam National University |
| Chang-Hoon Kim | Ph.D (Mar. 2006 - May. 2013) | Samsung Electronics |
| Dong-Il Moon | Ph.D (Sep. 2008 - Feb. 2015) | NASA (National Aeronautics and Space Administration) |
| Ji-Min Choi | Ph.D (Feb. 2009 - Feb. 2015) | Samsung Electronics |
| Jee-Yeon Kim | Ph.D (Feb. 2009 - Feb.2016) | Intel |
| Daewon Kim | Ph.D (Feb. 2010 - Feb. 2016) | Professor, Kyung Hee University |
| Myeong-Lok Seol | Ph.D (Feb. 2010 - Feb.2016) | Apple |
| Chang-Hoon Jeon | Ph.D (Feb. 2012 - Jul. 2016) | Samsung Electronics |
| Dongil Lee | Ph.D (Mar. 2013 - Feb. 2017) | Micron |
| Byung-Hyun Lee | Ph.D (Mar. 2013 - Feb. 2017) | Vice President of Samsung Electronics |
| Choongki Kim | Ph.D (Mar. 2014 - Feb. 2018) | SK Hynix |
| Hagyoul Bae | Ph.D (Mar. 2014- Feb. 2018) | Professor, Jeonbuk National University |
| Hwon Im | Ph.D (Mar. 2009 - Aug. 2018) | Samsung Electronics |
| Sang Jae Park | Ph.D (Mar. 2013 - Feb. 2019) | Samsung Electronics |
| Seung-Bae Jeon | Ph.D (Mar 2013. - Feb. 2019) | Professor, Hanbat National University |
| Jae Hur | Ph.D (Mar. 2013 - Feb. 2019) | Intel |
| Byeong-Woon Hwang | Ph.D (Mar. 2015 - Feb. 2019) | SK Hynix |
| Jun-Young Park | Ph.D (Mar. 2014 - Feb. 2020) | Professor, Chungbuk National University |
| Seong-Yeon Kim | Ph.D (Mar. 2016 - Feb. 2020) | SK Hynix |
| Myungsoo Seo | Ph.D (Mar. 2016 - Aug. 2020) | Samsung Electronics |
| Moon-seok Kim | Ph.D (Sep. 2018 - Feb. 2022) | Professor, Hanbat National University |
| Il-Woong Tcho | Ph.D (Mar. 2016 - Feb. 202 2) | Samsung Electronics |
| Geon-Beom Lee | Ph.D (Mar. 2016 - Feb. 202 2) | Samsung Electronics |
| Myung-Su Kim | Ph.D (Mar. 201 5 - Aug. 2022) | Samsung Electronics |
| Weon-Guk Kim | Ph.D (Mar.2016 - Aug.2022) | SK Hynix |
| Joon-Kyu Han | Ph.D (Sep. 201 7 - Feb. 202 3) | Professor, Seoul National University |
| J i-Man Yu | Ph.D (Mar. 201 8 - Feb. 202 4) | Professor, Kyungpook National University |
| Jung-Woo Lee | Ph.D (Sep. 2020 - Aug. 2024) | SK Hynix |
| Seung-Il Kim | Ph.D (Mar. 20 20 - Feb. 202 6) | SK Hynix |
| Do Hoon Lee | Ph.D (Mar. 20 22 - Feb. 202 6) | SK Hynix |
| Dong-Yoon Jang | M.S. (Mar. 2004 - Feb. 2006) | Samsung Electronics |
| Kuk-Hwan Kim | M.S. (Mar. 2005 - Feb. 2007) | Univ. of Michigan, Ann arbor |
| Lee-Eun Yu | M.S. (Mar. 2005 - Feb. 2007) | SK Hynix |
| Hyung-Soon Lim | M.S. (Mar. 2005 - Feb. 2007) | Professor, Harvard Univ. |
| Bongsan Gu | M.S. (Mar. 2006 - Feb. 2008) | Miraeasset Securities |
| Dong-Il Bae | M.S. (Mar. 2006 - Feb. 2008) | Samsung Electronics |
| Eujune Lee | M.S. (Sep. 2006 - Aug. 2008) | SK Hynix |
| Donghyun Kim | M.S. (Sep. 2007 - Aug. 2009) | Samsung Electronics |
| Soon-Gyu Kwon | M.S. (Mar. 2008 - Feb. 2010) | KAIST (Seoul) |
| Kwangwon Lee | M.S. (Mar. 2008 - Feb. 2010) | Fairchild |
| Yong-Bum Park | M.S. (Sep. 2008 - Jun. 2010) | Samsung SDI |
| Jinseong Lee | M.S. (Feb. 2009 - Jan. 2011) | Samsung Electronics |
| Hyunseung Cha | M.S. (Sep. 2010 - Jun. 2011) | Startup |
| Kyungyong Choi | M.S. (Feb. 2010 - Jan. 2012) | Samsung Electronics |
| Juan Pablo Duarte | M.S. (Sep. 2010 - Jan. 2012) | Apple |
| David Baek | M.S. (Sep. 2010 - Aug. 2012) | Intel |
| Seung-Won Ko | M.S. (Feb. 2011 - Feb. 2013) | Junctions |
| Dong-Oh Kim | M.S. (Mar. 2012 - Feb. 2014) | Samsung Electronics |
| Joon-Bae Moon | M.S. (Mar. 2012 - Feb. 2014) | University of Michigan |
| Hyunjae Jang | M.S. (Mar. 2012 - Feb. 2014) | Samsung Electronics |
| Jong-Ho Woo | M.S. (Sep. 2012 - Jun. 2014) | Samsung Electronics |
| Hee-Jeong Hong | M.S. (Sep. 2012 - Jun. 2014) | SK Hynix |
| Yongyoon Kim | M.S. (Feb. 2013 - Feb. 2015) | Samsung Electronics |
| Ui-Sik Jeong | M.S. (Feb. 2013 - Feb. 2015) | Samsung Electronics |
| Daechul Ahn | M.S. (Sep. 2014 - Jul. 2016) | Samsung Electronics |
| Gun-hee Kim | M.S. (Mar. 2015 - Feb. 2017) | Apple |
| Tewook Bang | M.S. (Mar. 2015 - Feb. 2017) | Sk Hynix |
| Do-Hyun Kim | M.S. (Sep. 2016 - Aug. 2018) | SK hynix |
| Seung-Wook Lee | M.S. (Sep. 2016 - Aug. 2018) | Samsung Electronics |
| Kyu-Man Hwang | M.S. (Sep. 2016 - Aug. 2018) | Samsung Electronics |
| Sung-Hwan Kim | M.S. (Mar. 2017 - Feb. 2019) | LG Innotek |
| Ik Kyeong Jin | M.S. (Mar. 2017 - Feb. 2019) | Ph.D candidate, The University of New South Wales |
| Jun Woo Son | M.S. (Sep. 2017 - Aug. 2019) | SK Hynix |
| Dae-Hwan Yun | M.S. (Mar. 2018 - Feb. 2020) | SK Hynix |
| Seong-Joo Ha n | M.S. (Sep. 201 9 - Aug. 20 21) | SK Hynix |
| Mun-Woo Lee | M.S. (Mar. 2 020 - Feb. 202 2) | Samsung Electronics |
| Byeong-Chan Bang | M.S. (Mar. 2019 - Feb. 2022) | SK Hynix (V-KEPSI) |
| Jeong-Hak Lee | M.S. (Mar. 2019 - Feb. 2022) | SK Hynix (V-KEPSI) |
| Gyeong-Jun Yun | M.S. (Mar. 20 19 - Aug. 2022) |  |
| Jin-Woo Jung | M.S. (Sep. 2020 - Aug. 2022) | Samsung Electronics |
| Young-Woo Chung | M.S. (Mar. 2021 - Feb. 2023) | Samsung Electronics |
| Yeon Nam Goung | M.S. (Mar. 2020 - Feb. 2023) | SK Hynix (V-KEPSI) |
| Bu-Kil Kim | M.S. (Mar. 2020 - Feb. 2023) | SK Hynix (V-KEPSI) |
| Geon-Woo Kim | M.S. (Mar. 202 0 - Feb. 202 3) | SK Hynix (V-KEPSI) |
| Jai-Houb Chun | M.S. (Mar. 2021 - Feb. 202 4) | SK Hynix (V-KEPSI) |
| Jun-Young Lim | M.S. (Mar. 2022 - Feb. 2025) | SK Hynix (V-KEPSI) |
| Ji-Hoon Kim | M.S. (Mar. 2023 - Feb. 202 5) | SK Hynix |
| Tae-Ho Cha | M.S. (Sep. 20 23 - Aug. 202 5) | SK Hynix |
| Hyeok-Jin Jang | M.S. (Mar. 202 4 - Feb. 202 6) | SK Hynix |
| Jong-Won Kim | M.S. (Mar. 202 4 - Feb. 202 6) | SK Hynix |
| Chi-ho Kim | M.S. (Mar. 2024 - Jun. 2026) | SK Hynix |
| Jae-wook Yang | M.S. (Mar. 202 3 - Jun. 2026) | SK Hynix |
| Ji-won Lee | M.S. (Mar. 2024 - Jun. 2026) | SK Hynix (V-K EPSI) |
| Hyeok-jun Choi | M.S. (Mar. 2023 - Jun. 2026) | SK Hynix (V-KEPSI) |

## 최근 논문 목록 (2021–2026)

트랜지스터와 메모리, 인공 감각·신경망, 보안 소자와 마찰전기 발전을 다룬 목록이다. 누리집 Journal의 2021–2026년 구역에 기재된 학술지 논문 107편과 International Conference의 같은 연도 범위 발표 2편, 합계 109편이다. 연도별로 2026년 14편, 2025년 10편, 2024년 19편, 2023년 18편, 2022년 28편, 2021년 20편이다. 연도는 누리집 구역을 따랐다. 「Effect of Annealing Temperature on Minimum Domain Size of Ferroelectric Hafnia」는 2023년 구역에 있지만 개별 서지에는 2024년 3월로 적혀 있다. 「Uncovering a third function of the transistor beyond switching and amplification: coupled photo-responsive oscillators for in-sensor computing」는 날짜 없는 게재 승인 항목이며 누리집의 2026년 구역에 두었다. 저자·제목·학술지와 학회 이름은 누리집 표기다. 저자 이름 옆 †는 해당 항목이 동등 기여라고 설명한 기호다.[^journal][^intl]

**2026**

- Jun-Hyoung Park, Hyun-Bin Noh, Sang-Won Lee, Seong-Yun Yun, and Yang-Kyu Choi. "Analytical Model for Single Transistor Latch in MOSFETs". *IEEE Electron Device Letters, Sep. 2026*.
- Jaewook Yoo, Hongseung Lee, Sojin Jung, Seongbin Lim, Soohyun Lim, Donghyeon Lee, Dongsun Shin , Junhui Park, Sieun Lee, Yang-Kyu Choi, and Hagyoul Bae. "Nonlinear Asymmetric Parasitic Resistance Extraction of Vertical Pillar-Type FET Using Physics-Informed Artificial Neural Network". *IEEE Electron Device Letters, Jun. 2026*.
- Soohyun Lim, Jaewook Yoo, Hongseung Lee, Seongbin Lim, Minah Park, Seohyeon Park, Sojin Jung, Donghyeon Lee, Sieun Lee, Dongsun Shin, Junhui Park, Yang-Kyu Choi,and Hagyoul Bae. "Simultaneous Observation of Donor- and Acceptor-Like Interface Trap Density in 5-Stage Si-NW GAA FETs Using Polychromatic Photonic I–V Characteristics". *IEEE Electron Device Letters, May 2026*.
- Seong-Yun Yun, Joon-Ha Son, and Yang-Kyu Choi. "Bio-inspired nociceptor with a leaky charge-trap field-effect transistor". *Chemical Engineering Journal, May. 2026*.
- Sang-Won Lee†, Seokho Seo†, Hakcheon Jeong†, Joon-Kyu Han†, Yujin Kim, Dongeun Yoo, Joon-Ha Son, Ji-Man Yu, Shinhyun Choi and Yang–Kyu Choi. "Array of Cointegrated Transistor-based Artificial Neurons and Synapses for Neuromorphic Computing". *Small*.
- Seung-Il Kim, In-Ki Hong, Sang-Won Lee, Hyeong-Jin You, Un-Shi An, Jeong-A Han, Myung-Su Kim, Seung-Tak Ryu and Yang-Kyu Choi. "A polycrystalline silicon thin-film transistor with grain-induced stochasticity for an energy-efficient true random number generator". *ACS Nano, July. 2026*.
- Hae-Yeon Kim†, Hyun-Bin Noh†, Ho-Young Maeng, and Yang-Kyu Choi. "A Selective Positive Ternary Inverter Using the Mirror Symmetry of a MOSFET With a Gate–Body Diode". *IEEE Transactions On Electron Devices, June. 2026*.
- Min-Jae Choi, Ju-Won Yeon, Ji-Man Yu, Myungsoo Seo, Min-Ho Kang, Sheung Hun Kim, Byung Jin Cho, Jun-Young Park and Yang-Kyu Choi. "High-Pressure Deuterium Annealing Effect on HfO2-based Gate-All-Around Ferroelectric FET". *IEEE Electron Device Letters, May. 2026*.
- Sang-Won Lee, Ho-Young Maeng, Seung-Il Kim and Yang-Kyu Choi. "Janus Behavior of Stochastic and Deterministic Operation in a MOSFET". *IEEE Electron Device Letters, May. 2026*.
- Ye-Seong Chung, Seong-Yun Yun, Sang-Won Lee, Jun-Hyoung Park, Ho-Young Maeng, and Yang-Kyu Choi. "Oscillatory Neural Network with High-Order Sub-Harmonic Injection Locking". *ACS Applied Materials & Interfaces, Apr. 2026*.
- Seong-Yun Yun†, Joon Pyo Kim†, Jaeyong Jeong, Sang-Won Lee, Ye-Seong Chung, Sanghyeon Kim, and Yang-Kyu Choi. "Scalable Ising machine composed entirely of Si transistors". *Science Advances, Mar. 2026*.
- Seong-Yun Yun, Sang-Won Lee, Hyun-Bin Noh, and Yang-Kyu Choi. "Bioinspired Tripartite Synaptor with Conjoined Twin Transistors for Homeostasis in Neuromorphic Hardware". *ACS Applied Materials & Interfaces, Mar. 2026*.
- Seong-Yun Yun, Joon-Kyu Han, and Yang-Kyu Choi. "Uncovering a third function of the transistor beyond switching and amplification: coupled photo-responsive oscillators for in-sensor computing". *Material Horizons. (게재 승인, 날짜 표기 없음)*.
- Do Hoon Lee† , Seungkyu Lee† , Minyong Park, Junehyeok Kim, Hanbit Jin, Su Yeong Kim, Donghyun Lee, Young-Soo Lim, Jun Chang Yang, Taehoon Lee, Byungkook Oh, Sang Yu Sun, Do-Wan Kim, Sihong Wang, Sung Gap Im, Hye Jin Kim, Sung-Min Park, Jihan Kim, Yang-Kyu Choi and Steve Park. "Universal cryogenic transfer of liquid metal particles in polymers for wafer-scale stretchable integrated electronics". *Nature Communications, Feb. 2026*.

**2025**

- Jae-Hyun Lee, Seong-Yun Yun, Joon-Kyu Han and Yang-Kyu Choi. "A Review of Single Transistor-based Neuron for Highly Scalable Neuromorphic Hardware". *IEEE Electron Devices Reviews, Nov. 2025*.
- Seung-Il Kim, Han-Sol Chin, Jeong-A Han, Sung-Ho Kim, Jong-Won Kim, Sang-Won Lee, Do-Hoon Lee, Myung-Su Kim, Seung-Tak Ryu and Yang-Kyu Choi. "A Cryptographic Transistor with Stochastic Carrier Trapping and Detrapping for a True Random Number Generator". *ACS Applied Materials & Interfaces, Nov. 2025*.
- Ho-Young Maeng† , Hyeonji Lee†, Sang-Won Lee, Jungyeop Oh, Hae-Yeon Kim, Sung-Yool Choi, and Yang-Kyu Choi. "A Reconfigurable Silicon Transistor for Noise-Resilient Stochastic Spiking Neural Networks". *ACS Nano, Nov. 2025*.
- Sang-Won Lee, Seong-Yun Yun, and Yang-Kyu Choi. "p-n-p Biristor With a Silicon Nanowire". *IEEE Transactions on Electron Devices, Sep. 2025*.
- Hyun-Bin Noh, Hae-Yeon Kim, Sang-Won Lee, Jun-Hyoung Park, Seong-Yun Yun, Joon-Ha Son, Jong-Won Kim, Yi-Hyun Kim, and Yang-Kyu Choi. "A Triristor with Tri-Stable States Using Double Latches". *IEEE Electron Device Letters, Jun. 2025*.
- Hae-Yeon Kim, Sang-Won Lee, Hyun-Bin Noh, In-Ki Hong, and Yang-Kyu Choi. "Latch Voltage Modulation of Cryptographic Transistor for True Random Number Generator". *Journal of Integrated Circuits and Systems, May. 2025*.
- Ye-Seong Chung†, Seong-Yun Yun†, Joon-Kyu Han, and Yang-Kyu Choi. "Oscillatory Neural Network with Tunable Frequency for Brain-Inspired Neuromorphic Computing". *Nano Letters, Apr. 2025*.
- Jung-Woo Lee†, See-On Park†, Seong-Yun Yun†, Yeeun Kim, Hyun Myung, Shinhyun Choi, and Yang-Kyu Choi. "Decoupling strategy to separate training and inference with three-dimensional neuromorphic hardware composed of neurons and hybrid synapses". *ACS Nano, Mar. 2025*.
- Do-Wan Kim†, Hyeonwoo Mun†, Yeonghun Kang, Weon-Guk Kim, Dahye Ahn, Seong-Yun Yun, Jeong-A Han, Do Hoon Lee, Taegoon Lee, Kihoon Jeong, Jihan Kim, Sung Gap Im, and Yang-Kyu Choi. "Synthesis of stretchable triboelectric material with strain-compensating ability using gradient interpenetrating polymer networks". *Energy & Environmental Science, Feb. 2025*.
- Seohyeon Park, Jaewook Yoo, Minah Park, Hongseung Lee, Hyeonjun Song, Seongbin Lim, Soyeon Kim, Sojin Jung, Taewan Kim, Yang-Kyu Choi, and Hagyoul Bae. "Determination of Donor- and Acceptor-like Interface Trap Density using Photoresponsive GIDL in Vertically Stacked Si-NW GAA FETs". *Applied Physics Letters, Feb. 2025*.

**2024**

- Ho-Young Maeng†, Joon-Kyu Han†, Jang-Uk Han, Soo-Hyung Lee, Sun-Woo Cheong, Cheol-Seong Hwang, and Yang-Kyu Choi. "Homeothermic P-Bit Computing Hardware with StochasticOperations Beyond Limit of Non-Stochastic Materials". *Advanced Functional Materials, Dec. 2024*.
- Jeong-A Ha n, Jung-Woo Lee, Joon-Kyu Han, Do-Wan Kim, Do-Hoon Lee, and Yang-Kyu Choi. "P-type Ternary Logic MOSFET with Tunable Middle State Using Bidirectional Threshold Switching". *IEEE Electron Device Letters, Nov. 2024*.
- Seong-Yun Yun, Ye-Seong Chung, Joon-Kyu Han, Sang-Won Lee, and Yang-Kyu Choi. "Resistive Coupling of Bistable Resistor-Based Oscillators for Oscillatory Neural Network". *IEEE Transactions on Electron Devices, Nov. 2024*.
- Seong-Yun Yun, Sang-Won Lee, Taegoon Lee, Joon-Ha Son, Ji-Man Yu, and Yang-Kyu Choi. "Frequency Response to AC Input Signal in a Neuristor". *IEEE Transactions on Electron Devices, Nov. 2024*.
- Seong-Yun Yun, Joon-Ha Son, Jin-Ki Kim, Joon-Kyu Han, and Yang-Kyu Choi. "Spike-based rotation detection using a self-powered triboelectric sensor with mimicry of a vestibular system". *Nano Energy, Dec. 2024*.
- Sang-Won Lee, Seung-Il Kim, Seong-Yun Yun, Joon-Kyu Han, Ji-Man Yu , Joon-Ha Son, and Yang-Kyu Choi. "Single Transistor Latch Near 1 V With Asymmetric Biasing in a MOSFET". *IEEE Transactions on Electron Devices, Oct. 2024*.
- Jung-Woo Lee†, Joon-Kyu Han†, Seung-Il Kim, Ho-Young Maeng, Seong-Yun Yun, Joon-Ha Son, Sang-Won Lee, and Yang-Kyu Choi. "Vertically integrated security devices with physically unclonable function and random number generation". *Nano Research, Sep. 2024*.
- Choong-Ki Kim, James Read, Minji Shon, Tae-Hyeon Kim, Myung-Su Kim, Ji-Man Yu, Min-Soo Yoo, Yang-Kyu Choi, and Shimeng Yu. "Capacitive Synaptor with Gate Surrounding Semiconductor Pillar Structure and Overturned Charge Injection for Compute-in-Memory". *Advanced Intelligent Systems, Aug. 2024*.
- Sang-Won Lee†, Seong-Yun Yun†, Joon-Kyu Han, Young-Hoon Nho, Seung-Bae Jeon and Yang-Kyu Choi. "Spike-Based Neuromorphic Hardware for Dynamic Tactile Perception with a Self-Powered Mechanoreceptor Array". *Advanced Science, Jul. 2024*.
- Choong-Ki Kim, Omkar Phadke, Tae-Hyeon Kim, Myung-Su Kim, Ji-Man Yu, Min-Soo Yoo, Yang-Kyu Choi, and Shimeng Yu. "Capacitive Synaptor with overturned Charge Injection for Compute-in-Memory". *IEEE Electron Device Letters , Mar. 2024*.
- Seong-Yun Yun†, Min Hyeok Kim†, Geon Gug Yang, Hee Jae Choi, Do-Wan Kim and Yang-Kyu Choi. "A triboelectric nanogenerator with synergistic complementary nanopatterns fabricated by block copolymer self-assembly". *Journal of Materials Chemistry A, Mar. 202 4*.
- Seong-Yun Yun†, Joon-Kyu Han†, and Yang-Kyu Choi. "A Nanoscale Bistable Resistor for an Oscillatory Neural Network". *Nano Letters, Jan. 202 4*.
- Jung-Woo Lee†, Joon-Kyu Han†, Dong-Hyun Wang, Seong-Yun Yun, Jeong-Seob Oh, Byeong-Chan Bang, Won-Hyo Cha, Jun-Young Park, and Yang-Kyu Choi. "High-pressure deuterium annealing for trap passivation for a 3-D integrated structure". *IEEE Transactions on Electron Devices , Feb. 2024*.
- Jae-Hyun Kim†, Joon-Kyu Han†, Ho-Young Maeng, Jang-Uk Han, Jeong-Woo Jeon, Yoon-Ho Jang, Kyung-Seok Woo, Yang-Kyu Choi, and Cheol-Seong Hwang. "Fully CMOS-Based p-Bits with a Bistable Resistor for Probabilistic Computing". *Advanced Functional Materials, Feb. 2024*.
- Seung-Il Kim, Hyeong-Jin You, Myung-Su Kim, Un-Shi An, Moon-Seok Kim, Do-Hoon Lee, Seung-Tak Ryu, and Yang-Kyu Choi. "Cryptographic transistor for true random number generator with low power consumption". *Science Advances, Feb. 202 4*.
- Ji-Man Yu†, You-Son Kim†, Chang-Hyeon Lee, Boo-Seok Jeong, Jin-Ki Kim, Joon-Kyu Han, Jung-Yeong Yang, Seong-Yun Yun, Sung-Gap Im, and Yang-Kyu Choi. "Bio-Inspired Organic Synaptor with in-situ ion-Doped Ultrathin Polyelectrolyte Containing Acetylcholine-like Cation". *Small, Feb. 2024*.
- Ji-Man Yu†, Gyeong-Do Ham†, Seong-Yeon Kim, Jin-Ki Kim, Joon-Kyu Han, Seong-Yun Yun, Seong-Hak Kim, Sang-Won Lee, Seung-Bae Jeon, Dae-Shik Kim, and Yang-Kyu Choi. "Self-Curable Synaptor with Tri-node Charge-Trap FinFET for Semi-Supervised Learning". *IEEE Electron Device Letters, Jan. 2024*.
- Moon-Seok Kim†, Il-Woong Tcho†, and Yang-Kyu Choi. "Cryptographic Triboelectric Random Number Generator with Gentle Breezes of an Entropy Source". *Scientific Reports, Jan. 2024*.
- Do-Hoon Lee†, Tae-Su Lim†, J eong-Su Pyeon, Hyun-Min Park, Sang-Won Lee, Seung-Kyu Lee, Won-Sik Kim, Min Kim, Jeong-Chan Lee, Do-Wan Kim, Seung-Min Han, Hyoung-Soo Kim, Steve Park, and Yang-Kyu Choi. "Self-Mixed Biphasic Liquid Metal Composite with Ultra-High Stretchability and Strain-Insensitivity for Neuromorphic Circuits". *Advanced Materials, Jan. 2024*.

**2023**

- Dae-Han Jung†, Ji-Man Yu†, Ja-Yun Ku, Sung-Su Yoon, Jae-Hun Kim, Joon-Kyu Han, Tae-Hyun Kil, Dong-Hyun Wang, Ju-Won Yeon, Yang-Kyu Choi, and Jun-Young Park. "Physically Unclonable Function With a Rough Silicon Channel MOSFET". *IEEE Transactions on Electron Devices, Dec. 2023*.
- Hae-Yeon Kim, Seung-Il Kim, Joon-Kyu Han, Jin-Woo Jung, and Yang-Kyu Choi. "A Single MOSFET-Based Oscillator on a Bulk-Silicon Wafer". *I EEE Electron Device Letters, Nov. 2023*.
- Joon-Kyu Han†, Jung-Woo Lee†, Young Bin Kim, Seong-Yun Yun, Ji-Man Yu, Keon Jae Lee, and Yang-Kyu Choi. "Vertically Integrated CMOS Ternary Logic Device with Low Static Power Consumption and High Packing Density". *ACS Applied Materials & Interfaces, Oct. 2023*.
- Hery Shin, Ji-Man Yu, Joon-Kyu Han, and Yang-Kyu Choi. "Co-integrated Neuromorphic Devices for Bio-inspired Compliance Control". *IEEE Transactions on Nanotechnology, Oct. 2023*.
- Moon-Seok Kim, Il-Woong Tcho, and Yang-Kyu Choi. "Analyses of unpredictable properties of a wind-driven triboelectric random number generator". *Scientific Reports, Oct. 2023*.
- Joon-Kyu Han†, Jung-Woo Lee†, Ye-eun Kim†, Young-Bin Kim†, Seong-Yun Yun, Sang-Won Lee, Ji-Man Yu, Keon-Jae Lee, Hyun-Myung, and Yang-Kyu Choi. "3D Neuromorphic Hardware with Single Thin-Film Transistor Synapses Over Single Thin-Body Transistor Neurons by Monolithic Vertical Integration". *Advanced Science, Sep. 2023*.
- Sang-Won Lee, Min-Gu Kang, Joon-Kyu Han, Seong-Yun Yun, In-Kyu Park, and Yang-Kyu Choi. "An artificial olfactory sensory neuron for selective gas detection with in-sensor computing". *Device, Sep. 2023*.
- Ja-Yun Ku†, Ji-Man Yu†, Dong-Hyun Wang, Dae-Han Jung, Joon-Kyu Han, Yang-Kyu Choi, and Jun-Young Park. "Improved SOI FinFETs Performance with Low-Temperature Deuterium Annealing". *IEEE Transactions on Electron Devices, Jul. 2023*.
- Ji-Man Yu, Joon-Kyu Han, Dong-Hyun Wang, Seong-Yun Yun, Jun-Young Park and Yang-Kyu Choi. "Lowering of Schottky Barrier Height in a MOSFET by Deuterium Annealing". *IEEE Electron Device Letters, Jun. 2023*.
- Geon-Beom Lee, Jeong-Yeon Kim, and Yang-Kyu Choi. "A Novel Charge Pumping Technique with Gate-Induced Drain Leakage Curent". *IEEE Electron Device Letters, May. 2023*.
- Joon-Kyu Han, Seong-Yun Yun, Ji-Man Yu, and Yan g-Kyu Choi. "A Leaky FinFET for Reservoir Computing with Temporal Signal Processing". *ACS A pplied Materials & Interfaces, May. 2023*.
- Jae Hur, Dongsuk Kang, Dong-Il Moon, Ji-Man Yu, Yang-Kyu Choi, and Shimeng Yu. "Cryogenic Storage Memory with High-Speed, Low-Power,and Long-Retention Performance". *Advanced Electronic Materials, Apr. 2023*.
- Seok-Jung Yun, Hoon Kim, Myung-Soo Seo, Min-Ho Kang, Tae-Ho Kim, Seong-Woo Cho, Min-Hyuk Park, Sang-Hun Jeon, Yang-Kyu Choi, and Seung-Bum Hong. "Effect of Annealing Temperature on Minimum Domain Size of Ferroelectric Hafnia". *ACS Applied Electronic Materials, Mar. 202 4*.
- Seong-Yun Yun, Joon-Kyu Han, Sang-Won Lee, Ji-Man Yu, Seung-Bae Jeon, and Yang-Kyu Choi. "Self-aware artificial auditory neuron with a triboelectric sensor for spike-based neuromorphic hardware". *Nano Energy, Vol. 109, May. 2023*.
- Anni Lu, Jae Hur, Yuan-Chun Luo, Hai Li, Dmitri E. Nikonov, Ian Young, Yang-Kyu Choi, and Shimeng Yu. "Scalable In-Memory Clustered Annealer with Temporal Noise of Charge Trap Transistor for Large Scale Travelling Salesman Problems". *IEEE Journal on Emerging and Selected Topics in Circuits and Systems , Vol. 1 3, Issue 1, Mar.2023*.
- Moon-Seok Kim, Sung-Ho Kim, Sang-Kyung Yoo, Bong-Soo Lee, Ji-Man Yu, Il-Woong Tcho, and Yang-Kyu Choi. "Error reduction of SRAM-based physically unclonable function for chip authentication". *International journal of information security, Feb.2023*.
- Joon-Kyu Han, Seong-Yun Yun, Ji-Man Yu, Seung-Bae Jeon, and Yang-Kyu Choi. "Artificial Multisensory Neuron with a Single Transistor for Multimodal Perception through Hybrid Visual and Thermal Sensing". *ACS Applied Materials & Interfaces, Vol. 15, Issue 4, Jan.2023*.
- Ji-Man Yu†, Seong-Yeon Kim†, Jin-Ki Kim, Joon-Kyu Han, Seung-Bae Jeon, and Yang-Kyu Choi. "Triple-Node FinFET with Non-Ohmic Schottky Junctions for Synaptic Devices". *IEEE Electron Device Letters, Vol. 44, Issue 1, Jan.202 3*.

**2022**

- Seokho Seo, Beomjin Kim, Donghoon Kim, Seungwoo Park, Tae Ryong Kim, Junkyu Park, Hakcheon Jeong, See-On Park, Taehoon Park, Hyeok Shin, Myung-Su Kim, Yang-Kyu Choi, Shi nhyun Choi. "The gate injection-based field-effect synapse transistor with linear conductance update for online training". *Nature Communications, Oct. 2022*.
- Ji-Man Yu, Dong-Hyun Wang, Ja-Yun Ku , Joon-Kyu Han , Dae-Han Jung ,Jun-Young Park , and Yang-Kyu Choi. "Low-temperature deuterium annealing to improve performance and reliability in a MOSFET". *Solid State Electronics, Vol. 197, Nov.2022*.
- Jung-Woo Lee , Joon-Kyu Han , Myung-Su, Kim , Ji-Man Yu , Jin-Woo Jung ,Seong-Yun Yun , and Yang-Kyu Choi. "Reliability Improvement of Gate-All-Around Junctionless SONOS Memory by Joule Heat From Inherent Nanowire Current". *IEEE Transactions on Electron Devices, Vol. 69, Issue 11, Nov.2022*.
- Joon-Kyu Han, Ji-Man Yu, Do-Wan Kim, and Yang-Kyu Choi. "An Artificial Neuron with a Leaky FinFET for a Highly Scalable Capacitive Neural Network". *Advanced Intelligent Systems, Vol. 4, Issue 1 2, Dec.2022*.
- †Young-Woo Chung, †Joon-Kyu Han, Jin-Woo Jung, Seong-Yun Yun, Ji-Man Yu, Mun-Woo Lee, and Yang-Kyu Choi. "Thermally Stable Single-Transistor Neuron for Reliable Neuromorphic System". *IEEE Electron Device Letters, , IEEE Electron Device Letters, Vol. 43, Issue 11, Nov.2022*.
- Myung-Su Kim, Jin-Ki Kim, Gyeong-Jun Yun, Ji-Man Yu, Joon-Kyu Han, Jung -Woo Lee, Seokho Seo, Shinhyun Choi, and Yang-Kyu Choi. "An Overturned Charge Injection Synaptic Transistor with a Floating-gate for Neuromorphic Hardware Computing". *IEEE Electron Device Letters, Vol. 43, Issue 9, Sep.2022*.
- Joon-Kyu Han†, Sang-Chan Park†, Ji-Man Yu, Jae-Hyuk Ahn, and Yang-Kyu Choi. "A Bio-inspired Artificial Gustatory Neuron for a Neuromorphic based Electronic-tongue". *Nano Letters, Vol. 2 2, No. 1 3, pp. 5244-5251, Jun. 202 2*.
- Joon-Kyu Han, Seong-Yun Yun, Sang-Won Lee, Ji-Man Yu and Yang-Kyu Choi. "A Review of Artificial Spiking Neuron Devices for Neural Processing and Sensing". *Advanced Functional Materials, Vol. 32, Issue 33, Aug.2022*.
- Weon-Guk Kim, Daewon Kim, Hye moon Lee and Yang-Kyu Choi. "Wearable Fabric-Based Hybrid Energy Harvester from Body Motion and Body Heat". *Nano Energy, Vol. 100, Sep.2022*.
- Ji-Man Yu, Chungryeol Lee, Joon-Kyu Han, Sang-Won Lee, Moon-Seok Kim, Sung Gap Im, and Yang-Kyu Choi. "Tunable and Reconfigurable Logic Gates with Electrolyte Gated Transistor Array Co-integrated with Neuromorphic Synapses". *IEEE Transaction on Electron Device, Vol. 69, Issue 8, Aug.2022*.
- Jin-Woo Jung, Joon-Kyu Han, Ji-Man Yu, Mun-Woo Lee, Moon-Seok Kim, Geon-Beom Lee, Il-Woong Tcho, Seong-Yun Yun, and Yang-Kyu Choi. "Concealable Oscillation-Based Physical Unclonable Function with a Single-Transistor Latch". *IEEE Electron Device Letters, Vol. 43, Issue 8, Aug.2022*.
- Seong-Yeon Kim†, Ji-Man Yu†, Gi Sung Lee, Dae-Hwan Yun, Moon-Seok Kim, Jin-Ki Kim, Da-Jin Kim, Geon-Beom Lee, Myung-Su Kim, Joon-Kyu Han, Myungsoo Seo, and Yang-Kyu Choi. "Synaptic Segmented Transistor with Improved Linearity by Schottky Junctions and Accelerated Speed by Double-Layered Nitride". *ACS Applied Materials & Interfaces, Vol. 14, No. 28, Jul.2022*.
- Ji-Man Yu, Joon-Kyu Han and Yang-Kyu Choi. "Mimicking Biological Synaptic Plasticity with a Leaky Charge-Trap FinFET". *Journal of Materials Chemistry C, Vol. 10, Issue 27, Jul.2022*.
- Joon-Kyu Han, Ji-Man Yu, Seo-Yeon Nam and Yang-Kyu Choi. "CMOS Ternary Logic with a Biristor Threshold Switch for Low Static Power Consumption". *IEEE Electron Device Letters, Vol. 43, Issue 7, Jul.2022*.
- Il-Woong Tcho, Weon-Guk Kim, Jin-Ki Kim, Do-Wan Kim, Seong-Yun Yun, Joon-Ha Son, and Yang-Kyu Choi. "A flutter-driven triboelectric nanogenerator for harvesting energy of gentle breezes with a rear-fixed fluttering film". *Nano Energy, Vol. 9 8, Ju l.2022*.
- Joon-Kyu Han†, Mingu Kang†, Jaeseok Jeong, Incheol Cho, Ji-Man Yu, Kuk-Jin Yoon, Inkyu Park, and Yang-Kyu Choi. "Artificial Olfactory Neuron for an In-sensor Neuromorphic Nose". *Advanced Science, Vol. 9, Issue 18, Jun.2022*.
- Ji-Man Yu†, Gyeongdo Ham†, Chungryeol Lee, Jae-Hyeok Lee, Joon-Kyu Han, Jin-Ki Kim, Donggon Jang, Nahyun Kim, Moon-Seok Kim, Sung Gap Im, Dae-Shik Kim, and Yang-Kyu Choi. "A Multiple-State Ion Synaptic Transistor Applicable to Abnormal Car Detection with Transfer Learning". *Advanced Intelligent Systems, Vol. 4, Issue 6, Jun.2022*.
- Joon-Kyu Han, Ji-Man Yu, and Yang-Kyu Choi. "A Junctionless Single Transistor Neuron with Vertically Stacked Multiple Nanowires for Highly Scalable Neuromorphic Hardware". *IEEE Transactions on Electron Devices, Vol. 69,Issue 6, Jun.2022*.
- Weon-Guk Kim, Jin-Ki Kim, Do-Wan Kim, Il-Woong Tcho, and Yang-Kyu Choi. "A triboelectric nanogenerator implemented with an acoustic foam for a self-driven silent tire". *Nano Energy, Vol. 96, Jun.2022*.
- Seong-Yun Yun, Il-Woong Tcho, Weon-Guk Kim, Do-Wan Kim, Joon-Ha Son, Sang-Won Lee, and Yang-Kyu Choi. "Mechanically robust triboelectric nanogenerator with shear thickening fluid for impact monitoring". *Journal of Materials Chemistry A, Vol. 10, Issue 19, May.2022*.
- Myung-Su Kim, Gyeong-Jun Yun, Wu-Kang Kim, Myungsoo Seo, Da-Jin Kim, Ji-Man Yu, Joon-Kyu Han, Jae Hur, Geon-Beom Lee, Seong-Yeon Kim, Dae-Hwan Yun, and Yang-Kyu Choi. "A Steep-Slope Phenomenon by Gate Charge Pumping in a MOSFET". *IEEE Electron Device Letters, Vol. 43, Issue 4, Apr.2022*.
- Joon-Kyu Han†, Il-Woong Tcho†, Seung-Bae Jeon, Ji-Man Yu, Weon-Guk Kim, and Yang-Kyu Choi. "Self-powered Artificial Mechanoreceptor based on Triboelectrification for a Neuromorphic Tactile System". *Advanced Science, Vol. 9, Issue 9, Mar.2022*.
- Hyun-Jung Kim, Geom-Beom Lee, Joon-Kyu Han, Seong-Joo Han, Da-Jin Kim, Ji-Man Yu, Myung-Su Kim, and Yang-Kyu Choi. "Curing of 1-Transistor-DRAM by Joule Heat From Punch-Through Current". *IEEE Electron Device Letters, Vol. 43, Issue 3, Mar.2022*.
- †Joon-Kyu Han, †Young-Woo Chung, Jaeho Sim, Ji-Man Yu, Geon-Beom Lee, Sang-Hyeon Kim, and Yang-Kyu Choi. "Mnemonic-Opto-Synaptic Transistor for In-sensor Vision System". *Scientific Reports, Vol. 12, Feb.2022*.
- Min-Kyeong Kim, Yang-Kyu Choi, and Jun-Young Park. "Power Reduction in Punch-Through Current-Based Electro-Thermal Annealing in Gate-All-Around FETs". *Micromachines, Vol. 1 3, No. 1, J an.202 2*.
- Seong-Joo Han†, Joon-Kyu Han†, Gyeong-Jun Yun, Mun-Woo Lee, Ji-Man Yu, and Yang-Kyu Choi. "Ultra-fast Data Sanitization of SRAM by Back-biasing to Resist a Cold Boot Attack". *Scientific Reports, Vol. 1 2, J a n. 202 2*.
- Jung-Woo Lee, Joon-Kyu Han, Ji-Man Yu, Geon-Beom Lee, Il-Woong Tcho, and Yang-Kyu Choi. "Reliability Improvement of Gate-All-Around SONOS Memory by Joule Heat from Gate Induced Drain Leakage Current". *IEEE Transactions on Electron Devices, Vol. 69, Issue 1, Jan. 202 2*.
- A. Lu, J. Hur, Y.-C. Luo, H. Li, D. E. Nikonov, I. Young, Y.-K. Choi, S. Yu. "Scalable in-memory clustered annealer with temporal noise of FinFET for the travelling salesman problem". *IEEE International Electron Devices Meeting (IEDM) 2022, San Francisco, USA*.

**2021**

- Joon-Kyu Han, Jungyeop Oh, Ji-Man Yu, Sung-Yool Choi, and Yang-Kyu Choi. "A Vertical Silicon Nanowire Based Single Transistor Neuron with Excitatory, Inhibitory, and Myelination Functions for Highly Scalable Neuromorphic Hardware". *Small, Vol. 17, Issue 49, Dec. 2021*.
- Geon-Beom Lee, Jin-Woo Jung, Choong-Ki Kim, Tewook Bang, Min-Soo Yoo, and Yang-Kyu Choi. "Improved Self-Curing Effect in a MOSFET with Gate Biasing". *IEEE Electron Device Letters, Vol. 42, No. 12, Dec. 20 21*.
- Geon-Beom Lee, Choong-Ki Kim, Tewook Bang, Min-Soo Yoo, and Yang-Kyu Choi. "Lateral Profiling of Gate Dielectric Damage by Off-State Stress and Positive-Bias Temperature Instability". *Microelectronics Reliability, Vol. 127, Dec.2021*.
- Joon-Kyu Han, Myung-Su Kim, Seung-Il Kim, Mun-Woo Lee, Sang-Won Lee, Ji-Man Yu, and Yang-Kyu Choi. "Investigation of Leaky Characteristic in a Single Transistor Based Leaky Integrate-and-fire Neuron". *IEEE Transactions on Electron Devices, Vol. 68, Issue 11, Nov.2021*.
- Mun-Woo Lee, Joon-Kyu Han, Gyeong-Jun Yun, Ji-Man Yu, Geon-Beom Lee, Seong-Joo Han, and Yang-Kyu Choi. "A Temperature Sensor with a Thermillator". *IEEE Electron Device Letters, Vol. 42, Issue 11, Nov.2021*.
- Moon-Seok Kim, Il-Woong Tcho, and Yang-Kyu Choi. "Strategy to enhance entropy of random numbers in a wind-driven triboelectric random number generator". *Nano energy, Vol. 89, Nov.2021*.
- Joon-Kyu Han, Jungyeop Oh, Gyeong-Jun Yun, Dongeun Yoo, Myung-Su Kim, Ji-Man Yu, Sung-Yool Choi, and Yang-Kyu Choi. "Co-integration of single transistor neurons and synapses by nanoscale CMOS fabrication for highly scalable neuromorphic hardware". *Science Advances, Vol. 7, Issue 32, Aug.2021*.
- Hagyoul Bae†, Geon-Beom Lee†, Jae Hur, Jun-Young Park, Da-Jin Kim, Myung-Su Kim, and Yang-Kyu Choi. "Gateless and Capacitorless Germanium Biristor with a Vertical Pillar Structure". *Micromachines, Vol. 12, No. 8, Jul.2021*.
- Jae Hur, Woo Jin Jeong, Mincheol Shin, and Yang-Kyu Choi. "Off-state leakage in MOSFET considering source/drain extension regions". *Semiconductor Sc ience and Technology, Vol. 36, No. 8 Jul.2021*.
- Joon-Kyu Han, Seong-Joo Han, Ji-Man Yu, and Yang-Kyu Choi. "Data Sanitization of SRAM by Thermal Distortion". *IEEE Transactions on Electron Devices, Vol. 68, No. 7, pp.3706-3710, Jul. 2021*.
- Sungho Kim, Moon-Seok Kim, Yongwoo Lee, Hee-Dong Kim, Yang-Kyu Choi, and Sung-Jin Choi. "Low-power true random number generator based on randomly distributed carbon nanotube networks". *IEEE Access, Vol. 9, Jun. 2021*.
- Seong-Joo Han, Joon-kyu Han, Myung-Su Kim, Gyeong-Jun Yun, Ji-Man Yu, Il-Woong Tcho, Myungsoo Seo, Geon-Beom Lee, and Yang-Kyu Choi. "Ternary Logic Decoder Using Independently Controlled Double-gate Si-NW MOSFETs". *Scientific Reports, Vol. 11, Jun. 2021*.
- Ji-Man Yu, Chungryeol Lee, Joon-Kyu Han, Seong-Joo Han, Geon-Beom Lee, Sung Gap Im, and Yang-Kyu Choi. "Multi-functional Logic Circuits Composed of Ultra-thin Electrolyte Gated Transistor with Wafer-scale Integration". *Journal of Materials Chemistry C, Vol. 9, No. 22, pp. 7222-7227. Jun. 2021*.
- Ji-Man Yu, Chungryeol Lee, Da-Jin Kim, Hongkeun Park, Joon-Kyu Han, Jae Hur, Jin-Ki Kim, Myung-Su Kim, Myeongsoo Seo, Sung Gap Im, and Yang-Kyu Choi. "All-solid-state Ion Synaptic Transistor for Wafer-scale Integration with Electrolyte of a Nanoscale Thickness". *Advanced Functional Materials, Vol. 31, No. 23, 2010971, Jun. 2021*.
- Wu-Kang Kim†, Pavlo Bidenko†, Jong Min Kim, Jaeho Shim, Joon-Kyu Han, Seongkwang Kim, Dae-Myeong Geum, Sanghyeon Kim, and Yang-Kyu Choi. "Vertical InGaAs Biristor for sub-1 V Operation". *IEEE Electron Device Letters, Vol. 42, No. 5, pp. 681-683, May. 2021*.
- Ji-Man Yu†, Gyeong-Jun Yun†, Moon-Seok Kim, Joon-Kyu Han, Da-Jin Kim, and Yang-Kyu Choi. "A Poly-Crystalline Silicon Nanowire Transistor with Independently Controlled Double-Gate for Physically Unclonable Function by Multi-States and Self-Destruction". *Advanced Electronic Materials, Vol. 7, No. 5, 2000989, May. 2021*.
- Joon-Kyu Han, Mun-Woo Lee, Ji-Man Yu, and Yang-Kyu Choi. "A Single Transistor-Based Threshold Switch for a Bio-inspired Reconfigurable Threshold Logic". *Advanced Electronic Materials, Vol. 7, No. 5, 2100117, May. 2021*.
- Jun-Young Park, Tae Jin Yoo, Ji-Man Yu, Byoung Hun Lee, and Yang-Kyu Choi. "Impact of Post-Metal Annealing with Deuterium or Nitrogen for Curing a Gate Dielectric using Joule Heat Driven by Punch-Through Current". *IEEE Electron Device Letters, Vol. 42, No. 2, pp. 276-279, Feb. 2021*.
- Weon-Guk Kim†, Do-Wan Kim†, Il-Woong Tcho, Jin-Ki Kim, Moon-Seok Kim, and Yang-Kyu Choi. "Triboelectric Nanogenerator: Structure, Mechanism, and Applications". *ACS Nano, Vol. 15, No. 1, pp. 258-287, Jan. 2021*.
- †Joon-Kyu Han, †Jaeho Sim, Dae-Myeong Geum, Seong Kwang Kim, Ji-Man Yu, Jongmin Kim, Sanghyeon Kim, and Yang-Kyu Choi. "3D Stackable Broadband Photoresponsive InGaAs Biristor Neuron for a Neuromorphic Visual System with Near 1 V Operation". *International Electron Devices Meeting (IEDM), Dec. 2021*.

## 수상과 선정

교수 소개에 게시된 수상·선정 가운데 2021년 10월 13일부터 2026년 10월 13일까지 범위에 해당하는 두 항목이다. 원문 날짜는 연도만 적혀 있다.[^professor]

- 2023 · 한국공학한림원(NAEK) 정회원 선출
- 2022 · Award of Dawon Kahng, The Korean Conference on Semiconductors (KCS)

## 연락과 위치

- 교수 연구실: E19 나노종합기술원 514호[^contact][^ee]
- 학생 연구실: E19 나노종합기술원 524호[^contact]
- 주소: 대전광역시 유성구 대학로 291 KAIST, 우편번호 34141[^contact]
- 연구실 전화: 042-350-5477[^contact]
- 교수 이메일: ykchoi@ee.kaist.ac.kr[^professor]
[^research]: 연구실 Research. <https://sites.google.com/view/nobelab/research> 관측 2026-10-26.
[^professor]: 연구실 Professor. <https://sites.google.com/view/nobelab/members/professor> 관측 2026-10-26.
[^ee]: KAIST 전기및전자공학부 최양규 교수 소개와 전임교수 명단. <https://ee.kaist.ac.kr/professor/12290/> <https://ee.kaist.ac.kr/professor-s1/3/> 관측 2026-10-26.
[^semicon]: KAIST 반도체공학대학원 연구실 목록. <https://semicon.kaist.ac.kr/sub02/view> 관측 2026-10-26.
[^phd]: 연구실 Ph. D. Candidate. <https://sites.google.com/view/nobelab/members/ph-d-candidate> 관측 2026-10-26.
[^postdoc]: 연구실 Post Doc. & Staff. <https://sites.google.com/view/nobelab/members/post-doc-staff> 관측 2026-10-26.
[^alumni]: 연구실 Alumni. <https://sites.google.com/view/nobelab/members/alumni> 관측 2026-10-26.
[^journal]: 연구실 Journal의 2021–2026년 구역. <https://sites.google.com/view/nobelab/Journal/journal> 관측 2026-10-26.
[^intl]: 연구실 International Conference. <https://sites.google.com/view/nobelab/Journal/intl-conference> 관측 2026-10-26.
[^contact]: 연구실 Contact Us. <https://sites.google.com/view/nobelab/contact-us> 관측 2026-10-26.
[^ms]: 연구실 M.S. Candidate. <https://sites.google.com/view/nobelab/members/m-s-candidate> 관측 2026-10-26.
[^p1]: S.-I. Kim 외, Y.-K. Choi, ACS Nano (누리집 2026년 구역). <https://doi.org/10.1021/acsnano.6c02362> 초록 기준(Crossref 등록 초록).
[^p2]: Y.-S. Chung, S.-Y. Yun, J.-K. Han, Y.-K. Choi, Nano Letters (누리집 2025년 구역). <https://doi.org/10.1021/acs.nanolett.5c00376> 초록 기준(OpenAlex 등록 초록).
[^p3]: H.-B. Noh 외, Y.-K. Choi, IEEE Electron Device Letters (누리집 2025년 구역). <https://doi.org/10.1109/led.2025.3580096> 초록 기준(OpenAlex 등록 초록).
[^p4]: D.-W. Kim 외, Y.-K. Choi, Energy & Environmental Science (누리집 2025년 구역). <https://doi.org/10.1039/d4ee03110e> 초록 기준(Crossref 등록 초록).
[^p5]: S.-Y. Yun, J.-K. Han, Y.-K. Choi, Nano Letters (누리집 2024년 구역). <https://doi.org/10.1021/acs.nanolett.3c04539> 초록 기준(OpenAlex 등록 초록).
[^p6]: S.-I. Kim 외, Y.-K. Choi, Science Advances (누리집 2024년 구역). <https://doi.org/10.1126/sciadv.adk6042> 초록 기준(Crossref 등록 초록).

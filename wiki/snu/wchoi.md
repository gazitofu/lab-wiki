# 초고주파집적시스템연구실 (High-frequency Integrated Circuits and Systems Research Group, HICS)

**서울대학교 공과대학 전기·정보공학부 · 최우열 부교수**

- 분야: 초고주파 집적회로와 시스템, 테라헤르츠 영상, 비선형 회로와 소자 계측
- 대분야: 전기전자·반도체·광학
- 태그: 집적회로 설계[^dept][^p1][^p2], 테라헤르츠 분광·소자[^p5][^p6], 무선·이동통신[^p3], 강유전체[^p8]
- 홈페이지: <https://www.wchoi.net/>

> 고속 연결과 무선 통신에 쓰는 송수신 회로, 테라헤르츠 영상용 화소 배열, 반도체 소자와 소재의 전기적 특성을 연구한다.

## 무엇을 연구하나

초고주파집적시스템연구실은 반도체 집적회로로 초고주파 응용 회로와 시스템을 만든다. 집적회로는 전자 부품과 연결선을 한 칩에 모은 회로다. 학과 소개는 회로 설계와 계측, 응용 시스템 구현, 비선형 회로 분석, 전력증폭기용 소자 계측과 모델링을 연구 분야로 든다. 전력증폭기는 신호가 전달하는 전력을 키우는 회로이며, 모델링은 대상의 동작을 수학식이나 계산 모형으로 나타내는 일이다. 신호는 정보를 나타내는 물리량의 변화다.[^dept][^faculty]

신호를 보내는 송신기와 받는 수신기의 회로를 연구한다. 고속 유전체 도파관 연결을 위한 전력증폭기를 만들고, 감지·통신 시스템에 쓸 밀리미터파 수신기를 구현했다. 유전체 도파관은 전기를 잘 통하지 않는 물질을 이용해 전자기파를 정해진 경로로 전하는 구조다. 또 송신 회로에 공급하는 전압을 데이터에 따라 바꾸는 전원 변조로 정보가 실린 신호를 만들었다.[^p2][^p3][^p4]

테라헤르츠 영상용 회로에서는 송신기와 수신기를 한 화소에 함께 넣고, 여러 화소가 동기화되어 동작하도록 배열한다. 화소는 영상을 이루는 한 점에 대응하는 검출 요소다. 최근 연구는 화소 사이의 연결 방식으로 외부 신호에 동기화되는 주파수 범위를 넓히고 이차원 배열을 구현했다. 테라헤르츠파는 마이크로파와 적외선 사이 주파수의 전자기파다. 전파를 만드는 회로로는 가변 용량 소자의 여러 단자를 이용해 입력 신호의 주파수를 올리는 송신기를 설계하고 계산으로 평가했다.[^p6][^p5]

소자 자체의 동작과 소재의 전기적 특성도 다룬다. 전류가 한쪽 방향으로 흐르는 성질을 이용하는 다이오드에 조절 전압을 걸어 누설 전류와 고주파 특성을 바꾸는 연구가 있다. 강유전체에서는 측정 구조의 기생 성분을 제거해 유전율을 구하는 방법을 제안하고, 주파수에 따라 유전율이 어떻게 달라지는지 분석했다.[^p7][^p8] 누리집은 연구를 테라헤르츠 마이크로전자공학, 마이크로파 기초 회로, 시스템·응용 공동 연구라는 세 갈래로 나눈다.[^research]

## 주요 연구 주제

### 고속 연결 회로의 모델링과 증폭

서로 영향을 주는 전송 경로의 특성으로 대칭 코일 구조를 모델링하고, 주파수에 따라 달라지는 기생 효과를 설계에 반영한다. 코일은 전류가 흐를 때 생기는 자기장을 이용하는 회로 부품이다. 송신 구동 회로를 제작해 모형과 측정값을 대조했다.[^p1] 고속 유전체 도파관 연결용 전력증폭기에서는 증폭을 맡는 부분과 회로 사이 연결을 설계해 동작 주파수 범위를 넓히고, 시제품의 출력과 효율을 측정했다.[^p2]

### 밀리미터파·테라헤르츠 송수신 회로

수신기에서는 주파수를 바꾸는 혼합기를 앞에 두고, 스위치와 증폭 회로를 함께 설계해 잡음과 동작 주파수 범위를 측정했다.[^p3] 송신기에서는 전원 변조로 데이터를 신호에 싣거나, 가변 용량 소자의 여러 단자를 이용해 입력 신호의 주파수를 올린다. 앞 연구는 회로의 측정 결과를, 뒤 연구는 시뮬레이션 결과를 제시한다.[^p4][^p5]

### 영상용 송수신 화소 배열

송수신 회로와 안테나를 화소에 함께 넣고, 여러 화소의 발진기를 연결해 외부 신호에 맞춰 동작하게 한다. 화소에 신호를 전달하는 방식과 화소 사이 동기화를 함께 고려해 주파수 동기화 범위를 넓히고 이차원 배열로 구현하는 방법을 연구한다.[^p6]

### 소자 설계와 강유전체 계측

다이오드의 게이트, 즉 전기적 동작에 영향을 주는 조절 단자에 전압을 걸어 누설 전류와 고주파 특성을 바꾼다. 소자 동작을 계산으로 분석하고 제작한 소자에서 특성을 측정했다.[^p7] 강유전체 연구에서는 측정 구조에 함께 나타나는 기생 성분을 제거한 뒤 유전율을 추출했다. 조사한 주파수 범위에서 유전율이 주파수 증가에 따라 감소하는 경향도 확인했다.[^p8]

## 대표 논문

서울대 부임 이후 출판된 논문 가운데 연결 회로 모델링·증폭, 송수신 회로, 영상용 화소 배열, 소자·소재 계측을 고르게 보여 주는 8편을 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다. 저자 역할은 랩 목록과 Crossref 등록 서지의 순서를 따랐다.[^pubs]

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Coupled-Line-Based Modeling and Design of Symmetric T-Coil Structures](https://doi.org/10.1109/TCSII.2026.3710230) · IEEE Transactions on Circuits and Systems II: Express Briefs | 고속 송신 구동 회로의 대칭 코일 구조를, 서로 영향을 주는 전송 경로의 특성으로 모델링했다. 주파수에 따라 달라지는 기생 효과를 모형에 넣고 설계에 쓸 식과 대응 관계를 구했다. 회로를 제작해 측정한 결과, 기존 모형에 비해 동작 주파수 범위와 지연 변화, 신호 반사에 대한 예측 오차를 줄였다.[^p1] | 1저자 Junyeop Kim, 마지막 저자 최우열 |
| 2 | 2026 | [A CMOS E/W-Band Power Amplifier with 53% Bandwidth Using an Over-Neutralized Active Core for Dielectric Waveguide Interconnects](https://doi.org/10.1109/IMSRFTT43070.2026.11602140) · IMS RFTT 2026 | 고속 유전체 도파관 연결에 쓰는 전력증폭기를 만들었다. 증폭을 맡는 회로와 단계 사이 연결을 함께 설계해 넓은 주파수 범위에서 동작하도록 하고, 불안정한 동작 가능성도 줄이려 했다. 시제품에서 동작 범위와 증폭 정도, 출력 전력, 효율을 측정했다.[^p2] | 1저자 Sungjun Lee, 마지막 저자 최우열 |
| 3 | 2025 | [W-band Mixer-First Receiver Using Floating Body Switches in 28-nm CMOS](https://doi.org/10.1109/APMC65046.2025.11376641) · APMC 2025 | 감지·통신 시스템을 위한 밀리미터파 수신기를 구현했다. 주파수를 바꾸는 혼합기를 앞에 놓고, 소자의 몸체에 고정된 전압을 연결하지 않는 스위치와 증폭기를 사용했다. 잡음, 동작 주파수 범위, 입력 신호가 커질 때 증폭 특성이 달라지는 정도와 전력 소모를 측정했다.[^p3] | 1저자 Kyubin Choi, 마지막 저자 최우열 |
| 4 | 2025 | [10-GSymbols/s Supply-Modulated APSKC SiGe HBT Transmitter RF Front End for Operation at 250 GHz With 6.8-dBm Peak Modulated Power](https://doi.org/10.1109/JSSC.2025.3575769) · IEEE Journal of Solid-State Circuits | 송신 회로의 전력증폭기에 공급하는 전압을 데이터에 따라 바꾸고, 신호의 크기와 주기 안의 위치를 함께 바꾸어 정보를 실었다. 회로를 제작해 정보 전송 속도와 출력 전력을 측정했다. 전송 속도는 측정 장비의 한계 안에서 얻은 값이며, 기존의 신호 변조 방식과 비교해 출력 전력과 전력 효율의 향상을 보고했다.[^p4] | 1저자 Haidong Guo, 공저 최우열(9명 중 5번째) |
| 5 | 2025 | [Terahertz Transmitter Frontend Using Multi-Port Varactors in 65-nm CMOS](https://doi.org/10.1109/ICCE-Asia67487.2025.11263663) · ICCE-Asia 2025 | 전압에 따라 전기를 저장하는 성질이 바뀌는 소자의 여러 단자를 이용해, 입력 신호의 주파수를 올리는 송신 회로를 제안했다. 원하는 주파수 성분을 얻고 원하지 않는 성분을 억제하도록 회로와 조절 전압을 정했다. 변환 과정에서의 증폭 정도와 출력 전력을 시뮬레이션으로 평가했다.[^p5] | 1저자 Saad Azmeen-ur-Rahman, 마지막 저자 최우열 |
| 6 | 2026 | [405-GHz 2×2 Concurrent Transceiver Pixel Array with 7.8-GHz Bandwidth Using Series-Coupled Standing-Wave Oscillators](https://doi.org/10.1109/RFIC70222.2026.11602373) · RFIC 2026 | 송신기와 수신기 기능, 안테나를 갖는 화소를 이차원으로 배열했다. 화소들의 발진기를 연결하고 외부 신호에 맞춰 동작하도록 해, 화소 사이 동기화와 신호 전달을 함께 다뤘다. 제작한 배열에서 동기화 가능한 주파수 범위와 전파 출력, 수신 잡음을 측정해 배열을 확장하는 회로 방법을 보였다.[^p6] | 1저자 Seungmo Noh, 공저 최우열(7명 중 6번째) |
| 7 | 2025 | [Biased Poly-gate-separated Schottky Barrier Diode in CMOS](https://doi.org/10.5573/JSTS.2025.25.4.414) · Journal of Semiconductor Technology and Science | 다이오드의 조절 단자에 전압을 걸어 누설 전류나 고주파 특성을 개선하는 소자를 제안했다. 소자의 동작을 계산으로 분석하고 기존 제작 공정을 바꾸지 않고 만들어 측정했다. 조절 전압에 따라 누설 전류를 줄이거나 고주파 동작 특성을 높일 수 있음을 보였다.[^p7] | 1저자 Deokgi Kim, 공저 최우열(4명 중 3번째) |
| 8 | 2024 | [Novel Ultra-Wideband Characterization Method for Ferroelectric's Non-Linearity](https://doi.org/10.1109/APMC60911.2024.10867608) · APMC 2024 | 강유전체의 전기적 특성을 넓은 주파수 범위에서 분석했다. 측정 구조의 기생 성분을 제거해 물질의 유전율을 구하는 방법을 제안했다. 조사한 범위에서는 가한 직류 전압(양·음의 방향이 바뀌지 않는 전압)과 관계없이 주파수가 증가하면 유전율이 감소하는 경향을 확인했다.[^p8] | 1저자 Yunsang Shin, 공저 최우열(6명 중 3번째) |


## 교수와 전문 분야

최우열 교수는 2001년 연세대학교 전자공학 학사, 2003년 서울대학교 전기공학 석사, 2011년 서울대학교 전기공학 박사 학위를 받았다. 누리집은 2011년 서울대학교 연구원, 2011–2013년 University of Texas at Dallas 연구원, 2013–2018년 같은 대학 연구조교수, 2018–2023년 Oklahoma State University 조교수 경력을 적는다.[^pi] 서울대 부임 소식은 2023년 8월이며, 누리집 경력은 2023–2025년 서울대 조교수와 2025년 이후 부교수로 나뉜다. 2025년 9월 소식은 정년보장 없는 부교수 승진이라고 적는다.[^home][^pi]

교수의 연구 관심은 무선주파수(RF, radio frequency)부터 테라헤르츠까지의 집적회로·시스템과 마이크로파 고출력 소자 계측이다.[^pi] 학과 소개는 초고주파 집적회로 설계·계측, 초고주파 응용 시스템 설계·구현, 비선형 초고주파 회로 분석·설계, 전력증폭기용 소자 계측·모델링을 적는다.[^faculty] 최근 논문으로 보면 연결 회로의 모델링과 증폭, 밀리미터파·테라헤르츠 송수신 회로, 영상용 화소 배열, 소자·소재의 전기적 특성 분석이 전문 분야의 구체적인 사례다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

학술 활동으로는 한국전자파학회 2024년 집행이사(국제), 2025년 집행이사(학술), 2026년 상임이사(국제)를 적는다. 학회 위원 활동은 IMS 2026 RFSA 운영위원회 홍보 담당, ISSCC 2026 기술 프로그램 위원회 RF 분과, APMC 2025 특별세션 위원장·기술 프로그램 위원, 2026년 전자파학회 동계학술대회 특별세션 분과 운영위원, 2025년 하계학술대회 주제강연 분과 운영위원과 동계학술대회 포상 분과 운영위원이다. 2023년부터 Journal of Electromagnetic Engineering and Science의 부편집위원(Associate Editor)도 맡고 있다.[^pi]

## 응용 분야

고속 유전체 도파관 연결을 위한 전력증폭기와 밀리미터파 감지·통신 시스템용 수신기를 연구한다.[^p2][^p3] 영상 분야에서는 테라헤르츠 송수신 화소를 이차원 배열로 확장하는 회로를 다룬다.[^p6] 첫 화면의 과제 소식에는 다중입출력 레이더용 시스템온칩, 이중 대역 테라헤르츠 영상 회로, 고속 유선 인터페이스, 집적 테라헤르츠 송수신기 연구가 있다. 다중입출력은 송신·수신 경로를 각각 여럿 사용하는 구성이고, 시스템온칩은 시스템의 여러 기능을 한 칩에 모은 회로다.[^home]

## 구성원

누리집 Team 페이지의 대학원 연구조교 14명과 연구 인턴 5명이다. 대학원생 명단의 기준 표기는 2026년 9월, 인턴 명단은 2026년 7월이며 열람일은 2026년 10월 27일이다. 대학원생 과정은 모두 Master-PhD track student로 적혀 있어 석박사통합과정으로 옮겼다. 인턴은 게시된 프로그램 이름을 함께 적었다. 연구 주제와 시작 기간은 누리집 표기다.[^team] "대표 논문 참여"는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Choi, Kyubin 최규빈 | 석박사통합과정 | 2024.03 - present | Millimeter-wave and Terahertz receiver | 1, 2, 3 |
| Lee, Sungjun 이성준 | 석박사통합과정 | 2024.03 - present | Power amplifiers for communication and radar sensing | 1, 2, 3 |
| Noh, Seungmo 노승모 | 석박사통합과정 | 2024.03 - present | Millimeter-wave and Terahertz signal generator | 3, 6 |
| Kim, Junyeop 김준엽 | 석박사통합과정 | 2024.09 - present | Wideband transmitter, digital RF | 1, 3 |
| Lee, Young Han 이영한 | 석박사통합과정 | 2024.09 - present | Millimeter-wave receiver, dielectric waveguide | 2, 3 |
| Lee, Minseok 이민석 | 석박사통합과정 | 2025.03 - present | Power amplifiers for communication |  |
| Lee, Young-Joon 이영준 | 석박사통합과정 | 2025.03 - present | Terahertz transmitter | 5, 6 |
| Mun, Seongjae 문성재 | 석박사통합과정 | 2025.03 - present | Millimeter-wave and Terahertz circuits | 6 |
| Park, Jaehyeon 박재현 | 석박사통합과정 | 2025.03 - present | Power amplifiers for communication and radar sensing |  |
| Park, Sungjae 박성재 | 석박사통합과정 | 2025.09 - present | RF and millimeter-wave receivers, SIC |  |
| Han, Seungho 한승호 | 석박사통합과정 | 2026.03 - present |  |  |
| Kim, Minseok 김민석 | 석박사통합과정 | 2026.03 - present |  |  |
| Kim, Daniel 김상형 | 석박사통합과정 | 2026.09-present |  |  |
| Lee, Hongju 이홍주 | 석박사통합과정 | 2026.09-present |  |  |
| Chung, Hyunbin, 정현빈 | 인턴 (공학연구실습) | 2025.07 |  |  |
| Won, Jaehee, 원재희 | 인턴 (공학연구실습) | 2026.01 |  |  |
| Han, GwangHeon, 한광헌 | 인턴 (미래인재인턴십) | 2026.07 |  |  |
| Kim, Junghun, 김정헌 | 인턴 (공학연구실습) | 2026.07 |  |  |
| Lim, Taehyun, 임태현 | 인턴 (공학연구실습) | 2026.07 |  |  |

## 졸업생과 이전 구성원

Team 페이지 Former Members 가운데 활동 종료 시기가 2022–2026년인 11명이다. 게시된 활동 기간은 2020–2026년에 걸쳐 있고, 학위 졸업생뿐 아니라 이전 박사과정생·학부 연구생·인턴도 포함한다. 2023년 8월 서울대 부임 전 Oklahoma State University 시절 구성원 기록이 섞인 교수 개인의 명단이다. 진로는 원문이 적은 첫 진로이며, 기간의 끝을 학위 취득일로 해석하지 않는다.[^team]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Azmeen Rahman | PhD graduate (2020 - 2025) | Qorvo |
| Haniye Mehraban | PhD student (2022 - 2023) | Oklahoma State U. (Grad Student/Prof. J. Hu) |
| Matthew Otto | Undergrad researcher (2020), NSF-REU Scholar (2021), CEAT URS (2022) (2020 - 2022) |  |
| Hwang, Suenghwan 황승환 | Undergrad intern (2024.01-02) |  |
| Ahn, Heegyun 안희균 | Undergrad Intern (미래인재인턴십) (2025.01-02) |  |
| Namkung, Minseo 남궁민서 | Undergrad Intern (미래인재인턴십) (2025.01-02) |  |
| Kim, Seonggyun 김성균 | Undergrad Intern (미래인재인턴십) (2025.07-08) |  |
| Chae, Beomjoon 채범준 | Undergrad Intern (공학연구실습 (24), 자율연구 (25.03)) (2024.03-26.02) | Seoul National U. (Grad Student/Prof. S. Yu) |
| Kim, Tong Joon 김동준 | Undergrad Intern (공학연구실습 (24), 졸업연구 (24.09), 자율연구 (25.03)) (2024.01-26.06) | MIT (Grad Student/Prof. R. Han) |
| Kwon, Jina 권진아 | Undergrad Intern (공학연구실습, 졸업연구 (26.03)) (2025.09-26.06) | SK Hynix |
| Kim, Namkwon 김남권 | Undergrad Intern (미래인재인턴십) (2026.01-06) |  |

## 논문 목록 (2021–2026 및 연도 미표기)

누리집 Publications의 국제 학술지 18건과 국제 학회 19건, 합계 37건이다. 2021–2026년 서지 36건과 연도 미표기 1건을 구분했다. 논문은 테라헤르츠 영상·송수신 회로, 신호 생성, 통신용 회로, 소자 계측 등을 다룬다. 2023년 8월 서울대 부임 전 Oklahoma State University 등 이전 소속 시절 논문도 포함하는 교수 개인 목록이다. 2021년 논문은 그해 전체를 포함했다.[^pubs]

대칭 T 코일 논문은 OpenAlex 등록 연도 2026년으로 분류했고, 첫 화면의 2026년 7월 게재 승인 소식도 함께 적었다. 380-GHz 신호 생성 논문은 초록 등록 페이지의 2025년 표기를 따랐다. 손잡기 상태에 반응하는 안테나 모듈 논문은 누리집 서지에 연도가 없어 마지막에 따로 두었다.[^home][^pubs][^p1][^year380]

**2026**

- J. Kim, S. Lee, K. Choi and W. Choi. "Coupled-Line-Based Modeling and Design of Symmetric T-coil Structures". *in IEEE Transactions on Circuits and Systems II: Express Briefs (TCSII), doi: 10.1109/TCSII.2026.3710230. (2026-07 소식: 게재 승인)*.
- G. Murugesan, M. Awais, S. Shariff, F. Zhang, W. Choi and K. K. O. "400-GHz Concurrent Transceiver Pixels for Short Range FMCW Radar Imaging". *in IEEE Transactions on Microwave Theory and Techniques (TMTT), doi: 10.1109/TMTT.2026.3672715*.
- S. Lee, Y. Lee, K. Choi and W. Choi. "A CMOS E/W-Band Power Amplifier with 53% Bandwidth Using an Over-Neutralized Active Core for Dielectric Waveguide Interconnects". *2026 IEEE MTT-S Radio Frequency Technology and Techniques Symposium (IMS RFTT), Boston, MA, USA, 2026, pp. 319-322, doi: 10.1109/IMSRFTT43070.2026.11602140*.
- S. Noh, G. Murugesan, S. Mun, Y. -J. Lee, F. Zhang, W. Choi, K. O. "405-GHz 2×2 Concurrent Transceiver Pixel Array with 7.8-GHz Bandwidth Using Series-Coupled Standing-Wave Oscillators". *2026 IEEE Radio Frequency Integrated Circuits Symposium (RFIC), Boston, MA, USA, 2026, pp. 187-190, doi: 10.1109/RFIC70222.2026.11602373*.

**2025**

- H. Guo, S. Ghosh, F. Zhang, S. Lee, W. Choi, S. Dong, I. Momson, K. Strecker, K. K. O. "10-GSymbols/s Supply-Modulated APSKC SiGe HBT Transmitter RF Front End for Operation at 250 GHz With 6.8-dBm Peak Modulated Power". *in IEEE Journal of Solid-State Circuits (JSSC), vol. 60, no. 9, pp. 3082-3094, Sept. 2025, doi: 10.1109/JSSC.2025.3575769*.
- D. Kim, J. Noh, W. Choi, and D. Shim. "Biased Poly-gate-separated Schottky Barrier Diode in CMOS". *JOURNAL OF SEMICONDUCTOR TECHNOLOGY AND SCIENCE, vol. 25, no. 4, pp. 414–419, Aug. 2025, doi: 10.5573/JSTS.2025.25.4.414*.
- Z. Chen, H. Dong, Z. Chen, W. Choi, J.-X. Chen, K. K. O, and W. Hong. "380-GHz Third Harmonic Signal Generation Using Differentially Pumped Varactors in a CMOS Voltage Controlled Oscillator". *in IEEE TCSI, doi: 10.1109/TCSI.2024.3519170*.
- K. Choi, Y. Lee, S. Noh, S. Lee, J. Kim and W. Choi. "W-band Mixer-First Receiver Using Floating Body Switches in 28-nm CMOS". *2025 Asia-Pacific Microwave Conference (APMC), Jeju, Korea, Republic of, 2025, pp. 1-3, doi: 10.1109/APMC65046.2025.11376641*.
- S. Azmeen-ur-Rahman, Y. -J. Lee and W. Choi. "Terahertz Transmitter Frontend Using Multi-Port Varactors in 65-nm CMOS". *2025 IEEE/IEIE International Conference on Consumer Electronics-Asia (ICCE-Asia), Busan, Korea, Republic of, 2025, pp. 1-5, doi: 10.1109/ICCE-Asia67487.2025.11263663*.
- (invited) W. Choi and K. K. O. "CMOS Compact Concurrent Transceiver Pixel Arrays for Terahertz Imaging Applications". *2025 55th European Microwave Conference (EuMC), Utrecht, Netherlands, 2025, pp. 2-5, doi: 10.23919/EuMC65286.2025.11235271*.
- (invited) W. Choi and K. K. O. "Reflection-Mode Terahertz Imaging using Concurrent Transceiver Pixel Arrays in CMOS". *2025 IEEE International Symposium on Radio-Frequency Integration Technology (RFIT), Kagoshima, Japan, 2025, pp. 109-111, doi: 10.1109/RFIT65667.2025.11364562*.
- G. Murugesan, M. Awais, S. Shariff, Y. Zhu, P. R. Byreddy, F. Zhang, W. Choi, and K. K. O. "400-GHz Concurrent Transceiver Imaging Pixel with Improved Noise Performance and Increased Injection Locking Range". *IEEE RFIC, San Francisco, CA, USA, 2025, pp. 303-306, doi: 10.1109/RFIC61188.2025.11082853*.

**2024**

- W. Choi and K. K. O. "Enabling Applications of Electromagnetic Waves at 0.3–1.0 THz Using Silicon Electronic Integrated Circuits". *ACS Photonics, Mar. 2024, doi: 10.1021/acsphotonics.3c01129*.
- P. R. Byreddy, Y. Zhu, S. Ghosh, H. S. Bakshi, W. S. Portillo, J. P. Van Marter, K. K. O, W. Choi. "Array of 296-GHz CMOS Concurrent Transceiver Pixels With Phase and Amplitude Extraction Circuits for Improving Reflection-Mode Imaging Resolution". *in IEEE Transactions on Terahertz Science and Technology (TTHZ), vol. 14, no. 2, pp. 216-227, March 2024, doi: 10.1109/TTHZ.2024.3350515*.
- Y. Shin, S. Nam, W. Choi, D. Kim, D. -H. Choe and S. -G. Nam. "Novel Ultra-Wideband Characterization Method for Ferroelectric's Non-Linearity". *in IEEE APMC, Bali, Indonesia, 2024, pp. 1078-1080, doi: 10.1109/APMC60911.2024.10867608*.
- H. Guo, S. Ghosh, F. Zhang, S. Lee, W. Choi, S. Dong, and K. K. O. "10-GSymbols/s Supply Modulated 250-GHz SiGe HBT Transmitter RF Front-End with 6.8-dBm Peak Modulated Power". *2024 IEEE BiCMOS and Compound Semiconductor Integrated Circuits and Technology Symposium (BCICTS), Fort Lauderdale, FL, USA, 2024, pp. 181-184, doi: 10.1109/BCICTS59662.2024.10745659*.
- J. Hu, J. Stine, W. Choi, and E. Dyke. "Research Experiences for Teachers on Chip Design". *in 2024 IEEE International Symposium on Circuits and Systems (ISCAS), May 2024, pp. 1–5. doi: 10.1109/ISCAS58744.2024.10558044*.

**2023**

- K. K. O, W. Choi, and R. Han. "Perspective on active submillimeter electromagnetic wave imaging using CMOS integrated circuits technologies". *Journal of Applied Physics, vol. 133, no. 15, p. 150903, Apr. 2023, doi: 10.1063/5.0143622*.
- P. R. Byreddy, W. E. Sosa, Y. Zhu, Z. Chen, B. Pouya, W. Choi, and K. K. O. "Lens-less Short-Range Reflection-Mode Imaging at 275 GHz Using CMOS Concurrent Transceivers". *in IEEE Sensors Letters, vol. 7, no. 2, pp. 1-4, Feb. 2023, Art no. 3500204, doi: 10.1109/LSENS.2023.3239804*.
- S. Azmeen-ur-Rahman, M. O. Hasna, S. Ekin, and W. Choi. "Two-Port Characterization of Symmetric Varactors in 65-nm CMOS Process for Mixer Applications". *in 2023 IEEE Texas Symposium on Wireless and Microwave Circuits and Systems (WMCS), Apr. 2023, pp. 1–4. doi: 10.1109/WMCS58822.2023.10194281*.
- H. Mehraban, W.-S. Park, H.-B. Jo, S.-M. Choi, D.-H. Kim, S.-K. Kim, J. Yun, T. Kim, W. Choi. "A W-Band Low-Noise Amplifier in 50-nm InP HEMT Technology". *in IEEE WMCS, Apr. 2023, pp. 1–4. doi: 10.1109/WMCS58822.2023.10194275*.
- K. Strecker, W. Choi, J. O’Hara. "A Wideband Millimeter-Wave Communication and Sensing Testbed for 75-500 GHz". *in IEEE WMCS, Apr. 2023, pp. 1–5. doi: 10.1109/WMCS58822.2023.10194272*.
- W. Choi, Y. Zhu, P. R. Byreddy, S. Dong, K. K. O. "430-GHz Concurrent Transceiver Array in CMOS for Power-efficient High-Resolution Stand-off Imaging". *2023 Government Microcircuit Applications and Critical Technology Conference (GOMACTech), Mar. 2023*.

**2022**

- K. K. O, W. Choi, Y. Zhu and H. Guo. "CMOS Platform for Everyday Applications Using Sub-Millimeter Electromagnetic Waves". *in IEEE Open Journal of the Solid-State Circuits Society, 2022, doi: 10.1109/OJSSCS.2022.3222121*.
- W. Raza, E. Abele, J. O'Hara, B. Sadr, P. LoPresti, A. Imran, W. Choi, I. Song, S. Altunc, O. Kegege, and S. Ekin. "Towards a Hybrid RF/Optical Lunar Communication System (LunarComm)". *in IEEE Network, vol. 36, no. 6, pp. 76-83, November/December 2022, doi: 10.1109/MNET.103.2100419*.
- Y. Zhu, P. R. Byreddy, K. K. O, and W. Choi. "426-GHz Concurrent Transceiver Pixel in 65-nm CMOS for Active Imaging". *in IEEE TTHZ, vol. 12, no. 5, pp. 446-456, Sept. 2022, doi: 10.1109/TTHZ.2022.3183159*.
- Z. Chen, W. Choi and K. K. O. "300-GHz Double-Balanced Up-Converter Using Asymmetric MOS Varactors in 65-nm CMOS". *in IEEE JSSC, vol. 57, no. 8, pp. 2336-2347, Aug. 2022, doi: 10.1109/JSSC.2022.3171545*.
- H. S. Cankurtaran, A. Kachroo, W. Choi, J. O'Hara, S. Yarkan, K. A. Qaraqe, M. O. Hasna, and S. Ekin. "Propeller Effects on mmWave UAV Channels: A Statistical and Empirical Modeling Study". *2022 IEEE International Black Sea Conference on Communications and Networking (BlackSeaCom), 2022, pp. 30-35, doi: 10.1109/BlackSeaCom54372.2022.9858315*.
- M. T. Anas, S. Azmeen-ur-Rahman and W. Choi. "A 410-GHz Detector using AC-coupled Substrate-Integrated Waveguide Slot Antenna in CMOS". *in IEEE WMCS, 2022, pp. 1-5, doi: 10.1109/WMCS55582.2022.9866391*.
- Y. Zhu, P. R. Byreddy, S. Dong, K. K. O and W. Choi. "A 430GHz CMOS Concurrent Transceiver Pixel Array for High Angular Resolution Reflection-Mode Active Imaging". *2022 IEEE International Solid-State Circuits Conference (ISSCC), 2022, pp. 1-3, doi: 10.1109/ISSCC42614.2022.9731698*.

**2021**

- A. Kachroo, C. A. Thornton, M. A. R. Sarker, W. Choi, H. Bai, I. Song, J. O'Hara, and S. Ekin. "Emulating UAV Motion by Utilizing Robotic Arm for mmWave Wireless Channel Characterization". *in IEEE Transactions on Antennas and Propagation, vol. 69, no. 10, pp. 6691-6701, Oct. 2021, doi: 10.1109/TAP.2021.3069484*.
- H. S. Bakshi, S. Dong, I. Momson, D. Chacon, Z. Chen, W. Choi, A. J. Blanchard, and K. K. O. "180-GHz Broadside Radiation Bond-Wire Antenna for Short-Range Wireless Communication". *in IEEE Transactions on Components, Packaging and Manufacturing Technology, vol. 11, no. 3, pp. 530-532, March 2021, doi: 10.1109/TCPMT.2021.3053558*.
- S. Dong, I. Momson, S. Kshattry, P. Yelleswarapu, W. Choi and K. K. O. "A 10-Gb/s 180-GHz Phase-Locked-Loop Minimum Shift Keying Receiver". *in IEEE JSSC, vol. 56, no. 3, pp. 681-693, March 2021, doi: 10.1109/JSSC.2020.3032972*.
- Q. Zhong, W. Choi and K. K. O. "Terahertz Even-Order Subharmonic Mixer Using Symmetric MOS Varactors". *in IEEE JSSC, vol. 56, no. 2, pp. 355-366, Feb. 2021, doi: 10.1109/JSSC.2020.3024177*.
- C. Thornton, A. Kachroo, H. Bai, S. Ekin, and W. Choi. "De-embedding Motion Artifacts from Robotic Arm Assisted Propagation Measurements". *IEEE WMCS, 2021, pp. 1-6, doi: 10.1109/WMCS52222.2021.9493296*.
- Z. Chen, W. Choi and K. K. O. "23.1 270-to-300GHz Double-Balanced Parametric Upconverter Using Asymmetric MOS Varactors and a Power-Splitting-Transformer Hybrid in 65nm CMOS". *IEEE ISSCC, 2021, pp. 324-326, doi: 10.1109/ISSCC42613.2021.9365953*.

**연도 표기 없음**

- G. Lee, J. -U. Yoo, S. Park, H. -W. Son, J. -M. Kim, W. Choi, and D. Im. "A Handgrip-Responsive mmWave Phased Array Antenna-PA Module With Antenna-Based Capacitive Sensor for EIRP Recovery via Adaptive Current Redistribution". *in IEEE Transactions on Circuits and Systems I: Regular Papers (TCSI), doi: 10.1109/TCSI.2026.3666207*.

## 과제와 지원 선정

첫 화면의 2022년 8월–2026년 4월 과제·지원 선정 소식 6건이다. 날짜는 소식의 연월이며 과제 전체 수행 기간을 뜻하지 않는다. 2023년 8월 서울대 부임 전 Oklahoma State University 시절 항목을 포함한다. Co-PI는 공동 연구책임자라는 원문 역할 표기다.[^home]

- 2026-04 · 서브테라헤르츠 다중입출력 레이더 시스템온칩 개발 (지원 KEIT·MOTIR, KCHIPS (누리집 사업 표기: 민관민관공동투자반도체고급인력양성사업))
- 2025-02 · 이중 대역 테라헤르츠 영상 회로 연구 제안 선정 (지원 한국연구재단 개인연구 우수신진연구과제)
- 2024-07 · 0.5Tb/s급 Sub-THz 주파수 대역 고속 유선 인터페이스 연구실(TWINCL Lab) 제안 선정 (지원 한국연구재단 기초연구실; 역할 최재혁(연구책임자), 최우석, DGIST 김가인과 공동 제안)
- 2024-06 · 집적 테라헤르츠 송수신기 연구 제안 선정 (지원 서울대학교 창의선도 신진연구자 지원사업)
- 2023-01 · RET Site: Chip Design Experiences for Teachers to Stimulate Semiconductor Education in Oklahoma (지원 NSF; 역할 최우열 Co-PI)
- 2022-08 · Versatile Experimental Platform for 6G and Beyond Communications and Sensing Innovations (지원 NASA; 역할 최우열 Co-PI)

## 수상과 선정

첫 화면의 2024년 8월–2026년 2월 수상 소식 6건이다. 날짜와 수상 등급, 학부 인턴·멘토 표기는 각 공지를 따른다.[^home]

- 2026-02 · 학부 인턴 Hongju의 포스터가 2026년 전자파학회 동계학술대회 학부 우수 논문 선정 (누리집 멘토 표기: Jaehyun)
- 2026-01 · Kyubin의 연구가 반도체 학술대회 현장우수포스터상 선정 (누리집 영문 행사 표기: KCS 2025 - Chip Design Contest)
- 2025-10 · Seungmo의 조향 가능한 초점면 배열 논문이 제25회 RF/아날로그 회로 워크샵 RF 집적회로연구회 운영위원장상 수상 (원문 3rd place)
- 2025-08 · Sungjun·Younghan의 W 대역 저잡음 증폭기·전력증폭기 논문이 2025년 전자파학회 하계학술대회 우수 포스터 논문 선정
- 2025-02 · Kyubin·Seungmo의 포스터가 2025년 전자파학회 동계학술대회 우수 포스터 논문 선정
- 2024-08 · 학부 인턴 Tong Joon의 포스터가 2024년 전자파학회 하계학술대회 학부 우수 논문 선정 (누리집 멘토 표기: Kyubin)

## 소식

2022년 3월–2026년 7월의 논문·과제·수상 소식 21건이다. 위 과제·수상 절의 항목도 날짜순으로 함께 담았다. 2023년 8월 서울대 부임 전 Oklahoma State University 시절 항목이 섞여 있으며, 채택·게재 승인·출판은 공지가 사용한 상태를 구분했다.[^home]

- 2026-07 · Junyeop의 대칭 T 코일 모델링·설계 논문이 IEEE Transactions on Circuits and Systems II에 게재 승인. 삼성전자 연구지원금 지원
- 2026-04 · 서브테라헤르츠 다중입출력 레이더 시스템온칩 개발
- 2026-02 · Seungmo의 테라헤르츠 영상용 화소 배열 논문이 IMS RFIC 2026에 채택. UT Dallas Kenneth O 교수와 협력, Semiconductor Research Corporation 지원
- 2026-02 · 학부 인턴 Hongju의 포스터가 2026년 전자파학회 동계학술대회 학부 우수 논문 선정 (누리집 멘토 표기: Jaehyun)
- 2026-01 · Sungjun의 E/W 대역 전력증폭기 논문이 IMS RFTT 2026에 채택. 한국연구재단 기초연구실 지원
- 2026-01 · Kyubin의 연구가 반도체 학술대회 현장우수포스터상 선정 (누리집 영문 행사 표기: KCS 2025 - Chip Design Contest)
- 2025-10 · Seungmo의 조향 가능한 초점면 배열 논문이 제25회 RF/아날로그 회로 워크샵 RF 집적회로연구회 운영위원장상 수상 (원문 3rd place)
- 2025-08 · Kyubin의 W 대역 수신기 논문이 APMC 2025에 채택
- 2025-08 · Sungjun·Younghan의 W 대역 저잡음 증폭기·전력증폭기 논문이 2025년 전자파학회 하계학술대회 우수 포스터 논문 선정
- 2025-02 · 이중 대역 테라헤르츠 영상 회로 연구 제안 선정
- 2025-02 · Kyubin·Seungmo의 포스터가 2025년 전자파학회 동계학술대회 우수 포스터 논문 선정
- 2024-08 · 학부 인턴 Tong Joon의 포스터가 2024년 전자파학회 하계학술대회 학부 우수 논문 선정 (누리집 멘토 표기: Kyubin)
- 2024-07 · 0.5Tb/s급 Sub-THz 주파수 대역 고속 유선 인터페이스 연구실(TWINCL Lab) 제안 선정
- 2024-06 · 집적 테라헤르츠 송수신기 연구 제안 선정
- 2024-04 · Oklahoma State University John Hu 교수가 NSF RET 과제의 첫해 결과를 ISCAS 2024 교육 세션에서 발표할 예정이라고 공지
- 2024-03 · 최우열·Kenneth O의 실리콘 집적회로 응용 전망 논문이 ACS Photonics에 출판
- 2024-03 · Pranith의 진폭·위상 출력을 갖는 송수신 화소와 반사 영상 논문 출판. UT Dallas Kenneth O 교수와 공동 연구
- 2023-01 · RET Site: Chip Design Experiences for Teachers to Stimulate Semiconductor Education in Oklahoma
- 2022-08 · Versatile Experimental Platform for 6G and Beyond Communications and Sensing Innovations
- 2022-06 · Yukun의 논문이 IEEE Transactions on Terahertz Science and Technology에 게재 승인. 2019년 VLSI 논문의 설계 설명을 확장한 판이라고 소개
- 2022-03 · Anas의 검출기 논문이 2022 IEEE Texas Symposium on Wireless and Microwave Circuits and Systems에 채택

## 연락과 위치

- 교수 사무실: 서울대학교 301동 807호[^faculty]
- 연구실: 서울대학교 301동 652-1호[^lab]
- 전화: 02-880-1817[^faculty]
[^home]: HICS@SNU 첫 화면, News & announcement. <https://www.wchoi.net/> 2026-10-27 열람.
[^pi]: HICS@SNU PI, 경력·학력·연구 관심·학술 활동. <https://www.wchoi.net/pi> 2026-10-27 열람.
[^team]: HICS@SNU Team, Graduate Research Assistants·Research Interns·Former Members. <https://www.wchoi.net/team> 2026-10-27 열람.
[^research]: HICS@SNU Research, 세 연구 갈래 제목. <https://www.wchoi.net/research> 2026-10-27 열람.
[^pubs]: HICS@SNU Publications, International Journal Articles·International Conference Papers. <https://www.wchoi.net/publications> 2026-10-27 열람.
[^faculty]: 서울대학교 전기·정보공학부 최우열 교수 소개. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p892> 2026-10-27 열람.
[^dept]: 서울대학교 전기·정보공학부 초고주파집적시스템연구실 소개. <https://ece.snu.ac.kr/research-faculty/research/lab?labidx=132&md=view> 2026-10-27 열람.
[^lab]: HICS@SNU Lab, 연구실 위치. <https://www.wchoi.net/lab> 2026-10-27 열람.

[^year380]: 380-GHz 신호 생성 논문의 ResearchGate 등록 서지, 2025년과 72권 7호 표기. <https://www.researchgate.net/publication/388716036_380-GHz_Third_Harmonic_Signal_Generation_Using_Differentially_Pumped_Varactors_in_a_CMOS_Voltage_Controlled_Oscillator> 2026-10-27 열람.

[^p1]: J. Kim, S. Lee, K. Choi, W. Choi, IEEE Transactions on Circuits and Systems II: Express Briefs (2026). <https://doi.org/10.1109/TCSII.2026.3710230> 초록 기준(OpenAlex 등록 초록).
[^p2]: S. Lee, Y. Lee, K. Choi, W. Choi, 2026 IEEE MTT-S Radio Frequency Technology and Techniques Symposium (IMS RFTT), 319-322 (2026). <https://doi.org/10.1109/IMSRFTT43070.2026.11602140> 초록 기준(OpenAlex 등록 초록).
[^p3]: K. Choi 외, W. Choi, 2025 Asia-Pacific Microwave Conference (APMC), 1-3 (2025). <https://doi.org/10.1109/APMC65046.2025.11376641> 초록 기준(OpenAlex 등록 초록).
[^p4]: H. Guo 외, K. K. O, IEEE Journal of Solid-State Circuits 60, 3082-3094 (2025). <https://doi.org/10.1109/JSSC.2025.3575769> 초록 기준(OpenAlex 등록 초록).
[^p5]: S. Azmeen-ur-Rahman, Y.-J. Lee, W. Choi, 2025 IEEE/IEIE International Conference on Consumer Electronics-Asia (ICCE-Asia), 1-5 (2025). <https://doi.org/10.1109/ICCE-Asia67487.2025.11263663> 초록 기준(OpenAlex 등록 초록).
[^p6]: S. Noh 외, K. K. O, 2026 IEEE Radio Frequency Integrated Circuits Symposium (RFIC), 187-190 (2026). <https://doi.org/10.1109/RFIC70222.2026.11602373> 초록 기준(OpenAlex 등록 초록).
[^p7]: D. Kim, J. Noh, W. Choi, D. Shim, JOURNAL OF SEMICONDUCTOR TECHNOLOGY AND SCIENCE 25, 414–419 (2025). <https://doi.org/10.5573/JSTS.2025.25.4.414> 초록 기준(OpenAlex 등록 초록).
[^p8]: Y. Shin 외, S.-G. Nam, 2024 IEEE Asia-Pacific Microwave Conference (APMC), 1078-1080 (2024). <https://doi.org/10.1109/APMC60911.2024.10867608> 초록 기준(OpenAlex 등록 초록).

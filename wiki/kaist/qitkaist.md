# 양자정보이론 연구실 (QIT @ KAIST)

**KAIST 전기및전자공학부 · 배준우 교수**

- 분야: 양자정보이론, 얽힘 검출과 증명, 양자 상태 구별과 측정, 양자 네트워크·통신 이론, 양자 컴퓨터 측정 오류 완화
- 홈페이지: <https://sites.google.com/view/qitkaist>
- 근거와 출처: [QIT 근거 페이지](qitkaist-sources.md)

> 양자역학으로 정보를 다룰 때 무엇이 가능하고 어디까지가 한계인지를 이론으로 밝히는 연구실이다. 적은 측정으로 얽힘을 찾아내고 증명하는 방법, 양자 상태를 높은 신뢰도로 가려내는 측정, 양자 자원으로 통신을 더 잘하는 부호화, 오늘날 잡음 많은 양자 컴퓨터의 측정 오류를 줄이는 방법을 연구하고, 국내외 실험 연구진과 함께 검증한다.[^research][^recent][^p1][^p2][^p5][^p8]

## 무엇을 연구하나

연구실은 연구 관심사를 양자정보이론(Quantum Information Theory)으로 적고, 최근 결과를 네 갈래로 소개한다. 실험 연구진과 함께하는 이론 연구, 오늘날 양자 기술의 알고리즘과 하드웨어 접점을 다루는 양자 공학, 양자 채널과 양자 규약의 근본 한계, 얽힘 이론이다.[^recent] 양자 채널·규약 갈래는 양자 시스템으로 고전적 한계를 넘는 높은 보안성과 더 효율적인(용량이 큰) 네트워크 통신에 관심을 둔다고 적었다.[^recent]

첫째 갈래는 **얽힘**(여러 입자의 상태를 입자 하나하나의 상태로 나누어 쓸 수 없는 양자 상관) **검출과 증명**이다. 얽힘 증인(entanglement witness, 분리 가능한 상태에서는 기댓값이 0 이상이고 이 부등식이 깨지면 얽힘으로 판정하는 관측량)에 상한도 있다는 "거울 얽힘 증인"을 여러 입자계와 고차원계로 넓혔고,[^p1] 측정할 수 있는 관측량이 크게 제한된 조건에서도 얽힘을 확인하는 방법을 광자 실험으로 보였다.[^p2] 장치 내부를 전혀 믿지 않는 방식(장치 독립)으로 양자 상태를 증명하면서 더 큰 정보 처리 규약에 부품으로 넣을 수 있는 틀도 만들었다.[^p3]

둘째 갈래는 **양자 상태 구별과 측정**이다. 직교하지 않는 양자 상태는 어떤 측정으로도 완벽하게 구별할 수 없다. 여러 구별 전략을 아우르는 최대 신뢰 측정에서 양자 이론이 고전 모형보다 유리하다는 것을 보였다.[^p4]

셋째 갈래는 **양자 네트워크와 통신**이다. 두 송신자가 한 수신자에게 보내는 통신로에서 송신자들이 양자 상태나 비국소 상관(멀리 떨어진 쪽끼리 고전 이론으로 설명할 수 없는 상관)을 미리 나눠 쓰면 합 용량이 커진다는 것을 보였고,[^p5] 양자 자원이 고전보다 유리한 두 사람 사이의 1회 통신 규약을 새로 제안했다.[^p6]

넷째 갈래는 **양자 컴퓨터 오류 완화**다. 잡음 섞인 큐비트 준비·측정을 되풀이해 오류를 줄이는 정화 규약을 제시했고,[^p7] IBM 양자 컴퓨터에서 측정 판독 오류를 줄이는 방법을 시연했다.[^p8]

## 주요 연구 주제

### 1. 얽힘 검출과 증명

거울 얽힘 증인, 불완전한 측정 조건의 얽힘 확인, 결합 가능한 장치 독립 상태 증명.[^p1][^p2][^p3] 대표 논문 1–3.

### 2. 양자 상태 구별과 측정

최대 신뢰 측정과 맥락성 이점.[^p4] 대표 논문 4.

### 3. 양자 네트워크와 통신

다중 접속 채널의 양자·비국소 부호화, 무작위 배제 부호.[^p5][^p6] 대표 논문 5, 6.

### 4. 양자 컴퓨터 오류 완화

준비·측정 잡음 정화, 측정 판독 오류 완화.[^p7][^p8] 대표 논문 7, 8.

## 대표 논문

랩 논문 목록의 2021–2026년 논문 가운데 배준우 교수가 마지막 저자이거나 1저자인 것에서 연구 갈래를 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2026 | [Mirrored entanglement witnesses for multipartite and high-dimensional quantum systems](https://doi.org/10.1088/2058-9565/ae30a3) · Quantum Science and Technology | 얽힘 증인은 분리 가능한 상태에서 기댓값이 0 이상인 관측량으로, 이 부등식이 깨지면 얽힘을 찾아낸다. 최근 도입된 거울 얽힘 증인은 같은 증인에 자명하지 않은(non-trivial) 상한도 있어 아래·위 두 경계로 더 많은 얽힌 상태를 가려낸다. 이 거울 얽힘 증인을 여러 큐비트가 함께 얽힌 GHZ 상태, 큐비트를 그래프 모양으로 얽은 두 색 그래프 상태, 세 입자 속박 얽힘 상태와 고차원계로 넓혔고, 3차원 두 입자계에서 최적 증인끼리의 거울 쌍을 만들었다.[^p1] | 1저자 Jiheon Seong, 마지막 저자 배준우 |
| 2 | 2026 | [Practical and efficient verification of entanglement with incomplete measurement settings](https://doi.org/10.1103/sgbs-7228) · APS Open Science | 상태를 완전히 재구성할 수 없을 만큼 측정할 수 있는 관측량이 제한된 조건에서 얽힘을 확인하는 틀이다. 적은 수의 관측량 측정값으로 많은 얽힘 증인을 만들고, 반정부호 계획법(최적화 기법의 하나)으로 주어진 측정 조건에 가장 잘 맞는 증인을 찾는다. 광자 편광 큐비트 실험에서 전체 측정 자료의 일부만으로 얽힘을 증명했다.[^p2] | 1저자 Jiheon Seong, 마지막 저자 배준우 |
| 3 | 2025 | [Composable Framework for Device-Independent State Certification](https://doi.org/10.1103/1j5f-qjhx) · PRX Quantum | 장치 내부를 전혀 믿지 않는 장치 독립 방식으로 양자 상태를 증명하되, 다른 정보 처리 규약 안에 부품으로 넣을 수 있도록(결합 가능성) 만든 증명 방법이다. 광원이 서로 독립이지만 꼭 같지는 않은 상태를 유한 개 만든다는 가정을 두고, 싱글릿 상태(두 큐비트가 최대로 얽힌 상태의 하나)를 자기 시험하는 벨 시나리오에서 필요한 양을 계산하는 방법을 개발해 CHSH 부등식(양자 상관을 시험하는 벨 부등식의 한 형태)으로 싱글릿 상태를 증명했다.[^p3] | 1저자 Rutvij Bhavsar, 마지막 저자 배준우 |
| 4 | 2022 | [Contextual Advantages and Certification for Maximum-Confidence Discrimination](https://doi.org/10.1103/prxquantum.3.030337) · PRX Quantum | 직교하지 않는 양자 상태는 어떤 측정으로도 완벽히 구별할 수 없다. 최소 오류 구별과 모호하지 않은 구별을 아우르는 최대 신뢰 측정이 비맥락적 이론(고전 모형)보다 유리한 "맥락성 이점"을 가진다는 것을 보였고, 일부 장치만 믿는 반장치독립 상황에서 최대 신뢰 측정을 증명할 때도 이 이점이 남는다는 것을 보였다.[^p4] | 1저자 Kieran Flatt, 마지막 저자 배준우 |
| 5 | 2026 | [Nonlocal and quantum advantages in network coding for multiple access channels](https://doi.org/10.1103/b4q8-bzcq) · Physical Review A | 두 송신자가 한 수신자에게 피드백 없이 보내는 다중 접속 채널에서, 송신자들이 공유 무작위성, 양자 상태와 측정, 비국소 상관 같은 미리 나눈 자원으로 부호화를 협력하는 경우를 다뤘다. 양자·비국소 자원을 쓸 때의 용량 영역과 합 용량의 하한을 구했고, CHSH 게임과 마방진 게임(둘 다 비국소 게임의 하나)으로 만든 채널에서 양자·비국소 자원이 국소 자원보다 높은 합 용량을 낸다는 것을 보였다.[^p5] | 1저자 Jiyoung Yun, 마지막 저자 배준우 |
| 6 | 2026 | [Random exclusion codes: Quantum advantages of single-shot communication](https://doi.org/10.1103/196j-lmzl) · Physical Review Research | 송신자가 무작위 메시지를 더 짧은 열로 부호화해 보내고, 수신자가 원래 메시지에서 무작위로 고른 한 글자를 배제하려는 1회 송수신 규약 "무작위 배제 부호(REC)"를 도입했다. 양자 자원을 쓰면 고전 전략보다 성공 확률이 높고, 성공이 고르게 오류 없이 일어나야 한다는 조건을 더하면 필요한 양자 자원의 차원이 고전보다 작다. 맞히기 쪽 짝인 무작위 접근 부호에는 차원 이점이 없을 수 있다는 것도 보였다.[^p6] | 1저자 배준우, 마지막 저자 Ashutosh Rai |
| 7 | 2026 | [Protocol for purifying noisy preparation and measurements of qubits](https://doi.org/10.1103/z6pg-m3q6) · Physical Review Research | 큐비트 준비와 측정에 생기는 잡음은 양자 정보 처리 오류의 큰 부분을 차지한다. 잡음 섞인 준비·측정을 되풀이해 그 오류를 임의로 낮은 수준까지 줄이는 정화 규약을 제시했다. 준비와 측정의 오류율이 각각 약 0.05일 때 보조 큐비트 2개로 10⁻³, 4개로 10⁻⁶까지 낮출 수 있고, 초전도 큐비트에서도 실현할 수 있다.[^p7] | 1저자 Jaemin Kim, 마지막 저자 배준우 |
| 8 | 2021 | [A Hybrid Quantum-Classical Approach to Mitigating Measurement Errors in Quantum Algorithms](https://doi.org/10.1109/tc.2020.3009664) · IEEE Transactions on Computers | 중간 규모 잡음 양자(NISQ) 장치에서는 상태 준비부터 측정까지 모든 단계에 검증하기 어려운 잡음이 섞인다. 측정 잡음을 직접 알아내는 검출기 단층 촬영을 거치지 않고, 비교적 정밀한 단일 큐비트 연산과 고전 후처리만으로 측정 판독 오류를 줄이는 방법을 제시했다. IBMQ yorktown과 IBMQ essex에서 번스타인-바지라니 알고리즘과 양자 진폭 추정 알고리즘에 적용해 측정 결과 통계가 나아짐을 보였다.[^p8] | Hyeokjea Kwon(1저자)·배준우(마지막 저자) |

## 교수와 전문 분야

배준우 교수는 스페인 바르셀로나대(Universitat de Barcelona)에서 박사학위(2007)를 받았다. KAIST 전기및전자공학부 교수 소개는 직위를 부교수, 주요 연구분야를 Quantum Science & Engineering, 주요 연구를 양자정보이론, 디비전을 Wave·Communication으로 적고, 대표업적으로 구조적 물리 근사를 이용한 양자 정보 처리 설계 리뷰(Reports on Progress in Physics, 2017)와 양자 상태 구별 리뷰(Journal of Physics A, 2015)를 든다.[^ee] 연구실 누리집도 이 두 리뷰를 얽힘·양자 동역학과 양자 구별 가능성의 리뷰 논문으로 소개한다.[^research]

연구실 소식에 따르면 2024년 KAIST 교육혁신의 날에 Best Teacher Award(Hyung-Gyu Lim LINKGENESIS Best-Teacher Award Grand Prize)와 국무총리 표창(Prime Minister's Commendation)을 받았고, 2024년 11월 GINP 컨소시엄 선정 소식이 실렸다.[^news] Research 페이지는 지원 기관으로 한국연구재단(NRF), 정보통신기획평가원(IITP), 국가기술표준원, Business Finland, LG전자, 삼성 등을 적었다.[^research]

논문으로 보면 전문 분야는 네 갈래다.

- **얽힘 증인과 얽힘 검증 이론**.[^p1][^p2][^p3]
- **양자 상태 구별과 최대 신뢰 측정**.[^p4]
- **양자·비국소 자원을 쓰는 네트워크 정보 이론**.[^p5][^p6]
- **NISQ 양자 컴퓨터의 준비·측정 오류 정화와 완화**.[^p7][^p8]

## 응용 분야

Recent Results 페이지는 ETRI, KAIST Space Institute, POSTECH, KIST, 연세대 실험 연구진과 함께 한 얽힘 검증·양자 통신·두 큐비트 게이트 증명 실험과, IBMQ 양자 컴퓨터에서 측정 판독 오류를 줄이고 IonQ 양자 컴퓨터에서 3큐비트 양자 데이터베이스 검색을 구현한 작업을 소개한다.[^recent] 대표 논문으로 보면 적은 측정으로 얽힘을 확인하는 양자 하드웨어 검증, 장치를 믿지 않아도 되는 양자 보안 규약의 부품, 양자 자원으로 용량을 늘리는 통신 부호화, 잡음 많은 양자 컴퓨터의 오류 줄이기에 닿아 있다.[^p2][^p3][^p5][^p7] 졸업생과 이전 구성원은 강원대·인도네시아 반둥공대·인도 공과대(Dharwad) 교수, 핀란드 위바스퀼래대·덴마크 올보르대·영국 킹스칼리지런던·싱가포르 양자기술센터(CQT), IBM 등으로 진출했다.[^people]

## 구성원

2026년 10월 20일 랩 People 페이지 기준이다. 과정은 랩이 적은 칸 이름(Senior Researchers의 "Res. Assis. Prof."는 연구조교수, Postdoctoral Researchers, PhD, MSc)을 옮겼고, 괄호 속 "with 기관"은 랩 표기 그대로다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Ashutosh Rai | 연구조교수 | 5, 6 |
| Jiyoung Yun | 박사후연구원 | 5, 7 |
| Qiucheng Song | 박사후연구원 |  |
| Sung Won Yun | 박사후연구원 |  |
| Jayeong Kim | 박사후연구원 |  |
| Jiheon Seong | 박사후연구원 | 1, 2 |
| Seungchan Seo | 박사과정 | 2, 7 |
| Karthik Mohan | 박사과정 | 6 |
| Hyunseong Jang | 박사과정 (with KRISS) |  |
| Lemieux Wang | 박사과정 |  |
| Dongwon Lee | 박사과정 |  |
| Junguk Moon | 박사과정 |  |
| Jieun Kim | 석사과정 |  |
| Gyungjun Kim | 석사과정 |  |
| Jaehun Han | 석사과정 (with ETRI) |  |
| In-Hee Yun | 석사과정 (with ETRI) |  |
| Lynn Syazwanie | 석사과정 |  |
| YuChao Hsu | 석사과정 |  |
| Dogyeom Kim | 석사과정 (with KRISS) |  |
| Donghun Jeong | 석사과정 (with IBS) |  |

## 졸업생과 이전 구성원

랩 People 페이지 Alumni 칸의 이름, 학위·기간, 랩이 적은 다음 소속과 학위 논문이다. 이름 앞 호칭과 "->"로 이어 적은 진로는 랩 표기 그대로다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Dr. Daniel McNulty | PhD 2013, Univ. of York; Post-doc. 2015-2017 | Aberystwyth University, Wales, the UK |  |
| Dr. Sudipto Roy | PhD 2017, Harish-Chandra Research Institute; Post-doc. 2017-2018 | UAM-CSIC, Madrid, Spain ->... -> Professor, Indian Institute of Technology (Dharwad) |  |
| Dr. Tanmay Singal | PhD 2016, Institute of Mathematical Sciences, Chennai; Post-doc. 2016-2018 | Hanyang Univ., Korea |  |
| Ms. Seungjoo Baek | Applied Maths., Hanyang University; 2017-2019, MSc |  | Efficient detection of entanglement with mutually unbiased bases |
| Ms. Jiyoung Yun | Applied Maths. Hanyang University; 2017-2019, MSc |  | Quantum network information theory |
| Dr. Ashutosi Rai | PhD 2013, Bose Center for Basic Sciences, Kolkata; Senior Researcher 2019-2020 | staff researcher (permanent) @ Slovak Academy of Sciences |  |
| Dr. Spiros Kechrimparis | PhD 2016, Univ. of York; Post-doc. 2018-2020 | Centre for Quantum Technologies (CQT), Singapore |  |
| Mr. Sangheon Lee | MS 2021, KAIST | JLK (industry) -> TmaxSoft -> IBM |  |
| Mr. Hyeokjea Kwon | EE, KAIST; 2019-2021, MS |  | Mitigating Measurement Readout Errors in NISQ Device |
| Mr. Seungchan Seo | EE, KAIST; 2020-2022, MS |  | Verification of Correlated Error in Noisy Measurements using NISQ Devices |
| Dr. Yonghae Lee | Post-doc. 2021-2022 | Professor, Kangwon National University, Korea |  |
| Mr. Munsik Kim | EE, KAIST; 2020-2023, MS |  | Quantum search by measurement with a priori information |
| Dr. Hanwool Lee | PhD 2024, KAIST | University of Jyväskylä, Finland |  |
| Mr. Woonsang Choi | MS 2024, KAIST, MS | PhD course at Hanyang University | Optimality of pretty-good measurements |
| Dr. Soyoung Shim | PhD 2018 University of Hamburg and DESY; Post-doc 2023-2024 |  |  |
| Dr. Rutvij Bhavsar | PhD 2023 Univ. of York; Post-doc. 2024-2025 | King's College London, the UK |  |
| Mr. Hojun Lee | MS 2025, KAIST, MS |  | Probabilistic Manipulation of Quantum Feature Map for Classification |
| Mr. Chanmin Park | MS 2026, KAIST, MS | PhD course at KAIST | Verification of Randomized Benchmarking in NISQ Devices |
| Ms. Dyah Aryanti | PhD course | Professor, Institut Teknologi Bandung, Indonesia |  |
| Dr. Jaemin Kim | PhD 2026 | Aalborg university, Denmark | Harnessing Quantum Networks:Entanglement Distillation and Teleportation |
| Mr. An Ning | MS 2026, MS | PhD course in KAIST. | Enhancing Neural Networks with Variational Quantum Circuits for Convolutional and Attention-Based Models |
| Ms. Chaeyeong Jin | MS 2026, MS |  | Readout Error Mitigation and Superconducting Quantum Computer Operation |
| Dr. Seung-Hyun Nam | PhD 2024, KAIST; Post-doc 2024-2026 | University of Jyväskylä, Finland |  |
| Dr. Hyeokjea Kwon | PhD 2026, KAIST | Centre for Quantum Technologies, NUS, Singapore |  |
| Dr. Kieran Flatt | PhD 2019, University of Glasgow; Post-doc. 2020-2026 |  |  |

## 최근 논문 목록 (2021–2026)

랩 Publications 페이지의 2021년 이후 논문(50–84번)이다.[^papers]

**2026**

- Sung Won Yun, Thi Ha Kyaw, and Joonwoo Bae. "Measurement circuit ansatz: Naimark versus quantum neural-network measurements". *to appear Quantum Science and Technology (2026)*.
- Seung-Hyun Nam, Hyun-Young Park, Jiyoung Yun, Ashutosh Rai, Si-Hyeon Lee, and Joonwoo Bae. "Enhancing Sum Capacity via Quantum and No-Signaling Cooperation Between Transmitters". *IEEE Journal on Selected Areas in Communications, doi: 10.1109/JSAC.2026.3728780 (2026)*.
- Kap-Joong Kim, Kyongchun Lim, Byung-Seok Choi, Wook-Jae Lee, Jong-Bum You, Young-Ho Ko, Joong-Seon Choe, Minchul Kim, Jeongho Bang, Joonwoo Bae, Chun Ju Youn. "Optimizing path-polarization interconversion on a photonic circuit for secure quantum communication". *EPJ Quantum Technology (2026) doi: 10.1140/epjqt/s40507-026-00542-7*.
- Jaemin Kim, Karthik Mohan, Sung Won Yun, and Joonwoo Bae. "Carrier-Assisted Entanglement Purification". *IEEE Journal on Selected Areas in Communications, doi: 10.1109/JSAC.2026.3710152 (2026)*.
- Seung-Hyun Nam, Hyun-Young Park, Si-Hyeon Lee, and Joonwoo Bae. "Quantum Advantage in Locally Differentially Private Hypothesis Testing". *IEEE Journal on Selected Areas in Communications, doi: 10.1109/JSAC.2026.3709807 (2026)*.
- Jaemin Kim, Seungchan Seo, Jiyoung Yun, Benjamin Lienhard, Joonwoo Bae. "Protocol for purifying noisy preparation and measurements of qubits". *Phys. Rev. Research 8, 023347 (2026)*.
- Jaemin Kim, Anindita Bera, Dariusz Chruscinski, and Joonwoo Bae. "Detecting Entanglement by State Preparation and Local Measurements". *Quantum 10, 2128 (2026)*.
- Carles Roch i Carceller, Hanwool Lee, Kieran Flatt, Jonathan Bohr Brask, and Joonwoo Bae. "Sequential semi-device-independent quantum randomness certification". *Phys. Rev. Research 8, 023186 (2026)*.
- J. Seong et al. "Practical and efficient verification of entanglement with incomplete measurement settings". *APS Open Sci. 1, 000008 (2026) ; highlighted in the APS Physics Magazine*.
- Lemieux Wang, Hanwool Lee, Joonwoo Bae, and Kieran Flatt. "Sharing quantum indistinguishability with multiple parties". *Open Systems & Information Dynamics (OSID) Vol. 33, No. 01, 2650004 (2026)*.
- Jiyoung Yun, Seung-Hyun Nam, Hyun-Young Park, Ashutosh Rai, Si-Hyeon Lee, and Joonwoo Bae. "Nonlocal and quantum advantages in network coding for multiple access channels". *Phys. Rev. A 113, 042624 (2026)*.
- Kieran Flatt and Joonwoo Bae. "Contextual advantages across two-state discrimination strategies". *New Journal of Physics 28 044509 (2026)*.
- Joonwoo Bae, Kieran Flatt, Teiko Heinosaari, Oskari Kerppo, Karthik Mohan, Andrés Muñoz-Moller, and Ashutosh Rai. "Random exclusion codes: Quantum advantages of single-shot communication". *Phys. Rev. Research 8, 013171 (2026)*.
- Jiheon Seong, Anindita Bera, Beatrix Hiesmayr, Dariusz Chruscinski, and Joonwoo Bae. "Mirrored Entanglement Witnesses for Multipartite and High-Dimensional Quantum Systems". *Quantum Sci. Technol. 11 015037 (2026)*.

**2025**

- Rutvij Bhavsar, Lewis Wooltorton, and Joonwoo Bae. "Composable Framework for Device-Independent State Certification". *PRX Quantum 6, 040356 (2025)*.
- Hanwool Lee, Kieran Flatt, and Joonwoo Bae. "Sequential quantum maximum-confidence discrimination". *Phys. Rev. A 112, 052206 (2025)*.
- Dariusz Chruscinski, Anindita Bera, Joonwoo Bae, and Beatrix Hiesmayr. "A mirrored pair of optimal non-decomposable entanglement witnesses for two qudits does exist". *Scientific Reports 15 28205 (2025)*.
- Andreas J. C. Fuchs, Eric Brunner, Jiheon Seong, Hyeokjea Kwon, Seungchan Seo, Joonwoo Bae, Andreas Buchleitner and Edoardo G Carnio. "Machine-learning certification of multipartite entanglement for noisy quantum hardware". *New Journal of Physics (2025)*.
- H. Ko et. al. "Secure Quantum Communication with the Preservation of Optimal Measurements". *IEEE Journal on Selected Areas in Communications ( Volume: 43, Issue: 8, August 2025)*.
- Yonghae Lee, Joonwoo Bae, Hayata Yamasaki and Soojoon Lee. "Improved bounds on quantum uncommon information". *Journal of Physics A: Mathematical and Theoretical 58 055304 (2025)*.
- Jaemin Kim, Jiyoung Yun, and Joonwoo Bae. "Purification of noisy measurements and faithful distillation of entanglement". *Journal of Physics A: Mathematical and Theoretical 58 03LT01 (2025)*.

**2024**

- Andris Ambainis, Dmitry Kravchenko, Sk Sazim, Joonwoo Bae, and Ashutosh Rai. "Quantum advantages in (n,d)->1 random access codes". *New Journal of Physics 26 123023 (2024)*.

**2023**

- Jiheon Seong and Joonwoo Bae. "Detecting Entanglement-Generating Circuits in Cloud-Based Quantum Computing". *spj Intelligent Computing 2 0051 (2023)*.
- Hwang K, Seong J, Park K, Kim J, Pramanik T, Bae J and Shin H. "Entanglement witness measurement of time-bin two-qubit states using fiber based Franson interferometers". *Frontiers in Physics 11 1254044 (2023)*.
- Anindita Bera, Joonwoo Bae, Beatrix Hiesmayr, and Dariusz Chruscinski. "On the structure of mirrored operators obtained from optimal entanglement witnesses". *Scientific Reports 13 10733 (2023)*.

**2022**

- Joonwoo Bae, Anindita Bera, Dariusz Chruściński, Beatrix C Hiesmayr and Daniel McNulty. "How many mutually unbiased bases are needed to detect bound entangled states?". *Journal of Physics A: Mathematical and Theoretical 55 505303 (2022)*.
- Seungchan Seo, Jiheon Seong, and Joonwoo Bae. "Correlations in noisy measurements". *Open Systems & Information Dynamics (OSID) Vol. 29 No. 02 2250009 (2022)*.
- Yujun Choi, Tanmay Singal, Young-Wook Cho, Sang-Wook Han, Kyunghwan Oh, Sung Moon, Yong-Su Kim, and Joonwoo Bae. "Single-copy certification of two-qubit gates without entanglement". *Phys. Rev. Applied 18, 044046 (2022)*.
- Hanwool Lee, Kieran Flatt, Carles Roch i Carceller, Jonathan Bohr Brask, and Joonwoo Bae. "Maximum-confidence measurements for qubit states". *Physical Review A 106, 032422 (2022)*.
- Kieran Flatt, Hanwool Lee, Carles Roch i Carceller, Jonathan Bohr Brask, and Joonwoo Bae. "Contextual advantages and Certification for Maximum Confidence Discrimination". *PRX Quantum 3 030307 (2022)*.
- Carles Roch i Carceller, Kieran Flatt, Hanwool Lee, Joonwoo Bae, and Jonathan Bohr Brask. "Quantum vs. Noncontextual Semi-Device-Independent Randomness Certification". *Physical Review Letters 129 050501 (2022)*.
- Seungchan Seo and Joonwoo Bae. "Measurement crosstalk errors in cloud-based quantum computing". *IEEE Internet Computing Vol 26 Issue 1 page 26-33 (2022)*.

**2021**

- Hyeokjea Kwon and Joonwoo Bae. "Quantum amplitude amplification operators (QAAO)". *Physical Review A 104 062438 (2021) Editors' Suggestion*.
- B. Hiesmayr, D. McNulty, S Baek, S. Singha Roy, J. Bae, and D. Chruscinski. "Detecting entanglement ca be more effective with inequivalent mutually unbiased bases". *New. J. Phys. 23 093018 (2021)*.
- Hyeokjea Kwon and Joonwoo Bae. "A hybrid quantum-classical approach to mitigating measurement errors in quantum algorithms". *IEEE Transactions on Computers, Vol 70 (9) 1401 (2021)*.

## 수상

랩 소식 페이지 "Entangled world!"의 2022–2024년 구역에 적힌 수상·인정 소식이다. 날짜는 소식이 실린 연·월이다.[^news]

- 2024-05 · KAIST Education Innovation Day, Joonwoo Bae was awarded a Best Teacher Award, the Hyung-Gyu Lim LINKGENESIS Best-Teacher Award Grand Prize
- 2024-04 · Joonwoo Bae was awarded a prize (Prime Minister's Commendation)
- 2023-09 · Best TA Award (EE, KAIST) to Sung Won Yun!
- 2023-03 · 2022 IOP Outstanding Reviewer Awards
- 2022-09 · Joonwoo Bae achieved IOP Trusted Reviewer Status
- 2022-04 · Dongjin Lee, a recipient of the Eun-Jong-Kwan fellowship
- 2022-01 · Best Paper Award@KICS 2021 Fall Meeting

## 연락과 위치

- 연구실: KAIST 전기및전자공학부동(E3-2) 3203·3216호[^people]
- 교수실: KAIST 전기및전자공학부동(E3-2) W-3209, 교내 전화 7446[^ee]
- 교수 이메일: joonwoo.bae@kaist.ac.kr[^ee]

[^people]: People 페이지 <https://sites.google.com/view/qitkaist/people> (2026-10-20 열람)
[^research]: Research 페이지 <https://sites.google.com/view/qitkaist/research> (2026-10-20 열람)
[^recent]: Recent Results 페이지 <https://sites.google.com/view/qitkaist/research/recent-works> (2026-10-20 열람)
[^papers]: Publications 페이지 <https://sites.google.com/view/qitkaist/research/publications> (2026-10-20 열람)
[^news]: 소식 페이지 Entangled world! <https://sites.google.com/view/qitkaist/home/entangled-world> (2026-10-20 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개 <https://ee.kaist.ac.kr/professor/16105/> (2026-10-20 열람)
[^p1]: J. Seong 외, J. Bae, Quantum Science and Technology 11, 015037 (온라인 2026-01-12). <https://doi.org/10.1088/2058-9565/ae30a3> 초록 기준.
[^p2]: J. Seong 외, J. Bae, APS Open Science 1, 000008 (온라인 2026-04-29). <https://doi.org/10.1103/sgbs-7228> 초록 기준.
[^p3]: R. Bhavsar, L. Wooltorton, J. Bae, PRX Quantum 6, 040356 (온라인 2025-12-05). <https://doi.org/10.1103/1j5f-qjhx> 초록 기준.
[^p4]: K. Flatt 외, J. Bae, PRX Quantum 3, 030337 (온라인 2022-09-13). <https://doi.org/10.1103/prxquantum.3.030337> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. Yun 외, J. Bae, Physical Review A 113, 042624 (온라인 2026-04-24). <https://doi.org/10.1103/b4q8-bzcq> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: J. Bae 외, A. Rai, Physical Review Research 8, 013171 (온라인 2026-02-17). <https://doi.org/10.1103/196j-lmzl> 초록 기준(출판사 논문 페이지).
[^p7]: J. Kim 외, J. Bae, Physical Review Research 8, 023347 (온라인 2026-06-26). <https://doi.org/10.1103/z6pg-m3q6> 초록 기준.
[^p8]: H. Kwon, J. Bae, IEEE Transactions on Computers 70, 1401-1411 (2021). <https://doi.org/10.1109/tc.2020.3009664> 초록 기준(Semantic Scholar 등록 초록).

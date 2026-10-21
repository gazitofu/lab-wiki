# 부호 및 통신 연구실 (CoCoA, Coding and Communications lAb)

**KAIST 전기및전자공학부 · 하정석 교수**

- 분야: 오류 정정 부호(채널 코딩), 양자 오류 정정, 6G 무선 통신(셀프리 대규모 MIMO), 물리계층 보안, 광·위성 통신
- 대분야: 전기전자·반도체·광학, 물리·양자
- 태그: 오류 정정 부호[^research][^p4][^p5], 양자 오류 정정·완화[^research][^p1][^p2], 무선·이동통신[^p6], 네트워크 보안·프라이버시[^p7][^p8], 광통신[^p3][^p8], 양자 통신·네트워크[^research]
- 홈페이지: <https://cocoa.kaist.ac.kr/>
- 근거와 출처: [CoCoA 근거 페이지](cocoa-sources.md)

> 잡음 속에서도 정보가 틀리지 않게 지키는 "오류 정정 부호"를 연구한다. 낸드 플래시 메모리·광통신용 부호부터 양자컴퓨터의 오류를 바로잡는 양자 부호, 엿듣는 사람이 해독할 수 없게 하는 무선 보안 통신까지 다룬다.[^intro][^research][^p1][^p3]

## 무엇을 연구하나

디지털 통신이나 저장 장치에서는 잡음 때문에 0과 1이 뒤바뀌는 오류가 생긴다. 오류 정정 부호는 원래 정보에 여분의 비트를 덧붙여, 일부가 틀려도 원래 내용을 복구하게 하는 방법이다.[^research] 이 연구실은 2004년 하정석 교수가 세웠고,[^intro] LDPC 부호(검사 규칙이 드문드문한 대형 행렬로 정의되는 부호)·폴라 부호 같은 현대 부호의 이론을 연구하면서 낸드 플래시 메모리처럼 오류가 거의 없어야 하는 응용을 위해 기계학습 기반 부호도 개발한다.[^research]

첫 번째 갈래는 **양자 오류 정정**이다. 양자컴퓨터를 만드는 가장 큰 걸림돌은 양자 정보(큐비트)가 쉽게 흐트러지는 오류다.[^research] 연구실은 이웃한 큐비트끼리만 상호작용하면 되는 표면 부호(surface code)를 실제 구현을 고려해 연구한다.[^research] 표면 부호의 구조를 분석해 기존 방법보다 훨씬 적은 계산으로 같은 오류율을 내는 후처리 복호(받은 정보에서 오류를 찾아 원래 정보를 되살리는 과정) 방법을 내놓았고,[^p1] 합성곱 신경망으로 표면 부호를 복호하는 방법도 제안했다.[^p2]

두 번째 갈래는 **고속 통신·저장용 고전 부호**다. 광통신에 쓰는 계단식 부호(staircase code)를 개선해 목표 비트 오류율 10⁻¹⁵에서 부호화 이득을 0.13 dB 높였고,[^p3] 여러 BCH 부호(대수 구조를 이용해 정해진 개수의 오류를 고치는 고전 부호)를 엮은 구조에서 각 부호가 고칠 수 있는 오류 수를 하나 늘리는 복호법을 만들었다.[^p4] 폴라 부호의 복호 성능도 높였다.[^p5]

세 번째 갈래는 **6G 무선 통신과 물리계층 보안**이다. 여러 안테나가 흩어져 협력하는 셀프리(cell-free) 대규모 MIMO망에서 전송률을 더 정확히 계산하는 방법으로 사용자 간 공정성을 높였고,[^p6] 암호 키 없이 신호의 물리적 성질로 도청을 막는 물리계층 보안을 사물인터넷 기기와[^p7] 저궤도 위성–고고도 비행체 사이의 레이저 통신에 적용했다.[^p8] 연구실은 양자 암호(양자 키 분배)도 연구 분야로 든다.[^research]

## 주요 연구 주제

### 1. 양자 오류 정정 부호와 복호

표면 부호의 저복잡도 복호와 기계학습 복호.[^p1][^p2] 2025년부터 초전도 양자 프로세서의 실시간 오류 정정 과제(한국연구재단, 2025.10–2029.12)를 수행한다.[^projects] 대표 논문 1, 2.

### 2. 광통신·저장장치용 오류 정정 부호

계단식 부호, BCH 연결 부호, 폴라 부호.[^p3][^p4][^p5] 삼성전자·LG전자와의 산학 과제가 랩 과제 목록에 있다.[^projects] 대표 논문 3, 4, 5.

### 3. 셀프리 대규모 MIMO

차세대 이동통신의 분산 안테나망 설계.[^p6] 대표 논문 6.

### 4. 물리계층 보안 통신

협력 재밍, 위성 레이저 통신 보안, 은닉 통신.[^p7][^p8] 대표 논문 7, 8.

## 대표 논문

최근 5년 논문 중 교수가 마지막 저자(연구 책임)인 것에서 주제별로 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2025 | [Topological blocking decoder for surface codes](https://doi.org/10.1103/physreva.111.042424) · Physical Review A | 표면 부호의 복호기가 실패할 때를 바로잡는 저복잡도 후처리 방법. 경쟁 방법(OSD)과 같은 논리 오류율을 훨씬 적은 계산으로 냈고, 더 무거운 최소 가중치 완전 매칭 복호보다 성능이 좋았다.[^p1] | 1저자 Hyunwoo Jung, 마지막 저자 하정석 |
| 2 | 2024 | [Convolutional Neural Decoder for Surface Codes](https://doi.org/10.1109/tqe.2024.3419773) · IEEE Transactions on Quantum Engineering | 표면 부호의 격자 구조에 맞춘 합성곱 신경망 복호기. 신경망 크기를 격자에 맞게 고르는 방법으로 복잡도를 줄였다.[^p2] | 1저자 Hyunwoo Jung, 마지막 저자 하정석 |
| 3 | 2026 | [Block-Wise Staircase Codes](https://doi.org/10.1109/jlt.2026.3730890) · Journal of Lightwave Technology | 광통신용 계단식 부호에 블록 단위 연결을 넣어 더 강한 부호를 쓰게 했다. 비트 오류율 10⁻¹⁵에서 순 부호화 이득 9.54 dB(기존보다 0.13 dB↑), 새 복호법으로 9.60 dB를 냈다.[^p3] | 1저자 Huiyu Zhang, 마지막 저자 하정석 |
| 4 | 2025 | [One-Step Ahead Decoding for Symmetric Block-Wise Concatenated BCH Codes](https://doi.org/10.1109/tcomm.2025.3544977) · IEEE Transactions on Communications | 여러 BCH 부호를 엮은 구조의 성질을 이용해 각 부호가 고칠 수 있는 오류 수를 t에서 t+1로 늘리는 복호법. 오류율이 크게 낮아졌다.[^p4] | 1저자 Gabriel Daniel, 마지막 저자 하정석 |
| 5 | 2024 | [Improved Automorphism Ensemble Decoder for Polar Codes](https://doi.org/10.1109/lcomm.2024.3407143) · IEEE Communications Letters | 폴라 부호를 여러 경로로 동시에 복호하는 방식에서, 경로들의 결과를 다시 합쳐 새 복호 경로를 하나 더 만들어 오류율을 크게 낮췄다.[^p5] | 1저자 Seokju Han, 마지막 저자 하정석 |
| 6 | 2025 | [Joint Optimization of Power Control and LSFD Coefficients for Uplink Cell-Free Massive MIMO in Weak Channel Hardening Environments](https://doi.org/10.1109/tvt.2025.3543898) · IEEE Transactions on Vehicular Technology | 분산 안테나망(셀프리 대규모 MIMO)에서 기존 계산법이 일부 사용자의 전송률을 과소평가하는 문제를 고친 새 계산법으로 송신 전력을 최적화해 사용자 간 공정성을 크게 높였다.[^p6] | 1저자 Hyeonsik Yeom, 마지막 저자 하정석 |
| 7 | 2026 | [Fluid Antenna-Aided Cooperative Jamming in Uplink IoT Systems](https://doi.org/10.1109/jiot.2026.3711144) · IEEE Internet of Things Journal | 미리 공유한 키 없이도, 위치를 바꿀 수 있는 유체 안테나를 쓴 다른 기기들이 방해 신호를 보내 도청을 막는 사물인터넷 보안 방식. 보안 전송량을 최적화했다.[^p7] | 1저자 Hyunjun Joe, 마지막 저자 하정석 |
| 8 | 2026 | [Beam Divergence Angle Optimization for Secure FSO-Based Space–Air Communications](https://doi.org/10.1109/taes.2025.3635574) · IEEE Transactions on Aerospace and Electronic Systems | 저궤도 위성에서 고고도 비행체로 보내는 레이저 통신에서 빔 퍼짐 각도가 신뢰성과 보안 사이의 맞교환을 만든다는 것을 보이고, 이를 최적화하는 알고리즘을 냈다.[^p8] | 1저자 Hung D. Nguyen, 마지막 저자 하정석 |

## 교수와 전문 분야

하정석 교수는 미국 조지아공대에서 전기·컴퓨터공학 박사(2003)를 받았고, 2004년 KAIST에서 이 연구실을 세웠다.[^prof][^intro] 교수 페이지는 연구 관심을 전송률 적응형 채널 부호, 저장장치·통신용 채널 부호, LDPC·터보 부호 같은 그래프 기반 부호, 정보이론적 보안(도청 채널)으로 적는다.[^prof] IEEE Data Storage 최우수 논문상(2018), 한국연구재단 기초연구 우수성과 50선(2014), SK하이닉스 산학과제 우수 발명 포상(2015)을 받았다.[^prof]

논문과 과제로 보면 전문 분야는 세 갈래다.

- **채널 부호 이론과 복호 알고리즘**: LDPC·폴라·BCH·계단식 부호.[^p3][^p4][^p5][^prof]
- **양자 오류 정정**: 표면 부호와 양자 LDPC 부호의 복호. 양자 LDPC 부호 복호 장치는 미국 특허로 등록됐다(랩 표기).[^p1][^p2][^patents]
- **물리계층 보안과 무선망 설계**.[^p6][^p7][^p8]

## 응용 분야

연구실과 과제 목록으로 보면 낸드 플래시 등 저장장치 오류 정정, 6G·광통신의 고속 오류 정정, 초전도 양자컴퓨터의 실시간 오류 정정, 소형 위성 통신 보안에 닿아 있다.[^research][^projects] 졸업생은 삼성전자·SK하이닉스·LG·현대자동차·한화탈레스와 ETRI·국방과학연구소로 진출했고, 부경대·한국해양대·한남대 교수로 임용된 졸업생이 있다.[^alumni][^intro]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 정현우 (Jung, Hyunwoo) | 박사후연구원 | Quantum Error Correction | destinylz@kaist.ac.kr | 1, 2 |
| 김명인 (Kim, Myungin) | 박사과정 | Coding Theory | kmi9212@kaist.ac.kr |  |
| 김재민 (Kim, Jaemin) | 박사과정 | Quantum Error Correction | jmkinn@kaist.ac.kr |  |
| 박태희 (Park, Taehee) | 박사과정 | Coding Theory | pth0314@kaist.ac.kr |  |
| Nguyen Duy Hung | 박사과정 | Wireless Communication | hungnd@kaist.ac.kr | 7, 8 |
| 조현준 (Joe, Hyunjun) | 박사과정 | Wireless Communication | namjoe@kaist.ac.kr | 7 |
| Zhang Huiyu | 박사과정 | Channel Coding Quantum Error Correction | zhanghuiyu@kaist.ac.kr | 3, 4 |
| 우준서 (Woo, Junseo) | 박사과정 | Channel Coding | woojoshua78@kaist.ac.kr |  |
| 허경표 (Heo, Gyeongpyo) | 박사과정 | Wireless Communication | boondo990@kaist.ac.kr |  |
| Felita Ariella | 박사과정 | Quantum Error Correction | felariel@kaist.ac.kr |  |
| Jiahui Gao | 박사과정 | Coding Theory | jiahuig19@kaist.ac.kr |  |
| 하유진 (Ha, Eugene) | 석사과정 | Coding Theory | eugene.ha@kaist.ac.kr |  |
| 이인규 (Lee, Ingyu) | 석사과정 | Quantum Error Correction | ingyu123@kaist.ac.kr |  |
| 서민성 (Seo, Minsung) | 석사과정 | Quantum Error Correction | suhms0230@kaist.ac.kr |  |
| 조웅기 (Cho, Woongki) | 석사과정 | Quantum Error Correction | littlewk@kaist.ac.kr |  |

## 졸업생 진로

랩 졸업생 페이지의 목록이다. 진로는 랩이 적은 소속을 옮겼다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 권진희 (Kwon, Jinhee) | M.S. (2007) | Samsung Electronics Co. |
| 신동혁 (Shin, Donghyuk) | M.S. (2007) | Samsung Electronics Co. |
| 오상봉 (Oh, Sangbong) | M.S. (2008) | Korean Air Lines. Co. |
| 김민기 (Kim, Minki) | M.S. (2010) | Hyundai Eng & Const |
| 정천성 (Jung, Cheongsung) | M.S. (2010) | LG CTO |
| 현명해 (Hyun, Myounghae) | M.S. (2010) | Samsung Thales. Co. |
| 카이스 (Azzouzi, Kais) | M.S. (2010) |  |
| 황대성 (Hwang, Daesung) | M.S. (2010) | LG CTO |
| 강동협 (Kang, Donghyub) | M.S. (2010) | Hyundai Motor |
| 권수림 (Kwon, Surim) | M.S. (2011) | Hyundai Motor |
| 김웅환 (Kim, Unghwan) | M.S. (2011) | Samsung Semiconductor |
| 유승재(Yoo, Seungjae) | M.S. (2012) | Hyundai Motor |
| 조성근(Cho, Sunggun) | M.S. (2012) | SK Hynix |
| 이상아 (Lee, Sangha) | M.S. (2013) | SK Hynix |
| 유광호 (Yoo, Kwangho) | M.S. (2014) | Samsung Semiconductor |
| 이재윤 (Lee, Jaeyoon) | M.S. (2014) | SK Hynix |
| 백진호 (Baek, Jinho) | M.S. (2015) | SK Hynix |
| 홍영표 (Hong, Youngpyo) | M.S. (2015) | Korean Air Lines. Co. |
| 오지은 (Oh, Jieun) | Ph.D. (2015) | Research Fellow, Gordon Center for Medical Imaging, Massachusetts General Hospital |
| 임상훈 (Im, Sanghun) | Ph.D. (2016) | Hanwha Thales |
| 서상아 (Seo, Sangah) | M.S. (2016) |  |
| 김대성 (Kim, Daesung) | Ph.D. (2017) | SK Hynix |
| 윤길수 (Yun, Gilsu) | M.S. (2017) | SK Hynix |
| 고명준 (Ko, Myoungjun) | M.S. (2018) | ADD |
| 윤상석 (Yun, Sangseok) | Ph.D. (2018) | Pukyong National University Professor |
| 정수황 (Jeong, Suhwang) | Ph.D. (2020) | Samsung |
| 강정환 (Kang, Jeonghwan) | M.S. (2021) | Samsung |
| Nguyen Thi Van | M.S. (2022) | Viettel Telecom |
| Dinh Trung Duc | M.S. (2022) | Samsung Electronics Vietnam |
| 이진영 (Lee, Jinyoung) | Ph.D. (2023) | Samsung |
| Inayat Ali | Ph.D. (2019) | LG |
| 박정욱 (Park, Junguk) | Ph.D. (2023) | Samsung |
| 한석주 (Han, Seokju) | Ph.D. (2024) | Samsung |
| Gabriel | M.S. (2024) |  |
| 이승현 (Lee, Seunghyun) | M.S. (2024) |  |
| 손지현 (Son, Jihyun) | M.S. (2025) |  |
| 염현식 (Yeom, Hyeonsik ) | Ph.D. (2025) | ETRI |
| 오경목 (Oh, Kyungmok) | Ph.D. (2026) |  |
| 김형석 (Kim, Hyeongseok) | M.S. (2026) |  |

## 최근 논문 목록 (2021–2026)

교수 페이지의 국제 학술지 목록에서 2021–2026년 항목 54편이다.[^papers] 대표 논문은 위 표에서 쉬운 설명을 붙였다.

**2026**

- J. Kim, H. Jung, and J. Ha. "Improved BP Decoding with Multiple Error-Path Detection for Topological Quantum Codes". *IEEE Transactions on Quantum Engineering, ACCEPTED, 2026*.
- H. Yeom and J. Ha. "System-level Performance Analysis of Uplink Cell-free Massive MIMO With L-MMSE Combining Using Stochastic Geometry". *IEEE Transactions on Vehicular Technology, ACCEPTED, 2026*.
- H. Yeom and J. Ha. "Performance Analysis of Uplink Cell-free Massive MIMO with Local MMSE Combining and Variable Resolution ADCs". *IEEE Transactions on Vehicular Technology, ACCEPTED, 2026*.
- H. Zhang and J. Ha. "Block-wise Staircase Codes". *Journal of Lightwave Technology, vol. 44, no. 20, pp. 8937-8951, Oct. 2026*.
- H. Joe, H. Yeom, H. Nguyen, and J. Ha. "Fluid Antenna-Aided Cooperative Jamming in Uplink IoT Systems". *IEEE Internet of Things Journal, vol. 13, no. 17, pp. 41070-41086, Sept. 2026*.
- J. Seo, J. Ha, and J. Kang. "Rate-Adaptive Vector Quantization for Deep Joint Source-Channel Coding". *IEEE Transactions on Cognitive Communications and Networking, vol. 12, pp. 11087-11101, Aug. 2026*.
- H. Nguyen and J. Ha. "Comments on "On Covert Communication Performance With Outdated CSI in Wireless Greedy Relay Systems". *IEEE Transactions on Information Forensics and Security, vol. 21, pp. 5090-5093, May 2026*.
- H. Joe, G. Heo, H. Nguyen, and J. Ha. "Delay-Doppler Domain Artificial Fast Fading for Secure OTFS Communications". *IEEE ICTC 2026, Jeju, Oct. 2026*.
- H. Kim, E. Ha, and J. Ha. "Design of QC-LDPC Codes at Finite Lengths". *IEEE VTC 2026 Fall, Boston, USA, Sep. 2026*.
- H. Joe, G. Heo, and J. Ha. "Secrecy Outage Probability of Fluid Antenna-Aided Cooperative Jamming Network". *IEEE ICC 2026, Glasgow, UK, May 2026*.
- H. Nguyen and J. Ha. "UAV-Assisted Downlink Satellite Covert Communication". *IEEE ICC 2026, Glasgow, UK, May 2026*.

**2025**

- H. Nguyen, H. Yeom, and J. Ha. "Beam Divergence Angle Optimization for Secure FSO-based Space-Air Communications". *IEEE Transactions on Aerospace and Electronic Systems, vol. 62, pp. 2218-2235, Nov. 2025*.
- G. Daniel, H. Zhang, I. Ali and J. Ha. "One-Step Ahead Decoding for Symmetric Block-Wise Concatenated BCH Codes". *IEEE Transactions on Communications, vol. 73, no. 9, pp. 6993-7006, Sept. 2025*.
- H. Jung, and J. Ha. "Topological blocking decoder for surface codes". *Physical Review A, vol. 111, no.4, pp. 042424, Apr. 2025*.
- H. Yeom, J. Park, J. Choi and J. Ha. "Joint Optimization of Power Control and LSFD Coefficients for Uplink Cell-Free Massive MIMO in Weak Channel Hardening Environments". *IEEE Transactions on Vehicular Technology, vol. 74, no. 7, pp. 10565-10581, July 2025*.
- S. Lee, H. Joe, and J. Ha. "PAoI Minimization in LEO Satellite Communication Based on Packet Management Schemes". *APISAT 2025, Seoul, Korea, Oct. 2025*.
- 조현준, Nguyen D. H., 곽정호, 하정석. "(초)소형 국방 위성의 통신 보안 및 신뢰성 향상을 위한 최적화". *2025 한국항공우주학회 춘계학술대회, 대한민국, 제주도, 2025년 4월*.

**2024**

- H. Jung, I. Ali and J. Ha. "Convolutional Neural Decoder for Surface Codes". *IEEE Transactions on Quantum Engineering, vol. 5, pp. 1-13, Jun. 2024*.
- S. Han, B. Kim, J. Chung and J. Ha. "Improved Automorphism Ensemble Decoder for Polar Codes". *IEEE Communications Letters, vol. 28, no. 8, pp. 1750-1754, Aug. 2024*.
- J. Park, H. Yeom, S. Yun and J. Ha. "Downlink Cell-Free Massive MIMO With Pilot Contamination". *IEEE Transactions on Vehicular Technology, vol. 73, no. 1, pp. 1412-1417, Jan. 2024*.
- J. Park, S. Yun and J. Ha. "Secure Power Control for Downlink Cell-Free Massive MIMO With Passive Eavesdroppers". *IEEE Transactions on Vehicular Technology, vol. 73, no. 6, pp. 9038-9043, June 2024*.
- H. Yeom, J. Lee, S. Lee and J. Ha. "Covert Communication with Multi-users Cooperation at Unequal Distances". *IEEE ICC 2024, Denver, USA, June. 2024*.
- 조현준, 하정석. "Orthogonal Time Frequency Space 기반 저궤도 위성통신 시스템에서의 Artificial Fast Fading 보안성능 평가". *JCCI 2024, 대한민국, 부산, 2024년 4월*.
- 김정수, 전수현, 이승현, 조현준, 염현식, 곽정호, 하정석. "(초)소형 국방 위성 통신 보안 및 신뢰성 향상 기법". *2024 한국항공우주학회 춘계학술대회, 대한민국, 제주도, 2024년 4월*.

**2023**

- J. Lee, H. Yeom, S. Lee and J. Ha. "Channel Correlation in Multi-User Covert Communication: Friend or Foe?". *IEEE Transactions on Information Forensics and Security, vol. 19, pp. 1469-1482, Nov. 2023*.
- I. Ali, and J. Ha. "Partial Spatial Coupling of LDPC Codes: Reducing the Gap to Capacity by Improving the Rate". *IEEE Transactions on Communications, vol. 71, no. 12, pp. 6898-6913, Dec. 2023*.
- J. Lee, D. Dinh, H. Yeom, S. Lee and J. Ha. "Multi-User Cooperation for Covert Communication Under Quasi-Static Fading". *IEEE Transactions on Information Forensics and Security, vol. 18, pp. 4625-4639, July 2023*.
- J. Kim, H. Jung and J. Ha. "Low-Complexity Decoding Algorithm Utilizing Degeneracy for Quantum LDPC Codes". *IEEE MILCOM 2023, Boston, USA, Oct. 2023*.
- 김재민, 하정석. "잉여 검사 행렬 기반의 양자 저밀도 패리티 검사 부호를 위한 신뢰 전파 복호". *2023 하계종합학술대회, 대한민국, 제주도, 2023년 6월*.
- 박태희, 한석주, 하정석. "극 부호를 위한 저복잡도 CRC 기반 치환 연속 소거 복호 알고리즘". *2023 하계종합학술대회, 대한민국, 제주도, 2023년 6월*.
- 김재민, 정현우, 하정석. "양자 저밀도 패리티 검사 부호를 위한 계층적 신뢰 전파 복호 알고리즘". *2023 동계종합학술대회, 대한민국, 용평, 2023년 2월*.

**2022**

- S. Han, J. Oh, K. Oh and J. Ha. "Deep-Learning for Breaking the Trapping Sets in Low-Density Parity-Check Codes". *IEEE Transactions on Communications, vol. 70, no. 5, pp. 2909-2923, May 2022*.
- J. Lee, S. Yun, I. Kim and J. Ha. "Deep Neural Network-based Precoder for Fairness Aware Secure NOMA Scheme". *IEEE Transactions on Vehicular Technology, vol. 71, no. 5, pp. 5615-5620, May 2022*.
- S. Han, B. Kim and J. Ha. "Rate-Compatible Punctured Polar Codes". *IEEE Communications Letters, vol. 26, no. 4, pp. 753-757, April 2022*.
- S. Jeong, H. Jung and J. Ha. "Rate-Compatible MET-LDPC Code Ensembles for CV-QKD Systems". *npj Quantum Information 8, 6 (2022)*.
- S. Yun, J. Kang, J. Ha, S. Lee, D. Ryu, and I. Kim. "Deep Learning-Based Ground Vibration Monitoring: Reinforcement Learning and RNN-CNN Approach". *IEEE Geoscience and Remote Sensing Letters, vol. 19, pp. 1-5, Mar. 2022*.
- H. Yeom and J. Ha. "Improper Gaussian Signalings for Secure Non-Orthogonal Multiple Access". *IEEE ICTC 2022, Jeju, Oct. 2022*.
- M. Kim and J. Ha. "Sneak Path Aware Bit-Flipping Algorithm for ReRAM Crossbar Array". *IEEE ICTC 2022, Jeju, Oct. 2022*.
- 이승현, 장갑석, 염현식, 하정석. "심볼 동기 오류를 고려한 CRLB 기반 ToA 추정성능 분석". *2022 CEIC, 대한민국, 대전, 2022년 12월*.
- 정현우, 하정석. "적은 수의 자기 동형 사상을 가지는 선형 부호의 무작위 여분 복호 알고리즘". *2022 하계종합학술대회, 대한민국, 제주도, 2022년 6월*.
- 한석주, 하정석. "극 부호를 위한 적응 치환 기반 신회 전파 복호 알고리즘". *2022 하계종합학술대회, 대한민국, 제주도, 2022년 6월*.
- 염현식, 하정석. "Data-Aided Sensing을 사용한 Cell-free Massive MIMO Fronthaul Overhead 감소 기법". *2022 동계종합학술대회, 대한민국, 용평, 2022년 2월*.
- 한석주, 하정석. "저밀도 패리티 검사 부호를 위한 효율적인 다단계 경판정 복호 알고리즘". *2022 동계종합학술대회, 대한민국, 용평, 2022년 2월*.
- 박정욱, 하정석. "Large Intelligent Surface를 활용한 은닉 통신 시스템". *2022 동계종합학술대회, 대한민국, 용평, 2022년 2월*.
- 김명인, 하정석. "멀티레벨 셀 스핀 전달 토크 형 자기 저항 메모리를 위한 저밀도 패리티 검사 부호의 차등 가중 경사 하강 비트 반전 알고리즘". *2022 동계종합학술대회, 대한민국, 용평, 2022년 2월*.

**2021**

- S. Jeong, and J. Ha. "MET-LDPC Code Ensembles of Low Code Rates with Exponentially Few Small Weight Codewords". *IEEE Transactions on Communications, vol. 69, no. 6, pp. 3517-3527, Jun. 2021*.
- S. Han and J. Ha. "Polar Codes for Fast Converging Belief-Propagation Decoding". *IEEE ICTC 2021, Jeju, Oct. 2021*.
- H. Jung, J. Kang and J. Ha. "Quantum-Assisted Decoding for Non-Binary Low-Density Parity-Check Codes". *IEEE ICTC 2021, Jeju, Oct. 2021*.
- 정현우, 하정석. "위상학적 양자 오류정정부호의 부호율 변화에 관한 연구". *2021 동계종합학술대회, 대한민국, 용평, 2021년 2월*.
- 김명인, 하정석. "보안키 추출을 위한 반복 부호 이점 증류 프로토콜의 증류 효율 향상에 관한 연구". *2021 동계종합학술대회, 대한민국, 용평, 2021년 2월*.
- 한석주, 하정석. "저복잡도 오토인코더 기반 통신 시스템". *2021 동계종합학술대회, 대한민국, 용평, 2021년 2월*.
- 박정욱, 하정석. "Large Intelligent Surface 기반 시스템에서 채널 추정을 고려한 Throughput 분석". *2021 동계종합학술대회, 대한민국, 용평, 2021년 2월*.
- 염현식, 하정석. "Improper Gaussian 신호를 사용한 보안 NOMA 성능 분석". *2021 동계종합학술대회, 대한민국, 용평, 2021년 2월*.
- 이진영, 윤상석, 하정석. "비직교 다중 접속 시스템의 보안 공평성을 고려한 딥러닝 기반 보안 빔형성 설계". *2021 동계종합학술대회, 대한민국, 용평, 2021년 2월*.

## 특허

교수 페이지에 게시된 특허 출원·등록 목록이다.[^patents]

- Method and Apparatus for Determining Recovery Operator Using Topological Structure of Rotated Surface Code (출원번호 18/525,914; 출원일 2023-12-01)
- Method and Apparatus for Managing Resource of Cell-Free Massive Multiple Input Multiple Output Network System, and Storage Medium Storing Instructions to Perform Method for Managing Resource of Cell-Free Massive Multiple Input Multiple Output Network System (출원번호 18/522,606; 출원일 2023-11-29)
- Two-Stage Deep Learning based Secure Precoders for Information and AN Signals in Non-Orthogonal Multiple Access (출원번호 17/317,633; 출원일 2021-05-11)
- Apparatus and Method for Decoding Quantum Low-Density Parity-Check Code (출원번호 18/407,498; 출원일 2024-01-09; 등록번호 US 12,346,774 B2; 등록일 2025-07-01)
- Apparatus and Method for Secure Communication Using Artificial Noise Scheme (출원번호 16/162,014; 출원일 2018-10-16; 등록번호 US 10,999,000; 등록일 2021-05-04)
- 양자 오류 정정 부호의 복호화를 위해 계층적 신뢰 전파 기반의 딥러닝 모델을 학습시키는 방법 및 장치 (출원번호 10-2024-1075288; 출원일 2024-11-29)
- CI-BCH 부호의 비-복호 오류를 정정하기 위한 비트 반전 방법 및 그 장치 (출원번호 10-2023-0134998; 출원일 2023-10-11)
- 회전한는 표면 부호의 위상학적 구조를 이용하여 복구 연산자를 결정하는 방법 및 장치 (출원번호 10-2023-0090819; 출원일 2023-07-13)
- 양자 저밀도 패리티 검사 부호 복호화 장치 및 방법 (출원번호 10-2023-0089867; 출원일 2023-07-11)
- 보안 전력 할당 장치 및 방법 (출원번호 10-2023-0086781; 출원일 2023-07-04)
- 셀-프리 대량 다중 입출력 네트워크 시스템의 자원 관리 장치 및 자원 관리 방법 (출원번호 10-2022-0165011; 출원일 2022-11-30)
- 표면 부호의 기계학습 기반 복호 방법 및 그 장치 (출원번호 10-2021-0028056; 출원일 2021-03-03)
- 채널 복호기의 동작과 결합한 플래시 메모리 읽기 방법 및 그 장치 (출원번호 10-2020-0076226; 출원일 2020-06-23; 등록번호 10-2247164-0000; 등록일 2021-04-27)
- 협력 재밍을 사용한 상향 링크 비직교 다중 접속 네트워크에서 보안 전송률 형평성 향상을 위한 복호화 순서 선택 방법 및 그 시스템 (출원번호 10-2019-0154521; 출원일 2019-11-27; 등록번호 10-2235149-0000; 등록일 2021-03-29)
- 개선된 터보 곱 부호 복호 알고리즘 (출원번호 10-2017-0060021; 출원일 2017-05-15; 등록번호 10-2226174-0000; 등록일 2021-03-04)

## 연구 과제

랩 과제 페이지에 게시된 목록이다. 지원 기관과 기간은 랩 표기를 옮겼다.[^projects]

- Development of Qubit Measurement, Reset, and Feedback Techniques, and Error-Correction Algorithms for Real-Time Error Correction in Superconducting Quantum Processors (지원 NRF; 기간 2025.10~2029.12)
- Research on Error-Correcting Codes for Improving the Performance and Reliability of Interface IP for Next-Generation (지원 Samsung Electronics; 기간 2025.10~2030.09)
- Study on Bias-Tailored Quantum Error-Correction Techniques (지원 NRF; 기간 2025.09~2028.08)
- Towards Secure and Reliable Quantum Networked Systems (지원 KAIST; 기간 2025.07~2027.12)
- Communication System에서 Reliability 확보를 위한 AI 기반 오류 정정 연구 (지원 Samsung Electronics; 기간 2023.09~2025.09)
- On Improving Security and Reliability for (Ultra) Small Satellite Communication (지원 KRIT; 기간 2022.12~2028.12)
- Optical Access and Indoor Networks for 6G Wireless Communication Systems (지원 IITP; 기간 2022.04~2025.12)
- Space Communications with Multi-Mission Low-Earth-Orbit Satellite Constellations (지원 NRF; 기간 2022.04~2026.12)
- Channel Coding Design Supporting Tbps High Speed Decoding for 6G Communications (지원 LG Electronics; 기간 2020.07~2025.12)
- 절대동기 타이밍 오류 요인 저감 기술 고도화 연구 (지원 ETRI; 기간 2022.04~2022.12)
- Development of Tbps Optical Communication Infrastructure Technology (Development of Low-complexity Error Correction Algorithm for 6G Optical Access) (지원 ETRI; 기간 2021.05~2023.11)
- Signal Processing and Error Correction Techniques for Data-centric Computing (지원 NRF; 기간 2021.03~2024.02)
- Fundamental Research on Quantum Computing for Artificial Intelligence (지원 ITRC; 기간 2018.06~2023.12)
- Backhaul Overhead Minimization Scheme for 6G Cell-Free Massive MIMO Systems (지원 IITP; 기간 2021.05~2022.04)
- A Study on Physical Layer Security for Heterogeneous Wireless Network (지원 IITP; 기간 2018.07~2022.12)
- Machine Learning based Optimization for Massive MIMO Systems (지원 IITP; 기간 2019.07~2021.06)
- Development of terrestrial / satellite quantum communication technology for flawless security (지원 IITP; 기간 2015.06~2020.12)
- Machine Learning-based Adaptive Signal Processing and Error Correction Codes for the Next-Generation Data Storage (지원 NRF; 기간 2018.03~2021.02)
- Sk Hynix-KAIST Storage Media Solutions Center (지원 Sk Hynix; 기간 2013.10~2019.10)
- Near Field security certification using NFC smart device (지원 MOTIE; 기간 2018.06~2019.05)
- Development of Quantum Communication Technologies for Ultimate Security (지원 ITRC; 기간 2015.06~2018.12)
- Low Complexity Physical Layer Security for Next Generation Distributed Networks (지원 NRF; 기간 2015.05~2018.04)
- Ultra wideband based 100Gbps Chip-to-chip wireless communication systems (지원 KCC; 기간 2013.05~2018.04)
- 완전분산형 D2D 환경에서 보안키 공유를 위한 물리계층 보안기술 연구 (지원 ETRI; 기간 2015.06~2016.01)
- Toward Perfectly Secure System Based on No-cloning Property of Wireless Channel (지원 RED&B; 기간 2015.06~2015.11)
- Study on cross-layer optimization techniques for improving security of next generation wireless networks (지원 NRF; 기간 2012.05~2015.04)
- Development of core technologies for next generation hyper MLC NAND based SSD (지원 MOTIE; 기간 2010.04~2015.03)
- 완전분산형 D2D에 최적화된 물리계층 보안 기술 연구 (지원 ETRI; 기간 2014.06~2015.01)
- Research of turbo product code for NAND flash memories (지원 Hynix; 기간 2012.09~2014.08)
- Development of fundamental technology for mobility supported VCN/BCMA (지원 Samsung; 기간 2012.09~2014.07)
- Implementation of noisy network coding and interference neutralization based on USRP (지원 SAIT; 기간 2013.04~2014.03)
- Collaborative coding/decoding for the tape channel (지원 INSIC; 기간 2012.02~2014.02)
- Large-scale Wireless-PON Convergence Technology Utilizing Network Coding (지원 KEIT; 기간 2009.05.01~2014.02.28)
- Research of secure channel coding (지원 SAIT; 기간 2012.08~2012.12)
- Study on Cross-layer Optimization Techniques for Improving Security of Next Generation Wireless Networks (지원 NRF; 기간 2009.05.01~2012.04.30)
- Development of Advanced Video Encoder with Low Complexity for Mobile Video Service (지원 KEIT; 기간 2009.03.01~2010.02.28)
- Research of Nested Lattice Transmission Technology for Mobile Communication Systems (지원 ETRI; 기간 2009.05.01~2009.12.31)
- Radio Education and Research Center Project (지원 IITA; 기간 2007.01.01~2009.12.31)
- Vehicle Multi-hop Communication Technology Development (지원 IITA; 기간 2007.03.01~2009.02.28)
- Research of LDPC Encoder and Decoder for Distributed Source Coding (지원 ETRI; 기간 2008.07.01~2009.01.28)
- Research of Technologies for IMT-Advanced (지원 ETRI; 기간 2008.07.01~2008.11.30)
- Research of Acquisitions of Sight Information Using Mobile Communication Systems (지원 ETRI; 기간 2008.03.01~2008.10.31)
- Research of the Elimination of Oscillations on the Decoding of LDPC Codes and the Retransmission Scheme for Hybird ARQ (지원 KRF; 기간 2007.08.01~2008.07.01)
- Research of Iterative Detection and Decoding Algorithm for MIMO-OFDM (지원 ETRI; 기간 2007.05.11~2007.11.30)
- Samsung-ICU Joint Research Center - Cognitive Radio Structure Research (지원 Samsung; 기간 2005.07.01~2007.06.30)
- Research of Channel Decoder for Wireless Communications (지원 ETRI; 기간 2006.04.01~2007.02.28)
- Wireless Mesh Networks Technology (지원 RERC; 기간 2006.01.01~2006.12.31)
- Research for 3G LTE H-ARQ and Channel Codec (지원 ETRI; 기간 2006.04.01~2006.11.30)
- Broadband Wireless Access Techniques (지원 RERC; 기간 2005.01.01~2005.12.31)
- Decoder Optimization for WiBro Upink Channel (지원 ETRI; 기간 2005.05.01~2005.11.30)
- Rate-Compatible Punctured Low-Density Parity-Check Codes at Finite Lengths (지원 ICU; 기간 2004.11.15~2005.11.15)

## 수상과 소식

- 졸업생 교수 임용(랩 표기): 박정욱 박사 부경대학교(2026), 이진영 박사 한국해양대학교(2025), 오지은 박사 한남대학교(2025), 윤상석 박사 부경대학교(2021).[^intro]
- 석사과정 이승현이 제24회 전자정보통신학술대회(CEIC) 우수논문상을 받았다(2022).[^intro]
- 교수 수상(랩 표기): IEEE ICT Convergence 최우수 논문상(2015·2019), IEEE Data Storage 최우수 논문상(2018), IEEE Transactions on Information Forensics and Security Best Readings(2011·2013) 등.[^prof]

## 연락과 위치

- 이메일: jsha@ee.kaist.ac.kr[^prof] (랩 첫 화면 표기 jsha@kaist.edu[^intro])
- 전화: 042-350-7424[^prof]
- 교수실: KAIST N1동 612호[^prof]
- 연구실: N1동 620호[^contact]
- 주소: 대전 유성구 과학로 335(랩 표기)[^contact]

[^intro]: 랩 첫 화면·소개 <https://cocoa.kaist.ac.kr/>, <https://cocoa.kaist.ac.kr/introduction.html> (2026-10-19 열람)
[^research]: 랩 연구 분야 페이지 <https://cocoa.kaist.ac.kr/research1.html> (2026-10-19 열람)
[^prof]: 랩 교수 페이지 <https://cocoa.kaist.ac.kr/members1.html> (2026-10-19 열람)
[^papers]: 랩 교수 페이지의 논문 목록 <https://cocoa.kaist.ac.kr/members1.html> (2026-10-19 열람)
[^patents]: 랩 교수 페이지의 특허 목록 <https://cocoa.kaist.ac.kr/members1.html> (2026-10-19 열람)
[^projects]: 랩 과제 페이지 <https://cocoa.kaist.ac.kr/research3.html> (2026-10-19 열람)
[^members]: 랩 구성원 페이지 <https://cocoa.kaist.ac.kr/members2.html>, members3.html, members4.html (2026-10-19 열람)
[^alumni]: 랩 졸업생 페이지 <https://cocoa.kaist.ac.kr/members6.html> (2026-10-19 열람)
[^contact]: 랩 연락처 페이지 <https://cocoa.kaist.ac.kr/contact.html> (2026-10-19 열람)
[^p1]: H. Jung, J. Ha, Physical Review A 111, 042424 (온라인 2025-04-18). <https://doi.org/10.1103/physreva.111.042424> 초록 기준(출판사 논문 페이지).
[^p2]: H. Jung, I. Ali, J. Ha, IEEE Transactions on Quantum Engineering 5, 1-13 (2024). <https://doi.org/10.1109/tqe.2024.3419773> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: H. Zhang, J. Ha, Journal of Lightwave Technology 44, 8937-8951 (2026). <https://doi.org/10.1109/jlt.2026.3730890> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: G. Daniel, H. Zhang, I. Ali, J. Ha, IEEE Transactions on Communications 73, 6993-7006 (2025). <https://doi.org/10.1109/tcomm.2025.3544977> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: S. Han, B. Kim, J. Chung, J. Ha, IEEE Communications Letters 28, 1750-1754 (2024). <https://doi.org/10.1109/lcomm.2024.3407143> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: H. Yeom, J. Park, J. Choi, J. Ha, IEEE Transactions on Vehicular Technology 74, 10565-10581 (2025). <https://doi.org/10.1109/tvt.2025.3543898> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: H. Joe, H. Yeom, H. D. Nguyen, J. Ha, IEEE Internet of Things Journal 13, 41070-41086 (2026). <https://doi.org/10.1109/jiot.2026.3711144> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: H. D. Nguyen, H. Yeom, J. Ha, IEEE Transactions on Aerospace and Electronic Systems 62, 2218-2235 (2026). <https://doi.org/10.1109/taes.2025.3635574> 초록 기준(Semantic Scholar 등록 초록).

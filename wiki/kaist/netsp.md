# 네트워크 보안 및 프라이버시 연구실 (Network Security and Privacy Research Lab, NetS&P)

**KAIST 전산학부 · 강민석 교수**

- 분야: 인터넷 라우팅과 서비스 거부(DoS) 공격·방어, 토르(Tor) 익명 네트워크 보안, 블록체인 네트워크·합의 보안, 이동통신(5G·6G) 보안, 암호화 통신과 화상회의의 프라이버시
- 대분야: 컴퓨팅·AI
- 태그: 네트워크 보안·프라이버시[^p1][^p6][^p7], 블록체인[^p3][^p4][^p5], 컴퓨터 네트워크[^p2]
- 홈페이지: <https://netsp.kaist.ac.kr/>
- 근거와 출처: [NetS&P 근거 페이지](netsp-sources.md)

> 인터넷, 블록체인, 이동통신망처럼 실제로 돌아가는 네트워크 시스템에서 설계와 현실이 어긋나는 틈을 찾아 공격 가능성을 증명하고, 운영자가 실제로 쓸 수 있는 방어책을 만드는 연구실이다. 찾아낸 취약점이 비트코인·이더리움 소프트웨어 수정, 줌(Zoom) 보안 패치로 이어졌다.[^home][^research]

## 무엇을 연구하나

연구실은 실제 네트워크·분산 시스템의 보안과 프라이버시를 연구하며, 특히 프로토콜 설계가 배포 현실(라우팅(데이터가 갈 길을 정하는 일) 구조, 제어 논리, 자원 관리, 메타데이터(내용이 아니라 언제 누구와 주고받았는지 같은 정보) 노출, 시스템 층 사이 상호작용)과 만날 때 생기는 실패에 주목한다고 소개한다. 공격 분석, 대규모 측정, 시험망 실험, 시제품 개발을 함께 써서 현실에서 성립하지 않는 보안 가정을 찾고 운영자가 배포할 수 있는 방어책을 설계하는 것이 목표다.[^research]

첫 번째 갈래는 **인터넷 기반 시설과 프로그래머블 네트워크 보안**이다. 인터넷 경로 정보가 위조되는 것을 막는 경로 출처 검증(ROV)이 정당한 긴급 경로 변경까지 조용히 버리는 문제를, 주소 소유자에게 실시간으로 확인받는 방식(iROV)으로 풀었다.[^p2] 프로그래머블 스위치(동작을 소프트웨어로 바꿀 수 있는 네트워크 장비)의 DoS 방어 기능 자체가 새 공격 통로가 될 수 있음을 보이고 방어 구조를 제안했다.[^p1] 교수는 2013년 목표 지역을 직접 공격하지 않고 그곳으로 가는 길목 링크에 트래픽을 몰아 지역을 끊는 공격(Crossfire)을 발표했고, 이후 연구로 라우팅 구조가 공격 표면이 된다는 점을 다뤘다.[^research][^prof]

두 번째 갈래는 **토르와 익명 네트워크 보안**이다. 토르(Tor)는 접속 경로를 여러 중계 컴퓨터로 감싸 누가 어디에 접속하는지 숨기는 익명 네트워크다. 익명성을 지키면서 공격에도 버텨야 하는 토르 숨은 서비스(onion service)에서, 방어용 퍼즐 난이도를 부풀려 정상 사용자를 막는 공격(OnionFlation)을 보였다. 이 연구는 USENIX Security 2025 Honorable Mention(입선)을 받았다.[^research][^home]

세 번째 갈래는 **블록체인 보안**이다. 이더리움 노드(네트워크에 참여하는 컴퓨터)를 모든 연결을 장악하지 않고도 몇 시간 동안 고립시키는 공격,[^p3] 서로 다른 블록체인 클라이언트가 블록 갈래(포크)를 처리하는 방식의 차이를 찾는 퍼징 도구(무작위 입력으로 오류를 찾는 시험 기법),[^p4] 거래 순서를 공정하게 정한다는 시스템에서도 남보다 먼저 거래를 끼워 넣는 선행매매 공격이 가능함을 보였다.[^p5]

네 번째 갈래는 **이동통신 보안**이다. 기기 모델 지문으로 불법 심박스(국제 전화 사기에 쓰는 장비)를 막는 방법,[^p6] 협조하지 않는 휴대 기기의 실제 위치를 찾는 방법을 연구했다.[^research]

다섯 번째 갈래는 **온라인 시스템의 프라이버시**다. 암호화된 DNS(DoH; DNS는 사이트 이름을 인터넷 주소로 바꿔 주는 체계)가 일반 DNS로 강등되는 현상을 전 세계에서 측정했고,[^p7] 화상회의 기능별로 사용자가 느끼는 프라이버시를 조사했다.[^p8] 화상회의 시스템의 화면과 실제 네트워크 동작의 차이에서 줌의 취약점을 찾아 보안 번호(CVE-2024-45424)를 받고 2만 달러 버그 포상금을 받았다.[^research][^home]

연구 페이지는 연구가 실제 시스템을 바꾼 사례로, 비트코인 코어가 연구실의 공격(Erebus)을 계기로 자율 시스템(AS, 인터넷을 이루는 개별 관리 단위 네트워크) 단위 연결 분산 기능을 넣었고, 이더리움 클라이언트(Go Ethereum)가 연구실이 제안한 완화책을 받아들였으며, 토르 프로젝트가 퍼즐 난이도 공격 대응을 검토 중이라고 적는다.[^research]

## 주요 연구 주제

### 1. 인터넷 라우팅·데이터 평면 보안

대화형 경로 검증, 프로그래머블 스위치 DoS.[^p1][^p2][^research] 대표 논문 1, 2.

### 2. 블록체인 네트워크·합의 보안

이더리움 고립 공격, 포크 처리 퍼징, 공정 순서 시스템 선행매매.[^p3][^p4][^p5] 대표 논문 3, 4, 5.

### 3. 이동통신 보안과 온라인 프라이버시

심박스 탐지, 암호화 DNS 강등, 화상회의 프라이버시.[^p6][^p7][^p8] 대표 논문 6, 7, 8.

## 대표 논문

랩 논문 목록의 2021–2027년 논문에서 주제별로 골랐다. 3은 랩 목록이 교수를 교신저자로 표시한 공동 연구이고, 6은 교수가 공저자로 참여한 공동 연구다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2026 | [On the Security Risks of Memory Adaptation and Augmentation in Data-plane DoS Mitigation](https://doi.org/10.14722/ndss.2026.241857) · NDSS 2026 | 프로그래머블 스위치의 DoS 방어는 부족한 스위치 메모리를 제어부의 도움으로 늘려 빠르게 대응한다. 바로 이 기능을 역이용해 메모리 경쟁을 일으켜 방어를 마비시키는 공격(Heracles)을 실제 장비에서 보이고, 메모리 작업을 층별로 나누는 방어 구조(Shield)를 제안했다.[^p1] | 1저자 Hocheol Nam, 마지막 저자 강민석 |
| 2 | 2026 | iROV: Breaking the Silence of RPKI with Interactive Validation · USENIX Security 2026 | 경로 출처 검증은 등록 정보와 다른 경로를 주소 소유자에게 묻지 않고 버려, DDoS 대응 같은 긴급 경로 변경이 막힌다. 라우터가 소유자에게 실시간 허가를 묻는 iROV를 제안해 긴급 경로의 도달률을 23%에서 최대 약 90%로 높였다.[^p2] | 1저자 Younsoo Kim, 마지막 저자 강민석 |
| 3 | 2023 | [Partitioning Ethereum without Eclipsing It](https://doi.org/10.14722/ndss.2023.24465) · NDSS 2023 | 이더리움 노드의 연결 절반 정도만 차지하고 느린 DoS를 걸어 노드를 몇 시간 동안 네트워크에서 고립시키는 공격(Gethlighting)을 실제 메인넷·테스트넷에서 보였다. 모든 노드를 24시간 공격하는 비용이 약 5,714달러로 낮다.[^p3] | 1저자 Hwanjo Heo, 교신 강민석(랩 표기), 마지막 저자 Seungwon Shin |
| 4 | 2025 | [Fork State-Aware Differential Fuzzing for Blockchain Consensus Implementations](https://doi.org/10.1109/icse55347.2025.00085) · ICSE 2025 | 같은 합의 규칙(블록 순서를 참여자 모두가 똑같이 정하는 규칙)을 서로 다른 개발자가 구현한 블록체인 클라이언트들이 블록 갈래(포크)를 다르게 처리하는 차이를 찾는 퍼징 도구(FORKY)를 만들어 비트코인과 이더리움에 시험했다.[^p4] | 공동 1저자 Wonhoi Kim·Hocheol Nam, 마지막 저자 강민석 |
| 5 | 2025 | [On Frontrunning Risks in Batch-Order Fair Systems for Blockchains](https://doi.org/10.1145/3719027.3744879) · ACM CCS 2025 | 거래를 들어온 순서대로 처리한다는 공정 순서 시스템(Themis)에서도 악성 노드 하나로 거의 100% 성공하는 선행매매 공격(Ambush)을 보였다. 거래 정보 전파를 적당히 늦춰 보안과 처리량을 함께 지키는 방법도 제안했다.[^p5] | 공동 1저자 Eunchan Park·Taeung Yoon, 마지막 저자 강민석 |
| 6 | 2023 | [Preventing SIM Box Fraud Using Device Model Fingerprinting](https://doi.org/10.14722/ndss.2023.24416) · NDSS 2023 | 국제 전화 사기에 쓰이는 심박스를 통신망에서 막기 위해, 쉽게 위조되는 단말 식별 번호 대신 네트워크 계층 정보 3만 1천여 개 특징으로 기기 모델을 구별하는 지문을 만들었다. 스마트폰 85종 대부분이 서로 구별됐다.[^p6] | 1저자 BeomSeok Oh, 강민석 공저, 마지막 저자 Yongdae Kim |
| 7 | 2024 | [Measuring DNS-over-HTTPS Downgrades: Prevalence, Techniques, and Bypass Strategies](https://doi.org/10.1145/3696385) · ACM CoNEXT 2024 | 암호화 DNS(DoH) 질의가 일반 DNS로 되돌려지는 강등을 바람직한 경우와 아닌 경우를 구분해 전 세계 규모로 측정했다. 강등은 전 세계에서 소수에 치우친 긴 꼬리 분포였고, 숨은 차단 장치를 찾아내 거의 완벽한 우회 전략도 설계했다.[^p7] | 1저자 Jinseo Lee, 마지막 저자 강민석 |
| 8 | 2025 | [Understanding User Privacy Perceptions in Video Conferencing: Insights from a Feature-Specific User Study](https://doi.org/10.56553/popets-2025-0096) · PETS 2025 | 업무 회의, 온라인 수업 같은 상황별로 화상회의 기능(집중도 추적, 녹화, 고정·스포트라이트 등)에 대한 사용자 프라이버시 인식을 조사했다. 남이 내 화면을 고정하거나 강조할 때 큰 불편을 느끼는 새 우려를 찾았다.[^p8] | 1저자 Hobin Kim, 마지막 저자 강민석 |

## 교수와 전문 분야

강민석 교수는 KAIST 전기및전자공학(EECS) 학사(2006)·석사(2008)와 미국 카네기멜런대 전기컴퓨터공학 박사(2016)를 받았다. 싱가포르국립대(NUS) 전산학부 조교수(2016–2020)를 거쳐 2020년 KAIST 전산학부 조교수로 부임했고, 2023년 8월부터 부교수다. 2023–2026년 권오현 석좌 조교수로 임명됐다.[^prof][^people] 연구 관심은 네트워크·분산 시스템 보안, 블록체인 보안, 이동통신망 보안, IoT 시스템 보안이다.[^prof] NDSS, ACM CCS 등 보안 학회 프로그램 위원을 여러 차례 맡았다.[^prof]

랩 소식에 따르면 교수는 이화여대·성신여대 교수와 함께 토르 보안·프라이버시를 주제로 한 한국연구재단 글로벌 기초연구실(15억 원)을 이끌고(2025), 2022년 아시아 최대 규모의 국제 블록체인 연구 센터(BRC) 공동 설립 소장을 싱가포르국립대 Prateek Saxena 교수와 함께 맡았다. 2023년 KAIST 공과대학 송암 우수 연구상을 받았다.[^home]

논문으로 보면 전문 분야는 세 갈래다.

- **인터넷 라우팅과 데이터 평면 보안**.[^p1][^p2]
- **블록체인 네트워크·합의 보안**.[^p3][^p4][^p5]
- **이동통신·프라이버시 측정**.[^p6][^p7][^p8]

## 응용 분야

대표 논문과 연구 사례로 보면 인터넷 서비스 사업자와 통신사 보안, 암호화폐·블록체인 플랫폼, 화상회의 서비스, 수사 기관의 사기 탐지·추적에 닿아 있다.[^p2][^p5][^p6][^research] 과제 목록에는 경찰청 보이스피싱 탐지·추적, 6G·위성 지상국 보안, 레이어2 블록체인 기반 가상자산 추적 같은 과제가 있다.[^projects]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다. 이름 옆 괄호는 소속 학과(정보보호대학원 또는 전산학부)다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Hocheol Nam (정보보호대학원) | 박사과정 | hcnam@kaist.ac.kr | 1, 4, 5 |
| SeungJin Baek (정보보호대학원) | 박사과정 | seungjinb@kaist.ac.kr | 2 |
| Won Hoi Kim (정보보호대학원) | 박사과정 | wh.kim@kaist.ac.kr | 4 |
| Seungwon Woo (정보보호대학원) | 박사과정 | seungww@kaist.ac.kr | 3 |
| Eunchan Park (정보보호대학원) | 박사과정 | paul.park@kaist.ac.kr | 5 |
| Dong Hyeok Kim (전산학부) | 박사과정 | kimdh98@kaist.ac.kr |  |
| Jinseo Lee (전산학부) | 박사과정 | jinseo.vik.lee@kaist.ac.kr | 7 |
| Janin Chaib (정보보호대학원) | 박사과정 | janin.chaib@kaist.ac.kr |  |
| Younsoo Kim (전산학부) | 석사과정 | younsookim@kaist.ac.kr | 2 |
| Wonho Song (전산학부) | 석사과정 | swh0329@kaist.ac.kr | 8 |
| Kyonghwa Song (정보보호대학원) | 석사과정 | song20@kaist.ac.kr |  |
| Yeonjong Jeong (전산학부) | 석사과정 | jyj020121@kaist.ac.kr |  |
| Amin Jalilov (전산학부) | 석사과정 | amin@kaist.ac.kr | 4 |
| Ahmad Elmoursi (전산학부) | 학부 연구생 | ahmadsm2005@kaist.ac.kr |  |
| Wooil Kim (전산학부) | 학부 연구생 | wooilkim@kaist.ac.kr |  |
| Uihyuk Moon (전산학부) | 학부 연구생 | eihyukmoon@kaist.ac.kr |  |
| Murad Ibrahimov (전산학부) | 학부 연구생 | murad2006@kaist.ac.kr |  |

## 졸업생과 이전 구성원

랩 구성원 페이지의 이전 구성원(학부 인턴 포함)과 랩이 적은 현재 소속이다. 싱가포르국립대 시절 구성원도 포함돼 있다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Mintae Kim | M.S. (KAIST) (2026) |  |
| Daehyun Lim | M.S. (KAIST) (2026) |  |
| Dongpyeong Seo | M.S. (KAIST) (2026) | Security Engineering at Hyundai Motor Company |
| Jaewoo Park | M.S. (KAIST) (2026) | Researcher at National Security Research Institute |
| Hoang Ngoc Bao Khue |  | Undergrad, KAIST |
| Jongkook Han |  | SoC undergrad, KAIST |
| Moonjung Kim |  | SoC undergrad, KAIST |
| Poopha Suwananek |  | Undergrad, Chulalongkorn University |
| Soyeon Park |  | SoC undergrad, KAIST |
| Hobin Kim | M.S. (KAIST) (2025) | PhD student at CMU |
| Taeung Yoon | M.S. (KAIST) (2025) | PhD student at UIUC |
| Aya Hamane |  | Undergrad, EPFL |
| Aziz Huseynov |  | SoC undergrad, KAIST |
| Amin Jalilov |  | SoC undergrad, KAIST |
| Jaehong Jung |  | Undergrad, GIST |
| Harin Kim |  | SoC undergrad, KAIST |
| Byungkyu Kong |  | SoC undergrad, KAIST |
| Jaehyun Ha | M.S. (KAIST) (2024) | Blockchain research analyst at Presto Labs |
| Yongwoo Oh | M.S. (KAIST) (2023) | Researcher at Desilo |
| Byoungjun Choi | M.S. (KAIST) (2023) |  |
| Muoi Tran | Ph.D. (NUS) (2022) | Postdoc researcher at ETH Zurich |
| Nitya Lakshmanan | Ph.D. (NUS) (2022) | Lecturer at National University of Singapore |
| Michael Hu |  | Currently PhD student at NUS |
| Akshaye Shenoi |  | PhD student at NUS; Master's degree at NUS |
| JunSeoung Choi |  | SoC undergrad, KAIST |
| Jehyun Lee |  | Researcher at Singtel/TrustWave |
| Levente Csikor |  | Researcher at Singtel/TrustWave |
| Xin Zhe Khooi |  | PhD at National University of Singapore |
| Andre Pousinho |  | PhD at National University of Singapore |
| Anh V. Vu |  | Japan Advanced Institute of Science and Technology |
| Gunwoo Kim |  | Postech |
| Videet Singhai |  | Carnegie Mellon University |
| Deli Gong |  | Zilliqa |
| Waqar Ahmad |  | PhD student at Tsinghua University |
| Inkyu Bang |  | Hanbat National University, South Korea |
| Gi Jun Moon |  | Korea University |
| Inho Choi |  | Yonsei University; currently, PhD student at NUS |
| Jun Seung Lee |  | Seoul National University |
| Junhee Lee |  | Sejong University |
| Hyowan Park |  | Sejong University |
| Seunghun Kim |  | Sejong University |
| Soyeon Park |  | currently PhD at Georgia Tech |
| Seunghoon Woo |  | currently PhD at Korea Univ |
| Weichuan Tan |  | Master at NUS |
| Victor Nguyen |  | Master at NUS |
| Jungki Min |  | from Korea Univ |
| Dong Sung Kim |  | from Korea Univ |

## 최근 논문 목록 (2021–2027)

랩 논문 목록의 2021년 이후 학술대회·학술지 논문 18편이다.[^papers]

**2027**

- Jinseo Lee, Jongkook Han, Yixin Sun, Min Suk Kang. "On the Effectiveness of NetFlow-Based Deanonymization of Tor Onion Services". *IEEE Symposium on Security and Privacy (IEEE S&P), May 2027. (To Appear)*.

**2026**

- Xin Zhe Khooi, Satis Kumar Permal, Dong Hyeok Kim, Robert Schmidt, Min Suk Kang, Mun Choon Chan. "THOR: Fine-grained Per-UE Baseband Routing in vRAN". *International Conference on Mobile Computing and Networking (ACM MobiCom), Oct 2026. (To Appear)*.
- Younsoo Kim, Seungjin Baek, Weitong Li, Taejoong Chung, Min Suk Kang. "iROV: Breaking the Silence of RPKI with Interactive Validation". *USENIX Security, August 2026*.
- Hocheol Nam, Daehyun Lim, Huancheng Zhou, Guofei Gu, Min Suk Kang. "On the Security Risks of Memory Adaptation and Augmentation in Data-plane DoS Mitigation". *Network and Distributed System Security Symposium (NDSS), February 2026*.

**2025**

- Eunchan Park\*, Taeung Yoon\*, Hocheol Nam, Deepak Maram, Min Suk Kang. "On Frontrunning Risks in Batch-Order Fair Systems for Blockchains". *ACM Conference on Computer and Communications Security (CCS), Oct 2025*.
- Jinseo Lee, Hobin Kim, Min Suk Kang. "Onions Got Puzzled: On the Challenges of Mitigating Denial-of-Service Problems in Tor Onion Services". *USENIX Security (USENIX Security), Aug 2025*.
- Hobin Kim, Wonho Song, Joseph Seering, and Min Suk Kang. "Understanding User Privacy Perceptions in Video Conferencing: Insights from a Feature-Specific User Study". *Privacy Enhancing Technologies Symposium (PETS), July 2025*.
- Wonhoi Kim\*, Hocheol Nam\*, Muoi Tran, Amin Jalilov, Zhenkai Liang, Sang Kil Cha, and Min Suk Kang. "Fork State-Aware Differential Fuzzing for Blockchain Consensus Implementations". *IEEE/ACM International Conference on Software Engineering (IEEE/ACM ICSE), Apr 2025*.

**2024**

- Jinseo Lee, David Mohaisen, Min Suk Kang. "Measuring DNS-over-HTTPS Downgrades: Prevalence, Techniques, and Bypass Strategies". *International Conference on emerging Networking EXperiments and Technologies (ACM CoNEXT), Dec 2024*.
- Taekkyung Oh, Sangwook Bae, Junho Ahn, Yonghwa Lee, Tuan Dinh Hoang, Min Suk Kang, Nils Ole Tippenhauer, Yongdae Kim. "Enabling Physical Localization of Uncooperative Cellular Devices". *International Conference On Mobile Computing And Networking (MobiCom), Nov 2024*.

**2023**

- Jaehyun Ha, Seungjin Baek, Muoi Tran, Min Suk Kang. "On the Sustainability of Bitcoin Partitioning Attacks". *Financial Cryptography and Data Security (FC), May 2023*.
- Hwanjo Heo, Seungwon Woo, Tae Ung Yoon, Min Suk Kang (corresponding), Seungwon Shin. "Partitioning Ethereum without Eclipsing It". *Network and Distributed System Security Symposium (NDSS), February 2023*.
- BeomSeok Oh, Junho Ahn, Sangwook Bae, Mincheol Son, Yonghwa Lee, Min Suk Kang, Yongdae Kim. "Preventing SIM Box Fraud Using Device Model Fingerprinting". *Network and Distributed System Security Symposium (NDSS), February 2023*.

**2022**

- Nitya Lakshmanan, Abdelhak Bentaleb, Byoungjun Choi, Roger Zimmermann, Jun Han, and Min Suk Kang. "On Privacy Risks of Watching YouTube over Cellular Networks with Carrier Aggregation". *ACM IMWUT/UbiComp 2022*.
- Seungjin Baek\*, Hocheol Nam\*, Yongwoo Oh, Muoi Tran, and Min Suk Kang. "Short Paper: On the Claims of Weak Block Synchronization in Bitcoin". *Financial Cryptography and Data Security (FC), February 2022*.

**2021**

- Levente Csikor, Himanshu Singh, Min Suk Kang, and Dinil Mon Divakaran. "Privacy of DNS-over-HTTPS: Requiem for a Dream?". *IEEE European Symposium on Security and Privacy (IEEE EuroS&P), Sept 2021*.
- Muoi Tran, Akshaye Shenoi, and Min Suk Kang. "On the Routing-Aware Peering against Network-Eclipse Attacks in Bitcoin". *USENIX Security (USENIX Security), Aug 2021*.
- Nitya Lakshmanan, Nishant Budhdev, Min Suk Kang, Mun Choon Chan, and Jun Han. "A Stealthy Location Identification Attack Exploiting Carrier Aggregation in Cellular Networks". *USENIX Security (USENIX Security), Aug 2021*.

## 연구 과제

랩 과제 페이지의 연구비 지원 과제 24건과 지원 기관, 기간, 연구비다.[^projects]

- Coexistence of Tor System Security Enhancement and Illicit-Use Detection: An Integrated Approach for Balancing Anonymity and Public Safety (지원 MSIT/NRF Global Basic Research Laboratory Program; 기간 06/2025–05/2028; 연구비 KRW 1,500,000,000)
- Security Threat Response and Privacy Protection for the Global 6G NTN Ecosystem Trust Framework (지원 MSIT; 기간 07/2025–12/2026; 연구비 KRW 186,900,000)
- Security Technologies for Trusted Quantum Network Systems (지원 KAIST; 기간 07/2025–12/2026; 연구비 KRW 176,000,000)
- Cybersecurity Threat Response Technologies for Satellite Ground Stations (지원 MSIT; 기간 04/2025–12/2025; 연구비 KRW 92,000,000)
- Policy and Practical Application Study on Virtual-Asset Tracing Based on Layer-2 Blockchains (지원 Police University; 기간 05/2025–11/2025; 연구비 KRW 24,100,000)
- Discovery and Defense of New Eavesdropping Attacks Based on IoT Sensor Information (지원 MSIT; 기간 07/2024–12/2026; 연구비 KRW 303,000,000)
- Trust-Model-Based Intelligent Intrusion Response in 6G Open Network Environments and International Collaboration (지원 MSIT; 기간 07/2024–12/2026; 연구비 KRW 277,800,000)
- Future Cybersecurity Technology Research (지원 Future Science Academy; 기간 03/2024–12/2025; 연구비 KRW 363,980,000)
- Building a Scalable and Decentralized Shared-Ordering Ledger (지원 Sui Foundation; 기간 03/2024–02/2025; 연구비 KRW 33,000,000)
- Security Technologies for Advanced Blockchain Vulnerability Analysis and Mitigation (지원 ETRI; 기간 03/2023–11/2023; 연구비 KRW 50,000,000)
- Safe and Fair Blockchain Decentralization Technologies (지원 KAIST; 기간 03/2023–02/2026; 연구비 KRW 60,000,000)
- Network-Based Voice Scam Detection and Tracing Technology (지원 Korean National Police Agency; 기간 04/2022–12/2024; 연구비 KRW 498,180,000)
- Foundational Technologies for the Overall Security of Blockchain Networks (지원 ETRI; 기간 05/2022–11/2022; 연구비 KRW 50,000,000)
- Winter/Spring 2022 Undergraduate Research Program (지원 KAIST; 기간 01/2022–06/2022; 연구비 KRW 2,000,000)
- Security Technologies for Built-in 6G Autonomous Security with Continuous Security Quality Assurance (지원 MSIT; 기간 04/2021–12/2024; 연구비 KRW 331,000,000)
- 5G/6G System Side-Channel Security Analysis and Defense (지원 National Research Foundation of Korea; 기간 03/2021–12/2023; 연구비 KRW 428,440,000)
- Securing and Improving BFT Consensus Protocols with Advanced Networking (지원 Korea Blockchain Research Institute/Klaytn Improvement Reserve; 기간 07/2021–06/2022; 연구비 KRW 173,700,000)
- Privacy-Preserving and Unblockable Real-Time IoT Monitoring Technology (지원 KAIST; 기간 07/2020–12/2023; 연구비 KRW 150,000,000)
- Research of New RF Attack Methods (지원 Institute for Information Industry, Taiwan; 기간 10/2019–12/2019; 연구비 US$100,000)
- Blockchain Network Security (지원 Crystal Centre; 기간 03/2019–12/2020; 연구비 S$150,000)
- Software-Defined Security for Enterprise Networks (지원 NUS-Singtel Corp Lab; 기간 06/2018–05/2021; 연구비 S$750,900)
- Source Filtering Distributed Denial-of-Service Defense with Trusted Hardware (지원 NUS-Singtel Corp Lab; 기간 07/2018–06/2021; 연구비 S$684,700)
- PhyPatch: Patching Permanent Flaws in Wireless Protocols of Internet of Things (지원 Ministry of Education, Singapore; 기간 02/2018–02/2021; 연구비 S$106,741)
- Defending Against Extremely Large-Scale DDoS Attacks (지원 Ministry of Education, Singapore; 기간 09/2016–09/2019; 연구비 S$180,000)

## 소식

랩 첫 화면의 소식이다.[^home]

- 2026/09 · New paper on NetFlow-Based Deanonymization of Tor Onion Services has been accepted to IEEE S&P 2027! Congrats Jinseo and Jongkook!
- 2026/08 · New paper on Fine-grained Per-UE Baseband Routing in vRAN has been accepted to MobiCom 2026! Congrats Dong Hyeok!
- 2026/06 · A paper on a New Routing Security Mechanism (called interactive ROV or iROV) has been (conditionally) accepted to USENIX Security 2026! Congrats Younsoo and Seungjin!
- 2026/05 · Our Jinseo Lee (PhD student) has been selected as one of the Distinguished Artifact Evaluators for IEEE S&P 2026. Congrats Jinseo!
- 2026/03 · Our paper (OnionFlation; USENIX Security 2025) has been invited at RSA Conference 2026 for a talk. Jinseo delivered it nicely!
- 2025/12 · New paper on Our Measurement Study of Low-Earth Orbit (LEO) Satellite Networks has been accepted to SpaceSec 2026! Congrats Dongpyeong, Jaewoo, and Hocheol!
- 2025/12 · New paper on DoS Attacks against Programmable Switches (and New Defenses) has been accepted to NDSS 2026! Congrats Hocheol and Daehyun!
- 2025/10 · Congrats to two ACM CCS 2025 award winners from the group: Hocheol (CCS 2025 Distinguished Artifact Reviewers Award) and Jinseo (CCS 2025 Top Poster Reviewers Award)!
- 2025/09 · Our paper on Tor security has received the Honorable Mention Award at USENIX Security 2025! Congrats Jinseo and Hobin! (Local news articles).
- 2025/06 · Min Suk (together with Se Eun Oh at Ewha Womans University and Seongmin Kim at Sungshin Women’s University) will lead the Global Basic Research Laboratory (KRW 1,500,000K from NRF) on the topic of Tor Security and Privacy.
- 2025/05 · New paper on Frontrunning Attacks against Blockchain Fair Ordering Systems has been conditionally accepted to ACM CCS 2025! Congrats Eunchan, Taeung, and Hocheol!
- 2025/03 · New paper on Users' Privacy Perception with Video Conferencing Tools has been accepted to PETS 2025! Congrats Hobin and Wonho!
- 2025/02 · A new master student is joining our group! Welcome Younsoo Kim (KAIST SoC)!
- 2025/01 · New paper on Novel Denial-of-Service (DoS) Attacks against Tor Onion Services has been accepted to USENIX Security 2025! Congrats Jinseo and Hobin!
- 2024/12 · New undergrad interns are joining our group. Welcome MoonJung Kim (KAIST SoC), Hoang Ngoc Bao Khue (KAIST SoC), Jongkook Han (KAIST SoC)!
- 2024/11 · New paper on Fork Sate-Aware Fuzzing for PoW/PoS Blockchains (Forky) has been accepted to ICSE 2025! Congrats Wonhoi and Hocheol (and Muoi and Amin; our former members)!
- 2024/09 · A new undergrad interns are joining our group. Welcome Yeonjong Jeong (KAIST SoC)!
- 2024/09 · New paper on DoH Downgrade Attacks and Bypass Strategies has been accepted to CoNEXT 2024! Congrats Jinseo!
- 2024/09 · A high-severity security bug we discovered in the Zoom platform has been assigned the CVE ID: CVE-2024-45424, and it earned us a $20,000 bug bounty. Congrats Seungwon and Wonho!
- 2024/08 · Our Eunchan Park has received the President's Award (IITP) for outstanding achievements presented at the '2024 Digital Innovation Talent Symposium,' based on our work on frontrunning attacks against fair-ordering blockchain systems.
- 2024/08 · New paper on Physical Localization of Uncooperative Cellular Devices has been accepted to MobiCom 2024!
- 2024/06 · Two new undergrad interns are joining our group. Welcome Ahmad Elmoursi (KAIST SoC), Aya Hamane (EPFL CS)!
- 2024/05 · Min Suk's work on blockchain technology has been selected as KAIST's Major Achievement in 14 Future Technology Areas.
- 2023/03 · Three new master students are joining our group! Welcome Dongpyeong Seo (KAIST GSIS), Jaewoo Park (KAIST GSIS), and Daehyun Lim (KAIST SoC)!
- 2024/02 · Sui Foundation funds our work on secure layer-2 sequencing. Thanks Sui Foundation!
- 2023/12 · LG funds our work on blockchain layer-2 security. Thanks LG-KAIST 6G Center!
- 2023/11 · Min Suk is serving as a PC at WiSec 2024.
- 2023/09 · A new master student is joining our group! Welcome Jinseo Lee (KAIST SoC)!
- 2023/04 · Min Suk is serving as a PC at NDSS 2024.
- 2023/03 · Min Suk is appointed as Kwon Oh-Hyun Endowed Assistant Professor for three-year term.
- 2023/03 · Three new master students are joining our group! Welcome Eunchan Park (KAIST GSIS), Taeung Yoon (KAIST GSIS), and Donghyeok Kim (KAIST SoC)!
- 2023/02 · Min Suk has been awarded College of Engineering’s Songam Distinguished Research Award.
- 2023/01 · New paper on Sustainability of Bitcoin Partitioning Attacks has been accepted to FC 2023! Congrats Jaehyun and Seungjin!
- 2023/01 · Min Suk is serving as a PC at ACM CCS 2023.
- 2023/01 · Four new undergraduate interns are joining our group! Welcome Jinseo Lee (KAIST SoC), Jaewon In (SNU CS), Dongpyeong Seo (KAIST SoC), and Byungkyu Kong (KAIST SoC)!
- 2022/12 · New paper on Partitioning Ethereum without Eclipsing It has been accepted to NDSS 2023. Congrats to Seungwon Woo and Tae Ung Yoon!
- 2022/12 · New paper on Preventing SIM Box Fraud Using Device Fingerprinting has been accepted to NDSS 2023!
- 2022/08 · Min Suk will be the founding co-director (along with Prateek Saxena at NUS) of the largest international Blockchain Research Center (BRC) in Asia (news: kor1, kor2, eng1, eng2). Thanks Klaytn Foundation!
- 2022/07 · Four new undergrad interns are joining our group. Welcome Taeung Yoon (Yonsei CS), Harin Kim (KAIST SoC), Seungmin Park (KAIST MS), and Amin Jalilov (KAIST SoC)!
- 2022/04 · Our alumni Dr. Nitya Lakshmanan will join School of Computing, NUS as a lecturer (teaching faculty member). Congrats Nitya!
- 2022/03 · Three new master students are joining our group! Welcome Wonhoi Kim (KAIST GSIS), Jaehyun Ha (KAIST GSIS), and Mintae Kim (KAIST SoC)!
- 2022/02 · Muoi has successfully defended his PhD thesis titled "Handling Network Attacks Exploiting Routing Information Asymmetries." Congrats Dr. Muoi Tran!
- 2022/02 · Nitya has successfully defended her PhD thesis titled "Risks and Use of Side Channels in Modern Wireless Systems." Congrats Dr. Nitya Lakshmanan!
- 2022/02 · Min Suk has been awarded The Soo-Young Lee Teaching Innovation Award (excellent prize).
- 2022/02 · Our recent work on Privacy Risk of Watching YouTube over Cellular Networks has been accepted to IMWUT/UbiComp 2022. Congrats to Nitya and Byoungjun!
- 2022/01 · Min Suk is serving as a PC at ACM CCS 2022 and ACM WiSec 2022.
- 2022/01 · One new undergrad intern is joining our group. Welcome Mintae Kim (Postech ITC)!
- 2021/12 · Two new undergrad interns are joining our group. Welcome Seohee Lee (KAIST SoC) and Junhyun Jang (KAIST SoC)!
- 2021/12 · Min Suk gave a talk at Department of Information and Communication Engineering at DGIST on Blockchain Security.
- 2021/11 · Our recent work on measuring block synchronization in Bitcoin has been accepted to FC 2022. Congrats to Seungjin, Hocheol, Yongwoo, and Muoi!
- 2021/10 · Min Suk had an interview with Arirang News In-Depth on Cyber Warfare and Ransomware.
- 2021/09 · We publish our recent findings on weak block synchronization in Bitcoin (Cryptology ePrint Archive: Report 2021/1282).
- 2021/09 · Min Suk is giving a talk at CS department at Yonsei University on Blockchain Security.
- 2021/09 · A new master student is joining our group. Welcome Hocheol Nam (KAIST GSIS)!
- 2021/07 · Our work on Defending against Network-Sybil Attacks in Bitcoin has been presented at The third workshop on Theory and Practice of Blockchains 2021. See the full presentation YouTube by Muoi Tran!
- 2021/07 · A new undergrad intern joins our group. Welcome Hobin Kim (KAIST SoC)!
- 2021/04 · Min Suk is listed as a Rising Star in the ICT field in Korea. See the interview.
- 2021/03 · Our recent work on Identifying DNS-over-HTTPS (DoH) messages using Machine Learning has been accepted to IEEE EuroS&P 2021. Congrats to Levi and Himanshu!
- 2021/02 · Our recent work on Defending against Network-Sybil Attacks in Bitcoin has been accepted to USENIX Security 2021. Congrats to Muoi and Akshaye!
- 2021/02 · Min Suk won the NRF Young Researcher Program (2021-2024) on the topic of 5G/6G system side-channel security analysis.
- 2021/02 · Three new master students are joining our group. Welcome Byoungjun Choi (KAIST GSIS), Yong Woo Oh (KAIST GSIS), and SeungJin Baek (KAIST SoC)!
- 2021/01 · Three new undergrad interns are joining our group. Welcome JunSeoung Choi (KAIST SoC), Wonhoi Kim (KAIST SoC), and Yonatan Gizachew (KAIST EE)!
- 2020/11 · Our work is acknowledged in GSMA Mobile Security Hall of Fame and it is referenced CVD-2020-40. Congrats to Nitya!
- 2020/10 · Min Suk presented at ISEC 2020 on New Trends in Enterprise Network Security in the Post-COVID Era.
- 2020/09 · Our recent work on Location Privacy Attack in Modern Cellular Networks has been accepted to USENIX Security 2021. Congrats to Nitya!
- 2020/09 · Min Suk presented at the Graduate School Seminar at UNIST.
- 2020/08 · Min Suk is joining School of Computing at KAIST from 26 Aug 2020.
- 2020/06 · CoinDesk covers how the latest Bitcoin Core code tries to address our Erebus attack (but fails to fix it completely).
- 2020/06 · I will leave NUS and start a new network security & privacy research group at KAIST from August 2020.
- 2020/05 · Our Erebus attack (a Bitcoin partitioning attack) was presented at the online IEEE S&P 2020: see a 1-min video or a full video (project website)
- 2020/03 · Our recent work on Amplification DDoS defense utilizing programmable switches is accepted for presentation at IEEE NetSoft 2020. Congrats to Khooi!
- 2019/11 · I will be serving as a PC at ACM CCS 2020 and IEEE ICDCS 2020.
- 2019/10 · Muoi Tran (4th-year PhD) has won the 2019 Microsoft Research Asia Fellowship. Congrats to Muoi!
- 2019/10 · Our recent work on DoS against Open vSwitches is accepted for presentation at the Open vSwitch 2019 Fall Conference. Congrats to Levente! paper
- 2019/09 · I was invited to give a talk on DDoS/Bitcoin attacks at KAIST, DGIST, Postech, Korea Univ, Tsinghua Univ. Talk slides can be found here.
- 2019/09 · Our paper on a novel Denial-of-Service attack against Open vSwitches has been accepted to ACM CoNEXT 2019. Congrats to Levente!
- 2019/09 · Institute for Information Industry (III), Taiwan funded our work on 5G security. Thanks III!
- 2019/08 · Our Erebus Bitcoin attack project webpage has been revamped! Please check this out.
- 2019/08 · Muoi Tran (4th-year PhD) receives Dean’s Graduate Research Excellence Award. Congrats to Muoi!
- 2019/07 · I was invited to give a talk on Bitcoin and 5G attacks at III, Taiwan.
- 2019/07 · Our paper on a Stealthy Partitioning Attack against Bitcoin has been accepted to IEEE S&P 2020. Congrats to Muoi, Inho, Gi Jun, Viet-Anh! paper
- 2019/05 · Muoi Tran (3rd-year PhD) has been awarded President’s Graduate Fellowship (PGF). Congrats to Muoi!
- 2019/03 · Our paper on Verifiable In-network Filtering for DDoS Defense has been accepted to IEEE ICDCS 2019. Congrats to Deli and Muoi!
- 2019/03 · Our paper on Detecting Surveillance Camera Looping Attacks via Wi-Fi has been accepted to ACM WiSec 2019. Congrats to Nitya!
- 2018/12 · Our paper on Transit-link DDoS Attacks and Defenses has been accepted to IEEE S&P 2019. Congrats to Muoi! (Link to the paper)

## 연락과 위치

- 교수 이메일: minsukk@kaist.ac.kr[^contact][^people]
- 위치: KAIST N5동 2322호 (대전 유성구 대학로 291)[^contact]

[^home]: NetS&P 누리집 첫 화면(소개·소식) <https://netsp.kaist.ac.kr/> (2026-10-19 열람)
[^research]: NetS&P 연구 페이지 <https://netsp.kaist.ac.kr/research> (2026-10-19 열람)
[^people]: NetS&P 구성원 페이지 <https://netsp.kaist.ac.kr/people> (2026-10-19 열람)
[^prof]: NetS&P 교수 소개 <https://netsp.kaist.ac.kr/min-suk-kang> (2026-10-19 열람)
[^papers]: NetS&P 논문 목록 <https://netsp.kaist.ac.kr/publications> (2026-10-19 열람)
[^projects]: NetS&P 과제 페이지 <https://netsp.kaist.ac.kr/projects> (2026-10-19 열람)
[^contact]: NetS&P 연락처 <https://netsp.kaist.ac.kr/contact> (2026-10-19 열람)
[^p1]: H. Nam 외, M. S. Kang, Proceedings 2026 Network and Distributed System Security Symposium (2026). <https://doi.org/10.14722/ndss.2026.241857> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: Y. Kim 외, M. S. Kang, USENIX Security Symposium 2026 (2026). <https://www.usenix.org/conference/usenixsecurity26/presentation/kim-younsoo> 초록 기준(출판사 논문 페이지).
[^p3]: H. Heo 외, S. Shin, Proceedings 2023 Network and Distributed System Security Symposium (2023). <https://doi.org/10.14722/ndss.2023.24465> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: W. Kim 외, M. S. Kang, 2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE), 3048-3059 (2025). <https://doi.org/10.1109/icse55347.2025.00085> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: E. Park 외, M. S. Kang, Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security, 918-932 (온라인 2025-11-22). <https://doi.org/10.1145/3719027.3744879> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: B. Oh 외, Y. Kim, Proceedings 2023 Network and Distributed System Security Symposium (2023). <https://doi.org/10.14722/ndss.2023.24416> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: J. Lee, D. Mohaisen, M. S. Kang, Proceedings of the ACM on Networking 2, 1-22 (온라인 2024-11-25). <https://doi.org/10.1145/3696385> 초록 기준.
[^p8]: H. Kim, W. Song, J. Seering, M. S. Kang, Proceedings on Privacy Enhancing Technologies 2025, 213-241 (2025). <https://doi.org/10.56553/popets-2025-0096> 초록 기준.

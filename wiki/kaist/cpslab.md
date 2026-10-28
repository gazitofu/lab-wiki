# 사이버 물리 시스템 연구실 (CPSLAB)

**KAIST 전산학부 · 신인식 교수**

- 분야: 실시간 임베디드 시스템, 모바일 컴퓨팅, 인간–컴퓨터 상호작용, 시스템 보안
- 대분야: 컴퓨팅·AI
- 태그: 컴퓨터 구조·운영체제[^p6][^p8], 컴퓨터 네트워크[^p7], 프로그램 분석·검증[^p1][^p8], 소프트웨어·시스템 보안[^p8], 인간–컴퓨터 상호작용[^p3], 대형 언어 모델[^p2], 강화학습[^p4], 실시간·임베디드 시스템[^p6][^p4]
- 홈페이지: <https://cs.kaist.ac.kr/research/labView?sn=71&menu=64>
- 근거와 출처: [사이버 물리 시스템 연구실 근거 페이지](cpslab-sources.md)

> 컴퓨터가 실제 기기와 사람의 행동에 맞춰 제때 동작하도록 계산·통신·앱 조작을 설계하고, 모바일 기기의 에너지 관리와 시스템 오류 검사를 연구하는 연구실이다.[^lab][^p1][^p4][^p7][^p8]

## 무엇을 연구하나

사이버 물리 시스템(CPS, Cyber-Physical Systems)은 컴퓨터의 계산·통신과 물리 세계의 동작을 결합하는 시스템이다. 연구실은 사람이 그 시스템의 중요한 일부라는 관점에서, 실시간 시스템(정해진 시간 안에 결과를 내는 것이 동작 조건인 시스템), 모바일 컴퓨팅(이동하며 사용하는 기기의 정보 처리), 인간–컴퓨터 상호작용(사람과 컴퓨터 사이의 입력·출력과 사용 경험)을 함께 연구한다고 소개한다. 학과 교수 소개는 신인식 교수의 관심 분야로 모바일 컴퓨팅, 시스템 보안, 실시간 임베디드 시스템(기기 안에서 특정 기능을 수행하며 시간 조건을 지키는 컴퓨터 시스템)을 든다.[^lab][^prof]

첫째 축은 **제때 끝나는 계산과 통신**이다. LaLaRAND는 심층 신경망(DNN, Deep Neural Network, 자료의 규칙을 배우는 연산 모형을 여러 층으로 연결한 것)의 층마다 CPU(Central Processing Unit, 프로그램 명령을 처리하는 중앙처리장치)와 GPU(Graphics Processing Unit, 그래픽 처리를 비롯한 병렬 계산을 수행하는 장치)를 배분한다. 계산을 어디에서 실행할지와 수치 표현을 함께 조정해 실행 마감을 지키는 과제 묶음을 늘리는 연구다.[^p6] RT-SDN은 소프트웨어 정의 네트워킹(SDN, Software-Defined Networking, 소프트웨어 제어기로 통신망의 동작을 정하는 방식)을 이용해 데이터가 지나갈 경로와 처리 우선순위를 함께 정한다. 출발지에서 목적지까지 데이터가 정해진 시간 안에 도착하도록 하는 것이 목표다.[^p7]

둘째 축은 **사람이 앱과 기기를 다루는 방식**이다. FLUID-IoT는 사물인터넷(IoT, Internet of Things, 사물들이 통신망에 연결되어 정보를 주고받는 체계) 기기를 공유하는 사람마다 화면 구성 요소에 대한 접근 권한을 달리 주는 방법이다.[^p3] MobileGPT는 대형 언어 모델(LLM, Large Language Model, 많은 언어 자료를 학습해 언어를 이해하고 생성하는 모형)로 앱의 작업 절차를 배우고 기억해 다시 쓰는 자동화 시스템이다.[^p2] VeriSafe Agent는 자연어 지시를 형식 검증(논리식으로 표현한 조건을 시스템 동작이 만족하는지 확인하는 방법)에 쓸 명세로 바꾸고, 모바일 GUI(Graphical User Interface, 그림·버튼·메뉴로 조작하는 화면) 에이전트(사용자 대신 목표에 맞춰 행동하는 소프트웨어)가 실행하려는 동작을 사전에 검사한다.[^p1]

셋째 축은 **모바일 에너지와 시스템 신뢰성**이다. EarDVFS는 강화학습(행동 결과로 받은 보상을 바탕으로 행동 방식을 배우는 방법)을 이용해 DVFS(Dynamic Voltage and Frequency Scaling, 프로세서의 전압과 주파수를 동작 중 조절하는 기술)를 기기와 주변 온도에 맞춘다.[^p4] MixMax는 성질이 다른 배터리의 조합 비율과 충전·방전(배터리에 전기를 저장하고 꺼내 쓰는 과정) 정책을 함께 정해 배터리 잔량이 낮은 시간을 줄이는 시스템이다.[^p5] 운영체제(컴퓨터 자원과 프로그램 실행을 관리하는 소프트웨어)의 커널(자원 관리와 기본 기능을 담당하는 핵심부)을 검사하는 OZZ 연구도 있다. 비순차 실행(프로세서가 명령에 적힌 순서와 다르게 메모리 접근 등을 수행하는 것)과 동시 실행(여러 스레드의 실행 과정이 겹치는 것)이 결합할 때 생기는 오류를 대상으로 한다.[^p8]

## 주요 연구 주제

### 실시간 계산 자원 배분과 통신 경로

실시간 시스템에서는 작업 결과의 정확성뿐 아니라 끝나는 시점도 다룬다. LaLaRAND는 신경망의 층별 계산을 CPU와 GPU에 나누는 스케줄링(계산 자원을 어떤 작업에 언제 배정할지 정하는 것)과 양자화(수치 값을 정해진 이산 값으로 표현하는 것)를 함께 설계한다. 정확도 손실을 억제하면서 시간 보장을 유지하는 것이 목표이며, 구현한 시스템에서 실행 마감을 지킬 수 있는 작업 묶음이 늘었다고 보고한다.[^p6] RT-SDN은 통신 경로 설정과 우선순위 결정을 연결해, 통신에 필요한 전송량과 마감 조건을 함께 맞춘다.[^p7]

### 화면 공유와 언어 모델 기반 모바일 자동화

FLUID-IoT는 기존 기기 제어 앱의 화면 구성 요소를 사용자 권한에 맞춰 나누어 보내, 기기 전체를 허용하거나 금지하는 방식에서 벗어난 접근 제어를 제안한다. 성능 평가와 사용자 연구에서는 일상적인 기기 공유에 쓸 수 있는 성능과 사용성을 보고한다.[^p3] MobileGPT는 앱 작업을 재사용 가능한 하위 작업으로 나누고, 탐색·선택·도출·회상의 절차로 작업을 학습한다.[^p2] VeriSafe Agent는 앱 조작 자동화가 사용자의 의도와 맞는지 실행 전에 논리적으로 검사해 오류 동작을 찾는 역할을 한다.[^p1]

### 모바일 기기의 온도와 배터리 사용

EarDVFS는 프로세서뿐 아니라 배터리·화면 등의 온도와 주변 온도를 고려해 동작 속도를 조절한다. 기기·작업·주변 온도를 달리한 실험에서 성능을 유지하면서 전력 효율이 개선됐다고 보고한다.[^p4] MixMax는 배터리 종류별 비율과 충방전 정책이 서로 영향을 주는 문제를 최적화 문제(제약을 지키면서 목적에 맞는 변수 값을 찾는 문제)로 만들고 여러 하위 문제로 나눠 푼다. 제작한 배터리로 모사 장치를 구성하고 스마트폰에 시제품을 구현했으며, 배터리 용량·부피·무게와 사용 습관을 희생하지 않고 잔량이 낮은 시간을 줄일 수 있었다고 보고한다.[^p5]

### 운영체제 오류 검사와 신뢰성

OZZ는 커널의 동시 실행 과정에서 메모리 접근 순서가 바뀔 때 드러나는 오류를 찾는 도구다. 실제 커널 코드가 실행되는 동안 비순차 실행을 모사하는 OEMU라는 기법을 만들고, 그것을 검사 도구에 결합했다. 실행 순서가 바뀌는 현상과 스레드 간 실행 순서의 영향을 함께 제어해 검사하며, 새로 찾은 커널 오류가 개발자에게 확인되고 수정됐다고 보고한다.[^p8]

## 대표 논문

모바일 조작과 AI, 에너지 관리, 실시간 계산·통신, 시스템 오류 검사의 네 갈래에서 2021–2025년 논문 8편을 골랐다. “쉽게 말하면” 칸은 각 논문의 초록만을 근거로 썼다. 저자 역할은 저자 순서와 원문에 명시된 교신 표시를 구분했다.[^dblp]

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 신인식 교수의 저자 역할 |
|---|---|---|---|---|
| 1 | 2025 | [VeriSafe Agent: Safeguarding Mobile GUI Agent via Logic-based Action Verification](https://doi.org/10.1145/3680207.3765248) · MobiCom | 앱을 대신 조작하는 AI가 사용자의 뜻과 어긋나는 동작을 하지 않도록, 자연어 지시를 검증 가능한 명세로 바꾸고 동작을 실행하기 전에 검사하는 시스템이다. 실험에서 검증 정확도와 작업 완료율의 개선을 보고한다.[^p1] | 마지막 저자, 공동 교신저자. 원문에 Sunjae Lee와 함께 명시.[^active] |
| 2 | 2024 | [MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation](https://doi.org/10.1145/3636534.3690682) · MobiCom | 언어 모델이 앱을 조작할 때 작업을 하위 절차로 나누고 기억해 재사용하게 한다. 새 작업을 배우고 상황에 맞게 바꾸는 실험에서 정확도와 실행 지연·비용을 평가했다.[^p2] | 마지막 저자 |
| 3 | 2024 | [FLUID-IoT : Flexible and Fine-Grained Access Control in Shared IoT Environments via Multi-user UI Distribution](https://doi.org/10.1145/3613904.3641991) · CHI | 여러 사람이 사물인터넷 기기를 공유할 때, 사람마다 허용된 버튼이나 화면 부분만 나누어 주는 접근 제어다. 기존 기기 제어 앱을 중심으로 화면을 배분하고, 동작 성능과 사용성을 평가했다.[^p3] | 마지막 저자 |
| 4 | 2025 | [EarDVFS: Environment-Adaptable RL-based DVFS for Mobile Devices](https://doi.org/10.1109/ICCAD66269.2025.11240765) · ICCAD | 모바일 기기가 놓인 환경과 부품들의 온도를 함께 고려하며 전압과 동작 주파수를 조절한다. 강화학습을 쓰는 제어를 설계해 다양한 기기·작업·온도에서 성능을 유지하며 전력 효율을 개선했다고 보고한다.[^p4] | 마지막 저자 |
| 5 | 2023 | [MixMax: Leveraging Heterogeneous Batteries to Alleviate Low Battery Experience for Mobile Users](https://doi.org/10.1145/3581791.3596843) · MobiSys | 서로 다른 성질의 배터리를 조합하고, 조합 비율과 충방전 정책을 함께 정한다. 배터리 모사 장치와 스마트폰 시제품으로 용량·부피·무게·사용 습관을 희생하지 않고 잔량이 낮은 시간을 줄이는 가능성을 보였다.[^p5] | 마지막 저자 |
| 6 | 2021 | [LaLaRAND: Flexible Layer-by-Layer CPU/GPU Scheduling for Real-Time DNN Tasks](https://doi.org/10.1109/RTSS52674.2021.00038) · RTSS | 신경망 전체를 한 계산 장치에 맡기지 않고 각 층을 CPU와 GPU에 배분하며 수치 표현도 조정한다. 실행 마감 보장을 유지하면서 정확도 손실을 억제하고, 마감을 지킬 수 있는 작업 묶음을 늘리는 연구다.[^p6] | 전체 5명 중 4번째 저자 |
| 7 | 2022 | [RT-SDN: Adaptive Routing and Priority Ordering for Software-Defined Real-Time Networking](https://doi.org/10.1109/JSYST.2021.3120539) · IEEE Syst. J. | 데이터가 이동할 경로와 먼저 처리할 순서를 함께 정하는 통신 시스템이다. 경로와 스케줄링이 서로 결과를 반영하도록 설계하고, 실제 기기로 구성한 망에서 출발지부터 목적지까지의 시간 보장을 평가했다.[^p7] | 전체 3명 중 2번째 저자 |
| 8 | 2024 | [OZZ: Identifying Kernel Out-of-Order Concurrency Bugs with In-Vivo Memory Access Reordering](https://doi.org/10.1145/3694715.3695944) · SOSP | 커널에서 메모리 접근 순서와 여러 작업의 실행 순서가 엇갈리며 생기는 오류를 찾는 도구다. 실제 코드 실행 중 비순차 실행을 모사해 검사 순서를 제어하며, 새로 찾은 오류는 커널 개발자가 확인하고 수정했다고 보고한다.[^p8] | 전체 5명 중 4번째 저자 |

## 교수와 전문 분야

신인식 교수는 2008년 KAIST 전산학과에 부임했다. 학과 교수 소개는 전공을 실시간 임베디드 시스템과 사이버-피지컬 시스템으로, 관심 분야를 모바일 컴퓨팅·시스템 보안·실시간 임베디드 시스템으로 적는다. 학위 칸은 “PhD, Univ of Pennsylvania, 2006”으로 표기한다.[^prof] 전산학부 교수 명단의 직위는 교수이며, 사이버 물리 시스템 연구실을 이끈다.[^faculty][^lab]

최근 논문으로 보면 전문 분야는 모바일 앱의 화면 분배와 언어 모델 기반 조작 자동화,[^p2][^p3] 시간 조건을 지키는 계산 자원 배분과 통신,[^p6][^p7] 모바일 기기의 에너지 관리,[^p4][^p5] 커널의 실행 순서 오류 검사로 이어진다.[^p8] VeriSafe Agent 원문은 신인식 교수를 KAIST 전산학부 소속 공동 교신저자로 명시한다.[^active]

## 응용 분야

여러 사용자가 사물인터넷 기기를 나누어 제어하는 환경과 모바일 앱 작업의 자동화에 적용한다.[^p1][^p2][^p3] 모바일 기기에서는 온도에 따른 전력 제어와 배터리 잔량이 낮은 시간의 감소를 다루며,[^p4][^p5] 실시간 임베디드 시스템의 신경망 실행과 통신 마감 보장,[^p6][^p7] 운영체제 핵심부의 오류 검사에도 연결된다.[^p8]

## 최근 논문 목록 (2021–2026)

신인식 교수의 KAIST 재직 기간에 해당하는 dblp 2021–2026년 구역의 연구 기록 32개다. 2026년 기록은 없고, 학술지 논문 6개·학회 논문 19개·책 장 1개·사전 공개본 6개를 포함한다. 모바일 앱 조작과 화면 공유, 실시간 계산·통신, 에너지 관리, 시스템 오류와 보안을 다룬다. 제목·저자·발표처는 dblp 표기이며, CoRR 항목에는 arXiv 사전 공개본임을 표시했다. 같은 연구의 사전 공개본과 출판본이 따로 실린 경우 각 기록을 그대로 두었다.[^dblp][^prof]

**2025**

- Jaeheon Kwak, Sunjae Lee, Dae R. Jeong, Arjun Kumar, Dongjae Shin, Ilju Kim, Donghwa Shin, Kilho Lee, Jinkyu Lee, Insik Shin. "Leveraging Customized Heterogeneous Batteries to Alleviate Low Battery Experience for Mobile Users". *IEEE Trans. Sustain. Comput. 10(6): 1292-1309 (2025)*.
- Jaeheon Kwak, Sangeun Oh, Jinkyu Lee, Insik Shin. "EarDVFS: Environment-Adaptable RL-based DVFS for Mobile Devices". *ICCAD 2025: 1-9*.
- Jungjae Lee, Dongjae Lee, Chihun Choi, Youngmin Im, Jaeyoung Wi, Kihong Heo, Sangeun Oh, Sunjae Lee, Insik Shin. "VeriSafe Agent: Safeguarding Mobile GUI Agent via Logic-based Action Verification". *MobiCom 2025: 817-831*.
- Jungjae Lee, Dongjae Lee, Chihun Choi, Youngmin Im, Jaeyoung Wi, Kihong Heo, Sangeun Oh, Sunjae Lee, Insik Shin. "Safeguarding Mobile GUI Agent via Logic-based Action Verification". *CoRR abs/2503.18492 (2025) (arXiv 사전 공개본)*.
- Arjun Kumar, Noppanat Wadlom, Jaeheon Kwak, Si-Hyuck Kang, Insik Shin. "mCardiacDx: Radar-Driven Contactless Monitoring and Diagnosis of Arrhythmia". *CoRR abs/2508.02274 (2025) (arXiv 사전 공개본)*.
- Youngmin Im, Byeongung Jo, Jaeyoung Wi, Seungwoo Baek, Tae Hoon Min, Joo Hyung Lee, Sangeun Oh, Insik Shin, Sunjae Lee. "Modular and Multi-Path-Aware Offline Benchmarking for Mobile GUI Agents". *CoRR abs/2512.12634 (2025) (arXiv 사전 공개본)*.

**2024**

- Sangeun Oh, Ahyeon Kim, Sunjae Lee, Kilho Lee, Dae R. Jeong, Steven Y. Ko, Insik Shin. "Supporting Flexible and Transparent User Interface Distribution Across Mobile Devices". *IEEE Trans. Mob. Comput. 23(8): 8398-8417 (2024)*.
- Sunjae Lee, Minwoo Jeong, Daye Song, Junyoung Choi, Seoyun Son, Jean Y. Song, Insik Shin. "FLUID-IoT : Flexible and Fine-Grained Access Control in Shared IoT Environments via Multi-user UI Distribution". *CHI 2024: 848:1-848:16*.
- Sunjae Lee, Junyoung Choi, Jungjae Lee, Munim Hasan Wasi, Hojun Choi, Steven Y. Ko, Sangeun Oh, Insik Shin. "MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation". *MobiCom 2024: 1119-1133*.
- Dae R. Jeong, Yewon Choi, Byoungyoung Lee, Insik Shin, Youngjin Kwon. "OZZ: Identifying Kernel Out-of-Order Concurrency Bugs with In-Vivo Memory Access Reordering". *SOSP 2024: 229-248*.
- Sera Lee, Dae R. Jeong, Junyoung Choi, Jaeheon Kwak, Seoyun Son, Jean Y. Song, Insik Shin. "SERENUS: Alleviating Low-Battery Anxiety Through Real-time, Accurate, and User-Friendly Energy Consumption Prediction of Mobile Applications". *UIST 2024: 60:1-60:20*.

**2023**

- Jaeheon Kwak, Kyunghoon Kim, Youngmoon Lee, Insik Shin, Jinkyu Lee. "Battery-aging-aware run-time slack management for power-consuming real-time systems". *J. Syst. Archit. 144: 103001 (2023)*.
- Anish Byanjankar, Yunxin Liu, Yuanchao Shu, Insik Shin, Myeongwon Choi, Hyosu Kim. "${{\sf S \text{-}UbiTap}}$S-UbiTap: Leveraging Acoustic Dispersion for Ubiquitous and Scalable Touch Interface on Solid Surfaces". *IEEE Trans. Mob. Comput. 22(11): 6800-6816 (2023)*.
- Kihyuk Nam, Taewhi Lee, Sung-Soo Kim, Insik Shin. "Learning for Spatio-temporal and Relational Data". *IEEE Big Data 2023: 6239-6241*.
- Seoyun Son, Junyoung Choi, Sunjae Lee, Jean Y. Song, Insik Shin. "It is Okay to be Distracted: How Real-time Transcriptions Facilitate Online Meeting with Distraction". *CHI 2023: 64:1-64:19*.
- Dae R. Jeong, Minkyu Jung, Yoochan Lee, Byoungyoung Lee, Insik Shin, Youngjin Kwon. "Diagnosing Kernel Concurrency Failures with AITIA". *EuroSys 2023: 94-110*.
- Jaeheon Kwak, Sunjae Lee, Dae R. Jeong, Arjun Kumar, Dongjae Shin, Ilju Kim, Donghwa Shin, Kilho Lee, Jinkyu Lee, Insik Shin. "MixMax: Leveraging Heterogeneous Batteries to Alleviate Low Battery Experience for Mobile Users". *MobiSys 2023: 247-260*.
- Dae R. Jeong, Byoungyoung Lee, Insik Shin, Youngjin Kwon. "SegFuzz: Segmentizing Thread Interleaving to Discover Kernel Concurrency Bugs through Fuzzing". *SP 2023: 2104-2121*.
- Sunjae Lee, Junyoung Choi, Jungjae Lee, Hojun Choi, Steven Y. Ko, Sangeun Oh, Insik Shin. "Explore, Select, Derive, and Recall: Augmenting LLM with Human-like Memory for Mobile Task Automation". *CoRR abs/2312.03003 (2023) (arXiv 사전 공개본)*.

**2022**

- Sangeun Oh, Insik Shin, Kilho Lee. "RT-SDN: Adaptive Routing and Priority Ordering for Software-Defined Real-Time Networking". *IEEE Syst. J. 16(2): 2379-2390 (2022)*.
- Kihyuk Nam, Taewhi Lee, Sung-Soo Kim, Choon Seo Park, Taek Yong Nam, Insik Shin. "An Efficient Data Analysis For Edge-Enabled Distributed Environments using Tractable Probabilistic Models". *IEEE Big Data 2022: 6787-6789*.
- Byunggill Joe, Insik Shin, Jihun Hamm. "Online Evasion Attacks on Recurrent Models: The Power of Hallucinating the Future". *IJCAI 2022: 3121-3127*.
- Sunjae Lee, Hoyoung Kim, Sijung Kim, Sangwook Lee, Hyosu Kim, Jean Y. Song, Steven Y. Ko, Sangeun Oh, Insik Shin. "A-mash: providing single-app illusion for multi-app use through user-centric UI mashup". *MobiCom 2022: 690-702*.
- Ju Chen, Wookhyun Han, Mingjun Yin, Haochen Zeng, Chengyu Song, Byoungyoung Lee, Heng Yin, Insik Shin. "SYMSAN: Time and Space Efficient Concolic Execution via Dynamic Data-flow Analysis". *USENIX Security Symposium 2022: 2531-2548*.
- Jin Hyun Kim, Deepak Gangadharan, Kyong Hoon Kim, Insik Shin, Insup Lee. "Hierarchical Scheduling". *Handbook of Real-Time Computing 2022: 269-301*.
- Byunggill Joe, Insik Shin, Jihun Hamm. "Online Evasion Attacks on Recurrent Models: The Power of Hallucinating the Future". *CoRR abs/2207.09912 (2022) (arXiv 사전 공개본)*.

**2021**

- Taejune Park, Seungwon Shin, Insik Shin, Kilho Lee. "Formullar: An FPGA-based network testing tool for flexible and precise measurement of ultra-low latency networking systems". *Comput. Networks 185: 107689 (2021)*.
- Sunjae Lee, Hayeon Lee, Hoyoung Kim, Sangmin Lee, Jeong Woon Choi, Yuseung Lee, Seono Lee, Ahyeon Kim, Jean Y. Song, Sangeun Oh, Steven Y. Ko, Insik Shin. "FLUID-XP: flexible user interface distribution for cross-platform experience". *MobiCom 2021: 762-774*.
- Adil Ahmad, Juhee Kim, Jaebaek Seo, Insik Shin, Pedro Fonseca, Byoungyoung Lee. "CHANCEL: Efficient Multi-client Isolation Under Adversarial Programs". *NDSS 2021*.
- Woosung Kang, Kilho Lee, Jinkyu Lee, Insik Shin, Hoon Sung Chwa. "LaLaRAND: Flexible Layer-by-Layer CPU/GPU Scheduling for Real-Time DNN Tasks". *RTSS 2021: 329-341*.
- Hyunjoo Lee, Jiyeon Lee, Daejun Kim, Suman Jana, Insik Shin, Sooel Son. "AdCube: WebVR Ad Fraud and Practical Confinement of Third-Party Ads". *USENIX Security Symposium 2021: 2543-2560*.
- Byunggill Joe, Akshay Mehra, Insik Shin, Jihun Hamm. "Machine Learning with Electronic Health Records is vulnerable to Backdoor Trigger Attacks". *CoRR abs/2106.07925 (2021) (arXiv 사전 공개본)*.

## 연락과 위치

- 교수연구실: KAIST E3-1 4425호[^faculty][^lab]
- 전화: 042-350-3524[^lab]
[^lab]: KAIST 전산학부, 「사이버 물리 시스템 연구실」. <https://cs.kaist.ac.kr/research/labView?sn=71&menu=64> 2026-10-27 열람.
[^faculty]: KAIST 전산학부 교수 명단, 「신인식」 행. <https://cs.kaist.ac.kr/people/faculty> 2026-10-27 열람.
[^prof]: KAIST 전산학부, 「신인식」 교수 상세 소개. <https://cs.kaist.ac.kr/people/view?idx=15&kind=faculty&menu=160> 2026-10-27 열람.
[^dblp]: dblp, Insik Shin 저자 목록의 2021–2026년 구역. <https://dblp.org/pid/45/4154.html> 2026-10-27 열람. 연도·제목·저자·발표처는 이 목록 기준이다.
[^active]: VeriSafe Agent arXiv HTML 원문, 저자 소속과 Co-corresponding authors 표시 및 학회 DOI. <https://arxiv.org/html/2503.18492v2> 2026-10-27 열람.

[^p1]: J. Lee 외, I. Shin, MobiCom 2025, 817-831 (2025). <https://doi.org/10.1145/3680207.3765248> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2503.18492> 2026-10-27 열람.
[^p2]: S. Lee 외, I. Shin, MobiCom 2024, 1119-1133 (2024). <https://doi.org/10.1145/3636534.3690682> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0002-9128-2415,publication_year:2021-2026> 2026-10-27 열람.
[^p3]: S. Lee 외, I. Shin, CHI 2024, 848:1-848:16 (2024). <https://doi.org/10.1145/3613904.3641991> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0002-9128-2415,publication_year:2021-2026> 2026-10-27 열람.
[^p4]: J. Kwak, S. Oh, J. Lee, I. Shin, ICCAD 2025, 1-9 (2025). <https://doi.org/10.1109/ICCAD66269.2025.11240765> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0002-9128-2415,publication_year:2021-2026> 2026-10-27 열람.
[^p5]: J. Kwak 외, I. Shin, MobiSys 2023, 247-260 (2023). <https://doi.org/10.1145/3581791.3596843> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0002-9128-2415,publication_year:2021-2026> 2026-10-27 열람.
[^p6]: W. Kang 외, H. S. Chwa, RTSS 2021, 329-341 (2021). <https://doi.org/10.1109/RTSS52674.2021.00038> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0002-9128-2415,publication_year:2021-2026> 2026-10-27 열람.
[^p7]: S. Oh, I. Shin, K. Lee, IEEE Syst. J. 16, 2379-2390 (2022). <https://doi.org/10.1109/JSYST.2021.3120539> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0002-9128-2415,publication_year:2021-2026> 2026-10-27 열람.
[^p8]: D. R. Jeong 외, Y. Kwon, SOSP 2024, 229-248 (2024). <https://doi.org/10.1145/3694715.3695944> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0002-9128-2415,publication_year:2021-2026> 2026-10-27 열람.

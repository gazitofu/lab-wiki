# 보안 최적화 연구실 (Security Optimization Research Lab, SOR Lab)

**서울대학교 공과대학 전기·정보공학부 · 백윤흥 교수**

- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: 소프트웨어·시스템 보안[^p3][^system], 하드웨어 보안[^p4][^hardware], AI·기계학습 보안·프라이버시[^p5][^p6], 암호학[^p1][^p2][^privacy], AI 반도체·가속기[^p7][^p8][^aicomputing]
- 홈페이지: <https://sor.snu.ac.kr/>
- 근거와 출처: [근거 페이지](sor-sources.md)

> 암호화 계산과 암호 하드웨어, 프로그램·차량 시스템 보호, 인공지능 보안과 전용 가속기 설계를 연구하는 연구실이다.[^p1][^p2][^p3][^p4][^p5][^p7][^p8]

## 무엇을 연구하나

보안 최적화 연구실은 컴퓨터의 자료와 프로그램을 보호하는 방법을 연구한다. 프로그램의 실행 보호, 암호화된 자료의 계산, 인공지능에 대한 공격·방어와 전용 하드웨어(컴퓨터를 구성하는 물리적인 장치) 설계를 함께 다룬다.[^system][^p1][^p2][^p5][^p7]

암호화 계산에서는 완전동형암호(Fully Homomorphic Encryption, FHE: 암호를 풀지 않은 자료에 대해 덧셈·곱셈을 임의 횟수 조합해 계산할 수 있는 암호 기술)를 다룬다. 신경망(연결된 계산 단위가 입력을 변환하고 결합해 결과를 만드는 계산 모델)의 추론(학습된 모델로 새 입력의 결과를 계산하는 과정)을 암호화된 상태에서 수행하는 방법을 연구한다.[^p1][^privacy] 양자내성암호(양자컴퓨터를 이용한 공격에 견디도록 설계한 암호)의 디지털서명을 처리하는 전용 장치도 설계한다. 디지털서명은 비공개 정보로 만든 서명값을 공개 정보로 검사해 메시지의 작성 주체와 내용 변경 여부를 확인하는 암호 기술이다.[^p2]

프로그램 보호에서는 메모리(프로그램이 사용하는 정보를 저장하는 공간)의 접근 권한과 프로그램의 취약점을 다룬다. Rust라는 프로그래밍 언어의 안전한 코드와 신뢰하지 않는 코드를 함께 실행하면서 자료를 보호한다.[^p3] System Security 팀은 퍼징(fuzzing: 다양한 입력을 자동으로 만들거나 변형해 프로그램의 오류·취약점을 찾는 시험 기법), 정적 분석(프로그램을 실행하지 않고 코드의 성질을 분석하는 방법), 심볼릭 실행(입력을 변수로 놓고 실행 경로와 그 경로가 실행되는 조건을 분석하는 방법)을 결합한 취약점 탐색을 소개한다.[^system]

차량 연구는 외부와 연결된 시스템이 보내는 제어 메시지를 검증한다. 신뢰 실행 환경(Trusted Execution Environment, TEE: 지정된 코드와 자료를 다른 실행 영역에서 격리해 보호하는 환경)과 하드웨어 보안 모듈(Hardware Security Module, HSM: 암호 키와 암호 연산을 보호하는 하드웨어)을 이용한다. 암호 키는 암호화나 서명 같은 연산에 사용하는 값이다.[^p4]

인공지능 보안에서는 연합학습(Federated Learning, FL: 여러 참여자가 각자의 자료를 직접 공유하지 않고 계산 결과를 주고받으며 함께 모델을 학습하는 방식)을 공격에서 보호한다. 악성 참여자가 학습 결과를 바꾸는 공격과 특정 입력에서 공격자가 원하는 출력을 내게 하는 백도어 공격을 다룬다.[^p5][^p6]

인공지능 가속기(특정 종류의 인공지능 계산을 수행하도록 설계한 전용 계산 장치) 연구에서는 신경망 모델에 맞는 장치 구조와 자료 배치 방법을 설계한다. 설계 공간 탐색(Design Space Exploration, DSE: 여러 설계안을 평가해 목표 조건에 맞는 안을 고르는 과정)을 이용해 설계 요소를 비교하고 계산에 맞는 동작 방식을 선택한다.[^aicomputing][^p7][^p8]

## 주요 연구 주제

### 암호 계산과 암호 하드웨어

산술 연산은 덧셈·뺄셈·곱셈·나눗셈 같은 수 계산이며, 함수는 입력을 정해진 규칙에 따라 출력에 대응시키는 것이다. SLOTHE는 기본 산술 연산으로 직접 처리하지 않는 함수의 코드를 산술 부분과 비산술 부분으로 나누고 필요한 비산술 부분만 근사한다. 근사는 정확한 값이나 계산을 일정한 오차를 허용하는 값이나 계산으로 나타내는 것이다. 암호화된 신경망 계산에서 쓰는 다항식(상수와 변수의 곱을 유한 번 더해 나타낸 식)을 만드는 과정과 계산 지연·정확도의 관계를 다룬다.[^p1]

SPHINCSLET은 양자내성 디지털서명 방식인 SPHINCS+ 전체를 처리하는 하드웨어 구현이다. 보안 수준과 해시 함수(입력을 정해진 길이의 값으로 바꾸는 함수)에 맞춰 구성을 바꾸면서 장치가 차지하는 면적과 서명 처리 성능을 함께 고려한다.[^p2]

### 프로그램과 차량 시스템 보호

TRust는 같은 프로그램 안에서도 신뢰하지 않는 코드가 안전한 Rust 코드의 자료를 쓰지 못하도록 메모리 영역을 분리한다.[^p3] System Security 팀은 취약점 진단·분석과 함께, 하드웨어를 활용한 신뢰 기반 실행환경을 안전하게 만들고 산업·클라우드(네트워크로 연결된 원격 컴퓨터의 계산·저장 자원을 사용하는 방식) 환경에서 사용할 수 있게 하는 연구를 소개한다.[^system]

SECV는 차량 외부 연결을 담당하는 시스템이 공격받더라도 내부 통신망에서 제어 메시지를 검증하는 방법이다. 보호된 실행 환경에서 검증한 메시지에 암호학적 증명을 붙이고, 하드웨어 보안 모듈이 그 증명을 확인한다.[^p4]

### 인공지능에 대한 공격과 방어

VFLIP(Vertical Federated Learning via Identification and Purification)는 수직 연합학습(같은 대상에 관한 서로 다른 종류의 정보를 참여자들이 나누어 보유하는 연합학습)의 추론 단계에서 참여자별 이상을 찾는다. 악성 중간 계산 결과를 제거한 뒤 남은 결과로 재구성해 백도어 공격을 완화한다.[^p5] FLGuard는 대조학습(서로 관련 있는 입력과 관련 없는 입력의 계산 결과를 구별하도록 학습하는 방식)을 이용한 모델들을 함께 사용해 악성 참여자가 보낸 학습 갱신을 찾아 제외한다.[^p6]

### 인공지능 가속기 설계

희소 텐서 가속기 연구는 자료에 들어 있는 0을 이용해 불필요한 계산을 생략하는 장치를 다룬다. 텐서는 축을 따라 수를 배열해 나타낸 자료이며, 희소 텐서는 많은 원소가 0인 텐서다. 자료 표현 방식과 0이 아닌 값을 찾는 기능 등 설계 요소를 분류·모델링하고, 개발 초기의 설계 탐색에 사용할 기능 모음을 제공한다.[^p7]

자료 흐름을 바꾸는 가속기 연구는 여러 동작 모드를 장치에 구현하고 신경망의 층(계산 단위들을 묶어 입력을 변환하는 단계)마다 적합한 모드를 선택한다. 자료 흐름은 계산 장치에서 자료를 이동시키고 사용하는 순서와 배치다. 모드를 바꿀 때 드는 부담과 하드웨어 구성 요소의 재사용을 함께 고려한다.[^p8] AI Computing 팀은 이처럼 연산과 하드웨어 조건을 기술해 가속기 구조와 연산 배치를 탐색하는 연구를 소개한다.[^aicomputing]

## 대표 논문

암호 계산·암호 하드웨어, 프로그램·차량 보호, 인공지능 공격·방어, 인공지능 가속기 설계에서 두 편씩 골랐다. 여덟 편 모두 백윤흥 교수가 마지막 저자이며 2003년 서울대 부임 이후의 연구다. 4·5·6·8번은 누리집이 교신저자 역할을 명시한다.[^pi][^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8] ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 5·6번은 arXiv 공개판이며 해당 페이지의 ESORICS 채택 연도와 공개판 게시 연도를 구분했다.

| 번호 | 연도 | 논문 | 쉽게 말하면 | 교수 역할 |
|---|---|---|---|---|
| 1 | 2025 | [SLOTHE : Lazy Approximation of Non-Arithmetic Neural Network Functions over Encrypted Data](https://www.usenix.org/conference/usenixsecurity25/presentation/nam-slothe) · USENIX Security | 암호화된 자료의 신경망 계산에서 비산술 함수를 미리 하나의 다항식으로 바꾸는 대신, 계산을 나누고 필요한 비산술 부분만 근사한다. 정확도와 계산 지연을 조절하는 비용 모델을 제시했다.[^p1] | 마지막 저자 |
| 2 | 2025 | [SPHINCSLET: An Area-Efficient Accelerator for the Full SPHINCS+ Digital Signature Algorithm](https://doi.org/10.1145/3728469) · ACM Transactions on Embedded Computing Systems | 양자내성 디지털서명 SPHINCS+ 전체를 처리하는 하드웨어를 제시했다. 여러 보안 수준과 해시 함수에 맞게 구성을 조정하며, 장치 면적과 서명·검증 성능을 함께 고려한다.[^p2] | 마지막 저자 |
| 3 | 2023 | [TRust: A Compilation Framework for In-process Isolation to Protect Safe Rust against Untrusted Code](https://www.usenix.org/conference/usenixsecurity23/presentation/bang) · USENIX Security | 안전한 Rust 코드의 자료를 분리된 메모리 영역에 두고 신뢰하지 않는 코드의 쓰기를 막는다. 소스 코드를 사람이 직접 고치지 않고 적용하는 컴파일 틀을 제시했다. 컴파일은 소스 코드를 실행할 수 있는 형태로 바꾸는 과정이다.[^p3] | 마지막 저자 |
| 4 | 2026 | [SECV: Securing Connected Vehicles with Hardware Trust Anchors](https://www.ndss-symposium.org/ndss-paper/secv-securing-connected-vehicles-with-hardware-trust-anchors/) · NDSS | 차량 외부 연결을 담당하는 시스템이 공격받아도 내부 통신망이 제어 메시지를 검증하도록 한다. 보호된 실행 환경에서 메시지를 검증하고 암호학적 증명을 붙이면 하드웨어 보안 모듈이 확인한다.[^p4] | 마지막·공동 교신저자 |
| 5 | 2024 | [VFLIP: A Backdoor Defense for Vertical Federated Learning via Identification and Purification](https://arxiv.org/abs/2408.15591) · arXiv 공개판, ESORICS 2024 채택 표기 | 수직 연합학습의 추론 단계에서 참여자별 이상을 찾아 백도어가 작동한 중간 표현을 식별한다. 악성 표현을 제거하고 남은 표현으로 전체 표현을 재구성한다. 표현은 입력의 정보를 계산에 쓰는 값으로 나타낸 것이다.[^p5] | 마지막·공동 교신저자 |
| 6 | 2024 | [FLGuard: Byzantine-Robust Federated Learning via Ensemble of Contrastive Models](https://arxiv.org/abs/2403.02846) · arXiv 공개판, ESORICS 2023 채택 표기 | 연합학습 참여자 중 공격자가 보내는 악성 갱신을 찾아 제외한다. 대조학습 모델들을 함께 사용하는 방어 방식을 제시하고 다양한 학습 오염 공격에서 평가했다.[^p6] | 마지막·공동 교신저자 |
| 7 | 2023 | [Modeling and Library Support for Early-Stage Exploration of Sparse Tensor Accelerator Designs](https://doi.org/10.1109/access.2023.3278274) · IEEE Access | 희소 텐서 가속기에 쓰는 설계 요소를 분류하고 모델링하는 방법을 제시했다. 설계 요소를 기능 모음으로 제공해 개발 초기에 여러 가속기 설계를 평가할 수 있게 했다.[^p7] | 마지막 저자 |
| 8 | 2025 | [Towards an efficient dataflow-flexible accelerator by finding optimal dataflows of DNNs](https://doi.org/10.1016/j.future.2025.108123) · Future Generation Computer Systems | 여러 자료 흐름을 동작 모드로 구현하고 신경망 층마다 적합한 모드를 고르는 가속기를 제안했다. 설계 탐색으로 모드의 수와 종류를 정하고 모드 전환과 하드웨어 재사용을 최적화했다.[^p8] | 마지막·공동 교신저자 |

## 교수와 전문 분야

백윤흥 교수는 서울대학교 컴퓨터공학과에서 학사와 석사를 마치고 1997년 미국 일리노이대학교 어바나샴페인(UIUC) 전산학 박사학위를 받았다. 뉴저지 공과대학교 조교수와 KAIST 전자전산학과 조교수·부교수를 거쳐 2003년 3월 서울대학교에 부임했다. 학과 소개는 2007년 10월부터 정교수로 적는다.[^pi]

학과 교수 소개가 적은 전공은 시스템 보안, 시스템온칩(System-on-Chip, SoC: 컴퓨터 시스템의 여러 기능을 하나의 칩에 통합한 집적회로) 최적화, 컴파일러(소스 코드를 다른 실행 형태로 바꾸는 프로그램), 프로세서(명령을 해석하고 계산을 수행하는 장치) 설계다. 연구 관심은 소프트웨어·시스템 보안, 기기 보안을 위한 하드웨어, 지능형 보안과 인공지능 보안이다.[^pi]

누리집은 백윤흥 교수와 이병영 교수가 컴퓨터·네트워크 시스템 보안을 연구하는 그룹을 이끈다고 소개한다.[^intro][^professors] Privacy Enhancing Computing과 AI Computing 팀의 담당 교수는 백윤흥, System Security 팀의 교수는 백윤흥·이병영으로 표기한다.[^privacy][^aicomputing][^system]

## 응용 분야

입력 자료를 암호화 상태로 처리하는 인공지능 서비스,[^p1] 자원이 제한된 장치의 양자내성 디지털서명,[^p2] Rust 응용 프로그램의 자료 보호,[^p3] 외부 통신망과 연결되는 차량의 제어 메시지 보호[^p4]가 적용 대상이다. 여러 기관이 자료를 직접 합치지 않고 모델을 함께 학습할 때의 공격 방어와, 신경망 계산에 맞는 전용 장치 설계도 다룬다.[^p5][^p6][^p7][^p8]

## 구성원

2026년 10월 27일 Students 목록의 27명이다. 과정과 학력은 누리집 표기이며, 연구 주제 칸은 상세 글의 분류명이다.[^students][^studentdetails] ‘대표 논문 참여’는 위 표 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 | 학력 표기 |
|---|---|---|---|---|
| [Junseung You](https://sor.snu.ac.kr/post/513) | 석사과정 (ECE, SNU) | Software Security | 4 | B.S.(2019) from ECE, SNU. |
| [Martin Kayondo](https://sor.snu.ac.kr/post/561) | 석사과정 (ECE, SNU) | Software Security | 3, 4 | B.S.(2020) from ECE, SNU. |
| [Heon Hui Jung](https://sor.snu.ac.kr/post/628) | 석사과정 (ECE, SNU) | Hardware Security |  | B.S.(2022) from Electrical and Computer Engineering, University of Seoul. |
| [Youngmin Kim](https://sor.snu.ac.kr/post/643) |  | Software Security |  | B.S.(2021) from ECE, SNU.; M.S from ECE, SNU. |
| [YoungJoo Lee](https://sor.snu.ac.kr/post/645) |  | Software Security |  | B.S.(2021) in IS, NILE.; M.S from ECE, SNU. |
| [Jinmyung Choi](https://sor.snu.ac.kr/post/734) | 석사과정 (ECE, SNU) | Software Security |  | B.S. (2023) from Computer Software Engineering(CSE), Hanyang University. |
| [Kibong Kang](https://sor.snu.ac.kr/post/750) | 석사과정 (ECE, SNU) | Software Security |  | B.S (2023) from Electronic Engineering(EE), KyungHee University(KHU) |
| [YunSeong Hwang](https://sor.snu.ac.kr/post/751) | 석사과정 (ECE, SNU) | Software Security |  | B.S.(2024) from ECE, SNU. |
| [Younghan Choe](https://sor.snu.ac.kr/post/855) | 석사과정 (ECE, SNU) | Hardware Security |  | B.S.(2025) from BSE/ECE, SNU. |
| [Eunmin Kim](https://sor.snu.ac.kr/post/857) | 석사과정 (ECE, SNU) | Software Security | 4 | B.S.(2025) from Cyber Security, DKU. |
| [Yungi Cho](https://sor.snu.ac.kr/post/869) | 석사과정 (ECE, SNU) | AI Security | 5, 6 | B.S.(2020) from Cyber Security, Ajou University. |
| [Jiwan Seo](https://sor.snu.ac.kr/post/870) | 석사과정 (ECE, SNU) | Hardware Security |  | B.S.(2025) from EEE, CAU. |
| [Kyungwook Boo](https://sor.snu.ac.kr/post/872) | 석사과정 (ECE, SNU) | Software Security |  | B.S.(2014) from EE, KAIST. |
| [Seungjin Ha](https://sor.snu.ac.kr/post/874) | 석사과정 (ECE, SNU) | Hardware Security | 1 | B.S.(2023) from Computer Science and Engineering (CS), Ewha Womans University(EWU). |
| [Woorim Han](https://sor.snu.ac.kr/post/875) | 석사과정 (ECE, SNU) | AI Security | 5, 6 | B.S.(2021) from Computer & Electronic Engineering, HGU. |
| [Youyeon Joo](https://sor.snu.ac.kr/post/876) | 석사과정 (ECE, SNU) | AI Security | 1 | B.S.(2022) from Cyber Security, Ewha Womans University(EWU). |
| [Miseon Yu](https://sor.snu.ac.kr/post/877) | 석사과정 (ECE, SNU) | AI Security | 5 | B.S.(2020) from Electronic engineering (EE), Ewha Womans University(EWU). |
| [Dongju Lee](https://sor.snu.ac.kr/post/878) | 석사과정 (ECE, SNU) | AI Security | 8 | B.S.(2022) from Department of Mathematics, Chung-Ang University. |
| [Sungyeon Lee](https://sor.snu.ac.kr/post/879) | 석사과정 (ECE, SNU) | AI Security |  | B.S.(2025) from Department of Mathematical Sciences, SNU. |
| [Sangyun Kim](https://sor.snu.ac.kr/post/881) | 석사과정 (ECE, SNU) | Software Security |  | B.S.(2020) from ECE, SNU. |
| [Haeun Kim](https://sor.snu.ac.kr/post/882) | 석사과정 (ECE, SNU) | Software Security |  | B.S.(2025) from Cyber Security, EWU |
| [Hanbin Yeo](https://sor.snu.ac.kr/post/897) | 석사과정 (Department of Future Automotive Mobility (FAM), SNU) | Software Security |  | B.S. (2026) from Automobile and IT Convergence, KMU |
| [Hwichan Choo](https://sor.snu.ac.kr/post/898) | 석사과정 (Interdisciplinary Program in Information Security and Privacy, SNU) | AI Security |  | B.A. (2025) in Public Administration, KNPU |
| [Hobin Dong](https://sor.snu.ac.kr/post/899) | 석사과정 (ECE, SNU) | Software Security |  | B.S. (2014) in Computer and Communication Engineering, Korea University |
| [Jinhyeong Kim](https://sor.snu.ac.kr/post/911) | 석사과정 (ECE, SNU) | AI Security |  | B.S.(2024) from ECE, SNU. |
| [Siyeon Lee](https://sor.snu.ac.kr/post/912) | 석사과정 (ECE, SNU) | Software Security |  | B.S. (2026) from Electronic Engineering, HYU |
| [Ji Woo Park](https://sor.snu.ac.kr/post/913) | 석사과정 (Interdisciplinary Program in Information Security and Privacy, SNU) | AI Security |  | B.S. (2026) in Division of Smart Security, Korea University |

## 졸업생과 이전 구성원

누리집 Alumni 두 쪽에 게시된 80명이다. 이 명단에는 백윤흥 교수의 서울대 부임 전 학위 이력도 포함되어 있다. 학위·과정과 연도, 진로는 누리집 표기다. 졸업생 분류와 본문의 Student 표기가 함께 있는 경우 두 표기를 함께 적었다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| [Jeonghun Cho](https://sor.snu.ac.kr/post/395) | Ph.D. (2003) | Associate professor in EEC, KNU. |
| [Minwook Ahn](https://sor.snu.ac.kr/post/396) | Ph.D. (2009) | Post Doctor (2009) from EE, SNU.; SK Telecom. |
| [Doosan Cho](https://sor.snu.ac.kr/post/397) | Ph.D. (2009) | Assistant Professor at Sunchun National University |
| [Jonghee Youn](https://sor.snu.ac.kr/post/398) | Ph.D. (2011) | Assistant Professor at Yeungnam University |
| [Sanghyun Park](https://sor.snu.ac.kr/post/399) | Ph.D. (2011) | ARM. |
| [Jonghee Yoon](https://sor.snu.ac.kr/post/400) | Ph.D. (2012) | Samsung Electronics |
| [Yongjoo Kim](https://sor.snu.ac.kr/post/401) | Ph.D. (2012) | ETRI |
| [JongWon Lee](https://sor.snu.ac.kr/post/402) | Ph.D. (2014) | Samsung Electronics LSI |
| [SeungJun Yang](https://sor.snu.ac.kr/post/403) | Ph.D. | Samsung Electronics. |
| [YongIn Kwon](https://sor.snu.ac.kr/post/404) | Ph.D. | Samsung Electronics. |
| [Jinyong Lee](https://sor.snu.ac.kr/post/405) | Ph.D. (2016) | ETRI. |
| [Ingoo Heo](https://sor.snu.ac.kr/post/406) | Ph.D. (2016) | Samsung Electronics. |
| [Hyungon Moon](https://sor.snu.ac.kr/post/436) | Ph.D. (2017) | Assistant Professor at UNIST (Ulsan National Institute of Science and Technology) |
| [Yeongpil Cho](https://sor.snu.ac.kr/post/407) | Ph.D. (2018) | Assistant Professor at Hanyang University |
| [YongJe Lee](https://sor.snu.ac.kr/post/408) | Ph.D. (2018) | Samsung Electronics. |
| [Donghyun Kwon](https://sor.snu.ac.kr/post/474) | Ph.D. (2019) | Assistant Professor at Pusan National University |
| [Sungjoon Jung](https://sor.snu.ac.kr/post/409) | M.S. (2002) | Google, USA |
| [Se-Jong Oh](https://sor.snu.ac.kr/post/410) | M.S. (2002) | Microsoft, USA |
| [Jin-Hwan Kim](https://sor.snu.ac.kr/post/411) | M.S. (2002) |  |
| [Soon-Young Kwon](https://sor.snu.ac.kr/post/412) | M.S. (2003) | Korean Air pilot. |
| [So-Young Min](https://sor.snu.ac.kr/post/413) | M.S. (2003) |  |
| [Junsik Choi](https://sor.snu.ac.kr/post/414) | M.S. (2001) |  |
| [Taesong Kim](https://sor.snu.ac.kr/post/415) | M.S. (2005) | Research Engineer at SAIT. |
| [JooYeon Lee](https://sor.snu.ac.kr/post/416) | M.S. (2007) | Research Engineer at SAP. |
| [SeokKyo Jung](https://sor.snu.ac.kr/post/417) | M.S. (2007) | Research Engineer at Google |
| [WonSub Kim](https://sor.snu.ac.kr/post/418) | M.S. (2008) | SK Telecom |
| [Yongmo Liang](https://sor.snu.ac.kr/post/419) | M.S. (2008) | Research Engineer at SAMSUNG Electronics. |
| [HoKyun Kim](https://sor.snu.ac.kr/post/420) | M.S. (2009) |  |
| [YoungKyu Choi](https://sor.snu.ac.kr/post/421) | M.S. (2010) | Research Staff at LG Electronics |
| [DaeHo Kim](https://sor.snu.ac.kr/post/422) | M.S. (2009) | Research Engineer at Timax |
| [Zhiwen Zheng](https://sor.snu.ac.kr/post/423) | M.S. (2011) |  |
| [Yunrong Li](https://sor.snu.ac.kr/post/424) | M.S. |  |
| [Jihoon Lee](https://sor.snu.ac.kr/post/425) | M.S. (2013) | Samsung Electronics |
| [Oparin Mikhail](https://sor.snu.ac.kr/post/426) | M.S. (2013) |  |
| [SangJun Han](https://sor.snu.ac.kr/post/427) | M.S. (2015) |  |
| [Ali Almokhtar](https://sor.snu.ac.kr/post/428) | M.S. |  |
| [Xuan Jun Zheng](https://sor.snu.ac.kr/post/429) | M.S. |  |
| [Wonha Choi](https://sor.snu.ac.kr/post/430) | M.S. | Samsung Electronics. |
| [Wenquan Jin](https://sor.snu.ac.kr/post/431) | M.S. | AnaPass. |
| [Kyungmin Kim](https://sor.snu.ac.kr/post/432) | M.S. | AnaPass. |
| [Gisoo Seo](https://sor.snu.ac.kr/post/433) | M.S. | Samsung Electronics. |
| [Jaesung Park](https://sor.snu.ac.kr/post/434) | M.S. (2018) | LG Electronics. |
| [Sehyun Baek](https://sor.snu.ac.kr/post/475) | M.S. (2019) | Samsung Electronics |
| [Myonghoon Yang](https://sor.snu.ac.kr/post/477) | M.S. (2019) | Samsung Electronics |
| [Junmo Park](https://sor.snu.ac.kr/post/478) | M.S. (2019) |  |
| [Hayoon Yi](https://sor.snu.ac.kr/post/527) | Ph.D. Graduates (본문: Ph.D. Student of EE, SNU.) | Samsung Research |
| [Jangseop Shin](https://sor.snu.ac.kr/post/534) | Ph.D. Graduates (본문: Ph.D. Student of EE, SNU.) | Samsung Research |
| [Seongil Jeon](https://sor.snu.ac.kr/post/535) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) |  |
| [Giyeol Kim](https://sor.snu.ac.kr/post/536) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) | Naver Labs |
| [Chigon Jung](https://sor.snu.ac.kr/post/537) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) |  |
| [Jiwon Chang](https://sor.snu.ac.kr/post/619) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) |  |
| [Yohan Kim](https://sor.snu.ac.kr/post/620) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) |  |
| [Dongil Hwang](https://sor.snu.ac.kr/post/622) | Ph.D. Graduates (본문: Ph.D. Student of ECE, SNU.) | Samsung Electronics |
| [Sohee Jun](https://sor.snu.ac.kr/post/646) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) | NAVER |
| [Myunghyun Cho](https://sor.snu.ac.kr/post/647) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) |  |
| [Hyunyoung Oh](https://sor.snu.ac.kr/post/648) | Ph.D. Graduates (본문: Ph.D. Student of ECE, SNU.) | Assistant Professor at Gachon University |
| [Seonghyun Park](https://sor.snu.ac.kr/post/650?page=2) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) |  |
| [Sunwoo Kim](https://sor.snu.ac.kr/post/651?page=2) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) |  |
| [Jeehwan Kim](https://sor.snu.ac.kr/post/666?page=2) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) | Samsung Electronics. |
| [Kyeongryong Lee](https://sor.snu.ac.kr/post/673?page=2) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) |  |
| [Seonggwan Ahn](https://sor.snu.ac.kr/post/674?page=2) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) |  |
| [Jiwon Seo](https://sor.snu.ac.kr/post/675?page=2) | Ph.D. Graduates (본문: Ph.D. Student of ECE, SNU.) | Assistant Professor at Dankook University |
| [Sunwoo Ahn](https://sor.snu.ac.kr/post/676?page=2) | Ph.D. Graduates (본문: Ph.D. Student of ECE, SNU.) | Samsung Electronics |
| [Inyoung Bang](https://sor.snu.ac.kr/post/742?page=2) | Ph.D. Graduates (본문: PH.D. Student of ECE, SNU.) | SK hynix |
| [Sebastian Soler Castaneda](https://sor.snu.ac.kr/post/743?page=2) | M.S. Graduates (본문: M.S Student of ECE, SNU.) |  |
| [Cansu Karakuzu](https://sor.snu.ac.kr/post/744?page=2) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) |  |
| [Younghan Lee](https://sor.snu.ac.kr/post/841?page=2) | Ph.D. | Assistant Professor at Sungshin Women's University |
| [Yongseok Lee](https://sor.snu.ac.kr/post/859?page=2) | Ph.D. Graduates (본문: Ph.D. Student of ECE, SNU.) | Samsung Advanced Institute of Technology (SAIT) |
| [Bastien Schoonaert](https://sor.snu.ac.kr/post/860?page=2) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) |  |
| [Subin Yun](https://sor.snu.ac.kr/post/861?page=2) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) |  |
| [Juhee Kim](https://sor.snu.ac.kr/post/862?page=2) | Ph.D. Graduates (본문: PH.D. Student of ECE, SNU.) |  |
| [Jaewon Hur](https://sor.snu.ac.kr/post/863?page=2) | Ph.D. Graduates (본문: PH.D. Student of ECE, SNU.) |  |
| [Hyunjun Kim](https://sor.snu.ac.kr/post/900?page=2) | Ph.D. (2025) | Assistant Professor at Myongji University |
| [Kevin Nam](https://sor.snu.ac.kr/post/901?page=2) | Ph.D. (2026) | Assistant Professor at Kyung Hee University |
| [Whoiree Ha](https://sor.snu.ac.kr/post/902?page=2) | Ph.D. (2026) |  |
| [Yunji Lee](https://sor.snu.ac.kr/post/903?page=2) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) |  |
| [Cheolwoo Myung](https://sor.snu.ac.kr/post/904?page=2) | Ph.D. Graduates (본문: Ph.D. Student of ECE, SNU.) |  |
| [Yoochan Lee](https://sor.snu.ac.kr/post/905?page=2) | Ph.D. Graduates (본문: Ph.D. Student of ECE, SNU.) |  |
| [Suhwan Song](https://sor.snu.ac.kr/post/906?page=2) | Ph.D. Graduates (본문: Ph.D. Student of ECE, SNU.) |  |
| [Jinhan Kwak](https://sor.snu.ac.kr/post/907?page=2) | M.S. Graduates (본문: M.S. Student of ECE, SNU.) |  |

## 최근 논문 목록 (2021–2026)

누리집에 게시된 국제 논문 40편과 국내 논문 79편, 모두 119편이다. 연도는 누리집 서지에 적힌 학회·학술지 연도이며 SECV는 상세 본문과 학회 자료의 2026년을 따른다. 국내 목록에는 학술지 글과 학회 발표가 함께 있다.[^pubs][^domesticpubs][^p4]

누리집의 conditional accept·to appear·early access 표시는 해당 항목에 남겼다. 대표 논문 설명에 사용한 arXiv 공개판의 게시 연도와 아래 학회 논문의 연도는 다를 수 있다. 저자 뒤의 기호는 누리집 표시다.[^pubs][^p5][^p6]

**2026**

- Whoi Ree Ha∗ , Dongju Lee∗ , Yongseok Lee , Kevin Nam , Sunwoong Kim† and Yunheung Paek†. "Design Space Exploration of Efficient FPGA-based Accelerators for Homomorphically Encrypted CNN Inference". *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems(TCAD), Oct 2026*.
- Dongju Lee, Sungyeon Lee, Youyeon Joo, Kevin Nam\*, Yunheung Paek\*. "PCPSI: Efficient Unbalanced Private Set Intersection Using Homomorphic Encryption with Plaintext–Ciphertext Multiplication". *IEEE Access, May 2026*.
- Yungi Cho, Miseon Yu, Jaejin Kim, Younghan Lee, Yunheung Paek. "PI-FD: Property Inference Attacks on Federated Learning with Distillation via Synthetic Data Generation". *IEEE Access, May 2026*.
- Kevin Nam, Youyeon Joo, Seungjin Ha, Hyungon Moon\*, Yunheung Paek\*. "HEPIC: Private Inference over Homomorphic Encryption with Client Intervention". *ASPLOS 2026*.
- Martin Kayondo, Junseung You, Eunmin Kim, Jiwon Seo\* and Yunheung Paek\*. "SECV: Securing Connected Vehicles with Hardware Trust Anchors". *Network and Distributed System Security Symposium (NDSS), 2026*.
- Woorim Han, Yeongjun Kwak, Miseon Yu, Kyeongmin Kim, Younghan Lee\*, Hyungon Moon, Yunheung Paek\*. "Rethinking the Capability of Fine-Tuned Language Models for Automated Vulnerability Repair". *ICSE 2026*.

**2025**

- Hyunjun Kim\*, Whoi Ree Ha\*, Yongseok Lee, Dongju Lee, Jongwon Lee, Deumji Woo, Jonghee Yoon, Jemin Lee, Yongin Kwon†, Yunheung Paek†. "Towards an Efficient Dataflow-flexible Accelerator by Finding Optimal Dataflows of DNNs". *Future Generation Computer Systems, Sep 2025*.
- Heonhui Jung \*, Whoiree Ha \*, Kevin Nam, Youyeon Joo, Lucas Oros, Yunheung Paek. "An Accelerator for Low-computational Overhead Privacy-Preserving GNN Inference". *HiPC 2025*.
- Kevin Nam\*, Youyeon Joo\*, Seungjin Ha, Yunheung Paek. "SLOTHE: Lazy Approximation of Non-Arithmetic Neural Network Functions over Encrypted Data". *USENIX Security 2025*.
- Junseung You, Jiwon Seo, Kyeongryong Lee, Yeongpil Cho\*, Yunheung Paek\*. "BASTAG: Byte-level Access Control on Shared Memory using ARM Memory Tagging Extension". *ACM CCS 2025*.
- Sanjay Deshpande, Yongseok Lee, Cansu Karakuzu, Jakub Szefer, Yunheung Paek. "SPHINCSLET:An Area-efficient Accelerator for the Full SPHINCS+ Digital Signature Algorithm". *ACM Transactions on Embedded Computing Systems, Mar 2025*.
- Kevin Nam, Heonhui Jung, Hyunyoung Oh\*, Yunheung Paek\*. "Affinity-based Optimizations for TFHE on Processing-in-DRAM". *The ACM International Conference on Architectural Support for Programming Languages and Operating Systems, 2025 (ASPLOS 2025)*.
- Kevin Nam, Youyeon Joo, Dongju Lee, Seungjin Ha, Hyunyoung Oh, Hyungon Moon\*, and Yunheung Paek\*. "LOHEN: Layer-wise Optimizations for Neural Network Inferences over Encrypted Data with high Performance or Accuracy". *USENIX Security 2025*.

**2024**

- Jiwon Seo, Kayondo Martin, Jeonghwan Kang, Donghyun Kwon†, Yunheung Paek†. "ROSEC: Intra-Process Isolation for ROS Composition with Memory Protection Keys". *IEEE Transactions on Automation Science and Engineering , Dec 2024*.
- Yungi Cho, Woorim Han, Miseon Yu, Younghan Lee, Ho Bae\* and Yunheung Paek\*. "VFLIP: A Backdoor Defense for Vertical Federated Learning via Identification and Purification". *ESORICS 2024*.
- Sanjay Deshpande, Yongseok Lee, Cansu Karakuzu, Jakub Szefer\*, Yunheung Paek\*. "SPHINCSLET - A Lightweight Implementation of SPHINCS+". *DAC WIP 2024*.
- Kevin Nam, Heonhui Jung, Hyunyoung Oh\*, Yunheung Paek\*. "Affinity-based Optimizations of Homomorphic Encryption Operations on Processing-in-DRAM". *DAC WIP 2024*.
- Yongseok Lee\*, Jonghee Youn\*, Kevin Nam, Heon Hui Jung, Myunghyun Cho Jimyung Na, Jong-Yeon Park, Seungsu Jeon, Bo Gyeong Kang, Hyunyoung Oh† and Yunheung Paek†. "An Efficient Hardware/Software Co-design for FALCON on Low-End Embedded Systems". *IEEE Access, April 2024*.
- Martin Kayondo, Inyoung Bang, Yeongjun Kwak, Hyungon Moon, and Yunheung Paek. "MetaSafe: Compiling for Protecting Smart Pointer Metadata to Ensure Safe Rust Integrity". *USENIX Security 2024*.
- Martin Kayondo, Jinmyung Choi, Eunmin Kim, Jiwon Seo, Yunheung Paek. "A Study on Hardware Trust Anchors for Securing Modern Automotive Systems". *AIComps 2024*.
- Woorim Han, Miseon Yu, Hyungon Moon, Younghan Lee, Yunheung Paek. "Learning-based Automated Vulnerability Repair: A Case Study on using Fine-tuned Language Models". *AIComps 2024*.
- Youyeon Joo, Hyunyoung Oh, Yunheung Paek. "Rotation Keyset Generation Strategy for Efficient Neural Networks using Homomorphic Encryption". *AIComps 2024*.
- Analyzing HTA-Based Security for Automotive Systems, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 마틴, 최진명, 백윤흥
- 스케줄링을 통한 동형암호 딥러닝 모델 가속, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 하회리, 이동주, 백윤흥
- Leveraging Reinforcement Learning for LLM-based Automated Software Vulnerability Repair, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 한우림, 유미선, 백윤흥
- Challenges and Future Directions for Large Language Models in Source Code Vulnerability Detection, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 윤수빈, 김현준, 백윤흥
- 자동화된 피드백을 통한 코드 생성 LLM 성능 향상 전략, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 유미선, 백윤흥
- 동형암호를 적용한 보안 제어 기술 동향 분석, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 이윤지, 백윤흥
- A Study on Securing Rust in Mixed-Language Applications, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 유준승, 마틴, 백윤흥
- RISC-V 코어의 보안 기능 구현을 위한 Dhrystone 기반 연산 성능 분석, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 강기봉, 황윤성, 유준승, 백윤흥
- 하드웨어를 이용한 자동차 보호 기법 연구, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 최진명, 마틴, 백윤흥
- A Study on Binary Code Similarity Detection, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 바스티안, 김현준, 백윤흥
- TFHE 가속화를 위한 CUDA 최적화 기법 비교 연구, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 하승진, 남기빈, 백윤흥
- 파인튜닝을 사용한 대형 언어 모델 기반 취약점 탐지 시스템에 대한 연구, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 김현준, 윤수빈, 백윤흥
- Secure Computing 을 위한 동형암호 가속기 연구에 대한 조망, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 정헌희, 남기빈, 이동주, 백윤흥
- 암호문 부채널 공격 및 대응 방안에 관한 연구, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 황윤성, 유준승, 강기봉, 백윤흥
- RIP: Robust Collaborative Inference via Participant-wise Anomaly Detection, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 조윤기, 한우림, 유미선, 백윤흥
- 빠르고 정확한 암호화된 신경망 연산을 위한 중간데이터을 활용한 근사식 생성 기술, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 남기빈, 주유연, 하승진, 백윤흥
- 클라우드 서버를 활용한 가블드 회로 위탁 연산에 대한 연구, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 이동주, 남기빈, 주유연, 백윤흥
- 효과적인 하드웨어 설계를 위한 격자기반 양자내성암호 통합 모듈 가속 기법 연구, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 이용석, 백윤흥
- 신뢰실행환경 기반 프록시 암호화를 활용한 동형암호 기반 클라우드 서비스의 성능 개선 연구, 2024 한국정보처리학회 추계학술대회 (ACK 2024), 주유연, 남기빈, 하승진, 백윤흥
- A Study on Code Vulnerability Repair via Large Language Models, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 한우림, 유미선, 백윤흥
- ARM 기밀 컴퓨팅 아키텍처에서의 안전하고 효율적인 메모리 공유, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 유준승, 백윤흥
- Assessing The Landscape: A Survey on Foreign Function Interface Isolation in Rust, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 마틴, 유준승, 최진명, 백윤흥
- RISC-V 프로세서에 대한 전력 분석 완화 기법 연구, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 강기봉, 백윤흥
- A Study on Defense Technique Against Use-After-Free Attacks Using MTE, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 황윤성, 유준승, 백윤흥
- A Survey on Privacy Vulnerabilities through Logit Inversion in Distillation-based Federated Learning, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 윤수빈, 조윤기, 백윤흥
- HLS를 활용한 FPGA기반의 FALCON 알고리즘 서명 생성 하드웨어 가속 연구, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 이용석, 이윤지, 백윤흥
- 코드 기반 양자 내성 암호 MEDS 알고리즘의 하드웨어 가속을 위한 부채널 공격 연구 동향 분석, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 이윤지, 이용석, 백윤흥
- Integrating Directed-Based Fuzzing with AFL++ in QEMU Mode, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 최진명, 김현준, 마틴, 백윤흥
- 협업 퍼징 기법에 대한 연구, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 김현준, 최진명, 백윤흥
- 배타적 프라이버시 보호기술을 활용한 효율적인 동형암호 연산 기술, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 이동주, 백윤흥
- 엣지 디바이스를 위한 AI 가속기 설계 방법, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 하회리, 김현준, 백윤흥
- TFHE 파라미터의 최적화에 대한 연구, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 하승진, 주유연, 남기빈, 백윤흥
- 코드 생성 언어 모델의 코드 보안성 향상을 위한 프롬프트 튜닝, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 유미선, 한우림, 조윤기, 백윤흥
- 효율적인 프라이버시 보존형 순환신경망을 위한 활성화함수의 cell-wise 근사, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 주유연, 남기빈, 하승진, 백윤흥
- 지식 증류 기반 연합학습에서의 강건성 평가, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 조윤기, 한우림, 유미선, 윤수빈, 백윤흥
- TFHE 기반 CNN 연산 최적화를 위한 비산술연산의 양자화 기술 연구, 2024 한국정보처리학회 춘계학술대회 (ASK 2024), 남기빈, 정헌희, 이동주, 백윤흥

**2023**

- Inyoung Bang, Martin Kayondo, Junseung You, Donghyun Kwon, Yeongpil Cho\*, Yunheung Paek\*. "Enhancing a Lock-and-Key Scheme With MTE to Mitigate Use-After-Frees". *IEEE Access, Dec 2023*.
- Yongseok Lee, Jonghee Youn, Kevin Nam, Hyunyoung Oh, Yunheung Paek. "Optimizing Hardware Resource Utilization for Accelerating the NTRU-KEM Algorithm". *Computers, 2023*.
- Junseung You, Kyeongryong Lee, Yeongpil Cho, Hyungon Moon\*, Yunheung Paek\*. "KVSEV: Secure In-Memory Key-Value Store on AMD Secure Encrypted Virtualization". *SoCC 2023*.
- Younghan Lee, Yungi Cho, Woorim Han, Ho Bae\* and Yunheung Paek\*. "FLGuard: Byzantine-Robust Federated Learning via Ensemble of Contrastive Models". *ESORICS 2023*.
- Jiwon Seo\*, Junseung You\*, Donghyun Kwon, Yeongpil Cho†, Yunheung Paek†. "ZOMETAG: Zone-based Memory Tagging for Fast, Deterministic Detection of Spatial Memory Violations on ARM". *IEEE Transactions on Information Forensics and Security, Jul 2023*.
- Yongseok Lee, Kevin Nam, Youyeon Joo, Jeehwan Kim, Hyunyoung Oh, Yunheung Paek. "Area-Efficient Accelerator for the Full NTRU-KEM Algorithm". *ICCSA 2023*.
- Hyunjun Kim \*, Yungi Cho \*, Younghan Lee, Ho Bae †, Yunheung Paek †. "Exploring Clustered Federated Learning’s Vulnerability against Property Inference Attack". *RAID 2023*.
- Whoi Ree Ha, Hyunjun Kim, Yunheung Paek. "Modeling and Library Support for Early-stage Exploration of Sparse Tensor Accelerator Designs". *IEEE Access, May 2023*.
- Jiwon Seo, Junseung You, Yungi Cho, Yeongpil Cho, Donghyun Kwon, Yunheung Paek. "SFITAG: Efficient Software Fault Isolation with Memory Tagging for ARM Kernel Extensions". *ASIACCS 2023*.
- Inyoung Bang, Malittini Kayondo, Hyungon Moon, Yunheung Paek. "TRUST: A compilation framework for in-process isolation to protect safe rust against untrusted code". *USENIX Security 2023*.
- 동형암호 가속 하드웨어 개발 기술 동향 분석, 정보처리학회지 2023년 10월, 남기빈, 정헌희, 백윤흥
- 로우해머 공격 방어 기법에 관한 연구, 2023 한국정보처리학회 춘계학술대회, 하승진, 백윤흥
- 수직 연합학습에서의 백도어 공격 연구, 2023 한국정보처리학회 춘계학술대회, 조윤기, 김현준, 한우림, 백윤흥
- A Survey on Threats to Federated Learning, 2023 한국정보처리학회 춘계학술대회, 한우림, 조윤기, 백윤흥
- 동형암호에 대한 부채널 공격과 대응에 관한 연구, 2023 한국정보처리학회 춘계학술대회, 남기빈, 주유연, 하승진, 백윤흥
- ViT 기반 모델 역전 공격 및 방어 기법들에 대한 연구, 2023 한국정보처리학회 춘계학술대회, 유미선, 백윤흥
- 공유 메모리에의 최소 특권의 원칙 적용 기법에 대한 연구, 2023 한국정보처리학회 춘계학술대회, 유준승, 방인영, 백윤흥
- 인공지능 가속기 데이터 흐름 다양성에 대한 연구, 2023 한국정보처리학회 춘계학술대회, 이동주, 백윤흥
- 연합학습 모델에 대한 특성 추론 공격 및 방어 기법에 대한 연구, 2023 한국정보처리학회 춘계학술대회, 김현준, 조윤기, 백윤흥
- Sparse Tensor 가속기의 모델링에 관한 연구 동향, 2023 한국정보처리학회 춘계학술대회, 하회리, 백윤흥
- PQC SPHINCS+ 전자 서명 알고리즘의 효과적인 하드웨어 설계에 관한 연구, 2023 한국정보처리학회 춘계학술대회, 이용석, 잔수, 백윤흥
- 동형암호를 적용한 CNN 추론을 위한 ReLU 함수 근사에 대한 연구, 2023 한국정보처리학회 춘계학술대회, 주유연, 남기빈, 이동주, 백윤흥

**2022**

- Sunwoo Ahn ,Seonggwan Ahn, Hyungjoon Koo, Yunheung Paek. "Practical Binary Code Similarity Detection with BERT-based Transferable Similarity Learning". *ACSAC 2022*.
- Kevin Nam, Hyunyoung Oh, Hyungon Moon, Yunheung Paek. "Accelerating N-bit Operations over TFHE on Commodity CPU-FPGA". *ICCAD 2022*.
- Jiwon Seo, Inyoung Bang, Yungi Cho, Jangseop Shin, Dongil Hwang, Donghyun Kwon, Yeongpill Cho, Yunheung Paek. "Exploring Effective Uses of the Tagged Memory for Reducing Bounds Checking Overheads (early access)". *The Journal of Supercomputing, July 2022*.
- Younghan Lee, Sohee Jun, Yungi Cho, Woorim Han, Hyungon Moon∗, Yunheung Paek∗. "Precise Extraction of Deep Learning Models via Side-Channel Attacks on Edge/Endpoint Devices". *ESORICS 2022*.
- Sunwoo Ahn, Hayoon Yi, Ho Bae, Sungroh Yoon, Yunheung Paek. "A Data Embedding Scheme for Efficient Program Behavior Modeling with Neural Networks (early access)". *IEEE Transactions on Emerging Topics in Computational Intelligence, May 2022*.
- 임베디드 시스템을 위한 양자후암호화 FALCON 알고리즘의 FFT 연산 가속 연구, 2022 한국통신학회 동계종합학술발표회, 이용석, 남기빈, 주유연, 백윤흥
- Performance Analysis of SPHINCS+ for Post-Quantum Cryptography, 2022 한국정보보호학회 동계학술대회, 잔수, 세바스찬, 이용석, 백윤흥
- 비잔틴-강건한 연합학습에 대한 동향, 2022 한국정보보호학회 동계학술대회, 한우림, 이영한, 조윤기, 백윤흥
- AMD Secure Encrypted Virtualization 기반 신뢰실행환경의 취약점과 방어기법에 대한 연구, 2022 한국정보보호학회 동계학술대회, 유준승, 서지원, 방인영, 백윤흥
- 모델 역전 공격 및 방어 기법들에 대한 연구, 2022 한국정보보호학회 동계학술대회, 유미선, 이영한, 한우림, 백윤흥
- Memory wall 을 극복하기 위한 PIM 가속 기술에 대한 조망, 2022 한국정보처리학회 추계학술대회, 정헌희, 백윤흥
- 신뢰실행환경을 활용한 딥러닝 추론에 관한 연구, 2022 한국정보처리학회 추계학술대회, 주유연, 백윤흥
- AI 가속기 설계영역 탐색에 대한 연구, 2022 한국정보처리학회 추계학술대회, 이동주, 백윤흥
- 연합학습의 비잔틴 강건성 연구 동향 분석, 2022 한국정보보호학회 하계학술대회, 조윤기, 한우림, 백윤흥
- A Study on Transient Execution Attacks on WebAssembly, 2022 한국정보보호학회 하계학술대회, 마틴, 서지원, 백윤흥
- 맬웨어 탐지를 위한 Computation Efficient CNN 모델의 하드웨어 가속기에 관한 연구 동향, 2022 한국정보보호학회 하계학술대회, 하회리, 김현준, 이동주, 백윤흥
- A STUDY OF USING CKKS HOMOMORPHIC ENCRYPTION OVER THE LAYERS OF A CONVOLUTIONAL NEURAL NETWORK MODEL, 2022 한국정보처리학회 춘계학술대회, 세바스찬, 남기빈, 주유연, 백윤흥
- 딥러닝 기반 취약점 탐색 기술에 대한 조망, 2022 한국정보처리학회 춘계학술대회, 김현준, 안선우, 안성관, 백윤흥

**2021**

- Donghyun Kwon , Dongil Hwang,and Yunheung Paek. "A Hardware Platform for Ensuring OS Kernel Integrity on RISC-V". *MDPI Electronics, August 2021*.
- Hyunjun Kim, Sunwoo Ahn, Whoi Ree Ha, Hyunjae Kang, Dong Seong Kim , Huy Kang Kim, Yunheung Paek. "Panop: Mimicry-Resistant ANN-based Distributed NIDS for IoT Networks". *IEEE Access, July 2021*.
- Ho Bae † , Younghan Lee † , Yohan Kim, Uiwon Whang, Sungroh Yoon \* , and Yunheung Peak \*. "Learn2Evade: Learning-based Generative Model for Evading PDF Malware Classifiers". *IEEE Transactions on Artificial Intelligence, July 2021*.
- Dongil Hwang, Sanzhar Yeleuov, Jiwon Seo, Minu Chung, Hyungon Moon, and Yunheung Paek. "Ambassy: A Runtime Framework to Delegate Trusted Applications in an ARM/FPGA Hybrid System (early access)". *IEEE Transactions on Mobile Computing (TMC), Jun 2021*.
- Hyunyoung Oh, Kevin Nam, Seongil Jeon, Yeongpil Cho, Yunheung Paek. "MeetGo: A Trusted Execution Environment for Remote Applications on FPGA (early access)". *IEEE Access, Mar 2021*.
- Hyunyoung Oh, Yeongpil Cho, Yunheung Paek. "A Metadata-driven Approach to Efficiently Detect Code Reuse Attacks on ARM Multiprocessors". *The Journal of Supercomputing, Jan 2021*.
- Analysis on AMD Secure Encrypted Virtualization Vulnerabilities and Attack Mitigations, 2021 CUTE, 유준승, 방인영, 백윤흥
- Why Rust Is the Future Of the Cloud, 2021 CUTE, 방인영, 마틴, 유준승, 백윤흥
- 스트립 바이너리에서 저자 식별에 관한 연구, 2021 한국정보처리학회 추계학술대회, 안성관, 안선우, 김현준, 하회리, 백윤흥
- 프라이버시 보존 머신러닝의 연구 동향, 2021 한국정보처리학회 추계학술대회, 한우림, 이영한, 전소희, 조윤기, 백윤흥
- NTRU PQC 알고리즘 가속을 위한 성능 분석, 2021 한국정보처리학회 추계학술대회, 김지환, 조명현, 이용석, 백윤흥
- 동형암호를 위한 FPGA 기반의 하드웨어 가속기에 관한 연구 동향, 2021 한국정보처리학회 추계학술대회, 이용석, 백윤흥
- A Study on Protecting Privacy of Machine Learning Models, 2021 한국정보처리학회 추계학술대회, 이영한, 한우림, 조윤기, 김현준, 백윤흥
- 대리자를 통한 원격증명 검증 및 보안 연결 성립 방법, 2021 한국정보처리학회 추계학술대회, 이경룡, 조영필, 유준승, 백윤흥
- 동형암호를 활용한 딥러닝 모델 학습에 대한 연구, 2021 한국정보처리학회 춘계학술대회, 남기빈, 조명현, 김현준, 백윤흥
- Rust 언어의 FFI로 인한 취약에 대한 연구, 2021 한국정보처리학회 춘계학술대회, 마틴, 방인영, 유준승, 서지원, 백윤흥
- AI 모델 탈취 공격 및 방어 기법들에 관한 연구, 2021 한국정보처리학회 춘계학술대회, 전소희, 이영한, 김현준, 백윤흥
- 멀티 모달 침입 탐지 시스템에 관한 연구, 2021 한국정보처리학회 춘계학술대회, 하회리, 안선우, 조명현, 안성관, 백윤흥
- 쿼리를 사용하지 않는 딥러닝 모델 탈취 공격 연구, 2021 한국정보처리학회 춘계학술대회, 조윤기, 이영한, 전소희, 백윤흥
- 머신 러닝 기반 코드 작성자 식별 기술에 대한 조망, 2021 한국정보처리학회 춘계학술대회, 김현준, 안선우, 안성관, 남기빈, 백윤흥
- 효율적인 프로그램 행위 모델링을 위한 데이터 임베딩 연구, 2021 한국정보처리학회 춘계학술대회, 안선우, 김현준, 하회리, 안성관, 백윤흥

## 특허

출원 또는 등록 월이 2021-10-22–2026-10-22 안에 있는 국외 네 개와 국내 열한 개, 모두 열다섯 개의 게시항목이다. 날짜는 목록에 적힌 출원·등록 월이며 일자는 게시되어 있지 않다. 같은 제목의 국가별 출원과 출원·등록 행을 각각 포함한 게시항목 수다.[^patents]

- 2024-07 · CRYPTOGRAPHY PROCESSOR AND METHOD OF OPERATING THE SAME, Taiwan, 출원 (국외)
- 2024-06 · CRYPTOGRAPHY PROCESSOR AND METHOD OF OPERATING THE SAME, America, 출원 (국외)
- 2024-03 · BINARY CODE SIMILARITY DETECTION DEVICE AND METHOD, America, 출원 (국외)
- 2023-07 · APPARATUS FOR AND METHOD OF DETECTING CODE REUSE ATTACK (CRA), Singapore, 등록 (국외)
- 2025-01 · 동형 암호문 처리 방법 및 전자 장치, 출원 (국내)
- 2024-11 · 다종 동형암호 체계를 활용한 암호화 데이터 연산 방법 및 장치, 출원 (국내)
- 2024-02 · 신뢰 기관을 이용한 동형암호 공통키 배포, 출원 (국내)
- 2023-11 · 암호화 프로세서 및 암호화 프로세서의 동작 방법, 출원 (국내)
- 2023-11 · IoT 시스템의 비정상행위 탐지 방법 및 그 장치, 등록 (국내)
- 2023-09 · 연합학습에서의 개인 정보 유출 측정 프레임워크 및 그 동작 방법, 출원 (국내)
- 2023-03 · 바이너리 코드의 유사도 탐지 장치 및 방법, 출원 (국내)
- 2022-07 · 민감데이터를 보호하기 위한 소스 코드 변환 디바이스 및 그 동작 방법, 등록 (국내)
- 2022-01 · 악성 코드 실행 여부를 판단하는 전자 장치 및 그 제어 방법, 등록 (국내)
- 2021-12 · IoT 시스템의 비정상행위 탐지 방법 및 그 장치, 출원 (국내)
- 2021-12 · 클라우드 데이터에 대한 암호화키의 보안성 보장기술, 출원 (국내)

## 최근 선정 소식

선정 연도와 사업 기간은 누리집 표기다.[^news]

- 2023 · 한국연구재단 중견연구 과제 선정, 누리집 표기 사업 기간 2023–2028

## 연락과 위치

- 교수 연구실: 서울대학교 302동 631호[^pi][^ypaek]
- 교수 전화: 02-880-1748[^pi][^ypaek]
- 연구실 전화: 02-880-1742[^lab][^ypaek]
- 주소: 서울특별시 관악구 관악로 1 서울대학교[^home]
[^home]: SOR Lab 첫 화면 바닥글. <https://sor.snu.ac.kr/> (열람 2026-10-27).
[^lab]: 서울대학교 전기·정보공학부, 보안 최적화 연구실. <https://ece.snu.ac.kr/research-faculty/research/lab?labidx=44&md=view> (열람 2026-10-27).
[^pi]: 서울대학교 전기·정보공학부, 백윤흥 교수 소개. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p058> (열람 2026-10-27).
[^ypaek]: SOR Lab, Yunheung Paek 교수 개인 소개. <https://sor.snu.ac.kr/document/ypaek> (열람 2026-10-27).
[^professors]: SOR Lab, Professors. <https://sor.snu.ac.kr/document/professors> (열람 2026-10-27).
[^intro]: SOR Lab, Introduction. <https://sor.snu.ac.kr/document/introduction> (열람 2026-10-27).
[^privacy]: SOR Lab, Privacy Enhancing Computing. 동형암호 연산 최적화와 가속 하드웨어, 프라이버시 보존형 인공지능 연구. <https://sor.snu.ac.kr/document/dataprivacy> (열람 2026-10-27).
[^aicomputing]: SOR Lab, AI Computing·Design Space Exploration. 가속기 구조·연산 배치의 설계 공간 탐색. <https://sor.snu.ac.kr/document/aisec> <https://sor.snu.ac.kr/post/677> (열람 2026-10-27).
[^system]: SOR Lab, System Security. 취약점 진단·퍼징·신뢰 기반 실행환경 연구. <https://sor.snu.ac.kr/document/swsec> (열람 2026-10-27).
[^hardware]: SOR Lab, Hardware-based Security. 프로세서 수정·보안 모듈·하드웨어 기능을 활용하는 보안 연구. <https://sor.snu.ac.kr/post/556> (열람 2026-10-27).
[^students]: SOR Lab, Students 이름 목록. <https://sor.snu.ac.kr/board/Students> (열람 2026-10-27).
[^studentdetails]: SOR Lab, 구성원 상세 글의 과정·분류·학력 표기. 각 표의 이름을 상세 글로 연결했다. <https://sor.snu.ac.kr/board/Students> (열람 2026-10-27).
[^alumni]: SOR Lab, Alumni 명단과 개인별 상세 글. 각 표의 이름을 해당 학위·진로를 적은 글로 연결했다. <https://sor.snu.ac.kr/board/Alumni> <https://sor.snu.ac.kr/board/Alumni?page=2> (열람 2026-10-27).
[^pubs]: SOR Lab, International Papers 목록과 개별 글의 저자 순서·발표 연월. <https://sor.snu.ac.kr/board/Publication> <https://sor.snu.ac.kr/board/Publication?page=2> <https://sor.snu.ac.kr/board/Publication?page=3> (열람 2026-10-27).
[^domesticpubs]: SOR Lab, Domestic Papers. <https://sor.snu.ac.kr/board/d_papers> <https://sor.snu.ac.kr/board/d_papers?page=2> <https://sor.snu.ac.kr/board/d_papers?page=3> <https://sor.snu.ac.kr/board/d_papers?page=4> <https://sor.snu.ac.kr/board/d_papers?page=5> (열람 2026-10-27).
[^patents]: SOR Lab, International Patents·Domestic Patents 목록과 개별 글의 출원·등록 월 표기. <https://sor.snu.ac.kr/board/i_patents> <https://sor.snu.ac.kr/board/d_patents> (열람 2026-10-27).
[^news]: SOR Lab, News 둘째 쪽의 2023년 한국연구재단 중견연구 과제 선정 글 제목. <https://sor.snu.ac.kr/board/news?&page=2> (열람 2026-10-27).
[^p1]: K. Nam, Y. Joo, S. Ha, Y. Paek, 34th USENIX Security Symposium (USENIX Security 25), 3083–3102 (2025). <https://www.usenix.org/conference/usenixsecurity25/presentation/nam-slothe> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://www.usenix.org/conference/usenixsecurity25/presentation/nam-slothe> (열람 2026-10-27).
[^p2]: S. Deshpande 외, Y. Paek, ACM Transactions on Embedded Computing Systems (2025). <https://doi.org/10.1145/3728469> 초록 기준(Crossref 등록 초록).
[^p3]: I. Bang, M. Kayondo, H. Moon, Y. Paek, 32nd USENIX Security Symposium (USENIX Security 23), 6947–6964 (2023). <https://www.usenix.org/conference/usenixsecurity23/presentation/bang> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://www.usenix.org/conference/usenixsecurity23/presentation/bang> (열람 2026-10-27).
[^p4]: M. Kayondo 외, Y. Paek, Network and Distributed System Security Symposium (NDSS) 2026 (2026). <https://www.ndss-symposium.org/ndss-paper/secv-securing-connected-vehicles-with-hardware-trust-anchors/> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://www.ndss-symposium.org/ndss-paper/secv-securing-connected-vehicles-with-hardware-trust-anchors/> (열람 2026-10-27). 교신저자 표기: <https://sor.snu.ac.kr/post/883>. 학회 연도: <https://www.ndss-symposium.org/ndss2026/accepted-papers/>.
[^p5]: Y. Cho 외, Y. Paek, arXiv:2408.15591 (공개판) (2024). <https://arxiv.org/abs/2408.15591> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2408.15591> (열람 2026-10-27). 교신저자 표기: <https://sor.snu.ac.kr/post/774>.
[^p6]: Y. Lee 외, Y. Paek, arXiv:2403.02846 (공개판) (2024). <https://arxiv.org/abs/2403.02846> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2403.02846> (열람 2026-10-27). 교신저자 표기: <https://sor.snu.ac.kr/post/689?page=2>.
[^p7]: W. R. Ha, H. Kim, Y. Paek, IEEE Access (2023). <https://doi.org/10.1109/access.2023.3278274> 초록 기준(OpenAlex 등록 초록).
[^p8]: H. Kim 외, Y. Paek, Future Generation Computer Systems (2025). <https://doi.org/10.1016/j.future.2025.108123> 초록 기준(OpenAlex 등록 초록). 교신저자 표기: <https://sor.snu.ac.kr/post/865>.

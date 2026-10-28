# 임베디드 컴퓨팅 연구실 (Embedded Computing Laboratory, ECL)

**KAIST 전산학부 · 김순태 교수**

- 분야: 임베디드 시스템, 컴퓨터 구조, 메모리·저장 시스템, 저전력·고신뢰성 컴퓨팅, 하드웨어 보안, 인공지능 시스템, 모바일 입력
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: 컴퓨터 구조·운영체제[^intro][^research], 저장 시스템·SSD[^research][^p2][^p3], AI 시스템·인프라[^research][^p1], 하드웨어 보안[^research][^p7], AI·기계학습 보안·프라이버시[^research][^p5], 메모리 내 연산[^projects], 인간–컴퓨터 상호작용[^p8], 실시간·임베디드 시스템[^intro][^research]
- 홈페이지: <https://ecl.kaist.ac.kr/>
- 근거와 출처: [ECL 근거 페이지](ecl-sources.md)

> 기기 안의 컴퓨터와 메모리·저장장치가 전력을 아끼면서 안정적으로 작동하도록, 하드웨어 구조와 시스템 소프트웨어를 함께 설계하는 연구실이다.[^intro][^research]

## 무엇을 연구하나

임베디드 컴퓨팅 연구실은 특정 기능을 수행하는 기기에 컴퓨터가 부품으로 들어가는 임베디드 시스템을 연구한다. 컴퓨터 구조(프로세서·메모리 같은 하드웨어의 구성과 동작 방식)와 메모리(처리에 필요한 명령과 데이터를 저장하는 장치)를 다루고, 하드웨어를 바탕으로 시스템 소프트웨어(컴퓨터 자원과 프로그램 실행을 관리하는 소프트웨어)를 설계한다. 목표는 성능, 전력 사용 효율, 실시간성(정해진 시간 조건에 맞춰 결과를 내는 성질), 신뢰성(정해진 조건과 기간에 요구되는 기능을 수행하는 성질)을 함께 개선하는 것이다.[^intro][^research]

한 축은 데이터를 저장하고 옮기는 구조다. 캐시(사용할 데이터를 보관해 다시 이용할 수 있게 하는 저장 공간), DRAM(Dynamic Random Access Memory, 저장 상태를 주기적으로 유지해 주어야 하는 반도체 메모리), 플래시 메모리(블록 단위로 지우고 다시 쓰는 비휘발성 반도체 메모리), SSD(Solid-State Drive, 반도체 메모리로 데이터를 보관하는 저장장치)를 연구 대상으로 든다. 최근 논문에서는 데이터 압축(데이터를 나타내는 분량을 줄이는 방법)과 SSD 내부 자원 관리를 결합해 저장·읽기 작업을 개선했다.[^research][^p2][^p3]

다른 축은 기기 안에서 인공지능을 실행하는 하드웨어다. 연구실은 인공지능 계산에 맞춘 아키텍처(구성 요소의 배치·연결·동작 방식을 정한 설계)를 최적화하고 전력과 성능을 개선한다고 설명한다. 대표 논문에서는 양자화(값을 정해진 표현 수준에 대응시키는 방법)를 적용한 합성곱 신경망(CNN, Convolutional Neural Network, 같은 계산 규칙을 입력의 여러 위치에 적용하는 신경망)의 데이터 압축을 다뤘다. 신경망은 연결된 계산 요소의 작동 관계를 자료로부터 학습하는 모형이다. 최근 과제는 대규모 인공지능 모델의 학습·추론(학습한 모형으로 결과를 계산하는 과정)에 특화된 플래시 기반 메모리 내 연산(PIM, Processing-in-Memory, 메모리 안이나 가까이에서 계산하는 방식) 구조 개발을 목표로 한다.[^research][^p1][^projects] 연산 가속기(특정 종류의 계산을 전담하도록 설계한 처리장치) 연구에서는 희소 행렬(원소 대부분이 영인 행렬)의 곱셈에서 데이터 이동과 중간 계산 결과를 관리하는 문제를 다뤘다. 행렬은 수를 행과 열로 나열한 표다.[^p6]

연구실은 데이터와 소프트웨어를 보호하는 시큐어 메모리(공격으로부터 저장된 정보를 보호하도록 설계한 메모리)도 연구한다. 암호화한 정보를 저장할 때 생기는 추가 저장 공간과 연산 부담, 보호 가능한 메모리 크기의 제약을 연구 문제로 든다. 외부 공격과 오류에 강한 인공지능, 오류를 견디는 캐시·메모리 설계, 전력 소비를 줄이는 메모리 구조, 실시간 운영체제(시간 조건을 만족하도록 자원과 작업 실행을 관리하는 소프트웨어)도 연구 갈래다.[^research] 대표 논문에서는 텍스트를 처리하는 모델의 정확도에 영향을 주는 입력 단위를 분류해 보호를 돕는 C2C를 제안했다.[^p5] 또 합성곱 신경망의 메모리 접근 특성을 살펴, 무결성(허가되지 않은 변경이나 손상이 없는 성질)을 검사하는 구조를 설계했다.[^p7]

모바일 기기에 감정을 입력하는 방법도 다뤘다. 이 연구는 표정과 심박수(일정 시간 동안 심장이 뛰는 횟수) 정보를 결합해 사용자의 감정을 알아내고 입력으로 쓰는 새 기법을 제안한다. 전면 카메라와 심박 센서가 있는 모바일 기기에 구현할 수 있는 방법으로, 사용자 평가를 통해 효과와 구현 가능성을 살폈다. 개인화된 기기 상호작용에 활용할 가능성을 제시한 연구다.[^p8]

## 주요 연구 주제

### 1. 메모리·저장장치의 자원 관리와 저전력 설계

SSD가 데이터를 읽고 쓰는 방식과 내부 저장 공간의 배분을 함께 연구한다. 대표 논문은 가상머신(Virtual Machine, 소프트웨어로 구현한 컴퓨터 실행 환경)들이 SSD를 공유할 때의 자원 관리와, 페이지(플래시 메모리의 읽기·쓰기 단위) 일부만 읽는 기능을 활용하는 압축·병렬 처리 구조를 다룬다.[^research][^p2][^p3]

프로그램 명령을 보관하는 캐시와 압축된 명령을 되푸는 장치도 함께 설계한다. 대표 논문 CID(Co-Architecting Instruction Cache and Decompression System for Embedded Systems)는 압축 여부와 원래 주소를 캐시가 다루도록 구조를 바꾸고, 압축 해제 장치의 부담을 줄이는 코드 압축 방법을 함께 제안했다.[^p4]

### 2. 인공지능 데이터 압축과 연산 가속

인공지능 모델의 데이터 특성을 하드웨어 설계에 반영한다. 대표 논문은 양자화된 합성곱 신경망의 데이터에 나타나는 영값과 적은 비트(이진 정보를 나타내는 기본 단위)로 표현할 수 있는 값을 이용해 압축하는 ENCORE를 제안했다.[^p1] 연구실은 임베디드 인공지능의 전력·성능 개선과 인공지능용 시큐어 메모리를 현재 연구로 소개한다.[^research]

HARP(Hardware-Based Pseudo-Tiling)는 압축된 원래 행렬을 유지하면서 하드웨어가 논리적으로 구획을 나누는 의사 타일링을 제안했다. 타일링은 계산할 데이터를 구획으로 나누는 방식이다. HARP는 구획마다 압축 표현을 새로 만들지 않으며, 실행 중 실제 계산에 쓰일 열·행 쌍을 가리키는 Run-time Operand Descriptor라는 정보로 불필요한 입력 접근을 건너뛴다. 여러 구획을 합치는 슈퍼 타일링(super-tiling)과 한 구획을 다시 나누는 서브 타일링(sub-tiling)도 수행해 의사 타일링의 효율을 높인다.[^p6]

### 3. 인공지능·메모리의 보안과 신뢰성

텍스트를 처리하는 모델의 토큰(모델이 입력을 나누어 다루는 단위)을 수치 배열로 나타낸 임베딩 벡터(입력의 특징을 수치 배열로 나타낸 표현)가 공격이나 오류로 손상되면 정확도에 영향을 줄 수 있다. C2C는 그중 정확도에 중요한 토큰을 분류해 해당 벡터의 보호를 돕는 틀이다.[^p5]

합성곱 신경망은 메모리의 특정 영역에 쓰기가 집중될 수 있다. Countermark-tree는 이 접근 특성을 반영해 메모리의 무결성을 검사하는 정보의 계층 구조를 설계한 연구다.[^p7] 연구실은 오류를 견디는 하드웨어와 시간 조건을 고려한 구조·운영체제도 연구한다고 설명한다.[^research]

### 4. 감정 정보를 이용하는 모바일 입력

표정과 심박 정보를 함께 이용해 감정을 기기의 입력으로 쓰는 방법이다. 말이나 글에 드러나지 않는 감정 정보를 모바일 상호작용에 활용하려는 연구로, 개인화되고 상황에 반응하는 상호작용을 제공할 가능성을 제시했다.[^p8]

## 대표 논문

최근 5년 논문 가운데 김순태 교수가 마지막 저자인 논문에서 압축·저장 시스템, 연산 가속, 인공지능·메모리 보안, 모바일 입력을 다룬 여덟 편을 골랐다. 최신 논문으로 2025년 C2C를 포함했다. “쉽게 말하면” 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2024 | [Zero and Narrow-width Value-aware Compression for Quantized Convolutional Neural Networks](https://doi.org/10.1109/TC.2023.3315051) · IEEE Transactions on Computers | 양자화한 합성곱 신경망에서는 영값만 이용하는 압축이 데이터 특성을 충분히 활용하지 못하는 문제를 다뤘다. 영값이 연속되는 길이와 적은 비트로 표현되는 값을 함께 이용하는 ENCORE 압축 방법을 제안했다.[^p1] | 1저자 Myeongjae Jang, 마지막 저자 김순태 |
| 2 | 2024 | [Highly VM-Scalable SSD in Cloud Storage Systems](https://doi.org/10.1109/TCAD.2023.3305573) · IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems | 여러 가상머신이 SSD를 함께 쓰면 내부 정리 작업의 효율이 낮아지는 문제를 다뤘다. 저장 자원을 동적으로 나누어 가상머신에 배분하면서, 쓰기 요청이 급변할 때 사용하는 공용 완충 공간을 함께 두는 관리 방법을 제안했다.[^p2] | 1저자 Wonyoung Lee, 마지막 저자 김순태 |
| 3 | 2023 | [PR-SSD: Maximizing Partial Read Potential By Exploiting Compression and Channel-Level Parallelism](https://doi.org/10.1109/TC.2022.3178326) · IEEE Transactions on Computers | 플래시 메모리의 일부만 읽는 기능을 압축과 함께 활용하는 PR-SSD를 제안했다. 압축 해제의 지연을 줄이는 압축 방법과, 압축되지 않은 요청도 나누어 서로 다른 데이터 통로에서 처리하게 하는 구조를 결합했다.[^p3] | 1저자 Mincheol Kang, 마지막 저자 김순태 |
| 4 | 2021 | [CID: Co-Architecting Instruction Cache and Decompression System for Embedded Systems](https://doi.org/10.1109/TC.2020.3010062) · IEEE Transactions on Computers | 프로그램 코드를 압축하면 저장 공간을 아낄 수 있지만 압축 해제와 주소 변환에도 자원이 필요하다. 명령어 캐시와 압축 해제 구조를 함께 설계하고 새 코드 압축 방법을 더해, 비교한 구조에 비해 에너지 소비와 면적 부담을 줄였다.[^p4] | 1저자 Jinkwon Kim, 마지막 저자 김순태 |
| 5 | 2025 | [C2C: A Framework for Critical Token Classification in Transformer-Based Inference Systems](https://doi.org/10.23919/date64628.2025.10992782) · DATE | 텍스트 입력을 나타내는 임베딩 벡터가 공격이나 오류로 손상되면 모델의 정확도가 낮아질 수 있다. 정확도에 중요한 토큰을 분류해 해당 벡터를 보호하는 데 쓰도록 C2C라는 틀을 제안했다.[^p5] | 1저자 Myeongjae Jang, 마지막 저자 김순태 |
| 6 | 2023 | [HARP: Hardware-Based Pseudo-Tiling for Sparse Matrix Multiplication Accelerator](https://doi.org/10.1145/3613424.3623790) · MICRO | 원래 압축 행렬은 유지하면서 하드웨어가 논리적으로 구획을 나누는 HARP를 제안했다. 계산에 쓰일 열·행 쌍을 가리키는 정보를 이용해 구획마다 압축 표현을 새로 만드는 작업과 불필요한 입력 접근을 피한다. 구획을 합치거나 다시 나누는 방법도 더해 의사 타일링의 효율을 높인다.[^p6] | 1저자 Jinkwon Kim, 마지막 저자 김순태 |
| 7 | 2022 | [Efficient Integrity-Tree Structure for Convolutional Neural Networks through Frequent Counter Overflow Prevention in Secure Memories](https://doi.org/10.3390/s22228762) · Sensors | 합성곱 신경망의 쓰기가 메모리의 특정 영역에 집중되면 보안용 카운터(횟수를 세는 값)가 표현 범위를 넘는 일이 잦아질 수 있음을 분석했다. 이를 바탕으로 Countermark-tree라는 무결성 검사 구조를 제안해 비교한 기법보다 에너지 소비를 줄이고 성능을 개선했다.[^p7] | 1저자 Jesung Kim, 마지막 저자 김순태 |
| 8 | 2023 | [Effective Emoticon Suggestion Technique Based on Active Emotional Input Using Facial Expressions and Heart Rate Signals](https://doi.org/10.3390/s23094460) · Sensors | 표정과 심박 정보를 결합해 감정을 모바일 시스템의 입력으로 쓰는 새 기법을 제안했다. 전면 카메라와 심박 센서가 있는 기기에서 구현할 수 있는 방법이며, 사용자 평가로 효과와 구현 가능성을 살폈다. 개인화된 모바일 상호작용에 활용할 가능성을 제시했다.[^p8] | 1저자 Jesung Kim, 마지막 저자 김순태 |

## 교수와 전문 분야

김순태 교수(Soontae Kim)는 KAIST 전산학부 교수다. 전산학부 교수 명단은 전문 분야를 임베디드 컴퓨팅, 컴퓨터 구조, 저전력, 신뢰성, 시큐리티로 적는다.[^faculty] 연구실 소개에 따르면 2007년 6월부터 KAIST에 재직했고, 그전에는 2004–2007년 미국 사우스플로리다대학교 조교수로 일했다. 2003년 12월 펜실베이니아주립대학교에서 Computer Science and Engineering 박사학위를, 1998년과 1996년 중앙대학교에서 같은 전공의 석사·학사학위를 받았다.[^members][^cv]

최근 논문에서 확인되는 전문 분야는 신경망 데이터의 압축, SSD 내부의 자원 관리와 읽기 구조, 명령어 캐시와 코드 압축의 공동 설계다.[^p1][^p2][^p3][^p4] 연구실 연구 소개는 여기에 메모리 보안, 오류를 견디는 시스템 설계, 실시간성과 저전력을 함께 고려하는 컴퓨팅을 포함한다.[^research]

대표 논문에는 텍스트 모델의 보호 대상 분류, 희소 행렬 연산 가속의 메모리 작업 관리, 신경망의 접근 특성을 반영한 시큐어 메모리, 감정 정보를 쓰는 모바일 입력도 나타난다.[^p5][^p6][^p7][^p8]

## 응용 분야

연구 대상은 스마트폰과 기기 내 컴퓨터, 메모리·SSD, 차량용 전자·컴퓨터 시스템이다.[^dept] 대표 논문은 클라우드에서 여러 가상머신이 함께 쓰는 저장장치와, 인공지능 계산에 쓰이는 데이터 저장·이동에 연결된다.[^p1][^p2][^p3] 최근 과제에는 공간 정보를 통합적으로 이해하는 인공지능(GeoAI)과 첨단 모빌리티, 대규모 인공지능용 플래시 기반 메모리 내 연산이 있다.[^projects]

감정 정보를 쓰는 입력 연구는 모바일 기기에서 사용자가 감정을 표현하는 일과, 개인화된 사용자 경험을 제공하는 데 활용할 가능성을 제시한다.[^p8]

## 구성원

2026년 10월 27일 연구실 Members 페이지 기준으로 박사과정 2명과 석사과정 2명이다.[^members] Mohammad Zain Farooq Gill과 Woosung Choi의 10월 28일 상세 페이지도 석사과정으로 적는다.[^member-gill][^member-choi] “대표 논문 참여”는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Haejin Nam | 박사과정 | Processor Microarchitecture; General Purpose Near Data Processing System | haejinnam@kaist.ac.kr | 1, 5, 6 |
| Sihyun Kim | 박사과정 | Computer Architecture; Flash-based Memory Systems | sihyun.kim@kaist.ac.kr | 5 |
| Mohammad Zain Farooq Gill | 석사과정 | Computer Architecture | zfgill@kaist.ac.kr |  |
| Woosung Choi | 석사과정 | Computer Architecture; Flash-based Memory Systems | woosung.choi@kaist.ac.kr |  |

## 졸업생 진로

연구실 Alumni 칸의 32명을 게시 순서로 실었다. 학위 연도가 있는 항목은 2010–2026년이며, 방문 연구원과 연구교수로 적힌 항목도 포함한다. 진로는 누리집에 적힌 기관·직함이고 졸업 당시의 진로로 한정하지 않는다.[^members] 홍정규·홍석인·김제성의 조교수 임용은 각각 2023년 9월 4일, 2022년 3월 1일, 2025년 3월 6일 연구실 공지에 적혀 있다.[^career1][^career2][^career3] 김제성 임용 공지는 연구실 석사 졸업 후 LG전자 연구원 경력과 연구실 박사·박사후 연구 경력을 함께 소개한다.[^career3]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Chen Yue | M.S. (2026 Spring) | Approaching AI |
| Jesung Kim (김제성) | Ph.D. (2022 Fall); Postdoc (Aug. 2022 ~  Dec. 2024) | Mokpo National University 인공지능공학과 조교수 |
| Myeongjae Jang | Ph.D. (2025 Spring) | ETRI (Electronics and Telecommunications Research Institute) |
| Jinkwon Kim | Ph.D. (2024 Spring) | Cornell University |
| Yongwook Lee | M.S. (2023 Spring) | FADU Technology |
| Hyungsoon Kim | M.S. (2023 Spring) | Koscom Corporation |
| Wonyoung Lee | Ph.D. (2023 Spring) | Samsung Advanced Institute of Technology |
| Mincheol Kang | Ph.D. (2022 Fall) | Samsung Advanced Institute of Technology |
| Junoh Moon | M.S. (2022 Spring) | December & Company |
| Jehoon Park | M.S. (2022 Spring) | Samsung Electronics |
| Imran Fareed | Ph.D. (2021 Spring) | Interuniversity Microelectronics Centre (IMEC) |
| Muhammad Avais Qureshi | Ph.D. (2020 Spring) |  |
| Myoungjoon Lee | Ph.D. (2020 Spring) | Samsung Electronics. |
| Jungwoo Park | Ph.D. (2019 Fall) | Samsung Electronics |
| Hyeonggyu Kim | Ph.D. (2019 Spring) | Samsung Electronics |
| Yeji Kang | M.S. (2018 Spring) | NAVER |
| Bohun Seo | M.S. (2018 Spring) | Korea Financial Telecommunications & Clearings Institute |
| Ryunkyun Park | M.S. (2018 Spring) | Samsung Electronics |
| Muhammad Hassan | M.S. (2017 Fall) |  |
| Jeongkyu Hong (홍정규) | Ph.D. (2017 Fall); Postdoc (Aug 2017 ~ Aug 2018) | University of Seoul 전자전기컴퓨터공학부 조교수 |
| Yebin Lee | Ph.D. (2017 Spring) | Founder & CEO of Nextwave |
| Minho Ju | M.S. (2016 Spring) | Samsung Electronics |
| Hamed Farbeh | Visiting Researcher (Oct. 2014 ~ May 2015) | Professor at Amirkabir University of Technology (AUT) |
| Hongsun Ahn | M.S. (2015 Spring) | The Export-Import Bank of Korea |
| Seokin Hong (홍석인) | Ph.D. (2015 Spring) | Sungkyunkwan University 반도체시스템공학과 조교수 |
| Jongmin Lee | Ph.D. (2015 Spring) | Professor at Wonkwang University |
| Mohammad Abdur Rouf | Ph.D. (2014 Fall) | Professor at Dhaka University of Engineering and Technology, Bangladesh |
| Tayyeb Mahmood | Ph.D. (2013 Spring); Postdoc (Sep 2014 ~ Feb 2015) | Professor at RCET-UET, Lahore, Pakistan |
| Kwangcheol Shin | Research Professor | Professor at Huree University, Ulan Bator, Mongolia |
| Seokgi Kim | M.S. (2012 Spring) | National Security Research Institute |
| Taeju Park | M.S. (2011 Fall) | University of Michigan, Ann Arbor |
| Gieil Lee | M.S. (2010 Fall) | LG Electronics (LG전자) |

## 최근 5년 논문 목록

아래 논문은 캐시·메모리·SSD의 구조와 관리, 데이터 압축, 인공지능 계산과 보안, 감정 정보를 쓰는 모바일 입력을 다룬다. 연구실 Publications의 2021–2026년 구역에서 학술지 10편과 학회 6편을 실었다. 제목·저자·발표처는 연구실 표기를 따른다. 2026년 PABLOR는 누리집이 Early Access로 적고, RepliCounter의 연도는 누리집 학회 구역의 표기다.[^pubs]

**2026**

- Sihyun Kim, Haejin Nam, Wonyoung Lee, Mincheol Kang, Jesung Kim, and Soontae Kim. "PABLOR: Intra-Block Variation-Aware Refresh for High Performance and Lifetime in 3D NAND Flash". *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), 2026 (Early Access)*.
- Jesung Kim, Jeongkyu Hong, and Soontae Kim. "RepliCounter: Improving Reliability of Counter Caches through Area-efficient Counter Replication". *IEEE International Conference on Computer Design (ICCD'26)*.

**2025**

- Myeongjae Jang, Jesung Kim, Haejin Nam, Sihyun Kim, and Soontae Kim. "C2C: A Framework for Critical Token Classification in Transformer-Based Inference System". *Design, Automation, and Test in Europe Conference (DATE'25)*. DOI: <https://doi.org/10.23919/date64628.2025.10992782>.

**2024**

- Myeongjae Jang, Jinkwon Kim, Haejin Nam, and Soontae Kim. "Zero and Narrow-width Value-aware Compression for Quantized Convolutional Neural Networks". *IEEE Transactions on Computers (TC), Vol. 73, No. 1, pp.249-262, Jan. 2024*. DOI: <https://doi.org/10.1109/TC.2023.3315051>.
- Wonyoung Lee, Mincheol Kang, and Soontae Kim. "Highly VM-Scalable SSD in Cloud Storage Systems". *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), Vol. 43, No. 1, Jan. 2024*. DOI: <https://doi.org/10.1109/TCAD.2023.3305573>.

**2023**

- Jesung Kim, Mincheol Kang, Bohun Seo, Jeongkyu Hong, and Soontae Kim. "Effective Emoticon Suggestion Technique Based on Active Emotional Input Using Facial Expressions and Heart Rate Signals". *Sensors 23, no. 9, May. 2023*. DOI: <https://doi.org/10.3390/s23094460>.
- Mincheol Kang, Wonyoung Lee, Jinkwon Kim, and Soontae Kim. "PR-SSD: Maximizing Partial Read Potential By Exploiting Compression and Channel-Level Parallelism". *IEEE Transactions on Computers (TC), Vol. 72, No. 3, pp.772-785, Mar.2023*. DOI: <https://doi.org/10.1109/TC.2022.3178326>.
- Jinkwon Kim, Myeongjae Jang, Haejin Nam, and Soontae Kim. "HARP: Hardware-Based Pseudo-Tiling for Sparse Matrix Multiplication Accelerator". *IEEE/ACM International Symposium on Microarchitecture (MICRO'23)*. DOI: <https://doi.org/10.1145/3613424.3623790>.

**2022**

- Jesung Kim, Wonyoung Lee, Jeongkyu Hong, and Soontae Kim. "Efficient Integrity-Tree Structure for Convolutional Neural Networks through Frequent Counter Overflow Prevention in Secure Memories". *Sensors 22, no. 22, Nov. 2022*. DOI: <https://doi.org/10.3390/s22228762>.
- Myeongjae Jang, Jinkwon Kim, Jesung Kim, and Soontae Kim. "ENCORE Compression: Exploiting Narrow-width Values for Quantized Deep Neural Networks". *Design, Automation, and Test in Europe Conference (DATE'22)*.
- Junoh Moon, Mincheol Kang, Wonyoung Lee, and Soontae Kim. "Salvaging Runtime Bad Blocks by Skipping Bad Pages for Improving SSD Performance". *Design, Automation, and Test in Europe Conference (DATE'22)*.
- Jinkwon Kim, Mincheol Kang, Jeongkyu Hong, and Soontae Kim. "Exploiting Inter-block Entropy to Enhance the Compressibility of Blocks with Diverse Data". *IEEE International Symposium on High-Performance Computer Architecture (HPCA'22)*.

**2021**

- Imran Fareed, Mincheol Kang, Wonyoung Lee, and Soontae Kim. "Update Frequency-directed Subpage Management for Mitigating Garbage Collection and DRAM Overheads". *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), Vol. 40, No. 12 pp. 2467-2480, Dec. 2021*.
- Jinkwon Kim, Seokin Hong, Jeongkyu Hong, and Soontae Kim. "CID: Co-Architecting Instruction Cache and Decompression System for Embedded Systems". *IEEE Transactions on Computers (TC), Vol. 70, No. 7, pp.1132-1145, Jul. 2021*. DOI: <https://doi.org/10.1109/TC.2020.3010062>.
- Jungwoo Park, Soontae Kim, and Jong-Uk Hou. "An L2 Cache Architecture Supporting Bypassing for Low Energy and High Performance". *ELECTRONICS, Vol. 28, No. 6, pp. 1357-1370, Jun. 2021*.
- Hamed Farbeh, Leila Delshadtehrani, Hyeonggyu Kim, and Soontae Kim. "ECC-United Cache: Maximizing Efficiency of Error Detection/Correction Codes in Associative Cache Memories". *IEEE Transactions on Computers (TC), Vol. 10, No. 11, pp. 640-654, Apr. 2021*.

## 과제

수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 과제 5건이다. 과제 설명의 NPU는 신경망 계산을 수행하는 처리장치(Neural Processing Unit)를 뜻한다.[^projects]

- GeoAI 기반 첨단 모빌리티 융합 연구소 (기간 2026.07 ~ 2028.12; 지원 KAIST (Korea Advanced Institute of Science and Technology); 연구 목표 본 연구에서는 다양한 공간 정보를 통합적으로 이해하는 시공간 맥락 기반 GeoAI 원천기술 개발을 목표로 한다. )
- 대규모 인공지능 모델의 신뢰성 중심 성능 향상을 위한 플래시 기반 PIM 시스템 연구 (기간 2026.03 ~ 2029.02; 지원 한국연구재단 (National Research Foundation); 연구 목표 본 연구에서는 대규모 인공지능 모델의 학습과 추론에 특화된 고신뢰·고성능 플래시 기반 PIM 아키텍처 개발을 목표로 한다.)
- 데이터 중심 컴퓨팅의 효율적 메모리 관리를 위한 소프트웨어-하드웨어 융합 연구 (기간 2022.03 ~ 2025.02; 지원 한국연구재단 (National Research Foundation); 연구 목표 본 연구에서는 소프트웨어의 특성을 이용한 하드웨어 최적 설계 또는 소프트웨어-하드웨어 융합 디자인을 통한 효율적인 메모리 관리 기법을 목표로 한다.)
- 고성능 SSD에 특화된 압축 알고리즘 및 아키텍처 개발 (기간 2021.06 ~ 2022.05; 지원 한국연구재단 (National Research Foundation); 연구 목표 본 연구에서는 고성능 SSD에 특화된 압축 알고리즘 재설계 및 아키텍처 개발을 목표로 한다.)
- 메모리-스토리지 복합 압축 기술 개발 (기간 2020.09 ~ 2025.09; 지원 삼성전자 (Samsung Electronics); 연구 목표 본 연구에서는 DRAM/SSD/NPU의 효율성을 향상하기 위한 압축 메모리/스토리지 시스템 구조를 연구한다.)

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291, KAIST 김병호IT융합빌딩(N1) 922호.[^intro]
- 교수연구실: N1 903호.[^intro][^faculty]
- 연구실 전화: 042-350-7854.[^intro]
- 교수 전화: 042-350-3554.[^cv]
- 교수 이메일: kims@kaist.ac.kr.[^members][^cv]

## 각주
[^intro]: 연구실 Introduction. 임베디드 시스템의 성능·전력 효율·실시간성·신뢰성을 하드웨어와 시스템 소프트웨어로 연구한다고 소개한다. <https://ecl.kaist.ac.kr/introduction> (2026-10-27 열람).
[^research]: 연구실 Research. 메모리·저장 기술, 안전한 메모리, 임베디드·보안 인공지능, 오류에 견디는 설계, 저전력 캐시·DRAM, 실시간 구조·운영체제를 연구한다고 설명한다. <https://ecl.kaist.ac.kr/research> (2026-10-27 열람).
[^members]: 연구실 Members. 교수 소개, 현재 학생, Alumni와 진로, 기관 이메일. <https://ecl.kaist.ac.kr/members> (2026-10-27 열람).
[^pubs]: 연구실 Publications. Journals·Conferences·Domestic Publications 구역과 논문 표기. <https://ecl.kaist.ac.kr/publications> (2026-10-27 열람).
[^projects]: 연구실 Projects. 각 과제의 제목·기간·지원기관·연구 목표. 대규모 인공지능 모델의 학습·추론에 특화된 플래시 기반 PIM 구조 개발을 목표로 한다고 적는다. <https://ecl.kaist.ac.kr/projects> (2026-10-27 열람).
[^faculty]: KAIST 전산학부 교수 명단, 김순태 교수 항목. 직위, 전문 분야, 교수연구실. <https://cs.kaist.ac.kr/people/faculty> (2026-10-28 열람).
[^dept]: KAIST 전산학부 임베디드 컴퓨팅 연구실 소개. 국문 이름, 김순태 교수, 임베디드 컴퓨팅·컴퓨터 구조·운영체제 연구와 스마트폰·메모리·차량용 시스템 응용. <https://cs.kaist.ac.kr/research/labView?sn=59&menu=64> (2026-10-27 열람).
[^cv]: 연구실 Curriculum Vitae. 김순태 교수의 소속·학력·경력과 연락처. <https://ecl.kaist.ac.kr/members/curriculum-vitae> (2026-10-28 열람).
[^career1]: 연구실 「홍정규 박사 서울시립대학교 조교수 임용」. 2023-09-04 게시. <https://ecl.kaist.ac.kr/announcements/%ED%99%8D%EC%A0%95%EA%B7%9C-%EB%B0%95%EC%82%AC-%EC%84%9C%EC%9A%B8%EC%8B%9C%EB%A6%BD%EB%8C%80%ED%95%99%EA%B5%90-%EC%A1%B0%EA%B5%90%EC%88%98-%EC%9E%84%EC%9A%A9> (2026-10-28 열람).
[^career2]: 연구실 「홍석인 박사 성균관대학교 조교수 임용」. 2022-03-01 게시. <https://ecl.kaist.ac.kr/announcements/%ED%99%8D%EC%84%9D%EC%9D%B8-%EB%B0%95%EC%82%AC-%EC%84%B1%EA%B7%A0%EA%B4%80%EB%8C%80%ED%95%99%EA%B5%90-%EC%A1%B0%EA%B5%90%EC%88%98-%EC%9E%84%EC%9A%A9%EC%9D%98-%EB%B3%B5%EC%82%AC%EB%B3%B8> (2026-10-28 열람).
[^career3]: 연구실 「김제성 박사 국립목포대학교 조교수 임용」. 2025-03-06 게시. 인공지능공학과 조교수 임용과 이전 연구 경력을 소개한다. <https://ecl.kaist.ac.kr/announcements/%EA%B9%80%EC%A0%9C%EC%84%B1-%EB%B0%95%EC%82%AC-%EA%B5%AD%EB%A6%BD%EB%AA%A9%ED%8F%AC%EB%8C%80%ED%95%99%EA%B5%90-%EC%A1%B0%EA%B5%90%EC%88%98-%EC%9E%84%EC%9A%A9> (2026-10-28 열람).
[^member-gill]: 연구실 Mohammad Zain Farooq Gill 상세. 석사과정·연구 관심·기관 이메일. <https://ecl.kaist.ac.kr/members/mohammad-zain-farooq-gill-m-s-student> (2026-10-28 열람).
[^member-choi]: 연구실 Woosung Choi 상세. 석사과정·연구 관심·기관 이메일. <https://ecl.kaist.ac.kr/members/woosung-choi-m-s-student> (2026-10-28 열람).
[^p1]: M. Jang, J. Kim, H. Nam, S. Kim, IEEE Transactions on Computers 73, 249-262. <https://doi.org/10.1109/TC.2023.3315051> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/373937367_Zero_and_Narrow-width_Value-aware_Compression_for_Quantized_Convolutional_Neural_Networks> (2026-10-28 열람).
[^p2]: W. Lee, M. Kang, S. Kim, IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems 43, 113-126. <https://doi.org/10.1109/TCAD.2023.3305573> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/373291840_Highly_VM-Scalable_SSD_in_Cloud_Storage_Systems> (2026-10-28 열람).
[^p3]: M. Kang, W. Lee, J. Kim, S. Kim, IEEE Transactions on Computers. <https://doi.org/10.1109/TC.2022.3178326> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/367774726_PR-SSD_Maximizing_Partial_Read_Potential_By_Exploiting_Compression_and_Channel-Level_Parallelism> (2026-10-28 열람).
[^p4]: J. Kim, S. Hong, J. Hong, S. Kim, IEEE Transactions on Computers 70, 1132-1145 (2021). <https://doi.org/10.1109/TC.2020.3010062> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/343025997_CID_Co-Architecting_Instruction_Cache_and_Decompression_System_for_Embedded_Systems> (2026-10-28 열람).
[^p5]: M. Jang 외, S. Kim, 2025 Design, Automation & Test in Europe Conference (DATE) (2025). <https://doi.org/10.23919/date64628.2025.10992782> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1109/tcad.2026.3734775|10.1145/3613424.3623790|10.23919/date64628.2025.10992782|10.3390/s22228762|10.3390/s23094460> (2026-10-28 열람).
[^p6]: J. Kim, M. Jang, H. Nam, S. Kim, 56th Annual IEEE/ACM International Symposium on Microarchitecture (2023). <https://doi.org/10.1145/3613424.3623790> 초록 기준(Semantic Scholar 등록 초록). 초록 원문 <https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3613424.3623790?fields=title,abstract,authors,venue,year> (2026-10-28 열람).
[^p7]: J. Kim, W. Lee, J. Hong, S. Kim, Sensors (2022). <https://doi.org/10.3390/s22228762> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=Efficient%20Integrity-Tree%20Structure%20for%20Convolutional%20Neural%20Networks%20through%20Frequent%20Counter%20Overflow%20Prevention%20in%20Secure%20Memories> (2026-10-28 열람).
[^p8]: J. Kim 외, S. Kim, Sensors (2023). <https://doi.org/10.3390/s23094460> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=Effective%20Emoticon%20Suggestion%20Technique%20Based%20on%20Active%20Emotional%20Input%20Using%20Facial%20Expressions%20and%20Heart%20Rate%20Signals> (2026-10-28 열람).

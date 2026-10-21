# 컴퓨터구조 및 시스템 연구실 (Computer Architecture and Systems Laboratory, CASys)

**KAIST 전산학부 · 허재혁·권영진·박종세 교수**

- 분야: 인공지능(대형 언어 모델) 시스템과 가속기, 메모리 내 연산(PIM), 엣지–클라우드 프로세서·메모리 구조, 차세대 메모리(CXL·분리형 메모리)를 위한 운영체제, 하드웨어 기반 시스템 보안
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: 대형 언어 모델[^p1][^p3], AI 시스템·인프라[^research][^p1][^p3], 메모리 내 연산[^p1][^p2], AI 반도체·가속기[^p1][^p2], 컴퓨터 구조·운영체제[^p4][^p5][^cs], 하드웨어 보안[^p7][^research], 소프트웨어·시스템 보안[^p6]
- 홈페이지: <https://casyslab.kaist.ac.kr/>
- 근거와 출처: [CASys 근거 페이지](casys-sources.md)

> 컴퓨터의 하드웨어 구조와 운영체제 같은 시스템 소프트웨어를 함께 설계하는 연구실이다. 대형 언어 모델을 더 싸고 빠르게 돌리는 칩·시스템, 새로운 메모리를 잘 쓰는 운영체제, 하드웨어로 지키는 보안 기술을 연구한다. 1974년 KAIST 전산학부가 세워질 때 함께 생긴 연구실로, 전산학부 연구실 소개에 교수 세 명이 함께 올라 있다.[^home][^cs]

## 무엇을 연구하나

연구실은 KAIST 전산학부가 세워진 1974년에 함께 설립됐고, 오랜 기간 컴퓨터 구조와 시스템 소프트웨어의 여러 주제를 연구해 왔다고 소개한다. 지금은 컴퓨팅 스택(하드웨어부터 응용까지 쌓인 계층)의 여러 층에 걸친 융합 연구로 네 문제를 푼다.[^home][^cs]

첫 번째는 **인공지능을 위한 시스템**이다. 인공지능은 모델이 복잡하고 데이터가 방대해 범용 컴퓨터로는 감당하기 어려운 처리 능력을 요구한다. 연구실은 하드웨어, 시스템 소프트웨어, 응용과 알고리즘을 함께 고려해 기계학습에 특화된 컴퓨팅 스택을 만든다.[^cs][^research] 대형 언어 모델의 연산 가운데 계산이 많은 부분은 신경망 가속기(NPU)에, 메모리 대역폭이 많이 드는 부분은 메모리 안에서 계산하는 PIM에 나눠 맡기는 시스템을 만들었고,[^p1] 트랜스포머 뒤를 잇는 새 언어 모델 구조까지 함께 처리하는 PIM 가속기,[^p2] GPU 한 장으로 큰 모델을 처리량 위주로 돌리는 추론 시스템도 내놓았다.[^p3]

두 번째는 **엣지–클라우드 시스템을 위한 프로세서·메모리 구조 설계**다. 응용이 다양해지고 엣지(사용자 가까운 기기)부터 클라우드까지 컴퓨팅 환경이 이질적이 되면서 생기는 프로세서·메모리 설계 문제를 푼다.[^cs][^research]

세 번째는 **차세대 메모리를 위한 운영체제**다. 빠르고 대역폭이 넓거나 전원이 꺼져도 데이터가 남는 새 메모리 기술을 제대로 쓰려면 운영체제가 받쳐 줘야 한다.[^cs] 계산 서버와 메모리 서버를 떼어 놓는 분리형 메모리에서 호환성을 잃지 않고 성능을 내는 라이브러리 운영체제(응용 프로그램과 함께 묶여 도는 가벼운 운영체제),[^p4] 여러 사용자가 함께 쓰는 클라우드에서 빠른 메모리를 나눠 주는 계층형 메모리 시스템을 만들었다.[^p5]

네 번째는 **시스템 보안을 위한 신뢰 컴퓨팅**이다. 보안과 사생활 문제를 시스템 관점에서 보고 하드웨어와 소프트웨어를 함께 설계해 푼다.[^cs][^research] 해제된 메모리를 다시 쓰는 버그(use-after-free)를 막는 메모리 할당기,[^p6] CXL(프로세서와 메모리·장치를 잇는 새 연결 규격) 메모리를 보안 주 메모리로 쓰는 구조를 제안했다.[^p7]

연구실 세미나로는 컴퓨터 시스템·구조 읽기 모임과 컴퓨터 구조, 운영체제, 기계학습 분야 특별 관심 모임(SIGARCH, SIGOPS, SIGML)을 운영한다.[^research]

## 주요 연구 주제

### 1. 대형 언어 모델 시스템과 PIM 가속

NPU–PIM 이종 가속, 차세대 언어 모델용 PIM, 단일 GPU 추론.[^p1][^p2][^p3] 대표 논문 1, 2, 3.

### 2. 차세대 메모리 운영체제

분리형 메모리 라이브러리 OS, 다중 사용자 계층형 메모리.[^p4][^p5] 대표 논문 4, 5.

### 3. 하드웨어·소프트웨어 협력 보안

메모리 오류 방어, 보안 CXL 메모리.[^p6][^p7] 대표 논문 6, 7.

## 대표 논문

랩 국제 학술대회·학술지 목록의 2023–2026년 논문에서 주제별로 골랐다. 연구실 교수 세 명 가운데 한 명이 마지막 저자인 논문이다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2024 | [NeuPIMs: NPU-PIM Heterogeneous Acceleration for Batched LLM Inferencing](https://doi.org/10.1145/3620666.3651380) · ACM ASPLOS 2024 | 대형 언어 모델을 여러 요청씩 묶어 처리할 때 행렬–행렬 곱셈은 계산이 많고, 어텐션(문장 속 단어들 사이의 관계를 계산하는 단계)의 행렬–벡터 곱셈은 메모리 대역폭이 많이 든다. 앞의 것은 NPU가, 뒤의 것은 메모리 안에서 계산하는 PIM이 맡게 하고 두 장치가 동시에 일하도록 묶은 이종 가속 시스템이다.[^p1] | 1저자 Guseul Heo, 마지막 저자 박종세 |
| 2 | 2025 | [Pimba: A Processing-in-Memory Acceleration for Post-Transformer Large Language Model Serving](https://doi.org/10.1145/3725843.3756121) · IEEE/ACM MICRO 2025 | 트랜스포머와 그 뒤를 잇는 새 언어 모델 구조(상태 공간 모델 등)가 여러 요청을 묶어 처리할 때 모두 메모리 대역폭에 막힌다는 분석에서, 두 종류를 한 틀에서 처리하는 PIM 가속기를 제안했다.[^p2] | 1저자 Wonung Kim, 마지막 저자 박종세 |
| 3 | 2025 | [Throughput-Oriented LLM Inference via KV-Activation Hybrid Caching with A Single GPU](https://doi.org/10.1109/iccd65941.2025.00045) · IEEE ICCD 2025 | 모델을 호스트 메모리에 두고 GPU 한 장으로 추론하면 둘 사이 연결이 병목이 된다. 키·값 캐시(앞서 계산한 어텐션 중간값을 저장해 다시 쓰는 저장소) 대신 메모리를 절반만 쓰는 중간 활성값을 저장하고, 모델을 옮겨 오는 동안 노는 GPU로 일부를 다시 계산해 두 방식의 비율을 최적으로 맞추는 추론 시스템(Capture)이다.[^p3] | 1저자 Sanghyeon Lee, 마지막 저자 허재혁 |
| 4 | 2023 | [DiLOS: Do Not Trade Compatibility for Performance in Memory Disaggregation](https://doi.org/10.1145/3552326.3567488) · EuroSys 2023 | 계산과 메모리 서버를 떼어 놓는 분리형 메모리에서, 기존 프로그램을 그대로 쓰는 페이징 방식은 느리다는 통념에 반해 이를 위한 라이브러리 운영체제를 새로 만들었다. 페이지 부재 처리와 미리 읽기를 고치고 응용 정보를 쓰는 기능을 더해 성능을 높였다.[^p4] | 1저자 Wonsup Yoon, 마지막 저자 권영진 |
| 5 | 2026 | [MTTM: Dynamic Fast Memory Partitioning with Bandwidth Optimization for Multi-tenant Cloud](https://doi.org/10.1145/3767295.3769371) · EuroSys 2026 | CXL로 원격 DRAM이나 비휘발성 메모리를 붙인 계층형 메모리에서, 여러 사용자가 함께 쓰는 클라우드의 빠른 DRAM을 작업 특성에 따라 나눠 주고 요청 거절을 줄이도록 실시간으로 조정하는 시스템. 리눅스에 구현해 클라우드 작업 9종으로 평가했다.[^p5] | 1저자 Changjun Lee, 마지막 저자 권영진 |
| 6 | 2024 | BUDAlloc: Defeating Use-After-Free Bugs by Decoupling Virtual Address Management from Kernel · USENIX Security 2024 | 해제된 메모리를 다시 쓰는 버그를 찾아 막는 일회용 메모리 할당기. 사용자 영역 할당기와 커널이 가상·물리 주소 관리를 나눠 맡게 하고, 커널의 페이지 부재 처리를 eBPF(커널 동작을 안전하게 고쳐 끼우는 장치)로 고쳐 해제 요청을 묶어 처리했다. 표준 벤치마크(SPEC CPU 2017)에서 기존 방식(DangZero)보다 성능이 15% 좋았고, 다른 방식(FFmalloc)보다 메모리 부담이 61% 적었다.[^p6] | 1저자 Junho Ahn, 마지막 저자 권영진 |
| 7 | 2025 | [ShieldCXL: A Practical Obliviousness Support with Sealed CXL Memory](https://doi.org/10.1145/3703354) · ACM TACO | 기존 DDR 메모리에서 기밀성·무결성(데이터가 몰래 바뀌지 않았음)·접근 패턴 은닉을 지키려면 비용이 큰 장치가 필요하다. CXL 메모리를 보조 확장이 아닌 보안 주 메모리로 쓰고 채널 암호화와 무결성 보호로 이 비용을 줄이는 구조를 제안했다.[^p7] | 1저자 Kwanghoon Choi, 마지막 저자 허재혁 |

## 교수와 전문 분야

연구실 구성원 페이지는 허재혁, 권영진, 박종세를 교수로, 맹승렬, 조정완을 명예교수로 적는다.[^members] 전산학부 교수진 목록에 따르면 허재혁 교수는 교수이자 석좌교수로 연구 분야는 컴퓨터 구조, 시스템 소프트웨어, 시스템 보안이다. 권영진 교수는 부교수로 운영체제와 시스템 보안을, 박종세 교수는 부교수로 컴퓨터 시스템, 컴퓨터 구조, 인공지능 시스템, 하드웨어–소프트웨어 공동 설계를 연구한다.[^faculty]

논문으로 보면 교수별 전문 분야는 다음과 같다.

- **박종세**: 대형 언어 모델용 가속기와 PIM.[^p1][^p2]
- **허재혁**: GPU 추론 시스템, 보안 메모리 구조.[^p3][^p7]
- **권영진**: 메모리 운영체제, 메모리 안전 보안.[^p4][^p5][^p6]

## 응용 분야

대표 논문과 과제로 보면 데이터센터의 대형 언어 모델 서비스, 클라우드 메모리 관리, 반도체(메모리·가속기) 설계, 시스템 소프트웨어 보안에 닿아 있다.[^p1][^p5][^p7][^projects]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다. 구성원 페이지는 이름과 과정만 적는다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Sangjin Choi | 박사후연구원 | 5 |
| Sanghyeon Lee | 박사후연구원 | 1, 3 |
| Minsu Kim | 박사과정 |  |
| Kwanghoon Choi | 박사과정 | 7 |
| Inhoe Koo | 박사과정 |  |
| Minseong Jang | 박사과정 |  |
| Changhun Oh | 박사과정 |  |
| Yewon Choi | 박사과정 |  |
| Sangyeop Lee | 박사과정 | 1 |
| Hongjin Kim | 박사과정 |  |
| Yubin Lee | 박사과정 | 2 |
| Jungin Rhee | 박사과정 |  |
| Seungjae Lim | 박사과정 |  |
| Jaehong Cho | 박사과정 | 1 |
| Jinwoo Hwang | 박사과정 | 2 |
| Junho Ahn | 박사과정 | 6 |
| Igjae Kim | 박사과정 | 7 |
| Chanshin Kwak | 박사과정 |  |
| Hongbeen Kim | 박사과정 | 3 |
| Jaehyeon Lee | 박사과정 | 6 |
| Daeun Kim | 박사과정 |  |
| Juhyun Lee | 박사과정 |  |
| Jeonghyeon Kim | 박사과정 |  |
| Shuangshuang Zhao | 박사과정 |  |
| Huanle Zhao | 박사과정 |  |
| Hyunmin Choi | 박사과정 | 1 |
| Yoonsung Kim | 박사과정 | 2 |
| Changjun Lee | 박사과정 | 5 |
| Guseul Heo | 박사과정 | 1, 3 |
| Jaehwan Lee | 박사과정 |  |
| Sukmin Cho | 박사과정 |  |
| Jeongwon Choi | 박사과정 |  |
| Wonung Kim | 박사과정 | 2 |
| Hyunjae Lee | 박사과정 |  |
| Janggun Lee | 박사과정 |  |
| Jonguk Jeon | 박사과정 |  |
| Siu Jeong | 박사과정 |  |
| Sieun Moon | 석사과정 |  |
| Dongha Kim | 석사과정 |  |
| Jaewon Jeong | 석사과정 |  |
| Junbong We | 석사과정 |  |
| Jimin Lee | 석사과정 |  |
| Sangin Jeon | 석사과정 |  |
| Yeongwook Kim | 석사과정 |  |
| Seungwuk Eun | 석사과정 |  |
| Jiyoung Jeong | 석사과정 |  |
| Jiyong Jung | 석사과정 | 2 |
| Subeen Park | 석사과정 |  |
| Juhyeong Kim | 석사과정 |  |
| Changyong Eom | 석사과정 |  |
| Seungjong Ha | 석사과정 |  |
| Hyunsu Ye | 석사과정 |  |
| Jin Heo | 석사과정 |  |
| Suhwan Kim | 석사과정 |  |
| Namwoo Kim | 석사과정 |  |
| Yeongmin Hwang | 석사과정 |  |
| Seonghun Jung | 석사과정 |  |
| Yelim Han | 석사과정 |  |
| Minjoo Kim | 석사과정 |  |
| Jihoon Kim | 석사과정 |  |

## 졸업생

랩 구성원 페이지의 Alumni 명단이다. 1974년부터의 졸업생과 옛 교수진이 이름만 실려 있고 학위·연도·진로는 적혀 있지 않다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Kyuho Park |  |  |
| Bumchun Lee |  |  |
| Seungkyu Park |  |  |
| Wonmo Hong |  |  |
| Namsung Woo |  |  |
| Byungki Kim |  |  |
| Seungryoul Maeng |  |  |
| Taisook Han |  |  |
| Yoonjun Lee |  |  |
| Dosoon Park |  |  |
| Youngtaek Park |  |  |
| Taemoo Jang |  |  |
| Bokkyu Joo |  |  |
| Seungbum Kim |  |  |
| Chulho Kim |  |  |
| Jongwon Park |  |  |
| Heesub Lee |  |  |
| Soonho Jung |  |  |
| Jong Kim |  |  |
| Yoonsik Lee |  |  |
| Ohan Kang |  |  |
| Nakwoon Sung |  |  |
| Kiseok Gong |  |  |
| Jinsoo Kim |  |  |
| Namseok Baek |  |  |
| Deukhwan Oh |  |  |
| Horae Lee |  |  |
| Yongwoon Kim |  |  |
| Boktae Bae |  |  |
| Gilhaeng Lee |  |  |
| Jaewoo Jang |  |  |
| Yoonsub Han |  |  |
| Seungwoon Park |  |  |
| Jungwoo Lee |  |  |
| Younghoon Kim |  |  |
| Sungyup Shin |  |  |
| Byungman Kim |  |  |
| Kyuhwan Sim |  |  |
| Youngsook Im |  |  |
| Ara Gil |  |  |
| Chunggeun Song |  |  |
| Hyunju Yoon |  |  |
| Jingeun Choi |  |  |
| Duktae Kim |  |  |
| Sangseok Shin |  |  |
| Sanghoon Lee |  |  |
| Sunmin Choi |  |  |
| Gilyoon Kim |  |  |
| Byungho Kim |  |  |
| Jinseok Kim |  |  |
| Dongmyung Choi |  |  |
| Kyungchul Kim |  |  |
| Jaehyung Park |  |  |
| Bumyoon Lee |  |  |
| Hyojung Song |  |  |
| Nara Won |  |  |
| Jaeman Kim |  |  |
| Kyungeun Lee |  |  |
| Myungkwon Cheon |  |  |
| Youngchul Son |  |  |
| Sungtak Lee |  |  |
| Wenam Kwon |  |  |
| Minsun An |  |  |
| Hosang Yoon |  |  |
| Inbum Jung |  |  |
| Sungki Jin |  |  |
| Moonsang Lee |  |  |
| Youngbae Jang |  |  |
| Yusung Kim |  |  |
| Seungtaek Oh |  |  |
| Sungwon Jeon |  |  |
| Jungwook Kang |  |  |
| Yeon No |  |  |
| Kyuyong Shin |  |  |
| Jungrok Yoo |  |  |
| Byungchun Jung |  |  |
| Inchul Hwang |  |  |
| Heeyeol Kim |  |  |
| Sanggeun Lee |  |  |
| Jinwon Lee |  |  |
| Jinwook Kim |  |  |
| Wonjae Lee |  |  |
| Junho Cho |  |  |
| Donghwan Kim |  |  |
| Youngjae Kim |  |  |
| Eunju Lee |  |  |
| Jongkwan Jung |  |  |
| Hakmin Kim |  |  |
| Eunkyu Byun |  |  |
| Donghyouk Lim |  |  |
| Min Lee |  |  |
| Yuseung Jung |  |  |
| Junbum Heo |  |  |
| Junghyun Kim |  |  |
| Youngjae Lee |  |  |
| Jaehoon Jung |  |  |
| Dongsung Kim |  |  |
| Hwanju Kim |  |  |
| Seungmin Jung |  |  |
| Jinho Seol |  |  |
| Yonggu Lee |  |  |
| Jaehong Kim |  |  |
| Hanbit Kim |  |  |
| Bonkeun Seo |  |  |
| Junghoon Lee |  |  |
| Changdae Kim |  |  |
| Jaewon Choi |  |  |
| Kunho Kim |  |  |
| Ganguk Lee |  |  |
| Jungi Jeong |  |  |
| Wonwik Seo |  |  |
| Seonjin Na |  |  |
| Jongyul Kim |  |  |
| Sunho Lee |  |  |
| Insub Baek |  |  |
| Moonjung Chung |  |  |
| Seungsoo Park |  |  |
| Byungchul Shin |  |  |
| Changhoon Lee |  |  |
| Yongman Kim |  |  |
| Haechul Im |  |  |
| Siyoung Hwang |  |  |
| Taewoo Jang |  |  |
| Byungkwan Park |  |  |
| Yoonsik Lee |  |  |
| Seohyun Jeon |  |  |
| Jihoon Kang |  |  |
| Younghoon Kim |  |  |
| Dongyeol Na |  |  |
| Sanggu Lee |  |  |
| Kyusik Jung |  |  |
| Taechung Jung |  |  |
| Daehwa Seo |  |  |
| Sunjung Choi |  |  |
| Sikwan Kim |  |  |
| Kyungtaek Jung |  |  |
| Kichul Kim |  |  |
| Jinho Kim |  |  |
| Jungbae Seo |  |  |
| Hosung Yoon |  |  |
| Seokho Kang |  |  |
| Jaeha Kim |  |  |
| Sanggu Seo |  |  |
| Hyogun Lee |  |  |
| Hanmo Cho |  |  |
| Myunghee Hong |  |  |
| Woogil Song |  |  |
| Youngpyo Jeon |  |  |
| Hyungchul Kim |  |  |
| Jaehoon Jung |  |  |
| Youngbok Park |  |  |
| Jongchul An |  |  |
| Moondon Joo |  |  |
| Donghoon Park |  |  |
| Byungik An |  |  |
| Youngmin Jung |  |  |
| Changmin Han |  |  |
| Seungwook Park |  |  |
| Sooyoung Yoon |  |  |
| Sungjun Lee |  |  |
| Seokryul Kang |  |  |
| Bumki Kim |  |  |
| Sungpyo Kim |  |  |
| Eunseok No |  |  |
| Junghwan Choi |  |  |
| Kyutaek Kim |  |  |
| Chanhee Park |  |  |
| Hyojung Hwang |  |  |
| Sangyup Oh |  |  |
| Jongmin Lee |  |  |
| Jongyeon Kim |  |  |
| Kiho Cho |  |  |
| Dongwook Kim |  |  |
| Kyuhwan Shin |  |  |
| Sihoon Cho |  |  |
| Manhee Kim |  |  |
| Byungchan An |  |  |
| Seokwon Lee |  |  |
| Hanjo Jung |  |  |
| Eunjin Kim |  |  |
| Sangkwon Lee |  |  |
| Jongwoong Hyun |  |  |
| Hyunchul Kim |  |  |
| Namyoon Woo |  |  |
| Sanghoon Jung |  |  |
| Namki Kim |  |  |
| Soyeon Park |  |  |
| Sunyoung Park |  |  |
| Heechul Yoon |  |  |
| Min Choi |  |  |
| Jungwook Kang |  |  |
| Euiseong Seo |  |  |
| Seunghak Lee |  |  |
| Hyungu Jung |  |  |
| Younghee Park |  |  |
| Uichin Lee |  |  |
| Kiseok Kwon |  |  |
| Sehoon Kim |  |  |
| Hojin Kim |  |  |
| Jaewan Jang |  |  |
| Hyeeun Choi |  |  |
| Donggeun Park |  |  |
| Daewoo Lee |  |  |
| Yongbon Koo |  |  |
| Seungmo Gu |  |  |
| Hanjin Lee |  |  |
| Heeseung Jo |  |  |
| Mikyung Kang |  |  |
| Hanjoon Kim |  |  |
| Hyeyeon Im |  |  |
| Jinkyu Jeong |  |  |
| Sang-Hoon Kim |  |  |
| Hyotaek Sim |  |  |
| Young-Sik Lee |  |  |
| Jiyong Shin |  |  |
| Jaeho Hwang |  |  |
| Sangwon Seo |  |  |
| Jung-Sang Ahn |  |  |
| Jungho Song |  |  |
| Jaeung Han |  |  |
| Sanghoon Cha |  |  |
| Sangjung Woo |  |  |
| Taehoon Kim |  |  |
| Hyung-Ho Choi |  |  |
| Taekyung Heo |  |  |
| Joongun Park |  |  |
| Daehyeon Baek |  |  |
| Minkyu Jung |  |  |
| Inchul Shin |  |  |
| Dongyoon Kim |  |  |
| Dongjae Choi |  |  |
| Kihyun Um |  |  |
| Sunki Hong |  |  |
| Jaejung Kim |  |  |
| Hyunsoo Choi |  |  |
| Byungsoo Park |  |  |
| Dongsoo Kim |  |  |
| Seok Park |  |  |
| Jongchang Lee |  |  |
| Injeong Chung |  |  |
| Sungwan Kim |  |  |
| Jinchun Kim |  |  |
| Younggil Park |  |  |
| Heungkyu Lee |  |  |
| Gyesung Lee |  |  |
| Jangsun Kim |  |  |
| Juwon Song |  |  |
| Euikyung Hong |  |  |
| Jiin Kim |  |  |
| Sangki Han |  |  |
| Jaemyung Kim |  |  |
| Youngkwang Nam |  |  |
| Jaedong Yang |  |  |
| Heongil Lee |  |  |
| Myungkyun Kim |  |  |
| Jun Kim |  |  |
| Dongwook Shin |  |  |
| Ikhyun Jang |  |  |
| Sungho Choi |  |  |
| Kiyeol Ryu |  |  |
| Sungbae Eun |  |  |
| Youngjo Jung |  |  |
| Jongho Nang |  |  |
| Namchul Heo |  |  |
| Eunyoung Son |  |  |
| Injae Lee |  |  |
| Minjae Hwang |  |  |
| Jaemin Park |  |  |
| Sangsoo Oh |  |  |
| Yongduk Cho |  |  |
| Jaechul Gong |  |  |
| Youngran Baek |  |  |
| Hosan Yoon |  |  |
| Naehoon Jung |  |  |
| Bosub Kwon |  |  |
| Byungchan Kim |  |  |
| Jiyoon Kim |  |  |
| Inyong Park |  |  |
| Youngjae Kang |  |  |
| Baekyung Park |  |  |
| Dongho Yoo |  |  |
| Sanghyun Park |  |  |
| Sungkyu Oh |  |  |
| Euihoon Jung |  |  |
| Byungkyu An |  |  |
| Jungyeon Cho |  |  |
| Eunkyung Park |  |  |
| Sangbum Lee |  |  |
| Sungmin Hong |  |  |
| Dohyun Park |  |  |
| Jaeheung Yeo |  |  |
| Yoonseok Lee |  |  |
| Minhwi Cho |  |  |
| Chulki Kim |  |  |
| Geunhwi Im |  |  |
| Sungwan Kim |  |  |
| Kwangwook Shin |  |  |
| Jaewon Lee |  |  |
| Woochul Kang |  |  |
| Hojoong Kim |  |  |
| Jungwoo Park |  |  |
| Jinsung Park |  |  |
| Wonjin Lee |  |  |
| Woosung Choi |  |  |
| Jinwook Kim |  |  |
| Donghyun Lee |  |  |
| Yoonho Lee |  |  |
| Sangwon Kim |  |  |
| Hyeyoung Yoon |  |  |
| Hyeyoung Jung |  |  |
| Dongwook Kim |  |  |
| Youngseok Kim |  |  |
| Eunji Pak |  |  |
| Dawoon Jung |  |  |
| Sooyoung Kim |  |  |
| Sangok Park |  |  |
| Byungho Lee |  |  |
| Jaegeuk Kim |  |  |
| Wook Jung |  |  |
| Yoonhee Chae |  |  |
| Junil Kwon |  |  |
| Hyungeol No |  |  |
| Seungmin Jung |  |  |
| Dongwon Kang |  |  |
| Sunhee Kim |  |  |
| Myeongjae Jeon |  |  |
| Youngjin Kwon |  |  |
| Youngsik Lee |  |  |
| Daehoon Kim |  |  |
| Seongwook Jin |  |  |
| Jeongseob Ahn |  |  |
| Jongse Park |  |  |
| Bokyeong Kim |  |  |
| Jinhyuk Kim |  |  |
| Kwangwon Koh |  |  |
| Chang Hyun Park |  |  |
| Jeongim Choi |  |  |
| Seikwon Kim |  |  |
| Jaeseong Im |  |  |
| Seungbeom Choi |  |  |
| Soojin Hwang |  |  |
| Daegil Im |  |  |
| Seungheun Jeon |  |  |
| Hyeon-Gi Jeon |  |  |
| Wonsang Kwak |  |  |
| Hyunwoo Jung |  |  |
| Yoonjae Jeon |  |  |
| Bokyung Cha |  |  |
| Jungwoo Kim |  |  |
| Seunghyo Kang |  |  |
| Gieun Jeong |  |  |
| Minwoo Noh |  |  |
| Kunhoon Baik |  |  |
| HaeJoon Lee |  |  |
| Taesoo Lee |  |  |
| Insu Jang |  |  |
| Taeksoo Kim |  |  |
| Dohee Kim |  |  |
| Yeaseul Park |  |  |
| Jinwon Pyo |  |  |
| Seonyoung Lee |  |  |
| Haechan An |  |  |
| Kanghyuk Lee |  |  |
| Jongwook Kim |  |  |
| Jaewook Woo |  |  |
| Sungjoon Park |  |  |
| Sukchul Cho |  |  |
| Jaewan Hong |  |  |
| Yeonjae Kim |  |  |
| Jinyoung Oh |  |  |
| Hyungjun Cho |  |  |
| Seongryong Oh |  |  |
| Woojin Lee |  |  |
| Tae Woo Kim |  |  |

## 최근 논문 목록 (2021–2026)

랩 국제 학술대회·국제 학술지 목록의 2021–2026년 논문 76편이다.[^papers]

**2026**

- Sangjin Choi, Sukmin Cho, Yifan Xiong, Ziyue Yang, Youngjin Kwon, Peng Cheng. "ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving". *ACM SIGOPS Annual Technical Conference(ATC), November, 2026*.
- Sunho Lee, Minwoo Noh, Jeongwon Choi, Kwanghoon Choi, Igjae Kim, Chang Hyun Park, and Jaehyuk Huh. "SecPIMlet: Confidential Computing for Spatio-temporally Shared Processing-in-Memory". *The 59th IEEE/ACM International Symposium on Microarchitecture (MICRO), October, 2026*.
- Sookyung Choi, Seungyong Lee, Kangkyu Park, Yunseo Chun, Junseok Lee, Hyeongseok Gwak, Myunghyun Rhee, Euiseok Kim, Donguk Moon, Kwangsik Shin, Guseul Heo, Youngpyo Joo, Hoshik Kim, Jongse Park. "NELSSA: A GPU–PNM Heterogeneous System for Mixed-Length LLM Serving via Length–based Request Placement". *The 59th IEEE/ACM International Symposium on Microarchitecture (MICRO), October, 2026*.
- Soojin Hwang, Sanghyeon Lee, Juhyun Lee, and Jaehyuk Huh. "A Hybrid Processing-in-Memory Architecture for Long Sequence LLM Inference with KV Cache Filtering". *The International Conference on Parallel Architectures and Compilation Techniques (PACT), October, 2026*.
- Jinghan Huang, Hongkun Zeng, Mike Montano, Jaehong Cho, Hyunmin Choi, Jinin So, Junhyeok Im, Handeok Lee, Jongse Park, Nam Sung Kim. "A Simulator for LLM Inference Systems Exploiting CXL Memory Pools". *IEEE Computer Architecture Letters (CAL), 2026*.
- Soojin Hwang, Sanghyeon Lee, Juhyun Lee, Jaehyuk Huh. "An Operand Divergence-Aware All-Bank PIM Architecture for Sparse Attention". *IEEE Computer Architecture Letters (CAL), 2026*.
- Siu Jeong, Suhwan Kim, Changyong Eom, Jaehyuk Huh. "Enabling Computation and Communication Overlap in PIMs for On-Device LLM Inference". *IEEE Computer Architecture Letters (CAL), 2026*.
- Jongyul Kim, Jaehwan Lee, Inhoe Koo, Peizhe Liu, Jiyuan Zhang, Junho Ahn, Tianyin Xu, Youngjin Kwon. "Oxbow: A Coordinated Architecture for Multi-component File Systems". *The 20th USENIX Symposium on Operating Systems Design and Implementation (OSDI), July, 2026*.
- Donghwan Kim, Xin Gu, Jinho Baek, Timothy Lo, Younghoon Min, Kwangsik Shin, Jongryool Kim, Jongse Park, Kiwan Maeng. "Cocoon: A System Architecture for Differentially Private Training with Correlated Noises". *The 20th USENIX Symposium on Operating Systems Design and Implementation (OSDI), July, 2026*.
- Hanyang Xu, SeongRyong Oh, Yubin Lee, Ashwin Rohit Alagiri Rajan, Rohan Mahapatra, Om Patil, Yuchuan Li, Jongse Park, Hadi Esmaeilzadeh. "Accelerator Polymorphism: Transcending Domain-Specific Architectures with Robotics". *The 53rd International Symposium on Computer Architecture (ISCA), June, 2026*.
- Jeonghyeon Kim, Jongse Park, Youngjin Kwon, Jeehoon Kang. "Revisiting Partial Tracing for Safe, Efficient, and Concurrent Garbage Collection in Unmanaged Languages". *The 47th ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI), June, 2026*.
- Hyunjae Lee, Sangjin Choi, Seungjae Lim, Youngjin Kwon. "BEAM: Joint Resource–Power Optimization for Energy-Efficient LLM Inference under SLO contraints". *9th Annual Conference on Machine Learning and Systems (MLSys), May, 2026*.
- Jaehong Cho, Hyunmin Choi, Guseul Heo, Jongse Park. "LLMServingSim 2.0: A Unified Simulator for Heterogeneous and Disaggregated LLM Serving Infrastructure". *IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS), April, 2026*.
- Jinwoo Hwang, Yeongmin Hwang, Tadiwos Meaza, Hyeonbin Bae, Jongse Park. "Understanding the Performance Behaviors of End-to-End Protein Design Pipelines on GPUs". *IEEE Computer Architecture Letters (CAL), 2026*.
- Minkyu Jung, Chanshin Kwak, Junho Ahn, Sunho Park, Changjun Lee, Jongyul Kim, Jeehoon Kang, Youngjin Kwon. "CofferOS: Hardening OS-level Virtualization with Rust". *European Conference on Computer Systems (EuroSys), April, 2026*.
- Changjun Lee, Sangjin Choi, Youngjin Kwon. "MTTM: Dynamic Fast Memory Partitioning with Bandwidth Optimization for Multi-tenant Cloud". *European Conference on Computer Systems (EuroSys), April, 2026*.
- Chanshin Gwak, Jaehyun Lee, Minkyu Jung, Youngjin Kwon. "BASK: Batch And SmartNIC-offloaded KSM". *European Conference on Computer Systems (EuroSys), April, 2026*.
- Changhun Oh, Seongryong Oh, Jinwoo Hwang, Yoonsung Kim, Hardik Sharma, Jongse Park. "Neo: Real-Time On-Device 3D Gaussian Splatting with Reuse-and-Update Sorting Acceleration". *the ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS), March, 2026*.
- Dongjae Lee\*, Bongjoon Hyun\*, Youngjin Kwon, Minsoo Rhu. "PIM-malloc: A Fast and Scalable Dynamic Memory Allocator for Processing-In-Memory (PIM) Architectures". *the 32nd IEEE International Symposium on High-Performance Computer Architecture (HPCA), January, 2026*.

**2025**

- Jaehong Cho, Hyunmin Choi, Jongse Park. "LLMServingSim2.0: A Unified Simulator for Heterogeneous Hardware and Serving Techniques in LLM Infrastructure". *IEEE Computer Architecture Letters (CAL), 2025*.
- Sanghyeon Lee, Hongbeen Kim, Soojin Hwang, Guseul Heo, Minwoo Noh, Jaehyuk Huh. "Throughput-Oriented LLM Inference via KV-Activation Hybrid Caching with a Single GPU". *The 43rd IEEE International Conference on Computer Design (ICCD), November, 2025*.
- Juncheol Ye, Seungkook Lee, Hwijoon Lim, JiHyuk Lee, Uitaek Hong, Youngjin Kwon, Dongsu Han. "SAND: A New Programming Abstraction for Video-based Deep Learning". *the 31st Symposium on Operating Systems Principles (SOSP), October, 2025*.
- Tae Woo Kim, Youngjin Kwon, Jeehoon Kang. "Scalable Address Spaces using Concurrent Interval Skiplist". *the 31st Symposium on Operating Systems Principles (SOSP), October, 2025*.
- Wonung Kim, Yubin Lee, Yoonsung Kim, Jinwoo Hwang, Seongryong Oh, Jiyong Jung, Aziz Huseynov, Woong Gyu Park, Chang Hyun Park, Divya Mahajan, Jongse Park. "Pimba: A Processing-in-Memory Acceleration for Post-Transformer Large Language Model Serving". *the 58th IEEE/ACM International Symposium on Microarchitecture (MICRO), October, 2025*.
- Wonhyuk Yang, Yunseon Shin, Okkyun Woo, Geonwoo Park, Hyungkyu Ham, Jeehoon Kang, Jongse Park, Gwangsun Kim. "PyTorchSim: A Comprehensive, Fast, and Accurate NPU Simulation Framework". *the 58th IEEE/ACM International Symposium on Microarchitecture (MICRO), October, 2025*.
- Jinwoo Hwang, Daeun Kim, Sangyeop Lee, Yoonsung Kim, Guseul Heo, Hojoon Kim, Yunseok Jeong, Tadiwos Meaza, Eunhyeok Park, Jeongseob Ahn, Jongse Park. "Déjà Vu: Efficient Video-Language Query Engine with Learning-based Inter-Frame Computation Reuse". *the 51st International Conference on Very Large Databases (VLDB), September, 2025*.
- Daeun Kim, Jinwoo Hwang, Changhun Oh, Jongse Park. "MixDiT: Accelerating Image Diffusion Transformer Inference with Mixed-Precision MX Quantization". *IEEE Computer Architecture Letters (CAL), 2025*.
- Sunho Lee, Seonjin Na, Jeongwon Choi, Jinwon Pyo, and Jaehyuk Huh. "Unified Memory Protection with Multi-granular MAC and Integrity Tree for Heterogeneous Processors". *the 52nd International Symposium on Computer Architecture (ISCA), June, 2025*.
- Minsu Kim, Seongmin Hong, RyeoWook Ko, Soongyu Choi, Hunjong Lee, Junsoo Kim, Joo-Young Kim, Jongse Park. "Oaken: Fast and Efficient LLM Serving with Online-Offline Hybrid KV Cache Quantization". *the 52nd International Symposium on Computer Architecture (ISCA), June, 2025*.
- Junho Ahn, KangHyuk Lee, Chanyoung Park, Hyungon Moon, Youngjin Kwon. "Defeating Use-After-Free Bugs Using Memory Sweeper Without Stop-the-World". *IEEE Symposium on Security and Privacy (S&P), May, 2025*.
- Sukmin Cho, Sangjin Choi, Taeho Hwang, Jeongyeon Seo, Soyeong Jeong, Huije Lee, Hoyun Song, Jong C. Park, Youngjin Kwon. "Lossless Acceleration of Large Language Models with Hierarchical Drafting based on Temporal Locality in Speculative Decoding". *The 2025 Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics (NAACL), April, 2025*.
- Wonsup Yoon, Jisu Ok, Sue Moon, Youngjin Kwon. "Adios to Busy-Waiting for Microsecond-scale Memory Disaggregation". *European Conference on Computer Systems (EuroSys), March, 2025*.
- Kwanghoon Choi, Igjae Kim, Sunho Lee, and Jaehyuk Huh. "ShieldCXL: A Practical Obliviousness Support with Sealed CXL Memory". *ACM Transactions on Architecture and Code Optimization (TACO), 2025*.

**2024**

- Yeonjae Kim, Igjae Kim, Kwanghoon Choi, Jeongseob Ahn, Jongse Park, Jaehyuk Huh. "Interference-Aware DNN Serving on Heterogeneous Processors in Edge Systems". *The 42nd IEEE International Conference on Computer Design (ICCD), November, 2024*.
- Dae R. Jeong, Yewon Choi, Byoungyoung Lee, Insik Shin, Youngjin Kwon. "OZZ: Identifying Kernel Out-of-Order Concurrency Bugs with In-Vivo Memory Access Reordering". *the 30th Symposium on Operating Systems Principles (SOSP), November, 2024, Best Paper Award*.
- Jaehong Cho, Minsu Kim, Hyunmin Choi, Guseul Heo, Jongse Park. "LLMServingSim: A HW/SW Co-Simulation Infrastructure for LLM Inference Serving at Scale". *the 2024 IEEE International Symposium on Workload Characterization (IISWC), September, 2024*.
- Seungjae Moon, Jung-Hoon Kim, Junsoo Kim, Seongmin Hong, Junseo Cha, Minsu Kim, Sukbin Lim, Gyubin Choi, Dongjin Seo, Jongho Kim, Hunjong Lee, Hyunjun Park, Ryeowook Ko, Soongyu Choi, Jongse Park, Jinwon Lee, Joo-Young Kim. "LPU: A Latency-optimized and Highly Scalable Processor for Large Language Model Inference". *IEEE Micro, Special Issue on Contemporary Industry Products, 2024*.
- Junho Ahn, Jaehyeon Lee, KangHyuk Lee, Wooseok Gwak, Minseong Hwang, Youngjin Kwon. "BUDAlloc: Defeating Use-After-Free Bugs by Decoupling Virtual Address Management from Kernel". *the 33rd USENIX Security Symposium, August, 2024*.
- Minsu Kim, Jinwoo Hwang, Guseul Heo, Seiyeon Cho, Divya Mahajan, Jongse Park. "Accelerating String-key Learned Index Structures via Memoization-based Incremental Training". *the 50th International Conference on Very Large Databases (VLDB), August, 2024*.
- Daehyeon Baek, Soojin Hwang, and Jaehyuk Huh. "pSyncPIM: Partially Synchronous Execution of Sparse Matrix Operations for All-bank PIM Architectures". *the 51st International Symposium on Computer Architecture (ISCA), June, 2024*.
- Yoonsung Kim, Changhun Oh, Jinwoo Hwang, Wonung Kim, Seongryong Oh, Yubin Lee, Hardik Sharma, Amir Yazdanbakhsh, Jongse Park. "DaCapo: Accelerating Continuous Learning in Autonomous Systems for Video Analytics". *the 51st International Symposium on Computer Architecture (ISCA), June, 2024, Distinguished Artifact Award*.
- Guseul Heo, Sangyeop Lee, Jaehong Cho, Hyunmin Choi, Sanghyeon Lee, Hyungkyu Ham, Gwangsun Kim, Divya Mahajan, Jongse Park. "NeuPIMs: NPU-PIM Heterogeneous Acceleration for Batched LLM Inferencing". *the ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS), April, 2024*.
- Soroush Ghodrati, Sean Kinzer, Hanyang Xu, Rohan Mahapatra, Yoonsung Kim, Byung Hoon Ahn, Dong Kai Wang, Lavanya Karthikeyan, Amir Yazdanbakhsh, Jongse Park, Nam Sung Kim, Hadi Esmaeilzadeh. "Tandem Processor: Grappling with Emerging Operators in Neural Networks". *the ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS), April, 2024*.
- Seonjin Na, Jungwoo Kim, Sunho Lee, and Jaehyuk Huh. "Supporting Secure Multi-GPU Computing with Dynamic and Batched Metadata Management". *the 30th IEEE International Symposium on High-Performance Computer Architecture (HPCA), March, 2024*.
- Soojin Hwang, Daehyeon Baek, Jongse Park, and Jaehyuk Huh. "Cerberus: Triple Mode Acceleration of Sparse Matrix and Vector Multiplication". *ACM Transactions on Architecture and Code Optimization (TACO), 2024*.
- Joongun Park, Seunghyo Kang, Sanghyeon Lee, Taehoon Kim, Jongse Park, Youngjin Kwon, and Jaehyuk Huh. "Hardware Hardened Sandbox Enclaves for Trusted Serverless Computing". *IEEE Transactions on Architecture and Code Optimization (TACO), 2024*.

**2023**

- \*Soojin Hwang, \*Sunho Lee, Jungwoo Kim, Hongbeen Kim, Jaehyuk Huh. "mNPUsim: Evaluating the Effect of Sharing Resources with Multi-Core NPUs". *the 2023 IEEE International Symposium on Workload Characterization (IISWC), October, 2023 (\* co-first authors)*.
- Jungwoo Kim, Seonjin Na, Sanghyeon Lee, Sunho Lee, and Jaehyuk Huh. "Improving Data Reuse in NPU On-chip Memory with Interleaved Gradient Order for DNN Training". *the 56th IEEE/ACM International Symposium on Microarchitecture (MICRO), October, 2023*.
- Jaehoon Heo, Yongwon Shin, Sangjin Choi, Sungwoong Yune, Jung-Hoon Kim, Hyojin Sung, Youngjin Kwon, Joo-Young Kim. "PRIMO: A Full-Stack Processing-in-DRAM Emulation Framework for Machine Learning Workloads". *International Conference on Computer-Aided Design (ICCAD), October, 2023*.
- Sangjin Choi, Inhoe Koo, Jeongseob Ahn, Myeongjae Jeon, Youngjin Kwon. "EnvPipe: Performance-preserving DNN Training Framework for Saving Energy". *USENIX Annual Technical Conference (ATC), July, 2023*.
- Dae R. Jeong, Byoungyoung Lee, Insik Shin, Youngjin Kwon. "SEGFUZZ: Segmentizing Thread Interleaving to Discover Kernel Concurrency Bugs through Fuzzing". *IEEE Symposium on Security and Privacy (S&P), May, 2023*.
- Dae R. Jeong, Minkyu Jung, Yoochan Lee, Byoungyoung Lee, Insik Shin, Youngjin Kwon. "Diagnosing Kernel Concurrency Failures with AITIA". *European Conference on Computer Systems (EuroSys), May, 2023*.
- Wonsup Yoon, Jisu Ok, Jinyoung Oh, Sue Moon, Youngjin Kwon. "DiLOS: Do Not Trade Compatibility for Performance in Memory Disaggregation". *European Conference on Computer Systems (EuroSys), May, 2023*.
- Taehyun Kim, Deondre Martin Ng, Junzhi Gong, Youngjin Kwon, Minlan Yu, KyoungSoo Park. "Rearchitecting the TCP Stack for I/O-Offloaded Content Delivery". *USENIX Symposium on Networked Systems Design and Implementation (NSDI), April, 2023*.
- Seock-Hwan Noh, Jahyun Koo, Seunghyun Lee, Jongse Park, Jaeha Kung. "FlexBlock: A Flexible DNN Training Accelerator with Multi-Mode Block Floating Point Support". *IEEE Transactions on Computers (TC), 2023*.
- Seonho Lee, Ranggi Hwang, Jongse Park, Minsoo Rhu. "HAMMER: Hardware-friendly Approximate Computing for Self-attention with Mean-redistribution and Linearization". *IEEE Computer Architecture Letters (CAL), 2023*.

**2022**

- Bokyeong Kim, Soojin Hwang, Sanghoon Cha, Chang Hyun Park, Jongse Park, and Jaehyuk Huh. "Supporting Dynamic Translation Granularity for Hybrid Memory Systems". *The 40th IEEE International Conference on Computer Design (ICCD), October, 2022*.
- Sunho Lee, Seonjin Na, Jungwoo Kim, Jongse Park, and Jaehyuk Huh. "Tunable Memory Protection for Secure Neural Processing Units". *The 40th IEEE International Conference on Computer Design (ICCD), October, 2022*.
- Joon Kyung Kim, Byung Hoon Ahn, Sean Kinzer, Soroush Ghodrati, Rohan Mahapatra, Brahmendra Yatham, Dohee Kim, Parisa Sarikhani, Babak Mahmoudi, Divya Mahajan, Jongse Park, Hadi Esmaeilzadeh. "Yin-Yang: Programming Abstraction for Cross-Domain Multi-Acceleration". *IEEE Micro, special issue on Compiling for Accelerators, 2022*.
- Jaeseong Im, Jongyul Kim, Youngjin Kwon, Seungryoul Maeng. "On-demand Virtualization for Post-copy OS Migration in Bare-metal Cloud". *IEEE Transactions on Cloud Computing (TCC), 2022*.
- Jinwoo Hwang, Minsu Kim, Daeun Kim, Seungho Nam, Yoonsung Kim, Dohee Kim, Hardik Sharma, and Jongse Park. "CoVA: Exploiting Compressed-Domain Analysis to Accelerate Video Analytics". *USENIX Annual Technical Conference (ATC), July 2022*.
- Seungbeom Choi, Sunho Lee, Yeonjae Kim, Jongse Park, Youngjin Kwon, and Jaehyuk Huh. "Serving Heterogeneous Machine Learning Models on Multi-GPU Servers with Spatio-Temporal Sharing". *USENIX Annual Technical Conference (ATC), July 2022*.
- Sangjin Choi\*, Taeksoo Kim\*, Jinwoo Jeong, Rachata Ausavarungniurn, Myeongjae Jeon, Youngjin Kwon, Jeongsub Ahn. "Memory Harvesting in Multi-GPU Systems with Hierarchical Unified Virtual Memory". *USENIX Annual Technical Conference (ATC), July 2022, (\*Co-first author)*.
- Sunho Lee, Jungwoo Kim, Seonjin Na, Jongse Park, and Jaehyuk Huh. "TNPU: Supporting Trusted Execution with Tree-less Integrity Protection for Neural Processing Unit". *the 28th IEEE International Symposium on High-Performance Computer Architecture (HPCA), April 2022*.

**2021**

- Jongyul Kim, Insu Jang, Waleed Reda, Jaeseong Im, Marco Canini, Dejan Kostic, Youngjin Kwon, Simon Peter, Emmett Witchel. "LineFS: Efficient SmartNIC Offload of a Distributed File System with Pipeline Parallelism". *Symposium on Operating Systems Principles (SOSP), October 2021, Best Paper Award*.
- Wonsup Yoon, Jinyoung Oh, Jisu Ok, Sue Moon, Youngjin Kwon. "DiLOS: Adding Performance to Paging-based Memory Disaggregation". *Asia-Pacific Workshop on Systems (APSys), August 2021*.
- Kyoungho Koo, Joontaek Oh, Kwangwon Min, Youngjin Kwon, Youjip Won. "C2J: Compulsory Compound Transaction for Journaling Filesystem". *Asia-Pacific Workshop on Systems (APSys), August 2021*.
- Jinyoung Oh, Youngjin Kwon. "Persistent Memory Aware Performance Isolation with Dicio". *Asia-Pacific Workshop on Systems (APSys), August 2021*.
- Daehyeon Baek, Soojin Hwang, Taekyung Heo, Daehoon Kim, and Jaehyuk Huh. "InnerSP: A Memory Efficient Sparse Matrix Multiplication Accelerator with Locality-aware Inner Product Processing". *accepted for the 30th International Conference on Parallel Architectures and Compilation Techniques (PACT), September 2021*.
- Gangmuk Lim, Jeongseob Ahn, Wencong Xiao, Youngjin Kwon, Myeongjae Jeon. "Zico: Efficient GPU Memory Sharing for Concurrent DNN Training". *USENIX Annual Technical Conference (ATC), Virtual Event, July 2021*.
- Yeonju Ro, Seongwook Jin, Jaehyuk Huh, and John Kim. "Ghost Routing to Enable Oblivious Computation on Memory-centric Networks". *The 48th International Symposium on Computer Architecture (ISCA), June, 2021*.
- Jungi Jeong, Jaewan Hong, Seungryoul Maeng, Changhee Jung, Youngjin Kwon. "Unbounded Hardware Transactional Memory for a Hybrid DRAM/NVM Memory System". *Non-Volatile Memories Workshop (NVMW), March 2021*.
- Taekyung Heo, Yang Wang, Wei Cui, Jaehyuk Huh, and Lintao Zhang. "Adaptive Page Migration Policy with Huge Pages in Tiered Memory Systems". *accepted for IEEE Transactions on Computers (TC)*.
- Wonik Seo, Sanghoon Cha, Yeonjae Kim, Jaehyuk Huh, and Jongse Park. "SLO-aware Inference Scheduler for Heterogeneous Processors in Edge Platforms". *accepted for ACM Transactions on Architecture and Code Optimization (TACO), 2021*.
- Seonjin Na, Sunho Lee, Yeonjae Kim, Jongse Park, and Jaehyuk Huh. "Common Counters: Compressed Encryption Counters for Secure GPU Memory". *accepted for the 27th IEEE International Symposium on High-Performance Computer Architecture (HPCA), Feburary 2021*.
- Ian Neal, Gefei Zuo, Eric Shiple, Tanvir Ahmed Khan, Youngjin Kwon, Simon Peter, Baris Kasikci. "Rethinking File Mapping for Persistent Memory". *USENIX Conference on File and Storage Technologies (FAST), February, 2021*.

## 연구 과제

랩 과제 페이지의 과제 69건과 지원 기관, 기간이다.[^projects]

- 차세대 HW 기술중심의 저지연·고확장성을 제공하는 분산파일 시스템 개발 (지원 한국연구재단; 기간 2020.03 ~ 2023.02)
- 이종 클라우드 시스템을 위한 SW-HW 융합 연구 (지원 한국연구재단; 기간 2019.06 ~ 2022.02)
- 차세대 공유/혼성 메모리 기반 통합 데이터 모델을 제공하는 메모리 중심 운영체제 기술개발 (지원 과학기술정보통신부; 기간 2019.04 ~ 2022.12)
- Non Von-Neumann Architecture (지원 삼성전자; 기간 2018.05 ~ 2020.04)
- GPU 기반의 기계학습 플랫폼을 위한 시스템 SW 연구 (지원 과학기술정보통신부; 기간 2017.09 ~ 2020.12)
- (SW 스타랩)신뢰할 수 있는 서비스 중심의 클라우드 소프트웨어 연구 (지원 미래창조과학부; 기간 2017.04 ~ 2021.03)
- 하드웨어 기반 악성 행위 탐지 및 방어 기법 (지원 삼성전자; 기간 2015.07 ~ 2020.06)
- 비휘발성 메모리를 위한 가상화 기반 분산 메모리 확장 기술 연구 (지원 SK Hynix; 기간 2018.02 ~ 2019.01)
- 고성능 클라우드 시스템을 위한 SW-HW 융합 연구 (지원 한국연구재단; 기간 2016.06 ~ 2019.05)
- 가상화 및 비가상화 시스템을 혼용하는 새로운 클라우드 모델 개발 (지원 한국연구재단; 기간 2016.06 ~ 2019.05)
- 랙스케일 기계학습 서비스를 위한 이론/시스템 융합연구 (지원 공과대학 Initiative 융합연구; 기간 2016.06 ~ 2016.12)
- UX 지향 모바일 SW 플랫폼 개발 (지원 지식경제부; 기간 2011.12 ~ 2016.08)
- 클라우드 컴퓨팅을 위한 미래 멀티코어 아키텍처 연구 (지원 한국연구재단; 기간 2013.05 ~ 2016.04)
- 뉴로몰픽 시뮬레이션 응용 개선을 통한 슈퍼컴퓨팅 개발 방향 전략 연구 (지원 KAIST; 기간 2015.11 ~ 2016.03)
- 하이브리드 메모리를 위한 HW 및 SW 시스템 지원 방안 연구 (지원 SK하이닉스; 기간 2015.03 ~ 2016.02)
- HBM(High Bandwidth Memory)를 위한 멀티 코어 아키텍처 연구 (지원 SK하이닉스; 기간 2015.03 ~ 2016.02)
- 모바일 사파리 보안위협 검증 기술 연구 (지원 국가보안기술연구소; 기간 2015.04 ~ 2015.11)
- 사용자 인터랙션 중심의 스마트폰 에너지 관리 기술 연구 (지원 한국연구재단; 기간 2012.05 ~ 2015.04)
- 메모리가 집적된 테라바이트 밴드폭 3차원 반도체 설계 및 테스트 방법론 연구 (지원 SK하이닉스; 기간 2013.10 ~ 2014.09)
- 에너지 효율을 고려한 이종 멀티 코어 모바일 프랫폼 기술연구 (지원 LG전자; 기간 2013.05 ~ 2014.04)
- 신뢰성 컴퓨팅(Trustworthy Computing) 기반 기술 개발 (지원 지식경제부; 기간 2009.03 ~ 2013.02)
- 모바일 플랫폼 취약점 기반기술 연구 (지원 국가보안기술연구소; 기간 2012.04 ~ 2012.11)
- 미래 매니 코어에서 코어간 성능 편차가 소프트웨어 시스템에 미치는 영향 연구 (지원 마이크로소프트; 기간 2011.10 ~ 2012.06)
- 미래 멀티코어와 시스템 가상화 기술의 융합 연구 (지원 한국연구재단; 기간 2010.09 ~ 2012.08)
- Touch & Search 웹 검색 서버 아키텍처 기술 개발 (지원 삼성전자; 기간 2010.03 ~ 2010.10)
- 사이언스 클라우드를 위한 가상 자원 관리 기술 연구 (지원 한국과학기술정보연구원; 기간 2011.02 ~ 2011.09)
- Linux 기반 Open Platform을 위한 신뢰성 컴퓨팅 기술 개발 (지원 삼성전자; 기간 2010.03 ~ 2010.12)
- 멀티 코어 및 이종 컴퓨팅 환경에서의 과학계산용 가상화 기술 연구 (지원 한국과학기술정보연구원; 기간 2010.02 ~ 2010.09)
- HLNAND에 최적화된 FTL 및 I/O Scheduler 구조 개발 (지원 INDILINX; 기간 2008.01 ~ 2008.12)
- 재구성 가능한 무선 단말을 위한 SCA 코어 프레임워크 연구 (지원 ITRC; 기간 2008.01 ~ 2008.12)
- 스토리지 접근 패턴에 따른 NAND FTL 기술 개발 (지원 KOSEF; 기간 2007.07 ~ 2008.06)
- Research on Storage System Technology for Large-scale Internet Service (지원 KOSEF; 기간 2007.07 ~ 2009.06)
- 네트워크 융합 모바일 플랫폼을 위한 임베디드 소프트웨어 기술 (지원 ITRC; 기간 2006.09 ~ 2009.09)
- Development of Hard Real-time Supporting Technique for Micro/Low-power Embedded Operating System, DSRC (지원 ADD; 기간 2006.07 ~ 2011.12)
- A Distributed Storage System for Large-scale Online Portal Sites (지원 NHN; 기간 2006.05 ~ 2009.03)
- Research on Embedded Systems for Next Generation Mobile Devices (지원 KOSEF Ministry of Science and Technology; 기간 2006.03 ~ 2009.02)
- A Platform Development for Ubiquitous/Embedded Systems (지원 ITRC; 기간 2003.08 ~ 2011.07)
- Research on tools for performance and stability of embedded SW (지원 ITRC)
- Virtualiation-based management technique for enforcing system stability (지원 KRF)
- Research on NAND Flash File System for Portable Devices (지원 Samsung; 기간 2006.10 ~ 2007.10)
- Fast Startup of DTV System Using Suspend and Resume (지원 Samsung; 기간 2006.04 ~ 2007.03)
- Real-time Performance Improvement of Embedded Linux Kernel (지원 ETRI; 기간 2006.09 ~ 2007.01)
- Digital TV Program Optimization (지원 Samsung; 기간 2005.04 ~ 2006.03)
- Performance Measurement of Real-time Operating System (지원 ETRI; 기간 2005.07 ~ 2005.11)
- Development of Cluster Computing Standard Prototype (지원 KISTI; 기간 2004.05 ~ 2004.12)
- Development of High Performance Cluster Computer (지원 Natonal Research Laboratory; 기간 1999.09 ~ 2004.09)
- Plant Monitoring/Controlling System (지원 LG Honeywell; 기간 1996 ~ 1997)
- Design and Implementation of Parallel Randering System on Distributed-Memory, Message-Passing Multicomputer (기간 1995 ~ 1996)
- Development of Security System for Communication with Public-Key Method (기간 1994 ~ 1996)
- Development of Techiniques for Connectionless Service with Public-Key Method (기간 1994 ~ 1996)
- Development of Techiniques for Connectionless Service for ATM Lan (기간 1994 ~ 1996)
- Design and Implementation of Multiprossor with Shared-Memory using SCI (기간 1993 ~ 1996)
- Research on Large-Capacity, Fault-Tolerent ATM Switch (기간 1993 ~ 1996)
- Development of a Parallel Computer Using Scalable Coherent Interface (지원 CAIR; 기간 1993 ~ 1995)
- Development of a Hardware Router for High Performance Multicomputers (지원 KAIST; 기간 1993 ~ 1995)
- Research on Design and Implementation of High-Performance Parallel Computer (기간 1992 ~ 1996)
- Development of a Recursive Ring Structured Massively Parallel Computer (지원 Ministry of Science and Technology; 기간 1992 ~ 1995)
- Design and Implementation of Interface Board for Video and Audio Data Processing (기간 1991 ~ 1993)
- Research on Wireless Communication on Intelligent Notepad Computer (기간 1991 ~ 1993)
- Research on General-purpose Parallel Neuro-Computer (기간 1991 ~ 1993)
- Research on Message Routing Technique and Performance Evaluation of Transputer-based Multicomputer (기간 1991 ~ 1992)
- Design and Implementation of RISC Microprocessor Chip with VLSI Technique and Related Systems (기간 1990 ~ 1994)
- The Design of PC Chipset Microcode (기간 1990 ~ 1994)
- Research on Test of Protocol Correctness (기간 1990 ~ 1991)
- Research on Computer System Architecture for Processing Multimedia and Knowledge Information (기간 1990 ~ 1991)
- Parallel Simulation System for Neural Network Model (기간 1989 ~ 1990)
- Parallel Processing System based on Logic Language (기간 1989 ~ 1990)
- Research on Object Oriented Operating System Architecture (기간 1989 ~ 1990)
- The Development of Next Generation Computer System (기간 1984 ~ 1989)

## 연락과 위치

- 연구실 이메일: info@casys.kaist.ac.kr, 전화 042-350-7719[^contact]
- 교수실: 전산학부 연구실 소개는 E3-1동 4406호(허재혁), 4405호(권영진), 4403호(박종세), 대표 전화 042-350-3580으로 적는다.[^cs]
- 주소: KAIST 전산학부, 대전 유성구 대학로 291[^contact]

[^home]: CASys 누리집 첫 화면 <https://casyslab.kaist.ac.kr/> (2026-10-19 열람)
[^research]: CASys 연구 페이지 <https://casyslab.kaist.ac.kr/research> (2026-10-19 열람)
[^members]: CASys 구성원 페이지 <https://casyslab.kaist.ac.kr/members> (2026-10-19 열람)
[^papers]: CASys 논문 목록(국제 학술대회·국제 학술지) <https://casyslab.kaist.ac.kr/publications/international-conference> 외 (2026-10-19 열람)
[^projects]: CASys 과제 페이지 <https://casyslab.kaist.ac.kr/projects> (2026-10-19 열람)
[^contact]: CASys 연락처 <https://casyslab.kaist.ac.kr/contact> (2026-10-19 열람)
[^cs]: KAIST 전산학부 연구실 소개(컴퓨터구조 및 시스템 연구실) <https://cs.kaist.ac.kr/research/labView?sn=57&menu=64> (2026-10-20 열람)
[^faculty]: KAIST 전산학부 교수진(시스템·네트워크) <https://cs.kaist.ac.kr/people/facultySystemsNetworks> (2026-10-20 열람)
[^p1]: G. Heo 외, J. Park, Proceedings of the 29th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 3, 722-737 (온라인 2024-04-27). <https://doi.org/10.1145/3620666.3651380> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p2]: W. Kim 외, J. Park, Proceedings of the 58th IEEE/ACM International Symposium on Microarchitecture, 292-307 (온라인 2025-10-17). <https://doi.org/10.1145/3725843.3756121> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: S. Lee 외, J. Huh, 2025 IEEE 43rd International Conference on Computer Design (ICCD), 269-276 (2025). <https://doi.org/10.1109/iccd65941.2025.00045> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: W. Yoon 외, Y. Kwon, Proceedings of the Eighteenth European Conference on Computer Systems, 266-282 (온라인 2023-05-08). <https://doi.org/10.1145/3552326.3567488> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: C. Lee, S. Choi, Y. Kwon, Proceedings of the 21st European Conference on Computer Systems, 1912-1927 (온라인 2026-04-26). <https://doi.org/10.1145/3767295.3769371> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: J. Ahn 외, Y. Kwon, USENIX Security Symposium 2024 (2024). <https://casyslab.kaist.ac.kr/publications/international-conference> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p7]: K. Choi, I. Kim, S. Lee, J. Huh, ACM Transactions on Architecture and Code Optimization 22, 1-25 (온라인 2025-03-20). <https://doi.org/10.1145/3703354> 초록 기준.

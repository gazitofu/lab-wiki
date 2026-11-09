# KAIST OS Lab (Operating Systems Laboratory)

**KAIST 전기및전자공학부 · 원유집 교수**

- 분야: 운영체제, 파일시스템, 저장 시스템, 다중 코어 성능 확장, 저장장치 안에서 하는 계산
- 대분야: 컴퓨팅·AI
- 태그: 컴퓨터 구조·운영체제[^research][^prof], 저장 시스템·SSD[^research][^prof]
- 홈페이지: <https://oslab.kaist.ac.kr>
- 근거와 출처: [KAIST OS Lab 근거 페이지](oslab-sources.md)

> 컴퓨터가 자료를 저장하고 읽는 경로와 여러 작업의 실행 방식을 설계해, 스마트폰부터 서버까지 계산 속도와 에너지 효율을 높이는 연구실이다.[^research]

## 무엇을 연구하나

KAIST OS Lab은 원유집 교수가 이끄는 운영체제(컴퓨터 자원을 관리하고 프로그램의 실행을 제어하는 기본 소프트웨어) 연구실이다. 연구실은 누리집에 Operating Systems Laboratory라는 이름을 함께 쓰며, 전기및전자공학부는 「운영체제 연구실」로 소개한다.[^home][^dept] 연구 소개는 스마트폰부터 많은 계산 장치를 갖춘 서버(다른 컴퓨터의 요청에 따라 자료나 서비스를 제공하는 컴퓨터)까지 여러 계산 환경을 다루고, 운영체제 내부의 동작을 이해해 속도와 에너지 효율을 높이는 일을 목표로 제시한다.[^research]

중심 대상은 파일시스템(파일의 이름·내용·위치와 저장 공간의 배치를 관리하는 체계)과 저장장치 관리 소프트웨어다. 플래시 저장장치(전원을 꺼도 자료가 남고 묶음 단위로 지운 뒤 다시 쓰는 반도체 저장장치)에 맞춘 파일시스템을 설계하고, 비휘발성 메모리(전원을 꺼도 저장한 내용을 유지하는 기억 장치)를 소프트웨어에서 다루는 방법을 개발한다. 연구실이 소개하는 HEAPO는 비휘발성 메모리를 관리하는 과정에서 파일시스템의 부가 작업을 줄이는 소프트웨어 계층이며, NVRAMDISK는 여러 변경을 전부 반영하거나 전부 취소하는 성질을 갖춘 저장장치 제어 소프트웨어다.[^research]

여러 계산 장치가 함께 일할 때 계산 성능이 확장되는 방법도 연구한다. 연구 소개는 다중 코어(명령을 실행하는 처리 단위가 여러 개 있는 구성)에서 대규모 자료 처리 응용을 실행하는 문제를 주요 갈래로 들고, 기계학습(자료에서 패턴을 학습해 예측이나 판단 규칙을 만드는 계산 방법) 모델을 실행하는 환경과 블록체인(여러 참여자가 공유하는 기록을 묶음별로 연결해 저장하고 변경 여부를 검증하는 체계) 응용의 시스템 지원도 연구 주제로 제시한다.[^research] 원유집 교수는 운영체제, 분산시스템(여러 컴퓨터가 통신하며 협력해 작업하는 체계), 저장 시스템, 비휘발성 메모리의 소프트웨어 지원을 관심 분야로 밝힌다. 교수 경력은 2019년 3월부터 KAIST 전기및전자공학부 교수로 적혀 있다.[^prof]

## 주요 연구 주제

### 파일시스템의 공간 회수와 검사

파일시스템은 내용을 기록하는 작업 외에도 쓰지 않는 저장 공간을 회수하고 자료 구조(자료를 조직하고 저장하는 방식)가 올바른지 검사해야 한다. 로그구조 파일시스템(변경된 내용을 저장 공간의 이어지는 위치에 순차적으로 기록하는 파일시스템)을 다룬 GAZE는 공간 회수 단계들을 겹쳐 실행하고 회수 작업에 쓸 메모리(실행 중인 명령과 자료를 보관하는 장치) 공간을 미리 준비해 지연을 줄이는 방법을 제안한다. lwFSCK(Light-weight Filesystem Check)는 검사 대상을 실행 흐름별로 나누고 임시 정보를 담는 자료 구조를 바꿔 검사 시간과 메모리 사용량을 줄이는 방법을 다룬다.[^p1][^p3]

### 여러 실행 흐름의 쓰기와 읽기 조정

ScaLog(Scalable Log-block Allocation)는 여러 스레드(프로그램 안에서 독립적으로 명령을 실행하는 흐름)가 동시에 자료를 기록할 때 저장 공간을 배정하는 경로가 병목이 되는 문제를 다룬다. 공간 배정 상태를 바꾸는 작업들을 분리하고, 관리 범위를 나누며, 여러 배정 요청을 묶어 처리한다.[^p2] 읽기와 쓰기가 저장장치를 함께 쓸 때의 공정성도 연구한다. 대표 논문 4의 공정한 입출력(자료를 읽거나 쓰는 동작) 조정 방법은 쓰기 내용의 영구 저장을 요구하는 요청이 읽기를 지연시키는 현상을 대상으로, 요청 종류별 이용 양상을 반영해 처리 자원을 배분한다.[^p4]

### 학습 기반 저장 주소 변환

저장장치는 소프트웨어가 쓰는 논리 주소와 실제 자료가 놓인 물리 주소를 대응시킨다. LeaST(Learned Sector Translation for Skipped Physical Page Address)는 학습한 모형으로 물리 주소를 예측하는 방식에서, 불량 저장 영역 때문에 주소의 연속성이 끊겨 예측 정확도가 낮아지는 문제를 다룬다. 끊긴 위치를 별도 기록에 보관하고 읽는 과정에서 예측 주소를 보정해 모형을 다시 학습하는 일을 피한다.[^p5]

### 키·값 저장소와 유사도 검색

키·값 저장소(자료를 식별하는 키와 그에 대응하는 값을 짝지어 보관하는 체계)의 기록 방식도 연구한다. Key-Space Partitioned RocksDB는 키 공간을 나누는 구조로 쓰기 작업이 멈추는 문제를 다룬다.[^p7] Aker는 벡터(여러 수를 순서대로 나열한 값)로 표현한 자료에서 비슷한 대상을 찾는 검색을 위한 근사 캐시를 제안한다. 캐시는 자료 조회나 계산의 반복을 피하도록 결과를 따로 보관하고 재사용하는 공간이며, 근사 캐시는 유사한 요청에 과거 결과를 재사용하는 방식이다. Aker는 주변 자료의 밀도에 맞게 재사용 기준을 조절하고, 자료가 삭제되거나 삽입될 때 저장된 검색 결과를 갱신하는 방법을 함께 설계한다.[^p6]

### 저장장치 안에서 하는 물체 검출 계산

SeeSSD는 자료를 중앙 컴퓨터로 보내기 전에 저장장치 안에서 이미지 계산을 수행하는 계산 저장장치다. 신경망(연결된 계산 단위 사이의 영향력을 조절해 자료의 관계를 학습하는 모형)을 이용한 물체 검출 계산을 저장장치 쪽으로 옮기고, 그 계산 장치와 제어 소프트웨어를 함께 구현해 자료 이동과 전력 사용을 줄이는 방법을 다룬다.[^p8]

## 대표 논문

KAIST 재직 시기의 논문 가운데 파일시스템, 다중 코어, 저장 주소 변환, 검색 구조, 계산 저장장치를 고르게 보여 주는 8편을 골랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 주요 저자 칸은 첫 저자와 원유집 교수의 저자 순서를 표시한다.

| 번호 | 연도 | 논문·발표처 | 주요 저자 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2026 | [GAZE: Rearchitecting Log-Structured Filesystem for Garbage Collection on Zoned Namespace Flash Storage](https://doi.org/10.1145/3830418.3843870) · ACM SIGOPS Symposium on Operating Systems Principles | 첫 저자 Juwon Kim; 마지막 저자 Youjip Won | 구역 단위로 공간을 회수하는 플래시 저장장치에 맞춰 파일시스템을 다시 설계했다. 회수 단계의 병렬 실행, 작업용 메모리의 사전 배정, 회수 중 쓰기 요청의 선택적 허용을 결합한다.[^p1] |
| 2 | 2026 | [Manycore Scalable Logging for Log-Structured Filesystem](https://doi.org/10.1145/3837053.3837347) · ACM Workshop on Hot Topics in Storage and File Systems | 첫 저자 Hwanseok Yoo; 마지막 저자 Youjip Won | 여러 실행 흐름이 직접 쓰기를 수행할 때 공간 배정 작업이 성능 확장을 막는 원인을 분석했다. 상태 변경의 분리와 관리 범위 분할, 여러 공간 배정의 묶음 처리로 그 병목을 줄인다.[^p2] |
| 3 | 2025 | [lwFSCK: Light-weight Filesystem Check](https://doi.org/10.1145/3672608.3707806) · ACM Symposium on Applied Computing | 첫 저자 Juwon Kim; 마지막 저자 Youjip Won | 큰 파일시스템을 검사하고 복구할 때 드는 시간과 메모리를 줄이는 도구다. 검사 대상을 실행 흐름마다 나누고 임시 정보를 담는 구조를 바꾼다.[^p3] |
| 4 | 2022 | [Fair I/O scheduler for alleviating read/write interference by forced unit access in flash memory](https://doi.org/10.1145/3538643.3539753) · ACM Workshop on Hot Topics in Storage and File Systems | 첫 저자 Jieun Kim; 마지막 저자 Youjip Won | 읽기와 영구 저장을 요구하는 쓰기가 서로 간섭할 때 요청 종류별로 공정하게 자원을 배분한다. 이용 양상에 따라 목표를 조정하고 소프트웨어의 관측 결과를 다시 반영한다.[^p4] |
| 5 | 2026 | [LeaST: Learned Sector Translation for Skipped Physical Page Address](https://doi.org/10.1109/nvmsa71223.2026.11658886) · IEEE Non-Volatile Memory Systems and Applications Symposium | 첫 저자 Jihoon Seok; 마지막 저자 Youjip Won | 불량 플래시 영역이 학습 기반 주소 예측을 어긋나게 하는 문제를 다룬다. 주소가 끊기는 위치를 기록하고 읽기 때 보정해 다시 학습하지 않고 예측을 개선한다.[^p5] |
| 6 | 2026 | [Aker: Density-Aware Approximate Caching for Vector Search](https://doi.org/10.14778/3828612.3828627) · Proceedings of the VLDB Endowment | 첫 저자 Sukjoon Oh; 마지막 저자 Youjip Won | 비슷한 검색 요청에 과거 결과를 재사용하되 주변 자료의 밀도에 맞춰 기준을 바꾼다. 삭제는 즉시 반영하고 삽입은 늦춰 반영하는 규칙으로 검색 결과를 갱신한다.[^p6] |
| 7 | 2024 | [Key-Space Partitioned LSM Tree for CMM-H](https://doi.org/10.1109/nvmsa63038.2024.10693654) · IEEE Non-Volatile Memory Systems and Applications Symposium | 첫 저자 Seung‐Ho Lim; 마지막 저자 Youjip Won | 키·값을 보관하는 자료 구조에서 쓰기 작업이 멈추는 현상을 다룬다. 키 공간을 분할한 자료 구조와 메모리 구성을 제안해 읽기와 쓰기의 성능을 개선한다.[^p7] |
| 8 | 2025 | [SeeSSD: Computational Storage for Energy-Efficient Real-Time Object Detection](https://doi.org/10.1145/3774649) · ACM Transactions on Embedded Computing Systems | 첫 저자 Muhammad Danish Tehseen; 마지막 저자 Youjip Won | 저장장치 안에서 이미지의 물체 검출 계산을 수행한다. 전용 계산 장치와 제어 소프트웨어, 검출 모형을 함께 구현해 중앙 컴퓨터로 보내는 자료량과 전력 사용을 줄인다.[^p8] |

## 구성원

구성원은 연구실 People에 게시된 15명이다. 과정은 각 사람의 소개 문장을 따르며, 「대표 논문 참여」는 논문의 전체 저자 목록에서 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Juwon Kim | 박사후연구원 | Filesystem | 1, 2, 3, 5 |
| Jieun Kim | 석박사통합과정 | computer vision and Embedded System | 4 |
| Dohyun Kim | 박사과정 | File system and OS kernel | 4, 6 |
| Junhan Lee | 박사과정 | Linux kernel |  |
| Seung Won Yoo | 박사과정 | Filesystem | 1, 3, 7 |
| Sukjoon Oh | 박사과정 | Linux kernel | 6 |
| Bonmoo Koo | 박사과정 | Storage |  |
| Gyeongjun Ha | 석박사통합과정 | File systems and Storage |  |
| Hyobyung Han | 석사과정 | File system and Storage |  |
| Hwanseok Yoo | 석사과정 | Filesystem and OS kernel | 1, 2 |
| Minki Kang | 석사과정 | Storage and GPU System | 6 |
| Jaewon Lee | 석사과정 | OS kernel |  |
| Whanseok Kim | 석사과정 | File system and Storage |  |
| Minjun Kim | 석사과정 | File system and Storage |  |
| Yoonsoo Oh | 석사과정 | GPU File System |  |

## 졸업생

연구실 People의 Alumni에 게시된 115행을 게시 순서대로 옮겼다. 연도와 진로는 연구실 표기를 따른다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Muhammad Danish Tehseen | (2026) | Braindeck |
| 석지훈 (Seok, Jihoon) | (2026) | SK hynix |
| 이승재 (Lee, Seungjae) | (2025) |  |
| 오준택 (Oh, Joontaek) | (2024) | University of Wisconsin–Madison |
| 최병현 (Choi, Byeonghyeon) | (2024) |  |
| 박수익 (Park, Suik) | (2024) | SK Hynix |
| 김동언 (Kim, Dongeon) | (2024) | Presto Labs |
| 임승호 (Lim, Seungho) | (2024) | SK Hynix |
| 황채영 (Hwang, Chaeyoung) | (2024) | LG CNS |
| 장주현(Jang, Juhyeon) | (2023) | 삼성전자 |
| 장민수(Jang, Minsu) | (2022) | 셀렉트스타 |
| 민광원(Min, Kwangwon) | (2022) | 삼성전자 |
| 김용진(Kim, Yongjin) | (2022) | LG CTO |
| 남호진(Nam, Hojin) | (2022) | 삼성전자 |
| 지시온(Ji, Sion) | (2022) | 삼성전자 |
| 박정안(Park,JeoungAhn) | (2022) | SK hynix |
| 이도근(Lee, Dokeun) | (2021) | SK hynix |
| 황태호(Hwang, Taeho) | (2020) | SK hynix |
| 김형준(Kim, Hyungjun) | (2020) | (주)윈스 |
| 김명선(Kim, Myeongseon) | (2020) | LG CTO |
| 이원종(Lee, Wonjong) | (2020) | 삼성전자 |
| 김선두(Kim, Sundoo) | (2019) | LG CTO |
| 조정우(Jo, Jungwoo) | (2019) | Exem |
| 윤주성(Yun, Juseong) | (2019) | (주)코비전 |
| 유진수(Yoo, Jinsoo) | (2018) | 삼성전자 |
| 조민재(Cho, Minjae) |  | (주) 우아한형제들 |
| 김선녕(Kim, Sunyoung) |  |  |
| 최경열(Choi, Gyeongyeol) | (2017) | TMaxSoft |
| 노연진(Noh, Yeonjin) | (2017) | LG CTO |
| 손성배(Son, Seongbae) | (2017) | HP |
| 김지현(Kim, Jihyun) | (2017) | 신세계 |
| 이성진(Lee, Seongjin) | (2016) | 경상대학교 |
| 천승용(Cheon, Seungyong) | (2016) | LG CTO |
| 손한근(Son, Hankeun ) | (2016) | SK Hynix |
| 유밝은(Yoo, Balgeun) | (2016) | LG CTO |
| 정재민(Jung, Jaemin) | (2016) | Samsung MSL |
| 이성수(Lee, Seongsu) | (2016) | LG CTO |
| Dam Quang Tuan | (2016) | Vietnam National Univ |
| 이건우(Lee, Keonwoo) | (2016) | Future Systems |
| 임은령(Lim, Eunryoung) | (2016) | 네이버 랩스 |
| 이원건(Lee, Onegun) | (2016) | 삼성전자 |
| 김명식(Kim, Myungsik) | (2016) | 삼성전자 |
| 이철희(Lee, Choelhee) | (2015) | 아리온 테크놀로지 |
| 박찬현(Park, Chanhyun) | (2015) | SK hynix |
| 박동일(Park, Dongil) | (2015) | 삼성전자 |
| 임경렬(Lim, Kyeongyeol) | (2015) | 고영테크놀러지 |
| 김준엽(Kim, Junyeop) | (2015) | 티맥스데이터 |
| 김규일(Kim, Kyuil) | (2014) | LG CTO |
| 정수만(Jeong, Sooman) | (2014) | 삼성전자 |
| 이기성(Lee, Kisung) | (2013) | 삼성전자 |
| 신진철(Shin, Jinchul) | (2013) | SK Planet |
| 김재운(Kim, Jaewoon) | (2013) |  |
| 정창훈(Jeong, Changhun) | (2013) | 티맥스데이터 |
| 조석희(Cho, Seokhei) | (2013) | LG CTO |
| 김종민(Gim, Jongmin) | (2012) | Samsung MSL |
| 김해성(Kim, Haesung) | (2012) | LG CTO |
| 홍성우(Hong, Sungwoo) | (2011) |  |
| 唐 智(Tang Zhi) | (2011) | 중국 Zhejiang시 금감원 |
| 김주현(Kim, Joohyun) | (2011) | 삼성전자 |
| 이철목(Lee, Chulmok) | (2011) | 삼성전자 |
| 구자진(Koo, Jajin) | (2011) | 이오테크닉스 |
| 전태종(Quan, TaiZhong) | (2011) | 중국산업은행 |
| 윤대영(Yoon, Daeyoung) | (2011) | 교대역 소재 감리회사 |
| Dashdorj Yamkhin | (2010) | Mongolia Univ. of Science and Technology |
| 최정헌(Choi, JeongHeon) | (2010) | Self-employeed |
| 이광호(Lee, Kwangho) | (2010) | 삼성전자 |
| 여해동(Yeo, Dylan) | (2010) | 삼성전자 |
| 김요환(Kim, Yohwan) | (2009) | LG전자 |
| 박진희(Park, Jinhee) | (2009) | 삼성전자 |
| 최민석(Choi, Minseok) | (2009) | 매크로 임팩트(주) |
| 신형종(Shin, Hyungjong) | (2008) | 삼성전자 |
| 장재혁(Chang, Jaehyeok) | (2008) | 네이버 |
| 조성호(Cho, Sungho) | (2008) |  |
| 한석희(Han, SeokHee) | (2008) | LG CTO |
| 민재홍(Min, Jaehong) | (2008) | 삼성전자 |
| 반종명(Ban, Jong-Myeong) | (2008) | 삼성전자 |
| 전병길(Jeon, Byunggil) | (2007) | 삼성전자 |
| 김은기(Kim, Eunki) | (2007) | 삼성전자 |
| 김락기(Kim, Rak-ki) | (2007) | 삼성전자 |
| 김영진(Kim,Youngjin) | (2007) | 네이버 |
| 박동주(Park, Dongju) | (2007) | Kakao |
| 박재석(Park, Jaeseok) | (2007) | 삼성전자 |
| 이모원(Lee, Mowon) | (2007) | Naver |
| 이주훤(Lee, Juhwon) | (2007) | (주)만도 |
| 정형원(Jung, Hyungwon) | (2007) | 삼성전자 |
| 정원민(Jung, Wonmin) | (2007) | LG CTO |
| 한영수(Han, Youngsoo) | (2006) | 삼성전자 |
| 노승현(Noh, Seunghyun) | (2006) | Phantom AI |
| 류재민(Ryu, Jaemin) | (2006) | 삼성전자 |
| 고영준(Goh, Youngun) | (2006) | 태민시스템 |
| 이시창(Lee, Sichang) | (2006) | 삼성 S1 |
| 한영수(Han, Youngsoo) | (2006) | 삼성전자 |
| 방창대(Bang, Changdae) |  |  |
| 강성주(Kang, Sungjoo) | (2005) | ETRI |
| 김재한(Kim, Jaehan) | (2005) |  |
| 윤영성(Yun, Youngsung) | (2005) | 삼성전자 |
| 김효준(Kim, Hyojun) | (2005) | Google |
| 장인광(Jang Ingwang) | (2005) | 삼성전자 |
| 장형규(Jang, Hyeonggyu) | (2005) | CTRing |
| 김두한(Kim, Duhan) | (2004) | 삼성전자 |
| 강광석(Gang, Gwangseok) | (2004) | 삼성전자 |
| 천지원(Chen, Jiwon) | (2004) | 삼성전자 |
| 송동현(Song, Donghyun) | (2004) | 삼성전자 |
| 이용만(Lee, Youngman) | (2004) | KOTBA |
| 김진용(Kim, Jinyong) | (2004) | Univ. of Texas at Dallas |
| 양승헌(Yang, Seunhyun) | (2004) | 넥슨코리아 |
| 최정완(Choi, Jungwan) | (2003) | LG 전자 MC연구소 |
| 송승호(Song, Seungho) | (2003) | 삼성전자 |
| 심보욱(Shim, Bouk) | (2002) | LG전자 |
| 오창영(Oh, Changyoung) | (2002) | Reakosys |
| 차승일(Cha, Seungil) | (2002) | TG삼보컴퓨터 |
| 백국실(Baek, Guksil) | (2002) | Nexdigm |
| 박진연(Park, Jinyeon) | (2002) | LG전자 |
| 김범은(Kim, Beopeun) | (2002) | 삼성전자 |
| 조경선(Cho, Kyungsun) | (2001) | 삼성전자 |

## 최근 논문과 발표 목록

연구실 Publications의 2021–2026년 구역에 게시된 논문과 발표 26건이다. 제목·저자·발표처는 연구실 표기를 따르며, 학회의 Accepted for publication은 「채택」, 학술지의 같은 표시는 「게재 승인」으로 적었다. 한 사람이 적힌 초청 세션 행은 발표자 표기다.[^pubs]

**2026**

- [ACM SoCC] Dohyun Kim, Sukjoon Oh, and Youjip Won, “MIDAS: Multi-core Scalable Replication for Key-Value Stores via Distributed Linearization”, In Proc. of ACM Symposium on Cloud Computing (SoCC), Singapore, Singapore, 채택, Nov. 18th – 20th, 2026
- [IEEE ICPADS] Minjun Kim, Jieun Kim, Youjip Won, “f2trace: Low-Overhead Memory-Efficient NVMe Queue-Level I/O Tracer”, In Proc. of IEEE International Conference on Parallel and Distributed Systems (ICPADS), Tokyo, Japan, 채택, Nov. 22 – 26, 2026
- [ACM HotStorage] Hwanseok Yoo, Juwon Kim, and Youjip Won, “Manycore Scalable Logging for Log-Structured Filesystem”, In Proc. of ACM Workshop on Hot Topics in Storage and File Systems (HotStorage), Prague, Czechia, 채택, Sep 28th – 29th, 2026 DOI: https://doi.org/10.1145/3837053.3837347
- [ACM SOSP] Juwon Kim, Hwanseok Yoo, Seung Won Yoo, and Youjip Won, “GAZE: Rearchitecting Log-Structured Filesystem for Garbage Collection on Zoned Namespace Flash Storage”, In Proc. ACM Symposium on Operating Systems Principles (SOSP), Prague, Czechia, 채택, Sep. 29th – Oct. 2nd, 2026. DOI: https://doi.org/10.1145/3830418.3843870
- [IEEE NVMSA] Jihoon Seok, Juwon Kim, and Youjip Won, “LeaST: Learned Sector Translation for Skipped Physical Page Address”, In Proc. of IEEE Non-Volatile Memory Systems and Applications Symposium (NVMSA),QingDao,China, 채택, Aug 11 – 13, 2026 DOI: https://doi.org/10.1109/nvmsa71223.2026.11658886
- [IEEE NVMSA] Minki Kang, Bonmoo Koo, and Youjip Won, “Understanding the Performance Characteristics of GPUDirect Storage”, In Proc. of IEEE Non-Volatile Memory Systems and Applications Symposium (NVMSA),QingDao,China, 채택(포스터), Aug 11 – 13, 2026
- [VLDB] Sukjoon Oh, Minki Kang, Dohyun Kim, Baotong Lu, Jing Liu, Qianxi Zhang, Qi Chen, Youjip Won, “Aker: Density-Aware Approximate Caching for Vector Search”, Proceedings of the VLDB Endowment, Boston, USA, 게재 승인, Aug 31 – Sep 4, 2026 DOI: https://doi.org/10.14778/3828612.3828627
- [ACM TOS] Joo-Young Hwang, Seokhwan Kim, Daejun Park, Yong-Gil Song, Junyoung Han, Seunghyun Choi, Sangyeun Cho and Youjip Won, “Advanced I/O Stack for Efficient Zone-based Mobile Flash Storage”, ACM Transactions on Storage, Volume 22, Jan, 2026 DOI: https://doi.org/10.1145/3797255
- [ACM TECS] Muhammad Danish Tehseen, Gyeongcheol Shin, Joo-Young Kim, Youjip Won, “SeeSSD: Computational Storage for Energy-Efficient Real-Time Object Detection”, ACM Transactions on Embedded Computing Systems (TECS), Volume 24, Issue 6, Jan, 2026 DOI: https://doi.org/10.1145/3774649

**2025**

- [KIISE 논문지] 김지은, 유승원, 원유집 “현대 입출력 스택에서 쓰기 순서 효율적 보장에 대한 고찰” 정보과학회 논문지, 제43권, 제3호, 2025년 3월, pp.27-35
- [USENIX FAST] Jieun Kim, Joontaek Oh, Juwon Kim, Seung Won Yoo, and Youjip Won, “OPIMQ: Order Preserving IO stack for Multi-Queue Block Device“, In Proc. of USENIX Conference on File and Storage Technologies (FAST), Feb, 2025
- [USENIX FAST] Juwon Kim, Seungjae Lee, Joontaek Oh, Dongkun Shin, and Youjip Won, “D2FS: Device-Driven Filesystem Garbage Collection“, In Proc. of USENIX Conference on File and Storage Technologies (FAST) , Feb, 2025
- [USENIX FAST] Seung Won Yoo, Joontaek Oh, Myoengin Cheon, Bonmoo Koo, Wonseb Jeong, Hyunsub Song, Hyeonho Song, Donghun Lee, and Youjip Won, “DJFS : Directory-Granularity Filesystem Journaling for CMM-H SSDs“, In Proc. of USENIX Conference on File and Storage Technologies (FAST), Feb, 2025
- [ACM SAC] Juwon Kim, Dongeon Kim, Seung Won Yoo, Myoengin Cheon, Joontaek Oh, and Youjip Won, “lwFSCK: Light-weight Filesystem Check“, In Proc. of ACM Symposium on Applied Computing (SAC)  Siciliy Italy, March,2025 DOI: https://doi.org/10.1145/3672608.3707806

**2024**

- [USENIX ATC] Joo-Young Hwang, Seokhwan Kim, Daejun Park, Yong-Gil Song, Junyoung Han, Seunghyun Choi, Sangyeun Cho, and Youjip Won, “Zone Abstracton for Mobile Flash Storage”, In Proc. of USENIX Annual Technical Conference (ATC) 2024, July 10-12, 2024
- [IEEE NVMSA] Seungho Lim, Seung Won Yoo, Joontaek Oh, Wonseb Jeong, Hyunsub Song, Hyeonho Song, Donghun Lee, and Youjip Won, “Key-Space Partitioned LSM Tree for CMM-H”, In Proc. of IEEE Non-Volatile Memory Systems and Applications Symposium (NVMSA) 2024, Aug 21 – 23, 2024 DOI: https://doi.org/10.1109/nvmsa63038.2024.10693654

**2023**

- [USENIX FAST] Joontaek Oh, Seung Won Yoo, Hojin Nam, Changwoo Min and Youjip Won, “CJFS : Concurrent Journaling for Better Scalability”, In Proc. of USENIX Conference on File and Storage Technologies (FAST) 2023, Feb, 20-23, 2023
- [IEEE NVMSA] Chaeyoung Hwang, Yongjin Kim, Junhan Lee, Youjip Won, “Addressing the Space Overhead of Vector Quotient Filter”, In Proc.of IEEE Non-Volatile Memory Systems and Applications Symposium (NVMSA) 2023, Aug 30 – Sep 1, 2023 DOI: https://doi.org/10.1109/nvmsa58981.2023.00020

**2022**

- [대한임베디드공학회 추계학술대회] Dohyun Kim, 우수학회논문 초청 세션, “ScaleXFS: Getting scalability of XFS back on the ring“, 제주 그라벨 호텔, November 2-4, 2022.
- [IEEE NVMSA] Kwangwon Min, Dohyun Kim, Seungho Lim, and Youjip Won, “Polling Based Per-core Workqueue Management in XFS Journaling“, In Proc. of IEEE NVMSA’22, Taipei, Taiwan, August. 23-25,2022 DOI: https://doi.org/10.1109/nvmsa56066.2022.00016
- [ACM HotStorage] Jieun Kim, Dohyun Kim and Youjip Won, “Fair I/O Scheduler for Alleviating Read/Write Interference by  Forced Unit Access in Flash Memory”, In Proc. of ACM HotStorage’22, Virtual, June. 27-28, 2022 DOI: https://doi.org/10.1145/3538643.3539753
- [USENIX ATC] Juwon Kim, Minsu Jang, Danish Muhammad Teeshen, Joontaek Oh, and Youjip Won “IPLFS: Log-Structured File System without Garbage Collection“, In Proc. of USENIX Annual Technical Conference (ATC) 2022, July. 11-13, 2022
- [ACM SYSTOR] Seung Won Yoo, Joontaek Oh, and Youjip Won “O-AFA: Order Preserving All Flash Array“, in Proc. of The ACM International Systems and Storage Conference (SYSTOR), Haifa, Israel, June. 13-15, 2022 DOI: https://doi.org/10.1145/3534056.3534942
- [USENIX FAST] Dohyun Kim, Kwangwon Min, Joontaek Oh, and Youjip Won “ScaleXFS: Getting scalability of XFS back on the ring“, In Proc. of USENIX Conference on File and Storage Technologies (FAST) 2022, Feb, 22-24, 2022
- [USENIX FAST] Joontaek Oh, Sion Ji, Yongjin Kim, and Youjip Won, “exF2FS: Transaction Support in Log-Structured Filesystem“, In Proc. of USENIX Conference on File and Storage Technologies (FAST) 2022, Feb, 22-24, 2022

**2021**

- [KIISE 논문지] 원유집 “아주 쉬운 논문 쓰기” 정보과학회 학회지, 제 39권, 제 11호, 2021년 11월, pp.108-118.

## 수상과 선정

연구실 글 목록 피드에 게시된 수상·선정 3건이다. 날짜는 글의 게시일이며, 선정 연도가 따로 적힌 항목은 그 연도를 함께 표시했다.[^news-feed]

- 2023-11-01 · 김주원이 NVRAMOS 2023 OpenSSD Best Practice Award 금상을 받았다.[^n061]
- 2023-04-17 · 오준택이 KAIST 전기및전자공학부의 2022 우수연구원으로 선정되었다.[^n068]
- 2022-10-28 · 김도현이 우수조교상을 받았다.[^n078]

## 소식

연구실의 논문 채택·게재 승인 소식과 논문 발표를 명시한 참석 후기 30건이다. 날짜는 글의 게시일이며, 같은 발표를 다룬 별도 글은 각각 표시했다.[^news-feed]

- 2026-10-12 · 강민기의 SOSP 2026 참석 후기가 김주원의 연구 발표와 포스터 발표를 소개했다.[^n001]
- 2026-10-12 · 유환석이 HotStorage 2026에서 Manycore Scalable Logging for Log-Structured Filesystem 연구를 발표했다.[^n002]
- 2026-10-12 · 김주원이 SOSP 2026에서 GAZE 논문을 발표하고, 유환석이 HotStorage 2026에서 Manycore Scalable Logging for Log-Structured Filesystem 연구를 발표했다고 알렸다.[^n003]
- 2026-09-18 · GAZE 논문이 ACM SOSP 2026에 채택되었다.[^gaze-news]
- 2026-09-14 · Sukjoon Oh가 VLDB 2026에서 Aker 논문을 발표했다.[^aker-news]
- 2026-08-20 · 강민기가 NVMSA 2026에서 Understanding the Performacne Characteristics of GPU Direct Storage 포스터 논문을 발표했다.[^n006]
- 2026-08-20 · 김주원이 NVMSA 2026에서 LeaST 논문을 발표했다.[^n008]
- 2026-06-02 · Aker 논문이 PVLDB 2026에 게재 승인되었다.[^n011]
- 2025-12-09 · 김지은의 IEEE AIoT 2025 출장 후기가 학회 마지막 날 본인의 발표를 마쳤다고 전했다.[^n018]
- 2025-04-14 · 김주원이 ACM SAC 2025에서 lwFSCK 논문을 발표했다.[^n033]
- 2025-03-11 · 구본무의 FAST 2025 참석 후기가 연구실 논문 3편의 채택과 발표를 소개했다.[^n034]
- 2025-03-11 · 유승원이 FAST 2025에서 DJFS 논문을 발표했다.[^n035]
- 2025-03-11 · 김주원이 FAST 2025에서 D2FS 논문을 발표했다.[^n036]
- 2025-03-11 · 김지은이 FAST 2025에서 OPIMQ 논문을 발표했다.[^n037]
- 2024-10-29 · 김주원의 NVRAMOS 2024 참석 후기가 원유집 교수 참여 논문인 Zone-based Mobile Storage device의 발표를 소개했다.[^n045]
- 2023-09-14 · 황채영이 NVMSA 2023에서 게재된 포스터 논문을 발표했다.[^n064]
- 2023-03-07 · 오준택이 FAST 2023에서 CJFS 논문을 구두 및 포스터로 발표했다.[^n069]
- 2023-02-27 · 유승원이 FAST 2023에서 오준택과 함께 CJFS 포스터 발표에 참여했다.[^n071]
- 2022-12-24 · CJFS 논문이 FAST 2023에 채택되었다.[^n077]
- 2022-07-24 · 오준택의 ATC 2022 참석 후기가 김주원의 IPLFS 논문 발표와 포스터 발표를 소개했다.[^n083]
- 2022-07-21 · 김주원이 ATC 2022에서 연구를 발표하고 포스터 세션을 진행했다.[^n084]
- 2022-06-23 · Fair I/O Scheduler for Alleviating Read/Write Interference by Forced Unit Access in Flash Memory 논문이 HotStorage 2022에 채택되었다.[^n086]
- 2022-06-21 · 유승원이 SYSTOR 2022에서 O-AFA 논문을 발표했다.[^n088]
- 2022-05-05 · IPLFS 논문이 ATC 2022에 채택되었다.[^n089]
- 2022-04-26 · O-AFA 논문이 SYSTOR 2022에 채택되었다.[^n090]
- 2022-03-06 · 김도현이 FAST 2022에서 ScaleXFS 연구를 발표했다.[^n091]
- 2022-03-06 · 장민수의 FAST 2022 참석 후기가 본인의 연구 발표 소감을 전했다.[^n092]
- 2022-03-06 · 오준택이 FAST 2022에 논문을 게재하고 발표했다.[^n094]
- 2021-12-28 · exF2FS 논문이 FAST 2022에 채택되었다.[^n096]
- 2021-12-28 · ScaleXFS 논문이 USENIX FAST 2022에 채택되었다.[^n097]

## 연락과 위치

- 교수 이메일: ywon@kaist.ac.kr.[^dept]
- 교수 연락처: 7456(학부 교수 소개 표기).[^dept]
- 교수 위치: IT융합빌딩 N1 309호(학부 교수 소개 표기).[^dept]
- 연구실 위치: IT융합빌딩 N1 313호.[^home]
- 주소: 대전광역시 유성구 대학로 291, KAIST. 우편번호 34141.[^home]
[^home]: KAIST OS Lab 첫 화면. <https://oslab.kaist.ac.kr> (2026-11-09 관측).
[^research]: KAIST OS Lab, Research. <https://oslab.kaist.ac.kr/research/> (2026-11-09 관측).
[^people]: KAIST OS Lab, People. <https://oslab.kaist.ac.kr/people-3/> (2026-11-09 관측).
[^pubs]: KAIST OS Lab, Publications. <https://oslab.kaist.ac.kr/publications/> (2026-11-09 관측).
[^dept]: KAIST 전기및전자공학부, 원유집 교수 소개. <https://ee.kaist.ac.kr/professor/16612/> (2026-11-09 관측).
[^prof]: KAIST OS Lab, 원유집 교수 소개. <https://oslab.kaist.ac.kr/professor-youjip-won/> (2026-11-09 관측).
[^gaze-news]: KAIST OS Lab, GAZE 논문 채택 소식, 2026-09-18. <https://oslab.kaist.ac.kr/gaze-rearchitecting-log-structured-filesystem-for-garbage-collection-on-zoned-namespace-flash-storage-accepted-in-sosp-26/> (2026-11-09 관측).
[^aker-news]: KAIST OS Lab, 오석준 VLDB 2026 참석 후기, 2026-09-14. <https://oslab.kaist.ac.kr/%EC%98%A4%EC%84%9D%EC%A4%80-vldb-26-%EC%B0%B8%EC%84%9D-%ED%9B%84%EA%B8%B0/> (2026-11-09 관측).
[^p1]: J. Kim, H. Yoo, S. W. Yoo, Y. Won, ACM SIGOPS Symposium on Operating Systems Principles (SOSP) (2026). <https://doi.org/10.1145/3830418.3843870> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5110391759,publication_year:2021-2026> (2026-11-09 관측).
[^p2]: H. Yoo, J. Kim, Y. Won, ACM Workshop on Hot Topics in Storage and File Systems (HotStorage) (2026). <https://doi.org/10.1145/3837053.3837347> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5110391759,publication_year:2021-2026> (2026-11-09 관측).
[^p3]: J. Kim 외, Y. Won, ACM Symposium on Applied Computing (2025). <https://doi.org/10.1145/3672608.3707806> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5110391759,publication_year:2021-2026> (2026-11-09 관측).
[^p4]: J. Kim, D. Kim, Y. Won, ACM Workshop on Hot Topics in Storage and File Systems (HotStorage) (2022). <https://doi.org/10.1145/3538643.3539753> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5110391759,publication_year:2021-2026> (2026-11-09 관측).
[^p5]: J. Seok, J. Kim, Y. Won, IEEE Non-Volatile Memory Systems and Applications Symposium (NVMSA) (2026). <https://doi.org/10.1109/nvmsa71223.2026.11658886> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5110391759,publication_year:2021-2026> (2026-11-09 관측).
[^p6]: S. Oh 외, Y. Won, Proceedings of the VLDB Endowment (2026). <https://doi.org/10.14778/3828612.3828627> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5110391759,publication_year:2021-2026> (2026-11-09 관측).
[^p7]: S.-H. Lim 외, Y. Won, IEEE Non-Volatile Memory Systems and Applications Symposium (NVMSA) (2024). <https://doi.org/10.1109/nvmsa63038.2024.10693654> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5110391759,publication_year:2021-2026> (2026-11-09 관측).
[^p8]: M. D. Tehseen, G. Shin, J.-Y. Kim, Y. Won, ACM Transactions on Embedded Computing Systems (2025). <https://doi.org/10.1145/3774649> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5110391759,publication_year:2021-2026> (2026-11-09 관측).
[^news-feed]: KAIST OS Lab, 누리집 글 목록 피드, 16쪽의 글 160건. <https://oslab.kaist.ac.kr/feed/> (2026-11-09 관측).
[^n001]: KAIST OS Lab 게시 글, 「강민기 SOSP`26 참석 후기」. <https://oslab.kaist.ac.kr/%ea%b0%95%eb%af%bc%ea%b8%b0-sosp26-%ec%b0%b8%ec%84%9d-%ed%9b%84%ea%b8%b0/> (2026-11-09 관측).
[^n002]: KAIST OS Lab 게시 글, 「유환석 SOSP`26 참석후기」. <https://oslab.kaist.ac.kr/%ec%9c%a0%ed%99%98%ec%84%9d-sosp26-%ec%b0%b8%ec%84%9d%ed%9b%84%ea%b8%b0/> (2026-11-09 관측).
[^n003]: KAIST OS Lab 게시 글, 「김주원 SOSP`26 참석후기」. <https://oslab.kaist.ac.kr/%ea%b9%80%ec%a3%bc%ec%9b%90-sosp26-%ec%b0%b8%ec%84%9d%ed%9b%84%ea%b8%b0/> (2026-11-09 관측).
[^n006]: KAIST OS Lab 게시 글, 「강민기 NVMSA 2026 출장 후기」. <https://oslab.kaist.ac.kr/%ea%b0%95%eb%af%bc%ea%b8%b0-nvmsa-2026-%ec%b6%9c%ec%9e%a5-%ed%9b%84%ea%b8%b0/> (2026-11-09 관측).
[^n008]: KAIST OS Lab 게시 글, 「김주원 NVMSA 2026 출장 후기」. <https://oslab.kaist.ac.kr/%ea%b9%80%ec%a3%bc%ec%9b%90-nvmsa26-%ec%b6%9c%ec%9e%a5%ed%9b%84%ea%b8%b0/> (2026-11-09 관측).
[^n011]: 누리집 글 목록 피드의 제목·게시 요약, 「“Aker: Density-Aware Approximate Caching for Vector Search” Accepted in PVLDB`26」. <https://oslab.kaist.ac.kr/feed/?paged=2> (2026-11-09 관측).
[^n018]: KAIST OS Lab 게시 글, 「김지은 IEEE AIoT 2025 출장 후기」. <https://oslab.kaist.ac.kr/%ea%b9%80%ec%a7%80%ec%9d%80-ieee-aiot-2025-%ec%b6%9c%ec%9e%a5-%ed%9b%84%ea%b8%b0/> (2026-11-09 관측).
[^n033]: KAIST OS Lab 게시 글, 「ACM SAC ’25 김주원 참석 후기」. <https://oslab.kaist.ac.kr/acm-sac-25-%ea%b9%80%ec%a3%bc%ec%9b%90-%ec%b0%b8%ec%84%9d-%ed%9b%84%ea%b8%b0/> (2026-11-09 관측).
[^n034]: KAIST OS Lab 게시 글, 「구본무 FAST`25 참석후기」. <https://oslab.kaist.ac.kr/%ea%b5%ac%eb%b3%b8%eb%ac%b4-fast25-%ec%b0%b8%ec%84%9d%ed%9b%84%ea%b8%b0/> (2026-11-09 관측).
[^n035]: KAIST OS Lab 게시 글, 「유승원 FAST ’25 참석 후기」. <https://oslab.kaist.ac.kr/%ec%9c%a0%ec%8a%b9-fast-25-%ec%b0%b8%ec%84%9d-%ed%9b%84%ea%b8%b0/> (2026-11-09 관측).
[^n036]: KAIST OS Lab 게시 글, 「김주원 FAST ’25 참석 후기」. <https://oslab.kaist.ac.kr/%ea%b9%80%ec%a3%bc%ec%9b%90-fast-25-%ec%b0%b8%ec%84%9d-%ed%9b%84%ea%b8%b0/> (2026-11-09 관측).
[^n037]: KAIST OS Lab 게시 글, 「김지은 FAST’25 참석 후기」. <https://oslab.kaist.ac.kr/%ea%b9%80%ec%a7%80%ec%9d%80-fast25-%ec%b0%b8%ec%84%9d-%ed%9b%84%ea%b8%b0/> (2026-11-09 관측).
[^n045]: KAIST OS Lab 게시 글, 「김주원 NVRAMOS`24 참석후기」. <https://oslab.kaist.ac.kr/57300-2/> (2026-11-09 관측).
[^n064]: KAIST OS Lab 게시 글, 「황채영 NVMSA’23 참석 후기」. <https://oslab.kaist.ac.kr/%ed%99%a9%ec%b1%84%ec%98%81-apsys23-%ec%b0%b8%ec%84%9d-%ed%9b%84%ea%b8%b0/> (2026-11-09 관측).
[^n069]: KAIST OS Lab 게시 글, 「오준택 FAST ’23 참석 후기」. <https://oslab.kaist.ac.kr/%ec%98%a4%ec%a4%80%ed%83%9d-fast-23-%ec%b0%b8%ec%84%9d-%ed%9b%84%ea%b8%b0/> (2026-11-09 관측).
[^n071]: KAIST OS Lab 게시 글, 「유승원 FAST`23 참석 후기」. <https://oslab.kaist.ac.kr/%ec%9c%a0%ec%8a%b9%ec%9b%90-fast/> (2026-11-09 관측).
[^n077]: 누리집 글 목록 피드의 제목·게시 요약, 「“CJFS: Concurrent Journaling for Better Scalability”, accepted in FAST’23」. <https://oslab.kaist.ac.kr/feed/?paged=8> (2026-11-09 관측).
[^n083]: KAIST OS Lab 게시 글, 「오준택 ATC ’22 참석 후기」. <https://oslab.kaist.ac.kr/%ec%98%a4%ec%a4%80%ed%83%9d-atc-22-%ec%b0%b8%ec%84%9d-%ed%9b%84%ea%b8%b0/> (2026-11-09 관측).
[^n084]: KAIST OS Lab 게시 글, 「김주원 ATC`22 참석 후기」. <https://oslab.kaist.ac.kr/%ec%9c%a0%ec%8a%b9%ec%9b%90-systor22-%ec%b0%b8%ec%84%9d-%ed%9b%84%ea%b8%b0-2/> (2026-11-09 관측).
[^n086]: 누리집 글 목록 피드의 제목·게시 요약, 「“Fair I/O Scheduler for Alleviating Read/Write Interference by Forced Unit Access in Flash Memory”, accpeted in Hotstoage 2022.」. <https://oslab.kaist.ac.kr/feed/?paged=9> (2026-11-09 관측).
[^n088]: KAIST OS Lab 게시 글, 「유승원 SYSTOR`22 참석 후기」. <https://oslab.kaist.ac.kr/%ec%9c%a0%ec%8a%b9%ec%9b%90-systor22-%ec%b0%b8%ec%84%9d-%ed%9b%84%ea%b8%b0/> (2026-11-09 관측).
[^n089]: 누리집 글 목록 피드의 제목·게시 요약, 「“IPLFS: Log-Structured File System without Garbage Collection”, accepted in ATC`22」. <https://oslab.kaist.ac.kr/feed/?paged=9> (2026-11-09 관측).
[^n090]: 누리집 글 목록 피드의 제목·게시 요약, 「“O-AFA:Order Preserving All Flash Array”, accepted in SYSTOR’22」. <https://oslab.kaist.ac.kr/feed/?paged=9> (2026-11-09 관측).
[^n091]: KAIST OS Lab 게시 글, 「김도현 FAST ’22 참석 후기」. <https://oslab.kaist.ac.kr/dohyun-attended-fast-22/> (2026-11-09 관측).
[^n092]: KAIST OS Lab 게시 글, 「장민수 FAST ’22 참석 후기」. <https://oslab.kaist.ac.kr/minsu-attended-fast-22/> (2026-11-09 관측).
[^n094]: KAIST OS Lab 게시 글, 「오준택 FAST ’22 참석 후기」. <https://oslab.kaist.ac.kr/joontaek-attended-fast-22/> (2026-11-09 관측).
[^n096]: 누리집 글 목록 피드의 제목·게시 요약, 「“exF2FS: Transaction Support in Log-Structured Filesystem”, accepted in FAST’22」. <https://oslab.kaist.ac.kr/feed/?paged=10> (2026-11-09 관측).
[^n097]: 누리집 글 목록 피드의 제목·게시 요약, 「“ScaleXFS: Getting scalability of XFS back on the ring”, accepted in USENIX FAST 2022.」. <https://oslab.kaist.ac.kr/feed/?paged=10> (2026-11-09 관측).
[^n061]: 누리집 글 목록 피드의 제목·게시 요약, 「NVRAMOS 2023 OpenSSD Best Practice Award 금상」. <https://oslab.kaist.ac.kr/feed/?paged=7> (2026-11-09 관측).
[^n068]: 누리집 글 목록 피드의 제목·게시 요약, 「오준택 연구원 2022 우수연구원 선정」. <https://oslab.kaist.ac.kr/feed/?paged=7> (2026-11-09 관측).
[^n078]: 누리집 글 목록 피드의 제목·게시 요약, 「김도현 우수조교상 수상」. <https://oslab.kaist.ac.kr/feed/?paged=8> (2026-11-09 관측).

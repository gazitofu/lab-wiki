# AI SOC Lab

**서울대학교 첨단융합학부 차세대지능형반도체전공, 공과대학 전기·정보공학부(겸무) · 박준석 조교수**

- 분야: 인공지능 계산용 반도체와 시스템 설계, 심층 신경망 가속기, 메모리 내 처리 구조
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: AI 반도체·가속기[^research], 집적회로 설계[^ece], 메모리 내 연산[^home], 컴퓨터 구조·운영체제[^home]
- 홈페이지: <https://sites.google.com/snu.ac.kr/soc>
- 근거와 출처: [AI SOC Lab 근거 페이지](aisoc-sources.md)

> 기기 안에서 인공지능을 실행할 반도체를 개발하는 연구실이다. 신경망 계산을 맡는 가속기, 여러 기능을 한 칩에 담는 시스템 온 칩, 메모리 안에서 계산하는 구조를 연구한다.[^research][^home]

## 무엇을 연구하나

AI SOC Lab은 기기 안에서 인공지능을 실행하는 온디바이스 인공지능(on-device AI)을 위한 차세대 반도체를 개발한다. Research 페이지는 이를 인공지능 시스템 온 칩(System-on-Chip, SoC)의 개발로 설명한다. 시스템 온 칩은 여러 시스템 기능을 한 반도체 칩에 통합한 집적회로(여러 전자 소자와 그 연결을 한 반도체 기판에 형성한 회로)다.[^research]

연구는 특정 계산을 수행하는 하드웨어(컴퓨터를 이루는 물리적 장치) 시스템을 대상으로 한다. 첫 화면은 컴퓨터 구조(계산 장치와 저장 장치의 구성 및 작동 방식), 초고밀도 집적회로 설계(Very-Large-Scale Integration, VLSI), 하드웨어와 소프트웨어(컴퓨터에서 실행하는 프로그램)의 공동 설계, 메모리(정보를 저장하는 장치) 내 처리 구조를 다룬다고 밝힌다. 개별 부품만이 아니라 시스템 전체를 함께 고려해 성능·효율·확장성을 개선하는 접근을 취한다고 설명한다.[^home]

Research 페이지가 제시하는 갈래는 심층 신경망 가속기, 인공지능 시스템 온 칩, 메모리 내 처리 구조다. 신경망은 서로 연결된 계산 단위와 연결의 가중치(입력의 반영 정도를 정하는 값)로 입력을 출력으로 바꾸는 계산 모형이고, 심층 신경망은 여러 층으로 구성된 신경망이다. 가속기는 특정 계산을 수행하도록 설계한 하드웨어다. 연구실은 이런 계산 장치와 칩의 구조를 인공지능 응용에 맞춰 개발하는 데 초점을 둔다.[^research][^home]

## 주요 연구 주제

### 심층 신경망 가속기

심층 신경망의 계산을 수행하는 전용 하드웨어가 연구 대상이다. 누리집은 딥러닝(여러 층의 계산을 통해 자료의 특징을 학습하는 기계학습)과 심층 신경망 가속기를 첫 연구 갈래로 적고, 기기 내부에서 실행할 인공지능을 위한 반도체 개발을 목표로 제시한다.[^research]

### 인공지능 시스템 온 칩과 공동 설계

인공지능을 지원하는 시스템 온 칩이 두 번째 갈래다. 교수의 학과 소개는 인공지능용 집적회로와 시스템, 저전력 디지털 회로(구분된 값으로 정보를 나타내며 동작하는 전자 회로), 응용 특화 계산 장치와 가속기 설계를 연구 관심으로 적는다. 하드웨어와 소프트웨어의 공동 설계는 장치의 구성과 그 장치에서 실행할 프로그램을 함께 설계하는 일이다.[^research][^ece]

### 메모리 내 처리 구조

정보를 저장하는 메모리 내부나 그 가까이에서 계산하는 메모리 내 처리(Processing-in-Memory, PIM) 구조를 연구한다. 첫 화면은 이를 특정 계산용 하드웨어 시스템 연구의 한 갈래로 적으며, Research 페이지도 메모리 내 처리 구조를 주요 연구 대상으로 제시한다.[^home][^research]

## 교수와 전문 분야

박준석(Jun-Seok Park)은 서울대학교 첨단융합학부 차세대지능형반도체전공 조교수이며 공과대학 전기·정보공학부를 겸무한다. 첨단융합학부 소개는 두 소속 모두 2026년 3월부터로 적는다.[^snuti]

KAIST 전기및전자공학 분야에서 학사(2009), 석사(2011), 박사(2015) 학위를 받았다. 서울대에 오기 전에는 삼성전자 DS 부문 S.LSI 사업부에서 일했다. 첨단융합학부 소개는 삼성전자 경력을 2015년 4월–2026년 2월로 적는다.[^snuti]

현재 공식 소개의 전문 분야는 인공지능 시스템 온 칩, 디지털 집적회로, 저전력 디지털 회로 설계, 하드웨어와 소프트웨어의 공동 설계다. 전기·정보공학부 소개는 응용에 맞춘 계산 장치와 가속기 설계도 연구 관심으로 제시한다.[^snuti][^ece]

## 응용 분야

Research 페이지는 온디바이스 인공지능 응용을 목표로 차세대 인공지능 시스템 온 칩을 개발한다고 밝힌다. 첫 화면은 향후 인공지능 응용을 지원할 고성능 컴퓨팅 플랫폼(계산에 필요한 하드웨어와 소프트웨어의 기반)의 개발을 현재의 초점으로 적는다.[^research][^home]

## 구성원

2026년 10월 26일 Researchers 페이지에 게시된 대학원생 1명과 인턴 2명이다. Narim Kim은 석사·박사 학생을 묶은 M.S./Ph.D. Students 구역에 있어 대학원생으로 적었다. 인턴 두 명은 Interns 구역의 표기다.[^members]

| 이름 | 과정 | 이메일 |
|---|---|---|
| Narim Kim | 대학원생 (M.S./Ph.D. Students) | narim.kim@snu.ac.kr |
| Junho Park | 인턴 | bryan123@snu.ac.kr |
| Seungwoo Son | 인턴 |  |

## 최근 논문 목록 (2021–2026)

교수의 부임 전 논문 목록에는 휴대기기용 인공지능 연산 칩과 그 구조를 다룬 논문이 실려 있다. 누리집 International Conference의 2021–2026년 구역 5편과 Journals의 같은 범위 1편이다. 교수의 서울대 부임 전인 2021·2022·2025년 구역의 항목이 섞여 있으며, 아래 6편은 모두 2026년 3월 부임보다 앞선 구역에 있다. 제목·저자·발표처와 연도 구역은 누리집 표기다. 학술지 목록의 2025년 구역과 국제 학회 목록의 2022년 구역에는 같은 제목의 논문이 각각 실려 있다.[^conferences][^journals][^snuti]

**2025**

- Jun-Seok Park, T aehee Lee, Heonsoo Lee, Changsoo Park, Youngsang Cho, Mookyung Kang, Heeseok Lee, Jinwon Kang, Taeho Jeon, Dongwoo Lee, Yesung Kang, Kyungmok Kum, Geunwon Lee, Hongki Lee, Minkyu Kim, Suknam Kwon, Sung-boem Park, Dongkeun Kim, Chulmin Jo, HyukJun Chung, Ilryoung Kim, Jongyoul Lee. "An On-Device Generative AI Focused Neural Processing Unit in 4nm Flagship Mobile SoC with Fan-Out Wafer-Level Package". *2025 IEEE International Solid-State Circuits Conference (ISSCC)*.
- Jun-Seok Park, Changsoo Park, Suknam Kwon, Hyeong-Seok Kim, Taeho Jeon, Yesung Kang, Heonsoo Lee, Dongwoo Lee, James Kim, YoungJong Lee, Sangkyu Park, Jun-Woo Jang, SangHyuck Ha, MinSeong Kim, Jihoon Bang, Suk Hwan Lim, Inyup Kang. "A Multi-Mode 8K-MAC HW-Utilization-Aware Neural Processing Unit with a Unified Multi-Precision Datapath in 4nm Flagship Mobile SoC". *Journal of Solid-State Circuits (JSSC), (Invited from ISSCC)*.

**2022**

- Jun-Seok Park, Changsoo Park, Suknam Kwon, Hyeong-Seok Kim, Taeho Jeon, Yesung Kang, Heonsoo Lee, Dongwoo Lee, James Kim, YoungJong Lee, Sangkyu Park, Jun-Woo Jang, SangHyuck Ha, MinSeong Kim, Jihoon Bang, Suk Hwan Lim, Inyup Kang. "A Multi-Mode 8K-MAC HW-Utilization-Aware Neural Processing Unit with a Unified Multi-Precision Datapath in 4nm Flagship Mobile SoC". *2022 IEEE International Solid-State Circuits Conference (ISSCC) (Session highlight)*.

**2021**

- Jun-Seok Park, Jun-Woo Jang, Heonsoo Lee, Dongwoo Lee, Sehwan Lee, Hanwoong Jung, Seungwon Lee, Suknam Kwon, Kyungah Jeong, Joon-Ho Song, SukHwan Lim, Inyup Kang. "A 6k-MAC Feature-Map-Sparsity-aware Neural Processing Unit in 5nm Flagship Mobile SoC". *2021 IEEE International Solid-State Circuits Conference (ISSCC)*.
- Jun-Seok Park, Heonsoo Lee, Dongwoo Lee, Jewoo Moon, Suknam Kwon, Sanghyuck Ha, MinSeong Kim, Junghun Park, Jihoon Bang, SukHwan Lim, Inyup Kang. "Samsung Neural Processing Unit: An AI accelerator and SDK for flagship mobile AP". *2021 Hotchips*.
- Jun-Woo Jang, Sehwan Lee, Dongyoung Kim, Hyunsun Park, Ali Shafiee Ardestani, Yeongjae Choi, Channoh Kim, Yoojin Kim, Hyeongseok Yu, Hamzah Abdel-Aziz, Jun-Seok Park, Heonsoo Lee, Dongwoo Lee, Myeong Woo Kim, Hanwoong Jung, Heewoo Nam, Dongguen Lim, Seungwon Lee, Joon-Ho Song, Suknam Kwon, Joseph Hassoun, SukHwan, Changkyu Choi. "Sparsity-aware and re-configurable NPU architecture for samsung flagship mobile SoC". *2021 ACM/IEEE 48th Annual International Symposium on Computer Architecture (ISCA)*.

## 수상

교수 소개에 게시된 수상 가운데 2021년 10월 22일–2026년 10월 22일 범위 안의 연도로 적힌 2건이다. 모두 서울대 부임 전 삼성전자 재직 시기의 수상이다.[^snuti]

- 2025 · 삼성전자 Device Solution 부문 최우수 논문상
- 2024 · 삼성전자 S.LSI 사업부 최우수 특허상

## 연락과 위치

- 교수 연구실: 서울특별시 관악구 관악로 1 서울대학교 18동 422호[^snuti][^contact]
- 전화: 02-880-8476(첨단융합학부·전기·정보공학부 교수 소개 표기)[^snuti][^ece]
- 교수 이메일: junseok.park@snu.ac.kr[^professor][^contact]
[^home]: AI SOC Lab, 첫 화면. <https://sites.google.com/snu.ac.kr/soc/home>. 연구실명과 특정 계산용 하드웨어 시스템, 컴퓨터 구조·VLSI 설계·하드웨어와 소프트웨어의 공동 설계·메모리 내 처리 구조를 다룬다는 설명, 현재 개발 방향. 2026-10-26 열람.
[^research]: AI SOC Lab, Research. <https://sites.google.com/snu.ac.kr/soc/research>. 온디바이스 인공지능 응용용 차세대 인공지능 시스템 온 칩을 개발한다는 문장과 심층 신경망 가속기·인공지능 시스템 온 칩·메모리 내 처리 구조의 세 연구 갈래. 2026-10-26 열람.
[^ece]: 서울대학교 전기·정보공학부, 박준석 조교수 소개. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p920>. 이름·직위·학위·연구 관심·연락처·누리집 연결. 인공지능용 집적회로와 시스템 및 디지털 시스템 온 칩·응용 특화 프로세서와 가속기를 설계한다는 설명. 2026-10-26 열람.
[^snuti]: 서울대학교 첨단융합학부, 박준석 조교수 소개. <https://snuti.snu.ac.kr/snu__professor/%EB%B0%95%EC%A4%80%EC%84%9D/>. 차세대지능형반도체전공, 첨단융합학부 조교수와 전기·정보공학부 겸무(각각 2026년 3월부터), 학력·삼성전자 경력·수상·연락처. 2026-10-26 열람.
[^professor]: AI SOC Lab, Professor. <https://sites.google.com/snu.ac.kr/soc/members/professor>. 이름·직위·서울대 부임 시점·학력·산업체 경력·학교 이메일·수상. 2026-10-26 열람.
[^members]: AI SOC Lab, Researchers. <https://sites.google.com/snu.ac.kr/soc/members/researchers>. M.S./Ph.D. Students의 Narim Kim, Interns의 Junho Park·Seungwoo Son 및 학교 이메일. 2026-10-26 열람.
[^conferences]: AI SOC Lab, International Conference. <https://sites.google.com/snu.ac.kr/soc/publication/international-conference>. 2010–2025년 구역의 논문 목록 중 2021·2022·2025년 구역 5편. 2026-10-26 열람.
[^journals]: AI SOC Lab, Journals. <https://sites.google.com/snu.ac.kr/soc/publication/journals>. 2011–2025년 구역의 논문 목록 중 2025년 구역 1편. 2026-10-26 열람.
[^contact]: AI SOC Lab, Contact. <https://sites.google.com/snu.ac.kr/soc/contact>. 교수 사무실과 학교 이메일. 2026-10-26 열람.

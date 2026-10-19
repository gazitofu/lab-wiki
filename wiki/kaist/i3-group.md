# I³ Group (Intelligence, Imaging & Integration Group)

**KAIST 전기및전자공학부 · 강익성 교수**

- 분야: 계산 현미경(computational microscopy), 적응 광학, 물리 기반 인공지능 영상 복원, X선 3차원 나노 영상, 반도체 비파괴 계측
- 홈페이지: <http://kangimaging.com/>
- 근거와 출처: [I³ Group 근거 페이지](i3-group-sources.md)

> 렌즈·측정 장치와 인공지능을 함께 설계해, 살아 있는 쥐의 뇌 속 신경세포나 반도체 칩 내부 같은 작은 3차원 구조를 부수지 않고 선명하게 보는 영상 기술을 만든다. 2026년 1월 KAIST에서 새로 문을 연 연구실이다.[^home][^research][^news]

## 무엇을 연구하나

연구실은 비파괴·고해상도 3차원 영상을 위한 계산 현미경을 연구한다. 광학 장치, 측정 방식, 복원 알고리즘을 함께 설계하고, 단층 촬영·라미노그래피·타이코그래피(빛을 여러 위치에서 비추고 회절 무늬로 영상을 되살리는 기법)처럼 측정값에 간접적으로 담긴 3차원 구조를 역문제(결과에서 원인을 거꾸로 추정하는 문제)로 풀어낸다.[^research] 빛이 적거나 각도가 제한되거나 수차(렌즈·시료 때문에 생기는 영상 왜곡)와 산란이 있으면 이 추정이 어려워, 영상이 만들어지는 물리 모형과 인공지능을 결합해 구조와 장치 변수를 함께 추정한다.[^research]

첫 번째 응용은 **생체 영상의 적응 광학**이다. 적응 광학은 시료가 일으키는 빛의 왜곡을 측정·보정해 선명한 영상을 되찾는 기술인데, 보통 값비싼 파면(빛의 물결이 같은 위상으로 이어진 면) 측정 장치가 필요하다. 교수는 별도 학습 데이터 없이 3차원 영상 묶음 하나만으로 빛의 왜곡과 시료 구조를 함께 추정하는 인공지능(CoCoA)을 만들어 살아 있는 쥐 뇌의 광시야 현미경(넓은 영역을 한 번에 비춰 찍는 현미경) 영상에 썼고,[^p2] 이를 이광자 현미경(빛 알갱이 두 개를 동시에 흡수시켜 깊은 조직을 찍는 현미경)으로 넓힌 NeAT는 상용 현미경에서도 실시간으로 왜곡을 보정해 쥐 뇌의 시냅스·신경세포 신호를 더 정확하게 쟀다.[^p1]

두 번째 응용은 **광학·X선 계측과 검사**다. 반도체 집적회로 내부를 X선으로 3차원 촬영하려면 여러 각도의 측정에 오랜 시간이 걸린다. 교수는 측정 각도를 크게 줄이고도 인공지능으로 정밀하게 복원하는 방법(APT, RAPID, 정답 영상 없이 측정 데이터만으로 배우는 자기 지도 학습 라미노그래피)을 개발했다.[^p4][^p5][^p6] 연구실은 빛을 일부러 적게 쓰거나 각도를 줄여 검사를 크게 빠르게 하는 방향을 목표로 든다.[^research]

이 밖에 렌즈 없는 홀로그래피 현미경,[^p7] 제한된 각도의 단층 촬영을 순환 신경망(순서가 있는 데이터를 차례로 처리하는 인공지능)으로 푸는 방법,[^p8] 신경세포 전압 변화를 초당 5천 번 넘게 기록하는 압축 측정 장치 공동 연구가 있다.[^p3]

## 주요 연구 주제

### 1. 계산 적응 광학 현미경

신경장(neural field) 기반 수차 추정·보정, 시료–수차 동시 추정.[^p1][^p2][^research] 대표 논문 1, 2.

### 2. X선 3차원 나노 영상과 반도체 계측

적은 각도 타이코-단층 촬영, 라미노그래피, 광자 부족 영상.[^p4][^p5][^p6][^research] 대표 논문 4, 5, 6.

### 3. 계산 영상 일반

렌즈 없는 홀로그래피, 제한 각도 단층 촬영, 압축 측정.[^p3][^p7][^p8] 대표 논문 3, 7, 8.

## 대표 논문

교수 개인 누리집과 랩 논문 페이지의 2021–2026년 학술지 논문이다. 랩 논문 페이지는 대표 논문 1(2026)을 KAIST 부임 뒤 논문으로, 나머지를 부임 전 미국 MIT·UC 버클리 시기 논문으로 나눈다. 저자 역할은 랩 논문 페이지 표기(† 공동 교신, * 공동 1저자)를 따랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^labpubs] |
|---|---|---|---|---|
| 1 | 2026 | [Adaptive optical correction for in vivo two-photon fluorescence microscopy with neural fields](https://doi.org/10.1038/s41592-026-03053-6) · Nature Methods | 이광자 형광 현미경에서 빛의 왜곡과 시료 구조를 3차원 영상 묶음만으로 함께 추정하는 계산 틀(NeAT). 시료 움직임 보정까지 넣어 상용 현미경에서도 쓸 수 있게 했고, 살아 있는 쥐 뇌에서 실시간 보정으로 시냅스·신경세포의 활동을 보여 주는 글루탐산·칼슘 신호를 더 정확히 쟀다.[^p1] | 1저자·공동 교신 강익성, 공동 교신 Na Ji |
| 2 | 2024 | [Coordinate-based neural representations for computational adaptive optics in widefield microscopy](https://doi.org/10.1038/s42256-024-00853-3) · Nature Machine Intelligence | 외부 학습 데이터 없이 3차원 영상 묶음 하나로 파면 왜곡과 시료 구조를 함께 추정하는 자기 지도 학습 알고리즘(CoCoA). 쥐 뇌 조직의 광시야 현미경 영상에 적용해 파면 측정 장치를 쓴 방식과 비교 검증했다.[^p2] | 1저자·공동 교신 강익성, 공동 교신 Qinrong Zhang |
| 3 | 2025 | [Optical segmentation-based compressed readout of neuronal voltage dynamics](https://doi.org/10.1038/s41467-025-62663-4) · Nature Communications | 관심 영역마다 검출기 픽셀 하나를 배정해 신호를 압축해 읽는 측정 방식. 빛의 방향·위상을 픽셀마다 바꾸는 공간 광 변조기 두 개와 마이크로렌즈 배열로 만들었고, 신경 회로의 전압 변화를 초당 5천 번 넘게 기록했다.[^p3] | 1저자 Seonghoon Kim, 강익성 공저, 마지막 저자 Myunghwan Choi |
| 4 | 2023 | [Accelerated deep self-supervised ptycho-laminography for three-dimensional nanoscale imaging of integrated circuits](https://doi.org/10.1364/OPTICA.492666) · Optica | 평평한 집적회로를 X선으로 3차원 촬영하는 타이코-라미노그래피에서, 물리 제약을 넣은 자기 지도 딥러닝으로 측정 각도를 16분의 1로 줄이고 계산을 4.67배 빠르게 했다.[^p4] | 1저자 강익성, 마지막 저자 George Barbastathis |
| 5 | 2023 | [Attentional Ptycho-Tomography (APT) for three-dimensional nanoscale X-ray imaging with minimal data acquisition and computation time](https://doi.org/10.1038/s41377-023-01181-8) · Light: Science & Applications | 집적회로 내부 패턴과 X선 전파 물리를 학습에 넣은 인공지능으로, 측정 각도를 12분의 1로 줄여도 기존 표준 방법과 비슷한 정확도로 3차원 영상을 복원했다.[^p5] | 공동 1저자 강익성·Ziling Wu(누리집 * 표기), 마지막 저자 George Barbastathis |
| 6 | 2023 | [Three-dimensional nanoscale reduced-angle ptycho-tomographic imaging with deep learning (RAPID)](https://doi.org/10.1186/s43593-022-00037-9) · eLight | 물체 일부를 충분한 각도로 찍어 학습한 뒤 나머지는 적은 각도만 찍어 복원하는 X선 타이코-단층 촬영. 349개 각도를 21개로 줄여 전체적으로 140배 빠르게 했다.[^p6] | 공동 1저자 Ziling Wu·강익성, 마지막 저자 George Barbastathis |
| 7 | 2022 | [Simultaneous spectral recovery and CMOS micro-LED holography with an untrained deep neural network](https://doi.org/10.1364/OPTICA.470712) · Optica | 일반 반도체 공정으로 만든 아주 작은 실리콘 마이크로 LED를 광원으로 쓰는 렌즈 없는 홀로그래피 현미경. 학습하지 않은 신경망이 회절 무늬 하나에서 영상과 광원 스펙트럼을 함께 되살린다.[^p7] | 공동 1저자 강익성·Marc de Cea(누리집 * 표기), 마지막 저자 Rajeev Ram |
| 8 | 2021 | [Dynamical machine learning volumetric reconstruction of objects' interiors from limited angular views](https://doi.org/10.1038/s41377-021-00512-x) · Light: Science & Applications | 여러 각도에서 찍은 영상을 시간에 따라 변하는 동적 시스템처럼 보고, 순환 신경망으로 제한된 각도의 단층 촬영 복원을 개선했다.[^p8] | 1저자 강익성, 마지막 저자 George Barbastathis |

## 교수와 전문 분야

강익성 교수는 서울대 전기정보공학부 학사(2017), 미국 MIT 전기공학·컴퓨터과학과 석사(2020)와 박사(2022)를 받았다. MIT에서 George Barbastathis 교수의 지도를 받았고 박사 과정 내내 한국고등교육재단 장학생이었다. UC 버클리에서 Na Ji·Stella X. Yu 교수와 박사후연구원(2022–2025)으로 일한 뒤, 2026년 1월 KAIST 전기및전자공학부 조교수(정년 트랙)로 부임했다.[^home][^team] 학부는 주요 연구로 계산 영상, 물리 기반 인공지능, 적응 광학과 현미경, 3차원 계측을 적는다.[^ee]

논문으로 보면 전문 분야는 세 갈래다.

- **계산 적응 광학**: 신경장으로 수차와 구조를 함께 추정.[^p1][^p2]
- **X선 3차원 나노 영상**: 적은 각도 촬영과 딥러닝 복원.[^p4][^p5][^p6]
- **계산 영상 하드웨어·알고리즘**: 렌즈 없는 홀로그래피, 제한 각도 단층 촬영.[^p7][^p8]

## 응용 분야

대표 논문으로 보면 살아 있는 뇌 영상 같은 생명과학 연구, 반도체 집적회로의 비파괴 3차원 검사, 소형 현미경에 닿아 있다.[^p1][^p4][^p7] 연구실은 2026년 한국연구재단 우수신진연구 과제를 받았고, KAIST 광학 인공지능(PICORE) 센터와 기초연구실(BRL) 연구팀에 참여한다.[^news]

## 구성원

2026년 10월 19일 랩 팀 페이지 기준이다. 연구 주제는 랩 표기를 옮겼다.[^team] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Bonha Woo | 석사과정 | Computational Microscopy; Adaptive Optics |  |
| Yunkyu Lee | 연구원 | Computational Microscopy; Adaptive Optics |  |
| Hyeonbin Jo | 학부 연구생 | Computational Metrology; Holography |  |
| Hoseung Bin | 학부 연구생 | Computational Microscopy; Adaptive Optics |  |
| Donghyuk Lee | 학부 연구생 | Computational Microscopy; Adaptive Optics |  |
| Seungjun Ahn | 학부 연구생 | Computational Metrology; Holography |  |

## 최근 논문 목록 (2021–2026)

교수 개인 누리집 논문 목록의 2021–2026년 학술지 논문 8편(대표 논문과 같다)이다. 사전 공개 논문과 학술대회 발표는 누리집 목록에 따로 있다.[^papers]

**2026**

- Kang I\*, Kim H, Natan R, Zhang Q, Yu SX, Ji N\*. "Adaptive optical correction for in vivo two-photon fluorescence microscopy with neural fields". *Nature Methods (2026)*.

**2025**

- Kim S, Yoon J, Ko G, Kang I, Tian H, Fan LZ, Li Y, Cohen AE, Wu J, Dai Q, Choi MM. "Optical segmentation-based compressed readout of neuronal voltage dynamics". *Nature Communications (2025) 16(7194)*.

**2024**

- Kang I\*, Zhang Q\*, Yu SX, Ji N. "Coordinate-based neural representations for computational adaptive optics in widefield microscopy". *Nature Machine Intelligence (2024) 6, 714-725*.

**2023**

- Kang I, Jiang Y, Holler M, Guizar-Sicairos M, Levi AFJ, Klug J, Vogt S, Barbastathis G. "Accelerated deep self-supervised ptycho-laminography for three-dimensional nanoscale imaging of integrated circuits". *Optica (2023) 10(8), 1000-1008*.
- Kang I\*, Wu Z\*, Jiang Y, Yao Y, Deng J, Klug J, Vogt S, Barbastathis G. "Attentional Ptycho-Tomography (APT) for three-dimensional nanoscale X-ray imaging with minimal data acquisition and computation time". *Light: Science & Applications (2023) 12(131)*.
- Wu Z\*, Kang I\*, Yao Y, Jiang Y, Deng J, Klug J, Vogt S, Barbastathis G. "Three-dimensional nanoscale reduced-angle ptycho-tomographic imaging with deep learning (RAPID)". *eLight (2023) 3(7)*.

**2022**

- Kang I\*, de Cea M\*, Xue J, Li Z, Barbastathis G, Ram R. "Simultaneous spectral recovery and CMOS micro-LED holography with an untrained deep neural network". *Optica (2022) 9(10), 1149-1155*.

**2021**

- Kang I\*, Goy A, Barbastathis G. "Dynamical machine learning volumetric reconstruction of objects’ interiors from limited angular views". *Light: Science & Applications (2021) 10(74)*.

## 연락과 위치

- 교수 이메일: iksung.kang@kaist.ac.kr[^ee]
- 교수 전화: 042-350-7483[^ee]
- 위치: KAIST LG이노베이션홀(N24) 3113호 (대전 유성구 대학로 291)[^ee][^home]

[^home]: 교수 개인 누리집 <https://iksungk.github.io/> (2026-10-19 열람)
[^labpubs]: 랩 논문 페이지 <http://kangimaging.com/publications/> (2026-10-20 열람)
[^papers]: 교수 개인 누리집 논문 목록 <https://iksungk.github.io/publications.html> (2026-10-19 열람)
[^research]: 랩 연구 페이지 <http://kangimaging.com/research/> (2026-10-20 열람)
[^team]: 랩 팀 페이지 <http://kangimaging.com/team/> (2026-10-20 열람)
[^news]: 랩 소식 페이지 <http://kangimaging.com/news/> (2026-10-20 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(강익성) <https://ee.kaist.ac.kr/professor/%EA%B0%95%EC%9D%B5%EC%84%B1/> (2026-10-19 열람)
[^p1]: I. Kang 외, N. Ji, Nature Methods 23, 1037-1046 (온라인 2026-04-13). <https://doi.org/10.1038/s41592-026-03053-6> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: I. Kang, Q. Zhang, S. X. Yu, N. Ji, Nature Machine Intelligence 6, 714-725 (온라인 2024-06-24). <https://doi.org/10.1038/s42256-024-00853-3> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: S. Kim 외, M. Choi, Nature Communications 16, 7194 (온라인 2025-08-05). <https://doi.org/10.1038/s41467-025-62663-4> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: I. Kang 외, G. Barbastathis, Optica 10, 1000 (온라인 2023-07-26). <https://doi.org/10.1364/optica.492666> 초록 기준.
[^p5]: I. Kang 외, G. Barbastathis, Light: Science & Applications 12, 131 (온라인 2023-05-30). <https://doi.org/10.1038/s41377-023-01181-8> 초록 기준.
[^p6]: Z. Wu 외, G. Barbastathis, eLight 3, 7 (온라인 2023-04-03). <https://doi.org/10.1186/s43593-022-00037-9> 초록 기준.
[^p7]: I. Kang 외, R. J. Ram, Optica 9, 1149 (온라인 2022-10-11). <https://doi.org/10.1364/optica.470712> 초록 기준.
[^p8]: I. Kang, A. Goy, G. Barbastathis, Light: Science & Applications 10, 74 (온라인 2021-04-07). <https://doi.org/10.1038/s41377-021-00512-x> 초록 기준.

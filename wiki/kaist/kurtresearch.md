# Kurt Research

**KAIST 전기및전자공학부 · 함자 쿠르트 교수**

- 영문 연구실 이름: Metaphotonics Research Lab at KAIST
- 분야: 나노광학, 실리콘 광회로 역설계, 빛을 이용한 계산, 광 위상 배열 거리 측정[^about][^research]
- 대분야: 전기전자·반도체·광학, 물리·양자
- 태그: 광집적회로[^research], 메타물질·메타광학[^research], 라이다·3차원 거리 센싱[^research], 태양전지[^research], 설계 최적화(위상·형상 최적화)[^research]
- 홈페이지: <https://kurtresearch.com>
- 근거와 출처: [Kurt Research 근거 페이지](kurtresearch-sources.md)

> 빛이 지나가는 구조를 설계해 칩 위에서 빛을 나누고 방향을 바꾸며, 이를 계산과 거리 측정에 연결하는 연구실이다. 원하는 기능에서 구조를 거꾸로 찾는 역설계, 실리콘 광회로, 빛으로 계산하는 신경망, 메타표면과 태양전지를 연구한다.[^research]

## 무엇을 연구하나

함자 쿠르트 교수가 이끄는 연구실은 나노광학(빛의 파장과 비슷하거나 그보다 작은 구조에서 빛과 물질의 상호작용을 다루는 분야)을 연구한다. 파장은 파동의 같은 진동 상태가 공간에서 되풀이되는 간격이다. 연구 대상은 빛이 지나가는 재료와 구조이며, 이를 광집적회로(빛을 보내고 나누고 바꾸는 광학 부품을 한 칩 위에 모은 회로)로 구현한다.[^research] 누리집은 연구 그룹이 2008년부터 활동해 왔다고 소개하며, 현재 구성원 쪽은 KAIST 전기및전자공학부의 Metaphotonics Research Lab이라는 이름을 쓴다.[^home][^members]

중심 방법은 역설계(원하는 기능을 먼저 정하고 그 기능을 내는 구조를 찾는 설계)다. 연구실은 구조를 바꿔 가며 시험하는 방법과 함께, 목표에서 벗어난 정도를 줄이도록 설계 변수를 조절하는 최적화 방법을 다룬다. 굴절률(진공에서의 빛의 속도를 재료 속에서의 빛의 속도로 나눈 값)의 공간적 배치를 설계하고, 빛을 나누거나 원하는 곳으로 전달하는 부품을 만든다. 연구 소개는 최적화 계산과 학습 방법으로 복잡한 광학 구조를 설계하는 것을 주요 갈래로 설명한다.[^research]

또 다른 갈래는 빛으로 계산하는 회로다. 신경망(계산 단위들의 연결과 그 연결의 가중치를 학습해 입력을 출력으로 바꾸는 모형)의 연산을 광학 부품에 옮기려 한다. 연구 소개에는 실리콘을 바탕으로 입력을 받아 가중치를 곱하고, 비선형 활성화(입력 크기에 단순히 비례하지 않는 규칙으로 계산 결과를 바꾸는 단계)를 수행하는 분류용 광 신경망 처리 회로의 설계·제작이 나온다. 광 위상 배열(여러 빛 방출부의 진동 주기상 위치인 위상을 조절해 합쳐진 빛의 방향을 바꾸는 장치)도 연구한다. 이를 이용하는 라이다는 빛을 쏘고 되돌아오는 시간을 재어 물체까지의 거리와 입체 모양을 알아내는 센서다.[^research]

메타표면(파장보다 작은 인공 구조를 평면에 배열해 빛의 성질을 조절하는 표면)과 평면 광학도 주요 대상이다. 구조의 배열로 빛의 위상, 진폭(진동이 기준 상태에서 벗어나는 최대 크기), 편광(빛을 이루는 전기장의 진동 방향과 그 변화 양상)을 바꾸고 빛을 꺾거나 모으는 기능을 연구한다.[^research] 전기장은 전하를 띤 물체가 전기력을 받는 공간의 상태이며, 전하는 물체가 전기력을 주고받게 하는 물리량이다. 태양전지에서는 빛을 받아 전기를 만드는 실리콘 소자(특정 기능을 수행하는 기본 부품)가 빛을 충분히 흡수하도록 표면과 내부 구조를 설계한다.[^research] 반사를 줄이거나 빛을 내부에 가두는 방법들을 함께 탐구하는 것이 목표다.[^research]

연구 소개는 빛의 증폭과 감쇠(세기가 줄어드는 것)를 균형 있게 배치한 구조의 광학 현상과, 구조의 경계를 따라 빛을 전달하는 원리도 다룬다. 전자는 빛을 키우는 부분과 줄이는 부분의 배치가 새로운 빛 전달 현상을 만드는 연구이고, 후자는 구조의 결함이나 무질서가 있어도 빛을 안정적으로 전달할 가능성을 살피는 연구다.[^research]

## 주요 연구 주제

### 1. 역설계로 만드는 실리콘 광회로

광 분배기(들어온 빛을 여러 출력으로 나누는 부품), 도파로(빛을 특정 경로 안에 가두어 전달하는 구조)의 굽힘, 온도로 기능을 바꾸는 부품을 설계한다. 원하는 출력과 손실을 목표로 재료의 배치나 구조의 치수를 조절하며, 실제 제작한 부품의 동작을 계산 결과와 연결한다.[^research] 대표 논문 2·6·7은 온도 조절, 빛의 분배, 급하게 꺾이는 경로를 각각 다룬다.[^p2][^p6][^p7]

### 2. 광 신경망과 광 논리 연산

여러 광학 부품을 연결해 계산을 수행하는 구조를 연구한다. 대표 논문 1은 광 신경망의 부품과 전체 구조, 구현의 한계를 정리한 리뷰이고, 대표 논문 3은 빛의 간섭(여러 빛의 진동이 겹쳐 세기 분포가 달라지는 현상)을 이용해 논리 연산과 두 입력의 크기 비교를 수행하는 부품을 제작한 연구다.[^research][^p1][^p3]

### 3. 광 위상 배열과 라이다

실리콘 광회로에서 빛이 나가는 방향을 조절해 주변을 살피고, 되돌아온 빛에서 거리를 알아낸다. 연구 소개는 기계적으로 움직이는 장치 대신 칩 위의 광 위상 배열을 쓰는 방식을 설명한다. 대표 논문 5는 방출부를 조절하는 광 위상 배열과 빛의 왕복 시간을 이용해 물체를 입체 영상으로 나타낸 연구다.[^research][^p5]

### 4. 메타표면과 태양전지의 빛 관리

평면에 배치한 인공 구조로 빛을 꺾거나 모으고, 실리콘 태양전지에서 빛의 반사를 줄이고 흡수를 높이는 구조를 설계한다. 연구 소개는 표면의 형태와 굴절률 배치, 빛의 진행을 늦추거나 특정 빛을 가려내는 구조 등을 함께 탐구할 방향으로 든다.[^research]

## 대표 논문

KAIST 재직 시기의 2022–2026년 논문 가운데 연구 갈래, 저자 순서, 초록을 고려해 일곱 편을 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. 주요 저자 칸의 역할은 전체 저자 순서에 따른다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [On-Chip Photonic Neural Network Architectures](https://doi.org/10.1002/adom.71567) · Advanced Optical Materials | 칩 위에서 빛으로 신경망 계산을 구현하는 기술을 정리한 리뷰다. 계산을 맡는 광학 부품과 여러 신경망 구조를 함께 살피고, 정밀도·전력 효율·회로를 모으는 복잡성 사이의 관계를 비교한다. 규모 확대와 비선형 기능 구현 등 실제 시스템으로 발전시키기 위해 해결할 과제도 정리한다.[^p1] | 1저자 Seokjin Hong, 마지막 저자 Hamza Kurt |
| 2 | 2026 | [Multifunctionality in Silicon Photonics Through Temperature-Driven Inverse Design](https://doi.org/10.1002/lpor.71717) · Laser & Photonics Reviews | 온도에 따라 실리콘의 광학적 성질이 달라지는 효과를 역설계에 함께 넣어, 하나의 구조가 여러 광학 기능을 수행하도록 했다. 빛의 경로를 바꾸는 스위치와 빛의 전달 형태를 바꾸는 변환기를 설계하고 실험으로 동작을 확인했다. 온도 조절에 따른 기능 변화와 계산 결과가 잘 맞았다.[^p2] | 1저자 Berkay Neseli, 마지막 저자 Hamza Kurt |
| 3 | 2025 | [Topology-Optimized Interference-Based Compact Photonic Logic Units](https://doi.org/10.1021/acsphotonics.5c00026) · ACS Photonics | 빛의 간섭과 역설계를 이용해 논리곱·논리합 연산을 하는 부품과 두 입력의 크기를 비교하는 부품을 만들었다. 논리곱은 두 조건이 모두 참일 때, 논리합은 하나라도 참일 때 참을 내는 연산이다. 실리콘을 절연층 위에 얹은 구조에 부품을 제작했고, 실험 결과가 계산과 잘 맞았다.[^p3] | 1저자 Berkay Neseli, 마지막 저자 Hamza Kurt |
| 4 | 2024 | [Semi-Supervised Learning Leveraging Denoising Diffusion Probabilistic Models for the Characterization of Nanophotonic Devices](https://doi.org/10.1002/lpor.202300998) · Laser & Photonics Reviews | 광학 부품의 특성을 학습하려면 빛의 진행을 계산하는 데 많은 시간이 필요하다는 문제를 다뤘다. 생성 모형(학습한 자료의 특성을 바탕으로 새로운 자료를 만드는 모형)으로 정답 표시가 없는 자료를 활용하고, 그 자료에 예측한 정답을 붙여 학습에 이용했다. 빛을 전달하는 구조를 대상으로 정답 표시가 있는 자료만 쓰는 학습과 비교해, 추가 수치 계산 없이 신경망의 성능을 높일 수 있음을 보였다.[^p4] | 1저자 Junhyeong Kim, 마지막 저자 Hamza Kurt |
| 5 | 2023 | [Demonstration of high-accuracy 3D imaging using a Si optical phased array with a tunable radiator](https://doi.org/10.1364/oe.481229) · Optics Express | 빛의 방출부를 조절하는 실리콘 광 위상 배열로 빛을 두 방향으로 조향하고, 빛의 왕복 시간으로 거리를 측정했다. 이를 위해 빛의 짧은 신호를 만드는 부품도 개발했다. 이 시스템으로 장난감 모형을 입체 영상으로 나타냈다.[^p5] | 1저자 Jinhyeong Yoon, 공저자 Hamza Kurt, 마지막 저자 Hyo-Hoon Park |
| 6 | 2022 | [Experimental demonstration of inverse-designed silicon integrated photonic power splitters](https://doi.org/10.1515/nanoph-2022-0443) · Nanophotonics | 길이가 서로 다른 실리콘 막대들을 배치해 하나의 입력을 네 출력으로 나누는 광 분배기 두 종류를 역설계했다. 계산으로 빛의 손실을 줄이고 출력이 고르게 나뉘도록 구조를 찾았다. 기존 반도체 제작 공정과 호환되는 방식으로 칩을 제작했으며, 실험과 계산이 잘 맞았다.[^p6] | 1저자 Junhyeong Kim, 마지막 저자 Hamza Kurt |
| 7 | 2026 | [Low-Loss Routing of Strongly Confined Light in Ultra-Compact Silicon Slot-Waveguide Bends](https://doi.org/10.1002/nap2.70260) · Nanophotonics | 두 실리콘 띠 사이의 틈에 빛을 모아 보내는 도파로가 급하게 꺾일 때 생기는 손실을 줄이려 했다. 두 띠의 폭을 서로 다르게 조절해 굽힘 구간에서 빛의 분포가 변한 뒤 출력에서 필요한 전달 형태를 되찾게 했다. 여러 굽힘이 이어진 구조에서도 빛의 전달을 실험으로 확인했다.[^p7] | 1저자 Ji-Hwan Park, 마지막 저자 Hamza Kurt |

## 교수와 전문 분야

함자 쿠르트(Hamza Kurt)는 KAIST 전기및전자공학부 교수이며 MetaPhotonics Research Lab을 이끈다.[^ee][^members] Middle East Technical University에서 전기전자공학 학사(2000), University of Southern California에서 전기공학 석사(2002), Georgia Tech에서 전기·컴퓨터공학 박사(2006)를 받았다.[^members] 2021년 7월 8일 출판된 논문에는 KAIST 전기및전자공학부 소속 공저자로 기재되어 있다.[^aff]

전문 분야는 나노광학 구조와 실리콘 광회로를 원하는 기능에 맞춰 설계하는 방법이다. 최근 논문에는 광학 부품의 역설계와 제작, 학습을 이용한 부품 특성 예측, 빛으로 계산하는 회로가 함께 나타난다.[^p2][^p3][^p4][^p6][^p7] 학부 교수 소개는 나노광학, 인공지능 기반 광학, 역설계, 메타표면, 광결정(굴절률이 파장 정도의 간격으로 주기적으로 달라지는 구조), 태양전지, 빛의 진행을 늦추는 구조와 빛을 우회시키는 광학적 은폐를 주요 연구로 적는다.[^ee]

## 응용 분야

광 신경망과 칩 위의 광학 계산, 빛을 원하는 출력으로 나누고 전달하는 광회로, 물체까지의 거리와 입체 모양을 재는 라이다가 주요 응용이다.[^research][^p1][^p3][^p5][^p6] 메타표면을 이용하는 평면 광학 부품과 빛을 효율적으로 흡수하는 태양전지 구조도 연구한다.[^research]

## 구성원

연구실 Members 쪽의 현재 대학원생 10명과 학부생·인턴 구획 9명이다. 과정과 연구 주제는 게시 표기이며, 시작 날짜는 합류 소식 또는 이름 옆의 인턴 기간 표기다. 「대표 논문 참여」는 전체 저자 목록에서 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members][^welcome]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Seokjin Hong (홍석진) | 석박사통합과정 (Ph.D. Candidate) | 2022-03-01 | Neuromorphic Photonics, Photonic Compting, Optical Phased Array |  | 1, 2, 3, 4, 7 |
| Berkay Neseli | 박사과정 | 2022-03-01 |  |  | 1, 2, 3, 4, 7 |
| Ji-Hwan Park (박지환) | 박사과정 |  | Computational Photonics |  | 7 |
| Rong Shi | 박사과정 |  |  |  |  |
| Seungsoo Lee (이승수) | 석박사통합과정 (Ph.D. Candidate) |  | Photonic Integrated Circuit, Optical Phased Arrays | sslee@kaist.ac.kr | 1, 2 |
| Seung-Yoon Choi (최승윤) | 박사과정 |  | Optical Phased Array, Metasurfaces, AI for Photonics |  | 2 |
| Junyeop Lee (이준엽) | 석박사통합과정 (Ph.D. Candidate) |  | Photonic Integrated Circuit, Quantum Photonics, Metasurfaces |  | 2 |
| Yeonjun Kim (김연준) | 석박사통합과정 (Ph.D. Candidate) |  | Co-Packaged Optics, PCM |  | 1, 2 |
| Seungyeon Cho (조승연) | 박사과정 |  |  |  | 1 |
| Kipyo Yang (양기표) | 석사과정 |  | Photonic Integrated Circuit |  |  |
| Sanghyun Joo | 학부생·인턴 (구획 표기) |  |  |  |  |
| Jaeyeon Eom | 학부생·인턴 (구획 표기) |  |  |  |  |
| Hojun Lee | 인턴 | 2025 Winter |  |  |  |
| Hoeseong Kim | 인턴 | 2025 Summer |  |  |  |
| Jiho Lim | 학부생·인턴 (구획 표기) |  |  |  |  |
| Donggeon Lee | 학부생·인턴 (구획 표기) |  |  |  |  |
| Youngmin Song | 학부생·인턴 (구획 표기) |  |  |  |  |
| Sumin Jeon | 학부생·인턴 (구획 표기) |  |  |  |  |
| Mammadova Fakhriyya | 학부생·인턴 (구획 표기) |  |  |  |  |

## 졸업생 진로

연구실 Members 쪽 Alumni 목록의 서로 다른 게시 항목 36행이다. 이 목록에는 이전 소속인 TOBB ETÜ에서 받은 학위가 함께 들어 있다. 학교를 적은 31행은 TOBB ETÜ 표기를 유지했고, 학교를 적지 않은 5행은 기관을 덧붙이지 않았다. 학위·연도·진로는 게시 표기다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jaeyong Kim | PhD, 2025 | SK Hynix |
| Namhyun Kwon | PhD, 2025 | Lessengers |
| Junhyeong Kim | PhD, 2025 | SK Hynix |
| Jinhyeong Yoon | PhD, 2024 | SK Hynix |
| Sabaina Irfan | MSc, 2023 |  |
| Emre Bor | MSc, TOBB ETÜ, 2016→ PhD, TOBB ETÜ, 2020 |  |
| Ceren Babayigit | MSc, TOBB ETÜ, 2020 |  |
| Cihat Nurettin Yilmaz | MSc, TOBB ETÜ, 2020 |  |
| Nazmi Yilmaz | MSc, TOBB ETÜ, 2020 |  |
| Abdullah Bera Icli | MSc, TOBB ETÜ, 2020 |  |
| Dogukan Apaydin | MSc, TOBB ETÜ, 2020 |  |
| Ahmet Mesut Alpkilic | MSc, TOBB ETÜ, 2020 |  |
| Nur Erim | PhD, TOBB ETÜ, 2019 |  |
| Muhhammed Necip Erim | PhD, TOBB ETÜ, 2019 |  |
| Done Yilmaz | PhD, TOBB ETÜ, 2019 |  |
| Ahmet Ozer | PhD, TOBB ETÜ, 2019 |  |
| Fehim Taha Bagei | MSc, TOBB ETÜ, 2018 |  |
| Utku Gorkem Yasa | MSc, TOBB ETÜ, 2018 |  |
| Zeki Hayran | MSc, TOBB ETÜ, 2018 |  |
| Mediha Tutgun | MSc, TOBB ETÜ, 2018 |  |
| Melike Gumus | MSc, TOBB ETÜ, 2018 |  |
| Ibrahim Halil Giden | PhD, TOBB ETÜ, 2017 |  |
| Khalil Dadashi | PhD, TOBB ETÜ, 2017 |  |
| Aytekin Ozdemir | PhD, TOBB ETÜ, 2017 |  |
| Yusuf Abdulaziz Yilmaz | MSc, TOBB ETÜ, 2017 |  |
| Takiyettin Oyutun Kille | MSc, TOBB ETÜ, 2017 |  |
| Fehmiye Yildiz | MSc, TOBB ETÜ, 2017 |  |
| Mirbek Turduev | PhD, TOBB ETÜ, 2015 |  |
| Melih Goktug Can | MSc, TOBB ETÜ, 2015 |  |
| Bilgehan Baris Oner | MSc, TOBB ETÜ, 2015 |  |
| Ibrahim Halil Giden | MSc, TOBB ETÜ, 2013 |  |
| Done Yilmaz | MSc, TOBB ETÜ, 2013 |  |
| Nur Erim | MSc, TOBB ETÜ, 2013 |  |
| Muhammed Necip Erim | MSc, TOBB ETÜ, 2013 |  |
| Lokman Ayas | MSc, TOBB ETÜ, 2011 |  |
| Kadir Ustun | MSc, TOBB ETÜ, 2011 |  |

## 최근 논문 목록 (2021–2026)

연구실 Publications 쪽의 2021–2026년 구역 중 23편이다. 교수의 이전 소속 시기부터 이어지는 개인 연구 이력을 함께 게시한 목록이며, 현재 KAIST 연구실만의 성과를 뜻하지 않는다. 연도는 누리집의 연도 구역이고, 제목·저자·발표처는 게시 표기다.[^pubs]

**2026**

- J. H. Park, J. -Y. Kim, S. Hong, B. Neseli, H. -H. Park, and H. Kurt. "Low – loss Routing of Strongly Confined Light in Ultra- Compact Silicon Slot – Waveguide Bends". *Nanophotonics, 15(16), e70260 (2026). <https://doi.org/10.1002/nap2.70260>*.
- S. Hong, B. Neseli, S. Cho, S. Lee, Y. Kim, S. Choi, H. -H. Park, M. Turduev, and H. Kurt. "On – Chip Photonic Neural Network Architectures". *Advanced Optical Materials, e71567 (2026). <https://doi.org/10.1002/adom.71567>*.
- B. Neseli, S. Hong, Y. Kim, S. Lee, S. Choi, J. Lee, H. -H. Park, M. Turduev, and H. Kurt. "Multifunctionality in Silicon Photonics Through Temeprature – Driven Inverse Design". *Laser & Photonics Reviews, e71717 (2026). <https://doi.org/10.1002/lpor.71717>*.
- Y. Kim, L. Kulmer, J. -Y. Kim, H. Kurt, J.Leuthold, and H.Wang. "Multibeam optical phased array and monolithically integrated electro-optic modulator for high performance wireless communication". *Journal of Lightwave Technology, 14(14), 3649-3661 (2026). <https://doi.org/10.1109/jlt.2026.3661243>*.

**2025**

- J. -Y. Kim, S. Lee, S. Hong, B. Neseli, S. Choi, H. -H. Park, and H. Kurt. "Experimental demonstration of dula-polarization multiplexed optical phased array empowered by inverse design". *Nanophotonics, 14(14), 2495-2505 (2025). <https://doi.org/10.1515/nanoph-2025-0148>*.
- B. Neseli, J. Kim,. S. Hong, J. -Y. Kim, H. -H. Park, M. Turduev, and H. Kurt. "Topology-Optimized Interference-Based Compact Photonic Logic Units". *ACS Photonics, 12(7), 3435-3446 (2025). <https://doi.org/10.1021/acsphotonics.5c00026>*.
- J. Kim, J. -Y. Kim, J. Kim, Y. Hyeong, B. Neseli, J. -B. You, J. Shim, J. Shin, H. -H. Park, and H. Kurt. "Inverse design of nanophotonic devices enabled by optimization algorithms and deep learning: Recent achievements and future prospects". *Nanophotonoics, 14(2), 121-151 (2025)*.

**2024**

- S. Hong, J. Yoon, J. Kim, B. Neseli, J. -Y. Kim, H. -H. Park, and H. Kurt. "Inverse-designed taper configuration for the enhancement of integrated 1×4 silicon photonic power splitters". *Nanophotonics, 13 (22), 4127-4135 (2024). <https://doi.org/10.1515/nanoph-2024-0295>*.
- N. -H. Kwon, H. Yoon, S. -H. Kim, J. -Y. Kim, J. Kim, J. Yoon, J. -B. You, H. Kurt, and H. -H. Park. "Managing grating parameters for longitudinal steering with 1D optical phased arrays". *IEEE Photonics Technology Letters, 1-4 (2024). <https://doi.org/10.1109/lpt.2024.3449089>*.
- J. Kim, Y. J. Lee, J. -Y. Kim, J. Yoon, H. Yoon, J. -B. You, S. J. Kim, H. Kurt, and H. -H. Park. "High-efficiency thermo-optic control of longitudinal radiation angle in silicon-based optical phased array by leveraging backside air trench structure". *Optics Letters, 49 (15), 4338-4341 (2024). <https://doi.org/10.1364/ol.524469>*.
- J. Kim, B. Neseli, J. Yoon, J. -Y. Kim, S. Hong, H. -H. Park, and H. Kurt. "Semi-supervised learning leveraging denoising diffusion probabilistic models for the characterization of nanophotonic devices". *Laser Photonics Review, 18 (10), 2300998, 1-8 (2024). <https://doi.org/10.1002/lpor.202300998>*.
- S. Irfan, J.Y. Kim, H. Kurt. "Ultra-compact and efficient photonic waveguide bends with different configurations designed by topology optimization". *Scientific Reports, 14 (1), 6453, 1-12, (2024). <https://doi.org/10.1038/s41598-024-53881-9>*.

**2023**

- J.-Y. Kim, J. Kim, J. Yoon, S. Hong, B. Neseli, N. Kwon, J.-B. You, H. Yoon, H.-H. Park, and H. Kurt. "Deep neural network-based phase calibration in integrated optical phased arrays". *Sci. Rep. 13 (1), 19929 (2023). <https://doi.org/10.1038/s41598-023-47004-z>*.
- J. Yoon, J.-Y. Kim, J. Kim, S. Hong, B. Neseli, J. Park, H.-H. Park, and H. Kurt. "Cladding modulated silicon waveguide Bragg grating with TM-polarized light for optical true time delay line". *Applied Physics Letters 123 (19), (2023). <https://doi.org/10.1063/5.0169731>*.
- J. Yoon, J.-Y. Kim, J. Kim, H. Yoon, B. Neseli, H.-H. Park, and H. Kurt. "Inverse design of Si-based high-performance vertical emitting metagrating coupler on 220 nm silicon-on-insulator platform". *Photonics Research 11 (6), 897-905 (2023). <https://doi.org/10.1364/prj.473978>*.
- J. Yoon, H. Yoon, J.-Y. Kim, J. Kim, G. Kang, N.-H. Kwon, H. Kurt, and H.-H. Park. "Demonstration of high-accuracy 3D imaging using a Si optical phased array with a tunable radiator". *Optics Express 31 (6), 9935-9944 (2023). <https://doi.org/10.1364/oe.481229>*.
- J. Kim, B. Neseli, J.-Y. Kim, J. Yoon, H. Yoon, H.-H. Park, H. Kurt. "Inverse design of an on-chip optical response predictor enabled by a deep neural network". *Optics Express 31 (2), 2049-2060 (2023). <https://doi.org/10.1364/oe.480644>*.

**2022**

- B. Neseli, H. Kurt, and M. Turduev. "Curved beam generation and its experimental realization by rectangular prism with asymmetric polynomial back surface". *Physica Scripta 98 (1), 015026 (2022). <https://doi.org/10.1088/1402-4896/acacce>*.
- H. Kocer, Y. Durna, H. Isik, M.C. Soydan, B. Khalichi, A. Ghobadi, H. Kurt, and E. Ozbay. "Uncovering the non-radiative thermal characteristics of a passive radiative cooler under real operating conditions". *Journal of Physics D: Applied Physics 56 (3), 035502 (2022). <https://doi.org/10.1088/1361-6463/ac9fde>*.
- J. Kim, J.-Y. Kim, J. Yoon, H. Yoon, H.-H. Park, and H. Kurt. "Experimental demonstration of inverse-designed silicon integrated photonic power splitters". *Nanophotonics 11 (20), 4581-4590 (2022). <https://doi.org/10.1515/nanoph-2022-0443>*.
- I. Mahariq, I.H. Giden, S. Alboon, W.H.F. Aly, A. Youssef, and H. Kurt. "Investigation and analysis of acoustojets by spectral element method". *Mathematics 10 (17), 3145 (2022). <https://doi.org/10.3390/math10173145>*.
- B. Neşeli, Y.A. Yilmaz, H. Kurt, and M. Turduev. "Inverse design of ultra-compact photonic gates for all-optical logic operations". *Journal of Physics D: Applied Physics 55 (21), 215107 (2022). <https://doi.org/10.1088/1361-6463/ac5660>*.
- M. Ayik, H. Kurt, O.V. Minin, I.V. Minin, and M. Turduev. "Multi-Directional Cloak Design by All-Dielectric Unit-Cell Optimized Structure". *Nanomaterials 12 (23), 4194 (2022). <https://doi.org/10.3390/nano12234194>*.

## 수상과 선정

연구실이 학회 이름과 연도로 게시한 2023년 수상 1건이다.[^award]

- 2023 · Jinhyeong Yoon이 Optica APC 2023에서 Best Student Paper Award를 받았다.

## 연락과 위치

- 교수 이메일: hamzakurt@kaist.ac.kr[^about]
- 연구실 문의 이메일: sslee@kaist.ac.kr(이승수 박사과정)[^members]
- 교수 전화: +82-42-350-7465[^members]
- 교수 연구실: KAIST 전기및전자공학부동 E3-2 2223호[^members][^ee]
- 실험실: E3-2 2231·2232호[^members]

## 각주
[^home]: Kurt Research, 첫 화면. <https://kurtresearch.com> 관측 2026-11-09.
[^about]: Kurt Research, About Us. <https://kurtresearch.com/about-us> 관측 2026-11-09.
[^research]: Kurt Research, Research Areas. <https://kurtresearch.com/research-areas> 관측 2026-11-09.
[^members]: Kurt Research, Members. <https://kurtresearch.com/members> 관측 2026-11-09.
[^pubs]: Kurt Research, Publications. <https://kurtresearch.com/publications> 관측 2026-11-09.
[^ee]: KAIST 전기및전자공학부, 함자 쿠르트 교수 소개. <https://ee.kaist.ac.kr/professor/17422/> 관측 2026-11-09.
[^welcome]: Kurt Research, Welcom on board, Welcome on Board [2022-03-01]. <https://kurtresearch.com/welcom-on-board-2022-03-01/> 관측 2026-11-09.
[^award]: Kurt Research, Optica APC 2023 Best Student Paper. <https://kurtresearch.com/apc2023award/> 관측 2026-11-09.
[^aff]: H. Kocer 외, E. Ozbay, “Nano shell impact on Huygens’ metasurface dipolar resonances and optical response”, Journal of Optical Society of America B (2021). DOI: 10.1364/josab.424589. OpenAlex 등록 서지의 Hamza Kurt 저자 소속. <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5048311306,publication_year:2021-2026> 관측 2026-11-09.
[^p1]: S. Hong 외, H. Kurt, Advanced Optical Materials (2026). <https://doi.org/10.1002/adom.71567> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5048311306,publication_year:2021-2026> 관측 2026-11-09.
[^p2]: B. Neseli 외, H. Kurt, Laser & Photonics Review (2026). <https://doi.org/10.1002/lpor.71717> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5048311306,publication_year:2021-2026> 관측 2026-11-09.
[^p3]: B. Neseli 외, H. Kurt, ACS Photonics (2025). <https://doi.org/10.1021/acsphotonics.5c00026> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5048311306,publication_year:2021-2026> 관측 2026-11-09.
[^p4]: J. Kim 외, H. Kurt, Laser & Photonics Review (2024). <https://doi.org/10.1002/lpor.202300998> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5048311306,publication_year:2021-2026> 관측 2026-11-09.
[^p5]: J. Yoon 외, H.-H. Park, Optics Express (2023). <https://doi.org/10.1364/oe.481229> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5048311306,publication_year:2021-2026> 관측 2026-11-09.
[^p6]: J. Kim 외, H. Kurt, Nanophotonics (2022). <https://doi.org/10.1515/nanoph-2022-0443> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5048311306,publication_year:2021-2026> 관측 2026-11-09.
[^p7]: J.-H. Park 외, H. Kurt, Nanophotonics (2026). <https://doi.org/10.1002/nap2.70260> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5048311306,publication_year:2021-2026> 관측 2026-11-09.

# I³ Group (Intelligence, Imaging & Integration Group)

**KAIST 전기및전자공학부 · 강익성 교수**

- 분야: 계산 영상(Computational Imaging), 계산 현미경, 적응 광학과 현미경, 물리 기반 AI(Physics-Informed AI), 역문제, 광학·X선 계측과 검사, 3차원 계측
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 광학 영상·현미경[^research][^ee][^p1], X선 영상·회절[^research], 반도체 계측·검사[^research], 과학·공학 AI[^research][^ee], 3차원 복원·인식[^research][^home]
- 홈페이지: <http://kangimaging.com> (교수 개인 누리집 <https://iksungk.github.io>)
- 근거와 출처: [I³ Group 근거 페이지](iksungk-sources.md)

> 광학 장치와 측정 방식, 물리 법칙을 담은 인공지능을 함께 설계해 작은 대상의 3차원 구조를 부수지 않고 선명하게 보는 계산 현미경을 만드는 연구실이다. 빛과 X선을 써서 마이크로·나노 크기의 대상을 보며, 생물 영상과 계측·검사에 쓴다.[^home][^research]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 강익성 조교수가 2026년 1월에 연 연구 그룹이다.[^news][^ee] 누리집 이름은 I³ Group이고 머리에 Intelligence, Imaging, Integration 세 낱말을 내건다.[^home] 전기및전자공학부 교수 소개는 소속 연구실을 Intelligence, Imaging & Integration Group으로, 주요 연구를 Computational Imaging, Physics-Informed AI, Adaptive Optics & Microscopy, 3D Metrology로 적는다.[^ee] 반도체시스템공학과 연구실 목록에는 Intelligent Imaging Systems Lab이라는 이름으로 올라 있다.[^ssel]

누리집이 핵심 기술로 내세우는 것은 계산 현미경(computational microscopy, 측정한 신호를 계산으로 처리해 영상을 얻는 현미경)이다.[^research] 시료를 부수지 않고 고해상도 3차원 영상을 얻으려고 광학 장치·측정 방식·복원 계산을 함께 설계하고, 단층 촬영(tomography, 여러 방향에서 찍은 투과 영상으로 내부 단면을 계산해 내는 방법)·라미노그래피(laminography, 넓고 납작한 시료를 기울인 채 돌려 가며 찍어 3차원 구조를 얻는 단층 촬영)·타이코그래피(ptychography, 빛이나 X선을 시료의 여러 위치에 겹치게 비춰 얻은 회절 무늬들로 시료의 모양과 위상을 계산해 내는 영상법)·위상 변조로 기록한 측정값에서 구조를 되찾는다.[^research] 이 3차원 구조는 측정값에 바로 드러나지 않아 역문제(inverse problem, 관측된 결과에서 그 결과를 만든 원인을 거꾸로 추정하는 문제)로 추론해야 한다.[^research]

연구 페이지는 적은 광자 수, 좁은 촬영 각도·범위, 수차(렌즈나 시료 때문에 빛의 파면이 이상적인 모양에서 어그러지는 현상), 산란이 이 추론을 어렵게 만든다고 설명한다.[^research] 연구실은 영상이 만들어지는 물리 모형을 인공지능과 결합해 시료의 구조와 영상 조건을 함께 추정하고, 물리적으로 맞는 구조를 되찾으면서 추론 과정을 해석할 수 있고 모형을 설명할 수 있게 만드는 것을 목표로 한다.[^research] 다루는 대상은 마이크로·나노 크기이고, 형광 영상과 결맞음 영상(coherent imaging, 위상이 고른 빛이나 X선으로 세기와 함께 위상 정보를 얻는 영상법)을 다루고, 빛과 X선을 모두 쓴다.[^research][^home]

이 기술의 쓰임으로 연구 페이지는 두 갈래를 든다. 하나는 생물 영상을 위한 적응 광학 형광 현미경이고, 다른 하나는 계측·검사를 위한 계산 광학·X선 계측이다.[^research] 각 갈래의 대표 성과로 연구 페이지가 드는 논문은 2026년 Nature Methods 논문을 빼면 교수가 MIT 박사과정과 UC Berkeley 박사후연구원으로 있던 때(누리집 표기 Before KAIST)의 논문이다.[^research][^gpubs][^team]

KAIST에서 연구실을 연 뒤의 소식을 보면, 2026년 3월 KAIST PICORE(광학 인공지능) 센터의 구성원이 되어 InnoCORE 박사후연구원을 모집했고, 같은 달 한국연구재단 우수신진연구 지원을 받기 시작했다.[^news][^prof] 2026년 6월에는 전기및전자공학부와 BBE·BCS 학과(누리집 표기)에 걸친 기초연구실(BRL) 팀에 참여했다.[^news] 누리집 논문 목록이 KAIST 시기(At KAIST)로 분류한 논문은 2026년 4월 Nature Methods에 실린 NeAT 한 편이다(대표 논문 1).[^gpubs][^p1]

## 주요 연구 주제

### 1. 계산 현미경: 물리 모형과 인공지능으로 3차원 구조 복원

측정값에 담긴 시료의 3차원 구조를 물리 모형과 인공지능을 결합한 계산으로 되찾는다.[^research] 연구 페이지는 이 핵심 기술의 범위를 마이크로·나노 크기 영상, 결맞음 영상과 형광 영상, 광학과 X선 방식으로 적는다.[^research] 아래 두 갈래가 이 기술을 생물 영상과 계측·검사에 적용한 것이다.

### 2. 생물 영상: 적응 광학 형광 현미경

형광 현미경(시료 속 형광 물질이 내는 빛을 받아 영상을 만드는 현미경)에 적응 광학(adaptive optics, 빛이 지나오며 생긴 파면의 어그러짐을 재고 되돌려 선명한 영상을 얻는 기술)과 물리 기반 인공지능을 결합해 수차를 빠르고 정확하게 추정하고 바로잡는다.[^research] 시료의 구조와 파면 수차를 함께 추정해, 신호 대 잡음비가 낮거나 시료가 만드는 수차가 큰 조건에서도 영상을 개선하고 파면 측정 장치에 덜 기대게 하는 것이 목표다.[^research] 연구 페이지가 드는 세부 주제는 계산·물리 적응 광학, 뉴럴 필드 기반 수차 추정과 보정, 부피 현미경, 시료와 수차의 동시 추정, 물리 기반 복원이다.[^research] 대표 논문 1.

### 3. 계측·검사: 계산 광학·X선 위상 영상

시료를 부수지 않고 재고 검사하기 위한 광학·X선 위상 영상을 연구한다.[^research] 물리 기반 방법으로 광자가 적거나 촬영 각도가 제한된 조건에서도 2차원 위상과 고해상도 3차원 구조를 믿을 만하게 되찾는 것을 겨냥하며, 검사를 크게 빠르게 하려고 일부러 측정을 줄인 조건도 포함한다.[^research] 세부 주제는 계산 X선 단층 촬영과 타이코그래피, 희소 시점 3차원 복원, 광자가 적은 조건의 영상, 인공지능 보조 복원, 광학 영상에서 X선 영상으로의 변환이다.[^research] 연구 페이지는 이 갈래의 그림 설명을 반도체 계측을 위한 계산 X선 영상(Computational X-ray imaging for semiconductor metrology)으로 적는다.[^research]

## 대표 논문

강익성 교수가 KAIST에 부임한 2026년 1월 뒤 출판된 논문 가운데 누리집 논문 목록이 KAIST 시기(At KAIST)로 분류한 논문은 한 편이어서 이 논문만 실었다. 이 논문의 사전 공개본은 부임 전인 2024년 bioRxiv에 올라왔다.[^gpubs][^ppubs] "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^gpubs] |
|---|---|---|---|---|
| 1 | 2026 | [Adaptive optical correction for in vivo two-photon fluorescence microscopy with neural fields](https://doi.org/10.1038/s41592-026-03053-6) · Nature Methods | 적응 광학은 복잡한 시료에서 광학 수차를 재고 바로잡아 이상적인 영상 성능을 되찾지만, 정밀하게 맞춘 파면 측정·조정 장치를 갖춘 맞춤 제작 현미경이 필요할 때가 많고 시료의 움직임에 약할 수 있다. NeAT는 뉴럴 필드를 써서 이광자 형광 현미경(형광 물질이 광자 두 개를 함께 흡수할 때만 빛을 내게 하는 형광 현미경)의 적응 광학을 계산으로 하는 틀이다. 외부 학습 데이터 없이 3차원 영상 묶음 하나에서 파면 수차를 추정하고 시료 구조를 되찾는다. 학습에 움직임 보정을 넣고 상용 현미경에서 흔한 공액 오차(파면 보정 장치와 현미경 광학계에서 짝이 되어야 할 면이 어긋나 생기는 오차)를 바로잡아, 생물학 실험실에서 살아 있는 생물을 찍는 데 쓰도록 설계했다. 파면 측정기를 단 맞춤 현미경으로 여러 신호 대 잡음비·수차·움직임 조건에서 성능을 확인했고, 상용 현미경으로 살아 있는 생쥐 뇌의 형태·기능 영상에서 수차를 실시간으로 바로잡아 시냅스와 뉴런의 글루타메이트·칼슘 영상의 신호와 정확도를 높였다.[^p1] | 1저자·공동 교신저자 강익성, 마지막 저자·공동 교신저자 Na Ji |

## 교수와 전문 분야

강익성 교수(Iksung Kang)는 KAIST 전기및전자공학부 조교수이고 디비전은 Signal이다.[^ee] 전기및전자공학부 교수 소개는 주요 연구분야를 AI & Machine Learning, Multimedia Signal Processing, Biomedical Engineering, Photonics로 적고,[^ee] 반도체시스템공학과 교수진 목록은 연구분야를 '컴퓨터, 인공지능 및 소프트웨어'로, 관심 분야를 Computational Imaging, Intelligent Optical Systems, Adaptive Optics, Machine Learning으로 적는다.[^ssep] 교수는 물리 원리와 계산, 시스템 수준 설계를 매끄럽게 묶은 지능형 영상 시스템을 만들어 첨단 영상 기술을 더 쉽게 쓰고, 규모를 키우고, 믿을 수 있게 하는 데 집중한다고 소개한다.[^prof]

서울대학교 ECE에서 학사(2017)를, 미국 MIT EECS(전기공학·컴퓨터과학)에서 석사(2020)와 박사(2022)를 받았다.[^team][^ee] MIT에서는 George Barbastathis 교수의 지도를 받았고, 박사과정 내내 Korea Foundation for Advanced Studies(한국고등교육재단) 장학금을 받았다.[^prof] 박사 뒤 UC Berkeley에서 Na Ji 교수와 Stella X. Yu 교수의 지도로 박사후연구원(2022–2025)을 지냈고, 2026년 1월 KAIST 전기및전자공학부의 정년 트랙(tenure-track) 조교수로 부임했다.[^team][^prof][^news]

논문으로 보면 전문 분야는 두 줄기다. 지도교수 Barbastathis와 함께 쓴 2021–2023년 논문은 산란 매질 너머의 투명한 물체를 보는 순환 신경망, 제한된 각도에서 찍은 영상으로 물체 내부를 3차원으로 복원하는 기계학습, X선 타이코그래피와 단층 촬영을 결합한 3차원 나노 영상, 집적회로를 3차원 나노 영상으로 보는 자기 지도 학습 타이코-라미노그래피, CMOS 마이크로 LED 홀로그래피(빛의 간섭 무늬를 기록해 대상의 3차원 정보를 담는 영상 기술)를 다룬다.[^gpubs] Na Ji와 함께 쓴 2024–2026년 논문과 사전 공개 논문은 광시야 현미경의 계산 적응 광학(Nature Machine Intelligence, 2024), 이광자 형광 현미경의 적응 광학(대표 논문 1), 넓은 시야에서 수차를 한꺼번에 재는 방법을 다룬다.[^gpubs] 전기및전자공학부 교수 소개는 대표업적으로 2021–2026년 논문 6편을 든다.[^ee]

## 응용 분야

연구 페이지가 드는 쓰임은 두 가지다. 생물 영상(Bio-imaging)에서는 형광 현미경에 적응 광학과 물리 기반 인공지능을 결합해 신호가 약하거나 시료가 만드는 수차가 큰 조건에서도 영상을 개선한다.[^research] 계측·검사(Metrology & Inspection)에서는 광학·X선 위상 영상으로 시료를 부수지 않고 재며, 일부러 측정을 줄여 검사를 크게 빠르게 하는 조건까지 겨냥한다.[^research] 누리집 첫 화면은 연구가 생물학과 계측을 위한 것이라고 적는다.[^home]

대표 논문 1은 상용 이광자 현미경으로 살아 있는 생쥐 뇌에서 수차를 실시간으로 바로잡아, 이 방법을 맞춤 현미경이나 상용 현미경에 쉽게 넣을 수 있게 했다고 밝힌다.[^p1] 교수 누리집에는 이 논문과 제목이 거의 같은 미국 특허 출원(발명자 Kang I, Ji N, 2025년 10월 15일 출원)이 올라 있다.[^ppubs]

## 구성원

누리집 Team 페이지의 석사과정(MS Students) 1명, 연구원(Research Associates) 1명, 학부 연구생(Undergraduate Interns) 4명이다. 과정 칸 괄호 안의 M2·U1–U3과 학과 표기(KAIST EE·KAIST SSE), 연구 주제는 페이지 표기 그대로다.[^team] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Bonha Woo | 석사과정 (M2) | Computational Microscopy ／ Adaptive Optics |  |  |
| Yunkyu Lee | 연구원 | Computational Microscopy ／ Adaptive Optics |  |  |
| Hyeonbin Jo | 학부 연구생 (U3, KAIST EE) | Computational Metrology ／ Holography | johyeonbin01@kaist.ac.kr |  |
| Hoseung Bin | 학부 연구생 (U3, KAIST EE) | Computational Microscopy ／ Adaptive Optics | hoseungbin@kaist.ac.kr |  |
| Donghyuk Lee | 학부 연구생 (U2, KAIST EE) | Computational Microscopy ／ Adaptive Optics | dhlee4832@kaist.ac.kr |  |
| Seungjun Ahn | 학부 연구생 (U1, KAIST SSE) | Computational Metrology ／ Holography | yoninf@kaist.ac.kr |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지의 2021–2026년 논문 11편(학술지 9편, 심사 중(Under review)으로 적힌 bioRxiv 사전 공개 논문 2편)과 교수 누리집 Publications 페이지 Conference Proceedings & Presentations 절의 2021–2024년 학회 발표 8건이다. 누리집이 KAIST 시기(At KAIST)로 분류한 논문은 2026년 Nature Methods 논문 한 편이고, 나머지는 교수가 MIT와 UC Berkeley에 있던 때(누리집 표기 Before KAIST)의 논문·발표라 현재 KAIST 연구실의 성과로 묶지 않는다. 학술지 논문 뒤의 날짜는 누리집이 적은 날짜이고, 저자 이름 뒤 †는 공동 교신저자, *는 공동 1저자 표시다. 학회 발표의 *는 교수 누리집 표기로 발표자(구두 발표)를 뜻한다.[^gpubs][^ppubs]

**2026**

- Kang I†, Kim H, Natan R, Zhang Q, Yu SX, Ji N†. "Adaptive optical correction for in vivo two-photon fluorescence microscopy with neural fields". *Nature Methods, 13 Apr 2026*.
- Zhu J, Natan R, Zhong J, Kang I, Ji N. "In vivo aberration measurement and correction for ultrafast FACED two-photon fluorescence microscopy of the brain". *bioRxiv, Under review*.

**2025**

- Kim H, Kang I, Natan R, Ji N. "Parallel frequency-multiplexed aberration measurement for widefield fluorescence microscopy". *bioRxiv, Under review*.
- Kim S, Yoon J, Ko G, Kang I, Tian H, Fan LZ, Li Y, Cohen AE, Wu J, Dai Q, Choi MM. "Optical segmentation-based compressed readout of neuronal voltage dynamics". *Nature Communications, 05 August 2025*.

**2024**

- Kang I†, Zhang Q†, Yu SX, Ji N. "Coordinate-based neural representations for computational adaptive optics in widefield microscopy". *Nature Machine Intelligence (2024) 6, 714-725*.
- Kang I\*, Zhang Q, Yaeger C, Pham T, Yu SX, Harnett M, Ji N. "Coordinate-based neural representations for computational adaptive optics in two-photon microscopy". *SPIE Photonics West (2024) 12851-9 (28 January 2024). https://doi.org/10.1117/12.3008468 \*Speaker, oral presentation*.

**2023**

- Kang I, Jiang Y, Holler M, Guizar-Sicairos M, Levi AFJ, Klug J, Vogt S, Barbastathis G. "Accelerated deep self-supervised ptycho-laminography for three-dimensional nanoscale imaging of integrated circuits". *Optica, 26 July 2023*.
- Kang I\*, Wu Z\*, Jiang Y, Yao Y, Deng J, Klug J, Vogt S, Barbastathis G. "Attentional Ptycho-Tomography (APT) for three-dimensional nanoscale X-ray imaging with minimal data acquisition and computation time". *Light Science and Applications, 30 May 2023*.
- Wu Z\*, Kang I\*, Yao Y, Jiang Y, Deng J, Klug J, Vogt S, Barbastathis G. "Three-dimensional nanoscale reduced-angle ptycho-tomographic imaging with deep learning (RAPID)". *eLight, 03 April 2023*.
- Barbastathis G, Pang S, Kang I\*, Wu Z, Liu Z, Guo Z, Zhang F. "On the use of deep learning for three-dimensional computational imaging". *SPIE Photonics West (2023) 124450J (8 March 2023). https://doi.org/10.1117/12.2655261 \*Speaker, oral presentation*.
- Kang I\*, Zhang Q, Ji N. "Deep self-supervised learning for computational adaptive optics in widefield microscopy". *SPIE Photonics West (2023) 123880H (16 March 2023). https://doi.org/10.1117/12.2658934 \*Speaker, oral presentation*.

**2022**

- Kang I\*, de Cea M\*, Xue J, Li Z, Barbastathis G, Ram R. "Simultaneous spectral recovery and CMOS micro-LED holography with an untrained deep neural network". *Optica, 11 October 2022*.
- Kim S, Wu J, Kang I, Ko G, Tian H, Fan LZ, Li Y, Cohen AE, Dai Q, Choi MM. "Optical segmentation for compressed readout on sub-millisecond neuronal circuit dynamics – Diffractive Multisite Optical Segmentation Assisted Image Compression: DeMOSAIC". *Frontiers in Neurophotonics (FiNs) (2022)*.
- Wu Z, Kang I, Zhou T, Coykendall V, Ge B, Cherukara MJ, Barbastathis G. "Photon-starved X-ray Ptychographic Imaging using Spatial Pyramid Atrous Convolution End-to-end Reconstruction (PtychoSPACER)". *Computational Optical Sensing and Imaging (COSI) (2022) CF1D.6. https://doi.org/10.1364/COSI.2022.CF1D.6*.
- Kim S, Wu J, Kang I, Li Y, Tian H, Fan LZ, Cohen AE, Dai Q, Choi MM. "Adaptive image segmentation for crosstalk-free high-speed compressive imaging". *Focus on Microscopy (FOM) (2022)*.

**2021**

- Kang I, Goy A, Barbastathis G. "Dynamical machine learning volumetric reconstruction of objects’ interiors from limited angular views". *Light Science and Applications, 07 April 2021*.
- Kang I, Pang S, Zhang Q, Fang N, Barbastathis G. "Recurrent neural network reveals transparent objects through scattering media". *Optics Express, 04 February 2021*.
- Kang I\*, Yao Y, Deng J, Klug J, Vogt S, Honig S, Barbastathis G. "Three-dimensional reconstruction of integrated circuits by single-angle X-ray ptychography with machine learning". *Computational Optical Sensing and Imaging (COSI) (2021) CTu6A.4. https://doi.org/10.1364/COSI.2021.CTu6A.4 \*Speaker, oral presentation*.
- Kang I\*, Barbastathis G. "Probability of error as an image metric for the assessment of tomographic reconstruction of dense-layered binary-phase objects". *SPIE Photonics West (2021) 116530T (5 March 2021). https://doi.org/10.1117/12.2577264 \*Speaker, oral presentation*.

## 특허

교수 누리집 Publications 페이지 Patents 절의 1건이다. KAIST 부임 전인 2025년 10월에 출원한 미국 특허 출원이다.[^ppubs]

- Adaptive optical correction in two-photon fluorescence microscopy with neural fields (발명자 Kang I, Ji N; 번호 U.S. Patent Application No. 19/358,888; 출원일 October 15, 2025)

## 소식

누리집 News 페이지의 글 5건(2026년)과 교수 누리집 첫 화면 소식 가운데 2025년 글 3건이다. 문구는 누리집 표기 그대로이고, 2025년 글은 교수가 KAIST에 부임하기 전의 소식이다.[^news][^prof] 2025년 6월 24일 글이 알린 Nature Machine Intelligence 논문은 2024년 6월 24일에 온라인으로 출판됐다.[^nmi]

- 2026-06-17 · Grant · We Are Now a Member of BRL (기초연구실). I³ have joined a Basic Research Laboratory (BRL) team spanning the School of EE and the Departments of BBE and BCS.
- 2026-04-13 · Publication · NeAT Published in Nature Methods. Our work on Neural fields for Adaptive optical Two-photon microscopy (NeAT) is now available in Nature Methods!
- 2026-03-27 · Grant · I³ Receive NRF Outstanding Early-Career Researcher Grant (우수신진연구). We are now receiving an outstanding early-career researcher grant from National Research Foundtion (NRF)!
- 2026-03-22 · Recruiting · We Are Now a Member of the PICORE Center. We are actively recruiting driven, curious, and collegial postdoctoral researchers for the InnoCORE program.
- 2026-01-23 · Beginning · Our Group Launches at KAIST EE. Starting Jan 26, 2026 at KAIST EE, building intelligent physics- and learning-driven computational imaging systems.
- 2025-10-20 · We present NeAT for adaptive optical correction in in vivo two-photon microscopy using neural fields, now available in bioRxiv.
- 2025-10-11 · Our study for parallel aberration measurement in a large field-of-view is now available in bioRxiv.
- 2025-06-24 · We present CoCoA for aberration and structural estimation in in vivo widefield fluorescence microscopy using coordinate-based neural representations, published in Nature Machine Intelligence!

## 연락과 위치

- 주소: LG Innovation Hall (N24), 291 Daehak-ro, Yuseong-gu, Daejeon, Republic of Korea (34141)[^home]
- 교수 연구실: LG이노베이션홀(N24) 3113호[^ee]
- 연락처(교내 번호): 7483[^ee]
- 교수 이메일: iksung.kang@kaist.ac.kr[^ee]
[^p1]: I. Kang 외, N. Ji, Nature Methods 23, 1037-1046 (온라인 2026-04-13). <https://doi.org/10.1038/s41592-026-03053-6> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 연구실 누리집 첫 화면 <http://kangimaging.com/> (소개문, 연구 낱말, 주소, 2026-10-22 열람)
[^research]: 연구실 누리집 Research 페이지 <http://kangimaging.com/research/> (핵심 기술과 두 응용 갈래, 세부 주제, 2026-10-22 열람)
[^team]: 연구실 누리집 Team 페이지 <http://kangimaging.com/team/> (교수 경력·학력, 구성원, 2026-10-22 열람)
[^gpubs]: 연구실 누리집 Publications 페이지 <http://kangimaging.com/publications/> (At KAIST·Before KAIST 논문 목록, 2026-10-22 열람)
[^news]: 연구실 누리집 News 페이지 <http://kangimaging.com/news/> (2026년 글 5건, 2026-10-22 열람)
[^prof]: 강익성 교수 개인 누리집 첫 화면 <https://iksungk.github.io/> (소개문, 소식, 대표 논문, 2026-10-22 열람)
[^ppubs]: 강익성 교수 개인 누리집 Publications 페이지 <https://iksungk.github.io/publications.html> (사전 공개 논문, 학술지, 학회 발표, 특허, 2026-10-22 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(강익성) <https://ee.kaist.ac.kr/professor/%ea%b0%95%ec%9d%b5%ec%84%b1/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 디비전, 학위, 대표업적, 2026-10-22 열람)
[^ssel]: KAIST 반도체시스템공학과 연구실 목록 <https://sse.kaist.ac.kr/research-laboratory/> (2026-10-22 열람)
[^ssep]: KAIST 반도체시스템공학과 교수진 <https://sse.kaist.ac.kr/professor/> (2026-10-22 열람)
[^nmi]: Nature Machine Intelligence 6권 6호 714-725쪽 출판사 등록 서지(Crossref) <https://doi.org/10.1038/s42256-024-00853-3> (온라인 출판 2024-06-24, 2026-10-22 조회)

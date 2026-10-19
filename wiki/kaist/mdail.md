# 다차원 원자 영상 연구실 (Multi-Dimensional Atomic Imaging Laboratory, MDAIL)

**KAIST 물리학과 · 양용수 교수**

- 분야: 원자 분해능 전자 토모그래피(AET), 표면 X선 회절, 나노 촉매·강유전체의 3차원 원자 구조, 인공지능 기반 영상 복원, 저선량 전자현미경과 극저온 전자현미경 영상
- 홈페이지: <https://mdail.kaist.ac.kr>
- 근거와 출처: [MDAIL 근거 페이지](mdail-sources.md)

> 전자현미경으로 물질을 여러 각도에서 찍어 원자 하나하나의 3차원 위치를 알아내는 연구실이다. 병원 CT처럼 단층 사진을 모아 3차원으로 재구성하는 방법을 원자 크기까지 끌어내려, 연료전지 촉매나 나노 크기 강유전체 속 원자 배열이 어떻게 생겼고 시간에 따라 어떻게 바뀌는지 본다.[^physics][^news-vortex]

## 무엇을 연구하나

물리학과 교수 소개에 실린 연구실 소개는 X선·전자 영상 기술과 계산 능력, 알고리즘이 발전해 이제 물질 속 개별 원자를 실제로 "볼" 수 있게 됐다고 설명한다. 연구실은 원자 분해능 전자 토모그래피(AET)와 결정 절단 막대(CTR) 기반 표면 X선 회절(SXRD)을 써서, 원자 구조를 3차원으로 볼 뿐 아니라 시간·온도 같은 추가 차원까지 다룬다.[^physics]

연구실은 물질 성질이 원자들의 3차원 배열에 크게 좌우되는데, 오랫동안 쓰인 결정학은 완벽한 결정을 가정하지만 실제 물질에는 결함, 결정립 경계(결정 알갱이 사이의 경계), 쌓임 결함(원자층이 쌓이는 순서가 어긋난 곳), 전위(원자 배열이 선을 따라 어긋난 결함) 같은 흐트러진 구조가 많다고 짚는다. 수차 보정 전자현미경(렌즈 왜곡을 바로잡은 고분해능 현미경)과 재구성 알고리즘으로 이런 결정학적 가정 없이 3차원 원자 구조와 그 변화를 밝히는 것이 목표다. 핵생성(새 결정이 처음 생기는 과정)과 상전이의 원자 수준 동역학, 비정질 물질의 구조, 고엔트로피 합금(여러 원소를 비슷한 비율로 섞은 합금), 자철석의 버웨이 전이(특정 온도에서 전기 전도성이 급변하는 현상) 같은 응집물질물리·재료과학의 미해결 문제를 겨냥한다.[^physics]

첫 번째 갈래는 **나노 촉매의 3차원 원자 구조와 변형**이다. 백금 나노입자 표면 원자 구조를 15 pm(피코미터) 정밀도로 측정했고,[^p3] 팔라듐–백금 코어–셸 나노입자에서 표면과 경계면의 변형(원자 간격이 늘거나 줄어든 정도)이 직접 연결됨을 보였다.[^p4] 연료전지에서 수천 번 쓰는 동안 백금–니켈 합금 촉매의 모양, 표면 성분, 변형이 어떻게 바뀌는지 원자 수준에서 추적했다.[^p2]

두 번째 갈래는 **강유전체·기능성 물질의 원자 구조**다. 외부 전기장 없이도 전기적 분극을 유지하는 강유전체를 나노 크기로 만들면 내부에 소용돌이 모양 분극이 생긴다는 20년 전 이론 예측을, 바륨–티타늄 산화물 나노입자에서 처음 실험으로 확인했다.[^p1][^news-vortex]

세 번째 갈래는 **새 영상 기법 개발**이다. 4차원 주사투과전자현미경(4D-STEM) 데이터로 적은 전자량에서도 가벼운 원소까지 정확히 재구성하는 다중 슬라이스 전자 토모그래피를 만들었고,[^p5] 물리 시뮬레이션으로 만든 학습 데이터로 극저온 전자 토모그래피 영상의 잡음을 줄이는 인공지능을 개발했다.[^p8]

## 주요 연구 주제

### 1. 나노 촉매의 3차원 원자 구조·변형·열화

신경망 보조 전자 토모그래피, 코어–셸 변형, 연료전지 촉매 열화.[^p2][^p3][^p4][^p6][^p7] 대표 논문 2, 3, 4, 6, 7.

### 2. 강유전체 나노입자의 위상학적 분극 구조

3차원 분극 지도, 크기에 따른 소용돌이 전이.[^p1] 대표 논문 1.

### 3. 저선량·다차원 전자현미경 영상 기법

다중 슬라이스 토모그래피, 극저온 영상 잡음 제거.[^p5][^p8] 대표 논문 5, 8.

## 대표 논문

물리학과 연구 소식 게시판의 연구실 논문 소개와 양용수 교수가 저자로 참여한 2021–2026년 논문 가운데 주제별로 골랐다. 6은 공동 연구 논문이다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^crossref] |
|---|---|---|---|---|
| 1 | 2024 | [Revealing the three-dimensional arrangement of polar topology in nanoparticles](https://doi.org/10.1038/s41467-024-48082-x) · Nature Communications | 2000년대 초 이론이 예측한 나노 강유전체 속 소용돌이 모양 분극 구조를, 원자 분해능 전자 토모그래피로 바륨–티타늄 산화물(BaTiO3) 나노입자의 원자 배열을 3차원으로 재구성해 찾아냈다. 입자 크기에 따라 소용돌이 하나에서 여러 개로 바뀌는 전이도 보였다.[^p1] | 1저자 Chaehwa Jeong, 마지막 저자 양용수 |
| 2 | 2025 | [Atomic-scale 3D structural dynamics and functional degradation of Pt alloy nanocatalysts during the oxygen reduction reaction](https://doi.org/10.1038/s41467-025-63448-5) · Nature Communications | 연료전지용 백금–니켈 합금 촉매가 반복 사용 중 모양 변화, 표면 합금화, 변형 완화를 겪는다는 것을 신경망 보조 전자 토모그래피로 원자 수준에서 쟀다. 갈륨을 넣으면 이런 변화가 줄어 초기 활성과 안정성이 모두 높아졌다.[^p2] | 1저자 Chaehwa Jeong, 마지막 저자 양용수 |
| 3 | 2021 | [Single-atom level determination of 3-dimensional surface atomic structure via neural network-assisted atomic electron tomography](https://doi.org/10.1038/s41467-021-22204-1) · Nature Communications | 딥러닝으로 빠진 측정 데이터를 채운 원자 전자 토모그래피로 백금 나노입자의 3차원 표면 원자 구조를 15 pm 정밀도로 쟀다. 결정면 종류에 따라 표면 변형이 다르게 나타났다.[^p3] | 1저자 Juhyeok Lee, 마지막 저자 양용수 |
| 4 | 2022 | [Direct strain correlations at the single-atom level in three-dimensional core-shell interface structures](https://doi.org/10.1038/s41467-022-33236-6) · Nature Communications | 팔라듐 핵을 백금 껍질이 감싼 코어–셸 나노입자의 3차원 원자 구조를 원자 하나 단위로 재구성해, 표면 변형과 경계면 변형이 직접 연결됨을 보였다. 관찰한 표면 변형으로 촉매 활성을 예측했다.[^p4] | 1저자 Hyesung Jo, 마지막 저자 양용수 |
| 5 | 2023 | [Multislice Electron Tomography Using Four-Dimensional Scanning Transmission Electron Microscopy](https://doi.org/10.1103/physrevapplied.19.054062) · Physical Review Applied | 기존 원자 분해능 토모그래피는 전자량이 많이 필요하고 가벼운 원소가 잘 안 보이는 한계가 있다. 4D-STEM 기울기 영상으로 재구성하는 다중 슬라이스 전자 토모그래피(MSET)를 만들어, 시뮬레이션에서 낮은 전자량으로도 가벼운 원소까지 정확히 재구성할 수 있음을 보였다.[^p5] | 1저자 Juhyeok Lee, 마지막 저자 양용수 |
| 6 | 2025 | [Suppressing Metal Dissolution in Multi-Grained Catalysts Through Intragrain Atomic Ordering for Stable Fuel Cells](https://doi.org/10.1002/adma.202504059) · Advanced Materials | 결정립 안에 원자가 규칙적으로 배열된 Ni3Pt5 상을 품은 니켈–백금 연료전지 촉매를 초음파 합성으로 만들었다. 니켈이 덜 녹아 나왔고, 대형 차량 조건에서도 미국 에너지부 내구성 목표를 넘었다.[^p6] | 1저자 Eungjun Lee, 양용수 공저(21명 중 열아홉째), 마지막 저자 Sung Jong Yoo |
| 7 | 2022 | [Direct Observation of Three-Dimensional Atomic Structure of Twinned Metallic Nanoparticles and Their Catalytic Properties](https://doi.org/10.1021/acs.nanolett.1c03773) · Nano Letters | 두 나노 클러스터가 합쳐져 생긴 아령 모양 백금 나노입자의 3차원 원자 구조를 재구성해, 경계면의 이중 쌍정(거울처럼 대칭인 결정 경계)과 내부 무질서를 관찰했다. 튀어나온 부분의 강한 인장 변형이 촉매 활성을 높였다.[^p7] | 1저자 Juhyeok Lee, 마지막 저자 양용수 |
| 8 | 2026 | [Supervised cryo-EM tomography denoising enabled by physics-based image simulation](https://doi.org/10.1063/5.0313245) · Applied Physics Letters | 극저온 전자 토모그래피는 전자량 제한 때문에 잡음이 크다. 실제 장비 조건을 반영한 물리 시뮬레이션으로 깨끗한 영상과 잡음 영상 쌍을 만들어 인공지능(U-Net)을 학습시켰고, 리포솜(지질막으로 된 작은 주머니) 영상의 신호 대 잡음비(잡음에 비해 신호가 얼마나 또렷한지)를 최대 132% 높였다.[^p8] | 1저자 Yeaeun Kim, 마지막 저자 양용수 |

## 교수와 전문 분야

양용수 교수는 서울대 물리학 학사(2003–2009)와 미국 미시간대 물리학 박사(2009–2014)를 받았다. 미국 UCLA 물리천문학과 박사후연구원(2014–2018)을 거쳐 2018년 KAIST 물리학과 조교수로 부임했고 지금은 부교수다.[^physics][^news-hire] 물리학과는 연구 분야를 실험 응집물질물리, 다차원 전자현미경, 구조 상전이, 기능성 경계면으로 적고,[^physics] 전기및전자공학부는 겸임교수로서의 연구를 2차원 이종 구조와 기능성 경계면의 원자 전자 토모그래피로 적는다.[^ee]

교수는 2차원에 머물던 투과전자현미경 기술을 3차원으로 넓혀 물질 속을 원자 하나 단위로 보는 기술을 개발한 공로로 2023년 제56회 과학의 날 과학기술정보통신부 장관 표창을 받았다.[^news-award] 2025년 KAIST 개교 54년 특별 포상에서 우수 강의대상을 받았다.[^news-54]

논문으로 보면 전문 분야는 세 갈래다.

- **원자 분해능 전자 토모그래피와 인공지능 재구성**.[^p3][^p5][^p8]
- **촉매 나노입자의 3차원 구조·변형·열화**.[^p2][^p4][^p7]
- **강유전체의 위상학적 분극 구조**.[^p1]

## 응용 분야

대표 논문으로 보면 연료전지 촉매 설계, 초고밀도 메모리 소자, 생체 분자 영상에 닿아 있다.[^p2][^p6][^p8][^news-vortex] 물리학과 소식은 강유전체 소용돌이 연구가 같은 크기 소자에 약 1만 배 많은 정보를 저장하는 메모리 기술로 이어질 수 있다는 교수의 기대를 전한다.[^news-vortex] 연구실 학생 이주혁(2023, 동상)과 정채화(2024, 은상)는 삼성휴먼테크논문대상 기초과학 부문에서 상을 받았다.[^news-humantech]

## 최근 논문 목록 (2021–2026)

물리학과 연구 소식 게시판이 소개한 연구실 논문과 양용수 교수가 저자로 참여한 2021–2026년 학술지 논문 19편이다. 게시판에만 있는 두 편은 저자를 게시판 표기로 적었다.[^research-board][^crossref]

**2026**

- Yeaeun Kim, Yongsoo Yang. "Supervised cryo-EM tomography denoising enabled by physics-based image simulation". *Applied Physics Letters, 128, 203701*.
- Minwoo Jang, Hyunkyu Lim, Sanghoon Yeom, Jaewhan Oh, Yongsoo Yang, Hyungwoo Lee. "Flexoelectric Suppression of Interfacial Carrier Loss in BaTiO3 Thin‐Film Bulk Photovoltaic Systems". *Advanced Science*.
- Yakun Yuan, Saman Moniri, Yao Yang, Jihan Zhou, Andrew Yuan, Dennis S. Kim, Yongsoo Yang, Chenyang Li, Kun Luo, Qi An, Wei Chen, Peter Ercius, Jianwei Miao. "Crystal nucleation and growth in high-entropy alloys revealed by atomic electron tomography". *Nature Materials*.
- 물리학과 연구 소식 표기: 홍석조, 오재환, 박제민, 김용관, 양희준, 이성빈, 양용수 연구팀. "Spatial Correlations of Charge Density Wave Order across the Transition in 2H-NbSe2". *Physical Review Letters (2026.01)*.

**2025**

- Woohyun Cho, Jaehun Cha, Yoon-Gu Kang, Dong Hyun David Lee, Jaewhan Oh, Dohyun Kim, Sangsu Yer, Jaein Lee, Heemyoung Hong, Yongsoo Yang, Yeongkwan Kim, Myung Joon Han, Heejun Yang. "Polymorphic Spin Ordering in a Single-Crystalline Cobalt-Doped Fe3GaTe2". *ACS Nano, 19, 41033-41043*.
- Chaehwa Jeong, Juhyeok Lee, Hyesung Jo, KwangHo Lee, SangJae Lee, Colin Ophus, Peter Ercius, EunAe Cho, Yongsoo Yang. "Atomic-scale 3D structural dynamics and functional degradation of Pt alloy nanocatalysts during the oxygen reduction reaction". *Nature Communications, 16, 8026*.
- Eungjun Lee, Haneul Jin, Hyesung Jo, Myeong‐Geun Kim, Jae Hyun Park, Jieun Baik, Jong Seok Park, Jue‐Hyuk Jang, Seung‐Hoon Kim, Dong Wook Lee, Jihyun Choi, Jong Kyeong Ryu, Daeil Choi, Juyoung Kim, Sang Moon Kim, Yung‐Eun Sung, Kug‐Seung Lee, Docheon Ahn, Yongsoo Yang, Dong Won Chun, Sung Jong Yoo. "Suppressing Metal Dissolution in Multi‐Grained Catalysts Through Intragrain Atomic Ordering for Stable Fuel Cells". *Advanced Materials, 37, 2504059*.
- Juhyeok Lee, Yongsoo Yang. "Advancing atomic electron tomography with neural networks". *Applied Microscopy, 55, 7*.
- Yeaeun Kim, Changin Kim, Yongsoo Yang, Hyotcherl Ihee. "Exploiting Anisotropic Orientation in Nanoparticle-Aided Cryo-Electron Microscopy Sampling". *Methods*.

**2024**

- Chaehwa Jeong, Juhyeok Lee, Hyesung Jo, Jaewhan Oh, Hionsuck Baik, Kyoung-June Go, Junwoo Son, Si-Young Choi, Sergey Prosandeev, Laurent Bellaiche, Yongsoo Yang. "Revealing the three-dimensional arrangement of polar topology in nanoparticles". *Nature Communications, 15, 3887*.
- Jiwon Park, Chaehwa Jeong, Moony Na, Yusik Oh, Kug-Seung Lee, Yongsoo Yang, Hye Ryung Byon. "Subnanometer Cu Clusters on Porous Ag Enhancing Ethanol Production in Electrochemical CO2 Reduction". *ACS Catalysis, 14, 3198-3207*.
- Sanghyeok Ryou, Sanghyeon Mo, Doyeop Kim, Sungjun Choi, Jaewhan Oh, Yongsoo Yang, Kitae Eom, Hyungwoo Lee. "Atomic-Scale Interface Modification in Complex Oxide Heterojunctions for Near-Infrared Photodetection". *ACS Nano, 18, 34606-34614*.

**2023**

- Changin Kim, Yeaeun Kim, Sang Jin Lee, So Ri Yun, Jungkweon Choi, Seong Ok Kim, Yongsoo Yang, Hyotcherl Ihee. "Visualizing Heterogeneous Protein Conformations with Multi-Tilt Nanoparticle-Aided Cryo-Electron Microscopy Sampling". *Nano Letters, 23, 3334-3343*.
- Juhyeok Lee, Moosung Lee, YongKeun Park, Colin Ophus, Yongsoo Yang. "Multislice Electron Tomography Using Four-Dimensional Scanning Transmission Electron Microscopy". *Physical Review Applied, 19, 054062*.

**2022**

- Ji Soo Lim, Ho-Hyun Nahm, Marco Campanini, Jounghee Lee, Yong-Jin Kim, Heung-Sik Park, Jeonghun Suh, Jun Jung, Yongsoo Yang, Tae Yeong Koo, Marta D. Rossell, Yong-Hyun Kim, Chan-Ho Yang. "Critical ionic transport across an oxygen-vacancy ordering transition". *Nature Communications, 13, 5130*.
- Hyesung Jo, Dae Han Wi, Taegu Lee, Yongmin Kwon, Chaehwa Jeong, Juhyeok Lee, Hionsuck Baik, Alexander J. Pattison, Wolfgang Theis, Colin Ophus, Peter Ercius, Yea-Lee Lee, Seunghwa Ryu, Sang Woo Han, Yongsoo Yang. "Direct strain correlations at the single-atom level in three-dimensional core-shell interface structures". *Nature Communications, 13, 5957*.
- Juhyeok Lee, Chaehwa Jeong, Taegu Lee, Seunghwa Ryu, Yongsoo Yang. "Direct Observation of Three-Dimensional Atomic Structure of Twinned Metallic Nanoparticles and Their Catalytic Properties". *Nano Letters, 22, 665-672*.
- 물리학과 연구 소식 표기: 양용수 교수 연구팀. "Metastable hexagonal close-packed palladium hydride in liquid cell TEM". *Nature (2022)*.

**2021**

- Juhyeok Lee, Chaehwa Jeong, Yongsoo Yang. "Single-atom level determination of 3-dimensional surface atomic structure via neural network-assisted atomic electron tomography". *Nature Communications, 12, 1962*.

## 연락과 위치

- 교수 이메일: yongsoo.yang@kaist.ac.kr[^physics]
- 교수 전화: 042-350-7303[^physics]
- 위치: KAIST 자연과학동(E6-2) 3302호 (대전 유성구 대학로 291)[^physics][^ee]

[^physics]: KAIST 물리학과 교수 소개(양용수) <https://physics.kaist.ac.kr/index.php?document_srl=9292&mid=p_people1> (2026-10-19 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(양용수) <https://ee.kaist.ac.kr/professor/%ec%96%91%ec%9a%a9%ec%88%98/> (2026-10-19 열람)
[^crossref]: Crossref 저자 검색(Yongsoo Yang, 2021년 이후)과 논문별 서지 <https://api.crossref.org/works?query.author=Yongsoo+Yang> (2026-10-20 조회)
[^research-board]: KAIST 물리학과 연구 소식 게시판(양용수 검색) <https://physics.kaist.ac.kr/index.php?mid=p_research2&search_target=title_content&search_keyword=%EC%96%91%EC%9A%A9%EC%88%98> (2026-10-20 열람)
[^news-vortex]: KAIST 물리학과 소식 「강유전체 ‘3차원 소용돌이’ 20년 난제 풀어」(2024-06-21) <https://physics.kaist.ac.kr/index.php?mid=p_news_event2&document_srl=16929> (2026-10-20 열람)
[^news-hire]: KAIST 물리학과 소식 「[신임교원] 양용수 교수 부임」(2018-10-08) <https://physics.kaist.ac.kr/index.php?mid=p_news_event2&search_target=title_content&search_keyword=%EC%96%91%EC%9A%A9%EC%88%98&document_srl=9277> (2026-10-20 열람)
[^news-award]: KAIST 물리학과 소식 「제56회 과학의날 기념, 과기부 장관표창 수상」(2023-04-23) <https://physics.kaist.ac.kr/index.php?mid=p_news_event2&search_target=title_content&search_keyword=%EC%96%91%EC%9A%A9%EC%88%98&document_srl=14621> (2026-10-20 열람)
[^news-54]: KAIST 물리학과 소식 「KAIST 개교 54년 특별 포상 수상자」(2025-02-24) <https://physics.kaist.ac.kr/index.php?mid=p_news_event2&document_srl=17809> (2026-10-20 열람)
[^news-humantech]: KAIST 물리학과 소식 「제29회·제30회 삼성휴먼테크논문대상 수상」(2023-02-23, 2024-04-04) <https://physics.kaist.ac.kr/index.php?mid=p_news_event2&search_target=title_content&search_keyword=%EC%96%91%EC%9A%A9%EC%88%98&document_srl=14357>, <https://physics.kaist.ac.kr/index.php?mid=p_news_event2&search_target=title_content&search_keyword=%EC%96%91%EC%9A%A9%EC%88%98&document_srl=16288> (2026-10-20 열람)
[^p1]: C. Jeong 외, Y. Yang, Nature Communications 15, 3887 (온라인 2024-05-08). <https://doi.org/10.1038/s41467-024-48082-x> 초록 기준.
[^p2]: C. Jeong 외, Y. Yang, Nature Communications 16, 8026 (온라인 2025-08-28). <https://doi.org/10.1038/s41467-025-63448-5> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Lee, C. Jeong, Y. Yang, Nature Communications 12, 1962 (온라인 2021-03-30). <https://doi.org/10.1038/s41467-021-22204-1> 초록 기준.
[^p4]: H. Jo 외, Y. Yang, Nature Communications 13, 5957 (온라인 2022-10-10). <https://doi.org/10.1038/s41467-022-33236-6> 초록 기준.
[^p5]: J. Lee 외, Y. Yang, Physical Review Applied 19, 054062 (온라인 2023-05-18). <https://doi.org/10.1103/physrevapplied.19.054062> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: E. Lee 외, S. J. Yoo, Advanced Materials 37, 2504059 (온라인 2025-05-06). <https://doi.org/10.1002/adma.202504059> 초록 기준.
[^p7]: J. Lee 외, Y. Yang, Nano Letters 22, 665-672 (온라인 2022-01-10). <https://doi.org/10.1021/acs.nanolett.1c03773> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: Y. Kim, Y. Yang, Applied Physics Letters 128, 203701 (온라인 2026-05-20). <https://doi.org/10.1063/5.0313245> 초록 기준.

# 다물리통합 원자력 열수력 연구실 (MIGHTY Lab)

**KAIST 원자력및양자공학과 · 성지현 교수**

- 분야: 원자로 열수력(냉각수의 흐름과 열 전달), 비등(끓음) 열전달과 임계 열유속(끓음으로 뺄 수 있는 열의 한계), 다물리 계산, 영상·딥러닝 기반 유동 계측, 차세대 원자로와 원자력 전지, 가속기 표적 냉각
- 홈페이지: <https://mighty.kaist.ac.kr/>
- 근거와 출처: [MIGHTY Lab 근거 페이지](mighty-sources.md)

> 원자로 안에서 냉각수가 끓으며 열을 빼앗는 과정을 실험과 계산으로 밝히고, 소형 모듈 원자로 같은 차세대 원자로와 우주용 원자력 전지를 연구하는 연구실이다. 끓을 때 나는 소리를 인공지능으로 분석해 끓음 현상을 재는 기술도 만든다.[^home][^research][^p4]

## 무엇을 연구하나

연구실 이름 MIGHTY는 다물리 통합 원자력 열수력(Multiphysics-InteGrated Nuclear Thermal-HYdraulics)의 약자다. 연구실은 다물리 계산과 여러 규모·여러 상(물과 증기 등)이 섞인 실험으로 깨끗한 원자력 에너지의 경계를 넓히는 것을 목표로 하며, 안전성·효율·다용도성을 높인 차세대 원자로를 주요 주제로 든다.[^home]

연구 페이지는 현재 관심사로 여러 물리 현상을 통합하는 다물리 계산, 실험과 계산을 함께 하는 다상 열전달, 미세·나노 규모 표면 특성이 열수력에 주는 영향(연마, 스퍼터링(입자를 쏘아 얇은 막을 입히는 방법), 산화, 코팅과 광학 형상 측정기·원자힘 현미경(뾰족한 탐침으로 표면 높낮이를 재는 현미경)·전자현미경), 실험과 계산을 잇는 영상 처리·컴퓨터 비전 알고리즘, 물리 원리를 수식으로 세우는 기계론적 모델링을 든다.[^research] 응용 분야로는 소형 모듈 원자로(SMR)·마이크로 원자로와 용융염·가스·액체 금속 냉각 4세대 원자로, 상용 경수로의 안전(사고 저항성 핵연료 피복관, 피복관 침적물이 임계 열유속에 주는 영향), 고준위 방사성 폐기물을 줄이는 가속기 구동 핵변환 시스템과 동위원소 생산 표적, 방사성 동위원소 열전 발전기(RTG) 같은 원자력 전지를 적는다.[^research]

첫 번째 갈래는 **원자력 전지와 차세대 원자로 계산**이다. 베타선 전자를 전자기 트랩에 가둬 내는 사이클로트론 복사를 거둬들이는 새 원자력 전지 개념을 계산으로 제안했고,[^p1] 고온가스로 증기 발생기의 냉각수 흐름에 따른 진동을 해석했다.[^p2]

두 번째 갈래는 **인공지능 기반 유동·비등 계측**이다. 입자 영상 유속계(PIV, 흐름에 뿌린 입자 사진으로 속도를 재는 방법)의 해상도를 딥러닝으로 높였고,[^p3] 방사선 때문에 카메라를 쓸 수 없는 환경에서 끓을 때 나는 소리를 수중 마이크로 듣고 인공지능으로 열유속과 기포 특성을 추정하는 방법을 만들었다.[^p4]

세 번째 갈래는 **비등 열전달과 임계 열유속**이다. 미국 로스앨러모스 국립연구소 동위원소 생산 시설의 냉각 채널에서 일어나는 끓음을 실험과 계산으로 예측했고,[^p5] 원자로 핵연료 피복관 재료(지르칼로이-4)의 산화가 끓음 성능에 주는 영향만 따로 떼어 쟀다.[^p6] 박사 과정 지도교수 Matteo Bucci 연구팀과 함께 끓음 위기(표면이 증기막에 덮여 열 전달이 갑자기 나빠지는 현상)를 하나의 기준으로 설명했다.[^p7][^p8]

## 주요 연구 주제

### 1. 원자력 전지와 차세대 원자로

사이클로트론 복사 원자력 전지, 고온가스로 증기 발생기 진동.[^p1][^p2][^research] 대표 논문 1, 2.

### 2. 딥러닝 유동·비등 진단

PIV 해상도 향상, 음향 기반 비등 진단.[^p3][^p4] 대표 논문 3, 4.

### 3. 비등 열전달과 끓음 위기

가속기 표적 냉각, 피복관 산화, 끓음 위기 기준.[^p5][^p6][^p7][^p8] 대표 논문 5–8.

## 대표 논문

랩 학술지 목록(최근 6년)의 2021–2026년 논문에서 주제별로 골랐다. 교수가 2023년 KAIST에 부임해, 5–8은 미국 MIT·로스앨러모스 국립연구소 시기의 연구다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2026 | [A novel beta nuclear battery concept by harvesting cyclotron emission](https://doi.org/10.1016/j.net.2026.104324) · Nuclear Engineering and Technology | 기존 원자력 전지(RTG, 베타 전지)는 효율 한계가 있다. 베타선 전자를 페닝–맘버그 트랩(전기장·자기장으로 입자를 가두는 장치)에 가두고, 전자가 도는 동안 내는 전자기파를 28 GHz 공진기로 거둬들이는 새 개념을 계산으로 보였다. 이론 변환 효율은 34.4%였다.[^p1] | 1저자 Sungbeen Park, 교신 성지현 |
| 2 | 2025 | [An investigation of flow-induced vibrations (FIV) during cold testing on a helical tube steam generator for a high-temperature gas-cooled reactor (HTGR)](https://doi.org/10.1016/j.anucene.2025.111597) · Annals of Nuclear Energy | 고온가스로용 나선관 증기 발생기를 열을 가하지 않은 상태로 시험할 때 흐름이 일으키는 진동 위험을 계산 소프트웨어로 해석했다. 압력 분포, 유량, 진동 주파수를 분석해 기계적 신뢰성 평가에 필요한 정보를 얻었다.[^p2] | 1저자 Muhammad Subhan, 마지막 저자 성지현 |
| 3 | 2023 | [Deep learning-based spatial refinement method for robust high-resolution PIV analysis](https://doi.org/10.1007/s00348-023-03595-x) · Experiments in Fluids | 흐름 사진의 작은 영역 쌍을 받아 국소 속도를 내도록 광학 흐름 신경망(FlowNet2)을 고치고, 기존 상관 기반 정밀화 방법과 결합해 작은 흐름부터 큰 이동까지 속도장을 정확하게 얻었다.[^p3] | 1저자 Jun Sung Choi, 공동 교신 Eung Soo Kim·성지현 |
| 4 | 2026 | [A non-intrusive framework using acoustic signals and deep learning for boiling diagnostics in visual-limited environments](https://doi.org/10.1038/s41598-026-41757-z) · Scientific Reports | 방사선 등으로 카메라를 쓰기 어려운 곳에서 끓을 때 나는 소리를 수중 마이크로 녹음해 주파수 영상으로 바꾸고, 합성곱 신경망(이미지 패턴을 찾는 인공지능)으로 열유속(벽에서 물로 전달되는 열의 양), 벽면 과열도(벽 온도가 끓는점보다 높은 정도), 기포 특성을 추정했다. 잡음이 섞여도 예측이 유지됐다.[^p4] | 1저자 Pei-Hsun Huang, 성지현 둘째 저자, 마지막 저자 Ellen M. O’Brien |
| 5 | 2023 | [Development of experimental and computational frameworks to predict subcooled flow boiling in the LANL Isotope Production Facility](https://doi.org/10.1016/j.ijheatmasstransfer.2022.123836) · International Journal of Heat and Mass Transfer | 로스앨러모스 국립연구소 동위원소 생산 시설의 표적은 양성자 빔으로 뜨거워져 냉각 채널에서 끓음이 생기지만 방사선 때문에 직접 볼 수 없다. 같은 조건의 끓음 실험과 계산 틀을 만들어 그 거동을 예측했다.[^p5] | 1저자 성지현, 마지막 저자 Christiaan Vermeulen |
| 6 | 2022 | [Separate effect of oxidation on the subcooled flow boiling performance of Zircaloy-4 at atmospheric pressure](https://doi.org/10.1016/j.ijheatmasstransfer.2022.122620) · International Journal of Heat and Mass Transfer | 같은 지르칼로이-4 시편을 산화 단계별로 시험해 산화만의 영향을 끓음 열전달과 임계 열유속에서 떼어 쟀다. 겉보기에 같은 시편도 끓음 거동이 크게 다를 수 있어 별도 시험 절차를 만들었다.[^p6] | 1저자 성지현, 마지막 저자 Matteo Bucci |
| 7 | 2023 | [A unifying criterion of the boiling crisis](https://doi.org/10.1038/s41467-023-37899-7) · Nature Communications | 끓음 위기가 표면 근처 기포들의 상호작용이 불안정해지는 퍼콜레이션(연결이 갑자기 이어지는 현상)으로, 핵생성 밀도, 기포 접촉 반지름, 성장 시간과 이탈 빈도라는 세 값으로 정해지는 기준을 따른다는 것을 이론과 실험으로 보였다.[^p7] | 1저자 Limiao Zhang, 성지현 공저, 마지막 저자 Matteo Bucci |
| 8 | 2021 | [Decrypting the boiling crisis through data-driven exploration of high-resolution infrared thermometry measurements](https://doi.org/10.1063/5.0048391) · Applied Physics Letters | 고해상도 적외선 측정으로 얻은 기포 데이터로 끓음 위기까지의 여유를 예측하는 신경망을 만들고, 기포 관련 네 값이 모두 똑같이 중요하다는 것을 보였다.[^p8] | 1저자 Madhumitha Ravichandran, 성지현 공저, 마지막 저자 Matteo Bucci |

## 교수와 전문 분야

성지현 교수는 서울대 원자핵공학 학사(2010–2014)와 에너지시스템공학 석사(2014–2016), 미국 MIT 원자력공학 박사(2016–2021, 지도교수 Matteo Bucci)를 받았다. 미국 로스앨러모스 국립연구소 동위원소 생산팀 박사후연구원(2021–2022)과 가속기 운영기술 부문 기계설계 그룹 엔지니어(2022–2023)를 거쳐 2023년 KAIST 원자력및양자공학과 조교수로 부임했다.[^members][^nqe]

논문으로 보면 전문 분야는 세 갈래다.

- **원자력 전지와 원자로 계통 해석**.[^p1][^p2]
- **딥러닝 기반 유동·비등 진단**.[^p3][^p4]
- **비등 열전달과 끓음 위기 실험**.[^p5][^p6][^p7][^p8]

## 응용 분야

대표 논문과 연구 페이지로 보면 소형 모듈 원자로와 고온가스로, 상용 원자로 핵연료 안전, 가속기 동위원소 생산 시설 냉각, 우주용 원자력 전지에 닿아 있다.[^research][^p1][^p2][^p5]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다. 구성원 페이지는 이름, 과정, 이메일만 적는다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| LEE, Hyun Kyu (이현규) | 박사후연구원 | hklee.mighty@kaist.ac.kr |  |
| LEE, JAE HO (이재호) | 대학원생 | lee990504@kaist.ac.kr |  |
| Na, YongHyun (나용현) | 대학원생 | nayh0518@kaist.ac.kr |  |
| JEONG, SEOKHWAN (정석환) | 대학원생 | jeong1567@kaist.ac.kr |  |
| kairolla, miras | 학부 연구생 | kai.miras.47@kaist.ac.kr |  |
| kim, ji Hyun (김지현) | 행정 직원 | jhkim9224@kaist.ac.kr |  |

## 졸업생

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| KIM, Yong Se (김용세) | M.S. |  |
| Rambe, Farhan Najmi | M.S. |  |

## 최근 논문 목록 (2021–2026)

랩 학술지 목록(최근 6년)의 2021–2026년 논문 12편이다. 교신저자 표시(*)는 랩 표기다.[^papers]

**2026**

- S. Park, B. Ahn, Y. -C. Ghim, J. H. Seong\*. "A novel beta nuclear battery concept by harvesting cyclotron emission". *Nuclear Engineering and Technology, 58, 8*.
- P.-H. Huang, J. H. Seong, J. M. Castro-Aguilar, C. Vermeulen, E. M. O'Brien\*. "A non-intrusive framework using acoustic signals and deep learning for boiling diagnostics in visual-limited environments". *Scientific Reports*.

**2025**

- M. Subhan\*, T.P. Soemardi\*, A. S. Baskoro, T. Setiadipura, E. Latifah, C. S. Abadi, J. H. Seong. "An investigation of flow-induced vibrations (FIV) during cold testing on a helical tube steam generator for a high-temprature gas-cooled reactor (HTGR)". *Annals of Nuclear Energy, 222, 111597*.

**2023**

- J. S. Choi, E. S. Kim\*, J. H. Seong\*. "Deep learning based spatial refinement method for robust high-resolution PIV analysis". *Experiments in Fluids (EIF], 64, 45*.
- J. H. Seong, J. Morrell, B. Singh, K. Woloshun, E. Olivas, P. Lance, N. Kollatrik, E. O'Brien\*, c. Vermeulen. "Development of experimental and computational frameworks to predict subcooled flow boiling in the LANL Isotope Production Facility". *International Journal of Heat and Mass Transfer (IJHMT), 203, 123836*.
- J. H. Seong, M. Ravichandran, G. Su, B. Phillips, M. Bucci\*. "Automated bubble analysis of high-speed subcooled flow boiling images using U-Net Transfer learning and global optical flow". *International Journal of Multiphase Flow (IJMF), 159, 104336*.
- L. Zhang, C. Wang, G. Su, A. Kossolapov, G. M. Aguiar, J. H. Seong, F. Chavagnat, B. Phillips, M. M. Rahman, M. Bucci\*. "A unifying criterion of the boiling crisis". *Nature Communications, 14, 2321*.

**2022**

- J. H. Seong, C. Wang, B. Phillips, M. Bucci\*. "The effect of PVD-coated chromium on the subcooled flow boiling performance of nuclear reactor cladding materials". *Applied Thermal Engineering (ATE), 213, 118670*.
- J. H. Seong, C. Wang, B. Phillips, M. Bucci\*. "Separate effect of oxidation on the subcooled flow boiling performance of Zircaloy-4 at atmospheric pressure". *IJHMT, 188, 122620*.
- Y. Song, C. Wang, D. J. Preston, G. Su, M. M. Rahman, H. Cha, J. H. Seong, B. Phillips, M. Bucci, E. N. Wang\*. "Enhancement of boiling with scalable sandblasted surfaces". *ACS Applied Material and Interfaces, 14, 9788-9794*.
- Y. Song, H. Cha, Z. Liu, J. H. Seong, L. Zhang, D. J. Preston, E. N. Wang\*. "Alteration of pool boiling heat transfer on metallic surfaces by in situ oxidation". *IJHMT, 185, 122320*.

**2021**

- M. Ravichandran, G. Su, C. Wang, J. H. Seong, A. Kossolapov, B. Phillips, M. M. Rahman, M. Bucci\*. "Decrypting the boiling crisis through data-driven exploration of high-resolution infrared thermometry measurements". *Applied Physics Letters (APL), 118, 253903*.

## 연락과 위치

- 교수 이메일: sjhyunmit@kaist.ac.kr[^contact][^nqe]
- 교수실: KAIST N7-1동 2403호 (대전 유성구 대학로 291)[^contact]

[^home]: MIGHTY Lab 누리집 첫 화면 <https://mighty.kaist.ac.kr/> (2026-10-19 열람)
[^research]: MIGHTY Lab 연구 페이지 <https://mighty.kaist.ac.kr/research> (2026-10-19 열람)
[^members]: MIGHTY Lab 구성원 페이지 <https://mighty.kaist.ac.kr/members> (2026-10-19 열람)
[^papers]: MIGHTY Lab 논문 목록 <https://mighty.kaist.ac.kr/publications> (2026-10-19 열람)
[^contact]: MIGHTY Lab 연락처 <https://mighty.kaist.ac.kr/contact> (2026-10-19 열람)
[^nqe]: KAIST 원자력및양자공학과 연구실 목록 <https://nuclear.kaist.ac.kr/eng/research/the_lap.php> (2026-10-19 열람)
[^p1]: S. Park, B. Ahn, Y.-C. Ghim, J. H. Seong, Nuclear Engineering and Technology 58, 104324 (2026). <https://doi.org/10.1016/j.net.2026.104324> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p2]: M. Subhan 외, J. H. Seong, Annals of Nuclear Energy 222, 111597 (2025). <https://doi.org/10.1016/j.anucene.2025.111597> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p3]: J. S. Choi, E. S. Kim, J. H. Seong, Experiments in Fluids 64, 45 (온라인 2023-02-21). <https://doi.org/10.1007/s00348-023-03595-x> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p4]: P.-H. Huang 외, E. M. O’Brien, Scientific Reports 16, 14934 (온라인 2026-03-25). <https://doi.org/10.1038/s41598-026-41757-z> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. H. Seong 외, C. Vermeulen, International Journal of Heat and Mass Transfer 203, 123836 (2023). <https://doi.org/10.1016/j.ijheatmasstransfer.2022.123836> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p6]: J. H. Seong, C. Wang, B. Phillips, M. Bucci, International Journal of Heat and Mass Transfer 188, 122620 (2022). <https://doi.org/10.1016/j.ijheatmasstransfer.2022.122620> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p7]: L. Zhang 외, M. Bucci, Nature Communications 14, 2321 (온라인 2023-04-22). <https://doi.org/10.1038/s41467-023-37899-7> 초록 기준.
[^p8]: M. Ravichandran 외, M. Bucci, Applied Physics Letters 118, 253903 (온라인 2021-06-23). <https://doi.org/10.1063/5.0048391> 초록 기준.

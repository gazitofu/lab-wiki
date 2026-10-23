# 의료전자 및 방사선광공학 연구실 (Medical Electronics & Radiation Photonics Lab, MERP Lab)

**KAIST 원자력및양자공학과 · 고근배 교수**

- 분야: 초고속 방사선 검출기, 차세대 의료 영상 시스템(양전자 방출 단층촬영·광자 계수 CT), 인공지능 기반 의료 영상 처리, 반도체 광검출기와 고속 전자회로
- 대분야: 전기전자·반도체·광학, 물리·양자
- 태그: 광검출기[^research], 집적회로 설계[^research], X선 영상·회절[^research], 컴퓨터 비전[^research], 과학·공학 AI[^research]
- 홈페이지: <https://merp.kaist.ac.kr/>
- 근거와 출처: [MERP Lab 근거 페이지](merp-sources.md)

> 몸을 통과하거나 몸에서 나오는 방사선을 잡아 의료 영상으로 바꾸는 검출기와 전자회로, 영상 장치를 만드는 연구실이다. 방사선이 들어온 시각을 정밀하게 재는 검출기, 뇌 전용 양전자 방출 단층촬영 장치와 광자 계수 CT, 인공지능으로 영상의 잡음을 줄이는 방법, 빛을 전기 신호로 바꾸는 반도체 소자와 전용 칩을 연구한다.[^home][^research]

## 무엇을 연구하나

연구실은 KAIST 원자력및양자공학과 고근배 조교수가 이끈다. 학과 연구실 목록은 방사선 분야에 「의료전자 및 방사선광공학 연구실」을 올리고 있다.[^deptlab] 교수는 2025년 7월 KAIST에 부임했다.[^prof]

누리집은 연구실이 방사선을 이용한 영상·치료 기술을 다루며, 광자와 하전 입자 같은 보이지 않는 에너지를 진단과 치료에 쓸 정보로 바꾸는 것을 목표로 한다고 소개한다.[^home] 이를 위해 양전자 방출 단층촬영(PET, 몸에 넣은 방사성 추적자에서 나온 양전자가 소멸하며 내는 감마선 쌍을 잡아 그 분포를 영상으로 만드는 장치), 광자 계수 CT(PCCT, 엑스선 광자를 하나하나 세고 에너지를 구분해 단면 영상을 만드는 CT), 이들을 합친 복합 영상 장치에 쓸 차세대 검출기·센서, 영상 형성·처리 알고리즘, 시스템을 개발한다고 적는다.[^home] 나노 광학, 메타물질(인공 구조의 배열을 설계해 자연 물질에 없는 광학 성질을 내도록 만든 소재), 초고속 전자회로, 실시간 인공지능 처리를 활용해 의료 영상의 공간·시간 분해능을 높이는 것을 목표로 하며, 질병을 더 일찍 찾고 환자가 받는 방사선량을 줄이고 치료 결과를 높이는 데 쓰겠다고 설명한다.[^home]

Research 페이지는 연구를 네 갈래로 나눈다.[^research] 첫째는 **초고속 방사선 검출기**다. 섬광체(방사선을 받으면 빛을 내는 물질)의 빛 발생량을 늘리고 섬광체와 광센서 사이의 빛 전달을 최적화하는 광학 기술, 첨단 전자회로, 엣지 AI(데이터가 생기는 기기 가까이에서 바로 계산하는 인공지능) 신호 처리를 함께 써서 방사선이 들어온 시각을 정밀하게 뽑아낸다고 적는다. 이 방법으로 방사선 사건을 10피코초 미만에 다가가는 시간 정밀도로 잡는다고 설명한다.[^research] 둘째는 **차세대 의료 영상 시스템**이다. 비행시간(TOF, 두 감마선이 검출기에 닿는 시각 차이로 발생 위치를 좁히는 기술)과 반응 깊이(DOI, 감마선이 결정 안 어느 깊이에서 반응했는지 재는 기술), 인공지능 영상 재구성을 합친 뇌 전용 PET를 개발하고, 섬광 변환 없이 소멸 광자(양전자가 전자와 만나 사라지며 내는 감마선)를 직접 검출하는 직접 양전자 방출 영상(dPEI)과 TOF를 더한 광자 계수 CT를 연구한다고 적는다.[^research] 셋째는 **인공지능 기반 의료 영상**으로, 심층 신경망부터 생성 모델·확산 모델까지 쓰는 의료 영상 잡음 제거·화질 개선 틀과, 영상과 촬영 조건·임상 맥락·문서 지식을 대형 언어 모델(LLM)로 함께 다루는 멀티모달 인공지능을 연구한다고 적는다.[^research] 넷째는 **반도체 광검출기와 고속 전자회로**로, 실리콘 광증배관(SiPM, 광자 하나 수준의 빛도 전기 신호로 바꿀 수 있는 반도체 광센서) 같은 광검출기의 새 구조를 설계·제작하고, 신호 증폭·시간-디지털 변환·데이터 처리를 맡는 전용 집적회로(ASIC)를 함께 만든다고 적는다.[^research]

교수가 KAIST에 부임한 뒤 출판된 대표 논문 세 편은 섬광체 표면에 나노 무늬를 새겨 빛 추출을 늘린 연구(대표 논문 1), 뇌·유방·팔다리를 찍는 PET 장치 PHAROS의 첫 사람 영상 결과(대표 논문 2), 플라즈마 장치의 빛을 여러 채널로 재 2차원 영상으로 복원하는 계측 시스템(대표 논문 3)이다.[^p1][^p2][^p3]

## 주요 연구 주제

### 1. 초고속 방사선 검출기와 섬광체

섬광체와 광센서 사이에서 잃는 빛을 줄이고 신호 처리로 시간 정밀도를 높여, 복잡한 영상 재구성 없이 빠르게 분자 영상을 얻는 직접 양전자 방출 영상과 산란된 신호를 시간 정보로 걸러 내는 TOF-CT를 목표로 한다.[^research] 대표 논문 1은 섬광체 표면에 나노 무늬를 찍어 빛 추출과 시간 분해능을 높였다.[^p1]

### 2. 차세대 의료 영상 시스템

TOF·DOI·인공지능 영상 재구성을 합친 뇌 전용 PET, 직접 양전자 방출 영상, 정지형 CT(선원과 검출기를 돌리지 않고 찍는 CT) 구조와 초고속 검출기를 쓴 광자 계수 CT를 연구한다. 정지형 CT로는 영상 획득을 빠르게 해 심장처럼 움직이는 장기를 움직임 없이 찍는 것을 목표로 한다.[^research] 대표 논문 2.

### 3. 인공지능 기반 의료 영상

저선량 영상을 돕고 진단 신뢰도를 높이는 범용 인공지능 플랫폼을 목표로, 의료 영상 잡음 제거·화질 개선과 멀티모달 인공지능을 연구한다.[^research]

### 4. 반도체 광검출기와 고속 전자회로

광 검출 효율과 시간 정밀도를 높이고 큰 면적으로 넓히기 쉬운 광검출기 구조를 설계·제작하고, 센서와 신호를 읽는 전용 집적회로를 함께 개발해 PET·CT·복합 영상 장치용 모듈을 만든다고 적는다.[^research] 대표 논문 3의 계측 시스템도 실리콘 광증배관 기반 검출부를 쓴다.[^p3]

## 대표 논문

고근배 교수가 KAIST에 부임한 2025년 7월 뒤 출판된 논문 세 편을 모두 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [Enhanced light extraction in flex-mold nanopatterned scintillators for TOF-PET](https://doi.org/10.1088/1361-6560/ae97d1) · Physics in Medicine & Biology | TOF-PET 검출기에서는 섬광 결정과 광센서 사이 경계에서 잃는 빛이 에너지 분해능과 동시 계수 시간 분해능(CTR, 두 감마선의 도착 시각 차이를 얼마나 정확히 재는지 나타내는 값)을 제한한다. 연구진은 섬광 결정 표면에 빛을 회절시키는 나노 무늬를 입혀 빛 추출을 늘렸다. 유연한 틀로 찍어 내는 소프트 리소그래피로 300 nm 구멍·선 무늬를 센티미터 규모 결정 표면에 상대 치수 편차 4% 미만으로 새겼고, LYSO·BGO·GAGG 세 섬광체를 공기와 광학 그리스, 맨 결정과 무늬 결정을 조합한 네 가지 결합 조건에서 시험했다. 3 × 3 × 20 mm³ BGO에 구멍 무늬(H_hole-plaid)와 광학 그리스를 쓰면 맨 결정·공기 결합보다 빛 추출이 최대 2.22배였고 에너지 분해능은 18%에서 11%로 좋아졌다. 같은 공정을 3 × 3 × 20 mm³ LYSO와 5 × 5 × 5 mm³ GAGG에 적용하자 빛 추출 이득은 1.58배와 1.72배였다. 무늬를 새긴 3 × 3 × 20 mm³ LYSO 결정의 평균 CTR은 고정 문턱에서 250.6 ps(맨 결정·공기)에서 142.6 ps(선 무늬·광학 그리스)로 줄었고, 문턱값을 더 맞추자 가장 좋은 값이 132.0 ps였다. 무늬는 기계적 하중과 20회 반복 세척 뒤에도 이득 대부분을 유지했다.[^p1] | 1저자 S. Hyeon, 마지막 저자 M. S. Lee(고근배 교수는 넷 중 셋째) |
| 2 | 2026 | [First-in-Human Imaging Results of PHAROS: A Versatile High-Resolution TOF/DOI PET Scanner for Brain, Breast, and Extremity Imaging](https://doi.org/10.2967/jnumed.125.271172) · Journal of Nuclear Medicine | TOF와 DOI 기술을 합친 고해상도 다기능 PET 장치 PHAROS의 설계와 성능, 뇌·유방 첫 사람 영상 결과를 여러 자세에서 보고했다. 검출기 머리를 움직이고 환자 침대 모양을 바꿀 수 있어 앉은 자세와 누운 자세의 뇌 영상, 유방과 팔다리 영상을 찍을 수 있다. 평가한 구성의 PET 고리는 검출기 구역 20개로 이뤄지고 축 방향 시야는 19.6 cm다. 블록 검출기마다 1.92 × 1.92 × 15 mm³ LSO 결정 8 × 8개를 4 × 4 실리콘 광증배관 배열 두 개에 붙여 DOI를 읽는다. 3차원 뇌 모형(Hoffman 팬텀)과 첫 사람 촬영([18F]FDG 뇌 영상, [18F]florbetaben 아밀로이드 영상, [18F]FP-CIT 도파민 운반체 영상, 엎드린 자세 [18F]FDG 유방 영상)으로 성능을 평가했고, 모든 영상은 TOF와 DOI 정보를 넣은 3차원 반복 재구성(OSEM)으로 만들었다. 모형 영상에서 대뇌 겉질과 그 아래 구조가 인공물 없이 선명하게 보였고, 건강한 자원자의 뇌 영상에서 회색질과 백색질의 대비가 뚜렷했으며, 유방 영상에서는 여러 종괴가 배경과 뚜렷이 구분됐다. 초록은 이 결과가 높은 공간 분해능과 화질을 보여 주며, 신경계·종양 영상을 비롯한 여러 임상·연구 용도에 쓸 수 있다고 결론짓는다.[^p2] | 1저자 고근배, 마지막 저자 J. S. Lee |
| 3 | 2026 | [Development of a multichannel filterscope system for two-dimensional plasma imaging in a magnetic mirror](https://doi.org/10.1063/5.0347709) · Review of Scientific Instruments | KAIST 자기 거울 장치(자기장으로 플라즈마를 가두는 실험 장치)에서 플라즈마가 내는 빛을 시간에 따라 2차원 영상으로 찍는 다채널 필터스코프 시스템을 개발했다. 진공 용기 안에 슬릿 바늘구멍 사진기 구조의 수신 모듈 세 개를 120° 간격으로 두어 플라즈마 단면을 가로지르는 시선 21개를 만들고, 플라즈마 빛은 슬릿으로 고르고 렌즈로 평행하게 모은 뒤 좁은 대역 필터로 걸러, 광 피드스루와 광섬유 다발로 용기 밖의 실리콘 광증배관 검출부에 보낸다. 헬륨 방전 실험에서 21개 채널 모두가 668 nm 근처의 중성 헬륨 빛을 동시에 시간에 따라 검출했고, 이득을 보정한 신호로 2차원 발광 분포를 복원해 축 대칭이 아닌 발광 구조와 그 시간 변화를 보였다.[^p3] | 1저자 D. Kim, 마지막 저자 C. Sung(고근배 교수는 아홉 중 일곱째) |

## 교수와 전문 분야

고근배 교수(Guen Bae Ko)는 KAIST 원자력및양자공학과 조교수(Assistant Professor)다.[^prof][^deptfac] 서울대학교에서 전기공학 학사(2010, 최우등)와 의과학(Biomedical Sciences) 박사(2017)를 받았다. 박사 논문은 소형 동물의 PET와 자기공명영상(MRI)을 동시에 찍는 실리콘 광증배관 PET를 다뤘고, 학사 논문은 클록 복원용 디지털 위상 고정 루프(기준 신호에 맞춰 일정한 주파수의 신호를 만드는 회로) 설계였다.[^prof]

경력으로는 LG전자 Digital Display Research Lab. 인턴(2008), 서울대병원 핵의학과 인턴(2008–2010), 서울대학교 의학연구원(SNU Medical Research Center) Assistant Researcher(2010–2013)와 Researcher(2013–2014)를 거쳤다. 2016년 10월부터 2025년 6월까지 브라이토닉스이미징(Brightonix Imaging Inc.)의 공동 창업자로 최고기술책임자(CTO)·부사장(EVP)을 맡았고, 2017년 7월부터 2025년 6월까지 서울대학교 방문연구원으로 있었다. 2025년 7월 KAIST 원자력및양자공학과 조교수로 부임했다.[^prof]

수상으로는 SNMMI의 Alavi-Mandell Publication Award(2017), IEEE NSS/MIC/RTSD의 Paul Phelps Grant와 Conference Trainee Grant(2015, 2016), IEEE NPSS Graduate Scholarship Award(2016), SNM Computer & Instrumentation Council의 Young Investigator Award(2013) 등을 받았다.[^prof]

누리집 논문 목록(2011–2026년 41편)으로 보면 전문 분야는 실리콘 광증배관을 쓴 PET 검출기와 PET/MRI 동시 영상 장치, 검출기 신호를 읽는 전자회로다.[^pubs] 2011–2019년 논문에는 여러 채널의 실리콘 광증배관 신호를 읽는 아날로그 회로, FPGA(프로그래밍으로 회로 구성을 바꿀 수 있는 반도체 칩)로 만든 시간-디지털 변환기, 톱니 모양 문턱값으로 신호를 시간 기준으로 표본화하는 방법, 신호선을 줄이는 다중화 읽기 방법이 이어진다.[^pubs] 2020–2024년 논문은 소형 동물용 PET/MRI 삽입형 장치 SimPET 계열의 성능 평가, 7테슬라 MRI와 함께 쓰는 뇌 PET 삽입 장치, 체렌코프 빛을 쓰는 BGO 양단 읽기 PET 검출기, FPGA만으로 하는 TOF-PET 신호 디지털화를 다룬다.[^pubs]

## 응용 분야

누리집은 연구의 쓰임으로 질병의 조기 발견, 환자 방사선량 감소, 치료 결과 개선을 들고, 검출기와 전자회로를 PET·CT·복합 영상 장치용 모듈로 만든다고 적는다.[^home][^research] 대표 논문이 직접 든 쓰임은 TOF-PET 검출기의 빛 추출과 시간 분해능 개선,[^p1] 뇌·유방·팔다리를 찍고 신경계·종양 영상에 쓰는 PET 장치,[^p2] 자기 거울 플라즈마 장치의 발광 영상 계측이다.[^p3] 교수 개인 목록인 누리집 특허 목록에는 신호 검출·처리 모듈, 섬광 검출기와 PET 장치, 복강경 수술용 융합 영상 장치, 자기공명영상 장치용 삼중 주파수 RF 안테나 같은 발명이 올라 있다.[^patents]

## 구성원

누리집 Members 페이지의 박사후연구원(Postdoctoral Researcher), 박사과정(Ph.D. Student), 학부 연구생(Undergraduate Researcher)이다. 과정·연구 분야·이메일은 페이지 표기 그대로다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Amar Prasad Gupta | 박사후연구원 | X-ray Source · Imaging System · DBT | apgupta@kaist.ac.kr |  |
| Hyeong Seok Shim | 박사후연구원 | PET Hardware · Fast Timing · ICS | s0h4s30@kaist.ac.kr |  |
| Suhan Choi | 박사과정 | PET Electronics · Signal Multiplexing | suhan.choi@kaist.ac.kr | 1 |
| Jaeyong Kim | 학부 연구생 | Stationary CT · Image Processing | jyong04@kaist.ac.kr |  |
| Gunhee Bae | 학부 연구생 | Radiation Detection Electronics · Signal Processing | kflying11@kaist.ac.kr |  |
| Arpon Krishna Roy | 학부 연구생 | Pulsed X-ray Source | arpon.roy@kaist.ac.kr |  |
| Swadhin Roy Sunny | 학부 연구생 | PET Data Processing | swadhin@kaist.ac.kr |  |

## 최근 논문 목록 (2021–2026)

누리집 Journals 페이지는 고근배 교수 개인의 학술지 논문 목록(2011–2026년 41편)이어서, 교수가 2025년 7월 KAIST에 부임하기 전 서울대학교·브라이토닉스이미징에 있던 시기의 논문이 함께 들어 있다.[^pubs][^prof] 아래는 연도가 2021–2026년인 12편(2026년 3, 2024년 5, 2023년 3, 2021년 1편)이고, 2021–2024년 9편은 부임 전에 출판된 논문이다. 저자·제목·학술지·연월·권호는 페이지 표기 그대로다.[^pubs]

**2026**

- Kim D, Lee M, Oh D, Jung Y, Moon C, Lee SG, Ko GB, Kim J, Sung C. "Development of a multichannel filterscope system for twodimensional plasma imaging in a magnetic mirror". *Rev Sci Instrum. Oct 2026; 97:103504*.
- Hyeon S, Choi S, Ko GB, Lee MS. "Enhanced Light Extraction in Flex-Mold Nanopatterned Scintillators for TOF-PET". *Phys Med Biol. Aug 2026; 71(16):165031*.
- Ko GB, Kim KY, Kang SK, Lee J, Jung R, Kwak DJ, Son J-W, Shin SA, Ryoo HG, Kang Y, Kim S, Paeng JC, Byun MS, Shin JH, Cheon GJ, Kim YK, Choi H, Lee JS. "First-in-Human Imaging Results of PHAROS: A Versatile High-Resolution TOF/DOI PET Scanner for Brain, Breast, and Extremity Imaging". *J Nucl Med. May 2026; 67(8):1329-1335*.

**2024**

- Ko GB, Kwak D, Lee JS. "Enhanced Timing Performance of Dual‑Ended PET Detectors for Brain Imaging Using Dual‑Finishing Crystal Approach". *Sensors. Oct 2024; 24(20):6520*.
- Hernandez D, Nam T, Lee E, Ko GB, Lee JS, Kim K-N. "Triple Antenna Combination for PET‑MRI Imaging Compatible with 3, 7 and 11.74T MRI Scanner". *Int J Imaging Syst Technol. Sep 2024; 34:e23191*.
- Suh M, Park JY, Ko GB, Kim JY, Hwang DW, Rees L, Conway GE, Doak SH, Kang H, Lee N, Hyeon T, Lee Y-S, Lee DS. "Optimization of micelle‑encapsulated extremely small sized iron oxide nanoparticles as a T1 contrast imaging agent: biodistribution and safety profile". *J Nanobiotech. July 2024; 22(1):419*.
- Ko GB, Lee JS. "Dual Threshold Input Receiver FPGA‑only Signal Digitization Method for Time‑of‑Flight Positron Emission Tomography". *Biomed Eng Lett. May 2024; 14(4):847–858*.
- Yi M, Ko GB, Lee JS. "Pushing the limit of BGO‑based dual‑ended Cherenkov PET detectors through photon transit time correction". *Phys Med Biol. Jan 2024; 69(2):025005*.

**2023**

- Lee S, Park J, Lee JS, Seo H, Ko GB, Seo JM, Kim SM. "Comparative study on gamma‑ray detectors for in‑situ ocean radiation monitoring system". *Appl Radiat Isot. Apr 2023; 110826*.
- Seo M, Park H, Lee S, Ko GB, Lee JS. "Depth‑of‑interaction positron emission tomography detector with 45‑degree tilted silicon photomultipliers using dual‑ended signal readout". *Med Phys. Mar 2023; 50(7):4112–4121*.
- Seo M, Ko GB, Kim KY, Son JW, Byun JW, Lee Y-S, Kim KM, Park JW, Kim K, Lee T, Lee JS. "Performance Evaluation of SimPET‑L and SimPET‑XL: MRI‑Compatible Small‑Animal PET Systems with Rat‑Body Imaging Capability". *EJNMMI Phys. Mar 2023; 10(1):16*.

**2021**

- Won JY, Park H, Lee S, Son J-W, Chung Y, Ko GB, Kim KY, Song J, Seo S, Ryu Y, Chung J-Y, Lee JS. "Development and Initial Results of a Brain PET Insert for Simultaneous 7‑Tesla PET/MRI Using an FPGA‑Only Signal Digitization Method". *IEEE Trans Med Imaging. Feb 2021; 40(6):1579–1590*.

## 특허

누리집 Patents 페이지도 교수 개인의 특허 목록(18건)이어서, 누리집이 적은 연월로 보면 대부분 KAIST 부임(2025년 7월) 전의 항목이다.[^patents][^prof] 아래는 누리집이 적은 연월이 2021년 10월 이후인 13건이다. 날짜는 누리집이 적은 연월이고, 번호·제목·국가·발명자는 페이지 표기 그대로다.[^patents]

- 2026-02 · 다채널 신호처리모듈 및 신호처리 장치 (Multi-channel signal processing module and signal processing apparatus) (번호 10-2928968; 국가 대한민국; 발명자 고근배, 이재성, 손정환)
- 2025-08 · 에너지의 변동 상황을 모니터링하기 위한 데이터 처리 방법 (Data processing method for monitoring energy fluctuations) (번호 10-2025-0112506; 국가 대한민국; 발명자 고근배, 이재성, 박상근)
- 2025-07 · 삼중 주파수 RF 안테나, 이를 이용한 다중 주파수 공진 제어 방법 및 이를 포함하는 자기공명영상 장치 (TRIPLE FREQUENCY RF ANTENNA, MULTI-FREQUENCY RESONANCE CONTROL METHOD USING THE SAME AND MAGNETIC RESONANCE IMAGING APPARATUS INCLUDING THE SAME) (번호 10-2025-0096132; 국가 대한민국; 발명자 김경남, 호세 다니엘 에르난데스 창, 이재성, 고근배)
- 2025-05 · 의자 (A Chair) (번호 10-2813900; 국가 대한민국; 발명자 김효성, 고근배, 이재성)
- 2025-05 · 양방향 회전이 가능한 커넥터 모듈 (Connector module with two-way rotation) (번호 10-2813884; 국가 대한민국; 발명자 김효성, 고근배, 이재성)
- 2025-01 · 이미지 생성 방법 (Method for create an image) (번호 10-2025-0011301; 국가 대한민국; 발명자 고근배, 이재성, 박상근)
- 2025-01 · 신호 검출 모듈 (Signal detection module) (번호 10-2025-0003312; 국가 대한민국; 발명자 고근배, 곽동진, 이재성)
- 2025-01 · 신호 검출 장치 및 방법 (Signal detection device and method thereof) (번호 10-2025-0003273; 국가 대한민국; 발명자 고근배, 곽동진, 이재성)
- 2025-01 · 신호 처리 방법 및 장치 (Signal processing method and device thereof) (번호 10-2025-0001203; 국가 대한민국; 발명자 이민석, 고근배, 이재성)
- 2024-10 · 신호처리모듈 및 신호처리 장치 (Signal processing module and signal processing apparatus) (번호 10-2024-0133833; 국가 대한민국; 발명자 고근배, 이재성, 손정환)
- 2024-06 · 섬광 검출기 및 이를 이용한 양전자방출단층촬영장치 (SCINTILLATOR DETECTOR AND POSITRON EMISSION TOMOGRAPHY APPARATUS USING THE SAME) (번호 10-2679432; 국가 대한민국; 발명자 고근배, 이재성, 서민지, 박해욱)
- 2022-10 · 복강경 수술용 융합영상장치 (HYBRID IMAGING APPARAYUS FOR LAPAROSCOPIC SURGERY) (번호 10-2022-0140242; 국가 대한민국; 발명자 이재성, 고근배, 손정환, 홍성종, 송성현, 한영빈)
- 2022-05 · Ultrafine iron oxide nanoparticle-based magnetic resonance imaging t1 contrast agent (번호 20220143225A1; 국가 US; 발명자 Yun Sang Lee, Taeg Hwan Hyeon, Jae Min Jeong, Jae Sung Lee, Ji Yong Park, Kyu Wan Kim, Jae Hwan Shin, Guen Bae Ko, Whal Lee, Eun Ah Park)

## 소식

누리집 Gallery 페이지의 학회 참석 글이다.[^gallery]

- 2026-05 · 2026 KOSOMBE Spring Conference: In May 2026, our lab attended the Spring Conference of the Korean Society of Medical and Biological Engineering held in Jeju Island.

## 연락과 위치

- 교수실: N7-1동 2411호(누리집 Contact 「Bldg. N7-1 #2411」, 학과 교수진 「N7-1, 2411」)[^contact][^deptfac]
- 실험실: N7-1동 4413호(누리집 Contact 「Bldg. N7-1 #4413」)[^contact]
- 전화: +82-42-350-3817[^prof]
- 교수 이메일: guenbko@kaist.ac.kr[^contact][^deptlab]
- 주소: 291 Daehak-ro, Yuseong-gu, Daejeon, Korea[^contact]
[^p1]: S. Hyeon, S. Choi, G. B. Ko, M. S. Lee, Physics in Medicine & Biology 71, 165031 (온라인 2026-08-25). <https://doi.org/10.1088/1361-6560/ae97d1> 초록 기준.
[^p2]: G. B. Ko 외, J. S. Lee, Journal of Nuclear Medicine 67, 1329-1335 (온라인 2026-05-28). <https://doi.org/10.2967/jnumed.125.271172> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: D. Kim 외, C. Sung, Review of Scientific Instruments 97, 103504 (온라인 2026-10-01). <https://doi.org/10.1063/5.0347709> 초록 기준.
[^home]: 연구실 누리집 첫 화면 <https://merp.kaist.ac.kr/> (연구실 소개문, 2026-10-23 열람)
[^research]: 연구실 누리집 Research 페이지 <https://merp.kaist.ac.kr/research> (연구 네 갈래 소개문, 2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <https://merp.kaist.ac.kr/people/professor> (직위, 경력, 학력, 수상, 전화, 2026-10-23 열람)
[^members]: 연구실 누리집 Members 페이지 <https://merp.kaist.ac.kr/people/members> (구성원 카드, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Journals 페이지 <https://merp.kaist.ac.kr/publications/journals> (교수 개인 학술지 논문 목록 41편, 2026-10-23 열람)
[^patents]: 연구실 누리집 Patents 페이지 <https://merp.kaist.ac.kr/publications/patents> (교수 개인 특허 목록 18건, 2026-10-23 열람)
[^gallery]: 연구실 누리집 Gallery 페이지 <https://merp.kaist.ac.kr/gallery> (2026-10-23 열람)
[^contact]: 연구실 누리집 Contact 페이지 <https://merp.kaist.ac.kr/contact> (2026-10-23 열람)
[^deptlab]: KAIST 원자력및양자공학과 연구실 목록(방사선) <https://nuclear.kaist.ac.kr/research/the_lap.php?category=004> (연구실 이름, 직위, 학위, 이메일, 2026-10-23 열람)
[^deptfac]: KAIST 원자력및양자공학과 교수진 <https://nuclear.kaist.ac.kr/people/professor.php> (직위, 최종학위, 교수실, 2026-10-23 열람)

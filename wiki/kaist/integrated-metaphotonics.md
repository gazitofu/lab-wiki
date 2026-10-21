# KAIST 집적 메타포토닉스 그룹 (KAIST Integrated Metaphotonics Group, KIM Group)

**KAIST 전기및전자공학부 · 김상식 교수**

- 분야: 광집적회로(PIC, 빛으로 신호를 처리하는 칩), 서브파장 격자(빛의 파장보다 촘촘한 줄무늬 구조) 메타물질, 예외점(손실이 있는 광학계에서 나타나는 특이점) 광학, 마이크로 공진기와 광 주파수 빗, 칩과 외부 광학계를 잇는 빔 변환, AI 가속기·광 패키징용 광집적회로
- 대분야: 전기전자·반도체·광학
- 태그: 광집적회로[^research], 메타물질·메타광학[^p1][^p2][^p3], 비에르미트 광학[^p4][^p5], 광 주파수 빗[^research], 양자 계측·센싱[^research], 광 미세 공진기[^p6][^p7]
- 홈페이지: <https://kimgroup.kaist.ac.kr/>
- 근거와 출처: [KIM 그룹 근거 페이지](integrated-metaphotonics-sources.md)

> 부피 큰 광학 장치를 작은 칩 위의 광회로로 바꾸는 연구를 하는 그룹이다. 빛의 파장보다 촘촘한 줄무늬 구조로 이웃한 빛길 사이의 신호 섞임을 없애 칩을 더 빽빽하게 만들고, 칩 위에서 빛을 정밀하게 다루는 새 원리를 찾는다.[^research][^home]

## 무엇을 연구하나

그룹은 광학의 기초와 기술을 함께 다뤄 기초 과학과 미래 기술의 간극을 잇는 것을 목표로 하며, 부피 큰 광학 장치를 작고 튼튼하며 확장 가능한 칩 규모 광집적회로로 바꾸는 집적 나노포토닉스를 연구한다고 소개한다.[^research] 연구 페이지는 연구를 네 분야로 나눈다. 서브파장 격자·예외점·위상 광학으로 확장성·잡음·손실·제작 민감도 같은 기존 광집적회로의 한계를 넘는 소자 혁신, 공진기 분산 설계로 칩 위 광 주파수 빗과 비선형·양자 광학을 구현하는 분야, 칩을 원자·이온·미세유체 시스템과 결합하는 하이브리드 광집적회로(양자 센싱, 라이다), 그리고 AI 가속기와 광 패키징(CPO)을 위한 시스템 수준 광집적회로다.[^research]

첫 번째 갈래는 **서브파장 격자로 빛길을 촘촘하게**다. 칩 위의 빛길(도파로)을 가까이 붙이면 이웃 신호가 섞이는 누화가 생기는데, 서브파장 격자로 누화를 완전히 없애는 원리를 Light: Science & Applications에 발표했다.[^p1] 편광과 상관없이 동작하는 결합기,[^p2] 칩 면적을 적게 차지하는 광 지연선도 만들었다.[^p3]

두 번째 갈래는 **예외점 광학**이다. 손실이 있는 매질에서도 빛이 지수적으로 약해지지 않고 깊이 퍼지는 현상을 교수가 미국 국립표준기술연구소(NIST) 연구진과 함께 Nature Nanotechnology에 보고했고,[^p4][^news] 이를 표준 실리콘 광회로 구조에서 구현했다.[^p5]

세 번째 갈래는 **공진기와 빔 변환**이다. 질화규소 동심원 링 공진기의 분산을 설계하는 방법,[^p6] 버스 도파로를 두 개 둔 공진기로 공진 모양을 자유롭게 조절하는 구조,[^p7] 칩 밖 공간에서 빛을 작은 점으로 모으는 평면형 렌즈를 개발했다.[^p8]

## 주요 연구 주제

### 1. 서브파장 격자 메타포토닉스

누설 서브파장 격자 무누화, 편광 무관 결합기, 고밀도 광 지연선.[^p1][^p2][^p3] 대표 논문 1, 2, 3.

### 2. 예외점 광학

손실 매질의 다항식 파동 침투, 스트립 도파로 예외점.[^p4][^p5] 대표 논문 4, 5.

### 3. 공진기 분산 설계와 칩–외부 빔 변환

동심원 링 분산 설계, 이중 버스 공진기, 경사 굴절률 메타렌즈.[^p6][^p7][^p8] 대표 논문 6, 7, 8.

## 대표 논문

그룹 논문 목록의 2021–2026년 학술지 논문 가운데 교수가 마지막 저자인 것에서 주제별로 골랐다. 4는 교수의 NIST 박사후연구원 시기에 시작한 공동 연구로 교수가 공동 1저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2023 | [Anisotropic leaky-like perturbation with subwavelength gratings enables zero crosstalk](https://doi.org/10.1038/s41377-023-01184-5) · Light: Science & Applications | 빛이 밖으로 새는 누설 모드는 이웃 빛길과 강하게 결합해 촘촘한 집적에 나쁘다고 여겨졌다. 서브파장 격자 메타물질 안에서 진동하는 장이 방향별 결합을 서로 상쇄하게 해 누화를 완전히 0으로 만들 수 있음을 보였고, 실험에서 일반 도파로보다 누화를 약 40 dB(결합 길이 약 100배) 줄였다. 가두기 어려운 TM 편광(전기장이 칩 면에 수직으로 떨리는 빛)에서도 통했다.[^p1] | 1저자 Md Faiyaz Kabir, 마지막 저자 김상식 |
| 2 | 2026 | [Polarization-independent directional coupler using tilted subwavelength gratings](https://doi.org/10.1364/josab.612181) · Journal of the Optical Society of America B | 일반 방향성 결합기(나란히 놓인 두 빛길 사이로 빛을 옮기는 소자)는 도파로 모양 때문에 편광에 따라 결합 길이가 달라진다. 서브파장 격자를 비스듬히 기울여 두 편광의 유효 굴절률을 같게 만들고, 실리콘 칩에서 기울기 약 32°일 때 편광 차이가 거의 없는 결합기를 구현했다(1550 nm에서 삽입 손실(소자를 지나며 줄어드는 빛) 3 dB, 소광비(원하는 출력과 원치 않는 출력의 세기 비) 약 20 dB).[^p2] | 공동 1저자 Jihwan You·Dohun Koh, 마지막 저자 김상식 |
| 3 | 2023 | [High-density integrated delay line using extreme skin-depth subwavelength grating waveguides](https://doi.org/10.1364/ol.479003) · Optics Letters | 빛이 도착하는 시간을 늦추는 광 지연선은 보통 긴 나선형 도파로라 칩 면적을 mm²–cm²나 차지한다. 빛의 표면 침투 깊이를 조절한 서브파장 격자 도파로로 가까이 붙인 도파로 사이 누화를 억제해, 면적을 크게 아끼는 고밀도 지연선을 만들었다.[^p3] | 1저자 Ishtiaque Ahmed, 마지막 저자 김상식 |
| 4 | 2022 | [Exceptional points in lossy media lead to deep polynomial wave penetration with spatially uniform power loss](https://doi.org/10.1038/s41565-022-01114-3) · Nature Nanotechnology | 손실이 있는 매질에 들어간 빛은 보통 지수적으로 약해진다. 예외점을 가진 나노 구조 광 도파로에서는 지수 감쇠 없이 파장 400개 깊이까지 서서히 줄어들며 퍼지고 손실이 고르게 분포함을 이론과 실험으로 보였다. 칩 표면에서 크고 고른 평면파를 내보내는 데 쓸 수 있다.[^p4] | 공동 1저자 Alexander Yulaev·김상식, 마지막 저자 Vladimir A. Aksyuk |
| 5 | 2025 | [Exceptional points in a passive strip waveguide](https://doi.org/10.1515/nanoph-2024-0701) · Nanophotonics | 예외점을 널리 쓰이는 스트립 도파로에 구현했다. 도파로 한쪽에 2차 격자를 넣어 앞뒤로 가는 빛을 직접·간접으로 결합시키고, 예외점 파장에서 대칭인 투과 스펙트럼과 고른 방사 분포를 실험으로 확인했다.[^p5] | 1저자 Shamkhal Hasanli, 마지막 저자 김상식 |
| 6 | 2025 | [Modeling method for concentric ring resonators with dispersion engineering](https://doi.org/10.1364/oe.577296) · Optics Express | 동심원 링 공진기의 분산을 설계하는 방법을 제안했다. 단일 링 시뮬레이션으로 왕복 광경로 지도를 만들어 위상이 맞는 형상을 찾고, 두께 50 nm 질화규소 링에서 보통은 얻기 어려운 이상 분산을 얻어 솔리톤(모양을 유지하는 빛 펄스)이 가능함을 시뮬레이션으로 보였다.[^p6] | 1저자 Mehedi Hasan, 마지막 저자 김상식 |
| 7 | 2026 | [Dual-bus resonator for multi-port spectral engineering](https://doi.org/10.1002/lpor.202502935) · Laser & Photonics Reviews | 공진기와 버스 도파로 하나를 결합하면 임계 결합(공진기로 들어오는 빛과 잃는 빛이 맞먹는 상태), 투과가 0이 되는 조건, 최대 내부 세기가 함께 묶여 따로 조절할 수 없다. 버스를 두 개 둔 경주로형 공진기로 이 제약을 풀어 채널마다 다른 결합 상태와 공진 모양을 만들었고, 가시광부터 중적외선까지 넓게 동작함을 보였다.[^p7] | 1저자 Taewon Kim, 마지막 저자 김상식 |
| 8 | 2024 | [In-plane beam focusing via integrated photonic gradient-index subwavelength grating metalens](https://doi.org/10.1364/oe.539591) · Optics Express | 도파로의 빛을 넓게 편 뒤 2차원 굴절률 경사 서브파장 격자로 파면을 바꿔, 칩 끝에서 수백 µm 떨어진 곳에 작은 점으로 모으는 평면 렌즈를 설계했다. 가시광에 투명한 질화규소로 만들어 생화학 시료를 다루는 칩 응용에 쓸 수 있다.[^p8] | 1저자 Nafiz Jaidye, 마지막 저자 김상식 |

## 교수와 전문 분야

김상식 교수는 서울대 전기·컴퓨터공학 학사(2008)와 미국 퍼듀대 전기컴퓨터공학 석사(2014)·박사(2015)를 받았다. 퍼듀대(2016)와 미국 국립표준기술연구소(NIST, 2017) 박사후연구원, 텍사스공대 전기컴퓨터공학과 조교수(2017–2022)를 거쳐 2022년부터 KAIST 전기및전자공학부 부교수이며 양자대학원과 반도체시스템공학과에도 소속돼 있다.[^members] 그룹 소식에 따르면 2022년 미국 국립과학재단(NSF) CAREER Award, 2021년 재미한인과학기술자협회 KSEA Young Investigator Grant를 받았고, 2026년 Introduction to Integrated Photonics(EE40042) 강의로 Best Teaching Award를 받았다.[^home]

논문으로 보면 전문 분야는 세 갈래다.

- **서브파장 격자 메타물질 광소자**.[^p1][^p2][^p3]
- **비에르미트(예외점) 광학**.[^p4][^p5]
- **공진기 분산 설계와 칩–자유공간 빔 변환**.[^p6][^p7][^p8]

## 응용 분야

대표 논문과 연구 소개로 보면 고밀도 광통신·광연결 칩, 광 주파수 빗과 양자 광원, 원자 기반 양자 센서, 칩 규모 라이다, AI 가속용 광집적회로에 닿아 있다.[^research][^p1][^p7] 졸업생은 인텔, 노키아, 루멘텀 등 광통신·반도체 기업과 해외 대학원으로 갔다고 그룹이 적는다.[^members]

## 구성원

2026년 10월 19일 그룹 구성원 페이지 기준이다. "시작"은 그룹이 적은 과정과 입학 연도(두 자리)다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Jaewhan Lee | 석박사통합과정 | MS/PhD 23 | jaewhan.lee@kaist.ac.kr | 8 |
| Kyungtae Kim | 석박사통합과정 | MS/PhD 23 | alex5093@kaist.ac.kr |  |
| Hyejin Yoon | 석박사통합과정 | MS/PhD 24 | ktrnyoon@kaist.ac.kr | 5 |
| Seungyong Lee | 석박사통합과정 | MS/PhD 24 | russ44@kaist.ac.kr | 2, 5 |
| Jongeon Lim | 석박사통합과정 | MS/PhD 24 | jongeon03@kaist.ac.kr |  |
| Jihwan You | 석박사통합과정 | MS/PhD 24 | jihwanyou@kaist.ac.kr | 2 |
| Yongsik Shin | 석박사통합과정 | MS/PhD 25 | ypooh2062@kaist.ac.kr |  |
| Junyeol Choi | 석박사통합과정 | MS/PhD 25 | junyeol@kaist.ac.kr |  |
| Jun Wang | 박사과정 | PhD 25 | junwang@kaist.ac.kr |  |
| Yunjeong Kim | 석박사통합과정 | MS/PhD 25 | yunjeong.kim@kaist.ac.kr |  |
| Yosep Shin | 박사과정 | MS 24, PhD 26 | josephshin@kaist.ac.kr |  |
| Jaeu Bae | 박사과정 | MS 24, PhD 26 | jaeu.bae@kaist.ac.kr |  |
| Seungyup Baek | 박사과정 | MS 24, PhD 26 | backsy@kaist.ac.kr | 6 |
| Jibaek Song | 석사과정 | MS 25 | burningbin2@kaist.ac.kr |  |
| Minseop Lee | 석사과정 | MS 25 | 2002lms@kaist.ac.kr | 2 |
| Soomin Kang | 석사과정 | MS 26 | soosoo02@kaist.ac.kr |  |
| Jungmyeong Kim | 석사과정 | MS 26 | jungmyeong@kaist.ac.kr |  |
| Pornananrat Napol | 석사과정 | MS 26 | engnapol@kaist.ac.kr |  |
| Dogyung Yoon | 석사과정 | MS 26 | dean010707@kaist.ac.kr |  |
| 선하은 | 학부 연구생 |  | haeon703@kaist.ac.kr |  |
| 전채훈 | 학부 연구생 |  | jeonchaehun@kaist.ac.kr |  |
| 이태강 | 학부 연구생 |  | taekang@kaist.ac.kr |  |

## 졸업생과 이전 구성원

그룹 구성원 페이지의 졸업 대학원생·박사후연구원과 방문 연구자, 그룹이 적은 다음 진로다. 텍사스공대(TTU) 시기 졸업생을 포함한다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Yeolheon Seong | 박사후연구원 (2026) | Samsung |
| Juntae Kim | 석사 (KAIST EE) (2026) |  |
| Peiyuan Li | 석사 (KAIST EE) (2026) |  |
| Lanxuan Zhang | 박사후연구원 (2025) | AMF |
| Mehedi Hasan | 박사 (TTU ECE) (2025) | Nokia (Senior PIC Development Engineer) |
| Shamkhal Hasanli | 석사 (KAIST EE) (2025) | DTU (PhD program, H. Hu group) |
| Nafiz Jaidye | 박사 (TTU PHYS) (2024) | Intel (Test Engineer) |
| Syed Z. Ahmed | 박사 (TTU ECE) (2023) | Intel (Test Engineer) |
| Daniel Pimbi | 석사 (TTU ECE) (2023) | University of Maryland (PhD program, K. Srinivasan Group) |
| Ishtiaque Ahmed | 박사 (TTU PHYS) (2022) | Intel (Process Engineer) |
| Md Borhan Mia | 박사 (TTU ECE) (2022) | Lumentum → OpenLight |
| Saleha Fatema | 석사 (TTU ECE) (2020) | Purdue University (PhD, A. Weiner group) → NIST (Postdoc) |
| Jing Wang | 방문 연구자 (EE, 2023 Fall - 2025 Summer) |  |

## 최근 논문 목록 (2021–2026)

그룹 논문 목록의 2021–2026년 학술지 논문 23편이다(해설 기사 1편 포함). 사전 공개 3편과 학술대회 발표 목록은 같은 페이지에 따로 있다.[^papers]

**2026**

- Jihwan You\*, Dohun Koh\*, Seungyong Lee, Minseop Lee, Hoon Kim, and Sangsik Kim. "Polarization-independent directional coupler using tilted subwavelength gratings". *Journal of the Optical Society of America B 43(11), 2537-2542 (\*equal contribution)*.
- Peiyuan Li, Yosep Shin, and Sangsik Kim. "Zero crosstalk in asymmetric multimode waveguides for higher-order mode crosstalk suppression via subwavelength gratings". *Optics Express 34(15), 28549-28561*.
- Jaewhan Lee, H. Lee, W. Lee, H. Kim, D. Kwon, S. Lee, M. Seo, T. Kwon, S. Seo, H. Hong, S. Kang, S. Park, Y. Park, J. Park, Y. Na, I. Kang, Sangsik Kim, and J. Lee. "Strontium 1S0 → 1P1 transition frequency measurements assisted by a photonic grating chip". *Metrologia 63, 045003*.
- Jaeu Bae, J. Kim, Sangsik Kim, and M. Song. "Closed-Loop Adaptive Pulse Shaping for Flat-Top Electro-Optic Supercontinuum Generation". *IEEE Journal of Lightwave Technology*.
- Taewon Kim, Mehedi Hasan, Y. Choi, J. Yoon, and Sangsik Kim. "Dual-bus resonator for multi-port spectral engineering". *Laser & Photonics Reviews e02935 (Cover Image)*.

**2025**

- Mehedi Hasan, Seungyup Baek, A. Bernussi, and Sangsik Kim. "Modeling method for concentric ring resonators with dispersion engineering". *Optics Express 33(24), 51499-51512*.
- Lanxuan Zhang, Q. Xie, Q. Na, D. Zhuang, X. Nie, L. Wang, Sangsik Kim, J. Song, and L. Wang. "Time-lens-based optical phased array LiDAR for ranging and accuracy enhancement". *APL Photonics 10(11), 116102*.
- Yosep Shin, Kyungtae Kim, Jaewhan Lee, Saman Jahani, Zubin Jacob, and Sangsik Kim. "Anisotropic metamaterials for scalable photonic integrated circuits: a review on subwavelength gratings for high-density integration". *Nanophotonics 14(9), 1311-1331*.
- Shamkhal Hasanli, Mehedi Hasan, Hyejin Yoon, Seungyong Lee, and Sangsik Kim. "Exceptional points in a passive strip waveguide". *Nanophotonics 14(8), 1301-1309*.

**2024**

- Nafiz Jaidye, Jaewhan Lee, Daniel Pimbi, Myoung-Hwan Kim, Ayrton Bernussi, and Sangsik Kim. "In-plane beam focusing via integrated photonic gradient-index subwavelength grating metalens". *Optics Express 32, 46225-46238*.
- S. Ahmed, M. Hasan, K. Kim, and S. Kim. "Zero-crosstalk silicon photonic refractive index sensor with subwavelength gratings". *Nano Convergence 11, 39*.
- G. Kim, H. Kim, Y. Jeon , I. Kim, S. Kim, S. Kim, J. Kim. "Scalable hot carrier–assisted silicon photodetector array based on ultrathin gold film". *Nanophotonics 13(7), 1049*.
- D. Pimbi, M. Mia, N. Jaidye, I. Ahmed, M. Hasan, S. Ahmed, and S. Kim. "Integrated polarization-free Bragg filters with subwavelength gratings for photonic sensing". *Optics Express 32(2), 2147-2161*.

**2023**

- S. Kim. "Silicon photonic Bessel–Gaussian beam generation unlocks new possibilities for long-range sensing". *Light: Science & Applications, 12, 141 (2023) (News & Views)*.
- M. Kabir, M. Mia, I. Ahmed, N. Jaidye, S. Ahmed, and S. Kim. "Anisotropic leaky-like perturbation with subwavelength gratings enables zero crosstalk". *Light: Science & Applications, 12, 135*.
- I. Ahmed, S. Ahmed, N. Jaidye, M. Mia, A. Bernussi, and S. Kim. "High-density integrated delay line using extreme skin-depth subwavelength grating waveguides". *Optics Letters 48(7), 1662-1665*.
- D. Pimbi, M. Hasan, M. Mia, N. Jaidye, and S. Kim. "Polarization-independent photonic Bragg grating filter with cladding asymmetry". *Optics Letters 48(5), 1192-1195*.
- M. Mia, N. Jaidye, I. Ahmed, S. Ahmed, and S. Kim. "Broadband integrated polarization splitter and rotator using subwavelength grating claddings". *Optics Express 31(3), 4140-4151*.

**2022**

- S. Kachiraju, I. Nekrashevich, I. Ahmed, H. Farooq, L. Chang, S. Kim, and M. Kim. "Coupled surface plasmon-phonon polariton nanocavity arrays for enhanced mid-infrared absorption". *Nanophotonics 11(2), 4489-4498*.
- A. Yulaev\*, S. Kim\*, Q. Li, D.A. Westly, B.J. Roxworthy, K. Srinivasan, and V. Aksyuk (\*equal contribution). "Exceptional points in lossy media lead to deep polynomial wave penetration with spatially uniform power loss". *Nature Nanotechnology 17, 583-589*.

**2021**

- M. Mia, S. Ahmed, N. Jaidye, I. Ahmed, and S. Kim. "Mode-evolution-based ultra-broadband polarization beam splitter using adiabatically tapered extreme skin-depth waveguide". *Optics Letters 46(18), 4490-4493*.
- S. Ahmed, I. Ahmed, M. Mia, N. Jaidye, and S. Kim. "Ultra-high extinction ratio polarization beam splitter with extreme skin-depth waveguide". *Optics Letters 46(9), 2164-2167*.
- S. Fatema, M. Mia, and S. Kim. "Multiple mode couplings in a waveguide array for broadband near-zero dispersion and supercontinuum generation". *IEEE Journal of Lightwave Technology 39, 216-222*.

## 특허

그룹 논문 목록의 특허 구간이다.[^papers]

- Rib waveguide with optical crosstalk eliminated (발명자 S. Kim, K. Kim, and Y. Shin; 번호 Korea Patent Application No. 10-2025-0062908 (filed in 2025))
- Plugable atomic-optical integrated circuit device (발명자 S. Kim, K. Yu, J. Lee, J. Lee, D. Yu, and H. Hong; 번호 Korea Patent Application No. 10-2025-0138712 (filed in 2025))
- Waveguides having highly suppressed crosstalk (발명자 S. Kim and M. Mia; 번호 U.S. Patent No. US11709316B2 (2023))
- Optical Coupler (발명자 M. Teng, M. Qi, B. Niu, J.C. Wirth, S. Kim, K. Han, Y. Xuan, and Y. Lee; 번호 U.S. Patent No. 10,197,731 (2019))
- Optical Coupler having segmented waveguides for coupling electromagnetic field (발명자 M. Qi, M. Teng, K. Han, S. Kim, B. Niu, and Y. Lee; 번호 U.S. Patent No. 10,444,434 (2019))
- Optical Coupler having exposed subwavelength gratings for coupling electromagnetic field (발명자 M. Qi, M. Teng, K. Han, S. Kim, B. Niu, and Y. Lee; 번호 U.S. Patent No. 10,126,500 (2018))

## 소식

그룹 첫 화면의 그룹 소식과 주요 소식이다.[^home]

- 2026-09-24 · Jihwan and Dohun’s paper, “Polarization-Independent Directional Coupler Using Tilted Subwavelength Gratings,” has been published in the Journal of the Optical Society of America B! Congratulations!
- 2026-07-24 · Peiyuan’s paper on “Zero crosstalk in asymmetric multimode waveguides for higher-order mode crosstalk suppression via subwavelength gratings” is published on Optics Express. Congratulations!
- 2026-07-17 · Jaewhan’s paper on “Strontium 1S0 → 1P1 transition frequency measurements assisted by a photonic grating chip” is published in Metrologia. Congratulations!
- 2026-07-14 · Jaeu’s paper on “Closed-Loop Adaptive Pulse Shaping for Flat-Top Electro-Optic Supercontinuum Generation” is published on Journal of Lightwave Technology. Congratulations!
- 2026-06-17 · Jibaek and Jongeon presented their research at ECIO 2026 at ETH Zurich! Great job!
- 2026-06-12 · Congratulations to Seungyup and Juntae on successfully defending their M.S. theses!
- 2026-05-15 · Dr. Yeolheon Seong joined our group as an InnoCORE postdoc! Welcome!
- 2026-03-30 · Sangsik and Minsup received the Best Teaching and Best TA Awards
- 2026-03-07 · Taewon’s paper (our URP undergraduate) on “Dual-Bus Resonator for Multi-Port Spectral Engineering” is published on Laser & Photonics Reviews! Congratulations!
- 2026-03-03 · Member updates: Yunjeong & Dokyung joined our group – welcome! Yoseph and Jaewoo move to PhD program, and Soomin, Jungmyeong, and Napol started their MS journey. Good luck to everyone on the next steps!
- 2026-02-20 · Six members graduated! (MS: Yoseph, Jaewoo, Peiyuan & BS: Soomin, Jungmyeong, Napol) Congratulations on your achievement. It’s a big milestone in your career!
- 2026-01-11 · KIM Group 2025 Recap
- 2025-12-01 · Mehedi successfully defended his PhD! He will be joining Nokia as a Senior PIC Development Engineer. With Nokia’s acquisition of Infinera earlier this year, this is an exciting time to be joining the team. Congratulations, Mehedi! Wishing you all the best in your next steps.
- 2025-11-27 · Mehedi’s paper on “Modeling method for concentric ring resonators with dispersion engineering” is published in Optics Express. Congratulations!
- 2025-11-05 · Lanxuan’s paper on “Time-lens-based optical phased array LiDAR for ranging and accuracy enhancement” is published in APL Photonics journal. Congratulations!
- 2025-09-10 · New Members! 🎉 Welcome Junyeol (MS/PhD), Jun Wang (PhD), Jungmyeong, Napol, Haeun, and Chaehun (Undergraduates)!
- 2025-07-04 · Sangsik, Jibaek, and Soomin presented our research at the OECC 2025 conference!
- 2025-06-18 · Taewon, our undergraduate URP student, recieved two poster awards! One from the 1st Optical Science & Opto-Semiconductor Workshop (OSW) and the other from the KAIST Optics Group students poster competetion. Good job!
- 2025-06-05 · Shamkhal successfully defended his MS thesis on “A Study on Exceptional Points in Passive Integrated Photonic Strip Waveguides”. He will move to DTU for his PhD journey. Good luck!
- 2025-03-30 · A Review paper by Yoseph Shin titled “Anisotropic Metamaterials for Scalable Photonic Integrated Circuits: A Review on Subwavelength Gratings for High-Density Integration” has been published in Nanophotonics journal.
- 2023-06-02 · Our paper on “Anisotropic leaky-like perturbation with subwavelength gratings enables zero crosstalk” is published in Light: Science & Applications. Congratulations!
- 2022-08-29 · Our group is moving to KAIST in South Korea. We have openings for postdoc, Ph.D., MS, and undergraduate positions.
- 2022-04-21 · Sangsik’s paper on “Exceptional points in lossy media lead to deep polynomial wave penetration with spatially uniform power loss” was published in Nature Nanotechnology!
- 2022-01-13 · Sangsik has been awarded the National Science Foundation (NSF) CAREER Award for 2022! We are excited to tackle the scaling issues inherent to integrated nanophotonics and apply subwavelength gratings for diverse photonic applications. Congratulations!
- 2021-02-09 · Sangsik has been selected as a recipient of the 2021 KSEA (Korean-American Scientists and Engineers Association) Young Investigator Grant! Congratulations!

## 연락과 위치

- 교수 이메일: sangsik.kim@kaist.ac.kr, 전화 042-350-7472[^contact]
- 위치: KAIST 정보전자공학동(E3-2) 3209호 (대전 유성구 대학로 291)[^contact]

[^home]: KAIST Integrated Metaphotonics Group 누리집 첫 화면(Highlights, Group News) <https://kimgroup.kaist.ac.kr/> (2026-10-19 열람)
[^research]: KIM 그룹 연구 페이지 <https://kimgroup.kaist.ac.kr/research/> (2026-10-19 열람)
[^members]: KIM 그룹 구성원 페이지 <https://kimgroup.kaist.ac.kr/members/> (2026-10-19 열람)
[^papers]: KIM 그룹 논문 목록 <https://kimgroup.kaist.ac.kr/publications/> (2026-10-19 열람)
[^contact]: KIM 그룹 연락처 <https://kimgroup.kaist.ac.kr/contact/> (2026-10-19 열람)
[^news]: KIM 그룹 소식 "Sangsik's paper on Exceptional points in lossy media ... was published in Nature Nanotechnology"(2022-04-21) <https://kimgroup.kaist.ac.kr/2022/04/21/sangsiks-paper-on-exceptional-points-in-lossy-media-lead-to-deep-polynomial-wave-penetration-with-spatially-uniform-power-loss-was-published-in-nature-nanotechnology/> (2026-10-19 열람)
[^p1]: M. F. Kabir 외, S. Kim, Light: Science & Applications 12, 135 (온라인 2023-06-02). <https://doi.org/10.1038/s41377-023-01184-5> 초록 기준.
[^p2]: J. You 외, S. Kim, Journal of the Optical Society of America B 43, 2537 (온라인 2026-10-01). <https://doi.org/10.1364/josab.612181> 초록 기준.
[^p3]: I. Ahmed 외, S. Kim, Optics Letters 48, 1662 (온라인 2023-03-22). <https://doi.org/10.1364/ol.479003> 초록 기준.
[^p4]: A. Yulaev 외, V. A. Aksyuk, Nature Nanotechnology 17, 583-589 (온라인 2022-04-21). <https://doi.org/10.1038/s41565-022-01114-3> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: S. Hasanli 외, S. Kim, Nanophotonics 14, 1301-1309 (온라인 2025-03-11). <https://doi.org/10.1515/nanoph-2024-0701> 초록 기준.
[^p6]: M. Hasan, S. Baek, A. Bernussi, S. Kim, Optics Express 33, 51499 (온라인 2025-11-26). <https://doi.org/10.1364/oe.577296> 초록 기준.
[^p7]: T. Kim 외, S. Kim, Laser & Photonics Reviews 20, e02935 (온라인 2026-03-06). <https://doi.org/10.1002/lpor.202502935> 초록 기준.
[^p8]: N. Jaidye 외, S. Kim, Optics Express 32, 46225 (온라인 2024-12-06). <https://doi.org/10.1364/oe.539591> 초록 기준.

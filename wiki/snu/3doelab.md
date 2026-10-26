# 3차원 광공학 연구실 (Three-Dimensional Optical Engineering Laboratory, 3DOELAB)

**서울대학교 공과대학 전기·정보공학부 · 박재형 교수**

- 분야: 가상·증강현실 디스플레이 광학, 홀로그래픽·라이트필드 입체영상, 광정보 처리와 영상 복원
- 대분야: 전기전자·반도체·광학
- 태그: 가상·증강현실[^home][^p2], 광학 영상·현미경[^heritage], 문화유산·예술 기술[^heritage]
- 홈페이지: <https://sites.google.com/view/3doelab>
- 근거와 출처: [3차원 광공학 연구실 근거 페이지](3doelab-sources.md)

> 눈앞에 입체 영상을 보여 주는 디스플레이의 광학 구조와 영상 계산법을 연구하며, 가상 물체의 깊이·가려짐·색을 다루고 빛으로 얻은 정보를 입체 형상으로 복원하는 연구실이다.[^home][^p2][^p8][^heritage]

## 무엇을 연구하나

연구실은 서울대학교 전기·정보공학부 박재형 교수가 이끈다. 학과는 연구 분야를 광공학과 가상·증강현실 디스플레이로 소개한다.[^dept][^prof] 증강현실(AR, Augmented Reality)은 실제 환경에 가상 정보를 겹쳐 보여 주는 기술이고, 가상현실(VR, Virtual Reality)은 컴퓨터가 만든 환경을 경험하게 하는 기술이다. 연구실은 특히 눈 가까이에서 영상을 보여 주는 근안 디스플레이의 광학 설계를 다룬다.[^home]

한 갈래는 눈이 받아들이는 깊이 정보를 다루는 일이다. 라이트필드(공간의 위치와 방향에 따른 빛의 분포)를 재현하거나, 여러 깊이에 영상면을 만들거나, 눈에 들어가는 빛의 경로를 조절한다. 이를 통해 시점을 옮겼을 때 보이는 모습과 눈의 초점 조절이 함께 입체감을 전달하도록 연구한다.[^home][^p3][^p4] 서로 다른 깊이에 초점을 맞출 수 있는 표시계와, 여러 방향에서 본 영상을 제공하는 표시계를 광학 소자와 영상 계산으로 구현한다.[^p3][^p4][^p5]

다른 갈래는 홀로그래피(빛의 세기와 위상 정보를 기록·재생하는 기술)다. 위상은 파동의 반복 과정에서 어느 지점에 있는지를 나타낸다. 연구실은 홀로그래픽 디스플레이의 영상 생성 계산법, 계산 가속과 전용 하드웨어, 사람이 느끼는 영상 품질을 다룬다.[^home] 가상 영상이 실제 배경을 가리는 폐색 효과를 광학적으로 구현하고, 레이저로 재생한 영상의 색이 사람이 보는 색과 맞도록 색을 관리하는 방법을 제안했다.[^p2][^p8]

빛으로 물체의 정보를 얻어 복원하는 연구도 한다. 문화유산 과제에서는 디지털 홀로그래픽 현미경(홀로그램을 수치 계산해 물체 정보를 복원하는 현미경)과 타이코그래피 현미경(겹치는 영역의 빛 무늬를 계산해 물체 정보를 복원하는 현미경)으로 얻은 표면 반사광을 이용한다. 반사광의 진폭(파동이 기준 상태에서 벗어나는 최대 크기)과 위상 분포로부터 문화재 표면의 입체 형상을 재구성하는 기술을 개발한다.[^heritage]

## 주요 연구 주제

### 눈의 초점과 입체 표시 광학

수렴·초점 불일치(VAC, Vergence-Accommodation Conflict)는 두 눈이 바라보는 깊이와 눈이 초점을 맞추는 깊이가 어긋나는 현상이다. 연구실은 이를 다루기 위해 가변 초점, 다초점, 라이트필드와 맥스웰리언 표시 방식을 연구한다.[^home][^p1][^p3] 맥스웰리언 표시는 빛을 눈의 동공 부근에 모아 망막에 영상을 투사하는 방식이다. 홀로그래픽 광학 소자(HOE, Holographic Optical Element, 기록한 빛 무늬로 빛의 진행을 바꾸는 소자)를 화면에 붙여 광원 배열을 재생하는 박형 가상현실 표시계를 제안했다.[^p1]

### 현실과 가상 영상의 가려짐

실제 환경을 투과해 보는 증강현실에서는 가상 영상과 배경의 빛이 함께 눈에 들어온다. 연구실은 실제 장면의 지정 영역을 가리는 마스크와 홀로그래픽 영상의 잡음 성분을 거르는 기능을 같은 광학계에서 시간에 따라 번갈아 작동시키는 구조를 제안했다. 이 구조로 불투명하게 보이는 가상 입체 영상과 가상 물체의 그림자를 표시했다.[^p2]

### 다중 시점과 공중 입체영상

운동시차(관찰 위치가 달라질 때 물체의 상대적인 위치가 달라 보이는 현상)와 눈의 초점 단서를 함께 제공하는 다중 시점·다초점 표시계를 연구한다.[^p4] 집적영상(여러 방향의 요소 영상을 광학적으로 결합하는 입체영상 방식) 표시계 둘을 거울 배열과 결합해 입체 영상의 깊이 범위를 확장하는 방법도 제안했다.[^p5] 거울 배열과 빛을 내는 소자, 디지털 미세거울 소자(DMD, Digital Micromirror Device, 미세거울의 방향을 바꾸어 빛을 조절하는 소자)를 결합해 공중에 떠 보이는 영상의 시점을 만드는 연구도 한다.[^p6]

### 홀로그래픽 영상의 색과 품질

홀로그래픽 도파관(빛을 내부에서 안내하는 구조)의 색 균일도와 시야각(영상이 보이는 각도 범위)을 함께 다루는 광학 설계를 연구했다.[^p7] 또 색 공간 변환(색을 수치로 표현하는 좌표 체계 사이의 변환), 조명 제어, 신경망(연결된 계산 단위의 관계를 자료로 학습하는 계산 모형)을 결합해 홀로그래픽 표시계의 입력 색과 사람이 느끼는 출력 색을 맞추는 방법을 제안했다.[^p8]

## 대표 논문

근안 표시계의 초점, 현실과 가상 영상의 폐색, 공중 입체영상, 색 재현을 고르게 보여 주는 8편을 골랐다. 박재형 교수가 저자이며 서울대 소속이 확인되는 2024–2026년 논문이다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 8번은 ACM Transactions on Graphics 게재 승인을 밝힌 arXiv 사전 공개본이다.[^p8]

| 번호 | 연도 | 논문 | 쉽게 말하면 | 박재형 교수 역할 |
|---|---|---|---|---|
| 1 | 2026 | Thin Maxwellian Virtual Reality Near-Eye Display Using Holographic Optical Element and Mini-Fresnel Lens Array · Journal of the Society for Information Display | 화면에 직접 붙인 홀로그래픽 광학 소자로 가상의 점광원 배열을 재생했다. 별도의 광원 모듈 사이 간격을 없애 광학 구조의 두께를 줄이면서 눈의 초점 변화에 따른 영상 선명도를 유지하는 맥스웰리언 표시계를 제안하고, 투과형과 반사형 구성을 실험했다.[^p1] | 교신저자 |
| 2 | 2025 | Enhancing Realism in Holographic Augmented Reality Displays Through Occlusion Handling · Laser & Photonics Reviews | 현실의 지정 영역을 가리는 광학계를 홀로그래픽 증강현실 표시계에 결합했다. 디지털 미세거울 소자를 실제 배경 마스크와 잡음 필터로 번갈아 사용해, 배경이 비쳐 보이는 가상 영상을 불투명하게 보이도록 하고 그림자도 표시했다.[^p2] | 교신저자 |
| 3 | 2025 | Multifocal near-eye display with a vari-focal lens and adjustable aperture · Optics Express | 여러 깊이에 영상을 보여 줄 때 각 영상면에서 선명하게 보이는 깊이 범위를 조절하는 방법이다. 빛을 통과시키는 구멍인 조리개의 크기를 공간적으로 빛을 조절하는 소자로 바꾸어, 영상면의 수와 깊이 범위 문제를 다루고 광학 실험과 분석으로 확인했다.[^p3] | 교신저자 |
| 4 | 2025 | Multi-view multi-focal 3D display using light source array and focus tunable optics · Optics Express | 여러 시점의 생성과 초점을 바꾸는 렌즈를 결합했다. 관찰 위치를 옮길 때 모습이 달라지는 운동시차와 눈의 초점 단서를 한 시스템에서 함께 제공했으며, 실험으로 원래 해상도(영상의 세부를 구분해 나타내는 능력)의 영상 표시와 소형 구성의 가능성을 보였다.[^p4] | 교신저자 |
| 5 | 2025 | Integral imaging 3D display with enhanced depth range using slit mirror array and dual display systems · Journal of Optics | 집적영상 표시계 둘을 투과형 재귀반사체와 빛을 나누는 소자로 결합했다. 한 표시계의 입체 영상을 공중에 만들면서 다른 표시계의 영상을 여러 깊이에서 합쳐, 입체 영상의 깊이 범위를 확장하는 방법을 제안했다.[^p5] | 교신저자 |
| 6 | 2024 | Time multiplexing multi-view display using slit mirror array and light emitting diode illuminated digital micromirror device · Journal of Information Display | 투과형 거울 배열과 디지털 미세거울 소자로 안경 없이 보는 공중 다중 시점 표시계를 만들었다. 빛을 내는 소자들의 상을 여러 시점으로 사용하고, 광원 5개로 각 시점의 영상을 표시해 제안한 구조를 확인했다.[^p6] | 교신저자 |
| 7 | 2025 | Improved color uniformity in monochrome holographic waveguide based near eye displays · Optics Express | 홀로그래픽 격자를 이용하는 도파관에서 시야각에 따라 색이 달라지는 문제를 다뤘다. 서로 다른 입사각에서 빛을 일정하게 전달하도록 격자를 중첩하는 구조를 설계하고, 계산과 광학 실험으로 시야각과 색 균일도의 개선을 확인했다.[^p7] | 중간 저자 |
| 8 | 2026 | PAColorHolo: A Perceptually-Aware Color Management Framework for Holographic Displays · arXiv 사전 공개본 | 레이저, 빛 조절 소자, 광학계와 카메라가 만드는 색 왜곡을 함께 다루는 색 관리 방법을 제안했다. 색 공간 변환, 조명 제어와 카메라의 색 반응을 다루는 신경망을 결합하고, 계산·광학 실험과 사용자 연구로 사람이 느끼는 색 재현의 개선을 확인했다.[^p8] | 마지막 저자 |

## 교수와 전문 분야

학과 전임교수 소개는 박재형의 직위를 교수로, 전문 분야를 홀로그래피, 가상·증강현실 디스플레이, 입체영상과 광공학으로 적는다.[^prof] 2024년 논문의 저자 소개에 따르면 서울대학교에서 2000년 학사, 2002년 석사, 2005년 박사 학위를 받았고, 삼성전자와 충북대학교, 인하대학교를 거쳐 2024년 서울대학교에 부임했다. 당시 저자 소개의 직위는 부교수다.[^bio]

현재 전문 분야는 입체 정보를 획득·처리·표시하는 광학과 눈 가까이에서 사용하는 표시계의 설계다.[^people][^bio] 대표 논문으로 보면 눈의 초점과 영상 깊이를 조절하는 광학계,[^p1][^p3][^p4] 현실 빛의 차단과 홀로그래픽 영상 생성을 결합하는 구조,[^p2] 다중 시점·공중 입체 표시,[^p5][^p6] 색 재현을 위한 광학 설계와 계산 방법을 다룬다.[^p7][^p8]

## 응용 분야

가상현실·증강현실 안경의 근안 디스플레이, 라이트필드 영상 서비스, 홀로그램 영상 서비스가 주요 응용이다.[^home] 문화유산 과제에서는 문화재 표면의 형상과 색감·질감을 비접촉으로 측정·복원하는 기술을 개발하며, 연구실은 측정한 빛 정보로부터 입체 형상을 재구성하는 부분을 담당한다.[^heritage]

## 구성원

2026년 10월 26일 People 페이지의 박사후연구원 3명, 박사과정 3명, 석박사통합과정 7명, 석사과정 1명, 인턴 1명이다. 연구 주제와 과정은 누리집 카드 표기다. ‘대표 논문 참여’는 위 표의 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Sahar Kheibarihafshejani | 박사후연구원 | Design  of Stereoscopic\Autostereoscopic 3D Displays; Computational Design of Holographic and Light Field Display | saharkheibari@snu.ac.kr | 4, 5, 6 |
| Chun Chen | 박사후연구원 | Computational Holographic Display; 3D Display; Visual Perception | chenchun@snu.ac.kr | 8 |
| Jaehong Lee | 박사후연구원 | Fast high-quality hologram generation; Ultra-high-resolution hologram processing | leejaehong@snu.ac.kr |  |
| Woongseob Han | 박사과정 | Optical design for AR/VR Near-Eye Displays; Three-dimensional optics including light field and holography; Occlusion optics | dndtjq89@snu.ac.kr | 2, 3 |
| Jiyun Han | 박사과정 | AR/VR Near-eye displays; Three-Dimensional displays; Signal optimization via learning-based methods | hzyunc@snu.ac.kr |  |
| Jungyeop Shin | 박사과정 | AR/VR Near-eye displays; Three-Dimensional displays (light field, holograp hy) | edison29@snu.ac.kr |  |
| Minseong Kim | 석박사통합과정 | AR/VR near-eye displays; Three-dimensional displays (light field, holography); Optical design |  | 1, 8 |
| Gyu-Chan Han | 석박사통합과정 | Light field; Vari-focal optics; AR/VR near-eye displays | hangc111@snu.ac.kr | 3 |
| Chanseul Lee | 석박사통합과정 | AR/VR near-eye displays; Three dimensional displays | lcs8913@snu.ac.kr | 2 |
| Minjae Shin | 석박사통합과정 | Three dimensional displays; Volumetric displays | p4r4dox82@snu.ac.kr |  |
| Jae-Woo Baek | 석박사통합과정 | Volumetric displays; Three dimensional displays; Acoustic levitation | earth1320@snu.ac.kr |  |
| Chee-Hyeok Song | 석박사통합과정 | Optical design for AR/VR Near-Eye Displays; Three dimensional displays; Metasurface for AR/VR displays | chsongg@snu.ac.kr |  |
| Jun-Yeong Goo | 석박사통합과정 | AR/VR near-eye displays; Three dimensional displays; Real-Time Computational Generated Holography | ycos3322@snu.ac.kr |  |
| Hyun-jun An | 석사과정 | Applied Optics; Projection Display Systems; Optical Diffusers and Films; Automotive HMI | anhyunjun@snu.ac.kr |  |
| SeEun Bae | 인턴 | AR/VR near-eye displays; Three dimensional displays; Visual Perception |  |  |

## 졸업생과 이전 구성원

People의 Alumni 구획에 게시된 29명이다. 인하대학교 등 박재형 교수의 서울대 부임 전 소속 시절 구성원도 포함하는 목록이며, 항목별 졸업 연도는 적혀 있지 않다. Ph.D.가 붙은 사람만 박사로 표시하고, 나머지 학위·과정과 비어 있는 진로는 보태지 않았다.[^people][^bio]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hyun-Eui Kim |  | ETRI(한국전자통신연구원) |
| Hee-Seung Kim |  | Ph.D. program at University of Connecticut |
| Kyeong-Min Jeong |  | LS산전 |
| Sung-In Hong |  | 캐논 비지니스 솔루션 |
| Yong-Soo Kim |  | 한교아이씨 |
| Na-Young Jo |  | LG전자 |
| Hong-Gi Lim |  | LG이노텍 |
| Sung-Keun Lee |  | LG전자 |
| Hee-Jae Kim |  |  |
| BoNi Li |  |  |
| Han-Ju Yeom |  | 한국전자통신연구원(ETRI) |
| Yeong-Min Ji |  | LG Display |
| HuiJun Zhang |  | Canon Optical Industrial Equipment (ShangHai) Inc. |
| Seok-Bum Ko |  | SK Magic |
| Sang-Hoo Kim |  | Hitachi Korea |
| Seong-Bok Kim |  | 주식회사 이솔 |
| Yong-Hoon Jo |  | LG Display |
| JAE-YONG PARK |  | KCB |
| DAE-YOUL PARK | Ph.D. | 한국전자통신연구원(ETRI) |
| Yeon-Gyeong Ju | Ph.D. | LG전자 |
| Junyoung Jang |  | 현대자동차 |
| Dabin Min | Ph.D. | 한국광기술원(KOPTI) |
| Xu Yunhan |  |  |
| Kyosik Min | Ph.D. | 현대모비스 |
| Kwang-Soo Shin | Ph.D. | 한국광기술원(KOPTI) |
| Changhi Lee |  | 현대모비스 |
| Minseok Kim |  | 경희대학교 |
| Mehdi Askari | Ph.D. | 한국전자통신연구원(ETRI) |
| Myeong-Ho Choi | Ph.D. | 삼성전자 MX사업부 |

## 최근 논문 목록 (2021–2026)

누리집 Publications의 2021–2026년 표기 논문 206건으로, 국제 학술지 38건, 국제 학회 99건, 국내 학회 69건이다. 2024년 서울대 부임 전 인하대학교 등 이전 소속 시절의 논문도 포함한다. 2021년 논문은 연도 전체를 포함하며, 학회 항목은 누리집의 발표 목록으로 학술지 논문과 구별한다.[^pubs][^bio]

**2026**

- S. Kheibarihafshejani, J.-H. Park "A review of transmission and reflective retroreflector arrays: characteristics and applications for 2D/3D aerial displays and retroreflector based optical architecture," Journal of Physics: Photonics, vol. 8, no. 4, article 042001 (2026). [Focus issue on 3D Imaging, Optical Imaging Sensors and AR/VR], DOI: https://doi.org/10.1088/2515-7647/aeaf98
- C. Lee, W. Han, and J.-H. Park, "Resolution improvement of super-multi-view near-eye displays via stochastic gradient descent method," Optics Express, vol. 34, no. 18, pp. 33057-33073 (2026). https://doi.org/10.1364/OE.609586
- W. Han, C.-H. Song, B. Chun, D. Lee, J.-H. Park, J. Kwak, and J. Y. Lee, "Review of recent display advancements: augmented reality, virtual reality, quantum-dot light-emitting diodes and organic light-emitting diodes," Journal of Information Display, vol. 27, article 15, (2026). https://doi.org/10.1007/s44469-026-00016-7
- M. Kim, M.-H. Choi, and J.-H. Park, “Thin Maxwellian Virtual Reality Near-Eye Display Using Holographic Optical Element and Mini-Fresnel Lens Array,” Journal of the Society for Information Display (2026): 1–10, https://doi.org/10.1002/jsid.70065.
- X. Hong, J. Xie, J. Sheng, F. Xie, J. Zhang, K. Wang, M. Cheng, C. Chen, J.-H. Park, and C. Wu, "Single-view neural illumination estimation and editing for dynamic light field display," Light: Science & Applications, vol. 15, article 147 (2026). https://doi.org/10.1038/s41377-026-02234-4
- C. Chen, M. Chae, S.-W. Nam, M.-H. Choi, M. Kim, E. Lee, Y. Jeong, and J.-H. Park, "PAColorHolo: A Perceptually-Aware Color Management Framework for Holographic Displays," ACM Transactions on Graphics, vol. 45, no. 2, article 22 (2026). [Presented at SIGGRAPH 2026] https://dl.acm.org/doi/10.1145/3789511
- J.-H. Park, "Toward Perceptually Realistic AR Glasses for the AI Era," Frontiers in Optics + Laser Science (Optica, FiO LS 2026) paper FTu2A.1, Rochester, New York, USA, Sep. 2026. [Visionary Talk]
- M. Shin, and J.-H. Park, "Pupil-Aware Incoherent Holographic Display," The 26th International Meeting on Information Display (IMID 2026), paper D58-3, Bexco, Busan, Korea, August 2026.
- S. Kheibarihafshejani, and J.-H. Park, "Image Brightness and Color Consistency for Multi-Layer Foveated Display," The 26th International Meeting on Information Display (IMID 2026), paper P3-081, Bexco, Busan, Korea, August 2026. [Best Poster Paper Award]
- G.-C. Han, J. Han, and J.-H. Park, "Spatially Reconfigurable Foveated Display Using 6-f Optics System," The 26th International Meeting on Information Display (IMID 2026), paper P3-106, Bexco, Busan, Korea, August 2026.
- C. Lee, W. Han, and J.-H. Park, "Optimization and Analysis Using Stochastic Gradient Descent for Resolution Improvement of Super-Multi-View Near-Eye Displays," The 26th International Meeting on Information Display (IMID 2026), paper P3-114, Bexco, Busan, Korea, August 2026.
- A. Mehdi and J.-H. Park, "End-to-End Polarization-Aware Phase-Only CGH from Four-Channel Polarimetric Images," The 26th International Meeting on Information Display (IMID 2026), paper P3-115, Bexco, Busan, Korea, August 2026.
- J.-H. Park, W. Han, C. Lee, C. Chen, M. Kim, and M.-H. Choi, "Holographic display with occlusion support and high color fidelity," Optica Digital Holography and Three-Dimensional Imaging Topical Meeting (DH 2026), paper Tu1A.1, Taipei, Taiwan, June 2026. [Invited]
- S. Kheibarihafshejani, and J.-H. Park, "Multilayer Foveated Near-eye Display Using a Spatial Light Modulator and Focus Tunable Optic," Optica Digital Holography and Three-Dimensional Imaging Topical Meeting (DH 2026), paper Tu1A.5, Taipei, Taiwan, June 2026.
- M. Kim, M.-H. Choi, and J.-H. Park, "Thin Maxwellian Virtual Reality Near-Eye Display Using Holographic Optical Element and Micro LensArray," SID Display Week 2026, paper 78.3, Los Angeles, CA, US, May 2026. [Distinguished Paper Award]
- J.-H. Park, "Near-eye display with optical foveation," SPIE Defense+Security, Three-Dimensional Imaging, Visualization, and Display 2026, Paper 14033-14, Maryland, US, April 2026. [Keynote presentation]
- J.-H. Park, C. Lee, W. Han, and M.-H. Choi, "Resolution enhancement of light field near-eye display using elemental image optimization," 2026 International Conference on Display Technology (ICDT 2026), Metaverse and Display Special Forum, Chongqing, China, March-April, 2026. [invited]
- G.-C. Han, C. Lee, and J.-H. Park, "Computational and optical design approaches for three-dimensional displays," The 25th International Conference on Electronics, Information, and Communication (ICEIC 2026), [Special Session 05] Key Technologies for Tera-level Light Field Displays, paper id: 1571217653, Macau, China, Jan. 2026.
- J.-H. Park, "Recent progress on enhancing realism of wearable extended reality displays," SPIE Photonics West, Ultra-High-Definition Imaging Systems IX, paper 13916-4, San Francisco, California, US, Jan. 2026. [invited]
- 박재형, 한지윤, Kheibarihafshejani Sahar, 한규찬, 송치혁, 구준영, "HOE-based optical coupling and system integration for curved waveguide AR displays," 한국광학회, 2026년 Optics and Photonics Congress (OPC 2026), 산업기술 알키미스트 프로젝트: 초실감 메타버스 시각화 기술 특별세션, paper T1D-S.03, ICC 제주, 2026년 7월. [invited]
- 이재홍, 김덕수, 박재형, "물리기반 렌더링과 경로 추적을 이용한 컴퓨터 생성 홀로그래피," 제33회 광전자 및 광통신 학술회의 (COOC 2026), paper W1D-I.02, 부산 해운대 한화리조트, 2026년 5월.
- 이찬슬, 한웅섭, 박재형, "Quantitative and Qualitative Analysis of Stochastic Gradient Descent for Resolution Enhancement in Super-Multi-View Near-Eye Displays," 제33회 광전자 및 광통신 학술회의 (COOC 2026), paper W1D-I.03, 부산 해운대 한화리조트, 2026년 5월.
- 김민성, 최명호, 박재형, "Virtual reality near eye display using waveguide and holographic optical element," 제33회 광전자 및 광통신 학술회의 (COOC 2026), paper W2D-II.03, 부산 해운대 한화리조트, 2026년 5월.
- 백재우, 박재형, "A Dithering Based Approach to High Resolution Ultrasonic Levitation," 제33회 광전자 및 광통신 학술회의 (COOC 2026), paper W2D-II.04, 부산 해운대 한화리조트, 2026년 5월.
- Mehdi Askari, 박재형, "Physics Informed Phase Only CGH Using Polarization Derived Geometry and Reflectance Cue," 제33회 광전자 및 광통신 학술회의 (COOC 2026), paper TPD-II.10, 부산 해운대 한화리조트, 2026년 5월.
- 한웅섭, Chen Chun, 박재형, "회절 심층 신경망 구조를 응용한 이진 진폭 홀로그래픽 근안 디스플레이용 컴팩트 단측파대 필터 연구," 제33회 광전자 및 광통신 학술회의 (COOC 2026), paper F2D-V.02, 부산 해운대 한화리조트, 2026년 5월. [우수논문상]
- 신민재, 박재형, "Pupil-Aware Incoherent Holographic Display," 제33회 광전자 및 광통신 학술회의 (COOC 2026), paper F2D-V.04, 부산 해운대 한화리조트, 2026년 5월.
- 박재형, 한지윤, Sahar KHEIBARIHAFSHEJANI, 최명호, 신광수, "광학적 포비에이션 적용된 근안 디스플레이 기술," 한국광학회 제37회 정기총회 및 2026년도 동계학술발표회, Paper W1C-III.02, 부산 벡스코, 2026년 2월. [Invited]
- 한지윤, 최명호, 신광수, 박재형, "위상 변조 빔 조향 기반 동적 포비에이티드 디스플레이 시스템," 한국광학회 제37회 정기총회 및 2026년도 동계학술발표회, Paper W4C-III.04, 부산 벡스코, 2026년 2월.
- 백재우, 한지윤, 박재형, "초음파 부양 체적 디스플레이의 복소 진폭 음향장 변조 분석," 한국광학회 제37회 정기총회 및 2026년도 동계학술발표회, Paper TP-III.10, 부산 벡스코, 2026년 2월.

**2025**

- R. Kumar, M.-H. Choi, R. Kaur, and J.-H. Park, "Double Maxwellian foveated display," Journal of Information Display, vol. 26, no. 4, pp. 483-492 (2025). https://doi.org/10.1080/15980316.2025.2565193
- W. Han, C. Lee, and J.-H. Park, "Enhancing realism in holographic augmented reality displays through occlusion handling," Laser & Photonics Reviews, vol. 19, no. 19, e01052 (2025). https://doi.org/10.1002/lpor.202501052
- K. Min, M.-H. Choi, and J.-H. Park, "Quality enhancement of computer-generated hologram without contents-dependent optimization by considering aberrations in the optical system," Optics Express, vol. 33, no. 13, pp. 27148-27163 (2025). https://doi.org/10.1364/OE.564892
- R. Kaur, B. Das, J.-H. Park, and R. Kumar, "Improved color uniformity in monochrome holographic waveguide based near eye displays," Optics Express, vol. 33, no. 11, pp. 22255-22269 (2025). https://doi.org/10.1364/OE.566713
- J. Han, W. Han, and J.-H. Park, "Varifocal near-eye display with extended eyebox using dual slit-mirror array," Optics & Laser Technology, vol. 189, article 113053 (2025). https://doi.org/10.1016/j.optlastec.2025.113053
- S. Kheibarihafshejani, and J.-H. Park, "Integral imaging 3D display with enhanced depth range using slit mirror array and dual display systems," Journal of Optics, vol. 27, no. 3, article 035701 (2025). https://doi.org/10.1088/2040-8986/adaf3b
- S. Kheibarihafshejani, and J.-H. Park, "Multi-view multi-focal 3D display using light source array and focus tunable optics," Optics Express , vol. 33, no. 3, pp. 5727-5745 (2025). https://doi.org/10.1364/OE.546843
- G.-C. Han, W. Han, K.-S. Shin, and J.-H. Park, "Multifocal near-eye display with a vari-focal lens and adjustable aperture," Optics Express, vol. 33, no. 1, pp. 1132-1147 (2025). https://doi.org/10.1364/OE.545790
- K.-S. Shin, J. Hong, W. Han, and J.-H. Park, "Field of view and angular-resolution enhancement in micro lens array type virtual reality near eye display using polarization grating," Optics Express, vol. 33, no. 1, pp. 263-278 (2025). https://doi.org/10.1364/OE.546812
- C. Lee, W. Han, and J.-H. Park, "Resolution Improvement for Light Field Near Eye Display by using Stochastic Gradient Descent Method," The 15th Japan-Korea Workshop on Digital Holography and Information Photonics (DHIP 2025), paper P07, Ishigaki, Japan, Dec. 2025.
- W. Han, C. Lee, and J.-H. Park, "Sparse Holographic Image Optimization for Augmented Reality Display with Active Fourier Filter," The 15th Japan-Korea Workshop on Digital Holography and Information Photonics (DHIP 2025), paper P11, Ishigaki, Japan, Dec. 2025.
- M. Kim, M.-H. Choi, and J.-H. Park, "Thin Maxwellian virtual reality near-eye display using holographic optical element and micro lens array," The 15th Japan-Korea Workshop on Digital Holography and Information Photonics (DHIP 2025), paper P17, Ishigaki, Japan, Dec. 2025.
- J.-H. Park, W. Han, and C. Lee, "Occlusion-capable holographic optical see-through near-eye-display," The 15th Japan-Korea Workshop on Digital Holography and Information Photonics (DHIP 2025), paper Su3-2, Ishigaki, Japan, Dec. 2025. [Invited]
- C. Chen, J.-H. Park, and Y. Jeong, "Addressing color fidelity challenges in holographic displays", SPIE Photonics Asia, Optical Design and Testing XV (Proc. SPIE 13716), paper 137160S, Beijing China, Oct. 2025. [Invited] https://doi.org/10.1117/12.3073352
- J.-H. Park, W. Han, and C. Lee, "Optical see-through holographic 3D near eye display with occlusion support", Optica, Frontiers in Optics + Laser Science (FiO LS), paper FTu6B.3, Colorado Convention Center, Denver, Colorado, USA, Oct. 2025. [Invited]
- M.-H. Choi, and J.-H. Park, "Eye-box Expansion Technique for Holographic Displays by Overlapping Replicated High-Order Diffraction Terms," Optica Imaging Congress 2025, Digital Holography and 3-D Imaging (DH), paper DTh3A.4, Hyatt Regency Seattle, Seattle, USA, Aug. 2025.
- J. Han, M.-H. Choi, K.-S. Shin, and J.-H. Park, "Spatially Reconfigurable Foveated Display Using Phase-Based Beam Steering," Optica Imaging Congress 2025, Digital Holography and 3-D Imaging (DH), paper DTh1C.3, Hyatt Regency Seattle, Seattle, USA, Aug. 2025.
- W. Han, C. Lee, and J.-H. Park, "Occlusion-Capable Holographic Augmented Reality Near-Eye Display Using a DigitalMicromirror Device," Optica Imaging Congress 2025, Digital Holography and 3-D Imaging (DH), paper DTh1C.2, Hyatt Regency Seattle, Seattle, USA, Aug. 2025.
- C. Lee, M.-H. Choi, and J.-H. Park, "Machine learning-based wobulation for automotive headlight projectors: High-speed generation of subpixel-shifted images," The 25th International Meeting on Information Display (IMID 2025), paper F14-3, Bexco, Busan, Korea, Aug. 2025.
- G.-C. Han, M.-H. Choi, K. Won, and J.-H. Park, "Field-of-view steerable waveguide-type near-eye display for augmented reality," The 25th International Meeting on Information Display (IMID 2025), paper P2-044, Bexco, Busan, Korea, Aug. 2025.
- M. Kim, and J.-H. Park, "Super multi-view near-eye display with adjustable point light source array," SID Display Week, paper 58.3, San Jose, CA, US, May 2025.
- J.-H. Park, W. Han, M.-H. Choi, and C. Lee, "Occlusion supporting augmented reality near-eye display," Optics & Photonics International Congress (OPIC), Optical Technology and Measurement for Industrial Applications, paper OPTM8-01, Pacifico Yokohama, Japan, April 2025. [Invited]
- J.-H. Park, W. Han, M.-H. Choi, and C. Lee, "Optical see-through three-dimensional near-eye display with occlusion support," SPIE Defense + Commercial Sensing, Three-Dimensional Imaging, Visualization, and Display 2025, paper 13465-20, Orlando, Florida, US, April 2025. [Invited] [Fumio Okano Best Paper Award]
- J.-H. Park, and M.-H. Choi, "Foveated Holographic Near-Eye-Display with a Compact Form Factor," International Conference on Display Technology (ICDT), paper 31.1, Xiamen Fliport C&E Center, China, March 2025. [Invited]
- J.-H. Park, M. Kim, W. Han, and X. Yunhan, "Thin virtual reality display presenting Maxwellian and super-multiview three-dimensional images," SPIE Photonics West, Advances in Display Technologies XV, paper 13388-20, Moscone center, San Francisco, CA, USA, Jan. 2025. [Invited]
- S. Kheibarihafshejani, 한규찬, 남제호, 김현의, 박재형, "Measurement of Monochromatic Speckle Contrast in Holographic Displays," Photonics Conference (PC 2025), paper TP-V.14, 휘닉스 평창, 2025년 11월.
- 신광수, 박재형, "단일 영상 기반 근안 디스플레이 화각 측정 시스템," Photonics Conference (PC 2025), paper TP-V.18, 휘닉스 평창, 2025년 11월.
- 이찬슬, 한웅섭, 박재형, "Resolution Improvement for Light Field Near Eye Display by using Stochastic Gradient Descent Method," Optics and Photonics Congress 2025, 한국광학회 하계학술대회, paper T1G-III.03, ICC 제주, 2025년 7월.
- 신민재, 박재형, "루프 내 카메라 기반 압축 전파 모델링 및 비간섭성 컴퓨터 생성 홀로그램 최적화," Optics and Photonics Congress 2025, 한국광학회 하계학술대회, paper T2G-III.03, ICC 제주, 2025년 7월. [우수논문상]
- 김민성, 박재형, "홀로그래픽 광학 소자를 이용한 가상 현실 근안 디스플레이의 두께 저감," 제32회 광전자 및 광통신 학술대회 (COOC 2025), paper W1D-I.03, 부산 해운대, 2025년 5월.
- 박재형, 한웅섭, 최명호, 이찬슬, "광투과 근안 디스플레이에서의 폐색 구현," 제32회 광전자 및 광통신 학술대회 (COOC 2025), paper T1D-II.02, 부산 해운대, 2025년 5월. [invited]
- 한웅섭, 박재형, "액티브 푸리에 필터를 활용한 증강현실용 희소 홀로그래픽 이미지 최적화," 제32회 광전자 및 광통신 학술대회 (COOC 2025), paper T1D-II.03, 부산 해운대, 2025년 5월.
- 한규찬, 최명호, 원강희, 박재형, "화각 조향이 가능한 도파관형 증강현실 근안 디스플레이," 제32회 광전자 및 광통신 학술대회 (COOC 2025), paper F2D-V.03, 부산 해운대, 2025년 5월.
- 최명호, 이재홍, 김덕수, 박재형, "깊이 범위 조작이 가능한 단일 신경망 기반 복소 홀로그램 생성 기법," 한국광학회 제36회 정기총회 및 2025년도 동계학술발표회, paper W3A-III.03, 벡스코, 부산, 2025년 2월.
- Sahar Kheibarihafshejani, 박재형, "Time-multiplexed foveated near-eye display with computational holography and focus tunable optics," 한국광학회 제36회 정기총회 및 2025년도 동계학술발표회, paper W3A-III.04, 벡스코, 부산, 2025년 2월. [우수논문상]
- 정동한, 최명호, 박재형, "Varifocal Augmented Reality Near Eye Display with Free Space Holographic Optical Element Combiner," 한국광학회 제36회 정기총회 및 2025년도 동계학술발표회, paper WP-III.05, 벡스코, 부산, 2025년 2월.
- Mehdi Askari, 임용준, 오관정, 박재형, "High-Resolution Complex Field Prediction in Polarization-Based Digital Holography," 한국광학회 제36회 정기총회 및 2025년도 동계학술발표회, paper TP-III.04, 벡스코, 부산, 2025년 2월.
- 한규찬, 한웅섭, 신광수, 박재형, "조리개 광 투과도 제어를 통한 초점심도 조절 다초점 근안 디스플레이의 영상 품질 개선," 1st Korean Meeting on Information Display (KMiD 2025), paper TC2-5, 세인트존스호텔, 강릉, 2025년 1월 20일-22일. [우수발표상]
- 민교식, 최명호, 박재형, "수차 반영 역 전파 방정식의 최적화를 통한 객체 비의존적 홀로그램 품질 향상," 1st Korean Meeting on Information Display (KMiD 2025), paper P2-041, 세인트존스호텔, 강릉, 2025년 1월 20일-22일.

**2024**

- A. Mehdi, Y. Lim, K.-J. Oh, and J.-H. Park, "U-Net Driven High-Resolution Complex Field Information Prediction in Single-Shot 4-Step Phase-Shifted Digital Holography using Polarization Camera" Photonics, vol. 11, no. 12, article 1172 (2024). https://doi.org/10.3390/photonics11121172
- J. Kang, G. W. Baek, J. Y. Lee, J. Kwak, and J.-H. Park, "Advances in Display Technology: Augmented Reality, Virtual Reality, Quantum Dot-Based Light-Emitting Diodes, and Organic Light-Emitting Diodes," Journal of Information Display, vol. 25, no. 3, pp. 219-234, (2024). https://doi.org/10.1080/15980316.2024.2350437
- M.-H. Choi, W. Han, K. Min, D. Min, G. Han, K.-S. Shin, M. Kim, and J.-H. Park, "Recent Applications of Optical Elements in Augmented and Virtual Reality Displays: a Review," ACS Applied Optical Materials, vol. 2, no. 7, pp. 1247-1268 (2024). https://doi.org/10.1021/acsaom.4c00033
- S. Kheibarihafshejani, and J.-H. Park, "Time multiplexing multi-view display using slit mirror array and light emitting diode illuminated digital micromirror device," Journal of Information Display, vol. 25, no. 4, pp. 349-365 (2024). https://doi.org/10.1080/15980316.2024.2329124 [JID Outstanding Paper Award]
- W. Han, J.-W. Lee, J.-Y. Shin, M.-H. Choi, H.-R. Kim, and J.-H. Park, "Varifocal occlusion in optical see-through near-eye display with single phase-only liquid crystal on Silicon," Photonics Research, vol 12, no 4, pp.833-854 (2024). https://doi.org/10.1364/PRJ.509948
- K. Min, D. Min, J. Hong, and J.-H. Park, "Speckle reduction for single sideband-encoded computer-generated holograms by using optimized carrier wave," Optics Express, vol. 32, no. 8, pp. 13508-13526 (2024). https://doi.org/10.1364/OE.518427
- M. Kim, W. Han, and J.-H. Park, "Slim Maxwellian near-eye display for virtual reality using point light source array," IEEE Journal of Selected Topics in Quantum Electronics, vol. 30, no. 2, article 3372001 (2024). DOI: 10.1109/JSTQE.2024.3372001
- M.-H. Choi, M. Kim, K.-S. Shin, J. Hong, and J.-H. Park, "Waveguide-Based Binocular Maxwellian Near-Eye display Employing a Single Micro-display and Polarization Grating," IEEE Journal of Selected Topics in Quantum Electronics, vol. 30, no. 2, article 4400110 (2024). DOI: 10.1109/JSTQE.2024.3369692
- R. Kaur, J.-H. Park, and R. Kumar, "Effect of shrinkage in photopolymer film on the information transmitted through holographic waveguide for near eye display," J. Opt. Soc. Am. A 41, A15-A24 (2024). https://opg.optica.org/josaa/abstract.cfm?URI=josaa-41-3-A15
- J.-H. Park, J. Han, W. Han, G.-C. Han, and K.-S. Shin, "Near eye displays using transmission type retroreflector," The 14th Korea-Japan Workshop on Digital Holography and Information Photonics (DHIP 2024), paper W1-1, Seoul National University, Seoul, Korea, Dec. 15-18, 2024. [Invited]
- J. Han, and J.-H. Park, "Performance analysis of a deep-learning-based Fourier ptychographic microscopy," The 14th Korea-Japan Workshop on Digital Holography and Information Photonics (DHIP 2024), paper P10, Seoul National University, Seoul, Korea, Dec. 15-18, 2024.
- K. Min, and J.-H. Park, "Quality enhancement of computer-generated hologram by considering aberrations in the optical system," The 14th Korea-Japan Workshop on Digital Holography and Information Photonics (DHIP 2024), paper P11, Seoul National University, Seoul, Korea, Dec. 15-18, 2024.
- S. Kheibarihafshejani, and J.-H. Park, "Time-multiplexed foveated near-eye display with computational holography and focus tunable optics," The 14th Korea-Japan Workshop on Digital Holography and Information Photonics (DHIP 2024), paper P12, Seoul National University, Seoul, Korea, Dec. 15-18, 2024.
- J.-H. Park, "Focus cue and occlusion supporting AR near eye displays," OPTIC 2024 (Optics & Photonics Taiwan International Conference, 2024 Annual Meeting of Taiwan Photonics Society), Nangang Exhibition Center, Taipei, Taiwan, Nov. 26-29, 2024. [Invited]
- J.-H. Park, M.-H. Choi, W. Han, and M. Kim, "Compact super multi-view and foveated holographic near eye display for augmented reality and virtual reality applications," JSAP-Optica Joint Symposia, The 85th JSAP(The Japanese Society of Applied Physics) Autumn Meeting, paper 17a-A37-4, Niigata, Japan, Sep. 2024. [Invited]
- J.-H. Park, M. Kim, W. Han, and X. Yunhan, "Slim and vergence-accommodation-conflict-free VR near eye display," The 24th International Meeting on Information Display (IMID 2024), paper D20-2, Jeju, Korea, Aug. 2024. [Invited]
- K.-S. Shin, and J.-H. Park, "Enhancing Field of View and the Angular Resolution in Micro Lens Array Type VR System through Polarization Grating," The 24th International Meeting on Information Display (IMID 2024), paper A49-4, Jeju, Korea, Aug. 2024.
- K. Min, J. Hong, and J.-H. Park, "Restoration of Speckled Hologram Reconstruction by Using Denoising Diffusion Probabilistic Model," The 24th International Meeting on Information Display (IMID 2024), paper P2-036, Jeju, Korea, Aug. 2024.
- G.-C. Han, W. Han, and J.-H. Park, "Multifocal Near-Eye Display with a Varifocal Lens and Adjustable Aperture," The 24th International Meeting on Information Display (IMID 2024), paper D60-3, Jeju, Korea, Aug. 2024.
- M. Kim, and J.-H. Park, "Direct-view type super multi-view near-eye display using point light source array," 16th Pacific Rim Conference on Lasers and Electro-Optics (CLEO-PR 2024), paper Fr1G-4, Incheon Korea, Aug. 2024.
- J.-H. Park, "Recent progress on super-multi-view and holographic near eye displays," Light Conference, Metaverse/AR/VR Track, Northeast Asia International Conference Center, Changchun, China, Jun 17-21, 2024. [Invited]
- M.-H. Choi, K. Won, and J.-H. Park, "Optimization Algorithm of Computer-Generated Hologram Considering Leakage of Active Beam Deflector," Optica Digital Holography and Three-Dimensional Imaging Topical Meeting (DH 2024), paper Tu1A.2, Mec Paestum Hotel, Capaccio Paestum, Italy, 03-06 June, 2024.
- M. Kim, and J.-H. Park, "Compact Near-eye Display for Mixed Reality Using Micro Lens Array and Point Light Source Array," Optica Digital Holography and Three-Dimensional Imaging Topical Meeting (DH 2024), paper W2B.7, Mec Paestum Hotel, Capaccio Paestum, Italy, 03-06 June, 2024.
- J.-H. Park, "Next generation MR 3D near eye display," OPTICS & PHOTONICS International Congress 2024, Laser Display and Lighting Conference, LDC1-01, Yokohama, Japan, April 2024. [Keynote presentation]
- J.-H. Park, M.-H. Choi, W. Han, and J. Han, "Recent progress on super-multi-view and foveated holographic displays for near-to-eye display application," SPIE Photonics West, Advances in Display Technologies XIV, paper 12908-13, San Francisco, United States, Jan. 2024. [Invited]
- K. Min, and J.-H. Park, "Quality evaluation of speckle-noise-contaminated computer-generated holograms by using deep neural network," SPIE Photonics West, Practical Holography XXXVIII: Displays, Materials, and Applications, paper 12910-4, San Francisco, United States, Jan. 2024. http://dx.doi.org/10.1117/12.3000279
- W. Han, M.-H. Choi, and J.-H. Park, "Video see-through super multi-view near eye display using waveguide-type light source and ferroelectric liquid crystal on silicon," SPIE AR/VR/MR, Optical Architectures for Displays and Sensing in Augmented, Virtual, and Mixed Reality (AR, VR, MR) V, paper 12913-13, San Francisco, United States, Jan. 2024. http://dx.doi.org/10.1117/12.3000271
- M. Kim, and J.-H. Park, "Dual-sided mixed reality near-eye display using dihedral corner reflector array," SPIE AR/VR/MR, Optical Architectures for Displays and Sensing in Augmented, Virtual, and Mixed Reality (AR, VR, MR) V, paper 12913-7, San Francisco, United States, Jan. 2024. https://doi.org/10.1117/12.3001334
- M.-H. Choi, K.-S. Shin, and J.-H. Park, "Foveated holographic near-eye display with geometric phase lens and camera feedback," SPIE AR/VR/MR, Optical Architectures for Displays and Sensing in Augmented, Virtual, and Mixed Reality (AR, VR, MR) V, paper 12913-14, San Francisco, United States, Jan. 2024. [Optical Design Challenge Finalist] http://dx.doi.org/10.1117/12.3002029
- K. Sahar, 박재형, "Multi-view multi-depth display using light emitting diode illuminated digital micromirror device and focus tunable lens," Optics and Photonics Congress 2024, 한국광학회 하계학술대회, paper T2B-VII.03, ICC 제주, 2024년 7월.
- 한웅섭, 민교식, 최명호, 박재형, "진폭변조 SLM을 이용한 폐색 적용 홀로그래픽 증강현실 디스플레이," Optics and Photonics Congress 2024, 한국광학회 하계학술대회, paper T1C-III.03, ICC 제주, 2024년 7월. [우수논문상]
- 박재형, "해상도 손실 적은 라이트필드와 홀로그램 간 데이터 변환 및 그 응용," Optics and Photonics Congress 2024, 한국광학회 하계학술대회, paper T1C-III.01, ICC 제주, 2024년 7월. [Invited paper]
- 신광수, 박재형, "핀라이트 어레이 및 램버시안 광원 기반 다초점 맥스웰리안 근안 디스플레이," 한국방송미디어공학회 2024년 하계학술대회, paper P2-21, 메종 글래드 제주 호텔, 제주, 2024년 6월.
- 최명호, 원강희, 박재형, "능동 빔 디플렉터의 누출을 고려한 컴퓨터 생성 홀로그램 최적화 알고리즘," 제31회 광전자 및 광통신 학술회의 (COOC 2024), paper W1D-I.02, 부산 해운대 한화리조트, 2024년 5월.
- 김민성, 박재형, "Near-eye display for mixed reality using point light source array," 제31회 광전자 및 광통신 학술회의 (COOC 2024), paper T2D-III.02, 부산 해운대 한화리조트, 2024년 5월.
- 최명호, 박재형, 기하 위상 렌즈를 이용한 포비티드 홀로그래픽 근안 디스플레이," 제35회 한국광학회 정기총회 및 2024 동계학술발표회, paper W2B-III.03, 수원컨벤션센터, 2024년 2월.
- 한웅섭, 최명호, 박재형, "강유전체 LCoS와 도파관 기반 광원을 이용한 초다시점 비디오 투과형 근안 디스플레이," 제35회 한국광학회 정기총회 및 2024 동계학술발표회, paper W3B-III.02, 수원컨벤션센터, 2024년 2월.
- 신광수, 박재형, "마이크로 렌즈 어레이를 이용한 얇은 가상현실 근안 디스플레이의 편광 격자 기반 해상도 및 화각 향상," 제35회 한국광학회 정기총회 및 2024 동계학술발표회, paper W3B-III.05, 수원컨벤션센터, 2024년 2월.
- 한규찬, 박재형, "마이크로 알바레즈 렌즈 배열을 이용한 라이트필드 카메라 구조 시뮬레이션," 제35회 한국광학회 정기총회 및 2024 동계학술발표회, paper WP-III.001, 수원컨벤션센터, 2024년 2월. [우수논문상]
- 서온한, 박재형, "홀로그래픽 광학 소자를 이용한 박형 가상현실 맥스웰리안 근안 디스플레이," 제35회 한국광학회 정기총회 및 2024 동계학술발표회, paper TP-VII.007, 수원컨벤션센터, 2024년 2월.

**2023**

- K. Min, D. Min, and J.-H. Park, "Wigner inverse transform based computer generated hologram for large object at far field from its perspective light field," Optics Communications, vol. 532, article 129229 (2023). 10.1016/j.optcom.2022.129229
- J.-H. Park, W. Han, J.-W. Lee, J.-Y. Shin, M.-H. Choi, and H.-R. Kim, "Occlusion-capable vari-focal augmented reality display," Proceedings of The 13th Japan-Korea Workshop on Digital Holography and Information Photonics (DHIP), paper 1-2, pp. 17, Beppu, Oita, Japan, Dec. 2023. [Invited]
- G.-C. Han, and J.-H. Park, "Simulation of light field camera using micro Alvarez lens array," Proceedings of The 13th Japan-Korea Workshop on Digital Holography and Information Photonics (DHIP), paper P04, pp. 48, Beppu, Oita, Japan, Dec. 2023.
- K. Min, D. Min, and J.-H. Park, "Speckle reduction using carrier wave optimization of single sideband-encoded computer-generated holograms without contents dependency," Proceedings of The 13th Japan-Korea Workshop on Digital Holography and Information Photonics (DHIP), paper P07, pp. 51, Beppu, Oita, Japan, Dec. 2023.
- M. Kim and J.-H. Park, "Slim Maxwellian near-eye display using pinlight array for virtual reality," Proceedings of The 13th Japan-Korea Workshop on Digital Holography and Information Photonics (DHIP), paper P12, pp. 55, Beppu, Oita, Japan, Dec. 2023.
- S. Kheibarihafshejani, and J.-H. Park, "Time multiplexing multi-view display using slit mirror array and light emitting diode illuminated digital micromirror device," Proceedings of The 13th Japan-Korea Workshop on Digital Holography and Information Photonics (DHIP), paper P16, pp. 60, Beppu, Oita, Japan, Dec. 2023. [Student Presentation Award]
- J.-H. Park, "Eyebox expansion and vision correction for varifocal near-eye-display," SPIE/COS Photonics Asia 2023, paper 12765-7, Beijing International Convention Center, Beijing, China, Oct. 2023. [Invited]
- J.-H. Park, "Eyebox expansion and vision correction for varifocal near-eye-display using two dimensional retro-refelctor," 2023 Frontiers in Optics + Laser Science (FiO LS), paper FM5C.1, Greater Tacoma Convention Center, Tacoma (Greater Seattle Area), Washington, USA, Oct. 2023. [Invited]
- W. Han, J.-W. Lee, J.-Y. Shin, M.-H. Choi, H.-R. Kim, and J.-H. Park, "Varifocal-occlusion supported near-eye display using stack of geometric phase lenses and electrically switchable half wave plate," The 23rd International Meeting on Information Display (IMID 2023), paper P2-050, Bexco, Busan, Korea, Aug. 2023. [Best Poster Paper Award]
- J.-H. Park, "Optical techniques toward hyper-realistic AR and MR glasses," The 23rd International Meeting on Information Display (IMID 2023), Merck Science Connect, paper H40-2, Bexco, Busan, Korea, Aug. 2023. [Invited]
- K. Min, D. Min, and J.-H. Park, "Quality enhancement of Wigner inverse transform-based light field to computer-generated hologram by optimizing carrier wave," Optica Imaging Congress 2023, Digital Holography and 3-D Imaging (DH), paper HM1D.3., Boston, USA, Aug. 2023.
- M.-H. Choi and J.-H. Park, "Leveraging High-Order Diffractions of Phase Hologram using Pupil Function for Enhanced Holographic Display," Optica Imaging Congress 2023, Digital Holography and 3-D Imaging (DH), paper HM1D.4, Boston, USA, Aug. 2023. [Student paper competition finalist]
- D. Min, K. Min, and J.-H. Park, "Wigner Inverse Transform Based Computer-generated Hologram Synthesis from Light Field Obtained by Neural Network," Optica Imaging Congress 2023, Digital Holography and 3-D Imaging (DH), paper HM3C.6, Boston, USA, Aug. 2023.
- J. Han, W. Han, and J.-H. Park, "Varifocal Near-eye Display with a Wide Field of View and Eyebox using Dihedral Corner Reflector Array," Optica Imaging Congress 2023, Digital Holography and 3-D Imaging (DH), paper HM4C.3, Boston, USA, Aug. 2023.
- S. Kheibarihafshejani and J.-H. Park, "Floating multi-view three-dimensional display using a digital micro-mirror and dihedral corner reflector array," Optica Imaging Congress 2023, Digital Holography and 3-D Imaging (DH), paper JTu4A.19, Boston, USA, Aug. 2023.
- W. Han and J.-H. Park, "Eyebox-Expanded Retina-Projection Near-eye Display Using Dihedral Corner Reflector Array," Optica Imaging Congress 2023, 3D Imaging Acquisition and Display: Technology, Perception and Applications (3D), paper JTu4A.33, Boston, USA, Aug. 2023.
- R. Kumar, M.-H. Choi, J. Jang, and J.-H. Park, "Combined effect of pin-mirror and concave mirror as outcouplers in Maxwellian holographic near-eye displays," Optica Imaging Congress 2023, Digital Holography and 3-D Imaging (DH), paper JW2A.21, Boston, USA, Aug. 2023.
- R. Kaur, J.-H. Park, and R. Kumar, "Pre-compensation model for shrinkage effect in photopolymer materials for holographic near eye displays," Optica Imaging Congress 2023, Digital Holography and 3-D Imaging (DH), paper DW3A.4, Boston, USA, Aug. 2023.
- J.-H. Park, W. Han, J. Lee, J. Shin, M.-H. Choi, H.-R. Kim, "Optical-see-through near-eye-display with 3D occlusion," Optica Imaging Congress 2023, 3D Imaging Acquisition and Display: Technology, Perception and Applications (3D), paper DW4A.2, Boston, USA, Aug. 2023. [Invited]
- M. Askari, and J.-H. Park, "Super resolution image generation from the complex field information generated using deep learning model," 12th International Symposium on Digital Holography (ISDH 2023), paper ISDH2023-ED-0236, Kwangwoon University, Seoul, Korea, June 2023.
- J.-H. Park, "Optical See-through augmented reality near-eye-display with monocular focus cue support," 2023 International Conference on Display Technology (ICDT 2023), paper 14.2, Nanjing International Exhibition Center, Nanjing, China, March 2023. [Invited]
- 박재형, 한웅섭, 이재원, 신중엽, 최명호, 김학린, "광투과 근안디스플레이에서의 3차원 폐색 구현," 한국광학회 Optics and Photonics Congress 2023, OSK Summer Annual Meeting, paper M2H-VII.02, ICC 제주, 2023년 8월. [Invited paper]
- 김민성, 박재형, "핀홀 배열을 이용한 근안 디스플레이의 균일도 분석 및 시뮬레이션," 한국광학회 Optics and Photonics Congress 2023, OSK Summer Annual Meeting, paper M1E-III.04, ICC 제주, 2023년 8월.
- 최명호, 박재형, "공간광변조기의 고차 회절 성분 및 동공 함수를 고려한 위상 변조 홀로그램 최적화 방법," 한국광학회 Optics and Photonics Congress 2023, OSK Summer Annual Meeting, paper M2E-III.03, ICC 제주, 2023년 8월. [우수논문상]
- 신광수, 박재형, "편광 격자를 이용한 가상현실 근안디스플레이의 시야각 및 해상도 향상," 한국광학회 Optics and Photonics Congress 2023, OSK Summer Annual Meeting, paper T1E-III.05, ICC 제주, 2023년 8월.
- 유동근, 박재형, 이홍석, "집적영상술과 이면 배열 코너 반사체를 사용한 3차원 즉석 사진 촬영," 한국광학회 Optics and Photonics Congress 2023, OSK Summer Annual Meeting, paper TP-III.04, ICC 제주, 2023년 8월.
- Mehdi Askari, 박재형, "Super-resolution for phase shifted digital hologram with U-Net-based architecture," 한국광학회 Optics and Photonics Congress 2023, OSK Summer Annual Meeting, paper W1E-III.04, ICC 제주, 2023년 8월.
- 민교식, 박재형, "Single sideband 인코딩된 복소 홀로그램의 반송파 최적화를 통한 객체 비의존적 스페클 저감 기법," 한국광학회 Optics and Photonics Congress 2023, OSK Summer Annual Meeting, paper W3E-III.04 , ICC 제주, 2023년 8월.
- 박재형, 한지윤, 한웅섭, "Dihedral corner reflector array를 이용한 가변 초점 가상현실 근안 디스플레이의 아이박스 확장," 제30회 광전자 및 광통신 학술회의 (COOC 2023), paper W1I-I.01, 부산 한화리조트 해운대, 2023년 5월. [invited paper]
- 김민성, 박재형, "Virtual reality and augmented reality near-eye-display using pinhole array," 제30회 광전자 및 광통신 학술회의 (COOC 2023), paper WP-VII.002, 부산 한화리조트 해운대, 2023년 5월.
- 박재형, 최명호, "기하위상렌즈 기반 자가간섭 홀로그래픽 카메라의 잡음 분석," 한국광학회 제34회 정기총회 및 2023 동계학술발표회, paper T1B-S.02, 부산 BEXCO, 2023년 2월. [invited paper]
- 민교식, 민다빈, 박재형, "고품질 홀로그램 생성을 위한 라이트필드를 사용한 위그너 역변환 기반 컴퓨터 생성 홀로그램의 반송파 최적화," 한국광학회 제34회 정기총회 및 2023 동계학술발표회, paper W2B-III.04, 부산 BEXCO, 2023년 2월.
- 한지윤, 한웅섭, 박재형, "초점 변환 렌즈와 2면 코너 리플렉터 어레이를 이용한 가변초점 근안 디스플레이," 한국광학회 제34회 정기총회 및 2023 동계학술발표회, paper W3B-III.03, 부산 BEXCO, 2023년 2월.
- 한웅섭, 이재원, 신중엽, 최명호, 김학린, 박재형, "전기적으로 초점 변환되는 기하 위상 렌즈군을 이용한 가변초점 폐색 가능 증강현실 근안 디스플레이," 한국광학회 제34회 정기총회 및 2023 동계학술발표회, paper W3B-III.05, 부산 BEXCO, 2023년 2월.
- 추현곤, 주연경, 박재형, 임용준, "광학 수차를 고려한 U-Net 기반 홀로그램 복원 성능 분석," 한국광학회 제34회 정기총회 및 2023 동계학술발표회, paper F1B-III.01, 부산 BEXCO, 2023년 2월.
- 민다빈, 민교식, 박재형, "단일 이미지로부터 위그너 역변환 기반 컴퓨터 생성 홀로그램 합성," 한국광학회 제34회 정기총회 및 2023 동계학술발표회, paper F1B-III.03, 부산 BEXCO, 2023년 2월.

**2022**

- W. Han, J. Han, Y.-G. Ju, J. Jang, and J.-H. Park, "Super multi-view near-eye display with a lightguide combiner," Optics Express, vol. 30, no. 26, pp. 46383-46403 (2022). https://doi.org/10.1364/OE.477517
- D. Min, K. Min. H.-J. Choi, H. Lee, and J.-H. Park, "A non-hogel-based computer generated hologram with occlusion processing between the foreground light field and background hologram," Optics Express, vol. 30, no. 21, pp. 38339-38356 (2022). https://doi.org/10.1364/OE.468748
- S. Ordones, J.-H. Park, H. Quach, D. Kim, and H. Choi, "Spatial–temporal phase demodulation decoding superimposed ghost reflections in optical testing," Optics Letters, vol. 47, no. 16, pp. 4135-4138 (2022). https://doi.org/10.1364/OL.468063
- Y.-G. Ju, H.-G. Choo, and J.-H. Park, "Learning-based complex field recovery from digital hologram with various depth objects," Optics Express, vol. 30, no. 15, pp. 26149-26168 (2022). https://doi.org/10.1364/OE.461782
- M. Askari, and J.-H. Park, "Augmentation of 3D holographic image graticule with conventional microscopy," Frontiers in Photonics, vol. 3, article 929936 (2022). DOI: 10.3389/fphot.2022.929936
- J.-H. Park, and B. Lee, "Holographic techniques for augmented reality and virtual reality near-eye displays," Light: Advanced Manufacturing, vol. 3, article number 9 (2022). https://doi.org/10.37188/lam.2022.009
- W. Han, J.-M. Jeon, M.-H. Choi, and J.-H. Park, "Lightguide type Maxwellian near-eye display with enlarged horizontal field of view by optical reconfiguration of input image," Journal of Information Display, vol. 23, no. 3, pp. 201-211 (2022). DOI: 10.1080/15980316.2022.2039789
- H. J. Jang, J. Y. Lee, G. W. Baek, J. Kwak, and J.-H. Park, "Progress in the development of the display performance of AR, VR, QLED and OLED devices in recent years," Journal of Information Display, vol. 23, no.1, pp.1-17 (2022). https://doi.org/10.1080/15980316.2022.2035835
- M.-H. Choi, K.-S. Shin, J. Jang, W. Han, and J.-H. Park, "Waveguide-type Maxwellian near-eye display using a pin-mirror holographic optical element array," Optics Letters, vol. 47, no. 2, pp. 405-408 (2022). https://doi.org/10.1364/OL.443004
- S. Kheibarihafshejani, and J.-H. Park, "Blurring phenomena in floating images at DCRA plates," The 12th Korea-Japan Workshop on Digital Holography and Information Photonics (DHIP 2022), paper T3-15-KP, Wonkwang University, Iksan, Korea, Dec. 2022.
- M. Kim, Y.-G. Ju, and J.-H. Park, "Compact Augmented reality near-eye display using pinhole array," The 12th Korea-Japan Workshop on Digital Holography and Information Photonics (DHIP 2022), paper M3-07-KS2, Wonkwang University, Iksan, Korea, Dec. 2022.
- M.-H. Choi, and J.-H. Park, "Waveguide-Based Binocular Maxwellian Near-Eye display Using a Single Micro-display and Polarization Grating," The 12th Korea-Japan Workshop on Digital Holography and Information Photonics (DHIP 2022), paper M3-05-KS1, Wonkwang University, Iksan, Korea, Dec. 2022. [Student Presentation Award]
- J.-H. Park, W. Han, J. Han, Y.-G. Ju, and J. Jang, "Super multi view near-eye-display using a lightguide and LED array," The 12th Korea-Japan Workshop on Digital Holography and Information Photonics (DHIP 2022), paper M1-04-KI, Wonkwang University, Iksan, Korea, Dec. 2022. [Invited]
- J.-H. Park, "Recent Progress on Optical-See-Through Near to Eye Displays with Focus Cue Support," The 20th International Display Workshops (IDW 2022), paper 3D6-1, Fukuoka International Congress Center, Fukuoka, Japan, Dec. 2022. [Invited]
- J.-H. Park, M.-H. Choi, W. Han, J. Han, and Y.-G. Ju, "Light field augmented reality near-eye displays using waveguide," The 22nd International Meeting on Information Display (IMID 2022), paper A33-3, Bexco, Busan, Korea, Aug. 2022. [Invited]
- M.-H. Choi, and J.-H. Park, "Waveguide-based binocular Maxwellian near-eye displays using a single microdisplay and polarization grating," The 22nd International Meeting on Information Display (IMID 2022), paper P1-130, Bexco, Busan, Korea, Aug. 2022.
- M.-H. Choi and J.-H. Park, "Optical See-Through Near-Eye Display for Augmented Reality with Focus Cue Support," 13th International Conference on Optics-photonics Design & Fabrication (ODF 2022), Sapporo, Japan, paper OFP3B-03, Aug. 2022. [Invited]
- W. Han, J. Han, Y.-G. Ju, and J.-H. Park, "Lightguide type optical see-through super multi-view near-eye display using digital micromirror device and LED array," Optica (formerly OSA), Digital Holography and Three-Dimensional Imaging (DH 2022), Cambridge, UK, paper Tu1A.3, Aug. 2022.
- K. Min, D. Min, and J.-H. Park, "Non-hogel-based computer-generated hologram from perspective light field," Optica (formerly OSA), Digital Holography and Three-Dimensional Imaging (DH 2022), Cambridge, UK, paper Th1A.2, Aug. 2022.
- J. Jang, M.-H. Choi, K.-S. Shin, and J.-H. Park, "Implementation of a 4-depth waveguide optical combiner using stacked volume gratings and polarization optics," Optica (formerly OSA), Digital Holography and Three-Dimensional Imaging (DH 2022), Cambridge, UK, paper Th1A.4, Aug. 2022.
- D. Min, K. Min, and J.-H. Park "Occlusion between three-dimensional scenes in light field and hologram domains using non-hogel-based computer generated hologram technique," Optica (formerly OSA), Digital Holography and Three-Dimensional Imaging (DH 2022), Cambridge, UK, paper Th2A.14, Aug. 2022.
- J.-H. Park, M.-H. Choi, K.-S. Shin, J. Jang, W. Han, and J. Han, "Near eye displays with enhanced focus cues using Maxwellian, Multi-layser, and light field technique," Optica Imaging and Applied Optics Congress, 3D Image Acquisition and Display: Technology, Perception and Applications, paper 3Th4A.2, Vancouver, British Columbia Canada, July 2022. [Invited]
- J.-H. Park, M.-H. Choi, and K.-S. Shin, "Optical-see-through augmented reality near-to-eye displays with focus cue support," Proc. SPIE PC12024, Advanceds in Display Technologies XII, PC120240B (9 March 2022); https://doi.org/10.1117/12.2607951 [Invited]
- J. Jang, and J.-H. Park, "Waveguide type floating display using holographic optical element with convergent power," Optical Architectures for Displays and Sensing in Augmented, Virtual, and Mixed Reality (AR, VR, MR) III, SPIE AR VR MR 2022, Proc. SPIE 11931, San Francisco, CA, USA, paper 11 931-41, Jan. 2022. https://doi.org/10.1117/12.2614748
- 민교식, 민다빈, 박재형, "원근 투사 영상 집합으로 표현된 라이트 필드를 사용한 논 호겔 기반 직렬연산 홀로그램 생성 기법," 한국광학회 Optics and Photonics Congress, paper T1F-III.05, 제주 ICC, 2022년 7월.
- 한웅섭, 한지윤, 박재형, "디지털 마이크로미러 디바이스와 LED어레이를 이용한 도파관 기반 초다시점 투과형 근안 디스플레이," 한국광학회 Optics and Photonics Congress, paper W1A-III.03, 제주 ICC, 2022년 7월.
- 장준영, 최명호, 신광수, 박재형, "체적 홀로그래픽 광학소자와 편광 광학소자를 이용한 4 초점면 도파관형 광결합기," 한국광학회 Optics and Photonics Congress, paper W2A-III.03, 제주 ICC, 2022년 7월.
- 신광수, 최명호, 장준영, 박재형, "기하학적 위상렌즈와 반투명 마이크로 거울 어레이를 이용한 직시형 라이트필드 근안디스플레이," 한국광학회 Optics and Photonics Congress, paper W3A-III.05, 제주 ICC, 2022년 7월.
- 민교식, 민다빈, 박재형, "스페클 영향을 고려한 홀로그램 화질 평가," 제33회 한국광학회 정기총회 및 2022 동계학술발표회, 대전컨벤션센터, 대전, paper W2C-III.02, 2022년 2월.
- 장준영, 최명호, 신광수, 한웅섭, 박재형, "굴절력을 가진 홀로그래픽 광학소자를 이용한 도파관형 플로팅 디스플레이," 제33회 한국광학회 정기총회 및 2022 동계학술발표회, 대전컨벤션센터, 대전, paper W3C-III.04, 2022년 2월.
- Mehdi Askari, 박재형, "Computer generated holographic image on an augmented reflected light microscope," 제33회 한국광학회 정기총회 및 2022 동계학술발표회, 대전컨벤션센터, 대전, paper FP-III-01, 2022년 2월.
- 최명호, 박재형, "도파관 및 편광의존 광학 소자 기반 복층 영상면을 갖는 투과형 양면 디스플레이," 제33회 한국광학회 정기총회 및 2022 동계학술발표회, 대전컨벤션센터, 대전, paper FP-III-02, 2022년 2월. [우수논문상 수상]

**2021**

- K.-S. Shin, M.-H. Choi, J. Jang, and J.-H. Park, "Waveguide-type see-through dual focus near-eye display with a polarization grating," Optics Express, vol. 29, no. 24, pp. 40294-40309 (2021). https://doi.org/10.1364/OE.444221
- D. Min, K. Min, and J.-H. Park, "Full-color non-hogel-based computer-generated hologram from light field without color aberration," Current Optics and Photonics, vol. 5, no. 4, pp. 409-420 (2021).
- D.-Y. Park, J.-H. Park, "Generation of distortion-free scaled hologram using light field data conversion," Optics Express, vol. 29, no. 1, pp. 487-508 (2021).
- D. Min, M.-H. Choi, and J.-H. Park, "Compact in-line floating display system using dihedral corner reflector array," Opt. Express 29(2), 1188-1209 (2021).
- J.-H. Park, M. Askari, D. Min, and K. Min, "Non-hogel based computer generated hologram from light field data," Three Dimensional Systems and Applications (3DSA), Online / Kwangwoon University, Seoul, Korea, paper S3-1, November 2021. [Invited]
- M.-H. Choi, and J.-H. Park, "Waveguide-type Maxwellian near-eye display for augmented reality with replicated eyebox using pin-mirror array holographic optical element," OSA FiO LS (Frontiers in Optics + Laser Science) 2021, A virtual event, paper FTh4C.2, November 2021. [Wolf Outstanding Student Paper Award]
- J.-H. Park, and D.-Y. Park, "Speckle-free reconstruction and distortion-free scaling of holographic three-dimensional images using hologram-light field conversion," Holography, Diffractive Optics, and Applications XI, SPIE Photonics Asia, Nantong, Jiangsu, China + Online, paper 11898-6, October 2021. [Invited]
- K. Min and J.-H. Park, "Binary-Encoded Full Color Hologram Using Error Diffusion for a Digital Micro-Mirror Device," The 21st International Meeting on Information Display, COEX, Seoul, Korea, paper WC3-3, August 25-27, 2021.
- J. Jang, and J.-H. Park, "Analysis of Multiplexed Holographic Optical Element with Rigorous Coupled Wave Theory," The 21st International Meeting on Information Display, COEX, Seoul, Korea, paper P7-23, August 25-27, 2021.
- W. Han, J.-M. Jeon, M.-H. Choi, and J.-H. Park, "Horizontal Field of View Enhancement of a Waveguide-Type Near-Eye-Display by Restructuring Input Image," The 21st International Meeting on Information Display, COEX, Seoul, Korea, paper P7-22, August 25-27, 2021.
- M. Askari and J.-H. park, "Analysis of the Distortion Effects in Holographic Projection Display caused by the Retroreflector Screen," OSA Imaging and Applied Optics Congress, Digital Holography and 3-D Imaging, paper JW2A.25, Virtual Event, 19 July 2021 - 23 July 2021.
- Y.-G. Ju, and J.-H. Park, "Complex field recovery from on-axis digital hologram using deep learning," OSA Imaging and Applied Optics Congress, Digital Holography and 3-D Imaging, paper DTh1D.7, Virtual Event, 19 July 2021 - 23 July 2021.
- M.-H. Choi, and J.-H. Park, "Waveguide-type optical see-through Maxwellian near-eye display with expanded eyebox using multiplexed holographic optical element and polarization gratings," OSA Imaging and Applied Optics Congress, Digital Holography and 3-D Imaging, paper DF2F.5, Virtual Event, 19 July 2021 - 23 July 2021. [Student Paper Award]
- H.-G. Choo, Y.-G. Ju, K.-J. Oh, Y. Lim, and J.-H. Park, "Hologram Reconstruction using cascaded deep learning networks," OSA Imaging and Applied Optics Congress, Digital Holography and 3-D Imaging, paper DF4C.3, Virtual Event, 19 July 2021 - 23 July 2021.
- D.-Y. Park, and J.-H. Park, "Resolution improvement and blur removal of light field data converted from hologram using deep learning," OSA Imaging and Applied Optics Congress, Digital Holography and 3-D Imaging, paper DF4C.5, Virtual Event, 19 July 2021 - 23 July 2021.
- J.-H. Park, and K. Min, "Color holographic display with reduced speckle using digital micromirror device and error diffusion," OSK-OSA-OSJ Joint Symposia, Optics and Photonics Congress 2021, paper W3B-XI.01, ICC, Jeju, July 2021. [Invited]
- B. Hellman, T. Lee, J.-H. Park, and Y. Takashima, "Gigapixel 1440-persepctive display by sub-megapixel DMD," Proc. SPIE 11765, Optical Architectures for Displays and Sensing in Augmented, Virtual, and Mixed Reality (AR, VR, MR) II, 117650M (27 March 2021); doi: 10.1117/12.2577283.
- J.-H. Park, Y.-G. Ju, M.-H. Choi, P. Liu, B. Hellman, T.L. Lee, and Y. Takashima, "Occlusion-capable AR near-to-eye display using a single digital micromirror device," Advances in Display Technologies XI, SPIE Photonics West, Online, paper 11708-14, March 2021. [Invited]
- C. Luo, B. Hellman, G. Chen, J. Rodriguez, C. Perkins, J.-H. Park, and Y. Takashima, "Single-chip DMD-based hybrid holographic beam steering for lidar," Emerging Digital Micromirror Device Based Systems and Applications XIII, SPIE Photonics West, Online, paper 11698-12, March 2021. http://dx.doi.org/10.1117/12.2577288
- 민다빈, 민교식, 박재형, "RGB 3채널에 대한 컬러 수차가 없는 논호겔 라이트필드 기반 컴퓨터 생성 홀로그램 합성," 2021년 한국방송미디어공학회 추계학술대회, Online, paper S4-01, 2021년 11월.
- 신광수, 최명호, 박재형, "편광격자를 이용해 복층 초점면을 갖는 도파관 기반 투과형 근안 디스플레이," 한국광학회 2021 하계학술발표회, Optics and Photonics Congress 2021, ICC 제주, paper M1F-III.05, 2021년 7월. [우수논문상 수상]
- 최명호, 박재형, "핀-거울 배열 홀로그래픽 광학 소자를 이용해 확장된 아이박스를 갖는 투과형 맥스웰리안 근안 디스플레이," 한국광학회 2021 하계학술발표회, Optics and Photonics Congress 2021, ICC 제주, paper M2F-III.04, 2021년 7월.
- 주연경, 박재형, "이미지센서로부터 촬영된 확산성 물체의 디지털 홀로그램의 복소 필드 복원 딥러닝 네트워크," 한국광학회 2021 하계학술발표회, Optics and Photonics Congress 2021, ICC 제주, paper MP-III.06, 2021년 7월.
- 민교식, 민다빈, 박재형, "원근 투사 영상 집합으로 표현된 라이트 필드를 사용한 논호겔 방식의 푸리에 홀로그램 생성," 한국광학회 2021 하계학술발표회, Optics and Photonics Congress 2021, ICC 제주, paper W2F-III.01, 2021년 7월.
- 박재형, "비호겔방식 라이트필드 기반 컴퓨터 생성 홀로그래피," 제32회 한국광학회 정기총회 및 2021 동계학술발표회, paper F1C-III-1, Virtual conference, 2021년 2월. [invited paper]
- 민교식, 박재형, "오차확산법을 이용한 이진화 홀로그램의 품질향상," 제32회 한국광학회 정기총회 및 2021 동계학술발표회, paper W2C-III-2, Virtual conference, 2021년 2월.
- 사하르, 박재형, "Ghost free floating volumetric image using dihedral corner reflector array and holography," 제32회 한국광학회 정기총회 및 2021 동계학술발표회, paper F2C-III-3, Virtual conference, 2021년 2월.
- 주연경, 박재형, "딥러닝을 이용한 단일 정축 디지털 홀로그램으로부터의 물체 복소 필드 복원," 제32회 한국광학회 정기총회 및 2021 동계학술발표회, paper F3C-III-3, Virtual conference, 2021년 2월.
- Askari Mehdi, 박재형, "Point spread function of a retroreflector screen in holographic projection display," 제32회 한국광학회 정기총회 및 2021 동계학술발표회, paper WP-III-9, Virtual conference, 2021년 2월.

## 과제

Projects의 진행 중 구획 13건과 완료 구획 16건이다. 시작 또는 종료 시점이 2021년 10월 22일–2026년 10월 22일 범위에 드는 과제로, 서울대 부임 전 시작하거나 이전 소속에서 수행한 과제도 포함한다. 기간과 진행 상태는 Projects 페이지 표기를 따른다.[^projects][^bio]

- 초다시점 광학계 집적 OLEDoG 마이크로 디스플레이 및 입체영상 모듈 원천기술 개발, ETRI (위탁) (기간 2025.01~2029.12; 상태 진행 중(Ongoing))
- 홀로그램 영상 서비스를 위한 Holo-TV 핵심 기술 개발, 과학기술정보통신부 (위탁) (기간 2022.01~2028.12; 상태 진행 중(Ongoing))
- Near-display processing (NDP) 기반의 테라급 라이트 필드 디스플레이 시스템 개발, 연구재단, 미래디스플레이 전략연구실지원사업 (공동) (기간 2024.04~2028.12; 상태 진행 중(Ongoing))
- 차세대 안경형 XR 기기용 경박단소 기하위상변조 메타렌즈의 초점가변 색수차 해소기술 및 고효율화/대구경화 원천기술 개발, 연구재단, 미래디스플레이 전략연구실지원사업 (공동) (기간 2024.04~2028.12; 상태 진행 중(Ongoing))
- 초경계 무한메타버스를 위한 융합현실주의적 적응시각전환 기술, 산업통상자원부 (공동) (기간 2026.01~2028.12; 상태 진행 중(Ongoing))
- 복합소재 문화유산 고품질 복원을 위한 디지털 문화유산 획득용 광학기술 및 공유 플랫폼 기술 개발, 문화체육관광부 (공동) (기간 2024.07~2027.12; 상태 진행 중(Ongoing))
- 수렴초점불일치 해결을 위한 XR 디스플레이 평가 방법 및 평가 기술 개발 (용역) (기간 2024.07~2027.12; 상태 진행 중(Ongoing))
- BK21 FOUR (정보기술 미래인재 교육연구단) (기간 2025.03~2027.08; 상태 진행 중(Ongoing))
- 무인이동체용 고속스위칭 가변 마이크로어레이 기반 2D/3D 공간정보 동시획득 기술 개발, 민군협력진흥원 (위탁) (기간 2022.06~2027.05; 상태 진행 중(Ongoing))
- 실사 객체 폐색 가능한 홀로그래픽 증강현실 3D 근안디스플레이 기술 개발, 연구재단, 기초연구사업, 중견연구 (책임) (기간 2022.03~2027.02; 상태 진행 중(Ongoing))
- VAC 개선을 위한 Maxwellian view 광학 시스템 연구, 삼성디스플레이 (기간 2024.03~2027.02; 상태 진행 중(Ongoing))
- 고정밀 RGB-Depth 정합 및 Phase Mask 변환 공간화소결상 콘텐츠 생성 기술 개발, ETRI (용역) (기간 2025.11~2026.10; 상태 진행 중(Ongoing))
- Integral imaging 3D 표시 인쇄물을 위한 multi pattern array 생성 코드 개발, 세경하이테크 (기간 2026.01~2026.03; 상태 진행 중(Ongoing))
- 초실감 메타버스 서비스를 위한 입체영상 디바이스 기술 개발, 과학기술정보통신부 (위탁) (기간 2022.01~2024.12; 상태 완료(Completed))
- 초실감 홀로그램 생성을 위한 실시간 고속 렌더러 기술 개발, 과학기술정보통신부 (공동) (기간 2021.04~2024.12; 상태 완료(Completed))
- 마이크로디스플레이 계측 시스템 개발, 산업통상자원부 (공동) (기간 2021.12~2024.11; 상태 완료(Completed))
- 라이트필드 기반 실감미디어 통합 플랫폼, 삼성전자 미래기술육성과제 (공동) (기간 2021.03~2024.08; 상태 완료(Completed))
- BK21 Four 인하대학교 산업융합형 차세대 인공지능 혁신인재 교육연구단, 연구재단 (기간 2020.09~2024.02; 상태 완료(Completed))
- 미세 패터닝 기술을 활용한 콘텐츠 복제 방지 및 홀로그램 활용 기술 개발, 문화체육관광부 (기간 2022.04~2023.12; 상태 완료(Completed))
- 광학 시뮬레이션을 이용한 디지털 HOE 홀로그램 생성용 저작도구 기술 개발, 정보통신방송 기술개발 사업 (홀로그램 핵심기술개발 사업), 과학기술정보통신부 (기간 2020.04~2023.12; 상태 완료(Completed))
- OLED 패널과 핀홀 배열을 이용한 직시형 VR 근안 디스플레이 개발, LG전 자 (기간 2023.03~2023.1 1; 상태 완료(Completed))
- 라이트필드 VR 광학 및 평가 지표 연구, LG디스플레이 (기간 2022.12~2023.11; 상태 완료(Completed))
- 홀로그램 유효성 평가, KET I (기간 2020.07~2023.11; 상태 완료(Completed))
- 홀로그램 기반의 위상 검출용 디지털 홀로그래피 메트롤로지 기술 개발, ETRI (기간 2020.06~2023.11; 상태 완료(Completed))
- 투과형 uLED 패널과 핀홀배열을 이용한 AR NED 개발, LG전자 (기간 2022.06~2022.12; 상태 완료(Completed))
- HOE기반 Waveguide 구조 및 재료에 따른 특성 분석 Tool 개발, 삼성전자 (기간 2021.10~2022.09; 상태 완료(Completed))
- 직시형 AR Glasses의 구현을 위한 광학구조 연구, LG디스플레이 (기간 2021.07~2022.06; 상태 완료(Completed))
- 하이브리드 홀로그래픽 디스플레이 원천 기술 개발, 연구재단(기초연구사업, 중견연구) (기간 2017.03~2022.02; 상태 완료(Completed))
- 모듈러 스크린의 최적 사용 경험을 위한 UI 디자인 가이드라인 도출, 삼성전자 (기간 2020.11~2021.11; 상태 완료(Completed))

## 수상과 선정

Publications의 Awards 구획 중 해당 기간 항목 29건과 소식에만 나오는 우수논문상·장학생·연구장려금 선정 6건을 합친 35건이다. 서울대 부임 전 소속 시절의 수상도 포함한다. 날짜가 연도로만 적힌 항목은 그 연도 표기를 따른다.[^pubs][^news][^home][^bio]

- 2026년 8월 · S. Kheibarihafshejani, Best Poster Paper Award, the 26rd International Meeting on Information Display (IMID2026), Busan, Korea, Aug. 2026
- 2026년 8월 · 박재형, JID 발전상 수상, 2026년 8월
- 2026년 5월 · 김민성, Distinguished Paper Award, SID Display Week 2026, 2026년 5월 (M. Kim, M.-H. Choi, and J.-H. Park, "Thin Maxwellian Virtual Reality Near-Eye Display Using Holographic Optical Element and Micro LensArray," SID Display Week 2026, paper 78.3, Los Angeles, CA, US, May 2026.)
- 2025년 12월 · 박재형, 가상증강현실 산업발전 산업통상부 장관 표창, 2025년 12월
- 2025년 8월 · Sahar Kheibarihafshejani, Journal of Information Display (JID) Distinguished Paper Award (우수논문상), 2025년 8월
- 2025년 7월 · 신민재, 한국광학회 2025년도 하계 학술발표회 (Optics and Photonics Congress 2025) 우수논문상
- 2025년 4월 · 박재형, SPIE Defense + Secruity 2025, Three-Dimensional Imaging, Visualization, and Display Fumio Okano Best Paper Award
- 2025년 · Sahar, 제36회 한국광학회 정기총회 및 2025 동계학술발표회 우수논문상 (Sahar, 박재형 "Time multiplexed foveated near-eye display with computational holography and focus tunable optics," 제36회 한국광학회 정기총회 및 2025 동계학술발표회)
- 2025년 1월 · 한규찬, 우수발표상, 1st Korean Meeting on Information Display (KMiD 2025), 한국정보디스플레이학회
- 2024년 10월 · 신광수, 2024 삼성디스플레이 산학협력논문대회 금상, 2024년 10월 (신광수, 박재형, "Enhancing field of view an angular resolution in micro lens array type VR system through polarization grating")
- 2024년 8월 · 신광수, Best Paper Award Bronze, The 24th International Meeting on Information Display (IMID 2024), Jeju, Korea, Aug. 2024
- 2024년 · 한웅섭, 한 국광학회 2024년도 하계 학술발표회 우수논문상
- 2024년 · 한규찬, 제35회 한국광학회 정기총회 및 2024 동계학술발표회 우수논문상
- 2024년 1월 · 최명호, Optical Design Challenge Finalist, SPIE AR/VR/MR
- 2023년 12월 20일 · S. Kheibarihafshejani, The 13th Japan-Korea Workshop on Digital Holography & Information Photonics (DHIP 2023), Student Presentation Award (Time multiplexing multi-view display using slit mirror array and light emitting diode illuminated digital micromirror device, Dec. 20, 2023)
- 2023년 8월 · 한웅섭, Best Poster Paper Award, the 23rd International Meeting on Information Display (IMID2023), Busan, Korea, Aug. 2023
- 2023년 · 최명호, Optics and Photonics Congress (OPC), 한국광학회 하계학술발표회 2023 우수논문상
- 2023년 8월 31일 · 박재형, 우수강사상, 제13회 KIDS Display School 디스플레이 광학 과목, 한국정보디스플레이학회, 2023년 8월 31일
- 2023년 8월 24일 · 박재형, 과학기술정보통신부장관상, 제23회 국제정보디스플레이 대상 기초원천기술부문, 2023년 8월 24일
- 2023년 8월 · 최명호, Student Paper Competition Finalist, OPTICA Imaging Congress, Boston, USA, Aug. 2023
- 2023년 2월 23일 · 한웅섭, BK21 우수연구상, presented by BK21 산업융합형 차세대 인공지능 혁신인재 연구단장, 2023년 2월 23일
- 2023년 2월 17일 · 한웅섭, Outstanding Research Award, Excellence of Journal Publication, presented by 인하대학교 대학원장, 2023 년 2 월 1 7 일
- 2023년 2월 · 민다빈, Byoungho Lee Best Student Paper Prize (formerly Optica-OSK Student Prize), presented by Optica Vice President at OSK Annual Meeting, 2023년 2월
- 2022년 12월 21일 · 최명호, The 12th Korea-Japan Workshop on Digital Holography & Information Photonics (DHIP 2022), Student Presentation Award (Waveguide-based binocular Maxwellian near-eye display using a single micro-display and polarization grating, Dec. 21, 2022)
- 2022년 9월 22일 · 박재형, 한국정보디스플레이학회 공로상, 2022년 9월 22일
- 2022년 2월 18일 · 최명호, 한국광학회 2022년도 동계 학술발표회 우수논문상
- 2022년 2월 18일 · 최명호, Outstanding Research Award, Excellence of Journal Publication, presented by 인하대학교 대학원장, 2022년 2월 18일
- 2022년 · Jae-Hyeung Park elected as a Optica (formerly OSA) Fellow 2022
- 2021년 11월 · Emil Wolf Student Paper Competition Winner 2021, Myeong-Ho Choi
- 2026년 8월 · 김민성, 삼일문화재단 장학생 선정
- 2026년 5월 · 한웅섭, Conference on Optoelectronics and Optical Communications Distinguished Paper Award(우수논문상) 수상
- 2025년 8월 · 한웅섭, 김민성, 삼일문화재단 장학생 선정
- 2025년 8월 · 한웅섭, 2025 율촌 AI 장학생 선발
- 2024년 8월 · 한웅섭, 삼일문화재단 장학생(박사) 선정
- 2024년 8월 · 김민성, 연구재단 석사과정생 연구장려금 지원 사업 선정

## 소식

2021년 11월–2026년 10월의 논문 출판·수상·선정 소식 49건이다. 서울대 부임 전 인하대학교 등 이전 소속 시절 소식도 포함한다. 날짜는 성과가 일어난 시점의 누리집 표기다.[^news][^home][^bio]

- 2026년 10월 · S. Kheibarihafshejani, Journal of Physics: Photonics 논문 출판
- 2026년 8월 · S. Kheibarihafshejani, the 26rd International Meeting on Information Display (IMID2026) 우수포스터상 수상
- 2026년 8월 · 이찬슬, 한웅섭, Optics Express 논문 출판
- 2026년 8월 · 박재형, JID 발전상 수상
- 2026년 8월 · 김민성, 삼일문화재단 장학생 선정
- 2026년 5월 · 한웅섭, Conference on Optoelectronics and Optical Communications Distinguished Paper Award(우수논문상) 수상
- 2026년 5월 · 김민성, SID Display Week Distinguished Paper Award(우수논문상) 수상
- 2025년 12월 · 박재형, 가상증강현실 산업발전 산업통상부 장관 표창
- 2025년 8월 · Sahar Kheibarihafshejani, Journal of Information Display (JID) Distinguished Paper Award (우수논문상)
- 2025년 8월 · 한웅섭, 김민성, 삼일문화재단 장학생 선정
- 2025년 7월 · 신민재, 한국광학회 2025년도 하계 학술발표회 우수논문상 수상
- 2025년 8월 · 한웅섭, 2025 율촌 AI 장학생 선발
- 2025년 4월 · 박재형, SPIE Defense + Security 2025, Three-Dimensional Imaging, Visualization, and Display Fumio Okano Best Paper Award 수상
- 2025년 7월 · 한웅섭, 이찬슬, Laser & Photonics Reviews 논문 출판
- 2025년 6월 · 민교식, 최명호, Optics express 논문 출판
- 2025년 5월 · 한지윤, 한웅섭 Optics & Laser Technology 논문 출판
- 2025년 1월 · 제1회 Korean Meeting on Information Display 2025 (KMiD 2025), 한규찬, 우수논문상 수상
- 2025년 1월 · 한규찬, Optics Express 논문 출판
- 2025년 1월 · 신광수, Optics Express 논문 출판
- 2024년 12월 · Askari, Photonics 논문 출판
- 2024년 11월 · Sahar, Journal of Information Display 논문 출판
- 2024년 8월 · 신광수, IMID Young leaders conference best paper award 동상 수상
- 2024년 9월 · 신광수, 삼성디스플레이 산학협력 논문대회 금상 수상
- 2024년 8월 · 한웅섭, 삼일문화재단 장학생(박사) 선정
- 2024년 8월 · 김민성, 연구재단 석사과정생 연구장려금 지원 사업 선정
- 2024년 7월 · 한웅섭, 한국광학회 2024년 동계학술발표회 우수논문상 수상
- 2024년 5월 · 최명호, ACS applied optical materials 리뷰 논문 출판
- 2024년 4월 · 한웅섭, 최명호, Photonics Research 논문 출판
- 2024년 3월 · 민교식, 민다빈, Optics Express 논문 출판
- 2024년 3월 · 김민성, 한웅섭, IEEE Journal of Selected Topics in Quantum Electronics 논문 출판
- 2024년 3월 · 최명호, 김민성, 신광수, IEEE Journal of Selected Topics in Quantum Electronics 논문 출판
- 2024년 2월 · 제35회 한국광학회 정기총회 및 2024 동계학술발표회, 한규찬, 우수논문상 수상
- 2023년 12월 · DHIP 2023, Sahar, 학생발표상 수상, Beppu, Japan
- 2023년 8월 · 한국광학회 Optics and Photonics Congress,최명호, 하계 학술발표회 우수논문상 수상
- 2023년 8월 · 박재형, 과학기술정보통신부장관상(제23회 국제정보디스플레이 대상 기초원천기술부문) 수상
- 2023년 8월 · The 23nd International Meeting on Information Display (IMID 2023, Busan, Korea),한웅섭, 우수포스터상
- 2023년 8월 · Optica imaging congress 2023(Boston, USA), 최명호, 학생논문 경연 결선 진출
- 2023년 2월 · 한국광학회 제34회 정기총회 및 2023 동계학술발표회,민다빈 Byoungho Lee Best Student Paper Prize 수상
- 2023년 4월 · 민교식, 민다빈, Optics Communications 논문 출판
- 2022년 12월 · The 12th Korea-Japan Joint Workshop on Digital Holography and Information Photonics (DHIP 2022), 최명호 학생발표상 수상
- 2022년 12월 · 한웅섭, 한지윤, 주연경, 장준영, Optics Express 논문 출판
- 2022년 10월 · 민다빈, 민교식, Optics Express 논문 출판
- 2022년 8월 · University of Arizona 협력 연구, Optics letters 논문 출판
- 2022년 7월 · 한웅섭, Journal of Information display 논문 출판
- 2022년 6월 · Askari, Frontier in Photonics 논문 출판
- 2022년 2월 · 최명호, 한국광학회 2022년 동계학술발표회 우수논문상 수상
- 2022년 2월 · 최명호, 인하대학교 대학원생 우수연구상 수상
- 2021년 11월 · 신광수, 최명호, 장준영 Optics Express 논문 출판
- 2021년 11월 · 최명호 Emil Wolf Outstanding Student Paper Competition 우승

## 연락과 위치

- 교수 연구실: 서울대학교 공과대학 301동 1106호[^home][^prof]
- 연구 공간: 서울대학교 공과대학 301동 1152-2호[^home]
- 교수 전화: 02-880-1825[^prof]
- 교수 이메일: jaehyeung@snu.ac.kr[^home]
[^dept]: 서울대학교 전기·정보공학부, 3차원 광공학 연구실. <https://ece.snu.ac.kr/research-faculty/research/lab?labidx=138&md=view> 관측 2026-10-26.
[^prof]: 서울대학교 전기·정보공학부, 박재형 전임교수 소개. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p897> 관측 2026-10-26.
[^home]: 3DOELAB, Home의 Research Topic, On-going Projects 및 Contact. <https://sites.google.com/view/3doelab> 관측 2026-10-26.
[^heritage]: 3DOELAB, Home의 문화유산 과제 설명. 문화재 표면 반사광의 진폭·위상 분포를 입체 형상으로 재구성하는 기술을 개발한다고 적는다. <https://sites.google.com/view/3doelab> 관측 2026-10-26.
[^people]: 3DOELAB, People의 Professor, Members 및 Alumni. <https://sites.google.com/view/3doelab/people> 관측 2026-10-26.
[^pubs]: 3DOELAB, Publications의 International Journal Papers, International Conference Papers, Domestic Journal Papers, Domestic Conference Papers, Chapters and Books, Awards, Etc. <https://sites.google.com/view/3doelab/publications> 관측 2026-10-26.
[^projects]: 3DOELAB, Projects의 Ongoing 및 Completed. <https://sites.google.com/view/3doelab/projects> 관측 2026-10-26.
[^news]: 3DOELAB, News/Events의 성과 목록. <https://sites.google.com/view/3doelab/newsevents> 관측 2026-10-26.
[^bio]: S. Kheibarihafshejani, J.-H. Park, “Time multiplexing multi-view display using slit mirror array and light emitting diode illuminated digital micromirror device”, 저자 소개. 2024년 서울대학교 부교수 부임과 이전 소속을 적는다. <https://www.researchgate.net/publication/379686996_Time_multiplexing_multi-view_display_using_slit_mirror_array_and_light_emitting_diode_illuminated_digital_micromirror_device> 관측 2026-10-26.
[^p1]: M. Kim, M.-H. Choi, J.-H. Park, Journal of the Society for Information Display 34, 254-263 (온라인 2026-04-03). <https://doi.org/10.1002/jsid.70065> 초록 기준(출판사 논문 페이지). 초록 원문 <https://sid.onlinelibrary.wiley.com/doi/full/10.1002/jsid.70065> 관측 2026-10-26.
[^p2]: W. Han, C. Lee, J.-H. Park, Laser & Photonics Reviews 19, e01052 (온라인 2025-07-05). <https://doi.org/10.1002/lpor.202501052> 초록 기준(출판사 논문 페이지). 초록 원문 <https://onlinelibrary.wiley.com/doi/full/10.1002/lpor.202501052> 관측 2026-10-26.
[^p3]: G.-C. Han, W. Han, K.-S. Shin, J.-H. Park, Optics Express 33, 1132-1147 (2025). <https://doi.org/10.1364/OE.545790> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/387268058_Multifocal_near-eye_display_with_a_vari-focal_lens_and_adjustable_aperture> 관측 2026-10-26.
[^p4]: S. Kheibarihafshejani, J.-H. Park, Optics Express 33, 5727-5745 (2025). <https://doi.org/10.1364/OE.546843> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/388191613_Multi-view_multi-focal_3D_display_using_light_source_array_and_focus_tunable_optics> 관측 2026-10-26.
[^p5]: S. Kheibarihafshejani, J.-H. Park, Journal of Optics 27 (2025). <https://doi.org/10.1088/2040-8986/adaf3b> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/388488518_Integral_imaging_3D_display_with_enhanced_depth_range_using_slit_mirror_array_and_dual_display_systems> 관측 2026-10-26.
[^p6]: S. Kheibarihafshejani, J.-H. Park, Journal of Information Display 25 (온라인 2024-04-07). <https://doi.org/10.1080/15980316.2024.2329124> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/379686996_Time_multiplexing_multi-view_display_using_slit_mirror_array_and_light_emitting_diode_illuminated_digital_micromirror_device> 관측 2026-10-26.
[^p7]: R. Kaur, B. Das, J.-H. Park, R. Kumar, Optics Express 33, 22255-22269 (2025). <https://doi.org/10.1364/OE.566713> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/391613953_Improved_color_uniformity_in_monochrome_holographic_waveguide_based_near_eye_displays> 관측 2026-10-26.
[^p8]: C. Chen 외, J.-H. Park, arXiv (온라인 2026-01-21). <https://arxiv.org/abs/2601.14766> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2601.14766> 관측 2026-10-26.

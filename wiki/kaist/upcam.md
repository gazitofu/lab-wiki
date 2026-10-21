# 초규모 광 제어 및 계측 연구실 (Ultra-Scale Photonic Control and Measurement Group, UPCaM)

**KAIST 기계공학과 · 김정원 교수**

- 분야: 저잡음 광주파수 빗(광섬유 레이저와 칩 위 마이크로 공진기), 초안정 레이저와 펨토초–아토초 정밀 타이밍·동기화, 전파천문 VLBI용 광 신호 발생과 위상 보정, 광주파수 빗 기반 반도체 계측·검사와 비행시간 측정
- 대분야: 전기전자·반도체·광학, 물리·양자
- 태그: 광 주파수 빗[^overview][^comb][^p1], 광 미세 공진기[^comb][^p1][^p2], 레이저 광원[^comb][^timing][^p4], 반도체 계측·검사[^semi][^p6], 라이다·3차원 거리 센싱[^semi][^p7], 광학 영상·현미경[^semi][^p6][^p7]
- 홈페이지: <https://upcam.kaist.ac.kr>
- 근거와 출처: [UPCaM 근거 페이지](upcam-sources.md)

> 일정한 간격의 수많은 빛 성분으로 이루어진 레이저 빛(광주파수 빗)을 잡음이 매우 낮게 만들고, 이를 써서 전기·빛 신호의 시각을 펨토초 수준으로 맞추거나 반도체 구조를 깎지 않고 정밀하게 재는 기술을 연구하는 연구실이다.[^home][^overview][^timing][^semi]

## 무엇을 연구하나

연구실은 KAIST 기계공학과 김정원 교수가 이끄는 그룹으로, 초고속 광학, 초안정 주파수 기준, 초정밀 타이밍을 양자 시스템, 정밀 계측, 극한 센싱에 쓰는 연구를 한다고 소개한다.[^home] 연구 개요는 잡음이 매우 낮은 광주파수 빗 광원을 만들고, 이를 초고속 양자 과학 시설과 전파천문 시설의 동기화부터 칩 크기의 마이크로파 포토닉스 시스템, 초고속 3차원 동역학 영상까지 시각 맞추기(타이밍)에 쓰는 것을 연구실의 일로 든다.[^overview] 광주파수 빗은 주파수가 일정한 간격으로 늘어선 수많은 빛 성분으로 이루어진 레이저 빛이며, 시간으로 보면 짧은 빛 펄스가 일정한 간격으로 이어진 펄스열이다. 펄스가 도착하는 시각이 제자리에서 흔들리는 정도를 타이밍 지터라고 하는데, 연구 페이지가 드는 여러 연구는 이 지터를 줄이고 재는 일과 이어져 있다.[^comb][^timing] 연구 페이지는 연구를 네 갈래로 나눈다.[^comb]

첫째 갈래는 **광주파수 빗: 광섬유 레이저에서 칩으로**다. 짧은 펄스를 일정한 간격으로 내는 모드 잠금 광섬유 레이저를 만들고, 그 개념을 질화규소와 실리카로 만든 칩 위의 마이크로 공진기(빛을 고리 모양 구조 안에 가두는 소자)로 넓힌다. 마이크로 공진기에서 만든 광주파수 빗(마이크로콤)의 잡음이 생기는 과정을 이해하고 제어하는 것이 주요 목표이며, 안정화된 밀리미터파 신호 발생, 두 빗을 함께 쓰는 이중 빗 분광, 빛 신호를 마이크로파로 정밀하게 바꾸는 기술도 다룬다.[^comb] 대표 논문에서는 여러 솔리톤(모양을 유지한 채 진행하는 빛 펄스)이 고르게 늘어선 상태로 마이크로콤의 펄스 반복률을 44 GHz와 66 GHz로 높이면서도 단일 솔리톤 상태의 낮은 지터가 유지되어 적분 지터가 각각 3.62 fs와 3.52 fs였고,[^p1] 지름 몇 mm의 실리카 마이크로콤을 지름 몇 cm의 광섬유 기반 타이밍 기준에 묶어 22 GHz의 초안정 마이크로파와 솔리톤 펄스를 만들었다.[^p2]

둘째 갈래는 **초안정 광신호와 정밀 타이밍**이다. 광학·마이크로파 장치를 펨토초에서 아토초 수준의 시각 정확도로 동기화하고 안정화하는 기술을 만든다. 연구 페이지는 연구실이 킬로미터 길이의 광섬유 링크에서 시간이 지나도 어긋나지 않는 타이밍 동기화를 개척했다고 적고, 이 기술이 초고속 전자 회절(UED, 짧은 전자 펄스로 원자 배열의 빠른 변화를 찍는 장치), X선 광원, 가속기 시설에서 레이저와 마이크로파 발진기를 맞추는 데 쓰인다고 설명한다. 광섬유 기준이나 원자 전이(원자가 정해진 주파수의 빛을 흡수·방출하는 현상)에 맞춰 안정화한 선폭이 매우 좁은 레이저도 만들어, 10의 −15제곱 수준에 가까운 주파수 안정도를 얻었다고 소개한다.[^timing] 대표 논문에서는 광주파수 빗에서 뽑은 광전류 펄스를 칩 안 클록 분배망(칩의 모든 회로에 같은 박자 신호를 나눠 주는 배선)에 넣어 CMOS 칩의 클록을 펨토초 정밀도로 분배했고,[^p3] 1 km 광섬유를 기준으로 삼아 진공 장치 없이 레이저 주파수 불안정도를 6.3×10⁻¹⁵까지 낮춘 장치를 휴대할 수 있는 상자에 넣었다.[^p4]

셋째 갈래는 **시공간 계측과 전파천문**이다. 초안정 광 기술을 과학 시설과 천문 관측의 시간·주파수 계측에 쓰며, 대표적인 일은 한국 VLBI 관측망(Korean VLBI Network, KVN)에 광주파수 빗 시스템을 넣는 것이다. 멀리 떨어진 전파망원경들을 하나로 묶어 관측하는 초장기선 전파 간섭계(VLBI)에 필요한 위상 기준을 위해 W 대역 이상까지 이어지는 넓은 대역의 RF 빗을 만들어 위상 보정(PCAL) 시스템을 개발한다.[^astro] 대표 논문에서는 수소 메이저(원자 시계의 한 종류)로 안정화한 광 펄스를 타이밍을 안정화한 광섬유로 망원경 수신기까지 보내 RF 신호를 만들고, 시험 관측에서 VLBI 간섭무늬를 검출했다.[^p5]

넷째 갈래는 **반도체 계측과 검사**다. 광주파수 빗의 높은 시간 정밀도를 반도체 제조와 산업 검사에 옮겨, 빛이 갔다 돌아오는 시간으로 거리를 재는 비행시간(TOF) 측정을 나노미터 이하, 옹스트롬 단위 분해능까지 끌어올리고, 3차원 집적회로(칩 여러 층을 쌓은 회로)와 실리콘 관통 전극(TSV, 쌓은 칩을 위아래로 잇도록 실리콘을 뚫어 금속을 채운 통로), 여러 층으로 된 광소자를 깎지 않고 재는 비파괴 계측을 개발한다. 신호 처리와 기계학습을 함께 쓰고, 나노 구조의 빠른 움직임과 여러 지점을 한꺼번에 찍는 영상 방법도 연구한다.[^semi] 대표 논문에서는 실리콘을 통과하는 적외선 광주파수 빗으로 웨이퍼 뒷면에서 두께와 굴절률을 함께 재고 상용 메모리 제품의 구리 TSV 깊이를 측정했고,[^p6] 1000개가 넘는 지점의 비행시간 변화를 한 번에 재는 라인 스캔 TOF 카메라로 미세 소자의 구조와 움직임을 찍었다.[^p7]

## 주요 연구 주제

### 1. 광주파수 빗: 광섬유 레이저에서 칩으로

저잡음 모드 잠금 광섬유 레이저, 질화규소·실리카 마이크로 공진기의 마이크로콤과 그 지터, 안정화된 밀리미터파 발생과 이중 빗 분광.[^comb][^p1][^p2] 대표 논문 1, 2.

### 2. 초안정 광신호와 정밀 타이밍

킬로미터 길이 광섬유 링크의 타이밍 동기화, 초고속 전자 회절 장치의 레이저·마이크로파 동기화, 광섬유 기준·원자 기준 초안정 레이저, 칩 안 광 클록 분배.[^timing][^p3][^p4] 대표 논문 3, 4.

### 3. 시공간 계측과 전파천문

한국 VLBI 관측망(KVN)의 광주파수 빗 기반 신호 발생과 위상 보정, 장거리 시간·주파수 전송의 한계 연구.[^astro][^p5] 대표 논문 5.

### 4. 반도체 계측과 검사

광주파수 빗 기반 비행시간 측정, 3차원 집적회로와 실리콘 관통 전극의 비파괴 계측, 기계학습을 쓴 다층 구조 두께 측정, 나노 구조의 빠른 움직임 영상.[^semi][^p6][^p7] 대표 논문 6, 7.

## 대표 논문

랩 Journal Publication 페이지의 2021–2026년 논문 가운데 김정원 교수가 교신 저자(\*)이자 마지막 저자인 것을 중심으로 네 갈래를 고르게 담도록 골랐고, 연구 페이지가 갈래별 대표 논문으로 드는 논문을 우선했다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2026 | [Preserving ultralow timing jitter in microcombs with repetition-rate multiplication via perfect soliton crystal formation](https://doi.org/10.1364/optica.581054) · Optica | 마이크로콤은 펄스 반복률이 높고 타이밍 지터가 매우 낮은 광 펄스열을 만들 수 있다. 실리카 마이크로콤은 빛을 오래 가두는(Q값이 매우 높은) 공진기 덕분에 마이크로파 반복률에서 지터가 뛰어나지만, 공진 주파수 사이 간격(FSR)을 밀리미터파 영역으로 넓히면 지터가 나빠진다. 여러 솔리톤이 고르게 늘어선 완전 솔리톤 결정(PSC)은 저잡음 성질을 지킬 가능성을 남긴 채 반복률을 몇 배로 높이는 방법이지만 그 지터는 체계적으로 연구되지 않았다. 헤테로다인 광섬유 간섭계(두 빛을 섞어 차이 주파수로 재는 장치)로 실리카 공진기의 PSC 지터를 재어, 단일 솔리톤 상태의 초저 지터가 2-FSR·3-FSR PSC에서도 유지되어 44 GHz와 66 GHz 반복률에서 적분 지터가 각각 3.62 fs와 3.52 fs임을 보였다. 저잡음 밀리미터파 발생, 고속 데이터 변환기, 정밀 타이밍 분배, 계측에 응용할 수 있다.[^p1] | 1저자 C. Ahn, 마지막 저자 김정원(교신) |
| 2 | 2022 | [Ultrastable microwave and soliton-pulse generation from fibre-photonic-stabilized microcombs](https://doi.org/10.1038/s41467-022-27992-8) · Nature Communications | 마이크로콤은 칩 크기 소자로 저잡음 마이크로파를 만들 수 있는 후보다. 더 넓은 주파수 범위와 더 긴 시간에 걸쳐 잡음을 낮추려면 더 안정한 기준 광원에 묶어야 하는데, 광 공동을 쓰는 초안정 기준은 대개 크고 정렬에 민감하고 비싸서 칩 크기의 장점을 잃는다. 지름 몇 mm의 실리카 마이크로콤과 지름 몇 cm의 광섬유 기반 타이밍 기준을 결합해 작고 위상 잡음이 낮은 마이크로파와 솔리톤 펄스를 만들었다. 22 GHz 마이크로파의 위상 잡음은 1 kHz에서 −110 dBc/Hz(100 Hz에서 −88 dBc/Hz)였고 1초 안 주파수 불안정도는 10⁻¹³ 수준이었다. 손바닥 크기 이하로 포장한 시스템의 가능성을 보였다.[^p2] | 공동 1저자 D. Kwon·D. Jeong, 마지막 저자 김정원(H. Lee와 공동 교신) |
| 3 | 2023 | [Femtosecond-precision electronic clock distribution in CMOS chips by injecting frequency comb-extracted photocurrent pulses](https://doi.org/10.1038/s41467-023-38122-3) · Nature Communications | 클록 분배망(CDN)은 칩 안 모든 회로 블록에 같은 박자의 클록 신호를 주는 요소이고, 칩 성능을 높이려면 지터, 스큐(회로마다 신호가 도착하는 시각 차이), 발열이 더 낮아야 한다. 기존 방식은 클록을 전압 신호로 나눠 주어 클록 구동기 때문에 지터·스큐·발열이 커졌다. 광주파수 빗에서 뽑은 광전류 펄스를 구동기 없는 클록 분배망에 넣어 전자 클록을 펨토초 정밀도로 분배했다. 빗의 초저 지터, 구동기 없는 여러 금속 그물 배선, 능동 스큐 제어를 결합해 CMOS 칩의 기가헤르츠 클록에서 펨토초 수준의 칩 내 지터와 스큐를 얻었고, 3차원 집적회로를 포함한 고성능 집적회로에 광주파수 빗으로 고품질 클록을 나눠 줄 가능성을 보였다.[^p3] | 공동 1저자 M. Hyun·H. Chung, 마지막 저자 김정원(H. Chung과 공동 교신) |
| 4 | 2025 | [10^-15-level laser stabilization down to fiber thermal noise limit using self-homodyne detection](https://doi.org/10.1364/ol.541281) · Optics Letters | 자기 호모다인 검출(레이저 자신의 빛을 섞어 주파수 변화를 읽는 방법)로 1550 nm 연속파 레이저를 1 km 광섬유 지연선에 맞춰 안정화해, 16 ms 평균 시간에서 주파수 불안정도 6.3×10⁻¹⁵를 얻었다. 이 결과는 광섬유의 열잡음이 한계를 정하며 진공 장치 없이 얻은 것이라 실험실 밖에서 쓰는 초안정 레이저의 가능성을 보인다. 수동 광섬유 부품 몇 개와 균형 광검출기 하나만 써서 안정화 과정을 단순하게 하면서 성능을 유지했고, 광학 장치 전체를 휴대할 수 있는 밀폐 금속 상자에 넣었다.[^p4] | 1저자 I. Jeon, 마지막 저자 김정원(교신) |
| 5 | 2026 | [Optical frequency comb integration in radio telescopes: advancing signal generation and phase calibration](https://doi.org/10.1038/s41377-025-02056-w) · Light: Science & Applications | 초장기선 전파 간섭계(VLBI)는 수백에서 수천 km 떨어진 망원경들로 가상의 망원경을 합성해 천문학과 측지학에서 높은 각분해능으로 관측한다. 기기의 위상을 안정하게 지키려면 천체 전파 신호를 낮은 주파수로 바꾸는 원자 기준 RF 국부 발진기(LO) 신호와 위상 보정용 RF 빗 신호가 필요한데, 관측 주파수가 높아지고 대역이 넓어지면 기존 전자 방식으로는 신호 품질을 지키기 어렵다. 광주파수 빗으로 저잡음·원자 기준 RF 빗과 RF-LO 신호를 만들어 VLBI 망원경에 나눠 줄 수 있음을 보였다. 수소 메이저로 안정화한 광 펄스를 타이밍 안정화 광섬유 링크로 관측동에서 망원경의 VLBI 수신기까지 보내 광검출로 필요한 RF 신호를 만들었고, VLBI 시험 관측에서 간섭무늬를 검출하고 위상 보정에 맞는 형식으로 RF 빗 특성을 뽑아냈다.[^p5] | 공동 1저자 M. Hyun·C. Ahn, 마지막 저자 김정원(교신) |
| 6 | 2025 | [Backside illumination-enabled metrology and inspection inside 3D-ICs using frequency comb-based chromatic confocal and spectral interferometry](https://doi.org/10.37188/lam.2025.074) · Light: Advanced Manufacturing | 반도체 소자가 작고 촘촘하고 고도로 집적될수록 빛으로 소자를 깎지 않고 검사하는 기술이 중요해진다. 기존 검사는 소자를 앞면에서 보는데, 미세하고 깊은 구조가 많은 고집적 소자에서는 빛의 산란과 낮은 신호 대 잡음비가 문제이고, 빛이 금속 속으로 깊이 들어가지 못해 구리를 채운 실리콘 관통 전극(TSV)의 깊이는 잴 수 없다. 실리콘을 통과하는 1560 nm 적외선 광주파수 빗에 색공초점 현미경(색마다 초점 거리가 다른 점을 이용해 높이를 재는 현미경)과 분광 간섭계를 결합해 뒷면에서 실리콘을 검사하는 방법을 보였다. 534.2 μm 실리콘 웨이퍼의 두께와 굴절률을 약 14 μm 공간 분해능과 72.3 nm 반복도로 함께 쟀고, 상용 메모리 제품의 구리 TSV 깊이를 개별 TSV와 TSV 배열에서 처음 측정했다고 보고했다.[^p6] | 1저자 H. Choi, 마지막 저자 김정원(교신) |
| 7 | 2023 | [Massively parallel electro-optic sampling of space-encoded optical pulses for ultrafast multi-dimensional imaging](https://doi.org/10.1038/s41377-023-01077-7) · Light: Science & Applications | 미세·나노 소자의 구조와 기계적 움직임을 연구하려면 표면 모양을 빠르고 정밀하게 찍어야 한다. 특히 기계 공진기의 비조화 진동처럼 비선형적이고 순간적이고 복잡한 움직임이 나타나면서, 깊이·옆 방향 분해능과 속도, 측정 범위가 더 높은 실시간 표면 변형 영상이 필요해졌지만 이를 실시간으로 잡기는 어려웠다. 광주파수 빗을 이용한 전기광학 샘플링(빛 펄스로 신호의 순간값을 읽는 방법)으로 1000개가 넘는 공간 좌표의 비행시간 변화를 동시에 재는 라인 스캔 TOF 카메라를 만들어, 초당 수억 화소의 속도와 나노미터 이하 깊이 분해능을 수 mm 시야에서 얻었다. 이 성능으로 3차원 소자와 기계 공진기의 복잡한 구조와 움직임을 빠르고 정밀하게 찍을 수 있다.[^p7] | 1저자 Y. Na, 마지막 저자 김정원(교신) |

## 교수와 전문 분야

김정원 교수는 서울대 전기공학 학사(1999, Summa Cum Laude)를 받은 뒤 대전의 FiberPro Inc에서 개발 엔지니어(1999–2002)로 일했고, MIT 전기공학·컴퓨터과학과에서 석사(SM, 2004)와 박사(2007)를 받았다. MIT RLE 박사후연구원(Postdoctoral Associate, 2007–2009)을 거쳐 2009년 KAIST 기계공학과 조교수가 됐고, 부교수(2012–2020)를 지나 2021년부터 교수다. 2013년에는 독일 가르힝의 MPQ LAP 방문 과학자(Visiting Scientist)였다.[^pi] 랩 PI 페이지는 직함을 기계공학과 교수(Professor of Mechanical Engineering)와 반도체시스템공학과 겸임교수(Adjunct Professor of Semiconductor System Engineering)로 적는다.[^pi] 기계공학과 교수 소개는 연구 분야를 Advanced lasers, Time-of-flight sensors and imaging, Timing and synchronization, Semiconductor metrology로 들고,[^meprof] 기계공학과 연구 분야 페이지는 김정원 교수를 헬스케어/나노/광학 분야 핵심교수(연구주제 Advanced laser engineering, Sensors and imaging, Industrial laser metrology)와 소재/역학/제조 분야 참여교수(Semiconductor device metrology, Semiconductor process inspection)로 싣는다.[^me-hno][^me-mmm]

학회 활동으로는 Optica(옛 미국광학회 OSA) 펠로(2023년부터), IEEE 시니어 회원(2012년부터), IEEE Photonics Society Distinguished Lecturer(2024)가 있고, 학술지 Optics Letters의 Topical Editor(2022년부터)와 Scientific Reports 편집위원(2016년부터)을 맡고 있다. 한국광학회(Optical Society of Korea, OSK)에서는 Director of Academic Affairs(2021–2022)와 Senior Director of Academic Affairs(2023–2024)를 지냈다.[^pi] PI 페이지에 적힌 수상으로는 한국광학회 Laser Science Award(2024), 과학기술정보통신부 이달의 과학기술인상(Scientist of the Month Award, 2020), 한국광학회 Haelim Photonics Award(2018), KAIST 기계공학과 Outstanding Teaching Award(2010, 2018), KAIST Technology Innovation Award(2015), KAIST 10대 연구 성과(Top 10 Research Accomplishments of KAIST, 2016), Ewon Endowed Chair Professorship(2012–2015)이 있다.[^pi] 기술 자문으로는 Menlo Systems USA(2009), 삼성전자(2021), 국방과학연구소(2022), Kohyoung Technology(2024)를 적었다.[^pi]

논문으로 보면 전문 분야는 세 갈래로 정리된다. 하나는 잡음이 매우 낮은 광섬유 레이저와 칩 위 마이크로콤으로 펄스의 타이밍 지터를 줄이고 재는 일이다.[^p1][^p2] 둘째는 광주파수 빗으로 전자 회로의 클록, 레이저 주파수, 전파망원경의 기준 신호처럼 서로 다른 장치의 시각과 주파수를 정밀하게 맞추는 일이다.[^p3][^p4][^p5] 셋째는 이 시간 정밀도를 비행시간 측정과 간섭계로 옮겨 반도체 구조와 미세 소자의 움직임을 깎지 않고 재는 일이다.[^p6][^p7] PI 페이지의 대표 논문 목록은 2008년 원격 광·마이크로파 광원의 드리프트 없는 펨토초 타이밍 동기화(Nature Photonics)와 2010년 아토초 정밀도 초고속 광학 리뷰(Laser & Photonics Reviews)부터 시작한다.[^pi]

## 응용 분야

연구 개요는 연구 결과가 양자 기술(휴대용 양자 시간 센서를 위한 칩 위 주파수 합성기, 양자 통신 링크의 타이밍), 정보통신·인공지능(칩 위 광 클록 분배와 데이터 변환기), 국방(광 기반 레이더), 반도체 제조(반도체 소자 제조 공정의 센싱과 영상) 같은 산업에 쓰이고 있다고 소개한다.[^overview] 진행 중인 과제로는 마이크로콤 기반 밀리미터파 발생기, VLBI 망원경용 광 신호 발생과 위상 보정, 양자 시간 센서용 집적 광 주파수 합성기, 라이다, TGV 유리 기판 계측(LG이노텍 지원), OLED 유리의 응력·결함 검출(LG디스플레이 지원), 펨토초 레이저 기반 반도체 웨이퍼 계측(삼성전자 지원)이 있다.[^overview] 대표 논문으로 보면 저잡음 밀리미터파 발생과 고속 데이터 변환기,[^p1] 칩 안 클록 분배,[^p3] 실험실 밖에서 쓰는 초안정 레이저,[^p4] 전파천문 관측,[^p5] 3차원 집적회로 검사에 닿아 있다.[^p6] PhDs 칸 졸업생의 현재 자리(Current Position)로는 삼성전자(5명), 한국기계연구원(2명), 한국표준과학연구원, 한국전기연구원, 국방과학연구소가 적혀 있고, Post-docs 칸 5명의 현재 자리는 모두 대학 교수(Professor, Associate Professor, Assistant Professor)다.[^alumni]

## 구성원

2026년 10월 21일 랩 Researchers 페이지 기준이다. Postdoctoral Researchers, Graduate Student Researchers, Undergraduate Student Researchers 칸의 구성원이며, 과정과 시작 시점, 연구 주제("Working on" 줄)는 랩 표기다.[^researchers] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Dr. Changmin Ahn 안창민 | 박사후연구원 | Mar 2025 | Working on atomic-referenced portable optical and microwave/mm-wave frequency synthesizers | 1, 4, 5, 7 |
| Jinho Bae 배진호 | 석박사통합과정 | Mar 2021 | Working on optical sensors for semiconductor manufacturing processes |  |
| Hyoungsu Choi 최형수 | 박사과정 | Sep 2023 | Working on comb-based industrial imaging and metrology | 6 |
| Jihoon Baek 백지훈 | 박사과정 | Mar 2025 | Working on comb-based vibration and micro/nano-mechanical sensors | 5 |
| Junyong Choi 최준용 | 박사과정 | Mar 2025 | Working on ultralow-jitter microcombs and optoelectronic synchronization | 1, 5 |
| Euisang Ryu 류의상 | 석사과정 | Mar 2025 |  |  |
| Joonhyeong Kim 김준형 | 석사과정 | Mar 2026 |  |  |
| Thi Minh Thu Le | 석사과정 | Mar 2026 |  |  |
| Changsun Ka 가창순 | 석사과정 | Sep 2026 |  |  |
| Jonghyun Kwon 권종현 | 학부 연구생 | Jun 2024 | Working on time-stretched TOF detection |  |

## 졸업생과 이전 구성원

랩 Alumni 페이지의 34명(PhDs 11, Masters 8, Post-docs 5, Visiting Researchers and Undergraduate Students 10)이다. 과정 칸은 랩이 적은 칸 이름과 연구실에서의 과정·기간이고, 진로 칸은 랩이 적은 현재 자리(Current Position) 또는 경력 줄이다. 이름 앞의 Dr.는 랩 표기 그대로다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Dr. Kwangyun Jung 정광연 | PhDs: Master-PhD Student @ UPCaM [Feb 2010 - Dec 2015] | Research Professor at Nagoya University (Nagoya, Japan) [Sep 2022-Aug 2023]; Senior Researcher at KIMM (Daejeon, Korea) [May 2019-Aug 2022]; Senior Engineer at Samsung Electro-Mechanics Co. Ltd. (Suwon, Korea) [April 2017-April 2019]; Research Associate at SYRTE (Paris, France) [Mar 2016 - Mar 2017] |
| Dr. Chur Kim 김철 | PhDs: Master-PhD Student @ UPCaM [Feb 2011 - Dec 2016] | Current Position: Senior Researcher at Korea Electrotechnology Research Institute (KERI, 한국전기연구원, Advanced Medical Device Research Division, Ansan, Korea, Jan 2017-) |
| Dr. Heewon Yang 양희원 | PhDs: Master-PhD Student @ UPCaM [Feb 2011 - Dec 2017] | Current Position: Senior Engineer at Samsung Electronics Co. Ltd. (Foundry Manufacturing Center, Giheung, Korea, Mar 2018-) |
| Dr. Dohyun Kim 김도현 | PhDs: Master-PhD student @ UPCaM [Mar 2014 - Nov 2019] | Current Position: Senior Researcher at Korea Institute of Machinery and Materials (KIMM, 한국기계연구원, Department of Laser and Electron Beam Application, Daejeon, Korea, December 2019-) |
| Dr. Chan-Gi Jeon 전찬기 | PhDs: Master-PhD student @ UPCaM [Mar 2014 - Jan 2020] | Current Position: Senior Engineer at Samsung Electronics Co. Ltd. (Memory Manufacturing Technology Center, Hwaseong, Korea, Feb 2020-) |
| Dr. Junho Shin 신준호 | PhDs: Master-PhD student @ UPCaM [Mar 2013 - Feb 2020] | Current Position: Senior Engineer at Samsung Electronics Co. Ltd. (Manufacturing Technology Center, Hwaseong, Korea, Dec 2021-); Postdoctoral Researcher at KAERI (Daejeon, Korea) [Mar 2020-Nov 2021] |
| Dr. Dohyeon Kwon 권도현 | PhDs: Master-PhD student @ UPCaM [Mar 2015 - Feb 2021] | Current Position: Senior Researcher at Korea Research Institute of Standards and Science (KRISS, 한국표준과학연구원, Climate Watch and Hydrogen Quality Metrology Team, Daejeon, Korea, April 2021-) |
| Dr. Hyunsoo Kwak 곽현수 | PhDs: Master-PhD student @ UPCaM [Mar 2016 - Feb 2023] | Current Position: Senior Engineer at Samsung Electronics Co. Ltd. (Memory Manufacturing Technology Center, Hwaseong, Korea, Mar 2023-) |
| Dr. Yongjin Na 나용진 | PhDs: Master-PhD student @ UPCaM [Mar 2017 - Feb 2023] | Current Position: Senior Engineer at Samsung Electronics Co. Ltd. (Semiconductor R&D Center, Hwaseong, Korea, April 2023-) |
| Dr. Minji Hyun 현민지 | PhDs: Master-PhD student [Mar 2018 - Feb 2024]; Postdoctoral Researcher [Mar 2024 - Aug 2024] | Current Position: Senior Researcher at Agency for Defense Development (ADD, 국방과학연구소, Daejeon, Korea, Oct 2024-) |
| Dr. Igju Jeon 전익주 | PhDs: Master-PhD student [Sep 2017 - Feb 2025]; Postdoctoral Researcher [Mar 2025 - Jul 2025] | Current Position: Senior Researcher at Korea Institute of Machinery and Materials (KIMM, 한국기계연구원, Department of Laser and Electron Beam Application, Daejeon, Korea, Aug 2025-) |
| Dr. Suhyeon Park 박수현 | Masters: Master student @ UPCaM [Sep 2010 - Jul 2012] |  |
| Dr. Hyoji Kim 김효지 | Masters: Master student @ UPCaM [Sep 2011 - Aug 2013] |  |
| Jiseok Lim 임지석 | Masters: Master student @ UPCaM [Feb 2012 - Jun 2014] |  |
| Sangho Bae 배상호 | Masters: Master student @ UPCaM [Mar 2013 - Dec 2014] |  |
| Dr. Jinho Kang 강진호 | Masters: Master student @ UPCaM [Mar 2013 - Dec 2014] |  |
| Jaegoan Lee 이재관 | Masters: Master student @ UPCaM [Mar 2017 - Dec 2018] |  |
| Myeong-chan Park 박명찬 | Masters: Master student @ UPCaM [Sep 2021 - Jun 2023] |  |
| Woosong Jeong 정우송 | Masters: Master student [Mar 2024 - Feb 2026] |  |
| Dr. Youjian Song | Post-docs: BK21 Postdoctoral Researcher @ UPCaM [Feb 2010 - Jun 2011] | Current Position: Professor at Tianjin University (Tianjin, China) |
| Dr. Dong Hou | Post-docs: Visiting Researcher @ UPCaM [Nov 2015 - Jan 2016] | Current Position: Associate Professor at University of Electronic Science and Technology of China (UESTC, Chengdu, China) |
| Dr. Shuangyou Zhang | Post-docs: BK21 Postdoctoral Researcher @ UPCaM [Aug 2016 - Aug 2017] | Current Position: Assistant Professor at Technical University of Denmark (DTU, Lyngby, Denmark) |
| Dr. Xiao-Zhou Li | Post-docs: Postdoctoral Researcher @ UPCaM [Oct 2018 - Mar 2019] | Current Position: Associate Professor at Dalian University of Technology (Dalian, China) |
| Dr. Ziye Wang | Post-docs: Postdoctoral Researcher @ UPCaM [Nov 2022 - Nov 2023] | Current Position: Assistant Professor at Jiangsu University of Science and Technology |
| Dr. Yeonjoon Cheong 정연준 | Visiting Researchers and Undergraduate Students: Undergraduate Researcher @ UPCaM [Mar 2014 - Jun 2015] |  |
| Dr. Peng Qin | Visiting Researchers and Undergraduate Students: Visiting student researcher @ UPCaM [Oct 2012 - Jan 2013] |  |
| Dr. Jieun Bae 배지은 | Visiting Researchers and Undergraduate Students: URP Researcher @ UPCaM [Dec 2015 - Jun 2016] |  |
| Dr. Xing Lu | Visiting Researchers and Undergraduate Students: Visiting PhD student researcher @ UPCaM [Mar 2017 - Sep 2017] |  |
| Dr. Juan Wei | Visiting Researchers and Undergraduate Students: Visiting PhD student researcher @ UPCaM (supported by CSC fellowship) [Nov 2016 - Oct 2017] |  |
| Suil Cho 조수일 | Visiting Researchers and Undergraduate Students: Visiting Researcher (from Samsung Electronics) [Jun 2017 - May 2018] |  |
| Chan-Hyeok Kwon 권찬혁 | Visiting Researchers and Undergraduate Students: Undergraduate Researcher [Jun 2022 - Aug 2022] |  |
| Dr. Hui Yang | Visiting Researchers and Undergraduate Students: CSC Scholarship-Supported Visiting Researcher [Nov 2021 - Oct 2022] |  |
| Seunghyun Oh 오승현 | Visiting Researchers and Undergraduate Students: Undergraduate Researcher [Jun 2022 - Aug 2022] |  |
| Jeewoo Kang 강지우 | Visiting Researchers and Undergraduate Students: Undergraduate Intern (MIT-Korea Program) [Jun 2024 - Aug 2024] |  |

## 최근 논문 목록 (2021–2026)

랩 Journal Publication 페이지의 2021년 이후 32편(목록 번호 65–96)이다. 93–96번은 랩이 제출일과 함께 올린 제출 원고다. 저자 이름 뒤 *는 교신 저자, ^는 공동 1저자를 뜻하는 랩 표기다.[^papers]

**2026**

- J. Bae, M. Hyun, J. Hong, K. Ko, Y. Jeon, Y. Park, and J. Kim\*. "Single-shot reflectometric monitoring of silicon melting in nanosecond laser annealing". *Submitted on August 14, 2026 (2026)*.
- S. Park, I. Jeon, M. Kim, C. Lee, K. Ko, D. Suk, J. Kim, H. Lee\*. "Near-pump-level relative intensity noise of dispersive waves in on-chip supercontinuum generation". *Submitted on August 6, 2026; opticaopen.33174038 (2026)*.
- C. Ahn^, H. Jeong^, S. Yang, J. Choi, I. Jeon, H. Moon\*, J. Kim\*. "Atomic-referenced Hz-linewidth lasers via fiber interferometric stabilization". *Submitted on July 29, 2026; arXiv:2605.26427 (2026)*.
- K. Twayana, F. Lei, J. Choi, J. Kim, V. Torres-Company\*. "Self-stabilization of microcombs". *Submitted on July 22, 2026; arXiv:2607.19614 (2026)*.
- S. Nam^, J. H. Kim^, Y. J. Park, D. Choi, D. U. Kim, N. Guezzi, S. Lee, Y. Seo, S. Choi, M. Kim, H. Seong, C. Lee, C. Ahn, J. Kim\*, J. Yu\*, S. Han\*. "Silicon photonic MEMS platform-based air-coupled optomechanical ultrasound receiver at 2.8 MHz with an ultra-compact active acoustic sensing area". *Photonics Research 14, 3802-3817 (2026)*.
- C. Ahn, J. Choi, D. Suk, H. Lee, and J. Kim\*. "Optical-to-microcomb stability transfer for ultrastable timing and microwave/milimeter-wave generation". *Laser & Photonics Reviews 20, e71135 (2026)*.
- C. Ahn, J. Choi, D. Suk, M. Kim, H. Lee, and J. Kim\*. "Preserving ultralow timing jitter in microcombs with repetition-rate multiplication via perfect soliton crystal formation". *Optica 13, 717 (2026)*.
- M. Hyun^, C. Ahn^, J. Choi, J. Baek, W. Jeong, D. Je, D. Byun, J. Wagner, M. Heo, T. Jung, and J. Kim\*. "Optical frequency comb integration in radio telescopes: advancing signal generation and phase calibration". *Light: Science & Applications 15, 53 (2026)*.

**2025**

- Y. Na, J. Suh, and J. Kim\*. "Frequency comb-based time-domain tracking of AFM cantilever dynamics from picometre-scale noise to micron-scale nonlinear motion". *PhotoniX 6, 36 (2025)*.
- H. Choi, H. Kwak, S. Ryu, Y. Sohn, and J. Kim\*. "Backside illumination-enabled metrology and inspection inside 3D-ICs using frequency comb-based chromatic confocal and spectral interferometry". *Light: Advanced Manufacturing 6, 74 (2025)*.
- Z. Wang\*^, J. Baek^, C. Ahn, D. Suk, H. Lee, and J. Kim\*. "FPGA-driven soliton locking for reduced manual intervention in microcombs". *Journal of Lightwave Technology 43, 9270-9275 (2025)*.
- J. Kim\*. "(Invited Review) Optical frequency combs and their applications in timing and synchronization". *Korean Journal of Optics and Photonics 36, 1-11 (2025)*.
- I. Jeon, W. Jeong, C. Ahn and J. Kim\*. "10^-15-level laser stabilization down to fiber thermal noise limit using self-homodyne detection". *Optics Letters 50, 1057-1060 (2025)*.

**2024**

- S. Pan, J. McKinney, A. Bogoni, and J. Kim. "Guest editorial for the special issue on microwave photonics". *Journal of Lightwave Technology 42, 7431-7433 (2024)*.
- J. Bae, M. Hyun, D. Kim, X. Mateos, J. G. Ajates, C. Romero, J. R. V. De Aldana, J. Kim\*, and F. Rotermund\*. "Characterization of noise spectra in low-jitter GHz mode-locked fs-laser-inscribed waveguide lasers". *Optics and Laser Technology 179, 111412 (2024)*.
- Z. Wang\*, I. Jeon, C. Ahn, and J. Kim\*. "Narrow linewidth, arbitrarily tuning DFB laser using 3x3 optical coupler-based fully digital feedback". *Journal of Lightwave Technology 42, 3820-3825 (2024)*.

**2023**

- I. Jeon, C. Ahn. C. Kim, S. Park, W. Jeon, L. Duan, and J. Kim\*. "Palm-sized, vibration-insensitive and vacuum-free all-fiber-photonic module for 10-14-level stabilization of CW lasers and frequency combs". *APL Photonics 8, 120804 (2023)*.
- M. Hyun, C. Ahn, Y. Bae, J. Cho, and J. Kim\*. "Femtosecond-resolution optical pulse interleaving time error detector". *Optics Letters 48, 6472-6475 (2023)*.
- H. Yang^, C. Ahn^, I. Jeon, D. Suk, H. Lee, and J. Kim\*. "Synchronization of a silica microcomb to a mode-locked laser with a fractional optoelectronic phase-locked loop". *Current Optics and Photonics 7, 557-561 (2023)*.
- H. Kwak and J. Kim\*. "(Invited Review) Semiconductor multilayer nano-metrology with machine learning". *Nanomanufacturing and Metrology 6, 15 (2023)*.
- M. Hyun^, H. Chung^\*, W. Na, and J. Kim\*. "Femtosecond-precision electronic clock distribution in CMOS chips by injecting frequency comb-extracted photocurrent pulses". *Nature Communications 14, 2345 (2023)*.
- Y. Na, H. Kwak, C. Ahn, S. Lee, W. Lee, C.-S. Kang, J. Lee, J. Suh, H. Yoo, and J. Kim\*. "Massively parallel electro-optic sampling of space-encoded optical pulses for ultrafast multi-dimensional imaging". *Light: Science & Applications 12, 44 (2023)*.
- C. Ahn, Y. Na, and J. Kim\*. "Dynamic absolute distance measurement with nanometer-precision and MHz acquisition rate using a frequency comb-based combined method". *Optics and Lasers in Engineering 162, 107414 (2023)*.

**2022**

- H. Kwak, Y. Na, C. Ahn, J. Bae, and J. Kim\*. "785-nm frequency comb-based time-of-flight detection for 3D surface profilometry of silicon devices". *IEEE Photonics Journal 14, 3150908 (2022)*.
- J. Kim\*. "(Perspective) Chip-scale power booster for light". *Science 376, 1269 (2022)*.
- D. Kwon^, D. Jeong^, I. Jeon, H. Lee\*, and J. Kim\*. "Ultrastable microwave and soliton-pulse generation from fibre-photonic-stabilized microcombs". *Nature Communications 13, 381 (2022)*.
- C. Ahn, Y. Na, M. Hyun, J. Bae, and J. Kim\*. "Synchronization of an optical frequency comb and a microwave oscillator with 53 zs/Hz1/2 resolution and 10^-20-level stability". *Photonics Research 10, 365-372 (2022)*.

**2021**

- M. Hyun, C. Jeon, and J. Kim. "Ultralow-noise microwave extraction from optical frequency combs using photocurrent pulse shaping with balanced photodetection". *Scientific Reports 11, 17809 (2021)*.
- I. Do, D. Kim, D. Jeong, D. Suk, D. Kwon, J. Kim, J. Lee\*, and H. Lee\*. "Self-stabilized soliton generation in a microresonator through mode-pulled Brillouin lasing". *Optics Letters 46, 1772-1775 (2021)*.
- H. Chung\*, M. Hyun, J. Kim. "A 360-fs-time-resolution 7-bit stochastic time-to-digital converter with linearity calibration using dual time offset arbiters in 65-nm CMOS". *IEEE Journal of Solid-State Circuits 56, 940-949 (2021)*.
- J. Shin, H. Kim, S. Park, H. Bark, I. Baek, K. Oang, K. Jang, K. Lee, F. Rotermund, Y. Jeong\*, and J. Kim\*. "Sub-10-fs timing for ultrafast electron diffraction with THz-driven streak camera". *Laser and Photonics Reviews 15, 2000326 (2021)*.
- H. Kwak, S. Ryu, S. Cho, J. Kim, Y. Yang, and J. Kim\*. "Non-destructive thickness characterisation of 3D multilayer semiconductor devices using optical spectral measurements and machine learning". *Light: Advanced Manufacturing 2, 9-19 (2021)*.

## 과제

Research overview 페이지가 진행 중인 과제로 적은 8건이다. 협력 기관과 지원 기관은 랩 표기 그대로다.[^overview]

- Micro-comb-based ultralow-noise mm-wave generators (지원 NRF)
- Investigation of high-frequency jitter of micro-combs (협력 기관 Chalmers; 지원 NRF-SSF)
- Photonic signal generation and phase calibration for VLBI telescopes (협력 기관 KASI, KRISS, KISTI; 지원 NST-CAP and KASI)
- Integrated optical frequency synthesizers for quantum time sensors (협력 기관 KRISS; 지원 IITP)
- Rapid, precise and multifunctional LiDARs (지원 NRF-ERC)
- Rapid and precise TGV glass substrate metrology (지원 LG Innotek)
- Stress and defect detection in OLED glasses (지원 LG Display)
- Femtosecond laser-based semiconductor wafer metrology (지원 Samsung Electronics)

## 수상과 임명

랩 News 게시판의 2021년 이후 글 가운데 수상과 임명 소식 16건이다. 날짜는 게시일이고, 같은 일을 두 번 올린 글도 게시된 대로 옮겼다.[^news]

- 2025-02-14 · Changmin and Hyoungsu are awarded Outstanding Paper Awards from OSK Winter Conference 2025.
- 2024-08-08 · Changmin is awarded CLEO-PR 2024 Best Student Paper (2nd Place) from CLEO-PR 2024.
- 2024-02-15 · Prof. Kim is awarded Laser Science Award from the Optical Society of Korea (Feb 15, 2024)
- 2024-02-15 · Prof. Kim is awarded Laser Science Award from Optical Society of Korea (OSK).
- 2023-12-01 · Alumnus Dr. Yongjin Na received the Outstanding Doctoral Thesis Award from KAIST ME.
- 2023-11-16 · Prof. Kim is appointed as an IEEE Photonics Society Distinguished Lecturer for 2024.
- 2023-08-30 · Minji is awarded Outstanding Student Paper Award from OSK-Optica-OSJ Joint Symposia 2023.
- 2023-05-09 · Prof Kim is awarded an Optica Fellow at CLEO 2023 (May 9, 2023)
- 2023-02-17 · Yongjin Na received PhD Dissertation Award from the Dean of KAIST College of Engineering.
- 2023-02-17 · Changmin's paper is awarded Outstanding Paper Award from OSK Winter Conference 2023.
- 2022-11-08 · Prof. Kim is elected as a Fellow of Optica (formerly, Optical Society of America (OSA)).
- 2022-09-08 · Prof. Kim is appointed as a Topical Editor (in ultrafast optics and frequency combs) of Optics Letters.
- 2021-12-03 · Minji and Changmin are awarded Outstanding Paper Award from OSK Photonics Conference 2021.
- 2021-10-28 · Alumnus Dr. Dohyeon Kwon received the Outstanding Doctoral Thesis Award from KAIST ME.
- 2021-07-07 · Igju Jeon is awarded Outstanding Paper Award from OSK Optics and Photonics Congress (Jul 7, 2021)
- 2021-07-07 · Mr. Jeon is awarded Outstanding Paper Award from OSK Optics and Photonics Congress 2021.

## 소식

같은 게시판의 2021년 이후 나머지 글 29건(논문 출판, 과제 선정, 협약, 교수의 학술지 기고)이다.[^news]

- 2026-01-04 · A new paper on comb integration in VLBI radio telescopes is published in Light: Science & Applications.
- 2025-10-29 · A new paper on comb-based 3D-IC TSV metrology is published in Light: Advanced Manufacturing.
- 2025-10-06 · A new paper on ultrawide-range AFM cantilver dynamics tracking is published in PhotoniX.
- 2025-10-02 · A new paper on FPGA-driven soliton locking is published in Journal of Lightwave Technology.
- 2025-02-03 · A new paper on simple and ultrastable fiber-photonic laser stabilization is published in Optics Letters.
- 2024-11-01 · We are awarded NRF-SSF Collaboration Project with Chalmers on optoelectronic synchronization.
- 2024-07-03 · A new paper on a low-noise GHz waveguide laser is published in Optics and Laser Technology.
- 2024-05-15 · A new paper on a narrow linewidth DFB laser is published in Journal of Lightwave Technology.
- 2023-12-15 · A new paper on a compact and robust laser stabilization method is published in APL Photonics. It is also selected as a Featured Article of APL Photonics.
- 2023-12-08 · A new paper on pulse interleaving time error detection method is published in Optics Letters.
- 2023-05-04 · A review paper on multilayer nanometrology is published in Nanomanufacturing and Metrology.
- 2023-04-25 · A new paper on photonic clock distribution in CMOS chips is published in Nature Communications. It is also featured in Research Highlights (entitled "Chips with a pulse") of Nature Electronics.
- 2023-04-24 · Optical frequency comb-injected on-chip clock distribution network (CDN) is published at Nature Communications (April 24, 2023) and also highlighted at Nature Electronics (May 26, 2023)
- 2023-02-15 · Ultrafast line-scan TOF camera for imaging structures and dynamics in micro-scale devices is published at Light: Science & Applications (Feb 15, 2023)
- 2023-02-15 · A new paper on ultrafast line-scan TOF camera is published in Light: Science & Applications.
- 2022-12-06 · A new paper on rapid absolute distance metrology is published in Optics & Lasers in Engineering.
- 2022-09-05 · A new paper on 3D surface profilometry of silicon devices is published in IEEE Photonics Journal.
- 2022-06-16 · Prof. Kim contributed a commentary on chip-scale optical amplifiers in Perspective section of Science.
- 2022-06-01 · We are awarded NST Creative Allied Project (CAP) with KRISS, KASI and KISTI on VLBI networks.
- 2022-01-19 · Ultrastable microwave and soliton-pulse generation from a palm-sized photonic platform is published at Nature Communications (Jan 19, 2022)
- 2022-01-19 · A new paper on ultrastable photonic microwave generation is published in Nature Communications.
- 2022-01-14 · A new paper on ultrastable comb-microwave synchronization is published in Photonics Research.
- 2021-11-24 · We are joining the research collaboration effort between 5 national institutes for extreme-precision space-time measurements (Nov 24, 2021)
- 2021-11-24 · An MOU is signed with 5 national institutes for extreme-precision space-time convergence research.
- 2021-09-08 · A new paper on pulse shaping-based microwave extraction is published in Scientific Reports.
- 2021-02-11 · UED timing work appeared as the front cover paper of Laser and Photonics Reviews (Feb 11, 2021)
- 2021-02-11 · A new paper on UED timing is published as a Front Cover paper of Laser & Photonics Reviews.
- 2021-01-12 · Multilayer thickness metrology method is published at Light: Advanced Manufacturing (Jan 12, 2021)
- 2021-01-12 · A new paper on multilayer thickness metrology is published in Light: Advanced Manufacturing.

## 연락과 위치

- 연구실: KAIST 기계공학동(N7-4) 6119·6120호, 전화 042-350-3276[^contact]
- 교수 연구실: N7-4 7105호, 전화 042-350-3236[^contact]
- 학생 연구실: N7-4 4120호, 전화 042-350-5236[^contact]
- 주소: 291 Daehak-ro, Yuseong-gu, Daejeon, 34141, Republic of Korea[^home]

[^home]: 연구실 누리집 첫 화면 <https://upcam.kaist.ac.kr> (2026-10-21 열람)
[^overview]: Research overview 페이지 <https://upcam.kaist.ac.kr/sub1_1.php> (2026-10-21 열람)
[^comb]: Research topics 페이지 「Advanced lasers for precision photonics」 <https://upcam.kaist.ac.kr/sub1_2_a.php> (2026-10-21 열람)
[^timing]: Research topics 페이지 「Ultrastable Photonics & Timing for Quantum and Photonic AI」 <https://upcam.kaist.ac.kr/sub1_2_b.php> (2026-10-21 열람)
[^astro]: Research topics 페이지 「Space-Time Metrology & Astro-Photonics」 <https://upcam.kaist.ac.kr/sub1_2_c.php> (2026-10-21 열람)
[^semi]: Research topics 페이지 「Semiconductor Metrology and Inspection」 <https://upcam.kaist.ac.kr/sub1_2_d.php> (2026-10-21 열람)
[^papers]: Journal Publication 페이지 <https://upcam.kaist.ac.kr/bbs/board.php?bo_table=sub2_1> (2026-10-21 열람)
[^pi]: PI 페이지 <https://upcam.kaist.ac.kr/bbs/board.php?bo_table=sub3_2> (2026-10-21 열람)
[^researchers]: Researchers 페이지 <https://upcam.kaist.ac.kr/bbs/board.php?bo_table=sub3_3> (2026-10-21 열람)
[^alumni]: Alumni 페이지 <https://upcam.kaist.ac.kr/bbs/board.php?bo_table=sub3_4> (2026-10-21 열람)
[^news]: News 게시판 <https://upcam.kaist.ac.kr/bbs/board.php?bo_table=sub5_1> (1–3쪽, 2026-10-21 열람)
[^contact]: Contact 페이지 <https://upcam.kaist.ac.kr/bbs/board.php?bo_table=sub6_1> (2026-10-21 열람)
[^meprof]: KAIST 기계공학과 교수 소개(김정원) <https://me.kaist.ac.kr/pop/team.html?uid=16&LANGUAGE_TYPE=kor> (교수진 목록 <https://me.kaist.ac.kr/team/team_010100.html>에서 연결, 2026-10-21 열람)
[^me-hno]: KAIST 기계공학과 연구분야 「헬스케어/나노/광학」 <https://me.kaist.ac.kr/research/research_010400.html> (2026-10-21 열람)
[^me-mmm]: KAIST 기계공학과 연구분야 「소재/역학/제조」 <https://me.kaist.ac.kr/research/research_010200.html> (2026-10-21 열람)
[^p1]: C. Ahn 외, J. Kim, Optica 13, 717 (온라인 2026-04-08). <https://doi.org/10.1364/optica.581054> 초록 기준.
[^p2]: D. Kwon 외, J. Kim, Nature Communications 13, 381 (온라인 2022-01-19). <https://doi.org/10.1038/s41467-022-27992-8> 초록 기준.
[^p3]: M. Hyun, H. Chung, W. Na, J. Kim, Nature Communications 14, 2345 (온라인 2023-04-24). <https://doi.org/10.1038/s41467-023-38122-3> 초록 기준.
[^p4]: I. Jeon, W. Jeong, C. Ahn, J. Kim, Optics Letters 50, 1057 (온라인 2025-02-03). <https://doi.org/10.1364/ol.541281> 초록 기준.
[^p5]: M. Hyun 외, J. Kim, Light: Science & Applications 15, 53 (온라인 2026-01-04). <https://doi.org/10.1038/s41377-025-02056-w> 초록 기준.
[^p6]: H. Choi 외, J. Kim, Light: Advanced Manufacturing 6, 74 (2025). <https://doi.org/10.37188/lam.2025.074> 초록 기준(출판사 논문 페이지).
[^p7]: Y. Na 외, J. Kim, Light: Science & Applications 12, 44 (온라인 2023-02-15). <https://doi.org/10.1038/s41377-023-01077-7> 초록 기준.

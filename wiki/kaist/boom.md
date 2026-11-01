# 의광학 및 광측정 연구실 (Biomedical Optics and Optical Metrology Lab, BOOM Lab)

**KAIST 기계공학과 · 유홍기 교수**

- 분야: 의광학 영상 장치, 광학 측정, 영상 처리
- 대분야: 전기전자·반도체·광학, 기계·로봇·제조
- 태그: 광학 영상·현미경[^bio][^p6], 광학 센서·분광기[^metrology][^p4], 의료 영상 기기·재구성[^bio][^p7], 의료 AI[^bio], 양자 광학·광양자 기술[^p1], 나노 패터닝·전사[^p5]
- 홈페이지: <https://boom.kaist.ac.kr/>

> 빛으로 몸속 조직과 물체 표면을 관찰하는 영상 장치와 측정 방법을 만들고, 영상에서 구조·성분 정보를 추출하는 연구실이다.[^home]

## 무엇을 연구하나

BOOM Lab은 새로운 광학 영상 기술을 개발해 의료 문제와 산업 현장의 측정 문제를 푼다. 의광학 팀은 몸속을 보는 카테터(몸 안에 넣는 관 형태의 기구)와 여러 영상 방식을 결합한 현미경을 개발하고, 광측정 팀은 물체에 접촉하지 않고 표면의 입체 모양과 성분을 알아내는 방법을 연구한다.[^home][^bio][^metrology]

몸속 영상에서는 광간섭단층영상(OCT, optical coherence tomography, 반사된 빛의 간섭으로 조직의 단면을 얻는 방법)을 다른 영상 방식과 결합한다. 형광수명영상(FLIm, fluorescence lifetime imaging, 빛을 흡수한 물질이 빛을 내기 전의 들뜬 상태에 머무는 평균 시간을 영상화하는 방법)을 함께 써서 조직의 구조와 생화학적 성분 정보를 얻는다. 또 광학 생검(빛으로 조직의 미세 구조와 성분을 관찰하는 검사 방법)을 위한 현미경과 영상 처리 방법을 개발한다.[^bio][^p7]

산업용 측정에서는 공초점 현미경(초점면과 맞지 않는 곳에서 오는 빛을 걸러 영상을 얻는 현미경)을 개발해 입체 표면을 재고, 표면 높이와 색 정보를 결합한다. 라만 분광(물질과 에너지를 주고받으며 산란된 빛의 파장 변화를 분석하는 방법) 장치도 개발한다. 영상 처리에서는 딥러닝(여러 층의 신경망으로 자료의 표현을 단계적으로 학습하는 기계학습 분야)을 이용해 영상의 영역을 구분하고 화질을 복원하는 방법을 연구한다.[^metrology][^bio]

2026년 논문에서는 얽힌 광자 쌍과 물질의 상호작용도 다뤘다. 광자(빛의 에너지가 나뉘어 전달되는 기본 단위) 쌍의 편광(빛의 진동 방향에 관한 성질) 관계를 바꿔, 단일층 이셀레늄화텅스텐(WSe2)에서 서로 다른 물질 상태를 선택적으로 만들어 내는 원리를 제시했다.[^p1]

## 주요 연구 주제

### 몸속의 구조와 성분을 함께 보는 영상 장치

혈관·식도 같은 기관의 안쪽을 볼 수 있는 내시경 영상 카테터를 개발한다. 연구실은 OCT에 형광 영상이나 형광수명영상을 결합하는 장치, 여러 현미경 기법을 한 장치에서 쓰는 다중 방식 현미경을 연구한다. 구조 정보와 성분 정보를 함께 얻는 것이 목표다.[^bio]

대표 논문 2는 파장에 따른 초점 이동과 잡음(원하는 신호에 섞인 불필요한 변동) 제거를 함께 활용해 조직의 깊이에 걸쳐 선명한 영상을 얻는 OCT 장치를 제시했다. 대표 논문 7은 OCT와 형광수명영상을 통합하고 학습 방법을 더해 혈관 조직의 여러 성분을 자동으로 정량 영상화했다. 대표 논문 6은 시료 쪽 대물렌즈(시료의 상을 형성하는 렌즈 또는 렌즈군) 하나로 조명과 검출을 함께 하는 입체 현미경을 개발했다.[^p2][^p7][^p6]

### 물체 표면과 성분을 재는 광학 장치

여러 위치의 높이를 병렬로 읽는 공초점 측정과 색을 함께 얻는 입체 영상, 라만 신호를 읽는 측정 장치를 개발한다. 연구실은 이 기술의 활용 대상으로 산업용 비접촉 검사와 생체 영상을 제시한다.[^metrology]

대표 논문 4는 파장이 바뀌는 레이저와 필터·광검출기(빛을 전기 신호로 바꾸는 부품)를 쓰는 라만 분광 장치를 개발했다. 대표 논문 5는 기판(공정의 바탕이 되는 재료)의 변형을 광학적으로 측정하고 그 결과를 노광(빛에 반응하는 재료에 빛으로 무늬를 만드는 과정)에 반영해, 무늬를 새기는 동안 위치 오차를 보상한다.[^p4][^p5]

### 영상의 영역 구분과 화질 복원

의광학 영상에서 병변이나 구조의 영역을 자동으로 구분하고, 영상 품질을 복원하는 학습 방법을 연구한다. 연구 소개는 새 딥러닝 기법을 이용한 영역 구분과 영상 복원 방법 개발을 관심 분야로 든다.[^bio]

대표 논문 3은 자료 자체에서 학습 문제를 구성하는 자기지도학습으로 형광 영상의 잡음을 제거한다. 같은 위치의 영상이 시간에 따라 어떻게 변하는지를 활용해, 움직이는 세포나 생물체의 영상을 복원하는 방법을 제안했다.[^p3]

## 대표 논문

광간섭 단층영상과 혈관 내시경 영상, 현미경·영상 복원, 분광·광학 측정, 양자 광학을 다룬 7편이다. 「쉽게 말하면」은 각 논문의 등록 초록 또는 출판사 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 교수의 역할 |
|---|---|---|---|---|
| 1 | 2026 | [Eigenstate-selective entangled two-photon absorption in monolayer WSe2](https://doi.org/10.1103/wl4l-hyky) · Physical Review B | 서로 독립된 상태로 나눠 설명할 수 없는 양자 관계인 얽힘을 가진 광자 쌍을 다룬다. 두 광자의 편광 상태 사이 관계를 정하는 위상에 따라, 단일층 WSe2에 만들어지는 서로 다른 들뜬 상태의 분포가 달라지는 원리를 제시했다. 얽힘이 없는 편광 상태로는 같은 위상 의존 분포를 재현할 수 없으며, 특정 상태가 만들어지는 비율로 광원의 편광 얽힘을 확인할 수 있음을 보였다.[^p1] | 마지막 저자·교신저자 |
| 2 | 2025 | [Chromatic optical coherence tomography for high-resolution deep tissue imaging](https://doi.org/10.1364/PRJ.561513) · Photonics Research | 조직을 선명하게 볼 수 있는 깊이 범위와 영상의 세부 구분 능력, 잡음에 대한 신호의 비율을 함께 개선한 OCT 장치를 제안했다. 파장에 따라 초점 위치가 달라지는 광학계와 새 잡음 제거 알고리즘을 결합했고, 모의실험과 실험으로 깊이에 따른 영상 품질을 비교했다.[^p2] | 마지막 저자 |
| 3 | 2025 | [Self-supervised denoising of dynamic fluorescence images via temporal gradient-empowered deep learning](https://doi.org/10.1186/s43074-025-00173-8) · PhotoniX | 시간에 따른 영상 변화량을 활용하는 자기지도 잡음 제거 신경망을 제안했다. 시간과 공간의 정보를 함께 활용해 움직이는 시료의 형광 영상을 복원했으며, 위치 이동 없이 형광 신호가 시간에 따라 변하는 영상에서도 방법의 견고함을 보였다.[^p3] | 마지막 저자 |
| 4 | 2024 | [Swept-source Raman spectroscopy of chemical and biological materials](https://doi.org/10.1117/1.jbo.29.s2.s22703) · Journal of Biomedical Optics | 파장이 바뀌는 레이저, 필터와 광검출기를 이용한 라만 분광 장치를 개발하고 하드웨어의 한계를 줄이는 신호 처리 방법을 제안했다. 화학·생체 시료의 분광 신호를 얻어 기존 분광 장치의 결과와 비교했고, 생체 시료의 위치별 성분 정보도 얻었다.[^p4] | 공저자, 4명 중 3번째 |
| 5 | 2026 | [DMD-based adaptive lithography system for real-time substrate deformation compensation](https://doi.org/10.1080/15599612.2026.2635849) · International Journal of Optomechatronics | 기판의 변형을 광학적으로 측정하고 그 결과에 따라 새길 무늬를 실시간으로 바꾸는 노광 장치를 개발했다. 무늬 생성과 계산을 병렬로 처리하며, 실험에서 변형 때문에 생기는 위치 오차를 보상하고 무늬를 맞추거나 이어 붙이는 정밀도를 개선했다.[^p5] | 마지막 저자 |
| 6 | 2026 | [Single-objective two-photon oblique light sheet microscopy with a low repetition rate for 3D high-SNR imaging](https://doi.org/10.1364/PRJ.584858) · Photonics Research | 두 광자를 함께 흡수하는 현상으로 영상을 얻는 현미경을 개발했다. 시료 쪽의 대물렌즈(시료의 상을 형성하는 렌즈 또는 렌즈군) 하나로 조명과 검출을 함께 한다. 빛 펄스의 반복률을 조절해 평균 출력이 일정할 때 펄스 에너지를 높였고, 입체 재구성과 깊은 조직 영상에서 선명한 구조를 관찰했다.[^p6] | 마지막 저자 |
| 7 | 2021 | [Comprehensive assessment of high-risk plaques by dual-modal imaging catheter in coronary artery](https://doi.org/10.1016/j.jacbts.2021.10.005) · JACC: Basic to Translational Science | 구조를 보는 OCT와 성분 정보를 얻는 형광수명영상을 통합해 혈관 조직을 함께 관찰했다. 성분마다 다른 형광수명 특성을 이용하고 기계학습을 결합해, 혈관 병변의 주요 구성 성분을 자동으로 정량 영상화하는 방법을 제시했다.[^p7] | 공저자, 11명 중 10번째 |

## 교수와 전문 분야

유홍기 교수는 KAIST 기계공학과에서 2001년 학사, 2003년 석사, 2007년 박사학위를 받았다. KAIST 박사후연구원과 Harvard Medical School·Massachusetts General Hospital의 Wellman Center for Photomedicine 연구 경력을 거쳐 한양대학교 의생명공학과에서 근무했다. 2019년 2월 KAIST 기계공학과 부교수로 합류했고, 2025년 9월부터 Professor로 적혀 있다.[^prof]

연구실 소개와 연구 주제를 함께 보면 전문 분야는 몸속 광학 영상 카테터, 여러 영상 방식을 결합한 현미경, 공초점 기반 입체 표면 측정, 라만 분광 장치, 의광학 영상의 영역 구분·복원 방법이다.[^home][^bio][^metrology] 2026년 논문에서는 편광 얽힘을 이용한 빛과 물질의 상호작용을 다룬다.[^p1]

## 응용 분야

의료 쪽에서는 혈관 조직의 구조·성분 관찰, 광학 생검, 진단과 치료에 연결되는 영상 장치를 지향한다. 산업 쪽에서는 물체 표면의 높이와 색을 얻는 비접촉 검사, 물질 성분을 알아내는 광학 측정이 응용 대상이다.[^bio][^metrology]

## 구성원

2026년 10월 31일 Student 페이지에 게시된 18명이다. 연구교수 1명, 박사후연구원 3명, 박사과정 11명, 석사과정 2명, Researcher 1명이며, 직위·과정은 페이지 표기를 옮겼다. 「대표 논문 참여」는 위 표의 번호이고, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정·직위 | 대표 논문 참여 |
|---|---|---|
| Hyeong Soo Nam | 연구교수 | 2, 3, 6, 7 |
| Jeongmoo Han | 박사후연구원 | 7 |
| Yeon Hoon Kim | 박사후연구원 |  |
| Jeonggeun Song | 박사후연구원 | 3, 4, 6 |
| Seung Eon Lee | 박사과정 | 2 |
| Soonyong Kwon | 박사과정 |  |
| Minseok Jang | 박사과정 |  |
| Youngeun Cho | 박사과정 |  |
| Wonjin Kim | 박사과정 |  |
| Hwijun Koo | 박사과정 |  |
| Juyeol Eom | 박사과정 |  |
| Hyeon Jun Kim | 박사과정 |  |
| Jeongeun Park | 박사과정 |  |
| Hyung Beom Kim | 박사과정 |  |
| Ilkyu Park | 박사과정 |  |
| Seohyoung Jeon | 석사과정 |  |
| Min Jae Lee | 석사과정 |  |
| Youmin Lee | 연구원 |  |

## 졸업생과 이전 구성원

Alumni 페이지의 17명이다. 학위·과정과 진로는 연구실 게시 표기이며, 한양대학교 시절의 학위·연구 경력도 함께 실려 있다. 연도 없는 Present 표기는 현재 연도를 덧붙이지 않고 그대로 두었다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Ungyo Kang | 2019-2026 Ph.D, Mechanical Engineering, KAIST; 2017-2019 M.S, Dept. Biomedical Engineering, Hanyang University |  | Multichannel two-photon autofluorescence imaging for characterization of atherosclerotic plaques |
| Woojin Lee | 2022-2026 Ph.D, Mechanical Engineering, KAIST; 2020-2022 M.S, Mechanical Engineering, KAIST | 2026-Present Researcher, Samsung electronics, 반도체 연구소 | Multicolor two-photon oblique plane microscopy and self-supervised denoising for comprehensive volumetric imaging |
| Gyeongho Kim | 2024-2026 M.S, Mechanical Engineering, KAIST | 2026-Present SK hynix; 2026-2026 LG 디스플레이 | Maximizing SNR in swept-source optical coherence tomography through intended saturation and restoration |
| Jinsu Choi | 2021-2025 Ph.D, Mechanical Engineering, KAIST; 2019-2021 M.S, Mechanical Engineering, KAIST | 2025-Present KIMM(한국기계연구원) | Adaptive patterning for compensation of substrate deformation in DMD-based maskless lithography systems |
| Minsuk Lee | 2021-2025 Ph.D, Mechanical Engineering, KAIST | Present Senior Researcher, Osong medical innovation foundation | Visualization of intra-abdominal embedded blood vessels for laparoscopic dissecting tool using optical coherence tomography |
| Jinsoo Choi | M.S (이름 뒤 표기); 2021-2024 Ph.D (ABD), Mechanical Engineering, KAIST | Present KIMM(한국기계연구원) |  |
| Jin Hwan Hwang | 2022-2024 M.S, Mechanical Engineering, KAIST | Present Samsung electronics, MX |  |
| Jue Hyung Kang | 2017-2021 Ph.D, Dept. Biomedical Engineering, Hanyang University; 2015-2017 M.S, Dept. Biomedical Engineering, Hanyang University | Present Researcher, Samsung electronics, 반도체 연구소 |  |
| Bomi Gweon | Ph.D | 2019-Present Assistant Professor, Sejong University; 2014-2019 Research Professor, Dept. Biomedical Engineering, Hanyang University |  |
| Jun Young Kim | 2015-2019 Ph.D, Dept. Biomedical Engineering, Hanyang University; 2013-2015 M.S, Dept. Biomedical Engineering, Hanyang University | 2024-present Senior Optical Systems Engineer, Intelon Optics; 2019-2024 Post-doctoral Researcher, Wellman Center for Photomedicine, Harvard Medical School and Massachusetts General Hospital Boston |  |
| Min Woo Lee | 2015-2019 Ph.D, Dept. Biomedical Engineering, Hanyang University; 2013-2015 M.S, Dept. Biomedical Engineering, Hanyang University | 2021-Present Research Director, Dotter Inc.; 2019-2021 Researcher, KIST |  |
| Chang-Soo Kim | 2014-2020 Integrated M.S. & Ph.D, Dept. Biomedical Engineering, Hanyang University | Present Researcher, Nexensor |  |
| Jing Chao Xing | 2016-2020 Ph.D, Dept. Biomedical Engineering, Hanyang University; 2014-2016 M.S, Dept. Biomedical Engineering, Hanyang University | 2024-Present Diligine Photonics Co., Ltd; 2020-2024 Researcher, Institute of Semiconductors, Guangdong Academy of Sciences |  |
| Yu Jin Shin | 2015-2017 M.S, Dept. Biomedical Engineering, Hanyang University | 2014-2019 Researcher, Dept. Biomedical Engineering, Hanyang University |  |
| Woo Seop Kim | 2017-2019 M.S, Dept. Biomedical Engineering, Hanyang University |  |  |
| Yun Jeong Jeong | M.S | 2014-2019 Researcher, Dept. Biomedical Engineering, Hanyang University |  |
| Zeyuan Li | 2015-2017 M.S, Dept. Biomedical Engineering, Hanyang University | Present JS Global CO. LTD |  |

## 최근 논문 목록 (2021–2026)

OCT·현미경·분광 장치, 광학 표면 측정, 영상 처리와 광학 소재를 다룬 44편이다. 연도는 연구실 Publication 페이지의 연도 구역이며, 제목·저자·발표처는 연구실 표기다. 날짜가 연도로만 적힌 2021년 항목도 해당 연도 구역에 따라 싣는다.[^pubs]

**2026**

- Young Geun Lim, Jin Hyuk Kim, Ryeong Hyun Kim, Hongki Yoo, Jin Won Kim, Kyeongsoon Park. "H2O2-and light-triggered MnO2-based nanoswitches for microenvironment reprogramming and photodynamic therapy of hypoxic atherosclerotic plaques". *Journal of Nanobiotechnology, 2026; doi: 10.1186/s12951-026-05117-3*.
- Minseok A. Jang, Hongki Yoo. "Eigenstate-selective entangled two-photon absorption in monolayer WSe2". *Physical Review B, 2026; doi: 10.1103/wl4l-hyky*.
- Juyeol Eom\*, Dong Oh Kang\*, Hyeong Soo Nam, Woojin Lee, Jin Won Kim, Hongki Yoo. "Lesion-Specific Prediction of Segmental Fractional Flow Reserve Using Deep Learning and Optical Coherence Tomography-Derived Features". *Circulation Journal, 2026; doi: 10.1253/circj.CJ-26-0020*.
- Woojin Lee, Soonyong Kwon, Hyeong Soo Nam, Jae Yeon Seok, Hongki Yoo. "Label-free diagnosis across the thyroid nodule pathology spectrum using deep learning-enabled optical coherence tomography". *Biomedical Optics Express, 2026; doi: 10.1364/BOE.591801*.
- Jeonggeun Song, Woojin Lee, Hyeong Soo Nam, Hamin Park, Young-Gyun Park, Hongki Yoo. "Single-objective two-photon oblique light sheet microscopy with a low repetition rate for 3D high-SNR imaging". *Photonics Research, 2026; doi: 10.1364/PRJ.584858*.
- Jinsoo Choi, Kyungrok Kim, Jaeyoung Kim, Hyunchang Kim, Hongki Yoo, Dongwoo Kang. "Impact of encoder-head installation errors and geometrical scale errors on angle self-calibration accuracy using four arbitrarily arranged encoder-heads". *Precision Engineering, 2026; doi: 10.1016/j.precisioneng.2026.05.003*.
- Jinsu Choi, Won-Sup Lee, Geehong Kim, Hyunmin Cho, Won Seok Chang, Hongki Yoo. "DMD-based adaptive lithography system for real-time substrate deformation compensation". *International Journal of Optomechatronics, 2026; doi: 10.1080/15599612.2026.2635849*.
- Jin Hwan Hwang, Woojin Lee, Jin Hyuk Kim, Dong Oh Kang, Jin Won Kim, Hongki Yoo, Hyeong Soo Nam. "Automated lipid detection in spectroscopic optical coherence tomography using a weakly supervised deep learning network". *Biomedical Optics Express, 2026; doi: 10.1364/BOE.585222*.

**2025**

- Seungjai Won, Jungyoon Kim, Yungeun Oh, Taewon Kim, Seungman Choi, Byunggi Kim, Hongki Yoo, Seung-Woo Kim, Young-Jin Kim. "Programmable structured DUV illumination by coherent harmonic generation at crystalline solids for nanometer-resolution inspection of periodic samples". *PhotoniX, 2025; doi: 10.1186/s43074-025-00206-2*.
- Seung Eon Lee, Hyeong Soo Nam, Ryeong Hyeon Kim, Hyun Jung Kim, Jae Yeon Seok, Jin Won Kim, Young-Jin Kim, Hongki Yoo. "Chromatic optical coherence tomography for high-resolution deep tissue imaging". *Photonics Research, 2025; doi: 10.1364/PRJ.561513*.
- Jeongmoo Han, Min Woo Lee, Hyeong Soo Nam, Sunwon Kim, Dong Oh Kang, Youngeun Cho, Jin Won Kim, Hongki Yoo. "Broadband fiber optic rotary joint for clinical multimodal optical coherence tomography". *IEEE Photonics Technology Letters, 2025; doi: 10.1109/LPT.2025.3601082*.
- Youngeun Cho, Jeongmoo Han, Yeon Hoon Kim, Hyeong Soo Nam, Min Woo Lee, Young-Jin Kim, Jin Won Kim, Hongki Yoo. "Reducing Multipath Artifacts in Double-Clad Fiber for Multimodal Endoscopic Optical Coherence Tomography". *Journal of Lightwave Technology, 2025; doi: 10.1109/JLT.2025.3576609*.
- Woojin Lee, Minseok A. Jang, Hyeong Soo Nam, Jeonggeun Song, Jieun Choi, Joon Woo Song, Jae Yeon Seok, Pilhan Kim, Jin Won Kim, Hongki Yoo. "Self-supervised denoising of dynamic fluorescence images via temporal gradient-empowered deep learning". *PhotoniX, 2025; doi: 10.1186/s43074-025-00173-8*.
- Sunwon Kim, Hyeong Soo Nam, Dong Oh Kang, Jeongmoo Han, Hyokee Kim, Joon Woo Song, Eun Jin Park, Ryeong Hyun Kim, Hyun Jung Kim, Jin Hyuk Kim, Sunki Lee, Young Su Kim, Pyoungjae Park, Man-Jong Baik, Hongki Yoo, Jin Won Kim. "Intracoronary Structural-Molecular Imaging for Multitargeted Characterization of High-Risk Plaque: First-in-Human OCT-FLIm". *JAMA Cardiology, 2025; doi: 10.1001/jamacardio.2025.0928*.
- Huy Hoang Chu, Dae Hee Kim, Jun Hyung Park, Sukkyung Kang, Jaiho Son, Hyunmin Lee, Hongki Yoo, Seung-Woo Kim, Sanha Kim, Young-Jin Kim. "Nanometer-resolution white-light scanning interferometry for surface-profiling of hybrid bonding samples for advanced semiconductor packaging". *Applied Surface Science, 2025; doi: 10.1016/j.apsusc.2025.162466*.
- Hyeong Soo Nam, Dong Oh Kang, Jeongmoo Han, Jin Won Kim, Hongki Yoo. "Deep Learning-Based Saturation Compensation for High Dynamic Range Multispectral Fluorescence Lifetime Imaging". *IEEE Transactions on Biomedical Engineering, 2025; doi: 10.1109/TBME.2025.3548297*.

**2024**

- Jeongmoo Han, Soonyong Kwon, Hongki Yoo. "Medical applications of endogenous fluorescence lifetime imaging". *Journal of Innovative Medical Technology, 2024; doi: 10.61940/jimt.240010*.
- Minseok A. Jang, Joon Woo Song, Tyeong Hyun Kim, Dong Oh Kang, Ungyo Kang, Hyun Jung Kim, Jin Hyuk Kim, Eun Jin Park, Ye Hee Park, Bo-Hyung Lee, Chi Kyung Kim, Hyeongsoon Park, Jin Won Kim and Hongki Yoo. "Real-time imaging assessment of stress-induced vascular inflammation using heartbeat-synchronized motion compensation". *Ateriosclerosis, Thrombosis, and Vascular Biology, 2024; doi: 10.1161/ATVBAHA.124.321566*.
- Dae Hee Kim, Young Ho Park, Jun Hyung Park, Duy-Anh Nguyen, Hongki Yoo, Seungchel Kim and Young-Jin Kim. "Quantitative measurement of spatial distribution of effective refractive index induced by local electron concentration at a nano slit". *Nanophotonics, 2024; doi: 10.1515/nanoph-2024-0179*.
- Jin Hyuk Kim, Joon Woo Song, Yeon Hoon Kim, Hyun Jung Kim, Ryeong Hyun Kim, Ye Hee Park, Hyeong Soo Nam, Dong Oh Kang, Hongki Yoo, Kyeongsoon Park, and Jin Won Kim. "Multimodal imaging-assisted intravascular theranostic photoactivation on atherosclerotic plaque". *Circulation Research, 2024; 135(5);e114-132; DOI: 10.1161/circresaha.123.323970*.
- Wonjin Kim, Sun-Young Jeon, Gyurl Byun, Hongki Yoo, and Jang-Hwan Choi. "A systematic review of deep learning-based denoising for low-dose computed tomography from a perceptual quality perspective". *Biomedical Engineering Letters, 2024; 1-21*.
- Tongmei jing, Han Ku Nam, Dongwook Yang, Younggeun Lee, Tongke Gao, Hongki Yoo, Soongeun Kwon, Seung-Woo Kim, Liandong Yu, and Young-Jin Kim. "In situ transfer of laser-induced graphene electronics for multifunctional smart windows". *Small Science. 2024; 240010*.
- Dongwook Yang, Younggeun Lee, Hyeokin Kang, Quang Huy Vu, Guseon Kang, Seung Eon Lee, Hyogeun Han, Seunghwan Kim, Han Ku Nam, Soongeun Kwon, Hyug-Gyo Thee, JooHyung Lee, Hongki Yoo, Hyosang  Yoon, and Young-Jin Kim. "Green manufacturing of electrically-tunable smart light-weight planar optics: a review". *International Journal of Precision Enineering and Manufacturing-Green Technology, 2024; 1-23*.
- Woojin Lee, Chang-Soo Kim, Dong-Ryoung Lee, and Hongki Yoo. "Color volumetric imaging with high dynamic range based on parallel confocal detection". *IEEE Photonics Technology Letters. 2024*.
- Jeonggeun Song, Peter T. C. So, Hongki Yoo, and Jeon Woong Kang. "Swept-source Raman spectroscopy of chemical and biological materials". *Journal of Biomedical optics. 2024; 29(S2), S22703-S22703; DOI: 10.1117/1.jbo.29.s2.s22703*.
- Jinsoo Choi, Hongki Yoo, EunJong Choi, Kihyun Kim and Hyo-Young Kim. "An active geophone sensor with optimized state variable filter for measuring low-band frequencies". *Precision Engineering and Manufacturing. 2024; 25(5):981-993*.
- Seung-Yul Lee, Jin Hyuk Kim, Joon Woo Song, Ji Seon Min, Hyun Jung Kim, Ryeong Hyun Kim, Jae Won Ahn, Hongki Yoo, Kyeongsoon Park and Jin Won Kim. "Macrophage-mannose-receptor-targeted photoactivatable agent for in vivo imaging and treatment of atherosclerosis". *International Journal of Pharmaceutics 2024; 10:654:123951; DOI: 10.1016/j.ijpharm.2024.123951*.

**2023**

- Minsuk Lee, Hyeonjin Bang, Eungjang Lee, Sungsoo Park, Hongki Yoo, Wang-yuhl Oh and Seungrag Lee. "Imaging peritoneal blood vessels through optical coherence tomography angiography for laparoscopic surgery". *Journal of Biophotonics 2023; e202300221*.
- Yongjin Na, Hyunsoo Kwak, Changmin Ahn, Seung Eon Lee, Woojin Lee, Chu-Shik Kang, Jungchul Lee, Junho Suh, Hongki Yoo and Jungwon Kim. "Massively parallel electro-optic sampling of space-encoded optical pulses for ultrafast multi-dimensional imaging". *Light: Science & Applications 2023; 12:44*.
- Jeonggeun Song\*, Juehyung Kang\*, Ungyo Kang, Hyeong Soo Nam, Hyun Jung Kim, Ryeong Hyeon Kim, Jin Won Kim and Hongki Yoo. "SNR enhanced high-speed two-photon microscopy using a pulse picker and time gating detection". *Scientific Reports 2023; 13.1:14244*.
- Yeounggeun Lee, Mun Ji Low, Dongwook Yang, Han Ku Nam, Truong-Son Dinh Le, Seung Eon Lee, Hyogeun Han, Seunghwan Kim, Quang Huy Vu, Hongki Yoo, Hyosang Yoon, Joohyung Lee, Suchand Sandeep, Keunwoo Lee, Seung-Woo Kim and Young-Jin Kim. "Ultra-thin light-weight laser-induced-graphene (LIG) diffractive optics". *Light: Science & Applications 2023; 12.1: 146*.
- Jeongmoo Han\*, Sunwon Kim\*, Hyun Jung Kim, Hyeong Soo Nam, Min Woo Lee, Joon Woo Song, Jin Won Kim and Hongki Yoo. "Label-Free Characterization of Atherosclerotic Plaques Via High-Resolution Multispectral Fluorescence Lifetime Imaging Microscopy". *Arteriosclerosis, Thrombosis and Vascular Biology 2023; 43: 1295-1307; DOI: 10.1161/atvbaha.123.319339*.
- Woojin Lee, Hyeong Soo Nam, Jae Yeon Seok, Wang-Yhul Oh, Jin Won Kim and Hongki Yoo. "Deep learning-based image enhancement in optical coherence tomography by exploiting interference fringe". *Communications Biology 2023; 6: 463*.

**2022**

- Jingchao Xing, Dong-Ryoung Lee, Jin Won Kim and Hongki Yoo. "Histological classification of atherosclerotic arteries using high-speed confocal Raman microscopy with machine learning". *Journal of Biophotonics 2022; e202200243; DOI: 10.1002/jbio.202200243*.
- Jeongmoo Han\*, Ungyo Kang\*, Eun-Yi Moon, Hongki Yoo  and Bomi Gweon. "Imaging Technologies for Microfluidic Biochips". *BioChip Journal 2022; 16: 255-269*.
- Jinsu Choi, Geehong Kim, Won-Sup Lee, Won Seok Chang, and Hongki Yoo. "Method for improving the speed and pattern quality of a DMD maskless lithography system using a pulse exposure method". *Optics Express 2022; 30(13): 22487-22500*.
- Minsuk Lee, Hyeonjin Bang, Eungjang Lee, Youngjae Won, Kisub Kim, Sungsoo Park, Hongki Yoo, Seungrag Lee. "Lateral image reconstruction of optical coherence tomography using one‐dimensional deep deconvolution network". *Lasers in Surgery and Medicine 2022; 1-12*.

**2021**

- Sunwon Kim\*, Hyeong Soo Nam\*, Min Woo Lee, Hyun Jung Kim, Woo Jae Kang, Joon Woo Song, Jeongmoo Han, Dong Oh Kang, Wang-Yuhl Oh, Hongki Yoo, Jin Won Kim. "Comprehensive assessment of high-risk plaques by dual-modal imaging catheter in coronary artery". *JACC: Basic to Translational Science 2021; 6(12): 948-960; DOI: 10.1016/j.jacbts.2021.10.005*.
- Joon Woo Song, Jae Won Ahn, Min Woo Lee, Hyun Jung Kim, Dong Oh Kang, Tyeong Hyun Kim, Ungyo Kang, Yeon Hoon Kim, Jeongmoo Han, Ye Hee Park, Hyeong Soo Nam, Hongki Yoo, Kyeongsoon Park, Jin Won Kim. "Targeted theranostic photoactivation on atherosclerosis". *Journal of Nanobiotechnology 2021; vol 19, 338; DOI: 10.1186/s12951-021-01084-z*.
- Woojin Lee, Hyeong Soo Nam, Young Gon Kim, Yong Ju Kim, Jun Hee Lee, Hongki Yoo. "Robust autoflcusing for scanning electron microscopy based on a dual deep learning network". *Scientific Reports 2021; vol 11, 20933*.
- Jiheun Ryu\*, Ungyo Kang\*, Joon Woo Song, Junyoung Kim, Jin Won Kim, Hongki Yoo, and Bomi Gweon. "Multimodal microscopy for the simultaneous visualization of five different imaging modalities using a single light source". *Biomedical Optics Express 2021; vol 12, Issue 9, pp. 5452-5469*.
- Chang-Soo Kim, Hongki Yoo. "Three-dimensional confocal reflectance microscopy for surface metrology". *Measurement Science and Technology 2021; 32(24) 102002*.
- Chang-Soo Kim, Junyoung Kim, Hongki Yoo. "Color three-dimensional imaging based on patterned illumination using a negative pinhole array". *Optics Express 2021; 29(5):6509-6522*.
- Juehyung Kang, Ungyo Kang, Hyeong Soo Nam, Wooseop Kim, Hyun Jung Kim, Ryeong Hyeon Kim, Jin Won Kim, Hongki Yoo. "Label-free multimodal microscopy using a single light source and detector for biological imaging". *Optics Letters 2021; 46(4):0892-0895*.

## 수상과 선정

날짜는 글의 게시일이며, 수상일과 구별한다.[^news]

- 2026-10-13 게시 · 유홍기 교수, 제61회 발명의 날 국무총리표창 수상[^award]
- 2026-03-20 게시 · 이중 모달리티 OCT-FLIm 시스템 연구, 2025 KAIST 대표 연구 성과 선정[^selection]
- 2025-11-08 게시 · 2025 대한의용생체공학회 추계학술대회: 김경호 우수 논문상, 권순용 최우수 포스터상 수상
- 2025-11-01 게시 · SPIE Advanced Biophotonics Conference 2025: 조영은·이승언 Young Investigator Award, 김연훈 Best Poster Award 수상
- 2025-05-10 게시 · 2025 대한의용생체공학회 춘계학술대회: 이우진 최우수 포스터상 수상
- 2024-11-04 게시 · ABC 2024: 한정무 Young Investigator Award 1st prize, 이우진 Best Poster Award 수상

## 소식

날짜는 글의 게시일이다.[^news]

- 2024-11-04 게시 · 남형수·한정무·이우진·이승언·조영은·엄주열·김경호·전서형, ABC 2024 학회 참여

## 연락과 위치

- 교수 연구실: N7-4 3204, ME Building[^prof]
- 교수 전화: +82-42-350-3243[^prof]
- 구성원 연구 공간: N25 3434, ID building. Researcher Youmin Lee의 공간은 N7, Mechanical Engineering building으로 적혀 있다.[^members]
[^home]: BOOM Lab, 「Home」. 의료 문제와 산업 과제에 쓸 새로운 광학 영상 기술·장치·방법을 개발하며, 의광학 팀과 광측정 팀의 연구를 설명한다. <https://boom.kaist.ac.kr/> (관측 2026-10-31).
[^prof]: BOOM Lab, 「Professor」. Hongki Yoo, Ph.D, Professor, KAIST 기계공학과 경력·학력·위치·연락처. <https://boom.kaist.ac.kr/professor> (관측 2026-10-31).
[^bio]: BOOM Lab, 「Biomedical Optics」. 새 내시경 영상 카테터 시스템, 광학 생검, 여러 영상 방식을 결합한 현미경, 혈관 내 다중 방식 OCT 장치를 개발한다. 새 딥러닝 기법을 이용한 영역 구분과 영상 화질 복원 방법 개발에 관심이 있다고 적는다. <https://boom.kaist.ac.kr/biomedical-optics> (관측 2026-10-31).
[^metrology]: BOOM Lab, 「Optical Metrology」. 실시간 입체 공초점 현미경과 색을 함께 얻는 입체 표면 재구성 방법, 라만 신호를 읽는 고속 공초점 분광 장치를 개발한다. <https://boom.kaist.ac.kr/opticalmetrology> (관측 2026-10-31).
[^members]: BOOM Lab, 「Student」. Meet The Team의 이름·직위·과정과 공간. <https://boom.kaist.ac.kr/student> (관측 2026-10-31).
[^alumni]: BOOM Lab, 「Alumni」. 이름·학위·과정·기간·진로와 학위 논문. <https://boom.kaist.ac.kr/alumni> (관측 2026-10-31).
[^pubs]: BOOM Lab, 「Publication」. 2021–2026년 구역의 연구실 게시 서지. <https://boom.kaist.ac.kr/publication> (관측 2026-10-31).
[^news]: BOOM Lab, 「News」. 게시글 제목·요약과 게시 시각을 기준으로 수상·선정·학회 참여 사실을 적었다. <https://boom.kaist.ac.kr/news> (관측 2026-10-31).
[^award]: BOOM Lab, 제61회 발명의 날 국무총리표창 수상 소식. 유홍기 교수의 표창과 광학 진단·측정 기술 개발 공로를 적는다. <https://boom.kaist.ac.kr/post/%EC%9C%A0%ED%99%8D%EA%B8%B0-%EA%B5%90%EC%88%98%EB%8B%98-%EC%A0%9C61%ED%9A%8C-%EB%B0%9C%EB%AA%85%EC%9D%98-%EB%82%A0-%EA%B5%AD%EB%AC%B4%EC%B4%9D%EB%A6%AC%ED%91%9C%EC%B0%BD-%EC%88%98%EC%83%81-prof-hongki-yoo-receives-the-prime-minister-s-commendation-at-the> (관측 2026-11-01).
[^selection]: BOOM Lab, 2025 KAIST 대표 연구 성과 선정 소식. 이중 모달리티 OCT-FLIm 시스템 연구의 선정 사실을 적는다. <https://boom.kaist.ac.kr/post/2025-%EC%B9%B4%EC%9D%B4%EC%8A%A4%ED%8A%B8-%EB%8C%80%ED%91%9C-%EC%97%B0%EA%B5%AC-%EC%84%B1%EA%B3%BC-10%EC%84%A0-%EC%84%A0%EC%A0%95-selected-for-the-2025-kaist-top-10-research-achievements> (관측 2026-11-01).
[^p1]: M. A. Jang, H. Yoo, Physical Review B 114, 115418 (온라인 2026-08-27). <https://doi.org/10.1103/wl4l-hyky> 초록 기준(출판사 논문 페이지). 초록 원문 <https://journals.aps.org/prb/abstract/10.1103/wl4l-hyky> (관측 2026-11-01).
[^p2]: S. E. Lee 외, H. Yoo, Photonics Research 13, 2888 (온라인 2025-10-01). <https://doi.org/10.1364/PRJ.561513> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1364/PRJ.561513> (관측 2026-11-01).
[^p3]: W. Lee 외, H. Yoo, PhotoniX 6, 15 (온라인 2025-05-23). <https://doi.org/10.1186/s43074-025-00173-8> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1186/s43074-025-00173-8> (관측 2026-11-01).
[^p4]: J. Song, P. T. C. So, H. Yoo, J. W. Kang, Journal of Biomedical Optics 29, 1-10 (2024). <https://doi.org/10.1117/1.jbo.29.s2.s22703> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=Swept-source%20Raman%20spectroscopy%20of%20chemical%20and%20biological%20materials> (관측 2026-11-01).
[^p5]: J. Choi 외, H. Yoo, International Journal of Optomechatronics 20, 2635849 (온라인 2026-03-14). <https://doi.org/10.1080/15599612.2026.2635849> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1001/jamacardio.2025.0928|10.1002/jbio.202200243|10.1007/s13534-026-00582-z|10.1016/j.bios.2025.117316|10.1016/j.ijpharm.2024.123951|10.1016/j.jacbts.2021.10.005|10.1016/j.nantod.2026.103020|10.1038/s41598-021-85634-3|10.1038/s41598-023-40363-7|10.1080/15599612.2026.2635849|10.1093/eurheartj/ehaa1095|10.1093/eurheartj/ehab463|10.1117/1.jbo.29.s2.s22703|10.1161/atvbaha.123.319339|10.1161/atvbaha.124.321566|10.1161/circresaha.123.323970|10.1186/s12951-021-01084-z|10.1186/s12951-026-05117-3|10.1186/s43074-025-00173-8|10.1253/circj.cj-26-0020|10.12997/jla.2025.14.3.258|10.1364/boe.591801|10.1364/prj.561513|10.1364/prj.584858|10.7150/thno.59759> (관측 2026-11-01).
[^p6]: J. Song 외, H. Yoo, Photonics Research 14, 2591 (온라인 2026-05-26). <https://doi.org/10.1364/PRJ.584858> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1364/PRJ.584858> (관측 2026-11-01).
[^p7]: S. Kim 외, J. W. Kim, JACC: Basic to Translational Science 6, 948-960 (2021). <https://doi.org/10.1016/j.jacbts.2021.10.005> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1001/jamacardio.2025.0928|10.1002/jbio.202200243|10.1007/s13534-026-00582-z|10.1016/j.bios.2025.117316|10.1016/j.ijpharm.2024.123951|10.1016/j.jacbts.2021.10.005|10.1016/j.nantod.2026.103020|10.1038/s41598-021-85634-3|10.1038/s41598-023-40363-7|10.1080/15599612.2026.2635849|10.1093/eurheartj/ehaa1095|10.1093/eurheartj/ehab463|10.1117/1.jbo.29.s2.s22703|10.1161/atvbaha.123.319339|10.1161/atvbaha.124.321566|10.1161/circresaha.123.323970|10.1186/s12951-021-01084-z|10.1186/s12951-026-05117-3|10.1186/s43074-025-00173-8|10.1253/circj.cj-26-0020|10.12997/jla.2025.14.3.258|10.1364/boe.591801|10.1364/prj.561513|10.1364/prj.584858|10.7150/thno.59759> (관측 2026-11-01).

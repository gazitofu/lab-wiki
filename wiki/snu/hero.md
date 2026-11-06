# Healthcare Robotics Lab (HeRo Lab)

**서울대학교 공과대학 기계공학부 · 한경원 부교수**

- 영문 이름: Healthcare Robotics Lab (HeRo Lab)
- 분야: 수술 로봇과 의료 도구, 조직 접촉 감지, 이식형 보조 장치, 인공근육과 촉각 전달[^home][^dept]
- 대분야: 기계·로봇·제조
- 태그: 수술·의료 로봇[^research], 로봇 구동기·센서[^research][^dept], 햅틱[^research], 인공 근육[^research]
- 홈페이지: <https://hero.snu.ac.kr/>
- 근거와 출처: [Healthcare Robotics Lab 근거 페이지](hero-sources.md)

> 수술 도구의 위치와 접촉을 알아내고, 몸속 기관의 움직임을 돕는 장치를 설계하는 연구실이다.[^home]

## 무엇을 연구하나

헬스케어 로보틱스 연구실은 수술·치료·재활에 필요한 구동기(공급받은 전기·압력 등을 움직임이나 힘으로 바꾸는 장치), 센서(물리적·화학적 상태를 감지해 읽을 수 있는 값으로 바꾸는 장치), 시스템과 기구(부품을 연결해 움직임과 힘을 전달하는 구조)를 개발한다. 한경원 교수가 이끄는 서울대학교 기계공학부 연구실이며, 2022년 3월 1일 공식 출범했다.[^past][^dept] 로봇의 움직임을 만드는 구동기와 접촉 상태를 알아내는 센서를 개발한다.[^research][^dept]

연구실은 네 갈래를 내세운다. 수술 도구와 로봇 팔을 개발하는 수술 로봇, 기관의 형태와 움직임을 돕거나 상태를 살피는 이식형 장치(몸 안에 넣어 사용하는 장치), 원격 로봇 시술과 의료 훈련을 위한 햅틱(힘·진동 등으로 촉감을 전하거나 촉각을 재는 기술), 착용형 보조·재활 기기에 쓸 인공근육(외부 자극에 따라 재료의 형태가 변하면서 움직임이나 힘을 만드는 구동 소재·장치)이다.[^research] 인공근육 분야에서는 유연하고 가벼운 구동기를 개발한다.[^research] 햅틱 분야에서는 조작자에게 촉감을 돌려주는 장치를 만든다.[^research]

최근 논문에서는 수술 중 조직을 잡는 힘과 미끄럼을 알아내는 센서, 영상에서 수술 도구의 위치·방향을 계산하는 방법, 심장과 혈관을 바깥에서 압박하는 보조 장치가 구체적인 연구 대상이다. 예를 들어 한 장의 엑스선 영상으로 카테터(체내에 넣어 액체를 보내거나 기구를 안내하는 관)의 입체 자세를 추정하고, 빛으로 수술 집게와 조직 사이의 미끄럼을 감지한다. 심장 보조 장치 연구에서는 혈액에 직접 닿지 않는 구조로 압박을 전달하는 구동기를 설계한다.[^p1][^p3][^p5]

## 주요 연구 주제

### 1. 수술 도구의 위치 추정과 의료 도구 설계

연구실은 수술 도구와 로봇 팔을 개발한다.[^research] 수술 중 도구가 어디에 있고 어느 방향을 향하는지 계산하는 수술 항법(도구·영상·환자의 위치 관계를 이용해 시술 위치를 안내하는 기술)을 연구한다. 얇은 표지를 단 카테터를 단일 엑스선 영상으로 추적하는 알고리즘과, 피부에 붙인 채 광학 추적 및 의료 영상에서 함께 보이는 표지 장치를 개발했다. 표지 장치는 컴퓨터 단층촬영(Computed Tomography, CT; 여러 방향에서 얻은 측정값을 계산해 대상 내부의 단면을 재구성하는 영상 기법)과 자기공명영상(Magnetic Resonance Imaging, MRI; 자기장과 전자기파에 대한 원자핵의 반응을 이용해 대상 내부 구조를 영상으로 만드는 기법)에서 모두 보이도록 설계했다.[^p1][^p2]

의료 도구 자체의 형상과 측정 정확도도 다룬다. 미세바늘(조직에 삽입하는 미세한 바늘)의 형상을 최적화해 조직에 고정되는 성질과 삽입에 필요한 힘을 함께 조절하고, 초음파(사람의 가청 주파수 상한을 넘는 소리)를 보내고 반사된 소리를 받아들이는 탐촉자의 위치 관계를 맞추는 보정 방법을 개발했다. 주파수는 주기적인 변화가 단위 시간에 반복되는 횟수다. 보정 연구에서는 구형 표지가 무작위로 배치된 시험 모형과 새 계산 방법을 함께 사용한다.[^p7][^p8]

### 2. 수술 중 조직 접촉과 미끄럼 감지

조직을 잡는 수술 집게에 센서를 결합해 접촉 상태를 알아낸다. 빛을 이용하는 미끄럼 센서는 조직이 집게에 대해 움직이는 거리·방향·속도를 감지하며, 두 센서의 관측값으로 조직의 이동·회전·늘어남을 구분했다. 다른 연구에서는 전극(전기가 통하는 재료로 만들어 대상에 전기를 전달하거나 전기적 상태를 재는 부분)의 간격을 바꾸는 정전용량 센서(전기가 통하는 두 부분 사이에 전기를 저장하는 성질의 변화를 감지하는 장치)로 조직 종류와 층의 두께를 추정했다.[^p3][^p4]

### 3. 이식형 심장·혈관 보조 장치와 인공근육

심장이나 혈관을 바깥에서 압박하는 장치를 만든다. E-CAD(Electroactive Polymer-Based Cardiac Assist Device)는 전기활성 고분자(Electroactive Polymer, EAP; 반복 단위가 이어진 긴 분자로 이루어지며 전기 자극에 따라 형태나 크기가 바뀌는 물질)와 스프링을 결합해 심장 압박을 돕는 장치다. SCS(Superior-Vena-Cava Compressing Shape-Memory-Alloy-Based Implantable Device)는 형상기억합금(변형된 뒤 온도 변화 등의 조건에 따라 미리 정해진 형상을 회복하는 합금)으로 구동해 상대정맥(상체의 혈액을 심장으로 돌려보내는 큰 정맥)을 압박한다. 두 연구 모두 혈액에 직접 닿지 않는 보조 구조를 설계했다.[^p5][^p6]

### 4. 촉각 전달과 착용형 보조·재활 구동기

연구실은 원격 로봇 시술과 의료 훈련 장치에서 조작자에게 촉감을 전하는 햅틱 장치를 개발한다. 또한 몸에 착용해 움직임을 돕거나 재활에 쓰는 기기에 맞도록 유연하고 작고 가벼운 인공근육 구동기를 연구한다. 교수 소개는 의료·햅틱·물체 잡기에 필요한 기구, 구동기와 센서의 설계를 전문 분야로 든다.[^home][^prof]

## 대표 논문

한경원 교수가 저자로 참여하고 서울대 소속이 적힌 2025–2026년 논문 중 수술 항법·접촉 감지·이식형 보조 장치·의료 도구 설계를 다루는 8편을 골랐다. 최신 연구와 교수가 마지막 저자인 논문을 함께 담았다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [3D pose estimation of epidural catheter markers based on a single-view 2D X-ray fluoroscopy](https://doi.org/10.1093/jcde/qwag045) · Journal of Computational Design and Engineering | 가는 표지를 단 카테터의 입체 자세를 한 장의 엑스선 영상으로 계산한다. 모의실험으로 학습한 여러 예측 모형과 기하학적 제약을 결합해, 실험 자료를 미리 모으지 않고도 카테터를 실시간 추적하는 방법을 제시했다.[^p1] | 1저자 Jegyeong Ryu, 공저자 Amy Kyungwon Han |
| 2 | 2026 | [A conformable multimodal imaging marker for surgical navigation systems](https://doi.org/10.1038/s41528-025-00525-1) · npj Flexible Electronics | 피부에 밀착하면서 광학 추적·CT·MRI에서 함께 보이는 표지 장치를 만들었다. 적외선을 내는 소자와 영상별로 보이게 하는 재료를 결합하고, 유방 시험 모형의 로봇 시술에서 표적 위치를 안내하는 성능을 평가했다.[^p2] | 1저자 Kyung Yeun Kim, 공저자 Amy Kyungwon Han |
| 3 | 2025 | [Reliable Tissue Grasping in Robotic Minimally Invasive Surgery Enabled by Optical-Based Slip Sensing](https://doi.org/10.1002/adem.202500910) · Advanced Engineering Materials | 수술 집게와 조직 사이의 미끄럼을 빛으로 감지하는 방법을 제시했다. 수술 집게에 센서를 결합한 시험에서 조직의 직선 이동과 회전, 조직이 늘어나는 상태를 구분해 수술 중 접촉 감지의 가능성을 보였다.[^p3] | 1저자 Minjae Lee, 마지막 저자 Amy Kyungwon Han |
| 4 | 2025 | [Noninvasive Tissue Identification and Thickness Estimation Using Gap-Changing Capacitive Sensor With Machine Learning Integration](https://doi.org/10.1109/jsen.2025.3582760) · IEEE Sensors Journal | 전극 사이 간격을 바꿔 감지하는 깊이를 조절하는 센서를 제안했다. 여러 간격에서 얻은 자료를 기계학습(자료에서 규칙을 배워 예측이나 분류를 하는 계산 방법)으로 분석해 조직 종류와 첫 조직층의 두께를 추정했다.[^p4] | 1저자 Dohyun Lee, 마지막 저자 Amy Kyungwon Han |
| 5 | 2025 | [E-CAD: Electroactive Polymer-Based Cardiac Assist Device with Low Power Consumption](https://doi.org/10.1002/aisy.202500076) · Advanced Intelligent Systems | 전기활성 고분자 구동부와 스프링을 심장을 감싸는 유연한 구조에 결합했다. 심장의 부위별 기계적 성질을 고려해 압박하도록 설계했고, 모형과 적출 심장 시험에서 장치가 없을 때보다 내보내는 부피를 늘리는 결과를 보였다.[^p5] | 1저자 Jiyeop Kim, 마지막 저자 Amy Kyungwon Han |
| 6 | 2025 | [SCS: Superior-Vena-Cava Compressing Shape-Memory-Alloy-Based Implantable Device for Heart Failure](https://doi.org/10.1002/adem.202402632) · Advanced Engineering Materials | 형상기억합금 구동기로 상대정맥을 바깥에서 압박해 혈류를 조절하는 장치를 제시했다. 시험 장치에서 유량 조절을 확인하고, 동물 모형에서 심장이 피를 내보내기 전에 받는 부하를 줄일 가능성을 보였다.[^p6] | 1저자 Yongjin Kim, 마지막 저자 Amy Kyungwon Han |
| 7 | 2025 | [Machine Learning-Based Design of 3D-Printable Microneedles for Enhanced Tissue Anchoring with Reduced Tissue Damage](https://doi.org/10.1002/adem.202501165) · Advanced Engineering Materials | 기계학습과 수치해석으로 미세바늘의 형상을 최적화해 조직 고정과 삽입 힘 사이의 문제를 다뤘다. 입체 프린터로 만들 수 있는 형상을 대상으로, 기존 원뿔형 바늘과 비교해 조직 고정과 손상 억제를 함께 개선하는 설계 가능성을 보였다.[^p7] | 1저자 Jegyeong Ryu, 마지막 저자 Amy Kyungwon Han |
| 8 | 2025 | [Rapid and robust ultrasonic probe calibration employing a CT-visible randomized spherical phantom](https://doi.org/10.1093/jcde/qwaf049) · Journal of Computational Design and Engineering | 구형 표지를 무작위로 배치한 모형을 CT로 측정하고 초음파 영상과 맞추는 보정 방법을 제안했다. 초음파 영상에 나타난 타원의 모양과 위치를 이용하는 새 알고리즘으로 탐촉자와 모형의 공간 관계를 맞추고, 영상과 추적 장치 사이의 시간 지연도 보정했다.[^p8] | 1저자 Jegyeong Ryu, 공저자 Amy Kyungwon Han |

## 교수와 전문 분야

한경원(Amy Kyungwon Han) 부교수는 Georgia Institute of Technology에서 기계공학 학사(2012), Stanford University에서 기계공학 석사(2015)와 박사(2020)를 받았다. 2020–2022년 Stanford University 박사후연구원을 거쳐 2022년 서울대학교 기계공학부 조교수로 부임했고, 2026년 부교수가 됐다. 누리집은 2023년부터 서울대학교 협동과정 바이오엔지니어링 전공 겸임교수도 맡고 있다고 적는다.[^dept][^prof]

교수 소개가 밝힌 전문 분야는 햅틱·의료 응용·물체 잡기를 위한 기구, 구동기와 센서 설계다. 최근 논문에서는 이 전문성이 수술 도구 위치 추정, 조직 접촉 감지, 의료 도구 형상 설계, 전기활성 고분자 및 형상기억합금 기반 보조 장치로 이어진다.[^prof][^p1][^p3][^p5][^p6][^p7]

## 응용 분야

수술 분야에서는 카테터의 위치 추적, 수술 집게의 미끄럼 감지, 조직 종류와 두께 추정, 수술 영상과 추적 장치의 위치 관계 보정에 적용한다. 몸속 보조 장치 분야에서는 심장 압박을 돕거나 혈관을 압박해 혈류를 조절하는 장치를 설계한다. 연구실 소개는 원격 로봇 시술, 의료 훈련, 착용형 보조·재활 기기를 응용 대상으로 든다.[^p1][^p3][^p4][^p5][^p6][^p8][^home]

## 구성원

누리집 People의 대학원생과 학부생·인턴 29명이다. 개인별 과정·학년·소속 표기를 따르며, 시작은 소식에서 합류를 알린 날짜다. 「대표 논문 참여」는 위 표의 번호이고, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people][^home][^past]

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| 류제경 (Jegyeong Ryu) | 박사과정 (Year 4, Mechanical Engineering) | 2023-03-01 | 1, 2, 7, 8 |
| 안정민 (Jungmin Ahn) | 박사과정 (Year 4, Mechanical Engineering Co-advised by Prof. Kyujin Cho) |  |  |
| 김용진 (Yongjin Kim) | 박사과정 (Year 3, Mechanical Engineering) | 2022-09-01 | 6 |
| 이민재 (Minjae Lee) | 박사과정 (Year 2, Mechanical Engineering) | 2023-03-01 | 3 |
| 변성주 (Seong Joo Byeon) | 박사과정 (Year 2, Mechanical Engineering) |  |  |
| Sihan Yang | 박사과정 (Year 2, Mechanical Engineering) | 2025-03-01 |  |
| 송세인 (Sein Song) | 박사과정 (Year 1, Mechanical Engineering) | 2024-03-01 | 5 |
| 엄태준 (Taejoon Um) | 석사과정 (Year 2, Mechanical Engineering) | 2025-03-01 |  |
| 김수민 (Sumin Kim) | 석사과정 (Year 2, Mechanical Engineering) | 2025-03-01 |  |
| 양진원 (Jinwon Yang) | 석사과정 (Year 2, Mechanical Engineering) | 2025-03-01 |  |
| 이창준 (Chang Jun Lee) | 석사과정 (Year 2, Mechanical Engineering) | 2025-03-01 |  |
| 전용주 (Yong Ju Jeon) | 석사과정 (Year 2, Mechanical Engineering) |  |  |
| Tammy Tang Hoi Yuen | 석사과정 (Year 2, Mechanical Engineering) |  |  |
| 조도민 (Do Min Cho) | 석사과정 (Year 1, Mechanical Engineering) | 2026-03-01 |  |
| 이성환 (Seonghwan Lee) | 석사과정 (Year 1, Mechanical Engineering) | 2026-03-01 |  |
| 김석희 (Seokhee Kim) | 석사과정 (Year 1, Mechanical Engineering) | 2026-03-01 |  |
| 홍현진 (Hyun Jin Hong) | 석사과정 (Year 1, Mechanical Engineering) |  |  |
| 권재현 (Jayhyun Kwon) | 석사과정 (Year 1, Mechanical Engineering) | 2026-09-01 |  |
| 하홍준 (Hongjun Ha) | 학부 연구생 (Year 4, Mechanical Engineering BS-MS/PhD Program) | 2026-09-01 |  |
| 김충만 (Chungman Kim) | 학부 연구생 (Year 4, Mechanical Engineering) |  |  |
| 배규석 (Gyuseok Bae) | 학부 연구생 (Year 4, Mechanical Engineering) |  |  |
| 임태건 (Taegun Lim) | 학부 연구생 (Year 4, Mechanical Engineering) |  |  |
| 김동현 (Donghyun Kim) | 학부 연구생 (Year 3, Mechanical Engineering, Yonsei University) |  |  |
| 김재현 (Jaehyun Kim) | 학부 연구생 (Year 2, Mechanical Engineering) |  |  |
| 김원재 (Wonjae Kim) | 학부 연구생 (Year 4, Mechanical Engineering) |  |  |
| 임준환 (Junhwan Lim) | 학부 연구생 (Year 2, Mechanical Engineering) |  |  |
| 최다민 (Damin Choi) | 학부 연구생 (Year 4, Mechanical Engineering, Ehwa Womans University) |  |  |
| 윤수빈 (Subin Yun) | 학부 연구생 (Year 3, Mechanical Engineering) |  |  |
| 이수빈 (Subin Lee) | 학부 연구생 (Year 4, Mechanical Engineering) |  |  |

## 졸업생과 이전 구성원

누리집 Alumni의 박사후연구원 1명, 석사 3명, 방문 대학원생 3명, 인턴 38명으로 모두 45명이다. 과정·소속과 시기는 게시 표기이며, 방문 대학원생과 인턴의 학교는 해당 항목이 적은 소속이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 박찬영 (Chan Young Park) | 박사후연구원 (Feb 2026) |  |
| 이정현 (Jeong Hyeon Lee) | 석사 (Feb 2025) |  |
| 김지엽 (Jiyeop Kim) | 석사 (Aug 2025) |  |
| 이준헌 (Jun Heon Lee) | 석사 (Feb 2026) |  |
| Svetlana Shachneva | 방문 대학원생 (Mechanical Engineering, University of Stuttgart) (Jul 2025–Aug 2025) |  |
| Bjørn Leth Møller | 방문 대학원생 (Comuter Science, University of Copenhagen) (Mar 2025–Jun 2025) |  |
| Nam Phuong Dam | 방문 대학원생 (JAIST) (Sep 2023) |  |
| 박연수 (Yeonsu Park) | 인턴 (Mechanical Engineering, SNU) (Jan 2025–Aug 2026) |  |
| 김민지 (Minji Kim) | 인턴 (Mechanical Engineering, GIST) (Nov 2025–Aug 2026) |  |
| 전인재 (Injae Jun) | 인턴 (Mechanical Engineering, SNU) (Dec 2024–Aug 2026) |  |
| 남정우 (Jungwoo Nam) | 인턴 (NVOT High School) (Jul 2026) |  |
| 박도연 (Doyeon Park) | 인턴 (Mechanical Engineering, SNU) (Jun 2025–Feb 2026) |  |
| 김동현 (Donghyun Kim) | 인턴 (Mechanical Engineering, Yeonsei University) (Dec 2025–Feb 2026) |  |
| 김민성 (Minsung Kim) | 인턴 (Mechanical Engineering, SNU) (Jun 2025–Dec 2025) |  |
| 이윤수 (Yunsu Yi) | 인턴 (Mechanical Engineering, SNU) (Dec 2024–Dec 2025) |  |
| 정다혜 (Dahye Jeong) | 인턴 (Mechanical Engineering, Korea University) (Jun 2025–Aug 2025) |  |
| 허승휘 (SeungHui Huh) | 인턴 (Computer Science, MS, Georgia Tech) (Dec 2024–Jun 2025) |  |
| 이건무 (Geonmoo Lee) | 인턴 (Mechanical Engineering, SNU) (Sep 2024–Jun 2025) |  |
| 김동광 (Dong Gwang Kim) | 인턴 (Mechanical Engineering, SNU) (Jun 2024–Jun 2025) |  |
| 조민 (Min Joh) | 인턴 (Mechanical Engineering, University of Alberta) (Dec 2024–Feb 2025) |  |
| 손호정 (Ho Jeong Son) | 인턴 (Mechanical Engineering, SNU) (Jun 2024–Feb 2025) |  |
| 현나린 (Narin Hyeon) | 인턴 (Mechanical Engineering, SNU) (Jun 2024–Feb 2025) |  |
| 김수인 (Suin Kim) | 인턴 (Mechanical Engineering, SNU) (Mar 2024–Dec 2024) |  |
| 이승섭 (Seungsup Lee) | 인턴 (Mechanical Engineering, SNU) (Mar 2024–Dec 2024) |  |
| 신창현 (Changhyun Shin) | 인턴 (Mechanical Engineering, Korea University) (Sep 2024–Nov 2024) |  |
| 김하선 (Haseon Kim) | 인턴 (Mechanical Engineering, Ajou University) (Jun 2024–Aug 2024) |  |
| 안제경 (Jegyeong An) | 인턴 (Mechanical Engineering, Korea University) (Jun 2024–Aug 2024) |  |
| 이현우 (Hyunwoo Lee) | 인턴 (Mechanical Engineering, NTU) (Jun 2024–Aug 2024) |  |
| 이도현 (Do Hyun Lee) | 인턴 (Mechanical Engineering, SNU) (Apr 2022–Aug 2024) |  |
| 최동수 (Dongsu Choi) | 인턴 (Mechanical Engineering, SNU) (Sep 2023–Jun 2024) |  |
| 한원준 (Wonjun Han) | 인턴 (Mechanical Engineering, SNU) (Mar 2024–May 2024) |  |
| Manami Oinuma | 인턴 (Mechanical Engineering, The University of Electro-Communications) (Jan 2024–Mar 2024) |  |
| 정승겸 (Seunggyeom Jung) | 인턴 (Mechanical Engineering, DGIST) (Jan 2024–Feb 2024) |  |
| 김재훈 (Jaehun Kim) | 인턴 (Mechanical Engineering, SNU) (Mar 2023–Dec 2023) |  |
| 이수미 (Soomi Lee) | 인턴 (Mechanical Engineering, SNU) (Mar 2023–Dec 2023) |  |
| 이상민 (Sang Min Lee) | 인턴 (Mechanical Engineering, SNU) (Jun 2023–Aug 2023) |  |
| Nathan Joonchul Tan | 인턴 (Mechanical Engineering, Stanford University) (Jun 2023–Aug 2023) |  |
| 김강산 (Gang San Kim) | 인턴 (Mechanical Engineering, SNU) (Dec 2022–Jun 2023) |  |
| 박기현 (Gi Hyun Park) | 인턴 (Mechanical Engineering, SNU) (Sep 2022–Jun 2023) |  |
| 박채환 (Chae Hwan Park) | 인턴 (Mechanical Engineering, Hanyang University) (Dec 2022–Feb 2023) |  |
| 김솔 (Sol Kim) | 인턴 (Mechanical Engineering, SNU) (Apr 2022–Dec 2022) |  |
| 김인영 (In Young Kim) | 인턴 (Mechanical Engineering, SNU) (Mar 2022–Dec 2022) |  |
| 정윤종 (Yoonjong Jung) | 인턴 (Mechanical Engineering, SNU) (Mar 2022–Dec 2022) |  |
| 이주형 (Juhyeong Lee) | 인턴 (Mechanical Engineering, SNU) (Jun 2022–Aug 2022) |  |
| 이소민 (Somin Mindy Lee) | 인턴 (Engineering Science, University of Toronto) (May 2022–Aug 2022) |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications에 게시된 2022–2026년 논문 18편이다. 원 목록에는 한경원 교수의 2022년 서울대 부임 전 논문도 함께 있으며, 아래 2022년 논문은 서울대 소속이 적힌 논문이다. 연도·저자·발표처는 연구실의 게시 표기다. 논문 옆 †와 * 표시는 누리집 표시다.[^pubs][^prof][^oa]

**2026**

- Jegyeong Ryu, Jae Chul Koh, Amy Kyungwon Han\*, and Deukhee Lee\*. "3D Pose Estimation of Epidural Catheter Markers based on a Single-View 2D X-ray Fluoroscopy". *Journal of Computational Design and Engineering (2026). DOI: <https://doi.org/10.1093/jcde/qwag045>*.
- Nam Phuong Dam, Jiyeop Kim, Amy Kyungwon Han, and Van Anh Ho. "FlexSeal: Passive Pinhole Valve Suction for PneuNet Gripper with One-way Flow Object Attachment and Release". *RoboSoft 2026 (2026). DOI: <https://doi.org/10.1109/robosoft67810.2026.11522913>*.
- Kyung Yeun Kim†, Jegyeong Ryu†, Joohyuk Kang†, Bongkyun Jang, Ji-young Lee, Yu-Chan Kim, Amy Kyungwon Han, Jae-Hoon Han, Hojeong Jeon, Seung Hwan Ko, Deukhee Lee, and Wonryung Lee. "A conformable multimodal imaging marker for surgical navigation systems". *npj Flexible Electronics (2026). DOI: <https://doi.org/10.1038/s41528-025-00525-1>*.

**2025**

- Jegyeong Ryu†, Jiyeop Kim†, Chan Wook Park, Hae-Yoon Kim, Deukhee Lee\*, and Amy Kyungwon Han\*. "Machine Learning-Based Design of 3D-Printable Microneedles for Enhanced Tissue Anchoring with Reduced Tissue Damage". *Advanced Engineering Materials (2025). DOI: <https://doi.org/10.1002/adem.202501165>*.
- Minjae Lee and Amy Kyungwon Han. "Reliable Tissue Grasping in Robotic Minimally Invasive Surgery Enabled by Optical‐Based Slip Sensing". *Advanced Engineering Materials (2025). DOI: <https://doi.org/10.1002/adem.202500910>*.
- Dohyun Lee, Hae Yoon Kim, Bjørn Leth Møller, Joonseok Lee, Jang W. Yoon, Chi Heon Kim, and Amy Kyungwon Han. "Non-Invasive Tissue Identification and Thickness Estimation Using Gap-Changing Capacitive Sensor with Machine Learning Integration". *IEEE Sensors Journal (2025). DOI: <https://doi.org/10.1109/jsen.2025.3582760>*.
- Jiyeop Kim, Junheon Lee, Sein Song, Si‐Hyuck Kang\*, and Amy Kyungwon Han\*. "E‐CAD: Electroactive Polymer‐Based Cardiac Assist Device with Low Power Consumption". *Advanced Intelligent Systems (2025). DOI: <https://doi.org/10.1002/aisy.202500076>*.
- Jegyeong Ryu, Nova Eka Diana, Gyuwon Kang, Chan Wook Park, Amy Kyungwon Han\*, Deukhee Lee\*. "Rapid and robust ultrasonic probe calibration employing a CT-visible randomized spherical phantom". *Journal of Computational Design and Engineering (2025). DOI: <https://doi.org/10.1093/jcde/qwaf049>*.
- Ali Kight, Moussa Haidar, Masafumi Shibata, Yoshikazu Ono, Gentaro Ikeda, Amit Sharir, Federica Semproni, Yellappa Palagani, Sawson Taheri, Amy Kyungwon Han, Michael Ma, Kirk Riemer, Doff B. McElhinney, Seraina A. Dual, Mark Cutkosky. "VITALS: an implantable sensor network for postoperative cardiac monitoring in heart failure patients". *npj Biomedical Innovations (2025). DOI: <https://doi.org/10.1038/s44385-025-00017-x>*.
- Yongjin Kim†, Jeonghyeon Lee†, Jeongwon Kim, Domin Cho, Hyunwoo Lee, Se Jin Oh\*, Amy Kyungwon Han\*. "SCS: Superior-Vena-Cava Compressing Shape-Memory-Alloy-Based Implantable Device for Heart Failure". *Advanced Engineering Materials (2025). DOI: <https://doi.org/10.1002/adem.202402632>*.
- Jun Young Choi, Geun Young Kim, Do Hoi Kim, Narae Yoon, Amy Kyungwon Han, Sung-Hoon Ahn. "Data-driven analysis of bonding strength in laser-structured metal-GFRP hybrid joints via groove morphology". *The International Journal of Advanced Manufacturing Technology (2025). DOI: <https://doi.org/10.1007/s00170-024-14881-1>*.

**2023**

- Hajj-Ahmad, A.\*, Han, A.K.\*, Lin, M.A., Glover, G.H., and Cutkosky, M.R. "An Electrostatically Actuated Gecko Adhesive Clutch". *Advanced Materials Technologies (2023). DOI: <https://doi.org/10.1002/admt.202202025>*.
- Pirozzi, I., Kight, A., Han, A. K., Cutkosky, M.R., and Dual, S.A. "Circulatory Support: Artificial Muscles for the Future of Cardiovascular Assist Devices". *Advanced Materials (2023). DOI: <https://doi.org/10.1002/adma.202210713>*.
- Kight, A., Pirozzi, I., Liang, X.Y., McElhinney, D.B., Han, A.K., Dual, S.A., and Cutkosky, M.R. "Decoupling Transmission and Transduction for Improved Durability of Highly Stretchable, Soft Strain Sensing: Applications in Human Health Monitoring". *Sensors 23(4), 1955 (2023). DOI: <https://doi.org/10.3390/s23041955>*.

**2022**

- Ham, J., Han, A.K., Cutkosky, M.R., Bao, Z. "UV-laser-machined stretchable multi-modal sensor network for soft robot interaction". *npj Flexible Electronics 6, 94 (2022). DOI: <https://doi.org/10.1038/s41528-022-00225-0>*.
- Pirozzi, I., Kight, A., Liang, X.Y., Han, A.K., Ennis, D.E., Hiesinger, W., Dual, S.A., Cutkosky, M.R. "Electrohydraulic Vascular Compression Device (e-VaC) with Integrated Sensing and Controls". *Advanced Materials Technologies (2022). DOI: <https://doi.org/10.1002/admt.202201196>*.
- Han, A.K.\*, Hajj-Ahmad, A.\*, and Cutkosky, M.R. "Bimanual Handling of Deformable Objects With Hybrid Adhesion". *IEEE Robotics and Automation Letters (2022), vol. 7, no. 2, pp. 5497-5503, doi: 10.1109/LRA.2022.3158231*.
- Pirozzi, I.\*, Kight, A.\*, Shad, R.A., Han, A.K., Dual, S.A., Fong, R., Jia, A., Hiesinger, W., Yock, P. and Cutkosky, M. "RVEX: Right Ventricular External Device for Biomimetic Support and Monitoring of the Right Heart". *Advanced Materials Technologies (2022) p.2101472. DOI: <https://doi.org/10.1002/admt.202101472>*.

## 수상과 선정

누리집 Lab Awards와 소식의 2022년 6월 23일–2026년 4월 3일 수상·선정 항목 38건이다. 수상 이름과 등급은 누리집 표기를 따르고, 날짜는 소식에 적힌 날짜다. 교수 개인의 전체 수상 목록에는 2022년 서울대 부임 전 항목도 함께 있다.[^home][^past][^prof]

- 2026-04-03 · Jungmin Ahn: Best Poster Presentation Award, Medical Metaverse Conference
- 2025-11-29 · Sein Song: Excellent Oral Presentation Award, Korea Innovative Medical Technology Conference
- 2025-11-29 · Sumin Kim, Taejoon Um, Jungmin Ahn: Excellent Innovative Medical Technology Award, Korea Innovative Medical Technology Conference
- 2025-11-28 · Do Min Cho, Injae Jun: Busan Metropolitan City Mayor's Award, COSS Next-Generation Semiconductor MCU Application Contest
- 2025-10-24 · Yongjin Kim: Next-Generation Engineering Researcher Excellence Award, Institute for Promotion of Engineering and Science of Korea (IPESK)
- 2025-10-20 · Jegyeong Ryu: Best Poster Award, IROS Workshop
- 2025-10-20 · Sihan Yang: Best Paper Finalist, IROS Workshop
- 2025-08-28 · Jiyeop Kim: Best Master’s Thesis Award, Seoul National University
- 2025-08-13 · Amy K. Han: New Leader Award in Science, World Federation of Power Leaders (WFPL)
- 2025-07-11 · Jegyeong Ryu, Yeonsu Park, Jiyeop Kim, Sanghyeon, Yongju Jeon: Best Work-in-Progress Paper Award, IEEE World Haptics Conference (WHC)
- 2025-07-11 · Hero Lab: Top Demonstration Contributor Award, IEEE World Haptics Conference (WHC)
- 2025-04-04 · Seong Joo Byeon: Excellent Oral Presentation Award, Medical Metaverse Conference
- 2025-02-26 · Jeonghyeon Lee: Best Master’s Thesis Award, Seoul National University
- 2025-02-14 · Yongjin Kim, Jeonghyeon Lee, Do Min Cho: Excellent Paper Award, Korea Robotics Conference (KRoC)
- 2025-02-13 · Amy K. Han: Rising Star of RoboSoft, IEEE International Conference on Soft Robotics (RoboSoft)
- 2024-12-20 · Jungmin Ahn, Yongjin Kim: Grand Prize, SNU Graduate Entrepreneurship Club Demo Day
- 2024-12-06 · Taejoon Um, Yong Joo Jeon: Outstanding Undergraduate Thesis Presentation Award, Seoul National University
- 2024-10-08 · Jegyeong Ryu: Innovation in Haptics Research Grant, IEEE RAS Technical Committee on Haptics
- 2024-09-28 · Seong Joo, Jeong Hyeon, Narin, Ho Jung, Jungmin: Best Poster Presentation Awards, Medical Metaverse Conference
- 2024-09-28 · Amy K. Han: Best Oral Presentation Award, Medical Metaverse Conference
- 2024-09-09 · Amy K. Han: MIT Technology Review 아시아·태평양 혁신가 선정
- 2024-08-21 · Sumin Kim, Taejoon Um, Minjae Lee, Jeong Hyeon Lee: 1st Place, Student Innovation Challenge, Korea Haptics Conference
- 2024-06-28 · Jungmin Ahn, Yongjin Kim: Runner-up(차점), Best Student Poster, Hamlyn Symposium Workshop
- 2024-05-13 · Amy K. Han: New Generation Star, ICRA 2024 / Nokov
- 2024-04-29 · Amy K. Han: APBEC Young Scholar Award, Asia Pacific Biomedical Engineering Consortium
- 2024-01-25 · Yongjin Kim: Outstanding Teaching Assistant Award, SNU Mechatronics
- 2023-12-08 · Do Hyun Lee, Soomi Lee: Outstanding Undergraduate Thesis Presentation Award, Seoul National University
- 2023-11-24 · Sang Hyun Lee, Seong Joo Byun, Jegyeong Ryu, Yongjin Kim: 1st Place, Student Innovation Challenge, Korea Haptics Conference
- 2023-11-10 · Amy K. Han: KIMTEC Innovation Award Grand Prize, Korean Innovative Medical Technology Society
- 2023-10-04 · Amy K. Han: Women in Robotics 선정
- 2023-06-09 · Gi Hyun Park: Outstanding Undergraduate Thesis Presentation Award, Seoul National University
- 2023-05-22 · Amy K. Han: Best RA-L Paper Award, IEEE Robotics and Automation Letters
- 2023-02-09 · Jiyeop Kim: Outstanding Teaching Assistant Award, SNU Mechatronics
- 2023-02-02 · Jun Heon Lee: Excellence Award, SNU Undergraduate Research Program
- 2022-12-09 · In Young Kim, Yoonjong Jung: Outstanding Undergraduate Thesis Presentation Award, Seoul National University
- 2022-10-20 · Amy K. Han: Young Engineer Award, Korean Society for Precision Engineering
- 2022-07-15 · Dohyun Lee: 2nd Place, Living Appliance Technology Idea Competition, Samsung–SNU
- 2022-06-23 · Amy K. Han: Outstanding Early Career Researcher Award, Institute of Control, Robotics, and Systems

## 소식

누리집 첫 화면과 Past Lab News의 2022년 3월 1일–2023년 4월 5일 연구실 출범·논문 출판 소식 6건이다.[^home][^past]

- 2023-04-05 · 정전기로 상태를 바꾸는 도마뱀붙이 접착 클러치 논문이 Advanced Materials Technologies에 온라인 출판됐다.
- 2023-02-24 · 심혈관 보조 장치용 인공근육을 다룬 리뷰 논문이 Advanced Materials에 온라인 출판됐다.
- 2023-02-09 · 변형 전달과 신호 변환을 분리한 신축성 변형 센서 논문이 Sensors에 온라인 출판됐다.
- 2022-11-20 · 소프트 로봇 상호작용용 신축성 다중 감지 센서망 논문이 npj Flexible Electronics에 온라인 출판됐다.
- 2022-11-15 · 감지·제어를 통합한 전기유압 혈관 압박 장치 논문이 Advanced Materials Technologies에 온라인 출판됐다.
- 2022-03-01 · 헬스케어 로보틱스 연구실이 공식 출범했다.

## 참여 안내

연구실은 의료 분야 문제를 풀고자 하는 학부생·대학원생·박사후연구원의 지원을 안내한다. 로봇공학, 기계 설계, 모형화 또는 제어 경험과 연구 관심을 설명하고 이력서·성적표 등을 보내도록 적는다. 대학원 지원자는 서울대학교 원서 제출 전에 교수에게 연락하도록 안내한다.[^join]

## 연락과 위치

- 연구실: 서울특별시 관악구 관악로 1 서울대학교 312동 209호, 우편번호 08826[^contact][^dept]
- 교수실: 서울대학교 301동 1406호[^dept]
- 누리집 연락 전화: +82-2-880-1678[^contact]
- 학부 교수 소개 전화: 02-880-1649[^dept]
- 교수 이메일: amyhan@snu.ac.kr[^dept]
[^research]: Healthcare Robotics Lab, 현재 연구 소개와 Research Areas. <https://hero.snu.ac.kr/home> (관측 2026-11-07).
[^home]: Healthcare Robotics Lab, 연구실 소개·연구 분야·소식·수상. <https://hero.snu.ac.kr/home> (관측 2026-11-07).
[^dept]: 서울대학교 기계공학부, 한경원 교수 소개. <https://me.snu.ac.kr/snu__professor/%ed%95%9c%ea%b2%bd%ec%9b%90-han-amy-kyungwon/> (관측 2026-11-07).
[^past]: Healthcare Robotics Lab, Past Lab News. <https://hero.snu.ac.kr/past-news> (관측 2026-11-07).
[^prof]: Healthcare Robotics Lab, Amy Kyungwon Han 교수 소개. <https://hero.snu.ac.kr/people/amyhan> (관측 2026-11-07).
[^people]: Healthcare Robotics Lab, People. <https://hero.snu.ac.kr/people> (관측 2026-11-07).
[^alumni]: Healthcare Robotics Lab, Alumni. <https://hero.snu.ac.kr/alumni> (관측 2026-11-07).
[^pubs]: Healthcare Robotics Lab, Publications. <https://hero.snu.ac.kr/publications> (관측 2026-11-07).
[^oa]: OpenAlex, Amy Kyungwon Han의 2021–2026년 논문 서지·초록·저자 소속. <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044337518,publication_year:2021-2026> (관측 2026-11-07).
[^join]: Healthcare Robotics Lab, Join. <https://hero.snu.ac.kr/join> (관측 2026-11-07).
[^contact]: Healthcare Robotics Lab, Contact. <https://hero.snu.ac.kr/contact> (관측 2026-11-07).
[^p1]: J. Ryu, J. C. Koh, A. K. Han, D. Lee, Journal of Computational Design and Engineering (2026). <https://doi.org/10.1093/jcde/qwag045> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044337518,publication_year:2021-2026> (관측 2026-11-07).
[^p2]: K. Y. Kim 외, W. Lee, npj Flexible Electronics (2026). <https://doi.org/10.1038/s41528-025-00525-1> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044337518,publication_year:2021-2026> (관측 2026-11-07).
[^p3]: M. Lee, A. K. Han, Advanced Engineering Materials (2025). <https://doi.org/10.1002/adem.202500910> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044337518,publication_year:2021-2026> (관측 2026-11-07).
[^p4]: D. Lee 외, A. K. Han, IEEE Sensors Journal (2025). <https://doi.org/10.1109/jsen.2025.3582760> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044337518,publication_year:2021-2026> (관측 2026-11-07).
[^p5]: J. Kim 외, A. K. Han, Advanced Intelligent Systems (2025). <https://doi.org/10.1002/aisy.202500076> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044337518,publication_year:2021-2026> (관측 2026-11-07).
[^p6]: Y. Kim 외, A. K. Han, Advanced Engineering Materials (2025). <https://doi.org/10.1002/adem.202402632> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044337518,publication_year:2021-2026> (관측 2026-11-07).
[^p7]: J. Ryu 외, A. K. Han, Advanced Engineering Materials (2025). <https://doi.org/10.1002/adem.202501165> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044337518,publication_year:2021-2026> (관측 2026-11-07).
[^p8]: J. Ryu 외, D. Lee, Journal of Computational Design and Engineering (2025). <https://doi.org/10.1093/jcde/qwaf049> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044337518,publication_year:2021-2026> (관측 2026-11-07).

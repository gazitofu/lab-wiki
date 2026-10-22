# 생체기계 연구실 (Biorobotics Lab)

**KAIST 기계공학과 · 김정 교수**

- 분야: 햅틱과 물리적 인간–로봇 상호작용, 로봇 촉각 센싱과 로봇 피부, 촉각 기반 로봇 조작, 표면 근전도 신호 처리와 동작 의도 인식, 착용형 로봇과 착용형 센서, 소프트 로보틱스, 로봇 구동기와 동력 전달
- 대분야: 기계·로봇·제조, 전기전자·반도체·광학
- 태그: 햅틱[^home][^prof], 인간–로봇 상호작용[^home][^prof][^p2], 로봇 구동기·센서[^tactile][^actuator][^p8], 착용형 로봇·외골격[^wearable][^p6], 소프트 로보틱스[^soft][^p7], 착용형 생체 센서[^biosig][^p5], 재활·보조·접근성 기술[^wearable][^p4]
- 홈페이지: <https://biorobotics.kaist.ac.kr/>
- 근거와 출처: [생체기계 연구실 근거 페이지](biorobotics-sources.md)

> 사람과 기계가 몸으로 맞닿아 함께 일하는 환경을 겨냥해, 로봇이 촉감을 느끼게 하는 로봇 피부와 촉각 센서, 근육의 전기 신호로 사람의 움직임 의도를 알아내는 기술, 사람 몸에 입히는 착용형 로봇, 부드러운 소재로 만든 소프트 로봇을 연구하는 기계공학과 연구실이다. 2004년에 문을 열었다.[^home][^prof]

## 무엇을 연구하나

연구실 첫 화면은 2004년에 문을 연 이 연구실이 여러 분야가 모인 연구 그룹이며, 다양한 환경에서 햅틱(진동·힘 같은 촉감을 사람에게 전하거나 촉각을 재는 기술)과 물리적 인간–로봇 상호작용(사람과 로봇이 몸으로 맞닿아 힘을 주고받는 상호작용)을 연구한다고 소개한다.[^home] 연구의 목표는 사람과 기계가 가까이 맞닿아 함께 움직이는, 정돈되지 않은 환경에 정보 기술과 지능형 기계를 녹여 넣는 것이라고 적는다.[^home] 이를 위해 생체역학 시스템의 모델링, 표면 근전도(sEMG, 피부에 붙인 전극으로 근육이 수축할 때 생기는 전기 신호를 재는 방법)를 바탕으로 한 동작 의도 인식, 정신물리학(물리적 자극과 사람이 느끼는 감각의 관계를 재는 학문), 촉각 센서, 운동 제어, 실시간 로봇 피부, 조작 기술을 쓴다고 든다.[^home] 연락 페이지는 연구실을 로봇 기술을 생체 의공학 응용에 적용하는 문제들을 다루는 융합 연구 그룹으로 적는다.[^contact]

연구실 Professor 페이지는 교수의 주된 연구 관심을 의공학과 물리적 인간–기계 상호작용으로 적고, 그 안에서 햅틱과 로봇의 지각, 생체 신호를 바탕으로 한 물리적 인간–로봇 상호작용, 로봇을 위한 촉각 학습, 건강 감시와 생체역학 분석을 위한 착용형 센서, 소프트 로보틱스를 든다.[^prof] 기계공학과 교수 소개는 연구 분야를 Biorobotics, Bioinstrumentation, Haptics, Physical HRI로 적고, 학과 연구분야 안내의 「헬스케어/나노/광학」 분야는 이 연구실의 연구 주제로 Medical Robotics, Physical Human Robot Interactions, Soft Robotics, Haptics를 적는다.[^meprof][^meres]

누리집 Research 메뉴는 연구를 생체 신호 처리(Bio-signal Processing), 로봇 구동기(Robotics Actuator), 로봇 조작(Robotics Manipulation), 로봇 촉각 센싱(Robotics Tactile Sensing), 소프트 로보틱스(Soft Robotics), 착용형 로보틱스(Wearable Robotics)의 여섯 갈래로 나누고, 갈래마다 대표 연구와 관련 논문을 소개한다.[^biosig][^actuator][^manip][^tactile][^soft][^wearable] 2021–2026년 논문 목록에는 로봇 피부와 촉각 센서, 촉각으로 물체를 알아보는 로봇 조작, 고밀도 근전도로 손동작을 알아보는 연구, 착용형 센서 수트와 외골격, 소프트 로봇과 변속기 연구가 고르게 있다.[^pubs]

## 주요 연구 주제

### 1. 로봇 촉각 센싱과 로봇 피부

로봇의 몸 넓은 면적을 덮어 접촉을 느끼게 하는 로봇 피부와 촉각 센서를 만든다. Robotics Tactile Sensing 페이지는 전기 임피던스 단층촬영(EIT, 물체 둘레에 배치한 전극들 사이의 전기 신호를 재서 내부의 전기 성질 분포를 영상으로 되살리는 방법)을 쓰는 촉각 센서를 심층 신경망으로 해석해 촉각 공간 해상도를 높이는 EIT-NN, 전기 저항 단층촬영(ERT, EIT와 같은 원리로 내부의 저항 분포를 되살리는 방법)을 쓰는 넓은 면적 촉각 센서에서 전극 수를 늘릴수록 측정 횟수와 계산량이 늘어나는 문제를 다루는 적응형·최적 측정 알고리즘, 부드러운 소재 속에 마이크를 드문드문 넣어 토닥이기나 찰싹 때리기 같은 접촉의 종류와 위치를 알아내는 큰 면적 로봇 피부를 소개한다.[^tactile] 대표 논문 1은 질긴 하이드로겔(물을 많이 머금은 고분자 그물 구조의 무른 소재)과 실리콘 엘라스토머(고무처럼 늘었다 돌아오는 고분자)를 겹친 다층 구조에 전극과 마이크를 넣고, 단층 영상화와 심층 신경망으로 여러 종류의 촉각 정보를 얻는 사람 피부를 닮은 로봇 피부다.[^p1] 대표 논문 2는 다중 모드 감지 모듈과 다층 직물로 몸 전체 크기의 로봇 피부를 만들어 상용 로봇 팔에 붙이고 사람의 접촉을 해석했다.[^p2] 논문 목록에는 사람 피부의 층 구조와 파치니 소체(피부 속에서 진동을 느끼는 감각 수용기)를 닮은 사회적 상호작용용 로봇 피부(IEEE/ASME TMECH), 인간형 로봇 얼굴에 적용한 그래프 구조 초해상도 단층 촉각 센싱(IEEE T-RO)도 있다.[^pubs] 대표 논문 1, 2.

### 2. 촉각 기반 로봇 조작

로봇 손가락의 촉각 정보로 물체를 잡고 알아보는 방법을 연구한다. Robotics Manipulation 페이지는 자외선(UV) 표식을 켜고 끌 수 있어 표식 영상과 반사막 영상을 분리하는 비전 기반 촉각 센서(카메라로 센서 표면의 변형을 찍어 접촉을 재는 촉각 센서) 손가락 UVtac, 사람이 물체를 쥘 때처럼 예측한 촉각 사건과 실제 촉각 사건을 비교해 잡기 단계를 넘기는 촉각 사건 기반 잡기 알고리즘, 원격 조종에서 사용자 의도에 따라 반응을 바꾸는 잡기 보조를 소개한다.[^manip] 대표 논문 3은 한 쌍의 비전 기반 촉각 센서 측정을 점 구름(공간 속 점들의 좌표 모음으로 물체 모양을 나타낸 자료)으로 나타내 손에 쥔 물체의 종류와 자세를 함께 추정하고, 시뮬레이션 자료로 먼저 학습한 뒤 실제 자료로 다듬었다.[^p3] 논문 목록에는 생성적 적대 신경망으로 표식이 든 촉각 영상을 만드는 연구(IEEE RA-L), 시각·촉각 측정으로 물체의 바깥 접촉면을 되살리는 연구(IROS 2025)도 있다.[^pubs] 대표 논문 3.

### 3. 생체 신호 처리와 동작 의도 인식

근육의 전기 신호로 사람의 움직임 의도를 읽어 로봇 제어에 쓴다. Bio-signal Processing 페이지는 여러 채널의 표면 근전도로 주요 근육의 활성을 예측해 관절 토크를 추정하는 방법과, 전도성 직물 전극과 연성 회로 기판, 실리콘 고무 외피로 피부 곡면에 맞게 휘는 표면 근전도 센서를 소개한다.[^biosig] 이 센서는 착용형 로봇에 쓰였고, 직물형은 호흡 근육에 붙여 착용자의 건강 상태를 평가할 지표를 얻는 데 쓰였다고 적는다.[^biosig] 대표 논문 4는 16채널 전극으로 근전도의 잡음을 지연 없이 줄이는 확률적 근전도 처리기를 만들어 팔꿈치 굽힘 토크를 추정했다.[^p4] 논문 목록에는 고밀도 표면 근전도(HD-sEMG, 전극을 촘촘히 배열해 근육 활동을 넓게 재는 방법)와 트랜스포머 모델로 손동작을 알아보는 연구(ICORR 2025, IROS 2025), 만성 뇌졸중 환자의 손 쥐기 의도를 고밀도 근전도로 알아보는 연구(EMBC 2023)도 있다.[^pubs] News 페이지는 생체 전위와 생체 임피던스를 쓴 인간–로봇 상호작용을 다룬 리뷰 논문이 2025년 Nature Reviews Electrical Engineering에 실렸다고 적는다.[^news] 대표 논문 4.

### 4. 착용형 로봇과 착용형 센서

사람 몸에 입혀 움직임을 돕는 착용형 로봇과, 걸음과 근육 상태를 재는 착용형 센서를 만든다. Wearable Robotics 페이지는 몸통에 차는 작은 맞춤형 압축기로 공압을 만들어 발목-발 보조기(AFO, 발목과 발을 감싸 걸음을 돕는 보조 장치)를 움직이고, 발 처짐 환자 다섯 명에게 시험한 연구와, 들어 올리는 동작에서 허리 부담을 덜어 주는 휴대형 공압 허리 보조 외골격(몸 바깥에 입는 뼈대 모양의 보조 장치)을 소개한다.[^wearable] 대표 논문 5는 피부에 닿지 않는 신축 센서와 공압 근음도 센서를 넣은 바지형 센서 수트로 걷는 환경을 분류했고, 대표 논문 6은 허리 보조 외골격의 보조 시점을 표면 근전도로 앞당겼다.[^p5][^p6] 논문 목록에는 발 처짐 환자의 발목 등굽힘을 돕는 동력 발목-발 보조기(JNER 2023), 무릎 착용형 소프트 로봇을 위한 팽창형 배기 밸브(IJCAS 2025)도 있다.[^pubs] 대표 논문 5, 6.

### 5. 소프트 로보틱스

부드럽고 잘 휘는 소재로 로봇과 구동기를 만든다. Soft Robotics 페이지는 천으로 만든 납작한 공압 인공 근육(공기압으로 줄어들며 힘을 내는 구동기)에 직물형 정전용량 수축 센서를 넣은 착용 로봇용 구동기, 전도성 액체로 굽힘 구동과 촉각·고유 감각(자기 몸의 모양과 위치를 스스로 느끼는 감각)을 함께 하는 종이접기 구조 로봇 손가락, 극피동물의 근골격 구조를 본뜬 가변 강성(필요에 따라 단단해지거나 물러지는 성질) 소프트 구동기를 소개한다.[^soft] 앞의 공압 인공 근육 논문은 ICRA 2021에서 서비스 로봇 분야 최우수 논문상을 받았다고 적는다.[^soft] 대표 논문 7은 열에 반응하는 고분자 필름에 금속 저항을 촘촘히 넣어 현장에서 접히는 선을 전자적으로 고르는 로봇 시트다.[^p7] 논문 목록에는 소프트 로봇의 고유 감각을 시뮬레이션에서 실제로 옮기는 비지도 학습(Soft Robotics 2025)도 있다.[^pubs] 대표 논문 7.

### 6. 로봇 구동기와 동력 전달

사람과 맞닿아 일하는 로봇에 맞는 구동기와 변속 장치를 설계한다. Robotics Actuator 페이지는 공기 스프링과 전자 밸브로 강성을 빠르게 바꾸는 안전한 정유압 구동기(액체에 압력을 걸어 힘을 전하는 구동기)와, 판 스프링의 유효 길이를 바꿔 강성을 빠르고 에너지 효율 좋게 조절하는 사람 보조 장치용 동력 전달 설계를 소개한다.[^actuator] 대표 논문 8은 압축 스프링을 쓴 기구로 감속비를 능동적으로 바꾸는 로봇용 변속기다.[^p8] 논문 목록에는 안전한 물리적 인간–로봇 상호작용을 위한 강성 전환형 정유압 전동 장치(IEEE THMS 2023), 빠른 강성 조절과 효율 좋은 동력 전달을 갖춘 전환형 순응 구동기(Mechatronics 2023)도 있다.[^pubs] 대표 논문 8.

## 대표 논문

김정 교수가 마지막 저자인 2021–2026년 학술지 논문 가운데 초록을 확인할 수 있는 여덟 편을 여섯 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다. 연도는 출판사 서지의 출판 연도다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2022 | [A biomimetic elastomeric robot skin using electrical impedance and acoustic tomography for tactile sensing](https://doi.org/10.1126/scirobotics.abm7187) · Science Robotics | 사람 피부처럼 부드럽고 회복력 있는 전신 로봇 피부를 만들었다. 질긴 하이드로겔과 실리콘 엘라스토머를 겹친 피부 닮은 다층 구조로 보호에 충분한 부드러움과 회복력을 얻었고, 심하게 베인 뒤에도 접착제로 쉽게 고칠 수 있다. 센서 안의 전극은 힘을 받아 이온성 하이드로겔 층이 변형될 때 생기는 국소 전도도 변화를 재고, 마이크는 접촉으로 생긴 진동을 재서 움직이는 촉각 자극의 위치와 종류를 알아낸다. 측정값은 단층 영상화와 심층 신경망으로 여러 종류의 촉각 정보로 바뀐다. 센서를 단 미용 의수로 변형되거나 모양이 복잡한 로봇 피부에도 쓸 수 있음을 보였다.[^p1] | 1저자 K. Park(Kyungseo Park), 마지막 저자 김정 (6명) |
| 2 | 2025 | [A Body-Scale Robotic Skin Using Distributed Multimodal Sensing Modules: Design, Evaluation, and Application](https://doi.org/10.1109/tro.2024.3502204) · IEEE Transactions on Robotics | 다중 모드 감지 모듈과 다층 직물로 몸 전체 크기의 로봇 피부를 만들었다. 초해상도 방식과 단층 변환 방식을 함께 써서 넓은 면적을 적은 감지 소자로 덮고, 사람이 느끼는 넓은 범위의 자극을 두 방식이 서로 보완해 감지한다. 측정값을 접촉의 시공간 특성으로 바꾸고, 학습한 합성곱 신경망이 접촉의 종류를 분류하며, 계산량을 줄여 장치 안에서 계산하도록 했다. 상용 로봇 팔에 붙여 사람의 접촉을 해석하는 촉각 소통을 보였다.[^p2] | 1저자 M. J. Yang(Min Jin Yang), 마지막 저자 김정 (5명) |
| 3 | 2024 | [In-Hand Object Classification and Pose Estimation With Sim-to-Real Tactile Transfer for Robotic Manipulation](https://doi.org/10.1109/lra.2023.3334971) · IEEE Robotics and Automation Letters | 로봇 손에 쥔 물체를 촉각만으로 알아보고 그 자세를 추정했다. 한 쌍의 비전 기반 촉각 센서로 잰 촉각 입력을 점 구름으로 나타내 물체 분류와 자세 추정에 함께 쓴다. 분류에는 PointNet을 촉각 자료에 맞게 고친 PoinTacNet을 만들고, 시뮬레이션 촉각 입력으로 먼저 학습한 뒤 실제 촉각 자료로 다듬어 학습 자료를 효율적으로 쓴다. 사람의 행동에서 착안해 다시 쥐면서 분류 확률을 쌓는 전략으로 McMaster-Carr CAD 모델의 물체 10개에서 분류 정확도 83.89%를 얻었고, 점 구름 정합으로 추정한 자세의 평균 오차(RMSE)는 각도 5.03°, 위치 2.41 mm였다.[^p3] | 1저자 S. Yang(Sanghoon Yang), 마지막 저자 김정 (6명) |
| 4 | 2023 | [Development of a High-SNR Stochastic sEMG Processor in a Multiple Muscle Elbow Joint](https://doi.org/10.1109/tnsre.2023.3281410) · IEEE Transactions on Neural Systems and Rehabilitation Engineering | 표면 근전도는 신호에 무작위성이 있어 신호 대 잡음비가 낮고, 이를 높이는 시간 평균 필터는 지연을 만들어 실시간 로봇 제어를 어렵게 한다. 이전 연구의 백색화 방법을 넓힌 재조정 방법을 쓰는 확률적 근전도 처리기를 만들어 지연 없이 신호 대 잡음비를 높였다. 16채널 전극의 앙상블 평균을 쓰고, 그 가운데 8채널로 깊은 근육의 활성을 재고 분리한다. 팔꿈치 관절의 굽힘 토크 추정에서 RMS 오차 6.17%로 이전 방법보다 나았고, 재활 로봇 공학에서 로봇 장치의 빠르고 정확한 제어 입력을 만드는 데 쓸 수 있다고 적는다.[^p4] | 1저자 H. Chang(Handdeut Chang), 마지막 저자 김정 (5명) |
| 5 | 2025 | [Development of a Sensor Suit for Gait Environment Detection Using Noncontact Sensors and Integrated Model](https://doi.org/10.1109/tmech.2025.3548686) · IEEE/ASME Transactions on Mechatronics | 피부에 직접 닿지 않아도 신호를 얻는 바지형 착용 센서 수트로 걷는 환경을 분류했다. 정전용량 신축 센서와 공압 근음도(pMMG) 센서를 함께 쓴다. 참가자 8명이 평지, 경사로 오르내리기, 계단 오르내리기의 다섯 조건에서 걸은 자료를 LSTM 모델로 분류해, 한 사람의 자료로 학습하고 시험한 경우 정확도 96.1%(표면 근전도 방식 94.0%), 여러 사람으로 학습하고 처음 보는 사람으로 시험한 경우 91.0%(표면 근전도 방식 76.4%)를 얻었다. 착용형 로봇과 보행 보조 시스템에 쓰일 가능성을 든다.[^p5] | 1저자 J. Choi(Junhwan Choi), 마지막 저자 김정 (4명) |
| 6 | 2022 | [sEMG-Triggered Fast Assistance Strategy for a Pneumatic Back Support Exoskeleton](https://doi.org/10.1109/tnsre.2022.3196361) · IEEE Transactions on Neural Systems and Rehabilitation Engineering | 허리 보조 외골격이 관절 움직임을 보고 보조를 시작하면 늦어지므로, 표면 근전도로 보조를 시작하는 전략을 제안하고 건강한 참가자 9명의 들어 올리기 실험으로 평가했다. 외부 하중이 0 kg에서 22.5 kg으로 늘수록 근전도 방식이 기존 방식보다 보조를 앞당긴 시간은 쪼그려 들기에서 114 ms에서 202 ms, 허리 굽혀 들기에서 163 ms에서 269 ms로 커졌다. 보조가 늦을수록 근육 활동이 늘었고, 반복 들기 실험에서 근전도 방식은 허리 굽혀 들기의 L1 근육 피로를 기존 방식보다 70.4% 줄였다.[^p6] | 1저자 U. Heo(Ung Heo), 마지막 저자 김정 (4명) |
| 7 | 2025 | [Field-programmable robotic folding sheet](https://doi.org/10.1038/s41467-025-61838-3) · Nature Communications | 고정된 경첩 구조 대신, 펼쳐 놓은 뒤에도 현장에서 원하는 접힘 모양을 끝없이 다양하게 프로그래밍할 수 있는 로봇 시트를 만들었다. 열에 반응하는 고분자 필름 안에 서로 이어진 금속 저항들을 넣어 히터와 온도 감지 소자로 함께 쓰고, 전력 분포를 전자적으로 바꿔 접힐 곳을 고른다. 전자 배치, 계산 알고리즘, 닫힌 고리 제어로 사용자의 의도를 현장에서 반영해 빠르고 안정적으로 접기를 프로그래밍하며, 물건 잡기와 이동에 응용했다.[^p7] | 1저자 H. Park(Hyunkyu Park), 마지막 저자 김정 (8명) |
| 8 | 2025 | [Variable Transmission With Actively Controllable Reduction Ratio](https://doi.org/10.1109/tmech.2024.3517540) · IEEE/ASME Transactions on Mechatronics | 여러 출력 하중에서 모터 효율을 높게 유지하도록 감속비를 원하는 때에 능동적으로 바꾸는 로봇용 변속기를 모델링하고 설계해 성능을 쟀다. 외부 에너지원 없이 압축 스프링으로 누르는 기구로 동력을 전달해 작게 만들었고, 토로이달 구동 설계의 운동학 해석으로 변속비 범위를 1:1과 4.2:1 사이로 정했다. 웜 기어의 역구동이 안 되는 자기 잠금 특성으로 변속 중 약 3.5 W, 멈춰 있을 때 약 0.2 W만 쓴다. 전체 운전 범위에서 동력 전달 효율 75%를 보였고, 디스크와 롤러 사이 미끄러짐으로 과부하를 막으며 토크 용량은 2.4 N·m다.[^p8] | 1저자 W. Shin(Wonseok Shin), 마지막 저자 김정 (5명) |

## 교수와 전문 분야

김정 교수는 KAIST 기계공학과 교수다.[^meprof][^melist] 연구실 Professor 페이지는 2004년부터 KAIST 기계공학과 교수이고 로보틱스 대학원 과정 겸임교수이며, 2019년부터 BK21+ KAIST value-created Mechanical Engineering 책임자, 2021–2026년 KAIST 기계공학과 학과장이라고 적는다.[^prof] News 페이지는 2021년 7월 교수가 기계항공공학부장과 기계공학과장에 임명됐다고 적는다.[^news]

Professor 페이지에 따르면 교수는 KAIST에서 생산공학 학사(1991)와 정밀공학 및 메카트로닉스 석사(1993)를, MIT에서 기계공학 박사(2004)를 받았다.[^prof] 1993–1999년 Institute for Advanced Engineering(IAE) 연구원으로 있었고, 그 사이 1995–1996년 Carnegie Mellon University 로보틱스 연구소 방문 연구원을 지냈다. 1999–2004년 MIT 연구 조교, 2003–2004년 미국 Yantric Inc. 선임 연구 엔지니어를 거쳐 2004–2008년 KAIST 기계공학과 조교수를 지냈다. 2007년부터 KAIST Institute for Design of Complex System(KIDCS) 부소장이고, 2012–2013년 University of California, Berkeley 방문 학자였다.[^prof]

같은 페이지는 수상으로 IEEE ICRA Best Paper Award in Service Robotics(ICRA 2021), Gaheon Academic Award(SindoRicho Foundation, 2020), IROS Academic Award(제어로봇시스템학회, 2020), IEEE ICRA Best Student Paper Finalist(ICRA 2020), Award for International collaboration(KAIST, 2016), Award for academic excellency(한국정밀공학회, 2012), Best paper Finalist(IEEE International Conference on Biomedical Robotics and Biomechatronics, 2010), Best Project Instructor Award for ED100(KAIST, 2009), Distinguished Achievement award(KAIST 기계공학과, 2008), Outstanding Instructor Award(KAIST 기계공학과, 2005)를 적고, Korean Government Overseas Scholarship Grantee(1999–2001), KAIST 기계공학과 Best Graduate Award(1993)를 적는다.[^prof] 학계 활동으로는 Korean Society of Biomechanics(KSB) 회장, 한국로봇학회 부회장, 제어로봇시스템학회와 한국정밀공학회 이사, IEEE 로봇자동화학회와 ASME 회원을 적고, 한국로봇종합학술대회(KRoC 2021)와 ACM/IEEE HRI 2019의 General Chair, ICCAS 2018의 Program Chair, International Federation of Automatic Control(IFAC) CC 4 Conference Board(Co-ordinating Committee Vice-Chair, 2020–2023)와 TC 4.3 Robotics Vice-Chair를 적는다.[^prof] News 페이지는 2024년 7월 ICROS 2024 학술대회가 교수의 의장(Chairmanship) 아래 열렸다고 적는다.[^news]

누리집 Patents 페이지는 교수가 발명자에 든 국내 등록 특허 30건(2007–2019년)과 국제 등록 특허 2건(2010, 2013년)을 적는다. 근력 보조와 근육 활성 측정, 힘 센서와 지면 반력 측정, 착용형 발목 보조, 조직 물성 진단과 영상 유도 수술, 세포 주입 장치, 햅틱 장치, 컨테이너 크레인 등 주제가 넓다.[^patents]

논문으로 보면 KAIST에서의 전문 분야는 사람과 맞닿는 로봇의 감지와 구동이다. 로봇 피부와 촉각 센싱(대표 논문 1, 2),[^p1][^p2] 촉각 기반 조작(대표 논문 3),[^p3] 근전도 신호 처리(대표 논문 4),[^p4] 착용형 센서와 외골격(대표 논문 5, 6),[^p5][^p6] 소프트 로봇(대표 논문 7),[^p7] 로봇 변속기(대표 논문 8)에 걸친다.[^p8]

## 응용 분야

Wearable Robotics 페이지는 공압 발목-발 보조기를 발 처짐 환자의 발목 등굽힘 보조에, 휴대형 허리 보조 외골격을 육체노동에서 흔한 허리 통증을 줄이는 들어 올리기 보조에 쓰는 연구를 소개한다.[^wearable] 대표 논문 5는 센서 수트를 착용형 로봇과 보행 보조 시스템에, 대표 논문 6은 산업용 외골격에 쓸 수 있다고 적는다.[^p5][^p6] Bio-signal Processing 페이지는 직물형 근전도 센서를 호흡 근육에 붙여 착용자의 건강 상태를 평가할 지표를 얻었다고 적는다.[^biosig] Robotics Tactile Sensing 페이지는 로봇 피부가 사람과 몸으로 맞닿는 로봇의 사회적 상호작용을 넓힐 수 있다고 적고, 대표 논문 1은 센서를 단 미용 의수를 시연했다.[^tactile][^p1]

누리집 바닥의 주요 링크에는 i2A Systems Co.,Ltd가 있고, Alumni 페이지는 박사 졸업생 Pilwon Heo(2015)의 진로를 i2A Systems Co., Ltd. 대표(CEO)로 적는다. 같은 페이지는 박사 졸업생 Gwangmin Gu(2016)의 진로를 K Response Robotics 대표, Handdeut Chang(2019)의 진로를 Incheon National University 조교수 겸 Faraday Dynamics 대표, 석사 졸업생 Wonil Park(2009)의 진로를 TimeBlocks Inc. 창업자 겸 대표로 적는다.[^home][^alumni]

## 구성원

연구실 누리집 Members 메뉴의 Postdoctoral Researcher 페이지 1명, Ph.D. Students 페이지 10명, M.S. Students 페이지 4명, 모두 15명이다.[^postdoc][^phd][^ms] 과정은 각 페이지의 구분이고, 연구 주제는 각 카드의 Research interests 표기다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Woojong Kim | 박사후연구원 | Vision-based Tactile Sensors, Tactile Intelligence & Manipulation, Pneumatic Artificial Muscles | 7 |
| Jirou Feng | 박사과정 | sEMG signal processing, Human-machine interface, Wearable robotics | 5, 6 |
| Seojung Min | 박사과정 | Haptic interfaces, Tactile sensors, Human-machine interaction | 3 |
| Junhwi Cho | 박사과정 | Robotic tactile sensing, Shape estimation, Soft robotics, Sensor actuator integration | 1, 5 |
| Junhwan Choi | 박사과정 | Soft robotics, Wearable robot | 5 |
| Sungbin Park | 박사과정 | Physical human-robot interaction, Hydrostatic actuation, Variable stiffness mechanism | 8 |
| Sangha Jeon | 박사과정 | Robotics tactile sensing, Soft robotics |  |
| Dayoung Yeom | 박사과정 | Soft robotics, Human-robot interaction |  |
| Yoonjin Kim | 박사과정 | Robotics tactile sensing, Robotics manipulation, Human-robot interaction | 2 |
| Minju Kim | 박사과정 | Soft robotics, Wearable robotics, Robotics tactile sensing, Human-robot interaction |  |
| Seunghyun Sung | 박사과정 | Robotics tactile sensing, VTLA model for robotics, Human motion foundation model, Heterogeneous Multi-Robot System |  |
| Hyunki Park | 석사과정 | Vision-based tactile sensors, EIT sensors, Soft robotics, Drones |  |
| Juhee Park | 석사과정 | Physical Human Robot Interaction (pHRI), Robotics Skin / Tactile Sensor |  |
| Gunhee Park | 석사과정 | Wearable robot, Robotics Skin / Tactile Sensor, Robotics actuator |  |
| Myeong Song | 석사과정 | Wearable robotics, Haptic, Human-robot interaction |  |

## 졸업생

누리집 Alumni 페이지의 42명 전부다(Ph.D Graduates 26명, 학위 연도 2010–2025; M.S. Graduates 16명, 학위 연도 2009–2025). 학위와 연도는 각 졸업생의 KAIST 학위 줄이고, 학위 논문은 그 줄 아래 제목, 진로는 Current Position 칸의 표기다. M.S. Graduates 가운데 KAIST 복수 학위 과정(Dual Degree program) 세 명은 KAIST 학위 줄에 연도가 없어 연도를 비웠다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Hyungjoo Kim | Ph.D. Grad. School of Medical Science and Engineering, KAIST (2010) | CTO and Head of Surgical Robot R&D Center, Meerecompany Inc. | Mechanical property characterization of prostate cancer using a minimally invasive motorized indenter in an Ex-vivo indentation Experiment |
| Changmok Choi | Ph.D. Mechanical Engineering, KAIST (2011) | Principal Researcher, Samsung Electronics | Surface electromyography interface study with neuromechanical models |
| Bummo Ahn | Ph.D. Mechanical Engineering, KAIST (2011) | Principal Researcher, KITECH | Inclusion detection with robotic palpation and mechanical property characterization for prostate abnormal tissue detection |
| Hyonyoung Han | Ph.D. Mechanical Engineering, KAIST (2012) | Senior Researcher, Electronics and Telecommunications Research Institute (ETRI) | Mechanical sensing of skeletal muscle contraction and fatigue for physical human-robot interaction |
| Jungsik Kim | Ph.D. Mechanical Engineering, KAIST (2012) | Professional, LG Electronics Inc. | A study of oocyte/embryo manipulation using microfluidics and robotics |
| Yeongjin Kim | Ph.D. Mechanical Engineering, KAIST (2012) | Assistant Professor, Incheon National University | Tissue abnormality localization based on the internal structure analysis and inhomogeneous modeling |
| Suncheol Kwon | Ph.D. Mechanical Engineering, KAIST (2013) | Senior Research Officer, KITECH | Power assistance using surface electromyography and its influence on human movement stability |
| Pilwon Heo | Ph.D. Mechanical Engineering, KAIST (2015) | CEO of i2A Systems Co., Ltd. | Glove-type assistive hand Exoskeleton with open fingerpad |
| Gwangmin Gu | Ph.D. Mechanical Engineering, KAIST (2016) | CEO of K Response Robotics | Measurement and compensation of ankle stiffness using sensor-integrated pneumatic ankle foot orthosis |
| Seongtae Kim | Ph.D. Mechanical Engineering, KAIST (2016) | K Response Robotics | Long-distance MR-compatible actuation method using cable-driven transmission |
| Youngjin Na | Ph.D. Mechanical Engineering, KAIST (2016) | Assistant Professor, Sookmyung Women’s University | Surface electromyography-based force estimation considering muscle fatigue effect |
| Hyosang Lee | Ph.D. Mechanical Engineering, KAIST (2017) | Eindhoven University of Technology | Soft and stretchable tactile sensor using MWCNT-elastomer nanocomposite and anisotropic electrical impedance tomography |
| Hongchul Kim | Ph.D. Mechanical Engineering, KAIST (2017) | Researcher, Agency for Defense Development | Locomotion control for hydraulic lower extremity exoskeleton for stable walking on level and non-level ground |
| Janghan Bae | Ph.D. Mechanical Engineering, KAIST (2019) | Researcher, Korea Institute of Oriental Medicine | Soft computing approach for pulse pattern classification system to objectification of Korean medicine diagnosis |
| Handdeut Chang | Ph.D. Mechanical Engineering, KAIST (2019) | Assistant Professor, Incheon National University, CEO of Faraday Dynamics | Development of self-stabilizing variable stiffness actuation system with variable radius gear and high torque motor |
| Sangjoon J. Kim | Ph.D. Mechanical Engineering, KAIST (2019) | Korea Institute of Science and Technology (KIST) | Untethered pneumatic ankle foot orthosis powered by a portable piston-crank compressor |
| Junghoon Park | Ph.D. Mechanical Engineering, KAIST (2021) | Staff Engineer, Samsung Research R&D Center | Design of a fast response inflatable soft pneumatic bending actuator for wearable robots |
| Yunjoo Kim | Ph.D. Mechanical Engineering, KAIST (2021) | Staff Engineer, Samsung Electronics DS | Development of multimodal sensing system and interactive potential field technique for safe and natural robot teaching |
| Seulki Kyeong | Ph.D. Mechanical Engineering, KAIST (2022) | Assistant Professor, Sejong University | Motion intention recognition from multi-channel surface electromyography through prediction of major muscle activation |
| Kyungseo Park | Ph.D. Mechanical Engineering, KAIST (2022) | Assistant Professor, Daegu Gyeongbuk Institute of Science and Technology (DGIST) | Biomimetic whole-body robotic skin for physical human-robot interaction |
| Wonseok Shin | Ph.D. Mechanical Engineering, KAIST (2023) | Senior Researcher, KITECH | A continuously variable transmission for physically interacting robot |
| Hwayeong Jeong | Ph.D. Mechanical Engineering, KAIST (2023) | Postdoctoral Researcher, UCLouvain | A soft high-radix fluidic demultiplexer for controlling multi-chamber soft robot |
| Hyunkyu Park | Ph.D. Mechanical Engineering, KAIST (2024) | Researcher, Samsung Advanced Institute of Technology (SAIT) | Software-reprogrammable shape-morphing technology based on distributed actuation / sensing |
| Won Dong Kim | Ph.D. Mechanical Engineering, KAIST (2025) | Staff Engineer, Samsung Research R&D Center | Tactile-based learning and inference of fully physical consistent inertial parameters for robotic in-hand object |
| Ung Heo | Ph.D. Mechanical Engineering, KAIST (2025) | Postdoctoral Researcher, KIST | Chemical reaction-based mobile pneumatic source for wearable robots |
| Min Jin Yang | Ph.D. Mechanical Engineering, KAIST (2025) | Assistant Professor, Pusan National University | Body-scale robotic skin and physical human-robot interaction using reconstructive multimodal tactile sensing |
| Yunjoo Lee | M.S. Mechanical Engineering, KAIST (2009) |  | Design of a reflective-type photoplethysmographic sensor with motion artifact reduction |
| Wonil Park | M.S. Robotics Program, KAIST (2009) | Founder/CEO, TimeBlocks Inc. | Real-Time Finger Force Estimation from Surface Electromyography (sEMG) and a Musculoskeletal Model |
| Wonkeun Youn | M.S. Mechanical Engineering, KAIST (2010) | Assistant Professor, Chungnam National University | Estimation of muscle force from mechanomyography (MMG) for physical human-robot interaction |
| Kihan Park | M.S. Mechanical Engineering, KAIST (2011) | Assistant Professor, University of Massachusetts, Dartmouth | Mirror image motion system with surface electromyography for shoulder rehabilitation of hemiplegic patients |
| Dongjune Chang | M.S. Mechanical Engineering, KAIST (2012) | Postdoctoral Researcher , Argonne National Laboratory | Design of a physiological hand tremor canceling mechanism for microsurgical applications |
| Jina Son | M.S. Mechanical Engineering, KAIST (2013) | Researcher, Hyundai Motor Co. | Development of sole instrumentation system for estimating ground reaction force in biomechanics |
| Yongkyun Shin | M.S. Mechanical Engineering, KAIST (2013) | Lead Test Engineer, Geotab | Orientation control of single cells in microfluidic channel |
| Dongju Lee | M.S. Mechanical Engineering, KAIST (2013) | Research Software Engineer, NAVER Corporation | Quantitative assessment of human sensitivity of scanning in lump detection |
| Haedo Cho | M.S. Mechanical Engineering, KAIST (2016) | Postdoctoral Researcher, Harvard University | Design of a flexible tactile sensor for measuring fingertip force and contact recognition |
| Hyein Lee | M.S. Mechanical Engineering, KAIST (2017) | Researcher, Hyundai Motor Co. | Development of an optical type torque sensor and application to impedance control |
| Natasha Jung | M.S. Mechanical Engineering, KAIST (Dual Degree program) | Solution Area Lead, HOMAG Group | A heuristic approach for a puzzle-based system providing material dynamically |
| Lukas Rossel | M.S. Mechanical Engineering, KAIST (Dual Degree program) | IWK Verpackungstechnik Gmbh | Investigation on the reuse of recycled carbon fibers in various non-wovens for HP-RTM and WCM processes |
| Isacco Zappa | M.S. Mechanical Engineering, KAIST (Dual Degree program) | ABB Robotics | Simulated solution for the heterogeneous pallet loading problem and application with a robotic manipulator |
| Chaeree Park | M.S. Mechanical Engineering, KAIST (2023) | Researcher, Bear Robotics | Unsupervised sim-real adaptation of the proprioceptive soft robot |
| Sanghoon Yang | M.S. Mechanical Engineering, KAIST (2023) | Staff engineer, Samsung Electronics Device Solution | Classification and pose estimation of in-hand object through contact information |
| Hyunjo Chung | M.S. Mechanical Engineering, KAIST (2025) |  | Proprioceptive robot hand integrated with vision-based tactile sensors |

## 최근 논문 목록 (2021–2026)

누리집 International Publications 페이지의 2021–2025년 연도 구역 53편(학술지 31, 국제 학회 22)과 Domestic Publications 페이지의 2021–2022년 연도 구역 20편(국내 학회)이다. 두 페이지 모두 2026년 구역에는 아직 논문을 적지 않았다. 연도는 누리집의 연도 구역이며, 몇몇 항목은 줄 안에 다른 출판 연도를 적는다(예: 2024년 구역의 IEEE Transactions on Robotics 두 편은 2025년, 2023년 구역의 몇 편은 2024년). 저자 순서와 제목·학술지·학회 표기는 누리집 그대로이고, 수상 표기는 누리집이 논문 아래에 적은 문구다.[^pubs]

**2025**

- Hyunkyu Park, Yongrok Jeong, Woojong Kim, Jungrak Choi, Junseong Ahn, Jun-Ho Jeong, Inkyu Park and Jung Kim. "Field-programmable robotic folding sheet". *Nature Communications, 2025*.
- Yoonjin Kim, Won Dong Kim and Jung Kim. "Extrinsic Line Contact Sensing from Visuo-Tactile Measurements". *2025 22nd International Conference on Ubiquitous Robots (UR), College Station, TX, USA, 2025*.
- Sangha Jeon, Jung Kim. "Development of CNN-Based Terrain Classifier Using Depth Camera". *2025 22nd International Conference on Ubiquitous Robots (UR), College Station, TX, USA, 2025*.
- Junhwan Choi, Jirou Feng and Jung Kim. "Wearable Soft Sensing Band with Stretchable Sensors for Torque Estimation and Hand Gesture Recognition". *2025 IEEE International Conference on Robotics and Automation (ICRA), Atlanta, GA, USA, 2025*.
- Junhwi Cho, Hyunjo Chung, Kyungseo Park and Jung Kim. "Spatial Sensitivity Equalization of ERT-Based Robotic Skin Through Gauge Factor Distribution Optimization". *2025 IEEE International Conference on Robotics and Automation (ICRA), Atlanta, GA, USA, 2025*.
- Sungbin Park, Won Dong Kim, Sangha Jeon and Jung Kim. "Application of Koopman Direct Encoding-Based Model Predictive Control to Nonlinear Electromechanical Systems". *2025 IEEE International Conference on Robotics and Automation (ICRA), Atlanta, GA, USA, 2025*.
- Jirou Feng, Xingce Bao, Won Dong Kim, Kun Wang and Jung Kim. "Low-Rank Adaptation for Transformers in Dynamic Hand Gesture Recognition Using High-Density Surface Electromyography". *2025 International Conference On Rehabilitation Robotics (ICORR), Chicago, IL, USA, 2025*.
- Jirou Feng, Xingce Bao, Junhwan Choi, Seulki Kyeong and Jung Kim. "Subject-Embedded Vision Transformer with Transfer Learning for Cross-Subject Dynamic Hand Gesture Recognition Using HD-sEMG". *2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Hangzhou, China, 2025*.
- Yoonjin Kim, Won Dong Kim and Jung Kim. "Object Extrinsic Contact Surface Reconstruction through Extrinsic Contact Sensing from Visuo-tactile Measurements". *2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Hangzhou, China, 2025*.
- Junhwan Choi, Jirou Feng, Junhwi Cho and Jung Kim. "Development of a Sensor Suit for Gait Environment Detection Using Noncontact Sensors and Integrated Model". *IEEE/ASME Transactions on Mechatronics, Oct. 2025*.
- Chaeree Park, Hyunkyu Park and Jung Kim. "Unsupervised Sim-to-Real Adaptation of Soft Robot Proprioception Using a Dual Cross-Modal Autoencoder". *Soft Robotics, 2025*.
- Junghoon Park, Youngjin Na and Jung Kim. "Design of an Inflatable Exhaust Valve to Improve Bandwidth of Inflatable Actuators: A Feasibility Study With a Soft Knee Wearable Robot". *International Journal of Control, Automation and Systems, 2025*.
- Wonseok Shin, Sungbin Park, Suncheol Kwon, Bummo Ahn and Jung Kim. "Variable Transmission With Actively Controllable Reduction Ratio". *IEEE/ASME Transactions on Mechatronics, Dec. 2025*.

**2024**

- Hyunkyu Park, Woojong Kim, Sangha Jeon, Youngjin Na and Jung Kim. "Graph-Structured Super-Resolution for Geometry- Generalized Tomographic Tactile Sensing: Application to Humanoid Faces". *IEEE Transactions on Robotics, 2025*.
- Min Jin Yang, Hyunjo Chung, Yoonjin Kim, Kyungseo Park, Jung Kim. "A Body-Scale Robotic Skin Using Distributed Multimodal Sensing Modules: Design, Evaluation, and Application". *IEEE Transactions on Robotics, 2025*.
- Junhyeong Lee, Kyungseo Park, Kundo Park, Yongtae Kim, Jung Kim and Seunghwa Ryu. "Electrode Placement Optimization for Electrical Impedance Tomography Using Active Learning". *Advanced Engineering Materials, 2024*.
- Heesoo Kim, Juhyun Lee, Ung Heo, Dhileep Kumar Jayashankar, Karen-Christian Agno, Yeji Kim, Choong Yeon Kim, Youngjun Oh, Sang-Hyuk Byun, Bohyung Choi, Hwayeong Jeong, Woon-Hong Yeo, Zhuo Li, Seongjun Park, Jianliang Xiao, Jung Kim and Jae-Woong Jeong. "Skin preparation–free, stretchable microneedle adhesive patches for reliable electrophysiological sensing and exoskeleton robot control". *Science Advances . 2024*.

**2023**

- Min Jin Yang, Kyungseo Park, Won Dong Kim and Jung Kim. "Robotic Skin Mimicking Human Skin Layer and Pacinian Corpuscle for Social Interaction". *IEEE/ASME Transactions on Mechatronics, Aug. 2024*.
- Sanghoon Yang, Won Dong Kim, Hyunkyu Park, Seojung Min, Hyonyoung Han and Jung Kim. "In-Hand Object Classification and Pose Estimation With Sim-to-Real Tactile Transfer for Robotic Manipulation". *IEEE Robotics and Automation Letters, Jan. 2024*.
- Yeonha Cho, Woojong Kim, Hyunkyu Park, Jung Kim, Youngjin Na. "Bidirectional Double-Spring Pneumatic Artificial Muscle With Inductive Self-Sensing". *IEEE Robotics and Automation Letters, Dec. 2023*.
- Wonseok Shin, Dongwoo Nam, Bummo Ahn, Sangjoon J Kim, Dong Yeon Lee, Suncheol Kwon and Jung Kim. "Ankle dorsiflexion assistance of patients with foot drop using a powered ankle-foot orthosis to improve the gait asymmetry". *Journal of NeuroEngineering and Rehabilitation (2023)*.
- Sungbin Park, Kyungseo Park, Wonseok Shin and Jung Kim. "Stiffness-Switchable Hydrostatic Transmission Toward Safe Physical Human–Robot Interaction". *IEEE Transactions on Human-Machine Systems, vol. 53, no. 5, pp. 855-864, Oct. 2023*.
- Jirou Feng, Min Jin Yang, Seulki Kyeong, Yusung Kim, SeongHyeon Jo, Hyung-Soon Park and Jung Kim. "Hand Grasp Motion Intention Recognition Based on High-Density Electromyography in Chronic Stroke Patients". *2023 45th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), Sydney, Australia, 2023*.
- Ung Heo, Hyunho Jeong, Jirou Feng, Junhwi Cho, Kyungseo Park, Youngsik Yoon, Dongyeon Lee and Jung Kim. "Development of a Bioimpedance and sEMG Fusion Sensor for Gait Phase Detection: Validation with a Transtibial Amputee". *2023 45th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), Sydney, Australia, 2023*.
- Junhwi Cho, Jung Kim. "Simulation Study of Electrical Resistance Tomography-based Tactile Sensors: Spatial Resolution and Image Performance Evaluation". *2023 20th International Conference on Ubiquitous Robots (UR), Honolulu, HI, USA, 2023*.
- Junhwan Choi, Eunseok Song, Hyunkyu Park, Kyoungchul Kong and Jung Kim. "Soft Sensing Brace for Monitoring Knee Joint Kinetics and Kinematics During Squatting". *2023 20th International Conference on Ubiquitous Robots (UR), Honolulu, HI, USA, 2023*.
- Hyunkyu Park, Jung Kim. "Data-Driven Investigation on Anisotropic Electrical Impedance Tomography for Robotic Shear Tactile Sensing". *2023 20th International Conference on Ubiquitous Robots (UR), Honolulu, HI, USA, 2023*.
- Hwayeong Jeong, Dayoung Yeom and Jung Kim. "Granular-Elastomer Hybrid Jamming Media for Complex Shape Soft Variable Stiffness Actuator". *2023 20th International Conference on Ubiquitous Robots (UR), Honolulu, HI, USA, 2023*.
- Sungbin Park, Seojung Min, Junhwan Choi, Min Jin Yang, Dayoung Yeom, Wonseok Shin, Chaeree Park and Jung Kim. "Preliminary Study of Portable Vibrotactile and Electrical Stimulation System for Knee Proprioception Enhancement". *2023 20th International Conference on Ubiquitous Robots (UR), 2023*.
- Hwayeong Jeong, Jung Kim. "Ossicle Reinforced Porous Structure for Variable Stiffness Soft Actuator Inspired From Echinoderms". *IEEE/ASME Transactions on Mechatronics, Dec. 2023*.
- Won Dong Kim, Sanghoon Yang, Woojong Kim, Jeong-Jung Kim, Chang-Hyun Kim and Jung Kim. "Marker-Embedded Tactile Image Generation via Generative Adversarial Networks". *IEEE Robotics and Automation Letters, Aug. 2023*.
- Handdeut Chang, Seulki Kyeong, Youngjin Na, Yeongjin Kim and Jung Kim. "Development of a High-SNR Stochastic sEMG Processor in a Multiple Muscle Elbow Joint". *IEEE Transactions on Neural Systems and Rehabilitation Engineering, 2023*.
- Min Jin Yang, Junhwi Cho, Hyunjo Chung, Kyungseo Park and Jung Kim. "Touch Classification on Robotic Skin using Multimodal Tactile Sensing Modules". *2023 IEEE International Conference on Robotics and Automation (ICRA), 2023*.
- Seongbin An, Jirou Feng, Eunseok Song, Kyoungchul Kong, Jung Kim and Hyunjin Choi. "High-Accuracy Hand Gesture Recognition on the Wrist Tendon Group Using Pneumatic Mechanomyography (pMMG)". *IEEE Transactions on Industrial Informatics, Feb. 2024*.
- Wonseok Shin, Jung Kim. "Switchable compliant actuator with fast stiffness modulation and energy efficient power transmission". *Mechatronics, Volume 90, 2023*.

**2022**

- Ung Heo, Jirou Feng, Sangjoon J. Kim, and Jung Kim. "sEMG-triggered Fast Assistance Strategy for a Pneumatic Back Support Exoskeleton". *IEEE Transactions on Neural Systems and Rehabilitation Engineering (2022). Aug. 2022*.
- Yunjoo Kim, and Jung Kim. "Estimation of the External Forces on a Robot Hand with Fingertip Tactile Sensors". *International Journal of Control, Automation and Systems 20.8 (2022): 2691-2701. Aug. 2022*.
- SeongHyeon Jo, Jun Ha Jung, Min Jin Yang, Yechan Lee, Sang Jin Jang, Jirou Feng, Si-Hwan Heo, Jung Kim, Joon-Ho Shin, Jaesung Jeong, Hyung-Soon Park. "EEG-EMG hybrid real-time classification of hand grasp and release movements intention in chronic stroke patients". *2022 International Conference on Rehabilitation Robotics (ICORR). IEEE, 2022*.
- Hwayeong Jeong, Jirou Feng, Jung Kim. "2.5 D Laser-Cutting-Based Customized Fabrication of Long-Term Wearable Textile sEMG Sensor: From Design to Intention Recognition". *IEEE Robotics and Automation Letters (2022). (presented at IEEE International Conference on Biomedical Robotics & Biomechatronics (BioRob)) Jul. 2022*.
- Kyungseo Park, and Jung Kim. "Neural-Gas Network-Based Optimal Design Method for ERT-Based Whole-Body Robotic Skin". *IEEE Transactions on Robotics (2022). Jul. 2022*.
- Kyungseo Park, Hyunwoo Yuk, Minjin Yang, Junhwi Cho, Hyosang Lee, and Jung Kim. "A biomimetic elastomeric robot skin using electrical impedance and acoustic tomography for tactile sensing". *Science Robotics 7.67 (2022). Jun. 2022*.
- Wonseok Shin, Sungbin Park, Gunhee Park, Jung Kim. "A Passively Adaptable Toroidal Continuously Variable Transmission Combined with Twisted String Actuator". *2022 International Conference on Robotics and Automation (ICRA). IEEE, 2022*.
- Woojong Kim, Won Dong Kim, Jeong-Jung Kim, Chang-Hyun Kim, Jung Kim. "UVtac: Switchable UV Marker-Based Tactile Sensing Finger for Effective Force Estimation and Object Localization". *IEEE Robotics and Automation Letters 7.3 (2022). Mar. 2022*.
- Seulki Kyeong, Jirou Feng, Jae Kwan Ryu, Jung Jae Park, Kyeong Ha Lee, Jung Kim. "Surface Electromyography Characteristics for Motion Intention Recognition and Implementation Issues in Lower-limb Exoskeletons". *International Journal of Control, Automation and Systems 20.3 (2022). Mar. 2022*.
- 신원석, 김정. "Validation of Pneumatic AFO Powered by a Portable Pneumatic Pump in Foot drop Correction". *한국정밀공학회 춘계학술대회회 KSPE 2022 spring conference, 2022-05-11*.

**2021**

- Sungbin Park, Kyungseo Park, Hwayeong Jeong, Wonseok Shin, Jung Kim. "A Safe and Rapidly Switchable Stiffness Hydrostatic Actuator through Valve-controlled Air Springs". *2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, 2021*.
- Junhwi Cho, Kyungseo Park, Hwayeong Jeong, Jung Kim. "A Soft Somesthetic Robotic Finger Based on Conductive Working Liquid and an Origami Structure". *2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, 2021*.
- Wonseok Shin, Handdeut Chang, Jung Kim. "Human elbow motor learning skills of varying loads: Proof of internal model generation using joint stiffness estimation". *Journal of Biomechanical Science and Engineering 16.3 (2021). Sept. 2021*.
- Hyosang Lee, Kyungseo Park, Jung Kim, Katherine J Kuchenbecker. "Piezoresistive Textile Layer and Distributed Electrode Structure for Soft Whole-body Tactile Skin". *Smart Materials and Structures (2021). Jul. 2021*.
- Wonseok Shin, Gunhee Park, Jooyong Lee, Handdeut Chang, Jung Kim. "Power Transmission Design of Fast and Energy-Efficient Stiffness Modulation for Human Power Assistance". *2021 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2021*.
- Min Jin Yang, Kyungseo Park, Jung Kim. "A Large Area Robotic Skin with Sparsely Embedded Microphones for Human-Robot Tactile Communication". *2021 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2021*.
- Hyunkyu Park, Kyungseo Park, Sangwoo Mo, Jung Kim. "Deep Neural Network Based Electrical Impedance Tomographic Sensing Methodology for Large-Area Robotic Tactile Sensing". *IEEE Transactions on Robotics (2021). Mar. 2021*.
- Kyungseo Park, Hyosang Lee, Katherine J Kuchenbecker, Jung Kim. "Adaptive Optimal Measurement Algorithm for ERT-based Large-area Tactile Sensors". *IEEE/ASME Transactions on Mechatronics (2021). Mar. 2021*.
- Woojong Kim, Hyunkyu Park, and Jung Kim. "Compact Flat Fabric Pneumatic Artificial Muscle (ffPAM) for Soft Wearable Robotic Devices". *IEEE Robotics and Automation Letters 6.2 (2021): 2603-2610. (presented at IEEE International Conference on Robotics and Automation (ICRA)) Feb. 2021 · Winner: Best Paper Award in Service Robotics (ICRA 2021)*.
- 박성빈, 김정. "안전한 물리적 인간-로봇 상호작용을 위한 가변 강성 유압 구동 시스템". *한국정밀공학회 추계학술대회 KSPE 2021 Autumn Conference, 2021-11-24*.
- 최준환, 김정. "외골격 장치를 위한 정전기 클러치 기반 소프트 가변 강성 밴드 개발". *한국정밀공학회 추계학술대회 KSPE 2021 Autumn Conference, 2021-11-24*.
- 허웅, 김정. "허리 보조 외골격 로봇의 sEMG 기반 신속한 보조의 성능 평가". *한국정밀공학회 추계학술대회 KSPE 2021 Autumn Conference, 2021-11-24*.
- 박경서, 김정. "하이드로겔-탄성체 하이브리드 기반의 유연 힘 센서". *한국정밀공학회 추계학술대회 KSPE 2021 Autumn Conference, 2021-11-24*.
- 경슬기, 김정. "Compensation for electrode environment change through prediction of main muscle activation using surface electromyography". *한국정밀공학회 KSPE 2021 Spring Conference, 2021-05-12*.
- 최준환, 김정. "센서 일체형 소프트 수동 구동기 개발". *제 16회 한국로봇종합학술대회 (KRoC 2021), 2021-05-19*.
- 박정훈, 김정. "팽창형 구동기의 빠른 배기를 위한 공압식 배기 밸브 개발". *제 16회 한국로봇종합학술대회 (KRoC 2021), 2021-05-19*.
- 허웅, 김정. "보행 보조를 위한 착용형 제어 모멘트 자이로스코프 시뮬레이션". *제 16회 한국로봇종합학술대회 (KRoC 2021), 2021-05-19*.
- 경슬기, Feng Jirou, 김정. "Joint angle estimation using surface electromyography during walking and running". *제 16회 한국로봇종합학술대회 (KRoC 2021), 2021-05-19*.
- 박성빈, 김정. "정유압 시스템을 위한 공기의 압축성을 이용한 컴플라이언트 요소 개발". *제 16회 한국로봇종합학술대회 (KRoC 2021), 2021-05-19*.
- 신원석, 김정. "고속 고효율 강성 변조용 동력전달 장치 설계". *제 16회 한국로봇종합학술대회 (KRoC 2021), 2021-05-19*.
- 양민진, 김정. "분산 배치된 마이크를 활용한 촉각 센서 개발". *제 16회 한국로봇종합학술대회 (KRoC 2021), 2021-05-19*.
- 조준휘, 허웅, 김정. "무릎 관절 운동 의도 인식을 위한 전기 임피던스 및 근전도 기반 센싱 시스템 개발". *제 16회 한국로봇종합학술대회 (KRoC 2021), 2021-05-19*.
- 김원동, 김연주, 김정. "굽힘센서-관성센서 통합 착용형 디바이스를 이용한 동작의 딥 러닝 기반 분류". *제 16회 한국로봇종합학술대회 (KRoC 2021), 2021-05-19*.
- 김연주, 김원동, 김정. "가중치 부여 동적 시간 워핑을 이용한 동적 동작 인식 알고리즘 개발". *제 16회 한국로봇종합학술대회 (KRoC 2021), 2021-05-19*.
- 박현규, 김정. "딥러닝을 이용한 소프트 센서의 이력현상 보상". *제 16회 한국로봇종합학술대회 (KRoC 2021), 2021-05-19*.
- Feng Jirou, 김정. "Development of Flexible High-Density Surface Electromyography Sensor and Its Application for Muscle Activation Estimation". *제 16회 한국로봇종합학술대회 (KRoC 2021), 2021-05-19*.
- 김우종, 김정. "센서가 내재된 평면형 천 소재 공압 인공 근육의 위치 제어". *제 16회 한국로봇종합학술대회 (KRoC 2021), 2021-05-19*.
- 정화영, 김정. "입자상 물질 재밍 구조가 결합된 부피변화 기반 흡착컵". *제 16회 한국로봇종합학술대회 (KRoC 2021), 2021-05-19*.

## 소식

누리집 News 페이지의 2021년 10월 13일 이후 글 13건(2021년 10월–2025년 10월)이다. 날짜는 글의 게시일이고 문구는 글 제목 그대로다.[^news]

- 2025-10-06 · Our Noncontact Sensor Suit for Gait Environment Detection Published in IEEE TMECH
- 2025-08-08 · Field-Programmable Robotic Folding Sheet Published in Nature Communications
- 2025-07-20 · New Insights into Bio-Signal–Based Human–Robot Interaction Published in Nature Reviews Electrical Engineering
- 2025-06-20 · Two Papers Accepted to IROS 2025
- 2025-05-24 · Three Papers Accepted to ICRA 2025
- 2025-04-07 · Our Unsupervised Sim-to-Real Proprioception Framework Published in Soft Robotics
- 2025-01-02 · Our Actively Controllable Variable Transmission Published in IEEE TMECH
- 2024-11-28 · Our Graph-Based Super-Resolution Tactile Sensing Published in IEEE Transactions on Robotic
- 2024-11-20 · Our Body-Scale Multimodal Robotic Skin Published in IEEE Transactions on Robotics
- 2024-07-05 · ICROS 2024 Successfully Held Under Prof. Kim’s Chairmanship
- 2022-06-08 · Our research on A biomimetic elastomeric robot skin is published in Science Robotics!
- 2022-02-15 · Our Biomimetic Robotic Skin team won the Silver Prize of Samsung Humantech Paper Award!
- 2021-10-13 · [Alumni News] Dr. Hyosang Lee was appointed as Cyber Valley Research Group Leader at the Institute for Smart Sensors at the University of Stuttgart

## 연락과 위치

- 위치: 연구실 기계동(N7-3) 2215호, 교수실 기계동(N7) 5201호[^home][^meprof]
- 전화: 연구실 +82-42-350-5230, 교수 042-350-3231[^home][^meprof]
- 교수 이메일: jungkim@kaist.ac.kr[^meprof]
[^p1]: K. Park 외, J. Kim, Science Robotics 7, eabm7187 (2022). <https://doi.org/10.1126/scirobotics.abm7187> 초록 기준.
[^p2]: M. J. Yang 외, J. Kim, IEEE Transactions on Robotics 41, 96-109 (2025). <https://doi.org/10.1109/tro.2024.3502204> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: S. Yang 외, J. Kim, IEEE Robotics and Automation Letters 9, 659-666 (2024). <https://doi.org/10.1109/lra.2023.3334971> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: H. Chang 외, J. Kim, IEEE Transactions on Neural Systems and Rehabilitation Engineering 31, 2654-2664 (2023). <https://doi.org/10.1109/tnsre.2023.3281410> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. Choi, J. Feng, J. Cho, J. Kim, IEEE/ASME Transactions on Mechatronics 30, 3978-3987 (2025). <https://doi.org/10.1109/tmech.2025.3548686> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: U. Heo, J. Feng, S. J. Kim, J. Kim, IEEE Transactions on Neural Systems and Rehabilitation Engineering 30, 2175-2185 (2022). <https://doi.org/10.1109/tnsre.2022.3196361> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: H. Park 외, J. Kim, Nature Communications 16, 6937 (온라인 2025-08-05). <https://doi.org/10.1038/s41467-025-61838-3> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: W. Shin 외, J. Kim, IEEE/ASME Transactions on Mechatronics 30, 4655-4665 (2025). <https://doi.org/10.1109/tmech.2024.3517540> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 생체기계 연구실 누리집 첫 화면 <https://biorobotics.kaist.ac.kr/> (About Us, Highlights, Important Links, Contact Us, 2026-10-23 열람)
[^contact]: 연구실 누리집 Contact 페이지 <https://biorobotics.kaist.ac.kr/contact/> (2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <https://biorobotics.kaist.ac.kr/members/professor/> (Positions, Research Interests, Education, Work Experience, Honors and Awards, Professional Activities, 2026-10-23 열람)
[^postdoc]: 연구실 누리집 Postdoctoral Researcher 페이지 <https://biorobotics.kaist.ac.kr/members/postdoctoral-researcher/> (2026-10-23 열람)
[^phd]: 연구실 누리집 Ph.D. Students 페이지 <https://biorobotics.kaist.ac.kr/members/phd-students/> (2026-10-23 열람)
[^ms]: 연구실 누리집 M.S. Students 페이지 <https://biorobotics.kaist.ac.kr/members/ms-students/> (2026-10-23 열람)
[^alumni]: 연구실 누리집 Alumni 페이지 <https://biorobotics.kaist.ac.kr/members/alumni/> (Ph.D Graduates, M.S. Graduates, 2026-10-23 열람)
[^biosig]: 연구실 누리집 Research 메뉴 Bio-signal Processing 페이지 <https://biorobotics.kaist.ac.kr/research/bio-signal-processing/> (2026-10-23 열람)
[^actuator]: 연구실 누리집 Research 메뉴 Robotics Actuator 페이지 <https://biorobotics.kaist.ac.kr/research/robotics-actuator/> (2026-10-23 열람)
[^manip]: 연구실 누리집 Research 메뉴 Robotics Manipulation 페이지 <https://biorobotics.kaist.ac.kr/research/robotics-manipulation/> (2026-10-23 열람)
[^tactile]: 연구실 누리집 Research 메뉴 Robotics Tactile Sensing 페이지 <https://biorobotics.kaist.ac.kr/research/robotics-tactile-sensing/> (2026-10-23 열람)
[^soft]: 연구실 누리집 Research 메뉴 Soft Robotics 페이지 <https://biorobotics.kaist.ac.kr/research/soft-robotics/> (2026-10-23 열람)
[^wearable]: 연구실 누리집 Research 메뉴 Wearable Robotics 페이지 <https://biorobotics.kaist.ac.kr/research/wearable-robotics/> (2026-10-23 열람)
[^pubs]: 연구실 누리집 Publications 메뉴: International Publications <https://biorobotics.kaist.ac.kr/international-publications/>, Domestic Publications <https://biorobotics.kaist.ac.kr/domestic-publications/> (목록 범위는 근거 페이지, 2026-10-23 열람)
[^patents]: 연구실 누리집 Patents 페이지 <https://biorobotics.kaist.ac.kr/patents/> (Domestic Patent, International Patent, 2026-10-23 열람)
[^news]: 연구실 누리집 News 페이지 <https://biorobotics.kaist.ac.kr/news/> (2026-10-23 열람)
[^meprof]: KAIST 기계공학과 교수 소개(김정) <https://me.kaist.ac.kr/pop/team.html?uid=15&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 연구실 웹사이트, 이메일, 사무실, 전화, 2026-10-23 열람)
[^melist]: KAIST 기계공학과 교수진 목록 <https://me.kaist.ac.kr/team/team_010100.html> (김정 교수 항목의 직위·연구분야·연구실·최종학위, 2026-10-23 열람)
[^meres]: KAIST 기계공학과 연구분야 「헬스케어/나노/광학」 <https://me.kaist.ac.kr/research/research_010400.html> (생체기계 연구실 항목의 연구주제, 2026-10-23 열람)

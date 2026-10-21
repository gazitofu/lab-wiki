# 인간–기계 상호작용 연구실 (Human-Machine iNteraction Lab, HUMAN Lab)

**KAIST 기계공학과 · 박용화 교수**

- 분야: 진동 해석과 기계 고장 진단·수명 예측(PHM), 인공지능 음향 인식(인공 청각), 인체 진동 기반 헬스 센서(비침습 혈압 등), 3차원 라이다·스테레오 계측
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 고장 진단·수명 예측[^phm][^p6][^vib], 음향·오디오 AI[^acoustic][^p3][^p5], 3차원 복원·인식[^scene], 컴퓨터 비전[^p8], 진동·소음 공학[^vib], 라이다·3차원 거리 센싱[^scene][^p7]
- 홈페이지: <http://human.kaist.ac.kr/>
- 근거와 출처: [HUMAN Lab 근거 페이지](human-lab-sources.md)

> 기계가 사람처럼 보고(3차원 시각) 듣고(음향) 느끼게(진동) 하는 센서와 인공지능을 연구한다. 소리로 기침을 찾아 화면에 표시하는 카메라, 진동과 전류로 모터 고장을 미리 알아내는 기술, 혈압계 신호로 혈관 상태를 읽는 헬스 센서, 작고 정밀한 라이다가 대표 주제다.[^intro][^p5][^phm][^p2][^scene]

## 무엇을 연구하나

연구실은 기계가 사람처럼 입체 시각, 음향, 진동을 감지하고 인공지능으로 주변 환경과 상황을 인식하게 해 사람과 기계의 상호작용을 혁신하는 기술을 연구한다고 소개한다.[^intro] 연구 분야는 진동 해석과 상태 감시, 고장 예측·건전성 관리(PHM), 인공 청각과 음향 인식, 인체 진동과 헬스 센서, 3차원 장면 인식이다.[^home]

첫 번째 갈래는 **진동 해석과 고장 진단**이다. 진동공학은 구조물의 움직임을 다루는 학문으로, 연구실은 복잡하고 서로 맞물린 구조물과 회전 기계의 정밀한 동적 모델을 만들고, 이를 원자력 발전소의 디지털 트윈(실제 설비를 본뜬 가상 모델)과 진동 해석에 써 왔다.[^vib] 영상 신호 처리를 진동공학과 결합한 "모션 증폭" 기술로, 센서를 붙이지 않고 영상만으로 미세한 떨림을 키워 고장 부위를 찾는다.[^vib][^p6] 설비가 언제 고장 날지 미리 예측하는 PHM을 위해 여러 고장 상황을 재현하는 시험 장치를 갖추고 공개 데이터셋도 내놓았다.[^phm]

두 번째 갈래는 **인공 청각과 음향 인식**이다. 소리가 공간을 거쳐 귀와 뇌에 이르는 전 과정을 본떠, 시끄러운 실제 환경에서도 어떤 소리인지, 어디서 났는지 알아내고 원하는 소리만 골라내는 연구를 한다.[^acoustic] 코로나19 시기에 기침 소리를 찾아 위치를 화면에 표시하는 카메라를 만들었고,[^p5] 소리 사건 인식 모델의 주파수 처리 방식을 분석했으며,[^p3] 사람마다 다른 머리·귀의 음향 특성(머리 전달 함수)을 회전하는 스피커 배열로 빠르게 재는 방법을 내놓았다.[^p4] 노인 돌봄 로봇이 기침·낙상 같은 소리를 알아듣게 하는 연구, 공장·발전소의 소리로 고장을 찾는 연구도 한다.[^acoustic]

세 번째 갈래는 **인체 진동과 헬스 센서**다. 심장에서 출발한 혈압파가 혈관을 따라 퍼지는 과정을 하나의 진동 전달 시스템으로 보고, 심혈관계 전체를 본뜬 "가상 환자" 장치를 만들어 혈압계에 전해지는 신호를 실험으로 규명했다.[^health] 혈압계 신호로 위팔 동맥 굵기를 가늠하는 연구,[^p2] 혈압파 계산을 15만 배 빠르게 하는 인공지능 대리 모델을 내놓았고,[^p1] 혈당·피부 탄력 같은 건강 지표를 몸에 상처 내지 않고 재는 센서도 연구한다.[^health]

네 번째 갈래는 **3차원 장면 인식**이다. 자율주행차와 로봇의 눈이 되는 작고 정밀한 라이다(레이저로 거리를 재는 센서)를 목표로 연속파 반도체 레이저와 광다이오드 하나로 부품 수를 줄였고, 오차 3 mm 이내가 요구되는 선박 블록 계측을 스테레오 카메라로 하는 연구도 한다.[^scene] 라이다 내부에서 새는 빛으로 생기는 거리 오차를 자동 보정했고,[^p7] 해상 구조를 위해 열화상 카메라로 멀리 있는 사람을 찾는 인공지능을 만들었다.[^p8]

## 주요 연구 주제

### 1. 인체 진동 기반 헬스 센서

혈압계 신호 분석, 가상 환자 장치, 혈압파 인공지능 계산.[^p1][^p2][^health] 대표 논문 1, 2.

### 2. 인공 청각과 음향 인식

소리 사건 인식, 머리 전달 함수 측정, 기침 인식 카메라.[^p3][^p4][^p5][^acoustic] 대표 논문 3, 4, 5.

### 3. 진동 해석과 PHM

모션 증폭 영상 진동 계측, 모터·베어링 고장 진단과 데이터셋, 원전 구조 진동 해석.[^p6][^phm][^vib] 대표 논문 6.

### 4. 3차원 라이다와 영상 인식

연속파 라이다 보정, 열화상 해상 구조 탐지, 선박 블록 스테레오 계측.[^p7][^p8][^scene] 대표 논문 7, 8.

## 대표 논문

랩 국제 학술지 목록의 2021–2026년 논문 중 교수가 마지막 저자인 것에서 주제별로 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2026 | [Robust prediction of parameterized cardiovascular hemodynamics using deep operator networks with time normalization](https://doi.org/10.1016/j.cmpb.2026.109311) · Computer Methods and Programs in Biomedicine | 수천 번 반복 계산이 필요한 심혈관 혈류 시뮬레이션을 대신하는 인공지능 모델(DeepONet). 심박수·동맥 경직도 등을 직접 입력으로 넣고 시간 축을 정규화해, 학습 범위 밖 조건에서도 오차를 비교적 작게 유지했다. 파형 하나 계산에 약 0.00038초로 기존 계산기보다 약 15만 배 빨랐다.[^p1] | 1저자 Junki Hong, 마지막 저자 박용화 |
| 2 | 2022 | [Correlation analysis of human upper arm parameters to oscillometric signal in automatic blood pressure measurement](https://doi.org/10.1038/s41598-022-24264-9) · Scientific Reports | 자동 혈압계 신호로 위팔 동맥의 굵기·경직도·두께를 알 수 있는지 이론·계산·실험으로 분석했다. 동맥 안쪽 반지름이 신호 크기를 가장 크게 좌우했고, 가상 환자 장치 실험에서 반지름이 10% 달라지면 신호가 6.5% 변했다.[^p2] | 1저자 Bomi Lee(졸업생), 마지막 저자 박용화 |
| 3 | 2025 | [Towards Understanding of Frequency Dependence on Sound Event Detection](https://doi.org/10.1109/taslpro.2025.3603891) · IEEE/ACM TASLP | 소리 사건 인식에서 주파수 대역별로 다르게 처리하는 두 방법(FilterAugment, 주파수 동적 합성곱)이 왜 효과적인지, 모델이 주목하는 시간–주파수 영역을 시각화하고 더 단순한 방법과 비교해 분석했다.[^p3] | 1저자 Hyeonuk Nam(졸업생), 마지막 저자 박용화 |
| 4 | 2025 | [DNN-Based HRIRs Identification With a Continuously Rotating Speaker Array](https://doi.org/10.1109/tim.2025.3644532) · IEEE Transactions on Instrumentation and Measurement | 머리와 귀가 소리를 바꾸는 특성(머리 전달 응답)을 재려면 스피커를 각도마다 옮겨야 해 오래 걸린다. 연속으로 도는 스피커 배열과 심층 신경망으로 이를 빠르게 재는 방법을 만들었고, 초당 45°로 돌려도 정적 측정과 같은 위치 단서를 얻었다.[^p4] | 1저자 Byeong-Yun Ko(졸업생), 마지막 저자 박용화 |
| 5 | 2022 | [Deep learning based cough detection camera using enhanced features](https://doi.org/10.1016/j.eswa.2022.117811) · Expert Systems with Applications | 기침 소리를 찾아내는 합성곱 신경망(이미지 같은 패턴을 찾는 데 쓰는 인공지능)을 마이크 배열로 소리 위치를 보여 주는 음향 카메라에 결합했다. 소리 특징의 변화율까지 쓴 입력으로 시험 F1 점수(정확히 맞힌 비율과 빠뜨리지 않은 비율을 함께 본 점수) 91.9%를 얻었고, 시범 시험에서 기침 위치를 실시간으로 화면에 표시했다.[^p5] | 1저자 Gyeong-Tae Lee(졸업생), 마지막 저자 박용화 |
| 6 | 2024 | [Enhanced Video Motion Magnification Utilizing Envelop Shift for Vision-Based Vibration Measurements](https://doi.org/10.1109/tim.2024.3381257) · IEEE Transactions on Instrumentation and Measurement | 영상 속 미세한 움직임을 키우는 위상 기반 모션 증폭의 흐림과 잡상을 줄이는 방법. 잡음 시뮬레이션에서 오차가 기존 방식의 36.4%로 줄었고, 외팔보(한쪽 끝만 고정한 막대) 실험에서 가속도계 기준 변위 측정이 더 정확했다.[^p6] | 1저자 Jaeduck Lee(졸업생), 마지막 저자 박용화 |
| 7 | 2024 | [Automatic Internal Stray Light Calibration of AMCW Coaxial Scanning LiDAR Using Black and White Image Patterns](https://doi.org/10.1109/tim.2023.3343786) · IEEE Transactions on Instrumentation and Measurement | 연속파 동축 스캐닝 라이다 안에서 새는 빛 때문에 생기는 거리 오차를, 흑백 체커보드(바둑판 무늬 판)를 여러 거리에서 찍어 자동으로 추정·보정했다. 1–4 m에서 수십 cm였던 오차가 3.2 mm로 줄었다.[^p7] | 1저자 Sung-Hyun Lee(졸업생), 마지막 저자 박용화 |
| 8 | 2024 | [Thermal-Infrared Remote-Target Detection System for Maritime Rescue Using 3-D Game-Based Data Augmentation With GAN](https://doi.org/10.1109/tgrs.2024.3454983) · IEEE Transactions on Geoscience and Remote Sensing | 바다에서 사람을 구조하기 위한 열화상 원거리 표적 탐지 인공지능. 실제 열화상 자료가 부족해 게임(ARMA3)으로 만든 합성 자료를 생성적 적대 신경망(GAN)으로 실제처럼 바꿔 학습에 보탰고, 작은 표적의 모양과 위치를 보존하는 방법으로 성능을 높였다.[^p8] | 1저자 Sungjin Cheong(졸업생), 마지막 저자 박용화 |

## 교수와 전문 분야

박용화 교수는 KAIST 기계공학과에서 학사, 석사(1993), 박사(1999)를 받았다. 박사 논문은 주파수 응답 합성을 이용한 최적 구조 동특성 변경으로, 진동·모드 해석과 시스템 식별을 연구했다.[^cv] 한국표준과학연구원 음향진동실(1999–2000)과 미국 콜로라도대 볼더(2000–2003) 박사후연구원을 거쳐, 삼성전자 영상디스플레이사업부(2003–2005)와 삼성종합기술원(2005–2016)에서 3차원 이미지 센서와 MEMS 스캐너 등을 개발했다.[^cv] 랩 소개는 이를 "삼성종합기술원 13년의 독특한 산학 이력"으로 적는다.[^intro] 2016년 8월 KAIST 기계공학과에 부임해 연구실을 세웠고, 로봇공학 학제전공 겸임교수(2021–)다.[^cv]

랩 과제 게시판은 KAIST 부임 뒤 책임 과제 144.52억 원, 책임·공동 과제 총 286.52억 원을 적는다. 한국타이어·삼성전자·LG전자·국방과학연구소 등과의 과제가 많다.[^projects][^cv] 2025년 한국소음진동공학회 추계 학술대회 조직위원장을 맡았고 같은 학술대회에서 국제학술상과 진동제어 최우수논문상을 받았다.[^awards]

논문으로 보면 전문 분야는 세 갈래다.

- **구조 동역학과 진동 계측**: 모드 해석, 디지털 트윈, 모션 증폭.[^p6][^vib]
- **소리·진동 인공지능**: 음향 사건 인식, 기침 탐지, 고장 진단.[^p3][^p5][^phm]
- **광학 3차원 센서와 생체 신호**: 라이다, 혈압계 신호 해석.[^p1][^p2][^p7]

## 응용 분야

대표 논문과 과제로 보면 공장·발전소·선박 설비의 고장 예측, 원자력 발전소 구조 안전, 돌봄 로봇과 감염병 대응, 비침습 혈압·헬스 모니터링, 자율주행차·로봇의 라이다, 해상 구조, 조선소 계측에 닿아 있다.[^p5][^p7][^p8][^phm][^vib][^scene] 졸업생은 삼성전자·LG이노텍·현대자동차·HD한국조선해양·고영테크놀러지, 한국원자력연구원·국방과학연구소·KIST, 한밭대·한국교통대 등으로 진출했고, 한 명은 Bujeon Electronics의 CTO다.[^alumni]

## 구성원

2026년 10월 19일 랩 구성원 페이지(연구원·박사과정·석사과정) 기준이다. 연구 주제와 이메일은 랩 표기다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Rismaya Kumar Mishra | 연구원 | Condition Monitoring, Noise & Vibration and Harshness (NVH), Optimization, Generative AI, Applied Machine Learning | rkmishra@kaist.ac.kr |  |
| 김정민 (Kim, Jeong Min) | 연구원 | 3D Vision Recognition | jmink0304@kaist.ac.kr |  |
| Hussain Altaf | 연구원 | Computer Vision, Industrial Anomaly Detection, Multimodal Learning, Video Analytics, and Machinery Fault Diagnostics | a.hussain@kaist.ac.kr |  |
| 김현준(Kim, Hyeon Jun) | 박사과정 | Health Sensors | khjapple@kaist.ac.kr |  |
| 홍준기 (Hong, Junki) | 박사과정 | Biometric/Medical Sensor | wnsrlwns@kaist.ac.kr | 1, 2 |
| 임윤섭(Lim, Yoon Seop) | 박사과정 | 3D ToF Sensor, 3D vision | bu2050@kaist.ac.kr | 7, 8 |
| 김민태(Kim, Min Tae) | 박사과정 | Intelligent tire, Prognostics and Health Management | mtkim@kaist.ac.kr |  |
| 정원호(Jung, Wonho) | 박사과정 | Prognostics and Health Management, Industrial AI | wonho1456@kaist.ac.kr | 8 |
| 윤창규(Yoon, Changgyu) | 박사과정 | Motion magnification | changgyu0401@kaist.ac.kr |  |
| 이원준(Yi, Wonjun) | 박사과정 | Anomaly detection, Fault diagnosis | lasscap@kaist.ac.kr |  |
| Adelle Persad | 박사과정 | Biometrics | adelle.persad@kaist.ac.kr | 1 |
| 안석준(An, Seok Jun) | 박사과정 | 3D ToF Sensor | asj0379@kaist.ac.kr |  |
| 김진(Kim, Jin) | 박사과정 | 3D vision | jinkim@kaist.ac.kr |  |
| 김준호(Kim, Jun Ho) | 박사과정 | Prognostic and Health Management(PHM) | junjun1201@kaist.ac.kr |  |
| 김명희 (Kim, Myounghee) | 박사과정 | Vibration, & Control, Flutter, AI | kimmyoungh@kaist.ac.kr |  |
| 안재영 (An, Jaeyoung) | 박사과정 | Motion Magnification, Depth Estimation | jyan0511@kaist.ac.kr |  |
| 송현우 (Song, Hyunwoo) | 박사과정 | Health Sensor (연구실 대표) | songever5696@kaist.ac.kr | 1 |
| Risky Ayu Febriani | 박사과정 | Vibration, Fault Diagnosis | riskyayuf@kaist.ac.kr |  |
| 최인한(Choi, Inhan) | 석사과정 | Acoustic recognition | ds5amk@kaist.ac.kr |  |
| 송유리(Song, Yuri) | 석사과정 | Biosignal Processing, Health Sensor | yurisong@kaist.ac.kr |  |
| 최승덕(Choi, Seungdeok) | 석사과정 | Acoustic Recognition, Audio Language Model | haroldchoi6@kaist.ac.kr |  |
| 최성민(Choi, Seongmin) | 석사과정 | Acoustic Recognition | seongmin.choi@kaist.ac.kr |  |
| 진민제(Jin, Minje) | 석사과정 | Prognostics and Health Management(PHM) | jin2530@kaist.ac.kr |  |
| 한동규(Han, Dongkyu) | 석사과정 | Prognostics and Health Management(PHM) | dk_han@kaist.ac.kr |  |
| 정수연(Jeong, Sooyeon) | 석사과정 | Prognostics and Health Management(PHM) | jsuyeon621@kaist.ac.kr |  |
| 신해인(Shin, Haein) | 석사과정 | Health Sensor | danteirum@kaist.ac.kr |  |
| 신재민 (Shin, Jaemin) | 석사과정 | Health Sensor | jmshin0224@kaist.ac.kr |  |
| 박종혁 (Park, Jonghyeok) | 석사과정 | Motion Magnification, 3D Vision | jonghyeokpark@kaist.ac.kr |  |
| 박세준 (Park, Sejun) | 석사과정 | Lidar, Vision | sejun01@kaist.ac.kr |  |
| 김병용(Kim, Byeongyong) | 석사과정 | LiDAR | byeongyong.kim@kaist.ac.kr |  |
| 반정규(Ban, Jeonggyu) | 석사과정 | Vision, VLA, AI | eddyban@kaist.ac.kr |  |
| 조준오(Cho,Junoh) | 석사과정 | Structural Dynamics, Modal Analysis, Digital Twin | Junoh.cho@kaist.ac.kr |  |

## 졸업생 진로

랩 졸업생 페이지의 목록(30명)이다. 학위는 학력란의 KAIST 학위, 진로는 "Current" 표기를 옮겼다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Yugang Chen | 2018-2019 Post Doc. Mechanical Engineering, KAIST |  |
| 이길용(Lee, Gil Yong) | 2023 PhD Mechanical Engineering, KAIST | Korea Atomic Energy Research Institute |
| 이성현(Lee, Sung Hyun) | 2023 PhD Mechanical Engineering, KAIST | Hanbat National University |
| 이경태(Lee, Gyeong Tae) | 2024 PhD Mechanical Engineering, KAIST | CTO, Bujeon Electronics |
| 김성후(Kim, Seong Hu) | 2024 PhD Mechanical Engineering, KAIST | Samsung Electronics |
| 정재학(Jeong, Jae-Hak) | 2024 PhD Mechanical Engineering, KAIST | Korea National University of Transportation |
| 이재덕(Lee, Jae Duck) | 2024 PhD Mechanical Engineering, KAIST | Agency for Defense Development (ADD) |
| 고병윤(Ko, Byeong Yun) | 2025 PhD Mechanical Engineering, KAIST | Samsung Electronics |
| 남현욱(Nam, Hyeonuk) | 2025 PhD Mechanical Engineering, KAIST | Samsung Electronics |
| 박강재(Park, Kang Jae) | 2025 PhD Mechanical Engineering, KAIST |  |
| 이보미 (Lee, Bomi) | 2026 PhD Mechanical Engineering, KAIST |  |
| 임대근(Lim, Dae geun) | 2025 PhD Mechanical Engineering, KAIST | RIMS (Research Institute of Medium and Small Shipbuilding) |
| 신준오(Shin, Joon Oh) | 2018 MS Mechanical Engineering, KAIST | Samsung Electronics |
| 박대희(Park, Dae Hee) | 2020 MS Mechanical Engineering, KAIST | KAIST |
| 유혜원(Yoo, Hye Won) | 2020 MS Mechanical Engineering, KAIST | Samsung Electronics |
| 이준혁(Lee, JunHyeok) | 2020 MS Mechanical Engineering, KAIST | Ph.D Student at Johns Hopkins University |
| 장인규(Jang, In Gyu) | 2020 MS Mechanical Engineering, KAIST | LG Innotek → Ph.D Student at Duke University |
| 권욱현 (Kwon, Wook Hyeon) | 2022 MS Mechanical Engineering, KAIST | Samsung Electronics |
| 최상민 (Choi, Sang Min) | 2022 MS Mechanical Engineering, KAIST | Samsung Electronics |
| 배재웅(Bae, Jae Woong) | 2022 MS Mechanical Engineering, KAIST | Hyundai Motors |
| 우수민 (Woo, Soomin) | 2022 MS Mechanical Engineering, KAIST |  |
| 정성진(Cheong, Sung Jin) | 2023 MS Mechanical Engineering, KAIST | LG Innotek → Ph.D Student at University of Wisconsin-Madison |
| 윤성현 (Yun, Sung Hyun) | 2024 MS Mechanical Engineering, KAIST | Samsung Electronics |
| 김도현(Kim, Dohyeon) | 2024 MS Mechanical Engineering, KAIST | Recon Labs |
| 민덕기(Min, Deokki) | 2024 MS Mechanical Engineering, KAIST | KIST |
| 민창희(Min, Changhee) | 2024 MS Mechanical Engineering, KAIST | Koh Young Technology |
| 장강민 (Jang, Kangmin) | 2026 MS Mechanical Engineering, KAIST | HD Korea Shipbuilding & Offshore Engineering |
| 조만희 (Cho, Manhee) | 2026 MS Mechanical Engineering, KAIST | Hyundai Motors |
| 신유정(Shin, Yujeong) | 2026 MS Mechanical Engineering, KAIST |  |
| 임준홍(Im, Junhong) | 2026 MS Mechanical Engineering, KAIST | Samsung Electronics |

## 최근 논문 목록 (2021–2026)

랩 국제 학술지 목록(최근 5년)에 실린 논문 40편이다. 서지는 랩 표기를 옮겼다.[^papers] 대표 논문은 위 표에서 쉬운 설명을 붙였다.

**2026**

- Junki Hong, Bomi Lee, Adelle Ria Persad, Hyunwoo Song, Changhee Min, Jae-Hak Jeong, Alireza Doostan, Yong-Hwa Park. "Robust prediction of parameterized cardiovascular hemodynamics using deep operator networks with time normalization". *Computer Methods and Programs in Biomedicine, 2026*.
- Jeongmin Kim, Jin Kim, Manhee Cho, Yeonghwan Kim, Bong-gook Kang, Yong-Hwa Park. "Three-dimensional measurement of ship blocks using a multi-vision system with weighted generic calibration". *Ocean Engineering, 2026*.
- K.C. Park, J.A. Gonzaelez, S.J. Shin, S.H. Kang, M.H. Hwang, J.G. Kim, M.F. Baqir, J.H. Hang, R.W. Hagos, S.C. Lee, Y.H. Park, H.J. Kim, K.K. Maute, C.A. Felippa. "Solving FEM models without assembly: Its promise and challenge". *Computer Methods in Applied Mechanics and Engineering, 2026*.
- Wonjun Yi, Wonho Jung, Heyonu Nam, Kangmin Jang, Yong-Hwa Park. "Multi-output classification using a cross-talk architecture for compound fault diagnosis of motors in partially labeled condition". *Mechanical Systems and Signal Processing, 2026*.

**2025**

- Wonho Jung, Junho Kim, Kangmin Jang, Sung-Hyun Yun, Daeguen Lim, Minje Jin, Yong-Hwa Park. "Vibration, current, torque, RPM dataset for multiple fault conditions in industrial-scale electric motors under randomized speed and load variations". *Data in Brief, 2025*.
- Hyeonuk Nam, Seong-Hu Kim, Deokki Min, Byeong-Yun Ko, Yong-Hwa Park. "Towards Understanding of Frequency Dependence on Sound Event Detection". *IEEE Transactions on Audio, Speech and Language Processing, 2025*.
- Byeong-Yun Ko, Deokki Min, Hyeonuk Nam, Yong-Hwa Park. "DNN-Based HRIRs Identification With a Continuously Rotating Speaker Array". *IEEE Transactions on Instrumentation and Measurement, 2025*.
- Junki Hong, Bomi Lee, Adelle Ria Persad, Hyunwoo Song, Changhee Min, Jae-Hak Jeong, Yong-Hwa Park. "Correlation analysis of arterial pressure waveform morphology similarity and relative pulse transit time using cardiovascular hardware simulator and hemodynamic model". *Computers in Biology and Medicine, 2025*.
- Dae-Guen Lim, Gil-Yong Lee, Yong-Hwa Park. "Application of DeepONet to predict transient drop motion of the control rod in real-time". *Nuclear Engineering and Technology, 2025*.
- Hyeonuk Nam, Yong-Hwa Park. "Coherence-based phonemic analysis on the effect on reverberation to practical automatic speech recognition". *Applied Acoustics, 2025*.

**2024**

- Sungjin Cheong, Wonho Jung ,Yoon Seop Lim, Yong-Hwa Park. "Thermal-Infrared Remote-Target Detection System for Maritime Rescue Using 3-D Game-Based Data Augmentation With GAN". *IEEE Transactions on Geoscience and Remote Sensing, 2024*.
- K.C. Park, C.A. Felippa, S.H. Kang, J.A. González, S.J. Shin, Y.H. Park, J.G. Kim. "A partitioned flexibility (PartFlex) method for structural analysis". *Computer Methods in Applied Mechanics and Engineering, 2024*.
- Dae-Guen Lim, Gil-Yong Lee, Nam-Gyu Park, Yong-Hwa Park. "A computational framework for drop time assessment of a control element assembly under fuel assembly deformations with fluid-structure interaction and frictional contact". *Nuclear Engineering and Technology, 2024*.
- Kang-Jae Park, Gil-Yong Lee, Jae-Hak Jeong, Yong-Hwa Park. "Validation of the added mass effect in the narrow gaps of nuclear reactor pressure vessels". *Journal of Sound and Vibration, 2024*.
- Jeongmin Kim, Jaeduck Lee, Yong-Hwa Park. "Highly accurate three-dimensional measurement of large structures using multiple stereo vision with improved two-step calibration algorithm". *Measurement, 2024*.
- Gil-Yong Lee, Kang-Jae Park, Dae-Guen Lim, Yong-Hwa Park. "Model order reduction based on low-rank approximation for parameterized eigenvalue problems in structural dynamics". *Journal of Sound and Vibration, 2024*.
- Wonho Jung, Sung-Hyun Yun, Yong-Hwa Park. "Vibration, and temperature run-to-failure dataset of ball bearing for prognostics". *Data in Brief, 2024*.
- Kun Woo Ko, Taehoon Lee, Jae-Hak Jeong, Yeonteak Lee, Ikjin Kim, Jungmok Seo, Yong-Hwa Park, Jin-Oh Kim, Steve Park. "Hydrogel Ink for 3D Printing with High and Widely Tunable Mechanical Properties via the Salting-Out Effect". *Advanced Materials Technologies, 2024*.
- Jae-Hak Jeong, Bomi Lee, Junki Hong, Changhee Min, Adelle Ria Persad, Tae-Heon Yang, Yong-Hwa Park. "Cardiovascular hardware simulator and artificial aorta- generated central blood pressure waveform database according to various vascular age for cardiovascular health monitoring applications". *Computers in Biology and Medicine, 2024*.
- Jaeduck Lee, Kang-Jae Park, Yong-Hwa Park. "Enhanced video motion magnification utilizing envelop shift for vision-based vibration measurements". *IEEE Transactions on Instrumentation and Measurement, 2024*.
- Dae-Guen Lim, Gil-Yong Lee & Yong-Hwa Park. "Proper generalized decomposition-based iterative enrichment process combined with shooting method for steady-state forced response analysis of nonlinear dynamical systems". *Computational Mechanics, 2024*.
- Seong-Hu Kim, Hyeonuk Nam, Sang-Min Choi, Yong-Hwa Park. "Real-Time Sound Recognition System for Human Care Robot Considering Custom Sound Events". *IEEE Access, 2024*.
- Hyewon Yoo, Jae Woong Bae, Jae-Hak Jeong, Yong-Hwa Park. "Feasibility study on person identification utilizing frequency response functions of human fingers". *Journal of Sound and Vibration, 2024*.
- Dong-Geun Lee, Kwan Chul Lee, J.-W. Juhn, Jae-seok Lee, Jayhyun Kim, SooHwan Park, Michael Lehnen, Yong-Hwa Park, Jae-Hak Jeong, aebeom Yim. "Development of the upgraded single crystal dispersion interferometer (SCDI-U) and its first measurements of the line integrated electron densities in KSTAR during shattered pellet injections". *Nuclear Fusion, 2024*.
- Sung-Hyun Lee, Yoon-Seop Lim, Wook-Hyeon Kown, Yong-Hwa Park. "Automatic Internal Stray Light Calibration of AMCW Coaxial Scanning LiDAR Using Black and White Image Patterns". *IEEE Transactions on Instrumentation and Measurement, 2024*.

**2023**

- K. C. Park, J. A. González, Y. H. Park, S. J. Shin, J. G. Kim, K. K. Maute, C. Farhat, C. A. Felippa. "Displacement-based partitioned equations of motion for structures: Formulation and proof-of-concept applications". *International Journal for Numerical Methods in Engineering, 2023*.
- Byeong-Yun Ko, Gyeong-Tae Lee, Hyeonuk Nam, Yong-Hwa Park. "PRTFNet: HRTF Individualization for Accurate Spectral Cues Using a Compact PRTF". *IEEE Access, 2023*.
- Sung-Hyun Lee, Yoon-Seop Lim, Wook-Hyeon Kwon, Yong-Hwa Park. "Multipath Interference Suppression of Amplitude-Modulated Continuous Wave Coaxial-Scanning LiDAR Using Model-Based Synthetic Data Learning". *IEEE Sensors Journal, 2023*.
- Seong-Hu Kim, Hyeonuk Nam, Yong-Hwa Park. "Analysis-Based Optimization of Temporal Dynamic Convolutional Neural Network for Text-Independent Speaker Verification". *IEEE Access, 2023*.
- Wonho Jung, Seong-Hu Kim, Sung-Hyun Yun, Jaewoong Bae, Yong-Hwa Park. "Vibration, acoustic, temperature, and motor current dataset of rotating machine under varying operating conditions for fault diagnosis". *Data in Brief, 2023*.
- Wonho Jung, Sung-Hyun Yun, Yoon-Seop Lim, Sungjin Cheong, Yong-Hwa Park. "Vibration and current dataset of three-phase permanent magnet synchronous motors with stator faults". *Data in Brief, 2023*.
- Peter Risby Andersen, Gyeong-Tae Lee, Daniel Gert Nielsen, Junghwan Kook, Vicente Cutanda Henriquez, Niels Aage, Yong-Hwa Park. "Experimental characterization of a shape optimized acoustic lens: Application to compact speakerphone design". *Journal of the Acoustical Society of America, 2023*.
- Gil-Yong Lee, Yong-Hwa Park. "A proper generalized decomposition-based harmonic balance method with arc-length continuation for nonlinear frequency response analysis". *Computers & Structures, 2023*.

**2022**

- Sung-Hyun Lee, Wook-Hyeon Kown, Yoon-Seop Lim, Yong-Hwa Park. "Highly precise AMCW time-of-flight scanning sensor based on parallel-phase demodulation". *Measurement, 2022*.
- Gyeong-Tae Lee, Hyeonuk Nam, Seong-Hu Kim, Sang-Min Choi, Youngkey Kim, Yong-Hwa Park. "Deep learning based cough detection camera using enhanced features". *Expert Systems with Applications, 2022*.
- Gil-Yong Lee, K.C. Park, Yong-Hwa Park. "Reduced-order modeling via proper generalized decomposition for uncertainty quantification of frequency response functions". *Computer Methods in Applied Mechanics and Engineering, 2022*.
- Bomi Lee, Jae-Hak Jeong, Junki Hong & Yong-Hwa Park. "Correlation analysis of human upper arm parameters to oscillometric signal in automatic blood pressure measurement". *Scientific Reports, 2022*.
- Jaewoong Bae, Wonho Jung and Yong-Hwa Park. "Normal data based rotating machine anomaly detection using CNN with self-labelling". *Smart Structures and Systems, 2022*.

**2021**

- Daehee Park, Yong-Hwa Park. "Identifying Reflected Images From Object Detector in Indoor Environment Utilizing Depth Information". *IEEE Robotics and Automation Letters, 2021*.
- Yugang Chen, Kang-Jae Park, Bomi Lee & Yong-Hwa Park. "A method for identification of analyte concentration in aqueous solution by using a mistuned fluid-structure coupled vibration". *Journal of Mechanical Science and Technology, 2021*.

## 특허 (2021년 이후 등록·출원)

랩 특허 목록에서 2021년 이후 날짜가 적힌 항목이다.[^patents]

- 게임데이터 학습 딥러닝 기반 소형 객체 탐지 방법 및 장치 (발명자 박용화, 정원호, 정성진; 번호 Pat.No. 10-2878352-0000 (2025.10.24), 대한민국)
- Deep learning-based cough recognition method and device (발명자 박용화, 이경태, 남현욱, 김성후, 김영기, 김인권, 이광현, 이재선, 박성효; 번호 Pat.No. 12156727 (2024.12.03), 미국)
- 전차 동력 장치의 고장 진단 시스템, 방법 및 프로그램 (발명자 박용화; 번호 Pat.No. 10-2723564-0000 (2024.10.24), 대한민국)
- 시계열 데이터 적응형 컨볼루션 기반 딥러닝 모델을 이용한 화자 인식 방법 (발명자 박용화, 김성후; 번호 Pat.No. 10-2709590-0000 (2024.09.20), 대한민국)
- ELECTRONIC APPARATUS AND METHOD FOR IDENTIFYING FALSE DETECTION OF OBJECT BY REFLECTION IN INDOOR ENVIRONMENT (발명자 박용화, 박대희, Simeneh Semegne Gulat; 번호 Pat.No. 3772701 (2024.05.01), 유럽)
- 다중채널 음향 및 진동신호 딥러닝 기반 전차 동력장치 고장진단체계 (발명자 박용화, 남현욱, 김성후, 민덕기, 서호준; 번호 Pat.No. 10-2647161-0000 (2024.03.08), 대한민국)
- 전동기 상태 진단 방법 및 장치 (발명자 박용화, 김준호, 정원호, 김재완, 양찬승; 번호 App.No. 10-2025-0147472 (2025.10.14), 대한민국)
- 소음 검출 장치의 마이크 배열을 설계하기 위한 설계 방법 및 소음 검출 장치의 제작 방법 (발명자 박용화, 김진, 고병윤, 변재민, 강병권, 유성근, 임광섭, 오현수; 번호 App.No. 10-2025-0081263 (2025.06.19), 대한민국)
- SIMULATION METHOD AND MULTIPATH INTERFERENCE CORRECTION SYSTEM AND METHOD FOR COAXIAL SCANNING LiDAR (발명자 박용화, 이성현, 임윤섭; 번호 App.No. 18/978,149 (2024.12.12), 미국)
- 구조물의 고장 진단장치 및 그 방법 (발명자 박용화, 박강재, 김현준; 번호 App.No. 10-2024-0077585 (2024.06.14), 대한민국)
- PULSE WAVE REPRODUCTION DEVICE AND METHOD OF OPERATING THE SAME (발명자 박용화, 정재학, 이보미, 홍준기, 민창희, PERSAD ADELLE RIA; 번호 App.No. 18/663,199 (2024.05.14), 미국)
- 고정밀 캘리브레이션 기반의 스테레오 시스템을 이용한 선체 블록 3차원 계측 시스템 (발명자 박용화, 김정민, 김도현, 김진; 번호 App.No. 10-2024-0060289 (2024.05.08), 대한민국)
- 동축 스캐닝 라이다의 시뮬레이션 방법과 다중 경로 간섭 보정 시스템 및 방법 (발명자 박용화, 이성현, 임윤섭; 번호 App.No. 10-2023-0179814 (2023.12.12), 대한민국)
- 동축 스캐닝 라이다의 내부 미광 추정 시스템 및 방법과 이를 이용한 내부 미광 보정 시스템 (발명자 박용화, 이성현, 임윤섭; 번호 App.No. 10-2023-0173307 (2023.12.04), 대한민국)
- DEVICE AND METHOD FOR EXTRACTING CARDIOVASCULAR HEALTH STATUS BY USING OSCILLOMETRIC SIGNAL (발명자 Yong-Hwa Park, Bomi Lee, Junki Hong, Jae-Hak Jeong; 번호 App.No. 18/198,397 (2023.05.17), 미국)
- 오실로메트릭 신호를 이용한 심혈관 건강 상태 추출 장치 및 방법 (발명자 박용화, 이보미, 홍준기, 정재학; 번호 App.No.10-2022-0178074 (2022.12.19) , 대한민국)
- 오실로메트릭 혈압계를 이용한 비침습적 동맥 혈압 추정 방법 및 장치 (발명자 박용화, 홍준기, 정재학, 이보미; 번호 App.No. 10-2022-0174890 (2022.12.14) , 대한민국)
- 주파수 적응형 컨볼루션 기반 음향 이벤트 검출 방법 (발명자 박용화, 남현욱, 김성후; 번호 App.No. 10-2022- 0135707 (2022.10.20) , 대한민국)
- 시계열 데이터 적응형 컨볼루션 기반 딥러닝 모델을 이용한 화자 인식 방법 (발명자 박용화, 김성후; 번호 App.No. 10-2022-0032079 (2022.03.15) , 대한민국)
- 회전체 결함 진단을 위한 전류데이터 이미지화 방법 및 장치 (발명자 박용화, 정원호, 배재웅; 번호 App.No. 10- 2022-0032157 (2022.03.15), 대한민국)
- 게임 데이터 학습 딥러닝 기반 소형 객체 탐지 방법 및 장치 (발명자 박용화, 정원호, 정성진; 번호 App.No.10- 2022-0026734 (2022.03.02), 대한민국)
- 스테레오 방법을 이용한 3 차원 형상정보 계측에 있어서의 이미지 왜곡 보정 방법 및 장치 (발명자 박용화, 김정민; 번호 App.No. 10-2021-0068250 (2021.05.27), Pat.No. 10-2412275-0000 (2022.06.20) , 대한민국)

## 연구 과제

랩 과제 게시판의 최근 과제(2021년 이후 시작)와 랩이 적은 연구비다.[^projects]

- 인공지능 기반 타이어 건전성 모니터링 기술 개발 (기간 01/2026-12/2026; 지원 한국타이어앤테크놀로지㈜; 연구비 1.1 억원)
- AI 기반 지능형 설계-제조 통합 연구단 (기간 01/2026-12/2026; 지원 한국과학기술원; 연구비 0.7 억원)
- 삼성전자 DS부문 전략 산학 과제 4기 (기간 10/2025-09/2026; 지원 삼성전자㈜; 연구비 0.7 억원)
- 컴프레서 소음의 청각심리학적 분석 및 레벨 정량화 신규 체계 개발 (기간 05/2025-09/2026; 지원 LG전자㈜; 연구비 0.9 억원)
- 냉장고 설치 공간 스캐닝 Kit 개발 (기간 05/2025-04/2026; 지원 LG전자㈜; 연구비 1.1 억원)
- 가상환자시스템과 물리기반 AI를 이용한 비침습적 심혈관 건강 상태 모니터링 핵심 기술 개발 (기간 05/2025-04/2026; 지원 한국연구재단; 연구비 2.4 억원)
- 초격차조선산업전문인력양성 (기간 03/2025-02/2026; 지원 한국생산성본부 산업통상자원부; 연구비 4.4 억원)
- 스마트 전문인력양성사업(2025 년도) (기간 03/2025-02/2026; 지원 한국산업기술진흥원 과학기술정보통신부; 연구비 5.2 억원)
- 다변량 시계열 데이터 기반 예측 기법 개발 (기간 05/2025-09/2025; 지원 삼성중공업㈜대덕연구소; 연구비 0.3 억원)
- 진동신호 기반 C-GIS 조작기 진단 알고리즘 개발 (기간 03/2025-11/2025; 지원 에이치디현대일렉트릭 주식회사; 연구비 1.3 억원)
- 머리전달함수 데이터 측정건 (기간 03/2025-05/2025; 지원 한국전자기술연구원; 연구비 0.3 억원)
- 모션증폭 기반 VR형태 실시간 고장 진단기 개발 (기간 01/2025-01/2026; 지원 주식회사 포스코; 연구비 1.3 억원)
- XR 기반 함정 조함 훈련 체계 개발(2025 년도) (기간 01/2025-12/2025; 지원 국방과학연구소 민군협력진흥원; 연구비 1.5 억원)
- 회전체 장비 진동 RMS 예측 (기간 01/2025-03/2025; 지원 삼성중공업㈜대덕연구소; 연구비 0.1 억원)
- 머리전달함수 데이터 측정건 (기간 12/2024-12/2024; 지원 한국전자기술연구원; 연구비 0.3 억원)
- AI알고리즘을 탑재한 예지보전시스템의 개발 (기간 10/2024-02/2025; 지원 주식회사 신성이엔지; 연구비 0.4 억원)
- 에어컨 고장진단을 위한 맞춤형 마이크로폰 어레이 개발 및 이상음 감지 시스템 구축 (기간 05/2024-01/2025; 지원 LG전자; 연구비 1.0 억원)
- 선체 블록 고속 고정밀 계측 기술 현업 적용을 위한 Ray Calibration 자동화 및 최적화 연구 (기간 05/2024-12/2024; 지원 ㈜HD한국조선해양; 연구비 0.5 억원)
- 가상환자시스템과 물리기반 AI를 이용한 비침습적 심혈관 건강 상태 모니터링 핵심 기술 개발 (기간 05/2024-04/2025; 지원 한국연구재단 과학기술정보통신부; 연구비 2.4 억원)
- 딥러닝 기반 청각인지 뇌파 데이터 처리 모델 구현 (기간 04/2024-06/2024; 지원 한국과학기술연구원; 연구비 0.1 억원)

## 수상과 소식

랩 수상 게시판(Awards)의 2021년 이후 항목이다.[^awards]

- 2026.02.04 · KAIST ME NewsLetter, Adelle Ria Persad 박사과정, ETME 2025 학술대회 Best Presentation Award 수상
- 2026.02.04 · KAIST ME NewsLetter, 정원호 박사과정, 현대모비스 전동화 우수논문경진대회 수상
- 2026.01.06 · KAIST ME NewsLetter, 박용화 교수, 2025 추계 소음진동 학술대회 국제학술상, 진동제어 최우수논문상 수상
- 2026.01.06 · KAIST ME NewsLetter, 박용화 교수, 2025 추계 소음진동 학술대회 조직위원장으로 성공적 개최
- 2025.12.14 · 임윤섭, 안석준, 김진 박사과정 공저 Invited Paper 선정, 2025 SPIE Photonics West, San Francisco, California, US
- 2025.12.05 · 정원호 박사과정, 조만희, 송현우 석사과정, 해군사관학교장상, 2025 Militech Challenge, Korea
- 2025.11.27 · 김진 박사과정, 우수논문상, ICSV31, 2025 31st Fall Conference, Incheon, Korea
- 2025.11.27 · 정재학 교수, 우수논문상, ICSV31, 2025 31st Fall Conference, Incheon, Korea
- 2025.11.26 · 박용화 교수님, 국제학술상, ICSV31, 2025 31st Fall Conference, Incheon, Korea
- 2025.11.26 · 박용화 교수님, 진동제어최우수논문상, KSNVE, 2025 Fall Conference, Gyeongju, Korea
- 2025.10.14 · 정원호 박사과정, IES Students & Young Professional Paper Assistance Award, IEEE Industrial Electronics Society
- 2025.09.09 · 포스코홀딩스 산업용 AI-로봇 경진대회 최우수상 (기계공학과 로봇 동아리 MR 지도교수), ㈜포스코홀딩스
- 2025.05.08 · 김정민 박사과정, 미래해양과학기술인상 최우수상, 한국해양과학기술협의회 공동학술대회
- 2024.12.06 · 제5회 밀리테크챌린지 우수상 (공군사관학교장상), 과학기술전문사관지원센터
- 2024.11.15 · 김정민 박사과정, 우수논문발표상, 대한조선학회
- 2024.10.24 · 우수논문상, 한국기계기술단체총연합회
- 2024.08.28 · 임대근 박사과정, Best Student Paper Award, The 11st Asian Conference on Multibody Dynamics
- 2024.04.25 · 이경태 박사과정, 우수박사학위논문상, 대한기계학회
- 2024.02.21 · 공과대학 박사학위 최우수논문상, KAIST 공과대학
- 2022.12.13 · 장관표창, 인공지능 산업발전 유공, 과학기술정보통신부

## 연락과 위치

- 교수 이메일: yhpark@kaist.ac.kr[^contact]
- 교수 전화: 042-350-3235[^contact]
- 학생실 전화: 042-350-5235[^contact]
- 위치: KAIST 기계공학동(N7-4) 4107호 (대전 유성구 대학로 291)[^contact]

[^home]: 랩 첫 화면 <http://human.kaist.ac.kr/> (2026-10-19 열람)
[^intro]: 랩 소개 페이지(Lab Intro) <http://human.kaist.ac.kr/index.php?mid=page_BLKq48> (2026-10-20 열람)
[^cv]: 랩 교수 이력 페이지(Full CV) <http://human.kaist.ac.kr/index.php?mid=sub02_01> (2026-10-19 열람)
[^contact]: 랩 연락처 페이지 <http://human.kaist.ac.kr/index.php?mid=sub01_02> (2026-10-19 열람)
[^people]: 랩 구성원 페이지(Researcher, Ph.D. Candidates, Master Candidates) <http://human.kaist.ac.kr/index.php?mid=sub02_02> 외 (2026-10-19–20 열람)
[^alumni]: 랩 졸업생 페이지 <http://human.kaist.ac.kr/index.php?mid=sub02_04> (2026-10-19 열람)
[^vib]: 랩 연구 페이지(Vibration Analysis & Condition Monitoring) <http://human.kaist.ac.kr/index.php?mid=page_dKMm77> (2026-10-20 열람)
[^phm]: 랩 연구 페이지(Prognostics and Health Management) <http://human.kaist.ac.kr/index.php?mid=sub03_05> (2026-10-20 열람)
[^acoustic]: 랩 연구 페이지(Auditory Intelligence & Acoustic Recognition) <http://human.kaist.ac.kr/index.php?mid=sub03_02> (2026-10-20 열람)
[^health]: 랩 연구 페이지(Human Vibration & Health Sensors) <http://human.kaist.ac.kr/index.php?mid=sub03_03> (2026-10-20 열람)
[^scene]: 랩 연구 페이지(3D Scene Recognition) <http://human.kaist.ac.kr/index.php?mid=sub03_01> (2026-10-19 열람)
[^papers]: 랩 국제 학술지 목록 <http://human.kaist.ac.kr/index.php?mid=sub04_01> (2026-10-19 열람)
[^patents]: 랩 특허 목록 <http://human.kaist.ac.kr/index.php?mid=sub04_08> (2026-10-19 열람)
[^projects]: 랩 과제 게시판 <http://human.kaist.ac.kr/index.php?mid=board_MNUb09> (2026-10-19 열람)
[^awards]: 랩 수상 게시판(Awards) <http://human.kaist.ac.kr/index.php?mid=News> (2026-10-20 열람)
[^p1]: J. Hong 외, Y.-H. Park, Computer Methods and Programs in Biomedicine 280, 109311 (2026). <https://doi.org/10.1016/j.cmpb.2026.109311> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: B. Lee, J.-H. Jeong, J. Hong, Y.-H. Park, Scientific Reports 12, 19763 (온라인 2022-11-17). <https://doi.org/10.1038/s41598-022-24264-9> 초록 기준.
[^p3]: H. Nam 외, Y.-H. Park, IEEE Transactions on Audio, Speech and Language Processing 33, 3948-3960 (2025). <https://doi.org/10.1109/taslpro.2025.3603891> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: B.-Y. Ko, D. Min, H. Nam, Y.-H. Park, IEEE Transactions on Instrumentation and Measurement 74, 1-18 (2025). <https://doi.org/10.1109/tim.2025.3644532> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: G.-T. Lee 외, Y.-H. Park, Expert Systems with Applications 206, 117811 (2022). <https://doi.org/10.1016/j.eswa.2022.117811> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: J. Lee, K.-J. Park, Y.-H. Park, IEEE Transactions on Instrumentation and Measurement 73, 1-14 (2024). <https://doi.org/10.1109/tim.2024.3381257> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: S.-H. Lee, Y.-S. Lim, W.-H. Kwon, Y.-H. Park, IEEE Transactions on Instrumentation and Measurement 73, 1-13 (2024). <https://doi.org/10.1109/tim.2023.3343786> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: S. Cheong, W. Jung, Y. S. Lim, Y.-H. Park, IEEE Transactions on Geoscience and Remote Sensing 62, 1-13 (2024). <https://doi.org/10.1109/tgrs.2024.3454983> 초록 기준(Semantic Scholar 등록 초록).

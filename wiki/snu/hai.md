# 서울대학교 초자율화 인공지능 연구실

**서울대학교 공과대학 기계공학부 · 윤병동 교수**

- 영문 이름: Hyperautonomy Artificial Intelligence Lab (HAI Lab.)
- 분야: 제조 설비 고장 진단·수명 예측, 공학 설계 인공지능, 산업 안전
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 고장 진단·수명 예측[^mfm], 스마트 제조[^mfm], 데이터 중심 AI·데이터 효율 학습[^mfm], 멀티모달 AI[^mfm], 과학·공학 AI[^dfm], 설계 최적화(위상·형상 최적화)[^pi]
- 홈페이지: <http://hai.snu.ac.kr/>
- 근거와 출처: [초자율화 인공지능 연구실 근거 페이지](hai-sources.md)

> 기계의 운전 자료에서 고장을 알아내고, 설계안을 만들고 검증하며, 공장 안에서 행동하는 인공지능의 안전을 평가하는 연구실이다.[^mfm][^dfm][^physical]

## 무엇을 연구하나

초자율화 인공지능 연구실은 기계와 공장의 상태를 알아내는 일에서 설계와 의사결정까지 이어지는 산업 인공지능을 연구한다. 실험과 시뮬레이션(현상의 규칙을 모형으로 만들어 컴퓨터에서 재현하는 방법)을 함께 사용하며, 전자제품·자동차·배터리부터 발전 설비·항공기·풍력발전기·생산라인까지 다룬다. 연구실은 2010년 9월 서울대학교 기계공학부에서 설립됐다.[^about]

첫째 갈래는 **제조 현장의 자료로 기계의 상태를 이해하는 일**이다. 기계학습(자료에서 규칙을 학습해 예측이나 판단을 수행하는 방법)을 바탕으로 고장 진단·수명 예측 기술을 개발한다. 신호(시간이나 공간에 따라 달라지는 물리량으로 정보를 나타낸 것), 이미지, 글을 함께 다루는 제조 파운데이션 모델(폭넓은 자료로 미리 학습해 여러 후속 과제에 맞춰 쓰는 기본 모형)을 만든다. 실제 고장 자료가 부족한 상황을 위해 제조 신호를 생성·증강하고, 기계와 운전 조건이 달라져도 고장 정보를 유지하는 표현을 학습하는 것이 주요 과제다.[^mfm]

둘째 갈래는 **원하는 성능에서 출발해 설계안을 만들고 검증하는 일**이다. 설계·계산 자료를 학습해 새로운 설계 문제에 적용하는 기본 모형, 요구 성능으로부터 구조와 설계 변수를 찾는 역설계(목표로 하는 특성에서 그 특성을 낼 구조나 조건을 찾는 방법), 생성된 설계의 물리적 타당성을 확인하는 모형을 개발한다. 설계 기준과 전문가 경험을 온톨로지(개념의 종류와 그 사이 관계를 명시한 지식 체계)로 연결해, 설계안이 요구 조건을 만족하는지 근거를 제시하며 점검하는 에이전트(주변 정보를 바탕으로 목표를 위한 행동이나 도구 사용을 결정하는 프로그램)도 연구한다.[^dfm]

셋째 갈래는 **현실에서 행동하는 인공지능의 산업 안전**이다. 산업 환경과 운전 조건을 재현한 디지털 트윈(실제 대상의 관측 자료와 연결된 가상 모형)을 안전 분석·자료 생성·평가에 활용한다. 로봇의 행동이 과업의 뜻에 맞는지와 물리적으로 안전한지를 함께 평가하는 시험 환경을 만들며, 영상으로 그럴듯한 미래를 생성하더라도 안전 판단에 필요한 물리 상태가 보존되는지 확인하는 방법을 개발한다.[^physical]

## 주요 연구 주제

### 제조 자료 생성과 설비 고장 진단

제조 신호의 물리적 특성을 보존하는 자료 생성·증강 방법, 기계 구조와 공정 맥락을 반영하는 표현 학습(과제에 필요한 자료의 특징을 모형이 스스로 찾아 표현하도록 학습하는 방법), 신호와 이미지를 결합하는 모형을 개발한다. 생산 현장에 적용할 때에는 적은 예시로 모형을 조정하고 자료 분포의 변화를 관찰하며, 진단 결과와 공학 지식·분석 도구를 연결해 정비와 문제 해결을 돕는 의사결정 방법을 연구한다.[^mfm] 대표 논문 1은 학습 때 보지 못한 고장까지 구별하는 방법을, 대표 논문 2는 여러 천장 반송 장비 사이의 차이를 다루는 진단 방법을 제시했다.[^p1][^p2]

### 설계 생성·검증과 신뢰성

설계 변수와 형상 자료를 학습하는 모형을 만들고, 생성된 설계안의 물리적 성능과 예측의 불확실성(어떤 값이나 결과를 하나로 확정할 수 없는 정도)을 평가한다. 설계 기준·경험을 연결한 지식에 근거해 검증하는 방법도 연구한다.[^dfm] 윤병동 교수의 공식 연구 분야에는 다양한 불확실성을 고려한 신뢰성(정해진 조건과 기간에 요구 기능을 수행할 가능성) 기반 설계 최적화가 포함된다.[^pi] 대표 논문 4는 음향양자 결정(재료나 구조가 주기적으로 배열되어 소리나 탄성파의 전달을 조절하는 구조)의 역설계를, 대표 논문 5는 사용 조건이 달라지는 산업용 로봇 감속기(회전 속도를 낮추어 동력을 전달하는 기계 장치)의 설계를 다룬다.[^p4][^p5]

### 산업 안전을 위한 물리 상태 평가와 추론

산업용 사족보행 로봇의 행동을 평가하는 가상 환경, 역할별 지식을 분리해 안전한 경로와 우선 대상을 결정하는 다중 에이전트 체계, 생성 영상에 남은 물리 상태를 확인하는 평가 방법을 연구한다. 안전 조건을 모두 만족하는 경로만 받아들이고, 그렇지 않으면 다른 대상을 검토하거나 판단을 보류하도록 하는 구조를 제안한다.[^physical] 대표 논문 7은 지게차의 적재 조건을 바꾼 가상 장면을 이용해 영상 생성 모형이 물리 상태를 얼마나 보존하는지 평가했다.[^p7]

## 대표 논문

서울대 재직 시기의 논문 가운데 제조 설비 진단, 자료 생성, 공학 설계와 산업 안전을 고르게 골랐다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 7번의 발표처는 연구실 기재 표기다.

| 번호 | 연도 | 논문 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2026 | [Center margin loss-based uncertainty-aware fault diagnosis for rotating machines to identify unseen faults](https://doi.org/10.1093/jcde/qwag057)[^p1] | 학습 자료의 종류별 중심과 신경망이 추출한 특징 사이 거리를 조절하고, 그 관계로 진단의 불확실성을 계산한다. 회전 기계 자료에서 학습 때 보지 못한 고장을 구별하는 방법을 보였다. 신경망은 연결된 계산 단위의 연결 세기를 학습해 입력을 출력으로 바꾸는 모형이다. |
| 2 | 2025 | [FL-SSDAN: Fleet-level semi-supervised domain adaptation network for fault diagnosis of overhead hoist transports](https://doi.org/10.1093/jcde/qwaf058)[^p2] | 반도체 공장의 천장 반송 장비마다 다른 운전 자료와 적은 고장 표지를 함께 이용해 진단하는 방법이다. 앞뒤 모터의 회전력을 물리적으로 의미 있는 신호로 바꾸고, 어떤 특징이 판단에 기여하는지도 보여 준다. |
| 3 | 2024 | [Frequency-focused sound data generator for fault diagnosis in industrial robots](https://doi.org/10.1093/jcde/qwae061)[^p3] | 산업용 로봇 감속기의 고장 소리를 만드는 생성 모형이다. 목표 주파수 범위를 선택해 소리를 만들고, 생성한 자료로 학습한 분류기를 실제 소리로 평가했다. 주파수는 반복 현상이 단위 시간에 되풀이되는 횟수다. |
| 4 | 2025 | [Inverse design of phononic crystals with double defects using surrogate-assisted conditional generative adversarial network](https://doi.org/10.1093/jcde/qwaf060)[^p4] | 두 결함이 있는 음향양자 결정에서 목표 주파수의 파동을 통과시키는 구조를 생성한다. 성능을 대신 계산하는 모형과 설계 제약을 학습에 결합하고, 기존 최적화 방법과 비교해 설계 가능성을 평가했다. |
| 5 | 2023 | [Probabilistic framework for reliable optimal design of gearboxes in general-purpose industrial robots considering random use conditions](https://doi.org/10.1093/jcde/qwad007)[^p5] | 로봇의 사용 동작이 정해져 있지 않은 상황을 확률적으로 나타내 감속기 크기를 설계한다. 회전력과 굽힘 하중의 제한을 만족할 가능성, 부품을 조합한 시스템 수명을 함께 고려한다. |
| 6 | 2022 | [L-shape triple defects in a phononic crystal for broadband piezoelectric energy harvesting](https://doi.org/10.1186/s40580-022-00321-x)[^p6] | 음향양자 결정 안의 세 결함을 L자 형태로 배치해 폭넓은 주파수 범위에서 파동의 에너지를 모으는 구조를 제안했다. 힘을 받으면 전기적 반응을 내는 압전 현상을 이용한 발전에서 전압과 전력의 변화를 수치 계산으로 확인했다. |
| 7 | 2026 | [Physical Safety Queries Reveal What World Models Forget](http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&wr_id=359)[^p7] | 지게차 영상에서 적재물의 질량·무게중심·안정성 등 안전 관련 상태를 읽어 내는 평가 방법을 제안했다. 장면이 시각적으로 이어져 보여도 생성된 미래 영상에서는 물리 상태를 읽는 오차가 커질 수 있음을 보였다. |

## 교수와 전문 분야

윤병동 교수는 인하대학교 기계공학 학사(1996년 2월), KAIST 기계공학 석사(1998년 2월), 아이오와대학교 기계공학 박사(2001년 12월)를 받았다. 아이오와대학교 연구원, Michigan Technological University, 메릴랜드대학교를 거쳐 2010년 9월 서울대학교에 부임했고, 연구실 교수 소개는 2017년 9월부터 서울대학교 정교수로 적는다.[^professor]

기계공학부가 밝힌 전문 분야는 불확실성을 고려한 신뢰성 기반 최적설계, 고장 진단·잔여 수명 예측, 통계 기반 모형 보정·검정, 주변 에너지를 전기로 바꾸는 에너지 수확이다.[^pi] 최근 논문에서는 운전 조건이 바뀌는 장비의 진단, 고장 자료 생성, 확률적 공학 설계, 파동 전달 구조의 설계, 산업 안전 평가로 이어진다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7]

기계공학부 경력 소개는 윤 교수가 2016년 원프레딕트를 창업했고 대표이사를 맡고 있다고 적는다. 연구실 과제 목록에는 OnePredict가 지원기관인 과제도 게시되어 있다.[^pi][^projects]

## 응용 분야

제조 설비의 상태 감시와 유지보수, 반도체 생산라인의 반송 장비, 산업용 로봇, 자동차·배터리·발전 설비가 주요 응용 대상이다.[^about][^mfm][^p2][^p3] 설계 분야에서는 음향양자 결정의 파동 전달 구조와 산업용 로봇 감속기를 다루고, 산업 안전 분야에서는 사족보행 점검 로봇과 지게차의 안전 상태 평가를 다룬다.[^p4][^p5][^physical][^p7]

## 구성원

2026년 11월 7일 관측한 현재 구성원 45명이다. 과정·연구 주제·학교 이메일은 연구실 게시 표기를 따른다. ‘대표 논문 참여’는 위 논문 표의 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Juhyeong Jeon (전주형) | 박사후연구원 | Manufacturing Foundation Model |  |  |
| Joo Hyeon Im (임주현) | 박사과정 | Manufacturing Foundation Model | imjoohyeon@snu.ac.kr |  |
| Minseok Chae (채민석) | 박사과정 | Manufacturing Foundation Model | mschae1811@snu.ac.kr | 1, 2 |
| Sungjong Kim (김성종) | 박사과정 | Manufacturing Foundation Model | tjdwhd0423@snu.ac.kr |  |
| Donghyu Lee (이동휴) | 박사과정 | Design Foundation Model | ddgorae123@snu.ac.kr | 4, 7 |
| Jinoh Yoo (유진오) | 박사과정 | Physical Aritficial Intelligence | cosmbusi@snu.ac.kr | 3 |
| Seungyun Lee (이승윤) | 박사과정 | Manufacturing Foundation Mode | lsy2140@snu.ac.kr |  |
| Taehyung Kim (김태형) | 박사과정 | Manufacturing Foundation Model | grunth@snu.ac.kr |  |
| Taehun Kim (김태훈) | 박사과정 | Design Foundation Model | crown3633@snu.ac.kr | 4, 7 |
| Hansoo Kim (김한수) | 박사과정 | Manufacturing Foundation Model | hskim3231@snu.ac.kr | 1 |
| Sang Kyung Lee (이상경) | 박사과정 | Manufacturing Foundation Model | sangkyung25@snu.ac.kr | 1 |
| Yong Chae Kim (김용채) | 박사과정 | Manufacturing Foundation Model | 313nara@snu.ac.kr |  |
| Wonbin Song (송원빈) | 박사과정 | Design Foundation Model | wonbinful@snu.ac.kr |  |
| Minjae Kim (Lab. Representative) (김민재) | 박사과정 | Manufacturing Foundation Model | djm03254@snu.ac.kr |  |
| Jonghyuk Park (Lab. Representative) (박종혁) | 박사과정 | Physical Aritficial Intelligence | kbantibot@snu.ac.kr |  |
| Hyeonchan Lee (이현찬) | 박사과정 | Manufacturing Foundation Model | hyeonchan523@snu.ac.kr |  |
| Gyeong Ryun Gwon (권경륜) | 박사과정 | Manufacturing Foundation Model | oikonomia12@snu.ac.kr |  |
| Joonho Yang (양준호) | 박사과정 | Physical Aritficial Intelligence | joejhy99@snu.ac.kr |  |
| Juhyun Kim (김주현) | 박사과정 | Manufacturing Foundation Model | juhyun.k@snu.ac.kr |  |
| Jeonghwan Lee (이정환) | 박사과정 | Physical Aritficial Intelligence | sean.datsci@snu.ac.kr |  |
| Seongjoon Yoo (유성준) | 박사과정 | Design Foundation Model | sjoon0618@snu.ac.kr |  |
| Nara Ju (주나라) | 박사과정 | Design Foundation Model | worldjoo4468@snu.ac.kr |  |
| Jiheon Kang (강지헌) | 박사과정 | Manufacturing Foundation Model | perbekjh@snu.ac.kr |  |
| Mintae Kim (김민태) | 박사과정 | Prognositcs and Health Management | mintae.kim@snu.ac.kr |  |
| Seungyoon Cho (조승윤) | 박사과정 | Manufacturing Foundation Model | seungyoon.cho@snu.ac.kr |  |
| Yongmin Lee (이용민) | 박사과정 | Prognostics and Health Management for Aircraft systems |  |  |
| Minji Yoo (유민지) | 박사과정 | Resilience-driven Design for an Aircraft Structural Integrity |  |  |
| Taewan Hwang (황태완) | 박사과정 | Prognostics and Health Management for a Rolling Element Bearing System |  |  |
| Beom Chan Jang (장범찬) | 박사과정 | Prognostics and Health Management for Lithium-ion Battery |  |  |
| Yong Hwan Choi (최용환) | 박사과정 | Prognostics and Health Management for Battery Packs |  |  |
| Jingyo Jeong (정진교) | 박사과정 | Prognostics and Health Management for Power Transmission Systems | jjg4033@snu.ac.kr |  |
| Jong Keun Lim (임종근) | 박사과정 | Prognostics and Health Management for wheel Bearings and Counter-parts at Vehicle Corner Modules | snavholein1@snu.ac.kr |  |
| Seungyoung Park (박승영) | 박사과정 | Prognostics and Health Management |  |  |
| Juhwan Han (한주환) | 석사과정 | Manufacturing Foundation Model | shb06083@snu.ac.kr | 7 |
| Minseok Park (박민석) | 석사과정 | Manufacturing Foundation Model | msp1029@snu.ac.kr |  |
| Uri Lim (임우리) | 석사과정 | Manufacturing Foundation Model | dladnffl@snu.ac.kr |  |
| Haesoo Yoo (유해수) | 석사과정 | Physical Aritficial Intelligence | seawater@snu.ac.kr |  |
| Sayhee Kim (김세희) | 석사과정 | Physical Aritficial Intelligence | sayheekim@snu.ac.kr | 7 |
| Joongmyung Choi (최중명) | 석사과정 | Design Foundation Model | joongchoi@snu.ac.kr |  |
| Jong Hyun Choi (최종현) | 석사과정 | Manufacturing Foundation Model | diplomat1105@snu.ac.kr |  |
| Junho Park (박준호) | 석사과정 | Manufacturing Foundation Model | brandon525@snu.ac.kr |  |
| Bole Wang (왕박락) | 석사과정 | Physical Aritficial Intelligence | baglagwang@snu.ac.kr |  |
| Uiil Jeong (정의일) | 석사과정 | Manufacturing Foundation Model | ui.jeong@snu.ac.kr |  |
| Chan Lee (이찬) | 석사과정 | Manufacturing Foundation Model | jacob014626@snu.ac.kr |  |
| Seungchan Jeong (정승찬) | 인턴 | Knowledge-Grounded Decision Making for Physical AI | jschan0911@snu.ac.kr |  |

## 졸업생 진로

졸업생 게시 항목 93명이다. 학위·과정, 연월, 진로와 학위 논문 제목은 연구실 표기를 따른다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Keon Kim (김건) | Ph.D. Alumni (February 2025) | HD Hyundai Xitesolution | System-Level Fault Diagnosis Framework for Excavator under Operational Variations with Limited Sensor Information |
| Jongmin Park (박종민) | Ph.D. Alumni (February 2025) | SAMSUNG Electronics | Deep Learning-based Speed-robust Diagnostics Considering Inherent Fault Characteristics of Vibration Signal for Rolling Element Bearings |
| Hyunhee Choi (최현희) | Ph.D. Alumni (August 2024) | SAMSUNG Electronics | Multi-Timescale Electromechanical Identification and Stress-Reflective Modeling of Lithium-Ion Battery for Reliability-Based Design |
| Jinwook Lee (이진욱) | Ph.D. Alumni (August 2024) | SAMSUNG Electronics | Unsupervised Domain Adaptation for Cross-Domain Fault Diagnosis of Rotating Machinery Under Limited Data Information |
| Hyeongmin Kim (김형민) | Ph.D. Alumni (February 2024) | SAMSNUG Electronics | Motor fault scale-focused feature learning considering operation variability and diagnosis uncertainty |
| Jin-gyun Park (박진균) | Ph.D. Alumni (February 2024) | Naver Labs | Design of General-Purpose Industrial Robot Considering Random Use Condition and Manufacturing Uncertainty |
| Kyumin Na (나규민) | Ph.D. Alumni (August 2023) | Assistant Professor in the Department of Mechanical Engineering at Pukyong National University | An Uncertainty-Aware Framework for Fault Diagnosis in Industrial Systems Using Low and High Sampling Rate Signals |
| Jin Uk Ko (고진욱) | Ph.D. Alumni (February 2023) | SAMSUNG Electronics | Deep-learning-based Methodology for Macro- and Micro-level Fault Diagnosis of Rotating Machinery Using Low- and High-resolution Signals |
| Keunsu Kim (김근수) | Ph.D. Alumni (February 2023) | BANF Inc. | A Study on Diagnosis of Bearings in Incipient Fault Stage Considering Vibration Generation Mechanisms |
| Boseong Seo (서보성) | Ph.D. Alumni (August 2022) | LG AI Research | Deep Learning Based Health Prognostics of Oil-immersed Transformers for Contaminated Dissolved Gas Analysis Data |
| Su J. Kim (김수지) | Ph.D. Alumni (August 2022) | ONEPREDICT Inc. | Investigation on Fault Information Extraction for Acoustic Emission based Rolling Element Bearing Diagnostics under Noisy Conditions |
| Sooho Kim (김수호) | Ph.D. Alumni (February 2022) | OpenAI | Inference of Central Blood Pressure Waveform and Arterial Disease Diagnosis using Explainable Artificial Intelligence Regularized for Individuality |
| Yunhan Kim (김윤한) | Ph.D. Alumni (February 2022) | Korea Electronics Technology Institute | Vibration-based Gearbox Diagnostics by Enhancement of Weak Fault-characteristic Information |
| Chan Hee Park (박찬희) | Ph.D. Alumni (February 2022) | Assistant Professor in the Department of Mechanical and Information Engineering at University of Seoul | Physics-guided Deep Learning Study for Fault Diagnostics of Industrial Motors Under Variable Operating Conditions Using Stator Current Signals |
| Wongon Kim (김원곤) | Ph.D. Alumni (February 2022) | Assistant Professor in the Department of Mechatronics Engineering at Konkuk University | Investigation on Statistical Model Calibration and Updating of Physics and Data-driven Modeling for Hybrid Digital Twin |
| Myungyon Kim (김명연) | Ph.D. Alumni (August 2021) | SAMSUNG Electronics | Maximal Information Use for Deep Learning Based Fault Diagnosis Techniques |
| Hyejeong Son (손혜정) | Ph.D. Alumni (August 2021) | SAMSUNG Electronics | Optimization-based Model Improvement for Error Sources Identification in a Computational Model |
| Sunuwe Kim (김선의) | Ph.D. Alumni (August 2021) | SAMSUNG Electronics | Deep-Learning-Based Fault Diagnosis Using Dissolved Gas Analysis for Unlabeled Fault Data of Industrial Power Transformers |
| Yong Chang Shin (신용창) | Ph.D. Alumni (August 2021) | SAMSUNG Electronics | Highly-Dense Elastic Wave Energy Harvesting via Standing Wave Manipulation Using a Phononic Band Gap |
| Soo-Ho Jo (조수호) | Ph.D. Alumni (February 2021) | Assistant Professor in the Department of Mechanical, Robotics and Energy Engineering at Dongguk University | Modeling and Design of a Phononic Crystal with Piezoelectric Defects for Broadband Energy Localization and Harvesting |
| Junmin Lee (이준민) | Ph.D. Alumni (February 2020) | SAMSUNG Electronics | Fault Diagnostics for Motor Drive Systems with Short-circuit Failure of Insulated Gate Bipolar Transistors (IGBTs) Using System-level Measurements |
| Hyunjae Kim (김현재) | Ph.D. Alumni (February 2020) | SNJ Lab Inc. | Training Approaches for Deep Learning Based Fault Diagnosis of Rotating Machinery Overcoming Fault Data Insufficiency |
| Jungho Park (박정호) | Ph.D. Alumni (August 2019) | Wooshin Venture Investment | Fault Diagnostics of Planetary Gears under Variable-speed Conditions Using Time-frequency Analysis |
| Guesuk Lee (이규석) | Ph.D. Alumni (February 2019) | Korea Electronics Technology Institute | Sequential Optimization and Uncertainty Propagation for Optimization-Based Model Calibration |
| Joon Ha Jung (정준하) | Ph.D. Alumni (February 2019) | Associate Professor in the Department of Industrial Engineering at Ajou University | Investigation on Preprocessing and Transformation of Vibration Signals for Deep Learning Based Diagnosis of Rotating Machinery |
| Woosung Choi (최우성) | Ph.D. Alumni (August 2018) | Korea Electric Power Research Institute | A Framework for Remaining Useful Life Prediction of Steam Turbines Applicable to Various Data Types |
| Joung Taek Yoon (윤정택) | Ph.D. Alumni (February 2018) | SAMSUNG Electronics | Resilience Analysis and Design Methodology Considering False Alarms for Complex Engineered Systems |
| Heonjun Yoon (윤헌준) | Ph.D. Alumni (February 2018) | Associate Professor in the School of Mechanical Engineering at Soongsil University | Modeling and Analysis of Piezoelectric Vibration Energy Harvesting Devices under Operating and Manufacturing Uncertainties |
| Dae Whan Kim (김대환) | Ph.D. Alumni (February 2018) | LG Electronics | Bivariate Lifetime Model and Validation Procedure for Organic Light-Emitting Diode Displays |
| Jong Moon Ha (하종문) | Ph.D. Alumni (August 2017) | Assistant Professor in the Department of Mechanical Engineering at Ajou University | Robust Vibration-Based Fault Diagnosis of a Planetary Gearbox under Environmental and Operational Uncertainties |
| Taejin Kim (김태진) | Ph.D. Alumni (February 2017) | Associate Professor in the Department of Industrial and Information Systems Engineering at Jeonbuk National University | Effective Independence-Based Sensor Network Design for Health Assessment of Engineered Systems |
| Byung Chul Jeon (전병철) | Ph.D. Alumni (February 2016) | Republic of Korea Airforce | Unsupervised Learning and Diagnosis Method for Journal Bearing System in a Large-scale Power Plant |
| Lulu Wang | Ph.D. Alumni (February 2012) | Beijing Newmicrot Company | Product Design Selection Using Online Customer Reviews |
| Chao Hu | Ph.D. Alumni (August 2011) | Associate Professor at University of Connecticut | Advances in System Reliability-based Design and Prognostics and Health Management (PHM) for System Resilience Analysis and Design |
| Byung C. Jung (정병창) | Ph.D. Alumni (August 2011) | Korea Institute of Machinery and Materials | A Hierarchical Framework for Statistical Model Validation of Engineered Systems |
| Pingfeng Wang | Ph.D. Alumni (August 2010) | Professor in the Department of Industrial and Enterprise Systems Engineering at University of Illinois at Urbana-Champaign | Reliability-Based Design and Structural Health Prognostics for a Resilient System Design |
| Zhimin Xi | Ph.D. Alumni (August 2010) | Tenured Associate Professor in the Department of Industrial and Systems Engineering at the Rutgers University | A Generic Reliability Analaysis and Design Framework with a Set of Random Parameter and Field Variables |
| Jiwon Lee (이지원) | M.S. Alumni (February 2025) | SAMSUNG Electronics | Deep learning-based super resolution of time-series data for bearing fault diagnosis: Overcoming low performance sensor |
| Jonghwa Baek (백종화) | M.S. Alumni (February 2025) | ROK ARMY Special Warfare Command | Vision-based Adaptive Filter for Anomaly Detection in Rotating Machinery |
| Gyeong Ryun Gwon (권경륜) | M.S. Alumni (February 2025) | Ph.D. Student in HAI Lab | Voltage-Adapted Physics-informed Neural Network for Lithium-ion Battery State Estimation |
| Minjung Kim (김민정) | M.S. Alumni (February 2025) | SAMSUNG Electronics | Deep learning-based tacholess instantaneous speed estimation of rotating machinery using vibration signals with a selective multi-order frequency module |
| Bongmo Kim (김봉모) | M.S. Alumni | HD KSOE | Battery Capacity Estimation in Partial Charge Curve with Current Charge State Invariant Feature |
| Hye Jun Oh (오혜준) | M.S. Alumni (February 2024) | KOREAN Reinsurance Company | Cross-modal Knowledge Distillation Based Multi-domain Adaptation for Motor Fault Diagnosis |
| Taehun Kim (김태훈) | M.S. Alumni (February 2023) | Ph.D. Student in HAI Lab | Spectrum-guided GAN: A Reliable Signal Generation Approach for Fault Diagnosis of Rotating Machinery with Limited Data |
| Hwayong Jeong (정화용) | M.S. Alumni (February 2023) | HD Hyundai Xitesolution | A Study of Deep Learning-based Spall Size Distribution Estimation for Rolling Element Bearing Diagnosis |
| Dowan Kim (김도완) | M.S. Alumni (February 2022) | SAMSUNG Electronics | Fault Detection of Gearbox in Industrial Robot using Current Residual from Singular Spectrum Template Matching |
| Chaehyun Suh (서채현) | M.S. Alumni (February 2022) | SAMSUNG Electronics | Feature-analytic, Fleet-adaptive Network for Fault Diagnosis of Automated Material Handling Systems |
| Hyeonchan Lee (이현찬) | M.S. Alumni (February 2022) | Ph.D. Student in HAI Lab | A New Initial Point Search Algorithm for Bayesian Calibration with Insufficient Statistical Information: Greedy Stochastic Section Search |
| In Chan Lee (이인찬) | M.S. Alumni (February 2022) | SAMSUNG Electronics | Deep Learning-based Domain Adaptation Method for Identifying Peripheral Arterial Disease Locations under Various Severity Levels |
| Dongkyu Lee (이동규) | M.S. Alumni (August 2021) | LIG Defense&Aerospace | A Diagnosis Framework for the Robotic Arm Joint with Strain Wave Gearing based on Ordinal Pattern Analysis |
| Joo Hyeon Im (임주현) | M.S. Alumni (February 2021) | Ph.D. Student in HAI Lab | Deep Neural Network based Disease Severity Regression for Diagnosis of Abdominal Aortic Aneurysm |
| Yongjin Shin (신용진) | M.S. Alumni (February 2021) | JYP Entertainment | Deep Learning Approach for Motor Diagnosis Using Bayesian Based Class Weight Optimization |
| Jonghyun Choi (최종현) | M.S. Alumni (February 2021) | Hyundai Motors | Study of Interpretable AI based Bearing Fault Frequency Estimation Utilizing Generated Signal |
| Yeongtak Oh (오영탁) | M.S. Alumni (August 2020) | Ph.D. Student at Seoul National University | Motion-Adaptive Few-Shot Fault Detection Method of Industrial Robot Gearboxes via Residual Convolutional Neural Network |
| Myeongbaek Youn (윤명백) | M.S. Alumni (August 2020) | Patent Attorney, YUIL HIGHEST | A Weighted Residual Rényi Information (WRRI) for Detecting Fault Feature of Motor and Gearbox in Linear Time-Frequency Representation |
| Hyeon Bae Kong (공현배) | M.S. Alumni (February 2020) | Riiid! Inc. | An Automated Interpretable Deep Learning (AutoIDL) Framework Development for Prognostics and Health Management (PHM) |
| Giljun Ahn (안길준) | M.S. Alumni (February 2020) | School of Law at Seoul National University | Estimated Disturbance Decomposition Based Fault Detection for Inter-Turn Short-Circuit Fault in PMSM |
| Hao Yuan (유안 하오) | M.S. Alumni (August 2019) | Huawei Device Co., Ltd. | Minimization of Multi-Axis Interference for Fault Detection of Industrial Robots Based on Blind Sources Separation |
| Joowhan Song (송주환) | M.S. Alumni (February 2019) | Nexon Games | Deep Learning Based Acoustic Fault Severity Estimation |
| Dongki Lee (이동기) | M.S. Alumni (August 2018) | LG Electronics | Defective Motor Classification with Acoustic Signal Using Convolutional Neural Network |
| Byungjoo Jeon (전병주) | M.S. Alumni (February 2018) | Senior Data Scientist at Coupang | Bearing Incipient Fault Detection, Diagnosis, and Unsupervised Prognosis with Failure Thresholding |
| Keon Kim (김건) | M.S. Alumni (August 2017) | HD Hyundai Xitesolution | Quantitative Performance Evaluation of a Knock Sensor for Vibration-Based Fault Diagnosis in a Planetary Gearbox |
| Hwanoh Choi (최환오) | M.S. Alumni (August 2016) |  | A New Calibration Metric - Probability Residual (PR) and Its Validation Practice for Rotor Dynamics Model of a Journal Bearing Rotor System |
| Sihyeong Woo (우시형) | M.S. Alumni (February 2016) | Republic of Korea Airforce | Time-Domain Reflectometry based Multiple Leak Detection System using Bayesian Inference and S-parameters Transmission Line Model for Pipelines |
| Jinshi Cui (최금실) | M.S. Alumni (August 2015) | SKF | Reliability-Based Design Optimization of Omnidirectional Energy Harvesting Sidewalk Block Considering Human Gait Analysis |
| Kyung Min Park (박경민) | M.S. Alumni (February 2014) | SAMSUNG Electronics | Statistical Health Reasoning System of Power Generator Stator Windings against Water Absorption |
| Chulmin Cho (조철민) | M.S. Alumni (February 2014) | SAMSUNG Electronics | Power Usage Maximization of a Piezoelectric Energy Harvesting Skin |
| Jong Moon Ha (하종문) | M.S. Alumni (August 2013) | Assistant Professor in the Department of Mechanical Engineering at Ajou University | Vibration-based Framework for Fault Diagnostics of Wind Turbine Gearbox |
| Seunghyuk Choi (최승혁) | M.S. Alumni (August 2013) | Agency for Defense Development | A Performance Degradation Model for Warranty Abuse Detection in Portable Electronics |
| Heonjun Yoon (윤헌준) | M.S. Alumni (February 2013) | Associate Professor in the School of Mechanical Engineering at Soongsil University | Analytical Model for Electric Power Prediction of Piezoelectric Energy Harvesting |
| Jisun Kim (김지선) | M.S. Alumni (February 2013) | Teaching Professor in Mechanical Engineering at Keimyung University | A Model Refinement Framework for Statistical Model Validation |
| Yein Park (박예인) | Post Doctor Alumni | Electronics and Telecommunications Research Institute |  |
| Xi Xiaopeng (시 샤오펑) | Post Doctor Alumni | Assistant Professor in SolBridge International School of Business at Woosong University |  |
| Chen Jiang (장 첸) | Post Doctor Alumni | Assistant Professor at Huazhong University of Science and Technology |  |
| Haichao An (안해조) | Post Doctor Alumni | Associate Professor at Beijing Institute of Technology |  |
| Junpeng Zhao (준펭 자오) | Post Doctor Alumni | Associate Professor at Beihang University |  |
| Vikas Sharma (비카스 샤마) | Post Doctor Alumni | Assistant Professor at The LNM Institute of Information Technology |  |
| Guilian Yi (이계연) | Post Doctor Alumni | R&D Engineer at Ansys Inc. |  |
| Moussa Hamadache (무사 하마다시) | Post Doctor Alumni | Associate Professor at M’Hamed BOUGARA University of Boumerdes |  |
| Kyung Ho Sun (선경호) | Post Doctor Alumni | Korea Institute of Machinery and Materials |  |
| Hyunseok Oh (오현석) | Post Doctor Alumni | Professor at Gwangju Institute of Science and Technology |  |
| Young Woo Park (박영우) | Post Doctor Alumni | SAMSUNG Engineering |  |
| Soobum Lee (이수범) | Post Doctor Alumni | Associate Professor at University of Maryland, Baltimore County |  |
| Fengmiao Tu | Others Alumni |  |  |
| Rhys MASSE | Others Alumni (Graduate Student) |  |  |
| Mingxuan ZHU | Others Alumni (Graduate Student) |  |  |
| Dapeng Wang | Others Alumni (Graduate Student) |  |  |
| Meide Yang | Others Alumni (Graduate Student) | Hunan University |  |
| Suyeon Byun (변수연) | Others Alumni (Programming Engineer) | Pennsylvania State University |  |
| Insik Kim (김인식) | Others Alumni (Programming Engineer) | Naver |  |
| Hosang Chun (천호상) | Others Alumni (Programming Engineer) | University of Illinois, Urbana-Champaign |  |
| Suhak Lee (이수학) | Others Alumni (Intern) | University of Michigan, Ann Arbor |  |
| Bak Won (원박) | Others Alumni (Intern) | Daewoo Shipbuilding and Marine Engineering |  |

## 최근 5년 논문 목록

2021년 10월 22일부터 2026년까지의 논문 게시 항목 270편으로, 학술지 87편과 학회 183편이다. 연도는 연구실의 연도 구역과 기재 날짜를 따른다. 학술지의 Accept 표기는 ‘게재 승인’으로 구분하고, 2026년 구역의 게재 승인 논문을 함께 싣는다. 학회명과 날짜는 연구실 기재 표기다.[^journals][^conferences]

**2026**

- Hyeongmin Kim, Taehun Kim, Wonbin Song, Jong Moon Ha\*, and Byeng D. Youn\*. "Domain Knowledge-Informed Neural Networks for Prognostics and Health Management: A State-of-the-Art Review and Taxonomy". *Archives of Computational Methods in Engineering (게재 승인)*.
- Taeri Kim¹, Sang Kyung Lee¹, Gun Jin Yun\*, Byeng D. Youn\*, and Christian Gogu\*. "Self-supervised Learning for Remaining Useful Life prediction of Composite Materials based on Physics-based Synthetic Strain Data". *Journal of Computational Design and Engineering (게재 승인)*.
- Xiaojing Yin, Chuang Nie, Xiaopeng Xi\*, and Byeng D. Youn\*. "A Multi-Evidence-Based Open-Set Domain Generalization Method for Bearing Fault Diagnosis". *Cybernetics and Intelligence (게재 승인)*.
- Hyeongmin Kim¹, Sangwook Langenstück-Lee¹, Donghyu Lee, Florian Hüsing, Henning Janssen, Christian Brecher, and Byeng D. Youn\*. "Deep Learning-based Rapid and Precise Die Design to Compensate Springback in Metallic Bipolar Plate Stamping for Proton Exchange Membrane Fuel Cells". *Measurement, 2026-11, Vol. 290, pp. 122923 · DOI <https://doi.org/10.1016/j.measurement.2026.122923>*.
- Jongheok Park, Donghyu Lee, Wonjae Choi, Byeng D. Youn\*, and Jong Moon Ha\*. "A Robust Deep Learning Framework for Weld Defect Classification in PAUT With Specimen-Level Preprocessing". *NDT & E International, 2026-10, Vol. 164, pp. 103840 · DOI <https://doi.org/10.1016/j.ndteint.2026.103840>*.
- Sang Kyung Lee, Hyeongmin Kim, Minseok Chae, Hansoo Kim, Joonho Yang, Heonjun Yoon\*, and Byeng D. Youn\*. "Frequency-Band Graph-based Sensor Fusion with Sensitivity-aware Energy Assist Network for Machinery System Fault Diagnosis". *Engineering Applications of Artificial Intelligence, 2026-09, Vol. 179, pp. 115273 · DOI <https://doi.org/10.1016/j.engappai.2026.115273>*.
- Jingyo Jeong, Jeong H. Choi, Wongon Kim\*, and Byeng D. Youn \*. "Time-Domain Signal Denoising and Expert Decision-Support Visualization with AttenTDNet for High-Voltage Power-Cable Joint-Box Monitoring". *Electrical Engineering, 2026-08, Vol. 108, pp. 364 · DOI <https://doi.org/10.1007/s00202-026-03721-y>*.
- Taehun Kim, Donghyu Lee, Juhwan Han, Sayhee Kim, Byeng D. Youn \*, and Soo-Ho Jo\*. "Structural Dependency-Aware Generative Design of Elastic Metasurfaces via Pseudo-Supervised Attention-based Transformer". *Computer Methods in Applied Mechanics and Engineering, 2026-08, Vol. 458, pp. 119041 · DOI <https://doi.org/10.1016/j.cma.2026.119041>*.
- Hyeongmin Kim, Minseok Chae, Hansoo Kim, Sang Kyung Lee, Hye Jun Oh, Heonjun Youn\*, and Byeng D. Youn\*. "Center Margin Loss-based Uncertainty-aware Fault Diagnosis for Rotating Machines to Identify Unseen Faults". *Journal of Computational Design and Engineering, 2026-07, Vol. 13, No. 7, pp. 20-34 · DOI <https://doi.org/10.1093/jcde/qwag057>*.
- Jay Lee\*, Hanqi Su\*, Marco Macchi, Adalberto Polenghi, Wei Wu, Zhiheng Zhao, George Q Huang, Kiva Allgood, Devendra Jain, Benedikt Gieger, Vibhor Pandhare, Soumyabrata Bhattacharjee, Ram Mohril, Lingbao Kong, Sungjong Kim, Chan Hee Park, Byeng D Youn, Guo D Goh, Xi Huang, Wai Yee Yeong, Yung C Shin, He Zhang, Zitong Wang, Fei Tao, Jagjit Singh Srai, Satyandra Gupta, Byung Gun Joung, Albin John, John W Sutherland, Sang W Lee, Olga Fink, Vinay Sharma, Faez Ahmed, Wei (Wayne) Chen, Mark Fuge, Arild Waaler, Martin G Skjæveland, Dimitris Kiritsis, Wei Chen, Vispi Nevile Karkaria, Yi-Ping Chen, Ying-Kuan Tsai, Joseph Cohen, Xun Huan, Jing (Janet) Lin, Liangwei Zhang, Gregory W Vogl, Aaron W Cornelius, Xiaodong Jia, Dai-Yan Ji, Takanobu Minami and Ruoxin Wang. "2026 Roadmap on Artificial Intelligence and Machine Learning for Smart Manufacturing". *Machine Learning: Engineering, 2026-07, Vol. 2, pp.022001 · DOI <https://doi.org/10.1088/3049-4761/ae5967>*.
- Sungjong Kim, Seungyun Lee, Jiwon Lee, Minjae Kim, Heonjun Yoon\*, and Byeng D. Youn\*. "Multi-scale Signal Transformer with Signal Processing-Based Attention Interpretation for Fault Diagnosis of Rotating Machinery under Variable Speed Conditions". *Reliability Engineering & System Safety, 2026-07, Vol. 271, pp. 112243 · DOI <https://doi.org/10.1016/j.ress.2026.112243>*.
- Yong Chae Kim, Bongmo Kim, MinJung Kim, Sang Kyung Lee, Joon Ha Jung\*, and Byeng D. Youn\*. "Physics-guided Deep Ensemble Learning for the Remaining Useful Life Prediction of Machine Tools Using Kernel Density Estimation". *International Journal of Precision Engineering and Manufacturing-Green Technology, 2026-05, Vol. 13, No. 3, pp. 875-892 · DOI <https://doi.org/10.1007/s40684-025-00827-9>*.
- Minseok Chae, Hyeongmin Kim, Sang Kyung Lee, Hansoo Kim, Joonho Yang, Heonjun Yoon\*, and Byeng D. Youn\*. "An Adapter-Enhanced, Fourier Feature Deep Operator Network for Fault Severity Estimation of Stator Inter-Turn Short Circuits in Induction Motors". *Engineering Applications of Artificial Intelligence, 2026-04, Vol. 170, pp. 114197 · DOI <https://doi.org/10.1016/j.engappai.2026.114197>*.
- Juhyun Kim, Yong Chae Kim, Jongwha Baek, Jinwook Lee, Joon Ha Jung\*, and Byeng D. Youn\*. "ARDiff: An Adaptive Reverse-Step Diffusion Framework for Unsupervised Vibration Signal Denoising with Frequency Attention". *Mechanical Systems and Signal Processing, 2026-01, Vol. 244, pp. 113726 · DOI <https://doi.org/10.1016/j.ymssp.2025.113726>*.
- Juhwan Han, Taehun Kim , Donghyu Lee , Sayhee Kim , Soo-Ho Jo, Byeng D. Youn. "Physical Safety Queries Reveal What World Models Forget". *Conference : ECCV 2026, 2026-09-09*.
- Sang Kyung Lee, Hyeongmin Kim, Minseok Chae, Hansoo Kim, Joonho Yang, Heonjun Yoon, Byeng D. Youn. "Graph-Based Multi-Sensor Fusion with Frequency-Band Decomposition for System-Level Machinery Fault Diagnosis". *Conference : ASME IDETC-CIE 2026, 2026-08-26*.
- Hansoo Kim, Minseok Chae, Sang Kyung Lee, Joonho Yang, Heonjun Yoon, Byeng D. Youn. "Physics-Guided Virtual Metrology of Motor Current Signals for Fault Diagnosis Under Unseen Conditions". *Conference : ASME IDETC-CIE 2026, 2026-08-26*.
- Jinoh Yoo, Hyeonchan Lee, Ju Hwan Han, Seongpil Ju, Juho Kim, Yong Gwon Jeon, Dae Un Sung, Byeng Dong Youn. "Vehicle Mass Estimation via EKF-Based Virtual Sensing Considering Mechanical Efficiency Variability". *Conference : ASME IDETC-CIE 2026, 2026-08-25*.
- Minjae Kim, Sungkyun Kim, Seungyun Lee, Heonjun Yoon, Byeng D. Youn. "Ex-MIND: An Expert-Inspired Multi-Task Learning Framework Based on Industrial Domain Knowledge for Trustworthy Rotating Machinery Fault Diagnosis Under Environmental Shifts". *Conference : ASME IDETC-CIE 2026, 2026-08-24*.
- Juhwan Han, Taehun Kim, Donghyu Lee, Sayhee Kim, Soo-Ho Jo, Byeng Dong Youn. "Counterfactual Data Generation via World Models for Enhancing Industrial Safety in Rare Event Scenarios". *Conference : Asian Congress of Structural and Multidisciplinary Optimization (ACSMO) 2026, 2026-05-19*.
- Sayhee Kim, Donghyu Lee, Taehun Kim, Ju Hwan Han, Soo-Ho Jo, , Byeng Dong Youn. "Scalable Deep Learning for Dispersion Relation Prediction in 2D Defective Phononic Crystals". *Conference : Asian Congress of Structural and Multidisciplinary Optimization (ACSMO) 2026, 2026-05-19*.
- Jiheon Kang, Gyeong Ryun Gwon, Seungyun Lee, Minjae Kim, Guesuk Lee, Byeng Dong Youn. "Cost-Effective Autonomous Experimental Design for Battery State-of-Health Prediction Using a Need Score". *Conference : Asian Congress of Structural and Multidisciplinary Optimization (ACSMO) 2026, 2026-05-19*.
- Wonbin Song, Guesuk Lee, Byeng Dong Youn. "DeepONet-Driven Probabilistic Thermal Characterization and Inverse Parameter Sensitivity Analysis for Power Semiconductor Packages". *Conference : Asian Congress of Structural and Multidisciplinary Optimization (ACSMO) 2026, 2026-05-19*.
- Haesoo Yoo, Wonbin Song, Guesuk Lee, Byeng Dong Youn. "A Structured Method for Automating Multiphysics Simulations Using Large Language Models". *Conference : A Structured Method for Automating Multiphysics Simulations Using Large Language Models, 2026-05-19*.
- Donghyu Lee, Taehun Kim, Juhwan Han, Sayhee Kim, Soo-Ho Jo, Byeng Dong Youn. "Transformer-based Latent Diffusion Model for Inverse Design of Phononic Crystals with Structural Variability". *Conference : Asian Congress of Structural and Multidisciplinary Optimization (ACSMO) 2026, 2026-05-18*.
- Taehun Kim, Donghyu Lee, Juhwan Han, Sayhee Kim, Soo-Ho Jo, Byeng Dong Youn. "End-to-End Generative Framework for the Inverse Design of Multi-functional Elastic Metasurfaces". *Conference : Asian Congress of Structural and Multidisciplinary Optimization (ACSMO) 2026, 2026-05-18*.
- 이상경, 김태리, 윤군진, 윤병동. "물리 기반 합성 변형률 데이터를 활용한 복합재료의 잔여수명 예측을 위한 시간 정보 기반 자기지도학습". *Conference : 한국PHM학회 2026년도 정기학술대회, 2026-06-26*.
- 주나라, 채민석, 윤병동, 김태진. "동기 릴럭턴스 모터의 전자기 응답 및 응력 장 예측을 위한 형상 기반 분리형 대리 모델". *Conference : 한국PHM학회 2026년도 정기학술대회, 2026-06-26*.
- 임주현, 김성종, 윤헌준, 윤병동. "Heterogeneous Sensor Integration for Machinery Fault Diagnosis via Band-partitioned Capsules and Interactive Attention Routing". *Conference : 한국PHM학회 2026년도 정기학술대회, 2026-06-26*.
- 채민석, 김용채, 이상경, 김주현, 강지헌, 임우리, 최종현, 박준호, 박찬희, 하종문, 윤병동. "주파수 축 토큰 학습 기반 고주파 진동 시계열 회전체 파운데이션 모델". *Conference : 한국PHM학회 2026년도 정기학술대회, 2026-06-26*.
- 김한수, Christian Gogu, Sebastien Schwartz, 윤병동. "모터 고장 진단을 위한 계층적 증거 추론 및 직교 분해 기반 다중 도메인 프레임워크". *Conference : 한국PHM학회 2026년도 정기학술대회, 2026-06-26*.
- 조승윤, 김한수, 박찬희, 윤병동. "베어링 고장진단을 위한 회전 호환형 표현과 전역 구조 유도 확산모델". *Conference : 한국PHM학회 2026년도 정기학술대회, 2026-06-25*.
- 이현찬, 유진오, 김태형, 하종문, 윤병동. "극단적 고장 데이터 부족 조건 하 베어링 고장 진단을 위한 Fourier Neural Operator 기반 고장 신호 분리 모듈 개발". *Conference : 한국PHM학회 2026년도 정기학술대회, 2026-06-25*.
- 김태훈, 김민재, 이용민, 윤병동, 김태우. "전이학습 및 물리 정보 신경망을 활용한 항공기 배터리 상태 추정". *Conference : 2026 한국군사과학기술학회 종합학술대회, 2026-06-11*.
- 김한수, 권경륜, 이홍철, 유종환, 윤병동. "유도무기체계 CBM+ 적용 방안 연구". *Conference : 2026 한국군사과학기술학회 종합학술대회, 2026-06-10*.
- 이승윤, 김봉모, 이지원, 이용민, 김태우, 윤병동. "고정익항공기용 배터리 고장 예지 및 건전성 모니터링 기법 개발을 위한 사전연구". *Conference : 2026 한국군사과학기술학회 종합학술대회, 2026-06-10*.
- 이상경, 김주현, 손혜정, 윤병동. "다변량 조건을 고려한 실험 설계 및 반도체 CMP 공정 결과 예측 모 델링 프레임워크". *Conference : 대한기계학회 CAE 및 응용역학부문 2026년 춘계학술대회, 2026-05-07*.
- 이정환, 김태훈, 유진오, 양준호, 박찬희, 윤병동. "이종 온톨로지 기반 다중 에이전트 시스템을 활용한 사족보행 로봇의 재난 환경 내 안전 탐색 프레임워크". *Conference : 대한기계학회 CAE 및 응용역학부문 2026년 춘계학술대회, 2026-05-07*.
- 권경륜, 이승윤, 김민재, 강지헌, 김태진, 윤병동. "부분 방전 데이터를 활용한 DeepONet 기반 리튬이온배터리 상태 추정". *Conference : 대한기계학회 CAE 및 응용역학부문 2026년 춘계학술대회, 2026-05-07*.
- 임우리, 김용채, 김주현, 박민석, 최종현, 정준하, 윤병동. "프롬프트 확장 기반 지속 학습을 통한 베어링 결함 진단". *Conference : 대한기계학회 CAE 및 응용역학부문 2026년 춘계학술대회, 2026-05-07*.
- 김주현, 김용채, 박민석, 임우리, 최종현, 정준하, 윤병동. "간섭 환경 내 설비 상태 관리를 위한 타겟 음향 신호 추출 기술". *Conference : 대한기계학회 CAE 및 응용역학부문 2026년 춘계학술대회, 2026-05-07*.
- 김용채, 김주현, 박민석, 임우리, 최종현, 정준하, 윤병동. "운전속도 변화 환경에서의 회전체 고장진단을 위한 연속 도메인 적응 기법". *Conference : 대한기계학회 CAE 및 응용역학부문 2026년 춘계학술대회, 2026-05-07*.
- 채민석, 김용채, 이상경, 김주현, 강지헌, 임우리, 최종현, 박준호, 박찬희, 하종문, 윤병동. "주파수 축 토큰 학습 기반 회전체 파운데이션 모델". *Conference : 대한기계학회 CAE 및 응용역학부문 2026년 춘계학술대회, 2026-05-07*.
- 송원빈, 이규석, 윤병동. "반도체 패키지 방열 품질 관리를 위한 확률론적 열 구조 함수". *Conference : 제33회 한국반도체학술대회, 2026-01-29*.

**2025**

- Bongmo Kim, Yong Chae Kim, Hyunhee Choi, Gyeong Ryun Gwon, Taejin Kim\*, and Byeng D. Youn\*. "Battery Maximum Available Capacity Estimation in Partial Charge Curve with Current Charge State Invariant Feature". *Journal of Energy Storage, 2025-12, Vol. 138, pp. 118726 · DOI <https://doi.org/10.1016/j.est.2025.118726>*.
- Donghyu Lee, Taehun Kim, Ju Hwan Han, Sayhee Kim, Byeng D. Youn\*, and Soo-Ho Jo\*. "Transformer-Based Prediction of Dispersion Relation and Transmittance in Phononic Crystals". *International Journal of Mechanical Sciences, 2025-12, Vol. 307, pp. 110880 · DOI <https://doi.org/10.1016/j.ijmecsci.2025.110880>*.
- Soo-Ho Jo¹, Taehun Kim¹, Donghyu Lee, Pengpeng Yu, Junlei Wang, Byeng D. Youn, and Heonjun Yoon\*. "Steering of Multiple Defect Bands in One-dimensional Phononic Crystals with Segmented Piezoelectric Defects". *Journal of Physics D-Applied Physics, 2025-11, Vol. 58, No. 46 pp. 465501 · DOI <https://doi.org/10.1088/1361-6463/ae1a95>*.
- Sina Masoumi Shahrbabak, Byeng D. Youn, Hao-Min Cheng, Chen-Huan Chen, Shih-Hsien Sung, Ramakrishna Mukkamala, and Jin-Oh Hahn\*. "Deep Learning-Enabled Diagnosis of Abdominal Aortic Aneurysm Using Pulse Volume Recording Waveforms: An In-Silico Study". *Sensors, 2025-11, Vol. 25, No. 21 pp. 6678 · DOI <https://doi.org/10.3390/s25216678>[^bioaaa]*.
- Jongmin Park, Jinoh Yoo, Taehyung Kim, Minjung Kim, Jonghyuk Park, Jong Moon Ha\*, and Byeng D. Youn\*. "Spectral Kurtosis Attention Network (SKAN): Synergizing Signal Processing and Deep Learning for Fault Diagnosis of Rolling Element Bearings". *Expert Systems with Applications, 2025-11, Vol. 292, pp. 128581 · DOI <https://doi.org/10.1016/j.eswa.2025.128581>*.
- Minjung Kim, Yong Chae Kim, Jinoh Yoo, Jongmin Park, Taehyung Kim, Jong Moon Ha\*, and Byeng D. Youn\*. "Deep Learning-based Cross-domain Tacholess Instantaneous Speed Estimation of Rotating Machinery with a Selective Multi-order Frequency Module". *IEEE Sensors Journal, 2025-10, Vol. 25, No. 20 pp. 37810-37820*.
- Wonbin Song, Guesuk Lee\*, and Byeng D. Youn\*. "Toward Robust Structure Function-Based Thermal Analysis: Quantitative Metrics for Semiconductor Packaging Evaluation". *Microelectronics Reliability, 2025-10, Vol. 173, pp. 115867 · DOI <https://doi.org/10.1016/j.microrel.2025.115867>*.
- Donghyu Lee, Taehun Kim, Byeng D. Youn\*, and Soo-Ho Jo\*. "Inverse Design of Defective Phononic Crystals Using Surrogate-assisted Conditional Generative Adversarial Network". *Journal of Computational Design and Engineering, 2025-07, Vol. 12, No. 7, pp. 129-147 · DOI <https://doi.org/10.1093/jcde/qwaf060>*.
- Chaehyun Suh¹, Hyeongmin Kim¹, Chan Hee Park, Minseok Chae, Joung Taek Yoon, Ilkyu Lee, Heonjun Yoon\*, and Byeng D. Youn\*. "FL-SSDAN: Fleet-Level Semi-Supervised Domain Adaptation Network for Fault Diagnosis of Overhead Hoist Transports". *Journal of Computational Design and Engineering, 2025-07, Vol. 12, No. 7, pp. 49-60 · DOI <https://doi.org/10.1093/jcde/qwaf058>*.
- Sungjong Kim, Seungyun Lee, Jiwon Lee, Minjae Kim, Su J. Kim, Heonjun Yoon\*, and Byeng D. Youn\*. "Fault-Relevance-Based, Multi-Sensor Information Integration Framework for Fault Diagnosis of Rotating Machineries". *Mechanical Systems and Signal Processing, 2025-06, Vol. 232, pp. 112742 · DOI <https://doi.org/10.1016/j.ymssp.2025.112742>*.
- Chen Jiang, Teng Zhong, Hyunhee Choi, and Byeng D. Youn\*. "Physics-informed Gaussian Process Probabilistic Modeling with Multi-source Data for Prognostics of Degradation Processes". *Reliability Engineering & System Safety, 2025-06, Vol. 258, pp. 110893 · DOI <https://doi.org/10.1016/j.ress.2025.110893>*.
- Hyunhee Choi, Yong Hwan Choi, Byeng D. Youn\*, and Guesuk Lee\*. "Sequential Optimization-Based Parameter Identification for Multi-Timescale Electromechanical Model of Battery". *Journal of Energy Storage, 2025-03, Vol. 112, pp. 115481 · DOI <https://doi.org/10.1016/j.est.2025.115481>*.
- Kyumin Na¹, Keon Kim¹, Jinoh Yoo, Jinwook Lee, and Byeng D. Youn\*. "Optimized Relative Entropy for Robust Fault Detection in Excavator Traveling Gearboxes via Smeared Envelope Spectrum Analysis of Cyclo-Non-Stationary Signals". *Expert Systems with Applications, 2025-03, Vol. 266, pp. 126110 · DOI <https://doi.org/10.1016/j.eswa.2024.126110>*.
- Taehyung Kim, Jongmin Park, Jinoh Yoo, Jong Moon Ha\*, and Byeng D. Youn\*. "Enhancing Gearbox Fault Diagnosis Under Phase Estimation Errors: A Dynamic Time Warping and Blind Deconvolution Approach". *Journal of Sound and Vibration, 2025-03, Vol. 598, pp. 118851 · DOI <https://doi.org/10.1016/j.jsv.2024.118851>*.
- Chen Jiang, Zhen Hu, Alba Sofi, Liang Gao, Haobo Qiu, and Byeng D. Youn. "Special Section on Uncertainty-Aware Diagnostics and Prognostics for Health Monitoring and Risk Management of Engineered Systems". *The American Society of Mechanical Engineers, 2025-03, Vol. 11, No.1, pp.010301 · DOI <https://doi.org/10.1115/1.4067253>*.
- Jongmin Park, Jinoh Yoo, Taehyung Kim, Minjung Kim, Jonghyuk Park, Jong Moon Ha\*, and Byeng D. Youn\*. "Fault frequency Band Segmentation and Domain Adaptation (FBSDA) with Fault Simulated Signal for Fault Diagnosis of Rolling Element Bearings". *Journal of Computational Design and Engineering, 2025-01, Vol. 12, No. 1, pp. 34-52 · DOI <https://doi.org/10.1093/jcde/qwae105>*.
- Haichao An\*, Yao Zhang, Qinyun Deng, Teng Long\*, Byeng D. Youn, and Heung Soo Kim. "Integrated Optimization of Ply Number, Layer Thickness, and Fiber Angle for Variable-stiffness Composites Using Dynamic Multi-fidelity Surrogate Model". *Thin-Walled Structures, 2025-01, Vol. 206, pp. 112392 · DOI <https://doi.org/10.1016/j.tws.2024.112392>*.
- Wongon Kim and Byeng D. Youn\*. "Physics-based Digital Twin Updating and Twin-based Explainable Crack Identification of Mechanical Lap Joint". *Reliability Engineering & System Safety, 2025-01, Vol. 253, pp. 110515 · DOI <https://doi.org/10.1016/j.ress.2024.110515>*.
- Sungjong Kim, Seungyun Lee, Minjae Kim, Heonjun Yoon, Byeng D. Youn. "Interpretable Sensor Importance-Based Multi-Sensor Integration for Condition Monitoring of Rotating Machinery". *Conference : The Asia Pacific Prognostics and Health Management Conference 2025, 2025-12-10*.
- Taehyung KIm, Jongmin Park, Jinoh Yoo, Jong Moon Ha, Byeng D. Youn. "Fault Diagnosis of Gearbox under Phase Estimation Error by Sequenctial Alignment Based on Dynamic Time Wraping of D Norms". *Conference : ASME 2025 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference, 2025-08-20*.
- Sang Kyung Lee, Hyeongmin Kim, Minseok Chae, Hye Jun Oh, Heonjun Yoon, Byeng D. Youn. "Self-supervised Stator Current Representation Learning for Motor Fault Diagnosis". *Conference : ASME 2025 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference, 2025-08-18*.
- Juhyun Kim, Yong Chae Kim, Jonghwa Baek, Jinwook Lee, Joon Ha Jung, Byend D. Youn. "Signal Reconstruction of Rotating Machinery Using a Frequency Focused And Reverse Step-Aware Diffusion Model". *Conference : ASME 2025 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference, 2025-08-18*.
- Yong Chae Kim, Jinwook Lee, Taehun Kim, Jonghwa Baek , Jin Uk Ko, Joon Ha Jung, Byeng D. Youn. "Partial Transfer Learning using Domain Knowledge Filter for Fault Diagnosis of Bearing". *Conference : ASME 2025 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference, 2025-08-18*.
- Taehun Kim, Donghyu Lee, Soo-Ho Jo, and Byeng D. Youn. "Generative AI-driven Inverse Design of Elastic Metasurface for Anomalous Refraction with Full Transmission". *Conference : 16th World Congress on Structural and Multidisciplinary Optimization, 2025-05-19*.
- 이동휴, 김태훈, 한주환, 김세희, 윤병동, 조수호. "음향양자 결정의 해석을 위한 트랜스포머 기반 대리모델 개발". *Conference : 대한기계학회 2025년 학술대회, 2025-12-12*.
- 박민석, 김태형, 김용채, 김주현, 임우리, 정준하, 윤병동. "환경 소음이 포함된 음원에서 베어링 타겟 음원 추출 방법". *Conference : 대한기계학회 2025년 학술대회, 2025-12-12*.
- 김태훈, 이동휴, 한주환, 김세희, 조수호, 윤병동. "탄성파 제어를 위한 딥러닝 기반 역설계 모델 개발". *Conference : 대한기계학회 2025년 학술대회, 2025-12-12*.
- 김민태, 정준하, 윤병동. "딥러닝 기반 전류 분석을 통한 프린터 정착기 고장 진단". *Conference : 대한기계학회 2025년 학술대회, 2025-12-12*.
- 이현찬,유진오, 한주환, 주성필, 김주호, 전용권, 성대운, 윤병동. "CAN 데이터 기반 가상 센서를 활용한 전기차 실시간 중량 추정 기법". *Conference : 대한기계학회 2025년 학술대회, 2025-12-10*.
- 한주환, 유진오, 이현찬, 주성필, 김주호, 전용권, 성대운, 윤병동. "CAN 데이터 기반 후륜구동 전기차의 축별 중량 추정 및 검증". *Conference : 대한기계학회 2025년 학술대회, 2025-12-10*.
- 강지헌, 권경륜, 이승윤, 김민재, 윤병동. "가변 온도 조건에서 임피던스를 활용한 리튬 이온 배터리 상태 추정에 대한 기초 연구". *Conference : 한국PHM학회 2025년도 정기학술대회, 2025-06-25*.
- 김한수, 김형민, 채민석, 오혜준, 이상경, 윤헌준, 윤병동. "가변 운행 환경에서의 모터 전류 잔차 분석을 위한 Park 벡터 모듈러스 기반 적응 커널 가우시안 프로세스 회귀 기법". *Conference : 한국PHM학회 2025년도 정기학술대회, 2025-06-25*.
- 조수호, 김선의, 박종민, 김원곤, 윤병동. "도메인 지식 기반 심층 신경망을 활용한 강건한 전력 변압기 고장 진단". *Conference : 한국PHM학회 2025년도 정기학술대회, 2025-06-25*.
- 이승윤, 권경륜, 김민재, 강지헌, 이규석, 윤병동. "전기-기계적 상관성을 활용한 딥러닝 기반 전기자동차 배터리 열화 예측". *Conference : 한국PHM학회 2025년도 정기학술대회, 2025-06-25*.
- 임주현, 김성종, 윤헌준, 윤병동. "크로스 어텐션 기반 라우팅 캡슐 네트워크를 활용한 모터 고장 진단 방법". *Conference : 한국PHM학회 2025년도 정기학술대회, 2025-06-25*.
- 김용채, 김주현, 박민석, 정준하, 윤병동. "시뮬레이션 신호를 활용한 주파수 대역 기반 특성을 활용한 베어링 상태 추적 알고리즘 개발". *Conference : 한국PHM학회 2025년도 정기학술대회, 2025-06-24*.
- 김주현, 김용채, 박민석, 정준하, 윤병동. "회전체 혼합 음향 신호에서 타겟 소리 추출을 위한 스펙트럼 유도형 Autoencoder 기법 개발". *Conference : 한국PHM학회 2025년도 정기학슬대회, 2025-06-24*.
- 채민석, 이상경, 김한수, 양준호, 윤헌준, 윤병동. "사전분포 랜덤화 앙상블을 이용한 모터 권선열화 고장 심각도 추정 및 불확실성 정량화". *Conference : 한국PHM학회 2025년도 정기학술대회, 2025-06-24*.
- 하종문, 박종민, 윤병동. "가상 결함 신호의 물리 정보를 활용한 딥러닝 기반 베어링 진단기법 개발". *Conference : 한국PHM학회 2025년도 정기학술대회, 2025-06-24*.
- 주나라, 김용채, 송원빈, 윤병동. "실시간 얼굴 추적과 3D 유사도 검사를 통한 차량 영상 이상자 감지 프레임워크". *Conference : 한국PHM학회 2025년도 정기학술대회, 2025-06-24*.
- 김건, 임원종, 정화용, 정준하, 윤병동. "건설기계의 시스템 레벨 고장 진단을 위한 프레임워크". *Conference : 한국PHM학회 2025년도 정기학술대회, 2025-06-24*.
- 박종혁, 이동휴, 최원재, 윤병동, 하종문. "인공지능 기반 용접 결함 분류에서 A-scan 및 S-scan PAUT 데이터의 비교 연구". *Conference : 대한기계학회 CAE 및 응용역학부문 2025년 춘계학술대회, 2025-04-18*.
- 이승윤, 강윤혁, 이장현, 김민재, 김동구, 윤병동. "면압기반 전기자동차 배터리 상태 예측을 위한 센서 적용성 검증 및 데이터 기반 알고리즘 개발". *Conference : 대한기계학회 CAE 및 응용역학부문 2025년 춘계학술대회, 2025-04-17*.
- 유진오, 김태형, 이현찬, 하종문, 윤병동. "도메인 지식 기반 인공지능을 활용한 신호 처리 한계 극복: 회전 설비 고장 진단 응용". *Conference : 대한기계학회 CAE 및 응용역학부문 2025년 춘계학술대회, 2025-04-17*.
- 김민재, 김성종, 이승윤, 이지원, 윤헌준, 윤병동. "노이즈에 강건한 베어링 고장진단 모델 개발을 위한 규제 기법". *Conference : 대한기계학회 CAE 및 응용역학부문 2025년 춘계학술대회, 2025-04-17*.
- 김주현, 김용채, 권경륜, 송원빈, 윤병동. "스마트 제조의 초자율화: 딥러닝 기반 고장 예측 및 최적 후보군 탐색". *Conference : 대한기계학회 CAE 및 응용역학부문 2025년 춘계학술대회, 2025-04-17*.
- 양준호, 김형민, 채민석, 김한수, 이상경, 윤헌준, 윤병동. "미확보 모터 고장 종류 진단을 위한 시뮬레이션 응용 도메인 적응 모델". *Conference : 대한기계학회 CAE 및 응용역학부문 2025년 춘계학술대회, 2025-04-17*.
- 권경륜, 최현희, 이승윤, 김봉모, 김태진, 윤병동. "리튬이온배터리 상태 추정을 위한 전이학습 기반 물리정보 신경망". *Conference : 대한기계학회 신뢰성부문 2025년 춘계학술대회, 2025-04-11*.
- 김태형, 장홍석, 임주희, 김민정, 윤병동. "전류, 자속, 진동 신호 퓨전 기반 차량 휠 구동 모터 진단". *Conference : 대한기계학회 신뢰성부문 2025년 춘계학술대회, 2025-04-11*.
- 이지원, 이승윤, 김성종, 김민재, 윤헌준, 윤병동. "베어링 결함 진단을 위한 딥러닝 기반 시계열 데이터의 초해상도: 저성능 센서 한계 극복". *Conference : 대한기계학회 신뢰성부문 2025년 춘계학술대회, 2025-04-10*.
- 송원빈, 이규석, 윤병동. "딥러닝을 활용한 구조함수 기반 반도체 패키지 열특성 해석 모델 개발". *Conference : (사)한국마이크로전자 및 패키징학회 2025년 정기학술대회, 2025-04-03*.
- 송원빈, 이규석, 윤병동. "Enhancing Structure Functions for Accurate Thermal Characterization and Monitoring of Semiconductor Packages: Sampling Optimization and Geometric Analysis". *Conference : 제 32회 한국반도체 학술대회, 2025-02-13*.

**2024**

- Taehun Kim, Jin Uk Ko, Jinwook Lee, Yong Chae Kim, Joon Ha Jung\*, and Byeng D. Youn\*. "Spectrum-guided GAN with Density-Directionality Sampling: Diverse High-fidelity Signal Generation for Fault Diagnosis of Rotating Machinery". *Advanced Engineering Informatics, 2024-10, Vol. 62, pp. 102821 · DOI <https://doi.org/10.1016/j.aei.2024.102821>*.
- Yong Chae Kim, Jin Uk Ko, Jinwook Lee, Taehun Kim, Joon Ha Jung\*, and Byeng D. Youn\*. "Latent Space Alignment based Domain Adaptation (LSADA) for Fault Diagnosis of Rotating Machinery". *Advanced Engineering Informatics, 2024-10, Vol. 62, pp. 102862 · DOI <https://doi.org/10.1016/j.aei.2024.102862>*.
- Seungyun Lee, Sungjong Kim, Su J. Kim, Jiwon Lee, Heonjun Yoon\*, and Byeng D. Youn\*. "Revolution and Peak Discrepancy-Based Domain Alignment Method for Bearing Fault Diagnosis Under Very Low-Speed Conditions". *Expert Systems with Applications, 2024-10, Vol. 251, pp. 124084 · DOI <https://doi.org/10.1016/j.eswa.2024.124084>*.
- Yong Chae Kim, Jinwook Lee, Taehun Kim, Jonghwa Baek, Jin Uk Ko, Joon Ha Jung\*, and Byeng D. Youn\*. "Gradient Alignment Based Partial Domain Adaptation (GAPDA) Using a Domain Knowledge Filter for Fault Diagnosis of Bearing". *Reliability Engineering & System Safety, 2024-10, Vol. 250, pp. 110293 · DOI <https://doi.org/10.1016/j.ress.2024.110293>*.
- Semin Ahn¹, Jinoh Yoo¹, Kyu-Wha Lee, Byeng D. Youn\*, and Sung-Hoon Ahn\*. "Frequency-Focused Sound Data Generator for Fault Diagnosis in Industrial Robots". *Journal of Computational Design and Engineering, 2024-08, Vol. 11, No. 4, pp. 234-248 · DOI <https://doi.org/10.1093/jcde/qwae061>*.
- Minseok Chae, Hyeongmin Kim, Hye Jun Oh, Chan Hee Park, Chaehyun Suh, Heonjun Yoon\*, and Byeng D. Youn\*. "PCDC: Prototype-assisted Dual-contrastive Learning with Depthwise Separable Convolutional Neural Network for Few-shot Fault Diagnosis of Permanent Magnet Synchronous Motors under New Operating Conditions". *Journal of Computational Design and Engineering, 2024-06, Vol. 11, pp. 337-358 · DOI <https://doi.org/10.1093/jcde/qwae052>*.
- Jinwook Lee, Jin Uk Ko, Taehun Kim, Yong Chae Kim, Joon Ha Jung\*, and Byeng D. Youn\*. "Domain Adaptation with Label-Aligned Sampling (DALAS) for Cross-Domain Fault Diagnosis of Rotating Machinery under Class Imbalance". *Expert Systems with Applications, 2024-06, Vol. 243, pp. 122910 · DOI <https://doi.org/10.1016/j.eswa.2023.122910>*.
- Jinoh Yoo, Jongmin Park, Taehyung Kim, Jong Moon Ha\*, and Byeng D. Youn\*. "Weighted Multi-order Viterbi Algorithm (WMOVA): Instantaneous Angular Speed Estimation under Harsh Condition". *Mechanical Systems and Signal Processing, 2024-04, Vol. 211, pp. 111187 · DOI <https://doi.org/10.1016/j.ymssp.2024.111187>*.
- Kyumin Na, Yunhan Kim, Heonjun Yoon\*, and Byeng D. Youn\*. "FASER: Fault-affected Signal Energy Ratio for Fault Diagnosis of Gearboxes Under Repetitive Operating Conditions". *Expert Systems with Applications, 2024-03, Vol. 238, Part C, pp. 122078 · DOI <https://doi.org/10.1016/j.eswa.2023.122078>*.
- Sang Kyung Lee, Hyeongmin Kim, Minseok Chae, Hye Jun Oh, Heonjun Yoon, and Byeng D. Youn\*. "Self-supervised Feature Learning for Motor Fault Diagnosis under Various Torque Conditions". *Knowledge-based Systems, 2024-03, Vol. 288, pp. 111465 · DOI <https://doi.org/10.1016/j.knosys.2024.111465>*.
- Sina Masoumi Shahrbabak, Sooho Kim, Byeng D. Youn, Hao-Min Cheng, Chen-Huan Chen, Ramakrishna Mukkamala, and Jin-Oh Hahn\*. "Peripheral Artery Disease Diagnosis Based on Deep Learning-Enabled Analysis of Non-Invasive Arterial Pulse Waveforms". *Computers in Biology and Medicine, 2024-01, Vol. 168, pp. 107813 · DOI <https://doi.org/10.1016/j.compbiomed.2023.107813>[^biopad]*.
- Donghyu Lee, Soo-Ho Jo, and Byeng D. Youn. "Inverse Design of Defect-introduced Phononic Crystals via a Deep Learning Approach". *Conference : The 26th International Congress of Theoretical and Applied Mechanics, 2024-08-30*.
- Taehun Kim, Jin Uk Ko, Jinwook Lee, Yong Chae Kim, Byeng D. Youn, and Joon Ha Jung. "Synthetic Signal Generation Framework for Fault Diagnosis of Rotating Machinery with Limited Fault Data". *Conference : ASME 2024 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference, 2024-08-28*.
- Sungjong Kim, Seungyun Lee, Jiwon Lee, Minjae Kim, Heonjun Yoon, and Byeng D. Youn. "Multi-sensor Fusion Framework for Fault Diagnosis of Rotating Machinery based on Sensor Importance Estimation". *Conference : ASME 2024 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference, 2024-08-28*.
- Semin Ahn, Jinoh Yoo, Kyu-Wha Lee, Byeng Dong Youn, and Sung-Hoon Ahn. "Frequency-Focused Sound Data Generator for Fault Diagnosis in Industrial Robots". *Conference : International Conference on Precision Engineering and Sustainable Manufacturing (PRESM) 2024, 2024-07-09*.
- Hyeongmin Kim and Byeong D. Youn. "Window Size and Sampling Rate Selection for Cost-optimal Deep Learning-based Fault Diagnosis". *Conference : Asian Congress of Structural and Multidisciplinary Optimization (ACSMO) 2024, 2024-05-21*.
- Donghyue Lee, Soo-Ho Jo, and Byeng D. Youn. "Deep Learning-based Inverse Design Framework: A Case Study of a Defective Phononic Crystal for Narrowband Filtering". *Conference : Asian Congress of Structural and Multidisciplinary Optimization (ACSMO) 2024, 2024-05-21*.
- 김한수, 채민석, 이상경, 백종화, Sebastien Schwartz, Christian Gogu, 윤병동. "모터 시스템 고장 진단을 위한 차원 축소 기반 헬스 맵 개발". *Conference : 대한기계학회 2024년 학술대회, 2024-11-08*.
- 채민석, 김형민, 이상경, 김한수, 양준호, 윤헌준, 윤병동. "유도 전동기의 턴 간 단락 심각도 추정을 위한 물리 기반 심층 연산자 네트워크". *Conference : 대한기계학회 2024년 학술대회, 2024-11-08*.
- 이상경, 김형민, 채민석, 김한수, 양준호, 윤헌준, 윤병동. "모터 구동 시스템 고장 진단을 위한 그래프 기반 센서 융합 네트워크". *Conference : 대한기계학회 2024년 학술대회, 2024-11-08*.
- 백종화, 이진욱, 김태훈, 김용채, 김주현, 정준하, 윤병동. "비전 기반 모션 증폭 및 시간 대역 통과 필터를 활용한 회전체 시스템 이상탐지". *Conference : 대한기계학회 2024년 학술대회, 2024-11-08*.
- 김주현, 이진욱, 김태훈, 김용채, 백종화, 정준하, 윤병동. "회전체 진동 신호 디노이징을 위한 노이즈 추정 및 확산 모델 기반 복원 네트워크 개발". *Conference : 대한기계학회 2024년 학술대회, 2024-11-06*.
- 이승윤, 최현희, 이규석, 윤병동. "데이터 기반 전기자동차 리튬이온 배터리 열화 예측을 위한 면압 특성 개발". *Conference : 대한기계학회 2024년 학술대회, 2024-11-06*.
- 김형민, 이상욱, 이동휴, 윤병동. "연료전지 양극판의 원하는 형상 제작을 위한 인공지능 기반 역설계 방법". *Conference : 대한기계학회 2024년 학술대회, 2024-11-06*.
- 조수호, 이동휴, 윤병동. "복수의 목표 주파수 필터링을 위한 딥러닝 기반 메타구조 역설계". *Conference : 2024년도 추계 소음진동 학술대회, 2024-10-24*.
- 박종민, 유진오, 김태형, 박종혁, 김민정, 하종문, 윤병동. "고장주파수 대역 세분화 및 도메인 적응 기반 다양한 속도 조건에서의 베어링 고장 진단". *Conference : 한국PHM학회 2024년도 정기학술대회, 2024-06-26*.
- 최현희, 최용환, 윤병동, 이규석. "리튬이온 배터리 전기역학모델 순차적 최적화기반 파라미터 식별". *Conference : 한국PHM학회 2024년도 정기학술대회, 2024-06-26*.
- 백종화, 이진욱, 김태훈, 김용채, 김주현, 정준하, 윤병동. "비전 기반 모션 증폭 및 시간 대역 통과 필터를 활용한 회전체 시스템 고장 진단". *Conference : 한국PHM학회 2024년도 정기학술대회, 2024-06-26*.
- 김형민, 김태훈, 송원빈, 하종문, 윤병동. "도메인 지식과 인공지능의 결합을 통한 건전성 및 예측 관리 방법". *Conference : 한국PHM학회 2024년도 정기학술대회, 2024-06-25*.
- 이진욱, 김태훈, 김용채, 백종화, 김주현, 정준하, 윤병동. "회전체 시스템 고장 진단을 위한 이중 수준 가중치 기반의 다중 소스 도메인 적응 기법 개발". *Conference : 한국PHM학회 2024년도 정기학술대회, 2024-06-25*.
- 조수호, 이동휴, 윤병동. "협대역 투과를 위한 결함 인가 음향양자 결정: 딥러닝 기반 역설계 방법론 중심으로". *Conference : 2024년 한국소음진동공학회 춘계 소음진동 학술대회, 2024-05-23*.
- 송원빈, 이규석, 윤병동. "구조 함수를 이용한 IGBT 솔더 레이어 열화 국소화". *Conference : 대한기계학회 CAE 및 응용역학부문 2024년 춘계학술대회, 2024-05-03*.
- 김한수, 김형민, 채민석, 오혜준, 이상경, 윤헌준, 윤병동. "전류 신호의 고장 민감도 향상을 통한 Park's Vector Modulus 기반 모터 고장 감지". *Conference : 대한기계학회 CAE 및 응용역학부문 2024년 춘계학술대회, 2024-05-02*.
- 김용채, 김봉모, 김민정, 이상경, 정준하, 윤병동. "물리지식을 이용한 트랜스포머 기반 CNC 밀링머신의 공구 잔여 수명 예측". *Conference : 대한기계학회 CAE 및 응용역학부문 2024년 춘계학술대회, 2024-05-02*.
- 김형민, 김태훈, 송원빈, 하종문, 윤병동. "PHM 분야에서의 도메인 지식 기반 신경망 활용 사례". *Conference : 대한기계학회 CAE 및 응용역학부문 2024년 춘계학술대회, 2024-05-02*.
- 김봉모, 최현희, 김용채, 권경륜, 김태진, 윤병동. "배터리 부분 충전 곡선의 현재 충전 상태 불변 특성을 활용한 배터리 용량 추정". *Conference : 대한기계학회 CAE 및 응용역학부문 2024년 춘계학술대회, 2024-05-02*.
- 김형민, 채민석, 오혜준, 이상경, 김한수, 윤헌준, 윤병동. "학습하지 않은 고장 감지를 위한 불확실성 고려 딥러닝 고장 진단 방법". *Conference : 대한기계학회 CAE 및 응용역학부문 2024년 춘계학술대회, 2024-05-02*.
- 김태훈, 이진욱, 김용채, 백종화, 김주현, 윤병동, 정준하. "부족한 고장 신호 데이터 조건에서 품질 및 다양성이 개선된 딥러닝 기반 생성 모델". *Conference : 대한기계학회 신뢰성부문 2024년 춘계학술대회, 2024-03-21*.

**2023**

- Hyunhee Choi, Chen Jiang, Byeng D. Youn\*, and Taejin Kim\*. "Uncertainty Analysis of Stack Pressure in EV Battery Module System Using a Phenomenological Modeling Approach". *Journal of Energy Storage, 2023-12, Vol. 73, Part A, pp. 108948 · DOI <https://doi.org/10.1016/j.est.2023.108948>*.
- Haichao An, Byeng D. Youn\*, and Heung Soo Kim\*. "Variable-Stiffness Composite Optimization Using Dynamic and Exponential Multi-Fidelity Surrogate Models". *International Journal of Mechanical Sciences, 2023-11, Vol. 257, pp. 108547 · DOI <https://doi.org/10.1016/j.ijmecsci.2023.108547>*.
- Hyeongmin Kim, Chan Hee Park, Chaehyun Suh, Minseok Chae, Hye Jun Oh, Heonjun Yoon\*, and Byeng D. Youn\*. "Stator Current Operation Compensation (SCOC): A Novel Preprocessing Method for Deep Learning-based Fault Diagnosis of Permanent Magnet Synchronous Motors Under Variable Operating Conditions". *Measurement, 2023-11, Vol. 221, pp. 113446 · DOI <https://doi.org/10.1016/j.measurement.2023.113446>*.
- Jin Uk Ko, Jinwook Lee, Taehun Kim, Yong Chae Kim, and Byeng D. Youn\*. "Frequency-learning Generative Network (FLGN) to Generate Vibration Signals of Variable Lengths". *Expert Systems with Applications, 2023-10, Vol. 227, pp. 120255 · DOI <https://doi.org/10.1016/j.eswa.2023.120255>*.
- Donghyu Lee, Byeng D. Youn\*, and Soo-Ho Jo\*. "Deep-learning-based Framework for Inverse Design of a Defective Phononic Crystal for Narrowband Filtering". *International Journal of Mechanical Sciences, 2023-10, Vol. 255, pp. 108474 · DOI <https://doi.org/10.1016/j.ijmecsci.2023.108474>*.
- Hyunhee Choi, Hyejeong Son, Yong Hwan Choi, Byeng D. Youn\*, and Guesuk Lee\*. "Reliability-Based Design Optimization of a Pouch Battery Module Using Gaussian Process Modeling in the Presence of Cell Swelling". *Structural and Multidisciplinary Optimization, 2023-10, Vol. 66, pp. 227 · DOI <https://doi.org/10.1007/s00158-023-03662-1>*.
- Soo-Ho Jo\*, Donghyu Lee, and Byeng D. Youn. "Defect-band Splitting of a One-dimensional Phononic Crystal with Double Defects for Bending Wave Excitation". *Mathematics, 2023-09, Vol. 11, No. 18, pp. 3852 · DOI <https://doi.org/10.3390/math11183852>*.
- Jongmin Park, Jinoh Yoo, Taehyung Kim, Jong M. Ha\*, and Byeng D. Youn\*. "Multi-head De-noising Autoencoder Based Multitask (MDAM) Model for Fault Diagnosis of Rolling Element Bearings under Various Speed Conditions". *Journal of Computational Design and Engineering, 2023-08, Vol 10, No. 4, pp 1804-1820 · DOI <https://doi.org/10.1093/jcde/qwad076>*.
- Taewan Hwang, Jong M. Ha\*, and Byeng D. Youn\*. "Robust Deep Learning-based Fault Detection of Planetary Gearbox Using Enhanced Health Data Map under Domain Shift Problem". *Journal of Computational Design and Engineering, 2023-08, Vol. 10, No. 4, pp. 1677-1693 · DOI <https://doi.org/10.1093/jcde/qwad056>*.
- Hye Jun Oh, Jinoh Yoo, Sang Kyung Lee, Minseok Chae, Jongmin Park, and Byeng D. Youn\*. "A Hybrid Approach Combining Data-Driven and Signal-Processing- Based Methods for Fault Diagnosis of a Hydraulic Rock Drill". *International Journal of Prognostics and Health Management, 2023-07, Vol. 14. No. 1, pp. 1-11 · DOI <https://doi.org/10.36001/ijphm.2023.v14i1.3458>*.
- Chao Hu, Kai Goebel, David Howey, Zhike Peng, Dong Wang, Peng Wang, and Byeng D. Youn. "Editorial: Special issue on Physics-informed Machine learning Enabling Fault Feature Extraction and Robust Failure Prognosis". *Mechanical Systems and Signal Processing, 2023-06, Vol. 192, pp. 110219 · DOI <https://doi.org/10.1016/j.ymssp.2023.110219>*.
- Hyeonchan Lee, Wongon Kim\*, Hyejeong Son, Hyunhee Choi, Soo-Ho Jo, and Byeng D. Youn\*. "A New Initial Point Search Algorithm for Bayesian Calibration with Insufficient Statistical Information: Greedy Stochastic Section Search". *Structural and Multidisciplinary Optimization, 2023-06, Vol. 66, pp. 124 · DOI <https://doi.org/10.1007/s00158-023-03577-x>*.
- Hyeongmin Kim, Jin Uk Ko, Kyumin Na, Hyeonchan Lee, Hee-soo Kim, Jong-duk Son, Heonjun Yoon\*, and Byeng D. Youn\*. "Opt-TCAE: Optimal Temporal Convolutional Auto-encoder for Boiler Tube Leakage Detection in a Thermal Power Plant Using Multi-sensor Data". *Expert Systems with Applications, 2023-04, Vol. 215, pp. 119377 · DOI <https://doi.org/10.1016/j.eswa.2022.119377>*.
- Jin Uk Ko, Jinwook Lee, Taehun Kim, Yong Chae Kim, and Byeng D. Youn\*. "Deep-learning-based Fault Detection and Recipe Optimization for a Plastic Injection Molding Process under the Class Imbalance Problem". *Journal of Computational Design and Engineering, 2023-04, Vol. 10, No. 2, pp. 694-710 · DOI <https://doi.org/10.1093/jcde/qwad011>*.
- Hyeongmin Kim, Chan Hee Park, Chaehyun Suh, Minseok Chae, Heonjun Yoon\*, and Byeng D. Youn\*. "MPARN: Multi-scale Path Attention Residual Network for Fault Diagnosis of Rotating Machines". *Journal of Computational Design and Engineering, 2023-04, Vol. 10, No. 2, pp. 860-872 · DOI <https://doi.org/10.1093/jcde/qwad031>*.
- Jin-gyun Park, Heonjun Yoon\*, and Byeng D. Youn\*. "Probabilistic Framework for Reliable Optimal Design of Gearboxes in General-purpose Industrial Robots Considering Random Use Conditions". *Journal of Computational Design and Engineering, 2023-04, Vol. 10, No. 2, pp. 539-548 · DOI <https://doi.org/10.1093/jcde/qwad007>*.
- Sehui Jeong, Hyunhee Choi, Byeng D. Youn\*, and Hyejeong Son\*. "Statistical Prior Modeling with Radius-Uniform Distribution for a Correlation Hyperparameter in Bayesian Calibration". *Structural and Multidisciplinary Optimization, 2023-04, Vol. 66, No. 4, pp. 69 · DOI <https://doi.org/10.1007/s00158-023-03520-0>*.
- Soo-Ho Jo\*, Donghyu Lee, Heonjun Yoon, and Byeng D. Youn. "Double Piezoelectric Defects in Phononic Crystals for Ultrasonic Transducers". *Journal of Physics D-Applied Physics, 2023-02, Vol 56, No 7, pp 074002 · DOI <https://doi.org/10.1088/1361-6463/acb21a>*.
- Kyumin Na, Heonjun Yoon\*, Jaedong Kim, Sungjong Kim, and Byeng D.Youn\*. "PERL: Probabilistic Energy-ratio-based Localization for Boiler Tube Leaks Using Descriptors of Acoustic Emission Signals". *Reliability Engineering & System Safety, 2023-02, Vol 230, pp 108923 · DOI <https://doi.org/10.1016/j.ress.2022.108923>*.
- Soo-Ho Jo and Byeng D. Youn\*. "Longitudinal Wave Localization Using a One-dimensional Phononic Crystal with Differently Patterned Double Defects". *International Journal of Mechanical Sciences, 2023-01, Vol. 237, pp. 107783 · DOI <https://doi.org/10.1016/j.ijmecsci.2022.107783>*.
- Keunsu Kim, Heonjun Yoon\*, and Byeng D. Youn\*. "A Noise-robust Feature Extraction Method for Rolling Element Bearing Diagnosis: Linear Power-Normalized Cepstral Coefficients (LPNCC)". *International Journal of Precision Engineering and Manufacturing-Green Technology, 2023-01, Vol. 10, pp. 217-232 · DOI <https://doi.org/10.1007/s40684-022-00448-6>*.
- Adam Thelen, Xiaoge Zhang, Olga Fink, Yan Lu, Sayan Ghosh, Byeng D. Youn, Michael D. Todd, Sankaran Mahadevan, Chao Hu\*, and Zhen Hu\*. "A Comprehensive Review of Digital Twin - Part 2: Roles of Uncertainty Quantification and Optimization, a Battery Digital Twin, and Perspectives". *Structural and Multidisciplinary Optimization, 2023-01, Vol. 66, pp. 1 · DOI <https://doi.org/10.1007/s00158-022-03410-x>*.
- Donghyu Lee, Yong Chae Kim, Gyeong Ryun Gwon, and Byeng D. Youn. "AI-Driven Diagnosis of Aircraft Anomalies using Flight Data Correlation Errors". *Conference : 14th International Symposium on NDT in Aerospace, 2023-11-08*.
- Yong Chae Kim, Jin Uk Ko, Jinwook Lee, Taehun Kim, Joon Ha Jung, and Byeng D. Youn. "Sequential Domain Adaptation for Fault Diagnosis in Rotating Machinery". *Conference : Asia Pacific Conference of the Prognostics and Health Management Society 2023, 2023-09-14*.
- Sang Kyung Lee, Jiwon Lee, Seungyun Lee, Bongmo Kim, Yong Chae Kim, Jinwook Lee, and Byeng D. Youn. "Hybrid Approach of XGBoost and Rule-based Model for Fault Detection and Severity Estimation in Spacecraft Propulsion System". *Conference : Asia Pacific Conference of the Prognostics and Health Management Society 2023, 2023-09-13*.
- Jinoh Yoo, Jongmin Park, Taehyung Kim, Jong M. Ha, and Byeng D. Youn. "Tacholess Instantaneous Speed Estimation Considering the Characteristics of Vibration Harmonics". *Conference : Asia Pacific Conference of the Prognostics and Health Management Society 2023, 2023-09-13*.
- Seungyun Lee, Sungjong Kim, Jiwon Lee, Su J. Kim, Heonjun Yoon, and Byeng D. Youn. "A Quantitative Analysis of Domain Discrepancies Between General- Speed and Very Low-Speed Bearings and Its Applications to Fault Diagnosis of Very Low-Speed Bearings Using Transfer Learning". *Conference : Asia Pacific Conference of the Prognostics and Health Management Society 2023, 2023-09-12*.
- Hyeongmin Kim, Kyumin Na, Jin Uk Ko, Heonjun Yoon, and Byeng D. Youn. "Convolutional Auto-Encoder Based Boiler Tube Leakage Detection Method in a Thermal Power Plant". *Conference : ASME 2023 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference, 2023-08-23*.
- Minseok Chae, Hyeongmin Kim, Hye Jun Oh, Chan Hee Park, Heonjun Yoon, and Byeng D. Youn. "Few-Shot Learning Method for Fault Diagnosis of Permanent Magnet Synchronous Motors Under New Operating Conditions". *Conference : ASME 2023 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference, 2023-08-23*.
- Jinwook Lee, Myungyon Kim, Jin Uk Ko, Joon Ha Jung, Kyung Ho Sun, and Byeng D. Youn. "Multi-Level Domain Adaptation Network Based Fault Diagnosis of Rotating Machinery". *Conference : ASME 2023 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference, 2023-08-23*.
- Yong Chae Kim, Seungyun Lee, Sang Kyung Lee, Bongmo Kim, Jiwon Lee, Jinwook Lee, and Byeng D. Youn. "Inter-class Metric Learning based Depth-wise Convolutional Neural Network for Gear Fault Diagnosis". *Conference : 2023 IEEE Conference on Prognostics and Health Management, 2023-06-06*.
- Donghyu Lee, Byeng D. Youn and Soo-Ho Jo. "Deep Learning-based Design Methodology of a Phononic Crystal with a Defect for Narrow Bandpass Filtering". *Conference : 15th World Congress of Structural and Multidisciplinary Optimization, 2023-06-05*.
- Hyunhee Choi, Chen Jiang, Taejin Kim, and Byeng D. Youn. "Statistical Stack Pressure Estimation in Module Level Using Phenomenological Swelling Model". *Conference : 15th World Congress of Structural and Multidisciplinary Optimization, 2023-06-05*.
- 김성종, 유장현, 안성훈, 윤병동. "가공 경로를 고려한 오토인코더 기반 CNC 밀링 공구 이상 조기 감지". *Conference : 한국정밀공학회 2023추계학술대회, 2023-11-17*.
- 채민석, 이상욱, Christian Brecher, 윤병동. "공구 형상을 고려한 대용량 바이폴라 플레이트 성형 공정의 공구 마모 예측 방법". *Conference : 한국정밀공학회 2023추계학술대회, 2023-11-17*.
- 이지원, 이승윤, 김성종, 김민재, 윤헌준, 윤병동. "부분 회전 조건 아래 선회 베어링 고장 진단을 위한 신호 확장 기법". *Conference : 대한기계학회 2023년 학술대회, 2023-11-03*.
- 김민정, 박종민, 유진오, 김태형, 하종문, 윤병동. "변속 조건 아래 비지도 도메인 적응 기반 기어박스 속도 추정 기법". *Conference : 대한기계학회 2023년 학술대회, 2023-11-03*.
- 김용채, 이진욱, 김태훈, 백종화, 고진욱, 정준하, 윤병동. "베어링 고장 진단을 위한 인벨롭 필터 기반의 부분 전이 학습 기법". *Conference : 대한기계학회 2023년 학술대회, 2023-11-03*.
- 이상경, 김형민, 채민석, 오혜준, 윤헌준, 윤병동. "모터 고장 진단을 위한 신호처리 기반 자기지도 학습 기법". *Conference : 대한기계학회 2023년 학술대회, 2023-11-03*.
- 이승윤, 최현희, 김봉모, 이규석, 윤병동. "면압을 고려한 지식 증류 기반 파우치 셀 수명 예측". *Conference : 대한기계학회 2023년 학술대회, 2023-11-03*.
- 송원빈, 이규석, 윤병동. "IGBT 모듈 접합계면 하단 솔더 파괴거동에 따른 접합온도 연구". *Conference : 대한기계학회 2023년 학술대회, 2023-11-03*.
- 이동휴, 김태훈, 윤병동, 조수호. "이중 결함 인가 음향양자 결정의 딥러닝 기반 역설계". *Conference : 대한기계학회 2023년 학술대회, 2023-11-01*.
- 백종화, 이진욱, 김태훈, 김용채, 정준하, 윤병동. "컴퓨터 비전 기반의 고장진단 수행으로 군 장비 운영유지비용 절감방안". *Conference : 제 16회 육군 M&S 국제학술대회, 2023-10-31*.
- 오혜준, 김형민, 유진오, 김태형, 김민정, 윤병동. "기어박스 고장진단을 위한 다변량 어텐션 멀티 커널 합성곱 신경망". *Conference : 한국PHM학회 2023년도 정기학술대회, 2023-07-04*.
- 김용채, 이승윤, 이상경, 김봉모, 이지원, 이진욱, 윤병동. "실시간 신호에 대한 메트릭 러닝 기반 기어 결함 진단". *Conference : 한국 PHM학회 2023년도 정기학술대회, 2023-07-04*.
- 나규민, 윤병동. "비정상 운행 조건 하 고장 진단을 위한 스펙트로그램 표현 에너지의 확률적 모델링". *Conference : 한국 PHM학회 2023년도 정기학술대회, 2023-07-04*.
- 김건, 나규민, 이진욱, 유진오, 윤병동. "건설장비 기어박스 진단을 위한 회전 속도 추정 방법 개발". *Conference : 한국자동차공학회 춘계학술대회, 2023-05-24*.
- 최현희, Chen Jiang, 윤병동, 김태진. "현상학적 모델링 접근방식을 통한 EV 배터리 모듈 시스템의 면압 불확실성 해석". *Conference : 대한기계학회 CAE 및 응용역학부문 2023년 춘계학술대회, 2023-05-19*.
- 김형민, 윤병동. "최적 가공을 위한 강화학습 기반 서보 모터 베어 파라미터 튜닝 방법". *Conference : 대한기계학회 CAE 및 응용역학부문 2023년 춘계학술대회, 2023-05-19*.
- Chen Jiang, 최현희, 윤병동. "Physics-informed Gaussian Process Probailistic Modeling with Multi-source Data for Prognostics of Degradation Processes". *Conference : 대한기계학회 CAE 및 응용역학부문 2023년 춘계학술대회, 2023-05-19*.
- 김태형, 유진오, 박종민, 김민정, 하종문, 윤병동. "신호 내 샘플 간 위상 대응을 통한 회전체 고장 진단". *Conference : 대한기계학회 CAE 및 응용역학부문 2023년 춘계학술대회, 2023-05-18*.
- 박종민, 유진오, 김태형, 김민정, 하종문, 윤병동. "주파수 대역 필터 기반 어텐션 네트워크 활용 다양한 속도에서의 구름 베어링 진단 기법 개발". *Conference : 대한기계학회 CAE 및 응용역학부문 2023년 춘계학술대회, 2023-05-18*.
- 김태훈, 고진욱, 이진욱, 김용채, 백종화, 정준하, 윤병동. "제한된 데이터 조건 하에서 고장 진단 성능 향상을 위한 적대적 생성 네트워크 개선 기법". *Conference : 대한기계학회 CAE 및 응용역학부문 2023년 춘계학술대회, 2023-05-18*.
- 오혜준, 김형민, 채민석, 이상경, 윤병동, 윤헌준. "전류 기반 모터 고장 진단 성능 향상을 위한 교차 모달 지식 증류 기법". *Conference : 대한기계학회 CAE 및 응용역학부문 2023년 춘계학술대회, 2023-05-18*.
- 이상경, 김형민, 채민석, 오혜준, 윤헌준, 윤병동. "자기지도 학습을 통한 제한된 레이블 데이터에서 모터 고장진단". *Conference : 대한기계학회 CAE 및 응용역학부문 2023년 춘계학술대회, 2023-05-18*.
- 이동휴, 윤병동, 조수호. "목표 주파수 정합 및 투과율 극대화를 위한 결함 인가 음향양자 결정의 딥러닝 기반 역설계". *Conference : 대한기계학회 CAE 및 응용역학부문 2023년 춘계학술대회, 2023-05-18*.
- 김봉모, 최현희, 김태진, 윤병동. "리튬이온 배터리의 건전성 추정을 위한 증분용량 분석 데이터 피쳐 엔지니어링". *Conference : 대한기계학회 CAE 및 응용역학부문 2023년 춘계학술대회, 2023-05-18*.
- 이진욱, 고진욱, 김태훈, 김용채, 백종화, 정준하, 윤병동. "데이터 불균형 조건에서 회전 기계의 교차 도메인 간 고장 진단 연구". *Conference : 대한기계학회 CAE 및 응용역학부문 2023년 춘계학술대회, 2023-05-18*.
- 채민석, 김형민, 오혜준, 박찬희, 서채현, 윤헌준, 윤병동. "다양한 운행조건에서 영구자석 동기모터의 미학습 고장 진단을 위한 퓨샷 학습 방법". *Conference : 대한기계학회 CAE 및 응용역학부문 2023년 춘계학술대회, 2023-05-18*.
- 김성종, 유장현, 윤병동, 안성훈. "나노물질 기반 저가형 진동 센서를 활용한 딥러닝 CNC 공구 수명 예측". *Conference : 대한기계학회 CAE 및 응용역학부문 2023년 춘계학술대회, 2023-05-18*.
- 유진오, 박종민, 김태형, 김민정, 하종문, 윤병동. "극한 운행 조건 하 진동 신호 기반 센서리스 순간 속도 추정". *Conference : 대한기계학회 CAE 및 응용역학부문 2023년 춘계학술대회, 2023-05-18*.
- 김용채, 김태훈, 고진욱, 이진욱, 김건, 윤병동. "가변 운행 조건 하에서 유압식 착암기 진단을 위한 다중 소스 도메인 적응 기법". *Conference : 대한기계학회 CAE 및 응용역학부문 2023년 춘계학술대회, 2023-05-18*.
- 이승윤, 김성종, 이지원, 김수지, 윤헌준, 윤병동. "알고리즘 공정성을 고려한 다양한 하중 조건에서의 베어링 고장 진단 기법". *Conference : 대한기계학회 CAE 및 응용역학부문 2023년 춘계학술대회, 2023-05-18*.
- 오혜준, 윤병동, 유진오, 이상경, 채민석, 박종민. "유압식 암반 드릴의 고장진단을 위한 데이터 기반 및 신호처리 기반의 하이브리드 기법". *Conference : 한국정밀공학회 2023춘계학술대회, 2023-05-11*.

**2022**

- Wongon Kim, Sunuwe Kim, Jingyo Jeong, Hyunjae Kim, Hyunchan Lee, and Byeng D. Youn\*. "Digital Twin Approach for On-Load Tap Changers Using Data-driven Dynamic Model Updating and Optimization-based Operating Condition Estimation". *Mechanical Systems and Signal Processing, 2022-12, Vol. 181, pp. 109471 · DOI <https://doi.org/10.1016/j.ymssp.2022.109471>*.
- Boseong Seo, Jaekyung Shin, Taejin Kim\*, and Byeng D. Youn\*. "Missing Data Imputation Using an Iterative Denoising Autoencoder (IDAE) for Dissolved Gas Analysis". *Electric Power Systems Research, 2022-11, Vol. 212, pp. 108642 · DOI <https://doi.org/10.1016/j.epsr.2022.108642>*.
- Haichao An, Byeng D. Youn\*, and Heung Soo Kim\*. "Optimal Placement of Non-redundant Sensors for Structural Health Monitoring under Model Uncertainty and Measurement Noise". *Measurement, 2022-11, Vol. 204, pp. 112102 · DOI <https://doi.org/10.1016/j.measurement.2022.112102>*.
- Adam Thelen, Xiaoge Zhang, Olga Fink, Yan Lu, Sayan Ghosh, Byeng D.Youn, Michael D. Todd, Sankaran Mahadevan, Chao Hu\*, and Zhen Hu\*. "A Comprehensive Review of Digital Twin - Part 1: Modeling and Twinning Enabling Technologies". *Structural and Multidisciplinary Optimization, 2022-11, Vol. 65, pp. 354 · DOI <https://doi.org/10.1007/s00158-022-03425-4>*.
- Chan Hee Park, Hyeongmin Kim, Chaehyun Suh, Minseok Chae, Heonjun Yoon\*, and Byeng D. Youn\*. "A Health Image for Deep Learning-based Fault Diagnosis of a Permanent Magnet Synchronous Motor Under Variable Operating Conditions: Instantaneous Current Residual Map". *Reliability Engineering & System Safety, 2022-10, Vol. 226, pp. 108715 · DOI <https://doi.org/10.1016/j.ress.2022.108715>*.
- Wongon Kim, Guesuk Lee\*, Hyejeong Son, Hyunhee Choi, and Byeng D. Youn\*. "Estimation of Fatigue Crack Initiation and Growth in Engineering Product Development using a Digital Twin Approach". *Reliability Engineering & System Safety, 2022-10, Vol. 226, pp. 108721 · DOI <https://doi.org/10.1016/j.ress.2022.108721>*.
- Yeongtak Oh, Yunhan Kim, Kyumin Na, and Byeng D. Youn\*. "A Deep Transferable Motion-Adaptive Fault Detection Method for Industrial Robots Using a Residual-Convolutional Neural Network". *ISA Transactions, 2022-09, Vol. 128, pp. 521-534 · DOI <https://doi.org/10.1016/j.isatra.2021.11.019>*.
- Izaz Raouf, Hyewon Lee, Yeong Rim Noh, Byeng D. Youn, and Heung Soo Kim\*. "Prognostic Health Management of the Robotic Strain Wave Gear Reducer Based on Variable Speed of Operation: A Data-Driven via Deep Learning Approach". *Journal of Computational Design and Engineering, 2022-09, Vol. 9, No. 5, pp. 1775-1788 · DOI <https://doi.org/10.1093/jcde/qwac091>*.
- Su J. Kim, Sungjong Kim, Seungyun Lee, Byeng D. Youn\*, and Taejin Kim\*. "Effective Band-selection Algorithm for Rolling Element Bearing Diagnosis Using AE Sensor Data under Noisy Conditions". *Structural and Multidisciplinary Optimization, 2022-09, Vol. 65, pp. 275 · DOI <https://doi.org/10.1007/s00158-022-03360-4>*.
- Soo-Ho Jo\* and Byeng D. Youn\*. "Enhanced Ultrasonic Wave Generation Using Energy-localized Behaviors of Phononic Crystals". *International Journal of Mechanical Sciences, 2022-08, Vol. 228, pp. 107483 · DOI <https://doi.org/10.1016/j.ijmecsci.2022.107483>*.
- Soo-Ho Jo¹, Heonjun Yoon¹, Yong Chang Shin, Wonjae Choi, Byeng D.Youn\*, and Miso Kim\*. "L-shape Triple Defects in a Phononic Crystal for Broadband Piezoelectric Energy Harvesting". *Nano Convergence, 2022-06, Vol. 9, pp. 29 · DOI <https://doi.org/10.1186/s40580-022-00321-x>*.
- Yong Chang Shin, Soo-Ho Jo, Heonjun Yoon\*, and Byeng D. Youn\*. "Design Principle for Effective Mechanical Boundary Using a Resonance Band Gap under Elastic Waves". *Journal of Computational Design and Engineering, 2022-04, Vol. 9, No. 2, pp. 772-782 · DOI <https://doi.org/10.1093/jcde/qwac026>*.
- Su J. Kim, Keunsu Kim, Taewan Hwang, Jongmin Park, Hwayong Jeong, Taejin Kim\*, and Byeng D. Youn\*. "Motor-current-based Electromagnetic Interference De-noising Method for Rolling Element Bearing Diagnosis Using Acoustic Emission Sensor". *Measurement, 2022-04, Vol. 193, pp. 110912 · DOI <https://doi.org/10.1016/j.measurement.2022.110912>*.
- Jin Uk Ko, Kyumin Na, Joon-Seok Oh, Jaedong Kim, and Byeng D. Youn\*. "A New Auto-encoder-based Dynamic Threshold to Reduce False Alarm Rates for Anomaly Detection of Steam Turbines". *Expert Systems with Applications, 2022-03, Vol. 189, pp. 116094 · DOI <https://doi.org/10.1016/j.eswa.2021.116094>*.
- Yunhan Kim, Kyumin Na, and Byeng D. Youn\*. "A Health-adaptive Time-Scale Representation (HTSR) Embedded Convolutional Neural Network for Gearbox Fault Diagnostics". *Mechanical Systems and Signal Processing, 2022-03, Vol. 167, pp. 108575 · DOI <https://doi.org/10.1016/j.ymssp.2021.108575>*.
- Jungho Park, Yunhan Kim, Kyumin Na, Byeng D. Youn\*, Yuejian Chen, Ming J. Zuo\*, and Yong-Chae Bae. "An Image-based Feature Extraction Method for Fault Diagnosis of Variable-speed Rotating Machinery". *Mechanical Systems and Signal Processing, 2022-03, Vol. 167, pp. 108524 · DOI <https://doi.org/10.1016/j.ymssp.2021.108524>*.
- Haichao An, Byeng D. Youn\*, and Heung Soo Kim\*. "Optimal Sensor Placement Considering Both Sensor Fault under Uncertainty and Sensor Clustering for Vibration-Based Damage Detection". *Structural and Multidisciplinary Optimization, 2022-03, Vol. 65, pp. 102 · DOI <https://doi.org/10.1007/s00158-021-03159-9>*.
- Soo-Ho Jo, Heonjun Yoon\*, Yong Chang Shin, and Byeng D. Youn\*. "Revealing Defect-mode-enabled Energy Localization Mechanisms of a One-dimensional Phononic Crystal". *International Journal of Mechanical Sciences, 2022-02, Vol. 215, pp. 106950 · DOI <https://doi.org/10.1016/j.ijmecsci.2021.106950>*.
- Jinwook Lee, Myungyon Kim, Jin Uk Ko, Joon Ha Jung, Kyung Ho Sun, and Byeng D. Youn\*. "Asymmetric Inter-Intra Domain Alignments (AIIDA) Method for Intelligent Fault Diagnosis of Rotating Machinery". *Reliability Engineering & System Safety, 2022-02, Vol. 218, pp. 108186 · DOI <https://doi.org/10.1016/j.ress.2021.108186>*.
- Hyejeong Son, Hyunhee Choi, Wongon Kim, Byeng D. Youn\*, and Guesuk Lee\*. "A Comparative Study of Statistical Validation Metrics with Consideration of Variance to Address Type II Errors in Statistical Model Validation". *Structural and Multidisciplinary Optimization, 2022-02, Vol. 65, pp. 63 · DOI <https://doi.org/10.1007/s00158-021-03127-3>*.
- Haichao An, Byeng D. Youn\*, and Heung Soo Kim\*. "A Methodology for Sensor Number and Placement Optimization for Vibration-Based Damage Detection of Composite Structures under Model Uncertainty". *Composite Structures, 2022-01, Vol. 279, pp. 114863 · DOI <https://doi.org/10.1016/j.compstruct.2021.114863>*.
- Hye Jun Oh, Jinoh Yoo, Sang Kyung Lee, Minseok Chae, Jongmin Park, and Byeng D. Youn. "A Hybrid Approach of Data-Driven and Signal Processing-Based Methods for Fault Diagnosis of Hydraulic Rock Drill". *Conference : Annual Conference of the Prognostics and Health Management Society 2022, 2022-11-03*.
- Jin Uk Ko, Kyumin Na, and Byeng D. Youn. "Anomaly Detection of a Steam Turbine by a Novel Auto-Encoder-Based Dynamic Threshold". *Conference : ASME 2022 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference, 2022-08-16*.
- Su J. Kim, Sungjong Kim, Seungyun Lee, Taejin Kim, and Byeng D. Youn. "Noise Robust Frequency Band Selection for Bearing Diagnosis using Acoustic Emission Signals". *Conference : ASME 2022 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference, 2022-08-16*.
- Hyeongmin Kim, Chan Hee Park, Chaehyun Suh, Minseok Chae, Heonjun Yoon, and Byeng D. Youn. "A Multi-scale Residual Network with Attention Mechanism for Fault Diagnosis of Rotating Machines". *Conference : ASME 2022 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference, 2022-08-15*.
- Haichao An, Heung Soo Kim, and Byeng D. Youn. "Adaptive Multi-Fidelity Surrogate Model Assisted by Gaussian Process Regression for Design Optimization of Variable Stiffness Composites with Fiber Steering Constraints". *Conference : 15th World Congress on Computational Mechanics & 8th Asian Pacific Congress on Computational Mechanics, 2022-08-05*.
- Hyunhee Choi and Byeng D. Youn. "Statistical Prediction of Stack Pressure Using Phenomenological Swelling Effect Model in Li-Ion Pouch Battery Module". *Conference : 15th World Congress on Computational Mechanics & 8th Asian Pacific Congress on Computational Mechanics, 2022-08-05*.
- Wongon Kim and Byeng D. Youn. "Stochastic Physics-based Model Updating for Fatigue Crack Detection in Riveted Lap Joints Using Lamb Waves". *Conference : 15th World Congress on Computational Mechanics & 8th Asian Pacific Congress on Computational Mechanics, 2022-08-05*.
- Sungjong Kim, Seungyun Lee, Su J. Kim, Jiwon Lee, Heonjun Yoon, and Byeng D. Youn. "Attention Based Multi-sensor Bearing Fault Diagnosis Considering Fault Relevance". *Conference : International Conference on Energy, Aquatech and Sustainability 2022, 2022-08-04*.
- Hyeongmin Kim, Maximilian Kosel, and Byeng D. Youn. "Reinforcement Learning-based Optimal Parameter Estimation of Ultra Precision Machine". *Conference : International Conference on Energy, Aquatech and Sustainability 2022, 2022-08-04*.
- Wongon Kim and Byeng D. Youn. "Stochastic Physics-based Model Updating Using Lamb Waves for Fatigue Crack Detection in Riveted Lap Joints". *Conference : International Conference on Precision Engineering and Sustainable Manufacturing 2022, 2022-07-21*.
- Minseok Chae, Wongon Kim, and Byeng D. Youn. "A Data-driven Molding Process Optimization Considering Important Features Related to Molding Quality and Efficiency". *Conference : Asian Congress of Structural and Multidisciplinary Optimization 2022, 2022-05-24*.
- Haichao An, Byeng D. Youn, and Heung Soo Kim. "A Methodology of Optimal Sensor Placement for Structural Health Monitoring Considering Information Redundancy, Model Uncertainty and Measurement Noise". *Conference : Asian Congress of Structural and Multidisciplinary Optimization 2022, 2022-05-24*.
- 이규석, 최현희, 최용환, 윤병동. "전기자동차용 파우치형 배터리 모듈에 대한 신뢰성 기반 최적 설계". *Conference : 2022 한국신뢰성학회 춘계학술대회, 2022-07-08*.
- 김태훈, 고진욱, 이진욱, 김용채, 윤병동. "적대적 생성 모델의 잠재공간 분석 기반 회전체 시스템의 다양한 신호 생성". *Conference : 한국PHM학회 2022년도 정기학술대회, 2022-07-01*.
- 김형민, 김태형, 윤병동. "이상 감지를 위한 재귀 신경망 기반 로봇 전류 신호 모델링". *Conference : 한국PHM학회 2022년도 정기학술대회, 2022-07-01*.
- 채민석, 김원곤, 윤병동. "사출 성형 작업의 성형 품질 관련 중요 인자를 고려한 데이터 기반 공학적 의사 결정 방법". *Conference : 한국PHM학회 2022년도 정기학술대회, 2022-07-01*.
- 오혜준, 김형민, 채민석, 서채현, 박찬희, 윤헌준, 윤병동. "다양한 토크 조건에서 모터 고장 진단을 위한 향상된 다중 소스 도메인 적응 기법". *Conference : 한국PHM학회 2022년도 정기학술대회, 2022-07-01*.
- 이진욱, 고진욱, 김태훈, 김용채, 윤병동. "회전체 시스템 고장 진단을 위한 샘플링 기반 비지도 도메인 적응 기법 개발". *Conference : 한국PHM학회 2022년도 정기학술대회, 2022-06-30*.
- 김건, 나규민, 이진욱, 유진오, 윤병동. "변속 조건 하에서의 기어박스 진단을 위한 회전 속도 추정 방법 개발". *Conference : 한국PHM학회 2022년도 정기학술대회, 2022-06-30*.
- 김수지, 김태진, 윤병동. "구름 요소 베어링 고장 진단을 위한 다중 센서 기반 전자파간섭 노이즈 제거 기법". *Conference : 한국PHM학회 2022년도 정기학술대회, 2022-07-01*.
- 김성종, 이승윤, 김수지, 윤헌준, 윤병동. "베어링 진단을 위한 고장 관련성 기반 다중 채널 데이터 융합 인공지능 모델 개발". *Conference : 2022년도 춘계 소음진동 학술대회, 2022-05-26*.
- 김태훈, 고진욱, 이진욱, 김용채, 윤병동. "회전체 시스템의 신뢰도 높은 신호 생성을 위한 적대적 생성 모델의 잠재 공간 분석 방법". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-20*.
- 이진욱, 고진욱, 김태훈, 김용채, 윤병동. "클래스 불균형 및 가변 운행 조건 하에서 회전 기계 진단을 위한 샘플링 기반 비지도 도메인 적응 기법". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-20*.
- Chen Jiang, 윤병동. "정적 및 동적 예측 모델의 불확실성 감소를 위한 베이지안 보정기법". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-20*.
- 채민석, 김형민, 오혜준, 박찬희, 서채현, 윤헌준, 윤병동. "적은 고장 데이터 상황에서의 퓨샷 학습 기반 영구 자석 동기 모터 고장 진단 기법 개발". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-20*.
- 최현희, 김태진, 윤병동. "스웰링을 고려한 파우치형 배터리 등가역모델 개발". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-20*.
- 김원곤, 윤병동. "리벳 접합부 균열 발생 추정을 위한 램 파형을 이용한 통계적 물리 모델 갱신 방법". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-20*.
- 김용채, 고진욱, 이진욱, 김태훈, 윤병동. "회전체 고장진단을 위한 잠재공간내 인스턴스 거리 기반 도메인 적응 기법". *Conference : 대한기계학회 2022년 학술대회, 2022-11-11*.
- 오혜준, 김형민, 채민석, 서채현, 박찬희, 윤헌준, 윤병동. "모터 고장 진단을 위한 손실 함수 적응적 가중치 기반 다중 도메인 적응 활용 토크 불변 특성 학습". *Conference : 대한기계학회 2022년 학술대회, 2022-11-11*.
- 김형민, 윤병동. "다채널 시스템 이상 감지를 위한 오토 인코더 잠재 공간 최적화". *Conference : 대한기계학회 2022년 학술대회, 2022-11-11*.
- 임주현, 김원곤, 안성훈, 윤병동. "FDM 방식 3D 프린터에 대한 딥러닝 기반 물성 추정". *Conference : 대한기계학회 2022년 학술대회, 2022-11-11*.
- Chen Jiang, 최현희, 윤병동. "Physics-Informed Gaussian Process Probabilistic Modeling for Prognostics of Degradation Processes". *Conference : 대한기계학회 2022년 학술대회, 2022-11-11*.
- Chen Jiang, 최현희, 윤병동. "Physics-Informed Gaussian Process Probabilistic Modeling for Prognostics of Degradation Processes". *Conference : 대한기계학회 2022년 학술대회, 2022-11-09*.
- 최현희, Chen Jiang, 김태진, 윤병동. "파우치형 배터리 모듈의 구조 신뢰성 분석을 위한 통계적 면압 예측 모델 개발". *Conference : 대한기계학회 2022년 학술대회, 2022-11-09*.
- 김원곤, 임주현, 안성훈, 윤병동. "융합 수지 압출 적층 조형의 디지털 트윈을 위한 최적화 기반 시계열 데이터 보간 기법". *Conference : 대한기계학회 2022년 학술대회, 2022-11-09*.
- 조수호, 윤병동. "다른 형상을 가진 이중 결함 인가 음향양자 결정의 에너지 국부화 양상". *Conference : 대한기계학회 2022년 학술대회, 2022-11-09*.
- 정화용, 김수지, 윤헌준, 윤병동. "딥러닝을 활용한 구름요소베어링 고장크기 추정 기법 개발". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-20*.
- 김형민, 박찬희, 서채현, 채민석, 오혜준, 윤병동, 윤헌준. "다양한 운행 조건에서 모터의 딥러닝 기반 순시 고장 진단 방법". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-20*.
- Haichao An, 윤병동, 김흥수. "고장 및 시스템의 다양한 건전성 상태를 고려한 새로운 복원도 인자 정식화". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-20*.
- 김용채, 고진욱, 이진욱, 김태훈, 윤병동. "회전체 고장진단을 위한 수도라벨링 기반 도메인 적응 기법". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-19*.
- 윤병동, 서채현, 김형민, 박찬희, 채민석, 윤헌준. "일반화 및 설명 가능성을 위한 도메인 지식과 인공지능의 융합-물류 자동화 시스템에의 적용". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-19*.
- 고진욱, 이진욱, 김태훈 ,김용채 ,윤병동. "인공지능 기반 불균형 데이터를 활용한 사출성형 공정 최적화 모델". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-19*.
- 조수호, 윤병동. "음향양자 결정의 결함 모드를 활용한 공진형 압전 트랜스듀서 개발". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-19*.
- 유진오, 박종민, 김태형, 하종문, 윤병동. "비정상 운행 조건 하 회전체 고장 진단을 위한 시주파수 영역에서의 센서리스 회전속도 추정 기법 개발". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-19*.
- 김수지, 김태진, 윤병동. "모터 전류 신호를 활용한 포락스팩트럼 상의 전자파장애 노이즈 제거 기법". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-19*.
- 오혜준, 김형민, 채민석, 서채현, 박찬희, 윤병동, 윤헌준. "모터 고장 진단을 위한 다중 소스 도메인 활용 도메인 적응 기법". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-19*.
- 이승윤,김성종,김수지,윤헌준,윤병동. "도메인 차이를 고려한 전이학습 기반 초저속 베어링 고장 진단". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-19*.
- 박종민, 하종문, 윤병동. "다양한 속도 조건에서 오토엔코더를 활용한 속도 무관 베어링 고장 피쳐 추출 기법 개발". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-19*.
- 김태형, 유진오, 박종민, 하종문, 윤병동. "고장 특성 정보 강화 및 시간동기 평균화를 통한 회전체 고장 진단". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-19*.
- 나규민, 김건, 윤헌준, 윤병동. "고장 신호 강화 이미지를 통한 기어박스 다중 클래스 고장 진단". *Conference : 대한기계학회 CAE 및 응용역학부문 2022년 춘계학술대회, 2022-05-19*.

**2021**

- Soo-Ho Jo and Byeng D. Youn\*. "An Explicit Solution for the Design of a Target-frequency-customized, Piezoelectric-defect-introduced Phononic Crystal for Elastic Wave Energy Harvesting". *Journal of Applied Physics, 2021-11, Vol. 130, No. 18, pp. 184902 · DOI <https://doi.org/10.1063/5.0072053>*.

## 과제

수행 기간이 2021년 10월 22일–2026년 10월 22일과 겹치는 49건이다. 과제명·기간·지원기관과 Ongoing·Completed 상태는 연구실 표기를 따른다.[^projects]

- Development of an Estimated Time of Arrival (ETA) Prediction Model and Framework for Robotic Parking Services (기간 2026-07-01 ~ 2027-06-30; 지원 HL Robotics; 상태 Ongoing)
- Development of a Manufacturing AI Foundation Model Specialized for Thermal Processes Ministry of Trade (기간 2026-06-01 ~ 2028-12-31; 지원 Industry and Resources; 상태 Ongoing)
- Manufacturing Task-Specific Foundation Models for a Full-Stack AI Factory (기간 2026-06-01 ~ 2031-02-28; 지원 Ministry of Science and ICT; 상태 Ongoing)
- AI-based OHT Routing Algorithm Development (기간 2026-05-01~2028-04-30; 지원 OnePredict; 상태 Ongoing)
- Development of Core Technologies for a PHM System for Fixed-Wing Aircraft Based on a System Lineage Graph (기간 2026-04-07~2026-12-31; 지원 OnePredict; 상태 Ongoing)
- Development and Demonstration of a Standard Model for a Korean Manufacturing-X Platform Ministry of Trade (기간 2026-04-01 ~ 2029-12-31; 지원 Industry and Resources; 상태 Ongoing)
- Advancing Thermo-Mechanical Reliability in 2.xD/3D Packages using Physics-Informed AI and Generative Models (기간 2025-10-01 ~ 2030-09-28; 지원 Samsung Electronics; 상태 Ongoing)
- Development of a Virtual Process Control System Based on Operational Data for Digital Twin Environment Construction (기간 2025-09-29 ~ 2027-09-28; 지원 Korea Western Power Co., Ltd; 상태 Ongoing)
- Development of Core Technologies for Manufacturing Foundation Models (MFM) (기간 2025-07-01 ~ 2028-01-31; 지원 Ministry of Trade, Industry and Energy; 상태 Ongoing)
- Foundation of Next-generation Eco-friendly Secondary Battery Components to Strengthen Supply Chain (기간 2025-05-01 ~ 2028-12-31; 지원 Ministry of Trade, Industry and Energy; 상태 Ongoing)
- Development and Demonstration of Purpose-Built Electric Vehicles Using Design Platforms (기간 2024-07-01 ~ 2027-12-31; 지원 Ministry of Trade, Industry and Energy; 상태 Ongoing)
- HRD Program in Industrial AI Manufacturing Innovation to Realize Autonomous Manufacturing (기간 2024-03-01 ~ 2029-02-28; 지원 Ministry of Trade, Industry and Energy; 상태 Ongoing)
- Development of CBM+-based Anomaly Detection, Condition Diagnosis, and Degradation Prediction Technologies for Major Railway Vehicle Systems (기간 2026-03-19~2026-09-30; 지원 OnePredict; 상태 Completed)
- Development of Predictive Maintenance (PDM) Algorithms for the Bead Forming and Bead Polishing Processes of Electric Vehicle Battery Cases (BPC) at ONEPREDICT (기간 2025-11-21 ~ 2026-06-30; 지원 OnePredict; 상태 Completed)
- Development of Predictive Maintenance (PdM) Algorithms for the Pre-Piercing, Cutting, and Round Bending Processes in the Roll Forming (R/F) Line at ONEPREDICT (기간 2025-11-21 ~ 2026-06-30; 지원 OnePredict; 상태 Completed)
- Safety Guardian Al Agent Using Four-Sense Sensor Data Quadruped Robot (기간 2026-01-01 ~ 2026-12-31; 지원 Ministry of Science and ICT; 상태 Completed)
- Development of Chamberless Noise Diagnosis Algorithm for Washing Machines (기간 2025-12-29 ~ 2026-09-30; 지원 Samsung Electronics; 상태 Completed)
- Development of PHM Technology for Fixed-wing Aircraft Using System-level Test Rig (기간 2025-08-29~2025-12-31; 지원 OnePredict; 상태 Completed)
- Advanced Data Augmentation of Semiconductor Datasets for Regression Models (기간 2025-08-01 ~ 2026-07-30; 지원 Samsung Electronics; 상태 Completed)
- Safety Guardian Al Agent Using Four-Sense Sensor Data Quadruped Robot (기간 2025-07-01 ~ 2025-12-31; 지원 Ministry of Science and ICT; 상태 Completed)
- Signal Processing and Algorithm Development for Abnormal Sound Diagnosis in Washing Machines (기간 2025-06-09 ~ 2025-11-17; 지원 Samsung Electronics; 상태 Completed)
- Development of Battery Anomaly Detection and Performance Degradation Prediction Technology Based on Electro-Mechanical Fusion Characteristics (Current, Voltage + Stack Pressure) (기간 2025-05-01 ~ 2025-12-31; 지원 Hyundai Motors & KIA Inc.; 상태 Completed)
- Failure Analysis of Washing Machine Bearings Based on Accelerated Degradation Testing (ADT) (기간 2024-12-20 ~ 2025-09-20; 지원 Samsung Electronics; 상태 Completed)
- Development of PHM Technology for Fixed-wing Aircraft Using System-level Test Rig (기간 2024-11-01 ~ 2024-12-31; 지원 OnePredict; 상태 Completed)
- Development of Diagnosis Algorithm for Sleeve Bearing (기간 2024-10-01 ~ 2025-01-31; 지원 OnePredict; 상태 Completed)
- Development of Vehicle Weight Prediction Algorithms Based on CAN Data And Research Direction for PHM Platforms (기간 2024-09-01 ~ 2025-09-30; 지원 Hyundai NGV; 상태 Completed)
- Development of Deep Learning Framework (기간 2024-08-01 ~ 2024-10-31; 지원 OnePredict; 상태 Completed)
- Experimental Design and Predictive Modeling Framework with Multivariate Condition (기간 2024-06-01 ~ 2025-05-31; 지원 Samsung Electronics; 상태 Completed)
- Stack Pressure-based Health Index Development of Li-ion Battery and Sensorless Real-time Fault Diagnosis Using Knowledge Distillation (기간 2024-03-15 ~ 2024-11-14; 지원 Hyundai NGV; 상태 Completed)
- Development of Diagnosis Section Segmentation and Load Estimation for Earth Moving Machinery (기간 2024-03-01 ~ 2025-02-28; 지원 HD Hyundai XiteSolution; 상태 Completed)
- Development of a Battery Prognostics and Health Management System for Fixed-Wing Aircraft (기간 2024-01-01 ~ 2024-06-30; 지원 Korea Aerospace Industries; 상태 Completed)
- Diagnostic Model Development for Electrification System Considering Vehicle (기간 2023-09-25 ~ 2024-09-24; 지원 Hyundai NGV; 상태 Completed)
- Development of Diagnosis Section Segmentation and Load Estimation for Earth Moving Machinery (기간 2023-03-01 ~ 2024-02-29; 지원 HD Hyundai Xitesolution; 상태 Completed)
- Development of Deep-learning-based Fault Diagnosis for Tipper System (기간 2023-03-01 ~2023-12-31; 지원 Ministry of Science and ICT; 상태 Completed)
- A Mechanical Fault Diagnosis of Induction Motors Using Current Signals (기간 2023-01-05 ~ 2023-04-05; 지원 OnePredict Inc.; 상태 Completed)
- Development of Diagnostic Technology for Gearbox Non-stationary Drive Area (기간 2022-03-01 ~ 2023-02-28; 지원 Hyundai Doosan Infracore; 상태 Completed)
- Development of Industrial Robot Fault Detection using Current Signal with Physics-based Inverse Modeling (기간 2021-11-15 ~ 2022-09-15; 지원 Hyundai Motor; 상태 Completed)
- ASIP Data Analysis and Prediction of Maintenance Demand Based on Big Data (기간 2021-07-01 ~ 2024-06-30; 지원 Korea Aerospace Industries; 상태 Completed)
- Data-Driven Modelling of Swelling Degradation for a Reliable Battery Module & Pack Design (기간 2021-04-15 ~ 2022-10-14; 지원 Hyundai NGV; 상태 Completed)
- Korea-Germany Intelligent Manufacturing Systems Laboratory (기간 2021-03-01 ~ 2024-02-29; 지원 National Research Foundation of Korea; 상태 Completed)
- Development of Fault Diagnosis for Gearbox under Non-stationary Rotational Operating Conditions (기간 2021-03-01 ~ 2022-02-28; 지원 Doosan Infracore; 상태 Completed)
- Operation of Industry-Academic Advisory Group for Reliability Component Development (기간 2021-03-01 ~ 2022-02-28; 지원 Hyundai Motor; 상태 Completed)
- Development of Health State Diagnostics and Prognostics for Substation Facility based on Integration of Artificial Intelligence and Expert Knowledge (기간 2020-08-01 ~ 2022-05-19; 지원 Korea Electric Power Corporation; 상태 Completed)
- Operation of Industry-Academic Advisory Group for Improving Automotive Reliability (기간 2020-06-01 ~ 2022-03-20; 지원 Hyundai Motor; 상태 Completed)
- Physics+AI Modeling and Evolution Methodology for Mechanical Systems (기간 2020-03-01 ~ 2024-02-29; 지원 National Research Foundation of Korea; 상태 Completed)
- Industrial Artificial Intelligence (AI) Human Resource Development (HRD) (기간 2020-03-01 ~ 2024-02-29; 지원 Ministry of Trade, Industry and Energy; 상태 Completed)
- Industrial Artificial Intelligence for Intelligent Machines and Manufacturing Digitalization (기간 2019-12-01 ~ 2022-11-30; 지원 Korea Institute for Advancement of Technology; 상태 Completed)
- Development of AI-based Diagnosis and Prognostics System for Power Plant (기간 2018-07-01 ~ 2022-05-19; 지원 Korea Electric Power Corporation; 상태 Completed)
- A Study on Bayesian-based Signal Acquisition System and Physics-AI Hybrid Model for Next-Generation Aircraft Structure Damage Estimation (기간 2022-09-30 ~ 2025-09-29; 지원 National Research Foundation of Korea; 상태 Completed)

## 특허

2021년 10월 22일–2026년 10월 22일의 출원·등록 게시 항목 69건이다. 출원과 등록은 서로 구분해 표시한다.[^patents]

- 2024-10-16 · 출원 · "Apparatus and Method for Estimating Rotational Speed of Gear Box Based on Vibration Signal" China Byeng D. Youn, Keon Kim, Kyumin Na, Jinwook Lee, and Jinoh Yoo Patent No. : 202411447334.3
- 2024-10-16 · 출원 · "Apparatus and Method for Estimating Rotational Speed of Gear Box Based on Vibration Signal" United States of America Byeng D. Youn, Keon Kim, Kyumin Na, Jinwook Lee, and Jinoh Yoo Patent No. : 18/917100
- 2024-10-16 · 출원 · "Apparatus and Method for Estimating Rotational Speed of Gear Box Based on Vibration Signal" European Patent Byeng D. Youn, Keon Kim, Kyumin Na, Jinwook Lee, and Jinoh Yoo Patent No. : 24206820.3
- 2024-09-30 · 출원 · "Apparatus And Method for Dignosing Gear Box Based on Vibration Signal" Patent Cooperation Treaty Byeng D. Youn, Keon Kim, Kyumin Na, Jinwook Lee, and Jinoh Yoo Patent No. : PCT/KR2024/014894
- 2023-06-30 · 출원 · "Transformer Malfunction Diagnosis Device and Malfuction Diagnosis Method Using Same" United States of America Byeng D. Youn, Sunuwe Kim, Soo-Ho Jo, Jongmin Park, and Wongon Kim Patent No. : 18/260090
- 2022-12-12 · 출원 · "System and Method for Estimating Pressure DIstribution of a Battery Cell" United States of America Byeng D. Youn, Wongon Kim, Hwayong Jeong, Yong Seok Choi, and Soon Chul Byun Patent No. : 18/079695
- 2026-09-10 · 출원 · "주파수 대역 그래프 기반 기계 시스템의 고장 진단 장치 및 방법" 윤병동, 이상경, 채민석, 김한수, 양준호, 김형민, 윤헌준 Patent No. : 10-2026-0173157
- 2026-09-10 · 출원 · "비정상 운전 조건 하에서의 모터 고장 진단 장치 및 방법" 윤병동, 김한수, 채민석, 이상경, 양준호, 김형민, 윤헌준 Patent No. : 10-2026-0173156
- 2026-08-26 · 출원 · "전이학습 기반 연산자 신경망을 이용한 회전 기기의 고장 심각도 추정 장치 및 방법" 윤병동, 김한수, 김형민, 양준호, 윤헌준, 이상경, 채민석 Patent No. : 10-2026-0161241
- 2026-08-06 · 출원 · "베어링 고장 진단 장치 및 진단 방법" 윤병동, 이현찬, 유진오, 김태형, 하종문 Patent No. : 10-2026-0147022
- 2026-03-27 · 출원 · "신호처리 기반 어텐션 가중치를 이용한 시계열 인공지능 모델 분석 장치 및 방법" 윤병동, 김민재, 김성종, 윤헌준, 이승윤 Patent No. : 10-2026-0056049
- 2025-10-16 · 출원 · "기어 기반 회전체 장치의 고장 진단 장치 및 방법" 윤병동, 김태형, 박종민, 유진오, 하종문 Patent No. : 10-2025-0149676
- 2025-09-16 · 출원 · "기계 시스템의 고장 진단 방법" 윤병동, 이상경, 김형민, 채민석, 김한수, 양준호, 윤헌준 Patent No. : 10-2025-0132923
- 2025-09-16 · 출원 · "전동기 고장 심각도 추정 방법" 윤병동, 채민석, 김한수, 양준호, 이상경, 김형민, 윤헌준 Patent No. : 10-2025-0132924
- 2025-09-16 · 출원 · "모터 고장 진단 방법" 윤병동, 김한수, 채민석, 양준호, 이상경, 김형민, 윤헌준 Patent No. : 10-2025-0132925
- 2025-08-27 · 출원 · "전동기의 고장을 감지하는 방법 및 장치" 윤병동, 김건, 김성종, 김한수, 박종혁, 정화용 Patent No. : 10-2025-0120300
- 2025-07-31 · 출원 · "전이학습 기반 회전 기계용 고장 진단 장치 및 방법" 윤병동, 김민재, 김성종, 김수지, 윤헌준, 이승윤, 이지원 Patent No. : 10-2025-0105287
- 2025-07-29 · 출원 · "고장 데이터 생성 기능을 이용하는 회전체용 고장 진단 장치 및 방법" 윤병동, 고진욱, 김용채, 김태훈, 이진욱 Patent No. : 10-2025-0103568
- 2025-07-08 · 출원 · "회전 기계용 고장 진단 시스템 및 방법" 윤병동, 김민재, 김성종, 김수지, 윤헌준, 이승윤, 이지원 Patent No. : 10-2025-0091744
- 2025-06-24 · 출원 · "회전 기계 시스템용 고장 진단 장치 및 방법" 윤병동, 김용채, 이진욱, 김태훈, 고진욱, 백종화, 정준하 Patent No. : 10-2025-0083506
- 2025-06-16 · 출원 · "자기지도학습 기반 모터 고장 진단 시스템 및 방법" 윤병동, 윤헌준, 이상경, 김형민, 채민석, 오혜준 Patent No. : 10-2025-0078755
- 2024-09-12 · 출원 · "잠재 공간 정렬 기반 도메인 적응을 이용한 고장 진단 장치 및 방법" 윤병동, 김용채, 이진욱, 김태훈, 고진욱, 정준하 Patent No. : 10-2024-0125101
- 2024-08-21 · 출원 · "다양한 토크 조건 하 모터 고장진단을 위한 자기지도학습 모델" 윤병동, 윤헌준, 이상경, 김형민, 채민석, 오혜준 Patent No. : 10-2024-0111970
- 2024-08-20 · 출원 · "베이지안 기반 딥러닝 진단 모델을 이용한 고장 진단 장치 및 방법" 윤병동, 채민석, 이상경, 김한수, 백종화 Patent No. : 10-2024-0111208
- 2024-06-17 · 출원 · "운행 상태 모델링 데이터 기반 회전 기계 시스템의 상태 진단 장치 및 방법" 윤병동, 나규민 Patent No. : 10-2024-0078387
- 2024-04-09 · 출원 · "회전 기계 시스템용 고장 진단 장치 및 방법" 윤병동, 이진욱, 김태훈, 김용채, 백종화 Patent No. : 10-2024-0048216
- 2023-10-17 · 출원 · "진동 신호에 기반한 기어 박스의 회전 속도 추정 장치 및 방법" 윤병동, 김건, 나규민, 이진욱, 유진오 Patent No. : 10-2023-0138195
- 2023-10-17 · 출원 · "진동 신호에 기반한 기어 박스 진단 장치 및 방법" 윤병동, 김건, 나규민, 이진욱, 유진오 Patent No. : 10-2023-0138192
- 2023-03-31 · 출원 · "회전 기계 시스템의 노이즈 제거 장치 및 방법" 윤병동, 김수지, 김태진, 박종민, 김근수, 황태완, 정화용 Patent No. : 10-2023-0042645
- 2022-05-02 · 출원 · "전지 셀의 압력분포 추정시스템 및 추정방법" 윤병동, 최용석, 변순철, 김원곤, 정화용 Patent No. : 10-2022-0054203
- 2023-08-09 · 등록 · "진동 신호 기반 모션 신호 추출 시스템 및 방법" 윤병동, 나규민, 김윤한 Patent No. : 10-2566810
- 2023-08-07 · 등록 · "탭 절환장치의 기계적 이상 검출방법" 윤병동, 김현재, 김원곤 Patent No. : 10-2565620
- 2023-07-24 · 등록 · "발전 설비의 상태 신호를 이용한 튜브 누설 검출 시스템 및 방법" 윤병동, 김재동, 손종덕, 김희수, 오준석, 김형민, 나규민 Patent No. : 10-2560573
- 2023-07-24 · 등록 · "발전 설비의 상태 신호를 이용한 튜브 누설 검출 시스템 및 방법" 윤병동, 김재동, 손종덕, 김희수, 오준석, 김형민, 나규민 Patent No. : 10-2560572
- 2023-07-14 · 등록 · "발전 설비의 상태 신호를 이용한 튜브 누설 검출 시스템 및 방법" 윤병동, 김재동, 손종덕, 김희수, 오준석, 김형민, 나규민 Patent No. : 10-2557199
- 2023-07-14 · 등록 · "발전 설비의 상태 신호를 이용한 튜브 누설 검출 시스템 및 방법" 윤병동, 김재동, 손종덕, 김희수, 오준석, 김형민, 나규민 Patent No. : 10-2557198
- 2023-05-25 · 등록 · "상전류 신호를 이용한 모터 고장 진단 방법 및 장치" 윤병동, 박찬희, 김현재, 이준민, 윤명백, 안길준 Patent No. : 10-2538542
- 2023-01-03 · 등록 · "선회장치의 고장진단 장치 및 방법" 윤병동, 김건, 하종문, 나규민 Patent No. : 10-2485686
- 2022-12-20 · 등록 · "다채널 신호를 이용한 모터 고장 진단 방법 및 장치" 윤병동, 서채현, 박찬희, 김형민, 채민석 Patent No. : 10-2480899
- 2022-12-15 · 등록 · "사출성형 공정 불량 검출 모델 학습 방법 및 사출성형 공정의 레시피 최적화 방법" 윤병동, 고진욱, 이진욱, 김태훈, 김용채 Patent No. : 10-2479531
- 2022-11-28 · 등록 · "전동기의 고장 검출 장치 및 방법" 윤병동, 김형민, 박찬희, 서채현, 채민석 Patent No. : 10-2473124
- 2022-08-11 · 등록 · "정보 행렬 기반 시험 설계를 통한 오류 식별 및 모델 업데이트 방법" 윤병동, 손혜정, 김태진 Patent No. : 10-2433219
- 2022-07-27 · 등록 · "데이터 전처리 장치 및 방법" 윤병동, 김수호, 최현희 Patent No. : 10-2437540
- 2022-05-27 · 등록 · "적응적 시간-주파수 표현 기반 합성곱 신경망을 활용한 산업용 기어박스 고장진단 장치 및 방법" 윤병동, 김윤한 Patent No. : 10-2404498
- 2022-05-10 · 등록 · "비지도 도메인 적응 기법을 통한 고장 진단 장치 및 이를 이용한 고장 진단 방법" 윤병동, 이진욱, 김명연, 고진욱 Patent No. : 10-2398046
- 2022-05-03 · 등록 · "가변 운행 환경에서 모터의 고장 발생 여부를 판단하는 장치 및 방법" 윤병동, 박찬희, 이준민, 신용진, 안길준, 윤명백 Patent No. : 10-2395570
- 2025-12-23 · 등록 · "회전 기계 시스템의 노이즈 제거 장치 및 방법" 윤병동, 김수지, 김태진, 박종민, 김근수, 황태완, 정화용 Patent No. : 10-2905399
- 2025-07-07 · 등록 · "다중 스케일 확장 합성곱을 이용한 회전체 고장 진단 장치 및 방법" 윤병동, 김형민, 박찬희, 서채현, 윤헌준, 채민석 Patent No. : 10-2832630
- 2025-05-12 · 등록 · "폐쇄성 말초 동맥질환의 진단 장치 및 그 진단을 위한 PAD 검출 모델의 구축 방법" 윤병동, 이인찬, 김수호, 임주현, 이동휴, 한진오 Patent No. : 10-2808131
- 2025-04-25 · 등록 · "회전체의 고장 진단 장치 및 방법" 윤병동, 김수지, 이승윤, 김성종, 김태진 Patent No. : 10-2802391
- 2024-03-27 · 등록 · "오토 인코더 기반 이상 데이터 감지 시스템 및 방법" 윤병동, 나규민, 고진욱, 김형민 Patent No. : 10-2653349
- 2024-02-05 · 등록 · "마르코프 체인 몬테 카를로 샘플링의 초기값 결정 방법" 윤병동, 이현찬, 김원곤, 손혜정, 최현희 Patent No. : 10-2635503
- 2024-01-18 · 등록 · "메타물질 기반 탄성파 평행 이동 장치" 윤병동, 조수호 Patent No. : 10-2628439
- 2023-12-27 · 등록 · "D-norm 기반 시간 동기 평균 기법에 의한 회전체 고장 진단 시스템 및 방법" 윤병동, 하종문, 최원재, 승홍민 Patent No. : 10-2619799
- 2023-11-23 · 등록 · "센서 데이터 활용 부분 방전 감지 시스템 및 방법" 윤병동, 박종민, 김수호 Patent No. : 10-2607227
- 2023-11-07 · 등록 · "모터 고장 진단을 위한 이미지 생성 방법 및 장치, 상기 이미지를 이용한 모터 고장 진단 방법 및 장치" 윤병동, 박찬희, 김형민, 서채현, 채민석, 윤헌준 Patent No. : 10-2601072
- 2023-11-01 · 등록 · "셉스트럼 기반 유성 기어박스의 고장 감지 장치 및 방법" 윤병동, 김윤한, 나규민 Patent No. : 10-2598458
- 2022-03-30 · 등록 · "위상 정보를 활용한 기어박스의 고장 감지 장치 및 방법" 윤병동, 김윤한, 나규민, 박정호 Patent No. : 10-2382628
- 2022-03-10 · 등록 · "변압기 고장 진단을 위한 방법 및 장치" 윤병동, 김선의, 조수호, 박종민, 김원곤 Patent No. : 10-2374551
- 2022-02-16 · 등록 · "회전체 설비 고장발생 위험도 지수 평가 장치 및 그 방법" 김동환, 김연환, 이두영, 윤병동, 정준하, 김명연 Patent No. : 10-2365772
- 2022-02-15 · 등록 · "생성적 적대 신경망을 이용한 상태 감시 데이터 생성 방법 및 장치" 윤병동, 김현재, 박정호, 황태완, 한명규, 신재경, 송용천 Patent No. : 10-2365150
- 2022-02-10 · 등록 · "다층 리커런스 플롯을 활용한 전이학습 기반 가공 품질 모니터링 방법" 윤병동, 안성훈, 김윤한, 김태겸 Patent No. : 10-2362971
- 2022-01-19 · 등록 · "선회장치의 고장진단 장치 및 방법" 윤병동, 김광일, 김건, 임동필, 하종문, 박정호 Patent No. : 10-2354568
- 2022-01-19 · 등록 · "진동 신호 이미지를 활용한 직접 연결 모델 기반 회전체 시스템 고장 진단 방법 및 장치" 윤병동, 김명연, 이진욱, 고진욱 Patent No. : 10-2354814
- 2022-01-18 · 등록 · "메타물질 기반 탄성파 에너지 국부화 장치" 윤병동, 조수호 Patent No. : 10-2354340
- 2022-01-18 · 등록 · "변압기의 고장 진단 장치 및 이를 이용한 고장 진단 방법" 윤병동, 김선의, 조수호, 박종민, 김원곤 Patent No. : 10-2354342
- 2022-01-18 · 등록 · "압전 결함 기반 탄성파 에너지 수확 장치" 윤병동, 조수호 Patent No. : 10-2354341
- 2021-12-08 · 등록 · "진동 신호 이미지를 활용한 직접 연결 모델 기반 회전체 시스템 고장 진단 장치 및 방법" 윤병동, 김명연, 고진욱, 이진욱 Patent No. : 10-2338737
- 2021-11-05 · 등록 · "다층 리커런스 플롯을 활용한 전이학습 기반 가공 품질 모니터링 장치 및 방법" 윤병동, 안성훈, 김윤한, 김태겸 Patent No. : 10-2324979

## 수상과 선정

2021년 10월 22일–2026년 10월 22일에 게시된 수상·장학금·선정 93건이다. 날짜는 게시일이며, 제목 속 행사 연도·학년도와 다를 수 있다. 등급과 수상자 이름은 연구실 표기를 따른다.[^awards][^news]

- 2026-09-18 · European Conference on Computer Vision (ECCV) 2026 Workshop – Best Paper Runner-Up · 한주환, 김태훈, 이동휴, 김세희, 조수호, 윤병동
- 2026-09-15 · PHM Korea 2026 정기학술대회 우수 발표상 · 채민석, 김용채, 이상경, 김주현, 강지헌, 임우리, 최종현, 박준호, 박찬희, 하종문, 윤병동
- 2026-09-15 · PHM Korea 2026 정기학술대회 우수 발표상 · 김한수, Christian Gogu, Sebastien Schwartz, 윤병동
- 2026-09-02 · 한국연구재단 2026년도 이공분야 학문후속세대지원사업 - 석사과정생 연구장려금 수주 · 김세희
- 2026-09-02 · 한국연구재단 2026년도 이공분야 학문후속세대지원사업 - 석사과정생 연구장려금 수주 · 강지헌
- 2026-09-02 · 한국연구재단 2026년도 이공분야 학문후속세대지원사업 - 박사과정생 연구장려금 수주 · 채민석
- 2026-09-02 · 한국연구재단 2026년도 이공분야 학문후속세대지원사업 - 박사과정생 연구장려금 수주 · 유성준
- 2026-09-02 · 한국연구재단 2026년도 이공분야 학문후속세대지원사업 - 박사과정생 연구장려금 수주 · 김태형
- 2026-09-02 · 한국연구재단 2026년도 이공분야 학문후속세대지원사업 - 박사과정생 연구장려금 수주 · 김주현
- 2026-06-19 · AI서울테크 연구지원사업 장학금 · 유성준
- 2026-05-11 · 대한기계학회 CAE 및 응용역학부문 2026년도 춘계학술대회 학생 경진대회 - 금상 · 김주현
- 2026-05-10 · 대한기계학회 CAE 및 응용역학부문 2026년도 춘계학술대회 학생 경진대회 - 은상 · 채민석
- 2026-04-26 · 대한기계학회 창립 80주년 기념 학술대회 - 우수논문상 · 한주환, 유진오, 이현찬, 주성필, 김주호, 전용권, 성대운, 윤병동
- 2026-01-15 · 2025년 현대모비스 전동화 우수논문대회-우수상 · 강지헌
- 2025-12-16 · 제 5회 K-인공지능 제조데이터 분석 경진대회-장려상 · 이상경, 김용채, 김주현
- 2025-12-16 · AI Factory Hackathon 2025-대상 · 박종혁, 한주환, 김세희, 유해수
- 2025-12-11 · 제4회 KSME-LG 퓨처 홈 테크 챌린지-은상 · 김용채, 김주현, 김태형, 임우리
- 2025-12-05 · Editage Grant-Certificate of Appreciation · 박예인
- 2025-09-01 · 한국연구재단 2025년도 이공분야 학문후속세대지원사업 - 박사과정생 연구장려금 수주 · 김성종
- 2025-09-01 · 한국연구재단 2025년도 이공분야 학문후속세대지원사업 - 박사과정생 연구장려금 수주 · 유진오
- 2025-09-01 · 한국연구재단 2025년도 이공분야 학문후속세대지원사업 - 박사과정생 연구장려금 수주 · 이승윤
- 2025-09-01 · 한국연구재단 2025년도 이공분야 학문후속세대지원사업 - 박사과정생 연구장려금 수주 · 김태훈
- 2025-09-01 · 한국연구재단 2025년도 이공분야 학문후속세대지원사업 - 박사과정생 연구장려금 수주 · 이상경
- 2025-09-01 · 한국연구재단 2025년도 이공분야 학문후속세대지원사업 - 석사과정생 연구장려금 수주 · 한주환
- 2025-08-26 · 율촌 AI Young Researcher 장학금 · 김용채
- 2025-05-30 · Springer Nature Editor of Distinction Awards 2025 · Byeng D. Youn
- 2025-04-18 · 대한기계학회 CAE 및 응용역학부문 2025년도 춘계학술대회 학생 경진대회 - 은상 · 김주현, 김용채, 권경륜, 송원빈, 정준하, 윤병동
- 2025-04-17 · 대한기계학회 CAE 및 응용역학부문 2024년도 춘계학술대회 - 우수논문상 · 이상경, 김형민, 채민석, 김한수, 양준호, 윤헌준, 윤병동
- 2025-04-10 · 대한기계학회 신뢰성 부문 2024년도 춘계학술대회 - 우수논문상 · 김태훈, 이진욱, 김용채, 백종화, 김주현, 정준하, 윤병동
- 2025-04-10 · 대한기계학회 신뢰성 부문 2025년도 - 우수학위논문상(석사) · 이지원
- 2025-03-24 · 원프레딕트 · Incubatenergy Challenge 결선 진출
- 2025-02-25 · 스마트 농업 인공지능(AI) 경진대회 - 대상 · 김태훈
- 2025-01-20 · 원프레딕트 · Emerging AI + X 선정
- 2025-01-15 · 한국최적설계학회 - 우수학위논문상 (박사) · 최현희
- 2025-01-14 · 산업AI해커톤 Factory Hack Korea 2025-대상 · 박종혁, 송원빈, 이현찬
- 2024-12-26 · 현대차 정몽구 스칼러십 글로벌 우수 장학생 · 김태훈
- 2024-12-03 · 2024년 K-인공지능 제조데이터 분석 경진대회 - 최우수상 · 김주현, 권경륜, 송원빈
- 2024-09-13 · 율촌 AI for All Fellowship 장학금 · 이승윤
- 2024-09-11 · Highly Ranked Scholar, Design Optimization 분야 선정 · 윤병동
- 2024-09-01 · 한국연구재단 2024년도 이공분야 학문후속세대지원사업 - 박사과정생 연구장려금 수주 · 김용채
- 2024-09-01 · 한국연구재단 2024년도 이공분야 학문후속세대지원사업 - 박사과정생 연구장려금 수주 · 이동휴
- 2024-07-01 · 한국연구재단 2024년도 이공분야 학문후속세대지원사업 - 석사과정생 연구장려금 수주 · 김주현
- 2024-06-28 · PHM Korea 2023 정기학술대회 우수 발표상 · 나규민
- 2024-05-03 · 대한기계학회 CAE 및 응용역학부문 2024년도 춘계학술대회 학생 경진대회 - 최우수상 · 김용채
- 2024-05-02 · 대한기계학회 CAE 및 응용역학부문 2024년도 - 우수학위논문상(박사) · 김형민
- 2024-05-02 · 대한기계학회 CAE 및 응용역학부문 감사패 · 윤병동
- 2024-01-30 · 산업AI해커톤 Factory Hack Korea 2024- 최우수상 · 김용채, 이상경, 김봉모, 김민정
- 2024-01-30 · 산업AI해커톤 Factory Hack Korea 2024- 우수상 · 김성종, 이승윤, 이지원, 김민재
- 2023-12-01 · Postech Open Innovation Big Data Challenge - 장려상 · 이상경, 김용채, 김봉모, 이지원, 김민정
- 2023-09-20 · 4단계 BK21 우수 대학원생 펠로우십 · 김민재
- 2023-09-11 · PHMAP 2023 Data Challenge Competition - Winner (2nd Place) · 이상경, 이지원, 이승윤, 김봉모, 김용채, 이진욱, 윤병동
- 2023-06-27 · 현대차 정몽구 재단 장학금 · 김태훈
- 2023-06-07 · 2023 IEEE International Conference on Prognostics and Health Management Conference - 2nd Place Winner in Data Challenge Competition · 김태형, 오혜준, 김민정, 유진오, 김형민
- 2023-06-07 · 2023 IEEE International Conference on Prognostics and Health Management Conference - 1st Place Winner in Data Challenge Competition · 이승윤, 김용채, 이상경, 김봉모, 이지원, 이진욱
- 2023-05-19 · 대한기계학회 CAE 및 응용역학부문 2023년도 춘계학술대회 학생 경진대회 - 우수상 · 오혜준
- 2023-05-19 · 대한기계학회 CAE 및 응용역학부문 2023년도 춘계학술대회 학생 경진대회 - 우수상 · 이동휴
- 2023-05-18 · 대한기계학회 CAE 및 응용역학부문 2023년도 - 우수학위논문상(박사) · 고진욱
- 2023-05-18 · 대한기계학회 CAE 및 응용역학부문 2022년도 춘계학술대회 - 우수논문상 · 박종민, 하종문, 윤병동
- 2023-05-18 · 대한기계학회 CAE 및 응용역학부문 2022년도 춘계 학술대회 - 우수논문상 · 최현희, 윤병동, 김태진
- 2023-05-18 · 대한기계학회 CAE 및 응용역학부문 2022년도 춘계 학술대회 - 우수논문상 · 윤병동, 서채현, 김형민, 박찬희, 채민석, 윤헌준
- 2023-05-18 · 대한기계학회 CAE 및 응용역학부문 2022년도 춘계 학술대회 - 우수논문상 · 임주현, 김원곤, 안성훈, 윤병동
- 2023-02-24 · 서울대학교 기계공학부 2022학년도 2학기 우수석사학위논문상 · 김태훈
- 2023-02-24 · 서울대학교 기계공학부 2022학년도 2학기 우수박사학위논문상 · 고진욱
- 2023-02-03 · 산업AI해커톤 Factory Hack Korea 2023 - 최우수상 · 이승윤, 김봉모
- 2023-02-03 · 산업AI해커톤 Factory Hack Korea 2023 - 우수상 · 오혜준, 이상경, 채민석, 김형민
- 2023-01-01 · National Natural Science Foundation of China - Young Scientist Fund Project · Haichao An
- 2022-12-31 · Crystals - 2022 Best Ph.D. Thesis Award · 조수호
- 2022-12-19 · Postech Open Innovation Big Data Challenge - 우수상 · 이상경, 오혜준, 김용채, 김봉모
- 2022-11-03 · 2022 PHM Society Data Challenge Competition - Winner (2nd Place) · 김용채, 김태훈, 고진욱, 이진욱, 김건, 윤병동
- 2022-11-03 · 2022 PHM Society Data Challenge Competition - Winner (1st Place) · 오혜준, 유진오, 이상경, 채민석, 박종민, 윤병동
- 2022-07-21 · 관정이종환장학재단 장학금 · 김용채
- 2022-07-08 · 한국신뢰성학회 2022 춘계 학술대회 - 우수발표 논문상 · 이규석, 최현희, 최용환, 윤병동
- 2022-06-01 · 한국연구재단 2022년도 이공분야 학문균형발전지원사업 - 창의도전연구과제 수주 · 조수호
- 2022-05-19 · 대한기계학회 CAE 및 응용역학부문 2022년도 춘계학술대회 학생논문발표경진대회 - 은상(3위) · 김형민
- 2022-05-19 · 대한기계학회 CAE 및 응용역학부문 2022년도 - 학술상 · 윤병동
- 2022-05-19 · 대한기계학회 CAE 및 응용역학부문 2022년도 - 우수학위논문상(석사) · 서채현
- 2022-05-19 · 대한기계학회 CAE 및 응용역학부문 2022년도 - 우수학위논문상(박사) · 박찬희
- 2022-05-19 · 대한기계학회 CAE 및 응용역학부문 2021년도 춘계학술대회 - 우수학생발표상 · 김명연
- 2022-05-19 · 대한기계학회 CAE 및 응용역학부문 2021년도 춘계학술대회 - 우수논문상 · 최현희, 최용환, 손혜정, 이규석, 윤병동
- 2022-03-24 · 대한기계학회 신뢰성부문 2022년도 - 우수학위논문상(박사) · 김윤한
- 2022-03-18 · 4단계 BK21 우수 대학원생 펠로우십 · 김용채
- 2022-02-25 · 서울대학교 기계공학부 2021학년도 2학기 우수박사학위논문상 · 김윤한
- 2022-02-25 · 제 2회 조선/해양산업 디지털 혁신을 위한 Big Data / AI 대학생 경진대회 - 장려상 · 김태훈, 이승윤, 김용채
- 2022-02-11 · 산업AI해커톤 Factory Hack Korea 2022 - 장려상 · 김태훈, 이동휴, 이승윤
- 2021-12-28 · 제 3회 동서발전 발전데이터 AI 경진대회 - 장려상 · 이승윤, 김태훈
- 2021-12-18 · Heart Disease AI Datathon 2021 - 대상 · 이동휴, 이승윤
- 2021-12-16 · 2021년 K-인공지능 제조데이터 분석 경진대회 - 장려상(KAIST K-Industry 4.0 추진본부장상) · 김수지, 박종민, 김성종
- 2021-12-16 · 2021년 K-인공지능 제조데이터 분석 경진대회 - 우수상(스마트제조혁신추진단장상) · 김원곤, 채민석
- 2021-12-16 · 2021년 K-인공지능 제조데이터 분석 경진대회 - 대상(중소벤처기업부 장관상) · 고진욱, 이진욱, 김태훈
- 2021-11-26 · 한국 신뢰성 대상 · 윤병동
- 2021-11-23 · 2021 현대자동차 R&D AI 경진대회 - 장려상 · 오혜준
- 2021-11-12 · 2021 산학 프로젝트 챌린지 - 최우수상(산업통상자원부 장관상) · 서채현, 김도완, 이현찬
- 2021-10-29 · 2021년 한국센서학회 추계학술대회 - 우수 발표 논문상 · 조수호, 윤병동

## 소식

2021년 10월 22일–2026년 10월 22일의 연구·과제·산학협력 소식과 언론 소개 109건이다. 날짜는 게시일이다.[^news][^press]

- 2026-10-22 · 언론 소개: 「[특별인터뷰]윤병동 원프레딕트 대표, “제조업의 진정한 혁신, 'AI 네이티브 팩토리'에 달렸다”」
- 2026-10-15 · 언론 소개: 「원프레딕트, 피지컬 AI 테크 위크서 차세대 공장 운영 전략 공개」
- 2026-10-07 · 언론 소개: 「원프레딕트, 국가 피지컬AI 사업 ‘제조 AI 공통 프레임워크’ 개발 나선다」
- 2026-10-07 · 언론 소개: 「원프레딕트 “버려지던 제조 데이터, AI 자산으로 바꾸겠다”」
- 2026-10-02 · 언론 소개: 「‘공정에 AI를 붙인다’…충북 제조현장 M.AX 전환 본격화」
- 2026-09-10 · 언론 소개: 「서울대 윤병동 교수팀, 제조 자율화 이끌 ‘풀스택 AI 팩토리’ 구축 나서」
- 2026-08-27 · 제조 분야별 파운데이션 모델 과제가 과학기술정보통신부 리더연구 지원사업에 선정됐다.
- 2026-08-24 · 언론 소개: 「윤병동 원프레딕트 대표 "AI가 공장 운영 중심 되는 시대 온다"」
- 2026-08-11 · 언론 소개: 「“숙련공 떠나기 전에 AI 심어라”…윤병동 대표가 말하는 제조 AX」
- 2026-08-09 · 언론 소개: 「윤병동 대표 "대기업과 손잡고 공장 '자율제조 3단계' 시대 주도"」
- 2026-07-27 · 언론 소개: 「“제조 경쟁력 갈림길…‘AI 네이티브 팩토리’ 전환해야”」
- 2026-07-07 · 언론 소개: 「원프레딕트, 국내 제약사 5곳과 AI 네이티브 팩토리 구축」
- 2026-07-03 · 언론 소개: 「세메스 'AI로 설계부터 공정최적화까지'…혁신 가속도」
- 2026-06-26 · 언론 소개: 「원프레딕트 윤병동 대표, AI 네이티브 팩토리 수출 국가 비전 제시」
- 2026-06-25 · 언론 소개: 「원프레딕트, 생산·품질·정비 AI 에이전트 하나로 연결한다」
- 2026-06-22 · 언론 소개: 「기대감 높아지는 AI 팩토리…원프레딕트, 'AI 팩토리 OS'로 시장 정조준」
- 2026-06-05 · 언론 소개: 「공장 기계 데이터 분석…장비 이상땐 즉각 감지」
- 2026-05-26 · 언론 소개: 「원프레딕트, 'One Model Many Task'로 제조업 AI 컨트롤타워 구축 추진」
- 2026-05-13 · 언론 소개: 「車 부품 공정에 AI 적용하니 불량률 20% 뚝」
- 2026-04-08 · 언론 소개: 「서울대 산업AI센터-DMI, ‘제조 AX’ 협력…대구 지역기업 지원」
- 2025-12-02 · 언론 소개: 「원프레딕트, 산업부 ‘AI팩토리 선도사업’ 수주…농심과 식품 제조 혁신 착수」
- 2025-11-24 · 언론 소개: 「산업부, 서울대에 휴머노이드 등 ‘제조 AI 전환’ 연구 기지」
- 2025-10-14 · 언론 소개: 「KETI, 산학연 협력으로 '제조 특화 AI 파운데이션 모델' 공동개발 착수」
- 2025-09-29 · 운영 데이터를 이용한 가상 공정 제어 및 디지털 트윈 환경 구축 과제를 시작했다.
- 2025-08-29 · 시스템 시험 장비를 이용한 고정익 항공기 상태 진단·수명 예측 기술 개발 과제를 시작했다.
- 2025-07-01 · 네 가지 감각의 센서 데이터와 사족보행 로봇을 이용한 안전 관리 인공지능 에이전트 과제를 시작했다.
- 2025-06-09 · 세탁기 이상 소음 진단을 위한 신호 처리·알고리즘 개발 과제를 시작했다.
- 2025-05-27 · 언론 소개: 「"제조현장에 AI 도입한다"...산업부, 'AI 팩토리' 본격 추진」
- 2025-05-01 · 전류·전압·적층 압력의 융합 특성에 기반한 배터리 이상 탐지·성능 저하 예측 과제를 시작했다.
- 2025-05-01 · 차세대 친환경 이차전지 부품의 공급망 강화를 위한 기반 구축 과제를 시작했다.
- 2025-03-11 · 언론 소개: 「원프레딕트, AW 2025 참가...AI 자산 통합관리 솔루션 '가디원 pdx' 전시」
- 2025-03-10 · 언론 소개: 「원프레딕트 윤병동 대표, "산업 AI의 미래, 데이터 플랫폼 구축이 최우선"」
- 2025-02-19 · 원프레딕트가 Motiva에 GuardiOne 솔루션을 공급하는 계약을 체결했다.
- 2024-12-20 · 가속 열화 시험에 기반한 세탁기 베어링 고장 분석 과제를 시작했다.
- 2024-12-16 · 언론 소개: 「월등한 정확성과 예측력…제조업체가 가디원 pdx를 선택하는 이유」
- 2024-11-01 · 시스템 시험 장비를 이용한 고정익 항공기 상태 진단·수명 예측 기술 개발 과제를 시작했다.
- 2024-10-22 · 언론 소개: 「'교수 창업가’ 윤병동 대표, 산업AI 표준에 도전하다」
- 2024-10-15 · 연구실과 현대자동차그룹이 차량 고장 예측 기술을 위한 공동 연구를 시작했다.
- 2024-10-01 · 슬리브 베어링 진단 알고리즘 개발 과제를 시작했다.
- 2024-09-12 · 언론 소개: 「"제조업 데이터 많이 쌓은 한, 산업용 AI에 기회"」
- 2024-09-01 · 차량 통신 자료를 이용한 차량 중량 예측 알고리즘 및 상태 진단·수명 예측 플랫폼 연구를 시작했다.
- 2024-08-09 · 언론 소개: 「운반로봇 동선 꼬이자 'AI처방'…소리·온도로 이상징후 탐지」
- 2024-08-02 · 언론 소개: 「윤병동 원프레딕트 대표_산업 AI 퍼스트 무버」
- 2024-08-01 · 딥러닝 체계 개발 과제를 시작했다.
- 2024-07-18 · 언론 소개: 「'AI가 생산시설을 구한다' 생산시설 진단하는 AI 개발한 윤병동 원프레딕트 대표」
- 2024-07-01 · 설계 플랫폼을 활용한 목적 기반 전기차 개발·실증 과제를 시작했다.
- 2024-07-01 · 언론 소개: 「LLM 출혈 대신 ‘돈 되는 서비스’ 경쟁 [메이킹 머니 AI]」
- 2024-06-13 · 언론 소개: 「원프레딕트, 하이텍앤솔과 MOU 체결」
- 2024-06-10 · 윤병동 교수가 공동 집필한 『테크 스타트업 챔피언』이 출간됐다.
- 2024-06-01 · 여러 조건을 고려하는 실험 설계 및 예측 모델링 과제를 시작했다.
- 2024-05-21 · 연구실의 새 이름과 연구 방향을 알렸다.
- 2024-04-24 · 언론 소개: 「원프레딕트, 2024 국제 전기전력 전시회서 산업 AI 기반 설비 예지보전 솔루션 소개 나선다… “다운타임 최소화”」
- 2024-04-19 · 언론 소개: 「AI가 공장의 건강 상태 진단해드립니다」
- 2024-04-14 · 언론 소개: 「윤병동 원프레딕트 대표 "산업의 디지털화 이끌겠다" [중기·벤처 'Why Pick']」
- 2024-03-27 · 언론 소개: 「[스마트공장·자동화산업전] 원프레딕트, AI이용한 ‘가디원’으로 예측 진단 솔루션 제시」
- 2024-03-20 · 언론 소개: 「원프레딕트, 국내외 예지보전 솔루션 시장 공략박차」
- 2024-03-15 · 리튬이온 배터리 적층 압력 기반 상태 지표 및 지식 전달을 통한 센서 없는 실시간 고장 진단 과제를 시작했다.
- 2024-03-01 · 자율제조 실현을 위한 산업 인공지능 제조혁신 인력 양성 과제를 시작했다.
- 2024-03-01 · 토공 기계의 진단 구간 분할·부하 추정 과제를 시작했다.
- 2024-02-14 · 언론 소개: 「원프레딕트, GS칼텍스 설비관리에 AI 기반 솔루션 ‘가디원 터보’ 구축」
- 2024-02-01 · 언론 소개: 「원프레딕트, AI 생산 프로세스 최적화 지원 솔루션 ‘눈앞’」
- 2024-01-01 · 고정익 항공기용 배터리 고장 예측·상태 관리 시스템 탐색 개발 과제를 시작했다.
- 2023-11-19 · 언론 소개: 「[DAMEX 2023] 원프레딕트, 산업AI/IoT 기반으로 설비 상태 진단 및 예측 솔루션 '가디원' 선보여」
- 2023-11-04 · 언론 소개: 「[AW 2024 참가업체 인터뷰] 원프레딕트 윤병동 대표이사 “ 변화하는 예지보전 솔루션 시장, 산업 AI와 융합한 솔루션 통해 시장 선도할 것”」
- 2023-10-18 · 언론 소개: 「[SMATOF 2023] 원프레딕트, 디지털 브레인 솔루션 ‘가디원 시리즈’ 소개」
- 2023-10-08 · 언론 소개: 「[SMATOF 2023] 원프레딕트, 변압기·모터 상태 진단 시리즈 ‘가디원’ 제시」
- 2023-09-25 · 차량을 고려한 전동화 시스템 진단 모델 개발 과제를 시작했다.
- 2023-07-18 · 언론 소개: 「원프레딕트, 산업AI 기반 변압기 예측진단 솔루션 ‘가디원 서브스테이션’ v2.0 론칭」
- 2023-06-29 · 언론 소개: 「[KOFAS 2023] 원프레딕트, 산업 설비 예지보전 솔루션 두 종 전시」
- 2023-06-28 · 원프레딕트가 제조자동화기술전에서 Guardione Motor와 Guardione Substation을 소개했다.
- 2023-06-15 · 언론 소개: 「원프레딕트, 2023 대한민국 전기산업엑스포서 '가디원 서브스테이션'선보여..."변압기 사고 미연에 방지한다!"」
- 2023-04-29 · 언론 소개: 「[나라장터]설비 상태 진단 및 예측하는 산업 AI 기반 솔루션」
- 2023-04-07 · 언론 소개: 「원프레딕트, 2023 국제 전기전력 전시회서 변전설비 진단 및 고장 예측 소프트웨어 소개 나선다... "생산 손실 최소화, 설비 가동률 최대화"」
- 2023-04-03 · 언론 소개: 「[기고] 디지털 시대에 기계공학인이 가야 할 길」
- 2023-03-08 · 언론 소개: 「공장장으로 취업한 AI, 제조 생산성을 높이다」
- 2023-03-01 · 팁퍼 시스템의 딥러닝 기반 고장 진단 개발 과제를 시작했다.
- 2023-03-01 · 토공 기계의 진단 구간 분할·부하 추정 과제를 시작했다.
- 2023-02-28 · 언론 소개: 「원프레딕트 ‘가디원 모터’, 국내 최대 규모 ‘스마트공장 자동화산업전 2023’ 참가」
- 2023-02-07 · 언론 소개: 「[SF+AW 2023 참가업체 인터뷰] 원프레딕트 윤병동 대표이사 “가디원 솔루션 적용 분야 확대로 예지보전 선도기업 우뚝”」
- 2023-02-03 · 언론 소개: 「[SF+AW 2023 PREVIEW] 원프레딕트, '가디원 모터'로 모터 종합 진단관리 지원」
- 2023-01-25 · 언론 소개: 「[기고]디지털 전환에 따른 설비 예지보전 최적화 솔루션 가이드」
- 2023-01-05 · 전류 신호를 이용한 유도 모터의 기계적 고장 진단 과제를 시작했다.
- 2022-12-21 · 언론 소개: 「[기고]실제 도입 사례로 본 설비 유지보수 디지털 대전환」
- 2022-12-14 · 언론 소개: 「원프레딕트, GS파워에 '가디원 모터' 산업AI 모터 진단 솔루션 공급」
- 2022-12-11 · 언론 소개: 「영화 ‘마이너리티 리포트’처럼…불량 생기기 전, 불량 잡아낸다」
- 2022-11-30 · 언론 소개: 「원프레딕트, E1에 ‘가디원’ 산업AI 기반 설비 예측진단 솔루션 공급」
- 2022-11-22 · 언론 소개: 「원프레딕트, 사우디서 산업AI 솔루션 소개」
- 2022-11-01 · 언론 소개: 「소음진동 특집 - 음향양자 결정의 결함 모드를 이용한 압전 에너지 수확 성능 증폭」
- 2022-11-01 · 언론 소개: 「기계저널 테마기획 - 산업 인공지능 기반 발전 설비 고장 진단 및 예측 시스템 개발」
- 2022-09-30 · 차세대 항공기 구조 손상 추정을 위한 베이지안 신호 취득 및 물리·인공지능 결합 모델 과제를 시작했다.
- 2022-09-25 · 언론 소개: 「산업AI 예지보전 솔루션으로 스마트제조 환경 완성…설비 건전성·고장 예측으로 비용 최소화」
- 2022-07-13 · 언론 소개: 「원프레딕트 ‘가디원 터보’, 과기정통부 우수연구개발 혁신제품 지정…공공기관 수의계약 허용」
- 2022-05-18 · 언론 소개: 「원프레딕트'가디원 서브스테이션', GS인증 1등급 획득」
- 2022-05-09 · 언론 소개: 「공장설비도 건강검진.. 고장 위험 미리 예측하죠」
- 2022-04-19 · 언론 소개: 「변전설비 AI로 유지보수...;가디원 서브스테이션' 호평 이어져」
- 2022-04-19 · 언론 소개: 「원프레딕트 "가디원 서브스테이션", 미 송배전 산업전시회 출품」
- 2022-04-07 · 언론 소개: 「원프레딕트, AI 회전자 상태 진단하는 '가디원로터' 출시 앞둬」
- 2022-03-31 · 언론 소개: 「원프레딕트, ‘SFAW 2022’ 참가…산업AI 솔루션 공개」
- 2022-03-23 · 언론 소개: 「로봇이 공장 움직인다…스마트팩토리 팔 걷은 기업들」
- 2022-03-14 · 언론 소개: 「원프레딕트, 모터 종합진단 관리 솔루션 '가디원 모터' 출시」
- 2022-03-01 · 기어박스의 비정상 운전 구간 진단 기술 개발 과제를 시작했다.
- 2022-02-19 · 언론 소개: 「{SF+AW 2022 참가업체 인터뷰] 원프레딕트 윤병동 대표이사 "가디원 솔루션은 '디지털 브레인', 고객 고민을 현실적, 혁신적으로 해법 제시"」
- 2022-02-16 · 언론 소개: 「설비 고장을 미리 알려준다. "AI 예지보전"시장 확산세」
- 2022-01-13 · 언론 소개: 「공장 다운타임 막는 "AI예지보전" 구축 문턱 낮아진다」
- 2021-12-29 · 언론 소개: 「한국 경제 근간 제조업, AI 로 혁신 활로 찾다」
- 2021-12-28 · 언론 소개: 「과학기술정보통신부 '5G융합서비스 발굴 및 공공선도'사업」
- 2021-12-17 · 언론 소개: 「뿌리 기업의 현장 문제, 'KAMP'로 해결 가능성 높인다」
- 2021-11-15 · 물리 기반 역모델링과 전류 신호를 이용한 산업용 로봇 고장 탐지 과제를 시작했다.
- 2021-11-05 · 언론 소개: 「[D파이오니어를 만나다] "인터넷 등장 버금가는 산업 AI시대 개막… 새로운 성장신화 쓸 것"」

## 연락과 위치

- 교수실: 서울대학교 301동 1514호. 전화 02-880-1919, 이메일 bdyoun@snu.ac.kr.[^professor]
- 연구실: 301동 215호(02-880-1664), 313동 214호(02-882-1884), 313동 324-2호(02-883-1664), 314동 306호(02-883-1884).[^location][^pi]
- 주소: 서울특별시 관악구 관악로 1, 서울대학교, 우편번호 08826.[^location][^professor]
- 모집 안내: 학부 연구 인턴, 박사후연구원, 연구교수를 모집하며, 지원자는 이력서를 연락 이메일로 보내도록 안내한다.[^location]
[^about]: HAI Lab, About HAI LAB. <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub1_1> (관측 2026-11-07).
[^dfm]: HAI Lab, Design Foundation Model 본문. <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub3_1> (관측 2026-11-07).
[^mfm]: HAI Lab, Manufacturing Foundation Model 본문. <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub3_2> (관측 2026-11-07).
[^physical]: HAI Lab, Physical AI. <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub3_3> (관측 2026-11-07).
[^pi]: 서울대학교 기계공학부, 윤병동 교수 소개. <https://me.snu.ac.kr/snu__professor/%ec%9c%a4%eb%b3%91%eb%8f%99-youn-byeng-dong/> (관측 2026-11-07).
[^professor]: HAI Lab, Professor. <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub2_1> (관측 2026-11-07).
[^members]: HAI Lab, Current members. <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub2_2> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub2_2&page=2> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub2_2&page=3> (관측 2026-11-07).
[^alumni]: HAI Lab, Alumni. <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub2_3> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub2_3&page=2> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub2_3&page=3> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub2_3&page=4> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub2_3&page=5> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub2_3&page=6> (관측 2026-11-07).
[^journals]: HAI Lab, Journal International. <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a&page=2> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a&page=3> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a&page=4> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a&page=5> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a&page=6> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a&page=7> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a&page=8> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a&page=9> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a&page=10> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a&page=11> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a&page=12> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a&page=13> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a&page=14> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a&page=15> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a&page=16> (관측 2026-11-07).
[^conferences]: HAI Lab, Conference International·Domestic. <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=2> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=3> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=4> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=5> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=6> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=7> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=8> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=9> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=10> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=11> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=12> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=13> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=14> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=15> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=16> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=17> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=18> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=19> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=20> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=21> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&page=22> <https://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=8> <https://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=15> <https://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=18> <https://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=20> <https://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=22> <https://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=23> <https://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=25> <https://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=28> <https://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=29> <https://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=30> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=2> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=3> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=4> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=5> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=6> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=7> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=9> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=10> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=11> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=12> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=13> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=14> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=16> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=17> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=19> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=21> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=24> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=26> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_b&page=27> (관측 2026-11-07).
[^patents]: HAI Lab, Patent Application·Registration. <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_2_a> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_2_a&page=2> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_2_a&page=3> <https://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_2_b&page=2> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_2_b> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_2_b&page=3> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_2_b&page=4> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_2_b&page=5> (관측 2026-11-07).
[^projects]: HAI Lab, Project. <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub5_1> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub5_1&page=2> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub5_1&page=3> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub5_1&page=4> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub5_1&page=5> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub5_1&page=6> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub5_1&page=7> (관측 2026-11-07).
[^awards]: HAI Lab, Awards. <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_2> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_2&page=2> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_2&page=3> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_2&page=4> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_2&page=5> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_2&page=6> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_2&page=7> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_2&page=8> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_2&page=9> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_2&page=10> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_2&page=11> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_2&page=12> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_2&page=13> (관측 2026-11-07).
[^news]: HAI Lab, News. <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=2> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=3> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=4> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=5> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=6> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=7> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=8> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=9> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=10> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=11> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=12> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=13> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=14> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=15> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=16> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=17> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=18> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=19> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=20> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=21> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_1&page=22> (관측 2026-11-07).
[^press]: HAI Lab, Press. <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=2> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=3> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=4> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=5> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=6> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=7> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=8> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=9> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=10> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=11> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=12> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=13> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=14> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=15> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=16> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=17> <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub6_3_a&page=18> (관측 2026-11-07).
[^location]: HAI Lab, Location. <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub1_2> (관측 2026-11-07).
[^bioaaa]: S. Masoumi Shahrbabak 외, J.-O. Hahn, Sensors 25(21), 6678 (2025). <https://doi.org/10.3390/s25216678> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5084771659,publication_year:2021-2026> (관측 2026-11-07).
[^biopad]: S. Masoumi Shahrbabak 외, J.-O. Hahn, Computers in Biology and Medicine 168, 107813 (2024). <https://doi.org/10.1016/j.compbiomed.2023.107813> 초록 기준(연구실 게시 논문 상세(Abstract)). 초록 원문 <https://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_1_a&page=4&wr_id=209> (관측 2026-11-07).
[^p1]: H. Kim 외, B. D. Youn, Journal of Computational Design and Engineering 13, 20-34 (2026). <https://doi.org/10.1093/jcde/qwag057> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5084771659,publication_year:2021-2026> (관측 2026-11-07).
[^p2]: C. Suh 외, B. D. Youn, Journal of Computational Design and Engineering 12, 49-60 (2025). <https://doi.org/10.1093/jcde/qwaf058> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5084771659,publication_year:2021-2026> (관측 2026-11-07).
[^p3]: S. Ahn 외, S.-H. Ahn, Journal of Computational Design and Engineering 11, 234-248 (2024). <https://doi.org/10.1093/jcde/qwae061> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5084771659,publication_year:2021-2026> (관측 2026-11-07).
[^p4]: D. Lee, T. Kim, B. D. Youn, S.-H. Jo, Journal of Computational Design and Engineering 12, 129-147 (2025). <https://doi.org/10.1093/jcde/qwaf060> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5084771659,publication_year:2021-2026> (관측 2026-11-07).
[^p5]: J.-g. Park, H. Yoon, B. D. Youn, Journal of Computational Design and Engineering 10, 539-548 (2023). <https://doi.org/10.1093/jcde/qwad007> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5084771659,publication_year:2021-2026> (관측 2026-11-07).
[^p6]: S.-H. Jo 외, M. Kim, Nano Convergence 9, 29 (2022). <https://doi.org/10.1186/s40580-022-00321-x> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5084771659,publication_year:2021-2026> (관측 2026-11-07).
[^p7]: J. Han 외, B. D. Youn, ECCV 2026 (연구실 기재) (2026). <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&wr_id=359> 초록 기준(논문 페이지 게시 초록). 초록 원문 <http://hai.snu.ac.kr/bbs/board.php?bo_table=sub4_3_a&wr_id=359> (관측 2026-11-07).

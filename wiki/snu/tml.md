# Turbomachinery Laboratory

**서울대학교 공과대학 기계공학부 · 송성진 교수**

- 영문 이름: Turbomachinery Laboratory (TML)
- 분야: 터보기계의 공력·유동 안정성, 로켓 터보펌프, 분산형 에너지 시스템 최적화
- 대분야: 기계·로봇·제조, 에너지·환경·지구
- 태그: 유체역학·유동[^research][^compressor], 발사체·로켓 추진[^cavitation], 진동·소음 공학[^rotordynamic][^forced]
- 홈페이지: <https://tml.snu.ac.kr/>
- 근거와 출처: [Turbomachinery Laboratory 근거 페이지](tml-sources.md)

> 회전하는 날개와 액체·기체 사이의 에너지 교환을 연구하고, 항공·발전용 터보기계의 손실과 불안정한 흐름을 줄이는 방법을 찾는 연구실이다.[^about][^research]

## 무엇을 연구하나

Turbomachinery Laboratory는 송성진 교수가 이끄는 서울대학교 기계공학부 연구실이다. 터보기계는 회전하는 날개를 통해 유체(흐를 수 있는 액체와 기체)와 기계 사이에서 에너지(일을 하거나 열을 전달할 수 있는 물리량)를 주고받는 장치다. 압력은 표면에 수직으로 작용하는 힘을 단위 면적으로 나눈 양이다. 연구실은 가스터빈(기체를 압축·가열한 뒤 터빈에서 팽창시켜 동력을 얻는 열기관), 압축기(기체의 압력을 높이는 장치), 터빈(유체에서 에너지를 받아 회전하는 기계)의 공력 성능과 손실을 연구한다. 실험과 수치해석(문제를 수식으로 나타내고 수치 계산으로 근삿값을 구하는 방법)을 함께 사용한다.[^about][^research][^faculty]

첫째는 **날개 주변 흐름과 기계의 운전 안정성**이다. 압축기 안에서 흐름이 불안정해지는 현상을 억제하고, 표면 거칠기와 습도가 날개 성능에 주는 영향을 분석한다.[^research] 터빈에서는 고온 기체가 회전 부품 사이 공간으로 들어오는 것을 막는 공기 흐름과 날개 끝의 틈새에서 새는 흐름을 다룬다. 흐름 자체의 구조뿐 아니라 그것이 날개에 주는 힘과 손실을 함께 밝히는 것이 목표다.[^compressor][^humidity][^roughness][^purge]

둘째는 **액체 추진 로켓과 산업용 펌프·압축기의 불안정성**이다. 산화제는 다른 물질에서 전자를 받는 물질이다. 로켓의 연료와 산화제를 보내는 터보펌프(터빈으로 구동하는 펌프)에서 캐비테이션(액체의 압력이 해당 온도의 증기압 아래로 낮아져 증기 기포가 생기는 현상)을 연구한다. 펌프 앞부분의 인듀서(주 회전 날개 앞에서 유체의 압력을 높여 흡입 성능을 돕는 회전 날개 장치)를 대상으로 온도와 입구 흐름의 불균일이 기포와 불안정성에 미치는 영향을 조사한다.[^cavitation] 산업용 회전기계에서는 유체가 회전축의 흔들림에 주는 힘과 날개의 진동 원인을 분석한다.[^rotordynamic][^forced]

셋째는 **재생에너지를 포함한 에너지 공급 설계**다. 태양광·태양열·풍력, 열과 전기를 함께 생산하는 설비, 에너지 저장을 묶은 현장 공급 시스템을 다룬다. 필요한 열과 전기를 공급하면서 환경 목표를 만족하고 총비용을 줄일 수 있도록 설비 구성과 시간별 운전을 결정하는 최적화 체계를 개발한다. 에너지 의무 사용 제도나 저장 설비 지원 정책의 평가도 응용 대상으로 든다.[^energy]

## 주요 연구 주제

### 압축기 안정성과 날개 주변 흐름

축류 압축기(주된 흐름이 회전축 방향으로 지나는 압축기)에서는 회전 실속을 억제하는 방법을 연구한다. 회전 실속은 날개 주변 흐름이 떨어져 나가 압력을 제대로 높이지 못하는 영역이 둘레 방향으로 이동하는 현상이다. 바깥 덮개에 비스듬한 홈을 내는 방법과 공기를 분사하는 방법을 다단 압축기에 적용해 작동 원리를 실험과 계산으로 조사한다.[^compressor] 또 여러 단의 고정 날개와 회전 날개가 남기는 후류, 날개 끝과 덮개 사이의 새는 흐름, 축 가까운 공간에서의 흐름이 서로 영향을 주는 방식을 분석한다.[^wake] 대표 논문 7은 이러한 흐름이 합쳐질 때 속도 변화와 흐름 각도의 주기적 변동이 어떻게 달라지는지 측정했다.[^p7]

천음속 압축기에서는 상대습도(같은 온도에서 공기가 수증기를 최대로 포함할 수 있는 양에 대한 현재 수증기량의 비율) 변화가 압력 분포와 손실, 날개를 지난 흐름의 방향에 미치는 영향을 조사한다.[^humidity] 표면 연구에서는 경계층이 층류에서 난류로 바뀌는 전이와 손실의 관계를 다룬다. 대표 논문 4는 적층 제조(Additive Manufacturing, 재료를 층별로 더해 입체 형상을 만드는 방법)로 생긴 표면 거칠기가 압축기 날개 성능에 미치는 영향을, 대표 논문 5는 터빈 날개에 해당하는 압력 변화 조건에서 거칠기가 경계층 전이에 주는 영향을 분석했다.[^roughness][^p4][^p5]

### 터빈의 밀봉·누설과 작동 유체

터빈에서는 고온 기체가 날개 원판 사이로 들어와 부품을 손상시키지 않도록 퍼지 유동을 공급한다. 연구실은 림실(원판 사이 공간과 주 흐름의 경계에 두어 기체 유입을 억제하는 밀봉 구조)의 형상별 밀봉 성능과, 밖으로 나온 퍼지 유동이 주 흐름과 섞일 때 생기는 손실을 연구한다. 바깥 덮개에서 주입한 흐름과 날개 끝 틈새 흐름의 상호작용도 분석한다.[^purge][^leakage] 대표 논문 6은 원판 쪽 흐름의 회전 성분을 높였을 때 고온 기체 유입을 막는 데 필요한 유량이 줄어드는 현상을 보였다.[^p6]

슈라우드는 누설 손실을 줄이는 한편 회전 부품의 무게와 응력을 증가시킬 수 있다. 연구실은 일부 구간에만 슈라우드를 두는 형상을 설계하고, 성능과 무게를 함께 고려해 계산과 실험으로 평가하는 연구를 소개한다.[^shroud] 초임계 이산화탄소를 작동 유체로 쓰는 터빈에서는 손실 발생 원인과 효율 향상 방법을 조사한다.[^sco2] 천연가스 팽창기에서는 팽창 중 응축으로 생긴 액체 방울에 따른 성능 저하와 날개 표면이 깎이는 문제를 흐름 계산으로 다룬다.[^condensation]

### 캐비테이션과 회전기계 진동

터보펌프 인듀서에서는 온도와 입구 흐름 변화가 캐비테이션 및 흡입 성능에 미치는 영향을 측정한다. 압력과 흐름을 시간에 따라 재고 기포의 모습을 관찰해 불안정성의 발생 원리를 연구한다.[^cavitation] 레이저는 물질이 빛에 반응해 같은 성질의 빛을 내놓는 과정으로 빛을 증폭하는 장치다. 기초 연구에서는 레이저로 정해진 위치에 기포를 만들어 고체 표면 근처와 액체 내부에서의 기포 거동을 조사한다.[^laser] 대표 논문 2는 날개 사이 상호작용을 서로 연결된 질량·스프링·감쇠기의 운동으로 나타내 불안정성이 발생한 뒤의 변화를 예측했다. 감쇠기는 운동 에너지를 소모해 진동을 줄이는 요소다.[^p2]

산업용 원심 압축기에서는 임펠러와 디퓨저의 상대 운동이 날개에 시간에 따라 변하는 힘과 진동을 만드는 원인을 연구한다.[^forced] 회전축이 덮개 중심에서 벗어난 편심 상태에서 비대칭 흐름과 회전축에 작용하는 힘을 조사하고, 이 힘이 축의 흔들림을 키우는 원리를 분석한다.[^rotordynamic] 대표 논문 3은 혼류 펌프(회전 날개를 지나는 흐름이 축 방향과 반지름 방향으로 함께 향하는 펌프)에서 주 흐름 통로와 부차적인 통로의 비대칭성을 함께 고려해야 회전축에 작용하는 힘을 정확히 예측할 수 있다고 제시했다.[^p3] 대표 논문 1은 딥러닝(여러 층의 연결된 계산 단위가 자료의 특징을 단계적으로 학습하는 기계학습 분야)으로 관측 범위가 제한된 영상에서 캐비테이션 불안정성을 구별하는 방법을 제안했다.[^p1]

### 재생에너지 공급 시스템 최적화

분산형 에너지 시스템에서 연구하는 대상은 개별 발전 장치만이 아니라 설비들의 조합과 시간별 운전이다. 연구실은 재생에너지와 저장 설비를 포함한 현장 전력·열 공급 시스템에 대해, 일정한 재생에너지 비중이나 일차에너지 사용 감축 같은 환경 목표를 만족하며 총비용을 최소화하는 구성을 찾는 체계를 개발한다. 일차에너지는 다른 형태로 바꾸기 전 자연에서 얻는 에너지를 뜻한다. 이 체계의 용도로 주어진 수요에 맞춘 시스템 설계와 에너지 정책 평가를 든다.[^energy]

## 대표 논문

서울대 재직 시기의 2021–2026년 논문 가운데 캐비테이션, 펌프 유체력, 표면 거칠기, 터빈 밀봉, 다단 압축기 흐름을 고르게 골랐다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 주요 저자는 초록과 함께 게시된 저자 목록의 첫 저자와 송성진 교수를 표시했다.

| 번호 | 연도 | 논문 | 주요 저자 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2026 | [Deep Learning-Based Identification of Cavitation Instabilities in Turbopump Inducers Using Raw Visualization Data](https://doi.org/10.1115/1.4071348)[^p1] | 1저자 Sanghyun Lee · 마지막 저자 Seung Jin Song | 공간과 시간의 특징을 함께 학습하는 신경망(연결된 계산 단위들이 자료의 특징과 관계를 학습하는 계산 모형)으로 인듀서 기포 영상에서 두 종류의 불안정성을 구별했다. 일부 시야와 짧은 영상에서도 별도 재학습 없이 구별 성능을 유지함을 보였다. |
| 2 | 2025 | [Model for Local Cavitation Instabilities in Two-Bladed Turbopump Inducers](https://doi.org/10.1115/1.4067027)[^p2] | 1저자 Youngkuk Yoon · 마지막 저자 Seung Jin Song | 인듀서 날개들을 연결된 진동계로 나타냈다. 유량 조건에 따라 날개마다 기포 크기가 번갈아 달라지는 현상이 강해졌다가 약해지고 사라지는 변화와, 기포들이 함께 커지고 작아지는 현상을 예측했다. |
| 3 | 2025 | [Analysis of Rotordynamic Stiffness Forces in a Mixed-Flow Pump With a Shrouded Impeller](https://doi.org/10.1115/1.4069436)[^p3] | 1저자 Tien-Dung Vuong · 마지막 저자 Seung Jin Song | 밀봉 틈새만 편심인 펌프와 주 회전 날개까지 편심인 펌프를 계산해 비교했다. 두 흐름 통로의 비대칭이 축에 작용하는 힘에 다르게 기여하므로 둘을 함께 고려해야 한다고 제시했다. |
| 4 | 2024 | [Impact of Additive Manufacturing Surface Roughness on the Aerodynamic Performance of Axial Compressor Blades](https://doi.org/10.1007/s42405-024-00769-7)[^p4] | 1저자 Sukhyeon Lim · 마지막 저자 Seung Jin Song | 적층 제조 표면의 거칠기가 다른 압축기 날개를 실험했다. 거칠기가 커질 때 출구 흐름 방향의 어긋남과 손실이 늘며, 그 증가가 거칠기에 단순 비례하지 않음을 보였다. |
| 5 | 2024 | [Impact of Low Freestream Turbulence and Surface Roughness on the Flat-Plate Boundary Layer Transition Under a High-Lift Airfoil Pressure Gradient](https://doi.org/10.1115/1.4065494)[^p5] | 1저자 Heechan Jeong · 마지막 저자 Seung Jin Song | 들어오는 흐름의 난류가 낮은 조건에서 표면 거칠기가 경계층 전이에 미치는 영향을 측정했다. 거칠기는 흐름이 표면에서 떨어진 영역의 크기와 전이 시점을 바꾸며, 난류가 차지하는 표면 영역과 운동량 손실에도 영향을 주었다. |
| 6 | 2024 | [Swirl Enhancement Effect on Turbine Rim Seal Performance](https://doi.org/10.1115/1.4064230)[^p6] | 1저자 Mingeun Choi · 마지막 저자 Seung Jin Song | 회전 원판에 흐름의 회전 성분을 높이는 장치를 두고 밀봉 효과를 측정했다. 원판 사이 흐름의 회전이 커지자 고온 기체 유입을 막는 데 필요한 최소 밀봉 유량이 감소했다. |
| 7 | 2022 | [Periodic Unsteady Kinematics of Hub Flows in a Shrouded Multistage Compressor](https://doi.org/10.1115/1.4053106)[^p7] | 1저자 Jaehyoung Lee · 마지막 저자 Seung Jin Song | 다단 압축기의 축 가까운 부분에서 고정 날개와 회전 날개의 후류, 밀봉 틈새의 누설 흐름이 합쳐지는 모습을 측정했다. 이 상호작용이 속도와 흐름 각도의 주기적 변동에 미치는 영향을 밝혔다. |

## 교수와 전문 분야

송성진 교수는 Duke University 기계공학·재료과학 학사, Massachusetts Institute of Technology 항공우주공학 석사와 박사 학위를 받았다. 학과 소개는 학위 연도를 학사 1986년, 석사 1988년, 박사 1995년으로 적는다. 1995–1999년 인하대학교 조교수를 지낸 뒤 1999년 서울대학교에 부임했다.[^faculty][^department]

연구실 교수 소개는 전문 분야로 터보기계 공력과 유체·구조 상호작용, 로켓 터보펌프 캐비테이션, 추진·발전 시스템 해석을 든다. 유체·구조 상호작용은 유체가 구조물에 힘을 주고 구조물의 움직임이나 변형이 다시 흐름에 영향을 주는 관계다.[^faculty] 최근 논문에서는 기포 불안정성의 모형화와 영상 식별, 펌프 편심이 만드는 힘, 날개 표면과 밀봉 흐름에 따른 손실을 다룬다.[^p1][^p2][^p3][^p4][^p6]

## 응용 분야

연구실은 항공기 추진과 발전용 가스터빈, 액체 추진 로켓의 터보펌프, 석유·가스 및 산업 공정의 원심 압축기·팽창기를 대상으로 든다. 연구 목표는 공력 손실과 불안정성을 줄이고 에너지 전환 장치의 성능을 개선하는 것이다.[^research] 재생에너지 연구는 현장 전력·열 공급 설계와 환경 목표에 따른 에너지 정책 평가를 응용 대상으로 한다.[^energy]

## 구성원

연구실의 「2025-1 Student Researchers」에 게시된 12명이다. 과정·연구 주제·학교 이메일은 게시 표기를 따른다. ‘대표 논문 참여’는 위 표의 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^staff]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 정낙신 (Nakshin Jeong) | 박사과정 | turbopump | nakshin@snu.ac.kr |  |
| Vuong Tiendung | 박사과정 | rotor dynamics of mixed flow pump | tiendung_209@snu.ac.kr |  |
| 고영언 (Youngeun Ko) | 박사과정 | surface roughness effects in turbomachine | yeko77@snu.ac.kr |  |
| 이상현 (Sanghyun Lee) | 박사과정 | machine learning in turbomachine | bear11235@snu.ac.kr | 1 |
| 장현지 (Hyunji Chang) | 박사과정 | Turbopump Inducer | hyunji0615@snu.ac.kr |  |
| 이태승 (Taeseung Lee) | 박사과정 |  | xotmdehowl@snu.ac.kr |  |
| 임준영 (Junyoung Lim) | 박사과정 | pump instability | junkoreas@snu.ac.kr |  |
| 김재훈 (Jaehun Kim) | 박사과정 | blade flutter | ehd3957@snu.ac.kr |  |
| 김도영 (Doyoung Kim) | 석사과정 | Industrial Turbomachinery | kdy873@snu.ac.kr |  |
| 구진모 (Jinmo Ku) | 석사과정 | SCO2 Compressor and Expander | jinmok@snu.ac.kr |  |
| 최현도 (Hyundo Choi) | 석사과정 | Exhaust Nozzle of Jet Engine | hyundo1113@snu.ac.kr |  |
| 이상윤 (Sangyoon Lee) | 석사과정 | Turbine Rim Seal | ghfd1234@snu.ac.kr |  |

## 졸업생 진로

연구실 Alumni에 게시된 80명의 학위·과정과 2002–2025년 연도, 진로 표기를 따른다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Kang, Janghoon (강장훈) | MS (2025) |  |
| Joo, Seongjong (주성종) | MS (2023) | Oxford university |
| Yoo, Jisang (유지상) | MS (2020) | Hyundai Motors |
| Lee, Jaehyung (이재형) | Ph.D (2019) | Hanhwa Power Systems |
| Jeong, Heechan (정희찬) | Ph.D (2019) | Korea Institute of Machinery & Materials |
| Song, Jieun (송지은) | Ph.D (2018) | Karlsruhe Institute of Technology |
| Kong, Dongjae (공동재) | MS (2018) | Republic of Korea Air Force Academy |
| choi, Yunjung (최윤정) | MS (2017) | Samsung Electro-Mechanics |
| Barratt, Dylan | MS (2015) | University of Oxford |
| Nguyen, Tien Thinh | MS (2014) | Frasen Inc. |
| Kim, Jihyeon (김지현) | BS (2014) | Korea Aerospace Industries, Ltd. |
| Jang, Semin (장세민) | MS (2012) | LG Electronics |
| Sohn, Younggee (손영기) | MS (2012) | Doosan Heavy Industries & Construction Co., Ltd. |
| Hur, InYoung (허인영) | Visiting student (2011) | University of Cambridge |
| Lee, Hyoseong (이효성) | MS (2011) | Doosan Heavy Industries Co., Ltd. |
| Back, Seungchul (백승철) | MS (2010) | Samsung Engineering Co., Ltd. |
| Kim, Jadan (김자단) | MS (2010) |  |
| Lim, Youngcheon (임영천) | MS (2010) |  |
| Yoon, Younkuk (윤영국) | Ph. D. (2024) | University of Cambridge (Postdoctoral Researcher) |
| Lee, Changyul (이창열) | MS (2023) | Hyundai Motors |
| Koo, Bonhan (구본한) | MS (2020) | Doosan Heavy Industry |
| Han, Wonseob (한원섭) | MS (2019) | Hyundai Motors |
| Yoo, Jiho (유지호) | MS (2019) | Samsung Electronics |
| Yoon, NamJun (윤남준) | MS (2018) | SFA Engineering Corp. |
| Ha, Jihun (하지훈) | MS (2017) | LIG NEXONE |
| Lee, Hochae (이호채) | Ph.D (2017) | Samsung Electronics |
| An, Youngmo (안영모) | MS (2014) | Samsung engineering |
| Shin, Juhyun (신주현) | Ph.D (2014) | Korea Aerospace Research institute |
| Kim, Dongil (김동일) | MS (2013) | Doosan Heavy Industries & Construction Co., Ltd. |
| Abid, Agha Raza | MS (2012) | Samsung Engineering Co., Ltd. |
| Bae, Hyo Jo (배효조) | MS (2012) | LG Electronics |
| Im, Juhyun (임주현) | Ph.D (2011) | Agency for Defense Development |
| Won, Hyejun (원혜준) | MS (2011) | Graduate school |
| Choi, Jungil (최정일) | MS (2010) | Kookmin University |
| Kim, Hyunjoong (김현중) | MS (2010) | Doosan Heavy Industries & Construction Co., Ltd. |
| Roh, Ujin (노유진) | MS (2010) | Doosan Heavy Industries & Construction Co., Ltd. |
| Hong, Dunam (홍두남) | Ph. D. (2024) | Samsung Electronics |
| Song, Jayeon (송자연) | MS (2022) | Hyundai Motors |
| Rhee, Jaemin (이재민) | Ph.D (2019) | Samsung Electronics |
| Song, Jeonghun (송정훈) | Ph.D (2019) | LG CNS |
| Choi, MinGeun (최민근) | MS (2019) | Republic of Korea Air Force Academy |
| Kim, Junho (김준호) | Ph.D (2018) | Samsung Electronics |
| Kim, Suyong (김수용) | MS (2017) | MIT |
| Kim, Youil (김유일) | Ph.D (2017) | Agency for Defense Development |
| Kim, Minji (김민지) | MS (2014) | Renault Samsung |
| Jang, Wonjoon (장원준) | MS (2014) |  |
| Jung, Jiyoung (정지영) | MS (2013) | Renault Samsung |
| Park, Jungchan (박정찬) | MS (2012) | Hyundai Engineering and Construction Co., Ltd. |
| Gillmeier, Conrad | Visiting student (2011) |  |
| Kim, Jinwook (김진욱) | Ph.D (2011) | Samsung Techwin Co., Ltd. |
| Yeo, Tonghyuk (여동혁) | BS (2011) | Hanwha Corporation |
| Kim, Hyerim (김혜림) | MS (2010) | Leibniz University Hannover |
| Guenther, Christoph | Visiting student (2010) |  |
| Kang, Kyungjun (강경준) | MS (2009) | Korean Atomic Energy Research Institute |
| Park, Kyungwook (박경욱) | MS (2009) | Samsung Corning Precision Materials |
| Choi, Seongwook (최성욱) | MS (2008) | Hyundai Heavy Industries Co., Ltd. |
| Lee, Sungdae (이성대) | MS (2008) | Doosan Heavy Industries & Construction Co., Ltd. |
| Cho, Seungho (조승호) | Ph.D (2007) | Samsung Techwin Co., Ltd. |
| Sohn, Junhyuk (손준혁) | MS (2007) | KAIST (MS Candidate, Financial Engineering) |
| An, Seho (안세호) | MS (2006) | Samsung Heavy Industries Co., Ltd. |
| Kim, Tongbeom (김동범) | Postdoctoral Researcher (2006) | University of the Witwatersrand (Professor) |
| Park, Hyunseong (박현성) | MS (2006) | UC Berkeley (Ph.D. Candidate) |
| Park, Kunjoong (박건중) | Ph.D (2006) | Samsung Advance Institute of Technology |
| Sohn, Daewoong (손대웅) | MS (2006) | UC Berkeley (Ph.D. Candidate) |
| Yun, Yongsang (윤용상) | Ph.D (2006) | University of Cambridge (Postdoctoral Researcher) |
| Yun, Yongil (윤용일) | Ph.D (2006) | Samsung Engineering Co., Ltd. |
| Choi, Ingee (최인지) | undergraduate (2005) | Dongbu Group |
| Choi, Kwonsick (최권식) | MS (2005) | Hyundai Motor Company |
| Kim, Hyunsik (김현식) | visiting student (2005) | Samsung Advanced Institute of Technology |
| Kim, Jinhee (김진희) | MS (2005) | Dae Dong Industrial Co., Ltd. |
| Lee, Jaeseok (이재석) | MS (2005) | Hyundai Heavy Industries Co., Ltd. |
| Lee, Sangmoo (이상무) | MS (2005) | Hyundai Motor Company |
| Seong, Sanghun (성상훈) | MS (2005) | LG Electronics |
| Jeong, Wangjo (정왕조) | MS (2004) | Samsung Heavy Industries Co., Ltd. |
| Kim, Woojun (김우준) | MS (2004) | Korean Register of Shipping |
| Kim, Youngjun (김영준) | MS (2004) |  |
| Park, Ilyoung (박일영) | MS (2004) | Samsung Techwin Co., Ltd. |
| Jeon, Byungsun (전병선) | MS (2003) | Hyundai Motor Company |
| Joo, Hyunsuk (주현석) | MS (2003) | Renault Samsung Motors (France) |
| Song, Bumho (송범호) | MS (2002) | Citi bank |

## 최근 5년 논문 목록

연구실 Journal과 Conference의 학술지·학회 논문이다. 연도와 발표처는 연구실의 구역 및 각 항목 표기를 따른다.[^journal][^conference]

**2025**

- Youngkuk Yoon, Seung Jin Song. "Impact of Flow Rate on Turbopump Inducer Blade-to-Blade Interaction During Local Cavitation Instability". *JOURNAL OF FLUIDS ENGINEERING-TRANSACTION OF THE ASME, Vol. 147(8), 081202. DOI: <https://doi.org/10.1115/1.4068040>*.
- Youngkuk Yoon, Seung Jin Song. "Model for Local Cavitation Instabilities in Two-Bladed Turbopump Inducers". *JOURNAL OF TURBOMACHINERY-TRANSACTIONS OF THE ASME, Vol.147(5), 051013. DOI: <https://doi.org/10.1115/1.4067027>*.
- Junyoung Lim, Moxiao Li, Seung Jin Song. "Impeller Wake Transport Along the Diffuser Midspan Passage of an Axial Flow Pump". *Journal of Mechanical Science and Technology, Vol. 39, pp. 275-285. DOI: <https://doi.org/10.1007/s12206-024-1226-2>*.
- Sanghyun Lee, Youngkuk Yoon, Seung Jin Song. "Deep Learning-Based Identification of Turbopump Inducer Cavitation Instability Using High-Speed Camera Images". *AIAA SciTech 2025. DOI: <https://doi.org/10.2514/6.2025-0760>*.
- Youngkuk Yoon, Seung Jin Song. "Analysis of Local Cavitation Instability Post-Onset Behaviors in Three-Bladed Turbopump Inducers". *AIAA SciTech 2025. DOI: <https://doi.org/10.2514/6.2025-0961>*.

**2024**

- Heechan Jeong, Seung Jin Song. "Impact of Low Freestream Turbulence and Surface Roughness on the Flat-Plate Boundary Layer Transition Under a High-Lift Airfoil Pressure Gradient". *JOURNAL OF TURBOMACHINERY-TRANSACTIONS OF THE ASME, Vol.146(11), 111003. DOI: <https://doi.org/10.1115/1.4065494>*.
- Sukhyeon Lim, Youngeon Ko, Dunam Hong, Myungho Kim, Seung Jin Song. "Impact of Additive Manufacturing Surface Roughness on the Aerodynamic Performance of Axial Compressor Blades". *International Journal of Aeronautical and Space Sciences, Vol, 26, pp. 42-49. DOI: <https://doi.org/10.1007/s42405-024-00769-7>*.
- Mingeun Choi, Bonhan Goo, GeonHwan Cho, Seung Jin Song. "Swirl Enhancement Effect on Turbine Rim Seal Performance". *JOURNAL OF TURBOMACHINERY-TRANSACTIONS OF THE ASME, Vol.146(5), 051002. DOI: <https://doi.org/10.1115/1.4064230>*.
- Sanghyun Lee, Changyeol Lee, Jisang Ryu, Yongsang Yoon, Seung Jin Song. "Partial Shroud Impact on the Cavitaty Flow in a Shrouded Turbine". *ISABE 2024*.
- Tien Dung Vuong, Youngkuk Yoon, Daehee Jeong, Minchul Kim, Taegyu Choi, Seung Jin Song. "Static Direct and Cross-Coupled Forces Due to Lateral Offset in a Mixed Flow Pump". *Global Power and Propulsion Technical Conference. DOI: <https://doi.org/10.33737/gpps24-tc-159>*.
- Youngeon Ko, Sukhyeon Lim, Dunam Hong, Myungho Kim, Seung Jin Song. "Effects of Additive Manufacturing-Induced Thickened Leading Edge on Aerodynamic Performance of Compressor Blade". *Asian Congress on Gas Turbines*.
- Youngkuk Yoon, Seung Jin Song. "Model for Local Cavitation Instabilities in 2-Bladed Turbopump Inducers". *ASME Turbo Expo 2024: Turbomachinery Technical Conference and Exposition. DOI: <https://doi.org/10.1115/gt2024-129494>*.

**2023**

- Youngkuk Yoon, Seung Jin Song. "Effects of Tip Leakage Vortex Caviatation on Flow Field under Cavitation Instability". *International Journal of Turbomachinery, Propulsion and Power, Vol.8(2), 17. DOI: <https://doi.org/10.3390/ijtpp8020017>*.
- Jun Young Lim, Tong Beum Kim, Seung Jin Song. "Spanwise Difference in Impeller Wake Decay Process in an Axial Flow Pump". *The 17th Asian International Conference on Fluid Machinery*.
- Youngkuk Yoon, Seung Jin Song. "Stability Analysis of the N-bladed System with Blade-to-blade Interaction". *Global Power and Propulsion Technical Conference. DOI: <https://doi.org/10.33737/gpps23-tc-163>*.
- Junyoung Lim, Youngkuk Yoon, Seung Jin Song. "Impeller Wake Transport at Mid-Span, Hub Region, and Tip Region in an Axial Flow Pump at Saddle Region". *ASM-JSME-KSME Fluids Engineering Division*.
- Dunam Hong, Minsuk Choi, Myungho Kim, Seung Jin Song. "Aerodynamic Performance in a Linear Turbine Cascade With Large Tip Clearance and Casing-side Injection". *ASME Turbo Expo 2023: Turbomachinery Technical Conference and Exposition. DOI: <https://doi.org/10.1115/gt2023-102124>*.
- Youngkuk Yoon, Seung Jin Song. "Quantification of Blade-Cavity Interaction Under Two-Bladed Inducer Alternate Blade Cavitation". *The 11th Asian Joint Conference on Propulsion and Power*.

**2022**

- Jaehyoung Lee, Sungkyung Lim, Hyoun-Woo Shin, Sungryong Lee, Seung Jin Song. "Periodic Unsteady Kinematics of Hub Flows in a Shrouded Multistage Compressor". *Journal of Engineering for Gas Turbines and Power, Vol.144(4). DOI: <https://doi.org/10.1115/1.4053106>*.
- Dongjae Kong, Seung Jin Song. "Influence of flow coefficient on unsteady impeller loading induced by impeller-diffuser interaction". *Journal of Mechanical Science and Technology, Vol.36(5). DOI: <https://doi.org/10.1007/s12206-022-0423-0>*.
- Youngkuk Yoon, Junho Kim, Seung Jin Song. "Identification of inducer cavitation instabilities using high-speed visualization". *Experimental Thermal and Fluid Science, Vol.132, 110548. DOI: <https://doi.org/10.1016/j.expthermflusci.2021.110548>*.
- Youngkuk Yoon, SangHyeon Lee, SeungJin Song. "Deep-Learning Based Identification of Inducer Cavitation Instability". *Measuring Techniques in Turbomachinery 2022. DOI: <https://doi.org/10.1088/1742-6596/2511/1/012028>*.
- Dunam Hong, SeungJin Song. "Experimental Investigation on the Effect of Downstream Casing Coolant Injection on Loss in Linear Turbine Cascade with Tip Clearance". *ISABE 2022*.
- Dunam Hong, Minsuk Choi, Myungho Kim, Seung Jin Song. "Aerodynamic Loss in a Linear Turbine Cascade with Tip Clearance and Upstream Casing Coolant Injection". *Global Power and Propulsion Technical Conference*.
- Youngkuk Yoon, SangHyeon Lee, SeungJin Song. "Effect of Flow Coefficient on Two-Bladed inducer Alternate Blade Cavitation". *Global Power and Propulsion Technical Conference. DOI: <https://doi.org/10.33737/gpps22-tc-52>*.
- Youngkuk Yoon, Seung Jin Song. "Effect of Tip Leakage Vortex Cavitation on Flow Field Under Cavitation Instability". *Conference on Modelling Fluid Flow (CMFF'22)*.
- Dunam Hong, Minsuk Choi, Myungho Kim, Seung Jin Song. "The Effect of Casing Coolant Injection on Aerodynamic Loss in a Linear Turbine Cascade With Tip Clearance". *ASME Turbo Expo 2022: Turbomachinery Technical Conference and Exposition. DOI: <https://doi.org/10.1115/gt2022-80252>*.

**2021**

- Youngkuk Yoon, Seung Jin Song. "Effects of Inlet S-duct on Inducer Performance and Cavitation Instability". *IAHR-Asia 2021. DOI: <https://doi.org/10.1088/1755-1315/1037/1/012018>*.
- Youngkuk Yoon, Seung Jin Song. "Mathematical Verification of Dual-Frequency Characteristic in Rotating Cavitations". *The 16th Asian International Conference on Fluid Machinery. DOI: <https://doi.org/10.1088/1742-6596/2217/1/012015>*.
- Youngkuk Yoon, Changkyoo Park, Seung Jin Song. "Experimental Characterization of Thermodynamic Effect on Two-Bladed Inducer Alternate Blade Cavitation". *11th International Symposium on Cavitation (CAV2021)*.

## 연락과 위치

- 교수: 송성진 · sjsong@snu.ac.kr · 02-880-1667.[^faculty]
- 연구실: 서울특별시 관악구 관악로 1 서울대학교 301동 1212호(02-880-1701), 1415호(02-880-1644), 우편번호 08826.[^contact]
- 교수 사무실: 301동 1417호. 학과 소개는 연구실 위치에 312동 106호와 313동 223호도 적는다.[^department]
[^about]: Turbomachinery Laboratory, About TML. <https://tml.snu.ac.kr/> 관측 2026-11-11.

[^faculty]: Turbomachinery Laboratory, Faculty. <https://tml.snu.ac.kr/faculty> 관측 2026-11-11.

[^department]: 서울대학교 기계공학부, 송성진 교수 소개. <https://me.snu.ac.kr/snu__professor/%ec%86%a1%ec%84%b1%ec%a7%84-song-seung-jin/> 관측 2026-11-11.

[^research]: Turbomachinery Laboratory, Research. <https://tml.snu.ac.kr/research> 관측 2026-11-11.

[^compressor]: 축류 압축기 안정성 연구. <https://tml.snu.ac.kr/axial-compressor-stability> 관측 2026-11-11.

[^wake]: 다단 압축기 비정상 흐름 연구. <https://tml.snu.ac.kr/unsteady-3-d> 관측 2026-11-11.

[^humidity]: 천음속 압축기의 습도 영향 연구. <https://tml.snu.ac.kr/humidity-effect-transonic> 관측 2026-11-11.

[^roughness]: 저압 터빈의 경계층 전이 연구. <https://tml.snu.ac.kr/roughness-turbine-blade> 관측 2026-11-11.

[^leakage]: 터빈의 누설 흐름과 주 흐름 상호작용 연구. <https://tml.snu.ac.kr/flow-interaction> 관측 2026-11-11.

[^purge]: 터빈 원판 공간과 림실 유동 연구. <https://tml.snu.ac.kr/purge-flow> 관측 2026-11-11.

[^shroud]: 터빈 부분 슈라우드 연구. <https://tml.snu.ac.kr/parial-shroud> 관측 2026-11-11.

[^sco2]: 이산화탄소 터빈 성능 연구. <https://tml.snu.ac.kr/sco2> 관측 2026-11-11.

[^cavitation]: 로켓 터보펌프 인듀서 캐비테이션 연구. <https://tml.snu.ac.kr/cavitation-instability> 관측 2026-11-11.

[^laser]: 레이저 유도 캐비테이션 연구. <https://tml.snu.ac.kr/laser> 관측 2026-11-11.

[^forced]: 원심 압축기 날개의 강제 응답 연구. <https://tml.snu.ac.kr/forced-response-1> 관측 2026-11-11.

[^rotordynamic]: 원심 압축기의 비축대칭 흐름과 회전축 유체력 연구. <https://tml.snu.ac.kr/non-axisymmetric-flow-field> 관측 2026-11-11.

[^condensation]: 반경 방향 팽창기의 응축 영향 연구. <https://tml.snu.ac.kr/condensation-radial-expander> 관측 2026-11-11.

[^energy]: 재생에너지 통합 공급 시스템 최적화 연구. <https://tml.snu.ac.kr/energy-optimization> 관측 2026-11-11.

[^staff]: Turbomachinery Laboratory, 2025-1 Student Researchers. <https://tml.snu.ac.kr/staff> 관측 2026-11-11.

[^alumni]: Turbomachinery Laboratory, Alumni. <https://tml.snu.ac.kr/alumni> 관측 2026-11-11.

[^journal]: Turbomachinery Laboratory, Journal. <https://tml.snu.ac.kr/journal> 관측 2026-11-11.

[^conference]: Turbomachinery Laboratory, Conference 2021~. <https://tml.snu.ac.kr/복제-conference-2016-2020> 관측 2026-11-11.

[^contact]: Turbomachinery Laboratory, Contact Us. <https://tml.snu.ac.kr/contact-us> 관측 2026-11-11.

[^p1]: S. Lee, Y. Yoon, S. J. Song, Journal of Fluids Engineering (2026). <https://doi.org/10.1115/1.4071348> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101125852,publication_year:2021-2026> 관측 2026-11-11.

[^p2]: Y. Yoon, S. J. Song, Journal of Turbomachinery 147, 051013 (2025). <https://doi.org/10.1115/1.4067027> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101125852,publication_year:2021-2026> 관측 2026-11-11.

[^p3]: T.-D. Vuong 외, S. J. Song, Journal of Fluids Engineering (2025). <https://doi.org/10.1115/1.4069436> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101125852,publication_year:2021-2026> 관측 2026-11-11.

[^p4]: S. Lim 외, S. J. Song, International Journal of Aeronautical and Space Sciences 26, 42-49 (2024). <https://doi.org/10.1007/s42405-024-00769-7> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101125852,publication_year:2021-2026> 관측 2026-11-11.

[^p5]: H. Jeong, S. J. Song, Journal of Turbomachinery 146, 111003 (2024). <https://doi.org/10.1115/1.4065494> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101125852,publication_year:2021-2026> 관측 2026-11-11.

[^p6]: M. Choi, B. Goo, G. Cho, S. J. Song, Journal of Turbomachinery 146, 051002 (2024). <https://doi.org/10.1115/1.4064230> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101125852,publication_year:2021-2026> 관측 2026-11-11.

[^p7]: J. Lee 외, S. J. Song, Journal of Engineering for Gas Turbines and Power 144 (2022). <https://doi.org/10.1115/1.4053106> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101125852,publication_year:2021-2026> 관측 2026-11-11.

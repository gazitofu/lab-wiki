# Turbulence, Flow Control & CFD Laboratory / Bio-Mimetic Engineering Laboratory

**서울대학교 공과대학 기계공학부 · 최해천 석좌교수**

- 영문 이름: Turbulence, Flow Control & CFD Laboratory / Bio-Mimetic Engineering Laboratory
- 분야: 난류의 예측과 제어, 생체모방공학, 전산유체역학[^r101]
- 대분야: 기계·로봇·제조
- 태그: 유체역학·유동[^r101][^r102], 설계 최적화(위상·형상 최적화)[^r133], 진동·소음 공학[^r102]
- 홈페이지: <https://tfc.snu.ac.kr/>
- 근거와 출처: [TFC & BME 근거 페이지](tfc-sources.md)

> 공기와 물의 복잡한 흐름을 계산하고, 표면 구조와 날개 모양을 바꾸어 물체가 받는 저항과 흐름에서 생기는 소음을 줄이는 방법을 연구한다.[^r101][^r102][^r133]

## 무엇을 연구하나

이 연구실은 난류(속도와 방향이 불규칙하게 변하며 여러 크기의 회전 운동이 섞이는 흐름)의 원리를 실험과 계산으로 밝힌다. 물체가 흐름 속에서 받는 항력(물체와 유체의 상대 운동을 방해하는 방향으로 작용하는 힘)을 줄이는 방법을 개발한다. 전산유체역학(공기와 물의 운동을 나타내는 식을 수치 계산으로 푸는 분야)에서는 복잡한 물체 안팎의 흐름을 빠르고 정확하게 계산하는 방법도 다룬다.[^r101]

다른 갈래는 생체모방공학(생물의 구조와 작동 원리를 공학 문제 해결에 활용하는 분야)이다. 상어 피부의 홈, 돌고래를 본뜬 유연한 표면, 식물 줄기와 조개껍데기의 구조를 살펴 물체 표면의 마찰과 모양 때문에 생기는 저항을 줄이고자 한다. 생물의 날개 형태와 움직임을 분석해 비행 성능을 높이는 연구도 한다.[^r103][^r133][^r134]

이러한 방법을 차량, 골프공, 날개, 팬과 펌프의 흐름에 연결한다. 의료 응용에서는 관상동맥(심장 근육에 혈액을 공급하는 동맥)의 혈관 구조와 좁아진 부분의 모양이 그곳의 압력 손실에 미치는 영향을 다룬다. 최근 논문에서는 혈관이 좁아지지 않은 구간의 압력 손실도 반영하는 새 계산식을 유도했다.[^r104][^f157] 연구실의 중심 방법은 흐름의 물리적 원리를 밝히고 이를 계산과 제어 방법으로 만드는 것이다.[^r101]

## 주요 연구 주제

### 난류를 예측하는 계산 모형

큰 와류 모사(흐름의 큰 회전 구조는 직접 계산하고 작은 구조의 영향은 모형으로 처리하는 방법)의 정확도와 계산 효율을 함께 높이는 방법을 개발한다. 기계학습(자료에서 규칙을 배워 예측이나 판단을 수행하는 계산 방법)으로 난류를 예측하고, 계산에서 직접 표현하지 못하는 작은 흐름의 영향을 모형화한다. 예측한 흐름을 바탕으로 저항을 줄이는 제어도 연구한다.[^r102][^r132]

### 표면 구조와 공기 분사로 흐름 제어

물체 주변으로 공기를 분사하거나 표면에 홈과 부착물을 두어 흐름을 바꾸는 방법을 다룬다. 구·원기둥·차량 모형에 능동적인 입력을 주는 방법과, 표면 구조를 이용하는 방법을 함께 연구한다. 흐름 때문에 생기는 소음을 줄이는 체계적인 유동제어 방법도 개발한다.[^r131][^r102]

### 생물에서 착안한 날개와 형상 설계

혹등고래 지느러미의 앞쪽 돌기, 장수풍뎅이의 날개, 날치의 날개 형태, 나비의 뒷날개 꼬리를 대상으로 형상과 공기 흐름의 관계를 살핀다. 제자리 비행에서는 필요한 동력(단위 시간에 전달되거나 소비되는 에너지)을 최소화하는 날개 모양과 움직임을 찾는 설계 최적화를 연구한다.[^r133]

### 서로 다른 물질과 변형되는 구조물이 있는 흐름

다상 유동(액체와 기체 등 서로 구분되는 물질 상태가 함께 움직이는 흐름)을 계산하고, 기포가 섞인 물과 기름·물의 흐름을 다룬다. 유체·구조 상호작용(흐름이 구조물에 힘을 가하고 구조물의 변형과 운동이 다시 흐름을 바꾸는 현상)을 계산에 반영하는 방법도 연구한다.[^r102]

## 대표 논문

서울대 재직 시기의 논문에서 기본 유동, 난류 모형, 기포 흐름, 생체모방 표면과 장치, 날개 설계, 구조물 진동, 유동제어를 보여 주는 여덟 편을 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Flow characteristics past a normal flat plate at Re = 5–10 000](https://doi.org/10.1063/5.0335953) · Physics of Fluids | 흐름을 정면으로 받는 평판 뒤에서 흐름이 어떻게 바뀌는지 계산했다. 레이놀즈수(흐름이 운동 상태를 유지하려는 영향과 유체 내부 마찰의 영향의 비를 나타내는 값)를 바꾸며 일정한 흐름이 시간에 따라 변하고, 입체적인 흐름과 난류로 바뀌는 과정을 구분했다. 연구에서 살핀 높은 레이놀즈수 구간에서는 평균 항력 등 일부 평균값이 레이놀즈수에 거의 의존하지 않았다.[^p1] | 1저자 Daeun Song, 마지막 저자 최해천 |
| 2 | 2024 | [A recursive neural-network-based subgrid-scale model for large eddy simulation: application to homogeneous isotropic turbulence](https://doi.org/10.1017/jfm.2024.992) · Journal of Fluid Mechanics | 신경망(자료의 입력과 출력 관계를 계산 단위 사이의 연결 강도로 학습하는 모형)으로 계산에 드러나지 않는 작은 난류의 영향을 예측한다. 먼저 낮은 레이놀즈수의 정밀 계산 자료로 학습하고, 높은 레이놀즈수의 큰 와류 모사에 적용한 다음 그 결과를 학습 자료에 보태 모형을 갱신한다. 이를 반복해 넓어진 계산 간격에도 적용하도록 했으며, 공간과 방향에 따른 통계적 차이가 없는 난류의 예측에 적용했다.[^p2] | 1저자 Chonghyuk Cho, 마지막 저자 최해천 |
| 3 | 2024 | [A numerical study on the turbulence characteristics in an air–water upward bubbly pipe flow](https://doi.org/10.1017/jfm.2024.652) · Journal of Fluid Mechanics | 관 안에서 물과 함께 올라가는 공기 방울이 흐름과 관 벽에 주는 영향을 계산했다. 연구 조건에서는 벽 근처 기포가 주로 벽에 부딪힌 뒤 튕겨 나갔고, 뒤에 생기는 회전 흐름이 빠른 물을 벽으로 보내 마찰을 키웠다. 기포 때문에 생기는 난류와 속도 차이로 생기는 난류의 상호작용을 반영한 평균 흐름 모형도 제안했다.[^p3] | 1저자 Ingu Lee, 마지막 저자 최해천 |
| 4 | 2024 | [Effect of the yaw angle on the riblet performance](https://doi.org/10.1063/5.0210054) · Physics of Fluids | 리블렛(물체 표면에 나란히 만든 미세한 홈과 돌기 구조)의 방향이 흐름 방향과 어긋날 때 저항 저감 효과가 어떻게 바뀌는지 계산했다. 연구 조건에서는 어긋난 각도가 20도보다 작을 때 항력이 줄었다. 각도가 커지면 표면 마찰 감소보다 물체 모양으로 생기는 항력 증가가 커져 전체 항력이 늘어나는 원리를 분석했다.[^p4] | 1저자 Jonghwan Park, 마지막 저자 최해천 |
| 5 | 2024 | [Aerodynamic performance enhancement of a vertical-axis wind turbine by a biomimetic flap](https://doi.org/10.1088/1748-3190/ad9a45) · Bioinspiration & Biomimetics | 새가 착륙할 때 깃털을 움직이는 모습에서 착안해, 회전축이 수직인 풍력 터빈 날개 안쪽에 주변 흐름에 따라 저절로 펼쳐지는 판을 달았다. 바깥에서 별도의 동력을 공급하지 않고 작동한다. 판을 달아도 날개 자체의 회전력은 변하지 않았으며, 판이 추가 회전력을 만들어 전체 성능이 좋아졌다. 부착 위치와 회전 조건에 따라 효과가 달라졌다.[^p5] | 1저자 Sangwoo Ahnn, 마지막 저자 최해천 |
| 6 | 2025 | [Neural-network-based optimization of the wing kinematics and geometry of a hovering flapping flight](https://doi.org/10.1063/5.0256748) · Physics of Fluids | 초파리의 제자리 비행과 비슷한 조건에서 동력 소비를 최소화하는 날개 모양과 움직임을 찾았다. 계산 자료로 학습한 신경망이 시간에 따른 공기력과 회전력의 계수를 예측하게 하고 이를 설계에 이용했다. 최적 날개 형태는 초파리 날개와 비슷했으며, 날개가 기본 운동면 밖으로 벗어나는 움직임을 허용한 설계가 이를 금지한 설계보다 동력을 적게 썼다.[^p6] | 1저자 Hyeoksu Lee, 마지막 저자 최해천 |
| 7 | 2022 | [Vertical and torsional vibrations before the collapse of the Tacoma Narrows Bridge in 1940](https://doi.org/10.1017/jfm.2022.748) · Journal of Fluid Mechanics | 타코마 다리가 붕괴하기 전의 상하 움직임과 비틀림을 흐름과 구조물 운동이 서로 영향을 주는 계산으로 재현했다. 실제 다리의 구조 값을 쓰되 사고 당시보다 낮은 레이놀즈수와 조정한 유체 성질을 사용했다. 상하 진동이 충분히 커진 뒤 공기력과 구조물 운동의 상호작용으로 비틀림 진동이 자라는 과정을 보였고, 계산한 진동의 파장과 진동수가 당시 기록과 잘 맞았다.[^p7] | 1저자 Daeun Song, 마지막 저자 최해천 |
| 8 | 2021 | [Modification of flow behind a circular cylinder by steady and time-periodic blowing](https://doi.org/10.1063/5.0067706) · Physics of Fluids | 원기둥 표면에서 공기를 계속 분사하거나 주기적으로 분사해 뒤쪽 흐름과 저항을 바꿨다. 계속 분사할 때는 나뉜 구멍으로 분사하는 방식이 균일하게 분사하는 방식보다 항력 저감에 효과적이었다. 주기적으로 분사할 때는 균일 분사가 더 효과적이었으며, 뒤쪽 회전 흐름이 분사에 맞춰 움직이는 방식에 따라 저항이 크게 줄거나 늘었다.[^p8] | 1저자 Zhi Jun Wu, 마지막 저자 최해천 |

## 교수와 전문 분야

최해천 교수의 전공은 유체역학이다. 서울대학교 기계공학과에서 1985년 학사와 1987년 석사를 받고, 1992년 Stanford University에서 기계공학 박사학위를 받았다. 학과 소개는 1993년부터 서울대학교에서 전임강사·조교수·부교수·교수로 재직했다고 적는다. 연구실 경력에는 1993–1995년 전임강사, 1995–1999년 조교수, 1999–2004년 부교수, 2004년부터 교수로 기재되어 있다.[^dept][^r105][^r135]

난류의 물리적 원리를 실험과 계산으로 밝히고, 관찰·수학 이론·생체모방을 바탕으로 흐름을 제어하는 방법을 개발한다. 2021–2023년 서울대학교 연구부총장 겸 대학원장을 지냈으며, 학과 소개에는 2015년부터 Journal of Fluid Mechanics 편집인으로 적혀 있다.[^r101][^dept]

## 응용 분야

차량과 날개의 공기 저항, 골프공의 비행 성능, 스키점프 자세, 팬과 펌프 내부 흐름이 연구실이 제시한 응용 대상이다. 생체모방 구조를 이용한 차량 저항 저감과 날개 끝 부착물을 통한 저항 저감도 소개한다.[^r104] 수직축 풍력 터빈의 성능을 개선하는 생체모방 장치는 대표 논문 5에서 다룬다.[^p5]

## 구성원

연구실의 Research Fellows 3명, Ph.D. Students 3명, Combined MS-Ph.D.Students 3명, Master Students 구획 5명이다. Master Students 구획의 Intern 표시는 이름에 적힌 그대로 두었다. 「대표 논문 참여」는 전체 저자 이름과 같은 이름의 구성원을 같은 사람으로 보아 표시했다.[^m107][^m108][^m109][^m110]

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Ahnn, Sangwoo | 연구원 | james406@snu.ac.kr | 5 |
| Park, Jonghwan | 연구원 | lkjmn123@snu.ac.kr | 2, 4 |
| Cho, Chonghyuk | 연구원 | chonghyuk3@snu.ac.kr | 2 |
| Kim, Jonghyun | 박사과정 | kjhyuns92@snu.ac.kr |  |
| Zhang, Ziyang (visiting student from HIT) | 박사과정 (visiting student from HIT) | 21B933009@stu.hit.edu.cn |  |
| Wang, Jian (visiting student from HIT) | 박사과정 (visiting student from HIT) | 22b933021@stu.hit.edu.cn |  |
| Kim, Changbeom | 석박사통합과정 | knight627@snu.ac.kr |  |
| Yun, Jongheon | 석박사통합과정 | jordan21@snu.ac.kr |  |
| Yoon, Young Jin | 석박사통합과정 |  |  |
| So, Jiwon (Intern) | 인턴 |  |  |
| Son, Seungwoo | 석사과정 |  |  |
| Kim, Daehan (Intern) | 인턴 | daehankim001@snu.ac.kr |  |
| You, Minwoo (Intern) | 인턴 | andy021127@snu.ac.kr |  |
| Kim, Huiung (Intern) | 인턴 | danax@snu.ac.kr |  |

## 졸업생과 이전 구성원

연구실의 Ph.D. Graduates 52행, MS Graduates 83행, Former Postdoctoral Fellows 37행을 합친 172행이다. 학위·과정과 연도, 진로는 각 구획의 게시 표기다. 같은 사람이 여러 과정이나 이전 구성원 구획에 반복될 수 있다.[^a111][^a139][^a140]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Song, Daeun | Ph.D. Graduates (2026.02) | Senior Researcher, Samsung Electronics |
| Cho, Chonghyuk | Ph.D. Graduates (2025.08) | Postdoctoral Fellow, Seoul National University |
| Kim, Myunghwa | Ph.D. Graduates (2025.08) | Senior Researcher, SK hynix |
| Lee, Ingu | Ph.D. Graduates (2025.02) | Senior Researcher, Hyundai Motors |
| Ahnn, Sangwoo | Ph.D. Graduates (2025.02) | Postdoctoral Fellow, Seoul National University |
| Jung, Hyunwoo | Ph.D. Graduates (2024.08) | Senior Researcher, Samsung Electronics |
| Chang, Jaehee | Ph.D. Graduates (2022.02) | Senior Researcher, Samsung Advanced Institute of Technology |
| Jin, Dohyun | Ph.D. Graduates (2022.02) | Senior Researcher, Samsung Electronics |
| Park, Jonghwan | Ph.D. Graduates (2021.08) | Postdoctoral Fellow, Seoul National University |
| Kye, Beomjun | Ph.D. Graduates (2021.08) | Senior Researcher, SK hynix |
| Kim, Hyunsik | Ph.D. Graduates (2021.02) | Support Engineer, Siemens Industry Software |
| Kim, Jaerim | Ph.D. Graduates (2020.02) | Senior Researcher, Samsung Electronics |
| Oh, Sehyeong | Ph.D. Graduates (2020.02) | Senior Researcher, Samsung Advanced Institute of Technology |
| Kim, Dongri | Ph.D. Graduates (2020.02) | Senior Researcher, Samsung Electronics |
| Cho, Seunghyun | Ph.D. Graduates (2019.02) | Senior Researcher, Doosan Heavy Industries |
| Kim, Heesu | Ph.D. Graduates (2019.02) | Senior Researcher, Samsung Electronics |
| Lee, Hongkwon | Ph.D. Graduates (2019.02) | Senior Researcher, SEMES |
| Park, Keuntae | Ph.D. Graduates (2019.02) | Senior Researcher, LG Electronics |
| Kim, Kiyoung | Ph.D. Graduates (2018.08) | CEO, Artificial Society Inc. |
| Bang, Kyeongtae | Ph.D. Graduates (2017.08) | Senior Researcher, Samsung Eletronics |
| Cho, Minjeong | Ph.D. Graduates (2017.08) | Senior Researcher, Korea Institute of Energy Research |
| Kim, Woojin | Ph.D. Graduates (2017.08) | Senior Researcher, Samsung Electronics |
| Lee, Injae | Ph.D. Graduates (2016. 08) | Senior Researcher, Samsung Electronics |
| Jung, Taeyong | Ph.D. Graduates (2016. 02) | Senior Researcher, LG Electronics |
| Kim, Jooha | Ph.D. Graduates (2015. 02) | Assistant Professor, Ulsan National Institute of Science and Technology (UNIST) |
| Kim, Euiyoung | Ph.D. Graduates (2015. 02) | Senior Researcher, Samsung Electro-Mechanics |
| Son, Donggun | Ph.D. Graduates (2014. 02) | Senior Researcher, Korea Atomic Energy Research Institute |
| Kweon, Jihoon | Ph.D. Graduates (2011. 02) | Research Professor, Asan Medical Center/University of Ulsan |
| Lee, Jungil | Ph.D. Graduates (2010.08) | Associate Professor, Ajou University |
| Park, Hyungmin | Ph.D. Graduates (2010. 02) | Associate Professor, Seoul National University |
| Sagong, Woong | Ph.D. Graduates (2010. 02) | Senior Researcher, Agency for Defense Development |
| Jeon, Seung | Ph.D. Graduates (2009. 08) | The Korean Intellectual Property Office |
| Yi, Wook | Ph.D. Graduates (2007. 08) | Senior Researcher, LG electronics |
| Kim, Chulkyu | Ph.D. Graduates (2007. 08) | Senior Researcher, Samsung Electro-Mechanics |
| Choi, Jin | Ph.D. Graduates (2007. 08) | Senior Researcher, Agency for Defense Development |
| Bae, Joonghun | Ph.D. Graduates (2007. 08) | Senior Researcher, Korean Air |
| Kim, Jinsung | Ph.D. Graduates (2005. 08) | Senior Researcher, LG electronics |
| Kim, Jungwoo | Ph.D. Graduates (2005. 02) | Associate Professor, Seoul National University of Science and Technology |
| Park, Noma | Ph.D. Graduates (2003. 08) | Senior Researcher, LG Electronics |
| Ahn, Joon | Ph.D. Graduates (2003. 08) | Associate Professor, Kookmin University |
| Yun, Giwoong | Ph.D. Graduates (2004. 02) | The Korean Intellectual Property Office |
| Park, Jeongyoung | Ph.D. Graduates (2002. 02) | Senior Researcher, Hyundai Mobis |
| Lim, Seokhyun | Ph.D. Graduates (2002. 02) | Senior Researcher, Samsung Electronics |
| Jeon, Sejeong | Ph.D. Graduates (2002. 02) | Head director, Techmetrix Inc. |
| Hahn, Seonghyeon | Ph.D. Graduates (2002. 02) | CFD Engineer, Vestas Technology R&D, Denmark |
| Min, Taegee | Ph.D. Graduates (2001. 02) | Director at S & H Ltd. |
| Kim, Dongjoo | Ph.D. Graduates (2001. 08) | Professor, Mechanical Engineering Kumoh National Institute of Technology |
| You, Jongwoo | Ph.D. Graduates (2000) | RIST |
| Kang, Hyung Suk | Ph.D. Graduates (1998) | Senior Research Scientist, The Johns Hopkins University |
| Cho, Sung Kwon | Ph.D. Graduates (1998) | Associate Professor, Mechanical Engineering, University of Pittsburgh |
| Choi, Myung-Ryul | Ph.D. Graduates (1998) | Senior Engineer, Samsung Electronics |
| Yang, Joon Mo | Ph.D. Graduates (1996. 08) | Sr.Engineer, Microfluidics & BioMEMS Fluidics & Device Systems Applied Biosystems |
| Na, Hyunsoo (Intern) | MS Graduates (2026.08) | Ph. D. Student, Massachusetts Institute of Technology |
| Lee, Gihwan | MS Graduates (2026.02) | Samsung Electronics |
| Kim, Ukjin | MS Graduates (2024.02) | LG Energy Solution |
| Oh, Hyejeong | MS Graduates (2023.02) | Engineer, Samsung Electronics |
| Lee, Hyeoksu | MS Graduates (2022.02) | Ph. D. Student, California Institute of Technology |
| Kim, Hyeongmin | MS Graduates (2019.02) | Hyundai Motors |
| Kim, Jonghyun | MS Graduates (2019.02) | Hyundai Heavy Industry |
| Yoon, Won Hyuck | MS Graduates (2018.02) | OUaR LaB |
| Kim, Sohee | MS Graduates (2018.02) | Samsung Electronics |
| Sung, Changwoo | MS Graduates (2017. 08) | LG Eletronics |
| Chang, Jaehee | MS Graduates (2017. 02) | Senior Researcher, Samsung Advanced Institute of Technology |
| Kim, Hanbyeol | MS Graduates (2017. 02) | Samsung Electronics |
| Oh, SeungYoung | MS Graduates (2016. 02) | Control Works, Inc. |
| Yi, Hansol | MS Graduates (2016. 02) | NCSOFT |
| Kim, Gyutae | MS Graduates (2016. 02) | Continental AG |
| Kim, Jiyoo | MS Graduates (2016. 02) | Korea Aerospace Research Institute |
| Cheon, Somin | MS Graduates (2016. 02) | Samsung Electronics |
| Ahn, Eunhye | MS Graduates (2014. 02) | PH. D. Student, University of Michigan |
| Jung, Minuk | MS Graduates (2013. 08) | Korea Electric Power Research Institute |
| Kim, Heesu | MS Graduates (2013. 08) | Senior Researcher, Samsung Electronics |
| Shin, Hoonjae | MS Graduates (2013. 02) | Midasit |
| Lim, Changwon | MS Graduates (2013. 02) | Agency for Defense Development |
| Kim, Jieun | MS Graduates (2013. 02) | Hyundai Motors |
| Jang, Yunsik | MS Graduates (2012. 08) | Hyundai Motors |
| Lee, Jaemyeong | MS Graduates (2012. 08) | Hyungdai Motor Group |
| Lee, Hoon | MS Graduates (2012. 08) | Roland Berger |
| Lee, Jongoh | MS Graduates (2012. 08) | PH. D. Student, Texas A&M University |
| Je, Duho | MS Graduates (2012. 02) | Korean Military Academy |
| Kim, Jinseok | MS Graduates (2011. 02) | Judicial Research & Training Inistitute |
| Jang, Sungil | MS Graduates (2011. 02) | Researcher, Hyundai Mobis |
| Park, Keuntae | MS Graduates (2010. 08) | Senior Researcher, LG Electronics |
| Kwak, Namhyuk | MS Graduates (2010. 08) | Samsung Electronics |
| Son, Donggun | MS Graduates (2010. 02) | Senior Researcher, Korea Atomic Energy Research Institute |
| Kim, Taehoon | MS Graduates (2009. 08) | Researcher, Hyundai Mortors Company |
| Seong, Jongkook | MS Graduates (2009. 02) | Researcher, Posco Energy |
| Moon, Sunghyun | MS Graduates (2009. 02) | Researcher, Hyundai Heavy Industries |
| Lee, Daeil | MS Graduates (2009. 02) | Researcher, Korean Air |
| Lee, Jongho | MS Graduates (2008. 08) | Assistant Professor, University of British Columbia |
| Seo, Sungki | MS Graduates (2008. 08) | Researcher, Hyundai Mortors Company |
| Kim, Hoondo | MS Graduates (2008. 02) | Researcher, Renault Samsung Motors Company |
| Choi, Sangho | MS Graduates (2008. 02) | School of Dentistry, Seoul National University |
| Lee, Byoungdo | MS Graduates (2007. 08) | Researcher, Hynix Semiconductor Inc. |
| Lee, Sungwon | MS Graduates (2007. 02) | Senior Researcher, Korea Shipbuilding & Offshore Engineering |
| Kim, Juhyun | MS Graduates (2007. 02) | Researcher, Hyosung Heavy Industry |
| Son, Kwangmin | MS Graduates (2007. 02) | CEO, PhAST |
| Hwang, Gyudeok | MS Graduates (2006. 08) | Researcher, Samsung Electronics Co.Ltd |
| Bae, Kisoo | MS Graduates (2006. 02) | Senior Researcher, Hyundai Motors Company |
| Moon, Shin-Il | MS Graduates (2006. 02) | Senior Researcher, Hyundai Motors Company |
| Hwang, Yongyeon | MS Graduates (2005. 08) | Assistant Professor, Imperial College London |
| Yun, Jieun | MS Graduates (2005. 02) |  |
| Lee, Euisung | MS Graduates (2005. 02) | Researcher, Hyundai Mobis |
| Jang, Hyunchul | MS Graduates (2004. 08) | PH. D. Student, University of Minnesota |
| Kim, Dokyun | MS Graduates (2004. 02) | Assistant Professor, Hongik University |
| Lee, Dongkon | MS Graduates (2004. 02) | Senior Researcher, Hyundai Motors Company |
| Cha, Seong Dae | MS Graduates (2003. 02) | Hyundai Motors |
| Chang, Woongjae | MS Graduates (2003. 08) | Assistant Engineer, Digital Media Business Samsung Electronics Co.Ltd |
| Choi, Hyungseok | MS Graduates (2003. 02) | Researcher, Samsung Electronics Co.Ltd |
| Kang, Eun-Gu | MS Graduates (2003. 02) |  |
| Kim, Jeong-lae | MS Graduates (2003. 02) | Assistant Professor, Arizona State University |
| Kang, Wonho | MS Graduates (2002. 02) | Research Engineer, MANDO Corp. |
| Lee, Choongyeop | MS Graduates (2002. 02) | Assistant Professor, Kyunghhee University |
| Park, Hyunwook | MS Graduates (2002. 02) | Senior Researcher, Hyundai Motors |
| Yi, Wook | MS Graduates (2001. 02) | Senior Researcher, LG electronics |
| Kim, Jinsung | MS Graduates (2001. 02) | Senior Researcher, LG electronics |
| Kim, Jungwoo | MS Graduates (2001. 02) | Associate Professor, Seoul National University of Science and Technology |
| Choi, Sungho | MS Graduates (2001. 02) | Research Engineer, Dasan Networks, INC. |
| Kim, Chulkyu | MS Graduates (2000. 02) | Senior Researcher, Samsung Electro-Mechanics |
| Yun, Giwoong | MS Graduates (2000. 02) | The Korean Intellectual Property Office |
| Choi, Jin | MS Graduates (2000. 02) | Senior Researcher, Agency for Defense Development |
| Shim, Jeongsup | MS Graduates (2000. 02) | Postdoctoral Research Fellow, Genentech |
| Choi, Byunggwi | MS Graduates (1999. 02) | Senior Researcher, Hyundai Motors |
| Choi, Joonhyuk | MS Graduates (1999. 02) |  |
| Je, Jongdoo | MS Graduates (1999. 02) | Researcher, Hyundai Mobis |
| Kang, Seongwon | MS Graduates (1999. 02) | Associate Professor, Sogang University |
| Jeon, Sejeong | MS Graduates (1998) | Head director, Techmetrix Inc. |
| Lee, Donghoon | MS Graduates (1998. 02) | SIMON International Patent&Trademark Law Office |
| You, Donghyun | MS Graduates (1998. 02) | Associate Professor, POSTECH |
| Min, Chulhong | MS Graduates (1998. 02) | Senior Researcher, Hyundai Motors |
| Lim, Seokhyun | MS Graduates (1997. 02) | Senior Researcher, Samsung Electronics |
| Park, Jeongyoung | MS Graduates (1997. 02) | Senior Researcher, Hyundai Mobis |
| Hahn, Seonghyeon | MS Graduates (1997. 02) | CFD Engineer, Vestas Technology R&D, Denmark |
| Kwon, Kiyoung | MS Graduates (1996. 02) | Senior Researcher, Hyundai Motors |
| Lim, Junwoo | MS Graduates (1996. 02) | Senior Scientific Specialist, Pittsburgh Supercomputing Center |
| Park, Jonghwan | Former Postdoctoral Fellows (2021-22) | Senior Researcher, Hyundai Motors |
| Wu, Zhi | Former Postdoctoral Fellows (2019-21) | Assistant Professor, Harbin Institute of Technology (Shenzhen) |
| Kim, Hyunsik | Former Postdoctoral Fellows (2021) | Support Engineer, Siemens Industry Software |
| Kim, Jaerim | Former Postdoctoral Fellows (2020-21) | Senior Researcher, Samsung Electronics |
| Oh, Sehyeong | Former Postdoctoral Fellows (2020) | Senior Researcher, Samsung Advanced Institute of Technology |
| Kim, Dongri | Former Postdoctoral Fellows (2020) | Senior Researcher, Samsung Electronics |
| Lee, Hongkwon | Former Postdoctoral Fellows (2019) | Senior Researcher, SEMES |
| Kim, Woojin | Former Postdoctoral Fellows (2017-18) | Senior Researcher, Samsung Electronics |
| Kim, Kiyoung | Former Postdoctoral Fellows (2018) | CEO, Artificial Society Inc. |
| Cho, Minjeong | Former Postdoctoral Fellows (2017) | Senior Researcher, Korea Institute of Energy Research |
| Lee, Injae | Former Postdoctoral Fellows (2016-17) | Senior Researcher, Samsung Electronics |
| Kim, Jooha | Former Postdoctoral Fellows (2015) | Assistant Professor, Ulsan National Institute of Science and Technology (UNIST) |
| Kweon, Jihoon | Former Postdoctoral Fellows (2011-13) | Research Professor, Asan Medical Center/University of Ulsan |
| Lee, Jungil | Former Postdoctoral Fellows (2010) | Associate Professor, Ajou University |
| Park, Hyungmin | Former Postdoctoral Fellows (2010-11) | Associate Professor, Seoul National University |
| Sagong, Woong | Former Postdoctoral Fellows (2010-11) | Senior Researcher, Agency for Defense Development |
| Lee, Sang Im | Former Postdoctoral Fellows (2008-15) | Assistant Professor, Daegu Gyeongbuk Institute of Science and Technology (DGIST) |
| Yi, Wook | Former Postdoctoral Fellows (2007-08) | Senior Researcher, LG electronics |
| Kim, Jungwoo | Former Postdoctoral Fellows (2005-06) | Associate Professor, Seoul National University of Science and Technology |
| Jeon, Woopyung | Former Postdoctoral Fellows (2006) |  |
| Bae, Joonghun | Former Postdoctoral Fellows (2005) | Senior Researcher, Korean Air |
| Lee, Moonjoo | Former Postdoctoral Fellows (2005) |  |
| Park, Noma | Former Postdoctoral Fellows (2004-05) | Senior Researcher, LG electronics |
| Park, Jinil | Former Postdoctoral Fellows (1999) | Professor, Mechanical Engineering, Ajou University |
| Park, Jeongyoung | Former Postdoctoral Fellows (2002) | Senior Researcher, Hyundai Mobis |
| Min, Taegee | Former Postdoctoral Fellows (2002) |  |
| Lim, Seokhyun | Former Postdoctoral Fellows (2003) | Senior Researcher, Samsung Electronics Co., Ltd. |
| Kong, Hojin | Former Postdoctoral Fellows (2000) | Patent Company |
| Kim, Dongjoo | Former Postdoctoral Fellows (2003) | Professor, Mechanical Engineering, Kumoh National Institute of Technology |
| Kang, Sang Mo | Former Postdoctoral Fellows (1998) | Professor, Mechanical Engineering, Dong-a University |
| Kang, Hyung Suk | Former Postdoctoral Fellows (1998) | Researcher, The Johns Hopkins University |
| Han, SangYeop | Former Postdoctoral Fellows (2000) | Senior Researcher, Space Propulsion System Department, Korea Aerospace Research Institute |
| Hahn, Seonghyeon | Former Postdoctoral Fellows (2004) | CFD Engineer, Vestas Technology R&D, Denmark |
| Choi, Myung-Ryul | Former Postdoctoral Fellows (1996) | Managing Director, Terasemicon |
| Choi, Hwajeong | Former Postdoctoral Fellows (2000) |  |
| Choi, Chang Ho | Former Postdoctoral Fellows (1999) | Senior Researcher, Aero Propulsion Department, Korea Aerospace Research Institute |
| Cho, Sung Kwon | Former Postdoctoral Fellows (1997) | Associate Professor, Mechanical Engineering, University of Pittsburgh |

## 최근 논문 목록 (2021–2026)

연구실 Journal의 2021–2026년 논문 20편이다. 제목·저자·발표처·권·쪽과 연도는 연구실의 표기이고 DOI를 함께 적었다.[^journal]

**2026**

- Song, D., Jin, D. & Choi, H. "Flow characteristics past a normal flat plate at Re=5-10000". *Phys. Fluids 38, 088108; DOI: https://doi.org/10.1063/5.0335953*.
- Na, H., Kim, C., Choi, H., Kweon, J., Yang, D. H. & Kim, Y.-H. "On the assumption of conventional FFR: a modified formulation". *J. Biomechanics 204, 113381; DOI: https://doi.org/10.1016/j.jbiomech.2026.113381[^f157]*.
- Lee, I. & Choi, H. "A numerical study on the clustering characteristics of rising air bubbles in stagnant water". *Int. J. Multiphase Flow 194, 105419; DOI: https://doi.org/10.1016/j.ijmultiphaseflow.2025.105419*.

**2025**

- Park, J. & Choi, H. "Large eddy simulation of turbulent flow over a backward-facing step with a neural-network-based subgrid-scale model". *Phys. Fluids 37, 125115; DOI: https://doi.org/10.1063/5.0303085*.
- Choi, H., Cho, C., Kim, M. & Park, J. "Perspective on machine-learning-based large-eddy simulation". *Phys. Rev. Fluids 10, 110701; DOI: https://doi.org/10.1103/bxcn-rmdv*.
- Song, D., Yoon, Y.-J. & Choi, H. "Effect of the spanwise domain size on the flow characteristics behind a circular cylinder at low Reynolds numbers". *Phys. Rev. Fluids 10, 074103; DOI: https://doi.org/10.1103/qz6g-dcx9*.
- Lee, H., Oh, S. & Choi, H. "Neural-network-based optimization of the wing kinematics and geometry of a hovering flapping flight". *Phys. Fluids 37, 031918; DOI: https://doi.org/10.1063/5.0256748*.

**2024**

- Ahnn, S., Kim, H. & Choi, H. "Aerodynamic performance enhancement of a vertical-axis wind turbine by a biomimetic flap". *Bioinspir. Biomim. 20, 016022; DOI: https://doi.org/10.1088/1748-3190/ad9a45*.
- Cho, C., Park, J. & Choi, H. "A recursive neural-network-based subgrid-scale model for large eddy simulation: application to homogeneous isotropic turbulence". *J. Fluid Mech. 1000, A76; DOI: https://doi.org/10.1017/jfm.2024.992*.
- Lee, I., Chang, J., Kim, K. & Choi, H. "A numerical study on the turbulence characteristics in an air-water upward bubbly pipe flow". *J. Fluid Mech. 994, A10; DOI: https://doi.org/10.1017/jfm.2024.652*.
- Chang, J., Kim, K. & Choi, H. "A locally redistributed level-set method for numerical simulation of thin interface structures". *Computers & Fluids 278, 106315; DOI: https://doi.org/10.1016/j.compfluid.2024.106315*.
- Park, J. & Choi, H. "Effect of the yaw angle on the riblet performance". *Phys. Fluids 36, 065110; DOI: https://doi.org/10.1063/5.0210054*.
- Kim, K. & Choi, H. "Characteristics of turbulent core-annular flow with water-lubricated high viscosity oil in a horizontal pipe". *J. Fluid Mech. 986, A19; DOI: https://doi.org/10.1017/jfm.2024.345*.
- Kim, M., Park, J. & Choi, H. "Large eddy simulation of flow over a circular cylinder with a neural-network-based subgrid-scale model". *J. Fluid Mech. 984, A6; DOI: https://doi.org/10.1017/jfm.2024.154*.
- Jung, H., Oh, S. & Choi, H. "Role of the deviation motion on the aerodynamic performance of a mosquito wing in hover". *Computers & Fluids 270, 106146; DOI: https://doi.org/10.1016/j.compfluid.2023.106146*.

**2023**

- Choi, H., Oh, S., Lee, C., Choi, H. & Park, H. "Effect of superhydrophilic surface on the cavitation behaviors of rotating blades". *Phys. Fluids 35, 113316; DOI: https://doi.org/10.1063/5.0173693*.
- Ahnn, S. & Choi, H. "Leading-edge vortex and aerodynamic performance scaling in a simplified vertical-axis wind turbine". *Phys. Fluids 35, 105140; DOI: https://doi.org/10.1063/5.0166161*.

**2022**

- Song, D., Kim, W., Kwon, O.-K. & Choi, H. "Vertical and torsional vibrations before the collapse of the Tacoma Narrows Bridge in 1940". *J. Fluid Mech. 949, A11; DOI: https://doi.org/10.1017/jfm.2022.748*.

**2021**

- Wu, Z. & Choi, H. "Modification of flow behind a circular cylinder by steady and time-periodic blowing". *Phys. Fluids 33, 115126; DOI: https://doi.org/10.1063/5.0067706*.
- Jin, D., Wu, Z. & Choi, H. "A predictive model of the drag coefficient of a circular cylinder". *Phys. Fluids 33, 111702; DOI: https://doi.org/10.1063/5.0071079*.

## 수상과 선정

연구실 공지의 수상·선정과 학과 교수 소개의 수상 항목이다. 2022년 항목은 연도만 게시되어 있다.[^n151][^n153][^dept]

- 2025-04-25 · 최해천 교수, 과학기술훈장 혁신장 수훈
- 2023-11-14 · 최해천 교수, 학계 부문 「올해의 기계인」 선정
- 2022 · 최해천 교수, 대한기계학회 유체공학학술상 수상

## 소식

연구실 Notice에 게시된 논문 소개와 연구 성과 소식이다. 날짜는 공지 게시일이다.[^n154][^n155]

- 2022-12-20 · 타코마 다리의 붕괴 전 수직·비틀림 진동을 다룬 논문을 연구실 공지로 소개했다.
- 2022-10-27 · 서울대·한국과학기술정보연구원 연구팀이 타코마 다리 붕괴 과정을 계산으로 재현하고, 바람과 다리 움직임이 서로 영향을 주는 현상을 분석한 연구를 소개했다.

## 연락과 위치

- 교수 사무실: 서울대학교 301동 1511호, 전화 02-880-8361, 팩스 02-883-0179[^dept]
- 연구실: 301동 1413호, 전화 02-880-1655; 44동 103호·104호, 전화 02-880-7125[^dept]
- 교수 이메일: choi@snu.ac.kr[^r105]
- 주소: 서울특별시 관악구 관악로 1 서울대학교, 우편번호 08826[^r101]
[^r101]: 연구실 Introduction 연구 소개. <https://tfc.snu.ac.kr/index.php?hCode=INTRO_01_01> (관측 2026-11-11).

[^r102]: 연구실 Turbulence & Flow Control 난류 계산. <https://tfc.snu.ac.kr/index.php?hCode=INTRO_01_02> (관측 2026-11-11).

[^r103]: 연구실 Bio & Bio-Mimetic Engineering 표면 구조. <https://tfc.snu.ac.kr/index.php?hCode=INTRO_01_03> (관측 2026-11-11).

[^r104]: 연구실 Engineering Application 응용 연구. <https://tfc.snu.ac.kr/index.php?hCode=INTRO_01_04> (관측 2026-11-11).

[^r105]: 연구실 Director 학력. <https://tfc.snu.ac.kr/index.php?hCode=PROFESSOR_02_01_01> (관측 2026-11-11).

[^r131]: 연구실 Flow Control 능동·수동 제어. <https://tfc.snu.ac.kr/index.php?hCode=INTRO_01_02_02> (관측 2026-11-11).

[^r132]: 연구실 Machine Learning 난류 예측과 모형화. <https://tfc.snu.ac.kr/index.php?hCode=INTRO_01_02_03> (관측 2026-11-11).

[^r133]: 연구실 Bio-Mimetic Engineering 날개 형태. <https://tfc.snu.ac.kr/index.php?hCode=INTRO_01_03_02> (관측 2026-11-11).

[^r134]: 연구실 Bio-Mimetic Engineering 전체 형상. <https://tfc.snu.ac.kr/index.php?hCode=INTRO_01_03_03> (관측 2026-11-11).

[^r135]: 연구실 Director 경력. <https://tfc.snu.ac.kr/index.php?hCode=PROFESSOR_02_01_02> (관측 2026-11-11).

[^m107]: 연구실 Research Fellows. <https://tfc.snu.ac.kr/index.php?hCode=STAFF_LIST&gubun=RF> (관측 2026-11-11).

[^m108]: 연구실 Ph.D. Students. <https://tfc.snu.ac.kr/index.php?hCode=STAFF_LIST&gubun=PH> (관측 2026-11-11).

[^m109]: 연구실 Combined MS-Ph.D.Students. <https://tfc.snu.ac.kr/index.php?hCode=STAFF_LIST&gubun=CP> (관측 2026-11-11).

[^m110]: 연구실 Master Students. <https://tfc.snu.ac.kr/index.php?hCode=STAFF_LIST&gubun=MS> (관측 2026-11-11).

[^a111]: 연구실 Ph.D. Graduates. <https://tfc.snu.ac.kr/index.php?hCode=STAFF_LIST&gubun=PM_D> (관측 2026-11-11).

[^a139]: 연구실 MS Graduates. <https://tfc.snu.ac.kr/index.php?hCode=STAFF_LIST&gubun=PM_M> (관측 2026-11-11).

[^a140]: 연구실 Former Postdoctoral Fellows. <https://tfc.snu.ac.kr/index.php?hCode=STAFF_LIST&gubun=PM_F> (관측 2026-11-11).

[^n151]: 연구실 Notice 과학기술훈장 혁신장. <https://tfc.snu.ac.kr/index.php?page=view&pg=1&hCode=BOARD&bo_idx=1&sfl=&stx=&idx=322> (관측 2026-11-11).

[^n153]: 연구실 Notice 올해의 기계인. <https://tfc.snu.ac.kr/index.php?page=view&pg=1&hCode=BOARD&bo_idx=1&sfl=&stx=&idx=320> (관측 2026-11-11).

[^n154]: 연구실 Notice 타코마 다리 논문. <https://tfc.snu.ac.kr/index.php?page=view&pg=1&hCode=BOARD&bo_idx=1&sfl=&stx=&idx=308> (관측 2026-11-11).

[^n155]: 연구실 Notice 타코마 다리 계산 재현 연구. <https://tfc.snu.ac.kr/index.php?page=view&pg=1&hCode=BOARD&bo_idx=1&sfl=&stx=&idx=304> (관측 2026-11-11).

[^dept]: 서울대학교 기계공학부 최해천 교수 소개. <https://me.snu.ac.kr/snu__professor/%ec%b5%9c%ed%95%b4%ec%b2%9c-choi-haecheon/> (관측 2026-11-11).

[^journal]: 연구실 Journal 1–2쪽. <https://tfc.snu.ac.kr/index.php?hCode=PAPER_LIST&publication_name=inter_paper> <https://tfc.snu.ac.kr/index.php?pg=2&page=list&hCode=PAPER_LIST&publication_name=inter_paper> (관측 2026-11-11).

[^f157]: Hyunsoo Na, Changbeom Kim, Haecheon Choi, Jihoon Kweon, Dong Hyun Yang, Young-Hak Kim, Journal of Biomechanics 204, 113381 (2026). <https://doi.org/10.1016/j.jbiomech.2026.113381> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.jbiomech.2026.113381%22> (관측 2026-11-11).

[^p1]: D. Song, D. Jin, H. Choi, Physics of Fluids 38, 088108 (2026). <https://doi.org/10.1063/5.0335953> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044149519,publication_year:2021-2026> (관측 2026-11-11).

[^p2]: C. Cho, J. Park, H. Choi, Journal of Fluid Mechanics 1000, A76 (2024). <https://doi.org/10.1017/jfm.2024.992> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044149519,publication_year:2021-2026> (관측 2026-11-11).

[^p3]: I. Lee, J. Chang, K. Kim, H. Choi, Journal of Fluid Mechanics 994, A10 (2024). <https://doi.org/10.1017/jfm.2024.652> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044149519,publication_year:2021-2026> (관측 2026-11-11).

[^p4]: J. Park, H. Choi, Physics of Fluids 36, 065110 (2024). <https://doi.org/10.1063/5.0210054> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044149519,publication_year:2021-2026> (관측 2026-11-11).

[^p5]: S. Ahnn, H. Kim, H. Choi, Bioinspiration & Biomimetics 20, 016022 (2024). <https://doi.org/10.1088/1748-3190/ad9a45> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044149519,publication_year:2021-2026> (관측 2026-11-11).

[^p6]: H. Lee, S. Oh, H. Choi, Physics of Fluids 37, 031918 (2025). <https://doi.org/10.1063/5.0256748> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044149519,publication_year:2021-2026> (관측 2026-11-11).

[^p7]: D. Song, W. Kim, O.-K. Kwon, H. Choi, Journal of Fluid Mechanics 949, A11 (2022). <https://doi.org/10.1017/jfm.2022.748> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044149519,publication_year:2021-2026> (관측 2026-11-11).

[^p8]: Z. J. Wu, H. Choi, Physics of Fluids 33, 115126 (2021). <https://doi.org/10.1063/5.0067706> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5044149519,publication_year:2021-2026> (관측 2026-11-11).

# 컴퓨터원용 정형가공 연구실 (Computer-Aided Net Shape Manufacturing Laboratory, CANESM)

**KAIST 기계공학과 · 윤정환 교수**

- 분야: 소성역학과 재료 구성 모델(항복 함수·경화), 판재 성형과 스프링백 예측, 기계학습 기반 소성 해석, 고속 충격·폭발 파괴, 경량 소재·접합부 특성 평가, 고성능 가공
- 대분야: 기계·로봇·제조, 소재
- 태그: 과학·공학 AI[^p3], 고체역학·소성[^research], 충격·내충돌·폭발 방호[^p6], 전산역학·수치 해석[^p1], 복합재료[^p2]
- 홈페이지: <https://canesm.kaist.ac.kr/>
- 근거와 출처: [CANESM 근거 페이지](canesm-sources.md)

> 가벼운 소재와 구조물을 높은 신뢰성으로 설계·해석·제조하는 것을 연구 초점으로 삼는 기계공학과 연구실이다. 금속이 힘을 받아 영구히 변하는 소성 거동을 계산 모델로 나타내는 연구를 중심으로, 금속 성형, 고속 파괴(탄도·폭발), 재료 특성 평가, 고성능 가공을 연구 영역으로 든다.[^research][^me]

## 무엇을 연구하나

연구실은 KAIST 기계공학과 윤정환 교수의 연구실로, 누리집 이름은 Computer-Aided Net Shape Manufacturing Laboratory(CANESM)이고 기계공학과 교수 소개는 연구실을 「컴퓨터원용 정형가공 연구실」로 적는다.[^home][^me] 정형 가공(net shape manufacturing)은 소재를 처음부터 최종 모양에 가깝게 만들어 나중에 깎아 내는 공정을 줄이는 가공을 말한다. 누리집 History 페이지는 연구실이 1978년에 세워졌다고 적고 Dong-Yol Yang 교수의 학력과 경력을 싣는다. 2016년 항목에는 Dong-Yol Yang 교수의 퇴임과 윤정환 교수의 KAIST 교수 시작을 함께 적는다.[^history]

연구 페이지는 연구의 초점을 가벼운 소재와 구조물의 높은 신뢰성 설계·해석·제조(High Reliability Design, Analysis, Manufacturing of Light Weight Materials/Structure)로 적는다.[^research] 연구 영역은 세 묶음이다. 역학과 재료(Mechanics & Materials) 묶음에는 전산역학(computational mechanics, 물체의 변형과 힘을 컴퓨터로 계산해 푸는 역학), 소성과 다중 스케일 모델링, 경량 소재 모델링, 고속 파괴(탄도·폭발)가 있고, 재료 공정과 특성 평가 묶음에는 금속 성형, 재료 특성 평가 방법, 고성능 가공이, 설계와 제조 묶음에는 새 공정 개발이 있다.[^research] 기계공학과 교수 소개는 연구분야를 Mechanics of Plasticity, Materials Processing으로 적는다.[^me]

연구의 바탕은 소성(plasticity, 힘을 없애도 원래 모양으로 돌아가지 않는 영구 변형)이다. 최근 논문 목록에는 금속 판재의 항복 함수와 경화 모델, 기계학습으로 소성 계산과 성형 결과를 예측하는 연구, 탄도·폭발 하중에서의 파괴 연구, 배터리 파우치 필름과 이종 금속 접합부의 특성 평가, 항공용 알루미늄 합금의 절삭 가공 연구가 이어진다.[^pubs][^cr] 교수 소개 글은 교수가 가벼운 소재와 구조물의 높은 신뢰성 설계와 제조를 연구한다고 적는다.[^prof]

## 주요 연구 주제

### 1. 이방성 소성 모델: 항복 함수와 경화

금속 판재가 언제부터 영구 변형을 시작하고 변형이 진행되며 어떻게 단단해지는지를 수식 모델로 나타낸다. 연구 페이지는 이 갈래를 소성과 다중 스케일 모델링, 전산역학으로 든다.[^research] 최근 논문 목록에는 항복 함수(yield function, 재료가 영구 변형을 시작하는 응력 조건을 나타내는 식)와 경화(hardening, 영구 변형이 진행될수록 더 변형시키는 데 큰 힘이 드는 현상) 모델 연구가 많다. 방향에 따라 성질이 다른 이방성(anisotropy, 재료 성질이 방향에 따라 달라지는 성질) 항복 함수, 인장과 압축에서 항복 강도가 다른 비대칭 항복 함수, 변형 경로가 바뀔 때 항복 조건의 모양 자체가 바뀌는 왜곡 경화(distortional hardening, 영구 변형이 진행되며 항복 조건을 나타내는 면의 모양이 바뀌는 경화) 모델이 International Journal of Plasticity 등에 실렸다.[^pubs][^cr] 대표 논문 1은 금속 결정의 미끄럼 변형을 반영하는 결정 소성 유한요소법(CPFEM, crystal plasticity finite element method, 재료를 이루는 결정 알갱이의 방향과 미끄럼 변형을 반영해 계산하는 유한요소 해석)의 응력 적분 계산을 쉽게 바꾸었고,[^p1] 대표 논문 2는 섬유 강화 복합재의 3차원 구성 모델(constitutive model, 재료에 가한 변형과 그때 생기는 응력의 관계를 나타내는 수식 모델)을 제안했다.[^p2] 대표 논문 1, 2.

### 2. 기계학습 기반 소성 해석과 성형 예측

소성 해석의 계산 일부를 인공 신경망으로 대신하거나, 성형 뒤 생기는 스프링백(springback, 성형한 소재에서 힘을 빼면 탄성으로 일부 되돌아가는 현상)을 인공지능으로 예측·보정한다. 대표 논문 3은 J2 소성 모델의 비선형 응력 적분을 인공 신경망(ANN, artificial neural network, 여러 층의 계산 단위가 자료에서 입력과 출력의 관계를 배우는 모델)으로 대신하는 구성 모델을 만들었고,[^p3] 대표 논문 4는 전기차 구동 모터 부품의 성형에서 스프링백을 인공지능으로 보정하는 방법을 내놓았다.[^p4] 논문 목록에는 판재 성형용 기계학습 응력 적분법(2023), 소재 차이를 고려한 그래프 신경망 스프링백 예측(2026), 판재 스탬핑의 유입량을 예측하는 그래프 신경망(2026), 베이지안 최적화로 알루미늄 파우치 성형의 블랭크 홀딩력을 설계하는 연구(2026)도 있다.[^pubs][^cr] 대표 논문 3, 4.

### 3. 고속 충격·폭발 파괴(탄도·폭발)

연구 페이지가 드는 고속 파괴(High Speed Fracture, Ballistic and Blast) 갈래다.[^research] 높은 변형률 속도와 온도에서의 재료 성질을 반영해 발사체가 표적을 뚫는 깊이나 폭발 하중을 받은 금속 구조물의 파괴를 예측한다. 대표 논문 5는 긴 막대 모양 관통체의 관통 깊이를 예측하는 모델을 넓혔고,[^p5] 대표 논문 6은 안에서 폭발 하중을 받는 금속 원통의 동적 파괴를 수치 해석으로 다뤘다.[^p6] 논문 목록에는 텅스텐 합금 관통체의 충격 파괴(2023), 변형률·변형률 속도·온도를 반영한 구형 공동 확장법(2023), 둘레에 홈을 낸 원통 케이스의 파편화 예측(2024), 폭발 하중에서 파편 속도 분포를 데이터로 예측하는 연구(2025), 속이 빈 발사체의 고변형률 속도 파괴(2025)가 이어진다.[^pubs][^cr] 대표 논문 5, 6.

### 4. 금속 성형, 재료 특성 평가와 경량 소재

연구 페이지가 드는 금속 성형, 재료 특성 평가 방법, 경량 소재 모델링 갈래다.[^research] 대표 논문 7은 리튬이온 배터리 파우치에 쓰는 알루미늄-고분자 적층 필름의 성형 한계(forming limit, 재료가 찢어지기 전까지 늘어날 수 있는 변형의 한계)를 재는 시험법을 다뤘다.[^p7] 논문 목록에는 배터리 파우치 필름의 층별 이방성 특성 평가와 성형 적용(2024), 알루미늄-강 저항 점용접부의 미세 전단 시험(2025), 자연 시효 중인 AA 2198 합금의 구성 모델과 성형성(2025), 판재 성형의 스프링백 예측을 위한 바우싱거 효과 보정(2023), 알루미늄-강 이종 용접부에서 미세 결함이 균열의 방향을 바꾸는 현상을 다룬 연구(2026)가 있다.[^pubs][^cr] 대표 논문 7.

### 5. 고성능 가공

연구 페이지가 드는 고성능 가공(High-performance machining) 갈래다.[^research] 대표 논문 8은 항공용 AA2024-T351 알루미늄 합금의 직교 절삭(orthogonal machining, 공구 날이 절삭 방향에 수직인 단순화된 절삭)을 다루기 위해 연성 파괴(ductile fracture, 재료가 큰 영구 변형을 겪은 뒤 끊어지는 파괴) 기준을 고변형률 속도·고온 조건으로 넓혔다.[^p8] 논문 목록에는 같은 합금을 코팅하지 않은 초경 공구로 깎는 가공성 연구(2021)도 있다.[^pubs] 대표 논문 8.

## 대표 논문

윤정환 교수가 저자인 2021–2026년 논문 가운데 초록을 확인할 수 있는 여덟 편을 연구 갈래마다 골랐다. 여덟 편 모두 교수가 마지막 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs][^cr] |
|---|---|---|---|---|
| 1 | 2024 | [Finite difference based stress integration algorithm for crystal plasticity finite element method](https://doi.org/10.1007/s12289-023-01806-8) · International Journal of Material Forming | 결정 소성 유한요소법(CPFEM)에서 쓰는 오일러 후진 응력 적분과 뉴턴-랩슨 방법은 분해 전단 응력(결정의 미끄럼 면과 방향으로 작용하는 전단 응력)의 1차 도함수를 계산해야 해서 복잡하다. 이 논문은 이 도함수를 유한 차분법(FDM, 값의 작은 차이로 도함수를 근사하는 수치 방법)으로 구하는 응력 적분 알고리즘을 내놓아, 구성 모델이 무엇이든 복잡한 도함수를 따로 유도하지 않고 쓸 수 있게 했다. 요소 하나짜리 시뮬레이션으로 정확도·수렴성·계산 효율을 확인했고, AA 2090-T3 합금에 축소 집합조직 접근(reduced texture approach)을 적용해 결정 방위 같은 매개변수를 맞추어 소성 이방성을 나타냈으며, 귀(earing, 원통 컵을 딥드로잉할 때 가장자리 높이가 둘레를 따라 오르내리는 현상) 모양을 여러 응력 적분법과 비교했다. 해석적 도함수를 쓰는 오일러 후진법과 견줄 만한 정확도·수렴성·계산 효율을 내면서 구현이 쉽다고 적는다.[^p1] | 1저자 D. Noh, 윤정환 마지막 (2명) |
| 2 | 2022 | [A general FRC (fiber reinforced composite) constitutive model considering transverse isotropy and accumulated damage](https://doi.org/10.1007/s12206-022-1129-z) · Journal of Mechanical Science and Technology | 한 방향으로 섬유를 넣은 섬유 강화 복합재를 3차원 유한요소 시뮬레이션으로 다루기 위한 구성 모델을 제안했다. 상용 프로그램 ABAQUS에 들어 있는 2차원 Hashin 기준과 Lapczyk 손상 모델을 바탕으로 손상 변수를 단계마다 계산하는 새 방식을 내놓고, 가로 등방성(transverse isotropy, 섬유 방향에 수직인 면 안에서는 성질이 방향과 상관없는 성질)을 이용해 이 손상 변수를 3차원 모델로 넓혔다. 요소 하나에 비례 하중을 건 조건에서 원래의 2차원 평면 응력 모델과 결과를 견주었고, 노치가 있는 적층판 문제와 탄도 예제로 일반 3차원 문제를 시험하며 3차원 구성 모델이 필요함을 논의했다.[^p2] | 1저자 J. Park, 윤정환 마지막 (2명) |
| 3 | 2021 | [Machine learning-based constitutive model for J2-plasticity](https://doi.org/10.1016/j.ijplas.2020.102919) · International Journal of Plasticity | 등방 경화와 연관 유동 법칙을 쓰는 J2 소성 모델(편차 응력의 두 번째 불변량으로 항복 여부를 판정하는 소성 모델)에서 탄소성 거동을 예측하는 기계학습 구성 모델을 제안했다. 기존 이론 모델의 비선형 응력 적분을 인공 신경망(ANN)으로 대신했고, 학습 자료는 주응력 공간에서 기존 리턴 매핑 방식으로 수치 계산해 만들었다. 가능한 모든 소성 하중 경로를 요소 하나 시뮬레이션으로 학습해 문제에 상관없이 쓰도록 했고, 신경망은 비선형 소성 하중에만 쓰고 선형 탄성 하중과 하중 제거에는 물리 기반 모델을 그대로 썼다. Abaqus 사용자 재료 루틴(UMAT)에 넣어 요소 하나·인장 시험·원형 컵 드로잉 시뮬레이션으로 확인했더니 기존 J2 모델의 결과와 잘 맞았고, 계산 시간에서도 이점을 보였다.[^p3] | 1저자 D. P. Jang, 윤정환 마지막 (3명) |
| 4 | 2022 | [Artificial intelligence for springback compensation with electric vehicle motor component](https://doi.org/10.1007/s12289-022-01671-x) · International Journal of Material Forming | 전기차 구동 모터에 쓰는 헤어핀은 아주 얇은 에나멜 막을 입힌 구리 코일을 여러 단계의 성형으로 원하는 모양으로 만든 부품인데, 피할 수 없는 스프링백이 모터 성능과 직결되는 제작 문제를 일으킨다. 이 논문은 인공지능으로 헤어핀 성형의 스프링백을 보정하는 방법을 내놓았다. AI 모델은 재료 성질, 단면 치수, 금형과 펀치 사이 간격(또는 펀치 행정)을 나타내는 die spotting 값을 입력으로 스프링백 매개변수 여덟 개를 계산하고, 학습 자료는 유한요소 시뮬레이션으로 만들었다. 구리와 얇은 에나멜 막의 재료 성질은 새로 설계한 시편, 나노 압입, 역해석을 함께 써서 구했고, 학습한 AI 모델과 심플렉스 최적화 알고리즘으로 die spotting 값을 최적화해 몇 초 만에 스프링백을 효과적으로 보정했다.[^p4] | 1저자 H. Choi, 윤정환 마지막 (7명) |
| 5 | 2024 | [Extension of One-Dimensional Penetration Model Considering Cylindrical Cavity Expansion with Johnson-Cook Hardening](https://doi.org/10.1115/hvis2024-068) · 2024 17th Hypervelocity Impact Symposium | Walker-Anderson 관통 모델(WAPM)에 Johnson-Cook 경화 모델(변형률·변형률 속도·온도에 따라 금속의 유동 응력이 달라지는 것을 나타내는 경화 모델) 기반의 원통 공동 확장법(CCEM-JC)을 결합했다. 넓은 범위의 변형률·변형률 속도·온도에서의 동적 재료 성질로 관통체가 깎여 나가며 뚫는 침식 관통을 해석해 관통 깊이를 예측하고, 많은 탄도 시험에 기대는 부담을 줄이려는 것이다. 확장 모델(eWAPM)은 긴 막대 관통체에 대한 유한요소 해석과 탄도 시험 결과로 검증했고, 표적 재료에 Johnson-Cook 모델을 넣어 고속 충돌을 다루며 종말 탄도(terminal ballistics, 발사체가 표적에 부딪힌 뒤 일어나는 현상) 예측 정확도를 높이고 실험 비용을 크게 줄인다고 적는다.[^p5] | 1저자 I. Ga, 윤정환 마지막 (2명) |
| 6 | 2022 | [Failure mechanism for metal cylinder under explosive loading](https://doi.org/10.1007/s12206-022-0811-5) · Journal of Mechanical Science and Technology | 안에서 폭발 하중을 받는 금속 원통의 동적 파괴를 수치 해석으로 연구하고, 파괴 모델과 홈(groove) 설계가 파괴 거동에 주는 영향을 살폈다. 동적 경화는 열 연화 효과를 포함한 Lim-Huh 모델을, 파괴 예측은 변형률 속도 의존성을 고려한 Lou-Huh 파괴 모델을 썼다. 인장 파괴가 바깥면에서 먼저 생기고 안쪽 면 근처에서는 전단 파괴가 관찰됐다. 바깥면에 U자 홈과 V자 홈을 하나씩 낸 설계를 유한요소 해석한 결과 인장 파괴선과 전단 파괴선이 각각 홈 끝과 안쪽 면 근처에서 예측됐고, 응력 삼축비(stress triaxiality, 응력의 정수압 성분을 등가 응력으로 나눈 값)가 금속 원통의 동적 파괴 예측에서 중요한 요인이라고 결론지었다.[^p6] | 1저자 D. Noh, 윤정환 마지막 (5명) |
| 7 | 2026 | [Forming Limit Test of Asymmetric Al-Polymer Laminate Composite Film](https://doi.org/10.4028/p-is64g3) · Solid State Phenomena | 더 효율적인 리튬이온 배터리를 만들려고 업계는 배터리 셀의 깊이를 늘리려 하며, 깊은 셀을 만들려면 소재의 성형성을 알아야 한다. 파우치형 배터리 소재는 폴리프로필렌·알루미늄·나일론·PET 네 층으로 된 비대칭 알루미늄-고분자 적층 복합 필름인데, 고분자 층의 성형성이 좋아 Nakazima 시편 같은 일반적인 성형 한계 시험으로는 성형 한계 곡선을 얻을 수 없다. 그래서 시편 가운데에 변형을 모으는 수정 Marciniak 시험을 쓰고, 펀치 모서리에 닿는 곳이 먼저 끊어지지 않도록 시편과 펀치 사이에 더미 판을 넣었다. 여러 고분자를 더미 판 재료로 시험하고 여러 설계의 시편을 시험했으며, 두께 153 μm인 알루미늄-고분자 필름의 성형 한계 시험 결과를 극 유효 소성 변형률(PEPS) 방식으로 변환했다.[^p7] | 1저자 C. Sagong, 윤정환 마지막 (4명) |
| 8 | 2021 | [Finite element modeling for orthogonal machining of AA2024-T351 alloy with an advanced fracture criterion](https://doi.org/10.1115/1.4051057) · Journal of Manufacturing Science and Engineering | 고속 가공 중의 소성 변형과 파괴를 수치로 모델링하기는 매우 어렵다. 이 논문은 정적 조건의 Lou-Yoon-Huh(LYH) 연성 파괴 기준에 변형률 속도와 온도 의존 항을 넣어 가공 같은 고변형률 속도·고온 조건으로 넓히고, 넓은 범위의 응력 삼축비와 여러 온도에서 보정했다. 가공 중 재료 흐름은 수정한 Khan-Huang-Liang 구성 모델과 가변 마찰 모델로 예측하고, 손상 진전으로 요소가 지워지는 시점을 정했다. 항공용 AA2024-T351 합금을 절삭 속도 100–400 m/min, 이송 0.1–0.3 mm/rev에서 직교 절삭 실험했고, Johnson-Cook 파괴 기준을 쓴 시뮬레이션과 견주어 확장 LYH 기준이 비절삭 에너지·칩 모양·압축비를 실험과 더 잘 맞게 예측했다.[^p8] | 1저자 P. R. Paresi, 윤정환 마지막 (4명) |

## 교수와 전문 분야

윤정환 교수(Jeong Whan Yoon)는 KAIST 기계공학과 교수다. 기계공학과 교수 소개는 최종학위를 Ph.D., KAIST (1997)로, 연구분야를 Mechanics of Plasticity, Materials Processing으로 적는다.[^me] 누리집 교수 페이지는 교수를 KAIST 기계공학과 교수(2015.11–현재)이자 오스트레일리아 Deakin University의 Research Professor of Applied Mechanics(2015.11–현재)로 적고, Korea Academy of Science and Technology의 Fellow와 International Journal of Plasticity의 Associate Editor를 함께 적는다.[^prof]

학력은 Hanyang Univ.의 Dept. of Precision Mechanical Eng. 학사(1991), KAIST의 Dept. of Precision Eng. & Mechatronics 석사(1993), KAIST 기계공학과(Dept. of Mechanical Engineering) 박사(1997)이고, 석사·박사 과정 동안 LG Electronics 장학생이었다.[^prof] 박사 뒤 미국 Alcoa Technical Center의 Post-Doc(1997.4–1998.3), LG Electronics의 Sr. Research Engineer(1998.4–2001.2, LG Production Engineering Research Center의 신제품 개발), 미국 MSC Software Corporation의 Senior Developer(2001.6–2003.10, 범용 비선형 상용 소프트웨어 Marc·Nastran의 소스 코드 개발), Alcoa Technical Center의 Sr. Staff Scientist(2003.10–2010.3, 고급 재료 모델 개발 과제 주도)를 거쳤다.[^prof] 이후 Swinburne University의 Full Professor of Advanced Manufacturing이자 Research Director of Australia Advanced Manufacturing Research Center with Boeing(AusAMRC)(2010.04–2013.06), Deakin University의 Chair Professor of Applied Mechanics & Head of Advanced Manufacturing(2013.07–2015.10)을 지냈고, 포르투갈 University of Aveiro의 High Merit Scientist / Invited Professor(2013.01–현재, 시간제)도 적혀 있다.[^prof] 교수 소개 글은 교수가 Swinburne University에서 Boeing-chaired manufacturing research(AusAMRC)를, Deakin University에서 GM-chaired manufacturing research(ICIM)를 이끌었다고 적는다.[^prof]

수상으로는 2023 Khan International Award(교수 소개 글은 소성 분야의 평생 기여로 받았다고 적는다), 2008 International Journal of Plasticity Award(Elsevier, 교수 소개 글의 표기로는 2008 International Journal of Plasticity Young Researcher Award이고 최근 5년의 기여로 받았다), Sigma Xi best paper award-Alcoa Chapter(2006)가 적혀 있다.[^prof] International Journal of Plasticity의 특집호 아홉 개와 International Journal of Solids and Structures 특집호 두 개를 객원 편집했고, NUMISHEET2014(오스트레일리아 멜버른), APEA2018(제주), ICPDF2023·ICPDF2024(도미니카 공화국·파나마) 학회의 의장을 맡았다.[^prof] 누리집은 교수가 국제 학술지와 학회에 300편이 넘는 논문을 냈다고 적는다.[^prof]

2021–2026년 논문으로 보면 전문 분야는 금속 판재의 이방성 항복 함수와 경화 모델, 결정 소성 해석, 기계학습 기반 소성 계산과 스프링백 예측, 탄도·폭발 하중에서의 동적 파괴 예측이다.[^pubs][^cr]

## 응용 분야

대표 논문과 논문 목록에 나오는 응용은 전기차 구동 모터 부품(헤어핀)의 성형,[^p4] 리튬이온 배터리 파우치 필름의 성형,[^p7] 탄도·폭발 하중을 받는 관통체와 금속 원통,[^p5][^p6] 항공용 알루미늄 합금의 절삭 가공이다.[^p8] 논문 목록에는 냉각재 상실 사고(LOCA) 때의 원자력 연료 피복관 풍선 변형·파열 예측(2021)과 롤 성형의 스프링백 예측(2026)도 있다.[^pubs][^cr]

## 구성원

누리집 Students 페이지의 박사과정(PH.D. Students) 8명과 석사과정(Master Students) 3명, PostDocs 페이지 현재(Current) 칸의 박사후연구원 3명, 모두 14명이다. 이름은 페이지 표기이고 학생은 국문 이름을 함께 적었다. 이메일은 각 카드에 적힌 KAIST 주소다.[^students][^postdocs] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Cheol Sagong (사공철) | 박사과정 | sak9709@kaist.ac.kr | 7 |
| Heon Yong Lim (임헌용) | 박사과정 | heonyonglim@kaist.ac.kr |  |
| Juwon Lee (이주원) | 박사과정 | juwonlee@kaist.ac.kr |  |
| Donghoon Han (한동훈) | 박사과정 | dhhan218@kaist.ac.kr |  |
| Sukkeun Oh (오석근) | 박사과정 | sukkeun.oh@kaist.ac.kr |  |
| Taegyun Ahn (안태균) | 박사과정 | t.ahn@kaist.ac.kr | 7 |
| Wonjin Park (박원진) | 박사과정 | wonjin27@kaist.ac.kr |  |
| Daecheon Cho (조대천) | 박사과정 | dcjo1025@kaist.ac.kr |  |
| Wooseok Lee (이우석) | 석사과정 | galaxy1045@kaist.ac.kr |  |
| Hyung Su Yoon (윤형수) | 석사과정 | yhsmansu@kaist.ac.kr |  |
| Hyungjoo Lee (이형주) | 석사과정 | 4rsenal@kaist.ac.kr |  |
| Guofeng Han | 박사후연구원 | hanguofeng@kaist.ac.kr |  |
| Donghyuk Cho | 박사후연구원 | d.cho@kaist.ac.kr |  |
| Hui Wang | 박사후연구원 | huiwang@kaist.ac.kr |  |

## 이전 박사후연구원

PostDocs 페이지 PasT 칸의 박사후연구원 2명이다. 진로는 페이지 표기 그대로다.[^postdocs]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Qi Hu | PostDoc (Past) | Associate Professor, Shanghai Jiao Tong University |
| Lihuang Zheng | PostDoc (Past) | Associate Professor, Shandong University |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지 Research Papers 목록의 2021–2023년 논문 33편(181–213번)과, 누리집 목록에는 없고 출판사 등록 서지(Crossref)에 교수가 저자로 오른 2024–2026년 논문 35편(끝에 doi를 적은 항목), 모두 68편이다. 누리집 목록은 2023년 11월 논문(213번)까지 적혀 있다. 누리집 항목은 목록 표기 그대로 저자, 발표 연월, 제목, 학술지·학회 순으로 적었고, 학술지 논문과 학회 논문집 논문이 함께 있다. doi를 적은 항목의 저자·제목·학술지·학회 표기는 출판사 등록 서지의 표기이고, 연도는 출판사 서지의 발행 연도다.[^pubs][^cr]

**2026**

- Lihuang Zheng, Cunsheng Zhang, and Jeong Whan Yoon. "An analytical yield criterion with two-dimensional convex domains for plasticity modeling of metal sheets across a wide range of stress states". *International Journal of Plasticity (doi:10.1016/j.ijplas.2026.104671)*.
- Lihuang Zheng, Qi Hu, BangSheng Zhou, Guoqun Zhao, and Jeong Whan Yoon. "An asymmetric yield criterion for plasticity modeling of metal sheets considering shear and near-plane strain tension". *Journal of Materials Research and Technology (doi:10.1016/j.jmrt.2026.09.163)*.
- Guijia Li, Junhe Lian, and Jeong Whan Yoon. "An evolving non-associated Hill-Barlat yield criterion for anisotropic hardening with closed-form analytical calibration and guaranteed convexity". *International Journal of Plasticity (doi:10.1016/j.ijplas.2026.104762)*.
- Donghoon Han, Donghyuk Cho, Seik An, and Jeong Whan Yoon. "Combined Finite Element Simulation and Regression Modeling for Predicting Final Protrusion Length of Twisted Hairpin Legs in Stators". *Solid State Phenomena (doi:10.4028/p-l8owxo)*.
- Donghyuk Cho, Hassan Ghassemi-Armaki, Blair E. Carlson, and Jeong Whan Yoon. "Crack deflection from micro-defect in Al-Steel dissimilar welds: Multi-scale experiments and finite element modeling". *Journal of Manufacturing Processes (doi:10.1016/j.jmapro.2026.03.082)*.
- Taegyun Ahn, Taek Jin Jang, Cheol Sagong, and Jeong Whan Yoon. "Design of spatially and temporally variable blank holding forces based on Bayesian optimization for aluminum pouch forming". *CIRP Annals (doi:10.1016/j.cirp.2026.04.086)*.
- Taegyun Ahn, Juwon Lee, Janghoon Lee, and Jeong Whan Yoon. "Experimental Study on the Relationship between Cooling Rate, Secondary Dendrite Arm Spacing and Tensile Properties in Aluminum Casting". *Solid State Phenomena (doi:10.4028/p-os8u1c)*.
- Cheol Sagong, Taek Jin Jang, Taegyun Ahn, and Jeong Whan Yoon. "Forming Limit Test of Asymmetric Al-Polymer Laminate Composite Film". *Solid State Phenomena (doi:10.4028/p-is64g3)*.
- Songchen Wang, Tianchi Ren, Hongchun Shang, Jeong Whan Yoon, Gang Chen, Dianyin Hu, and Yanshan Lou. "Fracture behavior characterization of AA6082 thin-walled rectangular tubes under low-velocity impact". *Engineering Structures (doi:10.1016/j.engstruct.2026.122462)*.
- Hui Wang, Taegyun Ahn, Lu Huang, Seog Chan Oh, Liang Huang, Andrey Ilinich, Sathya Dev, and Jeong Whan Yoon. "Graph Neural Network for Draw-in Prediction in Sheet Metal Stamping". *Key Engineering Materials (doi:10.4028/p-wkww4q)*.
- Guofeng Han and Jeong Whan Yoon. "Nonideality of simple shear deformation and shear strain assessment". *International Journal of Mechanical Sciences (doi:10.1016/j.ijmecsci.2026.112073)*.
- Hyunsung Choi, Jongsup Lee, Geunho Kim, and Jeong Whan Yoon. "Springback prediction considering anisotropy and nonlinear strain paths in roll forming process". *International Journal of Material Forming (doi:10.1007/s12289-026-02076-w)*.
- Hui Wang, Heonyong Lim, and Jeong Whan Yoon. "Stress-aware graph neural network for springback prediction considering material variations". *Journal of Materials Processing Technology (doi:10.1016/j.jmatprotec.2025.119189)*.

**2025**

- Jing Huang, Hui Wang, Donghoon Han, Choong Myoung Lee, Seung-Joo Jo, Chang-Won Seo, Sungpeel Kim, Seong-Sik Yoon, Jeong Whan Yoon, and Seong-Ook Park. "A Force-Based Elastic Mesh Model for Electrical Property Analysis of Reflector Antennas". *Journal of Electromagnetic Engineering and Science (doi:10.26866/jees.2025.6.r.334)*.
- Hyunsung Choi and Jeong Whan Yoon. "A strain rate-dependent distortional hardening model for nonlinear strain paths". *International Journal of Plasticity (doi:10.1016/j.ijplas.2024.104197)*.
- Chong Zhang, Chao Niu, Yanshan Lou, Jeong Whan Yoon, Liucheng Zhou, and Xiaoqing Liang. "Analytical anisotropic hardening extension of a differential hardening yield function for strength modelling under various stress states with non-associated flow rule by a new linear transformation tensor". *International Journal of Material Forming (doi:10.1007/s12289-025-01877-9)*.
- Qi Hu, Jeong Whan Yoon, and Jun Chen. "Anisotropic distortional hardening based on deviatoric stress invariants under non-associated flow rule. Part-II: Generalization combined with non-quadratic yield function under associated flow rule". *International Journal of Plasticity (doi:10.1016/j.ijplas.2025.104256)*.
- Donghyuk Cho, Hassan Ghassemi-Armaki, Thomas B. Stoughton, Blair E. Carlson, and Jeong Whan Yoon. "Characterization of micro-scale gradient material properties to visualize the variations of stress-strain relationships with digital image correlation method". *Materials Science and Engineering: A (doi:10.1016/j.msea.2025.148636)*.
- Donghwan Noh and Jeong Whan Yoon. "Consideration of Bauschinger effect based on a reduced texture approach for improved springback prediction with computational efficiency". *CIRP Annals (doi:10.1016/j.cirp.2025.03.022)*.
- Sook Lee, Taek Jin Jang, Deok Chan Ahn, and Jeong Whan Yoon. "Constitutive modeling and formability insights for AA 2198 during natural aging and its application to stretch forming". *International Journal of Material Forming (doi:10.1007/s12289-025-01917-4)*.
- Donghwan Noh, Piemaan Fazily, Songwon Seo, Jaekun Lee, Seungjae Seo, Hoon Huh, and Jeong Whan Yoon. "Data driven prediction of fragment velocity distribution under explosive loading conditions". *Defence Technology (doi:10.1016/j.dt.2024.07.007)*.
- Chang Soo Lee, Jeong Whan Yoon, Sang Hyun Woo, and Lee Ju Park. "High strain-rate fracture behavior of a hollow projectile". *International Journal of Impact Engineering (doi:10.1016/j.ijimpeng.2024.105138)*.
- Donghyuk Cho, Hassan Ghassemi-Armaki, Blair E. Carlson, Dong Ruan, and Jeong Whan Yoon. "Micro-scale shear testing for localized constitutive characterization of Al-Steel resistance spot weld under large deformation". *Mechanics Research Communications (doi:10.1016/j.mechrescom.2025.104495)*.
- Choong Myoung Lee, Donghwan Noh, Chungu Kang, and Jeong Whan Yoon. "Prediction of edge crack initiation of low carbon steel based on stress-based failure model during hot rolling process". *Journal of Mechanical Science and Technology (doi:10.1007/s12206-025-0423-y)*.

**2024**

- Lihuang Zheng and Jeong Whan Yoon. "A flexible yield criterion for strength modeling from biaxial compression to biaxial tension". *International Journal of Plasticity (doi:10.1016/j.ijplas.2024.104113)*.
- Lihuang Zheng and Jeong Whan Yoon. "A new failure criterion for predicting meso/micro-scale forming limit of composite metal foils". *International Journal of Plasticity (doi:10.1016/j.ijplas.2024.103962)*.
- Kwanghyun Yu and Jeong Whan Yoon. "Characterization of compressive fracture strain based on bilinear strain paths". *International Journal of Plasticity (doi:10.1016/j.ijplas.2024.104168)*.
- Taek Jin Jang, Cheol Sagong, Taegyun Ahn, and Jeong Whan Yoon. "Characterization of layered anisotropic properties for Li-ion battery pouch film and its application to forming". *CIRP Annals (doi:10.1016/j.cirp.2024.04.011)*.
- Inhan Ga and Jeong Whan Yoon. "Extension of One-Dimensional Penetration Model Considering Cylindrical Cavity Expansion with Johnson-Cook Hardening". *2024 17th Hypervelocity Impact Symposium (doi:10.1115/hvis2024-068)*.
- Donghwan Noh and Jeong Whan Yoon. "Finite difference based stress integration algorithm for crystal plasticity finite element method". *International Journal of Material Forming (doi:10.1007/s12289-023-01806-8)*.
- Songchen Wang, Jeong Whan Yoon, and Yanshan Lou. "Lode-dependent anisotropic-asymmetric yield function for isotropic and anisotropic hardening of pressure-insensitive materials. Part II: Stress invariant-based coupled quadratic and non-quadratic function". *International Journal of Plasticity (doi:10.1016/j.ijplas.2024.104043)*.
- Kwanghyun Yu, Sook Lee, Jong Won Yoon, Young Hyuk Jung, Hoon Huh, and Jeong Whan Yoon. "Mapping of gun-firing loading to high-impact testing velocity with shock response spectrum method". *Mechanical Systems and Signal Processing (doi:10.1016/j.ymssp.2024.111212)*.
- Kang Wu, Shunying Zhang, Matthias Weiss, and Jeong Whan Yoon. "Modeling of distortional hardening including plane strain tension and pure shear for a TWIP steel". *International Journal of Material Forming (doi:10.1007/s12289-024-01835-x)*.
- Donghwan Noh, Taek Jin Jang, Songwon Seo, Jaekun Lee, Seungjae Seo, Hoon Huh, and Jeong Whan Yoon. "Prediction of controlled fragmentation for cylindrical casing with circumferential grooves". *International Journal of Impact Engineering (doi:10.1016/j.ijimpeng.2024.104884)*.
- Qi Hu, Lorenz Maier, Takeshi Nishiwaki, Christoph Hartmann, Wolfram Volk, and Jeong Whan Yoon. "User friendly FE Formulation for anisotropic distortional hardening model based on non-associated flow plasticity and its application to springback prediction". *Thin-Walled Structures (doi:10.1016/j.tws.2024.112142)*.

**2023**

- Ga, I., Noh, D., & Yoon, J. W. (2023, November). Spherical cavity expansion method dependent on strain, strain rate, and temperature. International Journal of Impact Engineering, 181, 104730.
- Lou, Y., Zhang, C., & Yoon, J. W. (2023, August). Anisotropic-Asymmetric Hardening Characterization of BCC/FCC/HCP Metals: Experiments and Modeling. International Conference on the Technology of Plasticity, 613-621.
- Lee, C. S., Yoon, J. W., Woo, S. H., & Park, L. J. (2023, August). Thermal softening behavior up to fracture initiation during high-rate deformation. International Journal of Mechanical Sciences, 251, 108321.
- Sagong, C., Legarth, B. N., & Yoon, J. W. (2023, July). Particle-matrix debonding with Strength-Differential effects. European Journal of Mechanics-A/Solids, 105078.
- Lou, Y., & Yoon, J. W. (2023, July). Lode-dependent anisotropic-asymmetric yield function for isotropic and anisotropic hardening of pressure-insensitive materials. Part I: Quadratic function under non-associated flow rule. International Journal of Plasticity, 166, 103647.
- Fazily, P., & Yoon, J. W. (2023, July). Machine learning-driven stress integration method for anisotropic plasticity in sheet metal forming. International Journal of Plasticity, 166, 103642.
- Choi, H., Kwon, Y., Cho, J. H., & Yoon, J. W. (2023, June). Artificial intelligence-based springback compensation of EV motor component. IOP Conference Series: Materials Science and Engineering, 1284(1), 12069.
- Noh, D., Fazily, P., Yu, K., Lee, S., Ko, D. K., Sung, M. J., Huh, H., & Yoon, J. W. (2023, June). Tungsten alloy impact fracture for frangible armor piercing. International Journal of Impact Engineering, 180, 104681.
- Choi, H., & Yoon, J. W. (2023, June). A new simplified distortional hardening model for nonlinear strain paths. International Journal of Plasticity, 165, 103617.
- Jang, T. J., Yoon, J. W., & Kim, J. B. (2023, May). Determination of Johnson-Cook constitutive model coefficients considering the initial gap between contact faces in SHPB test. Journal of Materials Research and Technology, 24, 7242-7257.
- Zhang, S., Lou, Y., & Yoon, J. W. (2023, May). Earing prediction with a stress invariant-based anisotropic yield function under non-associated flow rule. International Journal of Material Forming, 16(3), 25.
- Yu, K., Choi, H., Ha, J., & Yoon, J. W. (2023, March). Bauschinger effect calibration by the different types of loading/reverse loading tests for springback prediction in sheet metal forming. International Journal of Material Forming, 16(2), 16.
- Hu, Q., Yoon, J. W., & Chen, J. (2023, March). Analytically described polynomial yield criterion by considering both plane strain and pure shear states. International Journal of Plasticity, 162, 103514.
- Kang, C. G., & Yoon, J. W. (2023, February). Effect of Strain Localization on the Mechanical Properties from Nonuniform Grain Size Distribution of Ultralow Carbon Steel. Steel Research International, 94(2), 2200335.

**2022**

- Park, J., & Yoon, J. W. (2022, December). A general FRC (fiber reinforced composite) constitutive model considering transverse isotropy and accumulated damage. Journal of Mechanical Science and Technology, 36(12), 6147-6156.
- Lou, Y., Wu, P., Zhang, C., Wang, J., Li, X., Chai, R., & Yoon, J. W. (2022, December). A stress-based shear fracture criterion considering the effect of stress triaxiality and Lode parameter. International Journal of Solids and Structures, 256, 111993.
- Lou, Y., Zhang, C., Zhang, S., & Yoon, J. W. (2022, November). A general yield function with differential and anisotropic hardening for strength modeling under various stress states with non-associated flow rule. International Journal of Plasticity, 158, 103414.
- Noh, D., Seo, S., Lee, J., Jang, M., & Yoon, J. W. (2022, September). Failure mechanism for metal cylinder under explosive loading. Journal of Mechanical Science and Technology, 36(9), 4463-4474.
- Lou, Y., Zhang, J., Zhang, C., & Yoon, J. W. (2022, August). Characterization of Yield Surface Evolution of AZ31 from Shear to Equibiaxial Tension. Key Engineering Materials, 926, 1093-1099.
- Park, N., Bae, G., Song, J. H., Lee, J. S., Stoughton, T. B., & Yoon, J. W. (2022, July). Modeling of the Anisotropic Evolution of Yield Surface Based on Non-associated Flow Rule. NUMISHEET 2022: Proceedings of the 12th International Conference and Workshop on Numerical Simulation of 3D Sheet Metal Forming Processes, 355-364.
- Oh, Y. S., Lee, H. W., Chung, K. C., Hwang, D. Y., Kang, S. H., & Yoon, J. W. (2022, July). Superconducting MgB2 Wire Drawing Considering Anisotropic Hardening Behavior and Hydrostatic Effect. Metals and Materials International, 28(7), 1697-1710.
- Choi, H., Fazily, P., Park, J., Kim, Y., Cho, J. H., Kim, J., & Yoon, J. W. (2022, May). Artificial intelligence for springback compensation with electric vehicle motor component. International Journal of Material Forming, 15(3), 22.
- Hu, Q., Chen, J., & Yoon, J. W. (2022, April). A new asymmetric yield criterion based on Yld 2000-2d under both associated and non-associated flow rules: Modeling and validation. Mechanics of Materials, 167, 104245.
- Hu, Q., & Yoon, J. W. (2022, April). Anisotropic distortional hardening based on deviatoric stress invariants under non-associated flow rule. International Journal of Plasticity, 151, 103214.

**2021**

- Paresi, P. R., Narayanan, A., Lou, Y., & Yoon, J. W. (2021, November). Finite element modeling for orthogonal machining of AA2024-T351 alloy with an advanced fracture criterion. Journal of Manufacturing Science and Engineering, 143(11), 111003.
- Kim, J., Yoon, J. W., Kim, H., & Lee, S. U. (2021, October). Prediction of ballooning and burst for nuclear fuel cladding with anisotropic creep modeling during Loss of Coolant Accident (LOCA). Nuclear Engineering and Technology, 53(10), 3379-3397.
- Hu, Q., Yoon, J. W., & Stoughton, T. B. (2021, July). Analytical determination of anisotropic parameters for Poly6 yield function. International Journal of Mechanical Sciences, 201, 106467.
- Lou, Y., & Yoon, J. W. (2021, May). A user-friendly anisotropic ductile fracture criterion for sheet metal under proportional loading. International Journal of Solids and Structures, 217, 48-59.
- Hu, Q., & Yoon, J. W. (2021, May). Analytical description of an asymmetric yield function (Yoon2014) by considering anisotropic hardening under non-associated flow rule. International Journal of Plasticity, 140, 102978.
- Jang, D. P., Fazily, P., & Yoon, J. W. (2021, March). Machine learning-based constitutive model for J2-plasticity. International Journal of Plasticity, 138, 102919.
- Noh, D., Fazily, P., Yu, K., Lee, S., Ko, D. K., Sung, M. J., Huh, H., & Yoon, J. W. (2021, January). Prediction of Impact Fracture for Tungsten Alloy Using the Mohr-Coulomb Fracture Model. Transactions of Materials Processing, 30(1), 16-21.
- Paresi, P. R., Arunachalam, N., Lou, Y., & Yoon, J. W. (2021, January). Machinability studies of AA2024-T351 alloy with an uncoated carbide tool. Materials Today: Proceedings, 44, 1058-1064.
- Hu, Q., Yoon, J. W., Manopulo, N., & Hora, P. (2021, January). A coupled yield criterion for anisotropic hardening with analytical description under associated flow rule: Modeling and validation. International Journal of Plasticity, 136, 102882.

## 연락과 위치

- 교수 연구실: 기계동(N7) 4202호[^me], 누리집 표기 Room 4202, Building N7-3[^contact]
- 학생 연구실: Room 1202, Building N7-3, 전화 042-350-3273[^contact]
- 교수 전화: 042-350-3233[^me][^contact]
- 교수 이메일: j.yoon@kaist.ac.kr[^me][^prof]
[^p1]: D. Noh, J. W. Yoon, International Journal of Material Forming 17, 11 (온라인 2024-01-04). <https://doi.org/10.1007/s12289-023-01806-8> 초록 기준.
[^p2]: J. Park, J. W. Yoon, Journal of Mechanical Science and Technology 36, 6147-6156 (온라인 2022-11-30). <https://doi.org/10.1007/s12206-022-1129-z> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: D. P. Jang, P. Fazily, J. W. Yoon, International Journal of Plasticity 138, 102919 (2021). <https://doi.org/10.1016/j.ijplas.2020.102919> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: H. Choi 외, J. W. Yoon, International Journal of Material Forming 15, 22 (온라인 2022-03-11). <https://doi.org/10.1007/s12289-022-01671-x> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: I. Ga, J. W. Yoon, 2024 17th Hypervelocity Impact Symposium, V001T06A010 (온라인 2025-05-20). <https://doi.org/10.1115/hvis2024-068> 초록 기준.
[^p6]: D. Noh 외, J. W. Yoon, Journal of Mechanical Science and Technology 36, 4463-4474 (온라인 2022-09-02). <https://doi.org/10.1007/s12206-022-0811-5> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: C. Sagong, T. J. Jang, T. Ahn, J. W. Yoon, Solid State Phenomena 388, 141-151 (온라인 2026-04-15). <https://doi.org/10.4028/p-is64g3> 초록 기준.
[^p8]: P. R. Paresi, A. Narayanan, Y. Lou, J. W. Yoon, Journal of Manufacturing Science and Engineering 143, 111003 (온라인 2021-05-28). <https://doi.org/10.1115/1.4051057> 초록 기준.
[^home]: 연구실 누리집 첫 화면 <https://canesm.kaist.ac.kr/> (연구실 이름, 2026-10-23 열람)
[^research]: 연구실 누리집 Research 페이지 <https://canesm.kaist.ac.kr/ssup> (Research Focus, 연구 영역 세 묶음, 2026-10-23 열람)
[^history]: 연구실 누리집 History 페이지 <https://canesm.kaist.ac.kr/history> (1978년 설립, Dong-Yol Yang 교수 이력, 2016년 항목, 2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <https://canesm.kaist.ac.kr/People/professor> (Bio, Professional Experiences, Educational Background, Award, Honors, Publication, 이메일, 2026-10-23 열람)
[^students]: 연구실 누리집 Students 페이지 <https://canesm.kaist.ac.kr/People/students> (PH.D. Students, Master Students, 2026-10-23 열람)
[^postdocs]: 연구실 누리집 PostDocs 페이지 <https://canesm.kaist.ac.kr/People/postdocs> (Current, PasT, 2026-10-23 열람)
[^contact]: 연구실 누리집 Contact us 페이지 <https://canesm.kaist.ac.kr/contact-us> (교수실·학생실 위치와 전화, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publications 페이지 <https://canesm.kaist.ac.kr/pu> (Research Papers 181–213번, 2026-10-23 열람)
[^cr]: 2024–2026년 논문과 대표 논문의 출판사 등록 서지(Crossref) <https://api.crossref.org/> (교수 확인 기준은 근거 페이지, 2026-10-23 조회)
[^me]: KAIST 기계공학과 교수 상세(윤정환) <https://me.kaist.ac.kr/pop/team.html?uid=41&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 연구실 웹사이트, 이메일, 교수실, 전화, 2026-10-23 열람)

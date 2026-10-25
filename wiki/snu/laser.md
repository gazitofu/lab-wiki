# 레이저 연구실 (SNU Laser Laboratory)

**서울대학교 공과대학 전기·정보공학부 · 정윤찬 교수**

- 분야: 고출력 레이저와 결맞음 빔 결합, 광섬유 비선형 광학, 양자 광학, 메타물질·메타표면을 이용한 빛 제어
- 대분야: 물리·양자, 전기전자·반도체·광학
- 태그: 레이저 광원[^home][^lab], 비선형 광학[^research], 양자 광학·광양자 기술[^research], 메타물질·메타광학[^p1][^p2][^p7], 플라즈모닉스[^p2][^p7], 레이저·광 공정[^home], 라이다·3차원 거리 센싱[^home]
- 홈페이지: <https://laser.snu.ac.kr/>
- 근거와 출처: [레이저 연구실 근거 페이지](laser-sources.md)

> 여러 레이저의 빛을 맞춰 결합하는 제어, 광섬유 안에서 빛이 서로 영향을 주는 원리, 인공 광학 구조로 빛을 다루는 방법을 연구한다.[^home][^research][^p1][^p3]

## 무엇을 연구하나

서울대학교 전기·정보공학부 정윤찬 교수가 이끄는 연구실이다. 누리집은 SNU Laser Laboratory라는 이름을 쓰며, 고출력·고에너지 영역의 광학과 이를 이용한 광자 시스템 개발을 연구 목표로 제시한다. 광자(빛의 에너지를 양자 단위로 나타내는 입자)를 만들고 빛과 빛, 전자, 물질 사이의 상호작용을 다룬다.[^home][^prof]

한 갈래는 **여러 레이저를 결합해 빛을 제어하는 방법**이다. 결맞음 빔 결합(Coherent Beam Combining, CBC, 여러 빔의 위상을 맞춰 합치는 방법)은 빔마다 위상(파동의 한 주기 안에서 진동이 진행된 상태)을 조절해 목표 지점에 빛을 모은다. 연구실은 위상 제어 알고리즘을 연구하며, 반복해서 최적화하는 방법 외에 측정 영상으로 위상을 직접 구하는 방법도 검증한다. 광섬유(빛을 유도해 전달하는 섬유형 구조)에서 나온 빛의 세기 분포를 보고 모드(전자기장이 공간에 분포하는 고유한 형태)의 구성과 상대 위상을 알아내는 연구도 한다.[^research][^p3][^p4][^p5]

다른 갈래는 **광섬유의 비선형 현상과 인공 구조의 광학**이다. 비선형 광학(물질의 반응이 빛의 세기에 비례하지 않는 광학)을 통해 빛의 파장이 바뀌거나 여러 파동이 함께 작용하는 현상을 다룬다. 메타물질(인공 구조를 설계해 유전율 등 물질의 파동 응답을 조절하는 재료)과 메타표면(인공 구조를 표면에 배열해 빛을 제어하는 구조)의 전파 특성과 공진(특정 조건에서 파동 에너지가 계에 축적되는 현상)도 분석한다. 이를 바탕으로 공간 필터(영상의 공간적 변화 성분을 골라 통과시키는 장치)를 설계한다.[^research][^p8][^p1][^p7]

강한 레이저와 반대되는 영역에서는 개별 광자 수준의 빛을 다루는 양자 광학(빛과 물질의 상호작용을 양자적으로 다루는 광학)을 연구한다. 연구 소개는 빛의 압축 상태(빛의 서로 짝을 이루는 물리량 중 한쪽의 요동이 진공 상태 한계 아래에 놓인 상태)를 만드는 응용을 현재 연구 중이라고 적는다. 레이저 응용 주제로는 광 신경망(신경망의 계산을 빛으로 수행하는 구조), 레이저 삭마(레이저로 물질을 제거하는 과정), 짧은 펄스를 묶어 내보내는 방식, 레이저 보조 주사전자현미경(전자빔으로 표면을 훑어 영상을 얻는 장치)도 제시한다.[^research]

## 주요 연구 주제

### 빔 결합 제어와 빛의 분포 복원

결맞음 빔 결합은 여러 빔이 목표 면에서 함께 작용하도록 상대 위상을 맞추는 문제다. 연구실은 카메라로 얻은 세기 분포에서 위상을 구하는 해석적 모드 분해(측정된 빛을 기본 모드들의 합으로 나눠 구하는 계산)를 제안했다. 수치 계산과 실제 빔 결합 실험으로 이 방법을 확인하고, 빔 배열과 잡음이 결과에 미치는 영향도 분석했다.[^p3]

전자회로에서 실행할 제어 알고리즘도 연구한다. CLA-ES(Correspondence Lookup-table Adaptation Evolution Strategy, 빔 세기와 위상 분포의 대응 관계를 갱신하는 진화전략)는 복잡한 행렬 연산을 줄이는 방식이다. FPGA(Field-Programmable Gate Array, 제작 후 내부 논리 연결을 설정할 수 있는 반도체 회로)에 구현하는 것을 목표로 제안됐으며, 시뮬레이션에서 공분산 행렬 적응 진화전략(Covariance Matrix Adaptation Evolution Strategy, CMA-ES)의 수렴 성능과 비교했다.[^p4]

광학장 복원에서는 합성곱 신경망(국소 특징을 추출하는 계산을 반복해 자료의 패턴을 학습하는 신경망)으로 모드 계수의 초기값을 얻고, 최적화 알고리즘으로 이를 조정한다. 또 수차(광학계에서 이상적인 파동면과 실제 파동면이 어긋나는 현상)를 위상 이동 측정 자료로 분석한다. 실제 측정에서 얻은 수차의 통계적 특성을 이용해 학습 자료를 만들고, 두 번의 위상 이동 측정으로 수차를 복원하는 방법을 시험했다.[^p5][^p6]

### 광섬유에서의 비선형 상호작용

광섬유에서는 빛과 물질의 상호작용으로 파장과 파형이 달라질 수 있다. 연구 소개는 초연속광(넓은 파장 범위에 연속적으로 분포하는 빛), 솔리톤(비선형 효과와 파동의 퍼짐이 균형을 이뤄 형태를 유지하는 파동), 비선형 파동 현상을 다룬다.[^research] 대표 논문은 유도 브릴루앙 산란(빛과 물질의 음향 진동이 상호작용하며 산란광이 증폭되는 현상)과 사광파 혼합(비선형 매질에서 네 광파가 상호작용하는 현상)을 함께 고려한다. 광섬유 끝에서 되반사된 빛이 있을 때 두 과정이 어떻게 서로 약화하거나 강화하는지 이론적으로 분석했다.[^p8]

### 메타물질·메타표면과 공간 필터

쌍곡 메타물질(주된 방향에 따라 유전율의 부호가 달라지는 메타물질)은 빛의 전파 방향과 파장 관계를 분석하는 대상이다. 연구실은 복소수(실수 부분과 허수 부분을 함께 갖는 수)로 표현한 유전율을 이용해 이 물질의 파동벡터(파동의 진행 방향과 공간적 변화를 나타내는 양)를 유한한 닫힌 표면으로 설명하는 방법을 제안했다. 서로 다른 적층 구조에 적용해 기존의 쌍곡면 표현에서 나타나는 무한한 파동벡터 문제를 다뤘다.[^p1]

플라즈모닉스(금속의 집단적인 전자 진동과 빛의 상호작용을 다루는 분야)를 이용한 메타표면에서는 나노슬릿(나노미터 규모의 좁은 틈)을 통과하는 빛의 공진을 연구한다. 여러 공진의 결합으로 입사각에 따른 투과 특성이 생기는 원리를 설명하고, 영상에서 공간 주파수(공간을 따라 밝기 등이 반복해 변하는 빈도)를 골라 통과시키는 필터의 설계 규칙을 수치적으로 확인했다.[^p7] 이어 폭이 점차 변하는 슬릿 구조의 여러 공진을 분석해, 하나의 메타표면에서 파장에 따라 저역통과·고역통과 필터 기능이 달라질 수 있음을 보였다. 저역통과는 공간적 변화가 완만한 성분을, 고역통과는 공간적 변화가 급한 성분을 통과시키는 방식이다.[^p2]

### 양자 광학과 레이저 응용

양자 광학에서는 개별 광자 수준의 방출을 설명하기 위해 빛의 전자기장과 방출체의 에너지 준위(계가 가질 수 있는 에너지 상태)를 함께 양자화(물리량과 그 관계를 양자역학의 규칙으로 표현하는 절차)해 다룬다. 현재 연구 소개는 압축 상태 생성 응용을 제시한다.[^research] 응용 연구에서는 광 신경망과 레이저 삭마 등을 다루며, 학과 연구실 소개는 라이다(Light Detection and Ranging, 빛을 이용해 거리를 측정하는 기술), 원격 센싱, 재료의 미세 가공을 연구 관심으로 적는다.[^research][^lab]

## 대표 논문

서울대 재직 시기의 최근 연구에서 빔 결합·광학장 복원, 메타광학, 광섬유 비선형 현상을 다루는 8편을 골랐다. 「쉽게 말하면」은 각 논문의 게시 초록만을 근거로 썼다. 연도는 연구실 논문 목록을 따르며, 논문 페이지의 날짜 표기가 다른 경우는 근거 페이지에 적었다.[^pubs]

| 번호 | 연도 | 논문 · 발표지 | 쉽게 말하면 | 교수 역할 |
|---|---|---|---|---|
| 1 | 2026 | [Complex Analysis of the K-Surface for Hyperbolic Metamaterials](https://doi.org/10.1109/JQE.2026.3691680) · IEEE Journal of Quantum Electronics | 쌍곡 메타물질을 유효매질 이론으로 다룰 때 무한한 파동벡터가 허용되는 문제를 살폈다. 복소 유전율을 쓰는 표현을 제안하고 두 종류의 적층 구조에 적용했다. 파동벡터의 실수 부분과 허수 부분을 유한한 닫힌 표면으로 표현해 기존 표현과 유효매질 가정 사이의 불일치를 다뤘다.[^p1] | 교신·마지막 저자 정윤찬 |
| 2 | 2026 | [Role of resonances in tapered bi-modal plasmonic nanoslit metasurfaces for multi-functional nonlocal spatial filtering](https://doi.org/10.1364/JOSAB.585450) · Journal of the Optical Society of America B | 폭이 점차 변하는 금속 나노슬릿 메타표면에서 여러 공진이 어떤 역할을 하는지 분석했다. 빛이 틈을 따라 진행하는 현상과 입사각·파장에 따른 결합을 함께 살펴 설계 지침을 제시했다. 수치 계산에서 하나의 메타표면이 파장에 따라 서로 다른 공간 필터로 작용할 수 있음을 보였으며, 광 계산과 계산 영상에 활용할 가능성을 제시했다.[^p2] | 교신·마지막 저자 정윤찬 |
| 3 | 2025 | [Direct Phase-Locking Algorithm for Tiled-Aperture Coherent Beam Combing Systems](https://doi.org/10.1109/JLT.2025.3594715) · Journal of Lightwave Technology | 여러 빔을 결합할 때 목표 면의 세기 영상으로 각 빔의 위상을 직접 구하는 방법을 제안했다. 해석적 모드 분해를 이용해 중심 부분에 빛이 모이도록 하며, 수치 계산과 실제 빔 결합 실험으로 가능성을 확인했다. 잡음에 대한 민감도가 영상 무늬의 상관관계와 어떻게 연결되는지도 분석했다.[^p3] | 교신·마지막 저자 정윤찬 |
| 4 | 2025 | [Phase Control Algorithms for CBC Systems Based on Evolutionary Strategy for Implementation on FPGA Boards](https://doi.org/10.1109/JLT.2025.3594709) · Journal of Lightwave Technology | 빔 결합 채널이 늘어날 때 위상 제어를 전자회로에서 계산하기 어렵다는 문제를 다뤘다. 빔 세기와 위상 분포 사이의 대응 관계를 이용하는 CLA-ES 알고리즘을 제안해 복잡한 행렬 연산을 줄였다. 시뮬레이션에서는 비교 대상인 CMA-ES와 비슷한 수렴 성능을 유지하면서 계산 효율을 높일 수 있음을 보였다. 실제 회로에 구현하는 것을 목표로 한 알고리즘 연구다.[^p4] | 교신·마지막 저자 정윤찬 |
| 5 | 2023 | [Convolutional Neural Network Combined With Stochastic Parallel Gradient Descent to Decompose Fiber Modes Based on Far-Field Measurements](https://doi.org/10.1109/JLT.2023.3276366) · Journal of Lightwave Technology | 광섬유에서 나온 빛의 원거리 세기 분포를 측정해 어떤 모드가 섞였는지 알아냈다. 합성곱 신경망이 모드 계수의 초기값을 주고, 확률적 병렬 경사하강법이 이를 조정한다. 신경망에서 해가 모호해지는 문제를 위상 차이의 표시 방법으로 다뤘으며, 수치 계산과 저장 영상·실시간 영상 실험으로 방법을 확인했다.[^p5] | 교신·마지막 저자 정윤찬 |
| 6 | 2023 | [Noise robust Zernike phase retrieval via learning based algorithm only with 2-step phase shift measurements](https://doi.org/10.1364/OE.497310) · Optics Express | 위상 이동 측정 자료를 이용해 잡음에 강하게 수차를 복원하는 학습 방법을 제안했다. 실제 측정에서 얻은 수차의 통계 분포를 바탕으로 합성 학습 자료를 만든 뒤 신경망을 학습했다. 두 번 측정한 자료를 쓰는 방법을 네 번 측정한 자료에 기반한 반복 계산 방법들과 비교했으며, 수치 시험과 실제 수차 측정에서 복원 성능을 확인했다.[^p6] | 마지막 저자 정윤찬 |
| 7 | 2023 | [Engineering angle selectivity of extraordinary optical transmission and nonlocal spatial filtering](https://doi.org/10.1364/JOSAB.496551) · Journal of the Optical Society of America B | 금속 나노슬릿 메타표면이 특정 입사각의 빛을 잘 통과시키는 원리를 분석했다. 여러 공진이 강하게 결합하면서 각도 선택성이 생긴다는 설명을 바탕으로 저역통과·대역통과 공간 필터의 설계 규칙을 세우고 수치적으로 확인했다. 메타표면의 크기가 유한할 때 나타나는 영향도 계산하고, 광학 영상용 공간 필터에 활용할 가능성을 제시했다.[^p7] | 교신·마지막 저자 정윤찬 |
| 8 | 2022 | [Study on the asymptotic behavior of the interplay of stimulated Brillouin scattering and Brillouin-enhanced four-wave mixing in standard single-mode fibers](https://doi.org/10.1007/s40042-021-00330-9) · Journal of the Korean Physical Society | 단일모드 광섬유에서 유도 브릴루앙 산란과 브릴루앙 증강 사광파 혼합을 함께 이론적으로 다뤘다. 광섬유 끝에서 빛이 일부 되반사되는 상황에서 두 과정의 상호작용을 분석했다. 주어진 가정 아래 해석해와 극한에서의 식을 구해 서로 약화하거나 강화하는 조건을 설명했으며, 고출력 광섬유 시스템의 설계·분석에 활용할 수 있다고 제시했다.[^p8] | 마지막 저자 정윤찬 |

## 교수와 전문 분야

정윤찬 교수는 서울대학교에서 광섬유·비선형 광학 연구로 1999년 박사학위를 받았다. 이후 같은 대학에서 박사후연구를 했고, 2001년 영국 사우샘프턴대학교 Optoelectronics Research Centre에 Research Fellow로 합류해 2006년 Reader가 됐다. 연구실 교수 소개는 2010년 서울대 교원으로 복귀했으며 현재 정교수라고 적는다. 학과 교수 상세 페이지는 「정윤찬 교수」, 연구 분야는 「레이저 및 양자전자」로 표기한다.[^prof][^faculty]

교수 소개는 광섬유·도파로·양자·비선형 광학, 홀로그래피(빛의 간섭 정보를 기록하고 재현하는 방법), 입체 디스플레이와 메타표면을 연구 관심으로 든다.[^prof] 최근 대표 논문을 기준으로 보면 전문 분야는 레이저 빔의 위상 제어와 광학장 복원, 비선형 광섬유 현상, 메타물질의 전파 이론과 메타표면 공간 필터 설계로 이어진다.[^p3][^p4][^p5][^p6][^p8][^p1][^p2][^p7]

## 응용 분야

학과 연구실 소개는 고출력 광섬유 레이저·증폭기, 빔 결합을 통한 출력 확장, 초고속·광대역 광원을 개발 대상으로 적는다. 응용 관심으로는 미세·나노 재료 가공, 레이저 조명·디스플레이, 생체 영상, 자유공간·수중에서의 거리 측정과 라이다를 제시한다.[^lab] 최근 논문에서는 빔 결합의 위상 제어와 광학장 측정, 메타표면을 이용한 광 계산·영상용 공간 필터의 가능성을 다룬다.[^p3][^p5][^p2][^p7]

## 구성원

2026년 10월 25일 Students 페이지 기준으로 박사과정 7명, 석사과정 4명, 학부 학생 3명이다. 과정과 연구 주제는 페이지 표기이며 시작 시점은 적혀 있지 않다. 「대표 논문 참여」는 위 표의 번호이며, 논문 페이지의 전체 이름과 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^students]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Juhwan Kim | 박사과정 | Quantum Optics, Nonlinear Optics | kjh2653350@snu.ac.kr |  |
| Hyungu Kang | 박사과정 | Quantum Optics, Nonlinear Fiber Optics | khgkgg@snu.ac.kr |  |
| Hyesun Cha | 박사과정 | Nonlinear Optics | hcha12@snu.ac.kr |  |
| Chaeyoung Lee | 박사과정 | Laser ablation, Nonlinear Optics | antimate@snu.ac.kr |  |
| Hongjae Jung | 박사과정 | Nonlinear Fiber Optics | wjdghdwp8096@snu.ac.kr |  |
| Yeeun Kim | 박사과정 | Optical Sensing Application | pine422@snu.ac.kr |  |
| Haesung Lee | 박사과정 | Optical Neural Network, Metasurface | jimmy3396@snu.ac.kr | 1 |
| Sungjong Park | 석사과정 | High power laser | 6474park@snu.ac.kr |  |
| Donghan Jung | 석사과정 | Quantum Optics, Optical Solitons, Scanning Electron Microscopy | ggullamul@snu.ac.kr |  |
| Sukjun Lee | 석사과정 | Optical Neural Network | kevin7598@snu.ac.kr |  |
| Daejin Kim | 석사과정 | Optical Phased Array, Laser Ablation | daejin3506@snu.ac.kr |  |
| Heechang Kim | 학부 연구생 | Metasurface Optimization | heechang.kim@snu.ac.kr |  |
| Chanyong Jeong | 학부 연구생 | Optical Neural Network | cyjeong@snu.ac.kr |  |
| Seunghyun Yeo | 학부 연구생 | Optical Neural Network, Me tasurface | shyeo0517@snu.ac.kr |  |

## 졸업생과 이전 구성원

2026년 10월 25일 Alumni 페이지에 게시된 25명이다. 구획은 Research Professor 2명, Ph. D. 13명, M.S. 10명이며, 첫 구획은 학위가 아니라 이전 직위다. 연도와 학위 논문은 기재돼 있지 않다. 진로는 페이지의 기관·직위 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Luis Alonso Vazquez-Zuniga | Research Professor | Calmar Laser |
| Hansol Kim | Research Professor | Assistant Professor, Sejong University, QISE |
| Hyuntai Kim | Ph. D. | Professor, Hongik University, EE |
| Youngchul Kwon | Ph. D. | Samsung Electronics - Test & Package Center |
| Seungjong Lee | Ph. D. | Samsung Electronics - Semiconductor R&D Center |
| Jinseob Kim | Ph. D. | Samsung Electronics - Mechatronics R&D Center |
| Seungsoo Hong | Ph. D. | Samsung Display - Mobile Display Business |
| Kyoungyoon Park | Ph. D. | Samsung Electronics - Semiconductor R&D Center |
| Seungsu Lee | Ph. D. | Samsung Electronics - Semiconductor R&D Center |
| Hanbyul Chang | Ph. D. | Samsung Electronics - Mobile eXperience Business |
| Mingon Han | Ph. D. | Samsung Electronics - DS Memory Business |
| Jeongkyun Na | Ph. D. | Samsung Electronics - Semiconductor R&D Center |
| Minsu Yeo | Ph. D. | Samsung Electronics -  Mobile eXperience Business |
| Byungho Kim | Ph. D. | Samsung Electronics - Semiconductor R&D Center |
| Hyukjin Yang | Ph. D. | SK Hynix - DRAM(HBM) PE System Lab |
| Geunchang Choi | M.S. | Associate Professor, Chung-Ang University, ECE |
| Hunmin Cho | M.S. | SUALAB |
| Byungsun Jeong | M.S. | Kim & Chang |
| Dongyoung Lee | M.S. | Samsung Electronics |
| Dongyeul Lee | M.S. | Samsung Electronics - Semiconductor R&D Center |
| Haechan An | M.S. | PostDoc at University of Chicago |
| Jeonghoon Woo | M.S. | Samsung Display |
| Jangwon Son | M.S. | DUDAJI |
| Meerin Park | M.S. | Samsung Electronics - DS Memory Business |
| Seunghyun Ahn | M.S. | Ph.D course at ECE, Seoul National University |

## 최근 논문 목록 (2021–2026)

연구실 Publications의 「Recent Publications (selected)」에 실린 논문 중 18편이다. 연도와 제목·저자·발표지 표기는 연구실 목록을 따르며, 2021년 논문은 그해 전체를 포함한다. 이 목록 자체가 연구실의 선정 목록이다.[^pubs]

**2026**

- M. Kim, H. Lee, and Y. Jeong. "Complex Analysis of the K-Surface for Hyperbolic Metamaterials". *IEEE J. Quantum Electron. 62(4):7300116 (2026)*.
- H. Chang, M. Yeo, S. Kim, H. Lee, S. Kim, and Y. Jeong. "Role of Resonances in Tapered Bi-model Plasmonics Nanoslit Metasurfaces for Multi-functional Nonlocal Spatial Filtering". *J. Opt. Soc. Am. B 43(3), 496-500 (2026)*.

**2025**

- K. Park, Y. Jeong, and H. Kim. "Numerical Analysis of Square Graded-index Optical Waveguides". *Curr. Opt. Photonics 9(5), 560-565 (2025)*.
- B. Kim, J. Na, C. Jun, and Y. Jeong. "Direct Phase-Locking Algorithm for Tiled-Aperture Coherent Beam Combining Systems". *J. Light. Technol. 43(18), 85 75-8585 (2025)*.
- M. Yeo, H. Kim, and Y. Jeong. "Phase Control Algorithms for CBC Systems Based on Evolutionary Strategy for Implementation on FPGA Boards". *J. Light. Technol. 43(18) 8563-8574 (2025)*.

**2024**

- J. Na, B. Kim, C. Jun, and Y. Jeong. "Analysis of Major Error Factors in Coherent Beam Combination: Phase, Tip Tilt, Polarization Angle, and Beam Quality". *Curr. Opt. Photonics 8(4), 406-415 (2024)*.
- K. Kim, T. Choi, S. Choi, H. Kim, Y. Lee, S. Kim, B. Lee, and Y. Jeong. "Multi-Objective Optimization of Dynamic VO 2 Metagrating: Broadband Polarization-Independent Transmission Modulator". *Opt. Express 32(19), 32 680-32690 (2024)*.
- H. Son, T. Choi, K. Kim, Y. Kim, J. Bang, S. Kim, B. Lee, and Y. Jeong. "Strong Coupling Induced Bound States in the Continuum in a Hybrid Metal-Dielectric Bilayer Nanograting Resonator". *ACS Photonics 11(8), 3221-3231 (2024)*.
- H. Kim, M. Yeo, and Y. Jeong. "Combinatorial Study of Coherent Multi-Channel Phase-Locking Based on Covariance Matrix Adaptation Evolution Strategy". *J. Korean. Phys. Soc. 85, 406-414 (2024)*.
- M. Yeo, B. Kim, H. Kim, and Y. Jeong. "Channel Phase Extraction for a Coherent Beam Combining System Using a 2D Target Intensity Image and the CMA-ES Algorithm". *J. Korean. Phys. Soc. 85, 120-128 (2024)*.

**2023**

- H. Chang, M. Yeo, S. Kim, and Y. Jeong. "Engineering Angle Selectivity of Extraordinary Optical Transmission and Nonlocal Spatial Filtering". *J. Opt. Soc. Am. B 40(10), 2576-2585 (2023)*.
- B. Kim, J. Na and Y. Jeong. "Convolutional Neural Network Combined With Stochastic Parallel Gradient Descent to Decompose Fiber Modes Based on Far-Field Measurements". *J. Light Technol. 41(18), 5973-5982 (2023)*.
- H. Kim, Y. Jeong, K. Lee, and Y. Jeong. "Noise robust Zernike phase retrieval via learning based algorithm only with 2-step phase shift measurements". *Opt. Express 31, 30248-30266 (2023)*.

**2022**

- S. Lee, Y. Lim, H. Kim, D. Seo, J. Na, H. Kim, K. Nam, and Y. Jeong. "Random Lasing with a High Degree of Circular Dichroism by Chiral Plasmonic Gold Nanoparticles". *ACS Photonics 9(2), 613–620 (2022)*.
- K. Park, Achar V. Harish, Johan Nilsson, and Y. Jeong. "Study on the asymptotic behavior of the interplay of stimulated Brillouin scattering and Brillouin‑enhanced four‑wave mixing in standard single‑mode fibers". *J. Korean Phys. Soc. 80(1), 37–52 (2022)*.

**2021**

- S. Lee, H. Kim, and Y. Jeong. "Angular distribution of luminescence dissymmetry observed from a random laser built upon the exocuticle of the scarab beetle Chrysina gloriosa". *Opt. Express 29(23), 37712-37721 (2021)*.
- B. Kim, J. Na, J. Kim, H. Kim and Y. Jeong. "Modal decomposition of fiber modes based on direct far-field measurements at two different distances with a multi-variable optimization algorithm". *Opt. Express, 29(14), 21502-21520 (2021)*.
- H. Kim and Y. Jeong. "Covariance matrix adaptation evolution strategy based optical phase control". *Electron. Lett. 57(13), 517-519 (2021)*.

## 연락과 위치

- 교수 사무실: 301-1105[^prof]
- 학생 연구실: 301-717, 301-718[^students]
- 교수 이메일: yoonchan@snu.ac.kr[^prof]
- 교수 전화: 02-880-1623[^faculty]
- 연구실 상세 페이지 전화: 880-1788[^lab]
[^home]: SNU Laser Laboratory, Home, 연구 목적·주요 관심과 응용. <https://laser.snu.ac.kr/> (열람 2026-10-25).
[^prof]: SNU Laser Laboratory, Professor, Yoonchan Jeong 소개·경력·사무실·학교 이메일. <https://laser.snu.ac.kr/members/professor> (열람 2026-10-25).
[^research]: SNU Laser Laboratory, Research, Coherent Beam Combining·Fiber-Optic Transmission Dynamics·Quantum Optics·Laser Applications. <https://laser.snu.ac.kr/research> (열람 2026-10-25).
[^lab]: 서울대학교 전기·정보공학부, 레이저 연구실 상세 소개, 이름·지도교수·연구 개발 대상과 응용·전화. <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=106> (열람 2026-10-25).
[^faculty]: 서울대학교 전기·정보공학부, 정윤찬 교수 상세 소개, 직위·연구 분야·전화. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p073> (열람 2026-10-25).
[^students]: SNU Laser Laboratory, Students, 현재 학생의 과정·연구 주제·학교 이메일·연구실. <https://laser.snu.ac.kr/members/students> (열람 2026-10-25).
[^alumni]: SNU Laser Laboratory, Alumni, 이전 구성원 구획과 진로 표기. <https://laser.snu.ac.kr/members/alumni> (열람 2026-10-25).
[^pubs]: SNU Laser Laboratory, Publications, Recent Publications (selected). <https://laser.snu.ac.kr/publications> (열람 2026-10-25).
[^p1]: M. Kim, H. Lee, Y. Jeong, IEEE Journal of Quantum Electronics 62, 7300116 (2026). <https://doi.org/10.1109/JQE.2026.3691680> 초록 기준(ResearchGate 등록 초록). 초록: <https://www.researchgate.net/publication/404671745_Complex_Analysis_of_the_K-surface_for_Hyperbolic_Metamaterials>.
[^p2]: H. Chang 외, Y. Jeong, Journal of the Optical Society of America B 43, 496-500 (온라인 2026-02-17). <https://doi.org/10.1364/JOSAB.585450> 초록 기준(ResearchGate 등록 초록). 초록: <https://www.researchgate.net/publication/400283795_Role_of_resonances_in_tapered_bi-modal_plasmonic_nanoslit_metasurfaces_for_multi-functional_nonlocal_spatial_filtering>.
[^p3]: B. Kim, J. Na, C. Jun, Y. Jeong, Journal of Lightwave Technology 43, 8575-8585 (온라인 2025-08-01). <https://doi.org/10.1109/JLT.2025.3594715> 초록 기준(ResearchGate 등록 초록). 초록: <https://www.researchgate.net/publication/394228953_Direct_phase-locking_algorithm_for_tiled-aperture_coherent_beam_combing_systems>.
[^p4]: M. Yeo, H. Kim, Y. Jeong, Journal of Lightwave Technology 43, 8563-8574 (온라인 2025-08-01). <https://doi.org/10.1109/JLT.2025.3594709> 초록 기준(ResearchGate 등록 초록). 초록: <https://www.researchgate.net/publication/394232905_Phase_control_algorithms_for_CBC_systems_based_on_evolutionary_strategy_for_implementation_on_FPGA_boards>.
[^p5]: B. Kim, J. Na, Y. Jeong, Journal of Lightwave Technology 41, 5973-5982 (온라인 2023-05-16). <https://doi.org/10.1109/JLT.2023.3276366> 초록 기준(ResearchGate 등록 초록). 초록: <https://www.researchgate.net/publication/370828437_Convolutional_neural_network_combined_with_stochastic_parallel_gradient_descent_to_decompose_fiber_modes_based_on_far-field_measurements>.
[^p6]: H. Kim, Y. Jeong, K. Lee, Y. Jeong, Optics Express 31, 30248-30266 (2023). <https://doi.org/10.1364/OE.497310> 초록 기준(PubMed 등록 초록). 초록: <https://pubmed.ncbi.nlm.nih.gov/37710571/>.
[^p7]: H. Chang, M. Yeo, S.-J. Kim, Y. Jeong, Journal of the Optical Society of America B 40, 2576-2585 (온라인 2023-09-12). <https://doi.org/10.1364/JOSAB.496551> 초록 기준(ResearchGate 등록 초록). 초록: <https://www.researchgate.net/publication/373405702_Engineering_angle_selectivity_of_extraordinary_optical_transmission_and_nonlocal_spatial_filtering>.
[^p8]: Park Kyoungyoon, Harish A.V., Johan Nilsson, Yoonchan Jeong, Journal of the Korean Physical Society 80(1), 랩 목록 37–52 (2022); 논문 페이지 날짜 2021년 12월. <https://doi.org/10.1007/s40042-021-00330-9> 초록 기준(ResearchGate 등록 초록). 초록: <https://www.researchgate.net/publication/357241703_Study_on_the_asymptotic_behavior_of_the_interplay_of_stimulated_Brillouin_scattering_and_Brillouin-enhanced_four-wave_mixing_in_standard_single-mode_fibers>.

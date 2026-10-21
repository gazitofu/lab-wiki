# 비평형 기체 플라즈마 연구실 (KAIST Non-equilibrium Gas and Plasma Dynamics Lab, KNGPDL)

**KAIST 항공우주공학과 · 전은지 교수**

- 분야: 희박 기체 역학, 극초음속 비평형 유동 해석, 입자 기반 계산 기법(DSMC, 포커–플랑크, BGK), 대기 흡입형 전기 추진, 플라즈마 플룸(추력기에서 뿜어져 나가는 배기 기둥) 해석, 초저궤도 위성의 기체–표면 상호작용
- 대분야: 기계·로봇·제조, 물리·양자
- 태그: 희박 기체 역학[^p1][^p2][^kinetic], 우주 전기 추진[^ep][^p4][^p5], 극초음속 공기열역학[^p8][^gsi][^hypersonic]
- 홈페이지: <https://kngpdl.kaist.ac.kr/>
- 근거와 출처: [KNGPDL 근거 페이지](kngpdl-sources.md)

> 우주에서처럼 공기가 아주 희박하거나 극초음속으로 나는 물체 주변처럼 공기 상태가 급변하는 곳의 기체 흐름을, 기체 분자 하나하나의 움직임을 따라가는 계산으로 푸는 연구실이다. 대기권 재진입 비행체, 재사용 로켓, 아주 낮은 궤도를 도는 위성의 전기 추진기 설계에 쓰인다.[^home][^lab]

## 무엇을 연구하나

연구실은 우주의 희박한 영역, 밀도가 급변하는 영역, 극초음속처럼 극한 조건의 유체·열역학을 계산하는 수치 기법을 개발한다고 소개한다. 이런 흐름은 평형에서 벗어나 있어(비평형) 보통의 전산유체역학(CFD)이 쓰는 나비에–스토크스 방정식 대신, 기체 입자의 움직임을 다루는 기본 방정식인 볼츠만 방정식에 기반한 입자 계산이 필요하다.[^home] 학과 소개는 행성 간 탐사선이 목적 행성에 들어가거나 지구로 돌아올 때 안정적인 대기권 진입을 위해 꼭 필요한 연구이며, 우주 비행체의 화학·전기 추력기(홀 추력기, 이온 추력기 등) 개발에도 쓰인다고 적는다.[^lab]

첫 번째 갈래는 **희박 기체 계산 모델**이다. 볼츠만 방정식은 직접 풀기 어려워, 분자 충돌을 연속적인 무작위 과정으로 근사하는 포커–플랑크(FP) 방법과 충돌을 이완 과정으로 근사하는 BGK 방법을 연구한다. 포커–플랑크 방법은 여러 규모가 섞인 흐름에서 볼츠만 방정식보다, BGK 방법은 연속체에 가까운 영역에서 직접 모사 몬테카를로(DSMC, 분자 충돌을 무작위로 모사하는 표준 방법)보다 효율적일 수 있다.[^kinetic] 연구실의 개선된 포커–플랑크 모델은 실린더 주위 극초음속 흐름에서 DSMC보다 네 배 빨랐다.[^p1] 연구실은 정확도를 2차로 높인 입자 FP 모델,[^p1] 여러 기체가 섞인 흐름을 다루는 다중 이완 BGK 모델을 만들었고,[^p2] BGK 방법들을 속도 분포 함수(입자 속도가 퍼진 모양)로 평가했다.[^p3]

두 번째 갈래는 **전기 추진과 플라즈마 플룸**이다. 지구에 아주 가까운 초저궤도(VLEO)는 발사 비용을 줄이고 위성 성능을 높일 수 있지만, 희박한 대기가 만드는 항력을 메우지 않으면 위성 궤도가 일찍 낮아진다. 연구실은 주변의 희박한 대기를 추진제로 빨아들여 쓰는 대기 흡입형 전기 추진(ABEP)을 연구한다.[^ep] 극저온 판에 기체를 얼렸다가 다시 기체로 되돌려 추진제로 쓰는 흡입 장치를 제안했고,[^p4] 원자 산소를 쓰는 이온 추력기의 플라즈마 배기가 위성 쪽으로 되돌아오는 현상,[^p5] 이온 액체를 쓰는 전기 분무 추력기 배기의 중화(양이온과 전자가 섞여 전기적으로 중성이 되는 것) 과정을 계산했다.[^p6]

세 번째 갈래는 **기체–표면 상호작용과 재진입 공기열역학**이다. 초저궤도 위성의 항력과 재진입 비행체의 표면 가열을 정확히 예측하려면 기체 분자가 표면에 부딪혀 튕겨 나가거나 반응하는 과정을 제대로 모델링해야 한다.[^gsi][^hypersonic] 연구실은 입사 속도에 따라 표면 요철의 영향이 커지는 산란 모델,[^p7] 재진입 때 표면에서 원자가 다시 결합하며 내놓는 열이 표면으로 얼마나 전달되는지를 반응 경로별로 다루는 모델을 만들었다.[^p8]

연구 페이지는 이 밖에 고체 로켓 배기의 산화알루미늄 입자, 달 착륙선 배기와 달 표토 입자, 토성 위성 엔셀라두스의 분출물처럼 기체와 고체 입자가 섞인 희박 다상 유동도 다룬다.[^multiphase]

## 주요 연구 주제

### 1. 입자 기반 희박 기체 계산 모델

2차 정확도 포커–플랑크, 혼합 기체 BGK, 속도 분포 함수 평가.[^p1][^p2][^p3][^kinetic] 대표 논문 1, 2, 3.

### 2. 대기 흡입형 전기 추진과 플라즈마 플룸

극저온 흡입 장치, 이온 추력기 플룸, 전기 분무 추력기.[^p4][^p5][^p6][^ep] 대표 논문 4, 5, 6.

### 3. 기체–표면 상호작용과 재진입 가열

속도 의존 표면 산란, 반응 경로별 화학 에너지 수용.[^p7][^p8][^gsi] 대표 논문 7, 8.

## 대표 논문

랩 국제 학술지 목록의 2022–2026년 논문 가운데 교수가 교신저자(*)인 것에서 주제별로 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2024 | [A second-order particle Fokker-Planck model for rarefied gas flows](https://doi.org/10.1016/j.cpc.2024.109323) · Computer Physics Communications | DSMC는 계산 격자와 시간 간격을 아주 작게 잡아야 해서 희박도가 섞인 흐름에 쓰기 어렵다. 기존 1차 정확도 입자 FP 방법을 개선한 통합 확률 입자 모델(USP-ESFP)과 공간 보간법을 제안해, 전단 응력과 열 흐름 예측 정확도를 높였다.[^p1] | 1저자 Sanghun Kim, 교신 전은지 |
| 2 | 2026 | [A particle multi-relaxation Bhatnagar–Gross–Krook method for rarefied monatomic gas mixtures](https://doi.org/10.1063/5.0340698) · Physics of Fluids | 여러 종류의 단원자 기체가 섞인 희박 흐름에서 기체 쌍마다 따로 이완하도록 BGK 모델을 넓혔다. 균일 이완, 확산, 압력으로 미는 관 속 흐름(포아죄유 흐름), 두 판 사이 끌림 흐름(쿠에트 흐름), 실린더 주위 극초음속 흐름의 다섯 시험에서 DSMC와 잘 맞게 기체별 비평형 거동을 잡아냈다. 시간 간격을 충분히 크게 잡으면 DSMC보다 효율적이지만, 1차 정확도라 고차 방식으로 더 개선할 여지가 있다.[^p2] | 1저자 Inchan Kim, 교신 전은지 |
| 3 | 2024 | [Evaluation of stochastic particle Bhatnagar–Gross–Krook methods with a focus on velocity distribution function](https://doi.org/10.1063/5.0189872) · Physics of Fluids | 두 가지 BGK 방법을 평균값 대신 입자 속도 분포 함수 자체로 DSMC와 비교했다. 고차 평균값 비교로는 결과가 엇갈렸지만 속도 분포로 보면 샤코프 BGK(열전도 성질을 보정한 BGK 변형)가 비평형 상태를 더 정확히 재현했다.[^p3] | 1저자 Woonghwi Park, 교신 전은지 |
| 4 | 2024 | [Design and Operational Concept of a Cryogenic Active Intake Device for Atmosphere-Breathing Electric Propulsion](https://www.sciencedirect.com/science/article/pii/S1270963824004310) · Aerospace Science and Technology | 초저궤도의 희박한 대기를 모아 압축하는 흡입 장치로, 극저온 판에 기체를 응축했다가 다시 기체로 되돌려 추진제로 쓰는 방식(CRAID)을 제안했다. DSMC 계산에서 기존 깔때기형 수동 흡입 장치보다 흡입 성능이 크게 좋아져 추력기 운용 조건을 넘었다.[^p4] | 1저자 Geonwoong Moon, 교신 전은지 |
| 5 | 2023 | [Plasma plume simulation of an atomic oxygen-fed ion thruster in very-low-earth-orbit](https://doi.org/10.1088/1361-6595/ad15b0) · Plasma Sources Science and Technology | 원자 산소를 추진제로 쓰는 이온 추력기의 플라즈마 배기를 해석 모델과 입자 계산(전하 입자는 PIC, 중성 입자는 DSMC로 다루는 결합 방법)으로 모사했다. 배기 이온이 옆으로 퍼지며 위성 쪽으로 되돌아오는 현상(역류)이 나타났다.[^p5] | 1저자 Geonwoong Moon, 교신 전은지 |
| 6 | 2025 | [Analysis of oscillatory local neutralization according to fragmentation in the ionic liquid electrospray thruster plume](https://doi.org/10.1063/5.0249312) · Physics of Plasmas | 이온 액체를 쓰는 전기 분무 추력기의 배기에서 이온 덩어리가 쪼개지는 현상이 이온 진동과 배기 중화에 주는 영향을 일곱 경우로 계산했다. 배기 중심 근처에 진동하는 이온이 모였고, 쪼개짐으로 생긴 이온이 진동 주파수를 높였다.[^p6] | 1저자 Insang Park, 교신 전은지 |
| 7 | 2025 | [Velocity-dependent surface corrugation in gas–surface scattering](https://doi.org/10.1063/5.0276122) · Physics of Fluids | 빠르게 부딪히는 분자일수록 표면 깊숙이 들어가 표면의 울퉁불퉁함을 더 크게 느끼는 점을 반영해, 입사 속도에 따라 요철 정도가 바뀌는 표면 산란 모델을 만들고 물리적 대칭성(가역성)을 지키도록 했다.[^p7] | 1저자 Woonghwi Park, 교신 전은지 |
| 8 | 2024 | [Mechanism-specific chemical energy accommodation with finite-rate surface chemistry in non-equilibrium flow](https://doi.org/10.1063/5.0222518) · Physics of Fluids | 재진입 때 비행체 표면에서 원자가 다시 결합하면 열이 나는데, 이 열이 표면으로 가는 정도가 결합 경로마다 다르다는 점을 DSMC 표면 화학 모델에 넣어 표면 열 흐름을 더 정확히 예측하도록 했다.[^p8] | 1저자 Youngil Ko, 교신 전은지 |

## 교수와 전문 분야

전은지 교수는 연세대 천문우주학 학사(2004)·석사(2006)와 미국 미시간대 항공우주공학 박사(2012)를 받았다. 미시간대 박사후연구원(2012–2013), 삼성SDI Senior Engineer(2013–2016), 독일항공우주센터(DLR) 괴팅겐(2016–2018)과 영국 에든버러대(2019) 박사후연구원, 미국 하와이대 기계공학과 조교수(2019–2020)를 거쳐 2021년 KAIST 항공우주공학과 조교수로 부임했고, 2025년 9월부터 부교수다.[^members] 학과는 연구 분야를 희박기체역학, 극초음속 유동 해석, 플라즈마 유동 해석으로 적는다.[^lab]

랩 소식에 따르면 교수는 2026년 국가우주위원회 민간위원으로 위촉됐고, 2025년 KAIST 임팩트 연구상과 KAIST 14대 미래 유망기술 대표 연구성과(초저궤도 이종 위성군 기술)에 선정됐다. 2025년 미국 샌디아 국립연구소 DSMC 워크숍 단기 강좌 강연을 맡았다.[^news]

논문으로 보면 전문 분야는 세 갈래다.

- **입자 기반 희박 기체 계산법**: FP·BGK·DSMC.[^p1][^p2][^p3]
- **전기 추진 계산**: 대기 흡입 장치, 플라즈마 플룸.[^p4][^p5][^p6]
- **기체–표면 상호작용**: 표면 산란, 표면 화학 가열.[^p7][^p8]

## 응용 분야

대표 논문과 연구 페이지로 보면 초저궤도 위성과 위성 추진기, 대기권 재진입 비행체 열보호, 재사용 로켓, 달 착륙선 설계에 닿아 있다.[^p4][^p8][^hypersonic][^multiphase] 랩 소식은 한국연구재단 중견연구, 미국 공군과학연구소(AFOSR) 지원 과제, 독일 기센대와의 한–독 공동 연구 선정을 전한다.[^news]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다. 연구 주제는 랩 표기를 옮겼다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Woonghwi Park (박웅휘) | 박사과정 | Kinetic Model/Gas-surface Interactions | whpark@kaist.ac.kr | 1, 2, 3, 7 |
| Joonbeom Kim (김준범) | 박사과정 | Kinetic Model | kjb9910@kaist.ac.kr | 2 |
| Hyesu Jeong (정혜수) | 박사과정 | Gas-surface Interactions | hyesu.jeong@kaist.ac.kr |  |
| Inchan Kim (김인찬) | 석사과정 | Kinetic Model | inzzankim@kaist.ac.kr | 2 |
| Donghyeon Kim (김동현) | 석사과정 | Electric Propulsion | kimdonghyeon@kaist.ac.kr |  |
| Jongwoo Kim (김종우) | 석사과정 | Multiphase | kimjongwoo@kaist.ac.kr |  |
| Eunbin Moon (문은빈) | 석사과정 | VLEO | ebmoon@kaist.ac.kr |  |
| Geunyoung Lim (임근영) | 석사과정 | Gas-surface Interactions | limgeun0@kaist.ac.kr |  |

## 졸업생 진로

랩 구성원 페이지의 박사·석사 졸업생과 현재 소속, 랩 논문 목록의 학위 논문이다.[^members][^papers]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Sanghun Kim (김상훈) | Ph.D. (2025) | Kyungpook National University, Assistant Professor | A stochastic particle Fokker-Planck method for multiscale rarefied gas flows (박사 2025) |
| Geonwoong Moon (문건웅) | Ph.D. (2026) | Korea Aerospace Research Institute, Senior Researcher | A Numerical Framework for the Propellant Transport Modeling of Atmosphere-Breathing Electric Propulsion (박사 2026); PIC-DSMC Simulation of Electric Propulsion Plasma Plume and Application to Atmosphere-Breathing Mode (석사 2022) |
| Hanyoung Ryu (류한영) | M.S. (2024) | Hanwha Aerospace, Researcher | Aerothermal Analysis of Reusable Rocket Using Direct Simulation Monte Carlo (석사 2024) |
| Yeongho Shin (신영호) | M.S. (2024) | Korea Aerospace Institutes, Researcher | Particle-based two-phase flow simulation of solid rocket motor plume at high altitudes (석사 2024) |
| Insang Park (박인상) | M.S. (2025) | SPACE Solutions, Researcher | Characterization of ion oscillation and neutralization in the exhaust plume of electrospray thruster based on fragmentation (석사 2025) |
| Songhyun Huh (허송현) | M.S. (2025) | Samsung Electronics, Researcher | Particle-based Analysis of Atomic Oxygen Adsorption and Gas-Surface Interaction in Very-Low-Earth-Orbit (석사 2025) |
| Youngil Ko (고영일) | M.S. (2025) | Purdue University, Ph.D. Candidate | Extension of finite-rate surface chemistry model using direct simulation Monte Carlo: chemical energy accommodation and radiative equilibrium boundary condition (석사 2025) |
| Suyeon Ma (마수연) | M.S. (2026) |  | A Pseudo-Reaction Method for Surface Chemistry Model in DSMC under Hypersonic Re-entry Conditions (석사 2026) |
| Seokyeong Lim (임석영) | M.S. (2026) |  | Predictive Assessment of a Zero-Dimensional Radio-Frequency Neutralizer Model and Analysis of the Effects of Physics-Based Model Extensions under Varying Mass-Flow-Rate and Neutral-Density Conditions (석사 2026) |

## 최근 논문 목록 (2022–2026)

랩 국제 학술지 목록의 [6]–[30]번 논문 25편이다. 교신저자 표시(*)는 랩 표기다.[^papers]

**2026**

- Inchan Kim, Joonbeom Kim, Woonghwi Park, Eunji Jun\*. "A Particle Multi-Relaxation Bhatnagar-Gross-Krook Method for Rarefied Monatomic Gas Mixtures". *Physics of Fluids 38, no. 8 (2026): 087001*.
- Geonwoong Moon, Youngil Ko, Minwoo Yi, Eunji Jun\*. "Operational Feasibility Analysis of a Cryogenic Active Intake Device for Atmosphere-Breathing Electric Propulsion". *Aerospace Science and Technology 176 (2026): 112138*.
- Youngil Ko, Eunji Jun\*. "Radiative equilibrium boundary condition and correlation analysis on catalytic surfaces in DSMC". *International Journal of Heat and Mass Transfer 225, no.1 (2026): 127693*.

**2025**

- Joonbeom Kim, Eunji Jun\*. "A second-order particle Fokker-Planck-Master method for diatomic gas flows". *Physics of Fluids 37, no. 11 (2025): 117117*.
- Woonghwi Park, Eunji Jun\*. "Velocity-dependent surface corrugation in gas–surface scattering". *Physics of Fluids 37, no.9 (2025): 097153*.
- Insang Park, Geonwoong Moon, Yoshinori Takao, Eunji Jun\*. "Analysis of oscillatory local neutralization according to fragmentation in the ionic liquid electrospray thruster plume". *Physics of Plasmas 32, no.3 (2025): 033511*.
- Sanghun Kim, Eunji Jun\*. "A stochastic particle method based on the Fokker-Planck-Master equation for rarefied gas flows of diatomic mixtures". *Physics of Fluids 37, no. 3 (2025): 036111*.
- Sanghun Kim, Eunji Jun\*. "A particle Fokker-Planck method for rarefied gas flows of monatomic mixtures". *Physics of Fluids 37, no. 1 (2025): 016104*.
- Songhyun Huh, Geonwoong Moon, Eunji Jun\*. "Drag Analysis Incorporating Atomic Oxygen Adsorption in Very-Low-Earth-Orbit". *Aerospace Science and Technology 158 (2025): 109900*.

**2024**

- Joonbeom Kim, Sanghun Kim, Eunji Jun\*. "A spatial interpolation for a stochastic particle Fokker-Planck model using a polynomial reconstruction". *Physics of Fluids 36, no. 12 (2024): 127171 (Editor's Pick)*.
- Sanghun Kim, Eunji Jun\*. "An evaluation of the hybrid Fokker-Planck-DSMC approach for high-speed rarefied gas flows". *Computers & Fluids 285 (2024): 106456*.
- Youngil Ko, Eunji Jun\*. "Mechanism-specific chemical energy accommodation with finite-rate surface chemistry in non-equilibrium flow". *Physics of Fluids 36, no. 9 (2024):096115*.
- Sanghun Kim, Woonghwi Park, Eunji Jun\*. "A second-order particle Fokker-Planck model for rarefied gas flows". *Computer Physics Communications 304 (2024): 109323*.
- Yeongho Shin, Sanghun Kim, Eunji Jun\*. "An approach for particle-based simulation of multiscale two-phase flows in Direct Simulation Monte Carlo framework". *Physics of Fluids 36, no. 6 (2024): 063331*.
- Geonwoong Moon, Minwoo Yi, Eunji Jun\*. "Design and Operational Concept of a Cryogenic Active Intake Device for Atmosphere-Breathing Electric Propulsion". *Aerospace Science and Technology 151 (2024): 103900*.
- Sanghun Kim, Eunji Jun\*. "A Stochastic Fokker--Planck--Master Model for Diatomic Rarefied Gas Flows". *Journal of Computational Physics 506 (2024): 112940*.
- Woonghwi Park, Sanghun Kim, Marcel Pfeiffer, Eunji Jun\*. "Evaluation of Stochastic Particle Bhatnagar-Gross-Krook Methods with a Focus on Velocity Distribution Function". *Physics of Fluids 36, no. 2 (2024): 027113*.

**2023**

- Geonwoong Moon, Wonho Choe, Eunji Jun\*. "Plasma plume simulation of an atomic oxygen-fed ion thruster in very-low-earth-orbit". *Plasma Sources Science and Technology 32, no. 12 (2023): 125012*.
- Youngil Ko, Sangwon Kim, Geonwoong Moon, Minwoo Yi, Kangmin Park, Younho Kim, Eunji Jun\*. "Parametric study on the flight envelope of a radio-frequency ion thruster based atmosphere-breathing electric propulsion system". *Acta Astronautica 212 (2023): 198-212*.
- Sanghun Kim, Hossein Gorji, Eunji Jun\*. "Critical assessment of various particle Fokker–Planck models for monatomic rarefied gas flows". *Physics of Fluids 35, no. 4 (2023): 046117*.
- Geonwoong Moon, Minwoo Yi, Kangmin Park, Younho Kim, Hyosang Yoon, Eunji Jun\*. "Performance characterization and kinetic analysis of atmosphere-breathing electric propulsion intake device". *Vacuum 212 (2023): 112066*.
- Siqi Yao, Fei Fei, Peng Luan, Eunji Jun, Jun Zhang\*. "Extension of the Shakhov Bhatnagar–Gross–Krook model for nonequilibrium gas flows". *Physics of Fluids 35, no. 3 (2023): 037102*.

**2022**

- Sanghun Kim, Eunji Jun\*. "A stochastic particle Fokker–Planck method with nonlinear production terms for a variable hard-sphere gas". *Physics of Fluids 34, no. 8 (2022): 086111*.

**연도 표기 없음**

- Minwoo Yi, Geonwoong Moon, Younho Kim, Eunji Jun\*. "Mission-oriented Maneuverability Assessment Framework for a Satellite Integrated with Atmosphere-Breathing Electric Propulsion". *Acta Astronautica. (게재 승인)*.
- Hyesu Jeong, Taewoong Jeong, Eunji Jun, Sungmin Jo\*. "First-Principle-Inspired Reduced-Order Models of Chemical Kinetics in Hydrogen System". *AIAA Journal*.

## 특허

- 입자 흡입기 성능측정을 위한 방법 및 장치 (발명자 구봉주, 최현진, 전은지, 문건웅, 이민우; 출원번호 10-2025-0019007; 출원일 2025.02.13)
- 인공위성 입자흡입형 전기추력기용 능동형 극저온 입자흡입 장치 (발명자 문건웅, 전은지; 출원번호 10-2024-0111861; 출원일 2024.08.21)

## 소식과 수상

랩 하이라이트 페이지의 소식 제목이다.[^news]

- October 2026 · Geonwoong Moon receives "Best Ph.D. Dissertation Award"
- October 2026 · Joonbeom Kim receives "Best M.S. Thesis Award"
- September 2026 · Joonbeom Kim selected for the Research Subsidies for Ph.D. Candidates
- July 2026 · Eunji Jun joins the National Space Committee of the Republic of Korea
- July 2026 · Eunji Jun receives "KAIST Outstanding Teaching Award"
- Jun 2026 · JLU Researchers Visit KNGPDL for the GEnKo Project
- Jun 2026 · KAIST-Cranfield-PNU Joint Electric Propulsion Workshop
- February 2026 · Eunji Jun receives "Best Lecture Award"
- February 2026 · KAIST–Giessen GEnKo Joint Research Project Selected
- December 2025 · Eunji Jun receives "KAIST Impact Research Award"
- November 2025 · Geonwoong Moon receives "Best Presentation Paper Award" in KSPE
- December 2025 · Insang Park receives "Best Master's Thesis Award" in KSPE
- September 2025 · Invited Lecturer at the DSMC Workshop Short Course, Sandia National Laboratories
- September 2025 · Inchan Kim Selected for the Master’s Research Grant Program
- August 2025 · Eunji Jun receives "KAIST Outstanding Teaching Award"
- August 2025 · Dr. Sanghun Kim Appointed as Assistant Professor at Kyungpook National University
- June 2025 · Woonghwi Park Selected for the Presidential Science Scholarship
- April 2025 · Eunji Jun receives "2025 KAIST Representative Research Achievement in the 14 Future Leading Technologies"
- April 2025 · Songhyun Huh receives "Best Paper Presentation Award" in KSAS
- March 2025 · Selection for the Mid-Career Researcher Program
- February 2025 · Dr. Sanghun Kim receives "Best Ph.D. Dissertation Award" in CoE
- December 2024 · Eunji Jun receives "KAIST Q-Day Special Commendation Award"
- December 2024 · Joonbeom Kim's paper was selected as "Editor's Pick"
- November 2024 · Yeongho Shin receives "Best Master's Thesis Award" in KSPE
- November 2024 · KNGPDL 1 Lab, 1 Volunteering (L.O.V.E) Program
- November 2024 · Geonwoong Moon receives "KAIST Best Paper Award"
- October 2024 · Woongwhi Park receives "Best M.S. Dissertation Award"
- September 2024 · Suyeon Ma receives "Encouragement Award" in URP
- September 2024 · Air Force Office of Scientific Research (AFOSR) Sponsorship
- January 2024 · KAIST AE News
- November 2023 · Geonwoong Moon receives "Best M.S. Dissertation Award"
- November 2023 · KNGPDL 1 Lab, 1 Volunteering (L.O.V.E) Program
- October 2023 · College of Engineering News
- September 2023 · KAIST Breakthroughs
- February 2023 · Youngil Ko and Sangwon Kim receives "Excellent Award" in URP
- August 2021 · Prof. Eunji Jun receives "Best Lecture Award"

## 연락과 위치

- 교수 이메일: eunji.jun@kaist.ac.kr[^home][^lab]
- 교수 전화: 042-350-3736[^lab]
- 교수실: KAIST N7-2동 4303호 (대전 유성구 대학로 291)[^lab][^contact]

[^home]: KNGPDL 누리집 첫 화면 <https://kngpdl.kaist.ac.kr/> (2026-10-19 열람)
[^lab]: KAIST 항공우주공학과 연구실 소개(KNGPDL) <https://ae.kaist.ac.kr/boards/view/board_lab/78> (2026-10-19 열람)
[^kinetic]: KNGPDL 연구 페이지(Kinetic Model) <https://kngpdl.kaist.ac.kr/research/kinetic-model> (2026-10-19 열람)
[^ep]: KNGPDL 연구 페이지(Electric Propulsion) <https://kngpdl.kaist.ac.kr/research/electric-propulsion> (2026-10-19 열람)
[^gsi]: KNGPDL 연구 페이지(Gas-Surface Interactions) <https://kngpdl.kaist.ac.kr/research/gas-surface-interactions> (2026-10-19 열람)
[^hypersonic]: KNGPDL 연구 페이지(Multiscale Hypersonic Flow) <https://kngpdl.kaist.ac.kr/research/multiscale-hypersonic-flow> (2026-10-19 열람)
[^multiphase]: KNGPDL 연구 페이지(Rarefied Multiphase Flow) <https://kngpdl.kaist.ac.kr/research/rarefied-multiphase-flow> (2026-10-19 열람)
[^members]: KNGPDL 구성원 페이지 <https://kngpdl.kaist.ac.kr/members> (2026-10-19 열람)
[^papers]: KNGPDL 논문 목록 <https://kngpdl.kaist.ac.kr/publications> (2026-10-19 열람)
[^news]: KNGPDL 하이라이트 <https://kngpdl.kaist.ac.kr/highlights-newsletter/lab-highlights> (2026-10-19 열람)
[^contact]: KNGPDL 연락처 페이지 <https://kngpdl.kaist.ac.kr/contact> (2026-10-19 열람)
[^p1]: S. Kim, W. Park, E. Jun, Computer Physics Communications 304, 109323 (2024). <https://doi.org/10.1016/j.cpc.2024.109323> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p2]: I. Kim, J. Kim, W. Park, E. Jun, Physics of Fluids 38, 087001 (온라인 2026-08-17). <https://doi.org/10.1063/5.0340698> 초록 기준.
[^p3]: W. Park, S. Kim, M. Pfeiffer, E. Jun, Physics of Fluids 36, 027113 (온라인 2024-02-06). <https://doi.org/10.1063/5.0189872> 초록 기준.
[^p4]: G. Moon, M. Yi, E. Jun, Aerospace Science and Technology 151, 103900 (2024). <https://www.sciencedirect.com/science/article/pii/S1270963824004310> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p5]: G. Moon, W. Choe, E. Jun, Plasma Sources Science and Technology 32, 125012 (온라인 2023-12-27). <https://doi.org/10.1088/1361-6595/ad15b0> 초록 기준.
[^p6]: I. Park, G. Moon, Y. Takao, E. Jun, Physics of Plasmas 32, 033511 (온라인 2025-03-21). <https://doi.org/10.1063/5.0249312> 초록 기준.
[^p7]: W. Park, E. Jun, Physics of Fluids 37, 097153 (온라인 2025-09-16). <https://doi.org/10.1063/5.0276122> 초록 기준.
[^p8]: Y. Ko, E. Jun, Physics of Fluids 36, 096115 (온라인 2024-09-10). <https://doi.org/10.1063/5.0222518> 초록 기준.

# 지능형 파동 시스템 연구실 (Intelligent Wave Systems Laboratory, IWSL)

**서울대학교 공과대학 전기·정보공학부 · 유선규 부교수**

- 대분야: 물리·양자, 전기전자·반도체·광학
- 태그: 광 컴퓨팅[^p2][^p5], 비에르미트 광학[^p7], 비선형 광학[^p3], 설계 최적화(위상·형상 최적화)[^design], 양자 광학·광양자 기술[^deptlab]
- 홈페이지: <https://waves.snu.ac.kr/>

> 빛이 흐르고 서로 영향을 주는 방식을 설계해 빛으로 계산하고 정보를 기억하는 장치를 연구하며, 물질의 복잡한 구조와 주변 환경을 새로운 광학 기능으로 연결하는 연구실이다.

## 무엇을 연구하나

지능형 파동 시스템 연구실은 2020년 9월 개설되었다. 중장기 목표는 광자 인공지능(빛을 이용해 인공지능의 계산을 수행하는 기술)이며, 현재 누리집은 이를 “Thinking with Light”로 소개한다. 출발점은 파동(공간과 시간에 따라 진동이나 변화가 퍼지는 현상)의 공통 원리를 찾는 일이다. 빛·소리·탄성파(물질이 변형된 뒤 원래 상태로 돌아가려는 힘을 통해 전달되는 파동)와 양자역학(상태의 중첩과 측정 결과의 확률적 성질을 다루는 물리 이론)에서 나타나는 수학적·물리적 유사성을 이용해 분석 방법과 소자(특정 기능을 수행하는 장치의 구성 요소)를 연구한다. 중첩은 가능한 상태들을 조합한 상태를 뜻한다.[^home][^deptlab]

한 축은 빛이 지나는 매질(파동이 퍼지는 물질이나 공간)의 구조를 설계하는 일이다. 규칙적인 배열만 다루지 않고 구성 요소의 위치나 성질이 불규칙한 무질서 구조도 다룬다. 이런 구조에서 산란(파동이 물체나 매질의 불균일성과 상호작용해 진행 방향 등이 바뀌는 현상)이 어떻게 일어나는지 연구하고, 원하는 빛의 흐름을 내는 구조를 찾는다. 학과 소개는 네트워크(대상과 그 사이의 연결 관계를 함께 나타낸 체계)를 이용한 광학 매질 설계와 서로 다른 파동 분야의 연결을 연구 방향으로 든다.[^deptlab][^home]

다른 축은 주변과 물질이나 에너지 등을 주고받는 열린계다. 연구실은 빛의 증폭(세기나 크기를 키우는 작용)과 손실이 있는 계를 활용한 비에르미트 광학(증폭이나 손실을 포함하는 광학계의 상태와 변화를 연구하는 분야), 뉴로모픽 소자(신경세포나 그 연결의 동작을 본떠 정보를 처리하는 구성 요소), 열린계의 양자 광학(빛을 양자 상태로 다루고 물질과의 상호작용을 연구하는 분야)을 다룬다. 안정하게 정보를 기억하면서 외부 입력으로 상태를 바꾸는 광학 메모리(빛을 이용해 정보를 저장하는 장치)가 그 사례다.[^deptlab][^p3][^p7]

계산과 물리의 관계도 양방향으로 다룬다. 빛의 거동으로 계산하는 회로를 연구하는 한편, 신경망(서로 연결된 계산 단위들이 입력을 변환해 출력을 만드는 계산 모형)으로 광학 구조를 설계한다. 심층 신경망은 입력과 출력 사이에 여러 처리층을 둔 신경망이다. 「AI Wave Mechanics」는 심층 신경망을 내부를 살피지 않는 도구로만 쓰는 관점에서 벗어나, 그 구조가 추론(학습한 모형으로 새 입력의 결과를 계산하는 과정)에 미치는 영향을 살피는 방향을 제시한다. 대표 논문에서는 목표 광학 응답에서 구조를 찾는 역설계(원하는 성질이나 동작에서 출발해 이를 만드는 구조나 조건을 찾는 설계)를 수행했다.[^ai][^p6]

## 주요 연구 주제

### 빛 기반 계산과 정보 처리

Photonic AI 쪽은 광학 회로를 이용한 계산, 광학 네트워크, 빛을 이용한 신경세포 기능과 메모리를 연구 갈래로 제시한다. 대표 논문 2는 빛을 한 번 통과시키는 계산을 시간 순환에 따른 계산으로 바꾸는 광학 회로를 제안한다. 공진기(특정 진동이 공진을 일으키도록 만든 구조) 두 개로 시간 게이트(계산의 한 단계를 수행하는 단위)를 만들고 이를 조합했다. 공진은 계가 특정 진동수의 외부 자극에 강하게 응답하는 현상이며, 진동수는 단위 시간에 진동이 반복되는 횟수다.[^photonic][^p2]

대표 논문 3은 정보를 저장하는 부분과 처리하는 부분을 함께 두는 인메모리 연산(in-memory computing)을 위한 광학 메모리 단위를 제안한다. 비선형(입력의 변화와 출력의 변화가 비례하지 않는 성질) 광학계에서 안정한 기억 상태를 얻고, 빛으로 그 상태 사이를 양방향 전환하는 방법을 보였다. 대표 논문 5는 빛의 산란을 이용해 리만 제타 함수라는 수학 함수를 계산하는 장치를 연구했다. 산란체 수를 늘릴 때 반사가 억제되는 경향과 여러 번 산란하는 효과를 분석했다.[^p3][^p5]

### 학습을 이용한 광학 소재 설계

대표 논문 6은 외부 조절에 따라 광학 응답을 바꾸는 능동 무질서 구조를 심층 신경망으로 설계한다. 목표 응답을 만드는 구조를 찾는 계산 모형과, 구조의 응답을 얼마나 조절할 수 있는지 평가하는 계산 모형을 각각 개발했다. 상변화 물질(물질의 상태나 원자 배열이 바뀌면서 성질이 달라지는 물질)을 포함한 구조에서 특정 입사각(들어오는 파동의 진행 방향과 표면에 수직인 방향 사이의 각)을 고르는 기능과 빛의 통과를 켜고 끄는 기능을 제시했다.[^p6]

이 갈래에서 인공지능은 물리 계산을 대신하는 예측 도구뿐 아니라, 빛의 성질과 구조 사이의 관계를 분석하는 수단이다. 학과 소개는 빛과 물질의 상호작용을 위한 합성곱 신경망(주변 입력에 공통된 계산 규칙을 적용해 특징을 추출하는 신경망)과 그래프 신경망(대상 사이의 연결 관계를 따라 정보를 주고받도록 구성한 신경망)을 관심 분야로 든다.[^ai][^deptlab]

### 연결 구조와 위상 광학

위상 광학은 파동 상태의 위상수학적 성질을 이용하는 광학 연구다. 여기서 위상수학적 성질은 연속적으로 모양을 바꾸어도 유지되는 연결·구멍 등의 성질을 가리키며, 파동의 진동 진행 상태를 뜻하는 위상과 구별한다. 대표 논문 1은 연산 순서를 바꾸면 결과도 달라지는 비아벨(non-Abelian) 현상을 재설정 가능한 광학 격자(구성 요소와 그 연결을 반복적으로 배치한 구조)에서 연구했다. 두 상태를 섞는 기본 단위를 조립해 위상 현상을 재현하고, 두 영역 각각에는 없던 비아벨 특성이 그 경계에 나타날 수 있음을 보였다.[^p1]

대표 논문 4는 합성 주파수 차원(서로 다른 주파수 상태 사이의 연결을 공간의 차원에 대응시킨 표현)을 이용한 광학계를 제안한다. 주파수는 파동의 진동수가 주기적인 신호에 쓰일 때의 이름이다. 파동의 서로 다른 상태를 독립적으로 조절해 주파수를 변환하면서 파면(같은 진동 상태에 있는 지점들이 이루는 면)을 바꾸는 방법을 보였다. 누리집은 이 연구들을 광학 네트워크와 위상적 성질을 이용한 파동 제어의 사례로 제시한다.[^p4][^photonic]

### 열린계 파동과 양자 현상

대표 논문 7은 하이퍼유니폼 구조(hyperuniformity, 큰 길이 척도에서 밀도 변동의 성분이 사라지는 성질을 갖는 구조)의 개념을 증폭과 손실이 있는 물질로 확장한다. 약한 산란 조건에서 물질의 구조 통계와 산란 사이의 대응을 정리하고, 한쪽 방향의 산란을 억제하는 상태를 분석했다. 빛의 에너지가 보존되는 물질의 기존 개념을 주변과 에너지를 주고받는 소재로 넓히는 연구다.[^p7]

대표 논문 8은 양자계와 환경의 상호작용이 따르는 확률 분포(어떤 값이 나올 수 있는지와 각 값이나 구간이 차지하는 비중을 나타낸 것)를 연구한 사전 공개본이다. 큰 값의 발생 비중이 멀리까지 남는 두꺼운 꼬리 분포(heavy-tailed distribution)를 적용해, 양자 결맞음(서로 다른 양자 상태 사이의 상대위상이 유지되는 성질)이 오래 지속되면서 환경 변화에도 민감할 수 있는 조건을 분석했다. 상대위상은 두 진동이나 상태 사이의 위상 차이다. 이 연구는 양자 센싱(양자 성질을 이용해 물리량이나 환경 변화를 감지하는 기술)을 가능한 응용으로 제시한다.[^p8]

## 대표 논문

2021–2026년 서울대 재직 시기 연구에서 네 연구 갈래를 설명하는 8편을 골랐다. 1–7은 학술지 논문이며 8은 arXiv 사전 공개본이다. 유선규는 이 8편의 교신저자로 표시되어 있다. “쉽게 말하면” 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2026 | [Programmable Lattices for Non-Abelian Topological Photonics and Braiding](https://doi.org/10.1103/rgfy-n6zd) · Physical Review Letters[^p1] | 상태를 섞는 광학 기본 단위를 조립해 연산 순서에 따라 결과가 달라지는 위상 현상을 재현하고, 경계에서 나타나는 상태를 설계했다. |
| 2 | 2024 | [Programmable Photonic Time Circuits for Highly Scalable Universal Unitaries](https://doi.org/10.1103/PhysRevLett.132.103801) · Physical Review Letters[^p2] | 시간 순환을 이용해 같은 광학 계산 단위를 되풀이해 사용하는 회로를 제안하고, 계산 규모를 늘릴 때 필요한 공간과 게이트 수를 줄이는 원리를 보였다. |
| 3 | 2022 | [Topologically Protected All-Optical Memory](https://doi.org/10.1002/aelm.202200579) · Advanced Electronic Materials[^p3] | 안정한 광학 기억 상태를 만들고 빛으로 그 상태 사이를 양방향 전환하는 기본 단위를 제안했다. |
| 4 | 2024 | [Photonic Topological Spin Pump in Synthetic Frequency Dimensions](https://doi.org/10.1103/PhysRevLett.132.033803) · Physical Review Letters[^p4] | 주파수 상태 사이의 연결을 활용한 광학계로 상태의 이동을 조절해, 변환할 주파수 사이에 원하지 않는 신호가 섞이지 않는 주파수 변환과 파면 조형을 보였다. |
| 5 | 2024 | [Computing Riemann zeros with light scattering](https://doi.org/10.1103/PhysRevB.110.L220201) · Physical Review B[^p5] | 빛의 산란으로 리만 제타 함수를 계산하는 구조를 만들고, 산란체 수와 다중 산란이 반사 억제에 미치는 영향을 살폈다. |
| 6 | 2022 | [Machine-Engineered Active Disorder for Digital Photonics](https://doi.org/10.1002/adom.202102642) · Advanced Optical Materials[^p6] | 신경망으로 외부 조절에 반응하는 무질서 물질을 설계하고, 원하는 빛의 응답을 내는 구조와 그 조절 가능성을 함께 분석했다. |
| 7 | 2026 | [Non-Hermitian Stealthy Hyperuniformity](https://doi.org/10.1002/advs.77054) · Advanced Science[^p7] | 증폭과 손실이 있는 무질서 물질의 구조 통계를 산란과 연결하고, 한 방향으로만 나타나는 산란 특성을 분석했다. |
| 8 | 2025 | [Heavy-tailed open quantum systems reveal long-lived and ultrasensitive coherence](https://doi.org/10.48550/arXiv.2506.22717) · arXiv 사전 공개본[^p8] | 환경과의 상호작용에 두꺼운 꼬리 분포를 적용해, 오래 지속되면서 변화에도 민감한 양자 결맞음이 나타날 수 있음을 보였다. |

## 교수와 전문 분야

유선규(Sunkyu Yu)는 서울대학교 전기·정보공학부 부교수다. 서울대에서 2007년 학사, 2015년 박사 학위를 받았고, 박사 논문은 복잡하고 무질서하며 비선형인 광학 퍼텐셜에서 대칭성이 깨지는 현상을 이용해 빛의 흐름을 조절하는 연구였다. 퍼텐셜은 위치나 상태에 따라 상호작용 또는 에너지 조건이 어떻게 달라지는지 나타내는 양이다. 박사 지도교수는 박남규다.[^prof][^deptprof]

누리집은 2015년 8월–2016년 5월 서울대 BK21 사업 박사후연구원, 2016년 6월–2020년 8월 대통령 Postdoc Fellowship 사업 박사후연구원, 2020년 9월–2024년 8월 서울대 조교수, 2024년 9월 이후 부교수로 경력을 적는다. 학과 교수 소개는 첫 박사후연구원 경력의 시작을 2015년 9월로 적는다.[^prof][^deptprof]

학과가 적은 전문 분야는 무질서 광학, 광자 컴퓨팅·인공지능, 위상 광학, 양자 광학이다. 최근 대표 논문으로 보면 광학 계산 단위와 기억 장치의 설계, 신경망을 이용한 광학 구조 설계, 연결 구조가 만드는 위상 현상, 증폭·손실과 환경 상호작용을 이용한 파동 제어가 전문 분야를 이룬다.[^deptprof][^p1][^p2][^p3][^p6][^p7][^p8]

## 응용 분야

연구실의 중심 응용은 빛을 이용한 인공지능 계산과 정보 처리다. 광학 시간 회로를 이용한 계산 규모 확장, 빛으로 쓰고 바꾸는 메모리, 빛의 주파수 변환과 파면 조형이 대표 논문에 나타난다. 열린 양자계 연구는 양자 센싱을 가능한 응용으로 제시한다.[^home][^p2][^p3][^p4][^p8]

공동 연구에는 자기공명영상(Magnetic Resonance Imaging, MRI, 자기장과 전자기파를 이용해 물체 내부의 구조를 영상으로 얻는 기술)의 장 분포를 고르게 하는 방법도 있다. 해당 논문의 arXiv 초록은 산란 이론에서 출발한 메타표면(구조 배열로 파동의 반응을 조절하도록 설계한 표면)의 설계 방법을 개발하고, 수치 계산으로 자기장 분포의 균일화와 국소적인 가열 억제를 보였다고 적는다. 질병 진단 결과가 아니라 전자기장 제어 방법의 개발 연구다.[^mri]

## 구성원

2026년 10월 27일 누리집 Group Members 기준 17명이다. 석박사통합과정 9명, Postdoctoral Researchers 구획 1명, 학부 인턴 7명이며 연구 주제와 시작 시기는 각 카드의 표기다. 박승균 카드는 같은 구획에서 KAIST InnoCORE PICORE Center 박사후연구원(2026년 5월 이후) 소속도 함께 적는다. “대표 논문 참여”는 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Hyungchul Park (박형철) | 석박사통합과정 | 2021.03- | Photonic Diffractive Learning; Optical Experiments (Visible); Quantum Experiments | pox1255@snu.ac.kr | 4 |
| Ikbeom Lee (이익범) | 석박사통합과정 | 2021.03- | Disordered Photonics; Non-Hermitian Photonics | ikbeom.lee@snu.ac.kr | 7 |
| Kyuho Kim (김규호) | 석박사통합과정 | 2021.09- | Optical Experiments (IR); Nanofabrication; Open Quantum Systems | kyuho.kim@snu.ac.kr |  |
| Dayeong Lee (이다영) | 석박사통합과정 | 2022.03- | Time-Varying Photonics; Lithography - Overlay | dayeong315@snu.ac.kr |  |
| Gitae Lee (이기태) | 석박사통합과정 | 2023.03- | Disordered Photonics; THz Experiments; Nanofabrication; Lithography - Overlay | ltk175@snu.ac.kr | 7 |
| Kunwoo Park (박건우) | 석박사통합과정 | 2024.09- | Disordered Photonics; Topological Photonics; Integrated Photonics | imotdnif43@snu.ac.kr | 7 |
| Jongheon Yeo (여종헌) | 석박사통합과정 | 2025.09- | THz Experiments; Time-Varying Photonics; Nanofabrication | zkdnqh12@snu.ac.kr |  |
| Duhwan Hwang (황두환) | 석박사통합과정 | 2025.09- | Quantum Photonics; Optical Experiments (IR); Nanofabrication | naemduu@snu.ac.kr | 7 |
| Beomjoon Chae (채범준) | 석박사통합과정 | 2026.03- | Integrated Photonics; Topological Photonics; Quantum Photonics | cbj000921@snu.ac.kr |  |
| Seungkyun Park (박승균) | 박사후연구원 (Postdoc in KAIST InnoCORE PICORE Center, 2026.05–) |  | Integrated Photonics; Open Quantum Systems; Neural Operator / LLM; Lithography - Overlay | sgpark0213@snu.ac.kr | 6, 7 |
| Jae-Hyun Lee (이재현) | 학부 인턴 | 2025.07- | Quantum Photonics | jaehyuny06@snu.ac.kr |  |
| Minjun Ko (고민준) | 학부 인턴 | 2025.07- | Topological Photonics | go22867361@snu.ac.kr |  |
| Jusung Kim (김주성) | 학부 인턴 | 2025.09- | Open Quantum Systems; LLM; Optical Experiments (Visible) | kjs7788@snu.ac.kr |  |
| Seonbin Sohn (손선빈) | 학부 인턴 | 2026.07- | Open Quantum Systems; THz Experiments | sonbnii@snu.ac.kr |  |
| Jinwon Park (박진원) | 학부 인턴 | 2026.07- | Quantum photonics; Circuit Experiments | boky618@snu.ac.kr |  |
| Jaehyeok Kim (김재혁) | 학부 인턴 | 2026.08- | Integrated photonics; Density functional theory | kimjaehyeok1019@snu.ac.kr |  |
| Youngjin Choi (최영진) | 학부 인턴 | 2026.09- | Metasurfaces; Optical Experiments | caniche25@snu.ac.kr |  |

## 졸업생과 이전 구성원

2026년 10월 27일 누리집 Alumni의 18명이다. 박사후연구원 1명, 방문 연구원 2명, 학부 인턴 15명이며, Graduate Students 제목 아래에는 별도의 이름이 적혀 있지 않다. 학위 취득을 추정하지 않고 연구실에서 맡았던 과정·역할과 기간을 적었다. 이 목록은 유선규 교수의 2020년 9월 교원 부임 전 활동 기간도 포함한다. 진로는 카드의 Affiliation 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jusung Park (박주성) | Postdoctoral Research / Visiting Researcher (2025.03-2025.09 / 2023.06-2025.02) | Samsung Medison |
| Jungmin Kim (김정민) | Visiting Researcher (2020.07-2023.02) | Photonics Engineer, Flexcompute |
| Jehyeon Shin (신제현) | Visiting Researcher (2024.09-2025.02) |  |
| Kyungmin Lee (이경민) | Research Intern (2020.07-2020.12) |  |
| Jaeha Park (박재하) | Research Intern (2021.08-2021.09) |  |
| Yoseop Jeong (정요섭) | Research Intern (2021.07-2021.11) |  |
| Jungmo Lee (이정모) | Research Intern (2021.07-2021.12) |  |
| Jongheon Yeo (여종헌) | Research Intern (2021.07-2022.06) |  |
| Gyujin Choi (최규진) | Research Intern (2022.02-2022.06) |  |
| Seou Choi (최서우) | Research Intern (2020.09-2022.07) | Ph.D. student at MIT (Prof. Marin Soljačić's group) |
| Joseph Suh (김지성) | Research Intern (2022.07-2023.07) | Ph.D. student at University of California, Berkeley (BAIR in UC Berkeley) |
| Gyunghun Kim (김경훈) | Research Intern (2022.07-2024.08) | Ph.D. student at MIT (Prof. William D. Oliver's group) |
| Minjae Shin (신민재) | Research Intern (2024.03-2024.10) |  |
| Subin Kim (김수빈) | Research Intern (2025.01-2025.01) |  |
| Seungbeom Lee (이승범) | Research Intern (2024.12-2025.06) |  |
| Chaehyeon Lim (임채현) | Research Intern (2025.03-2026.01) |  |
| Seungmok Youn (윤승목) | Research Intern (2024.03-2026.04) |  |
| Jungyoon Kim (김정윤) | Research Intern (2025.07-2026.05) |  |

## 최근 논문·발표 목록 (2021–2026)

누리집의 2021–2026년 표기에서 고른 93건이다. 학술지 논문 32편, 학술 논평 1편, arXiv 사전 공개본 7편, 국제 학회 발표 20건, 국내 학회 발표 33건이다. 연도만 게시된 학술지 논문의 2021년 항목은 연도 단위로 포함하며, 날짜가 게시된 학회 발표는 2021년 10월 22일–2026년 10월 22일을 기준으로 한다. 사전 공개본은 출판 논문과 구분해 arXiv로 적었다. 학회 목록은 누리집의 발표 기록을 옮긴 것이며 논문집 출판을 뜻하지 않는다. 논문 목록 원문에는 교수의 교원 부임 전 연구도 섞여 있으나, 여기 수록한 항목은 2021–2026년이다.[^journals][^conferences]

**2026**

- Sunkyu Yu, Xianji Piao & Namkyoo Park. "Topological insulators on complex networks". *arXiv preprint arXiv:2610.02888*.
- Kyuho Kim, Dayeong Lee, Seungkyun Park, Xianji Piao, Namkyoo Park, Sunkyu Yu. "Mapping open quantum dynamics onto graphs". *arXiv preprint arXiv:2607.04721*.
- Sunkyu Yu, Xianji Piao, Namkyoo Park. "Multi-objective design of photon blockade for bright single-photon sources". *arXiv preprint arXiv:2606.20160*.
- Jungyoon Kim, Kyuho Kim, Kunwoo Park, Namkyoo Park, Sunkyu Yu. "Task-specific programming of chaos in neural circuits". *arXiv preprint arXiv:2605.19465*.
- Chaehyeon Lim, Hyungchul Park, Beomjoon Chae, Jeonghun Kwak, Soo-Yeon Lee, Namkyoo Park, Sunkyu Yu. "Scalable memory sharing in photonic quantum memristors for reservoir computing". *arXiv preprint arXiv:2601.23044*.
- Sunkyu Yu & Namkyoo Park. "Topological highways for light". *Nature Reviews Electrical Engineering (2026)*.
- Sunkyu Yu, Xianji Piao, Namkyoo Park. "Magnetic graphs for cavity quantum electrodynamics". *Science Advances 12, eaee5566 (2026)*.
- Minsik Kong, Seong Eun Kim, Kyuho Kim, Sunkyu Yu, Namkyoo Park, Soo-Yeon Lee. "Monolithically Integrated IGZO Synaptic Transistors on a Silicon Nitride Waveguide for Optoelectronic Neuromorphic Computing". *ACS Photonics 13, 5358 (2026)*.
- Gitae Lee, Seungmok Youn, Ikbeom Lee, Kunwoo Park, Duhwan Hwang, Seungkyun Park, Xianji Piao, Namkyoo Park, Sunkyu Yu. "Non-Hermitian stealthy hyperuniformity". *Advanced Science 13, e77054 (2026)*.
- Sunkyu Yu, Xianji Piao & Namkyoo Park. "Topological heavy-tailed networks". *Newton 2, 100598 (2026)*.
- Seungkyun Park, Beomjoon Chae, Hyungchul Park, Sunkyu Yu, Xianji Piao, Namkyoo Park. "Fully Programmable Slow Light Based on a Spinor Representation of Generalized Coupled-Resonator-Induced Transparency". *Advanced Science 13, e76378 (2026)*.
- Minsik Kong, Min Kang, Chanwoo Jeong, Kyuho Kim, Sunkyu Yu, Soo-Yeon Lee. "Crystallographic Analysis of a Nonvolatile HZO Phase Shifter Integrated on a Si3N4 Waveguide". *Advanced Electronic Materials 12, e00765 (2026)*.
- Seungmok Youn, Kunwoo Park, Ikbeom Lee, Gitae Lee, Namkyoo Park, Sunkyu Yu. "Phase-Sensitive Engineering of Optical Disordered Materials Using Heterogeneous Networks". *Advanced Optical Materials 14, e03499 (2026)*.
- Gyoungsub Yoon, Sunkyu Yu, Jongho Lee & Namkyoo Park. "Volumetric B1+ field homogenization in 7 T brain MRI using metasurface scattering". *ACS Photonics 13, 1693 (2026)*.
- Gyunghun Kim, Jensen Li, Xianji Piao, Namkyoo Park, Sunkyu Yu. "Programmable lattices for non-Abelian topological photonics and braiding". *Physical Review Letters 136, 043804 (2026)*.
- Kyungmin Lee, Sunkyu Yu, Jiyong Kang, Seungwoo Yu, Wonhyeong Choi, Daun Chung, Sumin Park, and Taehyun Kim. "Phase-space topology in a single-atom synthetic dimension". *Physical Review A 113, L010401 (2026)*.
- Duhwan Hwang, Beomjoon Chae, Namkyoo Park & Sunkyu Yu. "Curvature-programmed Landau–Zener splitting in a double-spiral photonic coupler". *The 2nd Optical Science & Opto-Semiconductor Workshop 2026, PS-17, Suwon, 17th September 2026*.
- Hyungchul Park, Beomjoon Chae, Hyunsoo Jang, Xianji Piao & Sunkyu Yu. "Dynamic Q-switching for pulse loading and high-Q operation in programmable photonic time circuits". *The 2nd Optical Science & Opto-Semiconductor Workshop 2026, PS-14, Suwon, 17th September 2026*.
- Dayeong Lee, Jongheon Yeo, Gitae Lee, Beomjoon Chae, Namkyoo Park & Sunkyu Yu. "Temporal-Defect Engineering for Programmable Coherent Energy Control in Active Photonic integrated devices". *The 2nd Optical Science & Opto-Semiconductor Workshop 2026, PS-12, Suwon, 17th September 2026*.
- Kyuho Kim, Jongheon Yeo, Gitae Lee, Duhwan Hwang, Namkyoo Park & Sunkyu Yu. "Lithographically defined deep-etched facets for edge couplers". *The 2nd Optical Science & Opto-Semiconductor Workshop 2026, PS-07, Suwon, 17th September 2026*.
- Kyuho Kim, Dayeong Lee, Seungkyun Park, Xianji Piao, Namkyoo Park & Sunkyu Yu. "Spectral analysis of open quantum dynamics via graph". *Optics and Photonics Congress 2026, M1D-IV.03, Jeju, 20th July 2026*.
- Gitae Lee, Jongheon Yeo, Seungkyun Park, Namkyoo Park & Sunkyu Yu. "Terahertz Amplitude Modulation of Optically Pumped Silicon". *Optics and Photonics Congress 2026, M1C-V.04, Jeju, 20th July 2026*.
- Hyungchul Park, Beomjoon Chae, Hyunsoo Jang, Sunkyu Yu & Xianji Piao. "Synchronizing SU(2) Time Gates in Coupled Resonator Lattices". *Optics and Photonics Congress 2026, M3C-V.05, Jeju, 20th July 2026*.
- Jongheon Yeo, Beomjoon Chae, Duhwan Hwang, Kyuho Kim, Gitae Lee, Namkyoo Park & Sunkyu Yu. "Stress Evolution in Two-Step LPCVD Si3N4 Deposition with Different Intermediate Treatments". *Optics and Photonics Congress 2026, M4C-V.04, Jeju, 20th July 2026*.
- Beomjoon Chae, Hyungchul Park, Seungkyun Park, Namkyoo Park, Xianji Piao & Sunkyu Yu. "Reconfigurable Add-Drop Filtering via Phase Shift Control in Parallel-Coupled Waveguide Loops". *Optics and Photonics Congress 2026, T2C-V.03, Jeju, 21st July 2026*.
- Ikbeom Lee, Gitae Lee, Seungmok Youn, Kunwoo Park, Duhwan Hwang, Xianji Piao, Namkyoo Park & Sunkyu Yu. "Designing asymmetric scattering using gain and loss media". *Optics and Photonics Congress 2026, TP-V.23, Jeju, 21st July 2026*.
- Kunwoo Park, Gitae Lee, Ikbeom Lee, Seungmok Youn, Namkyoo Park & Sunkyu Yu. "Large-Scale Optical Material Design via Hypergraph Models". *Optics and Photonics Congress 2026, W3C-V.01, Jeju, 22nd July 2026*.
- Jongheon Yeo, Duhwan Hwang, Kyuho Kim, Namkyoo Park & Sunkyu Yu. "Hybrid Dissipation Shifts the Threshold of the Superradiant Phase Transition in the Dicke Model". *OSK Winter Meeting 2026, T1A-VIII.02, Busan, 5th February 2026*.
- Dayeong Lee, Jongheon Yeo, Beomjoon Chae, Jungmin Kim, Namkyoo Park & Sunkyu Yu. "Inverse-design of single temporal defect in a photonic time crystal". *OSK Winter Meeting 2026, W2G-V.04, Busan, 4th February 2026*.
- Jusung Kim, Dayeong Lee, Seungkyun Park, Namkyoo Park & Sunkyu Yu. "Reconfigurable Optical Permutation using Periodic Diffractive Deep Neural Networks". *OSK Winter Meeting 2026, W1G-V.04, Busan, 4th February 2026*.

**2025**

- Kunwoo Park, Ikbeom Lee, Seungmok Youn, Gitae Lee, Namkyoo Park, Sunkyu Yu. "Hypergraph modelling of wave scattering to speed-up material design". *arXiv preprint arXiv:2507.15329*.
- Sunkyu Yu, Xianji Piao, Namkyoo Park. "Heavy-tailed open quantum systems reveal long-lived and ultrasensitive coherence". *arXiv preprint arXiv:2506.22717*.
- Hyungchul Park, Beomjoon Chae, Hyunsoo Jang, Sunkyu Yu & Xianji Piao. "Scalable unitary computing using time-parallelized photonic lattices". *Nanophotonics 14, 5527 (2025)*.
- Sunkyu Yu, Xianji Piao & Namkyoo Park. "Nonlinear unitary circuits for photonic neural networks". *ACS Photonics 12, 6737 (2025)*.
- Kyuho Kim, Kunwoo Park, Hyungchul Park, Sunkyu Yu, Namkyoo Park & Xianji Piao. "Programmable photonic unitary circuits for light computing". *Nanophotonics 14, 1429 (2025)*.
- Jusung Park, Seungkyun Park, Kyuho Kim, Jeonghun Kwak, Sunkyu Yu & Namkyoo Park. "Deep-subwavelength engineering of stealthy hyperuniformity". *Nanophotonics 14, 1113 (2025)*.
- Sunkyu Yu. "Exploiting Disorder in Classical and Quantum Photonic Signal Processing". *PIERS Chiba 2025, Session 3P16, Makuhari Messe, Chiba, Japan, 8 th November 202 5*.
- Ikbeom Lee, Kunwoo Park, Seungmok Youn & Sunkyu Yu. "Inverse design of microstructures of non-Hermitian scattering systems". *SPIE Optics + Photonics 2025, 13578-59, San Diego, California, USA, 6th August 2025*.
- Hyungchul Park, Kyuho Kim, Beomjoon Chae, Xianji Piao & Sunkyu Yu. "Computing non-Euclidean wave dynamics with programmable photonic resonant circuits". *SPIE Optics + Photonics 2025, 13581-39, San Diego, California, US A, 6th August 2025*.
- Kunwoo Park, Ikbeom Lee, Seungmok Youn & Sunkyu Yu. "Modularization of light scattering for photonic computing applications". *SPIE Optics + Photonics 2025, 13581-25, San Diego, California, USA, 5th August 2025*.
- Duhwan Hwang, Jongheon Yeo, Kunwoo Park, Namkyoo Park & Sunkyu Yu. "Numerical Analysis of Single-Photon Dynamics in Nonreciprocal  Waveguide-Resonator Coupled Systems". *Photonics Conference 2025, T2A-II.05, Pyeongchang, 27th November 2025*.
- Jongheon Yeo, Duhwan Hwang, Seungkyun Park, Namkyoo Park & Sunkyu Yu. "Fidelity Benchmarking of Algorithms for Integrated Photonic Unitary Circuits". *Photonics Conference 2025, T2A-II.04, Pyeongchang, 27th November 2025*.
- Kyuho Kim, Seungkyun Park, Jongheon Yeo, Namkyoo Park & Sunkyu Yu. "Inverse Design of a Wavelength Division Multiplexer based on the Adjoint Optimization". *Photonics Conference 2025, T1A-II.05, Pyeongchang, 27th November 2025*.
- Kyuho Kim, Seungkyun Park, Namkyoo Park & Sunkyu Yu. "Assembling Discrete Fractional Fourier Transformation with Modal Filtering using Supersymmetric Engineering". *Optics and Photonics Congress 2025, M1B-V.06, Jeju, 7th July 2025*.
- Gitae Lee, Namkyoo Park & Sunkyu Yu. "Near- and far-field inverse design via generalized Wigner-Smith operator". *Optics and Photonics Congress 2025, W3F-I.05, Jeju, 9th July 2025*.
- Dayeong Lee, Beomjoon Chae, Jungmin Kim & Sunkyu Yu. "Local Energy Transport in Photonic Time Crystals under Multi-k Excitation". *Optics and Photonics Congress 2025, W3F-I.06, Jeju, 9th July 2025*.

**2024**

- Sunkyu Yu, Xianji Piao & Namkyoo Park. "Computing Riemann zeros with light scattering". *Physical Review B 110, L220201 (2024)*.
- Taesoo Lee, Minjun Kim, Beomsoo Chun, Ganghyun Park, Soojeong Yim, Sunkyu Yu & Jeonghun Kwak. "Recent Advances in Light Outcoupling from Quantum-Dot Light-Emitting Diodes". *ACS Photonics 11, 5050 (2024)*.
- Hyungchul Park, Xianji Piao & Sunkyu Yu. "Scalable and Programmable Emulation of Photonic Hyperbolic Lattices". *ACS Photonics 11, 3890-3897 (2024)*.
- Gyunghun Kim, Joseph Suh, Dayeong Lee, Namkyoo Park & Sunkyu Yu. "Long-range-interacting topological photonic lattices breaking channel-bandwidth limit". *Light: Science & Applications 13, 189 (2024)*.
- Geun Woo Baek, Yeon Jun Kim, Jaekwon Kim, Jun Hyuk Chang, Uhjin Kim, Soobin An, Junhyeong Park, Sunkyu Yu, Wan Ki Bae, Jaehoon Lim, Soo-Yeon Lee & Jeonghun Kwak. "Memristive Switching Mechanism in Colloidal InP/ZnSe/ZnS Quantum Dot-Based Synaptic Devices for Neuromorphic Computing". *Nano Letters 24, 5855 (2024)*.
- Xianji Piao, Sunkyu Yu & Namkyoo Park. "Programmable Photonic Time Circuits for Highly Scalable Universal Unitaries". *Physical Review Letters 132, 103801 (2024)*.
- Taesoo Lee, Minhyung Lee, Kyuho Kim, Hyunkoo Lee, Suk-Young Yoon, Heesun Yang, Sunkyu Yu & Jeonghun Kwak. "Angle-Independent Top-Emitting Quantum-Dot Light-Emitting Diodes Using a Solution-Processed Subwavelength Scattering–Capping Layer". *Advanced Optical Materials 2302509 (2024)*.
- Joseph Suh, Gyunghun Kim, Hyungchul Park, Shanhui Fan, Namkyoo Park & Sunkyu Yu. "Photonic Topological Spin Pump in Synthetic Frequency Dimensions". *Physical Review Letters 132, 033803 (2024)*.
- Jusung Park, Seungkyun Park, Kyuho Kim, Sunkyu Yu & Namkyoo Park. "Improved Retrieval of Effective Parameters in Hyperbolic Metamaterials for Oblique Incidence". *CLEO-PacificRim (CLEO-PR) 2024, P3-154, Incheon, Republic of Korea, 8th August 2024*.
- Gyunghun Kim, Joseph Suh, Dayeong Lee, Namkyoo Park & Sunkyu Yu. "Lattice Design for Multiple Topologically Protected Edge Modes". *CLEO-PacificRim (CLEO-PR) 2024, We1F-3, Incheon, Republic of Korea, 7th August 2024*.
- Ikbeom Lee, Kunwoo Park & Sunkyu Yu. "Design of Wave Scattering from Gain and Loss Disordered Materials". *CLEO-PacificRim (CLEO-PR) 2024, Mo2J-4, Incheon, Republic of Korea, 5th August 2024*.
- Gitae Lee, Hyungchul Park, Seungkyun Park, Namkyoo Park & Sunkyu Yu. "Iterative Design of Hyperuniform Materials using Wannier Functions". *CLEO-PacificRim (CLEO-PR) 2024, Mo2J-3, Incheon, Republic of Korea, 5th August 2024*.
- Kunwoo Park, Ikbeom Lee & Sunkyu Yu. "Inverse Design Method of Hyperuniform Materials using System Factorization". *CLEO-PacificRim (CLEO-PR) 2024, Mo2J-2, Incheon, Republic of Korea, 5th August 2024*.
- Dayeong Lee, Gitae Lee, Seungkyun Park, Hyungchul Park, Namkyoo Park & Sunkyu Yu. "Mutative Evolution for Calculating Maximally Localized Wannier Functions in Photonic Crystals". *CLEO-PacificRim (CLEO-PR) 2024, Mo1A-3, Incheon, Republic of Korea, 5th August 2024*.
- Kyuho Kim, Jusung Park, Seungkyun Park, Namkyoo Park & Sunkyu Yu. "Extracting effective material parameters of stealthy hyperuniform metamaterials". *Optics and Photonics Congress 2024, W1D-V.03, Jeju, 10th July 2024*.
- Gitae Lee, Ikbeom Lee, Namkyoo Park & Sunkyu Yu. "Wannier-based design of photonic crystals preserving neighboring coupling". *OSK Winter Meeting 202 4 T1D-V.04, Suwon, 15th February 202 4*.

**2023**

- Sunkyu Yu & Namkyoo Park. "Heavy tails and pruning in programmable photonic circuits for universal unitaries". *Nature Communications 14, 1853 (2023)*.
- Dayeong Lee, Hyungchul Park & Sunkyu Yu. "Engineering isospectrality in multidimensional photonic systems". *Nanophotonics 12, 2593-2601 (2023)*.
- Jungmin Kim, Dayeong Lee, Sunkyu Yu & Namkyoo Park. "Unidirectional scattering with spatial homogeneity using correlated photonic time disorder". *Nature Physics 19, 726 (2023)*.
- Sunkyu Yu. "Evolving scattering networks for engineering disorder". *Nature Computational Science 3, 128-138 (2023)*.
- Sunkyu Yu & Namkyoo Park. "Pruning for U(N) Programmable Photonic Circuits". *Optics, Photonics, and Lasers (OPL-2023), Hiroshima, Japan and Online, 7th December 2023*.
- Hyungchul Park, Seungkyun Park, Gyunghun Kim, Namkyoo Park & Sunkyu Yu. "Modal Localization in Disordered Hyperbolic Lattices". *Optica Advanced Photonics Congress, NoTh3C.5, Busan, Republic of Korea, 13th July 2023*.
- Gyunghun Kim, Joseph Suh, Ikbeom Lee & Sunkyu Yu. "Berry Curvature Engineering in Optical Resonator Networks Using Long-Range Hopping". *Optica Advanced Photonics Congress, NoTh2C.4, Busan, Republic of Korea, 13th July 2023*.
- Dayeong Lee, Hyungchul Park, Seungkyun Park, Namkyoo Park & Sunkyu Yu. "Perturbative Design for Quasi-Isospectrality in Multidimensional Photonic Systems". *Optica Advanced Photonics Congress, NoTh2C.3, Busan, Republic of Korea, 13th July 2023*.
- Joseph Suh, Gyunghun Kim, Hyungchul Park & Sunkyu Yu. "Topological Photonic Molecule With Time-Varying Modulations". *Optica Advanced Photonics Congress, JTu4A.17, Busan, Republic of Korea, 11th July 2023*.
- Dayeong Lee, Jungmin Kim, Hyungchul Park, Ikbeom Lee, Sunkyu Yu & Namkyoo Park. "Design of Correlated Photonic Time Disorder for Unidirectional Scattering". *Optica Advanced Photonics Congress, NoTu3C.4, Busan, Republic of Korea, 11th July 2023*.
- Sunkyu Yu. "Photonic Systems inspired by Network Science". *Photonics Conference 2023, Tutorial I, Pyeongchang, 29th November 2023*.
- Kyuho Kim, Ikbeom Lee, Seungkyun Park, Namkyoo Park & Sunkyu Yu. "Anisotropy in stealthy hyperuniform metamaterials". *Optics and Photonics Congress 2023, T1F-II.05, Jeju, 29th August 2023*.
- Ikbeom Lee, Kyuho Kim, Gitae Lee & Sunkyu Yu. "Optical mode converters using adjoint optimization". *Optics and Photonics Congress 2023, M4C-V.05, Jeju, 28th August 2023*.
- Sunkyu Yu & Namkyoo Park. "Photonics with Engineered Disorder". *OSK Winter Meeting 2023, Distinguished Lectures on Metamaterials 2023 W2H-S, Busan, 15th February 2023*.

**2022**

- Seunghwa Oh, Jungmin Kim, Xianji Piao, Seulong Kim, Kihong Kim, Sunkyu Yu & Namkyoo Park. "Control of localization and optical properties with deep-subwavelength engineered disorder". *Optics Express 30, 28301 (2022)*.
- Seou Choi, Jungmin Kim, Jeonghun Kwak, Namkyoo Park & Sunkyu Yu. "Topologically Protected All-Optical Memory". *Advanced Electronic Materials 8, 2200579 (2022)*.
- Jungmin Kim, Seungkyun Park, Sunkyu Yu & Namkyoo Park. "Machine-Engineered Active Disorder for Digital Photonics". *Advanced Optical Materials 10, 2102642 (2022)*.
- Seungkyun Park, Ikbeom Lee, Jungmin Kim, Namkyoo Park & Sunkyu Yu. "Hearing the shape of a drum for light: isospectrality in photonics". *Nanophotonics 11, 2763 (2022)*.
- Seungkyun Park, Dayeong Lee, Namkyoo Park, Sunkyu Yu. "Supersymmetric Engineering of Short-Range Order in Optical Materials". *FiO LS 2022, FTh1C, Rochester, NY, USA, 20th October 2022*.
- Dayeong Lee, Jungmin Kim, Namkyoo Park & Sunkyu Yu. "Molecular Dynamics for Microscopic Analysis of Refractive Index in Amorphous Hafnium Oxides". *FiO LS 2022, FW7C.5, Rochester, NY, USA, 19th October 2022*.
- Jungmin Kim, Seungkyun Park, Dayeong Lee, Sunkyu Yu & Namkyoo Park. "Data-Driven Engineering of Active Photonic Disorder". *FiO LS 2022, JW4A.20, Rochester, NY, USA, 19th October 2022*.
- Sunkyu Yu. "Engineered Disorder in Time-Varying Systems". *The 6th A3 Metamaterials Forum, MA6, Seoul National University, Seoul, Korea, 27th June 2022*.
- Sunkyu Yu. "Machine Learning for Designing Complex Materials". *KPS 70th Anniversary and 2022 Fall Meeting, F12.04, Busan, 21th October 2022*.
- Dayeong Lee, Ikbeom Lee, Seungkyun. Park, Namkyoo Park & Sunkyu Yu. "Molecular Dynamics Analysis of HfO2 Phase Transition for Optoelectronic Devices". *Optics and Photonics Congress 2022, T2C-V.03\*, Jeju, 5th July 2022*.
- Hyungchul Park, Jungmin Kim, Kyuho Kim, Namkyoo Park & Sunkyu Yu. "Analysis of Anderson Localization in Disordered Hyperbolic Lattices using Modal Areas". *Optics and Photonics Congress 2022, M2H-I.05\*, Jeju, 4th July 2022*.

**2021**

- Sunkyu Yu, Xianji Piao & Namkyoo Park. "Topologically protected optical signal processing using parity–time-symmetric oscillation quenching". *Nanophotonics 10, 2883 (2021)*.
- Sunkyu Yu, Cheng-Wei Qiu, Yidong Chong, Salvatore Torquato & Namkyoo Park. "Engineered Disorder in Photonics". *Nature Reviews Materials 6, 226 (2021)*.
- Jungmin Kim, Seungkyun Park, Ikbeom Lee, Sunkyu Yu & Namkyoo Park. "Design of Multilayer-based Active Photonic Devices using Artificial Neural Networks". *Photonics Conference 2021, F2B-II.02\*, Pyeongchang, 3rd December 2021*.
- Kyuho Kim, Seungkyun Park, Jungmin Kim, Ikbeom Lee, Namkyoo Park & Sunkyu Yu. "Designing Chaotic Resonators based on the Deformation Strengths and Frequencies in view of Engineered Disorder". *Photonics Conference 2021, T1B-II.06\*, Pyeongchang, 2nd December 2021*.
- Hyungchul Park, Seungkyun Park, Ikbeom Lee, Namkyoo Park & Sunkyu Yu. "Analysis of Wave Transport and Localization in Hyperbolic Lattices". *Photonics Conference 2021, T1B-II.05\*, Pyeongchang, 2nd December 2021*.
- Seungkyun Park, Jungmin Kim, Hyungchul Park, Sunkyu Yu & Namkyoo Park. "Predicting Optical Wave Properties of Disordered Materials using Graph Neural Networks". *Photonics Conference 2021, T1B-II.04\*, Pyeongchang, 2nd December 2021*.

## 과제

누리집 교수 소개의 PI(Principal Investigator, 연구책임자) 과제 가운데 2021년 10월 22일–2026년 10월 22일 사이에 시작하거나 끝난 7건이다. 진행 중 3건과 완료 4건이며 상태와 기간은 누리집 표기다.[^prof]

- Research on Multi-Channel Photonic Integrated Circuits for Noise-Resilient and Defect-Tolerant Operations (기간 Mar.2026 - Sep.2031; 사업 Core Research Grants (Type C); 지원 Ministry of Science and ICT (NRF); 상태 진행 중; 역할 PI)
- Research on Quantum Photonic Devices based on Open-System Degrees of Freedom (기간 Sep.2025 - Aug.2028; 사업 Pilot and Feasibility Grants; 지원 Ministry of Science and ICT (NRF); 상태 진행 중; 역할 PI)
- Basic Research Laboratory for Memristic Devices based on Electron-Photon Hybrids (기간 May.2024 - Apr.2027; 사업 Basic Research Laboratory (Subsequent); 지원 Ministry of Science and ICT (NRF); 상태 진행 중; 역할 PI)
- Research on Photonic Complex and Neural Networks based on Evolution Processes (기간 Jul.2023 - Jun.2026; 사업 Creative-Pioneering Researchers Program; 지원 Seoul National University; 상태 완료; 역할 PI)
- Femtosecond Laser Equipment Setup for THz and Quantum Photonic Artificial Intelligence (기간 Jun.2024 - May.2025; 사업 Young Researcher Infrastructure Program; 지원 Ministry of Science and ICT (NRF); 상태 완료; 역할 PI)
- Engineering Disordered Materials for Photonic Technology (기간 Mar.2021 - Feb.2026; 사업 Young Researcher Program; 지원 Ministry of Science and ICT (NRF); 상태 완료; 역할 PI)
- Basic Research Laboratory for Memristic Devices based on Electron-Photon Hybrids (기간 Jun.2021 - Feb.2024; 사업 Basic Research Laboratory; 지원 Ministry of Science and ICT (NRF); 상태 완료; 역할 PI)

## 특허

누리집 특허 목록 15개 발명 묶음 가운데 출원일이나 등록일이 2021년 10월 22일–2026년 10월 22일 안에 있는 9개 묶음이다. 같은 발명의 국가별 출원은 한 묶음으로 적고, 출원·등록·가출원 번호와 날짜를 누리집 표기대로 병기했다. 원문 목록에는 유선규 교수의 교원 부임 전 발명도 포함되어 있다.[^patents]

- 양자 광학 멤트랜지스터 및 이를 이용한 메모리 공유 네트워크 구조 (발명자 Namkyoo Park, Sunkyu Yu, Hyungchul Park, Chaehyeon Lim, Beomjoon Chae; 번호 KR (Application Number: 10-2026-0091663); (Filing Date: 2026.05.20))
- 입사각 의존적 파동 국소화 제어를 위한 스텔시 하이퍼유니폼 구조 기반 광학 소자 및 그 설계 방법 (발명자 Sunkyu Yu, Namkyoo Park, Jeonghun Kwak, Jusung Park, Seungkyun Park, Kyuho Kim; 번호 KR (Application Number: 10-2025-0097538); (Filing Date: 2025.07.18))
- 비선형 유니터리 광학 소자 (발명자 Sunkyu Yu, Namkyoo Park, Xianji Piao, Kunwoo Park; 번호 KR 10-2859166 (Application Number: 10-2025-0005056 / Provisional: 10-2024-0179951); Registration Date: 2025.09.09 (Filing Date: 2025.01.13 / Provisional: 2024.12.05); US (Application Number: 19/048,370); (Filing Date: 2025.02.07); EU (Application Number: 25156862.2); (Filing Date: 2025.02.10))
- 비아벨 게이지 장을 구현하는 광자 집적회로 (발명자 Namkyoo Park, Sunkyu Yu, Xianji Piao, Gyunghun Kim; 번호 KR 10-2930295 (Application Number: 10-2024-0147067 / P rovisional: 10-2024-0119460); Registration Date: 2026.02.19 (Filing Date: 2024.10.24 / Provisional: 2024.09.03); US (Application Number: 19/038,487); (Filing Date: 2025.01.27))
- 메타 표면 설계 장치 및 방법 (발명자 Namkyoo Park, Sunkyu Yu, Gyoungsub Yoon; 번호 KR 10-2964022 (Application Number: 10-2025-0005055 / Provisional: 10-2024-0028542); Registration Date: 2026.05.07 (Filing Date: 2025.01.13 / Provisional: 2024.02.28); US (Application Number: 19/066,055); (Filing Date: 2025.02.27))
- 양자 회로 설계 장치 및 방법 (발명자 Sunkyu Yu, Namkyoo Park; 번호 KR (Application Number: 10-2023-0068467); (Filing Date: 2023.05.26); US (Application Number: 18/422,939); (Filing Date: 2024.01.25))
- 선택적 반사가 가능한 투명 반사 패널 및 이의 제조 방법 (발명자 Hyeokjung Kang, Namkyoo Park, Sunkyu Yu, Xianji Piao; 번호 KR 10-2746381 (Application Number: 10-2022-0028958); Registration Date: 2024.12.19 (Filing Date: 2022.03.07))
- 위상학적으로 보호되는 광학 메모리 소자 (발명자 Sunkyu Yu, Namkyoo Park, Seou Choi, Jeonghun Kwak, Jungmin Kim; 번호 KR 10-2624621 (Application Number: 10-2022-0000869); Registration Date: 2024.01.09 (Filing Date: 2022.01.04))
- 딥러닝을 이용한 소재 설계 방법 및 장치 (발명자 Sunkyu Yu, Namkyoo Park, Xianji Piao; 번호 KR 10-2708560 (Application Number: 10-2021-0033525); Registration Date: 2024.09.13 (Filing Date: 2021.03.15); US 12,531,137 B2 (Application Number: 17/644,445); Registration Date: 2026.01.20 (Filing Date: 2021.12.15))

## 수상과 선정

2021년 10월 22일–2026년 10월 22일 소식에 게시된 수상·선정 7건이다. 소식이 날짜 범위를 적은 경우에는 그 범위를 그대로 적었다.[^newsold][^newsmid]

- 2025-11-27 · Jongheon Yeo가 Photonics Conference 2025의 Outstanding Paper Award를 받았다. 발표 제목은 「Fidelity Benchmarking of Algorithms for Integrated Photonic Unitary Circuits」다.
- 2025-03-08 · 유선규가 American Physical Society의 Outstanding Referee로 선정되었다. 누리집은 Lifetime Award로 적는다.
- 2025-03-05 · 유선규가 Light: Science & Applications의 2024년 Outstanding Reviewer로 선정되었다. 누리집은 Annual Award로 적는다.
- 2023-06-27 · Dayeong Lee가 서울대학교 BK21 Excellent Graduate Student Award를 받았다.
- 2023-02-24 · Jungmin Kim이 서울대학교 전기·정보공학부 Distinguished Dissertation Award를 받았다.
- 2022-10-16–2022-10-20 · Dayeong Lee가 Emil Wolf Student Paper Competition의 finalist로 선정되었다. 발표 제목은 「Molecular Dynamics for Microscopic Analysis of Refractive Index in Amorphous Hafnium Oxides」다.
- 2021-12-03 · Hyungchul Park가 Photonics Conference 2021의 Outstanding Paper Award를 받았다. 발표 제목은 「Wave Transport and Localization in Hyperbolic Lattices」다.

## 소식

2021년 10월 22일–2026년 10월 22일에 게시된 논문 게재·표지 선정 소식 22건이다. 날짜는 소식의 게시 날짜이며, 논문의 온라인 출판일과 다를 수 있다.[^newsold][^newsmid][^newsnew]

- 2026-09-25 · 「Magnetic graphs for cavity quantum electrodynamics」를 Science Advances에 게재했다.
- 2026-08-06 · 「Non-Hermitian Stealthy Hyperuniformity」를 Advanced Science에 게재했고 표지 논문으로 선정되었다.
- 2026-07-28 · 「Topological heavy-tailed networks」를 Newton에 게재했다.
- 2026-06-28 · 「Fully Programmable Slow Light Based on a Spinor Representation of Generalized Coupled-Resonator-Induced Transparency」를 Advanced Science에 게재했다.
- 2026-02-25 · 「Phase-Sensitive Engineering of Optical Disordered Materials Using Heterogeneous Networks」를 Advanced Optical Materials에 게재했다.
- 2026-01-30 · 「Programmable Lattices for Non-Abelian Topological Photonics and Braiding」을 Physical Review Letters에 게재했다.
- 2025-12-10 · 「Scalable unitary computing using time-parallelized photonic lattices」를 Nanophotonics에 게재했다.
- 2025-11-12 · 「Nonlinear Unitary Circuits for Photonic Neural Networks」를 ACS Photonics에 게재했다.
- 2025-02-14 · 「Programmable photonic unitary circuits for light computing」을 Nanophotonics에 게재했다.
- 2025-01-07 · 「Deep-subwavelength engineering of stealthy hyperuniformity」를 Nanophotonics에 게재했다.
- 2024-12-23 · 「Computing Riemann zeros with light scattering」을 Physical Review B에 게재했다.
- 2024-09-18 · 「Scalable and Programmable Emulation of Photonic Hyperbolic Lattices」를 ACS Photonics에 게재했다.
- 2024-09-02 · 「Long-range-interacting topological photonic lattices breaking channel-bandwidth limit」를 Light: Science & Applications에 게재했다.
- 2024-03-05 · 「Programmable Photonic Time Circuits for Highly Scalable Universal Unitaries」를 Physical Review Letters에 게재했다.
- 2024-01-17 · 「Photonic Topological Spin Pump in Synthetic Frequency Dimensions」를 Physical Review Letters에 게재했다.
- 2023-04-03 · 「Heavy tails and pruning in programmable photonic circuits for universal unitaries」를 Nature Communications에 게재했다.
- 2023-03-08 · 「Engineering isospectrality in multidimensional photonic systems」를 Nanophotonics에 게재했다.
- 2023-02-20 · 「Unidirectional scattering with spatial homogeneity using correlated photonic time disorder」를 Nature Physics에 게재했다.
- 2023-02-13 · 「Evolving scattering networks for engineering disorder」를 Nature Computational Science에 게재했고 표지 논문으로 선정되었으며 News & Views에서 소개되었다.
- 2022-06-30 · 「Topologically Protected All-Optical Memory」를 Advanced Electronic Materials에 게재했고 표지 논문으로 선정되었다.
- 2022-02-25 · 「Machine-Engineered Active Disorder for Digital Photonics」를 Advanced Optical Materials에 게재했고 표지 논문으로 선정되었다.
- 2021-12-08 · 「Hearing the shape of a drum for light: isospectrality in photonics」를 Nanophotonics에 게재했다.

## 연락과 위치

- 교수 연구실: 서울대학교 301동 1103호[^prof][^deptprof]
- 교수 전화: 02-880-7281[^prof]
- 교수 이메일: sunkyu.yu@snu.ac.kr[^prof]

## 각주
[^home]: IWSL, Home. 파동 분야의 공통 원리와 연구 목표. <https://waves.snu.ac.kr/> 관측 2026-10-27.
[^deptlab]: 서울대학교 전기·정보공학부, 지능형 파동 시스템 연구실 소개. 개설 시점과 연구 방향. <https://ece.snu.ac.kr/research-faculty/research/lab?labidx=69&md=view> 관측 2026-10-27.
[^deptprof]: 서울대학교 전기·정보공학부, 유선규 부교수 소개. 직위·학력·경력·전공. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p828> 관측 2026-10-27.
[^prof]: IWSL, Professor. 학력·교원 경력·과제·연락처. <https://waves.snu.ac.kr/people/professor> 관측 2026-10-27.
[^ai]: IWSL, AI Wave Mechanics. 심층 신경망의 구조와 추론에 대한 연구 방향. <https://waves.snu.ac.kr/research/ai-wave-mechanics> 관측 2026-10-27.
[^photonic]: IWSL, Photonic AI. 광학 계산·네트워크·신경세포 기능과 메모리의 연구 갈래 및 관련 논문. <https://waves.snu.ac.kr/research/photonic-ai> 관측 2026-10-27.
[^members]: IWSL, Group Members. 과정·기간·연구 주제·학교 이메일. <https://waves.snu.ac.kr/people/group-members> 관측 2026-10-27.
[^alumni]: IWSL, Alumni. 이전 연구원·학부 인턴의 역할·기간·진로. <https://waves.snu.ac.kr/people/alumni> 관측 2026-10-27.
[^journals]: IWSL, Journal Articles. 사전 공개본·학술 논평·국제 및 국내 학술지 논문 목록. <https://waves.snu.ac.kr/publications/journal-articles> 관측 2026-10-27.
[^conferences]: IWSL, Conferences. 국제·국내 학회 및 초청 세미나 목록. <https://waves.snu.ac.kr/publications/conferences> 관측 2026-10-27.
[^patents]: IWSL, Patents. 발명별 국가·번호·출원일·등록일. <https://waves.snu.ac.kr/publications/patents> 관측 2026-10-27.
[^newsold]: IWSL, Group News: 2020–2022. <https://waves.snu.ac.kr/news/2020-2022> 관측 2026-10-27.
[^newsmid]: IWSL, Group News: 2023–2025. <https://waves.snu.ac.kr/news/2023-2025> 관측 2026-10-27.
[^newsnew]: IWSL, Group News: 2026–2028. <https://waves.snu.ac.kr/news/2026-2028> 관측 2026-10-27.
[^mri]: G. Yoon, S. Yu, J. Lee, N. Park, “Volumetric B1+ field homogenization in 7 Tesla brain MRI using metasurface scattering”, arXiv:2409.05350 (2024). 초록 원문 <https://arxiv.org/abs/2409.05350>. arXiv 판 초록 기준이며, 같은 페이지가 ACS Photonics 13, 1693 (2026) 및 관련 DOI 10.1021/acsphotonics.5c02781을 연결한다. 관측 2026-10-27.
[^design]: J. Kim, S. Park, S. Yu, N. Park, “Machine-Engineered Active Disorder for Digital Photonics”, Advanced Optical Materials 10, 2102642 (2022), 본문 §3. 목표 응답과 계산 응답의 차이 제곱을 평균한 비용을 이용하는 신경망 최적화로 목표 광학 응답에 맞는 층 두께를 설계한다. <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adom.202102642> 관측 2026-10-27.
[^p1]: G. Kim 외, S. Yu, Physical Review Letters 136, 043804 (온라인 2026-01-30). <https://doi.org/10.1103/rgfy-n6zd> 초록 기준(출판사 논문 페이지). 초록 원문 <https://journals.aps.org/prl/abstract/10.1103/rgfy-n6zd>. 관측 2026-10-27.
[^p2]: X. Piao, S. Yu, N. Park, Physical Review Letters 132, 103801 (온라인 2024-03-05). <https://doi.org/10.1103/PhysRevLett.132.103801> 초록 기준(출판사 논문 페이지). 초록 원문 <https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.132.103801>. 관측 2026-10-27.
[^p3]: S. Choi 외, S. Yu, Advanced Electronic Materials 8, 2200579 (온라인 2022-06-30). <https://doi.org/10.1002/aelm.202200579> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/aelm.202200579>. 관측 2026-10-27.
[^p4]: J. Suh 외, S. Yu, Physical Review Letters 132, 033803 (온라인 2024-01-17). <https://doi.org/10.1103/PhysRevLett.132.033803> 초록 기준(출판사 논문 페이지). 초록 원문 <https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.132.033803>. 관측 2026-10-27.
[^p5]: S. Yu, X. Piao, N. Park, Physical Review B 110, L220201 (온라인 2024-12-23). <https://doi.org/10.1103/PhysRevB.110.L220201> 초록 기준(출판사 논문 페이지). 초록 원문 <https://journals.aps.org/prb/abstract/10.1103/PhysRevB.110.L220201>. 관측 2026-10-27.
[^p6]: J. Kim, S. Park, S. Yu, N. Park, Advanced Optical Materials 10, 2102642 (온라인 2022-02-25). <https://doi.org/10.1002/adom.202102642> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adom.202102642>. 관측 2026-10-27.
[^p7]: G. Lee 외, S. Yu, Advanced Science 13, e77054 (온라인 2026-08-06). <https://doi.org/10.1002/advs.77054> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.77054>. 관측 2026-10-27.
[^p8]: S. Yu, X. Piao, N. Park, arXiv (온라인 2025-06-28). <https://doi.org/10.48550/arXiv.2506.22717> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2506.22717>. 관측 2026-10-27.

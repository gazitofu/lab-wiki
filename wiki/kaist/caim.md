# 소재 인공지능 연구실 (Computation and AI for Materials, CAIM Lab)

**KAIST 신소재공학과 · 김동훈 부교수**

- 분야: 계산·인공지능 모델을 이용한 에너지 소재 설계, 원자 수준 모사, 소재 생성, 자율 연구실
- 대분야: 소재, 컴퓨팅·AI
- 태그: 과학·공학 AI[^research][^p4], 분자 동역학 시뮬레이션[^p4], 광촉매·광전기화학[^p5], 태양전지[^research]
- 홈페이지: <https://www.caim.kaist.ac.kr/>
- 근거와 출처: [CAIM 근거 페이지](caim-sources.md)

> 계산과 인공지능으로 촉매·배터리·태양전지에 쓸 소재의 설계를 가속하는 연구실이다. 기존 자료에서 후보를 고르는 방법과 새로운 소재 후보를 생성하는 방법을 함께 연구한다.[^research]

## 무엇을 연구하나

CAIM은 KAIST 신소재공학과 김동훈 부교수가 이끄는 소재 인공지능 연구실이다. 연구 소개는 계산 모델과 인공지능 모델을 개발해 에너지 소재의 설계를 가속하는 것을 목표로 들며, 주된 응용으로 촉매(반응에 참여하면서 반응 속도를 높이고 전체 반응에서는 재생되는 물질), 배터리와 태양전지를 적는다.[^people][^research]

연구실은 컴퓨터를 이용한 소재 연구의 역할을 실험 결과 해석, 후보 선별, 새로운 소재 생성으로 나눠 설명한다. 후보 선별은 이미 자료에 있는 물질 가운데 목적에 맞는 것을 찾는 일이다. 생성 인공지능은 학습한 자료의 특징을 바탕으로 새 자료를 만드는 인공지능이며, 연구실은 이를 이용해 기존 자료에 없는 소재 후보를 만드는 방향을 제시한다. 연구 소개는 소재 생성이 아직 초기 단계이며 소재 개발의 효율을 바꿀 가능성이 있다고 설명한다.[^research]

연구 소개에는 원자 수준 모사(물질을 이루는 원자와 그 상호작용을 계산하는 방법), 기계학습 원자간 퍼텐셜, 소재 생성 인공지능과 자율 연구실이 나란히 올라 있다. 기계학습은 자료에서 규칙을 학습해 예측이나 판단을 수행하는 방법이고, 원자간 퍼텐셜은 원자들의 배치에 따른 상호작용 에너지를 나타내는 함수다. 자율 연구실은 실험의 계획·실행·결과 분석을 자동화하고 결과를 다음 실험의 결정에 연결하는 연구 체계다.[^research] 2026년 연구실 튜토리얼도 계산 도구 사용법과 소재 생성 모델을 다뤘다.[^events]

연구 대상은 에너지 소재에만 한정되지 않는다. 소재 과학 문헌을 다루는 질문·답변 시스템과, 강철 내부 결함의 영상·정량 자료를 만드는 연구도 있다.[^p2][^p3] 빛을 받는 광촉매(빛을 받아 화학 반응을 촉진하는 물질)와 효소(생화학 반응을 촉진하는 촉매)를 이어 지방산의 특정 위치를 화학적으로 바꾸는 공동 연구도 수행했다.[^p5] 문헌에서 얻는 지식, 원자 수준 계산, 실험에서 얻는 자료와 반응 체계를 함께 다루는 흐름이다. 최근 논문 목록에는 김동훈 교수의 KAIST 부임 전 논문도 포함돼 있다.[^pubs][^professor]

## 주요 연구 주제

### 원자 수준 계산과 에너지 소재

원자 수준 모사와 기계학습 원자간 퍼텐셜은 연구실이 제시한 계산 연구 갈래다. 응용 대상으로는 수소 에너지와 관련된 촉매, 배터리 소재와 태양전지를 든다.[^research] 암모니아 분해 연구는 금속과 산화마그네슘의 경계가 반응 단계를 어떻게 바꾸는지 기계학습 모사로 살폈다. 계산한 계에서는 수소를 떼어 내는 단계가 주로 경계에서, 질소 원자끼리 결합하는 단계가 금속 표면에서 일어나며 두 단계의 상충 관계가 완화됐다. 니켈·구리 촉매가 루테늄보다 높은 활성을 보일 것으로 예측했다.[^p1]

다른 논문은 기계학습 원자간 퍼텐셜을 이용한 분자 동역학 시뮬레이션(원자·분자에 작용하는 힘으로 운동 방정식을 시간에 따라 풀어 움직임을 계산하는 방법)의 신뢰성을 다룬다. 나트륨 산화물 고체 전해질(이온의 이동으로 전류를 전달하는 고체 물질)을 대상으로, 추가 학습 자료를 만드는 계산 자원을 같게 맞추고 자료를 고르는 방식을 비교했다. 이온은 전자를 잃거나 얻어 전하를 띤 원자 또는 원자 집단이다. 처음부터 모델을 학습할 때와 기존 모델을 조정할 때 효과적인 자료 선택 방식이 달랐다.[^p4]

### 소재 생성과 자율 연구실

연구실은 자료 안에서 소재를 찾는 선별과 자료 밖의 후보를 만드는 생성을 구별한다. 소재 생성 인공지능과 자율 연구실을 연구 갈래로 제시하고, 소재 설계에서 계산과 인공지능의 역할을 확대하려 한다.[^research] 2024년 논문 목록에는 자율 실험을 통한 금속 입자 합성, 합성 자동화를 위한 투명 화학 용기 검출, 실험 작업의 운영·일정 관리 시스템이 올라 있다. 이 논문들은 김동훈 교수의 KIST 재직 시기에 발표됐다.[^pubs][^professor]

### 소재 과학 문헌과 실험 자료

소재 과학 지식과 대형 언어 모델(많은 글을 학습해 문장을 이해하고 생성하는 인공지능 모델)을 다루는 연구에서는 구조화된 데이터베이스에 바탕을 둔 질문·답변 시스템을 구성했다. 데이터베이스는 자료를 일정한 구조로 저장하고 찾아 쓸 수 있게 만든 자료 집합이다.[^p2] 최근 목록에는 KIST 재직 시기의 소재 과학 문헌 표 자료 추출 연구 MaTableGPT도 있다.[^pubs]

강철 내부 결함 연구는 잡아당기는 시험과 반복해서 힘을 가하는 시험을 거친 시료를 엑스선 전산화단층촬영(여러 방향에서 얻은 엑스선 측정값으로 물체 내부를 단면이나 입체 영상으로 재구성하는 방법)으로 살폈다. 두 자료 모음은 내부 결함의 영상과 수치로 나타낸 특성을 함께 담아 결함의 형성과 변화를 통계적으로 분석할 수 있게 했다.[^p3]

### 빛과 효소를 잇는 화학 반응

공동 연구에서는 나트륨·칼륨을 함께 넣은 탄소 질화물 광촉매와 효소를 연결한 반응 체계를 만들었다. 광촉매가 빛을 받아 만든 과산화수소(분자식이 H2O2인 화합물)를 효소가 사용해, 연구 대상 지방산인 테트라데칸산의 특정 위치에 하이드록실기(산소 원자와 수소 원자가 결합해 이루는 부분 구조)를 붙였다. 과산화수소를 외부에서 공급하는 비교 체계보다 두 위치에서의 반응 활성이 높았다.[^p5]

## 대표 논문

김동훈 교수의 KAIST 재직 시기에 발표되고 KAIST 소속이 기재된 다섯 편을 촉매 계산, 소재 문헌 지식, 결함 자료, 원자간 퍼텐셜, 광·생촉매 반응에서 골랐다. 「쉽게 말하면」은 각 논문의 등록 초록만을 근거로 썼다. 저자 위치와 교신 표시는 등록 저자 기록을 따른다.[^roles]

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 김동훈 교수의 저자 역할 |
|---|---|---|---|---|
| 1 | 2026 | [Interfacial Cooperation-Driven Shifts of Volcano Relationships in Ammonia Decomposition](https://doi.org/10.1021/acscatal.6c02680) · ACS Catalysis | 암모니아 분해에서는 수소를 떼어 내는 단계와 질소 원자끼리 결합하는 단계 사이의 상충 관계가 촉매 선택을 제한한다. 기계학습 모사로 살펴본 금속·산화마그네슘 계에서는 수소를 떼는 단계가 주로 두 물질의 경계에서 일어나고 질소 결합은 금속 표면이 좌우했다. 반응의 제약이 다른 곳으로 나뉘면서 상충 관계가 완화됐고, 니켈과 구리가 루테늄을 넘는 활성을 낼 것으로 예측했다.[^p1] | 마지막 저자·교신저자 |
| 2 | 2026 | [Structured Domain Knowledge Enables Trustworthy Materials Science Question-Answering with Large Language Models](https://doi.org/10.1039/d6dd00028b) · Digital Discovery | 구조화된 데이터베이스 구축을 바탕으로 소재 과학 분야에 맞춘 질문·답변 시스템을 구성했다.[^p2] | 마지막 저자 |
| 3 | 2025 | [Internal Defect Database of Mechanically Deformed Ferritic Steel via X-ray Computed Tomography](https://doi.org/10.1038/s41597-025-06141-y) · Scientific Data | 강철 내부 결함의 형성과 변화는 재료의 성질과 내구성에 영향을 준다. 잡아당기는 시험을 거친 시료와 반복해서 힘을 가하는 시험을 거친 시료를 엑스선 전산화단층촬영으로 측정해 두 자료 모음을 제시했다. 내부 결함의 영상과 수치로 나타낸 특성을 함께 담아 통계 분석에 쓸 수 있게 했다.[^p3] | 마지막 저자·교신저자 |
| 4 | 2026 | [Budget-Constrained Augmentation of Universal Interatomic Potentials for Reliable Multicomponent Molecular Dynamics](https://doi.org/10.1038/s41524-026-02202-x) · npj Computational Materials | 범용 기계학습 원자간 퍼텐셜에 추가할 학습 자료를 고르는 방식을, 같은 계산 자원 한도에서 비교했다. 나트륨 산화물 고체 전해질에서는 모델을 처음부터 학습할 때 기존 자료에서 부족한 구조를 보충하는 방식이 효과적이었다. 기존 모델을 조정할 때는 원자 배치를 얼마나 고르게 뽑는지가 중요했다. 모든 학습 방식에 공통으로 가장 좋은 선택법은 없었으며, 학습 방식에 맞춰 추가 자료를 골라야 한다는 결과다.[^p4] | 중간 저자·교신저자 |
| 5 | 2026 | [Regioselective C-H Oxyfunctionalization of Aliphatic Acids Through a Consecutive Biosolar Cascade](https://doi.org/10.1002/smll.75979) · Small | 나트륨·칼륨을 함께 넣은 탄소 질화물 광촉매와 효소를 잇는 반응 체계를 만들었다. 광촉매가 빛을 받아 과산화수소를 만들면 효소가 이를 사용해 테트라데칸산의 정해진 위치에 하이드록실기를 붙였다. 과산화수소를 외부에서 공급하는 비교 체계보다 두 위치에서의 반응 활성이 높았다.[^p5] | 중간 저자로 참여한 공동 연구 |

## 교수와 전문 분야

김동훈 교수의 누리집 소개는 2025년부터 KAIST 신소재공학과 Associate Professor로 재직하고, 2015–2025년에는 KIST 전산과학연구센터 선임연구원으로 일했다고 적는다. 2010년 POSTECH 신소재공학 학사, 2015년 MIT 신소재공학 박사 학위를 받았다.[^professor] 2025년 4월 17일 소식에는 KAIST에서 CAIM 연구실 출범을 알리는 글이 있다.[^events]

현재 연구 소개와 논문 목록을 함께 보면 전문 분야는 계산과 인공지능을 이용한 소재 설계다. 원자 수준 계산과 기계학습 원자간 퍼텐셜, 소재 생성, 자율 연구실을 연구 소개에 올리고, 문헌 자료 추출과 에너지 소재·촉매 연구를 논문 목록에 담고 있다.[^research][^pubs] 대한금속재료학회 인공지능재료과학분과에서는 2020–2024년 총무, 2024년부터 부위원장을 맡았다고 소개한다.[^professor]

대표 논문에서는 촉매 반응의 계산과 구조 재료의 결함 자료 연구에서 마지막·교신저자로, 원자간 퍼텐셜 연구에서는 중간·교신저자로 참여한다. 소재 과학 질문·답변 연구의 마지막 저자이며, 광촉매와 효소를 잇는 반응 연구에는 공동 연구자로 참여했다.[^p1][^p2][^p3][^p4][^p5][^roles]

## 응용 분야

연구실이 직접 밝힌 응용은 촉매, 배터리와 태양전지를 위한 에너지 소재 설계다.[^research] 대표 논문의 대상에는 암모니아 분해 촉매, 고체 전해질의 원자 수준 모사와 강철 내부 결함의 정량 자료가 있다. 빛과 효소를 연결한 반응 체계는 지방산의 선택적 화학 변환을 다룬다.[^p1][^p3][^p4][^p5] 2025년 6월 소식은 CAIM이 지능형 수소기술 혁신연구단에 참여한다고 알린다.[^events]

## 구성원

2026년 10월 31일 People 명단에는 교수 외 연구 구성원 10명이 있다. InnoCORE Postdoctoral Fellow 3명, 박사과정 2명, 석사과정 4명, 학부생 1명이다. 권오민과 조명근은 계산팀, 오기석은 실험팀의 Lead로, 이경훈은 Lab Chief로 기재돼 있다.[^people] 연구 주제와 2025년부터의 박사후 재직 표기는 각 개인 소개를 따르고, 오정호·장우찬의 시작 칸은 합류 공지 날짜다.[^bios][^events] 「대표 논문 참여」는 위 표의 번호이며, 전체 저자 목록에서 같은 이름을 확인해 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Ohmin Kwon (권오민) | 박사후연구원 | 2025– (현재) | AI for Materials, MLP (machine learning potential), Multiscale modeling, Electrocatalyst, Optimization |  |
| Kiseok Oh (오기석) | 박사후연구원 | 2025– (현재) | Solid Electrolyte Battery, Electrochemistry, Photoelectrochemistry, Machine Learning, Automation, Robotics |  |
| Myungkeun Cho (조명근) | 박사후연구원 |  |  |  |
| Gyeong Hoon Yi (이경훈) | 대학원생 (Ph. D. course) |  | Inverse design, Synthesis planning, Generative AI, LLMs, Self-driving lab, Energy materials | 2, 3 |
| Jungho Oh (오정호) | 대학원생 (Ph. D. course) | 2026-07-13 합류 공지 | Inverse design, Synthesis planning, Self-driving lab, Energy materials |  |
| Sihyun Joo (주시현) | 대학원생 (MS course) |  | DFT, Machine learning potential, Generative AI for material discovery, Multi-scale modeling, Self-driving lab, Catalyst |  |
| Junho Yang (양준호) | 대학원생 (MS course) |  | Generative AI for material discovery, Multiscale Modeling, Electrocatalyst |  |
| Dongwoo Kim (김동우) | 대학원생 (MS course) |  | Self-driving labs, AI for discovery, Inverse design, Synthesis planning, LLMs, Battery |  |
| Junhyeon Mun (문준현) | 대학원생 (MS course) |  |  |  |
| Woochan Jang (장우찬) | 학부 연구생 (BS course) | 2026-07-13 합류 공지 |  |  |

주시현은 정연식 교수, 양준호는 홍승범 교수, 김동우는 서동화 교수와 공동 지도를 받는다고 개인 소개에 적혀 있다.[^bios]

## 졸업생과 이전 구성원

2026년 10월 31일 People 명단의 이전 박사후연구원 4명과 대학원 또는 그에 준하는 연구 훈련을 받은 이전 구성원 5명이다. 학력과 진로는 명단의 표기다. 학력에 붙은 연도는 학위 연도이며 CAIM 재직 종료나 수료 연도가 아니다. KAIST 연구실 출범 전 이력도 포함한다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Mingyu Jeon (전민규) | Postdoctoral researcher; PhD Chemical and Biomolecular Engineering, KAIST, Korea (2024); MS Chemical and Biomolecular Engineering, KAIST, Korea (2021); BS Chemical and Biomolecular Engineering,KAIST, Korea (2019) | Assistant Professor at Kyungpook National University (경북대학교 응용화학공학과) |
| Jungwoo Choi (최정우) | Postdoctoral researcher; PhD Materials Science and Engineering, KAIST, Korea (2024); MS Materials Science and Engineering, KAIST, Korea (2019); BS Materials Science and Engineering, Korea University, Korea (2017) | Assistant Professor at Dankook University (단국대학교 고분자시스템공학부 융합소재공학과) |
| Doosun Hong (홍두선) | Postdoctoral researcher; PhD Materials Science and Engineering, KAIST, Korea (2022); MS Materials Science and Engineering, KAIST, Korea (2017); BS Materials Science and Engineering, Physics (Dual), Hanyang University, Korea (2015) | Assistant Professor at University of Seoul (서울시립대 신소재공학과) |
| Leslie Tiong (레슬리 티옹) | Postdoctoral researcher; PhD Information and Telecommunication Technology (Engineering), KAIST, Korea (2019); MS Computer Science, Lancaster University, UK (2014); BS Computer Science, Sunway University, Malaysia (2012) | Senior reseacher at Samsung Electronics |
| Jiwoo Choi (최지우) | PhD Materials Science and Engineering, Korea University, Korea (2026); BS Applied Chemistry, KyungHee University, Korea (2021) | Postdoctoral researcher at KIST |
| Daegun Lee (이대건) | MS Materials Science and Engineering, Korea University, Korea (2025); BS Chemistry (minor in Materials Science), Yonsei University, Korea (2022) |  |
| Seunghan Lee (이승한) | MS Chemical and Biomolecular Engineering, Sogang University, Korea (2023); BS Chemical and Biomolecular Engineering, Sogang University, Korea (2021) | Ph.D course at Northwestern University |
| Sungyeon Hong (홍성연) | PhD Australian National University (2023); MS Mathematics, École Polytechnique Fédérale de Lausanne (EPFL), Switzerland (2017); BS Mathematics, KAIST, Korea (2015) | Research fellow at Australian National University (ANU) |
| Myungjoon Kim (김명준) | PhD Materials Science and Engineering, KAIST, Korea (2023); MS Materials Science and Engineering, KAIST, Korea (2017); BS Materials Science and Engineering (Double major: Computer Science), KAIST, Korea (2015) | Postdoctoral researcher at Cornell University |

## 최근 논문 목록 (2021–2026)

에너지 소재·촉매, 원자 수준 계산, 소재 과학 문헌과 실험 자료를 다룬다. 연구실 Publication의 2021–2026년 구역에 게시된 학술지 논문 27편과 해설 2건이다. 김동훈 교수의 KAIST 부임 전 KIST 재직 시기 성과도 섞여 있다. 제목·저자·발표처는 연구실 표기를 따르고, 연도는 게시 구역이다. 날짜 없이 연도만 적힌 2021년 항목도 그 구역대로 실었다. 별표와 더하기 표시는 누리집 표시다.[^pubs][^professor]

**2026**

- CH Lee, MS Byun, HW Kim, K Park, D Kim, S Hong, SJ Yeom, CB Park\*. "Regioselective C-H Oxyfunctionalization of Aliphatic Acids Through a Consecutive Biosolar Cascade". *Small (2026), 0:e75979*.
- H Lee, Y Song, H Kim, M Kwon, S Ham, J Kim, D Kim\*, DH Seo\*. "Budget-Constrained Augmentation of Universal Interatomic Potentials for Reliable Multicomponent Molecular Dynamics". *npj Computational Materials (2026), Early Access*.
- J Choi, S Kang, BC Yeo\*, D Kim\*. "Interfacial Cooperation-Driven Shifts of Volcano Relationships in Ammonia Decomposition". *ACS Catalysis 16, 14471 (2026)*.
- D Lee, J Choi, GH Yi, SS Sohn, B Lee\*, D Kim\*. "Structured Domain Knowledge Enables Trustworthy Materials Science Question-Answering with Large Language Models". *Digital Discovery 5:2243-2253, (2026)*.

**2025**

- G Lee+, GH Yi+, L Tiong, SS Sohn\*, D Kim\*. "Internal Defect Database of Mechanically Deformed Ferritic Steel via X-ray Computed Tomography". *Scientific data 12, 1871 (2025)*.
- GH Yi+, J Choi+, H Song+, O Miano, J Choi, K Bang, B Lee, SS Sohn, D Buttler, A Hiszpanski\*, SS Han\*, D Kim\*. "MaTableGPT: GPT-Based Table Data Extractor from Materials Science Literature". *Advanced Science 12, 2408221 (2025)*.
- S Jeong+, KB Kim+, M Jeon+, JY Kim, JH Lee, SY Jang, DW Jeon, JM Park, CY Yoo, D Kim, JH Lee, SB Cho\*, YC Kang\*, JS Park\*. "Investigation on the Effect of Metal Incorporation in Metal Selenide Nanoparticles and Their Encapsulation in Hollow Carbon Nanospheres on Improving the Sodium-ion Battery Performance". *Chemical Engineering Journal 512, 167019 (2025)*.
- J Yoo+, CH Chan+, SY Choi, D Hong, SY Park, K Bang, JM Kim, D Kim\*, SS Han\*, HM Lee\*. "Simultaneous Enhancement of Activity and Durability of Oxygen Reduction Reaction Enabled by Pd3Mo@Pt/C Catalysts". *ACS Applied Materials & Interfaces 17, 22498 (2025)*.
- GR Lee+, K Song+, D Hong+, J Ahn, Y Roh, M Kim, D Kim\*, YS Jung\*, JY Park\*. "Unraveling Oxygen Vacancy-Driven Catalytic Selectivity and Hot Electron Generation on Heterointerfaces Using Nanostructured Platform". *Nature Communications 16:2909 (2025)*.

**2024**

- HJ Yoo, KY Lee\*, D Kim\*, SS Han\*. "OCTOPUS: Operation Control System for Task Optimization and Job Parallelization via a User-Optimal Scheduler". *Nature Communications 15:9669 (2024)*.
- BC Yeo\*, SY Jeong, JS Kim, D Kim. "Discovery of Alloy Catalysts for Ammonia Decomposition by Machine Learning-Based Prediction of Adsorption Energies". *Korean Journal of Metals and Materials 62, 920 (2024)*.
- S Choi+, D Hong+, J Yoo, C Lee, K Bang, JM Kim, SS Han\*, D Kim\*, HM Lee\*. "Enhancing Fuel Cell Durability with Heteroenergetic TaOx-Carbon Support". *ACS Energy Letters 9, 4265 (2024)*.
- HJ Shin+, D Hong+, H Cho, H Jang, GY Kim, KM Song, GY Kim, MJ Choi\*, D Kim\*, YS Jung\*. "Indirect-to-direct bandgap transition in GaP semiconductors through quantum shell formation on ZnS nanocrystals". *Nature Communications 15:8125 (2024)*.
- HJ Yoo+, N Kim+, HS Lee, DH Kim, L Tiong, CS Kim, SY Lee, KY Lee\*, D Kim\*, SS Han\*. "Bespoke Metal Nanoparticle Synthesis at Room Temperature and Discovery of Chemical Knowledge on Nanoparticle Growth Via Autonomous Experimentations". *Advanced Functional Materials 34, 2312561 (2024)*.
- K Bang+, J Kim+, D Hong+, D Kim\*, SS Han\*. "Inverse Design for Materials Discovery from Multidimensional Electronic Density of States". *Journal of Materials Chemistry A 12, 6004 (2024)*.
- L Tiong+, HJ Yoo+, NY Kim, KY Lee\*, SS Han\*, D Kim\*. "Machine Vision-based Detections of Transparent Chemical Vessels Toward the Safe Automations of Material Synthesis". *npj Computational Materials 10, 42 (2024)*.

**2023**

- J Choi+, K Bang+, S Jang, JW Choi, J Ordonez, D Buttler, A Hiszpanski, TYJ Han, SS Sohn, B Lee, KR Lee, SS Han\*, D Kim\*. "Deep Learning of Electrochemical CO2 Conversion Literature Reveals Research Trends and Directions". *Journal of Materials Chemistry A 11, 17628 (2023)*.
- GR Lee+, J Kim+, D Hong+, YJ Kim, HJ Han, H Jang, CG Hwang, D Kim\*, JY Kim\*, YS Jung\*. "Efficient and Sustainable Water Electrolysis Achieved by Excess Electron Reservoir Enabling Charge Replenishment to Catalysts". *Nature Communications 14:5402 (2023)*.
- Y Park+, CK Hwang+, K Bang, D Hong, H Nam, SH Kwon, BC Yeo, D Go, J An, BK Ju, SH Kim, JY Byun, SY Lee, JM Kim\*, D Kim\*, SS Han\*, HM Lee\*. "Machine Learning Filters Out Efficient Electrocatalysts in the Massive Ternary Alloy Space for Fuel Cells". *Applied Catalysis B: Environmental 339, 123128 (2023)*.
- K Bang, D Hong, Y Park, D Kim\*, SS Han\*, HM Lee\*. "Machine Learning-Enabled Exploration of the Electrochemical Stability of Real-Scale Metallic Nanoparticles". *Nature Communications 14:3004 (2023)*.
- L Tiong+, G Lee+, GH Yi, SS Sohn\*, D Kim\*. "Predicting Failure Progressions of Structural Material via Deep Learning Based on Void Topology". *Acta Materialia 250, 118862 (2023)*.
- HW Lee+, GU Jeong+, MC Kim, D Kim\*, SY Kim\*, SS Han\*. "Atomistic Origin of Mechanochemical NH3 Synthesis on Fe Catalysts". *International Journal of Hydrogen Energy 48, 3931 (2023)*.

**2022**

- 정두엽, 조유진 (원고작성: 한상수, 김동훈, 이노도). "소재 신(新)연구방법론". *KISTEP브리프 Vol.14 (발행기관: KISTEP 성장동력사업센터)*.

**2021**

- HW Lee+, E Jung+, GH Han+, MC Kim, D Kim, KY Lee\*, SS Han\*, T Yu\*. "Three-in-One Strategy to Improve both Catalytic Activity and Selectivity: Nonconcentric Pd-Au Nanoparticles". *Journal of Physical Chemistry Letters 12, 11098 (2021)*.
- J Kim+, L Tiong+, D Kim\*, SS Han\*. "Deep Learning-Based Prediction of Material Properties Using Chemical Compositions and Diffraction Patterns as Experimentally Accessible Inputs". *Journal of Physical Chemistry Letters 12, 8376 (2021)*.
- BC Yeo+, H Nam+, H Nam, MC Kim, HW Lee, D Kim, KY Lee, SY Lee\*, SS Han\*. "High-Throughput Computational-Experimental Screening Protocol for the Discovery of Bimetallic Catalysts". *npj Computational Materials 7, 137 (2021)*.
- 한상수, 김동훈. "AI로봇이 스스로 소재를 개발한다고?". *융합연구리뷰 Vol.7 No.5 (발행기관: KIST 융합연구정책센터)*.
- K Bang, BC Yeo, D Kim, SS Han\*, HM Lee\*. "Accelerated Mapping of Electronic Density of State Patterns of Metallic Nanoparticles Via Machine-Learning". *Scientific Reports 11, 11604 (2021)*.
- HW Lee+, H Nam+, GH Han+, YH Cho, BC Yeo, D Kim\*, KY Lee\*, SY Lee\*, SS Han\*. "Solid-Solution Alloying of Immiscible Pt and Au Boosts Catalytic Performance of H2O2 Direct Synthesis". *Acta Materialia 205, 116563 (2021)*.

## 수상과 선정

김동훈 교수 소개와 연구실 소식의 2021년 10월 13일–2026년 10월 13일 범위에 해당하는 수상·선정과 공지다. 연도만 적힌 항목은 그 연도 표기를 따랐다. 2023–2024년 KIST 재직 중 성과와 KAIST 출범 전 수상 공지도 포함한다.[^professor][^events][^posco]

- 2026-10-01 · 김동훈 교수, 포스코청암재단 POSCO Science Fellow 선정. 시상식은 서울 포스코센터에서 열렸다.
- 2024 · 김동훈 교수, KIST Excellent Research Team of the Year(우수연구개발팀 상).
- 2023-10-23 (공지) · KIST Young Fellow 수상 공지.
- 2023 · 김동훈 교수, KIST Researcher of the Month(이달의 KIST인 상).

## 소식

연구실 소식의 연구·학술 행사와 연구실 출범 공지다. 2024년 10월 28일–2026년 9월 30일에 해당하는 15건이며, KAIST 출범 전 행사도 포함한다. 날짜 범위는 누리집의 행사 날짜이고, 2026년 4월 30일 글은 누리집 기재 날짜를 표시했다.[^events]

- 2026-09-28–2026-09-30 · AI4SCI KOREA 2026에 참석해 소재 인공지능 연구를 공유하고 의견을 교환했다.
- 2026-09-14 · KAIST에서 KAIST·KENTECH·이화여자대학교가 함께하는 AI4S&T 출범식을 열었다.
- 2026-08-19–2026-08-21 · 인공지능 기반 소재 연구를 다루는 2026 AI-Materials Summer School에 참가했다.
- 2026-08-06 · 연구실 튜토리얼을 열어 CP-VASP 사용법, SevenNet, 소재 생성 모델을 다뤘다.
- 2026-06-24–2026-06-26 · 김동훈 교수가 KAIST에서 전산재료과학분과 여름학교를 조직하고 개최했다. 주제는 반도체 물성과 공정 모사다.
- 2026-04-30 (누리집 기재 날짜) · 2026 춘계 금속재료학회 안내에 소재 실험 지능화·디지털화 심포지엄과 인공지능재료과학분과가 기재돼 있다.
- 2026-04-28–2026-04-29 · 제주에서 열린 춘계 대한금속재료학회의 전산재료과학분과·인공지능재료과학분과 학술대회에 참석했다.
- 2026-02-04–2026-02-05 · 연구실 튜토리얼에서 연구 도구, 계산 작업 흐름과 실용적인 사용 방법을 공유했다.
- 2025-09-30 · 대학원생을 위한 첫 연구 튜토리얼을 열었다.
- 2025-06-30–2025-07-01 · 국민대학교에서 열린 금속재료학회 인공지능분과 여름학교에 참가했다.
- 2025-06-18 · InnoCORE 센터가 지능형 수소기술 혁신연구단으로 선정됐으며 CAIM이 참여한다고 알렸다.
- 2025-04-23–2025-04-25 · 춘계 금속재료학회 안내에 소재 실험 지능화·디지털화 심포지엄과 인공지능재료과학분과가 기재돼 있다.
- 2025-04-17 · KAIST에서 CAIM 연구실 출범을 알렸다.
- 2025-02-05–2025-02-07 · 김동훈 교수가 KAIST에서 열린 Nature Conference에서 자율 연구실 연구를 발표했다.
- 2024-10-28–2024-10-30 · 평창에서 열린 추계 금속재료학회에 연구실 팀이 참석해 연구를 공유했다.

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291 KAIST W1 응용공학동 3307호, 우편번호 34141[^recruit]
- 교수 이메일: donghun.kim@kaist.ac.kr[^events]
[^research]: CAIM Lab, Research. 계산·인공지능 모델을 개발해 촉매·배터리·태양전지용 소재 설계를 가속한다는 소개와 연구 갈래. <https://www.caim.kaist.ac.kr/research> (2026-10-31 열람)
[^people]: CAIM Lab, People. 교수, 현재 구성원과 Alumni 두 구획의 명단. <https://www.caim.kaist.ac.kr/people> (2026-10-31 열람)
[^pubs]: CAIM Lab, Publication. 2021–2026년 구역과 이전 연도 구역의 게시 목록. <https://www.caim.kaist.ac.kr/publication> (2026-10-31 열람)
[^professor]: CAIM Lab, Prof. Donghun Kim. 직위·소속, 학력·경력, 학회 활동과 수상. <https://www.caim.kaist.ac.kr/people-professor/donghunkim> (2026-11-01 열람)
[^bios]: CAIM Lab, 구성원 개인 소개. 권오민 <https://www.caim.kaist.ac.kr/people-members/ohminkwon>, 오기석 <https://www.caim.kaist.ac.kr/people-members/kiseokoh>, 이경훈 <https://www.caim.kaist.ac.kr/people-members/gyeonghoonyi>, 오정호 <https://www.caim.kaist.ac.kr/people-members/jeongho>, 주시현 <https://www.caim.kaist.ac.kr/people-members/sihyunjoo>, 양준호 <https://www.caim.kaist.ac.kr/people-members/junhoyang>, 김동우 <https://www.caim.kaist.ac.kr/people-members/dongwookim> (2026-11-01 열람)
[^events]: CAIM Lab, Event-sub. 연구실 행사·소식·수상 공지 30건의 목록과 본문. <https://www.caim.kaist.ac.kr/event-sub> (2026-11-01 열람)
[^posco]: CAIM Lab, Professor Donghun Kim Selected as a 2026 POSCO Science Fellow. <https://www.caim.kaist.ac.kr/event-sub/event-one-zl4y5-ej22w-55pem-3wngn> (2026-10-01 행사, 2026-11-01 열람)
[^recruit]: CAIM Lab, Recruit. 연구실 위치. <https://www.caim.kaist.ac.kr/recruit> (2026-11-01 열람)
[^p1]: J. Choi, S. Kang, B. C. Yeo, D. Kim, ACS Catalysis (2026). <https://doi.org/10.1021/acscatal.6c02680> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1021/acscatal.6c02680> (2026-11-01 열람)
[^p2]: D. Lee 외, D. Kim, Digital Discovery (2026). <https://doi.org/10.1039/d6dd00028b> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1039/d6dd00028b> (2026-11-01 열람)
[^p3]: G. Lee 외, D. Kim, Scientific Data (2025). <https://doi.org/10.1038/s41597-025-06141-y> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1038/s41597-025-06141-y> (2026-11-01 열람)
[^p4]: H.-J. Lee 외, D.-H. Seo, npj Computational Materials (2026). <https://doi.org/10.1038/s41524-026-02202-x> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/smll.75979|10.1021/acscatal.6c02680|10.1038/s41524-026-02202-x|10.1038/s41597-025-06141-y|10.1039/d6dd00028b> (2026-11-01 열람)
[^p5]: C. H. Lee 외, C. B. Park, Small (2026). <https://doi.org/10.1002/smll.75979> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1002/smll.75979> (2026-11-01 열람)
[^roles]: OpenAlex 등록 저자 기록. 대표 논문 1–5의 김동훈 KAIST 소속, 전체 저자 순서와 교신 표시. <https://api.openalex.org/works?per-page=50&select=doi,title,publication_year,authorships&filter=doi:10.1021/acscatal.6c02680|10.1039/d6dd00028b|10.1038/s41597-025-06141-y|10.1038/s41524-026-02202-x|10.1002/smll.75979> (2026-11-01 열람)

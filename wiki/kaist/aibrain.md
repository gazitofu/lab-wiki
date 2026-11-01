# 뇌 기계지능 연구실 (Brain x Machine Intelligence Lab)

**KAIST 뇌인지과학과·김재철AI대학원(겸임)·데이터사이언스대학원(겸임)·바이오및뇌공학과(겸임) · 이상완 부교수·KAIST 지정 석좌교수**

- 대분야: 컴퓨팅·AI, 기초생명·생물물리
- 태그: 계산신경과학[^intro][^p1], 뇌 모방 인공지능[^research][^p4], 강화학습[^p2][^p3], 생성 인공지능[^p6][^p7], AI·기계학습 보안·프라이버시[^security]
- 홈페이지: <https://aibrain.kaist.ac.kr/>
- 교수: 이상완(Sang Wan Lee)[^bcs][^pi][^chair]
- [근거와 읽은 자료](aibrain-sources.md)

> 뇌가 여러 학습 전략을 선택하고 경험에서 추론하는 원리를 계산 모형으로 설명하며, 그 원리에서 착안한 인공지능 학습법과 인간·AI 협력 기술을 연구한다.

## 무엇을 연구하나

뇌 기계지능 연구실은 계산신경과학(뇌와 신경계의 정보 처리를 수학 모형과 계산으로 설명하는 분야)과 인공지능을 연결한다. 뇌가 적은 경험에서 배우고, 미래를 예측하고, 상황에 맞는 목표를 정하는 과정을 이해하는 것이 중심 질문이다. 특히 전전두피질(이마 쪽 대뇌피질의 앞부분)이 서로 다른 방식으로 문제를 푸는 체계들을 어떻게 조절하는지 연구한다.[^intro]

연구의 한 방향은 뇌의 학습을 인공지능 관점에서 이해하는 Brain↦AI다. 강화학습(행동의 결과로 받는 보상을 바탕으로 행동 방법을 배우는 기계학습)과 추론을 설명하는 모형을 만들고 행동·뇌 활동 자료와 비교한다. 기능적 자기공명영상(functional magnetic resonance imaging, fMRI, 혈액의 산소화 변화와 관련된 자기공명 신호로 뇌 활동을 간접 측정하는 영상법)과 뇌파 측정(electroencephalography, EEG, 신경세포 집단의 활동에 따른 전기적 변화를 기록하는 방법)을 활용한다. 연구실은 여러 학습 체계 가운데 행동을 맡을 체계를 조절하는 기능을 전전두 메타인지 제어라고 부른다.[^research][^intro]

다른 방향은 뇌에서 얻은 원리를 새로운 인공지능 모형으로 구현하는 AI↦Brain이다. 뇌에서 착안한 모형이 실험 자료를 설명하는지 살펴보고, 별도의 인공지능으로 새로운 경험을 만들어 뇌 기능에 관한 가설을 세우려 한다. 목표는 뇌와 인공지능의 행동이 비슷한지 비교하는 데서 나아가, 각각이 어떤 계산으로 행동을 만들어 내는지 이해하는 것이다.[^intro][^research]

최근 논문에서는 다른 사람의 행동까지 고려해 자기 영향력을 추론하는 모형, 개인 경험과 다른 사람의 경험 가운데 무엇을 이용할지 고르는 방법, 안전을 고려한 탐색을 다룬다.[^p1][^p2][^p3] 목표와 불확실성의 표현으로 안정성과 유연성을 함께 설명하는 연구, 예상한 결과가 나왔는지에 따라 선택 전략을 바꾸는 계산 모형도 다룬다.[^supp-j60][^supp-j57]

인공지능 쪽에서는 신경망(연결된 계산 단위들이 신호를 주고받으며 입력과 출력의 관계를 나타내는 계산 모형)의 사전 학습(본격적인 대상 과제의 학습에 앞서 자료의 특성이나 계산 방식을 미리 배우는 과정), 편향 완화, 글에 맞는 이미지 생성과 영상의 움직임을 옮기는 방법을 연구한다.[^p4][^p5][^p6][^p7]

## 주요 연구 주제

### 자기 통제력과 학습 전략의 계산 모형

여러 사람이 결과에 영향을 줄 때 자신의 행동이 결과를 바꾸는 정도를 어떻게 추론하는지 연구한다. 대표 논문 1은 자신과 다른 사람의 행동·결과 관계를 함께 사용하는 새 추론 모형을 제안하고, 뇌 활동 분석과 연결했다. 여기서 베이즈 추론(기존의 믿음과 새로 관찰한 자료를 결합해 가능성에 대한 판단을 갱신하는 방법)을 사용해 통제력에 대한 판단을 설명한다.[^p1]

대표 논문 2는 직접 경험해서 배우는 개인 학습과 다른 사람의 행동을 따라 배우는 사회 학습을 함께 다룬다. 성공한 사람을 따르는 방법과 다수가 하는 행동을 따르는 방법의 성능이 환경의 불확실성에 따라 달라진다는 점에서 출발해, 학습 방법 자체를 선택하는 메타제어(문제를 푸는 여러 처리 과정 중 어느 것을 사용할지 조절하는 작용)를 제안했다.[^p2] 대표 논문 3은 보상을 얻는 행동과 위험을 피하는 행동의 비중을 불확실성에 따라 조절하는 모형으로 안전과 학습 효율의 관계를 설명한다.[^p3]

강화학습의 예측 오차(예측한 결과와 실제로 얻은 결과의 차이)를 상황에 맞춰 보정하는 이론도 연구했다. 편향·분산 절충(일정한 방향으로 틀리는 오차와 자료에 따라 예측이 달라지는 정도의 균형을 다루는 문제)의 해결책으로 예측 오차의 기준값을 조절하는 방법을 제안하고, 환경이 변하는 학습 과제에서 행동 자료와 연결했다.[^supp-j42]

### 뇌에서 착안한 학습과 편향 완화

대표 논문 4는 무작위 신호로 미리 학습한 신경망이 이후의 과제를 어떻게 배우는지 다룬다. 피드백 정렬(feedback alignment, 학습 오차를 전달하는 연결과 신호를 앞으로 전달하는 연결의 관계를 학습 과정에서 맞추는 방법)을 쓰는 신경망에서, 무작위 신호를 이용한 사전 학습이 이후의 학습과 새로운 자료에 대한 대응에 도움이 될 수 있음을 보였다.[^p4]

대표 논문 5는 학습 자료에 우연히 함께 나타난 특징을 정답의 근거로 사용하는 문제를 다룬다. 편향된 신경망 안에서 이런 특징에 의존하지 않는 부분 구조를 찾도록 연결을 선택하는 DCWP(Debiased Contrastive Weight Pruning)를 제안했다. 이 방법은 자료를 집단별로 구분하는 추가 주석 없이 편향을 완화하는 부분 신경망을 찾는다.[^p5] 별도의 적대적 학습(모형을 오판하게 하려는 입력 변화에 대응하도록 모형을 학습시키는 방법) 연구에서는 입력뿐 아니라 신경망 내부 표현에도 변화를 가해 공격에 대한 방어를 학습한다.[^security]

### 글에 맞는 이미지와 영상 생성

확산 모형(자료에 잡음을 더하는 과정에 대응해 잡음을 제거하는 복원 과정을 학습하고 이를 이용해 자료를 생성하는 모형)을 이용해 글의 의미에 맞는 이미지와 원하는 움직임을 담은 영상을 만드는 방법을 연구한다. 대표 논문 6은 생성 이미지가 입력 문장의 의미를 제대로 반영하지 못하는 문제를 다룬다. 글의 문맥을 나타내는 값을 생성 과정에서 조절하는 에너지 기반 모형(각 상태에 부여한 에너지 값으로 그 상태의 적합성이나 가능성을 나타내는 모형)을 제안했다.[^p6]

대표 논문 7은 영상의 연속된 화면에 담긴 움직임을 추출해 다른 영상으로 옮기는 SMA(Spectral Motion Alignment)를 제안한다. 움직임을 주파수 성분(시간이나 공간에 따라 반복되는 변화의 빠르기로 구분한 구성 요소)으로 분석해 영상 전체의 움직임을 반영하고 공간적 왜곡을 줄이는 방향을 다룬다.[^p7]

### 생성 모형의 실행 단계 보정

대표 논문 8은 증류(기존 모형의 지식이나 동작을 다른 모형이 배우도록 전달하는 학습 방법)로 만든 확산 모형을 실제 생성 과정에서 보정하는 Distillation++를 제안한다. 추가 원자료를 사용하거나 모형을 다시 조정하는 학습 없이, 원래 모형의 안내를 생성 단계에 넣어 결과를 보정한다. 설명의 대상은 2024년 arXiv 사전 공개본이다.[^p8]

## 대표 논문

이상완이 저자인 2021–2026년 문헌에서 판단 모형, 사회 학습·안전한 탐색, 뇌에서 착안한 학습·편향 완화, 영상 생성의 갈래를 골랐다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 학회 대응 표시가 있는 arXiv 문헌은 그 판본을 밝혔으며, eLife 문헌은 Reviewed Preprint v2다.

| 번호 | 연도 | 논문·판본 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2021 | [Neurocomputational mechanism of controllability inference under a multi-agent setting](https://doi.org/10.1371/journal.pcbi.1009549)[^p1] | 자신과 다른 사람의 행동이 결과에 미치는 영향을 함께 고려해 자기 통제력을 추론하는 모형이다. 뇌 활동 분석으로 그 추론과 관련된 뇌 영역을 살폈다. |
| 2 | 2022 | [Meta-control of social learning strategies](https://doi.org/10.1371/journal.pcbi.1009882)[^p2] | 직접 배우기, 성공한 사람 따르기, 다수 따르기를 환경의 변화와 불확실성에 맞춰 선택한다. 여러 환경의 모의실험에서 학습과 탐색 비용의 관계를 분석했다. |
| 3 | 2025 | [Balancing safety and efficiency in human decision making](https://doi.org/10.7554/eLife.101371.2)[^p3] · Reviewed Preprint v2 | 보상을 얻는 판단과 위험을 피하는 반응을 구분하고, 불확실성에 따라 둘의 비중을 조절한다. 모의실험과 인간 행동 자료에서 선택과 반응 시간을 설명했다. |
| 4 | 2024 | [Pretraining with random noise for fast and robust learning without weight transport](https://arxiv.org/abs/2405.16731)[^p4] · NeurIPS 2024 대응 arXiv 판 | 신경망을 무작위 신호로 먼저 학습시킨 뒤 대상 과제를 학습시켰다. 신호 전달 연결을 그대로 복사해 되돌리는 과정 없이도 학습 효율과 새로운 자료에 대한 대응이 향상될 수 있음을 보였다. |
| 5 | 2023 | [Training debiased subnetworks with contrastive weight pruning](https://arxiv.org/abs/2210.05247)[^p5] · CVPR 2023 대응 arXiv 판, 최초 공개 2022 | 우연한 상관관계에 편향된 신경망 안에서 그 편향에 의존하지 않는 부분 신경망을 찾는다. 집단 구분 주석 없이 연결을 선택하는 알고리즘을 제안했다. |
| 6 | 2023 | [Energy-based cross attention for Bayesian context update in text-to-image diffusion models](https://doi.org/10.52202/075280-3339)[^p6] | 이미지 생성 중에 글의 문맥을 나타내는 값을 조절해 입력 문장의 뜻을 반영하도록 한다. 여러 개념을 함께 생성하거나 이미지 일부를 수정하는 과제에 적용했다. |
| 7 | 2025 | [Spectral motion alignment for video motion transfer using diffusion models](https://arxiv.org/abs/2403.15249)[^p7] · AAAI 2025 대응 arXiv 판, 최초 공개 2024 | 영상 전체의 움직임을 주파수 성분으로 분석해 다른 영상에 옮기는 방법이다. 움직임 전달과 영상의 공간적 왜곡을 함께 다뤘다. |
| 8 | 2024 | [Inference-time diffusion model distillation](https://arxiv.org/abs/2412.08871)[^p8] · arXiv | 압축한 확산 모형이 이미지를 만들 때 원래 모형의 안내로 결과를 보정한다. 추가 원자료나 재학습 없이 생성 단계를 조절하는 방법을 제안했다. |

## 교수와 전문 분야

이상완은 KAIST에서 2009년 전기·전자·컴퓨터 분야 박사학위를 받았으며, MIT 박사후연구원과 Caltech Della Martin 박사후연구원을 거쳤다. KAIST 신경과학-인공지능 융합연구센터의 창립 센터장이다.[^pi][^bcs] 연구실은 2015–2023년 바이오및뇌공학과에 있었고, 2023년 4월 뇌인지과학과를 주 소속으로 옮겼다. 김재철AI대학원·데이터사이언스대학원·바이오및뇌공학과에서는 겸임 관계를 갖는다.[^news][^pi] 학과는 이상완을 부교수로 소개하며, 2026년 KAIST 지정 석좌교수 임용을 알렸다.[^bcs][^chair]

전문 분야는 뇌의 학습·추론을 설명하는 계산 모형과 뇌에서 착안한 인공지능이다. 학과 소개는 뇌기반 인공지능, 계산신경과학, 강화학습, 뇌-컴퓨터 인터페이스(뇌 신호와 기계 사이에서 정보를 전달하는 기술)를 연구 분야로 든다.[^bcs] 대표 논문에서 보면 여러 판단 체계를 조절하는 모형, 개인·사회 학습의 선택, 위험과 보상의 관계, 신경망 학습법과 생성 모형의 조절을 함께 다룬다.[^p1][^p2][^p3][^p4][^p6]

## 응용 분야

연구실은 뇌에서 착안한 인공지능과 인간 지능의 이해를 목표로 한다.[^intro] Microsoft Research Asia와는 인간·로봇 협력을 위한 가치 정렬(함께 행동하는 사람과 인공지능의 목표나 선호를 맞추는 과정)을 연구한다.[^news] 영상 생성 연구는 글에 따른 이미지 생성, 이미지의 일부 수정, 영상의 움직임 전달을 다룬다.[^p6][^p7] 학습 알고리즘 연구는 불확실한 환경의 학습 전략 선택, 새 자료에 대한 대응, 공격에 대한 신경망의 방어로 연결된다.[^p2][^p4][^security]

## 구성원

2026년 10월 31일 관측한 Lab members의 게시 항목이다. Postdoctoral scholars 구획 7명(그중 Research assistant professor 1명), Graduate students 20명과 Undergraduate students 구획의 2024–2026년 프로그램별 42행을 담았다. 학부 프로그램 표는 같은 사람이 여러 프로그램·연도에 등장할 수 있으며 현재 재학 인원 합계와 구별된다. 대학원생의 석사·박사 과정은 학력으로 추정하지 않는다.[^members]

| 이름 | 과정·게시 구획 | 게시 학력·공동지도 |
|---|---|---|
| MyoungHoon Ha | 박사후연구원 | PhD, Seoul National Univ |
| Minryung Song | 박사후연구원 | PhD, KAIST |
| Su Jin An | 박사후연구원 | PhD, KAIST |
| Jiewon Kang | 박사후연구원 | PhD, University of Oxford |
| Jaehoon Shin | 박사후연구원 | PhD, KAIST |
| Minsu Abel Yang | 박사후연구원 | PhD, KAIST |
| Yujin Cha | 연구조교수 | PhD, KAIST |
| Jun Yeol Kim | 대학원생 | BS in CS/BBE, KAIST; MS, KAIST |
| Young Ho Kang | 대학원생 | BS in CS, University of Manchester |
| Yoondo Sung | 대학원생 | BS in BBE, KAIST; MS, KAIST |
| Heejun Kim | 대학원생 | BS in EECS, GIST |
| Xu Xin | 대학원생 | BS in ME, Beijing Institute of Technology |
| Yeeun Ryoo | 대학원생 | BS in BBE, KAIST; MS in BBE, KAIST |
| Niklas Koeppe | 대학원생 | BS in AI, Radboud University |
| ELRHARBI-FLEURY Yannis | 대학원생 | BS in Math, University of Paris; MSc in AI, Sorbonne University |
| Jeongmin Seo | 대학원생 | BS in Biotech/AI, Yonsei University |
| Chamjin Joo | 대학원생 | BS in EE, KAIST |
| Phonlapee Lohajareekul | 대학원생 | BS in Math, Mahidol University |
| Younghoon Kim | 대학원생 | BS in BBE, KAIST; MD in Psychiatry, SNU |
| Junghyun Lee | 대학원생 | BS in Physics, SNU |
| JungYoon Nam | 대학원생 | BS in CS, KAIST |
| Soyeon Lee | 대학원생 | BS in EE, KAIST |
| Yuhwan Kim | 대학원생 | BS in Transdisciplinary Studies/Math, KAIST |
| Minseok Kang | 대학원생 | BS in EE, KAIST |
| Jung Young Kim | 대학원생 | BS in Physics, Kyunghee University co-supervisor: Ji Hyun Choi (KIST) |
| Xiaopeng Mao | 대학원생 | BS in BME, University of Copenhagen; MS, Technical University of Denmark co-supervisor: Sadasivan Puthusserypady (DTU) |
| Kyungyoon Jung | 대학원생 | BS in Biochem/Psych/AI, Yonsei University; co-supervisor: Juho Kim (KAIST) |
| Yeseul Seo | 2026 KAIST Individual study |  |
| SeokWon Han | 2026 KAIST Individual study |  |
| Junhyeok Yang | 2026 KAIST Individual study |  |
| Jonghoon Jeon | 2026 KAIST Individual study |  |
| Jaehyeon Lee | 2026 KAIST Individual study |  |
| Inkyoo Youn | 2026 KAIST Individual study |  |
| Dongyeong Kim | 2026 KAIST Individual study |  |
| Soyeon Lee | 2026 KAIST Individual study |  |
| Seongho Jo | 2026 KAIST Individual study |  |
| Lukas Bonkowski | 2026 Internship program (BCS, KAI-X, etc.) | Tech Univ Lubeck |
| Wallace Wang | 2026 Internship program (BCS, KAI-X, etc.) | Texas A&M |
| Heidi Lee | 2026 Internship program (BCS, KAI-X, etc.) | Princeton |
| Mobin Bagherian | 2026 Internship program (BCS, KAI-X, etc.) | Sharif University of Technology |
| Anjin Lee | 2026 Internship program (BCS, KAI-X, etc.) | Yonsei Univ College of Medicine |
| Junghyun Lee | 2025 Internship program (BCS, KAI-X, Campus Asia) | SNU |
| Nicolas Bosteels | 2025 Internship program (BCS, KAI-X, Campus Asia) | McGill |
| Hou Hei Lam | 2025 Internship program (BCS, KAI-X, Campus Asia) | Tsinghua |
| Soyeon Lee | 2025 URP |  |
| Minjoon Kim | 2025 URP |  |
| Jaeyong Shin | 2025 KAIST Individual study |  |
| JungYoon Nam | 2025 KAIST Individual study |  |
| Yoon-Seong Jeong | 2025 KAIST Individual study |  |
| JoonMyung Choi | 2025 KAIST Individual study |  |
| Yu hwan Kim | 2025 KAIST Individual study |  |
| Youngjin Cho | 2025 KAIST Individual study |  |
| Soyeon Lee | 2025 KAIST Individual study |  |
| Haein Lee | 2025 KAIST Individual study |  |
| Hyeong-geun Kim | 2024 Internship program | SNU |
| Jeffrey Kwon | 2024 Internship program | MIT |
| Jason Daniel Kurniawan | 2024 Internship program | National Taiwan University |
| Jaeyong Shin | 2024 KAIST Individual study |  |
| Minjun Kim | 2024 KAIST Individual study |  |
| Jae Kyoung Lee | 2024 KAIST Individual study |  |
| Haein Lee | 2024 KAIST Individual study |  |
| Soyeon Lee | 2024 KAIST Individual study |  |
| Jaeyong Shin | 2024 KAIST Individual study |  |
| Minseok Kang | 2024 KAIST Individual study |  |
| Chamjin Joo | 2024 KAIST Individual study |  |
| Kyunghyo Kim | 2024 KAIST Individual study |  |
| Elias Firisa | 2024 KAIST Individual study |  |
| Seokyung Kim | 2024 KAIST Individual study |  |
| Je Hyun Herh | 2024 KAIST Individual study |  |

## 졸업생과 이전 참여자

Alumni 구획 29행과 이전 방문·인턴·학부 연구 프로그램 102행이다. 학위와 방문·참여 구획, 연도, 진로는 연구실 표기를 따른다. 같은 이름의 반복 기재를 합치지 않은 게시 행 수이며, 과거 학부 프로그램 참여자를 모두 학위 졸업생으로 뜻하지 않는다. 연도가 적히지 않은 참여자는 연도를 비워 두었다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jungwon Ryu | Postdoc (‘19-‘25) | assistant professor at Sunmoon University |
| Geon Yeong Park | PhD; \*co-advisor: Jong Chul Ye (KAIST) (’25) |  |
| Su Jin An | PhD (’25) | postdoc at KAIST |
| Haram Joo | PhD (’25) | CEO at Leviosa AI |
| Juno Kim | PhD (’25) | research engineer at Samsung Research |
| Taekwan Kim | Postdoc (‘21-’24) | currently a postdoc at UCL |
| Changhwa Lee | PhD (’24) | research engineer at Samsung Research |
| Junghan Shin | PhD ; co-advisor: Sang Ah Lee in SNU (‘24) | currently a postdoc at SNU |
| Anil Yaman | Postdoc (‘20-’21) | currently an assistant professor at Vrije Universiteit Amsterdam, Netherlands |
| JeeHang Lee | Postdoc/Research assistant professor (‘16-’20) | currently an assistant professor at Sangmyung University, Seoul Campus |
| Fengkai Ke | Postdoc (‘17-’18) | currently at Hubei University of Technology |
| Yujin Cha | PhD (‘22) | currently an affiliated faculty at KAIST center for neuroscience-inspired AI |
| Dongjae Kim | PhD (‘21) | currently an assistant professor at Dankook University |
| Minryung Song | PhD (‘20) | currently a postdoc at KAIST |
| Sungyoung Kim | MS (‘26) |  |
| Wansoo Kim | MS (’ 25) |  |
| Youngha Cho | MS (‘25) |  |
| Nayeong Jeong | MS (‘25) |  |
| DoHyoung Lee | MS (‘25) |  |
| Sunghwa Ryu | MS (’24) |  |
| Jun Hyung Choi | MS ; MS researcher ‘22 (‘20) | currently an associate consultant at LG CNS Entrue Consulting |
| Myeong hyeon Kim | MS (‘22) | research engineer at Samsung Research |
| Shin Young Joo | MS (‘22) | currently Naver AI Lab |
| Suyeon Heo | MS (‘19) | currently at CHA university medical school |
| Jung Bae Park | MS (‘18) | currently a ML engineer at Bucketplace |
| Jihyea Lee | MS ('17) |  |
| Sang Hyun Yi | Researcher 17-18 | currently a graduate student at Caltech |
| Jun-Hyung Lee | Researcher; 18 |  |
| Mingoo Song | Researcher 18-19; jointly appointed at Prof. Sung-Hyon Myaeng's lab |  |
| Sukbin Lim | Visiting professor; Visiting professor ; NYU Shanghai (‘17) |  |
| Wooseok Jung | Internship; Oxford,  summer (‘20) |  |
| Younghoon Kim | Internship; SNU CM (‘18-’20) |  |
| DoHyun Kim | Internship; SNU (‘20) |  |
| Jin Yeob Chung | Internship; Oxford,  summer (‘18) |  |
| Junghan Shin | Internship; Postech,  winter (‘18) |  |
| Hyoung Jin Kim | Internship; SNU,  winter (‘17) |  |
| Minho Shin | Internship; DGIST,  summer (‘17) |  |
| Chloe Kwon | Internship; CMU,  summer (‘17) |  |
| Jonathan Chow | University of Waterloo co-op (‘20) |  |
| Namrata Sharma | University of Waterloo co-op (‘19) |  |
| Shuangyi Tong | University of Waterloo co-op; currently a graduate student at U Oxford (’18) |  |
| Cait Meredith | University of Leeds KISS program (‘19) |  |
| Charles Weston | University of Leeds KISS program (‘17) |  |
| Taek-Min Kim | KAIST Undergraduate dissertation (‘21) |  |
| Hyoungkyu Song | KAIST Undergraduate dissertation (‘19) |  |
| Suhyun Yang | KAIST Undergraduate dissertation (‘19) |  |
| Yoondo Sung | KAIST Undergraduate dissertation (‘18) |  |
| Yewon Kang | KAIST Undergraduate dissertation (‘18) |  |
| Seung-Wook Hwang | KAIST Undergraduate dissertation (‘18) |  |
| Enoch Kang | KAIST Undergraduate dissertation (‘17) |  |
| Jaehoon Shin | KAIST Undergraduate dissertation (‘17) |  |
| Ji Eun Lim | KAIST Undergraduate dissertation (‘17) |  |
| Yooju Shin | KAIST Undergraduate dissertation (‘17) |  |
| Jun Yeol Kim | KAIST Undergraduate dissertation (’16) |  |
| Juno Kim | KAIST Undergraduate dissertation (’16) |  |
| Minjun Kang | KAIST URP (‘22) |  |
| Jae Heon Lee | KAIST URP (‘21) |  |
| Gyubin Lee | KAIST URP (‘21) |  |
| Sanghwan Kim | KAIST URP (‘19) |  |
| Jeongseok Hwang | KAIST URP (‘19) |  |
| Jiseong Park | KAIST URP (‘19) |  |
| Geon Yeong Park | KAIST URP (‘18) |  |
| Lei Chen | KAIST URP (‘16) |  |
| Minjun Kang | KAIST Undergraduate Individual study (‘23) |  |
| Minseo Bang | KAIST Undergraduate Individual study (‘23) |  |
| Inhyeok Jeong | KAIST Undergraduate Individual study (‘23) |  |
| Junyup Kim | KAIST Undergraduate Individual study (‘23) |  |
| Khushi Parashar | KAIST Undergraduate Individual study (‘23) |  |
| Jaeyoung Shin | KAIST Undergraduate Individual study (‘23) |  |
| Dongyoon Hahm | KAIST Undergraduate Individual study (‘23) |  |
| Jimin Heo | KAIST Undergraduate Individual study (‘23) |  |
| Ye Gon Kim | KAIST Undergraduate Individual study (‘22) |  |
| Minjun Kang | KAIST Undergraduate Individual study (‘22) |  |
| Yena Choi | KAIST Undergraduate Individual study (‘22) |  |
| Inhyeok Jeong | KAIST Undergraduate Individual study (‘22) |  |
| Junyup Kim | KAIST Undergraduate Individual study (‘22) |  |
| Khushi Parashar | KAIST Undergraduate Individual study (‘22) |  |
| Yu hwan Kim | KAIST Undergraduate Individual study (‘22) |  |
| Ye Gon Kim | KAIST Undergraduate Individual study (‘21) |  |
| Inhyeok Jeong | KAIST Undergraduate Individual study |  |
| Seongho Keum | KAIST Undergraduate Individual study (‘21) |  |
| Minsik Kim | KAIST Undergraduate Individual study (‘21) |  |
| Minsu Abel Yang | KAIST Undergraduate Individual study (‘21) |  |
| Jae Heon Lee | KAIST Undergraduate Individual study (‘21) |  |
| Haeun Lee | KAIST Undergraduate Individual study (‘20) |  |
| Haram Kwon | KAIST Undergraduate Individual study (‘20) |  |
| Yujin Nam | KAIST Undergraduate Individual study (‘20) |  |
| Illia Churin | KAIST Undergraduate Individual study (‘20) |  |
| Minsu Abel Yang | KAIST Undergraduate Individual study (‘20) |  |
| Jae Heon Lee | KAIST Undergraduate Individual study (‘20) |  |
| Jisu Choi | KAIST Undergraduate Individual study (‘20) |  |
| Haeun Lee | KAIST Undergraduate Individual study (‘20) |  |
| YuJin Yang | KAIST Undergraduate Individual study (‘20) |  |
| Gyubin Lee | KAIST Undergraduate Individual study (‘20) |  |
| Jaeyeong Gim | KAIST Undergraduate Individual study (‘19) |  |
| Sangwoo Kim | KAIST Undergraduate Individual study (‘19) |  |
| Minsu Yang | KAIST Undergraduate Individual study (‘19) |  |
| Yuntae Kim | KAIST Undergraduate Individual study (‘19) |  |
| Tae Uk Ham | KAIST Undergraduate Individual study (‘19) |  |
| Hanung Lee | KAIST Undergraduate Individual study (‘19) |  |
| Abilmansur Zhumabekov | KAIST Undergraduate Individual study (‘19) |  |
| Chaeyoung Moon | KAIST Undergraduate Individual study (‘19) |  |
| Jiseong Park | KAIST Undergraduate Individual study (‘19) |  |
| Wanhee Cho | KAIST Undergraduate Individual study (‘19) |  |
| Woochan Lee | KAIST Undergraduate Individual study (‘19) |  |
| Jeongseok Hwang | KAIST Undergraduate Individual study (‘19) |  |
| Biniam Tamiru | KAIST Undergraduate Individual study (‘19) |  |
| Dong Seong Kim | KAIST Undergraduate Individual study (‘18) |  |
| Yewon Kang | KAIST Undergraduate Individual study (‘18) |  |
| Hyoung Kyu Song | KAIST Undergraduate Individual study (‘18) |  |
| Kyongwook Lee | KAIST Undergraduate Individual study (‘18) |  |
| Alisher Tortay | KAIST Undergraduate Individual study (‘18) |  |
| Manh Tuan Do | KAIST Undergraduate Individual study (‘18) |  |
| Haram Joo | KAIST Undergraduate Individual study (‘17) |  |
| Geon Yeong Park | KAIST Undergraduate Individual study (‘17) |  |
| Yoondo Sung | KAIST Undergraduate Individual study (‘17) |  |
| Min Seon Kim | KAIST Undergraduate Individual study (‘17) |  |
| Haeorm Park | KAIST Undergraduate Individual study (‘17) |  |
| Jaehoon Shin | KAIST Undergraduate Individual study (‘17) |  |
| Yewon Kang | KAIST Undergraduate Individual study (‘17) |  |
| Jun Yeol Kim | KAIST Undergraduate Individual study (‘16) |  |
| Jung Bae Park | KAIST Undergraduate Individual study (‘16) |  |
| Juno Kim | KAIST Undergraduate Individual study (‘16) |  |
| Kyungwook Lee | KAIST Undergraduate Individual study (‘16) |  |
| Yewon Kang | KAIST Undergraduate Individual study (‘16) |  |
| Geonwoo Kim | KAIST Undergraduate Individual study (‘16) |  |
| Geon Yeong Park | KAIST Undergraduate Individual study (‘16) |  |
| Ji Heon Lee | KAIST Undergraduate Individual study (‘16) |  |
| Geunchang Seong | KAIST Undergraduate Individual study (‘16) |  |
| Wonyong Kim | KAIST Undergraduate Individual study (‘16) |  |
| Jae Gwang Lee | KAIST Undergraduate Individual study (‘16) |  |

## 최근 논문 목록 (2021–2026)

뇌 모사 학습과 의사결정 계산 모형, 정상 세포·신경 회로의 작동 원리, 영상 생성·인식과 신경망 학습법을 다룬 목록이다. Journal의 20행과 Conference proceedings / posters의 42행을 담았다. 저자·제목·발표처와 연도는 연구실 표기이며, 같은 연구의 학술지·학회·워크숍 기재를 서로 다른 게시 항목으로 두었다. 학술지 목록의 Editorial과 Reviewed preprint는 그 종류를 표시했다. 연도만 적힌 2021년 항목은 해당 연도 구역을 따르고, 날짜가 확인된 항목은 2021년 10월 13일 이후를 기준으로 한다. 연구실이 accepted로 적은 Spectral motion alignment 항목은 채택으로 표시했다. NeurIPS 2026의 Rethinking credit assignment 항목은 연구실 기재로 표시했다.[^journal][^conference][^p1]

**2026**

- Xu X., Wang Y., Han D., Li D., Lee. S. W.\*. "Neural value alignment: human–AI collaboration under goal-action ambiguity". *IEEE Transactions on Cybernetics (2026). (Project summary & DEMO)*.
- C. Joo, M. H. Ha, S. W. Lee\*. "Rethinking credit assignment in cooperative MARL via interventional reward response". *Neural Information Processing Systems (NeurIPS), 2026 (연구실 기재)*.
- N. Koeppe, L. F. Vecchietti, D. Han, D. Li, S. W. Lee\*. "Mitigating plasticity loss through architectural design in continual learning". *International Conference on Machine Learning (ICML), 2026*.
- M. H. Ha, H. Kim+, Y. Sung+, Y. Jo, M. S. Kang, S. W. Lee\*. "Stable and scalable deep predictive coding networks with meta prediction errors". *International Conference on Learning Representations (ICLR), 2026*.

**2025**

- Sung Y, Rigotti M, Lee S. W.\*. "Factorized embedding of goal and uncertainty in the lateral prefrontal cortex guides stably flexible learning". *Nature Communications (2025)*.
- Kim J. Y., Lee S. W., Battaglia D., Choi J. H., and Yook S-H. "Optimal inhibitory-to-excitatory ratio governs slow and fast oscillations for enhanced neural communication". *Journal of Neuroscience (2025)*.
- Yang M. A.+, Kang S.+, Hong S. I.+, Lee J., Lee S. W.\*, Choi D. S.\*. "Astrocytes in the external globus pallidus selectively represent routine formation during repeated reward-seeking in mice". *eNeuro (2025)*.
- Yang M. A. Jung M. W., Lee S. W.\*. "Striatal arbitration between choice strategies guides few-shot adaptation". *Nature Communications (2025). (featured article in Editors’ Highlights)*.
- Mahajanauthor P., Tong S., Lee S. W., Seymour B. "Balancing safety and efficiency in human decision making". *eLife (2025). (Reviewed preprint) (Reviewed preprint)*.
- Y. Sung, M. Rigotti, S. W. Lee\*. "Factorized embedding of goal and uncertainty in the lateral prefrontal cortex guides stably flexible learning". *NeurIPS Workshop on the Symmetry and Geometry in Neural Representations (NeurReps), 2025*.
- G. Y. Park, S. W. Lee\*, Jong Chul Ye\*. "Inference-time diffusion model distillation". *Proceedings of International Conference on Computer Vision (ICCV), 2025*.
- S. J. An, C. Lee, S. W. Lee\*. "Deep neural experimenter: enhancing human one-shot inference through adaptive task design". *Multi-disciplinary Conference on Reinforcement Learning and Decision Making (RLDM), 2025. (Spotlight)*.
- H. Kim, N. Jeong, S. W. Lee\*. "Utilizing predictive representations for rapid, topology-aware reinforcement learning". *Multi-disciplinary Conference on Reinforcement Learning and Decision Making (RLDM), 2025*.
- X. Xu, Y. Wang, D. Han, D. Li, S. W. Lee\*. "Neural value alignment: decoding cortical prediction errors for flexible value alignment". *Multi-disciplinary Conference on Reinforcement Learning and Decision Making (RLDM), 2025*.
- J. Shin, Y. Sung, S. W. Lee\*. "Automated task design reveals modularity in reinforcement learning". *Multi-disciplinary Conference on Reinforcement Learning and Decision Making (RLDM), 2025*.
- Y. Ryoo, T. Kim, S. W. Lee\*. "Cognitive bias training through model parameter optimization". *Multi-disciplinary Conference on Reinforcement Learning and Decision Making (RLDM), 2025*.
- Y. Kim, H. Joo, S. W. Lee\*. "Optimal Markov decision tasks for simulating human reinforcement learning". *Multi-disciplinary Conference on Reinforcement Learning and Decision Making (RLDM), 2025*.
- Y. Ryoo, T. W. Kim, S. W. Lee\*. "Reshaping human cognitive processes through model parameter loss minimization". *Computational and Systems Neuroscience (COSYNE), 2025*.
- H. Kim, N. Jeong, S. W. Lee\*. "Topology-aware, unbiased grid coding for rapid task generalization". *Computational and Systems Neuroscience (COSYNE), 2025*.
- G. Y. Park+, H. Jeong+, S. W. Lee\*, Jong Chul Ye\*. "Spectral motion alignment for video motion transfer using diffusion models". *Proceedings of the 39th AAAI Conference on Artificial Intelligence (AAAI), 2025. (채택)*.

**2024**

- Lee C.-H. and Lee S. W.\*. "Transformation-based Data Synthesis for Limited Sample Scenario". *IEEE Access (2024)*.
- Song M. R. and Lee S. W.\*. "Rethinking dopamine-guided action sequence learning". *European Journal of Neuroscience (2024). (featured as the top 10% of most-viewed papers in 2024)*.
- Lee J. H., Heo S Y., Lee S. W.\*. "Controlling human causal inference through in-silico task design". *Cell Report (2024)*.
- J. Cheon, S. W. Lee, S. Paik\*. "Pretraining with random noise for fast and robust learning without weight transport". *Neural Information Processing Systems (NeurIPS), 2024*.
- G. Y. Park, C. Jung, S. Lee, J. C. Ye\*, S. W. Lee\*. "Self-supervised debiasing using low rank regularization". *IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2024*.
- M. H. Ha, S. Chi and S. W. Lee\*. "Learning to escape: multi-mode policy learning for the traveling salesmen problem". *IEEE International Conference on Evolving and Adaptive Intelligent Systems (EAIS), 2024*.
- H. Kim and S. W. Lee\*. "Robust and efficient grid code transformation for rapid task transfer". *Computational and Systems Neuroscience (COSYNE), 2024*.
- J. H. Shin and S. W. Lee\*. "Simulation-based behavioral profiling by model-guided task optimization and task-guided data generation". *Computational and Systems Neuroscience (COSYNE), 2024*.
- X. Xin and S. W. Lee\*. "Decoding human prediction errors for human-robot value alignment". *Proceedings of the 12th International Winter Conference on Brain-Computer Interface (IEEE BCI Winter), 2024. (oral presentation)*.
- S. Joo and S. W. Lee\*. "Learning Robust Goal Space with Hypothetical Analogy-Making". *arXiv (preprint), 2024*.

**2023**

- Kang Y. H., Khorasani A., Flint R., Farrokhi B., Lee S. W.\*. "Editorial: Neural Computations for Brain Machine Interface Applications". *Frontiers in Human Neuroscience (2023) (Editorial)*.
- Yaman A., Leibo J. Z., Iacca G., Lee S. W. "The emergence of division of labor through decentralized social sanctioning". *Proceedings of the Royal Society B: Biological Sciences (2023)*.
- Hwang S.-H., Park D., Paeng S., Lee S. W., Lee S.-H., Kim H. F. "Pneumatic tactile stimulus delivery system for studying brain responses evoked by active finger touch with fMRI". *Journal of Neuroscience Methods (2023)*.
- Baker M.+, Kang S.+, Hong S., Song M, Yang M, Peyton L, Essa H, Lee S. W., Choi DS. "External globus pallidus input to the dorsal striatum regulates habitual seeking behavior in male mice". *Nature Communications (2023)*.
- Kang S.+, Hong I.+, Kang S., Song M., Yang M. A., Essa H., Baker M., Lee J., Bruce R. A., Lee S. W., Choi DS. "Astrocyte activities in the external globus pallidus regulate action-selection strategies in reward-seeking behaviors". *Science Advances (2023)*.
- Kwon M., Lee S. W., Lee S.-H. "Hippocampal integration and separation processes with different temporal and spatial dynamics during learning for associative memory". *Human Brain Mapping (2023)*.
- G. Y. Park, J. Kim, B. Kim, S. W. Lee\* and J. C. Ye\*. "Energy-based cross attention for Bayesian context update in text-to-image diffusion models". *Neural Information Processing Systems (NeurIPS), 2023*.
- G. Y. Park, S. Lee, S. W. Lee\*, J. C. Ye\*. "Training debiased subnetworks with contrastive weight pruning". *IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2023*.

**2022**

- Lee J., Leibo J. Z., An S. J., Lee S. W.\*. "Importance of prefrontal meta control in human-like reinforcement learning". *Frontiers in Computational Neuroscience (2022)*.
- Yaman A.\*, Bredeche N., Caylak O., Leibo J., Lee S. W.\*. "Meta-control of social learning strategies". *PLOS Computational Biology (2022)*.
- J. Ryu and S. W. Lee\*. "Generalizable perceptual embedding with noise-tuning alignment". *The 31st Annual Computational Neuroscience Meeting (CNS), 2022*.
- H. Kim and S. W. Lee\*. "Hippocampal successor representation learning for zero-shot navigation". *Korean Artificial Intelligence Association Summer Conference, 2022*.
- S. J. An, B. D. Martino, and S. W. Lee\*. "How human metacognitive exploration improves reinforcement learning in a sparse reward environment". *Multi-disciplinary Conference on Reinforcement Learning and Decision Making (RLDM), 2022*.
- Y. Cha and S. W. Lee\*. "Information amplification in human-AI interactions via reinforcement learning". *Multi-disciplinary Conference on Reinforcement Learning and Decision Making (RLDM), 2022*.
- D. Kim, J. H. Lee, and S. W. Lee\*. "Exploring essential computations underlying generalizable human reinforcement learning". *Multi-disciplinary Conference on Reinforcement Learning and Decision Making (RLDM), 2022*.
- S. Joo and S. W. Lee\*. "Learning Robust Task Context with Hypothetical Analogy-Making". *International Conference on Learning Representations (ICLR) Workshop on Generalizable Policy Learning in the Physical World, 2022*.
- S. J. An and S. W. Lee\*. "Learning state-space uncertainty, but not value uncertainty, is sufficient for metacognitive exploration". *Cold Spring Harbor Laboratory meeting: From Neuroscience to Artificially Intelligent Systems (NAISys), 2022*.
- H. Chi, M. Ha, S. Chi, S. W. Lee, Q. Huang, and K. Ramani. "InfoGCN: Representation learning for human skeleton-based action recognition". *IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2022*.
- S. J. An, B. D. Martino, and S. W. Lee\*. "Rethinking Tolman's latent learning with metacognitive exploration". *Computational and Systems Neuroscience (COSYNE), 2022*.
- P. Mahajan, S. W. Lee, B. Seymour. "Balancing safety and efficiency in human decision-making". *Computational and Systems Neuroscience (COSYNE), 2022*.
- M. H. Kim. E. Jo, and S. W. Lee\*. "Goal-driven Atari environment". *Proceedings of the 10th International Winter Conference on Brain-Computer Interface (IEEE BCI Winter), 2022*.
- Y. H. Kang and S. W. Lee\*. "Meta-BCI: Perspectives on a role of self-supervised learning in meta brain computer interface". *Proceedings of the 10th International Winter Conference on Brain-Computer Interface (IEEE BCI Winter), 2022. (oral presentation)*.

**2021**

- Kim, D., Jeong J., Lee S. W.\*. "Prefrontal solution to the bias-variance tradeoff during reinforcement learning". *Cell Reports (2021)*.
- Kim J., Lee S. W., Yoon, S., Park H., Jeong B. "Neurocomputational mechanism of controllability inference under a multi-agent setting". *PLOS Computational Biology (2021)*.
- J. Seo and S. W. Lee\*. "Neural network-based intuitive physics for non-inertial reference frames". *IEEE Access (2021)*.
- H. Joo, I. Jeong, S. W. Lee\*. "Estimating the level of inference using an order-mimic agent". *Proceedings of Asian Conference on Pattern Recognition (ACPR), 2021*.
- G. Y. Park and S. W. Lee\*. "Reliably fast adversarial training via latent adversarial perturbation". *Proceedings of International Conference on Computer Vision (ICCV), 2021*.
- G. Y. Park and S. W. Lee\*. "Reliably fast adversarial training via latent adversarial perturbation". *Proceedings of International Conference on Learning Representations (ICLR) Workshop on Security and Safety in Machine Learning Systems, 2021*.
- G. Y. Park and S. W. Lee\*. "Information-theoretic regularization for multi-source domain adaptation". *Proceedings of International Conference on Computer Vision (ICCV), 2021*.
- S. J. An, B. D. Martino, and S. W. Lee\*. "Metacognition guides near-optimal exploration of a large state space with sparse rewards". *Computational and Systems Neuroscience (COSYNE), 2021*.
- Y-J. Cha, S. W. Lee\*. "Human uncertainty inference via deterministic ensemble neural networks". *Proceedings of the 35th AAAI Conference on Artificial Intelligence (AAAI), 2021*.
- D. Kim, M. H. Kim, S. W. Lee\*. "Decoding learning strategies from EEG signals provides generalizable features for decoding decision". *Proceedings of the 9th International Winter Conference on Brain-Computer Interface (IEEE BCI Winter), 2021*.

## 연구 과제와 지원

Research grants에서 2021년 10월 13일–2026년 10월 13일과 수행 기간이 겹치는 지원 11건, 연구실 소식의 ASTRA 연구비 수혜 1건이다. 기간과 역할은 연구실이 적은 표기다. ASTRA 항목의 날짜는 연구비 수혜 소식 날짜다.[^research][^news]

- Neural value alignment (지원 Microsoft Research Asia; 역할 PI; 기간 2023)
- System-3 level RL (지원 SW StarLab funded by the Ministry of Science and ICT, Korea; 역할 PI; 기간 2023 -)
- Brain-inspired AI (지원 Institute for Information & Communications Technology Promotion; 역할 PI; 기간 2019 - 2022)
- Development of metacognitive AI for rapid learning (지원 National Research Foundation of Korea; 역할 PI; 기간 2019-2023)
- phase II (지원 Samsung future technology foundation research grant; 역할 PI; 기간 2020 - 2023)
- Brain-like abstraction and reasoning engine (지원 KT; 역할 PI; 기간 2022 - 2024)
- Hippocampal transfer learning (지원 ETRI; 역할 Co-PI; 기간 2021 - 2025)
- Self-evolving HW intelligence (지원 AI Innovation Hub; 역할 Co-investigator; 기간 2021-2025)
- AI-based big data analysis technology for brain science (지원 NRF, Korea; 역할 Co-PI; 기간 2021 - 2023)
- Young researcher program (지원 National Research Foundation of Korea; 역할 PI; 기간 2017 - 2022)
- BCI (지원 Institute for Information & Communications Technology Promotion; 역할 co-PI; 기간 2017 - 2023)
- 2024-06-22 · Deep neural experimenter: closed-loop alignment of experimental design, brain model, and decoder for reading out executive control signals in working memory (지원 ASTRA research grant)

## 수상과 선정

2022–2025년 교수·연구실 구성원의 수상·선정 8건이다. 연도만 알려진 교수 수상은 연도로 표시한다.[^pi][^news]

- 2025-08-28 · Minsu Abel Yang: Institute for Promotion of Engineering and Science of Korea(IPESK)의 Next-Generation Engineer Prize
- 2025-01-24 · Heejun Kim: COSYNE Presenters Travel Grant
- 2025-01-24 · Yeeun Ryoo: COSYNE New Attendee Travel Grant
- 2023-02-27 · Yujin Cha: 세종과학펠로십 선정
- 2025 · Sang Wan Lee: KAIST Global Research Collaboration Award
- 2024 · Sang Wan Lee: KAIST Impact Research Award, College of Life Science and Bioengineering
- 2023 · Sang Wan Lee: KAIST Global Research Collaboration Award
- 2022 · Sang Wan Lee: KAIST International Cooperation Award

## 연구실 소식

2021년 12월 23일–2026년 10월 13일의 연구 발표·출판·협력·지원과 학술 행사 소식 22건이다. 날짜는 연구실 게시 날짜이며, 미래 행사에 관한 글은 발표나 참여 완료로 바꾸지 않았다.[^news]

- 2026-10-13 · 12월 8일 ELLIS UnConference의 Simulated vs. Unsimulated World Models 세션을 구성했다고 알렸다.
- 2026-05-21 · 학부 연구 참여자 9명이 연구실 미팅에서 연구 결과를 발표했다.
- 2025-11-26 · Yoondo Sung의 전전두피질 학습 연구가 Nature Communications에 출판됐다고 알렸다.
- 2025-10-28 · 연구실 기술이 KAIST Tech-Fair 2025에 소개됐다. 주제는 Deep neural experimenter다.
- 2025-07-30 / 2025-08-05 · 학부 연구 참여자 11명이 연구실 미팅에서 연구 결과를 발표했다.
- 2025-05-15 · Su Jin An의 논문이 RLDM 2025 Spotlight 발표로 선정됐다.
- 2025-02-21 · Minsu Abel Yang의 선조체 전략 선택 연구가 Nature Communications에 출판됐다고 알렸다.
- 2025-02-19 · 연구실 초록 8건이 RLDM 2025에 채택됐다고 알렸다.
- 2025-01-09 · 연구실 초록 2건이 COSYNE 2025에 채택됐다고 알렸다.
- 2024-10-30 · AI-human alignment 기술이 KAIST Tech-Fair 2024에 소개됐다.
- 2024-06-22 · 실험 설계·뇌 모형·해독기를 연결하는 Deep neural experimenter 과제의 ASTRA 연구비 수혜를 알렸다.
- 2024-01-18 · 연구실 초록 3건이 COSYNE 2024에 채택됐다고 알렸다.
- 2023-10-10 · Energy-Based Cross Attention for Bayesian Context Update in Text-to-Image Diffusion Models의 NeurIPS 2023 채택을 알렸다.
- 2023-08-31 · AI-human co-learning 기술이 KAIST Tech-Fair 2023에 소개됐다.
- 2023-06-07 · Microsoft Research Asia와 인간·로봇 협력을 위한 neural value alignment 공동 연구를 시작했다.
- 2023-04-24 · 과학기술정보통신부의 AI 분야 SW StarLab으로 선정됐다.
- 2023-04-01 · 연구실의 주 소속을 바이오및뇌공학과에서 뇌인지과학과로 옮겼으며, 바이오및뇌공학과·김재철AI대학원과 공동 임용 관계를 갖는다고 알렸다.
- 2023-01-25 · 연구실 초록 2건이 COSYNE 2023에 채택됐다고 알렸다.
- 2022-10-28 · Human-like AI design 기술이 KAIST Tech-Fair 2022에 소개됐다.
- 2022-06-12 · RLDM 2022에서 포스터 5건을 발표했다.
- 2022-02-01 · 연구실 초록 3건이 COSYNE 2022에 채택됐다고 알렸다.
- 2021-12-23 · BML 연례 심포지엄을 열었다.

## 연락과 위치

- 연구실 홈페이지: <https://aibrain.kaist.ac.kr/>
- 교수 연구실: KAIST W13, 402-6호[^bcs][^bbe]
- 교수 전화: 042-350-6514[^bcs][^bbe]
[^p1]: J. Kim 외, B. Jeong, PLOS Computational Biology 17, e1009549 (온라인 2021-11-09). <https://doi.org/10.1371/journal.pcbi.1009549> 초록 기준(출판사 논문 페이지). 초록 원문 <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009549> (관측 2026-11-01).

[^p2]: A. Yaman 외, S. W. Lee, PLOS Computational Biology 18, e1009882 (온라인 2022-02-28). <https://doi.org/10.1371/journal.pcbi.1009882> 초록 기준(출판사 논문 페이지). 초록 원문 <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009882> (관측 2026-11-01).

[^p3]: P. Mahajan, S. Tong, S. W. Lee, B. Seymour, eLife (Reviewed Preprint v2) (온라인 2025-06-12). <https://doi.org/10.7554/eLife.101371.2> 초록 기준(출판사 논문 페이지). 초록 원문 <https://elifesciences.org/reviewed-preprints/101371> (관측 2026-11-01).

[^p4]: J. Cheon, S. W. Lee, S.-B. Paik, Advances in Neural Information Processing Systems 37, 13748-13768 (2024). <https://doi.org/10.48550/arXiv.2405.16731> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2405.16731> (관측 2026-11-01).

[^p5]: G. Y. Park, S. Lee, S. W. Lee, J. C. Ye, arXiv (CVPR 2023 대응 판) (온라인 2022-10-11). <https://doi.org/10.48550/arXiv.2210.05247> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2210.05247> (관측 2026-11-01).

[^p6]: G. Y. Park 외, J. C. Ye, Advances in Neural Information Processing Systems 36 (2023). <https://doi.org/10.52202/075280-3339> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/f0878b7efa656b3bbd407c9248d13751-Abstract-Conference.html> (관측 2026-11-01).

[^p7]: G. Y. Park, H. Jeong, S. W. Lee, J. C. Ye, arXiv (AAAI 2025 대응 판) (온라인 2024-03-22). <https://doi.org/10.48550/arXiv.2403.15249> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2403.15249> (관측 2026-11-01).

[^p8]: G. Y. Park, S. W. Lee, J. C. Ye, arXiv (온라인 2024-12-12). <https://doi.org/10.48550/arXiv.2412.08871> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2412.08871> (관측 2026-11-01).

[^intro]: Lab Intro (English). <https://aibrain.kaist.ac.kr/about> (관측 2026-10-31).

[^research]: Research: Research topics, Research grants. <https://aibrain.kaist.ac.kr/research> (관측 2026-10-31).

[^pi]: Sang Wan Lee: Biosketch, Awards. <https://aibrain.kaist.ac.kr/sang-wan-lee> (관측 2026-10-31).

[^members]: Lab members: 현재 명단과 BML Alumni / past visitors. <https://aibrain.kaist.ac.kr/labmembers> (관측 2026-10-31).

[^journal]: Journal publications. *는 corresponding authors, +는 co-first authors로 정의한다.. <https://aibrain.kaist.ac.kr/journal> (관측 2026-10-31).

[^conference]: Conference proceedings / posters. <https://aibrain.kaist.ac.kr/proceedingconference> (관측 2026-10-31).

[^news]: Lab News. <https://aibrain.kaist.ac.kr/news> (관측 2026-10-31).

[^bcs]: KAIST 뇌인지과학과 전임교수: 이상완. <https://bcs.kaist.ac.kr/korean/sub030101/view/id/115> (관측 2026-11-01).

[^bbe]: KAIST 바이오및뇌공학과 교수진. <https://bioeng.kaist.ac.kr/index.php?category=8952&mid=bio_03_01> (관측 2026-11-01).

[^chair]: KAIST 뇌인지과학과, 「백세범 교수, 이상완 교수 KAIST 지정 석좌교수 임용」, 2026-03-04. <https://bcs.kaist.ac.kr/korean/sub0801/view/page/sub08/id/445> (관측 2026-11-01).

[^security]: G. Y. Park, S. W. Lee, 「Reliably fast adversarial training via latent adversarial perturbation」, arXiv:2104.01575. 초록 기준(arXiv 판). 초록은 신경망 내부 표현을 바꾸는 단일 단계 적대적 학습 방법과 공격 방어 성능을 서술한다. 초록 원문 <https://arxiv.org/abs/2104.01575> (관측 2026-11-01).

[^supp-j60]: Y. Sung, M. Rigotti, S. W. Lee, 「Factorized embedding of goal and uncertainty in the lateral prefrontal cortex guides stably flexible learning」, Nature Communications (2025). <https://doi.org/10.1038/s41467-025-66677-w> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/hbm.26319|10.1016/j.cobeha.2026.101672|10.1038/s41467-023-39545-8|10.1038/s41467-025-57049-5|10.1038/s41467-025-66677-w|10.1093/brain/awae102|10.1101/2025.06.22.660973|10.1111/ejn.16426|10.1126/sciadv.adh9239|10.1523/eneuro.0552-24.2025|10.21203/rs.3.rs-7117998/v1|10.2139/ssrn.3811830|10.31234/osf.io/ns6kq|10.32470/ccn.2023.1450-0> (관측 2026-11-01).

[^supp-j57]: M. A. Yang, M. W. Jung, S. W. Lee, 「Striatal arbitration between choice strategies guides few-shot adaptation」, Nature Communications (2025). <https://doi.org/10.1038/s41467-025-57049-5> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/hbm.26319|10.1016/j.cobeha.2026.101672|10.1038/s41467-023-39545-8|10.1038/s41467-025-57049-5|10.1038/s41467-025-66677-w|10.1093/brain/awae102|10.1101/2025.06.22.660973|10.1111/ejn.16426|10.1126/sciadv.adh9239|10.1523/eneuro.0552-24.2025|10.21203/rs.3.rs-7117998/v1|10.2139/ssrn.3811830|10.31234/osf.io/ns6kq|10.32470/ccn.2023.1450-0> (관측 2026-11-01).

[^supp-j42]: D. Kim, J. Jeong, S. W. Lee, 「Prefrontal solution to the bias-variance tradeoff during reinforcement learning」, Cell Reports (2021). <https://doi.org/10.1016/j.celrep.2021.110185> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=5&select=doi,title,publication_year,primary_location,type,abstract_inverted_index&filter=title.search:Prefrontal%20solution%20to%20the%20bias-variance%20tradeoff%20during%20reinforcement%20learning> (관측 2026-11-01).

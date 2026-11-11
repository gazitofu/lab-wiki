# Algorithmic General Intelligence Laboratory (AGI-LAB)

**KAIST 김재철AI대학원 · 신진우 교수**

- 분야: 범용 학습·추론 알고리즘, 로봇의 학습과 조작, 언어 모델과 에이전트, 영상·분자 생성, 학습 모델의 안전성과 개인정보 보호
- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 멀티모달 AI[^p1][^p6], 대형 언어 모델[^p2][^p3][^p4], 생성 인공지능[^prof][^p8], AI·기계학습 보안·프라이버시[^p3][^p7], 강화학습[^p1], 로봇 조작·파지[^prof]
- 홈페이지: <http://alinlab.kaist.ac.kr/>
- 근거와 출처: [AGI-LAB 근거 페이지](alinlab-sources.md)

> 자료와 계산을 효율적으로 쓰는 학습·추론 방법을 만들고, 이를 로봇의 행동, 언어 모델의 작업 수행, 영상 생성과 모델의 안전성으로 연결하는 연구실이다.[^topics][^prof]

## 무엇을 연구하나

AGI-LAB은 과학 계산(자연과학·공학 문제를 컴퓨터로 푸는 계산)에서 나오는 지능적인 알고리즘(문제를 풀기 위해 정해 놓은 계산 절차)을 이해하고 개발하는 것을 목표로 삼는다. 2015년부터는 기계학습(자료에서 규칙을 배워 예측이나 판단을 수행하는 방법)과 딥러닝(여러 층의 신경망을 통해 자료의 표현을 단계적으로 학습하는 기계학습 분야)에 주로 집중해 왔다. 신경망은 서로 연결된 계산 단위의 연결 강도를 학습하는 계산 모형이다. 연구 소개는 공통 목표를 자료·계산 효율과 폭넓은 활용을 갖춘 학습·추론 방법의 개발로 설명한다. 여기서 추론은 학습한 모형을 새 입력에 적용해 결과를 구하는 과정이다.[^home][^topics]

신진우 교수는 최근 연구의 중심을 물리적 환경에서 행동하는 인공지능(AI, Artificial Intelligence)과 에이전트(목표를 위해 주변 정보를 받아 판단하고 행동하는 시스템)에 두고 있다. 로봇이 물체를 잡고 다루는 방법, 사람의 자료에서 환경의 변화와 행동을 배우는 모형, 스스로 개선하는 에이전트, 계산을 효율적으로 수행하는 신경망 구조와 추론을 연구한다.[^prof] 대표 논문 Robot-R1은 장면 이미지와 전문가 시연에서 얻은 환경 정보를 받아 다음에 필요한 주요 지점의 상태를 예측하게 한다. 강화학습(행동의 결과로 받은 보상을 크게 하는 행동을 배우는 방법)으로 예측이 정확한 추론 응답을 강화해 로봇 제어에 필요한 추론을 학습한다.[^p1]

언어를 다루는 갈래에서는 대형 언어 모델(많은 언어 자료를 학습해 글을 이해하고 생성하는 큰 계산 모형)이 작업을 수행하고 학습하는 방법을 개발한다. MLE-STAR는 검색한 모형을 바탕으로 초기 코드를 만들고, 코드의 각 부분이 결과에 주는 영향을 분석해 특정 부분을 반복 개선한다.[^p2] OCTree(Optimizing Column feature generator with decision Tree reasoning)는 표 형태 자료의 예측에 쓸 특징(예측을 위해 자료에서 추출하거나 계산한 속성)을 언어 모델이 만들게 한다. 의사결정나무(속성에 대한 조건을 차례로 나누어 결과를 정하는 모형)로 이전 실험의 정보를 전달해 특징 생성 규칙을 개선한다.[^p4] 이미지와 글의 대응을 배우는 CLIP(Contrastive Language-Image Pre-training)을 학습하는 S-CLIP은 이미지와 설명문의 짝이 적은 상황에서 짝 없는 이미지도 활용해 모형을 학습하는 방법이다.[^p6]

생성 모형(학습한 자료에 나타나는 규칙을 이용해 새로운 자료를 만들어 내는 모형)과 안전성도 연구한다. 영상 생성에서는 영상의 공통 내용과 시간에 따른 움직임을 분리해 표현하고, 이를 각각 생성하는 방법을 제안했다.[^p8] 개인정보 보호에서는 글을 익명화(개인을 알아볼 수 있는 정보를 제거하거나 바꾸는 처리)하는 모델과 숨은 개인정보를 추정하는 모델의 상호작용을 학습 자료로 삼아, 작은 언어 모델이 스스로 익명화 결과를 개선하도록 한다.[^p3] 이미지 분류의 안전성에서는 입력을 교란하는 적대적 공격(모형이 잘못 판단하도록 입력을 의도적으로 바꾸는 행위)에 대해, 여러 크기의 잡음(자료에 섞여 원래 정보를 교란하는 불규칙한 성분)을 선택적으로 쓰는 방어 방법을 개발했다.[^p7] 원자(화학 반응으로 나눌 수 없는 원소의 기본 단위)들이 화학 결합으로 연결된 입자인 분자를 생성하는 연구에서는 원하는 화학적 특성을 향하도록 생성 과정을 유도하면서 생성 결과를 유지하는 알고리즘을 제안했다.[^p5]

## 주요 연구 주제

### 1. 로봇의 추론과 행동 학습

교수 소개는 로봇 학습과 조작, 사람의 자료에서 배우는 환경·행동 모형을 최근 연구 주제로 제시한다.[^prof] Robot-R1에서는 언어·영상 모형(Large Vision-Language Model)을 강화학습으로 훈련해, 현재 장면 이미지와 시연에서 얻은 환경 정보를 조건으로 과제 수행에 필요한 다음 주요 지점의 상태를 예측하게 하고, 그 예측이 정확한 응답을 강화한다.[^p1]

### 2. 언어 모델의 작업 수행과 자료 효율

MLE-STAR는 기계학습 코드를 자동으로 작성하는 에이전트다. 검색으로 과제에 맞는 모형을 찾아 초기 해법을 만들고, 코드 일부를 뺐을 때 결과가 어떻게 달라지는지 살펴 개선할 부분을 고른다.[^p2] OCTree는 언어 모델이 표의 새 특징을 만드는 규칙을 제안하고 이전 실험을 바탕으로 그 규칙을 고치게 한다. 이를 위해 의사결정나무로 실험 결과를 언어 형태로 전달한다.[^p4] S-CLIP은 소수의 이미지·설명문 쌍과 짝 없는 이미지로 영상·언어 모형을 학습해, 전문 분야의 자료를 다루는 방법을 제안한다.[^p6]

### 3. 영상과 분자의 생성

영상 생성 연구는 영상 전체를 큰 표현으로 한꺼번에 처리하는 대신 공통 내용을 담은 프레임(영상을 이루는 개별 이미지)과 움직임의 잠재 표현(자료를 변환해 얻은 내부 표현)을 나누어 만든다. 내용 쪽에는 미리 학습한 이미지 생성 모형을 조정해 쓰고, 움직임 쪽에는 새 경량 생성 모형을 학습한다.[^p8] 분자 생성 연구는 분자의 원하는 특성을 생성 과정에 반영하는 방법을 다룬다. 확산 모형(자료에 잡음을 더하는 과정의 역방향을 학습해 자료를 생성하는 모형)의 각 역방향 단계에서 유도 강도를 조절하고, 시간 보정으로 생성 결과를 유지하는 방식을 제안했다.[^p5]

### 4. 개인정보 보호와 적대적 공격 방어

익명화 연구는 문장에 드러나지 않은 개인 속성도 언어 모델이 추정할 수 있다는 위험을 다룬다. 익명화 모델과 추정 모델이 주고받은 결과로 작은 모델을 훈련하고, 그 모델이 익명화와 결과 평가를 반복하도록 한다.[^p3] 이미지 분류 연구에서는 잡음을 더한 입력들의 예측을 모으는 무작위 평활화(무작위로 바꾼 입력에 대한 예측을 결합해 판단의 안정성을 높이는 방법)를 여러 잡음 크기에서 선택적으로 적용한다. 이때 하나의 확산 모형으로 잡음을 제거하고, 원래 이미지를 복구할 수 있는지에 따라 학습 목표를 달리한다.[^p7]

## 대표 논문

KAIST 재직 시기의 논문 가운데 로봇 추론, 언어 모델·에이전트, 개인정보 보호, 표 자료 학습, 분자 생성, 영상·언어 학습, 공격 방어와 영상 생성을 고르게 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. 마지막 항목은 연구실 논문 목록이 연결한 arXiv 사전 공개본이다.[^pubs]

| 번호 | 연도 | 논문·발표처 | 주요 저자·교수 역할 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2025 | [Robot-R1: Reinforcement Learning for Enhanced Embodied Reasoning in Robotics](https://doi.org/10.52202/085713-5392) · NeurIPS | 1저자 Dongyoung Kim · 신진우 저자 참여 | 로봇이 다음에 맞춰야 할 주요 지점의 상태를 추론하게 하고, 정확한 예측으로 이어진 응답을 강화학습으로 보상한다. 로봇 제어를 위한 추론 과제에서 지도 미세조정(정답 예시를 이용해 이미 학습한 모형을 추가로 학습하는 방법) 방식보다 좋은 결과를 보였다.[^p1] |
| 2 | 2025 | [MLE-STAR: Machine Learning Engineering Agent via Search and Targeted Refinement](https://doi.org/10.52202/085713-3889) · NeurIPS | 1저자 Jaehyun Nam · 신진우 저자 참여 | 검색으로 과제에 맞는 모형을 찾아 초기 코드를 작성하고, 코드 각 부분의 영향을 분석해 특정 부분을 반복 개선한다. 기계학습 작업을 수행하는 에이전트를 만드는 방법이다.[^p2] |
| 3 | 2025 | [Self-Refining Language Model Anonymizers via Adversarial Distillation](https://doi.org/10.52202/085713-5520) · NeurIPS | 1저자 Kyuyoung Kim · 신진우 저자 참여 | 익명화한 글과 그 글에서 다시 추정한 개인 속성을 이용해 작은 언어 모델을 학습한다. 학습한 모델이 익명화와 평가를 반복해 결과를 개선하며, 실행 때 외부 모델에 의존하지 않게 한다.[^p3] |
| 4 | 2024 | [Optimized Feature Generation for Tabular Data via LLMs with Decision Tree Reasoning](https://doi.org/10.52202/079017-2932) · NeurIPS | 1저자 Jaehyun Nam · 신진우 저자 참여 | 표 자료에서 예측에 쓸 특징을 언어 모델이 만들게 한다. 의사결정나무로 이전 실험의 결과를 전달해 특징 생성 규칙을 반복 개선하며, 여러 예측 모형과 자료에서 효과를 보였다.[^p4] |
| 5 | 2024 | [Conditional Synthesis of 3D Molecules with Time Correction Sampler](https://doi.org/10.52202/079017-2417) · NeurIPS | 1저자 Hojung Jung · 신진우 저자 참여 | 원하는 화학적 특성으로 분자를 유도하면서 생성 결과를 유지하는 방법이다. 확산 과정의 각 역방향 단계에서 유도를 조절하는 시간 보정 방식을 제안했다.[^p5] |
| 6 | 2023 | [S-CLIP: Semi-supervised Vision-Language Learning using Few Specialist Captions](https://doi.org/10.52202/075280-2674) · NeurIPS | 1저자 Sangwoo Mo · 신진우 저자 참여 | 이미지와 설명문의 짝이 적은 전문 분야에서 짝 없는 이미지도 함께 활용한다. 설명문과 핵심어 수준의 두 가지 임시 학습 목표를 만들어 영상·언어 모형을 훈련한다.[^p6] |
| 7 | 2023 | [Multi-scale Diffusion Denoised Smoothing](https://doi.org/10.52202/075280-2945) · NeurIPS | 1저자 Jongheon Jeong · 신진우 저자 참여 | 이미지에서 잡음을 제거한 뒤 분류하는 방어 과정에 여러 잡음 크기를 선택적으로 적용한다. 확산 모형의 추가 학습을 결합해 분류 정확도와 수학적으로 보장할 수 있는 공격 저항성을 함께 다룬다.[^p7] |
| 8 | 2024 | [Efficient Video Diffusion Models via Content-Frame Motion-Latent Decomposition](https://doi.org/10.48550/arxiv.2403.14148) · arXiv 사전 공개본 | 1저자 Sihyun Yu · 신진우 저자 참여 | 영상의 공통 내용과 움직임을 분리해 표현한다. 내용에는 미리 학습한 이미지 생성 모형을 활용하고 움직임에는 별도의 가벼운 모형을 학습해, 영상 생성의 계산 부담을 줄였다.[^p8] |

## 교수와 전문 분야

신진우 교수는 2001년 서울대학교 수학·컴퓨터과학 학사 학위를, 2010년 Massachusetts Institute of Technology 수학 박사 학위를 받았다. Georgia Institute of Technology와 IBM T. J. Watson Research Center에서 박사후 연구를 수행한 뒤 2013년 가을 KAIST에 부임했다. 교수 소개는 김재철AI대학원과 전기및전자공학부에 공동 소속이라고 밝힌다.[^prof] 김재철AI대학원 전임교수 소개의 국문 직위는 「교수」다.[^gsai]

초기 전문 분야는 응용확률과 이론 컴퓨터과학이었고, KAIST 부임 후에는 기계학습의 알고리즘 기반, 생성 모형, 효율적인 학습·추론을 연구해 왔다. 현재는 로봇 학습과 물체 조작, 환경·행동 모형, 스스로 개선하는 에이전트와 효율적인 신경망 구조를 주요 연구로 소개한다.[^prof] 대표 논문에서는 로봇 제어용 추론, 기계학습 작업을 수행하는 에이전트, 개인정보 익명화, 영상 생성 알고리즘으로 이 전문성이 이어진다.[^p1][^p2][^p3][^p8]

## 응용 분야

연구실은 학습·추론 방법의 폭넓은 활용 분야로 컴퓨터 비전(사진·영상의 물체와 장면을 계산으로 이해하는 기술)과 자연어 처리(사람의 언어 자료를 계산으로 분석·이해·생성하는 방법)를 든다.[^topics] 대표 논문이 다루는 응용은 로봇 제어를 위한 공간·움직임 추론, 기계학습 작업의 코드 작성, 전문 분야의 이미지·글 공동 학습, 글의 개인정보 보호, 영상 생성, 목표 특성을 갖는 분자 설계다.[^p1][^p2][^p3][^p5][^p6][^p8] 분자 설계 논문은 신약 탐색과 재료과학에 기여할 가능성을 제시한다.[^p5]

## 구성원

구성원 페이지의 현재 연구 구성원 42명이다. 과정은 박사후연구원 3명, 박사과정 25명, 석사과정 14명이며 연구 주제와 공동지도 표기는 누리집 표기를 따른다. 「대표 논문 참여」의 숫자는 위 표의 번호이고, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Sihyun Yu | 박사후연구원 | World models | 8 |
| Kunwoong Kim | 박사후연구원 | Large language models and trustworthy AI |  |
| Junhoo Lee | 박사후연구원 | Large language models |  |
| Changyeon Kim | 박사과정 (co-advised by Prof. Kimin Lee ) | Deep RL and robotics |  |
| Woomin Song | 박사과정 | Large language models |  |
| Kyuyoung Kim | 박사과정 | Large language models | 3, 4 |
| Huiwon Jang | 박사과정 | Vision and robotics foundation models | 1 |
| June Suk Choi | 박사과정 (co-advised by Prof. Kimin Lee ) | Vision foundation models and diffusion models |  |
| Dongjun Lee | 박사과정 (co-advised by Prof. Kimin Lee ) | Agentic AI |  |
| Daewon Choi | 박사과정 | Large language models |  |
| Myungkyu Koo | 박사과정 | Robotics foundation models |  |
| Hyunseok Lee | 박사과정 | Agentic AI |  |
| Dongyoung Kim | 박사과정 | Robotics foundation models | 1 |
| Taeyoung Kim | 박사과정 | Robotics foundation models |  |
| Jeonghoon Kim | 박사과정 | Omni foundation models |  |
| Byungwoo Jeon | 박사과정 | Vision and robotics foundation models |  |
| Suhyeok Jang | 박사과정 | Robotics foundation models |  |
| Byungjun Yoon | 박사과정 | Robotics foundation models |  |
| Junbeom Kim | 박사과정 | Large language models |  |
| Hojin Jeon | 박사과정 | Robotics foundation models |  |
| John Won | 박사과정 | Robotics foundation models |  |
| Nayoung Oh | 박사과정 | Robotics foundation models |  |
| Seungjun Moon | 박사과정 | Robotics foundation models |  |
| Jimin Lee | 박사과정 |  |  |
| Beomjun Kim | 박사과정 |  |  |
| Hyunjun Jeon | 박사과정 |  | 3 |
| Yonghoon Dong | 박사과정 |  |  |
| Sanghyeok Lee | 박사과정 |  |  |
| Hyeonmo Kang | 석사과정 |  |  |
| Dongha Lim | 석사과정 |  |  |
| Seungku Kim | 석사과정 |  |  |
| Jonghoon Lee | 석사과정 |  |  |
| Wook Jung | 석사과정 |  |  |
| Seoyoung Choi | 석사과정 |  |  |
| Jungwoo Park | 석사과정 |  |  |
| Minha Lee | 석사과정 |  |  |
| Minseok Ko | 석사과정 |  |  |
| Junhyeong Park | 석사과정 |  |  |
| Junyoung Sung | 석사과정 |  |  |
| Jaewon Youm | 석사과정 |  |  |
| Jaehyuk Kim | 석사과정 |  |  |
| Seungyong Lee | 석사과정 |  |  |

## 졸업생과 이전 구성원

구성원 페이지의 Alumni 구획 40개 항목이다. 박사 24개, 석사 15개와 박사후연구원 경력 1개로, 학위·기간과 진로는 누리집 표기를 따른다. Academia와 Industry는 누리집의 구획이며 진로에는 여러 기관으로 이어진 경력이 함께 적혀 있다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Seong Hyeon Park | PhD (2026) | Assistant Professor@Ajou University |
| Jaehyung Kim | PhD (2024) | Postdoctoral Fellow@Carnegie Mellon University (hosted by Yiming Yang ) → Assistant Professor@Yonsei University |
| Jongheon Jeong | PhD (2024) | Assistant Professor@Korea University |
| Sangwoo Mo | PhD (2023) | Postdoctoral Fellow@University of Michigan, Ann Arbor (hosted by Stella X. Yu ) → Assistant Professor@POSTECH |
| Sukmin Yun | PhD (2023) | Postdoctoral Fellow@Mohamed bin Zayed University of Artificial Intelligence (hosted by Eric Xing ) → Assistant Professor@Hanyang University ERICA |
| Hankook Lee | PhD (2022) | LG AI Research → Assistant Professor@Sungkyunkwan University |
| Jaeho Lee | Postdoc (2019-2022) | Assistant Professor@POSTECH |
| Insu Han | PhD (2021) | Postdoctoral Fellow@Yale University (hosted by Amin Karbasi ) → Applied Scientist@Adobe Firefly → Assistant Professor@KAIST |
| Sungsoo Ahn | PhD (2021) | Postdoctoral Fellow@Mohamed bin Zayed University of Artificial Intelligence (hosted by Le Song ) → Assistant Professor@POSTECH → Assistant Professor@KAIST |
| Sejun Park | PhD (2020) | Postdoctoral Fellow@Vector Institute (hosted by Murat Erdogdu ) → Assistant Professor@Korea University |
| Kimin Lee | PhD (2020) | Postdoctoral Fellow@UC Berkeley (hosted by Pieter Abbeel ) → Google Research → Assistant Professor@KAIST |
| Tae-Hyun Oh | PhD, co-advised by In So Kweon  (2017) | Postdoctoral Fellow@MIT (hosted by Wojciech Matusik ) → Facebook AI Research → Associate Professor@POSTECH → Associate Professor@KAIST |
| Hyeryung Jang | PhD, co-advised by Yung Yi  (2017) | Postdoctoral Fellow@King's College London (hosted by Osvaldo Simeone ) → Assistant Professor@Dongguk University |
| Jungseul Ok | PhD, co-advised by Yung Yi  (2016) | Postdoctoral Fellow@KTH (hosted by Alexandre Proutiere ) → Postdoctoral Fellow@University of Washington (hosted by Sewoong Oh ) → Associate Professor@POSTECH |
| Sanghyuk Chun | MS (2016) | KAKAO → NAVER CLOVA AI Research → PhD Student@Princeton University (advised by Olga Russakovsky ) |
| Kyungmin Lee | PhD (2026) | Research Scientist@Google DeepMind |
| Insoo Kim | PhD (2026) | Research Scientist@NAVER Cloud |
| Jaehyun Nam | PhD (2026) | Research Scientist@Google Cloud AI |
| Subin Kim | PhD (2026) | Applied Scientist@Adobe Research |
| Jihoon Tack | PhD (2025) | Senior Researcher@Microsoft Research Redmond |
| Junsu Kim | PhD, co-advised by Prof. Kimin Lee  (2025) | Diden Robotics |
| Jongjin Park | PhD (2024) | Quant Researcher@Presto Labs |
| Kyunghwan Son | PhD, co-advised by Yung Yi  (2024) | Samsung Advanced Institute of Technology (SAIT) |
| Younggyo Seo | PhD (2023) | Research Scientist@Dyson Robot Learning Lab, London → Postdoctoral fellow@UC Berkeley (hosted by Pieter Abbeel ) → Applied Scientist@Amazon |
| Junhyun Nam | PhD (2022) | Samsung Advanced Institute of Technology (SAIT) |
| Donggyu Yun | PhD, co-advised by Yung Yi  (2016) | NAVER |
| Seunghyun Lee | MS (2026) | Hanwha Aerospace |
| Yisol Choi | MS (2025) | Doji |
| Seunghyuk Oh | MS (2025) | Furiosa AI |
| Seojin Kim | MS (2025) | JD Student@Law School, Seoul National University |
| Woohyuk Kim | MS (2025) |  |
| Sangkyung Kwak | MS (2025) | Research Engineer@General Robotics |
| Younghyun Kim | MS (2024) | Samsung Advanced Institute of Technology (SAIT) |
| Minkyu Kim | MS (2023) | KRAFTON |
| Hyunwoo Kang | MS (2022) | Hyperconnect |
| Chaewon Kim | MS (2022) | KRAFTON |
| Seunghyun Lee | MS (2021) | Diden Robotics |
| Hyuntak Cha | MS (2021) | Branch and Bound |
| Donggyu Lee | MS (2018) | LG |
| Kwihyuk Jin | MS (2017) | Qualcomm USA |

## 최근 논문 목록 (2021–2026)

연구실의 연도별 논문 목록 중 신진우 교수가 저자로 참여한 180개 게시 항목이다. 2026년 22개, 2025년 36개, 2024년 27개, 2023년 41개, 2022년 26개, 2021년 28개이며 학회·학술지·워크숍 논문과 기술 보고서를 함께 싣는다. 제목·저자·발표처는 연구실 표기를 따르며 별표는 동등 기여를 뜻한다. 동일 연구의 워크숍판과 후속 학회·학술지판은 별도 게시 항목으로 적혀 있다.[^pubs]

2026년 학회 항목에서 채택 소식이 있는 것은 「채택」으로 표시했다. 학회 출판판과 구분해 연구실이 연결한 arXiv의 DOI에는 「연결된 arXiv 사전 공개본」을 붙였으며, 연구실의 발표처 표기는 그대로 두었다. 「연구실 기재」는 누리집의 발표처·연도 표기다.[^pubs][^news]

**2026**

- Dongyoung Kim\*, Huiwon Jang\*, Myungkyu Koo\*, Suhyeok Jang\*, Taeyoung Kim\*, Beomjun Kim, Byungjun Yoon, Changsung Jang, Daewon Choi, Dongsu Han, Donguk Lee, Heeseung Kwon, Hojin Jeon, Jaehyun Kang, Jaekyoung Bae, Jihyuk Lee, Jimin Lee, John Won, Joonwoo Ahn, Junhyeong Park, Junyoung Sung, Kyungmin Lee, Minseong Han, Minsung Yoon, Sejune Joo, Seonil Son, Seungcheol Park, Seunggeun Cho, Seungjun Moon, Seungku Kim, Yonghoon Dong, Yongjin Cho, Youngchan Kim, Chang Hwan Kim, Dohyeon Kim, Heecheol Kim, Heewon Lee, Hensen Ahn, Hyungkyu Ryu, Hyunsoo Choi, Hyunsoo Shin, Jaeheon Jung, Jaewoo Kim, Jinwook Kim, Joochul Chang, Joonsoo Kim, Junghun Park, Jungwoo Park, Junho Cho, Junhyeok Park, Junwon Lee, Kangwook Lee, Kwanghoon Kim, Kyoungwhan Choe, Manoj Bhadu, Nayoung Oh, Sangjun Kim, Sangwoo Kim, Seunghoon Shim, Seunghyun Kim, Seungjun Lee, Seungyup Ka, Sungryol Yang, Wook Jung, Yashu Shukla, Yeonjae Lee, Yeonwoo Bae, Jinwoo Shin. "RLDX-1 Technical Report". *Technical Report ( TR ), 2026 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2605.03269*.
- Yonghoon Dong, Kyungmin Lee, Changyeon Kim, Jaehyuk Kim and Jinwoo Shin. "Trust Region Q Adjoint Matching". *Conference on Neural Information Processing Systems ( NeurIPS ), 2026 (채택) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2605.27079*.
- Jonghoon Lee\*, Seong Hyeon Park\*, Byungwoo Jeon, Minha Lee and Jinwoo Shin. "Pose6DAug: Physically Plausible Multi-view Object Swapping for Robot Data Augmentation". *Conference on Neural Information Processing Systems ( NeurIPS ), 2026 (채택) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2606.20118*.
- Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, Minsu Cho and Jinwoo Shin. "Latent Reasoning in Continuous Space for Unified Multimodal Models". *Conference on Neural Information Processing Systems ( NeurIPS ), 2026 (채택) · 연구실 기재*.
- Younghwan Kil, Joonhyeon Park, Giung Nam, Jinwoo Shin and Juho Lee. "Example-Based Spatial Guidance for Training-Free Concept Erasure in Diffusion Models". *Conference on Neural Information Processing Systems ( NeurIPS ), 2026 (채택) · 연구실 기재*.
- Woomin Song, Beomjun Kim, Daewon Choi, Sai Muralidhar Jayanthi, Saket Dingliwal, Jinwoo Shin and Aram Galstyan. "ExComm: Exploration-Stage Communication for Error-Resilient Agentic Test-Time Scaling". *Conference on Neural Information Processing Systems ( NeurIPS ), 2026 (채택) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2605.22102*.
- Hyunjun Jeon\*, Dongha Lim\*, Kunwoong Kim, Daewon Choi, Jinwoo Shin. "DoG: Sniffing Out Overconfidence in LLM Agents via Post-hoc Trajectory Restructuring". *Conference on Neural Information Processing Systems ( NeurIPS ), 2026 (채택) · 연구실 기재*.
- Jeonghoon Kim\*, Woojin Chung\*, Woomin Song, Cheonbok Park, Nako Sung, Jinwoo Shin. "A Simple Unigram Cross-Entropy Lens on the Lexical Imprint of Pre-training Data". *Conference on Neural Information Processing Systems ( NeurIPS ), 2026 (채택) · 연구실 기재*.
- Jimin Lee, Huiwon Jang, Myungkyu Koo, Jungwoo Park and Jinwoo Shin. "Modular Sensory Stream for Integrating Physical Feedback in Vision-Language-Action Models". *Conference on Robot Learning ( CoRL ), 2026 (채택) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2604.23272*.
- Kyuyoung Kim, Kevin Wang, Yunfei Xie, Peiyang Xu, Peiyao Sheng, Chen Wei, Zhangyang Wang, Jinwoo Shin, Pramod Viswanath, Sewoong Oh. "Correct Answers from Sound Reasoning: Verifiable Process Supervision for Language Models". *Conference on Language Modeling ( COLM ), 2026 (채택) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2605.12519*.
- Byungwoo Jeon\*, Dongyoung Kim\*, Huiwon Jang, Insoo Kim and Jinwoo Shin. "SpatialBoost: Enhancing Visual Representation through Language-Guided Reasoning". *European Conference on Computer Vision ( ECCV ), 2026 (채택) · DOI: 10.1007/978-3-032-37393-9_23*.
- Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, Minsu Cho and Jinwoo Shin. "Vision-aligned Latent Reasoning for Multi-Modal Large Language Model". *International Conference on Machine Learning ( ICML ), 2026 (채택) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2602.04476*.
- John Won, Kyungmin Lee, Huiwon Jang, Dongyoung Kim and Jinwoo Shin. "Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model". *International Conference on Machine Learning ( ICML ), 2026 (채택) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2510.27607*.
- Taeyoung Kim, Jimin Lee, Myungkyu Koo, Dongyoung Kim, Kyungmin Lee, Changyeon Kim, Younggyo Seo and Jinwoo Shin. "Contrastive Representation Regularization for Vision-Language-Action Models". *International Conference on Machine Learning ( ICML ), 2026 (채택) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2510.01711*.
- Subin Kim, Sangwoo Mo, Mamshad Nayeem Rizve, Yiran Xu, Difan Liu, Jinwoo Shin and Tobias Hinz. "Rethinking Prompt Design for Inference-time Scaling in Text-to-Visual Generation". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2026 (채택) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2512.03534*.
- June Suk Choi, Kyungmin Lee, Sihyun Yu, Yisol Choi, Jinwoo Shin and Kimin Lee. "Improving Motion in Image-to-Video Models via Adaptive Low-Pass Guidance". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2026 (채택) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2506.08456*.
- Suhyeok Jang, Dongyoung Kim, Changyeon Kim, Youngsuk Kim and Jinwoo Shin. "Verifier-free Test-Time Sampling for Vision Language Action Models". *International Conference on Learning Representations ( ICLR ), 2026 (채택) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2510.05681*.
- Hyunjun Jeon, Kyuyoung Kim and Jinwoo Shin. "RedacBench: Can AI Erase Your Secrets?". *International Conference on Learning Representations ( ICLR ), 2026 (채택) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2603.20208*.
- Myungkyu Koo\*, Daewon Choi\*, Taeyoung Kim, Kyungmin Lee, Changyeon Kim, Younggyo Seo and Jinwoo Shin. "HAMLET: Switch Your Vision-Language-Action Model into a History-Aware Policy". *International Conference on Learning Representations ( ICLR ), 2026 (채택) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2510.00695*.
- Kyungmin Lee, Sihyun Yu and Jinwoo Shin. "Decoupled MeanFlow: Turning Flow Models into Flow Maps for Accelerated Sampling". *International Conference on Learning Representations ( ICLR ), 2026 (채택) · 연구실 기재*.
- Jaehyun Nam, Jinsung Yoon, Jiefeng Chen, Rajarishi Sinha, Jinwoo Shin and Tomas Pfister. "DS-STAR: Data Science Agent for Solving Diverse Tasks across Heterogeneous Formats and Open-Ended Queries". *Transactions on Machine Learning Research ( TMLR ), 2026*.
- Sihyun Yu†\*, Nanye Ma†\*, Pinzhi Huang†\*, Hyunseok Lee\*, Shusheng Yang, June Suk Choi, Ellis Brown, Oscar Michel, Boyang Zheng, Jinwoo Shin, Saining Xie. "Benchmarking Visual State Tracking in Multimodal Video Understanding". *NeurIPS Workshop on VLM4RWD, 2026 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2606.03920*.

**2025**

- Seong Hyeon Park and Jinwoo Shin. "Track3R: Joint Point Map and Trajectory Prior for Spatiotemporal 3D Understanding". *Conference on Neural Information Processing Systems ( NeurIPS ), 2025 · DOI: 10.52202/085713-5536*.
- Kyuyoung Kim, Hyunjun Jeon and Jinwoo Shin. "Self-Refining Language Model Anonymizers via Adversarial Distillation". *Conference on Neural Information Processing Systems ( NeurIPS ), 2025 · DOI: 10.52202/085713-5520*.
- Dongyoung Kim, Huiwon Jang, Sumin Park, Jaehyung Kim, Younggyo Seo and Jinwoo Shin. "Robot-R1: Reinforcement Learning for Enhanced Embodied Reasoning in Robotics". *Conference on Neural Information Processing Systems ( NeurIPS ), 2025 · DOI: 10.52202/085713-5392*.
- Jaehyun Nam, Jinsung Yoon, Jiefeng Chen, Jinwoo Shin, Sercan O Arik and Tomas Pfister. "MLE-STAR: Machine Learning Engineering Agent via Search and Targeted Refinement". *Conference on Neural Information Processing Systems ( NeurIPS ), 2025 · DOI: 10.52202/085713-3889*.
- Woomin Song, Sai Muralidhar Jayanthi, Srikanth Ronanki, Kanthashree Mysore Sathyendra, Jinwoo Shin, Aram Galstyan, Shubham Katiyar and Sravan Babu Bodapati. "Compress, Gather, and Recompute: REFORMing Long-Context Processing in Transformers". *Conference on Neural Information Processing Systems ( NeurIPS ), 2025 · DOI: 10.52202/085713-3353*.
- Seojin Kim\*, Hyeontae Song\*, Jaehyun Nam and Jinwoo Shin. "Training Text-to-Molecule Models with Context-Aware Tokenization". *Conference on Empirical Methods in Natural Language Processing ( EMNLP ), 2025 (findings) · DOI: 10.48448/h9c9-sy36*.
- Daewon Choi, Jimin Lee, Jihoon Tack, Woomin Song, Saket Dingliwal, Sai Muralidhar Jayanthi, Bhavana Ganesh, Jinwoo Shin, Aram Galstyan and Sravan Babu Bodapati. "Think Clearly: Improving Reasoning via Redundant Token Pruning". *Conference on Empirical Methods in Natural Language Processing ( EMNLP ), 2025 (findings) · DOI: 10.48448/05rm-xh79*.
- Kyuyoung Kim, Jinwoo Shin and Jaehyung Kim. "Personalized Language Models via Privacy-Preserving Evolutionary Model Merging". *Conference on Empirical Methods in Natural Language Processing ( EMNLP ), 2025 · DOI: 10.48448/6n24-8k40*.
- Daewon Choi, Seunghyuk Oh, Saket Dingliwal, Jihoon Tack, Kyuyoung Kim, Woomin Song, Seojin Kim, Insu Han, Jinwoo Shin, Aram Galstyan, Shubham Katiyar and Sravan Babu Bodapati. "Mamba Drafters for Speculative Decoding". *Conference on Empirical Methods in Natural Language Processing ( EMNLP ), 2025 (findings) · DOI: 10.48448/mf0r-1c02*.
- Woomin Song, Saket Dingliwal, Sai Muralidhar Jayanthi, Bhavana Ganesh, Jinwoo Shin, Aram Galstyan and Sravan Babu Bodapati. "Accelerated Test-Time Scaling with Model-Free Speculative Sampling". *Conference on Empirical Methods in Natural Language Processing ( EMNLP ), 2025 (based on the preliminary version [W54] ) · DOI: 10.48448/n591-kj35*.
- Taeckyung Lee, Sorn Chottananurak, Junsu Kim, Jinwoo Shin, Taesik Gong and Sung-Ju Lee. "Test-Time Adaptation with Binary Feedback". *International Conference on Machine Learning ( ICML ), 2025 · 연구실 기재*.
- Hyunseok Lee\*, Seunghyuk Oh\*, Jaehyung Kim, Jinwoo Shin and Jihoon Tack. "ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification". *International Conference on Machine Learning ( ICML ), 2025 · 연구실 기재*.
- Jongin Lim, Sucheol Lee, Daeho Um, Sung-Un Park and Jinwoo Shin. "PRIME: Deep Imbalanced Regression with Proxies". *International Conference on Machine Learning ( ICML ), 2025 · 연구실 기재*.
- Jeonghoon Kim, Byeongchan Lee, Cheonbok Park, Yeontaek Oh, Beomjun Kim, Taehwan Yoo, Seongjin Shin, Dongyoon Han, Jinwoo Shin and Kang Min Yoo. "Peri-LN: Revisiting Layer Normalization in the Transformer Architecture". *International Conference on Machine Learning ( ICML ), 2025 · 연구실 기재*.
- Younghyun Kim\*, Jongheon Jeong\*, Sangkyung Kwak, Kyungmin Lee, Juho Lee and Jinwoo Shin. "StarFT: Robust Fine-tuning of Zero-shot Models via Spuriosity Alignment". *International Joint Conference on Artificial Intelligence ( IJCAI ), 2025 · DOI: 10.24963/ijcai.2025/616*.
- Dongyoung Kim, Jinsung Yoon, Jinwoo Shin and Jaehyung Kim. "Debiasing Online Preference Learning via Preference Feature Preservation". *Annual Meeting of the Association for Computational Linguistics ( ACL ), 2025 (findings) · DOI: 10.18653/v1/2025.findings-acl.1034*.
- Huiwon Jang, Sihyun Yu, Jinwoo Shin, Pieter Abbeel and Younggyo Seo. "Efficient Long Video Tokenization via Coordinated-based Patch Reconstruction". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2025 · 연구실 기재*.
- Jian Meng, Ahmed Hasssan, Li Yang, Deliang Fan, Jinwoo Shin and Jae-sun Seo. "Closest Neighbors are Harmful for Lightweight Masked Auto-encoders". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2025 · DOI: 10.1109/cvpr52734.2025.02349*.
- Kyungmin Lee, Xiaohang Li, Qifei Wang, Junfeng He, Junjie Ke, Ming-Hsuan Yang, Irfan Essa, Jinwoo Shin, Feng Yang and Yinxiao Li. "Calibrated Multi-Preference Optimization for Aligning Diffusion Models". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2025 · DOI: 10.1109/cvpr52734.2025.01721*.
- Yisol Choi, Sangkyung Kwak, Sihyun Yu, Hyungwon Choi and Jinwoo Shin. "Controllable Human Image Generation with Personalized Multi-Garments". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2025 · DOI: 10.1109/cvpr52734.2025.02676*.
- Dongyoung Kim, Kimin Lee, Jinwoo Shin and Jaehyung Kim. "Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment". *International Conference on Learning Representations ( ICLR ), 2025 · 연구실 기재*.
- Changyeon Kim, Minho Heo, Doohyun Lee, Honglak Lee, Jinwoo Shin, Joseph J Lim^, Kimin Lee^. "Subtask-Aware Visual Reward Learning from Segmented Demonstrations". *International Conference on Learning Representations ( ICLR ), 2025 · 연구실 기재*.
- Sihyun Yu, Sangkyung Kwak, Huiwon Jang, Jongheon Jeong, Jonathan Huang, Jinwoo Shin^ and Saining Xie^. "Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think". *International Conference on Learning Representations ( ICLR ), 2025 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2410.06940*.
- Dongjun Lee, Juyong Lee, Kyuyoung Kim, Jihoon Tack, Jinwoo Shin, Yee Whye Teh and Kimin Lee. "Learning to Contextualize Web Pages for Enhanced Decision Making by LLM Agents". *International Conference on Learning Representations ( ICLR ), 2025 · 연구실 기재*.
- June Suk Choi, Kyungmin Lee, Jongheon Jeong, Saining Xie, Jinwoo Shin and Kimin Lee. "DiffusionGuard: A Robust Defense Against Malicious Diffusion-based Image Editing". *International Conference on Learning Representations ( ICLR ), 2025 (based on the preliminary version [W50] ) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2410.05694*.
- Insoo Kim, Hana Lee, Hyong-Euk Lee and Jinwoo Shin. "Controllable Blur Data Augmentation Using 3D-Aware Motion Estimation". *International Conference on Learning Representations ( ICLR ), 2025 · 연구실 기재*.
- Byeongchan Lee, John Won, Seunghyun Lee and Jinwoo Shin. "CLIP Meets Diffusion: A Synergistic Approach to Anomaly Detection". *Transactions on Machine Learning Research ( TMLR ), 2025*.
- Insoo Kim, Geonseok Seo, Hyong-Euk Lee and Jinwoo Shin. "RefDeblur: Blind Motion Deblurring with Self-Generated Reference Image". *Transactions on Machine Learning Research ( TMLR ), 2025*.
- Woomin Song, Jihoon Tack, Sangwoo Mo, Seunghyuk Oh and Jinwoo Shin. "Sparsified State-Space Models are Efficient Highway Networks". *Transactions on Machine Learning Research ( TMLR ), 2025 (based on the preliminary version [W51] )*.
- Honggu Kang, Seohyeon Cha, Jinwoo Shin, Jongmyeong Lee and Joonhyuk Kang. "NeFL: Nested Model Scaling for Federated Learning with System Heterogeneous Clients". *IEEE Transactions on Mobile Computing ( TMC ), 2025 (accepted to appear) · DOI: 10.1109/tmc.2025.3549600*.
- Subin Kim Kim, Seoung Wug Oh, Wang. Jui-Hsien, Joon-Young Lee and Jinwoo Shin. "Tuning-Free Multi-Event Long Video Generation via Synchronized Coupled Sampling". *ICCV Workshop on the Findings, 2025 · DOI: 10.1109/iccvw69036.2025.00671*.
- Daewon Choi, Jimin Lee, Jihoon Tack, Woomin Song, Saket Dingliwal, Sai Muralidhar Jayanthi, Bhavana Ganesh, Jinwoo Shin, Aram Galstyan and Sravan Babu Bodapati. "Think Clearly: Improving Reasoning via Redundant Token Pruning". *ICML Workshop on Efficient Systems for Foundation Models III, 2025 · DOI: 10.48448/05rm-xh79*.
- Daewon Choi, Seunghyuk Oh, Saket Dingliwal, Jihoon Tack, Kyuyoung Kim, Woomin Song, Seojin Kim, Insu Han, Jinwoo Shin, Aram Galstyan, Shubham Katiyar and Sravan Babu Bodapati. "Mamba Drafters for Speculative Decoding". *ICML Workshop on Efficient Systems for Foundation Models III, 2025 · DOI: 10.48448/mf0r-1c02*.
- Woomin Song, Sai Muralidhar Jayanthi, Srikanth Ronanki, Kanthashree Mysore Sathyendra, Jinwoo Shin, Aram Galstyan, Shubham Katiyar and Sravan Babu Bodapati. "Compress, Gather, and Recompute: REFORMing Long-Context Processing in Transformers". *ICML Workshop on Efficient Systems for Foundation Models III, 2025 · DOI: 10.52202/085713-3353*.
- Woomin Song, Saket Dingliwal, Sai Muralidhar Jayanthi, Bhavana Ganesh, Jinwoo Shin, Aram Galstyan and Sravan Babu Bodapati. "Accelerated Test-Time Scaling with Model-Free Speculative Sampling". *ICML Workshop on Efficient Systems for Foundation Models III, 2025 (the newer version [C199] available at EMNLP 2025) · DOI: 10.48448/n591-kj35*.
- Sihyun Yu, Meera Hahn, Dan Kondratyuk, Jinwoo Shin, Agrim Gupta, Jose Lezama, Irfan Essa, David A Ross and Jonathan Huang. "MALT Diffusion: Memory-Augmented Latent Transformers for Any-Length Video Generation". *CVPR Workshop on AI for Content Creation, 2025 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2502.12632*.

**2024**

- Seong Hyeon Park, Huiwon Jang, Byungwoo Jeon, Sukmin Yun, Paul Hongsuck Seo and Jinwoo Shin. "TrackIME: Enhanced Video Point Tracking via Instance Motion Estimation". *Conference on Neural Information Processing Systems ( NeurIPS ), 2024 · DOI: 10.52202/079017-2143*.
- Hyunseok Lee\*, Jihoon Tack\* and Jinwoo Shin. "ReMoDetect: Reward Models Recognize Aligned LLM's Generations". *Conference on Neural Information Processing Systems ( NeurIPS ), 2024 · DOI: 10.52202/079017-0095*.
- Jihoon Tack, Jaehyung Kim, Eric Mitchell, Jinwoo Shin, Yee Whye Teh and Jonathan Richard Schwarz. "Online Adaptation of Language Models with a Memory of Amortized Contexts". *Conference on Neural Information Processing Systems ( NeurIPS ), 2024 · DOI: 10.52202/079017-4134*.
- Jaehyun Nam\*, Kyuyoung Kim\*, Seunghyuk Oh, Jihoon Tack, Jaehyung Kim and Jinwoo Shin. "Optimized Feature Generation for Tabular Data via LLMs with Decision Tree Reasoning". *Conference on Neural Information Processing Systems ( NeurIPS ), 2024 · DOI: 10.52202/079017-2932*.
- Kyungmin Lee, Sangkyung Kwak, Kihyuk Sohn and Jinwoo Shin. "Direct Consistency Optimization for Robust Customization of Text-to-Image Diffusion models". *Conference on Neural Information Processing Systems ( NeurIPS ), 2024 · DOI: 10.52202/079017-3281*.
- Hojung Jung, Youngrok Park, Laura Schmid, Jaehyeong Jo, Dongkyu Lee, Bongsang Kim, Se-Young Yun and Jinwoo Shin. "Conditional Synthesis of 3D Molecules with Time Correction Sampler". *Conference on Neural Information Processing Systems ( NeurIPS ), 2024 · DOI: 10.52202/079017-2417*.
- Kyuyoung Kim, Ah Jeong Seo, Hao Liu, Jinwoo Shin and Kimin Lee. "Margin Matching Preference Optimization: Enhanced Model Alignment with Granular Feedback". *Conference on Empirical Methods in Natural Language Processing ( EMNLP ), 2024 (findings) · DOI: 10.18653/v1/2024.findings-emnlp.792*.
- Sanghyun Kim, Seohyeon Jung, Balhae Kim, Moonseok Choi, Jinwoo Shin and Juho Lee. "Safeguard Text-to-Image Diffusion Models with Human Feedback Inversion". *European Conference on Computer Vision ( ECCV ), 2024 · DOI: 10.1007/978-3-031-72855-6_8*.
- Yisol Choi, Sangkyung Kwak, Kyungmin Lee, Hyungwon Choi and Jinwoo Shin. "Improving Diffusion Models for Authentic Virtual Try-on in the Wild". *European Conference on Computer Vision ( ECCV ), 2024 · DOI: 10.1007/978-3-031-73016-0_13*.
- Daewon Choi\*, Jongheon Jeong\*, Huiwon Jang, Jinwoo Shin. "Adversarial Robustification via Text-to-Image Diffusion Models". *European Conference on Computer Vision ( ECCV ), 2024 · DOI: 10.1007/978-3-031-73004-7_10*.
- Jaehyun Nam, Woomin Song, Seong Hyeon Park, Jihoon Tack, Sukmin Yun, Jaehyung Kim, Kyu Hwan Oh, and Jinwoo Shin. "Tabular Transfer Learning via Prompting LLMs". *Conference on Language Modeling ( COLM ), 2024 (based on the preliminary version [W43] ) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2408.11063*.
- Huiwon Jang, Dongyoung Kim, Junsu Kim, Jinwoo Shin, Pieter Abbeel, Younggyo Seo. "Visual Representation Learning with Stochastic Frame Prediction". *International Conference on Machine Learning ( ICML ), 2024 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2406.07398*.
- Seojin Kim, Jaehyun Nam, Sihyun Yu, Younghoon Shin, Jinwoo Shin. "Data-Efficient Molecular Generation with Hierarchical Textual Inversion". *International Conference on Machine Learning ( ICML ), 2024 (based on the preliminary version [W48] ) · 연구실 기재*.
- Insoo Kim, Jae Seok Choi, Geonseok Seo, Kinam Kwon, Jinwoo Shin and Hyong-Euk Lee. "Real-World Efficient Blind Motion Deblurring via Blur Pixel Discretization". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2024 · 연구실 기재*.
- Younghyun Kim\*, Sangwoo Mo\*, Minkyu Kim, Kyungmin Lee, Jaeho Lee and Jinwoo Shin. "Discovering and Mitigating Visual Biases through Keyword Explanation". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2024 (based on the preliminary version [W45] ) · DOI: 10.1109/cvpr52733.2024.01054*.
- Jaehyung Kim, Jaehyun Nam, Sangwoo Mo, Jongjin Park, Sang-Woo Lee, Minjoon Seo, Jung-Woo Ha and Jinwoo Shin. "SuRe: Improving Open-domain Question Answering of LLMs via Summarized Retrieval". *International Conference on Learning Representations ( ICLR ), 2024 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2404.13081*.
- Seong Jin Cho, Gwangsu Kim, Junghyun Lee, Jinwoo Shin and Chang D. Yoo. "Querying Easily Flip-flopped Samples for Deep Active Learning". *International Conference on Learning Representations ( ICLR ), 2024 · 연구실 기재*.
- Woomin Song\*, Seunghyuk Oh\*, Sangwoo Mo, Jaehyung Kim, Sukmin Yun, Jung-Woo Ha, and Jinwoo Shin. "Hierarchical Context Merging: Better Long Context Understanding for Pre-trained LLMs". *International Conference on Learning Representations ( ICLR ), 2024 · 연구실 기재*.
- Sihyun Yu, Weili Nie, De-An Huang, Boyi Li, Jinwoo Shin and Anima Anandkumar. "Efficient Video Diffusion Models via Content-Frame Motion-Latent Decomposition". *International Conference on Learning Representations ( ICLR ), 2024 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2403.14148*.
- Kyungmin Lee, Kihyuk Sohn and Jinwoo Shin. "DreamFlow: High-quality text-to-3D generation by Approximating Probability Flow". *International Conference on Learning Representations ( ICLR ), 2024 · 연구실 기재*.
- Kyuyoung Kim, Jongheon Jeong, Minyong An, Mohammad Ghavamzadeh, Krishnamurthy Dj Dvijotham, Jinwoo Shin and Kimin Lee. "Confidence-aware Reward Optimization for Fine-tuning Text-to-Image Models". *International Conference on Learning Representations ( ICLR ), 2024 · 연구실 기재*.
- Suhyeok Jang\*, Seojin Kim\*, Jinwoo Shin, Jongheon Jeong. "Confidence-aware Denoised Fine-tuning of Off-the-shelf Models for Certified Robustness". *Transactions on Machine Learning Research ( TMLR ), 2024 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2411.08933*.
- Seojin Kim\*, Jaehyun Nam\*, Junsu Kim, Hankook Lee, Sungsoo Ahn, Jinwoo Shin. "Holistic Molecular Representation Learning via Multi-view Fragmentation". *Transactions on Machine Learning Research ( TMLR ), 2024 (based on the preliminary version [W36] )*.
- Seojin Kim, Jaehyun Nam and Jinwoo Shin. "An Efficient Tokenization for Molecular Language Models". *NeurIPS Workshop on AI for New Drug Modalities (AIDrugX), 2024 · 연구실 기재*.
- Woomin Song, Jihoon Tack, Sangwoo Mo, Seunghyuk Oh and Jinwoo Shin. "Sparsified State-Space Models are Efficient Highway Networks". *NeurIPS Workshop on Efficient Natural Language and Speech Processing (ENLSP), 2024 (the newer version [J34] available at Transactions on Machine Learning Research) · 연구실 기재*.
- June Suk Choi, Kyungmin Lee, Jongheon Jeong, Saining Xie, Jinwoo Shin and Kimin Lee. "DiffusionGuard: A Robust Defense Against Malicious Diffusion-based Image Editing". *ICML Workshop on the Next Generation of AI Safety, 2024 (the newer version [C182] available at ICLR 2025) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2410.05694*.
- Subin Kim\*, Seong Hyeon Park\*, Sihyun Yu, Kihyuk Sohn, and Jinwoo Shin. "MC^2: Multi-view Consistent Depth Estimation via Coordinated Image-based Neural Rendering". *CVPR Workshop on Neural Rendering Intelligence, 2024 · 연구실 기재*.

**2023**

- Sangwoo Mo, Minkyu Kim, Kyungmin Lee and Jinwoo Shin. "S-CLIP: Semi-supervised Vision-Language Learning using Few Specialist Captions". *Conference on Neural Information Processing Systems ( NeurIPS ), 2023 · DOI: 10.52202/075280-2674*.
- Jian Meng, Li Yang, Kyungmin Lee, Jinwoo Shin, Deliang Fan and Jae-sun Seo. "Slimmed Asymmetrical Contrastive Learning and Cross Distillation for Lightweight Model Training". *Conference on Neural Information Processing Systems ( NeurIPS ), 2023 · DOI: 10.52202/075280-1828*.
- Huiwon Jang\*, Jihoon Tack\*, Daewon Choi, Jongheon Jeong and Jinwoo Shin. "Modality-Agnostic Self-Supervised Learning with Meta-Learned Masked Auto-Encoder". *Conference on Neural Information Processing Systems ( NeurIPS ), 2023 · DOI: 10.52202/075280-3232*.
- Jongheon Jeong and Jinwoo Shin. "Multi-scale Diffusion Denoised Smoothing". *Conference on Neural Information Processing Systems ( NeurIPS ), 2023 · DOI: 10.52202/075280-2945*.
- Jihoon Tack, Subin Kim, Sihyun Yu, Jaeho Lee, Jinwoo Shin and Jonathan Richard Schwarz. "Learning Large-scale Neural Fields via Context Pruned Meta-Learning". *Conference on Neural Information Processing Systems ( NeurIPS ), 2023 (based on the preliminary version [W35] ) · DOI: 10.52202/075280-3174*.
- Changyeon Kim, Younggyo Seo, Hao Liu, Lisa Lee, Jinwoo Shin, Honglak Lee and Kimin Lee. "Guide Your Agent with Adaptive Multimodal Rewards". *Conference on Neural Information Processing Systems ( NeurIPS ), 2023 (based on the preliminary version [W42] ) · DOI: 10.52202/075280-2373*.
- Subin Kim\*, Kyungmin Lee\*, June Suk Choi, Jongheon Jeong, Kihyuk Sohn, and Jinwoo Shin. "Collaborative Score Distillation for Consistent Visual Synthesis". *Conference on Neural Information Processing Systems ( NeurIPS ), 2023 (based on the preliminary version [W39] ) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2307.04787*.
- Dongyoung Kim, Jinwoo Shin, Pieter Abbeel and Younggyo Seo. "Accelerating Reinforcement Learning with Value-Conditional State Entropy Exploration". *Conference on Neural Information Processing Systems ( NeurIPS ), 2023 · DOI: 10.52202/075280-1380*.
- Taesik Gong, Yewon Kim, Adiba Orzikulova, Yunxin Liu, Sung Ju Hwang, Jinwoo Shin and Sung-Ju Lee. "DAPPER: Label-Free Performance Estimation after Personalization for Heterogeneous Mobile Sensing". *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies ( IMWUT ), 2023 (will be presented at ACM UbiComp 2023) · 연구실 기재*.
- Jaehyung Kim, Jinwoo Shin and Dongyeop Kang. "Prefer to Classify: Improving Text Classifiers via Auxiliary Preference Learning". *International Conference on Machine Learning ( ICML ), 2023 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2306.04925*.
- Jonathan Richard Schwarz\*, Jihoon Tack\*, Yee Whye Teh, Jaeho Lee, and Jinwoo Shin. "Modality-Agnostic Variational Compression of Implicit Neural Representations". *International Conference on Machine Learning ( ICML ), 2023 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2301.09479*.
- Younggyo Seo\*, Junsu Kim\*, Stephen James, Kimin Lee, Jinwoo Shin, Pieter Abbeel. "Multi-View Masked World Models for Visual Robotic Manipulation". *International Conference on Machine Learning ( ICML ), 2023 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2302.02408*.
- Jaehyung Kim, Yekyung Kim, Karin Johanna, Denton de Langis, Jinwoo Shin and Dongyeop Kang. "infoVerse: A Universal Framework for Dataset Characterization with Multidimensional Meta-information". *Annual Meeting of the Association for Computational Linguistics ( ACL ), 2023 · DOI: 10.18653/v1/2023.acl-long.547*.
- Sihyun Yu, Kihyuk Sohn, Subin Kim and Jinwoo Shin. "Video Probabilistic Diffusion Models in Projected Latent Space". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2023 · DOI: 10.1109/cvpr52729.2023.01770*.
- Sukmin Yun\*, Seong Hyeon Park\*, Paul Hongsuck Seo and Jinwoo Shin. "IFSeg: Image-free Semantic Segmentation via Vision-Language Model". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2023 · DOI: 10.1109/cvpr52729.2023.00290*.
- Jongheon Jeong, Sihyun Yu, Hankook Lee Lee and Jinwoo Shin. "Enhancing Multiple Reliability Measures via Nuisance-extended Information Bottleneck". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2023 (based on the preliminary version [W30] ) · DOI: 10.1109/cvpr52729.2023.01555*.
- Jongin Lim, Youngdong Kim, Byungjai Kim, Chanho Ahn, Jinwoo Shin, Eunho Yang and Seungju Han. "BiasAdv: Bias-Adversarial Augmentation for Debiasing Classifier". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2023 · 연구실 기재*.
- Kisoo Kwon, Kuhwan Jeong, Junghyun Park Park, Hwidong Na and Jinwoo Shin. "String-based Molecule Generation via Multi-decoder VAE". *IEEE International Conference on Acoustics, Speech and Signal Processing ( ICASSP ), 2023 · DOI: 10.1109/icassp49357.2023.10095212*.
- Huiwon Jang\*, Hankook Lee\* and Jinwoo Shin. "Unsupervised Meta-learning via Few-shot Pseudo-supervised Contrastive Learning". *International Conference on Learning Representations ( ICLR ), 2023 (based on the preliminary version [W34] ) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2303.00996*.
- Jaehyun Nam, Jihoon Tack, Kyungmin Lee, Hankook Lee, and Jinwoo Shin. "STUNT: Few-shot Tabular Learning with Self-generated Tasks from Unlabeled Tables". *International Conference on Learning Representations ( ICLR ), 2023 (based on the preliminary version [W33] ) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2303.00918*.
- Changyeon Kim\*, Jongjin Park\*, Jinwoo Shin, Honglak Lee, Pieter Abbeel, and Kimin Lee. "Preference Transformer: Modeling Human Preferences using Transformers for RL". *International Conference on Learning Representations ( ICLR ), 2023 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2303.00957*.
- Junsu Kim, Younggyo Seo, Sungsoo Ahn, Kyunghwan Son and Jinwoo Shin. "Imitating Graph-Based Planning with Goal-Conditioned Policies". *International Conference on Learning Representations ( ICLR ), 2023 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2303.11166*.
- Hankook Lee, Jongheon Jeong, Sejun Park and Jinwoo Shin. "Guiding Energy-based Models via Contrastive Latent Variables". *International Conference on Learning Representations ( ICLR ), 2023 (based on the preliminary version [W31] ) · 연구실 기재*.
- Seungwoo Shim, Hyeonho Shin, Myeongkyun Cho, Youngki Lee, Jinwoo Shin and Song Min Kim. "Mosaic: Extremely Low-resolution RFID Vision for Visually-anonymized Action Recognition". *ACM/IEEE International Conference on Information Processing in Sensor Networks ( IPSN ), 2023 · DOI: 10.1145/3583120.3586968*.
- Jung-hun Kim, Se-Young Yun, Minchan Jeong, Junhyun Nam, Jinwoo Shin and Richard Combes. "Contextual Linear Bandits under Noisy Features: Towards Bayesian Oracles". *International Conference on Artificial Intelligence and Statistics ( AISTATS ), 2023 · 연구실 기재*.
- Minseon Kim, Jihoon Tack, Jinwoo Shin and Sung Ju Hwang. "Rethinking the Entropy of Instance in Adversarial Training". *IEEE Conference on Secure and Trustworthy Machine Learning ( SaTML ), 2023 (based on the preliminary version [W20] ) · DOI: 10.1109/satml54575.2023.00029*.
- Jongheon Jeong\*, Seojin Kim\* and Jinwoo Shin. "Confidence-aware Training of Smoothed Classifiers for Certified Robustness". *AAAI Conference on Artificial Intelligence ( AAAI ), 2023 (based on the preliminary version [W29] ) · DOI: 10.1609/aaai.v37i7.25968*.
- Junhyun Nam, Sangwoo Mo, Jaeho Lee and Jinwoo Shin. "Breaking the Spurious Causality of Conditional Generation via Fairness Intervention with Corrective Sampling". *Transactions on Machine Learning Research ( TMLR ), 2023 (based on the preliminary version [W44] ) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2212.02090*.
- Seojin Kim, Jaehyun Nam, Sihyun Yu, Younghoon Shin and Jinwoo Shin. "Data-Efficient Molecular Generation with Hierarchical Textual Inversion". *NeurIPS Workshop on New Frontiers of AI for Drug Discovery and Development, 2023 (the newer version [C165] available at ICML 2024) · 연구실 기재*.
- Minji Lee, Kyungmin Lee and Jinwoo Shin. "Fine-tuning protein Language Models by ranking protein fitness". *NeurIPS Workshop on Generative AI and Biology (GenBio), 2023 · 연구실 기재*.
- Younggyo Seo\*, Junsu Kim\*, Stephen James, Kimin Lee, Jinwoo Shin, and Pieter Abbeel. "Multi-View Masked World Models for Visual Robotic Manipulation". *RSS Workshop on Experiment-oriented Locomotion and Manipulation Research, 2023 · 연구실 기재*.
- Younghyun Kim\*, Sangwoo Mo\*, Minkyu Kim, Kyungmin Lee, Jaeho Lee, Jinwoo Shin. "Bias-to-Text: Debiasing Unknown Visual Biases by Language Interpretation". *ICML Workshop on Spurious Correlations, Invariance and Stability, 2023 (the newer version [C163] available at CVPR 2024) · 연구실 기재*.
- Junhyun Nam, Sangwoo Mo, Jaeho Lee and Jinwoo Shin. "Breaking the Spurious Causality of Conditional Generation via Fairness Intervention with Corrective Sampling". *ICML Workshop on Spurious Correlations, Invariance and Stability, 2023 (the newer version [J30] available at Transactions on Machine Learning Research) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2212.02090*.
- Jaehyun Nam, Woomin Song, Seong Hyeon Park, Jihoon Tack, Sukmin Yun, Jaehyung Kim, and Jinwoo Shin. "Semi-supervised Tabular Classification via In-context Learning of Large Language Models". *ICML Workshop on Efficient Systems for Foundation Models, 2023 (the newer version [C168] available at COLM 2024) · 연구실 기재*.
- Changyeon Kim, Younggyo Seo, Hao Liu, Lisa Lee, Jinwoo Shin, Honglak Lee, and Kimin Lee. "Guide Your Agent with Adaptive Multimodal Rewards". *ICML Workshop on New Frontiers in Learning, Control, and Dynamical Systems, 2023 (the newer version [C151] available at NeurIPS 2023) · DOI: 10.52202/075280-2373*.
- Sangkyung Kwak, Jongheon Jeong, Hankook Lee, Woohyuck Kim, and Jinwoo Shin. "Few-shot Anomaly Detection via Personalization". *ICML Workshop on New Frontiers in Adversarial Machine Learning, 2023 · DOI: 10.1109/access.2024.3355021*.
- Subin Kim\*, Kyungmin Lee\*, June Suk Choi, Jongheon Jeong, Kihyuk Sohn, and Jinwoo Shin. "Collaborative Score Distillation for Consistent Visual Synthesis". *ICML Workshop on Structured Probabilistic Inference & Generative Modeling, 2023 (the newer version [C149] available at NeurIPS 2023) · 연구실 기재*.
- Sanghyun Kim, Seohyeon Jung, Balhae Kim Kim, Moonseok Choi Choi, Jinwoo Shin and Juho Lee. "Towards Safe Self-Distillation of Internet-Scale Text-to-Image Diffusion Models". *ICML Workshop on Deployable Generative AI, 2023 · 연구실 기재*.
- Jonathan Richard Schwarz\*, Jihoon Tack\*, Yee Whye Teh, Jaeho Lee, and Jinwoo Shin. "Modality-Agnostic Variational Compression of Implicit Neural Representations". *ICLR Workshop on Neural Fields across Fields: Methods and Applications of Implicit Neural Representations, 2023 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2301.09479*.
- Seojin Kim\*, Jaehyun Nam\*, Junsu Kim, Hankook Lee, Sungsoo Ahn, and Jinwoo Shin. "Fragment-based Multi-view Molecular Contrastive Learning". *ICLR Workshop on Machine Learning for Materials: From Molecules to Materials, 2023 (the newer version [J31] available at Transactions on Machine Learning Research) · 연구실 기재*.
- Jihoon Tack, Subin Kim, Sihyun Yu, Jaeho Lee, Jinwoo Shin and Jonathan Richard Schwarz. "Efficient Meta-Learning via Error-based Context Pruning for Implicit Neural Representations". *ICLR Workshop on Neural Fields across Fields: Methods and Applications of Implicit Neural Representations, 2023 (the newer version [C152] available at NeurIPS 2023) · 연구실 기재*.

**2022**

- Subin Kim\*, Sihyun Yu\*, Jaeho Lee, and Jinwoo Shin. "Scalable Neural Video Representations with Learnable Positional Features". *Conference on Neural Information Processing Systems ( NeurIPS ), 2022 · 연구실 기재*.
- Kyungmin Lee and Jinwoo Shin. "RenyiCL: Contrastive Representation Learning with Skew Renyi Divergence". *Conference on Neural Information Processing Systems ( NeurIPS ), 2022 · DOI: 10.52202/068431-0468*.
- Taesik Gong, Jongheon Jeong, Taewon Kim, Yewon Kim, Jinwoo Shin and Sung-Ju Lee. "NOTE: Robust Continual Test-time Adaptation Against Temporal Correlation". *Conference on Neural Information Processing Systems ( NeurIPS ), 2022 · DOI: 10.52202/068431-1976*.
- Jihoon Tack, Jongjin Park, Hankook Lee, Jaeho Lee and Jinwoo Shin. "Meta-Learning with Self-Improving Momentum Target". *Conference on Neural Information Processing Systems ( NeurIPS ), 2022 · DOI: 10.52202/068431-0457*.
- Seong Hyeon Park, Jihoon Tack, Byeongho Heo, Jung-Woo Ha and Jinwoo Shin. "K-centered Patch Sampling for Efficient Video Recognition". *European Conference on Computer Vision ( ECCV ), 2022 · DOI: 10.1007/978-3-031-19833-5_10*.
- Sukmin Yun, Jaehyung Kim, Dongyoon Han, Hwanjun Song, Jung-Woo Ha and Jinwoo Shin. "Time Is MattEr: Temporal Self-supervision for Video Transformers". *International Conference on Machine Learning ( ICML ), 2022 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2207.09067*.
- Hwijoon Lim, Yechan Kim, Sukmin Yun, Jinwoo Shin and Dongsu Han. "TSPipe: Learn from Teacher Faster with Pipelines". *International Conference on Machine Learning ( ICML ), 2022 · 연구실 기재*.
- Kyunghwan Son, Junsu Kim, Sungsoo Ahn, Roben Delos Reyes, Yung Yi and Jinwoo Shin. "Disentangling Sources of Risk for Distributional Multi-Agent Reinforcement Learning". *International Conference on Machine Learning ( ICML ), 2022 · 연구실 기재*.
- Minsu Ko, Eunju Cha, Sungjoo Suh, Huijin Lee, Jae-Joon Han, Jinwoo Shin and Bohyung Han. "Self-Supervised Dense Consistency Regularization for Image-to-Image Translation". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2022 · DOI: 10.1109/cvpr52688.2022.01776*.
- Sukmin Yun, Hankook Lee, Jaehyung Kim and Jinwoo Shin. "Patch-level Representation Learning for Self-supervised Vision Transformers". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2022 · DOI: 10.1109/cvpr52688.2022.00817*.
- Jian Meng, Li Yang, Jinwoo Shin, Deliang Fan and Jae-sun Seo. "Contrastive Dual Gating: Learning Sparse Features With Contrastive Learning". *IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ), 2022 · DOI: 10.1109/cvpr52688.2022.01194*.
- Jaehyung Kim, Dongyeop Kang, Sungsoo Ahn and Jinwoo Shin. "What Makes Better Augmentation Strategies? Augment Difficult but Not too Different". *International Conference on Learning Representations ( ICLR ), 2022 · 연구실 기재*.
- Junhyun Nam, Jaehyung Kim, Jaeho Lee and Jinwoo Shin. "Spread Spurious Attribute: Improving Worst-group Accuracy with Spurious Attribute Estimation". *International Conference on Learning Representations ( ICLR ), 2022 · 연구실 기재*.
- Jongjin Park, Younggyo Seo, Jinwoo Shin, Honglak Lee, Pieter Abbeel and Kimin Lee. "SURF: Semi-supervised Reward Learning with Data Augmentation for Feedback-efficient Preference-based Reinforcement Learning". *International Conference on Learning Representations ( ICLR ), 2022 (based on the preliminary version [W26] ) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2203.10050*.
- Youngmin Oh, Jinwoo Shin, Eunho Yang and Sung Ju Hwang. "Model-augmented Prioritized Experience Replay". *International Conference on Learning Representations ( ICLR ), 2022 · 연구실 기재*.
- Sihyun Yu\*, Jihoon Tack\*, Sangwoo Mo\*, Hyunsu Kim, Junho Kim, Jung-Woo Ha, and Jinwoo Shin. "Generating Videos with Dynamics-aware Implicit Generative Adversarial Networks". *International Conference on Learning Representations ( ICLR ), 2022 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2202.10571*.
- Joonhyung Park, June Yong Yang, Jinwoo Shin, Sung Ju Hwang and Eunho Yang. "Saliency Grafting: Innocuous Attribution-Guided Mixup with Calibrated Label Mixing". *AAAI Conference on Artificial Intelligence ( AAAI ), 2022 · DOI: 10.1609/aaai.v36i7.20766*.
- Jihoon Tack, Sihyun Yu, Jongheon Jeong, Minseon Kim, Sung Ju Hwang and Jinwoo Shin. "Consistency Regularization for Adversarial Robustness". *AAAI Conference on Artificial Intelligence ( AAAI ), 2022 (based on the preliminary version [W19] ) · DOI: 10.1609/aaai.v36i8.20817*.
- Huiwon Jang\*, Hankook Lee\* and Jinwoo Shin. "Unsupervised Meta-learning via Few-shot Pseudo-supervised Contrastive Learning". *NeurIPS Workshop on Meta-Learning, 2022 (the newer version [C135] available at ICLR 2023) · 연구실 기재*.
- Jaehyun Nam, Jihoon Tack, Kyungmin Lee, Hankook Lee, and Jinwoo Shin. "STUNT: Few-shot Tabular Learning with Self-generated Tasks from Unlabeled Tables". *NeurIPS Workshop on Table Representation Learning, 2022 (the newer version [C134] available at ICLR 2023) · 연구실 기재*.
- Changyeon Kim\*, Junsu Kim\*, Younggyo Seo, Kimin Lee, Honglak Lee, and Jinwoo Shin. "Dynamics-Augmented Decision Transformer for Offline Dynamics Generalization". *NeurIPS Workshop on Offline Reinforcement Learning, 2022 · 연구실 기재*.
- Hankook Lee, Jongheon Jeong, Sejun Park and Jinwoo Shin. "Guiding Energy-based Models via Contrastive Latent Variables". *NeurIPS Workshop on Self-Supervised Learning: Theory and Practice, 2022 (the newer version [C130] available at ICLR 2023) · 연구실 기재*.
- Jongheon Jeong, Sihyun Yu, Hankook Lee and Jinwoo Shin. "Learning Robust Representations via Nuisance-extended Information Bottleneck". *ECCV Workshop on Out-of-distribution Generalization in Computer Vision, 2022 (the newer version [C138] available at CVPR 2023) · 연구실 기재*.
- Jongheon Jeong\*, Seojin Kim\* and Jinwoo Shin. "Confidence-aware Training of Smoothed Classifiers for Certified Robustness". *ECCV Workshop on Adversarial Robustness in the Real World, 2022 (the newer version [C125] available at AAAI 2023) · DOI: 10.1609/aaai.v37i7.25968*.
- Jongjin Park\*, Sukmin Yun\*, Jongheon Jeong, and Jinwoo Shin. "OpenCoS: Contrastive Semi-supervised Learning for Handling Open-set Unlabeled Data". *ECCV Workshop on Learning from Limited and Imperfect Data, 2022 · DOI: 10.1007/978-3-031-25063-7_9*.
- Hyunwoo Kang\*, Sangwoo Mo\* and Jinwoo Shin. "ReMixer: Object-aware Mixing Layer for Vision Transformers and Mixers". *ICLR Workshop on the Elements of Reasoning: Objects, Structure and Causality, 2022 · 연구실 기재*.

**2021**

- Amir Zandieh\*, Insu Han\*, Haim Avron, Neta Shoham, Chaewon Kim and Jinwoo Shin. "Scaling Neural Tangent Kernels via Sketching and Random Features". *Conference on Neural Information Processing Systems ( NeurIPS ), 2021 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2106.07880*.
- Jongheon Jeong, Sejun Park, Minkyu Kim, Heung-Chang Lee, Doguk Kim and Jinwoo Shin. "SmoothMix: Training Confidence-calibrated Smoothed Classifiers for Certified Robustness". *Conference on Neural Information Processing Systems ( NeurIPS ), 2021 (based on the preliminary version [W21] ) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2111.09277*.
- Sihyun Yu, Sungsoo Ahn, Le Song and Jinwoo Shin. "RoMA: Robust Model Adaptation for Offline Model-based Optimization". *Conference on Neural Information Processing Systems ( NeurIPS ), 2021 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2110.14188*.
- Sangwoo Mo\*, Hyunwoo Kang\*, Kihyuk Sohn, Chun-Liang Li and Jinwoo Shin. "Object-aware Contrastive Learning for Debiased Scene Representation". *Conference on Neural Information Processing Systems ( NeurIPS ), 2021 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2108.00049*.
- Jongjin Park\*, Younggyo Seo\*, Chang Liu, Li Zhao, Tao Qin, Jinwoo Shin and Tie-Yan Liu. "Object-Aware Regularization for Addressing Causal Confusion in Imitation Learning". *Conference on Neural Information Processing Systems ( NeurIPS ), 2021 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2110.14118*.
- Jaeho Lee\*, Jihoon Tack\*, Namhoon Lee, and Jinwoo Shin. "Meta-Learning Sparse Implicit Neural Representations". *Conference on Neural Information Processing Systems ( NeurIPS ), 2021 (based on the preliminary version [W25] ) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2110.14678*.
- Junsu Kim, Younggyo Seo and Jinwoo Shin. "Landmark-Guided Subgoal Generation in Hierarchical Reinforcement Learning". *Conference on Neural Information Processing Systems ( NeurIPS ), 2021 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2110.13625*.
- Hankook Lee, Kibok Lee, Kimin Lee, Honglak Lee and Jinwoo Shin. "Improving Transferability of Representations via Augmentation-Aware Self-Supervision". *Conference on Neural Information Processing Systems ( NeurIPS ), 2021 (based on the preliminary version [W23] ) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2111.09613*.
- Seunghyun Lee\*, Younggyo Seo\*, Kimin Lee, Pieter Abbeel and Jinwoo Shin. "Offline-to-Online Reinforcement Learning via Balanced Replay and Pessimistic Q-Ensemble". *Conference on Robot Learning ( CoRL ), 2021 (based on the preliminary version [W13] ) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2107.00591*.
- Hyuntak Cha, Jaeho Lee and Jinwoo Shin. "Co2L: Contrastive Continual Learning". *IEEE/CVF International Conference on Computer Vision ( ICCV ), 2021 · DOI: 10.1109/iccv48922.2021.00938*.
- Sejun Park, Jaeho Lee, Chulhee Yun and Jinwoo Shin. "Provable Memorization via Deep Neural Networks using Sub-linear Parameters". *Conference on Learning Theory ( COLT ), 2021 · 연구실 기재*.
- Younggyo Seo\*, Lili Chen\*, Jinwoo Shin, Honglak Lee, Pieter Abbeel and Kimin Lee. "State Entropy Maximization with Random Encoders for Efficient Exploration". *International Conference on Machine Learning ( ICML ), 2021 (based on the preliminary version [W17] ) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2102.09430*.
- Junsu Kim, Sungsoo Ahn, Hankook Lee and Jinwoo Shin. "Self-Improved Retrosynthetic Planning". *International Conference on Machine Learning ( ICML ), 2021 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2106.04880*.
- Divyam Madaan, Jinwoo Shin and Sung Ju Hwang. "Learning to Generate Noise for Multi-Attack Robustness". *International Conference on Machine Learning ( ICML ), 2021 (based on the preliminary version [W15] ) · 연구실 기재*.
- Jongheon Jeong and Jinwoo Shin. "Training GANs with Stronger Augmentations via Contrastive Discriminator". *International Conference on Learning Representations ( ICLR ), 2021 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2103.09742*.
- Sejun Park, Chulhee Yun, Jaeho Lee and Jinwoo Shin. "Minimum Width for Universal Approximation". *International Conference on Learning Representations ( ICLR ), 2021 · 연구실 기재*.
- Youngmin Oh, Kimin Lee, Jinwoo Shin, Eunho Yang and Sung Ju Hwang. "Learning to Sample with Local and Global Contexts in Experience Replay Buffer". *International Conference on Learning Representations ( ICLR ), 2021 (based on the preliminary version [W14] ) · 연구실 기재*.
- Jaeho Lee, Sejun Park, Sangwoo Mo, Sungsoo Ahn and Jinwoo Shin. "Layer-adaptive Sparsity for the Magnitude-based Pruning". *International Conference on Learning Representations ( ICLR ), 2021 · 연구실 기재*.
- Kibok Lee, Yian Zhu, Kihyuk Sohn, Chun-Liang Li, Jinwoo Shin and Honglak Lee. "i-Mix: A Domain-Agnostic Strategy for Contrastive Representation Learning". *International Conference on Learning Representations ( ICLR ), 2021 (based on the preliminary version [W12] ) · 연구실 기재*.
- Changho Hwang, Taehyun Kim, Sunghyun Kim, Jinwoo Shin and KyoungSoo Park. "Elastic Resource Sharing for Distributed Deep Learning". *USENIX Symposium on Networked Systems Design and Implementation ( NSDI ), 2021 · 연구실 기재*.
- Jongjin Park, Younggyo Seo, Jinwoo Shin, Honglak Lee, Pieter Abbeel and Kimin Lee. "SURF: Semi-supervised Reward Learning with Data Augmentation for Feedback-efficient Preference-based Reinforcement Learning". *NeurIPS Workshop on Deep Reinforcement Learning, 2021 (the newer version [C108] available at ICLR 2022) · 연구실 기재*.
- Jaeho Lee, Jihoon Tack, Namhoon Lee and Jinwoo Shin. "Meta-Learning Sparse Implicit Neural Representations". *Workshop on Sparsity in Neural Networks: Advancing Understanding and Practice, 2021 (the newer version [C98] available at NeurIPS 2021) · 연구실 기재*.
- Hankook Lee, Kibok Lee, Kimin Lee, Honglak Lee and Jinwoo Shin. "Improving Transferability of Representations via Augmentation-Aware Self-Supervision". *ICML Workshop on Self-Supervised Learning for Reasoning and Perception, 2021 (the newer version [C96] available at NeurIPS 2021) · 연구실 기재*.
- Sihyun Yu, Sangwoo Mo, Sungsoo Ahn and Jinwoo Shin. "Abstract Reasoning via Logic-guided Generation". *ICML Workshop on Self-Supervised Learning for Reasoning and Perception, 2021 · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2107.10493*.
- Jongheon Jeong, Sejun Park, Minkyu Kim, Heung-Chang Lee, Doguk Kim and Jinwoo Shin. "SmoothMix: Training Confidence-calibrated Smoothed Classifiers for Certified Adversarial Robustness". *ICML Workshop on Adversarial Machine Learning, 2021 (the newer version [C102] available at NeurIPS 2021) · 연구실 기재*.
- Jihoon Tack, Sihyun Yu, Jongheon Jeong, Minseon Kim, Sung Ju Hwang and Jinwoo Shin. "Consistency Regularization for Adversarial Robustness". *ICML Workshop on Adversarial Machine Learning, 2021 (the newer version [C104] available at AAAI 2022) · DOI: 10.1609/aaai.v36i8.20817*.
- Youngbum Hur\*, Jihoon Tack\*, Eunho Yang, Sung Ju Hwang and Jinwoo Shin. "Consistency Regularization for Training Confidence-Calibrated Classifiers". *ICML Workshop on Uncertainty & Robustness in Deep Learning, 2021 · 연구실 기재*.
- Younggyo Seo\*, Lili Chen\*, Jinwoo Shin, Honglak Lee, Pieter Abbeel and Kimin Lee. "State Entropy Maximization with Random Encoders for Efficient Exploration". *ICLR Workshop on Self-Supervision on Reinforcement Learning, 2021 (the newer version [C91] available at ICML 2021) · 연결된 arXiv 사전 공개본 DOI: 10.48550/arxiv.2102.09430*.

## 수상과 선정

연구실 소식의 수상·선정 13건, 교수 소개의 KAIST Academic Award 1건, 논문 목록의 Best Presentation Award 1건이다. 2023년 KAIST Academic Award는 교수 소개의 연도 표기이고, 2025년 Best Presentation Award는 해당 워크숍의 연도 표기이며 일자는 게시되어 있지 않다.[^news][^prof][^pubs]

- 2026-03 · AGI-LAB, NVIDIA Academic Grant 선정
- 2025-12 · 신진우 교수, 한국정보처리학회 운당학술대상 수상
- 2025-11 · Sihyun Yu·Kyuyoung Kim, Qualcomm Innovation Fellowship Korea 2025 수상
- 2024-12 · 신진우 교수, 과학기술정보통신부 장관 최석정상 수상
- 2024-12 · Hyunseok Lee·Jihoon Tack, Qualcomm Innovation Fellowship Korea 2024 수상
- 2024-02 · Jongheon Jeong, KAIST 공과대학 Best PhD Dissertation Award 수상
- 2023-12 · 신진우 교수, KAIST Global Research Cooperation Award 2023 수상
- 2023-11 · Subin Kim·Sihyun Yu, Qualcomm Innovation Fellowship Korea 2023 수상
- 2023-10 · Jihoon Tack, Google PhD Fellowship 2023 선정
- 2023-01 · Jaehyun Nam, Samsung Humantech Paper Award Bronze Prize 수상
- 2022-11 · Jaehyung Kim·Sukmin Yun, Qualcomm Innovation Fellowship Korea 2022 수상
- 2022-01 · Jaehyung Kim, Samsung Humantech Paper Award Silver Prize 수상
- 2021-11 · Jaehyung Kim·Sangwoo Mo·Hyunwoo Kang, Qualcomm Innovation Fellowship Korea 2021 수상
- 2023 · 신진우 교수, KAIST Academic Award 수상
- 2025 · 「MALT Diffusion: Memory-Augmented Latent Transformers for Any-Length Video Generation」, CVPR Workshop on AI for Content Creation의 Best Presentation Award 수상

## 소식

2021년 12월부터 2026년 9월까지 연구실이 게시한 논문 채택·게재 승인과 기술 보고서 공개 소식 50건이다. 학회 항목의 「채택」과 학술지 항목의 「게재 승인」은 소식의 공지 내용을 나타낸다.[^news]

- 2026-09 · NeurIPS 2026 논문 9편 채택
- 2026-09 · CoRL 2026 논문 2편 채택
- 2026-08 · COLM 2026 논문 1편 채택
- 2026-07 · TMLR 2026 논문 1편 게재 승인
- 2026-06 · ECCV 2026 논문 1편 채택
- 2026-05 · RLWRLD와 공동으로 RLDX-1 기술 보고서 공개
- 2026-04 · ICML 2026 논문 3편 채택
- 2026-02 · CVPR 2026 논문 2편 채택
- 2026-01 · ICLR 2026 논문 5편 채택
- 2025-09 · NeurIPS 2025 논문 6편 채택
- 2025-08 · EMNLP 2025 논문 5편 채택
- 2025-05 · ICML 2025 논문 4편 채택
- 2025-05 · ACL 2025 논문 2편 채택
- 2025-04 · IJCAI 2025 논문 1편 채택
- 2025-02 · CVPR 2025 논문 5편 채택
- 2025-01 · ICLR 2025 논문 6편 채택(구두 발표 2편 포함)
- 2024-12 · AAAI 2025 논문 1편 채택 및 구두 발표 선정
- 2024-10 · NeurIPS Workshop 2024 논문 2편 채택(구두 발표 1편 포함)
- 2024-09 · NeurIPS 2024 논문 6편 채택(Spotlight Presentation 1편 포함)
- 2024-09 · EMNLP 2024 논문 1편 채택
- 2024-07 · COLM 2024 논문 1편 채택
- 2024-06 · ECCV 2024 논문 3편 채택
- 2024-05 · ICML 2024 논문 3편 채택
- 2024-04 · TMLR 2024 논문 1편 게재 승인
- 2024-04 · CVPR Workshop 2024 논문 1편 채택
- 2024-02 · CVPR 2024 논문 2편 채택
- 2024-01 · ICLR 2024 논문 6편 채택
- 2023-10 · NeurIPS Workshop 2023 논문 2편 채택
- 2023-10 · EMNLP 2023 논문 1편 채택
- 2023-09 · NeurIPS 2023 논문 9편 채택
- 2023-06 · RSS Workshop 2023 논문 1편 채택 및 Spotlight Presentation 선정
- 2023-06 · ICML Workshop 2023 논문 8편 채택
- 2023-06 · TMLR 2023 논문 1편 게재 승인
- 2023-05 · ACL 2023 논문 1편 채택
- 2023-04 · ICML 2023 논문 3편 채택
- 2023-03 · ICLR Workshop 2023 논문 3편 채택
- 2023-02 · CVPR 2023 논문 5편 채택
- 2023-01 · ICLR 2023 논문 6편 채택(Spotlight Presentation 3편 포함)
- 2023-01 · AISTATS 2023 논문 1편 채택
- 2022-11 · AAAI 2023 논문 2편 채택
- 2022-10 · NeurIPS Workshop 2022 논문 4편 채택
- 2022-09 · NeurIPS 2022 논문 4편 채택
- 2022-09 · CoRL 2022 논문 1편 채택
- 2022-08 · ECCV Workshop 2022 논문 3편 채택
- 2022-07 · ECCV 2022 논문 2편 채택
- 2022-05 · ICML 2022 논문 4편 채택
- 2022-03 · CVPR 2022 논문 3편 채택
- 2022-02 · ICLR Workshop 2022 논문 1편 채택
- 2022-01 · ICLR 2022 논문 5편 채택
- 2021-12 · AAAI 2022 논문 2편 채택

## 연락과 위치

- 연구실: KAIST 김재철AI대학원 양재캠퍼스[^home]
- 교수 사무실: 양재캠퍼스 5층 501호[^gsai]
- 교수 업무 이메일: jinwoos@kaist.ac.kr[^prof]
[^home]: AGI-LAB, Main. <http://alinlab.kaist.ac.kr/index.html> 관측일 2026-11-09.
[^prof]: AGI-LAB, Professor: Jinwoo Shin. <http://alinlab.kaist.ac.kr/shin.html> 관측일 2026-11-09.
[^people]: AGI-LAB, Members. <http://alinlab.kaist.ac.kr/members.html> 관측일 2026-11-09.
[^topics]: AGI-LAB, Research Topics. <http://alinlab.kaist.ac.kr/topic.html> 관측일 2026-11-09.
[^pubs]: AGI-LAB, Publications. <http://alinlab.kaist.ac.kr/publications.html> 관측일 2026-11-09.
[^news]: AGI-LAB, News. <http://alinlab.kaist.ac.kr/news.html> 관측일 2026-11-09.
[^gsai]: KAIST 김재철AI대학원, 구성원: 전임교수 신진우. <https://gsai.kaist.ac.kr/people-2/?lang=ko> 관측일 2026-11-09.
[^p1]: D. Kim 외, Y. Seo, neural information processing systems (2025). <https://doi.org/10.52202/085713-5392> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5102928677,publication_year:2021-2026> 관측일 2026-11-09.
[^p2]: J. Nam 외, T. Pfister, neural information processing systems (2025). <https://doi.org/10.52202/085713-3889> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5102928677,publication_year:2021-2026> 관측일 2026-11-09.
[^p3]: K. Kim, H. Jeon, J. Shin, neural information processing systems (2025). <https://doi.org/10.52202/085713-5520> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5102928677,publication_year:2021-2026> 관측일 2026-11-09.
[^p4]: J. Nam 외, J. Shin, neural information processing systems (2024). <https://doi.org/10.52202/079017-2932> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5102928677,publication_year:2021-2026> 관측일 2026-11-09.
[^p5]: H. Jung 외, J. Shin, neural information processing systems (2024). <https://doi.org/10.52202/079017-2417> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5102928677,publication_year:2021-2026> 관측일 2026-11-09.
[^p6]: S. Mo, M. Kim, K. Lee, J. Shin, neural information processing systems (2023). <https://doi.org/10.52202/075280-2674> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5102928677,publication_year:2021-2026> 관측일 2026-11-09.
[^p7]: J. Jeong, J. Shin, neural information processing systems (2023). <https://doi.org/10.52202/075280-2945> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5102928677,publication_year:2021-2026> 관측일 2026-11-09.
[^p8]: S. Yu 외, A. Anandkumar, arXiv (Cornell University) (온라인 2024-03-21). <https://doi.org/10.48550/arxiv.2403.14148> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5102928677,publication_year:2021-2026> 관측일 2026-11-09.

# 통계적 인공지능 연구실 (Statistical Artificial Intelligence Lab, SAILAB)

**KAIST 김재철AI대학원 · 최재식 교수**

- 분야: 인공지능의 판단 근거 설명, 생성 방법, 행동 계획, 시간에 따라 변하는 자료의 분석[^about][^research][^faculty]
- 대분야: 컴퓨팅·AI
- 태그: 설명 가능한 AI(XAI)[^research][^pi], 생성 인공지능[^research], 대형 언어 모델[^research], 강화학습[^research], 시계열 분석·예측[^research][^pi], 음향·오디오 AI[^research]
- 홈페이지: <https://sailab.kaist.ac.kr/ko>
- 근거와 출처: [통계적 인공지능 연구실 근거 페이지](sailab-sources.md)

> 인공지능이 어떤 근거로 판단하는지 설명하는 방법을 중심으로, 이미지·음성 생성, 로봇의 행동 계획, 기상과 시계열 예측 방법도 연구하는 연구실이다.[^research]

## 무엇을 연구하나

통계적 인공지능 연구실은 자료에서 규칙을 배우는 기계학습을 바탕으로, 불확실한 상황에서 기계가 어떻게 판단하는지 연구한다. 연구실 소개는 확률적 그래프 모델(여러 값 사이의 확률적 관계를 점과 선으로 나타내는 계산 모형)의 학습과 추론(알고 있는 정보로 아직 모르는 값을 알아내는 과정), 대규모 자료 분석, 로봇 동작 계획, 시간과 공간에 따라 변하는 자료의 분석을 주요 방향으로 제시한다.[^about] 최재식 교수의 현재 연구 소개는 복잡한 시스템에서의 학습·추론, 사람이 이해할 수 있는 기계학습 모형, 시공간 자료 분석에 중점을 둔다.[^pi]

설명가능 인공지능은 기계가 낸 답뿐 아니라 그 답에 도달한 근거를 사람이 이해하도록 하는 연구다. 연구실은 신경망(서로 연결된 계산 단위의 값과 연결 강도로 입력을 출력으로 바꾸는 계산 모형) 내부에서 어떤 계산 단위가 특정 시각 개념을 표현하는지 찾고, 입력 기여도(입력의 각 부분이 모형의 결과에 기여한 정도)를 계산하는 방법을 개발한다. 설명을 계산하는 경로, 계산 단위 사이의 연결, 개념을 공유하는 사례를 서로 다른 관점에서 다룬다.[^research]

생성 모델(학습 자료의 통계적 특성을 바탕으로 새로운 자료를 만들어 내는 모형)에서는 이미지의 창의성과 드문 이미지 생성, 합성 음성의 억양·발음 수정, 로봇이 실행할 행동 경로를 연구한다. 확산 모델(자료에 잡음을 더한 뒤 그 잡음을 단계적으로 제거하는 법을 학습해 자료를 생성하는 모형)이 만든 계획의 실행 가능성을 높이고, 강화학습(행동과 그 결과의 보상을 통해 누적 보상을 키우는 행동 방식을 배우는 방법)으로 여러 기술을 익히는 방법도 연구한다. 잡음은 자료의 관측·처리에서 원하는 정보 외에 섞인 변동 성분이다. 음성 연구는 이미 학습한 모형의 내부 값을 바꿔 출력의 오류를 수정하는 방법을 포함한다.[^research]

시계열(시간 순서로 기록된 자료) 연구에서는 시간에 따른 추세와 반복 변동을 분리하고, 자료의 성질에 맞는 정보를 골라 예측·분류하는 방법을 개발한다. 기상 분야에서는 예보 모형이 어떤 강수 특성을 근거로 판단하는지 전문가가 이해할 수 있는 사례와 설명을 제공한다. 대형 언어 모델(Large Language Model, 많은 언어 자료를 학습해 문맥에 따른 언어의 이해와 생성을 수행하는 큰 계산 모형) 연구는 내부 동작의 분석, 문서별 기억 구조, 단어가 함께 나타나는 빈도와 사실 오류의 관계를 다룬다.[^research]

## 주요 연구 주제

### 판단의 근거와 내부 표현

모형이 어떤 입력을 중요하게 보았는지와 어떤 내부 계산이 개념을 나타내는지를 함께 연구한다. 시각 개념에 대응하는 계산 단위들의 연결을 찾는 연구, 입력을 바꿔 가며 결과의 변화를 누적해 설명하는 연구, 기여도 계산에서 요소 사이의 상호작용을 반영하는 연구가 있다.[^research] 최신 대표 논문은 입력의 전체 구조를 먼저 반영하고 세부 정보를 뒤이어 반영하는 설명 경로를 제안한다.[^p1]

### 이미지·음성 생성과 행동 계획

이미지를 만드는 중간 과정의 특징을 조절해 창의적 결과를 얻고, 이미 학습한 생성 모델에서 드문 사례를 만드는 방법을 개발한다. 음성 합성에서는 추가 학습 없이 억양과 발음 오류를 고치는 방법을 다룬다. 행동 계획에서는 실행할 수 없는 경로가 만들어지는 원인을 분석하고 이를 줄이는 방법을 연구하며, 보상과 학습 순서를 이용한 로봇 기술 습득도 다룬다.[^research]

### 시간 자료와 기상 예측

시간에 따라 변하는 자료에서 장기 추세와 반복되는 변동을 나누고, 중요한 시점이나 자료를 묶는 방식을 선택해 예측하는 방법을 연구한다. 기상 모형의 설명에서는 모형 내부의 수치 표현을 전문가가 이해할 수 있는 강수 개념과 사례에 연결하고, 설명을 살펴볼 사용자 화면을 만든다.[^research][^p8]

### 언어 모델의 내부 동작과 기억

트랜스포머(자료의 각 요소가 다른 요소와 맺는 관련도를 계산해 문맥을 반영하는 신경망 구조)의 층을 연속적으로 표현해 내부 변화를 분석하고, 모형 안에 문서별 기억 위치를 만드는 방법을 연구한다. 단어가 함께 나타나는 빈도에 치우치는 성질이 사실을 떠올리는 능력에 미치는 영향도 다룬다.[^research]

## 대표 논문

KAIST 재직 시기의 연구에서 모델 설명, 생성, 행동 계획, 언어 모델, 시계열과 기상 설명을 나누어 골랐다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. arXiv 판을 읽은 항목은 발표처 옆에 표시했다. 주요 저자는 전체 저자 순서의 첫 저자와 마지막 저자이며, 별도 역할을 추정하지 않았다.

| 번호 | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Spectral Integrated Gradients for Coarse-to-Fine Feature Attribution](https://doi.org/10.48550/arxiv.2605.19607) · KDD 2026(채택), arXiv 판 | 입력의 어떤 부분이 판단에 기여했는지 계산할 때, 입력을 바꾸어 가는 경로에 따라 설명이 달라질 수 있다. 기준 입력과 실제 입력의 차이를 서로 직각인 방향의 성분과 그 크기로 나누고, 큰 성분부터 차례로 반영하는 경로를 제안했다. 이미지의 전체 구조에서 세부로 진행하며 설명 지도에 섞이는 잡음을 줄였다.[^p1] | 첫 저자 Soyeon Kim, 마지막 저자 Jaesik Choi |
| 2 | 2025 | [Granular Concept Circuits: Toward a Fine-Grained Circuit Discovery for Concept Representations](https://doi.org/10.1109/iccv51701.2025.00227) · ICCV | 시각 모형이 배운 개념은 여러 계산 단위에 흩어져 있어 위치를 찾기 어렵다. 계산 단위들의 기능적 의존성과 의미의 대응을 반복해서 살펴, 주어진 질문과 관련된 개념별 연결 묶음을 찾는 방법을 제안했다. 여러 이미지 분류 모형에서 개념별 해석의 활용 가능성을 확인했다.[^p2] | 첫 저자 Dahee Kwon, 마지막 저자 Jaesik Choi. 연구실의 첫 두 저자 표시 *는 뜻을 추정하지 않았다 |
| 3 | 2025 | [Local Manifold Approximation and Projection for Manifold-Aware Diffusion Planning](https://doi.org/10.48550/arxiv.2506.00867) · ICML, arXiv 판 | 확산 기반 계획이 실행 불가능한 경로를 만드는 원인을 생성 과정의 부정확한 안내에서 찾았다. 저장된 자료로 실행 가능한 경로가 놓인 공간을 근사하고, 안내를 받은 표본을 그 공간으로 옮기는 방법을 제안했다. 추가 학습 없이 긴 행동 계획 과제에서 평가했으며, 계층적 확산 계획기의 별도 구성 요소로 넣어 성능을 높일 수 있음을 보였다.[^p3] | 첫 저자 Kyowoon Lee, 마지막 저자 Jaesik Choi |
| 4 | 2025 | [Enhancing Creative Generation on Stable Diffusion-based Models](https://doi.org/10.1109/cvpr52734.2025.02664) · CVPR | 이미지 생성 모형에 창의적으로 그리라고 적는 것만으로 원하는 결과가 나오지 않는 문제를 다룬다. Creative Concept Catalyst는 잡음을 제거하는 과정에서 일부 특징을 선택적으로 증폭한다. 추가 학습 없이 여러 Stable Diffusion 기반 모형에서 효과를 확인하고, 창의성의 두 측면에 따른 증폭 계수 선택 지침을 제시했다.[^p4] | 첫 저자 Jiyeon Han, 마지막 저자 Jaesik Choi. Jiyeon Han·Dahee Kwon은 연구실의 공동 기여 표기 |
| 5 | 2025 | [Counterfactual Activation Editing for Post-hoc Prosody and Mispronunciation Correction in TTS Models](https://doi.org/10.21437/interspeech.2025-723) · Interspeech | 글을 음성으로 바꾸는 Text-to-Speech(TTS) 모형이 이미 학습된 뒤에도 억양과 발음을 조절하는 방법이다. 모형 내부 표현을 바꾸어 억양의 특징과 잘못된 발음을 수정하며, 음성 합성 품질을 유지했다. 재학습 없이 출력 시점에 합성 음성을 다듬는 길을 열었다고 밝혔다.[^p5] | 첫 저자 Kyowoon Lee, 마지막 저자 Jaesik Choi |
| 6 | 2025 | [Neural ODE Transformers: Analyzing Internal Dynamics and Adaptive Fine-tuning](https://iclr.cc/virtual/2025/poster/29292) · ICLR | 언어 모델의 층 사이 변화를 신경 상미분방정식(Neural Ordinary Differential Equation, 순간적인 변화의 방향과 정도를 신경망으로 계산해 연속적인 변화를 기술하는 방정식)으로 나타냈다. 각 층의 가중치(입력된 값이 계산 결과에 미치는 정도를 정하는 수치)를 연속적인 층 위치에 따라 바뀌도록 두어 내부 변화를 분석하고, 입력 조각에 대한 민감도를 살펴 해석을 돕는다. 여러 구성과 자료에서 기존 트랜스포머에 견줄 만하거나 나은 성능을 보이고, 구조 제약에 맞춘 추가 학습의 유연성을 제시했다.[^p6] | 첫 저자 Anh Tong, 마지막 저자 Jaesik Choi |
| 7 | 2025 | [xPatch: Dual-Stream Time Series Forecasting with Exponential Seasonal-Trend Decomposition](https://doi.org/10.1609/aaai.v39i19.34270) · AAAI | 시간 자료의 추세와 반복되는 변동을 나누고, 선형 관계(입력의 합과 배율이 출력에도 같은 방식으로 반영되는 관계)와 그 밖의 관계를 서로 다른 흐름으로 처리하는 예측 구조를 제안했다. 자료를 구간으로 나누는 방법과 항목별 독립 처리의 효과를 살폈다. 예측 오차를 매기는 방식과 한 번의 학습에서 모형의 값을 얼마나 바꿀지 정하는 방식도 제안해 과적합(학습 자료의 세부까지 따라가 새로운 자료에서는 맞지 않게 되는 현상)을 막고 예측 성능을 높였다.[^p7] | 첫 저자 Artyom Stitsyuk, 마지막 저자 Jaesik Choi |
| 8 | 2025 | [Example-Based Concept Analysis Framework for Deep Weather Forecast Models](https://doi.org/10.1175/aies-d-24-0079.1) · Artificial Intelligence for the Earth Systems | 예보 모형이 대상 사례와 비슷한 과정으로 판단한 다른 사례를 찾아 사람이 이해할 수 있는 형태로 보여 주는 설명 틀을 개발했다. 시각적으로나 개념적으로 비슷한 예와 개념 배정 확률을 함께 제공한다. 사람이 개념을 표시한 자료와 전문가용 사용자 화면을 마련해, 모형 내부 표현과 이해 가능한 설명 사이를 연결했다.[^p8] | 첫 저자 Soyeon Kim, 마지막 저자 Jaesik Choi |

## 교수와 전문 분야

최재식 교수는 2004년 서울대학교에서 컴퓨터공학 학사를, 2012년 일리노이대학교 어배너-섐페인에서 전산학 박사를 받았다. 버클리 랩 박사후연구원과 UNIST 교원을 거쳐 2019년 9월 KAIST 인공지능대학원 부교수로 부임했고, 2024년 9월부터 정교수로 재직한다. 교수 소개는 설명가능 인공지능연구센터 센터장 역할도 적는다.[^pi] 김재철AI대학원의 전임교수 명단은 직위를 ‘교수’로 표기한다.[^faculty]

전문 분야는 복잡한 모형의 판단과 내부 표현을 설명하는 방법, 생성 모형을 분석·조절하는 방법, 시간과 공간에 따라 변하는 자료를 예측하는 방법이다.[^pi][^p2][^p3][^p7] 최근 논문에서는 이를 이미지와 음성 생성, 연속적인 층 표현을 사용하는 언어 모델, 예보 전문가를 위한 설명으로 구체화한다.[^p4][^p5][^p6][^p8]

## 응용 분야

연구실은 기상, 과학, 로봇, 언어, 산업 현장으로 연구를 연결한다고 소개한다.[^home] 대표 연구에서는 기상 전문가를 위한 설명 화면, 이미지 생성 과정의 조절, 합성 음성 수정, 로봇의 긴 행동 계획을 다룬다.[^p8][^p4][^p5][^p3] 시간 자료의 예측 구조와 모형 내부 분석 방법은 특정 응용 하나에 한정하지 않는 연구다.[^p7][^p6]

## 구성원

2026년 11월 9일 구성원 쪽에 게시된 교수·연구교수·대학원생·연구원·인턴 33명이다. 시작 표기는 누리집의 연월과 기간 표기를 따른다.[^members] ‘대표 논문 참여’는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| 최재식 | 교수 | 2019.09 |  |
| Nari Kim | 연구교수 |  |  |
| Sehyun Lee | 박사과정 | 20.03 ~ | 2 |
| 김소연 | 박사과정 | 20.09 ~ |  |
| 김성운 | 박사과정 | 21.03 ~ |  |
| 강청웅 | 박사과정 | 21.03 ~ |  |
| Seongyeop Jeong | 박사과정 | 21.03 ~ |  |
| Wonjoon Chang | 박사과정 | 21.09 ~ |  |
| Dahee Kwon | 박사과정 | 22.09 ~ | 2, 4 |
| 박범진 | 박사과정 | 23.09 ~ |  |
| 성지현 | 박사과정 | 23.09 ~ |  |
| Myeongjin Lee | 박사과정 | 24.03 ~ |  |
| Won Jo | 박사과정 | 24.09 ~ |  |
| Haksoo Lim | 박사과정 | 24.09 ~ |  |
| Yeonjea Kim | 박사과정 | 25.02 ~ |  |
| Jihoon Na | 박사과정 | 26.09 ~ |  |
| 박영진 | 석박사통합과정 | 19.03 ~ |  |
| 김솔아 | 석박사통합과정 | 20.03 ~ |  |
| Hyeongjin Byeon | 석박사통합과정 | 20.09 ~ |  |
| Junho Choi | 석박사통합과정 | 21.03 ~ | 8 |
| Enver Menadjiev | 석박사통합과정 | 21.09 ~ |  |
| Artyom Stitsyuk | 석박사통합과정 | 21.09 ~ | 5, 7 |
| Jinsil Lee | 석박사통합과정 | 22.09 ~ |  |
| Seongwook Chung | 석박사통합과정 | 24.03 ~ |  |
| Artyom Tashyan | 석박사통합과정 | 25.09 ~ |  |
| Kwangmin Choi | 석사과정 | 23.09 ~ |  |
| Jongeun Baek | 석사과정 | 25.03 ~ |  |
| Sakib Hossain | 석사과정 | 25.03 ~ |  |
| Jisu Yeo | 석사과정 | 25.09 ~ |  |
| Hyejin Shin | 연구원 | 26.10~ |  |
| Geonhyeong Kim | 연구원 | 23.05 ~ |  |
| Damin Lee | 인턴 | 25.09 ~ |  |
| Jiyu Lim | 인턴 | 25.12 ~ |  |

## 졸업생과 진로

구성원 쪽의 ‘졸업생’ 구획에 게시된 과거 학생·연구원·인턴 80명이다. 학위·과정과 기간, 진로는 게시 표기를 따르며, KAIST 부임 전 다른 소속에서 함께한 사람도 포함한다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 임성우 | Ph.D., 2025.09. Postdoctoral Researcher, 2025.09 - | INEEJI |
| 한지연 | Ph.D., 2025.09 |  |
| Anh Tong |  | Graduate School of AI at Korea University |
| Haedong Jeong |  | Sogang University (Previously at Samsung Advanced Institute of Technology) |
| Giyoung Jeon |  | LG AI Research |
| Qin Xie |  | Institute of Microelectronics, Chinese Academy of Sciences |
| Subeen Lee | MS student, 2023.09 – 2025.09 |  |
| Tair Djanibekov | MS student, 2023.09 – 2025.09 |  |
| Chanwoo Lee | MS student, 2023.09 – 2025.09 |  |
| Youngju Joung | MS student, 2023.03 – 2025.02 |  |
| Sangun Gu | MS student, 2021.09 – 2025.02 |  |
| Jungmin Kim | MS student, 2022.03 – 2024.09 |  |
| Hyeha Im | MS student, 2021.09 – 24.03 |  |
| Sekwang Oh | MS student, 2021.03 - 2023.09 | POSCO |
| Inyoung Paik | MS student, 2021.03 ~ 2023.09 |  |
| Seongjin Park | MS from KAIST AI, 2020 Fall - 2022 Spring | Samsung Advanced Institute of Technology |
| Hwanil Choi | MS from KAIST aI, 2020 Fall - 2022 Spring | LG AI Research |
| Deokjun Eom | MS Student, KAIST, 2020.03 – 2022.02 | Samsung Research |
| Nguyen Thanh Nguyen | MS student, 2018 September - 2021.04 |  |
| Alisher Abdulov | Researcher, KAIST, 2020 Fall - 2022.02 | 42dot |
| Dongju Shin | MS from UNIST, 2018 September - 2020 September | DEEPNOID |
| 천예은 | MS from UNIST, 2018 September - 2020 June | Shinhan Bank AI/Big Data Team |
| Jiwoo Lee | MS from UNIST, 2018 September - 2020 June | DEEPNOID |
| GinKyeng Lee | MS from UNIST, 2018 March - 2020 February |  |
| Janghoon Ju | 2018 January ~ 2019 January | KRAFTON |
| Ali Tousi | Researcher, 2018 September - 2022 June |  |
| Subin Yi | MS Student, 2016 March - 2018 February | SK T-Brain |
| Thanh Nguyen | Researcher, 2018 March | Johns Hopkins University |
| 하파엘 리마 |  | Samsung R&D Institute Brazil |
| Yunseong Hwang | MS from UNIST, 2016 | NAVER |
| 이교운 | Postdoctoral Researcher, 2024.10 - |  |
| Jinseok Seol | Postdoctoral Researcher, 2024.09 - 2025.08 | Dankook University |
| Boseon Yu | Postdoctoral Researcher, 2017.12 - 2021 Summer | INEEJI |
| Peng Zhang | Researcher, 2020.10 - 2022.08 |  |
| Kallol Roy | Postdoctoral Researcher, 2015 August - present | University of Tartu |
| Hyeonjeong Kwak | Research Intern, 2025.06 - 2026.02 |  |
| Minseok Yoon | Research Intern, 2025.06 - 2026.02 |  |
| Jeongmin Ha | Research Intern, 2025.12 - 2026.04 |  |
| Junhyeok Park | Research Intern, 2025.06 ~ 2025.08 |  |
| Kyunghwan Sohn | MS/PhD student, 2020 Spring – present |  |
| Seijun Chung | Researcher, 2020 Fall - present | Hyundai Advanced Process Technology Development Team |
| Daiki E. Matsunaga | MS/PhD student, 2020 Fall - present | KAIST Graduate School of AI |
| 조소희 | Researcher, 2017 September - 2021.08 | BMW Korea |
| Soonjae Kwon | Researcher , 2017 April - 2021.08 |  |
| Juhyeong Kim | MS student, 2020 Fall |  |
| Junhyuk Shin | Researcher, 2020 February - 2020 June | Samsung Electronics Mechatronic Center |
| 성낙원 | Researcher, 2019 January - present |  |
| Seongman Heo | Researcher, 2019 March - 2020 Spring |  |
| Minsu Kang | MS/PhD Student, 2019 Spring at UNIST |  |
| Sungguk Cha | MS/PhD Student, 2019 Spring at UNIST |  |
| Eunji Bang | MS student, 2018 September - present |  |
| Dongeun Lee |  | Assistant Professor, Texas A&M University-Commerce |
| Man-Ki Yoon |  | Associate Research Scientist at Yale University |
| Seonghyun Jo | Researcher, 2017 December - present |  |
| Vladimir Nekrasov | PhD student, 2016 March - 2017 March |  |
| Agnieszka Mikołajczyk | Visiting Student at UNIST |  |
| Uyoung Jeong | BS Student at UNIST | Graduate School of AI UNIST |
| Wonjun Yoon | BS degree from UNIST 2017 March |  |
| 강상훈 | BS from UNIST |  |
| 정경중 | PhD candidate at UNIST |  |
| Yooseung Wang | BS from UNIST |  |
| Madi Khamitbekov | BS Student at UNIST |  |
| Taehoon Kim | BS at UNIST |  |
| Azamatbek Akhmedov | BS from UNIST |  |
| Doyeon Lim | BS from UNIST |  |
| Wen Pu | PhD student PhD with General Intelligence Lab at University of Illinois at Urbana-Champaign | LinkedIn |
| Kejia Hu | MS student at University of California, Davis (previously PhD student at Northwestern) | Assistant Professor at Vanderbilt University |
| Phuong Hoang | MS/PhD student student at UNIST |  |
| Tianfang Xu | previously MS student student at University of Illinois at Urbana-Champaign, PhD student at UIUC | Research Assistant Professor at Utah University |
| Jun-Young Min | MS Graduate, UNIST (previously Asiana IDT Inc, a subsidiary of Asiana Airline) | Korea Airports Corporation |
| Guhnoo Yun | BS Student at Gyeongsang National University (USURF Intern) |  |
| Haebeom Lee | BS Student at UNIST |  |
| Sorang Cho | BS Student at Busan National University (USURF Intern) |  |
| Jungwoon Shin | BS Student at Boston University (USURF Intern) |  |
| Owen Xu He | BS Student at Jacobs University (SPIKE Intern) |  |
| Jongwhan Moon | BS student at UNIST | MS/PhD student at POSTECH |
| William Gu | BS student at University of California, Berkeley |  |
| Suhwan Chung | BS Student, UNIST |  |
| Zumrat Kochshegulov | BS Student, UNIST |  |
| Chung-Geol Ryu | BS Student, UNIST |  |

## 최근 5년 논문 목록

2021–2026년 연구실 논문 목록에 게시된 최재식 교수 참여 논문 61편이다. 제목·저자·발표처는 연구실 표기를 따르며, 발표처 옆의 ‘채택’과 ‘게재 승인’은 소식에서 해당 상태를 알린 항목의 표시다. ‘연구실 기재’는 누리집의 발표처 표기다. 별표는 누리집의 표시이며, 뜻이 명시된 공동 기여·공동 교신 표기는 발표처 칸에 남겼다.[^pubs][^news]

**2026**

- Anh Tong , Kyowoon Lee , and Jaesik Choi. "PRISM: Principal Subspace Alignment for Parameter-Efficient Fine-Tuning". *The 40th Annual Conference on Neural Information Processing Systems (NeurIPS) (채택)*.
- Kyowoon Lee , Yunhao Luo, Anh Tong , and Jaesik Choi. "Refining Compositional Diffusion for Reliable Long-Horizon Planning". *The 40th Annual Conference on Neural Information Processing Systems (NeurIPS) (채택)*.
- Junho Choi , and Jaesik Choi. "TreePII: Efficient Computation of Higher-Order Probabilistic Interaction Indices in Tree Ensembles". *The 40th Annual Conference on Neural Information Processing Systems (NeurIPS) (채택)*.
- Won Jo , Dahee Kwon , Jongeun Baek , Cheongwoong Kang , and Jaesik Choi. "Decision Path Tracing for Causal Analysis in Transformers". *The 40th Annual Conference on Neural Information Processing Systems (NeurIPS) (채택)*.
- Cheongwoong Kang, Jongeun Baek , Yeonjea Kim, Jaesik Choi. "Beyond Paraphrases: Generalization Across Task Formats in Parametric Knowledge Editing". *Findings of EMNLP (연구실 기재)*.
- Haksoo Lim , Myeongjin Lee , Wonjoon Chang , and Jaesik Choi. "Unified Backbone Refinement for Diffusion Models via Internal-Latent Analysis". *European Conference on Computer Vision (ECCV) 2026. (채택)*.
- Soyeon Kim , Kyowoon Lee , and Jaesik Choi. "Diffusion Integrated Gradients: Controllable Path Generation for Flexible Feature Attribution". *European Conference on Computer Vision (ECCV) 2026. (채택)*.
- Sehyun Lee , Dahee Kwon , Damin Lee , and Jaesik Choi. "SPICE: Simple Polysemantic Feature Interpretation via Clustering-based Explanations". *European Conference on Computer Vision (ECCV) 2026. (채택)*.
- Soyeon Kim , Seongwoo Lim , Kyowoon Lee , and Jaesik Choi. "[Spectral Integrated Gradients for Coarse-to-Fine Feature Attribution\](https://doi.org/10.1145/3770855.3817830)". *Knowledge Discovery and Data Mining (KDD) 2026*.
- Enver Menadjiev , Jihyeon Seong , Jisu Yeo , and Jaesik Choi. "DistMatch: Adaptive Binning via Distribution Matching for Robust Sequential Conformal Prediction". *International Conference on Machine Learning (ICML), 2026. (채택)*.
- Dahee Kwon , Ha-Eun Lee , and Jaesik Choi. "Breaking the Lock-in: Diversifying Text-to-Image Generation via Representation Modulation". *International Conference on Machine Learning (ICML), 2026. (채택)*.
- Soyeon Kim , Seongwoo Lim , Kyowoon Lee , and Jaesik Choi. "Manifold-Aligned Guided Integrated Gradients for Reliable Feature Attribution". *International Conference on Machine Learning (ICML), 2026. (채택)*.
- Yeonjea Kim , Bumjin Park , and Jaesik Choi. "Incomplete Prompt Jailbreaks in Large Language Models". *Findings of the Annual Meeting of the Association for Computational Linguistics (ACL), 2026. (채택)*.
- Soyeon Kim , Cheongwoong Kang , Myeongjin Lee , Eun-Chul Chang, Jaedeok Lee, and Jaesik Choi. "K-MetBench: A Multi-Dimensional Benchmark for Fine-Grained Evaluation of Expert Reasoning, Locality, and Multimodality in Meteorology". *Findings of the Annual Meeting of the Association for Computational Linguistics (ACL), 2026. (채택)*.
- Youngjin Park , Anh Tong , Sehyun Lee , Jihyeon Seong , Qin Xie and Jaesik Choi. "Towards Transparent Time Series Analysis: Exploring Methods and Enhancing Interpretability". *ACM Computing Surveys, 2026. (게재 승인)*.

**2025**

- Kyowoon Lee and Jaesik Choi. "State-Covering Trajectory Stitching for Diffusion Planners". *Conference on Neural Information Processing Systems (NeurIPS), 2025. (채택)*.
- Seongjin Park , Haedong Jeong , Tair Djanibekov , Giyoung Jeon , Jinseok Seol and Jaesik Choi. "On the Relationship between Populated Regions and Adversarial Robustness in Deep Neural Networks". *IEEE International Conference on Data Mining (ICDM), 2025. (채택)*.
- Cheongwoong Kang , Jongeun Baek , Yeonjea Kim , and Jaesik Choi. "[When Format Changes Meaning: Investigating Semantic Inconsistency of Large Language Models\](https://doi.org/10.18653/v1/2025.findings-emnlp.143)". *Findings of EMNLP*.
- Soyeon Kim , Junho Choi , Subeen Lee and Jaesik Choi. "[Unsupervised Concept Discovery for Deep Weather Forecast Models with High-Resolution Radar Data\](https://doi.org/10.1371/journal.pclm.0000633)". *PLOS Climate, 2025*.
- Chanwoo Lee , Youngjin Park , Hyeongeun Lee, Yeeun Yoo, Daehee Han, Junho Choi , Geonhyeong Kim , Nari Kim and Jaesik Choi. "[Amortized Baseline Selection via Rank-Revealing QR for Efficient Model Explanation\](https://doi.org/10.1145/3746252.3761036)". *Conference on Information and Knowledge Management (CIKM), 2025*.
- Jisu Yeo , Artyom Stitsyuk and Jaesik Choi. "[Deep-DFVAR: Dynamic Factor Vector Autoregression with Deep Learning for Regional House Price Index Forecasting\](https://doi.org/10.1016/j.neucom.2025.131103)". *Neurocomputing, 2025*.
- Dahee Kwon \*, Sehyun Lee \* and Jaesik Choi. "[Granular Concept Circuits: Toward a Fine-Grained Circuit Discovery for Concept Representations\](https://doi.org/10.1109/iccv51701.2025.00227)". *International Conference on Computer Vision (ICCV), 2025*.
- Jinseok Seol and Jaesik Choi. "[Context-aware Negative Sampling for Sequential Recommendation\](https://doi.org/10.1109/access.2025.3576124)". *IEEE Access, 2025*.
- Soyeon Kim , Junho Choi , Subeen Lee and Jaesik Choi. "[Example-Based Concept Analysis Framework for Deep Weather Forecast Models\](https://doi.org/10.1175/aies-d-24-0079.1)". *Artificial Intelligence for the Earth Systems (AIES), 2025*.
- Kyowoon Lee , Artyom Stitsyuk , Gunu Jho, Inchul Hwang and Jaesik Choi. "[Counterfactual Activation Editing for Post-hoc Prosody and Mispronunciation Correction in TTS Models\](https://doi.org/10.21437/interspeech.2025-723)". *Annual Conference of the International Speech Communication Association (Interspeech), 2025*.
- Bumjin Park , Jinsil Lee and Jaesik Choi. "Deontological Keyword Bias: The Impact of Modal Verbs on Normative Judgments of Language Models". *Annual Meeting of the Association for Computational Linguistics (ACL), 2025. (채택)*.
- Kyowoon Lee and Jaesik Choi. "Local Manifold Approximation and Projection for Manifold-Aware Diffusion Planning". *International Conference on Machine Learning (ICML), 2025. (채택)*.
- Jiyeon Han \*, Dahee Kwon \*, Gayoung Lee, Junho Kim and Jaesik Choi. "[Enhancing Creative Generation on Stable Diffusion-based Models\](https://doi.org/10.1109/cvpr52734.2025.02664)". *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2025 (\* contributed equally)*.
- Seongyeop Jeong , June Sig Sung, Inchul Hwang and Jaesik Choi. "[An Automated Method to Correct Artifacts in Neural Text-to-Speech Models\](https://doi.org/10.1109/taslpro.2025.3550718)". *IEEE/ACM Transactions on Audio, Speech and Language Processing (T-ASLP), 2025*.
- Junyoung Choi, Gunwook Nam, Jaesik Choi and Yousung Jung. "[A Perspective on Foundation Models in Chemistry\](https://doi.org/10.1021/jacsau.4c01160)". *Journal of the American Chemical Society (JACS AU), 2025*.
- Wonjoon Chang , Myeongjin Lee and Jaesik Choi. "Rethinking Shapley Value for Negative Interactions in Non-convex Games". *International Conference on Learning Representations (ICLR), 2025. (채택)*.
- Anh Tong , Thanh Nguyen-Tang, Dongeun Lee , Duc Nguyen, Toan Tran, David Leo Wright Hall, Cheongwoong Kang and Jaesik Choi. "Neural ODE Transformers: Analyzing Internal Dynamics and Adaptive Fine-tuning". *International Conference on Learning Representations (ICLR), 2025*.
- Artyom Stitsyuk and Jaesik Choi. "[xPatch: Dual-Stream Time Series Forecasting with Exponential Seasonal-Trend Decomposition\](https://doi.org/10.1609/aaai.v39i19.34270)". *AAAI Conference on Artificial Intelligence (AAAI), 2025*.
- Subeen Lee , Jiyeon Han , Soyeon Kim and Jaesik Choi. "Diverse Rare Sample Generation with Pretrained GANs". *AAAI Conference on Artificial Intelligence (AAAI), 2025. (채택)*.

**2024**

- An Nguyen, Jaesik Choi , Anh Tong. "LoCo: Low-rank Compositional Rotation Fine-tuning". *International Joint Conference on Artificial Intelligence (IJCAI), 2024. (연구실 기재)*.
- Jihyeon Seong , Sekwang Oh and Jaesik Choi. "Towards Dynamic Trend Filtering through Trend Point Detection with Reinforcement Learning". *International Joint Conference on Artificial Intelligence (IJCAI), 2024. (연구실 기재)*.
- Bumjin Park and Jaesik Choi. "Memorizing Documents with Guidance in Large Language Models". *International Joint Conference on Artificial Intelligence (IJCAI), 2024. (채택)*.
- Luca Longo, Mario Brcic, Federico Cabitza, Jaesik Choi , Roberto Confalonieri, Javier Del Ser, Riccardo Guidotti, Yoichi Hayashi, Francisco Herrera, Andreas Holzinger, Richard Jiang, Hassan Khosravi, Freddy Lecue, Gianclaudio Malgieri, Andrés Páez, Wojciech Samek, Johannes Schneider, Timo Speith and Simone Stumpf. "[Explainable Artificial Intelligence (XAI) 2.0: A manifesto of open challenges and interdisciplinary research directions\](https://doi.org/10.1016/j.inffus.2024.102301)". *Information Fusion, 2024*.
- Seongwoo Lim , Won Jo , Joohyung Lee and Jaesik Choi. "Pathwise Explanation of ReLU Neural Networks". *International Conference on Artificial Intelligence and Statistics (AISTATS), 2024. (채택)*.
- Jihyeon Seong , Jungmin Kim and Jaesik Choi. "Towards Diverse Perspective Learning with Select over Multiple Temporal Poolings". *AAAI Conference on Artificial Intelligence (AAAI), 2024. (채택)*.
- Wonjoon Chang \*, Dahee Kwon \* and Jaesik Choi. "[Understanding Distributed Representations of Concepts in Deep Neural Networks without Supervision\](https://doi.org/10.1609/aaai.v38i10.28999)". *AAAI Conference on Artificial Intelligence (AAAI), 2024*.
- 김소연 , 성지현 , 한현경, 최재식. "[Capsule Neural Networks as Noise Stabilizer for Time Series Data\](https://doi.org/10.5626/jok.2024.51.8.678)". *정보과학회 논문지(Journal of KIISE), 2024*.

**2023**

- 박범진 , 강청웅 , 최재식. "멀티 에이전트 강화학습에서의 게이트 기반 메시지 교환". *제어·로봇·시스템학회 논문지*.
- Cheongwoong Kang and Jaesik Choi. "[Impact of Co-occurrence on Factual Knowledge of Large Language Models\](https://doi.org/10.18653/v1/2023.findings-emnlp.518)". *Findings of the Association for Computational Linguistics: EMNLP (Findings of EMNLP), 2023*.
- Yeeun Chun , Soonjae Kwon , Kyunghwan Sohn , Nakwon Sung , Junyoup Lee, Byoung Ki Seo, Kevin Compher, Seung-won Hwang and Jaesik Choi. "CR-COPEC: Causal Rationale of Corporate Performance Changes to learn from Financial Reports". *Findings of the Association for Computational Linguistics: EMNLP (Findings of EMNLP), 2023. (채택)*.
- Anh Tong , Thanh Nguyen-Tang, Dongeun Lee , Toan Tran and Jaesik Choi. "[SigFormer: Signature Transformers for Deep Hedging\](https://doi.org/10.1145/3604237.3626841)". *Association for Computing Machinery International Conference on Artificial Intelligence in Finance (ACM ICAIF), 2023*.
- Kyowoon Lee \*, Seongun Kim \* and Jaesik Choi. "Refining Diffusion Planner for Reliable Behavior Synthesis by Automatic Detection of Infeasible Plans". *Conference on Neural Information Processing Systems (NeurIPS), 2023 (\* contributed equally). (채택)*.
- Soyeon Kim , Junho Choi , Yeji Choi, Subeen Lee , Artyom Stitsyuk , Minkyoung Park, Seongyeop Jeong , Youhyun Baek and Jaesik Choi. "[Explainable AI-Based Interface System for Weather Forecasting Model\](https://doi.org/10.1007/978-3-031-48057-7_7)". *International Conference on Human-Computer Interaction International (HCII), 2023*.
- Giyoung Jeon , Haedong Jeong and Jaesik Choi. "[Beyond Single Path Integrated Gradients for Reliable Input Attribution via Randomized Path Sampling\](https://doi.org/10.1109/iccv51070.2023.00196)". *International Conference on Computer Vision (ICCV), 2023*.
- Seongun Kim \*, Kyowoon Lee \* and Jaesik Choi. "Variational Curriculum Reinforcement Learning for Unsupervised Discovery of Skills". *International Conference on Machine Learning (ICML), 2023 (\* contributed equally). (채택)*.
- Jiyeon Han , Hwanil Choi , Yunjey Choi, Junho Kim, Jung-Woo Ha and Jaesik Choi. "Rarity Score : A New Metric to Evaluate the Uncommonness of Synthesized Images". *International Conference on Learning Representations (ICLR), 2023. (채택)*.
- Kyowoon Lee \*, Seongun Kim \* and Jaesik Choi. "[Adaptive and Explainable Deployment of Navigation Skills via Hierarchical Deep Reinforcement Learning\](https://doi.org/10.1109/icra48891.2023.10160371)". *International Conference on Robotics and Automation (ICRA), 2023 (\* contributed equally) (pdf)*.
- 김소연 , 성지현 , 한현경, 최재식. "Capsule Neural Networks as Noise Stabilizer for Time Series Data". *한국컴퓨터종합학술대회(KCC), 2023. (연구실 기재)*.

**2022**

- Jaesik Choi. "South Korea’s Response to Surging AI Use in the US and China". *Global Asia, 17 (4), 2022*.
- Anh Tong , Thanh Nguyen-Tang, Toan Tran and Jaesik Choi. "Learning Fractional White Noises in Neural Stochastic Differential Equations". *Conference on Neural Information Processing Systems (NeurIPS), 2022. (연구실 기재)*.
- Giyoung Jeon \*, Haedong Jeong \* and Jaesik Choi. "Distilled Gradient Aggregation: Purify Features for Input Attribution in the Deep Neural Network". *Conference on Neural Information Processing Systems (NeurIPS), 2022 (\* contributed equally). (연구실 기재)*.
- Hwanil Choi , Wonjoon Chang and Jaesik Choi. "[Can We Find Neurons that Cause Unrealistic Images in Deep Generative Networks?\](https://doi.org/10.24963/ijcai.2022/400)". *International Joint Conference on Artificial Intelligence (IJCAI), 2022*.
- Haedong Jeong , Jiyeon Han and Jaesik Choi. "[An Unsupervised Way to Understand Artifact Generating Internal Units in Generative Neural Networks\](https://doi.org/10.1609/aaai.v36i1.19989)". *AAAI Conference on Artificial Intelligence (AAAI), 2022*.
- Bumjin Park , Cheongwoong Kang , Jaesik Choi. "Cooperative Multi-Robot Task Allocation with Reinforcement Learning". *Applied Sciences, 12 (1), 2022*.
- Cheongwoong Kang , Bumjin Park , Jaesik Choi. "Scheduling PID Attitude and Position Control Frequencies for Time-Optimal Quadrotor Waypoint Tracking under Unknown External Disturbances". *Sensors, 22 (1), 2022*.

**2021**

- Boseon Yu , Jiwoo Lee , Janghoon Ju , Seijun Chung , Soyeon Kim and Jaesik Choi. "Conditional Temporal Neural Processes with Covariance Loss". *International Conference on Machine Learning (ICML), 2021. (연구실 기재)*.

## 연구 과제

최근 5년과 수행 기간이 겹치는 과제다. 날짜는 선정 소식의 게시일이며 수행 기간은 교수 소개의 표기다.[^pi][^news]

- 2022-04-01 · Development of Plug and Play Explainable Artificial Intelligence Platform (기간 2022년 4월부터 57개월; 지원 과학기술정보통신부; 연구비 130억 원; 역할 최재식 교수가 이끎)

## 수상과 선정

2021년 10월 13일–2026년 10월 13일의 수상 소식과 2023년 학회 논문 옆에 게시된 수상 표기를 옮겼다. 2023년 항목의 연도는 학회 표기다.[^news][^pubs]

- 2025-12-01 · 논문 「Explainable Artificial Intelligence (XAI) 2.0: A manifesto of open challenges and interdisciplinary research directions」가 Information Fusion의 Best Paper Award를 받았다.
- 2025-05-27 · 최재식 교수가 공저한 「XAI: Explainable artificial intelligence」가 International Congress of Basic Science의 2025 Frontiers of Science Award 수상 대상으로 선정되었다.
- 2024-10-04 · Nari Kim 교수가 한국 개인정보보호법에 대한 기술적 기여로 개인정보보호위원장상을 받았다.
- 2024-07-05 · Youngju Joung, Sehyun Lee, Jaesik Choi의 「Probing Network Decisions: Capturing Uncertainties and Unveiling Vulnerabilities without Label Information」가 ICPRAI 2024 Best Paper Honorable Mention(입선)을 받았다.
- 2023 · 김소연·성지현·한현경·최재식의 「Capsule Neural Networks as Noise Stabilizer for Time Series Data」가 한국컴퓨터종합학술대회(KCC) 우수논문상을 받았다.
- 2022-06-15 · 설명가능 인공지능 공동 연구가 삼성전자로부터 감사를 받았다.

## 소식

2021년 10월 13일–2026년 10월 13일의 연구실 소식 중 논문 채택·게재 승인·발표와 연구 도구 공개 소식 48건이다. 날짜는 소식 목록의 게시일이다.[^news]

- 2026-07-08 · 논문 「Unified Backbone Refinement for Diffusion Models via Internal-Latent Analysis」: ECCV 2026 채택.
- 2026-07-08 · 논문 「Diffusion Integrated Gradients: Controllable Path Generation for Flexible Feature Attribution」: ECCV 2026 채택.
- 2026-07-08 · 논문 「SPICE: Simple Polysemantic Feature Interpretation via Clustering-based Explanations」: ECCV 2026 채택.
- 2026-05-28 · 논문 「Spectral Integrated Gradients for Coarse-to-Fine Feature Attribution」: KDD 2026 채택.
- 2026-05-04 · 논문 「Manifold-Aligned Guided Integrated Gradients for Reliable Feature Attribution」: ICML 2026 채택.
- 2026-05-02 · 논문 「Breaking the Lock-in: Diversifying Text-to-Image Generation via Representation Modulation」: ICML 2026 채택.
- 2026-05-02 · 논문 「DistMatch: Adaptive Binning via Distribution Matching for Robust Sequential Conformal Prediction」: ICML 2026 채택.
- 2026-04-19 · 논문 「Incomplete Prompt Jailbreaks in Large Language Models」: Findings of ACL 2026 채택.
- 2026-04-19 · 논문 「K-MetBench: A Multi-Dimensional Benchmark for Fine-Grained Evaluation of Expert Reasoning, Locality, and Multimodality in Meteorology」: Findings of ACL 2026 채택.
- 2026-03-20 · 논문 「Towards Transparent Time Series Analysis: Exploring Methods and Enhancing Interpretability」: ACM Computing Surveys 게재 승인.
- 2025-12-19 · 논문 「State-Covering Trajectory Stitching for Diffusion Planners」: NeurIPS 2025 채택.
- 2025-11-20 · 논문 「On the Relationship between Populated Regions and Adversarial Robustness in Deep Neural Networks」: ICDM 2025 채택.
- 2025-10-20 · 논문 「When Format Changes Meaning: Investigating Semantic Inconsistency of Large Language Models」: Findings of EMNLP 2025 채택.
- 2025-09-20 · 논문 「Amortized Baseline Selection via Rank-Revealing QR for Efficient Model Explanation」: CIKM 2025 채택.
- 2025-08-20 · 논문 「Unsupervised Concept Discovery for Deep Weather Forecast Models with High-Resolution Radar Data」: PLOS Climate 게재 승인.
- 2025-07-25 · 논문 「Deep-DFVAR: Dynamic Factor Vector Autoregression with Deep Learning for Regional House Price Index Forecasting」: Neurocomputing 게재 승인.
- 2025-06-29 · 논문 「Granular Concept Circuits: Toward a Fine-Grained Circuit Discovery for Concept Representations」: ICCV 2025 채택.
- 2025-06-03 · 논문 「Example-Based Concept Analysis Framework for Deep Weather Forecast Models」: Artificial Intelligence for the Earth Systems 게재 승인.
- 2025-06-03 · 논문 「Context-aware Negative Sampling for Sequential Recommendation」: IEEE Access 게재 승인.
- 2025-06-01 · 논문 「Counterfactual Activation Editing for Post-hoc Prosody and Mispronunciation Correction in TTS Models」: Interspeech 2025 채택.
- 2025-05-19 · 논문 「Local Manifold Approximation and Projection for Manifold-Aware Diffusion Planning」: ICML 2025 채택.
- 2025-05-17 · 논문 「Deontological Keyword Bias: The Impact of Modal Verbs on Normative Judgments of Language Models」: ACL 2025 채택.
- 2025-02-28 · 논문 「A Perspective on Foundation Models in Chemistry」: Journal of the American Chemical Society (JACS AU) 게재 승인.
- 2025-02-28 · 논문 「An Automated Method to Correct Artifacts in Neural Text-to-Speech Models」: IEEE/ACM Transactions on Audio, Speech and Language Processing 게재 승인.
- 2025-02-28 · 논문 「Enhancing Creative Generation on Stable Diffusion-based Models」: CVPR 2025 채택.
- 2025-02-04 · 논문 「Neural ODE Transformers: Analyzing Internal Dynamics and Adaptive Fine-tuning」: ICLR 2025 채택.
- 2025-02-04 · 논문 「Rethinking Shapley Value for Negative Interactions in Non-convex Games」: ICLR 2025 채택.
- 2025-01-03 · 논문 「xPatch: Dual-Stream Time Series Forecasting with Exponential Seasonal-Trend Decomposition」: AAAI 2025 채택.
- 2025-01-03 · 논문 「Diverse Rare Sample Generation with Pretrained GANs」: AAAI 2025 채택.
- 2024-12-31 · KAIST 설명가능 인공지능연구센터가 모델 구조를 자동으로 감지하고 호환되는 설명 알고리즘을 추천하는 플러그앤플레이 설명 프레임워크를 공개했다.
- 2024-04-26 · 논문 「Memorizing Documents with Guidance in Large Language Models」: IJCAI 2024 채택.
- 2024-04-22 · 논문 「Towards Dynamic Trend Filtering through Trend Point Detection with Reinforcement Learning」: IJCAI 2024 채택.
- 2024-02-20 · 논문 「Explainable Artificial Intelligence (XAI) 2.0: A manifesto of open challenges and interdisciplinary research directions」: Information Fusion 게재 승인.
- 2024-01-20 · 논문 「Pathwise Explanation of ReLU Neural Networks」: AISTATS 2024 채택.
- 2023-12-09 · 논문 「Towards Diverse Perspective Learning with Select over Multiple Temporal Poolings」: AAAI 2024 채택.
- 2023-12-09 · 논문 「Understanding Distributed Representations of Concepts in Deep Neural Networks without Supervision」: AAAI 2024 채택.
- 2023-11-30 · 논문 「Explainable AI-Based Interface System for Weather Forecasting Model」: Human-Computer Interaction International 2023 발표.
- 2023-10-08 · 「CR-COPEC: Causal Rationale of Corporate Performance Changes to learn from Financial Reports」와 「Impact of Co-occurrence on Factual Knowledge of Large Language Models」가 Findings of EMNLP 2023에 채택되었다.
- 2023-09-28 · 논문 「SigFormer: Signature Transformers for Deep Hedging」: ACM ICAIF 2023 채택.
- 2023-09-22 · 논문 「Refining Diffusion Planner for Reliable Behavior Synthesis by Automatic Detection of Infeasible Plans」: NeurIPS 2023 채택.
- 2023-07-15 · 논문 「Beyond Single Path Integrated Gradients for Reliable Input Attribution via Randomized Path Sampling」: ICCV 2023 채택.
- 2023-04-25 · 논문 「Variational Curriculum Reinforcement Learning for Unsupervised Discovery of Skills」: ICML 2023 채택.
- 2023-01-21 · 논문 「Rarity Score : A New Metric to Evaluate the Uncommonness of Synthesized Images」: ICLR 2023 채택.
- 2023-01-18 · 논문 「Adaptive and Explainable Deployment of Navigation Skills via Hierarchical Deep Reinforcement Learning」: ICRA 2023 채택.
- 2022-12-27 · 논문 「South Korea’s Response to Surging AI Use in the US and China」: Global Asia 게재.
- 2022-09-15 · 「Learning White Noises in Neural Stochastic Differential Equations」와 「Distilled Gradient Aggregation: Purify Features for Input Attribution in the Deep Neural Network」가 NeurIPS 2022에 채택되었다.
- 2022-04-23 · 논문 「Can We Find Neurons that Cause Unrealistic Images in Deep Generative Networks?」: IJCAI 2022 채택.
- 2021-12-01 · 논문 「An Unsupervised Way to Understand Artifact Generating Internal Units in Generative Neural Networks」: AAAI 2022 채택.

## 연락과 위치

- 소속: KAIST 김재철AI대학원.[^faculty]
- 교수 사무실: 성남연구센터.[^faculty]
- 교수 이메일: jaesik.choi@kaist.ac.kr.[^faculty]
- 연구실이 게시한 주소: 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea.[^home]
- 교수 소개의 대전 위치: 291 Daehak-ro, N24, Yuseong-gu, Daejeon 34141, Republic of Korea.[^pi]

## 각주
[^home]: 통계적 인공지능 연구실, 첫 화면. <https://sailab.kaist.ac.kr/ko> 관측 2026-11-09.
[^about]: 통계적 인공지능 연구실, 「SAIL 소개」. <https://sailab.kaist.ac.kr/ko/about> 관측 2026-11-09.
[^pi]: 통계적 인공지능 연구실, 「최재식」의 약력·연구 관심 분야·소식. <https://sailab.kaist.ac.kr/ko/members/jaesik> 관측 2026-11-09.
[^faculty]: KAIST 김재철AI대학원, 전임교수 구성원 명단의 최재식 항목. <https://gsai.kaist.ac.kr/people-2/?lang=ko> 관측 2026-11-09.
[^research]: 통계적 인공지능 연구실, 「연구 살펴보기」. 시각 개념 회로·입력 기여도·이미지 생성·음성 수정·행동 계획·시계열·언어 모델의 연구 설명. <https://sailab.kaist.ac.kr/ko/research> 관측 2026-11-09.
[^members]: 통계적 인공지능 연구실, 「구성원」과 「졸업생」. <https://sailab.kaist.ac.kr/ko/members> 관측 2026-11-09.
[^pubs]: 통계적 인공지능 연구실, 「논문」. <https://sailab.kaist.ac.kr/ko/publications> 관측 2026-11-09.
[^news]: 통계적 인공지능 연구실, 「소식과 공지」. <https://sailab.kaist.ac.kr/ko/news> 관측 2026-11-09.
[^p1]: S. Kim, S. Lim, K. Lee, J. Choi, KDD 2026 (채택), arXiv 사전 공개본 (온라인 2026-05-19). <https://doi.org/10.48550/arxiv.2605.19607> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2605.19607> 관측 2026-11-11.
[^p2]: D. Kwon, S. Lee, J. Choi, International Conference on Computer Vision (ICCV), 2025. (2025). <https://doi.org/10.1109/iccv51701.2025.00227> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5052985764,publication_year:2021-2026> 관측 2026-11-11.
[^p3]: K. Lee, J. Choi, ICML 2025, arXiv 사전 공개본 (온라인 2025-06-01). <https://doi.org/10.48550/arxiv.2506.00867> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2506.00867> 관측 2026-11-11.
[^p4]: J. Han 외, J. Choi, IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2025 (* contributed equally). (2025). <https://doi.org/10.1109/cvpr52734.2025.02664> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5052985764,publication_year:2021-2026> 관측 2026-11-11.
[^p5]: K. Lee 외, J. Choi, Annual Conference of the International Speech Communication Association (Interspeech), 2025. (2025). <https://doi.org/10.21437/interspeech.2025-723> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5052985764,publication_year:2021-2026> 관측 2026-11-11.
[^p6]: A. Tong 외, J. Choi, International Conference on Learning Representations (ICLR) (2025). <https://iclr.cc/virtual/2025/poster/29292> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://iclr.cc/virtual/2025/poster/29292> 관측 2026-11-11.
[^p7]: A. Stitsyuk, J. Choi, AAAI Conference on Artificial Intelligence (AAAI), 2025. (2025). <https://doi.org/10.1609/aaai.v39i19.34270> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5052985764,publication_year:2021-2026> 관측 2026-11-11.
[^p8]: S. Kim, J. Choi, S. Lee, J. Choi, Artificial Intelligence for the Earth Systems (AIES), 2025. (2025). <https://doi.org/10.1175/aies-d-24-0079.1> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5052985764,publication_year:2021-2026> 관측 2026-11-11.

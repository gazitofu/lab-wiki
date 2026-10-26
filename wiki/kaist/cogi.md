# 인지지능 연구실 (Cognitive Intelligence Laboratory, Paik Lab)

**KAIST 뇌인지과학과 · 백세범 교수**

- 분야: 계산신경과학, 뇌에서 배운 인공지능(뉴로-AI), 시각 지각, 학습과 기억, 정신물리학
- 대분야: 기초생명·생물물리, 컴퓨팅·AI
- 태그: 계산신경과학[^p5], 뇌 모방 인공지능[^p2][^p1], 인지과학·의사결정[^research], 연속학습[^p7]
- 홈페이지: <https://cogi.kaist.ac.kr/>
- 근거와 출처: [인지지능 연구실 근거 페이지](cogi-sources.md)

> 뇌가 학습하기 전부터 어떻게 지능을 갖추는지를 컴퓨터 모델로 밝히고, 그 원리로 더 효율적으로 배우고 잘 잊지 않는 인공지능을 만드는 계산신경과학 연구실이다.[^research][^bcs][^p1][^p7]

## 무엇을 연구하나

계산신경과학은 수학 모델과 컴퓨터 시뮬레이션으로 뇌의 작동 원리를 연구하는 분야다. 이 연구실은 이론 모델링과 시뮬레이션, 동물 실험 데이터 분석, 뉴로-AI 모델 개발, 사람 대상 지각 실험(정신물리학)을 도구로 쓴다.[^research]

첫 번째 질문은 **"뇌의 기능은 학습 없이도 생길 수 있는가"**다. 연구실은 학습하지 않고 무작위로 연결만 해 둔 인공 신경망에서도 물체 수 세기 같은 인지 기능이 저절로 생긴다는 것을 보였다.[^research] 갓 태어난 동물도 할 수 있는 "비율과 차이로 양 비교하기"가 학습 전의 무작위 회로에서 나타날 수 있음을 모델로 설명했고,[^p4] 초기 시각 경로에서 저절로 생기는 고정된 필터를 신경망 앞단에 넣으면 환경이 바뀌어도 물체를 잘 알아보는 것을 보였다.[^p3]

두 번째 질문은 **뇌 회로가 어떻게 효율적으로 짜이는가**다. 대뇌 시각 피질의 긴 수평 연결이 적은 비용으로 정보를 통합하는 "작은 세상 네트워크"를 만들며, 피질이 일정 크기 이상일 때만 이 연결이 유리하다는 것을 보였다.[^p5] 원숭이·쥐·생쥐의 뇌에서 신경 활동의 시간 척도가 감각 영역에서 연합 영역으로 갈수록 길어지는 공통 구조도 찾았다.[^p6]

세 번째 축은 **뇌의 원리로 인공지능을 개선하는 것**이다. 딥러닝의 표준 학습법(역전파)은 뇌에서는 일어나기 어려운 방식이라, 연구실은 뇌가 경험 전에 자발적 신경 활동으로 회로를 미리 다듬는 것을 본떠 무작위 잡음으로 신경망을 미리 학습시키면 더 빨리, 더 잘 일반화하며 배운다는 것을 보였다.[^p2][^p1] 사람의 작업 기억에서 착안해 새것을 배우면서 옛것을 잊지 않는 연속 학습 모델을 만들었고,[^p7] 아기의 시력이 서서히 발달하는 것이 오히려 편향에 강한 추상적 표현을 배우게 한다는 것을 사람 실험과 함께 보였다.[^p8]

## 주요 연구 주제

### 1. 학습 없이 생기는 인지 기능

무작위 신경망에서 나타나는 수량·물체 인식, 고정 시각 필터.[^p3][^p4] 대표 논문 3, 4.

### 2. 뇌 회로의 자발적 구성

시각 피질 연결 구조와 뇌 영역별 시간 척도.[^p5][^p6] 대표 논문 5, 6.

### 3. 뉴로-AI 학습 알고리즘

역전파 없이 학습하는 방법, 잡음 사전학습.[^p1][^p2] 대표 논문 1, 2.

### 4. 학습과 기억

연속 학습과 점진적 감각 발달.[^p7][^p8] 대표 논문 7, 8.

## 대표 논문

최근 5년 논문 중 교수가 마지막 저자(연구 책임)인 것에서 주제별로 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2026 | [One-Time Soft Alignment Enables Resilient Learning without Weight Transport](https://arxiv.org/abs/2505.20892) · NeurIPS | 역전파 대신 고정된 무작위 피드백으로 배우는 방식에서, 처음에 한 번만 순방향·역방향 가중치를 느슨하게 맞춰 두면 깊은 신경망도 역전파에 버금가게 배우고 공격에도 더 강해졌다.[^p1] | 1저자 Jeonghwan Cheon, 마지막 저자 백세범 |
| 2 | 2024 | [Pretraining with Random Noise for Fast and Robust Learning without Weight Transport](https://doi.org/10.52202/079017-0440) · NeurIPS | 뇌가 경험 전에 잡음 같은 자발적 활동으로 회로를 다듬는 것을 본떠, 신경망을 무작위 잡음으로 먼저 학습시키면 이후 더 빨리 배우고 낯선 데이터에도 잘 일반화했다.[^p2] | 1저자 Jeonghwan Cheon, 마지막 저자 백세범 |
| 3 | 2026 | [Prewired static visual receptive fields for environment-agnostic perception](https://doi.org/10.1016/j.patter.2025.101475) · Patterns | 초기 시각 경로처럼 고정된 필터(가보르 필터)를 신경망 앞단에 두면, 환경이 크게 바뀌어도 잊지 않고 계속 배우며 영장류처럼 모양 위주로 물체를 알아봤다.[^p3] | 1저자 Minjun Kang, 마지막 저자 백세범 |
| 4 | 2023 | [Comparison of visual quantities in untrained neural networks](https://doi.org/10.1016/j.celrep.2023.112900) · Cell Reports | 학습하지 않은 무작위 신경망에서도 두 물체 집단의 비율·차이에 반응하는 뉴런이 저절로 생겨 양 비교 과제를 할 수 있었다.[^p4] | 공동 1저자 Hyeonsu Lee·Woochul Choi, 마지막 저자 백세범 |
| 5 | 2023 | [Species-specific wiring of cortical circuits for small-world networks in the primary visual cortex](https://doi.org/10.1371/journal.pcbi.1011343) · PLOS Computational Biology | 시각 피질의 긴 수평 연결이 "작은 세상 네트워크"를 만들어 적은 비용으로 정보를 통합하며, 피질이 일정 크기를 넘어야 이득이 생겨 종마다 연결 유무가 다르다는 것을 설명했다.[^p5] | 공동 1저자 Seungdae Baek·Youngjin Park, 마지막 저자 백세범 |
| 6 | 2024 | [Hierarchical gradients of multiple timescales in the mammalian forebrain](https://doi.org/10.1073/pnas.2415695121) · PNAS | 원숭이·쥐·생쥐 모두에서 휴식 중 활동과 과제 관련 활동의 시간 척도가 감각 영역에서 연합 영역으로 갈수록 길어지는 같은 위계를 보였다. 시상은 이 순서를 따르지 않았다.[^p6] | 공동 1저자 Min Song·Eun Ju Shin, 공동 교신 D. Lee·M. W. Jung·백세범 |
| 7 | 2025 | [Neuromimetic metaplasticity for adaptive continual learning without catastrophic forgetting](https://doi.org/10.1016/j.neunet.2025.107762) · Neural Networks | 단단한 시냅스와 유연한 시냅스를 섞는 사람 작업 기억 모방 모델로, 추가 처리 없이 새것을 배우면서 옛것을 잊지 않게 했다. 잘못된 데이터 공격에도 강했다.[^p7] | 1저자 Suhee Cho, 마지막 저자 백세범 |
| 8 | 2025 | [Gradual sensory maturation promotes abstract representation learning](https://doi.org/10.1101/2025.06.24.661295) · bioRxiv(프리프린트) | 아기처럼 처음엔 흐리고 색을 잘 못 보는 입력으로 시작해 점점 선명하게 학습한 모델이, 지름길 학습에 빠지지 않고 편향에 강한 추상적 표현을 배웠다. 사람 실험과 행동 패턴이 비슷했다.[^p8] | 1저자 Jeonghwan Cheon, 마지막 저자 백세범 |

## 교수와 전문 분야

백세범 교수는 서울대에서 학사·석사를 받고, 미국 UC 버클리에서 도널드 글레이저(Donald A. Glaser) 교수 지도로 물리학 박사(2009)를 받았다.[^bcs][^people] 2013년 KAIST에 부임해 2021년 정년을 보장받았고 KAIST 특이점 교수(2021–2031)와 지정석좌교수(2026–2029)로 선정됐으며, 2026년 9월 교수로 승진했다.[^bcs][^people][^news] 한국계산신경과학회 회장(2024–), Science Advances 부편집장(2025–)을 맡고 있고, 바이오및뇌공학과 겸직교수 명단에도 있다.[^people][^bioeng] 2013년 포스코 청암과학펠로십을 받았다.[^bcs]

학과는 연구 분야를 계산신경과학, 시스템신경과학, 자연지능·인공지능, 시각 지각, 학습과 기억, 정신물리학으로 적는다.[^bcs] 논문으로 보면 전문 분야는 세 갈래다.

- **시각 회로의 발달과 선천적 기능의 계산 모델**.[^p3][^p4][^p5]
- **뇌 영역 간 동역학**: 신경 활동의 시간 척도.[^p6]
- **생물학적으로 그럴듯한 학습 알고리즘(뉴로-AI)**.[^p1][^p2][^p7][^p8]

## 응용 분야

대표 논문으로 보면 적은 계산으로 학습하는 인공지능, 환경 변화와 데이터 공격에 강한 인식 모델, 잊지 않고 계속 배우는 연속 학습 시스템, 뇌 발달 연구에 닿아 있다.[^p1][^p2][^p3][^p7] 박사 졸업생은 KIST·한국뇌연구원 연구원, MIT 박사후연구원, 스마일게이트 홀딩스 팀장 등으로 진출했다.[^people]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Hyeonbo Yang | 박사후연구원 | hyeonbo@kaist.ac.kr |  |
| Jaehyuk Bae | 석박사통합과정 | qowogur@kaist.ac.kr | 1 |
| Youngil Seo | 석박사통합과정 | lucy0513@kaist.ac.kr |  |
| Aner Zheng | 석박사통합과정 | zhenganer@kaist.ac.kr |  |
| Seungah Kim | 석박사통합과정 | sashrlaa@kaist.ac.kr |  |
| Chaewon Kim | 석박사통합과정 | chaewon@kaist.ac.kr |  |
| Sangmin Lee | 연구원 |  |  |
| Juhyoung Park | 학부 연구생 | juhpark@kaist.ac.kr |  |
| Hyeonsoo Lee | 학부 연구생 |  |  |
| Jinhee Kim | 행정 직원 | kjh77764@kaist.ac.kr |  |

## 졸업생 진로

랩 구성원 페이지의 졸업생·연구원·연구조교 목록이다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Seungdae Baek | Ph.D Alumni | Postdoctoral Researcher |
| Wooyeon Shin | Ph.D Alumni | Postdoctoral Researcher; Korea Institute of Science and Technology (KIST) |
| Hyeonsu Lee | Ph.D Alumni | Postdoctoral Researcher; Korea Institute of Science and Technology (KIST) |
| Gwangsu Kim | Ph.D Alumni | Postdoctoral Researcher; Massachusetts Institute of Technology (MIT) |
| Youngjin Park | Ph.D Alumni | Team manager; Smilegate Holdings |
| Min Song | Ph.D Alumni |  |
| Woochul Choi | Ph.D Alumni | Senior Researcher; Korea Brain Research Institute (KBRI) |
| Jaeson Jang | Ph.D Alumni | Senior Researcher; Korea Institute of Science and Technology (KIST) |
| Jeonghwan Cheon | M.S Alumni | Department of Brain and Cognitive Sciences, KAIST |
| Jaeyoung Lew | M.S Alumni (2023) |  |
| Minsoo Kang | M.S Alumni (2023) |  |
| Changju Lee | M.S Alumni | Public Official |
| Pachaya Sailamul | M.S Alumni |  |
| Soyoung An | M.S Alumni |  |
| Minjun Kang | Researcher Alumni | M.S/Ph.D Student; University of California, San Diego (UCSD) |
| Suhee Cho | Researcher Alumni | Post-bacc Researcher; Stanford University |
| Jinwoo Kim | Researcher Alumni | M.S/Ph.D student; Korea Advanced Institute of Science and Technology (KAIST) |
| Junho Song | Researcher Alumni | Stanford University |
| Yungeun Song | Research Assistant Alumni (2026) |  |
| Matylda Kornacka | Research Assistant Alumni (2026) |  |
| Aysenur Deniz | Research Assistant Alumni (2026) |  |
| Heesung Yang | Research Assistant Alumni (2025) |  |
| Yuseok Oh | Research Assistant Alumni (2025) |  |
| Bui Le Phuong | Research Assistant Alumni (2025) |  |
| Hyung Woo Kim | Research Assistant Alumni (2025) |  |
| Jehyun Herh | Research Assistant Alumni (2024) |  |
| Jaekyoung Lee | Research Assistant Alumni (2024) |  |
| Sieun Kim | Research Assistant Alumni (2024) |  |
| Dongil Lee | Research Assistant Alumni (2022) |  |
| Minseo Bang | Research Assistant Alumni (2021) |  |
| Yongsu Na | Research Assistant Alumni (2020) |  |
| Sejin Kim | Research Assistant Alumni (2019) |  |
| Chaeyoung Moon | Research Assistant Alumni (2019) |  |
| Chanwoong Yoon | Research Assistant Alumni (2019) |  |
| Heng Hui Ye | Research Assistant Alumni (2019) |  |
| Seohui Bae | Research Assistant Alumni (2018) |  |
| Hyoyeon Kim | Research Assistant Alumni (2017) |  |
| Geon Yeong Park | Research Assistant Alumni (2017) |  |
| Hyukjun Lee | Research Assistant Alumni (2017) |  |
| Donghoon Han | Research Assistant Alumni (2017) |  |
| Woosung Jeon | Research Assistant Alumni (2016) |  |
| Jaehoon Shin | Research Assistant Alumni (2016) |  |
| Pornbhussorn Kanchanakanok | Research Assistant Alumni (2015) |  |
| Minha Hwang | Research Assistant Alumni (2015) |  |
| Ji-Eun Lim | Research Assistant Alumni (2015) |  |
| Youhyeon Ko | Research Assistant Alumni (2015) |  |
| Taegyun Kwon | Research Assistant Alumni (2015) |  |
| Soohyun Kim | Research Assistant Alumni (2014) |  |
| Hyunwoo Jang | Research Assistant Alumni (2014) |  |
| Ryukwang Jung | Research Assistant Alumni (2014) |  |
| Seungwon Jeong | Research Assistant Alumni (2013) |  |

## 최근 논문 목록 (2021–2026)

랩 논문 목록에 실린 2021–2026년 항목 27편이다.[^papers] 대표 논문은 위 표에서 쉬운 설명을 붙였다.

**2026**

- Juhyoung Park , Jaehyuk Bae , Hyeonbo Yang , Se-Bum Paik. "Hierarchical Scaffolding Enables Human-Like Cognitive Selectivity under Data Scarcity". *arXiv 2607.04709. (2026)*.
- Jeonghwan Cheon , Jaehyuk Bae , Se-Bum Paik. "One-Time Soft Alignment Enables Resilient Learning without Weight Transport". *Advances in Neural Information Processing Systems (NeurIPS) (2026)*.
- Jeonghwan Cheon , Se-Bum Paik. "Brain-inspired warm-up training with random noise for uncertainty calibration". *Nature Machine Intelligence 8, 602–613. (2026)*.
- M Jeong , Seungdae Baek , Q Wang , L Yao , EJ Lee , AM Rivera , JJ Lee , H Jang , DB-Mukku , C HS Mun , T Boesen , S Nanda , CR Ku , H Dong , B Labonté , Se-Bum Paik† , BK Lim†. "Distinct interneuronal dynamics selectively gate target-specific cortical projections in drug seeking". *Neuron 114, 1-18. (2026)*.
- Minjun Kang , Seungdae Baek , Se-Bum Paik. "Prewired static visual receptive fields for environment-agnostic perception". *Patterns 7(2), 101475. (2026)*.

**2025**

- Jeonghwan Cheon , Se-Bum Paik. "Gradual sensory maturation promotes abstract representation learning". *bioRxiv 2025.06.24.661295. (2025)*.
- M Kang , S Kim , W Shin , K Kim , Y Jung , Woochul Choi , Se-Bum Paik , E Kim. "Grin2b-mutant mice exhibit heightened remote fear via suppressed extinction and chronic amygdalar synaptic and neuronal dysfunction". *Science Advances 11(38), eadr7691. (2025)*.
- Suhee Cho , Hyeonsu Lee , Seungdae Baek , Se-Bum Paik. "Neuromimetic metaplasticity for adaptive continual learning without catastrophic forgetting". *Neural Networks 190, 107762. (2025)*.

**2024**

- Se-Bum Paik. "Split-second insights from the brain's dual-stream visual system". *Neuron 112(24), 3991-3993. (2024)*.
- Min Song\* , EJ Shin\* , H Seo , A Soltani , NA Steinmetz , D Lee† , MW Jung† , Se-Bum Paik†. "Hierarchical gradients of multiple timescales in the mammalian forebrain". *Proceedings of the National Academy of Sciences 121(51), e2415695121. (2024)*.
- G Son , Y Na , Y Kim , JH Son , GD Clemenson , ST Schafer , JY Yoo , SL Parylak , A Paquola , H Do , D Kim , I Ahn , M Ju , CS Kang , Y Ju , E Jung , McDonald AH , Youngjin Park , G Kim , Se-Bum Paik , J Hur , J Kim , YM Han , SH Lee , FH Gage , JS Kim , J Han. "miR-124 coordinates metabolic regulators acting at early stages of human neurogenesis". *Communications Biology 7(1), 1393. (2024)*.
- Jeonghwan Cheon , SW Lee , Se-Bum Paik. "Pretraining with random noise for fast and robust learning without weight transport". *Advances in Neural Information Processing Systems (NeurIPS) 37, 13748-13768. (2024)*.

**2023**

- Hyeonsu Lee\* , Woochul Choi\* , Dongil Lee , Se-Bum Paik. "Comparison of visual quantities in untrained neural networks". *Cell Reports 42(8), 112900. (2023)*.
- Seungdae Baek\* , Youngjin Park\* , Se-Bum Paik. "Species-specific wiring of cortical circuits for small-world networks in the primary visual cortex". *PLOS Computational Biology 19(8), e1011343. (2023)*.
- B Ko , JY Yoo , T Yoo , Woochul Choi , R Dogan , K Sung , D Um , SB Lee , HJ Kim , S Lee , ST Baek , SK Park , Se-Bum Paik , TK Kim , JH Kim. "Npas4-mediated dopaminergic regulation of safety memory consolidation". *Cell Reports 42(7), 112678. (2023)*.
- H Oh , S Lee , Y Oh , S Kim , YS Kim , Y Yang , Woochul Choi , YE Yoo , H Cho , S Lee , E Yang , W Koh , W Won , R Kim , C.J. Lee , H Kim , H Kang , JY Kim , T Ku , Se-Bum Paik , E Kim. "Kv7/KCNQ potassium channels in cortical hyperexcitability and juvenile seizure-related death in Ank2-mutant mice". *Nature Communications 14, 3547. (2023)*.

**2022**

- W Kim , JJ Shin , YJ Jeong , K Kim , JW Bae , YW Noh , S Lee , Woochul Choi , Se-Bum Paik , MW Jung , E Lee , E Kim. "Suppressed prefrontal neuronal firing variability and impaired social representation in IRSp53-mutant mice". *eLife 11, e74998. (2022)*.
- Jeonghwan Cheon\* , Seungdae Baek\* , Se-Bum Paik. "Invariance of object detection in untrained deep neural networks". *Frontiers in Computational Neuroscience 16, 1030707. (2022)*.

**2021**

- Seungdae Baek\* , Min Song\* , Jaeson Jang , Gwangsu Kim , Se-Bum Paik. "Face detection in untrained deep neural networks". *Nature Communications 12, 7328. (2021)*.
- Gwangsu Kim , Jaeson Jang , Se-Bum Paik. "Periodic clustering of simple and complex cells in visual cortex". *Neural Networks 143, 148-160. (2021)*.
- Lee E\* , Lee S\* , Shin JJ\* , Woochul Choi\* , C Chung , S Lee , J Kim , S Ha , R Kim , T Yoo , YE Yoo , J Kim , I Rhim , SY Lee , YW Noh , W Kim , T Lee , H Shin , IJ Cho , Deisseroth K , SJ Kim , J Park† , MW Jung† , Se-Bum Paik† , E Kim†. "Excitatory synapses and gap junctions cooperate to improve Pv neuronal burst firing and cortical social cognition in Shank2-mutant mice". *Nature Communications 12, 5116. (2021)*.
- M Jeong\* , Hyeonsu Lee\* , Y Kim , E Wang , Se-Bum Paik† , BK Lim† , D Kim†. "Interhemispheric cortico-cortical pathway for sequential bimanual movements in mice". *eNeuro 8(4), ENEURO.0200-21.2021. (2021)*.
- JW Bae\* , H Jeong\* , YJ Yoon , C Bae , Hyeonsu Lee , Se-Bum Paik , MW Jung. "Parallel processing of working memory and temporal information by distinct types of cortical projection neurons". *Nature Communications 12, 4352. (2021)*.
- Koh HY\* , Jaeson Jang\* , Ju SH\* , R Kim , GB Cho , DS Kim , JW Sohn† , Se-Bum Paik† , JH Lee†. "Non-cell autonomous epileptogenesis in focal cortical dysplasia". *Annals of Neurology 1-15. (2021)*.
- Youngjin Park\* , Seungdae Baek\* , Se-Bum Paik. "A brain-inspired network architecture for cost-efficient object recognition in shallow hierarchical neural networks". *Neural Networks 134, 76-85. (2021)*.
- Min Song\* , Jaeson Jang\* , Gwangsu Kim , Se-Bum Paik. "Projection of orthogonal tiling from the retina to the visual cortex". *Cell Reports 34(1), 108581. (2021)*.
- Gwangsu Kim\* , Jaeson Jang\* , Seungdae Baek , Min Song , Se-Bum Paik. "Visual number sense in untrained deep neural networks". *Science Advances 7(1), eabd6127. (2021)*.

## 수상과 소식

랩 소식 게시판의 최근 항목(원문)이다.[^news]

- Sep 25, 2026 · [Publication] Jeonghwan Cheon (M.S.) & Jaehyuk Bae (Ph.D. Candidate) published a paper in NeurIPS 2026
- Sep 1, 2026 · [News] Prof. Se-Bum Paik has been appointed as a Full Professor
- Jul 6, 2026 · [Notice] 2026 Annual Meeting of the Korean Society for Computational Neuroscience (~8/28)
- Apr 27, 2026 · [Publication] Jeonghwan Cheon (M.S.) published a paper in Nature Machine Intelligence
- Mar 9, 2026 · [Publication] Seungdae Baek (Ph.D.) published a paper in Neuron
- Mar 1, 2026 · [News] Prof. Se-Bum Paik has been appointed as a KAIST Endowed Chair Professor
- Dec 18, 2025 · [Notice] 2026 Computational Neuroscience Winter School (~1/9)
- Nov 15, 2025 · [Conference] COGI in SfN 2025
- Aug 27, 2025 · [Awards] Seungdae Baek (Ph.D.) received the Outstanding Poster Award at KSBNS 2025
- Jul 18, 2025 · [Awards] Jeonghwan Cheon (M.S. Candidate) received the Outstanding Poster Award at Cbrain 2025

## 연락과 위치

- 이메일: sbpaik@kaist.ac.kr[^people][^bcs]
- 전화: 042-350-6513, 6573(랩 표기)[^people]
- 연구실: KAIST 기초과학연구원 캠퍼스(E22) A202-1호(랩 표기), 학과 표기 E22 A202-2호[^people][^bcs]

[^research]: 랩 연구 페이지 <https://cogi.kaist.ac.kr/research/> (2026-10-19 열람)
[^people]: 랩 구성원 페이지 <https://cogi.kaist.ac.kr/people/> (2026-10-19 열람)
[^papers]: 랩 논문 목록 <https://cogi.kaist.ac.kr/publication/> (2026-10-19 열람)
[^news]: 랩 소식 게시판 <https://cogi.kaist.ac.kr/news/> (2026-10-19 열람)
[^bcs]: KAIST 뇌인지과학과 교수 소개 <https://bcs.kaist.ac.kr/sub020101/view/id/114> (2026-10-19 열람)
[^bioeng]: KAIST 바이오및뇌공학과 교수 명단 <https://bioeng.kaist.ac.kr/index.php?mid=bio_03_01&category=8952> (2026-10-19 열람)
[^p1]: J. Cheon, J. Bae, S.-B. Paik, "One-Time Soft Alignment Enables Resilient Learning without Weight Transport", NeurIPS 2026(랩 표기). arXiv:2505.20892 <https://arxiv.org/abs/2505.20892> 초록 기준(arXiv 판).
[^p2]: J. Cheon, S. W. Lee, S.-B. Paik, Advances in Neural Information Processing Systems 37, 13748-13768 (2024). <https://doi.org/10.52202/079017-0440>, NeurIPS 논문 페이지 <https://proceedings.neurips.cc/paper_files/paper/2024/hash/18d3a2f3068d6c669dcae19ceca1bc24-Abstract-Conference.html> 게시 초록 기준.
[^p3]: M. Kang, S. Baek, S.-B. Paik, Patterns 7, 101475 (2026). <https://doi.org/10.1016/j.patter.2025.101475> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: H. Lee, W. Choi, D. Lee, S.-B. Paik, Cell Reports 42, 112900 (2023). <https://doi.org/10.1016/j.celrep.2023.112900> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: S. Baek, Y. Park, S.-B. Paik, PLOS Computational Biology 19, e1011343 (온라인 2023-08-04). <https://doi.org/10.1371/journal.pcbi.1011343> 초록 기준.
[^p6]: M. Song 외, S.-B. Paik, Proceedings of the National Academy of Sciences 121, e2415695121 (온라인 2024-12-13). <https://doi.org/10.1073/pnas.2415695121> 초록 기준.
[^p7]: S. Cho, H. Lee, S. Baek, S.-B. Paik, Neural Networks 190, 107762 (2025). <https://doi.org/10.1016/j.neunet.2025.107762> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: J. Cheon, S.-B. Paik, bioRxiv 2025.06.24.661295 (2025, 프리프린트). <https://doi.org/10.1101/2025.06.24.661295> 초록 기준.

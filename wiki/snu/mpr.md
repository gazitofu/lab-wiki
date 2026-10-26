# 기계 인지 및 추론 연구실 (SNU Machine Perception and Reasoning Lab.)

**서울대학교 공과대학 전기·정보공학부, 대학원 협동과정 인공지능전공 · 최종현 부교수**

- 분야: 컴퓨터 비전, 머신러닝, 멀티모달 인공지능, 자연어 처리, 지속 학습, 시각·언어 기반 로봇 행동
- 대분야: 컴퓨팅·AI
- 태그: 컴퓨터 비전[^p7], 멀티모달 AI[^intro][^p5], 강화학습[^p5], 생성 인공지능[^p7], 대형 언어 모델[^p8]
- 홈페이지: <https://ppolon.github.io/>
- 연구실 홈페이지: <https://mpr.snu.ac.kr/>
- 근거와 출처: [기계 인지 및 추론 연구실 근거 페이지](mpr-sources.md)

> 사진·영상과 언어를 함께 이해하는 인공지능을 연구하며, 학습에 필요한 자료와 계산을 줄이고 변화하는 환경에 맞춰 지식과 행동을 조정하는 방법을 개발하는 연구실이다.[^intro][^lab-en][^p1][^p3]

## 무엇을 연구하나

이 연구실은 최종현 부교수가 이끈다. 학과는 컴퓨터 비전(컴퓨터로 사진·영상의 내용을 알아보는 분야), 머신러닝(자료에서 규칙을 배워 예측이나 판단을 하는 방법), 멀티모달 인공지능(영상·글·소리처럼 종류가 다른 자료를 함께 다루는 인공지능), 자연어 처리(사람의 언어를 컴퓨터가 분석하고 만들어 내는 분야)를 연구 분야로 적는다.[^lab] 교수는 여러 종류의 자료를 다루는 인지 모델·알고리즘·시스템을 개발하되, 정답을 붙이는 비용과 학습·추론의 계산량을 함께 고려한다고 설명한다. 모델은 자료의 관계나 규칙을 나타내는 계산 체계이며, 학습은 자료를 바탕으로 그 체계를 조정하는 과정, 추론은 학습한 체계로 새 입력의 답이나 행동을 계산하는 과정이다.[^intro]

첫 갈래는 **영상과 언어를 함께 이해하는 모델**이다. 영상에 관한 질문에 답하려면 글에 드러난 요청과 실제 장면을 연결해야 한다. 연구실의 영상·언어 모델 연구는 인공지능이 스스로 만든 선호 피드백(후보 답변에 대한 선택이나 선호를 담은 평가 정보)을 강화학습(보상을 바탕으로 행동 방식을 배우는 방법)에 사용해 영상 내용과 답변을 맞추는 방법을 제안했다.[^p5] 다른 연구는 영상의 사건 순서를 평가하는 자료를 만들고, 사건별 설명을 이용한 학습과 답에 이르는 단계를 제시하도록 하는 지시를 결합했다.[^p6]

둘째 갈래는 **변화하는 자료를 계속 배우는 방법**이다. 지속 학습은 새로운 자료나 과제를 차례로 배우면서 이전에 배운 지식도 유지하려는 학습 방식이다. 계산량과 저장 공간을 같은 예산으로 맞춰 학습 방법을 비교하고, 필요에 따라 모델 일부의 갱신을 멈추거나 저장된 자료를 다시 고르는 방법을 연구한다.[^p3] 새 지시와 답변 예시가 계속 들어오는 상황에서는 이미 본 자료를 기준으로 새 표본(전체 자료에서 골라 다루는 개별 항목)의 정보량과 중복을 평가해 학습 대상을 고른다.[^p4]

셋째 갈래는 **주변을 보고 지시에 따라 행동하는 로봇 모델**이다. 시각-언어-행동 모델(Vision-Language-Action model, VLA)은 시각 관측과 언어 지시를 바탕으로 행동을 계산하는 모델이다. 연구실은 모델이 판단에 확신을 갖지 못하는 정도에 따라 보는 방식과 행동 선택을 함께 조절하는 방법을 제안했다.[^p1] 카메라의 자세나 로봇이 달라지는 상황에는 시연(사람 등이 과제 수행 방법을 보여 주는 자료) 하나로 모델을 적응시키는 방법도 연구했다.[^p2]

넷째 갈래는 **생성 모델을 실행하고 조절하는 방법**이다. 생성 모델은 배운 자료의 분포(가능한 값이나 유형마다 나타날 비중을 나타낸 것)를 바탕으로 새 자료를 만드는 계산 체계다. 확산 모델(자료에 잡음을 더하고 제거하는 과정을 이용하는 생성 모델)로 그림을 다른 그림으로 바꿀 때 필요한 계산을 줄이는 방법을 개발했다.[^p7] 글을 다루는 대형 언어 모델(Large Language Model, LLM, 많은 글에서 언어의 관계를 배워 글을 처리하고 만드는 모델)의 안전 연구에서는 유해 행동과 관련된 내부 표현(입력이나 상태의 특징을 수로 나타낸 것)을 조절하는 학습 방법을 제안했다.[^p8]

## 주요 연구 주제

### 영상·언어 모델의 내용 연결과 사건 순서

「Tuning Large Multimodal Models for Videos using Reinforcement Learning from AI Feedback」는 영상의 상세한 설명을 선호 피드백 생성의 맥락으로 사용한다. 인공지능 피드백 기반 강화학습(Reinforcement Learning from AI Feedback, RLAIF)을 통해 모델의 답변을 영상 내용과 맞추는 접근이다.[^p5] 「What Happens When」은 기존 평가에서 영상 프레임(동영상을 이루는 개별 정지 영상)의 순서를 뒤섞어도 모델이 좋은 결과를 낼 수 있음을 관찰했다. 사건 순서를 직접 평가하는 VECTOR를 제안하고, 사건별 설명으로 학습한 뒤 추론 과정에서 단계별 사고를 요구하는 지시를 사용하는 MECOT(Multi-Event instruction fine-tuning with Chain-of-Thought)를 제안했다.[^p6]

### 제한된 자원에서 계속 배우기

지속 학습 연구는 단순히 같은 횟수로 학습시키는 것과 실제 계산·저장 예산이 같다는 것을 구분한다. 「Budgeted Online Continual Learning」은 연산량과 전체 저장 용량으로 예산을 맞추고, 정보가 적은 자료 묶음에서는 모델의 일부 층(계산이 단계적으로 이어지는 모델의 구성 부분)을 갱신하지 않는 방법을 제안했다. 과거 자료를 다시 꺼내 학습하는 방법도 함께 다룬다.[^p3] OASIS(Online Sample Selection for Continual Instruction Tuning)는 새로 도착한 지시 데이터가 이전 자료에 비해 얼마나 정보를 더하는지 평가하고, 선택 점수를 반복 갱신해 비슷한 표본의 중복 선택을 줄인다.[^p4]

### 환경 변화에 적응하는 시각·언어 기반 행동

SCALE(Self-uncertainty Conditioned Adaptive Looking and Execution)은 자기 불확실성을 이용해 시각 인지와 행동을 함께 조절한다. 확신이 낮을 때는 여러 가능성을 탐색하고, 확신이 있을 때는 선택을 집중한다. 추가 학습이나 별도의 검증 모델 없이 한 번의 모델 계산으로 작동하도록 제안했다.[^p1] DART(Domain ARiThmetic)는 카메라 자세나 로봇이 바뀐 환경에 적응할 때, 환경 고유의 정보를 모델의 가중치(각 계산 요소가 결과에 기여하는 정도를 정하는 값)에서 분리해 더하는 방법이다. 초록은 시연 하나만 수집해 적응시키는 설정을 명시한다.[^p2]

### 생성 과정의 계산과 언어 모델 안전

DBMSolver는 그림 변환에 사용하는 확산 브리지 모델(Diffusion Bridge Model, 두 자료 분포 사이의 변환을 확산 과정으로 나타내는 모델)의 방정식 구조를 이용해, 추가 학습 없이 생성 계산을 수행하는 방법이다.[^p7] RepBend(Representation Bending)는 모델의 추론 중 내부 계산값을 조절하는 아이디어를 미세 조정(이미 학습한 모델을 추가 자료나 목적에 맞춰 더 학습시키는 과정)에 도입했다. 유해 행동과 관련된 표현을 바꾸어 언어 모델의 안전성을 높이려는 연구다.[^p8]

## 대표 논문

교수 누리집에 올라 있는 논문 중 2024년 3월 서울대 부임 이후 시기에 발표된 8편을 네 연구 갈래에서 골랐다. 모든 논문에서 최종현은 마지막 저자이며, 마지막 저자라는 사실을 교신저자라는 뜻으로 해석하지 않았다. 연도와 학회는 교수 누리집·학과·서지 기록의 발표 연도를 따르며, 아래의 쉬운 설명은 각주에 밝힌 초록만을 근거로 썼다. arXiv 초록을 쓴 5편은 초록 페이지가 해당 학회를 직접 명시한다.[^cv][^bib]

| 번호 | 연도 | 논문 | 쉽게 말하면 | 교수의 참여 |
|---|---|---|---|---|
| 1 | 2026 | [SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models](https://arxiv.org/abs/2602.04208) · ICML | 로봇 모델이 스스로 느끼는 불확실성에 따라 장면을 살피는 방식과 행동 선택을 함께 조절한다. 추가 학습이나 별도의 검증 모델 없이 한 번의 계산으로 실행하는 방법이다.[^p1] | 마지막 저자 |
| 2 | 2026 | [Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts](https://arxiv.org/abs/2607.00666) · ECCV | 카메라 자세나 로봇이 바뀌었을 때 시연 하나를 이용해 모델을 적응시킨다. 모델 가중치에서 환경 고유 정보를 구분해 더하는 방법을 제안했다.[^p2] | 마지막 저자 |
| 3 | 2025 | [Budgeted Online Continual Learning by Adaptive Layer Freezing and Frequency-based Sampling](https://arxiv.org/abs/2410.15143) · ICLR | 지속 학습 방법들을 같은 계산·저장 예산 안에서 비교한다. 정보가 적은 자료 묶음에서는 모델 일부의 갱신을 멈추고, 과거 자료를 다시 고르는 방법을 개선했다.[^p3] | 마지막 저자 |
| 4 | 2026 | [OASIS: Online Sample Selection for Continual Instruction Tuning](https://doi.org/10.18653/v1/2026.acl-long.158) · ACL | 지시 데이터가 계속 들어올 때 이전에 본 자료를 기준으로 정보가 있는 예시를 고른다. 선택 점수를 반복 갱신해 학습할 예시 사이의 정보 중복도 줄인다.[^p4] | 마지막 저자 |
| 5 | 2024 | [Tuning Large Multimodal Models for Videos using Reinforcement Learning from AI Feedback](https://doi.org/10.18653/v1/2024.acl-long.52) · ACL | 인공지능이 스스로 만든 선호 피드백으로 영상·언어 모델을 학습한다. 피드백을 만들 때 영상의 자세한 설명을 함께 넣어 답변이 영상 내용에 맞도록 한다.[^p5] | 마지막 저자 |
| 6 | 2026 | [What Happens When: Learning Temporal Orders of Events in Videos](https://arxiv.org/abs/2512.08979) · WACV | 영상 속 여러 사건의 순서를 모델이 이해하는지 평가하는 자료를 제안했다. 사건별 설명을 이용한 학습과 단계별 사고를 요구하는 추론 지시로 시간 순서 이해를 개선했다.[^p6] | 마지막 저자 |
| 7 | 2026 | [DBMSolver: A Training-free Diffusion Bridge Sampler for High-Quality Image-to-Image Translation](https://arxiv.org/abs/2605.05889) · CVPR | 그림을 다른 그림으로 바꾸는 확산 모델의 방정식 구조를 이용한다. 별도 학습 없이 생성 과정의 계산 횟수를 줄이는 방법을 제안하고 그림 채우기와 화풍 변환 등에 평가했다.[^p7] | 마지막 저자 |
| 8 | 2025 | [Representation Bending for Large Language Model Safety](https://doi.org/10.18653/v1/2025.acl-long.1173) · ACL | 대형 언어 모델에서 유해 행동과 관련된 내부 표현을 바꾸는 추가 학습 방법이다. 안전장치를 우회하는 여러 공격에 대해 평가하고 유용성과 안전성을 함께 살폈다.[^p8] | 마지막 저자 |

## 교수와 전문 분야

최종현(Jonghyun Choi)은 서울대학교 공과대학 전기·정보공학부 부교수이며, 대학원 협동과정 인공지능전공의 교무부주임으로도 소개된다.[^prof][^gsai] 2024년 3월 서울대에 부임했다. 이전에는 연세대학교 인공지능학과 부교수(2022년 3월–2024년 2월), 광주과학기술원 조교수(2018년 8월–2022년 2월), 앨런 인공지능 연구소 연구원 등으로 일했다. 메릴랜드 주립대학교에서 2015년 박사 학위를, 서울대학교에서 2008년 석사 학위와 2003년 학사 학위를 받았다.[^cv][^prof]

교수의 소개는 컴퓨터 비전·자연어 처리·머신러닝을 이용해 실용적인 멀티모달 인지 시스템을 만드는 일을 연구 관심으로 적는다.[^intro] 대표 논문으로 보면 영상 내용과 언어 답변을 연결하는 학습, 순서가 있는 사건 이해, 제한된 계산 자원을 고려한 지속 학습, 환경 변화에 적응하는 로봇 행동 모델이 전문 분야의 축을 이룬다.[^p1][^p2][^p3][^p4][^p5][^p6] 생성 과정의 계산 방법과 대형 언어 모델의 안전성도 다룬다.[^p7][^p8]

## 응용 분야

대표 논문이 직접 다룬 대상은 영상 질의응답과 사건 순서 이해,[^p5][^p6] 계속 도착하는 지시 데이터로 모델을 학습하는 상황,[^p4] 시각 관측과 언어 지시를 이용하는 로봇 행동,[^p1][^p2] 그림의 비어 있는 부분 채우기·화풍 변환·의미 정보를 그림으로 바꾸는 작업,[^p7] 대형 언어 모델의 유해 출력과 안전장치 우회 공격에 대한 방어다.[^p8]

## 최근 5년 논문 목록

교수 누리집의 2021–2026년 구역과 Preprints 구역의 2026년 사전 공개본을 담은 교수 개인 목록이며 부임 전 항목이 섞여 있다. 최종현 교수의 서울대 부임 시점은 2024년 3월이다. 학술지·학회·워크숍명과 연도는 누리집 표기다. Preprints 구역의 두 항목은 arXiv 사전 공개본으로, To appear라고 적힌 세 항목은 출판예정으로 표시했다. 다른 항목도 논문 링크가 arXiv 판일 수 있다. 저자 이름의 별표는 누리집 표시 그대로다.[^bib][^cv]

**2026**

- Young-Jun Lee, Jinheon Baek\*, Soyeong Jeong\*, Minki Kang\*, Seungyeon Jwa, Jonghyun Choi , Seungho Han, Dongyeop Kang. "EVODUET: Bilevel Co-Evolution of Web Searching and Task Solving for Scientific Discovery". *arXiv 2609 (arXiv 사전 공개본)*.
- San Kim, Daechul Ahn, Reokyoung Kim, Hyeonbeom Choi, Seungyeon Jwa, Jonghyun Choi. "RTSGameBench: An RTS Benchmark for Strategic Reasoning by Vision-Language Models". *arXiv 2606 (arXiv 사전 공개본)*.
- Minhyuk Seo, Minjae Lee, Chaeeun Lee, Wei Lin, Muhammad Jehanzeb Mirza, Tinne Tuytelaars, Jonghyun Choi. "Visual Grounding First, Multimodal In-context Learning Follows". *NeurIPS 2026 (To appear) (출판예정)*.
- Sanghyun Hahn, Jonghyun Choi. "Action Chunking Proximal Policy Optimization with Feedback Correction". *NeurIPS 2026 (To appear) (출판예정)*.
- Jisu Jeon, Seungyeon Jwa, Joosung Lee, Jinhyeon Kim, Woojin Chung, Hwiyeol Jo, Jeonghoon Kim, Jonghyun Choi , Soyoon Kim. "ParaPairAudioBench: Paralinguistic Pairwise Audio Benchmark for LALM-as-a-Judge". *Interspeech 2026 (To appear) (출판예정)*.
- Taewook Kang\*, Taeheon Kim\*, Donghyun Shin, Jonghyun Choi. "Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts". *ECCV 2026*.
- Sanghyun Jo, Wooyeol Lee, Ziseok Lee, Jonghyun Choi , Jaesik Park, Kyungsu Kim. "ISAC: Training-Free Instance-to-Semantic Attention Control for Multi-Instance Generation". *ECCV 2026*.
- Jonghyun Park, Minhyuk Seo, Chaewon Yeo, Jonghyun Choi. "Risk-adaptive Activation Steering for Safe Multimodal Large Language Models". *ECCV 2026 / CIKM 2025 Workshop of HCAI (Oral) Best Paper Award*.
- Vaggelis Dorovatas, Malte Schwerin, Andrew D. Bagdanov, Lucas Caccia, Antonio Carta, Laurent Charlin, Barbara Hammer, 
          Tyler L. Hayes, Timm Hess, Christopher Kanan, Dhireesha Kudithipudi, Xialei Liu, Vincenzo Lomonaco, Jorge Mendez-Mendez, Darshan Patil, 
          Ameya Prabhu, Elisa Ricci, Tinne Tuytelaars, Gido M. van de Ven, Liyuan Wang, Joost van de Weijer, Jonghyun Choi , Martin Mundt, Rahaf Aljundi. "Modular Memory is the Key to Continual Learning Agents". *ICML 2026 - (Position) (Spotlight)*.
- Hyeonbeom Choi, Daechul Ahn, Youhan Lee, Taewook Kang, Seongwon Cho, Jonghyun Choi. "SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models". *ICML 2026 (Spotlight)*.
- Minjae Lee, Minhyuk Seo, Tingyu Qu, Tinne Tuytelaars, Jonghyun Choi. "OASIS: Online Sample Selection for Continual Visual Instruction Tuning". *ACL 2026*.
- Sankarshana Venugopal, Mohammad Mostafavi, Jonghyun Choi. "FALCON: Fast Adaptive Lightweight Computation of Intensities and Events for Depth Estimation". *CVPR 2026 - Findings*.
- Sankarshana Venugopal, Mohammad Mostafavi, Jonghyun Choi. "DBMSolver: A Training-free Diffusion Bridge Sampler for High-Quality Image-to-Image Translation". *CVPR 2026*.
- Seongwon Cho, Daechul Ahn, Donghyun Shin, Hyeonbeom Choi, San Kim, Jonghyun Choi. "BINDER: Instantly Adaptive Mobile Manipulation with Open-Vocabulary Commands". *ICRA 2026*.
- Sanghyun Jo, Ziseok Lee, Wooyeol Lee, Jonghyun Choi , Jaesik Park, Kyungsu Kim. "TRACE: Your Diffusion Model is Secretly an Instance Edge Detector". *ICLR 2026 (Oral)*.
- Minhyuk Seo, Taeheon Kim, Hankook Lee, Jonghyun Choi , Tinne Tuytelaars. "Co-LoRA: Collaborative Model Personalization on Heterogeneous Multi-Modal Clients". *ICLR 2026 / AAAI 2026 Workshop of PerFM (Oral) Best Paper Award*.
- Seungyeon Jwa, Daechul Ahn, Reokyoung Kim, Dongyeop Kang, Jonghyun Choi. "Becoming Experienced Judges: Selective Test-Time Learning for Evaluators". *EACL 2026 (Short) (Oral) / ACL 2026 Eval Eval Workshop (Oral)*.
- Daechul Ahn, Yura Choi, Hyeonbeom Choi, Seongwon Cho, San Kim, Jonghyun Choi. "What Happens When: Learning Temporal Order of Events in Videos". *WACV 2026*.
- Dongjae Jeon, Wonje Jeung, Taeheon Kim, Albert No, Jonghyun Choi. "An Information Theoretic Evaluation Metric for Strong Unlearning". *AAAI 2026*.

**2025**

- Minhyuk Seo, Seongwon Cho, Minjae Lee, Diganta Misra, Hyeonbeom Choi, Seon Joo Kim, Jonghyun Choi. "GenOL: Generating Diverse Examples for Name-only Online Learning". *TMLR 2025*.
- Leekyeung Han, Hyunji Min, Gyeom Hwangbo, Jonghyun Choi , Paul Hongsuck Seo. "DialNav: Multi-turn Dialog Navigation with a Remote Guide". *ICCV 2025*.
- Hyung Rok Jung, Daneul Kim, Seunggyun Lim, Jeany Son, Jonghyun Choi. "Online Generic Event Boundary Detection". *ICCV 2025*.
- Daechul Ahn\*, San Kim\*, Jonghyun Choi. "Society of Mind Meets Real-Time Strategy: A Hierarchical Multi-Agent Framework for Strategic Reasoning". *COLM 2025*.
- Ashkan Yousefpour\*, Taeheon Kim\*, Ryan S. Kwon, Seungbeen Lee, Wonje Jeung, Seungju Han, Alvin Wan, Harrison Ngan, Youngjae Yu, Jonghyun Choi. "Representation Bending for Large Language Model Safety". *ACL 2025*.
- Wonje Jeung, Dongjae Jeon, Ashkan Yousefpour, Jonghyun Choi. "Large Language Models Still Exhibit Bias in Long Text". *ACL 2025 - Findings*.
- Minhyuk Seo, Hyunseo Koh, Jonghyun Choi. "Budgeted Online Continual Learning by Adaptive Layer Freezing and Frequency-based Sampling". *ICLR 2025 (Spotlight)*.
- Taewoong Kim, Byeonghwi Kim, Jonghyun Choi. "Multi-Modal Grounded Planning and Efficient Replanning For Learning Embodied Agents with A Few Examples". *AAAI 2025 (Oral)*.
- Daechul Ahn, Yura Choi, San Kim, Youngjae Yu, Dongyeop Kang, Jonghyun Choi. "ISR-DPO: Aligning Large Multimodal Models for Videos by Iterative Self-Retrospective DPO". *AAAI 2025*.
- Kanghyun Choi, Hyeyoon Lee, Dain Kwon, SunJong Park, Kyuyeun Kim, Noseong Park, Jonghyun Choi , Jinho Lee. "MimiQ: Low-Bit Data-Free Quantization of Vision Transformers with Encouraging Inter-Head Attention Similarity". *AAAI 2025*.

**2024**

- Jinyeon Kim, Cheolhong Min, Byeonghwi Kim, Jonghyun Choi. "Pre-emptive Action Revision by Environmental Feedback for Embodied Instruction Following Agents". *CoRL 2024*.
- Taewoong Kim, Cheolhong Min, Byeonghwi Kim, Jinyeon Kim, Wonje Jeung, Jonghyun Choi. "ReALFRED: Interactive Instruction Following Benchmark in Photo-Realistic Environments". *ECCV 2024*.
- Young Jin Ahn, Jungwoo Park, Sangha Park, Jonghyun Choi , Kee-Eung Kim. "SyncVSR: Data-Efficient Visual Speech Recognition with End-to-End Crossmodal Audio Token Synchronization". *Interspeech 2024*.
- Daechul Ahn, Yura Choi, Youngjae Yu, Dongyeop Kang, Jonghyun Choi. "Tuning Large Multimodal Models for Videos using Reinforcement Learning from AI Feedback". *ACL 2024 (Oral)*.
- Hyeyoon Lee, Kanghyun Choi, Dain Kwon, SunJong Park, Mayoore Selvarasa Jaiswal, Noseong Park, Jonghyun Choi , Jinho Lee. "DataFreeShield: Defending Adversarial Attacks without Training Data". *ICML 2024*.
- Minhyuk Seo, Hyunseo Koh, Wonje Jeung, Min Jae Lee, San Kim, Hankook Lee, Sungjun Cho, Sungik Choi, Hyunwoo Kim, Jonghyun Choi. "Learning Equi-angular Representations for Online Continual Learning". *CVPR 2024*.
- Byeonghwi Kim, Minhyuk Seo, Jonghyun Choi. "Online Continual Learning for Interactive Instruction Following Agents". *ICLR 2024*.
- Jinsung Jeon, Hyundong Jin, Jonghyun Choi , Sanghyun Hong, Dongeun Lee, Kookjin Lee, Noseong Park. "PAC-FNO: Parallel-Structured All-Component Fourier Neural Operators for Recognizing Low-Quality Images". *ICLR 2024*.
- Woojin Cho, Seunghyeon Cho, Hyundong Jin, Jinsung Jeon, Kookjin Lee, Sanghyun Hong, Dongeun Lee, Jonghyun Choi , Noseong Park. "Operator-learning-inspired Modeling of Neural Ordinary Differential Equations". *AAAI 2024*.

**2023**

- Byeonghwi Kim, Jinyeon Kim, Yuyeong Kim, Cheolhong Min, Jonghyun Choi. "Context-Aware Planning and Environment-Aware Memory for Instruction Following Embodied Agents". *ICCV 2023 - CVPR 2023 Embodied AI Workshop - 1st Place Winner*.
- Daechul Ahn, Daneul Kim, Gwangmo Song, Seung Hwan Kim, Honglak Lee, Dongyeop Kang, Jonghyun Choi. "Story Visualization by Online Text Augmentation with Context Memory". *ICCV 2023*.
- Byung Hyun Lee, Okchul Jung, Jonghyun Choi , Se Young Chun. "Online Continual Learning on Hierarchical Label Expansion". *ICCV 2023*.
- Xinyue Ma, Suyeon Jeong, Minjia Zhang, Di Wang, Jonghyun Choi , Myeongjae Jeon. "Cost-effective On-device Continual Learning over Memory Hierarchy with Miro". *MobiCom 2023 (Oral)*.
- Hyunseo Koh, Minhyuk Seo, Jihwan Bang, Hwanjun Song, Deokki Hong, Seulki Park, Jung-Woo Ha, Jonghyun Choi. "Online Boundary-Free Continual Learning by Scheduled Data Prior". *ICLR 2023*.
- Suvaansh Bhambri\*, Byeonghwi Kim\*, Jonghyun Choi. "Multi-level Compositional Reasoning for Interactive Instruction Following". *AAAI 2023 (Oral)*.

**2022**

- Kunal Pratap Singh, Luca Weihs, Alvaro Herrasti, Jonghyun Choi , Aniruddha Kembhavi, Roozbeh Mottaghi. "Ask4Help: Learning to Leverage an Expert for Embodied Tasks". *NeurIPS 2022*.
- Shlok Mishra, Anshul Shah, Ankan Bansal, Janit Anjaria, Jonghyun Choi , Abhinav Shrivastava, Abhishek Sharma, David Jacobs. "Learning visual representations for transfer learning by suppressing texture". *BMVC 2022*.
- Dahyun Kim, Jonghyun Choi. "Unsupervised Representation Learning for Binary Networks by Joint Classifier Learning". *CVPR 2022*.
- Jihwan Bang, Hyunseo Koh, Seulki Park, Hwanjun Song, Jung-Woo Ha, Jonghyun Choi. "Online Continual Learning on a Contaminated Data Stream with Blurry Task Boundaries". *CVPR 2022*.
- YeongWoo Nam, Mohammad Mostafavi, Kuk-Jin Yoon, Jonghyun Choi. "Stereo Depth from Events Cameras: Concentrate and Focus on the Future". *CVPR 2022*.
- Junghun Oh, Heewon Kim, Seungjun Nah, Cheeun Hong, Jonghyun Choi , Kyoung Mu Lee. "Attentive Fine-Grained Structured Sparsity for Image Restoration". *CVPR 2022*.
- Divyam Goel, Kunal Pratap Singh, Jonghyun Choi. "Language Guided Meta-Control for Embodied Instruction Following". *CVPR 2022 Workshop - Embodied AI Workshop*.
- Soobee Lee, Minindu Weerakoon, Jonghyun Choi , Minjia Zhang, Di Wang, Myeongjae Jeon. "CarM: Hierarchical Episodic Memory for Continual Learning". *DAC 2022*.
- Hyunseo Koh\*, Dahyun Kim\*, Jung-Woo Ha, Jonghyun Choi. "Online Continual Learning on Class Incremental Blurry Task Configuration with Anytime Inference". *ICLR 2022*.

**2021**

- Christopher Clark, Jordi Salvador, Dustin Schwenk, Derrick Bonafilia, Mark Yatskar, Eric Kolve, Alvaro Herrasti, Jonghyun Choi , 
          Sachin Mehta, Sam Skjonsberg, Carissa Schoenick, Aaron Sarnat, Hannaneh Hajishirzi, Aniruddha Kembhavi, Oren Etzioni and Ali Farhadi. "Iconary: A Pictionary-based Game for Testing Multimodal Communication with Drawings and Text". *EMNLP 2021 (Long) (Oral)*.
- Jinwoo Nam\*, Daechul Ahn\*, Dongyeop Kang, Seong Jong Ha, Jonghyun Choi. "Zero-Shot Natural Language Video Localization". *ICCV 2021 (Oral)*.
- Kunal Pratap Singh\*, Suvaansh Bhambri\*, Byeonghwi Kim\*, Roozbeh Mottaghi, Jonghyun Choi. "Factorizing Perception and Policy for Interactive Instruction Following". *ICCV 2021*.
- Yeonsik Jo, Se Young Chun, Jonghyun Choi. "Rethinking Deep Image Prior for Denoising". *ICCV 2021*.
- S. Mohammad Mostafavi I., Kuk-Jin Yoon, Jonghyun Choi. "Event-Intensity Stereo: Estimating Depth by the Best of Both Worlds". *ICCV 2021*.
- S. Mohammad Mostafavi I., Yeong-woo Nam Jonghyun Choi , Kuk-Jin Yoon. "E2SRI: Learning to Super Resolve Intensity Images from Events". *IEEE TPAMI 2021 (An extension of CVPR 2020 paper)*.
- Jihwan Bang\*, Heesu Kim\*, Youngjoon Yoo, Jung-Woo Ha, Jonghyun Choi. "Rainbow Memory: Continual Learning with a Memory of Diverse Samples". *CVPR 2021*.
- Dahyun Kim, Kunal Pratap Singh, Jonghyun Choi. "BNAS v2: Learning Architectures for Binary Networks with Empirical Improvements". *CVPR 2021 Workshop for Binary Networks for Computer Vision*.
- Seung-Cheol Han, Jonghyun Choi , Sung-Min Hong. "Acceleration of Semiconductor Device Simulation With Approximate Solutions Predicted by Trained Neural Networks". *IEEE Transactions on Electron Devices 2021*.

## 최근 소식

2021년 10월 22일–2026년 10월 22일의 연구 성과를 다룬 교수 개인 목록이며 부임 전 항목이 섞여 있다. 날짜는 교수 누리집의 소식 연월이다. 학회 논문은 게재 완료라는 뜻으로 바꾸지 않고 채택 소식으로 적었다.[^news][^cv]

- 2024.06 · CVPR 2024의 컴퓨터 비전 지속 학습 워크숍 CLVision 챌린지에서 2위를 받았다.
- 2023.09 · ICCV 2023 시각 지속 학습 워크숍의 SHIFT 챌린지에서 1위를 받았다. 주제는 물체 검출의 연속적인 시험 시점 적응이다.
- 2023.07 · 몸을 가진 에이전트의 인공지능, 영상·언어 이해, 지속 학습을 다룬 논문 3편이 ICCV 2023에 채택됐다.
- 2023.07 · 비용 효율적인 지속 학습 시스템 논문 1편이 MobiCom 2023에 채택됐다.
- 2023.06 · CVPR 2023 Embodied AI 워크숍의 Generalist Language Grounding Agents 챌린지에서 1위를 받았다.
- 2023.02 · 지속 학습 논문 1편이 ICLR 2023에 채택됐다.
- 2022.11 · 몸을 가진 에이전트의 인공지능을 다룬 논문 1편이 AAAI 2023에 채택됐다.
- 2022.10 · 질감 전처리를 이용해 새로운 자료에 대한 대응을 다룬 논문 1편이 BMVC 2022에 채택됐다.
- 2022.09 · 몸을 가진 에이전트의 인공지능을 다룬 논문 1편이 NeurIPS 2022에 채택됐다.
- 2022.03 · 논문 4편이 CVPR 2022에 채택됐다.
- 2022.02 · 지속 학습 논문 1편이 DAC 2022에 채택됐다.
- 2022.01 · 지속 학습 논문 1편이 ICLR 2022에 채택됐다.

## 연락과 위치

- 교수 연구실: 서울대학교 302동 523호.[^prof]
- 전화: 02-880-1766.[^prof]
- 이메일: jonghyunchoi@snu.ac.kr.[^gsai]

## 각주
[^intro]: 교수 개인 누리집 소개. 연구실 영문명, 전기·정보공학부와 협동과정 인공지능전공, 연구 관심과 이전 소속 표기. <https://ppolon.github.io/top.html> (2026-10-26 관측).
[^lab]: 서울대학교 전기·정보공학부 연구실 상세, 「기계 인지 및 추론 연구실」. 지도교수·연구 분야·최근 관심 분야와 주요 논문 7편. <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=141> (2026-10-26 관측).
[^lab-en]: 서울대학교 전기·정보공학부 영문 연구실 소개. 계산적 인지와 효율적인 학습 알고리즘의 접점, 에이전트의 지식 습득·표현·적응과 계산 부담을 연구한다고 설명한다. <https://ece.snu.ac.kr/en/research-faculty/research/groups?labidx=141&md=view> (2026-10-26 관측).
[^prof]: 서울대학교 전기·정보공학부 최종현 전임교수 소개. 부교수, 연구 분야·주요 경력·학력, 교수 연구실 302동 523호, 전화. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p900> (2026-10-26 관측).
[^gsai]: 서울대학교 대학원 협동과정 인공지능전공 소개, 교무부주임 최종현 부교수(소속 공과대학 전기·정보공학부), 학교 이메일. <https://gsai.snu.ac.kr/%ED%95%99%EA%B3%BC%EC%86%8C%EA%B0%9C-2/> (2026-10-26 관측).
[^cv]: Jonghyun Choi, C.V., Employment·Education. 서울대 부임 2024년 3월, 연세대 2022년 3월–2024년 2월, GIST 2018년 8월–2022년 2월, 학위 연도 확인. <https://ppolon.github.io/cv_JChoi.pdf> (2026-10-26 관측).
[^bib]: 교수 개인 누리집 Publications. 2021–2026년 구역과 Preprints 구역의 2026년 항목, 저자·학회·학술지·판본 상태. <https://ppolon.github.io/pub.html> (2026-10-26 관측).
[^news]: 교수 개인 누리집 News. 날짜가 2021-10-22–2026-10-22인 연구 성과 소식. <https://ppolon.github.io/news.html> (2026-10-26 관측).

[^p1]: H. Choi 외, J. Choi, International Conference on Machine Learning (ICML) 2026 (2026). <https://arxiv.org/abs/2602.04208> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2602.04208>.
[^p2]: T. Kang, T. Kim, D. Shin, J. Choi, European Conference on Computer Vision (ECCV) 2026 (2026). <https://arxiv.org/abs/2607.00666> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2607.00666>.
[^p3]: M. Seo, H. Koh, J. Choi, International Conference on Learning Representations (ICLR) 2025 (2025). <https://arxiv.org/abs/2410.15143> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2410.15143>.
[^p4]: M. Lee 외, J. Choi, Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 3491–3515 (2026). <https://doi.org/10.18653/v1/2026.acl-long.158> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2026.acl-long.158/>.
[^p5]: D. Ahn 외, J. Choi, Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 923–940 (2024). <https://doi.org/10.18653/v1/2024.acl-long.52> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2024.acl-long.52/>.
[^p6]: D. Ahn 외, J. Choi, IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) 2026 (2026). <https://arxiv.org/abs/2512.08979> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2512.08979>.
[^p7]: S. Venugopal, M. Mostafavi, J. Choi, IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) 2026 (2026). <https://arxiv.org/abs/2605.05889> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2605.05889>.
[^p8]: A. Yousefpour 외, J. Choi, Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 24073–24098 (2025). <https://doi.org/10.18653/v1/2025.acl-long.1173> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2025.acl-long.1173/>.

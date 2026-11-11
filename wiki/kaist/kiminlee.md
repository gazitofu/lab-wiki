# RISE Lab

**KAIST 김재철AI대학원 · 이기민 조교수**

- 분야: 로봇 학습, 강화학습, 사람과 로봇의 상호작용, 인공지능 에이전트의 안전, 영상 생성[^home]
- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 강화학습[^home][^p1][^p2], 대형 언어 모델[^p4][^p5][^p6], 생성 인공지능[^home][^p7][^p8], AI·기계학습 보안·프라이버시[^home][^p6][^p8]
- 홈페이지: <https://sites.google.com/view/kiminlee>
- 근거와 출처: [RISE Lab 근거 페이지](kiminlee-sources.md)

> 로봇과 컴퓨터 프로그램이 경험과 사람의 시범에서 행동을 배우게 하고, 그림을 만드는 인공지능의 학습 방법과 자율 행동의 안전을 연구하는 연구실이다.[^home][^p1][^p6][^p7]

## 무엇을 연구하나

이기민 교수는 학생들과 함께 로봇 학습, 사람과 로봇의 상호작용, 강화학습, 인공지능의 안전과 정렬, 시각 자료를 만드는 생성 모델을 연구한다고 소개한다.[^home] 강화학습은 행동의 결과로 받는 점수를 바탕으로 장기적으로 얻을 점수를 키우는 행동 방법을 배우는 기계학습이다. 기계학습은 자료에서 규칙과 관계를 배워 예측이나 결정을 하는 계산 방법이며, 정렬은 인공지능의 행동을 사람이 의도한 목표와 기준에 맞추는 일이다.

로봇 학습에서는 이미 기록된 행동과 사람이 보여 준 시연 영상에서 배울 수 있는 정보를 연구한다. DEAS(DEtached value learning with Action Sequence)는 연속된 행동을 묶어 학습하고, REDS(REward learning from Demonstration with Segmentations)는 시연 영상을 하위 과업으로 나눠 로봇의 행동에 줄 보상을 배운다. 여기서 보상은 어떤 행동이나 결과가 목표에 맞는지를 나타내는 점수다. 두 연구는 각각 긴 과제의 행동 가치(그 행동 뒤에 장기적으로 얻을 것으로 기대되는 보상) 추정과 영상에서 학습 신호를 얻는 문제를 다룬다.[^p1][^p3]

컴퓨터 안에서 일하는 에이전트도 연구한다. 에이전트는 주변 상태를 보고 목표를 이루기 위한 행동을 고르는 프로그램이나 장치다. 웹 작업에서는 복잡한 웹페이지를 읽는 부분과 다음 행동을 결정하는 부분을 나누고, 모바일 기기에서는 메시지·금융 앱을 다룰 때 생길 위험을 시험한다. 안전을 고려하도록 지시하는 방법도 제안하지만, 모바일 안전 연구는 위험을 막는 데 여전히 개선할 여지가 있다고 밝힌다.[^p5][^p6]

생성 인공지능에서는 글에 맞는 그림을 만드는 모델의 학습과 보안을 다룬다.[^home][^p7][^p8] 확산 모델은 자료에 잡음을 섞는 과정의 역방향을 배워 새 자료를 생성하는 모델이며, 잡음은 원하는 정보와 무관하게 섞인 변동이다. DiffExp는 보상이 높은 그림을 얻기 위한 탐색 방법을 개발한다.[^p7] Silent Branding Attack은 학습 자료에 섞은 로고가 특정 단어의 지시 없이도 생성 그림에 나타나게 하는 공격을 제안하고 평가한다.[^p8]

## 주요 연구 주제

### 기록된 경험과 시연으로 배우는 로봇

오프라인 강화학습(환경과 새로 상호작용하지 않고 이미 모은 기록에서 행동 방법을 배우는 강화학습)을 긴 로봇 과제에 적용하는 방법을 개발한다.[^p1] DEAS는 여러 행동을 한 묶음으로 다루면서 행동의 가치를 과하게 높게 추정하는 문제를 줄인다.[^p1] REDS는 동작 명령이 붙어 있지 않은 영상도 하위 과업별 시연으로 나눠 활용하며, 조립과 물체 조작 과제에서 보상을 학습한다.[^p3]

### 행동 생성과 언어 모델의 학습 신호

Q-Flow는 흐름 기반 모델(출발 자료를 연속적인 변환으로 목표 자료로 바꾸는 경로를 배우는 생성 모델)을 행동 선택에 이용하며, 그 변환 도중의 상태에도 행동의 최종 가치를 전달해 학습을 안정화한다. 언어 모델(글의 순서와 문맥을 배워 다음 글을 예측하거나 생성하는 모델)의 지식 증류(교사 모델의 출력에서 학생 모델이 배우도록 하는 학습)에서는 교사 출력의 불확실성(교사가 다음 말을 하나로 정하지 못하는 정도)에 따라 학습 목표를 조절한다. 불확실성이 클 때 가능한 출력의 다양성을 보존하는 것이 해당 연구의 목표다.[^p2][^p4]

### 웹·모바일 작업의 수행과 안전

LCoW(Learning language models to Contextualize complex Web pages)는 웹페이지의 내용을 언어 모델 에이전트가 행동을 결정하기 알맞은 형태로 바꾸는 별도 학습 모듈을 개발한다. MobileSafetyBench는 모바일 에이전트가 개인정보나 기기 설정을 다룰 때의 오용과 부작용을 시험하는 벤치마크(여러 방법을 같은 기준으로 평가하기 위한 과제와 측정 기준)를 개발한다. 외부 콘텐츠에 숨은 지시가 에이전트의 행동을 바꾸는 간접 프롬프트 주입 공격도 평가 대상으로 삼는다.[^p5][^p6]

### 그림 생성의 보상 학습과 자료 오염

그림 생성 모델의 미세조정(이미 학습한 모델을 특정 목표에 맞게 추가 학습하는 과정)에서는 다양한 그림과 보상이 높은 그림을 얻는 탐색을 함께 다룬다. DiffExp는 글 지시의 구절별 가중치와 생성 안내의 세기를 바꾼다. 자료 오염 공격(학습 자료를 의도적으로 바꿔 모델에 원치 않는 행동을 배우게 하는 공격) 연구에서는 그림에 삽입한 로고가 생성 결과에 섞이는 취약성을 분석한다.[^p7][^p8]

## 대표 논문

KAIST 재직 시기의 연구 가운데 로봇 학습, 학습 신호 설계, 에이전트, 그림 생성·보안 갈래의 논문을 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. arXiv는 심사 전후의 연구 원고를 공개하는 저장소이며, 표의 arXiv 표기는 해당 공개 원고의 연도다.

| 번호 | 연도 | 논문·발표처 | 주요 저자 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2025 | [DEAS: DEtached value learning with Action Sequence for Scalable Offline RL](https://doi.org/10.48550/arxiv.2510.07730) · arXiv | Changyeon Kim, Haeone Lee, Younggyo Seo, Kimin Lee, Yuke Zhu | 기록된 행동을 묶어서 긴 과제의 가치를 배우고, 기록에서 높은 보상을 얻은 행동 쪽으로 가치 추정을 이끈다. 모의 환경과 실제 로봇 조작 과제에서 행동 묶음을 예측하는 모델의 성능 향상을 보였다.[^p1] |
| 2 | 2026 | [Q-Flow: Stable and Expressive Reinforcement Learning with Flow-Based Policy](https://doi.org/10.48550/arxiv.2605.13435) · ICML 2026, arXiv 판 | JaeHyeok Doo, Byeongguk Jeon, Seonghyeon Ye, Kimin Lee, Minjoon Seo | 행동을 생성하는 흐름의 마지막 가치를 중간 상태로 전달해 학습한다. 계산 절차를 끝에서부터 모두 거슬러 계산하지 않으면서 안정적으로 행동을 개선하고, 기록에서 배운 뒤 새 경험에 적응하는 방법도 제시했다.[^p2] |
| 3 | 2025 | [Subtask-Aware Visual Reward Learning from Segmented Demonstrations](https://doi.org/10.48550/arxiv.2502.20630) · arXiv | Changyeon Kim, Minho Heo, Doohyun Lee, Jinwoo Shin, Honglak Lee, Joseph J. Lim, Kimin Lee | 시연 영상을 하위 과업으로 나눠 로봇에 줄 보상을 배운다. 행동 명령이 없는 영상으로도 물체 조작과 가구 조립을 학습하고, 보지 못한 과제와 다른 형태의 로봇에 적용할 가능성을 보였다.[^p3] |
| 4 | 2026 | [Entropy-Aware On-Policy Distillation of Language Models](https://doi.org/10.48550/arxiv.2603.07079) · ICML 2026, arXiv 판 | 1저자 Woogyeol Jin · 마지막 저자 Kimin Lee | 학생 언어 모델이 스스로 만든 답의 과정에서 교사 모델을 따라 배우게 한다. 교사가 여러 출력을 가능하게 보는 부분에서는 그 다양성을 보존하도록 학습 목표를 조절해, 수학 추론 평가에서 정확도를 높였다.[^p4] |
| 5 | 2025 | [Learning to Contextualize Web Pages for Enhanced Decision Making by LLM Agents](https://doi.org/10.48550/arxiv.2503.10689) · ICLR 2025, arXiv 판 | 1저자 Dongjun Lee · 마지막 저자 Kimin Lee | 복잡한 웹페이지를 이해하기 쉬운 형식으로 바꾸는 모듈을 따로 학습한다. 웹페이지 해석과 행동 결정을 나눈 구성으로 여러 언어 모델 에이전트의 웹 작업 성공률을 높였다.[^p5] |
| 6 | 2026 | [MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control](https://doi.org/10.1609/aaai.v40i44.41090) · AAAI 2026 | Juyong Lee, Dongyoon Hahm, June Suk Choi, W. Bradley Knox, Kimin Lee | 안드로이드 모의 환경에서 모바일 에이전트의 안전을 시험하는 과제를 만든다. 안전을 우선하도록 지시하는 방법은 개선 가능성을 보였지만, 작업 중 위해를 막는 데 여전히 한계가 있음을 확인했다.[^p6] |
| 7 | 2025 | [DiffExp: Efficient Exploration in Reward Fine-tuning for Text-to-Image Diffusion Models](https://doi.org/10.1609/aaai.v39i15.33723) · AAAI 2025 | Daewon Chae, June Suk Choi, Jinkyu Kim, Kimin Lee | 글에 맞는 그림을 만드는 모델을 보상으로 추가 학습할 때의 탐색 방법을 제안한다. 생성 안내의 세기를 조절하고 글 구절의 가중치를 무작위로 바꿔, 최근 보상 학습 방법의 표본 효율(같은 개선에 필요한 시도의 수)을 개선했다.[^p7] |
| 8 | 2025 | [Silent Branding Attack: Trigger-free Data Poisoning Attack on Text-to-Image Diffusion Models](https://doi.org/10.1109/cvpr52734.2025.00768) · CVPR 2025 | Sangwon Jang, June Suk Choi, Jaehyeong Jo, Kimin Lee, Sung Ju Hwang | 학습용 그림에 로고를 자연스럽게 섞어, 글 지시에 로고를 요구하는 단어가 없어도 생성 그림에 나타나게 한다. 이 공격이 그림의 품질과 글에 맞는 정도를 떨어뜨리지 않고 작동할 수 있음을 평가했다.[^p8] |

## 교수와 전문 분야

이기민 교수는 KAIST 김재철AI대학원 조교수다. 누리집 이력은 KAIST 조교수 재직을 2023년 8월부터로 적으며, 그 전에 UC Berkeley에서 박사후연구원으로, Google Research에서 연구원으로 일했다고 소개한다. KAIST 전기및전자공학부에서 학사·석사·박사 학위를 받았고, 박사 연구 분야는 기계학습·심층학습으로 적혀 있다. 심층학습은 여러 층의 신경망으로 자료의 표현을 단계적으로 배우는 기계학습이며, 신경망은 입력을 받아 값을 계산하는 단위들을 연결한 모델이다.[^home][^dept]

최근 논문의 주제에서 읽히는 전문 분야는 기록된 경험으로 배우는 로봇의 행동 가치 추정, 시연 영상에서의 보상 학습, 언어 모델 에이전트의 웹 작업과 안전, 그림 생성 모델의 학습 및 보안이다.[^p1][^p3][^p5][^p6][^p7][^p8]

## 응용 분야

로봇의 물체 조작과 가구 조립, 웹 작업 자동화, 모바일 기기의 안전한 제어, 글에 맞는 그림 생성이 논문에서 다루는 응용이다. 로봇에서는 여러 단계의 작업을 배우는 데 필요한 기록과 시연을 활용하고, 모바일·웹에서는 작업을 끝내는 능력과 위험을 피하는 능력을 함께 다룬다.[^p1][^p3][^p5][^p6][^p7]

## 구성원

Group 쪽에 게시된 구성원 17명이다. 과정은 게시 구획을 따른다. 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^group]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Seonghyeon Ye | 박사후연구원 | 2 |
| Changyeon Kim | 박사과정 | 1, 3 |
| June Suk Choi | 박사과정 | 6, 7, 8 |
| Dongjun Lee | 박사과정 | 5 |
| Jian Kim | 박사과정 |  |
| Jaehwi Song | 박사과정 |  |
| Taywon Min | 석사과정 | 4 |
| Haeone Lee | 석사과정 | 1 |
| Juheon Choi | 석사과정 |  |
| Woogyeol Jin | 석사과정 | 4 |
| Suchae Jeong | 석사과정 |  |
| JaeHyeok Doo | 석사과정 | 2 |
| Dong Kyu Shin | 석사과정 |  |
| Dongyoon Hahm | 학부 연구생 | 6 |
| Sinjae Kang | 학부 연구생 |  |
| Jeonghyeon Jang | 학부 연구생 |  |
| Yekyung Nah | 학부 연구생 |  |

Group의 「AI Agents」 구획에는 연구를 돕는 첫 AI 에이전트 Hae Bong도 소개되어 있다. AI는 Artificial Intelligence, 인공지능의 줄임말이다.[^group]

## 졸업생 진로

Group의 Alumni 구획에 게시된 7명이다. 학위·과정 칸은 누리집의 재학 과정과 기관 표기이며, 학위 취득 연도를 뜻하지 않는다.[^group]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Juyong Lee | PhD student at KAIST | Research Engineer at DeepMind |
| Chanyoung Kim | BS student at KAIST | Member of Technical Staff at Config |
| Seungku Kim | BS student at KAIST | Master student at KAIST |
| Junsu Kim | PhD student at KAIST | Research Scientist at Diden Robotics |
| Younggyo Seo | PhD student at KAIST | Research Scientist at Amazon |
| Lili Chen | BS student at UC Berkeley | PhD student at CMU |
| Xinran Liang | BS student at UC Berkeley | PhD student at Princeton |

## 최근 5년 논문 목록

교수 개인 누리집의 2021–2026년 연도 구역에 게시된 논문 66편이다. 이 목록에는 2023년 8월 KAIST 부임 전의 UC Berkeley·Google Research 재직 시기 논문도 포함된다. 연도·제목·저자·발표처는 누리집 표기를 따르며, 학회·워크숍·학술지·arXiv 원고를 함께 담았다. 별표는 누리집의 동등 기여 표시이고 ^는 동등 지도 표시다.[^home]

**2026**

- Jaehwi Song, Suchae Jeong, Byeongguk Jeon, Sungdong Kim, Hyungmok Son, Kimin Lee. "HABIT: Human-Aware Behavior and Interaction Training Dataset for Robot Manipulation". *Conference on Neural Information Processing Systems (NeurIPS) Datasets and Benchmarks Track 2026 as oral presentation*.
- Seonghyeon Lim, Hyeonwoo Lee, Mincheol Kim, Kimin Lee^, Hyun Myung^. "MAPO: Mixture of Experts with Alternating Policy Optimization for Universal Humanoid Motion Tracking". *Conference on Robot Learning (CoRL) 2026*.
- Xinyao Qin, Junjie Lu, Kaixin Wang, Chuheng Zhang, Sinjae Kang, Kimin Lee, Min Xu, Bin Liang, Jun Yang, Li Zhao. "Beyond Monotonic Progress: Retry-Supervised Value Learning for Robot Imitation". *Conference on Robot Learning (CoRL) 2026*.
- Woogyeol Jin, Taywon Min, Yongjin Yang, Dennis Wei, Yi Zhou, Swanand Ravindra Kadhe, Nathalie Baracaldo, Kimin Lee. "Entropy-Aware On-Policy Distillation of Language Models". *International Conference on Machine Learning (ICML) 2026*.
- Dongyoon Hahm, Dylan Hadfield-Menell, Kimin Lee. "Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases". *International Conference on Machine Learning (ICML) 2026*.
- JaeHyeok Doo, Byeongguk Jeon, Seonghyeon Ye, Kimin Lee, Minjoon Seo. "Q-Flow: Stable and Expressive Reinforcement Learning with Flow-based Policy". *International Conference on Machine Learning (ICML) 2026*.
- June Suk Choi, Kyungmin Lee, Sihyun Yu, Yisol Choi, Jinwoo Shin, Kimin Lee. "Improving Motion in Image-to-Video Models via Adaptive Low-Pass Guidance". *Conference on Computer Vision and Pattern Recognition (CVPR) 2026*.
- Suchae Jeong\*, Jaehwi Song\*, Haeone Lee, Hanna Kim, Jian Kim, Dongjun Lee, Dong Kyu Shin, Changyeon Kim, Dongyoon Hahm, Woogyeol Jin, Juheon Choi, Kimin Lee. "Learning Multi-View Spatial Reasoning from Cross-View Relations". *Conference on Computer Vision and Pattern Recognition (CVPR) 2026*.
- Haeone Lee, Taywon Min, Junsu Kim, Sinjae Kang, Fangchen Liu, Lerrel Pinto, Kimin Lee. "Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning". *International Conference on Robotics and Automation (ICRA) 2026*.
- Dongjun Lee, Changho Hwang, Kimin Lee. "Learning to generate unit test via adversarial reinforcement learning". *International Conference on Learning Representations (ICLR) 2026*.
- Changyeon Kim, Haeone Lee, Younggyo Seo, Kimin Lee^, Yuke Zhu^. "DEAS: DEtached value learning with Action Sequence for Scalable Offline RL". *International Conference on Learning Representations (ICLR) 2026*.
- Juheon Choi, Juyoung Lee, Jian Kim, Chanyoung Kim, Taewon Min, W Bradley Knox^, Min Kyung Lee^, Kimin Lee^. "State Your Intention to Steer Your Attention: An AI Assistant for Intentional Digital Living". *ACM Conference on Human Factors in Computing Systems (CHI) 2026 DOI: 10.1145/3772318.3791404*.
- Dongyoon Hahm\*, Taywon Min\*, Woogyeol Jin\*, Kimin Lee. "Unintended Misalignment from Agentic Fine-Tuning: Risks and Mitigation". *AAAI Conference on Artificial Intelligence (AAAI) AI Alignment Track 2026*.
- Juyong Lee\*, Dongyoon Hahm\*, June Suk Choi\*, W. Bradley Knox, Kimin Lee. "MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control". *AAAI Conference on Artificial Intelligence (AAAI) AI Alignment Track 2026 DOI: 10.1609/aaai.v40i44.41090*.
- Dongjun Lee, Juyong Lee, Changho Hwang, Kimin Lee. "Adversarial Iterative Unit Test Generation with Large Language Models". *ICLR workshop on Agentic AI in the Wild: From Hallucinations to Reliable Autonomy 2026*.

**2025**

- Eugene Jang, Kimin Lee, Jin-Woo Chung, Keuntae Park, Seungwon Shin. "Improbable Bigrams Expose Vulnerabilities of Incomplete Tokens in Byte-Level Tokenizers". *Conference on Empirical Methods in Natural Language Processing (EMNLP) 2025 (main) DOI: 10.18653/v1/2025.emnlp-main.919*.
- Juyong Lee, Taywon Min, Minyong An, Dongyoon Hahm, Haeone Lee, Changyeon Kim, Kimin Lee. "Benchmarking Mobile Device Control Agents across Diverse Configurations". *Conference on Lifelong Learning Agents (CoLLAs) 2025*.
- Taywon Min, Haeone Lee, Yongchan Kwon, Kimin Lee. "Understanding Impact of Human Feedback via Influence Functions". *Annual Meeting of the Association for Computational Linguistics (ACL) 2025 (main)*.
- Sangyeop Kim, Yohan Lee, Yongwoo Song, Kimin Lee. "What Really Matters in Many-Shot Attacks? An Empirical Study of Long-Context Vulnerabilities in LLMs". *Annual Meeting of the Association for Computational Linguistics (ACL) 2025 (main) DOI: 10.18653/v1/2025.acl-long.101*.
- Dongyoon Hahm, Woogyeol Jin, June Suk Choi, Sungsoo Ahn, Kimin Lee. "Enhancing LLM Agent Safety via Causal Influence Prompting". *Annual Meeting of the Association for Computational Linguistics (ACL) 2025 (findings) DOI: 10.18653/v1/2025.findings-acl.784*.
- Sangwon Jang, June Suk Choi, Jaehyeong Jo, Kimin Lee^, Sung Ju Hwang^. "Silent Branding Attack: Trigger-free Data Poisoning Attack on Text-to-Image Diffusion Models". *Conference on Computer Vision and Pattern Recognition (CVPR) 2025 DOI: 10.1109/cvpr52734.2025.00768*.
- Hanna Kim, Minkyoo Song, Seung Ho Na, Seungwon Shin, Kimin Lee. "When LLMs Go Online: The Emerging Threat of Web-Enabled LLMs". *USENIX Security Symposium 2025*.
- Dongjun Lee, Juyong Lee, Kyuyoung Kim, Jihoon Tack, Jinwoo Shin, Yee Whye Teh, Kimin Lee. "Learning to Contextualize Web Pages for Enhanced Decision Making by LLM Agents". *International Conference on Learning Representations (ICLR) 2025*.
- Yongjin Yang\*, Sihyeon Kim\*, Hojung Jung, Sangmin Bae, SangMook Kim, Se-Young Yun^, Kimin Lee^. "Automated Filtering of Human Feedback Data for Aligning Text-to-Image Diffusion Models". *International Conference on Learning Representations (ICLR) 2025*.
- June Suk Choi, Kyungmin Lee, Jongheon Jeong, Saining Xie, Jinwoo Shin, Kimin Lee. "DiffusionGuard: A Robust Defense Against Malicious Diffusion-based Image Editing". *International Conference on Learning Representations (ICLR) 2025*.
- Changyeon Kim, Minho Heo, Doohyun Lee, Honglak Lee, Jinwoo Shin, Joseph J Lim^, Kimin Lee^. "Subtask-Aware Visual Reward Learning from Segmented Demonstrations". *International Conference on Learning Representations (ICLR) 2025*.
- Dongyoung Kim, Kimin Lee, Jinwoo Shin, Jaehyung Kim. "Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment". *International Conference on Learning Representations (ICLR) 2025 as oral presentation*.
- Seonghyeon Ye\*, Joel Jang\*, Byeongguk Jeon, Sejune Joo, Jianwei Yang, Baolin Peng, Ajay Mandlekar, Reuben Tan, Yu-Wei Chao, Bill Yuchen Lin, Lars Liden, Kimin Lee^, Jianfeng Gao^, Luke Zettlemoyer^, Dieter Fox^, Minjoon Seo^. "Latent Action Pretraining from Videos". *International Conference on Learning Representations (ICLR) 2025*.
- Daewon Chae\*, June Suk Choi\*, Jinkyu Kim^, Kimin Lee^. "DiffExp: Efficient Exploration in Reward Fine-tuning for Text-to-Image Diffusion Models". *AAAI Conference on Artificial Intelligence (AAAI) 2025 as oral presentation DOI: 10.1609/aaai.v39i15.33723*.
- Hyungjun Yoon, Jaehyun Kwak, Biniyam Aschalew Tolera, Gaole Dai, Mo Li, Taesik Gong, Kimin Lee, Sung-Ju Lee. "SelfReplay: Adapting Self-Supervised Sensory Models via Adaptive Meta-Task Replay". *ACM Conference on Embedded Networked Sensor Systems (SenSys) 2025 DOI: 10.1145/3715014.3722066*.
- Dongryung Lee, Sejune Joo, Kimin Lee, Beomjoon Kim. "Prime the Search: Using Large Language Models for Guiding Geometric Task and Motion Planning by Warm-starting Tree Search". *International Journal of Robotics Research 2025 DOI: 10.1177/02783649251347307*.
- Inkyu Park, Jeong-Gwan Lee, Taehwan Kwon, Juheon Choi, Seungku Kim, Junsu Kim, Kimin Lee. "Adversarial Reinforcement Learning Framework for ESP Cheater Simulation". *Arxiv preprint 2025*.
- Yongjin Yang\*, Euiin Yi\*, Jongwoo Ko, Kimin Lee^, Zhijing Jin^, Se-Young Yun^. "Revisiting Multi-Agent Debate as Test-Time Scaling: A Systematic Study of Conditional Effectiveness". *Arxiv preprint 2025*.
- Yongjin Yang\*, Sinjae Kang\*, Juyong Lee, Dongjun Lee, Se-Young Yun^, Kimin Lee^. "Automated Skill Discovery for Language Agents through Exploration and Iterative Feedback". *Arxiv preprint 2025*.
- Dan Hendrycks, Dawn Song, Christian Szegedy, Honglak Lee, Yarin Gal, Erik Brynjolfsson, Sharon Li, Andy Zou, Lionel Levine, Bo Han, Jie Fu, Ziwei Liu, Jinwoo Shin, Kimin Lee, Mantas Mazeika, Long Phan, George Ingebretsen, Adam Khoja, Cihang Xie, Olawale Salaudeen, Matthias Hein, Kevin Zhao, Alexander Pan, David Duvenaud, Bo Li, Steve Omohundro, Gabriel Alfour, Max Tegmark, Kevin McGrew, Gary Marcus, Eric Schmidt, Yoshua Bengio. "A Definition of AGI". *Arxiv preprint 2025*.

**2024**

- Sangwon Jang\*, Jaehyeong Jo\*, Kimin Lee^, Sung Ju Hwang^. "Identity Decoupling for Multi-Subject Personalization of Text-to-Image Models". *Conference on Neural Information Processing Systems (NeurIPS) 2024 DOI: 10.52202/079017-3200*.
- Hyungjun Yoon, Biniyam Aschalew Tolera, Taesik Gong, Kimin Lee, Sung-Ju Lee. "By My Eyes: Grounding Multimodal Large Language Models with Sensor Data via Visual Prompting". *Conference on Empirical Methods in Natural Language Processing (EMNLP) 2024 (main) DOI: 10.18653/v1/2024.emnlp-main.133*.
- Kyuyoung Kim\*, Ah Jeong Seo\*, Hao Liu, Jinwoo Shin, Kimin Lee. "Margin Matching Preference Optimization: Enhanced Model Alignment with Granular Feedback". *Conference on Empirical Methods in Natural Language Processing (EMNLP) 2024 (findings) DOI: 10.18653/v1/2024.findings-emnlp.792*.
- Katherine Collins, Najoung Kim, Yonatan Bitton, Verena Rieser, Shayegan Omidshafiei, Yushi Hu, Sherol Chen, Senjuti Dutta, Minsuk Chang, Kimin Lee, Youwei Liang, Georgie Evans, Sahil Singla, Gang Li, Adrian Weller, Junfeng He, Deepak Ramachandran, Krishnamurthy Dvijotham. "Beyond Thumbs Up/Down: Untangling Challenges of Fine-Grained Feedback for Text-to-Image Generation". *Conference on AI, Ethics, and Society (AIES) 2024 DOI: 10.1609/aies.v7i1.31637*.
- Minyoung Hwang, Luca Weihs, Chanwoo Park, Kimin Lee, Aniruddha Kembhavi, Kiana Ehsani. "Promptable Behaviors: Personalizing Multi-Objective Rewards from Human Preferences". *Conference on Computer Vision and Pattern Recognition (CVPR) 2024 DOI: 10.1109/cvpr52733.2024.01535*.
- Kyuyoung Kim, Jongheon Jeong, Minyong An, Mohammad Ghavamzadeh, Krishnamurthy Dj Dvijotham, Jinwoo Shin, Kimin Lee. "Confidence-aware Reward Optimization for Fine-tuning Text-to-Image Models". *International Conference on Learning Representations (ICLR) 2024*.
- Daewon Chae, Nokyung Park, Jinkyu Kim^, Kimin Lee^. "InstructBooth: Instruction-following Personalized Text-to-Image Generation". *ICML Workshop on Foundation Models in the Wild 2024*.

**2023**

- Ying Fan\*, Olivia Watkins, Yuqing Du, Hao Liu, Moonkyung Ryu, Craig Boutilier, Pieter Abbeel, Mohammad Ghavamzadeh, Kangwook Lee, Kimin Lee\*. "DPOK: Reinforcement Learning for Fine-tuning Text-to-Image Diffusion Models". *Conference on Neural Information Processing Systems (NeurIPS) 2023*.
- Changyeon Kim, Younggyo Seo, Hao Liu, Lisa Lee, Jinwoo Shin, Honglak Lee, Kimin Lee. "Guide Your Agent with Adaptive Multimodal Rewards". *Conference on Neural Information Processing Systems (NeurIPS) 2023*.
- Kihyuk Sohn, Nataniel Ruiz, Kimin Lee, Daniel Castro Chin, Irina Blok, Huiwen Chang, Jarred Barber, Lu Jiang, Glenn Entis, Yuanzhen Li, Yuan Hao, Irfan Essa, Michael Rubinstein, Dilip Krishnan. "StyleDrop: Text-to-Image Generation in Any Style". *Conference on Neural Information Processing Systems (NeurIPS) 2023*.
- Younggyo Seo\*, Junsu Kim\*, Stephen James, Kimin Lee, Jinwoo Shin, Pieter Abbeel. "Multi-View Masked World Models for Visual Robotic Manipulation". *International Conference on Machine Learning (ICML) 2023*.
- Seohong Park, Kimin Lee, Youngwoon Lee, Pieter Abbeel. "Controllability-Aware Unsupervised Skill Discovery". *International Conference on Machine Learning (ICML) 2023*.
- Changyeon Kim, Jongjin Park, Jinwoo Shin, Honglak Lee, Pieter Abbeel, Kimin Lee. "Preference Transformer: Modeling Human Preferences using Transformers for RL". *International Conference on Learning Representations (ICLR) 2023*.
- Krishnamurthy Dj Dvijotham, Shayegan Omidshafiei, Katherine M. Collins, Deepak Ramachandran, Kimin Lee, Ying Fan, Jeremiah Zhe Liu, Milad Nasr, Mohammad Ghavamzadeh. "Algorithms for Optimal Adaptation of Diffusion Models to Reward Functions". *ICML workshop on New Frontiers in Learning, Control, and Dynamical Systems 2023*.
- Kimin Lee, Hao Liu, Moonkyung Ryu, Olivia Watkins, Yuqing Du, Craig Boutilier, Pieter Abbeel, Mohammad Ghavamzadeh, Shixiang Shane Gu. "Aligning Text-to-Image Models using Human Feedback". *Arxiv preprint 2023*.

**2022**

- Younggyo Seo, Danijar Hafner, Hao Liu, Fangchen Liu, Stephen James, Kimin Lee, Pieter Abbeel. "Masked World Models for Visual Control". *Conference on Robot Learning (CoRL) 2022*.
- Younggyo Seo, Kimin Lee, Stephen James, Pieter Abbeel. "Reinforcement Learning with Action-Free Pre-Training from Videos". *International Conference on Machine Learning (ICML) 2022*.
- Jongjin Park, Younggyo Seo, Jinwoo Shin, Honglak Lee, Pieter Abbeel, Kimin Lee. "SURF: Semi-supervised Reward Learning with Data Augmentation for Feedback-efficient Preference-based Reinforcement Learning". *International Conference on Learning Representations (ICLR) 2022*.
- Xinran Liang, Katherine Shu, Kimin Lee^, Pieter Abbeel^. "Reward Uncertainty for Exploration in Preference-based Reinforcement Learning". *International Conference on Learning Representations (ICLR) 2022*.
- Zhao Mandi\*, Fangchen Liu\*, Kimin Lee, Pieter Abbeel. "Towards More Generalizable One-shot Visual Imitation Learning". *International Conference on Robotics and Automation (ICRA) 2022 DOI: 10.1109/icra46639.2022.9812450*.
- Abdus Salam Azad\*, Edward Kim\*, Qiancheng Wu, Kimin Lee, Ion Stoica, Pieter Abbeel, Sanjit A. Seshia. "Programmatic Modeling and Generation of Real-time Strategic Soccer Environments for Reinforcement Learning". *AAAI Conference on Artificial Intelligence (AAAI) 2022 DOI: 10.1609/aaai.v36i6.20549*.
- Younggyo Seo, Kimin Lee, Fangchen Liu, Stephen James, Pieter Abbeel. "HARP: Autoregressive Latent Video Prediction with High-Fidelity Image Generator". *International Conference on Image Processing (ICIP) 2022 DOI: 10.1109/icip46576.2022.9897982*.
- Hao Liu, Lisa Lee, Kimin Lee, Pieter Abbeel. "Instruction-Following Agents with Jointly Pre-Trained Vision-Language Models". *Arxiv preprint 2022*.
- Changyeon Kim, Junsu Kim, Younggyo Seo, Kimin Lee, Honglak Lee, Jinwoo Shin. "Dynamics-Augmented Decision Transformer for Offline Dynamics Generalization". *NeurIPS Workshop on Offline RL 2022*.

**2021**

- Kimin Lee, Laura Smith, Anca Dragan, Pieter Abbeel. "B-Pref: Benchmarking Preference-Based Reinforcement Learning". *Conference on Neural Information Processing Systems (NeurIPS) Datasets and Benchmarks Track 2021 (round 1)*.
- Michael Laskin\*, Denis Yarats\*, Hao Liu, Kimin Lee, Albert Zhan, Kevin Lu, Catherine Cang, Lerrel Pinto, Pieter Abbeel. "URLB: Unsupervised Reinforcement Learning Benchmark". *Conference on Neural Information Processing Systems (NeurIPS) Datasets and Benchmarks Track 2021 (round 2)*.
- Lili Chen\*, Kevin Lu\*, Aravind Rajeswaran, Kimin Lee, Aditya Grover, Michael Laskin, Pieter Abbeel, Aravind Srinivas^, Igor Mordatch^. "Decision Transformer: Reinforcement Learning via Sequence Modeling". *Conference on Neural Information Processing Systems (NeurIPS) 2021*.
- Lili Chen, Kimin Lee, Aravind Srinivas, Pieter Abbeel. "Improving Computational Efficiency in Visual Reinforcement Learning via Stored Embeddings". *Conference on Neural Information Processing Systems (NeurIPS) 2021*.
- Hankook Lee, Kibok Lee, Kimin Lee, Honglak Lee, Jinwoo Shin. "Improving Transferability of Representations via Augmentation-Aware Self-Supervision". *Conference on Neural Information Processing Systems (NeurIPS) 2021*.
- Xiaofei Wang, Kimin Lee, Kourosh Hakhamaneshi, Pieter Abbeel, Michael Laskin. "Skill Preferences: Learning to Extract and Execute Robotic Skills from Human Feedback". *Conference on Robot Learning (CoRL) 2021*.
- Seunghyun Lee\*, Younggyo Seo\*, Kimin Lee, Pieter Abbeel, Jinwoo Shin. "Offline-to-Online Reinforcement Learning via Balanced Replay and Pessimistic Q-Ensemble". *Conference on Robot Learning (CoRL) 2021*.

## 연락과 위치

- 교수 업무 이메일: kiminlee@kaist.ac.kr[^home]
- 사무실: 9호관 9404호[^dept]

## 각주
[^home]: Kimin Lee, Home, 연구 소개·Publications·Education·Work Experience, <https://sites.google.com/view/kiminlee>, 관측 2026-11-09.
[^group]: Kimin Lee, Group, PostDoc·Ph.D. students·Master students·Undergraduate students·AI Agents·Alumni, <https://sites.google.com/view/kiminlee/group>, 관측 2026-11-09.
[^dept]: KAIST 김재철AI대학원, 구성원, 이기민 교수 소개, <https://gsai.kaist.ac.kr/people-2/?lang=ko>, 관측 2026-11-09.

[^p1]: C. Kim 외, Y. Zhu, arXiv:2510.07730 (2025). <https://doi.org/10.48550/arxiv.2510.07730> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2510.07730>, 관측 2026-11-11.
[^p2]: J. Doo 외, M. Seo, International Conference on Machine Learning (ICML); arXiv:2605.13435v2 (2026). <https://doi.org/10.48550/arxiv.2605.13435> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2605.13435>, 관측 2026-11-11.
[^p3]: C. Kim 외, K. Lee, arXiv:2502.20630 (2025). <https://doi.org/10.48550/arxiv.2502.20630> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2502.20630>, 관측 2026-11-11.
[^p4]: W. Jin 외, K. Lee, International Conference on Machine Learning (ICML); arXiv:2603.07079v3 (2026). <https://doi.org/10.48550/arxiv.2603.07079> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2603.07079>, 관측 2026-11-11.
[^p5]: D. Lee 외, K. Lee, International Conference on Learning Representations (ICLR); arXiv:2503.10689v2 (2025). <https://doi.org/10.48550/arxiv.2503.10689> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2503.10689>, 관측 2026-11-11.
[^p6]: J. Lee 외, K. Lee, Proceedings of the AAAI Conference on Artificial Intelligence (2026). <https://doi.org/10.1609/aaai.v40i44.41090> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5033571780>, 관측 2026-11-11.
[^p7]: D. Chae, J. S. Choi, J. Kim, K. Lee, Proceedings of the AAAI Conference on Artificial Intelligence (2025). <https://doi.org/10.1609/aaai.v39i15.33723> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5033571780>, 관측 2026-11-11.
[^p8]: S. Jang 외, S. J. Hwang, Conference on Computer Vision and Pattern Recognition (CVPR) (2025). <https://doi.org/10.1109/cvpr52734.2025.00768> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5033571780>, 관측 2026-11-11.

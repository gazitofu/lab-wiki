# Multimodal AI Lab

**KAIST 전기및전자공학부·메타버스대학원 · 정준선 부교수**

- 영문 이름: Multimodal AI Lab[^home][^metalabs]
- 대분야: 컴퓨팅·AI
- 태그: 음향·오디오 AI[^p1][^p7], 컴퓨터 비전[^p5][^p6], 멀티모달 AI[^p3][^p4]
- 홈페이지: <https://mm.kaist.ac.kr/>
- 소속: 전기및전자공학부, 메타버스대학원 겸임[^ee][^meta]

> 소리·영상·글과 촉각 정보 사이의 대응을 배우고, 사람의 말과 동작을 인식하거나 음성을 만들어 내는 인공지능을 연구한다.[^p2][^p3][^p5][^p6][^p7]

## 무엇을 연구하나

Multimodal AI Lab은 **멀티모달 AI(소리·영상·글처럼 종류가 다른 자료를 함께 다루는 인공지능)**를 연구한다. 정준선 교수는 연구 분야를 기계학습(자료에서 규칙을 배우게 하는 계산 방법), 음성 처리, 컴퓨터 비전(사진과 영상의 내용을 컴퓨터가 이해하게 하는 기술)으로 소개한다.[^prof] 대표 논문들을 함께 보면, 서로 다른 종류의 자료가 어떤 뜻이나 특성을 공유하는지 배우는 일이 연구를 잇는다. 예를 들어 말하는 얼굴의 움직임에서 음성을 만들고, 영상과 소리를 함께 이해하는 모델의 오류를 줄이며, 만져서 얻은 정보에 대응하는 영상 영역을 찾는다.[^p2][^p3][^p5]

첫째 갈래는 **음성 합성(주어진 내용이나 조건에 맞는 말소리를 만드는 기술)**이다. 문자에서 음성을 만드는 모델을 줄이는 SPADE(Structured Pruning and Adaptive Distillation for Efficient LLM-TTS)는 구조적 가지치기(계산 구조의 일부를 제거해 모델을 줄이는 방법)와 지식 증류(다른 모델의 출력이나 내부 정보를 학습에 활용하는 방법)를 결합한다. 단어를 잘못 생성하는 정도를 기준으로 제거할 층을 고른 뒤, 원래 모델의 정보를 배우게 해 음성이 이어지는 성질을 회복한다.[^p1] 「From Faces to Voices」는 소리가 없는 얼굴 영상에서 입 움직임·얼굴의 정체성·표정을 각각 발화 내용, 음색(소리를 구별하게 하는 고유한 음질), 운율(말의 높낮이·리듬·강세 같은 성질)에 대응시켜 음성을 만든다.[^p2]

둘째는 **소리·영상·글을 함께 이해하는 모델의 오류를 줄이는 일**이다. 시청각 대형 언어 모델(소리·영상·글을 함께 처리하고 언어로 답하는 대규모 학습 모델)은 입력에 근거하지 않은 내용을 답하는 환각을 보일 수 있다. AVCD(Audio-Visual Contrastive Decoding)는 모델이 자료별로 주의를 두는 정도를 이용해 덜 지배적인 종류의 자료를 찾는다. 주의 분포를 이용한 가리기로 비교용 출력을 만들고 원래 출력과 대조한다. 추가 학습 없이 답을 생성하는 과정에서 소리·영상·글 사이의 상호작용을 반영해 환각을 억제하는 방법이다.[^p3]

셋째는 **서로 다른 감각 정보의 대응과 위치를 찾는 일**이다. 소리 위치 추정(소리를 내는 대상이 시각 장면의 어디에 있는지 찾는 일)에서는 소리를 내지 않는 물체나 화면 밖 소리를 구분하려면 영상과 소리의 의미가 맞는지도 이해해야 한다. 연구진은 소리의 위치를 찾는 과제와 교차모달 검색(한 종류의 자료로 다른 종류의 관련 자료를 찾는 일)을 함께 다뤘다.[^p4] 「Seeing Through Touch」는 촉각 입력과 같은 재질 특성을 가진 영상 영역을 찾는다. 촉각과 영상의 세부 특징이 서로 대응하도록 배우게 하고, 재질을 공유하면서 겉모습은 다양한 장면을 학습에 활용한다.[^p5]

넷째는 **사람의 의사소통을 인식하는 일**이다. 연속 수어 인식(이어지는 수어 동작을 의미 단위의 순서로 알아내는 기술)에서는 손뿐 아니라 얼굴과 입의 표현도 함께 다루고, 영상의 낱장마다 정답을 붙이지 않아도 학습할 방법을 개발한다.[^p6] 화자 인식(목소리로 말하는 사람을 구별하는 기술)에서는 화자 임베딩(목소리의 특징을 수의 목록으로 나타낸 값)에서 화자의 특성과 나머지 정보를 나누어, 녹음 환경이 달라져도 사람을 구별하게 한다.[^p7]

## 주요 연구 주제

### 1. 음성 생성과 모델 경량화

문자를 음성으로 바꾸는 대형 모델의 계산 구조를 줄이는 SPADE와, 말하는 얼굴의 시각 정보를 발화 내용·음색·운율에 차례로 연결하는 영상 기반 음성 생성을 연구한다. 대표 논문 1, 2가 이 갈래다.[^p1][^p2]

### 2. 시청각 언어 모델의 환각 완화

소리·영상·글을 함께 다루는 모델에서 주의 분포에 따라 가리기를 적용한 경우와 원래 경우의 출력을 대조하고, 모델이 답에 확신하는 정도에 따라 생성 과정의 계산을 조절한다. 대표 논문 3은 AVCD의 arXiv 판이다.[^p3]

### 3. 소리·촉각과 영상의 대응 학습

영상 속 소리의 출처를 찾는 일과 관련 자료 검색을 함께 배우게 하며, 촉각과 재질 특성을 공유하는 영상 영역을 찾는 방법으로도 연구를 넓힌다. 대표 논문 4, 5가 이 갈래다.[^p4][^p5]

### 4. 연속 수어와 화자 인식

연속 수어에서 손·얼굴·입의 단서를 함께 추출하고 시간에 따른 학습용 정답을 보완한다. 목소리에서는 사람의 특성과 환경 정보를 나누는 표현을 배운다. 대표 논문 6, 7이 이 갈래다.[^p6][^p7]

## 대표 논문

2021년부터 KAIST에서 재직한 정준선 교수가 저자인 2023–2026년 논문 가운데 네 연구 갈래를 보여 주는 7편을 골랐다.[^prof] 1–4, 6, 7에서 교수는 마지막 저자이고, 5에서는 끝에서 두 번째 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다. 학회명·연도는 연구실 목록의 표기이며, 3과 5의 설명은 표에 명시한 arXiv 판을 따른다.[^pubs]

| # | 연도 | 논문 · 학회 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [SPADE: Structured Pruning and Adaptive Distillation for Efficient LLM-TTS](https://mm.kaist.ac.kr/pubs/pdfs/nguyen26a.pdf) · 연구실 게시 ICASSP 2026, 연구실 게시 논문 PDF | 문자를 말소리로 바꾸는 대형 모델에서 불필요한 층을 제거하고, 원래 모델의 지식을 배우게 해 음성이 이어지는 성질을 회복한다. 층을 절반으로 줄이면서도 지각적 품질을 거의 유지했고, 메모리(계산에 쓰는 정보를 저장하는 공간) 사용량과 생성 시간을 줄였다고 보고했다.[^p1] | 1저자 Tan Dat Nguyen, 마지막 저자 정준선 |
| 2 | 2025 | [From Faces to Voices: Learning Hierarchical Representations for High-quality Video-to-Speech](https://mm.kaist.ac.kr/pubs/pdfs/kim25b.pdf) · 연구실 게시 CVPR 2025, 연구실 게시 논문 PDF | 소리가 없는 말하는 얼굴 영상에서 음성을 만든다. 입 움직임·얼굴의 정체성·표정을 발화 내용·음색·운율에 차례로 대응시키고, 단순한 분포(어떤 값들이 얼마나 나타날 수 있는지를 나타낸 것)에서 목표 음성의 분포로 옮기는 경로를 배우는 흐름 매칭 모델로 음성을 생성한다. 실험에서 기존 방법보다 생성 품질이 높았다고 보고했다.[^p2] | 1저자 Ji-Hoon Kim, 마지막 저자 정준선 |
| 3 | 2025 | [AVCD: Mitigating Hallucinations in Audio-Visual Large Language Models through Contrastive Decoding](https://arxiv.org/abs/2505.20862) · 연구실 게시 NeurIPS 2025, 설명은 arXiv v2 | 소리·영상·글을 함께 처리하는 모델이 입력에 없는 내용을 답하는 문제를 다룬다. 자료별 주의의 분포를 바탕으로 가리기를 적용해 비교용 출력을 만들고 원래 출력과 대조한다. 추가 학습 없이 작동하며, 예측에 대한 확신에 따라 불필요한 생성 계산을 건너뛰는 방법도 결합했다.[^p3] | Chaeyoung Jung, Youngjoon Jang, 정준선(마지막 저자) |
| 4 | 2023 | [Sound Source Localization is All about Cross-Modal Alignment](https://mm.kaist.ac.kr/pubs/pdfs/senocak23a.pdf) · 연구실 게시 ICCV 2023, 연구실 게시 논문 PDF | 영상에서 소리의 위치를 찾는 정확도만으로는 영상과 소리의 뜻을 함께 이해하는지 판단하기 어렵다는 문제를 제기했다. 소리를 내지 않는 물체나 화면 밖 소리도 고려해, 소리 위치 추정과 서로 다른 종류의 자료 간 검색을 함께 학습하는 방법을 제안했다. 두 과제에서 기존 방법보다 좋은 결과를 보고했다.[^p4] | Arda Senocak·Hyeonggon Ryu·Junsik Kim, 마지막 저자 정준선 |
| 5 | 2026 | [Seeing Through Touch: Tactile-Driven Visual Localization of Material Regions](https://arxiv.org/abs/2604.11579) · CVPR 2026, 설명은 arXiv v1 | 만져서 얻은 입력과 같은 재질 특성을 가진 영상 영역을 찾는다. 촉각과 영상의 국소 특징을 서로 대응시키고, 하나의 촉각 자료에 겉모습이 다양하지만 촉각 특성은 일관된 영상을 짝지어 학습한다. 새로운 평가 자료도 구성했으며, 촉각으로 영상의 재질 영역을 찾는 성능이 기존 방법보다 높았다고 보고했다.[^p5] | Seongyu Kim, Seungwoo Lee, Hyeonggon Ryu, 정준선, Arda Senocak |
| 6 | 2023 | [Self-sufficient framework for continuous sign language recognition](https://mm.kaist.ac.kr/pubs/pdfs/jang23a.pdf) · 연구실 게시 ICASSP 2023, 연구실 게시 논문 PDF | 연속 수어를 이해하는 데 필요한 손·얼굴·입의 특징과, 영상의 낱장별 정답이 부족한 문제를 함께 다룬다. 추가 신경망(서로 연결된 계산 단위가 자료의 규칙을 배우는 모형)이나 정답 표시 없이 손과 그 밖의 특징을 추출하는 방법, 실제 의미 단위의 순서와 예측 순서를 결합해 학습용 정답을 보완하는 방법을 제안했다.[^p6] | 1저자 Youngjoon Jang, 마지막 저자 정준선 |
| 7 | 2024 | [Disentangled Representation Learning for Environment-agnostic Speaker Recognition](https://mm.kaist.ac.kr/pubs/pdfs/nam24a.pdf) · 연구실 게시 Interspeech 2024, 연구실 게시 논문 PDF | 녹음 환경이 달라도 사람을 구별하는 음성 표현을 배우는 방법이다. 입력을 압축했다가 되살리는 자동부호기로 화자 임베딩을 화자 관련 정보와 나머지 정보로 나누고, 압축 표현에 화자의 특성이 담기도록 학습한다. 기존 화자 특징 추출기의 구조를 바꾸지 않고 결합할 수 있다고 보고했다.[^p7] | KiHyun Nam, Hee-Soo Heo, Jee-weon Jung, 정준선(마지막 저자) |

## 교수와 전문 분야

정준선 교수(Joon Son Chung)는 전기및전자공학부 부교수이며, 메타버스대학원 교수진에서는 겸임(Joint)으로 소개된다.[^ee][^meta] 교수 소개에 따르면 2021년부터 KAIST에서 연구하고, 이전에는 2018–2021년 네이버의 Team Lead / Research Scientist로 일했다. 옥스퍼드대에서 2014년 Engineering, Economics and Management의 M.Eng.(B.A.), 2018년 공학 박사(D.Phil.) 학위를 받았다. 박사 논문 제목은 「Visual recognition of human communication」, 지도교수는 Andrew Zisserman이다.[^prof]

논문으로 본 전문 분야는 문자를 음성으로 바꾸는 모델의 경량화, 얼굴 영상과 음성의 대응, 소리·영상·글을 함께 처리하는 모델의 오류 완화, 감각 사이의 대응을 이용한 위치 추정, 수어와 화자 인식이다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7] 연구실 강의 목록에는 가을의 「Deep learning for visual understanding」(EE.40034)과 봄의 「Speech Recognition Systems」(EE.70038)가 있다.[^teaching]

## 응용 분야

대표 논문이 직접 다루는 쓰임은 문자에서의 음성 생성, 소리 없는 얼굴 영상에서의 음성 생성, 시청각 질문에 대한 답의 오류 완화, 장면 속 소리 출처 찾기, 촉각 입력에 대응하는 영상의 재질 영역 찾기, 연속 수어 인식, 환경 변화에 대응하는 화자 인식이다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7]

## 구성원

2026년 10월 26일 연구실 Members 페이지의 교수 외 구성원 29명이다. 박사후연구원 4명, 박사과정 10명, 석박사통합과정 6명, 석사과정 9명으로 게시돼 있다.[^members] "대표 논문 참여"는 위 대표 논문의 번호이며 전체 저자 이름을 구성원 이름과 대조했다. Kihyun Nam과 논문의 KiHyun Nam은 같은 이름으로 보았다.[^p7]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Youngjoon Jang | 박사후연구원 | 3, 6 |
| Kangwook Jang | 박사후연구원 |  |
| Jeongsoo Choi | 박사후연구원 | 2 |
| Kang Zhang | 박사후연구원 |  |
| Hyeongkeun Lee | 박사과정 |  |
| Kyeongha Rho | 박사과정 |  |
| Kihyun Nam | 박사과정 | 7 |
| Suyeon Lee | 박사과정 |  |
| Chaeyoung Jung | 박사과정 | 2, 3 |
| Jaehun Kim | 박사과정 | 1, 2 |
| Tan Dat Nguyen | 박사과정 | 1 |
| Seungwoo Lee | 박사과정 | 5 |
| Hyebin Cho | 박사과정 |  |
| Jihoo Jung | 박사과정 |  |
| Jaemin Jung | 석박사통합과정 |  |
| Doyeop Kwak | 석박사통합과정 |  |
| Youkyum Kim | 석박사통합과정 |  |
| Junseok Ahn | 석박사통합과정 |  |
| Jongbhin Woo | 석박사통합과정 |  |
| Seongyu Kim | 석박사통합과정 | 5 |
| Jongmin Choi | 석사과정 |  |
| Suho Yoo | 석사과정 |  |
| Jaewook Jeong | 석사과정 |  |
| Tae Wook Haam | 석사과정 |  |
| Siu Bae | 석사과정 |  |
| Sumin Park | 석사과정 |  |
| Adilkhan Alpysbay | 석사과정 |  |
| Gia Thinh Pham | 석사과정 |  |
| Seohyun Joo | 석사과정 |  |

## 졸업생과 이전 구성원

2026년 10월 26일 Members 페이지 Alumni의 8명이다. 박사 졸업생 4명, 석사 졸업생 2명, 이전 박사후연구원 2명이며 학위·기간과 진로는 연구실 표기다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Ji-Hoon Kim | PhD ('26) | Assistant Professor at Chung-Ang University |
| Hyeonggon Ryu | PhD ('26) | Assistant Professor at Hankuk University of Foreign Studies |
| Sooyoung Park | PhD ('26) | Researcher at ETRI |
| Arda Senocak | Postdoc ('22–'25) | Assistant Professor at UNIST |
| Dawit Mureja Argaw | PhD ('25) | Research Scientist at Netflix |
| Soyoon Kim | MS ('25) | Researcher at NAVER Cloud |
| Jiu Feng | MS ('24) | PhD Student at UT Austin |
| Jae Won Cho | Postdoc ('23–'24) | Assistant Professor at Sejong University |

## 최근 논문 목록 (2021–2026)

음성 생성·인식, 영상과 소리의 대응, 시청각 언어 모델, 수어와 영상 이해를 다룬 논문들이다. 연구실 Publications 페이지의 2022–2026년 구역 중 정준선 교수가 저자인 90편과 교수 개인 목록의 2021년 구역 10편을 합한 100편이다.[^pubs][^prof] 교수 개인 목록에는 이전 소속 시절 연구가 함께 있으며, 부임 연도가 2021년으로만 적혀 있어 2021년 항목을 부임 전후로 나누지 않았다.[^prof]

연도는 원문의 연도 구역이고 제목·저자·학회와 학술지 이름은 게시 표기다. 저자는 원문이 함께 제공하는 전체 이름으로 적고, co-first author는 원문이 밝힌 공동 1저자 표시다. 학회 이름과 연도만 적힌 항목은 발표·출판 완료 여부를 뜻하지 않는다. 대표 논문 3은 arXiv v2, 5는 CVPR 2026을 명시한 arXiv v1, 1·2·4·6·7은 연구실이 게시한 논문 PDF를 읽은 판이다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7]

**2026**

- Hyebin Cho, Suho Yoo, Jaehyuk Jang, Changick Kim, Joon Son Chung. "Who Wins the Conflict? Mechanistic Interpretability of Text Bias in Audio LLMs". *Conference on Empirical Methods in Natural Language Processing*.
- Chaeyoung Jung (co-first author), Youngjoon Jang (co-first author), Jongmin Choi, Joon Son Chung. "Fork-Merge Decoding: Enhancing Multimodal Understanding in Audio-Visual Large Language Models". *Findings of Empirical Methods in Natural Language Processing*.
- Seongyu Kim (co-first author), Seungwoo Lee (co-first author), Hyeonggon Ryu, Joon Son Chung, Arda Senocak. "See & Sniff: Learning Visuo-Olfactory Representations". *European Conference on Computer Vision*.
- Jaemin Jung (co-first author), Jaehun Kim (co-first author), Inkyu Shin, Joon Son Chung. "SCORE: Scaling audio generation using Standardized COmposite REwards". *IEEE Signal Processing Letters*.
- Doyeop Kwak (co-first author), Suyeon Lee (co-first author), Joon Son Chung. "Plug-and-Steer: Decoupling Separation and Selection in Audio-Visual Target Speaker Extraction". *Interspeech*.
- Jeongsoo Choi, Ji-Hoon Kim, Shujie Hu, Joon Son Chung. "ProsoCodec: Prosody-Oriented Speech Codec for Voice Conversion". *Interspeech*.
- Hyebin Cho, Jaehyuk Jang, Changick Kim, Joon Son Chung. "Acoustic Prompting via Stage-wise Modulation for Few-Shot Learning in Audio Language Models". *Interspeech*.
- Tan Dat Nguyen, Sangmin Bae, Joon Son Chung, Ji-Hoon Kim. "MamTra: A Hybrid Mamba-Transformer Backbone for Speech Synthesis". *Interspeech*.
- Jaemin Jung, Kyeongha Rho, Inkyu Shin, Joon Son Chung. "Inference-Time Scaling for Joint Audio-Video Generation". *Transactions on Machine Learning Research*.
- Sungnyun Kim (co-first author), Kangwook Jang (co-first author), Sungwoo Cho, Joon Son Chung, Hoirin Kim, Se-Young Yun. "Two Heads Are Better Than One: Audio-Visual Speech Error Correction with Dual Hypotheses". *Findings of the Association for Computational Linguistics*.
- Jihoo Jung, Chaeyoung Jung, Ji-Hoon Kim, Joon Son Chung. "Probing Cross-modal Information Hubs in Audio-Visual LLMs". *International Conference on Machine Learning*.
- Youngjoon Jang (co-first author), Jeongsoo Choi (co-first author), Junseok Ahn, Joon Son Chung. "Deep Understanding of Sign Language for Sign to Subtitle Alignment". *IEEE Transactions on Multimedia*.
- Kang Zhang (co-first author), Suyeon Lee (co-first author), Arda Senocak, Joon Son Chung. "Cinematic Audio Source Separation Using Visual Cues". *IEEE Conference on Computer Vision and Pattern Recognition*.
- Seongyu Kim, Seungwoo Lee, Hyeonggon Ryu, Joon Son Chung, Arda Senocak. "Seeing Through Touch: Tactile-Driven Visual Localization of Material Regions". *IEEE Conference on Computer Vision and Pattern Recognition*.
- Arda Senocak (co-first author), Sooyoung Park (co-first author), Tae-Hyun Oh, Joon Son Chung. "How Far Can We Go With Synthetic Data for Audio-Visual Sound Source Localization?". *IEEE Conference on Computer Vision and Pattern Recognition*.
- Hyeonggon Ryu, Joon Son Chung, David Harwath. "Hear you are: Teaching LLMs Spatial Reasoning with Vision and Spatial Sound". *IEEE Conference on Computer Vision and Pattern Recognition*.
- Doyeop Kwak, Youngjoon Jang, Seongyu Kim, Joon Son Chung. "EDNet: A Versatile Speech Enhancement Framework with Gating Mamba Mechanism and Phase Shift-Invariant Training". *IEEE Transactions on Audio, Speech and Language Processing*.
- Sooyoung Park (co-first author), Arda Senocak (co-first author), Joon Son Chung. "Hearing and Seeing Through CLIP: A Framework for Self-Supervised Sound Source Localization". *International Journal of Computer Vision*.
- Doyeop Kwak, Youngjoon Jang, Joon Son Chung. "LP-CFM: Perceptual Invariance-Aware Conditional Flow Matching for Speech Modeling". *International Conference on Acoustics, Speech, and Signal Processing*.
- Tan Dat Nguyen, Jaehun Kim, Ji-Hoon Kim, Shukjae Choi, Youshin Lim, Joon Son Chung. "SPADE: Structured Pruning and Adaptive Distillation for Efficient LLM-TTS". *International Conference on Acoustics, Speech, and Signal Processing*.
- The Hieu Pham (co-first author), Tan Dat Nguyen (co-first author), Phuong Thanh Tran, Joon Son Chung, Duc Dung Nguyen. "MAGE: A Coarse-to-Fine Speech Enhancer with Masked Generative Model". *International Conference on Acoustics, Speech, and Signal Processing*.
- Kihyun Nam (co-first author), Jongmin Choi (co-first author), Hyeongkeun Lee, Jungwoo Heo, Joon Son Chung. "Diffusion-Link: Diffusion Probabilistic Model for Bridging the Audio-Text Modality Gap". *International Conference on Acoustics, Speech, and Signal Processing*.
- Hyeongkeun Lee (co-first author), Jongmin Choi (co-first author), Kihyun Nam, Joon Son Chung. "LAMB: LLM-Based Audio Captioning with Modality Gap Bridging via Cauchy-Schwarz Divergence". *International Conference on Acoustics, Speech, and Signal Processing*.
- Jihoo Jung, Ji-Hoon Kim, Doyeop Kwak, Junwon Lee, Juhan Nam, Joon Son Chung. "UNMIXX: Untangling Highly Correlated Singing Voices Mixtures". *International Conference on Acoustics, Speech, and Signal Processing*.
- Chaeyoung Jung, Youngjoon Jang, Seungwoo Lee, Joon Son Chung. "FastAV: Efficient Token Pruning for Audio-Visual Large Language Model Inference". *International Conference on Acoustics, Speech, and Signal Processing*.

**2025**

- Arda Senocak (co-first author), Hyeonggon Ryu (co-first author), Junsik Kim, Tae-Hyun Oh, Hanspeter Pfister, Joon Son Chung. "Toward Interactive Sound Source Localization: Better Align Sight and Sound!". *IEEE Transactions on Pattern Analysis and Machine Intelligence*.
- Jee-weon Jung, Yihan Wu, Xin Wang, Ji-Hoon Kim, Soumi Maiti, Yuta Matsunaga, Hye-jin Shim, Jinchuan Tian, Nicholas Evans, Joon Son Chung, Wangyou Zhang, Seyun Um, Shinnosuke Takamichi, Shinji Watanabe. "SpoofCeleb: Speech Deepfake Detection and SASV In The Wild". *IEEE Open Journal of Signal Processing*.
- Ji-Hoon Kim, Hong-Sun Yang, Yoon-Cheol Ju, Il-Hwan Kim, Byeong-Yeol Kim, Joon Son Chung. "CrossSpeech++: Cross-lingual Speech Synthesis with Decoupled Language and Speaker Generation". *IEEE Transactions on Audio, Speech and Language Processing*.
- Chaeyoung Jung (co-first author), Youngjoon Jang (co-first author), Joon Son Chung. "AVCD: Mitigating Hallucinations in Audio-Visual Large Language Models through Contrastive Decoding". *Conference on Neural Information Processing Systems*.
- Kang Zhang, Trung X. Pham, Suyeon Lee, Axi Niu, Arda Senocak, Joon Son Chung. "Model-Guided Dual-Role Alignment for High-Fidelity Open-Domain Video-to-Audio Generation". *Conference on Neural Information Processing Systems*.
- Chenshuang Zhang, Kang Zhang, Joon Son Chung, In So Kweon, Junmo Kim, Chengzhi Mao. "Video Diffusion Models Excel at Tracking Similar-Looking Objects Without Supervision". *Conference on Neural Information Processing Systems*.
- Jeongsoo Choi (co-first author), Jaehun Kim (co-first author), Joon Son Chung. "Dub-S2ST: Textless Speech-to-Speech Translation for Seamless Dubbing". *Findings of Empirical Methods in Natural Language Processing*.
- Jeongsoo Choi, Ji-Hoon Kim, Sung-Bin Kim, Tae-Hyun Oh, Joon Son Chung. "AlignDiT: Multimodal Aligned Diffusion Transformer for Synchronized Speech Generation". *ACM International Conference on Multimedia*.
- Sung-Bin Kim, Jeongsoo Choi, Puyuan Peng, Joon Son Chung, Tae-Hyun Oh, David Harwath. "VoiceCraft-Dub: Automated Video Dubbing with Neural Codec Language Models". *International Conference on Computer Vision*.
- Chaeyoung Jung, Hojoon Ki, Ji-Hoon Kim, Junmo Kim, Joon Son Chung. "InfiniteAudio: Infinite-Length Audio Generation with Consistency". *Interspeech*.
- Kihyun Nam, Jungwoo Heo, Jee-weon Jung, Gangin Park, Chaeyoung Jung, Ha-Jin Yu, Joon Son Chung. "SEED: Speaker Embedding Enhancement Diffusion Model". *Interspeech*.
- Jeongsoo Choi (co-first author), Zhikang Niu (co-first author), Ji-Hoon Kim, Chunhui Wang, Joon Son Chung, Xie Chen. "Accelerating Diffusion-based Text-to-Speech Model Training with Dual Modality Alignment". *Interspeech*.
- Jee-weon Jung, Wangyou Zhang, Soumi Maiti, Yihan Wu, Xin Wang, Ji-Hoon Kim, Yuta Matsunaga, Seyun Um, Jinchuan Tian, Hye-jin Shim, Nicholas Evans, Joon Son Chung, Shinnosuke Takamichi, Shinji Watanabe. "The text-to-speech in the wild (TITW) dataset". *Interspeech*.
- Hyeonggon Ryu (co-first author), Seongyu Kim (co-first author), Joon Son Chung, Arda Senocak. "Seeing Speech and Sound: Distinguishing and Locating Audio Sources in Visual Scenes". *IEEE Conference on Computer Vision and Pattern Recognition*.
- Ji-Hoon Kim, Jeongsoo Choi, Jaehun Kim, Chaeyoung Jung, Joon Son Chung. "From Faces to Voices: Learning Hierarchical Representations for High-quality Video-to-Speech". *IEEE Conference on Computer Vision and Pattern Recognition*.
- Jaemin Jung (co-first author), Youngjoon Jang (co-first author), Joon Son Chung. "Test-Time Augmentation for Pose-invariant Face Recognition". *IEEE International Conference on Automatic Face and Gesture Recognition*.
- Dawit Mureja Argaw, Xian Liu, Qinsheng Zhang, Joon Son Chung, Ming-Yu Liu, Fitsum Reda. "High-Quality Joint Image and Video Compression with Causal VAE". *International Conference on Learning Representations*.
- Sung-Bin Kim (co-first author), Hyun-Bin Oh (co-first author), JungMok Lee, Arda Senocak, Joon Son Chung, Tae-Hyun Oh. "AVHBench: A Cross-Modal Hallucination Benchmark for Audio-Visual Large Language Models". *International Conference on Learning Representations*.
- Jeongsoo Choi (co-first author), Ji-Hoon Kim (co-first author), Jinyu Li, Joon Son Chung, Shujie Liu. "V2SFlow: Video-to-Speech Generation with Speech Decomposition and Rectified Flow". *International Conference on Acoustics, Speech, and Signal Processing*.
- Kyeongha Rho (co-first author), Hyeongkeun Lee (co-first author), Valentio Iverson, Joon Son Chung. "LAVCap: LLM-based Audio-Visual Captioning using Optimal Transport". *International Conference on Acoustics, Speech, and Signal Processing*.
- Jaemin Jung (co-first author), Junseok Ahn (co-first author), Chaeyoung Jung, Tan Dat Nguyen, Youngjoon Jang, Joon Son Chung. "VoiceDiT: Dual-Condition Diffusion Transformer for Environment-Aware Speech Synthesis". *International Conference on Acoustics, Speech, and Signal Processing*.
- Tan Dat Nguyen, Ji-Hoon Kim, Jeongsoo Choi, Shukjae Choi, Jinseok Park, Younglo Lee, Joon Son Chung. "Accelerating Codec-based Speech Synthesis with Multi-Token Prediction and Speculative Decoding". *International Conference on Acoustics, Speech, and Signal Processing*.
- Jaehun Kim, Ji-Hoon Kim, Yeunju Choi, Tan Dat Nguyen, Seongkyu Mun, Joon Son Chung. "AdaptVC: High Quality Voice Conversion with Adaptive Learning". *International Conference on Acoustics, Speech, and Signal Processing*.

**2024**

- Mehmet Hamza Erol (co-first author), Arda Senocak (co-first author), Jiu Feng, Joon Son Chung. "Audio Mamba: Bidirectional State Space Model for Audio Representation Learning". *IEEE Signal Processing Letters*.
- Youkyum Kim (co-first author), Jaemin Jung (co-first author), Jihwan Park, Byeong-Yeol Kim, Joon Son Chung. "Bridging the Gap between Audio and Text using Parallel-attention for User-defined Keyword Spotting". *IEEE Signal Processing Letters*.
- Jongbhin Woo, Hyeonggon Ryu, Youngjoon Jang, Jae Won Cho, Joon Son Chung. "Let Me Finish My Sentence: Video Temporal Grounding with Holistic Text Understanding". *ACM International Conference on Multimedia*.
- Junseok Ahn, Youkyum Kim, Yeunju Choi, Doyeop Kwak, Ji-Hoon Kim, Seongkyu Mun, Joon Son Chung. "VoxSim: A perceptual voice similarity dataset". *Interspeech*.
- Jaesong Lee (co-first author), Soyoon Kim (co-first author), Hanbyul Kim, Joon Son Chung. "Lightweight Audio Segmentation for Long-form Speech Translation". *Interspeech*.
- Jiu Feng, Mehmet Hamza Erol, Joon Son Chung, Arda Senocak. "ElasticAST: An Audio Spectrogram Transformer for All Length and Resolutions". *Interspeech*.
- Jee-weon Jung (co-first author), Xin Wang (co-first author), Nicholas Evans, Shinji Watanabe, Hye-jin Shim, Hemlata Tak, Siddhant Arora, Junichi Yamagishi, Joon Son Chung. "To what extent can ASV systems naturally defend against spoofing attacks?". *Interspeech*.
- Kihyun Nam, Hee-Soo Heo, Jee-weon Jung, Joon Son Chung. "Disentangled Representation Learning for Environment-agnostic Speaker Recognition". *Interspeech*.
- Chaeyoung Jung, Suyeon Lee, Ji-Hoon Kim, Joon Son Chung. "FlowAVSE: Efficient Audio-Visual Speech Enhancement with Conditional Flow Matching". *Interspeech*.
- Jongsuk Kim (co-first author), Hyeongkeun Lee (co-first author), Kyeongha Rho (co-first author), Junmo Kim, Joon Son Chung. "EquiAV: Leveraging Equivariance for Audio-Visual Contrastive Learning". *International Conference on Machine Learning*.
- Youngjoon Jang (co-first author), Ji-Hoon Kim (co-first author), Junseok Ahn, Doyeop Kwak, Hongsun Yang, Yooncheol Ju, Ilhwan Kim, Byeong-Yeol Kim, Joon Son Chung. "Faces that Speak: Jointly Synthesising Talking Face and Speech from Text". *IEEE Conference on Computer Vision and Pattern Recognition*.
- Dawit Mureja Argaw, Seunghyun Yoon, Fabian Caba Heilbron, Hanieh Deilamsalehy, Trung Bui, Zhaowen Wang, Franck Dernoncourt, Joon Son Chung. "Scaling Up Video Summarization Pretraining with Large Language Models". *IEEE Conference on Computer Vision and Pattern Recognition*.
- Dawit Mureja Argaw, Mattia Soldan, Alejandro Pardo, Chen Zhao, Fabian Caba Heilbron, Joon Son Chung, Bernard Ghanem. "Towards Automated Movie Trailer Generation". *IEEE Conference on Computer Vision and Pattern Recognition*.
- Tan Dat Nguyen (co-first author), Ji-Hoon Kim (co-first author), Youngjoon Jang, Jaehun Kim, Joon Son Chung. "FreGrad: Lightweight and fast frequency-aware diffusion vocoder". *International Conference on Acoustics, Speech, and Signal Processing*.
- Junseok Ahn (co-first author), Youngjoon Jang (co-first author), Joon Son Chung. "SlowFast Network for Continuous Sign Language Recognition". *International Conference on Acoustics, Speech, and Signal Processing*.
- Hee-Soo Heo, Kihyun Nam, Bong-Jin Lee, Youngki Kwon, Minjae Lee, You Jin Kim, Joon Son Chung. "Rethinking Session Variability: Leveraging Session Embeddings for Session Robustness in Speaker Verification". *International Conference on Acoustics, Speech, and Signal Processing*.
- Jongbhin Woo, Hyeonggon Ryu, Arda Senocak, Joon Son Chung. "Speech Guided Masked Image Modeling for Visually Grounded Speech". *International Conference on Acoustics, Speech, and Signal Processing*.
- Doyeop Kwak (co-first author), Jaemin Jung (co-first author), Kihyun Nam, Youngjoon Jang, Jee-weon Jung, Shinji Watanabe, Joon Son Chung. "VoxMM: Rich Transcription of Conversations in the Wild". *International Conference on Acoustics, Speech, and Signal Processing*.
- Jiu Feng (co-first author), Mehmet Hamza Erol (co-first author), Joon Son Chung, Arda Senocak. "From Coarse To Fine: Efficient Training for Audio Spectrogram Transformers". *International Conference on Acoustics, Speech, and Signal Processing*.
- Yeonghyeon Lee, Inmo Yeon, Juhan Nam, Joon Son Chung. "VoiceLDM: Text-to-Audio Generation with Linguistic Content". *International Conference on Acoustics, Speech, and Signal Processing*.
- Chaeyoung Jung (co-first author), Suyeon Lee (co-first author), Kihyun Nam, Kyeongha Rho, You Jin Kim, Youngjoon Jang, Joon Son Chung. "TalkNCE: Improving Active Speaker Detection with Talking-Aware Contrastive Learning". *International Conference on Acoustics, Speech, and Signal Processing*.
- Suyeon Lee (co-first author), Chaeyoung Jung (co-first author), Youngjoon Jang, Jaehun Kim, Joon Son Chung. "Seeing Through the Conversation: Audio-Visual Speech Separation based on Diffusion Model". *International Conference on Acoustics, Speech, and Signal Processing*.
- Ji-Hoon Kim (co-first author), Jaehun Kim (co-first author), Joon Son Chung. "Let There Be Sound: Reconstructing High Quality Speech from Silent Videos". *AAAI Conference on Artificial Intelligence*.
- Sooyoung Park (co-first author), Arda Senocak (co-first author), Joon Son Chung. "Can CLIP Help Sound Source Localization?". *Winter Conference on Applications of Computer Vision*.

**2023**

- Youngjoon Jang (co-first author), Kyeongha Rho (co-first author), Jongbhin Woo, Hyeongkeun Lee, Jihwan Park, Youshin Lim, Byeong-Yeol Kim, Joon Son Chung. "That's What I Said: Fully-Controllable Talking Face Generation". *ACM International Conference on Multimedia*.
- Arda Senocak (co-first author), Hyeonggon Ryu (co-first author), Junsik Kim, Tae-Hyun Oh, Hanspeter Pfister, Joon Son Chung. "Sound Source Localization is All about Cross-Modal Alignment". *International Conference on Computer Vision*.
- Jiu Feng (co-first author), Mehmet Hamza Erol (co-first author), Joon Son Chung, Arda Senocak. "FlexiAST: Flexibility is What AST Needs". *Interspeech*.
- Kihyun Nam (co-first author), Youkyum Kim (co-first author), Jaesung Huh, Hee-Soo Heo, Jee-weon Jung, Joon Son Chung. "Disentangled Representation Learning for Multilingual Speaker Recognition". *Interspeech*.
- Hee-Soo Heo, Jee-weon Jung, Jingu Kang, Youngki Kwon, Bong-Jin Lee, You Jin Kim, Joon Son Chung. "Curriculum learning for self-supervised speaker verification". *Interspeech*.
- Youngjoon Jang, Youngtaek Oh, Jae Won Cho, Myungchul Kim, Dong-Jin Kim, In So Kweon, Joon Son Chung. "Self-sufficient framework for continuous sign language recognition". *International Conference on Acoustics, Speech, and Signal Processing*.
- Jaemin Jung (co-first author), Youkyum Kim (co-first author), Jihwan Park, Youshin Lim, Byeong-Yeol Kim, Youngjoon Jang, Joon Son Chung. "Metric learning for user-defined keyword spotting". *International Conference on Acoustics, Speech, and Signal Processing*.
- Hyeonggon Ryu (co-first author), Arda Senocak (co-first author), In So Kweon, Joon Son Chung. "Hindi as a second language: improving visually grounded speech with semantically similar samples". *International Conference on Acoustics, Speech, and Signal Processing*.
- Sooyoung Park (co-first author), Arda Senocak (co-first author), Joon Son Chung. "MarginNCE: Robust Sound Localization with a Negative Margin". *International Conference on Acoustics, Speech, and Signal Processing*.
- You Jin Kim, Hee-Soo Heo, Jee-weon Jung, Youngki Kwon, Bong-Jin Lee, Joon Son Chung. "Advancing the dimensionality reduction of speaker embeddings for speaker diarisation: disentangling noise and informing speech activity". *International Conference on Acoustics, Speech, and Signal Processing*.
- Jee-weon Jung, Bong-Jin Lee, Jaesung Huh, Andrew Brown, Youngki Kwon, Shinji Watanabe, Joon Son Chung. "In search of strong embedding extractors for speaker diarisation". *International Conference on Acoustics, Speech, and Signal Processing*.
- Jiyoung Lee, Joon Son Chung, Soo-Whan Chung. "Imaginary Voice: Face-styled Diffusion Model for Text-to-Speech". *International Conference on Acoustics, Speech, and Signal Processing*.

**2022**

- Youngjoon Jang, Youngtaek Oh, Jae Won Cho, Dong-Jin Kim, Joon Son Chung, In So Kweon. "Signing Outside the Studio: Benchmarking Background Robustness for Continuous Sign Language Recognition". *British Machine Vision Conference*.
- Jingu Kang, Jaesung Huh, Hee-Soo Heo, Joon Son Chung. "Augmentation adversarial training for self-supervised speaker representation learning". *Journal of Selected Topics in Signal Processing*.
- Jee-weon Jung (co-first author), You Jin Kim (co-first author), Hee-Soo Heo, Bong-Jin Lee, Youngki Kwon, Joon Son Chung. "Pushing the limits of raw waveform speaker recognition". *Interspeech*.
- Namkyu Jung, Geonmin Kim, Joon Son Chung. "Spell my name: Keyword boosted speech recognition". *International Conference on Acoustics, Speech, and Signal Processing*.
- Youngki Kwon, Hee-Soo Heo, Jee-weon Jung, You Jin Kim, Bong-Jin Lee, Joon Son Chung. "Multi-scale speaker embedding-based graph attention networks for speaker diarisation". *International Conference on Acoustics, Speech, and Signal Processing*.
- Jee-weon Jung, Hee-Soo Heo, Hemlata Tak, Hye-jin Shim, Joon Son Chung, Bong-Jin Lee, Ha-Jin Yu, Nicholas Evans. "AASIST: Audio Anti-Spoofing using Integrated Spectro-Temporal Graph Attention Networks". *International Conference on Acoustics, Speech, and Signal Processing*.

**2021**

- Youngki Kwon, Jee-weon Jung, Hee-Soo Heo, You Jin Kim, Bong-Jin Lee, Joon Son Chung. "Adapting Speaker Embeddings for Speaker Diarization". *Interspeech*.
- Jee-weon Jung, Hee-Soo Heo, Youngki Kwon, Joon Son Chung, Bong-Jin Lee. "Three-class Overlapped Speech Detection using a Convolutional Recurrent Neural Network". *Interspeech*.
- You Jin Kim, Hee-Soo Heo, Soyeon Choe, Soo-Whan Chung, Yoohwan Kwon, Bong-Jin Lee, Youngki Kwon, Joon Son Chung. "Look Who's Talking: Active Speaker Detection in the Wild". *Interspeech*.
- Andrew Brown (co-first author), Jaesung Huh (co-first author), Arsha Nagrani (co-first author), Joon Son Chung, Andrew Zisserman. "Playing a Part: Speaker Verification at the Movies". *International Conference on Acoustics, Speech, and Signal Processing*.
- Yoohwan Kwon (co-first author), Hee-Soo Heo (co-first author), Bong-Jin Lee, Joon Son Chung. "The ins and outs of speaker recognition: lessons from VoxSRC 2020". *International Conference on Acoustics, Speech, and Signal Processing*.
- Jee-weon Jung (co-first author), Hee-Soo Heo (co-first author), Ha-Jin Yu, Joon Son Chung. "Graph Attention Networks for Speaker Verification". *International Conference on Acoustics, Speech, and Signal Processing*.
- Youngki Kwon, Hee-Soo Heo, Jaesung Huh, Bong-Jin Lee, Joon Son Chung. "Look who's not talking". *IEEE Spoken Language Technology Workshop*.
- Jaesung Huh (co-first author), Minjae Lee (co-first author), Hee-Soo Heo, Seongkyu Mun, Joon Son Chung. "Metric Learning for Keyword Spotting". *IEEE Spoken Language Technology Workshop*.
- Seong Min Kye, Yoohwan Kwon, Joon Son Chung. "Cross attentive pooling for speaker verification". *IEEE Spoken Language Technology Workshop*.
- Seong Min Kye, Joon Son Chung, Hoirin Kim. "Supervised attention for speaker recognition". *IEEE Spoken Language Technology Workshop*.

## 수상과 선정

연구실 논문 목록의 2023년 ICASSP 논문 선정 표기 1건이다.[^pubs]

- 2023 · 연속 수어 인식 논문 「Self-sufficient framework for continuous sign language recognition」이 ICASSP Paper Recognition에 선정됨

## 연락과 위치

- 교수 이메일: joonsc@kaist.ac.kr[^ee]
- 교수 사무실: LG이노베이션홀(N24) 3102호[^ee][^prof]
- 학과 게시 연락처: 7470[^ee]
- 연구실 게시 주소: 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea[^home]

## 근거와 출처

자료별 주소, 표기 차이, 목록 범위와 대표 논문 선정 근거는 [근거 페이지](mm-sources.md)에 정리했다.
[^home]: 연구실 누리집 첫 화면, 연구실 이름·소속·주소. <https://mm.kaist.ac.kr/> (2026-10-26 열람).
[^members]: 연구실 Members, 교수·현재 구성원·졸업생과 이전 구성원. <https://mm.kaist.ac.kr/members/> (2026-10-26 열람).
[^pubs]: 연구실 Publications, 연도별 제목·전체 저자·학회와 학술지, 논문 선정 표기. <https://mm.kaist.ac.kr/pubs/> (2026-10-26 열람).
[^teaching]: 연구실 Teaching, 강의명·과목 번호·계절. <https://mm.kaist.ac.kr/teaching/> (2026-10-26 열람).
[^prof]: 정준선 교수 소개, 이름·직위·소속·경력·학력과 개인 논문 목록. <https://mm.kaist.ac.kr/joon/> (2026-10-27 열람).
[^ee]: KAIST 전기및전자공학부 전임교수 명단의 정준선 항목, 부교수·연구 분야·사무실·연락처·학교 이메일. <https://ee.kaist.ac.kr/professor-s1/3/> (2026-10-27 열람).
[^meta]: KAIST 메타버스대학원 교수진, 정준선의 소속 전기및전자공학부와 겸임(Joint). <https://meta.kaist.ac.kr/professors/> (2026-10-27 열람).
[^metalabs]: KAIST 메타버스대학원 참여 연구실, Multimodal AI Lab과 담당교수 정준선. <https://meta.kaist.ac.kr/labs/> (2026-10-26 열람).
[^p1]: T. D. Nguyen 외, J. S. Chung. <https://mm.kaist.ac.kr/pubs/pdfs/nguyen26a.pdf> 초록 기준(연구실 게시 논문 PDF). 초록 원문 <https://mm.kaist.ac.kr/pubs/pdfs/nguyen26a.pdf> (2026-10-27 열람).
[^p2]: J.-H. Kim 외, J. S. Chung. <https://mm.kaist.ac.kr/pubs/pdfs/kim25b.pdf> 초록 기준(연구실 게시 논문 PDF). 초록 원문 <https://mm.kaist.ac.kr/pubs/pdfs/kim25b.pdf> (2026-10-27 열람).
[^p3]: C. Jung, Y. Jang, J. S. Chung, arXiv (온라인 2025-05-27). <https://arxiv.org/abs/2505.20862> 초록 기준(arXiv 판). 확인한 판: arXiv v2, 2025-09-30. 초록 원문 <https://arxiv.org/abs/2505.20862> (2026-10-27 열람).
[^p4]: A. Senocak 외, J. S. Chung. <https://mm.kaist.ac.kr/pubs/pdfs/senocak23a.pdf> 초록 기준(연구실 게시 논문 PDF). 초록 원문 <https://mm.kaist.ac.kr/pubs/pdfs/senocak23a.pdf> (2026-10-27 열람).
[^p5]: S. Kim 외, A. Senocak, arXiv (온라인 2026-04-13). <https://arxiv.org/abs/2604.11579> 초록 기준(arXiv 판). 확인한 판: arXiv v1, CVPR 2026 (arXiv Comments). 초록 원문 <https://arxiv.org/abs/2604.11579> (2026-10-27 열람).
[^p6]: Y. Jang 외, J. S. Chung. <https://mm.kaist.ac.kr/pubs/pdfs/jang23a.pdf> 초록 기준(연구실 게시 논문 PDF). 초록 원문 <https://mm.kaist.ac.kr/pubs/pdfs/jang23a.pdf> (2026-10-27 열람).
[^p7]: K. Nam, H.-S. Heo, J.-w. Jung, J. S. Chung. <https://mm.kaist.ac.kr/pubs/pdfs/nam24a.pdf> 초록 기준(연구실 게시 논문 PDF). 초록 원문 <https://mm.kaist.ac.kr/pubs/pdfs/nam24a.pdf> (2026-10-27 열람).

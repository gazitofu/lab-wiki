# 휴먼인터페이스 연구실 (Human Interface Laboratory)

**서울대학교 공과대학 전기·정보공학부 · 김남수 교수**

- 분야: 음성 신호 처리(음성 인식, 음성 합성, 음성 향상, 음성 부호화), 화자 인식과 위조 음성 검출, 오디오 신호 처리(실감 음향, 음향 장면 인식, 음원 위치 추정, 음원 분리), 음성·오디오를 위한 기계 학습, 대형 언어 모델
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: 음향·오디오 AI[^home][^audio][^p8], 생성 인공지능[^p2], 대형 언어 모델[^home], 모델 경량화·양자화[^p4]
- 홈페이지: <https://hi.snu.ac.kr/>
- 근거와 출처: [휴먼인터페이스 연구실 근거 페이지](hi-sources.md)

> 사람의 말소리와 여러 소리를 다루는 음성·오디오 신호 처리 연구실로, 음성 인식·합성·향상과 화자 인식, 실감 음향·음향 장면 인식·음원 분리 같은 오디오 처리를 기계 학습으로 연구하고 대형 언어 모델 연구도 함께 한다.[^home][^overview]

## 무엇을 연구하나

휴먼인터페이스 연구실은 서울대학교 공과대학 전기·정보공학부 김남수 교수가 이끄는 연구실이다.[^ecelab][^ecelabv] 누리집 첫 화면은 연구실이 1998년에 세워졌고 김남수 교수의 지도 아래 음성·오디오 신호 처리(말소리와 여러 소리를 신호로 받아 분석하고 가공하는 기술)를 연구한다고 소개한다. 지금 진행하는 연구 주제로는 음성 인식, 음성 합성, 음성 향상, 실감 음향, 음향 사건 검출, 음원 분리, 음원 위치 추정을 들고 기계 학습을 응용한다고 적으며, 음성과 오디오에만 머물지 않고 대형 언어 모델(LLM, Large Language Model; 많은 글을 학습해 글을 이해하고 만들어 내는 큰 인공지능 모델) 분야의 연구도 다룬다고 밝힌다.[^home] 국문 소개는 연구실이 2007년 국가 지정 연구실로 선정되었고, 음성 신호 처리와 그 응용을 연구하며, 대표적으로 음성 인식, 합성, 화자 인식, 향상 분야에서 활발하게 연구한다고 적는다.[^home] 전기·정보공학부 연구실 목록은 이 연구실을 멀티미디어 신호처리 연구그룹과 인공지능 및 머신러닝 연구그룹 두 곳에 올리고, 연구실 상세는 연구 분야를 「인공지능, 음성음향신호처리」로 적는다.[^ecelab][^ecelabv] 연구실 상세의 소개 글은 연구 분야를 음성 신호 처리와 알고리즘 구현·응용으로 설명하고, 대용량 연속어 인식 시스템·화자 인식·화자 적응·발음 검증·인식 시스템의 신뢰도를 다루는 음성 인식, 음향학적 모델링·자연음 합성·운율 제어 기법을 개발하는 음성 합성, 잡음 제거·반향 제거·신호 분리 기법을 개발하는 음성 강화, 저장과 전송을 효율화하는 저 전송률·고음질의 음성·오디오 부호화기를 연구하는 음성 코딩과 오디오 코딩을 든다.[^ecelabv]

누리집의 연구 소개는 연구를 음성 신호 처리, 인공지능과 기계 학습, 오디오 신호 처리 세 묶음으로 나눈다.[^overview] 음성 신호 처리 묶음의 첫째는 음성 인식(ASR, Automatic Speech Recognition)이다. 말소리를 받아 글자로 바꾸는 일로, 사람과 기계 사이 인터페이스의 핵심 기술이라고 적고, 음성 신호의 특성을 나타내도록 학습하는 음향 모델과 여러 간섭으로 일그러진 음성 특징을 바로잡는 특징 보상의 두 분야로 나눈다. 음향 모델에는 예전에 가우스 혼합 모델(GMM, Gaussian Mixture Model)을 널리 썼지만 지금은 성능이 뛰어난 심층 신경망(DNN, Deep Neural Network; 여러 층의 인공 신경망을 쌓은 기계 학습 모델)을 활발히 연구한다고 적는다.[^speech] 둘째 음성 합성은 주어진 글을 말소리로 만드는 기술이다. 사람에 가까운 자연스러움과 알아듣기 쉬움을 목표로 하는 고품질 음성 합성(보코더, 음향 모델 개선, 후처리)과, 한 사람의 합성 시스템을 적은 자료로 만드는 화자 적응 음성 합성(목표 화자 적응, 감정 음성 합성, 노래 음성 합성)으로 나눈다.[^speech] 셋째 음성 향상은 오디오 신호 처리 기법으로 일그러진 음성의 명료도와 품질을 높이는 기술로, 잡음 제거(단일 채널과 다채널), 반향 제거와 잔향 제거, 음성 명료도 향상(필터링, 대역폭 확장)을 다룬다.[^speech] 넷째 음성 부호화는 음성이 담긴 디지털 오디오 신호의 데이터 압축으로, 음성 신호를 나타내는 데 드는 비트 수를 줄여 전송 대역폭이나 저장 비용을 줄이는 것이 목적이다. 원천 부호화(고효율 오디오 부호화)와 채널 부호화(오류에 강한 오디오 부호화)로 나눈다.[^speech]

인공지능과 기계 학습 묶음은 음성·오디오 신호 처리와 관련된 인공지능의 연구 영역으로 음성 인식, 기계 청각(machine hearing), 대화 시스템, 청각 장면 이해를 든다. 음성·오디오 신호 처리는 오디오 신호에서 목적에 맞는 정보를 찾아 분류하거나 추정하는 분야이며 지금 기계 학습 기법을 쓰는 선도적인 분야라고 적는다.[^aiml] 연구실은 은닉 마르코프 모델(HMM, Hidden Markov Model)과 서포트 벡터 머신(SVM, Support Vector Machine) 같은 기계 학습을 음성·오디오 신호 처리에 응용해 왔고, 최근에는 DNN과 비음수 행렬 분해(NMF, Non-negative Matrix Factorization) 같은 최신 기법의 응용과 개발에 집중해 왔다고 적는다.[^aiml]

오디오 신호 처리 묶음에는 다섯 주제가 있다. 실감 음향 기술은 악기 소리가 악기의 지향 특성과 공연장의 실내 임펄스 응답 같은 요소의 영향을 받은 뒤 듣는 사람에게 닿는다는 데서 출발해, 무향실에서 녹음한 음원과 측정한 실내 임펄스 응답으로 공간 음향을 재현하는 방법을 다루며, 머리 전달 함수와 파면 합성, 앰비소닉을 주제로 든다.[^audio] 음향 장면 인식은 소리 환경을 계산으로 분석하고 그 안의 개별 소리 사건을 알아보는 일로, 사람·자연·기계의 소리 사건을 알아보는 음향 사건 검출과 소리만으로 녹음 장소의 환경을 알아내는 환경 장면 분류를 다룬다.[^audio] 음원 위치 추정은 음장(공간에 퍼진 소리의 분포)의 여러 측정값으로 소리를 내는 곳이나 마이크의 위치를 찾거나 따라가는 분야로, 음원 위치 추정·추적과 소리를 이용한 실내 위치 측정을 다룬다.[^audio] 사운드 코드는 오디오 데이터 은닉 기술로 데이터를 소리에 넣어 스피커로 틀고, 마이크가 달린 스마트 기기로 원래 메시지를 풀어내는 무선 데이터 전송 방식이다. 들리는 주파수 범위 안에서 신호를 부호화하고, 일반 스피커로 재생할 수 있으며, 여러 오디오 코덱에 강하고, 음질이 원래 소리와 비슷하다는 특징을 든다.[^audio] 음원 분리는 목표 소리와 배경 잡음이 섞인 신호에서 원하는 신호 하나 또는 여럿을 뽑아내는 기술로, 단일 채널 분리와 다채널 분리를 다룬다.[^audio]

첫째 갈래는 **음성 합성**이다. 글을 말소리로 바꾸는 음성 합성(TTS, Text-to-Speech)에서 대표 논문은 정렬을 위한 보조 길이 예측기나 자기회귀(앞서 만든 결과를 보고 다음 결과를 차례로 만드는 방식) 순서 모델링 없이 글 임베딩(글을 숫자 벡터로 바꾼 표현)을 프레임(음성을 일정한 길이로 나눈 시간 구간) 단위 특징의 구간으로 바꾸는 SegINR을 제시했고,[^p1] 잡음 제거 확산 틀(자료에 잡음을 더해 가는 과정을 거꾸로 되짚으며 잡음에서 자료를 만들어 내는 생성 방식)로 잡음 신호를 멜 스펙트로그램(사람의 음높이 감각에 맞춘 멜 눈금의 주파수 축으로 소리의 시간별 주파수 성분을 나타낸 자료)으로 바꾸는 비자기회귀(결과 전체를 한꺼번에 만드는 방식) 음성 합성 모델 Diff-TTS를 만들었다.[^p2] 최근 논문 목록에는 신경망 트랜스듀서(음성 특징과 이미 낸 출력을 함께 보고 다음 출력을 정하는 신경망 구조)로 의미 토큰(말소리의 내용을 나타내도록 뽑은 이산 기호)을 예측하는 2단계 음성 합성(IEEE Transactions on Audio, Speech and Language Processing, 2025), 자료가 적은 언어와 여러 언어, 처음 보는 화자를 다루는 다화자 음성 합성에 전이 학습(한 과제에서 배운 모델을 다른 과제에 옮겨 쓰는 학습)을 쓴 연구(IEEE/ACM Transactions on Audio, Speech, and Language Processing, 2024), 증거 딥러닝(예측과 함께 그 예측의 불확실성을 증거의 양으로 내놓도록 학습하는 딥러닝 방법)을 쓴 제로샷 음성 합성(학습에 쓰지 않은 화자의 목소리로 합성하는 방식) Evidential-TTS(ICASSP 2025), 노래 음성 합성 학습 방법 MakeSinger(Interspeech 2024), 긴 대화 음성 합성 ZipL-Dialog(누리집 표기 Proc. Interspeech, Sep.2026)도 있다.[^ijournal][^iconf]

둘째 갈래는 **음성 인식과 모델 경량화**다. 대표 논문은 말이 들어오는 대로 글자로 바꾸는 스트리밍 트랜스듀서 모델을 학습할 때 학습과 추론이 어긋나 생기는 가능도(모델이 관측한 자료를 낼 확률)의 차이를 수학적으로 나타내고 정확한 가능도를 추정하는 FoCCE를 제시했고,[^p3] 사전 학습(많은 자료로 일반적인 표현을 먼저 배워 두는 학습)한 HuBERT 모델이 중간 층에서 추론을 일찍 멈출 수 있게 하는 조기 종료 방식 HuBERT-EE로 음성 인식을 빠르게 했다.[^p4] 최근 논문 목록에는 경량 RNN-T(순환 신경망 트랜스듀서, Recurrent Neural Network Transducer)를 학습시키는 표본 추출 기반 가지치기(신경망의 연결이나 매개변수 일부를 잘라 내 모델을 줄이는 일) 지식 증류(이미 학습한 교사 모델의 출력을 학생 모델이 따라 배우게 하는 학습 방법) 연구(IEEE Signal Processing Letters, 2025), CTC(Connectionist Temporal Classification; 입력과 출력의 정렬을 모른 채 순서열을 학습하는 방법) 기반 음성 인식을 위한 지식 증류 Cons-KD(IEEE Access, 2024)와 Oracle Teacher(IEEE/ACM Transactions on Audio, Speech, and Language Processing, 2023), 종단형(입력에서 출력까지를 신경망 하나로 바로 학습하는) 음성 인식을 위한 지식 증류 TutorNet(같은 학술지, 2021), 순서열 학습을 위한 자기 증류(모델이 자신의 출력으로 다시 배우는 증류) EM-Network(ICML 2023)도 있다.[^ijournal][^iconf] 과제 목록에는 삼성전자 DS의 「LLM과 Diffusion 모델의 경량화」(2025년 10월–2030년 9월)와 관악아날로그 주식회사의 「AI 보드를 위한 AI 알고리즘 경량화 작업」(2025년)이 있다.[^projects]

셋째 갈래는 **화자 인식과 위조 음성 검출**이다. 화자 인식은 목소리로 말한 사람을 알아보는 기술이고, 그 가운데 화자 검증은 어떤 음성이 주장한 사람의 목소리인지 가리는 일이다. 대표 논문은 정답 표시 없이 화자 표현을 배우는 자기 지도 학습 전략(앞단의 부트스트랩 평형 학습과 뒷단의 확률적 화자 임베딩(목소리의 특징을 담은 숫자 벡터) 학습)을 제안했고,[^p5] 음성 합성·음성 변환(한 사람의 말소리를 다른 사람의 목소리로 바꾸는 기술) 기술의 발전으로 늘어난 위조 공격에 맞서, 학습 때 보지 못한 공격에도 강인하도록 모델의 불확실성을 예측에 넣는 가짜 음성 검출 틀 FADEL을 만들었다.[^p6] 최근 논문 목록에는 깊은 화자 임베딩을 위한 일반화된 점수 비교 기반 학습 목표(IEEE Access, 2025), 불확실성을 고려한 증거 점수를 쓰는 종단형 화자 검증(ICASSP 2026), EM-Network를 쓴 종단형 신경망 화자 분할(여러 사람이 말한 녹음에서 누가 언제 말했는지 나누는 일) EEND-EM(APSIPA ASC 2024)도 있다.[^ijournal][^iconf] Notice 게시판이 옮긴 2024년 7월 연합뉴스TV 보도는 서울대학교 연구진이 화자 인식 기술로 보이스피싱 음성분석 모델을 개발했다고 전하고,[^news] 과제 목록에는 경찰청 치안과학기술 연구개발사업의 「성문분석 프로그램 고도화 기술 개발」(2023년, 2024–2025년)과 과학기술정보통신부의 「책임감 있는 AI를 위한 생성형 콘텐츠 검출 및 검증 연구」(2025–2028년)가 있다.[^projects]

넷째 갈래는 **음성 향상과 신경망 오디오 코덱**이다. 대표 논문은 기존 신경망 오디오 코덱의 문제를 분석해 분산을 제약하는 설계와 왜곡 없는 판별기(생성한 소리와 진짜 소리를 가려 생성 신경망의 학습을 돕는 신경망)를 제안한 실시간 스트리밍 오디오 코덱 HILCodec을 만들었고,[^p7] 확산 시간 단계를 입력 신호의 신호 대 잡음비(신호 세기와 잡음 세기의 비)에 맞추는 일관성 확산 음성 향상 틀을 제안했다.[^p8] 최근 논문 목록에는 속도에 맞춰 최적화한 스트리밍 신경망 음성 향상 모델 FastEnhancer(ICASSP 2026), 저비트율 음성 코덱을 위한 신경망 최적화 복호기(IEEE Signal Processing Letters, 2022), GAN(생성적 적대 신경망, Generative Adversarial Network) 기반 음성 향상의 다중 해상도 접근(Applied Sciences, 2021)도 있다.[^ijournal][^iconf]

연구실은 말소리와 함께 글과 언어도 다룬다. 최근 논문 목록에는 한국어 구어의 의도 파악을 위한 말뭉치(연구용으로 모은 글이나 말의 자료 묶음) 연구(ACM Transactions on Asian and Low-Resource Language Information Processing, 2022), 한국어 토큰화(글을 낱말 같은 처리 단위로 나누는 일)를 위한 공개 말뭉치 OpenKorPOS와 한국어 질문·명령의 문체별 바꿔 쓰기 말뭉치 StyleKQC(LREC 2022), 한국어 음성을 영어로 옮기는 번역 말뭉치 kosp2e(Interspeech 2021), 번역 성별 편향의 언어 간 일반화(ACM FAccT 2021)가 있다.[^ijournal][^iconf] 국내 학회 논문 목록의 2024–2026년 항목에는 Llama2 기반 수학적 추론 성능 비교, 소형 오디오 LLM의 추론 성능 향상, 대형 오디오 언어 모델의 오디오-텍스트 정렬(NEAT), 검색을 활용한 LLM 생성 글 검출 같은 대형 언어 모델 연구가 있고,[^dconf] 과제 목록에는 정보통신산업진흥원 첨단 GPU 활용 지원 사업의 「한국형 전이중(Full-Duplex) Audio-Language 모델 개발」(2026년)과 LG전자 기술협력 「AI-Generated Text Detection 기법 연구」(2026–2027년)가 있다.[^projects]

## 주요 연구 주제

### 1. 음성 합성

글 임베딩을 프레임 단위 특징 구간으로 바로 바꾸는 신경망 음성 합성(SegINR), 확산 모델로 멜 스펙트로그램을 만드는 비자기회귀 음성 합성(Diff-TTS), 제로샷 다화자 합성과 노래 음성 합성.[^p1][^p2][^iconf]

### 2. 음성 인식과 모델 경량화

스트리밍 트랜스듀서 음성 인식의 가능도 학습(FoCCE), 사전 학습 음성 모델의 조기 종료(HuBERT-EE), 음성 인식 모델의 지식 증류.[^p3][^p4][^ijournal]

### 3. 화자 인식과 위조 음성 검출

자기 지도 화자 표현 학습과 확률적 화자 임베딩, 불확실성을 쓰는 가짜 음성 검출(FADEL), 화자 검증과 화자 분할.[^p5][^p6][^iconf]

### 4. 음성 향상과 신경망 오디오 코덱

실시간 스트리밍 신경망 오디오 코덱(HILCodec), 신호 대 잡음비에 맞춘 확산 음성 향상, 스트리밍 음성 향상.[^p7][^p8][^iconf]

## 대표 논문

랩 출판 목록의 2021–2026년 논문 가운데 김남수 교수가 마지막 저자인 학술지·학회 논문을 네 연구 갈래에 두 편씩 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^ijournal][^iconf] |
|---|---|---|---|---|
| 1 | 2025 | [SegINR: Segment-Wise Implicit Neural Representation for Sequence Alignment in Neural Text-to-Speech](https://doi.org/10.1109/lsp.2025.3528858) · IEEE Signal Processing Letters | 정렬을 위한 보조 길이 예측기나 자기회귀 순서 모델링이 필요 없는 신경망 음성 합성(TTS) 방법 SegINR을 제시했다. SegINR은 글 순서열을 프레임 단위 특징으로 바로 바꿔 TTS 과정을 단순하게 한다. 부호화한 글 임베딩을 조건부 암묵적 신경 표현(INR, Implicit Neural Representation; 좌표를 넣으면 그 위치의 값을 내놓는 신경망으로 신호를 나타내는 방법)으로 길이를 맞춘 프레임 단위 특징 구간으로 바꾸며, 각 구간 안의 시간 변화를 담으면서 구간 경계를 스스로 정해 계산 비용을 줄였다. 2단계 TTS 틀에 넣어 의미 토큰 예측에 썼고, 학습에 쓰지 않은 화자의 목소리로 합성하는 제로샷 적응 TTS 실험에서 기존 방법보다 음질이 좋으면서 계산 효율도 갖췄다.[^p1] | 1저자 M. Kim, 마지막 저자 김남수 |
| 2 | 2021 | [Diff-TTS: A Denoising Diffusion Model for Text-to-Speech](https://doi.org/10.21437/interspeech.2021-469) · Interspeech 2021 | 신경망 TTS 모델은 사람 같은 말소리를 만들어 주목받았지만, 자연스러움과 구조의 효율에는 아직 나아질 여지가 있다. 매우 자연스럽고 효율적인 음성 합성을 하는 새 비자기회귀 TTS 모델 Diff-TTS를 제안했다. 글이 주어지면 잡음 제거 확산 틀로 잡음 신호를 확산 시간 단계에 걸쳐 멜 스펙트로그램으로 바꾼다. 글을 조건으로 한 멜 스펙트로그램의 분포를 배우려고 TTS를 위한 가능도 기반 최적화 방법을 제시했고, 추론 속도를 높이려고 가속 표본 추출 방법을 써서 지각 품질(사람이 듣고 느끼는 품질)을 크게 떨어뜨리지 않고 소리 파형을 훨씬 빨리 만들게 했다. 실험에서 NVIDIA 2080Ti GPU 한 장으로 실시간보다 28배 빠르게 생성했다.[^p2] | 1저자 M. Jeong, 마지막 저자 김남수 |
| 3 | 2025 | [Towards Maximum Likelihood Training for Transducer-Based Streaming Speech Recognition](https://doi.org/10.1109/lsp.2024.3491019) · IEEE Signal Processing Letters | 트랜스듀서 신경망은 정확도와 지연 시간 사이의 균형에서 최신 수준(state-of-the-art)의 성능을 내며 스트리밍 자동 음성 인식(ASR)의 주된 방법이 되었다. 기존 틀에서는 스트리밍 트랜스듀서 모델을 비스트리밍 재귀 규칙에 바탕을 둔 가능도 함수를 최대화하도록 학습하는데, 이 때문에 학습과 추론이 어긋나 가능도가 일그러지고 그 결과 음성 인식 정확도가 최적에 못 미친다. 실제 가능도와 일그러진 가능도 사이의 차이를 수학적으로 나타낸 FoCC(forward variable causal compensation)와, 정확한 가능도를 추정하는 그 추정량 FoCCE를 제시했다. LibriSpeech 데이터셋 실험에서 FoCCE로 학습하면 스트리밍 트랜스듀서의 정확도가 높아졌다.[^p3] | 1저자 H. Lee, 마지막 저자 김남수 |
| 4 | 2024 | [HuBERT-EE: Early Exiting HuBERT for Efficient Speech Recognition](https://doi.org/10.21437/interspeech.2024-80) · Interspeech 2024 | HuBERT(Hidden-unit BERT)와 wav2vec 2.0 같은 자기 지도 모델로 사전 학습하면서 자동 음성 인식(ASR)이 크게 나아졌지만, 이런 모델은 뛰어난 성능을 내려면 계산 비용이 커서 추론 속도가 느려진다. 모델 효율을 높이려고 모델이 추론을 상황에 따라 멈출 수 있게 하는 음성 인식용 조기 종료 방식 HuBERT-EE를 제안했다. HuBERT-EE는 중간 층들에 조기 종료 갈래를 여럿 붙이고, 갈래의 중간 예측이 확신할 만하면 추론을 멈추고 그 결과를 일찍 내놓는다. 조기 종료를 잘 하기 위한 알맞은 종료 기준과 미세 조정 전략을 살폈다. LibriSpeech 실험에서 HuBERT-EE는 성능과 지연 시간 사이의 균형을 맞추면서 HuBERT의 추론을 빠르게 했다.[^p4] | 1저자 J. W. Yoon, 마지막 저자 김남수 |
| 5 | 2021 | [Bootstrap Equilibrium and Probabilistic Speaker Representation Learning for Self-Supervised Speaker Verification](https://doi.org/10.1109/access.2021.3137190) · IEEE Access | 앞단의 부트스트랩 평형 화자 표현 학습과 뒷단의 불확실성을 고려한 확률적 화자 임베딩 학습으로 이루어진 자기 지도 화자 표현 학습 전략을 제안했다. 앞단에서는 균일성 정규화 항(표현들이 고르게 퍼지도록 하는 학습 벌점 항)을 더한 부트스트랩 학습 방식으로 화자 표현을 배운다. 뒷단에서는 같은 화자에 속한 음성 표본 사이의 상호 가능도 점수를 최대화해 확률적 화자 임베딩을 추정하며, 이 임베딩은 화자 표현과 함께 자료의 불확실성도 준다. 실험에서 제안한 부트스트랩 평형 학습 전략은 화자 표현을 배우는 데 효과가 있었고 대조 학습(같은 것끼리는 가깝게, 다른 것끼리는 멀게 표현을 배우는 학습)에 바탕을 둔 기존 방법보다 나았으며, 두 단계를 합친 틀은 VoxCeleb1 시험 세트에서 EER(Equal Error Rate; 잘못 받아들이는 비율과 잘못 거부하는 비율이 같아지는 오류율)과 MinDCF(최소 검출 비용, 오류의 비용을 반영한 성능 지표) 기준의 화자 검증 성능을 더 높였다.[^p5] | 1저자 S. H. Mun, 마지막 저자 김남수 |
| 6 | 2025 | [FADEL: Uncertainty-aware Fake Audio Detection with Evidential Deep Learning](https://doi.org/10.1109/icassp49660.2025.10888053) · ICASSP 2025 | 음성 합성과 음성 변환 기술이 발전하면서 자동 화자 검증(ASV) 시스템이 위조 공격에 더 취약해져 가짜 음성 검출이 큰 관심을 받고 있다. 이 일의 핵심 과제는 학습 때 보지 못한 분포 밖(OOD, out-of-distribution) 공격까지 검출하도록 모델을 일반화하는 것이다. 기존 방법은 좋은 결과를 보였지만 분류에 소프트맥스(점수들을 합이 1인 확률로 바꾸는 함수)를 쓰기 때문에 과신 문제가 있어, 예측할 수 없는 위조 시도를 만나면 믿기 어려운 예측을 낼 수 있다. 이를 풀려고 증거 학습을 쓴 가짜 음성 검출 틀 FADEL을 제안했다. 클래스 확률을 디리클레 분포(여러 범주 확률의 조합이 어떻게 퍼져 있는지 나타내는 확률분포)로 모델링해 모델의 불확실성을 예측에 넣고, 그 결과 분포 밖 상황에서 더 강인하게 동작한다. ASVspoof2019 LA(Logical Access)와 ASVspoof2021 LA 데이터셋 실험에서 기준 모델들의 성능을 크게 높였고, 여러 위조 알고리즘에 걸쳐 평균 불확실성과 동일 오류율(EER) 사이의 강한 상관을 분석해 불확실성 추정이 타당함을 보였다.[^p6] | 1저자 J. Y. Kang, 마지막 저자 김남수 |
| 7 | 2024 | [HILCodec: High-Fidelity and Lightweight Neural Audio Codec](https://doi.org/10.1109/jstsp.2024.3469530) · IEEE Journal of Selected Topics in Signal Processing | 종단형 신경망 오디오 코덱이 발전하면서 아주 낮은 비트율(초당 쓰는 비트 수)로 오디오를 압축하고도 높은 충실도(원래 소리를 그대로 되살리는 정도)로 복원할 수 있게 되었지만, 이런 개선은 흔히 모델이 복잡해지는 대가를 치른다. 기존 신경망 오디오 코덱의 문제를 찾아 풀었다. SEANet 기반 코덱은 신경망이 깊어져도 성능이 꾸준히 오르지 않음을 보이고, 그 근본 원인을 분석해 분산을 제약하는 설계를 제안했다. 또 기존 파형 영역 판별기에 여러 왜곡이 있음을 밝히고 왜곡 없는 새 판별기를 제안했다. 이렇게 만든 HILCodec은 실시간 스트리밍 오디오 코덱으로, 여러 비트율과 오디오 종류에서 최신 수준(state-of-the-art)의 품질을 보인다.[^p7] | 1저자 S. Ahn, 마지막 저자 김남수 |
| 8 | 2025 | [SNR-Aligned Consistent Diffusion for Adaptive Speech Enhancement](https://doi.org/10.21437/interspeech.2025-1721) · Interspeech 2025 | 생성 모델은 음성 향상에서 강한 성능을 보였고, 일관성 모델(확산 모델의 생성 경로 위 어느 지점에서든 원래 자료로 바로 가도록 학습한 생성 모델)은 속도와 품질을 함께 더 높였다. 이를 바탕으로 확산 시간 단계를 입력 신호의 신호 대 잡음비(SNR)에 맞춰 바꾸는 SNR 적응 틀을 제안해, 여러 잡음 조건에서 강인성을 높였다. 이 틀에서 역과정(잡음에서 자료 쪽으로 되돌아가는 확산 생성 과정)은 추정한 SNR에 따라 조정한 확산 시간 단계를 조건으로 받고, 더하는 가우스 잡음(정규분포를 따르는 잡음)도 같은 SNR 추정값에 따라 조절한다. 이 설계로 확산 시간 단계가 SNR 조절 매개변수 구실을 하는 연속적인 SNR 조건화가 가능해져, 모델이 입력 SNR에 따라 향상 과정을 조정할 수 있다. 실험에서 제안한 틀은 지각 품질을 꾸준히 높였고, 어려운 SNR 조건에서 개선 폭이 더 컸다.[^p8] | 1저자 Y. Jun, 마지막 저자 김남수 |

## 교수와 전문 분야

김남수 교수는 서울대학교 전자공학과에서 학사(1988년)를, KAIST 전기전자공학과에서 석사(1990년)와 박사(1994년)를 받았다.[^prof][^eceprof] 삼성종합기술원(Samsung Advanced Institute of Technology)에서 연구원으로 일한 뒤(누리집은 1994–1998년, 학부 교수 상세는 1993–1998년 전문연구원으로 적는다) 1998년부터 서울대학교 교수로 있다.[^prof][^eceprof] 학부 교수 상세는 전공을 통신과 신호처리로, 분야를 인공지능과 음성음향신호처리로 적고, Research Interest로 음성인식, 음성부호화 및 음성향상, 음성합성을 든다.[^eceprof] 누리집 교수 소개의 연구 관심은 기계 학습과 인공지능, 음성 부호화와 음성 향상, 음성 인식과 음성 합성, 실감 오디오 기술과 음원 위치 추정, 음원 분리와 음향 장면 인식이다.[^prof] 학술 활동으로는 2013년부터 IEEE(Institute of Electrical and Electronics Engineers) Senior Member이고, 누리집은 이 밖에 The Institute of Electronics, Information and Electronics Engineers(2001년부터), Interspeech(2005년부터), Acoustical Society of Korea(1999년부터), The Korean Institute of Communications and Information Sciences(2008년부터)의 회원 활동을 적는다.[^prof] 랩 Books 페이지에는 교수가 Joon-Hyuk Chang과 함께 쓴 「Chapter 7. Statistical Model based Techniques for Robust Speech Communication」(Recent Advances in Robust Speech Recognition Technology, 2010년 1월)이 실려 있다.[^books]

랩 International Journals 페이지의 목록을 시기별로 보면, 1995–2002년 논문은 은닉 마르코프 모델에 바탕을 둔 음성 인식, 잡음 환경 보상, 화자 적응을 주로 다룬다. 1999–2010년 무렵 논문은 통계 모델에 바탕을 둔 음성 구간 검출(말소리가 있는 구간을 찾아내는 일)과 음성 향상, 반향 억제와 동시 통화(통화하는 양쪽이 한꺼번에 말하는 상황) 검출, 음성 부호화를 다루고, 2009–2015년 무렵에는 HMM 기반 음성 합성, 소리에 데이터를 숨겨 보내는 음향 데이터 전송, NMF 기반 음원 분리와 음성 향상 논문이 이어진다. 2016–2020년 논문은 DNN 기반 음성 향상과 음성 구간 검출, 화자 인식 임베딩, 음향 사건 검출, 종단형 음성 합성으로 옮겨 간다.[^ijournal] 2021–2026년 국제 학술지 목록에는 교수가 공저자로 이름을 올린 다른 분야 논문도 있다. 「An Ultrasonic Sensor IC for Automotive Parking Assist with Module ID Detection」(IEEE Sensors Journal, 2026)과 「A Fully Integrated Single-BJT-Based Temperature-to-Digital Converter Achieving ±0.23 °C (3σ) Over 2.0–5.5 V for Duty-Cycled Operation」(IEEE Transactions on Instrumentation and Measurement, 2026)은 회로 논문이고, 「Chiral symmetry and taste symmetry from the eigenvalue spectrum of staggered Dirac operators」(Physical Review D, 2021)는 물리 논문이다.[^ijournal]

논문으로 보면 지금의 전문 분야는 네 갈래다. 첫째, 글을 말소리로 바꾸는 신경망 음성 합성이다(대표 논문 1, 2).[^p1][^p2] 둘째, 스트리밍 음성 인식과 음성 인식 모델을 빠르게 만드는 방법이다(대표 논문 3, 4).[^p3][^p4] 셋째, 화자 표현 학습과 가짜 음성 검출이다(대표 논문 5, 6).[^p5][^p6] 넷째, 신경망 오디오 코덱과 음성 향상이다(대표 논문 7, 8).[^p7][^p8]

## 응용 분야

연구 소개 페이지는 음성 인식이 스마트홈과 전화 같은 기기의 인터페이스에 쓰이고, 음성 합성이 스마트폰 인터페이스, 차량 안 개인 비서, 자동 응답 시스템(ARS), 로봇 인터페이스처럼 기계가 말소리로 사용자에게 정보를 전하는 여러 분야에 쓰이며, 음성 향상이 이동통신 시스템, 보청기, 음성 인식에 응용된다고 적는다.[^speech] 공간 음향 재현은 3차원 실감 오디오 시스템과 음파 경로 분석에, 환경 장면 분류는 로봇 길 찾기와 법과학에, 음원 위치 추정은 박물관 가상 안내, 개인 물품 추적, 쇼핑몰 안내 같은 위치 기반 서비스에 쓸 수 있고, 사운드 코드는 광고에 제품 정보·유통사 정보·쿠폰 코드를 넣는 데 쓸 수 있다고 적는다.[^audio] Notice 게시판이 옮긴 2024년 7월 연합뉴스TV 보도는 연구진이 화자 인식 기술로 목소리가 비슷한 음성끼리 묶어 같은 범죄자로 추정되는 음성을 데이터베이스로 만들 수 있는 보이스피싱 음성분석 모델을 개발했고, 정부가 이 기술을 범인의 목소리 감정에 도입했으며 음성 관련 수사 전반에 적용할 계획이라고 전한다.[^news] 과제 목록에는 경찰청, 과학기술정보통신부, 정보통신산업진흥원의 과제와 함께 삼성전자, LG전자, LG 유플러스, 삼성에스디에스, 관악아날로그 주식회사 같은 기업의 과제가 있다.[^projects] 졸업생의 진로로는 Samsung Electronics, LG Electronics, SK Telecom, LG AI Research, Hyundai AIRS, Amazon, Qualcomm 같은 기업과, Hanyang University, Inha University, Gwangju Institute of Science and Technology, Chung-Ang University의 교수직이 있다.[^alumni]

## 구성원

2026년 10월 25일 랩 Students 페이지 기준이다. 카드 17장(Ph.D. Students 15명, M.S. Students 2명)이며, 과정은 페이지가 카드를 나눈 두 분류(Ph.D. Students, M.S. Students)를 박사과정과 석사과정으로 옮겼고, 시작은 카드의 Since 줄이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| 김정훈(Jeunghun Kim) | 박사과정 | Spring 2013 |  |
| 유주현(Juhyun Lyu) | 박사과정 | Spring 2019 |  |
| 김석민(Seokmin Kim) | 박사과정 | Autumn 2018 |  |
| 우범준(Beom Jun Woo) | 박사과정 | Spring 2019 | 4, 7, 8 |
| 안성환(SungHwan Ahn) | 박사과정 | Spring 2021 | 7 |
| 김세민(Semin Kim) | 박사과정 | Autumn 2021 | 6 |
| 김성수(Sungsoo Kim) | 박사과정 | Spring 2023 | 3 |
| 문찬영(Chanyeong Moon) | 박사과정 | Spring 2023 | 7 |
| 전용현(Yong Hyeon Jun) | 박사과정 | Spring 2023 | 8 |
| 박재홍(Jaehong Park) | 박사과정 | Spring 2023 |  |
| 강주연(Ju Yeon Kang) | 박사과정 | Spring 2023 | 6 |
| 한진모(Jinmo Han) | 박사과정 | Spring 2024 |  |
| 홍지민(Ji Min Hong) | 박사과정 | Spring 2024 |  |
| 김선욱(Seonuk Kim) | 박사과정 | Autumn 2024 |  |
| 박우성(Wooseong Park) | 석사과정 | Spring 2025 |  |
| 김지환(Jihwan Kim) | 박사과정 | Autumn 2025 |  |
| 이윤형(Yoonhyeong Lee) | 석사과정 | Spring 2026 |  |

## 졸업생과 이전 구성원

랩 Alumni 페이지에 실린 60명(박사 34명, 석사 26명)이다. 학위와 연도는 랩 표기이고, 진로는 랩이 이름 아래 적은 줄을 차례대로 옮겼다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Joon Hyuk Chang | Ph.D. (2004) | Post Doc, University of California, Santa Barbara 2004~2005; Professor of School of Electronic and Electrical Engineering, Inha University 2005~2011; Professor of Department of Electronic Engineering, Hanyang University since 2011 |
| Ki Hyun Choo | M.S. (2000) | Samsung Advanced Institute of Technology 2000~2011; Samsung Electronics since 2011 |
| Dong Kook Kim | Ph.D. (2003) | ETRI 2003~2004; Professor of Dept. of Electronics, Computer and Information Engineering, Chonnam Nat l Univ. since 2004 |
| Young Joon Kim | Ph.D. (2007) | SK Telecom since 2007 |
| Seung Yeol Lee | Ph.D. (2008) | Samsung Electronics since 2008 |
| Eugene Jon | M.S. (2001) | Samsung Advanced Institute of Technology 2001~2005; UCLA. Ph.D. course. 2005~2010; LG Electronics 2010~2012; SK Telecom since 2012 |
| Seung Seop Park | Ph.D. (2007) | Post Doc, Seoul Nat'l Univ. 2007~2009; Samsung Electronics since 2009 |
| Woohyung Lim | Ph.D. (2007) | Samsung Electronics since 2007; SK Telecom since 2013; LG AI Research since 2019 |
| Nam Suk Lee | M.S. (2002) | Samsung Electronics since 2002 |
| Jong Kyu Kim | Ph.D. (2009) | Samsung Electronics since 2009 |
| Hyun Woo Kim | M.S. (2003) | ETRI since 2003 |
| Young Sub Lim | M.S. (2003) | LG Electronics since 2003 |
| Jong Won Shin | Ph.D. (2008) | Senior Engineer in Qualcomm Inc. San Diego 2008~2012; Professor of Gwangju Institute of Science and Technology since 2012 |
| Dong Jin Seo | M.S. (2004) | Samsung Electronics since 2004 |
| Seung Woo Lee | M.S. (2005) | Samsung Electronics since 2005 |
| Bong Kyoung Kim | M.S. (2005) | Samsung Electronics since 2005 |
| Dong Hwi Kang | M.S. (2006) | Daewoo Electronics since 2006 |
| Hwan Sik Yun | Ph.D. (2011) | LG Electronics since 2011 |
| Hee Suk Jung | M.S. (2006) | LG Electronics Institute of Technology since 2006 |
| Jung Su Kim | M.S. (2006) | Samsung Electronics 2006~2009; MBA, Seoul National University 2009~2011; Kookmin Bank 2011; Hyundai Mobis since 2011 |
| Hyun Cheol Jo | M.S. (2007) | DGIST 2007~2011; Texas A&M University, Ph.D. course since 2011 |
| Tae Young Jo | M.S. (2007) | LG Telecom 2007-2009; PULSUS Technology since 2010; Atlas Labs since 2015 |
| Chang Woo Han | Ph.D. (2012) | Samsung Electronics since 2012 |
| June Sig Sung | Ph.D. (2013) | Samsung Electronics since 2013 |
| Kiho Cho | Ph.D. (2014) | Samsung Electronics since 2014 |
| Yu Gwang Jin | Ph.D. (2014) | Gwangju Institute of Science and Technology post doc. 2014~2015; SK telecom since 2015 |
| Yu Liu | M.S. (2009) | Samsung Electronics since 2009 |
| Doo Hwa Hong | Ph.D. (2015) | Samsung Electronics since 2015 |
| Shin Jae Kang | Ph.D. (2015) | Samsung Electronics since 2015 |
| Sung Soo Kim | M.S. (2010) | Samsung Electronics since 2010 |
| Subhojit Chakladar | M.S. (2010) | Samsung Electronics since 2010 |
| Kyung Hwan Oh | M.S. (2011) | Cowon since 2011; Kakao Enterprise |
| Hyun Woo Koo | M.S. (2013) |  |
| Sukanya Sonowal | M.S. (2010) | Samsung Electronics since 2010 |
| Chul Min Lee | Ph.D. (2016) | Samsung Electronics since 2016 |
| Ki Soo Kwon | Ph.D. (2017) | Samsung Electronics since 2017 |
| Tae Gyoon Kang | Ph.D. (2017) | Samsung Electronics since 2017 |
| Jae Choi | Ph.D. (2017) | Samsung Electronics since 2017; Hyundai AIRS since 2021 |
| Se Young Jang | M.S. (2017) |  |
| Kang Hyun Lee | Ph.D. (2019) | Samsung Electronics since 2019 |
| Ji Hwan Kim | M.S. (2019) | VUNO Inc. since 2019; Korea Telecom since 2023 |
| Seok Wan Chae | M.S. (2019) | NC soft since 2019; Samsung Electronics since 2022 |
| Soo Hyun Bae | Ph.D. (2020) | Samsung Electronics since 2020 |
| InKyu Choi | Ph.D. (2020) | Samsung Electronics since 2020 |
| Joun Yeop Lee | Ph.D. (2020) | Samsung Electronics since 2020 |
| Hyeong Rae Ihm | M.S. (2020) | LG AI Research since 2020 |
| Hyeong Ju Kim | M.S. (2021) | Neosapience since 2021; Supertone Inc. since 2022 |
| Woo Hyun Kang | Ph.D. (2021) | Computer Research Institute of Montreal (CRIM) since 2021; Amazon since 2022 |
| Sung Jun Cheon | Ph.D. (2021) | Samsung Electronics since 2021 |
| Hyung Yong Kim | Ph.D. (2021) | Hyundai AIRS since 2021 |
| Won Ik Cho | Ph.D. (2022) | Samsung Electronics since 2022 |
| Ji Hwan Kim | M.S. (2023) | Moreh Inc. since 2023 |
| Hyeon Seung Lee | Ph.D. (2024) | XL8.ai since 2024 |
| Byoung Jin Choi | Ph.D. (2024) | Samsung Electronics since 2024 |
| Sung Hwan Mun | Ph.D. (2024) | Samsung Electronics since 2024 |
| Ji Won Yoon | Ph.D. (2024) | Professor of Chung-Ang University since 2024 |
| Myeonghun Jeong | Ph.D. (2025) | Samsung Electronics since 2025 |
| Dongjune Lee | M.S. (2025) | Korea Aerospace Industries since 2025 |
| Min Hyun Han | Ph.D. (2025) | Samsung Electronics since 2025 |
| Minchan Kim | Ph.D. (2025) | Samsung Electronics since 2025 |

## 최근 논문 목록 (2021–2026)

랩 International Journals 페이지(전체 117편)와 Domestic Journals 페이지(전체 25편)에서 날짜 칸이 2021–2026년인 학술지 논문 27편(국제 26편, 국내 1편) 가운데, 김남수 교수가 저자가 아닌 1편과 정신건강의학 임상 연구 3편을 제외한 23편(국제 22편, 국내 1편)이다. 연도는 랩이 적은 날짜 칸의 연도이고, 저자·제목·학술지 표기는 랩 표기 그대로다. 학회 논문은 아래 두 절에 따로 적었다.[^ijournal][^djournal]

**2026**

- 김예린,박성철,김우영,이현중,전재훈,김남수,이주열. "An Ultrasonic Sensor IC for Automotive Parking Assist with Module ID Detection". *IEEE Sensors Journal, 2026*.
- 김우영,두권빈,이현중,김남수,이주열. "A Fully Integrated Single-BJT-Based Temperature-to-Digital Converter Achieving ±0.23 °C (3σ) Over 2.0–5.5 V for Duty-Cycled Operation". *IEEE Transactions on Instrumentation and Measurement, 2026*.

**2025**

- M. H. Han, S. H. Mun and N. S. Kim. "Generalized Score Comparison-Based Learning Objective for Deep Speaker Embedding". *IEEE Access, vol. 13, pp. 51194-51207, 2025*.
- M. Kim, M. Jeong, B. J. Choi, S. Kim, J. Y. Lee and N. S. Kim. "Utilizing Neural Transducers for Two-Stage Text-to-Speech via Semantic Token Prediction". *IEEE Transactions on Audio, Speech and Language Processing, vol. 33, pp. 1922-1932, 2025*.
- M. Kim, M. Jeong, J. Y. Lee, and N. S. Kim. "SegINR: Segment-Wise Implicit Neural Representation for Sequence Alignment in Neural Text-to-Speech". *IEEE Signal Processing Letters, Vol. 32, pp. 646-650, 2025*.
- S. Kim, D. Lee, J. Y. Kang, M. Jeong, and N. S. Kim. "Sampling-Based Pruned Knowledge Distillation for Training Lightweight RNN-T". *IEEE Signal Processing Letters, Vol. 32, pp. 631-635, 2025*.
- H. Lee, J. W. yoon, S. Kim, and N. S. Kim. "Towards Maximum Likelihood Training for Transducer-Based Streaming Speech Recognition". *IEEE Signal Processing Letters, Vol. 32, pp. 26-30, 2025*.

**2024**

- S. Ahn, B. J. Woo, M. H. Han, C. Moon, and N. S. Kim. "HILCodec: High-Fidelity and Lightweight Neural Audio Codec". *IEEE Journal of Selected Topics in Signal Processing, vol. 18, no. 8, pp. 1517-1530, 2024*.
- J. W. Yoon, H. Lee, J. Y. Kang, and N. S. Kim. "Cons-KD: Dropout-Robust Knowledge Distillation for CTC-Based Automatic Speech Recognition". *IEEE Access, vol. 12, pp. 131136-131146, 2024*.
- M. Jeong, M. Kim, J. Y. Lee, and N. S. Kim. "Efficient Parallel Audio Generation Using Group Masked Language Modeling". *IEEE Signal Processing Letters, vol. 31, pp 979-983, 2024*.
- B. J. Choi, M. Jeong, M. Kim, and N. S. Kim. "Variable-Length Speaker Conditioning in Flow-Based Text-to-Speech". *IEEE Signal Processing Letters, vol. 31, pp 899-903, 2024*.
- M. Jeong, M. Kim, B. J. Choi, J. Yoon, W. Jang, and N. S. Kim. "Transfer Learning for Low-Resource, Multi-Lingual, and Zero-Shot Multi-Speaker Text-to-Speech". *IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 32, pp. 1519-1530, 2024*.

**2023**

- J. W. Yoon, H. Y. Kim, H. Lee, S. Ahn, and N. S. Kim. "Oracle Teacher: Leveraging Target Information for Better Knowledge Distillation of CTC Models". *IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 31, pp. 2974-2987, 2023*.

**2022**

- B. J. Choi, M. Jeong, J. Y. Lee, and N. S. Kim. "SNAC: Speaker-Normalized Affine Coupling Layer in Flow-Based Architecture for Zero-Shot Multi-Speaker Text-to-Speech". *IEEE Signal Processing Letters, vol. 29, pp 2502-2506, 2022*.
- W. I. Cho and N. S. Kim. "Text implicates prosodic ambiguity: A corpus for intention identification of the Korean spoken language". *ACM Transactions on Asian and Low-Resource Language Information Processing, 2022*.
- H. Y. Kim, J. W. Yoon, W. I. Cho, and N. S. Kim. "Neurally Optimized Decoder for Low Bitrate Speech Codec". *IEEE Signal Processing Letters, vol. 29, pp 244-248, 2022*.
- S. J. Cheon, B. J. Choi, M. Kim, H. Lee, and N. S. Kim. "A Controllable Multi-Lingual Multi-Speaker Multi-Style Text-to-Speech Synthesis With Multivariate Information Minimization". *IEEE Signal Processing Letters, vol. 29, pp 55-59, 2022*.

**2021**

- S. H. Mun, M. H. Han, D. Lee, J. Kim and N. S. Kim. "Bootstrap Equilibrium and Probabilistic Speaker Representation Learning for Self-Supervised Speaker Verification". *IEEE Access, vol. 9, pp. 167615-167627, 2021*.
- Hwancheol Jeong, Chulwoo Jung, Seungyeob Jwa, Jangho Kim, Jeehun Kim, Nam Soo Kim, Sunghee Kim, Sunkyu Lee, Weonjong Lee, Youngjo Lee, and Jeonghwan Pak. "Chiral symmetry and taste symmetry from the eigenvalue spectrum of staggered Dirac operators". *Physical Review D, 2021*.
- J. W. Yoon, H. Lee, H. Y. Kim, W. I. Cho, and N. S. Kim. "TutorNet: towards flexible knowledge distillation for end-to-end speech recognition". *IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 29, pp. 1626-1638, 2021*.
- H. Lee, W. H. Kang, S. J. Cheon, H. Kim, and N. S. Kim. "Gated recurrent context: softmax-free attention for online encoder-decoder speech recognition". *IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 29, pp. 710-719, 2021*.
- H.Y. Kim, J.W Yoon, S. J. Cheon, W. H. Kang, and N. S. Kim. "A Multi-Resolution Approach to GAN-Based Speech Enhancement". *Applied Sciences, 11(2), 721, 2021*.
- 임형래, 천성준, 최병진, 김민찬, 김남수. "리포머 네트워크를 이용한 종단형 한국어 음성 합성 시스템". *한국통신학회논문지, 제 46권, 제 2호, 2021*.

## 국제 학회 논문 (2021–2026)

랩 International Conference 페이지(전체 145편)에서 날짜 칸이 2021–2026년인 32편이다. 연도는 날짜 칸의 연도이고, 학회 이름 뒤의 날짜와 저자 표기는 랩 표기다. 저자 이름 뒤의 \*는 누리집 표시이며 누리집은 그 뜻을 적지 않는다. 학회 논문집 서지를 찾을 수 없는 논문은 괄호에 「누리집 표기」로 표시했다.[^iconf]

**2026**

- J. Kim, N.S. Kim. "ZipL-Dialog: Memory-Efficient Long-Form Spoken Dialog Synthesis via Latent Flow Matching". *Proc. Interspeech, Sep.2026 (누리집 표기)*.
- M.H, Han, C. Moon, J.Y. Kang, N.S. Kim. "End-to-End Speaker Verification with Uncertainty-Aware Evidential Scoring". *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2026*.
- S. Ahn, J. Han, B.J. Woo, N.S. Kim. "FastEnhancer: Speed-Optimized Streaming Neural Speech Enhancement". *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2026*.

**2025**

- Y. Jun, B. Woo, M. Jeong, N. Kim. "SNR-Aligned Consistent Diffusion for Adaptive Speech Enhancement". *Proc. Interspeech, Aug. 2025*.
- M. Jeong, M. Kim, S. Kim and N. S. Kim. "Evidential-TTS: High Fidelity Zero-Shot Text-to-Speech Using Evidential Deep Learning". *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2025*.
- J. Y. Kang, J. W. Yoon, S. Kim, M. H. Han and N. S. Kim. "FADEL: Uncertainty-aware Fake Audio Detection with Evidential Deep Learning". *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2025*.

**2024**

- B. J. Woo, J. W. Yoon, M. H. Han, C. Moon, and N. S. Kim. "EEND-EM: End-to-End Neural Speaker Diarization with EM-Network". *Proc. Asia Pacific Signal and Information Processing Association Annual Summit and Conference(APSIPA ASC), Dec. 2024*.
- J. W. Yoon, B. J. Woo, and N. S. Kim. "HuBERT-EE: Early Exiting HuBERT for Efficient Speech Recognition". *Proc. Interspeech, Sep. 2024*.
- S. Kim, M. Jeong, H. Lee, M. Kim, B. J. Choi, and N. S. Kim. "MakeSinger: A Semi-Supervised Training Method for Data-Efficient Singing Voice Synthesis via Classifier-free Diffusion Guidance". *Proc. Interspeech, Sep. 2024*.
- J. Y. lee, M. Jeong, M. Kim, J. Lee, H. Cho, and N. S. Kim. "High Fidelity Text-to-Speech Via Discrete Tokens Using Token Transducer and Group Masked Language Model". *Proc. Interspeech, Sep. 2024*.

**2023**

- M. Kim, M. Jeong, B. J. Choi, D. Lee, and N. S. Kim. "Transduce and Speak: Neural Transducer for Text-to-Speech with Semantic Token Prediction". *IEEE Automatic Speech Recognition and Understanding(ASRU), Dec. 2023*.
- S. H. Mun\*, H. Shim\*, H. Tak\*, X. Wang, X. Liu, M. Sahidullah, M. Jeong, M. H. Han, M. Todisco, K. A. Lee, J. Yamagishi, N. Evans, T. Kinnunen, N. S. Kim, and J. Jung. "Towards single integrated spoofing-aware speaker verification embeddings". *Proc. Interspeech, Aug. 2023*.
- J. W. Yoon, S. M. Kim, and N. S. Kim. "MCR-Data2vec 2.0: Improving Self-supervised Speech Pre-training via Model-level Consistency Regularization". *Proc. Interspeech, Aug. 2023*.
- J. W. Yoon, S. Ahn, H. Lee, M. Kim, S. M. Kim, and N. S. Kim. "EM-Network: Oracle Guided Self-distillation for Sequence Learning". *Proc. ICML, 2023*.
- M. H. Han, S. H. Mun, M. Kim, M. Jeong, S. H. Ahn, and N. S. Kim. "Improving Learning Objectives for Speaker Verification from the Perspective of Score Comparison". *IEEE International Conference Acoustic Speech Signal Processing(ICASSP), June. 2023*.
- J. Lyu, J. Yang, J. Kim, W. Lim, W. Ahn, D. Kang, M. Kim, and N. S. Kim. "Multi-resolution sequence Aggregation and Model-Agnostic framework for time-series forecasting". *IEEE International Conference Acoustic Speech Signal Processing(ICASSP), June. 2023*.

**2022**

- S. H. Mun, J. Jung, M. H. Han, and N. S. Kim. "Frequency and Multi-Scale Selective Kernel Attention for Speaker Verification". *Proc. IEEE SLT, 2022*.
- D. Lee\*, M. Kim\*, S. H. Mun, M. H, Han, and N. S. Kim. "FULLY UNSUPERVISED TRAINING OF FEW-SHOT KEYWORD SPOTTING". *Proc. IEEE SLT, 2022*.
- J. W. Yoon, B. J. Woo, S. Ahn, H. Lee, and N. S. Kim. "Inter-KD: Intermediate Knowledge Distillation for CTC-Based Automatic Speech Recognition". *Proc. IEEE SLT, 2022*.
- B.J. Choi, M. Jeong, M. Kim, S.H. Mun, and N.S. Kim. "Adversarial speaker-consistency learning using untranscribed speech data for zero-shot multi-speaker text-to-speech". *Proc. APSIPA ASC, 2022*.
- S. H. Mun, M. H. Han, M. Kim, D. Lee, and N. S. Kim. "Disentangled Speaker Representation Learning via Mutual Information Minimization". *Proc. APSIPA ASC, 2022*.
- W. I. Cho, J. Kim, and N.S. Kim. "Cross-Modal Knowledge Distillation with Dropout-Based Confidence". *Proc. APSIPA ASC, 2022*.
- M. Kim\*, M. Jeong\*, B. J. Choi, S. Ahn, J. Y. Lee, and N. S. Kim. "Transfer Learning Framework for Low-Resource Text-to-Speech using a Large-Scale Unlabeled Speech Corpus (\*BEST STUDENT PAPER)". *Proc. Interspeech, Sep. 2022*.
- S. Moon, W. I. Cho, H. J. Han,, N. Okazaki, and N. S. Kim. "OpenKorPOS: Democratizing Korean tokenization with voting-based open corpus annotation". *Proc. LREC, 2022*.
- W. I. Cho, S. Moon, J. I. Kim, S. M. Kim, and N. S. Kim. "StyleKQC: A style-variant paraphrase corpus for Korean questions and commands". *Proc. LREC, 2022*.

**2021**

- B. J. Woo, H. Y. Kim, J. Kim, and N. S. Kim. "Speech Separation Based on DPTNet with Sparse Attention". *IC-NIDC, Nov. 2021*.
- M. Jeong, H. Kim, S.J. Cheon, B.J. Choi, and N. S. Kim. "Diff-TTS: A Denoising Diffusion Model for Text-to-Speech". *Proc. Interspeech, Aug. 2021*.
- M. Kim, S.J. Cheon, B.J. Choi, J.J. Kim, and N. S. Kim. "Expressive Text-to-Speech using Style Tag". *Proc. Interspeech, Aug. 2021*.
- W. H. Kang, N. S. Kim. "Team02 Text-independent speaker verification system for SdSV Challenge 2021". *Proc. Interspeech, Aug. 2021*.
- W. I. Cho, S. M. Kim, H. Cho, and N. S. Kim. "kosp2e: Korean speech to English translation corpus". *Proc. Interspeech, Aug. 2021*.
- W. I. Cho, S. J. Cheon, W. H. Kang, J. W. Kim, and N. S. Kim. "Giving space to your message: Assistive word segmentation for the electronic typing of digital minorities". *Proc. ACM DIS, pp. 1739-1747, Jun. 2021*.
- W. I. Cho\*, J. W. Kim\*, J. Yang, and N. S. Kim. "Towards cross-lingual generalization of translation gender bias". *Proc. ACM FAccT, pp. 449-457, Mar. 2021*.

## 국내 학회 논문 (2021–2026)

랩 Domestic Conference 페이지(전체 193편)에서 날짜 칸이 2021–2026년인 49편이다. 저자·제목·학회 표기는 랩 표기 그대로다.[^dconf]

**2026**

- 김선욱, 박재홍, 강주연, 전용현, 홍지민, 김남수. "NEAT: 대형 오디오 언어 모델에서의 오디오-텍스트 정렬을 위한 Norm Equalization". *대한전자공학회 하계종합학술대회, 2026*.
- 박우성, 문찬영, 김세민, 한진모, 이윤형, 김남수. "CGAM: CTC Knowledge Distillation 기반 Cross-Attention Masking을 통한 Whisper Hallucination 저감". *대한전자공학회 하계종합학술대회, 2026*.
- 박우성, 김남수. "Virtual CSA-Net : 가상 깊이 생성 및 교차 융합 기반의 콘크리트 균열 검출". *한국통신학회 동계종합학술대회, 2026*.
- 문찬영, 우범준, 김남수. "Transformer 기반 화자 분할을 위한 도착 순서 기반 Sort Loss의 특성 분석". *한국통신학회 동계종합학술대회, 2026*.
- 김세민 , 김선욱 , 강 주 연 김남수. "실환경 음성 데이터를 통한 디퓨전 음성 합성 모델 파인튜닝 에 관한 연구". *한국통신학회 동계종합학술대회, 2026*.
- 박재홍, 전용현, 김남수. "비스트리밍 음성 합성 모델의 세그먼트 기반 실시간 추론 기법". *한국통신학회 동계종합학술대회, 2026*.
- 안성환, 김세민, 김남수. "경량 실시간 음성인식 신경망의 양자화 영향 분석". *한국통신학회 동계종합학술대회, 2026*.
- 한진모, 강주연, 김남수. "Retrieval을 활용한 Finetuning-free LLM-generated text detection". *한국통신학회 동계종합학술대회, 2026*.
- 홍지민, 김석민, 김남수. "소형 오디오 LLM을 위한 Self-Consistency 기반 추론 성능 향상 기법에 관한 연구". *한국통신학회 동계종합학술대회, 2026*.

**2025**

- 김선욱, 홍지민, 강주연, 김남수. "발음 변이 기반 키워드 증강을 통한 한국어 키워드 스포팅 외래어 검출 성능 향상". *한국통신학회 하계종합학술대회, 2025*.
- 박재홍, 안성환, 김남수. "구간별 선형 근사를 통한 On-device용 화자 인식 모델 최적화". *한국통신학회 동계종합학술발표회, 2025*.
- 문찬영, 한민현, 김남수. "한국어 종단형 화자 분리 기법을 위한 한국어 데이터셋 구축". *한국통신학회 동계종합학술발표회, 2025*.
- 전용현, 우범준, 김정훈, 김남수. "잡음 레벨 정렬을 활용한 디퓨전 음성 향상". *한국통신학회 동계종합학술발표회, 2025*.
- 강주연, 김세민, 이동준, 김남수. "음성 인식 모델 경량화를 위한 Teacher Decoder 재사용 기반 지식 증류 기법". *한국통신학회 동계종합학술발표회, 2025*.
- 홍지민, 김선욱, 김민찬, 김남수. "프롬프트 동적 선택을 통한 언어 모델 성능 향상에 대한 연구: UPRISE를 기반으로". *한국통신학회 동계종합학술발표회, 2025*.
- 한진모, 김석민, 정명훈, 김남수. "RNN-T 기반 음성 인식에서 최적화 속도 향상을 위한 가중치 선택 기법". *한국통신학회 동계종합학술발표회, 2025*.

**2024**

- 우범준, 김정훈, 안성환, 전용현, 김남수. "직교 손실 함수를 통한 음성 분리 모델 성능 향상". *한국통신학회 하계종합학술발표회, pp 1970-1971, 2024*.
- 김석민, 한민현, 박재홍, 문찬영, 김남수. "Llama2 기반 수학적 추론 성능 비교". *한국통신학회 하계종합학술발표회, pp 1740-1741, 2024*.
- 김세민, 김민찬, 정명훈, 김남수. "한국어 음성 합성을 위한 Semantic Token 최적화에 관한 연구". *한국통신학회 하계종합학술발표회, pp 1726-1727, 2024*.
- 이동준, 강주연, 한진모, 홍지민, 김남수. "레벤슈타인 트랜스포머 기반 빠른 추론이 가능한 음성 인식 모델에 관한 연구". *한국통신학회 하계종합학술발표회, pp 825-826, 2024*.
- 정명훈, 김세민, 김남수. "Token merge layer를 활용한 효율적인 오디오 생성에 관한 연구". *한국통신학회 동계종합학술발표회, pp 574-575, 2024*.
- 김민찬, 최병진, 김남수. "전이 확률 통제를 활용한 Neural Transducer 기반 음성 합성 시스템의 발화 속도 제어". *한국통신학회 동계종합학술발표회, pp 576-577, 2024*.
- 강주연, 이현승, 윤지원, 김남수. "Self-Attention Map Knowledge Distillation을 이용한 음성 인식 모델 경량화에 대한 연구". *한국통신학회 동계종합학술발표회, pp 579-580., 2024*.
- 박재홍, 문성환, 김남수. "한글의 음절 단위 구분성을 이용한 한국어 음성 합성". *한국통신학회 동계종합학술발표회, pp 1454-1455., 2024*.
- 문찬영, 한민현, 김남수. "화자 검증 시스템을 활용한 종단형 화자 분할 기법". *한국통신학회 동계종합학술발표회, pp 1466-1467., 2024*.
- 전용현, 김석민, 김정훈, 김남수. "딥러닝을 활용한 종단형 자동 이득 제어 알고리즘". *한국통신학회 동계종합학술발표회, pp 1456-1457., 2024*.
- 안성환, 우범준, 이동준, 김남수. "임베디드 시스템을 위한 심층신경망 기반 스트리밍 음성 인식 모델". *한국통신학회 동계종합학술발표회, pp 1450-1451., 2024*.

**2023**

- 우범준, 김석민, 안성환, 강주연, 김남수. "음성 분리의 화자 종속 순열 불변 훈련". *한국통신학회 하계종합학술발표회, pp 1596-1597., 2023*.
- 이동준, 최병진, 한민현, 김남수. "Neural Codec Representation 기반 음성 인식". *한국통신학회 하계종합학술발표회, pp 1598-1599., 2023*.
- 김세민, 이현승, 정명훈, 박재홍, 김남수. "Diffusion 생성 모델을 통한 한국어 가창 음성 합성에 관한 연구". *한국통신학회 하계종합학술발표회, pp 1592-1593., 2023*.
- 안성환, 김정훈, 김민찬, 김세민, 문성환, 이동준, 정명훈, 김남수. "딥러닝 기반 종단형 음성 코덱의 학습 안정화". *한국통신학회 동계종합학술발표회, pp 587-588., 2023*.
- 우범준, 김석민, 김지환, 문성환, 윤지원, 이현승, 최병진, 한민현, 김남수. "화자의 특징 정보를 활용한 대상 음성 분리 알고리즘". *한국통신학회 동계종합학술발표회, pp 617-618., 2023*.
- 김석민, 김민찬, 문성환, 문찬영, 김남수. "Wav2vec 2.0 기반 한국어 감정인식 알고리즘". *한국통신학회 하계종합학술발표회, pp 1602-1603., 2023*.

**2022**

- 윤지원, 김석민, 김남수. "음성 감정인식 모델 내 정규화 파라미터의 표현력 및 영향 연구". *한국전자파학회 하계종합학술대회, 2022*.
- 이동준, 김민찬, 김지환, 문성환, 정명훈, 김남수. "Implicit Neural Representations 기반 배터리 수명 예측". *한국통신학회 하계종합학술발표회, pp 926-927, 2022*.
- 김석민, 조원익, 최병진, 우범준, 안성환, 김남수. "딥러닝 기반 한국어 감정인식 알고리즘". *한국통신학회 하계종합학술발표회, pp 1825-1826, 2022*.
- 김세민, 윤지원, 김정훈, 이현승, 한민현, 김남수. "적대적 훈련을 통해 학습한 VAE 기반의 음성향상 기술에 관한 연구". *한국통신학회 하계학술대회, 2022*.
- 김지환, 조원익, 이동준, 김남수. "정도 부사를 이용한 텍스트 분류 작업에서의 데이터 증강에 관한 연구". *한국통신학회 동계종합학술발표회, pp 1569-1570, 2022*.
- 한민현, 문성환, 김석민, 김남수. "화자 검증을 위한 교차 주의 기반 검증 점수 계산 시스템". *한국통신학회 동계학술대회, 2022*.
- 이현승, 윤지원, 김민찬, 김세민, 김남수. "한국어종단형 음성인식 모델의 weight 평균 기법에 대한 ablation study". *한국통신학회 동계종합학술발표회, pp 1656-1657, 2022*.
- 최병진, 정명훈, 조원익, 김남수. "종단형 한국어 다화자 스타일 음성 합성". *한국통신학회 동계종합학술발표회, pp 1660-1661, 2022*.

**2021**

- 손병찬, 조원익, 천성준, 최병진, 한민현, 김남수. "일반화된 에너지 거리를 이용한 음성 향상". *대한전자공학회 하계학술대회,pp 888-889., 2021*.
- 김석민, 안성환, 윤지원, 이현승, 정명훈, 김남수. "트랜스포머를 이용한 종단형 한국어-영어 음성 번역". *대한전자공학회 하계학술대회, pp 1084-1085., 2021*.
- 이동준, 김민찬, 김정훈, 김지환, 김형용, 문성환, 김남수. "음성 합성 모델을 이용한 키워드 스포팅 모델". *대한전자공학회 하계학술대회, pp 1082-1083., 2021*.
- 윤지원, 이현승, 김민찬, 정명훈, 이동준, 김남수. "종단간 한국어 음성 인식을 위한 언어 모델 활용". *한국전자파학회 동계종합학술대회, p. 328., 2021*.
- 최병진, 천성준, 조원익, 김석민, 손병찬, 김남수. "윈도우 마스킹을 이용한 종단형 감정 음성합성시스템의 강인한 주의집중 정렬 기법". *한국통신학회 동계종합학술발표회, pp 604-605., 2021*.
- 정명훈, 이현승, 김형주, 이동준, 김남수. "디퓨전 생성모델을 활용한 보코더의 샘플링 가속화에 관한 연구". *한국통신학회 동계종합학술발표회, pp 1,218-1,219, 2021*.
- 우범준, 김형용, 윤지원, 김정훈, 김남수. "음향 혼합 데이터 증강 기법을 이용한 SincNet 기반의 음향 사건 감지". *한국통신학회 동계종합학술발표회, pp 616 - 617, 2021*.
- 김민찬, 강우현, 문성환, 한민현, 김남수. "Monotonic Alignment Search를 활용한 비자귀 회귀 음성 합성 기법". *한국통신학회 동계종합학술발표회, pp 1,216-1,217, 2021*.

## 특허

랩 Patents 페이지 전체 94건 가운데 출원일이나 등록일이 2021-10-22–2026-10-22에 드는 29건이다. 제목, 발명자, 나라별 출원·등록 번호와 날짜는 랩 표기 그대로이며, 한 특허의 나라별 출원·등록 기록은 빗금(/)으로 나눴다.[^patents]

- 인공지능 모델 생성 방법, 생성된 인공지능 모델을 이용한 딥페이크 이미지 검출 방법 및 이를 수행하는 전자 장치 (발명자 김남수, 강주연, 박재홍; 출원·등록 대한민국특허, 10-2026-0023509, 출원일자 2026년 2월 5일)
- 불확실성 모델링을 활용한 음성합성 시스템 및 방법 (발명자 김남수, 정명훈; 출원·등록 대한민국특허, 출원번호 10-2024-0165747, 출원일자 2024년 11월 20일 / PCT, 출원번호 PCT/KR2025/016440, 출원일자 2025년 10월 17일)
- 음성 인식 방법 및 장치 (발명자 김남수, 강주연; 출원·등록 대한민국특허, 출원번호 10-2023-0152826, 출원일자 2023년 11월 7일 / 미국특허, 출원번호 19324498, 출원일자 2025년 9월 10일)
- 마이크 어레이의 이상 채널 검출 및 보상 신호 생성 방법 및 장치 (발명자 김남수, 윤지원; 출원·등록 대한민국특허, 출원번호 10-2021-0132102, 출원일자 2021년 10월 06일 / 미국특허, 출원번호 17689299, 츨원일자 2022년 03월 08일, 등록번호 12342149, 등록일자 2025년 6월 24일)
- 음성 합성 구조 기반의 음성 향상 시스템, 방법 및 컴퓨터 판독 가능 매체 (발명자 김남수, 김세민; 출원·등록 대한민국특허, 출원번호 10-2022-0175343, 출원일자 2022년 12월 14일, 등록번호 10-2749818, 등록일자 2024년 12월 30일)
- 화자 상태 변화 감지 기반 구간 단위 화자 분할 시스템 및 방법 (발명자 김남수, 문찬영; 출원·등록 대한민국특허, 출원번호 10-2024-0191916, 출원일자 2024년 12월 19일)
- 사용자 쿼리에 대한 프롬프트를 튜닝하는 방법 및 그 시스템 (발명자 김남수, 강호영, 황봉규, 최준화, 조수아, 조성호, 이동준, 김석민; 출원·등록 대한민국특허, 출원번호 10-2024-0128706, 출원일자 2024년 09월 24일)
- 무한 임펄스 응답 레이어 기반의 심층신경망 시스템 및 방법 (발명자 김남수, 안성환; 출원·등록 대한민국특허, 출원번호 10-2023-0172818, 출원일자 2023년 12월 01일 / PCT, 출원번호 PCT/KR2024/013363, 출원일자 2024년 09월 04일)
- 비지도 학습 기반 사용자 지정 키워드 스포팅 시스템 (발명자 김남수, 이동준, 김민찬; 출원·등록 대한민국특허, 출원번호 10-2022-0174255, 출원일자 2022년 12월 14일, 등록번호 10-2697580, 등록일자 2024년 08월 19일)
- 발화를 분석하기 위한 장치, 방법 및 이를 이용한 애플리케이션 (발명자 김한준, 이솔희, 김남수, 이동준; 출원·등록 대한민국특허, 출원번호 10-2024-0101847, 출원일자 2024년 07월 31일)
- 시퀀스 처리를 위한 심층신경망 시스템 및 학습 방법 (발명자 김남수, 안성환; 출원·등록 대한민국특허, 출원번호 10-2024-0090798, 출원일자 2024년 07월 09일)
- 화자 유사도 판단 방법 및 장치 (발명자 한민현, 김남수; 출원·등록 대한민국특허, 출원번호 10-2021-0194701, 출원일 2021년 12월 31일, 등록번호 10-2655367, 등록일자 2024년 04월 02 / PCT, 출원번호 PCT/KR2021/020384, 출원일자 2021년 12월 31일)
- 준지도 학습 기반의 가창 음성 합성 방법 및 장치 (발명자 김남수, 김세민; 출원·등록 대한민국특허, 출원번호 10-2023-0186110, 출원일자 2023년 12월 19일)
- 종합 화자 처리 토큰 기반 화자 분할 시스템 및 방법 (발명자 김남수, 문찬영; 출원·등록 대한민국특허, 출원번호 10-2023-0180208, 출원일자 2023년 12월 13일)
- 종단형 음성 합성 모델을 활용한 음정 및 음성 변조 시스템 (발명자 김남수, 김민찬; 출원·등록 대한민국특허, 출원번호 10-2021-0193990, 출원일자 2021년 12월 31일, 등록번호 10-2576709, 등록일자 2023년 09월 05일)
- 생성 모델 기반의 음성 코덱 복원 방법 및 장치, 컴퓨터 판독 가능한 기록 매체 및 컴퓨터 프로그램 (발명자 나선필, 김남수, 김형용, 김석민, 한민현, 손병찬; 출원·등록 대한민국특허, 출원번호 10-2020-0090965, 출원일자 2020년 07월 22일, 등록번호 10-2572141, 등록일자 2023년 08월 24일)
- 생성 속도를 조절할 수 있는 음성 합성 시스템 (발명자 김남수, 정명훈; 출원·등록 대한민국특허, 출원번호 10-2021-0115745, 출원일자 2021년 08월 31일, 등록번호 10-2518471, 등록일자 2023년 03월 31일)
- METHOD AND APPARATUS WITH NEURAL NETWORK TRAINING (발명자 Nam Soo KIM, Jiwon YOON; 출원·등록 미국특허, 출원번호 18108727, 출원일자 2023년 02월 13일)
- 화자 인식을 위한 뉴럴 네트워크 장치, 및 그 동작 방법 (발명자 박상하, 김남수, 김형용, 강성찬, 김재흥, 윤용섭, 이충호, 홍혁기; 출원·등록 대한민국특허, 출원번호 10-2017-0157507, 출원일자 2017년 11월 23일, 등록번호 10-2486395, 등록일자 2023년 01월 04일 / 미국특허, 출원번호 16134529, 출원일자 2018년 09월 18일, 등록번호 11094329, 등록일자 2021년 08월 17일)
- 자연어로 기술되는 스타일 태그를 활용하여 운율 조절이 가능한 멀티 스타일 음성 합성 시스템 (발명자 김남수, 김민찬; 출원·등록 대한민국특허, 출원번호 10-2021-0115826, 출원일자 2021년 08월 31일, 등록번호 10-2486106, 등록일자 2023년 01월 04일 / PCT, 출원번호 PCT/KR2021/015743, 출원일 2021년 11월 03일)
- 발화 스타일 인코딩 네트워크 이용한 스타일 음성 합성 장치 및 음성 합성 방법 (발명자 김남수, 천성준, 최병진, 김민찬, 김형주, 손병찬; 출원·등록 대한민국특허, 출원번호 10-2020-0158107, 출원일 2020년 11월 23일, 등록번호 10-2473685, 등록일 2022년 11월 29일)
- 비터비 빔 서치를 이용한 레지듀얼 벡터 양자화 장치, 방법 및 컴퓨터 판독 가능 매체 (발명자 김남수, 안성환; 출원·등록 대한민국특허, 출원번호 10-2022-0111938, 출원일자 2022년 09월 05일)
- 인공 신경망 모델의 동작 방법 및 장치 (발명자 김남수, 윤지원; 출원·등록 대한민국특허, 출원번호 10-2022-0105734, 출원일자 2022년 08월 23일)
- 화자 인식을 위한 음성인식기 기반 풀링 기법의 화자 임베딩 추출 방법 및 시스템, 그리고 이를 위한 기록매체 (발명자 김남수, 문성환; 출원·등록 대한민국특허, 출원번호 10-2020-0130575, 출원일 2020년 10월 08일, 등록번호 10-242956, 등록일자 2022년 08월 02일 / PCT, 출원번호 PCT/KR2021/013641, 출원일자 2021년 10월 05일)
- 인간 친화적인 목표 지향 대화 시스템 및 방법 (발명자 조원익, 김남수, 김종인; 출원·등록 대한민국특허, 출원번호 10-2020-0107917, 출원일자 2020년 08월 26일, 등록번호 10-2414107, 등록일자 2022년 06월 23일)
- 상호 정보량 추정을 이용한 화자 임베딩 추출 장치 및 방법, 컴퓨터 판독 가능한 기록 매체 및 컴퓨터 프로그램 (발명자 나선필, 김남수, 한민현, 김형용, 김석민, 손병찬; 출원·등록 대한민국특허, 출원번호 10-2020-0091037, 출원일자 2020년 07월 22일, 등록번호 10-2405163, 등록일자 2022년 05월 30일)
- 텍스트 기반 사전 학습 모델을 활용한 종단형 음성언어이해 지식 증류를 위한 방법, 시스템, 및 컴퓨터 판독가능한 기록 매체 (발명자 김남수, 조원익, 곽동현; 출원·등록 대한민국특허, 출원번호 10-2020-0106719, 출원일자 2020년 08월 25일, 등록번호 10-2368064, 등록일자 2022년 02월 22일)
- 통계적 불확실성 모델링을 활용한 음성 인식 방법 및 장치 (발명자 김남수, 이현승, 김민찬; 출원·등록 대한민국특허, 출원번호 10-2020-0052981, 출원일자 2020년 04월 30일, 등록번호 10-2363636, 등록일자 2022년 02월 11일)
- 딥러닝 기반 음성 통신 전처리 시스템 (발명자 김남수, 김정훈, 안성환, 김지환, 우범준; 출원·등록 대한민국특허, 출원번호 10-2021-0174265, 출원일자 2021년 12월 07일)

## 과제

랩 Project 페이지(전체 120건, Current Projects 6건과 Previous Projects 114건)에서 기간이 2021년 10월 이후까지 이어진 과제 41건 가운데, 건강·의료와 이어진 과제 3건을 제외한 38건이다. 과제 이름, 참여자, 지원 기관, 기간, 구분은 랩 표기 그대로이며, 랩이 참여자를 적지 않은 과제는 참여자 칸이 없다.[^projects]

- 보이스피싱 탐지 기법 품질 평가 체계 수립 (지원 LG 유플러스; 기간 2026. 04. 24 ~ 2026. 07.24; 참여자 김남수, 홍지민, 문찬영, 박재홍, 이윤형; 구분 Current Projects)
- 한국형 전이중(Full-Duplex) Audio-Language 모델 개발 (지원 정보통신산업진흥원 첨단 GPU 활용 지원 사업; 기간 2026. 04.01 ~ 2026. 07.15; 참여자 김남수, 한진모, 김선욱, 김석민, 우범준, 안성환, 문찬영, 전용현, 박재홍, 강주연; 구분 Current Projects)
- AI-Generated Text Detection 기법 연구 (지원 LG전자 기술협력; 기간 2026.02.01~2027.01.31; 참여자 김남수, 강주연, 홍지민, 한진모; 구분 Current Projects)
- LLM과 Diffusion 모델의 경량화 (지원 삼성전자 DS; 기간 2025. 10. 01~2030. 09. 30; 참여자 김남수, 김석민, 한진모, 홍지민; 구분 Current Projects)
- KWS Fine-Tuning (지원 관악아날로그 주식회사; 기간 2025.08.01 ~ 2026.01.31; 참여자 김남수, 안성환, 김선욱; 구분 Previous Projects)
- 음성합성 데이터 가공 자동화 기술 개발 (지원 삼성전자; 기간 2025.07.15 ~ 2025.12.31; 참여자 김남수, 김세민, 김선욱, 문찬영; 구분 Previous Projects)
- 책임감 있는 AI를 위한 생성형 콘텐츠 검출 및 검증 연구 (지원 과학기술정보통신부; 기간 2025.03.01 ~ 2028.02.29; 참여자 김남수, 홍지민, 한진모, 강주연, 박재홍, 전용현, 문찬영; 구분 Current Projects)
- AI 보드를 위한 AI 알고리즘 경량화 작업 (지원 관악아날로그 주식회사; 기간 2025.01.01 ~ 2025.12.31; 참여자 김남수, 안성환, 김선욱; 구분 Previous Projects)
- 배터리 이상 증후 예측 프로그램 개발 (지원 관악아날로그 주식회사 산업자문; 기간 2024.07.15~2024.10.15; 구분 Previous Projects)
- Low latency streaming TTS 연구 (지원 삼성전자 민간지원사업; 기간 2024.05.01~2024.12.27; 구분 Previous Projects)
- 온디바이스 (On-Device) AI 반도체 응용 소프트웨어 기술에 대한 자문 (지원 관악아날로그 주식회사 산업자문; 기간 2024.03.01~2026.02.28; 구분 Previous Projects)
- 대화형 음성안내 기술 (지원 (주)디지탈센스 단기산업자문; 기간 2024.01.29~2024.02.28; 구분 Previous Projects)
- 성문분석 프로그램 고도화 기술 개발 (지원 경찰청 치안과학기술 연구개발사업; 기간 2024.01.01~2025.03.31; 참여자 김남수, 우범준, 한민현, 김석민, 정명훈, 이동준, 문찬영, 박재홍, 강주연, 전용현, 홍지민, 한진모; 구분 Previous Projects)
- 효율적인 음성 합성을 위한 Adaptive TTS 기술 개발 (지원 현대엔지비 민간지원사업; 기간 2023.04.14 ~ 2023.12.31; 구분 Previous Projects)
- 성문분석 프로그램 고도화 기술 개발 (지원 경찰청 치안과학기술 연구개발사업; 기간 2023.04.01 ~ 2023.12.31; 참여자 김남수, 이현승, 문성환, 우범준, 한민현, 윤지원, 김석민, 이동준, 문찬영, 박재홍, 강주연; 구분 Previous Projects)
- In-context learning을 활용한 zero-shot TTS 기술개발 (지원 삼성전자 민간지원사업; 기간 2023.06.16 ~ 2023.12.29; 구분 Previous Projects)
- Prompt Network을 통한 prompt-tuning 기술 연구 (지원 삼성에스디에스 민간지원사업; 기간 2023.11~2024.10; 참여자 김남수, 김석민, 이동준, 박재홍; 구분 Previous Projects)
- 잡음을 제거해주는 딥러닝 기반 음성 향상 프로그램 (지원 주식회사 워프 기술이전; 기간 2023.09.01~2028.08.31; 구분 Current Projects)
- Streaming Speech-to-Text 모델 (지원 삼성에스디에스 민간지원사업; 기간 2022.08.05 ~ 2023.05.31; 구분 Previous Projects)
- 보이스피싱 음성 데이터 분석 (지원 라임솔루션 민간지원사업; 기간 2022.09.01 ~ 2023.02.28; 구분 Previous Projects)
- 화행 분류 모델 개발 (지원 삼성전자 민간지원사업; 기간 2022.10.19 ~ 2022.12.19; 구분 Previous Projects)
- Double-talk 특화된 Acoustic Echo Cancellation (지원 삼성에스디에스 민간지원사업; 기간 2022.01 ~ 2022.12; 참여자 김남수, 우범준, 김지환, 안성환; 구분 Previous Projects)
- 블루투스 이어폰에서의 오디오 처리에 대한 자문 (지원 엘지전자 산업자문; 기간 2022.07.01 ~ 2022.08.31; 구분 Previous Projects)
- 개인화 음성 합성을 위한 신규 화자 신경망 음향 모델링 기술 (지원 Samsung Research; 기간 2021.08.10 ~ 2022.08.12; 참여자 김남수, 최병진, 문성환, 김민찬, 정명훈, 안성환; 구분 Previous Projects)
- 금융서비스용 음성합성 시스템 (지원 삼성증권 기술이전; 기간 2022.05.11~2025.04.30; 구분 Previous Projects)
- 실시간 유해언어 필터링을 위한 음성인식기 개발 (지원 Samsung Research C-Lab; 기간 2021.12.15 ~ 2022.04.15; 참여자 김남수, 이현승, 윤지원, 김민찬, 김세민; 구분 Previous Projects)
- 엣지용 연산기능강화 DRAM PIM 반도체 기술 개발 (지원 과학기술정보통신부 정보통신기획평가원 PIM인공지능반도체핵심기술개발사업; 기간 2022.04~2025.12; 참여자 김남수, 문성환, 한민현, 윤지원, 김석민, 김민찬, 이동준, 안성환, 김세민; 구분 Previous Projects)
- Duration-invariant speaker verification (지원 네이버 민간지원사업; 기간 2022.01.01 ~ 2022.03.31; 구분 Previous Projects)
- 페르소나 기반 Self-Aware한 공감형 대화 에이전트를 위한 파일럿 데이터 구축 및 연구 (지원 스마일게이트; 기간 2021.11 ~ 2022.01; 참여자 김남수, 조원익, 김석민, 김지환; 구분 Previous Projects)
- AI 이용 배터리의 수명 및 고장 예측 시스템의 모델링 및 구현 (지원 관악아날로그 민간지원사업; 기간 2021.07.01 ~ 2021.12.31; 구분 Previous Projects)
- 성문분석을 통한 실시간 화자검색 기술 개발 (지원 경찰청 치안과학기술 연구개발사업; 기간 2021.01.01 - 2021.12.31; 참여자 김남수, 김정훈, 김형용, 강우현, 조원익, 이현승, 문성환, 한민현, 김석민, 김민찬, 김형주, 우범준, 손병찬, 정명훈, 이동준; 구분 Previous Projects)
- 소량 데이터만을 이용한 고품질 종단형(End-to-End) 기반의 딥러닝 다화자 운율 및 감정 복제 기술 개발 (지원 과학기술정보통신부 정보통신기획평가원 차세대인공지능핵심원천 사업; 기간 2020.04.01 ~ 2021.12.31; 참여자 김남수, 김정훈, 천성준, 조원익, 이현승, 최병진, 윤지원, 김석민, 김민찬, 손병찬; 구분 Previous Projects)
- 딥 러닝 기반 한국어 화자 인식 시스템의 학습 및 베이스라인 구축 방법 (지원 관악아날로그 기술 제휴; 기간 2021.12.14~2024.12.31; 구분 Previous Projects)
- 인공지능기반 실시간 음성 합성 시스템(TTS) 엔진 개발 연구 (지원 삼성증권; 기간 2020.11 ~ 2021.11; 참여자 김남수 천성준 최병진 김민찬 손병찬 정명훈 이동준; 구분 Previous Projects)
- C언어로 구현된 딥 러닝 기반 음성 합성 시스템 (지원 관악아날로그 기술 제휴; 기간 2021.06.11~2024.12.31; 구분 Previous Projects)
- 원격 다자간 영상회의에서의 음성 품질 고도화 기술개발 (지원 과학기술정보통신부 정보통신기획평가원 SW컴퓨팅산업원천사업; 기간 2021.04~2025.12; 참여자 김남수, 김정훈, 김형용, 이현승, 우범준, 안성환, 김지환; 구분 Previous Projects)
- On-device 향 음성인식을 위한 기술 개발 (지원 삼성전자 종합기술원; 기간 2020.9.16 ~ 2025.9.15; 참여자 김남수, 이현승, 윤지원, 김민찬, 정명훈, 이동준; 구분 Previous Projects)
- 인공지능 반도체 융합전문 인력육성 센터 (지원 과학기술정보통신부 정보통신기획평가원 원천기술개발사업; 기간 2020.04~2025.12; 참여자 김남수, 이동준, 김세민; 구분 Previous Projects)

## 소식

랩 Notice 게시판의 연구 소식 1건이다. 2024년 7월 연합뉴스TV 보도를 옮긴 글로, 서울대학교 연구진이 보이스피싱 음성분석 모델을 개발했고 정부가 이 기술을 수사에 활용할 방침이라고 전한다.[^news]

- 2024-07-12 · 어디서 들어본 목소린데...보이스피싱범 잡는 AI / 연합뉴스TV

## 연락과 위치

- 연구실: 서울대학교 132동 302호와 302동 511-2호(누리집 표기 Room 302 INMC(bldg. 132), Room 511-2(bldg.302), 1 Gwanak-ro, Gwanak-gu, Seoul, Korea (08826))[^info]
- 연구실 전화: 02-880-8439(132동 302호), 02-884-1824(302동 511-2호)[^info]
- 교수 연구실과 전화: 132동 410호, 02-880-8419[^eceprof]
[^home]: 연구실 누리집 첫 화면 <https://hi.snu.ac.kr/> (Welcome·About Us 칸, 최근 논문 칸, 2026-10-25 열람)
[^overview]: 누리집 Overview 페이지 <https://hi.snu.ac.kr/research-overview/> (Speech Signal Processing·AI & Machine Learning·Audio Signal Processing 칸, 2026-10-25 열람)
[^speech]: 누리집 Speech Signal Processing 페이지 <https://hi.snu.ac.kr/speech-signal-processing/> (2026-10-25 열람)
[^aiml]: 누리집 AI & Machine Learning 페이지 <https://hi.snu.ac.kr/ai-machine-learning/> (2026-10-25 열람)
[^audio]: 누리집 Audio Signal Processing 페이지 <https://hi.snu.ac.kr/audio-signal-processing/> (2026-10-25 열람)
[^prof]: 누리집 Professor 페이지 <https://hi.snu.ac.kr/professor/> (Profile, Research Interests, Academic Activities, 2026-10-25 열람)
[^members]: 누리집 Students 페이지 <https://hi.snu.ac.kr/member/> (Ph.D. Students·M.S. Students 카드, 2026-10-25 열람)
[^alumni]: 누리집 Alumni 페이지 <https://hi.snu.ac.kr/alumni/> (2026-10-25 열람)
[^ijournal]: 누리집 International Journals 페이지 <https://hi.snu.ac.kr/int_journals/> (1–12쪽, 117편, 2026-10-25 열람)
[^djournal]: 누리집 Domestic Journals 페이지 <https://hi.snu.ac.kr/do_journals/> (1–3쪽, 25편, 2026-10-25 열람)
[^iconf]: 누리집 International Conference 페이지 <https://hi.snu.ac.kr/int_conference/> (1–15쪽, 145편, 2026-10-25 열람)
[^dconf]: 누리집 Domestic Conference 페이지 <https://hi.snu.ac.kr/do_conference/> (1–20쪽, 193편, 2026-10-25 열람)
[^patents]: 누리집 Patents 페이지 <https://hi.snu.ac.kr/patents/> (1–10쪽, 94건, 2026-10-25 열람)
[^projects]: 누리집 Project 페이지 <https://hi.snu.ac.kr/project/> (1–8쪽, 120건, 2026-10-25 열람)
[^books]: 누리집 Books 페이지 <https://hi.snu.ac.kr/books/> (2026-10-25 열람)
[^news]: 누리집 Notice 게시판 글 「어디서 들어본 목소린데...보이스피싱범 잡는 AI / 연합뉴스TV」 <https://hi.snu.ac.kr/notice/document/85/> (2024-07-12 게시, 2026-10-25 열람)
[^info]: 누리집 INFORMATION 페이지 <https://hi.snu.ac.kr/information/> (2026-10-25 열람)
[^ecelab]: 서울대학교 전기·정보공학부 연구실 목록 <https://ece.snu.ac.kr/research-faculty/research/lab> (연구그룹별 연구실과 교수, 2026-10-25 열람)
[^ecelabv]: 서울대학교 전기·정보공학부 연구실 상세(휴먼인터페이스연구실) <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=8> (영문 이름, 지도·연구, 연구실 소개 및 연구분야, 2026-10-25 열람)
[^eceprof]: 서울대학교 전기·정보공학부 교수 상세(김남수) <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p004> (전화·사무실, 학위·전공·분야, 학력, 주요경력, Research Interest, 2026-10-25 열람)
[^p1]: M. Kim, M. Jeong, J. Y. Lee, N. S. Kim, IEEE Signal Processing Letters 32, 646-650 (2025). <https://doi.org/10.1109/lsp.2025.3528858> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: M. Jeong 외, N. S. Kim, Interspeech 2021, 3605-3609 (온라인 2021-08-30). <https://doi.org/10.21437/interspeech.2021-469> 초록 기준(학회 아카이브 게시 초록). 학회 아카이브 페이지 <https://www.isca-archive.org/interspeech_2021/jeong21_interspeech.html>.
[^p3]: H. Lee, J. W. Yoon, S. Kim, N. S. Kim, IEEE Signal Processing Letters 32, 26-30 (2025). <https://doi.org/10.1109/lsp.2024.3491019> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: J. W. Yoon, B. J. Woo, N. S. Kim, Interspeech 2024, 2400-2404 (온라인 2024-09-01). <https://doi.org/10.21437/interspeech.2024-80> 초록 기준(학회 아카이브 게시 초록). 학회 아카이브 페이지 <https://www.isca-archive.org/interspeech_2024/yoon24_interspeech.html>.
[^p5]: S. H. Mun 외, N. S. Kim, IEEE Access 9, 167615-167627 (2021). <https://doi.org/10.1109/access.2021.3137190> 초록 기준(arXiv 판). arXiv 판 <https://doi.org/10.48550/arxiv.2112.08929>.
[^p6]: J. Y. Kang 외, N. S. Kim, ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 1-5 (2025). <https://doi.org/10.1109/icassp49660.2025.10888053> 초록 기준(arXiv 판). arXiv 판 <https://doi.org/10.48550/arxiv.2504.15663>.
[^p7]: S. Ahn 외, N. S. Kim, IEEE Journal of Selected Topics in Signal Processing 18, 1517-1530 (2024). <https://doi.org/10.1109/jstsp.2024.3469530> 초록 기준(arXiv 판). arXiv 판 <https://doi.org/10.48550/arxiv.2405.04752>.
[^p8]: Y. Jun, B. Woo, M. Jeong, N. Kim, Interspeech 2025, 4073-4077 (온라인 2025-08-17). <https://doi.org/10.21437/interspeech.2025-1721> 초록 기준(학회 아카이브 게시 초록). 학회 아카이브 페이지 <https://www.isca-archive.org/interspeech_2025/jun25_interspeech.html>.

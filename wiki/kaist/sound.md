# 스마트 사운드 연구실 (Smart Sound Lab)

**KAIST AI시스템학과·전기및전자공학부 · 최정우 교수**

- 분야: 공간 음향, 오디오·음성 인공지능, 다채널 음성 향상·음원 분리, 목표 음원 추출, 음향 사건 위치 추정·탐지, 소리로 방 구조 추정, 방 임펄스 응답 합성, 바이노럴 렌더링, 기계 이상음 탐지
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: 음향·오디오 AI[^home][^p1][^p2], 3차원 복원·인식[^p5], 이상·변화점 탐지[^p7], 고장 진단·수명 예측[^research][^p8], 가상·증강현실[^research], 멀티모달 AI[^dataset]
- 홈페이지: <https://sound.kaist.ac.kr>
- 근거와 출처: [Smart Sound Lab 근거 페이지](sound-sources.md)

> 여러 개의 마이크로 받은 소리를 인공지능으로 분석해 원하는 말소리와 소리만 골라내고, 소리가 오는 방향과 방의 모양을 알아내며, 기계가 내는 이상한 소리를 잡아내고, 헤드폰으로 듣는 가상현실의 소리를 실감 나게 만드는 공간 음향·오디오 인공지능 연구실이다.[^home][^research][^p2][^p5]

## 무엇을 연구하나

연구실은 공간 음향(Spatial Audio, 소리가 나는 방향·위치 같은 공간 정보까지 담은 소리)과 오디오 인공지능 연구를 이끈다고 소개한다.[^home] 최정우 교수의 주된 연구 분야는 공간 음향과 음성을 위한 인공지능, 능동 음향 제어(소리를 내어 공간의 소리를 원하는 대로 조절하는 기술), 스피커와 마이크로폰을 여러 개 늘어놓은 배열의 신호 처리다. 음장 재현(어떤 공간의 소리를 다른 곳에서 다시 만들어 내는 것)과 소리를 한곳에 모으는 기술, 그 음향 시스템 응용도 연구 관심사다.[^prof] 연구 페이지는 음성 향상·분리, 바이노럴 렌더링, 방 형태 추정, 이상음 탐지, 목표 음원 추출, 음향 사건 위치 추정·탐지의 여섯 갈래를 든다.[^research]

첫째 갈래는 **다채널 음성 향상과 청각 장면 분석**이다. 야외에서 여러 마이크로 녹음하면 주변 소음이 섞이기 마련이라, 원하는 말소리가 잘 들리게 하려면 소음을 눌러야 한다고 연구실은 설명한다.[^research] 대표 논문에서는 트랜스포머(신호 안 요소들이 서로를 얼마나 참고할지 학습하는 신경망 구조)로 만든 다채널 음성 향상 모델 DeFTAN-II의 계산량을 크게 줄이면서 성능을 높였고,[^p1] 여러 소리의 분리, 잔향 제거, 소리 사건 탐지, 분류, 소리 방향 추정을 한 모델 안에서 함께 하는 청각 장면 분석 모델 DeepASA를 내놓았다.[^p2] 최정우 교수는 DeepASA 연구로 2025 KAIST 대표연구성과 10선에 선정되었다.[^news]

둘째 갈래는 **목표 음원 추출과 음향 사건 위치 추정·탐지**다. 붐비는 카페에서도 친구의 말소리만 골라 듣는 뇌처럼, 여러 소리가 섞인 녹음에서 특정 소리만 정확히 뽑아내는 딥러닝 모델을 연구한다.[^research] 대표 논문에서는 소리가 오는 방향과 소리가 난 시각을 단서로 여러 채널의 목표 소리를 그대로 뽑아내는 틀을 만들었고,[^p3] 여러 마이크 신호로 소리 사건의 종류와 방향을 함께 알아내는 과제에서 채널·주파수·시간 정보에 주의 집중을 따로 적용하는 모델을 제안했다.[^p4] 연구팀은 국제 음향 분석 대회 DCASE 2025 챌린지의 Task 4(Spatial Semantic Segmentation of Sound Scenes)에서 1위를 했고, 같은 해 이 대회의 Judge’s Award와 DCASE 2025 Workshop Best Student Paper Award를 받았다.[^news]

셋째 갈래는 **소리로 방 구조 읽기와 공간 음향 생성**이다. 카메라로 찍은 실내 영상에는 가려진 곳이 있어 정확한 실내 디지털 트윈(실제 공간을 컴퓨터 안에 똑같이 만든 모형)을 만들기 어렵기 때문에, 연구실은 벽에서 되돌아오는 메아리로 방 모양을 알아낸다.[^research] 대표 논문의 EchoScan은 방 임펄스 응답(소리를 냈을 때 방이 돌려주는 반응을 기록한 신호, RIR) 속 여러 번 반사된 메아리까지 써서, 곡면 벽이 있는 복잡한 방의 평면도와 높이 지도를 바로 추정한다.[^p5] 또 측정하지 않은 위치에서 들릴 RIR을 신경망으로 합성하는 방법을 만들었다.[^p6] 헤드폰으로 듣는 AR/VR 기기의 가상 소리가 실제 공간에서 나는 것처럼 들리도록, 두 귀에 들어오는 방의 반응(바이노럴 방 임펄스 응답, BRIR)을 효율적으로 설계하는 연구도 한다.[^research]

넷째 갈래는 **기계 이상음 탐지**다. 이상한 소리를 찾아내면 장비 고장을 일찍 알아채 정비 효율을 높이고, 보안 사고 대응과 교통사고 예방, 도시 소음 관리에도 도움이 된다고 연구실은 설명한다.[^research] 대표 논문에서는 같은 종류의 정상 데이터를 촘촘히 모으고 정상과 이상 소리 사이의 각도 차이를 넓히는 학습 기법 Noisy-ArcMix를 제안했고,[^p7] 섞은 소리로 학습하는 Mixup과 각도 여유를 두는 ArcFace를 합친 기법으로 기계 상태 감시의 이상음 탐지 성능을 더 높였다.[^p8]

연구실은 드론 고장 탐지용 드론 소리 데이터셋, 구형 마이크로폰 배열 9개와 스피커 위치 392곳으로 잰 방 임펄스 응답 데이터셋(6DRIRset), 대형 오디오 언어 모델(소리를 듣고 이해해 글로 답하는 인공지능)의 말소리·장면·사건 이해를 평가하는 벤치마크 SSEU-Bench, 움직이는 음원이 섞인 다채널 분리·분류용 ASA2 데이터셋을 공개하고 있다.[^dataset] 연구실 지원 안내는 학생이 참여할 과제로 음향 사건 위치 추정·탐지, 방향과 거리 단서를 쓰는 다채널 목표 음원 추출, 대형 오디오 언어 모델의 공간 음향 이해, 공간 음향 렌더링을 든다.[^apply]

## 주요 연구 주제

### 1. 다채널 음성 향상과 청각 장면 분석

계산량을 줄인 다채널 음성 향상 모델, 분리·잔향 제거·탐지·분류·방향 추정을 함께 하는 청각 장면 분석 모델.[^p1][^p2] 대표 논문 1–2.

### 2. 목표 음원 추출과 음향 사건 위치 추정·탐지

방향·시각 단서로 다채널 목표 소리 추출, 채널·주파수·시간 영역별 주의 집중으로 소리 사건의 종류와 방향 추정.[^p3][^p4] 대표 논문 3–4.

### 3. 소리로 방 구조 읽기와 공간 음향 생성

메아리로 복잡한 방의 평면도·높이 지도 추정, 측정하지 않은 위치의 방 임펄스 응답 합성, AR/VR용 바이노럴 렌더링.[^p5][^p6][^research] 대표 논문 5–6.

### 4. 기계 이상음 탐지

정상 작동음만으로 학습해 고장 소리를 찾아내는 이상음 탐지 학습 기법.[^p7][^p8] 대표 논문 7–8.

## 대표 논문

랩 논문 목록의 2021–2026년 논문 가운데 최정우 교수가 마지막 저자인 것에서 연구 갈래를 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2024 | [DeFTAN-II: Efficient Multichannel Speech Enhancement With Subgroup Processing](https://doi.org/10.1109/taslp.2024.3488564) · IEEE/ACM Transactions on Audio, Speech, and Language Processing | 트랜스포머는 음성 향상(녹음에서 소음을 걷어 내 말소리를 또렷하게 하는 것)에서 성공했지만, 가까운 부분끼리의 관계를 잡기 어렵고 계산량과 메모리 사용이 크다. 가까운 부분의 특징을 강조한 묶음과 원래 특징 묶음을 함께 처리하는 "부분군 처리"를 넣은 다채널 음성 향상 모델 DeFTAN-II를 만들었다. 공간 특징을 뽑는 블록에서는 묶음을 차례로 이어 처리해 계산량과 메모리를 줄였고, 시간·주파수 관계를 보는 트랜스포머에는 묶음끼리 서로를 참고하는 교차 주의를 넣었다. 최신 다채널 음성 향상 모델들보다 훨씬 적은 계산량으로 더 나은 성능을 냈고, 추가 학습 없이 실제 녹음에서도 잘 작동했다.[^p1] | 1저자 D. Lee, 마지막 저자 최정우 |
| 2 | 2025 | [DeepASA: An Object-Oriented Multi-Purpose Network for Auditory Scene Analysis](https://doi.org/10.52202/085713-5667) · Advances in Neural Information Processing Systems (NeurIPS) | 비슷한 소리 여러 개가 시간에 겹치고 공간에서 움직이는 복잡한 소리 장면을 위한 청각 장면 분석 모델이다. 여러 마이크 입력에서 여러 소리를 나누어 내는 분리, 잔향 제거, 소리 사건 탐지, 오디오 분류, 소리가 오는 방향 추정을 한 틀에서 한다. 여러 소리 특징을 소리 하나하나("객체")에 묶은 표현으로 바꾸고 추론을 이어 가며 다듬는 방식을 써서, 기존의 트랙별 처리에서 생기던 "어느 값이 어느 소리의 것인지" 모호함을 없앴다. 앞 단계에서 분리가 틀리면 뒤 과제가 실패할 수 있어, 추정한 청각 변수로 객체 특징을 되풀이해 고치는 단계를 넣었다. ASA2, MC-FUSS, STARSS23 같은 공간 음향 벤치마크 데이터의 모든 과제에서 최고 수준 성능을 냈다.[^p2] | 1저자 D. Lee, 마지막 저자 최정우 |
| 3 | 2025 | [Multichannel-to-Multichannel Target Sound Extraction Using Direction and Timestamp Clues](https://doi.org/10.1109/icassp49660.2025.10890145) · ICASSP 2025 (IEEE International Conference on Acoustics, Speech and Signal Processing) | 목표 음원 추출은 사용자가 준 단서로 특정 소리만 분리하는 기술인데, 보통 소리 종류 이름이나 소리가 나는 시간 정보를 단서로 한 채널 소리만 뽑는다. 다채널 소리의 공간 정보를 지키려고 여러 채널의 목표 소리를 그대로 뽑아내는 틀(M2M-TSE)을 만들었고, 소리가 오는 방향과 소리가 난 시각을 단서로 쓸 수 있게 했다. 트랜스포머 기반 구조가 여러 방 환경에서 다양한 종류의 소리를 섞어 만든 다채널 신호에서 이 과제를 해냈다. 다채널로 뽑게 하는 것만으로 신경망이 방향 단서를 직접 다룰 수 있어, 손으로 설계한 공간 특징이 필요 없었다.[^p3] | 1저자 D. Choi, 마지막 저자 최정우 |
| 4 | 2024 | [CST-Former: Transformer with Channel-Spectro-Temporal Attention for Sound Event Localization and Detection](https://doi.org/10.1109/icassp48485.2024.10447181) · ICASSP 2024 | 음향 사건 위치 추정·탐지(SELD)는 여러 마이크 신호로 소리 사건의 종류를 가리고 소리가 오는 방향을 찾는 과제다. 기존 연구는 주파수·채널 정보를 시간 축 주의 집중의 입력으로만 써서 주파수·공간 쪽의 쓸모 있는 특징을 뽑기 어려웠다. 채널·주파수·시간 정보에 주의 집중을 따로 적용하는 CST-former를 제안하고, 채널 쪽 주의 집중의 입력에 가까운 주파수·시간 정보를 담는 기법(ULE)을 더했다. 2022년과 2023년 DCASE 챌린지 Task 3 데이터로 실험해, 영역마다 나눈 주의 집중과 ULE가 성능을 높임을 확인했다.[^p4] | 1저자 Y. Shul, 마지막 저자 최정우 |
| 5 | 2024 | [EchoScan: Scanning Complex Room Geometries via Acoustic Echoes](https://doi.org/10.1109/taslp.2024.3485516) · IEEE/ACM Transactions on Audio, Speech, and Language Processing | 실내 공간의 모양을 정확히 아는 것은 정밀한 디지털 트윈을 만드는 데 중요하고, 낯선 곳에서의 길 찾기와 특히 어두운 곳에서의 대피 계획 같은 쓰임이 있다. 기존 소리 기반 기법은 벽 위치나 방 크기 같은 변수만 추정해 알아낼 수 있는 방 모양이 제한됐다. EchoScan은 메아리를 이용해 방의 평면도와 높이 지도를 바로 추정하는 심층 신경망으로, 곡면 벽이 있는 복잡한 방도 다룬다. 여러 번 반사된 소리까지 써서, 오디오 기기 위치에서 보이지 않는 벽이 있어도 방 모양을 추정한다. 맨해튼·애틀랜타형 배치를 포함한 복잡한 공간에서 합성한 RIR로, 시중 기기와 맞는 오디오 기기 구성을 써서 학습·평가했다.[^p5] | 1저자 I. Yeon, 마지막 저자 최정우 |
| 6 | 2026 | [Neural Acoustic Multipole Splatting for Room Impulse Response Synthesis](https://doi.org/10.1109/icassp55912.2026.11463493) · ICASSP 2026 | 공간 음향 재생 같은 응용에는 아무 듣는 위치에서나 방 임펄스 응답(RIR)을 예측할 수 있어야 한다. 소리를 내는 가상의 다중극(방향마다 세기가 다른 음원)의 위치를 학습하고 각 다중극이 내는 신호와 방향 특성을 신경망으로 예측해, 측정하지 않은 위치의 RIR을 합성하는 NAMS를 제안했다. 다중극들의 조합으로 음장을 나타내 복잡한 소리 장면을 표현하면서도 헬름홀츠 방정식(소리 파동이 따르는 방정식) 같은 물리 조건을 지킨다. 다중극을 촘촘히 뿌린 뒤 학습하면서 불필요한 것을 지워 나가는 가지치기를 썼다. 실제·합성 데이터 모두에서 대부분 지표가 이전 방법보다 좋았고 추론이 빨랐으며, 가지치기한 다중극 모델은 극의 20%만으로 단극 모델보다 좋은 성능을 냈다.[^p6] | 1저자 G. Baek, 마지막 저자 최정우 |
| 7 | 2024 | [Noisy-Arcmix: Additive Noisy Angular Margin Loss Combined With Mixup For Anomalous Sound Detection](https://doi.org/10.1109/icassp48485.2024.10447764) · ICASSP 2024 | 비지도 이상음 탐지는 정상 작동 소리의 특징을 배운 뒤 그와 다른 소리를 찾아낸다. 기존 방법은 같은 종류 데이터를 한데 충분히 모으지 못하고, 표본과 그 종류의 중심 사이에 각도 차이가 생겼다. 같은 종류 데이터를 촘촘히 모으고 정상과 이상 표본 사이의 각도 차이를 넓히는 학습 기법과, 어느 시간 구간을 강조하거나 누를지 배우는 구조를 제안했다. DCASE 2020 챌린지 Task 2 데이터에서 최신 방법보다 탐지 성능 지표 세 가지(AUC, pAUC, mAUC)에서 각각 0.90%, 0.83%, 2.16% 높은 최고 성능을 냈다.[^p7] | 1저자 S. Choi, 마지막 저자 최정우 |
| 8 | 2024 | [Integrating Mixup and ArcFace for enhanced anomalous sound detection](https://doi.org/10.3397/in_2024_3869) · INTER-NOISE and NOISE-CON Congress and Conference Proceedings (Inter-Noise 2024) | 기계 상태 감시에서는 제때 정비하려면 이상한 소리를 정확히 잡아내야 한다. 정상·비정상 작동음을 분류 신뢰도로 가르는 기존 자기지도 학습 모델은 과적합이나 지나친 확신 때문에 효과가 떨어진다. 섞은 소리 데이터로 학습해 일반화를 돕는 Mixup과, 각도 여유를 두어 종류 사이 거리를 넓히는 ArcFace를 합쳤다. ArcFace의 각도 여유는 한 종류에만 정해져 섞인 데이터에는 정하기 어려워, 섞은 비율에 따라 종류마다 다른 각도 여유를 두었다. DCASE2020 Task 2 데이터에서 Noisy-ArcMix 모델보다 이상 탐지 성능이 크게 좋았다.[^p8] | 1저자 J. Choi, 마지막 저자 최정우 |

## 교수와 전문 분야

최정우 교수는 KAIST에서 기계공학 학사(1999)·석사(2001)·박사(2005)를 받았다. 2006–2007년 영국 사우샘프턴대 Institute of Sound and Vibration Research(ISVR)의 박사후연구원, 2007–2011년 삼성전자 종합기술원(SAIT)에서 일했고, 이어 2014년까지 KAIST 기계공학과 연구부교수(Research Associate Professor)를 지냈다. 2015년 KAIST 전기및전자공학부에 부임해 2023년 정년을 보장받았고(tenure), 2026년 4월부터 AI시스템학과 부교수(Associate Professor)이자 전기및전자공학부 겸임교수(Adjunct Professor)다.[^prof] 책 *Sound Visualization and Manipulation*(Wiley, 2013)의 공저자이고, IEEE, Audio Engineering Society, Korean Society for Noise and Vibration Engineering의 회원이며 Acoustical Society of America의 Technical Committee on Signal Processing in Acoustics 위원이다.[^prof] Professor 페이지에 적힌 학술 활동은 Keynote Lecture(Acoustical Society of Korea, 2026 Spring Conference, Jeju, 2026), Local Scientific Committee(31st International Congress on Sound and Vibration (ICSV31), Incheon, 2025), Keynote Forum(NOVEM 2023, New Zealand, 2023), IET Signal Processing Associate Editor(2017–2021), 26th International Conference on Multimedia Modeling(MMM 2020) Organizing Chair(2020), Mechanical Systems and Signal Processing Editorial Board Member(2017–2020), 2016 AES International Conference on Sound Field Control(Guildford, UK) Paper Chair(2016), Journal of the Audio Engineering Society Special issue on Sound Field Control Guest Editor(2014), Inter-Noise 2014(Melbourne, Australia) Plenary Lecture(2014)다.[^prof] 연구실 소식에 따르면 KAIST 50주년 우수 강의상과 2020년 가을학기 우수 강의상(2021), 개교 52주년 기념 창의강의 대상(2023)을 받았다.[^news]

논문으로 보면 전문 분야는 세 갈래다.

- **다채널 음성 향상, 청각 장면 분석, 목표 음원 추출과 음향 사건 위치 추정**.[^p1][^p2][^p3][^p4]
- **메아리로 방 구조를 읽고 방 임펄스 응답을 합성하는 공간 음향**.[^p5][^p6]
- **정상 작동음으로 학습하는 기계 이상음 탐지**.[^p7][^p8]

## 응용 분야

연구 페이지는 응용으로 유튜브 같은 라이브 스트리밍의 야외 다채널 녹음에서 소음을 걷어 내는 일, AR/VR 기기의 실감 나는 가상 소리, 실내 공간의 디지털 트윈, 설비 고장 조기 발견·보안 사고 대응·교통사고 예방·도시 소음 관리를 든다.[^research] 대표 논문으로 보면 낯선 곳의 길 찾기와 어두운 곳의 대피 계획,[^p5] 공간 음향 재생,[^p6] 기계 상태 감시와 정비에 닿아 있다.[^p7][^p8] 공개한 드론 소리 데이터셋은 드론의 기계 고장을 실시간으로 찾아 운용 안전을 높이려고 만든 것이다.[^dataset] 졸업생은 삼성리서치, 삼성전자, ETRI, Meta Reality Labs, NAVER, 현대자동차, LIG Nex1 등으로 진출했다.[^alumni]

## 구성원

2026년 10월 21일 랩 Our Team 페이지 기준이다. 과정은 랩 표기다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Jihoon Choi | 박사과정 | DNN-based Anomaly Detection | wlgns2533@kaist.ac.kr | 8 |
| Dayun Choi | 박사과정 | Target Sound Extraction, Multimodal Analysis | cdy3773@kaist.ac.kr | 3 |
| Geonwoo Baek | 박사과정 | 3D and Metaverse Audio Rendering | bkw6287@kaist.ac.kr | 6 |
| Younghoo Kwon | 박사과정 | Source Localization and Event Detection | k0hoo@kaist.ac.kr | 2 |
| Han Yin | 박사과정 | Audio Understanding | hanyin@kaist.ac.kr |  |
| Hongju Jeong | 박사과정 | Binaural SELD | hongjuj0329@kaist.ac.kr |  |
| Yongjoon Lee | 석사과정 | General Speech Restoration | yongjoonlee@kaist.ac.kr |  |
| Dohwan Kim | 석사과정 | Speech Enhancement | dohwan@kaist.ac.kr |  |
| Juseung Lee | 석사과정 | RIR Estimation | ljsjoa@kaist.ac.kr |  |
| Junwoo Park | 석사과정 | DOA Estimation | park.junwoo@kaist.ac.kr |  |
| Kijoong Kwon | 석사과정 | Text-to-Audio Generation | kijoongkwon@kaist.ac.kr |  |
| Hyungjun Yoo | 석사과정 | Target Speaker Extraction | hyungjun@kaist.ac.kr |  |
| Minsoo Kim | 석사과정 |  | chaehwasu@kaist.ac.kr |  |
| Minjeong Kim | 석사과정 |  | minjeongkim@kaist.ac.kr |  |
| Jooeun Lim | 인턴 | Neural Acoustic Field | jooeun9199@kaist.ac.kr |  |

## 졸업생과 이전 구성원

랩 Alumni 페이지의 이름과 랩이 적은 현재 자리다. 학위·과정은 페이지의 칸 이름(Ph.D. Alumni, Master Alumni)이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Sooyeon Park | Ph.D. | Samsung Research |
| Yusun Shul | Ph.D. | Samsung Electronics |
| Byeongho Jo | Ph.D. | ETRI |
| Jaehyoun Yoo | Ph.D. | ETRI |
| Dongheon Lee | Ph.D. | Meta Reality Labs |
| Donghwan Kim | Master | NAVER |
| Sooyoung Park | Master | ETRI |
| Guensoo Jo | Master |  |
| Hyungjun So | Master | TmaxSoft |
| Jaegyu Noh | Master | GAUDIO |
| Minsung Kang | Master | Samsung Electronics |
| Jeongmin Liu | Master | NAVER |
| Hyeongmin Oh | Master | Samsung Research |
| Pilsun Eu | Master | GAUDIO |
| Kyeongseok Jeong | Master | NAVER |
| Hyunjun Lee | Master | TmaxSoft |
| Seongrae Kim | Master | Nimble Neuron |
| Kyeonji Kim | Master | Hyundai Motor Company |
| Jihoon Choi | Master | KAIST Smart Sound Lab Ph.D. |
| Taehun Choe | Master |  |
| Geonwoo Baek | Master | KAIST Smart Sound Lab Ph.D. |
| Soonhyeon Choi | Master | LIG Nex1 |
| Yewon Kim | Master |  |
| Seojin Park | Master |  |
| Hongju Jeong | Master | KAIST Smart Sound Lab Ph.D. |

## 최근 논문 목록 (2021–2026)

랩 Publications 페이지에 올라 있는 2021년 이후 논문과 학회 발표(국내 학회 발표 포함)다. 저자 이름 뒤 *는 랩 표기다.[^papers]

**2026**

- Younghoo Kwon, Junwoo Park, Han Yin, Jung-Woo Choi. "A Multi-Stage Separation-and-Classification Framework Guided by Complementary Acoustic-to-Semantic Clues". *DCASE challenge Technical report*.
- Han Yin, Yang Xiao, Younghoo Kwon, Ting Dang, Jung-Woo Choi. "Focus Then Listen: An Empirical Study of Plug-and-Play Audio Enhancer for Noise-Robust Large Audio Language Models". *ICML Workshop*.
- Dohwan Kim, Jung-Woo Choi. "MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation". *Interspeech*.
- Yongjoon Lee, Jung-Woo Choi. "SEMamba++: A General Speech Restoration Framework Leveraging Global, Local, and Periodic Spectral Patterns". *Interspeech (Long paper track)*.
- Yongjoon Lee, Jung-Woo Choi. "RAF: Relativistic Adversarial Feedback For Universal Speech Synthesis". *Interspeech (Long paper track)*.
- J.-W. Choi. "Unified Spatial Audio AI for Beyond-Human Auditory Scene Understanding". *Keynote Lecture, Spring Conference of the Acoustical Society of Korea, Seogwipo, Korea*.
- G. Baek, J.-W. Choi\*. "Neural Acoustic Field Generation: A comparative Analysis Across Varying Numbers of Observation Points". *Spring Conference of the Acoustical Society of Korea, Seogwipo, Korea*.
- H. Jeong, J.-W. Choi\*. "Rank-based Loss for Binaural Sound Source Localization". *Spring Conference of the Acoustical Society of Korea, Seogwipo, Korea*.
- Dohwan Kim, Jung-Woo Choi. "Dispatch: Distilling Selective Patches for Speech Enhancement". *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), Barcelona, Spain*.
- Han Yin, Jung-Woo Choi. "Can Large Audio Language Models Understand Audio Well?". *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), Barcelona, Spain*.
- Dayun Choi, Jung-Woo Choi. "SoundCompass:Navigating Target Sound Extraction With Effective Directional Clue Integration". *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), Barcelona, Spain*.
- Geonwoo Baek, Jung-Woo Choi. "Neural Acoustic Multipole Splatting for Room Impulse Response Synthesis". *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), Barcelona, Spain*.

**2025**

- D. Lee, Y. Kwon, and J-W. Choi. "DeepASA: An Object-Oriented Multi-Purpose Network for Auditory Scene Analysis". *Conference on Neural Information Processing Systems (NeurIPS), San Deigo, USA*.
- Y. Kwon, D. Lee, D. Kim, and J-W. Choi. "Self-Guided Target Sound Extraction and Classification through Universal Sound Separation Model and Multiple Clues". *DCASE workshop, Barcelona, Spain*.
- S. Park, J. Choi and J-W. Choi. "Description on 2025 ICSV AI challenge: Anomalous drone detection from sounds recorded in noisy environments". *31st International Congress on Sound and Vibration, Incheon, Korea, July*.
- G. Kim, J.-W. Choi\*. "Visualizing the Depth of Indoor Spaces Using Room Impulse Responses". *Spring Conference of the Acoustical Society of Korea, Seogwipo, Korea*.
- Y. Kwon, and J.-W. Choi\*. "Speech-Declipping Transformer with Complex Spectrogram and Learnable Temporal Features". *Spring Conference of the Acoustical Society of Korea, Seogwipo, Korea*.
- G. Baek, and J-W. Choi\*. "Validity of the Interaural Cross-Correlation Coefficient as an Objective Metric for the Apparent Source Width of a Lateral Sound Source". *2025 Spring Conference of the Acoustical Society of Korea, Seogwipo, Korea, May*.
- S. Park and J-W. Choi\*. "Machine Anomaly Detection based on Classification using a Pretrained EAT Model". *Spring Annual Conference of KSNVE 2025, Jeju, Korea, May*.
- J. Choi and J-W. Choi\*. "A Robust machine sound anomaly detection against external noise by predicting future prediction in latent space". *Spring Annual Conference of KSNVE 2025, Jeju, Korea, May*.
- I. Yeon and J-W. Choi. "Complex room geometry inference via acoustic echoes". *Forum acusticum euronoise 2025. EAA (european acoustics association)*.
- D. Lee and J-W. Choi. "Universal auditory scene analysis model for source separation, event localization, and detection". *Forum acusticum euronoise 2025. EAA (european acoustics association)*.
- Y. Kim, S. Choi, W. Choi, and J-W. Choi. "Target detection and classification via multi-task learning of prediction and classification". *31st International Congress on Sound and Vibration, Incheon, Korea, July*.
- D. Lee and J-W. Choi. "DeFT-Mamba: Universal Multichannel Sound Separation and Polyphonic Audio Classification". *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Hyderabad, India, Apr*.
- D. Choi and J-W. Choi. "Multichannel-to-Multichannel Target Sound Extraction Using Direction and Timestamp Clues". *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), Hyderabad, India, Apr*.

**2024**

- I. Yeon and J-W. Choi. "RGI-NET: 3D Room Geometry Inference from Room Impulse Responses in Absence of First-order Echoes". *IWAENC, Aalborg, Denmark*.
- D. Lee and J-W. Choi. "DeFTAN-AA: Array Geometry Agnostic Multichannel Enhancement". *INTERSPEECH, Kos Island*.
- J. Choi and J-W. Choi. "Integrating Mixup and ArcFace for Enhanced Anomalous Sound Detection". *Inter-Noise, Nantes, France*.
- S. Kim, J. Yoo, and J.-W. Choi. "Echo-aware Room Impulse Response Generation". *Journal of the Acoustical Society of America, vol. 156, Issue 1, pp.623-637*.
- Y. Lee, I. Yeon, J. Nam, and J-S Chung. "VoiceLDM: Text-to-Speech with Environmental Context". *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Seoul, Korea*.
- Y. Shul and J-W. Choi. "CST-FORMER: Transformer with Channel-Spectro-Temporal Attention for Sound Event Localization and Detection". *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Seoul, Korea*.
- S. Choi, I. Cho, J. Hyun, W. Choi, S. Sohn, and J.-W. Choi. "Research for Drone Target Classification Method Using Deep Learning Techniques". *Journal of the Korea Institute of Military Science and Technology, Vol. 27, No. 2, pp. 189-196*.
- D. Choi, and J-W. Choi\*. "Target sound extraction on reverberant mixture using sound-class label and timestamp information". *2024 Spring Conference of the Acoustical Society of Korea, Seogwipo, Korea, pp. 335-336, May*.
- I. Yeon, I. Jeong, S. Lee, and J-W. Choi\*. "Complex room geometry inference using room impulse responses". *2024 Spring Conference of the Acoustical Society of Korea, Seogwipo, Korea, pp. 333-334, May*.
- D. Lee, and J-W. Choi\*. "Multichannel speech enhancement and separation using rotary positional embedding". *Spring Annual Conference of KSNVE 2024, Jeju, Korea,May*.
- S. Choi and J-W. Choi\*. "Techniques for generating and training diverse normal machine sound data to ensure robustness against unseen data". *Spring Annual Conference of KSNVE 2024, Jeju, Korea, May*.
- J. Choi, and J.-W. Choi\*. "Time Series Learning in Feature Space for Anomaly Detection in Various Noisy Environments". *Spring Annual Conference of KSNVE 2023, Jeju, Korea, May*.
- Y. Kim, S. Choi, W. Choi and J-W. Choi\*. "Classification of projectile trajectory time-series data using a deep neural network based on channel and temporal attention". *Autumn Annual Conference of KSNVE 2024, Jeongseon, Korea, p85, October*.
- D. Choi, and J-W. Choi\*. "Target sound extraction on multichannel reverberant mixture". *2024 Fall Conference of the Acoustical Society of Korea, Busan, Korea, pp. 170-171, October*.
- I. Yeon, I. Jeong, S. Lee, and J-W. Choi. "EchoScan: Scanning Complex Room Geometries via Acoustic Echoes". *IEEE/ACM Transactions on Audio, Speech, and Language Processing (TASLP)*.
- S. Choi and J-W. Choi. "Noisy-ArcMix: Additive Noisy Angular Margin Loss Combined With Mixup Anomalous Sound Detection". *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Seoul, Korea*.
- D. Lee and J-W. Choi. "DeFTAN-II: Efficient Multichannel Speech Enhancement with Subgroup Processing". *IEEE/ACM Transactions on Audio, Speech, and Language Processing (TASLP)*.

**2023**

- T. Choe and J-W. Choi. "Impact of Direct-to-Reverberation Ratio and Interaural Cross-Correlation on Externalization in Binaural Audio Rendering". *Acoustics 2023, Sydney, Australia*.
- D. Choi and J-W. Choi. "Target sound extraction on reverberant mixture". *Acoustics 2023, Sydney, Australia*.
- Y. Shul and J-W. Choi. "Divided spectro-temporal transformer for sound event localization and detection in real scenes". *Acoustics 2023, Sydney, Australia*.
- D. Lee and J-W. Choi. "DeFT-AN RT: Real-time Multichannel Speech Enhancement using Dense Frequency-Time Attentive Network and Non-overlapping Synthesis Window". *INTERSPEECH 2023, Dublin, Ireland*.
- J. Choi and J-W. Choi. "Prediction-segmentation tasks for self-supervision of anomaly detection networks under noisy conditions". *Inter-Noise2023, Chiba, Japan*.
- J-W. Choi and F. Zotter. "Six degrees-of-freedom room impulse response dataset measured over a dense loudspeaker grid (6DRIR-DL)". *AES International Conference on Spatial and Immersive Audio, Huddersfield*.
- W. Yi, J-W. Choi., J-W. Lee. "Sound-based drone fault classification using multi-task learning". *Proceedings of the 29th International Congress on Sound and Vibration (ICSV 29), Prague, Czech Republic*.
- G. Kook, Y. Jo, C. Oh, X. Liang, J. Kim, S-M. Lee, S. Kim, J-W. Choi, and H. J. Lee. "Multifocal skull-compensated transcranial focused ultrasound system for neuromodulation applications based on acoustic holography". *Microsystems & Nanoengineering, vol.9, no.1*.
- Y. Shul, W. Yi, J. Choi, D-S. Kang, and J-W. Choi. "Noise-based self-supervised anomaly detection in washing machines using a deep neural network with operational information". *Mechanical Systems and Signal Processing, vol.189*.
- D. Lee and J-W. Choi. "DeFT-AN: Dense Frequency-Time Attentive Network for Multichannel Speech Enhancement". *IEEE Signal Processing Letters, vol.30, pp.155 - 159*.
- D. Choi, D. Lee, and J.-W. Choi\*. "Low Complexity DNN Model for Multichannel Speech Enhancement". *Spring Annual Conference of KSNVE 2023, Samcheok, Korea, May*.
- T. Choe, and J.-W. Choi\*. "Influence of the Presence of Early Reflections on Externalization in Binaural Audio Rendering". *Spring Annual Conference of KSNVE 2023, Samcheok, Korea, May*.
- I. Yeon, I. Jeong, S. Lee, and J.-W. Choi\*. "DNN-Based Room Layout Estimation Method". *Spring Annual Conference of KSNVE 2023, Samcheok, Korea, May*.
- J. Choi, and J.-W. Choi\*. "Deep learning-based Machine Anomaly Detection through Mixing Normal Data and Outlier Data". *Spring Annual Conference of KSNVE 2023, Samcheok, Korea, May*.
- Y. Shul, and J.-W. Choi\*. "Divided Spectral-Temporal Attention-based Sound Event Localization and Detection using Multi-Channel Array Signals". *Spring Annual Conference of KSNVE 2023, Samcheok, Korea, May*.
- G. Baek, T. Choe, and J.-W. Choi\*. "Influence of the Dynamic Reflection Rendering on Perceived Spatial Audio Externalization". *Autumn Annual Conference of KSNVE 2023, Yeosu, Korea, October*.
- J-W. Choi. "Sound field control in real and virtual auditory space". *Proceedings of Noise and Vibration: Emerging Methods (NOVEM), Univ. of Auckland, New Zealand*.

**2022**

- J. Choi and J-W. Choi. "Multi-task learning for acoustic anomaly detection of machine sounds". *PROCEEDINGS of the 24th International Congress on Acoustics, Gyeongju, Korea*.
- W. Yi and J-W. Choi. "On-site Noise Exposure technique for noise-robust machine fault classification". *24th International Congress on Acoustics, Gyeongju, Korea*.
- J-W. Choi and F. Zotter. "3D multi-source localization by joint ESPRIT with multiple spherical arrays". *24th International Congress on Acoustics, Gyeongju, Korea*.
- I. Yeon and J-W. Choi. "3D Room Geometry Inference from Multi-channel Room Impulse Response using Deep Neural Network". *24th International Congress on Acoustics, Gyeongju, Korea*.
- Seongrae Kim, Jung-Woo Choi\*. "Echo-Aware Differentiable Filtered Velvet Noise". *Korean Artificial Intelligence AssociationSummer Conference 2022, Jeju, Korea*.
- D. Lee and J-W. Choi. "Inter-channel Conv-TasNet for source-agnostic multichannel audio enhancement". *InterNoise2022, Glasgow, Scotland*.
- J-W. Choi, F. Zotter, B. Jo, and J-H. Yoo. "Multiarray Eigenbeam-ESPRIT for 3D Sound Source Localization with Multiple Spherical Microphone Arrays". *IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol.30, pp.2310-2325*.
- J. Par, J. Hong, J-W. Choi, M. Hahn. "Determinant-Based Generalized Sidelobe Canceller for Dual-Sensor Noise Reduction". *IEEE Sensors Journal, vol.22, no.9, pp.8858-8868*.
- Yusun Shul, Dong-soo Kang, Jung-Woo Choi\*. "DNN based washing machine anomaly detection using operation information". *Spring Annual Conference of KSNVE 2022, Changwon, Korea, p218, May*.
- Wonjun Yi, Jung-Woo Choi\*. "On-site Noise Exposure Technique for Noise-Robust Machine Fault Classification". *Spring Annual Conference of KSNVE 2022, Changwon, Korea, p217, May*.
- Jihoon Choi, Jung-Woo Choi\*. "Deep learning-based Machine Anomaly Detection using Multiscale Prediction and Classification". *Spring Annual Conference of KSNVE 2022, Changwon, Korea, p216, May*.
- Pilsun Eu, Franz Zotter, Jae-hyoun Yoo, Jung-Woo Choi\*. "Ambisonic Rendering for Diffuse Sound Field Simulations based on Geometrical Acoustics". *The Korean Institute of Broadcase and Media Engineers, 2022추계학술대회, Seoul, Korea, November*.
- Z-J. Zhao, J, Ahn, D. Lee, and J-W. Choi, I. Park, J-H. Jeong, et al. "Wafer-scale, highly uniform, and well-arrayed suspended nanostructures for enhancing the performance of electronic devices". *Nanoscale, vol.14, no.4, pp.1136-1143*.

**2021**

- J-W. Choi. "Generation of a Near-field Sound Zone Using Broadside Differential Array". *2021 Immersive and 3D Audio : from Architecture to Automotive (I3DA), Bologna*.
- D. Lee, B. Jo, and J-W. Choi. "Direction-of-arrival estimation with blind surface impedance compensation for spherical microphone array". *JASA Express Letters, vol.1, no.7*.
- S. Park, and J-W. Choi. "Iterative Echo Labeling Algorithm With Convex Hull Expansion for Room Geometry Estimation". *IEEE/ACM Transactions on Audio, Speech, and Language Processing vol.29, pp.1463-1478*.
- Dongheon Lee, Byeongho Jo, Jung-Woo Choi\*. "Spherical Array Beamforming Robust To Surface Impedance Mismatch". *the ASK Annual Spring Conference 2021, Jeju, Korea, p104, May*.
- Jihoon Choi, Jung-Woo Choi\*. "Deep Learning based Machine Sound Anomaly Detection using Multi-Task Learning". *2nd Korea Artificial Intelligence Conference, Jeju*.
- Dongheon Lee, Byeongho Jo, Jung-Woo Choi\*. "Blind surface impedance compensation for the beamforming using spherical microphone array". *Annual Conference of KIMST, Daejeon, Korea, November*.
- Yusun Shul, Jihoon Choi, Jung-Woo Choi\*. "Deep Learning based Fault Detection for Pressure Pipe Wall Thinning". *Autumn Annual Conference of KSNVE 2021, Jeju, Korea, p261, November*.

## 소식

랩 Announcements 게시판의 2021년 이후 글이다.[^news]

- 2026.05.20 · 최정우 교수 한국 음향학회(ASK) 기조강연 초청
- 2026.04.28 · 최정우 교수, 2025 KAIST 대표연구성과 10선 선정
- 2026.03.03 · 이동헌 박사(지도교수 최정우), 국립부경대 전자정보통신공학부 조교수 임용
- 2025.11.01 · DCASE 2025 Challenge Judge’s Award & DCASE 2025 Workshop Best Student Paper Award 수상
- 2025.07.14 · 백건우 박사과정 2025년 한국음향학회 춘계학술발표대회 우수발표상 수상
- 2025.07.11 · [과기원NOW] 최정우 KAIST 교수팀, 세계 최고 음향 AI 챌린지 세계 1위 外
- 2025.07.02 · 1st Place in DCASE2025 Challenge Task 4
- 2023.03.01 · 유재현, 김성래, 유필선 학위 수여식
- 2023.03.01 · 최정우 교수 KAIST 창의강의대상 수상
- 2022.12.30 · 유필선 석사과정 2022년 한국 방송 미디어 공학회 추계학술대회 우수 학생 논문상 수상
- 2022.11.03 · 설유선 박사과정 2022년도 춘계 소음진동 학술대회 우수 발표상 수상
- 2021.06.23 · 이동헌 석박통합과정 한국음향학회 우수 발표상 수상
- 2021.04.27 · [Paper] Iterative Echo Labeling Algorithm With Convex Hull Expansion for Room Geometry Estimation
- 2021.03.17 · 최정우 교수님 KAIST 50주년 우수 강의상 및 2020년 가을학기 우수 강의상 수상
- 2021.03.16 · 학부 연구생 유필선, 김채원 2020 여름/가을 URP 우수상 수상

## 연락과 위치

- 연구실: KAIST LG이노베이션홀(N24) 2103호 (전화 042-350-7535)[^contact]
- 교수실: KAIST LG이노베이션홀(N24) 2101호[^prof]
- 교수 전화: 042-350-7435[^ais]
- 교수 이메일: jwoo@kaist.ac.kr[^prof]

[^home]: 연구실 누리집 첫 화면 <https://sound.kaist.ac.kr> (2026-10-21 열람)
[^prof]: Professor 페이지 <https://sound.kaist.ac.kr/members/professor> (2026-10-21 열람)
[^research]: Research Area 페이지와 연구 분야별 6쪽 <https://sound.kaist.ac.kr/research> (2026-10-21 열람)
[^dataset]: Dataset 페이지 <https://sound.kaist.ac.kr/dataset> (2026-10-21 열람)
[^apply]: Lab Application 페이지 <https://sound.kaist.ac.kr/about/apply> (2026-10-21 열람)
[^members]: Our Team 페이지 <https://sound.kaist.ac.kr/members/our-team> (2026-10-21 열람)
[^alumni]: Alumni 페이지 <https://sound.kaist.ac.kr/members/alumni> (2026-10-21 열람)
[^papers]: Publications 페이지 <https://sound.kaist.ac.kr/publications> (2026-10-21 열람)
[^news]: Announcements 게시판 <https://sound.kaist.ac.kr/announcements> (2026-10-21 열람)
[^contact]: Contact 페이지 <https://sound.kaist.ac.kr/about/contact> (2026-10-21 열람)
[^ais]: KAIST AI시스템학과 교수진 페이지 <https://aicollege.kaist.ac.kr/ais/faculty> (2026-10-21 열람)
[^p1]: D. Lee, J.-W. Choi, IEEE/ACM Transactions on Audio, Speech, and Language Processing 32, 4850-4866 (2024). <https://doi.org/10.1109/taslp.2024.3488564> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: D. Lee, Y. Kwon, J.-W. Choi, Advances in Neural Information Processing Systems 38, 188566-188593 (2025). <https://doi.org/10.52202/085713-5667> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: D. Choi, J.-W. Choi, ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 1-5 (2025). <https://doi.org/10.1109/icassp49660.2025.10890145> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: Y. Shul, J.-W. Choi, ICASSP 2024 - 2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 8686-8690 (2024). <https://doi.org/10.1109/icassp48485.2024.10447181> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: I. Yeon, I. Jeong, S. Lee, J.-W. Choi, IEEE/ACM Transactions on Audio, Speech, and Language Processing 32, 4768-4782 (2024). <https://doi.org/10.1109/taslp.2024.3485516> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: G. Baek, J.-W. Choi, ICASSP 2026 - 2026 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 22592-22596 (2026). <https://doi.org/10.1109/icassp55912.2026.11463493> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: S. Choi, J.-W. Choi, ICASSP 2024 - 2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 516-520 (2024). <https://doi.org/10.1109/icassp48485.2024.10447764> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: J. Choi, J.-W. Choi, INTER-NOISE and NOISE-CON Congress and Conference Proceedings 270, 6778-6785 (2024). <https://doi.org/10.3397/in_2024_3869> 초록 기준.

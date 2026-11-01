# 계산지능연구실 (Computational Intelligence Laboratory, CI Lab.)

**KAIST 전기및전자공학부·안보과학기술대학원·녹색성장지속가능대학원(겸임)·반도체시스템공학과 · 김창익 교수**

- 대분야: 컴퓨팅·AI, 에너지·환경·지구
- 태그: 컴퓨터 비전[^vision], 생성 인공지능[^p6], 대형 언어 모델[^p1], 멀티모달 AI[^p5], AI·기계학습 보안·프라이버시[^security][^p1], 설명 가능한 AI(XAI)[^explain]
- 홈페이지: <https://cilabs.kaist.ac.kr/>

> 사진·영상과 여러 종류의 자료를 이해하는 인공지능을 만들고, 모델의 안전성·계산 효율·입체 생성과 기상·생태 분석을 연구하는 연구실이다.

## 무엇을 연구하나

계산지능연구실은 KAIST 전기및전자공학부의 신호처리(정보를 담은 자료를 변환·분석하는 기술) 분야에 속하며, 컴퓨터 비전(사진·영상에서 대상과 장면의 정보를 알아내는 기술)과 인공지능을 연구한다. 사진 속 대상의 종류를 알아보고, 영상의 위치별로 대상을 구분하며, 움직이는 사람·차량을 따라가거나 행동을 인식하는 문제가 연구의 출발점이다. 현재 랩 소개는 언어 모델의 추론, 여러 종류의 자료를 함께 다루는 모델에 대한 공격, 입체 시각, 기상·생태 AI와 AI 안전성을 함께 제시한다.[^home][^areas][^vision]

이 연구실은 자료를 통해 판단 규칙을 배우는 기계학습(사례 자료에서 규칙이나 관계를 학습하는 계산 방법)을 여러 조건에서 사용할 방법을 찾는다. 신경망(서로 연결된 계산 단위의 매개변수를 조정해 입력과 출력의 관계를 나타내는 모형)과 딥러닝(여러 층의 신경망을 통해 자료의 표현을 단계적으로 학습하는 기계학습 분야)이 주요 기반이다. 퓨샷 학습(범주마다 적은 예시로 새로운 과제를 학습하는 방법), 자기지도 학습(사람이 붙인 레이블 대신 자료 자체에서 학습 목표를 얻는 방법), 도메인 적응(학습 자료와 사용 자료의 분포 차이에 대응하는 학습 방법)을 다룬다.[^prof][^meta][^domain]

또 다른 축은 인공지능이 조작된 입력이나 추가 학습을 받았을 때의 안전성이다. 적대적 공격(모델이 잘못 판단하거나 의도에 어긋나게 동작하도록 입력 등을 조작하는 공격)과 그 방어를 함께 연구한다. 영상 모델을 속이는 입력이 다른 모델에도 통하는지 살피고, 대형 언어 모델(많은 글을 학습해 언어를 이해하고 생성하는 인공지능 모형)을 사용자의 목적에 맞추어 추가 학습하면서도 안전한 응답을 유지할 방법을 제안한다.[^security][^p1][^p2]

영상 분석의 대상은 사람과 사물에서 날씨와 생태계까지 이어진다. 극단적 이상 기후에 대응하는 초단기 기상예측을 위해 위성 자료로 기상영상 예측 모델을 개발한다. 사람이 계속 관찰하기 어려운 지역에서는 자동 촬영 카메라의 영상으로 포유류의 종을 분류하고, 두루미의 종과 개체 수를 분석하는 시스템을 연구한다.[^climate]

## 주요 연구 주제

### AI 공격·방어와 안전한 추가 학습

영상 인식 모델에 대한 공격과 방어를 연구하며, 인증 가능한 방어(정해진 입력 변화 범위에서 공격 성공이 불가능함을 증명하는 방어)도 다룬다. 최근에는 사용자의 자료로 언어 모델을 미세조정(미리 학습한 모형을 특정 목적의 자료로 추가 학습하는 과정)할 때 유해한 변화를 줄이고 안전한 거절 응답을 유지하는 방법으로 연구를 넓혔다. 공격을 분석하는 일과 방어 모델을 설계하는 일이 한 갈래 안에 있다.[^security][^p1][^p2]

### 영상·복합 자료 이해와 계산 효율

멀티모달 학습(영상·소리처럼 서로 다른 종류의 자료를 함께 이용하는 학습)으로 행동을 인식하고, 일부 자료가 사라져도 사용할 수 있는 모델을 연구한다. 계속 들어오는 동영상에서 현재 행동과 그 시작 시각을 찾고 다음 행동을 예측하는 문제도 다룬다. 소리와 영상의 시간 간격이 서로 다를 때 두 자료를 정렬하는 방법은 감정 인식 연구로 이어진다.[^action][^p5]

영상 이해에 필요한 계산을 줄이는 연구도 있다. VideoMamba는 상태 공간 모델(시간에 따라 변하는 체계의 내부 상태와 관측값의 관계를 나타내는 모형)을 영상에 맞추어 구성한다. Upsample Anything은 특징 지도(영상에서 추출한 특징값을 위치에 맞추어 배열한 자료)의 해상도(공간의 세부 정보를 구별해 표현하는 정도)를 높이는 업샘플링(자료의 공간 표본 수를 늘리는 변환)을 연구한다. 이를 통해 영상의 위치별 판단이나 깊이 추정(화면 속 대상까지의 거리를 추정하는 작업)에 필요한 출력을 얻는다.[^p3][^p4]

### 입체 시각과 생성

영상에서 입체 구조와 움직임을 추정하며 자율주행, 증강·가상현실과 로봇의 이동에 연결한다. 한 장의 사진으로 입체 모습을 만드는 연구에서는 여러 방향에서 본 모습이 서로 맞아야 하는 일관성과 가능한 모양을 다양하게 만들어야 하는 요구를 함께 다룬다. HarmonyView는 확산 모델(자료에 잡음을 넣는 과정을 거꾸로 학습해 자료를 생성하는 모형)의 샘플링(정해진 확률 분포에 따라 값을 뽑는 과정)을 조절해 이 두 요구를 함께 다루는 방법이다. 복잡한 문장에 들어 있는 대상과 관계에 맞추어 이미지를 생성하는 연구도 진행한다.[^three][^p6][^diffusion]

### 기상·생태 AI

기상 연구는 위성영상에서 앞으로의 강우 영상을 예측하는 방법으로 이어진다. RainUNet은 해상도와 관측 방식이 다른 위성 자료와 지상 레이더 강우 영상을 연결하는 예측 문제를 다룬다. 생태 연구는 자동 촬영 영상에서 야생동물의 종을 구별하고 개체 수를 분석하는 데 초점을 맞춘다. 최근 과제에는 생성형 AI의 안전성 평가, 기상·생태 분석, 디지털트윈(실제 대상의 관측 정보와 연결해 그 상태를 나타내는 디지털 모형) 생성 등이 함께 올라 있다.[^p7][^climate][^projects]

## 대표 논문

AI 안전성, 영상·복합 자료 이해와 계산 효율, 입체 생성, 기상 예측을 고르게 보여 주는 7편이다. arXiv에 공개된 판본 6편과 학회 아카이브의 논문 1편을 표시했다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·판본 | 쉽게 말하면 | 김창익의 저자 위치 |
|---|---|---|---|---|
| 1 | 2026 | [Jailbreak to Protect: Buffering and Reinforcing via Temporary Jailbreaking for Safe Fine-Tuning in Large Language Models](https://arxiv.org/abs/2605.24550) · arXiv 판 | 언어 모델을 개인화하는 추가 학습이 안전한 응답을 약화시키는 문제를 다룬다. 학습 중 유해한 변화를 줄이고, 학습 후에는 안전한 거절 동작을 강화하는 두 부분의 방법을 제안했다. 사용자 과제의 성능을 유지하면서 안전성을 높이는 결과를 보고했고, 사용자의 추가 학습 중 별도의 안전성 자료를 요구하지 않는다.[^p1] | 전체 4명 중 마지막 |
| 2 | 2022 | [Improving the Transferability of Targeted Adversarial Examples through Object-Based Diverse Input](https://arxiv.org/abs/2203.09123) · arXiv 판 | 한 영상 모델에서 만든 공격 입력이 다른 모델에서도 목표한 오분류를 일으키게 하는 방법이다. 입체 물체에 공격 영상을 입혀 여러 관측 조건의 입력으로 바꾸는 ODI(Object-Based Diverse Input)를 제안했다. 실험에서 표적 공격의 전이 성공률을 높였고 얼굴 검증 과제에 대한 적용도 보였다.[^p2] | 전체 5명 중 마지막 |
| 3 | 2025 | [Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling](https://arxiv.org/abs/2511.16301) · arXiv 판 | 영상 모델이 만든 낮은 해상도의 정보를 입력 영상마다 복원 규칙을 찾아 위치별 고해상도 출력으로 복원한다. 자료집합 전체를 새로 학습할 필요 없이 경계를 고려한 복원 규칙을 얻으며, 특징 지도뿐 아니라 거리와 확률을 나타낸 지도에도 적용한다. 영상 분할과 깊이 추정 등의 실험으로 방법을 평가했다.[^p3] | 전체 3명 중 마지막 |
| 4 | 2024 | [VideoMamba: Spatio-Temporal Selective State Space Model](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3565_ECCV_2024_paper.php) · ECCV | 동영상의 공간 정보와 시간 순서를 함께 처리하도록 Mamba 구조를 바꿨다. 앞뒤 방향의 정보를 처리하는 선택적 상태 공간 모델로 영상 안의 관계와 멀리 떨어진 시점 사이의 관계를 학습한다. 여러 동영상 이해 과제에서 인식 성능과 계산 자원 사용을 평가했다.[^p4] | 전체 5명 중 마지막 |
| 5 | 2026 | [Multimodal Self-Attention Network with Temporal Alignment for Audio-Visual Emotion Recognition](https://arxiv.org/abs/2603.11095) · arXiv 판 | 소리와 영상을 함께 써 감정을 인식할 때 두 자료의 관측 속도가 다른 문제를 다룬다. 자료 내부와 자료 사이의 관계를 함께 학습하는 구조에 시간 정렬 방법과 시간상 가까운 자료를 맞추는 학습 목표를 더했다. 두 공개 자료집에서 비교 방법 대비 개선을 보고했다.[^p5] | 전체 5명 중 마지막 |
| 6 | 2023 | [HarmonyView: Harmonizing Consistency and Diversity in One-Image-to-3D](https://arxiv.org/abs/2312.15980) · arXiv 판 | 한 장의 사진을 입체로 바꾸면 보이지 않은 부분에 여러 모양이 가능하다. 여러 방향의 모습이 서로 맞는 성질과 다양한 모양을 만드는 성질을 함께 다루는 생성 방법을 제안했다. 생성 과정에서 두 성질을 구분해 조절하며, 생성된 모습의 다양성을 평가하는 기준도 제안했다.[^p6] | 전체 5명 중 마지막 |
| 7 | 2022 | [RainUNet for Super-Resolution Rain Movie Prediction under Spatio-temporal Shifts](https://arxiv.org/abs/2212.04005) · arXiv 판 | 해상도가 낮은 위성영상으로 지상 레이더가 관측하는 고해상도 강우의 미래 모습을 예측한다. 자료를 전처리한 뒤 공간과 시간 정보를 처리하는 새 RainUNet으로 강우 영상을 만든다. 여러 평가 기준에서 기본 비교 방법보다 개선된 예측을 보고했다.[^p7] | 전체 5명 중 마지막 |

## 교수와 전문 분야

김창익 교수는 연세대학교 전기공학 학사, POSTECH 전자·전기공학 석사, 미국 University of Washington 전기공학 박사 학위를 받았다. 랩의 경력 소개는 2009년 3월 KAIST 전기및전자공학과 부교수, 2014년 9월 이후 전기및전자공학부 교수로 적는다. 현재 소개에는 KAIST 교수평의회 의장과 안보과학기술대학원 원장도 올라 있다.[^prof]

공개 연구 관심은 딥러닝과 최적화(목적과 제약에 맞는 해를 찾는 방법), 영상 분석, 패턴 인식(자료에서 반복되는 특징을 바탕으로 대상을 구분하는 기술), 적은 자료를 쓰는 학습, 설명 가능한 AI와 적대적 공격·방어, 기후 AI다. 대표 논문에서 드러나는 전문 분야는 모델의 공격 취약성과 안전한 학습, 영상 정보를 효율적으로 처리하는 구조, 소리와 영상의 결합, 사진을 이용한 입체 생성, 위성영상 기반 강우 예측이다.[^prof][^p1][^p2][^p3][^p4][^p5][^p6][^p7]

전기및전자공학부 교수 소개는 AI·기계학습, 멀티미디어 신호처리와 보안을 주요 분야로 적고, 안보과학기술대학원 명단도 소속학과를 전기및전자공학부로 적는다. 녹색성장지속가능대학원은 겸임교수 명단에 컴퓨터 비전, 인공지능, 생태·기상 AI를 연구하는 교수로 소개한다. 랩의 교수 소개에는 Department of AI & Futures Studies의 Professor도 함께 적혀 있다.[^ee][^gst][^gggs][^prof]

학술 활동으로는 IEEE Transactions on Circuits and Systems for Video Technology 부편집장(2025년 11월 이후), IET Computer Vision 부편집장(2022년), ICIP 2022–2026 분야위원장, VCIP 2021·2022 분야위원장, AVSS 2023 튜토리얼위원장과 ICME 2026 산업 프로그램·전시위원장이 게시되어 있다.[^prof]

## 응용 분야

행동 인식은 영상과 움직임 센서 자료를 쓰는 안전·보안 시스템, 일부 자료가 없는 환경의 인식에 연결된다. 입체 시각은 자율주행과 로봇 이동, 증강·가상현실을 대상으로 한다. AI 안전성 연구는 영상 인식 모델과 개인화된 언어 모델의 공격·오용을 다루며, 기상·생태 연구는 강우 예측과 야생동물 분석을 대상으로 한다. 과제 목록에는 분산 카메라의 화물 탐지·추적, 디지털 휴먼 생성, 무인잠수정 군집 운용, 허위정보 탐지와 온디바이스 AI(기기 안에서 인공지능 계산을 수행하는 방식)도 포함된다.[^action][^three][^p1][^climate][^projects]

## 구성원

2026년 10월 31일 랩의 Ph.D·MS 명단에 올라 있는 학생 33명이다. 박사 명단 26명 중 9명은 Part-time 구획에 있으며, 석사 명단은 7명이다. 과정은 명단의 구획을 옮겼다. ‘대표 논문 참여’는 위 표의 번호이며, 전체 저자 목록에서 같은 이름을 확인한 경우 같은 사람으로 보아 표시했다.[^phd][^ms]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Minseok Son | 박사과정 | 5, 7 |
| Seho Kim | 박사과정 |  |
| Jaehyuk Jang | 박사과정 | 1, 5 |
| Jinyoung Park | 박사과정 | 4, 7 |
| Kangwook Ko | 박사과정 | 4 |
| Hee-Seon Kim | 박사과정 | 2, 4 |
| Seokil Ham | 박사과정 | 1 |
| Minbeom Kim | 박사과정 | 4 |
| Wonjun Lee | 박사과정 | 1 |
| Chaehee Song | 박사과정 |  |
| Doyi Kim | 박사과정 |  |
| Minseok Seo | 박사과정 | 3 |
| Younghun Kim | 박사과정 |  |
| Yeeun Seong | 박사과정 | 5 |
| Yubin Choi | 박사과정 |  |
| YuJin Yang | 박사과정 |  |
| Yejin Lee | 박사과정 |  |
| Seungjun Lee | 박사과정 (Part-time) |  |
| Soyeong Jeon | 박사과정 (Part-time) |  |
| Taewon Kim | 박사과정 (Part-time) |  |
| Sungun Park | 박사과정 (Part-time) |  |
| Hyesun Jeong | 박사과정 (Part-time) |  |
| Je-Seok Ham | 박사과정 (Part-time) |  |
| Hoyoung Yoo | 박사과정 (Part-time) |  |
| Chungjae Choe | 박사과정 (Part-time) |  |
| Jae-Hyuck Park | 박사과정 (Part-time) |  |
| Kim ki hyun | 석사과정 |  |
| Minsuk Jang | 석사과정 |  |
| Minho Kim | 석사과정 |  |
| Jihyun Lee | 석사과정 |  |
| Kihyun Seol | 석사과정 |  |
| Yeongeun Shim | 석사과정 |  |
| Seungyeon Sa | 석사과정 |  |

## 졸업생과 이전 구성원

랩 Alumni 명단의 72명이다. 학위·과정과 연도는 랩이 적은 표기이며 2006–2026년을 포괄한다. 같은 사람에게 석사·박사·박사후 경력이 함께 적힌 경우 한 행에 모았다. 진로는 랩이 적은 기관·직무이고, 빈칸은 명단에 진로가 적혀 있지 않은 경우다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jungwoo Park | (M.S.   2006) | Samsung Electronics |
| Keewon Seo | (M.S.   2006) | NC Soft |
| Muhammad Usman | (M.S.   2008) | 3D Software Engineering in Arbisoft |
| Youngwoo Kim | (M.S.   2009) | 한국생산기술연구원 (KITECH) |
| Muhammad Abul Hasan | (M.S.   2009) | University of Technology, Sydney |
| Jaeseung Ko | (M.S.   2009) | LG Home Entertainment |
| Beomjoon Kim | (M.S.   2010) | Samsung Electronics |
| Jimin Park | (M.S.   2010) | Samsung Research |
| Minjin Kim | (M.S.   2011) | Samsung Electronics |
| Daeyoung Oh | (M.S.   2011) | Siliconworks |
| Jaekwang Kim | (M.S.   2012) | VUERON |
| Wonjun Kim | (M.S.   2008); (Ph.D. 2012) | Konkuk University |
| Chanho Jung | (Ph.D. 2013) | Hanbat National University |
| Dongjin Park | (M.S.   2013) | Samsung Electronics (System LSI) |
| Seungwoo Yoo | (M.S.   2013) | Qualcomm Korea |
| Jaeho Lee | (M.S.   2008); (Ph.D. 2014) | Hyundai Motor Company |
| Changhwan Chun | (M.S.   2014) | VUERON |
| IlKoo Ahn | (M.S.   2008); (Ph.D. 2014); (Post doc.  2015) | 한의학 연구원 |
| Jiwon Choi | (M.S. / Ph.D.  2015) | Samsung Electronics (System LSI) |
| NaKyoung Oh | (M.S.   2015) | 의학전문대학원 |
| Taeksun Kim | (M.S.   2015) | Samsung Electronics (System LSI) |
| Tran Duc Nhan | (M.S.   2015) | Accenture, UK |
| Joonhyang Choi | (M.S.   2016) | SKTelecom (SKT) |
| HeeKwang Kang | (M.S.   2017) | Samsung Electronics |
| Kyungchul Wee | (M.S.   2017) | 국방과학연구소 (ADD) |
| Jongmo Kim | (M.S.   2017) | Hyundai Motor Company |
| Jinsu Kim | (M.S. 2017) | SK Hynix |
| Daeyoung Kim | (Ph.D.   2018) | Samsung Research |
| Hangyeol Lee | (M.S.   2018) | LG Display |
| Hyunjun Eun | (Ph.D.   2020) | SKTelecom (SKT) |
| Hyukzae Lee | (Ph.D.   2020) | Hyundai Motor Company |
| Seungyoun Lee | (Ph.D.   2020) | 국방과학연구소 (ADD) |
| Jaehoon Choi | (M.S. 2020) | University of Maryland |
| Youngeun Kim | (M.S. 2020) | Yale University |
| Jonghee Kim | (Ph.D. 2021) | 한국전자통신연구원 (ETRI) |
| Seunghyeon Kim | (M.S. 2021) | TmaxSoft |
| Seunghan Yang | (M.S. 2021) | Qualcomm Korea |
| Juri Jung | (M.S. 2021) | LG Electronics |
| Hyoungseob Park | (M.S. 2021) | Yale University |
| Dongki Jung | (M.S. 2021) | NAVER LABS |
| Jieun Ko | (M.S. 2021) | Samsung Electronics (System LSI) |
| Yoonhyung Kim | (Ph.D. 2021) | 한국전자통신연구원 (ETRI) |
| Seokeon Choi | (Ph.D. 2021) | Qualcomm Korea |
| Sangbum Choi | (M.S. 2021) | Superb AI |
| Keunchul Park | (M.S. 2021) | Riiid |
| Taekyung Kim | (Ph.D. 2021) | NAVER CLOVA |
| Hyojun Go | (M.S. 2022) | Riiid |
| Sungjoon Yoon | (M.S. 2022) | KLleon |
| Sangwoo Seo | (M.S. 2022) |  |
| Jeongsoo Kim | (M.S. 2022) | Korea Military Academy |
| Kibum Yun | (M.S. 2022) | Korea Telecom (KT) |
| Minki Jeong | (Ph.D. 2023) | 삼성종합기술원 |
| Yeonju Park | (M.S. 2023) | Korea Telecom (KT) |
| Yoonji Kim | (M.S. 2023) | Hyundai Motor Company |
| Junyoung Byun | (Ph.D. 2023) | 삼성종합기술원 |
| Minji Son | (M.S. 2023) | Samsung Research |
| Kangil Lee | (Ph.D.   2024) | 국방과학연구소 (ADD) |
| Jubi Hwang | (M.S.   2024) | 현대자동차 남양연구소 |
| Inyoung Lee | (M.S.   2024) | 라이드플럭스 (RideFlux) |
| Woojin Jeon | (M.S.   2024) |  |
| Sumin Lee | (Ph.D.   2024) | 삼성종합기술원 (SAIT) |
| Yooseung Wang | (M.S.   2024) | 한국전자기술연구원 (KETI) |
| Youngjun Kwak | (Ph.D.   2024) | 카카오뱅크 금융기술연구소 |
| Muhammad Adi Nugroho | (Ph.D.   2025) |  |
| Kyujin Shim | (Ph.D.   2025) | Samsung Research |
| Hongsin Lee | (M.S.   2025) |  |
| Donguk Kim | (M.S.   2025) | LG CNS |
| Seungju Cho | (Ph.D.   2025) | 삼성전자 S.LSI |
| Byeongjun Park | (Ph.D.  2025) | EverEx |
| Sangmin Woo | (Ph.D.  2025) | Amazon Web Service |
| MyungJoon Kwon | (Ph.D.  2026) | Samsung Research |
| Inyong Koo | (Ph.D. 2025, Postdoc 2026) | 삼성전자 DX |

## 최근 논문 목록 (2021–2026)

국제 학술지 16편, 국제 학회 70편, 국내 학술지 3편, 국내 학회 28편을 합친 117편이다. 영상 인식·생성, AI 안전성, 복합 자료 처리와 기상·생태 분석을 다룬다. 제목·저자·발표처는 연구실 표기이며 연도는 항목에 적힌 날짜를 따른다. 동일 제목으로 반복된 국제 학술지 항목은 한 번 표시했다. 2021년은 10월 13일 이후의 항목을 싣는다. 연구실 소식에서 채택을 확인한 WordEval과 EMNLP 2026의 다섯 항목은 ‘채택’으로 표시했다.[^publications][^ij][^ic][^dj][^dc][^home]

**2026**

- Jeseok Ham, J. Huang, P. Jiang, J. Moon, Y. Kwon, S. Saripalli and Changick Kim. "Multimodal Understanding with GPT-4o to Enhance Generalizable Pedestrian Behavior Prediction". *Computers and Electrical Engineering, vol. 129, Part A, no.110741, Jan. 2026*.
- Jinyoung Park\*, Y. Huang\*, S.Zhang, J. Ding, Y. Jia, Y. Zhao, T. Lv, W. Wu, S. Huang, N. Yang, X. Zhou, D. Zhang, L. Dong, L. Cui, S. Mao, X. Wang, T. Ge, H. Jiao, S. Chen, Changick Kim†, and F. Wei†. "WordEval: Evaluating Word-Native Operation Fidelity in Document Editing". *in Proc. Neural Information Processing Systems (NeurIPS), 2026. (\* These two authors contributed equally, † These two authors are co-corresponding authors) (채택)*.
- Je-Seok Ham, H. Lee, Y. Lee, K. Park, J. Moon, and Changick Kim. "Infrastructure-Assisted Defensive Forecasting of Latent Traffic Hazards from Uncalibrated CCTV". *in Proc. IEEE/CVF European Conference on Computer Vision Workshop (ECCVW), Malmö, Sweden, Sep. 8-12, 2026*.
- H.Cho, S.Yoo, Jaehyuk Jang, Changick Kim and J. Chung. "Who Wins the Conflict? Mechanistic Interpretability of Text Bias in Audio LLMs". *in Proc. the Empirical Methods in Natural Language Processing (EMNLP), 2026 (채택)*.
- Kangwook Ko\*, Jaehyuk Jang\*, Wonjun Lee\*, Hee-Seon Kim and Changick Kim. "Where Identity Lives: Localized, Retain-Free Identity Unlearning in Multimodal Large Language Models". *in Proc. the Empirical Methods in Natural Language Processing (EMNLP) Findings, 2026. (\* These three authors contributed equally) (채택)*.
- Wonjun Lee\*, Jaehyuk Jang\*, Kangwook Ko\*, Hee-Seon Kim and Changick Kim. "AIM: Anchor Identity Features, then Match for Multimodal Large Language Model Unlearning". *in Proc. the Empirical Methods in Natural Language Processing (EMNLP) Findings, 2026. (\* These three authors contributed equally) (채택)*.
- Jaehyuk Jang, Kangwook Ko, Wonjun Lee and Changick Kim. "SubT: Subspace Tuning for Few-shot Generalization of Audio-Language Models". *in Proc. the Empirical Methods in Natural Language Processing (EMNLP) Findings, 2026 (채택)*.
- Minsuk Jang\*, Hee-Seon Kim\*, H. Yu\*, and Changick Kim. "MATE: Mobile Agent Trustworthy Execution for Safe and Efficient Mobile Control". *in Proc. the Empirical Methods in Natural Language Processing (EMNLP) Findings, 2026. (\* These three authors contributed equally) (채택)*.
- Yeeun Seong\*, Doyi Kim\*, Minseok Seo, and Changick Kim. "RainODE: Continuous-Time Precipitation Forecasting with Latent Neural ODEs". *in Proc. IEEE/CVF European Conference on Computer Vision (ECCV), Malmö, Sweden, Sep. 8-12, 2026. (\* These two authors contributed equally)*.
- H. Cho, Jaehyuk Jang, Changick Kim†, and J. S. Chung†. "Acoustic Prompting via Stage-wise Modulation for Few-Shot Learning in Audio Language Models". *in Proc. Interspeech, 2026. († These two authors are co-corresponding authors)*.
- Seokil Ham, Jaehyuk Jang, Wonjun Lee, and Changick Kim. "Jailbreak to Protect: Buffering Harmful Fine-Tuning via Temporary Jailbreaking LoRA in Large Language Models". *in Proc. the International Conference on Machine Learning (ICML), Seoul, South Korea, Jul. 6-11, 2026*.
- Jinyoung Park, Minseok Son, and Changick Kim. "Towards Efficient Vision State Space Models via Token Merging". *in Proc. IEEE International Conference on Image Processing (ICIP), Tampere, Finland, Sep. 13-17, 2026*.
- Yubin Choi\*, Yujin Yang\*, S. Kim\*, Seokil Ham, Seungju Cho, J. Son, Youngjun Kwak, and Changick Kim. "FinHarmBench: Financial Jailbreak Benchmark and Unsupervised Safety Fine-Tuning via Refusal Steering Distillation". *in Proc. the Annual Meeting of the Association for Computational Linguistics (ACL) Industry Track, San Diego, California, USA, Jul. 2-7, 2026. (\* These three authors contributed equally)*.
- Jaehyuk Jang\*, Wonjun Lee\*, Kangwook Ko\*, and Changick Kim. "Generalizable Prompt Tuning for Audio-Language Models via Semantic Expansion". *in Proc. the Annual Meeting of the Association for Computational Linguistics (ACL) Findings, San Diego, California, USA, Jul. 2-7, 2026. (\* These three authors contributed equally)*.
- Minseok Seo, M. Hamilton, and Changick Kim. "Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling". *in Proc. the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Denver, Colorado, USA, Jun. 3-7, 2026*.
- Doyi Kim, Minseok Seo, and Changick Kim. "Station2Radar: Query‑Conditioned Gaussian Splatting for Precipitation Field". *in International Conference on Learning Representations (ICLR), Rio de Janeiro, Brazil, Apr. 23-27, 2026*.
- Doyi Kim, J. Ahn, H. McJeon and Changick Kim. "Efficiency vs Demand in AI Electricity: Implications for Post-AGI Scaling". *in International Conference on Learning Representations Workshop (ICLRW), Rio de Janeiro, Brazil, Apr. 23-27, 2026*.
- Inyong Koo, Yeeun Seong, Minseok Son, Jaehyuk Jang, and Changick Kim. "Multimodal Self-Attention Network with Temporal Alignment for Audio-Viusal Emotion Recognition". *in Proc. the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), Barcelona, Spain, May 4-8, 2026*.

**2025**

- Sumin Lee, Sangmin Woo, Muhammad Adi Nugroho, and Changick Kim. "Modality mixer exploiting complementary information for multi-modal action recognition". *Computer Vision and Image Understanding, vol. 256, pp.104358, May. 2025*.
- Hyojun Go\*, Byeongjun Park\*, H. Nam, B. Kim, H. Chung, and Changick Kim. "VideoRFSplat: Direct Scene-Level Text-to-3D Gaussian Splatting Generation with Flexible Pose and Multi-View Joint Modeling". *in Proc. IEEE/CVF International Conference on Computer Vision (ICCV), Honolulu, Hawaii, Oct. 19-23, 2025. (\* These two authors contributed equally)*.
- Byeongjun Park\*, Hyojun Go\*, H. Nam, B. Kim, H. Chung, and Changick Kim. "SteerX: Creating Any Camera-Free 3D and 4D Scenes with Geometric Steering". *in Proc. IEEE/CVF International Conference on Computer Vision (ICCV), Honolulu, Hawaii, Oct. 19-23, 2025. (\* These two authors contributed equally)*.
- Sangmin Woo\*, Donguk Kim\*, Jaehyuk Jang\*, Yubin Choi, and Changick Kim. "Don't Miss the Forest for the Trees: Attentional Vision Calibration for Large Vision Language Models". *in Proc. the Annual Meeting of the Association for Computational Linguistics (ACL) Findings, Vienna, Austria, Jul. 27 - Aug. 1, 2025. (\* These three authors contributed equally)*.
- Hyojun Go\*, Byeongjun Park\*, J. Jang, J. Kim, S. Kwon, and Changick Kim. "SplatFlow: Multi-View Rectified Flow Model for 3D Gaussian Splatting Synthesis". *in Proc. the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Nashville, USA, Jun. 17-21, 2025. (\* These two authors contributed equally)*.
- Seokil Ham, Hee-Seon Kim, Sangmin Woo, and Changick Kim. "Parameter Efficient Mamba Tuning via Projector-targeted Diagonal-centric Linear Transformation". *in Proc. the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Nashville, USA, Jun. 17-21, 2025*.
- Kyujin Shim, Kangwook Ko, YuJin Yang, and Changick Kim. "Focusing on Tracks for Online Multi-Object Tracking". *in Proc. the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Nashville, USA, Jun. 17-21, 2025*.
- Hongsin Lee\*, Seungju Cho\*, and Changick Kim. "Indirect Gradient Matching for Adversarial Robust Distillation". *in International Conference on Learning Representations (ICLR), Singapore, Apr. 24-28, 2025. (\* These two authors contributed equally)*.
- Seungju Cho\*, Hongsin Lee\*, and Changick Kim. "Long-tailed Adversarial Training with Self-Distillation". *in International Conference on Learning Representations (ICLR), Singapore, Apr. 24-28, 2025. (\* These two authors contributed equally)*.
- Myung-Joon Kwon\*, Wonjun Lee\*, SH Nam, Minji Son, and Changick Kim. "SAFIRE: Segment Any Forged Image Region". *in Proc. the AAAI conference on artificial intelligence (AAAI), Philadelphia, USA, Feb. 25 - Mar. 4, 2025. (\* These two authors contributed equally)*.
- Seokil Ham\*, Sangmin Woo\*, J.-Y. Kim, Hyojun Go, Byeongjun Park, and Changick Kim. "Diffusion Model Patching via Mixture-of-Prompts". *in Proc. the AAAI conference on artificial intelligence (AAAI), Philadelphia, USA, Feb. 25 - Mar. 4, 2025. (\* These two authors contributed equally)*.
- Seungju Cho\*, Hongsin Lee\*, and Changick Kim. "Enhancing Robustness in Incremental Learning with Adversarial Training". *in Proc. the AAAI conference on artificial intelligence (AAAI), Philadelphia, USA, Feb. 25 - Mar. 4, 2025. (\* These two authors contributed equally)*.
- Minseok Son\*, Inyong Koo\*, Jinyoung Park, and Changick Kim. "Difficulty-aware Balancing Margin Loss for Long-tailed Recognition". *in Proc. the AAAI conference on artificial intelligence (AAAI), Philadelphia, USA, Feb. 25 - Mar. 4, 2025. (\* These two authors contributed equally)*.
- 최유빈, 함석일, 조승주, 김창익. "거절 벡터 정렬 기반 Llama-Guard 미세조정을 통한 LLM 안전성 강화". *대한전자공학회 하계학술대회, Jun. 24-27, 2025*.
- 김기현, 김희선, 김민범, 이원준, 김창익. "안전 경계를 활용한 이미지 기반 Universal Jailbreak 공격". *대한전자공학회 하계학술대회, Jun. 24-27, 2025*.
- 양유진, 고강욱, 김창익. "푸앵카레 임베딩을 이용한 하이퍼볼릭 공간 기반 사람 재식별". *대한전자공학회 하계학술대회, Jun. 24-27, 2025*.
- 김영헌, 김창익. "딥페이크 탐지 모델이 특정 기술에 과도하게 집중하는 문제 완화를 위한 학습 프레임워크". *대한전자공학회 하계학술대회, Jun. 24-27, 2025*.
- 장민석, 김영헌, 박병준, 김창익. "뉴로모픽 컴퓨팅 기반 스파이킹 토큰화를 활용한 경량 비전 트랜스포머 인코더 설계". *대한전자공학회 하계학술대회, Jun. 24-27, 2025*.
- 성예은, 박진영, 김창익. "약지도 군중행동 인식을 위한 시간 및 공간 표현의 분리 학습". *한국군사과학기술학회 종합학술대회, Jun. 11-13, 2025*.
- 박진영, 성예은, 김창익. "태스크 적응형 전문가를 활용한 군중 행동 인식". *한국군사과학기술학회 종합학술대회, Jun. 11-13, 2025*.

**2024**

- Kyujin Shim, Junyoung Byun, Kangwook Ko, Jubi Hwang, and Changick Kim. "Enhancing Robustness of Multi-Object Trackers with Temporal Feature Mix". *IEEE Transactions on Circuits and Systems for Video Technology (TCSVT), vol. 34, no.10, pp.9822-9835, Oct. 2024*.
- Byeongjun Park\*, Hyojun Go\*, and Changick Kim. "Bridging Implicit and Explicit Geometric Transformation for Single-Image View Synthesis". *IEEE Transaction on Pattern Analysis and Machine Intelligence (TPAMI), vol. 46, no. 9, pp.6326-6340, Sep. 2024. (\* These two authors contributed equally)*.
- Jaehyuk Jang, Yooseung Wang, and Changick Kim. "FCGNet: Foreground and Class Guided Network for Human Parsing". *Pattern Recognition, vol. 157, pp.110879, Aug. 2024*.
- Yooseung Wang, Jaehyuk Jang, and Changick Kim. "Subdivided Mask Dispersion Framework for Semi-Supervised Semantic Segmentation". *Pattern Recognition Letters, vol. 179, pp. 58-64, Jan. 2024*.
- Kangil Lee and Changick Kim. "A Gyro-based Tracking Assistant for Drones with Uncooled Infrared Camera". *IEEE Sensors, vol. 24, no. 1, pp. 645-659, Jan. 2024*.
- Muhammad Adi Nugroho, Jinyoung Park, Donguk Kim, and Changick Kim. "Anchoring Vision and Language Knowledge for Weakly Supervised Group Activity Recognition". *in IEEE International Conference on Visual Communications and Image Processing (VCIP), Tokyo, Japan, Dec. 8-11, 2024*.
- Younghun Kim, Myung-Joon Kwon, Wonjun Lee, and Changick Kim. "FRIDAY: Mitigating Unintentional Facial Identity in Deepfake Detectors Gudided by Facial Recognizers". *in IEEE International Conference on Visual Communications and Image Processing (VCIP), Tokyo, Japan, Dec. 8-11, 2024*.
- Jeseok Ham, J. Huang, P. Jiang, J. Moon, Y. Kwon, S. Saripalli,  and Changick Kim. "OmniPredict: GPT-4o Enhanced Multi-modal Pedestrian Crossing Intention Prediction". *in Proc. the 38th Annual Conference on Neural Information Processing Systems Workshop (NeurIPSW), Vancouver, Canada, Dec. 10-15, 2024*.
- Jeseok Ham, S. Kim, J. Huang, P. Jiang, J. Moon, S. Saripalli, and Changick Kim. "LLaMAPed: Multi-modal Pedestrian Crossing Intention Prediction". *in Proc. IEEE/CVF European Conference on Computer Vision Workshops (ECCVW), Milano, Italy, Sep. 29 - Oct. 04, 2024*.
- Byeongjun Park, Hyojun Go, Jin-Young Kim, Sangmin Woo, Seokil Ham, and Changick Kim. "Switch Diffusion Transformer: Synergizing Denoising Tasks with Sparse Mixture-of-Experts". *in Proc. IEEE/CVF European Conference on Computer Vision (ECCV), Milano, Italy, Sep. 29 - Oct. 04, 2024*.
- Jinyoung Park\*, Hee-Seon Kim\*, Kangwook Ko\*, Minbeom Kim, and Changick Kim. "VideoMamba: Spatio-Temporal Selective State Space Model". *in Proc. IEEE/CVF European Conference on Computer Vision (ECCV), Milano, Italy, Sep. 29 - Oct. 04, 2024. (\* These three authors contributed equally)*.
- Muhammad Adi Nugroho, Sangmin Woo, Sumin Lee, Jinyoung Park, Yooseung Wang, Donguk Kim, and Changick Kim. "Flow-Assisted Motion Learning Network for Weakly-Supervised Group Activity Recognition". *in Proc. IEEE/CVF European Conference on Computer Vision (ECCV), Milano, Italy, Sep. 29 - Oct. 04, 2024*.
- Sumin Lee, Yooseung Wang, Sangmin Woo, and Changick Kim. "Spatio-Temporal Proximity-Aware Dual-Path Model for Panoramic Activity Recognition". *in Proc. IEEE/CVF European Conference on Computer Vision (ECCV), Milano, Italy, Sep. 29 - Oct. 04, 2024*.
- Kyujin Shim, Jubi Hwang, Kangwook Ko, and Changick Kim. "A Confidence-Aware Matching Strategy For Generalized Multi-Object Tracking". *IEEE International Conference on Image Processing (ICIP), Abu Dhabi, United Arab Emirates, Oct. 2024*.
- Kyujin Shim, Kangwook Ko, Jubi Hwang, and Changick Kim. "AdapTrack: Adaptive Thresholding-Based Matching For Multi-Object Tracking". *IEEE International Conference on Image Processing (ICIP), Abu Dhabi, United Arab Emirates, Oct. 2024*.
- Sangmin Woo\*, Byeongjun Park\*, H. Go, J. Kim and Changick Kim. "HarmonyView: Harmonizing Consistency and Diversity in One-Image-to-3D". *in Proc. the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Seattle, USA, Jun. 17-21, 2024*.
- Byeongjun Park\*, Sangmin Woo\*, H. Go\*, J. Kim\* and Changick Kim. "Denoising Task Routing for Diffusion Models". *in International Conference on Learning Representations (ICLR), Vienna, Austria, May. 7-11, 2024*.
- Jaehyuk Jang, Yooseung Wang, and Changick Kim. "TOWARDS ROBUST MULTIMODAL PROMPTING WITH MISSING MODALITIES". *in Proc. the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), Seoul, Korea, Apr. 14-19, 2024*.
- Sangmin Woo, So-Yeong Jeon, Jinyoung Park, Minji Son, Sumin Lee, and Changick Kim. "Sketch-based Video Object Localization". *in Proc. the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), Hawaii, USA, Jan. 4-6, 2024*.
- Byeongjun Park and Changick Kim. "Point-DynRF: Point-based Dynamic Radiance Fields from a Monocular Video". *in Proc. the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), Hawaii, USA, Jan. 4-6, 2024*.
- 이원준, 권명준, 김영헌, 김창익. "편향과의 전투: 적대적 훈련을 통한 신경망 모델 교정". *대한전자공학회 하계학술대회, 롯데호텔 제주, Jun. 26-28, 2024*.
- 김영헌, 권명준, 이원준, 김창익. "부분적 이미지 조작 증강 기법을 통한 딥페이크 탐지 일반화 성능 향상". *대한전자공학회 하계학술대회, 롯데호텔 제주, Jun. 26-28, 2024*.
- 최유빈, 김동욱, 우상민, 장재혁, 김창익. "대형 시각-언어 모델에서의 객체 환각 현상 완화를 위한 이미지 처리 필터 기반 대조 학습". *대한전자공학회 하계학술대회, 롯데호텔 제주, Jun. 26-28, 2024*.
- 권명준, 이원준, 김영헌, 김창익. "사전 학습된 모델의 앙상블을 통한 합성 영상 탐지의 일반화 능력 향상". *대한전자공학회 하계학술대회, 롯데호텔 제주, Jun. 26-28, 2024*.
- 성예은, 손민석, 구인용, 임정은, 김영민, 김창익. "야생동물 종 분류를 위한 손실 값 기반 로짓 조정 기법". *대한전자공학회 하계학술대회, 롯데호텔 제주, Jun. 26-28, 2024*.
- 양유진, 심규진, 고강욱, 김창익. "다중 물체 추적 기법들의 실제적 영향 비교 및 새로운 베이스라인 탐색". *대한전자공학회 하계학술대회, 롯데호텔 제주, Jun. 26-28, 2024*.
- 김동욱, 우상민, 장재혁, 최유빈, 김창익. "하이패스 필터링을 활용한 대형 비전 언어 모델의 환각 현상 완화". *대한전자공학회 하계학술대회, 롯데호텔 제주, Jun. 26-28, 2024*.

**2023**

- Yeonju Park, Sangmin Woo, Sumin Lee, Muhammad Adi Nugroho, and Changick Kim. "Cross-Modal Alignment and Translation for Missing Modality Action Recognition". *Computer Vision and Image Understanding, vol. 236, pp.103805, Aug. 2023*.
- Kangwook Ko, Kyujin Shim, Kangil Lee, and Changick Kim. "Large-scale Benchmark for Uncooled Infrared Image Deblurring". *IEEE Sensors, vol. 23, no. 24, pp. 30119-30128, Dec. 2023*.
- Kyujin Shim, Kangwook Ko, Jubi Hwang, H Jang, and Changick Kim. "Fast Online Multi-target Multi-camera Tracking for Vehicles". *Applied Intelligence (APIN), vol. 53, Oct. 2023*.
- Jubi Hwang, Kyujin Shim, Kangwook Ko, N. Ha, and Changick Kim. "Robust Multi-Object Tracking with Local Appearance and Stable Motion Models". *IEEE Access, vol. 11, pp. 77023-77033, Jul. 2023*.
- Inyong Koo, Yeonju Park, Minki Jeong, and Changick Kim. "Contrastive Accelerometer-Gyroscope Embedding Model for Human Activity Recognition". *IEEE Sensors, vol. 23, no. 1, pp. 506-513, Jan. 2023*.
- Sumin Lee, Hyunjun Eun, J. Moon, Seokeon Choi, Yoonhyung Kim, Chanho Jung, and Changick Kim. "Learning to Discriminate Information for Online Action Detection: Analysis and Application". *IEEE Transaction on Pattern Analysis and Machine Intelligence (TPAMI), vol. 45, no.5, pp. 5918-5934, 1 May 2023*.
- Yooseug Wang, Jaehyuk Jang, and Changick Kim. "Noise-Augmented Missing Modality Aware Prompt based Learning for Robust Visual Recognition". *in IEEE International Conference on Visual Communications and Image Processing (VCIP), Dec 4-7, 2023*.
- Muhammad Adi Nugroho, Sangmin Woo, Sumin Lee, and Changick Kim. "AHFu-Net: Align, Hallucinate, and Fuse Network for Missing Multimodal Action Recognition". *in IEEE International Conference on Visual Communications and Image Processing (VCIP), Dec 4-7, 2023*.
- Donguk Kim, Sumin Lee, Sangmin Woo, Jinyoung Park, Muhammad Adi Nugroho, and Changick Kim. "Multi-Modal Social Group Activity Recognition in Panoramic Scene". *IEEE International Conference on Visual Communications and Image Processing (VCIP), Dec 4-7, 2023*.
- Inyong Koo\*, Inyoung Lee\*, Se-Ho Kim, Hee-Seon Kim, Woo-jin Jeon, and Changick Kim. "PG-RCNN: Semantic Surface Point Generation for 3D Object Detection". *in Proc. IEEE/CVF International Conference on Computer Vision (ICCV), Paris, France, Oct. 02-06, 2023. (\* These two authors contributed equally)*.
- Hee-Seon Kim, Minji Son, Minbeom Kim, Myung-Joon Kwon, and Changick Kim. "Breaking Temporal Consistency: Generating Video Universal Adversarial Perturbations Using Image Models". *in Proc. IEEE/CVF International Conference on Computer Vision (ICCV), Paris, France, Oct. 02-06, 2023*.
- Muhammad Adi Nugroho, Sangmin Woo, Sumin Lee, and Changick Kim. "Audio-Visual Glance Network for Efficient Video Recognition". *in Proc. IEEE/CVF International Conference on Computer Vision (ICCV), Paris, France, Oct. 02-06, 2023*.
- H. Kim\*, Youngjun Kwak\*, M. Jung, J. Shin, Y. Kim, and Changick Kim. "ProtoFL: Unsupervised Federated Learning via Prototypical Distillation". *IEEE/CVF International Conference on Computer Vision (ICCV), 2023. (\* These two authors contributed equally)*.
- Yoonji Kim, Seungju Cho, Junyoung Byun, Myung-Joon Kwon, and  Changick Kim. "Improving Adversarial Transferability via Feature Translation". *Proc. the 29th IEEE International Conference on Image Processing (ICIP), Kuala Lumpur, Malaysia, Oct. 8-11, 2023*.
- Taekyung Kim, D. Das, Seokeon Choi, Minki Jeong, Seunghan Yang, S. Yun and Changick Kim. "Neural Transformation Network to Generate Diverse Views for Contrastive Learning". *in Proc. the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW), Vancouver, Canada, Jun. 18 - 22, 2023*.
- Junyoung Byun, Myung-Joon Kwon, Seungju Cho, Yoonji Kim, and Changick Kim. "Introducing Competition to Boost the Transferability of Targeted Adversarial Examples through Clean Feature Mixup". *in Proc. the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Vancouver, Canada, Jun. 18 - 22, 2023*.
- Youngjun Kwak, M. Jung, H. Yoo, J. Shin, Changick Kim. "Liveness Score-Based Regression Neural Networks for Face Anti-Spoofing". *Proc. the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), Rhodes Island, Greece, Jun. 4-10, 2023*.
- Sangmin Woo, Sumin Lee, Yeonju Park, Muhammad Adi Nugroho, and Changick Kim. "Towards Good Practices for Missing Modality Robust Action Recognition". *in Proc. the AAAI conference on artificial intelligence (AAAI), Washington, DC, USA, Feb. 7-14, 2023*.
- Sumin Lee, Sangmin Woo, Yeonju Park, Muhammad Adi Nugroho, and Changick Kim. "Modality Mixer for Multi-modal Action Recognition". *in Proc. the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), Hawaii, USA, Jan. 4-6, 2023*.
- 이수민, 김창익. "멀티모달 행동 인식을 위한 적대적 보강 학습 방법에 대한 연구". *한국군사과학기술학회 종합학술대회, 제주국제컨벤션센터(ICC) 제주, Jun. 15-16, 2023*.

**2022**

- Myung-Joon Kwon, S. Nam, I. Yu, H. Lee, and Changick Kim. "Learning JPEG Compression Artifacts for Image Manipulation Detection and Localization". *International Journal of Computer Vision (IJCV), vol. 130, no. 8, pp.1875-1895, Aug. 2022*.
- Kangil Lee, Y. Ban, and Changick Kim. "Motion Blur Kernel Rendering Using an Inertial Sensor: Interpreting the Mechanism of a Thermal Detector". *IEEE Sensors, vol. 22, no. 5, Feb. 2022*.
- Seunghan Yang, Hyoungseob Park, Junyoung Byun, and Changick Kim. "Robust Federated Learning with Noisy Labels". *IEEE Intelligent Systems, vol. 37, no. 2, pp.35-43, Feb. 2022*.
- 손민지, 권명준, 조승주, 김창익. "적대적 공격의 전이성 향상을 위한 이미지 왜곡 기법". *대한전자공학회논문지, Oct. 2022*.
- 김희선, 권명준, 변준영, 김창익. "카메라 시점 변환을 이용한 전이 기반 적대적 공격 기법". *대한전자공학회논문지, Jul. 2022*.
- 손민석, 권명준, 김윤지, 김창익. "얼굴 영상 분석을 위한 다중 모달 딥러닝 모델 연구". *한국통신학회지(정보와통신), 제 39권, 제 5호, pp. 60-66, Apr. 2022*.
- 고강욱, 박연주, 김윤지, 김희선, 심규진, 김창익. "거리두기 손실 함수를 통한 자기지도 대조 학습의 성능 향상". *대한전자공학회 하계학술대회, 제주신화월드 랜딩컨벤션센터 제주, Jun. 29- Jul. 1, 2022*.
- 김민범, 김희선, 변준영, 김창익. "이중 무작위 변환 기법을 통한 보편적 적대적 섭동의 전이성 향상". *대한전자공학회 하계학술대회, 제주신화월드 랜딩컨벤션센터 제주, Jun. 29- Jul. 1, 2022*.
- 전우진, 김윤지, 권명준, 김창익. "스테레오 깊이 추정 신경망에 대한 표적성 적대적 공격". *대한전자공학회 하계학술대회, 제주신화월드 랜딩컨벤션센터 제주, Jun. 29- Jul. 1, 2022*.
- 권명준, 손민지, 김윤지, 김창익. "적대적 취약성 다양화를 통한 적대적 전이성 향상". *대한전자공학회 하계학술대회, 제주신화월드 랜딩컨벤션센터 제주, Jun. 29- Jul. 1, 2022*.
- 황주비, 윤기범, 고강욱, 심규진, 조승연, 김창익. "도시 규모 교통 관리를 위한 다중 대상 다중 카메라 차량 추적 시스템". *대한전자공학회 하계학술대회, 제주신화월드 랜딩컨벤션센터 제주, Jun. 29- Jul. 1, 2022*.
- 김희선, 변준영, 손민지, 김창익. "혼합 이미지를 통한 보편적 적대적 섭동의 공격 성공률 향상". *대한전자공학회 하계학술대회, 제주신화월드 랜딩컨벤션센터 제주, Jun. 29- Jul. 1, 2022*.
- 손민지, 권명준, 김희선, 김창익. "생성 모델 기반 적대적 공격의 전이성 향상을 위한 구분 모델의 특성 지도 마스킹 방법". *대한전자공학회 하계학술대회, 제주신화월드 랜딩컨벤션센터 제주, Jun. 29- Jul. 01, 2022*.
- Jinyoung Park, Minseok Son, Seungju Cho, Inyoung Lee, and Changick Kim. "RainUNet for Super-Resolution Rain Movie Prediction under Spatio-temporal Shifts". *in Proc. the 36th Annual Conference on Neural Information Processing Systems Workshop (NeurIPSW), New Orleans, USA, Nov. 27 - Dec. 6, 2022*.
- Jinyoung Park, Inyoung Lee, Minseok Son, Seungju Cho, and Changick Kim. "Nowformer : A locally enhanced temporal learner for precipitation nowcasting". *in Proc. the 36th Annual Conference on Neural Information Processing Systems Workshop (NeurIPSW), New Orleans, USA, Nov. 27 - Dec. 6, 2022*.
- Jinyoung Park, Minseok Son, Sumin Lee, and Changick Kim. "DAT: DOMAIN ADAPTIVE TRANSFORMER FOR DOMAIN ADAPTIVE SEMANTIC SEGMENTATION". *in Proc. the 2 9 th IEEE International Conference on Image Processing (ICIP), Bordeaux, France, Oct. 16-19, 2022*.
- Kibum Yun, Kyujin Shim, Kangwook Ko, and Changick Kim. "DYNAMIC TEMPLATE UPDATE FOR VISUAL OBJECT TRACKING". *in Proc. the 29th IEEE International Conference on Image Processing (ICIP), Bordeaux, France, Oct. 16-19, 2022*.
- Jeongsoo Kim, Sangmin Woo, Byeongjun Park, and Changick Kim. "TEMPORAL FLOW MASK ATTENTION FOR OPEN-SET LONG-TAILED RECOGNITION OF WILD ANIMALS IN CAMERA-TRAP IMAGES". *in Proc. the 29th IEEE International Conference on Image Processing (ICIP), Bordeaux, France, Oct. 16-19, 2022*.
- Minji Son, Myung-Joon Kwon, Hee-Seon Kim, Junyoung Byun, Seungju Cho, and Changick Kim. "ADAPTIVE WARPING NETWORK FOR TRANSFERABLE ADVERSARIAL ATTACKS". *in Proc. the 29th IEEE International Conference on Image Processing (ICIP), Bordeaux, France, Oct. 16-19, 2022*.
- Seungju Cho, Junyoung Byun, Myung-Joon Kwon, Yoonji Kim, and Changick Kim. "ADVERSARIAL TRAINING WITH CHANNEL ATTENTION REGULARIZATION". *in Proc. the 29th IEEE International Conference on Image Processing (ICIP), Bordeaux, France, Oct. 16-19, 2022*.
- Junyoung Byun, Kyujin Shim, Hyojun Go, and Changick Kim. "HIDDEN CONDITIONAL ADVERSARIAL ATTACKS". *in Proc. the 29th EEE International Conference on Image Processing (ICIP), Bordeaux, France, Oct. 16-19, 2022*.
- Junyoung Byun, Hyojun Go, Seungju Cho, and Changick Kim. "EXPLOITING DOUBLY ADVERSARIAL EXAMPLES FOR IMPROVING ADVERSARIAL ROBUSTNESS". *in Proc. the 29th IEEE International Conference on Image Processing (ICIP), Bordeaux, France, Oct. 16-19, 2022*.
- Sangwoo Seo, Seungjun Jung, and Changick Kim. "Explanation-based Graph Neural Networks for Graph Classification". *in Proc. the 26th International Conference on Pattern Recognition (ICPR), Montreal Quebec, Canada, Aug. 21-25, 2022*.
- Junyoung Byun, Seungju Cho, Myung-Joon Kwon, Hee-Seon Kim, and Changick Kim. "Improving the Transferability of Targeted Adversarial Examples through Object-Based Diverse Input". *in IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Jun. 19-2 4, 202 2*.
- Junyoung Byun, Hyojun Go, and Changick Kim. "Geometrically Adaptive Dictionary Attack on Face Recognition". *in Proc. IEEE Winter Conference on Applications of Computer Vision (WACV), Waikoloa, HI, USA, Jan. 4-8, 2022*.
- Junyoung Byun, Hyojun Go, and Changick Kim. "On the Effectiveness of Small Input Noise for Defending Against Query-based Black-Box Attacks". *in Proc. IEEE Winter Conference on Applications of Computer Vision (WACV), Waikoloa, HI, USA, Jan. 4-8, 2022*.

**2021**

- 김윤지, 조승주, 권명준, 김창익. "픽셀 드랍을 이용한 레이블을 사용하지 않는 전이 기반 적대적 공격". *대한전자공학회 추계학술대회, 송도컨벤시아 인천, Nov. 26-27, 2021*.
- 고강욱, 심규진, 변준영, 김창익. "합성곱 신경망의 가중치 다변화를 통한 성능 향상". *대한전자공학회 추계학술대회, 송도컨벤시아 인천, Nov. 26-27, 2021*.
- 박연주, 구인용, 정민기, 김창익. "트랜스포머를 이용한 다종 센서 기반 행동 인식". *대한전자공학회 추계학술대회, 송도컨벤시아 인천, Nov. 26-27, 2021*.
- 김희선, 권명준, 변준영, 김창익. "원근 변환 기법을 통한 적대적 이미지의 전이성 향상". *대한전자공학회 추계학술대회, 송도컨벤시아 인천, Nov. 26-27, 2021*.
- 손민지, 권명준, 조승주, 김창익. "탄성변환을 이용한 적대적 예제의 전이성 향상". *대한전자공학회 추계학술대회, 송도컨벤시아 인천, Nov. 26-27, 2021*.
- 김정수, 박병준, 조승주, 최명애, 박진영, 서형수, 김창익. "트랩 카메라 영상 데이터셋을 활용한 옵티컬 플로우 퓨전 딥러닝 네트워크". *대한전자공학회 추계학술대회, 송도컨벤시아 인천, Nov. 26-27, 2021*.

## 과제

수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 35건이다. 과제명과 수행 기간은 연구실 표기이며, 시작이 이 범위보다 빠르거나 종료가 이 범위보다 늦은 과제도 포함한다.[^projects]

- 멀티모달 인공지능 기반 디지털트윈 모델 자동 생성 기술 개발 (기간 2026.04 ~ 2028.12)
- 멀티모달(이미지) 생성형 AI 안전성 평가기술 개발 (기간 2026.04 ~ 2026.12)
- 삼성전자전략산학과제 (기간 2025.09 ~ 2030.08)
- 온디바이스AI 사물간협력행동(인지, 판단, 대응) 핵심기술개발 (기간 2025.04 ~ 2028.12)
- 회복탄력성 있는 Multimodal Large Language Model (MLLM) 기술 연구 (기간 2025.01 ~ 2028.12)
- Video Adversarial Attack 고도화 (Universal adversarial perturbations) (기간 2024.01 ~ 2027.12)
- 기뢰탐지용 무인잠수정 군집 운용 기술 (기간 2024.07 ~ 2026.06)
- 미래국방 인공지능 특화연구센터 2단계 (기간 2023.05 ~ 2026.04)
- Efficiency Optimization for World Model (기간 2025.03 ~ 2026.03)
- 멀티모달 3D BEV 인식 성능 향상을 위한 자기지도 학습 기술개발 (기간 2025.03 ~ 2025.08)
- 챗봇 생성 허위정보 탐지 (기간 2025.03 ~ 2025.12)
- 인류세 연구센터 (CRC): Eco-AI (기간 2018.06 ~ 2025.02)
- Scene Text Recognition (기간 2024.02 ~ 2024.12)
- 교통영상내 객체 트래킹 (기간 2023.12 ~ 2024.12)
- Precise landing technology for drones (기간 2022.05 ~ 2024.12)
- AI 기반 분산카메라 환경 화물 탐지 및 추적 시스템 개발 (Development of AI-based cargo detection and tracking system on distributed multi-camera environment) (기간 2021.07 ~ 2024.12)
- 디지털 휴먼 생성 (Digital human creation) (기간 2021.04 ~ 2024.12)
- 야생동물 자동종동정 기법 고도화 연구 (기간 2024.07 ~ 2024.08)
- Self-supervised Learning of Multi-modal Representation for Autonomous Driving (기간 2023.12 ~ 2024.11)
- Video object detection (기간 2023.02 ~ 2023.12)
- Captcha(Completely Automated Public Turing test to tell Computers and Humans Apart) 기술 고도화 (기간 2023.02 ~ 2023.12)
- Adversarial Attack (4th year) (기간 2023.02 ~ 2023.12)
- 광역해양감시·수색을 위한 기획연구 (기간 2023.07 ~ 2023.12)
- Increasing resolution of the Nano Prism sensor (기간 2022.06 ~ 2023.06)
- Just Climate AI for Nowcasting (기간 2022.05 ~ 2022.12)
- Adversarial Defense (3rd year) (기간 2022.02 ~ 2022.12)
- Adversarial Attack (3rd year) (기간 2022.02 ~ 2022.12)
- 미래국방 인공지능 특화연구센터(2019) 1단계 (기간 2019.12 ~ 2022.12)
- Explainable AI 기반 상호작용형 인공위성 이미지 분석 및 딥러닝 가속화 기술 개발 (기간 2019.09 ~ 2022.08)
- 영상 개선 및 추적 알고리즘 연구 (image enhancement and object tracking) (기간 2020.04 ~ 2021.12)
- 영상 내 객체간 관계 분석 기반 해상 선박/구조물 상세 식별 콘텐츠 기술 개발 (기간 2019.04 ~ 2021.12)
- 비디오 이해를 위한 데이터수집 및 보정 자동화 시스템 개발 (기간 2017.07 ~ 2021.12)
- 소량의 데이터를 활용한 머신러닝 기술 고도화 (Few-Shot Open-Set Learning) (기간 2020.03 ~ 2021.11)
- 알고리즘을 통한 AI 안면인식 교란 대응기술 고도화 (Digital-domain adversarial attack) (기간 2020.03 ~ 2021.11)
- 물리적 패턴을 통한 AI 안면인식 교란 기술 연구 (Physical adversarial attack) (기간 2020.03 ~ 2021.11)

## 특허

2021년 10월 13일–2026년 10월 13일에 등록된 특허 1건이다. 발명자·명칭·등록번호·등록일은 연구실 표기다.[^patents]

- 사용자의 행동 범주를 분류하기 위한 인간 행동 인식장치, 인간 행동 인식 방법 및 컴퓨터 프로그램 (발명자 김창익, 구인용, 박연주, 정민기, 이수민, 우상민; 등록번호 10-2515065; 등록일 2023. 03. 23.)

## 수상·선정

2021년 10월 13일–2026년 10월 13일 범위의 수상·선정 17건이다. 곽영준 학생의 학회 워크숍 수상은 2023년만 표시되어 있다.[^news]

- 2026.06.27 · 설기현 학생, 대한전자공학회 하계학술대회 산업체(LG) 관심논문상
- 2026.06.07 · 서민석 학생, CVPR 2026 Compute Gold Star 및 Transparency Champion
- 2025.12.05 · 김영헌 학생, E5 KAIST 창업경진대회 우수상
- 2025.12.05 · 함제석 학생, 운당학술상 운당학생논문상
- 2025.11.17 · 김영헌 학생, 4대 과학기술원 공동창업 경진대회 우수상(DGIST 총장상)
- 2025.06.27 · 장민석 학생, 대한전자공학회 하계학술대회 우수논문상
- 2024.05.27 · 김창익 교수, KAIST Education Innovation Day 교육혁신상
- 2023.11.22 · 「인공지능 안전성」 세종도서 선정
- 2023 · 곽영준 학생, ICCV 2023 Workshop on Resource Efficient DL for Computer Vision Challenge Tr 1의 1등상
- 2022.07.01 · 권명준 학생, 대한전자공학회 하계학술대회 우수학생논문상
- 2022.07.01 · 전우진 학생, 대한전자공학회 하계학술대회 우수논문상
- 2022.07.01 · 손민지 학생, 대한전자공학회 하계학술대회 산업체(LG) 관심논문상
- 2022.07.01 · 김민범 학생, 대한전자공학회 하계학술대회 산업체(LG) 관심논문상
- 2022.07.01 · 황주비 학생, 대한전자공학회 하계학술대회 산업체(현대자동차) 관심논문상
- 2022.07.01 · 이인영 학생, 대한전자공학회 하계학술대회 우수학생논문상
- 2022.02 · 김창익 교수, KAIST 개교 51주년 융합연구상
- 2021.11.26 · 김정수 학생, 대한전자공학회 추계학술대회 우수논문상

## 소식

2021년 10월 13일–2026년 10월 13일 범위에 있는 연구 성과, 학술 행사, 강연·기고와 자문 활동 소식 32건이다. 아래 소식의 게시 날짜는 2023–2026년이다.[^news][^home]

- 2026.10.05 · 뜻밖의강의실에 김창익 교수의 「AI는 정말 느끼기 시작했을까」 기사 게시
- 2026.09.23 · 한겨레에 「집단 기억은 누구 것인가」 게시
- 2026.09.04 · 국가정보원과 센티언트 AI 미래포럼 개최
- 2026.08.31 · 한겨레에 「AI에 의식이 있다면…인격과 권리를 인정해야 할까」 게시
- 2026.08.26 · 국립생태원과 생태안보미래포럼 개최
- 2026.08.15 · 주간경향에 센티언트 AI의 위험과 질문을 다룬 기고 게시
- 2026.08.12 · 시사위크에 「두루미에서 안보까지… AI로 ‘환경’을 보는 과학자」 기사 게시
- 2026.08.08 · 동아일보에 「‘연기인가, 진짜 감정인가’ 다시 불붙는 AI 의식 논의」 기사 게시
- 2026.07.15 · CILAB의 안전한 AI 학습법 개발 소식 게시
- 2026.06.17 · CILAB의 Upsample Anything 기술 개발 소식 게시
- 2026.05.14 · 서울경제에 「AI가 국가 안보에 던지는 경고장」 게시
- 2026.03.05 · 안보과학기술대학원 봄학기 정기 세미나
- 2025.12.12 · 김창익 교수가 국제전략문제연구소(IISS) 워크숍에 참여해 인지전과 인식 영역을 주제로 발표
- 2025.11.26 · 김창익 교수가 프라하의 제10차 한·체코 미래포럼에 참여해 AI 시스템의 보안 취약성과 경제적 위험을 주제로 발표
- 2025.11.17 · 김창익 교수가 주보스턴 대한민국 총영사관이 주최한 보스턴 CIC 행사에서 초청 강연
- 2025.11.11 · 김창익 교수가 불가리아 소피아에서 민주주의연구센터(CSD)가 주최한 AI 시대 경제 회복력과 안보 패널 토론에 참여
- 2025.11.10 · 김창익 교수가 한·불가리아 민주주의 라운드테이블에서 「AI와 민주주의」 강연
- 2025.08.28 · 안보과학기술대학원 세미나 개최
- 2025.08.01 · 「빨라진 기후위기: AI Paradox」 게시
- 2025.03.20 · 「국립생태원, 이제는 인공지능(AI)으로 야생동물 분석한다」 소식 게시
- 2025.02.27 · 안보과학기술대학원 봄학기 정기 세미나
- 2024.11.01 · 한·체코 미래 경제 협력 토론회 개최
- 2024.07.24 · 제1차 안보과학기술대학원 세미나 개최
- 2024.07.23 · 비디오 인식용 VideoMamba 개발 소식 게시
- 2024.07.22 · 김창익 교수의 도서 출간 소식 게시
- 2024.07.17 · 서울경제에 「AI 챗봇이 인류에 전하는 경고」 게시
- 2024.04.22 · 사이버안보연구소 관련 기사 게시
- 2023.05.19 · 「인공지능 안전성(AI Safety)」 출간
- 2023.05.18 · 김창익 교수가 해양경찰청 유무인복합체계 자문위원으로 위촉
- 2023.03.01 · 김창익 교수가 삼성전자 MX사업부 기술자문위원으로 위촉
- 2023.02.20 · 김창익 교수가 국가안보실 정책자문위원으로 위촉
- 2023.02.15 · 스프에 「AI가 당신을 노린다면? AI를 속여서 방어한다!」 게시

## 연락과 위치

- 교수실: KAIST IT융합빌딩(N1) 413호[^ee][^prof]
- 주소: 대전광역시 유성구 대학로 291 KAIST, 34141[^prof]
- 전화: 042-350-7421[^prof]
- 교수 이메일: changick@kaist.ac.kr[^prof]

## 각주
[^home]: CI Lab., Home, 연구실 소개·최근 소식·논문 채택 소식. <https://cilabs.kaist.ac.kr/> 관측 2026-10-31.
[^prof]: CI Lab., Members, 김창익 교수의 직위·소속·경력·학력·연구 관심·연락처. <https://cilabs.kaist.ac.kr/members> 관측 2026-10-31.
[^areas]: CI Lab., Research Area, 적대적 공격·방어, 학습, 영상 인식, 입체 시각과 행동 분석 등의 연구 갈래. <https://cilabs.kaist.ac.kr/research/research-area> 관측 2026-10-31.
[^vision]: CI Lab., Image Recognition. 영상의 각 위치를 의미에 따라 구분하는 영상 분할을 설명하고 연구 논문을 소개한다. <https://cilabs.kaist.ac.kr/research/research-area/image-recognition> 관측 2026-10-31.
[^meta]: CI Lab., Meta Learning & Deep Network, 적은 예시와 새로운 범주를 다루는 학습 및 캡슐 네트워크 연구. <https://cilabs.kaist.ac.kr/research/research-area/meta-learning-deep-network> 관측 2026-10-31.
[^domain]: CI Lab., Domain Adaptation, 학습·사용 자료의 차이와 도메인 적응 연구. <https://cilabs.kaist.ac.kr/research/research-area/domain-adaptation> 관측 2026-10-31.
[^security]: CI Lab., Adversarial Attack & Defense. 조작된 입력으로 인공지능의 정상 작동을 방해하는 공격, 강인한 모델의 설계·공격 탐지와 인증 가능한 방어 연구를 서술한다. <https://cilabs.kaist.ac.kr/research/research-area/adversarial-attack-defense> 관측 2026-10-31.
[^action]: CI Lab., Action Analysis, 실시간 행동 검출·예측, 여러 종류의 자료를 쓰는 행동 인식과 자료 소실에 대응하는 연구. <https://cilabs.kaist.ac.kr/research/research-area/action-analysis> 관측 2026-10-31.
[^three]: CI Lab., 3D Vision, 입체 구조·움직임 추정과 자율주행·증강·가상현실·로봇 이동의 연결. <https://cilabs.kaist.ac.kr/research/research-area/3d-vision> 관측 2026-10-31.
[^diffusion]: CI Lab., Diffusion Model, 복잡한 텍스트와 그 안의 관계에 맞는 이미지를 생성하는 연구. <https://cilabs.kaist.ac.kr/research/research-area/diffusion-model> 관측 2026-10-31.
[^explain]: CI Lab., Captioning & Explainable A.I. 인공지능의 판단 근거를 시각화하거나 서술하며 영상과 외부 지식의 결합을 통한 추론을 연구한다고 서술한다. <https://cilabs.kaist.ac.kr/research/research-area/captioning-explainable-a-i> 관측 2026-10-31.
[^climate]: CI Lab., Climate-AI & Eco-AI. 극단적 이상 기후에 대응할 초단기 기상예측과 위성영상 예측 모델을 개발하고, 자동 촬영 영상의 야생동물 분류·개체 수 분석을 연구한다고 서술한다. <https://cilabs.kaist.ac.kr/research/research-area/climate-eco-ai> 관측 2026-10-31.
[^ee]: KAIST 전기및전자공학부, 김창익 교수 소개, 직위·연구실 이름·분야·위치. <https://ee.kaist.ac.kr/professor/12156/> 관측 2026-10-31.
[^gst]: KAIST 안보과학기술대학원, 교수 명단, 김창익의 소속학과·연구분야·연구실. <https://gst.kaist.ac.kr/member/faculty/> 관측 2026-10-31.
[^gggs]: KAIST 녹색성장지속가능대학원, 전체 교수진의 겸임교수 구획, 김창익의 소속과 기상·생태 AI 연구분야. <https://gggs.kaist.ac.kr/all-professor> 관측 2026-10-31.
[^phd]: CI Lab., Ph.D, 박사과정과 Part-time 명단. <https://cilabs.kaist.ac.kr/members/ph-d> 관측 2026-10-31.
[^ms]: CI Lab., MS, 석사과정 명단. <https://cilabs.kaist.ac.kr/members/ms> 관측 2026-10-31.
[^alumni]: CI Lab., Alumni, 학위·과정·연도와 진로. <https://cilabs.kaist.ac.kr/members/alumni> 관측 2026-10-31.
[^publications]: CI Lab., Publications, 국제·국내 학술지·학회 목록. <https://cilabs.kaist.ac.kr/research/publications> 관측 2026-10-31.
[^ij]: CI Lab., International Journal, 1–80번 목록. <https://cilabs.kaist.ac.kr/research/publications/international-journal> 관측 2026-10-31.
[^ic]: CI Lab., International Conference, 1–186번 목록. <https://cilabs.kaist.ac.kr/research/publications/international-conference> 관측 2026-10-31.
[^dj]: CI Lab., Domestic Journal, 1–47번 목록. <https://cilabs.kaist.ac.kr/research/publications/domestic-journal> 관측 2026-10-31.
[^dc]: CI Lab., Domestic Conference, 1–123번 목록. <https://cilabs.kaist.ac.kr/research/publications/domestic-conference> 관측 2026-10-31.
[^projects]: CI Lab., Projects, 수행 중·이전 과제명과 기간. <https://cilabs.kaist.ac.kr/projects> 관측 2026-10-31.
[^patents]: CI Lab., Patents, 발명자·특허명·출원·등록 정보. <https://cilabs.kaist.ac.kr/patents> 관측 2026-10-31.
[^news]: CI Lab., News, 수상·연구 소식·행사·자문 활동. <https://cilabs.kaist.ac.kr/news> 관측 2026-10-31.

[^p1]: S. Ham, J. Jang, W. Lee, C. Kim, arXiv (온라인 2026-05-23). <https://doi.org/10.48550/arXiv.2605.24550> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2605.24550> 관측 2026-10-31.
[^p2]: J. Byun 외, C. Kim, arXiv (온라인 2022-03-17). <https://doi.org/10.48550/arXiv.2203.09123> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2203.09123> 관측 2026-10-31.
[^p3]: M. Seo, M. Hamilton, C. Kim, arXiv (온라인 2025-11-20). <https://doi.org/10.48550/arXiv.2511.16301> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2511.16301> 관측 2026-10-31.
[^p4]: J. Park 외, C. Kim, ECCV 2024 (2024). <https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3565_ECCV_2024_paper.php> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3565_ECCV_2024_paper.php> 관측 2026-10-31.
[^p5]: I. Koo 외, C. Kim, arXiv (온라인 2026-03-11). <https://doi.org/10.48550/arXiv.2603.11095> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2603.11095> 관측 2026-10-31.
[^p6]: S. Woo 외, C. Kim, arXiv (온라인 2023-12-26). <https://doi.org/10.48550/arXiv.2312.15980> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2312.15980> 관측 2026-10-31.
[^p7]: J. Park 외, C. Kim, arXiv (온라인 2022-12-07). <https://doi.org/10.48550/arXiv.2212.04005> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2212.04005> 관측 2026-10-31.

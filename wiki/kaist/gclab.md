# 기하 컴퓨팅 연구실 (Geometric Computing Lab., GCLab)

**KAIST 전산학부 · 최성희 부교수**

- 분야: 계산기하학, 기하 모델링, 컴퓨터 그래픽스, 색상·영상 처리, 오디오 처리, 계산 자원 분배
- 대분야: 컴퓨팅·AI, 수학·통계
- 태그: 컴퓨터 그래픽스·기하 처리[^research], 3D 프린팅[^dept], 음향·오디오 AI[^dept], 컴퓨터 비전[^p3]
- 홈페이지: <https://sites.google.com/view/kaist-gclab>
- 근거와 출처: [GCLab 근거 페이지](gclab-sources.md)

> 점과 표면, 색상 같은 자료를 컴퓨터로 다루는 기하학적 계산 방법을 만들고, 이를 입체 모델 처리와 시각 콘텐츠 분석 등에 적용하는 연구실이다.[^home][^dept]

## 무엇을 연구하나

KAIST 전산학부 최성희 부교수가 이끄는 연구실로, 계산기하학(점·선·도형에 관한 문제를 푸는 계산 절차와 그 복잡도를 연구하는 분야)을 바탕으로 이론과 응용을 함께 연구한다. 기하학적 문제를 해결하는 실용적인 알고리즘을 개발해 다양한 분야에 적용하는 것이 목표다. 누리집은 기하 모델링, 컴퓨터 그래픽스, 시각화를 주요 관심으로 제시한다.[^home][^dept][^prof]

입체 모양을 다루는 연구에서는 물체 표면에서 얻은 표본점으로 원래 표면을 근사하는 표면 재구성과, 물체의 내부 구조를 나타내는 중심축을 계산한다. 연구 소개는 표면 재구성 알고리즘의 이론적 보장을 다루고, 그래픽 처리 장치인 GPU(Graphics Processing Unit)를 이용해 중심축에 속하는 점들을 구하는 방법을 제시한다. 옷감 시뮬레이션(옷감의 움직임과 변형을 계산으로 재현하는 일)에서는 모양의 세밀함에 따라 메시를 다르게 나누어 계산한다.[^research]

색상도 기하학적 계산의 대상이다. 색상 팔레트(함께 사용하는 색의 집합)를 이루는 색들을 정렬하고, 서로 다른 팔레트에서 색들이 이어지는 전체 흐름을 비교하는 방법을 연구한다. 대표 논문에서는 색 사이의 거리와 색들을 연결한 그래프를 이용하는 DCCW(Dynamic Closest Color Warping)를 제안하고, 팔레트 사이의 중간 색상 조합 만들기와 이미지 색 바꾸기 등의 응용을 보였다.[^p2]

연구 대상은 입체 모양과 색상에만 머물지 않는다. 학과 소개는 점구름 압축, 리듬 게임의 비트맵 생성, 인체 동작 생성, 오디오 고해상도 변환과 부하 평형 알고리즘도 연구 주제로 적는다. 모델 전송 연구에서는 학습을 마친 딥러닝 모델을 조각으로 나눠 보내고, 전송 도중에도 받은 부분으로 추론을 수행하게 한다.[^dept][^p1]

## 주요 연구 주제

### 기하 모델과 표면 처리

표면 재구성은 물체 표면의 점들로부터 원래 표면을 근사하는 문제다. 중심축 연구는 물체 표면에 여러 곳에서 닿는 내부의 최대 공들로 정의되는 골격 표현을 계산하는 문제를 다룬다. 학과 소개는 메시 압축, 이미지 기반 입체 모델링, 3차원 프린팅의 모델 방향 후보 자동 생성과 출력 결과를 고려한 방법을 함께 제시한다.[^research][^dept]

센서 네트워크(센서들이 자료를 주고받는 망)에서는 감지 영역을 가로지르는 경로 전체를 고려해 망의 감지 범위를 평가하고 센서를 추가로 배치하는 문제를 연구한다. 이 문제를 병목 스타이너 트리 문제(정해진 수의 점을 더해 고리 없이 연결할 때 가장 긴 연결선의 길이를 최소화하는 문제)와 연결하며, 해당 기하학적 연결 문제의 정확한 해를 찾는 알고리즘도 다룬다.[^research]

### 색상과 시각 콘텐츠 분석

색상 정렬 연구는 팔레트 안의 색을 따로 비교하는 데서 나아가 색의 조합과 흐름을 함께 다룬다. DCCW는 한 팔레트의 색과 다른 팔레트의 색을 잇는 그래프 사이의 거리 합을 계산한다. 연구진은 여러 데이터셋에서 기존 방법과 정확도 및 계산 시간을 비교하고, 사람의 선호를 조사해 정렬 결과를 평가했다.[^p2] 리듬 게임 연구의 공개 구현 vid2bmap은 게임의 재생 영상을 입력받아 비트맵 차트 이미지를 만드는 도구다.[^beatmap]

리듬 게임 영상 연구에서는 객체 탐지(영상에 나타나는 대상을 찾아 구별하는 방법)를 이용해 여러 게임의 화면 요소를 비트맵 표현에 대응시킨다. 대상 게임에서 어떤 동작 버튼을 언제 사용해야 하는지와 그 유형을 영상에서 찾아 게임 진행 자료로 추출하는 방법이다.[^p3]

### 오디오 분석과 모델 실행

학과 소개는 오디오 고해상도 변환과 딥러닝 기반 오디오 주파수 편이 변조를 연구 주제로 제시한다.[^dept] 모델 실행 연구에서는 서버가 모델 조각을 순차적으로 전송하고 사용자 기기가 그 조각을 결합해 근사 모델을 구성한다. 전체 전송이 끝나기 전에도 중간 결과를 제공하는 방식이다.[^p1]

## 대표 논문

2021–2026년 KAIST 재직 시기 논문 가운데 교수의 저자 참여를 확인하고 초록을 확보한 3편을 골랐다. 아래의 ‘쉽게 말하면’은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 교수의 저자 위치 |
|---|---|---|---|---|
| 1 | 2021 | [Progressive Transmission and Inference of Deep Learning Models](https://doi.org/10.48550/arxiv.2110.00916) · arXiv 판 | 학습을 마친 딥러닝 모델을 서버에서 사용자 기기로 보낼 때, 파일을 모두 받은 뒤에야 계산을 시작하는 문제를 다룬다. 모델을 조각으로 나눠 순서대로 보내고, 사용자 기기는 받은 조각들을 합쳐 근사 모델로 추론한다. 실험에서는 모델 크기와 전체 전송 시간을 늘리지 않으면서 정확도를 보존했고, 특히 느린 연결에서 중간 결과를 제공하는 방식을 보였다.[^p1] | 저자 4명 중 마지막 저자 |
| 2 | 2021 | [Dynamic Closest Color Warping to Sort and Compare Palettes](https://doi.org/10.1145/3450626.3459776) · ACM Transactions on Graphics | 팔레트의 색들을 정렬해 두 팔레트의 전체적인 색 흐름이 얼마나 비슷한지 재는 방법이다. 색과 다른 팔레트의 색들을 연결한 그래프 사이의 최소 거리 합을 계산한다. 여러 데이터셋에서 기존 방법과 정확도·계산 시간을 비교했고, 사람의 선호 조사로 정렬 결과를 평가했다. 팔레트 사이의 중간 조합 만들기, 팔레트 탐색, 이미지 색 바꾸기도 보였다.[^p2] | 저자 2명 중 마지막 저자 |
| 3 | 2021 | [Vision-based beatmap extraction in rhythm game toward platform-aware note generation](https://doi.org/10.1109/cog52621.2021.9619108) · 2021 IEEE Conference on Games (CoG) | 리듬 게임의 콘텐츠를 자동으로 만들려면 게임이 실행되는 기기와 조작 방식의 특징을 반영한 자료가 필요하다. 연구진은 게임의 재생 영상을 분석해 그 자료를 얻는 방법을 제안했다. 여러 게임에서 공통으로 나타나는 화면 요소를 객체 탐지로 찾고 비트맵 표현에 대응시킨다. 대상 게임에서 동작 버튼과 유형·시점을 올바르게 찾아 비트맵을 추출했다고 보고했다.[^p3] | 저자 2명 중 마지막 저자 |

## 교수와 전문 분야

최성희 부교수의 영문 이름은 Sunghee Choi다. 전산학부 교수 명단은 전문 분야를 계산기하학과 컴퓨터그래픽스로 적는다.[^faculty] 교수 소개는 기하학적 문제의 알고리즘과 복잡도를 연구하는 계산기하학을 중심 분야로 밝히고, 컴퓨터 그래픽스·로봇·기하 모델링·계산생물학·계산위상수학·시각화에도 관심이 있다고 적는다.[^prof]

서울대학교에서 컴퓨터공학 학사(1995), University of Texas at Austin에서 전산학 석사(1997)와 박사(2003)를 받았고, 2003년 Mathematical Sciences Research Institute에서 박사후연구 경력을 적고 있다.[^prof] 최근 논문에서 볼 수 있는 전문 분야로는 색상 팔레트의 기하학적 비교[^p2]와 전송 중인 학습 모델을 부분적으로 실행하는 계산 방법[^p1]이 있다.

## 응용 분야

표면 재구성은 컴퓨터 지원 설계, 컴퓨터 그래픽스, 컴퓨터 비전과 수학적 모델링에서 표면을 표현하는 문제와 연결된다.[^research] 학과 소개는 3차원 프린팅의 출력 방향 선택, 이미지 기반 입체 모델링, 리듬 게임 콘텐츠 생성과 오디오 처리를 응용 대상으로 적는다.[^dept] 색상 정렬 논문은 팔레트 탐색과 이미지 색 바꾸기를,[^p2] 모델 전송 논문은 웹 브라우저나 모바일 기기에서의 모델 실행을 대상으로 한다.[^p1]

## 구성원

2026년 10월 27일 누리집 Students 페이지의 박사과정 6명과 석사과정 1명이다. 과정은 페이지 표기이며, ‘대표 논문 참여’는 위 표의 논문 번호다. 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^students]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Hangyul Park | 박사과정 |  |
| Hyeonguk Ryu | 박사과정 |  |
| Yoonsung Choi | 박사과정 |  |
| Kyounga Woo | 박사과정 |  |
| Jihoon Hyun | 박사과정 |  |
| Haun Kim | 박사과정 |  |
| Changyu Lee | 석사과정 |  |

## 졸업생과 진로

2026년 10월 27일 Alumni 페이지에 게시된 박사 졸업생 7명과 석사 졸업생 22명이다. 학위 연도와 논문 제목은 학위논문 목록의 같은 이름·학위 항목을 함께 적었다. 진로는 Alumni 페이지가 적은 소속이다.[^alumni][^thesis]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Yeonghun Kim | Ph. D. (2026) | Samsung Electro-Mechanics | Spatial Data Compression through Frequency-Aware Transform Coding |
| Suzi Kim | Ph. D. (2022) | Unity (Weta Digital) | Developing a Sortable Color Palette through Geometric Approaches |
| Jeongho Son | Ph. D. (2020) | Hana Financial Group Inc. | Cropping-Resilient 3D Mesh Model Watermarking |
| Donghoon Shin | Ph. D. (2016) | DGIST | Efficient algorithms with performance guarantees for geometric problems in wireless networks |
| Jaehwan Ma | Ph. D. (2012) | CLO Virtual Fashion Inc. | Medial axis point approximation and applications |
| Chunseok Lee | Ph. D. (2012) | Samsung DMC R&D center | Path problems in wireless sensor networks |
| Yongjoon Lee | Ph. D. (2012) | CLO Virtual fashion Inc. | Multi-resolution simulation and automated fitting for virtual garments |
| Jeong Uk Lee | M.S. (2025) |  | ARGS: Advanced Regularization on Aligning Gaussians over the Surface |
| Hyeongseok Gwak | M.S. (2025) | MSR, SK hynix | Super-Resolution Enhancement via Kernel-based High-Order Degradation |
| Sangwon Kwak | M.S. (2024) | whereable.ai | Talking Face Generation by Disentangled Audio-Visual Representation and Implicit Natural Code |
| Youngjo Min | M.S. (2023) | Mobilint, Inc. | Learning with Diffusion and Anisotropic Operators for Shape Correspondence |
| Sanghyun Jung | M.S. (2023) | ENERZAi | Deep Learning based Audio Super Resolution |
| Beomki Kim | M.S. | REALTIMEVISUAL |  |
| Youngsoo Lee | M.S. (2021) | HYPERCONNECT LLC. | Progressive Transmission and Inference of Deep Learning Models Served over Network |
| Jihwan Kim | M.S. (2020) | Peoplefund | Hallucinating Very Low-Resolution Face Image by 16x Magnification with Age-based Attribute |
| Jongmin Park | M.S. (2020) | Twinny Co.,Ltd. | Real-time Arthroscopy Support System with Object Detection |
| Eunseok Kim | M.S. (2014) | Milliman Inc. | I/O-Efficient minimizing range sum |
| Sehyun Joo | M.S. (2018) | Tmaxsoft | Many-to-Many matching with capacity using lexicographic preference |
| Heewon Chung | M.S. (2017) | The Bank of Korea | Attention-based image classification using semantic segmentation and convolutional neural network |
| Jungbin Hwang | M.S. | SK Telecom |  |
| Dodam Kim | M.S. (2016) | Samsung Electronics | Object relationship network model for image collections |
| Juyeon Park | M.S. (2015) | NCSoft | Automated laughter detection on a mobile platform |
| Sangil Kim | M.S. | Aramin Inc. |  |
| Jongwon Han | M.S. (2012) | HBSmith Inc. | Smartphone interface based on image processing |
| Changbum Park | M.S. (2006) | Dentistry graduate school | Geometric analysis and prediction systems for protein domain interacting interfaces |
| Taewon Yoo | M.S. (2006) | SK Planet | Distributed kinetic delaunay triangulation |
| Jihye Kim | M.S. (2007) | Samsung Electronics | Homotopy-preserving power shape simplification |
| Hyongjin Yang | M.S. | LG Electornics |  |
| Sangyoon Lee | M.S. | TmaxSoft |  |

## 최근 논문 목록 (2021–2026)

색상 처리, 리듬 게임의 영상 분석, 점구름 압축, 기하학적 계산, 오디오 분석과 계산 자원 분배를 다룬 논문 목록이다. 국제 목록의 2021년 구역 4편과 국내 목록의 2021–2025년 구역 9편이다. 제목·저자·발표처는 연구실 표기를 따른다.[^pubs][^domestic]

**2025**

- Kyounga Woo and Sunghee Choi. "합성곱 신경망과 트랜스포머 융합 모델 기반 인공지능 생성 음악 탐지 기법 / AI-generated Music Dection Using Hybrid  CNN-Transformer". *Korea Computer Congress, Korea, July 2025*.
- Jihoon Hyun and Sunghee Choi. "이차 제약 이차 계획법을 사용한 유클리드 평면 상에서 레이블된 점들의 회전의 가짓수 계산 / Enumerating Orientations of Labeled Points on a Euclidean Plane using a Quadratically Constrained Quadratic Program". *정보과학회 컴퓨팅의 실제 논문지(KTCP), Vol. 31, No. 4, pp. 207-210, April 2025*.

**2024**

- Hyeonguk Ryu and Sunghee Choi. "3차원 기하 모델 프로세싱 프레임워크 개발". *정보과학회지, Vol. 42, No. 2, pp. 15-20, Feb. 2024*.
- Hyeonguk Ryu and Sunghee Choi. "QR 코드 인식 향상을 위한 결함 검사 도구 개발 / Development of a Defect Inspection Tool for Enhanced QR Code  Recognition". *Korea Computer Congress, Korea, June 2024*.
- Jihoon Hyun and Sunghee Choi. "이차 제약 이차 계획법을 사용한 유클리드 평면 상에서 레이블된 점들의 회전의 가짓수 계산 / Enumerating Orientations of labeled Points on a Euclidean Plane using a Quadratically Constrained Quadratic Program". *Korea Computer Congress, Korea, June 2024*.
- Kyounga Woo, Yeonghun Kim, and Sunghee Choi. "적대적 학습을 통한 점 구름 속성 손실 압축 / Adversarial Learning for Lossy Point Cloud Attribute Compression". *Korea Computer Congress, Korea, June 2024*.

**2023**

- Yeonghun Kim and Sunghee Choi. "vid2bmap: 샴 네트워크와 노이즈 최적화를 통한 리듬게임 비트맵 추출 / vid2bmap: Beatmap Extraction in Rhythm Game using Siamese Net and Noise Optimization". *Korea Software Congress, Korea, Dec. 2023*.

**2022**

- Yeonghun Kim and Sunghee Choi. "웨이블릿 공간에서의 저역 필터를 통한 차원 점구름 속성의 손실압축 / Lossy Point Cloud Attribute Compression using Low-pass Filter on Wavelet Domain". *Korea Software Congress, Korea, Dec. 2022*.

**2021**

- Youngsoo Lee, Sangdoo Yun, Yeonghun Kim and Sunghee Choi. "Progressive Transmission and Inference of Deep Learning Models". *IEEE International Conference on Machine Learning and Applications (ICMLA), 2021*.
- Youngsoo Lee and Sunghee Choi. "A Greedy Load Balancing Algorithm on Serverless Platforms Maximizing Locality". *International Conference on Cloud and Big Data Computing (ICCBDC), 2021*.
- Yeonghun Kim and Sunghee Choi. "Vision-based beatmap extraction in rhythm game toward platform-aware note generation". *IEEE Conference on Games (CoG), 2021*. <https://doi.org/10.1109/cog52621.2021.9619108>
- Suzi Kim and Sunghee Choi. "Dynamic Closest Color Warping to Sort and Compare Palettes". *ACM Transactions on Graphics (TOG), 2021 (presented at SIGGRAPH 2021)*.
- Suzi Kim and Sunghee Choi. "이미지 분할과 관심 영역 맵 기반 색상 스키마 추출 / Color Scheme Extraction Based on Image Segmentation and Saliency Map". *정보과학회논문지 (Journal of KIISE), Vol. 48, No. 3, pp. 302-307, Mar. 2021*.

## 과제

연구실은 SW StarLab 과제로 3차원 기하 모델 처리 프레임워크 개발을 소개한다. 아래 수행 기간은 2021년 10월 13일–2026년 10월 13일과 겹친다.[^home]

- Development of a Framework for 3D Geometric Model Processing (지원 IITP; 사업 SW StarLab; 기간 2019. 4. 1.~2026. 12. 31.)

## 연락과 위치

- 연구실 주소: 대전광역시 유성구 대학로 291 KAIST 전산학부, E3-1, 우편번호 34141[^contact]
- 연구실 전화: +82-42-350-7834[^contact]
- 교수 사무실: E3-1 3404호, 전화 +82-42-350-3534[^prof][^faculty]

## 각주
[^home]: 누리집 첫 화면. <https://sites.google.com/view/kaist-gclab> (열람 2026-10-27). 연구 목표, 관심 분야, SW StarLab 과제와 기간.

[^dept]: KAIST 전산학부 연구실 소개. <https://cs.kaist.ac.kr/research/labView?sn=56&menu=64> (열람 2026-10-27). 국문명, 지도교수, 이론·응용 연구, 세부 주제.

[^faculty]: KAIST 전산학부 교수 명단. <https://cs.kaist.ac.kr/people/faculty> (열람 2026-10-27). 최성희 부교수, 계산기하학·컴퓨터그래픽스, 사무실.

[^research]: Research. <https://sites.google.com/view/kaist-gclab/research> (열람 2026-10-27). 표면 재구성·중심축·센서 망·스타이너 트리·옷감 계산.

[^pubs]: Publications. <https://sites.google.com/view/kaist-gclab/publications> (열람 2026-10-27). 국제 논문 목록.

[^domestic]: Domestic. <https://sites.google.com/view/kaist-gclab/publications/domestic> (열람 2026-10-27). 국내 논문 목록.

[^prof]: Professor. <https://sites.google.com/view/kaist-gclab/members/Members> (열람 2026-10-27). 학력, 연구 관심, 소속, 사무실·전화.

[^students]: Students. <https://sites.google.com/view/kaist-gclab/members/students> (열람 2026-10-27). 박사과정 6명, 석사과정 1명.

[^alumni]: Alumni. <https://sites.google.com/view/kaist-gclab/members/alumni> (열람 2026-10-27). 박사 졸업생 7명, 석사 졸업생 22명과 진로.

[^thesis]: Technical Report/Book/Thesis. <https://sites.google.com/view/kaist-gclab/publications/TR-Book-Thesis> (열람 2026-10-28). 졸업생 학위 연도·논문.

[^contact]: Contact. <https://sites.google.com/view/kaist-gclab/contact> (열람 2026-10-28). 연구실 주소·전화.

[^beatmap]: vid2bmap 연구진 공개 구현. <https://github.com/Neutrinoant/vid2bmap> (열람 2026-10-28). 영상 입력·차트 출력, 2023년 발표와 2021년 선행 논문 관계.

[^p1]: Y. Lee, S. Yun, Y. Kim, S. Choi, arXiv:2110.00916 [cs.LG] (온라인 2021-10-03). <https://doi.org/10.48550/arxiv.2110.00916> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2110.00916> (열람 2026-10-28).

[^p2]: S. Kim, S. Choi, ACM Transactions on Graphics (Proceedings SIGGRAPH) 40, 1–15 (Article 95) (2021). <https://doi.org/10.1145/3450626.3459776> 초록 기준(논문 페이지 게시 초록). 연구진 공개 구현의 Abstract 칸. 초록 원문 <https://github.com/SuziKim/DCCW> (열람 2026-10-28).

[^p3]: Y. Kim, S. Choi, 2021 IEEE Conference on Games (CoG) (2021). <https://doi.org/10.1109/cog52621.2021.9619108> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1109/cog52621.2021.9619108%7C10.20972/kjee.17.2.200701.197> (열람 2026-10-28).

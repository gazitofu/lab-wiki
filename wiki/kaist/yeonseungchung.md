# 정연승 교수 연구실

**KAIST 수리과학과 · 정연승 교수**

- 분야: 베이지안 통계·응용통계[^dept]
- 대분야: 수학·통계
- 태그: 통계적 추론·검정[^p1][^p3][^p5], 시계열 분석·예측[^p2][^p4][^p5]
- 홈페이지: <https://sites.google.com/view/yeonseungchung>
- 근거와 출처: [정연승 교수 연구실 근거 페이지](yeonseungchung-sources.md)

> 지역과 시간에 따라 달라지는 자료의 관계를 다루는 통계 모형을 만들고, 환경 자료·반도체 제조·영상 속 이동 경로 분석에 연결하는 연구실이다.[^home][^p1][^p2][^p3][^p6][^p7][^p8]

## 무엇을 연구하나

정연승 교수 연구실은 베이지안 통계(관측 전의 정보와 새 자료를 결합해 알지 못하는 값에 대한 확률을 갱신하는 통계 방법)를 바탕으로 자료의 관계를 설명하는 모형을 개발한다. 누리집은 비모수·준모수 베이지안 계층 모형과 베이지안 시공간 모형을 연구 관심으로 적는다. 비모수 모형은 자료가 따르는 분포를 고정된 유한 개수의 값만으로 나타내도록 제한하지 않는 모형이며, 준모수 모형은 형태를 정한 부분과 형태를 유연하게 둔 부분을 결합한 모형이다. 계층 모형은 여러 집단이나 수준의 관계를 단계로 연결한 모형이다.[^home] 최근 논문에서는 지역 간 차이를 유연하게 표현하고[^p1][^p3] 추정의 불확실성을 다루는[^p3] 새 통계 방법을 제안한다.[^p2]

중요한 문제는 같은 환경 요인과 결과의 관계가 지역마다, 또 시기마다 달라질 때 이를 어떻게 함께 분석하느냐다. 시계열(시간 순서에 따라 관측한 자료)에서 온도와 사망의 관계가 시간에 따라 직선적으로 변한다는 가정 대신 변화점(자료를 만드는 관계나 변화 구조가 바뀌는 시점)을 찾는 메타분석(여러 연구나 집단에서 얻은 추정 결과를 통합하는 분석) 모형을 만든다. 온도와 사망의 관계를 예로 삼아 시간 구간을 나누고, 일반적인 관측과 크게 어긋난 값의 영향을 함께 다룬다.[^p2] 사건 수가 영인 날이 많은 자료에서는 사건의 발생 여부와 발생했을 때의 수를 나누어 분석하는 모형을 제안한다.[^p3]

여러 지역의 환경 자료를 묶어 읽는 방법도 연구한다. 여러 오염물질의 계절적 변화 곡선과 지역 특성을 함께 반영해 군집(자료 사이의 유사성을 기준으로 묶은 집단)을 찾는 모형을 개발했다. 직접 관측되지 않지만 여러 변수의 공통 변화를 설명하는 잠재요인을 이용하고, 시간 의존성도 다루도록 확장했다.[^p5] 진드기 개체 수 연구에서는 진드기가 있는지와 양의 개체 수를 분리하고, 지리적 위치에 따른 의존성과 계절 패턴을 함께 설명한다.[^p1]

통계 방법의 응용은 제조와 영상 자료로도 이어진다. 웨이퍼(반도체 소자를 만드는 공정의 바탕으로 쓰는 얇은 판) 지도의 무늬를 군집으로 나누고, 새 자료가 들어올 때 그 구조를 갱신하는 학습 방법과 관리도(공정의 관측값을 정해진 기준과 비교해 변화를 감시하는 도표)를 제안했다.[^p6] 영상 분석에서는 잡음(관심 있는 변화에 섞여 들어온 불필요한 변동)에 해당할 가능성이 있는 점을 분리해 이동 경로 사이의 거리를 계산하고,[^p7] 영상에서 보행자의 현재 위치와 미래 경로를 직접 예측하는 모형을 연구한다.[^p8]

## 주요 연구 주제

### 1. 지역별 차이와 영이 많은 자료를 다루는 통계 모형

한 지역의 관측이 다른 지역과 관련되는 공간 의존성과, 관측값이 영인 경우가 많은 자료를 함께 다룬다. 진드기 분포 연구는 존재 확률과 양의 개체 수를 나누고 지리적 위치를 반영하는 새 모형을 제안한다(대표 논문 1).[^p1] 온도와 자살 사건 수의 관계를 분석한 연구도 발생 여부와 양의 수를 나누며, 지역별 하위 집단을 찾는 모형을 개발한다(대표 논문 3).[^p3]

### 2. 시간에 따라 바뀌는 관계와 지연 효과

환경 요인의 영향이 나타나는 시간 지연과, 관계 자체가 시간에 따라 달라지는 문제를 모형화한다. 변화점이 있는 메타분석 모형으로 시간 구간의 구조와 특이한 관측값을 함께 다루고(대표 논문 2),[^p2] 환경 노출의 크기·지연·시간이 단순히 더해지지 않는 상호작용을 표현하는 계층 베이지안 방법과 계산 절차를 개발한다(대표 논문 4).[^p4]

### 3. 여러 변수의 시간 곡선을 함께 묶는 방법

지역의 특성과 여러 오염물질의 계절 곡선을 함께 사용해 지역들을 군집으로 묶는다. 비모수 베이지안 잠재요인 모형을 제안하고 시간 의존성을 포함하도록 확장했으며, 모의 자료와 캐나다 도시의 대기오염 자료로 방법을 살폈다(대표 논문 5).[^p5]

### 4. 제조 품질과 영상 속 이동 경로 분석

반도체 제조에서는 새 웨이퍼 자료가 들어올 때 무늬의 군집 구조를 갱신하고, 군집별 비율 변화와 공정 이상을 감시한다(대표 논문 6).[^p6] 영상 속 경로 분석에서는 잡음의 영향을 줄이는 거리 계산과 검색 알고리즘(문제 해결을 위해 정한 계산 절차)을 개발하고(대표 논문 7),[^p7] 보행자를 찾아 연결하면서 미래 위치까지 함께 예측하는 모형을 제안한다(대표 논문 8).[^p8]

## 대표 논문

정연승 교수가 KAIST 소속 저자로 참여한 2021–2026년 논문 가운데 초록이 있는 출판 논문을 연구 갈래에 따라 골랐다. 마지막 저자·교신저자 논문과 최근 방법론 논문을 우선하고 영상 분석 연구도 함께 담았다. “쉽게 말하면” 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Spatial nonparametric Bayesian Poisson hurdle model for analyzing zero-inflated tick data](https://doi.org/10.1007/s42952-026-00390-2) · Journal of the Korean Statistical Society | 진드기가 관측되는지와 관측됐을 때의 개체 수를 나누어 분석하는 새 베이지안 모형이다. 지역 사이의 공간 의존성과 환경 특성을 함께 반영해 계절 패턴과 지역별 군집을 설명한다. 공간 관계를 넣지 않은 비교 모형보다 자료 적합도가 나았다고 보고한다.[^p1] | 1저자 Jinsu Park, 마지막·교신저자 Yeonseung Chung |
| 2 | 2026 | [Nonparametric Bayesian Meta‐Analysis Model With Change Point Detection: A Case Study on Time‐Varying Temperature–Mortality Associations](https://doi.org/10.1002/sim.70506) · Statistics in Medicine | 온도와 사망의 관계가 시간에 따라 직선적으로 변한다는 가정 대신, 관계가 달라지는 시간 구간을 찾는 새 메타분석 모형을 제안한다. 지역과 시기별 관계를 함께 모으고 특이한 관측값의 영향도 다루며, 모의 자료와 일본 자료로 방법을 살폈다.[^p2] | 1저자 Daewon Yang, 마지막·교신저자 Yeonseung Chung |
| 3 | 2025 | [Nonparametric Bayesian Poisson hurdle random effects model: an application to temperature–suicide association study](https://doi.org/10.1007/s10651-025-00655-9) · Environmental and Ecological Statistics | 사건 수가 영인 경우가 많은 자료를 발생 여부와 양의 사건 수로 나누는 새 모형이다. 온도와 자살 사건 수의 관계가 지역마다 다른 점을 다루고, 지역 특성과 관계의 차이를 함께 이용해 하위 집단을 찾는다. 모의 연구와 일본 자료에 적용해 방법을 보였다.[^p3] | 1저자 Jinsu Park, 마지막·교신저자 Yeonseung Chung |
| 4 | 2025 | [Bayesian hierarchical time-varying distributed lag nonlinear model: applications in the short-term association between ambient temperature and daily confirmed cases of COVID-19](https://doi.org/10.1080/02664763.2025.2577659) · Journal of Applied Statistics | 환경 노출의 크기와 영향이 나타나는 지연 시간, 관측 시점의 관계를 함께 다루는 새 계층 베이지안 방법이다. 이 관계들이 단순히 더해지지 않는 상호작용을 모형에 넣고 추정 계산 절차를 개발했다. 모의 자료와 미국의 온도·감염 발생 자료로 방법을 살폈다.[^p4] | 1저자 Dongu Han, 공동저자 Yeonseung Chung, 마지막 저자 Taeryon Choi |
| 5 | 2022 | [Non-Parametric Bayesian Covariate-Dependent Multivariate Functional Clustering: An Application to Time-Series Data for Multiple Air Pollutants](https://doi.org/10.1111/rssc.12589) · Journal of the Royal Statistical Society Series C (Applied Statistics) | 여러 오염물질의 계절 곡선이 비슷한 지역을 묶되, 지역 특성도 함께 반영하는 새 비모수 베이지안 모형이다. 잠재요인을 이용하는 군집화 방법을 제안하고 시간 의존성도 포함하도록 확장했다. 모의 자료와 캐나다 도시의 오염물질 농도 자료에 적용했다.[^p5] | 1저자 Daewon Yang, 마지막·교신저자 Yeonseung Chung |
| 6 | 2025 | [Profile monitoring via a nonparametric Bayesian online learning framework: Application to wafer map data in the semiconductor manufacturing industry](https://doi.org/10.1080/00224065.2025.2528853) · Journal of Quality Technology | 반도체 웨이퍼 지도의 무늬를 군집으로 묶고 새 자료가 들어올 때 구조를 갱신하는 학습 알고리즘을 제안한다. 군집별 평균 무늬를 추정하고 각 군집의 비율 변화를 감시하는 관리도를 함께 사용해 공정 변화를 찾는다.[^p6] | 1저자 Daewon Yang, 마지막·교신저자 Yeonseung Chung |
| 7 | 2024 | [Noise-Tolerant Trajectory Distance Computation in the Presence of Inherent Noise for Video Surveillance Applications](https://doi.org/10.1109/access.2024.3422098) · IEEE Access | 이동 경로에서 잡음에 해당할 가능성이 있는 점을 별도 공간 구조에 두고 경로 사이 거리를 계산하는 방법이다. 별도의 잡음 검출 단계 없이 거리 계산과 경로 검색을 수행하는 새 구조와 알고리즘을 제안하고 실제 영상 자료로도 살폈다.[^p7] | 1저자 Yongjin Kwon, 마지막 저자 Yeonseung Chung |
| 8 | 2025 | [PredDETR: An End-to-End Transformer-Based Model for One-Stage Pedestrian Trajectory Prediction](https://doi.org/10.1109/avss65446.2025.11149937) · IEEE International Conference on Advanced Video and Signal Based Surveillance (AVSS) | 과거 영상들을 입력받아 여러 보행자의 미래 경로를 직접 예측하는 모형이다. 연속 장면에서 같은 사람의 위치를 연결하는 작업과 미래 위치 예측을 함께 수행하며, 기존의 한 단계 예측 방법과 비교해 모형을 평가했다.[^p8] | 1저자 Yongjin Kwon, 마지막 저자 Yeonseung Chung |

## 교수와 전문 분야

정연승 교수(Yeonseung Chung)는 KAIST 수리과학과 교수이며, 학과는 전문 분야를 베이지안 통계와 응용통계로 적는다.[^dept] 고려대학교 통계학 학사(2000), 미국 노스캐롤라이나대학교 채플힐 생물통계학 석사(2005년 5월)와 박사(2009년 5월)를 받았다. 박사 논문은 변수에 따라 달라지는 분포를 비모수 베이지안 방법으로 모형화하는 추론을 다뤘다.[^about]

누리집 경력표는 하버드대학교 생물통계학 박사후연구원(2008년 9월–2010년 1월)과 Research Associate(2010년 1–12월), KAIST 수리과학과 조교수(2011년 1월–2017년 2월)와 2017년 3월부터의 부교수 경력을 적는다.[^about] 최근 방법론 논문의 전문성은 지역별 차이를 반영하는 유연한 통계 모형, 시간 변화와 지연 효과의 추정, 여러 변수의 곡선 자료 분석, 순차적으로 들어오는 자료의 품질 감시에 걸쳐 있다.[^p1][^p2][^p4][^p5][^p6]

## 응용 분야

환경 분야에서는 진드기의 공간·계절 분포와 여러 대기오염물질의 변화 곡선을 분석한다.[^p1][^p5] 보건 자료를 다룬 방법론 논문은 온도와 사망·자살 사건 수의 관계, 온도와 감염 발생의 단기 관계를 예시로 사용한다.[^p2][^p3][^p4] 제조 분야에서는 웨이퍼 지도 무늬와 반도체 공정의 이상을 감시하고,[^p6] 영상 분야에서는 잡음이 있는 이동 경로를 검색하거나 보행자의 미래 경로를 예측한다.[^p7][^p8]

## 구성원

누리집 Lab Members의 현재 구성원은 박사과정 3명과 석사과정 2명이다. 과정은 게시 표기대로 옮겼다.[^members] “대표 논문 참여”는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Kisung Sim (심기성) | 박사과정 | 1, 3 |
| Daewon Yang (양대원) | 박사과정 | 1, 2, 3, 5, 6 |
| Yongjin Kwon (권용진) | 박사과정 | 7, 8 |
| Taeyeon Kim (김태연) | 석사과정 |  |
| Jaemin Oh (오재민) | 석사과정 |  |

## 졸업생과 이전 구성원

누리집 Lab Members의 졸업생은 박사 4명과 석사 2명이다. 학위 논문과 진로는 누리집 표기대로 옮겼다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Gyuseok Sim (심규석) | 박사 | Samsung Fire & Marine Insurance | Nonparametric Bayesian multivariate meta-regression: an application in environmental epidemiology |
| Heesang Noh (노희상) | 박사 | Samsung Electronics | Bayesian latent factor regression for multivariate functional data analysis |
| Jaeeun Yu (유재은) | 박사 | Samsung Electronics | Nonparametric Bayesian functional meta-regression: an application in environmental epidemiology |
| Jinsu Park (박진수) | 박사 | KAIST Institute of Natural Science Research Faculty (Post-Doc.) | Nonparametric Bayesian functional two-part random effects model |
| Bitna Cho (조빛나) | 석사 |  |  |
| Nomirovska, Alina | 석사 |  |  |

## 최근 논문 목록 (2021–2026)

정연승 교수가 저자로 참여한 14편이다. 교수 개인의 저작 목록이며, 연도는 등록 서지의 출판 연도다. 제목·저자·발표처는 등록 서지 표기를 따르고, 사전 공개본 2편은 발표처 뒤에 “사전 공개본”으로 표시했다.[^bib]

**2026**

- Seungone Kim; Dongkeun Yoon; Kiril Gashteovski; Juyoung Suk; Jinheon Baek; Pranjal Aggarwal; Ian Wu; Viktor Zaverkin; Spase Petkoski; Daniel R. Schrider; Ilija Dukovski; Francesco Santini; B. Mitreska; Yong Jeong; Kyeongha Kwon; Young Min Sim; Dragana Manasova; Arthur Porto; Biljana Mojsoska; Makoto Takamoto; Marko Shuntov; Ruoqi Liu; Hyunjoo J. Lee; Niyazi Ulaş Dinç; Yehhyun Jo; Sunkyu Han; Chungwoo Lee; Hui-Shan Li; Esther H. R. Tsai; Ergün Şimşek; Khushboo Shafi; Yeonseung Chung; Jihye Park; Aleksandar Shulevski; Henrik Christiansen; Yoosang Son; Elly Knight; Amanda Montoya; Jeongyoun Ahn; Christian Langkammer; Heera Moon; Changwon Yoon; Nikola Stikov; Mooseok Jang; Edward Choi; Junhan Kim; Yeon Sik Jung; Woo Youn Kim; Jae Kyoung Kim; Ishraq Md Anjum; Hyun Uk Kim; Drew Bridges; Carolin Lawrence; Xiang Yue; Alice Oh; Akari Asai; Sean Welleck; Graham Neubig. "On the limits and opportunities of AI reviewers: Reviewing the reviews of Nature-family papers with 45 expert scientists". *Research Square (사전 공개본); DOI <https://doi.org/10.21203/rs.3.rs-10896922/v1>*.
- Jinsu Park; Kisung Sim; Hee Il Lee; Seong Yoon Kim; Jong‐Hun Kim; Ah-Young Lim; Daewon Yang; Yeonseung Chung. "Spatial nonparametric Bayesian Poisson hurdle model for analyzing zero-inflated tick data". *Journal of the Korean Statistical Society; DOI <https://doi.org/10.1007/s42952-026-00390-2>*.
- 정지섭; Daewon Yang; Whanhee Lee; Yejin Kim; Yeonseung Chung. "Bayesian kernel machine meta-regression: an application in environmental epidemiology". *Research Square (사전 공개본); DOI <https://doi.org/10.21203/rs.3.rs-10458547/v1>*.
- Daewon Yang; Taeryon Choi; Jinsu Park; Hohyun Jung; Yoonhee Kim; Masahiro Hashizume; Yeonseung Chung. "Nonparametric Bayesian Meta‐Analysis Model With Change Point Detection: A Case Study on Time‐Varying Temperature–Mortality Associations". *Statistics in Medicine; DOI <https://doi.org/10.1002/sim.70506>*.

**2025**

- Dongu Han; Kiljae Lee; Yeonseung Chung; Genya Kobayashi; Taeryon Choi. "Bayesian hierarchical time-varying distributed lag nonlinear model: applications in the short-term association between ambient temperature and daily confirmed cases of COVID-19". *Journal of Applied Statistics; DOI <https://doi.org/10.1080/02664763.2025.2577659>*.
- Daewon Yang; Jinsu Park; Hohyun Jung; Yeonseung Chung. "Profile monitoring via a nonparametric Bayesian online learning framework: Application to wafer map data in the semiconductor manufacturing industry". *Journal of Quality Technology; DOI <https://doi.org/10.1080/00224065.2025.2528853>*.
- Yongjin Kwon; Sungchan Oh; Jin-Young Moon; Yeonseung Chung. "PredDETR: An End-to-End Transformer-Based Model for One-Stage Pedestrian Trajectory Prediction". *IEEE International Conference on Advanced Video and Signal Based Surveillance (AVSS); DOI <https://doi.org/10.1109/avss65446.2025.11149937>*.
- Seoyeong Ahn; Ayoung Kim; Yeonseung Chung; Cinoo Kang; Sooyoung Kim; Dohoon Kwon; Jiwoo Park; Jieun Oh; Jinah Park; Jeongmin Moon; In-Sung Song; Jieun Min; Hyung Joo Lee; Ho Kim; Whanhee Lee. "Nationwide Machine Learning-Ensemble PM2.5 Mapping Prediction and Forecasting Models in South Korea with High Spatiotemporal Resolution and Health Risk Estimation-Based Evaluations". *Environment & Health; DOI <https://doi.org/10.1021/envhealth.4c00201>*.
- Jinsu Park; Kisung Sim; Daewon Yang; Yoonhee Kim; Masahiro Hashizume; Yeonseung Chung. "Nonparametric Bayesian Poisson hurdle random effects model: an application to temperature–suicide association study". *Environmental and Ecological Statistics; DOI <https://doi.org/10.1007/s10651-025-00655-9>*.

**2024**

- Yongjin Kwon; Jinyoung Moon; Yeonseung Chung. "Noise-Tolerant Trajectory Distance Computation in the Presence of Inherent Noise for Video Surveillance Applications". *IEEE Access; DOI <https://doi.org/10.1109/access.2024.3422098>*.

**2023**

- Daewon Yang; Jinsu Park; Hayang Park; Sungki Hong; Jongmin Kim; Seonghui Huh; Eunkyung Kim; Jaeyong Jeong; Yeonseung Chung. "Robust control chart based on mixed-effects modeling framework: A case study in NAND flash memory industry". *Quality Engineering; DOI <https://doi.org/10.1080/08982112.2023.2251570>*.

**2022**

- Daewon Yang; Taeryon Choi; Éric Lavigne; Yeonseung Chung. "Non-Parametric Bayesian Covariate-Dependent Multivariate Functional Clustering: An Application to Time-Series Data for Multiple Air Pollutants". *Journal of the Royal Statistical Society Series C (Applied Statistics); DOI <https://doi.org/10.1111/rssc.12589>*.

**2021**

- Jaehong Yoon; Ji‐Hwan Kim; Yeonseung Chung; Jinsu Park; Glorian Sorensen; Seung‐Sup Kim. "Gender differences in under-reporting hiring discrimination in Korea: a machine learning approach". *Epidemiology and Health; DOI <https://doi.org/10.4178/epih.e2021099>*.
- Ah-Young Lim; Hae‐Kwan Cheong; Yeonseung Chung; Kisung Sim; Jong‐Hun Kim. "Mosquito abundance in relation to extremely high temperatures in urban and rural areas of Incheon Metropolitan City, South Korea from 2015 to 2020: an observational study". *Parasites & Vectors; DOI <https://doi.org/10.1186/s13071-021-05071-z>*.

## 과제

교수 개인의 연구비 목록 가운데 수행 기간이 2021-10-13–2026-10-13과 겹치는 반도체 생산 과제다. 역할·지원·기간·금액은 누리집 표기대로 옮겼다.[^research]

- Two-phase sampling to improve the prediction accuracy and the detection rate for the anomaly in semi-conductor production (역할 Co-Principle Investigator; 지원 Samsung Electronics (Device Solution: Semiconductor Business); 기간 9/01/2018-8/31/2023; 연구비 $4,235,385 total)

## 연락과 위치

- 주소: 34141 대전광역시 유성구 대학로 291 KAIST[^home]
- 교수 연구실: E2 #3214. 학과 표기는 산업경영학동 3214이다.[^home][^dept]
- 구성원 연구실: E2 #3215[^members]
- 기관 전화: +82-42-350-7304[^home]
[^dept]: KAIST 수리과학과, 교수 목록의 정연승 항목. <https://mathsci.kaist.ac.kr/home/people/professor/> 관측 2026-11-07.
[^home]: Yeonseung Chung, 첫 화면의 Research interests·Contact Information. <https://sites.google.com/view/yeonseungchung> 관측 2026-11-07.
[^about]: Yeonseung Chung, About Me의 Education·Professional experience. <https://sites.google.com/view/yeonseungchung/top/about-me> 관측 2026-11-07.
[^members]: Yeonseung Chung, Lab Members의 CURRENT MEMBERS·ALUMNI. <https://sites.google.com/view/yeonseungchung/top/lab-members> 관측 2026-11-07.
[^research]: Yeonseung Chung, Research의 RESEARCH GRANTS. <https://sites.google.com/view/yeonseungchung/top/research> 관측 2026-11-07.
[^bib]: OpenAlex, Yeonseung Chung 저자의 2021–2026년 등록 저작 서지·초록. <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5045926685,publication_year:2021-2026> 관측 2026-11-07.
[^p1]: J. Park 외, Y. Chung, Journal of the Korean Statistical Society (2026). <https://doi.org/10.1007/s42952-026-00390-2> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W7211882503> 관측 2026-11-07.
[^p2]: D. Yang 외, Y. Chung, Statistics in Medicine (2026). <https://doi.org/10.1002/sim.70506> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W7147197223> 관측 2026-11-07.
[^p3]: J. Park 외, Y. Chung, Environmental and Ecological Statistics (2025). <https://doi.org/10.1007/s10651-025-00655-9> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W4409166728> 관측 2026-11-07.
[^p4]: D. Han 외, T. Choi, Journal of Applied Statistics (2025). <https://doi.org/10.1080/02664763.2025.2577659> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W4415508164> 관측 2026-11-07.
[^p5]: D. Yang, T. Choi, É. Lavigne, Y. Chung, Journal of the Royal Statistical Society Series C (Applied Statistics) (2022). <https://doi.org/10.1111/rssc.12589> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W4293547557> 관측 2026-11-07.
[^p6]: D. Yang, J. Park, H. Jung, Y. Chung, Journal of Quality Technology (2025). <https://doi.org/10.1080/00224065.2025.2528853> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W4413211203> 관측 2026-11-07.
[^p7]: Y. Kwon, J. Moon, Y. Chung, IEEE Access (2024). <https://doi.org/10.1109/access.2024.3422098> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W4400228838> 관측 2026-11-07.
[^p8]: Y. Kwon, S. Oh, J.-Y. Moon, Y. Chung, IEEE International Conference on Advanced Video and Signal Based Surveillance (AVSS) (2025). <https://doi.org/10.1109/avss65446.2025.11149937> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W4414165958> 관측 2026-11-07.

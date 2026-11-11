# Atmospheric Chemistry Modeling Group

**서울대학교 자연과학대학 지구환경과학부 · 박록진 교수**

- 분야: 대기화학, 대기오염 모델링, 위성 관측, 화학과 기후의 상호작용, 탄소 순환
- 대분야: 에너지·환경·지구, 화학
- 태그: 위성 원격탐사[^sat], 분무·에어로졸[^dept][^pm], 기후·극한 기상[^climate]
- 홈페이지: <http://airchem.snu.ac.kr/acmg/>
- 근거와 출처: [Atmospheric Chemistry Modeling Group 근거 페이지](airchem-sources.md)

> 대기 속 오염물질이 생기고 이동하고 사라지는 과정을 계산하며, 위성·지상·항공 관측을 연결해 대기질과 기후, 탄소의 흐름을 연구하는 연구실이다.[^dept][^sat][^climate][^campaign]

## 무엇을 연구하나

대기화학(대기 속 물질의 성분과 화학적 변화를 다루는 분야)을 연구하며, 미량기체(대기에서 차지하는 비율이 작은 기체 성분)와 에어로졸(기체 속에 떠 있는 작은 액체·고체 입자)이 어떻게 생기고 사라지며 이동하는지 정량적으로 밝힌다. 이를 위해 화학 수송 모형(물질의 화학적 변화와 대기의 흐름에 따른 이동을 함께 계산하는 모형)과 기후 모형을 개발하고, 대기 성분의 변화가 생태계와 기후에 주는 영향을 연구한다.[^dept]

위성 원격탐사에서는 우주에서 측정한 빛으로 대기 속 기체의 양을 알아내는 계산 방법을 개발한다. GEMS(Geostationary Environment Monitoring Spectrometer)는 빛을 파장별로 나눠 대기 성분을 재는 위성 장비다. 연구실은 그 산출 결과를 다른 위성과 지상·항공 관측으로 평가한다.[^sat] 대표 논문 3은 빛을 분석할 때의 기준과 파장 범위를 달리해 기체량 산출을 평가했고, 대표 논문 2는 하루 중 반복 관측이 배출량 추정에 주는 이점이 계절에 따라 달라짐을 보였다. 여름에는 관측의 불확실성 때문에 관측 횟수를 늘려도 추정이 나아지지 않거나 오히려 악화될 수 있었다.[^p3][^p2]

입자 오염을 다룰 때는 물질의 생성 반응과 대기의 수직 혼합을 함께 본다. 연구실은 상대습도(같은 온도에서 공기가 수증기를 최대로 포함할 수 있는 양에 대한 현재 수증기량의 비율)의 변화 이력에 따른 입자의 고체·액체 상태를 모형에 반영하고, 관측과 비교하는 연구를 한다.[^pm] 대표 논문 4는 혼합층(불규칙한 공기 움직임으로 성질이 위아래로 섞이는 대기층)의 높이를 계산하는 방법을 제안해 기체·입자 농도(혼합물 안에 특정 성분이 어느 정도 들어 있는지를 나타내는 양)의 편향을 줄였다. 대표 논문 5와 7은 공기 중 유기물(탄소를 주요 골격으로 하는 화합물)에서 입자가 만들어지는 과정과 그 계산 방법을 다룬다.[^p4][^p5][^p7]

기후 연구는 대기화학과 기상 변화의 상호작용, 동아시아의 겨울철 오염 예측, 탄소 순환으로 이어진다.[^climate] 대표 논문 6은 화학 계산과 기상 계산을 결합해 기체·입자가 빛과 열의 전달에 미치는 영향을 계산하는 모형을 개발했다.[^p6] 대표 논문 1은 위성 관측과 대기 수송 계산을 결합해 동아시아 육지와 바다의 탄소 교환을 추정했다. 자연의 탄소 흡수원이 화석연료 배출의 일부만 상쇄해 이 지역 전체로는 대기에 탄소를 내보내고 있다는 결과다.[^p1]

## 주요 연구 주제

### 위성 관측에서 오염기체의 양과 배출량 알아내기

위성으로 측정한 빛을 대기 속 기체의 양으로 바꾸는 산출 알고리즘(입력 자료에서 결과를 얻기 위해 정한 계산 절차)을 개발하고, 다른 관측과 비교해 평가한다. 연구실은 이 자료로 오염물질의 배출과 이동을 이해하고 대기질 예측을 개선하려 한다.[^sat] 대표 논문 2는 위성의 반복 관측을 모두 쓸 때와 하루 중 일부만 쓸 때의 배출량 추정을 비교했다. 대표 논문 3은 위성 기체량의 공간 분포뿐 아니라 월별·시간별 변화가 관측 자료 사이에서 얼마나 일치하는지 살폈다.[^p2][^p3]

### 입자가 생기는 반응과 공기 중 혼합 계산하기

한·중 공동 연구에서는 관측과 여러 모형의 비교로 입자 오염의 화학반응·이동 특성을 분석하고, 유기 입자 생성에 관련된 반응 계산을 개선한다.[^pm] 대표 논문 5는 실험실 반응 자료에 맞춘 새 입자 생성 표현을 대기 모형에 넣어 관측과 비교했다. 대표 논문 7은 서로 다른 입자 생성 계산법을 비교해, 전구물질(뒤이은 반응에서 다른 물질을 만드는 출발 물질)과 공기 중에서 계속되는 화학적 변화의 중요성을 살폈다.[^p5][^p7]

### 화학과 기후, 탄소 순환의 연결 계산하기

연구실은 기후에 영향을 주는 외부 조건을 되돌려도 기후가 원래 상태로 돌아오는지, 비가역적 변화가 동아시아와 지구 전체에 어떻게 나타나는지를 연구한다. 또한 지구시스템 모형(대기·해양·육지 등의 변화와 상호작용을 함께 계산하는 모형)으로 동아시아 탄소 순환의 불확실성을 진단하고 이산화탄소 예측을 개선하려 한다.[^climate] 대표 논문 6은 화학과 기상의 결합 모형을 관측과 비교했고, 대표 논문 1은 위성 관측을 이용해 육지와 바다의 탄소 흡수·방출을 추정했다.[^p6][^p1]

### 공동 관측을 지원하는 대기질 예측

연구실이 참여하는 국제 공동 관측은 위성, 항공기, 선박, 지상 관측망과 전지구·지역 화학 수송 모형을 함께 사용한다. 모형으로 일별 대기질을 예측해 연구 항공기의 비행 경로 조정과 관측 결과의 종합 분석을 지원하며, 겨울철 입자의 이차 생성(기체가 대기에서 반응해 입자로 바뀌는 과정)과 아시아 오염원, 위성 산출 자료의 평가를 연구 대상으로 삼는다.[^campaign]

## 대표 논문

서울대 재직 시기의 2021–2026년 논문 가운데 연구 갈래와 최근 연구를 함께 보여 주는 7편이다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 주요 저자 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2026 | [Top-down estimate of regional carbon sinks over East Asia for 2010–2019 using satellite observations](https://doi.org/10.5194/acp-26-6869-2026) · Atmospheric Chemistry and Physics[^p1] | 첫 저자 Mina Kim, 박록진 공저 | 위성 관측과 대기 모형을 결합해 동아시아 육지와 바다의 탄소 흡수·방출을 추정했다. 자연의 흡수량을 반영해도 지역 전체의 탄소 배출을 상쇄하지 못했다. |
| 2 | 2026 | [Do GEMS geostationary satellite observations of tropospheric NO2 always improve NOx emission estimates and related air quality modelling?](https://doi.org/10.5194/acp-26-12049-2026) · Atmospheric Chemistry and Physics[^p2] | 첫 저자 Fei Yao, 마지막 저자 Rokjin J. Park | 하루 중 반복하는 위성 관측으로 오염기체 배출량을 추정했다. 여름 이외 계절에는 유용했지만 여름에는 불확실성 때문에 개선 효과가 없거나 나빠질 수 있었다. |
| 3 | 2024 | [First evaluation of the GEMS glyoxal products against TROPOMI and ground-based measurements](https://doi.org/10.5194/amt-17-6369-2024) · Atmospheric Measurement Techniques[^p3] | 첫 저자 Eunjo S. Ha, 박록진 공저 | 위성에서 글리옥살 기체의 양을 산출하는 설정을 평가했다. 다른 위성·지상 관측과 공간 분포와 시간 변화를 비교하고 계절에 따라 차이가 생기는 원인을 살폈다. |
| 4 | 2024 | [A mixed layer height parameterization in a 3-D chemical transport model: Implications for gas and aerosol simulations](https://doi.org/10.1016/j.scitotenv.2024.176838) · Science of The Total Environment[^p4] | 첫 저자 Hyeonmin Kim, 박록진 공저 | 밤에 지표 근처 오염물질을 과다하게 계산하는 문제를 줄이도록, 공기가 위아래로 섞이는 높이의 계산법을 제안했다. 이를 반영하자 기체와 입자 농도가 관측에 가까워졌다. |
| 5 | 2023 | [A Scheme for Representing Aromatic Secondary Organic Aerosols in Chemical Transport Models: Application to Source Attribution of Organic Aerosols Over South Korea During the KORUS-AQ Campaign](https://doi.org/10.1029/2022jd037257) · Journal of Geophysical Research: Atmospheres[^p5] | 첫 저자 Jared F. Brewer, 박록진 공저 | 실험실 반응 자료에 맞춰 유기 기체에서 입자가 생기는 새 계산 방식을 만들었다. 대기 모형에 넣자 한국의 항공·지상 관측을 기존 방식보다 잘 재현했다. |
| 6 | 2022 | [A New Chemistry-Climate Model GRIMs-CCM: Model Evaluation of Interactive Chemistry-Meteorology Simulations](https://doi.org/10.1007/s13143-022-00281-6) · Asia-Pacific Journal of Atmospheric Sciences[^p6] | 첫 저자 Seungun Lee, 박록진 공저 | 대기화학과 기상을 서로 연결하는 모형을 만들고 기체·입자 관측과 비교했다. 여러 공간·계절 변화를 재현했지만 토양 먼지 입자에는 편향이 남았다. |
| 7 | 2022 | [Evaluation of Secondary Organic Aerosol (SOA) Simulations for Seoul, Korea](https://doi.org/10.1029/2021ms002760) · Journal of Advances in Modeling Earth Systems[^p7] | 첫 저자 Yujin J. Oak, 박록진 공저 | 서울의 항공·지상 관측으로 유기 입자 생성 계산법 네 가지를 비교했다. 출발 물질과 공기 중 화학적 변화가 중요했고, 방법과 계절에 따라 계산 오차가 달랐다. |

## 교수와 전문 분야

박록진은 서울대학교 자연과학대학 지구환경과학부 교수이자 학부장이다. 서울대학교 대기과학 학사(1995), University of Maryland 대기과학 박사(2001)이며, Harvard University Research Associate(2001–2007)를 거쳐 2007년부터 서울대학교에서 조교수·부교수·교수로 재직한 경력을 적는다. 학과 소개에는 2019년부터 서울대학교 미세먼지연구소 소장 경력도 올라 있다.[^dept]

학과가 밝힌 전공은 대기화학과 대기오염 모델링이다. 전지구·지역 대기화학 모형과 기후 모형을 개발해 미량기체·입자의 생성과 소멸, 이동 및 지구생태계·기후 영향을 정량적으로 연구한다.[^dept] 최근 논문에서 드러나는 전문 분야는 위성 관측을 이용한 배출량·탄소 교환 추정, 위성 기체량 산출과 평가, 대기 혼합·유기 입자 생성 계산, 화학과 기상의 결합 모형이다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7]

## 응용 분야

연구실은 위성 자료를 통한 아시아 오염물질 배출과 이동 파악, 대기질 예측 개선을 목표로 한다.[^sat] 한·중 관측과 모형 비교는 오염 원인 규명과 예측 모형 개선으로 이어지며, 겨울철 오염 예측은 배출 저감 정책과 연결된다. 탄소 순환 계산은 온실가스 감축에 필요한 동아시아 이산화탄소의 분포·교환 이해를 목표로 한다.[^pm][^climate] 국제 공동 관측에서는 일별 예측으로 관측 항공기의 경로 조정과 관측 분석을 지원한다.[^campaign]

## 구성원

2026년 11월 11일 Research Fellow와 Graduate Student 쪽 기준으로 연구원 구획 3명과 대학원생 8명이다. 대학원생은 박사과정 6명과 석사과정 2명이다.[^members][^students] 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Changsik Lim | 연구원 | atlasago@snu.ac.kr |  |
| Seungun Lee | 연구원 | hb3099@snu.ac.kr | 6 |
| Jaein Jeong | 연구부교수 | ss99@snu.ac.kr |  |
| Eunjo Ha | 박사과정 | gkdmswh23@snu.ac.kr |  |
| Gitaek Lee | 박사과정 | gitaek2@snu.ac.kr |  |
| Mina Kim | 박사과정 | kma0603@snu.ac.kr | 1 |
| Sangik Oh | 박사과정 | ohsangik98@snu.ac.kr |  |
| Yujoo Jeong | 박사과정 | yjjeong@snu.ac.kr |  |
| Yoonbae Chung | 박사과정 | ybchung@snu.ac.kr |  |
| Yujin Seo | 석사과정 | yujin.seo@snu.ac.kr |  |
| Jingi Jung | 석사과정 | jjg2408@snu.ac.kr | 1 |

## 졸업생 진로

연구실 Alumni에 게시된 16명의 이름과 진로다. 진로는 연구실의 게시 표기다.[^alumni][^alumni1][^alumni2][^alumni3]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hyeonmin Kim |  | JIFRESSE, UCLA / NASA JPL |
| Eunlak Choi |  | Hana Bank |
| Haein Lee |  | Korea Sustainability Investing Forum |
| Sieun Lee |  | Hana Bank |
| Yujin Oak (옥유진) |  | Assistant Professor, UNIST |
| Byeonghyeon Gwak (곽병현) |  | 4D Solution Inc. |
| Hyung-Min Lee (이형민) |  | Korea Environment Institute |
| Hyeong-Ahn Kwon (권형안) |  | Assistant Professor, The University of Suwon |
| Gisu Seo (서지수) |  | Samsung Electronics |
| Jinkyul Choi (최진결) |  | NASA Postdoctoral Program (NPP) fellow at JPL |
| Duseong Jo (조두성) |  | Assistant Professor, Seoul National University |
| Minjoong Kim (김민중) |  | Associate Professor, Myongji University |
| Seungkyu Hong (홍승규) |  | Samsung Electronics |
| Hansol Lee (이한솔) |  | National Institute of Environmental Research |
| Bonyang Ku (구본양) |  | Korea Meteorological Administration |
| Sooya Bae (배수야) |  | Korea Institute of Atmospheric Prediction Systems |

## 최근 5년 논문 목록

연구실 Publications의 2021–2026년 구역에 게시된 논문·학술대회 논문이다. 연도 구역은 누리집의 표기를 따르며, 「in press」·「accepted」는 「게재 승인」을 함께 표시했다.[^pub2026][^pub2025][^pub2024][^pub2023][^pub2022][^pub2021]

**2026**

- 192. Gitaek T. Lee, Rokjin J. Park, Hyeong-Ahn Kwon, Jaein I. Jeong, Seungun Lee, Eunjo S. Ha, Yoonbae Chung, Cheol-Hee Kim, Soontae Kim, Chul Han Song, Chang-Keun Song, Jung‐Hun Woo, Glenn M. Wolfe, Jason St. Clair, Erin Delaria, Abby E. Sebol, Hyeonmin Kim, and Jhoon Kim Air mass factor sensitivity to a priori profiles in GEMS formaldehyde retrieval during the ASIA-AQ campaign, Atmospheric Environment (2026) 122255., DOI: https://doi.org/10.1016/j.atmosenv.2026.12225 DOI: https://doi.org/10.1016/j.atmosenv.2026.122255
- 191. Fei Yao, Paul I. Palmer, Xiaolin Wang, Yi Wang, Gitaek T. Lee, Haolin Wang, Liang Feng, Daven K. Henze, and Rokjin J. Park Do GEMS geostationary satellite observations of tropospheric NO₂ always improve NOₓ emission estimates and related air quality modelling? (2026), Atmospheric Chemistry and Physics, 26, 12049–12066, DOI: https://doi.org/10.5194/acp-26-12049-2026
- 190. Joon-Gu Jeon, Sang-Wook Yeh, Rokjin J. Park, Jaein Jeong, and Robert J. Allan Impact of near-term climate forcing on the Arctic Oscillation, Elem Sci Anth, 14: 1. DOI: https://doi.org/10.1525/elementa.2026.00009
- 189. Park, Do-Hyeon et al., Decrease in nucleated particles and cloud condensation nuclei observed across a range of environments, Environmental Science & Technology, DOI: 10.1021/acs.est.5c18035.
- 188. S.-Y. Kim, S.-W. Son, Y. Ming, D.-C. Hong, Xihui Gu, and R. J. Park Declining anthropogenic aerosols amplify Northern Hemisphere Hadley circulation weakening in the 21st century. Nat Commun 17, 3355 (2026). https://doi.org/10.1038/s41467-026-69990-0
- 187. Mina Kim, Rokjin J. Park, Jingi Jung, Sang-Ik Oh, Eunjo S. Ha, Jaein I. Jeong, and Sang-Wook Yeh Top-down estimate of regional carbon sinks over East Asia for 2010–2019 using satellite observations, ACP, in press. [게재 승인; 연도는 누리집 연도 구역] DOI: https://doi.org/10.5194/acp-26-6869-2026
- 186. Kim, Hyeonmin; Park, Rokjin; Jeong, Jaein; Choi, Enulak; Woo, Jung-Hun; Kim, Jinseok; Song, Chul H.; Yu, Jinhyeok; Han, Kyungman; Song, Chang-Keun; Cha, Yesol; Lee, Hyo-Jung; Kim, Cheol-Hee; Baek, Seunghee; Kim, Soontae; Jeong, Seongeun; Kim, Eunhye; Lee, Meehye; Chang , Lim-Seok; Crawford, James H., Ensemble-based source attribution of fine particulate matter over South Korea during the ASIA-AQ/SIJAQ campaign, Environ. Sci. Technology, 2026, 60, 12292-12303. DOI: https://doi.org/10.1021/acs.est.5c15003

**2025**

- 185. Seung-Hee Baek, Hyo-Jung Lee, Hyun-Young Jo, Cheol-Hee Kim, Min-Jun Park, Jong-Min Kim, Juseon Bak, Hanlim Lee, Yeonjin Jung, Junsung Park, Jung-Hun Woo, Jinseok Kim, Rokjin Park, Lim-Seok Chang, and Chang-Keun Song Long-range transport of short-lived nitrogen dioxide in East Asia, Science of the Total Environment 1006 (2025) 180850. DOI: https://doi.org/10.1016/j.scitotenv.2025.180850
- 184. Yong-Cheol Jeong, Yuxuan Wang, Wei Li, Hyeonmin Kim, Rokjin J. Park, and Mahmoudreza Momeni Modeling on the drought stress impact on the summertime biogenic isoprene emissions in South Korea, accepted in ACP. [게재 승인; 연도는 누리집 연도 구역] DOI: https://doi.org/10.5194/acp-25-15507-2025
- 183. Jeong, J.I., Park, R.J., and Yeh, S.-W. Future projections of winter haze events in northern East Asia under different Shared Socioeconomic Pathways (SSPs), Science of the total environment, 1004, https://doi.org/10.1016/j.scitotenv.2025.180805.
- 182. Hyeon-Kook Kim, EunRyoung Kim, Chang-Keun Song, Jae-Ho Choi, Ganghan Kim, Myong-In Lee, Yujin J. Oak, Rokjin J. Park, Ilhan Ryoo, Seung-Muk Yi, Kyung-Mi Lee, Hyeok-Gi Cheo, Kwon-Ho Jeon Comparative evaluation of surface-level PM2.5 modeling across Northeast Asia: relevance for regulatory and scientific applications, Environmental Pollution, Vol. 377, https://doi.org/10.1016/j.envpol.2025.126428
- 180. Kangho Bae, Chang-Keun Song, Michel Van Roozendael, Andreas Richter, Thomas Wagner, Alexis Merlaud, Gaia Pinardi, Martina M. Friedrich, Caroline Fayt, Ermioni Dimitropoulou, Kezia Lange, Tim Bosch, Bianca Zilker, Miriam Latsch, Lisa K. Behrens, Steffen Ziegler, Simona Ripperger-Lukosiunaite, Leon Kuhn, Bianca Lauster, Lucas Reischmann, Katharina Uhlmannsiek, Alexander Cede, Martin Tiefengraber, Manuel Gebetsberger, Rokjin J. Park, Hanlim Lee, Hyunkee Hong, Lim-Seok Chang, Kwonho Jeon Validation of GEMS operational v2.0 total column NO2 and HCHO during the GMAP/SIJAQ campaign, Science of the Total Environment, Vol. 974, https://doi.org/10.1016/j.scitotenv.2025.179190
- 179. Yeonsoo Cho, Hyeonmin Kim, Rokjin J. Park, Sang-Woo Kim Unprecedented East Siberian wildfires intensify Arctic snow darkening through enhanced poleward transport of black carbon, Science of The Total Environment, Vol. 961, https://doi.org/10.1016/j.scitotenv.2025.178423
- 178. Lim-Seok Chang, Soi Ahn, Min-Suk Bae, Seung Myung Park, Junsu Gil, Kwang-Rae Kim, Gangwoong Lee, Taehyoung Lee, Jung-Hun Woo, Rokjin Park, Hyeong-Ahn Kwon, Gyo-Hwang Choo, Chang-Keun Song Role of factors controlling diurnal variation of cold-season formaldehyde during Satellite Integrated Joint Monitoring of Air Quality 2021 campaign, Science of The Total Environment, Vol. 960, https://doi.org/10.1016/j.scitotenv.2024.178283
- 177. Tai-Long He, Glenn-Michael Oomen, Wenfu Tang, Idir Bouarar, Kelly Chance, Cathy Clerbaux, David P. Edwards, Henk Eskes, Benjamin Gaubert, Claire Granier, Marc Guevara, Daniel J. Jacob, Jennifer Kaiser, Jhoon Kim, Shobha Kondragunta, Xiong Liu, Eloise A. Marais, Kazuyuki Miyazaki, Rokjin Park, Vincent-Henri Peuch, Gabriele Pfister, Andreas Richter, Trissevgeni Stavrakou, Raid M. Suleiman, Alexander J. Turner, Ben Veihelmann, Zhao-Cheng Zeng, and Guy P. Brasseur Challenges and opportunities offered by geostationary space observations for air quality research and emission monitoring, BAMS, https://doi.org/10.1175/BAMS-D-23-0145.1
- 176. Yesol Cha, Jong-Jae Lee, Chul Han Song, Soontae Kim, Rokjin J. Park, Myong-In Lee, Jung-Hun Woo, Jae-Ho Choi, Kangho Bae, Jinhyeok Yu, Eunhye Kim, Hyeonmin Kim, Seung-Hee Lee, Jinseok Kim, Lim-Seok Chang, Kwon-ho Jeon, Chang-Keun Song Investigating uncertainties in air quality models used in GMAP/SIJAQ 2021 field campaign: General performance of different models and ensemble results, Atmospheric Environment Volume 340, 1 January 2025, 120896, https://doi.org/10.1016/j.atmosenv.2024.120896
- 175. Weitao Fu, Lei Zhu, Hyeong-Ahn Kwon, Rokjin J. Park, Gitaek T. Lee, Isabelle De Smedt, Song Liu, Xicheng Li, Yuyang Chen, Dongchuan Pu, Juan Li, Xiaoxing Zuo, Peng Zhang, Yali Li, Zhuoxian Yan, Xue Zhang, Jiaming Zhang, Xingyi Wu, Huizhong Shen, Jianhuai Ye, Chen Wang, Tzung-May Fu, Xin Yang Evaluating GEMS HCHO Retrievals With TROPOMI Product, Pandora Observations, and GEOS-Chem Simulations, Earth and Space Science, Vol. 12, https://doi.org/10.1029/2024EA003894

**2024**

- 174. Man-Hae Kim, Young-Suk Oh, Myoung-Hwan Ahn, Mina Kang, Hoyeon Shi, Rokjin Park, Sangik Oh , Sangwon Joo, Sang-Woo Kim Retrieving the Vertical Profile of Greenhouse Gas Using Fourier Transform Spectrometer (FTS) - Part II: Methane (CH4), Korean Society for Atmospheric Environment, Vol. 40, 10.5572/KOSAE.2024.40.3.361
- 173. Man-Hae Kim, Young-Suk Oh, Myoung-Hwan Ahn, Mina Kang, Hoyeon Shi, Rokjin Park, Mina Kim, Sangwon Joo, Sang-Woo Kim Retrieving the Vertical Profile of Greenhouse Gas Using Fourier Transform Spectrometer (FTS) - Part I: Carbon Dioxide (CO2), Korean Society for Atmospheric Environment, Vol. 40, 10.5572/KOSAE.2024.40.3.349
- 172. Haein Lee, Rokjin Park, Jaein Jeong Impact of Recent Meteorological Changes on Surface Ozone Increases in Seoul Metropolitan Area, Korean Society for Atmospheric Environment, Vol. 40, 10.5572/KOSAE.2024.40.4.467
- 171. Yeonsoo Cho, Jin-Ho Yoon, Jee-Hoon Jeong, Jong-Seong Kug, Baek-Min Kim, Hyungjun Kim, Rokjin J. Park, and Sang-Woo Kim Precipitation-induced abrupt decrease of Siberian wildfire in summer 2022 under continued warming, Environmental Research Letters, https://iopscience.iop.org/article/10.1088/1748-9326/ad5573
- 170. Min-Jun Park, Seung-Hee Baek, Hyo-Jung Lee, Hyun-Young Jo, Cheol-Hee Kim, Jin-Seok Kim, Jung-Hun Woo, Rokjin Park, Jong-Jae Lee, Chang-Keun Song, Jung-Woo Yoo, Lim-Seok Chang, Taehyoung Lee Inter-annual changes in transboundary air quality from KORUS-AQ 2016 to SIJAQ 2022 campaign periods and assessment of emission reduction strategies in Northeast Asia, Environmental Pollution, Vol. 363, https://doi.org/10.1016/j.envpol.2024.125114
- 169. Hyeonmin Kim, Rokjin J. Park, Song-you Hong, Do-Hyeon Park, Sang-Woo Kim, Yujin J. Oak, Xu Feng, Haipeng Lin, Tzung-May Fu A mixed layer height parameterization in a 3-D chemical transport model: Implications for gas and aerosol simulations, Science of The Total Environment, https://doi.org/10.1016/j.scitotenv.2024.176838
- 168. Oak, Y. J., Jacob, D. J., Balasus, N., Yang, L. H., Chong, H., Park, J., Lee, H., Lee, G. T., Ha, E. S., Park, R. J., Kwon, H.-A., Kim, J. A bias-corrected GEMS geostationary satellite product for nitrogen dioxide using machine learning to enforce consistency with the TROPOMI satellite instrument, Atmospheric Measurement Techniques, https://doi.org/10.5194/amt-17-5147-2024.
- 167. Kam, J., Min, S.-K., Kim, B.-H., Kim, Y.-H., Diaz, L. B., Kug, J.-S., Park, R. Climate models indicate compensating effects between anthropogenic greenhouse gases and aerosols on the 2022 Central Andes spring drought, Bulletin of the American Meteorological Society, 105(5). https://doi.org/10.1175/bams-d-23-0241.1, 2024.
- 166. Ha, E. S., Park, R. J., Kwon, H.-A., Lee, G. T., Lee, S. D., Shin, S., Lee, D.-W., Hong, H., Lerot, C., De Smedt, I., Hendrick, F., Irie, H. First evaluation of the GEMS glyoxal products against TROPOMI and ground-based measurements, Atmospheric Measurement Techniques, https://doi.org/10.5194/amt-17-6369-2024, 2024.
- 165. Jeong, Y.-C., Yeh, S.-W., Jeong, J.I., Park, R.J., Wang, Y. Existence of typical winter atmospheric circulation patterns leading to high PM2.5 concentration days in East Asia, Environmental Pollution, 348, 123829. DOI: https://doi.org/10.1016/j.envpol.2024.123829
- 164. Seung-Ha Lee, Ji-Seon Lee, Hyung-Min Lee, Hyeong-Ahn Kwon, Caroline R. Nowlan, Gonzalo González Abad, Rokjin J. Park, Ji-Hoon Park, Soyoung Kang, Hye-Jung Shin, Dai-Gon Kim, Jung-Min Park Understanding Ozone Formation and Carbonyl Contributions in the Seoul Metropolitan Area January 2024, Aerosol and Air Quality Research 24(1):230227, DOI: 10.4209/aaqr.230227
- 163. Gitaek T. Lee, Rokjin J. Park, Hyeong-Ahn Kwon, Eunjo S. Ha, Sieun D. Lee, Seunga Shin, Myoung-Hwan Ahn, Mina Kang, Yong-Sang Choi, Gyuyeon Kim, Dong-Won Lee, Deok-Rae Kim, Hyunkee Hong, Bavo Langerock, Corinne Vigouroux, Christophe Lerot, Francois Hendrick, Gaia Pinardi, Isabelle De Smedt, Michel Van Roozendael, Pucai Wang, Heesung Chong, Yeseul Cho, and Jhoon Kim First evaluation of the GEMS formaldehyde product against TROPOMI and ground-based column measurements during the in-orbit test period (2024), Atmospheric Chemistry and Physics, 24(8), 4733-4749, DOI: 10.5194/acp-24-4733-2024.
- 162. Jeong, J.I., Park, R.J., Song, C.-K., Yeh, S.-W., and Woo, J.-H. Quantitative analysis of winter PM2.5 reduction in South Korea, 2019/20 to 2021/22: Contributions of meteorology and emissions, Science of the total environment, 907, 168179. DOI: https://doi.org/10.1016/j.scitotenv.2023.168179

**2023**

- 161. Giyoon Lee, Jinho Ahn, Seung-Myung Park, Jonghan Moon, Rokjin J. Park, Min Sub Sim, Hanna Choi, Jinsoo Park, and Joon-Yong Ahn Sulfur isotope-based source apportionment and control mechanisms of PM2.5 sulfate in Seoul, South Korea during winter and early spring (2017–2020), Science of the Total Environment, 905, 167112. DOI: https://doi.org/10.1016/j.scitotenv.2023.167112
- 160. Hyeonmin Kim, Rokjin J. Park, Saewung Kim, Jaein I. Jeong, Daun Jeong, Xiao Fu and Seogju Cho Effect of nitryl chloride chemistry on air quality in South Korea during the KORUS-AQ campaign, Atmospheric Environment, Volume 312, 120045, https://doi.org/10.1016/j.atmosenv.2023.120045
- 159. Jeong, J.I., and Park, R.J. Can climate indices forecast daily variations of wintertime PM2.5 concentrations in East Asia?, Science of the total environment, (2023), 881, 163505. DOI: https://doi.org/10.1016/j.scitotenv.2023.163505
- 158. Brewer, J. F., D. J. Jacob, S. H. Jathar, Y. He, A. Akherati, S. Zhai, D. S. Jo, A. Hodzic, B. A. Nault, P. Campuzano-Jost, J. L., Jimenez, R. J. Park, Y. J. Oak, and H. Liao, A Scheme for Representing Aromatic Secondary Organic Aerosols in Chemical Transport Models: Application to Source Attribution of Organic Aerosols Over South Korea During the KORUS-AQ Campaign, (2023), Journal of Geophysical Research: Atmospheres, 128. DOI: https://doi.org/10.1029/2022jd037257
- 157. Bethany Sutherland, Sharon Burton, Chris A. Hostetler, Richard A. Ferrare, Johnathan Hair, Rokjin J. Park, Yujin J. Oak, Nicholas Meskhidze, Application of DIAL/HSRL and CATCH algorithm-based methodologies for surface PM2.5 concentrations during the KORUS-AQ campaign (2023), Atmospheric Environment. DOI: https://doi.org/10.1016/j.atmosenv.2023.119719
- 156. Jeong Y.C., Yeh S.W., Jeong J.I., Park R.J., Yoo C., Yoon J.H., Intrinsic atmospheric circulation patterns associated with high PM2.5 concentration days in South Korea during the cold season (2023), Science of the Total Environment, 863, 160878. DOI: https://doi.org/10.1016/j.scitotenv.2022.160878
- 155. Seohee H. Yang, Rokjin J. Park, Seungun Lee, Duseong S. Jo, and Minjoong J. Kim, Impact of changes in refractive indices of secondary organic aerosols on precipitation over China during 1980–2019 (2023), Atmospheric Environment, 299, 119644. DOI: https://doi.org/10.1016/j.atmosenv.2023.119644
- 154. Oak, Y.J., Park, R.J., Lee, J.-T., Byun, G., Future Air Quality and Premature Mortality in Korea (2023), Science of the Total Environment, 865, 161134. DOI: https://doi.org/10.1016/j.scitotenv.2022.161134
- 153. Myung‑Seo Koo, Kanghyun Song, Jung‑Eun Esther Kim, Seok‑Woo Son, Eun‑Chul Chang, Jee‑Hoon Jeong, Hyungjun Kim, Byung‑Kwon Moon, Rokjin J. Park, Sang‑Wook Yeh, Changhyun Yoo, Song‑You Hong The Global/Regional Integrated Model System (GRIMs): an Update and Seasonal Evaluation (2023), Asia-Pacific Journal of Atmospheric Sciences, https://doi.org/10.1007/s13143-022-00297-y.

**2022**

- 152. James H. Crawford, Katherine R. Travis, Laura M. Judd, Barry L. Lefer, Jack E. Dibb, Jhoon Kim, Rokjin Park, Gangwoong Lee, Limseok Chang, James Bernard B. Simpas, Maria Obiminda L. Cambaliza, Ronald C. Macatangay, Vanisa Surapipith, Narisara Thongboonchoo, Nguyen Thi Kim Oanh, To Thi Hien, Bich Thuy Ly, Abdus Salam, Sachin D. Ghude, Mohd Talib Latif, Liya E. Yu, Hiroshi Tanimoto, Yugo Kanaya The Airborne and Satellite Investigation of Asian Air Quality (Asia-Aq): An Opportunity for International Collaboration, International Geoscience and Remote Sensing Symposium, Vol. 2022-July, 10.1109/IGARSS46834.2022.9883819
- 151. Jeong, J.I., Seo J., and Park, R.J. Compromised Improvement of Poor Visibility Due to PM Chemical Composition Changes in South Korea, Remote Sensing, 14, 5310. https://doi.org/10.3390/rs14215310.
- 150. Hyeonmin Kim, Rokjin J. Park, Saewung Kim, William H. Brune, Glenn S. Diskin, Alan Fried, Samuel R. Hall, Andrew J. Weinheimer, Paul Wennberg, Armin Wisthaler, Donald R. Blake, Kirk Ullmann Observed versus simulated OH reactivity during KORUS-AQ campaign: implications for emission inventory and chemical environment in East Asia, Elementa: Science of the Anthropocene (2022) 10 (1): 00030, https://doi.org/10.1525/elementa.2022.00030
- 149. Naresh Kumar, Jeremiah Johnson, Greg Yarwood, Jung-Hun Woo, Younha Kim, Rokjin J. Park, Jaein I. Jeong, Suji Kang, Sungnam Chun, and Eladio Knipping. Contributions of domestic sources to PM2.5 in South Korea, Atmospheric Environment, 119273. DOI: https://doi.org/10.1016/j.atmosenv.2022.119273
- 148. Seungun Lee, Rokjin J. Park, Song-You Hong, Myung-Seo Koo, Jaein I. Jeong, Sang-Wook Yeh, Seok-Woo Son, 2022 A new chemistry-climate model GRIMs-CCM: Model evaluation of interactive chemistry-meteorology simulations, Asia-Pacific Journal of Atmospheric Sciences, https://doi.org/10.1007/s13143-022-00281-6
- 147. Yujin J. Oak, Rokjin J. Park, Duseong S. Jo, Alma Hodzic, Jose L. Jimenez, Pedro Campuzano-Jost, Benjamin A. Nault, Hwajin Kim, Hyeonmin Kim, Eunjo S. Ha, Chang-Keun Song, Seung-Muk Yi, Glenn S. Diskin, Andrew J. Weinheimer, Donald R. Blake, Armin Wisthaler, Mihee Shim, Yoonmi Shin Evaluation of Secondary Organic Aerosol (SOA) Simulations for Seoul, Korea, Journal of Advances in Modeling Earth Systems, https://doi.org/10.1029/2021MS002760
- 146. Hyung-Min Lee and Rokjin J. Park Factors determining the seasonal variation of ozone air quality in South Korea: Regional background versus domestic emission contributions, 2022, Environmental Pollution, 308, 119645. DOI: https://doi.org/10.1016/j.envpol.2022.119645
- 145. Zhaozhong Feng, Yansen Xu, Kazuhiko Kobayashi, Lulu Dai, Tianyi Zhang, Evgenios Agathokleous, Vicent Calatayud, Elena Paoletti, Arideep Mukherjee, Madhoolika Agrawal, Rokjin J. Park, Yujin J. Oak, Xu Yue Ozone pollution threatens the production of major staple crops in East Asia, Nature Food, 3, 47–56 DOI: https://doi.org/10.1038/s43016-021-00422-6
- 144. Jinkyul Choi, Daven K. Henze, Hansen Cao, Caroline R. Nowlan, Gonzalo González Abad, Hyeong-Ahn Kwon, Hyung-Min Lee, Yujin J. Oak, Rokjin J. Park, Kelvin H. Bates, Joannes D. Maasakkers, Armin Wisthaler, Andrew J. Weinheimer An inversion framework for optimizing non-methane VOC emissions using remote sensing and airborne observations in Northeast Asia during the KORUS-AQ field campaign, Journal of Geophysical Research: Atmospheres, https://doi.org/10.1029/2021JD035844
- 143. Sang-Wook Yeh, Guojian Wang, Wenju Cai, and Rokjin Park Diversity of ENSO-related surface temperature response in future projectionin CMIP6 climate models:climate change scenario versus ENSO intensity, Geophysical Research Letters, doi:10.1029/2021GL096135.

**2021**

- 131. Shixian Zhai, Daniel J. Jacob, Jared F. Brewer, Ke Li, Jonathan M. Moch, Jhoon Kim, Seoyoung Lee, Hyunkwang Lim, Hyun Chul Lee, Su Keun Kuk, Rokjin J. Park, Jaein I. Jeong, Xuan Wang, Pengfei Liu, Gan Luo, Fangqun Yu, Jun Meng, Randall V. Martin, Katherine R. Travis, Johnathan W. Hair, Bruce E. Anderson, Jack E. Dibb, Jose L. Jimenez, Pedro Campuzano-Jost, Benjamin A. Nault, Jung-Hun Woo, Younha Kim, Qiang Zhang, Hong Liao Relating geostationary satellite measurements of aerosol optical depth (AOD) over East Asia to fine particulate matter (PM2.5): insights from the KORUS-AQ aircraft campaign and GEOS-Chem model simulations, 2021, Atmos. Chem. Phys., 21, 16775-16791. DOI: https://doi.org/10.5194/acp-21-16775-2021

## 학회 발표

연구실 Presentations의 2021–2026년 발표 제목과 저자·발표처 표기다. 연도와 날짜는 누리집의 게시 표기다.[^pres2026][^pres2025][^pres2024][^pres2023][^pres2022][^pres2021]

**2026**

- Observed vs. simulated aerosol phase state during the ASIA-AQ campaign: its implication for climate forcing. Yoonbae Chung, Rokjin J Park, Hyeonmin Kim, Meehye Lee, Mijung Song, Vienna, Austria, European Geosciences Union, 2026 Annual Meeting
- Attribution of Latitudinal Methane Seasonal Cycles Constrained by Multi-year GOSAT Observations. Sang-Ik Oh, Rokjin J. Park, Sang-Woo Kim, and Robert J. Parker, Vienna, Austria, European Geosciences Union, 2026 Annual Meeting
- Nonstationary Summer Ozone-Temperature Climate Penalty over East Asia: Decadal Trends and Regional Variability. Jaein Jeong, Rokjin Park, Sang-Wook Yeh, and Seungun Lee, Vienna, Austria, European Geosciences Union, 2026 Annual Meeting
- Impact of Vertical Mixing on CO2 Simulations During the ASIA-AQ campaign. Mina Kim, Rokjin J. Park, Jingi Jung, Sang-Ik Oh, Jaein I. Jeong, Vienna, Austria, European Geosciences Union, 2026 Annual Meeting

**2025**

- Top-down Estimates of Regional Carbon Fluxes over East Asia Using Satellite Observations. Mina Kim, Rokjin J. Park, Sang-ik Oh, Eunjo S. Ha, and Jingi Jung, New Orleans, USA, 2025 AMS Annual Meeting
- Future air quality predictions using deep learning algorithms. Yujoo Jeong and Rokjin J. Park, New Orleans, USA, 2025 AMS Annual Meeting
- Sensitivity of GEMS formaldehyde vertical columns to a priori profile for air mass factor during ASIA-AQ. Gitaek T. Lee, Rokjin J. Park, Jaein I. Jeong, Seungun Lee, Hyeonmin Kim, and Hyeong-Ahn Kwon, Vienna, Austria, European Geosciences Union, 2025 Annual Meeting
- Constraining monthly variability of atmospheric methane budget through Kalman filter using GOSAT / TROPOMI XCH4. Sang-Ik Oh and Rokjin J. Park, Vienna, Austria, European Geosciences Union, 2025 Annual Meeting
- Assessing the sensitivity of GEMS HCHO AMF using observations and model simulations during ASIA-AQ. Gitaek T. Lee, Rokjin J. Park, Jaein I. Jeong, Seungun Lee, Hyeonmin Kim, and Hyeong-Ahn Kwon, Seoul, Korea, Student Colloquium of KOSAE (Korean Society for Atmospheric Environment)
- Top-down Estimate of Global Methane Budget using TROPOMI / GOSAT XCH4 Data. Sang-Ik Oh and Rokjin J. Park, Seoul, Korea, Student Colloquium of KOSAE (Korean Society for Atmospheric Environment)
- Analysis of secondary inorganic aerosol formation during ASIA_AQ campaign using a thermodynamic model. Yoonbae Chung, Rokjin J. Park, Meehye. Lee, Seoul, Korea, 2025 CMAS-Asia-Pacific and Regional IUAPPA Conference.
- Satellite-based Constraints on Global Methane Emissions and Tropospheric OH Variability. Sang-Ik Oh, Rokjin J. Park, Robert J. Parker, Seoul, Korea, 2025 CMAS-Asia-Pacific and Regional IUAPPA Conference
- Top-down Estimate of Global Methane Budget using GOSAT. Sang-Ik Oh and Rokjin J. Park. Cheongju, Korea, Korea Geoscience Union, The 6th Annual Meeting
- Sensitivity of GEMS formaldehyde vertical columns to key input parameters. Gitaek T. Lee, Rokjin J. Park, Jaein I. Jeong, Seungun Lee, Hyeonmin Kim Eunjo Ha, and Hyeong-Ahn Kwon, The 16th GEMS international workshop
- Insights into VOC emissions from GEMS HCHO and CHOCHO retrievals. Eunjo S. Ha, Rokjin J. Park, Gitaek T. Lee and Hyeong-Ahn Kwon, Goyang, Korea, The 16th GEMS International Workshop
- Current status of GEMS VOCs and their scientific applications. Rokjin J. Park, Gitaek T. Lee, Eunjo S. Ha, Yoonbae Chung, Hyeong-Ahn Kwon, Isabelle De Smedt, Michel Van Roozendael, and Jhoon Kim, Goyang, Korea, The 16th GEMS International Workshop
- Impact of Climate Hysteresis on East Asian Winter Haze under Carbon Removal Scenarios. Jaein Jeong, Rokjin J. Park, Sang-Wook Yeh, Soon-Il An, New Orleans, USA, American Geophysical Union, 2025 Annual Meeting.
- Performance and Bias Assessment of Historical Climate Simulations from the GRIMs-NEMO Coupled Earth System Model. Seungun Lee, Rokjin J. Park, Sang-Woo Kim, Seok-Woo Son, Sang-Wook Yeh, Changhyun Yoo, Byung-Kwon Moon et al. New Orleans, USA, American Geophysics Union, 2025 Annual Meeting.

**2024**

- Validation and Development Approaches for GEMS Glyoxal Retrievals. Eunjo S. Ha, Rokjin J. Park, Incheon, Korea, Student Colloquium of KOSAE (Korean Society for Atmospheric Environment)
- Evaluation of simulated CH4-C2H6 correlation during KORUS-AQ & ASIA-AQ. Sang-ik Oh, Rokjin J. Park, Incheon, Korea, Student Colloquium of KOSAE (Korean Society for Atmospheric Environment)
- Reconciling missing OH reactivity in the 3-D chemical transport model. Hyeonmin Kim, Rokjin J. Park, Saewung Kim, Do-Hyeon Park, Sang-Woo Kim, Hyeong-Ahn Kwon, Jinkyul Choi, Pyeongchang, Korea, Asia Oceania Geosciences Society (AOGS) 21st annual meeting
- Evaluation of GEMS formaldehyde vertical column densities. Gitaek T. Lee, Rokjin J. Park, Hyeong-Ahn Kwon, Jaein I. Jeong, Hyeonmin Kim, Cheol-Hee Kim, Soontae Kim, Chul Han Song, Chang-Keun Song, Jung-Hun Woo, and Jhoon Kim, Pyeongchang, Korea, Asia Oceania Geosciences Society (AOGS) 21st annual meeting
- Estimates of diurnal hydroxyl radical (OH) concentrations in East Asia using GEMS observations. Sang-Ik Oh, Rokjin J. Park, Pyeongchang, Korea, Asia Oceania Geosciences Society (AOGS) 21st annual meeting
- Current status of GEMS VOCs and their future development plan. Rokjin J. Park, Gitaek T. Lee, Eunjo S. Ha, Yoonbae Chung, Hyeong-Ahn Kwon, Isabelle De Smedt, Michel Van Roozendael and Jhoon Kim, Kailua-Kona, Hawaii, United States of America, TEMPO/GEMS Joint Science Team Workshop.
- Update of a priori profile and its effect on GEMS observations. Yoonbae Chung and Rokjin J. Park, Kailua-Kona, Hawaii, United States of America, TEMPO/GEMS Joint Science Team Workshop.
- Analysis of drought effects on VOC emissions in Asia using GEMS products. Eunjo S. Ha, Rokjin J. Park, Jaein I. Jeong, Gitaek T. Lee, and Sang-ik Oh, Kailua-Kona, Hawaii, United States of America, TEMPO/GEMS Joint Science Team Workshop.
- Evaluation of GEMS formaldehyde vertical column densities during ASIA-AQ. Gitaek T. Lee, Rokjin J. Park, Hyeong-Ahn Kwon, Eunjo S. Ha, Yoonbae Chung, Jaein I. Jeong, Hyeonmin Kim, Cheol-Hee Kim, Soontae Kim, Chul Han Song, Chang-Keun Song, Jung‐Hun Woo, and Jhoon Kim, Kailua-Kona, Hawaii, United States of America, TEMPO/GEMS Joint Science Team Workshop.
- Estimates of diurnal hydroxyl radical (OH) columns in East Asia using GEMS observations. Sang-Ik Oh, Rokjin J. Park, Hyeji Cha, Jhoon Kim, Kailua-Kona, Hawaii, United States of America, TEMPO/GEMS Joint Science Team Workshop.

**2023**

- Analysis of drought effects on VOC emissions in East Asia using GEMS products. Eunjo S. Ha, Rokjin J. Park, Hyeong-Ahn Kwon, Gitaek T. Lee, Sangik Oh, Haein Lee, Sieun Lee, Dong-Won Lee, Hyunkee Hong, Christophe Lerot, and Hitoshi. Irie, American Geophysical Union, 2023 Annual
- Effect of Nitryl Chloride Chemistry on Air Quality in South Korea during the KORUS-AQ Campaign. Hyeonmin Kim, Rokjin J. Park, Saewung Kim, Daun Jeong, Xiao Fu, Seogju Cho, American Meteorological Society, 103rd Annual Meeting
- Mixed Layer Height in a 3-D Chemical Transport Model: Implications for Gas and Aerosol Simulations. Rokjin J. Park, Hyeonmin Kim, Yujin J. Oak, Song-You Hong, Dohyun Park, Sang-Woo Kim, American Meteorological Society, 103rd Annual Meeting
- Effect of Current and Future Climate Change on Haze Events in East Asia. Jaein I. Jeong, Rokjin J. Park, American Meteorological Society, 103rd Annual Meeting
- Impact of the Recent Aerosol Trend on Regional Climate in East Asia. Seungun Lee, Rokjin J. Park, Sang-Wook Yeh, Yong-Cheol Jeong, American Meteorological Society, 103rd Annual Meeting
- Retrieval Sensitivity to a Priori Profiles for GEMS NO2 and HCHO. Sieun Lee, Rokjin J. Park, Gitaek Lee, Jaein I. Jeong, Hyeong-Ahn Kwon, Hanlim Lee,Junsung Park, Dong-Won Lee, Hyunkee Hong, American Meteorological Society, 103rd Annual Meeting
- Modeling nitryl chloride and its source and effect on gaseous and aerosol chemistry. Hyeonmmin Kim, Rokjin Park, Jean Jeong, Saewung Kim, Daun Jeong, Xiao Fu, and Seogju Cho, European Geosciences Union, 2023 Annual Meeting
- Effect of aerosol changes on regional climate in East Asia. Seungun Lee, Rokjin Park, Sang-Wook Yeh, and Yong-Cheol Jeong, European Geosciences Union, 2023 Annual Meeting
- Prediction of PM2.5 concentrations during winter in East Asia using climate indices. Jaein Jeong and Rokjin Park, European Geosciences Union, 2023 Annual Meeting
- Top-down estimates of Net Ecosystem Exchange (NEE) using satellite observations. Mina Kim, Rokjin Park, Sang-ik Oh, Eunjo Ha. Busan, Korea, The 4th Korea Geoscience Union Annual Meeting
- Validation of simulated atmospheric methane : A comparative analysis with remote-sensing observation data. Sang-ik Oh, Rokjin Park. Busan, Korea. The 4th Korea Geoscience Union Annual Meeting.
- Effect of the recent aerosol changes on regional climate in East Asia. Rokjin Park, Seungun Lee, Sang-Wook Yeh, Yong-Cheol Jeong. Busan, Korea. The 4th Korea Geoscience Union Annual Meeting.
- Evaluation of GEMS glyoxal column with TROPOMI and MAX-DOAS measurements. Eunjo S. Ha, Rokjin J. Park, Hyeong-Ahn Kwon, Gitaek T. Lee, Yoonbae Chung, Dong-Won Lee, Hyunkee Hong, Christophe Lerot, and Hitoshi Irie, 06-08 Sep, Seoul, Korea, The 14th GEMS international workshop
- Sensitivity of GEMS formaldehyde vertical columns to multiple factors. Gitaek T. Lee, Rokjin. J. Park, Hyeong-Ahn Kwon, Eunjo S. Ha, Sieun D. Lee, Myoung-Hwan Ahn, Mina Kang, Mijin Eo, Bavo Langerock, Corinne Vigouroux, Francois Hendrick, Gaia Pinardi, Isabelle De Smedt, Michel Van Roozendael, Pucai Wang, Yesul Cho, and Jhoon Kim, 06-08 Sep, Seoul, Korea, The 14th GEMS international workshop
- Top-down estimates of Net Ecosystem Exchange (NEE) Using Satellite Observations. Mina Kim, Rokjin J. Park, Sang-ik Oh, and Eunjo S. Ha, San Francisco, American Geophysical Union, 2023 Annual Meeting

**2022**

- Regional analysis of monthly averaged carbon dioxide concentration simulated by GEOS-Chem. Mina Kim, Rokjin Park, 17 Aug, Pyeong-Chang, Korea, The 3rd Korea Geoscience Union Annual Meeting
- First evaluation of GEMS formaldehyde retrieval algorithm. Gitaek Lee, Rokjin. J. Park, Hyeong-Ahn Kwon, Eunjo S. Ha, Sieun D. Lee, Dong-Won Lee, Hyunkee Hong, Christophe Lerot, Corinne Vigouroux, Francois Hendrick, Gaia Pinardi, Isabelle De Smedt, Michel Van Roozendael, and Pucai Wang, 10-14 Oct, Taormina, Italy, Sentinel -5P mission: 5 years anniversary
- Evaluation of GEMS glyoxal vertical column densities. Eunjo S. Ha, Rokjin J. Park, Hyeong-Ahn Kwon, Gitaek Lee, Sieun D. Lee, Dong-Won Lee, Hyunkee Hong and Christophe Lerot, 10-14 Oct, Taormina, Italy, Sentinel -5P mission: 5 years anniversary
- Evaluation of GEMS formaldehyde retrieval algorithm. Gitaek Lee, Rokjin. J. Park, Hyeong-Ahn Kwon, Eunjo S. Ha, Sieun D. Lee, Dong-Won Lee, Hyunkee Hong, Christophe Lerot, Corinne Vigouroux, Francois Hendrick, Gaia Pinardi, Isabelle De Smedt, Michel Van Roozendael, and Pucai Wang, 9-11 Nov, Seoul, Korea, The 13th GEMS international workshop
- Evaluation of GEMS glyoxal vertical column densities. Eunjo S. Ha, Rokjin J. Park, Hyeong-Ahn Kwon, Gitaek Lee, Sieun D. Lee, Dong-Won Lee, Hyunkee Hong, Christophe Lerot, and H. Irie, 9-11 Nov, Seoul, Korea, The 13th GEMS international workshop

**2021**

- Evaluation of GEMS HCHO retrieval during the in-orbit test period. Gitaek Lee, Rokjin J. Park, Hyeong-Ahn Kwon, Seunga Shin, Dong-Won Lee, Hyunkee Hong Michel Van Roozendael, and Francois Hendrick, 13-17 Dec, online, AGU fall meeting

## 연락과 위치

- 교수 이메일: rjpark@snu.ac.kr.[^prof]
- 교수 연구실: 서울대학교 501동 520호, 02-880-6715.[^dept]
- 실험실: 서울대학교 501동 506호, 02-880-6712.[^dept]
- 주소: 서울특별시 관악구 관악로 1 서울대학교, 우편번호 08826.[^prof]
[^dept]: 서울대학교 지구환경과학부, 박록진 교수 소개. <https://sees.snu.ac.kr/research-faculty/faculty/fulltime?mode=view&profidx=55> (관측일 2026-11-11).
[^prof]: 연구실 Professor. <http://airchem.snu.ac.kr/acmg/people/professor> (관측일 2026-11-11).
[^sat]: 연구실 GEMS Satellite 연구 소개. <http://airchem.snu.ac.kr/acmg/research?categoryId=35> (관측일 2026-11-11).
[^pm]: 연구실 PM Modeling 연구 소개. <http://airchem.snu.ac.kr/acmg/research?categoryId=36> (관측일 2026-11-11).
[^climate]: 연구실 Chemistry-Climate Modeling 연구 소개. <http://airchem.snu.ac.kr/acmg/research?categoryId=37> (관측일 2026-11-11).
[^campaign]: 연구실 SIJAQ/ASIA-AQ Campaign 연구 소개. <http://airchem.snu.ac.kr/acmg/research?categoryId=38> (관측일 2026-11-11).
[^members]: 연구실 Research Fellow. <http://airchem.snu.ac.kr/acmg/people/postdoctoral> (관측일 2026-11-11).
[^students]: 연구실 Graduate Student. <http://airchem.snu.ac.kr/acmg/people/graduate> (관측일 2026-11-11).
[^alumni]: 연구실 Alumni. <http://airchem.snu.ac.kr/acmg/people/aluimni> (관측일 2026-11-11).
[^alumni1]: 연구실 Alumni 추가 목록 1. <http://airchem.snu.ac.kr/acmg/people/more?peopleType=ALUMNI&current=0> (관측일 2026-11-11).
[^alumni2]: 연구실 Alumni 추가 목록 2. <http://airchem.snu.ac.kr/acmg/people/more?peopleType=ALUMNI&current=1> (관측일 2026-11-11).
[^alumni3]: 연구실 Alumni 추가 목록 3. <http://airchem.snu.ac.kr/acmg/people/more?peopleType=ALUMNI&current=2> (관측일 2026-11-11).
[^pub2026]: 연구실 Publications 2026. <http://airchem.snu.ac.kr/acmg/publications?categoryId=79> (관측일 2026-11-11).
[^pub2025]: 연구실 Publications 2025. <http://airchem.snu.ac.kr/acmg/publications?categoryId=76> (관측일 2026-11-11).
[^pub2024]: 연구실 Publications 2024. <http://airchem.snu.ac.kr/acmg/publications?categoryId=73> (관측일 2026-11-11).
[^pub2023]: 연구실 Publications 2023. <http://airchem.snu.ac.kr/acmg/publications?categoryId=70> (관측일 2026-11-11).
[^pub2022]: 연구실 Publications 2022. <http://airchem.snu.ac.kr/acmg/publications?categoryId=67> (관측일 2026-11-11).
[^pub2021]: 연구실 Publications 2021. <http://airchem.snu.ac.kr/acmg/publications?categoryId=55> (관측일 2026-11-11).
[^pres2026]: 연구실 Presentations 2026. <http://airchem.snu.ac.kr/acmg/presentations?categoryId=81> (관측일 2026-11-11).
[^pres2025]: 연구실 Presentations 2025. <http://airchem.snu.ac.kr/acmg/presentations?categoryId=78> (관측일 2026-11-11).
[^pres2024]: 연구실 Presentations 2024. <http://airchem.snu.ac.kr/acmg/presentations?categoryId=75> (관측일 2026-11-11).
[^pres2023]: 연구실 Presentations 2023. <http://airchem.snu.ac.kr/acmg/presentations?categoryId=71> (관측일 2026-11-11).
[^pres2022]: 연구실 Presentations 2022. <http://airchem.snu.ac.kr/acmg/presentations?categoryId=69> (관측일 2026-11-11).
[^pres2021]: 연구실 Presentations 2021. <http://airchem.snu.ac.kr/acmg/presentations?categoryId=64> (관측일 2026-11-11).
[^p1]: M. Kim 외, S.-W. Yeh, Atmospheric chemistry and physics (2026). <https://doi.org/10.5194/acp-26-6869-2026> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5027270746,publication_year:2021-2026> (관측일 2026-11-11).
[^p2]: F. Yao 외, R. J. Park, Atmospheric chemistry and physics (2026). <https://doi.org/10.5194/acp-26-12049-2026> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5027270746,publication_year:2021-2026> (관측일 2026-11-11).
[^p3]: E. S. Ha 외, H. Irie, Atmospheric measurement techniques (2024). <https://doi.org/10.5194/amt-17-6369-2024> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5027270746,publication_year:2021-2026> (관측일 2026-11-11).
[^p4]: H. Kim 외, T.-M. Fu, The Science of The Total Environment (2024). <https://doi.org/10.1016/j.scitotenv.2024.176838> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5027270746,publication_year:2021-2026> (관측일 2026-11-11).
[^p5]: J. F. Brewer 외, H. J. Liao, Journal of Geophysical Research Atmospheres (2023). <https://doi.org/10.1029/2022jd037257> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5027270746,publication_year:2021-2026> (관측일 2026-11-11).
[^p6]: S. Lee 외, S.-W. Son, Asia-Pacific Journal of Atmospheric Sciences (2022). <https://doi.org/10.1007/s13143-022-00281-6> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5027270746,publication_year:2021-2026> (관측일 2026-11-11).
[^p7]: Y. J. Oak 외, Y. M. Shin, Journal of Advances in Modeling Earth Systems (2022). <https://doi.org/10.1029/2021ms002760> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5027270746,publication_year:2021-2026> (관측일 2026-11-11).

# 통계적 의사결정 연구실 (Statistical Decision Making Lab, SDM)

**KAIST 산업및시스템공학과·데이터사이언스대학원 · 송호승 교수**

- 분야: 변화점 탐지(데이터의 성질이 바뀌는 순간을 찾는 통계 방법)와 이상 탐지, 두 집단·여러 집단 비교 검정(A/B 검정), 연관성 검정, 공간 군집 분석, 커널 기반 비모수 통계, 제조·사회·생명의학 데이터 응용
- 홈페이지: <https://hoseungs.github.io/group.html>
- 근거와 출처: [통계적 의사결정 연구실 근거 페이지](statistical-decision-making-sources.md)

> 데이터가 언제 달라졌는지, 두 데이터 묶음이 정말 다른지, 두 종류의 변수가 서로 관련이 있는지를 엄밀하게 판단하는 통계 방법을 만드는 연구실이다. 차원이 높거나 구조가 복잡한 큰 데이터에서도 빠르게 쓸 수 있는 방법을 개발해 제조 공정, 생명의학, 사회 데이터에 적용한다.[^group][^home]

## 무엇을 연구하나

연구실은 빅데이터와 인공지능 시대의 통계 방법론과 데이터 기반 의사결정을 연구한다고 소개한다. 복잡하고 차원이 높으며 구조가 있는 데이터를 다룰 수 있는 튼튼하고 해석 가능한 통계 방법을 만드는 것이 목표이고, 특히 변화점 탐지, 비모수 가설 검정(데이터 분포를 미리 가정하지 않는 검정), 공간 군집 분석에 집중하며 제조, 금융공학, 사회·생명의학에 응용한다.[^group] 교수 누리집은 연구 관심사를 통계적 의사결정과 AX(AI 전환), 변화점 분석(이상 탐지), 두 집단·여러 집단(A/B) 검정과 연관성 검정, 공간 군집, 제조·사회·생명의학 응용으로 적는다.[^home]

첫 번째 갈래는 **두 데이터 묶음을 비교하는 검정**이다. 커널(데이터 사이 유사도를 재는 함수)을 이용한 두 집단 검정은 차원이 높아지면 성능이 떨어지는데, 고차원 데이터에 흔한 패턴을 활용해 검정력(실제 차이가 있을 때 이를 찾아내는 능력)을 크게 높인 새 검정을 Biometrika에 발표했고,[^p1] 큰 데이터에서도 빠르게 돌아가는 검정을 만들었다.[^p2] 그래프 구조 데이터에서 학습 데이터와 실제 데이터의 분포가 달라지는 것을 검정으로 찾아내는 방법도 제안했다.[^p3]

두 번째 갈래는 **변화점 탐지**다. 연속해서 들어오는 고차원 데이터에서 분포가 바뀌는 지점을 찾는 커널 기반 방법,[^p4] 같은 값이 반복해 나오는 네트워크 같은 데이터에서도 쓸 수 있는 그래프 기반 변화점 탐지를 만들었다.[^p5] 연구실은 2026년부터 한국연구재단 기초연구실(비정상 순차 데이터의 변화 탐지와 적응적 의사결정)을 맡고 있다.[^projects]

세 번째 갈래는 **연관성 검정과 생명의학 데이터 분석**이다. 두 조건에서 변수들 사이의 관계가 달라지는지 확인하는 검정,[^p6] 군집으로 묶인 데이터에서 두 변수의 독립성을 확인하는 빠른 검정,[^p7] 미생물 군집 연구에서 데이터 정규화(분석 전에 자료의 크기 차이를 맞추는 처리) 방법 선택의 어려움을 덜어 주는 종합 검정을 개발했다.[^p8] 개발한 방법들은 R 패키지(kerTests, kerSeg, gSeg, kerDAA 등)로 공개했다고 연구 페이지가 적는다.[^research]

## 주요 연구 주제

### 1. 고차원 두 집단 검정

일반화 커널 두 집단 검정, 대규모 데이터용 빠른 검정, 그래프 데이터 분포 변화 탐지.[^p1][^p2][^p3] 대표 논문 1, 2, 3.

### 2. 변화점 탐지

커널 기반 변화점 탐지, 반복 관측 데이터의 그래프 기반 탐지.[^p4][^p5] 대표 논문 4, 5.

### 3. 연관성 검정과 생명의학 응용

다변량 차이 연관 분석, 군집 상관 데이터 독립성 검정, 미생물군 연관 분석.[^p6][^p7][^p8] 대표 논문 6, 7, 8.

## 대표 논문

교수 누리집 논문 목록의 2021–2026년 학술지 논문에서 주제별로 골랐다. 8편 모두 교수가 1저자이고 그중 5편은 KAIST 부임(2024) 전 박사과정·박사후연구원 시기 연구이며, 1·2·4·5는 박사 지도교수(Hao Chen), 6·7·8은 박사후연구원 시기 지도자(Michael C. Wu)와의 공동 연구다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^research] |
|---|---|---|---|---|
| 1 | 2024 | [Generalized kernel two-sample tests](https://doi.org/10.1093/biomet/asad068) · Biometrika | 두 데이터 묶음의 분포가 같은지 보는 기존 커널 검정은 특정 차이만 잘 잡고 차원이 중간 이상이면 잘 작동하지 않는다. 중·고차원 데이터에 흔한 패턴을 활용해 여러 유형의 차이에서 검정력을 크게 높인 새 통계량과, 계산 비용이 낮은 검정 절차를 제안했다. 분자 모양 비교와 공항 택시 운행 비교에 적용했고 R 패키지 kerTests로 공개했다.[^p1] | 1저자 송호승, 공저 Hao Chen |
| 2 | 2026 | [A fast and effective kernel two-sample test for large-scale data](https://doi.org/10.1007/s11222-026-10969-8) · Statistics and Computing | 기존 대규모 데이터용 커널 두 집단 검정은 계산이 무겁거나 고차원의 흔한 차이에 약하다. 여러 유형의 차이에서 검정력이 높고, 고차원에 더 견고하며, 커널 폭 같은 설정을 데이터를 나눠 최적화할 필요가 없는 새 검정을 제안했다.[^p2] | 1저자 송호승, 공저 Hao Chen |
| 3 | 2021 | [Preventing failures by dataset shift detection in safety-critical graph applications](https://doi.org/10.3389/frai.2021.589632) · Frontiers in Artificial Intelligence | 학습 때와 실제 사용 때 입력 데이터의 분포가 달라지는 문제는 의료·신약 개발 같은 안전이 중요한 분야에서 큰 걸림돌이다. 그래프 구조 데이터에서 이런 변화를 통계적 가설 검정으로 찾아내는 두 집단 검정 기반 방법을 제안했고, 방향성 그래프와 표본 크기가 다른 경우에도 쓸 수 있음을 보였다.[^p3] | 1저자 송호승, 공저 Jayaraman J. Thiagarajan·Bhavya Kailkhura |
| 4 | 2024 | [Practical and powerful kernel-based change-point detection](https://doi.org/10.1109/tsp.2024.3479274) · IEEE Transactions on Signal Processing | 관측이 이어지는 데이터에서 분포가 바뀌는 지점을 찾는 커널 기반 방법은 잘못된 발견을 통제하기 어려웠다. 고차원 데이터의 중요한 패턴을 이용해 검정력을 높인 새 틀을 만들고, 유의성을 빠르게 계산하는 근사식을 유도해 큰 데이터에 바로 쓸 수 있게 했다. 전화 통화 네트워크 데이터에 적용했고 R 패키지 kerSeg로 공개했다.[^p4] | 1저자 송호승, 공저 Hao Chen |
| 5 | 2022 | [Asymptotic distribution-free changepoint detection for data with repeated observations](https://doi.org/10.1093/biomet/asab048) · Biometrika | 관측값 사이 유사도를 그래프로 나타내는 변화점 탐지는 고차원 데이터에 유연하지만, 네트워크 데이터처럼 같은 값이 반복해 나오면 쓰기 어렵다. 가능한 최적 그래프들을 평균하거나 합치는 방식으로 이를 풀고, 오류를 통제하는 계산식을 유도했다. 시간에 따라 바뀌는 네트워크의 변화 탐지에 적용했다.[^p5] | 1저자 송호승, 공저 Hao Chen |
| 6 | 2024 | [Multivariate differential association analysis](https://doi.org/10.1002/sta4.704) · Stat | 환자와 대조군 사이에서 유전체 특징들의 관계가 달라지는지처럼, 두 조건에서 두 변수 묶음의 관계가 다른지 확인하는 커널 기반 검정을 제안했다. 계산이 빨라 큰 데이터에 쓸 수 있고, 선형·비선형 관계의 차이를 모두 잘 잡았다.[^p6] | 1저자 송호승, 공저 Michael C. Wu |
| 7 | 2022 | [A fast kernel independence test for cluster-correlated data](https://doi.org/10.1038/s41598-022-26278-9) · Scientific Reports | 생명의학·종단 연구에서 흔한, 군집으로 묶인 데이터에서는 기존 커널 독립성 검정(HSIC)을 바로 쓸 수 없다. 각 군집 안의 의존 구조를 반영하는 HSIC 기반 독립성 검정과 빠른 p값(관찰된 차이가 우연일 가능성) 근사를 제안했다.[^p7] | 1저자 송호승, 마지막 저자 Michael C. Wu |
| 8 | 2023 | [Accommodating multiple potential normalizations in microbiome associations studies](https://doi.org/10.1186/s12859-023-05147-w) · BMC Bioinformatics | 미생물 개체 수 데이터는 분석 전 정규화가 필요하지만 어떤 방법이 최선인지 고르기 어렵다. 여러 정규화 방법의 p값을 코시 결합 검정(여러 p값을 하나로 묶는 방법)으로 합치는 종합 검정을 제안해, 오류를 잘 통제하면서 가장 좋은 정규화에 가까운 검정력을 냈다.[^p8] | 1저자 송호승, 마지막 저자 Michael C. Wu |

## 교수와 전문 분야

송호승 교수는 서울대 통계학 학사(2014, 수리과학 부전공)·석사(2016)와 미국 UC Davis 통계학 박사(2021, 지도교수 Hao Chen)를 받았다. 미국 로런스 리버모어 국립연구소 데이터과학 연구 인턴(2019), 프레드 허친슨 암연구소 박사후연구원(2021–2024)을 거쳐 2024년 4월 KAIST 조교수로 부임했다.[^about] 산업및시스템공학과와 데이터사이언스대학원 소속이며 AX학과와 AI수학대학원 겸임이다.[^home]

논문으로 보면 전문 분야는 세 갈래다.

- **커널·그래프 기반 고차원 두 집단 검정**.[^p1][^p2][^p3]
- **변화점 탐지**.[^p4][^p5]
- **연관성·독립성 검정과 미생물군 데이터 분석**.[^p6][^p7][^p8]

## 응용 분야

대표 논문과 과제 목록으로 보면 제조 공정의 이상·불량 탐지, 생명의학과 미생물군 연구, 네트워크·물류 데이터 분석에 닿아 있다.[^p4][^p8][^projects] 과제 목록에는 반도체 코팅 불량 예측, 타이어 혼합 시방서 작성, 물류 매칭·운임 예측 자문 같은 산업 과제와 피지컬 AI 플랫폼 공동 과제가 있다.[^projects]

## 구성원

2026년 10월 19일 연구실 그룹 페이지 기준이다.[^group] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 대표 논문이 대부분 연구실 개설 전 논문이라 비어 있다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Mingyu Go | 박사과정 | gomg9157@kaist.ac.kr |  |
| Serim Han | 박사과정 | haser@kaist.ac.kr |  |
| Jinhyeok Park | 석사과정 | zinhyeok@kaist.ac.kr |  |
| Taejoon Yang | 석사과정 | tj2875@kaist.ac.kr |  |
| Dogeon Lee | 석사과정 | magictive@kaist.ac.kr |  |
| Dongbeen Kim | 석사과정 | dbk3216@kaist.ac.kr |  |
| Eunyoung Yu | 행정 직원 |  |  |

## 졸업생

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Serim Han | M.S. (2026) | PhD student at KAIST |

## 최근 논문 목록 (2021–2026)

교수 누리집 연구 페이지의 학술지 논문 13편이다. 사전 공개(preprint) 6편은 같은 페이지에 따로 있다.[^research]

**2026**

- Wrobel, J.\*, Song, H.\*. "A robust, scalable K-statistic for quantifying immune cell clustering in spatial proteomics data". *The Annals of Applied Statistics*.
- Song, H., Chen, H. "A fast and effective kernel two-sample test for large-scale data". *Statistics and Computing, 36(5):214*.

**2024**

- Song, H., Chen, H. "Practical and powerful kernel-based change-point detection". *IEEE Transactions on Signal Processing, 72:5174-5186*.
- Song, H., Chen, H. "Generalized kernel two-sample tests". *Biometrika, 111(3):755-770*.
- Casto, A.M., Song, H., Xie, H., Selke, S., Roychoudhury, P., Wu, M.C., Wald, A., Greninger, A.L., Johnston, C. "Viral genomic variation and the severity of genital HSV-2 infection as quantified by shedding rate: a viral genome-wide association study". *Journal of Infectious Diseases, 230(6):1357-1366*.
- Song, H., Wu, M.C. "Multivariate differential association analysis". *Stat, 13(2), e704*.
- Byrne, E.H., Song, H., Srinivasan, S., Fredricks, D.N., Reed, S.D., Guthrie, K., Wu, M.C., Mitchell, C.M. "Association between vaginal microbiota and vaginal inflammatory immune markers in postmenopause". *Menopause: The Journal of The Menopause Society, 31(7):575-581*.

**2023**

- Song, H., Wu, M.C. "Limitation of permutation-based differential correlation analysis". *Genetic Epidemiology, 47(3):583-642*.
- Song, H., Ling, W., Zhao, N., Plantinga, A.M., Broedlow, C.A., Klatt, N.R., Hensley-McBain, T., Wu, M.C. "Accommodating multiple potential normalizations in microbiome associations studies". *BMC Bioinformatics, 24(1):22*.

**2022**

- Song, H., Liu, H., Wu, M.C. "A fast kernel independence test for cluster-correlated data". *Scientific Reports, 12(1):21659*.
- Ling, W., Lu, J., Zhao, N., Lulla, A., Plantinga, A., Fu, W., Zhang, A., Liu, H., Song, H., Li, Z., Chen, J., Randolph, T., Koay, W., White, J., Launer, L., Fodor, A., Meyer, K., Wu, M.C. "Batch effects removal for microbiome data via conditional quantile regression". *Nature Communications, 13(1):5418*.
- Song, H., Chen, H. "Asymptotic distribution-free changepoint detection for data with repeated observations". *Biometrika, 109(3):783-798*.

**2021**

- Song, H., Thiagarajan, J., Kailkhura, B. "Preventing failures by dataset shift detection in safety-critical graph applications". *Frontiers in Artificial Intelligence, 4:589632*.

## 연구 과제

교수 누리집 과제 페이지의 과제명, 역할, 기간, 지원 기관이다.[^projects]

- Advisory on Building a Modular AI Pipeline for Intelligent Logistics Matching and Freight Rate Prediction (지능형 물류 매칭 및 운임 예측을 위한 모듈형 AI 파이프라인 구축 자문) (기간 2026-2027; 지원 AOROA Labs Co., Ltd. (아로아랩스))
- Development of an Integrated Sim-to-Real Platform for Physical AI-Enabled Collaborative Intelligence (피지컬AI 기반 협업지능 Sim-to-Real 통합 플랫폼 기술 개발) (역할 Co-I; 기간 2026-2030; 지원 National IT Industry Promotion Agency (정보통신산업진흥원))
- Change Detection and Adaptive Decision-Making in Nonstationary Sequential Data (역할 PI; 기간 2026-2029; 지원 National Research Foundation of Korea (한국연구재단); 사업 Basic Research Lab (기초연구실))
- Development of a Program for Drafting Mixing Specifications Based on Compound Properties (정련 물성 기반 혼합 시방서 작성 프로그램 개발) (역할 PI; 기간 2026-2027; 지원 Hankook Tire & Technology (한국타이어))
- Development of a Comprehensive Change-Point Detection Framework Adaptive to Complex Data Structures and Dynamic Environments (역할 PI; 기간 2026-2031; 지원 National Research Foundation of Korea (한국연구재단); 사업 Young Scientist Grants (신진연구,유형B))
- Prediction of Semiconductor Coating Defects and Key Factor Identification PoC (반도체 Coating 불량 예측 및 핵심 인자 규명 PoC) (역할 PI; 기간 2026; 지원 Nepes (네페스))
- Establishment of a Leading Physical AI Model and PoC (피지컬 AI 선도모델 수립 및 PoC) (역할 Co-I; 기간 2025; 지원 National IT Industry Promotion Agency (정보통신산업진흥원))
- Development of a Unified Change-Point Detection Framework for Multiple Types of Distributional Changes (역할 PI; 기간 2025-2026; 지원 National Research Foundation of Korea (한국연구재단); 사업 Young Scientist Grants (신진연구,씨앗))
- KAIST Starting Fund (역할 PI; 기간 2024-2027; 지원 KAIST)

## 연락과 위치

- 교수 이메일: hoseung@kaist.ac.kr, 전화 042-350-3117[^home]
- 위치: KAIST 산업경영학동(E2-2) 4103호 (대전 유성구 대학로 291)[^home]

[^home]: 송호승 교수 누리집 첫 화면 <https://hoseungs.github.io/> (2026-10-19 열람)
[^about]: 송호승 교수 누리집 약력(Bio) <https://hoseungs.github.io/about.html> (2026-10-19 열람)
[^research]: 송호승 교수 누리집 연구(논문 목록) <https://hoseungs.github.io/research.html> (2026-10-19 열람)
[^projects]: 송호승 교수 누리집 과제 <https://hoseungs.github.io/project.html> (2026-10-19 열람)
[^group]: 통계적 의사결정 연구실 그룹 페이지 <https://hoseungs.github.io/group.html> (2026-10-19 열람)
[^p1]: H. Song, H. Chen, Biometrika 111, 755-770 (온라인 2023-11-14). <https://doi.org/10.1093/biomet/asad068> 초록 기준.
[^p2]: H. Song, H. Chen, Statistics and Computing 36, 214 (온라인 2026-08-29). <https://doi.org/10.1007/s11222-026-10969-8> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: H. Song, J. J. Thiagarajan, B. Kailkhura, Frontiers in Artificial Intelligence 4, 589632 (온라인 2021-05-18). <https://doi.org/10.3389/frai.2021.589632> 초록 기준.
[^p4]: H. Song, H. Chen, IEEE Transactions on Signal Processing 72, 5174-5186 (2024). <https://doi.org/10.1109/tsp.2024.3479274> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: H. Song, H. Chen, Biometrika 109, 783-798 (온라인 2021-09-29). <https://doi.org/10.1093/biomet/asab048> 초록 기준.
[^p6]: H. Song, M. C. Wu, Stat 13, e704 (온라인 2024-06-07). <https://doi.org/10.1002/sta4.704> 초록 기준.
[^p7]: H. Song, H. Liu, M. C. Wu, Scientific Reports 12, 21659 (온라인 2022-12-15). <https://doi.org/10.1038/s41598-022-26278-9> 초록 기준.
[^p8]: H. Song 외, M. C. Wu, BMC Bioinformatics 24, 22 (온라인 2023-01-19). <https://doi.org/10.1186/s12859-023-05147-w> 초록 기준.

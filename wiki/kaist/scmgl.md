# 단일 세포 유전체 의학 연구실 (Single-Cell Medical Genomics Laboratory, SCMGL)

**KAIST 의과학대학원 · 박종은 부교수**

- 분야: 단일 세포 자료 통합·분석 방법, 조직의 물리적 성질을 이용한 측정, 세포 배양 플랫폼과 표적 조합 설계
- 대분야: 기초생명·생물물리, 컴퓨팅·AI
- 태그: 바이오정보학·계산생물학[^research][^p3][^p4], 단일 세포·공간 오믹스[^research][^p1][^p5], 생체재료·조직 공학[^p6]
- 홈페이지: <https://sites.google.com/view/scmglkaist>
- 근거와 출처: [SCMGL 근거 페이지](scmgl-sources.md)

> 서로 다른 단일 세포 자료를 함께 분석하는 계산 방법과 조직 속 세포를 측정하는 기법을 개발하고, 세포 배양과 표적 조합 설계로 연결하는 연구실이다.[^research][^p1][^p2][^p7]

## 무엇을 연구하나

박종은 부교수가 이끄는 KAIST 의과학대학원 연구실이다. 누리집은 영문 이름을 Single-Cell Medical Genomics Laboratory, 약칭을 SCMGL로 적는다.[^home][^members] 연구의 바탕인 단일 세포 유전체학(개별 세포의 유전정보와 그 활용 상태를 분석하는 분야)은 여러 세포를 한꺼번에 평균 내는 대신 세포별 차이를 다룬다. 연구실은 여러 출처·세포 유형·측정 층위의 자료를 통합하는 계산 방법과 데이터베이스를 개발하겠다고 밝힌다.[^research]

주요 분석 대상은 RNA(ribonucleic acid, 리보핵산: 유전정보의 전달과 발현 조절 등에 관여하는 생체 분자)와 전사체(세포나 조직에 존재하는 RNA의 전체)다. 서로 다른 측정법으로 얻은 자료를 합치고, 자료 속 신호와 잡음을 구분하며, 세포가 변하는 경로를 비교하는 방법을 연구한다. MultiMAP은 자료 통합과 차원 축소(자료의 주요 관계를 유지하며 변수 수를 줄이는 계산)를, scLENS는 신호 검출과 차원 축소를, Genes2Genes는 세포 변화 경로의 유전자별 비교를 다룬다.[^p5][^p4][^p3]

계산에 들어갈 자료를 얻는 측정 방식도 연구한다. FiNi-seq(fibrotic niche enrichment sequencing)는 조직의 물리적 성질을 이용해 섬유화 영역(섬유성 성분이 축적된 조직 부위)을 모은 뒤 세포별 분자 상태를 측정하는 방법이다. 일반 분석에서 놓치기 쉬운 노화 관련 조직 부위를 분석하기 위해 제시됐다.[^p1] 세포 배양에서는 침샘의 다양한 세포 특성을 유지하는 오가노이드(세포를 배양해 조직·장기의 일부 구조와 기능을 재현한 입체 모델) 플랫폼과, 유도만능줄기세포(분화한 세포의 상태를 바꾸어 여러 세포 유형으로 발달할 능력을 갖게 한 세포)에서 특정 면역 세포를 만드는 방법을 다룬다.[^p7][^p8]

분석 결과를 세포 공학(원하는 성질이나 기능을 갖도록 세포를 설계·변형하는 기술)에 연결하는 연구도 있다. 암세포와 정상 세포를 구별하는 표적 항원(면역계가 인식하는 표적 물질)의 조합을 고르고, 두 표적의 존재 여부에 따라 반응하는 논리 연산을 평가한다. 이는 개별 유전자 하나의 발현만이 아니라 표적 조합을 설계 대상으로 삼는 접근이다.[^p2]

## 주요 연구 주제

### 단일 세포 자료의 통합과 계산 방법

MultiMAP은 여러 자료에 공통으로 있는 특징뿐 아니라 각 자료에만 있는 특징도 이용해 자료를 통합한다. 자료마다 결과에 미치는 비중을 정할 수 있고, 서로 다른 분자 측정 자료를 함께 분석하는 데 쓰였다.[^p5] scLENS는 자료를 정리하는 과정의 신호 왜곡과 사용자의 수동 선택 문제를 다루는 도구다. 신호 차원을 자료에서 정하도록 해 단일 세포 RNA 분석의 수동 조정을 줄인다.[^p4]

Genes2Genes는 두 세포 변화 경로에서 개별 유전자의 변화가 일치하는 구간과 일치하지 않는 구간을 정렬한다. 베이지안 추론(관측 자료에 따라 가설의 확률을 갱신하는 통계적 추론)과 동적 계획법(문제를 부분 문제로 나누고 그 답을 재사용해 전체 답을 구하는 계산 방법)을 결합한다. 실제 자료와 모의 자료에서 경로 정렬을 평가했으며, 체외에서 만든 세포와 체내 세포의 상태가 어디에서 달라지는지 분석하는 데 적용했다.[^p3]

### 조직의 물리적 성질을 이용한 측정

FiNi-seq(fibrotic niche enrichment sequencing)는 섬유화 미세환경(세포를 둘러싼 섬유성 조직의 국소 환경)을 모아 분석하는 방법이다. 조직이 효소 분해에 견디는 성질을 이용해 해당 부위를 선택적으로 모으고, 개별 세포의 RNA와 유전물질 접근성을 분석한다. 초록은 이 방법으로 노화 초기에 나타나는 조직 환경을 자세히 분석할 수 있다고 설명한다.[^p1]

### 세포 배양 모델과 실험 플랫폼

침샘 오가노이드 연구는 쥐와 사람의 침샘 세포를 장기간 배양하면서 서로 다른 세포 유형과 분비샘의 특성을 유지하는 플랫폼을 확립했다.[^p7] 골수계 세포(단핵구·대식세포 등으로 이어지는 혈액 세포 계열) 연구에서는 유도만능줄기세포의 분화(세포가 서로 다른 구조와 기능을 갖추는 과정)를 분석하고, 수지상세포(면역 반응을 시작하는 데 필요한 항원 정보를 다른 면역 세포에 제시하는 세포)를 만드는 프로토콜(실험 수행을 위해 정한 절차)을 개발했다.[^p8]

환자 유래 세포외기질(세포 바깥에서 세포를 지지하고 신호를 전달하는 물질의 집합)을 배양 바탕으로 삼는 연구도 있다. 대장암 오가노이드의 배양 바탕을 바꾸고 세포별 분자 자료를 함께 분석해, 암세포가 퍼져 나가는 초기 변화를 재현하는 체외 모델을 제시했다.[^p6]

### 논리 연산에 따른 표적 조합 설계

CAR(chimeric antigen receptor, 키메라 항원 수용체: 특정 표적을 인식하도록 여러 기능 부분을 결합해 만든 수용체) 연구에서는 암세포와 정상 세포를 구별하는 유전자 쌍을 선별했다. 단일 세포 발현 지도를 바탕으로 두 단계 선별법을 적용하고, AND·OR·NOT 논리 연산(두 조건의 동시 충족·어느 하나의 충족·특정 조건의 부정을 조합하는 규칙)에 따른 표적 조합의 암세포 포괄 범위와 정상 세포 구별 정도를 평가했다. 선택한 조합은 세포 표면의 표적 측정과 연결해 검증했다.[^p2]

## 대표 논문

단일 세포 자료의 통합·측정, 세포 배양 플랫폼과 표적 조합 설계의 연구 갈래를 보여 주는 논문이다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문 · 발표처 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2025 | [Quasi-spatial single-cell transcriptome based on physical tissue properties defines early aging associated niche in liver](https://doi.org/10.1038/s43587-025-00857-7) · Nature Aging 5, 929–949 | 조직의 물리적 성질을 이용해 섬유화 미세환경을 모은 뒤 세포별 분자 상태를 측정하는 FiNi-seq를 제시했다. 간의 노화 초기에 나타나는 조직 환경과 세포 변화를 분석했다.[^p1] |
| 2 | 2023 | [Single-cell mapping of combinatorial target antigens for CAR switches using logic gates](https://doi.org/10.1038/s41587-023-01686-y) · Nature Biotechnology 41, 1593–1605 | 암세포와 정상 세포의 단일 세포 지도를 만들고, 두 표적의 조합과 논리 연산으로 암세포를 구별할 후보를 선별·평가했다. 선택한 조합을 세포 표면 측정과 연결해 검증했다.[^p2] |
| 3 | 2025 | [Gene-level alignment of single-cell trajectories](https://doi.org/10.1038/s41592-024-02378-4) · Nature Methods 22, 68–81 | 두 세포 변화 경로에서 개별 유전자의 변화가 일치하는 구간과 어긋나는 구간을 정렬하는 Genes2Genes를 제시했다. 실제 자료와 모의 자료에서 정렬을 평가하고, 체외 세포와 체내 세포 상태의 차이를 분석하는 데 적용했다.[^p3] |
| 4 | 2024 | [scLENS: data-driven signal detection for unbiased scRNA-seq data analysis](https://doi.org/10.1038/s41467-024-47884-3) · Nature Communications 15, 3575 | 단일 세포 RNA 자료의 신호 왜곡과 수동 선택 문제를 다루는 차원 축소 도구를 개발했다. 자료 정리 방식을 조정하고 잡음 제거와 신호의 안정성 평가를 결합해 신호 차원을 자료에서 정한다.[^p4] |
| 5 | 2021 | [MultiMAP: dimensionality reduction and integration of multimodal data](https://doi.org/10.1186/s13059-021-02565-y) · Genome Biology 22, 346 | 서로 다른 자료에 공통인 특징과 각 자료에만 있는 특징을 함께 이용하는 통합·차원 축소 알고리즘을 개발했다. 자료별 비중을 정할 수 있으며 여러 종류의 단일 세포 분자 자료를 함께 분석하는 데 적용했다.[^p5] |
| 6 | 2025 | [Single-cell multiomic modelling of early metastatic events promoted by the extracellular matrix](https://doi.org/10.1038/s41416-025-03181-4) · British Journal of Cancer 133, 1708–1719 | 환자 유래 세포외기질로 대장암 오가노이드의 배양 바탕을 바꾸는 체외 모델을 제시했다. 세포별 분자 자료를 함께 분석해 암세포가 퍼져 나가는 초기 변화와 기질의 역할을 조사했다.[^p6] |
| 7 | 2022 | [Salivary gland organoid culture maintains distinct glandular properties of murine and human major salivary glands](https://doi.org/10.1038/s41467-022-30934-z) · Nature Communications 13, 3291 | 다양한 침샘 세포와 분비샘의 특성을 유지하는 쥐·사람 오가노이드 장기 배양법을 확립했다. 침샘 종양의 특성을 보존한 배양 모델도 만들 수 있는 실험 플랫폼을 제시했다.[^p7] |
| 8 | 2022 | [Robust temporal map of human in vitro myelopoiesis using single-cell genomics](https://doi.org/10.1038/s41467-022-30557-4) · Nature Communications 13, 2885 | 유도만능줄기세포에서 골수계 세포로 분화하는 과정을 분석해 체내 발달과 비교했다. 이와 함께 유도만능줄기세포에서 수지상세포를 만드는 프로토콜을 개발했다.[^p8] |

## 교수와 전문 분야

박종은은 누리집 Members에서 Associate Professor로 소개된다. 서울대학교 생명과학 분야 학사(2009)와 박사(2015)를 마쳤으며, 서울대학교 V. Narry Kim 연구실(2015–2017)과 영국 웰컴 생어 연구소 Sarah Teichmann 연구실(2017–2020)의 박사후연구원 경력을 적고 있다.[^members] 학과 소개는 단일 세포 유전체학, 생명정보학, 세포생물학을 연구 분야로 든다.[^prof]

최근 논문에서 확인되는 전문 분야는 단일 세포 자료를 통합·비교하는 계산 방법, 조직의 물리적 성질을 이용한 측정, 세포 배양 플랫폼과 세포 표적 조합의 설계다.[^p5][^p3][^p4][^p1][^p2][^p7]

## 응용 분야

개발한 방법은 여러 종류의 세포 자료를 함께 분석하거나, 조직 내 특정 미세환경을 조사하거나, 배양한 세포와 체내 세포의 상태를 비교하는 데 쓰인다.[^p5][^p1][^p3] 세포 배양 플랫폼은 조직 재생·항암 연구를 위한 실험 기반으로, 표적 조합 선별은 암세포를 구별하는 세포 공학 설계에 연결된다.[^p7][^p8][^p2]

## 구성원

2026-10-30 누리집 Current members에 게시된 21명이다. 과정과 시작 연도는 누리집 표기다. 「대표 논문 참여」는 대표 논문의 전체 저자 목록에서 같은 이름을 확인한 사람에게 표시했다.[^members]

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Kyuheum Jeon | 박사후연구원 | 2023- | jkh9057@kaist.ac.kr |  |
| Seongryong Kim | 박사후연구원 | 2024- | srkim727@kaist.ac.kr |  |
| Myungsun Park | 박사후연구원 | 2026- | ms0219@kaist.ac.kr | 1 |
| Sangcheol Park | 박사후연구원 | 2026- |  |  |
| Doil Yoon | 박사후연구원 | 2026- | doilyoon@ibs.re.kr |  |
| Hanee Lee | 박사후연구원 | 2026- |  |  |
| Hyun-Kyung Chang | 박사후연구원 | 2026- |  |  |
| JiSu Han | 연구원 | 2026- | friendlystar@ibs.re.kr |  |
| Jangwon Oh | 박사과정 | 2024- | jangwon5@kaist.ac.kr |  |
| Yongjun Koh | 석박사통합과정 | 2021- | way2gokoh@ibs.re.kr | 1 |
| Wooseok Kim | 석박사통합과정 | 2022- | kwseok1114@kaist.ac.kr | 1 |
| Jeongwoo La | 석박사통합과정 | 2022- | castle1998@kaist.ac.kr |  |
| Seoyeong Lee | 석박사통합과정 | 2023- | seoylee@kaist.ac.kr | 1 |
| Sungmin Cheong | 석박사통합과정 | 2023- | scheong@kaist.ac.kr |  |
| Suho Lee | 석박사통합과정 | 2024- | shl0113@kaist.ac.kr |  |
| Soo Hyeon Ma | 석박사통합과정 | 2024- | hyeon423@kaist.ac.kr |  |
| Minjun Choi | 석박사통합과정 | 2025- | choiminjun@kaist.ac.kr |  |
| Jiyeon Lyu | 석박사통합과정 | 2025- | jiyeonlyu@kaist.ac.kr |  |
| Yeju Kim | 석박사통합과정 | 2026- | yejukim@kaist.ac.kr |  |
| Seonho Kim | 석박사통합과정 | 2026- | lake_1830@kaist.ac.kr |  |
| 이지헌 | 인턴 |  |  |  |

## 졸업생과 이전 구성원

누리집 Alumni에 게시된 7명이다. Seongryong Kim과 Myungsun Park은 박사 졸업생과 현재 박사후연구원 양쪽에 적혀 있다. 연도와 진로는 누리집 표기다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hyo Jae Kim | Postdoctoral researcher (2022-2024) | Assistant Professor, Department of Neurology, Asan Medical Center |
| Junho Kang | PhD (2024) |  |
| Seongryong Kim | PhD (2024) |  |
| Kwon Yong Tak | PhD (2025) |  |
| Myungsun Park | PhD (2025) |  |
| Hyerin Hwang | Researcher |  |
| Mert Yakup Baykan | Lab Intern (2021-2022) |  |

## 최근 논문 목록 (2021–2026)

단일 세포 자료 통합·분석, 조직 측정, 세포 배양 모델, 표적 조합 설계와 정상 세포의 분화·조절 원리에 관한 논문이다. 연도는 누리집 all publications의 연도 구역이며, 제목·저자·발표처는 게시 표기를 그대로 두고 DOI를 덧붙였다. 목록의 별표와 #은 누리집 기호를 유지했다.[^pubs]

**2025**

- Tak, K.Y.\*, Kim, J.\*, Park, M.\*,\* ... , Kim, C#, & Park, J.-E.# (2025). Quasi-spatial single-cell transcriptome based on physical tissue properties defines early aging associated niche in liver. Nature Aging DOI: <https://doi.org/10.1038/s43587-025-00857-7>.
- Lee, H. J.\*, Lee, J. H.\*, ..., Park, J.-E.#, Kim, P.#, & Choi, J. K.# (2025). Single-cell multiomic modelling of early metastatic events promoted by the extracellular matrix. British Journal of Cancer, 133(11), 1708–1719. DOI: <https://doi.org/10.1038/s41416-025-03181-4>.
- Sumanaweera, D.\*, Suo, C.\*, ..., Park, J.-E., ..., & Teichmann, S. A.# (2025). Gene-level alignment of single-cell trajectories. Nature Methods, 22(1), 68–81. DOI: <https://doi.org/10.1038/s41592-024-02378-4>.
- Mohammed, A., ... Park, J.-E,..., Weinacht, K. G. (2025). Distinct type I and II interferon responses direct cortical and medullary thymic epithelial cell development. Science Immunology, 10(107), eado4720. DOI: <https://doi.org/10.1126/sciimmunol.ado4720>.

**2024**

- Kim, H., Chang, W., Chae, S.J., Park, J.-E., Seo, M. and Kim, J.K. (2024). scLENS: data-driven signal detection for unbiased scRNA-seq data analysis. Nature Communications, 15, 3575 DOI: <https://doi.org/10.1038/s41467-024-47884-3>.
- Choi, S., Kang, JG., Tran, Y.T.H., ..., Park, M., ..., Park, J.-E,  Lim, D.-S., Suh, J. M. (2024) Hippo–YAP/TAZ signalling coordinates adipose plasticity and energy balance by uncoupling leptin expression from fat mass. Nat Metab 6, 847–860 DOI: <https://doi.org/10.1038/s42255-024-01045-4>.

**2023**

- Kwon, J.\*, Kang, J.\*, ..., An, H. J.#, Lee, H.-O.#, Park J.-E.#, Choi, J. K.# (2023). Single-cell mapping of combinatorial target antigens for CAR switches using logic gates. Nature Biotechnology, 1-13. DOI: <https://doi.org/10.1038/s41587-023-01686-y>.

**2022**

- Yoon, Y. J., Kim, D., Tak, K. Y., ... Park J.-E, Lim, J. Y. (2022). Salivary gland organoid culture maintains distinct glandular properties of murine and human major salivary glands. Nature communications, 13(1), 3291. DOI: <https://doi.org/10.1038/s41467-022-30934-z>.
- Alsinet, C., Primo, M. N., Lorenzi, V., Bello, E., Kelava, I., Jones, C. P., ..., Park J.-E, ...,  & Vento-Tormo, R. (2022). Robust temporal map of human in vitro myelopoiesis using single-cell genomics. Nature Communications, 13(1), 2885. DOI: <https://doi.org/10.1038/s41467-022-30557-4>.

**2021**

- Jain, M. S., Polanski, K., Conde, C. D., Chen, X., Park, J., Mamanova, L., ..., Park J.-E, …, Teichmann SA (2021). MultiMAP: dimensionality reduction and integration of multimodal data. Genome biology, 22(1), 1-26. DOI: <https://doi.org/10.1186/s13059-021-02565-y>.

## 연락과 위치

- 소속: KAIST 의과학대학원[^members]
- 교수 이메일: jp24@kaist.ac.kr[^contact][^members]
- 누리집 사무실 전화: +82-42-350-4866[^members]
- 학과 교수 소개 전화: 042-350-0229[^prof]
[^home]: 연구실 첫 화면 <https://sites.google.com/view/scmglkaist> (2026-10-30 열람).
[^research]: Research <https://sites.google.com/view/scmglkaist/research> (2026-10-30 열람).
[^members]: Members <https://sites.google.com/view/scmglkaist/members> (2026-10-30 열람).
[^pubs]: Publications <https://sites.google.com/view/scmglkaist/publications> (2026-10-30 열람).
[^contact]: Contact <https://sites.google.com/view/scmglkaist/contact> (2026-10-30 열람).
[^prof]: 의과학대학원 박종은 교수 소개 <https://gsmse.kaist.ac.kr/boards/view/professor_01/12> (2026-10-30 열람).
[^p1]: K. Y. Tak 외, J.-E. Park, Nature Aging 5, 929-949 (온라인 2025-05-05). <https://doi.org/10.1038/s43587-025-00857-7> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1038/s43587-025-00857-7%22> (2026-10-30 열람).
[^p2]: J. Kwon 외, J. K. Choi, Nature Biotechnology 41, 1593-1605 (온라인 2023-02-16). <https://doi.org/10.1038/s41587-023-01686-y> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1038/s41587-023-01686-y%22> (2026-10-30 열람).
[^p3]: D. Sumanaweera 외, S. A. Teichmann, Nature Methods 22, 68-81 (온라인 2024-09-19). <https://doi.org/10.1038/s41592-024-02378-4> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=Gene-level%20alignment%20of%20single-cell%20trajectories> (2026-10-30 열람).
[^p4]: H. Kim 외, J. K. Kim, Nature Communications 15, 3575 (온라인 2024-04-27). <https://doi.org/10.1038/s41467-024-47884-3> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=scLENS%3A%20data-driven%20signal%20detection%20for%20unbiased%20scRNA-seq%20data%20analysis> (2026-10-30 열람).
[^p5]: M. S. Jain 외, S. A. Teichmann, Genome Biology 22, 346 (온라인 2021-12-20). <https://doi.org/10.1186/s13059-021-02565-y> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=MultiMAP%3A%20dimensionality%20reduction%20and%20integration%20of%20multimodal%20data> (2026-10-30 열람).
[^p6]: H. J. Lee 외, J. K. Choi, British Journal of Cancer 133, 1708-1719 (온라인 2025-09-15). <https://doi.org/10.1038/s41416-025-03181-4> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=Single-cell%20multiomic%20modelling%20of%20early%20metastatic%20events%20promoted%20by%20the%20extracellular%20matrix> (2026-10-30 열람).
[^p7]: Y.-J. Yoon 외, J.-Y. Lim, Nature Communications 13, 3291 (온라인 2022-06-07). <https://doi.org/10.1038/s41467-022-30934-z> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=Salivary%20gland%20organoid%20culture%20maintains%20distinct%20glandular%20properties%20of%20murine%20and%20human%20major%20salivary%20glands> (2026-10-30 열람).
[^p8]: C. Alsinet 외, R. Vento-Tormo, Nature Communications 13, 2885 (온라인 2022-05-24). <https://doi.org/10.1038/s41467-022-30557-4> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=Robust%20temporal%20map%20of%20human%20in%20vitro%20myelopoiesis%20using%20single-cell%20genomics> (2026-10-30 열람).

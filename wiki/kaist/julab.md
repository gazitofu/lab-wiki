# 유전체 돌연변이 모자이시즘 연구실 (COSMOS: Comprehensive Observation of Somatic Mosaicism, its Origin and Significance)

**KAIST 의과학대학원 · 주영석 부교수**

- 분야: 체세포 돌연변이 검출·계통 분석, 공간 유전체 측정, 오가노이드 기반 평가 체계
- 대분야: 기초생명·생물물리, 컴퓨팅·AI
- 태그: 바이오정보학·계산생물학[^p3], 단일 세포·공간 오믹스[^p1][^p2], 장기 칩·체외 질병 모델[^p4]
- 홈페이지: <https://www.julab.kaist.ac.kr/>
- 근거와 출처: [COSMOS 근거 페이지](julab-sources.md)

> 세포의 유전적 차이를 검출하고 그 관계를 해석하는 계산 방법과 측정 절차를 연구하며, 유전체 분석 소프트웨어와 오가노이드 기반 평가 체계도 다루는 연구실이다.[^research][^software][^p1][^p2][^p3][^p4]

## 무엇을 연구하나

주영석 부교수가 이끄는 연구실로, 유전체(생물이 지닌 유전 물질 전체)의 차이를 측정하고 해석하는 방법을 연구한다.[^home][^members][^profile] 중심 대상은 체세포 돌연변이(생식세포를 제외한 몸의 세포에 생기는 유전 물질의 변화)와 모자이시즘(같은 개체 안에 유전적으로 다른 세포 집단이 공존하는 현상)이다. 연구 소개는 개별 세포의 유전적 차이를 검출하고 세포 집단의 관계를 파악하려는 목표를 밝힌다.[^research]

이를 위해 전장 유전체 서열 분석(유전 물질 전반의 염기 배열을 읽는 방법)과 세포별 자료를 결합한다. 구성 비율이 낮은 변이를 놓치지 않도록 세포 선별과 서열 분석을 결합하는 검출 절차를 제시했고, 변이 자료를 걸러 발생 계통도(공통 조상 세포에서 갈라지는 관계를 나타낸 도식)를 재구성하는 자체 분석 절차도 개발했다.[^p1][^p3] 소프트웨어 목록에는 돌연변이 양상 분석용 온라인 도구 MUTALISK와 초기 발생 세포 집단·변이를 추적하는 웹 화면 SCV(Somatic Clonal Viewer)가 있다. SCV는 연구 자료와 결과를 상호작용 방식으로 살펴보도록 만든 도구다.[^software][^scv]

세포가 조직의 어느 위치에 놓이는지도 측정 방법의 일부다. RNA(리보핵산, ribonucleic acid; 유전 정보의 전달·발현 등에 관여하는 분자)를 대상으로 하는 전사체(세포나 조직에서 만들어진 RNA 전체) 분석과 유전체 자료를 연결해, 조직 단면에서 유전적으로 구별되는 세포 집단의 위치를 정량 지도로 나타내는 분석 절차와 전용 알고리즘(문제를 풀기 위한 계산 단계)을 제시했다.[^p2] 유전적 차이, 세포의 위치, 유전자 발현(유전자 정보로 RNA나 단백질을 만드는 과정)과 조직의 특징을 함께 살피는 측정 체계다.[^p2]

오가노이드(장기의 일부 구조·기능을 재현하는 삼차원 세포 배양체)와 단일 세포 전사체 분석을 결합한 바이러스 감염성 평가 체계를 제시했다.[^p4]

## 주요 연구 주제

### 1. 낮은 비율의 세포 변이를 검출하는 측정 절차

조직에 섞인 세포를 구분해 분석하고, 기존에 드러나지 않던 체세포 변이와 구조변이(유전 물질 구간의 결실·중복·재배열 등 구조적 변화)를 검출하는 방법을 다룬다. 세포 선별과 유전체 분석을 결합한 절차 및 이를 간소화한 방법이 대표 논문에 있다.[^p1]

### 2. 조직의 위치와 유전적 세포 집단을 잇는 공간 분석

조직 단면의 유전적 하위 세포 집단을 정량 지도로 나타내고, 세포별 전사체·조직 특징을 전용 알고리즘으로 연결한다. 세포의 유전적 구분과 조직 내 위치를 함께 읽는 공간 유전체 분석 절차를 개발했다.[^p2]

### 3. 발생 계통을 해석하는 계산 방법

발생 계통 분석에서는 자체 바이오정보학(유전체 등 생물 자료를 계산 방법으로 분석하는 분야) 분석 절차로 변이를 걸러 세포 계통도를 구성했다.[^p3]

### 4. 오가노이드와 단일 세포 분석을 결합한 평가 체계

사람 폐포를 재현하는 오가노이드와 단일 세포 전사체 분석을 결합해 바이러스 감염성을 비교하는 체계를 제시했다. 초록은 새로운 실험 절차를 제공하며 새로 나타나는 변이의 관찰에 적용할 수 있다고 설명한다.[^p4]

## 대표 논문

2021–2026년 랩 논문 목록에서 주영석 교수가 저자이고, 측정·분석 방법 또는 평가 체계의 기여를 담은 논문을 골랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 교신저자 표시는 랩 목록의 # 설명을 따른다.[^pubs]

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주영석의 저자 역할 |
|---|---|---|---|---|
| 1 | 2023 | [Ultra-Low Level Somatic Mutations and Structural Variations in Focal Cortical Dysplasia Type II](https://doi.org/10.1002/ana.26609) · Annals of Neurology | 조직 전체를 한꺼번에 읽을 때 드러나지 않는 변이를 검출하려고, 특정 표지를 보이는 세포를 구분한 뒤 유전체 분석을 결합하는 방법을 제시했다. 이어 이 접근을 간소화한 분석 방법도 제시했다. 초록은 이 방법이 낮은 비율의 체세포 변이와 구조변이 검출을 돕는다고 설명한다.[^p1] | 공저자 |
| 2 | 2022 | [Spatial genomics maps the structure, nature and evolution of cancer clones](https://doi.org/10.1038/s41586-022-05425-2) · Nature | 조직 단면에서 유전적으로 다른 하위 세포 집단이 어디에 분포하는지 정량 지도로 나타내는 분석 절차를 개발했다. 전장 유전체 분석, 조직 내 서열 분석, 세포별 전사체 분석과 이들을 연결하는 전용 알고리즘을 결합해 각 세포 집단의 위치·조직 특징을 함께 살피도록 했다.[^p2] | 공저자 |
| 3 | 2022 | [Asymmetric Contribution of Blastomere Lineages of First Division of the Zygote to Entire Human Body Using Post-Zygotic Variants](https://doi.org/10.1007/s13770-022-00443-7) · Tissue Engineering and Regenerative Medicine | 발생 초기에 생긴 변이를 이용해 세포들의 계보를 추적하려고 자체 바이오정보학 분석 절차를 개발했다. 변이를 걸러 발생 계통도를 구성하고, 다른 조직의 변이 비율 자료와 대조했다. 이 접근으로 초기 세포 계통이 몸에 기여하는 관계를 분석했다.[^p3] | 공저자 |
| 4 | 2022 | [Relative infectivity of the SARS-CoV-2 Omicron variant in human alveolar cells](https://doi.org/10.1016/j.isci.2022.105571) · iScience | 바이러스의 감염성을 비교하는 실험 체계를 마련하려고 사람 폐포 오가노이드와 단일 세포 전사체 분석을 결합했다. 이 체계로 상대 감염성을 평가할 수 있음을 보였고, 새로 나타나는 변이를 관찰하는 데 적용할 수 있는 실험 절차를 제시했다.[^p4] | 교신저자 |

## 교수와 전문 분야

주영석은 KAIST 의과학대학원 전임교수 명단에 올라 있으며, 랩 구성원 쪽은 직위를 Associate Professor로 적고 MD·PhD 학위를 병기한다.[^roster][^profile][^members] 학과 소개의 전문 분야는 「돌연변이/모자이시즘, 생명정보학」이다.[^profile]

방법 연구에서의 전문 분야는 세포 변이 검출 절차, 조직 위치와 분자 정보를 연결하는 분석, 발생 계통을 해석하는 계산 방법이다.[^p1][^p2][^p3]

## 응용 분야

세포에 낮은 비율로 존재하는 변이를 검출하는 유전체 분석, 조직 단면의 세포 집단을 정량 지도화하는 공간 분석, 발생 세포 계통의 재구성에 적용한다.[^p1][^p2][^p3] 오가노이드 기반 바이러스 감염성 비교 평가도 응용 대상이다.[^p4]

## 구성원

2026년 10월 30일 관측한 랩 구성원 쪽의 박사후연구원 5명과 박사과정 학생 5명이다. 페이지의 갱신 표기는 2026년 10월 10일이며, 시작 시점은 게시된 경우만 적었다. Group leader는 교수 절에 적었다.[^members] 「대표 논문 참여」는 대표 논문의 전체 등록 저자 목록에서 이름이 대응하는 경우에 표시한다.

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| 안요한 (Yohan An) | 박사후연구원 | 2022.3-present |  |
| 남창현 (Chang Hyun Nam) | 박사후연구원 |  |  |
| 이윤아 (Yunah Lee) | 박사후연구원 |  |  |
| 원혜인 (Hyein Won) | 박사후연구원 |  |  |
| 이범기 (Beomki Lee) | 박사후연구원 |  |  |
| 정진실 (Jinsil Jeong) | 박사과정 | 2022- |  |
| 김연진 (Yeonjin Kim) | 박사과정 | 2023- |  |
| 유진희 (Jinhee Ryu) | 박사과정 | 2024- |  |
| 김희경 (Heegyeong Kim) | 박사과정 | 2025- |  |
| 박소윤 (Soyoon Park) | 박사과정 | 2026- |  |

## 졸업생과 이전 구성원

랩 Alumni의 PhD graduates 16행, Other tracks 6행과 Undergraduate Research Program 1행이다. 현 구성원과 졸업생에 함께 실린 이름 및 박한솔의 박사·URP 항목은 게시 구획대로 각각 적었다. 학위·기간·진로는 랩 표기다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 이준구 (June-Koo Lee) | PhD (2017) | Moved to Harvard Med School as a Postdoc then to MSKCC (2025-) |
| 육정환 (Jeonghwan Youk) | PhD (2016-2020) | Moved to Inocras Inc., then SNUH (Professor at Dept. of Internal Medicine) |
| 박성열 (Seongyeol Park) | PhD (2016-2020) | Moved to Inocras Inc. as a Senior Scientist (2021), then to Stanford University (2023-) |
| 김률 (Ryul Kim) | PhD (2017-2021) | Moved to Inocrs Inc. as a CTO |
| 임준오 (Joonoh Lim) | PhD (2017-2022.2) | Moved to Inocras. Inc. |
| 이기종 (Kijong Yi) | PhD (2017-2022.2) | Moved to Inocras Inc. |
| 안요한 (Yohan An) | PhD (2016.9-2022.2) |  |
| 박한솔 (Hansol Park) | PhD (2018-2023.2) | Moved to Inocras Inc. |
| 민경일 (Kyoung Il Min) | PhD (2019-2023.2) | Moved to Catholic Medical Center (Clinical fellow) |
| 김태우 (Taewoo Kim) | PhD (2018. Fall-2022. Fall) | Currently a post-doc @ Weill Cornell Medicine |
| 박지형 (Ji-Hyung Park) | PhD (2019-2023) | Moved to SNUBH |
| 남창현 (Chang Hyun Nam) | PhD (2020-2024) |  |
| 이윤아 (Yunah Lee) | PhD (2020-2025) |  |
| 원혜인 (Hyein Won) | PhD (2021-2025) |  |
| 안지송 (Jisong An) | PhD (2021-2026) | Moved to University of Washington (postdoc) |
| 이범기 (Beomki Lee) | PhD (2023-2026) |  |
| 강규혁 (Kyu Hyuk Kang) | Julab PhD studen (2017.3-2018.8) | Moved to Genome and Company |
| 강준호 (Junho Kang) | Julab PhD student (2020.3-2020.9) | Relocated to Prof Jong Eun Park's Lab |
| 김수연 (Su Yeon Kim) | Julab, Research Professor (2019.6-2020.12) |  |
| 윤종수 (Chris Jongsoo Yoon) | MPhil |  |
| 최명숙 (Myungsuk Choi) | Research associate (2018.06-2021) |  |
| 오수아 (Soo A Oh) | Research associate (2019.05-2022) |  |
| 박한솔 (Hansol Park) | Undergraduate Research Program (URP) (2017 Autumn) | joined Julab as a graduate student |

## 최근 논문 목록 (2021–2026)

세포 변이 검출, 공간 유전체 측정, 발생 계통의 계산 분석, 체외 평가 체계, 정상 세포의 유전체 변화와 조절 원리를 다룬 논문이다. 연도·제목·저자·발표처는 랩 게시 표기를 따르고 DOI를 덧붙였다. 2021년 항목은 출판일이 2021년 10월 13일 이후인 논문이다.[^pubs]

**2024**

- Youk J\*, Kwon HW\*, Lim J\*, Kim E\*, Kim T\*, …, Chang JH#, Kim KS#, Son TG#, Ju YS#. Quantitative and qualitative mutational impact of ionizing radiation on normal cells. Cell Genomics. 2024 Feb 14;4(2):100499. PMID:38359788 DOI: 10.1016/j.xgen.2024.100499

**2023**

- Nam CH\*, Youk J\*, Kim JY, Lim J, Park JW, ..., Kwon HW#, Kim MJ#, Ju YS#. Widespread somatic L1 retrotransposition in normal colorectal epithelium. Nature. 2023 May; 617(7961):540-547. PMID:37165195 DOI: 10.1038/s41586-023-06046-z
- Kim JH, Park JH, Lee J, Park JW, Kim HJ, ..., Lee JH. Ultra-Low Level Somatic Mutations and Structural Variations in Focal Cortical Dysplasia Type II. Ann Neurol. 2023 Jun;93(6):1082-1093. PMID:36700525 DOI: 10.1002/ana.26609

**2022**

- Yoon C\*, Kim S, Nam CH, Lee JH, Park JW, …, Griffith OL#, Ju YS#. Estimation of intrafamilial DNA contamination in family trio genome sequencing using Mendelian inconsistencies. Genome Res. 2022 Dec; 32(11-12):2134-2144. PMID:36617634 DOI: 10.1101/gr.276794.122
- Kim T\*, Min KI\*, Yang J, Kim JW, Cho J, …, Na KJ#, Lee J-Y#, Ju YS#. Relative infectivity of the SARS-CoV-2 Omicron variant in human alveolar cells. iScience. 2022 Dec;25(12):105571. PMID:36406862 DOI: 10.1016/j.isci.2022.105571
- Lomakin A, Svedlund J, Strell C, Gataric M, Shmatko A, …, Yates LR. Spatial genomics maps the structure, nature and evolution of cancer clones. Nature. 2022 Nov;611(7936):594-602. Epub 2022 Nov 9. PMID:36352222 DOI: 10.1038/s41586-022-05425-2
- Lee JH, Kim S, Han S, Min J, Caldwell B, …, Kim JK. p57Kip2 imposes the reserve stem cell state of gastric chief cells. Cell Stem Cell. 2022 May 5;29(5):826-839.e9. PMID:35523142 DOI: 10.1016/j.stem.2022.04.001
- Kwon SG, Bae GH, Choi JH, Mali NM, Jun MS, …, Oh JW. Asymmetric Contribution of Blastomere Lineages of First Division of the Zygote to Entire Human Body Using Post-Zygotic Variants. Tissue Eng Regen Med. 2022 Aug;19(4):809-821. PMID:35438457 DOI: 10.1007/s13770-022-00443-7
- Cho YW, Min DW, Kim HP, An Y, Kim S, …, Kim TY. Patient-derived organoids as a preclinical platform for precision medicine in colorectal cancer. Mol Oncol. 2022 Jun;16(12):2396-2412. PMID:34850547 DOI: 10.1002/1878-0261.13144

**2021**

- (Review) Youk J\*, Kwon HW\*, Kim R, Ju YS#. Cdissecting single-cell genomes through the clonal organoid technique. Exp Mol Med. 2021 Oct;53(10):1503-1511. PMID:34663940 DOI: 10.1038/s12276-021-00680-1

## 수상

2021년 10월 13일–2026년 10월 13일 범위의 랩 소식에 게시된 수상이다.[^news]

- 2022-09-16 · Taewoo와 Chan Hyun이 제31회 International KOGO Conference에서 각각 (Oral) Presentation Award와 Poster Presentation Award를 받았다.
- 2022-05-24 · 주영석이 Human Genome Organisation(HUGO)의 Chen Award of Excellence를 받았고, 시상식을 위해 Human Genome Meeting 2022에 초청받았다.
- 2022-03-02 · 주영석이 제1회 Lim Sung-Ki Award for Young Investigators를 받았다.

## 소식

2021년 10월 13일–2026년 10월 13일 범위의 연구실 명칭 변경과 방법 연구 발표 소식이다.[^news]

- 2023-06-29 · 연구실 이름을 Lab of Cancer Genomics에서 COSMOS로 바꾸었다.
- 2022-12-22 · 사람 폐포 세포에서 SARS-CoV-2 오미크론 변이의 상대 감염성을 다룬 논문을 iScience에 발표했다.

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291 한국과학기술원 고성능집적시스템 연구센터 N26, 323호.[^contact]
- 연구실 전화: +82-42-350-0424, 팩스: +82-42-350-4240.[^contact]
- 교수 전화: 042-350-0224. 교수 이메일: ysju@kaist.ac.kr.[^profile]
[^home]: 연구실 첫 화면. <https://www.julab.kaist.ac.kr/> (관측 2026-10-30).

[^profile]: KAIST 의과학대학원 주영석 교수 소개. <https://gsmse.kaist.ac.kr/boards/view/professor_01/21> (관측 2026-10-30).

[^roster]: KAIST 의과학대학원 전임교수 목록. <https://gsmse.kaist.ac.kr/boards/lists/professor_01> (관측 2026-10-30).

[^members]: 랩 MEMBERS. <https://www.julab.kaist.ac.kr/members> (관측 2026-10-30).

[^research]: 랩 RESEARCH. <https://www.julab.kaist.ac.kr/research> (관측 2026-10-30).

[^software]: 랩 SOFTWARES. <https://www.julab.kaist.ac.kr/softwares> (관측 2026-10-30).

[^scv]: 랩 Somatic Clone Viewer 소개. <https://www.julab.kaist.ac.kr/somatic-clone-viewer> (관측 2026-10-30).

[^pubs]: 랩 PUBLICATIONS. <https://www.julab.kaist.ac.kr/publications> (관측 2026-10-30).

[^news]: 랩 NEWS. <https://www.julab.kaist.ac.kr/news> (관측 2026-10-30).

[^contact]: 랩 CONTACTS. <https://www.julab.kaist.ac.kr/contact-us> (관측 2026-10-30).

[^p1]: J. H. Kim 외, J. H. Lee, Annals of Neurology (2023). <https://doi.org/10.1002/ana.26609> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=Ultra-Low%20Level%20Somatic%20Mutations%20and%20Structural%20Variations%20in%20Focal%20Cortical%20Dysplasia%20Type%20II> (관측 2026-10-30).

[^p2]: A. Lomakin 외, L. R. Yates, Nature (2022). <https://doi.org/10.1038/s41586-022-05425-2> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=Spatial%20genomics%20maps%20the%20structure%2C%20nature%20and%20evolution%20of%20cancer%20clones> (관측 2026-10-30).

[^p3]: S. G. Kwon 외, J. W. Oh, Tissue engineering and regenerative medicine (2022). <https://doi.org/10.1007/s13770-022-00443-7> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1007/s13770-022-00443-7%22> (관측 2026-10-30).

[^p4]: T. Kim 외, Y. S. Ju, iScience (2022). <https://doi.org/10.1016/j.isci.2022.105571> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/1878-0261.13144/v1/review1|10.1002/ana.26609|10.1007/s13770-022-00443-7|10.1016/j.ccell.2021.03.005|10.1016/j.ebiom.2023.104596|10.1016/j.ejca.2024.114206|10.1016/j.isci.2022.105571|10.1016/j.stem.2022.04.001|10.1016/j.xcrm.2025.102206|10.1016/j.xhgg.2024.100301|10.1016/s0302-2838(23)01082-5|10.1038/s10038-024-01258-1|10.1038/s10038-025-01325-1|10.1038/s12276-021-00658-z|10.1038/s12276-021-00680-1|10.1038/s12276-024-01284-1|10.1038/s41380-022-01697-2|10.1038/s41416-020-01146-3|10.1038/s41467-021-24807-0|10.1038/s41467-022-29925-x|10.1038/s41467-024-45366-0|10.1038/s41586-021-03786-8|10.1038/s41586-022-05425-2|10.1038/s41586-023-06046-z|10.1038/s41590-020-00860-7|10.1038/s41598-022-11492-2|10.1096/mmdmr2025.s03.p01|10.1101/2023.12.20.23300156|10.1101/2024.10.28.620744|10.1111/liv.14814|10.1136/bjo-2023-323388|10.1161/circresaha.122.320845|10.1172/jci148517|10.1186/s12887-021-02923-6|10.1186/s12943-025-02273-2|10.1210/endocr/bqad082|10.14348/molcells.2021.0094|10.37473/fic/10.1101/2020.04.23.057778|10.4078/jrd.2025.0001|10.4078/jrd.21.0046> (관측 2026-10-30).

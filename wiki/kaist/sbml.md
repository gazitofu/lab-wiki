# Systems Biology and Medicine Laboratory (SBML)

**KAIST 생명화학공학과 · 김현욱 부교수**

- 영문 이름: Hyun Uk Kim
- 분야: 시스템생물학·대사공학·생물 계산 모형[^research][^faculty]
- 대분야: 화학공정·바이오공학, 컴퓨팅·AI
- 태그: 바이오정보학·계산생물학[^research], 합성생물학·DNA 합성[^research][^p1][^p2], 과학·공학 AI[^research][^p1][^p2]
- 홈페이지: <https://sbml.kaist.ac.kr/>
- 근거와 출처: [Systems Biology and Medicine Laboratory (SBML) 근거 페이지](sbml-sources.md)

> 생명체의 물질 반응과 유전자 작용을 컴퓨터 모형으로 표현해, 미생물 생산과 생물 기능 설계에 필요한 방법을 만들고 질병 관련 표적을 예측하는 연구실이다.

## 무엇을 연구하나

SBML은 시스템생물학(생명체의 구성 요소와 상호작용을 전체 체계로 연구하는 분야)을 바탕으로 생물산업과 의학의 문제를 다룬다. 대사(생명체 안에서 물질이 만들어지고 바뀌거나 분해되는 반응 전체), 신호 전달, 유전자(생물의 기능과 형질에 관여하는 유전 정보의 단위)의 작용을 연결한 생물 네트워크를 만들고 분석하며, 목표로 하는 생물의 성질을 얻기 위해 무엇을 바꿀지 예측하는 계산 모형과 작업 절차를 개발한다.[^research]

산업 쪽에서는 대사공학(생물의 물질 반응 경로와 조절을 바꾸어 원하는 물질 생산을 설계하는 분야)과 합성생물학(생물의 구성 요소와 작동 체계를 설계하여 원하는 기능을 만드는 분야)을 위한 계산 방법을 연구한다. 미생물의 천연물(생물이 만드는 화합물) 생산을 늘릴 유전자 조절 대상을 예측하고, 생물 반응 경로를 모형으로 표현한다.[^research] 생합성 유전자 묶음과 생산 균주의 대사를 함께 바꾸는 연구, 여러 세균에서 표적 유전자의 작용을 낮추는 도구 개발이 그 예다.[^p6][^p7]

생물 자료를 분석하고 모형화하는 바이오정보학·계산생물학도 주요 갈래다. 유전체 규모 대사 모형(생물의 유전자 정보와 연결된 대사 반응을 생물 전체 범위에서 표현한 계산 모형)을 만들고, 목표한 물질 생산이나 생물의 상태를 예측한다.[^research] 소 근육세포의 대사 모형을 새로 구축해 실험 성장률과 예측을 대조한 연구는 배양육(동물에서 얻은 세포를 키워 만드는 고기) 연구와 배양 공정 최적화에 쓸 도구로 제시되었다.[^p4]

또 다른 갈래는 생물 기능을 예측하는 과학·공학 인공지능(Artificial Intelligence, AI)이다. 연구실은 기계학습(자료에서 규칙과 관계를 학습해 예측이나 판단을 하는 계산 방법)을 활용해 생물·화학 자료를 분석하며 생물학 문제를 위한 계산 모형을 개발한다.[^research] 최근에는 언어 모형에서 얻은 표현과 생화학 규칙을 결합해 유전자 조절 요소와 결합 물질 사이의 결합 세기를 예측했고, 세균이 단백질을 내보내는 데 필요한 신호 부분을 설계하는 모형도 개발했다.[^p1][^p2]

질병 관련 연구에서는 새 계산 절차를 만드는 갈래가 있다. 약물 내성 세포의 대사 상태를 바꿀 유전자 표적을 찾거나, 돌연변이와 대사물질·반응 경로의 관계를 예측한다. 대표 논문 3과 5는 각각 이런 계산 틀과 작업 절차의 개발을 다룬다.[^p3][^p5]

## 주요 연구 주제

### 생물 기능과 단백질 분비 신호의 계산 설계

RNA(Ribonucleic Acid, 리보핵산)는 유전 정보의 전달·조절과 생체 반응에 관여하는 물질이며, 유전자 발현은 유전 정보가 읽혀 기능하는 산물이 만들어지는 과정이다. 리보스위치(결합 물질을 감지하여 유전자 발현을 조절하는 RNA 요소)를 연구한다. 대표 논문 1은 언어 모형의 표현과 생화학 사전 지식을 결합해 자료가 제한된 조건에서 리보스위치의 결합 세기를 예측하는 틀을 제시했다.[^p1] 대표 논문 2는 단백질을 세포 밖으로 내보내도록 이끄는 신호 펩타이드의 배열을 생성하고 실험으로 검증했다. 펩타이드는 아미노산이 펩타이드 결합으로 이어진 물질이며, 아미노산은 아미노기와 카복실기를 함께 가진 유기 화합물이다.[^p2]

### 생물 대사 모형과 질병 표적 예측 방법

대사 모형의 반응 흐름(단위 시간에 반응을 거치는 물질의 양)을 계산하여 생물의 상태와 유전자 조작의 영향을 예측한다. 대표 논문 4는 소 근육세포의 대사를 표현하는 모형을 새로 구축했다.[^p4] 대표 논문 3은 유전자를 하나씩 제거한 경우의 반응 흐름을 모의하고, 그 결과를 군집 분석으로 묶어 약물 감수성을 높일 표적을 예측했다.[^p3] 대표 논문 5는 환자별 대사 모형과 돌연변이 자료를 함께 써 대사물질·유전자·경로의 관련 묶음을 예측하는 작업 절차를 개발했다.[^p5]

### 미생물 대사 경로와 유전자 작용 설계

대표 논문 6은 오비에도마이신(미생물이 만드는 화합물)을 만드는 유전자 묶음을 다른 생산 균주로 옮기고, 프로모터와 생산 균주 대사를 함께 바꾸어 생산을 늘렸다.[^p6] 대표 논문 7은 합성 조절 RNA를 이용해 여러 종류의 세균에서 유전자의 작용을 낮추는 플랫폼을 개발했다. 이 방법을 화학 원료와 천연 색소를 생산하는 균주의 설계에도 적용했다.[^p7]

## 대표 논문

KAIST 재직 시기의 2021–2026년 논문 가운데 연구 갈래와 최근 방법 개발을 고르게 보여 주는 7편을 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. 연구실이 게재 승인으로 적은 논문과 bioRxiv로 적은 논문은 그 상태를 함께 표시했다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자와 교수 역할 |
|---|---|---|---|---|
| 1 | 2026 | [LLM-guided prediction of riboswitch–ligand binding affinity under data-limited conditions](https://doi.org/10.1016/j.nbt.2026.08.008) · New Biotechnology (게재 승인) | 리보스위치의 배열과 구조, 결합 물질을 언어 모형이 만든 표현으로 나타내고 생화학 규칙과 결합했다. 자료가 적은 조건에서 결합 세기를 예측하며, 결합이 강하다고 과도하게 예측하는 문제를 줄이는 계산 틀을 제시했다.[^p1] | 1저자 Sunggi An, 마지막 저자 Hyun Uk Kim |
| 2 | 2026 | [Transformer-based prediction of Sec- and Tat-type signal peptides for enhanced bacterial protein secretion](https://doi.org/10.1002/biot.70204) · Biotechnology Journal | 주어진 단백질에 맞는 두 종류의 분비 신호를 생성하는 모형을 개발했다. 세균 자료로 학습한 뒤 Corynebacterium glutamicum에서 설계한 신호를 시험했으며, 두 표적 단백질에 대해 설계한 16개 가운데 15개가 분비에 성공했다.[^p2] | 1저자 Seongmo Kang, 마지막 저자 Hyun Uk Kim |
| 3 | 2025 | [Genome-scale knockout simulation and clustering analysis of drug-resistant breast cancer cells reveal drug sensitization targets](https://doi.org/10.1073/pnas.2425384122) · PNAS | 약물 내성 세포의 대사 모형에서 유전자를 하나씩 제거한 결과를 계산하고, 비슷한 결과끼리 묶어 약물에 민감한 세포의 상태로 돌아가게 할 표적을 찾았다. 예측한 표적을 억제했을 때 약물 감수성이 높아지는 것을 실험으로 검증했다.[^p3] | 1저자 JinA Lim, 마지막 저자 Hyun Uk Kim |
| 4 | 2024 | [Multi-omics analysis and genome-scale metabolic reconstruction of cattle Bos taurus for optimal production of cultured meat](https://doi.org/10.1101/2024.12.09.627468) · 연구실 기재 bioRxiv | 소 근육세포의 여러 생물 자료를 분석하고 소에 특화된 유전체 규모 대사 모형을 구축했다. 모형으로 예측한 생물량을 실제 성장률과 대조했으며, 배양육 연구와 배양 공정 최적화를 위한 도구로 제시했다.[^p4] | 1저자 Junkyu Lee, 마지막 저자 Hyun Uk Kim |
| 5 | 2024 | [Prediction of metabolites associated with somatic mutations in cancers by using genome-scale metabolic models and mutation data](https://doi.org/10.1186/s13059-024-03208-8) · Genome Biology | 환자별 대사 모형과 돌연변이 자료로 특정 유전자 변화에 연관된 대사물질과 반응 경로를 함께 예측하는 절차를 개발했다. 수집한 생물 자료와 공개된 여러 암의 자료를 이용해 예측한 관계를 검증했다.[^p5] | 1저자 GaRyoung Lee, 마지막 저자 Hyun Uk Kim |
| 6 | 2023 | [Heterologous overproduction of oviedomycin by refactoring biosynthetic gene cluster and metabolic engineering of host strain Streptomyces coelicolor](https://doi.org/10.1186/s12934-023-02218-8) · Microbial Cell Factories | 평소 실험 조건에서 잘 작동하지 않는 물질 생산 유전자 묶음을 다른 세균으로 옮겼다. 유전자 작동을 조절하는 부분과 생산 균주의 대사를 함께 바꾸어 오비에도마이신 생산을 늘렸다.[^p6] | 1저자 Boncheol Gu, 공저자 Hyun Uk Kim, 마지막 저자 Min‐Kyu Oh |
| 7 | 2023 | [Targeted and high-throughput gene knockdown in diverse bacteria using synthetic sRNAs](https://doi.org/10.1038/s41467-023-38119-y) · Nature Communications | 여러 세균에서 표적 유전자의 작용을 낮추는 합성 RNA 플랫폼을 개발했다. 화학 원료를 만드는 균주의 설계와 천연 색소를 많이 만드는 균주의 탐색에도 적용했다.[^p7] | 1저자 Jae Sung Cho, 공저자 Hyun Uk Kim, 마지막 저자 Sang Yup Lee |

## 교수와 전문 분야

김현욱은 KAIST 생명화학공학과 부교수다. 학과 소개는 학력을 연세대학교 학사(2005), KAIST 석사(2007)와 박사(2011)로 적고, 연구 관심 분야로 Biotechnology, Systems Biology, Biological Networks, Systems Medicine, Metabolic Engineering을 제시한다.[^faculty] 연구실 People 쪽은 생명화학공학과에 이어 Graduate School of Engineering Biology와 Department of AX, College of AI를 함께 적는다.[^people]

연구 소개와 대표 논문으로 보면 전문 분야는 생물 반응 네트워크의 계산 모형, 미생물 대사 설계, 생물 기능 예측 방법이다.[^research][^p1][^p2][^p6] SBML은 이상엽 특훈교수와 김현욱 교수가 함께 운영하는 Systems Metabolic Engineering and Systems Healthcare (SMESH) Laboratory의 일부이며, Metabolic and Biomolecular Engineering National Research Laboratory (MBEL)와 협력한다고 소개한다.[^smesh]

## 응용 분야

연구실은 미생물을 이용한 천연물 생산과 목표한 생물 기능의 설계를 응용 분야로 든다.[^research] 대표 논문은 단백질 분비, 배양육 연구와 배양 공정 최적화를 위한 도구, 화학 원료·천연 색소 생산, 질병 관련 대사 표적을 찾는 계산 방법을 다룬다.[^p2][^p3][^p4][^p7]

## 구성원

2026-11-05 연구실 People 쪽에 게시된 교수 외 구성원 22명이다. 과정과 시작 시기는 게시 표기를 따랐고, Graduate student는 대학원생으로 옮겼다. 「대표 논문 참여」는 전체 저자 이름이 완전히 일치할 때 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| Dr. Byung Tae Lee | 박사후연구원 | Spring 2025 |  |
| Dr. Seongmo Kang | 박사후연구원 | Spring 2026 | 2 |
| Dr. Sunggi An | 박사후연구원 | Fall 2026 | 1 |
| Yoo Jin Sung | 대학원생 | Spring 2021 |  |
| Eujin Hong | 대학원생 | Fall 2021 |  |
| Junkyu Lee | 대학원생 | Spring 2022 | 4 |
| Ye Rin Park | 대학원생 | Fall 2025 |  |
| Seo Young Kim | 대학원생 | Fall 2023 |  |
| Haechan Sung | 대학원생 | Spring 2024 |  |
| Jaehyun Kim | 대학원생 | Spring 2024 | 4 |
| Seok Hwan Yoon | 대학원생 | Spring 2024 |  |
| Byeongsub Lee | 대학원생 | Spring 2024 |  |
| Joon Young Kwon | 대학원생 | Fall 2024 |  |
| Taeyoung Lee | 대학원생 | Spring 2025 |  |
| Jihi Yeom | 대학원생 | Spring 2025 |  |
| Soomin Lee | 대학원생 | Spring 2025 |  |
| Nithya Manickavasagam | 대학원생 | Fall 2025 |  |
| Lavi Hong | 대학원생 | Spring 2026 |  |
| Akira Mishima | 대학원생 | Spring 2026 |  |
| Jaeseung Kim | 대학원생 | Spring 2026 |  |
| Christian Kronborg Cantalapiedra | 방문 학생 | Fall 2026 |  |
| Jonas Schneider | 방문 학생 | Fall 2026 |  |

## 졸업생 진로

People 쪽 Alumni에 게시된 13명이다. 학위·과정과 진로는 연구실의 표기다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Dr. Mun Su Kwon | 2026 Postdoctoral researcher; 2025 Ph.D., Chemical and Biomolecular Engineering, KAIST; 2021 M.S., Chemical and Biomolecular Engineering, KAIST | Korea Research Institute of Bioscience & Biotechnology (permanent) |
| Sofia Mun | 2026 M.S., Chemical and Biomolecular Engineering, KAIST | Technical University of Denmark |
| Dr. Hae Deok Jung | 2025 Ph.D., Chemical and Biomolecular Engineering, KAIST; 2021 M.S., Chemical and Biomolecular Engineering, KAIST | Dong-A ST |
| Anna Svetlova | Visiting student (Fall 2024); PhD Student, Technical University of Denmark |  |
| Dr. Junhyeok Jeon | 2024 Ph.D.,  Chemical and Biomolecular Engineering, KAIST; 2021 M.S., Chemical and Biomolecular Engineering, KAIST | SK Hynix |
| Dr. Sang Mi Lee | 2024 Ph.D.,  Chemical and Biomolecular Engineering, KAIST | Harvard Medical School |
| Dr. GaRyoung Lee | 2024 Ph.D.,  Chemical and Biomolecular Engineering, KAIST | Harvard Medical School |
| Dr. Mohammad Rifqi Ghiffary | 2023 Postdoctoral Researcher, BioProcess Engineering Research Center, KAIST; 2023 Ph.D.,  Chemical and Biomolecular Engineering, KAIST; 2018 M.S., Biotechnology, Wageningen University and Research, The Netherlands | Antheia, Singapore |
| Minji Kim | 2023 M.S., Chemical and Biomolecular Engineering, KAIST | Technical University of Denmark |
| Sung Han Bae | 2023 M.S., Chemical and Biomolecular Engineering, KAIST | HITS |
| Dr. Komal Sharma | 2023 Postdoctoral Researcher, BioProcess Engineering Research Center, KAIST; 2022 Ph.D.,  Chemical and Biomolecular Engineering, KAIST; 2016 M.S., Biotechnology, Birla Institute of Technology & Science, Pilani, India | Oak Ridge National Laboratory |
| Joshua Julio Adidjaja | 2022 M.S., Chemical and Biomolecular Engineering, KAIST | Bionomic, Netherlands |
| Dr. Shuan Chen | 2023 Ph.D.,  Chemical and Biomolecular Engineering, KAIST; 2020 M.S., Chemical and Biomolecular Engineering, KAIST | SB Intuitions (a SoftBank subsidiary), Japan |

## 최근 5년 논문 목록

연구실 Publications의 2021–2026년 구역의 논문 32건이다. 학술지 논문뿐 아니라 bioRxiv로 적은 논문과 책 장 1건을 포함한다. 연도·저자·제목·발표처는 누리집의 표기를 따랐고, 게재 승인으로 적힌 항목은 출판 논문과 구분했다. 게재 승인 항목의 연도는 누리집 연도 구역 표기다. 저자 이름 뒤의 1과 *는 누리집 표시다.[^pubs]

**2026**

- An S1, Mun S1, Jung Y\*, Kim HU\*. LLM-guided prediction of riboswitch–ligand binding affinity under data-limited conditions. New Biotechnology. 게재 승인. <https://doi.org/10.1016/j.nbt.2026.08.008>
- Yoon SH, Park YR, Kim HU\*. A Bayesian network-based framework for causal cancer drug target discovery integrating patient and cell line data. bioRxiv: https://doi.org/10.64898/2026.07.13.736676 (July 2026)
- Lee BT1, Lee B1, Kwon JY1, Weber T\*, Kim HU\*. AI and mechanistic modeling for characterizing biosynthetic pathways of natural products. Natural Product Reports 43, 787-802 (May 2026) <https://doi.org/10.1039/d5np00059a>
- Rudenko A, Booth TJ, Williams SE, Blin K, Kim HU, Weber T, Charusanti P. Unraveling rare codon bias in Actinomycetota: lineage-specific and 5’ terminal enrichment across 1936 genomes. BMC Genomics 27, 370 (March 2026) <https://doi.org/10.1186/s12864-026-12708-9>
- Kang S1, Lee SM1, Park RH, Lee G, Lee JH, Jeong KJ\*, Kim HU\*. Transformer-based prediction of Sec- and Tat-type signal peptides for enhanced bacterial protein secretion. Biotechnology Journal 21, e70204 (March 2026) <https://doi.org/10.1002/biot.70204>
- Moon CW, Ghiffary MR, Prabowo CPS, Kim HU, Lee SY. Metabolic engineering of Corynebacterium glutamicum for vitamin B12-independent production of 3-hydroxypropionic acid. Metabolic Engineering 94, 90-98 (March 2026) <https://doi.org/10.1016/j.ymben.2025.11.013>

**2025**

- Lee YK1, Kang S1, Lim J1, Kim K, Kim SM, Casel MAB, Choi I, Choi YK\*, Kim HU\*, Kim Y\*. Rapid discovery of antiviral targets through dimensionality reduction of genome-scale metabolic models. bioRxiv: https://doi.org/10.1101/2025.10.02.679942 (December 2025)
- Lee BT, Mohite OS, Kwon MS, Kang HS, Weber T\*, Lee SY\*, Kim HU\*. Pan-reactome analysis of Streptomyces strains reveals association and disconnection between primary and secondary metabolism. Metabolic Engineering 92, 241-251 (November 2025) <https://doi.org/10.1016/j.ymben.2025.08.005>
- Lee S, Kwon MS, Kim HU in Comprehensive Biotechnology, 4th Edition, Artificial intelligence for multiscale biological system design and optimization (Elsevier, October 2025, In press) <https://doi.org/10.1016/b978-0-443-24738-5.00003-3>
- Lim J1, Jung HD1, Park SY, Jeon M, Kim DS, Cho R, Han D, Ryu HS, Kim Y\*, Kim HU\*. Genome-scale knockout simulation and clustering analysis of drug-resistant breast cancer cells reveal drug sensitization targets. Proceedings of the National Academy of Sciences U S A (PNAS) 122, e2425384122 (June 2025) <https://doi.org/10.1073/pnas.2425384122>
- Zdouc MM, Blin K, …, Kim HU, …, Lee BT, …, Weber T, Medema MH. MIBiG 4.0: advancing biosynthetic gene cluster curation through global collaboration. Nucleic Acids Research 53, D678-D690  (January 2025) <https://doi.org/10.1093/nar/gkae1115>

**2024**

- Lee J1, Kim J1, Bae HW1, Kim M, Jung BK, Kim J, Lee S\*, Kim HU\*. Multi-omics analysis and genome-scale metabolic reconstruction of cattle Bos taurus for optimal production of cultured meat. bioRxiv: https://www.biorxiv.org/content/10.1101/2024.12.09.627468v1 (December 2024)
- Kwon MS1, Lee J1, Kim HU\*. A machine learning framework for extracting information from biological pathway images in the literature. Metabolic Engineering  86, 1-11 (November 2024) <https://doi.org/10.1016/j.ymben.2024.09.001>
- Raman K,  Kratochvíl M, Olivier BG,  König M, ..., Nielsen J, Lee G, Lee SM, Kim GB, ..., Kim HU, Lee SY, ...,  Malik-Sheriff RS. FROG analysis ensures the reproducibility of genome scale metabolic models. bioRxiv: https://www.biorxiv.org/content/10.1101/2024.09.24.614797v1 (September 2024)
- Lee J1, Lee BT1, Kwon MS1, Kim HU\*. Metabolic modeling of microorganisms involved in anaerobic digestion. Biotechnology and Bioprocess Engineering 29, 613-624 (August 2024) <https://doi.org/10.1007/s12257-024-00128-z>
- Bae SH1, Sim MS1, Jeong KJ, He D, Kwon I, Kim TW\*, Kim HU\*, Choi J\*. Intracellular flux prediction of recombinant Escherichia coli producing gamma-aminobutyric acid. Journal of Microbiology and Biotechnology 34, 978-984 (April 2024) <https://doi.org/10.4014/jmb.2312.12022>
- Lee G1, Lee SM1, Lee S, Jeong CW, Song H, Lee SY, Yun H\*, Koh Y\*, Kim HU\*. Prediction of metabolites associated with somatic mutations in cancers by using genome-scale metabolic models and mutation data. Genome Biology 25, 66 (March 2024) <https://doi.org/10.1186/s13059-024-03208-8>
- Sharma K, Ghiffary MR, Lee G, Kim HU\*. Efficient production of an antitumor precursor actinocin and other medicinal molecules from kynurenine pathway in Escherichia coli. Metabolic Engineering 81, 144-156 (January 2024) <https://doi.org/10.1016/j.ymben.2023.11.008>

**2023**

- Song S1, Koh Y1, Kim S1, Lee SM, Kim HU\*, Ko JM\*, Lee SH\*, Yoon SS\*, Park S\*. Systematic analysis of Mendelian disease-associated gene variants reveals new classes of cancer-predisposing genes. Genome Medicine 15, 107 (December 2023) <https://doi.org/10.1186/s13073-023-01252-w>
- Kim WJ1, Lee Y1, Kim HU1, Ryu JY, Yang JE, Lee SY. Genome-wide identification of overexpression and downregulation gene targets based on the sum of covariances of the outgoing reaction fluxes. Cell Systems 14, 990-1001 (November 2023) <https://doi.org/10.1016/j.cels.2023.10.005>
- Mullowney MW, Duncan KR, Elsayed SS, Garg N, van der Hooft JJJ, Martin NI, Meijer D, Terlouw BR, Biermann F, Blin K, Durairaj J, Gorostiola González M, Helfrich EJN, Huber F, Leopold-Messer S, Rajan K, de Rond T, van Santen JA, Sorokina M, Balunas MJ, Beniddir MA, van Bergeijk DA, Carroll LM, Clark CM, Clevert DA, Dejong CA, Du C, Ferrinho S, Grisoni F, Hofstetter A, Jespers W, Kalinina OV, Kautsar SA, Kim H, Leao TF, Masschelein J, Rees ER, Reher R, Reker D, Schwaller P, Segler M, Skinnider MA, Walker AS, Willighagen EL, Zdrazil B, Ziemert N, Goss RJM, Guyomard P, Volkamer A, Gerwick WH, Kim HU, Müller R, van Wezel GP, van Westen GJP, Hirsch AKH, Linington RG, Robinson SL, Medema MH. Artificial intelligence for natural product drug discovery. Nature Reviews Drug Discovery 22, 895-916 (November 2023) <https://doi.org/10.1038/s41573-023-00774-7>[^s03]
- Gu B, Kim DG, Kim DK, Kim M, Kim HU\*, Oh MK\*. Heterologous overproduction of oviedomycin by refactoring biosynthetic gene cluster and metabolic engineering of host strain Streptomyces coelicolor. Microbial Cell Factories 22, 212 (October 2023) <https://doi.org/10.1186/s12934-023-02218-8>
- Yun KH, Sharma K, Kim HU, Bae TH. Modification of a PES microfiltration membrane to enhance sterile filtration by inhibiting protein adsorption. Journal of Industrial and Engineering Chemistry 123, 311-319 (July 2023) <https://doi.org/10.1016/j.jiec.2023.03.048>
- Lee JA1, Kim HU1, Na JG1, Ko YS, Cho JS, Lee SY. Factors affecting the competitiveness of bacterial fermentation. Trends in Biotechnology 41, 798-816 (June 2023) <https://doi.org/10.1016/j.tibtech.2022.10.005>
- Lee G1, Lee SM1, Kim HU\*. A contribution of metabolic engineering to addressing medical problems: metabolic flux analysis. Metabolic Engineering 77, 283-293 (May 2023) <https://doi.org/10.1016/j.ymben.2023.04.008>[^s04]
- Cho JS, Yang D, Prabowo CPS, Ghiffary MR, Han T, Choi KR, Moon CW, Zhou H, Ryu JY, Kim HU, Lee SY. Targeted and high-throughput gene knockdown in diverse bacteria using synthetic sRNAs. Nature Communications 14, 2359 (April 2023) <https://doi.org/10.1038/s41467-023-38119-y>
- Kwon MS, Adidjaja JJ, Kim HU\*. Predicting the effects of cultivation condition on gene regulation in Escherichia coli by using deep learning. Computational and Structural Biotechnology Journal 21, 2613-2620 (April 2023) <https://doi.org/10.1016/j.csbj.2023.04.010>
- Hong E, Jeon J, Kim HU\*. Recent development of machine learning models for the prediction of drug-drug interactions. Korean Journal of Chemical Engineering 40, 276-285 (February 2023) <https://doi.org/10.1007/s11814-023-1377-3>[^s06]

**2022**

- Ghiffary MR, Prabowo CPS, Adidjaja JJ, Lee SY, Kim HU\*. Systems metabolic engineering of Corynebacterium glutamicum for the efficient production of β-alanine. Metabolic Engineering 74, 121-129 (November 2022) <https://doi.org/10.1016/j.ymben.2022.10.009>
- Cho MK1, Lee BT1, Kim HU\*, Oh MK\*. Systems metabolic engineering of Streptomyces venezuelae for the enhanced production of pikromycin. Biotechnology and Bioengineering 119, 2250-2260 (August 2022) <https://doi.org/10.1002/bit.28114>
- Jo HG1, Adidjaja JJ1, Kim DK, Park BS, Lee N, Cho BK, Kim HU\*, Oh MK\*. Comparative genomic analysis of Streptomyces rapamycinicus NRRL 5491 and its mutant overproducing rapamycin. Scientific Reports 12, 10302 (June 2022) <https://doi.org/10.1038/s41598-022-14199-6>
- Baek Y, Lee S, Son J, Lee T, Oh J-M, Lee SH, Kim HU, Seo SW, Park SJ, Yoo HY, Park C. Efficient production of naringin acetate with different acyl donors via enzymatic transesterification by lipases. International Journal of Environmental Research and Public Health 19, 2972 (March 2022) <https://doi.org/10.3390/ijerph19052972>

## 수상과 선정

연구실 소식에서 2021-10-13–2026-10-13에 해당하는 수상·선정 17건이다. 수상 이름과 등급은 게시 표기를 따랐다.[^news]

- 2026-10-02 · Byung Tae Lee가 2026 KSBB Fall Meeting and International Symposium에서 KRIBB Young Researcher Award를 받았다.
- 2026-10-02 · Junkyu Lee가 2026 KSBB Fall Meeting and International Symposium에서 Best Oral Presentation Award를 받았다.
- 2026-06-04 · Taeyoung Lee가 KAIST Open Source Impact 주최 KAIST Open Source x AI Hackathon에서 장려상을 받았다.
- 2026-05-29 · Soomin Lee가 2026 제16회 생명화학공학과 대학원생 심포지엄에서 Excellence Award (Oral Presentation)를 받았다.
- 2026-05-19 · 김현욱이 임형규 Link Genesis-Best Teacher Award를 받았다.
- 2026-04-30 · Soomin Lee가 Google Summer of Code 2026 프로그램 참여가 확정되었다.
- 2025-12-04 · 김현욱이 Clarivate의 Highly Cited Researcher로 선정되었다.
- 2023-11-15 · Hae Deok이 BIOINFO 2023에서 Best Poster Award를 받았다.
- 2023-10-06 · GaRyoung이 2023 KSBB Fall Meeting and International Symposium에서 Best Poster Presentation Award를 받았다.
- 2023-04-14 · Eujin이 2023 KSBB Spring Meeting and International Symposium에서 Best Poster Presentation Award를 받았다.
- 2022-12-04 · Seongmo가 제33회 International Symposium on Chemical Engineering에서 Oral Presentation Award를 받았다.
- 2022-10-21 · Sang Mi가 BIOINFO 2022에서 Outstanding Poster Award를 받았다.
- 2022-09-30 · Minji가 2022 KSBB Fall Meeting and International Symposium에서 Best Poster Presentation Award를 받았다.
- 2022-06-10 · Komal이 2022 KIChE Spring Meeting에서 Best Poster Presentation Award를 받았다.
- 2022-05-27 · Sang Mi가 2022 생명화학공학과 대학원생 심포지엄에서 Best Poster Presentation Award를 받았다.
- 2022-02-24 · Sang Mi가 아산사회복지재단 의생명과학분야 장학생으로 선발되었다.
- 2021-10-29 · Byung Tae가 2021 KIChE Fall Meeting and International Symposium에서 Best Oral Presentation Award를 받았다.

## 소식

연구실 소식의 논문 발표·연구 협약·학술 활동 관련 게시 11건이다.[^news]

- 2026-01-01 · 김현욱이 Chemical Engineering Journal의 Editor로 편집위원회에 합류했다.
- 2025-11-07 · 김현욱이 Biotechnology and Bioengineering의 Early Career Researcher Editorial Board에 합류했다.
- 2025-07-07 · 약물 내성 유방암 세포의 대사 유전자 제거 모의와 군집 분석으로 약물 감수성을 높일 표적을 찾는 논문을 PNAS에 발표했다고 알렸다.
- 2024-11-28 · 문헌의 생물 경로 그림에서 정보를 추출하는 기계학습 틀의 Metabolic Engineering 논문을 소개했다.
- 2024-04-12 · 김현욱의 Expert Opinion이 Nature Metabolism에 실렸다고 알렸다.
- 2024-04-05 · 더존비즈온과 KAIST의 공동연구 업무협약식을 알렸다.
- 2024-03-18 · 유전체 규모 대사 모형과 돌연변이 자료로 암의 돌연변이 관련 대사물질을 예측하는 Genome Biology 논문을 소개했다.
- 2022-06-18 · 라파마이신 생산 균주와 과잉 생산 변이 균주의 비교 유전체 분석 논문을 Scientific Reports에 발표했다고 알렸다.
- 2022-04-20 · 피크로마이신 생산을 늘리는 Streptomyces venezuelae의 시스템 대사공학 논문을 Biotechnology and Bioengineering에 발표했다고 알렸다.
- 2022-04-01 · 김현욱이 Journal of Microbiology and Biotechnology의 편집위원회에 합류했다.
- 2022-03-12 · 김현욱이 Frontiers in Genetics의 Statistical Genetics and Methodology 분야 Associate Editor로 편집위원회에 합류했다.

## 연락과 위치

학과 교수 소개의 업무 이메일은 ehukim@kaist.ac.kr, 기관 전화는 +82-42-350-3915이며, 위치는 Bldg W14 Room 304다. 학과가 적은 기관 주소는 대전광역시 유성구 대학로 291, KAIST다.[^faculty]

## 각주
[^research]: SBML, Research. <https://sbml.kaist.ac.kr/research> (관측 2026-11-05).

[^faculty]: KAIST 생명화학공학과, Hyun Uk Kim (김현욱) 교수 소개. <https://cbe.kaist.ac.kr/boards/view/faculty/50/1/> (관측 2026-11-05).

[^people]: SBML, People. <https://sbml.kaist.ac.kr/people> (관측 2026-11-05).

[^smesh]: SBML, SMESH. <https://sbml.kaist.ac.kr/smesh> (관측 2026-11-05).

[^pubs]: SBML, Publications. <https://sbml.kaist.ac.kr/publications> (관측 2026-11-05).

[^news]: SBML, News. <https://sbml.kaist.ac.kr/news> (관측 2026-11-05).

[^p1]: S. An, S. Mun, Y. Jung, H. U. Kim, New Biotechnology (2026). <https://doi.org/10.1016/j.nbt.2026.08.008> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5048072583> (관측 2026-11-05).

[^p2]: S. Kang 외, H. U. Kim, Biotechnology Journal (2026). <https://doi.org/10.1002/biot.70204> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5048072583> (관측 2026-11-05).

[^p3]: J. Lim 외, H. U. Kim, Proceedings of the National Academy of Sciences (2025). <https://doi.org/10.1073/pnas.2425384122> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5048072583> (관측 2026-11-05).

[^p4]: J. Lee 외, H. U. Kim, bioRxiv (Cold Spring Harbor Laboratory) (2024). <https://doi.org/10.1101/2024.12.09.627468> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5048072583> (관측 2026-11-05).

[^p5]: G. Lee 외, H. U. Kim, Genome biology (2024). <https://doi.org/10.1186/s13059-024-03208-8> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5048072583> (관측 2026-11-05).

[^p6]: B. Gu 외, M.-K. Oh, Microbial Cell Factories (2023). <https://doi.org/10.1186/s12934-023-02218-8> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5048072583> (관측 2026-11-05).

[^p7]: J. S. Cho 외, S. Y. Lee, Nature Communications (2023). <https://doi.org/10.1038/s41467-023-38119-y> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5048072583> (관측 2026-11-05).

[^s03]: Michael W. Mullowney 외, Marnix H. Medema, Nature Reviews Drug Discovery (2023). <https://doi.org/10.1038/s41573-023-00774-7> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1038/s41573-023-00774-7%22> (관측 2026-11-05–2026-11-06).

[^s04]: GaRyoung Lee, Sang Mi Lee, Hyun Uk Kim, Metabolic Engineering (2023). <https://doi.org/10.1016/j.ymben.2023.04.008> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.ymben.2023.04.008%22> (관측 2026-11-05–2026-11-06).

[^s06]: Eujin Hong, Junhyeok Jeon, Hyun Uk Kim, Korean Journal of Chemical Engineering (2023). <https://doi.org/10.1007/s11814-023-1377-3> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1007/s11814-023-1377-3%22> (관측 2026-11-05–2026-11-06).

# Jung Lab

**KAIST 생명과학과 · 정인경 부교수**

- 영문 이름: Epigenomics & Computational Biology Lab
- 분야: 3차원 유전체·후성유전 조절·단일세포 분석
- 대분야: 기초생명·생물물리, 컴퓨팅·AI
- 태그: 바이오정보학·계산생물학[^structure][^learning], 단일 세포·공간 오믹스[^learning][^p3], 후성유전 조절·노화 리프로그래밍[^main][^p1][^p2], 과학·공학 AI[^learning]
- 홈페이지: <https://sites.google.com/view/junglab-kaist/main>
- 근거와 출처: [Jung Lab 근거 페이지](junglab-sources.md)

> 유전 물질이 입체적으로 접히는 구조와 세포마다 달라지는 유전자 작동 원리를 밝히고, 이를 분석하는 계산법과 학습 모형을 만드는 연구실이다.

## 무엇을 연구하나

유전자(기능성 산물을 만드는 유전 정보의 단위)가 언제 얼마나 쓰이는지는 세포의 성질을 결정한다. 이 연구실은 유전체(생물이나 세포가 가진 유전 물질 전체)의 입체 구조와 후성유전(유전 정보의 배열을 바꾸지 않고 그 정보가 사용되는 상태를 조절하는 현상)을 연결해 유전자 조절 원리를 연구한다. 특히 유전체의 조절 영역이 어떤 유전자에 작용하는지와 그 관계가 세포 종류에 따라 어떻게 달라지는지에 초점을 둔다.[^main][^structure]

유전 물질은 핵 안에 입체적으로 포장되어 있어, 배열상 멀리 떨어진 구간도 공간에서는 가까이 만날 수 있다. 연구실은 이런 접촉을 측정하고 수학적으로 설명하는 실험·계산 방법을 개발한다.[^structure] 대표 논문 4에서는 서로 다른 염색체 사이의 접촉을 설명하는 확률 모형을 제안했고, 대표 논문 8에서는 효모의 입체 구조를 조절하는 인자들의 서로 다른 역할을 밝혔다.[^p4][^p8]

세포가 성숙하는 과정의 조절 원리도 연구한다. 대표 논문 1은 CREST라는 조절 인자(유전자 작동을 조절하는 분자)가 운동신경세포의 성숙 관련 유전자 작동을 돕는 과정을 설명한다. 대표 논문 2는 별아교세포(신경세포의 활동 환경을 유지하고 물질대사와 면역반응에 관여하는 신경계 세포)의 출생 초기 유전자 조절 상태가 이후 면역반응의 준비상태에 영향을 준다는 결과다. 두 연구는 발달 시기와 세포 종류에 따라 유전 정보가 사용되는 방식을 다룬다.[^p1][^p2]

연구실은 단일세포 오믹스(세포별로 여러 분자 성분의 집합을 체계적으로 측정·분석하는 기술) 자료의 품질을 높이고 서로 다른 측정 자료를 함께 분석하는 방법도 개발한다.[^learning] 딥러닝(여러 층으로 연결된 계산 단위로 자료의 표현을 단계적으로 학습하는 기계학습 분야)으로 유전 물질의 접촉을 예측하거나 세포별 자료를 복원하는 계산 틀을 만든다.[^learning] 대표 논문 3은 같은 세포의 조절 정보를 함께 측정하는 기술이고, 대표 논문 5는 단일세포의 유전체 구조 변이(유전체의 큰 구간이 재배열되는 등 배열 구조가 바뀐 변화) 양상을 분류하는 계산 틀이다.[^p3][^p5]

## 주요 연구 주제

### 입체 유전체 구조와 유전자 조절

연구실은 유전 정보의 배열상 거리가 아닌 실제 입체 접촉을 이용해 조절 영역과 목표 유전자의 관계를 밝힌다. 입체 구조가 만들어지고 바뀌는 원리를 연구하면서, 접촉 자료의 처리·보정과 측정값의 정량 비교 방법도 개발한다.[^main][^structure][^p4][^p7]

### 세포 성숙의 후성유전 조절

운동신경세포와 별아교세포의 성숙 과정에서 특정 조절 인자가 유전자 작동과 이후 세포 반응을 어떻게 정하는지 연구한다. 성숙한 세포의 기능을 유지하는 조절 관계와, 발달 초기에 정해진 상태가 남기는 영향을 함께 다룬다.[^p1][^p2]

### 계산·단일세포 분석법 개발

세포별 유전자 작동 자료와 입체 접촉 자료를 분석하는 새 계산 방법을 만든다. 딥러닝을 통한 세포별 자료 복원, 여러 측정 자료의 통합, 유전 물질의 접촉 예측이 주요 갈래다. 암 유전체의 구조 변화에 특화한 기계학습 방법도 개발했다.[^learning][^p3][^p5][^p6][^p7]

## 대표 논문

KAIST 재직 시기의 2021–2026년 논문에서 연구 갈래를 고르게 담고, 교신저자 참여와 최근 연구를 고려해 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. GEM-Finder는 medRxiv 사전 공개본이다.

| 번호 | 연도 | 논문·발표처 | 주요 저자와 교수 역할 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2026 | [CREST functions as a molecular bridge between neuron-specific enhancers and epigenetic regulators in mature motor neurons](https://doi.org/10.1038/s41467-026-78396-x) · *Nature Communications* | 1저자 Kaitlin N. Montanera·Andrew Lee·Woobin Yun(공동 기여); 교신 Inkyung Jung·Ho Sung Rhee | 생쥐 배아줄기세포를 운동신경세포로 분화시킨 실험에서 CREST가 조절 인자들을 연결해 성숙 관련 유전자를 활성화하고 전구세포 유전자를 억제한다는 원리를 밝혔다.[^p1] |
| 2 | 2025 | [NR3C1-mediated epigenetic regulation suppresses astrocytic immune responses in mice](https://doi.org/10.1038/s41467-025-64088-5) · *Nature Communications* | 1저자 Seongwan Park·Hyeonji Park(공동 기여); 교신 Won-Suk Chung·Inkyung Jung | 생쥐에서 출생 초기 별아교세포의 NR3C1이 이후 면역반응의 준비상태를 정함을 보였다. 초기 손실과 후기 손실의 영향이 달라 발달 시기의 중요성을 드러냈다.[^p2] |
| 3 | 2026 | [Trimodal single-cell profiling of transcriptome, epigenome and 3D genome in complex tissues with scHiCAR.](https://doi.org/10.1038/s41587-026-03013-7) · *Nature biotechnology* | 1저자 Xiaolin Wei·Yueyuan Xu·Dongchan Yang(공동 기여); 교신 Inkyung Jung·Yarui Diao | 같은 세포에서 유전자 작동, 유전 물질이 열려 있는 상태, 입체 접촉을 함께 측정하는 scHiCAR 기술을 개발했다. 복잡한 조직의 세포 종류별 조절 관계와 근육 줄기세포 재생 과정의 변화를 분석했다.[^p3] |
| 4 | 2023 | [Probabilistic establishment of speckle-associated inter-chromosomal interactions](https://doi.org/10.1093/nar/gkad211) · *Nucleic Acids Research* | 1저자 Jaegeon Joo·Sunghyun Cho(공동 기여); 교신 Yongdae Shin·Inkyung Jung | 서로 다른 염색체의 접촉을 분석하는 계산법을 제시하고, 개별 유전 물질 구간이 핵 속 구조물과 확률적으로 만나는 행동이 집단 수준의 접촉 양상을 설명한다는 모형을 제안했다.[^p4] |
| 5 | 2026 | [scCAPReSE: detection of large-scale genomic rearrangements from single-cell Hi-C based on few-shot learning](https://doi.org/10.1186/s44342-026-00069-4) · *Genomics & Informatics* | 1저자 Kyukwang Kim; 교신 Chul-Hwan Lee·Inkyung Jung | 적은 학습 예시로 단일세포의 유전체 구조 변이 양상을 분류하는 scCAPReSE 계산 틀을 개발했다. 미리 학습한 영상 모형의 표현을 이용하며, 암세포 사이에서 달라지는 입체 접촉의 차이도 분석했다.[^p5] |
| 6 | 2025 | [GEM-Finder: dissecting GWAS variants via long-range interacting cis-regulatory elements with differentiation-specific genes](https://doi.org/10.1101/2025.03.02.25323165) · *medRxiv 사전 공개본* | 1저자 Gyeongsik Park·Andrew J. Lee(공동 기여); 교신 Inkyung Jung | 유전자 작동·조절 상태·입체 접촉 자료를 통합하는 GEM-Finder 분석 틀을 제안했다. 세포 분화 단계별 유전자와 연결된 조절 영역을 찾아 유전 변이와 질환·형질의 관계를 해석한다.[^p6] |
| 7 | 2026 | [Comparative analyses of ChIP-seq, CUT&RUN and CUT&Tag for Polycomb chromatin profiling](https://doi.org/10.5483/bmbrep.2025-0247) · *BMB Reports* | 1저자 Yoonji Oh; Inkyung Jung 공저자; 마지막 저자 Chul-Hwan Lee | 유전 물질의 조절 상태를 재는 서로 다른 측정법의 신호를 비교할 수 있도록 정량 보정 전략을 개발했다. 각 기법의 신호 형태를 보존하면서 신호 크기를 같은 기준으로 맞춘다.[^p7] |
| 8 | 2021 | [A compendium of chromatin contact maps reflecting regulation by chromatin remodelers in budding yeast](https://doi.org/10.1038/s41467-021-26629-6) · *Nature Communications* | 1저자 Hyelim Jo; Inkyung Jung 공저자; 교신 Daeyoup Lee | 효모에서 염색질을 재배열하는 인자 8종이 3차원 유전체 구조에 서로 다르게 기여함을 비교했다. 그중 Chd1p, Swr1p, Sth1p 세 인자의 역할은 염색체 위치와 세포주기 단계에 따라 달랐다.[^p8] |

## 교수와 전문 분야

정인경(Inkyung Jung) 부교수는 KAIST에서 바이오시스템 학사와 바이오및뇌공학 박사 학위를 받았다. KAIST와 미국 Ludwig Institute for Cancer Research에서 박사후연구원을 지냈으며, 연구실은 2016년 10월 5일 KAIST 생명과학과에서 출범했다.[^professor][^news]

전문 분야는 유전 물질의 입체 구조에 기반한 유전자 조절과 단일세포 자료의 계산 분석이다. 최근 연구는 세포 성숙을 조절하는 원리, 염색체 접촉의 확률 모형, 유전체 구조 변이 분류와 측정 자료의 정량 분석을 함께 다룬다.[^dept][^p1][^p2][^p4][^p5][^p7]

## 응용 분야

개발한 기술은 여러 세포가 섞인 조직에서 세포 종류와 유전 정보의 조절 상태를 해석하는 데 쓰인다. 암 유전체 연구에서는 세포마다 달라지는 유전체 구조 변이 양상을 분류하고, 그 차이를 정량적으로 해석한다.[^p3][^p5]

## 구성원

2026년 11월 13일 연구실 Current Members에 게시된 책임연구자 1명, 박사후연구원 2명, 박사과정 10명이다. 시작은 합류 소식의 학기 표기이며 과정과 연구 주제는 현재 구성원 페이지 표기다. 「대표 논문 참여」는 전체 저자 목록과 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members][^news]

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Inkyung Jung | Principal Investigator |  |  | 1, 2, 3, 4, 5, 6, 7, 8 |
| Baekgyu Choi | 박사후연구원 |  | single cell multi-omics |  |
| Kyukwang Kim | 박사후연구원 |  | Bioinformatics, cancer 3D genome, and deep learning | 3, 4, 5 |
| Jaegeon Joo | 박사과정 |  | 3D-chromatin structure | 2, 4 |
| Seyoung Jin | 박사과정 | 2022년 가을학기 | Single cell omics |  |
| Sang Hyun Lee | 박사과정 | 2023년 봄학기 | 3D chromatin organization |  |
| Gyeongsik Park | 박사과정 | 2024년 봄학기 | 3D-chromatin structure | 6 |
| Seongwoo Kim | 박사과정 | 2024년 봄학기 | 3D-chromatin structure |  |
| Hyunho Yang | 박사과정 | 2025년 가을학기 | Bioinformatics, Single cell omics |  |
| Dain Kang | 박사과정 | 2026년 봄학기 | Spatial omics, Single-cell omics |  |
| Byeongjun Choi | 박사과정 | 2026년 봄학기 | Single cell multi-omics |  |
| Jungin Park | 박사과정 | 2026년 봄학기 | Single Cell 3D epigenomics |  |
| Euikyoung Song | 박사과정 | 2026년 가을학기 | Bioinformatics, Single cell omics |  |

## 졸업생과 이전 구성원

Alumni에 게시된 박사후연구원 4명, 박사 5명, 석사 2명, 연구참여자 3명이다. 연도는 게시된 해당 학위의 종료 연월이고 진로는 연구실 표기다. Baekgyu Choi와 Kyukwang Kim은 현재 박사후연구원 명단에도 올라 있다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| KeeOk Haam | 박사후연구원 | Researcher at Korea Research Institute of Bioscience and Biotechnology (KRIBB) |
| Sion Yi | 박사후연구원 | Researcher at Daegu Gyeongbuk Medical Innovation Foundation (DGMIF) |
| Sunwoo Min | 박사후연구원 | Assistant Professor at Chungnam National University |
| Dongchan Yang | 박사후연구원 | Postdoc Fellow at Dongguk University |
| Andrew Jeoungun Lee | Ph.D. (2022.02) | Postdoc Fellow at Post Boston Children’s Hospital/Broad Institute |
| Mooyoung Kim | Ph.D. (2024.02) | Researcher |
| Seongwan Park | Ph.D. (2025.02) | Postdoc Fellow at Institute for Basic Science |
| Baekgyu Choi | Ph.D. (2025.08) | Postdoc Fellow at KAIST |
| Kyukwang Kim | Ph.D. (2026.02) | Postdoc Fellow at KAIST |
| Jung-Hyun Eom | M.S. (2019.08) | PharmaVentures |
| Yunkyu Bae | M.S. (2025.08) | Researcher |
| Ben Kim | Undergraduate Research Program |  |
| Jayeong Ryu | Undergraduate Research Program |  |
| Seungbeom Han | Research student |  |

## 최근 논문 목록 (2021–2026)

연구실 Publications의 2021–2026년 구역과 Preprints에 게시된 16편이다. 저자·제목·발표처는 연구실 표기이며 *는 공동 기여, #는 교신저자를 뜻한다. scHyena는 arXiv 사전 공개본, GEM-Finder는 medRxiv 사전 공개본이다. GEM-Finder 뒤의 RECOMB2025는 연구실 기재 표기다.[^publications][^p6]

**2026**

- Montanera KN\*, Lee AJ\*, Yun W\*, Ialongo A, Yeh SY, Jung I#, Rhee HS# (2026) CREST functions as a molecular bridge between neuron - specific enhancers and epigenetic regulators in mature motor neurons, Nature Communications. DOI: https://doi.org/10.1038/s41467-026-78396-x
- Kim K\*, Lee CH#, Jung I# (2026) scCAPReSE: detection of large-scale genomic rearrangements from single-cell Hi-C based on few-shot learning, Genomics Infom. DOI: https://doi.org/10.1186/s44342-026-00069-4
- Oh Y, Kim H, Lee S, Park SJ, Park YG, Moon SH, Jung I, Lee CH (2026) Comparative analyses of ChIP-seq, CUT&RUN and CUT&Tag for Polycomb chromatin profiling, BMB Rep. DOI: https://doi.org/10.5483/bmbrep.2025-0247
- Lee J, Son S, Chung Y, Cho SD, Kwon JS, Bae S, Seok J, Choi B, Jung I, Oh JE, Shin EC, Kim SH, Park SH (2026) Robust effector memory features of human T-bethi B cells induced by repeated mRNA vaccination, iScience. DOI: https://doi.org/10.1016/j.isci.2026.114804
- Wei X\*, Xu Y\*, Yang D\*, Kim K, Yi L, Luo W, Lin X, Xiang Y, Williams A, Wang X, Srivas S, Tan C, Zhang K, Li W, Li Y, Yue F, Huang Z, Jung I#, Diao Y# (2026) Trimodal single-cell profiling of transcriptome, epigenome and 3D genome in complex tissues with scHiCAR, Nature Biotechnology. DOI: https://doi.org/10.1038/s41587-026-03013-7

**2025**

- Park G\*, Lee A\*, Jung I# (2025) GEM-Finder: dissecting GWAS variants via long-range interacting cis-regulatory elements with differentiation-specific genes, medRxiv. RECOMB2025 [사전 공개본] DOI: https://doi.org/10.1101/2025.03.02.25323165
- Anglen T\*, Kaplow I, Choi B, Dewars E, Perelli R, Hagy K, Tran D, Ramaker M, Shah S, Jung I, Landstrom A, Karra R, Diao Y, Gersbach C# (2025)  A gene regulatory element modulates myosin expression and controls cardiomyocyte response to stress, Genome Research. 온라인 2025-10-22. DOI: https://doi.org/10.1101/gr.280825.125[^myosin]
- Park S\*, Park H\*, Byun Y, Wei X, Eom J, Joo J, Lee A, Diao Y, Chung W#, Jung I# (2025) NR3C1-mediated epigenetic regulation suppresses astrocytic immune responses in mice, Nature Communications. DOI: https://doi.org/10.1038/s41467-025-64088-5
- Ahn H\*, Yu J\*,Ryu K\*, Ryu J,Kim S, Park J, Kim J, Jung I, An H, Hong S, Kim E, Park K, Ahn M, Min S, Jung I, Lee D, Lee T, Byun Y, Song J, Kim J, Cho W, Lee G#, Kim S# (2025) Single-molecule analysis reveals that IPMK enhances the DNA-binding activity of the transcription factor SRF, Nucleic Acids Research. DOI: https://doi.org/10.1093/nar/gkae1281

**2024**

- Chen S, Wang J\*, Jung I, Qui Z, Gao X#, Li Y# (2024) A fast and adaptive detection framework for genome-wide chromatin loop mapping from Hi-C data, Genome Research. DOI: https://doi.org/10.1101/gr.279274.124

**2023**

- Oh G, Choi B\*, Jung I#, Ye JC (2023) SCHYENA: FOUNDATION MODEL FOR FULL-LENGTH SINGLE-CELL RNA-SEQ ANALYSIS IN BRAIN, arXiv. [Preprint] [사전 공개본] DOI: https://doi.org/10.48550/arXiv.2310.02713
- Kim K\*, Kim M\*, Lee A\*, Song SH\*, Kang JK, Eom J, Kang GH, Bae JM, Min S, Kim Y, Lim Y, Kim HS, Kim YJ, Kim TY#, Jung I# (2023) Spatial and clonality-resolved 3D cancer genome alterations reveal enhancer-hijacking as a potential prognostic marker for colorectal cancer, Cell Reports. DOI: https://doi.org/10.1016/j.celrep.2023.112778
- Joo J\*, Cho S\*, Hong S, Min S, Kim K, Kumar R, Choi J, Shin Y#, Jung I# (2023) Probabilistic establishment of speckle-associated inter-chromosomal interactions, Nucleic Acids Research. DOI: https://doi.org/10.1093/nar/gkad211

**2022**

- Han S\*, Kim K\*, Park S, Lee A, Chun H, Jung I#  (2022) scAVENGERS: A genotype-based deconvolution of individuals in multiplexed single-cell ATAC-seq data without reference genotypes, NAR Genomics and Bioinformatics. DOI: https://doi.org/10.1093/nargab/lqac095

**2021**

- H Jo, T Kim, Y Chun, Jung I, D Lee# (2021) A compendium of chromatin contact maps reflecting regulation by chromatin remodelers in budding yeast, Nature Communications. DOI: https://doi.org/10.1038/s41467-021-26629-6
- S Han, H Lee, AJ Lee, SK Kim, Jung I, GY Koh, TK Kim, D Lee# (2021) CHD4 Conceals Aberrant CTCF-Binding Sites at TAD Interiors by Regulating Chromatin Accessibility in Mouse Embryonic Stem Cells, Molecules and Cells. DOI: https://doi.org/10.14348/molcells.2021.0224

## 수상과 선정

연구실 News의 수상·선정 글 14건이다. 2023–2025년 항목의 연도는 글에 적힌 행사 또는 수상 연도이고 정확한 날짜는 게시되어 있지 않다. 2022년 항목 가운데 두 건은 글에 적힌 날짜이고, 회원 선정은 교수 이력에 적힌 연도다.[^news]

- 2025 · 정인경 교수, BIOINFO 온빛상
- 2025 · 진세영, BIOINFO 우수포스터상
- 2025 · 이상현, CSH-Asia 우수포스터상
- 2024 · 정인경 교수, 의과학 분야 차세대 리더 선정
- 2024 · 주재건, BIOINFO 우수 포스터상
- 2024 · 진세영, K4DN Workshop 우수 포스터상
- 2024 · 정인경 교수, 제17회 아산의학상 젊은의학자부문
- 2023 · 이정운, BIOINFO 최우수논문상
- 2023 · 주재건·진세영, BIOINFO 우수 포스터상
- 2023 · 이정운·최백규, SSRC-K4DN Conference 우수 포스터상
- 2023 · 민선우, 생화학분자생물학회 운봉 젊은과학자상
- 2022 · 정인경 교수, 차세대과학기술한림원(Y-KAST) 회원 선정
- 2022-10-21 · 양동찬·김무영·김규광, BIOINFO 최우수포스터상; 박성완, BIOINFO 우수포스터상
- 2022-10-20 · 양동찬, BIOINFO Standigm 우수논문상

## 연락과 위치

- 교수 이메일: ijung@kaist.ac.kr[^professor][^contacts]
- 교수 전화: 042-350-7314[^professor]
- 연구실 전화: 042-350-7354, 팩스 042-350-2610[^contacts]
- 교수실: KAIST 자연과학동 E6-3, 5210호[^contacts]
- 연구실: KAIST 자연과학동 E6-3, 5213–5214호[^contacts]
- 주소: 대전광역시 유성구 대학로 291, KAIST, 34141[^contacts]

## 각주
[^main]: 연구실 Main, Research topics. <https://sites.google.com/view/junglab-kaist/main> (확인 2026-11-13).
[^structure]: 연구실 3D genome organization. <https://sites.google.com/view/junglab-kaist/research/3d-genome-organization> (확인 2026-11-13).
[^learning]: 연구실 Deep-learning in omics. <https://sites.google.com/view/junglab-kaist/research/deep-learning-in-omics> (확인 2026-11-13).
[^professor]: 연구실 Professor. <https://sites.google.com/view/junglab-kaist/current-members/professor> (확인 2026-11-13).
[^dept]: KAIST 생명과학과 정인경 교수 소개. <https://bio.kaist.ac.kr/doc/ko/selectDoc.do?docSeq=9752&menuSeq=3344&bbsSeq=120> (확인 2026-11-13).
[^news]: 연구실 News. <https://sites.google.com/view/junglab-kaist/news> (확인 2026-11-13).
[^members]: 연구실 Current Members. <https://sites.google.com/view/junglab-kaist/current-members> (확인 2026-11-13).
[^alumni]: 연구실 Alumni. <https://sites.google.com/view/junglab-kaist/current-members/alumni> (확인 2026-11-13).
[^publications]: 연구실 Publications. <https://sites.google.com/view/junglab-kaist/publications> (확인 2026-11-13).
[^contacts]: 연구실 Contacts. <https://sites.google.com/view/junglab-kaist/contacts> (확인 2026-11-14).
[^p1]: K. N. Montanera 외, H. S. Rhee, Nature Communications (2026). <https://doi.org/10.1038/s41467-026-78396-x> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5080272556,publication_year:2021-2026> (확인 2026-11-13).
[^p2]: S. Park 외, I. Jung, Nature Communications (2025). <https://doi.org/10.1038/s41467-025-64088-5> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5080272556,publication_year:2021-2026> (확인 2026-11-13).
[^p3]: X. Wei 외, Y. Diao, Nature biotechnology (2026). <https://doi.org/10.1038/s41587-026-03013-7> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1038/s41587-026-03013-7%22> (확인 2026-11-14).
[^p4]: J. Joo 외, I. Jung, Nucleic Acids Research (2023). <https://doi.org/10.1093/nar/gkad211> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5080272556,publication_year:2021-2026> (확인 2026-11-13).
[^p5]: K. Kim, C.-H. Lee, I. Jung, Genomics & Informatics (2026). <https://doi.org/10.1186/s44342-026-00069-4> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=scCAPReSE%3A%20detection%20of%20large-scale%20genomic%20rearrangements%20from%20single-cell%20Hi-C%20based%20on%20few-shot%20learning> (확인 2026-11-14).
[^p6]: G. Park, A. J. Lee, I. Jung, medRxiv 사전 공개본 (2025). <https://doi.org/10.1101/2025.03.02.25323165> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1101/2025.03.02.25323165> (확인 2026-11-14).
[^p7]: Y. Oh 외, C.-H. Lee, BMB Reports 59, 242–252 (2026). <https://doi.org/10.5483/bmbrep.2025-0247> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/advs.77736|10.1016/j.heliyon.2023.e14039|10.1016/j.isci.2026.114804|10.1016/j.molcel.2026.06.021|10.1038/s41587-026-03013-7|10.1038/s41590-023-01547-5|10.1101/2025.03.02.25323165|10.1101/2025.07.19.665672|10.1186/s44342-026-00069-4|10.5483/bmbrep.2025-0247|10.64898/2026.01.05.697725> (확인 2026-11-14).
[^p8]: H. Jo 외, D. Lee, Nature Communications (2021). <https://doi.org/10.1038/s41467-021-26629-6> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5080272556,publication_year:2021-2026> (확인 2026-11-13).
[^myosin]: T. Anglen 외, Genome Research (온라인 2025-10-22). <https://doi.org/10.1101/gr.280825.125> 초록 기준(Crossref 등록 사전 공개본 초록, DOI 10.1101/2025.07.19.665672). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=A%20gene%20regulatory%20element%20modulates%20myosin%20expression%20and%20controls%20cardiomyocyte%20response%20to%20stress>. 학술지판 서지 <https://api.crossref.org/works?query.bibliographic=A+gene+regulatory+element+modulates+myosin+expression+and+controls+cardiomyocyte+response+to+stress&filter=type:journal-article&rows=5&select=DOI,title,container-title,published-online,published-print,issued> (확인 2026-11-14).

# 오믹스 연구실 (OMICS Laboratory for Computational Biology and Medicine)

**KAIST 바이오및뇌공학과 · 최정균 교수**

- 분야: 오믹스 자료 기반 계산생물학과 의학(시스템 유전학·후성유전체학, 기계학습, 차세대 염기서열 분석), 종양 신생항원의 면역원성 예측, 혈중 DNA·전사체로 암 진단과 치료 반응 예측, 단일세포 지도와 체외 종양 모형으로 치료 표적 찾기
- 대분야: 기초생명·생물물리, 컴퓨팅·AI
- 태그: 과학·공학 AI[^p2][^p6][^p7], 장기 칩·체외 질병 모델[^p8]
- 홈페이지: <https://omics.kaist.ac.kr/>
- 근거와 출처: [오믹스 연구실 근거 페이지](omics-sources.md)

> 유전체·후성유전체·전사체처럼 유전체 전체 규모로 얻는 대규모 생물 자료(오믹스)를 계산과 기계학습으로 분석하는 바이오및뇌공학과 연구실이다. 연구 페이지는 연구 주제를 「Omics-based Computational Biology and Medicine」(오믹스 기반 계산생물학과 의학)으로 적고, 2021년 이후 대표 논문은 암세포 돌연변이 조각의 면역 반응 예측, 혈중 DNA로 암을 찾는 알고리즘, 단일세포 지도로 세포 치료 표적을 고르는 방법을 내놓았다.[^research][^p1][^p4][^p7]

## 무엇을 연구하나

연구 페이지는 연구 주제를 「Omics-based Computational Biology and Medicine」으로 적고, 연구 키워드로 시스템 유전학(Systems genetics), 시스템 후성유전학(Systems epigenetics, 유전자 조절 표지와 분자·세포의 연결망이 함께 생물의 기능에 관여하는 방식을 연구하는 분야), 기계학습(Machine learning), 차세대 염기서열 분석(Next-generation sequencing), 암 유전체학(Cancer genomics), 면역치료(Immunotherapy), 신경유전체학(Neurogenomics), 유전체 진화(Genome evolution), 후성유전체학(Epigenomics)을 든다.[^research] 바이오및뇌공학과 교수진 목록은 교수의 연구분야를 오믹스, 유전체/후성유전체학, 시스템유전학으로 적는다.[^deptlist]

연구 페이지는 학술지 Science의 글을 인용해, 시스템 유전학의 원리를 유전 정보가 분자·세포·생리 수준의 네트워크를 거쳐 통합되고 조율되고 전달되어 생물 시스템의 고차 기능과 창발적 성질을 만드는 방식을 이해하는 것으로 소개한다.[^research] 이어 Omics Gateway의 설명을 인용해, 유전체학 이후 유전체 전체 규모로 하는 연구 분야 이름에 「-omics」를 붙이게 되었고, 오믹스는 여러 「-ome」에 걸친 생물 정보 대상들의 상호작용을 분석하는 과학·공학 분야를 두루 이르는 말이라고 적는다. 인용한 설명은 그 중심을 유전자·단백질·리간드 같은 정보 대상의 지도 작성, 대상 사이 상호작용 관계 찾기, 조절 기전을 이해하고 조작하려는 네트워크와 대상의 공학, 여러 오믹스 분야의 통합으로 든다.[^research]

누리집 Resources 페이지는 논문과 함께 공개한 도구와 자료를 모아 둔다. CAR-T 세포 치료의 표적을 찾기 위한 암세포 지도 웹 브라우저(Nature Biotechnology 2023 논문), 면역원성 신생항원을 예측하는 웹 서비스 DeepNeo(Nature Genetics 2023, Nature Communications 2020 논문), 인트론 안쪽 가까운 자리의 스플라이싱 이상 돌연변이를 예측하는 코드(Oncogene 논문), 임상 시료에서 암에 특이한 취약점을 계산으로 추정하는 코드(in silico CRISPR/RNA 간섭(RNA interference, RNAi: 특정 RNA를 표적으로 유전자 발현을 억제하는 과정)과 의존성 예측, Genome Biology 2020 논문), 복잡한 조절 특징을 공유하는 인과 위험 요인을 예측하는 합성곱 신경망 모델 cnnGWAS의 코드(Nucleic Acids Research 2019 논문)가 있다.[^resources]

## 주요 연구 주제

### 1. 종양 신생항원의 면역원성 예측

암세포의 돌연변이로 새로 생긴 단백질 조각(신생항원) 가운데 실제로 면역세포의 반응을 일으키는 조각을 계산으로 가려낸다. 대표 논문 1은 36,000건이 넘는 면역원성 시험 결과로, 펩타이드와 MHC 분자의 구조적 배열이 T세포 반응을 돕는 쌍을 찾는 방법을 개발해, MHC II와 MHC I의 신생항원을 예측했다.[^p1] 대표 논문 2는 펩타이드-MHC 쌍의 구조적 성질을 잡아내는 딥러닝 모델 DeepNeo를 최신 학습 자료로 고친 DeepNeo-v2를 웹서버로 공개했다.[^p2] 대표 논문 3은 B세포 반응을 예측하기 어려웠던 문제를 다뤄, 항체 결합 시험을 거친 펩타이드와 B세포 수용체 클론 자료로 B세포 항원결정부위를 찾는 방법을 개발했다.[^p3]

### 2. 혈중 DNA·전사체로 암 진단과 치료 반응 예측

혈액에 떠다니는 DNA 조각(세포유리 DNA)과 종양의 전사체 자료로 암을 찾고 치료에 대한 반응을 예측하는 방법을 만든다. 대표 논문 4는 종양 조직의 돌연변이 분포와 염색질 구성 정보를 참조로 삼는 알고리즘으로, 세포유리 DNA 전장 유전체 자료에서 암 여부와 암이 생긴 조직을 찾았다.[^p4] 대표 논문 5는 젊은 LINE-1 서열을 깊게 읽어 세포유리 DNA에서 유전체 저메틸화 상태를 추정하는 측정법 iMethyl을 개발해 면역관문억제제 치료 반응 예측에 썼다.[^p5] 대표 논문 6은 DNA 수선 유전자의 비기능성 이소형이 쓰이는 양상으로 상동 재조합 결손을 판별하는 기계학습 검출법을 내놓아, PARP 억제제 반응 예측에 썼다.[^p6]

### 3. 단일세포 지도와 체외 모형으로 찾는 치료 표적

세포 하나하나의 유전자 발현을 모은 지도와 환자 유래 조직으로 키운 체외 모형으로 치료 표적과 암 전이 과정을 살핀다. 대표 논문 7은 종양 412개와 정상 장기 12개의 세포 약 140만 개를 통합한 단일세포 발현 지도를 만들고, 랜덤 포레스트와 합성곱 신경망을 쓴 두 단계 선별로 암세포와 정상 세포를 가르는 데 가장 크게 기여하는 유전자 쌍을 골라 CAR 세포 치료의 AND·OR·NOT 논리 게이트 표적을 찾았다.[^p7] 대표 논문 8은 환자 대장암 오가노이드를 환자 유래 세포외기질에서 키워 종양의 전이 초기 과정을 재현하는 체외 모형을 제시하고, 단일세포 다중 오믹스 분석으로 그 과정을 재구성했다.[^p8]

논문 목록에는 T세포·B세포 수용체 서열의 추출, 자료 처리, 클론형 판별 방법과 계산 도구를 정리한 고찰(2025년)과, L1 레트로트랜스포존이 RNA의 m6A 메틸화를 이용해 복제하고 진화해 왔다는 기초 연구(2021년, 교수는 20명 중 열넷째 저자)도 있다.[^tcrbcr][^l1]

## 대표 논문

최정균 교수가 KAIST에 있는 2021–2026년의 학술지 논문 가운데 교수가 마지막 저자이고 초록을 확인할 수 있는 논문을, 위의 세 연구 갈래에 고르게 여덟 편 골랐다. 저자 순서는 학술지 서지 기록(Crossref)을 따랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2023 | [MHC II immunogenicity shapes the neoepitope landscape in human tumors](https://doi.org/10.1038/s41588-022-01273-y) · Nature Genetics | 돌연변이 펩타이드가 MHC I(세포 표면에서 단백질 조각을 면역세포에 내보이는 분자의 한 종류)에 물리적으로 붙는지는 예측이 발전했지만, 실제로 면역 반응을 일으키는 신생항원결정부위를 가려내기는 여전히 어렵고 특히 MHC II에서 그렇다. 이 논문은 36,000건이 넘는 면역원성 시험 결과를 써서, 펩타이드와 MHC의 구조적 배열이 T세포 반응을 돕는 쌍을 찾는 방법을 개발했다. 여러 종류의 종양 시료 1,200개가 넘는 자료에 적용하자, 면역관문억제제 치료에 반응한 MHC II·MHC I 신생항원결정부위를 예측했다. 치료받지 않은 종양 9,000개가 넘는 자료에서 돌연변이 2,500만 개가 넘는 빈도 분포를 면역 표현형 100가지가 넘는 지표와 함께 분석하자, MHC II 면역원성은 면역 압력이 높은 종양, 특히 T세포 수용체 클론 집중도와 MHC II 발현이 높은 종양에서 그 변이의 빈도를 특이하게 낮췄다. MHC I 신생항원결정부위도 비슷한 경향을 보였지만 일부 조직 종류에서만 그랬다. 연구진은 MHC II에 묶인 자연적·치료적 T세포 반응이 종양에 면역 선택을 가한다고 보고한다.[^p1] | 1저자 J. Y. Kim(Jeong Yeon Kim), 마지막 저자 최정균 (15명) |
| 2 | 2023 | [DeepNeo: a webserver for predicting immunogenic neoantigens](https://doi.org/10.1093/nar/gkad275) · Nucleic Acids Research | 외부 물질이나 체세포 돌연변이에서 생긴 자기 아닌 항원결정부위는 MHC 분자에 실려 T세포에 인식되면 면역 반응을 일으키므로, 면역 반응을 실제로 일으키는 신생항원결정부위를 찾는 일은 암과 바이러스 의학에서 중요하다. 그러나 지금의 방법은 대부분 돌연변이 펩타이드와 MHC의 물리적 결합 예측에 머문다. 연구진은 앞서 T세포 반응성이 있는 펩타이드-MHC 쌍의 구조적 성질을 잡아내 면역원성 신생항원결정부위를 찾는 딥러닝 모델 DeepNeo를 개발했고, 이 논문에서 최신 학습 자료로 모델을 고쳤다. 고친 모델(DeepNeo-v2)은 평가 지표가 나아졌고, 예측 점수의 분포가 알려진 신생항원의 성질에 더 잘 맞았다. 예측은 https://deepneo.net 에서 할 수 있다.[^p2] | 1저자 J. Y. Kim(Jeong Yeon Kim), 마지막 저자 최정균 (4명) |
| 3 | 2025 | [B cell-reactive neoantigens boost anti-tumor immunity](https://doi.org/10.1126/sciadv.adx8303) · Science Advances | 신생항원이 이끄는 항암 면역에서 B세포가 하는 역할은 B세포 반응을 예측하기 어려워 거의 연구되지 않았다. 이 논문은 IgG 항체 결합을 시험한 펩타이드(437,000개 넘게)와 B세포 수용체 클론(3억 7천만 개 넘게)을 분석해 B세포 항원결정부위를 찾는 방법을 개발했다. 코로나19(SARS-CoV-2) 백신 접종 전후의 단일세포 B세포 수용체 서열 분석으로 방법의 성능을 검증했고, 생쥐 백신 실험에서 B세포 신생항원결정부위가 면역 반응을 높여 B세포 수용체 클론의 증식과 종양 축소를 이끌었다. 암 유전체 아틀라스(TCGA) 시료 8,000개 넘게를 분석하자 예측된 B세포 반응성과 돌연변이 대립유전자 빈도가 반비례해, B세포를 통한 신생항원 제거를 가리켰다. 다중 오믹스 모델을 환자 2,074명의 면역관문억제제 반응에 적용해 B세포 신생항원결정부위 예측의 임상적 의미를 보였고, 신생항원 1,739개를 다룬 맞춤형 백신 시험 11건의 메타분석은 B세포 신생항원결정부위를 넣으면 백신 효과가 나아질 수 있음을 시사했다.[^p3] | 1저자 J. Y. Kim(Jeong Yeon Kim), 마지막 저자 최정균 (14명) |
| 4 | 2023 | [Integrative modeling of tumor genomes and epigenomes for enhanced cancer diagnosis by cell-free DNA](https://doi.org/10.1038/s41467-023-37768-3) · Nature Communications | 혈액 속 세포유리 DNA로 여러 암을 일찍 찾는 액체 생검은 아직 큰 과제다. 이 논문은 세포유리 DNA 전장 유전체 염기서열 분석으로 9개 암종 환자 시료 2,125개와 정상 대조 시료 1,241개를 담은 시험 자료 두 벌과, 건강한 사람의 얕은 깊이 시료 20,529개로 만든 배경 변이 거르기용 참조 자료를 만들었다. 외부 자료(암 208개, 정상 대조 214개)로 추가 평가도 했다. 종양 조직의 암종별 돌연변이 분포와 염색질 구성 정보를 모델의 참조로 넣은 알고리즘으로 암 검출과 암이 생긴 조직 찾기의 정확도를 얻었다. 이 통합 모델은 췌장암을 포함한 초기 암을 말기 암 검출에 견줄 만한 높은 민감도로 찾았고, 모델 해석은 암종별 유전체·후성유전체 특징의 기여를 드러냈다. 연구진은 이 방법이 특히 초기 단계의 정확한 세포유리 DNA 기반 암 진단의 바탕이 될 수 있다고 적는다.[^p4] | 1저자 M. Bae(Mingyun Bae), 마지막 저자 최정균 (28명) |
| 5 | 2023 | [Genomic hypomethylation in cell-free DNA predicts responses to checkpoint blockade in lung and breast cancer](https://doi.org/10.1038/s41598-023-49639-4) · Scientific Reports | 유전체 저메틸화는 면역관문억제제 치료 반응을 가르는 요인으로 최근 밝혀졌지만, 이를 세포유리 DNA에 쓸 수 있는지, 조직 메틸화 분석에서 생기는 낮은 종양 순도 문제를 풀 수 있는지는 분명하지 않았다. 이 논문은 젊은 LINE-1 서열을 시료당 40만 개가 넘는 서열 조각으로 깊게 읽는 표적 염기서열 분석으로 세포유리 DNA의 유전체 저메틸화 상태를 추정하는 측정법 iMethyl을 개발했다. 폐암·유방암·난소암의 면역관문억제제 치료 시료 모두 653개에 적용했다. 혈액 시료용 iMethyl-liquid는 조직 시료의 종양 순도와 관계없이 치료 반응을 정확히 예측했고, 치료 시작 3주나 6주 뒤의 이른 시기에 치료 반응을 살피고 종양이 진행하면서 저메틸화가 심해지는 것도 잡아냈다. 조직 시료용 iMethyl-tissue는 종양 돌연변이 부담과 PD-L1 발현보다 예측력이 좋았다. 연구진은 iMethyl-liquid가 면역관문억제제 치료 반응을 몸에 상처를 내지 않고 믿을 만하게 예측하고, 일찍 평가하고, 추적할 수 있게 한다고 결론짓는다.[^p5] | 1저자 K. Kim(Kyeonghui Kim), 마지막 저자 최정균 (13명) |
| 6 | 2021 | [Aberrant transcript usage is associated with homologous recombination deficiency and predicts therapeutic response](https://doi.org/10.1158/0008-5472.can-21-2023) · Cancer Research | 상동 재조합 결손 가운데 BRCA1/2 돌연변이로 설명되는 경우는 일부뿐이고, 최근 나온 유전체 기반 결손 검사는 교란 요인 때문에 PARP 억제제와 DNA 손상 약물에 반응할 시료를 정밀하게 예측하지 못한다. 이 논문은 부 이소형의 비정상적 전사체 사용에 바탕을 둔 「전사 수준의 상동 재조합 결손」의 분자·임상 근거를 제시했다. 유전체 기반 결손이 있는 유방암·난소암에서는 DNA 수선 유전자의 비기능성 이소형 사용이 늘어 있었고, 기능 시험으로 이것이 상동 재조합 기능 저하와 이어짐을 확인했다. 핵심 유전자의 전사체 사용 양상으로 결손을 판별하는 기계학습 검출법은 유전체 기반 결손이나 BRCA1/2 돌연변이를 직접 찾는 방법보다 세포주와 암 환자의 PARP 억제제·유전독성 약물 반응을 정확하게 예측했고, 백금 내성이 생긴 뒤 올라파립으로 치료받은 난소암 환자 집단에서도 실제 상동 재조합 상태를 반영했다. 연구진은 이 결손 판별에 바탕을 둔 진단 검사가 PARP 억제제의 임상 쓰임을 넓힐 것으로 본다.[^p6] | 1저자 H. G. Kang(Hyeon Gu Kang), 마지막 저자 최정균 (12명) |
| 7 | 2023 | [Single-cell mapping of combinatorial target antigens for CAR switches using logic gates](https://doi.org/10.1038/s41587-023-01686-y) · Nature Biotechnology | 종양 안의 세포가 제각각인 암에서 키메라 항원 수용체(CAR) 세포 치료를 하려면 암세포를 주변 정상 조직 세포와 가르는 표적 항원을 찾는 일이 핵심 과제다. 이 논문은 종양 412개와 정상 장기 12개에서 얻은 종양 세포, 종양에 스며든 정상 세포, 기준 정상 세포 약 140만 개를 통합한 단일세포 발현 지도를 만들어 조직의 복잡성을 세포 하나 단위로 나눠 보았다. 랜덤 포레스트와 합성곱 신경망을 쓴 두 단계 선별 방법으로 개별 암세포와 정상 세포를 가르는 데 가장 크게 기여하는 유전자 쌍을 골랐고, 짝지은 유전자가 단일세포마다 함께 발현하는 양상을 바탕으로 AND·OR·NOT 논리 게이트별 종양 포괄 범위와 특이도를 평가했다. 단일세포 전사체와 세포 표면 단백질을 함께 재는 분석으로 난소암과 대장암에서 찾은 AND·OR·NOT 스위치 표적을 검증했다.[^p7] | 1저자 J. Kwon(Joonha Kwon), 마지막 저자 최정균 (16명) |
| 8 | 2025 | [Single-cell multiomic modelling of early metastatic events promoted by the extracellular matrix](https://doi.org/10.1038/s41416-025-03181-4) · British Journal of Cancer | 암 전이는 주로 상피-중간엽 전이(EMT)로 일어나고 암 사망 대부분의 원인인데, 기존 전임상 모형은 사람의 기질 조직이 빠져 중간엽 성질을 제대로 담지 못하고, 기존 체외 모형은 정해진 세포외기질 성분에 기대 사람 몸의 환경을 충분히 재현하지 못한다. 이 논문은 환자 유래 대장암 오가노이드의 배양 기질을 기저막 추출물에서 환자 유래 세포외기질로 바꿔 암세포가 실제 조직에서 퍼져 나가는 모습을 흉내 냈고, 전사체와 후성유전체를 함께 보는 단일세포 다중 오믹스 분석으로 오가노이드의 변화와 EMT 경로를 재구성했다. 이 기질에서 키운 오가노이드는 외부 신호 물질을 넣지 않아도 종양 세포의 퍼짐과 움직임이 늘어 실제 병변과 닮았다. 분석은 TNF-α 신호를 EMT 경로의 초기 전이 사건으로 드러냈고, 후성유전체 변화로 AP-1 복합체 표적 유전자, 특히 MMP7의 염색질 접근성이 높아졌고, MMP7은 침윤성 표현형을 이끌었다. 여러 자료를 함께 쓴 계산 방법은 초기와 후기 EMT 상태를 구별했고, 이 기질이 일으킨 EMT가 전통적인 EMT 주 조절 인자와 무관하게 일어나며 상피와 중간엽 성질이 섞인 부분 EMT 상태임을 보였다. 연구진은 이 체외 모형이 실제 조직의 종양 형성을 가깝게 재현하고 표적 치료 개발에 쓸 수 있는 플랫폼이라고 적는다.[^p8] | 1저자 H. J. Lee(Hyun Jin Lee), 마지막 저자 최정균 (14명) |

## 교수와 전문 분야

최정균 교수는 KAIST 바이오및뇌공학과 교수다. 학과 교수진 목록은 직위를 교수로 적고, 학과 교수 소개는 직위를 부교수로, 경력을 「2014.09 ~ Present Associate Professor」로 적는다.[^deptlist][^deptprof] KAIST에서 생명과학으로 박사 학위(2004년)를 받았다.[^deptlist][^deptprof]

학과 교수 소개가 적는 경력은 Korea Research Institute of Bioscience and Biotechnology(한국생명공학연구원) 연구원(Research Scientist, 2004년 9월–2007년 2월), 연세대학교 Yonsei Genome Institute 연구교수(Research Professor / Instructor, 2007년 3월–2009년 9월), KAIST 바이오및뇌공학과 조교수(2009년 10월–2014년 8월)와 부교수(2014년 9월–), 싱가포르 Genome Institute of Singapore 책임연구자 겸직(Principal Investigator, Joint appointment, 2010년 1월–2012년 12월)이다.[^deptprof]

학과 교수 소개의 수상 경력은 제10회 아산의학상 젊은 의학자부문 수상(2017년), 한국차세대과학기술한림원 Y-KAST 창립회원 선정(2017년), KAIST 46주년 개교기념 학술상(2016년), 한국분자세포생물학회 Blue Ribbon Lecture Award(2015년), 한국과학기술한림원 한림선도과학자 선정(2013년), 한국생명정보학회 OnBIT 학술상(2011년), 포스코청암재단 펠로우십 신진교수 부문 선정(2009년), 한국분자세포생물학회 차세대 바이오니어 연구자상 대상(2009년)이다.[^deptprof]

전문 분야는 오믹스, 유전체·후성유전체학, 시스템 유전학이다.[^deptlist] 학과 교수 소개가 드는 대표 연구실적은 후성유전 조절과 유전자 발현의 변이성(Nature Genetics, 2008년), 뉴클레오솜 위치 서열에 새겨진 유전자 발현 변이성(Nature Genetics, 2009년), 암의 반복 비암호화 돌연변이를 염색질 구조로 예측한 연구(Nature Genetics, 2016년) 등 다섯 편이다.[^deptprof] 2021년 이후에는 위의 대표 논문처럼 계산·기계학습 방법으로 신생항원 면역원성, 세포유리 DNA 기반 암 진단, 치료 반응을 예측하는 연구를 내놓아 왔다.[^p1][^p2][^p4][^p6]

## 응용 분야

대표 논문들은 면역관문억제제 치료 반응 예측(대표 논문 1·3·5), 맞춤형 신생항원 백신(대표 논문 3), 혈액으로 여러 암을 일찍 찾는 액체 생검(대표 논문 4), PARP 억제제의 동반 진단(대표 논문 6), CAR 세포 치료의 표적 선정(대표 논문 7), 표적 치료 개발을 위한 체외 종양 모형(대표 논문 8)을 응용으로 든다.[^p1][^p3][^p4][^p5][^p6][^p7][^p8] Resources 페이지는 CAR-T 세포 치료 표적 찾기용 암세포 지도를 웹 브라우저로, DeepNeo를 웹 서비스로 연결해 둔다.[^resources]

## 구성원

Members 페이지 Current 구역의 교수를 뺀 13명이다. 박사후연구원(Postdoctoral Researcher) 4명, 박사과정(PhD Candidate) 4명, 석사과정(MS Candidate) 4명, Research Assistant 1명이며, 카드는 이름과 과정만 적는다. 이름 뒤의 MD·PhD는 페이지 표기 그대로다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Junho Kang, MD, PhD | 박사후연구원 | 7, 8 |
| Jinhyeon An, PhD | 박사후연구원 | 1, 3 |
| Hyunjin Lee, PhD | 박사후연구원 | 8 |
| Gyuhee Kim, PhD | 박사후연구원 | 4 |
| Hyunwook Park | 박사과정 | 4 |
| Soyeon Kim | 박사과정 | 3 |
| Jiye Yoo | 박사과정 |  |
| Sungyi Yoon | 박사과정 |  |
| Hyunwoo Lim | 석사과정 |  |
| Minju Kim | 석사과정 | 3 |
| Kyungmin Min | 석사과정 |  |
| Yeonji Hwang | 석사과정 |  |
| Hyo Jung Yoon | Research Assistant |  |

## 졸업생과 이전 구성원

Members 페이지 Alumni 구역의 30명 전부다(2015년 8월–2026년 2월). 학위·과정 칸은 페이지가 이름 뒤 대괄호에 적은 표기이고, 괄호의 날짜는 페이지가 「~ Aug 2015」처럼 적은 달·연도다. 진로 칸은 이름 뒤 괄호의 기관을 적힌 차례대로 옮겼고, 기관이 여럿이면 쌍반점으로 이었다. 기관 괄호가 없는 줄은 진로 칸을 비웠다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Kwoneel Kim | PhD (Aug 2015) | Asan Medical Center; Kyung Hee University |
| Kibaick Lee | PhD (Feb 2017) | National Institute of Health; ichrogene, Inc.; Hancom Carelink; Jeju Techno Park |
| Woojin Yang | PhD (Aug 2017) | Korean Bioinformation Center; Seegene, Inc. |
| Hyo-Jeong Ban, PhD | Postdoc (Sep 2017) | Korea Institute of Oriental Medicine |
| Min Kyung Sung | PhD (Feb 2018) | MRC Laboratory of Molecular Biology; Cell Mogrify, Ltd. |
| Hyunchul Jung | PhD (Aug 2018) | Wellcome Trust Sanger Institute |
| Kang Seon Lee | PhD (Aug 2018) | Bioorchestra Co., Ltd.; Kyung Hee Medical Center |
| Jihyun An, MD, PhD | Senior Researcher (Feb 2019) | Hanyang University Hospital |
| Seulkee Lee, MD | PhD (Feb 2019) | Samsung Medical Center |
| Kiwon Jang | MS, PhD (Feb 2019) | Korean Bioinformation Center |
| Haeun Hwangbo | Research Scientist (June 2019) | UNC-Chapel Hill; Bristol Myers Squibb |
| Taeyeop Lee, MD | PhD (Feb 2020) | Asan Medical Center |
| Junghoon Shin, MD | PhD (Feb 2022) | Seoul National University Hospital; Samsung Medical Center |
| Chang Hwan Sung, MD | PhD (Feb 2022) | Asan Medical Center |
| Dohyeon An | MS (Feb 2022) | 3billion, Inc.; 4Grit |
| Hyoeun Bang | MS, PhD (Aug 2022) | PentaMedix Co., Ltd.; The University of Suwon |
| Joonha Kwon | PhD (Aug 2022) | National Cancer Center |
| Hyeon Gu Kang | MS, PhD (Aug 2022) | Jackson Laboratory |
| Min Gyun Bae | MS, PhD (Aug 2023) | Boston Children's Hospital / Harvard Medical School |
| Jeong Yeon Kim | MS, PhD (Aug 2023) | Korea Virus Research Institute |
| Jaeho Oh | PhD (Feb 2024) | Aimed Bio, Inc. |
| Dakyum Shin, MD | Research Associate (Feb 2024) | Chosun University Hospital |
| Jun Hyeong Lee | MS, PhD (Feb 2024) | Samsung Bioepis |
| Jae Soon Park | MS, PhD (Feb 2024) |  |
| Seungmin Park | MS (Aug 2025) |  |
| Kyeonghui Kim | MS, PhD (Aug 2025) |  |
| Jinok Yang | PhD (Feb 2026) |  |
| Kayoung Seo | PhD (Feb 2026) |  |
| Elizaveta Ignatova | PhD (Feb 2026) |  |
| Sujie Lee | MS (Feb 2026) |  |

## 최근 논문 목록 (2021–2026)

2021–2026년 논문 10편이다(2025년 3, 2023년 5, 2021년 2). Publications 페이지가 보여 주는 연구실 논문 목록의 2021–2026년 28편 가운데, 의생명 연구는 자연·공학과 직접 연계된 연구만 싣는 이 위키의 수록 범위에 따라 논문마다 초록으로 확인해 18편은 싣지 않았다(사유는 근거 페이지).[^pubs] 제목·학술지·연도는 누리집 목록 그대로이고, 누리집 목록에 저자가 없어 저자는 학술지 서지 기록(Crossref)을 따랐다.[^cr]

- 누리집 목록의 * 표시는 목록 머리가 밝힌 대로 연구실 구성원이 주 저자를 함께 맡은 논문(Primary authorship shared by lab members)이라는 뜻이며, 학술지 뒤에 「누리집 표시 *」로 옮겼다.[^pubs]

**2025**

- Jeong Yeon Kim, Jinhyeon An, Soyeon Kim, Hye-Yeong Jo, Eun Ji Lee, Minju Kim, Hongui Cha, Se-Hoon Lee, Hyun-Young Park, Sang Cheol Kim, Dae-Yeon Cho, Inkyung Shin, Suhwan Chang, Jung Kyoon Choi. "B cell-reactive neoantigens boost anti-tumor immunity". *Science Advances, 2025 (누리집 표시 \*)*.
- Hyun Jin Lee, Jun Hyeong Lee, Junho Kang, Kyeonghui Kim, Youngwon Cho, Jihyun Park, Sang-Hyun Song, Joonha Kwon, Young-Joon Kim, Woong-Yang Park, Tae-You Kim, Jong-Eun Park, Pilnam Kim, Jung Kyoon Choi. "Single-cell multiomic modelling of early metastatic events promoted by the extracellular matrix". *British Journal of Cancer, 2025 (누리집 표시 \*)*.
- Kayoung Seo, Jung Kyoon Choi. "Comprehensive analysis of TCR and BCR repertoires: Insights into methodologies, challenges, and applications". *Genomics & Informatics, 2025 (누리집 표시 \*)*.

**2023**

- Kyeonghui Kim, Hyemin Kim, Inkyung Shin, Seung-Jae Noh, Jeong Yeon Kim, Koung Jin Suh, Yoo-Na Kim, Jung-Yun Lee, Dae-Yeon Cho, Se Hyun Kim, Jee Hyun Kim, Se-Hoon Lee, Jung Kyoon Choi. "Genomic hypomethylation in cell-free DNA predicts responses to checkpoint blockade in lung and breast cancer". *Scientific Reports, 2023 (누리집 표시 \*)*.
- Jeong Yeon Kim, Hyoeun Bang, Seung-Jae Noh, Jung Kyoon Choi. "DeepNeo: a webserver for predicting immunogenic neoantigens". *Nucleic Acids Research, 2023 (누리집 표시 \*)*.
- Mingyun Bae, Gyuhee Kim, Tae-Rim Lee, Jin Mo Ahn, Hyunwook Park, Sook Ryun Park, Ki Byung Song, Eunsung Jun, Dongryul Oh, Jeong-Won Lee, Young Sik Park, Ki-Won Song, Jeong-Sik Byeon, Bo Hyun Kim, Joo Hyuk Sohn, Min Hwan Kim, Gun Min Kim, Eui Kyu Chie, Hyun-Cheol Kang, Sun-Young Kong, Sang Myung Woo, Jeong Eon Lee, Jai Min Ryu, Junnam Lee, Dasom Kim, Chang-Seok Ki, Eun-Hae Cho, Jung Kyoon Choi. "Integrative modeling of tumor genomes and epigenomes for enhanced cancer diagnosis by cell-free DNA". *Nature Communications, 2023 (누리집 표시 \*)*.
- Joonha Kwon, Junho Kang, Areum Jo, Kayoung Seo, Dohyeon An, Mert Yakup Baykan, Jun Hyeong Lee, Nayoung Kim, Hye Hyeon Eum, Sohyun Hwang, Ji Min Lee, Woong-Yang Park, Hee Jung An, Hae-Ock Lee, Jong-Eun Park, Jung Kyoon Choi. "Single-cell mapping of combinatorial target antigens for CAR switches using logic gates". *Nature Biotechnology, 2023 (누리집 표시 \*)*.
- Jeong Yeon Kim, Hongui Cha, Kyeonghui Kim, Changhwan Sung, Jinhyeon An, Hyoeun Bang, Hyungjoo Kim, Jin Ok Yang, Suhwan Chang, Incheol Shin, Seung-Jae Noh, Inkyung Shin, Dae-Yeon Cho, Se-Hoon Lee, Jung Kyoon Choi. "MHC II immunogenicity shapes the neoepitope landscape in human tumors". *Nature Genetics, 2023 (누리집 표시 \*)*.

**2021**

- Hyeon Gu Kang, Haeun Hwangbo, Myung Ji Kim, Sinae Kim, Eun Ji Lee, Min Ji Park, Jae-Weon Kim, Byoung-Gie Kim, Eun-Hae Cho, Suhwan Chang, Jung-Yun Lee, Jung Kyoon Choi. "Aberrant transcript usage is associated with homologous recombination deficiency and predicts therapeutic response". *Cancer Research, 2021 (누리집 표시 \*)*.
- Sung-Yeon Hwang, Hyunchul Jung, Seyoung Mun, Sungwon Lee, Kiwon Park, S. Chan Baek, Hyungseok C. Moon, Hyewon Kim, Baekgyu Kim, Yongkuk Choi, Young-Hyun Go, Wanxiangfu Tang, Jongsu Choi, Jung Kyoon Choi, Hyuk-Jin Cha, Hye Yoon Park, Ping Liang, V. Narry Kim, Kyudong Han, Kwangseog Ahn. "L1 retrotransposons exploit RNA m6A modification as an evolutionary driving force". *Nature Communications, 2021*.

## 연락과 위치

- 위치: 교수실 515호, 연구실 520호, YBS Building (E16-1), KAIST[^contact][^deptlist]
- 주소: 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea[^contact]
- 전화: 교수 +82-42-350-4327[^deptlist][^deptprof]
- 이메일: 교수 jungkyoon@kaist.ac.kr[^deptlist][^deptprof]
[^p1]: J. Y. Kim 외, J. K. Choi, Nature Genetics 55, 221-231 (온라인 2023-01-09). <https://doi.org/10.1038/s41588-022-01273-y> 초록 기준(출판사 논문 페이지).
[^p2]: J. Y. Kim, H. Bang, S.-J. Noh, J. K. Choi, Nucleic Acids Research 51, W134-W140 (온라인 2023-04-18). <https://doi.org/10.1093/nar/gkad275> 초록 기준.
[^p3]: J. Y. Kim 외, J. K. Choi, Science Advances 11, eadx8303 (2025). <https://doi.org/10.1126/sciadv.adx8303> 초록 기준.
[^p4]: M. Bae 외, J. K. Choi, Nature Communications 14, 2017 (온라인 2023-04-10). <https://doi.org/10.1038/s41467-023-37768-3> 초록 기준.
[^p5]: K. Kim 외, J. K. Choi, Scientific Reports 13, 22482 (온라인 2023-12-18). <https://doi.org/10.1038/s41598-023-49639-4> 초록 기준.
[^p6]: H. G. Kang 외, J. K. Choi, Cancer Research 82, 142-154 (온라인 2021-10-28). <https://doi.org/10.1158/0008-5472.can-21-2023> 초록 기준.
[^p7]: J. Kwon 외, J. K. Choi, Nature Biotechnology 41, 1593-1605 (온라인 2023-02-16). <https://doi.org/10.1038/s41587-023-01686-y> 초록 기준(출판사 논문 페이지).
[^p8]: H. J. Lee 외, J. K. Choi, British Journal of Cancer 133, 1708-1719 (온라인 2025-09-15). <https://doi.org/10.1038/s41416-025-03181-4> 초록 기준.
[^tcrbcr]: K. Seo, J. K. Choi, Genomics & Informatics 23, 6 (온라인 2025-02-24). <https://doi.org/10.1186/s44342-024-00034-z> 초록 기준.
[^l1]: S.-Y. Hwang 외, K. Ahn, Nature Communications 12, 880 (온라인 2021-02-09). <https://doi.org/10.1038/s41467-021-21197-1> 초록 기준.
[^research]: 연구실 누리집 Research 페이지 <https://omics.kaist.ac.kr/research> (연구 주제, 연구 키워드, 시스템 유전학·오믹스 인용 설명, 2026-10-23 열람)
[^resources]: 연구실 누리집 Resources 페이지 <https://omics.kaist.ac.kr/resources> (논문별 공개 도구·코드·자료, 2026-10-23 열람)
[^members]: 연구실 누리집 Members 페이지 <https://omics.kaist.ac.kr/members> (Current·Alumni 구역, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publications 페이지 <https://omics.kaist.ac.kr/publications> (페이지에 들어 있는 논문 목록 표 <https://docs.google.com/spreadsheets/d/1t9B1AUteaYIPxQtYwb8hIUN2rJYdT_K80lDS_xvQKMI/htmlembed?gid=0>; 목록 범위는 근거 페이지, 2026-10-23 열람)
[^contact]: 연구실 누리집 Contact 페이지 <https://omics.kaist.ac.kr/contact> (교수실·연구실 호수, 건물, 주소, 2026-10-23 열람)
[^cr]: 학술지 서지 기록(Crossref) <https://api.crossref.org/> (2021–2026년 목록 논문의 저자·DOI·출판일, 제목 검색과 DOI 조회 2026-10-23)
[^deptlist]: KAIST 바이오및뇌공학과 교수진 목록 <https://bioeng.kaist.ac.kr/index.php?mid=bio_03_01> (최정균 교수 항목: 직위, 박사 학위, 연구분야, 연구실, 전화, 이메일, 2026-10-23 열람)
[^deptprof]: KAIST 바이오및뇌공학과 교수 소개(최정균) <https://bioeng.kaist.ac.kr/index.php?document_srl=6860&mid=bio_03_01> (직위, 연구실명, 최종학위, 연구분야, 경력, 수상 경력, 대표 연구실적, 2026-10-23 열람)

# 뇌 치료 및 오가노이드 지능 연구실 (KAIST BRAIN RePAIR & ORGANOID INTELLIGENCE)

**KAIST 뇌인지과학과 · 최민이 조교수**

- 영문 표기: BRAIN RePAIR & ORGANØID 1NTEL, BRØ1 Lab
- 분야: 인간 뇌세포 실험 모형, 세포 영상 분석 방법, 약물 반응 예측, 생물학적 컴퓨팅
- 대분야: 컴퓨팅·AI, 기초생명·생물물리
- 태그: 바이오정보학·계산생물학[^home], AI 신약 개발[^home], 장기 칩·체외 질병 모델[^home]
- 홈페이지: <https://mineechoilab.kaist.ac.kr/>
- 근거와 출처: [뇌 치료 및 오가노이드 지능 연구실 근거 페이지](mineechoilab-sources.md)

> 사람의 뇌세포로 만든 실험 모형과 컴퓨터 분석을 연결해, 세포의 상태를 읽고 약물 반응을 예측하는 방법을 개발한다.[^home]

## 무엇을 연구하나

연구실은 인간 뇌세포를 이용한 약물 평가 플랫폼과 세포 상태를 읽는 계산 방법을 개발한다. 세포는 생물체를 이루고 생명 활동을 수행하는 기본 단위다. 인간 유도만능줄기세포(human induced pluripotent stem cell, hiPSC)는 성체 세포를 다양한 세포 종류로 바뀔 수 있는 상태로 되돌린 것이다. 분화는 세포가 특정 구조와 기능을 갖는 종류로 바뀌는 과정이다. 연구실은 환자에게서 얻은 이런 세포로 뇌세포와 뇌 오가노이드(장기의 구조나 기능 일부를 재현하도록 입체적으로 기른 세포 모형)를 만든다. 세포에서 얻은 자료를 분석해 환자마다 약물이 어떻게 작용할지 예측하고, 개인별 약물 조합을 찾는 것이 목표다.[^home] 대상은 파킨슨병·치매 같은 퇴행성 뇌질환이다.[^dept]

계산 분야에서는 세포 상태의 예측 모형을 개발한다. 누리집은 세포의 시간에 따른 변화 자료를 학습하고, 환자 사이의 차이를 반영해 약물 반응을 예측하는 인공지능 모형을 개발한다고 설명한다.[^home] 최근에는 영상 표현학습(영상의 특징을 이후 분석에 쓸 수 있는 수치 표현으로 배우는 방법)을 다뤘다. 서로 다른 특징들이 같은 수치 표현에 겹쳐 담겨 생기는 해석의 문제를 분석하고, 이를 줄인 영상 표현을 다른 종류의 세포 측정 자료와 연결하는 방법을 제안했다.[^p1] 살아 있는 신경세포(자극에 따른 전기적 변화와 세포 사이 화학 전달로 정보를 주고받는 세포)의 내부 구조를 반영해, 표지 물질(세포 구조를 형광 물질 등으로 표시하는 물질)을 붙이지 않은 영상으로 기능 이상을 찾는 분석 틀도 제시했다.[^p2]

또 다른 개발 방향은 **뇌 오가노이드와 계산 장치의 연결**이다. 연구실은 인간 세포에서 기른 뇌 오가노이드를 컴퓨터와 연결하는 신경 컴퓨터를 개발하며, 이를 학습과 기억에 대한 약물의 영향을 평가하는 실험 기반으로 삼으려 한다. 누리집은 이런 접근을 생물학적 컴퓨팅(살아 있는 생물의 정보 처리 기능을 계산에 이용하는 방식)이라고 소개한다. 목표는 약물의 작용을 세포의 상태뿐 아니라 인지 기능의 반응에서도 살펴보는 것이다.[^home]

기초 연구에서는 신경세포가 대사 스트레스(물질을 얻고 쓰는 세포 활동에 부담이 생긴 상태)에 어떻게 대응하는지도 비교한다. 인간 배아줄기세포(human embryonic stem cell, hESC; 초기 배아에서 얻어 다양한 세포로 분화할 수 있는 세포)에서 기른 신경세포와 유도만능줄기세포에서 기른 신경세포는 스트레스 아래의 회복·적응 양상이 달랐다. 이 연구는 세포를 얻은 방식에 따라 기능 유지 능력이 달라질 수 있음을 보여 주며, 실험 모형의 성질을 비교하는 기준으로 스트레스 대응 능력을 제시했다.[^p3]

## 주요 연구 주제

### 1. 세포 상태를 읽는 계산 방법

세포 영상의 특징을 해석 가능한 수치 표현으로 만들고, 서로 다른 종류의 세포 자료를 연결한다. 살아 있는 신경세포 영상에서는 내부 구조의 정보를 반영한 분석 방법으로 기능 이상을 구별한다. 대표 논문 1과 2가 이 갈래에 해당한다.[^p1][^p2]

### 2. 뇌 오가노이드 기반 약물 평가

환자 세포로 뇌 오가노이드를 만들고, 오가노이드와 계산 장치를 연결한 신경 컴퓨터와 세포 상태 예측 모형을 함께 쓰는 약물 평가 기반을 개발한다. 세포 수준의 변화와 학습·기억에 대한 반응을 함께 살피는 것이 목표다.[^home]

### 3. 신경세포의 기능 유지와 회복

인간 배아줄기세포와 유도만능줄기세포에서 각각 기른 신경세포를 비교해, 대사 스트레스 아래에서 기능을 유지하고 회복하는 양상의 차이를 연구한다. 대표 논문 3이 이 갈래에 해당한다.[^p3]

## 대표 논문

KAIST 재직 시기에 발표한 2021–2026년 연구 가운데 영상 분석 방법과 정상 세포 기능을 다룬 세 편을 골랐다. 세 편 모두 사전 공개본이다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 교신저자 표시는 연구실 누리집의 해당 논문 표기를 따른다.[^pubs][^pi]

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Resolving superposition in AI for interpretability and cross-modal alignment in patient-neuronal images](https://doi.org/10.48550/arXiv.2606.31394) · arXiv 사전 공개본 | 자료 차원에 비해 표현 공간이 좁아지는 조건에서 인공지능이 여러 특징을 같은 수치 표현에 겹쳐 담으면 해석뿐 아니라 표현 사이 거리 관계도 왜곡될 수 있음을 분석했다. 일부 특징만 활성화하도록 학습하는 희소 오토인코더(sparse autoencoder, SAE; 일부 수치 표현만 활성화되도록 제약하면서 입력 자료를 변환하고 복원하는 학습 모형)를 사용해 이러한 왜곡을 줄였다. 이어 영상 표현과 세포별 유전자(유전 정보를 담아 세포 기능에 관여하는 단위) 활동 측정 자료를 연결하는 GW-map(Gromov-Wasserstein 최적 수송으로 두 자료를 맞추는 방법)을 제안했다.[^p1] | 1저자 Jisung Park, 마지막·교신저자 Minee L. Choi |
| 2 | 2025 | [Organelle-Aware Representation Learning Enables Label-Free Detection of Mitochondrial Dysfunction in Live Human Neurons](https://doi.org/10.1101/2025.10.12.681848) · bioRxiv 사전 공개본 | 살아 있는 인간 신경세포를 빛으로 입체 관찰한 영상에 계산으로 가상의 표지를 입히고, 세포 내부 구조를 반영한 학습 모형과 모양 지표 기반 분류기(입력을 정해진 범주로 가르는 모형)를 제시했다. 미토콘드리아(세포 호흡에 관여하고 자체 유전 정보를 가진 세포 내부 구조)의 기능 이상을 두 모형 모두 약 85% 정확도로 구별했다.[^p2] | 1저자 SeungJu Yoo, 마지막·교신저자 Minee L. Choi |
| 3 | 2025 | [Autonomous neuronal resilience under metabolic stress highlights fundamental differences between hESC and hiPSC-derived neurons](https://doi.org/10.1101/2025.08.15.670492) · bioRxiv 사전 공개본 | 대사 스트레스 아래에서 인간 배아줄기세포 유래 신경세포는 세포 밀도가 늘고 형태와 기능이 유지되는 자발적 회복을 보였다. 유도만능줄기세포 유래 신경세포는 살아남았지만 적응 능력이 낮았다. 두 세포 모형의 기능적 성질을 비교할 기준으로 스트레스 대응 능력을 제안했다.[^p3] | 1저자 SeungJu Yoo, 마지막·교신저자 Minee L. Choi |

## 교수와 전문 분야

최민이 교수는 신경생리학자(신경계의 기능을 연구하는 학자)로, 인간 줄기세포로 만든 뇌세포 실험 모형과 계산 분석을 연결하는 연구를 한다. 한양대학교에서 학사·석사를 마치고 2013년 케임브리지대학교에서 임상신경과학 박사학위를 받았다. 이후 런던대학교와 프랜시스 크릭 연구소에서 연구했으며 2023년 2월 KAIST 뇌인지과학과 조교수로 부임했다.[^pi][^dept]

누리집 이력은 2024년부터 KAIST 줄기세포 및 재생생물학 대학원과 대만 Chang Gung University & Memorial Hospital의 겸임교수를 맡고 있다고 적는다. UCL Queen Square Institute of Neurology와 프랜시스 크릭 연구소의 Honorary Fellow(명예 펠로우)도 함께 기재되어 있다.[^pi]

최근 연구에서 드러나는 전문 분야는 인간 신경세포 실험 모형, 세포 영상의 수치 표현과 자료 결합, 세포 내부 구조를 반영한 영상 분석, 줄기세포 유래 신경세포의 스트레스 대응 비교다.[^p1][^p2][^p3]

## 응용 분야

주된 응용 목표는 환자 유래 뇌세포와 뇌 오가노이드에서 약물 반응을 예측하고 평가하는 전임상 기반이다. 전임상은 사람 대상 임상시험에 앞서 세포나 동물 등을 통해 성질과 작용을 살피는 연구 단계다. 연구실은 개인별 약물 조합의 예측과, 학습·기억에 대한 약물 영향 평가를 목표로 삼는다.[^home]

## 구성원

누리집 Team의 현재 연구 인력 13명과 Esteemed Collaborator로 적은 외부 협력자 4명이다. 과정·시작·연구 주제는 팀 목록과 개별 소개 표기를 따른다. MS/PhD는 석박사통합과정이며, Lab Chief와 UG/PhD (TUBE)는 누리집의 역할·과정 표기다. UG Research는 학부 연구 참여를 뜻한다. ‘대표 논문 참여’는 논문 저자와 이름이 같은 경우 표시했으며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^team]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Jieun Kim[^m-jieun-kim] | 박사후연구원 (InnoCore AI-CRED) | Sep, 2025 - Present | InnoCore AI-CRED |  |  |
| Daeun Yoo[^m-daeun-yoo] | Lab Chief (MS/PhD) | Mar, 2024 |  |  | 1 |
| Changwon Jung[^m-changwon-jung] | 석박사통합과정 | Sep, 2024 |  |  |  |
| Hayeon Kim[^m-hayeon-kim] | 석박사통합과정 | Mar, 2025 |  |  |  |
| Jeonghyun Kim[^m-jeonghyun-kim] | 석박사통합과정 | Mar, 2025 |  |  |  |
| Jisung Park[^m-jisung-park] | 석박사통합과정 | Mar, 2025 |  |  | 1 |
| Seohyeon Kang[^m-seohyeon-kang] | 석박사통합과정 | Mar, 2026 |  |  | 1 |
| Yeeun Shin[^m-yeeun-shin] | 석박사통합과정 | Sep, 2026 |  |  |  |
| Yuchae Lee[^m-yuchae-lee] | 석박사통합과정 | Mar, 2024 |  |  |  |
| Ian Choi[^m-ian-choi] | UG/PhD (TUBE) | Sep, 2025 - Present |  |  | 1 |
| Seoin Cho[^m-seoin-cho] | UG Research | Mar, 2024 - Present |  |  | 1 |
| Wooyeop Choi[^m-wooyeop-choi] | UG Research | 2026 - Present |  |  | 1 |
| Yonghun Son[^m-yonghun-son] | UG Research | Mar, 2025 - Present |  |  |  |
| Andrey Y. Abramov[^m-andrey-abramov] | Esteemed Collaborator |  |  |  |  |
| David Klenerman[^m-david-klenerman] | Esteemed Collaborator |  |  | dk10012@cam.ac.uk |  |
| Roger Barker[^m-roger-barker] | Esteemed Collaborator |  |  | rab46@cam.ac.uk |  |
| Sonia Gandhi[^m-sonia-gandhi] | Esteemed Collaborator |  |  | sonia.gandhi@crick.ac.uk | 1 |

## 졸업생과 이전 구성원

누리집 Team의 이전 구성원 17명이다. Ex-MS·Ex-UG·Ex-Internship·Ex-MD Internship은 누리집이 적은 이전 과정·참여 구분이다. 괄호 안의 Feb, 2025는 졸업 시점이고, 그 밖의 기간은 누리집이 적은 활동 기간이다. Present도 누리집의 기간 표기다. 진로 칸은 누리집에 적힌 진로를 담는다.[^team]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Eunjin Yang[^m-eunjin-yang] | Ex-MS (Feb, 2025) |  |
| Seungju Yoo[^m-seungju-yoo] | Ex-MS (Feb, 2025) |  |
| Amen Woldesenbet[^m-amen-woldesenbet] | Ex-UG (Mar - Dec, 2024) |  |
| Donghyun Kim[^m-donghyun-kim] | Ex-UG (2025) |  |
| Irene Song[^m-irene-song] | Ex-UG (2025) |  |
| Jeongwoo Lee[^m-jeongwoo-lee] | Ex-UG (Mar, 2024 - Dec, 2025) |  |
| Jihee Yu[^m-jihee-yu] | Ex-UG (2025 - 2026) |  |
| Jungyoon Nam[^m-jungyoon-nam] | Ex-UG (Sep, 2023 - Present) |  |
| Sumin Lee[^m-sumin-lee] | Ex-UG (2025 - 2026) |  |
| Geonhee Go[^m-gunhee-go] | Ex-Internship (Summer break, 2026) |  |
| Hyeonjin Kwak[^m-hyeonjin-kwak] | Ex-Internship (Summer break, 2026) |  |
| Hyeonseo Choi[^m-hyeonseo-choi] | Ex-Internship (Winter break, 2023) |  |
| Jaewoong Yoon[^m-jaewoong-yoon] | Ex-Internship (Summer break, 2024) |  |
| Jeongjin Lee[^m-jeongjin-lee] | Ex-Internship (Winter break, 2023 & Summer break, 2024) |  |
| Yejin Hong[^m-yejin-hong] | Ex-Internship (Summer break, 2026) |  |
| Eunsu Lee[^m-eunsu-lee] | Ex-MD Internship (Dec, 2024 - July, 2026) |  |
| Jihee Kim[^m-jihee-kim] | Ex-MD Internship (Nov, 2024 - July, 2025) |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications의 2021–2026년 연도 구역 논문 가운데 세 편이다. 발표처와 저자는 누리집 표기 그대로이며 DOI를 함께 적었다. arXiv와 openRxiv로 적힌 이 세 항목은 사전 공개본이다.[^pubs][^p1][^p2][^p3]

**2026**

- Jisung Park, Seohyeon Kang, Daeun Yoo, Eunsu Lee, Seoin Cho, ..., Ian Choi, James R. Evan, Daesoo Kim, Sonia Gandhi, Minee L. Choi. "Resolving superposition in AI for interpretability and cross-modal alignment in patient-neuronal images". *arXiv*. <https://doi.org/10.48550/arXiv.2606.31394>

**2025**

- SeungJu Yoo, Eunjin Yang, Seo-Hyun Kim, Hoewon Park, Daesoo Kim, Ki-Jun Yoon, Minee L. Choi. "Organelle-Aware Representation Learning Enables Label-Free Detection of Mitochondrial Dysfunction in Live Human Neurons". *openRxiv*. <https://doi.org/10.1101/2025.10.12.681848>
- SeungJu Yoo, Eunjin Yang, Minee L. Choi. "Autonomous neuronal resilience under metabolic stress highlights fundamental differences between hESC and hiPSC-derived neurons". *openRxiv*. <https://doi.org/10.1101/2025.08.15.670492>

## 수상과 선정

교수 소개의 Honours & Awards에 적힌 2023–2024년 수상 세 건이다. 연도는 누리집의 연도 표기이고 날짜는 게시되어 있지 않다.[^pi]

- 2024 · KAIST Q-DAY Special Prize (Internatinalization)
- 2024 · KAIST Outstanding Lecture Award
- 2023 · KAIST Q-DAY Special Prize (Education)

## 연락과 위치

- 교수 이메일: minee.choi@kaist.ac.kr[^contact][^pi]
- 전화: +82 (0)42-350-6516[^contact]
- 연구실: KAIST 메타융합관(W13) 5층 Room 4[^contact]
- 주소: 대전광역시 유성구 대학로 291, KAIST[^contact]
[^home]: 연구실 누리집, 첫 화면의 국문·영문 연구실 소개. <https://mineechoilab.kaist.ac.kr/> 관측 2026-11-12.
[^pubs]: 연구실 누리집, Publications의 All 및 Selected 목록과 저자 역할 표시. <https://mineechoilab.kaist.ac.kr/publications/> 관측 2026-11-12.
[^pi]: 연구실 누리집, Minee Choi의 Biographical Sketch·Professional History·Honours & Awards. <https://mineechoilab.kaist.ac.kr/members/minee-choi.html> 관측 2026-11-12.
[^dept]: KAIST 뇌인지과학과, 최민이 교수 국문 소개. <https://bcs.kaist.ac.kr/korean/sub030101/view/id/117> 관측 2026-11-12.
[^team]: 연구실 누리집, Team의 현재 구성원·이전 구성원·외부 협력자 목록. <https://mineechoilab.kaist.ac.kr/team/> 관측 2026-11-12.
[^contact]: 연구실 누리집, Contact의 업무 연락처·위치·소속 소개. <https://mineechoilab.kaist.ac.kr/contact/> 관측 2026-11-12.
[^p1]: J. Park 외, M. L. Choi, arXiv (2026). <https://doi.org/10.48550/arXiv.2606.31394> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5108206730,publication_year:2021-2026> 관측 2026-11-12.
[^p2]: S. Yoo 외, M. L. Choi, bioRxiv (2025). <https://doi.org/10.1101/2025.10.12.681848> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5108206730,publication_year:2021-2026> 관측 2026-11-12.
[^p3]: S. Yoo, E. Yang, M. L. Choi, bioRxiv (2025). <https://doi.org/10.1101/2025.08.15.670492> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5108206730,publication_year:2021-2026> 관측 2026-11-12.
[^m-jieun-kim]: 연구실 누리집, Jieun Kim 개별 소개. <https://mineechoilab.kaist.ac.kr/members/jieun-kim.html> 관측 2026-11-12.
[^m-daeun-yoo]: 연구실 누리집, Daeun Yoo 개별 소개. <https://mineechoilab.kaist.ac.kr/members/daeun-yoo.html> 관측 2026-11-12.
[^m-changwon-jung]: 연구실 누리집, Changwon Jung 개별 소개. <https://mineechoilab.kaist.ac.kr/members/changwon-jung.html> 관측 2026-11-12.
[^m-hayeon-kim]: 연구실 누리집, Hayeon Kim 개별 소개. <https://mineechoilab.kaist.ac.kr/members/hayeon-kim.html> 관측 2026-11-12.
[^m-jeonghyun-kim]: 연구실 누리집, Jeonghyun Kim 개별 소개. <https://mineechoilab.kaist.ac.kr/members/jeonghyun-kim.html> 관측 2026-11-12.
[^m-jisung-park]: 연구실 누리집, Jisung Park 개별 소개. <https://mineechoilab.kaist.ac.kr/members/jisung-park.html> 관측 2026-11-12.
[^m-seohyeon-kang]: 연구실 누리집, Seohyeon Kang 개별 소개. <https://mineechoilab.kaist.ac.kr/members/seohyeon-kang.html> 관측 2026-11-12.
[^m-yuchae-lee]: 연구실 누리집, Yuchae Lee 개별 소개. <https://mineechoilab.kaist.ac.kr/members/yuchae-lee.html> 관측 2026-11-12.
[^m-ian-choi]: 연구실 누리집, Ian Choi 개별 소개. <https://mineechoilab.kaist.ac.kr/members/ian-choi.html> 관측 2026-11-12.
[^m-seoin-cho]: 연구실 누리집, Seoin Cho 개별 소개. <https://mineechoilab.kaist.ac.kr/members/seoin-cho.html> 관측 2026-11-12.
[^m-yonghun-son]: 연구실 누리집, Yonghun Son 개별 소개. <https://mineechoilab.kaist.ac.kr/members/yonghun-son.html> 관측 2026-11-12.
[^m-eunjin-yang]: 연구실 누리집, Eunjin Yang 개별 소개. <https://mineechoilab.kaist.ac.kr/members/eunjin-yang.html> 관측 2026-11-12.
[^m-seungju-yoo]: 연구실 누리집, Seungju Yoo 개별 소개. <https://mineechoilab.kaist.ac.kr/members/seungju-yoo.html> 관측 2026-11-12.
[^m-amen-woldesenbet]: 연구실 누리집, Amen Woldesenbet 개별 소개. <https://mineechoilab.kaist.ac.kr/members/amen-woldesenbet.html> 관측 2026-11-12.
[^m-jeongwoo-lee]: 연구실 누리집, Jeongwoo Lee 개별 소개. <https://mineechoilab.kaist.ac.kr/members/jeongwoo-lee.html> 관측 2026-11-12.
[^m-hyeonseo-choi]: 연구실 누리집, Hyeonseo Choi 개별 소개. <https://mineechoilab.kaist.ac.kr/members/hyeonseo-choi.html> 관측 2026-11-12.
[^m-jaewoong-yoon]: 연구실 누리집, Jaewoong Yoon 개별 소개. <https://mineechoilab.kaist.ac.kr/members/jaewoong-yoon.html> 관측 2026-11-12.
[^m-jeongjin-lee]: 연구실 누리집, Jeongjin Lee 개별 소개. <https://mineechoilab.kaist.ac.kr/members/jeongjin-lee.html> 관측 2026-11-12.
[^m-eunsu-lee]: 연구실 누리집, Eunsu Lee 개별 소개. <https://mineechoilab.kaist.ac.kr/members/eunsu-lee.html> 관측 2026-11-12.
[^m-jihee-kim]: 연구실 누리집, Jihee Kim 개별 소개. <https://mineechoilab.kaist.ac.kr/members/jihee-kim.html> 관측 2026-11-12.
[^m-andrey-abramov]: 연구실 누리집, Andrey Y. Abramov 개별 소개. <https://mineechoilab.kaist.ac.kr/members/andrey_%20abramov.html> 관측 2026-11-12.
[^m-david-klenerman]: 연구실 누리집, David Klenerman 개별 소개. <https://mineechoilab.kaist.ac.kr/members/david_klenerman.html> 관측 2026-11-12.
[^m-roger-barker]: 연구실 누리집, Roger Barker 개별 소개. <https://mineechoilab.kaist.ac.kr/members/roger-barker.html> 관측 2026-11-12.
[^m-sonia-gandhi]: 연구실 누리집, Sonia Gandhi 개별 소개. <https://mineechoilab.kaist.ac.kr/members/sonia_gandhi.html> 관측 2026-11-12.
[^m-donghyun-kim]: 연구실 누리집, Donghyun Kim 개별 소개. <https://mineechoilab.kaist.ac.kr/members/donghyun-kim.html> 관측 2026-11-12.
[^m-gunhee-go]: 연구실 누리집, Geonhee Go 개별 소개. <https://mineechoilab.kaist.ac.kr/members/gunhee-go.html> 관측 2026-11-12.
[^m-hyeonjin-kwak]: 연구실 누리집, Hyeonjin Kwak 개별 소개. <https://mineechoilab.kaist.ac.kr/members/hyeonjin-kwak.html> 관측 2026-11-12.
[^m-irene-song]: 연구실 누리집, Irene Song 개별 소개. <https://mineechoilab.kaist.ac.kr/members/irene-song.html> 관측 2026-11-12.
[^m-jihee-yu]: 연구실 누리집, Jihee Yu 개별 소개. <https://mineechoilab.kaist.ac.kr/members/jihee-yu.html> 관측 2026-11-12.
[^m-jungyoon-nam]: 연구실 누리집, Jungyoon Nam 개별 소개. <https://mineechoilab.kaist.ac.kr/members/jungyoon-nam.html> 관측 2026-11-12.
[^m-sumin-lee]: 연구실 누리집, Sumin Lee 개별 소개. <https://mineechoilab.kaist.ac.kr/members/sumin-lee.html> 관측 2026-11-12.
[^m-wooyeop-choi]: 연구실 누리집, Wooyeop Choi 개별 소개. <https://mineechoilab.kaist.ac.kr/members/wooyeop-choi.html> 관측 2026-11-12.
[^m-yeeun-shin]: 연구실 누리집, Yeeun Shin 개별 소개. <https://mineechoilab.kaist.ac.kr/members/yeeun-shin.html> 관측 2026-11-12.
[^m-yejin-hong]: 연구실 누리집, Yejin Hong 개별 소개. <https://mineechoilab.kaist.ac.kr/members/yejin-hong.html> 관측 2026-11-12.

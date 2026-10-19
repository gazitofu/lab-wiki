# 디지털 헤리티지 연구실 (Digital Heritage Lab)

**KAIST 문화기술대학원 · 안재홍 초빙교수**

- 분야: 디지털 헤리티지(디지털 기술로 문화유산을 기록·해석·전달하는 분야), 문화유산 3차원 스캔과 분석, 유산 메타버스와 가상 박물관, 문화유산 기관을 위한 인공지능
- 홈페이지: <https://dhlab.kaist.ac.kr/>
- 근거와 출처: [디지털 헤리티지 연구실 근거 페이지](digital-heritage-sources.md)

> 문화유산을 3차원 스캔과 사진 기술로 정밀하게 기록하고, 메타버스·가상현실 같은 디지털 공간에서 사람들이 유산을 체험하고 이해하도록 돕는 방법을 연구하는 연구실이다. 박물관 같은 문화유산 기관이 인공지능을 믿고 쓸 수 있게 하는 연구도 한다.[^gsmv][^p1][^p2]

## 무엇을 연구하나

메타버스대학원 참여 연구실 소개는 연구 관심사로 디지털 헤리티지, 문화유산 3차원 기록과 분석, 디지털 기술의 문화유산 분야 적용, 박물관 기술, 가상 박물관을 든다.[^gsmv] 문화기술대학원 교수 소개는 교수의 분야를 디지털 헤리티지와 3차원 스캐닝으로 적는다.[^ct]

첫 번째 갈래는 **유산 메타버스와 디지털 유산 체험**이다. 국립중앙박물관이 메타버스 플랫폼 제페토에 만든 유산 메타버스에서 20대 참여자 12명이 닷새 동안 겪은 경험을 질적 방법으로 분석해, 사용자가 주도하는 유산 해석 경험을 설계하는 데 필요한 점을 정리했다.[^p1] 연구실 소개 페이지에 실린 다른 연구는 익산 미륵사지 메타버스에서 102명을 대상으로, 함께 접속한 사람들 사이의 소통 방식이 문화 학습에 어떤 영향을 주는지 분석했다.[^p3][^gsmv]

두 번째 갈래는 **문화유산 기관을 위한 인공지능**이다. 대형 언어 모델(LLM)은 그럴듯한 거짓 답(환각)을 내기 쉬워 박물관이 쓰기 어렵다. 연구실은 웹에서 모은 자료가 문화유산 분야에서 믿을 만한지 걸러 내는 검증 절차와, 전문가가 알맞은 자료를 모으도록 질문을 만들어 주는 에이전트를 제안했다.[^p2]

세 번째 갈래는 **문화유산의 디지털 기록과 진단**이다. 빛의 방향을 바꿔 가며 찍은 사진으로 표면을 다시 비춰 볼 수 있게 하는 반사 변환 영상(RTI)으로 조선 시대 동전의 보존 처리 과정을 기록해, 맨눈으로 보기 어려운 표면 변화를 찾아냈다.[^p4] 가상현실에서 목조 건축 문화유산을 원격으로 진단하기 위한 정보 구조도 설계했다.[^p5]

교수는 문화유산 3차원 스캔 지침, 공룡 발자국 화석의 3차원 기록, 가상 석굴 재구성 같은 연구를 2010년대부터 학술대회에 발표해 왔다.[^crossref]

## 주요 연구 주제

### 1. 유산 메타버스와 디지털 유산 소통

사용자 주도 유산 해석, 소셜 가상현실의 문화 학습.[^p1][^p3] 대표 논문 1, 3.

### 2. 문화유산 기관을 위한 신뢰할 수 있는 인공지능

웹 자료 신뢰도 검증, 큐레이터 질문 생성.[^p2] 대표 논문 2.

### 3. 문화유산 3차원·영상 기록과 원격 진단

반사 변환 영상 기록, 가상현실 원격 진단.[^p4][^p5] 대표 논문 4, 5.

## 대표 논문

메타버스대학원 연구실 소개에 실린 논문과 안재홍 교수가 저자로 참여한 문화유산 주제 논문 가운데 초록이 있는 것을 골랐다. 3은 연구실 소개 페이지가 연구실 논문으로 올린 것이며 교수는 저자 명단에 없다. 5는 2021년 이전 논문이다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^crossref] |
|---|---|---|---|---|
| 1 | 2024 | [Diving into a Heritage Metaverse: Learning from End User-driven Experiences and Perspectives to Enhance Virtual Heritage Interpretation](https://doi.org/10.1145/3637322) · Proceedings of the ACM on Human-Computer Interaction | 국립중앙박물관이 제페토에 만든 유산 메타버스 Peaceful Hill에서 20대 12명이 닷새 동안 겪은 경험을 문화 탐침(참여자가 스스로 기록하는 도구)과 집단 면접으로 분석했다. 공간 구성, 생활 기록 같은 상호작용, 매개 역할, 유산 해석이라는 네 주제를 찾아 참여형 유산 해석 경험의 설계 방향을 제시했다.[^p1] | 1저자 Hyeseung Shim, 마지막 저자 안재홍 |
| 2 | 2025 | [Towards a Curatorial Agent for Heritage Institutions: Web Source Credibility Verification for Grounding Domain-Specific LLMs](https://doi.org/10.5194/isprs-archives-xlviii-m-9-2025-1213-2025) · ISPRS Archives | 박물관이 대형 언어 모델을 쓰려면 환각 문제를 줄여야 해서, 웹 자료를 근거로 붙이되 그 자료가 믿을 만한지 거르는 검증 절차와 전문가에게 자료 수집 질문을 만들어 주는 에이전트를 제안했다. 두 분류 과제에서 중간 수준의 성능을 냈고 학습용 데이터셋도 만들었다.[^p2] | 1저자 Aleksandra Pshenova, 마지막 저자 안재홍 |
| 3 | 2025 | [Exploring the Social Heritage Metaverse for Virtual Heritage Communication from Multi End-user Centered Experiences](https://doi.org/10.1145/3736225) · ACM Journal on Computing and Cultural Heritage | 익산 미륵사지 메타버스에서 102명(34개 모둠)을 대상으로 여럿이 함께 쓰는 가상현실이 문화 학습에 주는 영향을 검증했다. 서로 주고받는 소통, 함께 있다는 느낌, 협력은 학습에 도움이 되고 일부 요인은 오히려 방해가 됐다.[^p3] | 1저자 Hyeseung Shim, Kyung Taek Oh 공저, 마지막 저자 Chung-Kon Shi(안재홍 교수는 저자 아님) |
| 4 | 2021 | [Reflectance transformation imaging for documenting changes through treatment of Joseon dynasty coins](https://doi.org/10.1186/s40494-021-00584-3) · Heritage Science | 빛의 위치를 계산해 화면에서 조명을 바꿔 볼 수 있는 반사 변환 영상(RTI)으로 조선 시대 동전의 녹 제거·강화 처리 단계를 기록했다. 녹에 덮였던 글자의 획이 가상 조명으로 또렷이 드러나, 맨눈으로 보기 어려운 변화를 찾는 도구가 될 수 있음을 보였다.[^p4] | 1저자 Jihyun Min, 안재홍 공저(8명 중 여섯째), 마지막 저자 Sangdoo Ahn |
| 5 | 2019 | [Remote Diagnosis of Architectural Heritage Based on 5W1H Model-Based Metadata in Virtual Reality](https://doi.org/10.3390/ijgi8080339) · ISPRS International Journal of Geo-Information | 건축 문화유산을 가상현실에서 원격으로 진단하도록, 육하원칙(5W1H)에 따라 상황 정보를 붙이는 메타데이터 구조를 설계했다. 위치 기반 콘텐츠 도구와 원격 진단 앱을 만들어 전문가 평가를 했고, 상황에 맞는 정보를 주는 기능의 만족도가 가장 높았다.[^p5] | 1저자 Jongwook Lee, 안재홍 셋째 저자, 마지막 저자 Woontack Woo |

## 교수와 전문 분야

안재홍 교수는 서울대 기계설계학 학사(1989–1994)·석사(1995–1997)와 KAIST 문화기술학 박사(2009–2015)를 받았고, 2016년 11월부터 KAIST 문화기술대학원 초빙교수다.[^ct] 메타버스대학원 참여 교수 소개는 관심 분야를 디지털 문화유산으로 적는다.[^gsmv-prof]

논문으로 보면 전문 분야는 세 갈래다.

- **유산 메타버스와 디지털 유산 해석**.[^p1]
- **문화유산 분야 인공지능의 신뢰성**.[^p2]
- **문화유산 3차원·영상 기록과 원격 진단**.[^p4][^p5][^crossref]

## 응용 분야

대표 논문으로 보면 박물관 전시와 교육, 문화재 보존 처리 기록, 건축 문화유산 관리, 박물관의 인공지능 도입에 닿아 있다.[^p1][^p2][^p4][^p5] 메타버스대학원 지원 성과로 베트남 후에 디지털 박물관 사례를 다룬 공적개발원조(ODA) 디지털 박물관 틀 연구가 실려 있다.[^gsmv-prof]

## 구성원

메타버스대학원 연구실 소개에 실린 명단이다(2026년 10월 19일 열람).[^gsmv] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| 배서현 | 박사과정 |  |
| 두지언 | 박사과정 |  |
| 오경택 | Interdisciplinary Major |  |

## 졸업생

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 쿨롱지나 | Master Course |  |

## 최근 논문 목록

메타버스대학원 연구실 소개·참여 교수 소개에 실린 논문 3편과 안재홍 교수가 저자로 참여한 2021년 이후 문화유산 주제 논문 3편이다.[^gsmv][^gsmv-prof][^crossref]

**2026**

- Hail Song, Jinseok Hong, Seonji Kim, Kyung Taek Oh, Woontack Woo, and Sungyoung Kim. "VR Zen Garden: Designing a Virtual Environment for Stress Relief". *2026 IEEE Conference on Virtual Reality and 3D User Interfaces Abstracts and Workshops (VRW)*.

**2025**

- Hyeseung Shim, Kyung Taek Oh, Chung-Kon Shi. "Exploring the Social Heritage Metaverse for Virtual Heritage Communication from Multi End-user Centered Experiences". *ACM Journal on Computing and Cultural Heritage*.
- Aleksandra Pshenova, Jaehong Ahn. "Towards a Curatorial Agent for Heritage Institutions: Web Source Credibility Verification for Grounding Domain-Specific LLMs". *The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences*.

**2024**

- Hyeseung Shim, Eun Seo Kim, Kyung Taek Oh, Chung-Kon Shi, Jaehong Ahn. "Diving into a Heritage Metaverse: Learning from End User-driven Experiences and Perspectives to Enhance Virtual Heritage Interpretation". *Proceedings of the ACM on Human-Computer Interaction*.

**2021**

- Jihyun Min, Sanghoon Jeong, Kangwoo Park, Yeonghwan Choi, Daewon Lee, Jaehong Ahn, Donghwan Har, Sangdoo Ahn. "Reflectance transformation imaging for documenting changes through treatment of Joseon dynasty coins". *Heritage Science*.

**연도 표기 없음**

- Seohyeun Bae, Jieon Du, and Jaehong Ahn. "The Need for a Digital Museum Framework in ODA: Lessons from the Hue Digital Museum, Vietnam". *메타버스대학원 지원 성과(게재처·연도 표기 없음)*.

## 연락과 위치

- 교수 이메일: ahnjaehong@kaist.ac.kr[^ct]
- 교수 전화: 042-350-2991[^ct]
- 위치: KAIST N25동 3228호 (대전 유성구 대학로 291)[^ct]

[^gsmv]: KAIST 메타버스대학원 참여 연구실 소개(Digital Heritage Lab) <https://meta.kaist.ac.kr/labs/dh-lab> (2026-10-19 열람)
[^gsmv-prof]: KAIST 메타버스대학원 참여 교수 소개(안재홍) <https://meta.kaist.ac.kr/members/11> (2026-10-19 열람)
[^ct]: KAIST 문화기술대학원 교수 소개(안재홍) <https://ct.kaist.ac.kr/boards/view/faculty_board/118> (2026-10-20 열람)
[^crossref]: Crossref 저자 검색(Jaehong Ahn, 문화유산·박물관 주제) <https://api.crossref.org/works?query.author=Jaehong+Ahn&query.bibliographic=heritage+museum+digital+cultural> (2026-10-20 조회)
[^p1]: H. Shim 외, J. Ahn, Proceedings of the ACM on Human-Computer Interaction (2024). <https://doi.org/10.1145/3637322> 초록 기준.
[^p2]: A. Pshenova, J. Ahn, The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences (2025). <https://doi.org/10.5194/isprs-archives-xlviii-m-9-2025-1213-2025> 초록 기준.
[^p3]: H. Shim, K. T. Oh, C.-K. Shi, Journal on Computing and Cultural Heritage 18, 1-36 (온라인 2025-07-24). <https://doi.org/10.1145/3736225> 초록 기준.
[^p4]: J. Min 외, S. Ahn, Heritage Science 9, 105 (온라인 2021-09-08). <https://doi.org/10.1186/s40494-021-00584-3> 초록 기준.
[^p5]: J. Lee, J. Kim, J. Ahn, W. Woo, ISPRS International Journal of Geo-Information 8, 339 (온라인 2019-07-30). <https://doi.org/10.3390/ijgi8080339> 초록 기준.

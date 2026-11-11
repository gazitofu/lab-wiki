# KAIST IAM Group (Integrated Assessment Modeling Group)

**KAIST 녹색성장지속가능대학원 · 믹전 해원 부교수**

- 영문 이름: KAIST IAM Group
- 분야: 기후·에너지 통합평가, 탈탄소 경로, 정책 시나리오
- 대분야: 에너지·환경·지구, 컴퓨팅·AI
- 태그: 기후·극한 기상[^models], 과학·공학 AI[^models][^p1], 기후·에너지 통합평가모형[^home][^models]
- 홈페이지: <https://kaist-iam.github.io/group/>
- 근거와 출처: [KAIST IAM Group 근거 페이지](kaist-iam-sources.md)

> 에너지·경제·토지·기후를 연결한 계산 모형을 만들고 활용해, 온실가스를 줄이는 기술과 정책의 조합 및 그 사회경제적 영향을 연구하는 그룹이다.

## 무엇을 연구하나

KAIST IAM Group은 통합평가모형(Integrated Assessment Model, IAM, 에너지·경제·토지·물·기후의 관계를 연결해 함께 계산하는 모형)을 개발하고 활용한다. 환경과학, 에너지 시스템 공학, 경제학, 공공정책을 결합해 넷제로(온실가스 배출량과 제거량의 차이가 없는 상태)에 이르는 경로와 기후변화 대응 전략을 연구한다. 기술의 보급과 정책의 효과를 같은 틀에서 비교해 실제 의사결정을 돕는 것이 목적이다.[^home][^models]

기본 도구인 GCAM(Global Change Analysis Model)은 에너지·물·토지·경제·기후를 연결한다. 그룹은 이를 바탕으로 한국의 조건, 산업별 세부 구조와 정책 시나리오(정책 등 서로 다른 조건을 가정해 미래 변화를 계산하는 설정)를 담은 GCAM-KAIST를 개발한다. GHIM(Geophysics-Human Interaction Model) 과제에서는 기후변화가 인간 사회에 미치는 영향과 정책·이주·무역 같은 사회경제적 대응이 다시 기후 시스템에 미치는 영향을 함께 모의하는 틀을 개발하려 한다.[^models][^p3]

계산에 드는 시간도 연구 대상이다. 기계학습(자료에서 관계와 규칙을 학습해 예측이나 판단에 쓰는 계산 방법)으로 기존 통합평가모형의 결과를 재현하는 대리 모형(원래 모형의 입력과 출력 관계를 근사하는 모형)을 개발한다. ML-IAM(기계학습으로 통합평가모형을 대신하는 계산 모형) 연구는 서로 다른 모형 계열의 결과를 학습해 기후 시나리오를 빠르게 탐색하는 방법을 제시한다.[^p1]

기술 전환의 총량과 비용에 더해 누가 부담을 지는지도 살핀다. 인도의 에너지 빈곤(생활에 필요한 에너지 서비스를 안정적으로 이용하지 못하거나 그 비용을 감당하기 어려운 상태), 한국의 농업과 식량 자급정책(국내에서 소비하는 식량의 일정 비율을 국내 생산으로 충당하려는 정책)을 분석해 사회집단별 취약성과 생산자·소비자 사이의 차이를 연구한다.[^p2][^p3]

## 주요 연구 주제

### 1. 한국과 세계의 탈탄소 경로

GCAM-KAIST에 국가별 조건과 산업별 세부 구조를 반영해 탈탄소화(인간 활동에서 발생하는 이산화탄소 배출을 줄이는 전환)를 분석한다. 석탄발전소를 개별 발전 단위로 표현하도록 모형을 확장하는 연구도 진행한다. 발전소별 수명·전력망(전기를 생산하는 곳과 사용하는 곳을 연결해 전기를 공급하는 설비의 망) 연결·자원 조건의 차이를 국가 및 세계의 장기 경로와 연결하는 접근이다.[^models]

탄소 제거(대기에서 이산화탄소를 빼내 지속적으로 저장하는 활동)와 배출 감축을 함께 확대하는 경로도 연구한다. 대표 논문 4는 두 전략을 동시에 강하게 추진하는 경로를 비교하되, 현재 조건에서 곧바로 실행할 수 있는 전망이 아니라 이상적인 가능 조건에서 달성할 수 있는 기후적 상한으로 제시한다. 대표 논문 5는 항공·해운까지 포함한 세계 운송 부문의 전환과 에너지 공급에 미치는 영향을 분석한다.[^p4][^p5]

### 2. 인공지능을 이용한 기후·인간 상호작용 모형

GHIM 과제는 MetaEarth Lab과 협력해 지구 시스템과 인간 사회 사이의 양방향 영향을 모형화하려 한다. 인공지능으로 물·식량·에너지·도시 부문의 세부 관계를 다루고, 정책과 무역 등 사회경제적 변화도 함께 분석하는 것이 목표다.[^models]

ML-IAM v1.0 사전 공개본은 IPCC(Intergovernmental Panel on Climate Change, 기후변화에 관한 정부 간 협의체)의 제6차 평가보고서 시나리오 자료로 대리 모형을 학습했다. 초록은 ML-IAM v1.0이 2천 개 시나리오의 결과를 50초에 생성한다고 보고한다. 전통적인 통합평가모형을 보완하는 계산 방법으로 제시한 결과다.[^p1]

연구실은 딥러닝(여러 층의 신경망을 통해 자료의 표현을 단계적으로 학습하는 기계학습 분야)으로 합성 시나리오(원자료에 없던 값을 모형이 새로 만든 시나리오)를 생성하는 연구도 소개한다. 여기서 신경망은 연결된 계산 단위들이 입력을 변환하며 자료의 관계를 학습하는 모형이다. 개별 설명에 따르면 기존 통합평가모형 시나리오의 변수 분포와 변수 사이 관계를 재현하고, 발전 부문의 물리적 일관성을 내부 점검했다.[^p7]

### 3. 에너지 접근성과 전환의 분배 효과

인도 연구는 카스트(출생을 바탕으로 구분되는 인도의 사회적 신분 집단)·농촌 거주·교육·소득의 불리함이 겹칠 때 전기와 취사 연료의 접근성 및 비용 부담이 어떻게 달라지는지 분석했다. 특히 농촌 가구가 직접 모은 연료를 쓸 수 있어 금전 부담은 낮게 보이더라도, 연료 수집에 드는 무급 노동 부담이 가려질 수 있음을 보여 준다. 하나의 에너지 빈곤 지표로 모든 취약성을 대표하기 어렵다는 결과다.[^p2]

### 4. 농업·토지와 지역별 전환 영향

한국의 농업 연구는 국내 기후 영향, 다른 지역의 생산 변화가 무역을 통해 미치는 영향, 식량 자급정책을 함께 분석한다. 국내 작물 수확량에 대한 직접 영향보다 세계 기후변화에 따른 무역 변화가 한국에 큰 영향을 줄 수 있으며, 밀·콩 자급정책은 생산자 수입을 늘리면서 소비자 지출도 높일 수 있다고 보고했다.[^p3]

토지 연구는 통합평가와 세부 토지 이용 모형을 연결해 1.5°C 목표를 위한 기후 공약이 세계의 경작지에 미칠 영향을 분석한다. 식량 안보나 환경에 뜻하지 않은 영향이 생기지 않도록 지속가능성의 다른 측면도 함께 살펴야 한다는 연구실 설명이다.[^p8] 미국의 주별 연구는 탄소중립 경로에 따른 자본 투자·좌초 자산(경제적 수명이 끝나기 전에 가치를 잃는 자산), 물 취수·대기오염 피해 비용·산림 면적을 함께 평가한다. 국가 배출 감축에 대한 각 주의 기여와 그 주에 돌아오는 경제·환경 효과 사이에 상관관계가 없을 수 있다는 결과다.[^p6]

## 대표 논문

KAIST 재직 시기의 믹전 해원 또는 공동 PI 엄지용이 저자인 논문을 계산 방법, 분배, 농업·토지, 탄소 제거, 운송, 지역별 전환 영향의 갈래로 골랐다. 학술지 논문 7편과 사전 공개본 1편이며, 방문교수 시기의 논문도 포함한다. “쉽게 말하면” 칸은 1–6번은 각 논문의 초록, 7–8번은 각주에 밝힌 연구실 개별 설명만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [ML-IAM v1.0: Emulating Integrated Assessment Models With Machine Learning](https://doi.org/10.5194/egusphere-2025-5305) · 사전 공개본 | 기후·경제·기술 조건에 따라 미래를 계산하는 통합평가모형은 계산 부담이 크다. 여러 모형 계열의 결과를 학습한 기계학습 대리 모형을 제시해, 원래 모형의 결과를 빠르게 탐색할 수 있도록 했다. 초록은 ML-IAM v1.0이 서로 다른 IAM 계열의 예측을 생성할 수 있다고 보고한다.[^p1] | 1저자 Yen Shin, 마지막 저자 Haewon McJeon |
| 2 | 2026 | [Different dimensions, different vulnerabilities: Intersectional energy poverty in India](https://doi.org/10.1016/j.erss.2026.104930) · Energy Research & Social Science | 인도의 가구 자료로 카스트, 농촌 거주, 교육, 소득 빈곤이 겹칠 때 전기와 취사 연료의 접근성·비용 부담·서비스 제공이 어떻게 달라지는지 분석했다. 불리함이 겹친 가구가 대체로 큰 결핍을 겪지만, 취사 연료의 금전 부담에서는 농촌의 수집 연료 사용 때문에 관계가 달라진다. 에너지 빈곤의 차원과 사회집단을 나누어 정책 대상을 정해야 한다는 결과다.[^p2] | 1저자 Mel George, 마지막 저자 Haewon McJeon |
| 3 | 2025 | [The impact of climate change on Korea’s agricultural sector under the national self-sufficiency policy](https://doi.org/10.1371/journal.pone.0313748) · PLOS ONE | 한국의 농업이 국내외 기후변화와 식량 자급정책에 어떻게 반응하는지 GCAM으로 비교했다. 세계의 생산 변화가 무역을 통해 미치는 영향이 국내 기후의 직접 영향보다 클 수 있다. 밀·콩의 자급정책은 생산자 수입을 늘리는 한편, 기후변화와 함께 소비자의 식료품 지출도 늘리는 것으로 나타났다.[^p3] | 1저자 Seulki Kim, 공저자 Jiyong Eom |
| 4 | 2026 | [Ambitious Co-scaling of Carbon Dioxide Removal and Decarbonization Delivers Better Climate Outcomes Than Strategies That Prioritize Efforts in One Domain](https://doi.org/10.1021/acs.est.5c17017) · Environmental Science & Technology | 탄소 제거와 배출 감축을 동시에 강하게 확대하는 경로를, 어느 한쪽에 우선순위를 두는 두 경로와 비교했다. 이상적인 가능 조건에서 기후적으로 달성할 수 있는 상한을 살핀 연구이며 현재 조건에서의 즉각적인 실행 가능성을 뜻하지 않는다. 동시 확대 경로는 이산화탄소 순배출 제로에 일찍 도달하고 온도 목표를 일시적으로 넘는 기간을 줄였지만, 지질학적 탄소 저장의 실현 가능성이 주요 제약이었다.[^p4] | 1저자 Jeffrey Dankwa Ampah, 마지막 저자 Haewon McJeon |
| 5 | 2024 | [Integrated assessment modeling of a zero-emissions global transportation sector](https://doi.org/10.1038/s41467-024-48424-9) · Nature Communications | 화석연료 퇴출 시점과 대체 기술 도입을 달리해 항공·해운을 포함한 세계 운송 부문의 탈탄소 경로를 비교했다. 전기화가 가장 크게 기여하며 바이오연료와 수소가 항공과 해운에서 특히 중요했다. 가장 강한 감축 시나리오는 세기 중반 운송 부문의 배출을 없애지만, 연료 수요와 공급 및 다른 에너지 부문까지 연결된 빠른 기술 전환이 필요하다.[^p5] | 1저자 Simone Speizer, 마지막 저자 Haewon McJeon |
| 6 | 2023 | [State-by-state energy-water-land-health impacts of the US net-zero emissions goal](https://doi.org/10.1016/j.egycc.2023.100117) · Energy and Climate Change | 미국 탄소중립의 네 경로가 주별 투자·좌초 자산, 물 취수, 대기오염 피해 비용, 산림에 미치는 영향을 함께 살폈다. 전환에 따른 주별 경제·지속가능성 효과가 국가 배출 감축에 대한 각 주의 감축 기여와 상관관계가 없을 수 있다는 결과다.[^p6] | 1저자 Yang Ou, 공저자 Haewon McJeon |
| 7 | 2025 | [Using deep learning to generate key variables in global mitigation scenarios](https://doi.org/10.1038/s41558-025-02352-8) · Nature Climate Change | 연구실 개별 설명에 따르면 기존 통합평가모형 시나리오를 분석한 뒤 딥러닝으로 합성 시나리오를 생성했다. 기존 자료의 변수 분포와 상관관계를 재현하고 발전 부문 변수의 물리적 일관성을 내부적으로 점검해, 기존 통합평가모형을 보완할 가능성을 제시했다.[^p7] | 1저자 Peijin Li, 공저자 Haewon McJeon |
| 8 | 2025 | [Heterogeneous pressure on croplands from land-based strategies to meet the 1.5 °C target](https://doi.org/10.1038/s41558-025-02294-1) · Nature Climate Change | 연구실 개별 설명에 따르면 통합평가와 세부 토지 이용 모형을 결합해 1.5°C 목표를 위한 기후 공약이 세계 토지 이용과 경작지에 미칠 영향을 평가했다. 감축 전략을 설계할 때 식량 안보와 환경의 다른 측면도 함께 고려해야 한다는 결과다.[^p8] | 1저자 Peichao Gao, 공저자 Haewon McJeon |

## 교수와 전문 분야

믹전 해원(Haewon C. McJeon)은 KAIST 녹색성장지속가능대학원 부교수다. 교수 소개는 2024년부터 이 직위에 있다고 적으며, 통합평가모형으로 저탄소·탄소중립·탄소 네거티브(이산화탄소 제거량이 배출량보다 큰 상태) 경로를 연구하고 한국과 아시아 개발도상국의 탈탄소 전략을 정량적으로 평가하는 교육을 한다고 설명한다.[^pi][^dept]

서울대학교에서 경제학 학사, 메릴랜드대학교에서 환경정책 석사·박사를 받았다. 이전에는 Pacific Northwest National Laboratory의 Joint Global Change Research Institute에서 Research Scientist(2012–2023), 메릴랜드대학교 Center for Global Sustainability에서 Joint Affiliate(2020–2024)로 일했다. GCAM 개발에 참여했고 미국 백악관의 2021년 Long-Term Strategy와 2016년 Mid-Century Strategy 보고서에서 통합평가모형 분석을 이끌었다. 전문 분야는 화석연료의 기후 영향, 탈탄소 기술, 불확실성 아래의 의사결정이다.[^pi]

그룹의 교수 명단에는 엄지용(Jiyong Eom)과 방문교수 Son H. Kim도 있다. 엄지용의 게시 연구 주제는 수요 측면, 에너지 경제학, 통합평가모형이다. Son H. Kim의 소개는 PNNL의 Joint Global Change Research Institute에서 휴직 중인 방문교수이며, GCAM의 모형 구조를 만든 연구자로서 인간 활동과 지구 시스템을 연결하는 통합평가모형을 개발·활용해 왔다고 설명한다. 매사추세츠공과대학교에서 원자력공학 박사를 받았다.[^members][^son]

## 응용 분야

연구실이 드는 협력 연구에는 프린스턴대학교와 한국의 에너지·산업 전환을 분석하는 Net-Zero Korea, 지구와 사회의 양방향 영향을 다루는 GHIM, 국가 및 세계의 저배출 경로를 다루는 NEWPATHWAYS가 있다. 기존 석탄발전소 부지를 활용하는 전환 방안을 분석하는 연구도 진행한다.[^models]

## 구성원

누리집 Members에 게시된 교수 3명, 박사후연구원 1명, 박사과정 4명, 석사과정 3명이다. 과정·직위와 연구 주제는 게시 표기를 따른다. Members는 엄지용을 Associate Professor로, Son H. Kim을 Visiting Professor로 교수 구획에 게시한다.[^members] “대표 논문 참여”는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

엄지용 개인 소개는 KAIST 경영대학 Associate Professor로 적는다. 연구 분야는 에너지·환경 경제 및 경영, 기후정책 분석을 위한 통합평가모형, 정보통신기술을 활용한 전력 수요 관리, 녹색 정보 시스템과 에너지 정보학이다. 연세대학교 화학공학 학사, KAIST 생명화학공학 석사, 스탠퍼드대학교 경영과학·공학 박사 학위를 받았다.[^eom]

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Jiyong Eom | Associate Professor | Demand-side · Energy Economics · IAM | 3 |
| Haewon C. McJeon | Associate Professor | Decarbonization · AI4IAM · IPCC Scenarios |  |
| Son H. Kim | Visiting Professor | Energy Systems · Model Architecture · IAM |  |
| Hyuntae Choi | Postdoctoral Researcher | Climate Policy · Econometrics · IAM |  |
| Ahmed SM Sobhy | PhD Candidate | Energy Demand · Transportation Modeling · IAM |  |
| Jiseok Ahn | PhD Candidate | Energy Systems · Energy & Environmental Policy · IAM |  |
| Jiwon Kwun | PhD Candidate | Hydrogen · Energy Security · IAM |  |
| Sungeun (Rachel) Kim | PhD Student | Iron & Steel · Decarbonization · IAM |  |
| Medina Mukhamedina | MS Student | Climate Policy · Energy Systems · IAM |  |
| Jiheun Ha | MS Student | Climate Policy · Subnational Strategies · IAM | 1 |
| Jin Lee | MS Student | Climate Risk · Carbon Neutrality · IAM |  |

## 졸업생 진로

Members의 Alumni 구획에 게시된 2명이다. 학위·과정의 약칭, 연도와 진로는 게시 표기를 따른다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jeongho Jo | MS, GBP (2024) | 기후솔루션, Researcher |
| Jungme Lee | MS, GGGS (2026) | KIA |

## 최근 5년 논문 목록

연구실 Publications의 논문 소개 제목과 소개글 게시 연도를 따른 목록이다. 완전한 저자·권호를 적은 서지 목록과는 형식이 다르다. 개별 글이 적은 DOI를 함께 두었으며, 기고문과 사전 공개본을 구분했다.[^pubs][^u46] 믹전 해원의 교수 소개가 밝힌 2024년 부교수 부임 전 항목이 섞여 있으며, 2023년과 2024년 초의 일부 소개글은 당시 KAIST 방문교수로 적는다.[^pi][^u4][^u9] 범위는 2021–2026년이다.

**2026**

- How Decarbonization Pathway Design Shapes Household Energy Burdens. [DOI](https://doi.org/10.1088/1748-9326/aeb55d)[^u51]
- Carbon dioxide removal consistent with climate pledges: a multi-model assessment of regional potential. [DOI](https://doi.org/10.1039/d6va00109b)[^u50]
- Different dimensions, different vulnerabilities: Intersectional energy poverty in India. [DOI](https://doi.org/10.1016/j.erss.2026.104930)[^u49]
- Ambitious co-scaling of carbon dioxide removal and decarbonization delivers better climate outcomes than strategies that prioritize efforts in one domain. [DOI](https://doi.org/10.1021/acs.est.5c17017)[^u48]
- Artificial Intelligence to Support Cross-Disciplinary Climate Change Research. 기고문. [DOI](https://doi.org/10.1038/s41558-026-02624-x)[^u46]
- ML-IAM v1.0: Emulating Integrated Assessment Models With Machine Learning. 사전 공개본. [DOI](https://doi.org/10.5194/egusphere-2025-5305)[^u46]
- Bridging China’s Climate Targets and Mitigation Capacity through Sectoral Policy Implementation. [DOI](https://doi.org/10.1021/acs.est.5c11232)[^u45]
- Korea’s “Tripling” Clean Energy Pledge: How Consistent Is It with Global Climate Pathways?. [DOI](https://doi.org/10.1016/j.isci.2026.115305)[^u44]
- 36 Solutions to Stabilize Earth’s Climate: New Perspective in Science Reflects on the 20-Year History of the Wedges. [DOI](https://doi.org/10.1126/science.aed5212)[^u43]
- Ensuring consistency between biogeochemical planetary boundaries. [DOI](https://doi.org/10.1038/s41893-026-01770-6)[^u42]

**2025**

- Transportation in net-zero emissions futures: Insights from the EMF-37 model intercomparison study. [연구실 게시 링크](https://doi.org/10.1016/j.egycc.2025.10021)[^u41]
- Bioenergy pathways within United States net-zero CO2 emissions scenarios in the Energy Modeling Forum 37 study. [DOI](https://doi.org/10.1016/j.egycc.2025.100209)[^u39]
- 제11차 전력수급기본계획과 대안적 전원 구성 시나리오의 통합평가에 관한 연구. 학술지 논문. [DOI](https://doi.org/10.15531/KSCCR.2025.16.3.459)[^u38]
- High-ambition climate action in all sectors can achieve a 60% greenhouse gas emissions reduction in Korea by 2035. 사전 공개본. [DOI](https://doi.org/10.31223/X50161)[^u38]
- Using Deep Learning to Generate Key Variables in Global Mitigation Scenarios. [DOI](https://doi.org/10.1038/s41558-025-02352-8)[^u34]
- Scaling carbon removal without delaying emission reductions. [DOI](https://doi.org/10.1038/s44359-025-00081-x)[^u35]
- Rate and growth limits for carbon capture and storage. [연구실 게시 링크](https://doi.org/10.1016/j.egycc.2025.100191)[^u31]
- The impact of climate change on Korea’s agricultural sector under the national self-sufficiency policy. [DOI](https://doi.org/10.1371/journal.pone.0313748)[^u32]
- A multi-model assessment of carbon neutrality pathways for Korea’s power sector[^u33]
- Global land system maps at 1 km resolution for 1.5 °C climate. [DOI](https://doi.org/10.1038/s41597-025-04991-0)[^u29]
- Policy implications of Net-Zero emissions: A multi-model analysis of United States emissions and energy system impacts. [DOI](https://doi.org/10.1016/j.egycc.2025.100191)[^u30]
- Meeting the global 1.5-degree goal could result in large-scale heterogeneous loss in croplands. [DOI](https://doi.org/10.1038/s41558-025-02294-1)[^u27]
- A Multi-Model Study to inform the United States’ 2035 NDC. [DOI](https://doi.org/10.1038/s41467-025-55858-2)[^u25]
- Large Ensemble Exploration of Global Energy Transitions Under National Emissions Pledges. [DOI](https://doi.org/10.1029/2024EF004754)[^u24]

**2024**

- KAIST Research Team Unveils Pathway to Carbon Neutrality for Korea’s Industrial Sector. [DOI](https://doi.org/10.1016/j.jclepro.2024.143749)[^u22]
- Carbon Management Technology Pathways for Reaching a U.S. Economy-Wide Net-Zero Emissions Goal. [DOI](https://doi.org/10.1016/j.egycc.2024.100154)[^u20]
- The impact of Regional Resources and Technology availability on Carbon Dioxide Removal Potential in the United States. [DOI](https://doi.org/10.1088/2753-3751/ad81fb)[^u21]
- High-ambition climate action in all sectors can achieve 65% greenhouse gas emissions reduction in the United States by 2035[^u17]
- The role of electrification and the power sector in U.S. carbon neutrality. [DOI](https://doi.org/10.1016/j.egycc.2024.100155)[^u19]
- Provincial-Scale Assessment of Direct Air Capture to Meet China’s Climate Neutrality Goal Under Limited Bioenergy Supply. [DOI](https://doi.org/10.1088/1748-9326/ad77e7)[^u16]
- Integrated assessment modeling of a zero-emissions global transportation sector. [DOI](https://doi.org/10.1038/s41467-024-48424-9)[^u15]
- The hydrogen economy can reduce costs of climate change mitigation by up to 22%. [DOI](https://doi.org/10.1016/j.oneear.2024.04.012)[^u14]
- Ambitious efforts on residual emissions can reduce CO2 removal and lower peak temperatures in a Net-Zero future. [DOI](https://doi.org/10.1088/1748-9326/ad456d)[^u13]
- Modeling direct air carbon capture and storage in a 1.5°C climate future using historical analogues. [DOI](https://doi.org/10.1073/pnas.2215679121)[^u12]
- Helping the climate by replacing liquefied natural gas with liquefied hydrogen or ammonia?. [DOI](https://doi.org/10.1088/1748-9326/ad376f)[^u11]
- Trade-Offs in Land-Based Carbon Removal Measures under 1.5°C and 2°C Futures. [DOI](https://doi.org/10.1038/s41467-024-46575-3)[^u10]
- Global Energy System Transitions. [DOI](https://doi.org/10.1086/728206)[^u8]
- Equity Implications of Net-Zero Emissions: A Multi-Model Analysis of Energy Expenditures Across Income Classes Under Economy-Wide Deep Decarbonization Policies. [DOI](https://doi.org/10.1016/j.egycc.2023.100118)[^u9]
- The role of bioenergy in Brazil’s low-carbon future. [DOI](https://doi.org/10.1016/j.egycc.2023.100123)[^u7]
- Power sector impacts of the Inflation Reduction Act of 2022. [DOI](https://doi.org/10.1088/1748-9326/ad0d3b)[^u5]
- An Integrated Assessment of the Leading Paths to Mitigate CO2 Emissions from the Organic Chemical and Plastics Industry. [DOI](https://doi.org/10.1021/acs.est.3c05202)[^u6]

**2023**

- Supply and Demand Drivers of Global Hydrogen Deployment in the Transition towards a Decarbonized Energy System. [DOI](https://doi.org/10.1021/acs.est.3c03751)[^u4]
- State-by-state energy-water-land-health impacts of the US net-zero emissions goal. [등록 DOI](https://doi.org/10.1016/j.egycc.2023.100117); [연구실 게시 링크](https://doi.org/10.1016/j.oneear.2023.08.019)[^u3]
- Global Stocktake: to limit global warming to 1.5°C, continued ratcheting of decarbonization is needed. [DOI](https://doi.org/10.1016/j.oneear.2023.08.019)[^u1]

## 수상과 선정

연구실 소식이 수상을 알린 2025년 항목이다. 상 이름은 같은 글의 영문·국문 표기를 함께 따른다.[^n40]

- 2025-08-22 · Ahmed SS Mahmoud가 KAIST Green Growth & Sustainability Workshop에서 수상했다. 같은 글 영문부는 Outstanding Paper Award, 국문 전재는 우수연구상으로 적는다.[^n40]
- 2025-08-29 · Ahmed SS Mahmoud가 KAIST Joint Academic Workshop의 Outstanding Presentation Award를 받았다.[^n40]

## 소식

2021-10-13–2026-10-13의 연구 성과·연구 출범·발표 초록 채택 소식이다. 날짜는 소개글 게시일이며, 학회 발표 초록 채택은 “채택”으로 표시했다.[^news][^n43] 믹전 해원의 2024년 부교수 부임 전 게시 항목도 포함한다.[^pi]

- 2026-06-30 · IAMC(Integrated Assessment Modeling Consortium, 통합평가모형 연구 협의체) 2026 연례회의 발표 초록 7편 채택. 구두발표는 Hyuntae Choi의 산업 경쟁력 약화와 무역 규제의 이중 부담을 해소할 수 있는 산업별 탄소중립 경로, Rachel Kim·Hanwoong Kim의 한국 에너지 시스템 변동성·회복력 분석을 위한 모형 결합, Jiheun Ha의 국내 17개 시도 기후행동의 배출 영향, Yen Shin·Jiheun Ha의 기계학습을 이용한 통합평가모형 대체 계산이다. 포스터는 Jin Lee의 원자력 이용이 국내총생산에 미치는 영향, Jiseok Ahn의 인공지능 데이터센터 성장에 따른 에너지·기후 영향, Jiwon Kwun의 연료·비료용 청정 암모니아 국제무역 모형화다.[^n43]
- 2025-08-29 · KAIST와 프린스턴대학교 Andlinger Center가 Net-Zero Korea 연구 출범을 알렸다. 구글·KAIST·프린스턴대학교의 지원으로 한국의 에너지·산업 전환을 분석하며, KAIST 측 연구책임자는 믹전 해원이다. 프린스턴의 상세 에너지 시스템 분석과 한국의 국제무역·공급망을 반영한 통합평가를 결합하려 한다.[^n37]
- 2025-04-08 · International Energy Workshop 2025 발표 초록 3편 채택. Jiseok Ahn은 한국의 재생에너지·원자력 동시 확대 목표, Ahmed S.S. Mahmoud는 자율주행차 도입의 에너지·배출 영향, Jiwon Kwun은 한국의 2050년 탄소중립 목표를 위한 수소 무역을 다룬다.[^n28]
- 2023-10-10 · One Earth 기고문 소개에서 메탄·불화가스 등 이산화탄소 이외 배출의 감축, 대기 중 이산화탄소 제거 확대, 산림 훼손 중단을 지구온난화 억제를 위한 세 갈래 노력으로 제시했다. 믹전 해원은 KAIST 방문교수이자 기고문 공저자로 소개되어 있다.[^n2]

## 연락과 위치

- 교수 이메일: hmcjeon@kaist.ac.kr.[^home]
- 위치: KAIST 대전 본원, 대전광역시 유성구 대학로 291.[^home]
[^home]: KAIST IAM Group, 연구실 첫 화면. <https://kaist-iam.github.io/group/index.html> (2026-11-11).
[^pi]: KAIST IAM Group, Haewon C. McJeon 교수 소개. <https://kaist-iam.github.io/group/hmcjeon.html> (2026-11-11).
[^dept]: KAIST 녹색성장지속가능대학원, 전체 교수진. <https://gggs.kaist.ac.kr/all-professor> (2026-11-11).
[^members]: KAIST IAM Group, Members. <https://kaist-iam.github.io/group/members.html> (2026-11-11).
[^models]: KAIST IAM Group, Models & Projects. <https://kaist-iam.github.io/group/models.html> (2026-11-11).
[^pubs]: KAIST IAM Group, Publications. <https://kaist-iam.github.io/group/publications.html> (2026-11-11).
[^news]: KAIST IAM Group, News. <https://kaist-iam.github.io/group/news.html> (2026-11-11).
[^son]: KAIST IAM Group, Son H. Kim 교수 소개. <https://kaist-iam.github.io/group/sonhkim.html> (2026-11-11).
[^eom]: KAIST IAM Group, Jiyong Eom 교수 소개. <https://kaist-iam.github.io/group/eomjiyoung.html> (2026-11-11).
[^n37]: KAIST IAM Group, Net-Zero Korea 출범 소식. <https://kaist-iam.github.io/group/posts_news/post37/index_post37.html> (2026-11-11).
[^n28]: KAIST IAM Group, International Energy Workshop 2025 초록 채택 소식. <https://kaist-iam.github.io/group/posts_news/post28/index_post28.html> (2026-11-11).
[^n2]: KAIST IAM Group, One Earth 기고문을 소개한 연구 성과 소식. <https://kaist-iam.github.io/group/posts_news/post2/index.html> (2026-11-11).
[^n40]: KAIST IAM Group, Ahmed SS Mahmoud 수상 소식. <https://kaist-iam.github.io/group/posts_news/post40/index_post40.html> (2026-11-11).
[^n43]: KAIST IAM Group, IAMC 2026 발표 초록 채택 소식. <https://kaist-iam.github.io/group/posts_news/post43/index_post43.html> (2026-11-11).
[^u51]: KAIST IAM Group, How Decarbonization Pathway Design Shapes Household Energy Burdens. <https://kaist-iam.github.io/group/posts_publications/potst51/index_post51.html> (2026-11-11).
[^u39]: KAIST IAM Group, Bioenergy pathways within United States net-zero CO2 emissions scenarios in the Energy Modeling Forum 37 study. <https://kaist-iam.github.io/group/posts_publications/potst39/index_post39.html> (2026-11-11).
[^u38]: KAIST IAM Group, High-ambition climate action in all sectors can achieve a 60% greenhouse gas emissions reduction in Korea by 2035. <https://kaist-iam.github.io/group/posts_publications/potst38/index_post38.html> (2026-11-11).
[^u20]: KAIST IAM Group, Carbon Management Technology Pathways for Reaching a U.S. Economy-Wide Net-Zero Emissions Goal. <https://kaist-iam.github.io/group/posts_publications/potst20/index_post20.html> (2026-11-11).
[^u21]: KAIST IAM Group, The impact of Regional Resources and Technology availability on Carbon Dioxide Removal Potential in the United States. <https://kaist-iam.github.io/group/posts_publications/potst21/index_post21.html> (2026-11-11).
[^u17]: KAIST IAM Group, High-ambition climate action in all sectors can achieve 65% greenhouse gas emissions reduction in the United States by 2035. <https://kaist-iam.github.io/group/posts_publications/potst17/index_post17.html> (2026-11-11).
[^u5]: KAIST IAM Group, Power sector impacts of the Inflation Reduction Act of 2022. <https://kaist-iam.github.io/group/posts_publications/potst5/index_post5.html> (2026-11-11).
[^u6]: KAIST IAM Group, An Integrated Assessment of the Leading Paths to Mitigate CO2 Emissions from the Organic Chemical and Plastics Industry. <https://kaist-iam.github.io/group/posts_publications/potst6/index_post6.html> (2026-11-11).
[^u3]: KAIST IAM Group, State-by-state energy-water-land-health impacts of the US net-zero emissions goal. <https://kaist-iam.github.io/group/posts_publications/potst3/index.html> (2026-11-11).
[^u1]: KAIST IAM Group, Global Stocktake: to limit global warming to 1.5°C, continued ratcheting of decarbonization is needed. <https://kaist-iam.github.io/group/posts_publications/potst1/index.html> (2026-11-11).
[^u34]: KAIST IAM Group, Using Deep Learning to Generate Key Variables in Global Mitigation Scenarios. <https://kaist-iam.github.io/group/posts_publications/potst34/index_post34.html> (2026-11-11).
[^u50]: KAIST IAM Group, Carbon dioxide removal consistent with climate pledges: a multi-model assessment of regional potential. <https://kaist-iam.github.io/group/posts_publications/potst50/index_post50.html> (2026-11-11).
[^u49]: KAIST IAM Group, Different dimensions, different vulnerabilities: Intersectional energy poverty in India. <https://kaist-iam.github.io/group/posts_publications/potst49/index_post49.html> (2026-11-11).
[^u48]: KAIST IAM Group, Ambitious co-scaling of carbon dioxide removal and decarbonization delivers better climate outcomes than strategies that prioritize efforts in one domain. <https://kaist-iam.github.io/group/posts_publications/potst48/index_post48.html> (2026-11-11).
[^u46]: KAIST IAM Group, AI로 기후위기 미래 예측한다. <https://kaist-iam.github.io/group/posts_publications/potst46/index_post46.html> (2026-11-11).
[^u45]: KAIST IAM Group, Bridging China’s Climate Targets and Mitigation Capacity through Sectoral Policy Implementation. <https://kaist-iam.github.io/group/posts_publications/potst45/index_post45.html> (2026-11-11).
[^u44]: KAIST IAM Group, Korea’s “Tripling” Clean Energy Pledge: How Consistent Is It with Global Climate Pathways?. <https://kaist-iam.github.io/group/posts_publications/potst44/index_post44.html> (2026-11-11).
[^u43]: KAIST IAM Group, 36 Solutions to Stabilize Earth’s Climate: New Perspective in Science Reflects on the 20-Year History of the Wedges. <https://kaist-iam.github.io/group/posts_publications/potst43/index_post43.html> (2026-11-11).
[^u42]: KAIST IAM Group, Ensuring consistency between biogeochemical planetary boundaries. <https://kaist-iam.github.io/group/posts_publications/potst42/index_post42.html> (2026-11-11).
[^u41]: KAIST IAM Group, Transportation in net-zero emissions futures: Insights from the EMF-37 model intercomparison study. <https://kaist-iam.github.io/group/posts_publications/potst41/index_post41.html> (2026-11-11).
[^u35]: KAIST IAM Group, Scaling carbon removal without delaying emission reductions. <https://kaist-iam.github.io/group/posts_publications/potst35/index_post35.html> (2026-11-11).
[^u31]: KAIST IAM Group, Rate and growth limits for carbon capture and storage. <https://kaist-iam.github.io/group/posts_publications/potst31/index_post31.html> (2026-11-11).
[^u32]: KAIST IAM Group, The impact of climate change on Korea’s agricultural sector under the national self-sufficiency policy. <https://kaist-iam.github.io/group/posts_publications/potst32/index_post32.html> (2026-11-11).
[^u33]: KAIST IAM Group, A multi-model assessment of carbon neutrality pathways for Korea’s power sector. <https://kaist-iam.github.io/group/posts_publications/potst33/index_post33.html> (2026-11-11).
[^u29]: KAIST IAM Group, Global land system maps at 1 km resolution for 1.5 °C climate. <https://kaist-iam.github.io/group/posts_publications/potst29/index_post29.html> (2026-11-11).
[^u30]: KAIST IAM Group, Policy implications of Net-Zero emissions: A multi-model analysis of United States emissions and energy system impacts. <https://kaist-iam.github.io/group/posts_publications/potst30/index_post30.html> (2026-11-11).
[^u27]: KAIST IAM Group, Meeting the global 1.5-degree goal could result in large-scale heterogeneous loss in croplands. <https://kaist-iam.github.io/group/posts_publications/potst27/index_post27.html> (2026-11-11).
[^u25]: KAIST IAM Group, A Multi-Model Study to inform the United States’ 2035 NDC. <https://kaist-iam.github.io/group/posts_publications/potst25/index_post25.html> (2026-11-11).
[^u24]: KAIST IAM Group, Large Ensemble Exploration of Global Energy Transitions Under National Emissions Pledges. <https://kaist-iam.github.io/group/posts_publications/potst24/index_post24.html> (2026-11-11).
[^u22]: KAIST IAM Group, KAIST Research Team Unveils Pathway to Carbon Neutrality for Korea’s Industrial Sector. <https://kaist-iam.github.io/group/posts_publications/potst22/index_post22.html> (2026-11-11).
[^u19]: KAIST IAM Group, The role of electrification and the power sector in U.S. carbon neutrality. <https://kaist-iam.github.io/group/posts_publications/potst19/index_post19.html> (2026-11-11).
[^u16]: KAIST IAM Group, Provincial-Scale Assessment of Direct Air Capture to Meet China’s Climate Neutrality Goal Under Limited Bioenergy Supply. <https://kaist-iam.github.io/group/posts_publications/potst16/index_post16.html> (2026-11-11).
[^u15]: KAIST IAM Group, Integrated assessment modeling of a zero-emissions global transportation sector. <https://kaist-iam.github.io/group/posts_publications/potst15/index_post15.html> (2026-11-11).
[^u14]: KAIST IAM Group, The hydrogen economy can reduce costs of climate change mitigation by up to 22%. <https://kaist-iam.github.io/group/posts_publications/potst14/index_post14.html> (2026-11-11).
[^u13]: KAIST IAM Group, Ambitious efforts on residual emissions can reduce CO2 removal and lower peak temperatures in a Net-Zero future. <https://kaist-iam.github.io/group/posts_publications/potst13/index_post13.html> (2026-11-11).
[^u12]: KAIST IAM Group, Modeling direct air carbon capture and storage in a 1.5°C climate future using historical analogues. <https://kaist-iam.github.io/group/posts_publications/potst12/index_post12.html> (2026-11-11).
[^u11]: KAIST IAM Group, Helping the climate by replacing liquefied natural gas with liquefied hydrogen or ammonia?. <https://kaist-iam.github.io/group/posts_publications/potst11/index_post11.html> (2026-11-11).
[^u10]: KAIST IAM Group, Trade-Offs in Land-Based Carbon Removal Measures under 1.5°C and 2°C Futures. <https://kaist-iam.github.io/group/posts_publications/potst10/index_post10.html> (2026-11-11).
[^u8]: KAIST IAM Group, Global Energy System Transitions. <https://kaist-iam.github.io/group/posts_publications/potst8/index_post8.html> (2026-11-11).
[^u9]: KAIST IAM Group, Equity Implications of Net-Zero Emissions: A Multi-Model Analysis of Energy Expenditures Across Income Classes Under Economy-Wide Deep Decarbonization Policies. <https://kaist-iam.github.io/group/posts_publications/potst9/index_post9.html> (2026-11-11).
[^u7]: KAIST IAM Group, The role of bioenergy in Brazil’s low-carbon future. <https://kaist-iam.github.io/group/posts_publications/potst7/index_post7.html> (2026-11-11).
[^u4]: KAIST IAM Group, Supply and Demand Drivers of Global Hydrogen Deployment in the Transition towards a Decarbonized Energy System. <https://kaist-iam.github.io/group/posts_publications/potst4/index.html> (2026-11-11).
[^p1]: Y. Shin 외, H. McJeon, EGUsphere (온라인 2026-01-09). <https://doi.org/10.5194/egusphere-2025-5305> 사전 공개본. 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5121721323,publication_year:2021-2026> (2026-11-11).
[^p2]: M. George 외, H. McJeon, Energy Research & Social Science (온라인 2026-08-21). <https://doi.org/10.1016/j.erss.2026.104930> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5121721323,publication_year:2021-2026> (2026-11-11).
[^p3]: S. Kim, J. Eom, Y. Zhang, S. Waldhoff, PLOS ONE 20, e0313748 (온라인 2025-01-24). <https://doi.org/10.1371/journal.pone.0313748> 초록 기준(출판사 논문 페이지). 초록 원문 <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0313748> (2026-11-11).
[^p4]: J. D. Ampah 외, H. McJeon, Environmental Science & Technology (2026). <https://doi.org/10.1021/acs.est.5c17017> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1021/acs.est.5c17017> (2026-11-11).
[^p5]: S. Speizer 외, H. McJeon, Nature Communications (2024). <https://doi.org/10.1038/s41467-024-48424-9> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1038/s41467-024-48424-9> (2026-11-11).
[^p6]: Y. Ou 외, D. H. Loughlin, Energy and Climate Change (2023). <https://doi.org/10.1016/j.egycc.2023.100117> 초록 기준(Semantic Scholar 등록 초록). 초록 원문 <https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.egycc.2023.100117?fields=title,abstract,venue,year,externalIds,publicationDate> (2026-11-11).
[^p7]: P. Li 외, Y. Ou, Nature Climate Change (2025). <https://doi.org/10.1038/s41558-025-02352-8> 연구실 개별 설명 기준. 설명 원문 <https://kaist-iam.github.io/group/posts_publications/potst34/index_post34.html> (2026-11-11).
[^p8]: P. Gao 외, C. Song, Nature Climate Change (2025). <https://doi.org/10.1038/s41558-025-02294-1> 연구실 개별 설명 기준. 설명 원문 <https://kaist-iam.github.io/group/posts_publications/potst27/index_post27.html> (2026-11-11).

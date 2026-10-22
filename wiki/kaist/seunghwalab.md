# 지능형 설계 및 제조 연구실 (AiM⁴ Lab, Laboratory for AI-powered Modeling in Mechanics, Materials, and Manufacturing)

**KAIST 기계공학과 · 유승화 교수**

- 분야: AI 기반 역설계와 최적화, 물리정보 기계학습과 역문제, 대형 언어 모델 다중 에이전트, AI 기반 제조 공정(사출성형·원자층 증착 챔버·선박 강판 가공), 다중 스케일 재료 모델링과 복합재 균질화, 구조 모니터링·열전·신축 복합재 응용
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 과학·공학 AI[^home][^research][^p3], 대형 언어 모델[^research][^p5], 스마트 제조[^research][^apps], 메타물질·메타광학[^apps][^p4], 열전[^apps][^p3], 유연·신축 전자[^apps][^p7], 3D 프린팅[^research][^pubs]
- 홈페이지: <https://sites.google.com/site/seunghwalab>
- 근거와 출처: [지능형 설계 및 제조 연구실 근거 페이지](seunghwalab-sources.md)

> 물리 법칙과 분야 지식을 인공지능과 결합해 기계·재료·제조 분야의 모델링, 설계, 최적화 방법을 만드는 기계공학과 연구실이다. 적은 데이터로 성능을 예측하고 원하는 성능에서 거꾸로 구조와 공정 조건을 찾는 방법으로 제조, 모빌리티, 전자, 에너지 분야의 공학 문제를 푼다고 소개한다.[^home]

## 무엇을 연구하나

연구실은 KAIST 기계공학과 유승화 교수의 연구실이다. 누리집 이름은 AiM⁴ Lab(Laboratory for AI-powered Modeling in Mechanics, Materials, and Manufacturing)이고 국문 이름은 「지능형 설계 및 제조 연구실」이며, 기계공학과 교수진 목록도 연구실을 「AiM⁴ Lab - 지능형 설계 및 제조 연구실」로 적는다. 기계공학과 연구분야 안내의 소재/역학/제조 쪽은 「멀티스케일 역학 및 재료 모델링 연구실」이라는 이름으로 적는다.[^home][^melist][^meres] 첫 화면 소개 글은 연구실이 물리 및 도메인 지식과 AI를 결합해 기계·재료·제조 분야의 모델링, 설계, 최적화 방법을 개발하고, 데이터 효율적인 예측과 역설계(원하는 성능을 먼저 정하고 그 성능을 내는 구조나 조건을 거꾸로 찾는 설계)로 제조, 모빌리티, 전자, 에너지 분야의 공학 문제를 해결한다고 적는다.[^home]

첫 화면은 연구 방향을 세 가지로 든다. AI 대리모델(시간이 오래 걸리는 시뮬레이션이나 실험의 결과를 빠르게 내도록 학습한 모델)과 생성형 AI를 활용한 예측·역설계·최적화, 물리 법칙과 다물리 모델링(열·전기·힘처럼 서로 다른 물리 현상을 함께 계산하는 모델링)을 결합한 데이터 효율적 AI, 그리고 도메인 전문지식과 물리적 추론, 인간-AI 협력을 통합해 공학 문제를 푸는 지식 기반 에이전트 AI(Knowledge-Guided Agentic AI)다.[^home] Research 페이지는 이 지식 기반 에이전트 AI를 연구실의 비전으로 적고, 목표로 물리 원리·계산 모델·데이터 학습을 통합한 데이터 효율적 예측과 역설계 방법의 개발, 그리고 연구자와 엔지니어가 제조·모빌리티·전자·에너지 분야에서 추론하고 탐색하고 결정을 내리도록 돕는 AI 에이전트와 설계 도구의 개발을 든다.[^research]

누리집 Publications by Methods 페이지는 국제 학술지 목록의 228편(투고 중인 논문 포함)을 방법에 따라 다섯 묶음으로 나눈다. 물리정보 학습과 역문제 식별 13편, 예측 학습과 센싱 및 불확실성 28편, AI 기반 설계와 최적화 44편, 대규모 언어모델과 에이전트 자동화 8편, 물리 기반 모델링과 실험 135편이다.[^methods] Publications by Application Areas 페이지는 같은 논문을 응용 분야에 따라 구조형 재료와 구조용 복합재 60편, 제조 공정과 공학 시스템 37편, 에너지와 열 및 환경 시스템 21편, 바이오메디컬과 소프트 및 웨어러블 기술 37편, 나노재료와 기초 물리 73편으로 나눈다.[^apps] 기계공학과 교수진 목록은 교수의 연구분야를 Multiscale mechanics and material simulation, Machine learning based design of structural materials로 적는다.[^melist] 기계공학과 연구분야 안내는 소재/역학/제조 분야에서 이 연구실의 연구주제를 여러 길이·시간 단위에 걸친 역학·열 물성의 이론·계산 모델링과 원하는 역학 성질을 내는 재료·구조 설계로 적고, 헬스케어/나노/광학 분야에서는 Multiscale modeling, Nanomechanics로 적는다.[^meres]

## 주요 연구 주제

### 1. AI 기반 설계 전략과 역설계

Research 페이지는 기계학습이 기존 재료 이론으로 다 설명하지 못하는 복잡한 물리 과정과 메커니즘을 예측해 새 재료의 발견과 생산을 앞당겼지만, 복잡한 기계학습 모델이 많아지면서 어떤 알고리즘이 알맞은지가 중요한 물음이 되었다고 적는다. 연구실은 설계 문제의 성격에 맞춰 알맞은 모델을 전략적으로 고르는 기준을 제시하는 것을 이 갈래의 목표로 든다.[^research] Publications by Methods 페이지의 AI 기반 설계와 최적화 묶음(44편)은 생성모델, 베이지안 최적화(지금까지 시험한 결과로 성능을 예측하는 확률 모델을 세워 다음에 시험할 조건을 골라 나가는 최적화 방법), 강화학습(시행착오를 거치며 보상이 커지는 행동을 배우는 기계학습 방법), 학습형 대리모델로 재료 구조와 공정 조건을 탐색하는 연구다. 이 묶음의 소개 글은 베이지안 최적화로 복합재의 설계변수와 성능 사이의 관계를 탐색하는 데서 출발해 다목적 설계와 나노격자(나노미터 굵기의 기둥을 격자로 엮은 구조) 설계로 넓혔고, 생성모델과 강화학습으로 비선형 응답과 능동적인 형상 변화를 내는 구조를 역설계한다고 적는다.[^methods]

대표 논문 1은 재료 설계에 쓰는 기계학습 알고리즘을 정리한 리뷰로, 설계 문제를 학습 데이터의 양과 설계 공간의 크기에 따라 네 가지로 나누고 경우마다 알맞은 대리모델과 설계 방법을 정리했다.[^p1] 대표 논문 2는 열을 받으면 스스로 모양이 바뀌는 복합재의 재료 배치를 강화학습으로 정하고, 4D 프린팅(자극을 받으면 시간이 지나며 모양이 바뀌도록 설계한 물체를 3D 프린터로 만드는 방법)한 시편으로 확인했다.[^p2] 최근 논문 목록에는 확산 모델(잡음에서 출발해 잡음을 단계적으로 걷어 내며 새 데이터를 만드는 생성 모델)로 다중 물리 제약을 만족하는 진주층 모사 복합재를 역설계한 연구(2026)와 비선형 거동을 목표로 미세구조를 역설계한 연구(2026), 생성형 AI와 능동학습(모델 학습에 쓸모 있는 데이터를 골라 추가로 얻어 가며 학습하는 방식)으로 나노 구조재의 비강성(무게에 대한 강성의 비. 강성은 힘을 받을 때 변형에 버티는 정도)을 높인 연구(게재 승인), 베이지안 최적화로 탄소 나노격자를 설계한 공동 연구(2025)가 있다.[^pubs] 대표 논문 1, 2.[^p1][^p2]

### 2. 물리정보 기계학습과 역문제

Research 페이지는 제조의 실제 설계 문제가 적고 비싼 데이터와 복잡한 물리적 제약을 안고 있어 데이터만으로 학습한 AI 모델을 믿기 어렵다고 적는다. 물리정보 기계학습(PIML, Physics-Informed Machine Learning)은 지배 방정식(현상을 나타내는 기본 물리 법칙의 식)을 학습 과정에 넣어 데이터가 적어도 물리적으로 일관된 모델을 만든다. 연구실은 최근 데이터가 극히 적은 조건에서 재료 물성을 알아내는 데 집중하며, 이를 AI 기반 설계를 위한 대량 재료 물성 평가와 선별에 쓰려 한다고 적는다.[^research] Publications by Methods 페이지의 물리정보 학습과 역문제 식별 묶음(13편) 소개 글은 물리법칙과 미분가능 계산을 결합해 초탄성(큰 변형을 받은 뒤에도 힘을 없애면 원래 모양으로 돌아오는 성질) 구성모델(재료에 걸린 힘과 변형 사이의 관계를 나타내는 식)과 온도에 따라 달라지는 물성을 식별하고, 이를 소성 구성법칙과 불확실성을 고려한 역추정으로 넓히고 있다고 적는다.[^methods]

대표 논문 3은 물리정보 신경망(PINN, 물리 법칙의 식을 학습 목표에 넣어 학습하는 신경망)과 신경 연산자(입력 조건 전체를 출력 해 전체로 옮기는 관계를 학습하는 신경망)를 결합해, 적은 온도·전압 측정값에서 열전 재료(온도 차이로 전기를 만드는 재료)의 온도 의존 물성을 알아냈다.[^p3] 대표 논문 4는 두 가지 안정된 모양을 갖는 키리가미(판에 칼집을 내어 모양과 변형을 만드는 기법) 메타물질(재료보다 작은 인공 구조를 배열해 자연 물질에 없는 성질을 내는 물질)의 에너지 곡선을, 미리 모은 학습 데이터 없이 물리정보 신경망으로 예측하고 거꾸로 설계했다.[^p4] 최근 논문 목록에는 극히 적은 데이터에서 초탄성 구성모델을 찾아낸 연구(2025), 변형률의 기울기에 따라 전기 분극이 생기는 현상인 플렉소일렉트릭 효과의 정문제와 역문제(측정 결과에서 원인이나 물성을 거꾸로 알아내는 문제)를 푸는 계산 틀(2026), 펼쳐지는 순서를 조절하는 종이접기 메타물질 연구(2025), 도로 포장층 역해석에서 물리 제약을 부과하는 두 방식을 비교한 연구(게재 승인)가 있다.[^pubs] 대표 논문 3, 4.[^p3][^p4]

### 3. 대형 언어 모델과 다중 에이전트

Research 페이지는 대형 언어 모델(LLM, 많은 글을 학습해 글을 이해하고 만들어 내는 큰 AI 모델)이 자연어로 된 질문을 설계 작업, 시뮬레이션, 최적화 작업 흐름으로 옮겨 역설계를 사람이 다루기 쉽게 만든다고 적는다. 검색 증강 생성(답을 만들기 전에 관련 문서를 찾아 참고하게 하는 방법)과 다중 에이전트 시스템(역할을 나눈 여러 AI가 함께 일하는 구조)을 결합하면 AI 기반 제조 환경에서 접근성, 추론, 협업이 나아진다고 적고, 이중 페로브스카이트 소재 탐색용 다중 에이전트 연구(심사 중)도 함께 든다.[^research] Publications by Methods 페이지의 대규모 언어모델과 에이전트 자동화 묶음(8편) 소개 글은 사출성형(녹인 플라스틱을 틀에 밀어 넣어 굳혀 부품을 만드는 공정) 지식 전달과 오류를 스스로 고치는 물리 시뮬레이션에서 출발해 구성모델 보정과 분자동역학(원자와 분자의 움직임을 운동 방정식으로 계산하는 시뮬레이션) 작업 자동화로 넓히고 있다고 적는다.[^methods]

대표 논문 5는 모호하거나 빠진 것이 있는 자연어 요청을 받아 여러 에이전트가 입력 확인, 코드 생성, 오류 진단, 여러 언어의 설명을 나눠 맡아 검증된 시뮬레이션과 설명 보고서를 만드는 틀(MCP-SIM)을 내놓았다.[^p5] 최근 논문 목록에는 사출성형 산업의 지식 전달을 돕는 다중 에이전트 LLM 틀(IM-Chat, 2025)이 있고,[^pubs] 과제 목록에는 첨단 제조산업 생산성 향상을 위한 특화형 거대언어모델 적용 기술 개발(2025.09.-2028.08., 연구책임)이 있다.[^research] 대표 논문 5.[^p5]

### 4. AI 기반 제조 공정

Research 페이지는 AI 기반 제조 연구로 네 가지를 든다. 반도체 산업에 널리 쓰이는 원자층 증착(ALD, 원료 기체를 번갈아 흘려 원자 한 층씩 막을 쌓는 공정) 코팅 챔버는 전산유체역학(유체의 흐름을 컴퓨터로 계산하는 방법) 시뮬레이션과 AI를 결합해 코팅의 균일도를 높이는 설계를 연구했다. 사출성형은 AI 기반 시뮬레이션과 실험 데이터로 공정을 최적화한다. 조선 산업에서 가열선으로 강판을 굽히는 작업은 숙련 기술자의 경험과 많은 시행착오에 기대어 왔는데, 연구실은 원하는 변형을 얻는 최적의 가열선 무늬를 정하는 AI 알고리즘을 개발해 생산성을 크게 높였다고 적는다. 열 관리 시스템은 데이터와 AI 모델링을 결합해 모델링하고 최적화한다.[^research] Publications by Application Areas 페이지의 제조 공정과 공학 시스템 묶음(37편) 소개 글은 사출성형 연구가 공정 조건의 다목적 최적화에서 출발해 다중 충실도 데이터(정확도와 비용이 서로 다른 여러 종류의 데이터) 활용, 적응형 생산 조건 결정, 데이터 주권을 지키는 품질 예측과 지식 전달로 이어졌다고 적는다.[^apps]

대표 논문 6은 원자층 증착 챔버 안 가스 흐름을 고르게 하도록, 적은 전산유체역학 데이터로 학습한 신경망 대리모델과 입자 군집 최적화(여러 후보 해가 서로의 결과를 참고하며 함께 최적점을 찾는 방법)로 다공성 배플(흐름을 고르게 나누도록 구멍을 뚫은 판)의 구멍 배치를 정하고 실험으로 확인했다.[^p6] 최근 논문 목록에는 심층 강화학습으로 사출성형 공정 변수를 정한 연구(2026), 연합학습(데이터를 한곳에 모으지 않고 각자 학습한 모델만 모아 합치는 학습 방법)으로 사출성형 품질을 예측한 연구(게재 승인), 확산 모델로 사출성형 생산 조건을 추론한 연구(2025), 조선용 강판 가열 무늬를 신경망과 최적화로 역설계한 연구(2025), 차량 테일게이트의 보강 리브 배치를 베이지안 최적화로 정한 연구(2025)가 있다.[^pubs] 대표 논문 6.[^p6]

### 5. 다중 스케일·다중 물리 모델링

Research 페이지는 연구실이 여러 크기 단위에서 재료의 이론·계산 모델을 만든다고 적는다. 원자 시뮬레이션으로 재료의 역학 거동을 이해하고 그 결과를 더 큰 단위의 연속체(물체를 빈틈없이 이어진 덩어리로 보는 관점) 모델과 복합재 모델의 입력으로 쓰며, 다중 물리 시뮬레이션 틀을 만들어 기존 유한요소 해석(물체를 작은 조각으로 나눠 각 조각의 방정식을 이어 풀어 변형과 힘을 계산하는 방법) 코드에 넣는다. 제조 품질을 높이려고 3D 프린팅 공정과 사출성형의 계산 모델링 도구를 쓰고, 피로 수명(되풀이되는 하중을 받는 구조가 부서지기까지 견디는 횟수) 예측 모델을 상용 소프트웨어에 넣어 AI 알고리즘과 함께 구조의 내구성을 높인다고 적는다.[^research] Publications by Methods 페이지의 물리 기반 모델링과 실험 묶음(135편) 소개 글은 원자 시뮬레이션, 미시역학, 연속체 해석과 실험으로 서로 다른 크기 단위의 구조와 물성을 연결해 왔다고 적고, 전위(결정 속 원자 배열이 어긋난 선 모양 결함) 핵생성, 복합재 균질화, 충격 파괴와 나노 단위 측정 연구를 든다.[^methods] Publications by Application Areas 페이지는 생체모사 판상 복합재의 탄성과 파괴 메커니즘 분석에서 출발해 안정 상태와 에너지 지형 자체를 설계하는 프로그래머블 재료로 넓혀 온 구조형 재료·복합재 묶음(60편, 프로그래머블 메타물질과 생체모사 복합재 포함)과, 전위 핵생성과 나노선의 소성 변형에서 출발해 복합 계면의 결함 구조와 원자 단위 변형률을 연구해 왔고 최근에는 계면과 쌍정(결정의 두 부분이 경계면을 사이에 두고 서로 거울 대칭으로 배열된 구조)의 형성 경로를 다루는 나노재료·기초 물리 묶음(73편)을 둔다.[^apps]

대표 논문 7은 액체 금속 방울을 탄성 고분자에 넣은 복합재의 탄성·열·유전 성질을 평균장 균질화(섞인 재료를 하나의 고른 재료로 보고 평균적인 유효 물성을 계산하는 방법)의 여러 방식으로 계산하고, 방울 표면의 산화막까지 포함한 코어-셸 구조를 정확히 다루는 방식을 제시했다.[^p7] 최근 논문 목록에는 신축성 유기 반도체용 고분자 혼합물의 조대입자 모델링(여러 원자를 한 입자로 묶어 계산량을 줄인 분자 모델링, 2026), 짧은 섬유 강화 복합재의 미시역학 균질화 리뷰(2024), 기계발광(힘을 받으면 빛을 내는 현상) 복합재를 광중합 3D 프린팅과 기계학습으로 만든 연구(2024), 나노 단위 마찰로 강유전체 분역(전기 분극 방향이 같은 영역)을 영상화한 공동 연구(2026)가 있다.[^pubs] 대표 논문 7.[^p7]

### 6. 구조 모니터링·에너지·웨어러블 응용

Publications by Methods 페이지의 예측 학습과 센싱 및 불확실성 묶음(28편) 소개 글은 미세구조에서 응력-변형률 응답과 공간 분포를 예측하는 연구에서 출발해, 새로운 형상·잡음·측정 해상도에 대한 일반화와 예측 불확실성의 구분, 최근에는 어디를 측정해야 하는지까지 다룬다고 적는다.[^methods] Publications by Application Areas 페이지의 에너지와 열 및 환경 시스템 묶음(21편)은 열전 연구로 계면을 고려한 유효 물성 예측, 온도 의존 물성을 반영한 열전 발전기 최적화, 성능 지표의 물리적 해석과 측정 기반 물성 역추정을 다루고 파동 에너지 수확, 배터리 열 관리, 탄소 포집·전환도 연구한다고 적는다. 바이오메디컬과 소프트 및 웨어러블 기술 묶음(37편)은 신축성 복합재의 전기·기계적 거동을 분석해 센서와 섬유형 소자의 설계를 돕고, 생체 신호와 영상을 해석하는 AI를 함께 연구한다고 적는다.[^apps]

대표 논문 8은 늘이면 옆으로도 넓어지는 오그제틱 구조의 변형률 분포를 유한요소 데이터로 학습한 신경망으로 예측하고, 기계발광 입자를 넣어 3D 프린팅한 시편으로 변형이 몰리는 곳을 확인했다.[^p8] 최근 논문 목록에는 베이지안 신경망으로 불확실성을 나눠 보는 실시간 구조 건전성 모니터링(구조물에 센서를 달아 손상을 계속 살피는 기술, 2026), 푸리에 신경 연산자로 형상·잡음·해상도 변화에 흔들리지 않게 한 초음파 탄성 영상(2026), 온도 의존 물성을 반영한 분절형 열전 발전기의 기계학습 최적화(2024), 공랭식 배터리 열 관리 시스템의 다목적 베이지안 최적화(2025), 에너지 수확용 경사 굴절률 포논 결정(탄성파의 진행을 조절하도록 구조를 주기적으로 배열한 재료)의 최적화(2026)가 있다.[^pubs] 대표 논문 8.[^p8]

## 대표 논문

유승화 교수가 마지막 저자인 2021–2026년 학술지 논문 가운데 연구 갈래마다 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2023 | [Machine learning-based inverse design methods considering data characteristics and design space size in materials design and manufacturing: a review](https://doi.org/10.1039/D3MH00039G) · Materials Horizons | 기계학습은 기존 재료 이론으로 다 설명하지 못하는 복잡한 물리 과정을 예측해 새 재료의 발견과 생산을 앞당겼지만, 모델이 많아지면서 어떤 알고리즘을 쓸지가 문제가 되었다. 이 리뷰는 재료 설계에 흔히 쓰는 기계학습 알고리즘을 정리하고, 설계 문제의 성격에 맞는 모델을 고르는 기준을 제시한다. 설계 문제를 네 가지로 나눈다. (i) 학습 데이터가 설계 공간의 경향을 담을 만큼 넉넉한 내삽 문제, (ii) 처음 데이터만으로는 다 탐색할 수 없는 넓은 설계 공간의 외삽 문제, (iii) 정확한 작은 데이터와 근사적인 큰 데이터가 함께 있는 다중 충실도 문제, (iv) 작은 데이터만 있는 문제다. 경우마다 성공적인 대리모델과 설계 방법을 관련 문헌과 함께 다루며, 적층 제조(재료를 한 층씩 쌓아 물체를 만드는 방법)의 등장으로 관심이 커진 복잡한 복합재 구조의 역설계를 주로 다룬다.[^p1] | 1저자 J. Lee, 마지막·교신 저자 유승화 (7명) |
| 2 | 2026 | [Inverse design of thermally active composite via policy-transferred reinforcement learning](https://doi.org/10.1039/D6MH00239K) · Materials Horizons | 바깥 자극을 받으면 스스로 모양을 바꾸는 능동 복합재는 소프트 로봇, 생체의료 기기, 지능형 구조에 새 가능성을 열지만, 여러 재료를 쓰는 3D 프린팅에서는 재료 배치의 경우의 수가 너무 많아 역설계를 계산하기 어렵다. 이 연구는 열에 반응하는 능동 복합재의 역설계를 차례로 결정을 내리는 문제로 바꾼 강화학습 틀을 내놓았다. 4 × 24 격자를 열 단위 결정 24개로 나눠, 목표 변형 궤적과의 차이를 줄이도록 재료를 정한다. 먼저 목표 하나에 대한 설계를 보이고, 여러 목표로 목표 조건부 정책을 학습해 다양한 모양을 빠르게 설계했으며, 이 정책을 옮겨 써서 목표 하나의 최적화도 앞당겼다. 같은 종료 조건에서 유전 알고리즘 등과 필요한 시료 수·계산 횟수를 견주었고, 회색조 디지털 광 처리 방식으로 4D 프린팅한 시편과 KAIST 로고 모양 같은 복잡한 궤적으로 실험 확인을 해, 적은 시료와 계산 횟수로 목표 정확도(평균 제곱근 오차 0.1 이하)에 이르렀다.[^p2] | 1저자 S. Lee, 마지막·교신 저자 유승화 (6명) |
| 3 | 2025 | [Physics-informed neural operators for generalizable and label-free inference of temperature-dependent thermoelectric properties](https://doi.org/10.1038/s41524-025-01769-1) · npj Computational Materials | 열전도도와 제베크 계수(재료 양 끝의 온도 차이에 대한 전압의 비) 같은 열전 물성이 온도에 따라 어떻게 바뀌는지 정확히 알아야 열전 소자를 모델링하고 설계할 수 있다. 그러나 물성이 온도에 비선형으로 바뀌고 열과 전기의 이동이 서로 얽혀 있어, 측정값이 드문드문할 때는 정방향 계산과 물성 역추정이 모두 어렵다. 이 연구는 물리정보 신경망(PINN)과 물리정보 신경 연산자(PINO)를 결합한 틀을 내놓았다. PINN은 지배 방정식을 손실 함수(학습이 줄여 나가는 오차의 척도)에 넣어 물리량의 공간 분포를 복원하고 물성을 추론하며, PINO는 다시 학습하지 않고도 여러 재료에 일반화된다. p형 재료 20종의 시뮬레이션 데이터로 학습하고 처음 보는 재료 60종으로 시험한 결과, PINO는 드문드문한 온도·전압 데이터만으로 열전 물성을 정확히 추론했다. 저자들은 이 틀이 열전 재료의 대량 선별과 역설계에 쓰일 수 있다고 적는다.[^p3] | 1저자 H. Moon, 마지막·교신 저자 유승화 (교신 표시 2명 중 1명, 5명) |
| 4 | 2026 | [Data-free physics-informed inverse programming of bistable kirigami energy landscapes](https://doi.org/10.1039/D6MH00630B) · Materials Horizons | 평면 판에 칼집을 낸 키리가미 메타물질은 형상에 따라 달라지는 에너지 곡선 덕분에 두 가지 안정된 모양을 가질 수 있다. 정해진 에너지 장벽과 목표 변형 상태를 갖도록 설계하는 일이 프로그래밍 가능한 역학 기능에 중요하다. 이 연구는 미리 모은 정답 데이터 없이, 평형 조건·에너지 식·기하학적 적합 조건을 학습 목표에 직접 넣은 물리정보 신경망으로 에너지 곡선의 예측과 역설계를 한 틀에서 해냈다. 예측에서는 결정계수(예측이 실제 값의 변화를 얼마나 설명하는지 나타내는 지표)가 0.99를 넘고 장벽 오차가 0.1% 미만이었고, 전체 에너지 곡선을 주면 장벽 오차 5% 미만으로 형상을 찾았다. 목표 장벽과 에너지가 0인 안정 상태만 주는 경우에도 전체 에너지 곡선을 스스로 추론해 평균 장벽 오차 0.4%를 얻었다. 유한요소 해석과 3D 프린팅 시제품 실험으로 장벽 순서가 지켜짐을 확인했고, 장벽이 다른 단위 칸을 이어 붙여 당길 때 장벽이 낮은 칸부터 차례로 변하는 순차 작동을 보였다. 저자들은 펼침 구조, 소프트 로봇 구동기, 충격 완화 장치에 쓰일 수 있다고 적는다.[^p4] | 1저자 S. Kang, 마지막·교신 저자 유승화 (교신 표시 2명 중 1명, 4명) |
| 5 | 2026 | [A self-correcting multi-agent LLM framework for language-based physics simulation and explanation](https://doi.org/10.1038/s44387-025-00057-z) · npj Artificial Intelligence | 물리 시뮬레이션을 만들려면 보통 수치 해석 프로그램과 지배 방정식에 대한 전문 지식이 필요하다. 대형 언어 모델로 자연어만으로 시뮬레이션을 만들 길이 열렸지만, 요청이 모호하거나 빠진 것이 있거나 여러 언어로 되어 있으면 자주 실패한다. 이 연구는 불완전한 요청을 검증된 시뮬레이션과 설명 보고서로 바꾸는 스스로 고치는 다중 에이전트 틀 MCP-SIM을 내놓았다. 입력 확인, 코드 생성, 오류 진단, 여러 언어의 설명을 에이전트들이 나눠 맡고 기억을 이어 가며, 한 번에 코드를 만드는 대신 계획, 실행, 되돌아보기, 고치기를 되풀이한다. 난도가 점점 높아지는 12개 과제에서 모든 시험 사례를 풀었고, 이 연구가 정한 지표로 GPT 기반 방법과 사람이 개입하는 방법 대비 수렴 효율이 나아졌다. 각 시뮬레이션의 물리적 논리를 사용자의 언어로 설명하는 보고서도 만든다. 저자들은 시험 범위 밖의 전문 분야에서의 성능은 앞으로 확인할 과제로 남긴다.[^p5] | 1저자 D. Park, 마지막·교신 저자 유승화 (3명) |
| 6 | 2026 | [Optimizing chamber systems for deposition processes in the semiconductor industry with deep learning framework: tackling small simulation datasets](https://doi.org/10.1007/s10845-025-02584-7) · Journal of Intelligent Manufacturing | 원자층 증착은 반도체 산업에서 아주 얇고 정밀한 막을 입히는 데 중요하지만, 복잡한 챔버 안에서 가스가 고르지 않게 흐르면 막이 고르지 않게 입혀진다. 이 연구는 전산유체역학 계산, 자기 정규화 신경망(층마다 출력의 분포가 스스로 일정하게 유지되도록 만든 신경망), 입자 군집 최적화를 결합해 수평형 원자층 증착 챔버의 다공성 배플 구멍 배치를 최적화하는 AI 틀을 내놓았다. 자기 정규화 신경망은 전산유체역학 학습 데이터가 적어도 과적합(학습 데이터에만 맞춰져 새 데이터에서 틀리는 현상)을 줄이고 일반화를 높이며, 대리모델로서 흐름 균일도를 빠르게 예측해 계산 비용을 줄인다. 이를 최적화 반복 안에 넣어 최적 배플 설계를 찾았고, 실험에서 기준 챔버 대비 흐름 균일도가 85.9% 개선되고 산화알루미늄 막 두께 균일도가 50% 높아졌다.[^p6] | 1저자 D. Park, 마지막·교신 저자 유승화 (교신 표시 2명 중 1명, 5명) |
| 7 | 2024 | [Mean-field homogenization of liquid metal elastomer composites: comparative study and exact dilute solution of core-shell inclusion](https://doi.org/10.1088/1361-648X/ad765e) · Journal of Physics: Condensed Matter | 액체 금속을 탄성 고분자에 넣은 복합재는 늘어나는 성질을 해치지 않으면서 고분자보다 높은 유전율(전기장 안에서 물질이 전기를 저장하는 정도)과 열전도도를 보여 신축성 기능 소자에 쓰일 수 있다. 이런 복합재의 유효 물성을 구하는 데는 에셸비 개재물 해(재료 속에 박힌 알갱이 둘레의 응력과 변형을 구한 해)에 바탕을 둔 미시역학 균질화가 쓸모 있지만, 상들 사이의 탄성 상수 차이가 극단적이고 특히 나노 크기 알갱이 둘레에 단단한 금속 산화막이 생기면 알맞지 않은 방식은 예측에 크게 실패할 수 있다. 이 연구는 코어-셸 구조에 쓸 수 있는 평균장 균질화 방식 네 가지(다상, 순차, 의사 결정립, 직접)를 제시하고 유효 탄성·열·유전 물성의 정확도를 수치 균질화 결과와 보고된 실험값에 견주었다. 묽은 코어-셸 알갱이의 정확한 장 해를 쓰는 방식을 강조하고, 널리 쓰이는 계면상 모델(알갱이와 바탕 재료 사이에 중간층을 두는 모델)은 코어-셸 구조를 제대로 나타내지 못해 피해야 한다고 보였다.[^p7] | 1저자 H. Lee, 마지막 저자 유승화 (5명) |
| 8 | 2024 | [Data-driven prediction of strain fields in auxetic structures and non-contact validation with mechanoluminescence for structural health monitoring](https://doi.org/10.36922/ijamd.3539) · International Journal of AI for Materials and Design | 3D 프린팅 기술이 발전하면서 푸아송 비가 음수인 오그제틱 구조를 센서와 구조 건전성 모니터링에 쓸 가능성이 커졌다. 구조의 건전성을 평가하려면 유효 변형률을 정확히 추정해야 하는데 구조가 복잡할수록 어렵고, 실제로 만들어 확인하는 일도 중요하다. 이 연구는 두 가지를 내놓았다. 첫째, 유한요소 시뮬레이션 데이터를 학습한 다중 커널 계층형 심층 신경망으로 복잡한 오그제틱 구조의 유효 변형률 분포를 예측했다. 학습할 변수 수를 줄이면서 특징 학습과 일반화를 높였고, 변형률 분포 예측 정확도가 90%를 넘었다. 둘째, 기계발광 입자를 넣어 3D 프린팅한 시편으로 변형을 접촉 없이 실시간으로, 높은 공간·시간 해상도로 보며 예측을 확인했고, 예측한 변형 집중 부위와 관찰한 부위가 맞았다.[^p8] | 1저자 J. Jo, 마지막 저자 유승화 (7명) |

## 교수와 전문 분야

유승화 교수(Seunghwa Ryu, 柳昇和)는 KAIST 기계공학과 교수다. 누리집 교수 페이지는 직위를 KAIST 지정 석좌 교수(KAIST Endowed Chair Professor)로 적고, 2025년 7월부터 InnoCORE PRISM-AI Center(AI 기반 지능형 설계-제조 통합 연구단)의 센터장을, 2026년 1월부터 KAIST AX학과 학과장을 맡고 있다고 적는다.[^prof] 첫 화면은 PRISM-AI를 유승화 교수가 연구단장을 맡고 여러 대학이 참여하는 AI 기반 지능형 설계·제조 통합 연구단으로 소개한다.[^home] 기계공학과 교수진 목록은 최종학위를 Ph.D., Stanford University (2011)로 적는다.[^melist]

교수 페이지에 따르면 KAIST에서 물리학 학사(2000–2004)를, Stanford University에서 물리학 석사(2004–2006)와 박사(2004–2011)를 받았다. Stanford University 기계공학과(2011.10–2012.03)와 MIT 토목환경공학과(2012.04–2013.01)에서 박사후 연구원을 지낸 뒤 2013년 2월 KAIST 기계공학과 조교수가 되었고, 부교수(2017.03–2022.08, 2020년 3월 정년 보장)를 거쳐 2022년 9월부터 정교수, 2025년 3월부터 KAIST 지정 석좌교수다. 2013년 2월부터 KAIST KI for the NanoCentury의 Adjunct Professor이고, 안식년에 Stanford University 기계공학과(2018.03–2019.02)와 UC Berkeley 기계공학과(2024.02–2025.02)의 방문 교수를 지냈다.[^prof] 학술 활동으로는 Advances in Nano Research의 Chief Editor(2022년 7월부터), Frontiers in Materials(Mechanics of Materials)와 Journal of Mechanical Science and Technology의 Associate Editor, International Journal of Plasticity의 Advisory Board Member(2026년 4월부터)를 적는다.[^prof]

교수 페이지가 적은 2021–2026년 수상과 선정은 과기부총리 과학기술진흥유공 표창, KAIST 학술상, KAIST 미래선도기술 대표연구성과 선정, 한국전산역학회 젊은연구자상(이상 2026), KAIST 지정 석좌교수, 대한기계학회 CAE부문 신진학술상, 한국전산구조공학회 미래기술상(이상 2025), 특허청 국제지식재산연수원 우수강사 표창장(2024), 한국멀티스케일역학회 젊은연구자상, KAIST 융합연구상(이상 2023), 한국 차세대 과학기술한림원(Y-KAST) 2022년도 신입회원, 기계공학과 우수강의상(2022년 봄 고체역학, 2021년에 받은 2020년 가을 응력해석기초)이다.[^prof] Teaching 페이지는 2021–2024년 강의로 고체역학(ME231), 응력해석기초(ME330), 고등고체역학(ME530), 탄성학 및 미시역학 개론(ME639)을 적는다.[^teach] Publications 페이지 Books 목록에는 공저 『제조 AI 빅데이터 분석기법 현장공장 제조데이터 이해 및 AI 분석의 첫걸음』(2022)이 있다.[^pubs]

Publications 페이지의 국제 학술지 목록은 2008년부터 이어진다. 2011년의 전위 핵생성 속도 예측 연구, 2016년의 금속 나노선 전위와 펄라이트강 계면의 원자 시뮬레이션, 2019년의 미시역학 기반 복합재 균질화와 합성곱 신경망으로 복합재 물성을 예측한 연구가 있다.[^pubs] 2021–2026년 논문으로 보면 전문 분야는 고체역학과 다중 스케일 재료 모델링을 바탕으로 한 기계학습 기반 재료·구조 역설계, 물리정보 기계학습, 사출성형 등 제조 공정 최적화, 대형 언어 모델 기반 공학 에이전트다.[^pubs][^methods]

## 응용 분야

Research 페이지는 연구의 응용 분야로 제조, 모빌리티, 전자, 에너지를 들고, AI 기반 제조 연구의 대상으로 반도체 원자층 증착 챔버, 사출성형, 조선 강판 가열 가공, 열 관리 시스템을 든다.[^research] 기계공학과 연구분야 안내는 주요 응용 산업으로 자동차와 반도체(소재/역학/제조), 반도체와 자동차·항공(헬스케어/나노/광학)을 적는다.[^meres] 대표 논문에 나오는 응용은 소프트 로봇·생체의료 기기·지능형 구조(열 반응 능동 복합재),[^p2] 열전 재료의 대량 선별과 역설계,[^p3] 펼침 구조·소프트 로봇 구동기·충격 완화 장치(키리가미 메타물질),[^p4] 신축성 기능 소자(액체 금속 복합재),[^p7] 센서와 구조 건전성 모니터링(오그제틱 구조)이다.[^p8] 진행 과제 목록에는 리튬이차전지 설계 인공지능 플랫폼, 다상소재 혁신 생산공정, 식약처 컴퓨터모델링 기반 의료기기 평가체계 구축사업의 심뇌혈관 의료진단 기술, 체내 생체 신호 모니터링 시스템, 첨단 제조산업용 거대언어모델 과제와, 기업과의 AI 기반 제품 제작 최적화(EnableFusion), AI 기반 해석 가속화와 물성 평가(한국타이어), AI 기반 설계(현대일렉트릭), 다물리 시뮬레이션 기반 공정 개선(한국일렉트릭) 과제가 있다.[^research]

## 구성원

누리집 People 페이지의 박사후연구원(Postdoc) 4명, 박사과정(PhD Candidate) 14명, 석사과정(MS Candidate) 13명, 학부 연구생(URP student) 1명, 모두 32명이다. 시작 칸은 과정 옆 괄호의 시작 연월이고, 연구 주제는 카드에 적힌 그대로다. 과정 칸 괄호의 학생 대표(Student Representative)와 장학 표기도 카드 표기다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Jun Kyu Choe (최준규) | 박사후연구원 | 2025.8~ | soft actuator design powered by AI |  |
| Kyeongsun Kim (김경선) | 박사후연구원 | 2026.9~ | digital twin, surrogate models, soil mechanics |  |
| Junhyeong Lee (이준형) | 박사후연구원 | 2026.3~ | agentic AI, fatigue life prediction/optimization | 1 |
| Hugon Lee (이후곤) | 박사후연구원 | 2026.9~ | homogenization theory, process optimization, multi-fidelity data based design | 1, 7, 8 |
| Junhee Cho (조준희) | 박사과정 | 2022.8~ | modeling and optimization of 3d printing process and structure |  |
| Songho Lee (이송호) | 박사과정 | 2023.2~ | 3d printing experiments , fatigue life prediction/optimization | 2, 3 |
| Heekyu Kim (김희규) | 박사과정 | 2023.9~ | energy and biomedical applications of deep learning |  |
| Joonyoung Kim (김준영) | 박사과정 | 2022.8~ | injection modeling process optimization |  |
| Sukheon Kang (강석헌) | 박사과정 (Student Representative) | 2024.3~ | metastructure modeling and optimization | 2, 4, 8 |
| Sung Jae Heo (허성재) | 박사과정 | 2024.3~ | data-driven aerospace turbine optimization |  |
| Joohee Choi (최주희) | 박사과정 | 2024.3~ | modeling and optimization with atomistic modeling |  |
| Minwoo Park (박민우) | 박사과정 | 2024.9~ | modeling and optimization of composite structures | 8 |
| Hyunbin Moon (문현빈) | 박사과정 | 2024.9~ | multiphysics modeling, structural optimization | 3, 5, 7 |
| Hanbin Cho (조한빈) | 박사과정 | 2025.3~ | machine learning applications to energy materials | 6 |
| Jecheon Yu (유제천) | 박사과정 | 2025.3~ | reinforcement learning for structural design | 2, 7 |
| Inhyo Lee (이인효) | 박사과정 | 2026.3~ | multi-agent AI for materials development and discovery |  |
| Jinun Byun (변진언) | 박사과정 | 2026.3~ | diffusion model for structural design |  |
| Sangwoo Jung (정상우) | 박사과정 | 2026.9~ | physics informed machine learning |  |
| Jongwon Park (박종원) | 석사과정 | 2025.3~ | agentic ai for materials discovery and numerical analysis |  |
| Hyeok Jae Chae (채혁재) | 석사과정 | 2025.3~ | agentic ai for materials discovery and numerical analysis |  |
| Jihye Shin (신지혜) | 석사과정 | 2025.3~ | agentic ai for structural design |  |
| Junseo Park (박준서) | 석사과정 | 2025.9~ | experimental design of metastructures |  |
| Junyoung Lee (이준영) | 석사과정 (Hankook Tire CTO fellow) | 2025.9~ | physics-informed ai, physical ai |  |
| Junhee Shin (신준희) | 석사과정 | 2026.3~ | physics-informed ai |  |
| Hyeongcheol Choi (최형철) | 석사과정 | 2026.3~ |  |  |
| Hyuna Kim (김현아) | 석사과정 | 2026.3~ |  |  |
| John Robbie Laurio | 석사과정 (GKS program fellow) | 2026.9~ |  |  |
| Daeyoung Kwon (권대영) | 석사과정 | 2026.9~ | physics-informed ai |  |
| Junhyung Lee (이준형) | 석사과정 | 2026.9~ |  |  |
| Wonjong Jeong (정원종) | 석사과정 | 2026.9~ | agentic - physical ai for closed-loop experiments |  |
| Jiyoun Lee (이지연) | 석사과정 | 2026.9~ |  |  |
| Junghyeon Chae (채정현) | URP student |  | agentic ai for numerical modeling |  |

## 졸업생과 이전 구성원

누리집 People 페이지 Alumni의 박사(PhD Degree) 16명, 석사(MS Degree) 27명, 박사후연구원(Postdoctoral Researchers) 7명, URP 학생 4명(항목 3개), 모두 54건이다. 같은 사람이 석사와 박사, URP와 학위 과정에 함께 나오는 경우가 있다. 학위·과정 칸은 페이지에 적힌 학위 연도와 재적 기간 그대로이고, 박사후연구원은 페이지가 괄호에 적은 박사 학위 기관과 기간을 함께 적었다. 진로 칸의 「직후」와 「현재」는 페이지의 right after group과 now 표기이며, 화살표는 페이지가 적은 이동 순서다. 2026년 석사 졸업생 3명은 페이지의 학위 논문 칸이 비어 있다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 | 랩이 적은 수상 |
|---|---|---|---|---|
| Jiyoung Yoon | PhD 2026, from Mar 2022 to Feb 2026 (PhD) | 직후·현재: Research Staff at KITECH |  |  |
| Junhyeong Lee | PhD 2026, from Mar 2022 to Feb 2026 (PhD) | 직후·현재: InnoCORE postdoc fellow at KAIST |  |  |
| Donggeun Park | PhD 2026, from Mar 2022 to Feb 2026 (PhD) | 직후·현재: Research Staff at Samsung Electronics |  |  |
| Jinwook Yeo | PhD 2025, from Mar 2021 to Feb 2025 (PhD) | 직후·현재: Research Staff at Samsung Electronics | Development of Architectured Materials for Enhanced Specific Stiffness Utilizing Data-Driven Optimization |  |
| Wabi Demeke | PhD 2024, from Sep 2020 to Aug 2024 (PhD) | 직후·현재: Postdoc Researcher at KAIST → Research Staff at Enablefusion → U of Wyoming Postdoc Fellowship |  |  |
| Taegu Lee | PhD 2024, from Mar 2019 to Feb 2024 (PhD) | 직후·현재: Research Staff at Samsung Electronics | Molecular dynamics study on deformation behavior of aluminum- graphene composite and prediction of mechanical properties through deep neural networks |  |
| Jaemin Lee | PhD 2024, from Mar 2020 to Feb 2024 (PhD) | 직후·현재: Research Staff at Agency for Defense Development (ADD) | Leveraging machine learning in material and structural design : applications in heating patterns, composite configuration, and rib pattern optimization |  |
| Kundo Park | PhD 2024, from Sep 2019 to Feb 2024 (PhD) | 직후·현재: Postdoc at UC Berkeley → InnoCORE Postdoc at KAIST → Samsung Electronics | Analysis and optimization of non-linear mechanical properties of structural composite materials using machine learning-based algorithms |  |
| Jiyoung Jung | PhD 2023, from Mar 2019 to Feb 2023 (PhD) | 직후·현재: Postdoc at UC Berkeley → Tesla R&D, California | Effective Behavior Analysis of Composite using Homogenization and Transfer Learning and Process Optimization for Injection Molding based on Machine Learning |  |
| Yongtae Kim | PhD 2022, from Mar 2018 to Feb 2022 (PhD) | 직후·현재: Research Staff at Samsung Electronics | Optimal design of nature-inspired structures with machine learning and theoretical analysis |  |
| Youngsoo Kim | PhD 2020, from Sep 2016 to Aug 2020 (PhD) | 직후: Senior Researcher at KIMM; 현재: Research Staff at Samsung Electronics → Research Staff at Agency for Defense Development (ADD) | Theoretical, data-driven, and experimental analyses on composites with various microstructures |  |
| Sangryun Lee | PhD 2020, from Mar 2014 to Feb 2020 (integrated MS-PhD) | 직후: Postdoc at UC Berkeley, USA; 현재: Assistant Professor of Mechanical Engineering at Ewha Womans University | Micromechanics-Based Homogenization of the Effective Physical Properties of Reinforced Composites |  |
| Donggyu Kim | PhD 2020, from Mar 2016 to Feb 2020 (PhD) | 직후: Postdoc at KIMM; 현재: Research Staff at Samsung Electronics → Start-up founder | Theoretical Study on Wettability of Microstructured Sruface |  |
| Sunghwan Kim | PhD 2019, from Aug 2013 to Feb 2019 (integrated MS-PhD) |  | A computational study on the atomic-level structure-property relationship and mechanical behavior of irradiated metallic glasses |  |
| Jaemin Kim | PhD 2018, from Feb 2015 to Feb 2018 (integrated MS-PhD) |  | Atomistic simulation study on mechanical properties of pearlitic steel |  |
| Jihoon Han | PhD 2015 (co-advised with Prof. Se-young Im at KAIST) | 직후: Postdoc at KAERI; 현재: Assistant Professor of Mechanical Engineering at Chonbuk National University | Evaluation of mechanical properties for nanostructures using atomistic modeling |  |
| Jinun Byun | MS 2026, from Mar 2024 to Feb 2026 | 직후: PhD student at S. Ryu group at KAIST |  |  |
| Inhyo Lee | MS 2026, from Mar 2024 to Feb 2026 | 직후: PhD student at S. Ryu group at KAIST |  |  |
| Sangwoo Jung | MS 2026, from Mar 2024 to Feb 2026 | 직후: PhD student at S. Ryu group at KAIST |  |  |
| Benno Schoenstei | MS 2025, from Sep 2023 to Aug 2025 | 직후: PhD student at Bundeswehr University Munich | Improving Mechanical Property Predictions in Composites Using Deep Neural Networks with Attention, Transfer Learning, and Data Augmentation |  |
| Jecheon Yu | MS 2025, from Mar 2023 to Feb 2025 | 직후: PhD student at S. Ryu group at KAIST | Deep Reinforcement Learning-based Optimization for the Shape of an Adhesive Pillar with Enhanced Adhesion |  |
| Han-Bin Cho | MS 2025, from Mar 2023 to Feb 2025 | 직후: PhD student at S. Ryu group at KAIST |  |  |
| Hyeonbin Moon | MS 2024, from Sep 2022 to Aug 2024 | 직후: PhD student at S. Ryu group at KAIST | Prediction of Deformation and Inverse Design of Heating Patterns for Hot Forming Processes of Ship Components with High-Dimensional Shape Degrees of Freedom |  |
| Minwoo Park | MS 2024, from Sep 2022 to Aug 2024 | 직후: PhD student at S. Ryu group at KAIST | Enhancing Prediction Performance and Generalizing Transverse Behavior of Unidirectional Composites via Strategic Input Feature Augmentation |  |
| Sukheon Kang | MS 2024, from Mar 2022 to Feb 2024 | 직후: PhD student at S. Ryu group at KAIST | Design of Auxetic Metamaterial Structures for Improved Low Cycle Fatigue Life and Negative Poisson’s Ratio using Multi- objective Bayesian Optimization |  |
| Hyukjoon Choi | MS 2023, from Sep 2021 to Aug 2023 | 직후: Samsung Electronics | A research about data-driven approach to design space exploration and optimization of bossed structure for silicon piezo-resistive pressure sensor |  |
| Keonpyo Kong | MS 2022, from Mar 2021 to Feb 2023 | 직후: Hyundai Motors | Optimization of the Structural Rib Layout for the Stiff Tailgate Based on Multi-Objective Bayesian Optimization |  |
| Eunjeong Park | MS 2022, from Sep 2020 to Aug 2022 | 직후: Samsung Electronics | Design of Elasticity Prediction Machine Learning Model and Shape Optimization |  |
| Junhyeong Lee | MS 2022, from Mar 2020 to Feb 2022 | 직후: PhD student at S. Ryu group at KAIST | Electrode Placement Optimization for Electrical Impedance Tomography using Active Transfer Learning |  |
| Jinwook Yeo | MS 2021, from Mar 2019 to Feb 2021 | 직후: PhD student at S. Ryu group at KAIST | A study on the simulation model for the analysis of piezoelectric resistance in 1D nanomaterial networks |  |
| Sojin Kim | MS 2021, from Mar 2019 to Feb 2021 | 직후: Researcher at Samsung Electronics(삼성전자) | 머신러닝을 이용한 복합접착기둥의 최적화 |  |
| Wabi Demeke | MS 2020, from Sep 2018 to Aug 2020 | 직후: PhD student at S. Ryu group at KAIST | Optimization of segmented thermoelectric power generators using artificial neural network (ANN) and genetic optimization algorithm (GOA) |  |
| Jaemin Lee | MS 2020, from Mar 2018 to Feb 2020 | 직후: PhD student at S. Ryu group at KAIST | Prediction of irreversible jumps in Cu64Zr36 metallic glass using machine learning |  |
| Jiyoung Jung | MS 2019, from Mar 2017 to Feb 2019 | 직후: PhD student at S. Ryu group at KAIST; 현재: postdoc at UC Berkeley | Investigation of effective thermoelectric properties of composite with interfacial resistance using micromechanics-based homogenisation |  |
| Taegu Lee | MS 2019, from Mar 2017 to Feb 2019 | 직후: PhD student at S. Ryu group at KAIST | Development of interatomic potential to predict deformation behavior of γ-TiAl and analysis of ternary effect |  |
| Kundo Park | MS2019 (co-advised with Prof Flavia Libonati for dual degree with Polimi, Italy), from Mar 2017 to Aug 2019 | 직후: PhD student at S. Ryu group at KAIST | Coupled CNT network and IR Thermography monitoring for analysis of damage and fatigue property of composite materials |  |
| Yongtae Kim | MS 2018, from Mar 2016 to Feb 2018 | 직후: PhD student at S. Ryu group at KAIST; 현재: Samsung Electronics | Elastic and fracture property analyses of two-dimensional composite structure with lattice spring model |  |
| Byungkwan Jeong | MS 2018, from Mar 2016 to Feb 2018 | 직후: Researcher at Korea Institute of Industrial Technology, Inchon Campus | Systematic investigation of the deformation mechanisms of -TiAl single crystal nanowire |  |
| Heeyeong Jeong | MS 2018, from Mar 2016 to Feb 2018 | 직후: Staff member at TmaxSoft; 현재: Start-up founder | Phase-field modeling for crack propagation in bio-inspired composites |  |
| Youngsoo Kim | MS 2016, from Sep 2014 to Aug 2016 | 직후: PhD student at S. Ryu group at KAIST; 현재: ADD | Mechanical analysis on staggered platelet composites and experiment using 3D printer |  |
| Hansol Lee | MS 2016, from Sep 2014 to Aug 2016 | 직후·현재: Researcher at Korea Aerospace Industries, LTD | Development of molecular dynamics force field for predicting the vapor pressure of metal-organic compound |  |
| Donggyu Kim | MS 2016, from Mar 2014 to Feb 2016 | 직후: PhD student at S. Ryu group at KAIST; 현재: Samsung Electronics | Theoretical study of wetting transparency of graphene on realistic surface |  |
| Joo-Yeun Ham | MS 2014 (Co-advised with Prof. Seunghwan Ko at KAIST (now at SNU)) | 직후: PhD student at Z. Bao group at Stanford University; 현재: Lam Research | Hierarchical multiscale hybrid nanocomposite of metal-nanowires / carbon-nanotubes for highly stretchable and transparent conductors in wearable electronics |  |
| Heok Yoon | Postdoctoral Researcher (PhD from Stanford), from Sep 2025 to Feb 2026 (0.5 yrs) | Researcher at Samsung Electronics |  |  |
| Hyunggwi Song | Postdoctoral Researcher (PhD from UIUC), from Sep 2020 to Aug 2023 (3 yrs) | Researcher at ADD (Agency for Defense Development), USA, Now, Professor at Chungbuk National University |  |  |
| Sangryun Lee | Postdoctoral Researcher (PhD from KAIST, Korea at Ryu group), from Mar 2020 to Feb 2021 (1 yr) | Researcher at UC Berkeley, USA, Now, Professor at Ewha Womans University |  |  |
| Suman Timilsina | Postdoctoral Researcher (PhD from Kyungbuk National University, Korea), from Mar 2020 to Dec 2020 (10 months) | Lecturer at Kyungbuk National University, Korea |  |  |
| Stefano Signetti | Postdoctoral Researcher (PhD from University of Trento, Italy), from 2017 to 2019 (2 yr) | Research Scientist at Fraunhofer Institute for High-Speed Dynamics, Germany |  |  |
| Hadi Ghaffarian | Postdoctoral Researcher (PhD from Sharif University, Iran), from 2017 to 2019 (2 yr) | Researcher at Prof Dongchan Jang group at KAIST NQE |  |  |
| Jichul Kim | Postdoctoral Researcher (PhD from Stanford University, USA), from 2013 to 2014 (1 yr) | Researcher at Prof Taeyoung Yoon group at Seoul National University |  |  |
| Sangjun Lee (이상준) | URP, Aug 2013-May 2014 | 직후: to PhD Course at UIUC Physics |  | URP 발표대회 장려상 수상 |
| Kundo Park (박건도) | URP, Jan 2016 to June 2016 | 직후: to MS Course at KAIST, Ryu group |  | URP 발표대회 장려상 수상 |
| Simeneh S. Guelat | URP from Jan 2017 to June 2017 |  |  |  |
| Wabi Demeke | URP from Jan 2017 to June 2017 | 직후: to MS Course at KAIST, Ryu group |  |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지 International Journal 목록의 2021–2026년 연도 구역 119편(83–202번 가운데 191번 제외)과 Domestic Journal 목록의 2025년 1편, 연도 표기가 없는 국내 보고서 1편이다. 연도는 누리집의 연도 구역이고, 제목·저자·학술지 표기는 누리집 그대로이며 이름 뒤 †·* 표시도 누리집 표기다. 2026년 구역의 3편과 2025년 구역의 2편은 누리집이 권·쪽 없이 accepted로 적은 논문이라 학술지 이름 뒤에 「(게재 승인)」을 붙여 출판 논문과 구분했고, 연도는 누리집이 둔 구역을 따랐다. 2021년 구역 항목은 연도만 적혀 있어 2021년 10월 전에 나온 논문이 섞여 있을 수 있다. 유승화 교수가 마지막 저자가 아닌 공동 연구 논문도 목록대로 실었다. 국내 보고서(화학소재 정보은행 심층보고서)는 누리집에 연도가 적혀 있지 않아 「연도 표기 없음」 아래에 두었다.[^pubs]

**2026**

- Yongjin Choi†, Hyeonbin Moon†, and Seunghwa Ryu\*. "Differentiable FEM versus PINN for pavement layer inverse analysis: enforcing physics as hard or soft constraints". *Computer-Aided Civil and Infrastructure Engineering (게재 승인)*.
- Jinwook Yeo†, Peter Serles†, Donggeun Park, and Julia Greer\*, and Seunghwa Ryu\*. "Enhancing Specific Stiffness of Nano-Architected Materials through Generative AI and Active Learning". *Advanced Science (게재 승인)*.
- Minwoo Park†, Junseo Park†, Minkyu Lee†, Hugon Lee, Hanbin Cho, Ikjin Lee\* and Seunghwa Ryu\*. "Uncertainty-Aware Structure-Property Mapping of Spinodoid Metamaterials via Heteroscedastic Gaussian Process Regression". *Materials & Design 270, 116914 (2026)*.
- Jinun Byun†, Kundo Park†, Jecheon Yu, Donggeun Park\*, and Seunghwa Ryu\*. "Inverse Design of Nacre-Inspired Composites with Multi-physics Constraints via Diffusion Model". *Composites Part B:Engineering 327, 114134 (2026). Invited article*.
- Yongwoo Kim, Hugon Lee, Sangmin Rhie, Seunghwa Ryu, Keonwook Kang. "Structural hierarchy can enhance the elastic modulus of random porous materials". *Heliyon 12, e45275 (2026)*.
- Sung Jun Park, Dongeun Park, Seunghwa Ryu, Jun Young Kim\* et al. "Measurement-informed Deep Learning for Real-time Monitoring of Hydrodynamic Drying Dynamics in Inkjet-printed Display Pixels via Low-resolution Imaging". *ACS Applied Materials & Interfaces 18, 42223 (2026)*.
- Sukheon Kang†, Sukkyung Kang†, Sanha Kim\*, and Seunghwa Ryu\*. "Data-Free Physics-Informed Inverse Programming of Bistable Kirigami Energy Landscapes". *Materials Horizons 13, 9028 (2026). Selected to feature on the outside front cover*.
- Jecheon Yu†, Jinun Byun†, Hyeonbin Moon, Junhyeong Lee, and Seunghwa Ryu\*. "Dual-Constrained Diffusion Model for Nonlinear Microstructure Inverse Design with Direct Evaluation". *Computer Methods in Applied Mechanics and Engineering 461, 119267 (2026)*.
- Yunheum Lee, Sungha Jeon, Min Kim, Joonhee Won, Jinwook Yeo, Kyunghyun Jo, Soyeon Lee, Kieun Park, Yechan Yang, Chul Kim, Gun-Hee Lee, Seunghwa Ryu, Sungho Jo, and Seongjun Park. "1-D Collocated Dual-Gradient Sensory Fibers for Comprehensive Sensing and Decoding of Complex Human Motion and Physiology". *Advanced Materials 38, e74328 (2026)*.
- Hanbin Cho, Jecheon Yu, Hyeonbin Moon, Jiyoung Yoon, Junhyeong Lee, Giyoung Kim, Jinhyoung Park and Seunghwa Ryu. "Real-Time Structural Health Monitoring with Bayesian Neural Networks: Distinguishing Aleatoric and Epistemic Uncertainty for Digital Twin Frameworks". *International Journal of Precision Engineering and Manufacturing - Green Technology 13, 2555 (2026)*.
- Daeho Kim, Joohee Choi, Inhyeok Yeo, Seunghwa Ryu, Seung Min Han. "Thermo-mechanically Reliable Miscible Ni-Ti Multilayers via Graded Interface Engineering". *International Journal of Mechanical Sciences 325, 111817 (2026)*.
- Seongwoo Cho†\*, Hyeonbin Moon†, Iaroslav Gaponenko, Eunnuri Cho, Céline Lichtensteiger, Ruben Skjelstad Dragland, Ji Hye Lee, Jan Schultheiß, Dennis Meier, Seunghwa Ryu\*, Seungbum Hong\*, Patrycja Paruch\*. "Nanoscale frictional imaging of ferroelectric domains". *Science Advances 12, eaee0247 (2026)*.
- Heekyu Kim, Hugon Lee, Minwoo Park, and Seunghwa Ryu\*. "Morphology-, Noise-, and Resolution-Robust Ultrasound Elasticity Imaging with Fourier Neural Operators". *Computer Methods and Programs in Biomedicine 283, 109432 (2026)*.
- Joon-Young Kim, Songho Lee, Jecheon Yu, Junhyeong Lee, and Seunghwa Ryu\*. "Federated Learning Framework for Data-Sovereign Quality Prediction in Injection Molding". *International Journal of Precision Engineering and Manufacturing (게재 승인)*.
- Donggeun Park†, Minwoo Park†, Junheui Jo†, and Seunghwa Ryu. "Surface-Based Stress Tomography of Architected Metamaterials via Physics-Constrained Generative Learning". *Materials Horizons 13, 5369 (2026). Invited article. Selected to feature on the supplementary cover*.
- Songho Lee, Sukheon Kang, Jisoo Nam, Jecheon Yu, Miso Kim, and Seunghwa Ryu\*. "Inverse Design of Temperature-Responsive 4D Active Composites Using Reinforcement Learning". *Materials Horizons 13, 6500 (2026)*.
- Inhyo Lee, Hyeokjae Chae, Jongwon Park, Jihye Shin, Hugon Lee\*, and Seunghwa Ryu\*. "Comparative Assessment of Composition- and Structure-Based Surrogate Models Across 2D Materials Databases". *Physical Chemistry Chemical Physics, 28, 10119 (2026)*.
- Wabi Demeke, Sangryun Lee, Wonju Jeon\*, and Seunghwa Ryu\*. "Enhancing Elastic Energy Focusing in Multimode Strain Regions via Bayesian Optimization of Gradient-Index Phononic Crystals for Energy Harvesting". *International Journal of Solids and Structures 330, 113871 (2026)*.
- Joohee Choi, Gibeom Son, Hae-Jin Kim\*, Joonmyung Choi\*, and Seunghwa Ryu\*. "Coarse-Grained Modeling of P3HT:SBS Blends for Stretchable Organic Semiconductors". *Macromolecules 59, 3241 (2026) Selected to feature on the supplementary cover*.
- Hyeonbin Moon†, Donggeun Park†, Jinwook Yeo, and Seunghwa Ryu\*. "An Energy-Based Physics-Informed Computational Framework for Forward and Inverse Flexoelectric Problems". *International Journal for Numerical Methods in Engineering 28, e70280 (2026)*.
- Joon-Young Kim†, Jecheon Yu†, Heekyu Kim, and Seunghwa Ryu. "DRL-Based Injection Molding Process Parameter Optimization for Adaptive and Profitable Production". *Expert Systems With Applications 305, 1307034 (2026)*.
- Donggeun Park, Hanbin Cho, Changseob Kwon, Youngyeon Ji\*, and Seunghwa Ryu\*. "Optimizing Chamber Systems for Deposition Processes in the Semiconductor Industry with Deep Learning Framework: Tackling Small Simulation Datasets". *Journal of Intelligent Manufacturing 37, 1075 (2026)*.
- Hyeonbin Moon, Junhyeong Lee, Jechun Yu, and Seunghwa Ryu\*. "Physics-Informed AI for Material Characterization: A Perspective on Data-Efficient Discovery through Physics- Informed Neural Networks". *International Journal of AI for Materials and Design 2, 1 (2026). Invited article. Selected to feature on the front cover*.
- Donggeun Park†, Hyeonbin Moon†, and Seunghwa Ryu\*. "A Self-Correcting Multi-Agent Framework for Language-Based Physics Simulation and Explanation". *npj Artificial Intelligence 2, 10 (2026)*.

**2025**

- Sukheon Kang, Youngkwon Kim, Jinkyu Yang\*, and Seunghwa Ryu\*. "Physics-informed neural networks for programmable origami metamaterials with controlled deployment". *Materials Horizons 12, 10641 (2025) Invited article. Selected to feature on the inside back cover*.
- Minwoo Park†, Junheui Jo†, and Seunghwa Ryu\*. "Data-driven Design of Isotropic and High-Stiffness TPMS-based Amorphousness-Induced Architected Material (TAAM)". *Materials & Design 260, 115065 (2025)*.
- Junhyeong Lee†, Joon-Young Kim†, Heekyu Kim†, Inhyo Lee, and Seunghwa Ryu\*. "IM-Chat: A Multi-agent LLM-based Framework for Knowledge Transfer in Injection Molding Industry". *Journal of Manufacturing Systems 83, 839 (2025)*.
- Hugon Lee†, Hyeongbin Moon†, Junhyeong Lee†, and Seunghwa Ryu. "Toward Knowledge-Guided AI for Inverse Design in Manufacturing: A Perspective on Domain, Physics, and Human-AI Synergy". *Advanced Intelligent Discovery 0, e2500107 (2025) Invited article*.
- Hyunju Kang†, Junhyeong Lee†, Soo Hyun Lee, Jinhyeok Jeon, ChaeWon Mun, Jun-Yeong Yang, Hyung-Jun Kwon, In-Chul Lee, Sunjoo Kim, Eun-Kyung Lim, Juyeon Jung, Yongwon Jung\*, Seunghwa Ryu\*, Sung-Gyu Park\* and Taejoon Kang\*. "Interpretability-Driven Deep Learning for SERS-Based Classification of Respiratory Viruses". *Biosensors and Bioelectronics 289, 117891 (2025)*.
- Hyeonbin Moon†, Songho Lee†, Wabi Demeke\*, Byungki Ryu, and Seunghwa Ryu\*. "Physics-Informed Neural Operators for Generalizable and Label-Free Inference of Temperature-Dependent Thermoelectric Properties". *npj Computational Materials 11, 272 (2025)*.
- Hyeonbin Moon†, Donggeun Park†, Hanbin Cho, Hong-Kyun Noh, Jae Hyuk Lim\*, and Seunghwa Ryu\*. "Physics-Informed Neural Network-Based Discovery of Hyperelastic Constitutive Models from Extremely Scarce Data". *Computer Methods in Applied Mechanics and Engineering 446, 118258 (2025)*.
- Hanbin Cho, Minjik Kim, Youngseo Park, Hugon Lee, Ijin Lee, and Seunghwa Ryu. "Comparative Study of Gaussian Process and Additive Gaussian Process for Multi-objective Optimization in Air-Cooled Battery Thermal Management Systems". *Journal of Mechanical Science and Technology 39, 7623 (2025)*.
- Daeho Kim†, Joohee Choi†, Seunghwa Ryu\* , and Seung Min Han\*. "Strengthening Effect in Aluminum-Graphene Nanolayered Composites via Interface Engineering". *Materials Science & Engineering A 938, 148440 (2025)*.
- Gun-Hee Lee, Yunheum Lee, Hyeonyeob Seo, Kyunghyun Jo, Jinwook Yeo, Semin Kim, Jae-Young Bae, Carmel Majidi, Jiheong Kang, Seung-Kyun Kang, Seunghwa Ryu and Seongjun Park\*. "Mass production of liquid metal-based twisted fiber electrodes with high conductivity, stretchability, and toughness for intelligent digital apparel". *Nature Communications 16, 4320 (2025)*.
- Jecheon Yu, and Seunghwa Ryu. "Deep reinforcement learning-based optimization for the shape of an adhesive pillar with enhanced adhesion strength". *Journal of Mechanical Design 147, 091703 (2025)*.
- Byungki Ryu, Seunghyun Oh, Wabi Demeke, Jaywan Chung, Jongho Park, Nirma Kumari, Aadil Fayaz Wani, Seunghwa Ryu and SuDong Park. "Wiedemann-Franz Law and Thermoelectric Inequalities: Effective ZT and Single-leg Efficiency Overestimation". *Journal of Applied Physics 137, 115001 (2025)*.
- Hyeonbin Moon, Kundo Park, Jaemin Lee, Dongki Lee\*, and Seunghwa Ryu\*. "Towards the automation of plate forming process for shipbuilding: A DNN-based multi-start convex optimization framework for the prompt inverse design of line heating patterns". *Extreme Mechanics Letters 76, 102313 (2025). Invited article*.
- Sukheon Kang†, Hyeonbin Moon, Seonho Shin, Mahmoud Mousavi, Hyokyung Sung\*, and Seunghwa Ryu\*. "Design of Auxetic Metamaterial for Enhanced Low Cycle Fatigue Life and Negative Poisson’s Ratio through Multi-objective Bayesian Optimization". *Materials & Design 252, 113798 (2025). Selected to feature on the front cover*.
- Hyun Seok Kang†, Sumin Kim†, Hyunggwi Song, Yung Lee, Junho Jang, Won Gi Chung, Changyeon Gu, Junmo Kim, Taek-Soo Kim, Seunghwa Ryu, Jang-Ung Park\* and Byeong-Soo Bae\*. "Skin-Tailored Adhesive Electrode with Tunable Poisson’s Ratio for Stable Electrophysiological Communication". *Advanced Health Care Materials 14, 2404882 (2025)*.
- Hanbin Cho, Hugon Lee, and Seunghwa Ryu. "Sequential Multi-Objective Bayesian Optimization of Air-Cooled Battery Thermal Management System with Spoiler Integration". *Journal of Energy Storage 114, 115586 (2025)*.
- Joon-Young Kim†, Heekyu Kim†, Keonwoo Nam, Daeyoung Kang , Seunghwa Ryu. "Development of an Injection Molding Production Condition Inference System Based on Diffusion Model". *Journal of Manufacturing Systems 79, 162 (2025)*.
- Peter Serles†, Jinwook Yeo†, Michel Haché, Pedro Guerra Demingos,Jonathan Kong, Pascal Kiefer, Somayajulu Dhulipala, Boran Kumral, Katherine Jia, Shuo Yang, Tianjie Feng, Charles Jia, Pulickel M. Ajayan, Carlos Portela, Martin Wegener, Jane Howe, Chandra Veer Singh, Yu Zou, Seunghwa Ryu\*, Tobin Filleter\*. "Ultrahigh Specific Strength by Bayesian Optimization of Carbon Nanolattices". *Advanced Materials 37, 2570108 (2025). Selected to feature on the front cover*.
- Jiyoung Yoon†, Junhyeong Lee†, Seunghwa Ryu\*, and Jinhyoung Park\*. "Enhanced Energy Harvesting in Rotary Triboelectric Nanogenerators via Gaussian Process Regression-Based Bayesian Optimization". *Nano Energy 135, 110653 (2025)*.
- Hugon Lee†, Jinwook Yeo†, Keonpyo Kong, Dujae Myeong, Donghoon Jang, Jongyeob Lee, Hyeokhwan Choi, Namkeun Kim\*, and Seunghwa Ryu\*. "Bayesian optimization of tailgate rib structure enhancing structural stiffness under manufacturing constraints of injection molding". *Journal of Manufacturing Processes 134, 739 (2025)*.
- Minwoo Park, Jiyoung Jung, Hyeonbin Moon, Donggeun Park, Myeong-Seok Go, Hong-Kyun Noh, Jae Hyuk Lim,\* and Seunghwa Ryu\*. "Enhancing prediction performance and generalizing for transverse behavior of unidirectional composites via strategic input feature augmentation". *Advanced Theory and Simulations (게재 승인)*.
- Jinwook Yeo, Samantha Cheung, Wendy Gu, and Seunghwa Ryu. "Hybrid TPMS-Based Architectured Materials (HTAM) for Enhanced Specific Stiffness Using Data-Driven Design". *Materials & Design 249, 113523 (2025)*.
- Jongil Kim†, Jinwook Yeo†, Bumsu Park, Jeehun Jeong, Seunghwa Ryu\*, and Sang Ho Oh\*. "Elastic Relaxation of Coherent InGaN/GaN Interfaces at the Microwire LED Sidewall". *Advanced Science (게재 승인) (2025). Selected to feature on the back cover*.
- Daekyeong Jung†, Soojin Jang†, Donggeun Park†, Nam Ho Bae, Chung Soo Han, Seunghwa Ryu\*, Eun-Kyung Lim\*, Kyoung G. Lee\*. "Automated Microfluidic Systems Facilitating the Scalable and Reliable Production of Lipid Nanoparticles for Gene Delivery". *Biochip Journal 19, 79 (2025)*.
- 유승화, 이후곤, 문현빈, 이준형, 이율희. "인공지능 기반 고성능 나노복합재 설계 기술". *Nano Insight 25, 16-54 (2025)*.

**2024**

- Sukheon Kang†, Hyunggwi Song†, Hyun Seok Kang, Byeong-Soo Bae, and Seunghwa Ryu\*. "Customizable Metamaterial Design for Desired Strain-Dependent Poisson's Ratio Using Constrained Generative Inverse Design Network". *Materials & Design 247, 113377 (2024). Invited article*.
- J. Gu, Y. Jung, J. Ahn, J. Choi, B. Kang, J. Jung, Y. Jeong, J.-H. Ha, Y. Jung, J. Park, S. Ryu, I. Lee, and I. Park\*. "Auxetic Kirigami Structure-Based Self-Powered Strain Sensor with Customizable Performance using Machine Learning". *Nano Energy 130, 110124 (2024)*.
- Hugon Lee, Jinwook Yeo, Jecheon Yu, Hyeonbin Moon, and Seunghwa Ryu. "Mean-field homogenization of liquid metal elastomer composites: comparative study and exact dilute solution of core-shell inclusion". *Journal of Physics: Condensed Matter 36, 505702 (2024). Invited article*.
- Junheui Jo, Kundo Park, Hyunggwi Song, and Seunghwa Ryu. "Innovative 3D printing of mechanoluminescent composites: Vat photopolymerization meets machine learning". *Additive Manufacturing 90, 104324 (2024)*.
- Ziyue Yang, Kundo Park, Jisoo Nam, Jaewon Cho, Yong-Il Kim, Hyeonsoo Kim, Seunghwa Ryu, and Miso Kim\*. "Laminate-inspired high strength piezoelectric self-powered sensing yarns via multi-objective Bayesian optimization". *Advanced Science 11, 2402440 (2024)*.
- Seunghwa Ryu, Geoffrey Robert Mitchell, Antonio Caggiano, Raul A Radovitzky, Patrizia Trovalusci, Nicola Maria Pugno. "Innovators in mechanics of materials". *Frontiers in Materials 10, 1346034 (2024)*.
- Seong-Won Jin, Myeong-Seok Go, Youngu Lee, Seunghwa Ryu and Jae Hyuk Lim. "Comprehensive correlation analysis of electromechanical behavior in high-stretchable carbon nanotube/polymer composites". *Functional Composites and Structures 6, 025010 (2024)*.
- Junheui Jo†, Minwoo Park†, Sukheon Kang†, Hugon Lee†, Chang-Yeon Gu, Taek-Soo Kim, Seunghwa Ryu. "Data-driven prediction of strain fields in auxetic structures and non-contact validation with Mechanoluminescence for structural health monitoring". *IJAMD 1, 48 (2024). Invited article. highly downloaded paper award*.
- Dongeun Park, Jaemin Lee, Hugon Lee, Grace X. Gu, and Seunghwa Ryu\*. "Deep Generative Spatiotemporal Learning for Integrating Fracture Mechanics in Composite Materials: Inverse Design, Discovery, and Optimization". *Materials Horizons 11, 3048 (2024). Selected to feature on the inside front cover*.
- Hugon Lee+, Mingyu Lee+, Jiyoung Jung, Ikjin Lee\*, and Seunghwa Ryu\*. "Enhancing Injection Molding Optimization for SFRPs Through Multi-Fidelity Data-Driven Approaches Incorporating Prior Information in Limited Data Environments". *Advanced Theory and Simulations 7, 2400135 (2024)*.
- Jiyoung Jung, Kundo Park, Hugon Lee, Byungjin Cho, and Seunghwa Ryu. "Comparative Study of Multi-objective Bayesian Optimization and NSGA-III based Approaches for Injection Molding Process". *Advanced Theory and Simulations 7, 2400130 (2024)*.
- Junhyeong Lee, Kyungseo Park, Kundo Park, Yongtae Kim, Jung Kim\*, and Seunghwa Ryu\*. "Electrode Placement Optimization for Electrical Impedance Tomography using Active Learning". *Advanced Engineering Materials 26, 2301865 (2024). Invited article*.
- Hyunju Kang+, Junheyong Lee+, Jeong Moon+, Taegu Lee+, Eun-Kyung Lim, Juyeon Jung, Yongwon Jung, Seok Jae LEe, Kyung G. Lee\*, Seunghwa Ryu\*, and Taejoon Kang\*. "Multiplex Detection of Foodborne Pathogens using 3D Nanostructure Swab and Deep Learning-Based Classification of Raman Spectra". *Small 20, 2308317 (2024)*.
- Soeun Lee, Hyeongbin Moon, Juri Kim, Seunghwa Ryu\*, Soon Mo Park\*, and Dong Ki Yoon\*. "On-demand Crack Formation on DNA Film via Organic Solvent-induced Dehydration". *Advanced Materials 36, 2314374 (2024)*.
- Nello Sansone, Jiyoung Jung, Peter Serles, Rafaela Aguia, Matthew Leroux, Tobin Filleter, Seunghwa Ryu\*, and Patrick Lee\*. "Synergy in Bioinspired Hybrid Composites with Hierarchically Structured Fibrous Reinforcements". *Chemical Engineering Journal 487, 150357 (2024)*.
- Lei Zhao+, Taegu Lee+, Siting Zheng, Wangshu Zheng, Seunghwa Ryu\*, Di Zhang\*, and Qiang Guo\*. "Ultrastrong and Deformable Aluminum-Based Composite Nanolaminates with Transformable Binary Intergranular Films". *Nano Letters 24, 3843 (2024)*.
- Haejin Lee+, Jaemin Lee+, Seunghwa Ryu\*, and Ilhan Chang\*. "Machine learning-based analysis and prediction model on the strengthening mechanism of biopolymer-based soil treatment". *Geomechanics and Engineering 36, 381 (2024)*.
- Jaemin Lee+, Donggeun Park+, Kundo Park, Hyunggwi Song, Taek-Soo Kim, and Seunghwa Ryu\*. "Integrating Hierarchical DNNs and Genetic Algorithms for Grid Composite Configuration Optimization for High Toughness". *Materials & Design 238, 112700 (2024)*.
- Hugon Lee, Sangryun Lee\*, and Seunghwa Ryu\*. "Advancements and challenges of micromechanics-based homogenization for the short fiber reinforced composites". *Multiscale Science and Engineering 5, 133 (2024)*.
- Wabi Demeke, Byungki Ryu\*, and Seunghwa Ryu\*. "Machine Learning-based Optimization of Segmented Thermoelectric Power Generators Using Temperature-Dependent Performance Properties". *Applied Energy 355, 122216 (2024)*.
- Young Jung, Jimin Gu, Jinwook Yeo, Wookjin Lee, Hyeonseok Han, Jungrak, Choi, Ji-Hwan Ha, Junseong, Ahn, Hanchul Cho, Seunghwa Ryu and Inkyu Park. "Highly Sensitive Soft Pressure Sensors for Wearable Applications based on Composite Films with Curved 3D Carbon Nanotube Structures". *Small 20, 2303981 (2024)*.

**2023**

- Wabi Demeke, Jiyoung Jung, Byungki Ryu, Wonju Jeon, and Seunghwa Ryu. "Design of Aluminum Plate Phononic Crystals with Wide Bandgaps Using Deep Neural Network-based Free-form Optimization". *Extreme Mechanics Letters 65, 102098 (2023)*.
- Juhee Lee+ , Tae Gu Lee+, Ha Neul Lee, Hyoungsoo Kim, Yoo Kyung Kang, Seunghwa Ryu\*, and Hyun Jung Chung\*. "Simple and multiplexed detection of nucleic acid targets based on fluorescent ring patterns and deep learning analysis". *ACS Applied Materials and Interfaces 15, 54335 (2023)*.
- Donggeun Park, Jaemin Lee, Kundo Park, and Seunghwa Ryu. "HGNet: A Hierarchical Multi-Task Learning Approach for Accelerated Composite Material Design and Discovery". *Advanced Engineering Materials 25, 2300867 (2023)*.
- Seunghwa Ryu. "K-Nanomechanics: Advancements and Applications of Atomistic Simulations in the Korean Solid Mechanics Community". *JMST Advances 5, 53 (2023). Invited Article*.
- Yongtae Kim†, Jinwook Yeo†, Kundo Park, Aymeric Destree, Zhao Qin, and Seunghwa Ryu\*. "Designing Directional Adhesive Pillar using Deep Learning-Based Optimization, 3D printing, and Testing". *Mechanics of Materials 185, 104778 (2023). Invited article*.
- Dongwook Yang, Han Ku Nam, Truong-Son Dinh Le, Jinwook Yeo, Younggeun Lee, Young-Ryeul Kim, Seung-Woo Kim, Hak-Jong Choi, Hyung Cheoul Shim, Seunghwa Ryu, Soongeun Kwon\*, and Young-Jin Kim\*. "Multi-modal E-Textile Enabled by One-step Maskless Patterning of Femtosecond-Laser-Induced Graphene on Nonwoven, Knit, and Woven Textiles". *ACS Nano 17, 18893 (2023)*.
- Donggeun Park+, Minwoo Park+, and Seunghwa Ryu. "Expanding Design Spaces in Digital Composite Materials: A Multi-Input Deep Learning Approach Enhanced by Transfer Learning and Multi-kernel Network". *Advanced Theory and Simulations 6, 2300465 (2023)*.
- Junhyeong Lee, Donggeun Park, Mingyu Lee, Hugon Lee, Kundo Park, Ikjin Lee, and Seunghwa Ryu\*. "Machine learning-based inverse design methods considering data characteristics and design space size in materials design and manufacturing: a review". *Materials Horizons 10, 5436 (2023)*.
- Kundo Park, Chihyeon Song, Jinkyoo Park, and Seunghwa Ryu. "Multi-objective Bayesian optimization for the designing of nacre-inspired composites: optimizing and understanding the biomimetics through AI". *Materials Horizons 10, 4329 (2023)*.
- Jinwook Yeo, Jiyoung Jung, and Seunghwa Ryu\*. "Coarse-Grained Modeling for Predicting the Piezoresistive Response of CNT-elastomer Nanocomposites". *Frontiers in Materials 10, 1219688 (2023). invited paper*.
- Dabin Kim, Ziyue Yang, Jaewon Cho, Donggeun Park, Dong Hwi Kim, Jinkee Lee, Seunghwa Ryu, Sang-Woo Kim, Miso Kim. "High-Performance Piezoelectric Yarns for Artificial Intelligence-enabled Wearable Sensing and Classification". *EcoMat 5, e12384 (2023)*.
- Donggeun Park, Jiyoung Jung, and Seunghwa Ryu\*. "Double Generative Network (DGNet) Pipeline for Structure- Property Relation of Digital Composites". *Composite Structures 319, 117131 (2023)*.
- Hyunggwi Song†, Eunjeong Park†, Hongjae Kim, Chung-Il Park, Taek-Soo Kim, Yoon Young Kim, and Seunghwa Ryu\*. "Free-form optimization of pattern shape for improving mechanical characteristics of a concentric tube". *Materials & Design 230, 111974 (2023)*.
- Youngki Yeo, Soo-Yoon Hwang, Jinwook Yeo, Jihun Kim, Jinhyuk Jang, Heung-Sik Park, Yong-Jin Kim, Duc Duy Le, Kyung Song, Moonhong Kim, Seunghwa Ryu\*, Si-Young Choi\* and Chan-Ho Yang\*. "Configurable crack wall conduction in a complex oxide". *Nano Letters 23, 398 (2023)*.
- Jiyoung Jung, Kundo Park, Byungjin Cho, Jinkyoo Park, and Seunghwa Ryu\*. "Optimization of Injection Molding Process using Multi-objective Bayesian Optimization and Constrained Generative Inverse Design Networks". *Journal of Intelligent Manufacturing 34, 3623 (2023)*.

**2022**

- Jiyoung Yoon, Junhyeong Lee, Giyoung Kim, Seunghwa Ryu\*, and Jinhyoung Park\*. "Deep Neural Network-Based Structural Health Monitoring Technique for Real-time Crack Detection and Localization using Strain Gauge Sensors". *Scientific Reports 12, 20204 (2022)*.
- Donggyu Kim, and Seunghwa Ryu\*. "Computational Experiments for Predicting Intrinsic Wetting Characteristics". *MRS Bulletin (2022). opinion & perspective article*.
- Wonbeom Lee, Hyunjun Kim, Inho Kang, Hongjun Park, Jiyoung Jung, Haeseung Lee, Hyunchang Park, Jisu Park, Jongmin Yuk, Seunghwa Ryu, Jae-Woong Jeong, and Jiheong Kang\*. "Universal assembly of liquid metal particles in polymers enables elastic printed circuit board". *Science 378, 637 (2022). Selected to feature on the front cover*.
- Donggeun Park, Jiyoung Jung, Grace Gu, and Seunghwa Ryu\*. "A generalizable and interpretable deep supervised neural network to predict strain field of composite in unseen design space". *Materials & Design 223, 111192 (2022)*.
- Sangryun Lee, Wonjae Choi, Jeongwon Park, Daesu Kim, Sahn Nahm, Wonju Jeon, Grace X. Gu, Miso Kim\*, and Seunghwa Ryu\*. "Machine Learning-enabled Development of High Performance Gradient-index Phononic Crystals for Energy Focusing and Harvesting". *Nano Energy 103, 107846 (2022)*.
- Hyesung Jo, Dae Han Wi, Taegu Lee, Yongmin Kwon, Chaehwa Jeong, Juhyeok Lee, Hionsuck Baik, Alexander J. Pattison, Wolfgang Theis, Colin Ophus, Peter Ercius, Yea-Lee Lee, Seunghwa Ryu, Sang Woo Han,\* and Yongsoo Yang\*. "Direct strain correlations at the single-atom level in three-dimensional core-shell interface structures". *Nature Communications 13, 5957 (2022)*.
- Kwanbyung Chae, Van Tu Nguyen, Sangryun Lee, Thi Quynh Phung, Yumin Sim, Maeng-Je Seong, Sangwoon Lee, Yeong Hwan Ahn, Soonil Lee, Seunghwa Ryu, Ji-Yong Park\*. "Mechanical Failures of Two-Dimensional Materials on Polymer Substrates". *Applied Surface Sciences 605, 154736 (2022)*.
- Jiyoung Jung, Youngsoo Kim, Sangryun Lee, Issam Doghri\*, and Seunghwa Ryu\*. "Improved incrementally affine method for viscoelastic-viscoplastic composite by utilizing an adaptive scheme". *Composite Structures 297, 115982 (2022)*.
- Jaemin Lee and Seunghwa Ryu\*. "Evaluating the predictive power of machine learning algorithms for shear transformation in metallic glasses using metrics for an imbalanced dataset". *Frontiers in Materials 9, 874339 (2022)*.
- Stefano Signetti, Seunghwa Ryu, and Nicola M. Pugno\*. "Impact mechanics of multilayer composite armors: analytical modeling, FEM numerical simulation, and ballistic experiments". *Composite Structures 297, 115916 (2022)*.
- Jihyuck Son, Seounghee Yun, Kundo Park, Seunghwa Ryu, and Sanha Kim\*. "Isotropic material extrusion using shell pre-printing and core post-casting". *Additive Manufacturing 58, 102974 (2022)*.
- Hyunggwi Song, Suman Timilsina, Jiyoung Jung, Taek-soo Kim\*, and Seunghwa Ryu\*. "Improving the sensitivity of the mechanoluminescence composite through functionalization for structural health monitoring". *ACS Applied Materials & Interfaces 14, 30205 (2022)*.
- In Ho Kim, Jieun Lee, Subi Choi, Jiyoung Jung, Jinwook Yeo, Tae Hong Im, Taeyeong Yun, Kyu Hyo Han, Jun Tae Kim, Seunghwa Ryu, Suk-kyun Ahn, Jiheong Kang and Sang Ouk Kim\*. "Human-muscle-inspired single fibre actuator with reversible percolation". *Nature Nanotechnology 17, 1198 (2022) Selected to feature on the front cover*.
- Wabi Demeke, Yongtae Kim, Jiyoung Jung, Jaywan Chung, Byungki Ryu\* and Seunghwa Ryu\*. "Neural network-assisted optimization of segmented thermoelectric power generators using active learning based on a genetic optimization algorithm". *Energy Reports 8, 6633 (2022)*.
- Sooun Lee, Dabin Kim, Sangryun Lee, Youg-il Kim, Siheyon Kim, Sang-Woo Kim, Yunseok Kim, Seunghwa Ryu, and Miso Kim\*. "Ambient Humidity-induced Phase Separation Fiber Morphology Engineering toward Piezoelectric Self-Powered Sensing". *Small 18, 2105811 (2022)*.
- Youngsoo Kim†, Jiyoung Jung†, Sangryun Lee, Issam Doghri\*, and Seunghwa Ryu\*. "Adaptive Affine Homogenization Method for Visco-hyperelastic Composites with Interfacial Damage". *Applied Mathematical Modelling 107, 72 (2022)*.
- Juhyeok Lee, Chaehwa Jeong, Taegu Lee, Seunghwa Ryu, Yongsoo Yang\*. "Direct observation of three-dimensional atomic structure of twinned metallic nanoparticles and their catalytic properties". *Nano Letters 22, 665 (2022)*.
- Jiyoung Jung, Yongtae Kim, Jinkyoo Park, and Seunghwa Ryu\*. "Transfer learning for enhancing the homogenization-theory-based prediction of elasto-plastic response of particle/fiber-reinforced composites". *Composite Structures 285, 115210 (2022)*.
- Kundo Park, Youngsoo Kim, Minki Kim, Chihyeon Song, Jinkyoo Park\*, and Seunghwa Ryu\*. "Designing staggered platelet composite structure with Gaussian Process Regression based Bayesian optimization". *Composites Science and Technology 220, 109254 (2022)*.
- Ji Young Kim, E. S. Park\*, Taegu Lee, Seunghwa Ryu\*, Seong-Eon Kim, Seong-Woong Kim\*. "Origin of Enhanced Room Temperature Ductility in Tial Alloys: Reducing Activation Difference of Deformation Mechanism of γ Phase". *Journal of Alloys and Compounds 899, 163307 (2022)*.
- Subin Lee†, Hadi Ghaffarian†, Wonsik Kim†, Taegu Lee, Seung Min Han\*, Seunghwa Ryu\*, and Sang Ho Oh\*. "A Study on Dislocation Mechanisms of Toughening in Cu-Graphene Nanolayered Composite". *Nano Letters 22, 188 (2022)*.
- Daanish Aleem Qureshi, Yongtae Kim, Yulong Han, Ming Guo, Seunghwa Ryu, Zhao Qin\*. "Why the Mussel Byssal Plaques are Tiny yet Strong in Attachment". *Matter 5, 710 (2022)*.

**2021**

- Aly Hassan†, Yongtae Kim†, Seunghwa Ryu\*, Benjamin Hatton, and Tobin Filleter\*. "Divisions in a Fibrillar Adhesive Increase the Adhesive Strength". *ACS Applied Materials & Interface 13, 59478 (2021)*.
- Kundo Park, Junhyeong Lee, and Seunghwa Ryu\*. "Structural health monitoring of composite materials via electrical resistance measurement and IR thermography: A review". *Structural Engineering and Mechanics 80, 563 (2021)*.
- Sangryun Lee, Jiyoung Jung, and Seunghwa Ryu\*. "Applicability of Interface Spring and Interphase Models in Micromechanics for Predicting Effective Stiffness of Polymer-Matrix Nanocomposite". *Extreme Mechanics Letters 49, 101489 (2022)*.
- Jimin Gu†, Junseong Ahn†, Jiyoung Jung, Seokjoo Cho, Jungrak Choi, Yongrok Jeong, Jaeho Park, Soonhyoung Hwang, Incheol Cho, Jiwoo Ko, Ji-Hwan Ha, Zhi-Jun Zhao, Sohee Jeon, Seunghwa Ryu, Jun-Ho Jeong\*, Inkyu Park\*. "Self-Powered Strain Sensor based on the Piezo-Transmittance of a Mechanical Metamaterial". *Nano Energy 89, 106447 (2021)*.
- Yongtae Kim+, Youngsoo Kim+, Charles Yang, Kundo Park, Grace X. Gu, and Seunghwa Ryu\*. "Deep Learning Framework for Material Design Space Exploration using Active Transfer Learning and Data Augmentation". *npj Computational Materials 7, 140 (2021)*.
- Lei Zhao+, Taegu Lee+, Seunghwa Ryu\*, Yoshifumi Oshima, Qiang Guo\*, and Di Zhang\*. "Mechanical robustness of aluminum-matrix composites rendered by graphene functionalization". *Nano Letters 21, 5706 (2021)*.
- Jamie Gravell, Sangryun Lee, Seunghwa Ryu, and Ill Ryu\*. "Effect of size and orientation on stability of dislocation networks upon torsion loading and unloading". *Acta Materialia 214, 117010 (2021)*.
- Woon Ik Park\*, Tae Wan Park, Young Joon Choi, Sangryun Lee, Seunghwa Ryu, Xiaogan Liang, Yeon Sik Jung. "Extreme-Pressure Imprint Lithography for Heat and UV-Free Direct Patterning of Rigid Nanoscale Features". *ACS Nano 15, 10464 (2021)*.
- Jiyoung Jung , Wabi Demeke , Sangryun Lee, Jaywan Chung , Byungki Ryu\*, and Seunghwa Ryu\*. "Micromechanics-based theoretical prediction for thermoelectric properties of anisotropic composites and porous media". *International Journal of Thermal Sciences 165, 106918 (2021)*.
- Sangryun Lee, Jiyoung Jung, Youngsoo Kim, Yongtae Kim, and Seunghwa Ryu\*. "Multiscale Modeling Framework to Predict Effective Stiffness of Crystalline-Matrix Nanocomposite". *International Journal of Engineering Science 161, 103457 (2021)*.
- Kyung Hoon Kim, Ahreum Hwang, Younseong Song, Wang Sik Lee, Jeong Moon, Jinyoung Jeong, NamHo Bae, Young Mee Jung, JiYoung Jung, Seunghwa Ryu, Seok Jae Lee, Bong Gill Choi, Tae Joon Kang, Kyoung Lee\*. "3D Hierarchical Nanotopography for On-site Rapid Capture and Sensitive Detection of Infectious Microbial Pathogens". *ACS Nano 15, 4777 (2021)*.
- Yongtae Kim, Seunggyu Lee, Jongchul Kim, and Seunghwa Ryu\*. "Development of Generalized Scaling Law for Underwater Explosion Using Numerical and Experimental Parametric Study". *Structural Engineering and Mechanics 77, 305 (2021)*.
- Sanghyeok Kim, Jaeho Park, Jinjae Lee, Jae-hyun Kim, Seunghwa Ryu, and Inkyu Park\*. "Mechanical Characteristics of Metal Nanoparticle Thin Film on Flexible Substrate Exposed to Saline Solution". *Nanotechnology 32, 055701 (2021)*.

**연도 표기 없음**

- 김희규, 이송호, 김준영, 이준형, 유제천, 유승화. "AI 기반 컴파운딩 소재 설계 및 사출성형 공정 최적화 전략". *화학소재 정보은행 심층보고서*.

## 과제

누리집 Research 페이지 ONGOING FUNDED PROJECTS의 10건이다. 앞의 6건은 정부과제 진행 현황, 뒤의 4건은 기업체과제 진행 현황이며 기업체과제의 지원 칸은 기업 이름이다. 과제 이름, 지원 기관, 기간, 역할은 목록 그대로이고, 기간이 2025년 12월에 끝나는 1건도 진행 목록에 적혀 있다.[^research]

- AI 기반 지능형 설계-제조 통합 연구단 (지원 과학기술정보통신부 (Ministry of Science and ICT); 기간 2025.07.-2029.12; 역할 연구단장)
- 다상소재 혁신 생산공정 연구센터 (지원 한국연구재단 (NRF of Korea) ERC; 기간 2023.06.-2030.05.; 역할 공동연구)
- 개인 맞춤형 의료진단기술 기반의 심뇌혈관 M3DT 기술개발 및 검증 (지원 식약처 컴퓨터모델링 기반 의료기기 평가체계 구축사업; 기간 2023.04.-2027.12; 역할 공동연구)
- i-Lab-on-Human 기반 체내 생체 신호 모니터링 시스템 개발 (지원 나노종합기술원; 기간 2022.01.-2025.12.; 역할 위탁연구)
- 다각도-멀티스케일 데이터 융합형 리튬이차전지 설계 인공지능 플랫폼 개발 (지원 한국연구재단 (NRF of Korea) STEAM 연구사업; 기간 2023.04.-2027.12; 역할 공동연구)
- 첨단 제조산업 생산성 향상을 위한 특화형 거대언어모델 적용 기술 개발 (지원 한국연구재단 (NRF of Korea) 개인기초연구사업; 기간 2025.09.-2028.08.; 역할 연구책임)
- AI 기반 제품 제작 최적화 (지원 EnableFusion; 기간 2025.06.-2027.05.)
- AI 기반 해석 가속화 및 물성 평가 (지원 한국타이어; 기간 2025.07.-2026.06.)
- AI 기반 설계 (지원 현대일렉트릭; 기간 2025.05.-2026.12.)
- AI 및 다물리 시뮬레이션 기반 공정 개선안 도출 (지원 한국일렉트릭; 기간 2025.09.-2026.12.)

## 수상

누리집 People 페이지 Student/Postdoc Awards 목록 가운데 괄호 안 연도가 2021–2026년인 43건이다. 학생·박사후연구원·졸업생의 장학금·펠로십·연구장려금, 학회 논문상·발표상, 학위 논문상과 우수 졸업생 상이며, 문장은 게시된 그대로다(이름 앞의 Dr.도 게시 표기). 연도만 적혀 있어 2021년 항목은 2021년 10월 전의 것일 수 있다. 교수의 수상은 위 「교수와 전문 분야」에 적었다.[^people]

- Hyeonbin Moon, 제3기 한국이공학진흥원(IPESK) 차세대 공학(연구)자 선정 (2026)
- Hyeonbin Moon, 한국연구재단 박사과정생 연구장려금 지원사업 선정 (2026)
- Inhyo Lee, 한국장학재단 대학원 대통령 과학장학금 (2026)
- Heekyu Kim, 한국장학재단 이공계 박사우수장학금 (2026)
- Hyeokjae Chae, 한국장학재단 이공계 석사우수장학금 (2026)
- Jongwon Park, 2026 KSME-CAE conference, 학생경진대회 은상 (2026)
- Hugon Lee, 2025 KSME-CAE conference, 대한기계학회 CAE부문 우수논문상 (2026)
- Dr. Junhyeong Lee, 2025 KSME-CAE conference, 대한기계학회 CAE부문 우수논문상 (2026)
- Dr. Donggeun Park, CoE Best PhD Dissertation Award, KAIST Colleage of Engineering (2026) (공과대학 박사학위 최우수논문상)
- Dr. Junhyeong Lee, Excellent PhD Thesis Award, KSME, 대한기계학회 본부 우수학위논문상 (2026)
- Dr. Donggeun Park, Excellent PhD Thesis Award, KSME, 대한기계학회 CAE부문 우수학위논문상 (2026)
- Junhyeong Lee, Woodeok Fellowship (2025)
- Dr. Wabi Demeke, UW (University of Wyoming) Distinguished Doctoral Fellow For AI-Enabled Interdisciplinary Research (2025)
- Heekyu Kim, BK Paper Award, KAIST Mechanical Engineering (2025) (BK논문상)
- Hyeonbin Moon, Excellent M.S. Graduate Award, KAIST Mechanical Engineering (2025) (기계공학과 석사우수 졸업생)
- Jinun Byun, KIM Student of the Year, KIM, 대한금속재료학회 추계학술대회 학생세션 최우수 논문상 (2025)
- Donggeun Park, 제2기 한국이공학진흥원(IPESK) 차세대 공학(연구)자 선정 (2025)
- Inhyo Lee, 제2기 한국이공학진흥원(IPESK) 차세대 공학(연구)자 선정 (2025)
- Inhyo Lee, KIM Student of the Year, KIM, 대한금속재료학회 춘계학술대회 학생세션 최우수 논문상 (2025)
- Dr. Jinwook Yeo, Excellent PhD Thesis Award, KSME, 대한기계학회 본부 우수학위논문상 (2025)
- Donggeun Park, 2024 KSME-CAE conference, 대한기계학회 본부 우수논문상 (2025)
- Hyunbin Moon, 2024 KSME-CAE conference, 대한기계학회 CAE부문 우수논문상 (2025)
- Hugon Lee, 2024 KSME-CAE conference, 대한기계학회 CAE부문 우수논문상 (2025)
- Junhyeong Lee, 2024 KSME-CAE conference, 대한기계학회 CAE부문 우수논문상 (2025)
- Inhyo Lee, SBS Scholarship Foundation Scholarship (SBS 장학재단 스칼라십) (2024)
- Jinun Byun, OK Scholarship (OK배정장학재단 장학생) (2024)
- Dr. Jiyoung Jung, Overseas Postdoc fellowship, National Research Foundation of Korea (한국연구재단) (2024)
- Dr. Kundo Park, Sejong Science Fellowship (세종과학펠로우쉽) (2024)
- Dr. Kundo Park, Excellent PhD Graduate Award, KAIST Mechanical Engineering (2024) (기계공학과 박사우수 졸업생/기계동문회장상)
- Dr. Kundo Park, Excellent PhD Thesis Award, KSME-CAE division (대한기계학회 부문 우수학위논문상) (2024)
- Junhui Jo, Best Poster Award, KMSM (2023) (한국멀티스케일역학회 학술대회 최우수 포스터상)
- Dr. Jiyoung Jung, Excellent PhD Graduate Award, KAIST Mechanical Engineering (2023) (기계공학과 박사우수 졸업생/기계동문회장상)
- Dr. Jiyoung Jung, Excellent PhD Thesis Award, KSME-CAE division (대한기계학회 부문 우수학위논문상) (2023)
- Dr. Jiyoung Jung, Excellent Presentation Award for 2022 KSME-CAE conference, KSME-CAE division (대한기계학회-CAE부문 우수발표상) (2023)
- Dr. Jiyoung Jung, CoE PhD Dissertation Award, KAIST Colleage of Engineering (2023) (공과대학 박사학위 우수논문상)
- Jiyoung Jung, Woodeok Fellowship (2022)
- Dr. Yongtae Kim, Excellent PhD Graduate Award, KAIST Mechanical Engineering (2022) (기계공학과 박사우수 졸업생/기계동문회장상)
- Dr. Yongtae Kim, Excellent PhD Thesis Award, KSME (대한기계학회 본부 우수학위논문상) (2022)
- Dr. Yongtae Kim, Excellent Paper Award for 2021 KSME, KSME-CAE division (대한기계학회 춘계학회 우수논문상) (2022)
- Dr. Hyunggwi Song, Excellent Presentation Award for 2021 KSME-CAE conference, KSME-CAE division (대한기계학회-CAE부문 우수발표상) (2022)
- Dr. Youngsoo Kim, Excellent PhD Graduate Award, KAIST Mechanical Engineering (2021) (기계공학과 박사우수 졸업생/ICEM학술상)
- Jiyoung Jung, Kim Younghan Global Leader Fellowship (2021)
- Dr. Hyunggwi Song, G-core Postdoctoral Fellowship, KAIST (2021)

## 연락과 위치

- 교수실: 기계동(N7) 3205[^meprof] (교수 페이지 표기 N7-3, Room 3205 (3rd floor))[^prof]
- 교수 전화: 042-350-3019[^meprof][^prof]
- 교수 이메일: ryush@kaist.ac.kr[^home][^prof][^meprof]
- 첫 화면은 연구실 입학, 연구 참여, 학술·산업 협력에 관심 있는 사람은 유승화 교수에게 연락하라고 안내한다.[^home]
[^p1]: J. Lee 외, S. Ryu, Materials Horizons 10, 5436-5456 (2023). <https://doi.org/10.1039/d3mh00039g> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: S. Lee 외, S. Ryu, Materials Horizons 13, 6500-6516 (2026). <https://doi.org/10.1039/d6mh00239k> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: H. Moon 외, S. Ryu, npj Computational Materials 11, 272 (온라인 2025-08-22). <https://doi.org/10.1038/s41524-025-01769-1> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: S. Kang, S. Kang, S. Kim, S. Ryu, Materials Horizons 13, 9028-9041 (2026). <https://doi.org/10.1039/d6mh00630b> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: D. Park, H. Moon, S. Ryu, npj Artificial Intelligence 2, 10 (온라인 2026-01-20). <https://doi.org/10.1038/s44387-025-00057-z> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: D. Park 외, S. Ryu, Journal of Intelligent Manufacturing 37, 1075-1091 (온라인 2025-02-27). <https://doi.org/10.1007/s10845-025-02584-7> 초록 기준(논문 페이지 게시 초록).
[^p7]: H. Lee 외, S. Ryu, Journal of Physics: Condensed Matter 36, 505702 (온라인 2024-09-23). <https://doi.org/10.1088/1361-648x/ad765e> 초록 기준.
[^p8]: J. Jo 외, S. Ryu, International Journal of AI for Materials and Design 1, 48 (온라인 2024-07-30). <https://doi.org/10.36922/ijamd.3539> 초록 기준.
[^home]: 연구실 누리집 첫 화면 <https://sites.google.com/site/seunghwalab> (누리집 제목 지능형 설계 및 제조 연구실, AiM⁴ Lab, About Us, Research & Vision, Join & Collaborate, PRISM-AI Center, 2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <https://sites.google.com/site/seunghwalab/professor_1> (직위, Email, Phone, Office, EDUCATION, EMPLOYMENTS, SERVICE, AWARDS and HONORS, 2026-10-23 열람)
[^people]: 연구실 누리집 People 페이지 <https://sites.google.com/site/seunghwalab/staff> (구성원 카드, Student/Postdoc Awards, Alumni의 PhD Degree 1–16번·MS Degree 1–27번·Postdoctoral Researchers 1–7번·URP Students 1–3번, 2026-10-23 열람)
[^research]: 연구실 누리집 Research 페이지 <https://sites.google.com/site/seunghwalab/research> (VISION, OBJECTIVES, 연구 갈래 1–5, ONGOING FUNDED PROJECTS, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publications 페이지 <https://sites.google.com/site/seunghwalab/publications> (International Journal 2021–2026년 구역 83–202번(191번 제외)과 그 이전 구역, Domestic Journal 8·9번, Books 2번, 2026-10-23 열람)
[^methods]: 연구실 누리집 Publications by Methods 페이지 <https://sites.google.com/site/seunghwalab/publications/publications-by-methods> (M1–M5 분류와 편수, 묶음별 국문 소개, Last Update: October 20th 2026, 2026-10-23 열람)
[^apps]: 연구실 누리집 Publications by Application Areas 페이지 <https://sites.google.com/site/seunghwalab/publications/publications-by-application-areas> (A1–A5 분류와 편수, 묶음별 국문 소개, Last Update: Oct 20th 2026, 2026-10-23 열람)
[^teach]: 연구실 누리집 Teaching 페이지 <https://sites.google.com/site/seunghwalab/teaching> (Courseworks at KAIST, Spring 2021–Spring 2024 강의, 2026-10-23 열람)
[^melist]: KAIST 기계공학과 교수진 목록 2쪽 <https://me.kaist.ac.kr/team/team_010100.html?page=2&plist=&find_field=&find_word=&find_state=&find_ordby=&conf=&mode=1> (유승화 교수 항목의 직위, 연구분야, 연구실, 최종학위, 2026-10-23 열람)
[^meprof]: KAIST 기계공학과 교수 상세(유승화) <https://me.kaist.ac.kr/pop/team.html?uid=37&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 연구실 웹사이트, E-mail, Office, Phone, 2026-10-23 열람)
[^meres]: KAIST 기계공학과 연구분야 안내 소재/역학/제조 <https://me.kaist.ac.kr/research/research_010200.html> 와 헬스케어/나노/광학 <https://me.kaist.ac.kr/research/research_010400.html> (유승화 교수 항목의 연구주제, 주요 응용 산업, 연구실, 웹사이트, 2026-10-23 열람)

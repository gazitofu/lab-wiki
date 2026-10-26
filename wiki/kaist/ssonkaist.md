# Web Security & Privacy Lab (WSP Lab)

**KAIST 전산학부·정보보호대학원·안보과학기술대학원 · 손수엘 부교수**

- 분야: 웹 보안·프라이버시, 웹 응용·브라우저의 취약점을 찾는 프로그램 분석과 시험 도구(퍼징, 차등 시험), 기계학습 모델(대형 언어 모델 포함)의 보안·프라이버시, 웹 서비스의 보안·프라이버시 결함 분석, 온라인 사기·범죄 활동 분석
- 대분야: 컴퓨팅·AI
- 태그: 소프트웨어·시스템 보안[^research][^gs][^p4], 프로그램 분석·검증[^gs][^cs][^gsis], 퍼징[^gst][^p3], 대형 언어 모델[^p1][^p2][^p5], AI·기계학습 보안·프라이버시[^gsresearch]
- 홈페이지: <https://wsp-lab.github.io/> (교수 개인 누리집 <https://sites.google.com/site/ssonkaist/>)
- 근거와 출처: [WSP Lab 근거 페이지](ssonkaist-sources.md)

> 웹 보안과 프라이버시에 관한 여러 주제를 연구하는 전산학부 연구실이다.[^research][^gs] 새로운 착상을 실제 서비스에 구현해 인터넷 서비스를 더 안전하고 사적으로 만드는 것을 목표로 든다.[^research]

## 무엇을 연구하나

연구실은 KAIST 전산학부 손수엘 교수의 연구실이다. 누리집은 연구실 이름을 KAIST WSP Lab(KAIST Web Security & Privacy Lab)으로 적고[^home], 안보과학기술대학원 교수진 목록은 연구실을 Web Security & Privacy (WSP) Lab으로 적는다.[^gst] 교수 개인 누리집도 교수가 이끄는 연구 그룹을 WSP Lab으로 적는다.[^gs]

누리집 Research 페이지는 연구실이 웹 보안과 프라이버시(privacy, 개인에 관한 정보가 본인의 뜻과 달리 수집·공개·이용되지 않도록 지키는 일)에 관한 여러 주제를 연구하며, 새로운 착상을 실제 서비스에 구현해 인터넷 서비스를 더 안전하고 사적으로 만들고자 한다고 적는다.[^research] 같은 페이지는 연구 주제를 네 갈래로 나눈다. 기계학습 모델의 보안·프라이버시 위험 분석(R1), 서버 쪽·클라이언트 쪽 웹 응용 프로그램의 취약점(vulnerability, 공격자가 악용할 수 있는 시스템·소프트웨어의 약점)을 찾는 도구 개발(R2), 웹 서비스의 보안·프라이버시 취약점 찾기(R3), 인터넷에서 일어나는 온라인 사기·범죄 활동 분석(R4)이다.[^research] 교수 개인 누리집의 Research 페이지도 같은 네 갈래를 적는다.[^gsresearch]

교수 개인 누리집은 연구 관심사로 웹 보안·프라이버시, 취약점을 찾기 위한 정적·동적 프로그램 분석(program analysis, 프로그램을 실행하지 않고 코드를 살피거나 실행하면서 동작을 살펴 그 성질과 결함을 알아내는 기술), 기계학습 보안·프라이버시를 든다.[^gs] 전산학부 교수 목록은 교수의 연구 분야를 웹보안, 프라이버시, 프로그램 분석으로, 정보보호대학원 교수진 목록은 웹보안, 개인정보 보호, 프로그램 분석으로 적는다.[^cs][^gsis]

## 주요 연구 주제

### 1. 기계학습 모델의 보안·프라이버시 위험

Research 페이지의 첫 갈래(R1)는 기계학습 모델의 보안·프라이버시 위험 분석이다.[^research] 교수 개인 누리집 Research 페이지는 이 갈래의 과제로 「Penetration Security Testing of ML Model Vulnerabilities and Defense」(IITP 전문연구실)를 들고, 최근 기계학습 모델의 여러 보안·프라이버시 위협을 조사하며 침투 보안 시험(penetration security testing, 공격자의 방식으로 시스템을 모의 공격해 보안 약점을 찾는 평가)으로 주어진 기계학습 모델의 강건성을 평가하는 도구를 구현한다고 적는다.[^gsresearch] Research 페이지는 이 갈래의 대표 연구로 대표 논문 1과 함께, 모델 설명(model explanation, 기계학습 모델이 어떤 입력 특징을 근거로 판단했는지 보여 주는 정보)에서 원래 이미지를 복원하는 공격의 위험을 줄이는 방어 틀을 다룬 NeurIPS 2022 논문(GNIME), 심층 신경망에 심은 트리거 집합 기반 워터마크의 강건성을 평가한 TDSC 2022 논문을 든다.[^research]

대표 논문 1·2는 대형 언어 모델(LLM, 대량의 글로 학습해 글을 이해하고 만들어 내는 인공지능 언어 모델)의 프라이버시와 안전을 다룬다.[^p1][^p2] 대표 논문 1은 사용자의 개인 데이터로 미세조정(fine-tuning, 이미 학습된 모델을 특정 과제나 데이터에 맞게 추가로 학습시키는 일)한 언어 모델이 기억한 개인 식별 정보(PII, 이름·전화번호·이메일 주소 등 특정 개인을 알아볼 수 있게 하는 정보)가 새어 나갈 위험을 평가하려고, 이런 정보를 끌어내는 질문문(프롬프트)을 자동으로 만들고 고르는 틀 Private Investigator를 내놓았다.[^p1] 대표 논문 2는 전문가 혼합(MoE, Mixture-of-Experts, 여러 하위 신경망(전문가) 가운데 입력마다 일부를 골라 계산에 쓰는 모델 구조) LLM을 미세조정하면 해로운 입력을 안전에 중요한 전문가로 보내는 경로 결정이 바뀌어 해로운 미세조정 공격에 취약해지는 문제를 다뤄, 이 경로를 지키는 안전한 미세조정 방법 SafeMoE를 제안했다.[^p2] 누리집 Publications 목록에는 이 밖에도 LLM이 안전 정렬을 잊게 하는 것(Unlearning Safety Alignment)을 제목에 단 USENIX Security 2025 논문(Refusal Is Not an Option), 전문가 혼합 LLM의 안전성을 다룬 ACSAC 2025 논문(MoEvil), 캡션 없는 멤버십 추론을 제목에 단 ICLR 2026 논문(No Caption, No Problem), 인페인팅 조작에서 이미지를 보호하는 방법을 제목에 단 ICLR 2025 논문(AdvPaint), 신경망 워터마킹을 다룬 ICML 2023 논문(Margin-based Neural Network Watermarking)이 있다.[^pubs] Publications 목록은 MoEvil에 Distinguished paper award를 표시하고, 누리집 첫 화면 소식(2025년 12월)은 ACSAC'25 Distinguished Paper Award 수상을 알린다.[^pubs][^home]

### 2. 웹 응용 프로그램의 취약점을 찾는 도구

Research 페이지의 두 번째 갈래(R2)는 서버 쪽·클라이언트 쪽 웹 응용 프로그램의 취약점을 찾는 도구 개발이다.[^research] 안보과학기술대학원 교수진 목록도 교수의 세부 연구 분야에 웹취약점탐지와 브라우저 퍼즈 테스팅(fuzz testing, 퍼징이라고도 하며, 프로그램에 많은 입력을 자동으로 넣어 보며 오류와 취약점을 찾는 시험)을 적는다.[^gst] Research 페이지는 이 갈래의 대표 연구로 대표 논문 4와 함께, PHP 객체 주입 취약점을 다룬 USENIX Security 2022 논문(FUGIO), 강화학습으로 반사형 교차 사이트 스크립팅(XSS, 공격자가 웹페이지에 악성 스크립트를 끼워 넣어 다른 사용자의 브라우저에서 실행되게 하는 공격) 취약점을 자동으로 찾는 WWW 2022 논문(Link), 코드 속성 그래프(code property graph, 프로그램의 문법 구조·실행 흐름·데이터 의존 관계를 하나로 합쳐 나타낸 그래프)로 취약한 코드 복제(code clone, 복사되어 여러 곳에 쓰인 코드 조각)를 찾는 것을 제목에 단 WWW 2022 논문(HiddenCPG), 모바일 광고 사기를 일으키는 앱 모듈을 찾는 NDSS 2021 논문(The Abuser Inside Apps), 2020년 논문 2편을 든다.[^research][^gsresearch]

대표 논문 3·4는 웹 응용과 브라우저의 결함을 자동으로 찾는 시험 도구다.[^p3][^p4] 대표 논문 3은 웹 응용을 대상으로 하는 닫힌 상자 퍼징(closed-box fuzzing, 프로그램 내부 코드를 보지 않고 입력과 응답만으로 하는 퍼징)에 피드백 장치가 없어 입력 탐색이 제한되는 문제 등을 다뤄, 웹 응답에서 피드백 신호를 추론해 퍼징을 이끄는 웹 퍼징 도구 Zelda를 내놓았다.[^p3] 대표 논문 4는 웹사이트가 브라우저에 자바스크립트 실행을 제한하도록 지시하는 콘텐츠 보안 정책(CSP, Content Security Policy, 웹페이지에서 실행할 수 있는 스크립트와 불러올 수 있는 자원을 웹사이트가 브라우저에 지정하는 보안 규칙)을 브라우저가 잘못 적용하는 버그를, 차등 시험(differential testing, 같은 입력을 같은 기능의 여러 구현에 넣고 결과를 비교해 어긋나는 곳에서 버그를 찾는 시험 방법)으로 찾는 틀 DiffCSP를 제안했다.[^p4] 누리집 Publications 목록에는 Trusted Types로 DOM 기반 교차 사이트 스크립팅 공격을 탐지하는 것을 제목에 단 AsiaCCS 2025 논문(TrustyMon), 웹 에이전트의 간접 프롬프트 주입 위험 평가를 제목에 단 ISSTA 2026 논문(AgentBreaker), 광고·추적기 차단을 위한 자바스크립트 코드 속성 그래프 분류를 제목에 단 CCS 2023 논문(AdCPG)도 있다.[^pubs]

### 3. 웹 서비스의 보안·프라이버시 결함

Research 페이지의 세 번째 갈래(R3)는 웹 서비스의 보안·프라이버시 취약점 찾기이고, 이 갈래의 대표 연구로 2018년과 2019년 논문 2편을 든다.[^research]

대표 논문 5·6은 새로운 웹 기능과 메시징 서비스의 보안·프라이버시 위험을 분석한다.[^p5][^p6] 대표 논문 5는 LLM과 웹 에이전트(사용자 대신 웹페이지를 읽고 클릭·입력 같은 작업을 수행하는 인공지능 프로그램)를 통합한 에이전트형 브라우저와 확장 프로그램이 사이트 격리(site isolation, 출처가 다른 웹페이지를 서로 다른 프로세스에서 처리해 한 사이트가 다른 사이트의 데이터에 접근하지 못하게 하는 브라우저 보안 구조)를 어떻게 구현하는지 분석해, 프로세스 간 통신 채널을 제대로 고려하지 않아 생기는 위험을 밝히고 방어 지침을 내놓았다.[^p5] 대표 논문 6은 연락처 찾기, 단일 로그인(SSO, 한 번의 로그인으로 여러 서비스를 쓸 수 있게 하는 인증 방식) 기반 계정 연결, 주변 사용자 검색 같은 메시징 앱 기능이 여러 앱에 흩어진 사용자 개인정보를 서로 잇게 하는 프라이버시 위협을 분석하고, 위협을 줄이는 완화 전략을 제안했다.[^p6] 누리집 Publications 목록에는 광고 차단기의 필터링 논리를 제목에 단 CCS 2026 채택 논문(Overloading Ad Blockers), WebVR 광고 사기와 제3자 광고 격리를 제목에 단 USENIX Security 2021 논문(AdCube), 광고 차단기 우회를 제목에 단 ACSAC 2024 논문(You Only Perturb Once)도 있다.[^pubs]

### 4. 온라인 사기·범죄 활동 분석

Research 페이지의 네 번째 갈래(R4)는 인터넷에서 일어나는 온라인 사기·범죄 활동 분석이고, 이 갈래의 대표 연구로 대표 논문 7·8과 다크웹의 피싱 사이트를 측정한 2019년 논문을 든다.[^research] 안보과학기술대학원 교수진 목록의 세부 연구 분야에도 피싱을 활용한 사이버공격이 있다.[^gst]

대표 논문 7은 가짜 계정을 대량으로 만들어 악용하는 시빌 공격(Sybil attack)에서, 적대적 공격(adversarial attack, 기계학습 모델이 잘못 판단하도록 일부러 조작한 입력이나 데이터를 쓰는 공격)으로 기존 집단 분류(collective classification, 그래프에서 이웃 노드와의 관계를 함께 고려해 노드의 종류를 정하는 분류 방법)를 피해 가는 시빌 계정을 가려내는 강건한 집단 분류 틀 RICC를 제안했다.[^p7] 대표 논문 8은 보이스피싱 앱 1,017개를 분석해 새로운 피싱 기능을 밝히고, 피싱 앱이 실행 중에 하는 피싱 동작을 탐지해 막는 안드로이드 시스템 수준 서비스 HearMeOut을 제안했다.[^p8] 누리집 Publications 목록에는 참조 기반 피싱 탐지기의 강건성 평가를 제목에 단 AsiaCCS 2025 논문(Evaluating Robustness of Reference-based Phishing Detectors)도 있다.[^pubs]

## 대표 논문

손수엘 교수가 저자인 2021–2026년 논문 가운데 네 연구 갈래(기계학습 모델의 보안·프라이버시 위험, 웹 응용 프로그램의 취약점을 찾는 도구, 웹 서비스의 보안·프라이버시 결함, 온라인 사기·범죄 활동 분석)에서 초록을 확인할 수 있는 여덟 편을 골랐다. 여덟 편 모두 교수가 마지막 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [Private Investigator: Extracting Personally Identifiable Information from Large Language Models Using Optimized Prompts](https://wsp-lab.github.io/papers/keum-privateinvestigator-sec25.pdf) · 34th USENIX Security Symposium (USENIX Security 2025) | 학습 데이터 추출 공격 연구는 언어 모델 생태계에 심각한 위협이 있음을 보여 왔다. 사전학습한 언어 모델을 사용자의 개인 데이터로 미세조정하는 흔한 배포 상황에서, 공격자는 미세조정된 모델이 기억한 개인 식별 정보(PII)를 빼내려 할 수 있다. 앞선 연구는 손으로 만들거나 외부에서 가져온 프롬프트로 모델이 PII를 내놓게 해 이 위험을 보였지만, 공격자가 PII 추출에 알맞은 프롬프트를 어떻게 설계할지는 거의 다뤄지지 않았다. Private Investigator는 미세조정에 쓰인 PII를 대상 언어 모델에서 끌어내도록 프롬프트를 최적화하는 공격 틀이다. 다양한 맥락을 탐색해 모델이 PII를 되도록 많이 내놓게 하는 프롬프트 생성 방법과, 유망한 프롬프트를 먼저 쓰는 선택 전략을 더했다. 평가에서 기존 공격보다 최대 이메일 주소 1,254개, 전화번호 634개, 사람 이름 5,087개를 더 추출했다.[^p1] | 1저자 Seongho Keum, 마지막 저자 손수엘 (5명) |
| 2 | 2026 | [SafeMoE: Safe Fine-Tuning for MoE LLMs by Aligning Harmful Input Routing](https://wsp-lab.github.io/papers/kim-safemoe-iclr26.pdf) · 14th International Conference on Learning Representations (ICLR 2026) | 최근 LLM은 효율을 위해 전문가 혼합(MoE) 구조를 점점 더 많이 쓴다. MoE 기반 LLM은 해로운 입력을 안전에 중요한 전문가로 보내는 피상적인 안전 장치에 크게 기댄다. 저자들의 분석에 따르면 미세조정 뒤 해로운 입력의 경로 결정이 크게 바뀌어, 해로운 미세조정(HFT) 공격에 취약해진다. 단일 구조 LLM을 위해 설계된 기존 방어는 이 경로 변화를 막지 못해 MoE LLM에는 효과가 떨어진다. SafeMoE는 MoE LLM에 맞춘 안전한 미세조정 방법으로, 미세조정한 모델의 경로 가중치와 처음 안전 정렬된 모델의 경로 가중치 사이의 차이에 벌점을 주어, 해로운 입력이 안전에 중요한 전문가로 가는 경로를 지킨다. 7B에서 141B 매개변수의 공개 MoE LLM 실험에서 HFT 공격을 효과적으로 줄였다. 예를 들어 OLMoE의 유해성 점수를 62.0에서 5.0으로 낮추면서 과제 성능 저하를 1% 안으로 유지했고, 추가 비용은 2%였다. 최신 방어 방법보다 크게 앞섰고, gpt-oss와 Llama 4 같은 최근 대규모 MoE LLM에서도 효과를 유지했다.[^p2] | 1저자 Jaehan Kim, 마지막 저자 손수엘 (4명) |
| 3 | 2026 | [Zelda: Feedback-driven Closed-box Fuzzing for Identifying Web Application Vulnerabilities](https://doi.org/10.1145/3774904.3792378) · Proceedings of the ACM Web Conference 2026 (WWW 2026) | 실용적 영향이 있는데도 웹 응용에 대한 닫힌 상자 퍼징은 연구가 적다. 이 논문은 닫힌 상자 웹 퍼징의 두 가지 근본 한계, 곧 피드백 장치가 없어 입력 공간 탐색이 제한되는 점과 취약점을 얕게 확인하는 데서 오는 비효율적인 공략 전략을 살핀다. Zelda는 이 한계를 다루는 닫힌 상자 웹 퍼저로, 웹 응답에서 피드백 신호를 추론해 퍼징 과정을 이끈다. 또 탐색 단계에 따라 경로 탐색과 취약점 공략을 위한 두 입력 생성 전략을 조율해, 페이지 안 코드 커버리지(시험 중에 실제로 실행된 코드의 범위)와 취약점 확인을 함께 돕는다. 실제 응용 15개와 벤치마크 집합 9개에서 평가한 결과 피드백 장치와 전략이 실제 웹 취약점 발견에 효과적이었다. Zelda는 취약점 182개를 찾아 최신 웹 퍼저 6개보다 앞섰고, 실제 환경에서 그때까지 보고되지 않은 취약점을 더 찾아 CVE(공개된 보안 취약점마다 붙이는 공용 식별 번호) 29개를 받았다.[^p3] | 1저자 Soyoung Lee, 마지막 저자 손수엘 (4명) |
| 4 | 2023 | [DiffCSP: Finding Browser Bugs in Content Security Policy Enforcement through Differential Testing](https://doi.org/10.14722/ndss.2023.24200) · Proceedings 2023 Network and Distributed System Security Symposium (NDSS 2023) | 콘텐츠 보안 정책(CSP)은 웹 위협을 줄이는 사실상의 보안 장치의 하나로, 많은 웹사이트가 주로 교차 사이트 스크립팅(XSS) 공격을 줄이려고 브라우저의 자바스크립트(JS) 실행을 제한하는 CSP를 쓴다. 그러나 브라우저의 CSP 적용 버그가 있으면 공격자가 배포된 CSP를 우회할 수 있다. CSP 명세가 지시어를 늘려 가며 복잡해지면서 올바른 적용 동작을 구현하기도 어려워졌지만, CSP 적용 버그를 체계적으로 찾는 연구는 적었다. DiffCSP는 JS 실행과 관련된 CSP 적용 버그를 찾는 첫 차등 시험 틀이다. CSP와, JS 조각을 실행하는 알려진 모든 방법을 담은 HTML 사례 집합을 만들고, 만든 정책마다 각 HTML 사례를 여러 브라우저에서 실행해 서로 어긋나는 실행 결과를 모은다. 많은 실행 결과는 결정 트리(조건 질문을 차례로 따라가며 자료를 나누는 분류 모형)로 분석해 어긋남의 공통 원인을 찾는다. 보안 버그 29개와 기능 버그 8개를 찾았고, 그 가운데 3개가 CSP 명세의 불분명한 서술 때문임을 보였다. 잘못된 CSP 상속과 해시 처리 같은 공통 근본 원인도 밝혔다. 같은 CSP를 브라우저마다 완전히 다르게 해석하는 위험한 경향을 확인했고, 이 결과는 Chrome과 Safari를 포함한 주요 브라우저의 보안 버그 12개를 고치는 데 이바지했다.[^p4] | 1저자 Seongil Wi, 마지막 저자 손수엘 (5명) |
| 5 | 2026 | [Site Isolation is Dead: How Site Isolation is Broken in Agentic Browsers and Extensions](https://doi.org/10.1109/sp63933.2026.00241) · 2026 IEEE Symposium on Security and Privacy (SP) | 사이트 격리는 현대 웹 브라우저 보안의 핵심이다. 출처가 다른 신뢰할 수 없는 웹페이지를 화면에 그리는 렌더러 프로세스(브라우저에서 웹페이지의 내용을 해석해 표시하는 실행 단위)를 엄격히 나눠, 악성 웹사이트가 다른 웹사이트의 민감한 데이터에 접근하지 못하게 한다. 그러나 브라우저가 복잡한 사용자 작업을 자동화하려고 LLM과 웹 에이전트를 통합하면서, 에이전트가 격리 경계를 넘어 LLM 기반 동작을 해야 하는 일이 잦아져 새로운 보안 위험이 생긴다. 이런 에이전트형 브라우저가 신뢰할 수 없는 웹 콘텐츠에서 에이전트 동작을 지키는 보안 장치를 어떻게 구현하는지는 그동안 연구되지 않았다. 이 논문은 공개 소스 에이전트형 브라우저 2개와 에이전트형 확장 프로그램 7개의 보안 설계를 분석해, 권한을 가진 프로세스가 사용자 프롬프트와 에이전트 동작을 관리하고 신뢰할 수 없는 렌더러 프로세스는 격리되며, 프로세스 간 통신(IPC) 채널이 둘을 잇는 공통 구조를 찾았다. 이를 바탕으로 IPC 채널을 이용한 두 가지 종단 간 공격(악성 프롬프트 주입, LLM 관련 데이터 유출)을 보였다. 시험한 모든 에이전트형 브라우저와 확장 프로그램이 이 공격에 취약했고, 기존 구현이 IPC 채널을 제대로 고려하지 못함이 드러났다. 끝으로 에이전트형 브라우저와 확장 프로그램의 사이트 격리를 강화하는 방어 지침을 내놓았다.[^p5] | 1저자 Suyoung Lee, 마지막 저자 손수엘 (7명) |
| 6 | 2026 | [Connecting the Dots: An Investigative Study on Linking Private User Data Across Messaging Apps](https://doi.org/10.14722/ndss.2026.230556) · Proceedings 2026 Network and Distributed System Security Symposium (NDSS 2026) | 모바일 메시징 앱은 일상 소통의 일부가 되었다. 메시징 앱은 사용자 참여와 사용자 기반을 늘리려고 주변 사용자 검색, 연락처 찾기, 단일 로그인(SSO) 기반 계정 연결 같은 기능을 준다. 이 기능 덕분에 사용자는 한 기기에서 여러 메시징 앱을 쓰지만, 여러 앱에 걸친 사용자 개인정보가 서로 이어지는 프라이버시 위험도 생기며, 이 위험은 연구가 적었다. 이 논문은 KakaoTalk, Telegram, WhatsApp, Signal, Tinder 등 한국에서 널리 쓰이는 메시징 앱의 프라이버시 위협을 깊이 분석해, 연락처 찾기·SSO 기반 계정 연결·주변 사용자 검색 기능을 이용한 구체적 공격을 보였다. 나아가 이 공격들을 이어 첫 플랫폼 간 연결 공격을 수행해, 많은 비표적·표적 사용자의 이름에서 익명성을 벗기고 물리적 위치를 평균 오차 324미터로 추정할 수 있음을 보였다. 허용적인 연락처 찾기 정책에서는 전화번호와 프로필 이미지가 여러 앱의 개인정보를 잇는 연결 열쇠가 되므로 연락처 찾기를 안전하게 하는 일이 중요하다고 강조하고, 위협을 줄이는 완화 전략을 논의하고 제안했다.[^p6] | 1저자 Junkyu Kang, 마지막 저자 손수엘 (4명) |
| 7 | 2023 | [RICC: Robust Collective Classification of Sybil Accounts](https://doi.org/10.1145/3543507.3583475) · Proceedings of the ACM Web Conference 2023 (WWW 2023) | 시빌 공격은 가짜(시빌) 계정을 대량으로 만들어 악용해 웹 서비스의 신뢰와 무결성을 해치는 심각한 위협이다. 앞선 연구는 시빌 계정을 찾으려고 집단 분류를 쓰자고 제안했지만, 최근 연구는 최신 적대적 공격이 기존 집단 분류 방법을 피할 수 있음을 보였다. RICC는 적대적 공격으로 만든 시빌 계정을 가려내도록 설계한 강건한 집단 분류 틀이다. 이 공격이 공격 예산을 최적화하려고 대상 집단 분류 모델에 맞춰져 있어서, 계정의 사전 평판 점수를 매기는 데 쓴 원래 학습 집합과 다른 새 학습 집합을 쓰면 적대적 시빌 계정의 분류 결과가 크게 바뀌는 경우가 많다는 관찰을 이용한다. 이에 따라 라운드마다 무작위로 뽑은 서로 다른 학습 집합에 걸쳐 분류 결과를 안정시켜 강건성을 얻는다. Enron, Facebook, Twitter_S, Twitter_L 데이터 집합에서 적대적 시빌 계정을 찾을 때 거짓 음성률(실제 시빌 계정을 정상 계정으로 잘못 분류하는 비율)은 각각 0.01, 0.11, 0.00, 0.01이었고, 원래 과제인 시빌 계정 탐지에서도 AUC(분류 모형이 두 부류를 가려내는 성능을 나타내는 지표)가 각각 0.99, 1.00, 0.89, 0.74였다. 기존의 모든 시빌 탐지 방법보다 크게 앞섰다.[^p7] | 1저자 Dongwon Shin, 마지막 저자 손수엘 (3명) |
| 8 | 2022 | [HearMeOut: Detecting Voice Phishing Activities in Android](https://doi.org/10.1145/3498361.3538939) · Proceedings of the 20th Annual International Conference on Mobile Systems, Applications and Services (MobiSys 2022) | 한국에서는 보이스피싱 앱이 나오면서 보이스피싱이 늘어, 2020년 한 해 피해자가 34,527명, 금전 피해가 약 5억 9,800만 달러에 이르렀다. 그러나 이런 앱이 구현한 보이스피싱 기능은 연구가 적었다. 저자들은 보이스피싱 앱 1,017개를 분석해 발신 전화 전환, 통화 화면 덮어씌우기, 가짜 통화 음성이라는 새 피싱 기능을 밝혔다. 피해자가 건 전화의 수신자를 바꾸는 발신 전화 전환이 보이스피싱에 결정적 역할을 하며, 사용자 연구에서 참여자의 87%가 전환이 일어났을 때 수신자가 바뀐 것을 알아차리지 못했다. 이 기능들의 구현을 살펴 정상 앱의 비슷한 동작과 악성 동작을 구분하고, 피싱 앱이 실행 중에 하는 피싱 동작을 탐지해 막는 안드로이드 시스템 수준 서비스 HearMeOut을 제안했다. HearMeOut은 피싱 동작 분류에서 거짓 양성(정상 동작을 피싱으로 판정)과 거짓 음성(피싱 동작을 놓침) 없이 높은 정확도를 보였고 평균 지연은 0.36ms로 알아차릴 수 없는 수준이었다. 사용자 연구에서는 능동 경고로 참여자 100%가 피싱을 당하지 않게 했다. 안드로이드 시스템 변경 권고와 함께 실용적인 완화 방안을 내놓았다.[^p8] | 1저자 Joongyum Kim, 마지막 저자 손수엘 (5명) |

## 교수와 전문 분야

손수엘 교수(Sooel Son)는 KAIST 전산학부 부교수다. 전산학부 교수 목록은 직위를 부교수로, 연구 분야를 웹보안, 프라이버시, 프로그램 분석으로 적는다.[^cs] 정보보호대학원 교수진 목록은 교수를 전산학부와 정보보호대학원 소속으로 싣는다.[^gsis] 안보과학기술대학원 교수진 목록은 교수를 소속학과 전산학부로 싣고, 연구분야를 인공지능/무인체계로, 세부 연구 분야를 기계학습보안, 적대적공격, 백도어공격 / 웹취약점탐지, 브라우저 퍼즈 테스팅, 피싱을 활용한 사이버공격으로 적는다.[^gst] 이 가운데 백도어공격은 학습 과정에 몰래 심은 표식이 든 입력에서만 기계학습 모델이 공격자가 정한 대로 동작하게 만드는 공격을 가리킨다. 교수 개인 누리집은 직함을 Associate Professor로, 소속을 KAIST, School of Computing, Graduate School of Information Security로 적는다.[^gs]

교수 개인 누리집에 따르면 교수는 2014년 The University of Texas at Austin 컴퓨터과학과(Department of Computer Science)에서 박사 학위를 받았다. 학위 논문은 「Toward Better Server-side Web Security」이고, 지도교수는 Kathryn S. McKinley와 Vitaly Shmatikov다. 2011년 5월부터 8월까지 SRI International에서, 2014년 4월부터 2017년 7월까지 Google의 Security/Privacy Research Group과 Display Ads Identity Group에서 일했고, 2017년 8월부터 KAIST 전산학부에서 조교수·부교수(Assistant/Associate Professor)로 있다.[^gs] 개인 누리집의 학회 활동(Professional Services) 항목은 편집위원(Editorial Board)으로 ACM Transactions on the Web의 Associate Editors를, 프로그램 위원장(Program Chair)으로 SecWeb 2023과 SecWeb 2022를 적고, NDSS, USENIX Security, CCS, S&P, WWW, ACSAC, Euro S&P 등의 프로그램 위원 경력을 적는다.[^gs]

교수 개인 누리집 Teaching 페이지에 따르면 교수의 2021–2026년 강의는 CS447 Web Security Attack Laboratory(2021년 가을, 2022–2025년 봄), CS206 Data Structure(2021년 봄), IS593 Machine Learning Application Trends in Information Security(2023·2024년 봄), IS542 Web Service Security and Privacy(2021년 봄, 2022–2024년 가을, 2026년 가을)다.[^teaching]

학과 교수 목록의 연구 분야, 개인 누리집의 연구 관심사, 2021–2026년 논문 목록을 함께 보면, 교수의 전문 분야는 웹 보안·프라이버시, 웹 응용과 브라우저의 취약점을 찾는 프로그램 분석과 시험 도구, 대형 언어 모델을 포함한 기계학습 모델의 보안·프라이버시다.[^cs][^gs][^pubs]

## 응용 분야

누리집은 연구 목표를 새로운 착상을 실제 서비스에 구현해 인터넷 서비스를 더 안전하고 사적으로 만드는 것으로 적는다.[^research] 대표 논문 3은 실제 환경에서 그때까지 보고되지 않은 웹 응용 취약점을 찾았고[^p3], 대표 논문 4의 결과는 Chrome과 Safari를 포함한 주요 브라우저의 보안 버그 수정에 이바지했다.[^p4] 대표 논문 8은 보이스피싱을 막는 안드로이드 시스템 변경 권고를 내놓았다.[^p8] 누리집 첫 화면 소식은 2025년 10월 연구실이 2025 Korea Cyber Security Research Competition에서 2nd place award(최우수상)를 받았고, 2026년 7월 Microsoft의 External Red Team Alliance(EXTRA)에 선정되었다고 알린다.[^home]

## 구성원

누리집 People 페이지의 박사과정(Ph.D. students) 6명과 석사과정(Master’s students) 5명, 모두 11명이다. 카드는 이름과 과정을 적는다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Sunnyeo Park | 박사과정 | 3 |
| Soyoung Lee | 박사과정 | 3, 6 |
| Dongwon Shin | 박사과정 | 1, 5, 7 |
| Seongho Keum | 박사과정 | 1, 5 |
| Sungwoo Jeon | 박사과정 |  |
| Junkyu Kang | 박사과정 | 6 |
| Changoo Lee | 석사과정 | 5 |
| Yongbi Son | 석사과정 |  |
| Hyunjoon Lee | 석사과정 |  |
| Taekwan Lee | 석사과정 |  |
| Jinwoo Park | 석사과정 |  |

## 졸업생

누리집 People 페이지 Alumni 구역의 16줄이다(Master 13줄, Ph.D. 3줄). 학위와 진로는 각 줄의 표기 그대로이며, 진로는 now 뒤에 적힌 소속이다. 졸업 연도는 적혀 있지 않다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Taekjin Lee | Master | National Security Research Institute, South Korea |
| Junghwan Park | Master | Naver, South Korea |
| Daejun Kim | Master | Theori, South Korea |
| Hyuntae Kim | Master | Theori, South Korea |
| Hyunjoo Lee | Master | Korea Institute of Nuclear Nonproliferation and Control, South Korea |
| Dahun Lee | Master | Theori, South Korea |
| Wonho Song | Master | Upstage, South Korea |
| Joongyum Kim | Ph.D. | Moloco, South Korea |
| Hoyong Jeong | Master | Deeping Source, South Korea |
| Seongil Wi | Ph.D. | Assistant Professor at UNIST, South Korea |
| Jihwan Kim | Master | ENKI, South Korea |
| Beomsoo Kim | Master | Hyundai Motor Company, South Korea |
| Kiwon Chung | Master | ClumL, South Korea |
| Changmin Lee | Master | Rebellions, South Korea |
| Yoonha Bahng | Master | CJ OliveNetworks, South Korea |
| Suyoung Lee | Ph.D. | Postdoctoral Researcher at UMass Amherst, US |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지의 2021–2026년 구역 35편과, 교수 개인 누리집 Publications 페이지에만 있는 2023년 학술지 논문 1편(Scalable and Secure Virtualization of HSM with ScaleTrust)을 합한 36편이다(2026년 10편, 2025년 7편, 2024년 2편, 2023년 6편, 2022년 8편, 2021년 3편).[^pubs][^gspubs] 저자·제목·학회·학술지 표기는 누리집 그대로이며, 연도는 누리집 구역의 연도다. 저자 이름 뒤의 (co-leading author)는 누리집 표기다. 2026년 구역에서 누리집이 제목 뒤에 (to appear)를 붙이고 첫 화면 소식이 채택(accepted)을 알린 학회 논문 2편(NeurIPS 2026, CCS 2026)은 학회 이름 뒤에 「(채택)」으로 표시했다.[^pubs][^home] 목록 구성 기준은 근거 페이지에 적었다.

**2026**

- Woo Jae Kim, Seongho Keum, Joonsung Jeon, Suhyeon Ha, Sooel Son, and Sung-eui Yoon. "AdKnob: Ad Intensity Control and Labeling for LLM-Native Advertising". *40th Annual Conference on Neural Information Processing Systems (NeurIPS 2026) (채택)*.
- Suhyeon Ha, Woo Jae Kim, Joonsung Jeon, Sooel Son, and Sung-eui Yoon. "APT: Anchor-aligned Perturbations for Tamper Localization in Fully Regenerated Images". *19th European Conference on Computer Vision (ECCV)*.
- Yongbi Son, Changoo Lee (co-leading author), Dongwon Shin, Byoungyoung Lee, Sanghyun Hong, and Sooel Son. "AgentBreaker: Evaluating Context-Aware Indirect Prompt Injection Risks in Modern Web Agents". *35th ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA 2026)*.
- Hyunjoon Lee, Suyoung Lee (co-leading author), Heiko Kiesel, and Sooel Son. "Overloading Ad Blockers: Exploiting Filtering Logic for Selective Denial of Service". *33th ACM Conference on Computer and Communications Security (CCS 2026) (채택)*.
- Suyoung Lee, Seongho Keum, Changoo Lee, Dongwon Shin, Sanghyun Hong, Byoungyoung Lee, and Sooel Son. "Site Isolation is Dead: How Site Isolation is Broken in Agentic Browsers and Extensions". *47th IEEE Symposium on Security and Privacy (S&P 2026)*.
- Jaehan Kim, Minkyoo Song, Seungwon Shin, and Sooel Son. "SafeMoE: Safe Fine-Tuning for MoE LLMs by Aligning Harmful Input Routing". *14th International Conference on Learning Representations (ICLR 2026)*.
- Joonsung Jeon, Woo Jae Kim, Suhyeon Ha, Sooel Son, and Sung-eui Yoon. "No Caption, No Problem: Caption-Free Membership Inference via Model-Fitted Embeddings". *14th International Conference on Learning Representations (ICLR 2026)*.
- Soyoung Lee, Sunnyeo Park, Yonghwi Kwon, and Sooel Son. "Zelda: Feedback-driven Closed-box Fuzzing for Identifying Web Application Vulnerabilities". *The Web Conference 2026: Security and Privacy Research Track (WWW 2026)*.
- Dongwon Shin and Sooel Son. "LLMs Killed Q&A Stars? Analyzing the Impact of LLM-Generated Answers on an Online Q&A Platform". *The Web Conference 2026: Social Networks and Social Media Research Track (WWW 2026)*.
- Junkyu Kang, Soyoung Lee (co-leading author), Yonghwi Kwon, and Sooel Son. "Connecting the Dots: An Investigative Study on Linking Private User Data Across Messaging Apps". *33th Network & Distributed System Security Symposium (NDSS 2026)*.

**2025**

- Jaehan Kim, Seung Ho Na, Minkyoo Song, Seungwon Shin, and Sooel Son. "MoEvil: Poisoning Expert to Compromise the Safety of Mixture-of-Experts LLMs". *41th Annual Computer Security Applications Conference (ACSAC 2025)*.
- Woo Jae Kim, Kyu Beom Han, Yoonki Cho, Youngju Na, Junsik Jung, Sooel Son, and Sung-eui Yoon. "AegisRF: Adversarial Perturbations Guided with Sensitivity for Protecting Intellectual Property of Neural Radiance Fields". *36th British Machine Vision Conference (BMVC 2025)*.
- Seongho Keum, Dongwon Shin, Leo Marchyok, Sanghyun Hong, and Sooel Son. "Private Investigator: Extracting Personally Identifiable Information from Large Language Models Using Optimized Prompts". *34th USENIX Security Symposium (USENIX Security 2025)*.
- Minkyoo Song, Hanna Kim, Jaehan Kim, Seungwon Shin, and Sooel Son. "Refusal Is Not an Option: Unlearning Safety Alignment of LLMs". *34th USENIX Security Symposium (USENIX Security 2025)*.
- Sunnyeo Park, Jihwan Kim, Seongho Keum, Hyunjoon Lee, and Sooel Son. "TrustyMon: Practical Detection of DOM-based Cross-Site Scripting Attacks Using Trusted Types". *20th ACM ASIA Conference on Computer and Communications Security (AsiaCCS 2025)*.
- Joonsung Jeon, Woo Jae Kim, Suhyeon Ha, Sooel Son, and Sung-eui Yoon. "AdvPaint: Protecting Images from Inpainting Manipulation via Adversarial Attention Disruption". *13th International Conference on Learning Representations (ICLR 2025)*.
- Eunjin Roh, Sungwoo Jeon (co-leading author), Sooel Son, and Sanghyun Hong. "Evaluating Robustness of Reference-based Phishing Detectors". *20th ACM ASIA Conference on Computer and Communications Security (AsiaCCS 2025)*.

**2024**

- Dongwon Shin, Suyoung Lee, Sanghyun Hong, and Sooel Son. "You Only Perturb Once: Bypassing (Robust) Ad-Blockers Using Universal Adversarial Perturbations". *40th Annual Computer Security Applications Conference (ACSAC 2024)*.
- Hoyong Jeong, Kiwon Chung, Sung Ju Hwang, and Sooel Son. "Targeted Model Inversion: Distilling Style Encoded in Predictions". *Elsevier Computers & Security (Journal COSE 2024)*.

**2023**

- Minseon Kim, Hyeonjeong Ha, Sooel Son, and Sung Ju Hwang. "Effective Targeted Attacks for Adversarial Self-Supervised Learning". *37th Annual Conference on Neural Information Processing Systems (NeurIPS 2023)*.
- Changmin Lee and Sooel Son. "AdCPG: Classifying JavaScript Code Property Graphs with Explanations for Ad and Tracker Blocking". *30th ACM Conference on Computer and Communications Security (CCS 2023)*.
- Byungjoo Kim, Suyoung Lee, Seanie Lee, Sooel Son, and Sung Ju Hwang. "Margin-based Neural Network Watermarking". *40th International Conference on Machine Learning (ICML 2023)*.
- Dongwon Shin, Suyoung Lee (co-leading author), and Sooel Son. "RICC: Robust Collective Classification of Sybil Accounts". *The Web Conference 2023: Security, Privacy, and Trust Research Track (WWW 2023)*.
- Seongil Wi, Trung Tin Nguyen, Jihwan Kim, Ben Stock, and Sooel Son. "DiffCSP: Finding Browser Bugs in Content Security Policy Enforcement through Differential Testing". *30th Network & Distributed System Security Symposium (NDSS 2023)*.
- Juhyeng Han, Insu Yun, Seongmin Kim, Taesoo Kim, Sooel Son, Dongsu Han. "Scalable and Secure Virtualization of HSM with ScaleTrust". *IEEE/ACM Transactions on Networking*.

**2022**

- Hoyong Jeong, Suyoung Lee, Sung Ju Hwang, and Sooel Son. "Learning to Generate Inversion-Resistant Model Explanations". *36th Annual Conference on Neural Information Processing Systems (NeurIPS 2022)*.
- Suyoung Lee, Wonho Song, Suman Jana, Meeyoung Cha, and Sooel Son. "Evaluating the Robustness of Trigger Set-Based Watermarks Embedded in Deep Neural Networks". *IEEE Transactions on Dependable and Secure Computing (Journal TDSC 2022)*.
- Dongkwan Kim, Eunsoo Kim, Sang Kil Cha, Sooel Son, and Yongdae Kim. "Revisiting Binary Code Similarity Analysis using Interpretable Feature Engineering and Lessons Learned". *IEEE Transactions on Software Engineering (Journal TSE 2022)*.
- Joongyum Kim, Jihwan Kim, Seongil Wi, Yongdae Kim, and Sooel Son. "HearMeOut: Detecting Voice Phishing Activities in Android". *20th ACM International Conference on Mobile Systems, Applications, and Services 2022 (MobiSys 2022)*.
- Sunnyeo Park, Daejun Kim (co-leading author), Suman Jana, and Sooel Son. "FUGIO: Automatic Exploit Generation for PHP Object Injection Vulnerabilities". *22nd USENIX Security Symposium (USENIX Security 2022)*.
- Sangwook Bae, Mincheol Son, Dongkwan Kim, CheolJun Park, Jiho Lee, Sooel Son, and Yongdae Kim. "Watching the Watchers: Practical Video Identification Attack in LTE Networks". *22nd USENIX Security Symposium (USENIX Security 2022)*.
- Seongil Wi, Sijae Woo, Joyce Whang, and Sooel Son. "HiddenCPG: Large-Scale Vulnerable Clone Detection Using Subgraph Isomorphism of Code Property Graphs". *The Web Conference 2022: Security, Privacy, and Trust Research Track (WWW 2022)*.
- Soyoung Lee, Seongil Wi, and Sooel Son. "Link: Black-Box Detection of Cross-Site Scripting Vulnerabilities Using Reinforcement Learning". *The Web Conference 2022: Security, Privacy, and Trust Research Track (WWW 2022)*.

**2021**

- Hyunjoo Lee, Jiyeon Lee (co-leading author), Daejun Kim, Suman Jana, Insik Shin, and Sooel Son. "AdCube: WebVR Ad Fraud and Practical Confinement of Third-Party Ads". *21st USENIX Security Symposium (USENIX Security 2021)*.
- Doowon Kim, Haehyun Cho, Yonghwi Kwon, Adam Oest, Adam Doupe, Sooel Son, Gail-Joon Ahn, and Tudor Dumitras. "Security Analysis on Practices of Certificate Authorities in the HTTPS Phishing Ecosystem". *16th ACM ASIA Conference on Computer and Communications Security (ASIACCS 2021)*.
- Joongyum Kim, Junghwan Park (co-leading author), and Sooel Son. "The Abuser Inside Apps: Finding the Culprit Committing Mobile Ad Fraud". *28th Network & Distributed System Security Symposium (NDSS 2021)*.

## 수상

누리집 첫 화면 News 가운데 수상 소식 4건(2022년 2월–2025년 12월)이다. 날짜는 소식의 월 표기이고, 문장은 소식 본문 그대로다.[^home]

- Dec, 2025 · We won the Distinguished Paper Award at ACSAC'25!
- Oct, 2025 · We won the 2nd place award (최우수상) at 2025 Korea Cyber Security Research Competition!
- Dec, 2022 · Seongil Wi awarded 2022 Naver Ph.D. Fellowship!
- Feb, 2022 · Soyoung Lee awarded 2022 KAIST SoC Best Thesis Award!

## 소식

누리집 첫 화면 News 가운데 논문 채택·게재 소식 23건과 Microsoft의 External Red Team Alliance(EXTRA) 선정 소식 1건, 모두 24건이다(2022년 1월–2026년 9월). 날짜는 소식의 월 표기이고, 문장은 소식 본문 그대로다.[^home]

- Sep, 2026 · A paper accepted in NeurIPS'26!
- Jul, 2026 · We were selected for Microsoft’s External Red Team Alliance (EXTRA)!
- Jun, 2026 · A paper accepted in ECCV'26!
- Apr, 2026 · A paper accepted in ISSTA'26!
- Apr, 2026 · A paper accepted in CCS'26!
- Mar, 2026 · A paper accepted in S&P'26!
- Jan, 2026 · Two papers accepted in ICLR'26!
- Jan, 2026 · Two papers accepted in WWW'26!
- Sep, 2025 · A paper accepted in ACSAC'25!
- Aug, 2025 · A paper accepted in NDSS'26!
- Jun, 2025 · Two papers accepted in USENIX Security'25!
- Apr, 2025 · A paper accepted in AsiaCCS'25!
- Jan, 2025 · A paper accepted in ICLR'25!
- Jan, 2025 · A paper accepted in AsiaCCS'25!
- Oct, 2024 · A paper accepted in ACSAC'24!
- Aug, 2024 · A paper published at Computers & Security 2024!
- Sep, 2023 · A paper accepted in NeurIPS'23!
- Sep, 2023 · A paper accepted in CCS'23!
- Apr, 2023 · A paper accepted in ICML'23!
- Jan, 2023 · A paper accepted in WWW'23!
- Dec, 2022 · A paper accepted in NDSS'23!
- Sep, 2022 · A paper accepted in NeurIPS'22!
- May, 2022 · A paper accepted in MobiSys'22!
- Jan, 2022 · Two papers accepted in WWW'22!

## 연락과 위치

- 교수 연구실: E3-1 4434[^gs][^cs][^contact]
- 교수 전화: 042-350-3575[^gsis][^cs]
[^p1]: S. Keum 외, S. Son, 34th USENIX Security Symposium (USENIX Security 2025) (2025). <https://wsp-lab.github.io/papers/keum-privateinvestigator-sec25.pdf> 초록 기준(연구실 누리집 Publications 페이지에 올린 논문 PDF의 초록).
[^p2]: J. Kim, M. Song, S. Shin, S. Son, 14th International Conference on Learning Representations (ICLR 2026) (2026). <https://wsp-lab.github.io/papers/kim-safemoe-iclr26.pdf> 초록 기준(연구실 누리집 Publications 페이지에 올린 논문 PDF의 초록).
[^p3]: S. Lee, S. Park, Y. Kwon, S. Son, Proceedings of the ACM Web Conference 2026, 2917-2928 (온라인 2026-04-12). <https://doi.org/10.1145/3774904.3792378> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: S. Wi 외, S. Son, Proceedings 2023 Network and Distributed System Security Symposium (2023). <https://doi.org/10.14722/ndss.2023.24200> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: S. Lee 외, S. Son, 2026 IEEE Symposium on Security and Privacy (SP), 1804-1821 (2026). <https://doi.org/10.1109/sp63933.2026.00241> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: J. Kang, S. Lee, Y. Kwon, S. Son, Proceedings 2026 Network and Distributed System Security Symposium (2026). <https://doi.org/10.14722/ndss.2026.230556> 초록 기준(연구실 누리집 Publications 페이지에 올린 논문 PDF의 초록).
[^p7]: D. Shin, S. Lee, S. Son, Proceedings of the ACM Web Conference 2023, 2329-2339 (온라인 2023-04-30). <https://doi.org/10.1145/3543507.3583475> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: J. Kim 외, S. Son, Proceedings of the 20th Annual International Conference on Mobile Systems, Applications and Services, 422-435 (온라인 2022-06-27). <https://doi.org/10.1145/3498361.3538939> 초록 기준(연구실 누리집 Publications 페이지에 올린 논문 PDF의 초록).
[^home]: 연구실 누리집 첫 화면 <https://wsp-lab.github.io/> (연구실 이름, News, 2026-10-23 열람)
[^research]: 연구실 누리집 Research 페이지 <https://wsp-lab.github.io/research/> (Research Area, 네 연구 갈래, Representative Works, 2026-10-23 열람)
[^people]: 연구실 누리집 People 페이지 <https://wsp-lab.github.io/people/> (Professor, Ph.D. students, Master’s students, Alumni, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publications 페이지 <https://wsp-lab.github.io/publications/> (2021–2026년 구역, 2026-10-23 열람)
[^contact]: 연구실 누리집 Contact 페이지 <https://wsp-lab.github.io/contact/> (연구실 위치, 2026-10-23 열람)
[^gs]: 교수 개인 누리집 첫 화면 <https://sites.google.com/site/ssonkaist/> (직함·소속·연구실 위치, Research Interests, Education, Work Experience, Professional Services, 2026-10-23 열람)
[^gsresearch]: 교수 개인 누리집 Research 페이지 <https://sites.google.com/site/ssonkaist/research_1> (네 연구 갈래, R1 과제 소개, 2026-10-23 열람)
[^gspubs]: 교수 개인 누리집 Publications 페이지 <https://sites.google.com/site/ssonkaist/research> (2023년 학술지 논문 항목, 2026-10-23 열람)
[^teaching]: 교수 개인 누리집 Teaching 페이지 <https://sites.google.com/site/ssonkaist/teaching> (강의 목록, 2026-10-23 열람)
[^cs]: KAIST 전산학부 교수 목록 <https://cs.kaist.ac.kr/people/faculty> (손수엘 항목의 직위, 교수연구실, 전화, 연구 분야, 2026-10-23 열람)
[^gsis]: KAIST 정보보호대학원 교수진 목록 <https://gsis.kaist.ac.kr/people/faculty> (손수엘 항목의 소속, 웹사이트, 전화, 연구 분야, 2026-10-23 열람)
[^gst]: KAIST 안보과학기술대학원 교수진 목록 3쪽 <https://gst.kaist.ac.kr/member/faculty/?page=3> (손수엘 항목의 소속학과, 연구분야, 세부 연구 분야, 연구실, 2026-10-23 열람)

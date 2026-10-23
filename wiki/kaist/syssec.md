# SysSec 연구실 (System Security Lab)

**KAIST 전기및전자공학부·정보보호대학원·안보과학기술대학원 · 김용대 교수**

- 분야: 이동통신(LTE·5G·6G) 보안, 드론 보안, 자율주행차 보안, 사이버-물리 시스템 보안, 기계학습을 쓰는 보안 연구
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: 네트워크 보안·프라이버시[^cellular][^p1][^p4], 무선·이동통신[^cellular][^p2][^p3], 소프트웨어·시스템 보안[^cve][^p2][^p3], 퍼징[^cellular][^p2]
- 홈페이지: <https://yongdaek.github.io/>
- 근거와 출처: [SysSec 연구실 근거 페이지](syssec-sources.md)

> 이동통신망, 드론, 자율주행차처럼 새로 등장하는 시스템에서 보안 취약점을 찾아내고 분석하는 연구실이다.[^home]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 김용대 교수가 이끄는 System Security Lab(SysSec Lab)이다.[^ee][^gst][^cve] 교수 개인 누리집은 연구를 이동통신망, 드론, 자율주행차처럼 새로 등장하는 시스템의 보안 취약점을 찾아 분석하는 일로 소개하고, 현재 연구 관심으로 이동통신망 보안(4G/5G/6G), 자율주행차 보안, 드론 보안, 기계학습(ML)을 쓰는 보안 연구를 든다.[^home] 안보과학기술대학원 교수 명단은 연구분야를 「사이버보안/센서/WMD대응」으로, 세부 연구 분야를 이동통신보안, 드론보안, 자율주행보안으로 적는다.[^gst]

누리집 Researches 절에는 이동통신 보안, 사이버-물리 시스템 보안, 연구실이 찾은 취약점 목록(Discovered CVEs)의 세 글이 있다.[^research] 이동통신 보안 글에서 교수는 지난 15년 동안 이동통신 보안의 여러 문제를 다뤄 이 주제로 18편이 넘는 논문을 냈다고 적는다. 다룬 주제는 사생활, 과금, 응용 보안, 미들박스(통신망 중간에서 패킷 전달 외에 검사·변환·차단 같은 처리를 하는 장비), 자동 성능 분석, 반자동 보안 시험·분석, 물리 계층, 범죄 대응이며, 연구실은 상용 이동통신망과 상용 시험망(테스트베드), 스마트폰으로 직접 실험하고 정부·수사기관, 3GPP·GSMA 같은 표준 단체, 망 장비·단말 제조사와 이동통신사의 연구자와 교류해 왔다고 쓴다.[^cellular] 글은 그 경험에서 이동통신 산업의 일곱 가지 문제를 꼽는다. 10년마다 새 세대가 설계·구현·배치되며 새 취약점이 생길 수 있고, 이동통신망은 통신사마다 운영 정책과 설정이 다른 닫힌 시스템이며, 한 세대의 표준은 정해진 뒤 고쳐지지 않아 설계 취약점이 남는다. 또 운영 중인 이동통신망을 퍼징(무작위에 가까운 입력을 대량으로 넣어 오류를 찾는 시험)하는 일은 대부분 나라에서 불법이고, 보안 정책을 정할 때 통신사(때로는 정부)가 제조사나 일반 사용자보다 우선하며, 표준이 모호하게 쓰인 채 구현 세부를 제조사에 맡기고, 여러 문서와 계층, 주체에 나뉘어 있다. 연구는 이 문제들을 동기로 삼아 체계적 보안 시험과 설계 취약점 연구로 나뉜다.[^cellular]

사이버-물리 시스템 보안 글은 연구실이 지난 10년 동안 사이버-물리 시스템(CPS, 컴퓨터 계산과 물리 장치가 맞물려 움직이는 시스템)의 보안 취약점을 연구해 왔고, 특히 센서 보안, 자율 시스템, IoT 펌웨어(기기 안에 들어가 하드웨어를 제어하는 소프트웨어) 분석에 초점을 둔다고 적는다. 드론·차량 같은 자율 시스템, 의료 기기·화재 감지·전력망 같은 핵심 기반 시설, 센서 보안의 체계적 분석, IoT·펌웨어 보안을 다룬다.[^cps] Discovered CVEs 글은 연구실과 협력자가 찾아 책임 있게 공개한 취약점의 CVE(공개된 보안 취약점에 붙이는 식별 번호)를 이동통신·베이스밴드, 이동 전화, 네트워크 기기에 걸쳐 최신순으로 적는다.[^cve]

대표 논문으로 보면 연구는 네 갈래로 모인다. 첫째, LTE 코어망(가입자 정보와 연결을 관리하는 이동통신망의 중심부)과 스마트폰 베이스밴드(휴대폰에서 이동통신 신호와 통신 규약을 처리하는 모뎀 부분)의 구현 결함을 체계적 시험으로 찾는 연구다(대표 논문 1–3).[^p1][^p2][^p3] 둘째, 국제 사기 범죄에 쓰이는 SIM 박스(인터넷 전화 통화와 이동통신 통화를 서로 바꿔 주는 VoIP 게이트웨이)를 이동통신망에서 가려내는 연구다(대표 논문 4).[^p4] 셋째, 드론의 관성 센서(가속도와 회전을 재는 센서), 광전 센서(빛을 받아 그 세기를 전기 신호로 바꾸는 센서), 전력망의 위상 측정 장치(전압·전류의 위상을 시각에 맞춰 재는 장치)처럼 물리 세계와 맞닿은 장치에 대한 공격의 원리와 조건을 밝히고 탐지·복구 방법을 만드는 연구다(대표 논문 5–7).[^p5][^p6][^p7] 넷째, 대형 언어 모델(LLM)이 만든 한국어 뉴스 댓글을 가려내는 연구다(대표 논문 8).[^p8]

## 주요 연구 주제

### 1. 이동통신망과 단말의 체계적 보안 시험

이동통신 보안 글이 첫 갈래로 드는 체계적 보안 시험이다. LTE의 IP 기반 음성 통화(VoLTE) 보안 시험에서 출발해, LTEFuzz는 표준이 금지한 메시지(잘못된 메시지 인증 코드를 단 메시지 등)를 통신사 망과 스마트폰에 보내 받는 쪽이 이를 버리는지 확인했다. 이어 DoLTEst는 단말(UE, 이동통신망에 접속하는 휴대폰 같은 사용자 기기)의 LTE 규약 구현에서 표준을 따르지 않는 결함을 찾는 상태 기반(stateful) 부정 시험(표준이 허용하지 않는 입력을 넣어 거부하는지 보는 시험) 틀로, CITesting은 인증되지 않은 단말이 다른 가입자의 코어망 상태를 바꿀 수 있는 상향링크(단말에서 망으로 가는 방향) 쪽 결함을 찾는 틀로, LLFuzz는 상용 스마트폰 베이스밴드의 하위 계층(무선 신호 처리와 데이터 전달을 맡는 아래쪽 통신 규약 계층인 RLC, MAC, PDCP, PHY)을 무선으로 퍼징하는 틀로 만들었다. 동적 시험만으로 모든 취약점을 찾을 수는 없어서, BaseSpec은 베이스밴드 바이너리(기계어로 된 실행 파일)와 이동통신 규격을 비교하는 정적 분석(프로그램을 실행하지 않고 코드를 분석하는 방법)을 했고, 무결성 보호를 분석하는 BaseComp로 넓혔다. 여러 나라 통신사의 제어 메시지를 모아 통신사 사이를 비교해 성능 버그와 그 원인을 찾는 연구도 했다.[^cellular] 글은 LTEFuzz 이후 3GPP·GSMA와 계속 소통하며 체계적 부정 시험을 이동통신 시험 규격에 넣으려 한다고 적는다.[^cellular] 대표 논문 1–3.

### 2. 이동통신 설계 취약점과 범죄 대응

둘째 갈래는 이동통신 규격 설계에 있어 다음 세대에서나 고칠 수 있는 취약점을 찾고, 고칠 방법을 제안하거나 패치를 앞당기려 공격을 실제로 구현하는 연구다. 가입자·단말 식별자가 드러나 위치 사생활이 깨지는 문제, 무결성 보호가 없는 방송 메시지를 덮어쓰는 신호 덮어쓰기(signal overshadowing), 암호화되지 않은 하향링크(기지국에서 단말로 가는 방향) 제어 정보로 사용자가 보는 영상을 알아내는 응용 계층 사생활 문제, 데이터 과금 우회와 그 탐지를 다뤘다. 기지국과 스마트폰 사이의 LTE 무선 메시지를 양방향으로 수집하는 공개 도구 LTESniffer도 만들었으며, 이 도구는 암호화된 메시지를 풀지 못하고 암호화되지 않은 부분의 분석에 쓰인다.[^cellular] 글은 현재의 설계 취약점과 고칠 방법을 담은 문서를 학생들과 준비해 6G 연구 항목에 넣으려 한다고 적는다.[^cellular]

범죄 대응으로는 2022년 한국 경찰로부터 보이스피싱 범죄에 대응하는 망 기반 해법을 개발할 연구비를 받아 여러 해법을 개발하고 있으며, 첫 결과로 SIM 박스를 다른 스마트폰과 구별하는 방법을 냈다.[^cellular] 교수는 2022년 4월부터 KAIST Police Science and Technology Research Center의 센터장(Head)을 맡고 있다.[^home][^cv] 대표 논문 4.

### 3. 드론·센서·기반 시설의 사이버-물리 시스템 보안

사이버-물리 시스템 보안 글은 센서의 물리 특성과 제어 알고리즘이 맞물리면서 생기는 취약점을 다루며, 각 부품만으로는 취약하지 않아도 둘의 결합이 공격받을 수 있는 동작을 만든다는 것을 핵심 통찰로 든다.[^cps] 드론에서는 소리로 MEMS 자이로스코프(반도체 공정으로 만든 미세 기계 구조로 회전 속도를 재는 센서)를 교란하는 음향 주입, 센서와 비행 제어기 사이 통신 선로에 대한 전자기 간섭(EMI) 신호 주입, GPS 위조, 조종기 무선 신호의 분석을 연구했고, 음향 주입 공격의 원리를 이론으로 정리해 실시간 공격 탐지와 안전 착륙을 위한 방어를 만들었다. 자이로스코프의 제조 편차로 드론을 식별·추적하는 연구와 차량용 라이다·자기 센서에 대한 공격 연구도 있다.[^cps] 기반 시설과 의료 쪽에서는 아날로그 센서에 대한 전자기 신호 주입, 수액 펌프와 광역 광전식 연기 감지기의 센서 공격, 광전 센서 공격을 탐지하는 방어(Lightbox), 전력망 위상 측정 장치의 GPS 위조를 다뤘다. 아날로그 센서 보안 연구를 하나의 모델로 체계화한 SoK(Systematization of Knowledge, 한 분야의 연구를 체계적으로 정리하는 논문 형식) 논문, 필요한 장비·전문성·근접성 같은 요인으로 물리 센서 공격의 어려움을 정량화한 연구, IoT 펌웨어를 대규모로 에뮬레이션(다른 컴퓨터에서 그 기기처럼 실행)해 취약점을 동적 분석하는 FirmAE도 이 갈래에 든다.[^cps] 대표 논문 5–7.

### 4. 인공지능과 인터넷 서비스 보안

교수 누리집은 현재 연구 관심의 하나로 기계학습을 쓰는 보안 연구를 든다.[^home] 대표 논문 8은 설명 가능한 인공지능(XAI)을 써서 대형 언어 모델이 만든 한국어 뉴스 댓글을 가려내고 만든 모델을 알아내는 연구다.[^p8] 최근 논문 목록에는 한국 금융 서비스가 설치를 요구하는 보안 소프트웨어의 보안 분석(USENIX Security 2025), 콘텐츠 전송 네트워크(CDN)에 TLS(인터넷 통신을 암호화하고 서버를 인증하는 규약) 인증을 맡기는 방식(ACSAC 2023), 무선 몰래카메라(ACSAC 2022), 안드로이드의 보이스피싱 활동 탐지(MobiSys 2022)를 다룬 논문도 있다.[^pubs]

## 대표 논문

교수 개인 누리집 Publications 페이지의 2021–2026년 논문 가운데 김용대 교수가 마지막 저자인 논문을 연구 갈래마다 고르게 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학회·학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [CITesting: Systematic Testing of Context Integrity Violations in LTE Core Networks](https://doi.org/10.1145/3719027.3765230) · ACM CCS 2025 | 이동통신망이 점점 핵심 기반 시설을 떠받치지만, 이전 연구는 주로 하향링크 취약점에 집중했고 단말이 코어망에 영향을 주는 상향링크 보안은 주목을 덜 받았다. 이 논문은 인증되지 않았거나 제대로 인증되지 않은 단말이 다른 가입자의 내부 상태를 바꾸는 상향링크 취약점을 문맥 무결성 위반(CIV)으로 정의하고, LTE 코어망에서 CIV를 체계적으로 찾는 틀 CITesting을 내놓았다. CITesting은 여러 절차의 연쇄와 넓은 범위의 정보 요소(IE, 메시지 안의 항목)를 시험하고 단말 연결 상태마다 동작을 확인하며, 두 단말을 함께 제어해 피해 단말의 상태를 관리하는 시험과 동작으로 판정하는 장치(오라클)로 안을 들여다볼 수 없는 망에서도 문맥 변경을 찾아낸다. 공개 소스 구현 두 가지(Open5GS, srsRAN)와 상용 구현 두 가지(Amarisoft, Nokia)를 평가해 사후 분석 뒤 각각 29, 22, 16, 59개의 서로 다른 CIV를 찾았고, 이 결함들은 단말 연결 해제, 가입자 식별 번호(IMSI) 노출, 존재 확인 같은 원격 공격을 가능하게 했다. 모든 결과는 책임 있게 공개했고 Amarisoft와 Open5GS에 패치를 기여했다.[^p1] | 1저자 Mincheol Son, 마지막 저자 김용대 |
| 2 | 2025 | [LLFuzz: An Over-the-Air Dynamic Testing Framework for Cellular Baseband Lower Layers](https://www.usenix.org/conference/usenixsecurity25/presentation/hoang) · USENIX Security 2025 | 베이스밴드의 메모리 손상(프로그램이 허용되지 않은 메모리 영역을 잘못 읽거나 쓰는 결함)은 무선으로 원격 악용될 수 있어 원격 코드 실행, 서비스 거부, 정보 유출 같은 심각한 결과로 이어진다. 이전 연구는 특히 3계층 규약(NAS, RRC 등)의 메모리 손상 탐지에 크게 기여했지만, 하위 계층은 상대적으로 주목을 덜 받았고 소수 연구만 제한적이고 비체계적으로 다뤘다. 이 논문은 베이스밴드 하위 계층(이동통신 규약 스택의 PDCP, RLC, MAC, PHY 계층)의 메모리 손상을 찾는 무선(over-the-air) 동적 시험 틀 LLFuzz(Lower-Layer Fuzzer)를 내놓았다. 이 계층들은 채널이 여럿이고 패킷 구조를 동적으로 설정할 수 있어 시험이 까다롭다. LLFuzz는 채널 중심·설정 인식 퍼징으로 여러 채널을 체계적으로 탐색하고, 시험 중에 신호 메시지로 계층별 설정을 바꿔 상용망에서 드물게 쓰이는 패킷 구조까지 시험한다. 또 3GPP 규격을 바탕으로 하위 계층 패킷 구조에 맞춘 시험 입력을 만들어, 입력이 문법적으로 올바르고 목표 계층에 닿기 전에 버려지지 않게 했다. 5개 주요 제조사의 상용 베이스밴드 15개를 평가해 알려지지 않았던 메모리 손상 9개(PDCP 2, RLC 2, MAC 5)를 찾았다.[^p2] | 1저자 Tuan Dinh Hoang, 마지막 저자 김용대 |
| 3 | 2022 | [DoLTEst: In-depth Downlink Negative Testing Framework for LTE Devices](https://www.usenix.org/conference/usenixsecurity22/presentation/park-cheoljun) · USENIX Security 2022 | 단말의 LTE 제어 평면(통신의 설정과 관리를 맡는 신호를 다루는 부분) 규약 구현에 결함이 있으면 곧바로 심각한 보안 위협이 된다. 이런 결함을 찾는 데는 잘못되었거나 금지된 메시지만으로 시험하는 부정 시험이 유망하지만, 이동통신 표준은 주로 긍정 시험(올바른 메시지로 하는 시험)에 집중해 많은 구현 취약점이 점검되지 않은 채 남았다. 이 논문은 단말을 포괄적으로 시험하는 부정 시험 틀 DoLTEst를 내놓았다. 규격을 자세히 분석해 만든 하나하나 셀 수 있는 시험 입력과 결정론적 판정 장치(오라클)를 갖춰, 구현 취약점을 찾는 표준으로 쓰기에 알맞다. 5개 베이스밴드 제조사의 단말 43대에서 구현 결함 26개를 찾아 효과를 보였다.[^p3] | 공동 1저자 CheolJun Park·Sangwook Bae(교수 이력서 표기), 마지막 저자 김용대 |
| 4 | 2023 | [Preventing SIM Box Fraud Using Device Model Fingerprinting](https://doi.org/10.14722/ndss.2023.24416) · NDSS 2023 | SIM 박스는 개인 피해자와 이동통신사로부터 수십억 달러를 빼앗는 국제 규모 사기의 지하 생태계에서 핵심 역할을 해 왔다. 이전 대책은 주로 사기 통화 세션을 찾는 데 집중했고, SIM 박스 장치가 망을 쓰지 못하게 막는 직접적인 방법은 주목받지 못했다. 이 논문은 허가받지 않은 SIM 박스가 통신에 이동통신망을 쓰는 것을 찾아내는 간단한 접근 제어 논리를 제안했다. 핵심은 쉽게 위조할 수 있는 단말 고유 번호(IMEI)에 기대지 않고, 단말 모델(예: iPhone 13을 다른 스마트폰 모델과 구별)과 단말 종류(스마트폰과 IoT 기기)를 정밀하게 지문화하는 것이다. 망 계층의 보조 정보에서 뽑은 3만 1천 개가 넘는 특징으로 만든 지문이 스마트폰 85대 사이에서 대부분 서로 달라, 불법 SIM 박스 대부분이 허가 없이 음성 통화를 하지 못하게 막는 데 쓸 수 있음을 실험으로 보였다.[^p4] | 공동 1저자 Beomseok Oh·Junho Ahn(교수 이력서 표기), 마지막 저자 김용대 |
| 5 | 2023 | [Un-Rocking Drones: Foundations of Acoustic Injection Attacks and Recovery Thereof](https://doi.org/10.14722/ndss.2023.24112) · NDSS 2023 | MEMS 관성 측정 장치(IMU, 가속도와 회전을 재는 센서 묶음)를 단 드론은 음향 주입 공격에 노출되어 있다. 이 공격은 센서를 공진(외부 진동의 진동수가 구조의 고유 진동수와 같을 때 진동이 커지는 현상)시켜 출력을 망가뜨리고 드론을 추락시킨다. 이전 대책은 공격 중에 드론을 계획한 목적지까지 날게 하지 못해 실용성에 한계가 있었다. 이 논문은 실용적인 대응을 위해 망가진 센서 값을 복구하는 것을 목표로 했다. 실제와 가까운 시험 환경을 만들어 공진하는 MEMS 센서가 드론에 주는 영향을 살폈고, 센서 값을 읽어 오는 시간 지연이 일정하지 않은 샘플링 지터가 공격 중 드론 추락에 큰 영향을 준다는 것을 발견했다. 실시간 시스템에는 제조 오차나 일정 관리·운영 부담 때문에 샘플링 지터가 있고 실시간 요구 조건으로는 무시할 만하지만, 공격받는 드론에서는 샘플링 지터가 공진 신호를 제어 논리가 다루는 대역 안으로 퍼뜨려 저역 통과 필터(정해진 주파수 아래 성분만 통과시키는 필터) 같은 안전 장치를 무력화한다. 샘플링 지터의 영향을 받은 공진 신호를 잡음으로 보고, 잡음 제거 오토인코더(잡음 섞인 입력에서 원래 신호를 복원하도록 학습하는 신경망)로 다른 보조 센서 없이 망가진 신호에서 정상 센서 신호를 복구하는 대응 방법을 만들었다. 이 시제품 UNROCKER를 구현해 실제 상황을 반영한 일련의 실험으로 능력을 보였고, 소스 코드와 실험 자료를 공개했다.[^p5] | 1저자 Jinseob Jeong, 마지막 저자 김용대 |
| 6 | 2023 | [Lightbox: Sensor Attack Detection for Photoelectric Sensors via Spectrum Fingerprinting](https://doi.org/10.1145/3615867) · ACM Transactions on Privacy and Security | 광전 센서(빛을 받아 그 세기를 전기 신호로 바꾸는 센서)는 의료 기기와 자율주행차처럼 안전이 중요한 곳에 쓰이지만, 입력 통로가 밖으로 드러나 있어 악의적 입력에 취약하다. 이 논문은 신호 지문으로 광전 센서에 대한 센서 공격을 탐지하는 방어 시스템 Lightbox를 내놓았다. 받은 빛의 스펙트럼(파장별 세기 분포)을 특징으로 써서, 공격자가 넣은 신호와 센서 자체 광원에서 온 정상 신호를 구별한다. 센서를 포화시키는 공격자, 단순 위조 공격자, Lightbox를 알고 여러 광원을 섞어 정상 광원을 흉내 내는 정교한 공격자를 상대로 평가해, 앞의 두 공격자에 대해 99%가 넘는 전체 정확도를 얻고 정교한 공격자에도 견고함을 보였다. 전송 매질, 배경 잡음, 입력 파형 같은 여러 환경에서도 평가했고, 학습 시간을 더 줄인 뒤 단일 보드 컴퓨터로 실험해 실용성을 보였다.[^p6] | 1저자 Dohyun Kim, 마지막 저자 김용대 |
| 7 | 2025 | [Revisiting GPS Spoofing in Phasor Measurement: Real-World Exploitation and Practical Detection in Power Grids](https://doi.org/10.1145/3720543) · ACM Transactions on Privacy and Security | 위상 측정 장치(PMU)는 전압·전류의 페이저(크기와 위상을 함께 나타낸 값)를 정밀하게 재어 동기 위상 측정값(synchrophasor)을 내며, 현대 전력망의 실시간 감시, 고장 탐지, 안정도 평가에 쓰이는 핵심 장치다. 이전 연구는 GPS 위조(가짜 위성 신호로 수신기를 속이는 것)로 시각을 임의로 조작하면 전력망 운영을 교란할 수 있다고 보았지만, 이 논문은 공격이 성공하려면 특정 조건이 필요하다는 것을 밝혔다. 동기 위상 측정 자료 규격(IEEE Standard C37.118.x)을 분석해, 임의의 시각 조작은 곧바로 위상 조작으로 이어지지 않고 GPS 홀드오버(위성 신호와의 동기를 잃은 상태)를 일으켜 잘못된 시각을 운영자에게 알리고 결국 받은 측정값을 무효로 만든다는 것을 보였으며, 상용 PMU 실험으로 확인했다. 홀드오버를 피하는 시각 위조 조건을 밝히고, 상용 광역 감시 시스템(WAMS) 시험대에서 그 조건을 만족하는 위조가 경보 없이 시각 오차를 만든다는 것을 보였다. 이에 대응해 GPS 위조로 생긴 거짓 고장을 낙뢰나 접지 단락 같은 실제 고장과 구별하는 실용적인 방법을 제안했고, 실제 사고 기록 분석에서 실제 고장은 전기 주기 세 번 안에 순간적인 위상 변화를 보인다는 구별 근거를 얻었다.[^p7] | 1저자 Chunghyo Kim, 마지막 저자 김용대 |
| 8 | 2025 | [XDAC: XAI-Driven Detection and Attribution of LLM-Generated News Comments in Korean](https://doi.org/10.18653/v1/2025.acl-long.1108) · ACL 2025 | 대형 언어 모델(LLM)은 사람이 쓴 것 같은 글을 만들어 속이는 콘텐츠에 악용될 우려가 있고, 온라인 뉴스의 LLM 생성 댓글(LGC)을 찾아내는 일은 온라인 담론의 건전성을 지키고 여론 조작을 막는 데 꼭 필요하다. 그러나 뉴스 댓글은 짧고 격식이 없어 기존 방법이 잘 통하지 않고, 공개된 LGC 데이터 세트가 없어 특히 영어가 아닌 언어에서 모델 학습이 어렵다. 이 논문은 다양하고 복잡한 예를 담은 데이터 세트를 만드는 LGC 생성 틀과, 설명 가능한 인공지능(XAI)으로 한국어 뉴스 기사의 짧은 LGC를 찾아내고 어느 모델이 만들었는지 가려내는 틀 XDAC를 함께 내놓았다. XDAC는 XAI로 토큰(언어 모델이 글을 나누어 다루는 단위)과 글자 수준에서 구별되는 언어 패턴을 드러낸다. 한국 뉴스 플랫폼에서 사람이 쓴 댓글 130만개와 서로 다른 14개 모델이 만든 댓글 100만개로 이루어진 대규모 벤치마크 데이터 세트를 내놓았다. XDAC는 기존 방법을 앞서 LGC 탐지에서 F1 점수(정밀도와 재현율의 조화 평균) 98.5%를 얻었고 상대 개선율은 68.1%였으며, 생성 모델 판별에서는 F1 점수 84.3%를 얻었다. 실제 적용 가능성을 확인하려고 네이버 뉴스 댓글 524만개를 분석해 LLM이 만들었을 가능성이 있는 댓글 27,029개를 찾았다.[^p8] | 1저자 Wooyoung Go, 마지막 저자 김용대 |

## 교수와 전문 분야

김용대 교수는 KAIST 전기및전자공학부 교수이자 정보보호대학원 겸임 교수(Joint Appointment)이고, 2025년 3월부터 KAIST ICT 석좌교수와 한국공학한림원(National Academy of Engineering of Korea) 회원이며, IEEE 석학회원(Fellow)이다.[^home][^cv][^ee] 전기및전자공학부 교수 소개는 주요 연구분야를 Information, Communication & Coding, Security, Software Systems & Networking으로, 주요 연구를 Network and Distributed System Security, Applied Cryptography로, 디비전을 Computer로 적는다.[^ee] 안보과학기술대학원 교수 명단에는 소속학과 전기및전자공학부로 올라 있다.[^gst]

교수 개인 누리집과 이력서에 따르면 연세대학교에서 수학 학사(1991년 2월)와 석사(1993년 2월)를, 미국 서던캘리포니아대학교(USC)에서 Gene Tsudik 교수의 지도로 컴퓨터과학 박사학위(2002년 5월)를 받았다.[^home][^cv] 1993년 2월–1998년 8월 한국전자통신연구원(ETRI) 연구원(Member of Research Staff), 2001년 1월–2002년 7월 UC 어바인 방문 연구원을 거쳐 2002년 8월–2012년 6월 미네소타대학교 컴퓨터과학과 조교수·부교수로 일했고, 그사이 2006년 7월–2008년 6월 McKnight Land-Grant Professor였다.[^home][^cv] 2012년 8월 KAIST 전기및전자공학부 교수와 정보보호대학원 겸임 교수가 됐고, 2013년 1월–2015년 12월 KAIST 석좌교수(Chair Professor), 2017년 12월–2020년 2월 KAIST 사이버보안연구센터(Cyber Security Research Center) 센터장을 지냈다.[^home][^cv] 사이버-물리 시스템 보안 글은 아날로그 센서에 전자기 신호를 주입하는 연구(IEEE S&P 2013)가 교수의 첫 센서 공격 논문이며, 전기공학 학생들과 센서 보안 연구를 이어 가려고 KAIST 전기및전자공학부로 옮긴 계기였다고 적는다.[^cps]

이력서에 따르면 2024년부터 NDSS(Network and Distributed System Security Symposium) 운영위원장을 맡고 있으며, 2022년부터 ACM WiSec 운영위원이고 2022년 ACM WiSec 프로그램 공동위원장, 2021년 ACM CCS 공동 대회장(General Co-chair), 2018년 ACM ASIACCS 프로그램 공동위원장을 맡았다. 2013–2020년에는 ACM Transactions on Privacy and Security 편집위원이었다.[^cv] 누리집과 이력서는 이전 수상으로 NSF CAREER Award(2005), McKnight Land-Grant Professorship(2006), ACM WiSec Best Paper Award(2016)를 적는다.[^home][^cv] 누리집은 지난 연구 관심으로 블록체인 보안, IoT 보안, 임베디드 시스템 보안, 네트워크 프로토콜 분석, 무선 보안, 응용 암호, 익명성, 프라이버시, 모바일 보안, 센서 보안, 소프트웨어 보안, 시스템 보안을 든다.[^home]

누리집 Teaching 페이지는 맡은 과목으로 Security of Emerging Systems(2022–2025년 가을), Special Topics: Introduction to Cybersecurity for EE(2024·2026년 봄), Special Topics: Introduction to Cryptography Engineering(2016·2018·2022·2025년 봄), Discrete Methods for Electrical Engineering(2013·2017·2021·2023년 봄), Think Like an Adversary(2012–2019·2021년 가을), Introduction to Information Security(2014–2019년 봄), Special Topics: Blockchain and Cryptocurrencies(2019년 봄)를 적는다.[^teaching]

논문으로 보면 전문 분야는 세 갈래다. 첫째, LTE 코어망과 스마트폰 베이스밴드를 대상으로 한 체계적 보안 시험과 이동통신 범죄 대응이다(대표 논문 1–4).[^p1][^p2][^p3][^p4] 둘째, 드론 센서, 광전 센서, 전력망 위상 측정 장치처럼 물리 세계와 맞닿은 시스템의 보안이다(대표 논문 5–7).[^p5][^p6][^p7] 셋째, 기계학습을 쓰는 보안 연구다(대표 논문 8).[^p8]

## 응용 분야

연구 대상은 이동통신망과 스마트폰 모뎀, 드론과 자율주행차의 센서, 의료 기기, 화재 감지기, 전력망 감시 장치, IoT 기기 펌웨어다.[^cellular][^cps] 이동통신 보안 글은 연구실이 찾은 취약점을 책임 있게 공개해 단말·망에서 패치되게 했고, 여러 연구가 3GPP 보안 표준 작업반(SA3) 회의에서 논의됐다고 적는다. 한국 경찰의 지원으로 보이스피싱 대응 해법을 개발하며, SIM 박스 탐지 방법은 국내 주요 통신사와 시험하고 있다고 적는다.[^cellular] 전력망 연구는 한국전력(KEPCO)과 캐나다 Hydro-Québec의 상용 PMU 시험대와 협력했다.[^cps]

## 최근 논문 목록 (2021–2026)

김용대 교수 개인 누리집 Publications 페이지의 2021–2026년 항목 27건과, 같은 누리집에 올린 교수 이력서에만 있는 2025년 2건(ACSAC 2025의 OTABase 논문, IEEE Power and Energy Magazine 글)으로 모두 29건이다. 저자·제목·학회·학술지 표기는 누리집 그대로이고, 이력서에서 온 2건은 이력서 표기 그대로다. 교수 개인 목록이라 교수가 마지막 저자가 아닌 공동 연구도 들어 있다. 2022년의 「Attack of the Clones」는 누리집이 CoRR로 적고 arXiv 사전 공개본(2201.08678)으로 잇는 논문이다.[^pubs][^cv]

**2026**

- Kwangmin Kim, Taekkyung Oh, Yongdae Kim. "Denied by Border: Denial-of-Service Attack Exploiting Location Restrictions in Non-Terrestrial Networks". *19th ACM Conference on Security and Privacy in Wireless and Mobile Networks (WiSec ‘26)*.

**2025**

- Wooyoung Go, Hyoungshick Kim, Alice Oh, Yongdae Kim. "XDAC: XAI-Driven Detection and Attribution of LLM-Generated News Comments in Korean". *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2025, Vienna, Austria, July 27 - August 1, 2025*.
- Taisic Yun, Suhwan Jeong, Yonghwa Lee, Seungjoo Kim, Hyoungshick Kim, Insu Yun, Yongdae Kim. "Too Much of a Good Thing: (In-)Security of Mandatory Security Software for Financial Services in South Korea". *34th USENIX Security Symposium, USENIX Security 2025, Seattle, WA, USA, August 13-15, 2025*.
- Chunghyo Kim, Juhwan Noh, Esmaeil Ghahremani, Yongdae Kim. "Revisiting GPS Spoofing in Phasor Measurement: Real-World Exploitation and Practical Detection in Power Grids". *ACM Trans. Priv. Secur*.
- Yooho Jang, Ju-Hong Park, Taekkyung Oh, Yongdae Kim, Seong-Ook Park. "Passive 3-D User Equipment Tracking Using Long-Term Evolution Uplink Signals". *IEEE Trans. Instrum. Meas*.
- Tuan Dinh Hoang, Taekkyung Oh, CheolJun Park, Insu Yun, Yongdae Kim. "LLFuzz: An Over-the-Air Dynamic Testing Framework for Cellular Baseband Lower Layers". *34th USENIX Security Symposium, USENIX Security 2025, Seattle, WA, USA, August 13-15, 2025*.
- Suhwan Jeong, Beomseok Oh, Kwangmin Kim, Insu Yun, Yongdae Kim, CheolJun Park. "FirmState: Bringing Cellular Protocol States to Shannon Baseband Emulation". *18th ACM Conference on Security and Privacy in Wireless and Mobile Networks, WiSec 2025, Arlington, VA, USA, 30 June 2025- 3 July 2025*.
- Mincheol Son, Kwangmin Kim, Beomseok Oh, CheolJun Park, Yongdae Kim. "CITesting: Systematic Testing of Context Integrity Violations in LTE Core Networks". *Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security, CCS 2025, Taipei, Taiwan, October 13-17, 2025*.
- C. Park, M. Egli, B. Oh, T. Hoang, S. Jeong, M. Crettol, I. Yun, M. Payer, and Y. Kim. "OTABase: Enhancing Over-the-Air Testing to Detect Memory Crashes in Cellular Basebands". *Annual Computer Security Applications Conference (ACSAC'25)*.
- C. Kim, H. Kim, S. Lee, J. Noh, E. Ghahremani, and Y. Kim. "Enhancing synchrophasor Reliability Through Network-Based Time Synchronization: KEPCO's Practical Approach". *IEEE Power and Energy Magazine, 2025, 23 (1), 2025*.

**2024**

- Taekkyung Oh, Sangwook Bae, Junho Ahn, Yonghwa Lee, Tuan Dinh Hoang, Min Suk Kang, Nils Ole Tippenhauer, Yongdae Kim. "Enabling Physical Localization of Uncooperative Cellular Devices". *Proceedings of the 30th Annual International Conference on Mobile Computing and Networking, ACM MobiCom 2024, Washington D.C., DC, USA, November 18-22, 2024*.
- Hyungsub Kim, Rwitam Bandyopadhyay, Muslum Ozgur Ozmen, Z. berkay celik, Antonio Bianchi, Yongdae Kim, Dongyan Xu. "A Systematic Study of Physical Sensor Attack Hardness". *IEEE Symposium on Security and Privacy, SP 2024, San Francisco, CA, USA, May 19-23, 2024*.

**2023**

- Jinseob Jeong, Dongkwan Kim, Joon-Ha Jang, Juhwan Noh, Changhun Song, Yongdae Kim. "Un-Rocking Drones: Foundations of Acoustic Injection Attacks and Recovery Thereof". *30th Annual Network and Distributed System Security Symposium, NDSS 2023, San Diego, California, USA, February 27 - March 3, 2023*.
- Dongkwan Kim, Eunsoo Kim, Sang Kil Cha, Sooel Son, Yongdae Kim. "Revisiting Binary Code Similarity Analysis Using Interpretable Feature Engineering and Lessons Learned". *IEEE Trans. Software Eng*.
- Beomseok Oh, Junho Ahn, Sangwook Bae, Mincheol Son, Yonghwa Lee, Min Suk Kang, Yongdae Kim. "Preventing SIM Box Fraud Using Device Model Fingerprinting". *30th Annual Network and Distributed System Security Symposium, NDSS 2023, San Diego, California, USA, February 27 - March 3, 2023*.
- Joon-Ha Jang, ManGi Cho, Jaehoon Kim, Dongkwan Kim, Yongdae Kim. "Paralyzing Drones via EMI Signal Injection on Sensory Communication Channels". *30th Annual Network and Distributed System Security Symposium, NDSS 2023, San Diego, California, USA, February 27 - March 3, 2023*.
- Tuan Dinh Hoang, CheolJun Park, Mincheol Son, Taekkyung Oh, Sangwook Bae, Junho Ahn, Beomseok Oh, Yongdae Kim. "LTESniffer: An Open-source LTE Downlink/Uplink Eavesdropper". *Proceedings of the 16th ACM Conference on Security and Privacy in Wireless and Mobile Networks, WiSec 2023, Guildford, United Kingdom, 29 May 2023 - 1 June 2023*.
- Dohyun Kim, ManGi Cho, Hocheol Shin, Jaehoon Kim, Juhwan Noh, Yongdae Kim. "Lightbox: Sensor Attack Detection for Photoelectric Sensors via Spectrum Fingerprinting". *ACM Trans. Priv. Secur*.
- DaeGeun Yoon, Taejoong Chung, Yongdae Kim. "Delegation of TLS Authentication to CDNs using Revocable Delegated Credentials". *Annual Computer Security Applications Conference, ACSAC 2023, Austin, TX, USA, December 4-8, 2023*.
- Eunsoo Kim, Minwoo Baek, CheolJun Park, Dongkwan Kim, Yongdae Kim, Insu Yun. "BASECOMP: A Comparative Analysis for Integrity Protection in Cellular Baseband Software". *32nd USENIX Security Symposium, USENIX Security 2023, Anaheim, CA, USA, August 9-11, 2023*.

**2022**

- Sangwook Bae, Mincheol Son, Dongkwan Kim, CheolJun Park, Jiho Lee, Sooel Son, Yongdae Kim. "Watching the Watchers: Practical Video Identification Attack in LTE Networks". *31st USENIX Security Symposium, USENIX Security 2022, Boston, MA, USA, August 10-12, 2022*.
- Joongyum Kim, Jihwan Kim, Seongil Wi, Yongdae Kim, Sooel Son. "HearMeOut: detecting voice phishing activities in Android". *MobiSys ‘22: The 20th Annual International Conference on Mobile Systems, Applications and Services, Portland, Oregon, 27 June 2022 - 1 July 2022*.
- CheolJun Park, Sangwook Bae, Beomseok Oh, Jiho Lee, Eunkyu Lee, Insu Yun, Yongdae Kim. "DoLTEst: In-depth Downlink Negative Testing Framework for LTE Devices". *31st USENIX Security Symposium, USENIX Security 2022, Boston, MA, USA, August 10-12, 2022*.
- Yongdae Kim. "Cellular Security: Why is it difficult?". *ASIA CCS ‘22: ACM Asia Conference on Computer and Communications Security, Nagasaki, Japan, 30 May 2022 - 3 June 2022*.
- Jusop Choi, Wonseok Choi, William Aiken, Hyoungshick Kim, Jun Ho Huh, Taesoo Kim, Yongdae Kim, Ross j. anderson. "Attack of the Clones: Measuring the Maintainability, Originality and Security of Bitcoin 'Forks' in the Wild". *CoRR (arXiv 사전 공개본)*.
- Jeongyoon Heo, Sangwon Gil, Youngman Jung, Jinmok Kim, Donguk Kim, Woojin Park, Yongdae Kim, Kang g. shin, Choong-Hoon Lee. "Are There Wireless Hidden Cameras Spying on Me?". *Annual Computer Security Applications Conference, ACSAC 2022, Austin, TX, USA, December 5-9, 2022*.

**2021**

- Dongkwan Kim, Eunsoo Kim, Mingeun Kim, Yeongjin Jang, Yongdae Kim. "Enabling the Large-Scale Emulation of Internet of Things Firmware With Heuristic Workarounds". *IEEE Secur. Priv*.
- Eunsoo Kim, Dongkwan Kim, CheolJun Park, Insu Yun, Yongdae Kim. "BaseSpec: Comparative Analysis of Baseband Software and Cellular Specifications for L3 Protocols". *28th Annual Network and Distributed System Security Symposium, NDSS 2021, virtually, February 21-25, 2021*.
- Hoseok Seol, Minhye Kim, Taesoo Kim, Yongdae Kim, Lee-Sup Kim. "Amnesiac DRAM: A Proactive Defense Mechanism Against Cold Boot Attacks". *IEEE Trans. Computers*.

## 특허

교수 이력서 「International Patents: Granted」 절의 미국 등록 특허 5건이다. 이력서는 출원·등록 날짜를 적지 않으며, 제목·번호·발명자는 이력서 표기 그대로다.[^cv]

- Dynamic security analysis method for control plane and system therefore (번호 US11463880B2; 발명자 Y. Kim, Hongil Kim, Jiho Lee, Eunkyu Lee)
- Method for GPS spoofing detection with GPS receivers leveraging inaccuracies of GPS spoofing devices and apparatus therefore (번호 US12025713B2; 발명자 Y. Kim, Juhwan Noh, Jaehoon Kim, Dohyun Kim, Song Min Kim)
- Physical signal overshadowing attack method for LTE broadcast message and the system thereof (번호 US11405787B2; 발명자 Y. Kim, Hojoon Yang, Sangwook Bae, Mincheol Son, Hongil Kim, Song Min Kim)
- Apparatus and method for diagnosing abnormality of mobile communication network using operational logic modeling and comparative analysis (번호 USUS11082866B2; 발명자 Y. Kim, Sangwook Bae, Mincheol Son, Sooel Son)
- Apparatus and method for diagnosing anomaly in mobile communication network (번호 US10111120B2; 발명자 Y. Kim, Byeong Do Hong, Sung-Ju Lee, Shinjo Park, Hongil Kim, HyunWook Hong, Dongkwan Kim, HyunWoo Choi)

## 수상

교수 개인 누리집 「Awards & Honors」 절의 2022–2025년 항목이다. 표기는 누리집 그대로이고, ACM CCS 2025 Distinguished Paper Award를 받은 논문(CITesting, 대표 논문 1)은 그 논문 페이지와 이력서가 밝힌다.[^home][^citesting][^cv]

- 2025 · Distinguished Paper Award, ACM CCS 2025 (CITesting)
- 2025 · Member, National Academy of Engineering of Korea
- 2025 · KAIST ICT Chair Professor (2025–Present)
- 2024 · IEEE Fellow
- 2022 · Best Lecture Award, KAIST Electrical Engineering

## 연락과 위치

- 교수 연구실: (34141) 대전광역시 유성구 대학로 291 KAIST CHiPS동(N26) 201호[^contact][^ee]
- 전화: +82-42-350-7430(교내 7430)[^contact][^ee]
- 교수 이메일: yongdaek@kaist.ac.kr[^contact][^ee]
- 누리집: 교수 개인 누리집 <https://yongdaek.github.io/>. 전기및전자공학부 교수 소개의 웹사이트 칸 주소 <http://syssec.kaist.ac.kr/~yongdaek>는 이 누리집으로 연결된다.[^home][^ee]
- 공개 코드: 논문 목록의 코드 링크는 GitHub의 SysSec-KAIST 저장소(LTESniffer, LLFuzz 등)를 가리킨다.[^pubs]
[^p1]: M. Son 외, Y. Kim, Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security, 276-290 (온라인 2025-11-22). <https://doi.org/10.1145/3719027.3765230> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: T. D. Hoang 외, Y. Kim, 34th USENIX Security Symposium, USENIX Security 2025, Seattle, WA, USA, August 13-15, 2025 (2025). <https://www.usenix.org/conference/usenixsecurity25/presentation/hoang> 초록 기준(USENIX 발표 페이지 게시 초록).
[^p3]: C. Park 외, Y. Kim, 31st USENIX Security Symposium, USENIX Security 2022, Boston, MA, USA, August 10-12, 2022 (2022). <https://www.usenix.org/conference/usenixsecurity22/presentation/park-cheoljun> 초록 기준(USENIX 발표 페이지 게시 초록).
[^p4]: B. Oh 외, Y. Kim, Proceedings 2023 Network and Distributed System Security Symposium (2023). <https://doi.org/10.14722/ndss.2023.24416> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. Jeong 외, Y. Kim, Proceedings 2023 Network and Distributed System Security Symposium (2023). <https://doi.org/10.14722/ndss.2023.24112> 초록 기준(NDSS 논문 페이지 <https://www.ndss-symposium.org/ndss-paper/un-rocking-drones-foundations-of-acoustic-injection-attacks-and-recovery-thereof/> 게시 초록).
[^p6]: D. Kim 외, Y. Kim, ACM Transactions on Privacy and Security 26, 1-30 (온라인 2023-10-14). <https://doi.org/10.1145/3615867> 초록 기준.
[^p7]: C. Kim, J. Noh, E. Ghahremani, Y. Kim, ACM Transactions on Privacy and Security 28, 1-27 (온라인 2025-04-03). <https://doi.org/10.1145/3720543> 초록 기준.
[^p8]: W. Go, H. Kim, A. Oh, Y. Kim, Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 22728-22750 (2025). <https://doi.org/10.18653/v1/2025.acl-long.1108> 초록 기준(ACL Anthology 페이지 <https://aclanthology.org/2025.acl-long.1108/> 게시 초록).
[^home]: 김용대 교수 개인 누리집 첫 화면 <https://yongdaek.github.io/> (Professional Summary, Education, Interests, My Research, Experience, Awards & Honors, 2026-10-23 열람)
[^research]: 같은 누리집 Researches 절 <https://yongdaek.github.io/research/> (2026-10-23 열람)
[^cellular]: 같은 누리집 Cellular Security Research 글 <https://yongdaek.github.io/research/01_cellular_security/> (2025-01-04 게시, 2026-10-23 열람)
[^cps]: 같은 누리집 Cyber-Physical Systems Security 글 <https://yongdaek.github.io/research/02_cps_security/> (2025-01-03 게시, 2026-10-23 열람)
[^cve]: 같은 누리집 Discovered CVEs 글 <https://yongdaek.github.io/research/cve/> (2026-01-04 게시, 2026-10-23 열람)
[^pubs]: 같은 누리집 Publications 페이지 <https://yongdaek.github.io/publications/> (2026-10-23 열람)
[^citesting]: 같은 누리집 CITesting 논문 페이지 <https://yongdaek.github.io/publications/citesting-systematic-testing-of-context-integrity-violations/> (2026-10-23 열람)
[^teaching]: 같은 누리집 Teaching 페이지 <https://yongdaek.github.io/teaching/> (2026-10-23 열람)
[^contact]: 같은 누리집 Contact 페이지 <https://yongdaek.github.io/contact/> (2026-10-23 열람)
[^cv]: 같은 누리집에 올린 교수 이력서 <https://yongdaek.github.io/uploads/resume.pdf> (2026-10-23 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(김용대) <https://ee.kaist.ac.kr/professor/12306/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 웹사이트, 디비전, 학위, 2026-10-23 열람)
[^gst]: KAIST 안보과학기술대학원 교수진 목록 1쪽 <https://gst.kaist.ac.kr/member/faculty/> (소속학과, 연구분야, 세부 연구 분야, 연구실, 2026-10-23 열람)

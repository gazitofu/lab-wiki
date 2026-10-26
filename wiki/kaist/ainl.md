# AI-Native Networking Lab (AINL)

**KAIST 전기및전자공학부 · 최성현 교수**

- 분야: AI 네이티브 네트워킹, AI-RAN(인공지능을 넣은 무선 접속망), 자율 네트워크 운영, 엣지·클라우드 협업 인공지능 서비스, 차세대 통신 인프라와 테스트베드
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 무선·이동통신[^research][^home], 컴퓨터 네트워크[^research], AI 시스템·인프라[^research], 대형 언어 모델[^notice], 엣지 컴퓨팅·엣지 AI[^research], 다중 에이전트 시스템·분산 의사결정[^notice]
- 홈페이지: <https://ainl.kaist.ac.kr> (교수 개인 누리집 <https://sites.google.com/view/sunghyun-chois-home>)
- 근거와 출처: [AINL 근거 페이지](ainl-sources.md)

> 이동통신망을 인공지능이 설계와 운영의 중심에 있는 망으로 다시 짜는 연구실이다. 인공지능을 넣은 무선 접속망, 인공지능 에이전트가 스스로 망을 운영하는 자율 네트워크, 망 가까이에서 인공지능 서비스를 돌리는 엣지 인공지능, 클라우드 방식의 통신 인프라를 하나의 시스템으로 다루고, 실제로 돌아가는 테스트베드에서 검증한다.[^home][^research]

## 무엇을 연구하나

AINL은 최성현 교수가 2026년 4월 KAIST 전기및전자공학부에 부임하면서 연 연구실이다.[^news][^notice][^people] 누리집은 네트워크가 인공지능 시스템이 되어 가고 있다고 보고, 인공지능과 네트워크, 차세대 통신 인프라가 만나는 곳에서 실제로 돌아가는 시스템을 만든다고 소개한다.[^home] 연구 페이지는 미래 네트워크가 연결만 제공하는 기반 시설에서 인공지능 서비스와 자율 운영, 현실 세계의 디지털 전환을 떠받치는 지능형 플랫폼으로 바뀌고 있다고 적는다.[^research] 첫 화면이 내세우는 말은 「네트워크를 위한 인공지능, 인공지능을 위한 네트워크(AI for the network, network for AI)」이고, 무선 구간부터 인공지능 서비스까지를 따로 만든 두 시스템이 아니라 하나의 시스템으로 설계하겠다고 밝힌다.[^home]

연구 페이지는 연구를 네 영역으로 나눈다. 인공지능을 중심에 둔 무선 접속망(AI-RAN), 스스로 운영되는 자율 네트워크 시스템, 망 가까이에서 인공지능 서비스를 돌리는 엣지 인공지능, 클라우드 방식으로 짓는 차세대 통신 인프라다.[^research] 연구 페이지는 연구 철학으로 따로 떨어진 알고리즘이나 개념 모형을 넘어 시스템 전체를 설계·구현·검증하는 일, 산업계·공공 부문 협력자와 함께 통신 인프라와 인공지능 서비스의 실제 문제를 푸는 일, 네트워크와 인공지능이 서로를 바꾸는 접점을 연구하는 일을 든다.[^research] 장기 목표는 무선·엣지·클라우드에 걸쳐 스스로 상황을 감지하고 판단하고 최적화하고 적응하는 네트워크 시스템이다.[^research]

연구실은 AI-RAN 에뮬레이션 테스트베드(testbed, 새 기술을 실제에 가까운 조건에서 시험하려고 갖춘 실험 설비)를 운영한다.[^research] 코어망(core network, 이동통신망에서 가입자 인증과 데이터 경로를 관리하는 중심부), 무선 접속망, 단말 장치로 이루어진 공개 소스 5G 시스템 전체를 실시간 제어기 아래에서 돌리고, 연구실이 직접 만든 이동 시뮬레이터로 움직인다.[^research] 전파를 실제로 공중에 보내는 대신 시뮬레이터가 각 단말을 실제 도로 경로를 따라 움직이고, 그 결과로 생기는 통신 채널을 시스템에 넣는다.[^research] 망 성능과 장비 상태, 단말 위치를 한 화면에 모아 보고, 실험 시나리오를 파일로 적어 두어 같은 실험을 그대로 다시 할 수 있게 한다.[^research] 연구 페이지는 여러 단말이 실제 도로를 동시에 달리는 다중 단말 이동 시뮬레이터와, 두 셀(cell, 기지국 하나가 맡는 통신 구역) 사이를 오가는 단말의 핸드오버를 경로 위에 표시하는 핸드오버 시뮬레이터를 연구실이 직접 만든 도구로 소개한다.[^research]

전기및전자공학부의 부임 안내는 최성현 교수가 KAIST에서 AI 네이티브 네트워크 구조, LLM(대형 언어 모델)과 멀티 에이전트 시스템(여러 인공지능 에이전트가 나눠 맡고 협력하는 시스템)을 바탕으로 한 자율 네트워크 운영, 물리 세계에서 움직이는 인공지능(Physical AI)을 위한 차세대 네트워크 인프라를 중심으로 연구와 교육을 할 예정이라고 밝힌다.[^notice] 2026년 가을학기에는 AI-Native Networking 과목(EE49904)을 처음 열었다.[^news] 누리집 논문 목록에는 KAIST 부임 뒤의 논문이 아직 올라 있지 않고, 2021–2023년 논문은 교수가 삼성전자에 있던 때의 논문이다(아래 「최근 논문 목록」).[^pubs][^bg]

## 주요 연구 주제

### 1. AI 네이티브 네트워킹과 AI-RAN

미래 이동통신망을 인공지능을 중심에 두는 플랫폼으로 다시 설계하는 방법을 연구한다.[^research] 여기에는 AI-RAN 구조, RAN(Radio Access Network, 휴대폰 같은 단말과 기지국을 무선으로 잇는 이동통신망의 접속 구간) 지능화, 인공지능을 활용한 무선·망 최적화, 인공지능 작업과 통신 시스템 사이의 상호작용이 들어간다.[^research] 연구 페이지가 이 영역의 낱말로 드는 것은 AI-RAN, 5G-Advanced, 6G, RAN intelligence, O-RAN(Open RAN, 장비 사이의 연결 규격을 공개해 여러 회사의 장비를 함께 쓸 수 있게 한 무선 접속망 구조), 망 상태를 고려하는 인공지능(network-aware AI), 인공지능 작업을 고려하는 네트워킹(AI-aware networking)이다.[^research] 지금 하고 있는 일로는 미래 이동통신망을 위한 AI 네이티브 구조와 AI-RAN·지능형 무선 접속망 제어를 든다.[^research]

### 2. 자율 네트워크 시스템

데이터에 기반한 관측성(observability, 측정 데이터로 시스템 내부 상태를 알아낼 수 있는 정도), 폐루프 자동화(closed-loop automation, 상태를 재고 그 결과로 설정을 바꾸는 과정을 사람 손 없이 되풀이하는 자동화), 인공지능 에이전트로 통신망을 스스로 운영하는 방법을 연구한다.[^research] 망이 스스로를 지켜보고, 운영자의 의도를 이해하고, 이상을 감지하고, 사람의 개입을 줄인 채 상황에 맞게 최적화하는 방법을 찾는다.[^research] 연구 페이지가 드는 낱말은 자율 네트워크, 폐루프 자동화, 관측성, 인공지능 에이전트, 의도 기반 네트워킹(intent-based networking, 운영자가 원하는 결과를 지정하면 망이 그에 맞는 설정을 찾아 적용하는 방식), xApp·rApp, 준실시간·비실시간 RIC(RAN Intelligent Controller, 무선 접속망을 소프트웨어로 감시하고 제어하는 제어기)다.[^research] 지금 하고 있는 일로 인공지능 에이전트를 이용한 자율 망 운영, 준실시간·비실시간 RIC와 xApp·rApp, 통신망의 관측성과 폐루프 자동화를 든다.[^research] 부임 안내는 이 방향을 LLM과 멀티 에이전트 시스템을 바탕으로 한 자율 네트워크 운영으로 적는다.[^notice]

### 3. 엣지 인공지능과 현실 세계 인공지능 서비스

지연이 짧고 믿을 만하며 상황을 고려하는 인공지능 서비스를 위해, 엣지(edge, 사용자와 가까운 망 쪽 장비)와 클라우드가 함께 일하는 인공지능 시스템을 만든다.[^research] 연구 페이지가 드는 응용은 로봇, 스마트 캠퍼스 서비스, 지능형 이동 수단, 첨단 네트워크 인프라 위의 멀티모달 인공지능 서비스이고, 낱말로 엣지 인공지능, 분산 추론, 지연이 짧은 인공지능 서비스, 캠퍼스 네트워크를 든다.[^research] 지금 하고 있는 일로 엣지·클라우드 협업 인공지능 추론과 로봇·현실 세계 인공지능 서비스를 위한 네트워크 인프라를 든다.[^research]

### 4. 차세대 통신 인프라

앞으로의 인공지능 서비스를 위해 프로그래밍할 수 있고, 클라우드 방식으로 만들고, 규모를 키울 수 있는 통신 인프라를 연구한다.[^research] 여기에는 텔코 클라우드(telco cloud, 통신사의 망 기능을 전용 장비 대신 범용 서버의 클라우드 소프트웨어로 돌리는 방식), 가상화, Kubernetes(여러 서버에 프로그램을 나눠 배치하고 관리하는 공개 소스 소프트웨어) 기반 네트워크 플랫폼, 프로그래밍할 수 있는 전송망, 미래 망 구조를 검증하는 대규모 테스트베드가 들어간다.[^research] 지금 하고 있는 일로 5G-Advanced와 6G 시스템을 위한 확장 가능한 테스트베드를 든다.[^research] 2026년 10월 소식에 따르면 연구실은 국산 장비로 만든 AI-RAN 테스트베드를 KAIST·서울대학교·연세대학교에 깔고 KOREN 망으로 잇는 국가 AI-RAN 캠퍼스 테스트베드 사업의 KAIST 거점을 맡는다.[^news]

## 교수와 전문 분야

최성현 교수(Sunghyun Choi)는 2026년 4월부터 KAIST 전기및전자공학부 교수(정년 보장)이고, AI시스템학과 겸임교수와 AINL 책임자를 맡는다.[^bg][^phome][^people] 전기및전자공학부 교수 소개는 직위 칸에 IEEE 석학회원(IEEE Fellow)을 적고, 디비전을 Computer·Communication으로, 주요 연구분야를 AI & Machine Learning, Information, Communication & Coding, Big Data, Software Systems & Networking으로, 주요 연구를 AI-Native Network, Wireless Networking, Mobile System/Computing으로 적는다.[^ee] 부임 안내는 교수를 무선 네트워킹과 모바일 시스템 분야의 연구자로 소개하고, 그동안의 주요 연구 분야를 디지털 트윈(실제 대상을 컴퓨터 안에 재현한 모형) 기반 지능형 네트워크 최적화, 차세대 무선통신·네트워크 기술, 저지연 모바일 시스템, 모바일 기기 기반 위치 추정과 인식 기술로 든다.[^notice]

KAIST에서 전기공학 학사(1992, 최우등)와 석사(1994)를, 미국 University of Michigan, Ann Arbor에서 전기공학·컴퓨터과학 박사(1999)를 받았다.[^bg][^notice] 1999년부터 2002년까지 미국 Philips Research USA의 Senior Member of Research Staff로 있으면서 IEEE 802.11 무선랜(와이파이 표준) 과제를 이끌었다.[^bg][^people] 2002년 9월부터 2019년 8월까지 서울대학교 교수(조교수 2002–2006, 부교수 2006–2011, 교수 2011–2019, 학과 표기 Department of Electrical Engineering, Department of Electrical and Computer Engineering)로 있었고, 이 기간에 공과대학 교무부학장(Vice Dean of Academic Affairs, 2017–2019)을 지냈으며 2009–2010년에는 미국 Stanford University 방문 부교수였다.[^bg] 서울대 시절 연구실 이름은 MWNL(Multimedia & Wireless Networking Laboratory)이었고, 17년 동안 와이파이·셀룰러·모바일 시스템을 연구했다.[^alumni] 2000–2007년 IEEE 802.11 작업반의 투표 회원이었고, 2000–2012년에 IEEE 802.11 표준 기고문을, 2005년에 Zigbee 표준 기고문을 냈다.[^board][^std]

2019년 9월부터 2025년 12월까지 삼성전자에 있었다.[^bg][^notice] Samsung Research의 Advanced Communications Research Center 센터장(Senior Vice President 2019–2021, Executive Vice President 2021–2024)으로 6G·5G Advanced·사물인터넷 연결의 연구와 표준화를 이끌었고, 이어 Samsung Networks의 Advanced R&D Team 팀장(Executive Vice President, 2023–2025)으로 망의 계획·구축·운영·최적화를 자동화하는 인공지능 기반 클라우드 플랫폼 Samsung CognitiV NOS의 개발을 이끌었다. 부임 안내는 이 직위를 삼성전자 부사장으로 적는다.[^bg] 교수 누리집은 이 시기의 일로 삼성전자의 6G 비전 백서(2020)와 6G 주파수 백서(2022)를 들고, 교수는 IEEE ICC 2022, ACM MobiHoc 2022 등에서 6G를 주제로 기조연설을 했다.[^samsung][^talks]

교수는 270편이 넘는 논문을 함께 썼고 200건이 넘는 특허를 가지고 있다고 소개한다.[^bg] 전기및전자공학부 교수 소개가 드는 대표업적은 지능형 네트워크를 위한 디지털 트윈(IEEE Communications Magazine, 2023), 밀리미터파(파장이 밀리미터 단위인 높은 주파수의 전파) 대역에서 고출력 전이중(full duplex, 같은 주파수에서 동시에 보내고 받는 방식) 통신을 구현한 설계·시제품(IEEE Journal on Selected Areas in Communications, 2023), 웨어러블 카메라로 붐비는 도시 공간에서 사람을 식별하는 EagleEye(ACM MobiCom, 2020), 클라우드의 도움을 받아 모바일 기기에서 지연이 짧은 초해상도(super-resolution, 낮은 해상도의 영상에서 더 세밀한 영상을 만들어 내는 처리) 처리를 하는 Supremo(IEEE Transactions on Mobile Computing, 2020), 사람 개입 없는 스마트폰 기반 실내 경로 추정과 위치 측정(IEEE Transactions on Mobile Computing, 2020) 다섯 편이다.[^ee] 학술지 편집으로는 IEEE Transactions on Mobile Computing의 Associate Editor(2007–2013), IEEE Transactions on Wireless Communications의 Editor(2014–2018), IEEE Wireless Communications Magazine의 Technical Editor(2010–2015) 등을 지냈다.[^editor]

교수 개인 누리집이 드는 주요 영예는 IEEE Fellow(2014), KICS(한국통신학회) Dr. Irwin Jacobs Award(2013), National Academy of Engineering of Korea의 Award of Excellence(2013, 2020년 한국을 이끌 100대 기술의 주역 선정), Young Scientist Award, President of Korea(2008, 제11회 젊은과학자상), IEEK/IEEE IT 젊은과학기술자상(2007)이다.[^recog] 2020년에는 부총리 겸 교육부장관 표창을 받았고, 2008년 IEEE WoWMoM에서 Best Paper Award를 받았다.[^recog] 6G Forum의 Co-Chair(2024–2025)와 Advisory Committee Member(2024년 4월부터), 한국통신학회 산업계 협동부회장(2021, 2024, 2025), 과학기술정보통신부 제5차 과학기술기본계획(2023–2027) 수립위원회 위원(2022), 한국정보통신기술협회(TTA) 이사(2020–2022)를 지냈다.[^board]

## 응용 분야

연구 페이지가 드는 쓰임은 로봇, 스마트 캠퍼스 서비스, 지능형 이동 수단, 첨단 네트워크 인프라 위의 멀티모달 인공지능 서비스다.[^research] 2026년 10월 소식에 따르면 국가 AI-RAN 캠퍼스 테스트베드 사업의 KAIST 테스트베드는 10월 말 설치될 예정이고, 캠퍼스를 오가는 자율 배달 로봇으로 시연한다. 이 사업은 Newgens가 HFR과 함께 이끌며 2027년 12월까지 이어진다.[^news] 부임 안내는 물리 세계에서 움직이는 인공지능을 위한 차세대 네트워크 인프라를 KAIST에서의 연구 방향으로 든다.[^notice]

## 구성원

누리집 People 페이지의 석사과정 2명, 학부 연구생 3명(누리집 표기 Undergraduate Individual Research), 방문 연구원 1명, 여름 인턴 1명(2026년 6–8월)이다. 시작 시점과 연구 주제는 페이지 표기 그대로다.[^people] 첫 석사과정 학생 두 명은 2026년 가을학기에 들어왔다.[^news]

| 이름 | 과정 | 시작 | 연구 주제 |
|---|---|---|---|
| Kyuhee Bak | 석사과정 | 2026.8 – present | AI-RAN, 6G, O-RAN, 5G-Advanced, and wireless network systems |
| Duc Cuong Nguyen | 석사과정 | 2026.8 – present | AI-RAN, 5G-Advanced, 6G, RAN intelligence, and O-RAN |
| Sujeong Jeon | 학부 연구생 | 2026.4 – present | AI-RAN |
| Junhwan Heo | 학부 연구생 | 2026.5 – present | AI-RAN and wireless network design |
| Jinhwan Kim | 학부 연구생 | 2026.9 – present | AI-native networking, edge computing, and network infrastructure for physical AI |
| Andrew Younghoon Choi | 방문 연구원 (KAIST AI FX / prev UC Berkeley EECS) | 2026.5 – present | AI systems, social computing, NLP, and AI for communications |
| Eunwoo Won | 인턴 (Iowa State University) | 2026.6 – 2026.8 | AI ethics, responsible AI, human-centered AI, applied AI, and AI-powered web applications |

## 졸업생과 이전 구성원 (서울대 MWNL)

누리집 Alumni 페이지의 107줄이다. 모두 교수가 서울대학교에서 이끈 MWNL(2002–2019) 시절의 사람들로, KAIST의 AINL 졸업생이 아니다. 누리집 구분대로 교수가 지도한 박사 졸업생 21명(2008–2019)과 석사 졸업생 31명(2005–2019), 교수가 2019년 삼성전자로 옮길 때 연구실에 있던 구성원 22명(「2019년 MWNL 구성원」, 대부분 다른 서울대 교수의 지도로 학위를 마쳐 진로 칸에 지도교수를 함께 적었다), 방문·연구 교수 6명, 박사후연구원 4명, 연구원·인턴 23명 순이다. 학위·직위와 연월, 진로는 누리집 표기 그대로다. 누리집은 이 명단을 2019년 8월의 서울대 기록에서 옮긴 뒤 2026년 7월에 졸업생들이 직접 고쳤다고 밝히며, 진로 칸의 "as of 2019"는 2019년 기록 그대로이고 그 뒤 확인되지 않았다는 표시라고 적는다. 한 사람이 인턴·박사후연구원과 졸업생 두 줄에 함께 오른 경우가 있다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Sunggeun Jin | Ph.D. (Aug. 2008) | Professor, Daegu University, Korea (as of 2019) |
| Youngsoo Kim | Ph.D. (Feb. 2009) | Mobile eXperience, Samsung Electronics, Korea |
| Seongkwan Kim | Ph.D. (Feb. 2009) | Network Group, KT, Korea |
| Youngkyu Choi | Ph.D. (Feb. 2009) | Network Division, Samsung Electronics, Korea |
| Jeonggyun Yu | Ph.D. (Feb. 2009) | System LSI, Samsung Electronics, Korea (as of 2019) |
| Kwanghun Han | Ph.D. (Feb. 2011) | Mobile eXperience, Samsung Electronics, Korea |
| Dongmyoung Kim | Ph.D. (Feb. 2012) | Samsung Research, Samsung Electronics, Korea |
| Munhwan Choi | Ph.D. (Aug. 2013; also M.S. 2007) | Mobile eXperience, Samsung Electronics, Korea |
| Edwin Monroy | Ph.D. (Feb. 2014) | Ericsson, Sweden (as of 2019); Co-advised with Prof. Junseok Hwang |
| Hyewon Lee | Ph.D. (Aug. 2014) | Apple Inc., CA, USA |
| Wonbo Lee | Ph.D. (Feb. 2015) | Mobile Division, Samsung Electronics, Korea (as of 2019) |
| Okhwan Lee | Ph.D. (Feb. 2015) | Network Division, Samsung Electronics, Korea |
| Jongwoo Hong | Ph.D. (Feb. 2016) | InterDigital, USA |
| Seungmin Yoo | Ph.D. (Aug. 2016; also M.S. 2011) | Mobile eXperience, Samsung Electronics, Korea |
| Weiping Sun | Ph.D. (Feb. 2017) | Samsung Research, Samsung Electronics, Korea |
| Yeonchul Shin | Ph.D. (Aug. 2017) | Network Division, Samsung Electronics, Korea |
| Jonghoe Koo | Ph.D. (Aug. 2017) | Samsung Research, Samsung Electronics, Korea (as of 2019) |
| Seongwon Kim | Ph.D. (Aug. 2017; also M.S. 2013) | SK Telecom, Korea |
| Seongho Byeon | Ph.D. (Feb. 2018; also M.S. 2013) | Samsung Research, Samsung Electronics, Korea |
| Seungil Park | Ph.D. (Aug. 2018; also M.S. 2013) | Samsung Research, Samsung Electronics, Korea |
| Kangjin Yoon | Ph.D. (Feb. 2019) | Siemens Healthineers, USA |
| Jaehyuk Jang | M.S. (Feb. 2005) | Samsung Research, Samsung Electronics, Korea |
| Jongseok Kim | M.S. (Feb. 2006) |  |
| Tae Hyun Kim | M.S. (Feb. 2006) | CEO, Geniefy, Inc., Korea |
| Kihwan Choi | M.S. (Feb. 2006) | Seoul National University of Science & Technology, Korea; Ph.D., Stanford University |
| Alexey Sidelnikov | M.S. (Feb. 2006) | Venuiti Solutions, Inc., Canada |
| Maria Samokhina | M.S. (Feb. 2008) | Google, Switzerland |
| Kirill Moklyuk | M.S. (Aug. 2008) | Swisscom, Switzerland |
| Lochan Verma | M.S. (Aug. 2008) | Apple Inc., CA, USA |
| Hua Cai | M.S. (Feb. 2009) | Kookmin Bank, Beijing, China (as of 2019) |
| Minsoo Na | M.S. (Feb. 2009) | SK Telecom, Korea (as of 2019) |
| Youngwoo Hwang | M.S. (Feb. 2009) | No update yet |
| Kiran Tharanath | M.S. (Aug. 2009) | Network Division, Samsung Electronics, Korea (as of 2019) |
| Seungmin Woo | M.S. (Feb. 2010) | Texas Instruments, Korea (as of 2019) |
| Changyeon Yeo | M.S. (Feb. 2010) | Mobile Division, Samsung Electronics, Korea |
| Suhwook Kim | M.S. (Feb. 2010) | Samsung Research, Korea |
| Jonghee Lee | M.S. (Feb. 2010) |  |
| Du Ho Kang | M.S. (Aug. 2010) | Ericsson Research, Sweden (as of 2019); Ph.D., KTH, Sweden |
| Kyuhwan Kwak | M.S. (Feb. 2011) | CJ Investment, Korea |
| Seunghyun Choi | M.S. (Feb. 2011) | Network Division, Samsung Electronics, Korea |
| Byoungjin Kim | M.S. (Feb. 2012) | Prosecutor, Korea |
| Hyunwoo Kim | M.S. (Feb. 2012) |  |
| Byungkab Jo | M.S. (Aug. 2012) | Korea Electric Power Corporation (KEPCO), Korea |
| Ildefonso de la Cruz | M.S. (Aug. 2012) | Omdia, London, UK |
| Tianyu Piao | M.S. (Aug. 2013) | China Mobile Communications Corporation HQ, Beijing, China (as of 2019) |
| Jihoon Seo | M.S. (Feb. 2014) | Electronics and Telecommunications Research Institute (ETRI), Korea |
| Soonwon Ka | M.S. (Feb. 2016) | Coupang, Korea |
| Taejun Park | M.S. (Aug. 2018) | Hyundai Rotem, Korea |
| Juheon Yi | M.S. (Aug. 2018) | Microsoft Research Asia; Ph.D., Seoul National University |
| Hwijae Kwon | M.S. (Feb. 2019) | Naver, Korea |
| Minseok Jang | M.S. (Aug. 2019) | Korea Credit Information Services, Korea |
| Byungjun Kim | M.S. (Aug. 2019) | Postdoctoral Researcher, Rutgers University, USA (as of 2019); Ph.D., University of California, San Diego |
| Gyujin Lee | 2019년 MWNL 구성원, Ph.D. (Feb. 2020) | Mobile eXperience, Samsung Electronics, Korea; Advised by Prof. Saewoong Bahk |
| Changmok Yang | 2019년 MWNL 구성원, Ph.D. (Feb. 2020) | Mobile eXperience, Samsung Electronics, Korea; Advised by Prof. Saewoong Bahk |
| Sundo Kim | 2019년 MWNL 구성원, Ph.D. (Feb. 2020) | Samsung Research, Samsung Electronics, Korea; Advised by Prof. Byonghyo Shim |
| Junseok Kim | 2019년 MWNL 구성원, Ph.D. (Aug. 2020) | System LSI, Samsung Electronics, Korea; Advised by Prof. Saewoong Bahk |
| Hoyoung Yoon | 2019년 MWNL 구성원, Ph.D. (Aug. 2020) | Samsung Research, Samsung Electronics, Korea; Advised by Prof. Saewoong Bahk |
| Junyoung Choi | 2019년 MWNL 구성원, Ph.D. (Aug. 2020) | Samsung Research, Samsung Electronics, Korea; Advised by Prof. Saewoong Bahk |
| Youngwook Son | 2019년 MWNL 구성원, Ph.D. (Aug. 2020) | University of Colorado Boulder, USA; Advised by Prof. Saewoong Bahk |
| Jaehong Yi | 2019년 MWNL 구성원, Ph.D. (Feb. 2021) | Mobile eXperience, Samsung Electronics, Korea; Advised by Prof. Saewoong Bahk |
| Jihoon Kim | 2019년 MWNL 구성원, Ph.D. (Aug. 2021) | System LSI, Samsung Electronics, Korea; Advised by Prof. Saewoong Bahk |
| Kitaek Lee | 2019년 MWNL 구성원, Ph.D. (Aug. 2022) | Samsung Research, Samsung Electronics, Korea; Advised by Prof. Saewoong Bahk |
| Chulyoung Kwak | 2019년 MWNL 구성원, Ph.D. (Aug. 2023) | Advanced Vehicle Platform, Hyundai Motor Company, Korea; Advised by Prof. Saewoong Bahk |
| Sunwook Hwang | 2019년 MWNL 구성원, Ph.D. (Aug. 2023) | System LSI, Samsung Electronics, Korea; Advised by Prof. Saewoong Bahk |
| Jaewon Hur | 2019년 MWNL 구성원, Ph.D. (Aug. 2023) | Apple Inc., USA; Advised by Prof. Byoungyoung Lee |
| Kanghyun Lee | 2019년 MWNL 구성원, Ph.D. (Feb. 2025) | Mobile eXperience, Samsung Electronics, Korea; Advised by Prof. Saewoong Bahk |
| Jihwan Lee | 2019년 MWNL 구성원, Ph.D. Student | No update yet |
| Suhun Lim | 2019년 MWNL 구성원, M.S. (Feb. 2020) | Memory Division, Samsung Electronics, Korea; Advised by Prof. Saewoong Bahk |
| Kyungjin Lee | 2019년 MWNL 구성원, M.S. (Feb. 2020) | Ph.D. student; Advised by Prof. Youngmin Kim / Prof. Youngki Lee |
| Hanyeoreum Bae | 2019년 MWNL 구성원, M.S. Student | No update yet |
| Heejin Yang | 2019년 MWNL 구성원, M.S. Student | Ph.D. student, University of Michigan, USA |
| Jinmyeong Lee | 2019년 MWNL 구성원, M.S. Student | No update yet |
| Kayondo Martin | 2019년 MWNL 구성원, Research Intern | No update yet |
| Minwoo Kim | 2019년 MWNL 구성원, Research Intern | No update yet |
| Kyung-Joon Park | Visiting Professor (Jul. 2010 – Jan. 2011) | Professor, Electrical Engineering and Computer Science, DGIST, Korea |
| Bijan Jabbari | Visiting Professor (Feb. – Jun. 2011) | Professor, Electrical and Computer Engineering, George Mason University, USA; Also Professeur Associé, Télécom Paris, Institut Polytechnique de Paris. |
| Wei Xiang | Visiting Professor (May 2011) | Distinguished Professor and Cisco Chair of AI and IoT, La Trobe University, Australia |
| Bo Ryu | Visiting Professor (May – Sep. 2013) | Applied Intuition, USA; Co-founder and CEO of EpiSci (EpiSys Science) until Applied Intuition acquired it in February 2025. |
| Jonghan Lim | Research Professor (2019) | No update yet; Dates not recorded in the archive. |
| Ji-Woong Choi | Visiting Professor (2019) | Professor, Electrical Engineering and Computer Science, DGIST, Korea; Dates not recorded in the archive. |
| Ilenia Tinnirello | Postdoctoral Fellow (Mar. – Nov. 2004) | Professor, Department of Engineering, University of Palermo, Italy |
| Lei Wang | Postdoctoral Fellow (Mar. – Dec. 2006) | Professor, School of Software, Dalian University of Technology, China |
| Weiping Sun | Postdoctoral Fellow (May 2017 – Apr. 2018; also Ph.D. 2017) | Samsung Research, Samsung Electronics, Korea |
| Seongwon Kim | Postdoctoral Fellow (Sep. 2017 – Feb. 2019; also Ph.D. 2017) | SK Telecom, Korea |
| Jeongyeup Paek | Research Intern (Jan. – Jun. 2003) | Professor, Computer Science and Engineering, Chung-Ang University, Korea; Ph.D., University of Southern California |
| Sekyu Park | Research Scientist (Jan. 2003 – Jun. 2005) | Broadcom Corp., USA (as of 2019) |
| Tae Hyun Kim | Research Intern (Mar. – Jul. 2006; also M.S. 2006) | CEO, Geniefy, Inc., Korea |
| Kihwan Choi | Research Intern (Mar. – Jun. 2006; also M.S. 2006) | Seoul National University of Science & Technology, Korea; Ph.D., Stanford University |
| Heeyoung Lee | Research Scientist (Apr. 2007 – Jun. 2008) | Member of Technical Staff, OpenAI, USA; Ph.D., Stanford University |
| Sang Phil Moon | Research Intern (Mar. – Dec. 2008) | Malgun Miso Dental Clinic, Korea (as of 2019) |
| Seunghyun Choi | Research Intern (Mar. – Aug. 2011; also M.S. 2011) | Network Division, Samsung Electronics, Korea |
| Juno Kim | Research Intern (Apr. – Sep. 2011) | Three Line Technologies, Inc., Korea (as of 2019) |
| Taejun Park | Research Intern (Jul. 2011 – Aug. 2012; also M.S. 2018) | Hyundai Rotem, Korea |
| Changmok Yang | Research Intern (Jul. 2012 – Feb. 2013; also Ph.D. 2020) | Mobile eXperience, Samsung Electronics, Korea |
| Kyuhwan Kwak | Research Scientist (Oct. 2012 – Jun. 2015; also M.S. 2011) | CJ Investment, Korea |
| Seongho Byeon | Research Intern (Mar. – Aug. 2013; also Ph.D. 2018) | Samsung Research, Samsung Electronics, Korea |
| Seongwon Kim | Research Intern (Mar. – Aug. 2013; also Ph.D. 2017) | SK Telecom, Korea |
| Youngwook Son | Research Intern (Feb. – Aug. 2013; also Ph.D. 2020) | University of Colorado Boulder, USA |
| Seungil Park | Research Intern (Sep. 2013 – Feb. 2014; also Ph.D. 2018) | Samsung Research, Samsung Electronics, Korea |
| Changwung Jo | Research Intern (Nov. – Dec. 2015) | Undergraduate student, SNU, Korea (as of 2019) |
| Jaewon Hur | Research Intern (Dec. 2015 – Jan. 2016; also Ph.D. 2023) | Apple Inc., USA |
| Ingab Kang | Research Intern (Jan. – May 2016) | Undergraduate student, SNU, Korea (as of 2019) |
| Sangwon Park | Research Intern (Jan. – Feb. 2016) | Undergraduate student, SNU, Korea (as of 2019) |
| Juheon Yi | Research Intern (Feb. – Aug. 2016; also M.S. 2018) | Microsoft Research Asia; Ph.D., Seoul National University |
| Kanghyun Lee | Research Intern (Feb. – Aug. 2016; also Ph.D. 2025) | Mobile eXperience, Samsung Electronics, Korea |
| Sengchan Ryu | Research Intern (Jan. – Feb. 2017) | Undergraduate student, SNU, Korea (as of 2019) |
| Joonho Park | Research Intern (Jul. – Aug. 2017) | Carnegie Mellon University, USA (as of 2019) |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지는 교수의 논문 목록을 옮겨 적은 것으로, 1995년부터 2023년까지 289편(학술지·매거진 95편, 국제 학회·워크숍 182편, 책·책 속 장 7편, 편집 서문 5편)을 싣는다.[^pubs] 아래는 그 가운데 2021–2023년 13편(2023년 2편, 2022년 7편, 2021년 4편)이다. 이 논문들은 교수가 삼성전자에 있던 때(2019년 9월–2025년 12월)의 논문이라 현재 KAIST 연구실의 성과로 묶지 않으며, 목록에는 2024년 이후 논문이 없다.[^pubs][^bg] 저자 순서와 제목·학술지·학회 표기는 누리집 그대로다.[^pubs]

**2023**

- B Yu, C Qian, J Lee, S Shao, Y Shen, W Pan, P Lin, Z Zhang, S Kim, S Hu, K Lee, J Jung, S Choi, C Sun. "Realizing High Power Full Duplex in Millimeter Wave System: Design, Prototype and Results". *IEEE Journal on Selected Areas in Communications, June 2023*.
- S Jang, J Jeong, J Lee, S Choi. "Digital Twin for Intelligent Network: Data Lifecycle, Digital Replication, and AI-based Optimizations". *IEEE Communications Magazine, Aug. 2023*.

**2022**

- B Yu, C Qian, J Lee, S Shao, Y Shen, W Pan, P Lin, Z Zhang, J Jung, S Choi, C Sun, S Hu. "Realizing High Power Millimeter Wave Full Duplex: Practical Design, Prototype and Results". *IEEE Globecom, 2022*.
- D Je, A Deshmukh, S Cho, D Kim, N Sharma, J Jung, J Lee, S Choi. "Selective User Plane (UP) Security for Throughput Enhancement in Mobile Communication". *IEEE Globecom Workshops (GC Wkshps), 2022*.
- D Jung, CJ Park, JW Seo, TS Kwon, JG Jeong, SH Wi, I Na, S Choi. "Stub-Loaded Sub-Terahertz Wideband Antenna Design and Measurement". *16th European Conference on Antennas and Propagation (EuCAP), 1-4, 2022*.
- J Cha, YG Moon, S Cho, D Kim, J Choi, J Jung, J Lee, S Choi. "RAN-CN Converged User-Plane for 6G Cellular Networks". *IEEE Globecom, 2022*.
- J Choi, N Sharma, SS Gantha, V Mandawaria, J Cha, D Kim, J Jung, J Lee, S Choi. "RAN-CN Converged Control-Plane for 6G Cellular Networks". *IEEE Globecom, 2022*.
- S Kim, K Lee, Y Bin, C Qian, J Jung, J Lee, S Choi. "Measurement and System-level Evaluation of Inter-Sector Self-Interference on Full Duplex in mmWave Band". *IEEE ICC 2022, May 2022*.
- S Lee, W Jeong, J Jung, J Lee, S Choi. "A New Preamble Signal Design for Random Access in Sub-Terahertz 6G Cellular Systems". *IEEE ICC Workshop, May 2022*.

**2021**

- DH Je, J Jung, S Choi. "Toward 6G Security: Technology Trends, Threats, and Solutions". *IEEE Communications Standards Magazine, 5 (3), pp. 64-71, 2021*.
- H Jang, S Jang, Y Park, J Jung, J Lee, S Choi. "SeqNet: Data-Driven PAPR Reduction via Sequence Classification". *2021 IEEE Globecom Workshops (GC Wkshps), 2021*.
- M Choi, K Kim, H Jang, H Woo, JS Pujol-Roig, Y Wang, H Yeon, S Choi. "Cell On/Off Parameter Optimization for Saving Energy via Reinforcement Learning". *2021 IEEE Globecom Workshops (GC Wkshps), 2021*.
- SH Kim, BH Jung, J Jung, J Lee, S Choi. "ODC: Orchestration for Dynamic Coupling between Satellites and Cells via Reinforcement Learning". *2021 IEEE Globecom Workshops (GC Wkshps), 2021*.

## 특허

교수 개인 누리집 Patents 페이지의 미국·한국 특허 가운데 등록일이 2021년 10월 13일 이후인 17건(미국 6건, 한국 11건)이다. 날짜는 누리집이 적은 등록일이고, 모두 KAIST 부임(2026년 4월) 전에 등록된 특허다. 발명자와 번호는 누리집 표기 그대로다.[^patents] 교수 누리집은 교수가 가진 특허가 200건이 넘는다고 소개한다.[^bg]

- 2025-12-16 · Method and device for self-interference cancellation in wireless communication system (국가 미국; 번호 US-12501470-B2; 발명자 K Lee, Y Kim, H Lee, J Lee, S Choi)
- 2025-11-03 · 전자 장치 및 이의 제어 방법 (국가 한국; 번호 10-2882388; 발명자 임상순, 손위평, 최성현, 박우진, 반대현, 한성원)
- 2025-09-25 · 무선 통신 시스템에서 안테나 설정 방법 및 장치와 자기 간섭 제거 방법 및 장치 (국가 한국; 번호 10-2866572; 발명자 이권종, 김영준, 이효진, 이주호, 최성현)
- 2024-04-05 · 비면허 대역에서의 다중 채널을 이용한 통신 방법 및 장치 (국가 한국; 번호 10-2656607; 발명자 정병훈, 김지훈, 최성현, 윤강진, 이재홍)
- 2023-09-25 · 무선 통신 시스템에서 비면허대역의 채널을 점유하는 방법 및 장치 (국가 한국; 번호 10-2584500; 발명자 정병훈, 박승훈, 이재홍, 최성현, 김지훈, 윤강진)
- 2023-08-25 · 공간 재사용을 이용하여 데이터를 전송하는 무선 통신 장치 및 이를 이용한 데이터 통신 방법 (국가 한국; 번호 10-2572878; 발명자 한종훈, 손영욱, 최성현, 김성원, 이강현)
- 2023-08-21 · 무선 통신 시스템에서 코디네이션을 통한 와이파이 핸드오프를 위한 방법 및 장치 (국가 한국; 번호 10-2570561; 발명자 이민규, 최성현, 최준영, 이규진)
- 2022-12-20 · Method and apparatus for WiFi handoff via coordination in wireless communication system (국가 미국; 번호 US Patent 11,533,664; 발명자 M Lee, S Choi, J Choi, LEE Gyujin)
- 2022-10-18 · Base station group reconfiguration messaging based on terminal movement (국가 미국; 번호 US Patent 11,477,618; 발명자 J Byounghoon, LEE Kitaek, S Choi, P Seungil, H Yang, K Lee)
- 2022-09-14 · 무선 통신 시스템에서 복수의 캐리어들을 사용하기 위한 장치 및 방법 (국가 한국; 번호 10-2444738; 발명자 정병훈, 김지훈, 최성현, 박승훈, 정정수, 박태준, 윤강진, 이재홍, 황선욱)
- 2022-07-18 · 무선 통신 시스템에서 예약 신호를 송신하기 위한 장치 및 방법 (국가 한국; 번호 10-2423374; 발명자 정병훈, 이재홍, 최성현, 박승훈, 정정수, 김지훈, 윤강진)
- 2022-07-05 · Wireless communication devices for transmitting data using spatial reuse and data communication methods using the same (국가 미국; 번호 US Patent 11,381,366; 발명자 JH Han, YW Son, SH Choi, SW Kim, K Lee)
- 2022-06-27 · 무선 통신 시스템에서 버퍼 상태 정보 송수신 방법 및 장치 (국가 한국; 번호 KR-102413703-B1; 발명자 손영욱, 장상현, 정병훈, 김성원, 유승민, 이재홍, 최성현, 장수영)
- 2022-05-10 · Apparatus and method for using multiple carriers in wireless communication system (국가 미국; 번호 US-11330585-B2; 발명자 Byounghoon JUNG, Jihoon Kim, Sunghyun Choi, Seung-Hoon Park, Jungsoo JUNG, Taejun PARK, Kangjin YOON, Jaehong Yl, SunWook HWANG)
- 2022-01-19 · 다중 안테나 선택 기법 및 장치 (국가 한국; 번호 KR-102353333-B1; 발명자 김영집, 김성원, 김태준, 손영욱, 유승민, 이옥환, 이운균, 이재홍, 최성현)
- 2022-01-05 · 무선 통신 시스템에서 캐리어 감지 임계값 결정 방법 및 장치 (국가 한국; 번호 KR-102347428-B1; 발명자 김성원, 장상현, 정병훈, 손영욱, 유승민, 이재홍, 최성현, 장수영)
- 2021-12-21 · Method and apparatus for occupying channel of unlicensed band in wireless communication system (국가 미국; 번호 US-11206546-B2; 발명자 Byounghoon JUNG, Seunghoon PARK, Jaehong YI, Sunghyun Choi, Jihoon Kim, Kangjin YOON)

## 소식

누리집 News 페이지의 글 8건(2026년 4월–10월) 전부다. 제목 문구는 누리집 그대로다.[^news]

- 2026-10-02 · AINL will run the KAIST site of a national AI-RAN campus testbed program.
- 2026-09-18 · Invited talk at the KICS Workshop on AI-Native Networks and Communications for 6G.
- 2026-08-31 · Kyuhee Bak and Duc Cuong Nguyen join AINL as M.S. students.
- 2026-08-31 · EE49904 AI-Native Networking is offered for the first time this fall.
- 2026-06-19 · Invited talk at the KIPS AI Systems Research Group (AIS) Workshop.
- 2026-06-04 · DGIST Distinguished Lecture Series.
- 2026-06-02 · Seminar at Dongguk University on next-generation communication networks.
- 2026-04-13 · AINL opened at the KAIST School of Electrical Engineering.

## 연락과 위치

- 연구실: 김병호·김삼열 IT융합빌딩(N1) 617호(누리집 표기 Room 617)[^contact]
- 교수 연구실: IT융합빌딩(N1) 616호[^ee][^notice]
- 전화: 042-350-7486[^contact]
- 교수 이메일: sungh.choi@kaist.ac.kr[^contact][^ee]
[^home]: AINL 누리집 첫 화면 <https://ainl.kaist.ac.kr/> (소개문, 네 연구 영역, 소식, 2026-10-22 열람)
[^research]: AINL 누리집 Research 페이지 <https://ainl.kaist.ac.kr/research/> (네 연구 영역과 낱말, 테스트베드, 지금 하는 일, 연구 철학, 2026-10-22 열람)
[^people]: AINL 누리집 People 페이지 <https://ainl.kaist.ac.kr/people/> (교수 소개, 구성원, 2026-10-22 열람)
[^alumni]: AINL 누리집 Alumni 페이지 <https://ainl.kaist.ac.kr/alumni/> (서울대 MWNL 졸업생과 이전 구성원, 2026-10-22 열람)
[^pubs]: AINL 누리집 Publications 페이지 <https://ainl.kaist.ac.kr/publications/> (1995–2023년 논문 289편, 2026-10-22 열람)
[^news]: AINL 누리집 News 페이지 <https://ainl.kaist.ac.kr/news/> (2026년 글 8건, 2026-10-22 열람)
[^contact]: AINL 누리집 Contact 페이지 <https://ainl.kaist.ac.kr/contact/> (주소, 전화, 이메일, 2026-10-22 열람)
[^phome]: 최성현 교수 개인 누리집 첫 화면 <https://sites.google.com/view/sunghyun-chois-home/home> (직위, 2026-10-22 열람)
[^bg]: 최성현 교수 개인 누리집 Background 페이지 <https://sites.google.com/view/sunghyun-chois-home/background> (약력, 경력, 학력, 2026-10-22 열람)
[^recog]: 최성현 교수 개인 누리집 Recognition 페이지 <https://sites.google.com/view/sunghyun-chois-home/recognition> (수상과 영예, 2026-10-22 열람)
[^talks]: 최성현 교수 개인 누리집 Talks 페이지 <https://sites.google.com/view/sunghyun-chois-home/activities/talks> (초청 강연, 2026-10-22 열람)
[^board]: 최성현 교수 개인 누리집 Membership and Board 페이지 <https://sites.google.com/view/sunghyun-chois-home/activities/membership-and-board> (학회 회원, 위원회, 2026-10-22 열람)
[^editor]: 최성현 교수 개인 누리집 Editorship 페이지 <https://sites.google.com/view/sunghyun-chois-home/activities/editorship> (학술지 편집, 2026-10-22 열람)
[^std]: 최성현 교수 개인 누리집 Standard Contributions 페이지 <https://sites.google.com/view/sunghyun-chois-home/publications/standard-contributions> (IEEE 802.11·Zigbee 표준 기고문, 2026-10-22 열람)
[^samsung]: 최성현 교수 개인 누리집 Samsung Archive 페이지 <https://sites.google.com/view/sunghyun-chois-home/samsung-archive> (삼성전자 시기 활동, 2026-10-22 열람)
[^patents]: 최성현 교수 개인 누리집 Patents 페이지 <https://sites.google.com/view/sunghyun-chois-home/publications/patents> (미국·유럽·일본·중국·한국 특허, 2026-10-22 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(최성현) <https://ee.kaist.ac.kr/professor/%EC%B5%9C%EC%84%B1%ED%98%84/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 디비전, 학위, 대표업적, 2026-10-22 열람)
[^notice]: KAIST 전기및전자공학부 공지 「신임 교원 최성현 교수님 부임 안내」(2026-04-13) <https://ee.kaist.ac.kr/notices/%ec%8b%a0%ec%9e%84-%ea%b5%90%ec%9b%90-%ec%b5%9c%ec%84%b1%ed%98%84-%ea%b5%90%ec%88%98%eb%8b%98-%eb%b6%80%ec%9e%84-%ec%95%88%eb%82%b4/> (부임일, 연구 분야와 계획, 학력, 경력, 2026-10-22 열람)

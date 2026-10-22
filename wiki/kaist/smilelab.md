# SMILE Lab (Smart and Mobile Systems Lab)

**KAIST 전기및전자공학부 · 김성민 교수**

- 분야: 밀리미터파 백스캐터 통신과 초정밀 위치 추적, 차세대 이동통신을 위한 저전력 재구성 메타표면과 기지국 스케줄링, 배터리 없는 AI 사물인터넷, 서로 다른 무선 기술 사이의 직접 통신
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 무선·이동통신[^eeprof][^p5][^p6], 에너지 하베스팅[^old][^p7], 컴퓨터 비전[^bf][^p7]
- 홈페이지: <https://sites.google.com/view/smilelab/>
- 근거와 출처: [SMILE Lab 근거 페이지](smilelab-sources.md)

> 모바일 시스템과 배터리 없는 기기의 하드웨어와 소프트웨어를 함께 설계해, 대규모 통신, 초정밀 센싱, 지능형 상호작용을 이루려는 연구실이다.[^pi]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 김성민 교수가 이끄는 SMILE(Smart and Mobile Systems) Lab이다.[^eeprof][^pi] 전기및전자공학부 교수 소개는 교수의 주요 연구를 무선 네트워크, 모바일 컴퓨팅, 사물인터넷으로 적고,[^eeprof] 누리집 첫 화면은 연구실의 분야를 무선 네트워크(Wireless Networks), 사물인터넷(Internet of Things), 모바일 컴퓨팅(Mobile Computing)으로 적는다. 첫 화면의 학생 모집 글은 함께할 분야로 무선 네트워크·통신, RF(무선 주파수 신호)·레이더 시스템, 임베디드 시스템(기기 안에 넣어 정해진 일을 하는 컴퓨터 시스템)과 집적회로 설계를 든다.[^home]

교수 개인 누리집은 연구실이 모바일 시스템과 배터리 없는 기기의 하드웨어와 소프트웨어를 함께 설계해 대규모 통신(massive communication), 초정밀 센싱, 지능형 상호작용을 이루는 데 집중한다고 적는다. 교수가 MobiCom 2015 논문부터 서로 다른 무선 기술 사이의 직접 통신(CTC, Cross-technology Communication)이라는 새 분야를 키워 왔다고도 적는다.[^pi]

연구 페이지는 연구를 네 갈래로 나눈다. 밀리미터파 백스캐터(mmWave Backscatter), 차세대 이동통신 네트워킹(Next Generation Mobile Networking), 배터리 없는 AI 사물인터넷(Battery-free AI of Things), 서로 다른 무선 기술 사이의 통신(Cross-technology Communication)이다.[^research] 백스캐터(backscatter)는 기기가 스스로 전파를 만들지 않고, 받은 전파를 되반사하면서 그 반사를 바꿔 데이터를 싣는 통신 방식이다. 밀리미터파(mmWave)는 파장이 밀리미터 단위로 짧은 높은 주파수 대역의 전파다. 첫 화면에서 이어지는 연구 소개 페이지는 배터리 없는 사물인터넷을 태양전지·전파·진동 같은 전력 수확 장치로 움직이는 초저전력 사물인터넷으로, 사물인터넷의 AI(Artificial Intelligence of Things)를 저전력·저비용 사물인터넷 기기에서 학습과 추론을 하는 일로 설명한다.[^old]

최근 연구는 세 갈래로 모인다. 첫째, **밀리미터파 백스캐터 위치 추적과 통신**이다. 상용 FMCW 레이더(주파수를 시간에 따라 바꾸며 쏘는 레이더)로 백 미터가 넘는 거리에서 수백 개 태그의 3차원 위치를 센티미터 이하 정확도로 동시에 찾는 Hawkeye,[^p2] 벽 같은 장애물에 가려 직접 보이지 않는 곳의 태그 위치를 반사파로 찾는 SuperSight,[^p1] 수신 감도가 -115dBm인 백스캐터로 태그 1100개의 동시 통신을 보인 OmniScatter,[^p3] 상용 밀리미터파 WiFi 기기로 백스캐터 태그와 빠르게 통신하는 mmComb[^p4]가 있다. 둘째, **차세대 이동통신 네트워킹**이다. 5G 이동통신 표준(NR)을 따르며 실시간으로 재구성되고 AA 건전지 하나로 2.1년 동작하는 메타표면 NR-Surface를 만들었고,[^p5] 이동통신 기지국이 데이터 흐름의 완료 시간을 함께 고려해 전송 순서를 정하는 스케줄러 OutRAN을 다른 연구실과 함께 내놓았다.[^p6] 셋째, **배터리 없는 AI 사물인터넷**이다. 6×10 화소의 초저해상도 근적외선 영상 센서와 배터리 없는 RFID(전파로 태그를 읽고 쓰는 무선 인식 기술) 태그로, 촬영 단계부터 익명화된 영상만으로 사람의 행동을 알아보는 Mosaic을 만들었다.[^p7] 최근 논문 목록에는 벽 너머 센티미터 이하 위치 추적을 소개한 ACM GetMobile 초청 글(2025)과 밀리미터파 백스캐터 위치 추적 포스터(MobiSys 2023)도 있다.[^pubs]

## 주요 연구 주제

### 1. 밀리미터파 백스캐터 위치 추적과 통신

연구 페이지는 이 갈래의 목표를 넓은 영역에서 아주 많은 물체의 위치를 정확히 아는 것으로 적고, 대량 동시 추적(Massive-scale), 초정밀(Super Precision), 넓은 범위(Wide Coverage)를 내건다. 연구실이 만든 백스캐터 태그는 8.4마이크로와트를 써서 전지 하나로 40년 넘게 쓸 수 있고, 태그의 반 아타(Van Atta) 배열(들어온 전파를 온 방향으로 되돌려 보내도록 안테나를 짝지어 이은 배열)이 3차원 위치를 주고 다중 경로(전파가 벽 등에 반사돼 여러 길로 도착하는 현상)를 억누른다고 적는다.[^mmw] 연구실은 Hawkeye 태그 설계 파일과 위치 계산 알고리즘을 도구로 공개했다.[^mmw] 대표 논문 1–4.[^p1][^p2][^p3][^p4]

### 2. 차세대 이동통신 네트워킹

메타표면(작은 인공 구조를 판 위에 늘어놓아 전파를 반사하는 방향 등을 바꾸는 표면)은 밀리미터파 통신이 닿는 범위를 넓히는 경제적 방법이지만, 이동통신 표준에 맞춘 실시간 재구성과 여러 해 가는 배터리 수명을 함께 이루기 어렵다. 연구 페이지는 이를 이룬 지능형 메타표면을 소개한다.[^ng] 교수 개인 누리집은 이 갈래를 재구성 메타표면을 포함한 믿을 만한 차세대 이동통신 시스템을 만드는 일로 적는다.[^pi] 대표 논문 5, 6.[^p5][^p6]

### 3. 배터리 없는 AI 사물인터넷

개인 공간의 영상 모니터링은 데이터 유출 걱정 때문에 널리 쓰이지 못한다. 연구 페이지는 촬영 단계부터 데이터를 익명으로 만들고 배터리 없이 동작해 사각지대 없이 계속 지켜보는 영상 기반 행동 인식 시스템과, 그 태그를 위한 행동 인식 신경망을 소개한다.[^bf] 대표 논문 7.[^p7]

### 4. 서로 다른 무선 기술 사이의 통신

WiFi, 블루투스 저전력(BLE), ZigBee처럼 신호 방식이 서로 맞지 않는 무선 기기들이 상용 기기 그대로 직접 통신하게 하는 연구다. 이렇게 이어진 기기들은 주파수를 효율적으로 함께 쓰고, 기술이 다른 기기들 사이에서 MIMO(여러 안테나로 여러 데이터를 동시에 주고받는 기술)를 이룰 수 있다. 연구 페이지는 WiFi가 WiFi가 아닌 신호를 엿들어 숨겨진 카메라와 불법 드론을 찾아내는 쓰임도 든다.[^ctc] 연구실은 서로 다른 기술 사이의 채널을 추정하는 도구를 공개했다.[^ctc] 연구 페이지가 이 갈래로 든 논문은 2015–2020년 논문이다.[^ctc]

## 대표 논문

랩 Publications 페이지의 2021–2026년 논문 가운데 김성민 교수가 저자인 학회·학술지 논문을 세 연구 갈래에 고르게 담도록 일곱 편을 골랐다. 4번과 6번은 다른 연구실 교수가 마지막 저자인 공동 연구다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2024 | [SuperSight: Sub-cm NLOS Localization for mmWave Backscatter](https://doi.org/10.1145/3643832.3661857) · MobiSys 2024 | 실내 위치 추적은 콘크리트 벽, 금속 선반, 칸막이, 전자 제품 같은 물체가 전파를 쉽게 가려 사각지대가 생긴다. SuperSight는 가려져 직접 보이지 않는(NLOS) 곳의 밀리미터파 백스캐터 태그 위치를, 주변 다중 경로 환경을 미리 조사하거나 바꾸지 않고 찾는 방법이다. 밀리미터파가 한 방향으로 곧게 나가고 거울처럼 반사되는 성질을 삼각형 태그 배열과 함께 써서, 8m 거리에서 센티미터 이하 정확도로 위치를 찾았고, 경쟁 방법보다 약 10배의 성능 개선이라고 적는다. 원편파(전기장이 원을 그리며 도는 전파) 77GHz 역반사 태그가 여러 반사면과 태그 방향에서 정밀도를 지킨다. 금속·콘크리트·석고를 포함한 반사면 재료 여섯 가지에서 시험했고, 복도와 사무실에서 8m 거리 금속 반사면 기준 x·y·z 위치 정확도가 최대 5.7mm·5.5mm·7.7mm, 요·피치·롤 각도 정확도가 0.22·0.28·0.1도였다.[^p1] | 공동 1저자 K. M. Bae·H. Moon(랩 표시), 마지막 저자 김성민 |
| 2 | 2023 | [Hawkeye: Hectometer-range Subcentimeter Localization for Large-scale mmWave Backscatter](https://doi.org/10.1145/3581791.3596869) · MobiSys 2023 | 넓은 영역에서 많은 물체의 위치를 정확히 아는 것이 사물인터넷과의 상호작용에서 핵심이다. Hawkeye는 새 밀리미터파 백스캐터로, (i) 수백 개 규모의 동시 3차원 위치 추적을 (ii) 센티미터 이하 정확도로 (iii) 백 미터가 넘는 거리에서 처음 해냈다고 적는다. 실내와 실외, 움직이는 상황에 모두 쓸 수 있다. 태그는 가로와 세로 두 방향 모두 들어온 쪽으로 되반사하는 반 아타 배열로 3차원 위치를 주고 다중 경로를 억누른다. 위치 계산은 상용 FMCW 레이더와 호환되는 가벼운 신호 처리이고, 태그 신호와 주변 잡반사(클러터) 사이의 관계와 스펙트럼 누설을 이용해 위치를 세밀하게 정한다. 복도·강의실·축구장 시험에서 160m 거리에서 중앙값 7mm 정확도를 냈고, 태그 100개를 33.2ms 만에 동시에 찾았다. 온도가 바뀌어 발진기 주파수가 크게 어긋나도 안정적이었다.[^p2] | 공동 1저자 K. M. Bae·H. Moon(랩 표시), 마지막 저자 김성민 |
| 3 | 2022 | [OmniScatter: Extreme Sensitivity mmWave Backscattering Using Commodity FMCW Radar](https://doi.org/10.1145/3498361.3538924) · MobiSys 2022 | 사물인터넷이 성공하려면 아주 많은 기기를 연결해야 한다. 밀리미터파 백스캐터는 잠재력이 크지만 신호가 크게 약해지고 주변 반사가 압도적이라는 어려움이 있다. OmniScatter는 수신 감도 -115dBm의 실용적인 밀리미터파 백스캐터로, 이 성능이 이론적으로 널리 쓰이는 상용 RFID EPC Gen2(900MHz)와 견줄 만하다고 적는다. 6m 떨어진 나무 옷장 안에 태그를 둔 사무실, 금속 선반 두 줄 너머에 태그를 둔 도서관과 매장처럼 주변 반사와 가림이 많은 환경에서 확인했다. 핵심인 새 HD-FMCW는 태그의 FSK 신호(주파수를 바꿔 0과 1을 나타내는 신호)와 맞물려 주파수 영역에서 주변 반사와 태그 신호를 떼어 낸다. 서로 조율할 필요 없이 주파수를 나눠 쓰는 FDMA로 동시 태그를 수천 개까지 늘릴 수 있다. 리더는 상용 레이더로, 태그는 PCB로 만들었고, 기록 기반 평가에서 태그 1100개가 비트 오류율 1.5% 미만으로 동시에 통신했다.[^p3] | 1저자 K. M. Bae, 마지막 저자 김성민 |
| 4 | 2024 | [mmComb: High-speed mmWave Commodity WiFi Backscatter](https://www.usenix.org/conference/nsdi24/presentation/chae) · NSDI 2024 | 고속 연결은 여러 새 사물인터넷 응용을 여는 열쇠이고, 밀리미터파 백스캐터는 빠르고 전력을 적게 쓰는 사물인터넷 망의 해법이 될 수 있다. 그러나 지금의 밀리미터파 백스캐터 시스템은 전용 리더 기기가 필요해 비싸다. mmComb는 상용 밀리미터파 WiFi에서 동작하는 백스캐터 시스템으로, 태그를 802.11ad/ay 밀리미터파 WiFi 망에 바로 넣는 것을 목표로 한다. 첫째, 프로토콜을 고치지 않고 WiFi 기기가 이미 쓰는 빔포밍(전파를 원하는 방향으로 모아 보내는 기술) 프레임으로 태그와 통신하는 기법을, 둘째, 수신 빔포밍으로 실내 다중 경로 환경에서도 약한 백스캐터 신호를 뽑아내는 자기 간섭 억제 방법을 내놓았다. 태그 시제품과 60GHz 상용 WiFi 기기로 구현해, 802.11ad/ay 제어 프레임만으로 최대 55Mbps 전송률을 내면서 87.3μW를 썼고, 5.5m 거리까지 비트 오류율이 10⁻³보다 낮았다.[^p4] | 1저자 Y. Chae, 김성민은 5명 중 4번째, 마지막 저자 P. Pathak |
| 5 | 2024 | [NR-Surface: NextG-ready µW-reconfigurable mmWave Metasurface](https://www.usenix.org/conference/nsdi24/presentation/kim) · NSDI 2024 | 메타표면은 밀리미터파 통신 범위를 넓히는 경제적 해법으로 떠올랐지만, 260ns의 엄격한 NR 동기 조건과 실시간 무선 재구성을 맞추면서 여러 해 배터리 수명을 지키기 어려워 널리 쓰이지 못하고 있다. NR-Surface는 NR 표준을 완전히 따르는 첫 실시간 재구성 메타표면이라고 적으며, 242.7μW로 동작해 AA 건전지 하나로 2.1년을 쓴다. 동기와 실시간 재구성을 위한 초저전력(14kHz 표본화) 재구성 인터페이스 NBPU와, 짧게 켜고 길게 쉬는 저듀티 동작에 맞춘 반응이 빠르고 누설이 적은 메타표면을 갖췄고, NR 표준의 빔 관리 절차의 구조와 주기성을 이용했다. srsRAN으로 만든 NR 기지국과 함께 처음부터 끝까지 시험해, 기지국 하나에 여러 NR-Surface, NR-Surface 하나에 여러 단말, 3차원 빔포밍을 보였다. 모퉁이 너머 단말 평가에서 사용자 이동 패턴에 따라 20.3dB, 동적인 가림 상황에서 22.2dB의 이득을 냈다.[^p5] | 공동 1저자 M. Kim·N. Ahn(랩 표시), 마지막 저자 김성민 |
| 6 | 2022 | [OutRAN: Co-optimizing for Flow Completion Time in Radio Access Network](https://doi.org/10.1145/3555050.3569122) · CoNEXT 2022 | 짧은 지연을 요구하는 대화형 응용의 트래픽이 이동통신망의 대부분을 차지하게 됐다. 그런데 기지국의 기존 스케줄러는 서비스 품질(QoS) 정보가 따로 없으면 서비스를 가리지 않고 무선 자원 활용이나 사용자 사이 공평성만 높이려 해 짧은 지연을 내지 못한다. 기지국의 하향 전송 순서를 정할 때 데이터 흐름이 끝나는 데 걸리는 시간(FCT)을 함께 고려하면 지연에 민감한 흐름의 지연을 줄일 수 있다는 새 기회를 찾았다. 다만 기존 스케줄러의 최적화 지표를 크게 해칠 수 있고, 트래픽을 미리 알지 못한 채 동작해야 한다는 어려움이 있다. OutRAN은 FCT와 셀룰러 스케줄러의 기존 최적화 목표를 함께 최적화하는 무선 접속망용 흐름 스케줄러로, 사전 정보가 필요 없다. 시뮬레이션과 실제 무선 시험에서 기존 LTE/5G 스케줄러보다 FCT가 좋아 Android 휴대폰의 웹페이지 로딩 시간이 줄었다.[^p6] | 1저자 J. Kim, 김성민은 6명 중 5번째, 마지막 저자 D. Han |
| 7 | 2026 | [Extremely Low-resolution RFID Vision for Real-time and Visually-anonymized Action Recognition](https://doi.org/10.1145/3715697) · ACM Transactions on Sensor Networks | 건강 관리 같은 영상 기반 개인 모니터링은 쓸모가 있지만, 침실 같은 개인 공간에서는 사생활 데이터 유출 걱정 때문에 널리 쓰이지 못한다. 기존 익명화 방법은 고화질 영상을 기기에 저장했다가 클라우드에 올리기 전에 후처리로 익명화하는데, 최근의 사물인터넷 카메라 해킹과 기기 안 데이터 유출은 촬영 단계부터 익명화된 데이터를 요구한다. Mosaic은 촬영 단계부터 데이터를 익명으로 만들고 배터리 없이 동작해 사각지대 없이 계속 지켜보는, 처음부터 끝까지 이어진 영상 기반 행동 인식 시스템이다. 6×10 화소의 초저해상도 근적외선 영상 센서로 영상을 익명으로 만들고, 태양전지 네 개를 단 RFID 호환 완전 수동형 태그(배터리 없이 받은 전파와 주변 에너지로 동작하는 태그)로 조도가 30럭스까지 낮은 곳(예: 직사광이 닿지 않는 선반 깊숙한 곳)에서도 초저해상도 영상을 실시간으로 보낸다. 실시간 추론을 위한 가벼운 행동 인식 신경망(Intel Core i7-8700에서 18.4ms)을 함께 만들었고, 10가지 행동에서 평균 98% 정확도를 냈다. 눈에 보이지 않는 근적외선을 써서 어두운 곳에서도 잠을 방해하지 않고 동작하며, 20m 거리의 산불 감지도 시연했다.[^p7] | 공동 1저자 H. Shin·S. Shim(랩 표시), 마지막 저자 김성민 |

## 교수와 전문 분야

김성민(Song Min Kim) 교수는 University of Minnesota에서 컴퓨터과학 박사 학위(2016)를, 고려대학교에서 전기공학 학사(2007)와 석사(2009) 학위를 받았다.[^pi][^eeprof] 2016년 8월부터 2019년 1월까지 George Mason University 컴퓨터과학과 조교수였고, 2019년 2월 KAIST 전기및전자공학부에 부임해 조교수를 거쳐 부교수가 됐다.[^pi] 교수 개인 누리집과 Members 페이지는 직위를 정년 보장 부교수(Associate Professor, tenured)로 적고,[^pi][^members] 전기및전자공학부 교수 소개는 직위를 부교수, 소속 디비전을 Computer와 Communication division으로 적는다.[^eeprof]

전기및전자공학부 교수 소개는 주요 연구분야를 AI & Machine Learning, Multimedia Signal Processing, Information, Communication & Coding, Software Systems & Networking, Human Computer Interaction, RF/mmWave Devices & Systems로 적는다.[^eeprof] 교수 개인 누리집은 교수가 ACM/IEEE Transactions on Networking(2022년부터), ACM Transactions on Sensor Networks(2023년부터), ACM Transactions on Internet of Things(2024년부터)의 부편집장을 맡고 있고, IEEE ICNP 2025 공동 대회장(General Co-chair), ACM MobiCom 2024 등록 공동 위원장, IEEE MASS 2024 워크숍 공동 위원장을 맡았으며, ACM MobiCom(2021–2027, 2023년 제외), ACM SenSys 2024, IEEE INFOCOM(2019–2027), USENIX NSDI 2023의 프로그램 위원을 맡았다고 적는다.[^pi]

교수 개인 누리집의 수상 목록에는 KAIST LINKGNESIS Best Teacher Award(2026), ACM MobiSys Best Paper Award(2024, 2022), SIGMOBILE Research Highlight(2023), 전기및전자공학부 Teaching Award(EE414 Embedded Systems, 2022), KAIST International Cooperation Award(2022)가 있다. KAIST 부임 전의 IEEE ICDCS Best Paper Award(2018)와 University of Minnesota Doctoral Dissertation Fellowship(2016)도 적혀 있다.[^pi] 랩 목록에 따르면 MobiSys 2024 Best Paper Award는 대표 논문 1, MobiSys 2022 Best Paper Award와 SIGMOBILE Research Highlight는 대표 논문 3이 받았고, 대표 논문 2는 MobiSys 2023 Best Paper Finalist, 대표 논문 6은 CoNEXT 2022 Best Paper Finalist에 올랐다. 대표 논문 7의 학회판인 Mosaic(IPSN 2023)은 Institute of Embedded Engineering of Korea의 Outstanding Paper Award를 받았다.[^pubs]

전기및전자공학부 교수 소개의 대표업적에는 "Achieving Receiver-Side Cross-Technology Communication with Cross-Decoding"(MobiCom 2018), "Symbol-level Cross-technology Communication via Payload Encoding"(ICDCS 2018, Best Paper), "FreeBee: Cross-technology Communication via Free Side-channel"(MobiCom 2015), "cETX: Incorporating Spatiotemporal Correlation for Better Wireless Networking"(SenSys 2015)이 올라 있다.[^eeprof] 이 논문들은 교수의 KAIST 부임 전 논문이다.[^pi] 교수 개인 누리집은 그 밖의 연구 주제(More Topics)로 서로 다른 무선 기술 사이의 통신(2015–2020년 논문)과 저전력 무선 기기의 공존(Low-power Wireless Coexistence, 2013–2020년 논문)을 든다.[^pi] 논문으로 보면 지금의 전문 분야는 세 갈래다. 첫째, 밀리미터파 백스캐터의 위치 추적과 통신이다(대표 논문 1–4).[^p1][^p2][^p3][^p4] 둘째, 차세대 이동통신의 메타표면과 기지국 스케줄링이다(대표 논문 5, 6).[^p5][^p6] 셋째, 배터리 없는 영상 센싱과 행동 인식이다(대표 논문 7).[^p7] 교수 개인 누리집에 따르면 교수는 KAIST에서 Mobile Computing and Systems for Intelligent Living(EE595), 임베디드 시스템(EE414), 컴퓨터 네트워크(EE323), 전기공학을 위한 프로그래밍 구조(EE209)를 가르쳤다.[^pi]

## 응용 분야

대표 논문이 겨누는 응용은 아주 많은 사물인터넷 기기의 연결과 위치 추적,[^p2][^p3] 몰입형 상호작용 서비스를 위한 실내 위치 추적,[^p1] 전용 리더 없이 상용 WiFi 망에 넣는 고속 저전력 사물인터넷,[^p4] 밀리미터파 이동통신이 닿는 범위의 확장,[^p5] 이동통신 기지국의 지연 감소(휴대폰 웹페이지 로딩),[^p6] 침실 같은 개인 공간의 사생활을 지키는 행동 모니터링과 산불 감지다.[^p7] 연구 페이지는 서로 다른 무선 기술 사이의 통신을 숨겨진 카메라와 불법 드론 탐지에도 쓸 수 있다고 적는다.[^ctc] Members 페이지에 따르면 박사 졸업생 Kang Min Bae는 MilliTrack(스타트업)의 Chief Technology Officer이고, 석사 졸업생 Geonung Lee의 진로도 MilliTrack(startup)으로 적혀 있다. 박사 졸업생 Jinhwan Jung은 Asleep(스타트업)의 Chief Research Officer, Yoon Chae는 University of Texas at Arlington 컴퓨터과학과 조교수이고, 석사 졸업생의 진로에는 LIG Defense&Aerospace와 Samsung Research가 있다.[^members]

## 구성원

2026년 10월 23일 랩 Members 페이지 기준이다. Graduate Student Researchers 칸 11명과 Undergraduate Interns 칸 7명이다. 과정과 시작 시점은 각 구성원 칸의 표기("PhD Program@KAIST (Mar 2022 -)" 등)를 옮겼고, "PhD + MS Joint Program"은 석박사통합과정으로 적었다. 연구 주제는 연구 페이지의 각 갈래 아래 구성원 명단에 이름이 오른 갈래다. 학부 인턴의 괄호는 누리집이 적은 학과다.[^members][^research] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다. 학부 인턴 Minseok Kim(KAIST CS)은 Members 페이지에 박사과정 Minseok Kim과 따로 적혀 있어 표시하지 않았다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Geonha Park (박건하) | 박사과정 | Sep. 2020 | mmWave Backscatter |  |
| Namjo Ahn (안남조) | 석박사통합과정 | Mar 2021 | Next Generation Mobile Networking, Battery-free AI of Things | 3, 5 |
| Hyeonho Shin (신현호) | 박사과정 | Mar 2022 | Battery-free AI of Things | 7 |
| Seokwon Yang (양석원) | 박사과정 | Mar 2025 | Next Generation Mobile Networking |  |
| Hankyeol Moon (문한결) | 석박사통합과정 | Mar 2022 | mmWave Backscatter | 1, 2 |
| Seungwoo Shim (심승우) | 석박사통합과정 | Mar 2022 | Battery-free AI of Things | 7 |
| Minseok Kim (김민석) | 박사과정 | Mar 2023 | Next Generation Mobile Networking | 5 |
| Haksun Son (손학선) | 석박사통합과정 | Mar 2023 | mmWave Backscatter |  |
| Hyunhee Cho (조현희) | 석사과정 | Mar 2025 |  |  |
| Minjae Kim (김민재) | 석사과정 | Mar 2026 |  |  |
| Anel Murat | 석사과정 | Sep 2026 |  |  |
| Minji Cho | 학부 인턴 (KAIST EE) |  |  |  |
| Minseok Kim | 학부 인턴 (KAIST CS) |  |  |  |
| Yongin Shin | 학부 인턴 (KAIST EE) |  |  |  |
| Junyong Kim | 학부 인턴 (KAIST BCS) |  |  |  |
| Bokyeong Kim | 학부 인턴 (KAIST EE) |  |  |  |
| Dohoon Lee | 학부 인턴 (KAIST EE) |  |  |  |
| Kibeom Kim | 학부 인턴 (KAIST EE) |  |  |  |

## 졸업생과 학부 연구생

랩 Members 페이지 Alumni 칸의 대학원 졸업생 10명(박사 3, 석사 7)과 학부생 46줄(KAIST 41줄, 다른 학교 5명)이다. 졸업 연도와 진로는 랩이 적은 것이고, 박사 졸업생 한 명은 학위 학교를 George Mason University로 적는다. 석사 졸업생 세 명은 진로가 이 연구실의 박사과정으로 적혀 있어 위 구성원 표에도 있다. 학부생 칸은 이름만 적고 기간을 적지 않으며, KAIST 칸에는 Hankyul Moon이 두 번 적혀 있다. 학부생 두 명의 이름 뒤 괄호에는 URP Excellence Award가 적혀 있다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 랩이 적은 수상 |
|---|---|---|---|
| Jongeun Park (박종은) | MS (2026) |  |  |
| Geonung Lee (이건웅) | MS (2026) | MilliTrack (startup) |  |
| Seokwon Yang (양석원) | MS (2025) | PhD program@Smile Lab |  |
| Junbeom Park (박준범) | MS (2025) | LIG Defense&Aerospace |  |
| Kang Min Bae (배강민) | Ph.D. (2024) | Chief Technology Officer@MilliTrack (startup) |  |
| Yoon Chae (채윤) | Ph.D. (George Mason University) (2024) | Assistant Professor@University of Texas at Arlington, Computer Science |  |
| Minseok Kim (김민석) | MS (2023) | PhD program@Smile Lab |  |
| Hyeonho Shin (신현호) | MS (2022) | PhD program@Smile Lab |  |
| Woojae Jeong (정우재) | MS (2021) | Samsung Research |  |
| Jinhwan Jung (정진환) | Ph.D. (2020) | Chief Research Officer@Asleep (startup) |  |
| Hakson Son | Undergraduate Students (KAIST) |  | URP Excellence Award |
| Seokwon Yang | Undergraduate Students (KAIST) |  | URP Excellence Award |
| Ananya Besufekad | Undergraduate Students (KAIST) |  |  |
| Jongeun Park | Undergraduate Students (KAIST) |  |  |
| Youngchan Kim | Undergraduate Students (KAIST) |  |  |
| Akotet Y. Tesema | Undergraduate Students (KAIST) |  |  |
| Kyutae Lee | Undergraduate Students (KAIST) |  |  |
| Jaemin Myung | Undergraduate Students (KAIST) |  |  |
| Geumseo Yeom | Undergraduate Students (KAIST) |  |  |
| Myunggeun Cho | Undergraduate Students (KAIST) |  |  |
| Zhamaliddin Kalzhan | Undergraduate Students (KAIST) |  |  |
| Jihyeon Park | Undergraduate Students (KAIST) |  |  |
| Seonkyu Kim | Undergraduate Students (KAIST) |  |  |
| Handong Lee | Undergraduate Students (KAIST) |  |  |
| Jaechan So | Undergraduate Students (KAIST) |  |  |
| Yukyeum Kim | Undergraduate Students (KAIST) |  |  |
| Hankyul Moon | Undergraduate Students (KAIST) |  |  |
| Seungwoo Shim | Undergraduate Students (KAIST) |  |  |
| Nahyeon Park | Undergraduate Students (KAIST) |  |  |
| Jaewon Jung | Undergraduate Students (KAIST) |  |  |
| Jaehyun Kim | Undergraduate Students (KAIST) |  |  |
| Shyngys Aitkazinov | Undergraduate Students (KAIST) |  |  |
| Jeongwon Lee | Undergraduate Students (KAIST) |  |  |
| Hyeann Lee | Undergraduate Students (KAIST) |  |  |
| Kangmin Bae | Undergraduate Students (KAIST) |  |  |
| Hankyul Moon | Undergraduate Students (KAIST) |  |  |
| Hojin Yu | Undergraduate Students (KAIST) |  |  |
| Chanhyun Park | Undergraduate Students (KAIST) |  |  |
| Sojeong Song | Undergraduate Students (KAIST) |  |  |
| Hyeonghun Cha | Undergraduate Students (KAIST) |  |  |
| Hanna Kim | Undergraduate Students (KAIST) |  |  |
| Dongwon Kim | Undergraduate Students (KAIST) |  |  |
| Wonhyun Kim | Undergraduate Students (KAIST) |  |  |
| Daehwan Kwon | Undergraduate Students (KAIST) |  |  |
| Hyeongjin Cho | Undergraduate Students (KAIST) |  |  |
| Minjae Kim | Undergraduate Students (KAIST) |  |  |
| Vee Han Ling | Undergraduate Students (KAIST) |  |  |
| Minji Cho | Undergraduate Students (KAIST) |  |  |
| Chang Wan Kang | Undergraduate Students (KAIST) |  |  |
| Axmadjonov Ulugbek | Undergraduate Students (KAIST) |  |  |
| Gulomjonov Jasurbek | Undergraduate Students (KAIST) |  |  |
| Geonung Lee | Undergraduate Students (Korea Univ.) |  |  |
| Seunggi Lee | Undergraduate Students (DGIST) |  |  |
| Hyunhee Cho | Undergraduate Students (Sungkyunkwan Univ.) |  |  |
| Jaechang Shin | Undergraduate Students (Sungkyunkwan Univ.) |  |  |
| Chen Yimin | Undergraduate Students (Harbin Institute of Technology) |  |  |

## 최근 논문 목록 (2021–2026)

랩 Publications 페이지에서 대괄호 표기의 연도가 2021–2026년인 11편(2025년 2, 2024년 4, 2023년 3, 2022년 2)이다. 학회 논문 7편, 학회 포스터 1편, 학술지 ACM Transactions on Sensor Networks 논문 1편, 잡지 ACM GetMobile 초청 글 2편이며, 2021년 표기 항목은 없다. 제목·저자·학회와 학술지 표기는 랩 표기 그대로이고, 저자 이름 뒤 *는 랩이 밝힌 공동 기여 표시, 괄호 안의 수상·선정·Fast Track 표시는 랩이 논문 옆에 적은 것이다.[^pubs]

**2025**

- Kang Min Bae\*, Hankyeol Moon\*, Song Min Kim (\*: equal contribution). "Subcentimeter Localization from Behind the Wall". *[ACM GetMobile '25] ACM GetMobile: Mobile Computing and Communications 28 (4), 27-31, Jan. 2025, (Invited)*.
- Hyeonho Shin\*, Seungwoo Shim\*, Myeongkyun Cho, Youngki Lee, Jinwoo Shin, Song Min Kim (\*: equal contribution). "Extremely Low-resolution RFID Vision for Real-time and Visually-anonymized Action Recognition". *[ACM TOSN '25] ACM Transactions on Sensor Networks (Fast Track)*.

**2024**

- Kang Min Bae\*, Hankyeol Moon\*, Song Min Kim (\*: equal contribution). "SuperSight: Sub-cm NLOS Localization for mmWave Backscatter". *[ACM MobiSys '24] The 22nd ACM International Conference on Mobile Systems, Applications, and Services (Best Paper Award)*.
- Minseok Kim\*, Namjo Ahn\*, Song Min Kim (\*: equal contribution). "NR-Surface: NextG-ready µW-reconfigurable mmWave Metasurface". *[USENIX NSDI '24] USENIX Symposium on Networked Systems Design and Implementation*.
- Yoon Chae, Zhenzhe Lin, Kang Min Bae, Song Min Kim, Parth Pathak. "mmComb: High-speed mmWave Commodity WiFi Backscatter". *[USENIX NSDI '24] USENIX Symposium on Networked Systems Design and Implementation*.
- Kang Min Bae, Namjo Ahn, Yoon Chae, Parth Pathak, SungMin Sohn, Song Min Kim. "OmniScatter: Extreme Sensitivity mmWave Backscattering Using Commodity FMCW Radar". *[ACM GetMobile '24] ACM GetMobile: Mobile Computing and Communications 27 (4), 26-30, Jan. 2024, (Invited)*.

**2023**

- Kang Min Bae\*, Hankyeol Moon\*, Sung-Min Sohn, Shin, Song Min Kim (\*: equal contribution). "Hawkeye: Hectometer-range Subcentimeter Localization for Large-scale mmWave Backscatter". *[ACM MobiSys '23] The 21st ACM International Conference on Mobile Systems, Applications, and Services (Best Paper Finalist)*.
- Seungwoo Shim\*, Hyeonho Shin\*, Myeongkyun Cho, Youngki Lee, Jinwoo Shin, Song Min Kim (\*: equal contribution). "Mosaic: Extremely Low-resolution RFID Vision for Visually-anonymized Action Recognition". *[ACM/IEEE IPSN '23] The 22nd ACM/IEEE International Conference on Information Processing in Sensor Networks (Outstanding Paper Award by Institute of Embedded Engineering of Korea)*.
- Kang Min Bae, Hankyeol Moon, and Song Min Kim. "Poster: Submillimeter Localization for mmWave Backscatter Using Commodity 77 GHz Radar". *[ACM MobiSys '23 Poster] Proceedings of the 21th ACM International Conference on Mobile Systems, Applications, and Services*.

**2022**

- Kang Min Bae, Namjo Ahn, Yoon Chae, Parth Pathak, SungMin Sohn, Song Min Kim. "OmniScatter: Extreme Sensitivity mmWave Backscattering Using Commodity FMCW Radar". *[ACM MobiSys '22] The 20th ACM International Conference on Mobile Systems, Applications, and Services (Best Paper Award, SIGMOBILE Research Highlight)*.
- Jaehong Kim, Yunheon Lee, Hwijoon Lim, Youngmok Jung, Song Min Kim, Dongsu Han. "Co-optimizing for Flow Completion Time in Radio Access Network". *[ACM CoNEXT '22] The 18th International Conference on emerging Networking EXperiments and Technologies (Best Paper Finalist)*.

## 수상

교수 개인 누리집 Awards and Recognitions 목록의 2022–2026년 항목 6건이다. 목록은 연도만 적는다. 논문 수상과 선정 표시는 위 논문 목록의 괄호에 있다.[^pi]

- 2026 · LINKGNESIS Best Teacher Award, KAIST, 2026
- 2024 · Best Paper Award, ACM MobiSys 2024
- 2022 · Best Paper Award, ACM MobiSys 2022
- 2023 · SIGMOBILE Research Highlight, 2023
- 2022 · Teaching Award (EE414 Embedded Systems), School of EE, KAIST, 2022
- 2022 · International Cooperation Award, KAIST 2022

## 연락과 위치

- 연구실: KAIST IT융합빌딩(N1) 918호[^home]
- 교수 연구실: IT융합빌딩(N1) 913호, 연락처 7453[^eeprof][^pi]
- 교수 이메일: songmin@kaist.ac.kr[^eeprof][^pi]
[^p1]: K. M. Bae, H. Moon, S. M. Kim, Proceedings of the 22nd Annual International Conference on Mobile Systems, Applications and Services, 278-291 (온라인 2024-06-04). <https://doi.org/10.1145/3643832.3661857> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: K. M. Bae, H. Moon, S.-M. Sohn, S. M. Kim, Proceedings of the 21st Annual International Conference on Mobile Systems, Applications and Services, 303-316 (온라인 2023-06-18). <https://doi.org/10.1145/3581791.3596869> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: K. M. Bae 외, S. M. Kim, Proceedings of the 20th Annual International Conference on Mobile Systems, Applications and Services, 316-329 (온라인 2022-06-27). <https://doi.org/10.1145/3498361.3538924> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: Y. Chae 외, P. Pathak, 21st USENIX Symposium on Networked Systems Design and Implementation (NSDI '24) (2024). <https://www.usenix.org/conference/nsdi24/presentation/chae> 초록 기준(학회 논문집 페이지 게시 초록).
[^p5]: M. Kim, N. Ahn, S. M. Kim, 21st USENIX Symposium on Networked Systems Design and Implementation (NSDI '24) (2024). <https://www.usenix.org/conference/nsdi24/presentation/kim> 초록 기준(학회 논문집 페이지 게시 초록).
[^p6]: J. Kim 외, D. Han, Proceedings of the 18th International Conference on emerging Networking EXperiments and Technologies, 369-385 (온라인 2022-11-30). <https://doi.org/10.1145/3555050.3569122> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: H. Shin 외, S. M. Kim, ACM Transactions on Sensor Networks 22, 1-26 (온라인 2026-04-13). <https://doi.org/10.1145/3715697> 초록 기준.
[^home]: 연구실 누리집 첫 화면 <https://sites.google.com/view/smilelab/home> (연구 분야, 학생 모집 글, 연락처, 2026-10-23 열람)
[^research]: Research 페이지 <https://sites.google.com/view/smilelab/research> (네 연구 갈래 목록, 2026-10-23 열람)
[^mmw]: mmWave Backscatter 페이지 <https://sites.google.com/view/smilelab/research/mmwave-backscatter> (연구 소개, 공개 도구, 논문, 구성원, 2026-10-23 열람)
[^ng]: Next Generation Mobile Networking 페이지 <https://sites.google.com/view/smilelab/research/next-generation-mobile-networking> (연구 소개, 논문, 구성원, 2026-10-23 열람)
[^bf]: Battery-free AI of Things 페이지 <https://sites.google.com/view/smilelab/research/battery-free-ai-of-things> (연구 소개, 논문, 구성원, 2026-10-23 열람)
[^ctc]: Cross-technology Communication 페이지 <https://sites.google.com/view/smilelab/research/cross-technology-communication> (연구 소개, 공개 도구, 논문, 2026-10-23 열람)
[^old]: 연구 소개 페이지(첫 화면 연구 분야 아래 more 링크) <https://sites.google.com/view/smilelab/re_sea_rch_old_02> (Cross-technology Communication, Millimeter Wave 5G/6G Wireless Communication & Networking, Batteryless Internet of Things, Artificial Intelligence of Things 소개, 2026-10-23 열람)
[^members]: Members 페이지 <https://sites.google.com/view/smilelab/members> (Professor, Graduate Student Researchers, Undergraduate Interns, Alumni 칸, 2026-10-23 열람)
[^pubs]: Publications 페이지 <https://sites.google.com/view/smilelab/publications> (전체 논문 목록, 2026-10-23 열람)
[^pi]: 김성민 교수 개인 누리집 <https://sites.google.com/view/songminkim/> (소개, Latest Research, Academic Appointments/Education, Latest Services, Current Graduate Students, Awards and Recognitions, Teaching, 2026-10-23 열람)
[^eeprof]: KAIST 전기및전자공학부 교수 소개(김성민) <https://ee.kaist.ac.kr/professor/16205/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 디비전, 학위, 대표업적, 2026-10-23 열람)

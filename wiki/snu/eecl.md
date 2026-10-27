# 전기 에너지 변환 연구실 (Electric Energy Conversion Lab, EECL)

**서울대학교 공과대학 전기·정보공학부 · 하정익 교수**

- 분야: 전력전자, 전동기 제어(센서리스 구동, 개방 권선 전동기, 토크 리플 저감, 전동기 일체형 충전), 무선 전력 전송(유도·용량 결합), 고주파·공진형 전력 변환 회로(GaN·SiC 스위치, 이중 능동 브리지, 스위치드 커패시터 변환기), 계통 연계·비절연 변환기의 누설 전류 억제, 전력전자의 기계 학습(고장 진단, 이상 탐지, 데이터 기반 위치 추정)
- 대분야: 전기전자·반도체·광학, 에너지·환경·지구
- 태그: 무선 전력 전송[^home][^p3][^p4], 전기차[^ecelabv][^home][^p2], 고장 진단·수명 예측[^home][^p7], 제어 이론·제어 공학[^home][^p1], 전력전자 변환기·전력 변환 시스템[^p5], 전동기·발전기 설계·구동 제어[^home], 상태 추정·필터링(데이터 동화)[^p8]
- 홈페이지: <https://eecl.snu.ac.kr/>
- 근거와 출처: [EECL 근거 페이지](eecl-sources.md)

> 전기 에너지를 쓰임에 맞는 형태로 바꾸는 전력전자 회로와 그 제어를 연구하는 연구실이다. 전동기 제어, 무선 전력 전송, 고주파 전력 변환 회로, 전력전자에 쓰는 기계 학습을 주요 연구 주제로 두고, 연구 결과를 산업 응용에 바로 쓸 수 있게 하는 응용 지향 연구를 목표로 한다.[^home][^weare][^ecelabv]

## 무엇을 연구하나

연구실은 서울대학교 전기·정보공학부 하정익 교수가 이끄는 곳으로, 누리집은 이름을 EECL(Electric Energy Conversion Lab)로 적고 학부 연구실 목록은 「전기 에너지 변환 연구실」로 적는다.[^home][^ecelab] 학부 연구실 상세에 따르면 연구실은 서울대학교 전력전자센터(SPEC, Seoul national university Power Electronics Center) 안에 있고, 전기 에너지 변환을 위한 회로 설계와 제어 알고리즘 개발을 연구한다.[^ecelabv] 같은 페이지는 친환경 자동차, 가전 제품, 산업에 널리 쓰이는 전동기 구동 시스템의 설계와 제어, 풍력·태양광 같은 신재생 에너지, 무선 전력 전송, GaN(질화갈륨)과 SiC(탄화규소) 같은 고속 스위칭 소자(전류를 빠르게 켜고 끌 수 있는 반도체 스위치)를 이용한 전력 변환 회로 개발을 연구 내용으로 든다.[^ecelabv] 학부 연구실 목록은 이 연구실을 전기에너지 시스템 연구그룹에 올린다.[^ecelab]

누리집 We are 페이지는 EECL을 서울대 본교 캠퍼스에 있는 전력·에너지 전자(power and energy electronics) 전문 연구 센터로 소개한다.[^weare] 전력전자(power electronics)는 반도체 스위치를 켜고 끄는 동작으로 전력의 전압·전류·주파수를 바꾸고 제어하는 기술이다. 같은 페이지는 연구실이 전동기 제어, 무선 전력 전송, 고주파 변환기, 계통 연계 변환기(전력망에 연결되어 전력망과 전력을 주고받는 변환기), 전력전자의 기계 학습을 다룬다고 적는다.[^weare] We are 페이지의 Mission은 연구실이 전력전자 전반에서 응용 지향 연구를 목표로 하며, 이론 해석과 시뮬레이션 설계는 실제로 구현할 수 있는 하드웨어로 가는 디딤돌이고, 최종 목표는 연구 결과를 산업 응용에 바로 쓸 수 있게 하는 것이라고 밝힌다.[^weare] 연구 결과는 대부분 국제 학회와 학술지로 발표되고, 산업체 협력사와 함께 제품에 구현된다고 적는다.[^weare]

누리집 첫 화면은 연구 주제를 네 갈래로 적는다.[^home] 첫째 전동기 제어(Electric Machine Control)는 전동기의 구동 특성을 높이는 제어 알고리즘 개발로, 자동차와 철도 차량에 쓰는 견인 전동기(차량을 움직이는 힘을 내는 전동기), 의료 기기에 쓰는 소형 구동 시스템(Micro Drive Systems), 가변 샘플링(제어기가 측정값을 읽는 시간 간격을 바꾸는 기법)을 쓰는 정밀 전동기 제어, 전동기의 비선형성을 다뤄 토크 리플(전동기가 내는 회전력이 일정하지 않고 주기적으로 오르내리는 성분)을 줄이는 일을 든다. 둘째 무선 전력 전송은 와이드 밴드갭 반도체(전자가 전류를 나를 수 있게 되려면 넘어야 하는 에너지 간격인 띠틈이 넓은 반도체로, SiC와 GaN이 여기에 든다)가 쓰이면서 관심이 커지고 있다는 점과, 더 높은 전력 효율과 줄어든 크기·무게, 낮은 비용을 가능하게 한다는 점을 적는다. 방식으로는 IPT(유도 전력 전송, Inductive Power Transfer: 코일 사이의 자기장으로 전력을 보내는 방식)와 CPT(용량성 전력 전송, Capacitive Power Transfer: 마주 보는 도체판 사이의 전기장으로 전력을 보내는 방식)를, 응용으로는 휴대폰 무선 충전기, 로프 없는 엘리베이터, 차량 탑재형 전기차 충전기를 든다.[^home]

셋째 전력전자의 기계 학습은 인공 신경망으로 토크 리플을 줄이는 일, 기존 센서리스 방법(회전자의 위치·속도를 재는 센서 없이 전압·전류 신호로 이를 추정하는 방법)을 기계 학습 기반 추정으로 대신하는 일, 온도 센서를 없애 신뢰성을 높이고 비용을 줄이는 일, 기계 학습으로 고장을 분류하고 이상을 탐지하는 일을 든다. 첫 화면은 이 고장 분류와 이상 탐지의 적용 대상으로 산업용 6축 로봇과 전기차 구동 시스템을 들고, 고장을 일찍 찾아 시스템 신뢰성을 높인다고 적는다.[^home] 넷째 고주파 변환기(High Frequency Converter)는 SiC와 GaN 스위치로 수십 MHz의 동작 주파수에 이르는 변환기다. 첫 화면은 스위칭 주파수가 높아지면 인덕터(전류가 흐를 때 자기장에 에너지를 저장하고 전류의 변화를 거스르는 부품)와 커패시터(두 도체 사이에 전하를 모아 에너지를 저장하는 부품)의 크기가 줄고, 철심 없는 공심 인덕터를 쓸 수 있어 철손(철심에서 생기는 전력 손실)이 없어진다고 적는다. 스위칭 손실과 전자기 잡음을 줄이는 일, 소프트 스위칭(스위치에 걸린 전압이나 흐르는 전류가 0인 순간에 켜고 끄는 방식)의 조건·설계 방법·제어 전략 연구, 부하의 동작점에 따라 제어 방법을 바꾸는 일을 들고, 응용으로 휴대폰 무선 충전기와 반도체 제조 공정의 플라스마 시스템을 든다.[^home]

학부 연구실 상세의 연구 분야 목록은 일반 전력 전자 분야(고효율 인버터 기술과 회로 최적화, 센서 제거 및 저감 기술, 고속 스위칭 DC/DC 컨버터, 초고속 전동기 제어 기술, 고성능 필터 디자인 등), 동력변환 분야(「전기자동차 및 전자 차량 제어의 에너지 변환 기술」, 차세대 가전과 로봇의 에너지 변환·제어 기술), 신재생 에너지 분야(풍력, 태양광, 화학 발전 기술), 의료용 마이크로 로봇 시스템 설계(자기 추진(Magnetic propulsion)을 이용한 의료용 로봇 구동 시스템 설계)를 든다.[^ecelabv] 인버터는 직류 전력을 교류 전력으로 바꾸는 장치이고, DC/DC 컨버터는 직류 전압을 크기가 다른 직류 전압으로 바꾸는 회로다. 최근 학술지 논문 목록에도 여러 코일이 만드는 자기장으로 물체를 움직이는 자기 조작 시스템과 전자기 항법 시스템의 논문이 있다.[^pubs] Research Fields 페이지는 협력(Collaboration) 대학 10곳(Stanford University, Massachusetts Institute of Technology, KAIST 등)과 기관(Agency) 6곳, 후원 기업(Our Sponsors) 16곳(Samsung Electronics, LG Electronics, Hyundai Motor Company, General Motors 등)을 적는다.[^fields]

## 주요 연구 주제

### 1. 전동기 제어와 센서리스 구동

첫 화면의 첫째 갈래가 전동기의 구동 특성을 높이는 제어 알고리즘 개발이고,[^home] Professor 페이지는 교수가 교류 전동기 구동(ac drives)의 센서리스 제어에 기여한 공로로 IEEE Fellow가 되었다고 적는다.[^prof] 최근 논문 목록에는 인버터의 직류단에 단 전류 센서 하나(single DC-link current sensor)나 세 개의 션트 전류 센서(three-shunt current sensors, 션트는 전류가 흐를 때 양 끝에 생기는 전압으로 전류를 재는 저항)로 전류를 재면서 IPMSM(매입형 영구자석 동기 전동기, Interior Permanent Magnet Synchronous Motor: 회전자 안에 영구자석을 묻고, 고정자가 만드는 회전 자기장과 같은 속도로 도는 전동기)을 센서 없이 제어하는 논문이 이어진다.[^pubs] 개방 권선 전동기(open-end winding motor: 세 상 권선을 한 점에 묶지 않고 양 끝을 모두 인버터에 잇는 전동기 구성) 구동에서는 영상분 전류(zero-sequence current: 세 상에 크기와 위상이 같게 흐르는 전류 성분)를 억제하는 혼합 변조(IEEE Transactions on Power Electronics 2026)와, 영상분 전류까지 함께 다루는 다변수 비간섭 전류 제어(대표 논문 1)가 있다.[^pubs][^p1] 대표 논문 2는 전기차의 전동기 구동 시스템을 충전기로 쓰는 전동기 일체형 충전기에서 전동기 두 상에 전류를 흘려 충전 효율을 높이고 토크를 없애는 방법이다.[^p2] 그 밖에 인버터로 구동하는 IPMSM의 베어링 전류(전동기 축을 받치는 베어링을 지나 흐르는 전류) 분석과 억제(IEEE Transactions on Industrial Electronics 2025), 6스텝 운전(인버터가 한 주기에 여섯 가지 스위칭 상태만 쓰는 운전)을 포함하는 동기 과변조(변조 지수를 선형 범위 밖으로 높여 출력 전압을 키우는 변조, IEEE Transactions on Industrial Electronics 2024), 인덕턴스가 낮은 BLDC 전동기(브러시 없는 직류 전동기, Brushless DC motor)의 전류 전환 토크 리플을 줄이는 PWM(펄스 폭 변조, Pulse Width Modulation: 스위치를 켜 두는 시간의 비율을 바꿔 평균 전압을 조절하는 방법) 방법(IEEE Transactions on Industrial Electronics 2023)이 있다.[^pubs] 과제로는 Hyundai Motor Group의 개방 권선 PMSM 구동 시스템(2020년 1월–), Hyundai TRANSYS의 6스텝 운전을 포함한 동기 과변조(2023년 1–12월), Hyundai MOBIS의 베어링 전류 분석·억제(2022년 7월–2023년 8월), Samsung Electronics의 가전용 단일 션트 인버터 저속 센서리스 제어(2023년 6월–2024년 6월)가 있다.[^projects] 2025년 IEEE SLED 학회에서는 세 션트 전류 센서를 쓰는 IPMSM 센서리스 제어 논문이 Best Paper Award를 받았다.[^news]

### 2. 무선 전력 전송

첫 화면의 둘째 갈래로, 코일의 자기장으로 보내는 유도 방식(IPT)과 도체판의 전기장으로 보내는 용량 방식(CPT)을 함께 다룬다.[^home] 대표 논문 3은 용량성 전력 전송에서 공기 틈과 도체판의 어긋남이 바뀌어도 출력 전력이 거의 일정하도록, 한쪽에만 보상 회로망을 두어 수신 쪽 회로의 부피와 무게를 줄이는 설계 방법이다.[^p3] 대표 논문 4는 6.78 MHz 유도 전력 전송에서 코일이 어긋나도 출력 전력이 일정하도록 임피던스 정합 회로망(전원과 부하 사이에 두어 부하가 전원 쪽에서 보이는 임피던스를 원하는 값으로 바꾸는 회로)을 최적화하는 절차다.[^p4] 논문 목록에는 2포트 회로망(입력 단자 한 쌍과 출력 단자 한 쌍을 가진 회로) 해석에 바탕을 둔 무선 전력 전송용 임피던스 압축 정합 회로망(IEEE Journal of Emerging and Selected Topics in Industrial Electronics 2022)도 있고, 학회 발표에는 전기차용 비대칭 패드를 쓴 10 kW 소간극 무선 전력 전송 시스템(WPTCE 2024)과 3상·단상 무선 전력 전송 시스템의 상호 운용 제어(IPEC 2026)가 있다.[^pubs] 과제로는 Hyundai Motor Group의 전기차용 10 kW 소간극 무선 전력 전송 시스템(2023년 1–12월)과 결합 변화를 고려한 용량성 전력 전송 보상 회로망 설계(2022년 1–12월)가 있다.[^projects]

### 3. 고주파·고효율 전력 변환 회로

첫 화면의 넷째 갈래인 고주파 변환기와, 학부 연구실 상세가 드는 GaN·SiC 고속 스위칭 소자 기반 전력 변환 회로가 이 갈래다.[^home][^ecelabv] 대표 논문 5는 48 V를 12 V로 바꾸는 공진형 플라잉 커패시터 멀티레벨 변환기(접지에 고정되지 않은 커패시터를 스위치 사이에 두어 여러 단계의 전압을 만드는 변환기)에서 공진 주파수를 일정하게 유지하는 새 구조를 제안하고, 이 구조에 필요한 스위치를 GaN 스위치로 구현했다.[^p5] 대표 논문 6은 이중 능동 브리지(DAB, Dual Active Bridge: 변압기 양쪽에 스위치 브리지를 하나씩 두고 두 브리지의 스위칭 위상 차로 전력의 크기와 방향을 조절하는 직류-직류 변환기)의 5차 공진 회로망 설계와, 네 가지 제어 변수를 함께 쓰는 변조 방법이다.[^p6] 논문 목록에는 DAB 변환기의 공진 회로망 설계와 해석(IEEE Journal of Emerging and Selected Topics in Power Electronics 2024), 정해진 전기차 충전 곡선에 맞춘 공진형 DAB 변환기 설계(IEEE Access 2026), 영전압 스위칭(ZVS, Zero-Voltage Switching: 스위치에 걸린 전압이 0일 때 스위치를 켜는 방식)과 최소 실효 전류를 노리는 직렬 공진 이중 능동 하프 브리지 변환기의 변조(IEEE Transactions on Industry Applications 2024), 저전압 직류(LVDC) 배전 시스템을 위한 개선형 DAB 변환기의 구조와 제어(IEEE Transactions on Power Electronics 2023), PCB(인쇄 회로 기판, Printed Circuit Board) 변압기를 쓴 27.12 MHz 단일 스위치 DC-DC 변환기(IEEE Access 2023), 스위치드 커패시터 변환기(커패시터의 연결을 스위치로 바꿔 가며 전압을 바꾸는 변환기)의 방정식 기반 설계 방법(IEEE Transactions on Power Electronics 2026)이 있다.[^pubs] 계통 연계 쪽으로는 누설 전류(의도한 회로 경로를 벗어나 접지 등으로 새어 흐르는 전류)를 억제하는 단상·3상 PWM 변환기의 제어와 변조(IEEE Transactions on Power Electronics 2025), 저전압 직류 전력망에서 누설 전류를 억제하는 비절연(변압기로 입력과 출력을 전기적으로 나누지 않은) 3스위치 DC-DC 변환기(IEEE Transactions on Power Electronics 2026), 매우 약한 전력망(ultra-weak grid)에서 그리드 포밍 인버터(스스로 전압과 주파수의 기준을 만들어 전력망에 전력을 내보내는 인버터)의 출력 능력 분석(IEEE Journal of Emerging and Selected Topics in Power Electronics 2026), 불평형 전력망에서 3상 변환기의 제어(Journal of Power Electronics 2025)가 있다.[^pubs] 과제로는 사람의 안전과 전자파 적합성(전자 기기가 내는 전자파가 다른 기기에 방해가 되지 않고 주변 전자파에도 견디는 성질)을 위한 비절연 전기차 충전기의 제어·변조 방법(NRF, 2024년 4월–), GaN 기반 13.56 MHz, 1 kW 병렬 결합 RF(무선 주파수, Radio Frequency) 전력 증폭기, Samsung Electronics의 공진형 DAB 변환기 4자유도 변조(2023년 1–12월)가 있다.[^projects] 이 갈래의 연구로 2025–2026년에 IEEE Journal of Emerging and Selected Topics in Power Electronics의 2025 Second Place Prize Paper Award(대표 논문 5), IEEE/PSMA PwrSoC 2025와 IEEE COMPEL 2026의 Best Poster Award, IPEC-Nagasaki 2026의 Outstanding Paper Award for Young Engineers가 나왔다.[^news]

### 4. 전력전자의 기계 학습

첫 화면의 셋째 갈래로, 기계 학습으로 센서를 대신하는 추정과 고장 분류·이상 탐지를 다룬다.[^home] 대표 논문 7은 임베디드 시스템(기기 안에 넣어 정해진 일을 하도록 만든 컴퓨터 시스템)에서 돌아가는 전동기 구동 시스템의 데이터 기반 고장 진단이고, 대표 논문 8은 저속 영역에서 PMSM(영구자석 동기 전동기, Permanent Magnet Synchronous Motor: 회전자에 영구자석을 쓰고 고정자가 만드는 회전 자기장과 같은 속도로 도는 전동기)의 회전자 위치를 신경망으로 추정해 위치 센서 없이 제어하는 방법이다.[^p7][^p8] 논문 목록에는 특징 거리를 종합한 앙상블(여러 모델의 판단을 합쳐 쓰는 방법) 기반 유도 전동기(고정자의 회전 자기장이 회전자에 전류를 유도해 도는 전동기) 이상 탐지(IEEE Transactions on Industry Applications 2024)가 있고, 학회 발표에는 오토인코더(입력을 압축했다가 다시 복원하도록 학습하는 신경망)를 쓴 왕복동 압축기의 비지도 이상 탐지(ECCE 2024), 다중 모듈 신경망을 쓴 전압 주입 기반 전력 소자 고장 진단(IPEMC 2024), 다채널 신경망 기반 전동기 열 감시(SLED 2023)가 있다.[^pubs] 과제로는 LG Electronics의 전동기 고장 진단·분류 기술(2023년 7월–2024년 7월), Samsung Electronics의 오토인코더를 쓴 왕복동 압축기 비지도 이상 탐지(2023년 6월–2024년 6월), 데이터 기반 PMSM 센서리스 제어(2023년 6월–2024년 6월)가 있다.[^projects]

## 대표 논문

하정익 교수가 마지막 저자인 2021–2026년 학술지 논문 가운데 누리집 첫 화면의 연구 주제 갈래(전동기 제어, 무선 전력 전송, 고주파 변환기, 전력전자의 기계 학습)마다 두 편씩, 초록을 확인할 수 있는 논문을 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다. 연도는 출판사 서지의 출판 연도다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [Multivariable Decoupling Current Control for Open-End Winding Permanent Magnet Motor Drives](https://doi.org/10.1109/TIE.2026.3663722) · IEEE Transactions on Industrial Electronics | 이 논문은 공통 직류 전원 하나에 연결된 개방 권선 영구자석 동기 전동기(OEW-PMSM)의 전류 제어기를 설계했다. 기존 제어는 영상분(n축) 성분을 독립 변수로 다루며 그 성분이 dq 성분(세 상 전류를 회전자와 함께 도는 서로 직각인 두 축으로 바꿔 나타낸 성분)에 주는 동적 영향을 무시해 왔다. 이 논문은 먼저 상호 인덕턴스(한 권선의 전류 변화가 다른 권선에 전압을 일으키는 정도)와 회전자 위치에 따른 공간 고조파(회전자 위치에 따라 달라지는, 기본 성분 밖의 자기적 성분)를 모든 축에 넣은 통합 dqn 전동기 모델을 세우고, 이 모델로 부하가 바뀌어도 안정하게 동작하면서 전류 동특성을 완전히 비간섭(한 축의 전류가 다른 축의 전류 변화에 끌려가지 않게 함)으로 만드는 다변수 제어기를 해석적으로 유도했다. 제어기가 축 사이의 결합을 구조에 담아 영상분 전류를 능동적으로 조절하므로 정상 상태와 과도 상태 성능이 좋아진다. 전기차용으로 개발된 전동기로 한 실험에서 기존 제어보다 정상 상태 파형 품질이 좋아졌고, 전류의 전고조파 왜곡(THD, Total Harmonic Distortion: 기본 주파수 밖의 성분이 섞인 정도)이 6.61%에서 4.86%로 줄었다. 과도 응답도 크게 나아졌고, 토크가 갑자기 바뀔 때에도 영상분 전류는 d–q 전류의 외란(바깥에서 끼어드는 변동)에 영향받지 않고 안정했다.[^p1] | 1저자 G. C. Lim(Gyu Cheol Lim), 마지막 저자 하정익 (5명) |
| 2 | 2025 | [Two-Phase DC Charging Method for Improved Efficiency and Zero Torque in Motor-Integrated Charger](https://doi.org/10.1109/TIE.2024.3468730) · IEEE Transactions on Industrial Electronics | 최근 전기차는 더 빠른 충전을 위해 배터리 전압을 거의 두 배로 높였지만, 기존 저전압 급속 충전기로는 이런 차를 충전하기 어렵다. 이 문제를 풀려고 전동기 구동 시스템을 쓰는 승압 충전 구조가 나와 상용 전기차에 쓰이고 있다. 이런 전동기 일체형 충전기는 3상 인터리브드 승압 변환기(여러 상의 승압 회로를 시간을 엇갈려 번갈아 동작시키는 변환기)로 제어되는데, 승압에 낮은 영상분 인덕턴스를 쓰기 때문에 리플 전류(평균값 주위로 오르내리는 전류 성분)와 손실이 커질 수 있다. 이 논문은 손실을 분석하고, 충전 효율을 높이면서 전동기가 돌지 않도록 토크를 없애는 방법을 찾았다. 영상분 인덕턴스를 쓰는 기존 방법과 달리 전동기 두 상에 전류를 흘려 차동 모드 인덕턴스(두 상 사이를 오가는 전류가 겪는 인덕턴스)를 쓰며, 그 결과 전류 리플이 크게 줄어 효율이 높아진다. 회전을 명시적으로 억제하는 위치 제어기도 제안했다. 이론으로 타당성을 따지고, 축소 규모 실험 장치의 실험 결과로 효과를 보였다.[^p2] | 1저자 J. Yang(Junhyuk Yang), 마지막 저자 하정익 (4명) |
| 3 | 2024 | [Single-Sided Compensation Network Design Method for Capacitive Power Transfer System Considering Coupling Variation](https://doi.org/10.1109/TIA.2024.3384346) · IEEE Transactions on Industry Applications | 용량성 전력 전송 시스템에서는 공기 틈의 변화와 결합판의 어긋남 때문에 결합 정도가 변하는 일이 피할 수 없이 생긴다. 이 논문은 결합 변화를 고려한 용량성 전력 전송 시스템의 단측 보상 회로망(결합부가 일으키는 전압과 전류의 어긋남을 상쇄하도록 덧붙이는 인덕터·커패시터 회로) 설계 방법을 제시했다. 보상 회로망을 한쪽에만 두어 수신 쪽 회로의 부피와 무게를 줄인다. 제안한 보상 회로망은 미리 고른 좁은 동작 주파수 범위 안에서 변하는 부하 임피던스를 하나의 저항성 점(임피던스가 순수한 저항처럼 보이는 동작점)으로 바꿔, 결합이 변해도 출력 전력이 일정하고 위상각(전압과 전류 파형이 어긋난 정도)이 0인 동작을 얻는다. 설계에는 2포트 회로망 해석에 바탕을 둔 임피던스 정합 회로망 설계 방법을 쓴다. 시뮬레이션과 공기 틈이 작은 1.2 kW 용량성 전력 전송 시제품으로 검증했고, 시제품은 어긋남이 없을 때 최대 효율 91.2%, 결합 도체판의 면적이 최대 40% 어긋났을 때 최소 효율 89.9%를 내면서 출력 전력이 거의 일정하고 위상각이 0인 동작을 보였다.[^p3] | 1저자 S. Choi(Sunghyuk Choi), 마지막 저자 하정익 (6명) |
| 4 | 2024 | [Impedance Matching Network Design for 6.78-MHz Wireless Power Transfer System With Constant Power Characteristics Against Misalignment](https://doi.org/10.1109/TPEL.2023.3320199) · IEEE Transactions on Power Electronics | 무선 전력 전송 기술은 기계적 접촉 없이 에너지를 보낼 수 있어 여러 산업 분야에 알맞고, 그래서 점점 널리 쓰이고 있다. 이 논문은 수 MHz 이상의 주파수에서 Class E(스위치 하나와 공진 회로로 고주파 교류를 만드는 방식) 같은 단일 스위치 인버터로 구동하는 유도 전력 전송 시스템을 다룬다. 이런 시스템의 주요 문제는 송신 코일과 수신 코일의 상대 위치에 따라 출력과 효율이 크게 달라진다는 것이고, 기존 해결책 다수는 조정 가능한 부품과 그 구동 회로를 더 넣어야 해 비용과 복잡도가 늘었다. 이 논문은 코일이 어긋나거나 공기 틈이 바뀌어도 출력 전력이 일정한 특성을 얻도록 무선 전력 전송 시스템의 2포트 임피던스 정합 회로망을 체계적으로 최적화하는 절차를 제시했다. 시스템 자체가 어긋남에 강한 특성을 가지므로 제어와 조정 가능한 부품의 필요를 크게 줄일 수 있다. 6.78 MHz/60 W 시제품과 실험 결과로 효과를 확인했다.[^p4] | 1저자 E. Chung(Euihoon Chung), 마지막 저자 하정익 (2명) |
| 5 | 2025 | [Flying Capacitor Multilevel Converter at Constant Resonant Frequency With Negative-Voltage-Blocking GaN Switch](https://doi.org/10.1109/JESTPE.2025.3571425) · IEEE Journal of Emerging and Selected Topics in Power Electronics | 스위치드 커패시터(SC) 방식으로 동작하는 공진형 플라잉 커패시터 멀티레벨(RFCML) 변환기는 효율과 전력 밀도(부피당 다룰 수 있는 전력)가 높아 주목받아 왔다. RFCML 변환기는 플라잉 커패시터의 연결을 바꿔 전하를 옮기므로 동작 단계마다 공진 주파수가 달라진다. 이렇게 공진 주파수가 여럿이면 인덕터 전류의 최댓값과 실효값(교류의 크기를 같은 저항에서 같은 열을 내는 직류 값으로 나타낸 값)이 모두 커져 인덕터가 커진다. 이 논문은 크기가 작은(compact) 경로 변경 커패시터(rerouted capacitor)로 공진 주파수를 일정하게 유지해 필요한 인덕터 부피를 줄이는 새 RFCML 변환기를 제안했다. 이 구조에는 경로 변경 커패시터의 충전 전압보다 큰 역전압을 막을 수 있는 스위치가 필요하며, 이를 GaN 스위치와 음전압 게이트 구동 회로(스위치를 켜고 끄는 제어 전압을 만드는 회로)로 구현했다. 경로 변경 커패시터를 위해 스위치 두 개를 더한 이 구조는 기존 구조보다 스위치 저항이 낮아 도통 손실(스위치가 켜져 전류가 흐를 때 저항 때문에 생기는 손실)이 줄고 효율이 높아진다. 영전압 스위칭도 적용해 가벼운 부하에서의 효율을 높였다. 48 V를 12 V로 바꾸는 RFCML 변환기 시제품의 실험으로 검증해 공진 주파수가 일정한 동작을 확인했고, 최고 효율 98.9%, 전부하 효율 96.7%, 전력 밀도 2169 W/in³를 얻었다.[^p5] | 1저자 D. Yun(Dam Yun), 마지막 저자 하정익 (3명) |
| 6 | 2024 | [Design and Four-Degree-of-Freedom Modulation Method of Dual Active Bridge Converter](https://doi.org/10.1109/JESTPE.2024.3448290) · IEEE Journal of Emerging and Selected Topics in Power Electronics | 이 논문은 출력 전압이 넓게 바뀌어도 고르게 높은 효율을 내는 5차 공진형 이중 능동 브리지(DAB) 변환기의 설계와 변조 방법을 제시했다. 5차 공진 회로망(인덕터와 커패시터가 에너지를 주고받도록 연결한 회로)은 새로 제안한 두 주파수 공진 회로망 설계 방법으로 설계한다. DAB 변환기 제어의 네 자유도(4DOF), 곧 1차 쪽과 2차 쪽의 듀티비(한 주기에서 스위치를 켜 두는 시간의 비율), 전압 위상 이동각, 스위칭 주파수를 함께 써서 부하 전압 범위 전체에서 영전압 스위칭을 하면서 도통 손실을 줄인다. 양쪽의 정상 상태 공진 전류를 고조파 분해(파형을 기본 주파수와 그 정수배 주파수 성분들로 나누는 일)로 정확히 구하고, 이를 써서 최적의 4DOF 변조 변수를 수치 계산으로 얻는다. 같은 4DOF 변조를 쓰는 직렬 공진(SR) DAB 변환기와 비교해 실효 전류와 주파수 범위 면에서 장점을 보였다. 5.0 kW DAB 변환기 시제품의 시뮬레이션과 실험으로 효과를 확인했으며, 시제품은 입력 전압 400 V 고정, 스위칭 주파수 140–200 kHz에서 부하 전압 400–800 V 범위를 다루고 최고 효율 98.9%를 얻었다.[^p6] | 1저자 J. Lee(Junhyeong Lee), 마지막 저자 하정익 (3명) |
| 7 | 2025 | [Fault Diagnosis for Electric Drives Using Averagely Pooled and Downsampled Data Fusion on Embedded Systems](https://doi.org/10.1109/JESTPE.2024.3515659) · IEEE Journal of Emerging and Selected Topics in Power Electronics | 이 연구는 임베디드 시스템에서 전동기 구동 시스템의 고장을 진단하는 데이터 기반 방법을 제시했다. 추가 센서나 외부 계산 자원 없이 전류 홀 센서(전류가 만드는 자기장의 세기를 재어 전류를 알아내는 센서)의 오프셋(입력이 0일 때도 나오는 출력 치우침)·배율 오차(측정값이 실제 값과 일정한 비율로 어긋나는 오차)와 전력 스위치 개방 고장(스위치가 켜지지 않아 그 전류 경로가 끊기는 고장)을 진단하도록 설계했다. 첫째, 전동기 구동 시스템에서 고장 관련 정보가 풍부한 데이터 종류를 찾아 제시하고, 통계 분석으로 여러 후보 가운데 진단 모델을 만들 입력 데이터 종류의 효과적인 결합 방법을 제안했다. 둘째, 디지털 신호 처리기(DSP, Digital Signal Processor: 신호 계산에 맞춘 프로세서)가 다루는 많은 원시 데이터에서 핵심 정보를 지키면서 데이터 크기를 줄이도록, 평균 풀링(정해진 구간마다 평균값 하나만 남기는 방법)을 쓰는 다운샘플링(데이터의 표본 수를 줄이는 일) 방법을 도입했다. 셋째, 다운샘플링한 데이터로 고장을 정확히 진단하는 신경망 기반 분류기 진단 방식을 제안했다. 표본 추출부터 진단까지 방법의 효과를 해석적·통계적 검증으로 보였고, TMS320F28379S DSP에서 실시간 진단 결과를 제시했다.[^p7] | 1저자 J. Shim(Jaehoon Shim), 마지막 저자 하정익 (4명) |
| 8 | 2026 | [Data-Driven Position Estimation and Sensorless Control of PMSM Drive in Low-Speed Region](https://doi.org/10.1109/TIA.2025.3595132) · IEEE Transactions on Industry Applications | 이 논문은 영구자석 동기 전동기(PMSM)의 위치 센서리스 제어를 위한 데이터 기반 방법으로, 특히 저속 영역의 성능을 높이는 데 맞췄다. 이전의 데이터 기반 방법과 달리 세 가지를 내놓았다. 첫째, 신경망 기반 위치 추정기의 설계 과정을 제시하고 입력 특징을 격자 탐색(후보 값의 조합을 모두 시험해 고르는 방법)으로 골랐다. 둘째, 신경망 추정기의 학습 성능을 높이는 손실 함수(예측이 정답에서 벗어난 정도를 수치로 나타내, 학습이 줄여 나가는 함수)와 학습 알고리즘을 제안해 썼다. 셋째, 학습 데이터 집합을 효율적으로 만들고 데이터 수집 시간을 줄이는 데이터 증강(가진 데이터를 바꾸거나 합성해 학습 데이터를 늘리는 일) 방법을 도입했다. 그 결과 제안한 입력 특징과 학습 알고리즘은 기존 데이터 기반 방법보다 신경망 추정기의 위치 추정 정확도를 크게 높였다. 개발한 모델을 디지털 신호 처리기(DSP)에 구현해 실시간 동작을 확인했고, 4상한 운전(정회전·역회전과 구동·제동을 모두 하는 운전)에서 저속 영역의 동작 가능 영역이 최근 연구된 모델 기반 방법보다 49.80% 넓어졌다. 동적 상태 운전에서의 강인성도 검증했다.[^p8] | 1저자 J. Shim(Jaehoon Shim), 마지막 저자 하정익 (4명) |

## 교수와 전문 분야

하정익 교수(Jung-Ik Ha)는 서울대학교 전기·정보공학부 교수이다.[^ecefac][^eceprof] 학부 교수 상세는 전공을 전력전자, 전기 에너지 변환으로, 분야를 전력 전자 및 전기에너지 변환으로 적고, Research Interest로 센서리스·정밀 전동기 제어, 자동차와 가전 제품 기술·지능형 기기 기술, 전기-열 및 신재료 기반 에너지 변환, 스마트 그리드 접속 제품 기술과 에너지 네트워크를 든다.[^eceprof] 누리집 Professor 페이지의 Biography는 교수의 연구 관심을 여러 산업 분야를 위한 고효율·집적형 전기 에너지 변환의 회로와 제어로 적고, 교수가 전력전자와 전동기 구동 분야에서 200편이 넘는(more than 200) 학술지·학회 논문을 쓰거나 함께 썼으며 교류 전동기 구동의 센서리스 제어에 기여한 공로로 IEEE Fellow가 되었다고 적는다.[^prof]

교수는 서울대학교에서 전기공학 학사(1995년), 석사(1997년), 박사(2001년) 학위를 받았다.[^prof][^eceprof] 학부 교수 상세는 박사 학위 논문을 「고주파 신호 주입을 이용한 위치 및 속도 검출기가 없는 교류 전동기의 제어」로 적는다.[^eceprof] 경력은 일본 Yaskawa Electric 개발연구소 연구원(2001년 5월–2002년 6월), 서울대학교 기초전력공학공동연구소 전력전자센터 전임연구원(2002년 7월–2003년 3월), Samsung Electronics 생산기술연구소(Mechatronics & Manufacturing Technology Center)의 책임 연구원(Senior Engineer, 2003년 4월–2008년 2월)과 수석 연구원(Principal Engineer, 2008년 3월–2009년 11월), LS메카피온 기술총괄이사(CTO, 2009년 12월–2010년 8월)이고, 2010년 9월부터 서울대 전기·정보공학부에 있다.[^prof][^eceprof] 2016년 8월–2017년 7월에는 Massachusetts Institute of Technology의 방문 학자(Visiting Scholar)였다.[^prof] 학부 교수 상세는 2021년부터 서울대학교 공과대학 기획부학장과 시그넷 EV(SK group) 사외이사를 맡고 있다고 적는다.[^eceprof]

학회 활동으로 Professor 페이지는 IEEE Fellow(S’97–M’01–SM’12–F’18), 전력전자학회(KIPE, The Korean Institute of Power Electronics)의 부회장(Vice-President)과 이사(Board Member, BM’16–18), The Korean Institute of Electrical Engineers(KIEE) 이사(BM’16, 18), The Institute of Electronics and Information Engineers(IEIE) 회원, Journal of Power Electronics 편집장(Editor-in-Chief), IEEE Journal of Emerging and Selected Topics in Power Electronics 부편집장(Associate Editor)을 적는다.[^prof] 학부 교수 상세는 전력전자학회 부회장과 Journal of Power Electronics 편집장을 2018–2021년, IEEE Journal of Emerging and Selected Topics in Power Electronics 부편집장을 2015–2020년으로 적는다.[^eceprof] Professor 페이지의 수상 칸은 IEEE APEC의 Outstanding Presentation Award(2014년), IEEE IPEC ECCE-Asia의 Second Prize Paper Award(2018년), IEEE Transactions on Power Electronics의 Second Place Prize Paper Award(2018년), RWTH Aachen University의 Best Dissertation Prize(STAWAG Promotionspreis für die beste Dissertation, 2019년), IEEE PEAS 2021의 Excellent Speaker Award(2021년)를 적는다.[^prof] Courses 페이지에 따르면 교수는 학부 과목 Fundamentals of Circuit Theory and Lab과 Electric Machine and Control, 대학원 과목 Modern Resonant Converters와 Renewable Energy Conversion Systems를 맡고, 회로 실험 교재(Circuit Theory Experiment, Rainbow Books, 2021)의 저자로 이름이 올라 있다.[^courses] News and Info 페이지에는 공진형 변환기의 최근 연구 흐름과 발전을 다룬 교수의 책 「Modern Resonant Converters」가 나왔다는 글이 있다.[^news]

논문으로 보면 교수의 전문 분야는 교류 전동기의 센서리스 구동과 전력 변환 회로다. 누리집 학술지 목록의 1999–2005년 논문은 고주파 신호 주입 등으로 유도 전동기와 영구자석 전동기 등의 회전자 위치와 속도를 센서 없이 추정하는 제어가 중심이고, 2008–2010년에는 속도가 0이거나 낮은 영역의 센서리스 구동을 위한 대칭 교류 전동기의 고유한 자기적 위치 센서 해석, 단일 센서로 세 상 전류를 복원하는 전압 주입 방법, 단일 직류단 전류 센서를 쓰는 전류 예측을 다룬 교수 단독 저자 논문 세 편이 있다.[^pubs] 2013–2020년 목록은 인버터 하나로 전동기 두 대를 병렬 구동하는 시스템, 개방 권선·권선형 회전자 전동기, 작은 직류단 커패시터를 쓰는 전동기 구동과 계통 전류 제어, 고주파 단일 스위치 DC-DC 변환기, 자기 조작 시스템으로 넓어진다.[^pubs] 2021–2026년 목록은 단일 직류단·세 션트 전류 센서를 쓰는 센서리스 제어와 개방 권선 전동기 구동, DAB·공진형·스위치드 커패시터 변환기, 무선 전력 전송, 누설 전류 억제, 기계 학습 기반 고장 진단과 위치 추정으로 이어진다.[^pubs] 2021–2026년 대표 논문 8편은 모두 교수가 마지막 저자다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

첫 화면은 연구 주제마다 응용을 적는다. 전동기 제어는 자동차·철도 차량의 견인 전동기와 의료 기기의 소형 구동 시스템, 무선 전력 전송은 휴대폰 무선 충전기·로프 없는 엘리베이터·차량 탑재형 전기차 충전기, 기계 학습 고장 진단은 산업용 6축 로봇과 전기차 구동 시스템, 고주파 변환기는 휴대폰 무선 충전기와 반도체 제조 공정의 플라스마 시스템이다.[^home] 학부 연구실 상세는 친환경 자동차, 가전 제품, 산업의 전동기 구동 시스템과 풍력·태양광 신재생 에너지를 든다.[^ecelabv] 대표 논문 1은 전기차용으로 개발된 전동기로 실험했고, 대표 논문 2는 전기차의 전동기 구동 시스템으로 배터리를 충전하는 방법이다.[^p1][^p2] 대표 논문 5는 48 V를 12 V로 바꾸는 변환기이며, News and Info 페이지는 이 연구를 AI 데이터센터의 48 V 전원 시스템에 쓰는 저전압·대전류 중간 버스 변환기(IBC, Intermediate Bus Converter) 기술로 소개한다.[^p5][^news] 2026년 IEEE COMPEL Best Poster Award 논문은 모바일 기기용 6:1 스위치드 커패시터 변환기다.[^news] Research Fields 페이지의 후원 기업은 Samsung Electronics, Samsung SDI, LG Electronics, LG Innotek, Hyundai Motor Company, Hyundai Mobis, Hyundai Transys, Hyundai Rotem, HD KSOE, HD Heavy Industries, HD Elevator, Hyosung Heavy Industries, HL Mando, General Motors, STELLANTIS, QIT다.[^fields] 졸업생 진로에는 Hyundai Motor Company, Samsung Electronics, LG Electronics, Hyundai Mobis, SK Hynix, Analog Devices, National Renewable Energy Laboratory(NREL), Korea Institute of Machinery & Materials 같은 기업·연구기관과 Kookmin University, Ewha Womans University, Incheon National University, Myongji University, Hanyang University ERICA, Kwangwoon University의 연구실이 있다.[^alumni]

## 구성원

2026년 10월 23일 누리집 People 메뉴 기준 19명이다. Ph.D. Candidates 페이지의 Post Doctoral Researcher 칸 1명과 Ph.D. Candidates 칸 10명, M.S. Candidates 페이지 8명이며, 과정은 칸 이름을 옮겼고 「연구 주제」는 각 사람의 Research Interest 칸, 이메일은 페이지가 적은 학교 주소다.[^phd][^ms] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Juwon Lee | 박사후연구원 | Non-Isolated DC Charger, Grid-Connected Converter, Common Mode Voltage, EMI | wronskian@snu.ac.kr |  |
| Dongsu Lee | 박사과정 | Non-Isolated DC Charger, MVDC-LVDC Modular Converter, DC Microgrid | babypighill0@snu.ac.kr |  |
| Taesuk Joung | 박사과정 | Wireless Power Transfer, Power Converters | djm02055@snu.ac.kr |  |
| Dam Yun | 박사과정 | DC-DC Converters, WBG Switching Device Converters, Switched Capacitor DC-DC Converters | dam0710@snu.ac.kr | 5 |
| Minha Kim | 박사과정 | Data-Driven Electric Drive, Sensorless Drive | minha1998@snu.ac.kr | 8 |
| Junhyuk Yang | 박사과정 | Motor Drive, Control of Open-End Winding Motor | jhyang22@snu.ac.kr | 1, 2 |
| Sung Jun Lee | 박사과정 | Motor Drive, Common Mode Voltage, Bearing Current, Control of Wound Rotor Machine | sj1king@snu.ac.kr |  |
| Seongwon Lee | 박사과정 | Motor Drive, Sensorless Drive | sicorea1@snu.ac.kr |  |
| Taewoo Lee | 박사과정 | Wireless Power Transfer, High-Frequency DC-DC Converters | taewoo97@snu.ac.kr |  |
| Jun-sik Hwang | 박사과정 | Motor Drive, Single-shunt Current Reconstruction, Control of Open-End Winding Motor | js.hwang@snu.ac.kr |  |
| Won Hyo Jeong | 박사과정 | Power Converter, Motor Drive | wonhyo0428@snu.ac.kr |  |
| Joohyoung Ko | 석사과정 | Wireless Power Transfer, DC-DC Converters | joohyoung.ko@snu.ac.kr |  |
| Yewon Song | 석사과정 | Motor Drive, Renewable Energy | syewon@snu.ac.kr |  |
| Jin Wook Jung | 석사과정 | Wireless Power Transfer, Power Converter | dnr3377@snu.ac.kr |  |
| Min Suk Seo | 석사과정 | Wireless Power Transfer, Power Converter | min99@snu.ac.kr |  |
| Jiho Heo | 석사과정 | Motor Drive, Power Converter | jiho377@snu.ac.kr |  |
| Sangjin Park | 석사과정 | Motor Drive, Power Converter | 135psj@snu.ac.kr |  |
| Sumin Bae | 석사과정 | Motor Drive, Power Converter | sumin806@snu.ac.kr |  |
| Seung Su Jung | 석사과정 | Motor Drive, Power Converter | leo411@snu.ac.kr |  |

## 졸업생

누리집 People 메뉴 Alumni 페이지의 52행이다. Visiting Scholars 칸 4행(Post Doc. 2행, Visiting Scholar 2행), Ph.D. Holders 칸 27행, Master's Degree Graduates 칸 19행, Undergraduates 칸 2행이며, 학위·연도와 진로(Office 칸)는 누리집 표기 그대로다. Gyu Cheol Lim은 석사(M.S. 2019)와 박사(Ph.D. 2026) 칸에 두 번 올라 있고, Seongwon Lee와 Taewoo Lee는 석사 졸업(M.S. 2025) 뒤 박사과정으로 위 구성원 표에도 있다.[^alumni][^phd]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Wook-jin Lee | Post Doc. (2012) | Dept. of Electrical Engineering, Chungnam National University |
| Je-Hyun Yi | Post Doc. (2022) | New Power Plasma |
| Hirotaka Kato | Visiting Scholar (2025) | Nagaoka Power Electronics |
| Shanshan Zhao | Visiting Scholar (2025) | LS Electric |
| Hojoon Shin | Ph.D. (2015) | Hyundai Motor Company |
| Sungho Jung | Ph.D. (2017) | Korea Institute of Machinery & Materials |
| Yongjae Lee | Ph.D. (2017) | Hyundai Motor Company |
| Yongsu Han | Ph.D. (2017) | ITEC Lab, Dept. of Electrical Engineering, Kookmin University |
| Youngrack Son | Ph.D. (2017) | National Renewable Energy Laboratory (NREL) |
| Kahyun Lee | Ph.D. (2017) | ECCL, Dept. of Electronic and Electrical Engineering, Ewha Womans University |
| Kyunghwan Lee | Ph.D. (2018) | Samsung Electronics MX Division |
| Sangwoo Kang | Ph.D. (2018) | Samsung Electronics |
| Jinwoong Kim | Ph.D. (2018) | Hyundai Mobis |
| Hyeon-Gyu Choi | Ph.D. (2020) | ECCC Lab, Dept. of Electrical Engineering, Incheon National University |
| Eui-Hoon Jung | Ph.D. (2020) | AMPL, Dept. of Electrical Engineering, Myongji University |
| Jun Lee | Ph.D. (2020) | Samsung Electronics Semiconductor R&D Center |
| Sun-Ku Kwon | Ph.D. (2021) | LG Electronics HS Division |
| Geonhong Min | Ph.D. (2021) | Samsung Electronics MX Division |
| Gwangyol Noh | Ph.D. (2022) | Analog Devices |
| Jae-Yong Park | Ph.D. (2022) | Samsung Electronics Future Robotics Office |
| Jin-Su Hong | Ph.D. (2023) | Hyundai Motor Company |
| Jonghun Choi | Ph.D. (2023) | Hyundai Motor Company |
| Sangwon Lee | Ph.D. (2024) | HY-EMS Lab, School of Electrical Engineering, Hanyang University ERICA |
| Jaehoon Shim | Ph.D. (2024) | SEED Lab, Dept. of Electrical Engineering, Myongji University |
| Junhyeong Lee | Ph.D. (2024) | PE Lab, Dept. of Electrical Engineering, Kwangwoon University |
| Jeongjun Seo | Ph.D. (2025) | Samsung Electronics Network Division |
| Byungryang Park | Ph.D. (2025) | LG Electronics ES Division |
| Sunghyuck Choi | Ph.D. (2026) | Samsung Electronics Network Division |
| Cheolmin Hwang | Ph.D. (2026) | Hyundai Mobis Robotics Business Group |
| Juwon Lee | Ph.D. (2026) | Postdoctoral Researcher in Purdue Power Lab @ Purdue University |
| Gyu Cheol Lim | Ph.D. (2026) | Postdoctoral Researcher in PENGUIN Lab @ University of Pennsylvania |
| Kwonyub Hyung | M.S. (2014) | Samsung Electronics |
| Youngnam Kim | M.S. (2014) | Patent Attorney |
| Young-Ho Chae | M.S. (2016) | Hyundai Motor Company |
| Choongin Lee | M.S. (2018) | Obtained Ph.D. degree from Railab @ Kaist |
| Gyu Cheol Lim | M.S. (2019) | Obtained Ph.D. degree from EECL @ SNU |
| Young-Hyun Choi | M.S. (2019) |  |
| Dong-eon Kim | M.S. (2019) | Naver Labs |
| Min Jea Sung | M.S. (2020) | Dawonsys Co. Ltd |
| Jules Mace | M.S. (2020) | Obtained Ph.D. degree from Power Electronics Lab (PEL) @ EPFL |
| Yongjin Jeon | M.S. (2020) | Samsung Research |
| Jimin Park | M.S. (2023) | Hyundai Motor Company |
| Hyunjun Lee | M.S. (2023) | Hyundai Motor Company |
| Jeonghwan Kim | M.S. (2024) | LG Electronics ES Division |
| YoungJun Kim | M.S. (2025) | Hanyang University Law School |
| Seongil Lee | M.S. (2025) | LG Electronics ES Division |
| Seongwon Lee | M.S. (2025) | Ph.D. Candidate in EECL |
| Taewoo Lee | M.S. (2025) | Ph.D. Candidate in EECL |
| Wontom Chae | M.S. (2026) | HD Hyundai KSOE |
| Nahyun Kang | M.S. (2026) | SK Hynix |
| Hyukjae Kwon | B.S. (2022) | Ph.D. Candidate in Power Electronics Research Lab @ Princeton University |
| Seokwon Choi | B.S. (2025) | Ph.D. Candidate in Berkeley Power and Energy Center (BPEC) @ UC Berkeley |

## 최근 학술지 논문 (2021–2026)

누리집 Achievements 메뉴 International Journals 페이지의 2021–2026년 구역 37편(2026년 5, 2025년 7, 2024년 10, 2023년 7, 2022년 3, 2021년 5)과 Domestic Journals 페이지의 2021년 구역 1편(끝에 (국내))이다. 연도는 누리집이 나눈 연도 구역이고, 구역 연도와 학술지 호의 연도가 다른 논문이 있다(예: 2025년 구역에 실린 2026년 호 논문). 저자 순서와 제목·학술지·DOI 표기는 누리집 그대로이고, 2023년 구역 한 편 끝의 (Corresponding Author)도 누리집 문구다. 저자와 제목을 따옴표로 나누지 않고 한 줄로 적은 두 편(2025년 구역 1편, 국내 1편)은 누리집 줄을 그대로 실었다. 교수는 2010년 9월부터 서울대에 있으므로 모두 서울대 재직 시기 논문이다.[^pubs][^prof]

**2026**

- M. Kim, B. R. Park, S. Lee and J. -I. Ha. "Switching-Frequency Voltage Injection Methods for Sensorless IPMSM Control in Three-Shunt Current Sensing Inverter". *IEEE Journal of Emerging and Selected Topics in Power Electronics, doi: 10.1109/JESTPE.2026.3707033*.
- J. Lee, E. Chung, T. Ryu and J. -I. Ha. "Design Methodology for a CLLLC Resonant Dual Active Bridge Converter with Minimized RMS Current and ZVS Operation for Predefined EV Charging Profile". *IEEE Access, vol. 14, pp. 82018-82035, 2026, doi: 10.1109/ACCESS.2026.3698097*.
- J. Yang, G. C. Lim and J. -I. Ha. "Hybrid Modulation for Zero-Sequence Current Suppression in Common-Source Fed Open-End Winding Motor Drive System". *IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2026.3683933*.
- G. C. Lim, J. Yang, C. -M. Hwang, K. Lee and J. -I. Ha. "Multivariable Decoupling Current Control for Open-End Winding Permanent Magnet Motor Drives". *IEEE Transactions on Industrial Electronics, vol. 73, no. 7, pp. 9787-9799, July 2026, doi: 10.1109/TIE.2026.3663722*.
- B. R. Park, G. C. Lim, J. Shim and J. -I. Ha. "Switching Frequency Voltage Injection Method for Sensorless Control Using Current Derivatives in IPMSM Drives". *IEEE Transactions on Industry Applications, doi: 10.1109/TIA.2026.3654506*.

**2025**

- S. Choi, D. Yun and J. -I. Ha. "Equation-Based Design Methodology for Switched-Capacitor Converter Topologies". *IEEE Transactions on Power Electronics, vol. 41, no. 6, pp. 9437-9453, June 2026, doi: 10.1109/TPEL.2025.3647425*.
- D. Lee, J. Lee and J. -I. Ha. "Non-Isolated Three-Switch DC-DC Converter Suppressing Leakage Currents in Low-Voltage DC Grid". *IEEE Transactions on Power Electronics, vol. 41, no. 4, pp. 6811-6827, April 2026, doi: 10.1109/TPEL.2025.3625952*.
- S. Zhao, J. Lee, S. Cui and J. -I. Ha. "Analysis of the Power Output Capabilities of Grid-Forming Inverters under Reactive Power Control Mode in Ultra-Weak Grid". *IEEE Journal of Emerging and Selected Topics in Power Electronics, vol. 14, no. 2, pp. 1724-1741, April 2026, doi: 10.1109/JESTPE.2025.3625922*.
- J. Shim, B. R. Park, M. Kim and J. -I. Ha. "Data-Driven Position Estimation and Sensorless Control of PMSM Drive in Low-Speed Region". *IEEE Transactions on Industry Applications, vol. 62, no. 1, pp. 1103-1116, Jan.-Feb. 2026, doi: 10.1109/TIA.2025.3595132*.
- D. Yun, S. Choi and J. -I. Ha. "Flying Capacitor Multi-Level Converter at Constant Resonant Frequency with Negative-Voltage-Blocking GaN Switch". *IEEE Journal of Emerging and Selected Topics in Power Electronics, vol. 13, no. 5, pp. 5492-5506, Oct. 2025, doi: 10.1109/JESTPE.2025.3571425*.
- J. Lee, D. Lee and J. -I. Ha. "Control and Modulation Methods of Single-/Three-Phase PWM Converter for Suppressing Leakage Current". *IEEE Transactions on Power Electronics, vol. 40, no. 7, pp. 9137-9152, July 2025, doi: 10.1109/TPEL.2025.3546298*.
- Seo, J., Choi, S. & Ha, JI. Control strategy for three-phase converters under unbalanced grid conditions with closed-loop compensation. J. Power Electron. 25, 469–479 (2025). https://doi.org/10.1007/s43236-025-00996-5.

**2024**

- J. Shim, G. Cheol Lim, S. Lee and J. -I. Ha. "Fault Diagnosis for Electric Drives Using Averagely Pooled and Downsampled Data Fusion on Embedded Systems". *IEEE Journal of Emerging and Selected Topics in Power Electronics, vol. 13, no. 1, pp. 1224-1241, Feb. 2025, doi: 10.1109/JESTPE.2024.3515659, doi: 10.1109/JESTPE.2024.3515659*.
- J. Yang, G. C. Lim, C. Hwang and J. -I. Ha. "Two-Phase DC Charging Method for Improved Efficiency and Zero Torque in Motor-Integrated Charger". *IEEE Transactions on Industrial Electronics, vol. 72, no. 5, pp. 4535-4545, May 2025, doi: 10.1109/TIE.2024.3468730*.
- S. J. Lee, J. Choi, G. C. Lim, S. M. Kim, E. -K. Kim and J. -I. Ha. "Analysis and Mitigation of Bearing Current in Inverter-Fed IPMSMs Drive System". *IEEE Transactions on Industrial Electronics, vol. 72, no. 4, pp. 3503-3513, April 2025, doi: 10.1109/TIE.2024.3456435*.
- J. Lee, S. Choi and J. -I. Ha. "Design and Four-Degree-of-Freedom Modulation Method of Dual Active Bridge Converter". *IEEE Journal of Emerging and Selected Topics in Power Electronics, vol. 12, no. 5, pp. 4478-4493, Oct. 2024, doi: 10.1109/JESTPE.2024.3448290*.
- J. Lee, S. Choi and J. -I. Ha. "Design and Analysis of Resonant Network for Dual Active Bridge Converter". *IEEE Journal of Emerging and Selected Topics in Power Electronics, vol. 12, no. 4, pp. 3784-3799, Aug. 2024, doi: 10.1109/JESTPE.2024.3406953*.
- J. Shim, J. Seo, S. Lee, T. Joung, H. Kwak and J. -I. Ha. "Ensemble-Based Anomaly Detection With Comprehensive Feature Distances for Induction Motors". *IEEE Transactions on Industry Applications, vol. 60, no. 4, pp. 6033-6044, July-Aug. 2024, doi: 10.1109/TIA.2024.3384356*.
- S. Choi, E. Chung, G. C. Lim, J. -S. Hong, G. -Y. Choe and J. -I. Ha. "Single-Sided Compensation Network Design Method for Capacitive Power Transfer System Considering Coupling Variation". *IEEE Transactions on Industry Applications, vol. 60, no. 4, pp. 6351-6365, July-Aug. 2024, doi: 10.1109/TIA.2024.3384346*.
- B. R. Park, G. C. Lim, Y. Han and J. -I. Ha. "Six-Vertex Voltage Injection Strategy for Sensorless IPMSM Control Using Single DC-Link Current Sensor". *IEEE Transactions on Industrial Electronics, doi: 10.1109/TIE.2024.3368166*.
- J. Shim, S. Lee, D. Jeon and J. -I. Ha. "Contact Force Estimation Using Uncertain Torque Model and Friction Models for Robot Manipulator". *IEEE Transactions on Industrial Electronics, vol. 71, no. 10, pp. 12634-12644, Oct. 2024, doi: 10.1109/TIE.2024.3352145*.
- C. Hwang, G. C. Lim, S. Lee, J. -J. Moon, K. -S. Park and J. -I. Ha. "Synchronous Overmodulation With Less Switchings Including Six-Step Operation". *IEEE Transactions on Industrial Electronics, vol. 71, no. 10, pp. 11967-11977, Oct. 2024, doi: 10.1109/TIE.2023.3347852*.

**2023**

- H. -g. Choi, J. -I. Ha and K. Lee. "Ultra-Low Inductance PMSM Drive Using a DC Current Sensor". *IEEE Transactions on Industrial Electronics, vol. 71, no. 6, pp. 5597-5607, June 2024, doi: 10.1109/TIE.2023.3288203*.
- J. -S. Hong, S. Choi and J. -I. Ha. "Modulation Method of Series-Resonant Dual-Active Half-Bridge Converter for ZVS and Minimum RMS Current". *IEEE Transactions on Industry Applications, vol. 60, no. 1, pp. 694-708, Jan.-Feb. 2024, doi: 10.1109/TIA.2023.3324316*.
- E. Chung and J. -I. Ha. "Impedance Matching Network Design for 6.78-MHz Wireless Power Transfer System With Constant Power Characteristics Against Misalignment". *IEEE Transactions on Power Electronics, vol. 39, no. 1, pp. 1788-1801, Jan. 2024, doi: 10.1109/TPEL.2023.3320199*.
- S. Lee, J. -S. Hong, J. Shim, M. Kim and J. -I. Ha. "Magnetic Field Synthesis of Electromagnetic Navigation Systems in Current Limits". *IEEE Transactions on Industrial Electronics, vol. 71, no. 7, pp. 7477-7487, July 2024, doi: 10.1109/TIE.2023.3306399*.
- J. -S. Hong, J. -I. Ha, S. Cui and J. Hu. "Topology and Control of an Enhanced Dual-Active Bridge Converter With Inherent Bipolar Operation Capability for LVDC Distribution Systems". *IEEE Transactions on Power Electronics, vol. 38, no. 10, pp. 12774-12789, Oct. 2023, doi: 10.1109/TPEL.2023.3297389. (Corresponding Author)*.
- B. R. Park, G. C. Lim, Y. Han and J. -I. Ha. "Saliency-Based Sensorless Control Using Current Derivative in IPMSM Drives With Single DC-Link Current Sensor". *IEEE Transactions on Industrial Electronics, vol. 71, no. 4, pp. 3394-3404, April 2024, doi: 10.1109/TIE.2023.3274858*.
- H. Kwon, J. Lee, J. Lee and J. -I. Ha. "Analytical Modeling and Design of 27.12 MHz Single-Switch DC–DC Converter With PCB Transformer". *IEEE Access, vol. 11, pp. 12742-12754, 2023, doi: 10.1109/ACCESS.2023.3242010*.

**2022**

- J. Choi, G. C. Lim, C. Hwang, B. R. Park and J. -I. Ha. "Feedback Gain Design of Induction Machine Full-Order Flux Observer". *IEEE Transactions on Industrial Electronics, vol. 70, no. 10, pp. 9870-9881, Oct. 2023, doi: 10.1109/TIE.2022.3217605*.
- J. Lee, G. C. Lim and J. -I. Ha. "Pulse Width Modulation Methods for Minimizing Commutation Torque Ripples in Low Inductance Brushless DC Motor Drives". *IEEE Transactions on Industrial Electronics, vol. 70, no. 5, pp. 4537-4547, May 2023, doi: 10.1109/TIE.2022.3189104*.
- S. Lee, G. Noh and J. -I. Ha. "Reconfigurable Power Circuits to Series or Parallel for Energy-Balanced Multicell Battery Pack". *IEEE Transactions on Industrial Electronics, vol. 70, no. 4, pp. 3641-3651, April 2023, doi: 10.1109/TIE.2022.3181412*.

**2021**

- J. -S. Hong, S. Lee and J. -I. Ha. "Control Method in Minimum Infinity-Norm Approach for Multicoil Magnetic Manipulation System". *IEEE Transactions on Magnetics, vol. 58, no. 1, pp. 1-9, Jan. 2022, Art no. 5600209, doi: 10.1109/TMAG.2021.3123093*.
- H. Chen, K. Sun, H. Shi, J. -I. Ha and S. Lee. "A Battery Charging Method With Natural Synchronous Rectification Features for Full-Bridge CLLC Converters". *IEEE Transactions on Power Electronics, vol. 37, no. 2, pp. 2139-2151, Feb. 2022, doi: 10.1109/TPEL.2021.3108622*.
- E. Chung, J. -I. Ha, A. A. Bastami and D. J. Perreault. "Impedance Compressing Matching Network Based on Two-Port Network Analysis for Wireless Power Transfer System". *IEEE Journal of Emerging and Selected Topics in Industrial Electronics, vol. 3, no. 3, pp. 432-442, July 2022, doi: 10.1109/JESTIE.2021.3103679*.
- G. Noh, J. Lee and J. -I. Ha. "Design and Analysis of Single-Inductor Power Converter for Both Battery Balancing and Voltage Regulation". *IEEE Transactions on Industrial Electronics, vol. 69, no. 3, pp. 2874-2884, March 2022, doi: 10.1109/TIE.2021.3065606*.
- H. -G. Choi, K. Lee and J. -I. Ha. "Design and Control Method for Interior Permanent Magnet Synchronous Machine Drive With Capacitor Power Network". *IEEE Journal of Emerging and Selected Topics in Power Electronics, vol. 9, no. 1, pp. 259-273, Feb. 2021, doi: 10.1109/JESTPE.2019.2958693*.
- Sunghyuk Choi, Jin-Su Hong and Jung-Ik Ha. (2021). Phase Control of Capacitive-Coupled Dual Active Bridge DC-DC Converters through Voltage Barrier Sensing. The Transactions of the Korean Institute of Power Electronics, 31-33 (국내).

## 국제 학회 발표 (2021–2026)

International Conferences 페이지의 2021–2026년 구역 60편(2026년 8, 2025년 12, 2024년 12, 2023년 8, 2022년 10, 2021년 10)이다. 저자·제목·학회 이름과 개최지, 쪽, DOI는 누리집 표기 그대로다.[^pubs]

**2026**

- H. Kato, J. -i. Itoh, G. -C. Lim and J. -I. Ha. "Model-based Spatial Harmonic Compensation in Signal-Injection Sensorless Control of IPMSMs". *2026 International Power Electronics Conference (IPEC-Nagasaki 2026 - ECCE Asia), Nagasaki, Japan, 2026, pp. 1-6, doi: 10.23919/IPEC-Nagasaki2026-EC64663.2026.11597389*.
- W. H. Jeong, G. C. Lim, M. Kim and J. -I. Ha. "Charge Pump Circuits for Negative Voltage Turn-Off in Gate Drivers". *2026 International Power Electronics Conference (IPEC-Nagasaki 2026 - ECCE Asia), Nagasaki, Japan, 2026, pp. 1-6, doi: 10.23919/IPEC-Nagasaki2026-EC64663.2026.11597238*.
- J. Shin, J. -I. Ha and J. -W. Shin. "Single Input Multi Output Converter Design by Three-Port Network Analysis". *2026 International Power Electronics Conference (IPEC-Nagasaki 2026 - ECCE Asia), Nagasaki, Japan, 2026, pp. 1-4, doi: 10.23919/IPEC-Nagasaki2026-EC64663.2026.11596959*.
- J. Jung, S. Choi, J. Lee, W. H. Jeong, M. Seo and J. -I. Ha. "Interoperable Control Method of Three-Phase and Single-Phase Wireless Power Transfer Systems". *2026 International Power Electronics Conference (IPEC-Nagasaki 2026 - ECCE Asia), Nagasaki, Japan, 2026, pp. 1-6, doi: 10.23919/IPEC-Nagasaki2026-EC64663.2026.11597401*.
- S. J. Lee, G. C. Lim, M. Kim and J. -I. Ha. "Suppression of Cross-Coupling Effects on Current Control in Wound Field Synchoronous Motor Drives". *2026 IEEE Applied Power Electronics Conference and Exposition (APEC), San Antonio, TX, USA, 2026, pp. 2322-2327, doi: 10.1109/APEC51134.2026.11517054*.
- C. Hwang, S. Lee and J. -I. Ha. "Low DC-link Voltage Operation of Three-Phase Bidirectional AC-DC Converter with Fixed Voltage Modulation Index". *2026 IEEE Applied Power Electronics Conference and Exposition (APEC), San Antonio, TX, USA, 2026, pp. 1969-1974, doi: 10.1109/APEC51134.2026.11517113*.
- S. Choi, J. Jung and J. -I. Ha. "Reactive Power Analysis of EV Wireless Power Transfer Systems Using Magnetomotive Force and Magnetic Circuit". *2026 IEEE Applied Power Electronics Conference and Exposition (APEC), San Antonio, TX, USA, 2026, pp. 906-913, doi: 10.1109/APEC51134.2026.11516733*.
- N. Kang, J. Yang, G. C. Lim and J. -I. Ha. "Battery Preheating Strategy for Electric Vehicles Utilizing Motor Drive System with Maximum Power Loss Point Tracking". *2026 IEEE Applied Power Electronics Conference and Exposition (APEC), San Antonio, TX, USA, 2026, pp. 3059-3064, doi: 10.1109/APEC51134.2026.11516678*.

**2025**

- G. C. Lim, J. Yang, C. Hwang, K. Lee and J. -I. Ha. "Decoupling Current Control for Open-End Winding Motors". *2025 28th International Conference on Electrical Machines and Systems (ICEMS), Busan, Korea, Republic of, 2025, pp. 3807-3811, doi: 10.23919/ICEMS66262.2025.11317264*.
- J. Yang, G. C. Lim and J. -I. Ha. "Hybrid Voltage Modulation for Zero-Sequence Current Suppression in Open-End Winding Motors". *2025 28th International Conference on Electrical Machines and Systems (ICEMS), Busan, Korea, Republic of, 2025, pp. 3801-3806, doi: 10.23919/ICEMS66262.2025.11316985*.
- J. Lee, D. Lee and J. -I. Ha. "Unified Modulation Strategy for Leakage Current Suppression in Three-Phase Transformerless Grid-Connected Converter". *2025 IEEE Energy Conversion Conference Congress and Exposition (ECCE), Philadelphia, PA, USA, 2025, pp. 1-8, doi: 10.1109/ECCE58356.2025.11260223*.
- M. Kim, B. R. Park and J. -I. Ha. "Switching-Frequency Voltage Injection Method for Low-Speed Sensorless Control Using Three-Shunt Current Sensors in IPMSM Drives". *2025 IEEE Energy Conversion Conference Congress and Exposition (ECCE), Philadelphia, PA, USA, 2025, pp. 1-7, doi: 10.1109/ECCE58356.2025.11260394*.
- S. Lee, B. R. Park and J. -I. Ha. "Injection Sequence Design for Mitigating High-Frequency Current in Low-Speed Sensorless Control Using Single DC-Link Current Sensor". *2025 IEEE 12th International Symposium on Sensorless Control for Electrical Drives (SLED), Harbin, China, 2025, pp. 1-6, doi: 10.1109/SLED63792.2025.11154661*.
- B. R. Park, G. Cheol Lim, M. Kim, S. Lee and J. -I. Ha. "High Frequency Voltage Injection Method for Sensorless Control Using Single DC-Link Current Sensor in IPMSM Drives". *2025 IEEE 12th International Symposium on Sensorless Control for Electrical Drives (SLED), Harbin, China, 2025, pp. 1-6, doi: 10.1109/SLED63792.2025.11154723*.
- M. Kim, B. R. Park and J. -I. Ha. "Minimum Voltage Injection for Sensorless Control of IPMSMs using Three-Shunt Current Sensors". *2025 IEEE 12th International Symposium on Sensorless Control for Electrical Drives (SLED), Harbin, China, 2025, pp. 1-6, doi: 10.1109/SLED63792.2025.11154739*.
- S. J. Lee, J. Shim and J. -I. Ha. "Temperature Estimation Based on Parameter Identification in Electric Motor Drive Using a Single DC-Link Current Sensor". *2025 IEEE 12th International Symposium on Sensorless Control for Electrical Drives (SLED), Harbin, China, 2025, pp. 1-6, doi: 10.1109/SLED63792.2025.11154663*.
- G. C. Lim, W. H. Jeong, K. Lee and J. -I. Ha. "Cost-Effective Fault Diagnosis for Motor and Inverter Using Bootstrap Charging and Single DC Link Current Sensor". *2025 IEEE Applied Power Electronics Conference and Exposition (APEC), Atlanta, GA, USA, 2025, pp. 2937-2942, doi: 10.1109/APEC48143.2025.10977437*.
- S. Choi, D. Yun and J. -I. Ha. "Representation and Design Methodology for Generalized Switched-Capacitor Converter Topologies". *2025 IEEE Applied Power Electronics Conference and Exposition (APEC), Atlanta, GA, USA, 2025, pp. 2268-2275, doi: 10.1109/APEC48143.2025.10977276*.
- T. Lee, D. Yun, S. Choi and J. -I. Ha. "Modified N:1 Switched Capacitor Converter with Reduced Capacitor DC Bias Voltage for High Power Density". *2025 IEEE Applied Power Electronics Conference and Exposition (APEC), Atlanta, GA, USA, 2025, pp. 1659-1665, doi: 10.1109/APEC48143.2025.10977174*.
- D. Lee, J. Lee and J. -I. Ha. "DC-Link Voltage Reduction with Synergetic Common-Mode Voltage Control of Single-Phase Two-Stage Non-Isolated EV Chargers". *2025 IEEE Applied Power Electronics Conference and Exposition (APEC), Atlanta, GA, USA, 2025, pp. 457-463, doi: 10.1109/APEC48143.2025.10977561*.

**2024**

- S. J. Lee, J. Choi, G. C. Lim, S. Min Kim, E. K. Kim and J. -I. Ha. "Enhancing Bearing Reliability in Inverter-Fed IPMSMs Drive: Control Method for Low-Speed Operation". *2024 IEEE Energy Conversion Congress and Exposition (ECCE), Phoenix, AZ, USA, 2024, pp. 6503-6509, doi: 10.1109/ECCE55643.2024.10861531*.
- D. Yun, S. Choi and J. -I. Ha. "Resonant Flying Capacitor Multi-Level Converter with Rerouted Capacitor for High Power Density and Efficiency". *2024 IEEE Energy Conversion Congress and Exposition (ECCE), Phoenix, AZ, USA, 2024, pp. 3514-3518, doi: 10.1109/ECCE55643.2024.10861002*.
- J. Lee, D. Lee, S. Lee and J. -I. Ha. "Control and Modulation Method for Leakage Current Mitigation in Single-Phase Non-Isolated EV Charger". *2024 IEEE Energy Conversion Congress and Exposition (ECCE), Phoenix, AZ, USA, 2024, pp. 4683-4690, doi: 10.1109/ECCE55643.2024.10861271*.
- M. Kim, J. Shim, J. Lee, J. Shin and J. -I. Ha. "Unsupervised Anomaly Detection of Reciprocating Compressors using Auto-Encoder". *2024 IEEE Energy Conversion Congress and Exposition (ECCE), Phoenix, AZ, USA, 2024, pp. 5762-5767, doi: 10.1109/ECCE55643.2024.10861618*.
- B. R. Park, G. C. Lim, J. Shim and J. -I. Ha. "Switching Frequency Voltage Injection for Sensorless IPMSM Control Using Current Derivative Measurements". *2024 IEEE Energy Conversion Congress and Exposition (ECCE), Phoenix, AZ, USA, 2024, pp. 5938-5943, doi: 10.1109/ECCE55643.2024.10861366*.
- S. Choi, E. Chung, G. C. Lim, T. Joung and J. -I. Ha. "10 kW Small-Gap Wireless Power Transfer System with Asymmetric Pads for Electric Vehicles". *2024 IEEE Wireless Power Technology Conference and Expo (WPTCE), Kyoto, Japan, 2024, pp. 28-31, doi: 10.1109/WPTCE59894.2024.10557379*.
- M. Kim, J. Kim, J. Shin, J. Shim and J. -I. Ha. "Voltage Injection-Based Fault Diagnosis for Power Devices with Multi-Module Neural Networks". *2024 IEEE 10th International Power Electronics and Motion Control Conference (IPEMC2024-ECCE Asia), Chengdu, China, 2024, pp. 4660-4665, doi: 10.1109/IPEMC-ECCEAsia60879.2024.10567341*.
- J. Lee, D. Lee, S. Lee and J. -I. Ha. "Direct Leakage Current Control Method of Single-Phase Non-Isolated EV Charger". *2024 IEEE 10th International Power Electronics and Motion Control Conference (IPEMC2024-ECCE Asia), Chengdu, China, 2024, pp. 5053-5058, doi: 10.1109/IPEMC-ECCEAsia60879.2024.10567233*.
- J. Lee, S. Choi, E. Chung and J. -I. Ha. "Design Method of Impedance Transformation Network for Robust Resonant Power Converters with Wide Load Impedance Variation". *2024 IEEE Applied Power Electronics Conference and Exposition (APEC), Long Beach, CA, USA, 2024, pp. 101-106, doi: 10.1109/APEC48139.2024.10509146*.
- G. C. Lim, J. Yang, C. Hwang and J. -I. Ha. "Zero Sequence and Ground Current Analysis of Dual Source Open-End Winding PMSM Drive System". *2024 IEEE Applied Power Electronics Conference and Exposition (APEC), Long Beach, CA, USA, 2024, pp. 575-580, doi: 10.1109/APEC48139.2024.10509161*.
- J. Yang, G. C. Lim, C. Hwang and J. -I. Ha. "Two-Phase Interleaved DC Charging Method of Integrated Charger for Efficiency Enhancement". *2024 IEEE Applied Power Electronics Conference and Exposition (APEC), Long Beach, CA, USA, 2024, pp. 801-806, doi: 10.1109/APEC48139.2024.10509044*.
- C. Hwang, G. C. Lim, S. Lee, J. -J. Moon, K. -S. Park and J. -I. Ha. "Synchronous Overmodulation for Reduced Number of Switchings with Unit Voltage Gain Including Six-Step Operation". *2024 IEEE Applied Power Electronics Conference and Exposition (APEC), Long Beach, CA, USA, 2024, pp. 122-127, doi: 10.1109/APEC48139.2024.10509358*.

**2023**

- J. Shim, S. Lee, D. Jeon and J. -I. Ha. "Static Friction Torque Estimation for Robot Manipulators Using a Data-Driven Approach". *2023 IEEE International Symposium on Sensorless Control for Electrical Drives (SLED), Seoul, Korea, Republic of, 2023, pp. 1-5, doi: 10.1109/SLED57582.2023.10261391*.
- J. Shim, J. Choi, S. Lee and J. -I. Ha. "Multi-Channel Neural Networks-Based Thermal Monitoring of Electric Motor". *2023 IEEE International Symposium on Sensorless Control for Electrical Drives (SLED), Seoul, Korea, Republic of, 2023, pp. 1-6, doi: 10.1109/SLED57582.2023.10261386*.
- B. R. Park, G. C. Lim, Y. Han and J. -I. Ha. "Hexa-Active Vector Pulse Width Modulation in IPMSM Sensorless Drives Using Single DC-Link Current Sensor". *2023 IEEE International Symposium on Sensorless Control for Electrical Drives (SLED), Seoul, Korea, Republic of, 2023, pp. 1-7, doi: 10.1109/SLED57582.2023.10261368*.
- G. C. Lim, J. Lee, B. R. Park and J. -I. Ha. "Analysis of Pulse Width Modulation Methods for PMSM Sensorless Control Based on Current Derivative Measurement". *2023 IEEE International Symposium on Sensorless Control for Electrical Drives (SLED), Seoul, Korea, Republic of, 2023, pp. 1-5, doi: 10.1109/SLED57582.2023.10261383*.
- G. -H. Min, H. Kwon, J. Lee and J. -I. Ha. "Virtually Isolated Class E Converter with Coupled Capacitors". *2023 IEEE Applied Power Electronics Conference and Exposition (APEC), Orlando, FL, USA, 2023, pp. 2124-2128, doi: 10.1109/APEC43580.2023.10131604*.
- J. Lee, B. R. Park, G. C. Lim and J. -I. Ha. "Hybrid Pulse Width Modulation with Current Derivative Measurement for PMSM Sensorless Control". *2023 IEEE Applied Power Electronics Conference and Exposition (APEC), Orlando, FL, USA, 2023, pp. 1090-1096, doi: 10.1109/APEC43580.2023.10131520*.
- B. R. Park, G. C. Lim, Y. Han, J. Lee and J. -I. Ha. "Saliency-Based Sensorless IPMSM Drives Using Derivatives of Phase Currents With Single DC-Link Current Sensor". *2023 IEEE Applied Power Electronics Conference and Exposition (APEC), Orlando, FL, USA, 2023, pp. 1402-1408, doi: 10.1109/APEC43580.2023.10131390*.
- H. Lee, J. Lee and J. -I. Ha. "Chattering Suppression of Sliding Mode Observer in Load Torque Estimation". *2023 IEEE Applied Power Electronics Conference and Exposition (APEC), Orlando, FL, USA, 2023, pp. 678-685, doi: 10.1109/APEC43580.2023.10131276*.

**2022**

- J. Lee and J. -I. Ha. "Active Reactance Control for Output Voltage Regulation in Wireless Power Transfer". *2022 IEEE Energy Conversion Congress and Exposition (ECCE), Detroit, MI, USA, 2022, pp. 1-5, doi: 10.1109/ECCE50734.2022.9948184*.
- J. Seo, Y. Lee and J. -I. Ha. "Diode Current Reduction Method of Three-Phase Boost PFC Converter with Semi-Bridgeless PFC Diode". *2022 IEEE Energy Conversion Congress and Exposition (ECCE), Detroit, MI, USA, 2022, pp. 1-5, https://ieeexplore.ieee.org/document/9948185doi: 10.1109/ECCE50734.2022.9948185*.
- S. Lee, C. Hwang, J. Shim and J. Ha. "A Control Method of Servo Motor Drives for Fast Dynamic Response and Low Torque Ripple". *2022 IEEE Energy Conversion Congress and Exposition (ECCE), Detroit, MI, USA, 2022, pp. 01-05, doi: 10.1109/ECCE50734.2022.9947638*.
- S. Choi, G. C. Lim, J. -S. Hong, E. Chung, G. Choe and J. -I. Ha. "Compensation Network Design Method for Capacitive Power Transfer System Considering Coupling Variation". *2022 IEEE Energy Conversion Congress and Exposition (ECCE), Detroit, MI, USA, 2022, pp. 1-6, doi: 10.1109/ECCE50734.2022.9947582*.
- J. Shim, B. R. Park, S. Choi and J. -I. Ha. "Learning-based Position Sensorless Control in Low-speed Region for SMPMSM". *2022 IEEE Energy Conversion Congress and Exposition (ECCE), Detroit, MI, USA, 2022, pp. 1-5, doi: 10.1109/ECCE50734.2022.9947561*.
- J. Shim, T. Joung, S. Lee and J. -I. Ha. "Audio Data-driven Anomaly Detection for Induction Motor Based on Generative Adversarial Networks". *2022 IEEE Energy Conversion Congress and Exposition (ECCE), Detroit, MI, USA, 2022, pp. 1-5, doi: 10.1109/ECCE50734.2022.9947652*.
- C. Hwang, G. C. Lim, J. Choi and J. -I. Ha. "Voltage Modulation Method for T-type Three-Level Inverter with Reduced Conduction Loss in Low Voltage Modulation Region". *2022 International Power Electronics Conference (IPEC-Himeji 2022- ECCE Asia), Himeji, Japan, 2022, pp. 945-951, doi: 10.23919/IPEC-Himeji2022-ECCE53331.2022.9806877*.
- J. -S. Hong, S. Choi and J. -I. Ha. "A Modulation Method of Series-Resonant Dual-Active Half-Bridge Converter for ZVS and Minimum RMS current". *2022 International Power Electronics Conference (IPEC-Himeji 2022- ECCE Asia), Himeji, Japan, 2022, pp. 1028-1035, doi: 10.23919/IPEC-Himeji2022-ECCE53331.2022.9807261*.
- J. Shim, G. C. Lim and J. -I. Ha. "Unsupervised Anomaly Detection for Electric Drives Based on Variational Auto-Encoder". *2022 IEEE Applied Power Electronics Conference and Exposition (APEC), Houston, TX, USA, 2022, pp. 1703-1708, doi: 10.1109/APEC43599.2022.9773565*.
- J. Lee, G. C. Lim and J. -I. Ha. "One-Digital-Sampling Commutation Method for Low Inductance Brushless DC Motor". *2022 IEEE Applied Power Electronics Conference and Exposition (APEC), Houston, TX, USA, 2022, pp. 01-07, doi: 10.1109/APEC43599.2022.9773603*.

**2021**

- S. Choi, J. -S. Hong and J. -I. Ha. "Phase Control using Network Node Voltage Feedback for Capacitor-Coupled Dual Active Bridge DC-DC Converters". *2021 IEEE Energy Conversion Congress and Exposition (ECCE), Vancouver, BC, Canada, 2021, pp. 3033-3038, doi: 10.1109/ECCE47101.2021.9595864*.
- J. Lee and J. -I. Ha. "Design and analysis of resonant inverter for a wide range of input voltage". *2021 IEEE Energy Conversion Congress and Exposition (ECCE), Vancouver, BC, Canada, 2021, pp. 2336-2342, doi: 10.1109/ECCE47101.2021.9595476*.
- G. Noh, G. C. Lim and J. -I. Ha. "Analysis of Synchronous-Rectification Switch Control for Active Class-E Rectifier". *2021 IEEE Energy Conversion Congress and Exposition (ECCE), Vancouver, BC, Canada, 2021, pp. 2059-2066, doi: 10.1109/ECCE47101.2021.9595063*.
- B. R. Park, G. C. Lim, J. Choi, C. Hwang and J. -I. Ha. "Torque Ripple Minimization of PMSM Drive with Speed Ripple Feedback Considering Non-linearities of PMSM". *2021 IEEE Energy Conversion Congress and Exposition (ECCE), Vancouver, BC, Canada, 2021, pp. 4948-4954, doi: 10.1109/ECCE47101.2021.9595926*.
- J. -h. Shim, J. Lee and J. -I. Ha. "Current-Sensor and Switch-Open Fault Diagnosis Based on Discriminative Machine Learning Model for PMSM Driving System". *2021 IEEE Energy Conversion Congress and Exposition (ECCE), Vancouver, BC, Canada, 2021, pp. 5098-5104, doi: 10.1109/ECCE47101.2021.9595123*.
- G. C. Lim, G. Noh and J. -I. Ha. "Analysis and Control of Synchronous Rectification for MHz Class-E Resonant Rectifier with Load Variation". *2021 IEEE Energy Conversion Congress and Exposition (ECCE), Vancouver, BC, Canada, 2021, pp. 3275-3281, doi: 10.1109/ECCE47101.2021.9595602*.
- G. C. Lim, G. Noh, J. Choi, J. -H. Shim, H. -G. Choi and J. -I. Ha. "Two-Phase Commutation Control Method of Open-End Winding PMSM with Reduced Loss for Low Torque Operation". *2021 IEEE Applied Power Electronics Conference and Exposition (APEC), Phoenix, AZ, USA, 2021, pp. 2147-2153, doi: 10.1109/APEC42165.2021.9487257*.
- S. Lee, G. Noh and J. -I. Ha. "Reconfigurable Multi-cell Battery Pack for Portable Electronic Devices with the Capability of Simultaneous Charging and Discharging". *2021 IEEE Applied Power Electronics Conference and Exposition (APEC), Phoenix, AZ, USA, 2021, pp. 2818-2824, doi: 10.1109/APEC42165.2021.9487069*.
- J. -H. Shim, K. Lee and J. -I. Ha. "Fault Diagnosis of Inverter Current Sensor Using Artificial Neural Network Considering Out-of-distribution". *2021 IEEE 12th Energy Conversion Congress & Exposition - Asia (ECCE-Asia), Singapore, Singapore, 2021, pp. 1520-1525, doi: 10.1109/ECCE-Asia49820.2021.9479085*.
- S. Lee, G. Noh and J. -I. Ha. "Efficient and Reconfigurable Multi-cell Battery Pack for Portable Electronic Devices with Simultaneous Charging and Discharging Capability". *2021 IEEE 12th Energy Conversion Congress & Exposition - Asia (ECCE-Asia), Singapore, Singapore, 2021, pp. 1021-1026, doi: 10.1109/ECCE-Asia49820.2021.9479094*.

## 과제

누리집 Research 메뉴 Projects 페이지(Research Projects)의 13건이다. 줄 앞의 연도는 누리집이 나눈 연도 구역(2024년 3건, 2023년 6건, 2022년 4건)이고, 과제 이름·기간·지원 기관(Sponsored by)은 누리집 표기 그대로다. 2022년 구역의 Gan-based 13.56 MHz, 1 kW Parallel Combined RF Power Amplifier는 기간과 지원 기관을, 2023년 구역의 Data-Driven Sensorless Control of PMSM은 지원 기관을 적지 않는다.[^projects]

- 2024년 구역 · Control and Modulation Method of Non-Isolated EV Charger for Human Safety and Electromagnetic Compatibility (기간 2024.04 ~; 지원 NRF (National Research Foundation of Korea))
- 2024년 구역 · Development of Non-Intrusive Power Measurement System for Inverter in Electric Vehicle (기간 2024.01 ~ 2024.12; 지원 Hyundai Motor Group)
- 2024년 구역 · Open-End Winding (OEW) PMSM Drive System (기간 2020.01 ~; 지원 Hyundai Motor Group)
- 2023년 구역 · Devloping Motor Failure Diagnosis and Calssification Technology (기간 2023.07 ~ 2024.07; 지원 LG Electronics)
- 2023년 구역 · Data-Driven Sensorless Control of PMSM (기간 2023.06 ~ 2024.06)
- 2023년 구역 · Low-Speed Sensorless Control with Single Shunt Inverter in Home Appliances (기간 2023.06 ~ 2024.06; 지원 Samsung Electronics)
- 2023년 구역 · Unsupervised Anomaly Detection of Reciprocating Compressors using Auto-Encoder (기간 2023.06 ~ 2024.06; 지원 Samsung Electronics)
- 2023년 구역 · Synchronous Overmodulation with Reduced Number of Switchings including Six-step Operation (기간 2023.01 ~ 2023.12; 지원 Hyundai TRANSYS)
- 2023년 구역 · 10 kW Small-Gap Wireless Power Transfer System with Asymmetric Pads for Electric Vehicles (기간 2023.01 ~ 2023.12; 지원 Hyundai Motor Group)
- 2022년 구역 · Gan-based 13.56 MHz, 1 kW Parallel Combined RF Power Amplifier
- 2022년 구역 · Design and 4 DOF Modulation Methods of Resonant Dual Active Bridge Converter (기간 2023.01 ~ 2023.12; 지원 Samsung Electronics)
- 2022년 구역 · Analysis and Mitigation of Bearing Current in Inverter-Fed IPMSMs Drive System (기간 2022.07 ~ 2023.08; 지원 Hyundai MOBIS)
- 2022년 구역 · Compensation Network Design Method for Capacitive Power Transfer System Considering Coupling Variation (기간 2022.01 ~ 2022.12; 지원 Hyundai Motor Group)

## 수상

누리집 News and Info 페이지의 수상 글 5건이다. 날짜는 글 머리의 @ 표기(행사 기간)이고, 날짜가 없는 JESTPE 논문상 글은 그 글이 연결한 학부 뉴스의 게시일(2026년 8월 7일)을 적었다. 상 이름, 학회·학술지, 수상자 이름과 과정, 논문 제목은 누리집 표기 그대로다.[^news][^ecenews]

- 2026.08.07 (학부 뉴스 게시일) · 2025 Second Place Prize Paper Award, IEEE Journal of Emerging and Selected Topics in Power Electronics (JESTPE) · Dam Yun (Ph.D. candidate, first author) · “Flying Capacitor Multilevel Converter at Constant Resonant Frequency with Negative-Voltage-Blocking GaN Switch”
- 2026.07.20~2026.07.23 · Best Poster Award, 27th IEEE Workshop on Control and Modeling for Power Electronics (COMPEL 2026, Cambridge, United Kingdom) · Ju-hyeong Ko (master’s student) · “A Highly Integrated 6:1 Switched-Capacitor Converter with Minimized Components and IC Pins for Mobile Applications”
- 2026.05.31~2026.06.04 · Outstanding Paper Award for Young Engineers, 2026 International Power Electronics Conference (IPEC-Nagasaki 2026 -ECCE ASIA-, Nagasaki, Japan) · Won-Hyo Jung (Ph.D. candidate) · “Charge Pump Circuits for Negative Voltage Turn-Off in Gate Drivers”
- 2025.09.24~2025.09.26 · Best Poster Award, 9th International Workshop on Power Supply on Chip (IEEE/PSMA PwrSoC 2025) · Dam Yun, Seong-Hyeok Choi · “Flying Capacitor Multi-Level Converter at Constant Resonant Frequency with Negative-Voltage-Blocking GaN Switch”
- 2025.08.15~2025.08.17 · Best Paper Award, 12th International Symposium on Sensorless Control for Electric Drives (IEEE SLED 2025) · Minha Kim, Byung Ryang Park · “Minimum Voltage Injection for Sensorless Control of IPMSMs using Three-Shunt Current Sensors”

## 소식

News and Info 페이지의 그 밖의 글 가운데 7건이다. 졸업생 교수 임용 3건, 교수 저서 출간 1건, IEEE PELS(IEEE Power Electronics Society) 행사 2건, 삼성전자-서울대 공대 생활 가전 기술 아이디어 공모전 안내 1건이다. 저서 출간 글과 공모전 안내 글에는 날짜가 없다. 제목은 누리집 표기 그대로다.[^news]

- 2026.09.01 · Dr. Sangwon Lee Appointed Professor at Hanyang University ERICA Campus
- 2026.03.01 · Dr. Jun-Hyeong Lee Appointed Professor at Kwangwoon University
- 2025.09.01 · Dr. Jaehoon Shim Appointed Professor at Myongji University
- 날짜 표기 없음 · Professor Ha's new book has been published (“Modern Resonant Converters”)
- 2024.06.20 · IEEE PELS Day Meeting Seoul Chapter 2024
- 2023.05.19~2023.05.20 · IEEE PELS Leaders Conference Korea 2023
- 날짜 표기 없음 · 삼성전자-서울대 공대 생활 가전 기술 아이디어 공모전

## 연락과 위치

- 주소: 08826 서울특별시 관악구 관악로 1 서울대학교 301동[^contact][^eceprof]
- 교수실: 누리집은 301동 606호(Bldg. 301, Room 606), 학부 교수 상세는 301동 508호로 적는다.[^prof][^contact][^eceprof]
- 전화: 070-4312-0428(누리집 Join EECL 페이지·학부 연구실 상세), 02-880-1760(학부 교수 상세·전임교수 목록)[^contact][^ecelabv][^eceprof][^ecefac]
- 교수 이메일: jungikha@snu.ac.kr[^prof][^contact]
[^p1]: G. C. Lim 외, J.-I. Ha, IEEE Transactions on Industrial Electronics 73, 9787-9799 (2026). <https://doi.org/10.1109/tie.2026.3663722> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J. Yang, G. C. Lim, C. Hwang, J.-I. Ha, IEEE Transactions on Industrial Electronics 72, 4535-4545 (2025). <https://doi.org/10.1109/tie.2024.3468730> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: S. Choi 외, J.-I. Ha, IEEE Transactions on Industry Applications 60, 6351-6365 (2024). <https://doi.org/10.1109/tia.2024.3384346> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: E. Chung, J.-I. Ha, IEEE Transactions on Power Electronics 39, 1788-1801 (2024). <https://doi.org/10.1109/tpel.2023.3320199> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: D. Yun, S. Choi, J.-I. Ha, IEEE Journal of Emerging and Selected Topics in Power Electronics 13, 5492-5506 (2025). <https://doi.org/10.1109/jestpe.2025.3571425> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: J. Lee, S. Choi, J.-I. Ha, IEEE Journal of Emerging and Selected Topics in Power Electronics 12, 4478-4493 (2024). <https://doi.org/10.1109/jestpe.2024.3448290> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: J. Shim, G. C. Lim, S. Lee, J.-I. Ha, IEEE Journal of Emerging and Selected Topics in Power Electronics 13, 1224-1241 (2025). <https://doi.org/10.1109/jestpe.2024.3515659> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: J. Shim, B. R. Park, M. Kim, J.-I. Ha, IEEE Transactions on Industry Applications 62, 1103-1116 (2026). <https://doi.org/10.1109/tia.2025.3595132> 초록 기준(Semantic Scholar 등록 초록).
[^home]: EECL 누리집 첫 화면 <https://eecl.snu.ac.kr/> (About EECL의 Welcome Message, Research Topics, Publications 칸, 2026-10-23 열람)
[^weare]: 누리집 We are 페이지 <https://eecl.snu.ac.kr/we-are> (Overview, Mission, 2026-10-23 열람)
[^prof]: 누리집 People 메뉴 Professor 페이지 <https://eecl.snu.ac.kr/people/professor> (About, Biography, The Educations, The Career, 수상·학회 활동 칸, E-mail, Office, 2026-10-23 열람)
[^phd]: 누리집 People 메뉴 Ph.D. Candidates 페이지 <https://eecl.snu.ac.kr/people/ph-d-candidates> (Post Doctoral Researcher, Ph.D. Candidates 칸, 2026-10-23 열람)
[^ms]: 누리집 People 메뉴 M.S. Candidates 페이지 <https://eecl.snu.ac.kr/people/m-s-candidates> (2026-10-23 열람)
[^alumni]: 누리집 People 메뉴 Alumni 페이지 <https://eecl.snu.ac.kr/people/alumni> (Visiting Scholars, Ph.D. Holders, Master's Degree Graduates, Undergraduates 칸, 2026-10-23 열람)
[^fields]: 누리집 Research 메뉴 Research Fields 페이지 <https://eecl.snu.ac.kr/research/research-fields> (Collaboration: Academic, Agency, Our Sponsors, 2026-10-23 열람)
[^projects]: 누리집 Research 메뉴 Projects 페이지 <https://eecl.snu.ac.kr/research/projects> (Research Projects, 2026-10-23 열람)
[^pubs]: 누리집 Achievements 메뉴: International Journals <https://eecl.snu.ac.kr/achievements/international-journals>, International Conferences <https://eecl.snu.ac.kr/achievements/international-conferences>, Domestic Journals <https://eecl.snu.ac.kr/achievements/domestic-journals> (목록 범위는 근거 페이지, 2026-10-23 열람)
[^news]: 누리집 We are 메뉴 News and Info 페이지 <https://eecl.snu.ac.kr/we-are/news-and-info> (2026-10-23 열람)
[^courses]: 누리집 Courses 페이지 <https://eecl.snu.ac.kr/courses> (Undergraduate Course, Graduate Course, 2026-10-23 열람)
[^contact]: 누리집 Join EECL 페이지 <https://eecl.snu.ac.kr/join-eecl> (Contact: E-Mail, Phone, Address, 2026-10-23 열람)
[^ecelab]: 서울대학교 전기·정보공학부 연구실 목록 <https://ece.snu.ac.kr/research-faculty/research/lab> (연구그룹별 연구실 이름과 교수, 2026-10-23 열람)
[^ecelabv]: 서울대학교 전기·정보공학부 연구실 상세(전기 에너지 변환 연구실) <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=122> (지도, 연구, TEL, 연구실 소개 및 연구분야, 최근 관심분야 및 주요 연구과제, 2026-10-23 열람)
[^ecefac]: 서울대학교 전기·정보공학부 전임교수 목록 <https://ece.snu.ac.kr/research-faculty/faculty/full-time> (하정익 항목의 직위·분야·전화·웹사이트, 2026-10-23 열람)
[^eceprof]: 서울대학교 전기·정보공학부 교수 상세(하정익) <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p072> (TEL, OFFICE, 학위, 전공, 분야, 학력, 주요경력, Research Interest, 2026-10-23 열람)
[^ecenews]: 서울대학교 전기·정보공학부 학부뉴스 「하정익 교수 연구팀 (윤담, 최성혁), IEEE JESTPE 우수 논문상 수상」 <https://ece.snu.ac.kr/ece/news?md=v&bbsidx=57959> (2026.08.07 게시, 2026-10-23 열람)

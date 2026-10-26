# 측정 로봇 및 진단 AI 연구실 (Measurement Robotics & Diagnostic AI Lab, MAI Lab)

**KAIST 항공우주공학과 · 이정률 교수**

- 분야: 레이저 초음파 전파 영상화 비파괴 검사(펄스-에코·투과·유도파 방식, 회전·로봇·이동형 검사), 구조 건전성 모니터링(PZT·광섬유 센서, 무선 초음파 장치), 스텔스·레이돔 구조의 전자기 성능 측정, 우주 환경 모사 시험, 진단 인공지능, 연속섬유 복합재 3D 프린팅, 파이로 충격 측정
- 대분야: 기계·로봇·제조, 전기전자·반도체·광학
- 태그: 3D 프린팅[^r3dp][^p5], 진동·소음 공학[^pyro], 과학·공학 AI[^overall][^p8], 우주 환경 시험·우주 소재 내구성[^space], 비파괴 검사·구조 건전성 모니터링[^overall], 복합재료[^r3dp]
- 홈페이지: <https://mailab.kaist.ac.kr/>
- 근거와 출처: [측정 로봇 및 진단 AI 연구실 근거 페이지](mailab-sources.md)

> 레이저·로봇·안테나·인공지능 기술로 실제 쓰이는 구조물의 상태를 재고, 부수지 않고 결함을 찾아내며, 성능을 측정하는 항공우주공학과 연구실이다.[^aelab] 레이저로 초음파를 만들어 구조물 속을 지나는 파동을 영상으로 보여 주는 검사 장치, 항공기 구조에 붙여 손상을 계속 살피는 무선 센서, 스텔스 구조의 전파 흡수 성능 측정, 위성 소재가 우주 환경에서 받는 영향을 땅 위에서 재현하는 시험 장치, 검사 자료를 자동으로 판독하는 진단 인공지능을 연구한다.[^overall]

## 무엇을 연구하나

연구실은 KAIST 항공우주공학과 이정률 교수의 연구실이다. 학과 연구실 소개는 연구실 이름을 「측정 로봇 및 진단 AI 연구실(Measurement Robotics & Diagnostic AI Lab, MAI)」로 적고, 로봇, 레이저, 안테나, 인공지능 등의 기술을 응용해 실제 사용되는 여러 구조의 센싱, 비파괴 검사, 성능 측정을 가능하게 하는 연구를 한다고 소개한다. 특히 레이저를 이용한 로보틱 비파괴 검사(Robotic nondestructive testing), 구조 건전성 모니터링(Structural Health Monitoring), 스텔스 기술(Stealth Technology), 3D 프린팅(Additive Manufacturing), 진단 인공지능(Diagnostic Artificial Intelligence)을 연구하고, 이 기술들을 스마트 격납고, 우주 발사체, 무인 항공기(UAM, UCAV), 풍력 터빈, 유무인 전투기 등에 적용한다고 적는다.[^aelab] 같은 소개는 보잉(Boeing), 삼성전자, 한국항공, 대한항공, 공군 항공기술연구소 등 국내외 산업체·연구기관과 협업한다고 적는다.[^aelab]

누리집 첫 화면은 연구실의 핵심을 여러 구조·소재 센싱 기술을 개발해 실제 현장에 적용하는 일로 소개한다. 광학, 전자공학, 메카트로닉스(기계와 전자·제어를 결합한 기술), 신호 처리와 인공지능을 아울러, 공학에서의 레이저와 광학, 통합 건전성 관리, 광섬유 센싱, 비접촉·무선 센싱, 첨단 비파괴 평가, 파이로 충격(폭발로 생기는 충격파) 측정과 모사, 스텔스·레이돔(레이더 안테나를 덮어 보호하는 덮개)을 위한 마이크로파 영상, 우주 환경 위협 측정 분야를 다룬다고 적는다.[^home] 학과 교수진 목록은 교수의 연구분야를 Smart Hangar(스마트 격납고), Diagnostic AI(진단 인공지능), Additive manufacturing(적층 제조), Sensor and robotics(센서와 로봇), Stealth composites(스텔스 복합재)로 적는다.[^aefac]

누리집 Research 메뉴는 연구를 Guided Wave UPI, Bulk Wave UPI, Robotic UPI, Integrated SHM, Shock & Vibration, Stealth Measurement Technology, Smart Hangar, Space Environment, UPI & RCS Rover, Reusable Launch Vehicle, 3D Printing Composites로 나눈다.[^overall] 여기서 UPI(Ultrasonic Propagation Imaging, 초음파 전파 영상화)는 레이저 등으로 초음파를 일으키고 재어, 초음파가 구조물 속을 퍼져 나가는 모습을 영상으로 보여 주는 검사 방식이다.[^overall][^guided] 2021–2026년 논문 목록에는 레이저 초음파 검사, 무선 초음파 장치를 쓴 구조 건전성 모니터링, 전파 흡수 구조의 설계·측정, 우주 환경 모사 시험, 위상 배열 초음파 검사와 비디오스코프 검사의 인공지능 판독을 다룬 논문과 학회 발표가 이어진다.[^ij][^dc]

## 주요 연구 주제

### 1. 레이저 초음파 전파 영상화 검사

Overall Introduction 페이지는 검사의 원리를 이렇게 적는다. 펄스 레이저가 고체 표면의 한 점을 순간적으로 데우면 초음파가 생기고, 이 초음파는 가열점에서 퍼져 나가 반대쪽 표면이나 같은 표면에서 측정된다. 반대쪽 표면에서 재면 투과 모드(through-transmission mode), 반사되어 같은 표면에서 재면 펄스-에코 모드(pulse-echo mode), 항공우주 구조의 얇은 껍질을 따라 멀리 진행한 뒤 재면 유도 모드(guided mode)라고 한다. 어느 방식이든 파동이 손상과 만나며 성질이 바뀌므로 내부 손상을 찾아낼 수 있다.[^overall] 같은 페이지는 이동식 펄스-에코 UPI 시스템을 생성 레이저와 감지 레이저를 쓰는 완전 비접촉 검사 장치로 소개하고, 층간 분리(delamination, 복합재 층 사이가 벌어지는 결함)처럼 두께 방향으로 생긴 결함을 검사한다고 적는다.[^overall]

Guided Wave UPI 페이지는 레이저로 초음파를 일으키고 PZT 센서(압전 소자로 만든 센서)로 받는 PZT-UPI 시스템을 펄스 반복률 최대 20 kHz, 측정 거리 100 m 초과(over 100 m)로, 레이저 도플러 진동계(레이저 빛의 주파수 변화로 표면 진동 속도를 재는 장치)로 받는 LDV-UPI 시스템을 완전 비접촉 방식으로 소개한다.[^guided] Bulk Wave UPI 페이지는 F-16 표준 시편을 펄스-에코 UPI로 현장 검사하는 연구를 적는다.[^bulk] 발사체 쪽으로는 발사체에 쓰는 Type-3 복합재 고압 용기를 회전하며 검사하는 회전형 투과·펄스-에코 레이저 초음파 영상화 시스템과, 하이브리드 로켓의 대형 복합재 고체 연료 연소실을 한 번 스캔에 폭 최대 2.0 m까지 검사하는 회전형 펄스-에코 시스템이 있다.[^overall] Reusable Launch Vehicle 페이지는 발사 환경에 노출된 탄소섬유 복합재(CFRP) 연소실의 바깥 변화와 내부 결함을 찾아 재사용 여부를 판단하는 검사 시스템을 개발하고 있다고 적는다.[^rlv] Smart Hangar 페이지는 스마트 격납고를 빠르고 먼 거리의 레이저 초음파 스캔, 여러 영역 동시 스캔, 대용량 자료의 빠른 신호 처리로 소개한다.[^hangar]

대표 논문 1은 Type-3 복합재 고압 용기를 회전 스캔 방식의 펄스-에코 레이저 초음파 검사로 평가할 수 있음을 보이고, 투과 모드 결과와 비교해 검증했다.[^p1]

### 2. 로봇과 이동 플랫폼을 이용한 검사

Robotic UPI 페이지에 따르면 로보틱 펄스-에코 레이저 초음파 검사 시스템은 곡률이 여러 가지인 복잡한 복합재 구조를 검사하도록, 검사 대상의 3차원 정보에서 검사 경로를 자동으로 만들고 결함을 찾는다. 가우스 곡률(곡면이 휜 정도를 나타내는 기하학 값)이 다른 면으로 경로 생성 알고리즘을 시험했고, 무인 항공기 조종면을 대상으로 연속섬유 3D 프린팅 과정에서 생긴 결함을 영상으로 보였다.[^robotic] Overall Introduction 페이지는 PUPI 기술을 이동 로버에 얹은 PUPI Rover를 소개하고, 대형 항공우주 부품과 복합재 구조, 접근이 제한된 산업 환경에서 파동 전파 영상화로 손상을 찾는 연구를 한다고 적는다.[^overall] UPI & RCS Rover 페이지는 이 로버가 SLAM(위치 추정과 지도 작성을 함께 하는 기술)으로 스스로 이동하며 레이저 초음파 검사와 인공지능 보조 진단을 한다고 적는다.[^rover]

대표 논문 2는 6자유도 로봇 팔로 검사 대상의 자세를 바꾸어 가며 연속섬유 3D 프린팅 복합재 구조물의 모든 면을 레이저 초음파로 검사하는 경로 계획 방법이다.[^p2]

### 3. 구조 건전성 모니터링

Overall Introduction 페이지는 항공기 구조 손상 진단·모니터링 시스템을 무선 초음파 장치(Wireless Ultrasonic Device, WUD)와 광섬유 브래그 격자(FBG) 센서를 결합한 하이브리드 구조 건전성 모니터링 시스템으로 소개한다. 이 시스템은 항공기 구조의 상태를 감시하고 외부 충격과 내부 손상을 실시간으로 찾는다.[^overall] WUD는 항공기 안에 설치되어 PZT 센서망과 무선 통신으로 구조 상태를 실시간 감시하며, 6채널 동시 측정, 무선 자료 전송, 40 g(70×70×15 mm)의 가벼운 설계를 특징으로 든다.[^overall] 동체에 PZT 센서 세 개를 직렬로 이은 단일 채널 센서망으로 떨어진 곳의 표면 균열을 찾고, 미리 학습한 UPI 자료로 충격 위치를 추정하는 연구도 있다.[^overall] Integrated SHM 페이지는 FBG 센싱으로 날개 처짐과 충격을 감시해 지상 조종사의 햅틱 인터페이스(촉감으로 정보를 전하는 장치)로 전달하는 스마트 무인기 연구를 적는다.[^ishm]

대표 논문 3은 센서와 자료 수집 장치 사이의 선을 없앤 무선 유도 초음파 전파 영상화 시스템이고,[^p3] 대표 논문 4는 초음파 감쇠와 균열 밀도의 관계로 수소 연료용 Type 4 복합재 고압 용기의 상태를 감시하는 방법이다.[^p4]

### 4. 스텔스 구조와 전자기 성능 측정

Stealth Measurement Technology 페이지에 따르면 연구실은 시편 전체의 스텔스 성능을 평가하는 주사형 자유 공간 측정 시스템(SFSM system)과 스텔스·레이돔 성능의 모사 해석을 연구한다. SFSM 시스템은 초점형 혼 안테나 두 개 사이에 시편을 놓고 2축 직선 이송 장치로 자동 래스터 스캔(가로줄을 차례로 훑는 스캔)을 하며, 측정한 주파수 범위의 결과를 시편 전체에 걸쳐 영상으로 보여 준다.[^stealth] Overall Introduction 페이지는 전용 시설 없이 이동 로봇이 대상 주위를 돌며 얻은 근거리 자료로 현장에서 레이더 반사 단면적(RCS, 물체가 레이더 전파를 되돌려 보내는 정도를 면적으로 나타낸 값)을 재는 기술, 무반향실에서 안테나 복사 패턴을 3차원으로 재는 시스템, 근거리 측정값을 원거리 값으로 바꾸는 변환(NFFFT), 높은 온도에서 시편의 전자기 성질을 재는 전기로, 곡면 시편을 재는 로봇 팔 기반 측정 시스템을 소개한다.[^overall] 넓은 주파수와 넓은 입사각에서 전자기파를 흡수하려면 3차원 격자 구조가 필요해, 복잡하고 반복되는 전파 흡수 구조를 3D 프린팅으로 설계·제작한다고도 적는다.[^overall]

대표 논문 5는 연속섬유 3D 프린팅으로 만든 다층 전파 흡수 구조의 유전율 변화를 보정하는 설계 방법이고,[^p5] 대표 논문 6은 6축 로봇 팔로 곡면 전파 흡수 구조를 움직이며 전자기 성능을 재는 측정 시스템이다.[^p6]

### 5. 우주 환경 모사 시험

Overall Introduction 페이지는 위성 소재와 전자 부품이 궤도에서 겪는 열 순환, 자외선, 진공, 원자 산소 환경을 함께, 그리고 가속해서 재현하는 TUVA 챔버, 극지방과 밴앨런대(지구 자기장에 붙잡힌 고에너지 입자 띠)를 지날 때의 고에너지 전자와 고진공 환경을 재현해 위성 전자 부품의 표면·내부 대전과 정전기 방전 특성을 평가하는 EV 챔버, 다섯 가지 우주 위협 요인을 동시에 재현하는 TUVEA 챔버를 소개한다.[^overall] 같은 페이지는 위성 궤도와 자세, 소재 성질을 입력하면 초저궤도(VLEO)부터 정지궤도(GEO)까지의 우주 위협 환경을 계산해 지상 시험 조건으로 바꾸는 우주 환경 프로파일링 소프트웨어(SEP)와, 상용 부품(COTS)인 대역 통과 필터를 초저궤도 환경에서 가속 시험해 원자 산소에 의한 표면 침식과 산화를 주된 열화 원인으로 밝히고 희생층 개념의 보호 코팅을 제안한 연구를 적는다.[^overall] Space Environment 페이지는 위성 외피에 쓰는 CFRP와 PCB에 쓰는 유리섬유 강화 플라스틱(GFRP)이 우주 환경에 노출되며 노화하는 현상을 연구하고, 가속 기법으로 고장에 이르는 노화의 가속 모델을 얻는 연구를 진행한다고 적는다.[^space]

대표 논문 7은 저궤도 복합 환경 모사 챔버와 정지궤도 대전 챔버를 갖춘 시설을 구축하고 상용 저항 소자, GFRP, PCB가 받는 영향을 정량적으로 비교했다.[^p7]

### 6. 진단 인공지능

Overall Introduction 페이지는 자동 구조 진단을 위해 개발한 통합 진단 인공지능 솔루션 「KAIST Structural Doctor」를 소개한다. 여러 자료 과학 진단 기능을 갖추어 얇은 기능성 복합재 구조와 두께 최대 약 30 mm의 금속 구조 검사를 지원하고, 검출 확률(PoD, 결함이 있을 때 검사가 그 결함을 찾아낼 확률)과 산업 표준 수립을 다룬다고 적는다.[^overall] 같은 페이지는 항공기 엔진 안 고압 압축기 블레이드의 손상을 비디오스코프(가는 관 끝의 카메라로 기계 내부를 촬영하는 장치) 영상에서 실시간으로 찾아 표시하는 인공지능 보조 검사 시스템(EVT)도 소개한다.[^overall]

대표 논문 8은 위상 배열 초음파 검사로 얻은 용접부 신호를 정상과 두 가지 결함으로 나누는 딥러닝 분류 방법이다.[^p8]

### 7. 연속섬유 복합재 3D 프린팅

3D Printing Composites 페이지에 따르면 연구실은 무인 항공기용 3D 프린팅 윙렛(날개 끝에 세운 작은 날개)과 CLAS(Conformal load-bearing antenna structure, 하중을 견디는 구조물에 안테나 기능을 넣은 구조)를 개발·평가한다. 연속섬유 복합재 3D 프린팅으로 복잡한 모양의 구조물을 빠르게 만들고, 윙렛과 푸셔 캡에 대해 열·구조 해석을 한 뒤 윙렛을 무인기에 달아 장착 가능성을 확인했다. 사각형 CLAS를 설계·제작해 무반향실에서 복사 패턴을 재고 해석 결과와 비교했으며, 로봇 팔 기반 측정 시스템으로 2차원·3차원 복사 패턴을 측정해 보여 준다.[^r3dp]

### 8. 파이로 충격 측정

Shock & Vibration 페이지에 따르면 파이로 충격은 로켓 단 분리처럼 폭발로 생긴 높은 주파수, 높은 세기의 응력파에 구조물이 응답하는 현상이다. 연구실의 파이로 충격 팀은 이 충격의 전파를 영상으로 보여 주는 레이저 파이로 충격 측정·전파 영상 장치를 개발한다. 이 장치는 폭발로 생긴 충격파를 최대 8채널까지 동시에 재는 비접촉 측정 시스템과, 레이저로 만든 충격파를 최대 16채널까지 동시에 재고 재구성 알고리즘으로 점·선 형태 폭발 충격의 전파를 모사하는 다점 동시 레이저 충격 감지 시스템으로 이루어진다.[^pyro]

## 대표 논문

이정률 교수가 저자인 2021–2026년 학술지 논문 가운데 초록을 확인할 수 있는 여덟 편을 다섯 연구 갈래(레이저 초음파 검사, 로봇 기반 검사, 구조 건전성 모니터링, 전파 흡수 구조와 스텔스 성능 측정, 우주 환경 시험과 진단 인공지능)에 나눠 골랐다. 누리집 목록과 출판사 서지에서 5번은 교수가 네 저자 가운데 셋째이고, 나머지 일곱 편은 교수가 마지막 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^ij] |
|---|---|---|---|---|
| 1 | 2025 | [Rotational laser ultrasonic propagation imager in pulse-echo mode for defect evaluation of type-3 COPV](https://doi.org/10.1177/14759217251326072) · Structural Health Monitoring | Type-3 복합재 고압 용기(COPV, 금속 내피 겉에 연속 탄소섬유 층을 감아 만든 압력 용기)는 가볍고 강해 항공우주 분야에서 연료 저장·운송과 고압 시스템에 널리 쓰인다. 섬유를 감는 제조 과정에서 결함이 생기기 쉬워 정밀한 비파괴 검사 기술이 필요하다. 이 논문은 레이저 초음파 검사에 회전 스캔 방식을 결합해 펄스-에코 모드로 검사할 수 있음을 보였다. 고출력 레이저를 결합한 펄스-에코 모드의 깊이 방향 결함 탐지 성능을 평가했고, 인공 결함을 넣은 Type-3 COPV를 검사해 투과 모드와 비교함으로써 적용 가능성과 실용성을 검증했다.[^p1] | 1저자 K.-J. Lee, 마지막 저자 이정률 (4명) |
| 2 | 2025 | [Path planning and inspection of complex-shaped 3D-printed composites based on robotic pulse-echo laser ultrasonic testing](https://doi.org/10.1080/09243046.2024.2372902) · Advanced Composite Materials | 항공 산업에서 복합재 부품 수요가 늘고, 복합재 3D 프린팅이 무인 항공기 2차 구조물의 제조 공정을 대신할 가능성이 생겼다. 이 기술을 쓰려면 프린팅 뒤에 적용할 자동 비파괴 검사가 필요하다. 이 연구는 연속섬유 3D 프린팅으로 만든 복잡한 모양의 구조물에 레이저 초음파 검사를 쓰는 방법을 제안했다. 6자유도 로봇 팔로 검사 대상의 위치를 제어하고, 좌표 변환과 쿼터니언(물체의 회전을 나타내는 수학적 표현)을 이용한 공간 회전으로 스캔 점과 경로를 계산해 대상의 모든 면을 검사했다. 감지 레이저가 표면에 수직으로 들어가고 대상과의 거리가 일정하게 유지되어 초음파 신호의 신호 대 잡음비가 높았고, 검사 결과 이 기법이 복잡한 모양의 3D 프린팅 구조물의 결함 탐지에 알맞음을 보였다.[^p2] | 1저자 K.-J. Lee, 마지막 저자 이정률 (2명) |
| 3 | 2024 | [Development of Wireless Ultrasonic Device for Wireless Guided-Wave Ultrasonic Propagation Imaging System](https://doi.org/10.1007/s42405-023-00691-4) · International Journal of Aeronautical and Space Sciences | 구조물을 완전히 무선으로 검사하는 무선 유도 초음파 전파 영상화(GUPI) 시스템을 제안했다. 기존 GUPI 시스템은 초음파를 일으키는 레이저, 레이저 미러 스캐너, 자료 수집 장치를 갖춘 컴퓨터, 대역 통과 필터, 센서로 이루어지는데, 센서를 자료 수집 장치에 선으로 연결해야 해서 현장 적용에 걸림돌이 되었다. 이 연구는 무선 초음파 장치(WUD)와 최댓값 검출 기반 무선 동기화 알고리즘을 개발해 시편과 검사 시스템 사이의 선을 없앴고, 복합재 날개 외피 시편으로 유선과 무선 GUPI의 측정 결과를 비교했다. 저자들은 무선 검사 기능이 GUPI 시스템을 항공기 구조 검사에 적용할 가능성을 높이고 항공기의 구조 안전을 높일 것이라고 적는다.[^p3] | 1저자 J. W. Park, 마지막 저자 이정률 (2명) |
| 4 | 2025 | [Structural health monitoring of type 4 composite fuel tank based on correlation between ultrasonic attenuation and crack density](https://doi.org/10.1080/09243046.2024.2398289) · Advanced Composite Materials | 수소전기차(FCEV)가 늘면서 수소 연료를 안전하게 저장하는 일이 중요해졌다. 수소는 플라스틱 내피에 복합재 섬유를 감아 만든 Type 4 고압 용기에 저장하는데, 충전과 방전을 되풀이하면 복합재 부분이 손상된다. 이 논문은 초음파 감쇠(초음파가 진행하며 세기가 줄어드는 정도)와 균열 밀도의 상관관계에 바탕을 둔 구조 건전성 모니터링 방법을 제안했다. 유압 반복 시험으로 손상을 재현하고 마이크로 CT 영상으로 실제 균열 밀도를 확인한 뒤, 유압 시험 반복 수를 매개변수로 초음파 감쇠와 균열 밀도를 한 식으로 묶었다. 연료 탱크에 붙인 PZT 능동 센서망으로 초음파 전파를 재면 Type 4 연료 탱크의 상태를 실시간으로 감시할 수 있다고 적는다.[^p4] | 1저자 K. Kim, 마지막 저자 이정률 (4명) |
| 5 | 2024 | [Design and verification of the square convex surface multilayer radar absorbing structure based on additive manufacturing](https://doi.org/10.1177/10996362241278222) · Journal of Sandwich Structures & Materials | 연속섬유 3D 프린팅으로, 비스듬히 들어오는 전자기파에 맞춘 사각 볼록 표면 다층 전파 흡수 구조(RAS)를 설계·제작했다. 3D 프린팅 구조물에서는 구조 모양에 따라 노즐 경로가 바뀌어 복소 유전율(물질이 전기장에 반응하는 정도와 그때의 에너지 손실을 함께 나타내는 값)이 달라진다. 이를 다루려고 「공정 유전율 보정 방법(Process Permittivity Correction Method)」을 개발해, 구조 모양과 정한 노즐 경로에 따라 달라지는 공정 유전율을 각 구조의 최적화 전에 설계에 반영했다. 60° 입사각에서 TE·TM 두 모드를 함께 고려해 최적화한 RAS는 해석한 흡수 성능과 측정한 흡수 성능의 경향이 높은 상관을 보였다. 저자들은 이 방법이 설계와 제작의 일관성을 지키면서 전자기 성질과 흡수 성능을 유지한다고 적는다.[^p5] | 1저자 D.-H. Jin, 셋째 저자 이정률, 마지막 저자 J.-M. Ahn (4명) |
| 6 | 2022 | [Robotic scanning free-space measurement system for electromagnetic performance evaluation of curved radar absorbing structures](https://doi.org/10.1177/17298806221114554) · International Journal of Advanced Robotic Systems | 전파 흡수 구조는 조립 전에 성능을 평가하는 전수 검사를 거친다. 이 연구는 주사형 자유 공간 측정 시스템에서 6축 로봇 팔로 시편을 움직이게 했다. 로봇 팔이 시편을 안테나 초점에 계속 두게 해, 2축·3축 주사형 장치에서 문제가 된 곡률이 반사 손실 결과에 미치는 영향을 해결했다. RobotStudio로 시편 위 각 측정점의 위치와 방향을 뽑고 로봇 스캔 알고리즘으로 측정점을 스캔 경로로 바꾼다. 주파수 선택 표면(특정 주파수의 전파만 통과시키거나 반사하도록 무늬를 새긴 면)을 단, 곡률이 변하는 시편과 일정한 시편으로 시스템을 검증했다. 3축 장치로는 정확히 평가하지 못한 비대칭 캠버 날개꼴 시편과 S자 이중 곡률 시편의 반사 손실(S11)을 측정했고, 모든 결과가 시편의 이론 값에 맞았다. S자 시편의 결과에는 곡률 보정을 적용해 음과 양의 곡률이 공진 주파수에 미치는 영향을 확인했다.[^p6] | 1저자 S. ud Din, 마지막 저자 이정률 (4명) |
| 7 | 2025 | [LEO Complex Space Environment Experiment Interpretation About COTS Resistor, GFRP, and PCB](https://doi.org/10.1007/s42405-025-00905-x) · International Journal of Aeronautical and Space Sciences | 저궤도(LEO) 복합 환경 모사 챔버와 정지궤도(GEO) 우주선 대전(우주선 표면이나 내부에 전하가 쌓이는 현상) 챔버를 갖춘 시설을 구축해 그 실현 가능성을 보이고, 이 시설로 수동 소자, 유리섬유 강화 고분자(GFRP), 인쇄회로기판(PCB)이 받는 영향을 분석했다. 실험 장치에서 모사할 수 있는 우주 환경 요인과 각 측정값을 실험 전후에 수치로 기록해 비교했다. 저항 소자 20개 가운데 11개가 몇 시간 안에 저항값이 허용 범위를 벗어나 쓸 수 없게 되었다. GFRP와 PCB의 질량 손실과 증기 질량 증가를 실험 전후로 비교했고, PCB 소재는 강도와 강성 같은 기계적 성질도 비교했다. 저자들은 이렇게 얻은 정량 값이 위성에 각 소재와 부품을 쓸 때 보호 구조나 기계 구조 설계의 기초 자료가 될 것으로 본다.[^p7] | 1저자 H.-J. Lee, 마지막 저자 이정률 (3명) |
| 8 | 2026 | [Weld Defect Classification in Phased-Array Ultrasonic Testing Using a CNN with FiLM Layer](https://doi.org/10.1007/s42405-026-01251-2) · International Journal of Aeronautical and Space Sciences | 위상 배열 초음파 검사(PAUT)는 항공우주를 비롯해 안전이 중요한 산업에서 용접부 검사에 널리 쓰이지만, A-스캔 신호를 자동으로 해석하는 일은 잡음, 용접 모양에서 생기는 반사, 결함 종류 사이의 자료 불균형 때문에 어렵다. 이 연구는 맞대기 용접부의 A-스캔을 정상, 선형 결함, 체적 결함으로 분류하는 딥러닝 틀을 제안했다. 분야 지식에 바탕을 둔 두 단계 전처리와, 미리 계산한 물리 특징으로 특징 지도를 조절하는 FiLM(feature-wise linear modulation) 층을 단 합성곱 신경망을 결합했다. 탄소강·스테인리스강 시편 40개로 검사 파일 단위의 10겹 교차 검증을 한 결과 평균 정확도 87.66%, 매크로 F1 81.02%였고, 전처리는 매크로 F1을 10.98%p, FiLM 층은 체적 결함 정확도를 8.01%p 높였다. 두 결함 종류를 합쳐 결함 유무만 가리면 정확도가 99.26%로, 현장 검사 결과를 빠르게 선별하기에 알맞은 수준이라고 적는다.[^p8] | 1저자 J. Lee, 마지막 저자 이정률 (3명) |

## 교수와 전문 분야

이정률 교수(Lee, Jung-Ryul)는 KAIST 항공우주공학과 교수이자 학과장이다. 학과 교수진 목록은 직위를 Professor, Department Head로, 학력을 B.S. Busan National Univ(1999), M.S. KAIST(2001), Ph.D. ENSMSE in France(2004)로, 연구분야를 Smart Hangar, Diagnostic AI, Additive manufacturing, Sensor and robotics, Stealth composites로 적는다.[^aefac] 누리집 교수 페이지는 Full Professor로 적고, Measurement Science and Technology의 Editorial Board Member·Asian-Pacific Regional Editor, Structural Health Monitoring-An International Journal의 Associate Editor, Advanced Composite Materials의 Editorial Board Member·EiC, ASME Journal of Nondestructive Evaluation, Diagnostics and Prognostics of Engineering Systems의 Associate Editor, 국토부 K-UAM 운영위원회 민간위원, 법원 전문심리위원, KAIST 항공우주공학과 학과장을 적는다.[^prof] Research 메뉴의 Overall Introduction 페이지는 이 밖에 KAIST Chaired Professor, Space Stealth Inc.의 Executive Director, 공군 정책자문위원을 적고, 성과로 국내외 학술지 논문 208편, 국내외 학회 논문 486편, 국제·미국·일본·한국 특허 41건을 든다.[^overall]

누리집 특허 목록의 앞쪽 항목은 일본·유럽·미국에 낸 FBG 초음파 센서, 광섬유 센서 누액 검출 장치, 음향 방출(AE, 재료가 손상될 때 내는 탄성파)·초음파 검출 시스템 특허이고, 이어서 한국에서 음향초음파 전파 영상화 장치, 기형 초음파 전파 영상화 장치, 풍력 터빈 블레이드 처짐 감시 시스템, 전영역 펄스-에코 레이저 초음파 전파 영상화 장치 특허를 냈다.[^patent] 이 목록과 2021–2026년 논문으로 보면 전문 분야는 레이저 초음파 전파 영상화를 중심으로 한 비파괴 평가와 구조 건전성 모니터링, 광섬유·압전 센서와 무선 센싱, 스텔스·레이돔 구조의 전자기 성능 평가, 우주 환경 시험, 검사 자료의 인공지능 진단이다.[^patent][^ij]

## 응용 분야

누리집 첫 화면은 응용 분야로 스마트 격납고, 우주 발사체, 인공위성, 전투기, 무인 항공기, 전자전, 풍력 터빈, 발전소, 철도 구조물, 공공 안전을 든다.[^home] 학과 연구실 소개는 스마트 격납고, 우주 발사체, 무인 항공기, 풍력 터빈, 유무인 전투기 등에 적용한다고 적는다.[^aelab] 연구 페이지들은 발사체의 Type-3 복합재 고압 용기와 하이브리드 로켓 고체 연료 연소실의 검사[^overall], 재사용 발사체 연소실의 재사용 판단[^rlv], 항공기 구조 손상 감시와 항공기 엔진 블레이드 검사[^overall], 위성 소재·전자 부품의 우주 환경 내구성 평가[^overall][^space]를 다룬다. 대표 논문 4는 수소전기차의 Type 4 수소 연료 용기를 대상으로 한다.[^p4]

## 구성원

누리집 Members 메뉴의 Professor 페이지에 교수와 함께 실린 연구부교수(Associate Research Professor) 2명, Doctoral Student 페이지 8명, Master Student 페이지 8명, Postdoc 페이지 3명, 모두 21명이다. Visiting Prof./Researcher 페이지에는 카드가 없다. 「시작」은 카드의 PERIOD 칸에 적힌 시작 연월이다. 이메일은 카드에 적힌 KAIST 주소만 실었다.[^prof][^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Chen Ciang CHIA | 연구부교수(Associate Research Professor) |  |  | 8 |
| HYE JIN SHIN (신혜진) | 연구부교수(Associate Research Professor) |  | shinh@kaist.ac.kr | 7 |
| MU SEUNG JEON (전무승) | 박사과정 | 2022.09 | msjeon94@kaist.ac.kr |  |
| DONG JIN PARK (박동진) | 박사과정 | 2022.09 | pdj1009@kaist.ac.kr | 5 |
| KYU JIN LEE (이규진) | 박사과정 | 2023.03 | pos2323@kaist.ac.kr | 1, 2 |
| KING SUM MA | 박사과정 | 2024.09 | ks.ma@kaist.ac.kr |  |
| YOUNG HOON JO (조영훈) | 박사과정 | 2025.09 | mmbv0987@kaist.ac.kr |  |
| SALAH UD DIN | 박사과정 | 2025.09 | u2014314@kaist.ac.kr | 6 |
| CHANG MIN LEE (이창민) | 박사과정 | 2026.03 | akflsvkdld@kaist.ac.kr |  |
| SA SEONG MOON (문사성) | 박사과정 | 2026.03 | moon4seong@kaist.ac.kr |  |
| JI HYUN KIM (김지현) | 석사과정 | 2025.03 | matilda0403@kaist.ac.kr |  |
| HYUN WOO LEE (이현우) | 석사과정 | 2025.03 | hwlee0108@kaist.ac.kr |  |
| HEE BEOM YUN (윤희범) | 석사과정 | 2025.03 | maxdavid@kaist.ac.kr |  |
| JUN WON LEE (이준원) | 석사과정 | 2025.03 | lee96368423@kaist.ac.kr |  |
| JAE HEON BAN (반재헌) | 석사과정 | 2025.09 | reptileban09@kaist.ac.kr |  |
| SUNG HUN YUN (윤성훈) | 석사과정 | 2026.03 | ahnong00@kaist.ac.kr |  |
| DONG MUK JOO (주동묵) | 석사과정 | 2026.09 | ehdanr1372@kaist.ac.kr |  |
| Krzysztof Jamrozy | 석사과정 | 2026.09 | kjamrozy20264784@kaist.ac.kr |  |
| KYUNG HWAN KIM (김경환) | 박사후연구원 | 2025.03 | fddcd@kaist.ac.kr | 4 |
| SHI YN LEE (이시인) | 박사후연구원 | 2025.09 | leeshiyn@kaist.ac.kr |  |
| JAEHO LEE(이재호) | 박사후연구원 | 2026.09 | barbossa0412@kaist.ac.kr | 4, 8 |

## 졸업생과 이전 구성원

누리집 Members 메뉴의 Alumni 페이지 카드 48명과 Intern 페이지 카드 27명이다. Alumni 카드의 「학위·과정 (연도)」는 POSITION IN LAB 칸의 과정과 괄호 안 연월이고, 진로는 CURRENT 칸 그대로다. 석사를 마치고 이 연구실 박사과정이나 박사후연구원으로 남은 사람도 Alumni 카드에 함께 실려 있다. Intern 카드는 인턴 기간과 당시 소속, 괄호 안 프로그램 표기(URP, Individual Research)를 적는다.[^alumni][^intern]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Dr. RAVI PANWAR | Postdoctoral fellow (Jun. 2016) | Assistant Professor, |
| DAE YUN BAE (배대윤) | Postmaster (Mar. 2016) | Korea Construction Equipment Technology Institute |
| MANISH MAN SHRESTHA | Postmaster (Feb. 2017) | PhD Course in |
| YONG WOON KIM (김용운) | Master (Aug. 2017) | Korea Aerospace Industries (KAI) |
| JAE YOON PARK (박재윤) | Master (Aug. 2017) | Researcher in Golfzon Company |
| AYALSEW DAGNEW ABETEW | Master (Aug. 2017) | Lecturer in |
| Dr. HYE JIN SHIN (신혜진) | Postdoctor (Jun. 2018) | Associate Research Professor in OERL |
| Dr. SYED HAIDER ABBAS | Doctor (Feb. 2019) | Assistant Professor in |
| BYUNGHAK JUNG (정병학) | Master (Feb. 2019) | Korea Aerospace Industries (KAI) |
| THANH THAI MAI | Master (Feb. 2019) | Assistant Professor in |
| Dr. YUNSHIL CHOI(최윤실) | PhD, Postdoc (Feb. 2019) | Korea Aerospace Industries (KAI) |
| Dr. JAEYEONG JANG(장재경) | Postdoctor (Mar. 2019) | Institute for Adavanced Engineering (IAE) |
| Dr. SEUNG-CHAN HONG (홍승찬) | PhD, Postdoc (Aug. 2019) | CEO, X-NDT Inc. |
| Dr. YOUNGJUN LEE (이영준) | Doctor (Aug. 2019) | Professor in Republic of Korea Air Force Academy |
| JOONHEE JOH (조준희) | Master (Aug. 2019) | LIVSMED Inc. |
| Dr. HASAN AHMED | Doctor (Feb. 2020) | ARM (Advanced RISC Machines) |
| JAEHO LEE(이재호) | MS, PhD (Aug. 2026) | Postdoc in MAI |
| ALI MOHSIN | Master (Aug. 2020) |  |
| JIHYUNG AN (안지형) | Master (Aug. 2020) | KIA Motors |
| SOOHYUN EOM (엄수현) | Master (Feb. 2021) | Korea Aerospace Industries (KAI) |
| Dr. DAESUNG SON (손대성) | Doctor (Aug. 2021) | LG Electronics |
| SALAH UD DIN | Master (Aug. 2021) |  |
| JUNMIN LEE (이준민) | Master (Aug. 2021) | PhD course in graduate school of AI |
| HIRA MAJEED | Master (Aug. 2021) |  |
| SANGYEON CHO (조상연) | Master (Feb. 2022) | SAMSUNG Elctronics |
| JINWOO PARK (박진우) | MS, PhD (Aug. 2022) | SAMSUNG Elctronics |
| MUSEUNG JEON (전무승) | Master (Aug. 2022) | PhD course in MAI |
| DONGJIN PARK (박동진) | Master (Aug. 2022) | PhD course in MAI |
| KYUJIN LEE (이규진) | Master (Feb. 2023) | PhD course in MAI |
| YOONKYU KIM (김윤규) | Master (Feb. 2023) | LG Energy Solution |
| MINJI IM (임민지) | Master (Aug. 2023) | Hanhwa Aerospace |
| Dr. JONGMIN HYUN (현종민) | MS, PhD, Postdoc (Feb. 2024) | Agency for Defense Development (ADD) |
| YONGHO KIM (김용호) | MS, PhD (Feb. 2024) | SAMSUNG Elctronics |
| HYEONGYU PARK (박현규) | Master (Feb. 2024) | ASML |
| KISEOK KIM (김기석) | Master (Feb. 2024) | Korea Aerospace Industries (KAI) |
| HANJUN LEE (이한준) | Master (Aug. 2024) | Korea Aerospace Research Institute(KARI) |
| KINGSUM MA | Master (Aug. 2024) | PhD course in MAI |
| KYUNGHWAN KIM (김경환) | MS, PhD (Feb. 2025) | Postdoc in MAI |
| TAEYOUNG KIM (김태영) | Master (Feb. 2025) | SAMSUNG Elctronics |
| JAEMIN YOU (유재민) | Master (Feb. 2025) | Korean Air |
| JEONGWAN HONG (홍정완) | Master (Feb. 2025) |  |
| DU HWAN KIM (김두환) | PhD (Aug. 2025) | MUJIN CO |
| DO HYEON JIN (진도현) | PhD (Aug. 2025) | Agency for Defense Development (ADD) |
| GYEONG MIN LEE (이경민) | Master (Feb. 2026) | LIG Defense&Aerospace |
| TOMASZ KORGUL | Master (Feb. 2026) |  |
| Włodzimierz Zalewski | Master (Feb. 2026) |  |
| CHANG MIN LEE (이창민) | Master (Feb. 2026) | PhD course in MAI |
| JEONG HOON PARK (박정훈) | Master (Aug. 2026) |  |
| KYLE EMBRY | Intern, University of Texas at Dallas (2015.05.17 ~ 2015.06.27) |  |
| KALEB R. KLEINE | Intern, Virginia Polytechnic Institute and State University (2015.05.17 ~ 2015.06.24) |  |
| AZIMIRA FRIDA | Intern, Universiti Putra Malaysia (2015.06.29 ~ 2015.09.14) |  |
| JAEKYEONG JANG | Intern, Chonbuk National University (2015.08 ~ 2017.02.22) |  |
| HAMID REZA ASEMANI | Intern, University of Teheran (2015.10.12 ~ 2016.06.30) |  |
| JINWOO PARK | Intern, KAIST (2015.12.20~2016.08.31) |  |
| JONGMIN HYUN | Intern, Busan National University (2016.01.11~2016.03.01) |  |
| KYUNG HWAN KIM | Intern, KAIST (2017.01.01 ~ 2017.02.28) |  |
| YUN JI WO | Intern, KAIST (2017.03.15 ~ 2017.08.25) |  |
| JOON HEE JOH | Intern (2017.03.02 ~ 2017.08.25) |  |
| ABI SYAMIL | Intern (URP), KAIST (2018.06.25 ~ 2018.12.14) |  |
| SEUL LEE | Intern (Individual Research), KAIST (2018.08.27 ~ 2018.12.14) |  |
| SEUL LEE | Intern (URP), KAIST (2018.08.27 ~ 2018.12.14) |  |
| ROBEL A. ASMAMAWU | Intern (Individual Research), KAIST (2019.01.02 ~ 2019.02.28) |  |
| BYUNG HO LEE | Intern (Individual Research), KAIST (2019.01.02 ~ 2019.02.28) |  |
| JUNMIN LEE | Intern (Individual Research), KAIST (2019.02.25 ~ 2019.06.14) |  |
| REEM SAEED SULIMAN | Intern, Khalifa University (2019.05.27 ~ 2019.07.18) |  |
| FATIMA SULAIMAN | Intern, Khalifa University (2019.05.27 ~ 2019.07.18) |  |
| Jimin Choi | Intern, KAIST (2020.07.13 ~ 2020.08.28) |  |
| DAEHAN LEE | Intern, KAIST (2020.12.28 ~ 2021.02.28) |  |
| DongWook Yang | Intern, KAIST (2021.06.24 ~ 2021.08.31) |  |
| Kamran Gasimov | Intern, KAIST (2021.12.20 ~ 2022.02.28) |  |
| Alexandra Suchshenko | Intern, KAIST (2021.12.20 ~ 2022.02.28) |  |
| Kamran Gasimov | Intern, KAIST (2022.06.24 ~ 2022.12.21) |  |
| Jin Hyeong Park | Intern, Chungnam National University (23.07.01-23.08.31) |  |
| Ji Hyun Kim | Intern, KAIST (24.09.02 ~ 25.02.23) |  |
| Bartosz Popiela | Intern, Bundesanstalt für Materialforschung und -prüfung (BAM) (24.10.21 ~ 24.11.08) |  |

## 최근 논문 목록 (2021–2026)

누리집 Publication 메뉴 다섯 페이지에서 2021–2026년에 해당하는 203편이다. 국제 학술지 페이지의 첫 번호 구획 131–170번 40편과 별도 번호 구획 13–18번 6편, 국제 학회 발표 19편, 국내 학술지 4편, 국내 학회 발표 133편, 책의 장 1편이다. 줄 끝 대괄호는 논문 종류와 누리집 번호이며, 국제 학술지 페이지의 별도 번호 구획 항목은 「별도 구획」으로 표시했다. 연도는 각 줄에 적힌 출판·발표 연도이며, 국제 학술지 170번은 누리집이 「Accepted, Sep. 2026」으로 적은 게재 승인 논문이라 2026년에 두고 「(게재 승인)」으로 표시했다. 저자, 제목, 학술지·학회 표기와 괄호 안 수상 표기는 누리집 그대로다.[^ij][^ic][^dj][^dc][^book]

**2026**

- T Korgul, D J Park, D H Jin, J R Lee, Curved Dual-Band Conformal Load-Bearing Antenna Structure Integrated into a Composite UAV Winglet Leading Edge for Structural Health Monitoring, Composite Structures, Accepted, Sep. 2026. (게재 승인) [국제 학술지 170]
- J H Lee, C C Chia, J R Lee, Weld Defect Classification in Phased-Array Ultrasonic Testing Using a CNN with FiLM Layer, International Journal of Aeronautical and Space Sciences, Jul. 2026 [국제 학술지 169]
- C C Chia, J R Lee, Editorial for the MST special issue: selected papers from the 20th World Conference on Non-Destructive Testing (WCNDT), Measurement Science and Technology, Jan. 2026 [국제 학술지 168]
- K H Kim, C M Lee, J W Lee, J R Lee, Deep learning-based environmental compensation for ultrasonic damage localization in wireless ultrasonic devices (2026), 2026.03.16 ~ 2026.03.19 [국제 학회 189]
- T Korgul, D J Park, D H Jin, J R Lee. Additively Manufactured Fiber-Reinforced Composite-Integrated Curved Dual-Band Conformal Antenna for UAV Winglet Applications. Composites Research, 2026 [국내 학술지 23]
- K S Ma, K J Lee, C C Chia, J R Lee. CAD Model-based Robotic Pulse-echo Ultrasonic Propagation Imaging for 3D Printed Composites and Data Acquisition for AI-based Defect Diagnosis. 비파괴검사학회지 제46권 제2호, pp.106-112, 2026 [국내 학술지 22]
- 김지현, 이정률, 지상모사실험 통한 초저궤도(VLEO)에서 Onyx/Onyx ESD 열가 소성 복합재 운용 가능성 평가, 2026 우주학술대회, 2026.06.24 ~ 2026.06.26 [국내 학회 297]
- 신혜진, 이현우, 이정률, 레이저 가진/센싱 듀얼 스캐닝 초음파전파영상화 시스템 기반 인공결함 시편 결함 가시화, 2026년 한국비파괴검사학회 춘계학술대회, 2026.05.27 ~ 2026.05.29. [국내 학회 296]
- 이준원,이창민,김경환,이정률, 복합재 항공기 구조물에서의 PZT 센서 접착 품질 균일화를 위한 휴대용 진공-열 경화 장치 개발, 2026년 한국비파괴검사학회 춘계학술대회, 2026.05.27 ~ 2026.05.29. [국내 학회 295]
- 전무승, 박정훈, 문사성, 이정률, 가스터빈 엔진 블레이드 비디오스코프 검사 자동화를 위한 AI 기 반 실시간 손상 탐지, 2026년 한국비파괴검사학회 춘계학술대회, 2026.05.27 ~ 2026.05.29. [국내 학회 294]
- Chia Chen Ciang, Lee Shi Yn, 신혜 진, 이정률, Thickness Mapping for Corroded Thick Steel Walls using Multi-Modal Laser-Ultrasonic Wavefields: Bridging Deterministic, 2026년 한국비파괴검사학회 춘계학술대회, 2026.05.27 ~ 2026.05.29. [국내 학회 293]
- Shi Yn Lee, Chen Ciang Chia, 이정률, Enhanced Guided Ultrasonic Wavefield Imaging via Wavenumber Bandpass Filtering for Loosened Fastener, 2026년 한국비파괴검사학회 춘계학술대회, 2026.05.27 ~ 2026.05.29. [국내 학회 292]
- King Sum Ma, 이정률, Development of a Modified Robotic Pulse-Echo Ultrasonic Propagation Imaging System Using a Fiber-Optic-Delivered Excitation Laser, 2026년 한국비파괴검사학회 춘계학술대회, 2026.05.27 ~ 2026.05.29. [국내 학회 291]
- 조영훈, 이정률, 연속섬유 3D 프린팅 기반 저피탐 나노위성 설계 및 전자기 성능 평가, 2026년 한국항공우주학회 춘계학술대회, 2026.03.31 ~ 2026.04.03. [국내 학회 290]
- 김지현, 이규진, 이정률, 초저궤도(VLEO)에서 Onyx/Onyx ESD 열가소성 복합재 운용 적 합성 평가, 2026년 한국항공우주학회 춘계학술대회, 2026.03.31 ~ 2026.04.03. [국내 학회 289]
- 이현우, 박동진, 이정률, 모바일 로봇 기반 RCS 측정 시스템 설계및 구축, 2026년 한국항공우주학회 춘계학술대회, 2026.03.31 ~ 2026.04.03. [국내 학회 288]
- 반재헌, 이규진, 김지현, 이정률, 저궤도 복합위협인자 지상모사실험 기반 HSC의 운용 성능 평가, 2026년 한국항공우주학회 춘계학술대회, 2026.03.31 ~ 2026.04.03. [국내 학회 287]
- 이규진, 임채민, 김완식, 이정률, 초저궤도 우주위협환경에서의 상용 밴드패스필터 신뢰성 평가 및 보호 설계 연구, 2026년 한국항공우주학회 춘계학술대회, 2026.03.31 ~ 2026.04.03. [국내 학회 286]
- 김지현, 이규진, 이정률, 초저궤도(VLEO) 우주 위협환경 프로파일링 개발 및 Onyx/Onyx ESD 열가소성 복합재 운용 적합성 평가, 2026년 한국항공우주학회 춘계학술대회, 2026.03.31 ~ 2026.04.03. [국내 학회 285]
- 박정훈, 전무승, 이정률, 진단 AI 기반 실시간 항공기 가스터빈 엔진 고압 압축기 블레이드 자동 비디오스코프 검사 시스템 개발, 2026년 한국항공우주학회 춘계학술대회, 2026.03.31 ~ 2026.04.03. [국내 학회 284]
- 이창민, 김경환, 이준원, 이정률, 서은 포화도 분석 기반 항공기 SHM용 최소 PZT 네트워크 설계 및 RAPID 알고리즘 최적화 연구, 2026년 한국항공우주학회 춘계학술대회, 2026.03.31~2026.04.03. [국내 학회 283]
- S Y Lee, C C Chia, J R Lee, M Y Harmin, Highlighting Loosened Fastener in Simple Lap Joint based on Wavenumber Bandpass Filtering of Ultrasonic Wavefield, J. Aeronaut. Astronaut. Aviat. 58(7S) (2026) 1117–28. Jul. 2026. [국제 학술지 별도 구획 18]
- X J Che , R H Xin, N S Goo, J R Lee, Mechanical Property Measurement of 3D Printed Carbon Fiber Reinforced Composites and Three-point Bending Test of a 3D Printed Control Surface, JOURNAL OF THE KOREAN SOCIETY FOR AERONAUTICAL AND SPACE SCIENCES Vol. 54, No. 5, pp. 505-513, May. 2026 [국제 학술지 별도 구획 17]
- C C Chia, S Y Lee, J R Lee, M. Y. Harmin, "Laser Ultrasonic Wavefield Propagation Imaging for Aircraft Structures", in Non-Destructive Inspection for Aircraft Materials, S. Gürgen (Ed.) , Springer, 2026. (Chapter 5) [책의 장 1]

**2025**

- D H Kim, S C Hong, J R Lee, Model-Assisted Probability of Detection Using QL-Scan GUPI for Wall-Thinning Defects, International Journal of Aeronautical and Space Sciences, Nov. 2025 [국제 학술지 167]
- D H Kim, C C Chia, S C Hong, J R Lee, Probability of detection analysis of CFRP delamination with a triple functional ultrasonic propagation imager, Measurement, Dec. 2025 [국제 학술지 166]
- D Khan, Y J Cho, J R Lee, H S Yoon, G S Park, J G Kim, Experimental erosion analysis and computational modeling of SiOx-coated polyimide in atomic oxygen under super-low-Earth-orbit conditions, Aerospace Science and Technology, Aerospace Science and Technology, Dec. 2025 [국제 학술지 165]
- H J Lee, H J Shin, J R Lee, LEO Complex Space Environment Experiment Interpretation About COTS Resistor, GFRP, and PCB, International Journal of Aeronautical & Space Sciences, Jan. 2025 [국제 학술지 164]
- K J Lee, S C Hong, S Y Rhee, J R Lee, Rotational laser ultrasonic propagation imager in pulse-echo mode for defect evaluation of type-3 COPV, Structural Health Monitoring, Sep. 2025 [국제 학술지 163]
- J R Lee, C C Chia, Special issue: World Conference on Nondestructive Testing 2024, Structural Health Monitoring, Sep. 2025 [국제 학술지 162]
- B Popiela, K H Kim, K J Lee, J R Lee, Impact of internal pressure regulation in filament winding on the quality of composite cylinders: a study with pulse-echo ultrasonic propagation imaging, Advanced Composite Materials, Vol 35(3), Aug. 2025 [국제 학술지 161]
- W H Jang, C M Seok, D J Park, J W Shim, M S Ki, H M Kim, C G Kim, J R Lee, Y W Nam, High-temperature corrugated-core radar stealth Ni-plated glass/ bismaleimide sandwich composites, Composite Structures, Aug. 2025 [국제 학술지 160]
- S Y Lee, Z Zaludin, J B Harley, J R Lee, M Y Harmin, C C Chia, Statistical Thresholding of Ultrasonic Amplitude Maps for Automated Damage Segmentation, Journal of Aeronautics, Astronautics and Aviation, Vol 57(3), Mar. 2025 [국제 학술지 159]
- K S Ma, K J Lee, J R Lee, A Study on 3D Scan-Based Robot Arm Approach for Pulse-Echo Laser Ultrasonic Testing of Curved Composite Structures, Measurement Science and Technology, 36(045903), Mar. 2025 [국제 학술지 158]
- J R Lee, H K Yoo, C C Chia, et al., Roadmap on industrial imaging techniques, Measurement Science and Technology, 36(013001), Jan. 2025 [국제 학술지 157]
- K J Lee, J R Lee, Path planning and inspection of complex-shaped 3D-printed composites based on robotic pulse-echo laser ultrasonic testing, Advanced Composite Materials, 2025 [국제 학술지 156]
- K H Kim, J H Lee, Y J Cho, J R Lee, Structural health monitoring of type 4 composite fuel tank based on correlation between ultrasonic attenuation and crack density, Advanced Composite Materials, 1–18., 2025 [국제 학술지 155]
- C C Chia, K S Ma, J R Lee, KAIST Structural Doctor: An AI System for Automatic Health Diagnosis of Composite Structures, The 3rd China–Korea–Japan Joint Symposium on Composite Materials (2025), 2025.11.22 ~ 2025.11.24 [국제 학회 188]
- G M Lee, K J Lee, J R Lee, Space Threat Environmental Testing of Passive Components for Future Application in RF Transceiver Modules, 13th IEEE Wireless for Space and Extreme Environments (2025), 2025.10.13 ~ 2025.10.15 [국제 학회 187]
- 이창민, 이정률. 항공기 구조물에 대한 램파 기반 무선 초음파 장치를 이용한 손상 모니터링 알고리즘 적용 가능성 연구. 비파괴검사학회지 제45권 제6호, pp. 474-480, 2025 [국내 학술지 21]
- 이경민, 이정률, COTS 인덕터 대상 초저궤도 복합 우주위협인자 환경 내구성 평가, 2025년도 미래 항공우주 학술대회, 2025.12.04 ~ 2025.12.04 [국내 학회 282]
- 박동진, 이유렬, 이정률, 형상 변화에 따른 회전익 블레이드 모델의 레이더 반사 면적 측정에 관한 연구, 2025년도 한국복합재료학회 추계학술대회, 2025.11.19 ~ 2025.11.21 [국내 학회 281]
- Tomasz Korgul, 박동진, 진도현, 이정률, Composite-Based Dual-Band Conformal Load-Bearing Antenna Structure for Structural Health Monitoring System in UAV, 2025년도 한국복합재료학회 추계학술대회, 2025.11.19 ~ 2025.11.21 [국내 학회 280]
- 진도현, 이정률, RAS 기반 전자전기 내부 EMI 차폐 구조물의 전자기 해석 연구, 2025년도 한국복합재료학회 추계학술대회, 2025.11.19 ~ 2025.11.21 [국내 학회 279]
- 이현우, 전무승, 홍승찬, 이정률, 모바일 로봇 기반 4차원 레이저 초음파 검사 시스템 설계 및 구축, 2025년 비파괴검사학회 추계학술대회, 2025.11.12 ~ 2025.11.14 [국내 학회 278]
- 신혜진, 이정률, 산업용 탱크 모사 금속재 시편 인공감육 손상가시화를 위한 레이저 초음파전파영상화 기술 개발, 2025년 비파괴검사학회 추계학술대회, 2025.11.12 ~ 2025.11.14 [국내 학회 277]
- Chia Chen Ciang, 신혜진, Ma King Sum, Lee Shi Yn, 이정률, AI-based Structural Health Diagnosis using Laser Ultrasonic Wavefield Data, 2025년 비파괴검사학회 추계학술대회, 2025.11.12 ~ 2025.11.14 [국내 학회 276]
- 김지현, 이규진, 이경민, 이정률, 초저궤도(VLEO) 우주 위협환경 모사 시험 기반 Onyx/Onyx ESD 열가소성 복합재의 성능 평가, 2025년 항공우주학회 추계학술대회, 2025.11.11 ~ 2025.11.14 [국내 학회 275]
- 이준원, 이창민, 이정률, PZT기반 Lamb 파와 CWT-CNN을 이용한 CFRP 평판 손상 위치 예측, 2025년 비파괴검사학회 추계학술대회, 2025.11.12 ~ 2025.11.14 [국내 학회 274]
- 이창민, 이준원, 이정률, 무선 초음파 장치 기반 다중 DI 융합 손상 위치 추정 알고리즘 연구, 2025년 항공우주학회 추계학술대회, 2025.11.11 ~ 2025.11.14 [국내 학회 273]
- King Sum Ma, 이규진, Chen Ciang Chia, 이정률, CAD Model-based Robotic Pulse-echo Ultrasonic Propagation Imaging for 3D Printed Composites and Data Acquisition for AI-based Defect Diagnosis, 2025년 비파괴검사학회 추계학술대회, 2025.11.12 ~ 2025.11.14 [국내 학회 272]
- Zalewski Włodzimierz, King Sum Ma, 이정률, Study on whole fiber optic laser ultrasonic test, 2025년 비파괴검사학회 추계학술대회, 2025.11.12 ~ 2025.11.14 [국내 학회 271]
- 전무승, 박정훈, 이정률, 비디오스코프 기반 항공기 엔진 블레이드 자동 검사 시스템 개발2025년 항공우주학회 추계학술대회, 2025.11.11 ~ 2025.11.14 [국내 학회 270]
- 이규진, 이경민, 이정률, 초저궤도 위성 송수신 모듈 적용 COTS 부품 우주위협환경 모사 시험 및 성능 변화 분석, 2025년 항공우주학회 추계학술대회, 2025.11.11 ~ 2025.11.14 [국내 학회 269]
- 박정훈, 전무승, 이정률, 엔진 블레이드 검사 자동화를 위한 손상 진단 AI 테스트베드 개발, 2025년 항공우주학회 추계학술대회, 2025.11.11 ~ 2025.11.14 [국내 학회 268]
- 이규진, 홍승찬, 이승윤, 이정률, 회전식 펄스-에코 레이저 초음파 검사 기술을 활용한 우주추진용 복합재료 고압가스 부품 검사 및 결과 분석, 2025 우주학술대회, 2025.06.25 ~2025.06.27 [국내 학회 267]
- 이경민, 이규진, 이정률, COTS 전자부품 대상 위성 궤도 기반 복합우주위협인자 시험 방법 개발, 2025 우주학술대회, 2025.06.25 ~2025.06.27 [국내 학회 266]
- 이규진, 홍승찬, 이승윤, 이정률, 회전식 펄스-에코 레이저 초음파 영상화 장치 기반 Type-3 복합재 고압탱크 검사, 2025년 비파괴검사학회 춘계학술대회, 2025.05.28 ~2025.05.30 [국내 학회 265]
- 이창민, 이정률, 항공기 구조물에 대한 무선 초음파 장치 기반 손상 모니터링 알고리즘 적용 가능성 연구, 2025년 비파괴검사학회 춘계학술대회, 2025.05.28 ~2025.05.30 [국내 학회 264]
- Chen Ciang CHIA, King Sum MA, Du Hwan KIM, and Jung-Ryul LEE, AI-Based Defect Diagnosis in Aerospace Structures Using Pulse-Echo Ultrasonic Propagation Imaging, 2025년 비파괴검사학회 춘계학술대회 (KSNT-JSNDI Workshop), 2025.05.28 ~2025.05.30 [국내 학회 263]
- 사정강, 신혜진, 이정률, Local Plate Thickness Estimation via Wavenumber–Time Analysis of Guided Ultrasonic Wavefields, 2025년 비파괴검사학회 춘계학술대회, 2025.05.28 ~2025.05.30 [국내 학회 262]
- 이정률, 자가수리포함 신개념 항공기 구조건전성 프로그램 제안, 2025년 비파괴검사학회 춘계학술대회, 2025.05.28 ~2025.05.30 [국내 학회 261]
- 신혜진, 이정률, 레이저초음파기반 산업용 탱크 모사 탄소강 시편 결함가시화 기술 개발, 2025년 비파괴검사학회 춘계학술대회, 2025.05.28 ~2025.05.30 [국내 학회 260]
- 박정훈, 전무승, 이정률, 항공기 엔진 블레이드 결함 진단용 AI 테스트베드 구축, 2025년 비파괴검사학회 춘계학술대회, 2025.05.28 ~2025.05.30 [국내 학회 259]
- 박동진, 진도현, 이정률, 회전익 항공기의 레이더 반사 면적 측정에 관한 연구, 2025년 한국복합재료학회 춘계학술대회, 2025.04.30 ~ 2025.05.02 [국내 학회 258]
- 진도현, 박동진, 이정률, 연속섬유 3D 프린트 기반 전파흡수구조의 RCS 저감 효과에 관한 연구, 2025년 한국복합재료학회 춘계학술대회, 2025.04.30 ~ 2025.05.02 [국내 학회 257]
- Tomasz Korgul, 박동진, 이정률, Development of a Robotic Antenna Measurement System for Conformal Load-Bearing Antenna Structures, 2025년 한국복합재료학회 춘계학술대회, 2025.04.30 ~ 2025.05.02 [국내 학회 256]
- King Sum Ma, 이규진, 이정률, Inspection of Complex-Shaped Composite Structures using a Robotic Pulse-echo Ultrasonic Propagation Imaging System, 2025년 한국복합재료학회 춘계학술대회, 2025.04.30 ~ 2025.05.02 [국내 학회 255]
- 박동진, 유재민, 이정률, Micro-Doppler 효과를 고려한 회전익 블레이드 모델의 레이더 반사 면적 측정에 관한 연구, 2025년 항공우주학회 춘계학술대회, 2025.04.02 ~ 2025.04.04 [국내 학회 254]
- 이경민, 이규진, 이정률, 우주환경모사장비를 활용한 소자 단위 COTS 부품 성능 변화 분석, 2025년 항공우주학회 춘계학술대회, 2025.04.02 ~ 2025.04.04 [국내 학회 253]

**2024**

- M S Jeon, J R Lee, Development of an in-situ real-time laser targeting algorithm for a 3D LiDAR-integrated galvanometric laser scanner system, Optics and Lasers in Engineering, Dec. 2024 [국제 학술지 154]
- D H Jin, D J Park, J R Lee, J M Ahn, Design and verification of the square convex surface multilayer radar absorbing structure based on additive manufacturing, Journal of Sandwich Structures and Materials, 26(7), Oct. 2024 [국제 학술지 153]
- D H Jin, J M Hyun, J R Lee, J M Ahn, Fabrication of multi-layer radar absorbing structures based on continuous fiber 3D printing and thickness correction method, Advanced Composite Materials, Vol.33(4), Jul. 2024 [국제 학술지 152]
- S Y Lee, F I Romli, N Mazlan, J R Lee, M Y Harmin, C C Chia, High-Resolution Wavenumber Bandpass Filtering of Guided Ultrasonic Wavefield for the Visualization of Subtle Structural Flaws, Aerospace, Jul. 2024 [국제 학술지 151]
- J W Park, J R Lee, Development of Wireless Ultrasonic Device for Wireless Guided-Wave Ultrasonic Propagation Imaging System, International Journal of Aeronautical and Space Sciences, Apr. 2024 [국제 학술지 150]
- J M Hyun, J R Lee, Evaluation of electromagnetic characteristics of 3D-printed radar absorbing structures based on three-dimensional period pattern surface, Measurement, Mar. 2024 [국제 학술지 149]
- Y H Kim, J R Lee, Automated Data Evaluation for Phased-Array Ultrasonic Testing based on A-scan and Feature Training, NDT & E International, Jan. 2024 [국제 학술지 148]
- D J Park, J M Hyun, J R Lee, A Study on the Electromagnetic Transmission Performance Evaluation of Antenna Housing Using 6-DOF Robot Manipulator, 20th World Conference on Non-Destructive Testing (2024), 2024.05.27 ~ 2024.05.31 [국제 학회 186]
- K H Kim and J R Lee, Acoustic Emission Localization using Laser Structural Training with Neural Network on Hydraulic-tested Type 4 COPV, 20th World Conference on Non-Destructive Testing (2024), 2024.05.27 ~ 2024.05.31 [국제 학회 185]
- D H Jin, K J Lee, J R Lee, Comparative Study of FEM-based Structural Analysis and Laser Ultrasonic Testing Results on CFRP Combustion Chambers of Hybrid Rockets, 20th World Conference on Non-Destructive Testing (2024), 2024.05.27 ~ 2024.05.31 [국제 학회 184]
- J H Lee, K J Lee, H G Park, J R Lee, Development of inspection process of 3D printed CFRP products using laser ultrasonic testing technology and AI model, 20th World Conference on Non-Destructive Testing (2024), 2024.05.27 ~ 2024.05.31 [국제 학회 183]
- D H Kim, S C Hong, J R Lee, H H Kim, J S Park, Sensitivity study between 633 nm and 1550 nm sensing LDVs on surface conditions of metallic structure using laser pulse-echo ultrasonic propagation imager, 20th World Conference on Non-Destructive Testing (2024), 2024.05.27 ~ 2024.05.31 [국제 학회 182]
- J W Hong, M S Jeon, J R Lee, Automatic Laser Beam Alignment Algorithm for Angular Pulse-Echo Ultrasonic Propagation Imaging System, 20th World Conference on Non-Destructive Testing (2024), 2024.05.27 ~ 2024.05.31 [국제 학회 181]
- K J Lee, D H Jin, J R Lee, Development of Laser Ultrasonic Testing Technology for Diagnosis of Reusable Rocket CFRP Composite Combustion Chamber, 20th World Conference on Non-Destructive Testing (2024), 2024.05.27 ~ 2024.05.31 [국제 학회 180]
- K S Ma, K J Lee, J R Lee, A Study on 3D Scan-Based Robot Arm Control Approach for Pulse-Echo Laser Ultrasonic Testing of Curved Composite Structures, 20th World Conference on Non-Destructive Testing (2024), 2024.05.27 ~ 2024.05.31 [국제 학회 179]
- M S Jeon, J R Lee, 4-Dimensional mapping method based on angular pulse-echo ultrasonic propagation imaging system, 20th World Conference on Non-Destructive Testing (2024), 2024.05.27 ~ 2024.05.31 [국제 학회 178]
- K S Ma, K J Lee, J R Lee, Development of 3D Scan Integrated Robot Arm Control for Pulse-Echo Laser Ultrasonic Testing, SPIE Smart Structures+NDE (2024), 2024.03.25 ~ 2024.03.28 [국제 학회 177]
- J H Lee, J R Lee, Development of measurement method of effective elastic properties of 3D printed CFRP plates using laser ultrasonic technique, SPIE Smart Structures+NDE (2024), 2024.03.25 ~ 2024.03.28 [국제 학회 176]
- M S Jeon, J R Lee, Research on real-time laser targeting through calibration of laser mirror scanner and LiDAR camera, SPIE Smart Structures+NDE (2024), 2024.03.25 ~ 2024.03.28 [국제 학회 175]
- 유재민, 이정률, 완전 도체(PEC) 블레이드 모델의 레이더 반사 면적 측정 및 특성 분석 , 2024년 공군사관학교 미래 항공우주 학술대회, 2024.12.05 [국내 학회 252]
- 홍정완, 이정률, 항공기 고압 압축기 블레이드 시각 검사의 인공지능 기반 실시간 자동 손상 진단 연구, 2024년 공군사관학교 미래 항공우주 학술대회, 2024.12.05 [국내 학회 251]
- 진도현, 박동진, 이정률, 연속 섬유 3D 프린트 기반 안테나 내장 일체형 구조 최적 설계에 관한 연구, 2024년 복합재료학회 추계학술대회, 2024.11.13~2024.11.15 [국내 학회 250]
- 유재민, 이정률, 회전익 블레이드 모델 레이더 단면적 측정 및 분석에 관한 연구, 2024년 복합재료학회 추계학술대회, 2024.11.13~2024.11.15 [국내 학회 249]
- 이경민, 이규진, 이정률, 초 저궤도 환경에서 인공위성 전자부품에 대한 복합우주위협인자의 영향 분석, 2024년 항공우주학회 추계학술대회, 2024.11.13~2024.11.15 [국내 학회 248]
- 이창민, 이정률, 무선 초음파 장치를 이용한 구조 손상 탐지 데이터의 보정 및 가시화 알고리즘 연구, 2024년 항공우주학회 추계학술대회, 2024.11.13~2024.11.15 [국내 학회 247]
- King Sum Ma, 이규진, 이정률, 3D 프린팅 복합재 구조 검사를 위한 CAD 모델 기반 로보틱 펄스-에코 레이저 초음파 검사 기법 개발, 2024년 항공우주학회 추계학술대회, 2024.11.13~2024.11.15 [국내 학회 246]
- 홍정완, 전무승, 이정률, 딥러닝 기법을 이용한 항공기 엔진 고압 압축기 블레이드 손상 실시간 자동 진단 연구, 2024년 항공우주학회 추계학술대회, 2024.11.13~2024.11.15 [국내 학회 245]
- 김태영, 이재호, 이정률, 이정률, CNN-GRU 기반 평판 용접부 대상 위상배열 초음파 검사 데이터의 결함 이진분류, 2024년 비파괴검사학회 추계학술대회, 2024.10.30~2024.11.01 [국내 학회 244]
- CHIA CHEN CIANG, 이정률, 산업 구조물 UPI 검사에서의 파수 대역통과 필터링 적합성, 2024년 비파괴검사학회 추계학술대회, 2024.10.30~2024.11.01 [국내 학회 243]
- 이재호, 김태영, 이정률, PAUT 진단 인공지능 솔루션 성능 개선 및 GUI 개발, 2024년 비파괴검사학회 추계학술대회, 2024.10.30~2024.11.01 [국내 학회 242]
- 신혜진. CHIA CHEN CIANG, 이정률, 레이저초음파전파영상화 기반 대형 석유화학 저장탱크 손상가시화 기술 개발, 2024년 비파괴검사학회 추계학술대회, 2024.10.30~2024.11.01 [국내 학회 241]
- 전무승, 이정률, 포인트 클라우드 기반 4차원 레이저 초음파 매핑 알고리즘 연구, 2024년 비파괴검사학회 추계학술대회, 2024.10.30~2024.11.01 [국내 학회 240]
- 이규진, 홍승찬, 이승윤, 이정률, 발사체 CFRP 복합재 연소관 및 고압용기 진단을 위한 레이저 초음파 검사 기술 개발 , 2024년 우주학술대회 , 2024.06.26~2024.06.28 [국내 학회 239]
- 신혜진, 이정률, 광섬유 기반 로보틱 레이저 초음파 검사 시스템 스캐닝 헤드 경량화 기술 개발, 2024년 복합재료학회 춘계학술대회, 2024.04.24~2024.04.26 [국내 학회 238]
- 박동진, 유재민, 이정률, 회전익 항공기 RCS 측정 기술에 대한 연구 동향, 2024년 복합재료학회 춘계학술대회, 2024.04.24~2024.04.26 [국내 학회 237]
- 유재민, 박동진, 이정률, RCS 측정 정확도 향상을 위한 근거리-원거리 변환 알고리즘 연구, 2024년 복합재료학회 춘계학술대회, 2024.04.24~2024.04.26 [국내 학회 236]
- 이한준, 이규진, 이정률, 우주위협모사장치 기반 위성 송수신모듈 실험, 2024년 항공우주학회 춘계학술대회, 2024.04.03~2024.04.05 [국내 학회 235]
- S Y Lee, C C Chia, F I Romli, N Mazlan, J R Lee, M Y Harmin, Visualizing Partially Loosened Fastener through Frequency-Wavenumber Analysis of Ultrasonic Wavefield, J. Aeronaut. Astronaut. Aviat. 56 (2024) 147–155. Mar. 2024. [국제 학술지 별도 구획 16]

**2023**

- M Shanigaram, M J Kim, C M Seok, D J Hong, M S Kim, J M Hyun, J R Lee, C G Kim, Y W Nam, Folded-core radar-absorbing sandwich composite with sendust particle-added Ni-plated glass/polyether ether ketone thermoplastic resin in the ultrahigh-frequency band, Composites Part B-Engineering, v.264, Sept. 2023 [국제 학술지 147]
- J M Hyun, J R Lee, Electromagnetic Characteristics of 3D-printed Composites by Free-space Measurement, Measurement, Vol. 217, 113022, Aug. 2023 [국제 학술지 146]
- K J Lee, M S Jeon,J R Lee, Evaluation of manufacturing defects in 3D printed carbon fiber reinforced cylindrical composite structure based on laser ultrasonic testing, NDT & E International, Volume. 135, Apr 2023, 102802 [국제 학술지 145]
- M A A Shahrim, C C Chia, H R Ramli, J R Lee, M Y Harmin, Adaptive Mode Filter for Lamb Wavefield in the Wavenumber-Time Domain based on Wavenumber Response Function, Aerospace 2023, 10, 347. Apr. 2023 [국제 학술지 144]
- C C Chia, S Y Lee, M Y Harmin, Y S Choi, J R Lee, Guided Ultrasonic Waves Propagation Imaging: A Review, Measurement Science and Technology, Vol. 34, 052001, Feb. 2023 [국제 학술지 143]
- H G Park, J R Lee, Laser-ultrasonic testing and deep-learning based defect diagnosis in 3D-printed CFRP, International Committee on Aeronautical Fatigue and Structural Integrity (ICAF 2023), 2023.06.26 ~ 2023.06.29 [국제 학회 174]
- M J Im, J R Lee, A mobile robotic non-destructive inspection system based on laser ultrasonic propagation and optical images, International Committee on Aeronautical Fatigue and Structural Integrity (ICAF 2023), 2023.06.26 ~ 2023.06.29 [국제 학회 173]
- K J Lee, J R Lee, Robotic-based laser ultrasonic non-destructive testing of 3d-printed continuous fiber reinforced flight control surface, International Committee on Aeronautical Fatigue and Structural Integrity (ICAF 2023), 2023.06.26 ~ 2023.06.29 [국제 학회 172]
- 박현규, 이정률 , 항공우주 3D 프린팅 복합재 비파괴검사에서 레이저 초음파 및 인공지능 기반 자동 진단 알고리즘 연구, 2023 공군사관학교 미래 항공우주 학술대회, 2023.12.05 (대학원 우수상) [국내 학회 234]
- 이한준, 현종민, 이정률, 우주위협모사장치 기반 전자 환경 노출에 따른 CFRP 및 GFRP 복합재의 기계적 성능 저하에 대한 연구, 2023년 항공우주학회 추계학술대회, 2023.11.15~2023.11.17 [국내 학회 233]
- 김경환, 조용주, 이정률, 수소저장용 COPV에서 PZT 초음파 전파 감쇠를 이용한 구조 건전성 모니터링 기법 연구, 2023년 항공우주학회 추계학술대회, 2023.11.15~2023.11.17 [국내 학회 232]
- 김기석, 이정률, 무선 구조 건전성 모니터링을 위한 저온 환경에서의 무선 초음파 이용 온도 보상 기법 연구, 2023년 항공우주학회 추계학술대회, 2023.11.15~2023.11.17 [국내 학회 231]
- 이규진, 이정률, 로보틱 펄스-에코 레이저 초음파 검사 기술 개발 및 복잡형상 3D 프린팅 복합재 구조 결함 탐지 적용 연구, 2023년 복합재료학회 추계학술대회, 2023.11.08~2023.11.10 [국내 학회 230]
- 진도현, 현종민, 이정률, 안준모, 경사 입사 전파 흡수에 특화된 직사각형 볼록 요철면 다층 전파흡수구조 설계, 2023년 복합재료학회 추계학술대회, 2023.11.08~2023.11.10 [국내 학회 229]
- 박동진, 남영우, 이정률, 고온 환경에서의 전파흡수구조의 전자기 성능 평가에 관한 연구, 2023년 복합재료학회 추계학술대회, 2023.11.08~2023.11.10 [국내 학회 228]
- Chen Ciang Chia, Shi Yn Lee, 김두환, 전무승, Mohd. Yazdi Harmin, 이정률, Visualization of Wall Thinning through Wavenumber Bandpass Filtering of Guided Ultrasound Propagation Imaging Wavefield Data, 2023년 비파괴검사학회 추계학술대회, 2023.11.08~2023.11.10 [국내 학회 227]
- 이재호, 이정률, 레이저 초음파 기반 판형 소재의 분산곡선 도출 및 물성 역산, 2023년 비파괴검사학회 추계학술대회, 2023.11.08~2023.11.10 [국내 학회 226]
- 김용호, 이정률, PAUT 결함평가 솔루션 GUI 개발 및 시연 결과, 2023년 비파괴검사학회 추계학술대회, 2023.11.08~2023.11.10 [국내 학회 225]
- 홍정완, 전무승, 이정률, 각회전 펄스-에코 초음파전파 영상화 시스템 기반 빔 정렬 자동화 알고리즘 연구, 2023년 비파괴검사학회 추계학술대회, 2023.11.08~2023.11.10 [국내 학회 224]
- MA KING SUM, 이규진, 이정률, 3D Scan-Based Robot Arm Control for Pulse-Echo Laser Ultrasonic Testing: A Proposed Methodology, 2023년 비파괴검사학회 추계학술대회, 2023.11.08~2023.11.10 [국내 학회 223]
- 이한준, 현종민, 이정률 , 우주환경모사장치 기반 Spacecraft charging & ESD 현상의 가속수명시험에 관한 연구, 제1회 우주학술대회, 2023.06.28~2023.06.30 [국내 학회 222]
- 김기석, 이정률, 무선 초음파 장치를 이용한 구조 건전성 모니터링에서의 온도 보상 기법 연구, 한국비파괴검사학회 2023 춘계학술대회, 2023.05.24~2023.05.26 [국내 학회 221]
- 박현규, 김용호, 이정률, 위상 배열 초음파 검사 3D 데이터 및 딥러닝 신경망 기반 용접부 결함 탐지 연구, 한국비파괴검사학회 2023 춘계학술대회, 2023.05.24~2023.05.26 [국내 학회 220]
- 이규진, 이정률, 형상 위치 제어 기반 로보틱 펄스-에코 레이저 초음파 검사 기술 개발 및 연속섬유 3D 프린팅 조종면 제작 결함 탐지 적용 연구, 한국비파괴검사학회 2023 춘계학술대회, 2023.05.24~2023.05.26 [국내 학회 219]
- 사정강, 유재민, 이시인, M.Y. Harmin, 이정률, 파수-시간 도메인 필터 기반 초음파 파동장 데이터의 특징 추출, 한국비파괴검사학회 2023 춘계학술대회, 2023.05.24~2023.05.26 [국내 학회 218]
- 김용호, 박현규, 이정률, PAUT 진단 인공지능 솔루션 및 시작품 개발 계획, 한국비파괴검사학회 2023 춘계학술대회, 2023.05.24~2023.05.26 [국내 학회 217]
- 김두환, 전무승, 홍승찬, 이정률, 구조물 비파괴 검사 적용을 위한 완전 비접촉 레이저 유도 초음파 전파 영상화 기술 기반 결함 가시화 연구, 한국항공우주학회 2023 춘계학술대회, 2023.04.19~2023.04.21 [국내 학회 216]
- 임민지, 전무승, 이정률, 항공기 하부면 비파괴 검사를 위한 모바일 로봇 기반 레이저 초음파 검사 기술 연구, 한국항공우주학회 2023 춘계학술대회, 2023.04.19~2023.04.21 [국내 학회 215]
- 전무승, 이정률, 최적화 기법을 활용한 레이저 미러 스캐너 LiDAR 카메라 캘리브레이션 기법 연구, 한국항공우주학회 2023 춘계학술대회, 2023.04.19~2023.04.21 [국내 학회 214]
- 김경환, 전무승, 이정률, 복합재 연료용기 음향방출 위치효정을 위한 G-UPI 시스템 곡률 보정 적용 연구, 한국복합재료학회 2023 춘계학술대회, 2023.04.19~2023.04.21 [국내 학회 213]
- 진도현, 현종민, 이정률, 안준모, 연속섬유 3D 프린팅 기술 기반 사각 볼록 요철면 다층 전파흡수구조 설계, 한국복합재료학회 2023 춘계학술대회, 2023.04.19~2023.04.21 [국내 학회 212]
- 박동진, 진도현, 이정률, 로봇팔을 이용한 안테나 전자기 성능 평가에 대한 연구, 한국복합재료학회 2023 춘계학술대회, 2023.04.19~2023.04.21 [국내 학회 211]

**2022**

- S U Din, J M Hyun, D S Son, J R Lee, Robotic scanning free-space measurement system for electromagnetic performance evaluation of curved radar absorbing structures, International Journal of Advanced Robotic Systems, Vol. 19, No. 4, pp.1-15, July. 2022. [국제 학술지 142]
- S U Din, J M Hyun, D S Son, J R Lee, Rotation Included 3-Axis Scanning Free-Space Measurement and Curvature Compensation for Electromagnetic Evaluation of Leading-edge and Curved Stealth Structures, Measurement Science and Technology, Vol. 33, 055903, May. 2022. [국제 학술지 141]
- A S Shin, J H Park, H S Lee, Y S Choi, J R Lee, Corrosion visualization under organic coating using laser ultrasonic propagation imaging, Smart Structures and Systems, Vol. 29, pp. 301-309 Feb. 2022. [국제 학술지 140]
- J M Lee, Y S Choi, J R Lee, Laser structural training, artificial intelligence-based acoustic emission localization and structural/noise signal distinguishment in a thick FCEV fuel tank, International Journal of Hydrogen Energy, Vol. 47, pp. 4236-4254, Jan. 2022. [국제 학술지 139]
- M S Jeon, D H Kim, J R Lee, S C Hong. Cylindrical structure technique based on angular QL-scan G-UPI system, Journal of the Korean Society for Nondestructive Testing, Vol. 42, No. 6, pp. 487-495, Dec 2022 [국내 학술지 20]
- 이규진, 이정률, 재사용 발사체 CFRP 복합재 연소관 진단을 위한 레이저 초음파 검사 기술 개발, 한국항공우주학회 2022 추계학술대회, 2022.11.16~2022.11.18 [국내 학회 210]
- 김윤규, 김용호, 이정률, PAUT S-scan 영상 데이터 딥러닝을 이용한 용접부 자동 결함 평가 연구, 한국항공우주학회 2022 추계학술대회, 2022.11.16~2022.11.18 [국내 학회 209]
- 박동진, 현종민, 이정률, 고온 환경에서의 전자기 특성 분포에 관한 연구, 한국복합재료학회 2022 추계학술대회, 2022.11.02~2022.11.04 [국내 학회 208]
- 진도현, 현종민, 이정률, 3D 프린트 기반 구조물 형상에 따른 전자기 특성에 관한 연구, 한국복합재료학회 2022 추계학술대회, 2022.11.02~2022.11.04 [국내 학회 207]
- 박현규, 이규진, 이정률, 레이저 초음파 검사 기반 연속섬유 3D 프린팅 CFRP 복합재 디본딩 진단 AI 개발, 한국복합재료학회 2022 추계학술대회, 2022.11.02~2022.11.04 (우수발표논문상) [국내 학회 206]
- 전무승, 김두환, 이정률, 홍승찬, 각회전 QL 스캔 G-UPI 시스템 기반 원통형 구조 스캔 기술 연구, 한국비파괴검사학회 2022 추계학술대회, 2022.10.26~2022.10.28 (우수발표논문상) [국내 학회 205]
- 김용호, 김윤규, 이정률, A-scan 학습 신경망 기반 위상배열초음파 결함 평가 알고리즘, 한국비파괴검사학회 2022 추계학술대회, 2022.10.26~2022.10.28 [국내 학회 204]
- 김두환, 전무승, 홍승찬, 이정률, 플랜트 구조물 비파괴 검사 적용을 위한 비 접촉 레이저 유도 초음파 전파 영상화 기술 기반 결함 가시화 연구, 한국비파괴검사학회 2022 추계학술대회, 2022.10.26~2022.10.28 (우수발표논문상) [국내 학회 203]
- 김기석, 박진우, 이정률, 무선 초음파 장치를 이용한 알루미늄 시편의 손상 탐지 가시화 연구, 한국비파괴검사학회 2022 추계학술대회, 2022.10.26~2022.10.28 [국내 학회 202]
- 김경환, 조용주, 이정률, TYPE 4 복합재 연료용기에서의 PZT 초음파 감쇠비를 통한 구조 건전성 모니터링 기법 연구, 한국비파괴검사학회 2022 추계학술대회, 2022.10.26~2022.10.28 [국내 학회 201]
- 사정강, 이시인, Mohd. Yazdi Harmin, 최윤실, 이정률, Guided Ultrasonic Waves Propagation Imaging: A Review, 한국비파괴검사학회 2022 춘계학술대회, 2022.05.25~2022.05.27 [국내 학회 200]
- 김윤규, 홍승찬, 김용호, 전무승, 이길성, 이정률, 레이저 투과 초음파 검사를 통한 풍력 터빈 블레이드 CFRP 스파캡 AI 결함 진단, 한국비파괴검사학회 2022 춘계학술대회, 2022.05.25~2022.05.27 [국내 학회 199]
- 김용호, 김윤규, 이정률, PAUT 데이터 학습을 위한 신경망 구조 설계 및 최적화, 한국비파괴검사학회 2022 춘계학술대회, 2022.05.25~2022.05.27 [국내 학회 198]
- 임민지, 전무승, 김두환, 이정률, 로버 기반 레이저 도플러 진동계 센싱 유도 초음파 전파 영상화 시스템, 한국비파괴검사학회 2022 춘계학술대회, 2022.05.25~2022.05.27 (우수논문발표상) [국내 학회 197]
- 전무승, 임민지, 김두환, 이정률, 로버 기반 유도 초음파전파영상화 시스템 개발, 한국비파괴검사학회 2022 춘계학술대회, 2022.05.25~2022.05.27 [국내 학회 196]
- 홍승찬, 이정률, 레이저초음파 비파괴검사 기술의 국내외 적용 사례, 한국비파괴검사학회 2022 춘계학술대회, 2022.05.25~2022.05.27 (우수발표논문상) [국내 학회 195]
- 김두환, 홍승찬, 이정률, 복합재료 소재 내부 결함 가시화를 위한 선택적 초음파 전파 영상화 기술 개발, 한국비파괴검사학회 2022 춘계학술대회, 2022.05.25~2022.05.27 [국내 학회 194]
- 이재호, 이정률, 펄스-에코 기법을 활용한 연속 섬유 3D 프린팅 시편 비파괴 검사, 한국복합재료학회 2022 춘계학술대회, 2022.05.18~2022.05.20 (최우수발표논문) [국내 학회 193]
- 이규진, Salah Ud Din, 이정률, 레이저 초음파 검사 기반 연속섬유 3D 프린팅 CFRP 결합 원통형 구조 결함 가시화, 한국복합재료학회 2022 춘계학술대회, 2022.05.18~2022.05.20 (우수발표논문) [국내 학회 192]
- Salah Ud Din, 현종민, 손대성, 이정률, Dual port robotic scanning free-space measurement for electromagnetic evaluation of stealth radome structures, 한국복합재료학회 2022 춘계학술대회, 2022.05.18~2022.05.20 [국내 학회 191]
- 현종민, 이정률, 스텔스 구조의 근거리 RCS 평가를 위한 연구, 한국복합재료학회 2022 춘계학술대회, 2022.05.18~2022.05.20 [국내 학회 190]
- 손대성, 현종민, 이정률, 스텔스 구조물의 설계 및 전자기 성능 평가, 한국복합재료학회 2022 춘계학술대회, 2022.05.18~2022.05.20 [국내 학회 189]
- 진도현, 현종민, 이정률, 안준모, 3D 프린트 기반 다층형 전파흡수구조 제작 특성에 대한 연구, 한국항공우주학회 2022 춘계학술대회, 2022.04.20~2022.04.22 [국내 학회 188]
- 현종민, 이정률, 안준모, 3D 프린트 기반 요철면 전파흡수구조의 전자기 특성에 대한 연구, 한국항공우주학회 2022 춘계학술대회, 2022.04.20~2022.04.22 [국내 학회 187]
- M A Shahrim, M Y Harmin, F I Romli , C C Chia, J R Lee, Damage Visualization based on Frequency Shift of Single-Mode Ultrasound-Guided Wavefield, Journal of Aeronautics, Astronautics and Aviation, Vol. 54, pp. 297–306, Sep. 2022. [국제 학술지 별도 구획 15]
- J W Park, J R Lee, Strain measurements of an aircraft wing using embedded CNT fiber sensor and wireless SHM sensor node, Functional Composites and Structures, Vol. 4, 035004, Sep. 2022. [국제 학술지 별도 구획 14]

**2021**

- J H An, H Ahmed, J R Lee, Defect Visualization of Cylindrical and Conical CFRP Lattice Structures using Rotational Ultrasonic Propagation Imager, Measurement Science and Technology, Vol. 32(12), 124001, pp. 19, Dec. 2021. [국제 학술지 138]
- A R Syamil, Y S Choi, J R Lee, Novel distance-based slicing algorithm for ultrasonic propagation imaging, Structural Control and Health Monitoring, Vol. 28, pp. e2846, Dec. 2021. [국제 학술지 137]
- J H An, S Din, H Ahmed, J R Lee, Simultaneous external and internal inspection of a cylindrical CFRP lattice-skin structure based on rotational ultrasonic propagation imaging and laser displacement sensing, Composite Structures, Vol. 276, 114592, Nov. 2021. [국제 학술지 136]
- D S Son, J M Hyun, S Chaki, C H Park and J R Lee, Evaluation of Mechanical/Electromagnetic Preformation of Single-Sided Active Frequency Selective Surface for Stealth Radomes, International Journal of Aeronautical and Space Science, Vol. 22, pp. 1235-1242, Oct. 2021. [국제 학술지 135]
- Young-Jun Lee, Seung-Chan Hong, Jung-Ryul Lee, Sung-Jin Hong, Corner inspection method for L-shaped composite structures using laser ultrasonic rotational scanning technique, Advanced Composite Materials, Vol. 30(5), pp. 431-442, Sept. 2021 [국제 학술지 134]
- J W Park, Y H Sung, S Y On, O H Kwon, H C Bang, S S Kim, J H Han and J R Lee, Development of wireless SHM sensor node for in-flight real-time monitoring using embedded CNT fiber sensors, Smart Structures and Systems, Vol. 28, No. 3 333-341, Sept. 2021. [국제 학술지 133]
- H Ahmed, A Moshin, S C Hong, J R Lee, J B Ihn, Robotic Laser Sensing and Laser Mirror Excitation for Pulse-Echo Scanning Inspection of Fixed Composite Structures with Non-planar Geometries, Measurement, Vol. 176, 109109, May. 2021. [국제 학술지 132]
- J Joh, Y Choi, J R Lee, Reverberation-based High-speed Guided-Wave Ultrasonic Propagation Imager for Structural Inspection of Thick Composites, Composite Structures, Vol. 259, 113446, Mar. 2021. [국제 학술지 131]
- J M Hyun, S Y Cho, K H Kim, J R Lee, J K Yang. A study on the electromagnetic performance evaluation of composite specimen based on 3D printer, SPIE Active and Passive Smart Structures and Integrated Systems 2021, Digital Forum, 2021.03.22 ~ 2021.03.26 [국제 학회 171]
- 조상연, 이정률, 딥러닝을 활용한 3D 프린트 복합재의 자동 결함 탐지 기법, 한국항공우주학회 2021 추계학술대회, 2021.11.17~2021.11.19 [국내 학회 186]
- 손대성, 이정률, 주파수 선택막이 적용된 스텔스 레이돔의 구조 해석을 위한 물성 매핑 기법, 한국항공우주학회 2021 추계학술대회, 2021.11.17~2021.11.19 [국내 학회 185]
- 이재호, 조상연, 이정률, 연속 섬유 3D 프린터를 이용한 일체형 조종면 설계 및 제작, 한국복합재료학회 2021 추계학술대회, 2021.11.11~2021.11.12 [국내 학회 184]
- 손대성, 이정률, 물성 매핑 기법을 이용한 균일하지 않은 단위 구조가 적용된 구조 해석, 한국복합재료학회 2021 추계학술대회, 2021.11.11~2021.11.12 [국내 학회 183]
- 손대성, 조상연, 이정률, 복합재료 3D 프린터로 제작한 전파흡수구조의 비파괴 검사 및 전자기 성능 평가, 한국복합재료학회 2021 추계학술대회, 2021.11.11~2021.11.12 [국내 학회 182]
- 이규진, 조상연, 이정률, 회전식 투과 레이저 초음파 전파 영상화 기반 연속섬유 3D 프린팅 CFRP 원통형 구조 제작 결함 평가, 한국복합재료학회 2021 추계학술대회, 2021.11.11~2021.11.12(최우수발표논문상) [국내 학회 181]
- 박동진, 현종민, 이정률, 전기로 및 자유 공간 측정을 이용한 고온에서의 전자기 물성 측정 방법, 한국복합재료학회 2021 추계학술대회, 2021.11.11~2021.11.12 [국내 학회 180]
- 김두환, 이정률, 선택적 초음파 전파 영상화 시스템 활용 CFRP 복합재 손상 가시화 특성 연구, 한국비파괴검사학회 2021 추계학술대회, 2021.10.28~2021.10.29 [국내 학회 179]
- 박진우, 이정률, 무선 초음파 장치와 센서 네트워크를 이용한 CFRP 복합재 손상 탐지 기법, 한국비파괴검사학회 2021 추계학술대회, 2021.10.28~2021.10.29 [국내 학회 178]
- 김윤규, 홍승찬, 김용호, 전무승, 이길성, 이정률, 레이저 투과 초음파 기술을 통한 풍력 터빈 블레이드 CFRP 스파캡의 자동 결함 탐지 연구, 한국비파괴검사학회 2021 추계학술대회, 2021.10.28~2021.10.29 [국내 학회 177]
- 김용호, 김윤규, 이정률, 위상배열초음파 자동평가기술을 위한 데이터 추출 및 전처리 기술 개발, 한국비파괴검사학회 2021 추계학술대회, 2021.10.28~2021.10.29 [국내 학회 176]
- 전무승, 김용호, 김윤규, 이정률, 홍승찬, 이길성, 레이저 투과 초음파 전파 영상화 장치를 사용한 복합재 풍력 터빈 블레이드 스파캡 현장 비파괴 평가, 한국비파괴검사학회 2021 추계학술대회, 2021.10.28~2021.10.29 [국내 학회 175]
- 이준민, 이정률, 복합재 수소 저장 압력 용기의 음향방출 위치 표정 기법과 음향방출 및 잡음 신호 특징 분석, 2021년도 한국항공우주학회 춘계학술대회, 삼척, 2021.07.07~2021.07.09 [국내 학회 174]
- 김두환, 홍승찬, 이정률, 초음파 전파 모드에 따른 복합재료 내부 결함 가시화 특성 연구, 2021년도 한국항공우주학회 춘계학술대회, 삼척, 2021.07.07~2021.07.09 [국내 학회 173]
- 박진우, 이정률, Real-time structural health monitoring by composite wing skin with embedded carbon nanotube fiber sensor, 2021년도 한국복합재료학회 춘계학술대회, 대전, 2021.06.24~2021.06.25 (우수발표논문상) [국내 학회 172]
- Salah ud Din, 현종민, 손대성, 이정률, Coordinate-based Scanning of Leading-edge Specimen for Electromagnetic Performance Evalution Using 3-Axis Scanning Free-space Measurement Method, 2021년도 한국복합재료학회 춘계학술대회, 대전, 2021.06.24~2021.06.25 [국내 학회 171]
- 최윤실, 이정률, 유도초음파 전파 영상화 시스템을 사용한 Type Ⅳ 고압수소저장용기의 구조 감쇠비 측정 기법, 2021년도 한국복합재료학회 춘계학술대회, 대전, 2021.06.24~2021.06.25 [국내 학회 170]
- 홍승찬, 전무승, 김용호, 이정률, 이길성, 레이저 투과 초음파 기술을 사용한 풍력 터빈 블레이드 복합재 스파캡 품질 평가 현장 적용을 위한 운용 전략, 2021년도 한국복합재료학회 춘계학술대회, 대전, 2021.06.24~2021.06.25 [국내 학회 169]
- 손대성, 현종민, 이정률, 곡률을 가지는 가변 주파수 스텔스 레이돔의 전자기 성능 예측 기법, 2021년도 한국복합재료학회 춘계학술대회, 대전, 2021.06.24~2021.06.25 [국내 학회 168]
- 현종민, 조상연, 이정률, 연속섬유 3D 프린트 복합소재의 전자기 성능에 관한 연구, 2021년도 한국복합재료학회 춘계학술대회, 대전, 2021.06.24~2021.06.25 [국내 학회 167]
- 이재호, 이정률, 펄스레이저와 레이저 도플러 진동계를 통한 램파의 분산곡선 비접촉측정, 비파괴검사학회 2021 춘계학술대회, 2021.6.3~2021.6.4 [국내 학회 166]
- 전무승, 이정률, 홍승찬, 이길성, 풍력 터빈 블레이드 복합재 스파캡의 품질 평가를 위한 레이저 투과 초음파 기술의 현장 적용성 개선 연구, 비파괴검사학회 2021 춘계학술대회, 2021.6.3~2021.6.4 (우수논문발표상) [국내 학회 165]
- S Y Cho, J R Lee, Investigation of manufacturing defects in 3D-printed CFRP using laser ultrasonic testing and X-ray micro-computed tomography, Functional Composites and Structures, Vol.3, 025005 June. 2021. [국제 학술지 별도 구획 13]

## 특허

누리집 Patent 페이지의 42건 가운데 등록일(등록 전이면 출원일)이 2021년 10월 13일 이후인 13건이다(27번, 31–42번). 발명자, 명칭, 국가, 출원·등록 번호와 날짜는 누리집 표기 그대로다. 27번과 31번은 2019년에 출원해 2025년에 등록된 특허다.[^patent]

- 이정률, 이현우, 레이더 반사 단면적 측정 시스템 및 이를 이용한 레이더 반사 단면적 측정 방법, KR Patent, 출원번호 : 10-2026-0119435, 출원일: 2026.06.30
- 이정률, 이규진, 이경민, 우주위협환경모사 장치, KR Patent, 출원번호: 10-2025-0037412, 출원일: 2025.03.24
- 이정률, 김기석, 압전 소자에 기초한 무선 초음파 측정 방법 및 시스템, KR Patent, 출원번호: 10-2023-0181170, 출원일: 2023.12.13
- 조용주, 이정률, 김경환, Apparatus for Inspecting Fuel Vessel, and System and Method for Identifying Crack Density of Vessel, US Patent, 출원번호: 18/459,513, 출원일: 2023.09.01
- 이정률, 진도현, 안준모, 연속 섬유 3D 프린트 기반 요철면 다층 전파흡수구조장치 및 그 설계방법, KR Patent, 출원번호 : 10-2023-0097595, 출원일: 2023.07.26, 등록번호 : 10-2922968, 등록일: 2026.01.30
- 홍영기, 이정률, 김건, 윤병기, 이은석, 전무승, 크랙 검사 장치 및 그것을 이용한 크랙 검사 방법, KR Patent, 출원번호 : 10-2023-0055675, 출원일: 2023.04.27
- 이정률, 진도현, 3D 프린터 및 이를 이용한 3D 프린팅 방법, KR Patent, 출원번호: 10-2022-0155627, 출원일: 2022.11.18
- 조용주, 이정률, 김용호, Pressure Vessel Inspection Device, CN Patent, 출원번호: 202210899695.6, 출원일: 2022.07.28
- 조용주, 이정률, 김용호, Pressure Vessel Inspection Apparatus, US Patent, 출원번호: 17859423, 출원일: 2022.07.07, 등록번호 : 12146862, 등록일: 2024.11.19
- 이정률, 박동진, 물성 평가 시스템, KR Patent, 출원번호: 10-2022-0028119, 출원일: 2022.03.04, 등록번호 : 10-2771760, 등록일 : 2025.02.18
- 조용주, 이정률, 김용호, 압력용기검사장치, KR Patent, 출원번호: 10-2021-0138720, 출원일: 2021.10.18
- 이정률, 이영준, 조용주, 정재한, 이현준, 황기호, 압력용기검사장치, KR Patent, 출원번호: 10-2019-0134815, 출원일: 2019.10.28, 등록번호: 10-279253, 등록일: 2025.04.01
- 인정범, 이정률, 구조물 내의 이상들의 강화된 시각화를 위한 방법 및 장치, KR Patent, 출원번호: 10-2019-0034359, 출원일: 2019.03.26, 등록번호: 10-2806833, 등록일: 2025.05.08

## 소식

누리집 Media Coverage 페이지에 실린 방송·강의 4건과, 연구실이 개발한 시작품을 알리는 Prototype Launch 메뉴의 2021년·2023년 페이지에 실린 시작품 3건이다. 날짜는 연도만 적혀 있다.[^media][^proto21][^proto23]

- 2024 · [과학으로 보는 세상 SEE] - 하늘길을 달린다! UAM / KBS대전 (2024)
- 2023 · KTV 특집 ／ 대한민국, 우주시대를 열다 (2023)
- 2023 · KAIST IP 영재기업인 교육원 ／ 미래기술트렌드 7차시 (2023)
- 2023 · 전과자 ep.44 ／ 카이스트 항공우주공학과 (2023)
- 2023 · 시작품 공개(Prototype Launch): High Temperature-Scanning Free Space Measurement, HT-SFSM system
- 2023 · 시작품 공개(Prototype Launch): Wireless Ultrasonic Device (WUD) System
- 2021 · 시작품 공개(Prototype Launch): Through-transmission Ultrasonic Propagation Imaging System, TUPI System

## 연락과 위치

- 교수실: N7-2 #3334(누리집 바닥글, 학과 연구실 소개)[^home][^aelab]
- 교수 전화: 042-350-3768(누리집 바닥글, 학과 연구실 소개)[^home][^aelab]
- 교수 이메일: leejrr@kaist.ac.kr[^prof][^aelab][^aefac]
- 주소: 291 Daehak-ro, Yuseong-gu, Daejeon 34141, KAIST(누리집 바닥글 표기)[^home]
[^home]: 연구실 누리집 첫 화면 <https://mailab.kaist.ac.kr/> (연구실 소개, 응용 분야, 바닥글 주소·전화·이메일, 2026-10-23 열람)
[^overall]: 연구실 누리집 Research > Overall Introduction 페이지 <https://mailab.kaist.ac.kr/research/overall-introduction> (MAI Lab?, About Supervisor, Achievements, Research field, 2026-10-23 열람)
[^guided]: 연구실 누리집 Research > Guided Wave UPI 페이지 <https://mailab.kaist.ac.kr/research/guided-wave-upi> (2026-10-23 열람)
[^bulk]: 연구실 누리집 Research > Bulk Wave UPI 페이지 <https://mailab.kaist.ac.kr/research/bulk-wave-upi> (2026-10-23 열람)
[^robotic]: 연구실 누리집 Research > Robotic UPI 페이지 <https://mailab.kaist.ac.kr/research/robotic-upi> (2026-10-23 열람)
[^ishm]: 연구실 누리집 Research > Integrated SHM 페이지 <https://mailab.kaist.ac.kr/research/integrated-shm> (2026-10-23 열람)
[^pyro]: 연구실 누리집 Research > Shock & Vibration 페이지 <https://mailab.kaist.ac.kr/research/shock-vibration> (Pyroshock Team, 2026-10-23 열람)
[^stealth]: 연구실 누리집 Research > Stealth Measurement Technology 페이지 <https://mailab.kaist.ac.kr/research/stealth-measurement-technology> (2026-10-23 열람)
[^hangar]: 연구실 누리집 Research > Smart Hangar 페이지 <https://mailab.kaist.ac.kr/research/smart-hangar> (2026-10-23 열람)
[^space]: 연구실 누리집 Research > Space Environment 페이지 <https://mailab.kaist.ac.kr/research/space-environment> (2026-10-23 열람)
[^rover]: 연구실 누리집 Research > UPI & RCS Rover 페이지 <https://mailab.kaist.ac.kr/research/upi-rcs-rover> (2026-10-23 열람)
[^rlv]: 연구실 누리집 Research > Reusable Launch Vehicle 페이지 <https://mailab.kaist.ac.kr/research/reusable-launch-vehicle> (2026-10-23 열람)
[^r3dp]: 연구실 누리집 Research > 3D Printing Composites 페이지 <https://mailab.kaist.ac.kr/research/3d-printing-composites> (2026-10-23 열람)
[^prof]: 연구실 누리집 Members > Professor 페이지 <https://mailab.kaist.ac.kr/members/professor> (교수와 연구부교수 카드, 2026-10-23 열람)
[^members]: 연구실 누리집 Members 메뉴의 Doctoral Student <https://mailab.kaist.ac.kr/members/doctoral-student>, Master Student <https://mailab.kaist.ac.kr/members/master-student>, Postdoc <https://mailab.kaist.ac.kr/members/postdoc>, Visiting Prof./Researcher <https://mailab.kaist.ac.kr/members/visiting-prof-researcher> 페이지 (2026-10-23 열람)
[^alumni]: 연구실 누리집 Members > Alumni 페이지 <https://mailab.kaist.ac.kr/members/alumni> (카드 48장, 2026-10-23 열람)
[^intern]: 연구실 누리집 Members > Intern 페이지 <https://mailab.kaist.ac.kr/members/intern> (2026-10-23 열람)
[^ij]: 연구실 누리집 Publication > International Journal 페이지 <https://mailab.kaist.ac.kr/publication/international-journal> (첫 번호 구획 1–171번, 별도 번호 구획 1–18번, 2026-10-23 열람)
[^ic]: 연구실 누리집 Publication > International Conference 페이지 <https://mailab.kaist.ac.kr/publication/international-conference> (2026-10-23 열람)
[^dj]: 연구실 누리집 Publication > Domestic Journal 페이지 <https://mailab.kaist.ac.kr/publication/domestic-journal> (2026-10-23 열람)
[^dc]: 연구실 누리집 Publication > Domestic Conference 페이지 <https://mailab.kaist.ac.kr/publication/domestic-conference> (2026-10-23 열람)
[^book]: 연구실 누리집 Publication > Book & Chapter 페이지 <https://mailab.kaist.ac.kr/publication/book-chapter> (2026-10-23 열람)
[^patent]: 연구실 누리집 Publication > Patent 페이지 <https://mailab.kaist.ac.kr/publication/patent> (2026-10-23 열람)
[^media]: 연구실 누리집 Media Coverage 페이지 <https://mailab.kaist.ac.kr/media-coverage> (2026-10-23 열람)
[^proto21]: 연구실 누리집 Prototype Launch > 2021 페이지 <https://mailab.kaist.ac.kr/prototype-launch/2021> (2026-10-23 열람)
[^proto23]: 연구실 누리집 Prototype Launch > 2023 페이지 <https://mailab.kaist.ac.kr/prototype-launch/2023> (2026-10-23 열람)
[^aelab]: KAIST 항공우주공학과 연구실 소개 「Measurement Robotics & Diagnostic AI Lab」 <https://ae.kaist.ac.kr/boards/view/board_lab/81> (연구실명, 교수, 연구실 소개, 웹사이트, 이메일, Tel, Office, 연구분야, 2021-08-16 게시, 2026-10-23 열람)
[^aefac]: KAIST 항공우주공학과 교수진 목록 <https://ae.kaist.ac.kr/boards/lists/board_faculty/sc_category/1/> (이정률 항목의 직위, Career, Tel, Website, E-mail, 연구분야, 2026-10-23 열람)
[^p1]: K.-J. Lee, S.-C. Hong, S. Y. Rhee, J.-R. Lee, Structural Health Monitoring 24, 2648-2660 (2025). <https://doi.org/10.1177/14759217251326072> 초록 기준.
[^p2]: K.-J. Lee, J.-R. Lee, Advanced Composite Materials 34, 329-351 (2025). <https://doi.org/10.1080/09243046.2024.2372902> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Park, J.-R. Lee, International Journal of Aeronautical and Space Sciences 25, 460-467 (온라인 2023-12-15). <https://doi.org/10.1007/s42405-023-00691-4> 초록 기준(논문 페이지 게시 초록).
[^p4]: K. Kim, J.-H. Lee, Y.-J. Cho, J.-R. Lee, Advanced Composite Materials 34, 707-724 (온라인 2024-09-04). <https://doi.org/10.1080/09243046.2024.2398289> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: D.-H. Jin, D.-J. Park, J.-R. Lee, J.-M. Ahn, Journal of Sandwich Structures & Materials 26, 1288-1311 (온라인 2024-09-03). <https://doi.org/10.1177/10996362241278222> 초록 기준.
[^p6]: S. u. Din, J.-M. Hyun, D.-S. Son, J.-R. Lee, International Journal of Advanced Robotic Systems 19, 17298806221114554 (온라인 2022-07-29). <https://doi.org/10.1177/17298806221114554> 초록 기준.
[^p7]: H.-J. Lee, H. J. Shin, J.-R. Lee, International Journal of Aeronautical and Space Sciences 26, 2282-2307 (온라인 2025-03-02). <https://doi.org/10.1007/s42405-025-00905-x> 초록 기준.
[^p8]: J. Lee, C. C. Chia, J.-R. Lee, International Journal of Aeronautical and Space Sciences (온라인 2026-07-13). <https://doi.org/10.1007/s42405-026-01251-2> 초록 기준.

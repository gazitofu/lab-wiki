# 정밀 메카트로닉스 연구실 (Precision Mechatronics Laboratory, PML)

**KAIST 기계공학과 · 노민균 교수**

- 분야: 전동기와 액추에이터의 설계·해석(무베어링 모터, 매입형 영구자석 동기 전동기, 능동 자기 베어링, 선형 모터), 전동기 제어와 전력전자, 실시간 임베디드 제어 하드웨어, 자기 부상 혈액 펌프·드론용 자기 구동기·로봇 손 같은 메카트로닉스 시스템, 3D 프린팅 모터 부품, 모터 신호를 쓴 드론 프로펠러 고장 진단
- 대분야: 기계·로봇·제조, 전기전자·반도체·광학
- 태그: 제어 이론·제어 공학[^research][^p1][^p4], 진동·소음 공학[^research][^p2], 로봇 구동기·센서[^research], 전기차[^research][^past], 3D 프린팅[^past][^pubs], 고장 진단·수명 예측[^past][^pubs], 전동기·발전기 설계·구동 제어[^research], 실시간·임베디드 시스템[^research]
- 홈페이지: <https://pml.kaist.ac.kr/>
- 근거와 출처: [정밀 메카트로닉스 연구실 근거 페이지](pml-sources.md)

> 전동기와 자기 부상 장치 같은 전기기계 하드웨어와 그 제어를 처음부터 함께 설계하는 기계공학과 연구실이다. 기계식 베어링 없이 회전자를 자기력으로 띄운 채 돌리는 무베어링 모터, 계산 효율을 높인 전동기 자기장 해석, 센서 없는 자기 베어링 제어를 연구하고, 이를 혈액 펌프, 전기차, 드론, 로봇 손, 반도체 제조 장비로 잇는다.[^home][^research][^current]

## 무엇을 연구하나

누리집 첫 화면은 연구실이 기계 시스템, 전기기계(전기 에너지와 기계 운동을 서로 바꾸는 장치), 제어, 전자 회로를 아우르는 결정론적 공동 설계(deterministic co-design)로 새롭고 쓸모 있는 메카트로닉스 시스템을 만든다고 소개한다. 이때 제어를 위한 설계(design-for-control) 방식을 택해, 하드웨어를 먼저 설계하고 제어를 나중에 붙이는 대신 처음부터 제어를 고려해 되먹임 시스템 전체를 설계한다고 적는다. 정밀 메카트로닉스 연구를 미래 모빌리티, 로보틱스, 에너지 변환, 바이오메디컬, 첨단 제조 시스템 같은 산업 응용으로 잇는다고 밝힌다.[^home]

연구 페이지는 연구 갈래를 전기 기계와 액추에이터(Electric Machines & Actuators), 제어와 전력전자(Control & Power Electronics), 메카트로닉스와 로보틱스(Mechatronics & Robotics)의 셋으로 든다.[^research] Contact 페이지는 연구실의 일상적인 연구 활동을 세 가지로 든다. 전동기·액추에이터·로봇 같은 전기기계 시스템을 설계해 만드는 일, 전력전자 회로와 인쇄 회로 기판(PCB) 조립체 같은 전자 시스템을 설계해 만드는 일, 제어 알고리즘을 설계해 마이크로컨트롤러·FPGA 같은 실시간 계산 장치에 구현하는 일이다. 새 구성원을 위한 전동기 제어 입문 과정은 네 번의 실습으로 이루어진다. 첫 실습은 H-브리지 변환기(스위치를 켜고 끄는 조합으로 부하에 걸리는 전압의 방향을 바꾸는 회로)로 인덕터 전류를 제어하고, 마지막 실습은 3상 인버터와 엔코더 되먹임으로 영구자석 동기 전동기(PMSM)를 제어한다.[^contact]

기계공학과 교수진 목록과 교수 소개는 교수의 연구분야를 Electric motors and drives, Sensors and actuators, Control, instrumentation, and robotics로 적고, 학과 연구분야 페이지는 연구실을 「로보틱스/제어/모빌리티」 분야에 넣는다.[^melist][^meprof][^medept]

## 주요 연구 주제

### 1. 전동기와 액추에이터의 설계와 해석

에너지 변환과 운동 제어에 쓰이는 전기기계 시스템을 설계하고 해석하고 모형으로 만든다. 연구 페이지는 개발 대상으로 전기차용 매입형 영구자석(IPM) 동기 전동기, 히트펌프 압축기용 능동 자기 베어링(AMB), 혈액 펌프용 자기 부상 무베어링 모터, 소형 헬리콥터 드론용 스와시코일(swashcoil) 구동기, 반도체 제조용 고가속 선형 모터, 로봇 손용 고토크 밀도 모터를 든다. 전자기, 열, 구조 응력, 진동을 함께 다루는 계산 효율 높은 모형 도구를 유한요소, 회로 요소, 해석적 연속체 영역을 섞은 정식화로 만들고, 설계 쪽에서는 다상·다자유도 기계, 영구자석을 줄인 설계, 열관리와 제조성을 높인 액추에이터를 탐구한다고 적는다.[^research]

진행 중인 과제 가운데 고속 무베어링 모터 과제(NRF 지원)는 중·고출력 산업 응용을 위한 고속 무베어링 모터(회전자를 자기력으로 띄운 채 돌리는 모터 시스템)의 기초 연구로, 고속 회전에 맞는 새 회전자 구조, 다상 결합 권선, 계산 효율 높은 전자기 해석과 최적화, 전력전자와 제어 시스템 개발을 다룬다.[^current] 전동기 하이브리드 부분 영역 모형 과제(NRF 지원)는 기존 유한요소해석(FEA)에 비해 계산 효율을 크게 높이면서 오차를 받아들일 만한 수준으로 두는 전동기 전자기 해석 방법을 개발한다. 이 방법은 고정자와 회전자를 등가 자기 회로로 나타내고, 공극은 맥스웰 방정식의 연속 공간 해석해(수치 계산을 되풀이하지 않고 식을 풀어 수식 꼴로 얻은 답)로 나타낸다. 두 영역의 식은 하나의 결합 행렬 방정식으로 묶고, 자기 포화가 일으키는 비선형성은 반복 풀이로 반영한다. 과제 페이지는 이 방법이 FEA에 비해 60배 초과의 속도 향상과 약 3%의 평균 토크 오차를 얻는다고 적는다.[^current] 이 밖에 IPM 전동기 회전자의 계산 효율 높은 응력 해석(Hyundai Motors 지원)과 반도체 제조용 고가속 선형 스테이지(Samsung Electronics 지원) 과제가 있다.[^current] 대표 논문 1은 페라이트 자석을 넣은 IPM 무베어링 슬라이스 모터를 설계·제어해 부상과 회전을 실험으로 보였고, 대표 논문 2는 같은 종류 모터 회전자의 움직임을 4자유도 회전체 동역학 모형으로 분석했으며, 대표 논문 3은 IPM 동기 전동기의 자기장을 자기 회로와 공극 해석해를 묶어 빠르게 계산했다.[^p1][^p2][^p3]

### 2. 제어와 전력전자

전동기와 구동 시스템을 위한 제어와 전력전자를 연구한다. 연구 페이지에 따르면 제어 설계는 낮은 수준의 전류 조절부터 높은 수준의 운동 제어까지 걸치고, 루프 셰이핑, 상태·매개변수 추정, 다변수 제어, 비선형 제어 같은 모형 기반 방법에 바탕을 둔다. 주파수 영역 접근(시스템이 여러 주파수의 입력에 어떻게 반응하는지로 분석하는 방법)과 상태 공간 접근(시스템 안의 상태 변수와 그 변화를 나타내는 식으로 분석하는 방법)을 함께 쓰고, 디지털 제어와 신호 처리도 다룬다. 이 알고리즘을 구현하려고 전력전자, 센싱·계측 회로, 마이크로컨트롤러나 FPGA를 맞춤 PCB 조립체에 묶은 실시간 임베디드 플랫폼을 만든다. 이때 전력·신호 무결성(회로 안에서 전원 전압과 신호가 잡음이나 왜곡 없이 전달되는 정도)과 결정론적 타이밍(계산과 입출력이 늘 정해진 시점에 일어나게 하는 것)을 고려한다고 적는다.[^research]

자기 베어링의 센서 없는 제어 과제(KETEP 지원, LG electronics 등 협력)는 HVAC 칠러 같은 에너지 변환 시스템에 쓰이는 능동 자기 베어링을 다룬다. 과제 페이지는 기존 자기 베어링이 와전류 센서 같은 별도 센서로 회전자 위치를 재어 되먹임 제어를 하지만, 산업 협력사들이 히트펌프처럼 온도가 높은 환경에서 센서가 고장 나기 쉬운 점을 우려한다고 적고, 연구실이 별도 센서가 필요 없는 제어 방법을 개발한다고 밝힌다.[^current] 대표 논문 4는 전압 방정식과 사각파 전압 주입으로 센서 없이 회전자 위치를 추정했고, 특허 목록에는 능동 자기 베어링 시스템의 센서 없는 회전자 위치 추정 장치와 방법 국내 특허(2026년 7월)가 있다.[^p4][^pubs] 학회 논문 목록에는 6상 결합 권선을 쓴 12/8 무베어링 스위치드 릴럭턴스 모터의 부상 제어 논문(ECCE 2026 발표 채택)도 있다.[^pubs]

### 3. 메카트로닉스 시스템과 로봇

기구, 구동, 센싱, 제어를 한데 묶은 메카트로닉스 시스템과 로봇 플랫폼을 설계하고 만들어 실험으로 검증한다. 연구 페이지는 로봇 손, 자기 부상 시스템, 정밀 운동 스테이지, 전기 모빌리티 같은 물리 플랫폼 전체를 만든다고 적고, 하위 시스템이 서로 강하게 얽힌 되먹임 구조에서는 기계 시스템, 구동, 센싱, 제어 알고리즘을 차례로가 아니라 함께 설계해야 한다고 설명한다. 이 바탕 위에서 로봇 조작을 위한 학습 기반 제어와 피지컬 AI로 연구를 넓히고 있다고 밝힌다.[^research]

자기 부상 심폐 혈액 펌프 과제(KMDF 지원, Insung Medical·Samsung Medical Center 등 협력)는 무베어링 모터로 임펠러를 접촉 없이 띄워 돌리는 원심 혈액 펌프와 심폐 보조 장치의 지능형 운전 플랫폼을 개발한다. 과제 페이지는 기계적 접촉이 없어 마찰과 마모가 줄고 유량을 정밀하게 제어할 수 있다고 적고, 연구 내용으로 회전자·고정자의 전자기 설계, 전산유체역학(CFD)을 쓴 임펠러·하우징 최적화, 안정된 부상을 위한 고속 센싱과 되먹임 제어, 전력전자·실시간 제어 하드웨어 통합을 든다.[^current] 스와시플레이트 없는 소형 헬리콥터 드론 과제(KRIT·대전시 지원)는 헬리콥터가 날개 피치를 주기적으로 바꿔 자세와 움직임을 제어하는 데 쓰는 스와시플레이트가 소형 드론에는 부피가 크고 기계 구조가 복잡하다고 보고, 부피와 기계적 복잡도를 줄여 그 기능을 대신하는 새 자기 구동기를 개발한다.[^current]

양팔 이동 매니퓰레이터 과제(NRF 지원)는 제조 장비와 함께 일하며 공작물 다루기, 옮기기, 기계 관리 같은 장비 중심 작업을 하는 이동 로봇을 개발하고, 로봇 제어, 작업 계획, 인식, 기계 인터페이스를 통합해 여러 제조 공정을 오가며 스스로 일하는 유연한 자동화를 목표로 한다.[^current] 이 밖에 제조용 피지컬 AI를 위한 손재주 있는 로봇 손(NIPA 지원)과 정밀 안정화를 위한 다자유도 구동 시스템 제어(Hanwha Systems 지원) 과제가 있다.[^current] 첫 화면 소식은 2026년 2월 구성원 Junggeun과 Jaehyeon이 함께 쓴 학회 논문이 ICRA 2026에 채택됐다고 적는다.[^home]

### 4. 미래 모빌리티 요소 기술과 고장 진단

끝난 과제 가운데 KAIST 지원 미래 모빌리티 전기 구동계 요소 기술 과제(Sanha Kim, Hansohl Cho, Jeonyoon Lee 교수와 협력)는 3D 프린팅 전기 모터, 탄소 강화 고속 회전자, 설계 최적화를 위한 하이브리드 자기 회로 모형, 연속체 전기기계 모형 같은 요소 기술을 개발했다. 과제 페이지는 철 입자를 많이 넣은 고분자 필라멘트를 압출 적층해 축방향 자속 모터의 고정자를 만든 학술지 논문(Additive Manufacturing, 2026년)과 자성 조성이 다른 필라멘트로 모터 부품을 압출 3D 프린팅한 학회 발표(2023년)를 이 과제에 묶는다. Publications 페이지는 이 학술지 논문의 저자로 교수와 함께 K. Kim, J. Kong, M. Choi를 적고, 첫 화면 소식은 이를 구성원 Kangyeon의 논문(Jikang, Minyoung 공저)으로 알렸다.[^past][^pubs][^home] Hyundai Motors 지원의 전기차 구동 모터(EV traction motor) 하이브리드 자기 회로 모형 과제도 끝난 과제로 적혀 있다.[^past]

드론 프로펠러 시스템의 센서 없는 감시 과제(NST 지원, KARI·KITECH 협력)는 전자 변속기, 브러시리스 직류(BLDC) 모터, 프로펠러로 이루어진 드론 프로펠러 시스템에서 모형 기반 추정과 기계학습 알고리즘을 결합해, 실시간으로 잰 모터 전압과 전류로 프로펠러의 마모나 파손 같은 손상을 알아내는 센서 없는 감시 시스템을 개발하는 과제다.[^past] 논문 목록에는 모터 신호와 생성 모형 기반 준지도 학습으로 전기 추진 항공기의 프로펠러 고장을 찾는 학술지 논문(2025년)과 전기 신호 기반 생성 모형으로 프로펠러 상태 이상을 찾는 학회 논문(2024년)이 있다.[^pubs] 이 밖에 KAIST 지원 과제(Heejin Ahn 교수와 협력)로, 자율주행 시스템의 사회적 수용성을 높이려는 스마트 시티 시험장 과제의 일부로서 교차로에서 여러 차량을 조정하는 중앙 제어기와 통신하는 15:1 축소 자율주행차를 개발한 과제가 있다.[^past] 대표 논문 5는 구성원 Jikang Kong이 참여한 공동 연구로, 받침 매질 속에 액체 잉크를 짜 넣는 매립형 3D 프린팅에서 실리콘 오일과 액체 금속을 안정되게 찍는 조건을 밝혔다.[^p5]

## 대표 논문

노민균 교수가 2022년 8월 KAIST에 연구실을 연 뒤에 나온 2025–2026년 논문 가운데 초록을 확인할 수 있는 다섯 편을 연구 갈래에 고르게 담도록 골랐다. 표는 전동기와 액추에이터의 설계·해석(대표 논문 1–3), 자기 베어링 제어(대표 논문 4), 3D 프린팅 공동 연구(대표 논문 5)를 다루며, 드론 프로펠러 고장 진단과 3D 프린팅 모터 고정자 학술지 논문은 포함하지 않는다. 대표 논문 1과 5는 학술지 논문이고 2–4는 학회 논문이다. 대표 논문 1은 누리집 목록이 「accepted, 2026」으로 적고 저자 T. Loutit과 J. Kim(Jungha Kim)에 †를 붙였으며, 학술지 기록에는 2026년 8월 31권 4호로 실려 있다. 대표 논문 5에서 교수는 5명 가운데 넷째 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [Design, Modelling, and Control of a Bearingless Slice Motor with a Ferrite-based Interior Permanent Magnet Rotor](https://doi.org/10.1109/tmech.2026.3719707) · IEEE/ASME Transactions on Mechatronics | 페라이트 자석을 넣은 새 매입형 영구자석(IPM) 무베어링 슬라이스 모터(얇은 원판 모양 회전자를 자기력으로 띄운 채 돌리는 모터)를 설계하고 모형으로 만들고 제어했다. 자기적으로 방향에 따라 성질이 다른 페라이트 IPM 회전자를 써서, 페라이트 자석이 내는 작은 자석 정렬 토크를 릴럭턴스 토크(회전자 방향에 따라 자기 저항이 달라 생기는 토크)로 보탰다. 그러면 토크를 내는 전류와 부상력을 내는 전류가 비선형으로 얽히는데, 이를 다루려고 토크 전류가 부상력에 미치는 영향을 드러내는 다상 dq 좌표계 힘·전류 모형을 유도했다. 바이어스 전류를 바꾸는 전략과 힘·전류 관계를 거꾸로 푼 대응(inverse mapping)으로 자석 자속이 약해도 안정된 수동 부상을 얻었다. 시제품을 만들어 실험한 결과 최대 11 500 r/min에서 안정된 자기 부상과 회전을 얻었다.[^p1] | 첫 저자 T. Loutit(Taryn E. Loutit), 둘째 저자 J. Kim(Jungha Kim)(두 사람에게 누리집 표시 †), 마지막 저자 노민균 (5명) |
| 2 | 2026 | [4-DOF rotor dynamics of an interior permanent magnet bearingless slice motor](https://doi.org/10.23919/ipec-nagasaki2026-ec64663.2026.11596787) · 2026 IPEC-Nagasaki (ECCE Asia) 학회 논문집 | 무베어링 슬라이스 모터 회전자의 4자유도 회전체 동역학 모형을 만들고 실험으로 검증했다. 이 모형은 Jeffcott 회전자 모형을 넓혀 평행 이동과 회전 면 밖으로 기우는 각운동을 담았다. 모형으로 여러 회전 속도에서 근궤적 분석을 해 휘돌림(whirl) 진동수를 찾고, 회전자 비대칭에 대한 동기 응답의 특성을 밝혔다. 페라이트 IPM 쌍극자 회전자를 쓴 시제품 실험에서, 잰 휘돌림 진동수는 근궤적 분석과 맞게 속도에 따라 옮겨 갔고, 잰 반경 방향 변위는 예측한 동기 응답과 잘 맞았다.[^p2] | 1저자 J. Kim(Jungha Kim), 마지막 저자 노민균 (2명) |
| 3 | 2025 | [Hybrid magnetic circuit modeling for interior permanent magnet synchronous motors](https://doi.org/10.1109/ecce58356.2025.11260068) · 2025 IEEE ECCE 학회 논문집 | 매입형 영구자석 동기 전동기(IPMSM)의 새 모형화 방법을 제시했다. 고정자와 회전자는 이산 공간의 자기 회로로, 공극은 연속 공간 영역으로 다루고, 두 영역을 경계 조건으로 이어 하나의 확장 행렬 방정식으로 함께 풀었다. 이 방법으로 여러 운전 조건에서 IPMSM의 자기장을 해석할 수 있다. 공극 자속 밀도와 토크 리플(토크가 회전하며 오르내리는 변동) 결과는 유한요소해석(FEA)과 잘 맞았고, 평균 토크의 상대 오차는 8% 미만, 계산 속도는 FEA의 약 9.85배였다.[^p3] | 1저자 K. Kim(Kangyeon Kim), 마지막 저자 노민균 (3명) |
| 4 | 2025 | [Sensorless position estimator for active magnetic bearings based on non-linear voltage equation and square-wave voltage injection](https://doi.org/10.1109/iemdc60492.2025.11061164) · 2025 IEEE IEMDC 학회 논문집 | 능동 자기 베어링을 위한 새 센서 없는 위치 추정기를 제시했다. 추정 알고리즘의 중심은 전압 방정식을 그대로 이산화해 얻은 1차 비선형 유한 차분 방정식이고, 나이퀴스트 주파수의 사각파 전압을 더 주입해 추정 성능을 높였다. 모의실험과 하드웨어 시험으로 성능을 확인했고, 5 kHz 샘플링 주파수에서 잰 위치 반복도는 6.41 μm로 믿을 만한 부상 제어를 할 수 있었다.[^p4] | 1저자 M. Choi(Minyoung Choi), 마지막 저자 노민균 (3명) |
| 5 | 2025 | [Embedded 3D printing of newtonian fluids in elasto-viscoplastic matrix](https://doi.org/10.1021/acsami.5c16150) · ACS Applied Materials & Interfaces | 매립형 3D 프린팅(EM3D)은 항복 응력이 있는 받침 매질 속에 잉크를 짜 넣어 부드러운 재료로 자유로운 모양을 찍는다. 뉴턴 유체 잉크는 바늘이 움직이며 매질을 항복시키는 문제와 계면 장력이 일으키는 Rayleigh-Plateau(RP) 불안정성 때문에 찍기 어렵다. 이 논문은 표면 장력이 매우 낮은 실리콘 오일과 매우 높은 Galinstan 액체 금속을 탄성-점소성 Laponite 매질 속에 찍었다. 입자 영상 유속계로 흐름을 보아 바늘 둘레의 매질 항복이 특성 전단율과 항복 기준의 비의 1/3제곱에 비례함을 밝혔고, 곧은 바늘의 직각 방향으로 찍으면 항복이 심해져 인쇄 정확도가 떨어짐을 보였다. 이를 풀려고 굽은 바늘 형상을 제안해 항복 영역을 줄이고 필라멘트 안정성을 높였다. RP 불안정성에 대해서는 계면 장력과 항복 응력의 균형으로 안정 기준을 이론으로 유도하고, 계면 장력이 다른 두 잉크(실리콘 오일 35 mN/m, Galinstan 345 mN/m)로 실험 검증했다. 저자들은 이 결과가 연성 전자 소자와 바이오프린팅에서 뉴턴 잉크를 믿을 만하게 찍는 실용 지침이 된다고 적는다.[^p5] | 1저자 H. Jun(Hyejoon Jun), 넷째 저자 노민균, 마지막 저자 H. Kim(Hyoungsoo Kim) (5명) |

## 교수와 전문 분야

노민균 교수는 KAIST 기계공학과 조교수다(2022년부터).[^prof][^people] 교수 소개 페이지는 겸직으로 KAIST Institute for Robotics(2022년부터), Cho Chun Shik Graduate School of Mobility(2023년부터), Department of AX, School of AI(2026년부터)의 Joint-appointment Professor, KAIST Robotics Program의 Affiliated Professor(2024년부터), UBC(University of British Columbia) 기계공학과의 Affiliate Assistant Professor(2022년부터)를 적는다.[^prof] 첫 화면 소식은 교수가 2022년 8월 KAIST에 연구실을 열었다고 적는다.[^home]

교수 소개 페이지에 따르면 서울대학교(SNU)에서 기계항공공학(Mechanical & Aerospace Engineering) 학사(2012년, 지도 교수 Kyu-jin Cho, Summa cum laude), MIT에서 기계공학 석사(SM, 2014년)와 박사(PhD, 2018년)를 받았다. 두 학위 모두 지도 교수는 David L. Trumper이고, 박사 과정의 주전공은 Mechatronics, 부전공은 Signal processing이다. 박사 학위 논문은 「Homopolar bearingless slice motors with magnet-free rotors for extracorporeal life support」, 석사 학위 논문은 「Hydraulically controlled magnetic bougienage for correction of long-gap esophageal atresia」다. MIT Research Laboratory of Electronics의 Precision Motion Control Laboratory에서 Research Assistant(2012–2018년), MIT Kavli Institute for Astrophysics and Space Research의 LIGO Laboratory에서 Postdoctoral Associate(2018–2019년), UBC 기계공학과 조교수(2019–2022년)를 지냈다.[^prof] 기계공학과 교수 소개는 최종학위를 Ph.D., MIT (2018)로 적는다.[^meprof][^melist]

교수 소개 페이지의 수상 칸은 KAIST 기계공학과 우수강의상(「시스템 모델링 및 제어」, 2023년 ME361, 2025년 ME.30061), 제어·로봇·시스템학회 우수신진연구자상(2023년), KAIST Impact Research Award(2023년), 대한기계학회 동역학·제어·로봇 부문 유망과학기술자상(2024년), 한국정밀공학회 젊은공학자상(2025년)을 적는다. MIT 시기의 상으로는 3rd ASPE Annual Student Challenge First Place Winner(2016년), NI Engineering Impact Awards Advanced Research Winner(2017년), MIT 기계공학과의 Wunsch Foundation Silent Hoist and Crane Award와 Sontheimer Travel Award(2018년)를 적는다.[^prof]

Past Projects 페이지에는 지원 기관이나 협력 기관이 UBC, MIT, 서울대학교 연구실인 과제도 있다. UBC·NSERC·CFI 지원 고속 무베어링 모터 과제는 와이드 밴드갭 전력 소자와 FPGA 제어기를 쓴 다상 전력전자, 자석이 없거나 자석을 줄인 회전자와 다상 권선을 쓴 새 모터 구조, 최적 설계와 모형 기반 제어를 위한 전기기계 모형을 다뤘다. MIT와 관련된 과제는 NSF 지원의 중력파 관측소(LIGO) 능동 파면 제어용 피에조 구동 변형 거울, NIH·Samsung Scholarship 지원의 회전체에 영구자석이 없는 자기 부상 무베어링 혈액 펌프, MIT Lincoln Laboratory 지원의 위성 자세 제어용 쌍극자 자석 반작용 구(reaction sphere), DARPA 지원의 장기 칩 미세유체 장치용 정전용량 액면 감지와 되먹임 제어, Samsung Scholarship 지원의 긴 간격 식도 폐쇄증(long-gap esophageal atresia)을 덜 침습적으로 교정하는 자석 끝 카테터 연구다. 서울대학교 Biorobotics Laboratory와 협력한 NRF 지원 과제는 형상 기억 합금 스프링을 쓴 벼룩 모사 점프 로봇 연구다.[^past]

기계공학과 페이지가 적는 연구분야는 전동기와 구동, 센서와 액추에이터, 제어·계측·로보틱스다.[^melist][^meprof] 2021–2026년 논문으로 보면 KAIST에서의 전문 분야는 무베어링 모터를 비롯한 전동기의 설계·해석과 자기 부상 제어로, 페라이트 IPM 무베어링 슬라이스 모터의 설계와 제어(대표 논문 1), 회전체 동역학(대표 논문 2), 계산 효율 높은 전동기 자기장 해석(대표 논문 3), 자기 베어링의 센서 없는 위치 추정(대표 논문 4)에 걸친다.[^p1][^p2][^p3][^p4]

## 응용 분야

첫 화면은 응용 분야로 미래 모빌리티, 로보틱스, 에너지 변환, 바이오메디컬, 첨단 제조 시스템을 든다.[^home] 연구 페이지와 과제 페이지가 적는 대상은 전기차 구동 모터, 히트펌프 압축기와 HVAC 칠러의 자기 베어링, 심폐 보조 장치의 혈액 펌프, 소형 헬리콥터 드론, 반도체 제조용 선형 스테이지, 로봇 손과 제조용 이동 매니퓰레이터, 정밀 안정화 장치, 드론 프로펠러 감시다. 과제 지원·협력 기관에는 Samsung Electronics, Hyundai Motors, Hanwha Systems, LG electronics, Insung Medical이 있다.[^research][^current][^past]

## 구성원

People 페이지 Graduate Students 칸의 13명과 Undergraduate Students 칸의 3명, 모두 16명이다. 대학원생은 PhD Candidate 2명, PhD Student 5명, MS Student 6명이며, PhD Candidate와 PhD Student는 모두 「박사과정」으로 적었다. 학부생 카드의 과정 줄은 「BS Student, Mechancial Engineering, KAIST」로 적혀 있어 「학부 연구생」으로 적었다. 이메일은 대학원생 카드의 E-mail 연결 주소이고 학부생 카드에는 이메일이 없다. 카드는 학력(학위, 학교, 연도)과 연구실 호수(N7-2212)도 적는다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Sungwon Cho (조성원) | 박사과정 | bruce1206@kaist.ac.kr | 3 |
| Jikang Kong (공지강) | 박사과정 | brrandon13@kaist.ac.kr | 5 |
| Kangyeon Kim (김강연) | 박사과정 | cozypond@kaist.ac.kr | 3 |
| Minyoung Choi (최민영) | 박사과정 | minong2@kaist.ac.kr | 4 |
| Jungha Kim (김중하) | 박사과정 | kjh0703@kaist.ac.kr | 1, 2 |
| Sangwoo Shin (신상우) | 박사과정 | ssw990907@kaist.ac.kr |  |
| Seungwon Yun (윤승원) | 박사과정 | laswyun1@kaist.ac.kr |  |
| Daeyong Kim (김대용) | 석사과정 | daeyong521@kaist.ac.kr | 4 |
| Junggeun Seo (서정근) | 석사과정 | sjg12044@kaist.ac.kr |  |
| Beomsu Kim (김범수) | 석사과정 | 3618kbs0306@kaist.ac.kr |  |
| Hohyeon Byeon (변호현) | 석사과정 | hbyeon@kaist.ac.kr |  |
| Taekwon Choe (최태권) | 석사과정 | tkchoe@kaist.ac.kr |  |
| Hosung Doh (도호성) | 석사과정 | star_doh@kaist.ac.kr |  |
| Juhyun Ha (하주현) | 학부 연구생 |  |  |
| Seungheon Jeon (전승헌) | 학부 연구생 |  |  |
| Bosung Kwon (권보성) | 학부 연구생 |  |  |

## 졸업생과 이전 구성원

People 페이지 Alumni 칸의 7명 전부다. 카드는 이름, 현재 직위와 소속, 학위 줄(학위, 학과, 학교, 연도)을 적는다. 표의 학위·과정은 카드의 첫 학위 줄이고, 진로 칸은 카드의 현재 직위·소속 줄 그대로다. Eungjoe Kang 카드에는 현재 직위·소속 줄이 없다. 학위 줄의 학교가 UBC(University of British Columbia)인 4명이 함께 적혀 있으며, 교수 소개 페이지는 교수가 2019–2022년 UBC 기계공학과 조교수였고 2022년부터 같은 학과의 Affiliate Assistant Professor라고 적는다.[^people][^prof]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jaehyeon Kim (김재현) | MS in Mechanical Engineering, KAIST (2026) | Researcher, Rainbow Robotics |
| Ouyang (Stanley) Chen | MASc, Mechanical Engineering, UBC (2023) | Researcher, Planar Motors, Inc. |
| Yeongheon Kim (김영헌) | MS, Mechanical Engineering, KAIST (2025) |  |
| Eungjoe Kang (강응조) | BS, Mechanical Engineering, KAIST (2025) |  |
| Taryn Loutit | MASc, Mechanical Engineering, UBC (2022) | PhD Candidate, Mechanical Engineering, MIT |
| Simon Szoke | MASc, Mechanical Engineering, UBC (2022) | Researcher, Phillips Lightening |
| Hosam Ibrahim | MASc, Mechanical Engineering, UBC (2023) | Researcher, Planar Motors, Inc. |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지의 Journal Papers와 Conference Papers 가운데 연도가 2021–2026년인 17편이다. 학술지 논문 7편(2026년 2편, 2025년 2편, 2022년 1편, 2021년 2편)과 학회 논문 10편(2026년 3편, 2025년 2편, 2024년 1편, 2023년 2편, 2022년 2편)이고, 연도마다 학술지 논문을 먼저 적었다. 저자 순서와 제목·학술지·학회 표기는 페이지 그대로이며, 저자 이름 뒤 †와 *는 페이지가 적은 표시다.[^pubs]

- 2022년 학술지 논문 1편과 2021년 학술지 논문 2편은 페이지가 연도 구역이 아니라 「Prior Publications」 구역에 둔 논문이고, 연도는 줄 끝의 출판 연도다. 교수는 2022년 8월 KAIST에 연구실을 열었다. Past Projects 페이지는 이 가운데 2편(Optics Express 2022, IEEE Transactions on Industry Applications 2021)과 2022–2023년 학회 논문 4편을 협력 기관이나 지원 기관에 MIT 또는 UBC가 적힌 과제(NSF 지원 변형 거울, NIH·Samsung Scholarship 지원 혈액 펌프, UBC·NSERC·CFI 지원 고속 무베어링 모터)의 논문으로 묶는다.[^pubs][^past][^home]
- 2026년 IEEE/ASME Transactions on Mechatronics 논문은 페이지가 「accepted, 2026」으로 적은 게재 승인 논문이고, 첫 화면 소식은 2026년 7월에 승인을 알렸다. 학술지 기록에는 2026년 8월 31권 4호로 실려 있다.[^pubs][^home][^p1]
- 2026년 ECCE 학회 논문 2편은 첫 화면이 2026년 5월에 채택을 알린 논문이고, 페이지는 학회 이름과 개최지·시기(Vancouver, Canada, Oct. 2026)로 적는다. 두 줄 끝에 「ECCE 2026 발표 채택」으로 표시했다.[^pubs][^home]

**2026**

- T. Loutit†, J. Kim†, O. Chen, J. Kim, and M. Noh. "Design, Modelling, and Control of a Bearingless Slice Motor with a Ferrite-based Interior Permanent Magnet Rotor". *IEEE/ASME Transactions on Mechatronics, accepted, 2026*.
- T. Kim†, H. Je†, K. Kim†, H. Jun, J. Kong, M. Choi, H. Kim, M. Noh\*, and S. Kim\*. "Material extrusion additive manufacturing of high iron particle loaded polymer filaments for axial flux motor stator". *Additive Manufacturing, vol. 127, Art. no. 105275, 2026*.
- S. Cho and M. Noh. "Coupled finite element and analytical subdomain modeling of surface-mounted permanent magnet synchronous motors". *2026 IEEE Energy Conversion Congress and Exposition (ECCE), Vancouver, Canada, Oct. 2026 (ECCE 2026 발표 채택)*.
- J. Kim and M. Noh. "Levitation control of a 12/8 bearingless switched reluctance motor with six-phase combined windings". *2026 IEEE Energy Conversion Congress and Exposition (ECCE), Vancouver, Canada, Oct. 2026 (ECCE 2026 발표 채택)*.
- J. Kim and M. Noh. "4-DOF rotor dynamics of an interior permanent magnet bearingless slice motor". *2026 International Power Electronics Conference (IPEC-Nagasaki 2026 - ECCE Asia), Nagasaki, Japan, May 2026*.

**2025**

- S. Lee, D. Kim, M. Noh, S. Jeong, J. Kong, and Y. Yoo. "Propeller fault-detection method for electric-propulsion aircraft using motor signals and generative model-based semi-supervised learning". *Engineering Applications of Artificial Intelligence, vol. 162, Part A, pp. 112301, Dec. 2025*.
- H. Jun, J. Ryu, J. Kong, M. Noh, and H. Kim. "Embedded 3D printing of newtonian fluids in elasto-viscoplastic matrix". *ACS Applied Materials & Interfaces, vol. 17, no. 47, pp. 65281–65289, Nov. 2025*.
- K. Kim, S. Cho, and M. Noh. "Hybrid magnetic circuit modeling for interior permanent magnet synchronous motors". *2025 IEEE Energy Conversion Congress and Exposition (ECCE), Philadelphia, PA, Oct. 2025*.
- M. Choi, D. Kim, and M. Noh. "Sensorless position estimator for active magnetic bearings based on non-linear voltage equation and square-wave voltage injection". *2025 IEEE International Electric Machines and Drives Conference (IEMDC), Houston, TX, May 2025 (Best Student Oral Presentation Award)*.

**2024**

- D. Kim, J. Kong, M. Noh, S. Jeong, and S. Lee. "Training an electric signal-based generative model for anomaly detection in propeller condition diagnosis". *Asia Pacific International Symposium On Aerospace Technology (APISAT 2024), Adelaide, Australia, Oct. 2024, pp. 874 - 881*.

**2023**

- H. Ibrahim, R. Nagamune, and M. Noh. "FPGA-based multi-phase motor control platform for bearingless motor research". *2023 IEEE Energy Conversion Congress and Exposition (ECCE), Nashville, TN, Oct. 2023, pp. 5250–5257*.
- O. Chen, R. Nagamune, and M. Noh. "Self-excitation and speed hysteresis of a bearingless slice motor". *2023 IEEE Energy Conversion Congress and Exposition (ECCE), Nashville, TN, Oct. 2023, pp. 3899–3905*.

**2022**

- V. Srivastava, G. Mansell, C. Makarem, M. Noh, R. Abbott, S. Ballmer, G. Billingsley, A. Brooks, H. T. Cao, P. Fritschel, D. Griffith, W. Jia, M. Kasprzack, M. MacInnis, S. Ng, L. Sanchez, C. Torrie, P. Veitch, and F. Matichard. "Piezo-deformable mirrors for active mode matching in advanced LIGO". *Optics Express, vol. 30, no. 7, pp. 10491-10501, Mar. 2022*.
- T. Loutit and M. Noh. "Design of a dipole internal permanent magnet bearingless motor for flux-weakening control". *2022 IEEE Energy Conversion Congress and Exposition (ECCE), Detroit, Oct. 2022, pp. 1-8*.
- S. Szkoe and M. Noh. "Homopolar bearingless slice motor with quadruple three-phase windings". *2022 IEEE Energy Conversion Congress and Exposition (ECCE), Detroit, Oct. 2022, pp. 1-6*.

**2021**

- B. S. Weinreb, M. Noh, D. C. Fyler, and D. L. Trumper. "Design and implementation of a novel interior permanent magnet bearingless slice motor". *IEEE Transactions on Industry Applications, vol. 57, no. 6, pp. 6774–6782, Nov/Dec. 2021*.
- J. Y. Yoon†, M. Noh†, and D. L. Trumper. "Duffing oscillation and jump resonance: spectral hysteresis and input-dependent resonance shift". *Precision Engineering, vol. 70, pp. 63–69, Jul. 2021*.

## 특허

Publications 페이지 Patents 칸 7건 가운데 줄 끝 날짜가 2021년 10월 13일 이후인 3건이다(2022년 7월–2026년 7월). 줄 앞 날짜는 줄 끝 날짜이고, 발명자·제목·번호는 페이지 표기 그대로다. 미국 특허 2건은 발명자에 D. L. Trumper(교수 소개 페이지가 적은 MIT 박사 지도교수)가 함께 적힌 특허이고, 2026년 국내 특허는 능동 자기 베어링의 센서 없는 회전자 위치 추정 장치와 방법이다.[^pubs][^prof]

- 2026-07-10 · D. Kim and M. Noh, "Apparatus and Method for Sensorless Rotor Position Estimation in Active Magnetic Bearing System," Republic of Korea Patent, 10-2991529, Jul. 10, 2026.
- 2023-09-05 · M. Bhushan, D. Rathbone, D. L. Trumper, M. Noh, and J. Yoon, "Pumps and hardware for organ-on-chip platforms," U.S. Patent 11,749,437, Sep. 5, 2023.
- 2022-07-05 · M. Gartner, M. Noh, and D. L. Trumper, "Adult and pediatric extracorporeal life support system with heparin treated oxygenator surface and magnetic levitation motor," U.S. Patent 11,376,413, Jul. 5, 2022.

## 연구 과제

Current Projects 페이지의 10건과 Past Projects 페이지 11건 가운데 지원 기관이 KAIST, Hyundai Motors, NST(국가과학기술회)인 4건, 모두 14건이다. 과제 이름과 지원 기관(Sponsor), 협력 기관(Collaborators)은 페이지 표기 그대로이고, 페이지는 과제 기간을 적지 않는다. Past Projects 페이지의 나머지 7건은 지원 기관이나 협력 기관이 UBC, MIT, 서울대학교 연구실인 과제라 이 목록에 넣지 않고 「교수와 전문 분야」에 적었다.[^current][^past]

- Magnetically Levitated Cardiopulmonary Blood Pump (지원 KMDF (범부처의료기기연구개발사업단); 협력 기관 Insung Medical, Samsung Medical Center, KIMM, LOTCES, K-MEDI hub; 상태 Current Projects)
- High-speed Bearingless Motors (지원 NRF (한국연구재단); 상태 Current Projects)
- Hybrid Sub-domain Modeling of Electric Motors (지원 NRF (한국연구재단); 상태 Current Projects)
- Sensorless Control of Magnetic Bearings (지원 KETEP (한국에너지기술평가원); 협력 기관 LG electronics, Chungnam National Univ, Soongsil Univ, Yonsei Univ, Postech, KIER; 상태 Current Projects)
- Swashplate-less Miniature Helicopter Drones (지원 KRIT (국방기술진흥연구소), Daejeon City (대전시); 협력 기관 Chungnam National Univ and Daejeon Technopark; 상태 Current Projects)
- Dual-Arm Mobile Manipulation for Autonomous Manufacturing (지원 NRF (한국연구재단); 상태 Current Projects)
- Dexterous Robot Hands for Manufacturing Physical AI (지원 NIPA (정보통신산업진흥원); 상태 Current Projects)
- High-acceleration Linear Stages for Semiconductor Manufacturing (지원 Samsung Electronics; 상태 Current Projects)
- Computationally Efficient Rotor Stress Analysis for IPM Motors (지원 Hyundai Motors; 상태 Current Projects)
- Control of multi-DOF actuation systems for precision stabilization (지원 Hanwha Systems; 상태 Current Projects)
- Miniature Autonomous Vehicles (지원 KAIST; 협력 기관 Prof. Heejin Ahn; 상태 Past Projects)
- Hybrid Magnetic Circuit Modeling of EV Traction Motors (지원 Hyundai Motors; 상태 Past Projects)
- Elementary Technologies for Future Mobility Advanced Electric Powertrain (지원 KAIST; 협력 기관 Profs. Sanha Kim, Hansohl Cho, Jeonyoon Lee; 상태 Past Projects)
- Sensorless Monitoring of Drone Propeller Systems (지원 NST (국가과학기술회); 협력 기관 KARI and KITECH; 상태 Past Projects)

## 수상

첫 화면 News에서 수상 소식으로 올라온 2023년 3월–2026년 3월의 6건이다. 교수 수상 5건과 구성원 수상 1건이며, 날짜는 소식 글의 날짜이고 문구는 누리집 영어 표기 그대로다.[^home]

- 2026-03-31 · Prof. Noh received the Outstanding Teaching Award from KAIST ME.
- 2025-11-13 · Prof. Noh received the KSPE Young Engineer Award.
- 2025-05-22 · Minyoung received the Best Student Oral Presentation Award from IEMDC 2025. Congratulations!
- 2023-12-26 · Prof. Noh received the Impact Research Award from KAIST.
- 2023-06-22 · Prof. Noh received the Outstanding Early Career Researcher Award from ICROS 2023.
- 2023-03-30 · Prof. Noh received the Outstanding Teaching Award from KAIST ME.

## 소식

첫 화면 News의 2022년 8월–2026년 7월 글 29건이다(수상 소식은 위 수상 목록에 따로 적는다). 연구실 개설, 새 구성원, 학위 취득, 논문 채택, 학회 발표, 초청 강연과 강의 소식이다. 날짜는 연도 제목과 글 앞 (월/일) 표기를 합친 것이고, 문구는 누리집 표기 그대로다.[^home]

- 2026-07-31 · Jungha's journal paper, co-authored by Jaehyun, was accepted to IEEE/ASME Transactionn on Mechatronics. Congratulations!
- 2026-06-23 · Kangyeon's journal paper, co-authored by with Jikang and Minyoung, was accepted to Additive Manufacturing. Congratulations!
- 2026-06-02 · Jungha gave an oral presentation at the IPEC 2026-ECCE Asia, Nagasaki, Japan.
- 2026-05-22 · Jaehyun's conference paper was accepted to the ECCE 2026. Congratulations!
- 2026-05-22 · Sungwon's conference paper was accepted to the ECCE 2026. Congratulations!
- 2026-02-01 · A conference paper co-authored by Junggeun and Jaehyeon was accepted to ICRA 2026. Congratulations!
- 2026-01-30 · Jungha's conference paper was accepted to the IPEC 2026-ECCE Asia. Congratulations!
- 2026-01-12 · Seungwon joined the PML.
- 2025-10-30 · A journal paper co-authored by with Jikang was accepted to ACS Applied Materials & Interfaces. Congratulations!
- 2025-10-19 · Kangyeon gave poster presentation at the ECCE 2025, Philadelphia.
- 2025-09-10 · A journal paper co-authored by with Jikang was accepted to Engineering Applications of Artificial Intelligence. Congratulations!
- 2025-08-18 · Beomsu joined the PML.
- 2025-08-08 · Prof. Noh gave a lecture at the KSDO's Summer Workshop.
- 2025-07-07 · Sangwoo joined the PML.
- 2025-05-25 · Kangyeon's conference paper, co-authored by Sungwon, was accepted to the ECCE. Congratulations!
- 2025-02-24 · Daeyong and Junggeun joined the PML.
- 2025-02-14 · Kangyeon, Minyoung, and Yeoungheon received their MS degrees.
- 2025-01-28 · Minyoung's conference paper, co-authored by with Daeyong, was accepted to the IEMDC 2025. Congratulations!
- 2024-11-07 · Prof. Noh gave an invited talk at the KSME's Promising Scientists and Engineers session.
- 2024-10-20 · Prof. Noh gave a bearingless motor tutorial at the ECCE 2024, Phoenix.
- 2024-08-31 · Jikang received the MS degree.
- 2024-07-03 · Jikang and Minyoung presented posters at the ICROS 2024, Daejeon.
- 2024-02-26 · Sungwon and Jaehyun joined the PML.
- 2023-10-29 · Prof. Noh gave an oral and poster presentations at the ECCE 2023, Nashville.
- 2023-10-20 · Prof. Noh gave a Keynote Speech at the ICMT 2023, Busan.
- 2023-08-28 · Jungha and Nicola joined the PML.
- 2023-02-27 · Kangyeon, Minyoung, and Yeoungheon joined the PML.
- 2022-08-29 · Jikang joined the PML.
- 2022-08-01 · Prof. Noh founded the PML at KAIST.

## 연락과 위치

- 위치: 교수실 Mechanical Engineering Building (N7), Room 4203(연구실 누리집), 기계동(N7) 4203(기계공학과 교수 소개), 연구실 Mechanical Engineering Building (N7), Room 2212[^contact][^meprof]
- 주소: KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea[^contact]
- 전화: 교수 +82-42-350-3021, 연구실 +82-42-350-3061[^contact]
- 교수 이메일: minkyun.noh@kaist.ac.kr[^contact][^meprof]
[^p1]: T. E. Loutit 외, M. Noh, IEEE/ASME Transactions on Mechatronics 31, 4283-4294 (2026). <https://doi.org/10.1109/tmech.2026.3719707> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J. Kim, M. Noh, 2026 International Power Electronics Conference (IPEC-Nagasaki 2026 - ECCE Asia), 1-6 (2026). <https://doi.org/10.23919/ipec-nagasaki2026-ec64663.2026.11596787> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: K. Kim, S. Cho, M. Noh, 2025 IEEE Energy Conversion Conference Congress and Exposition (ECCE), 1-6 (2025). <https://doi.org/10.1109/ecce58356.2025.11260068> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: M. Choi, D. Kim, M. Noh, 2025 IEEE International Electric Machines & Drives Conference (IEMDC), 1238-1243 (2025). <https://doi.org/10.1109/iemdc60492.2025.11061164> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: H. Jun 외, H. Kim, ACS Applied Materials & Interfaces 17, 65281-65289 (온라인 2025-11-07). <https://doi.org/10.1021/acsami.5c16150> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 정밀 메카트로닉스 연구실 누리집 첫 화면 <https://pml.kaist.ac.kr/> (연구실 소개 문장, News 2022–2026, 2026-10-23 열람)
[^research]: 연구실 누리집 Research 페이지 <https://pml.kaist.ac.kr/research> (Electric Machines & Actuators, Control & Power Electronics, Mechatronics & Robotics, 2026-10-23 열람)
[^current]: 연구실 누리집 Research 메뉴 Current Projects 페이지 <https://pml.kaist.ac.kr/research/current-projects> (과제 설명, Sponsor, Collaborators, 과제별 논문, 2026-10-23 열람)
[^past]: 연구실 누리집 Research 메뉴 Past Projects 페이지 <https://pml.kaist.ac.kr/research/past-projects> (과제 설명, Sponsor, Collaborators, 과제별 논문·특허, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publications 페이지 <https://pml.kaist.ac.kr/publications> (Journal Papers, Conference Papers, Patents; 목록 범위는 근거 페이지, 2026-10-23 열람)
[^people]: 연구실 누리집 People 페이지 <https://pml.kaist.ac.kr/people> (Faculty & Staff, Graduate Students, Undergraduate Students, Alumni, 2026-10-23 열람)
[^prof]: 연구실 누리집 교수 소개 페이지(Minkyun Noh) <https://pml.kaist.ac.kr/minkyun-noh> (Affiliation, Employment, Education, Honors and Award, 2026-10-23 열람)
[^contact]: 연구실 누리집 Contact 페이지 <https://pml.kaist.ac.kr/contact> (Prospective Students, PML Onboarding Program, Contact Information, 2026-10-23 열람)
[^melist]: KAIST 기계공학과 교수진 목록 <https://me.kaist.ac.kr/team/team_010100.html> (노민균 교수 항목: 연구분야, 연구실, 최종학위, 2026-10-23 열람)
[^meprof]: KAIST 기계공학과 교수 소개(노민균) <https://me.kaist.ac.kr/pop/team.html?uid=107&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 연구실 웹사이트, E-mail, Office, 2026-10-23 열람)
[^medept]: KAIST 기계공학과 연구분야 「로보틱스/제어/모빌리티」 페이지 <https://me.kaist.ac.kr/research/research_010100.html> (노민균 교수 항목: 연구주제, 연구실, 웹사이트, 2026-10-23 열람)

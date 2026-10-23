# 차세대 항공모빌리티 연구실 (Aerial Innovation Mobility Lab, AIM Lab)

**KAIST 항공우주공학과 · 이상봉 교수**

- 분야: 전산유체역학과 난류 수치 모사, 도심 항공 모빌리티를 위한 도심 유동 예측, 해상 풍력 터빈과 풍력 단지 후류, 초음속·극초음속 충격파 유동과 우주 비행체 공력, 회전익 공력·소음, 유동 예측 인공지능
- 대분야: 기계·로봇·제조, 에너지·환경·지구
- 태그: 유체역학·유동[^research][^p1][^p3], 극초음속 공기열역학[^research], 과학·공학 AI[^research][^p5][^p7], 진동·소음 공학[^research]
- 홈페이지: <https://cfd.kaist.ac.kr/>
- 근거와 출처: [AIM Lab 근거 페이지](cfd-sources.md)

> 대규모 병렬 계산으로 하는 난류 수치 모사(LES·DNS)와 물리 정보 인공지능을 결합해, 도심 항공 모빌리티와 풍력, 초음속 유동의 복잡한 흐름을 빠르고 정확하게 예측하는 연구실이다.[^home][^research]

## 무엇을 연구하나

연구실은 KAIST 항공우주공학과 이상봉 교수가 이끄는 연구실이다.[^home][^board] 학과 연구실 소개는 국문 이름을 「차세대 항공모빌리티 연구실」로, 영문 이름을 Aerial Innovation Mobility Lab으로 적고, 누리집은 AIM Lab으로 줄여 부른다.[^board][^research] 학과 연구실 소개는 이 연구실이 새로운 개념의 항공 이동 수단을 연구한다고 적는다. 도심항공모빌리티(도시 안을 낮은 고도로 나는 사람·화물 수송 비행체와 그 운항 체계)를 연구하려고 도심 기상을 반영한 다물체 동역학 시뮬레이션(여러 물체가 서로 힘을 주고받으며 움직이는 과정을 함께 계산하는 모사)을 수행하고, 안전과 에너지 효율을 고려한 항로 설계를 연구하며, 초음속 유동과 풍력 에너지 연구도 함께 한다고 소개한다.[^board]

누리집 첫 화면은 「Aerospace · Energy · AI for Fluid Physics」(항공우주, 에너지, 유체 물리를 위한 인공지능)를 표어로 단다. 대규모 병렬 계산, 큰 에디 모사와 직접 수치 모사로 하는 난류 계산, 작동선 기법과 가상 경계 기법, 물리 정보 인공지능을 결합해 복잡한 흐름을 빠르고 정확하게 예측한다고 적고, 초점으로 도심 항공 모빌리티(UAM)·풍력·초음속 유동을, 도구로 RANS·LES·DNS·ALM·기계학습을, 규모로 CPU·GPU 병렬 계산을 든다.[^home] Research 페이지는 연구 범위를 안전한 도심 항공 모빌리티, 재생에너지 시스템, 초음속·극초음속 유동, 우주 비행체의 공기역학과 공기열역학, 회전익 소음, 유체-구조 연성, 난류 모형, 인공지능을 쓰는 유동 예측으로 요약한다.[^research]

Methods 페이지는 연구실이 쓰는 계산 방법 다섯 가지를 소개한다. RANS(레이놀즈 평균 나비에-스토크스, 흐름을 시간 평균한 방정식으로 푸는 방법)는 설계 후보를 빠르게 걸러 보는 데 쓰고, LES(큰 에디 모사, 큰 소용돌이는 직접 풀고 작은 소용돌이는 모형으로 대신하는 방법)는 도심 유동, 회전 날개의 후류, 대기 경계층에 쓴다. DNS(직접 수치 모사, 난류의 모든 크기의 소용돌이를 모형 없이 계산하는 방법)는 충격파와 난류 경계층의 상호작용이나 천이 같은 세밀한 기구를 밝히는 데 쓰고, ALM(작동선 기법, 날개 모양 대신 날개를 따라 나눠 놓은 힘으로 날개의 효과를 나타내는 방법)은 회전익기와 풍력 터빈의 계산을 효율적으로 만든다. 기계학습은 정밀한 계산 자료를 신경망과 이어 유동장 복원, 시간 예측, 빠른 설계 탐색에 쓴다.[^methods] Research 페이지의 In-house Code 칸은 연구실이 C/C++와 CUDA(GPU에서 계산을 돌리는 프로그래밍 도구)로 자체 전산유체역학 해석 프로그램을 만들어, 이산화 방식, 메모리 배치, 병렬 계산 부분, MPI(여러 컴퓨터가 메시지를 주고받으며 함께 계산하는 규약) 확장, 검증 절차를 직접 다룬다고 적는다.[^research]

Research 페이지는 연구 분야를 여섯 칸으로 나눈다. 도심 항공 모빌리티 유동 예측은 LES와 가상 경계 기법으로 고층 건물 주변의 복잡한 도심 난류를 풀고, 축소 모형과 신경망으로 빠른 예측을 탐색한다. 해상 풍력과 풍력 단지 후류 제어는 부유식 풍력 터빈 플랫폼의 동역학, 날개 피치 제어, 후류 섞임을 연구해 발전량을 늘리면서 피로 하중을 줄이려 한다. 초음속·극초음속 충격파 유동은 고차 DNS로 충격파와 난류 경계층의 상호작용, 스크램제트, 흡입구, 노즐 속 압축성 난류를 살피며 압력 손실과 열 부하에 초점을 둔다. 우주 비행체 공기역학·공기열역학은 전산유체역학과 부품별 합산 기법으로 아음속부터 극초음속까지의 임무 구간에서 공력 계수와 가열 자료를 만든다. 회전익기·수직 이착륙기의 공력·소음·유체-구조 연성은 ALM과 LES로 회전 날개의 흐름과 소음원을 계산하고, FW-H 음향 해석과 유체-구조 연성 모듈로 소리의 전파와 구조물과의 연성까지 분석을 넓힌다. 물리 정보 인공지능과 유동 초해상도는 합성곱 신경망, 그래프 신경망, 트랜스포머, 확산 모형 계열의 구조를 유동 물리에 맞게 바꿔 전산유체역학 자료의 생성·보정·예측·초해상도에 쓴다.[^research]

대표 논문에서는 충격파와 난류 경계층이 만나는 초음속 압축 경사면 흐름을 DNS로 계산해 저주파 흔들림이 생기는 기구와 난류 에너지가 커지는 과정을 밝혔고,[^p1][^p2] 벽을 따라 움직이는 파동과 벽 진동으로 벽면 압력 변동과 마찰을 줄이는 제어를 비교했으며,[^p3] 충격파와 소용돌이가 있는 흐름을 높은 해상도로 푸는 고차 수치 기법을 개선했다.[^p4] 도심 난류를 건물 형상과 함께 3차원으로 빠르게 예측하는 트랜스포머 모델을 만들었고,[^p5] 상류 터빈의 후류가 부유식 해상 풍력 터빈의 피로 하중에 주는 영향을 분석했으며,[^p6] 풍력 터빈 후류를 실시간으로 예측하는 신경 연산자 모델과 풍력 단지 후류의 3차원 딥러닝 대리 모델을 만들었다.[^p7][^p8]

## 주요 연구 주제

### 1. 초음속 충격파와 난류 경계층

Research 페이지의 초음속·극초음속 충격파 유동 칸과 우주 비행체 공기역학·공기열역학 칸에 해당한다.[^research] 대표 논문 1은 마하 2.9 흐름에서 모서리 곡률이 다른 압축 경사면 세 가지를 DNS로 계산해 충격파-난류 경계층 상호작용의 저주파 흔들림을 분석했고,[^p1] 대표 논문 2는 자체 개발한 컴팩트 유한 차분 해석 프로그램으로 강한 상호작용에서 난류 운동 에너지가 두 곳에서 커지는 기구를 밝혔다.[^p2] Projects 페이지는 비행 중인 로켓의 공기력과 안정성 계수 계산을 연구 주제로 소개한다.[^projects]

### 2. 벽 난류 제어와 고차 수치 기법

Methods 페이지의 DNS 칸(충격파-난류 경계층 상호작용과 천이 같은 세밀한 기구 연구)과 벽 난류의 응집 구조, 천이·박리 과정을 보여 주는 계산 결과, Research 페이지 In-house Code 칸의 자체 해석 프로그램 개발에 해당한다.[^methods][^research] 대표 논문 3은 공간적으로 발달하는 난류 경계층에서 불어 넣기, 빨아들이기, 벽의 가로 방향 진동, 흐름 방향으로 움직이는 파동을 비교해 벽면 압력 변동과 마찰 저항의 변화를 살폈고,[^p3] 대표 논문 4는 충격파와 소용돌이가 있는 흐름을 위한 고차 ESWENO-P 수치 기법을 제안했다.[^p4] Projects 페이지는 난류 경계층 천이를 연구 주제로 소개한다.[^projects]

### 3. 도심 항공 모빌리티와 도심 유동 예측

Research 페이지의 도심 항공 모빌리티 유동 예측 칸과 물리 정보 인공지능 칸, 학과 연구실 소개의 도심 기상 반영 비행 모사와 항로 설계에 해당한다.[^research][^board] 대표 논문 5는 건물 형상 정보를 넣은 3차원 스윈 트랜스포머로 도심 난류의 속도와 압력을 한꺼번에 예측했다.[^p5] Projects 페이지는 건물 밀집 지역의 난류를 LES로 예측하는 연구, 전산유체역학 자료로 도심 유동장을 보정·가속·초해상도화하는 기계학습 연구, 도심 난류가 수직 이착륙기의 안전·제어·회전 날개 성능에 주는 영향 평가, 헬리콥터 흐름을 위한 가상 경계 기법과 작동선 기법의 결합을 소개한다.[^projects]

### 4. 해상 풍력 터빈과 후류

Research 페이지의 해상 풍력과 풍력 단지 후류 제어 칸에 해당한다.[^research] 대표 논문 6은 LES로 만든 상류 터빈 후류에서 부유식 해상 풍력 터빈의 날개·타워 피로 하중과 플랫폼 움직임을 분석했다.[^p6] 대표 논문 7과 8은 LES 자료로 학습한 신경망으로 요(yaw, 터빈의 회전면이 바람 방향에서 옆으로 돌아간 각도) 상태 풍력 터빈의 먼 후류와 풍력 단지의 3차원 후류를 예측했다.[^p7][^p8] Projects 페이지는 요 상태 풍력 터빈 후류의 비대칭 소용돌이 구조, 개별 피치 제어로 부유식 터빈의 피로 하중을 줄이는 전략, 부유식 해상 풍력 터빈의 안정 운전을 위한 날개 피치 제어 설계를 소개한다.[^projects]

## 대표 논문

랩 Publications 페이지의 2021–2026년 논문 가운데 이상봉 교수가 마지막 저자인 학술지 논문을 네 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [On low-frequency unsteadiness in shock-wave–turbulent boundary layer interaction with varying corner curvature](https://doi.org/10.1017/jfm.2026.11644) · Journal of Fluid Mechanics | 충격파와 난류 경계층이 만나는 곳(STBLI)에서 생기는 저주파 흔들림의 물리 기구를 마하 2.9, 운동량 두께 레이놀즈 수 약 2400의 직접 수치 모사로 연구했다. 모서리가 날카로운 24° 압축 경사면(R24)과, 반지름이 경계층 두께의 7배(C7)와 14배(C14)인 곡면 경사면 두 가지를 비교했다. R24와 C7에서는 흐름이 벽에서 떨어져(박리) 떨어져 나간 전단층이 생기고 저주파 흔들림이 뚜렷했지만, C14에서는 박리가 시작 단계에 그치고 저주파 흔들림이 뚜렷이 약했다. 흐름을 주파수별 구조로 나누는 분석에서 모든 경우에 서로 반대로 도는 구조가 생겨 하류로 자랐고, R24와 C7에서는 이 구조가 떨어져 나간 전단층 안에서 자라고 합쳐지며 큰 규모의 저주파 운동을 만들었다. 결과는 떨어져 나간 전단층과 반대로 도는 구조의 상호작용이 큰 구조로 자라 저주파 흔들림을 지배함을 시사한다.[^p1] | 1저자 Y. Kang, 마지막 저자 이상봉 |
| 2 | 2024 | [Direct numerical simulation of turbulence amplification in a strong shock-wave/turbulent boundary layer interaction](https://doi.org/10.1063/5.0180077) · Physics of Fluids | 마하 2.9 흐름이 24° 압축 경사면을 지날 때 강한 충격파와 난류 경계층의 상호작용 안에서 난류가 커지는 기구를 직접 수치 모사로 연구했다. 컴팩트 유한 차분법에 기반한 새 자체 해석 프로그램을 소개하고, 기존 직접 수치 모사와 실험 자료와 흐름 통계를 비교해 정확도를 검증했다. 난류 운동 에너지가 커지는 지점이 두 곳 나타났고, 흐름이 벽에 다시 붙는 지점 근처의 둘째 증폭에는 중간 주파수 특성을 가진 작은 충격파(shocklet)가 핵심 요인이었다. 유선 좌표 분석에서는 난류 운동 에너지 생성에 흐름이 느려지는 효과보다 전단 효과가 지배적이었다.[^p2] | 1저자 Y. Kang, 마지막 저자 이상봉 |
| 3 | 2025 | [Suppression of pressure fluctuation and turbulent friction at the wall in spatially developing turbulent boundary layers via streamwise-traveling waves and wall oscillations](https://doi.org/10.1063/5.0281564) · Physics of Fluids | 난류 경계층은 벽면의 압력 변동과 마찰 저항을 크게 만들어 항공기, 배, 풍력 장치에 공기역학·음향 손실을 준다. 높은 레이놀즈 수의 압력 기울기 없는 난류 경계층에 불어 넣기(BW), 빨아들이기(SC), 벽의 가로 방향 진동(SWO), 흐름 방향으로 움직이는 파동을 더한 벽 진동(STWO)의 네 가지 제어를 적용해 직접 수치 모사로 비교했다. SC는 벽 근처 난류를 키워 마찰을 늘렸고, BW, SWO, STWO는 마찰을 줄였으며 STWO가 가장 크게 줄였다. SWO와 STWO에서는 벽면 압력 변동과 벽 근처의 흐름 방향 소용돌이가 만드는 에너지가 눈에 띄게 줄어, 두 방법이 벽면 압력 변동과 저항을 줄이는 데 효과적인 접근임을 보였다.[^p3] | 1저자 D. Lee, 마지막 저자 이상봉 |
| 4 | 2022 | [Improved high-order high-resolution energy stable weighted essentially non-oscillatory plus scheme for shock/vortex problems](https://doi.org/10.1063/5.0083675) · AIP Advances | 충격파 근처에서 계산값이 불필요하게 흔들리지 않도록 하는 WENO 계열 수치 기법의 가중 함수를 고쳐, 고차·고해상도 ESWENO-P 기법을 개발했다. 먼저 사용자가 정하는 새 변수를 넣어 가중 함수를 바꾸고, WENO-ZP 기법의 미세 조정 항을 가져와 붙였으며, 이 변수의 값을 정하는 매개변수 연구를 했다. 충격파와 소용돌이가 있는 잘 알려진 1·2차원 시험 문제로 정확도와 해상도를 검증한 결과, ESWENO-P는 ESWENO에 견줘 압력 같은 값이 갑자기 바뀌는 곳 근처에서 더 안정했고, WENO-ZP에 견줘 사용자 정의 변수에 덜 민감했다. 기존 WENO 계열 기법들에 견줘 계산 부담을 크게 늘리지 않고 높은 해상도로 흐름을 꾸준히 풀어 냈다.[^p4] | 1저자 S. H. Park, 마지막 저자 이상봉 |
| 5 | 2026 | [Three-dimensional Primitive prediction with building embedded Swin Transformer for urban turbulence](https://doi.org/10.1063/5.0324405) · Physics of Fluids | 큰 에디 모사(LES)는 보행자 쾌적성, 오염 물질 확산, 도심 항공 모빌리티 운항에 중요한 도심 캐노피의 물리를 푸는 기준이지만, 긴 시간의 자료를 만들려면 계산 시간이 지나치게 길다. 속도 세 성분과 압력(u, v, w, p)을 직접 예측하는 3차원 스윈 트랜스포머 모델 3DSwinUrbanNet을 개발했고, 시간 간격은 1분으로 LES의 0.05초보다 크게 잡았다. 3차원 건물 형상 정보를 부호기, 중간 구조, 복호기에 모두 넣었다. 시간 평균장, 벽에 수직인 방향의 분포, 난류 통계, 확률 밀도 함수와 에너지 스펙트럼으로 정확도를 평가했고, 20분 예보를 2.58초에 계산해(LES 5120초) 1984배 빨라졌으며 그래픽 처리 장치 한 장으로 실시간 예측이 가능했다.[^p5] | 1저자 J. Park, 마지막 저자 이상봉 |
| 6 | 2024 | [Wake effect on floating offshore wind turbine fatigue load](https://doi.org/10.1063/5.0242835) · Physics of Fluids | 상류 풍력 터빈의 후류에 잠긴 터빈은 발전량이 줄고 피로 하중이 커지지만, 지금의 풍력 단지 배치 최적화는 발전량만 우선하고 피로 하중은 평가가 복잡해 다루지 않는다. 후류와 터빈이 겹치는 정도가 부유식 해상 풍력 터빈의 피로 하중에 주는 영향을 연구했다. LES로 상류 터빈 후류를 만든 뒤 공력-탄성 모사를 폭넓게 수행했다. 날개 피로 하중은 후류의 속도 손실과 난류와 관련이 있었고, 옆 방향으로 약 0.5 터빈 지름(D) 떨어진 곳에서 정점이 둘인 분포를 보였으며 흐름 방향으로는 줄었다. 옆으로 1D 떨어지면 발전량은 완전히 회복되지만 피로 하중은 상당히 남았고, 타워 피로 하중과 플랫폼 움직임도 겹침 정도와 파도의 영향을 받았다. 배치 최적화에 피로 하중 분석을 넣어야 함을 보였다.[^p6] | 1저자 Y. Kang, 마지막 저자 이상봉 |
| 7 | 2025 | [Channel-assisted Fourier neural operator for high-fidelity far-wake prediction of a wind turbine under yawed conditions](https://doi.org/10.1063/5.0287914) · Physics of Fluids | 요(yaw) 상태 풍력 터빈의 먼 후류를 실시간으로, 높은 해상도로, 긴 시간에 걸쳐 예측하는 채널 보조 푸리에 신경 연산자(CFNO)를 제안했다. 요 각도를 채널 보조 층으로 넣고, 깊이별 분리 스펙트럼 합성곱과 잔차를 강화한 푸리에 층을 결합해 긴 자기회귀 예측을 안정시켰고, 매개변수 수를 푸리에 신경 연산자(FNO)의 약 23%, DSSC-FNO의 약 50%로 줄였다. 회전을 넣은 작동 원판 모형(ADM-R)으로 만든 LES 자료로 학습·검증했고, 최대 x/D=12까지의 180 × 70 격자에서 오차 0.89%를 얻어 FNO 기준 모델을 넘었으며 GPU 한 장에서 밀리초부터 1초 미만의 지연 시간으로 돌았다. 이 능력이 디지털 트윈을 이용한 후류 방향 조정과 요 기반 모델 예측 제어를 가능하게 한다고 적는다.[^p7] | 1저자 E. Lee, 마지막 저자 이상봉 |
| 8 | 2026 | [A Fully Three-Dimensional Deep Learning Surrogate Model for Large-Eddy Simulation-Resolved Wake Dynamics in Wind Farm](https://doi.org/10.1063/5.0330691) · Physics of Fluids | 큰 풍력 단지에서 후류끼리의 상호작용은 발전량을 줄이고 구조 피로 하중을 키워, 단지 설계와 제어에 정확한 후류 예측이 필요하다. LES는 반복 평가에 쓰기에 계산이 지나치게 무겁고, 기존 저정밀 모형은 3차원 비정상 후류와 여러 터빈의 상호작용을 담기 어렵다. 스윈 트랜스포머 중간 구조에 U자형 합성곱 신경망을 결합해 풍력 단지의 3차원 난류 후류를 오래 예측하는 딥러닝 틀을 제안했다. 여러 터빈 기울임(tilt) 설정을 담은 LES 자료로 학습해 3차원 후류와 수직 방향 휘어짐을 담았고, 순간 3차원 흐름 방향 속도장을 긴 시간 동안 정확하게 예측했으며, 학습하지 않은 기울임 설정에서도 속도 손실 분포, 후류 중심선 궤적, 날개 회전면 유입 속도를 재현했다. 상류의 제한된 유입 정보를 더하면 유입 경계 근처 터빈의 유입 속도 예측이 좋아졌다.[^p8] | 1저자 M. Ahn, 마지막 저자 이상봉 |

## 교수와 전문 분야

이상봉 교수는 연세대학교에서 기계공학 학사(1999), Stanford University에서 기계공학 석사(2002), University of Illinois at Urbana-Champaign에서 항공우주공학 박사(2009)를 받았다.[^faculty][^deptlist] 연구실 교수 카드의 경력 칸에 따르면 미국 National Renewable Energy Laboratory(국립재생에너지연구소)에서 박사후연구원(2010–2013)과 Engineer III(2013–2016)로, University of New Mexico에서 조교수(2016–2019)로 일했고, 2019년부터 KAIST에서 조교수·부교수(Assistant/Associate Professor)로 있다.[^faculty] 교수 카드와 학과 교수진 목록은 현재 직위를 Associate Professor(부교수)로 적는다.[^faculty][^deptlist]

학과 교수진 목록은 교수의 연구분야를 전산유체역학(Computational Fluid Dynamics), 난류(Turbulence), 극초음속 유동(Hypersonic Flows), 차세대 항공 모빌리티(Next Generation Air Mobility), 재생에너지(Renewable Energy), 항공 기상(Aeronautical Meteorology)으로 적고,[^deptlist] 학과 연구실 소개는 연구분야를 항공모빌리티, 풍력에너지, 초음속으로 적는다.[^board] 연구실 Awards 페이지에 따르면 교수는 KAIST 강의혁신상(Teaching Innovation Award)을 두 번 받았다(2023년 봄학기 AE37000 Numerical Analysis, 2025년 가을학기 AE42000 Viscous Aerodynamics).[^awards] Teaching 페이지는 2020년 봄학기부터 2026년 가을학기까지 교수가 맡은 과목으로 Viscous Aerodynamics(점성 공기역학), Turbulent Flows(난류), Introduction to CFD(전산유체역학 입문), Advanced Aerodynamics(고급 공기역학), Numerical Analysis(수치해석) 등을 적는다.[^teaching]

랩 Publications 페이지의 2018년 이전 논문을 보면, 2005년 논문은 등방성 난류에서 가속도의 간헐성을, 2008–2012년 논문은 초음속 충격파와 경계층의 상호작용을 작은 경사면(micro-ramp)과 소용돌이 발생기로 제어하는 연구와 고정 날개 배열의 착빙 모사를, 2012–2015년 논문은 대기 난류와 풍력 터빈 후류가 터빈 하중과 풍력 단지 성능에 주는 영향, 후류 방향 조정 기법, 후류 모형을 다룬다. 2018년 논문은 정상 충격파와 경계층의 상호작용 제어, 해상 풍력 발전소의 LES와 피치 제어로 피로 하중을 줄이는 연구다.[^pubs] 논문으로 보면 지금의 전문 분야는 고차 직접 수치 모사로 초음속 충격파-난류 경계층 상호작용과 벽 난류를 분석하는 일(대표 논문 1–4),[^p1][^p2][^p3][^p4] LES 자료를 학습한 인공지능으로 도심 난류와 풍력 후류를 빠르게 예측하는 일(대표 논문 5, 7, 8),[^p5][^p7][^p8] LES와 공력-탄성 모사로 부유식 해상 풍력 터빈의 하중을 분석하는 일(대표 논문 6)이다.[^p6]

## 응용 분야

학과 연구실 소개는 도심항공모빌리티를 위해 도심 기상을 반영한 비행 모사로 안전과 에너지 효율을 고려한 항로를 설계한다고 적고,[^board] Research 페이지는 도심 항공 모빌리티의 안전, 재생에너지 시스템, 우주 비행체의 공력·가열 자료, 회전익 소음을 연구 범위로 든다.[^research] 대표 논문은 보행자 쾌적성·오염 물질 확산·도심 항공 모빌리티 운항을 위한 도심 난류의 실시간 예측,[^p5] 풍력 단지 배치 최적화에 피로 하중을 넣는 일,[^p6] 디지털 트윈을 이용한 풍력 터빈 후류 방향 조정과 모델 예측 제어,[^p7] 풍력 단지 설계와 제어를 위한 후류 예측,[^p8] 항공기·배·풍력 장치의 소음과 저항을 줄이는 벽 제어[^p3]를 응용 대상으로 든다. 졸업생의 진로로는 국방과학연구소, 한국항공우주연구원, 고등기술연구원, KOREATECH, 삼성전자, 대한항공, 이에이트, QUNOVA Computing, Unastella, Sandia National Lab, US Air Force Academy 등이 있다.[^members]

## 구성원

2026년 10월 23일 랩 Members 페이지 기준이다. Research Staff 칸의 박사후연구원 2명과 Student Researchers 칸의 박사과정 6명, 석사과정 7명, 학부 연구생 2명이다. 과정은 카드의 표기(Research Staff · Postdoctoral Researcher, Ph.D. Student, M.S. Student, Undergraduate Researcher)를 옮겼고, 시작은 카드의 Period 칸, 연구 주제는 Research interest 칸이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| 박준 (Jun Park) | 박사후연구원 | 2025-present | Machine learning, Turbulence prediction, Urban flow prediction | junpark@kaist.ac.kr | 5, 8 |
| Chhote Lal Shah | 박사후연구원 | 2025-present | Immersed boundary method |  |  |
| 정태빈 (Taebin Jung) | 박사과정 |  | Hypersonic flow, Turbulent boundary layer | wingssy@kaist.ac.kr |  |
| 권혁민 (Hyeokmin Kwon) | 박사과정 | 2023-present |  | hyeokmin@kaist.ac.kr |  |
| 강유주 (Yujoo Kang) | 박사과정 |  | Computational fluid dynamics, High performance computing, Knowledge extraction | ky5731@kaist.ac.kr | 1, 2, 6 |
| Moosarreza Shokati | 박사과정 |  | Integration of wind turbines with smart-grid technologies, Advanced control systems for wind-turbine performance optimization | rezashokati@kaist.ac.kr |  |
| 김용재 (Yongjae Kim) | 박사과정 |  | Future transportation system, Turbulence modeling | yongjae99@kaist.ac.kr |  |
| 권태연 (Taeyeon Kwon) | 박사과정 |  | Rotary wing aerodynamics, Parallel computation | tervalentlion5@kaist.ac.kr |  |
| 김해찬 (Haechan Kim) | 석사과정 |  | Urban air mobility simulation, Rotary wing aerodynamics | haechan010@kaist.ac.kr | 5 |
| 박재환 (Jaehwan Park) | 석사과정 |  | High altitude aerodynamics, Shock-turbulence boundary-layer interaction | park99@kaist.ac.kr |  |
| Sheela Moorthy | 석사과정 |  | Aerospace engineering research | sheela.moorthy.m@kaist.ac.kr |  |
| 남유주 (Yuju Nam) | 석사과정 |  | Chemical-reacting multi-solver, Compressible-flow shock detection | yujupr0506@kaist.ac.kr |  |
| 정성원 (Seongwon Jeong) | 석사과정 |  | FNO | swjeong0302@kaist.ac.kr |  |
| 양선재 (SeonJae Yang) | 석사과정 |  | Gas turbine engine | polarbean1209@kaist.ac.kr |  |
| 김성돈 (Seong Don Kim) | 석사과정 |  | Large-eddy simulation | kimsdon@kaist.ac.kr |  |
| 신지호 (Jiho Shin) | 학부 연구생 |  | Unstructured-grid CFD |  |  |
| 정재훈 (Jaehun Jung) | 학부 연구생 | 2026-present |  |  |  |

## 졸업생과 이전 구성원

랩 Members 페이지 Alumni 칸의 18명이다. 학위·과정과 연도는 카드의 표기이고, 진로는 카드의 Affiliation 칸이다. 이 가운데 Brad Philipbar, Sterling Olson, Rubel Das 세 사람은 카드가 학위 기관을 University of New Mexico로 적는다. 교수는 KAIST로 오기 전 2016–2019년 University of New Mexico 조교수였다.[^members][^faculty]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 안명환 (Myeonghwan Ahn) | Post-doctoral fellow (2025) | Assistant professor, KOREATECH |
| 박상현 (Sanghyun Park) | Post-doctoral fellow (2022) | 국방과학연구소 (Agency for Defense Development) |
| 정성문 (Seongmun Jung) | Post-doctoral fellow (2023) | 국방과학연구소 (Agency for Defense Development) |
| Rubel Das | Ph.D.'s degree, University of New Mexico (2024) |  |
| Brad Philipbar | Master's degree, University of New Mexico (2019) | US Air Force Academy |
| 이예담 (Yedam Lee) | Ph.D.'s degree (2026) | 한국항공우주연구원 (Korea Aerospace Research Institute) |
| 김혜빈 (Hyebin Kim) | Ph.D.'s degree (2026) | 고등기술연구원 (Institute for Advanced Engineering) |
| Sterling Olson | Master's degree, University of New Mexico (2019) | Sandia National Lab |
| 여현민 (Hyunmin Yeo) | Master's degree (2022) | 삼성전자 (Samsung Electronics Co., Ltd.) |
| Yisehak Abreham Keflemariam | Master's degree (2023) | Ph.D. Candidate at Pennsylvania State University |
| 박준범 (Junbeom Park) | Master's degree (2024) | 국방과학연구소 (Agency for Defense Development) |
| 이동현 (Donghyun Lee) | Master's degree (2025) | 이에이트 (E8 Co., Ltd.) |
| 윤승환 (SeungHwan Yun) | Master's degree (2025) | 대한항공 (Korean Air Co., Ltd.) |
| Ong Jesslyn Wei Yan | Master's degree (2025) |  |
| 양병헌 (Byeongheon Yang) | Master's degree (2026) | QUNOVA Computing Inc. |
| 강민재 (Minjae Kang) | Master's degree (2026) | Unastella Inc. |
| 이은찬 (Eunchan Lee) | Master's degree (2026) |  |
| 조병현 (Byeonghyun Cho) | Master's degree (2026) | 육군 대위 (Captain, Republic of Korea Army) |

## 최근 논문 목록 (2021–2026)

랩 Publications 페이지의 2022–2026년 학술지 논문 27편과 Conferences 페이지의 2021년 11월–2026년 5월 학회 발표 51건이다. Publications 페이지에는 2021년 논문이 없다. 연도는 페이지의 연도 표기이고, 학회 발표 줄 끝에는 페이지의 연·월 표기를 붙였다. 제목·저자·학술지와 학회 이름은 랩 표기 그대로다.[^pubs][^confs]

**2026**

- H. Kim, S. Kim, S. Lee, J.W. Hong. "Viscous Scaling Laws for Wall Shear Stress in Asymmetric Twin-Jet Impingement". *International Journal of Heat and Fluid Flow, 122, 110747*.
- J. Park, S. Lee. "Fine-Scale Urban Wind Field Prediction via Small-Scale Generator and Spectral Loss with Rolling-Out Transfer Learning". *Physics of Fluids, 38, 085167*.
- E. Lee, L. Chamorro, S. Lee. "Joint reconstruction and temporal prediction of three-dimensional wind turbine wakes using Fourier neural operators". *Physics of Fluids, 38, 088133*.
- H. Kim, J. Park, J. Hong, S. Lee. "Large-eddy simulation of turbulent flow and coherent structures over rotated random-height building arrays". *Physics of Fluids, 38, 075167*.
- H. Kim, S. Kim, S. Lee, J. Hong. "Physical Similarity and Scaling Laws for Ground Shear Stress in Circular Twin-Jet Impingement Flow". *Physics of Fluids, 38, 075157*.
- S. Kim, H. Kim, S. Lee, J. Hong. "Physics-Guided Residual Learning for Predicting Aerodynamic Characteristics of 3D Wing under Diverse Operating Conditions". *Aerospace Science and Technology, 176, 112606*.
- Y. Kang, S. Lee. "On low-frequency unsteadiness in shock-wave–turbulent boundary layer interaction with varying corner curvature". *Journal of Fluid Mechanics, 1036, A47*.
- D. Lee, S. Lee. "A coupled LES-vehicle dynamics simulation framework for quadcopter response in urban turbulent flows". *Advances in Engineering Software, 104192*.
- M. Ahn, J. Park, S. Lee. "A Fully Three-Dimensional Deep Learning Surrogate Model for Large-Eddy Simulation-Resolved Wake Dynamics in Wind Farm". *Physics of Fluids, 38, 055122*.
- S. Yun, M. Shokati, J. S. Kim, Y. J. Ha, K. H. Kim, S. Lee. "Control-Induced Modification in a Tension-Leg Platform Floating Wind Turbine". *Ocean Engineering, 358, 125592*.
- J. Park, H. Kim, P. Tsiotras, S. Lee. "Three-dimensional Primitive prediction with building embedded Swin Transformer for urban turbulence". *Physics of Fluids, 38, 045136*.
- M. Shokati, S. Lee. "Control to Structure Pathways in the Upstream TetraSpar Floating Wind Turbine". *Renewable Energy, 125623*.
- Y. Lee, S. Lee. "Tail-like vortical structures in extreme turbulent kinetic energy dissipation events of wall turbulence". *Physics of Fluids, 38, 035140*.
- H. Kim, T. H. Lee, S. Kim, S. Lee, J. Hong. "Regression analysis of heat transfer in twin slot jet impingement with computational fluid dynamics and machine learning technique". *International Journal of Heat and Fluid Flow, 118, 110220*.
- Y. Keflemariam, M. Shokati, S. Lee. "Large eddy simulation of wake mixing control strategies in offshore wind farms". *Energy Conversion and Management, 347, 120552*.
- Kunhyuk Kong, Taeyeon Kwon, Byeonguk Im, Sang Lee, SangJoon Shin. "Open-Loop Higher Harmonic Control Simulation by Tightly Coupled Actuator Line Method/Computational Structural Dynamics". *The Vertical Flight Society 82nd Annual Forum, 2026.05 (학회 발표)*.
- 김용재, 김해찬, 이상봉. "도심 난류 유동 내 6자유도 UAM 비행 제어 응답 및 안정성 비교". *Korean Society for Aeronautical and Space Sciences Spring Conference, 2026.04 (학회 발표)*.
- 권태연, 공건혁, 신상준, 이상봉. "전진비행 헬리콥터 로터의 고해상도 CFD 기반 CFD-CSD 연계해석". *Korean Society for Aeronautical and Space Sciences Spring Conference, 2026.04 (학회 발표)*.
- Yuju Nam, Sang Lee. "Integrated Simulation Framework for Atmospheric Entry and Vehicle Motion Analysis". *Korean Society for Aeronautical and Space Sciences Spring Conference, 2026.04 (학회 발표)*.

**2025**

- E. Lee, S. Lee. "Channel-assisted Fourier neural operator for high-fidelity far-wake prediction of a wind turbine under yawed conditions". *Physics of Fluids, 37, 097143*.
- D. Lee, S. Lee. "Suppression of pressure fluctuation and turbulent friction at the wall in spatially developing turbulent boundary layers via streamwise traveling waves and wall oscillations". *Physics of Fluids, 37, 095117*.
- Y. Lee, S. Lee. "A prediction of urban boundary layer using Recurrent Neural Network and reduced order modeling". *Building and Environment, 112804*.
- S. Jung, S. Shin, S. Lee. "Dimensionality reduction of solution reconstruction methods for a four-point stencil". *Advances in Engineering Software, 199*.
- Yujoo Kang, Sang Lee. "Curvature effect on low-frequency unsteadiness on shock-turbulent boundary layer interaction". *APS DFD 78th Annual Meeting, 2025.11 (학회 발표)*.
- Taeyeon Kwon, Kunkyuk Kong, SangJoon Shin, Sang Lee. "A High-Fidelity Coupled CFD-CSD Framework for Articulated Rotorcraft Analysis". *APS DFD 78th Annual Meeting, 2025.11 (학회 발표)*.
- Yongjae Kim, Donghyun Lee, Yedam Lee, Hyebin Kim, Sang Lee. "Impact of local wind conditions on Urban Air Mobility". *APS DFD 78th Annual Meeting, 2025.11 (학회 발표)*.
- Taeyeon Kwon, Kunkyuk Kong, SangJoon Shin, Sang Lee. "Fluid-Structure Coupled Analysis of UH-60A Helicopter under Operational Conditions". *Asia-Pacific International Symposium on Aerospace Technology, 2025.10 (학회 발표)*.
- 권태연, 공건혁, 신상준, 이상봉. "전진비행 조건에서 작동하는 관절식 로터의 유동-구조 연계해석". *Korean Society for Aeronautical and Space Sciences Space Conference, 2025.11 (학회 발표)*.
- Yedam Lee, Eunchan Lee, Yongjae Kim, Hyebin Kim, Haechan Kim, Sang Lee. "Reduced order prediction of urban boundary layers". *Asia-Pacific International Symposium on Aerospace Technology, 2025.10 (학회 발표)*.
- H. Kim, M. Shokati, S. Lee. "Wake Structures in Yawed Turbines: An LES Perspective". *The 8th International Conference on Civil, Structural and Environmental Engineering Computing, 2025.08 (학회 발표)*.
- 조병현, 강유주, Jesslyn Wei Yan Ong, 이상봉. "Falcon 9 재진입 과정의 열공력 해석". *Korean Society for Aeronautical and Space Sciences Space Conference, 2025.06 (학회 발표)*.
- Jesslyn Wei Yan Ong, 강유주, 조병현, 이상봉. "재사용발사체 역추진과정의 공력 해석". *Korean Society for Aeronautical and Space Sciences Space Conference, 2025.06 (학회 발표)*.
- Shokati Moosarreza, 이상봉. "부유식 풍력터빈에서 후류 제어가 하중 응답에 미치는 영향". *KWEA Spring Conference, 2025.06 (학회 발표)*.
- 윤승환, 이상봉. "15MW 인장각형 부유식 해상풍력터빈의 제어 최적화 및 플랫폼 동적 안정성 향상 연구". *KWEA Spring Conference, 2025.06 (학회 발표)*.
- 김용재, 이동현, 이예담, 이상봉. "도심 건물 데이터 기반 도심 유동 내에서의 UAM 비행 시뮬레이션". *Korean Society for Aeronautical and Space Sciences Spring Conference, 2025.04 (학회 발표)*.
- 윤승환, 이상봉. "15MW급 인장각형 방식 부유식 해상풍력 플랫폼 제어기 설계 연구". *Korea Energy Society Spring Conference, 2025.04 (학회 발표)*.

**2024**

- Y. Kang, S. Lee. "Wake effect on floating offshore wind turbine fatigue load". *Physics of Fluids, 36, 125176*.
- Y. Kang, S. Lee. "Direct numerical simulation of turbulence amplification in a strong shock-wave/turbulent boundary layer interaction". *Physics of Fluids, 36, 016127*.
- Yujoo Kang, Sang Lee. "Shock-wave/turbulent boundary layer interaction over curved compression ramp". *APS DFD 77th Annual Meeting, 2024.11 (학회 발표)*.
- Taeyeon Kwon, Junbeom Park, Yedam Lee, Kunhyuk Kong, Byeonguk Im, Sangjoon Shin, Sang Lee. "Helicopter Rotor Simulation via Actuator Line Method coupled with DYMORE". *APS DFD 77th Annual Meeting, 2024.11 (학회 발표)*.
- Yedam Lee, Sang Lee. "A statistical investigation of near-wall quasi-streamwise vortices with extreme events of turbulent kinetic energy dissipation in turbulent channel flow". *APS DFD 77th Annual Meeting, 2024.11 (학회 발표)*.
- 권태연, 이예담, 이상봉. "Actuator Line Method를 이용한 헬리콥터 로터 공력해석". *Korean Society for Aeronautical and Space Sciences Fall Conference, 2024.11 (학회 발표)*.
- 이동현, 이예담, 이상봉. "도심 유동을 고려한 쿼드콥터의 동적 시뮬레이션". *Korean Society for Aeronautical and Space Sciences Fall Conference, 2024.11 (학회 발표)*.
- Jesslyn Wei Yan Ong, 강유주, 조병현, 전은지, 이상봉. "재사용발사체 재진입과정의 공력 해석". *Korean Society for Aeronautical and Space Sciences Fall Conference, 2024.11 (학회 발표)*.
- 조병현, 강유주, Jesslyn Wei Yan Ong, 전은지, 이상봉. "RETALT 지상실험 모사를 통한 충격파-플룸 상호작용 분석". *Korean Society for Aeronautical and Space Sciences Fall Conference, 2024.11 (학회 발표)*.
- 이예담, 김혜빈, 김용재, 양병헌, 이상봉. "인공 신경망 기반 도심 난류 유동 초해상도화를 통한 난류 통계 복원". *Society for Aerospace System Engineering Fall Conference, 2024.10 (학회 발표)*.
- 이은찬, 이예담, 김혜빈, 김용재, 양병헌, 이상봉. "인공 신경망 기반 도심 지역의 난류 유동 예측". *Society for Aerospace System Engineering Fall Conference, 2024.10 (학회 발표)*.
- Jesslyn Wei Yan Ong, 강유주, 전은지, 이상봉. "재사용발사체 초음속 역추진 시스템의 전산 유체 역학적 연구". *Korean Society for Aeronautical and Space Sciences Space Conference, 2024.06 (학회 발표)*.
- 강유주, 이예담, 이상봉. "DNS를 이용한 충격파-난류 경계층 상호작용 난류 증폭 메커니즘 연구". *KSCFE Spring Conference, 2024.05 (학회 발표)*.
- Jesslyn Wei Yan Ong, 강유주, 전은지, 이상봉. "재사용발사체 초음속 역추진 시스템의 전산 유체 역학적 연구". *KSCFE Spring Conference, 2024.05 (학회 발표)*.
- 박준범, 이예담, 공건혁, 임병욱, 이상봉, 신상준. "Actuator Line Method를 이용한 UH-60 메인로터 제자리 비행 공력해석". *Korean Society for Aeronautical and Space Sciences Spring Conference, 2024.04 (학회 발표)*.
- Yujoo Kang, Sang Lee. "Direct numerical simulation study on pressure amplification and shock-boundary layer interaction". *HiSST 2024, 2024.04 (학회 발표)*.
- Yujoo Kang, Sang Lee. "Direct numerical simulation of strong shock-turbulent boundary layer interaction". *HiSST 2024, 2024.04 (학회 발표)*.
- Jesslyn Wei Yan Ong, Yujoo Kang, Jaemyung Ahn, Sang Lee. "Aerodynamics of the Reusable Launch Vehicle Supersonic Retropropulsion System". *HiSST 2024, 2024.04 (학회 발표)*.

**2023**

- Y. A. Keflemariam, S. Lee. "Control and dynamic analysis of a 10MW floating wind turbine on a TetraSpar multi-body platform". *Renewable Energy, 217, 119194*.
- Y. Kang, H. Kim, and S. Lee. "Benefits of individual pitch control on offshore wind turbine submerged in upstream wake". *Renewable Energy, 217, 119127*.
- S. H. Park, O. J. Kwon, S. Lee. "Aerodynamic Analysis of High-speed Compound Unmanned Rotorcraft Using an Unstructured Flow Solver". *International Journal of Aeronautical and Space Sciences*.
- H. Yeo, S. Lee. "Impact of heterogeneous building arrangement on local turbulence escalation". *Building and Environment*.
- Hyebin Kim, Sang Lee. "Characteristics of a secondary wake steering from two tandem wind turbines under yaw misalignment". *APS DFD 76th Annual Meeting, 2023.11 (학회 발표)*.
- Yedam Lee, Sang Lee. "Influence of rectangular cylinder array on vortex statistics in atmospheric boundary flow". *APS DFD 76th Annual Meeting, 2023.11 (학회 발표)*.
- Yujoo Kang, Sang Lee. "Shock-induced turbulence amplification on a supersonic compression ramp: a DNS investigation". *APS DFD 76th Annual Meeting, 2023.11 (학회 발표)*.
- 김혜빈, 이예담, 김용재, 이상봉. "UAM 운용을 위한 WRF-URANS 기반의 멀티스케일 기상 예측 시뮬레이션". *Korean Society for Aeronautical and Space Sciences Fall Conference, 2023.11 (학회 발표)*.
- 윤승환, 하윤진, 박세명, 이상봉. "인장각형(TLP)방식 부유식 해상풍력 플랫폼 제어 연구". *KWEA Fall Conference, 2023.11 (학회 발표)*.
- Yisehak Abreham Keflemariam, 윤승환, 이상봉. "Higher-order dynamic individual pitch control for wake mixing in offshore wind farms: Using LES approach". *KWEA Spring Conference, 2023.06 (학회 발표)*.
- 이예담, 이상봉. "건물형상이 반영된 도심 경계층 난류 유동의 와류 특성 변화". *KSCFE Spring Conference, 2023.05 (학회 발표)*.
- 강유주, 이상봉. "DNS를 이용한 초음속 압축 램프의 난류 증폭 메커니즘 연구". *KSCFE Spring Conference, 2023.05 (학회 발표)*.

**2022**

- S. H. Park, O. J. Kwon, S. Lee. "Assessment of a High-Order High-Resolution ESWENO-P Scheme for AVI/BVI Problems". *International Journal of Aeronautical and Space Sciences*.
- S. H. Park, O. J. Kwon, and S. Lee. "Improved high-order high-resolution energy stable weighted essentially non-oscillatory plus scheme for shock/vortex problems". *AIP Advances, 12, 045106*.
- Yedam Lee, Sang Lee. "A data-driven prediction of turbulent flow in urban environment using deep neural network". *APS DFD 75th Annual Meeting, 2022.11 (학회 발표)*.
- Yedam Lee, Sang Lee. "An artificial neural network approach in prediction of atmospheric flow for urban air mobility". *13th Asian Computational Fluid Dynamics Conference, 2022.10 (학회 발표)*.
- Yujoo Kang, Sang Lee. "On transitory shock interaction with incipient flow separation". *32nd International Symposium on Rarefied Gas Dynamics, 2022.06 (학회 발표)*.
- Yisehak Abreham Keflemariam, 김응수, 이상봉. "DTU10 MW 부유식 해상풍력터빈의 제어 연구". *KWEA Spring Conference, 2022.06 (학회 발표)*.
- 강유주, 김혜빈, 이상봉. "후류유동장에서의 10MW 부유식 풍력터빈의 개별피치제어". *KWEA Spring Conference, 2022.06 (학회 발표)*.
- 김혜빈, 여현민, 이예담, 이상봉. "도심항공모빌리티를 위한 도심기상 데이터 인프라". *Society for Aerospace System Engineering Spring Conference, 2022.05 (학회 발표)*.
- 이예담, 여현민, 김혜빈, 이상봉. "인공 신경망 기반 고해상도 도심 난류 유동 예측". *Korean Society for Aeronautical and Space Sciences Spring Conference, 2022.04 (학회 발표)*.
- 여현민, 이예담, 김혜빈, 이상봉. "LES와 잠입경계법을 이용한 건물 형상이 반영된 도심 경계층 난류 유동 해석". *Korean Society for Aeronautical and Space Sciences Spring Conference, 2022.04 (학회 발표)*.

**2021**

- 여현민, 김혜빈, 김정우, 이예담, 이상봉. "중규모 수치예보모델을 연계한 고해상도 도심기상예측 시뮬레이션". *Korean Society for Aeronautical and Space Sciences Fall Conference, 2021.11 (학회 발표)*.
- 김성환, Y. A. Keflemariam, 김혜빈, 신희준, 여현민, 김정우, 이예담, 강유주, 이상봉. "NREL 5MW 반잠수식 해상풍력터빈 하중 해석". *KWEA Fall Conference, 2021.11 (학회 발표)*.

## 수상

랩 Awards 페이지에 실린 12건 가운데 2021년 10월 이후의 10건이다. 날짜는 페이지의 표기이고, 수상 이름·상 이름·발표 주제·수상자는 카드의 표기 그대로다.[^awards]

- 2026 · Outstanding Doctoral Student Scholarship in Science and Engineering, Scholarship from Ministry of Science and ICT and Korea Student and Foundation: 2026 Outstanding Doctoral Student Scholarship in Science and Engineering (수상자 Yujoo Kang)
- 2025.04 · KAIST 2025 Fall Teaching Innovation Award, Teaching Innovation Award: AE42000 Viscous Aerodynamics (수상자 Sang Lee)
- 2024.09 · The 1st Supercomputing Visualization Challenge, Grand Prize: Direct numerical simulation of shock-turbulent boundary-layer interaction (수상자 Yujoo Kang, Sang Lee)
- 2024.09 · The 1st Supercomputing Visualization Challenge, Excellence Award: UAM urban flight simulation visualization (수상자 Sang Lee, Yedam Lee, Hyebin Kim, Donghyun Lee, Yongjae Kim, Byeongheon Yang)
- 2024.09 · The 1st Supercomputing Visualization Challenge, Encouragement Award: UH-60 fuselage and main rotor aerodynamic analysis in forward flight (수상자 Junbeom Park, Taeyeon Kwon, Sang Lee)
- 2024.05 · KSCFE Spring Conference, Best Presentation Paper Award: DNS study of turbulence amplification mechanism in shock-turbulent boundary-layer interaction (수상자 Yujoo Kang, Yedam Lee, Sang Lee)
- 2023.11 · KWEA Fall Conference, Best Presentation Paper Award: Control study of a tension-leg-platform floating offshore wind system (수상자 SeungHwan Yun, Yunjin Ha, Se-Myung Park, Sang Lee)
- 2023.07 · KAIST 2023 Spring Teaching Innovation Award, Teaching Innovation Award: AE37000 Numerical Analysis (수상자 Sang Lee)
- 2023.06 · KWEA Spring Conference, Best Presentation Paper Award: Higher-order dynamic individual pitch control for wake mixing in offshore wind farms using LES (수상자 Yisehak Abreham Keflemariam, SeungHwan Yun, Sang Lee)
- 2022.06 · KWEA Spring Conference, Best Presentation Paper Award: Control study of a DTU 10MW floating offshore wind turbine (수상자 Yisehak Abreham Keflemariam, Eungsoo Kim, Sang Lee)

## 연락과 위치

- 교수실: KAIST N7-2동 3307호[^faculty][^board]
- 교수 이메일과 전화: slee1@kaist.ac.kr, 042-350-3735[^faculty][^board]
- 학생 연구실: N7-2동 3312호(구성원 카드 표기)[^members]
[^home]: 연구실 누리집 첫 화면 <https://cfd.kaist.ac.kr/> (2026-10-23 열람)
[^research]: Research 페이지 <https://cfd.kaist.ac.kr/research> (Research Scope·In-house Code 칸과 연구 분야 여섯 칸; 연구 분야 칸은 페이지가 불러오는 자료 파일 <https://cfd.kaist.ac.kr/data/site-data.js> 의 research 항목, 2026-10-23 열람)
[^methods]: Methods 페이지가 불러오는 자료 파일 <https://cfd.kaist.ac.kr/data/site-data.js> 의 methods 항목(RANS·LES·DNS·ALM·ML 다섯 칸, 2026-10-23 열람)
[^projects]: Projects 페이지 <https://cfd.kaist.ac.kr/projects> (Project Highlights 열 칸; 페이지가 불러오는 자료 파일 <https://cfd.kaist.ac.kr/data/site-data.js> 의 projects 항목, 2026-10-23 열람)
[^pubs]: Publications 페이지 <https://cfd.kaist.ac.kr/publications> (Journal Papers; 페이지가 불러오는 자료 파일 <https://cfd.kaist.ac.kr/data/site-data.js> 의 publications 항목 45편, 2026-10-23 열람)
[^confs]: Conferences 페이지 <https://cfd.kaist.ac.kr/conferences> (Conference Presentations; 페이지가 불러오는 자료 파일 <https://cfd.kaist.ac.kr/data/site-data.js> 의 conferences 항목 53건, 2026-10-23 열람)
[^awards]: Awards 페이지 <https://cfd.kaist.ac.kr/awards> (페이지가 불러오는 자료 파일 <https://cfd.kaist.ac.kr/data/site-data.js> 의 awards 항목 12건, 2026-10-23 열람)
[^members]: Members 페이지 <https://cfd.kaist.ac.kr/members> 와 Research Staff·Student Researchers·Alumni 페이지 (페이지가 불러오는 자료 파일 <https://cfd.kaist.ac.kr/data/site-data.js> 의 members 항목, 2026-10-23 열람)
[^faculty]: Members 페이지 Faculty 칸 <https://cfd.kaist.ac.kr/members-faculty> (교수 카드: 직위, 학력, 경력, 연락처; 페이지가 불러오는 자료 파일 <https://cfd.kaist.ac.kr/data/site-data.js> 의 members.faculty 항목, 2026-10-23 열람)
[^board]: KAIST 항공우주공학과 연구실 소개 「Aerial Innovation Mobility Lab」 <https://ae.kaist.ac.kr/boards/view/board_lab/77> (연구실명, 연구실 소개, 연구분야, 연락처, 2026-10-23 열람)
[^deptlist]: KAIST 항공우주공학과 교수진 목록 <https://ae.kaist.ac.kr/boards/lists/board_faculty/sc_category/1/> (이상봉 항목: 직위, 학력, 연구분야, 2026-10-23 열람)
[^teaching]: Teaching 페이지가 불러오는 자료 파일 <https://cfd.kaist.ac.kr/data/site-data.js> 의 teaching 항목(2020년 봄–2026년 가을 학기별 강의, 2026-10-23 열람)
[^p1]: Y. Kang, S. Lee, Journal of Fluid Mechanics 1036, A47 (온라인 2026-06-05). <https://doi.org/10.1017/jfm.2026.11644> 초록 기준.
[^p2]: Y. Kang, S. Lee, Physics of Fluids 36, 016127 (온라인 2024-01-12). <https://doi.org/10.1063/5.0180077> 초록 기준.
[^p3]: D. Lee, S. Lee, Physics of Fluids 37, 095117 (온라인 2025-09-03). <https://doi.org/10.1063/5.0281564> 초록 기준.
[^p4]: S. H. Park, O. J. Kwon, S. Lee, AIP Advances 12, 045106 (온라인 2022-04-04). <https://doi.org/10.1063/5.0083675> 초록 기준.
[^p5]: J. Park, H. Kim, P. Tsiotras, S. Lee, Physics of Fluids 38, 045136 (온라인 2026-04-14). <https://doi.org/10.1063/5.0324405> 초록 기준.
[^p6]: Y. Kang, S. Lee, Physics of Fluids 36, 125176 (온라인 2024-12-16). <https://doi.org/10.1063/5.0242835> 초록 기준.
[^p7]: E. Lee, S. Lee, Physics of Fluids 37, 097143 (온라인 2025-09-11). <https://doi.org/10.1063/5.0287914> 초록 기준.
[^p8]: M. Ahn, J. Park, S. Lee, Physics of Fluids 38, 055122 (온라인 2026-05-11). <https://doi.org/10.1063/5.0330691> 초록 기준.

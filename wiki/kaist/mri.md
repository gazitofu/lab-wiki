# 자기공명영상 연구실 (Magnetic Resonance Imaging Laboratory)

**KAIST 바이오및뇌공학과 · 박성홍 교수**

- 분야: 자기공명영상(MRI)의 영상 획득·처리·분석 기법 개발, 신경유체 MRI로 뇌 노폐물이 빠져나가는 경로와 기전 규명, 생리·대사·기능 MRI, MRI 촬영 가속과 영상 분석·합성·진단을 위한 딥러닝
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: 과학·공학 AI[^research][^p6], 컴퓨터 비전[^research][^p7], 생성 인공지능[^research][^p7]
- 홈페이지: <https://mri.kaist.ac.kr/>
- 근거와 출처: [자기공명영상 연구실 근거 페이지](mri-sources.md)

> 자기공명영상(MRI)으로 영상을 얻고 처리하고 분석하는 새 기법을 만들고, 신경유체 MRI로 뇌의 노폐물이 빠져나가는 경로와 기전을 밝히며, 딥러닝 알고리즘을 MRI 촬영 가속, 영상 분석과 합성, 임상 진단에 적용하는 바이오및뇌공학과 연구실이다.[^research]

## 무엇을 연구하나

연구실 RESEARCH 화면은 연구 관심을 세 가지로 요약한다. 첫째는 MRI의 영상 획득, 처리, 분석 기법을 새로 개발하는 것, 둘째는 신경유체 MRI(뇌척수액 등 뇌 안팎을 흐르는 액체를 영상으로 재는 MRI)로 뇌 노폐물 배출 경로와 기전을 밝히는 것, 셋째는 딥러닝 알고리즘을 MRI 가속, 영상 분석과 합성, 임상 진단에 적용하는 것이다.[^research] 같은 화면은 이를 다섯 연구 주제로 나눠 설명한다. 신경유체 영상으로 뇌 노폐물 배출 경로와 기전을 밝히는 연구, 생리·대사·기능 MRI, MRI 가속을 위한 딥러닝, 영상 분할·합성과 질병 진단을 위한 딥러닝, 그리고 이 기법들을 모아 여러 뇌 질환을 여러 지표로 평가하는 의생명 응용이다.[^research]

연구실은 사람과 동물을 대상으로 영상 기법을 만든다.[^research] FACILITY 화면은 연구실 장비로 3T 전임상 동물 MRI 스캐너(MR Solutions), 냉매가 필요 없는 초전도 자석, Endoscout 위치 추적 장치(Robin Medical)를 들고, 실험 대상으로 생쥐 종양 모델과 쥐를 든다.[^facility]

바이오및뇌공학과 교수진 목록은 교수의 연구분야를 구조/생리/기능 자기공명영상, 머신러닝 기반 의료영상 획득/분석/진단, 뇌질환 진단/예후, 이미징 바이오마커로 적고, 교수 소개 페이지는 구조/생체/기능 자기공명영상, 머신러닝을 이용한 의료영상, 수술중 자기공명영상, 뉴런전류 자기공명영상으로 적는다.[^deptlist][^deptprof]

## 주요 연구 주제

### 1. 신경유체 MRI: 뇌 노폐물이 빠져나가는 경로와 기전

RESEARCH 화면은 치매 연구가 베타 아밀로이드와 타우 같은 독성 단백질에 집중해 왔지만 뇌가 이런 노폐물을 내보내는 기전은 아직 분명하지 않다고 적는다. 2015년 Nature 논문으로 뇌의 수막 림프관이 알려진 뒤 뇌 노폐물 배출 연구가 활발해졌으나, 관련된 흐름이 느려 영상으로 보기 어렵고 흐름이나 박동을 정량하기는 더 어렵다고 설명한다. 한국과 미국을 포함한 여러 나라에서 뇌척수액에 조영제를 직접 넣는 것이 허용되지 않아 비침습 영상 기법(몸에 칼을 대거나 무언가를 넣지 않고 찍는 기법)의 개발이 중요하다고 밝힌다. 연구실은 사람과 동물에서 수막 림프계, 뇌척수액, 글림프 시스템의 기능을 체계적이고 정량적으로 재는 비침습 영상 기법을 개발한다.[^research]

대표 논문 1은 층과 층 사이 혈류를 영상으로 만드는 MRI 기법 ALADDIN에 반전 회복을 더한 IR-ALADDIN으로 사람의 수막 림프관을 찾아내고 그 유속을 쟀다.[^p1] 대표 논문 2는 흔히 쓰는 에코 평면 영상 기반 기능 MRI 자료에서 뇌척수액 박동을 정량하는 지표 CSFpulse를 제안했다.[^p2] 목록에는 시신경 둘레 공간의 뇌척수액 흐름을 자세에 따라 잰 연구(2025), 뇌혈류와 뇌척수액 흐름을 함께 재는 방법(2025), 젊은 성인의 지주막하 공간에서 확산 이방성이 나이에 따라 바뀌는 양상을 잰 연구(2024)도 있다.[^pubs]

### 2. 생리·대사·기능 MRI

RESEARCH 화면은 혈관, 혈류, 혈액 투과성, 혈액 산소 수준 의존(BOLD, Blood Oxygen Level Dependent) 신호를 비침습으로 영상화하는 것이 뇌 질환의 원인과 뇌 기능을 이해하는 중요한 단계라고 적는다. 연구실은 한 번의 MRI 촬영으로 동맥과 정맥을 화질을 해치지 않고 함께 찍는 방법, 뇌와 신장의 혈액 관류를 비침습으로 지도화하는 방법, 뇌 기능을 높은 공간 해상도로 지도화하는 방법을 개발한다. 이 기법들은 뇌종양과 뇌졸중 같은 질환의 이해, 신장 기능의 비침습 지도화, 고해상도 기능 MRI의 신호 출처 이해에 쓰였다고 밝힌다. 생리·대사·기능 MRI에 흔히 쓰는 단일 촬영 에코 평면 영상(EPI, Echo Planar Imaging)의 화질도 개선해 왔다.[^research]

대표 논문 3은 신장의 산소 소비를 사람에서 정량 지도로 그리는 방법을, 대표 논문 4는 혈뇌장벽을 지나는 물의 교환율과 관류를 함께 추정하는 방법을 제안했다.[^p3][^p4] 목록에는 에코 평면 영상의 왜곡을 한 번 얻은 자료로 바로잡는 TASK 알고리즘(2023), 자화 준비 영상을 위한 단일 촬영 의사 중심 EPI(2021), 신장 사구체의 혈액 전달률 측정(2022), 7T 장비로 찍는 사람 뇌의 확산 강조 화학 교환 포화 전이 영상(2026)도 있다.[^pubs]

### 3. MRI 가속과 정량 지도화를 위한 딥러닝

RESEARCH 화면은 MRI 인공물 억제, 잡음 제거, 빠른 자료 획득을 위한 딥러닝 알고리즘을 개발하고 적용한다고 적는다. 시뮬레이션 기반 물리 정보 신경망은 실제 정답을 따로 측정할 필요가 없어 일반화 능력이 높고 적용 범위가 넓은 접근으로 소개하고, 조직 변수를 정량 지도화하는 데 드는 긴 처리 시간을 딥러닝으로 크게 줄일 수 있다고 설명한다.[^research]

대표 논문 5는 균형 정상상태 자유 세차 영상에서 여러 조직 변수를 한꺼번에 지도화하는 물리 기반 신경망을, 대표 논문 6은 동적 자화율 대조 MRI의 관류 계산을 시뮬레이션 자료만으로 학습한 신경망으로 푸는 SPINNED를 제안했다.[^p5][^p6] 목록에는 정량 자화 전이 영상을 신경망으로 가속하는 qMTNet(2021), 위상 순환 bSSFP 정량 자화 전이 영상에 물리 기반 시뮬레이션 학습 신경망을 쓰는 SIMPLEX(2023), 여러 대비 영상을 함께 가속하는 표본 추출 패턴 최적화(2022), 딥러닝 기반 가속 MRI 재구성 방법의 리뷰(2024)도 있다.[^pubs]

### 4. 영상 분할·합성과 질병 진단을 위한 딥러닝

RESEARCH 화면은 딥러닝을 장기와 병변의 분할, 영상 합성, 여러 질병의 진단에 쓰며, 연구실은 분할, 진단·예후·치료 계획과 모니터링을 위한 딥러닝 알고리즘을 개발하고 적용한다고 적는다. 같은 화면은 Huan Minh Luu가 2021 Brain Tumor Segmentation Challenge(BRATS)에서 전 세계 2200 참가자(competitors) 가운데 1위를 했다고 소개한다.[^research]

대표 논문 7은 MR 영상만으로 방사선 치료 계획을 세울 수 있도록 MR에서 합성 CT와 그 장기 분할을 함께 만드는 CycleSeg를, 대표 논문 8은 여러 MR 촬영 프로토콜의 정보를 합쳐 대퇴골두 무혈성 괴사의 병기를 판정하는 신경망을 제안했다.[^p7][^p8] 목록에는 여러 딥러닝 방법으로 MR에서 만든 합성 CT를 전립선암 방사선 치료 계획에 쓸 수 있는지 비교한 연구(2022)와 동적 혈관 MRI에서 딥러닝으로 관류 지도를 얻는 연구(2023)도 있다.[^pubs]

### 5. 의생명 응용

RESEARCH 화면은 이 영상 기법들을 모아 여러 뇌 질환을 여러 지표로 평가해 왔고, 공학자, 신경과학자, 임상의가 함께 하는 학제 간 공동 연구를 기대한다고 적는다.[^research] 목록에는 활성산소에 반응하는 빌리루빈 나노입자와 나노버블을 MRI·초음파 영상 조영제로 쓰는 공동 연구(2024, 2026)도 있다.[^pubs]

## 대표 논문

박성홍 교수는 2012년부터 KAIST 바이오및뇌공학과에 있어 2021–2026년 논문은 모두 KAIST 재직 시기 논문이다. 이 가운데 교수가 마지막 저자이고 초록을 확인할 수 있는 논문을, RESEARCH 화면의 네 연구 갈래(신경유체 MRI, 생리·대사·기능 MRI, MRI 가속과 정량 지도화, 영상 분할·합성과 진단)마다 두 편씩 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2023 | [Non-invasive flow mapping of parasagittal meningeal lymphatics using 2D interslice flow saturation MRI](https://doi.org/10.1186/s12987-023-00446-z) · Fluids and Barriers of the CNS | 사람에서 뇌 노폐물이 빠져나가는 경로는 아직 논쟁 중인데, 그 이유의 하나는 수막 림프관(뇌를 싸는 막에 있는 림프관)을 비침습으로 찍는 기술이 없기 때문이다. 이 논문은 층 사이 혈류를 영상으로 만드는 MRI 기법 ALADDIN에 반전 회복(IR: 자기 신호를 뒤집은 뒤 정해진 시간을 기다려 찍는 방식)을 더한 IR-ALADDIN을 제안했다. 반전 시간 2300 ms 한 번으로 찍는 방식은 사람의 상시상정맥동(머리 꼭대기 가운데를 앞뒤로 지나는 정맥 통로) 둘레의 수막 림프관을, 앞서 제안된 비침습 기법들보다 높은 검출력과 특이도로 보여 주었다. 찾아낸 혈관이 뒤에서 앞으로 흐르는 방향, 속도, 모양이 문헌과 맞아 수막 림프관임을 확인했고, 조영제를 쓴 흑혈 영상(혈액 신호를 지워 어둡게 나타내는 영상)과도 비교했다. 반전 시간을 2000, 2300, 2600 ms로 바꿔 찍는 방식으로 흐름 모형(유속을 아는 실험 장치)과 사람에서 유속을 쟀고, 예비 결과로 사람 등쪽 수막 림프관의 유속은 2.2–2.7 mm/s였다. 한 반전 시간 방식은 뇌 전체를 약 17분에, 여러 반전 시간 방식은 제한된 범위를 약 10분(또는 그보다 짧게)에 찍을 수 있다.[^p1] | 1저자 J.-H. Kim(Jun-Hee Kim), 마지막 저자 박성홍 (4명) |
| 2 | 2022 | [Measurement of CSF pulsation from EPI-based human fMRI](https://doi.org/10.1016/j.neuroimage.2022.119293) · NeuroImage | 글림프 시스템과 수막 림프 시스템이 뇌 노폐물을 치우는 주요 경로로 밝혀졌고, 뇌척수액(CSF) 흐름이 이 과정을 돕는다. 하지만 뇌척수액 흐름과 뇌 기능 활동의 관계는 덜 연구되었고, 최근 연구들이 기능 MRI의 가장자리 단면에서 잰 뇌척수액 유입 지표(CSFedge)를 제안했으나 박동을 정량하는 면이 부족했다. 이 논문은 제4뇌실(뇌 아래쪽의 뇌척수액이 차 있는 공간)에서 층 사이 뇌척수액 박동 모형을 세워, 에코 평면 영상 기반 기능 MRI로 뇌척수액 박동을 정량하는 새 방법 CSFpulse를 제안했다. CSFpulse는 쉬는 상태의 뇌척수액 흐름이 시각·운동 과제 상태보다 높다는 것을 찾아냈는데(p<.05), 이는 위상대조(PC) MRI(흐르는 액체의 속도를 신호의 위상으로 재는 MRI)와 뇌척수액 부피 MRI를 쓴 선행 연구와 맞고, CSFedge 기반 지표나 관심 영역의 기본 신호로는 찾지 못했다. 과제 활성 구간에서는 줄고 쉬는 구간에서는 늘어 뇌척수액 박동의 기능적 변화를 보였다. 뇌척수액 박동 정량의 표준 방법인 PC MRI로 잰 박출량과 유의하게 상관했고, 뇌 전체 BOLD 신호와의 상관은 CSFedge보다 약했다. CSFpulse는 PC MRI보다 훨씬 빠르고 뇌 기능 활성화 정보도 함께 준다.[^p2] | 1저자 J.-H. Kim(Jun-Hee Kim), 둘째 저자 J.-G. Im(Jae-Geun Im)(두 사람에게 누리집의 동등 기여 표시 #), 마지막 저자 박성홍 (3명) |
| 3 | 2025 | [Quantitative mapping of renal oxygen consumption using pseudo-continuous arterial spin labeling and quantitative susceptibility mapping in humans](https://doi.org/10.1002/mrm.30288) · Magnetic Resonance in Medicine | 신장의 산소 대사율을 정량 지도로 그리는 새 방법을 제안하고 카페인 섭취 조건으로 평가했다. 유사 연속 동맥 스핀 표지(pCASL: 혈액을 자기적으로 표시해 조영제 없이 혈류를 재는 MRI)와 정량 자화율 지도화(QSM: 조직이 자기장에 반응하는 정도를 계산해 지도로 그리는 MRI 기법) 영상을 신장에서 얻어 DICOM(의료 영상 파일의 표준 형식)에 담긴 정보와 평행 이동으로 서로 맞추고, 픽 원리(혈류와 들어오고 나가는 혈액의 산소 차이로 소비량을 구하는 원리)로 산소 대사율을 추정했다. 건강한 자원자 6명을 카페인을 먹은 날과 대조 날에 찍었다. 추정한 신장 혈류, QSM, 산소 대사율 지도는 문헌 보고와 맞았고, 신장 산소 대사율은 뇌의 산소 대사율보다 높았으며 카페인을 먹은 날에 대조 날보다 유의하게 줄어 MRI가 아닌 방법의 문헌과도 맞았다. 저자들은 사람 신장의 산소 소비 정량 지도를 처음 제시했다고 적고, 조영제 합병증이 있는 환자의 신장 산소 소비를 비침습으로 재는 쓰임을 제시했다.[^p3] | 1저자 Y. Jung(Yujin Jung), 마지막 저자 박성홍 (3명) |
| 4 | 2026 | [Estimating blood-brain barrier exchange rate using diffusion-weighted arterial spin labeling and physics-guided neural networks](https://doi.org/10.1016/j.neuroimage.2026.122132) · NeuroImage | 여러 단면을 여러 지연 시간으로 찍는 확산 강조 동맥 스핀 표지(DW-ASL) MRI에서 관류와 혈뇌장벽(혈액과 뇌 조직 사이에서 물질이 드나드는 것을 가려 막는 혈관 벽 구조)의 물 투과성 변수를 추정하는 물리 기반 신경망(PgNN: 물리 모형을 학습에 함께 쓰는 신경망) 방법을 제안했다. 두 구획 관류 모형에 물이 통과하지 않는 동맥 구획을 더해 물 교환율, 뇌혈류, 동맥 통과 시간을 함께 추정하게 했다. 젊은 건강인 9명, 고령 건강인 3명, 알츠하이머병 고령 환자 4명, 모두 16명의 자료를 얻었고, 단면을 찍는 순서를 바꿔 여러 지연 시간을 얻었다. 물리 모형으로 만든 합성 신호로 학습한 뒤 각 시험 자료에 맞추는 다층 퍼셉트론(층을 여러 겹 쌓은 기본 신경망) 기반 PgNN과, 사전 학습 없이 물리 모형으로 시험 자료에 맞추는 3차원 U-Net(영상 처리에 흔히 쓰는 신경망 구조) 기반 PgNN 두 가지를 만들었으며, 둘 다 실제 생체 자료로 학습할 필요가 없다. 두 방법 모두 기존 수치 계산법인 ADMM과 비선형 최소제곱법보다 정확도와 잡음에 대한 강건성이 좋았다. 고령자에서 물 교환율은 낮고 동맥 통과 시간은 길었으며, 물 교환율 감소는 알츠하이머병 집단에서 더 뚜렷했다.[^p4] | 1저자 H.-S. Ahn(Hyun-Seo Ahn), 마지막 저자 박성홍, 첫 세 저자에게 누리집의 동등 기여 표시 # (9명) |
| 5 | 2026 | [Physics-guided neural network for quantitative parameter mapping using balanced steady state free precession MRI](https://doi.org/10.1002/mrm.70411) · Magnetic Resonance in Medicine | 균형 정상상태 자유 세차(bSSFP: 짧은 간격으로 신호를 되풀이해 얻는 MRI 촬영 방식) 영상으로 여러 조직 변수를 지도화하는 물리 기반 신경망 방법을 제안했다. 회백질, 백질, 뇌척수액에 해당하는 범위에서 고르게 뽑은 조직 변수로 위상 순환 각도 여섯 가지의 bSSFP 신호를 8천만 개 넘게 시뮬레이션해 다층 퍼셉트론을 학습시켰고, 변수 항과 재구성 신호 항을 합친 L2 손실(오차의 제곱을 더해 재는 학습 기준)을 썼다. 시험 자료에 맞추는 적응을 한 경우와 하지 않은 경우를 모두 얻었다. BrainWeb의 뇌 디지털 모형 10개와 3T 장비로 찍은 10명의 생체 자료에서 비교 방법인 PLANET과 CELF보다 지도의 정확도와 일관성이 눈으로 보나 수치로 보나 좋았고, 적응을 한 경우가 하지 않은 경우보다 좋았다. 추정한 변수로 찍지 않은 위상 순환 각도와 숙임각(자기 신호를 기울이는 각도)의 영상을 더 정확히 재구성해 일반화 능력을 시사했다. 시뮬레이션 자료만으로 학습한 이 신경망은 임상에서 받아들일 만한 7분 촬영으로 높은 공간 해상도의 여러 변수 지도를 얻게 한다.[^p5] | 1저자 H.-R. Choi(Hye-Ryeong Choi), 마지막 저자 박성홍 (3명) |
| 6 | 2024 | [SPINNED: Simulation-based physics-informed neural network for deconvolution of dynamic susceptibility contrast MRI perfusion data](https://doi.org/10.1002/mrm.30095) · Magnetic Resonance in Medicine | 동적 자화율 대조(DSC) MRI(조영제가 뇌혈관을 지나는 동안 신호 변화를 연속으로 찍어 관류를 재는 방법)의 디컨볼루션(잰 신호에서 동맥으로 들어온 조영제의 영향을 풀어내 조직의 반응을 구하는 계산)을 위해, 시뮬레이션 기반 물리 정보 신경망 SPINNED를 제안했다. 수학적 시뮬레이션으로 조직 잔류 함수(조직에 남은 조영제 양의 시간 변화)와 동맥 입력 함수(동맥으로 들어오는 조영제 농도의 시간 변화)를 만들고 이를 써서 합성 DSC 시계열을 만든 뒤, 시계열과 동맥 입력 함수 사이의 물리 관계를 신경망이 배우게 했다. 흔히 쓰는 두 디컨볼루션 방법인 순환 특이값 분해, 볼테라 특이값 분해(둘 다 행렬을 나누어 푸는 기존 계산법)와 시뮬레이션 자료와 실제 환자 자료로 비교했다. SPINNED는 모든 신호 대 잡음비 수준에서 기존 방법들보다 정확했고, 두 자료 모두에서 잡음에 더 강했으며, 처리 속도도 훨씬 빨랐다. 학습에 따로 잰 정답이 필요 없다.[^p6] | 1저자 M. Asaduddin(Muhammad Asaduddin), 마지막 저자 박성홍 (3명) |
| 7 | 2024 | [CycleSeg: Simultaneous synthetic CT generation and unsupervised segmentation for MR-only radiotherapy treatment planning of prostate cancer](https://doi.org/10.1002/mp.16976) · Medical Physics | MR 영상만으로 방사선 치료 계획을 세우면 촬영 시간과 전리 방사선 노출을 줄일 수 있는데, 그러려면 MR에서 선량 계산에 쓸 전자 밀도 지도나 합성 CT를 얻어야 하고, 장기를 자동으로 분할하면 손으로 윤곽을 그리는 시간을 줄일 수 있다. 그러나 분할 정답은 많은 경우 CT에만 있다. 이 논문은 MR 분할 정답 없이 MR에서 합성 CT와 그 분할을 함께 만드는 통합 틀 CycleSeg를 제안했다. 짝지어지지 않은 영상으로 합성 CT를 만들고 영상을 맞추는 CycleGAN 방식을 쓰고, 의미 분할 공간에서 특징을 맞추는 의사 표지(모델이 스스로 붙인 임시 정답) 방식의 비지도 도메인 적응(정답이 없는 영상 종류에 모델을 맞추는 방법)을 넣어 MR과 합성 CT 모두를 분할하게 했다. 전립선암 환자 자료(학습 78명, 검증 7명, 시험 10명)에서 합성 CT 생성에서 평균 절대 오차 102.2, 프레셰 인셉션 거리(합성 영상의 통계가 실제 영상과 다른 정도를 재는 지표) 13.0으로 가장 좋은 결과를 냈고, 분할도 평균 다이스 점수(분할 결과가 정답과 겹치는 정도) 81.0(MR), 81.1(합성 CT)로 가장 좋았으며, 절제 실험(구성 요소를 하나씩 빼며 기여를 보는 실험)으로 각 구성 요소의 기여를 확인했다.[^p7] | 1저자 H. M. Luu(Huan Minh Luu), 둘째 저자 G. S. Yoo(Gyu Sang Yoo)(두 사람에게 누리집의 동등 기여 표시 #), 마지막 저자 박성홍 (4명) |
| 8 | 2023 | [Attention fusion network with self-supervised learning for staging of osteonecrosis of the femoral head (ONFH) using multiple MR protocols](https://doi.org/10.1002/mp.16380) · Medical Physics | 대퇴골두 무혈성 괴사(ONFH: 엉덩관절에서 넓적다리뼈 위쪽 끝의 뼈세포가 죽는 병)의 병기 판정은 흔히 MRI와 CT로 한다. 이 논문은 CT 촬영의 추가 비용과 방사선 노출을 줄이도록 MR 영상만으로 병기를 판정하는 딥러닝 모델을 제안했다. 다섯 가지 촬영 프로토콜의 MR 영상 정보를 한 영상 종류 안의 주의와 영상 종류 사이의 주의(신경망이 입력의 어느 부분에 무게를 둘지 스스로 정하는 방법)로 된 새 주의 융합 방법으로 합쳤다. 또 많은 MR-CT 짝 자료로 자기 지도 학습(정답 표시 없이 자료 자체에서 학습 과제를 만들어 배우는 방법)을 해, MR을 CT로 바꾸는 신경망의 인코더를 병기 판정의 사전 학습 신경망으로 써서 병기 정답 자료가 적은 문제를 넘으려 했다. ARCO 병기 네 단계 분류의 AUROC(분류 성능을 나타내는 지표)를 일반 VGG 신경망보다 6.8%p 높였고, 절제 실험에서 자기 지도 학습이 4.7%p, 주의 융합이 2.6%p를 높였다.[^p8] | 1저자 B. Kim(Bomin Kim), 마지막 저자 박성홍 (3명) |

## 교수와 전문 분야

박성홍 교수는 KAIST 바이오및뇌공학과 부교수(Associate Professor)다. 연구실 PEOPLE 화면과 학과 교수 소개는 KAIST 바이오및뇌공학과 조교수(2012년 2월–2016년 8월)를 거쳐 2016년 9월부터 부교수로 적는다.[^prof][^deptprof] 그 전에는 University of Pittsburgh 영상의학과(Department of Radiology) 조교수(2010년 9월–2012년 1월), University of Texas Health Science Center at San Antonio의 Research Imaging Institute 연구조교수(Research Assistant Professor, 2009년 7월–2010년 8월)였고, University of Pittsburgh 신경생물학과 연구원(Research Fellow, 2003년 6월–2004년 12월), Medison(1998년 3월–2000년 4월)과 ISOL Technology(2000년 5월–2003년 5월)의 연구원(Research Associate)으로도 일했다.[^prof][^deptprof] 학력은 KAIST 전기공학 학사(1995년)와 석사(1998년), University of Pittsburgh 생명공학(Bioengineering) 박사(2009년)다.[^prof]

학과 교수 소개는 수상으로 BRIC 생물학연구정보센터의 2019년 국내 바이오분야 의과학부문 Top5 연구성과 선정, KAIST 이수영교수학습혁신상(2019년 5월), 대한자기공명의과학회 제13차 학술대회 Bracco Young Investigator Award(2008년)를 적고, 학회 활동으로 대한자기공명의과학회 학술이사(2018년 4월–현재)·정보이사(2016년 4월–2018년 3월)·학술위원·교육위원, 한국자기공명학회 학술이사(2014년 8월–2015년 4월)를 적는다.[^deptprof] 연구실 첫 화면 Lab News는 교수의 「departmental instructor award」 수상(2018년 2월)과, 중추신경계와 눈의 림프계와 관련 MR 영상 기법을 다룬 Henry Stewart Talks 온라인 강연 공개(2026년 4월 30일)를 알렸다.[^news]

전문 분야는 MRI 영상 기법 개발과 머신러닝을 이용한 의료영상이다.[^deptlist][^deptprof] 학과 교수 소개는 대표 연구실적으로 뇌척수액 박동 측정(대표 논문 2)과 함께, 두개골 바닥의 수막 림프관이 뇌척수액을 배출한다는 Nature 2019년 논문(학과 페이지가 교수와 Gou Young Koh 이름 뒤에 * 표시), 가변 두께 이중 에코 TOF 혈관 영상과 자화율 강조 영상을 함께 얻는 연구(IEEE Transactions on Medical Imaging, 2018년), 딥러닝으로 동맥 스핀 표지를 개선한 연구(Radiology, 2018년) 등을 든다.[^deptprof] KAIST에서는 신경유체 MRI, 생리·대사 MRI, 물리 기반 신경망을 쓴 정량 MRI와 영상 분석 딥러닝 연구를 이어 오고 있다(대표 논문 1–8).[^p1][^p3][^p5][^p7]

## 응용 분야

RESEARCH 화면은 뇌 노폐물 배출 기전을 사람에서 정확히 이해하면 치매 같은 신경 퇴행성 뇌 질환의 조기 발견과 치료에 쓸 수 있다고 적는다. 또 혈관·관류 영상 기법이 뇌종양과 뇌졸중 같은 질환의 이해와 신장 기능의 비침습 지도화에 쓰였고, 영상 분석 딥러닝을 여러 질병의 진단·예후·치료 계획과 모니터링에 쓴다고 밝힌다.[^research] 대표 논문 7은 MR 영상만으로 하는 방사선 치료 계획, 대표 논문 8은 CT 없이 MR만으로 하는 질병 병기 판정, 대표 논문 3은 조영제 합병증이 있는 환자의 신장 산소 소비 측정을 쓰임으로 든다.[^p7][^p8][^p3]

## 구성원

PEOPLE 화면의 「Graduate Students」 13명(박사과정 8명, 석사과정 5명)과 「Visiting researcher」 1명, 모두 14명이다. 시작 칸은 각 카드의 현재 과정 시작 연월이고, 박사과정 6명의 카드에는 앞서 마친 석사 과정 기간도 적혀 있다. 이메일은 카드에 적힌 KAIST 주소다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Seonghyuk Kim | 박사과정 | 2024.03 | tjdgur1214@kaist.ac.kr | 4 |
| Sojeong Kim | 박사과정 | 2024.03 | sojeong990810@kaist.ac.kr |  |
| Dongho Shin | 박사과정 | 2024.09 | lencute@kaist.ac.kr |  |
| HyeRyeong Choi | 박사과정 | 2025.03 | hyeryeongchoi@kaist.ac.kr | 5 |
| Minjae Kim | 박사과정 | 2025.09 | ljsmd0703@kaist.ac.kr |  |
| HyoSeok Lee | 박사과정 | 2025.09 | hyord@kaist.ac.kr |  |
| Youngeun Jeon | 박사과정 | 2026.03 | jeonye96@kaist.ac.kr |  |
| Titouan LE GOURRIEREC | 박사과정 | 2026.09.01 | titouanlegourrierec@kaist.ac.kr | 4 |
| Wooseung Kim | 석사과정 | 2025.03 | wooseung.kim@kaist.ac.kr |  |
| Napasara Asawalertsak | 석사과정 | 2025.09 | napasara.asa@kaist.ac.kr |  |
| JongHyeok Lee | 석사과정 | 2025.09 | dlwhdgur317@kaist.ac.kr |  |
| Zhipeng Zou | 석사과정 | 2026.09 | zhipeng.zou@kaist.ac.kr |  |
| Stefani Xiadani Gonzalez Garcia | 석사과정 | 2026.09 | stefanigonzalez@kaist.ac.kr |  |
| Xiaohan Hao | 방문 연구원 |  |  |  |

## 졸업생과 이전 구성원

PEOPLE 화면 「Past Members」 칸의 20명 전부다. 박사 학위 13명, 박사과정 기간만 적힌 1명, 석사 학위 6명이다. 학위·과정 칸은 카드에 적힌 학위·과정과 기간 그대로이고, 진로 칸은 카드의 진로 줄 그대로다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Paul Kyu Han | PhD degree (2013.03 - 2016.07) | Assistant Professor at Yale University School of Medicine, USA |
| Ki-Hwan Kim | PhD degree (2014.03 - 2018.01) | Clinical Director in Lunit Inc. |
| Jae-Woong Kim | PhD degree (2015.03 - 2019.02); MS degree (2013.03 - 2015.02) | Researcher in Samsung Display |
| Won-Joon Do | PhD degree (2015.09 -2019.02); MS degree (2013.09 - 2015.08) | Researcher in Samsung Electronics |
| Hyun-Soo Lee | PhD degree (2016.03 - 2020.08); MS degree (2014.03 - 2016.02) | Researcher in Siemens Korea |
| Hyo-Im Heo | PhD Student (2017.03 - 2020.01); MS degree (2015.03 - 2017.02) | Researcher in Net Protections Inc. |
| Hyun-Seo Ahn | PhD degree (2018.03 - 2022.02); MS degree (2016.03 - 2018.02) | Researcher in Samsung Electronics |
| Sung-Hun Seo | PhD degree (2018.03 - 2022.02); MS degree (2016.03 - 2018.02) | Researcher in Samsung Electronics |
| Huan Minh Luu | PhD degree (2019.09 - 2023.08); MS degree (2017.09 - 2019.08) | Researcher in Samsung Electronics |
| Jun-Hee Kim | PhD degree (2020.03 - 2024.02); MS degree (2018.03 - 2020.02) | Research Professor in Seoul National University Hospital. |
| Muhammad Asaduddin | PhD degree (2020.03 - 2024.02); MS degree (2018.03 - 2020.02) | Researcher in Samsung Electronics |
| JaeGeun Im | PhD Degree (2020.09 - 2025.02) | CEO in BrainTracer |
| Seon-Ha Hwang | PhD degree (2021.03 - 2025.02); MS degree (2019.03 - 2021.02) | Researcher in Samsung Electronics |
| Yujin Jung | PhD Degree (2021.09 - 2025.08); MS degree (2019.09 - 2021.08) | Postdoc in Korea University Medical Center |
| Sul-Li Lee | MS degree (2014.09 - 2016.08) | Researcher in SK Hynix |
| Ji-Yong Um | MS degree (2015.03 - 2017.02) | Researcher in Vieworks |
| Je-Seok Ham | MS degree (2017.03 - 2019.02) | Researcher in ETRI |
| Dong-Hyun Kim | MS degree (2017.09 - 2019.07) | Researcher in ETRI |
| Bomin Kim | MS degree (2021.03 - 2022.12) | Researcher in Kakao |
| Jaa Yeon Lee | MS Degree (2021.09 - 2023.08) | PhD Student at KAIST |

## 최근 논문 목록 (2021–2026)

PUBLICATIONS 화면 International Publications의 Papers 목록에서 2021–2026년 구역에 있는 32편 가운데 25편이다(2026년 4, 2025년 3, 2024년 5, 2023년 5, 2022년 6, 2021년 2). 저자·제목·학술지 표기와 링크는 누리집 그대로다. 누리집은 #을 동등 기여(equal contributions) 표시로, 밑줄을 교신 저자 표시로 쓴다고 적으며, 이 목록은 글자만 싣는다. 2026년 Scientific Reports 논문의 「in press」도 누리집 표기다.[^pubs]

- 같은 화면의 Book Chapter, Meeting Abstracts and Conference Paper, Domestic Publications의 Papers와 Meeting Abstracts and Conference Paper 목록에는 2021년 이후 항목이 없다.[^pubs]
- 의생명 연구는 자연·공학과 직접 연계된 연구만 싣는 이 위키의 수록 범위에 따라 논문마다 확인했고, 영상 기법·알고리즘·조영제 개발이나 정량 측정 연구로 확인된 논문만 목록에 있다. 질병 기전이나 임상 관찰이 중심이거나 기존 영상 지표·재구성 기법을 환자 자료에 적용한 7편은 이 목록에 없다(판정과 사유는 근거 페이지).

**2026**

- Yujin Jung#, Youngeun Jeon#, Jaeseok Park, Seong-Gi Kim, and Sung-Hong Park, Diffusion-weighted chemical exchange saturation transfer MRI in the human brain at 7T, Scientific Reports 2026, in press, https://doi.org/10.1038/s41598-026-65594-2
- Hyun-Seo Ahn#, Titouan Le Gourrierec#, Yujin Jung#, Seonghyuk Kim, Seon-Ha Hwang, Jaeseok Park, Dong Young Lee, Chul Ho Sohn, and Sung-Hong Park, Estimating blood-brain barrier exchange rate using diffusion-weighted arterial spin labeling and physics-guided neural networks. NeuroImage, 2026;338(1);122132, https://dx.doi.org/10.1016/j.neuroimage.2026.122132
- Wonsik Jung#, Youngju Son#, Dong Yun Lee, Youngeun Jeon, Muhammad Asaduddin, Sung-Hong Park, and Sangyong Jon, ROS-responsive nanobubbles for dual-enhanced Ultrasound and magnetic resonance imaging of tumor oxidative stress, Advanced Science, 2026;13(14):e00071, https://dx.doi.org/10.1002/advs.202600071
- Hye-Ryeong Choi, Huan Minh Luu, and Sung-Hong Park, Physics-guided neural network for quantitative parameter mapping using balanced steady state free precession MRI, Magnetic Resonance in Medicine 2026;96(3):1313-1322, https://dx.doi.org/10.1002/mrm.70411

**2025**

- Minjae Kim and Sung-Hong Park, Posture-dependent cerebrospinal fluid flow measurement in the optic nerve subarachnoid space using multi-delay 2D interslice saturation MRI, Brain Research Bulletin 2025;232:111620, https://dx.doi.org/10.1016/j.brainresbull.2025.111620.
- Jae-Geun Im, Jun-Hee Kim, and Sung-Hong Park, Simultaneous measurement of cerebral blood flow and cerebrospinal fluid flow using pseudo-continuous arterial spin labeling, NeuroImage, 2025;311:121192, https://doi.org/10.1016/j.neuroimage.2025.121192
- Yujin Jung, Hyun-Seo Ahn, and Sung-Hong Park, Quantitative mapping of renal oxygen consumption using pseudo-continuous arterial spin labeling and quantitative susceptibility mapping in humans, Magnetic Resonance in Medicine, 2025;93(2):699-708, https://doi.org/10.1002/mrm.30288

**2024**

- Yujin Jung and Sung-Hong Park, Age-related brain-region-specific changes in diffusion anisotropy in subarachnoid space of young adults, Neuroscience 2024;560:36-42, https://doi.org/10.1016/j.neuroscience.2024.09.023
- Seonghyuk Kim, HyunWook Park, and Sung-Hong Park, A review of deep learning-based reconstruction methods for accelerated MRI using spatiotemporal and multi-contrast redundancies, Biomedical Engineering Letters, 2024;14(6):1221-1242, https://doi.org/10.1007/s13534-024-00425-9
- Wonsik Jung#, Muhammad Asaduddin#, Hyeongseop Keum, Youngju Son, Dohyun Yoo, Dohyeon Kim, Seojung Lee, Dong Yun Lee, Jin Roh, Sung-Hong Park, and Sangyong Jon, Longitudinal Magnetic Resonance Imaging with ROS-Responsive Bilirubin Nanoparticles Enables Monitoring of Nonalcoholic Steatohepatitis Progression to Cirrhosis, Advanced Materials, 2024;36(24):2305830, https://doi.org/10.1002/adma.202305830
- Muhammad Asaduddin, Eung Yeop Kim, and Sung-Hong Park, SPINNED: Simulation-based physics-informed neural network for deconvolution of dynamic susceptibility contrast MRI perfusion data, Magnetic Resonance in Medicine, 2024;92(3):1205-1218, https://doi.org/10.1002/mrm.30095
- Huan Minh Luu#, Gyu-Sang Yoo#, Won Park, and Sung-Hong Park, CycleSeg: Simultaneous synthetic CT generation and unsupervised segmentation for MR-only radiotherapy treatment planning of prostate cancer, Medical Physics 2024;51(6):4365-4379, https://doi.org/10.1002/mp.16976

**2023**

- Huan Minh Luu and Sung-Hong Park, SIMPLEX: Multiple phase-cycled bSSFP quantitative magnetization transfer imaging with physics-guided simulation learning of neural network, NeuroImage 2023;284:120449, https://doi.org/10.1016/j.neuroimage.2023.120449
- Seon-Ha Hwang, Hyun-Soo Lee, Seung Hong Choi, and Sung-Hong Park, Distortion correction using topup algorithm by single k-space (TASK) for echo planar imaging, Scientific Reports, 2023;13(1):18751, https://doi.org/10.1038/s41598-023-46163-3
- Jun-Hee Kim, Roh-Eul Yoo, Seung Hong Choi, and Sung-Hong Park, Non-invasive flow mapping of parasagittal meningeal lymphatics using 2D interslice flow saturation MRI, Fluids and Barriers of the CNS, 2023;20(1):37, https://doi.org/10.1186/s12987-023-00446-z
- Bomin Kim, Geun Young Lee, and Sung-Hong Park, Attention Fusion Network with Self-supervised Learning for Staging of Osteonecrosis of the Femoral Head (ONFH) Using Multiple MR Protocols, Medical Physics, 2023;50(9):5528-5540, https://doi.org/10.1002/mp.16380
- Muhammad Asaduddin, Hong Gee Roh, Hyun Jeong Kim, Eung Yeop Kim, and Sung-Hong Park, Perfusion Maps Acquired from Dynamic Angiography MRI using Deep Learning Approaches, Journal of Magnetic Resonance Imaging, 2023;57(2):456-469, http://dx.doi.org/10.1002/jmri.28315

**2022**

- Hyun-Seo Ahn, Yujin Jung, and Sung-Hong Park, Measuring glomerular blood transfer rate in kidney using diffusion-weighted arterial spin labeling, Magnetic Resonance in Medicine, 2022;88(6):2408-2418, http://dx.doi.org/10.1002/mrm.29401
- Sunghun Seo#, Huan Minh Luu#, Seung Hong Choi, and Sung-Hong Park, Simultaneously Optimizing Sampling Pattern for Joint Acceleration of Multi-contrast MRI using Model-Based Deep Learning, Medical Physics, 2022;49(9):5964-5980, http://dx.doi.org/10.1002/mp.15790
- Jun-Hee Kim#, Jae-Geun Im#, and Sung-Hong Park, Mesurement of CSF Pulsation from EPI-based Human fMRI, NeuroImage, 2022;257:119293, http://dx.doi.org/10.1016/j.neuroimage.2022.119293
- Gyutaek Oh, Hyukyoung Bae, Hyun-Seo Ahn, Sung-Hong Park, Won-Jin Moon, Jong Chul Ye, Unsupervised Resolution-Agnostic Quantitative Susceptibility Mapping using Adaptive Instance Normalization, Medical Image Analysis, 2022;79:102477, https://doi.org/10.1016/j.media.2022.102477
- Ki Hwan Kim#, Sunghun Seo#, Won-Joon Do, Huan Minh Luu, and Sung-Hong Park, Varying Undersampling Dimension for Accelerating Multiple-Acquisition Magnetic Resonance Imaging, NMR in Biomedicine 2022;35:e4572, http://dx.doi.org/10.1002/nbm.4572
- Gyu Sang Yoo#, Huan Minh Luu#, Heejung Kim#, Won Park, Hongryull Pyo, Youngyih Han, Ju Young Park, and Sung-Hong Park, Feasibility of Synthetic Computed Tomography Images Generated from Magnetic Resonance Imaging Scans using Various Deep Learning Methods in the Planning of Radiation Therapy for Prostate Cancer, Cancers 2022;14(1):40, https://www.mdpi.com/2072-6694/14/1/40

**2021**

- Hyun-Soo Lee, Seon-Ha Hwang, Jaeseok Park, and Sung-Hong Park, Single-shot Pseudo-centric EPI for Magnetization-Prepared Imaging, Magnetic Resonance in Medicine 2021;86(5):2656-2665, http://dx.doi.org/10.1002/mrm.28897
- Huan Minh Luu#, Dong-Hyun Kim#, Jae-Woong Kim, Seung Hong Choi, and Sung-Hong Park, qMTNet: Accelerated Quantitative Magnetization Transfer Imaging with Artificial Neural Networks, Magnetic Resonance in Medicine, 2021;85(1):298-308, https://onlinelibrary.wiley.com/doi/abs/10.1002/mrm.28411

## 수상

첫 화면 Lab News의 수상 글 가운데 2021년 이후 글 7건으로, 모두 구성원 수상이다. 문구는 화면 표기 그대로이고, 날짜는 글에 적힌 연월 또는 연도다. 2021년의 두 글은 연도만 적혀 있어 2021년 10월 전의 일일 수 있다.[^news]

- 2025 · Wooseung Kim, Napasara Asawalertsak, Minjae Kim, and Dongho Shin won first place in the TopBrain Challenge 2025 (brain blood vessel segmentation challenge) both MRA and CTA hosted by MICCAI.
- 2025-02 · Jae-Geun Im received the Outstanding Dissertation Award at the university's graduation ceremony in February 2025.
- 2024-11 · Seon-Ha Hwang received the Grand Prix award for an abstract presentation at the International Congress on Magnetic Resonance Imaging (ICMRI) in November 2024.
- 2024-11 · Seon-Ha Hwang received the Outstanding Paper Award at the university in November 2024.
- 2023 · Jun-Hee Kim received Summa Cum Laude in International Society for Magnetic Resonance in Medicine 2023.
- 2021 · Huan Minh Luu won first place in the brain tumor segmentation challenge (BRATS) 2021 (hosted by RSNA/MICCAI/ASNR) among 2200 teams and 30000 submissions in the world.
- 2021 · Hyun-Seo Ahn and Huan Minh Luu received Summa Cum Laude and Magna Cum Laude, respectively, in International Society for Magnetic Resonance in Medicine 2021.

## 소식

첫 화면 Lab News에서 수상 글을 뺀 2021년 10월 이후 글 1건과, 날짜가 적히지 않은 글 1건이다. 문구는 화면 표기 그대로다.[^news]

- 2026-04-30 · Sung-Hong Park's online talk on Henry Steward Talks has been released as follows. Park, S. (2026, April 30). The lymphatic system in the CNS and the eye: related MR imaging techniques. In The Biomedical & Life Sciences Collection, Henry Stewart Talks. https://doi.org/10.69645/DICF7231
- 날짜 표기 없음 · Muhammad Asaduddin published a paper in Advanced Materials as a co-first author.

## 연락과 위치

- 위치: 정문술빌딩(Chung-Moon-Soul Building, E16) 305호(CONTACT 화면), 교수실 E16 1002호(PEOPLE 화면, 학과 교수 소개)[^contact][^prof][^deptprof]
- 주소: 291, Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea (Department of Bio and Brain Engineering, KAIST)[^contact]
- 전화: 042-350-4352, 팩스 042-350-4310(CONTACT 화면), 교수 전화 042-350-4312(PEOPLE 화면, 학과 교수 소개)[^contact][^prof][^deptprof]
- 교수 이메일: sunghongpark@kaist.ac.kr[^prof][^deptlist][^deptprof]
[^p1]: J.-H. Kim, R.-E. Yoo, S. H. Choi, S.-H. Park, Fluids and Barriers of the CNS 20, 37 (온라인 2023-05-26). <https://doi.org/10.1186/s12987-023-00446-z> 초록 기준.
[^p2]: J.-H. Kim, J.-G. Im, S.-H. Park, NeuroImage 257, 119293 (2022). <https://doi.org/10.1016/j.neuroimage.2022.119293> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: Y. Jung, H.-S. Ahn, S.-H. Park, Magnetic Resonance in Medicine 93, 699-708 (온라인 2024-09-02). <https://doi.org/10.1002/mrm.30288> 초록 기준.
[^p4]: H.-S. Ahn 외, S.-H. Park, NeuroImage 338, 122132 (2026). <https://doi.org/10.1016/j.neuroimage.2026.122132> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: H.-R. Choi, H. M. Luu, S.-H. Park, Magnetic Resonance in Medicine 96, 1313-1322 (온라인 2026-05-08). <https://doi.org/10.1002/mrm.70411> 초록 기준.
[^p6]: M. Asaduddin, E. Y. Kim, S.-H. Park, Magnetic Resonance in Medicine 92, 1205-1218 (온라인 2024-04-16). <https://doi.org/10.1002/mrm.30095> 초록 기준.
[^p7]: H. M. Luu, G. S. Yoo, W. Park, S.-H. Park, Medical Physics 51, 4365-4379 (온라인 2024-02-07). <https://doi.org/10.1002/mp.16976> 초록 기준.
[^p8]: B. Kim, G. Y. Lee, S.-H. Park, Medical Physics 50, 5528-5540 (온라인 2023-03-30). <https://doi.org/10.1002/mp.16380> 초록 기준.
[^research]: 자기공명영상 연구실 누리집 RESEARCH 화면의 글 <https://mri.kaist.ac.kr:3100/quill_data?research> (누리집이 RESEARCH 화면에 불러오는 자료; 연구 관심 세 가지와 다섯 연구 주제, 2026-10-23 열람)
[^facility]: 자기공명영상 연구실 누리집 FACILITY 화면의 글 <https://mri.kaist.ac.kr:3100/quill_data?facility> (장비와 실험 대상, 2026-10-23 열람)
[^prof]: 자기공명영상 연구실 누리집 PEOPLE 화면 교수 칸의 글 <https://mri.kaist.ac.kr:3100/prof_info> (직위, 연락처, 학력, 경력, 2026-10-23 열람)
[^people]: 자기공명영상 연구실 누리집 PEOPLE 화면 구성원 칸의 글 <https://mri.kaist.ac.kr:3100/students>, <https://mri.kaist.ac.kr:3100/student_type> (Graduate Students, Visiting researcher, Past Members, 2026-10-23 열람)
[^pubs]: 자기공명영상 연구실 누리집 PUBLICATIONS 화면 International Publications의 Papers 목록 <https://mri.kaist.ac.kr:3100/quill_data?internationalPapers> (화면 머리의 표시 설명 「Underscore : corresponding author(s), #: equal contributions」; 같은 화면의 나머지 네 목록과 목록 범위는 근거 페이지, 2026-10-23 열람)
[^news]: 자기공명영상 연구실 누리집 첫 화면 Lab News의 글 <https://mri.kaist.ac.kr:3100/quill_data?labNews> (2026-10-23 열람)
[^contact]: 자기공명영상 연구실 누리집 CONTACT 화면의 글 <https://mri.kaist.ac.kr:3100/quill_data?contact> (위치, 주소, 전화·팩스, 2026-10-23 열람)
[^deptlist]: KAIST 바이오및뇌공학과 교수진 목록 <https://bioeng.kaist.ac.kr/index.php?mid=bio_03_01> (박성홍 교수 항목: 직위, 박사 학위, 연구분야, 연구실, 2026-10-23 열람)
[^deptprof]: KAIST 바이오및뇌공학과 교수 소개(박성홍) <https://bioeng.kaist.ac.kr/index.php?document_srl=6771&mid=bio_03_01> (직위, 연구실명, 최종학위, 연구분야, 경력, 학회 활동, 수상경력, 대표 연구실적, 2026-10-23 열람)

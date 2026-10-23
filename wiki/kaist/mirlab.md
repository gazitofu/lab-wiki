# 의료영상 및 의학물리 연구실 (Medical Imaging & Radiotherapy Laboratory, MIRLAB)

**KAIST 원자력및양자공학과 · 조승룡 교수**

- 분야: X선 CT 영상 재구성(희소 샘플링·저선량 CT, 딥러닝 재구성), 물리 요인 보정(산란선 보정, 금속 인공물 저감), 새 X선 영상 시스템(디지털 유방 단층합성, 이중 에너지 영상, 치과 콘빔 CT), 영상 유도 방사선 치료의 물리, 산업용 X선 비파괴 검사
- 대분야: 물리·양자, 컴퓨팅·AI
- 태그: X선 영상·회절[^home][^novel][^p5], 과학·공학 AI[^dl][^p3][^p4], 컴퓨터 비전[^p1][^p2]
- 홈페이지: <https://www.mirlab.kaist.ac.kr/>
- 근거와 출처: [MIRLAB 근거 페이지](mirlab-sources.md)

> 의료 영상 과학, 특히 영상 유도 방사선 치료에 쓰는 영상을 중심으로 연구하는 원자력및양자공학과 연구실이다.[^home] 추가 X선 선량 없이 X선 의료 영상의 질을 높이는 처리와 치료 중의 정확한 영상 유도 기술로, 질병의 조기 발견과 고정밀 치료, 정확한 예후 판단을 돕는 것을 목표로 한다고 소개한다.[^home]

## 무엇을 연구하나

연구실은 KAIST 원자력및양자공학과 조승룡 교수의 연구실이다. 누리집은 연구실을 MIRLAB, Medical Imaging & Radiotherapy Laboratory로 부르고, 원자력및양자공학과 연구실 목록은 국문 이름을 의료영상 및 의학물리 연구실로, 영문 페이지는 Medical Imaging and Radiotherapy Laboratory로 적는다.[^home][^nqe]

누리집 첫 화면은 연구 관심의 중심을 의료 영상 과학, 특히 영상 유도 방사선 치료(IGRT, image-guided radiation therapy, 치료 전·중·후에 표적의 영상을 찍어 방사선을 정확히 쏘도록 돕는 치료 방식)에 둔다고 적는다.[^home] 현대 방사선 치료에서는 치료 표적의 정확한 영상이 종양 제어 확률을 높이고 정상 조직의 합병증 확률을 낮추는 데 특히 중요하며, 콘빔 CT(CBCT, cone-beam computed tomography, 원뿔 모양으로 퍼지는 X선과 평면 검출기를 돌려 3차원 영상을 얻는 CT)의 영상 재구성 기법 발전이 IGRT 응용 연구를 이끌었다고 설명한다. 새로운 방사선 치료 방식을 위한 알고리즘도 연구한다고 적는다.[^home]

첫 화면은 X선 촬영과 3차원 CT 장치가 몸을 절개하지 않고 몸 안의 정보를 풍부하게 담는다고 보고, 추가 X선 선량 없이 전처리·후처리로 X선 의료 영상의 질을 높이면 여러 응용에서 의사의 판단을 도울 수 있다고 적는다. 치료 중의 정확한 영상 유도 기술은 임상 결과를 개선하는 데 도움이 된다고 적는다.[^home] 연구실은 방사선 촬영, CT 영상, 하드론 영상(양성자 등 쿼크로 이루어진 입자인 하드론의 빔으로 찍는 영상), 방사선 치료 물리, 신기술 분야의 과제를 진행한다고 소개한다.[^home] 진행 중인 과제로는 나선형 CT(helical CT, 환자 침대가 움직이는 동안 X선관이 계속 돌아 나선 궤적으로 촬영하는 CT), 이동형 C-arm CT(C자 모양 팔의 양 끝에 X선관과 검출기를 단 장비로 찍는 CT), 단층합성(tomosynthesis, 제한된 각도 범위에서 찍은 여러 장의 X선 투영으로 단면 영상을 만드는 방법) 시스템 같은 X선 의료 영상 장비 개발을 들고, 산업 분야 과제로 전자 소자의 비파괴 검사(물체를 부수거나 자르지 않고 내부의 결함이나 상태를 살피는 검사)를 위한 라미노그래피(laminography, 넓고 얇은 판 모양 물체의 단면 영상을 얻는 X선 단층 촬영 방법)와 고에너지 X선 화물 검색 시스템을 든다.[^home] 치과 크라운·인레이 제작을 위해 치아 본(인상체)을 X선 3차원 영상으로 재구성하는 과제도 예로 든다.[^home]

첫 화면의 Research Areas 구역은 연구 분야 일곱 가지를 든다. 저선량 CT를 위한 희소 샘플링(측정을 듬성듬성 줄여서 하는 자료 수집) 방법, 물리 요인 보정 방법, 새 영상 시스템, 영상 유도 방사선 치료의 물리, 비파괴 검사, CT 계측(CT 영상으로 물체의 치수와 모양을 재는 측정) 기반 제조 응용, 딥러닝 기반 연구다.[^home]

## 주요 연구 주제

### 1. 적은 측정으로 CT 영상을 되살리는 재구성

Sparse-sampling Approach to Low-dose CT 페이지는 저선량 CT의 한 방법으로, X선관 출력을 바꾸지 않고 희소 샘플링을 하는 MVUS(many-view under-sampling) 방법을 제안했다고 적는다.[^sparse] X선관과 환자 사이에 가는 틈이 여럿 난 콜리메이터(collimator, X선이 지나는 범위를 제한하는 차폐 부품)를 두어 환자가 받는 방사선량을 줄이고, 샘플링 밀도를 고르게 하려고 촬영 중 콜리메이터를 왕복시키는 방법을 제안했다고 설명한다.[^sparse] 정해진 선량 제약 아래에서 희소 샘플링 방식을 최적화하려고 압축 센싱(compressive sensing, 신호가 적은 수의 성분으로 표현된다는 성질을 이용해 적은 측정에서 신호를 복원하는 이론)에서 나온 두 지표인 샘플링 밀도와 데이터 상관을 썼다고 적는다. 실험에서 산란 감소와 한 번의 촬영으로 하는 이중 에너지 영상(서로 다른 두 X선 에너지 스펙트럼으로 찍어 물질을 구분하는 영상) 같은 부가 이점도 보였고, 이 기법을 방 안에 설치한 CT와 C-arm CT 같은 임상 CT 시스템에 구현하는 연구를 하고 있다고 적는다.[^sparse]

Deep Learning based MIR Research 페이지는 희소 투영(sparse-view, 적은 수의 촬영 각도에서만 투영을 얻는 촬영) CT 영상에서 측정하지 않은 사이노그램(sinogram, 촬영 각도마다 얻은 투영 자료를 각도 순서로 쌓은 자료)을 심층 신경망으로 합성했고, 딥러닝을 쓴 다른 기법과 딥러닝 기반 방사선 치료 계획 연구에도 관심을 둔다고 적는다.[^dl] 대표 논문 1은 희소 투영 CT에서 생기는 앨리어싱(aliasing, 샘플링이 듬성해 원래 신호에 없는 거짓 무늬가 생기는 현상) 줄무늬 인공물(실제 물체에는 없는데 촬영·재구성 과정 때문에 영상에 나타나는 거짓 구조)을 촬영 각도별 역투영(투영 자료를 촬영 방향을 따라 영상 공간에 되돌려 펼치는 계산) 텐서(숫자를 여러 축으로 늘어놓은 다차원 배열) 영역에서 지우는 신경망 TMAA-net을 제안했다.[^p1] 대표 논문 2는 희소 투영 CT 재구성과 금속 인공물 저감을 한꺼번에 푸는 자기 지도(self-supervised, 정답 영상 없이 자료 자체에서 학습 신호를 만드는) 방법을 내놓았다.[^p2] 누리집 목록에는 이 밖에도 접힌 역투영 텐서 신경망으로 하는 희소 투영 CT 재구성(Fully 3D 2023)과 희소 투영 CBCT 재구성(Computers in Biology and Medicine 2025)을 제목에 단 논문이 있다.[^pubs]

### 2. 산란선·금속 인공물 같은 물리 요인 보정

Methods for Physical Factor Correction 페이지는 산란선(물체 안에서 진행 방향이 바뀐 X선)이 콘빔 CT에서 영상 대비와 해상도를 떨어뜨리는 주된 물리 요인이라고 보고, 산란 합성곱 커널(kernel, 한 점에 들어온 신호가 주변으로 퍼지는 모양을 나타내는 함수) 최적화, 빔 차단기 기반 산란 추정, 몬테카를로 시뮬레이션(난수로 여러 경우를 반복 계산해 결과의 분포나 평균 등을 추정하는 계산 방법)으로 산란 보정 문제에 접근해 왔다고 적는다.[^phys] 원형 궤도 콘빔 CT의 데이터 일관성 조건(같은 물체를 여러 각도에서 찍은 투영 자료가 서로 만족해야 하는 수학적 관계)으로 산란 커널의 모형 변수를 최적화했고, 일부가 가려진 자료에서 영상을 재구성하면서 가려진 자료를 산란 추정과 보정에 쓰는 재배열 BPF(backprojection-filtration, 투영 자료를 먼저 역투영한 뒤 걸러 영상을 만드는 재구성 방식) 알고리즘을 개발했으며, 몬테카를로 기반 산란 추정을 GPU 병렬 계산 구조로 구현했다고 설명한다.[^phys]

같은 페이지는 금속 인공물이 영상을 덮어 버려 의료와 산업 응용 모두에서 해부 정보를 지키려면 억제해야 한다고 적는다. 인공물이 주로 빔 경화(beam hardening, 여러 에너지가 섞인 X선이 물체를 지나며 낮은 에너지 성분이 주로 흡수되어 평균 에너지가 높아지는 현상)에서 오면 빔 경화 보정과 이중 에너지 촬영으로 다룰 수 있지만, 주로 광자 부족(photon starvation, 물체를 지나 검출기에 닿는 X선 광자 수가 측정에 필요한 만큼에 못 미치는 현상)에서 오는 인공물은 두 방법으로 다룰 수 없다고 설명한다.[^phys] 금속에 가려진 사이노그램 부분을 메우는 인페인팅(inpainting, 영상이나 자료의 빈 부분을 주변 정보로 채우는 처리)을 외부 문제 설정(영상의 일부 영역을 빼고 그 바깥 영역만 재구성하는 문제 설정)의 반복 영상 재구성에 기반해 기존 보간 기법보다 정확하게 하는 방법과, 이산 대수 재구성(영상 값이 정해진 몇 가지 값만 갖는다고 두고 방정식을 반복해 푸는 재구성)을 쓴 가속 판을 내놓았다고 적는다.[^phys]

대표 논문 3은 물리에 기반한 빔 경화 보정과 생성 딥러닝 모형을 묶어, 실제 짝 자료 없이 학습하는 CT 금속 인공물 저감 틀을 제안했다.[^p3] 대표 논문 4는 디지털 유방 단층합성 투영 영상의 산란선을 비대칭 산란 커널의 중첩에서 착안한 딥러닝으로 추정하는 방법을 내놓았다.[^p4] 누리집 목록에는 이 밖에도 확산 모형(잡음을 단계적으로 걷어 내며 자료를 만드는 생성 모형)을 쓴 치과 CBCT 금속 인공물 저감(Journal of Applied Clinical Medical Physics 2025), 나비넥타이 필터(bowtie filter, X선관 앞에 두어 부채꼴 빔의 가장자리 쪽 세기를 줄이는, 가운데가 얇고 양옆이 두꺼운 필터)를 단 콘빔 CT의 화질 개선(Medical Physics 2023), 딥러닝 기반 산란 보정의 영역별 비교(SPIE Medical Imaging 2025)를 제목에 단 논문이 있다.[^pubs]

### 3. 유방 단층합성·이중 에너지·치과 영상 같은 새 영상 시스템

Novel Imaging Systems 페이지는 양성자 치료 계획이 X선 CT 자료에 기대고 있지만 X선 CT 자료는 양성자와 물질의 상호작용을 정확히 반영하지 못한다고 보고, 양성자 CT를 그 대안으로 연구했다고 적는다.[^novel] 선량–깊이 분포(몸 안의 깊이에 따라 흡수되는 방사선량의 분포)가 광자 빔과 같은 모양이 되도록 변조한 양성자 빔으로 실험대 규모의 양성자 CT 영상을 찍었고, 국립암센터와 함께 환자별 양성자 비정 보상체(range compensator, 양성자가 몸 안에서 멈추는 깊이를 환자 모양에 맞추려고 빔 경로에 두는 부품)의 품질 보증 도구로 양성자 방사선 촬영의 가능성을 보였으며, 희소 투영 양성자 CT로 연구를 넓혔다고 설명한다.[^novel]

같은 페이지는 디지털 유방 단층합성(DBT, digital breast tomosynthesis, 유방을 여러 각도에서 찍은 X선 투영으로 단면 영상을 만드는 촬영)이 유방 촬영만 할 때보다 민감도(병이 있는 사람을 양성으로 가려내는 비율)와 특이도(병이 없는 사람을 음성으로 가려내는 비율)가 높다는 근거와 함께 임상에서 관심을 모으고 있다고 적는다. KAIST 바이오및뇌공학과 Jong-Chul Ye 교수와 국내 여러 기관과 함께 DBT와 확산 광 단층촬영(DOT, diffuse optical tomography, 조직에 비춘 빛이 흩어져 나오는 것을 재서 내부의 광학 성질 분포를 영상으로 만드는 방법)을 묶은 다중 모달(여러 영상 방식을 함께 쓰는) 영상 시스템을 만들고 있다고 설명한다.[^novel] DOT 영상은 DBT 영상 위에 암과 관련된 혈관계의 산소 농도에 관한 기능 정보를 더한다고 적고, DBT·DOT 화질 개선과 DBT 단면 영상으로 합성 유방 촬영 영상을 만드는 연구도 한다고 적는다.[^novel]

CT Metrology-based Manufacturing Applications 페이지는 3D 프린팅 같은 적층 제조(재료를 층층이 쌓아 물체를 만드는 제조 방식)의 생의학 응용에 관심을 두고, 제품의 치수 정확도를 보장하는 CT 계측을 앞으로 중요해질 분야로 본다.[^metro] CT 기반 3D 프린팅 치아 모형으로 어린이의 이상 앞니를 치료했고, 미국 치과의사와 함께 석고 모형 대신 치아 본을 CT로 찍어 얻은 디지털 모형으로 치과 크라운을 만드는 절차를 제안했다고 적는다.[^metro]

대표 논문 5는 두 에너지 스펙트럼을 번갈아 촬영하고 측정하지 않은 투영을 신경망으로 합성해, 기존 단일 에너지 DBT와 비슷한 촬영 시간과 환자 선량으로 유방 조성 영상을 얻는 이중 에너지 DBT를 제안했다.[^p5] 대표 논문 6은 이중 에너지 CT의 물질 분해(material decomposition, 영상을 몇 가지 기준 물질의 분포로 나누어 나타내는 처리)를 영상 재구성과 한 단계로 하는 알고리즘 GSART를 제안했다.[^p6] 대표 논문 7은 치과 콘빔 CT 투영 자료에서 파노라마 투영 자료를 뽑아 추가 촬영 없이 파노라마 영상을 재구성하는 방법을 제안했다.[^p7] 누리집 목록에는 이 밖에도 단층합성의 촬영 각도 범위 최적화(Physica Medica 2024), 오프셋 검출기(중심을 회전축에서 비켜 단 검출기)를 단 치과 콘빔 CT의 기하 보정(Precision Engineering 2023), 저지능(stopping power, 지나가는 입자가 물질 안에서 단위 길이마다 잃는 에너지) 추정 개선을 위한 3중 에너지 CT 영상(Nuclear Engineering and Technology 2023)를 제목에 단 논문이 있다.[^pubs]

### 4. 방사선 치료와 산업 검사로 넓힌 영상 기술

Physics of Image-guided Radiation Therapy 페이지는 앞의 연구 성과가 IGRT용 콘빔 CT에 쓰일 수 있다고 보고, 임상 환경에서 IGRT와 더 직접 관련된 연구도 해 왔다고 적는다.[^igrt] 소아 환자나 매일 되풀이하는 콘빔 CT 촬영에서 중요한 영상 촬영 선량을 GATE 시뮬레이션 환경에 XCAT 인체 팬텀(phantom, 영상 장비 시험이나 선량 평가에서 사람 몸 대신 쓰는 모형이나 계산 모형)을 넣어 평가·검증했고, 매일 하는 콘빔 CT의 선량을 줄이는 관심 영역 영상 기법과 관전류 변조(촬영 중 X선관에 흐르는 전류를 바꿔 X선 세기를 조절하는 방법) 기법을 제안했다고 설명한다.[^igrt] Asan Medical Center 연구진과 함께 선형가속기(전자를 곧은 관에서 가속해 치료용 고에너지 X선을 만드는 장치) 치료기에 단 콘빔 CT로 움직이는 표적의 표지자 궤적을 재구성했고, 하드론 치료에서 몸 안 하드론의 도달 범위를 확인하고 선량 분포를 추정하려고 University of Chicago의 Kao 교수와 함께 빔 경로 안 비행시간 PET(TOF-PET, 양전자 소멸에서 나온 두 감마선이 검출기에 닿는 시간 차까지 재는 양전자 방출 단층촬영) 스캐너용 새 영상 재구성 기법을 개발하고 있다고 적는다.[^igrt] 대표 논문 8은 양성자 치료의 선량 분포를 빔 경로 안 TOF-PET으로 감시하려고, 치료와 동시에 양전자 분포를 영상화하는 재구성 알고리즘 SPIRA를 제안했다.[^p8]

Nondestructive Testing 페이지는 결함 검출에 쓰는 비파괴 검사가 의료 영상의 병변 검출과 닮았다고 보고, 의료 영상 기술의 병변 검출을 산업 응용으로 옮기는 알고리즘을 개발한다고 적는다.[^ndt] 압축 센싱 관점에서 컴퓨티드 라미노그래피의 비원형 촬영 궤적을 제안했고, 화물 검색을 위해 이중 에너지 X선 방식을 물질 분해에 적용한 실험에서 상용화 가능성을 보였다고 설명한다.[^ndt] 누리집 목록에는 이 밖에도 이중 방사선 비파괴 화물 검색 시스템의 영상 업샘플링(Nuclear Instruments and Methods in Physics Research Section A 2024), 복잡한 선원–검출기 배치에서 3차원 스캔으로 방사능을 추정하는 방법(Applied Radiation and Isotopes 2026), 리튬이온 배터리 단층합성 영상 개선(IEEE Nuclear Science Symposium·Medical Imaging Conference 2023)을 제목에 단 논문이 있다.[^pubs]

## 대표 논문

조승룡 교수가 저자인 2021–2026년 학술지 논문 가운데 네 연구 주제(적은 측정으로 하는 CT 재구성, 물리 요인 보정, 새 영상 시스템, 방사선 치료·산업 검사 응용)에서 초록을 확인할 수 있는 여덟 편을 골랐다. 여덟 편 모두 교수가 마지막 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2024 | [TMAA-net: tensor-domain multi-planal anti-aliasing network for sparse-view CT image reconstruction](https://doi.org/10.1088/1361-6560/ad8da2) · Physics in Medicine & Biology 69 | 희소 투영 CT 영상 재구성에 쓰는 심층 신경망 연구는 주로 사이노그램을 늘려 빠진 각도의 정보를 합성해 왔지만, 이런 사이노그램 기반 신경망은 앨리어싱 줄무늬 인공물을 지우고 대비가 낮은 작은 구조를 되살리는 데 한계가 있다. 이 논문은 촬영 각도별 역투영(VVBP, view-by-view back-projection) 텐서 영역의 신경망으로 이 한계를 넘는다. 2차원 사이노그램 대신 3차원 텐서 영역에서 앨리어싱 인공물을 직접 다루며, 다면 앨리어싱 제거 모듈로 관상면(coronal, 몸을 앞뒤로 나누는 단면)·시상면(sagittal, 몸을 좌우로 나누는 단면) 방향 텐서 평면 안의 인공물을 지우고, 데이터 충실도(재구성 영상이 실제 측정 자료와 맞는 정도) 기반 보정 모듈로 텐서 신경망의 출력 영상을 이어 처리해 선명도와 질감을 되살린다. 최신 사이노그램 기반 신경망들과 비교해 앨리어싱 인공물 제거와 저대비 세부 복원에서 나은 성능을 보였고, 원형 팬빔 CT(부채꼴로 퍼지는 X선으로 촬영하는 CT) 구성의 수치 투영 자료와 임상 투영 자료로 검증했다. 텐서 공간 처리가 앨리어싱 인공물 제거에서 기존 사이노그램 영역 처리보다 높은 일반화 성능을 낸다는 것도 보였다.[^p1] | 1저자 Sungho Yun, 마지막 저자 조승룡 (5명) |
| 2 | 2026 | [Diffusion prior-guided implicit neural representation for metal artifact reduction in sparse-view CT reconstruction](https://doi.org/10.1088/1361-6560/ae6a5a) · Physics in Medicine & Biology 71 | 희소 투영 CT(SVCT)는 방사선 노출을 줄이지만 심한 줄무늬 인공물이 생기고, 금속 이식물이 있으면 더 두드러진다. 기존 방법 대부분은 SVCT와 금속 인공물 저감(MAR)을 따로 다뤄 둘을 함께 푸는 문제(SVMAR)에는 최적이 아니고, 둘을 함께 다루는 몇몇 방법도 대부분 지도 학습(정답이 붙은 자료로 배우는 기계학습)이라 임상에서 구하기 어려운 대규모 짝 자료가 필요하다. 이 논문은 잡음 제거 확산 확률 모형(DDPM, 자료에 잡음을 더해 가는 과정을 거꾸로 되짚도록 학습해 잡음에서 자료를 만드는 생성 모형)과 암시적 신경 표현(INR, 좌표를 넣으면 그 위치의 값을 내도록 신경망에 영상을 함수로 담는 방식)을 쓰는 자기 지도 틀을 제안한다. 먼저 금속 흔적 바깥의 광선만 골라 희소 측정으로 INR을 최적화해 첫 재구성을 얻고, 이를 역확산 과정(확산 모형이 잡음에서 출발해 잡음을 단계적으로 걷어 내는 과정)을 빠르게 하는 데 쓴다. 역확산 동안 확산 사전 정보(확산 모형이 학습한 영상의 통계적 특성)로 측정값의 금속 흔적 영역을 푸아송 블렌딩(이어 붙인 영역의 밝기 변화가 주변과 자연스럽게 이어지도록 맞추는 영상 합성 방법)으로 메우는 MAR 단계와, 확산 사전 정보와 MAR로 고친 사이노그램으로 INR을 다듬어 데이터 충실도를 지키는 SVCT 단계를 번갈아 한다. 모의 자료와 임상 자료 실험에서 대규모 짝 자료 없이 질 높은 영상을 재구성했고, 학습 분포 밖(OOD) 자료의 160·80·40개 투영 설정에서 IndudoNet+를 포함한 기존 방법들보다 최대 신호 대 잡음비(PSNR, 복원 영상과 원본의 오차를 신호 크기에 견주어 나타낸 화질 지표)와 구조 유사도(SSIM, 두 영상의 밝기·대비·구조가 닮은 정도를 나타내는 지표)가 높았다.[^p2] | 1저자 Subong Hyun, 마지막 저자 조승룡 (5명) |
| 3 | 2026 | [A strategy for simulation-driven CT metal artifact reduction toward improving network generalizability](https://doi.org/10.1002/mp.70336) · Medical Physics 53 | 딥러닝 기반 CT 금속 인공물 저감(MAR) 방법은 대체로 인공물이 생기는 물리를 명시적으로 모형화하지 않고 자료 기반 대응에 크게 기대어, 짝 자료나 과제별 자료가 필요해 확장성이 떨어지고 환각(실제로 없는 구조를 만들어 내는 오류), 해부 구조 왜곡, 불안정한 인공물 억제를 겪기 쉽다. 이 논문은 가벼운 다층 퍼셉트론(MLP, 계산 단위를 여러 층으로 이은 기본 신경망) 기반 빔 경화 보정과 조건부 잠재 확산 모형(LDM, 입력 영상을 조건으로 받아 압축된 잠재 공간에서 잡음을 걷어 내며 영상을 만드는 생성 모형)을 묶은 자기 지도 MAR 틀을 제안한다. MLP는 물리에 기반한 다항식 보정을 하면서 사이노그램 일관성을 최적화 목표에 담아 사례마다 맞춰지고, 학습한 MLP 변수를 다시 써 인공물 없는 영상에서 인공물이 낀 영상을 모의해 실제 짝 자료 없이 자기 지도 학습용 유사 짝 자료를 만든다. 이렇게 만든 합성 짝 자료로 조건부 LDM을 학습해 남은 인공물을 지운다. LDM은 저차원 잠재 공간(자료를 압축해 나타낸 내부 표현 공간)에서 작동해 추론 시간을 크게 줄이면서 질 높은 재구성을 유지했고, SynDeepLesion 자료와 실제 임상 자료에서 기존 최신 MAR 기법들과 비교해 인공물 제거와 구조 보존이 뛰어났다.[^p3] | 1저자 Sungho Yun, 마지막 저자 조승룡 (4명) |
| 4 | 2025 | [Asymmetric scatter kernel estimation neural network for digital breast tomosynthesis](https://doi.org/10.1117/1.jmi.12.s2.s22008) · Journal of Medical Imaging 12 | 디지털 유방 단층합성(DBT)의 산란선 추정에는 여러 딥러닝 방법이 개발됐지만, 대체로 입력에서 출력까지 한 번에 학습하는 방식이라 산란이 생기는 물리를 놓친다. 이 논문은 비대칭 산란 커널의 중첩에서 착안한 딥러닝으로 DBT의 산란을 추정한다. 신경망이 산란 진폭 분포와 함께 산란 커널 폭과 비대칭 인자 지도를 내고, DBT 투영 자료에서 국소적인 유방 두께와 모양의 변화를 반영하려고 유클리드 거리 지도(각 화소에서 기준 경계까지의 직선거리를 값으로 담은 지도)와 투영 각도 정보를 비대칭 인자 추정 신경망 설계에 넣었다. 수치 팬텀 자료와 실제 실험 자료의 체계적인 실험에서, 산란을 보정한 영상의 신호 대 잡음비와 구조 유사도 지수로 볼 때 UNet(영상을 줄였다가 다시 키우는 대칭 구조의 신경망) 기반의 한 번에 학습하는 산란 추정과 대칭 커널 기반 방법보다 나은 성능을 보였다.[^p4] | 1저자 Subong Hyun, 마지막 저자 조승룡 (5명) |
| 5 | 2022 | [A feasibility study on deep‐neural‐network‐based dose‐neutral dual‐energy digital breast tomosynthesis](https://doi.org/10.1002/mp.16071) · Medical Physics 50 | X선 유방 영상의 진단 성능은 유방 밀도에 좌우되며, DBT가 치밀 유방(젖샘과 섬유 조직의 비율이 높은 유방)에서 기존 유방 촬영보다 낫다고 보고되지만 종괴(덩어리 모양의 병변) 검출과 악성 판별은 여전히 어려운 것으로 여겨지는 경우가 많다. 이 논문은 치밀 유방의 진단을 개선할 방안으로, 기존 단일 에너지 DBT와 비슷한 촬영 시간과 환자 선량으로 유방 조성 영상을 얻는 이중 에너지 DBT를 제안한다. 두 에너지 스펙트럼을 번갈아 투영 자료를 얻고, 측정한 투영과 다른 에너지에서 얻은 이웃 투영을 이용하는 심층 신경망으로 측정하지 않은 투영을 합성한다. 물질 분해를 위해 측정·합성 투영과 물체 두께 정보로 X선이 물·지질·단백질을 지나는 부분 경로 길이를 추정하고, 투영 영역에서 물질 분해를 한 뒤 물질 선택 DBT 영상을 재구성한다. 신경망은 수치 유방 팬텀으로 학습했고, 시제품 이중 에너지 DBT 시스템으로 돼지고기 팬텀을 촬영해 가능성을 보였다. 합성 자료로 재구성한 물질 선택 영상은 모두 측정한 자료의 영상과 비교할 만한 암 종괴의 조성 대비를 보였다.[^p5] | 1저자 Hyeongseok Kim, 마지막 저자 조승룡 (9명) |
| 6 | 2022 | [A generalized simultaneous algebraic reconstruction technique (GSART) for dual-energy X-ray computed tomography](https://doi.org/10.3233/xst-211054) · Journal of X-Ray Science and Technology 30 | 이중 에너지 CT(DECT)는 단일 에너지 CT보다 물체의 물리적 성질을 정확히 추정하는 영상 방식이다. 원스텝(one-step) 방법이라 불리는 반복 재구성 방법이 기존 방법들의 얽힌 한계를 풀 수 있어 최근 주목받지만, 계산 비용이 크고 물질 분해 성능이 스펙트럼 계수 추정의 정확도에 크게 좌우된다. 이 논문은 비선형 순방향 모형(물체에서 측정값이 나오는 과정을 계산으로 나타낸 모형)과 가중 제곱 오차를 쓰는 새 손실 함수(학습·최적화에서 줄이려는 오차를 수식으로 나타낸 함수)로, 기준 물질 지도로 효과적으로 분해하면서 스펙트럼 계수의 정확도에 덜 민감한 원스텝 재구성 알고리즘 GSART를 제안한다. 모의 실험과 실제 실험에서 빔 경화 인공물을 줄여 물질 분해의 정확도를 높였고, 영상 영역 물질 분해와 기존 원스텝 알고리즘보다 나은 결과를 보였다.[^p6] | 1저자 Donghyeon Lee, 마지막 저자 조승룡 (6명) |
| 7 | 2023 | [Panoramic dental tomosynthesis imaging by use of CBCT projection data](https://doi.org/10.1038/s41598-023-35805-1) · Scientific Reports 13 | 치과 콘빔 CT와 파노라마 영상은 치과 진단과 치료 계획에 쓰는 중요한 영상이다. 이 논문은 추가 파노라마 촬영 없이 파노라마 영상을 얻으려고, 치과 콘빔 CT 투영 자료에서 파노라마 투영 자료를 뽑아 파노라마 영상을 재구성하는 방법을 제안한다. 환자의 콘빔 CT 영상에서 치열궁(치아가 늘어선 활 모양의 줄)을 정한 뒤, 이에 맞는 파노라마 촬영 궤적을 따라 콘빔 CT 투영 자료에서 파노라마 투영 자료를 뽑는다. 사람 임상 자료 40건과 머리 팬텀 자료 1건으로 시험했고, 임상 자료에는 금속 인공물이 심하거나 치아가 없는 경우처럼 콘빔 CT 영상에서 파노라마 영상을 만들기 어려운 사례가 들어 있다. 여러 환자의 콘빔 CT 투영 자료에서 파노라마 영상을 얻었고, 콘빔 CT 화질과 금속 인공물의 영향을 덜 받는 파노라마 영상을 얻을 수 있었다.[^p7] | 1저자 Taejin Kwon, 마지막 저자 조승룡 (6명) |
| 8 | 2022 | [Feasibility study of a concurrent image reconstruction algorithm for proton therapy with in-beam TOF-PET](https://doi.org/10.1007/s40042-022-00571-2) · Journal of the Korean Physical Society 81 | 방사선 치료 중 치료의 정확도를 감시하는 실시간 선량 유도가 매우 바람직하다. 이 논문은 입자 치료에서 리스트 모드(검출 사건을 하나씩 시각·위치와 함께 기록하는 방식) TOF-PET 자료로 양전자 분포를 치료와 동시에 영상화할 수 있는 순차 처리 영상 재구성 알고리즘 SPIRA를 내놓는다. SPIRA는 최대 우도(관측 자료가 나올 확률을 가장 크게 하는 값을 고르는 추정) 기준을 쓰고 연속 좌표 사건 공간에서 영상을 재구성하며, 동시 영상화를 위해 직렬 처리기를 함께 쓴다. 양성자 치료의 선량 분포를 빔 경로 안 TOF-PET으로 감시하는 쓰임을 가정해, 전체 고리 시스템과 두 검출 헤드의 부분 고리 시스템의 컴퓨터 모의 자료에 적용했다. 동시 계수 분해 시간(두 감마선이 검출된 시각의 차를 구분하는 정밀도) 300 ps와 600 ps, 부분 고리 구성의 열림 각도 45°와 90°를 고려했다. SPIRA 영상은 TOF 측정으로 계산한 위치에 사건을 그대로 놓는 기존 재구성 방법과 비교해 해상도와 대비 회복이 나아 보였다.[^p8] | 1저자 Kihong Son, 마지막 저자 조승룡 (4명) |

## 교수와 전문 분야

조승룡 교수(Seungryong Cho)는 KAIST 원자력및양자공학과 교수다. 누리집 Professor 페이지는 직위를 Professor로, 소속을 Dept. of Nuclear & Quantum Engineering, KAIST로 적고, 학과 교수 페이지도 교수로 싣는다.[^prof][^nqeprof]

Professor 페이지에 따르면 교수는 1995년 2월 서울대학교 물리학과에서 학사, 1997년 2월 같은 학과에서 석사 학위를 받았고, 2002년 8월–2004년 6월 State University of New York(Buffalo) 물리학과에서 대학원 과정을 밟은 뒤 2009년 8월 The University of Chicago의 Committee on Medical Physics에서 의학물리 박사 학위를 받았다.[^prof] 경력은 1995년 3월–1997년 1월 서울대학교 물리학과 연구조교(Research Assistant), 1997년 2월–2000년 7월 Samsung Advanced Institute of Technology Photonics Lab 연구원(Research Engineer), 2000년 8월–2002년 5월 Samsung Electronics Co. Optoelectronics Business의 R & D Engineer, 2003년 6–9월 SUNY at Buffalo 물리학과 연구조교, 2004년 9월–2005년 8월 The University of Chicago Committee on Medical Physics의 Research Rotation, 2005년 9월–2009년 8월 같은 곳의 연구조교, 2009년 9–12월 The University of Chicago Department of Radiology의 Post-doc Scholar다.[^prof]

학술 활동으로는 Medical Physics의 Associate Editor(2023–), Physics in Medicine and Biology의 Editorial Board Member(2019–), SPIE Physics of Medical Imaging의 Program Committee Member(2021–), AFOMP의 Award and Honors Committee Member(2023–)를 맡고 있고, 2016–2019년 AAPM Seed Grant Committee Member를 지냈다.[^prof] 수상 목록에는 Distinguished Reviewer Award, IEEE Tran. Med. Imag.(2021, 2022), Innovative Technology Award, School of Engineering, KAIST(2018), Top 100 R&D Achievements, Ministry of Science and ICT(2018), Journal of Endodontics 2015 Best Paper Award(2016), Samsung Humantech Research Paper Competition(Silver Award, 2016), Best Paper Award, Korean Society of Medical Physics(2015), Best Paper Award, Korean Society of Radiation Industry(2014), PMB Top 25 Reviewers Award, IOP Publishing(2014), Best Lecturer Award, KAIST(2013), Excellent Lecturer Award, KAIST(2011)가 있고, 박사과정 시기의 Paul C. Hodges Research Award(2008) 등도 있다.[^prof]

학위와 경력, Research 페이지들과 2021–2026년 논문 목록을 함께 보면, 교수의 전문 분야는 의학물리, 특히 X선 CT와 단층합성의 영상 재구성, 산란선·금속 인공물 같은 물리 요인 보정, 영상 유도 방사선 치료와 입자 치료의 영상 물리다.[^prof][^home][^pubs]

## 응용 분야

누리집 첫 화면은 질병의 조기 발견, 고정밀 치료, 정확한 예후 판단을 의료 영상 기술로 다룰 과제로 들고, 나선형 CT, 이동형 C-arm CT, 단층합성 시스템 같은 X선 의료 영상 장비 개발 과제와 전자 소자 비파괴 검사용 라미노그래피, 고에너지 X선 화물 검색 시스템 같은 산업 과제를 든다.[^home] CT Metrology-based Manufacturing Applications 페이지는 3D 프린팅 두개골을 쓰는 surgical makeup, 치아 상실 회복, 치아 본 관련 시술 같은 적층 제조의 생의학 응용과 CT 기반 디지털 치과 기술을 든다.[^metro] 대표 논문 5는 이중 에너지 DBT가 특히 치밀 유방에서 종괴의 악성 검출 정확도를 높이는 데 크게 기여할 것으로 기대하고, 대표 논문 8은 SPIRA가 실시간 선량 유도 입자 치료에서 몸 안 치료 검증에 쓰일 수 있다고 적는다.[^p5][^p8]

## 구성원

누리집 Members 페이지 Students 구역의 박사과정(Ph. D Candidate) 9명과 석사과정(Master Candidate) 2명, 모두 11명이다. 연구 주제는 카드에 적힌 연구 분야다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Miran Park | 박사과정 | Image correction (Scatter, Beam Hardening, etc.) |  |
| Jongha Lee | 박사과정 | CT Reconstruction, Tomosynthesis, Deep Learning |  |
| Sunhee Wi | 박사과정 | CT Reconstruction |  |
| Sunho Lim | 박사과정 | Deep Learning | 6 |
| Hyoyi Kim | 박사과정 | Compressed Sensing, Windmill Artifact, Helical CT | 6 |
| Yeonkyoung Choi | 박사과정 | CT Reconstruction |  |
| Chanyoung Oh | 박사과정 | Deep learning, Image segmentation |  |
| Raymond HyunWoo Moon | 박사과정 | Deep learning, Medical Device Development |  |
| Jihye Lee | 박사과정 | Tomosynthesis |  |
| Dohyun Lim | 석사과정 | Medical diagnostic algorithms design |  |
| Gayoung Kim | 석사과정 | Deep learning |  |

## 졸업생

누리집 Alumni 페이지의 박사(Ph. D Degree) 22줄, 석사(Master Degree) 10줄, 학부(Undergraduate) 2줄, 모두 34줄이다. 진로는 카드에 적힌 현재 소속이나 직위이고, 진로 칸이 「-」이거나 「Current Position」으로만 적힌 카드는 진로를 비워 두었다. 졸업 연도는 적혀 있지 않다. 박사 구역에는 Sajid Abbas 이름의 카드가 두 장 있고 두 카드의 진로가 다르며, 두 줄 모두 누리집 표기대로 실었다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Sajid Abbas | Ph.D. |  |
| Jiseoc Lee | Ph.D. | SK Hynix |
| Rizza Pua | Ph.D. | De La Salle University Manila |
| Jonghwan Min | Ph.D. | Samsung Electronics |
| Taewon Lee | Ph.D. | Assistant professor, Hoseo University |
| Kihong Son | Ph.D. | ETRI |
| Sajid Abbas | Ph.D. | KINS |
| Sabir Sohail | Ph.D. |  |
| Changhwan Kim | Ph.D. | Clinical assistant Professor, Yonsei Cancer Hospital |
| Hoyeon Lee | Ph.D. | Assistant Professor, University of Hong Kong |
| Sanghoon Cho | Ph.D. | Samsung Display |
| Donghyeon Lee | Ph.D. | Postdoc. fellow, University of Pennsylvania |
| Taejin Kwon | Ph.D. | Samsung Electronics |
| Yejin Kim | Ph.D. | Medical Physics Resident, Harvard MGH |
| Jaehong Hwang | Ph.D. | Korea Research Institute of Standards and Science |
| Jeongtae Soh | Ph.D. | LG Electronics |
| Seoyoung Lee | Ph.D. | Postdoc, Mayo |
| Hwanhui Jo | Ph.D. | Postdoc, KAIST |
| Sungho Yun | Ph.D. | Postdoc, KAIST |
| Da-in Choi | Ph.D. |  |
| Joonil Hwang | Ph.D. | Postdoc, Yonsei Cancer Hospital |
| Subong Hyun | Ph.D. | Postdoc, KAIST |
| Boyeol Yoo | M.S. | Patent Attorney |
| Yun Jeong Lee | M.S. | KOFONS |
| Jieun Chang | M.S. | Kyungpook Nat'l University School of Medicine |
| Hyeongseok Kim | M.S. | PhD Student, Harvard-MIT Health Sci & Tech |
| Kalyan LY | M.S. |  |
| Uijin Jeong | M.S. | Samsung Eletronics |
| Kangsan Kim | M.S. | LG Electronics |
| Donghyun Kim | M.S. | SNUAILAB |
| Gibok Kim | M.S. | SK Hynix |
| Cecilia Nova Wijaya | M.S. | PhD Student, Politecnico di Milano |
| Dongkyu kwak | Undergraduate |  |
| Jeryl Lewis | Undergraduate |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications 메뉴의 세 페이지(Peer-reviewed Journal Papers, Peer-reviewed Original Articles, Conference Proceedings and Abstracts)에서 2021–2026년 항목을 모은 95편이다. 학술지 논문 26편, 심사 원저 논문 8편, 학술대회 발표·초록 61편이고, 연도별로는 2026년 7편, 2025년 14편, 2024년 21편, 2023년 25편, 2022년 10편, 2021년 16편, 연도 표기 없음 2편이다.[^pubs] 각 항목 끝의 「학술지 논문」, 「심사 원저 논문」, 「학술대회 발표·초록」은 그 항목이 실린 누리집 페이지의 구분이다. 연도는 학술지·학회 표기의 연도이고, 연도가 적히지 않은 학술지 논문 9편은 학술지의 출판 연도에 두었다. 학술대회 발표 2편은 연도가 적혀 있지 않아 「연도 표기 없음」에 두었다. 저자·제목·학술지와 학회 표기는 누리집 그대로다. 목록 구성 기준과 싣지 않은 항목은 근거 페이지에 적었다.

**2026**

- J. Lee, S Cho, J. Kim, H. Kim, Y. Kim. "A 3D scan–driven method for activity estimation under complex source–detector geometries". *Applied Radiation and Isotopes v.234 · 학술지 논문*.
- J. Hwang, H. Moon, J. Yoon, K. Cheong, J. Jung, S Cho, I. Yeo, H. Lee. "Four-dimensional on-beam computed tomography reconstruction using projection-difference images". *Physics in Medicine & Biology 71 (13), 135034 · 학술지 논문*.
- J. Hwang, S. Park, S Cho, J. Kim. "Knowledge-distilled diffusion models for improving cone-beam CT image quality with meta-learning under imbalanced data". *Medical Physics v.53 (8), e70530 · 학술지 논문*.
- H. Kim, S. Lee, S Cho. "Source-free domain adaptation for multi-institutional chest X-ray images". *Journal of Applied Clinical Medical Physics, v.27 (5), e70626 · 학술지 논문*.
- S Hyun, S Yun, S Lee, D Choi, S Cho. "Diffusion prior-guided implicit neural representation for metal artifact reduction in sparse-view CT reconstruction". *Physics in Medicine & Biology 71 (10), 105007 · 학술지 논문*.
- S Yun, S Hyun, D Choi, S Cho. "A strategy for simulation-driven CT metal artifact reduction toward improving network generalizability". *Medical Physics 2026 v.53 (2), e70336 · 학술지 논문*.
- C. Oh, J. Hwang, J. Hwang, S. Cho. "Robust Automatic Geometric Calibration of Dental CBCT using Kalman Filter-Based Marker Tracking". *IFMIA, 2026 · 학술대회 발표·초록*.

**2025**

- D Choi, S Yun, S Hyun, S Cho. "Metal artifact reduction algorithm with conditional latent diffusion model for dental cone-beam CT". *Journal of Applied Clinical Medical Physics 2025; 25:e70317 · 학술지 논문*.
- S Lee, S Hyun, D Kim, HH Kim, HJ Kim, I Choi, CW Shin, S Cho. "Can scout scan help choose a scanning angle in digital breast tomosynthesis?". *Journal of Medical Imaging 12 (S2), S22016-S22016 · 학술지 논문*.
- S Hyun, S Lee, I Choi, CW Shin, S Cho. "Asymmetric scatter kernel estimation neural network for digital breast tomosynthesis". *Journal of Medical Imaging 12 (S2), S22008-S22008 · 학술지 논문*.
- H Shin, T Kim, J Lee, SY Chun, S Cho, D Shin. "Sparse-view CBCT reconstruction using meta-learned neural attenuation field and hash-encoding regularization". *Computers in Biology and Medicine 189, 109900 · 학술지 논문*.
- S. Hyun, S. Yun, S. Lee, D. Choi, S. Cho. "Implicit Neural Representation with Diffusion Priors for Joint Sparse-View CT reconstruction and Metal Artifact Reduction". *Fully 3D, 2025 · 심사 원저 논문*.
- D. Choi, S. Yun, S. Hyun, S. Cho. "Improving the Normalized Metal Artifact Reduction with Prior Image Synthesized via Latent Diffusion Model". *18th International Meeting on Fully Three-Dimensional Image Reconstruction in Radiology and Nuclear Medicine, 2025 · 심사 원저 논문*.
- S. Hyun, S. Lee, J. Hwang, S. Cho. "Backprojection filteration-based high density object artifact suppression method in digital breast tomosynthesis". *KSRI, 2025 · 학술대회 발표·초록*.
- S. Hyun, S. Cho. "High-attenuation object artifact reduction in digital breast tomosynthesis with backprojection filteration image-guided segmentation". *KSMP, 2025 · 학술대회 발표·초록*.
- D. Choi, S. Yun, S. Hyun, S. Cho. "Revisiting NMAR: Diffusion-Based Prior Synthesis and Deep Artifact Correction in CT". *KSIIM, 2025 · 학술대회 발표·초록*.
- S. Hyun, D. Choi, S. Yun, S. Lee, S. Cho. "Diffusion prior guided neural attenuation field for CT metal artifact reduction in sparse-view scenario". *KSMP, 2025 · 학술대회 발표·초록*.
- D. Choi, S. Yun, S. Hyun, S. Cho. "Metal artifact reduction in dental CBCT via latent diffusion model". *IFMIA, 2025 · 학술대회 발표·초록*.
- S. Hyun, D. Choi, S. Yun, S. Lee, S. Cho. "Plug-and-Play Diffusion Priors for Self-supervised Dual-Domain CT Metal Artifact Reduction". *IFMIA, 2025 · 학술대회 발표·초록*.
- S. Hyun, D. Choi, S. Yun, S. Lee, H. Moon, S. Cho. "A diffusion model-based dual-domain approach for CT metal artifact reduction". *SPIE Medical Imaging, 2025 · 학술대회 발표·초록*.
- S. Lee, S. Hyun, S. Cho. "Evaluation of deep learning-based scatter correction in x-ray breast imaging: across image domains and downsampling ratios". *SPIE Medical Imaging, 2025 · 학술대회 발표·초록*.

**2024**

- S Yun, S Lee, D Choi, T Lee, S Cho. "TMAA-net: tensor-domain multi-planal anti-aliasing network for sparse-view CT image reconstruction". *Physics in Medicine & Biology 69 (22), 225012 · 학술지 논문*.
- H. Kim, H. Kim, H. Eom, W. Choi, E. Chae, H. Shin, J. Cha, Y. Choi, Y. Choi, K. Kim, J. Min, W. Shim, S. Lee, S. Cho. "Optimizing angular range in digital breast tomosynthesis: A phantom study investigating lesion detection across varied breast density and thickness". *Physica Medica, 2024 · 학술지 논문*.
- H. Jo, D. Lee, S. Cho. "Image up-sampling method for dual-radiation nondestructive cargo inspection system". *Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment, 2024 · 학술지 논문*.
- Y. Yoo, J. Hwang, S. Park, J. Hwang, S. Cho, S. Kim. "A novel analysis of the formation and resorption changes in dental hard tissue using longitudinal in vivo micro computed tomography". *DENTAL MATERIALS JOURNAL, 2024 · 학술지 논문*.
- J. Hwang, S. Park, N. Park, J. Kim, S. Cho. "CT Slice Generation From Limited Data using Diffusion Model". *MICCAI, 2024 · 학술대회 발표·초록*.
- J. Hwang, S. Park, J. Kim, S. Cho. "Boosting Medical Image Quality with Knowledge Distillation in Diffusion Models for Imbalanced Datasets". *JKMP, 2024 · 학술대회 발표·초록*.
- D. Choi, S. Yun, S. Cho. "Metal artifact reduction with prior image synthesis via latent diffusion model". *JKMP, 2024 · 학술대회 발표·초록*.
- S. Hyun, D. Choi, S. Yun, S. Lee, S. Cho. "Unsupervised CT MAR using Poisson blending method with diffusion prior in sinogram domain". *JKMP, 2024 · 학술대회 발표·초록*.
- S. Lee, S. Cho. "Comparative Analysis of Deep Learning-Based Scatter Correction Across Various Domains and Downsampling Ratios". *KSRI, 2024 · 학술대회 발표·초록*.
- D. Choi, S. Yun, S. Cho. "Latent Diffusion Network를 사용한 금속 아티팩트 저감 알고리즘". *KSRI, 2024 · 학술대회 발표·초록*.
- Wijaya, C. N. , S. Cho. "Investigation of the Effect of Gold Nanoparticles in a Proton Therapy Setting: A Water Phantom Simulation Study". *KSRI, 2024 · 학술대회 발표·초록*.
- D. Choi, S. Yun, S. Cho. "Predicting Metal Artifact from Backprojection Image with Convolutional Neural Network". *AAPM, 2024 · 학술대회 발표·초록*.
- J. Hwang, S. Park, S. Cho, J. Kim. "Diffusion Model-Based Generation of CT Slices with Limited Data". *AAPM, 2024 · 학술대회 발표·초록*.
- D. Kim, S. Lee, S. Hyun, S. Cho. "Slab Image Synthesis in Digital Breast Tomosynthesis". *AAPM, 2024 · 학술대회 발표·초록*.
- S. Hyun, S. Lee, U. Jeong, S. Cho. "Asymmetric scatter kernel superposition-inspired deep learning approach to estimate scatter in breast tomosynthesis". *IWBI, 2024 · 학술대회 발표·초록*.
- D. Choi, S. Yun, S. Cho. "Ramp Filter Effect Estimation with UNET". *KSMP, 2024 · 학술대회 발표·초록*.
- S. Hyun, S. Cho. "Unsupervised Learning for Sparse-view CT Reconstruction Using Diffusion Prior with Residual Guidance". *KSMP, 2024 · 학술대회 발표·초록*.
- J. Hwang, S. Park, S. Cho, J. Kim. "Enhancing the Image Quality of Cone-Beam CT Through The Integration of Knowledge Distillation in a Diffusion Model Under Conditions of Imbalanced Data". *KSMP, 2024 · 학술대회 발표·초록*.
- S. Yun, D. Choi, G.Cho, S. Ye, S. Cho. "Investigation on substantial asymmetry of HU value in dental cone-beam CT with offset detector". *SPIE medical imaging, 2024 · 학술대회 발표·초록*.
- G. Kim, S. Yun, T. Lee, S. Cho. "Unsupervised Medical Image Generation for Dental Imaging: Super-Resolution of Synthetic Panoramic X-ray Images with CycleGAN". *SPIE medical imaging, 2024 · 학술대회 발표·초록*.
- S. Lee, H. Kim, H. Kim, S. Cho. "Predict Risk of Stereotactic Body Radiotherapy Induced Vertebral Compression Fracture Using Multi-Modal Deep Learning Network". *SPIE medical imaging, 2024 · 학술대회 발표·초록*.

**2023**

- S. Yun, U. Jeong, D. Lee, H. Kim, S. Cho. "Image quality improvement in bowtie-filter-equipped cone-beam CT using a dual-domain neural network". *MEDICAL PHYSICS, 2023 · 학술지 논문*.
- H. Kim, S. Lee, W. Shim, M. Choi, S. Cho. "Homogenization of multi-institutional chest x-ray images in various data transformation schemes". *Journal of Medical Imaging, v.10, pg. 061103, 2023 · 학술지 논문*.
- T. Kwon, D. Choi, J. Hwang, T. Lee, I. Lee, S. Cho. "Panoramic dental tomosynthesis imaging by use of CBCT projection data". *Scientific Reports, v.13, pg. 8817, 2023 · 학술지 논문*.
- J. Hwang, H. Kim, T. Lee, D. Choi, T. Kwon, S. Cho. "Geometry calibration for a dental cone-beam CT system with an offset detector". *Precision Engineering, v.79, pg. 264-276, 2023 · 학술지 논문*.
- Y. Kim, J. Kim, S. Cho. "Feasibility study of using triple-energy CT images for improving stopping power estimation". *Nuclear Engineering and Technology, 2023 · 학술지 논문*.
- H. Kim, H. Lee, S. Lee, Y. Choi, Y. Choi, K. Kim, W. Seo, C. Shin, S. Cho. "A feasibility study on deep‐neural‐network‐based dose‐neutral dual‐energy digital breast tomosynthesis". *MEDICAL PHYSICS, 2023 · 학술지 논문*.
- S. Yun, D. Choi, S. Lee, S. Cho. "Folded-VVBP Tensor Network for Sparse-view CT Image Reconstruction". *17th International Meeting on Fully Three-Dimensional Image Reconstruction in Radiology and Nuclear Medicine, 2023 · 심사 원저 논문*.
- C. Oh, T. Lee, S. Cho. "Improving Bump Defect Detection in Semiconductor Chips with U-Net Preprocessing and YOLOv3 Model: A Phantom-Based Study". *KSNT, 2023 · 학술대회 발표·초록*.
- C. Oh, J. Soh, D. Lee, M. Park, M. Ito, B. Lee, S. Cho. "Enhancing Lithium-Ion Battery Tomosynthesis Reconstruction Images using a 3-D UNet". *IEEE Nulcear Science Symposium, Medical Imaging Conference and Room, 2023 · 학술대회 발표·초록*.
- H. Jo, G. Kim, B. Lee, J. Park, S. Cho. "An attenuation model-based dual-energy calibration method for dual-energy luggage inspection system". *IEEE Nulcear Science Symposium, Medical Imaging Conference and Room, 2023 · 학술대회 발표·초록*.
- C. Oh, S. Cho. "3D U-Net을 활용한 리튬이온 배터리 Tomosynthesis 영상 개선". *KSRI, 2023 · 학술대회 발표·초록*.
- D. Choi, S. Yun, G. Kim, S. Cho. "Ramp Filtering Effect Mitigation Network for Metal Artifact Reduction in the Image Domain". *KSRI, 2023 · 학술대회 발표·초록*.
- G. Kim, S. Yun, T. Lee, S. Cho. "순환생성 적대신경망을 이용한 합성 파노라마 엑스레이 초해상도 이미지 생성". *KSRI, 2023 · 학술대회 발표·초록*.
- S. Hyun, S. Lee, S. Cho. "Missing view interpolation using reprojection data: a preliminary study". *KSRI, 2023 · 학술대회 발표·초록*.
- S. Yun, S. Lee, D. Cho, S. Cho. "Sparse-view CT image reconstruction by use of the Folded view-by-view backprojection tensor network". *KSRI, 2023 · 학술대회 발표·초록*.
- G. Kim, S. Yun, S. Hyun, T. Lee, S. Cho. "Super-Resolution of Synthetic Dental Panoramic X-ray Images using Unsupervised Learning with CycleGAN". *KSMP, 2023 · 학술대회 발표·초록*.
- J. Hwang, G. Kim, S. Cho, J. Yoon, H. Lee, I. Yeo. "Reconstructing online images during radiotherapy (On-beam CT) to validate and address setup uncertainties". *KSMP, 2023 · 학술대회 발표·초록*.
- S. Hyun, H. Kim, J. Sho, S. Cho. "Feasibility Study of Method for Synthesizing Rib-Suppressed Chest Radiography from Digital Tomosynthesis System Using 2D CNT Array". *AAPM, 2023 · 학술대회 발표·초록*.
- S. Lee, S. Hyun, S. Cho. "Enhancing of Scout Scan Using Diffusion Denoising in Digital Breast Tomosynthesis". *AAPM, 2023 · 학술대회 발표·초록*.
- S. Yun, S. Lee, D. Cho, S. Cho. "Folded-VVBP tensor network for sparse-view CT image reconstruction". *KSIIM, 2023 · 학술대회 발표·초록*.
- S. Lee, S. Hyun, S. Cho. "Denoising of pre-shot images using the diffusion model for digital breast tomosynthesis". *KSMP, 2023 · 학술대회 발표·초록*.
- S. Lee, S. Hyun, D. Kim, S. Cho. "Model observer analysis for suggestion of angular range in digital breast tomosynthesis based on patient breast type". *IFMIA, 2023 · 학술대회 발표·초록*.
- J. Hwang, H. Kim, T. Lee, D. Choi, T. Kwon, Y. Kim, S. Cho. "Effective phantom design for an accurate geometry calibration in an offset-detector-based cone-beam CT system". *IFMIA, 2023 · 학술대회 발표·초록*.
- S. Yun, U. Jeong, T. Kwon, D. Choi, T. Lee, S. Ye, G. Cho, S. Cho. "Penalty-driven enhanced self-supervised learning (Noise2Void) for CBCT denoising". *SPIE medical imaging, 2023 · 학술대회 발표·초록*.
- J. Soh, S. Hyun, H. Kim, M. Ito, Y. Jung, T. Kim, S. Cho. "Smooth manifold extraction for 2D synthetic radiography using 2D CNT array-based DTS system". *SPIE medical imaging, 2023 · 학술대회 발표·초록*.

**2022**

- K. Son, J. Kim, C. Kao, S. Cho. "Feasibility study of a concurrent image reconstruction algorithm for proton therapy with in-beam TOF-PET". *Journal of the Korean Physical Society, v.81, pg. 1091–1099, 2022 · 학술지 논문*.
- S. Lee, H. Kim, H. Lee, S. Cho. "Deep-learning-based projection-domain breast thickness estimation for shape-prior iterative image reconstruction in digital breast tomosynthesis". *MEDICAL PHYSICS, v.49, pg. 3670-3682, 2022 · 학술지 논문*.
- D. Lee, S. Yun, J. Soh, S. Lim, H. Kim, S. Cho. "A generalized simultaneous algebraic reconstruction technique (GSART) for dual-energy X-ray computed tomography". *JOURNAL OF X-RAY SCIENCE AND TECHNOLOGY, v.30, no.3, pp.549-566, 2022 · 학술지 논문*.
- D. Choi, T. Kwon, J. Hwang, JI. Hwang, Y. Choi, S. Cho. "Virtual non-metal network for metal artifact reduction in the sinogram domain". *7th International Conference on Image Formation in X-Ray Computed Tomography, 2022 · 심사 원저 논문*.
- S. Yun, U. Jeong, D. Kim, H. Kim, S. Cho. "Dual-domain network with transfer learning for bowtie-filter-induced artifacts in half-fan cone-beam CT". *7th International Conference on Image Formation in X-Ray Computed Tomography, 2022 · 심사 원저 논문*.
- S. Lim, S. Cho, T. Lee. "U-Net based X-ray image background removal method for semiconductor bonding defect inspection". *IEIE, 2022 · 학술대회 발표·초록*.
- T. Kwon, D. Choi, J. Hwang, S. Yun, S. Cho. "Feasibility Study of Metal Artifact Reduction Using Virtual Non-Metal Network in the Sinogram Domain". *IEEE Nulcear Science Symposium, Medical Imaging Conference and Room, 2022 · 학술대회 발표·초록*.
- S. Yun, T. Lee, T. Kwon, S. Cho. "A scatter artifact correction network in cone-beam CT using paired fan-beam slot scan data". *IEEE Nulcear Science Symposium, Medical Imaging Conference and Room, 2022 · 학술대회 발표·초록*.
- H. Kim, H. Lee, S. Lee, Y. Choi, Y. Choi, K. Kim, W. Seo, C. Shin, S. Cho. "A feasibility study of dual-energy digital breast tomosynthesis for three-compartment-breast imaging". *SPIE medical imaging, 2022 · 학술대회 발표·초록*.
- S. Lim, S. Hyun, C. Oh, S. Cho. "A beam-filter-based low-dose imaging for multi-detector-row helical CT". *SPIE medical imaging, 2022 · 학술대회 발표·초록*.

**2021**

- J. Moon, M. Park, S. Cho, J.G. Park, S.H. Jung. "Image reconstruction with sparse-view measurements from a ring scanning gamma CT system". *Journal of Instrumentation, v.16, no.2, 2021 · 학술지 논문*.
- S. Yun, Y. Kim, H. Kim, S. Lee, U. Jeong, H. Lee, Y.W. Choi, S. Cho. "Three-compartment-breast (3CB) prior-guided diffuse optical tomography based on dual-energy digital breast tomosynthesis (DBT)". *Bioedical optics express, v.12, no.8, pp.4837 - 4851, 2021 · 학술지 논문*.
- S. Cho, S. Lee, J. Lee, D. Lee, H. Kim, J.H. Ryu, K. Jeong, K.G. Kim, K.H. Yoon, S. Cho. "A novel low-dose dual-energy imaging method for a fast-rotating gantry-type CT scanner". *IEEE Transactions on Medical Imaging, 2021 · 학술지 논문*.
- D. Lee, S. Cho. "Learned energy-flexible algorithm using joint sparsity for dual-energy CT: a preliminary study". *16th International Meeting on Fully Three-Dimensional Image Reconstruction in Radiology and Nuclear Medicine, 2021 · 심사 원저 논문*.
- S. Cho, T. Kwon, J. Lee, S. Cho. "Feasibility study of residual U-Net based low-dose dual-energy imaging for a gantry-type CT scanner". *16th International Meeting on Fully Three-Dimensional Image Reconstruction in Radiology and Nuclear Medicine, 2021 · 심사 원저 논문*.
- S. Yun, D. Lee, H Kim, R. Pua, S. Cho, S. Cho. "Efficient prior image generation for normalized metal artifact reduction (NMAR) using normalized sinogram surgery with the beam-hardening correction". *16th International Meeting on Fully Three-Dimensional Image Reconstruction in Radiology and Nuclear Medicine, 2021 · 심사 원저 논문*.
- S. Lee, H. Kim, H. Lee, S. Cho. "Breast thickness map estimation and its associated correction in DBT imaging". *AAPM, 2021 · 학술대회 발표·초록*.
- J. Kim, J. Hwang, K. Ko, E. Ko, S. Cho, G. Cho. "Ghost Imaging with Bayesian denoising Method". *IEIE, 2021 · 학술대회 발표·초록*.
- T. Kwon, J. Soh, D. Choi, S. Lim, D. Woo, N. Lee, J. Kim, S. Cho. "심층신경망 기반의 3차원 광학 현미경 영상을 이용한 디스플레이 불량 판별". *IEIE, 2021 · 학술대회 발표·초록*.
- J. Soh, S. Kim, C. Kim, B. Cho, S. Cho. "Simulation study of a electron arc therapy with a scatterer for skin cancer in the distal extremities". *KSMP, 2021 · 학술대회 발표·초록*.
- D. Lee, U. Jeong, S. Yun, J. Hwang, S. Cho. "Learned energy-flexible algorithm using joint sparsity for dual-energy CT". *KSMP, 2021 · 학술대회 발표·초록*.
- S. Yun, D. Lee, H. Kim, R. Pua, S. Cho, S. Cho. "Efficient prior image generation for normalized metal artifact reduction (NMAR) using normalized sinogram surgery with the beam-hardening correction". *KSMP, 2021 · 학술대회 발표·초록*.
- U. Jeong, H. Kim, S. Lee, S. Cho. "디지털 유방 단층촬영에서의 지도학습 기반 산란 저감 방법 연구". *KSMP, 2021 · 학술대회 발표·초록*.
- H. Kim, S. Cho, S. Cho. "Advanced Wiener Filter for Helical Windmill Artifact Reduction". *IFMIA, 2021 · 학술대회 발표·초록*.
- T. Kwon, D. Choi, J. Hwang, J. Lee, J. Lim, I. Lee, S. Cho. "Algorithm for removing shading artifacts around dental prosthesis in dental panoramic image". *IFMIA, 2021 · 학술대회 발표·초록*.
- S. Yun, D. Lee, S. Cho. "A feasibility study of metal artifacts reduction using weighted iterative reconstruction algorithm for frequency split metal artifact reduction". *IFMIA, 2021 · 학술대회 발표·초록*.

**연도 표기 없음**

- J .Park, A. Gupta, W. Kim, J. Lim, S. Yeo, D. Kim, C. Jeong, K. Yoon, S. Cho, J. Ahn, M. Mallory, J. Ryu. "Stationary Multi X-ray Source System with Carbon Nanotube Emitters for Digital Tomosynthesis". *Medical Imaging Conference - Physics of Medical Imaging · 학술대회 발표·초록*.
- J. Park, J. Jung, A. Gupta, J. Soh, C. Jeong, J. Ahn, S. Cho, K. Yoon, D. Kim, M. Mativenga, J. Ryu. "Multi-beam X-ray Sources with Carbon Nanotube Emitter for Tomosynthesis System". *Conference on Medical Imaging - Physics of Medical Imaging · 학술대회 발표·초록*.

## 수상

누리집 Awards 페이지의 2022–2025년 구역 32건이다. 구성원과 졸업생의 학회 발표상·논문상, 창업경진대회 입상·진출·선정, 장학생·연구 프로그램 선정이 함께 실려 있다. 날짜는 구역의 연도이고, 이름과 상 이름은 누리집 표기 그대로다.[^awards]

- 2025 · Da-in Choi: Best Poster Award, The 39th Conference of Korean Society of imaging Informatics in Medicine
- 2025 · Da-in Choi: Best Poster Presentation, The 18th Int'l Meeting on Fully 3D Image Reconstruction in Radiology and Nuclear Medicine
- 2025 · Da-in Choi: Best Poster Award, International Forum on Medical Imaging in Asia
- 2024 · Joonil Hwang, Yeonkyoung Choi: 도전K스타트업 본선 진출, 창업
- 2024 · Sungho Yun: 2024방사선 산업학회 신진연구자발표대회 우수발표상
- 2024 · Joonil Hwang, Yeonkyoung Choi: 창업유망팀 U300+ 1위, 창업
- 2024 · Cecilia Nova Wijaya: 2024년도 한국방사선산업학회 정기총회 및 학술대회 우수논문발표상 수상
- 2024 · Joonil Hwang, Yeonkyoung Choi: E5 창업경진대회 2024, 2위
- 2024 · Joonil Hwang: 2024 한국의학물리학회 춘계 최우수 포스터상
- 2024 · Joonil Hwang, Yeonkyoung Choi: 제4회 원자력 혁신창업경진대회 최우수상, 창업
- 2024 · Subong Hyun: 2024 한국의학물리학회 춘계 우수 포스터상
- 2024 · Joonil Hwang, Yeonkyoung Choi: 생애최초패키지 (건국대학교) , 창업
- 2024 · Subong Hyun: 2024 대한의학영상정보학회 장려 포스터상
- 2024 · Joonil Hwang, Yeonkyoung Choi: 정주영창업경진대회 본선진출, 창업
- 2024 · Da-in Choi: 2024 The 10th Japan-Korea Joint Meeting on Medical Physics Young Investigator Award
- 2024 · Joonil Hwang: 2024 대한의학영상정보학회 장려 포스터상
- 2024 · Da-in Choi: 2024년도 한국방사선산업학회 정기총회 및 학술대회 우수논문발표상 수상
- 2023 · Joonil Hwang: 2023 한국의학물리학회 춘계학술대회 우수포스터 발표상 수상
- 2023 · Joonil Hwang: 제 3회 원자력 혁신창업경진대회 우수상
- 2023 · Sungho Yun: Fully 3D 2023 student Travel Awards 수상
- 2023 · Seoyoung Lee: 한국원자력학회(KNS) 퀴리상(Curie Student Award) 수상
- 2023 · Sungho Yun: 2023년도 제 37회 대한의학영상정보학회 최우수구연발표상 수상
- 2023 · Cecilia Nova Wijaya: The IAEA Marie Sklodowska-Curie Fellowship Programme (MSCFP) 선정
- 2023 · Joonil Hwang: DMC 이노베이션 캠프 창업경진대회 (DIC2023) 최우수상
- 2023 · Joonil Hwang: NAACst STEP 창업경진대회 4기 최우수상
- 2023 · Seoyoung Lee: International Forum on Medical Imaging Asia(IFMIA) 2023 Best Presentation Award 수상
- 2023 · Yeonkyoung Choi: International Forum on Medical Imaging Asia(IFMIA) 2023 Best Presentation Award 수상
- 2022 · Hyoyi Kim: 2nd Prize in Unicorn House EO Studio(창업)
- 2022 · Yejin Kim: 60th PTCOG (Particle Therapy Co-operative Group) Young Investigator Award 수상
- 2022 · Dohyun Lim: 2022 두산에너빌리티 장학생 선정
- 2022 · Yejin Kim: 한국의학물리학회 2022 추계 학술발표회 우수종설상 수상
- 2022 · Sungho Yun: 한국의학물리학회 2022 추계 학술발표회 구두발표 장려상 수상

## 연락과 위치

- 위치: Rm. 5114, N27 Eureka Building, KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon(첫 화면 표기, 국문 표기 「대한민국 대전광역시 유성구 어은동 대학로 KAIST 유레카관 N27 5114호」)[^home]
- 전화: 연구실 +82-42-350-3884, 교수 +82-42-350-3828, 팩스 +82-42-350-3810[^home][^prof]
- 교수 이메일: scho@kaist.ac.kr[^nqe][^nqeprof]
[^p1]: S. Yun 외, S. Cho, Physics in Medicine & Biology 69, 225012 (온라인 2024-11-12). <https://doi.org/10.1088/1361-6560/ad8da2> 초록 기준.
[^p2]: S. Hyun 외, S. Cho, Physics in Medicine & Biology 71, 105007 (온라인 2026-05-20). <https://doi.org/10.1088/1361-6560/ae6a5a> 초록 기준.
[^p3]: S. Yun, S. Hyun, D.-i. Choi, S. Cho, Medical Physics 53, e70336 (온라인 2026-02-16). <https://doi.org/10.1002/mp.70336> 초록 기준.
[^p4]: S. Hyun 외, S. Cho, Journal of Medical Imaging 12, 1-18 (2025). <https://doi.org/10.1117/1.jmi.12.s2.s22008> 초록 기준.
[^p5]: H. Kim 외, S. Cho, Medical Physics 50, 791-807 (온라인 2022-11-03). <https://doi.org/10.1002/mp.16071> 초록 기준.
[^p6]: D. Lee 외, S. Cho, Journal of X-Ray Science and Technology 30, 549-566 (2022). <https://doi.org/10.3233/xst-211054> 초록 기준.
[^p7]: T. Kwon 외, S. Cho, Scientific Reports 13, 8817 (온라인 2023-05-31). <https://doi.org/10.1038/s41598-023-35805-1> 초록 기준.
[^p8]: K. Son, J. S. Kim, C.-M. Kao, S. Cho, Journal of the Korean Physical Society 81, 1091-1099 (온라인 2022-08-03). <https://doi.org/10.1007/s40042-022-00571-2> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 연구실 누리집 첫 화면 <https://www.mirlab.kaist.ac.kr/> (교수 카드, About, Get to Know Us, Detained Info, Research Areas, 바닥글의 전화·위치, 2026-10-23 열람)
[^sparse]: 연구실 누리집 Sparse-sampling Approach to Low-dose CT 페이지 <https://www.mirlab.kaist.ac.kr/%EB%B3%B5%EC%A0%9C-sparse-sampling> (2026-10-23 열람)
[^phys]: 연구실 누리집 Methods for Physical Factor Correction 페이지 <https://www.mirlab.kaist.ac.kr/%EB%B3%B5%EC%A0%9C-physical-factor-correction> (산란 보정과 금속 인공물 저감, 2026-10-23 열람)
[^novel]: 연구실 누리집 Novel Imaging Systems 페이지 <https://www.mirlab.kaist.ac.kr/%EB%B3%B5%EC%A0%9C-novel-imaging-system> (양성자 CT, DBT·DOT, 2026-10-23 열람)
[^igrt]: 연구실 누리집 Physics of Image-guided Radiation Therapy 페이지 <https://www.mirlab.kaist.ac.kr/%EB%B3%B5%EC%A0%9C-image-guided-radiation-therapy> (2026-10-23 열람)
[^ndt]: 연구실 누리집 Nondestructive Testing 페이지 <https://www.mirlab.kaist.ac.kr/%EB%B3%B5%EC%A0%9C-nondestructive-testing> (2026-10-23 열람)
[^metro]: 연구실 누리집 CT Metrology-based Manufacturing Applications 페이지 <https://www.mirlab.kaist.ac.kr/%EB%B3%B5%EC%A0%9C-ct-metrology-based-applica> (2026-10-23 열람)
[^dl]: 연구실 누리집 Deep Learning based MIR Research 페이지 <https://www.mirlab.kaist.ac.kr/%EB%B3%B5%EC%A0%9C-deep-learning-based-mir-research> (2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <https://www.mirlab.kaist.ac.kr/%EB%B3%B5%EC%A0%9C-professor> (직위·소속, Professional Activities, Education, Research Experience, Awards, 전화·팩스, 2026-10-23 열람)
[^members]: 연구실 누리집 Members 페이지 <https://www.mirlab.kaist.ac.kr/%EB%B3%B5%EC%A0%9C-members> (Students 구역의 Ph. D Candidate Students·Master Candidate Students 카드, 2026-10-23 열람)
[^alumni]: 연구실 누리집 Alumni 페이지 <https://www.mirlab.kaist.ac.kr/%EB%B3%B5%EC%A0%9C-alumni> (Ph. D Degree, Master Degree, Undergraduate 카드, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publications 메뉴의 Peer-reviewed Journal Papers 페이지 <https://www.mirlab.kaist.ac.kr/%EB%B3%B5%EC%A0%9C-publications> (1–101번), Peer-reviewed Original Articles 페이지 <https://www.mirlab.kaist.ac.kr/%EB%B3%B5%EC%A0%9C-peer-reviewed-original-articles> (1–36번), Conference Proceedings and Abstracts 페이지 <https://www.mirlab.kaist.ac.kr/%EB%B3%B5%EC%A0%9C-conference-proceedings-and-abstr> (1–238번) (2026-10-23 열람)
[^awards]: 연구실 누리집 Awards 페이지 <https://www.mirlab.kaist.ac.kr/%EB%B3%B5%EC%A0%9C-awards> (2025, 2024, 2023, 2022 구역, 2026-10-23 열람)
[^nqe]: KAIST 원자력및양자공학과 연구실 목록 <https://nuclear.kaist.ac.kr/research/the_lap.php?category=004> 와 영문 페이지 <https://nuclear.kaist.ac.kr/eng/research/the_lap.php?category=004> (조승룡 항목의 국·영문 연구실 이름, 직위, 학위, 이메일, 누리집 주소, 2026-10-23 열람)
[^nqeprof]: KAIST 원자력및양자공학과 교수 페이지 <https://nuclear.kaist.ac.kr/people/professor.php> (조승룡 교수 항목의 최종학위, 연구실 위치, 전화, 이메일, 2026-10-23 열람)

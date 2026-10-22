# 뇌 계측 및 컴퓨팅 연구실 (Neuro-Instrumentation & Computational Analysis Lab, NICA)

**KAIST 전기및전자공학부 · 윤영규 교수**

- 분야: 뇌공학, 뇌이미징, 광학시스템 설비, 바이오신호처리, 인공지능
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 광학 영상·현미경[^research][^p1][^p4], 생물 영상 분석[^research][^p3][^p8], 계산신경과학[^research], 뇌 모방 인공지능[^research], 메모리 내 연산[^p7]
- 홈페이지: <https://nica.kaist.ac.kr/>
- 근거와 출처: [뇌 계측 및 컴퓨팅 연구실 근거 페이지](nica-sources.md)

> 뇌와 생체 조직을 빛으로 관찰하는 광학 영상 기술과, 그렇게 얻은 큰 영상 데이터를 분석하는 계산·인공지능 기술을 함께 개발하는 연구실이다.[^home][^research]

## 무엇을 연구하나

누리집 첫 화면은 연구실이 뇌와 생체의학 응용을 위한 광학 기술과 계산 기술을 개발한다고 소개한다.[^home] 전기및전자공학부 교수 소개와 반도체시스템공학과 연구실 목록은 주요 연구를 뇌공학, 뇌이미징, 광학시스템 설비, 바이오신호처리, 인공지능으로 적는다.[^eeprof][^ssel] Research 페이지는 연구를 세 묶음으로 나눈다. 뇌에서 큰 데이터를 얻는 생체의학 영상, 그 데이터를 분석하는 생체 신호처리, 그리고 인공지능과 생체의학공학이다.[^research]

첫째 묶음인 영상 연구는 세 주제로 이루어진다. 기능 영상에서는 유전공학으로 신경세포가 활동할 때 밝기가 바뀌게 만들면 뇌 활동이 눈에 보이게 되는데, 이 빛 신호를 높은 시공간 해상도로 기록하는 광학 영상 기술을 개발한다.[^research] 계산 영상에서는 물리·생물·정보 이론·표본화 정리 같은 요인이 영상 장치의 성능을 제한하므로, 기계학습으로 제한된 데이터에서 더 많은 정보를 예측하는 방법을 쓴다.[^research] 다중·초해상도 영상에서는 형광 분자의 방출 스펙트럼이 넓어 형광 현미경이 한 번에 단백질 네 개까지만 볼 수 있다는 한계를 넘으려고, 기계학습 알고리즘으로 섞인 신호를 원래 성분으로 나누는 블라인드 신호 분리를 이용한 다중 영상 기술을 개발한다.[^research]

둘째 묶음인 신호처리 연구는 뇌 영상 처리와 신경 데이터 마이닝이다. Research 페이지는 최신 기능 영상 방법이 초당 1기가바이트가 넘는 데이터를 만들어 자동 분석 알고리즘이 필요하다고 보고, 정답 표시(라벨)가 없는 데이터로도 뇌 영상을 처리하는 빠르고 확장 가능한 기계학습 알고리즘을 개발한다고 적는다.[^research] 신경 데이터 마이닝에서는 계산 방법으로 뇌 활동 데이터를 분석해 정보 흐름을 정량화하고 신경세포 사이의 기능적 연결을 찾아, 되풀이되는 패턴, 함께 동작하는 국소 회로, 시냅스 세기 정보를 뽑아내려 한다.[^research]

셋째 묶음은 인공지능과 생체의학공학이다. 생물 영감 인공지능에서는 생물 지능의 구조와 학습 과정의 특성을 인공지능에 넣으려 하고, 의료 인공지능에서는 촬영 조건·장비의 차이와 적은 라벨 데이터 때문에 실제 진단에 인공지능을 쓰기 어려운 문제를, 인공지능 기법과 데이터 특성에 대한 이해를 결합해 풀려고 한다.[^research]

대표 논문으로 보면 연구는 다섯 갈래다. 첫째, 살아 있는 동물의 뇌 활동을 빠르게 3차원으로 찍는 현미경이다(대표 논문 1, 2).[^p1][^p2] 둘째, 영상의 잡음과 빛의 일그러짐을 계산으로 바로잡는 기술이다(대표 논문 3, 4).[^p3][^p4] 셋째, 한 시료에서 여러 단백질을 각각 구별해 찍는 다중 형광 영상이다(대표 논문 5, 6).[^p5][^p6] 넷째, 멤리스터 배열 위에서 인공지능 계산을 하는 아날로그 계산 플랫폼이다(대표 논문 7).[^p7] 다섯째, 서로 다른 생체의학 영상 사이를 바꾸는 인공지능이다(대표 논문 8).[^p8]

## 주요 연구 주제

### 1. 뇌 활동을 빠르게 3차원으로 찍는 현미경

계산 현미경 방법 3DM은 신경 활동이 시간적으로 드문드문 일어난다는 성질을 이용해, 디컨볼루션 현미경이 풀어야 하는 역문제를 두 신경망으로 다시 세워 풀었다. 살아 있는 제브라피시 유생의 뇌 전체 신경 활동을 초당 최대 4.2 부피로 찍었다.[^p1] 경사면 현미경과 유전자로 발현되는 전압 지시자를 써서 살아 있는 제브라피시 유생에서 초당 최대 200 부피의 3차원 전압 영상도 얻었다.[^p2] Research 페이지는 이 주제에 이벤트 카메라로 생체 신경·혈관의 동적 변화를 찍고 복원한 연구(2026)와 신경세포 몸체에 모이는 붉은 형광 칼슘 지시자 연구(2025) 같은 공동 연구도 둔다.[^research] 대표 논문 1, 2.

### 2. 영상을 계산으로 바로잡는 기술

자기지도 학습으로 전압 영상 데이터의 잡음을 없애는 SUPPORT를 만들어, 한 픽셀 값이 시간·공간으로 이웃한 픽셀에 크게 의존한다는 점을 합성곱 신경망으로 이용했다.[^p3] 파면 센서 없이 영상만으로 빛의 일그러짐을 재고 바로잡는 적응 광학에서는, 그래프 기반 모형으로 장치의 불완전함을 스스로 보정하고 위치마다 다른 일그러짐과 움직이는 생체 시료까지 다루는 GRAPHYCS를 내놓았다.[^p4] Research 페이지는 이 밖에 재귀 광 전파 신경망으로 초점을 계산으로 다시 맞추는 3차원 형광 현미경(2022)과, 칼슘 영상 데이터를 효율적으로 정렬하고 자동 분석하는 알고리즘(2021, 2023)을 든다.[^research] 대표 논문 3, 4.

### 3. 한 시료에서 여러 단백질을 찍는 다중 형광 영상

PICASSO는 기준 방출 스펙트럼 없이 한 번의 촬영으로 공간적으로 겹치는 단백질을 15색 넘게 구별해 찍고, 순환 면역형광 염색과 결합해 생쥐 뇌를 세 주기에 45색으로 찍었다.[^p5] SEPARATE는 두 단백질을 같은 형광체로 표지한 뒤 3차원 공간 발현 패턴의 차이로 신경망이 신호를 나눠, 3차원 다중 영상의 반복 주기 수를 절반으로 줄였다.[^p6] Research 페이지는 확장 현미경으로 생쥐 배아 전체를 나노미터 단위 해상도로 찍은 연구(2025)와 팽창하는 조직 젤 속 3차원 다중 순환 영상을 정확하게 정합하는 연구(2025)도 이 주제에 둔다.[^research] 대표 논문 5, 6.

### 4. 인공지능 계산 하드웨어와 의료 영상 인공지능

KAIST의 Shinhyun Choi 교수 연구실과 함께, 선택 소자가 없는 아날로그 멤리스터 배열과 주변 회로·디지털 제어기로 이루어진 계산 플랫폼을 만들어, 보정 연산이나 사전 학습 없이 스스로 보정하며 실시간 영상의 전경과 배경을 나누는 인공지능 알고리즘을 돌렸다.[^p7][^pubs] 짝지은 데이터 없이 서로 다른 생체의학 영상 사이를 바꾸면서 공간 정보와 신호 세기를 보존하는 영상 간 변환 방법 STABLE을 만들어, 제브라피시 뇌 칼슘 영상 변환과 가상 조직 염색에 적용했다.[^p8] 대표 논문 7, 8.

### 5. 신경 데이터 마이닝

Research 페이지는 신경 데이터 마이닝의 성과로 두 학회 논문을 든다. KAIST의 Kijung Shin 교수 연구실과 함께, 여러 개체가 한꺼번에 맺는 고차 상호작용을 하이퍼에지(여러 개체를 한꺼번에 잇는 연결)로 나타내 아직 드러나지 않은 하이퍼에지를 예측하는 알고리즘(2025)과, 시간 변동이 있어도 자주 나타나는 시간 순서 패턴을 찾는 알고리즘(2025)을 발표했다.[^research][^pubs]

## 대표 논문

랩 Publication 목록의 2021–2026년 학술지 논문 가운데 윤영규 교수가 마지막 저자이거나 공동 교신저자(\*\*)인 논문을, 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2021 | [3DM: Deep decomposition and deconvolution microscopy for rapid neural activity imaging](https://doi.org/10.1364/oe.439619) · Optics Express | 신경 활동을 3차원 부피로 찍는 계산 현미경 방법 3DM을 만들었다. 디컨볼루션 현미경(흐려진 영상을 계산으로 되돌려 선명하게 만드는 현미경)의 주요 난제는 잘 정의되지 않은 역문제(관측 결과에서 원인을 거꾸로 구할 때 답이 하나로 정해지지 않거나 작은 오차에 크게 흔들리는 문제)다. 이 연구는 신경 활동이 시간적으로 드문드문 일어난다는 성질을 이용해 이 역문제를 다시 세우고, 희소 분해와 디컨볼루션을 맡는 두 신경망으로 풀었다. 살아 있는 제브라피시 유생의 뇌 전체 신경 활동을 1040 µm × 400 µm × 235 µm 시야에서, 가로 1.7 µm·깊이 방향 5.4 µm로 추정되는 해상도로 초당 최대 4.2 부피까지 찍어 성능을 보였다. | 공동 1저자 E.-S. Cho·S. Han, 마지막 저자 윤영규 (5명) |
| 2 | 2026 | [Three-dimensional voltage imaging in live larval zebrafish brains using fully genetically encoded voltage indicator](https://doi.org/10.1038/s41598-026-58107-8) · Scientific Reports | 전압 영상(세포막 전압의 변화를 빛 신호로 기록하는 영상)은 빠른 신경 사건을 높은 시간 정밀도로 직접 재는 도구다. 뇌는 3차원 회로라서 부피 전체의 신호를 기록해야 하지만, 많은 신경세포의 3차원 전압 영상은 빠른 촬영 속도, 높은 신호 대 잡음비, 넓은 부피를 함께 요구해 어렵다. 이 연구는 경사면 현미경(oblique plane microscopy)과, 유전자로 발현되는 전압 지시자(막 전압에 따라 형광 밝기가 바뀌는 단백질) Ace-mNeon2-Kv2.1을 써서 살아 있는 제브라피시 유생에서 초당 최대 200 부피의 3차원 전압 영상을 얻었다. 염료 없이 전압을 영상화해 실험 과정을 단순하게 하고 생체 전압 영상 실험의 재현성을 높인다. | 공동 1저자 E.-S. Cho·M. Eom·S. Zhou, 공동 교신 저자 C.-H. Kim·K. D. Piatkevich·윤영규 (8명, 윤영규 마지막) |
| 3 | 2023 | [Statistically unbiased prediction enables accurate denoising of voltage imaging data](https://doi.org/10.1038/s41592-023-02005-8) · Nature Methods | 전압 영상 데이터의 푸아송–가우스 잡음(광자 수의 통계적 흔들림에서 생기는 잡음과 검출 회로의 잡음이 섞인 잡음)을 없애는 자기지도 학습 방법 SUPPORT를 만들었다. 전압 영상에서는 앞뒤 프레임만으로 예측할 정보가 없을 때에도 한 픽셀 값이 시간·공간으로 이웃한 픽셀에 크게 의존한다는 점에 착안했다. 이 의존성을 시공간 블라인드 스폿(예측할 픽셀 자신은 보지 못하게 가린 영역)을 둔 합성곱 신경망으로 잡아내, 다른 프레임의 정보로는 활동전위가 있었는지 알 수 없는 프레임까지 정확히 잡음을 없앤다. 시뮬레이션과 실험으로 전압 영상과 다른 종류의 현미경 영상에서 장면 속 동적 변화를 보존하면서 잡음을 정밀하게 없앰을 보였다. | 공동 1저자 M. Eom·S. Han·P. Park, 마지막 저자 윤영규 (25명) |
| 4 | 2026 | [Graph-based modeling of optical system enables adaptive optics on dynamic samples with self-calibration](https://doi.org/10.1016/j.isci.2026.116769) · iScience | 파면 센서 없이 영상만으로 빛의 일그러짐을 재는 센서 없는 적응 광학은 하드웨어 방식보다 이점이 크지만, 이상적인 모형이 장치의 불완전함을 담지 못하면 성능이 떨어지고, 시야 전체에 같은 일그러짐만 다루며, 대상이 멈춰 있다고 가정해 움직이는 생체 시료에 쓸 수 없었다. 이 연구는 미분 가능한 그래프 기반 모형 GRAPHYCS로 장치 고유의 불완전함을 스스로 보정하고, 국소 일그러짐을 모형에 넣어 넓은 시야에서 위치마다 다른 파면을 재며, 살아 있는 시료의 동적 영상을 지원한다. 시뮬레이션에서 장치가 불완전할 때 해석적 위상 다이버시티 방법보다 파면 측정 정확도를 최대 9배 높였고, 실제 현미경 실험에서도 이 연구에서 비교한 위상 다이버시티 기반 방법들보다 일관되게 좋은 결과를 냈다. 살아 있는 제브라피시 뇌 영상에서는 하드웨어를 더하지 않고 파면 측정과 신경 활동 검출을 동시에 해냈다. | 공동 1저자 E.-S. Cho·J. Park, 공동 교신 저자 J.-H. Park·윤영규 (9명, 윤영규 마지막) |
| 5 | 2022 | [PICASSO allows ultra-multiplexed fluorescence imaging of spatially overlapping proteins without reference spectra measurements](https://doi.org/10.1038/s41467-022-30168-z) · Nature Communications | 초다중 형광 영상(한 시료의 여러 단백질을 각각 다른 형광으로 구별해 찍는 영상)을 하려면 방출 스펙트럼이 겹치는 형광체로 단백질을 표지한 뒤 영상을 분리해야 한다. 그러나 뇌처럼 성질이 고르지 않은 시료에서는 형광체의 방출 스펙트럼이 많이 달라져 이 일이 어렵다. PICASSO는 기준 방출 스펙트럼 없이, 공간적으로 겹치는 단백질을 한 번의 촬영 라운드에서 15색 넘게 찍는다. 형광체 수와 같은 수의 영상만 있으면 되어 대역 통과 필터를 쓰는 현미경으로도 다중 영상을 할 수 있다. 순환 면역형광 염색과 결합해 생쥐 뇌를 세 주기에 45색으로 찍었다. | 공동 1저자 J. Seo·Y. Sim·J. W. Kim, 공동 교신 저자 윤영규·J.-B. Chang (8명, 윤영규 7번째) |
| 6 | 2025 | [Doubling multiplexed imaging capability via spatial expression pattern-guided protein pairing and computational unmixing](https://doi.org/10.1038/s42003-025-08357-5) · Communications Biology | 3차원 다중 형광 영상은 신경과학에 꼭 필요한 기술이다. 2차원에서는 염색·촬영·신호 제거를 여러 주기 되풀이하는 순환 면역형광이 널리 쓰였지만, 두꺼운 시료는 한 번 염색에 12시간 넘게 걸려 3차원에서 여러 주기를 되풀이하면 지나치게 오래 걸린다. SEPARATE는 두 단백질을 같은 형광체로 표지하고 신경망으로 두 단백질의 3차원 공간 발현 패턴 차이에 따라 신호를 나눠, 형광체 하나로 단백질 두 개를 찍어 주기 수를 절반으로 줄인다. 특징 추출 신경망으로 단백질 사이 공간 패턴의 차이를 수치(특징 기반 거리)로 나타내 짝지을 단백질을 고르고, 단백질 열 개로 이 신경망을 검증했다. 형광체 세 개로 단백질 여섯 개의 3차원 다중 영상을 보였다. | 1저자 G. Kim, 공동 교신 저자 J.-B. Chang·윤영규 (6명, 윤영규 마지막) |
| 7 | 2025 | [Self-supervised video processing with self-calibration on an analogue computing platform based on a selector-less memristor array](https://doi.org/10.1038/s41928-024-01318-6) · Nature Electronics | 멤리스터 기반 플랫폼은 아날로그 영역에서 병렬로 계산할 수 있어 작고 에너지 효율이 높은 엣지 컴퓨팅(데이터가 생기는 기기 가까이에서 계산하는 방식) 인공지능 시스템에 쓰일 수 있다. 그러나 낮은 수율, 고르지 않은 특성, 내구성 문제 때문에 기기 안에서 학습까지 하는 실시간 인공지능 알고리즘을 돌리기 어려웠다. 이 연구는 선택 소자 없는 아날로그 멤리스터 배열로 계산 플랫폼을 만들었다. 산소 분포가 점진적인 계면형 산화 티타늄 멤리스터를 써서 높은 신뢰성과 선형성, 형성 과정(처음 쓰기 전에 높은 전압으로 전도 통로를 만드는 과정)이 필요 없는 성질, 자기 정류 특성을 얻었다. 선택 소자 없는 32 × 32(1K) 교차 배열, 주변 회로, 디지털 제어기로 이루어진 플랫폼은 보정 연산이나 사전 학습 없이 스스로 보정하며 아날로그 영역에서 인공지능 알고리즘을 돌린다. 실시간 영상의 전경·배경 분리에서 평균 최대 신호 대 잡음비 30.49 dB와 구조적 유사도 지수 0.81을 얻었고, 이 값은 이상적인 경우의 시뮬레이션 값과 비슷했다. | 공동 1저자 H. Jeong·S. Han, 공동 교신 저자 윤영규·S. Choi (19명, 윤영규 18번째) |
| 8 | 2025 | [Preserving spatial and quantitative information in unpaired biomedical image-to-image translation](https://doi.org/10.1016/j.crmeth.2025.101074) · Cell Reports Methods | 생물 시료를 분석하려면 여러 영상 방식의 결과를 함께 봐야 하는 경우가 많다. 짝지은 데이터로 학습하는 생체의학 영상 변환은 성과가 있었지만, 영상 정렬과 시료 준비의 어려움 때문에 짝지은 데이터를 얻기 어려운 경우가 많다. 짝 없이 학습하는 방법은 정확한 분석에 필요한 공간·정량 정보를 지키기 어려웠다. STABLE은 정보 일관성을 강제하고 학습 가능한 동적 업샘플링 연산자를 써서 픽셀 수준의 정확도를 얻는, 짝 없는 영상 간 변환 방법이다. 제브라피시 뇌 칼슘 영상의 변환과 가상 조직 염색을 포함한 여러 생체의학 영상 과제에서 기존 방법보다 공간 세부, 신호 세기, 정렬을 더 잘 보존함을 보였다. | 공동 1저자 J. Y. You·M. Eom·T.-I. Choi, 공동 교신 저자 P. Kim·C.-H. Kim·윤영규 (12명, 윤영규 마지막) |

## 교수와 전문 분야

윤영규 교수는 KAIST 전기및전자공학부 부교수이고, 전기및전자공학부 교수 소개는 Signal·Computer 디비전으로 적는다. 같은 소개의 주요 연구분야는 AI & Machine Learning, Multimedia Signal Processing, Biomedical Engineering, Photonics다.[^eeprof] People 페이지 소개는 교수가 반도체시스템공학과와 KAIST Institute for Human Augmentation Convergence에 겸직하며, 신경기술·광학 영상·컴퓨팅을 함께 다루는 학제 연구실을 이끈다고 적는다.[^people] 반도체시스템공학과 교수진에는 연구분야 「컴퓨터, 인공지능 및 소프트웨어」, 연구실 「뇌 계측 및 컴퓨팅 연구실」로 올라 있다.[^ssep]

People 페이지에 따르면 교수는 KAIST에서 전기공학 학사(2007)와 석사(2009)를, MIT에서 EECS 박사(2018)를 받았다. KAIST Institute 연구원(Research Engineer, 2009–2012)과 MIT 박사후연구원(2018)을 거쳐 2018년 KAIST 조교수가 됐고 2023년 부교수가 됐다.[^people] SeongHwan Cho 교수 연구실에서 한 혼성 신호 CMOS 회로 설계 연구로 2009 IEEE Transactions on Circuits and Systems Guillemon-Cauer Best Paper Award를 받았고, 박사과정에서는 Ed Boyden 교수와 함께 뇌 회로를 영상화하고 분석하는 광학·계산 도구를 개발했다.[^people] 누리집은 KAIST 부임 전 논문을 따로 묶어, 광 필드 현미경으로 동물 전체의 신경 활동을 3차원으로 동시에 찍은 연구(Nature Methods, 2014), 반복 확장 현미경(Nature Methods, 2017), 단백질의 방향성 진화로 형광 전압 지시자를 만든 연구(Nature Chemical Biology, 2018)와 시간 기반·전압 제어 발진기 기반 아날로그-디지털 변환기 회로 논문(2008–2012) 등을 적는다.[^pubs]

People 페이지가 적는 수상·영예는 Human Frontier Science Program(HFSP) Award(accelerator track, 2025), KAIST Breakthroughs 선정(2025, 2024, 2022), KAIST's Research Highlights 선정(2021), Samsung Scholarship(2012), IEEE CAS Guillemon-Cauer Best Paper Award(2009), KAIST 신입생 학업성취도 시험(수학·물리) 최고 성적(2003)이다.[^people] 첫 화면 소식은 교수가 2025 KAIST Top 10 Research Achievements Award를 받았다고 적는다(2026년 4월).[^home]

논문으로 보면 KAIST에서의 전문 분야는 뇌 활동을 3차원으로 빠르게 찍는 형광 현미경(대표 논문 1, 2),[^p1][^p2] 잡음 제거와 적응 광학 같은 계산 영상(대표 논문 3, 4),[^p3][^p4] 다중 형광 영상(대표 논문 5, 6),[^p5][^p6] 그리고 인공지능 계산 하드웨어와 생체의학 영상 인공지능(대표 논문 7, 8)이다.[^p7][^p8]

## 응용 분야

대표 논문들은 살아 있는 제브라피시 유생의 뇌 전체 신경 활동 영상(대표 논문 1, 2, 4)과 생쥐 뇌의 다중 단백질 영상(대표 논문 5)에 새 방법을 적용했다.[^p1][^p2][^p4][^p5] 대표 논문 7은 멤리스터 계산 플랫폼이 작고 에너지 효율이 높은 엣지 컴퓨팅 인공지능 시스템에 쓰일 수 있다고 보고, 실시간 영상의 전경·배경 분리로 시험했다.[^p7] 대표 논문 8은 영상 간 변환을 가상 조직 염색에 적용했다.[^p8] Research 페이지는 의료 진단 영상의 분류에 인공지능을 쓰는 의료 인공지능도 연구 주제로 든다.[^research]

## 구성원

연구실 누리집 People 페이지의 박사후연구원 2명, 박사과정 6명, 석사과정 1명, 학부생 5명이다.[^people] 과정과 연구 분야(Research area)는 페이지 표기다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Cho, Eun-Seo | 박사후연구원 | Imaging brain activity, Computational imaging | 1, 2, 3, 4, 8 |
| Han, Seungjae | 박사후연구원 | Computational imaging, Neuro-image processing | 1, 3, 7 |
| Kim, Gyuri | 박사과정 | Imaging brain activity, Neuro-data mining | 2, 3, 6 |
| Eom, Minho | 박사과정 | Computational neuroscience of mental disorders, Functional / structural connectomics, Neuro-image processing | 2, 3, 4, 6, 8 |
| You, Joshua Yedam | 박사과정 | Deep-learning driven biomedical & neural image processing, Functional / structural connectomics, Computational neuroscience | 8 |
| Kim, Soi | 박사과정 | Computational imaging, Neuro-image processing | 2 |
| Park, Joon | 박사과정 | Computational imaging, Neuro-image processing | 4 |
| Yu, Hayeong | 박사과정 | Computational imaging, Neuro-image processing |  |
| Park, Jinho | 석사과정 | Neural signal analysis |  |
| Kim, Seo Young | 학부 연구생 |  |  |
| Cho, Juno | 학부 연구생 |  |  |
| Ko, Sangjun | 학부 연구생 |  |  |
| Hong, Junseong | 학부 연구생 |  |  |
| Park, Seunghee | 학부 연구생 |  |  |

## 졸업생과 이전 구성원

누리집 People 페이지 Alumni 절의 석사 졸업생 6명, 방문 대학원생 1명, 학부 연구생 41명이다. 석사 졸업생의 연도는 각 카드의 학력 칸에 적힌 KAIST 석사 연도이고, 학부 연구생의 기간은 페이지가 이름 아래 적은 학기다. 진로는 페이지에 적혀 있지 않다. 학부 연구생 가운데 「Kim, Seo Young」·「Cho, Juno」·「Ko, Sangjun」은 현재 구성원 표에도 있고, 「Yu, Hayeong」·「Park, Joon」·「Ahn, Sungjin」은 뒤에 대학원생으로도 적혀 있다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Kang, Woosuk | M.S. (2021) |  |
| Cho, Junmo | M.S. (2022) |  |
| Shin, Changyeop | M.S. (2022) |  |
| Bae, Seoungbin | M.S. (2024) |  |
| Lee, Minyoung | M.S. (2024) |  |
| Ahn, Sungjin | M.S. (2025) |  |
| Liu, Huiling | M.S. student (visiting graduate student, Chongqing University of Technology (CQUT)) |  |
| Jeon, Jiwon | Undergraduate student (Spring 2019–Summer 2019) |  |
| Jeon, Sang Eon | Undergraduate student (Spring 2020) |  |
| Jeong, Jaewon | Undergraduate student (Summer 2020) |  |
| Nam, Seo Yeon | Undergraduate student (Summer 2020) |  |
| Jung, Hohurn | Undergraduate student (Summer 2020) |  |
| Park, Gyutae | Undergraduate student (Fall 2020) |  |
| Lee, Inhee | Undergraduate student (Fall 2020, Winter 2021–Spring 2022) |  |
| Lee, Chang Sun | Undergraduate student (Summer 2020–Winter 2020) |  |
| Lee, Jeongwon | Undergraduate student (Winter 2020–Spring 2021) |  |
| Cho, Eun Yeong | Undergraduate student (Winter 2020–Spring 2021) |  |
| Ryu, Hyun | Undergraduate student (Spring 2020–Summer 2021, Spring 2023) |  |
| Suh, Teokkyu | Undergraduate student (Spring 2021–Summer 2021) |  |
| Lee, Seyeon | Undergraduate student (Fall 2020–Fall 2021) |  |
| Kim, Eunsu | Undergraduate student (Winter 2020–Fall 2021) |  |
| Bae, Jeongin | Undergraduate student (Spring 2021–Fall 2021) |  |
| Yi, Euiin | Undergraduate student (Summer 2021–Winter 2021) |  |
| Jeon, Minsik | Undergraduate student (Fall 2021–Winter 2021) |  |
| Kim, Dawon | Undergraduate student (Winter 2021) |  |
| Lee, Sanghun | Undergraduate student (Fall 2021–Spring 2022) |  |
| Lee, Gyuwon | Undergraduate student (Winter 2021–Spring 2022, Fall 2022) |  |
| Lee, Sowoo | Undergraduate student (Spring 2022–Summer 2022) |  |
| Park, Mingi | Undergraduate student (Spring 2022) |  |
| Huh, Chan | Undergraduate student (Spring 2022) |  |
| Hwang, Namun | Undergraduate student (Spring 2022) |  |
| Ahn, Sungjin | Undergraduate student (Summer 2022–Fall 2022) |  |
| Choi, Jinsung | Undergraduate student (Summer 2022–Fall 2022) |  |
| Park, Jong Geon | Undergraduate student (Fall 2022) |  |
| Yu, Hayeong | Undergraduate student (Winter 2022–Fall 2023) |  |
| Park, Joon | Undergraduate student (Spring 2023–Winter 2023) |  |
| Cho, Hoyeon | Undergraduate student (Spring 2023) |  |
| Joo, Chamjin | Undergraduate student (Fall 2023) |  |
| Eun, Songji | Undergraduate student (Fall 2023) |  |
| Kang, Jeonggyu | Undergraduate student (Winter 2023) |  |
| Lee, Soyeon | Undergraduate student (Spring 2024–Summer 2024) |  |
| Suh, Soomin | Undergraduate student (Summer 2024) |  |
| Lee, Haesung | Undergraduate student (Summer 2024) |  |
| Kim, Nahye | Undergraduate student (Summer 2024–Fall 2024) |  |
| Chung, Yoonjae | Undergraduate student (Winter 2022–Spring 2024) |  |
| Kim, Seo Young | Undergraduate student (Fall 2025–Winter 2025) |  |
| Cho, Juno | Undergraduate student (Fall 2025–Winter 2025) |  |
| Ko, Sangjun | Undergraduate student (Fall 2025–Winter 2025) |  |

## 최근 논문 목록 (2021–2026)

누리집 Publication 페이지 Journal & Conference 절의 2021–2026년 논문 25편(학술지 18, 학회 7)과 Preprints 절의 사전 공개 논문 2편, 모두 27편이다. 사전 공개 논문은 동료 심사를 거쳐 출판된 논문이 아니어서 학술지 칸 뒤에 「사전 공개, 동료 심사 전」을 붙였다. 제목·저자·학술지·학회 표기는 누리집 그대로이고, 저자 이름 뒤 *는 공동 1저자, **는 공동 교신저자 표시다. 연도마다 학술지 논문, 학회 논문, 사전 공개 논문 순으로 적었다. 교수가 교신저자가 아닌 공동 연구 논문도 누리집 목록대로 실었고, 2025년 Nature Reviews Electrical Engineering 항목은 KAIST 교수들이 반도체 연구와 교육을 소개한 글이다.[^pubs]

**2026**

- E.-S. Cho\*, J. Park\*, H. Jin, Y. Chung, M. Eom, H. Shin, J.-B. Chang, J.-H. Park\*\*, Y.-G. Yoon\*\*. "Graph-based modeling of optical system enables adaptive optics on dynamic samples with self-calibration". *iScience, 2026*.
- E.-S. Cho\*, M. Eom\*, S. Zhou\*, G. Kim, S. Kim, C.-H. Kim\*\*, K. D. Piatkevich\*\*, Y.-G. Yoon\*\*. "Three-dimensional voltage imaging in live larval zebrafish brains using fully genetically encoded voltage indicator". *Scientific Reports, 2026*.
- W. La\*, S. Bae\*, J. Seo\*, H. Yu\*, J. Cho, H. Kim, H. Nam, S. Han, E. Yi, E. Kim, C. Kang, H. Shin, C. W. Song, Y.-G. Yoon\*\*, J.-B. Chang\*\*. "Abunmix enables the simple and robust multiplexed immunofluorescence imaging". *VIEW, 2026*.
- J. Yoon\*, S. Kim\*, S. Han\*, M. Eom, E.-S. Cho, F. D. Nezhad, S. Hong, E. Kim, I.-H. Park, E. Chung\*\*, K. Shin\*\*, Y.-G. Yoon\*\*, M. Choi\*\*. "Event-based optical imaging and reconstruction of in vivo neuronal and vascular dynamics". *PhotoniX, 2026*.

**2025**

- K. M. Kim\*\*, Y.-G. Yoon\*\*, S. Choi\*\*, S.-Y. Choi\*\*, S. Yoo\*\*. "Semiconductor-related research and education at KAIST". *Nature Reviews Electrical Engineering, 2025*.
- H. Kim\*, J.-G. Kim\*, J. Sim, H. Nam, I. Cho, H. Shin, J. Kwon, D.-H. Song, S. Bae, Y.-G. Yoon\*\*, T. Ku\*\*, J.-B. Chang\*\*. "Highly accurate image registration for 3D multiplexed cyclic imaging using dense labeling in expandable tissue gels". *PLOS Biology, 2025*.
- S.-H. Lee\*, T. Liang\*, G. Chandrasekaran, J. Zhang, S. S. Kim, S. Parvathi, S. W. Lee, E.-S. Cho, H.-Y. Shin, Y.-G. Yoon, J. Jo, M. A. Bae, S.-Y. Choi\*\*, M.-K. Kim\*\*. "Mutant zebrafish lacking slc25a22a show spontaneous seizures and respond to the anti-seizure medication valproic acid". *Disease Models & Mechanisms, 2025*.
- G. Kim, H. Shin, M. Eom, H. Kim, J.-B. Chang\*\*, Y.-G. Yoon\*\*. "Doubling multiplexed imaging capability via spatial expression pattern-guided protein pairing and computational unmixing". *Communications Biology, 2025*.
- J. Y. You\*, M. Eom\*, T.-I. Choi\*, E.-S. Cho, J. Choi, M. Lee, C. Shin, J. Moon, E. Kim, P. Kim\*\*, C.-H. Kim\*\*, Y.-G. Yoon\*\*. "Preserving spatial and quantitative information in unpaired biomedical image-to-image translation". *Cell Reports Methods, 2025*.
- S. Zhou\*, Q. Zhu\*, M. Eom\*, S. Fang\*, O. M. Subach, C. Ran, J. S. Alvarado, P. S. Sunkavalli, Y. Dong, Y. Wang, J. Hu, H. Zhang, Z. Wang, X. Sun, T. Yang, Y. Mu\*\*, Y.-G. Yoon\*\*, Z. V. Guo\*\*, F. V. Subach\*\*, K. D. Piatkevich\*\*. "A sensitive soma-localized red fluorescent calcium indicator for multi-modality imaging of neuronal populations in vivo". *PLOS Biology, 2025*.
- H. Jeong\*, S. Han\*, S.-O. Park, T. R. Kim, J. Bae, T. Jang, Y. Cho, S. Seo, H.-J. Jeong, S. Park, T. Park, J. Oh, J. Park, K. Koh, K.-H. Kim, D. Jeon, I. Kwon, Y.-G. Yoon\*\*, S. Choi\*\*. "Self-supervised video processing with self-calibration on an analogue computing platform based on a selector-less memristor array". *Nature Electronics, 2025*.
- J. Sim\*, C. E. Park\*, I. Cho\*, K. Min, M. Eom, S. Han, H. Jeon, E.-S. Cho, Y. Lee, Y. H. Yun, S. Lee, D.-H. Cheon, J. Kim, M. Kim, H.-J. Cho, J.-W. Park, A. Kumar, Y. Chong, J. S. Kang, K. D. Piatkevich, E. E. Jung, D.-S. Kang, S.-K. Kwon, J. Kim, K.-J. Yoon, J.-S. Lee, C.-H. Kim, M. Choi, J. W. Kim, M.-R. Song, H. J. Choi, E. S. Boyden, Y.-G. Yoon\*\*, J.-B. Chang\*\*. "Nanoscale resolution imaging of whole mouse embryos using expansion microscopy". *ACS Nano, 2025*.
- H. Choo, F. Bu, H. Hwang, Y.-G. Yoon, K. Shin. "HyperSearch: prediction of new hyperedges through unconstrained yet efficient search". *IEEE International Conference on Data Mining (ICDM), 2025*.
- H. Yu\*, S. Han\*, Y.-G. Yoon. "Design principles of multi-scale J-invariant networks for self-supervised image denoising". *IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), 2025 (selected for oral presentation)*.
- H. Choo, M. Eom, G. Kim, Y.-G. Yoon, K. Shin. "RASP: robust mining of frequent temporal sequential patterns under temporal variations". *International Conference on Extending Database Technology (EDBT), 2025*.
- H. Zhang\*, S. Zhou\*, T. P. Kuzmicheva, O. M. Subach, C. Grimm, M. Eom, S. B.-Sebban, Y. Adam, Y.-G. Yoon, V. Emilliani, F. V. Subach\*\*, K. D. Piatkevich\*\*. "Bright and Photostable Voltage Sensors Derived from mBaoJin". *bioRxiv, 2025 (사전 공개, 동료 심사 전)*.

**2024**

- S. Han, J. Y. You, M. Eom, S. Ahn, E.-S. Cho, Y.-G. Yoon. "From pixels to information: artificial intelligence in fluorescence microscopy". *Advanced Photonics Research, 2024*.
- G. T. Franzesi\*, I. Gupta\*, M. Hu, K. Piatkevich, M. Yildirim, J.-P. Zhao, M. Eom, S. Han, D. Park, H. Andaraarachchi, Z. Li, J. Greenhagen, A. M. Islam, P. Vashishtha, Z. Yaqoob, N. Pak, A. D Wissner-Gross, D. A. Martin-Alarcon, J. J. Veinot, P. T. C. So, U. Kortshagen, Y.-G. Yoon, M. Sur\*\*, E. S. Boyden\*\*. "In Vivo Optical Clearing of Mammalian Brain". *bioRxiv, 2024 (사전 공개, 동료 심사 전)*.

**2023**

- M. Eom\*, S. Han\*, P. Park\*, G. Kim, E.-S. Cho, J. Sim, K.-H. Lee, S. Kim, H. Tian, U. L. Böhm, E. Lowet, H. Tseng, J. Choi, S. E. Lucia, S. H. Ryu, M. Rózsa, S. Chang, P. Kim, X. Han, K. D. Piatkevich, M. Choi, C.-H. Kim, A. E. Cohen, J.-B. Chang, Y.-G. Yoon. "Statistically unbiased prediction enables accurate denoising of voltage imaging data". *Nature Methods, 2023*.
- E.-S. Cho, S. Han, G. Kim, M. Eom, K.-H. Lee, C.-H. Kim, Y.-G. Yoon. "In vivo whole-brain imaging of zebrafish larvae using three-dimensional fluorescence microscopy". *Journal of Visualized Experiments (JoVE), 2023*.
- J. Cho\*, S. Han\*, E.-S. Cho, K. Shin, Y.-G. Yoon. "Robust and efficient alignment of calcium imaging data through simultaneous low rank and sparse decomposition". *IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), 2023*.

**2022**

- C. Shin\*, H. Ryu\*, E.-S. Cho, S. Han, K.-H. Lee, C.-H. Kim, Y.-G. Yoon. "Three-dimensional fluorescence microscopy through virtual refocusing using a recursive light propagation network". *Medical Image Analysis, 2022*.
- J. Seo\*, Y. Sim\*, J. W. Kim\*, H. Kim, I. Cho, H. Nam, Y.-G. Yoon\*\*, J.-B. Chang\*\*. "PICASSO allows ultra-multiplexed fluorescence imaging of spatially overlapping proteins without reference spectra measurements". *Nature Communications, 2022*.
- J. Cho, D.-H. Lee, Y.-G. Yoon. "Inducing functions through reinforcement learning without task specification". *Neural Information Processing Systems Workshop (NeurIPS Workshop) on Deep Reinforcement Learning, 2022*.

**2021**

- E.-S. Cho\*, S. Han\*, K.-H. Lee, C.-H. Kim, Y.-G. Yoon. "3DM: Deep decomposition and deconvolution microscopy for rapid neural activity imaging". *Optics Express, 2021. (highlighted as Editors' Pick, featured as Image of the Week on the main webpage of Optica publishing group)*.
- S. Han, E.-S. Cho, I. Park, K. Shin, Y.-G. Yoon. "Efficient neural network approximation of robust PCA for automated analysis of calcium imaging data". *International Conference on Medical Image Computing and Computer Assisted Intervention (MICCAI), 2021*.
- C. Shin\*, H. Ryu\*, E.-S. Cho, Y.-G. Yoon. "RLP-Net: A recursive light propagation network for 3-D virtual refocusing". *International Conference on Medical Image Computing and Computer Assisted Intervention (MICCAI), 2021. (selected for MICCAI Young Scientist Award, MICCAI Student Travel Award, and oral presentation)*.

## 소식

누리집 첫 화면 News & Notice 가운데 2021년 10월 13일 이후 글 22건(2021-12-13–2026-04-28)이다. 날짜와 문장은 게시된 그대로다.[^home]

- 2026-04-28 · Prof. Yoon received the 2025 KAIST Top 10 Research Achievements Award.
- 2026-03-30 · Dr. Han received the 2026 Outstanding Dissertation Award.
- 2026-03-16 · Dr. Han was selected as a recipient of the Jang Young Sil Fellowship.
- 2026-02-28 · Dr. Han was selected as a recipient of the Sejong Science Fellowship.
- 2025-10-31 · Dr. Cho and Joon won the Best Poster Award at SPIE Advanced Biophotonics Conference (ABC) 2025.
- 2025-08-18 · Nature Reviews Electrical Engineering: Semiconductor-related research and education at KAIST
- 2025-04-01 · Prof. Yoon was selected as a recipient of 2025 Human Frontier Science Program (HFSP) Award.
- 2025-03-06 · Our work on self-calibrating analog neuromorphic computing was highlighted as one of the Breakthrough achievements of KAIST.
- 2025-02-27 · Our work on self-calibrating analog neuromorphic computing was highlighted in Editorial section of Nature Electronics.
- 2025-02-11 · Our work on self-calibrating analog neuromorphic computing was featured in News & Views section of Nature Electronics.
- 2025-01-08 · Nature Electronics: Analog neuromorphic computing with self-calibration (Jeong\*, Han\* et al)
- 2024-02-26 · SUPPORT was highlighted as one of the Breakthrough achievements of KAIST.
- 2023-12-22 · Our multiplexed imaging technique, PICASSO, was covered by Nature Portfolio.
- 2023-11-13 · Seungjae Han received Trainee Professional Development Award (TPDA) and AKN Outstanding Research Award at SfN Neuroscience 2023.
- 2023-10-09 · SUPPORT (Eom\*, Han\*, Park\* et al) made the cover of Oct. 2023 issue of Nature Methods.
- 2023-09-19 · Nature Methods: SUPPORT (Eom\*, Han\*, Park\* et al) takes voltage imaging to the next level through self-supervised learning
- 2023-09-19 · Prof. Young-Gyu Yoon posted our story behind the development of SUPPORT on Nature Communities.
- 2022-08-29 · PICASSO was highlighted as one of the Breakthrough achievements of KAIST.
- 2022-06-16 · Our multiplexed imaging method, PICASSO, was covered by Nature Communications.
- 2022-05-31 · Changyeop and Hyun's work on virtual refocusing, RLP-Net, was selected as one of KAIST's research highlights of 2021.
- 2022-05-05 · Nature Communications: PICASSO (Seo\*, Sim\*, Kim\* et al) enables ultra-multiplexed imaging through blind source separation
- 2021-12-13 · Prof. Young-Gyu Yoon's EIRIC interview is available online.

## 연락과 위치

- 주소: Building N24, Room #4103-1, School of Electrical Engineering, KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea[^home]
- 교수 연구실: LG이노베이션홀(N24) 4103-1호[^eeprof][^ssel]
- 전화: 042-350-7449 (교수)[^ssep]
- 교수 이메일: ygyoon@kaist.ac.kr[^eeprof]
- 첫 화면 Joining our group은 대학원생·학부생·박사후연구원 지원자가 성적표와, 배경 지식·관심·기술을 적은 CV를 교수에게 이메일로 보내고, 연락하기 전에 Research 탭의 유튜브 영상 두 편을 보라고 안내한다.[^home]
[^p1]: E.-S. Cho 외, Y.-G. Yoon, Optics Express 29, 32700 (온라인 2021-09-24). <https://doi.org/10.1364/oe.439619> 초록 기준.
[^p2]: E.-S. Cho 외, Y.-G. Yoon, Scientific Reports 16, 27491 (온라인 2026-06-16). <https://doi.org/10.1038/s41598-026-58107-8> 초록 기준.
[^p3]: M. Eom 외, Y.-G. Yoon, Nature Methods 20, 1581-1592 (온라인 2023-09-18). <https://doi.org/10.1038/s41592-023-02005-8> 초록 기준.
[^p4]: E.-S. Cho 외, Y.-G. Yoon, iScience 29, 116769 (2026). <https://doi.org/10.1016/j.isci.2026.116769> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. Seo 외, J.-B. Chang, Nature Communications 13, 2475 (온라인 2022-05-05). <https://doi.org/10.1038/s41467-022-30168-z> 초록 기준.
[^p6]: G. Kim 외, Y.-G. Yoon, Communications Biology 8, 928 (온라인 2025-06-14). <https://doi.org/10.1038/s42003-025-08357-5> 초록 기준.
[^p7]: H. Jeong 외, S. Choi, Nature Electronics (온라인 2025-01-08). <https://doi.org/10.1038/s41928-024-01318-6> 초록 기준(출판사 논문 페이지).
[^p8]: J. Y. You 외, Y.-G. Yoon, Cell Reports Methods 5, 101074 (2025). <https://doi.org/10.1016/j.crmeth.2025.101074> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 뇌 계측 및 컴퓨팅 연구실 누리집 첫 화면 <https://nica.kaist.ac.kr/> (소개문, News & Notice, Contact, 2026-10-23 열람)
[^people]: 뇌 계측 및 컴퓨팅 연구실 누리집 People 페이지 <https://nica.kaist.ac.kr/people> (Principal Investigator, Postdoctoral researcher, Graduate students, Undergraduate students, Alumni, 2026-10-23 열람)
[^research]: 뇌 계측 및 컴퓨팅 연구실 누리집 Research 페이지 <https://nica.kaist.ac.kr/research> (세 묶음 일곱 주제와 주제별 논문, 2026-10-23 열람)
[^pubs]: 뇌 계측 및 컴퓨팅 연구실 누리집 Publication 페이지 <https://nica.kaist.ac.kr/publication> (Preprints, Journal & Conference, KAIST 부임 전 Journal·Conference, 목록 범위는 근거 페이지, 2026-10-23 열람)
[^eeprof]: KAIST 전기및전자공학부 교수 소개(윤영규) <https://ee.kaist.ac.kr/professor/16230/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 디비전, 2026-10-23 열람)
[^ssel]: KAIST 반도체시스템공학과 연구실 목록 <https://sse.kaist.ac.kr/research-laboratory/> (뇌 계측 및 컴퓨팅 연구실 항목, 2026-10-23 열람)
[^ssep]: KAIST 반도체시스템공학과 교수진 <https://sse.kaist.ac.kr/professor/> (윤영규 교수 항목, 2026-10-23 열람)

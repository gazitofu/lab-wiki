# 방사선계측 및 의료영상센서 연구실 (Radiation Detection and Medical Image Sensor Laboratory)

**KAIST 원자력및양자공학과 · 조규성 교수**

- 분야: 섬광 검출기와 반도체 검출기를 쓰는 방사선 계측, 검출기 스펙트럼에서 바로 구하는 방사선량 평가, 감마선 분광 분석과 방사성 핵종 판별·정량, 인공신경망과 기계학습을 쓴 스펙트럼·신호 해석, 중성자·감마선 펄스 파형 판별, 방사성 폐기물과 원자력 시설 해체 관련 측정, 표적 알파 치료용 CZT 선량 교정기와 컴프턴 카메라, 해양·환경 방사선 감시, 고스트 영상
- 대분야: 물리·양자, 전기전자·반도체·광학
- 태그: 과학·공학 AI[^p2][^p4], 방사선 검출·계측[^p1], 의료 영상 기기·재구성[^p6]
- 홈페이지: 학과 교수 소개 페이지 <https://nuclear.kaist.ac.kr/people/professor.php>
- 근거와 출처: [방사선계측 및 의료영상센서 연구실 근거 페이지](radiation-sources.md)

> 원자력및양자공학과 「방사선」 연구그룹에 속한 방사선 계측 연구실이다.[^deptlab] 2021–2026년 대표 논문은 섬광 검출기 스펙트럼으로 중성자 선량을 실시간 추정하는 방법, 기계학습으로 중성자 신호를 가려내는 알고리즘, 방사성 폐기물 감마선 분광의 보정과 인공신경망 감마선 분광, 표적 알파 치료용 CZT 선량 교정기와 컴프턴 카메라, 선박용 실시간 감마선 측정 장치, 고스트 영상의 잡음 제거를 다룬다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 무엇을 연구하나

연구실은 KAIST 원자력및양자공학과 조규성 교수의 연구실이다. 학과 연구그룹 페이지는 「방사선」 그룹 아래 이 연구실을 「방사선계측 및 의료영상센서 연구실」로 적고,[^deptlab] 영문 연구그룹 페이지는 Medical Radiation 분야에 Radiation Detection and Medical Image Sensor Laboratory로 적는다.[^deptlaben] 학과 교수 소개는 조규성 교수를 교수로 적는다.[^dept]

교수가 저자로 참여한 2021–2026년 논문은 Nuclear Engineering and Technology, Radiation Physics and Chemistry, Nuclear Instruments and Methods in Physics Research Section A, Applied Radiation and Isotopes, IEEE Transactions on Nuclear Science 같은 방사선 계측·원자력 학술지의 논문과, IEEE Nuclear Science Symposium·Medical Imaging Conference와 SPIE Medical Imaging의 학회 발표 논문이 중심이다.[^cr] 제목으로 보면 주제는 다섯 갈래다. 첫째는 섬광체(방사선을 받으면 빛을 내는 물질)로 만든 검출기의 스펙트럼을 선량으로 바꾸는 방사선량 평가다. 둘째는 감마선 분광(감마선의 에너지 분포인 스펙트럼을 재고 분석하는 측정) 자료를 인공신경망, 희소 표현, 베이지안 추론, 몬테카를로 모사(무작위 표본 추출을 되풀이해 수치 결과를 얻는 계산 방법)로 해석하는 연구이며, 방사성 폐기물, 원자력 시설 해체, 우라늄 폐기물의 측정을 다룬다. 셋째는 중성자와 감마선 신호를 가려내는 펄스 파형 판별과 실리콘 광증배관(SiPM) 판독 같은 검출기 신호 처리다. 넷째는 표적 알파 치료용 CZT 검출기와 컴프턴 카메라, 치과용 콘빔 CT 같은 의료 방사선 연구이고, 다섯째는 라돈·토론 측정, 선박용 감마선 측정, 수중 퇴적물 오염 탐사 같은 환경 방사선 감시와 고스트 영상이다.[^cr]

대표 논문으로 보면, 연구실은 유기 섬광 검출기의 펄스 높이 스펙트럼을 스펙트럼 가중 함수로 바로 선량으로 바꾸고,[^p1] 다채널 플라스틱 섬광체의 중성자 신호를 비지도 학습과 지도 학습을 합친 알고리즘으로 자동 분류했다.[^p2] 방사성 폐기물 감마선 분광의 자기 흡수 보정 인자를 몬테카를로 계산으로 구하고,[^p3] 인공신경망 감마선 분광에서 필요한 계수 시간을 실제 스펙트럼 없이 정하는 방법을 제안했다.[^p4] 표적 알파 치료에 쓰는 ²²⁵Ac의 낮은 방사능을 재는 CZT 선량 교정기를 설계하고,[^p5] CZT 컴프턴 카메라의 한 층·두 층 구성을 비교했다.[^p6] 선박에 싣는 실시간 감마선 측정 장치를 만들어 현장 시험을 했고,[^p7] 고스트 영상의 화질을 높이는 베이지안 잡음 제거법도 제안했다.[^p8]

## 주요 연구 주제

### 1. 섬광 검출기 스펙트럼으로 재는 방사선량과 중성자 신호 판별

대표 논문 1은 원자력 시설과 의료 환경처럼 중성자와 감마선이 섞인 방사선장에서 방사선 방호에 쓰는 주변 선량당량 H\*(10)(방사선 방호에서 어떤 위치의 방사선량을 나타내도록 정한 측정량)을 유기 섬광 검출기로 실시간 추정하는 틀을 제안했다. ²⁵²Cf 선원을 쓴 비행시간 측정으로 중성자 응답 행렬을 실험으로 얻고, 이 응답으로 펄스 높이 스펙트럼을 펼침(unfolding) 과정 없이 H\*(10)으로 바로 바꾸는 스펙트럼 가중 함수 G(E)를 구했다. 3–150 μSv/h 선량률 범위에서 강한 선형성을 보였고 상대 오차는 약 5% 이내였다.[^p1]
대표 논문 2는 고속 중성자 투과 영상을 얻으려고, 실리콘 광증배관을 붙인 다채널 유기 플라스틱 섬광체의 펄스 파형 판별 결과에서 중성자 신호를 자동으로 분류하는 기계학습 알고리즘을 제안했다. 1.7 MeVee보다 큰 영역은 비지도 학습으로, 그보다 작은 영역은 앞 영역의 자료 분포 특징을 이용한 지도 학습으로 나눠 분류했고, 비행시간 측정으로 얻은 신호에서 수신자 조작 특성 곡선 아래 면적(AUC) 0.9904를 보였다.[^p2]
논문 목록에는 위치 민감형 검출기의 화소를 묶은 G(E) 함수로 선원 분포를 모를 때 선량률을 추정한 논문(2023), 플라스틱 섬광 검출기의 주변 선량당량률 추정(2023)과 딥러닝 스펙트럼–선량 예측(2022), 겹친(pile-up) 중성자·감마선 신호의 펄스 높이 추정과 펄스 파형 판별(2023), SiPM 기반 디지털 중성자·감마선 펄스 파형 판별의 운전 조건 연구(2024)도 있다.[^cr]

### 2. 감마선 분광 분석과 방사성 폐기물 측정

대표 논문 3은 방사성 폐기물의 감마선 분광에서 교정 기준인 인증 표준물질과 폐기물 시료의 재질·밀도 차이 때문에 생기는 자기 흡수 효과를 보정하려고, MCNP6.2(몬테카를로 방법으로 방사선 수송을 계산하는 코드)로 자기 흡수 보정 인자를 구하는 방법을 제시했다. 고순도 저마늄(HPGe) 검출기 세 대의 모형을 실험과 맞춰 다듬은 뒤 밀도 0.1–8.0 g/cm³ 범위의 보정 인자를 계산하고, 가연성·불연성·금속 폐기물별로 비교했으며, 콘크리트 기반 표준물질로 방법을 실험으로 확인했다.[^p3]
대표 논문 4는 NaI(Tl) 섬광 검출기의 인공신경망 감마선 분광에서, 여섯 방사성 동위원소의 기준 스펙트럼으로 만든 가상 스펙트럼을 써서 실제 스펙트럼을 재지 않고 최적 계수 시간을 정하는 방법을 제안했다. 각 최적 계수 시간까지 잰 실제 스펙트럼에서 정확도가 크게 좋아졌다.[^p4]
논문 목록에는 다중 작업 학습으로 플라스틱 섬광 검출기에서 유사 감마선 분광(pseudo-gamma spectroscopy)을 한 논문(2021), 설명 가능한 인공지능을 쓴 우라늄 농축도 측정 신경망(2021), 사전(dictionary) 학습 기반 희소 표현을 쓴 환경 방사선 감시용 핵종 판별(2022), 폐기물 드럼 속 고르지 않게 분포한 우라늄 방사능의 베이지안 정량(2023), 원자력 시설 해체에서의 방사성 동위원소 판별(2024), 현장 적용을 위해 여러 변수를 고려한 딥러닝 감마선 분광 분석(2025)과 고방사선장용 딥러닝 감마선 분광 분석 시스템(2026)도 있다.[^cr] 방사성 폐액 측정의 최소 검출 방사능 추론(2024), CeBr₃·LaBr₃(Ce)·NaI(Tl) 섬광 검출기로 방사성 폐액 특성을 비교한 논문(2025), 베이지안 방법으로 방사성 폐액 측정의 주변 선량당량을 추정한 논문(2026)도 있다.[^cr]

### 3. 의료 방사선 계측과 영상

대표 논문 5는 표적 알파 치료에 쓰는 ²²⁵Ac의 낮은 방사능을 정확히 재려고, 몬테카를로 모사 도구 GATE로 CZT 기반 미세 방사능 선량 교정기를 설계했다. 표준 선량 교정기인 고압 기체 전리함은 이 범위에서 감도가 낮고 에너지를 구별하지 못한다는 점을 들어, 상자 모양 우물 구조와 시간 일치 화소 단위 묶음을 쓰는 교정기를 설계했고, 모사에서 NaI(Tl) 우물형 계수기와 비교했다.[^p5]
대표 논문 6은 ²²⁵Ac 영상을 위해 CZT 검출기 기반 3차원 위치 측정 컴프턴 카메라를 두 층으로 고쳐 한 층·두 층 구성의 감도와 각 분해능을 측정·비교했다. 두 층 구성은 각 분해능을 개선했고, 감도는 한 층 구성이 높았다.[^p6]
논문 목록에는 콘빔 CT 영상의 자기 지도 학습 잡음 제거(2023)와 오프셋 검출기를 쓰는 치과용 콘빔 CT의 HU 값 비대칭(2024)을 다룬 학회 발표 논문도 있다.[^cr]

### 4. 환경 방사선 감시와 영상 복원

대표 논문 7은 해양 방사선을 감시하려고 선박에서 쓰는 이동형 실시간 감마선 측정 시스템을 만들었다. 배 안에 설치한 용기로 엔진이나 발전기 냉각수를 재며, 60초 측정에서 최소 검출 방사능은 약 0.8 Bq/L이고, 실시간 자료 전송과 원격 제어가 된다.[^p7]
대표 논문 8은 고스트 영상의 품질을 높이는 베이지안 잡음 제거 방법을 제안했고, 실험에서 재구성한 영상의 PSNR과 SSIM이 3000번 측정한 기존 고스트 영상의 값보다 높았다.[^p8]
논문 목록에는 직렬로 이은 전리함 두 개 사이의 공기 흐름 지연으로 라돈과 토론을 실시간으로 구별해 재는 방법(2022)과 같은 공기에서 토론과 라돈을 따로 검출하는 방법(2024), 수중 방사능 오염 퇴적물의 탐사 측정 보정법(2021), 펜슬 빔 주사 방식 후방 산란 X선 검출 시스템(2024), 심층 신경망 제약을 둔 X선 고스트 영상 재구성(2024)도 있다.[^cr]

## 대표 논문

2021–2026년 논문 가운데 논문 기록에 교수 소속이 KAIST로 적혀 있고 초록을 확인할 수 있는 여덟 편을 연구 갈래별로 골랐다.[^cr][^oa] 일곱 편은 교수가 마지막 저자이고, 6번은 교수가 중간 저자로 참여한 공동 연구다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Real-time ambient neutron dosimetry based on TOF-derived response and G(E) convolution](https://doi.org/10.1038/s41598-026-69119-9) · Scientific Reports | 원자력 시설과 의료 환경의 복잡한 혼합 방사선장에서 방사선 방호를 하려면 중성자와 감마선 모두의 주변 선량당량 H\*(10)을 정확히 평가해야 한다. 중성자는 생물학적 효과가 크고 에너지 의존성이 강해, 믿을 만한 선량 측정에는 스펙트럼을 정밀하게 재는 일이 중요하다. 기존 선량 측정 방법은 실시간 감시 능력, 스펙트럼 민감도, 실제 배치 가능성 사이의 맞바꿈에서 오는 한계가 있었다. 연구진은 유기 섬광 검출기로 H\*(10)을 실시간으로 동시에 추정하는 스펙트럼 기반 선량 측정 틀을 제안했다. ²⁵²Cf 선원을 쓴 비행시간 측정으로 중성자 응답 행렬을 실험으로 얻고, 기준 핵분열 와트(Watt) 스펙트럼으로 검증했다. 이 응답을 바탕으로 펄스 높이 스펙트럼을 기존 펼침 과정 없이 H\*(10)으로 바로 바꾸는 스펙트럼 가중 함수 G(E)를 얻었다. G(E)는 최소제곱 최소화와 적응 모멘트 추정(Adam) 최적화로 맞췄고, 각각 최적 차수 k_max = 6과 k_max = 22에서 평균 절대 백분율 오차가 가장 작았다. 이 틀은 3–150 μSv/h 선량률 범위에서 강한 선형성을 보였고, 상대 오차는 약 5% 이내, 평균 절대 백분율 오차의 최솟값은 2.36%였다. 연구진은 실험으로 얻은 응답 함수가 안정적인 실시간 중성자 선량 추정을 가능하게 해, 모사에 기대는 방법의 실용적 대안이 된다고 적었다.[^p1] | 1저자 Gyohyeok Song, 마지막 저자 Gyuseong Cho(조규성 교수) (5명) |
| 2 | 2025 | [Automatic classification of multi-channel PSD results combining unsupervised and supervised learning](https://doi.org/10.1016/j.net.2024.11.033) · Nuclear Engineering and Technology 57 | 고속 중성자 투과 영상(고속 중성자를 물체에 통과시켜 내부를 보는 영상)은 국토 안보(homeland security) 같은 여러 분야에서 쓰는 비파괴 검사 기법이다. 고속 중성자는 감속재를 둔 열중성자 포획 검출 방식이나, 되튐 양성자(중성자와 부딪혀 튕겨 나간 양성자)를 이용하는 중성자 산란 검출 방식으로 잴 수 있고, 투과 영상에는 되튐 양성자 방식이 더 알맞다. 연구진은 실리콘 광증배관을 붙인 다채널 유기 플라스틱 섬광체에서 얻은 중성자 신호를 영상 획득용으로 자동 분류하는 기계학습 알고리즘을 제안했다. 이 알고리즘은 펄스 파형 판별 결과 가운데 펄스 높이 문턱값 150 keVee(keVee는 같은 양의 빛을 내는 전자의 에너지로 나타낸 단위) 위의 전체 에너지 범위를 다룬다. 결과를 1.7 MeVee보다 큰 비지도 학습 영역과 1.7 MeVee보다 작은 지도 학습 영역으로 나누고, 비지도 학습 영역 자료 분포의 특징을 이용해 지도 학습 영역의 중성자 신호를 효과적으로 분류했다. 비행시간 측정으로 얻은 중성자·감마선 신호에 적용한 결과, 수신자 조작 특성 곡선 아래 면적(분류기가 두 부류를 가려내는 정도를 나타내는 지표) 0.9904의 분류 성능을 보였다.[^p2] | 1저자 Gyohyeok Song, 마지막 저자 Gyuseong Cho(조규성 교수) (7명) |
| 3 | 2026 | [Estimation of self-absorption correction factors for gamma-ray spectrometry of radioactive waste using MCNP](https://doi.org/10.1016/j.net.2025.104064) · Nuclear Engineering and Technology 58 | 감마선 분광은 방사성 폐기물의 방사능 특성을 평가하는 데 알맞은 기법이다. 하지만 교정 기준으로 쓰는 인증 표준물질(CRM)과 폐기물 시료는 재질과 밀도가 달라 자기 흡수(시료가 낸 방사선을 시료 자신이 흡수하는 현상) 효과가 생기므로 보정이 필요하다. 연구진은 MCNP6.2로 자기 흡수 보정 인자를 구하는 실용적 방법을 제시했다. 검출기와 측정 배치를 MCNP6.2 안에 자세히 모형화하고 실험 결과와 비교해 최적화했으며, 모형 정확도를 높이려고 세 가지 CRM 형상을 썼다. 고순도 저마늄 검출기 세 대에 대해 59.54–1836.05 keV 에너지 범위에서 모사를 다듬어, 모사와 측정의 전에너지 피크 효율(FEPE, 선원이 낸 광자 가운데 에너지를 모두 검출기에 남겨 전에너지 피크에 들어간 비율) 차이를 평균 1.9 ± 2.16%, 최대 4.9 ± 1.9%로 맞췄다. 최적화한 입력으로 밀도 0.1–8.0 g/cm³ 범위의 자기 흡수 보정 인자를 계산하고, 특정 형상에 대한 유효 경로 길이 식을 구했다. 같은 밀도 범위에서 가연성·불연성·금속 폐기물의 자기 흡수 효과를 평가해 재질별 보정 인자를 비교했고, 콘크리트 기반 CRM으로 방법의 타당성을 실험으로 확인했다. 연구진은 이 결과가 방사성 폐기물 관리의 시료 채취와 방사능 농도 분석의 정확도와 효율을 높일 것이라고 적었다.[^p3] | 1저자 Kyungmin Kim, 마지막 저자 Gyuseong Cho(조규성 교수) (7명) |
| 4 | 2024 | [A counting-time optimization method for artificial neural network (ANN) based gamma-ray spectroscopy](https://doi.org/10.1016/j.net.2024.02.029) · Nuclear Engineering and Technology 56 | 기계학습 기술이 발전하면서 인공신경망은 NaI(Tl) 섬광 검출기(탈륨을 첨가한 요오드화 나트륨 결정을 섬광체로 쓰는 검출기) 기반 감마선 분광의 성능을 높이는 데 널리 쓰인다. 보통 신경망 성능은 실제 스펙트럼으로 만든 시험 자료로 평가하지만, 여러 상황을 대표하는 실제 스펙트럼을 폭넓게 모으는 일은 비효율적이고 시간이 많이 든다. 연구진은 실제 스펙트럼을 재는 대신 ⁵⁴Mn, ⁵⁷Co, ⁶⁰Co, ¹³⁴Cs, ¹³⁷Cs, ²⁴¹Am 여섯 방사성 동위원소의 기준 스펙트럼에서 얻은 범주형 분포 함수로 표본을 뽑아, 스펙트럼 특징이 다양한 가상 스펙트럼을 만들었다. 실제 적용을 위해, 신경망 학습에 쓴 합성 스펙트럼과 가상 스펙트럼 사이 쿨백–라이블러 발산(두 확률 분포가 서로 다른 정도를 재는 척도) 값의 변화가 0에 가까워지는 지점을 최적 계수 시간(OCT)으로 정했다. 각 OCT까지 잰 실제 스펙트럼에서는 정확도가 크게 좋아졌다. 연구진은 이 방법으로 실제 스펙트럼을 재지 않고도 인공신경망 기반 감마선 분광의 OCT를 정할 수 있다고 적었다.[^p4] | 1저자 Moonhyung Cho, 마지막 저자 Gyuseong Cho(조규성 교수) (6명) |
| 5 | 2025 | [Design and evaluation of CZT-based micro-activity dose calibrator for TAT application using Monte Carlo simulation](https://doi.org/10.1088/1748-0221/20/12/c12021) · Journal of Instrumentation 20 | 표적 알파 치료(TAT)에 쓰는 ²²⁵Ac의 낮은 방사능을 정확히 재려고, 몬테카를로 모사 도구 GATE로 새 CZT 기반 미세 방사능 선량 교정기를 설계했다. TAT에서는 작은 과다 투여도 심한 국소 독성을 일으킬 수 있어 마이크로퀴리에서 나노퀴리(퀴리는 방사능의 단위) 수준의 방사능이 자주 필요하고, 안전하고 효과적인 치료에는 선량 교정기로 방사능을 정확히 재는 일이 먼저다. 표준 선량 교정기인 고압 기체 전리함은 감도가 낮고 에너지를 구별하지 못해 이 범위에 알맞지 않다. 연구진이 설계한 교정기는 입체각을 넓게 덮는 상자 모양 우물 구조를 쓰고, 여러 곳에서 일어난 컴프턴 산란 때문에 잃던 전에너지 피크 순계수를 시간 일치 화소 단위 묶음으로 되찾는다. GATE로 1.0 μCi에서 10⁻⁶ μCi까지 연속 희석한 시료를 모사하고, 218 keV와 440 keV 감마선 피크에서 방사능을 재구성해, 표준 선량 교정기의 대안으로 쓰이는 NaI(Tl) 우물형 계수기와 성능을 비교했다. 이 100만 배 범위에서 CZT 교정기는 기울기 m = 0.9934의 1에 가까운 선형성과 백분율 수준의 편향을 보였고, 같은 조건에서 NaI(Tl) 계수기는 계통적으로 낮게 응답했다. 연구진은 CZT 방식이 TAT의 낮은 방사능을 정확히 정량할 수 있음을 보여, 이어질 하드웨어 검증의 근거가 된다고 적었다.[^p5] | 1저자 Seoyun Jang, 마지막 저자 Gyuseong Cho(조규성 교수) (5명) |
| 6 | 2026 | [Performance Evaluation of Single- and Double-Layer CZT Compton Cameras for 225 Ac Imaging](https://doi.org/10.1109/tns.2026.3663840) · IEEE Transactions on Nuclear Science 73 | CZT 검출기 기반 3차원 위치 측정 컴프턴 카메라를 ²²⁵Ac 영상 용도로 평가했다. 알파 입자를 내는 방사성 핵종 ²²⁵Ac은 암의 표적 알파 치료에 쓸 가능성이 크고, 붕괴 사슬에서 ²¹³Bi가 내는 440 keV 감마선으로 컴프턴 영상을 얻을 수 있다. TAT 방사성 의약품, 특히 ²²⁵Ac 기반 의약품은 주입 방사능이 매우 낮아 감마선을 높은 감도로 재는 능력이 중요하고, 컴프턴 카메라는 조준기(collimator, 정해진 방향의 방사선만 통과시키는 장치)를 쓰는 카메라보다 높은 감도를 낼 수 있다. 방사성 의약품의 위치를 정확히 찾을 공간 분해능을 얻으려면 컴프턴 카메라의 각 분해능이 정밀해야 한다. 연구진은 GDS-100 CZT 카메라(IDEAS)를 CZT 결정 두 층으로 고쳐 한 층과 두 층 컴프턴 영상을 비교했고, ²²⁵Ac 영상의 핵심 성능 지표인 감도와 각 분해능을 쟀다. 비교를 위해 662 keV 감마선을 내는 ¹³⁷Cs 선원으로 더 높은 에너지에서도 카메라 특성을 쟀다. 3차원 위치 측정을 위해 상호작용 깊이(DOI)와 무게중심 방법을 최적화한 뒤 3차원 복셀 단위 에너지 교정을 했다. 두 층 구성은 각 분해능 척도(ARM)를 ¹³⁷Cs(662 keV)에서 14.0°에서 4.3°로, ²²⁵Ac(440 keV)에서 15.8°에서 8.9°로 개선했다. 반면 감도는 한 층 구성이 두 층 구성보다 약 40배 높았고, 초록은 그 이유를 작은 크기와 산란층에서 산란된 광자의 흡수로 든다. 연구진은 검출기 면적을 늘린 더 큰 두 층 컴프턴 카메라가 같은 수준의 감도에 훨씬 나은 각 분해능을 낼 것으로 기대한다.[^p6] | 1저자 Gyohyeok Song, 마지막 저자 Javier Caravaca (5명), 조규성 교수는 4번째 저자 |
| 7 | 2023 | [Development of a real-time mobile gamma-ray measurement system for shipboard use](https://doi.org/10.1016/j.net.2023.07.026) · Nuclear Engineering and Technology 55 | 해양 환경에서 방사선을 감시하려면 넓은 지역을 빠르게 살펴야 한다. 연구진은 이를 위해 선박에서 쓰는 이동형 실시간 감마선 측정 시스템을 만들고 성능을 평가했다. 시스템은 배 안에 용기(canister)를 설치해 엔진이나 발전기 냉각수를 재도록 만들었다. 60초 측정에서 시스템의 최소 검출 방사능은 약 0.8 Bq/L이고, 실시간 자료 전송과 원격 제어가 된다. 시스템은 현장 시험을 거쳤고, 초록은 운항 중인 선박에 설치되어 운용되고 있다고 적는다. 연구진은 이런 선박 기반 실시간 감마선 측정 시스템이 여러 해양 방사선 감시 용도에 알맞고 빠르게 배치될 것으로 기대한다고 적었다.[^p7] | 1저자 Chang-Jong Kim, 마지막 저자 Gyu-Seong Cho(조규성 교수) (6명) |
| 8 | 2021 | [Ghost imaging with Bayesian denoising method](https://doi.org/10.1364/oe.438478) · Optics Express 29 | 고스트 영상의 품질을 높이는 베이지안 잡음 제거 방법을 제안했다. 이 방법은 이진 대상과 회색조 대상 모두에서 더 적은 측정으로 가장 높은 PSNR(최대 신호 대 잡음비)과 SSIM(구조 유사도 지수)을 얻었다. 실험에서 USAF 표적을 재구성한 영상의 PSNR과 SSIM은 최대 12.80 dB와 0.77이었고, 3000번 측정한 기존 고스트 영상은 7.24 dB와 0.28이었다. 더해진 가우스 잡음에도 강건했다. 연구진은 이 방법이 고스트 영상 기술을 실제 응용에 더 쓸 만하게 만들 수 있다고 적었다.[^p8] | 1저자 Junhyeok Kim, 마지막 저자 Gyuseong Cho(조규성 교수) (6명) |

## 교수와 전문 분야

조규성 교수(Cho, Gyuseong)는 KAIST 원자력및양자공학과 교수다.[^dept][^depten] 학과 교수 소개는 최종학위를 Ph.D. (1992) UC Berkeley로 적고, 교수 상세 창은 연구 분야(Research Field)를 「방사선 계측 및 의료영상기기」로 적는다.[^dept][^deptdetail]

교수 상세 창에 따르면 서울대학교 공과대학 원자핵공학에서 학사(1983)와 석사(1985)를, UC Berkeley 원자핵공학에서 박사(1992)를 받았다.[^deptdetail] 이어 미국 로렌스 버클리 연구소 박사후과정(1992-1993)과 미국 로스알라모스 연구소 박사후과정(1993-1994)을 거쳤고, 상세 창은 KAIST 원자력 및 양자공학과 교수 경력을 「1994-현재」로 적는다.[^deptdetail] 2002-2003년에는 미국 미시건대학교 교환교수였다.[^deptdetail]

상세 창의 경력(Experience)은 KAIST 방사선및핵의공학연구소 소장(2006-현재), IEEE NPS RISC 위원(2010-현재), 원자력안전전문위원회 방재환경분과 전문위원(2009-현재), 한국의학물리학회 명예이사(2006-현재), 한국원자력학회 평의원(2004-현재), 대한방사선방어학회 편집위원(2004-현재)을 「현재」로 적는다.[^deptdetail] 학과 연구센터 페이지는 「방사선 및 핵의공학 연구센터」를 조승룡 교수 이름과 함께 싣는다.[^center] 상세 창이 기간을 끝맺어 적은 경력은 원자력안전전문위원회 정책제도분과 전문위원(2006-2007), 중저준위 방사성폐기물 처분시설 부지선정위원(2005-2006), 한국원자력학회 편집위원(2003-2006), 원자력사고고장등급평가위원(2003-2006), 한국관세청 컨테이너 도입 자문위원(2001-2003)이다.[^deptdetail]

교수가 저자로 참여한 2021–2026년 논문 목록을 보면 교수의 전문 분야는 섬광 검출기와 반도체 검출기를 쓰는 방사선 계측과 그 스펙트럼·신호의 해석이다. 감마선·베타선 분광 자료의 핵종 판별과 정량, 선량 평가에 인공신경망, 희소 표현, 베이지안 추론, 몬테카를로 모사를 쓰고, 중성자·감마선 펄스 파형 판별, 실리콘 광증배관과 단일 광자 애벌랜치 다이오드(SPAD, 광자 하나에도 신호를 내도록 만든 광다이오드) 같은 광센서의 방사선 검출 응용, 방사성 폐기물·우라늄 폐기물과 원자력 시설 해체 관련 측정, 라돈·토론 측정, 표적 알파 치료용 CZT 검출기를 다룬다.[^cr] 파이로프로세싱(사용후핵연료를 고온 용융염 속에서 전기화학적으로 처리하는 기술) 시설의 물질수지 평가(핵물질이 들어오고 나가고 남은 양을 맞춰 보는 평가) 전략, 치과용 콘빔 CT 영상, 수중 비열 플라즈마(전자와 기체 분자의 온도가 열평형을 이루지 않은 플라즈마)로 옥살산을 무기화(유기물을 무기물로 분해하는 일)하는 연구에도 저자로 참여했다.[^cr]

## 응용 분야

대표 논문 1은 원자력 시설과 의료 환경의 방사선 방호를,[^p1] 대표 논문 3은 방사성 폐기물 관리의 시료 채취와 방사능 농도 분석을 응용으로 든다.[^p3] 대표 논문 2는 고속 중성자 투과 영상을 국토 안보 같은 여러 분야에서 쓰는 비파괴 검사 기법으로 소개한다.[^p2] 대표 논문 5·6은 표적 알파 치료에 쓰는 ²²⁵Ac의 방사능 측정과 영상을 목표로 하고,[^p5][^p6] 대표 논문 7은 해양 방사선 감시를 위한 선박용 측정 시스템을 다룬다.[^p7] 논문 목록에는 원자력 시설 해체에서의 방사성 동위원소 판별과 상용 규모 파이로프로세싱 시설의 물질수지 평가 전략을 다룬 논문도 있다.[^cr]

## 최근 논문 목록 (2021–2026)

조규성 교수가 저자로 참여한 2021–2026년 논문 48편이다(학술지 논문 39편, 학회 발표 논문 9편; 2026년 7편, 2025년 8편, 2024년 12편, 2023년 10편, 2022년 3편, 2021년 8편). 학회 발표 논문은 IEEE Nuclear Science Symposium, Medical Imaging Conference and Room Temperature Semiconductor Detector Conference(2024·2025년)와 SPIE Medical Imaging(2023·2024년)에 실린 논문이다. 저자·제목·학술지 표기는 출판사가 등록한 서지를 따랐고, 연도는 서지의 발행 연도이며, 연도 안에서는 발행일이 늦은 논문부터 적었다.[^cr]

**2026**

- Jaehyun Park, Gyohyeok Song, Jisoo Kim, Gyuseong Cho. "A Bayesian approach to estimate ambient dose equivalent for liquid radioactive waste measurements". *Applied Radiation and Isotopes 236, 112689 (2026)*.
- Gyohyeok Song, Jisung Hwang, Jaehyun Park, Jisoo Kim, Gyuseong Cho. "Real-time ambient neutron dosimetry based on TOF-derived response and G(E) convolution". *Scientific Reports (2026)*.
- Wonku Kim, Hyunbin Yun, Deokseong Kim, Jaehyun Park, KyungTaek Lim, Gyuseong Cho. "Development of a deep learning-based gamma spectroscopic analysis system for high-radiation field applications". *Radiation Physics and Chemistry 246, 113963 (2026)*.
- Deokseong Kim, Wonku Kim, Sangho Lee, Hyunbin Yun, Kilyoung Ko, Gyuseong Cho. "Feasibility study of deep learning-based beta spectroscopic analysis using a plastic scintillation detector". *Radiation Measurements 194, 107672 (2026)*.
- Kyungmin Kim, Kyunghun Jung, Won-Hyuk Jang, Yu-Jeong Choi, Jong Soo Nam, Tack-Jin Kim, Gyuseong Cho. "Estimation of self-absorption correction factors for gamma-ray spectrometry of radioactive waste using MCNP". *Nuclear Engineering and Technology 58, 104064 (2026)*.
- Gyohyeok Song, Biswajit Das, Youngho Seo, Gyuseong Cho, Javier Caravaca. "Performance Evaluation of Single- and Double-Layer CZT Compton Cameras for 225 Ac Imaging". *IEEE Transactions on Nuclear Science 73, 1481-1494 (2026)*.
- Ki-baek Shin, Heejae Lee, Geon Woo Yang, Yong Cheol Hong, Daeseok Hong, Kangil Kim, Gyuseong Cho. "Mineralization of oxalic acid by underwater non-thermal plasma: TOC removal and 13C isotope tracer". *Carbon Letters 36, 201-211 (2026)*.

**2025**

- Seoyun Jang, Robin Peter, Biswajit Das, Youngho Seo, Gyuseong Cho. "Design and evaluation of CZT-based micro-activity dose calibrator for TAT application using Monte Carlo simulation". *Journal of Instrumentation 20, C12021 (2025)*.
- D. Kim, W. Kim, J. Park, S. Lee, G. Song, H. Yun, S. Jang, U. Lee, H. Kim, J. Park, G. Cho. "Optimizing Scintillator Thickness and GEB Parameters for Beta Spectroscopy in Plastic Scintillation Detectors". *2025 IEEE Nuclear Science Symposium (NSS), Medical Imaging Conference (MIC) and Room Temperature Semiconductor Detector Conference (RTSD), 1-1 (2025)*.
- G. Song, J. Hwang, J. Hwang, J. Park, S. Lee, D. Kim, S. Jang, U. Lee, G. Cho. "Feasibility Study on Material Decomposition Using Neutron and Gamma-Ray". *2025 IEEE Nuclear Science Symposium (NSS), Medical Imaging Conference (MIC) and Room Temperature Semiconductor Detector Conference (RTSD), 1-1 (2025)*.
- Jaehyun Park, Gyohyeok Song, Wonku Kim, Yeon Kyoung Choi, Ki-baek Shin, Gyuseong Cho. "Comparison of liquid radioactive waste characteristics using CeBr3, LaBr3(Ce), and NaI(Tl) scintillators for on-site applications". *Radiation Measurements 188, 107503 (2025)*.
- Jaehyun Park, Gyohyeok Song, Wonku Kim, Shin Ki-baek, Yeon Kyoung Choi, Gyuseong Cho. "Uncertainty estimation of minimum detectable activity through sparse spectrum using kernel-based Gaussian process regression". *Radiation Physics and Chemistry 233, 112667 (2025)*.
- Gyohyeok Song, Jisung Hwang, Junhyeok Kim, Hojik Kim, Sangho Lee, Jaehyun Park, Gyuseong Cho. "Automatic classification of multi-channel PSD results combining unsupervised and supervised learning". *Nuclear Engineering and Technology 57, 103331 (2025)*.
- Byung Hee Won, Man-Sung Yim, Gyuseong Cho. "Development of optimal Material Balance Evaluation (MBE) strategy for commercial-scale pyroprocessing facility using stochastic modeling and simulation techniques". *Nuclear Engineering and Technology 57, 103386 (2025)*.
- Wonku Kim, Kilyoung Ko, Jaehyun Park, Sangho Lee, Hyunbin Yun, Gyuseong Cho. "Deep learning-based gamma spectroscopic analysis considering multiple variables for in situ applications". *Radiation Physics and Chemistry 226, 112261 (2025)*.

**2024**

- Wonku Kim, Kilyoung Ko, Jaehyun Park, Sangho Lee, Gyuseong Cho. "Parametric optimization for estimating beta detection efficiency in thin plastic scintillation detector". *Radiation Physics and Chemistry 225, 112116 (2024)*.
- G. Song, J. Park, S. Lee, W. Kim, H. Yun, D. Kim, S. Jang, K. Lee, G. Cho. "Performance Evaluation of Automatic Classification Algorithm for Acquisition Fast Neutron Radiography with Multi-Channel Pulse Shape Discrimination Results". *2024 IEEE Nuclear Science Symposium (NSS), Medical Imaging Conference (MIC) and Room Temperature Semiconductor Detector Conference (RTSD), 1-1 (2024)*.
- J. Park, G. Song, W. Kim, S. Lee, K. Ko, K. Lee, H. Yoon, D. Kim, G. Cho. "A Study on Inference Method of Minimum Detectable Activity for Measurement of Liquid Radioactive Waste". *2024 IEEE Nuclear Science Symposium (NSS), Medical Imaging Conference (MIC) and Room Temperature Semiconductor Detector Conference (RTSD), 1-1 (2024)*.
- S. Das, J. Kim, J. Park, G. Cho. "A New Method for Thoron Radon Individual Detection from Same Air". *2024 IEEE Nuclear Science Symposium (NSS), Medical Imaging Conference (MIC) and Room Temperature Semiconductor Detector Conference (RTSD), 1-1 (2024)*.
- S. Lee, J. Kim, J. Hwang, W. Kim, K. Ko, J. Park, G. Song, D. Kim, H. Yun, G. Cho. "Preliminary Study of X-ray Ghost Imaging Reconstruction with a Deep Neural Network Constraint". *2024 IEEE Nuclear Science Symposium (NSS), Medical Imaging Conference (MIC) and Room Temperature Semiconductor Detector Conference (RTSD), 1-2 (2024)*.
- H. Yun, W. Kim, J. Park, S. Lee, G. Song, K. Lee, S. Jang, D. Kim, G. Cho. "Trapezoidal Pulse Height Method Using Deep Learning for Pile-Up Correction in High Radiation Environments". *2024 IEEE Nuclear Science Symposium (NSS), Medical Imaging Conference (MIC) and Room Temperature Semiconductor Detector Conference (RTSD), 1-1 (2024)*.
- Sangho Lee, Kilyoung Ko, Gyohyeok Song, Wonku Kim, Seonkwang Yoon, Chaehun Lee, Kyung Taek Lim, Gyuseong Cho. "Investigation of neutron/gamma-ray distribution in SiPM-based pulse shape discrimination using EJ-276 plastic scintillators". *Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment 1066, 169638 (2024)*.
- Jaehyun Park, Gyohyeok Song, Wonku Kim, Junhyeok Kim, Jisung Hwang, Hyunduk Kim, Gyuseong Cho. "Identification of radioactive isotopes in decommissioning of nuclear facilities using ensemble learning". *Radiation Physics and Chemistry 220, 111598 (2024)*.
- Moonhyung Cho, Jisung Hwang, Sangho Lee, Kilyoung Ko, Wonku Kim, Gyuseong Cho. "A counting-time optimization method for artificial neural network (ANN) based gamma-ray spectroscopy". *Nuclear Engineering and Technology 56, 2690-2697 (2024)*.
- Jaehyun Park, Geunyoung An, Gyohyeok Song, Wonku Kim, Junhyeok Kim, Kyung Taek Lim, Jisung Hwang, Gyuseong Cho. "Development and optimization of a backscatter X-ray detection system based on pencil beam scanning". *Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment 1063, 169277 (2024)*.
- Kilyoung Ko, Changyeop Lee, Wonku Kim, Sangho Lee, Wooseub Kim, Gyohyeok Song, Jisung Hwang, Jaehyun Park, Yongsun Yi, Gyuseong Cho. "Study on the effect of operating conditions on SiPM-based digital γ/n pulse shape discrimination". *Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment 1062, 169225 (2024)*.
- Sungho Yun, Dain Choi, Sung-Joon Ye, Gyuseong Cho, Seungryong Cho. "Investigation on substantial asymmetry of HU value in dental cone-beam CT with offset detector". *Medical Imaging 2024: Physics of Medical Imaging, 100 (2024)*.

**2023**

- Jisung Hwang, Hyoungtaek Kim, Kyung Taek Lim, Gyuseong Cho. "Evaluation of SiPM-based readout system with gain stabilization for TL dosimetry". *Radiation Physics and Chemistry 212, 111164 (2023)*.
- Chang-Jong Kim, Mee Jang, Hyuncheol Kim, Jong-Myoung Lim, Wanno Lee, Gyu-Seong Cho. "Development of a real-time mobile gamma-ray measurement system for shipboard use". *Nuclear Engineering and Technology 55, 4077-4082 (2023)*.
- Junhyeok Kim, Byoungil Jeon, Jisung Hwang, Gyohyeok Song, Myungkook Moon, Gyuseong Cho. "Pulse height estimation and pulse shape discrimination in pile-up neutron and gamma ray signals from an organic scintillation detector using multi-task learning". *Applied Radiation and Isotopes 199, 110880 (2023)*.
- Junhyeok Kim, Jisung Hwang, Gyohyeok Song, Kilyoung Ko, Hojik Kim, Gyuseong Cho. "Untrained neural network-based unfolding method for quantitative analysis of NaI(Tl) gamma spectrometers". *Radiation Physics and Chemistry 209, 110993 (2023)*.
- Kilyoung Ko, Wonku Kim, Hyunwoong Choi, Gyuseong Cho. "Feasibility study on a stabilization method based on full spectrum reallocation for spectra having non-identical momentum features". *Nuclear Engineering and Technology 55, 2432-2437 (2023)*.
- Jichang Ryu, Junghwan Hong, Jungsuk Park, Gyuseong Cho. "Bayesian Inference for the Quantitative Analysis of Nonuniformly Distributed Uranium Radioactivity in a Waste Drum". *IEEE Transactions on Nuclear Science 70, 1477-1489 (2023)*.
- Hojik Kim, Junhyeok Kim, Jisung Hwang, Kilyoung Ko, Gyuseong Cho. "Pixel-Grouping G(E) Functions for Estimating Dose Rates from Unknown Source Distributions with a Position-Sensitive Detector". *Sensors 23, 4591 (2023)*.
- Sungho Yun, Uijin Jeong, Taejin Kwon, Da-in Choi, Taewon Lee, Sung-Joon Ye, Gyuseong Cho, Seungryong Cho. "Penalty-driven enhanced self-supervised learning (Noise2Void) for CBCT denoising". *Medical Imaging 2023: Physics of Medical Imaging, 86 (2023)*.
- Jisung Hwang, Junhyeok Kim, Byoungil Jeon, Kilyoung Ko, Eunbie Ko, Gyuseong Cho. "Estimation of ambient dose equivalent rate with a plastic scintillation detector using the least-square and first-order methods-based G(E) function". *Applied Radiation and Isotopes 194, 110707 (2023)*.
- Hyeonjun Choi, Ji-yong Shin, Jaeho Jang, Gyuseong Cho. "A modified decaying source method for dead time measurement with non-negligible background counts". *Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment 1048, 168026 (2023)*.

**2022**

- Sopan Das, Junhyeok Kim, Jaehyun Park, Hojong Chang, Gyuseong Cho. "A preliminary study on real-time Rn/Tn discriminative detection using air-flow delay in two ion chambers in series". *Nuclear Engineering and Technology 54, 4644-4651 (2022)*.
- Jisung Hwang, Byoungil Jeon, Junhyeok Kim, Hyoungtaek Kim, Gyuseong Cho. "Deep learning-based spectrum-dose prediction for a plastic scintillation detector". *Radiation Physics and Chemistry 201, 110444 (2022)*.
- Junhyeok Kim, Daehee Lee, Jinhwan Kim, Giyoon Kim, Jisung Hwang, Wonku Kim, Gyuseong Cho. "Radioisotope identification using sparse representation with dictionary learning approach for an environmental radiation monitoring system". *Nuclear Engineering and Technology 54, 1037-1048 (2022)*.

**2021**

- Junhyeok Kim, Jisung Hwang, Jinwoo Kim, Kilyoung Ko, Eunbie Ko, Gyuseong Cho. "Ghost imaging with Bayesian denoising method". *Optics Express 29, 39323 (2021)*.
- Jichang Ryu, Chanjun Park, Jungsuk Park, Namchan Cho, Jaehyun Park, Gyuseong Cho. "Development of Neural Network Model With Explainable AI for Measuring Uranium Enrichment". *IEEE Transactions on Nuclear Science 68, 2670-2681 (2021)*.
- Kilyoung Ko, Hyunwoong Choi, Yongsun Yi, Wonku Kim, Junhyeok Kim, Jisung Hwang, Eunbie Ko, Gyuseong Cho. "Discrete Convolution-Based Energy Spectrum Configuring Method for the Analysis of the Intrinsic Radiation of 176Lu". *Sensors 21, 7040 (2021)*.
- Jun-Ha Kim, Gyu-Seong Cho, Jung-Jun Lee, Sang-Bum Hong, Eun-Joong Lee, Byung-Chae Lee, Bum-Kyung Seo. "Development of Scan Survey Adjust Method for Radioactively Contaminated Sediment in Underwater Conditions". *Journal of Coastal Research 114 (2021)*.
- Hojong Chang, KyungDon Choi, Byunghun Han, Hyunduk Kim, Jaeho Ko, Gyuseong Cho. "Development of Chemiluminescence Resonance Test System Using SiPM Front-end ASIC to Detect Na and K Ions in Urine". *International Journal on Advanced Science, Engineering and Information Technology 11, 1172-1177 (2021)*.
- Hyoungtaek Kim, Kyung Taek Lim, Jungil Lee, Gyuseong Cho. "On the use of silicon photomultipliers for thermoluminescence measurements". *Radiation Physics and Chemistry 182, 109381 (2021)*.
- Kyung Taek Lim, Hyoungtaek Kim, Jinhwan Kim, Gyuseong Cho. "Effect of electric field on primary dark pulses in SPADs for advanced radiation detection applications". *Nuclear Engineering and Technology 53, 618-625 (2021)*.
- Byoungil Jeon, Junha Kim, Eunjoong Lee, Myungkook Moon, Gyuseong Cho. "Pseudo-Gamma Spectroscopy Based on Plastic Scintillation Detectors Using Multitask Learning". *Sensors 21, 684 (2021)*.

## 연락과 위치

- 위치: N27, 5117(학과 교수 소개의 교수 연구실 표기)[^dept]
- 우편 주소: (34141) 대전광역시 유성구 대학로 291(구성동, 373-1)(학과 페이지 바닥글 주소)[^dept]
- 전화: 3821(학과 교수 소개의 표기)[^dept]
- 교수 이메일: gscho@kaist.ac.kr[^dept]
[^p1]: G. Song 외, G. Cho, Scientific Reports (온라인 2026-09-03). <https://doi.org/10.1038/s41598-026-69119-9> 초록 기준.
[^p2]: G. Song 외, G. Cho, Nuclear Engineering and Technology 57, 103331 (2025). <https://doi.org/10.1016/j.net.2024.11.033> 초록 기준(OpenAlex 등록 초록).
[^p3]: K. Kim 외, G. Cho, Nuclear Engineering and Technology 58, 104064 (2026). <https://doi.org/10.1016/j.net.2025.104064> 초록 기준(OpenAlex 등록 초록).
[^p4]: M. Cho 외, G. Cho, Nuclear Engineering and Technology 56, 2690-2697 (2024). <https://doi.org/10.1016/j.net.2024.02.029> 초록 기준(OpenAlex 등록 초록).
[^p5]: S. Jang 외, G. Cho, Journal of Instrumentation 20, C12021 (온라인 2025-12-17). <https://doi.org/10.1088/1748-0221/20/12/c12021> 초록 기준.
[^p6]: G. Song 외, J. Caravaca, IEEE Transactions on Nuclear Science 73, 1481-1494 (2026). <https://doi.org/10.1109/tns.2026.3663840> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: C.-J. Kim 외, G.-S. Cho, Nuclear Engineering and Technology 55, 4077-4082 (2023). <https://doi.org/10.1016/j.net.2023.07.026> 초록 기준(OpenAlex 등록 초록).
[^p8]: J. Kim 외, G. Cho, Optics Express 29, 39323 (온라인 2021-11-10). <https://doi.org/10.1364/oe.438478> 초록 기준.
[^dept]: KAIST 원자력및양자공학과 교수 소개 페이지 <https://nuclear.kaist.ac.kr/people/professor.php> (조규성 교수 항목의 최종학위, Office-Rm, Tel, Email과 바닥글의 학과 주소, 2026-10-25 열람)
[^deptdetail]: KAIST 원자력및양자공학과 교수 소개 페이지 <https://nuclear.kaist.ac.kr/people/professor.php> (조규성 교수 상세 창의 Education, Experience, Research Field, 2026-10-25 열람)
[^center]: KAIST 원자력및양자공학과 연구센터 페이지 <https://nuclear.kaist.ac.kr/research/researchcenter.php> (연구센터 네 곳과 함께 적힌 교수 이름, 2026-10-25 열람)
[^depten]: KAIST 원자력및양자공학과 영문 교수 소개 페이지 <https://nuclear.kaist.ac.kr/eng/people/professor.php> (Cho, Gyuseong Professor 항목, 2026-10-25 열람)
[^deptlab]: KAIST 원자력및양자공학과 연구그룹 페이지 「방사선」 <https://nuclear.kaist.ac.kr/research/the_lap.php?category=004> (방사선계측 및 의료영상센서 연구실, 교수 조규성, 2026-10-25 열람)
[^deptlaben]: KAIST 원자력및양자공학과 영문 연구그룹 페이지 「Medical Radiation」 <https://nuclear.kaist.ac.kr/eng/research/the_lap.php?category=004> (Radiation Detection and Medical Image Sensor Laboratory, Professor Cho, Gyuseong, 2026-10-25 열람)
[^cr]: Crossref 출판사 등록 서지 <https://api.crossref.org/> (교수 ORCID 0000-0001-7493-4111이 붙은 기록, 교수 이름 Gyuseong Cho·Gyu-Seong Cho 검색 기록, DOI 조회; 2021–2026년 논문의 저자·제목·학술지·권·쪽·발행일, 2026-10-25 조회)
[^oa]: OpenAlex 서지 <https://api.openalex.org/> (ORCID 0000-0001-7493-4111이 붙은 저자 기록의 2021–2026년 논문과 저자 이름 Gyuseong Cho 검색 기록; 논문별 교수 소속, 2026-10-25 조회)

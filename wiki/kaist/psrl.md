# 광자 시스템 연구실 (Photonics Systems Research Lab, PSRL)

**KAIST 전기및전자공학부 · 김훈 교수**

- 분야: 광자 시스템, 광 전송 시스템, 자유공간 광통신, 광섬유 전송·광 가입자망, 광 기반 sub-THz 무선 신호
- 대분야: 전기전자·반도체·광학
- 태그: 광통신[^home][^research][^p2], 무선·이동통신[^research][^p7], 컴퓨터 네트워크[^research][^p4]
- 홈페이지: <https://psrl.kaist.ac.kr/>
- 근거와 출처: [광자 시스템 연구실 근거 페이지](psrl-sources.md)

> 빛으로 데이터를 주고받는 광 통신 시스템을 연구하는 연구실이다. 공기와 우주 공간으로 레이저 빛을 보내는 자유공간 광통신, 광 가입자망·데이터센터를 잇는 단거리 광섬유 전송, 6G 이후 무선통신을 위해 빛으로 sub-THz 무선 신호를 만드는 기술을 다룬다.[^home][^research]

## 무엇을 연구하나

연구실 누리집은 광자 시스템과 그 부분 시스템에 관련된 과학·공학 주제에 관심을 두고, 2014년부터 대용량 광섬유 전송 시스템, 자유공간 광통신, 광대역 광 가입자망, 광 센서 시스템을 연구해 왔다고 소개한다.[^home] 전기및전자공학부 교수 소개와 반도체시스템공학과 연구실 목록은 주요 연구를 광자 시스템(Photonic systems)과 광파 전송 시스템(lightwave transmission systems)으로 적는다.[^eeprof][^ssel]

Research 페이지가 드는 첫째 주제는 자유공간 광통신(FSO, 광섬유 없이 공기나 우주 공간으로 레이저 빛을 보내 데이터를 주고받는 통신)이다. 무선 주파수(RF) 대역 자원이 모자라고 더 많은 데이터 용량이 필요해 FSO가 두 지점을 잇는 무선 링크에 점점 많이 쓰인다고 설명하며, 2022년 이후 발사된 Starlink 위성이 위성끼리 잇는 레이저 통신 단말을 단 예와 NASA가 우주선과 지상국 사이 통신에 이 기술을 쓰는 예를 든다. 위성과 광 지상국을 잇는 데 FSO가 앞으로도 쓸 해법으로 여겨지지만, 위성의 빠른 궤도 속도 때문에 안정한 링크를 세우기 어렵고 대기 난류와 날씨 변화가 빛의 전파를 크게 해칠 수 있다. 연구실은 대기 난류가 만든 파면 왜곡(빛의 위상 면이 흐트러지는 것)을 줄이거나 보상하는 기술, 빠르고 정밀한 조준·포착·추적(PAT) 알고리즘, FSO 송수신기의 크기·무게·전력 소모를 줄이는 연구를 한다.[^research]

둘째 주제는 광섬유 전송 시스템이다. Research 페이지는 1977년 광섬유 통신이 도입된 뒤 용량이 3백만 배 넘게 늘어 광대역 인터넷·클라우드 컴퓨팅·동영상 스트리밍을 이끌었지만, 세계 망 트래픽이 해마다 약 2 dB씩 늘고 있어 용량을 더 늘릴 기술이 필요하고 시스템의 효율·유연성·에너지 소비도 과제로 남았다고 설명한다. 광섬유는 전자 부품 사이를 잇는 짧은 연결로도 쓰임이 넓어지고 있다. 연구실은 광 가입자망(가입자 집이나 건물까지 광섬유로 잇는 통신망), 데이터센터 네트워크, 광 컴퓨트 인터커넥트(계산 장치 사이를 빛으로 잇는 연결)에 쓰이는 단거리 광섬유 전송 시스템의 용량을 늘리고 비용을 줄이는 기술을 개발한다.[^research]

셋째 주제는 6G 이후를 위한 광 기반 sub-THz 기술이다. 셀룰러 무선통신은 셀 크기를 줄이고 더 넓은 RF 대역을 써서 용량을 늘려 왔고, 다음 세대 시스템은 0.1–1 THz의 sub-THz 대역으로 이동 사용자에게 초당 수백 기가비트의 데이터를 전할 것으로 기대된다. 그러나 이런 넓은 대역의 sub-THz 무선 신호를 전자 기술만으로 만들고 검출하기는 어렵다. 연구실은 sub-THz 무선 신호를 비용 효율적으로 만들고 검출하는 광 기술을 개발한다.[^research]

대표 논문으로 보면 연구는 세 갈래다. 첫째, 대기 난류 속 빛의 세기 흔들림과 빔 정렬·포착을 다루는 자유공간 광통신이다(대표 논문 1, 2, 3).[^p1][^p2][^p3] 둘째, 데이터센터 연결과 광 가입자망을 위한 광섬유 전송의 신호 처리와 변조다(대표 논문 4, 5, 6).[^p4][^p5][^p6] 셋째, 두 레이저 빛을 섞어 sub-THz 신호를 만들고 그 흔들림을 보상하는 기술이다(대표 논문 7, 8).[^p7][^p8]

## 주요 연구 주제

### 1. 자유공간 광통신: 대기 난류와 빔 정렬

편광 방향이 빔 단면의 자리마다 다른 벡터 빔이 약한 대기 난류에서 보이는 빛 세기 흔들림의 정도를 이론식으로 구했고,[^p1] 사분할 검출기로 수신 빔의 위치를 추정해 빔을 빠르게 추적하는 방법을 실험으로 보였다.[^p2] 위성 사이를 레이저로 잇는 링크에서 위성 진동이 있을 때 상대 위성의 빔을 잡는 데 걸리는 시간을 분석하고, 그 시간에 대한 최적 빔 발산각을 유도했다.[^p3] 최근 논문 목록에는 위성-지상 FSO 링크를 지상 시험대로 모사하는 데 필요한 최소 링크 거리, FSO 기반 이동통신에서 수신기가 직사광선에 노출될 확률, 가변 초점 액체 렌즈로 빔의 방향과 퍼짐을 조절하는 연구도 있다.[^pubs] 대표 논문 1, 2, 3.

### 2. 광섬유 전송과 광 가입자망

데이터센터 연결용 세기 변조·직접 검출 시스템에서 비선형 등화기를 미니배치 경사 하강법과 Adam으로 학습시켜 빠르게 수렴하게 했고,[^p4] 코히어런트 수동형 광 네트워크에서 쉬고 있는 가입자 단말이 흘리는 빛을 변조기 바이어스 조절로 줄였다.[^p5] 직접 변조 레이저와 직접 검출을 쓰는 시스템에서 평균 광 출력과 최대 전기 진폭의 제약 아래 채널 용량을 얻는 신호 분포를 계산하고 실험으로 확인했다.[^p6] 최근 논문 목록에는 직접 변조 레이저로 보낸 100 Gb/s PAM-6 신호, 2비트 DAC로 만든 50 Gb/s 광 가입자망, 인공 신경망 등화기를 과적합 없이 학습시키는 데 필요한 의사 난수 이진 수열의 길이 연구도 있다.[^pubs] 대표 논문 4, 5, 6.

### 3. 빛으로 만드는 sub-THz 무선 신호

두 레이저 빛을 섞어 그 주파수 차이로 sub-THz 신호를 만드는 광 헤테로다인 방식에서, 따로 도는 두 레이저의 주파수·위상 흔들림을 검출해 광 IQ 변조기로 보상하는 피드포워드 방법을 내놓았고,[^p8] 이 방법으로 132 GHz에서 16-QAM 신호를 무선으로 보냈다.[^p7] 최근 논문 목록에는 편광 다중화와 광검출기 하나로 중간 주파수 데이터와 국부 발진 신호를 함께 보내는 밀리미터파 이동 프론트홀 연구도 있다.[^pubs] 대표 논문 7, 8.

## 대표 논문

랩 International Journals 목록의 2021–2026년 학술지 논문 가운데 김훈 교수가 마지막 저자인 논문을, 세 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [Scintillation index of arbitrary vector beams in atmospheric turbulence](https://doi.org/10.1364/ol.580752) · Optics Letters | 편광 방향이 빔 단면의 자리마다 고르지 않게 분포하는 벡터 빔은 대기 난류 때문에 생기는 빛 세기의 깜빡임(신틸레이션)을 줄인다는 사실이 최근 보고됐다. 이 연구는 약한 대기 난류에서 임의의 벡터 빔이 보이는 신틸레이션 지수(빛 세기가 흔들리는 정도를 나타내는 값)를 리토프 섭동 이론(Rytov perturbation theory)으로 구하는 일반식을 세웠다. 분할 단계 푸리에 방법(split-step Fourier method)으로 한 모의실험 결과는 이 식이 벡터 빔의 신틸레이션 지수를 정확히 예측함을 확인했다.[^p1] | 1저자 W. Moon, 마지막 저자 김훈 (2명) |
| 2 | 2025 | [Beam position estimation method for fast beam tracking in free-space optical systems using a quadrant detector](https://doi.org/10.1364/ol.576243) · Optics Letters | 자유공간 광통신에서 송신기와 수신기의 빔을 빠르고 정밀하게 맞추려면, 수신기에 들어오는 빔의 각도 방향을 정확히 추정하는 일이 중요하다. 이 연구는 사분할 검출기(빛을 받는 면을 넷으로 나눈 검출기)에 쓰는 빔 위치 추정 방법을 내놓고, 이 방법으로 빠른 빔 추적을 실험으로 보였다. 실험에서 제안한 방법은 기존의 difference-over-sum 방법보다 21%, log-ratio 방법보다 36% 빠르게 빔을 추적했다.[^p2] | 1저자 M. T. Nguyen, 마지막 저자 김훈 (3명) |
| 3 | 2023 | [Acquisition Time in Laser Inter-Satellite Link Under Satellite Vibrations](https://doi.org/10.1109/jphot.2023.3291807) · IEEE Photonics Journal | 위성 사이를 레이저로 잇는 위성 간 링크(ISL)에서는 빔의 조준·포착·추적(PAT)이 큰 기술 과제다. 링크를 빨리 열고 통신 시간을 늘리려면 상대 빔을 잡는 데 걸리는 포착 시간을 줄여야 하는데, 위성 진동은 PAT 과정을 방해해 포착 시간을 늘린다. 이 연구는 위성 진동이 있을 때 레이저 위성 간 링크의 평균 포착 시간을 이론으로 분석해, 나선형으로 훑기 시작해 탐색 빔을 잡을 때까지 걸리는 시간을 진동이 만든 조준 오차를 넣어 식으로 냈고, 포착 시간에 대한 최적 빔 발산각(빔이 퍼지는 각도)도 유도했다. 몬테카를로 모의실험과 개념 증명 실험으로 분석을 검증했고, 링크 조건에 맞춰 빔 발산각을 조절하면 포착 시간을 최소로 줄일 수 있음을 보였다.[^p3] | 1저자 K. Lee, 마지막 저자 김훈 (3명) |
| 4 | 2026 | [Fast-converging Volterra equalizer using mini-batch gradient descent-based Adam optimization](https://doi.org/10.1109/lpt.2026.3682670) · IEEE Photonics Technology Letters | 세기 변조·직접 검출(IM/DD, 빛의 세기에 데이터를 싣고 수신기에서 세기만 읽는 방식) 하이브리드 데이터센터 연결을 위해, 2차 볼테라 비선형 등화기(VNLE, 신호가 겪은 비선형 왜곡을 수신 쪽에서 되돌리는 신호 처리)를 미니배치 경사 하강법(MGD)과 Adam(학습률을 스스로 조절하는 최적화 방법)으로 학습하게 했다. Adam의 적응 학습률과 미니배치 단위 갱신을 함께 써서 큰 배치 없이도 빠르고 안정하게 수렴한다. 200 Gb/s PAM-4 신호를 1 km와 2 km 단일 모드 광섬유로 보낸 전송 실험에서, 수렴에 필요한 반복 횟수로 잰 수렴 속도가 기존의 재귀 최소 제곱(RLS) 기반 VNLE보다 크게 좋아졌다.[^p4] | 1저자 J. Kim, 마지막 저자 김훈 (2명) |
| 5 | 2026 | [Suppression of optical power leakage through IQ modulator bias control in upstream coherent PON](https://doi.org/10.1109/lpt.2026.3669146) · IEEE Photonics Technology Letters | 시간 분할 다중화(TDM) 방식 코히어런트 수동형 광 네트워크(PON, 광섬유 하나를 여러 가입자가 나눠 쓰는 광 가입자망)에서는, 쉬고 있는 가입자 단말(ONU)도 IQ 변조기의 소광비(켜짐과 꺼짐 상태의 빛 세기 비)가 유한해서 상향(가입자에서 망 쪽으로 가는) 방향으로 남은 빛을 흘릴 수 있다. 이 연구는 IQ 변조기의 바이어스를 조절해 새어 나가는 빛의 세기를 최소로 하는 방법을 내놓고, 그 이론과 실험 검증을 함께 보였다. 실험에서 새는 빛을 49 dB 넘게 억눌렀다.[^p5] | 1저자 J. Lee, 마지막 저자 김훈 (3명) |
| 6 | 2023 | [Capacity-achieving symbol distributions for directly modulated laser and direct detection systems](https://doi.org/10.1364/oe.484104) · Optics Express | 직접 변조 레이저(DML, 구동 전류로 레이저 빛의 세기를 바로 바꾸는 광원)와 직접 검출(DD)을 쓰는 시스템에서, 확률적 성상 성형(PCS, 신호 점마다 보내는 빈도를 다르게 정하는 기법)을 적용한 PAM 신호의 용량 달성 심볼 분포를 찾았다. DML-DD 시스템은 바이어스 티로 직류 바이어스 전류와 교류 결합 변조 신호를 넣고 레이저 구동에 전기 증폭기를 흔히 쓰기 때문에, 평균 광 출력과 최대 전기 진폭의 제약을 받는다. 이 제약 아래 블라후트-아리모토 알고리즘으로 채널 용량을 계산해 용량을 달성하는 심볼 분포를 구하고 실험으로 확인했다. 광 변조 지수(OMI)가 1보다 작을 때 PCS는 용량을 조금만 늘리지만, PCS를 쓰면 클리핑 왜곡 없이 OMI를 1보다 크게 키울 수 있어 고르게 분포한 신호보다 용량을 높일 수 있다.[^p6] | 1저자 D. Kim, 마지막 저자 김훈 (2명) |
| 7 | 2025 | [Photonics-based wireless transmission of 16-QAM signals using feedforward compensation of the frequency and phase noise of free-running lasers](https://doi.org/10.1364/ol.568731) · Optics Letters | 두 레이저 빛을 섞어 신호를 만드는 광 헤테로다인 방식은 sub-THz 무선 시스템을 위한 방법으로 기대되지만, 서로 묶이지 않고 따로 도는 레이저의 주파수·위상 흔들림이 무선 신호 품질을 크게 떨어뜨린다. 이 연구는 따로 도는 두 레이저를 헤테로다인한 출력에 피드포워드 방식의 주파수·위상 보상을 적용해 16-QAM 신호를 무선으로 보내는 실험을 했다. 90° 하이브리드 결합기로 헤테로다인 신호의 주파수·위상 흔들림을 검출하고, 그 값으로 광 IQ 변조기를 구동해 보상했다. 132 GHz에서 80 Gb/s 16-QAM 신호를 수신기의 반송파 위상 추정 없이 최대 30 m 무선 채널로 보냈다.[^p7] | 1저자 K. Woo, 마지막 저자 김훈 (3명) |
| 8 | 2024 | [Feedforward Compensation of Laser Frequency and Phase Noise for Photonics-Based Sub-THz Generation](https://doi.org/10.1109/lpt.2024.3379496) · IEEE Photonics Technology Letters | 두 레이저 빛을 합쳐 광검출기로 검출하는 광 헤테로다인 검출은 sub-THz 신호를 만드는 광학적 방법의 하나지만, 따로 도는 두 레이저를 헤테로다인해 만든 신호는 주파수 안정도가 낮고 위상 잡음이 크다. 이 연구는 sub-THz 신호를 만들려고 헤테로다인한 두 레이저의 주파수와 위상을 피드포워드 방식으로 보상하는 방법을 제안하고 시연했다. 광학적 주파수 하향 변환 뒤 두 레이저 빛이 만드는 맥놀이 신호에서 주파수 드리프트와 위상 흔들림을 검출하고, 광 IQ 변조기로 보상한다. 165 GHz 신호로 한 이론 분석과 실험에서, 이렇게 만든 sub-THz 신호의 주파수 안정도와 위상 잡음 특성은 보상에 쓴 RF 발진기의 특성으로 제한됨을 보였다.[^p8] | 1저자 K. Woo, 마지막 저자 김훈 (2명) |

## 교수와 전문 분야

김훈 교수는 KAIST 전기및전자공학부 교수이고, 전기및전자공학부 교수 소개는 직위 옆에 「KAIST ICT 석좌교수」를 적는다. 디비전은 Wave와 Communication이고, 주요 연구분야는 Information, Communication & Coding과 Photonics로 적혀 있다.[^eeprof] 반도체시스템공학과 교수진에도 연구실 「광자 시스템 연구실」로 올라 있다.[^ssep]

연구실 교수 소개 페이지에 따르면 교수는 KAIST(Dept. of Electrical Engineering)에서 학사(1994), 석사(1996), 박사(2000)를 받았다. 같은 학과의 Postdoctoral Fellow(2000–2001), Lucent Technologies Bell Laboratories의 Postdoctoral Member of Technical Staff(2001–2002), 삼성전자 Telecommunication R&D Center의 Senior Engineer(2002–2007), NUS Dept. of Electrical & Computer Engineering의 Assistant Professor(2007–2014)를 거쳐 2014년 KAIST 전기및전자공학부 부교수로 왔고, 2023년부터 교수다.[^prof] 학술지 Optics Communications의 Editor(2021년부터)와 IEEE Photonics Technology Letters의 Senior Editor(2018년부터)를 맡고 있고, 앞서 Optics Express(2015–2021)와 IEEE Photonics Technology Letters(2008–2018)의 Associate Editor를 지냈다. OECC, ACP, CLEO-PR, ICOCN, COIN의 기술 프로그램 위원회 분과 위원장과 OFC, ECOC, OECC, IPC, ACP, COIN, IPOC, PGC의 기술 프로그램 위원을 맡았다.[^prof] 2025년 2월 Optical Society of Korea의 Haerim Photonics Award를 받았다고 누리집 소식이 알린다.[^home]

전기및전자공학부 교수 소개가 대표 업적으로 드는 다섯 편은 2002–2012년 논문(스펙트럼 분할 비간섭 광원 기반 파장 분할 광 가입자망, 반사형 반도체 광증폭기의 10 Gb/s 동작, DPSK 시스템의 비선형 위상 잡음, 마흐-젠더 변조기의 처프 특성 등)으로, KAIST 부임 전 시기의 연구다.[^eeprof]

논문으로 보면 KAIST에서의 전문 분야는 세 갈래다. 대기 난류와 빔 정렬·포착을 다루는 자유공간 광통신(대표 논문 1, 2, 3),[^p1][^p2][^p3] 데이터센터 연결과 광 가입자망을 위한 광섬유 전송의 등화·변조(대표 논문 4, 5, 6),[^p4][^p5][^p6] 레이저 헤테로다인으로 만드는 sub-THz 무선 신호(대표 논문 7, 8)다.[^p7][^p8] 최근 논문 목록의 초청 강연 항목은 셀룰러 이동통신을 위한 FSO 기술, 위성 간 링크와 자유공간 광통신을 위한 적응 빔 제어·빔 조향, 광 단측파대 송신기, 직접 변조 레이저 전송의 비선형 전기 등화를 주제로 한다.[^pubs]

## 응용 분야

Research 페이지는 FSO를 위성끼리 잇는 링크와 위성과 광 지상국을 잇는 링크에 쓰는 예를 들고, 광섬유 전송 연구를 광 가입자망·데이터센터 네트워크·광 컴퓨트 인터커넥트에, sub-THz 기술을 6G 이후 이동통신에 겨냥한다.[^research] 대표 논문으로는 레이저 위성 간 링크의 포착 시간(대표 논문 3), 하이브리드 데이터센터 연결용 200 Gb/s 전송(대표 논문 4), 코히어런트 광 가입자망의 상향 전송(대표 논문 5), 132 GHz 무선 전송(대표 논문 7)이 있다.[^p3][^p4][^p5][^p7] 최근 논문 목록에는 차세대 셀룰러 이동통신을 위한 FSO 기술을 다룬 IEEE Communications Magazine 글(2024)과 낮은 레이더 반사 면적 표적을 찾는 광자 레이더 현장 실험(2021)도 있다.[^pubs]

## 구성원

연구실 누리집 People 페이지의 박사후연구원 1명, 박사과정 9명, 석박사통합과정 1명, 석사과정 2명이다.[^people] 과정은 페이지 표기이고, 박사과정 한 명은 Lab captain으로 적혀 있다. 이름 옆 괄호는 페이지가 함께 적은 국문 이름이다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Jaeyoon Kim (김재윤) | 박사후연구원 | 4 |
| Gihong Park (박기홍) | 박사과정 |  |
| Keunjae Lee (이근재) | 석박사통합과정 |  |
| Sungjae Kim (김성재) | 박사과정 |  |
| Mincheol Kim (김민철) | 박사과정 |  |
| Woohyeon Moon (문우현) | 박사과정 (Lab captain) | 1, 2 |
| Seokjun Yun (윤석준) | 박사과정 |  |
| Horyun Lee (이호륜) | 박사과정 |  |
| Jinbae Park (박진배) | 박사과정 |  |
| Seyun Oh (오세윤) | 박사과정 |  |
| Gyuwan Kim (김규완) | 박사과정 |  |
| Hyungwoo Kim (김형우) | 석사과정 |  |
| Heeseung Kim (김희승) | 석사과정 |  |

## 졸업생과 이전 구성원

누리집 People 페이지 Alumni 절의 박사후연구원 3명, 박사 9명, 석사 13명이다. 학위 연도는 적혀 있지 않고, 진로는 누리집 표기 그대로다. 이름 옆 괄호는 페이지가 함께 적은 국문 표기다. 석사 졸업생 Gyuwan Kim(김규완)은 현재 박사과정 구성원으로도 올라 있다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Yukui Yu (유쿠이) | Postdoctoral Fellow | Xidian University |
| Tianwai Bo (티안아이) | Postdoctoral Fellow | Beijing Institute of Technology |
| Vuong Mai (마이) | Postdoctoral Fellow | University of Bradford |
| Daeho Kim (김대호) | Ph.D. | Samsung Electronics System LSI Division |
| Daeseong Lee (이대성) | Ph.D. | Samsung Electronics Mobile Division |
| Jongwan Kim (김종완) | Ph.D. | Electronics and Telecommunications Research Institute |
| Kwanyong Lee (이관용) | Ph.D. | Samsung Electronics Mobile Division |
| Numan Kifayat (뉴먼) | Ph.D. | Aston University |
| Kyungmin Woo (우경민) | Ph.D. | Electronics and Telecommunications Research Institute |
| Jihoon Lee (이지훈) | Ph.D. | Samsung Electronics Mobile Division |
| Mat Nguyen Thi (맛) | Ph.D. | University of Bradford |
| Yi Che (차이) | Ph.D. | Baidu |
| Prasetiyo (프라스) | Master | CastLab |
| Zonglong He (종롱) | Master | Chalmers University of Technology |
| Myeongryeol Choi (최명렬) | Master | Samsung Electronics Mobile Division |
| Dung Trung Ha (하) | Master | University of Illinois at Chicago |
| Sunghyun Moon (문성현) | Master | TmaxSoft |
| Hanul Yeon (연한울) | Master | Samsung Electronics |
| Chuanbowen Sun (쑨) | Master | University of Melbourne |
| Gyuwan Kim (김규완) | Master |  |
| Seokyoung Yoon (윤석영) | Master |  |
| Xi Jiang (강희) | Master | China Mobile Communications Corporation |
| Arman Lee (이아르만) | Master | Univeristy College Cork |
| Vu Thi Thanh Ngoc (응옥) | Master | VINIFAST |
| Dohun Koh (고도훈) | Master | Korea Advanced Institute of Science and |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지의 2021–2026년 연도 구역 147건이다. International Journals 36편, International Conferences 46건, Domestic Journals 4편, Domestic Conferences 61건이고, 연도마다 이 순서로 적었다. International Conferences 46건 가운데 16건은 누리집이 (invited talk)로 표시한 초청 강연이고, International Journals 2편은 (Invited paper)로 표시돼 있다. 저자 순서와 제목·학술지·학회 표기는 누리집 그대로이며, 교수가 마지막 저자가 아닌 공동연구 논문도 목록대로 실었다.[^pubs]

**2026**

- J. Kim and H. Kim. "Fast-converging Volterra equalizer using mini-batch gradient descent-based Adam optimization". *IEEE Photon. Technol. Lett., vol. 38, no. 17, pp. 1183-1186, Sep. 2026*.
- J. Lee, K. Woo, and H. Kim. "Suppression of optical power leakage through IQ modulator bias control in upstream coherent PON". *IEEE Photon. Technol. Lett., vol. 38, no. 12, pp. 783-786, Jun. 2026*.
- W. Moon and H. Kim. "Scintillation index of arbitrary vector beams in atmospheric turbulence". *Opt. Lett., vol. 51, no. 1, pp. 61-64, Jan. 2026*.
- G. Park and H. Kim. "Intelligent reflecting surface-assisted pointing, acquisition, and tracking algorithm for cellular FSO communication". *OECC 2026, Busan, Korea, July. 2026*.
- Y. Che and H. Kim. "Real-valued modulation and single-sideband filtering for heterodyne detected PONs". *OECC 2026, Busan, Korea, July. 2026*.
- J. Park and H. Kim. "Turbulence-resilient channel configuration of mode-division multiplexed system using mode diversity with a limited mode pool". *OECC 2026, Busan, Korea, July. 2026*.
- D. Koh, K. Woo, and H. Kim. "Sub-THz signal generation using optical heterodyne detection of cavity-locked lasers and receiver DSP". *OECC 2026, Busan, Korea, July. 2026*.
- J. Kim and H. Kim. "Mini-batch gradient descent adam algorithm for fast-converging volterra equalizers". *OECC 2026, Busan, Korea, July. 2026*.
- S. Oh and H. Kim. "Dynamic adaptive beam control using a variable-focus liquid lens for free-space optical systems". *OECC 2026, Busan, Korea, July. 2026*.
- W. Moon and H. Kim. "Do vector beams outperform scalar beams in reducing scintillation index?". *OECC 2026, Busan, Korea, July. 2026*.
- Nguyen Thi Mat, W. Moon, and H. Kim. "Experimental comparison between quadrant detector and photodetector array for fast beam tracking in FSOC". *OECC 2026, Busan, Korea, July. 2026*.
- 박기홍, 김 훈. "셀룰러 FSO 이동통신을 위한 지능형 반사 표면 기반 PAT 알고리즘". *제 33회 광전자 및 광통신 학술대회, 부산 한화리조트, 2026년 5월*.
- 박진배, 김 훈. "OAM 모드 수가 제한된 환경에서 대기 난류 채널을 통과하는 모드 분할 다중화 무선 광통신 시스템의 모드 다이버시티 성능 비교". *제 33회 광전자 및 광통신 학술대회, 부산 한화리조트, 2026년 5월*.
- Nguyen Thi Mat, 문우현, 김 훈. "Experimental comparison between quadrant detector and photodetector array for fast beam tracking in FSOC". *제 33회 광전자 및 광통신 학술대회, 부산 한화리조트, 2026년 5월*.
- 문우현, 김 훈. "벡터 빔과 스칼라 빔의 대기 난류에 대한 강건성 비교". *제 33회 광전자 및 광통신 학술대회, 부산 한화리조트, 2026년 5월*.
- 문우현, 김 훈. "Minimum link distance of terrestrial testbed for emulating satellite-to-ground free-space optical links". *2026 한국우주과학회 봄 학술대회, 여수 소노캄, 2026년 5월*.

**2025**

- K. Lee and H. Kim. "Millimeter-wave mobile fronthaul system incorporating IF data transmission and remote LO delivery based on polarization multiplexing and single photo-detector". *Opt. Commun., vol. 593, 132298, Nov. 2025*.
- M. T. Nguyen, W. Moon, and H. Kim. "Beam position estimation method for fast beam tracking in free-space optical systems using a quadrant detector". *Opt. Lett., vol. 50, no. 20, pp. 6441-6444, Oct. 2025*.
- W. Moon and H. Kim. "Minimum link distance of terrestrial testbeds required to simulate the satellite-to-ground FSO communication links". *IEEE. Photonics. J., vol. 17, no.5, pp. 1-11, Oct. 2025*.
- K. Woo, M. T. Nguyen, and H. Kim. "Photonics-based wireless transmission of 16-QAM signals using feedforward compensation of the frequency and phase noise of free-running lasers". *Opt. Lett., vol. 50, no. 17, pp. 5506-5509, Aug. 2025*.
- H. Lee and H. Kim. "Transmission of 100-Gb/s PAM-6 signal by using DML wavelength-locked to delay interferometer". *IEEE. Photonics. J., vol. 17, no. 5, pp. 1-7, Oct. 2025*.
- J. Lee and H. Kim. "Generation of pulse-position modulated signals having high extinction ratios via an IQ modulator". *Opt. Express, vol. 33, no. 16, pp. 34924-34938, Aug. 2025*.
- W. Moon and H. Kim. "Standard deviation of coupling efficiency to few mode fiber under atmospheric turbulence". *Opt. Express, vol. 33, no. 13, pp. 27461-27475, Jun. 2025*.
- G. Park and H. Kim. "Probability of exposure of optical receiver to direct sunlight in FSO-based wireless mobile communications". *IEEE Photonics J., vol. 17, no. 2, pp. 1-11, Apr. 2025*.
- J. Kim and H. Kim. "Impact of receiver bandwidth on the performance of nonlinear volterra equalizer in IM/DD systems". *Opt. commun., vol. 575, no. 131288, Jan. 2025*.
- K. Woo and H. Kim. "Feedforward compensation of frequency drift and phase noise of sub-THz signal in optical heterodyne technique". *ACP 2025, Suzhou, China, Nov. 2025*.
- K. Woo and H. Kim. "Wireless D-band transmission of 80-Gb/s 16-QAM signal generated by using feedforward compensation of free-running lasers' phase and wavelength fluctuations". *OECC 2025, Sapporo, Japan, July. 2025, paper WG3-2*.
- K. Lee and H. Kim. "Simultaneous transmission of IF and LO signals by using polarization multiplexing and single photodetector for mobile fronthaul network". *OECC 2025, Sapporo, Japan, July. 2025, paper TuA3-4*.
- J. Kim and H. Kim. "100-Gbaud PAM-4 transmission using a sub-rate sampled, non-integer fractionally spaced Volterra equalizer". *OECC 2025, Sapporo, Japan, July. 2025, paper TuB1-3*.
- H. Lee and H. Kim. "100-Gb/s PAM-6 transmission using directly modulated laser wavelength-locked to delay interferometer-based optical equalizer". *OECC 2025, Sapporo, Japan, July. 2025, paper WD2-3*.
- W. Moon and H. Kim. "Standard deviation of free-space to few-mode-fiber coupling efficiency under atmospheric turbulence". *OECC 2025, Sapporo, Japan, July. 2025, paper MH1-3*.
- M. T. Nguyen and H. Kim. "Experimental demonstration of fast beam tracking in free-space optical system using a quadrant detector". *OECC 2025, Sapporo, Japan, July. 2025, paper ThA1-2*.
- H. Kim. "Cellular mobile communications using FSO technologies". *(invited talk) IEEE Summer Optical Meeting Series, Berlin, Germany, July. 2025*.
- H. Kim. "Adaptive beam control techniques for free-space optical communications". *(invited talk) SPPCom, Optica Advanced Photonics Congress, Marseille, France, July. 2025*.
- J. Lee and H. Kim. "Generation of high-extinction-ratio PPM signals using a single IQ modulator". *OFC 2025, San Francisco, California, USA, Apr. 2025,paper Th3J.2*.
- S. Yun, Y.-T. Han, D.-H. Lee, D.-H. Lee, S.-Y. Lee, Y.-K. Choi, J.-U. Shin, S.-H. Park, H. Kim, and Y. Baek. "Enhancement of RF performance of 128-Gbaud lumped EML submodule utilizing LC resonance with capacitive wire-bonding pad". *OFC 2025, San Francisco, California, USA, Apr. 2025, paper W2A.2*.
- 김 훈. "자유공간 광통신 기술". *한국광학회지, 제 36 권, 제 6호, pp. 304-313, 2025년 12월*.
- 이지훈, 김 훈. "IQ 변조기 바이어스 제어를 통한 TDM 상향 코히어런트 PON 누설 전력 억제". *2025 광자기술 학술회의, 평창 휘닉스파크, 2025년 11월*.
- Arman, 김 훈. "Experimental study on optical modulation formats for 100-Gb/s IM/DD passive optical network". *2025 광자기술 학술회의, 평창 휘닉스파크, 2025년 11월*.
- 박진배, 김 훈. "모드 분할 다중화 방식 무선 광통신 시스템에서 대기 외란에 저항성을 가진 OAM 모드 다이버시티 조합 선별". *2025 광자기술 학술회의, 평창 휘닉스파크, 2025년 11월*.
- 김재윤, 김 훈. "볼테라 비선형 등화기를 위한 미니배치 경사하강법 기반 Adam 알고리즘". *2025 광자기술 학술회의, 평창 휘닉스파크, 2025년 11월*.
- 고도훈, 우경민, 김 훈. "광공진기에 파장 잠금된 레이저를 이용한 광 헤테로다인 검출 방식 sub-THz 신호 생성". *2025 광자기술 학술회의, 평창 휘닉스파크, 2025년 11월*.
- 오세윤, 김 훈. "무선 광통신을 위한 가변 초점 액체 렌즈 기반 동적 적응형 빔 제어 기술 실험". *2025 광자기술 학술회의, 평창 휘닉스파크, 2025년 11월*.
- Y. Che, 김 훈. "Single-Sideband Filtering Technique for 100-Gb/s/lambda Coherent Heterodyne Passive Optical Networks". *2025 광자기술 학술회의, 평창 휘닉스파크, 2025년 11월*.
- 문우현, 김 훈. "대기 난류를 통과한 임의의 벡터 빔의 신틸레이션 지수". *2025 광자기술 학술회의, 평창 휘닉스파크, 2025년 11월*.
- 이호륜, 김재윤, 김 훈. "1 Tb/s (8×136 Gb/s) 다중 모드 광섬유 300 m 전송 실험". *2025 광자기술 학술회의, 평창 휘닉스파크, 2025년 11월*.
- 윤석준, 한영탁, 이동훈, 이동효, 이서영, 최영규, 신장욱, 박상호, 김 훈, 백용순. "Capacitive wire-bonding pad 기반의 LC 공진효과를 이용한 EML 서브모듈의 고주파 특성 개선". *Optics and Photonics Congress 2025, 제주 ICC, 2025년 7월*.
- 이호륜, 김 훈. "지연 간섭계에 파장 잠금된 직접 변조 레이저 기반 100 Gb/s PAM-6 신호 전송 실험". *제 32회 광전자 및 광통신 학술대회, 부산 한화리조트, 2025년 5월*.
- Arman Lee, 김 훈. "직접 검출 방식 100 Gb/s 수동형 광통신망을 위한 광변조 방식 연구". *제 32회 광전자 및 광통신 학술대회, 부산 한화리조트, 2025년 5월*.
- 문우현, 김 훈. "FMF 기반 광수신기의 커플링 효율 표준편차". *제 32회 광전자 및 광통신 학술대회, 부산 한화리조트, 2025년 5월*.
- Nguyen Thi Mat, 김 훈. "무선 광통신을 위한 사분면 검출기 기반 고속 빔 위치 추정 알고리즘 실험". *제 32회 광전자 및 광통신 학술대회, 부산 한화리조트, 2025년 5월*.

**2024**

- J. Kim and H. Kim. "Sub-rate sampled, non-integer fractionally spaced Volterra nonlinear equalizer for IM/DD systems". *Opt. Express., vol. 32, no. 15, pp. 26332-26341, Jul. 2024*.
- K. Woo and H. Kim. "Feedforward compensation of laser frequency and phase noise for photonics-based sub-THz generation". *IEEE Photon. Technol. Lett., vol. 36, no. 8, pp. 563-566, Jul. 2024*.
- G. Park, V. Mai, H. Lee, S. Lee, and H. Kim. "Free-space optical communication technologies for next-generation cellular wireless communications". *IEEE Comm. Mag., vol. 62, no. 3, pp. 24-30, Mar. 2024*.
- H. Kim. "Adaptive beam control technique for inter-satellite laser links". *(invited talk) CLEO-PR 2024, Incheon, Korea, Aug. 2024*.
- N. Kifayat and H. Kim. "Sensitivity enhancement through triangular chirped-pulse phase OTDR". *CLEO-PR 2024, Incheon, Korea, Aug. 2024, paper Tu1G-2*.
- J. Lee and H. Kim. "Bounds on the receiver sensitivity of PPM signals having finite extinction ratios". *CLEO-PR 2024, Incheon, Korea, Aug. 2024, paper Th1K-4*.
- M. T. Nguyen and H. Kim. "Improved beam spot position estimation algorithm for quadrant detector in free-space optical communications". *OECC 2024, Melbourne, Australia, July. 2024, paper 324*.
- K. Woo and H. Kim. "Feedforard phase noise compensation of free-running DFB lasers heterodyned for sub-THz generation without optical filtering". *SPPCom 2024, Quebec, Canada, July. 2024, paper 354*.
- G. Park and H. Kim. "FSO technologies for cellular mobile communications". *(invited talk) ICOCN 2024, Harbin, China, July. 2024*.
- H. Kim. "FSO technologies for cellular mobile communications". *(invited talk) Workshop on Optical Wireless Technology in OECC 2024, Melbourne, Australia, June. 2024*.
- 윤석영, 문우현, 김 훈. "대기 난류와 열적 블루밍을 겪는 고출력 레이저 빔의 대기전파 시뮬레이션에 필요한 위상판 개수 분석". *한국광학회지, 제 35 권, 제 2호, pp. 49-60, 2024년 4월*.
- 우경민, 김 훈. "차세대 셀룰러 통신을 위한 포토닉스 기반 sub-THz 대역 신호 송신 시스템". *(초청논문) , 2024 광자기술 학술회의, 평창 휘닉스파크, 2024년 11월*.
- 문우현, 김 훈. "무선 광통신을 위한 부분 코히어런트 빔을 이용한 다중 입력 단일 출력 시스템의 신틸레이션 완화". *2024 광자기술 학술회의, 평창 휘닉스파크, 2024년 11월*.
- 이지훈, 김 훈. "PPM 신호의 수신 감도". *(초청논문) , 2024 광자기술 학술회의, 평창 휘닉스파크, 2024년 11월*.
- 김재윤, 김 훈. "심볼 당 2 샘플 이하, 비정수배 간격 볼테라 비선형 등화기를 사용한 100-Gbaud PAM-4 전송 실험". *2024 광자기술 학술회의, 평창 휘닉스파크, 2024년 11월*.
- 이근재, 김 훈. "편광 분할 다중화와 단일 광검출기를 이용한 IF와 LO 신호의 동시 전송 실험". *2024 광자기술 학술회의, 평창 휘닉스파크, 2024년 11월*.
- 우경민, 김 훈. "광학 필터 없이 서브 테라헤르쯔 신호를 생성하기 위한 헤테로다인 방식 피드포워드 위상 잡음 보상 기술". *제 30회 광전자 및 광통신 학술대회, 부산 한화리조트, 2024년 5월*.
- Nguyen Thi Mat, 김 훈. "무선 광통신을 위한 사분면 검출기 기반 빔 위치 추정 알고리즘". *제 30회 광전자 및 광통신 학술대회, 부산 한화리조트, 2024년 5월*.
- 박기홍, 김 훈. "인공위성-지상 무선 광통신 시스템에서 지상국 수신기에 태양광이 직접 인가될 확률". *제 31회 광전자 및 광통신 학술대회, 부산 한화리조트, 2024년 5월*.
- 이지훈, 김 훈. "유한한 소광비를 가진 PPM 신호의 수신감도의 상한과 하한". *2024 통신정보 합동학술대회, 부산, 2024년 4월*.
- 문우현, 김 훈. "인공위성-지상간 무선 광통신 다운링크 모사를 위한 실험 조건". *2024 통신정보 합동학술대회, 부산, 2024년 4월*.

**2023**

- M. T. Nguyen, V. Mai, and H. Kim. "Time-efficient simulation of free-space optical communication systems under atmospheric turbulence, pointing error, and angle-of-arrival fluctuations". *IEEE Photonics J., vol. 15, no. 6, pp. 1-9, Dec. 2023*.
- K. Lee, V. Mai, and H. Kim. "Acquisition time in laser inter-satellite link under satellite vibrations". *IEEE Photonics J., vol. 15, no. 4, Aug. 2023*.
- W. Moon and H. Kim. "Standard deviation of fiber-coupling efficiency for free-space optical communication through atmospheric turbulence". *IEEE Photonics J., vol. 15, no. 3, Jun. 2023*.
- J. Lee and H. Kim. "Receiver sensitivity of type-I return-to-zero signals having finite extinction ratios". *Opt. Express, vol. 31, no. 9, pp. 13724-13738, Apr. 2023*.
- D. Kim and H. Kim. "Capacity-achieving symbol distributions for directly modulated laser and direct detection systems". *Opt. Express, vol. 31, no. 8, pp. 12609-12623, Apr. 2023*.
- T. Bo, H. Kim, Z. Tan, and Y. Dong. "Optical single-sideband transmitters". *J. Lightwave Technol., vol. 41, no. 4, pp. 1163-1174, Feb. 2023*.
- Y. Che and H. Kim. "Cost-effective C-Band 50-Gb/s PON implemented by using a 2-bit DAC and linear electrical equalizer". *IEEE Photon. Technol. Lett., vol. 35, no. 4, Feb. 2023*.
- V. Mai and H. Kim. "Beaconless angle-of-arrival tracking with improved receiver sensitivity and tracking precision for free-space optical communications". *Opt. Commun., vol. 527, 128963, Jan. 2023*.
- V. Mai, K. Lee, and H. Kim. "Applications of adaptive beam control technique for laser satellite communication systems". *(invited talk) PGC 2023, Stockholm, Sweden, Aug. 2023*.
- V. Mai, K. Lee, and H. Kim. "Adaptive beam control for optical inter-satellite communication systems". *(invited talk) ICOCN 2023, Qufu, China, July. 2023*.
- H. Kim and T. Bo. "Compact single side-band transmitter based on dual modulation". *(invited talk) Photonic Network and Devices, Busan, Korea, July. 2023*.
- 이관용, 김 훈. "인공위성 간 광링크를 위한 빔 제어 기술". *(초청논문) , 2023 광자기술 학술회의, 평창 휘닉스파크, 2023년 12월*.
- 김재윤, 김 훈. "서브 나이퀴스트, 비정수배 간격 볼테라 비선형 등화기". *2023 광자기술 학술회의, 평창 휘닉스파크, 2023년 12월*.
- 이지훈, 김 훈. "유한한 소광비를 가진 PPM 신호의 수신 감도". *2023 광자기술 학술회의, 평창 휘닉스파크, 2023년 12월*.
- 문우현, 김 훈. "난류를 통과한 빛의 통계적 특성을 보존하는 위상판 스케일링 조건". *2023 광자기술 학술회의, 평창 휘닉스파크, 2023년 12월*.
- 윤석영, 김 훈. "대기 난류와 열적 블루밍 효과를 포함하는 고출력 레이저의 대기 전파 시뮬레이션에 필요한 위상판 개수". *2023 광자기술 학술회의, 평창 휘닉스파크, 2023년 12월*.
- 이지훈, 김 훈. "임의의 소광비와 듀티 사이클을 가진 Type-I RZ 신호의 수신 감도". *제 30회 광전자 및 광통신 학술대회, 부산 한화리조트, 2023년 5월*.
- Nguyen Thi Mat, Vuong Mai, 김 훈. "시간 효율적인 무선 광통신 시스템 컴퓨터 시뮬레이션". *제 30회 광전자 및 광통신 학술대회, 부산 한화리조트, 2023년 5월*.
- 윤석영, 김 훈. "고출력 레이저의 대기 전파에서 발생하는 열적 블루밍과 대기 외란 효과의 시뮬레이션 구현". *제 30회 광전자 및 광통신 학술대회, 부산 한화리조트, 2023년 5월*.
- 이관용, 김 훈. "위성 간 광 링크의 정렬 습득 시간을 최소화하기 위한 적응형 빔 제어". *제 30회 광전자 및 광통신 학술대회, 부산 한화리조트, 2023년 5월*.
- 이지훈, 김 훈. "Performance analysis of PPM signals having finite extinction ratios in free-space optical communication". *2023 한국우주과학회 봄 학술대회, 창원 컨벤션센터, 2023년 4월*.

**2022**

- J. Lee and H. Kim. "Receiver sensitivity of type-II return-to-zero signals having finite extinction ratios". *Opt. Express, vol. 30, no. 23, pp. 42594-42604, Nov. 2022*.
- V. Mai and H. Kim. "Beam steering and divergence control using variable focus liquid lenses for WDM FSO communications". *IEEE Photon. Technol. Lett., vol. 34, no. 22, pp. 1226-1229, Sept. 2022*.
- J. Kim and H. Kim. "PRBS orders required to train ANN equalizer for PAM signal without overfitting". *Opt. Express, vol. 30, no. 14, pp. 25486-25497, July 2022*.
- K. Lee, V. Mai, and H. Kim. "Dynamic adaptive beam control system using variable focus lenses for laser inter-satellite link". *IEEE Photonics J., vol. 14, no. 4, pp. 1–8, Aug. 2022*.
- D. Lee, V. Mai, and H. Kim. "Mitigation of scintillation in FSO communication using a temporally and spatially incoherent spectrum-sliced light source". *Opt. Lett., vol. 47, no. 9, pp. 2282–2285, May 2022*.
- M. T. Nguyen, V. Mai, and H. Kim. "Multiple-aperture direct-detection receiver based on maximal ratio combining for FSO communication". *IEEE Photon. Technol. Lett., vol. 34, no. 8, pp. 405–408, Apr. 2022*.
- G. Kim and H. Kim. "Link reliability of satellite-to-ground free-space optical communication systems in South Korea". *MILCOM 2022. (Travel Grant Award)*.
- V. Mai and H. Kim. "Beam steering and divergence control using variable focus liquid lenses for free-space optical communication systems". *(invited talk) ACP2022, Shenzhen, China, Nov. 2022*.
- V. Mai and H. Kim. "Non-mechanical beam steering and divergence control based on variable focus lenses for free-space optical communication systems". *(invited talk) SPPCom 2022, Maastricht, Netherland, July. 2022*.
- Y. Che and H. Kim. "Cost-effective 50-Gb/s PAM-4 passive optical network operating at C-band emplemented by using 2-bit DAC and FFE". *OECC 2022, Toyama, Japan, July. 2022, paper WP-A-5*.
- D. Lee, V. Mai, and H. Kim. "Mitigation of scintillation using temporally and spatially incoherent spectrum-sliced light source". *OECC 2022, Toyama, Japan, July. 2022, paper TuP-B-8*.
- V. Mai and H. Kim. "Optical beam control based on variable focus lenses for WDM FSO communications". *(invited talk) CLEO 2022, San Jose, CA, May. 2022*.
- T. Bo, Z. Tan, H. Kim, and Y. Don. "Monolithically integrable optical single sideband transmitters for inter-datacenter applications". *(invited talk) OFC/NFOEC 2022, San diego, CA, Mar. 2022*.
- V. Mai and H. Kim. "Variable Focus Lens-Based Beam Steering and Divergence Control for WDM Free-Space Optical Communication". *OFC 2022, San Diego, CA, Mar. 2022, paper M1C.6*.
- M. T. Nguyen, V. Mai, and H. Kim. "Seven-aperture direct-detection receiver for free-space optical communication systems". *OFC 2022, San Diego, CA, Mar. 2022, paper Th2A.28*.
- 김종완, 김 훈. "직접 검출 시스템을 위한 인공 신경망 기반의 등화기 기술 동향". *주간기술동향, 2076호, 2022년 12월*.
- 김규완, 김대호, Vuong V. Mai, 김 훈. "우리나라 위성-지상 하향 무선 광통신 시스템의 링크 가용성". *한국광학회지, 제 34 권, 제 3호, pp. 113-121, 2022년 6월*.
- 조형준, 김 훈. "디지털 코히어런트 광 수신기를 위한 합성곱 신경망 기반 광 신호 성능 감시 기법 연구". *(초청논문) 2022 광자기술 학술회의, 평창 알펜시아, 2022년 12월*.
- Nguyen Thi Mat, Vuong Mai, 김 훈. "사분면 검출기와 PID 제어를 이용한 무선 광통신 시스템의 대기 난류 영향 완화". *2022 광자기술 학술회의, 평창 알펜시아, 2022년 12월*.
- 조형준, Yi Che, 김종완, 김 훈. "거리 별로 훈련될 필요가 없는 시간적 합성곱 신경망 기반 비선형 등화기". *2022 광자기술 학술회의, 평창 알펜시아, 2022년 12월*.
- 문우현, 김 훈. "광섬유 기반 무선 광통신 수신기의 커플링 효율 표준편차 분석". *2022 광자기술 학술회의, 평창 알펜시아, 2022년 12월*.
- 김규완, 윤석영, 김 훈. "대기 손실 모델을 활용한 위성 하향 무선 광통신 시스템의 링크 신뢰도 분석". *2022 광자기술 학술회의, 평창 알펜시아, 2022년 12월*.
- Vuong Mai, 김 훈. "가변 초점 렌즈 기반 빔 조향 및 발산각 제어 기술의 파장 의존성". *2022 광자기술 학술회의, 평창 알펜시아, 2022년 12월*.
- 이지훈, 김 훈. "유한한 소광비를 가진 Type-I RZ 신호의 수신 감도 하한". *2022 광자기술 학술회의, 평창 알펜시아, 2022년 12월*.
- 김종완, 김 훈. "PAM 신호를 위한 인공 신경망 등화기를 과적합 없이 학습하기 위한 유사 랜덤 이진 시퀀스의 요구조건". *제 29회 광전자 및 광통신 학술대회, 부산 한화리조트, 2022년 5월*.
- Vuong Mai, 김 훈. "무선 광통신 시스템을 위한 비기계식 빔 조향 및 제어 기술". *(초청논문) 제 29회 광전자 및 광통신 학술대회, 부산 한화리조트, 2022년 5월*.
- 김규완, 김대호, Vuong Mai, 김 훈. "우리나라 위성-지상 하향 무선 광통신 시스템의 링크 가용성". *제 29회 광전자 및 광통신 학술대회, 부산 한화리조트, 2022년 5월*.
- 이지훈, 김 훈. "매우 작은 듀티 사이클을 가진 RZ 신호의 수신 감도 하한". *제 29회 광전자 및 광통신 학술대회, 부산 한화리조트, 2022년 5월*.

**2021**

- J. Kim and H. Kim. "Length of Pseudorandom Binary Sequence Required to Train Artificial Neural Network Without Overfitting". *IEEE Access, vol. 9, pp. 125358–125365, 2021*.
- V. V. Mai and H. Kim. "Non-mechanical Beam Steering and Adaptive Beam Control Using Variable Focus Lenses for Free-space Optical Communications". *(Invited paper) J. Lightwave Technol., 2021*.
- Y. Bae, J. Shin, S.-G. Lee, and H. Kim. "Field Experiment of Photonic Radar for Low-RCS Target Detection and High-Resolution Image Acquisition". *IEEE Access, vol. 9, pp. 63559–63566, 2021*.
- G.-T. Gil, J. Y. Lee, H. Kim, and D.-H. Cho. "Comparison of UCA-OAM and UCA-MIMO systems for sub-THz band line-of-sight spatial multiplexing transmission". *J. Commun. Netw., pp. 1–8, 2021*.
- T. Bo, B. G. Kim, Y. Yu, D. Kim, and H. Kim. "Generation of Broadband Optical SSB Signal Using Dual Modulation of DML and EAM". *J. Lightwave Technol., vol. 39, no. 10, pp. 3064–3071, May 2021*.
- V. V. Mai and H. Kim. "Beaconless PAT and adaptive beam control using variable focus lens for free-space optical communication systems". *(Invited paper) APL Photonics, vol. 6, no. 2, p. 020801, Feb. 2021*.
- D. Lee, V. V. Mai, and H. Kim. "Mitigation of Scintillation in FSOC Using RSOA-Based Spectrum-Sliced Incoherent Light". *IEEE Photon. Technol. Lett., vol. 33, no. 5, pp. 227–230, Mar. 2021*.
- T. Bo and H. Kim. "Monolithically integrable optical single sideband transmitter for low-cost, high-density optical interconnects". *(invited talk) Optical Interconnects XXI, Mar. 2021, vol. 11692, p. 1169206*.
- T. Bo, H. Kim, and Y. Dong. "Recent advances in optical sideband transmitters". *(invited talk) ICOCN 2021, Qufu, China, Aug. 2021*.
- V. Mai and H. Kim. "Non-mechanical beam steering and adaptive beam control for free-space optical communications". *(invited talk) ICOCN 2021, Qufu, China, Aug. 2021*.
- Vuong V. Mai and Hoon Kim. "Variable focus lens-based optical beam steering and adaptive beam control techniques for free-space optical communications". *2021 OECC, Hong Kong, July. 2021, p. S4B.7*.
- Y. Yu and H. Kim. "Low-complexity nonlinear electrical equalization for directly modulated laser-based transmission systems". *(invited talk) OECC 2021, Hong Kong, July. 2021*.
- D. Kim and H. Kim. "Optimum symbol distribution of probabilistically shaped PAM signal in amplifier-less IMDD systems". *OECC 2021, Hong Kong, July. 2021. p. M3A.5*.
- T. Bo and H. Kim. "147-Gbps transmission of optical single sideband DMT signal generated by dual modulation of DML and EAM". *OFC 2021, Jun. 2021*.
- Y. Yu, Y. Che, T. Bo, D. Kim, and H. Kim. "Low-complexity, loop-unrolled decision-feedback equalizer for IM/DD system using PAM formats". *OFC 2021, Jun. 2021*.
- 정욱진, 이관일, 박기홍, 김 훈, T. Lien, 이상배. "첩 광섬유 격자를 이용한 30, 40 Gbaud(60, 80 Gb/s) PAM-4 신호의 분산 보상 성능 평가". *2021 광자기술 학술회의, 평창 알펜시아, 2021년 12월*.
- 김종완, 김 훈. "인공 신경망을 과적합 없이 학습하기 위해 요구되는 유사 난수의 길이". *2021 광자기술 학술회의, 평창 알펜시아, 2021년 12월*.
- Yi Che, 김 훈. "2비트 DAC와 선형 등화기를 사용하는 50 Gb/s 광가입자망 전송 실험". *2021 광자기술 학술회의, 평창 알펜시아, 2021년 12월*.
- Vuong Mai, 김 훈. "WDM 무선 광통신 시스템을 위한 가변 초점 렌즈 기반 빔 조향 및 발산각 제어 기술". *2021 광자기술 학술회의, 평창 알펜시아, 2021년 12월*.
- 박기홍, 김 훈. "이동형 무선 광통신 시스템에서 수신기에 태양광이 입사될 확률 분석". *2021 광자기술 학술회의, 평창 알펜시아, 2021년 12월*.
- 이대성, Vuong Mai, 김 훈. "스펙트럼 저미어진 시공간 비가간섭 광원을 이용한 신틸레이션 완화". *2021 광자기술 학술회의, 평창 알펜시아, 2021년 12월*.
- Nguyen Thi Mat, Vuong Mai, 김 훈. "7개 조리개로 구성된 최대율 합기반 수신기를 사용한 무선 광통신 실험". *2021 광자기술 학술회의, 평창 알펜시아, 2021년 12월*.
- 이관용, Vuong Mai, 김 훈. "위성 간 광링크를 위한 적응형 빔 제어 기능이 있는 송수신 광학 시스템 디자인 및 수치적 시뮬레이션 검증". *2021 광자기술 학술회의, 평창 알펜시아, 2021년 12월*.
- 이지훈, 김 훈. "유한한 소광비를 가진 RZ 신호의 수신 감도 하한". *2021 광자기술 학술회의, 평창 알펜시아, 2021년 12월*.
- 이연우, 이관일, 박기홍, 김 훈, 이상배. "첩 광섬유 격자 분산보상기 이용한 40 Gbps 광신호의 분산 보상 성능 평가". *한국광학회 하계학술발표회, 제주 국제컨벤션센터, 2021년 7월*.
- Vuong Mai, 김 훈. "무선 광통신 시스템을 위한 가변 초점 렌즈를 이용한 빔 조향 및 적응 제어 기술". *제 28회 광전자 및 광통신 학술대회, 부산 한화리조트, 2021년 6월*.

## 특허

누리집 Publications 페이지 Patents 절 90건 가운데 2021–2024년 연도 구역의 9건이다(2025–2026년 구역은 없다). 발명자·제목·번호·날짜와 「대한민국 특허」·「대한민국 특허 출원」·「U. S. patent number」 표기는 누리집 그대로다.[^pubs]

- 2024년 12월 16일 · 멀티캐스트 자유 공간 광통신을 위한 빔 조향 장치 및 이를 포함하는 송신기 (발명자 박재돈, 마이베트왕, 김 훈; 상태 대한민국 특허; 번호 10-2744862)
- 2024년 8월 7일 · 비정수배 간격 볼테라 비선형 등화기 및 그 동작 방법 (발명자 김 훈, 김재윤; 상태 대한민국 특허 출원; 번호 10-2024-0105507)
- 2023년 12월 22일 · 저 위상잡음 테라헤르츠 신호 생성을 위한 레이저 위상잡음 상쇄 방법 및 시스템 (발명자 김 훈, 우경민; 상태 대한민국 특허 출원; 번호 10-2023-0189391)
- 2023년 8월 23일 · 광비팅을 이용한 헤테로다인 광검출 시스템에서 포켈스셀을 이용한 빔포밍 시스템 및 방법 (발명자 김 훈, 이근재; 상태 대한민국 특허 출원; 번호 10-2023-0110819)
- 2022년 12월 28일 · 과적합 없이 펄스 진폭 변조 신호로 기계 학습 알고리즘을 학습하기 위한 유사 랜덤 이진 시퀀스의 차수 결정 방법, 이를 수행하는 장치 및 컴퓨터 프로그램 (발명자 김 훈, 김종완; 상태 대한민국 특허 출원; 번호 10-2022-0187315)
- 2022년 5월 31일 · PAM 신호 검출을 위한 복잡도가 낮은 최대 우도 시퀀스 추정 등화기 및 그의 동작 방법 (발명자 김 훈, 유유쿠이; 상태 대한민국 특허; 번호 10-2405741-0000)
- 2022년 4월 7일 · 자유 공간 광통신 시스템에서 빔의 조준을 정렬하기 위한 장치 및 방법 (발명자 박재돈, 마이베트왕, 김 훈; 상태 대한민국 특허; 번호 10-2385865-0000)
- 2021년 12월 22일 · 광 주입 고정 기반 sub-THz 대역 주파수 안정화 장치 (발명자 김 훈, 우경민; 상태 대한민국 특허 출원; 번호 10-2021-0184572)
- Mar. 30, 2021 · Apparatus and method for nonlinear equalization based on absolute operation (발명자 H. Kim and Y. Yu; 상태 U. S. patent number; 번호 US10,965,380 B1)

## 소식

누리집 첫 화면 News에 오른 2024년 2월–2026년 3월 글이다. 날짜와 문장은 게시된 그대로다.[^home]

- 2026-03-03 · Gyuwan joined our lab.
- 2025-11-28 · Seyun was honored with the Best Paper Award in PC2025.
- 2025-07-03 · Kyungmin and Jaeyoon won the Best Paper Award and Best Student Paper Award in OECC2025, respectively.
- 2025-05-30 · Horyun was honored with the Best Paper Award in COOC2025.
- 2025-02-24 · Hyungwoo and Heeseung joined our lab.
- 2025-02-13 · Prof. Kim received the prestigious Haerim Photonics Award from the Optical Society of Korea.
- 2024-11-29 · Woohyeon and Jaeyoon won the Best Paper Awards in PC2024.
- 2024-11-18 · Gihong won the Excellent Paper Award in KAIST.
- 2024-08-01 · Jaeyoon won the Student Paper Award in APC2024.
- 2024-05-01 · Kyungmin was honored with the Best Paper Award in COOC2024.
- 2024-02-26 · Seokjun, Jinbae, Dohun, Seyun, and Ngoc joined our lab.

## 연락과 위치

- 주소: Building E3-2, Room 4204, School of Electrical Engineering, KAIST, 291 Daehak-ro Yuseong-gu, Daejeon 34141[^home]
- 전화: +82-42-350-7433, 팩스 +82-42-350-3410[^prof]
- 교수 이메일: hoonkim@kaist.ac.kr[^eeprof]
- 첫 화면 Join Us는 광자 시스템·부분 시스템과 광 전송 시스템에 관심 있는 석사·박사과정 학생을 찾고, 자유공간 광통신과 대용량 전송 시스템을 연구할 박사후연구원 자리가 있다고 안내한다.[^home]
[^p1]: W. Moon, H. Kim, Optics Letters 51, 61 (온라인 2025-12-18). <https://doi.org/10.1364/ol.580752> 초록 기준.
[^p2]: M. T. Nguyen, W. Moon, H. Kim, Optics Letters 50, 6441 (온라인 2025-10-15). <https://doi.org/10.1364/ol.576243> 초록 기준.
[^p3]: K. Lee, V. Mai, H. Kim, IEEE Photonics Journal 15, 1-9 (2023). <https://doi.org/10.1109/jphot.2023.3291807> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: J. Kim, H. Kim, IEEE Photonics Technology Letters 38, 1183-1186 (2026). <https://doi.org/10.1109/lpt.2026.3682670> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. Lee, K. Woo, H. Kim, IEEE Photonics Technology Letters 38, 783-786 (2026). <https://doi.org/10.1109/lpt.2026.3669146> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: D. Kim, H. Kim, Optics Express 31, 12609 (온라인 2023-03-31). <https://doi.org/10.1364/oe.484104> 초록 기준.
[^p7]: K. Woo, M. T. Nguyen, H. Kim, Optics Letters 50, 5506 (온라인 2025-08-29). <https://doi.org/10.1364/ol.568731> 초록 기준.
[^p8]: K. Woo, H. Kim, IEEE Photonics Technology Letters 36, 563-566 (2024). <https://doi.org/10.1109/lpt.2024.3379496> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 광자 시스템 연구실 누리집 첫 화면 <https://psrl.kaist.ac.kr/> (Welcome, News, Join Us, Contact Us, 2026-10-23 열람)
[^research]: 광자 시스템 연구실 누리집 Research 페이지 <https://psrl.kaist.ac.kr/psrl_research.html> (Free-space optical communication systems, Fiber-optic transmission systems, Photonics-based sub-THz technology for 6G and beyond, 2026-10-23 열람)
[^people]: 광자 시스템 연구실 누리집 People 페이지 <https://psrl.kaist.ac.kr/psrl_people.html> (Professor, Postdoctoral Fellow, Graduate Students, Alumni, 2026-10-23 열람)
[^prof]: 광자 시스템 연구실 누리집 교수 소개 페이지 <https://psrl.kaist.ac.kr/professor_profile.html> (Education, Professional Experience, Professional Activities, 연락처, 2026-10-23 열람)
[^pubs]: 광자 시스템 연구실 누리집 Publications 페이지 <https://psrl.kaist.ac.kr/psrl_publications.html> (International Journals, International Conferences, Domestic Journals, Domestic Conferences, Patents; 목록 범위는 근거 페이지, 2026-10-23 열람)
[^eeprof]: KAIST 전기및전자공학부 교수 소개(김훈) <https://ee.kaist.ac.kr/professor/12356/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 이메일, 디비전, 학위, 대표업적, 2026-10-23 열람)
[^ssel]: KAIST 반도체시스템공학과 연구실 목록 <https://sse.kaist.ac.kr/research-laboratory/> (광자 시스템 연구실 항목, 2026-10-23 열람)
[^ssep]: KAIST 반도체시스템공학과 교수진 <https://sse.kaist.ac.kr/professor/> (김훈 교수 항목, 2026-10-23 열람)

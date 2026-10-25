# 고성능 집적마이크로시스템 연구실 (Jerald Yoo Group)

**서울대학교 공과대학 전기·정보공학부 · 유담 교수**

- 분야: 의생명 응용을 위한 저전력 집적회로와 시스템(생체 신호 측정 회로와 데이터 변환기, 착용형 건강 관리 SoC와 칩 안 기계학습(on-chip machine learning)), 인체영역네트워크(몸을 통한 통신과 전력 전송)와 에너지 자율 센서, 드론·의료용 초음파 회로와 시스템, 이징 머신 같은 차세대 계산 회로
- 대분야: 전기전자·반도체·광학
- 태그: 집적회로 설계[^project][^ecelabv][^p1], 착용형 생체 센서[^profile][^p2], 에너지 하베스팅[^p2][^p3]
- 홈페이지: <https://www.jeraldyoo.com>
- 근거와 출처: [고성능 집적마이크로시스템 연구실 근거 페이지](jeraldyoo-sources.md)

> 의생명 응용을 위한 에너지 효율 높은 집적회로와 시스템을 만드는 연구실이다. 착용형 건강 관리용 저전력 칩과 생체 신호 측정 회로, 사람의 몸을 통로로 데이터와 전력을 보내는 인체영역네트워크, 초음파 센서를 위한 전용 칩, 최적화 문제를 푸는 이징 머신 같은 차세대 계산 회로를 연구한다.[^project][^ecelabv][^profile][^p2][^p4][^eceen]

## 무엇을 연구하나

연구실은 서울대학교 전기·정보공학부 유담(Jerald Yoo) 교수가 이끈다. 학과 연구실 목록은 연구실을 국문 「고성능 집적마이크로시스템 연구실」, 영문 "Integrated Microsystems Laboratory"로 올리고, 교수 누리집은 연구실을 "Jerald Yoo Group"(Yoo group)이라 부른다.[^ecelabv][^profile][^project] 누리집은 연구의 초점을 의생명 응용을 위한 에너지 효율 높은 집적회로(IC, 여러 전자 소자와 배선을 반도체 칩 하나에 함께 만든 회로)와 시스템의 개발에 둔다고 적고, 진행 중인 과제로 착용형 건강 관리용 저전력 SoC(System-on-Chip, 시스템을 이루는 여러 기능을 칩 하나에 모은 집적회로), 유연 회로 기판(휘어지는 재료로 만든 회로 기판) 플랫폼, 통신과 전력 공급을 위한 인체영역네트워크(BAN, Body Area Network, 몸 위나 몸 안, 몸 둘레의 기기들을 잇는 통신망) 송수신기, pMUT(piezoelectric Micromachined Ultrasonic Transducer, 압전 박막이 붙은 얇은 막의 진동으로 초음파를 내고 받는 미세 가공 변환기)용 ASIC(Application-Specific Integrated Circuit, 특정 용도에 맞춰 설계한 집적회로)를 든다.[^project] 학과 연구실 소개는 최근 관심분야를 집적회로 및 시스템, 바이오메디컬용 회로 및 시스템과 머신러닝, 드론 및 의료용 초음파 회로 및 시스템, 인체영역네트워크(통신 및 전력전송), 차세대 컴퓨팅 회로 및 시스템의 다섯 줄로 적는다.[^ecelabv] 학과 연구실 목록에서 연구실은 생체전자정보, 인공지능 및 머신러닝, 집적회로, 회로 및 시스템의 네 연구그룹에 올라 있다.[^ecelab]

첫째 갈래는 **생체 신호를 재는 회로와 착용형 건강 관리 칩**이다. 교수 소개는 지금의 연구 관심으로 착용형 생체 신호 센서를 위한 저에너지 회로 기술과, 착용형 건강 관리 응용을 위한 SoC를 설계에서 시스템 구현까지 다루는 일을 든다.[^profile] 누리집 과제 목록에는 기계학습을 쓰는 환자 맞춤형 착용형 건강 관리·발작 검출 SoC가 있다.[^project] 대표 논문에서는 ADC(Analog-to-Digital Converter, 아날로그 신호를 디지털 값으로 바꾸는 회로) 가운데 한 주기에 2비트씩 변환하는 순환형 ADC(같은 회로를 되풀이해 쓰며 남은 값을 차례로 디지털로 바꾸는 ADC)로 변환 속도를 두 배로 높이면서 커패시터 수를 50% 줄였다.[^p1] 최근 논문 목록에는 입력 범위가 전원 전압 양 끝까지 닿고(rail-to-rail) 입력 임피던스를 스스로 높인 생체 신호 측정용 ADC(IEEE JSSC 2025), 여러 채널의 생체 전위(세포 활동으로 몸에 생기는 전기 신호)를 함께 기록하는 계측 증폭기(두 입력 사이의 전압 차이를 키우고 두 입력에 함께 실린 전압은 억누르는 증폭기), 뇌전도(EEG, 뇌의 전기 활동을 기록한 신호)로 뇌전증(발작이 되풀이되는 뇌 질환) 환자의 상태를 추적하는 SoC, 발작 검출용 합성곱 신경망(CNN, Convolutional Neural Network, 합성곱 연산으로 자료의 특징을 뽑는 신경망) 처리기도 있다.[^pubs]

둘째 갈래는 **인체영역네트워크와 에너지 자율 센서**다. 교수 소개는 교수가 통신과 전력 공급을 위한 인체영역네트워크 송수신기와, 평면 회로 기판 P-FCB(planar-fashionable circuit board)를 쓴 착용형 인체 센서 네트워크 연구를 개척했다고 적는다.[^profile] 누리집 과제 목록은 이 갈래를 인체 결합 통신·전력 공급(사람의 몸을 신호와 전력이 지나는 통로로 쓰는 방식)으로 에너지 효율을 높인 인체영역네트워크로 적는다.[^project] 대표 논문에서는 몸의 여러 곳에 둔 에너지 하베스터(주변 환경의 에너지를 모아 전기로 바꾸는 장치)의 전력을 몸을 통해 가슴의 심전도(ECG, 심장의 전기 활동을 시간에 따라 기록한 신호) 센서로 보내 배터리 없이 동작하는 피부형 센서 SkinECG를 만들었고,[^p2] 몸에 결합되는 50/60Hz 전자기파와 열전(온도 차이로 전기가 생기거나 전류로 온도 차이가 생기는 현상), 유기 태양전지에서 동시에 에너지를 모으는 칩을 만들어 스스로 얻은 전력만으로 근전도(EMG, 근육의 전기 활동을 기록한 신호)와 심전도를 재 보였다.[^p3]

셋째 갈래는 **초음파 영상 회로**다. 누리집 과제 목록은 pMUT 초음파 응용을 위한 ASIC를 들고, 학과 연구실 소개는 이 갈래를 드론 및 의료용 초음파 회로 및 시스템으로 적는다.[^project][^ecelabv] 대표 논문에서는 무인 항공기의 3차원 깊이 감지를 위해 저주파와 고주파 두 대역의 초음파 영상을 SoC 하나에 넣어 각도 해상도를 높이고, 날고 있는 드론에서 7m 거리로 동작함을 보였다.[^p4] 최근 논문 목록에는 드론용 초음파 영상 센서 SoC(ISSCC 2022), 칩 안에서 영상의 점마다 수신 빔을 모으는 초음파 영상 시스템(IEEE JSSC 2022), 초음파 영상 시스템용 14V 승압 변환기(IEEE SSC-L 2023)도 있다.[^pubs]

넷째 갈래는 **이징 머신과 차세대 계산 회로**다. 영문 교수 소개는 이 갈래를 비전통 컴퓨팅을 위한 회로와 시스템(Circuits and Systems for Non-Traditional Computing)으로 적는다.[^eceen] 이징 머신은 조합 최적화 문제(유한한 선택지들의 조합 가운데 목적에 가장 맞는 것을 찾는 문제)를 서로 영향을 주고받는 스핀(두 값 가운데 하나를 갖는 변수)들의 배치 문제(이징 모형)로 바꾸어, 에너지가 가장 낮은 배치를 찾는 방식으로 푸는 계산 장치다. 최근 논문 목록에는 다시 구성할 수 있고 문제마다 조정이 필요 없는 에너지 피드백 어닐링(무작위성을 차츰 줄여 가며 에너지가 낮은 상태를 찾아가는 방법)을 쓰는 64K 스핀 이징 머신(A-SSCC 2024)과, 12방향(12-Way) 주입 고정 발진기(밖에서 넣은 신호에 주파수와 위상이 맞춰지는 발진 회로)로 스핀을 3차원으로 잇는 CMOS(Complementary Metal-Oxide-Semiconductor, p형과 n형 트랜지스터를 짝지어 쓰는 집적회로 기술) 이징 머신(A-SSCC 2024, IEEE TCAS-I 2026)이 있고, 메모리 안에서 계산하는 영상 처리 가속기(IEEE JSSC 2026), 우주용 방사선 내성 CMOS 영상 센서(ISSCC 2026), 다층 뇌-컴퓨터 인터페이스 시스템 설계를 평가하는 시뮬레이션 틀(ASPLOS 2026)처럼 교수가 공저자로 참여한 논문도 있다.[^pubs]

## 주요 연구 주제

### 1. 생체 신호 측정 회로와 데이터 변환기

고속 순환형 ADC와 생체 신호 측정용 ADC, 착용형 건강 관리·발작 검출 SoC(대표 논문 1).[^p1][^pubs][^project]

### 2. 인체영역네트워크와 에너지 자율 센서

몸을 통해 전력을 받는 피부형 심전도 센서(SkinECG), 여러 에너지원에서 동시에 전력을 모으는 칩(대표 논문 2, 3).[^p2][^p3]

### 3. 초음파 영상 회로

pMUT 초음파 센서용 ASIC, 무인 항공기용 두 대역 초음파 영상 SoC(대표 논문 4).[^project][^p4]

### 4. 이징 머신과 차세대 계산 회로

다시 구성할 수 있는 이징 머신, 스핀을 3차원으로 잇는 CMOS 이징 머신.[^eceen][^pubs]

## 대표 논문

유담 교수가 서울대에 부임한 2024년 3월 뒤 출판된 논문 가운데 교수가 마지막 저자이고 학술지·학회 서지 기록이 교수 소속을 서울대로 적으며 초록을 구할 수 있는 논문 네 편을 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [A 13-bit 70-MS/s SAR-Assisted Cyclic ADC With Charge-Reused 2-bit/Cycle Operation](https://doi.org/10.1109/tcsi.2026.3690163) · IEEE Transactions on Circuits and Systems I: Regular Papers | 에너지 효율이 높은 13비트 고속 SAR(축차 비교형, 기준 전압과의 비교를 되풀이해 한 비트씩 값을 정하는 방식) 보조 순환형 ADC를 만들었다. 첫 단의 6비트 SAR ADC가 입력 신호를 거칠게 양자화(연속된 값을 정해진 단계 값으로 나타냄)하고, 뒤의 순환형 ADC가 전하를 다시 쓰며 한 주기에 2비트씩 변환해 변환 속도를 두 배로 높이면서 커패시터 수를 50% 줄였다. 비교기 잡음을 억누르는 회로와 순환형 ADC가 소자 불일치에 강한 성질 덕분에 단 사이 증폭 이득이 2배면 충분해, 증폭기 설계 부담을 크게 덜고 증폭기의 전고조파 왜곡(THD, 입력 주파수의 정수배 성분 세기를 합해 기본 성분 세기와 견준 값)을 개선했다. 40나노미터 CMOS 공정으로 만든 칩은 보정 없이 초당 7천만 번(70MS/s) 변환하며 13비트 분해능을 냈고, SNDR(신호 세기와 잡음·왜곡 세기의 비) 66.5dB, SFDR(신호 세기와 그 밖의 성분 가운데 가장 큰 것의 세기의 비) 80.1dB에 전력은 0.88mW였다. 잰 칩 9개 사이 SNDR 차이가 1dB 미만이어서 편차에 강함을 보였다.[^p1] | 1저자 R. Jiang, 마지막 저자 유담 |
| 2 | 2026 | [SkinECG: An orthogonal remote powering wearable skin-like sensor](https://doi.org/10.1126/sciadv.aec9803) · Science Advances | 사물인터넷(IoT, Internet of Things, 사물에 센서와 통신 기능을 넣어 인터넷으로 잇는 기술) 시대에 몸에 지니는 착용형 기기가 크게 늘었고, 기기마다 오래 동작할 전원이 필요하다. 그러나 배터리는 닳아 갈아야 하고, 에너지 하베스팅은 몸의 어느 자리에 두느냐에 따라 효과가 다르다. 이 연구는 피부형(skin-like) 심전도 센서 SkinECG를 만들고, 몸의 여러 자리에 그 자리에 알맞은 에너지 하베스터를 두어 얻은 전력을 인체 결합 전력 공급(BCP, body-coupled powering)으로 센서에 보내 하베스터 자리와 센서 자리가 어긋나는 문제를 풀었다. 원격 직교 에너지 하베스팅 네트워크(O-EHN)는 여러 하베스터의 전력을 노드 사이의 간섭과 상쇄 없이 전달한다. 두께 0.71mm의 유연한 SkinECG가 사람 가슴에 밀착해 번거로운 배터리나 직접 연결한 전원 없이 심전도를 재, 오랜 건강 감시에 쓸 수 있음을 보였다.[^p2] | 공동 1저자 J. S. Y. Tan·Z. Li, 마지막 저자 유담 |
| 3 | 2025 | [Concurrent Multi-Energy Harvesting IC for Self-Sustained Biomedical Applications](https://doi.org/10.1109/esserc66193.2025.11214087) · IEEE European Solid-State Electronics Research Conference (ESSERC) 2025 | 여러 에너지원에서 동시에 에너지를 모으는 동시 다중 에너지 하베스팅(C-MEH) 시스템을 처음으로 제안했다. 몸에 결합되는 50/60Hz 전자기파, 열전, 유기 태양전지에서 함께 에너지를 모아, 주변 환경이 바뀌어도 전력을 안정적으로 대고 출력 수준을 높인다. 지금까지는 여러 원천의 에너지를 동시에 모으면 에너지 되돌림(energy kickback)이 생겨 한계가 있었다. 이를 막는 다입력 다출력 승강압 변환기(EKP-MIMO Buck-Boost, 전압을 낮추거나 높여 바꾸는 직류 변환 회로)로 출력 전력을 56.8% 늘렸다. 하베스터 종류와 상관없이 쓰는 저전력 최대 전력점 추적 회로(SUH-MPPT, 전력원에서 가장 큰 전력을 얻는 동작 조건을 찾아 맞추는 회로)는 0.672μW를 쓰며 면적과 전력을 각각 55.2%, 33.7% 줄였다. 바뀌는 환경 조건에서 생체에서(in vivo) 스스로 얻은 전력만으로 근전도와 심전도를 재는 것을 보였다.[^p3] | 1저자 Z. Li, 마지막 저자 유담 |
| 4 | 2026 | [A Hybrid Dual-Band Ultrasound Imaging SoC With Enhanced Spatial Resolution for UAV Applications](https://doi.org/10.1109/tcsi.2025.3645401) · IEEE Transactions on Circuits and Systems I: Regular Papers | 무인 항공기(UAV, Unmanned Aerial Vehicle)·드론이 보고 길을 찾으려면 강하거나 약한 빛과 여러 날씨에서도 견디는 저전력 3차원 깊이 감지가 필요하다. CMOS 이미지 센서는 깊이를 재지 못하고 어두운 곳에서 어려움을 겪으며, 라이다(빛을 쏘아 되돌아온 빛으로 물체까지의 거리를 재는 센서)는 짙은 안개에 약하고 비싸고, 레이더는 날씨에 강하지만 부피가 크고 비싼 편이다. 초음파 영상 시스템은 날씨와 빛에 강하고 값이 싸지만 대개 해상도와 초당 영상 수가 낮다. 높은 주파수의 초음파를 쓰면 이론상 해상도가 오르지만, 감쇠가 커 거리가 짧아지고 격자 엽(grating lobe, 배열 센서에서 주 빔 말고 다른 방향에 함께 생기는 빔) 현상이 심해진다. 이 연구는 공기 중 초음파 영상 시스템 가운데 처음으로 저주파와 고주파 두 대역 초음파 영상을 SoC 하나에 넣어, 주파수를 거의 지연 없이 바꾸며 지금까지 가장 높은 각도 해상도를 얻었고, 보통 초당 1104만 개의 초점(focal point)을 처리해 실시간 고해상도 3차원 영상을 만든다. 거리에 따른 신호 대 잡음비 측정, 두 대역 혼합 영상, 0.5도 각도 해상도를 보인 두 점 분리 실험, 날고 있는 드론 위 공중 측정을 포함한 시스템 검증에서 저주파와 고주파 모드 모두 7m 거리, 초당 21장으로 안정되게 동작함을 확인했다. 180나노미터 CMOS 공정으로 만든 칩은 넓이 30mm², 전력 116.1mW다.[^p4] | 공동 1저자 J. Guo·S. Chen, 마지막 저자 유담 |

## 교수와 전문 분야

유담 교수는 KAIST에서 전기 및 전자공학을 전공해 2002년 학사, 2007년 석사, 2010년 박사 학위를 받았다.[^profile][^eceprof] 2002–2004년 Triton Tech, Inc.에서 Assistant Manager로 일했고, 2010년 6월부터 2016년 12월까지 아랍에미리트 아부다비의 Masdar Institute of Science and Technology에서 Assistant/Associate Professor로 있었다. 그사이 2010–2011년에는 MIT Microsystems Technology Laboratory의 Visiting Scholar, 2011–2012년에는 MIT의 Research Affiliate였다. 2017년 1월부터 2024년 2월까지 싱가포르 국립대(National University of Singapore) 전기·컴퓨터공학과 Associate Professor였고, 2024년 3월 서울대학교로 옮겨 부교수가 됐으며 2026년 9월부터 교수다.[^profile][^news] 학과 교수 소개는 전공을 「집적회로 및 시스템 설계, 바이오메디컬 및 초음파 시스템」, 분야를 「집적회로, 바이오메디컬 및 초음파 시스템, 머신러닝」으로 적는다.[^eceprof]

교수는 IEEE Fellow다. 누리집 소식은 2026년 1월 1일부터 효력이 있는 IEEE Fellow 선정 이유를 의생명 회로·시스템과 인체영역네트워크에 대한 기여(for contributions to Biomedical Circuits and Systems and Body-Area Network)로 적는다.[^news][^profile] IEEE Solid-State Circuits Society(SSCS)의 Distinguished Lecturer(2017–2018, 2024–2025)와 IEEE Circuits and Systems Society(CASS)의 Distinguished Lecturer(2019–2021, 2026–2027)를 맡았고, 2026–2028년 SSCS Administrative Committee(AdCom) 위원이다.[^profile] ISSCC(IEEE International Solid-State Circuits Conference)에서 Executive Committee 위원(2021년부터), Medical Subcommittee 위원장(2026년부터), Student Research Preview 위원장(2021–2026)을 맡았고, ISLPED의 TPC Co-Chair(2024)와 General Co-Chair(2025), A-SSCC와 CICC의 분과 위원장, IEEE Transactions on Biomedical Circuits and Systems(TBioCAS)의 Steering Committee 위원(2023년부터)을 맡았다. TBioCAS와 IEEE Open Journal of Solid-State Circuits Society의 Associate Editor를 지냈다.[^profile] 교수 소개는 교수가 ISSCC 2020·2022 Demonstration Session Award(Certificate of Recognition), ISCAS 2015 Best Paper Award(BioCAS Track)와 Runner-Up Best Student Paper Award, 2015년 Masdar Institute Best Research Award, A-SSCC Outstanding Design Award(2005, 2022, 2024)를 받거나 함께 받았다고 적는다.[^profile] Springer 책 네 권에 장을 썼고(2010, 2017, 2018, 2021),[^profile] 누리집 논문 목록의 특허 칸은 "He holds 11 patents. (3 pending)"이라고만 적는다.[^pubs]

누리집 논문 목록을 시기별로 보면, 2006–2016년 논문은 착용형 인체 센서 네트워크와 유도 결합(한 회로의 전류 변화가 만드는 자기장으로 다른 회로에 신호나 전력을 전하는 방식) 송수신기, 옷감에 만든 평면 회로 기판(Planar-Fabric Circuit Board)과 셔츠형 심전도 측정 시스템, 환자 맞춤형 뇌전증 발작 분류 SoC, 인체 결합 통신 송수신기, pMUT 초음파 인터페이스 회로를 주로 다룬다.[^pubs] 2017–2023년 논문은 여러 채널의 생체 전위 계측 증폭기, 몸을 통한 전력 전송과 에너지 하베스팅, 환자 맞춤형 뇌전증 관리 SoC, 드론용 초음파 영상 ASIC으로 넓어졌다.[^pubs] 서울대 시기의 대표 논문은 고속 순환형 ADC(대표 논문 1), 몸을 통한 전력 공급과 여러 에너지원의 동시 수집(대표 논문 2, 3), 무인 항공기용 초음파 영상 SoC(대표 논문 4)이고, 같은 시기 논문 목록에는 생체 신호 측정용 ADC와 CMOS 이징 머신도 있다.[^p1][^p2][^p3][^p4][^pubs]

## 응용 분야

누리집은 연구가 의생명 응용을 위한 것이라고 밝히고, 과제로 착용형 건강 관리와 환자 맞춤형 발작 검출을 든다.[^project] 교수 소개는 착용형 인체 센서 네트워크를 지속적인 건강 감시 시스템을 위한 것으로 적는다.[^profile] 학과 연구실 소개는 초음파 회로와 시스템의 쓰임을 드론과 의료로 적는다.[^ecelabv] 대표 논문은 배터리 없이 오래 쓰는 건강 감시용 피부형 심전도 센서,[^p2] 무인 항공기의 길 찾기를 위한 3차원 깊이 감지[^p4]를 대상으로 한다. 누리집 소식은 연구실의 의생명 회로·시스템과 초음파 연구가 2024년 9월 ARM의 연구 협력 블로그에 소개됐다고 적는다.[^news] 졸업생과 이전 구성원의 진로로는 Samsung Electronics, HiSilicon, Huawei Technologies, Analog Devices, ST Microelectronics, Apple 같은 반도체·전자 기업과, Xidian University·Southern University of Science and Technology·Western Washington University·Singapore Institute of Technology·경희대학교의 교수 자리가 있다.[^people]

## 구성원

2026년 10월 25일 누리집 People 페이지 기준이다. Students 칸의 Graduate Students 23명과 Undergradate Students(페이지 표기) 4명이며, 페이지는 학생마다 석사·박사 과정, 시작 시점, 연구 주제를 적지 않는다. 이름 뒤 (from NUS)는 페이지 표기다. Research Staffs 칸(Postdoctoral Research Fellows, Research Engineers)과 Visiting Graduate Students 칸에는 이름이 없다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Sunwoo HONG | 대학원생 |  |
| Jeongyong SHIN | 대학원생 |  |
| Hoang Chung NGUYEN | 대학원생 |  |
| Gwangjin KIM | 대학원생 | 2 |
| Sooyoung CHOI | 대학원생 |  |
| Donghan KIM | 대학원생 | 2 |
| Yeejoo HAN | 대학원생 |  |
| Florian SREDNIAWA | 대학원생 |  |
| Kwonbeen DU | 대학원생 |  |
| Wonyi HONG | 대학원생 |  |
| Hyeongseon EOM | 대학원생 |  |
| Jihye PARK | 대학원생 |  |
| Donghyeon KIM | 대학원생 |  |
| Kyungsoo PARK | 대학원생 | 2 |
| Sein KIM | 대학원생 |  |
| Silin CHEN (from NUS) | 대학원생 | 4 |
| Junwei FENG (from NUS) | 대학원생 | 2, 4 |
| Jiaer CHEN (from NUS) | 대학원생 | 3 |
| Zhongqi LI (from NUS) | 대학원생 | 2 |
| Hyunseung LEE | 대학원생 |  |
| Junbeom PARK | 대학원생 |  |
| Hyoungjoon KIM | 대학원생 |  |
| Jinhong AHN | 대학원생 |  |
| Saeram SON | 학부 연구생 |  |
| Donguk KIM | 학부 연구생 |  |
| Dojin KIM | 학부 연구생 |  |
| Kyumin KIM | 학부 연구생 |  |

## 졸업생과 이전 구성원

누리집 People 페이지 Alumni 칸의 네 구획(Past Graduate Students 35명, Past Undergraduate Students 10명, Past Visiting Graduate Students 4명, Past Research Staffs 5명)에 오른 54줄이다. 이 명단은 교수가 Masdar Institute(2010–2016)와 싱가포르 국립대(NUS, 2017–2024)에 있던 때의 학생·연구원을 함께 올리며, 어느 학교 소속이었는지는 적지 않는다.[^people][^profile] 학위·과정 칸은 페이지의 구획 이름을 옮긴 것이고, 괄호 안 졸업 시기와 진로는 페이지가 이름 옆에 적은 표기를 옮긴 것이다. 이름 뒤의 Ph.D.와 CFA도 페이지 표기다. 방문 대학원생 칸의 괄호 안 기관·직함은 페이지가 이름 옆에 적은 표기로, 방문 당시 소속과 이후 직장이 섞여 있다. Joanne Si Ying TAN은 대학원생과 연구 직원 구획에 모두 올라 있다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Muhammad Hareez | 대학원생 (2026년 7월 졸업) | Samsung Electronics, Korea |
| Yingna HUANG, Ph.D. | 대학원생 (2026년 7월 졸업) | Research Fellow, NUS |
| Muhammad Nur Hakim ROSLI | 대학원생 |  |
| Zhouyue LI, Ph.D. | 대학원생 (2026년 7월 졸업) | HiSilicon |
| Kangmin LEE | 대학원생 (2026년 2월 졸업) | Samsung Electronics, Korea |
| Rucheng JIANG, Ph.D. | 대학원생 (2025년 12월 졸업) | Analog Devices, Singapore |
| Jiaqi GUO, Ph.D. | 대학원생 (2024년 6월 졸업) | Professor, Xidian University, China |
| Jia Yi FONG | 대학원생 (2024년 6월 졸업) |  |
| Chne Wuen TSAI, Ph.D. | 대학원생 (2023년 12월 졸업) | ST Microelectronics, Singapore |
| Liuhao WU, Ph.D. | 대학원생 (2023년 5월 졸업) | ST Microelectronics, Singapore |
| Benjamin Ho Yin LEE | 대학원생 (2023년 12월 졸업) | Lecturer, Singapore Polytechnic, Singapore |
| Ahmet Selman KURT | 대학원생 (co-advised) |  |
| Joanne Si Ying TAN, Ph.D. | 대학원생 (2023년 2월 졸업) | Huawei Technologies, Singapore |
| Lian ZHANG, Ph.D. | 대학원생 (2022년 2월 졸업) | Apple, CA, USA |
| Miaolin ZHANG, Ph.D. | 대학원생 (2022년 1월 졸업) | Huawei Technologies |
| Yilong DONG, Ph.D. | 대학원생 (2022년 1월 졸업) | HiSilicon |
| Jiamin LI, Ph.D. | 대학원생 (2022년 1월 졸업) | Associate Professor, Southern University of Science and Technology, China |
| Han WU, Ph.D. | 대학원생 (2022년 1월 졸업) | Research Fellow, NUS |
| Luo YANG | 대학원생 (2022년 졸업) |  |
| Yue ZHUANG | 대학원생 (2022년 졸업) |  |
| Zhongwei YAN | 대학원생 (2022년 졸업) |  |
| Yihan HE | 대학원생 (2021년 졸업) | Ph.D. student, NUS, Singapore |
| Boyang CAO | 대학원생 (2021년 졸업) |  |
| Hector Andreaz Gonzalez Diaz | 대학원생 (2018년 졸업) | Ph. D. student, TU Dresden, Germany |
| Thaer Alafghani | 대학원생 | Ph.D student, University of Southern California, CA, USA |
| Nimesh Shah | 대학원생 (2017년 졸업) | Ph.D. student, Nanyang Technological University, Singapore |
| Aydah Albadow | 대학원생 | Biomedical Engineer, Ministry Of Health & Prevention (MOHAP), UAE |
| Haneen Alsuradi | 대학원생 (2017년 졸업) | Ph.D. student, New York University Abu Dhabi, Abu Dhabi, UAE |
| Judyta Tillak, Ph.D. | 대학원생 (2017년 졸업) | AMS Architect, Axign BV, Netherlands |
| Ljubomir Radakovic | 대학원생 (2017년 졸업) | Research Engineer, Masdar Institute, UAE |
| Muhammad Awais Bin Altaf, Ph.D. | 대학원생 (2016년 졸업) | Assistant Professor, Western Washington University, WA, USA |
| Wala Saadeh, Ph.D. | 대학원생 (2016년 졸업) | Associate Professor, Western Washington University, WA, USA |
| Abdulfattaahi Kunle Raji, CFA | 대학원생 | CEO, RajFin |
| Chen Zhang | 대학원생 (2014년 졸업) | Huawei Technologies |
| Yonatan Kifle | 대학원생 (2013년 졸업) | Ph.D. student, Linköping University, Sweden |
| Beom Jun KIM | 학부생 |  |
| Sangkook LEE | 학부생 |  |
| Siun LEE | 학부생 |  |
| Euntaek PAEK | 학부생 |  |
| Dong-geon KIM | 학부생 |  |
| Somi HONG | 학부생 |  |
| Daeheon KWON | 학부생 |  |
| Lou Alsteens | 학부생 |  |
| Jonathan En Zhe CHUA | 학부생 |  |
| Lingke DING | 학부생 |  |
| Samuel FURTER | 방문 대학원생 (EPFL, Switzerland) |  |
| Jihee LEE | 방문 대학원생 (Ph.D. student, KAIST) |  |
| KyongRog LEE | 방문 대학원생 (Ph.D. student, KAIST) |  |
| Long YAN, Ph.D. | 방문 대학원생 (Principal Member of Technical Staff, Samsung Electronics) |  |
| Joanne Si Ying TAN, Ph.D. | 연구 직원 | Huawei Technologies, Singapore |
| Astrid Rusley | 연구 직원 (former research engineer) |  |
| Tao TANG, Ph.D. | 연구 직원 | Principal Investigator, Research Center for Cyber-Physical-Social System, Zhejiang Labs |
| Kian Ann NG, Ph.D. | 연구 직원 | Professor, Singapore Institute of Technology, Singapore |
| JeongHoan Park, Ph.D. | 연구 직원 | Professor, Kyunghee University, Korea |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지 Journal Papers 칸의 2021–2026년 논문 가운데 25편과 Conference Papers 칸의 2021–2026년 논문 가운데 19편이다. 연도는 각 항목에 적힌 날짜의 연도이고, 제목·저자·학술지와 학회 이름은 누리집 표기 그대로다. 이름 뒤 *는 누리집이 공동 기여 저자(Equally contributed authors)로 밝힌 표시다.[^pubs] 날짜 없이 게재 승인(accepted)으로 적힌 Falcon 논문은 학술지 서지 기록이 2026년 9월호(61권 9호)로 적어 2026년 구역에 두었다.[^falcon] 이 목록은 교수 개인 목록이라, 교수가 서울대로 옮긴 2024년 3월 전 싱가포르 국립대 시기의 논문이 함께 있다.[^profile][^pubs]

**2026**

- Jiaer Chen, Yingna Huang, Zhongqi Li, Han Wu, Longyang Lin, Jiamin Li and Jerald Yoo. "A 3-D Connectivity CMOS Ising Machine with 12-Way Toroidal Hexagonal Close-Packed Supply-and-Bulk Injection Locking Oscillators for Combinatorial Optimization". *IEEE Transactions on Circuits and Systems Part I: Regular Papers (TCAS-I), vol. 73, no. 8, pp. 5064-5077, Aug. 2026. (doi: 10.1109/TCSI.2026.3704449)*.
- Rucheng Jiang, Han Wu, Kian Ann Ng, Chne-Wuen Tsai and Jerald Yoo. "A 13-bit 70MS/s SAR-Assisted Cyclic ADC with Charge-Reused 2-bit/Cycle Operation". *IEEE Transactions on Circuits and Systems Part I: Regular Papers (TCAS-I), vol. 73, no. 8, pp. 5142-5153, Aug. 2026. (doi: 10.1109/TCSI.2026.3690163)*.
- Jin Wang, Moxiao Lou, Zhengke Yang, Zhixiong Li, Jiamin Li, Yida Li, Jerald Yoo and Longyang Lin. "AdaPIM: A CIM-Based General-Purpose Vision Accelerator With Adaptive Inter-Macro Parallelism and Multi-Level Feature Reuse". *IEEE Journal of Solid-State Circuits (JSSC), vol. 61, no. 8, pp. 4399-4413, Aug. 2026. (doi: 10.1109/JSSC.2026.3654682)*.
- Joanne Si Ying Tan\*, Zhuoyue Li\*, Sixing Xiong, Shinyoung Lee, Jia Yi Fong, Tao Tang, Jiamin Li, Zhongqi Li, Kyungsoo Park, Donghan Kim, Junwei Feng, Gwanjin Kim, Lian Zhang, Astrid Rusly, Benjamin Ho Yin Lee, Kian Ann Ng, Kenjiro Fukuda, Takao Someya and Jerald Yoo. "SkinECG: An orthogonal remote powering wearable skin-like sensor". *Science Advances vol. 12, eaec9803 (2026). doi:10.1126/sciadv.aec9803*.
- Wenao Xie, Haoyang Sang, Zhamaliddin Kalzhan, Jingu Lee, Jerald Yoo, Kangho Lee and Hoi-Jun Yoo. "Falcon: Event-Driven Hybrid Object Tracking SoC with Bit-Column-Similarity-Based MRAM PIM and Heterogeneous Read-Only-Once Attention Flow". *IEEE Journal of Solid-State Circuits (JSSC) (accepted)*.
- Jiaqi Guo\*, Silin Chen\*, Junwei Feng, Zhuoyue Li and Jerald Yoo. "A Hybrid Dual-Band Ultrasound Imaging SoC with Enhanced Spatial Resolution for UAV Applications". *IEEE Transactions on Circuits and Systems Part I: Regular Papers (TCAS-I) vol. 73, no. 6, pp. 4246-4258, Jun. 2026*.
- S. Song, Y. Jang, D. Jung, K. Park, D. Kim, G. Kim, H. Lee, J. Yoo and J. Kim. "TierX: A Simulation Framework for Multi-tier BCI System Design Evaluation and Exploration". *ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS) , Mar. 2026*.
- Y. Wang, L. Lin, J. Yoo and J. Li. "A 16.4nJ/Class Patient-Independent Prototype-Based Spatio-Temporal CNN Processor with Forward-Inference-Based Adaptation for Robust and Low-Latency Seizure Detection". *IEEE International Solid-State Circuits Conference (ISSCC) , Feb. 2026*.
- Q. Cheng, Z. Yang, H. Li, Q. Li, Z. Kong, G. Niu, Y. Liang, J. Li, J. Yoo, M. Hashimoto and L. Lin. "A Radiation-Hardened Self-Healing CMOS Imager with Online Pixel/Logic Annealing and Tile-Adaptive Compression for Space Applications". *IEEE International Solid-State Circuits Conference (ISSCC) , Feb. 2026*.

**2025**

- Joanne Si Ying Tan\*, Zhuoyue Li\*, Chne-Wuen Tsai, Jeong Hoan Park, Jiamin Li, Yilong Dong, Kwok Hoe Chan, Ghim Wei Ho and Jerald Yoo. "A 0.5 nJ/Conversion Self-Resetting Energy-Autonomous Multi-Node Temperature Sensor with Hybrid Energy Harvesting". *IEEE Open Journal of Solid-State Circuits Society (OJ-SSCS) vol. 6, pp. 377-387, Dec. 2025*.
- Yiqing Lan, Longyang Lin, Jerald Yoo and Jiamin Li. "A Leakage-Suppressing Differential-Drive Rectifier for Sporadic Wearable Triboelectric Energy Harvesting". *IEEE Transactions on Circuits and Systems II - Express Briefs, vol. 72, no. 11, pp. 1645-1649, Nov. 2025*.
- Rucheng Jiang, Jia Yi Fong, Chne-Wuen Tsai, Jiaer Chen, Zhongqi Li, Benjamin Ho Yin Lee and Jerald Yoo. "A Rail-to-Rail Input NS-Pipelined-SAR ADC with Self-Boosted Input Impedance and Reused Residue Amplifier for Biosignal Acquisition". *IEEE Journal of Solid-State Circuits (JSSC), vol. 60, no. 10, pp. 3551-3565, Oct. 2025*.
- Zhuoyue Li, Joanne Si Ying Tan, Jia Yi Fong, Yingna Huang, Astrid Rusly, Jiaer Chen, Benjamin Ho Yin Lee and Jerald Yoo. "Concurrent Multi-Energy Harvesting IC for Self-Sustained Biomedical Applications". *IEEE European Solid-State Circuits Conference (ESSCIRC) , Sep. 2025*.
- Jin Wang, Moxiao Lou, Zhengke Yanq, Rujie Peng, Humiao Li, Weirong Dong, Haoran Lyu, Yida Li, Jiamin Li, Hao Yu, Jerald Yoo, and Longyang Lin. "A 22nm 29.3TOPS/W End-to-End CIM-Utilization-Aware Accelerator with Reconfigurable 4D-CIM Mapping and Adaptive Feature Reuse for Diverse CNNs and Transformers". *IEEE Custom Integrated Circuits Conference (CICC) , Apr. 2025*.

**2024**

- Kian Ann Ng, Lian Zhang, Han Wu, Tao Tang and Jerald Yoo. "A Single-Stage, Capacitively-Coupled Instrumentation Amplifier with Complementary Transimpedance Boosting". *IEEE Transactions on Circuits and Systems I - Regular Papers, vol. 71, no. 7, pp. 2989-3001, Jul. 2024*.
- Jia Si, Shuhan Yang, Yunuo Cen, Jiaer Chen, Yingna Huang, Zhaoyang Yao, Dong-Jun Kim, Kaiming Cai, Jerald Yoo, Xuanyao Fong and Hyunsoo Yang. "Energy-efficient superparamagnetic Ising machine and its application to traveling salesman problems". *Nature Communications 15, 3457 (2024). doi: 10.1038/s41467-024-47818-z*.
- Jiamin Li, Yilong Dong, Longyan Lin, Joanne Tan Si Ying, Jia Yi Fong and Jerald Yoo. "Concurrent Body-Coupled Powering and Communication ICs with a Single Electrode". *IEEE Journal of Solid-State Circuits (JSSC), vol. 59, no. 4, pp.1006-1016, April 2024*.
- Yingna Huang, Chne-Wuen Tsai, Jiaer Chen, Zhongqi Li, Longyang Lin, Jiamin Li and Jerald Yoo. "PRIM-CAEFA: a 64K-Spin Packet-Based Reconfigurable Ising Machine with Cross-Problem Adjustment-Free Energy Feedback Annealing". *IEEE Asian Solid-State Circuits Conference (A-SSCC) , Nov. 2024*.
- Jiaer Chen, Yingna Huang, Jiamin Li, Longyang Lin, Han Wu and Jerald Yoo. "A 3-D Ising Machine with 12-Way Supply-and-Bulk Injection Locking Oscillators for Combinatorial Problem Solving". *IEEE Asian Solid-State Circuits Conference (A-SSCC) , Nov. 2024*.
- Rucheng Jiang and Jerald Yoo. "A 3.32mW 300MS/s 13b Pipelined SAR ADC Using a Time-Assisted Ringamp with Dynamic Slew Rate and Low-Supply Bias". *IEEE European Solid-State Circuits Conference (ESSCIRC) , Sep. 2024*.
- Jiaqi Guo, Junwei Feng, Silin Chen, Liuhao Wu, Chne-Wuen Tsai, Yingna Huang, Bochi Lin and Jerald Yoo. "A 0.5°-Resolution Hybrid Dual-Band Ultrasound Imaging SoC for UAV Applications". *IEEE International Solid-State Circuits Conference (ISSCC) , Feb. 2024*.

**2023**

- Chne-Wuen Tsai, Rucheng Jiang, Lian Zhang, Miaolin Zhang and Jerald Yoo. "Seizure-Cluster-Inception CNN (SciCNN): A Patient-Independent Epilepsy Tracking SoC With 0-Shot-Retraining". *IEEE Transactions on Biomedical Circuits and Systems (TBioCAS), vol. 17, no. 6, Dec. 2023*.
- Han Wu, Jeong Hoan Park, Rucheng Jiang, Junghwan Choi and Jerald Yoo. "A Charge Recycling Logic Data Links for Single and Multiple Channel I/Os". *IEEE Journal of Solid-State Circuits (JSSC) , vol. 58, no. 10, pp. 2790-2800, Oct. 2023*.
- Jerald Yoo. "Body Area Network - Connecting and Powering Things Together Around the Human Body". *IEEE Solid-State Circuit Magazine (SSC-M), Spring 2023 issue*.
- Jiaqi Guo, Jiamin Li and Jerald Yoo. "A Hybrid Boost Converter with Standard CMOS-Compatible 14V Output for an Ultrasound Imaging System". *IEEE Solid-State Circuits Letters (invited), vol. 6, pp. 125-128, Apr. 2023*.
- Rucheng Jiang, Han Wu, Kian Ann Ng and Jerald Yoo. "A 13-bit 70MS/s SAR-Assisted 2-bit/cycle Cyclic ADC with Offset Cancellation and Slack-Borrowing Logic". *IEEE European Solid-State Circuits Conference (ESSCIRC) , pp. 281-284, Sep. 2023*.
- Jiamin Li, Yilong Dong, Jiayi Fong, Longyan Lin and Jerald Yoo. "Wireless Body-Area Network Transceiver ICs with Concurrent Body-Coupled Powering and Communication using Single Electrode". *IEEE Symposium on VLSI Circuits (VLSI Symp.) , Jun. 2023*.

**2022**

- Liuhao Wu\*, Jiaqi Guo\*, Rucheng Jiang, Yande Peng, Han Wu, Jiamin Li, Yang Luo, Liwei Lin and Jerald Yoo. "An Ultrasound Imaging System With On-Chip Per-Voxel RX Beamfocusing for Real-Time Drone Applications". *IEEE Journal of Solid-State Circuits (JSSC) , vol. 57, no. 11, pp. 3186-3199, Nov. 2022*.
- Han Wu, Miaolin Zhang, Zhichun Shao, Jiaqi Guo, Kian Ann Ng, Liwei Lin and Jerald Yoo. "An Ultrasound ASIC with Universal Energy Recycling for >7-m All-weather Metamorphic Robotic Vision". *IEEE Journal of Solid-State Circuits (JSSC) , vol. 57, no. 10, pp. 3036-3047, Oct. 2022*.
- Tao Tang, Jeong Hoan Park, Lian Zhang, Kian Ann Ng and Jerald Yoo. "Group-Chopping: An 8-Channel, 0.04% Gain Mismatch, 2.1μW 0.017mm2 Instrumentation Amplifier for Bio-potential Recording". *IEEE Transactions on Biomedical Circuits and Systems (TBioCAS), vol. 16, no. 3, pp. 361-371, Jun. 2022*.
- Miaolin Zhang\*, Lian Zhang\*, Chne-Wuen Tsai and Jerald Yoo. "A Patient-Specific Closed-Loop Epilepsy Management SoC with One-Shot Learning and Online-Tuning". *IEEE Journal of Solid-State Circuits (JSSC) , vol. 57, no. 4, pp. 1049-1060, Apr. 2022*.
- Jiaqi Guo, Jiamin Li and Jerald Yoo. "A 14V Hybrid Boost Converter With Scalable Conversion Ratio in 180nm Standard CMOS for an Ultrasound Imaging System". *IEEE Asian Solid-State Circuits Conference (A-SSCC) , Nov. 2022*.
- Han Wu, Jeong Hoan Park, Miaolin Zhang, Longyang Lin, Rucheng Jiang, Jung-Hwan Choi and Jerald Yoo. "A 0.95pJ/b 5.12Gb/s/pin Charge-Recycling IOs with 47% Energy Reduction for Big Data Applications". *IEEE Asian Solid-State Circuits Conference (A-SSCC) , Nov. 2022*.
- Lian Zhang\*, Miaolin Zhang\*, Chne-Wuen Tsai and Jerald Yoo. "Review of AI-on-the-Edge EEG-Based Patient-Specific Epilepsy Tracking SoCs". *IEEE Interregional NEWCAS Conference (NEWCAS) , Jun. 2022*.
- Chne-Wuen Tsai\*, Miaolin Zhang\*, Lian Zhang and Jerald Yoo. "A Closed-Loop Brain-Machine Interface with One-Shot Learning and Online Tuning for Patient-Specific Neurological Disorder Treatment". *IEEE International Conference on Artificial Intelligence Circuits and Systems (AICAS) , Jun. 2022*.
- Liuhao Wu\*, Jiaqi Guo\*, Rucheng Jiang, Yande Peng, Han Wu, Jiamin Li, Yilong Dong, Miaolin Zhang, Zhuoyue Li, Kian Ann Ng, Chne-Wuen Tsai, Lian Zhang, Longyang Lin, Liwei Lin and Jerald Yoo. "BatDrone: A 9.83M-focal points/s, 7.76μs Latency Ultrasound Imaging Sensor SoC with On-Chip Per-Voxel RX Beam-Focusing for 7-m Range Drone Applications". *IEEE International Solid-State Circuits Conference (ISSCC) , Feb. 2022*.

**2021**

- Jerald Yoo and Mahsa Shoaran. "Neural interface systems with on-device computing: machine learning and neuromorphic architectures". *Current Opinion in Biotechnology vol. 72, pp. 95-101, Dec. 2021*.
- Joanne Tan, Jeong Hoan Park, Jiamin Li, Yilong Dong, Kwok Hoe Chan, Ghim Wei Ho and Jerald Yoo. "A Fully Energy-Autonomous Temperature-to-Time Converter Powered by a Triboelectric Energy Harvester for Biomedical Applications". *IEEE Journal of Solid-State Circuits (JSSC), vol. 56, no. 10, pp. 2913-2923, Oct. 2021*.
- Jiamin Li\*, Yilong Dong\*, Jeong Hoan Park and Jerald Yoo. "Body-coupled power transmission and energy harvesting". *Nature Electronics 4, 530-538 (2021). doi: 10.1038/s41928-021-00592-y*.
- Hector Andreaz Gonzalez Diaz, Richard George, Shahzad Muzzafar, Javier Acevedo, Sebastian Hoeppner, Christian Mayr, Jerald Yoo, Frank Fitzek and Ibrahim Elfadel. "Hardware Acceleration of EEG-based Emotion Classification Systems: A Comprehensive Survey". *IEEE Transactions on Biomedical Circuits and Systems (TBioCAS) , vol. 15, no. 3, pp. 412-442, Jun. 2021*.
- Jihee Lee, Kyoung-Rog Lee, Benjamin E. Eovino, Jeong Hoan Park, Luna Yue Liang, Liwei Lin, Hoi-Jun Yoo and Jerald Yoo. "A 36-Channel Auto-Calibrated Front-End ASIC for a pMUT-based Miniaturized 3-D Ultrasound System". *IEEE Journal of Solid-State Circuits (JSSC) vol. 56, no. 6, pp. 1910-1923, Jun. 2021*.
- Han Wu, Miaolin Zhang, Jiaqi Guo, Zhichun Shao, Kian Ann Ng, Jiamin Li, Lian Zhang, Yilong Dong, Liuhao Wu, Chne-Wuen Tsai, Benjamin Ho Yin Lee, Liwei Lin and Jerald Yoo. "A 7m-range, 4.3mW/Ch. Ultrasound ASIC with Universal Energy Recycling TX for All-Weather Metamorphic Robotic Vision System". *IEEE Asian Solid-State Circuits Conference (A-SSCC) , Nov. 2021*.
- Yilong Dong\*, Jiamin Li\*, Longyang Lin, Tao Tang, Jeong Hoan Park, Kian Ann Ng, Miaolin Zhang, Lian Zhang, Joanne Si Ying Tan and Jerald Yoo. "Body-Coupled Power Transceiver with Node-Specific Body-Area Powering". *IEEE European Solid-State Circuits Conference (ESSCIRC) , Sep. 2021*.
- Miaolin Zhang\*, Lian Zhang\*, Jeonghoan Park, Chne-Wuen Tsai, Kian Ann Ng, Longyan Lin, Yilong Dong, Jiamin Li, Tao Tang, Han Wu, Liuhao Wu and Jerald Yoo. "A One-Shot Learning, Online-Tuning, Closed-Loop Epilepsy Management SoC with 0.97uJ/Classification and 97.8% Vector-Based Sensitivity". *IEEE Symposium on VLSI Circuits (VLSI Symposium), Jun. 2021*.

## 수상

누리집 News 페이지의 수상 글 4건과 Publications 페이지가 A-SSCC 2021·2024 논문 항목에 붙인 수상 표시 2건이다. 날짜는 글의 연월(논문 항목은 학회 연월)이다. 수상 글은 누리집 문구 그대로이고, 논문 항목은 누리집의 수상 표시 뒤에 논문 제목과 학회를 붙였다. 2024년 3월 전 항목은 교수가 싱가포르 국립대에 있던 때의 수상이다.[^news][^pubs][^profile]

- 2025-12 · Prof. Jerald Yoo has been elected as an IEEE Fellow (Effective Jan. 1, 2026), for contributions to Biomedical Circuits and Systems and Body-Area Network.
- 2024-11 · Yingna Huang (Ph.D. Student) won the IEEE A-SSCC Student Design Contest.
- 2024-11 · A-SSCC2024 Best Demo Award Winner: 「PRIM-CAEFA: a 64K-Spin Packet-Based Reconfigurable Ising Machine with Cross-Problem Adjustment-Free Energy Feedback Annealing」 (IEEE Asian Solid-State Circuits Conference (A-SSCC), Nov. 2024)
- 2023-02 · Liuhao Wu (Ph.D. student) and Jiaqi Quo (Ph.D. student) won the IEEE International Solid-State Circuits Conference (ISSCC) 2022 Demonstration Award with their paper on ultrasound ASIC for all-light-condition drone.
- 2021-11 · Han Wu (Ph.D. student) received the Best Design Award at IEEE Asian Solid-State Circuits Conference (A-SSCC) Student Design Contest.
- 2021-11 · A-SSCC2021 Demo Award Winnner: 「A 7m-range, 4.3mW/Ch. Ultrasound ASIC with Universal Energy Recycling TX for All-Weather Metamorphic Robotic Vision System」 (IEEE Asian Solid-State Circuits Conference (A-SSCC), Nov. 2021)

## 소식

누리집 News 페이지의 2021년 11월–2026년 9월 글 가운데 논문·발표·강연·학술 활동 글 52건이다. 수상 글은 위 「수상」에 있다. 날짜는 글의 연월이고 문구는 누리집 글을 옮긴 것이다. 교수가 서울대로 옮긴 2024년 3월 전 글은 싱가포르 국립대 시기의 글이다.[^news][^profile]

- 2026-06 · Jiaer Chen (Ph.D. student) got his paper accepted to IEEE Trans. Circuits and Systems I - Regular Papers (TCAS-I). The paper title is "A 3-D Connectivity CMOS Ising Machine with 12-Way Toroidal Hexagonal Close-Packed Supply-and-Bulk Injection Locking Oscillators for Combinatorial Optimization."
- 2026-05 · Joanne Si Ying Tan (former Ph.D. student) and Zhuoyue Li (Ph.D. student) got their paper accepted to Science Advances. The paper title is "SkinECG: An orthogonal remote powering wearable skin-like sensor."
- 2026-04 · Rucheng Jiang (Ph.D. graduate) got his paper accepted to IEEE Trans. Circuits and Systems I - Regular Papers (TCAS-I). The paper title is "A 13-bit 70MS/s SAR-Assisted Cyclic ADC with Charge-Reused 2-bit/Cycle Operation."
- 2026-03 · Prof. Jerald Yoo has been appointed Chair of the ISSCC Medical Subcommittee.
- 2026-02 · Prof. Jerald Yoo presented at a panel @ ISSCC2027, "The Augmented Human: Will Chips in Our Brain Enhance Our Cognitive Abilities?."
- 2025-12 · Jiaqi Guo (former Ph.D. student), Silin Chen (Ph.D. student) and Junwei Feng (Ph.D. student) got their paper accepted to IEEE Transactions on Circuits and Systems - Part 1: Regular Papers (TCAS-I). The paper title is "A Hybrid Dual-Band Ultrasound Imaging SoC with Enhanced Spatial Resolution for UAV Applications."
- 2025-12 · Joanne Si Ying Tan (former Ph.D. student) and Zhuoyue Li (Ph.D. student) got their paper accepted to IEEE Open Journal of Solid-State Circuits Society (OJ-SSCS). The paper title is "A 0.5 nJ/Conversion Self-Resetting Energy-Autonomous Multi-Node Temperature Sensor with Hybrid Energy Harvesting."
- 2025-11 · Prof. Jerald Yoo gave a talk at Caltech, CA.
- 2025-11 · Prof. Jerald Yoo gave two SSCS DL talks at Intel, Hilsoboro, OR and University of Southern California (USC), CA.
- 2025-11 · Prof. Jerald Yoo gave two SSCS DL talks at Tsinghua University and Beijing University, China.
- 2025-10 · Prof. Jerald Yoo is elected as an IEEE Solid-State Circuits Society (SSCS) Administrative Committee (AdCom) member (Effective Jan. 1, 2026).
- 2025-07 · Rucheng Jiang (Ph.D. student) got his paper accepted to IEEE Journal of Solid-State Circuits (JSSC). The paper title is "A Rail-to-Rail Input NS-Pipelined-SAR ADC with Self-Boosted Input Impedance and Reused Residue Amplifier for Biosignal Acquisition."
- 2025-07 · Prof. Jiamin Li (Ph.D. graduate) got her paper accepted to IEEE Trans. Circuits and Systems II - Express Briefs (TCAS-II). The paper title is "A Leakage-Suppressing Differential-Drive Rectifier for Sporadic Wearable Triboelectric Energy Harvesting."
- 2025-06 · Zhuoyue Li (Ph.D. student) got her paper accepted at IEEE European Solid-State Electronics Research Conference (ESSERC) 2025. The paper title is "Concurrent Multi-Energy Harvesting IC for Self-Sustained Biomedical Applications."
- 2025-05 · Prof. Jerald Yoo gave a talk at ARM Ltd., Cambridge, UK.
- 2025-05 · Prof. Jerald Yoo gave an SSCS DL talk at University Lille, Lille, France.
- 2025-05 · Prof. Jerald Yoo gave two DL talks at AGH University of Science and Technology, Krakow, Poland.
- 2025-04 · Prof. Jerald Yoo gave a tutorial at IEEE Custom Integrated Circuits Conference (CICC).
- 2025-04 · Prof. Jerald Yoo gave a talk at Analog Devices, Inc. Head Quarter at Wilmington, MA, USA.
- 2024-10 · Prof. Jerald Yoo delivered the keynote at IEEE CASS Workshop and Medical Wearables.
- 2024-10 · Prof. Jerald Yoo gave three lectures at XJTU (Xian), UESTC (Chengdu) and HUST (Wuhan) under the IEEE SSCS Distinguished Lecturer (DL) program.
- 2024-09 · Prof. Jerald Yoo gave a lecture at EPFL, Laussane under the IEEE SSCS Distinguished Lecturer (DL) program.
- 2024-09 · Prof. Jerald Yoo gave a lecture at ETH Zurich under the IEEE SSCS Distinguished Lecturer (DL) program.
- 2024-09 · Prof. Jerald Yoo presented at Korea-Switzerland Forum on Semiconductor.
- 2024-09 · Rucheng Jiang (Ph.D. student) presented his paper at IEEE European Solid-State Electronics Research Conference (ESSERC). The paper title is "A 3.32mW 300MS/s 13b Pipelined SAR ADC Using a Time-Assisted Ringamp with Dynamic Slew Rate and Low-Supply Bias."
- 2024-09 · Yoo group research on Biomedical Circuit & System and Ultrasound is highlighted in ARM's Blog on Research Collaboration and Enablement.
- 2024-08 · Jiaer Chen (Ph.D. student) got his paper accepted to IEEE Asian Solid-State Circuits Conference (A-SSCC). The paper title is "A 3-D Ising Machine with 12-Way Supply-and-Bulk Injection Locking Oscillators for Combinatorial Problem Solving."
- 2024-08 · Yingna Huang (Ph.D. student) got her paper accepted to IEEE Asian Solid-State Circuits Conference (A-SSCC). The paper title is "PRIM-CAEFA: a 64K-Spin Packet-Based Reconfigurable Ising Machine with Cross-Problem Adjustment-Free Energy Feedback Annealing."
- 2024-05 · Prof. Kian Ann Ng (Former research fellow) got his paper accepted to IEEE Transaction on Circuits and Systems I: Regular Papers. The paper title is "A Single-Stage, Capacitively-Coupled Instrumentation Amplifier with Complementary Transimpedance Boosting."
- 2024-04 · Jiaer Chen and Huang Yingna (Ph.D. students) got their co-authored collaborative work on Ising Machine published at Nature Communications.
- 2023-12 · Prof. Jiamin Li (Ph.D. graduate) got her paper accepted to IEEE Journal of Solid-State Circuits (JSSC). The paper title is "Concurrent Body-Coupled Powering and Communication ICs with a Single Electrode."
- 2023-11 · Prof. Jerald Yoo is nominated and will serve as a Technical Program Committee Chair (TPC Chair) of ACM/IEEE International Symposium on Low-Power Electronics and Design (ISLPED).
- 2023-11 · Jiaqi Guo (Ph.D. student) got his paper accepted to IEEE International Solid-State Circuits Conference (ISSCC). The paper title is "A 0.5°-Resolution Hybrid Dual-Band Ultrasound Imaging SoC for UAV Applications."
- 2023-10 · Chne-Wuen Tsai (Ph.D. student) got his paper accepted to IEEE Transactions on Biomedical Circuits and Systems (TBioCAS). The paper title is "Seizure-Cluster-Inception CNN (SciCNN): A Patient-Independent Epilepsy Tracking SoC With 0-Shot-Retraining."
- 2023-09 · Prof. Jerald Yoo is nominated as a Steering Committee Member of IEEE Transactions on Biomedical Circuits and Systems (TBioCAS).
- 2023-08 · Han Wu (Ph.D. graduate) got his paper accepted to IEEE Journal of Solid-State Circuits (JSSC). The paper title is "A Charge Recycling Logic Data Links for Single and Multiple Channel I/Os."
- 2023-06 · Rucheng Jiang (Ph.D. student) got his paper on 2b/Cycle Cyclic ADC accepted to IEEE European Solid-State Circuits Conference (ESSCIRC).
- 2023-06 · Prof. Jerald Yoo's article on Body Area Network (BAN) for communication and powering is published in Spring Edition of IEEE Solid-State Circuits Magazine.
- 2023-05 · Prof. Jiamin Li (Ph.D. graduate) got her paper accepted to IEEE Symposium on VLSI Circuits (VLSI). The paper title is "Wireless Body-Area Network Transceiver ICs with Concurrent Body-Coupled Powering and Communication using Single Electrode."
- 2023-05 · Jiaqi Guo (Ph.D. student) got his paper on power management circuit for ultrasound ASIC accepted to IEEE Solid-State Circuit Letters (SSC-L).
- 2022-11 · Prof. Jerald Yoo presented a keynote talk at IEEE Brain Discovery Neurotechnology Workshop-Brain Mind Body Cognitive Engineering for Health and Wellness.
- 2022-09 · Liuhao Wu (Ph.D. student) got his paper accepted to IEEE Journal of Solid-State Circuits (JSSC). The paper title is "An Ultrasound Imaging System With On-Chip Per-Voxel RX Beamfocusing for Real-Time Drone Applications".
- 2022-07 · Jiaqi Guo (Ph.D. student) got his paper on power management circuit for ultrasound ASIC accepted to IEEE Asian Solid-State Circuits Conference (A-SSCC).
- 2022-07 · Dr. Han Wu (Ph.D. graduate) got his paper on energy-recycling memory interface circuit accepted to IEEE Asian Solid-State Circuits Conference (A-SSCC).
- 2022-06 · Prof. Jerald Yoo presented an invited talk at IEEE International Microwave Symposium (IMS) Workshop on Human Body Communications.
- 2022-06 · Dr. Han Wu (Ph.D. graduate) got his paper accepted to IEEE Journal of Solid-State Circuits (JSSC). The paper title is "An Ultrasound ASIC with Universal Energy Recycling for >7-m All-weather Metamorphic Robotic Vision".
- 2022-05 · Chne-Wuen Tsai (Ph.D. student) got his paper accepted to IEEE International Conference on Artificial Intelligence Circuits and Systems (AICAS). The paper title is "A Closed-Loop Brain-Machine Interface with One-Shot Learning and Online Tuning for Patient-Specific Neurological Disorder Treatment."
- 2022-03 · Dr. Tao Tang (Former Research Fellow, now a PI at Zhejiang Labs) got his paper accepted to IEEE Transactions on Biomedical Circuits and Systems (TBioCAS). The paper title is "Group-Chopping: An 8-Channel, 0.04% Gain Mismatch, 2.1uW 0.017mm2 Instrumentation Amplifier for Bio-potential Recording."
- 2022-03 · Prof. Jerald Yoo's Circuit Insights talk Circuits for Human Health is now available online.
- 2022-02 · Prof. Jerald Yoo will serve as an Associate Editor of IEEE Transactions on Biomedical Circuits and Systems.
- 2022-01 · Miaolin Zhang and Lian Zhang (Ph.D. students) got their paper accepted to IEEE Journal of Solid-State Circuits (invited). The paper title is "A Patient-Specific Closed-Loop Epilepsy Management SoC with One-Shot Learning and Online-Tuning".
- 2021-12 · Prof. Jerald Yoo will be presenting at the inaugural ISSCC Circuit Insights event.

## 연락과 위치

- 주소: 1 Gwanak-ro, Office 301-906, Gwanak-gu, Seoul, Korea 08826[^profile]
- 전화: +82-2-880-1776[^profile][^eceprof]
[^profile]: 교수 누리집 About 페이지 <https://www.jeraldyoo.com/jeraldyoo_profile.html> (첫 화면 <https://www.jeraldyoo.com>이 넘어가는 쪽. 이름·직함, Biography, Professional Activities, Career, Education, Contacts, 2026-10-25 열람)
[^project]: 교수 누리집 Research and Projects 페이지 <https://www.jeraldyoo.com/jeraldyoo_project.html> (Yoo Group Research and Projects 칸, 2026-10-25 열람)
[^pubs]: 교수 누리집 Publications 페이지 <https://www.jeraldyoo.com/jeraldyoo_publication.html> (Journal Papers, Conference Papers, Book Chapters, Patents 칸, 2026-10-25 열람)
[^news]: 교수 누리집 News 페이지 <https://www.jeraldyoo.com/jeraldyoo_news.html> (Recent News, 2026-10-25 열람)
[^people]: 교수 누리집 People 페이지 <https://www.jeraldyoo.com/jeraldyoo_people.html> (Yoo Group Members의 Principal Investigator, Research Staffs, Students, Alumni 칸, 2026-10-25 열람)
[^ecelab]: 서울대학교 전기·정보공학부 연구실 목록 <https://ece.snu.ac.kr/research-faculty/research/lab> (생체전자정보, 인공지능 및 머신러닝, 집적회로, 회로 및 시스템 연구그룹, 2026-10-25 열람)
[^ecelabv]: 서울대학교 전기·정보공학부 연구실 상세(고성능 집적마이크로시스템 연구실) <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=135> (국·영문 이름, 지도, 연구, 최근 관심분야 및 주요 연구과제, 2026-10-25 열람)
[^eceprof]: 서울대학교 전기·정보공학부 교수 상세(유담) <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p895> (TEL, OFFICE, 학위, 전공, 분야, 학력, 주요경력, Research Interest, 2026-10-25 열람)
[^eceen]: 서울대학교 전기·정보공학부 영문 교수 상세(Yoo, Jerald) <https://ece.snu.ac.kr/en/research-faculty/faculty/fulltime?md=view&profid=p895> (Major, Research Areas, Career, Research Interest, 2026-10-25 열람)
[^p1]: R. Jiang 외, J. Yoo, IEEE Transactions on Circuits and Systems I: Regular Papers 73, 5142-5153 (2026). <https://doi.org/10.1109/tcsi.2026.3690163> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J. S. Y. Tan 외, J. Yoo, Science Advances 12, eaec9803 (2026). <https://doi.org/10.1126/sciadv.aec9803> 초록 기준.
[^p3]: Z. Li 외, J. Yoo, 2025 IEEE European Solid-State Electronics Research Conference (ESSERC), 425-428 (2025). <https://doi.org/10.1109/esserc66193.2025.11214087> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: J. Guo 외, J. Yoo, IEEE Transactions on Circuits and Systems I: Regular Papers 73, 4246-4258 (2026). <https://doi.org/10.1109/tcsi.2025.3645401> 초록 기준(Semantic Scholar 등록 초록).
[^falcon]: IEEE Journal of Solid-State Circuits 서지 기록 「Falcon: Event-Driven Hybrid Object Tracking SoC With Bit-Column-Similarity-Based MRAM PIM and Heterogeneous Read-Only-Once Attention Flow」 <https://doi.org/10.1109/jssc.2026.3680504> (61권 9호, 5084-5097쪽, 2026년 9월, 2026-10-25 확인)

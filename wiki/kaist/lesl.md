# 저차원 전자 시스템 연구실 (Low-dimensional Electron Systems Lab, LESL)

**KAIST 전기및전자공학부 · 이가영 교수**

- 분야: 저차원 반도체 물리(2차원 물질의 전하 수송과 양자 현상), 나노 전자·광전자 소자(양극성 트랜지스터, 3진 논리 소자, 광검출기), 반데르발스 접촉, 저전력 터널링 소자
- 홈페이지: <https://lesl.kaist.ac.kr/>
- 근거와 출처: [LESL 근거 페이지](lesl-sources.md)

> 원자 몇 겹 두께의 얇은 반도체 속에서 전자가 어떻게 움직이는지 재고, 그 성질을 살려 실리콘 다음 세대의 트랜지스터와 빛 센서를 만드는 연구실이다. 한 소자가 여러 기능을 바꿔 가며 하도록 하거나, 0과 1 사이에 중간 상태를 하나 더 두어 정보를 더 많이 담는 소자를 만든다.[^home][^research]

## 무엇을 연구하나

반도체 회로를 계속 작게 만들다 보면 전자의 양자적 성질이 드러나는 나노미터 크기에 이른다. 연구실은 실리콘이 한계에 가까워지는 지금 더 작고 빠르며 전력을 덜 쓰는 소자가 필요하다고 보고, 나노 구조 속 전자의 움직임(전하 수송)을 연구한다. 목표는 두 가지로, 새로 등장한 저차원 물질(두께나 폭이 원자 몇 개 수준이라 전자가 평면이나 선 안에서만 움직이는 물질)과 그 적층 구조의 기본 전기적 성질을 이해하는 것, 그리고 이를 바탕으로 성능이 뛰어난 나노 소자를 실제로 구현하는 것이다.[^home]

연구 대상은 주로 2차원 반데르발스 물질이다. 층과 층이 약한 힘으로만 붙어 있어 한 겹씩 떼어 쌓을 수 있는 물질로, 이황화몰리브데넘(MoS2), 인듐셀레나이드(InSe), 흑린 같은 반도체가 여기에 속한다. 연구실은 이런 2차원 반도체가 작게 만들어도 성능이 떨어지지 않아 실리콘을 대신할 후보지만, 금속 전극과 맞닿는 곳의 저항이 크고 페르미 준위 고정(전극 금속을 바꿔도 전류를 막는 장벽 높이가 거의 그대로 남는 현상) 때문에 p형(전자가 빠진 자리인 정공이 전류를 나르는 형) 소자를 만들기 어렵다는 점을 산업화의 걸림돌로 꼽는다.[^research]

이 문제를 풀기 위해 연구실은 반도체 표면에 결함을 만들지 않는 반데르발스 접촉을 개발해, 원래 전자만 잘 흐르던 MoS2와 InSe에서 전자와 정공이 모두 흐르는 양극성 동작을 얻었다고 소개한다. 이를 이용해 한 소자의 기능을 전기로 바꿔 쓰는 재구성 소자를 만들고, 이 소자로 이루어진 회로까지 보이는 것이 다음 목표다.[^research] 대표 논문에서는 이 접촉으로 InSe에서 강한 p형 동작을 얻었고,[^p5] 0과 1 외에 중간 상태를 하나 더 쓰는 3진 트랜지스터를 만들었다.[^p2][^p4]

또 하나의 축은 물질 자체의 물리다. 연구실은 전자 밀도에 따른 전자 에너지(페르미 에너지)를 직접 재는 수송 분광 기법을 갖고 있어, 밴드갭(전자가 가질 수 없는 에너지 구간의 폭)과 유효 질량(결정 속 전자가 움직일 때 보이는 겉보기 질량) 같은 기본 성질을 얻고, 양자 홀 효과(강한 자기장 속 2차원 전자의 전기저항이 계단처럼 정해진 값을 갖는 현상) 같은 양자 상태의 에너지를 잰다고 적는다.[^research] 대표 논문에서는 InSe 속 전자가 강한 전기장에서 낼 수 있는 최고 속도를 재고,[^p6] 절대온도 1.5도 부근의 극저온에서 정공이 움직이는 방식을 밝혔다.[^p1]

마지막으로 저전력 소자와 센서를 만든다. 문턱 아래에서 전류를 더 가파르게 켜고 끄는 터널링 트랜지스터를 반데르발스 접촉으로 구현하려 하고, 같은 기술을 감도가 높은 센서와 양자 센서로 넓힌다고 소개한다.[^research] 대표 논문에서는 외부 전원 없이 빛을 감지하는 MoS2 광검출기와[^p3] 가시광부터 근적외선까지 감지하는 InSe 광검출기를 만들었다.[^p8]

## 주요 연구 주제

### 1. 양극성 2차원 반도체와 재구성 소자

결함 없는 반데르발스 접촉으로 MoS2·InSe·흑린에서 전자와 정공을 모두 흘리고, 한 소자를 트랜지스터·정류기·다이오드로 바꿔 쓰거나 3진 논리 소자로 쓴다.[^research][^p2][^p4][^p5][^p7] 대표 논문 2, 4, 5, 7.

### 2. 인듐셀레나이드의 전하 수송 물리

이동도(전하가 물질 속에서 움직이는 쉬움)가 높은 InSe에서 고전기장 수송과 극저온 정공 수송을 잰다.[^p1][^p6] 대표 논문 1, 6.

### 3. 2차원 물질 광검출기

pn 접합과 표면 도핑으로 외부 전원 없이도 빛을 감지하는 소자를 만든다.[^p3][^p8] 대표 논문 3, 8.

## 대표 논문

랩 논문 목록의 2021–2026년 논문 가운데 이가영 교수가 교신저자(랩 표기 *)인 것에서 세 연구 주제를 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2026 | [Cryogenic hole transport in 2D indium selenide](https://doi.org/10.1021/acsnano.6c07680) · ACS Nano | 2차원 InSe는 실리콘 이후 반도체 후보지만 지금까지는 거의 n형으로만 쓰였다. 일함수가 큰 백금 하부 전극과 육방정 질화붕소(절연성 2차원 물질) 덮개로 p형 InSe 트랜지스터를 만들어 1.5 K까지 정공을 주입했고, 이동도가 3,000 cm²/(V·s)를 넘었다. 낮은 전하 밀도에서 금속-절연체 교차(crossover)가 나타나는 등 InSe의 정공 수송 특성을 밝혀 극저온 전자공학용 p형 반도체 선택지를 넓혔다.[^p1] | 1저자 Yongwook Seok, 교신 이가영 |
| 2 | 2026 | [Binary-to-ternary reconfigurable transistors using plasma-assisted MoS2](https://doi.org/10.1002/adfm.77555) · Advanced Functional Materials | 3진 논리는 소자 하나에 2진보다 많은 정보를 담아 회로를 단순하게 만들 수 있다. 게이트(전압으로 전류를 조절하는 단자)가 둘인 MoS2 동종접합(같은 물질 안에서 성질을 달리해 만든 접합)의 전극 쪽만 산소 플라즈마로 처리해 뚜렷한 중간 상태를 만들었고, 이 트랜지스터를 전기로 2진 트랜지스터로도 바꿀 수 있게 해 회로 복잡도와 에너지 소모가 적은 2진-3진 변환기를 보였다.[^p2] | 공동 1저자 Yeonghyeon Ko·Jungi Song, 교신 이가영 |
| 3 | 2026 | [Gated pn junction in ambipolar MoS2 for superior self-powered photodetection](https://doi.org/10.1002/adfm.202510113) · Advanced Functional Materials | 외부 전원 없이 동작하는 광검출기는 저전력 모바일 기기의 핵심 부품이 될 수 있지만, MoS2는 n형 성질이 강해 pn 접합을 만들기 어렵다. 백금과 흑연 하부 전극을 비대칭으로 두고 게이트를 일부에만 거는 구조로 정공 주입을 쉽게 해, 복잡한 적층이나 화학 도핑 없이 광응답도(받은 빛의 세기에 비해 나오는 전류) 21 A/W 이상의 자가 구동 광검출기를 만들었다.[^p3] | 공동 1저자 Jaeha Hwang·Jungi Song, 교신 이가영 |
| 4 | 2025 | [Ternary transistors with reconfigurable polarities](https://doi.org/10.1002/adfm.202502112) · Advanced Functional Materials | 다치 논리 회로는 면적·복잡도·전력을 함께 줄일 수 있지만, 안정적인 중간 상태를 가진 p형과 n형 다치 트랜지스터는 드물었다. 몇 겹 흑린 동종접합에 비대칭 전극과 제어 게이트를 달아 p형 3진 동작과 n형 3진 동작을 전기로 오갈 수 있는 트랜지스터를 만들었다.[^p4] | 공동 1저자 Dongju Yeom·Yeonghyeon Ko·Youngkyu Ko, 교신 이가영 |
| 5 | 2024 | [Superior p-type switching in InSe nanosheets for complementary multifunctional systems](https://doi.org/10.1021/acs.nanolett.4c04624) · Nano Letters | InSe는 원래 n형 성질 때문에 주로 n형 소자로 쓰였다. 반데르발스 하부 전극으로 p형 켜짐/꺼짐 전류비가 10⁹를 넘는 양극성 트랜지스터를 만들고, 게이트를 일부에만 거는 구조로 같은 소자를 n형·p형 트랜지스터, 정류기(전류를 한쪽으로만 흘리는 소자), 항복 다이오드(일정 전압을 넘으면 전류가 갑자기 흐르는 다이오드)로 바꿔 쓰는 기능을 보였다.[^p5] | 공동 1저자 Minsu Kim·Dongju Yeom·Yongwook Seok, 교신 이가영 |
| 6 | 2024 | [High-field transport and high saturation velocity in multilayer indium selenide transistors](https://doi.org/10.1021/acsnano.3c11613) · ACS Nano | 고주파 전자 소자에는 강한 전기장에서 전자가 내는 최고 속도(포화 속도)가 높아야 한다. 질화붕소 위에 놓고 얇은 인듐 층으로 덮은 다층 InSe에서 상온 이동도 2,600 cm²/(V·s), 포화 속도 2×10⁷ cm/s 이상을 얻어 밴드갭이 있는 다른 반데르발스 반도체보다 높았고, 양자컴퓨터 근처에서 쓰는 극저온 제어 전자소자로 쓸 가능성을 보였다.[^p6] | 1저자 Yongwook Seok, 교신 이가영 |
| 7 | 2024 | [Drain-induced multifunctional ambipolar electronics based on junctionless MoS2](https://doi.org/10.1021/acsnano.3c09876) · ACS Nano | 백금 하부 전극을 단 양극성 MoS2 트랜지스터에서 드레인 전압으로 전하 종류를 바꾸는 방식을 써서, 한 소자가 양극성 트랜지스터, 정류기, 항복 전압을 조절할 수 있는 다이오드, 광검출기로 동작하게 했다. 복잡한 적층이나 도핑 없이 상보형 인버터(신호를 뒤집는 기본 논리 회로)도 만들었다.[^p7] | 공동 1저자 Jungi Song·Suyeon Lee, 교신 이가영 |
| 8 | 2021 | [High performance near-infrared photodetectors based on surface-doped InSe](https://doi.org/10.1002/adfm.202006788) · Advanced Functional Materials | InSe 표면 윗부분만 염화금으로 도핑하고 몇 겹 그래핀을 전극으로 써서, 470–980 nm 파장의 빛을 감지하는 광검출기를 만들었다. 게이트 전압 없이 동작하는 기존 2차원 물질 적외선 광검출기보다 성능이 높았고, 질화붕소로 덮어 3개월 동안 안정했다.[^p8] | 1저자 Hanbyeol Jang, 교신 이가영 |

## 교수와 전문 분야

이가영 교수는 연세대 전기전자공학 학사(2009) 뒤 미국 텍사스대 오스틴에서 전기·컴퓨터공학 석사(2012)와 박사(2016)를 받았고, 스탠퍼드대 박사후연구원(2016–2017), 광주과학기술원 신소재공학부 조교수(2018–2020)를 거쳐 2021년 KAIST 전기및전자공학부에 왔다. 2024년부터 부교수이며 반도체시스템공학과와 반도체공학대학원에도 소속돼 있다고 적는다.[^pi] 안보과학기술대학원 교수 명단에도 전기및전자공학부 소속으로 올라 있고, 세부 분야를 저차원물질, 반도체 물리학, 나노구조 전자소재로 적는다.[^gst]

랩이 적은 수상으로는 ICAMD 2025 Young Researcher Award, 2024 KAIST 공과대학 기술혁신상, 2023 KAIST Q-Day Faculty Special Award(연구 부문), 2022 한국그래핀학회 신진학술상, 2020 POSCO TJ Park Foundation의 POSCO Science Young Faculty Fellowship이 있다.[^pi] 박사과정 시절 이중층 그래핀의 양자 홀 상태를 다룬 1저자 논문이 Science(2014) 표지에 실렸다고 논문 목록에 적혀 있다.[^papers]

논문으로 보면 전문 분야는 세 갈래다.

- **2차원 반도체의 금속 접촉과 양극성·다치 소자**.[^p2][^p4][^p5][^p7]
- **저차원 물질의 전하 수송 측정과 물리**.[^p1][^p6]
- **2차원 물질 광검출기**.[^p3][^p8]

## 응용 분야

대표 논문으로 보면 전력을 적게 쓰는 논리 회로와 3진 논리 회로,[^p2][^p4] 외부 전원 없이 동작하는 모바일 기기용 광센서,[^p3] 적외선 감지,[^p8] 양자컴퓨터 곁에서 쓰는 극저온·고주파 전자소자에 닿아 있다.[^p1][^p6] 연구실은 2024년 Nano Letters와 ACS Nano 논문들이 여러 언론에 보도됐다고 적는다.[^papers] 졸업생은 삼성전자, 삼성 반도체연구소, 한국세라믹기술원 등으로 진출했다.[^team]

## 구성원

2026년 10월 20일 랩 Team 페이지 기준이다. 대학원생은 랩이 과정을 적지 않은 경우 "대학원생"으로 썼고, 이메일은 랩이 적은 학교 주소다.[^team] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Yongwook Seok | 박사후연구원 | seok5162@kaist.ac.kr | 1, 2, 3, 4, 5, 6, 7, 8 |
| Jungi Song | 석박사통합과정 | sjg731@kaist.ac.kr | 2, 3, 4, 5, 7 |
| Minsu Kim | 석박사통합과정 | sidlilac@kaist.ac.kr | 1, 2, 5 |
| Dongju Yeom | 대학원생 | 1500dd87a8@kaist.ac.kr | 1, 4, 5 |
| Jaeha Hwang | 대학원생 | jhhwang@kaist.ac.kr | 1, 3, 4 |
| Yeonghyeon Ko | 대학원생 | yhgo19@kaist.ac.kr | 2, 4, 5, 6, 7 |
| Hakyeong Kim | 대학원생 | hakyeong.kim@kaist.ac.kr |  |
| Seongje Moon | 대학원생 | msj9905@kaist.ac.kr | 1, 2 |
| Jinwook Do | 대학원생 | jndo915@kaist.ac.kr |  |
| Giwan Kim | 대학원생 | tnlfna64@kaist.ac.kr |  |
| Geunwoo Jung | 대학원생 | geunwoo7777@kaist.ac.kr |  |
| Yunsik Woo | 대학원생 | woo2163@kaist.ac.kr |  |
| Geunchang Kim | 대학원생 | gc9771@kaist.ac.kr |  |
| Yue (Juliet) Zhu | 대학원생 | zzzhujuliettt@kaist.ac.kr |  |
| Seunghwan Lee | 학부 연구생 (Individual Study) |  |  |
| Hyeongjun Choi | 학부 연구생 (Individual Study) |  |  |
| Eungchan Jeong | 학부 연구생 (Individual Study) |  |  |
| Hak Gyeom Kim | 학부 연구생 (Individual Study) |  |  |
| Junhyeok Lee | 학부 연구생 (Individual Study) |  |  |
| Chae Yeon Park | 학부 연구생 (Individual Study) |  |  |
| Seonmin Yu | 학부 연구생 (Individual Study) |  |  |
| Ayoung Oh | 학부 연구생 (Individual Study) |  |  |

## 졸업생

랩 Team 페이지의 지난 구성원(학위·연도·진로)과 학부 연구생(참여 연도)이다.[^team]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hanbyeol Jang | MSE PhD (2023) | Samsung Semiconductor R&D Center |
| Suyeon Lee | EE MS (2024) | Samsung Electronics |
| Seokhun Jin | EE MS (2025) | Samsung Electronics |
| Sang-Hoo Cho | MSE MS (2020) | Samsung Electronics |
| Yitaek Choi | MSE MS (2020) | Samsung Semiconductor R&D Center |
| Sang-Soo Chee | MSE PhD (2019) | Korea Institute of Ceramic Engineering and Technology |
| Sanghyun Kim | 연구원 (2018-2020) | Prof. Joo-Hyung Lee's group |
| Donghyeon Lee | 연구원 (2018-2020) | Prof. Sanghan Lee's group |
| Seung-Jae Baek | 학부 연구생 (2026) |  |
| RokYeong Kim | 학부 연구생 (2026) |  |
| Seoyoung Moon | 학부 연구생 (2026) |  |
| Hosung Lee | 학부 연구생 (2026) |  |
| Chae Yeon Park | 학부 연구생 (2026) |  |
| Mingyo Jang | 학부 연구생 (2026) |  |
| Do Hoon Kim | 학부 연구생 (2026) |  |
| Jeong Su Lee | 학부 연구생 (2026) |  |
| Jaewoo Jeon | 학부 연구생 (2026) |  |
| Giwan Kim | 학부 연구생 (2026) |  |
| Geunchang Kim | 학부 연구생 (2026) |  |
| Yunsik Oh | 학부 연구생 (2026) |  |
| Sang Hyun Kim | 학부 연구생 (2026) |  |
| Taehun Park | 학부 연구생 (2026) |  |
| Hyeongjun Choi | 학부 연구생 (2026) |  |
| Taehoon Kim | 학부 연구생 (2026) |  |
| Eungchan Jeong | 학부 연구생 (2026) |  |
| Sohyeon Park | 학부 연구생 (2026) |  |
| Soochul Shin | 학부 연구생 (2026) |  |
| Eungchan Lee | 학부 연구생 (2026) |  |
| Seunghwan Lee | 학부 연구생 (2025) |  |
| Jaewoo Lee | 학부 연구생 (2025) |  |
| Hyeon Seo Kang | 학부 연구생 (2025) |  |
| Seohyun Lee | 학부 연구생 (2025) |  |
| Geunchang Kim | 학부 연구생 (2025) |  |
| Eunjune Heo | 학부 연구생 (2025) |  |
| Yoonji Byun | 학부 연구생 (2025) |  |
| Seongyoon Kim | 학부 연구생 (2025) |  |
| Joonha Yang | 학부 연구생 (2024) |  |
| Yoonji Byun | 학부 연구생 (2024) |  |
| Sungbin Park | 학부 연구생 (2024) |  |
| Jaewoo Lee | 학부 연구생 (2024) |  |
| Mingu Ko | 학부 연구생 (2024) |  |
| Jaeyeon Eom | 학부 연구생 (2024) |  |
| Dakyeong Seo | 학부 연구생 (2024) |  |
| Yeonjun Jung | 학부 연구생 (2024) |  |
| Birm Jin Kim | 학부 연구생 (2024) |  |
| Jin Gang Lim | 학부 연구생 (2024) |  |
| Taehyeong Kim | 학부 연구생 (2024) |  |
| Siheon Park | 학부 연구생 (2024) |  |
| Woojun Choi | 학부 연구생 (2024) |  |
| Jun Yeong Yun | 학부 연구생 (2024) |  |
| Sungjin Lee | 학부 연구생 (2023) | UNIST |
| Jihun Baek | 학부 연구생 (2023) |  |
| Yeonghyeon Go | 학부 연구생 (2023) |  |
| Seungbeen Noh | 학부 연구생 (2023) |  |
| Ha Young Lee | 학부 연구생 (2023) |  |
| Woobeen Oh | 학부 연구생 (2023) |  |
| Jiwi Park | 학부 연구생 (2023) | DGIST |
| Min Gyu Lee | 학부 연구생 (2022) |  |
| Jun Mo Kim | 학부 연구생 (2022) |  |
| Dahyun Gil | 학부 연구생 (2022) |  |
| Dongju Yeom | 학부 연구생 (2022) |  |
| Jaehwan Hyun | 학부 연구생 (2022) |  |
| Hosang Hwang | 학부 연구생 (2022) |  |
| Yeonghyeon Go | 학부 연구생 (2022) |  |
| Minsu Kim | 학부 연구생 (2021) |  |
| Jungi Song | 학부 연구생 (2021) |  |
| Junsik Cho | 학부 연구생 (2020) |  |
| Jungwook Lee | 학부 연구생 (2020) |  |
| Jungwon Oh | 학부 연구생 (2019) |  |
| Donghyeon Lee | 학부 연구생 (2018) |  |
| Yongwook Seok | 학부 연구생 (2018) |  |

## 최근 논문 목록 (2021–2026)

랩 논문 목록의 2021년 이후 학술지 논문이다. 저자 이름 뒤 #은 공동 1저자를 뜻하는 랩 표기다.[^papers]

**2026**

- Yongwook Seok, Seongje Moon, Minsu Kim, Dongju Yeom, Jaeha Hwang, Kenji Watanabe, Takashi Taniguchi, and Kayoung Lee. "Cryogenic hole transport in 2D indium selenide". *ACS Nano, in press (2026)*.
- Yeonghyeon Ko,# Jungi Song,# Minsu Kim, Yongwook Seok, Seongje Moon, Kenji Watanabe, Takashi Taniguchi, and Kayoung Lee. "Binary-to-ternary reconfigurable transistors using plasma-assisted MoS2". *Advanced Functional Materials, in press (2026)*.
- Jaeha Hwang,# Jungi Song,# Hanbyeol Jang, Yongwook Seok, Jiwi Park, Suyeon Lee, Jun-Hyeok Choi, Gyeongsu Lee, Kenji Watanabe, Takashi Taniguchi, Byoung Hun Lee, Kyoungsik Yu, and Kayoung Lee. "Gated pn junction in ambipolar MoS2 for superior self-powered photodetection". *Advanced Functional Materials 36, e10113 (2026)*.

**2025**

- Minyoung Lee,# Changho Kim,# Soon-Yong Kwon, Kayoung Lee, Giyoon Kwak, Hyunseob Lim, and Jae Hun Seol. "Residue-free fabrication of two-dimensional materials using van der Waals interactions". *Advanced Materials 37, 2418669 (2025)*.
- Dongju Yeom,# Yeonghyeon Ko,# Youngkyu Ko,# Heungsoon Im, Jungi Song, Yongwook Seok, Hanbyeol Jang, Jaeha Hwang, Seokhun Jin, Kenji Watanabe, Takashi Taniguchi, and Kayoung Lee. "Ternary transistors with reconfigurable polarities". *Advanced Functional Materials 35, 2502112 (2025)*.

**2024**

- Minsu Kim,# Dongju Yeom,# Yongwook Seok,# Jungi Song, Hanbyeol Jang, YiTaek Choi, Yeonghyeon Ko, Kenji Watanabe, Takashi Taniguchi, and Kayoung Lee. "Superior p-type switching in InSe nanosheets for complementary multifunctional systems". *Nano Letters 24, 16090 (2024)*.
- Yongwook Seok, Hanbyeol Jang, YiTaek Choi, Yeonghyeon Ko, Minje Kim, Heungsoon Im, Kenji Watanabe, Takashi Taniguchi, Jae Hun Seol, Sang-Soo Chee, Junghyo Nah, and Kayoung Lee. "High-field transport and high saturation velocity in multilayer indium selenide transistors". *ACS Nano 18, 8099 (2024)*.
- Jungi Song,# Suyeon Lee,# Yongwook Seok, Yeonghyeon Ko, Hanbyeol Jang, Kenji Watanabe, Takashi Taniguchi, and Kayoung Lee. "Drain-induced multifunctional ambipolar electronics based on junctionless MoS2". *ACS Nano 18, 4320 (2024)*.

**2022**

- Hanbyeol Jang, Yumin Song, Yongwook Seok, Heungsoon Im, Tae Hyung Kim, Joo-Hyoung Lee, Yong-Hoon Kim, and Kayoung Lee. "Zero power infrared sensing in 2D/3D-assembled heterogeneous graphene/In/InSe/Au". *Nanoscale 14, 3004 (2022)*.

**2021**

- Sang-Hoo Cho, Hanbyeol Jang, Heungsoon Im, Donghyeon Lee, Je-Ho Lee, Kenji Watanabe, Takashi Taniguchi, Maeng-Je Seong, Byoung Hun Lee, and Kayoung Lee. "Bias-controlled multi-functional transport properties of InSe/BP van der Waals heterostructures". *Scientific Reports 11, 7843 (2021)*.
- Sanghyun Kim,# Donghyeon Lee,# Binbin Wang, Shangjie Yu, Kenji Watanabe, Takashi Taniguchi, Jonathan A. Fan, Jiamin Xue, and Kayoung Lee. "Raman spectroscopic study of artificially twisted and non-twisted trilayer graphene". *Applied Physics Letters 118, 133101 (2021)*.
- YiTaek Choi,# Yongwook Seok,# Hanbyeol Jang,  Arvind Kumar, Kenji Watanabe, Takashi Taniguchi, Xuan Gao, and Kayoung Lee. "Multiterminal transport measurements of multilayer InSe encapsulated by hBN". *ACS Applied Electronic Materials 3, 163 (2021)*.
- Hanbyeol Jang, Yongwook Seok, YiTaek Choi, Sang-Hoo Cho, Kenji Watanabe, Takashi Taniguchi, and Kayoung Lee. "High performance near-infrared photodetectors based on surface-doped InSe". *Advanced Functional Materials 31, 2006788 (2021)*.

## 수상

랩 PI 페이지에 적힌 교수의 수상이다.[^pi]

- 2025 · Young Researcher Award, 14th International Conference on Advanced Materials and Devices (ICAMD 2025)
- 2024 · Technology Innovation Award (기술혁신상) of College of Engineering, KAIST
- 2023 · KAIST Q-Day Faculty Special Award - Research Category, KAIST
- 2022 · Young Faculty Award (신진학술상), Korean Graphene Society
- 2020 · POSCO Science Young Faculty Fellowship, POSCO TJ Park Foundation
- 2015 · Ben Streetman Award, The University of Texas at Austin
- 2015 · Best Paper Award, KSEA (Korean-American Scientists and Engineers Association) Austin

## 소식

랩 News 페이지의 2021년 이후 논문·수상·학위 소식이다.[^news]

- 27 August 2026 · Yeonghyeon, Jungi, Minsu, Yongwook, Seongje, and Kayoung have published a new paper in Advanced Functional Materials, “Binary-to-ternary reconfigurable transistors using an MoS2 homojunction.” Congrats!
- 25 August 2026 · Yongwook, Seongje, Minsu, Dongju, Jaeha, and Kayoung have published a new paper in ACS Nano, “Cryogenic hole transport in 2D indium selenide.” Congrats!
- 10 June 2026 · Congratulations to Hakyeong Kim for successfully defending her Master thesis! We are so proud of you.
- 12 December 2025 · Congratulations to Dongju for receiving the Best Poster Award and to Kayoung for receiving the Young Researcher Award at the 14th International Conference on Advanced Materials and Devices (ICAMD 2025)!
- 26 November 2025 · Congratulations to Yongwook Seok for successfully defending his PhD thesis! We are so proud of you.
- 9 July 2025 · Jaeha, Jungi, Hanbyeol, Yongwook, Suyeon, and Kayoung have published a new paper in Advanced Functional Materials, “Gated pn junction in ambipolar MoS2 for superior self-powered photodetection.” Congrats!
- 20 June 2025 · Congratulations to Yeonghyeon and Seokhun for successfully defending their Master theses! We are so proud of you.
- 3 April 2025 · Dongju, Yeonghyeon, Heungsoon, Jungi, Yongwook, Hanbyeol, Jaeha, Seokhun, and Kayoung have published a new paper in Advanced Functional Materials, “Ternary transistors with reconfigurable polarities.” Congrats!
- 27 December 2024 · Kayoung was honored with the 2024 Technology Innovation Award (기술혁신상) of College of Engineering at KAIST.
- 20 December 2024 · Congratulations to Dongju and Jaeha for successfully defending their Master theses! We are so proud of you.
- 18 December 2024 · Minsu, Dongju, Yongwook, Jungi, Hanbyeol, YiTaek, Yeonghyeon, and Kayoung have published a new paper in Nano Letters, “Superior p-type switching in InSe nanosheets for complementary multifunctional systems.” Congrats!
- 27 November 2024 · Minsu and Youngkyu received the Oral Session Awards at ENGE. Congratulations! We are so happy for you!
- 18 November 2024 · Yongwook received the Best Graduate Student Paper Award from KAIST EE. Congratulations! This is very exciting, and we are so happy for you!
- 12 July 2024 · Jaeha received the Merck Best Oral Presentation Award at the 11th Korean Symposium on Graphene and 2D Materials. Congratulations! We are so happy for you!
- 26 April 2024 · Youngkyu received the Best Presentation Award at 2024 KPS Spring Meeting. Congratulations! We are so happy for you!
- 19 March 2024 · Yongwook, Hanbyeol, YiTaek, Yeonghyeon, Heungsoon, Sang-Soo, and Kayoung have published a new paper in ACS Nano, “High-field transport and high saturation velocity in multilayer indium selenide transistors.” Congrats!
- 26 January 2024 · Jungi, Suyeon, Yongwook, Yeonghyeon, Hanbyeol, and Kayoung have published a new paper in ACS Nano, “Drain-induced multifunctional ambipolar electronics based on junctionless MoS2.” Congrats!
- 12 December 2023 · Congratulations to Suyeon for successfully defending her Master thesis! We are so proud of you.
- 28 November 2023 · Kayoung was honored with the KAIST Q-Day Faculty Special Award in the Research Category.
- 29 November 2022 · Congratulations to Hanbyeol for successfully defending his doctoral thesis!
- 12 July 2022 · Kayoung received 신진학술상 (Early Career Award) from Korean Graphene Society.
- 10 February 2022 · Hanbyeol, Yongwook, Heungsoon, and Kayoung have published a new paper in Nanoscale, “Zero power infrared sensing in 2D/3D-assembled heterogeneous graphene/In/InSe/Au.” Congrats!
- 10 December 2021 · Yongwook received the Best Poster Presentation Award at ICAMD 2021. Congrats! So exciting!
- 14 October 2021 · Hanbyeol received the Best Poster Presentation Award (Silver Medal) at RPGR 2021. Congrats! So exciting!
- 30 August 2021 · Youngkyu Ko and Jungi Song have joined our group as graduate students. Welcome on board!
- 25 June 2021 · Kayoung has been awarded the 2021 C2 (Creative and Challenging) research grant from KAIST!
- 12 April 2021 · Sanghoo, Hanbyeol, Heungsoon, Donghyeon, and Kayoung have published a new paper in Scientific Reports, “Bias-controlled Multi-functional Transport Properties of InSe/BP van der Waals Heterostructures.” Congrats!
- 30 March 2021 · Sanghyun, Donghyeon, and Kayoung have published a new paper in Applied Physics Letters, “Raman Spectroscopic Study of Artificially Twisted and Non-twisted Trilayer Graphene.” Congrats!

## 연락과 위치

- 교수 이메일: kayoung.lee@kaist.ac.kr[^pi]

[^home]: LESL 누리집 첫 화면 <https://lesl.kaist.ac.kr/> (2026-10-20 열람)
[^pi]: LESL PI 페이지 <https://lesl.kaist.ac.kr/pi> (2026-10-20 열람)
[^team]: LESL Team 페이지 <https://lesl.kaist.ac.kr/team> (2026-10-20 열람)
[^research]: LESL Research 페이지 <https://lesl.kaist.ac.kr/research> (2026-10-20 열람)
[^papers]: LESL 논문 목록 <https://lesl.kaist.ac.kr/publications> (2026-10-20 열람)
[^news]: LESL News 페이지 <https://lesl.kaist.ac.kr/news> (2026-10-20 열람)
[^gst]: KAIST 안보과학기술대학원 교수 명단 4쪽 <https://gst.kaist.ac.kr/member/faculty/?page=4> (2026-10-20 열람)
[^p1]: Y. Seok 외, K. Lee, ACS Nano 20, 24439-24446 (온라인 2026-08-25). <https://doi.org/10.1021/acsnano.6c07680> 초록 기준.
[^p2]: Y. Ko 외, K. Lee, Advanced Functional Materials 36, e77555 (온라인 2026-08-26). <https://doi.org/10.1002/adfm.77555> 초록 기준.
[^p3]: J. Hwang 외, K. Lee, Advanced Functional Materials 36, e10113 (온라인 2025-07-26). <https://doi.org/10.1002/adfm.202510113> 초록 기준.
[^p4]: D. Yeom 외, K. Lee, Advanced Functional Materials 35, 2502112 (온라인 2025-04-03). <https://doi.org/10.1002/adfm.202502112> 초록 기준.
[^p5]: M. Kim 외, K. Lee, Nano Letters 24, 16090-16098 (온라인 2024-11-25). <https://doi.org/10.1021/acs.nanolett.4c04624> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: Y. Seok 외, K. Lee, ACS Nano 18, 8099-8106 (온라인 2024-03-07). <https://doi.org/10.1021/acsnano.3c11613> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: J. Song 외, K. Lee, ACS Nano 18, 4320-4328 (온라인 2024-01-26). <https://doi.org/10.1021/acsnano.3c09876> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: H. Jang 외, K. Lee, Advanced Functional Materials 31, 2006788 (온라인 2020-10-16). <https://doi.org/10.1002/adfm.202006788> 초록 기준.

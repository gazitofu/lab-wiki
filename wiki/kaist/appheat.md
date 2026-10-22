# 응용열전달 연구실 (Applied Heat Transfer Lab)

**KAIST 기계공학과 · 김성진 교수**

- 분야: 전자 소자·반도체 냉각(매니폴드 마이크로채널, 진동형 히트파이프, 히트싱크), 마이크로 스케일 열전달과 유동, 풀 비등의 임계 열유속, 히트싱크·열교환기의 최적 설계
- 대분야: 기계·로봇·제조
- 태그: 열전달·열관리[^about][^meres][^p1], 유체역학·유동[^members][^p2]
- 홈페이지: <http://appheat.kaist.ac.kr/>
- 근거와 출처: [응용열전달 연구실 근거 페이지](appheat-sources.md)

> 전자 소자와 반도체에서 나오는 열을 빼내는 냉각 기술을 연구하는 기계공학과 연구실로, 매니폴드 마이크로채널과 진동형 히트파이프 같은 냉각 장치, 끓음 현상의 임계 열유속, 히트싱크의 최적 설계를 실험과 해석으로 다룬다.[^about][^members]

## 무엇을 연구하나

연구실은 KAIST 기계공학과 김성진 교수가 이끄는 응용열전달 연구실이다.[^home][^meteam] 누리집 아래쪽에는 영문 이름 Applied Heat Transfer Lab.과 기계공학과 소속이 적혀 있다.[^home] 기계공학과 교수진 페이지는 교수의 연구분야를 마이크로 스케일 열전달과 유동, 열교환기·히트파이프·히트싱크의 최적 설계로 적고,[^meteam] 기계공학과 연구분야 안내는 교수를 에너지/환경/해양 분야의 핵심교수로 올리며 연구주제로 전자 패키지 냉각 기술, 마이크로 스케일 열전달과 유동, 열교환기·히트파이프·히트싱크의 최적 설계, 다공성 매질의 대류 열전달, 풀 비등의 임계 열유속 메커니즘을 든다.[^meres] 교수 소개의 연구 관심도 전자 패키지 냉각 기술(Cooling Technology for Electronic Packages), 마이크로 스케일 열전달과 유동(Microscale Heat Transfer and Fluid Flow), 열교환기·히트파이프·히트싱크의 최적 설계, 다공성 매질의 대류 열전달 네 가지다.[^members]

연구 소개 페이지는 연구를 네 주제로 나눠 설명한다. 매니폴드 마이크로채널(MMC), 진동형 히트파이프(PHP), 풀 비등의 임계 열유속(CHF) 메커니즘, 위상 최적화 히트싱크다.[^about] 누리집 첫 화면도 매니폴드 마이크로채널과 진동형 히트파이프를 연구 그림의 제목으로 앞세운다.[^home]

첫째 갈래는 **매니폴드 마이크로채널(MMC)로 하는 고열유속 냉각**이다. 연구 소개 페이지는 인공지능 가속기와 고성능 반도체의 집적도가 높아지면서 단위 면적당 나오는 열이 빠르게 늘어, 첨단 전자 소자의 열유속(단위 면적을 지나는 열의 양)이 1,000 W/cm²를 넘는 수준에 이르렀다고 적는다.[^about] 이런 열을 빼려고 반도체 기판 안에 미세한 유로를 만들고 냉각수를 직접 흘리는 마이크로채널 냉각이 연구되지만, 냉각수가 긴 유로를 지나며 압력강하가 커지고 칩 전체에 냉각수가 고르게 가지 않아 온도가 고르지 않은 문제가 있다고 설명한다.[^about] 매니폴드 마이크로채널은 위쪽의 매니폴드(유체를 여러 갈래로 나눠 보내고 다시 모으는 통로)로 냉각수를 여러 개의 짧은 마이크로채널에 나눠 보낸 뒤 다시 모으는 구조로, 냉각수가 흐르는 거리를 줄여 압력강하를 낮추면서 열을 잘 전하게 한다.[^about] 연구실은 매니폴드 마이크로채널 안의 복잡한 열과 유동을 빠르게 예측하는 1차원 모델을 만들고, 이를 3차원 전산유체역학 해석과 묶은 다중 충실도 최적화로 열저항, 압력강하, 유량 균일도를 함께 따진 최적 설계를 했으며, 최적화한 구조를 실리콘 기판에 만들어 냉각 성능을 실험으로 확인했다고 적는다.[^about] 연구 소개 페이지에 따르면 이 구조는 상온의 물로 하는 단상 냉각만으로 약 2,000 W/cm²의 열유속에서 정션 온도를 100 °C 이하로 유지하며 약 8 kPa의 낮은 압력강하를 보였고, 1,180 W/cm²의 열유속에서 성능계수 106,000을 얻어 기존 최고 수준보다 약 10배 높은 에너지 효율을 보였다.[^about] 최근 논문 목록에는 매니폴드 마이크로채널의 1차원 모델(International Communications in Heat and Mass Transfer, 2024), 핀을 세운 매니폴드 마이크로채널의 실험(International Journal of Heat and Mass Transfer, 2024), 성능계수 100,000이 넘는 매니폴드 마이크로채널(Energy Conversion and Management, 2026)이 있다.[^pubs]

둘째 갈래는 **진동형 히트파이프(PHP)**다. 연구 소개 페이지는 전자 장치가 작아지고 집적되면서 제곱센티미터당 열 발생이 수백 와트에 이르러, 열을 잘 옮기는 냉각 장치가 필요하다고 적는다.[^about] 히트파이프는 열을 매우 잘 옮겨 널리 쓰이는데, 그 성질은 안쪽의 윅(wick) 구조에서 나오고 이 구조를 만드는 공정이 복잡해 작게 만들고 집적하기 어렵다고 설명한다.[^about] 진동형 히트파이프는 윅 없이 가는 관 안에서 액체와 기체 덩어리가 번갈아 놓인 상태로 스스로 진동하며 증발부의 열을 응축부로 옮기는 장치이고, 액체와 기체가 번갈아 나타나는 슬러그 유닛은 모세관력에서 생기므로 관의 지름이 작아야 한다고 적는다.[^about] 연구 소개 페이지는 여기에 휘어지는 성질을 더하면 휘는 디스플레이용 냉각 장치, 태양전지, 인공위성 같은 여러 분야에 쓸 수 있다고 적는다.[^about] 대표 논문에서는 진동형 히트파이프에서 진동의 크기가 커질수록 잠열로 옮기는 열의 비중이 커지고 열저항이 줄어드는 것을 실험으로 보였고,[^p1] 평판에 새긴 진동형 히트파이프에서 이웃한 유로 사이의 벽을 통한 열 교환이 성능에 주는 영향을 수치 모델로 따졌으며,[^p2] 진동형 히트파이프 연구의 쟁점과 실용상의 기술 문제를 정리한 리뷰를 냈다.[^p3] 최근 논문 목록에는 수동 체크 밸브를 단 진동형 히트파이프(2023), 우주용 진동형 히트파이프의 응축부 구성(2025), 딥러닝으로 액체 덩어리의 진동을 예측하는 연구(2021), 홈을 낸 유로의 진동형 히트파이프(2024·2025)도 있다.[^pubs]

셋째 갈래는 **풀 비등의 임계 열유속(CHF) 메커니즘**이다. 연구 소개 페이지는 임계 열유속을 풀 비등(고인 액체 속 가열면에서 일어나는 끓음)에서 가장 높은 냉각 성능을 내는 최대 열유속으로 설명한다.[^about] 그동안은 끓는 면의 국부 온도 분포와 기포의 움직임을 자세히 관찰하기 어려워 임계 열유속의 메커니즘을 밝히기 어려웠는데, 연구실은 적외선 카메라로 국부 온도 분포와 열유속을 재어 이 어려움을 넘었다고 적는다.[^about] 젖은 면적의 비율, 접촉선 길이 밀도, 드라이아웃(가열면이 마르는 현상) 발생 지점 사이의 주파수, 마른 부분(dry patch)의 수명과 크기 분포, 접촉선이 나아가고 물러나는 속도, 액체로 덮인 부분의 열전달 등을 쟀고, 열유속에 젖은 면적 비율을 가중해 비등 곡선을 쉽게 얻을 수 있음을 밝혔으며, 제안한 메커니즘을 관측 결과와 비교했다고 적는다.[^about] 최근 논문 목록에는 접촉각에 따른 액체 공급 실패 메커니즘으로 풀 비등의 임계 열유속을 예측하는 모델(International Journal of Heat and Mass Transfer, 2023)이 있다.[^pubs]

넷째 갈래는 **위상 최적화 히트싱크**다. 히트싱크는 핀(fin)으로 열 교환 면적을 넓힌 냉각 장치로, 열을 많이 내는 전자 장치의 냉각에 널리 쓰여 왔다.[^about] 연구 소개 페이지는 전자 장치가 작아지며 히트싱크를 놓을 공간이 좁고 복잡해져 정해진 모양의 핀으로는 최적 형상을 찾기 어려워졌다고 적고, 형상의 제한을 없애려고 히트싱크 설계에 위상 최적화 기법을 쓴다고 설명한다.[^about] 위상 최적화는 계산 영역을 수많은 요소로 나누고 각 요소에 구조물이 있는지 없는지를 변수로 두어, 목적 함수를 최적화하는 방향으로 구조물의 형상이 스스로 바뀌게 하는 기법이다.[^about] 연구실은 이 기법으로 시스템의 형상과 발열 조건에 맞는 자연대류 히트싱크를 제안했고, 강제대류 히트싱크, 열교환기 안의 히트싱크, 상변화 냉각 장치에도 적용하려 한다고 적는다.[^about] 대표 논문에서는 펌프 동력을 고정한 강제대류 히트싱크의 위상 최적화 방법을 제안해 상용 히트싱크보다 총 열저항과 무게를 줄였고,[^p4] 히트싱크 위상 최적화에 쓰는 목적 함수의 정의와 물리적 뜻을 정리했으며,[^p5] 자연대류로 식히는 핀 히트싱크에서 핀 밀도를 흐름 방향으로 바꿔 열저항과 무게를 함께 줄였다.[^p6]

## 주요 연구 주제

### 1. 매니폴드 마이크로채널(MMC)로 하는 고열유속 냉각

반도체 기판 안 미세 유로로 냉각수를 나눠 보내는 매니폴드 마이크로채널의 1차원 모델, 3차원 전산유체역학 해석과 결합한 다중 충실도 최적화, 실리콘 기판 시제작과 냉각 성능 실험.[^about][^pubs]

### 2. 진동형 히트파이프(PHP)

윅 없이 액체와 기체 덩어리의 진동으로 열을 옮기는 진동형 히트파이프의 열전달 메커니즘 실험, 평판형 구조의 수치 모델, 유로 배치와 체크 밸브, 우주용 응축부 설계, 휘는 히트파이프.[^about][^p1][^p2][^p3] 대표 논문 1–3.

### 3. 풀 비등의 임계 열유속(CHF) 메커니즘

적외선 카메라로 끓는 면의 국부 온도와 열유속, 마른 부분과 접촉선의 거동을 재고, 임계 열유속 메커니즘과 예측 모델을 세운다.[^about][^pubs]

### 4. 위상 최적화 히트싱크

강제대류와 자연대류 히트싱크의 위상 최적화와 목적 함수, 핀 밀도를 바꾼 핀 히트싱크의 열 최적화.[^about][^p4][^p5][^p6] 대표 논문 4–6.

## 대표 논문

김성진 교수가 마지막 저자인 2021–2026년 학술지 논문 가운데 초록을 확인할 수 있는 여섯 편을 담았다. 아래 표는 진동형 히트파이프와 위상 최적화 히트싱크 두 갈래를 다루며, 매니폴드 마이크로채널과 임계 열유속 갈래의 논문은 포함하지 않는다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2021 | [Effects of oscillation amplitudes on heat transfer mechanisms of pulsating heat pipes](https://doi.org/10.1016/j.ijheatmasstransfer.2020.120642) · International Journal of Heat and Mass Transfer | 진동형 히트파이프의 열전달 메커니즘이 진동의 크기(진폭)에 따라 어떻게 달라지는지 실험으로 살폈다. 유리 윗판과 실리콘 아랫판으로 다섯 번 굽은 닫힌 고리 모양의 마이크로 진동형 히트파이프를 만들고, 작동 유체로 에탄올을 넣었다. 고속 촬영으로 진폭을, 고속 적외선 촬영으로 유체와 벽 사이의 열유속 분포를 동시에 얻어, 벽과 유체 사이에서 옮겨지는 열을 온도 변화로 옮기는 현열과 증발·응축으로 옮기는 잠열로 나눴다. 넣는 열이 7 W에서 16 W로 늘자 진폭은 3.4 mm에서 8.3 mm로, 전체 열 가운데 잠열의 비중은 54.8%에서 81.9%로 커졌고, 그에 따라 열저항이 13.5% 줄었다. 진폭이나 증발부·응축부의 잠열 비중을 키우면 진동형 히트파이프의 열 성능을 높일 수 있다는 실마리를 제시했다.[^p1] | 1저자 C. Jung, 마지막 저자 김성진 |
| 2 | 2021 | [Investigation into the effect of transverse conduction on the thermal performance of a flat-plate pulsating heat pipe](https://doi.org/10.1016/j.ijheatmasstransfer.2021.121842) · International Journal of Heat and Mass Transfer | 평판에 유로를 새겨 만든 진동형 히트파이프에서 이웃한 유로 사이를 벽을 통해 옆으로 오가는 열전도가 성능에 주는 영향을 수치 해석으로 살폈다. 직사각형 유로 안의 액체·기체 두 상의 흐름을 1차원 모델로, 고체 벽의 열전도를 3차원 모델로 결합한 수치 모델을 만들고 실험으로 검증했다. 이 모델로 벽 재료, 작동 유체, 이웃한 유로 사이의 거리를 바꿔 가며 유로 사이의 열 교환이 있을 때와 없을 때의 열 성능 차이를 비교했다. 그 결과 유로 사이의 열 교환이 열 성능에 크게 영향을 줄 수 있음을 확인하고, 푸리에 수가 일정 값보다 클 때는 이를 반드시 고려해야 한다는 판단 기준을 내놓았다.[^p2] | 1저자 H. Y. Noh, 마지막 저자 김성진 |
| 3 | 2021 | [Fundamental Issues and Technical Problems About Pulsating Heat Pipes](https://doi.org/10.1115/1.4051465) · Journal of Heat Transfer | 진동형 히트파이프는 1990년대 초 처음 소개된 뒤 구조가 단순하고 따로 전력을 쓰지 않고도 높은 열유속에 쓸 수 있다는 장점으로 주목받았지만, 지난 30년 동안 많은 연구에도 기본 특성에 관한 논쟁과 실제 응용의 기술 문제가 남아 있다. 이 리뷰는 최근 연구를 비판적으로 검토해 결과를 기본 특성과 실용 측면 두 가지로 나눠 정리했다. 기본 특성 쪽은 현재까지 알려진 진동형 히트파이프의 특성을 검토하고, 실용 쪽은 응용을 위해 풀린 기술 문제를 요약했다.[^p3] | 1저자 W. Kim, 마지막 저자 김성진 |
| 4 | 2021 | [Topology optimization of a heat sink with an axially uniform cross-section cooled by forced convection](https://doi.org/10.1016/j.ijheatmasstransfer.2020.120732) · International Journal of Heat and Mass Transfer | 펌프 동력을 고정한 조건에서, 흐름 방향으로 단면이 같은 강제대류 히트싱크의 열 성능을 가장 크게 하는 위상 최적화 방법을 제안했다. 목적 함수로 대류 저항과 열용량 저항을 합한 총 열저항을 쓰고, 대류 저항과 열 컴플라이언스의 관계를 유도해 총 열저항을 다르게 표현함으로써 민감도 해석에 드는 계산 시간을 줄였다. 이 방법으로 얻은 형상을 해석적으로 최적화한 판형 핀 히트싱크와 비교해 검증한 뒤, 실제 영역에서 히트싱크를 최적화하고 제작하기 쉽게 단순화했다. 이 히트싱크는 상용 히트싱크보다 총 열저항이 31% 낮고 무게가 9% 가벼웠다. 열용량 저항을 빼고 설계하면 열 성능이 나쁜 히트싱크가 나올 수 있어 두 저항의 합을 줄이는 것이 중요함도 확인했다.[^p4] | 1저자 G. Lee, 마지막 저자 김성진 |
| 5 | 2021 | [On the Objective Function for Topology Optimization of Heat Sinks](https://doi.org/10.1109/tcpmt.2021.3120383) · IEEE Transactions on Components, Packaging and Manufacturing Technology | 위상 최적화는 목적 함수의 기울기로 형상을 거듭 고쳐 가며 최적 배치를 얻으므로, 알맞은 목적 함수를 고르는 것이 중요하다. 이 논문은 열전도 문제부터 최근의 전산유체역학 기반 열전달 문제까지 히트싱크 위상 최적화 연구에서 쓰인 목적 함수의 수학적 정의와 물리적 뜻을 검토했다. 대부분의 연구는 히트싱크의 열저항이나 열원의 최고 온도를 줄이도록 목적 함수를 정하고, 열저항 대신 열 컴플라이언스를 흔히 쓴다. 그런데 열 컴플라이언스는 열원의 평균 온도에 비례해 최고 온도와 다를 수 있어, 이를 줄이면 최소 열저항 설계와 꽤 다른 형상이 나올 수 있다고 짚었다. 열전도 문제에서는 고체의 열전도도가 낮을수록, 대류 문제에서는 유체의 열용량 유량이 작아 흐름 방향의 유체 온도 변화가 클수록 그 차이가 커진다.[^p5] | 1저자 G. Lee, 마지막 저자 김성진 |
| 6 | 2021 | [Thermal optimization of the pin-fin heat sink with variable fin density cooled by natural convection](https://doi.org/10.1016/j.applthermaleng.2021.116692) · Applied Thermal Engineering | 자연대류로 식히는 핀 히트싱크에서 핀 밀도를 흐름 방향으로 바꿀 때의 열 성능을 수치 해석으로 살폈다. 핀 히트싱크를 유체가 차 있는 다공성 매질로 보는 간략 모델로 핀 밀도의 분포를 최적화했고, 핀과 공기 사이의 대류 열전달을 다공성 매질을 지나는 유체가 옮기는 열에 견주어 새 유효 열전도도 모델을 제안해 문헌의 실험 자료와 직접 수치 해석 결과로 검증했다. 바닥판과 핀 높이를 고정하고 크리깅 방법으로 열저항이 가장 작은 핀 밀도 분포를 찾았더니, 공극률이 흐름 방향으로 0.898에서 0.946까지 꾸준히 커지는 분포, 곧 아래쪽은 핀이 촘촘하고 위쪽은 성긴 배치가 나왔다. 이렇게 최적화한 히트싱크는 기존 상관식으로 최적화한 고른 밀도의 핀 히트싱크보다 열저항이 11% 낮고 무게가 30% 가벼웠다.[^p6] | 1저자 Y. J. Lee, 마지막 저자 김성진 |

## 교수와 전문 분야

김성진 교수는 서울대학교에서 학사(1982)와 석사(1984)를, 미국 Ohio State University에서 박사(1989)를 받았다.[^members][^meprof] 1990–1997년 미국 IBM에서 Development Staff Member(1990–1992), Advisory Engineer(1992–1996), Senior Engineer(1996–1997)로 일했고, 1997–2003년 KAIST 부교수(Associate Professor), 2003년부터 교수(Professor)로 적혀 있다. 2021년부터는 KEPCO Endowed Chair Professor다.[^members] 교수 소개는 이 밖의 경력으로 International Journal of Transport Phenomena의 Associate Editor(2002–), ASME Fellow(2005–), Journal of Mechanical Science and Technology의 Editor(2006–2008), ASME Journal of Heat Transfer의 Associate Editor(2007–2009), KSME Thermal Engineering Division의 Chair(2011), Transactions of KSME의 Editor-in-Chief(2012–2015), Center for Flexible and Thin Superconductors의 Director(2012–2021), Korean Academy of Science and Technology(KAST)의 Member(2014–), Asian Union of Thermal Science and Engineering(AUTSE)의 President(2017–2021)를 적는다.[^members]

수상으로는 Market Driven Quality Team Award(IBM, 1993), Author Recognition Awards(IBM, 1991, 1992, 1994, 1997), Prize for Excellence in Teaching(KAIST, 2001), Research Excellence Award(KSME, 2006), Grand Prize for Excellence in Teaching(KAIST, 2012), Minister's Award(Ministry of Trade, Industry and Energy, 2015), Order of Science and Technology Merit Innovation Medal(The Government of the Republic of Korea, 2018), LINKGENESIS Best Teacher Award Grand Prize(KAIST, 2020), Grand Prize for Academic Excellence(KAIST, 2022)를 적는다.[^members] 연구실 소식란은 2022년 3월 「김성진 교수님, KAIST 학술대상 수상」과 2022년 10월 「김성진 교수님, 2022 일본기계학회 Thermal Engineering Award 수상」을 알렸다.[^news] 교수 상세 페이지는 1995–2018년 논문 목록과 특허 18건(1993년 12월–2012년 11월)을 적는다.[^profdet]

연구실 소식란은 2025년 4월 3일 글에서 지난 28년간 교육과 연구에 헌신한 김성진 교수의 은퇴식을 마쳤다고 알리고, 교수가 명예교수로서 앞으로도 연구실과 학문 공동체에 조언을 나눌 예정이라고 적는다.[^retire] 2026년 10월 23일 기계공학과 교수진 페이지는 교수를 「교수」 탭에 올리고 연구분야, 연구실, 최종학위를 적으며,[^meteam][^meprof] 같은 페이지의 「명예교수」 탭 명단에는 교수 이름이 없다.[^meemer]

교수의 연구 관심은 전자 패키지 냉각, 마이크로 스케일 열전달과 유동, 열교환기·히트파이프·히트싱크의 최적 설계, 다공성 매질의 대류 열전달이다.[^members] 2021–2026년 논문으로 보면 지금의 전문 분야는 세 갈래다. 첫째, 반도체와 전자 소자를 식히는 매니폴드 마이크로채널과 진동형 히트파이프 같은 냉각 장치의 실험과 모델링이다(대표 논문 1–3).[^p1][^p2][^p3][^pubs] 둘째, 위상 최적화와 간략 모델로 히트싱크의 형상을 최적 설계하는 일이다(대표 논문 4–6).[^p4][^p5][^p6] 셋째, 끓음 현상의 임계 열유속을 실험과 모델로 밝히는 일이다.[^about][^pubs]

## 응용 분야

연구 소개 페이지는 매니폴드 마이크로채널 연구의 배경으로 인공지능 가속기와 고성능 반도체의 발열을 들고,[^about] 휘는 진동형 히트파이프가 휘는 디스플레이용 냉각 장치, 태양전지, 인공위성에 쓰일 수 있다고 적는다.[^about] 연구실 Projects 페이지는 2021년 10월 이후에 걸친 과제로 삼성전자의 차세대·고집적 반도체 열 특성 개선용 박막형 Heat Spreading Die 요소기술 개발(2023–2026), 국방기술진흥연구소의 우주비행체용 차세대 능동 냉각 구조 기술 개발과 초고열유속 냉각시스템 특화연구실(2022–2028), 한국연구재단의 PIM-HBM 3D 구조의 아키텍처 설계와 전기적·열적·재료적 성능 분석(2022–2025), 초고열유속 발열체를 위한 3D Multiporous 냉각장치 개발(2021–2025), 차세대지능형반도체 기술개발사업(2020–2023), KAIST의 차세대 초열전도체 연구실(2022–2027), 엘오티머트리얼즈의 진동형 히트파이프 최적 설계·제작 기술 개발(2021)을 적는다.[^projects] 연구실 소식란은 2021년 11월 KAIST 초세대 협업연구실 선정, 2022년 1월 그 현판식, 2022년 11월 초고열유속 냉각시스템 특화연구실 착수회의를 알렸고, 대한기계학회 학술대회, IHTC, InterPACK, ACTS, PRTEC 같은 학회 이름을 제목으로 한 글과 KAIST 산학협동공개강좌 「전자패키지 및 시스템의 열설계」 안내를 올렸다.[^news] 졸업생 진로로는 한국항공우주연구원(KARI), 한국기계연구원(KIMM), 한국에너지기술연구원(KIER), 국방과학연구소(ADD), 삼성전자, 현대자동차와 여러 대학이 적혀 있다.[^alumni]

## 구성원

2026년 10월 23일 연구실 누리집 Members 메뉴 기준이다. Ph.D. 페이지의 박사과정(Ph.D. Candidate) 1명과 M.S. 페이지의 석사과정(M.S. Candidate) 1명이며, Post Doctor 페이지에는 사람이 없다. 연구 주제는 각 카드의 interests 칸이고 이메일은 카드의 학교 주소다.[^phd][^ms] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Yang, Jae Wan | 박사과정 | Manifold microchannels, Microfluidic cooling, Two-phase cooling | baggn123@kaist.ac.kr |  |
| Yu, Kyeong Hwan | 석사과정 | Pulsating Heat Pipe | ghksruddb_12@kaist.ac.kr |  |

## 졸업생

연구실 누리집 Alumni 페이지의 56명 전부다(2001년 8월–2025년 2월 졸업). 학위는 페이지의 Degree 칸 표기(M.S., Ph.D., M.S., Ph.D., Combined M.S./Ph.D)이고, 연도는 Graduation 칸의 졸업 연월이며, 진로는 Office 칸이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jeung Sang Ko | Ph.D. (2001.08) | Pusan National Univ. |
| Ho Chul Rhyoo | M.S. (2002.02) | KCL |
| Kyu In Shim | M.S. (2002.02) | Doosan Infracore |
| Duckjong Kim | M.S., Ph.D (2003.02) | Gyeongsang Univ. |
| Seok Pil Jang | M.S., Ph.D. (2003.08) | Korea Aerospace Univ. |
| Jin Wook Kim | M.S. (2004.02) | Hanwha NxMD |
| Jae Wook Yoo | Ph.D. (2004.08) | SAMSUNG Electronics |
| Joung Ki Seo | M.S., Ph.D. (2005.02) | SaTReC |
| Jung Yim Min | M.S., Ph.D. (2005.02) | Chungbuk Univ. |
| Il Hyun Jo | M.S (2005.02) | SAMSUNG Electronics |
| Hwan Hee Oh | M.S. (2005.02) | 변호사 오환희 법률사무소 |
| Il Young Han | M.S., Ph.D. (2005.08) | SAMSUNG Electronics |
| Jin Kwon Bae | M.S. (2007.02) | HYUNDAI Mobis |
| Kyu Hyung Do | M.S., Ph.D. (2007.08) | KIMM |
| Dong Kwon Kim | M.S., Ph.D. (2007.08) | Ajou Univ. |
| Tae Hoon Kim | M.S., Ph.D. (2009.02) | KIMM |
| Yong Seok Choi | M.S., Ph.D. (2010.02) | LG Chemical |
| Tae Young Kim | M.S., Ph.D. (2010.02) | Seoultech |
| Heeseung Park | M.S. (2010.02) | ADD |
| Young Jin Baik | Ph.D. (2011.02) | KIER |
| Kyo Sung Choo | M.S., Ph.D. (2011.02) | Youngstown State Univ. |
| Tae Yeob Kang | M.S. (2011.02) | Suwon Univ. |
| Chan Byon | M.S., Ph.D. (2012.02) | UNIST |
| Sunghoon Choi | M.S. (2012.02) | HYUNDAI Motors |
| Young jik Youn | M.S., Ph.D. (2012.08) | Hanbat National Univ. |
| Daniel Gordon Trainer | Ph.D. (2013.08) | koreatech |
| Ju Wan Kim | M.S., Ph.D. (2013.08) | KARI |
| Jaehoon Jung | Combined M.S./Ph.D (2014.02) | KAERI |
| Sungwan Park | M.S. (2014.02) | 국립과학수사연구원 |
| Gihwan Kwon | Combined M.S./Ph.D (2014.08) | ADD |
| Hyeseung Lee | M.S. (2016.08) | HYUNDAI Motors |
| Hyeokmin Kwon | M.S. (2017.02) | ADD |
| Younghwan Joo | M.S., Ph.D (2017.08) | KIER |
| Kilyoung Lee | M.S. (2017.08) | SAMSUNG Display |
| Jung Seok Lee | M.S., Ph.D. (2018.02) | KARI |
| Sung Il Kim | Ph.D. (2018.02) | KIER |
| Sang Ho Choi | Ph.D. (2018.02) | KARI |
| Seongbeom Heo | M.S. (2018.08) | PAL |
| Aejung Yoon | M.S., Ph.D. (2018.08) | UNIST |
| Changhwan Kim | M.S. (2019.02) | LG Electronics |
| Jaeyeong Jo | M.S., Ph.D. (2019.02) | SAMSUNG Electronics |
| Dahm Yu | M.S., Ph.D. (2019.02) | SAMSUNG Electronics |
| Soohwan Jun | M.S., Ph.D. (2019.02) | KARI |
| Hyeseong Choi | M.S. (2020.02) | KSOE |
| Hyung Yun Noh | M.S., Ph.D. (2020.02) | KARI |
| Juno Kim | M.S., Ph.D. (2020.02) | SAMSUNG Electronics |
| Gillho Lee | M.S., Ph.D. (2021.02) | KARI |
| Jonghyun Lim | M.S., Ph.D. (2021.02) | SAMSUNG Electronics |
| Wookyung Kim | M.S., Ph.D. (2021.02) | KIMM |
| Minchang Kim | M.S., Ph.D. (2022.02) | KIMM |
| Jeongwon Cho | M.S. (2023.02) | HYUNDAI Motors |
| Chuljae Jung | M.S., Ph.D. (2023.02) | KIER |
| Hyunhee Kim | M.S. (2024.02) | SAMSUNG Electronics |
| Hansol Lee | M.S. (2024.02) | Georgia Institute of Technology |
| Young Jin Lee | M.S., Ph.D. (2025.02) | Georgia Institute of Technology |
| Young Jong Lee | M.S., Ph.D. (2025.02) | EPFL |

## 최근 논문 목록 (2021–2026)

연구실 누리집 Publication 페이지 International Journal 칸의 2021–2026년 연도 구역 23편이다(2026년 3, 2025년 5, 2024년 4, 2023년 2, 2022년 1, 2021년 8). 저자 순서와 제목·학술지 표기는 누리집 그대로다. 교수가 마지막 저자가 아닌 공동연구 논문도 누리집 목록대로 실었다.[^pubs]

**2026**

- T.W. Lee, S.J. Kim, M. Hnizdl, M. Chabicovsky and M. Raudensky. "Thermodynamic prediction of the Leidenfrost temperature during spray cooling of hot surfaces". *International Journal of Heat and Mass Transfer 271 (2026) 129410*.
- H.J. Eom, J. Bae, T. Dixit, B. Baudouy, S.J. Kim and A. Yoon. "Characteristics of neon pulsating heat pipes in vertical orientation". *International Journal of Thermal Sciences (2026) 110950*.
- Y.J. Lee, C. Hwang, H. Lee, I. Lee and S.J. Kim. "Highly energy-efficient manifold microchannel for cooling electronics with a coefficient of performance over 100,000". *Energy Conversion and Management (2026) 121422*.

**2025**

- Y.J. Lee, S.J. Kim. "Experimental investigation on the effect of microgrooves with reentrant cavities on the thermal performance of a pulsating heat pipe". *International Communications in Heat and Mass Transfer (2025) 109797*.
- J. Cho, C. Jung, and S.J. Kim. "A channel layout for an orientation-independent performance of a pulsating heat pipe under excessively localized heating conditions". *Applied Thermal Engineering (2025) 128136*.
- J. Shin, J. Bae, S.J. Kim, and T.Y. Kim. "Flow regimes and flow instability of transpiration cooling". *International Journal of Heat and Mass Transfer 252 (2025) 127457*.
- J.-H. Jeong, J. Heo, S. Lee, S.J. Kim, and J.-H. Han. "Numerical prediction of permeability and effective thermal conductivity in simple cubic and body-centered truss structures". *ASME Journal of Fluids Engineering (2025) 091502*.
- A. Yoon, H.Y. Noh, S.J. Lee, and S.J. Kim. "Study on the effect of condenser configuration of pulsating heat pipes for space applications". *International Journal of Thermal Sciences (2025) 109418*.

**2024**

- J. Kim, Y.J. Lee, J.-Y. Kim, J. Yoon, H. Yoon, J.-B. You, S.J. Kim, H. Kurt, and H.-H. Park. "High-efficiency thermo-optic control of longitudinal radiation angle in silicon-based optical phased array by leveraging backside air trench structure". *Optics Letters (2024) 524469*.
- H. Lee, Y.J. Lee, and S.J. Kim. "One-dimensional model of manifold microchannels for embedded cooling: Prediction of thermal performance and flow non-uniformity". *International Communications in Heat and Mass Transfer (2024) 107498*.
- Y.J. Lee, S.J. Kim. "Experimental investigation on thermal-hydraulic performance of manifold microchannel with pin-fins for ultra-high heat flux cooling". *International Journal of Heat and Mass Transfer (2024) 125336*.
- Y.J. Lee, S.J. Kim. "Experimental investigation on the effect of transverse grooves in a channel on the thermal performance of a flat-plate pulsating heat pipe". *International Journal of Heat and Mass Transfer (2024) 124759*.

**2023**

- M. Kim, S.J. Kim. "A mechanistic model of critical heat flux for pool boiling based on supply failure mechanisms depending on the contact angle". *International Journal of Heat and Mass Transfer (2023) 124090*.
- C. Jung, S.J. Kim. "Investigation into the effects of passive check valves on the thermal performance of pulsating heat pipes". *International Journal of Heat and Mass Transfer 204 (2023) 123850*.

**2022**

- Y.J. Lee, S.J. Kim. "Effects of the micro-post array on the maximum allowable input power for a micro pulsating heat pipe". *International Journal of Heat and Mass Transfer 193 (2022) 122898*.

**2021**

- G. Lee, Y. Joo, and S.J. Kim. "On the Objective Function for Topology Optimization of Heat Sinks". *IEEE Transactions on Components, Packaging and Manufacturing Technology 11 (2021) 1776-1782*.
- W. Kim, S.J. Kim. "Fundamental issues and technical problems about pulsating heat pipes". *Journal of Heat Transfer-Transactions of the ASME 143 (2021) 4051465*.
- A. Yoon, S.J. Kim. "A deep-learning approach for predicting oscillating motion of liquid slugs in a closed-loop pulsating heat pipe". *International Journal of Heat and Mass Transfer 181 (2021) 121860*.
- H.Y. Noh, A. Yoon, and S.J. Kim. "Investigation into the effect of transverse conduction on the thermal performance of a flat-plate pulsating heat pipe". *International Journal of Heat and Mass Transfer 181 (2021) 121842*.
- J. Lim, S.J. Kim. "A channel layout of a micro pulsating heat pipe for an excessively localized heating condition". *Applied Thermal Engineering 196 (2021) 117266*.
- Y.J. Lee, S.J. Kim. "Thermal optimization of the pin-fin heat sink with variable fin density cooled by natural convection". *Applied Thermal Engineering 190 (2021) 116692*.
- G. Lee, I. Lee, and S.J. Kim. "Topology optimization of a heat sink with an axially uniform cross-section cooled by forced convection". *International Journal of Heat and Mass Transfer 168 (2021) 120732*.
- C. Jung, S.J. Kim. "Effects of oscillation amplitudes on heat transfer mechanisms of pulsating heat pipes". *International Journal of Heat and Mass Transfer 165 (2021) 120642*.

## 연구 과제

연구실 누리집 Projects 페이지의 과제 가운데 수행 기간이 2021년 10월 13일 이후에 걸친 8건이다. 과제명, 기간, 위탁 기관, 상태(완료·진행중)는 페이지 표기 그대로다.[^projects]

- 차세대/고집적 반도체 열특성 개선을 위한 박막형 Heat Spreading Die 요소기술 개발 (기간 2023.03.01 – 2026.02.28; 지원 (주)삼성전자; 상태 완료)
- 우주비행체용 차세대 능동 냉각 구조 기술 개발 (기간 2022.11.01 – 2028.10.31; 지원 국방기술진흥연구소; 상태 진행중)
- 초고열유속 냉각시스템 특화연구실 (기간 2022.11.01 – 2028.10.31; 지원 국방기술진흥연구소; 상태 진행중)
- PIM-HBM 3D 구조의 아키텍처 설계 및 전기적/열적/재료적 성능 분석 (기간 2022.04.20 – 2025.12.31; 지원 한국연구재단; 상태 완료)
- 차세대 초열전도체 연구실 (기간 2022.01.01 – 2027.06.30; 지원 KAIST; 상태 진행중)
- 초고열유속 발열체를 위한 3D Multiporous 냉각장치 개발 (기간 2021.03.02 – 2025.08.31; 지원 한국연구재단; 상태 완료)
- 차세대지능형반도체 기술개발사업 (기간 2020.07.01 – 2023.03.31; 지원 한국연구재단; 상태 완료)
- 진동형 히트파이프 최적 설계 기술 및 제작 기술 개발 (기간 2021.04.12 – 2021.12.31; 지원 (주)엘오티머트리얼즈; 상태 완료)

## 소식

연구실 누리집 Notice 게시판의 2021년 11월 8일–2026년 9월 16일 글 가운데 연구·수상·진로·과제·학회·강좌 소식 52건이다. 제목은 게시판 표기 그대로이고, 수상·진로 소식에는 졸업생의 소식이 많다.[^news]

- 2026-09-16 · 정철재 선배님, 한국에너지기술연구원 BEST 신입직원상 수상
- 2026-05-17 · 백영진 선배님, 한국연구재단 한계도전전략센터 책임PM 부임
- 2026-04-27 · 2026년 대한기계학회 춘계학술대회 (제주도)
- 2025-10-27 · 2025년 J-K TFEC
- 2025-10-18 · 추교성 선배님, Distinguished Professorship Award 수상
- 2025-06-20 · 김민창 선배님, 한국기계연구원 신인상 수상
- 2025-06-16 · [강좌취소안내]KAIST산학협동공개강좌_전자패키지 및 시스템의 열설계
- 2025-05-11 · 제 24차 전자패키지 및 시스템의 열설계
- 2025-04-28 · 2025년 대한기계학회 춘계학술대회 (제주도)
- 2025-04-03 · 김성진 교수님 은퇴식
- 2025-02-28 · 이영진 선배님, Georgia Institute of Technology의 박사후연구원으로 임용
- 2025-02-12 · 이영종 선배님, 카이스트 공과대학 박사학위 우수논문상 수상
- 2025-01-21 · 2025년 응용열전달 연구실 신입생 입학
- 2024-12-26 · 2024년 PRTEC
- 2024-12-07 · 이한솔 선배님, 2024 기계공학과우수상 수상
- 2024-11-21 · 이영종 박사과정, 최종발표
- 2024-11-21 · 이영진 박사과정, 최종발표
- 2024-09-29 · 김덕종 선배님, 경상국립대학교 정교수로 승진
- 2024-07-02 · 2024년 ACTS
- 2024-06-21 · 제 23차 전자패키지 및 시스템의 열설계 추가 자료
- 2024-04-26 · 2024년 대한기계학회 춘계학술대회 (제주도)
- 2024-04-05 · 제 23차 전자패키지 및 시스템의 열설계
- 2024-02-22 · 윤영직 선배님, 한밭대학교 부임
- 2024-01-08 · 2024년 응용열전달 연구실 신입생 입학
- 2024-01-04 · 정철재 선배님, 한국에너지기술연구원 합격
- 2024-01-04 · 김현희 선배님, 삼성전자 합격
- 2023-12-07 · 정철재 선배님, 한국기계연구원장상 수상
- 2023-11-07 · 김덕종 선배님, 경상대학교 총장특별상 수상
- 2023-11-06 · 2023 대한기계학회 추계학술대회
- 2023-10-30 · 2023 InterPACK
- 2023-08-18 · 이영종 선배님, 2023 IHTC Best Paper Award 수상
- 2023-08-18 · 2023 IHTC
- 2023-06-28 · 제 22차 전자패키지 및 시스템의 열설계 예제 솔루션
- 2023-06-19 · 2023 한국군사과학기술학회
- 2023-05-12 · 이혜승 선배님, 책임연구원으로 승진
- 2023-05-10 · 제 22차 전자패키지 및 시스템의 열설계
- 2023-05-02 · 강태엽 선배님, 수원대학교 부임
- 2023-04-24 · 2023년 대한기계학회 춘계학술대회 (부산)
- 2023-01-17 · 조정원 선배님, 현대자동차 합격
- 2022-11-22 · 초고열유속 냉각시스템 특화연구실 착수회의 행사 진행
- 2022-11-21 · 정철재 박사과정, 최종발표
- 2022-10-28 · 김성진 교수님, 2022 일본기계학회 Thermal Engineering Award 수상
- 2022-09-19 · 김민창 선배님, 한국기계연구원 합격
- 2022-04-08 · 도규형 선배님, 연구실장으로 승진
- 2022-03-02 · 김성진 교수님, KAIST 학술대상 수상
- 2022-02-28 · 2022년 응용열전달 연구실 신입생 입학
- 2022-02-10 · 정철재 박사과정, 우덕윤덕병재단 장학생 최종선발
- 2022-02-10 · 김민창 박사과정, 최종발표
- 2022-01-25 · KAIST 초세대 협업연구실 현판식 진행
- 2021-11-26 · 이길호 선배님, 한국항공우주연구원 이직
- 2021-11-22 · KAIST 초세대 협업연구실 선정
- 2021-11-08 · 윤애정 선배님, UNIST 부임

## 연락과 위치

- 연구실: Room# 3104, Department of Mechanical Engineering, KAIST(누리집 아래쪽 표기), 전화 042-350-3083, 팩스 042-350-3210[^home]
- 교수 사무실: 기계동(N7) 5109[^meprof]
- 교수 전화와 이메일: 042-350-3043, sungjinkim@kaist.ac.kr[^members][^meprof]
[^p1]: C. Jung, S. J. Kim, International Journal of Heat and Mass Transfer 165, 120642 (2021). <https://doi.org/10.1016/j.ijheatmasstransfer.2020.120642> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: H. Y. Noh, A. Yoon, S. J. Kim, International Journal of Heat and Mass Transfer 181, 121842 (2021). <https://doi.org/10.1016/j.ijheatmasstransfer.2021.121842> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: W. Kim, S. J. Kim, Journal of Heat Transfer 143, 100803 (온라인 2021-09-08). <https://doi.org/10.1115/1.4051465> 초록 기준.
[^p4]: G. Lee, I. Lee, S. J. Kim, International Journal of Heat and Mass Transfer 168, 120732 (2021). <https://doi.org/10.1016/j.ijheatmasstransfer.2020.120732> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: G. Lee, Y. Joo, S. J. Kim, IEEE Transactions on Components, Packaging and Manufacturing Technology 11, 1776-1782 (2021). <https://doi.org/10.1109/tcpmt.2021.3120383> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: Y. J. Lee, S. J. Kim, Applied Thermal Engineering 190, 116692 (2021). <https://doi.org/10.1016/j.applthermaleng.2021.116692> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 연구실 누리집 첫 화면 <http://appheat.kaist.ac.kr/> (연구 그림 제목, Notice, 아래쪽 연구실 이름·주소·전화, 2026-10-23 열람)
[^about]: About Us(Introduction) 페이지 <http://appheat.kaist.ac.kr/aboutus/aboutus.php> (Manifold microchannel, Pulsating Heat Pipes, Critical Heat Flux Mechanism in Pool Boiling, Topology Optimized Heat Sink, 2026-10-23 열람)
[^members]: Members 페이지 Professor 칸 <http://appheat.kaist.ac.kr/members/members.php> (학력, Career, Research interests, Awards, 연락처, 2026-10-23 열람)
[^profdet]: 교수 상세 페이지 <http://appheat.kaist.ac.kr/members/professor_details.php> (Papers, Patents, 2026-10-23 열람)
[^phd]: Members 메뉴 Ph.D. 페이지 <http://appheat.kaist.ac.kr/members/phd.php> (2026-10-23 열람)
[^ms]: Members 메뉴 M.S. 페이지 <http://appheat.kaist.ac.kr/members/ms.php> (2026-10-23 열람)
[^alumni]: Members 메뉴 Alumni 페이지 <http://appheat.kaist.ac.kr/members/alumi.php> (2026-10-23 열람)
[^pubs]: Publication 페이지 <http://appheat.kaist.ac.kr/publication/publication.php> (International Journal 칸, 2026-10-23 열람)
[^projects]: Research 메뉴 Projects 페이지 <http://appheat.kaist.ac.kr/research/research.php> (2026-10-23 열람)
[^news]: Notice 게시판 <http://appheat.kaist.ac.kr/bbs/zboard.php?id=bbs> (1–6쪽, 2026-10-23 열람)
[^retire]: Notice 게시판 글 「김성진 교수님 은퇴식」 <http://appheat.kaist.ac.kr/bbs/view.php?id=bbs&no=285> (2025-04-03 게시, 2026-10-23 열람)
[^meteam]: KAIST 기계공학과 교수진(교수 탭) <https://me.kaist.ac.kr/team/team_010100.html> (2026-10-23 열람)
[^meemer]: KAIST 기계공학과 교수진(명예교수 탭) <https://me.kaist.ac.kr/team/team_010100.html?mode=2> (2026-10-23 열람)
[^meprof]: KAIST 기계공학과 교수 상세(김성진) <https://me.kaist.ac.kr/pop/team.html?uid=12&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 이메일, 사무실, 전화, 2026-10-23 열람)
[^meres]: KAIST 기계공학과 연구분야(에너지/환경/해양) <https://me.kaist.ac.kr/research/research_010300.html> (핵심교수 김성진 항목, 2026-10-23 열람)

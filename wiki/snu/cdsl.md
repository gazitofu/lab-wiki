# 제어 및 동역학 연구실 (Control and Dynamic Systems Lab, CDSL)

**서울대학교 공과대학 전기·정보공학부 · 심형보 교수, 이진규 교수**

- 분야: 제어 이론(비선형 시스템의 안정성 해석, 상태 관측기 설계), 외란 관측기로 하는 강인 제어, 다개체 시스템(혼합 동역학 정리, 분산 관측·최적화·계산 알고리즘), 제어 시스템 보안과 동형암호로 하는 제어기 암호화, 데이터 기반 제어, 뉴로모픽 제어, 하이브리드·스위칭 시스템
- 대분야: 전기전자·반도체·광학, 수학·통계
- 태그: 제어 이론·제어 공학[^about][^overview][^p1], 네트워크 보안·프라이버시[^enc][^p5][^p6], 스마트 그리드·전력 관리[^hicl][^hiclws], 다중 에이전트 시스템·분산 의사결정[^p3], 상태 추정·필터링(데이터 동화)[^cps], 암호학[^p5][^p6], 수리 최적화·최적화 알고리즘[^hiclws]
- 홈페이지: <https://post.cdsl.kr/> (심형보 교수 개인 누리집 <https://hyungbo.github.io/>, 이진규 교수 개인 누리집 <https://jingyulee92.wordpress.com/>)
- 근거와 출처: [Control and Dynamic Systems Lab 근거 페이지](cdsl-sources.md)

> 심형보 교수와 이진규 교수가 함께 이끄는 수학적 제어 이론 연구실이다. 외란 관측기로 하는 강인 제어, 여러 개체가 통신망으로 묶인 다개체 시스템의 혼합 동역학과 분산 알고리즘, 제어 시스템 보안과 동형암호로 하는 제어기 암호화, 데이터 기반 제어와 뉴로모픽 제어를 연구한다.[^people][^overview][^shimhome][^leeri][^p1][^p3][^p5][^p8]

## 무엇을 연구하나

연구실 누리집의 People 페이지는 서울대학교 전기·정보공학부 심형보 교수와 이진규 교수를 지도교수(Supervisor)로 함께 올린다.[^people] 학부 연구실 목록은 두 교수를 각각 「제어 및 동역학 연구실」로 적어 제어공학 연구그룹과 지능 및 로봇 공학 연구그룹에 올리고, 두 교수의 연구실 상세는 모두 이 누리집을 연결한다.[^ecelab][^ecelab62][^ecelab146] About 페이지에 따르면 연구실은 1989년 서진헌 교수가 「Automatic Control Lab」이라는 이름으로 세웠고, 1995년 「Optimal Robust Control Lab」으로, 2006년 지금 이름인 「Control and Dynamic Systems Lab」으로 바뀌었다. 심형보 교수는 2003년 연구실에 합류했고, 연구실은 100명이 넘는 박사와 석사를 배출했다고 적는다.[^about] 이진규 교수는 이 연구실에서 심형보 교수와 서진헌 교수의 지도로 2019년 박사 학위를 받았고, 2024년 9월 1일 서울대학교 전기정보공학부 조교수로 임용되었다.[^lee24] About 페이지는 연구 관심을 제어 이론(control theory)으로 적고, 연구를 잘 나타내는 두 낱말로 「제어(control)」와 「동역학(dynamics)」을 든다.[^about]

Research Overview 페이지는 연구실이 수학적 제어 이론을 연구한다고 적는다. 그 목표는 제어하기 어렵다고 알려진 시스템을 위한 새 방법론을 만들고, 수학적 근거 없이 참이라고 여겨져 온 것을 형식적이고 엄밀한 이론으로 뒷받침하는 것이다. 제어 이론의 역사는 길지만 비선형 시스템(입력과 출력의 관계가 중첩의 원리를 따르지 않는 시스템)을 분석하고 제어기를 합성하는 도구가 나온 지는 비교적 오래되지 않아 비선형 제어 이론은 지금도 활발히 연구되고, 이 도구들 덕분에 군사, 항공우주, 고정밀 기계, 생물학에서 흔히 나타나는 비선형성이 강한 시스템에 대해 높은 성능 기준을 맞추는 새 비선형 제어기를 설계할 수 있게 되었다고 적는다. 다루는 주제로는 외란 관측기, 다개체 시스템, 사이버 물리 시스템의 보안, 동형암호 기반 제어기, 영점 배치 문제를 위한 병렬 피드포워드 보상기, 하이브리드·스위칭 시스템, 비선형 관측기와 출력 궤환 문제를 든다.[^overview] 학부 연구실 상세(심형보 교수)는 연구실이 미분 또는 차분 방정식으로 표현되는 여러 동적 시스템(상태가 시간에 따라 정해진 규칙으로 변하는 시스템)의 해석과 제어 기법을 연구하며, 이런 시스템을 다루는 일반 이론을 연구·개발하는 한편 개별 시스템에 특화된 제어 기법을 고안하는 것을 목표로 한다고 적는다. 연구 분야로는 비선형 시스템의 안정성 해석과 제어 합성, 다개체 시스템, 외란 관측기, 출력 조절(output regulation), 하이브리드 시스템과 스위칭 시스템을 든다.[^ecelab62]

두 교수의 개인 누리집도 연구 관심을 적는다. 심형보 교수는 네트워크로 연결된 동적 시스템과 분산 최적화, 다개체 시스템의 창발 거동(개체들의 상호작용에서 전체 수준으로 나타나는 거동)과 그 제어 설계 응용, 외란 관측기 기반 강인 제어, 제어 시스템 보안, 제어 시스템의 암호학 응용, 비선형 관측기와 비선형 시스템의 안정성 해석, 데이터 기반 제어를 든다.[^shimhome] 이진규 교수는 네트워크 제어 시스템의 집단 거동과 분산 알고리즘 설계, 적응 제어와 관측기, 사이버 물리 시스템의 분산 고장 검출과 상태 추정, 리듬 있는 신호를 스스로 만들어 내는 신경 회로인 CPG(central pattern generator)와 뉴로모픽 공학, 모멘트 정합(전달 함수를 급수로 전개한 계수인 모멘트를 원래 시스템과 맞추는 방법)으로 하는 모델 축소와 시스템 식별을 든다.[^leeri] 학부 교수 상세는 이진규 교수의 Research Interest를 Multi-Agent Systems, Nonlinear System Theory, Observer, Secure Control Systems, Adaptive Control, Neuronal Networks & Neuromorphic Engineering으로 적는다.[^ecelee] 아래 네 갈래 가운데 첫째와 셋째는 주로 심형보 교수의 논문에서 나오고, 둘째와 넷째에는 두 교수의 논문이 함께 있다.

첫째 갈래는 **외란 관측기로 하는 강인 제어**다. 외란 관측기(disturbance observer, DOB)는 시스템에 들어오는 외란과 모형 오차의 영향을 측정한 입출력으로 추정해 제어 입력에서 상쇄하는 제어 기법이고, 강인 제어는 모형이 불확실하거나 외란이 있어도 안정성과 성능을 지키도록 하는 제어다. 국문 외란 관측기 연구 소개는 외란 관측기를 모델 불확실성과 외란이 시스템에 미치는 영향을 관측하거나 추정해 보상하는 강인 제어 기법으로 설명한다.[^dobkr] 영문 외란 관측기 연구 페이지는 연구실의 성과를 Springer의 Encyclopedia of Systems and Control 항목 「Disturbance Observers」(2020)와 튜토리얼 논문(Control Theory and Technology, 2016)에 정리했다고 적고, 연구 흐름을 열여섯 항목으로 소개한다. 첫 결과는 특이 섭동 이론(빠르게 변하는 부분과 느리게 변하는 부분이 섞인 시스템을 시간 척도를 나누어 분석하는 이론)으로 선형 플랜트(제어 대상 시스템)에서 외란 관측기의 안정성과 성능 한계를 상태 공간에서 분석하고 영동역학(출력이 늘 0이 되도록 입력을 정했을 때 남는 시스템 내부의 동역학)의 역할을 밝힌 것이다. 이어 임의로 크지만 유계인(값이 유한한 범위 안에 머무는) 매개변수 불확실성에 대해서도 폐루프 강인 안정성을 늘 보장하는 필터 설계 절차, 과도 응답까지 강인하게 만드는 수정 구조와 그 비선형·다입력 다출력 시스템 확장, 비최소 위상 시스템(영동역학이 불안정한 시스템), 플랜트의 상대 차수(출력을 시간으로 몇 번 미분해야 입력이 처음 나타나는지를 나타내는 수)를 모르는 경우, 내부 모델을 넣어 특정 부류의 외란을 완전히 없애는 방법, 외란과 잡음을 함께 줄이는 방법, 디지털 장치에 구현하기 위한 이산 시간 외란 관측기로 넓혀 왔다고 적는다.[^dob] 2026년 2월 소식에 따르면 심형보 교수의 IEEE Fellow 선정 사유는 다개체 시스템과 외란 관측기에 관한 제어 이론 기여다.[^fellow] 대표 논문에서는 매개변수가 불확실한 선형 시스템에 시변 외부 시스템이 만들어 내는 외란이 들어올 때, 외란 모형을 담은 필터를 플랜트 앞에 붙이고 외란 관측기 기반 제어기로 강인하게 안정화해 모형화된 외란을 완전히 없앴고,[^p1] 상대 차수가 높은 플랜트에서 외란 관측기 안 고이득 관측기(큰 이득으로 출력과 그 도함수를 빠르게 추정하는 상태 관측기)의 이득이 상대 차수만큼 거듭제곱되어 생기는 수치 문제를, 이득을 고이득 매개변수의 최대 2차로 제한한 「저전력(low-power)」 외란 관측기로 풀었다.[^p2] 최근 논문 목록에는 불확실한 선형 시스템의 공칭 성능(설계에 쓴 기준 모형이 내는 성능)을 슬라이딩 모드로 점근적으로 되찾는 연구(IEEE Transactions on Industrial Electronics, 2026), 필터를 넣은 외란 관측기의 강인 안정 조건과 간단한 설계(International Journal of Control, Automation, and Systems, 2024), 출력을 바꿔 가며 다시 정의하는 외란 관측기로 하는 비최소 위상 선형 시스템의 강인 안정화(CDC 2024), 측정 잡음 아래에서 과도·정상 상태 성능을 보장하도록 외란 관측기 안 필터(Q-필터)의 대역폭을 정하는 연구(ICCAS 2025)도 있다.[^pubs]

둘째 갈래는 **다개체 시스템의 혼합 동역학과 분산 알고리즘**이다. 다개체 시스템(multi-agent system)은 여러 동적 개체가 통신망으로 정보를 주고받으며 함께 움직이는 시스템이다. 국문 연구 소개는 개체 사이의 정보 교환을 정하는 네트워크, 이산적인 네트워크로 이어진 연속적인 개체들, 느린 정보 교환으로 네트워크에 생기는 시간 지연 같은 요소까지 고려한 시스템을 다개체 시스템이라 부르고, 이런 시스템이 군집 자율 주행 같은 공학 문제의 해결과 생태계의 군집 현상 해석에서 중요하다고 적는다. 여기서 합의(consensus) 문제는 개체들이 주어진 네트워크로만 정보를 주고받으면서도 각자 상태 변수의 일부를 같은 값으로 수렴시키는 문제다.[^maskr] 영문 연구 소개에 따르면 연구는 출력만 주고받는 출력 궤환 합의에서 시작해 서로 다른(이종) 개체들의 합의와 내부 모델 문제로 나아갔고, 이종 개체들을 큰 결합 이득으로 묶으면 각 개체 벡터장(상태가 움직이는 방향과 빠르기를 정하는 함수)의 평균에 따라 움직이는 현상을 찾아 혼합 동역학 정리(blended dynamics theorem)로 정식화했다. 이 정리는 분산 최적화, 개체가 실행 중에 네트워크에 들어오고 나가도 알고리즘을 다시 초기화할 필요가 없는 플러그 앤 플레이 동작, 네트워크 크기 추정, 분산 상태 추정, 분산 중앙값·분위수·최빈값 계산으로 이어졌고, 출력만 결합하는 경우, 진동자 네트워크, 비선형 결합 이득(이웃과의 출력 차이가 미리 정한 시간에 따라 변하는 경계 안에 머물도록 결합 세기를 바꾸는 퍼널 결합), 이산 시간 통신, 연속이 아닌 이산적 가십(gossiping) 통신으로 넓어졌다고 적는다.[^mas] 분산 관측기는 각 센서가 전체를 관측할 능력이 없어도 네트워크 통신으로 전체 환경을 관측할 수 있게 하는 기술이다.[^maskr] 대표 논문에서는 혼합 동역학 정리의 이산 시간 판을 만들어, 연속 시간에서 이웃 사이의 높은 결합 이득이 하던 역할에 맞먹는 「다단계 결합(multi-step coupling)」을 제안하고 네트워크 크기 추정, PageRank 계산, 그래프 차수 수열 계산에 적용했으며,[^p3] 비동기 동작, 한쪽 방향 통신, 패킷 손실, 통신 지연을 포함한 여러 간헐적 통신 상황을 견디는 분산 관측기를 제안했다.[^p4] 현대자동차·기아 지능제어 공동연구실 과제로 대규모 V2G(vehicle-to-grid, 전기차가 전력망에서 충전할 뿐 아니라 남는 전력을 전력망으로 내보내는 방식) 운영을 위한 분산 최적화도 연구하며, 2022년 12월 워크숍 소식은 연구실 구성원들이 혼합 동역학으로 V2G 문제를 분산해서 푸는 방법을 제시했다고 적는다.[^hicl][^hiclws] 최근 논문 목록에는 방향 그래프에서 고정 시간 안에 가중치 균형을 맞추는 연구(IEEE Control Systems Letters, 2026), 이종 다개체 시스템의 매개변수 적응(CDC 2025), 상태 전이 확률이 서로 다른 다개체 마르코프 결정 과정의 분산 Q-러닝(CDC 2025), 혼합 동역학으로 하는 분산 최빈값 계산(Systems & Control Letters, 2025), V2G 시스템의 부하 평탄화를 위한 완전 분산 전기차 충전 일정(CDC 2024), 방위(bearing)만 재는 측정으로 하는 다개체 표적 위치 추정(ACC 2024)도 있다.[^pubs]

셋째 갈래는 **제어 시스템 보안과 제어기 암호화**다. 사이버 물리 시스템 보안 연구 소개는 사이버 물리 시스템(cyber-physical system, CPS)을 센서와 구동기를 가진 물리 시스템과 이를 제어하는 컴퓨팅 요소가 결합된 네트워크 기반 분산 제어 시스템으로 설명하고, 많은 시스템이 네트워크에 연결된 컴퓨터로 제어되면서 가상 공간의 보안 피해가 실제 물리 시스템으로 번질 수 있다고 적는다. 연구실은 제어 공학 관점에서 사이버 물리 시스템의 안전과 보안을 강화하는 방안을 연구해, 센서 공격과 외란·측정 잡음이 함께 있을 때도 동작하는 상태 추정기를 제안했고, 공격자 입장에서 외란 관측기를 쓰면 정확히 알 수 없는 시스템도 들키지 않고 공격할 수 있음을 밝혔으며, 입력 샘플링이 출력 샘플링보다 빠른 다중 샘플링 시스템에서 출력의 샘플링 순간에는 들키지 않는 공격을 보였다고 적는다.[^cps] 제어기 암호화 연구 소개는 그 목표를 네트워크에 연결된 제어 시스템 안의 사적 데이터를 보호하는 것, 곧 제3자가 제어 신호나 매개변수의 정보를 얻지 못하게 하는 것으로 적는다. 제어기의 모든 연산을 복호화 없이 암호 데이터끼리의 연산으로 처리하려면 동형암호(암호문을 풀지 않은 채 덧셈·곱셈 같은 연산을 할 수 있는 암호 방식)가 필요하며, 연구실은 서울대 수리과학부 천정희 교수팀과 함께 완전동형암호로 제어기를 암호화하는 알고리즘을 2016년에 발표했다고 적는다.[^enc] 2026년 9월 소식은 연구실이 동형암호로 암호화한 데이터 위에서 바로 동작하는 동적 제어기, LWE(Learning With Errors, 작은 오차가 더해진 선형 방정식들에서 비밀 값을 찾기 어렵다는 수학 문제)와 그 변형인 Ring-LWE 암호 체계에 기반한 효율적 구현, 최근에는 프라이버시를 지키는 최적화와 모델 예측 제어(앞으로 일정 구간의 움직임을 모형으로 예측해 최적 입력을 고르는 일을 매 순간 되풀이하는 제어)를 연구해 왔다고 적는다.[^teranishi] 대표 논문에서는 모든 신호가 암호화되어 비밀 키 없이는 이상을 알아채기 어려운 문제를, 암호화 동적 시스템의 영동역학을 LWE 기반 암호 방식에 넣어 이상 탐지용 잔차 신호(측정한 출력과 예측한 출력의 차이)만 저절로 드러나게 하는 방식으로 풀었고,[^p5] 제어기 출력을 정해진 개수의 이전 입출력의 선형 결합으로 나타내 암호화 제어기가 암호 데이터마다 정해진 횟수의 곱셈만 하게 하는 방법과, 여러 메시지를 암호문 하나에 담는 RLWE 기반 암호 체계에 맞춘 방법을 제안했다.[^p6] 최근 논문 목록에는 암호화 최적화를 위한 다항식 기반 QCQP(목적 함수와 제약식이 모두 이차식인 최적화 문제) 풀이기(CDC 2025), 검증 가능한 계산과 분산 집계로 하는 다개체 시스템 인증(CDC 2024), 균등 관측 가능 비선형 시스템의 복원력 있는 상태 추정의 계산 복잡도 축소(IEEE Transactions on Automatic Control, 2025), LWE 기반 동형암호를 쓰는 암호화 제어 방법들의 비교와 튜토리얼(Annual Reviews in Control, 2022)도 있다.[^pubs]

넷째 갈래는 **데이터 기반 제어와 뉴로모픽 제어**다. 이진규 교수가 공동 조직한 IFAC World Congress 2026 사전 워크숍 「Alternative Representations for Control: Neuromorphic, Data-driven, and Moment-based Methods」는 학습, 데이터 기반 방법, 뉴로모픽 시스템, 네트워크 시스템, 모멘트 기반 접근을 중심으로 동적 시스템을 나타내고 제어하는 다른 방법들을 다뤘고, 소식 글은 이 워크숍이 연구실의 다개체 시스템, 관측기 설계, 보안 제어, 분산 최적화, 뉴로모픽 공학 연구와 가깝다고 적는다.[^arc] 현대자동차·기아 지능제어 공동연구실 설립 소식은 연구실의 첫째 과제가 데이터 기반 제어 이론을 연구하는 것으로, 불확실성에 강인한 제어기 구현, D2PC(Data-Driven Predictive Control), DD-DOB(Data-Driven Disturbance Observer), MR-GPR(Model Reference Gaussian Process Regression)에 집중할 계획이라고 적고, 데이터 기반 제어의 기초 자료로 「시스템 식별을 하지 않고 실험 데이터로 제어기 설계하기」라는 부제의 해설을 든다.[^hicl] 2023년 12월 소식은 연구실이 가우스 과정 회귀(함수를 가우스 과정이라는 확률 모형으로 두고 관측 자료로 함수값과 그 불확실성을 추정하는 회귀 방법)와 그 제어 이론 응용을 연구해 왔다고 적는다.[^grussler] 대표 논문에서는 상태·입력 측정 자료로 가우스 과정 회귀가 찾아낸 시스템의 역모델(원하는 출력에서 필요한 입력을 계산하는 모형)을 바탕으로, 원하는 궁극 경계(시간이 충분히 지난 뒤 상태가 머무는 범위)에 이르기에 알맞은 기준 궤적을 자료에서 만들어 추종하는 비선형 시스템 제어기를 제안하고 자료가 갖춰야 할 충분조건을 제시했다.[^p7] 뉴로모픽 공학은 신경계의 구조와 동작 원리를 본떠 시스템을 설계하는 공학이다. 2024년 2월 소식에 따르면 이진규 교수(당시 Inria)는 혼합 동역학을 이종 개체들이 동기화를 강요받을 때 나타나는 창발적 집단 거동으로 설명하고, 생물 신경계에서 일어나는 스파이크(짧은 전기 펄스) 상호작용을 공학 알고리즘에 쓰는 방안을 이야기했다.[^etec] 대표 논문에서는 같은 비선형 진동자들의 위상을 분산 방식으로 맞추려고, 펄스로 결합한 뉴런 네트워크가 동기화해 아래층에 동기화된 강제 신호를 주고 아래층의 뉴런 쌍이 그 신호를 흉내 내는 스파이크 열을 만들어 진동자에 걸어 동조(진동자가 외부의 주기적 자극에 맞춰 진동하게 되는 현상)를 일으키는 계층 구조를 제안해, 연속 통신이나 진동자 측정 없이 위상 동기화를 얻었다.[^p8] 최근 논문 목록에는 데이터 기반 출력 궤환 제어기를 만드는 모델 기준 가우스 과정 회귀(ACC 2023), 비선형 시스템을 위한 데이터 기반 제어 방법 MR-GPR과 MR-NN의 평가(International Journal of Control, Automation, and Systems, 2024), 외란 관측기에 쓰는 선형 시스템의 데이터 기반 역시스템(ACC 2023)도 있다.[^pubs]

Research Overview가 든 주제 가운데 하이브리드 시스템은 연속 시간 역학과 이산 시간 역학으로 이루어진 동적 시스템이다.[^hybrid] 하이브리드 시스템 연구 소개는 연구실이 2014년에 상태 점프를 다듬어 연속 시간 동적 시스템과 비슷한 성질을 갖게 하는 글루잉(gluing) 방법을 개발했고, 이 방법을 쓰면 연속 시간 시스템용 제어·상태 추정 기법을 쓸 수 있다고 적는다.[^hybrid] 2025년 8월 소식은 하이브리드 시스템이 지금 연구실 연구자들의 큰 관심 주제라고 적는다.[^tran] 최근 논문 목록에는 느리고 빠른 시간 변화와 스위칭이 함께 있는 선형 시스템의 안정성(Nonlinear Analysis: Hybrid Systems, 2025), 자주 바뀌는 그래프로 이어진 네트워크를 분석하는 특이 섭동 하이브리드 시스템(IEEE Transactions on Automatic Control, 2025), 학습 기반 역변환으로 하는 비최소 위상 비선형 시스템의 점근적 출력 추종(International Journal of Robust and Nonlinear Control, 2024)이 있다.[^pubs]

## 주요 연구 주제

### 1. 외란 관측기로 하는 강인 제어

시변 외부 시스템이 만드는 외란을 완전히 없애는 외란 관측기 기반 제어, 상대 차수가 높은 시스템의 저전력 외란 관측기, 슬라이딩 모드·필터 삽입·출력 재정의 외란 관측기(대표 논문 1, 2).[^dob][^p1][^p2][^pubs]

### 2. 다개체 시스템의 혼합 동역학과 분산 알고리즘

혼합 동역학 정리와 그 이산 시간 판, 간헐적 통신을 견디는 분산 관측기, 분산 최적화와 분산 계산, V2G 운영을 위한 분산 최적화(대표 논문 3, 4).[^mas][^p3][^p4][^hicl]

### 3. 제어 시스템 보안과 제어기 암호화

이상 탐지용 잔차만 드러내는 LWE 기반 암호화 제어기, 곱셈 횟수를 제한한 동적 제어기 암호화와 RLWE 맞춤 구현, 센서 공격 아래의 상태 추정과 영동역학 공격(대표 논문 5, 6).[^cps][^enc][^p5][^p6]

### 4. 데이터 기반 제어와 뉴로모픽 제어

가우스 과정 회귀로 찾은 역모델을 쓰는 데이터 기반 제어, 적분-발화 뉴런으로 하는 진동자 위상 동기화(대표 논문 7, 8).[^hicl][^arc][^p7][^p8]

## 대표 논문

연구실 Publication in English 페이지의 2021–2026년 논문 가운데 심형보 교수나 이진규 교수가 마지막 저자인 학술지 논문을 네 연구 갈래에 두 편씩 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2025 | [Robust disturbance rejection for uncertain linear system with time-varying exo-system: A disturbance observer approach](https://doi.org/10.1016/j.automatica.2024.112100) · Automatica | 매개변수가 불확실한 선형 최소 위상 시스템(영동역학이 안정한 시스템)에, 선형 시변 외부 시스템(exo-system)이 만들어 내는 모형화된 외란이 들어올 때 이 외란을 완전히 없애는 문제를 다뤘다. 내부 모델 원리(외란이나 기준 신호를 만드는 모형을 제어기 안에 담아야 그 신호를 완전히 없애거나 따라갈 수 있다는 원리)에서 착안해, 외란 모형을 동역학 안에 담고 그 자신도 최소 위상인 필터를 플랜트 앞에 덧붙이는 것이 핵심이다. 그런 다음 플랜트와 필터를 이어 붙인 시스템을 외란 관측기 기반 제어기로 강인하게 안정화했다. 기존의 내부 모델 원리 기반 방법보다 설계가 간단하면서도, 큰 매개변수 불확실성과 모형에 없는 추가 외란에 강하고 과도 상태와 정상 상태 모두에서 미리 정한 공칭 추종 성능을 보장하는 외란 관측기 기법의 장점도 누린다. 제어기의 안정성과 성능은 특이 섭동 이론으로 분석했다.[^p1] | 1저자 H. Kim, 마지막 저자 심형보 |
| 2 | 2026 | [Low-Power Disturbance Observer for Linear Systems of High Relative Degree with Robust Stability Condition](https://doi.org/10.1007/s12555-026-00072-z) · International Journal of Control, Automation, and Systems | 외란 관측기 기반 제어는 외부 외란을 없애고 공칭 성능을 되찾는 강인 제어 기법이다. 그러나 플랜트의 상대 차수가 높으면 기존 외란 관측기는 구현에서 수치 문제를 겪는다. 안에 든 고이득 관측기의 이득이 시간 상수의 역수에 비례해 커지고 다시 상대 차수만큼 거듭제곱되어, 수치 불안정이 생길 수 있기 때문이다. 이를 풀려고 상대 차수가 아무리 커도 이득이 고이득 매개변수의 최대 2차로 제한되는 수정 외란 관측기를 제안했다. 핵심은 원래의 고이득 관측기를 이른바 「저전력(low-power)」 고이득 관측기로 바꾸는 것이다. 이 저전력 외란 관측기는 바깥 고리 제어기를 강인성을 따로 고려하지 않고 설계할 수 있게 하는 외란 관측기 본래의 능력을 지키면서, 수치 문제 없이 플랜트의 추정 상태도 바깥 고리 제어기에 준다. 강인 안정 조건을 특이 섭동 이론으로 분석했고, Kharitonov 정리(계수가 구간 안에서 바뀌는 다항식들의 안정성을 판별하는 정리)와 근궤적 기법(제어 이득을 바꿀 때 시스템 특성 방정식의 근이 움직이는 자취를 보는 방법)으로 설계 계수를 체계적으로 정하는 방법을 만들었으며, 수치 모의실험으로 이론 결과를 확인했다.[^p2] | 1저자 D. Song, 마지막 저자 심형보 |
| 3 | 2024 | [A design method of distributed algorithms via discrete-time blended dynamics theorem](https://doi.org/10.1016/j.automatica.2023.111371) · Automatica | 분산 계산 알고리즘을 설계하려고 혼합 동역학 정리의 이산 시간 판을 만들었다. 혼합 동역학 정리는 이종 다개체 시스템의 거동을 예측하게 해 주므로, 어떤 계산 과제에 맞는 혼합 동역학을 얻고 나면 개별 개체의 노드 동역학을 설계하는 생각이 쉽게 나온다. 연속 시간에서는 이웃 개체 사이의 높은 결합 이득이 혼합 동역학에 의한 예측을 가능하게 했는데, 이산 시간에서는 이와 맞먹는 작용으로 「다단계 결합(multi-step coupling)」을 제안했다. 연속 시간의 경우와 비교해 혼합 동역학이 결합 행렬에 따라 더 다양해질 수 있다는 이점을 세 응용으로 보였다. 네트워크 크기의 분산 추정, PageRank(링크 구조로 노드의 중요도를 매기는 값)의 분산 계산, 그래프 차수 수열(각 노드에 이어진 선의 개수를 늘어놓은 것)의 분산 계산이며, 각각 이중 확률 행렬(각 행과 각 열의 합이 1인 음이 아닌 행렬), 열 확률 행렬, 행 확률 행렬에 의한 결합에 해당한다.[^p3] | 1저자 J. W. Kim, 마지막 저자 심형보(이진규 교수 2저자) |
| 4 | 2025 | [A Distributed Observer Accommodating a Broad Range of Intermittent Communication Scenarios](https://doi.org/10.1109/LCSYS.2025.3583672) · IEEE Control Systems Letters | 간헐적 통신을 쓰면서 비동기 동작, 한쪽 방향 통신, 패킷 손실, 통신 지연을 포함한 폭넓은 상황을 견디는 분산 관측기를 제안했다. 일정 구간 동안 모은 연결이 전체를 잇는(jointly connected) 스위칭 통신망에서의 분석이 이를 뒷받침하며, 추정 오차가 지수적으로 수렴하는 조건을 준다. 이 조건으로 통신 빈도를 정할 수 있다. 분석은 각 개체의 관측 불가능 부분공간(그 개체의 측정만으로는 구별할 수 없는 상태들의 모임)이 불변인 직교 여공간을 가질 때 성립하며, 이는 시스템 행렬이 복소수 범위에서 대각화 가능하면 좌표 변환으로 늘 얻을 수 있는 성질이다.[^p4] | 1저자 S. Koo, 마지막 저자 심형보(이진규 교수 2저자) |
| 5 | 2026 | [A Learning With Errors-Based Encryption Scheme for Dynamic Controllers That Discloses Residue Signal for Anomaly Detection](https://doi.org/10.1109/TCNS.2026.3698371) · IEEE Transactions on Control of Network Systems | 암호화 제어 시스템은 사적 데이터의 기밀성을 보장하지만, 모든 신호가 암호화된 채로 남아 비밀 키 없이는 이상을 알아채기 어렵다. 이를 풀려고 이상 탐지용 잔차 신호는 저절로 드러내고 나머지 신호는 모두 비공개로 두는, 동적 제어기용 동형암호 방식을 제안했다. 이를 위해 정수로 이루어진 유한체(원소가 유한 개이고 0으로 나누기를 빼고 사칙연산이 닫혀 있는 수 체계) 위에서 정의한 암호화 동적 시스템의 영동역학을 밝히고, 이를 LWE 기반 암호 방식에 넣었다. 나아가 드러난 잔차 신호를 이용해, 상태 행렬이 정수가 아닌 동적 제어기도 재암호화 없이 암호 데이터 위에서 구현하는 방법을 제시했다.[^p5] | 1저자 Y. Jang, 마지막 저자 심형보 |
| 6 | 2025 | [Encrypted Dynamic Control Exploiting Limited Number of Multiplications and a Method Using RLWE-based Cryptosystem](https://doi.org/10.1109/TSMC.2024.3452007) · IEEE Transactions on Systems, Man, and Cybernetics: Systems | 연산 횟수나 깊이의 허용 범위가 다른 여러 동형암호 방식(somewhat, leveled fully, fully homomorphic encryption)을 포함해 대부분의 동형암호 방식으로 구현할 수 있는 동적 제어기 암호화 방법을 제시했다. 이를 위해 주어진 제어기의 출력을 정해진 개수의 이전 입력과 출력의 선형 결합으로 나타냈다. 그 결과 출력을 구동기 쪽에서 다시 암호화해 돌려보낸다고 가정하면, 암호화 제어기는 암호 데이터마다 정해진 횟수의 동형 곱셈만 하게 된다. 암호화 제어기가 무한한 시간 동안 미리 정한 성능을 내도록 매개변수를 고르는 지침도 주었다. 또 여러 메시지를 암호문 하나에 담아 동시에 연산할 수 있는 RLWE(ring learning with errors) 기반 암호 체계에 맞춘 방법을 제안해 계산과 통신 부담을 줄였다. 이전 결과와 달리 이 방법은 기본 덧셈과 곱셈 말고 회전(rotation) 같은 추가 알고리즘을 쓰지 않는다. 모의실험으로 효과를 보였다.[^p6] | 1저자 J. Lee, 마지막 저자 심형보 |
| 7 | 2024 | [Path Generating Inverse Gaussian Process Regression for Data-Driven Ultimate Boundedness Control of Nonlinear Systems](https://doi.org/10.1109/LCSYS.2024.3403525) · IEEE Control Systems Letters | 비선형 시스템을 위한 데이터 기반 궁극 유계 제어기(시간이 지나면 상태가 정해진 범위 안에 들어와 머물게 하는 제어기)를 제안했다. 제어기는 상태·입력 측정 자료로 가우스 과정 회귀가 찾아낸 시스템의 역모델을 바탕으로, 원하는 궁극 경계에 이르기에 알맞은 기준 궤적을 추종하도록 설계된다. 특히 알맞은 기준 궤적을 시스템 식별에 쓴 자료를 바탕으로 능동적으로 만들어 내므로, 이 제어기를 경로 생성 역 가우스 과정 회귀(PGIGP) 제어기라 불렀다. PGIGP 제어기가 원하는 궁극 경계로 궁극 유계를 보장하기 위해 자료가 갖춰야 할 충분조건을 주었고, 이 조건이 자료를 모으는 실용 지침이 될 수 있으며 거꾸로 주어진 자료로 이룰 수 있는 제어 성능의 기준선을 정하는 데 쓰일 수 있음을 보였다. 수치 모의실험으로 효과를 보였다.[^p7] | 1저자 Y. Jang, 마지막 저자 심형보 |
| 8 | 2026 | [Distributed phase synchronization through neuromorphic entrainment by synchronized integrate-and-fire neurons](https://doi.org/10.1016/j.sysconle.2026.106559) · Systems & Control Letters | 같은 비선형 진동자들의 위상을 분산 방식으로 맞추는, 신경세포에서 착안한 방법을 제안했다. 틀은 위아래 두 층으로 된 계층 구조다. 위층에서는 펄스로 결합한 뉴런들의 네트워크가 동기화를 이루고 동기화된 강제 신호를 아래층에 준다. 아래층에서는 뉴런 쌍들이 그 강제 신호를 흉내 내는 스파이크 열을 만들어 비선형 진동자에 걸고, 진동자가 이에 동조한다. 그 결과 네트워크의 연속 통신이나 연속 강제 신호, 진동자 측정 없이 점근적 위상 동기화를 이룬다. 반 데르 폴 진동자(진폭에 따라 감쇠가 달라지는 비선형 항 때문에 일정한 주기 진동으로 수렴하는 진동자 모형)를 쓴 수치 예제로 방법을 보였다.[^p8] | 1저자 D. Song, 마지막 저자 이진규 |

## 교수와 전문 분야

심형보 교수는 서울대학교에서 전기공학 학사(1993), 석사(1995), 박사(2000)를 받았고, University of California, Santa Barbara의 CCEC에서 박사후 연구원(2000–2001)으로 있었다. 한양대학교 전자전기컴퓨터공학부 조교수(2002–2003)를 거쳐 2003년부터 서울대학교 전기·정보공학부에 있으며, University of Illinois, Urbana-Champaign의 Coordinated Science Laboratory 방문 연구원(2010–2011), 일본 게이오대학교 객원교수(2016)를 지냈다.[^shimcv][^eceshim] 개인 누리집은 교수의 지금 직함으로 전기·정보공학부 교수, 수리과학부 겸임교수(Adjunct professor), 제어 및 동역학 연구실 책임자(PI), Engineering Research Center for Trustworthy Distributed Physical Systems 센터장을 적고,[^shimhome] 학부 전임교수 목록은 「심형보교수(학생센터장)」로 올린다.[^ecefac] 학부 교수 상세는 학위를 「서울대학교 전기공학부 박사 (2000)」, 전공을 「제어이론 / 동적 시스템」으로 적는다.[^eceshim]

교수 CV는 Automatica(2014–2018), IEEE Transactions on Automatic Control(2012–2013), International Journal of Robust and Nonlinear Control(2009–2012), European Journal of Control(2008–2010), International Journal of Control, Automation, and Systems(2006–2007)의 부편집장(Associate Editor)과 International Journal of Control, Automation, and Systems의 Editor(2011–2013)을 적고, IFAC World Congress 2026 대회장(General Chair), IEEE Control Systems Society 이사회 구성원(Member of Board of Governors, 2024), IFAC Distinguished Lecturer Program Committee 위원장(2026–2029), 서울대학교 자동화시스템공동연구소 소장(2020–2022)과 Engineering Research Center for Advanced Control and Instrumentation 센터장(2016–2020)을 적는다.[^shimcv] 2021년 10월 이후의 영예로는 CV가 IEEE 학술활동상(ICROS, 2022), Fellow of ICROS(2022), 서울대학교 공과대학 Excellent Teaching Award(2023), IFAC Distinguished Lecturer(2023–2026), 한국과학기술한림원 정회원(2024), IFAC Outstanding Service Award(2026), IEEE Fellow(2026)를 적는다.[^shimcv] 2026년 2월 소식은 IEEE Fellow 선정 사유를 「contributions to control theory on multi-agent systems and disturbance observers」로 적고,[^fellow] 2024년 1월 소식은 한국과학기술한림원 2024년 정회원 선출을 알린다.[^kast] People 페이지는 그 밖에 제어로봇시스템학회(ICROS)의 Young Researcher Award(2009)와 Scientific Award(2012), ICCAS 2014 프로그램 위원장과 IFAC World Congress 2008 부프로그램 위원장을 적는다.[^people]

심형보 교수의 개인 누리집 논문 목록은 주제별 보기에서 논문을 외란 관측기, 다개체 시스템, 비선형 관측기, 출력 궤환 안정화, 안정성 해석, 제어 방법, 제어 시스템 보안, 스위칭·하이브리드 시스템, 병렬 피드포워드 보상기, 생물 동역학과 제어, 데이터 기반·학습, 기타의 열두 묶음으로 나누며, 2021년 이후 논문이 있는 묶음은 외란 관측기, 다개체 시스템, 비선형 관측기, 안정성 해석, 제어 방법, 제어 시스템 보안, 스위칭·하이브리드 시스템, 데이터 기반·학습이다.[^shimpubs] 학부 교수 상세의 Research Interest 칸은 비선형 시스템 제어 및 해석, 생물 동역학의 제어와 해석(HIV 감염 치료), 내부 모델 원리와 주기 외란 제거 응용, 비선형 동역학의 상태 관측기 설계, 출력 궤환 안정화를 적는다.[^eceshim] 논문으로 보면 지금 심형보 교수의 전문 분야는 외란 관측기 이론(대표 논문 1, 2), 혼합 동역학으로 하는 다개체 시스템과 분산 알고리즘(대표 논문 3, 4), 동형암호로 하는 제어기 암호화(대표 논문 5, 6), 가우스 과정 회귀를 쓰는 데이터 기반 제어(대표 논문 7)다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7]

이진규 교수는 서울대학교에서 학사(2009.3–2013.2)와 석박사 통합과정(2013.3–2019.8)을 마쳤다. 학부 교수 상세는 학사를 「서울대학교 전기정보공학부」, 석박사를 「서울대학교 전기컴퓨터공학부」로 적는다.[^ecelee] 박사 논문은 「Practical Synchronization among heterogeneous agents: A tool for analysis and synthesis」(2019)다.[^leehome][^alumni] 개인 누리집의 학력·경력 칸에 따르면 이후 University of Cambridge 공학과 Control Group의 Visiting Research Fellow(2019.9–2020.8)와 Research Associate(2020.10–2021.7), 서울대학교 전기·정보공학부 박사후 연구원(2021.8–2022.4), Imperial College London 전기전자공학과 Research Associate(2022.5–2022.9), Centre Inria de l'Université de Lille의 Valse 팀 ISFP(Inria Starting Faculty Position, 2022.12–2024.7)를 지냈다.[^leehome] 학부 교수 상세는 2021–2022년 경력을 「서울대학교 자동화시스템공동연구소 박사후 연구원」으로 적고, 「2024- : 서울대학교 전기정보공학부 조교수」를 적는다.[^ecelee] 개인 누리집은 수상으로 한국연구재단 Fully Funded Fellowship(2019.9–2020.8), 11th IFAC Symposium on Nonlinear Control Systems(NOLCOS)의 IFAC Young Author Award 최종 후보(Finalist, 2019), IEEE Control Systems Letters의 Outstanding Service as Reviewer(2023)를 적고, 활동으로 Annual European Systems & Control PhD Thesis Award 심사위원(2023), IEEE Conference on Decision and Control 2023 「Identification I」 세션 좌장, Frontiers in Control Engineering의 Review Editor(2020–)를 적는다.[^leehome] 서울대 부임 뒤에는 연구실에서 BK21 Zoom Seminar Series on Control Theory(2026년 1월 23일–3월 5일, 14회)를 주관했고,[^bk21zoom] IFAC World Congress 2026 사전 워크숍 「Alternative Representations for Control」을 함께 조직하고 마지막 발표를 맡았다.[^arc]

이진규 교수의 개인 누리집 논문 목록은 2024년까지의 논문을 싣는다. 심형보 교수와 함께 쓴 혼합 동역학·퍼널 결합 논문(Automatica, 2022·2023)과 함께, 서울대 부임 전에 Rodolphe Sepulchre 교수와 쓴 약한 시냅스 결합으로 하는 빠르고 강인한 동기화(Automatica, 2024)와 열린 고리 수축 설계(CDC 2022), Alessandro Astolfi 교수와 쓴 모멘트로부터의 선형 시스템 실현(CDC 2023), 대형 제어 논문(Entropy, 2024; CDC 2021)이 있다.[^leepubs] 논문으로 보면 지금 이진규 교수의 전문 분야는 다개체 시스템의 혼합 동역학과 분산 관측기(대표 논문 3, 4)와 신경세포 방식 통신을 쓰는 뉴로모픽 동기화(대표 논문 8)다.[^p3][^p4][^p8]

## 응용 분야

Research Overview는 새 비선형 제어 도구가 군사, 항공우주, 고정밀 기계, 생물학에서 나타나는 비선형성이 강한 시스템의 제어기 설계를 가능하게 했다고 적는다.[^overview] 국문 다개체 시스템 연구 소개는 합의 문제를 풀면 자동차들이 속도와 앞차와의 거리를 맞춰 공기 저항을 줄이고 연료 효율을 높이는 군집 자율 주행을 할 수 있고, 각 센서가 전체를 관측하지 못해도 넓은 환경을 관측하는 센서 네트워크를 설계할 수 있으며, 서로 똑같지 않은 세포들이 함께 역할을 해내는 생물학적 시스템의 해석에도 쓰일 수 있다고 적는다.[^maskr] 외란 관측기 연구 페이지는 응용 예로 디젤 발전기와 배터리 저장 장치를 함께 쓰는 마이크로그리드의 부하 주파수 제어, 강화학습 기반 제어기의 강인성 향상, 대형 차량 군집 주행의 연비 개선, 장비를 단 멀티로터(드론) 제어 실험을 든다.[^dob] 사이버 물리 시스템 보안 연구 소개는 스마트폰·자동차 같은 일상 기기부터 발전소, 상하수도, 공항, 철도 같은 기반 시설까지 네트워크에 연결되면서 사이버 공격이 실제 제어 시스템을 위협할 수 있다고 적고,[^cps] 제어기 암호화 연구 소개는 동형암호 기반 제어기를 드론 자율 비행 시스템에 처음 실증한 공동 논문(IEEE Access, 2018)을 소개한다.[^enc] Funded Projects 페이지는 진행 중인 과제로 현대자동차의 대규모 V2G 운영을 위한 분산 최적화 연구와 데이터 기반 제어기의 모형 불확실성 강인성 향상 연구, 국방과학연구소의 Artificial Intelligence based Flight Control Research Laboratory 과제를 적는다.[^projects] 졸업생의 진로로는 KTH, Purdue University, University of Oxford, 숙명여자대학교의 박사후 연구원, 한국철도기술연구원, 현대자동차, 삼성전자, 삼성SDI, Naver Labs, KIST, 국방과학연구소, 한국항공우주산업(KAI), 그리고 국립한국교통대학교·인천대학교·서울과학기술대학교·세종대학교·서울시립대학교·숙명여자대학교·한국기술교육대학교의 교수가 있다.[^alumni]

## 구성원

2026년 10월 25일 누리집 People 페이지 기준 Student 칸의 18명이다. 과정은 학생 소개 문장의 표기(Ph.D. candidate·Ph.D. student는 박사과정, M.S. student·M.S. candidate는 석사과정으로 적고, 괄호 안 combined M.S./Ph.D.와 학과 이름은 원문)를 옮겼고, 시작은 소개 문장의 「Since 연도」, 연구 주제는 카드의 Research 칸, 이메일은 카드의 표기다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Seongjun Kim (김성준) | 박사과정 |  | Passivation of non-passive systems, Distributed estimation | sjkim@cdsl.kr |  |
| Seungbeom Lee (이승범) | 박사과정 | 2020 | Encrypted control systems, Cyber-physical systems, Verification of controllers | sblee@cdsl.kr |  |
| Heein Park (박희인) | 박사과정 |  | Nonlinear systems and control | phoinee@cdsl.kr | 7 |
| Deuksun Hong (홍득선) | 박사과정 (combined M.S./Ph.D.) | 2021 | Learning-based robust control, Data-driven control | dshong@cdsl.kr |  |
| Donghyeon Song (송동현) | 박사과정 (combined M.S./Ph.D.) | 2022 | Disturbance observer, Encrypted control, Neuromorphic engineering | dhsong@cdsl.kr | 2, 8 |
| Jinwook Heo (허진욱) | 박사과정 (combined M.S./Ph.D.) | 2022 | Multi-agent systems, Distributed optimization | jwheo@cdsl.kr |  |
| Yeongjun Jang (장영준) | 박사과정 (combined M.S./Ph.D.) | 2022 | Data-driven control, Encrypted control systems | jangyj@cdsl.kr | 5, 7 |
| Hyungjo Byun (변형조) | 박사과정 (combined M.S./Ph.D.) | 2023 | Reinforcement learning, Multi-agent systems | hjobyun@cdsl.kr |  |
| Sihyun Ahn (안시현) | 박사과정 |  | Stochastic approximation, Multi-agent systems, Model predictive control | shahn@cdsl.kr |  |
| Sunghyun Koo (구성현) | 박사과정 (combined M.S./Ph.D.) | 2024 | Multi-agent systems, Distributed estimation, Path integral methods | shkoo@cdsl.kr | 4 |
| Yong Joo Do (도용주) | 박사과정 (combined M.S./Ph.D.) | 2024 | Stochastic process, Multi-agent systems, Learning-based control | yjdo@cdsl.kr |  |
| Hyeonyeong Jang (장현영) | 박사과정 (combined M.S./Ph.D.) | 2024 | Moment based control, Hybrid systems and applications, Multi-agent systems, Data-driven control | hyjang@cdsl.kr | 8 |
| Yunjeong Yang (양윤정) | 석사과정 (combined M.S./Ph.D.) | 2025 | Multi-agent systems, Data-driven control | yjyang@cdsl.kr |  |
| Seokho Jeong (정석호) | 석사과정 (combined M.S./Ph.D.) | 2025 | Multi-agent systems, Data-driven control | shjeong@cdsl.kr |  |
| Heemin Moon (문희민) | 석사과정 (Department of Future Automotive Mobility) | 2025 | Data-driven control | hmmoon@cdsl.kr |  |
| Yosep Son (손요셉) | 석사과정 (Department of Future Automotive Mobility) | 2026 | Path integral methods, Model predictive control | ysson@cdsl.kr |  |
| Sangyoon Lee (이상윤) | 석사과정 (combined M.S./Ph.D.) | 2026 | Multi-agent systems, Moment matching, Neuromorphic control and systems | sylee@cdsl.kr |  |
| Sungyoung Kim (김성영) | 석사과정 (combined M.S./Ph.D.) |  | Reinforcement Learning | sungyoungkim041@cdsl.kr |  |

## 졸업생과 이전 구성원

누리집 Alumni 페이지의 Recent Ph.D Alumni 23명, Recent Master Alumni 4명, Recent Post-doc Alumni 4명과 All Alumni List 표의 91명(1–91번)이다. 앞의 세 칸은 이름 옆의 학위와 연도, 학위 논문(Thesis), 진로(After graduation 줄과 Currently 줄), 일부 졸업생 칸에 적힌 수상을 옮겼고, Recent Post-doc Alumni는 칸에 적힌 박사 학위 기관과 지금 직위를 옮겼다. All Alumni List는 표의 번호 순서대로 이름, 학위(연도), 진로 칸을 옮겼으며, Recent 칸의 졸업생 일부와 심형보 교수(26번)도 이 표에 함께 올라 있다.[^alumni] Former Visitors 페이지는 장기 방문자 10명을 적고, 그 가운데 2021년 이후 방문은 Yutian Wang(Northeastern University 박사과정, 2021.9.1–2022.8.1)과 Sebastian Schlor(Stuttgart University 박사과정, 2024.10.15–2025.1.31)다.[^visitors]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 | 랩이 적은 수상 |
|---|---|---|---|---|
| Joowon Lee (이주원) | Ph.D. (2026) | Post-doc at KTH, Sweden | Input-Output Data-Driven Representation for Linear Systems: Stability and Applications |  |
| Soojeong Hyeon (현수정) | Ph.D. (2025) | Post-doc at Sookmyung Women’s University | Bearing-only Target Localization by a Group of Agents and Range-only Displacement-based Formation Control |  |
| Hamin Chang (장하민) | Ph.D. (2025) | Post-doc at Purdue University | Inverse Dynamics and Control: Model-based and Learning-based Approaches |  |
| Hyuntae Kim (김현태) | Ph.D. (2024) | Post-doc at University of Oxford | Asymptotic Nominal Performance Recovery of Disturbance Observer |  |
| Jiyeon Nam (남지연) | Ph.D. (2024) | Korea Railroad Research Institute | Initialization-free Dynamic Average Consensus Algorithm and Its Application to Time-delay Systems, Distributed Optimization, and Pose-graph SLAM |  |
| Jeongmo Seong (성정모) | Ph.D. (2024) | Hyundai Motor Company | Asymptotic Synchronization of Heterogeneous Multi-agent Systems by Adaptive Diffusive Coupling |  |
| Jongsoo Ha (하종수) | Ph.D. (2024) |  | Sampled-Data Systems Employing Gerneralized Holds: Fundamental Limitations and Realizable Design |  |
| Dongil Lee (이동길) | Ph.D. (2023) | Post-doc at KIST; Currently a professor at Incheon National University | Decentralized Design of Distributed Controller for Output Regularization of Multi-Channel Systems |  |
| Jeongwoo Kim (김정우) | Ph.D. (2023) | Hyundai Motor Company | Design of Distributed Algorithms via Discrete-Time Blended Dynamics Theorem |  |
| Seungjoon Lee (이승준) | Ph.D. (2021) | Naver Labs | Consensus of Linear Time Invariant Multi-agent Systems over Multilayer Network |  |
| Junsoo Kim (김준수) | Ph.D. (2020) | Post-doc at KTH, Sweden; Currently a professor at Seoul National University of Science and Technology | Homomorphic Encryption of Linear Dynamic Controllers to Operate for Infinite Time Horizon |  |
| Jihan Kim (김지한) | Ph.D. (2020) | Samsung SDI | Design and Countermeasure of Stealthy Attacks on Cyber-Physical Systems in Sampled-data Framework |  |
| Taekyoo Kim (김태규) | Ph.D. (2019) | Post-doc at CDSL; Currently a professor at Korea National University of Transportation | Fully decentralized design for distributed observer for linear timeinvariant systems |  |
| Jin Gyu Lee (이진규) | Ph.D. (2019) | Post-doc at University of Cambridge; Currently a professor at Seoul National University | Practical Synchronization among heterogeneous agents: A tool for analysis and synthesis |  |
| Chanhwa Lee (이찬화) | Ph.D. (2018) | Hyundai Motor Company; Currently a professor at Sejong University | Attack-resilient feedback control systems: Secure state estimation under sensor attacks | 학문후속세대 장학생 (2015-2017); 휴먼테크 논문대상 동상 (2015); 우수 논문상 (CICS 2014) |
| Hyeonjun Yun (윤현준) | Ph.D. (2018) | Samsung Electronics | Privacy-Guaranteed Distributed Optimization Algorithms for Power Network Systems | SICE Annual Conference International Award (2017); IFAC 2008 참여기금상 (2017) |
| Gyunghoon Park (박경훈) | Ph.D. (2018) | KIST; Currently a professor at University of Seoul | Theory of Disturbance Observers: A New Perspective on Inverse Model-based Designs | 산업통상자원부 장관상 (ICCAS 2015 & ICCAS 2014); Excellent Joint Research Award (Seoul National University, 2017) |
| Jisu Kim (김지수) | Ph.D. (2017) | Agency for Defense Development | State Estimation and Tracking Control for Hybrid Systems by Gluing the Domains | 최우수 학생 논문상 (2012) ICROS 학술대회; ICROS 학술대회 우수 논문상 (2016) |
| Jaeyong Kim (김재용) | Ph.D. (2016) | Samsung Electronics | Robust consensus and synchronization in heterogeneous multi-agent systems | Student best paper award (ICCAS 2012) |
| Hyungjong Kim (김형종) | Ph.D. (2016) | Samsung Electronics; Currently a Principal Researcher at Korea Institute of Industrial Technology | Adaptive Output Regulation for Linear Systems with Unknown Sinusoidal Exogenous Inputs | 서울대학교 전기정보공학부 우수 박사논문상 |
| Youngjun Joo (주영준) | Ph.D. (2014) | Post-doc at University of Central Florida; Currently a professor at Sookmyung Women’s University | Theoretical analysis of disturbance observer: stability and performance | ICCAS 2016 우수 논문상 |
| Hansung Cho (조한성) | Ph.D. (2014) | Samsung Electronics | Nonlinear observer design via reduced-order dynamic observer error linearization and extended nonlinear observer canonical form |  |
| Hongkeun Kim (김홍근) | Ph.D. (2012) | Post-doc at Groningen Univ., Netherland; Currently a professor at School of Mechatronics Engineering, Korea University of Technology and Education | Consensus and synchronization among output-coupled identical and non-identical linear systems through fast switching network |  |
| Gaeun Kim (김가은) | M.S. (2025) | Hyundai Motor Company | Disturbance Observers with Reference Injection for Robust Tracking of Uncertain Linear Systems |  |
| Si Hyun Ahn (안시현) | M.S. (2025) | Ph.D student at CDSL | Stability analysis of nonlinear systems in a separable form of slow and fast time parameters |  |
| Minryong Kim (김민령) | M.S. (2020) | Samsung Electronics | Learning With Errors 기반 제어기 암호화 라이브러리와 파라미터 결정 알고리즘 |  |
| Hyemin Lim (임혜민) | M.S. (2016) | Korea Aerospace Industries(KAI) | Consensus of linaer multi-agent systems with multilayer network using output feedback controller |  |
| Gia Quoc Bao TRAN | Post-doc (Ph.D, Mines Paris, Université Paris Sciences et Lettres, France) | Post-doc at University of Illinois Urbana-Champaign, USA |  |  |
| Ismi Rosyiana Fitri | Post-doc (Ph.D, Seoul National University of Science and Technology, Korea) | Assistant Professor, Universitas Indonesia, Indonesia |  |  |
| Abhisek Behera | Post-doc (Ph.D, Indian Institute of Technology at Bombay, India) | Assistant Professor, Indian Institute of Technology at Roorkee and Patna, India |  |  |
| Zhaowu Ping | Post-doc (Ph.D, Chinese University of Hong Kong, China) | Professor, Hefei University of Technology, China |  |  |
| 이상혁 |  |  |  |  |
| 장영수 | 석사(88)/박사(93) | LG전자 Information Display 부문 |  |  |
| 공재섭 | 석사(89)/박사(96) |  |  |  |
| 김학용 |  |  |  |  |
| 이정준 | 석사(90) | LS산전 / 연구위원 |  |  |
| 배영환 | 석사(90) | Intersil(Renesas)/엔지니어 |  |  |
| 이종필 | 석사(91) | Broadcom Limited |  |  |
| 노대종 | 석사(90)/박사(01) | 삼성전자 |  |  |
| 박경철 | 석사(92)/박사수료(00) | (주)비슬로 / 대표이사 |  |  |
| 최진한 | 석사(90) | 헌터스기술 |  |  |
| 주성준 | 석사(92)/박사(97) | 호서대학교 디지털제어과/교수; (주)이잰 대표이사 |  |  |
| 진주화 | 석사(91)/박사(00) |  |  |  |
| 박용환 | 석사(92)/박사(97) |  |  |  |
| 이상용 |  |  |  |  |
| 이종명 |  |  |  |  |
| 유영준 | 석사(92.5) | Samsung Research America |  |  |
| 조철형 | 석사(93)/박사(98) | 앳폰주식회사 대표이사 |  |  |
| 김준석 |  |  |  |  |
| 변지준 | 석사(94) | LG전자 경영전략부문 |  |  |
| 유성욱 |  |  |  |  |
| 조남훈 | 석사(94)/박사(00) | 숭실대학교 전기공학부/교수 |  |  |
| 최영문 |  |  |  |  |
| 김태훈 | 석사(95) |  |  |  |
| 박일훈 | 석사(95) | 두산중공업 |  |  |
| 손영익 | 석사(97)/박사(02) | 명지대학교 전기공학과 |  |  |
| 심형보 | 석사(95)/박사(00) | 서울대학교 전기정보공학부/교수 |  |  |
| 천관호 | 석사(95)/박사(02) | 충남대학교 전기공학과 |  |  |
| 윤장현 | 석사(96) |  |  |  |
| 최상철 | 석사(95) |  |  |  |
| 김용민 | 석사(96) |  |  |  |
| 남동경 | 석사(96) | 삼성전자 (종합기술원) |  |  |
| 유경탁 | 석사(96)/박사(06) | 목동탁일학원장 |  |  |
| 구현철 | 석사(97) | 건국대학교 전자공학과/교수 |  |  |
| 여운승 | 석사(99) | 이화여대 융합콘텐츠학과/부교수 |  |  |
| 이장원 | 석사(97) | 애플 |  |  |
| 강민수 | 석사(99) | 코맥스 |  |  |
| 박지훈 | 석사(98) | Hyundai MIB International |  |  |
| 이주석 | 석사(98) | 파크시스템스 |  |  |
| 정용식 | 석사(99) | ETRI/변리사 |  |  |
| 이상민 |  |  |  |  |
| 백주훈 | 박사(04) | 광운대학교 로봇학부/부교수 |  |  |
| 김기범 |  |  |  |  |
| 박성현 |  |  |  |  |
| 양원준 |  |  |  |  |
| 지일훈 |  |  |  |  |
| 양종욱 |  |  |  |  |
| 박승언 |  |  |  |  |
| 복나리 |  |  |  |  |
| 이정용 | 석사(2002) | 한국과학기술원 EEWS대학원/교수 |  |  |
| 최용운 |  |  |  |  |
| 백재민 |  |  |  |  |
| 한승주 | 석사(03) | 삼성종합기술원 |  |  |
| 장혁준 | 석사(04) | 국민대학교 전자공학부/조교수 |  |  |
| 정승균 | 석사(04) |  |  |  |
| 서상보 | 석박사통합(2010) | 가천대 의용생체공학과 연구교수 |  |  |
| 오현정 | 석사(06) | KT Service연구소 |  |  |
| 남희현 | 석사(06) | 삼성전자 메모리사업부 |  |  |
| 이재화 | 석사 2006 | Postdoc, University of Oxford |  |  |
| 조원민 | 석사(07) | 국방과학연구소/선임연구원 |  |  |
| 김홍근 | 석박사통합(2012) | 한국기술교육대학교 메카트로닉스공학부/조교수 |  |  |
| 조한성 | 석박사통합 (2014) | 삼성전자 생산기술연구소/책임연구원 |  |  |
| 주영준 | 석사(07)/박사(14) | Post-doc(University of Central Florida) |  |  |
| 방재성 | 박사(10) | 현대자동차 |  |  |
| 강세진 | 석사(08) | NH아문디자산운용 |  |  |
| 김병인 | 석사(08) | 삼성증권 |  |  |
| 김상훈 | 석사(08) | 현대다이모스 |  |  |
| 김태규 | 석사(09) | 서울대 전기정보 박사과정 |  |  |
| Artem Shamsuarov |  |  |  |  |
| 김수범 | 석사(10) | 해군 소령 |  |  |
| 이진영 | 석사(10) | 삼성전자 |  |  |
| 이찬화 | 석사(10) | 서울대학교 전기정보공학부/박사과정 |  |  |
| 정진우 | 석사(10) | 삼성전자/변리사 |  |  |
| 이성훈 | 석사(10) | 특허법인 고려/변리사 |  |  |
| 김형종 | 박사(16) | 삼성전자 |  |  |
| 김형준 | 석사(11) | SK이노베이션 |  |  |
| 김성준 | 석사(11) | 국방과학연구소 |  |  |
| 김상현 | 석사(12) | 서울대학교 전기정보공학부/박사과정 |  |  |
| 김재용 | 석박사통합(16) | 삼성전자 VD사업부/책임연구원 |  |  |
| 최현철 |  | 현대오트론 |  |  |
| 좌동경 |  | 아주대학교 전자공학과/교수 |  |  |
| 김정수 |  | 서울과학기술대학교/부교수 |  |  |
| Dmitry Vengertsev |  |  |  |  |
| 김지수 |  |  |  |  |
| 윤형주 | 석사(12) |  |  |  |
| 박경훈 | 석사(13) | 서울대학교 전기컴퓨터공학부/박사과정 |  |  |
| 윤현준 |  | 서울대학교 전기정보공학부/박사과정 |  |  |
| 한우석 | 석사(2013) | 서울대학교 의과대학/박사과정 |  |  |
| 오상록 | 석사(2015) |  |  |  |
| Zhaowu Ping |  |  |  |  |
| 홍용준 | 석박통합과정(2014/1) | 서울대학교 전기정보공학부 석박통합과정 |  |  |
| 임혜민 | 석사졸업(2017) | KAI/KFX제어SW팀 제어법칙파트 |  |  |

## 최근 논문 목록 (2021–2026)

연구실 Publication in English 페이지(281건) 2021–2026년 연도 구역에서 저자 칸에 심형보 교수나 이진규 교수가 적힌 66편과, 연구실 목록에 없고 이진규 교수 개인 누리집 Publications 쪽에만 있는 2021–2024년 논문 4편(줄 끝에 「이진규 교수 개인 누리집 목록」으로 표시)이다. 연도는 연구실 페이지의 연도 구역(개인 누리집 논문은 그 목록이 적은 연도)이고, 제목·저자·학술지와 학회 이름은 누리집 표기 그대로다. 학술지 이름이 빈 2026년의 한 줄(「A Learning With Errors based Encryption Scheme for Dynamic Controllers that Discloses Residue Signal for Anomaly Detection」)은 같은 누리집의 2026년 9월 17일 소식 글이 적은 학술지 이름이다.[^pubs][^leepubs][^tcnspost] 이진규 교수는 2024년 9월 1일 서울대에 부임했으므로, 목록에서 그 전에 나온 이진규 교수의 논문은 부임 전 박사후 연구원·연구원으로 있던 때(케임브리지 대학교, 서울대학교 자동화시스템공동연구소, 임페리얼 칼리지 런던, Inria)의 논문이다.[^lee24][^ecelee] 2023년 구역의 「Distributed Resilient Observer: Blended Dynamics Theory Meets ℓ1-Minimization Approach」는 학회(CDC 2023) 줄과 학술지(IEEE Control Systems Letters) 줄로 두 번 올라 있다. 개인 누리집 목록의 *는 누리집 표시이며, 누리집은 그 뜻을 적지 않는다.[^pubs][^leepubs]

**2026**

- G. Q. Bao Tran, Daniel Liberzon, Hyungbo Shim. "Stability of Slow-Fast Nonlinear Dynamics: Non-Periodic Case". *27th International Symposium on Mathematical Theory of Networks and Systems (MTNS 2026), pp. 127–132, International Federation of Automatic Control (IFAC) Waterloo, ON, Canada, 2026*.
- Donghyeon Song, Hyeonyeong Jang, Giordano Scarciotti, Jin Gyu Lee. "Distributed Phase Synchronization through Neuromorphic Entrainment by Synchronized Integrate-and-fire Neurons". *Systems & Control Letters, iss. 217, no. 106559, 2026*.
- Aneel Tanwani, Hyungbo Shim, Andrew R. Teel. "On Asymptotic Stability of Hybrid Systems with Frequent Updates and Sampled-data Observers". *European Journal of Control, 2026*.
- Jinwook Heo, Jin Gyu Lee, Hyungbo Shim. "Fixed-Time Weight Balancing Over Digraphs Even Under Disturbances". *IEEE Control Systems Letters, 2026*.
- Yeongjun Jang, Joowon Lee, Junsoo Kim, Takashi Tanaka, Hyungbo Shim. "A Learning With Errors based Encryption Scheme for Dynamic Controllers that Discloses Residue Signal for Anomaly Detection". *IEEE Transactions on Control of Network Systems, 2026*.
- Donghyeon Song, Hyuntae Kim, Hyungbo Shim. "Low-Power Disturbance Observer for Linear Systems of High Relative Degree with Robust Stability Condition". *International Journal of Control Automation and Systems, vol. 24, iss. 6, pp. 1297-1307, 2026*.
- Hyuntae Kim, Hyungbo Shim, Mohammad Ataei, Nam Hoon Jo, Gyunghoon Park. "A Sliding Mode Approach to Asymptotic Recovery of Nominal Performance for Uncertain Linear Systems". *IEEE Transactions on Industrial Electronics, 2026*.

**2025**

- Sebastian Schlor, Andrea Iannelli, Junsoo Kim, Hyungbo Shim, Frank Allgöwer. "A polynomial-based QCQP solver for encrypted optimization". *2025 IEEE 64th Conference on Decision and Control (CDC), IEEE Control Systems Society, Rio de Janeiro, Brazil, 2025*.
- Yong Joo Do, Deuksun Hong, Hyungbo Shim. "Distributed Q-Learning on Multi-Agent Markov Decision Process with Heterogeneous State Transition Probabilities". *2025 IEEE 64th Conference on Decision and Control (CDC), IEEE Control Systems Society, Rio de Janeiro, Brazil, 2025*.
- Hyungbo Shim, Jin Gyu Lee, Brian D. O. Anderson. "Adaptation of Parameters in Heterogeneous Multi-agent Systems". *2025 IEEE 64th Conference on Decision and Control (CDC), IEEE Control Systems Society, Rio de Janeiro, Brazil, 2025*.
- Gaeun Kim, Hyungbo Shim. "Determination of Bandwidth of Q-Filter in Disturbance Observers to Guarantee Transient and Steady State Performance Under Measurement Noise". *Institute of Control, Robotics and Systems 2025 25th International Conference on Control, Automation and Systems (ICCAS), Songdo Convensia, Incheon, Korea, 2025*.
- Sangwon Lee, Hyungbo Shim. "Actuator Position Estimation for Electro-Hydraulic Ride Height Control System Using EKF and a Reduced-Order Model Obtained via Singular Perturbation". *Institute of Control, Robotics and Systems 2025 25th International Conference on Control, Automation and Systems (ICCAS), Songdo Convensia, Incheon, Korea, 2025*.
- Hyungbo Shim, Daniel Liberzon. "Stability of linear systems with slow and fast time variation and switching: General case". *Nonlinear Analysis: Hybrid Systems, vol. 58, pp. 101626, 2025*.
- Chao Huanga, Siliang Yu, Hyungbo Shim, Brian D.O. Anderson. "Two algorithms for distributed mode computing based on blended dynamics approach". *Systems & Control Letters, vol. 202, iss. Systems & Control Letters, pp. 106082, 2025*.
- Aneel Tanwani, Hyungbo Shim, Andrew R. Teel. "Singularly Perturbed Hybrid Systems for Analysis of Networks With Frequently Switching Graphs". *IEEE Transactions on Automatic Control, vol. 70, iss. 7, pp. 4344-4359, 2025*.
- Soojeong Hyeon, Hyuntae Kim, Hyungbo Shim. "Data-driven displacement-based formation control with range-only measurements". *IEEE Access, vol. 13, pp. 115167-115177, 2025*.
- Sunghyun Koo, Jin Gyu Lee, Hyungbo Shim. "A Distributed Observer Accommodating a Broad Range of Intermittent Communication Scenarios". *IEEE Control Systems Letters, vol. 9, pp. 1682-1687, 2025*.
- Hyuntae Kim, Gyunghoon Park, Hyungbo Shim. "Robust disturbance rejection for uncertain linear system with time-varying exo-system: A disturbance observer approach". *Automatica, iss. 174, pp. 112100, 2025*.
- Junsoo Kim, Jin Gyu Lee, Henrik Sandberg, Karl H. Johansson. "Complexity Reduction for Resilient State Estimation of Uniformly Observable Nonlinear Systems". *IEEE TRANSACTIONS ON AUTOMATIC CONTROL, vol. 70, iss. 2, pp. 1267-1272, 2025*.
- Joowon Lee, Donggil Lee, Junsoo Kim, Hyungbo Shim. "Encrypted Dynamic Control Exploiting Limited Number of Multiplications and a Method Using RLWE-based Cryptosystem". *IEEE Transactions on Systems, Man, and Cybernetics: Systems, vol. 55, iss. 1, pp. 158-169, 2025*.

**2024**

- Chao Huang, Hyungbo Shim, Siliang Yu, Brian D. O. Anderson. "New Results on Finite Convergence Time Mode Consensus: a Summary". *2024 IEEE 63rd Conference on Decision and Control (CDC), IEEE, Milan, Italy, 2024*.
- Daniel Liberzon, Hyungbo Shim. "Stability of Nonlinear Systems with Slow and Fast Time Variation and Switching: The Common Equilibrium Case". *2024 IEEE 63rd Conference on Decision and Control (CDC), IEEE, Milan, Italy, 2024*.
- Jinwook Heo, Soojeong Hyeon, Hyungbo Shim, Jinsung Kim. "Fully Distributed EV Charging Scheduling for Load Flattening in V2G Systems". *2024 IEEE 63rd Conference on Decision and Control (CDC), IEEE, Milan, Italy, 2024*.
- Seungbeom Lee, Dongwoo Kim, Heewon Chung, Junsoo Kim, Hyungbo Shim. "Authentication of Multi-agent System with Verifiable Computation and Distributed Aggregation". *2024 IEEE 63rd Conference on Decision and Control (CDC), IEEE, Milan, Italy, 2024*.
- Hamin Chang, Donghyeon Song, Stephan Trenn, Hyungbo Shim. "Disturbance Observer with Switched Output Redefinition for Robust Stabilization of Non-Minimum Phase Linear Systems". *2024 IEEE 63rd Conference on Decision and Control (CDC), IEEE, Milan, Italy, 2024*.
- Hamin Chang, Donghyeon Song, Chanhwa Lee, Hyungbo Shim. "Robust Stability Condition and Simplified Design of Filter-embedded Disturbance Observer". *International Journal of Control, Automation, and Systems, vol. 22, pp. 3584-3594, 2024*.
- Yutian Wang, Tengfei Liu, Hyungbo Shim, George A. Rovithakis, Zhong-Ping Jiang. "A Lyapunov Characterization of Prescribed Performance Control Systems". *IEEE Transactions on Automatic Control, vol. 69, iss. 11, pp. 7917 - 7924, 2024*.
- Andrew Teel, Aneel Tanwani, Hyungbo Shim. "Stability Analysis of Nonlinear Systems Over Switching Networks Using Singularly Perturbed Hybrid Systems Framework". *26th International Symposium on Mathematical Theory of Networks and Systems, MTNS, cambridge,UK, 2024*.
- Hyuntae Kim, Hamin Chang, Hyungbo Shim. "Evaluating MR-GPR and MR-NN: An Exploration of Data-driven Control Methods for Nonlinear Systems". *International Journal of Control, Automation, and Systems, vol. 22, pp. 2934–2941, 2024*.
- Soojeong Hyeon, Iman Shames, Hyungbo Shim. "Multi-agent Target Position Estimation Using Bearing-only Measurments via Spatial Excitation". *2024 American Control Conference, pp. 548-553, IEEE, 2024*.
- Sunghyun Koo, Hyungbo Shim. "Reference-Tracking Sliding-Mode Control Robust to Mismatched Exogenous Disturbances". *2024 14th Asian Control Conference, pp. 848-853, 2024*.
- Deuksun Hong, Hyungbo Shim. "A Reinforcement Learning Approach for Safe Control Using Multi-Agent Q-Learning". *2024 14th Asian Control Conference, 2024*.
- Gyunghoon Park, Hyungbo Shim, Tomomichi Hagiwara. "On Existence of Uniformly Marginally Stable Zeros of Linear Sampled-data Systems and its Application to Stable Inversion-based Control". *IEEE Access, vol. 12, pp. 49826 - 49836, 2024*.
- Sihyun Ahn, Hyungbo Shim, Daniel Liberzon. "Semi-global practical stability of nonlinear systems with slow and fast time variation and switching in a separable form". *2024 IFAC Conference on Analysis and Control of Nonlinear Dynamics and Chaos, 2024*.
- Miao Guo, Bayu Jayawardhana, Jin Gyu Lee, Hyungbo Shim. "Maintaining and steering a formation in an unknown dynamic environment via a consistent distributed dynamic map". *International Journal of Robust and Nonlinear Control, vol. 34, iss. 13, pp. 8785-8801, 2024*.
- Yeongjun Jang, Hamin Chang, Heein Park, Hyungbo Shim. "Path Generating Inverse Gaussian Process Regression for Data-Driven Ultimate Boundedness Control of Nonlinear Systems". *IEEE Control Systems Letters, vol. 8, pp. 748 - 753, 2024*.
- Hyungbo Shim, Daniel Liberzon. "Further Results on Stability of Linear Systems with Slow and Fast Time Variation and Switching". *HSCC24: HYBRID SYSTEMS: COMPUTATION AND CONTROL 2024, HSCC, Hong Kong, 2024*.
- Taekyoo Kim, Donggil Lee, Hyungbo Shim. "Decentralized Design and Plug-and-Play Distributed Control for Linear Multi-Channel Systems". *IEEE Transactions on Automatic Control, vol. 69, iss. 5, pp. 2807 - 2822, 2024*.
- Hyungbo Shim. "How Does a Swarm Exhibit Emergent Behavior Through Synchronization?". *Journal of Institute of Control, Robotics and Systems, vol. 30, iss. 4, pp. 352, 2024*.
- Jin Gyu Lee, Cyrus Mostajeran, Graham Van Goffrier. "Node-Wise Monotone Barrier Coupling Law for Formation Control". *Entropy, vol. 26, iss. 2, pp. 134, 2024*.
- Namguk Kim, Hyungbo Shim. "Asymptotic output tracking in a class of non-minimum phase nonlinear systems via learning-based inversion". *International Journal of Robust and Nonlinear Control, vol. 34, iss. 1, pp. 240-269, 2024*.
- Jiyeon Nam, Soojeong Hyeon, Youngjun Joo, DongKi Noh, Hyungbo Shim. "Spectral Trade-off for Measurement Sparsification of Pose-graph SLAM". *IEEE Robotics and Automation Letters, vol. 9, iss. 1, pp. 723 - 730, 2024*.
- Jeong Woo Kim, Jin Gyu Lee, Donggil Lee, Hyungbo Shim. "A design method of distributed algorithms via discrete-time blended dynamics theorem". *Automatica, vol. 159, pp. 111371, 2024*.
- Jin Gyu Lee and Rodolphe Sepulchre\*. "Rapid and robust synchronization via weak synaptic coupling". *Automatica, 2024 (이진규 교수 개인 누리집 목록)*.

**2023**

- Joowon Lee, Donggil Lee, Seungbeom Lee, Junsoo Kim, Hyungbo Shim. "Conversion of Controllers to Have Integer State Matrix for Encrypted Control: Non-Minimal Order Approach". *2023 62nd IEEE Conference on Decision and Control (CDC), pp. 5091-5096, IEEE Control Systems Society, Marina Bay Sands, Singapore, 2023*.
- Donggil Lee, Junsoo Kim, Hyungbo Shim. "Distributed Resilient Observer: Blended Dynamics Theory Meets L1-Minimization Approach". *2023 62nd IEEE Conference on Decision and Control (CDC), IEEE IEEE Control Systems Society, Marina Bay Sands, Singapore, 2023*.
- Seungbeom Lee, Jinwook Heo, Soojeong Hyeon, Jiyeon Nam, Hyungbo Shim, Jinsung Kim. "User-friendly Vehicle-to-Grid Optimal Scheduling Problem and Distributed Implementation for Plug-and-play Operation". *International Conference on Control, Automation and Systems (ICCAS 2023), IEEE, Yeosu, Korea, Republic of, 2023*.
- Jeong Mo Seong, Donggil Lee, Hyungbo Shim. "Exponential Synchronization of Heterogeneous Multi-agent Systems via Linear-signum-type Diffusive Coupling: Blended Dynamics Approach". *International Conference on Control, Automation and Systems (ICCAS 2023), IEEE, Yeosu, Korea, Republic of, 2023*.
- Jin Gyu Lee, Thomas Berger, Stephan Trenn, Hyungbo Shim. "Edge-wise funnel output synchronization of heterogeneous agents with relative degree one". *Automatica, vol. 156, pp. 111204, 2023*.
- Hiroshi Ito, Hyungbo Shim. "A Toolkit for Globally Robust Observer-Based Feedback with Relaxed Characterization of iISS/ISS". *IEEE Transactions on Automatic Control, vol. 68, iss. 7, pp. 3858-3871, 2023*.
- Donggil Lee, Junsoo Kim, Hyungbo Shim. "Distributed Resilient Observer: Blended Dynamics Theory Meets ℓ1-Minimization Approach". *IEEE Control Systems Letters, vol. 7, pp. 2083 - 2088, 2023*.
- Hyuntae Kim, Hamin Chang, Hyungbo Shim. "Model Reference Gaussian Process Regression: Data-Driven Output Feedback Controller". *2023 American Control Conference (ACC), pp. 955-960, IEEE, San Diego, CA, USA, 2023*.
- Yongsoon Eun, Jaeho Lee, Hyungbo Shim. "Data-Driven Inverse of Linear Systems and Application to Disturbance Observer". *2023 American Control Conference (ACC), pp. 2806-2811, IEEE, San Diego, CA, USA, 2023*.
- Junsoo Kim, Hyungbo Shim, Kyoohyung Han. "Dynamic Controller that Operates over Homomorphically Encrypted Data for Infinite Time Horizon". *IEEE Transactions on Automatic Control, vol. 68, no. 2, pp. 660-672, 2023*.
- Jin Gyu Lee and Alessandro Astolfi\*. "Realization from moments: The linear case". *In Proc. of 62nd IEEE Conference on Decision and Control, 2023 (이진규 교수 개인 누리집 목록)*.

**2022**

- Hyungbo Shim, Daniel Liberzon. "Stability of linear systems with slow and fast time variation and switching". *Proc. of 2022 IEEE 61st Conference on Decision and Control (CDC), pp. 674-678, IEEE, Cancun, Mexico, 2022*.
- Jin Gyu Lee, Thiago B. Burghi, Rodolphe Sepulchre. "Open-loop contraction design". *Proc. of 2022 IEEE 61st Conference on Decision and Control (CDC), IEEE, Cancun, Mexico, 2022*.
- Jiyeon Nam, Jinwook Heo, Jeongwoo Kim, Hyungbo Shim, Jae Sung Bang, Jinsung Kim. "Initialization-free Algorithm for Discrete-time Dynamic Average Consensus and Its Application to Distributed Optimization". *Proc. of 22th International Conference on Control, Automation and Systems (ICCAS), pp. 424-429, IEEE, Busan, Korea, 2022*.
- Chulhong Kim, Junghyun Park, Taeyup Kim, Jee-Seong Kim, Jeongmo Seong, Hyungbo Shim, Hyoungho Ko, Dong-Il (Dan) Cho. "Development and evaluation of haltere-mimicking gyroscope for three-axis angular velocity sensing using a haltere-mimicking structure pair". *Bioinspiration & Biomimetics, vol. 18, no. 1, pp. 016003, 2022*.
- Junsoo Kim, Dongwoo Kim, Yongsoo Song, Hyungbo Shim, Henrik Sandberg, Karl H. Johansson. "Comparison of encrypted control approaches and tutorial on dynamic systems using Learning With Errors-based homomorphic encryption". *Annual Reviews in Control, vol. 54, pp. 200-218, 2022*.
- Jin Gyu Lee, Thiago B. Burghi. "Funnel control by induced contraction". *Proceedings of the 25th International Symposium on Mathematical Theory of Networks and Systems, pp. 248, IFAC-PapersOnLine, Bayreuth, Germany, 2022*.
- Jin Gyu Lee, Stephan Trenn, Hyungbo Shim. "Synchronization with prescribed transient behavior: Heterogeneous multi-agent systems under funnel coupling". *Automatica, vol. 141, pp. 110276, 2022*.
- Seungjoon Lee, Hyungbo Shim. "Blended dynamics approach to distributed optimization: Sum convexity and convergence rate". *Automatica, vol. 141, pp. 110290, 2022*.
- Hyungbo Shim, Juhoon Back, Yongsoon Eun, Gyunghoon Park, Jihan Kim. "Zero-dynamics Attack, Variations, and Countermeasures". *Hideaki Ishii; Quanyan Zhu (Ed.): Security and Resilience of Control Systems, vol. 489, Chapter 2, pp. 31–61, Springer Cham, 1, 2022*.
- Jin Gyu Lee and Junsoo Kim\*. "Mixed analog-digital method of designing a heterogeneous network with the desired collective behavior and rapid convergence". *Systems & Control Letters, 2022 (이진규 교수 개인 누리집 목록)*.

**2021**

- Junsoo Kim, Hyungbo Shim, Henrik Sandberg, Karl H. Johansson. "Method for Running Dynamic Systems Over Encrypted Data for Infinite Time Horizon without Bootstrapping and Re-Encryption". *Proc. of 2021 IEEE 60th Conference on Decision and Control, pp. 5614-5619, IEEE, Austin, Texas, USA, 2021*.
- Aneel Tawani, Hyungbo Shim. "Lyapunov Functions for Singularly Perturbed Hybrid Systems with Frequent Jump Dynamics". *Proc. of 2021 IEEE 60th Conference on Decision and Control, pp. 5382-5387, IEEE, Austin, Texas, USA, 2021*.
- Jeong Mo Seong, Jeong Woo Kim, Seungjoon Lee, Hyungbo Shim. "Distributed Dynamic Quantile Solver With Plug-and-Play Operation". *IEEE Access, vol. 9, pp. 165517-165525, 2021*.
- Jin Gyu Lee, Hyungbo Shim. "Design of Heterogeneous Multi-agent System for Distributed Computation". *Zhong-Ping Jiang; Christophe Prieur; Alessandro Astolfi (Ed.): Trends in Nonlinear and Adaptive Control, vol. 489, Chapter 4, pp. 83-108, Springer, Cham, Switzerland, 1, 2021*.
- Cyrus Mostajeran\*, Jin Gyu Lee, Graham Van Goffrier, and Rodolphe Sepulchre. "Target formation on the circle by monotone system design". *In Proc. of 60th IEEE Conference on Decision and Control, 2021 (이진규 교수 개인 누리집 목록)*.

## 국내 논문 (2021–2026)

누리집 List of Korean Publication 페이지의 2021–2026년 구역 73편이다. 제목·저자·학술지와 학회 이름은 누리집 표기 그대로이며, 누리집은 국내 학회 발표 항목 대부분에 학생 이름만 적는다.[^pubskr] 심형보 교수 개인 누리집 목록은 2025년의 「구조에 관한 사전지식을 활용하는 반매개변수화 커널 릿지 회귀」를 제어로봇시스템학회 논문지 논문으로 적는다.[^shimpubs]

**2026**

- 안시현. "리만 다양체 위의 다개체 시스템의 근사적 동기화". *제어로봇시스템학회(ICROS 2026), 2026*.
- 허진욱. "이벤트 트리거 통신을 갖는 이산시간 분산 알고리즘의 창발적 거동". *제어로봇시스템학회(ICROS 2026), 2026*.
- 장영준. "역모델 학습 기반의 강인 튜브 모델 예측 제어". *제어로봇시스템학회(ICROS 2026), 2026*.
- 도용주. "분포적 혼합동력학 이론". *제어로봇시스템학회(ICROS 2026), 2026*.
- 이상윤. "유향 간선별 양자화기를 활용한 분산 관측기의 동적 양자화 통신 설계". *제어로봇시스템학회(ICROS 2026), 2026*.
- 변형조. "분산 강인 연합 강화학습". *제어로봇시스템학회(ICROS 2026), 2026*.
- 정석호. "빠르게 진동하는 동역학을 갖는 이종 다개체 시스템의 실질적 동기화". *제어로봇시스템학회(ICROS 2026), 2026*.
- 문희민. "차량 기준 상태 추종을 위한 NCM 기반 강건 GP-MPPI 제어기". *제어로봇시스템학회(ICROS 2026), 2026*.
- 양윤정. "Willems의 Fundamental Lemma 속 지속 여기 차수의 필요충분성에 관한 재고". *제어로봇시스템학회(ICROS 2026), 2026*.
- 박희인. "비선형모멘트이론의 불변방정식의 해의 존재성 및 유일성에 대하여". *제어로봇시스템학회(ICROS 2026), 2026*.
- 홍득선. "상수 및 저주파 외란 억제를 위한 확장 데드존 관측기". *제어로봇시스템학회(ICROS 2026), 2026*.
- 장현영. "매개변수화된 지수적 안정 극한 주기 궤도의 입력-상태 안정성에 대하여". *제어로봇시스템학회(ICROS 2026), 2026*.

**2025**

- 구성현. "다단 다차원 적분기 시스템에 대한 통신 부하가 적은 분산 관측기". *제어로봇시스템학회(ICROS 2025), 2025*.
- 도용주. "확률적 동기화 기반 이산시간 혼합 동역학 정리". *제어로봇시스템학회(ICROS 2025), 2025*.
- 송동현. "휠더 연속 미분기 기반 외란 관측기와 2관성계 시스템에의 적용". *제어로봇시스템학회(ICROS 2025), 2025*.
- 홍득선. "외란에 강인한 비선형 관측기의 필요성 고찰 및 강화학습 기반 설계". *제어로봇시스템학회(ICROS 2025), 2025*.
- 정석호. "제어 장벽함수 기반 최적화를 통한 다개체 시스템의 균형 행동". *제어로봇시스템학회(ICROS 2025), 2025*.
- 허진욱. "가중치 불균형 유향그래프에서의 강인한 동적 평균 합의". *제어로봇시스템학회(ICROS 2025), 2025*.
- 김가은. "급격한 외란 변화 및 잡음에 대응하는 외란 관측기 파라미터 결정 로직". *제어로봇시스템학회(ICROS 2025), 2025*.
- 장현영. "데이터 기반 보조 제어를 활용한 미지의 비선형 입력 아핀 시스템의 실시간 모델 예측 제어". *제어로봇시스템학회(ICROS 2025), 2025*.
- 변형조. "매개변수화된 오목 메이저란트를 사용한 Q-러닝과 액터-크리틱 관점에서의 해석". *제어로봇시스템학회(ICROS 2025), 2025*.
- 박희인, 장하민, 장영준, 장현영, 심형보. "구조에 관한 사전지식을 활용하는 반매개변수화 커널 릿지 회귀". *제어로봇시스템학회(ICROS 2025), 2025*.
- 도용주. "독립 항등 분포 및 마르코프 과정 기반 스위칭 시스템에서의 혼합 동역학 정리". *정보 및 제어 학술대회(CICS 2025), pp. 231-232, 2025*.
- 문희민. "자율주행차량의 실시간 횡방향 제어를 위한 데이터 기반 MR-GPR". *정보 및 제어 학술대회(CICS 2025), pp. 314-315, 2025*.
- 양윤정. "Willems의 Fundamental Lemma 속 지속 여기 조건의 보수성에 대한 신호발생기 관점의 재고". *정보 및 제어 학술대회(CICS 2025), pp. 312-313, 2025*.

**2024**

- 변형조. "강화학습 기반 선형 피드백 제어기 이득 선택에서 안정적 학습을 위한 지속적 행동". *제어, 로봇 시스템 학회 논문지 (Journal of Institute of Control, Robotics and Systems), 30권 9호, pp. 965-972, 2024*.
- 박희인, 장하민, 장영준. "사후 평균을 활용한 가우스 과정 회귀의 오차 한계 근사". *항공우주학회 춘계학술대회, 2024*.
- 장하민. "필터가 삽입된 외란 관측기의 안정도 해석". *제어로봇시스템학회(ICROS 2024), 2024*.
- 허진욱. "가중 유향그래프에서 네트워크 참여자를 식별하는 분산 알고리즘". *제어로봇시스템학회(ICROS 2024), 2024*.
- 송동현. "외란 관측기의 공칭 성능 복원 능력에 대한 오차 동역학을 통한 관찰". *제어로봇시스템학회(ICROS 2024), 2024*.
- 김가은. "강인 추종 제어를 위한 명령 주입 외란 관측기". *제어로봇시스템학회(ICROS 2024), 2024*.
- 변형조. "강화학습 기반 제어 이득 선택에서 안정적 학습을 위한 지속적 행동". *제어로봇시스템학회(ICROS 2024), 2024*.
- 이주원. "암호화된 데이터에 대한 선형 최소제곱법: 부트스트래핑을 사용하지 않는 동형암호 알고리즘". *제어로봇시스템학회(ICROS 2024), 2024*.
- 장영준. "절단된 완전최소자승법 기반 데이터 주도 출력궤환 예측 제어". *제어로봇시스템학회(ICROS 2024), 2024*.
- 홍득선. "비선형 동역학 시스템의 지역적 관측 가능성을 이용한 강화학습 입력 설계". *제어로봇시스템학회(ICROS 2024), 2024*.
- 박희인. "데이터의 추가 및 제거에 따른 역제곱 커널 가우스 과정 회귀 사후분산의 변화 분석". *제어로봇시스템학회(ICROS 2024), 2024*.
- 도용주. "상태전이확률이 다른 다개체 마르코프 결정과정과 분산 Q-러닝 알고리즘". *정보 및 제어 학술대회(CICS 2024), pp. 123-124, 2024*.
- 장현영. "입력 및 출력 측정 잡음에 강인한 커널 기반 회귀". *정보 및 제어 학술대회(CICS 2024), pp. 126-127, 2024*.

**2023**

- 이주원. "제어기의 입출력 표현을 활용해 Ring-LWE 기반 암호 체계로 암호화된 제어 시스템". *제어, 로봇 시스템 학회 논문지 (Journal of Institute of Control, Robotics and Systems), 29권 1호, pp. 1-6, 2023*.
- 현수정. "베어링 측정을 활용한 다개체 시스템의 다중 표적 선회를 위한 중심 위치 추정 알고리즘 개발". *제어로봇시스템학회(ICROS 2023), 2023*.
- 송동현. "고주파 출력 잡음에 강인한 낮은 차수의 이득을 가지는 선형 외란 관측기". *제어로봇시스템학회(ICROS 2023), 2023*.
- 이주원. "입출력 데이터만을 사용한 데이터 기반 LQR 설계". *제어로봇시스템학회(ICROS 2023), 2023*.
- 장영준. "측정 잡음에 강인한 완전최소제곱법 기반 데이터 주도 출력 궤환 예측 제어 기법". *제어로봇시스템학회(ICROS 2023), 2023*.
- 박희인. "Willems 의 Behavioral Approach 에 대한 소개". *제어로봇시스템학회(ICROS 2023), 2023*.
- 허진욱. "비례-적분형 다단 결합을 적용한 이산시간 이종 다개체 시스템의 동기화". *제어로봇시스템학회(ICROS 2023), 2023*.
- 홍득선. "PGNN 기반 피드포워드 제어기법의 한계". *제어로봇시스템학회(ICROS 2023), 2023*.
- 이승범. "다개체 시스템의 인증을 위한 방향 3개체 선형 시스템의 계산검증". *제어로봇시스템학회(ICROS 2023), 2023*.
- 안시현. "비선형 제어기 암호화를 위한 다항식 제어기의 양자화 오차 분석". *정보 및 제어 학술대회(CICS 2023), pp. 142-143, 2023*.
- 변형조. "혼합 동역학을 사용한 분산형 네트워크 크기 추정에서 오차 페널티 가중치를 통한 신규 개체 참여에서의 강인성 향상". *정보 및 제어 학술대회(CICS 2023), pp. 180-181, 2023*.
- 장하민. "종방향 미사일 동역학의 데이터 기반 온라인 MR-GPR 제어". *한국항공우주학회 2023 추계학술대회, 2023*.

**2022**

- 현수정. "지역 좌표계의 위치 정보를 활용한 3차원에서의 leader-follower 대형 제어". *제어로봇시스템학회(ICROS 2022), 2022*.
- 장하민. "측정 잡음이 포함된 입출력 데이터를 이용한 단일 입출력 선형 시스템의 식별". *제어로봇시스템학회(ICROS 2022), 2022*.
- 이주원. "Ring-LWE 기반 암호 체계를 활용한 단일 입출력 제어기의 암호화". *제어로봇시스템학회(ICROS 2022), 2022*.
- 이승범. "출력 중심의 검증체계를 통한 선형제어기의 효율적인 인증". *제어로봇시스템학회(ICROS 2022), 2022*.
- 홍득선. "국소적 시스템 식별을 통한 SINDy 기반 모델예측제어기의 계산 경량화". *정보 및 제어 학술대회(CICS 2022), pp. 259-260, 2022*.
- 허진욱, 김정우, 방재성, 김진성. "부하 평탄화를 위한 완전분산 전기차 충전 스케줄링: Blended Dynamics 접근법". *정보 및 제어 학술대회(CICS 2022), pp. 215-216, 2022*.
- 송동현. "이득 스케줄러의 성긴 다항식 근사를 이용한 3-루프 제어기 동형암호화". *정보 및 제어 학술대회(CICS 2022), pp. 213-214, 2022*.
- 장영준, 이동길. "데이터 주도 출력 궤환 예측 제어의 측정 잡음에 대한 강인성 해석". *정보 및 제어 학술대회(CICS 2022), pp. 211-212, 2022*.
- 박희인. "실시간 가우시안 프로세스 회귀의 미사일 공력계수 식별 응용 가능성". *한국항공우주학회 2022 추계학술대회, 2022*.

**2021**

- 이승범, 이주원, 심형보. "사이버 물리 시스템의 보안을 위한 동형암호 소개". *제어, 로봇 시스템 학회 논문지 (Journal of Institute of Control, Robotics and Systems), 27권 3호, pp. 177-184, 2021*.
- 심형보, 김정우, 박주영. "강화학습 기반 강인 제어를 위한 과거 입출력 정보 필요성 탐구". *전기학회논문지, 70권, 12호, pp. 1953-1957, 2021*.
- 남지연. "샘플된 데이터 기반 연속시간 선형 시불변 시스템의 시스템 식별". *제어로봇시스템학회 학술대회(ICROS2021), 2021*.
- 현수정. "불확실한 영동역학을 갖는 시스템에 대한 외란 관측기를 활용한 피드스루 보상기 설계법". *제어로봇시스템학회 학술대회(ICROS2021), 2021*.
- 이주원. "궤환 선형화 기법을 활용한 비선형 제어기 동형암호화". *제어로봇시스템학회 학술대회(ICROS2021), 2021*.
- 성정모. "1.5-IQR 이상치 선정 방법에 근거한 절사평균의 분산적 추정". *제어로봇시스템학회 학술대회(ICROS2021), 2021*.
- 이승범. "동적 시스템의 인증체계 도입에 필요한 조건". *제어로봇시스템학회 학술대회(ICROS2021), 2021*.
- 이동길. "시스템의 입력과 출력 데이터를 이용한 데이터 주도 기반의 최적제어". *제어로봇시스템학회 학술대회(ICROS2021), 2021*.
- 장하민. "로봇 매니퓰레이터를 위한 비선형 외란 관측기가 포함된 폐루프 시스템의 안정도 해석". *제어로봇시스템학회 학술대회(ICROS2021), 2021*.
- 김정우. "초기화 과정없이 시변 네트워크의 크기를 추정하는 이산시간 분산 알고리즘의 개발". *제어로봇시스템학회 학술대회(ICROS2021), 2021*.
- 장하민, 이동길. "가우시안 프로세스를 활용한 미사일 동역학의 모델링 및 모델 예측 제어". *한국군사과학기술학회 종합학술대회, pp. 1420-1421, 2021*.
- 김정우, 성정모. "Proximal Policy Optimization 알고리즘을 이용한 Skid-To-Turn 미사일의 종방향 모델 제어". *한국군사과학기술학회 종합학술대회, pp. 1416-1417, 2021*.
- 김현태, 남지연. "실제 시스템에서 외란 관측기를 통한 강화 학습의 성능 향상". *한국군사과학기술학회 종합학술대회, pp. 1418-1419, 2021*.
- 김정우, 이동길, 김현태, 성정모, 장하민, 강형관, 이영준, 심형보, 김유단, 박종호. "데이터 기반 모델-프리 조종 기법 연구: Proximal Policy Optimization을 이용한 Skid-To-Turn 유도탄의 종방향 모델 제어". *한국항공우주학회, pp. 151-153, 2021*.

## 과제

누리집 Funded Projects 페이지의 Selected On-going Projects 4건과, Selected Past Projects 16건 가운데 기간이 2021년 10월 이후까지 이어진 3건, 모두 7건이다. 역할(PI, Co-PI), 과제 이름, 지원 기관, 기간은 누리집 표기 그대로다. 「Artificial Intelligence based Flight Control Research Laboratory」는 2020년 10월에 시작해 기간 끝을 적지 않은 진행 과제다.[^projects]

- 연결된 동적 시스템에 관한 제어 이론 심화 연구 (역할 PI; 지원 National Research Foundation of Korea; 기간 2022/9/1 ~ )
- Research of distributed optimization for large-scale V2G operation (역할 PI; 지원 Hyundai Motors; 기간 2022/5/25 ~ )
- Research on Learning Methods for Improving Robustness of Data-driven Controller against Model Uncertainty (역할 PI; 지원 Hyundai Motors; 기간 2022/4/18 ~ )
- Artificial Intelligence based Flight Control Research Laboratory (역할 Co-PI; 지원 Agency for Defense Development; 기간 2020/10 ~ )
- Development of pose-graph optimization and node simplification algorithm for multi-agent systems (역할 Co-PI; 지원 LG electronics; 기간 2022/5/1 ~ 2022/12/31, Co-PI: Youngjun Joo at Sookmyung Women’s Univ.)
- Research on Control Theory for Connected Cyber-Physical & Human System (역할 PI; 지원 National Research Foundation of Korea; 기간 2017/9/1 ~ 2022/8/31)
- 실시간 자율 복원 사이버물리 시스템 기초 연구 (Resilient Cyber-Physical Systems) (역할 Co-PI; 지원 DGIST; 기간 2016 ~ 2022/2/28)

## 수상

누리집 News 분류의 수상·선정 글 가운데 2021년 10월 22일–2026년 10월 22일에 올라온 6건이다. 날짜와 제목은 글 표기 그대로다.[^newscat] 교수 개인의 영예는 위 「교수와 전문 분야」에 적었다.

- February 15, 2026 · Congratulations! Prof. Hyungbo Shim Elected as 2026 IEEE Fellow
- July 23, 2024 · 구성현 학생, ASCC 2024 “Best Paper Award” 수상
- July 17, 2024 · 변형조 학생, ICROS 2024 최우수논문상 수상
- January 29, 2024 · 심형보 교수, 한국과학기술한림원 2024년 정회원 선출
- July 21, 2023 · 송동현 학생, ICROS 2023 우수논문상 수상
- January 20, 2022 · 인턴 김예린 학생, 학부생 논문 경진대회 장려상 수상

## 소식

누리집 News·Research·Event 분류 글 가운데 2021년 10월 22일–2026년 10월 22일에 올라온 연구 소식 36건이다. 날짜와 제목은 글 표기 그대로이고, 방문자 세미나 글은 글에 적힌 세미나 제목이나 강연 내용을 괄호에 옮겼다.[^newscat] 2021년 11월 29일 글의 SNU-DGIST-GIST 합동 워크숍은 글에 따르면 2021년 9월에 열렸다.[^joint]

- September 29, 2026 · Yeongjun Jang presented recent result at SICE-FES 2026
- September 29, 2026 · International Workshop on Sparse and Geometric Representations in Systems and Control @ IFAC 2026
- September 29, 2026 · Alternative Representations for Control (Pre-Congress Workshop) @ IFAC 2026
- September 22, 2026 · Prof. Robert Mahony visited CDSL (세미나 “Equivariant Systems Theory”)
- September 22, 2026 · Prof. Kaoru Teranishi visited CDSL (세미나 “Secure Two-Party Matrix Multiplication from Lattices and Its Application to Encrypted Control”)
- September 17, 2026 · New Paper on Encrypted Control and Anomaly Detection Accepted in IEEE TCNS
- February 15, 2026 · BK21 Zoom Seminar Series on Control Theory Underway at CDSL (1/23-3/5)
- August 28, 2025 · Prof. Shinkyu Park visited CDSL (세미나 “Learning Models in Large-Population Games”)
- August 28, 2025 · Prof. Brian D. O. Anderson visited CDSL (세미나 “Reverse Time Diffusions and Applications”)
- August 28, 2025 · Dr. Namhoon Cho visited CDSL (세미나 ‘DDH: Data-Driven Hamiltonian for Safe Set Construction and Beyond’)
- August 28, 2025 · Dr. G. Q. Bao Tran visited CDSL (세미나 ‘Gluing KKL Observer for Hybrid Systems with Unknown Jump Times’)
- April 15, 2025 · Video Lecture: Introduction to Blended Dynamics Theorems
- April 15, 2025 · Video Lecture: History of Consensus
- February 4, 2025 · Yongjae Oh visited CDSL (세미나 “Stochastic Thermodynamics: Implementing Energy and Entropy into Dynamical Systems.”)
- February 4, 2025 · Prof. Quanyan Zhu visited CDSL (세미나 ‘The Role of Information in Dynamic Games and Multi-Agent Learning’)
- February 4, 2025 · Dr. Rijad Alisic visited CDSL (세미나 ‘Understanding the Learning Attacker in Cyber-Physical Systems’)
- November 22, 2024 · 2024 BK21/CDSL GoGE Workshop
- August 13, 2024 · Prof. Toru Namerikawa visited CDSL (세미나 ‘Distributed Dynamic Pricing in Electricity Market with Information Privacy’)
- July 15, 2024 · Prof. Wen-Hua Chen visited CDSL (세미나 “Disturbance Observer-Based Control (DOBC) and Recent Development”)
- May 7, 2024 · Prof. Sutrisno visited CDSL (세미나 ‘Singular Switched Systems in Discrete Time: Recent Solution Theory and Open Problems’)
- May 7, 2024 · PhD students affiliated with WASP visited CDSL
- February 19, 2024 · e-TEC Talks @ SNU Winter 2024 : Control and Automation Session
- January 17, 2024 · Dr. Jinrae Kim visited CDSL (세미나 “Universal convex approximation for learning objective function in amortized optimization”)
- December 20, 2023 · Prof. Christian Grussler visited CDSL (총양성(total positivity) 연구 소개)
- October 31, 2023 · 2023 BK21/CDSL GoGE Workshop
- August 10, 2023 · 5-Day Lectures on Robust Control based on Parameter Approach and Modern PID Control
- July 3, 2023 · Prof. Nak-seung Patrick Hyun visited CDSL (세미나 “Autonomous Control of Extreme Behaviors in Bio-Inspired Robotics”)
- June 28, 2023 · Prof. Daniel Liberzon visited CDSL (“Nonlinear control with limited information” 등 세 강연)
- January 6, 2023 · Prof. Rolf Findeisen visited CDSL (세미나 “Fusing Machine Learning and Predictive Control for the Safe and Optimal Operation of Autonomous Systems“)
- December 5, 2022 · 현대자동차 지능 제어 공동연구실 워크샵 개최
- December 4, 2022 · 2022 GoGE Workshop on Optimization, Decision and AI
- October 28, 2022 · Article published: Comparison of encrypted control approaches and tutorial on dynamic systems using Learning With Errors-based homomorphic encryption
- August 30, 2022 · Prof. Rasoul Etesami visited CDSL (세미나 “Duality and Stability in Multiagent State-Dependent Network Dynamics”)
- May 18, 2022 · 현대자동차·기아, 지능 제어 공동연구실 설립
- November 30, 2021 · GoGE Workshop on Optimization, Decision, and AI
- November 29, 2021 · The 1st SNU-DGIST-GIST Joint Workshop on Control Systems

## 연락과 위치

- 연구실: 08826 서울특별시 관악구 관악로 1 서울대학교 133동(자동화시스템공동연구소) 307호 제어 및 동역학 연구실. 학생 공간은 133동 304, 305, 306, 307호다.[^contact]
- 전화: +82 2 880-9053(학생 공간), 팩스 +82 2 871-2527[^contact]
- 심형보 교수: hshim@snu.ac.kr, Building 133 Room 302 / Building 302 Room 530, +82 2 880 6486 / +82 2 880 1745[^people] (학부 교수 상세 표기는 301동 709호, 02-880-1745[^eceshim])
- 이진규 교수: jingyu.lee@snu.ac.kr, Building 302 Room 630, +82 2 880 1728[^people][^ecelee]
[^about]: 연구실 누리집 About 페이지 <https://post.cdsl.kr/about> (History, Research Interest 칸, 2026-10-25 열람)
[^overview]: 연구실 누리집 Research Overview 페이지 <https://post.cdsl.kr/research-overview> (2026-10-25 열람)
[^people]: 연구실 누리집 People 페이지 <https://post.cdsl.kr/people> (Supervisor, Student 칸, 2026-10-25 열람)
[^alumni]: 연구실 누리집 Alumni 페이지 <https://post.cdsl.kr/alumni> (Recent Ph.D Alumni, Recent Master Alumni, Recent Post-doc Alumni, All Alumni List 칸, 2026-10-25 열람)
[^visitors]: 연구실 누리집 「Former long-term visitors to CDSL」 <https://post.cdsl.kr/archives/246> (2026-10-25 열람)
[^contact]: 연구실 누리집 Location & Contact 페이지 <https://post.cdsl.kr/contact-us> (2026-10-25 열람)
[^pubs]: 연구실 누리집 List of English Publication 페이지 1–2쪽 <https://post.cdsl.kr/publication-list>, <https://post.cdsl.kr/publication-list?limit=2&tgid=&yr=&type=&usr=&auth=&tsr=> (2021–2026년 연도 구역, 저자 순서와 게시 초록, 2026-10-25 열람)
[^pubskr]: 연구실 누리집 List of Korean Publication 페이지 <https://post.cdsl.kr/publication-list-kr> (Publication in 2021–2026 구역, 2026-10-25 열람)
[^projects]: 연구실 누리집 Funded Projects 페이지 <https://post.cdsl.kr/funded-projects> (Selected On-going Projects, Selected Past Projects 칸, 2026-10-25 열람)
[^newscat]: 연구실 누리집 News 분류 1–5쪽 <https://post.cdsl.kr/archives/category/news>, Research 분류 <https://post.cdsl.kr/archives/category/research>, Event 분류 1–4쪽 <https://post.cdsl.kr/archives/category/event>와 각 글 (2026-10-25 열람)
[^mas]: 연구실 누리집 「Research on Multi-agent System (blended dynamics approach)」 <https://post.cdsl.kr/archives/3672> (2026-10-25 열람)
[^maskr]: 연구실 누리집 「다개체 시스템 연구 소개」 <https://post.cdsl.kr/archives/30> (2026-10-25 열람)
[^dob]: 연구실 누리집 「Research on Disturbance Observer」 <https://post.cdsl.kr/archives/69> (Research Timeline 1–16, Selected Experiments 칸, 2026-10-25 열람)
[^dobkr]: 연구실 누리집 「외란 관측기 연구 소개」 <https://post.cdsl.kr/archives/467> (2026-10-25 열람)
[^cps]: 연구실 누리집 「Research on Security of Cyber-Physical System」 <https://post.cdsl.kr/archives/71> (2026-10-25 열람)
[^enc]: 연구실 누리집 「제어기 암호화 연구 소개」 <https://post.cdsl.kr/archives/949> (2026-10-25 열람)
[^hybrid]: 연구실 누리집 「하이브리드 시스템 연구 소개」 <https://post.cdsl.kr/archives/1250> (2026-10-25 열람)
[^lee24]: 연구실 누리집 소식 「이진규 박사의 교원 임용 소식」(2024년 7월 27일) <https://post.cdsl.kr/archives/5357> (2026-10-25 열람)
[^fellow]: 연구실 누리집 소식 「Congratulations! Prof. Hyungbo Shim Elected as 2026 IEEE Fellow」(2026년 2월 15일) <https://post.cdsl.kr/archives/5902> (2026-10-25 열람)
[^kast]: 연구실 누리집 소식 「심형보 교수, 한국과학기술한림원 2024년 정회원 선출」(2024년 1월 29일) <https://post.cdsl.kr/archives/5108> (2026-10-25 열람)
[^hicl]: 연구실 누리집 소식 「현대자동차·기아, 지능 제어 공동연구실 설립」(2022년 5월 18일) <https://post.cdsl.kr/archives/4566> (2026-10-25 열람)
[^hiclws]: 연구실 누리집 소식 「현대자동차 지능 제어 공동연구실 워크샵 개최」(2022년 12월 5일) <https://post.cdsl.kr/archives/4733> (2026-10-25 열람)
[^arc]: 연구실 누리집 소식 「Alternative Representations for Control (Pre-Congress Workshop) @ IFAC 2026」(2026년 9월 29일) <https://post.cdsl.kr/archives/6129> (2026-10-25 열람)
[^teranishi]: 연구실 누리집 소식 「Prof. Kaoru Teranishi visited CDSL」(2026년 9월 22일) <https://post.cdsl.kr/archives/6104> (2026-10-25 열람)
[^tcnspost]: 연구실 누리집 소식 「New Paper on Encrypted Control and Anomaly Detection Accepted in IEEE TCNS」(2026년 9월 17일) <https://post.cdsl.kr/archives/6098> (2026-10-25 열람)
[^grussler]: 연구실 누리집 소식 「Prof. Christian Grussler visited CDSL」(2023년 12월 20일) <https://post.cdsl.kr/archives/5101> (2026-10-25 열람)
[^etec]: 연구실 누리집 소식 「e-TEC Talks @ SNU Winter 2024 : Control and Automation Session」(2024년 2월 19일) <https://post.cdsl.kr/archives/5145> (2026-10-25 열람)
[^tran]: 연구실 누리집 소식 「Dr. G. Q. Bao Tran visited CDSL」(2025년 8월 28일) <https://post.cdsl.kr/archives/5666> (2026-10-25 열람)
[^bk21zoom]: 연구실 누리집 소식 「BK21 Zoom Seminar Series on Control Theory Underway at CDSL (1/23-3/5)」(2026년 2월 15일) <https://post.cdsl.kr/archives/5893> (2026-10-25 열람)
[^joint]: 연구실 누리집 소식 「The 1st SNU-DGIST-GIST Joint Workshop on Control Systems」(2021년 11월 29일) <https://post.cdsl.kr/archives/4480> (2026-10-25 열람)
[^shimhome]: 심형보 교수 개인 누리집 첫 화면(about) <https://hyungbo.github.io/> (직함, 소개, Research Interests 칸, 2026-10-25 열람)
[^shimcv]: 심형보 교수 개인 누리집 cv 페이지 <https://hyungbo.github.io/cv/> (Education and Career, Honor and Awards, Activities 칸, 2026-10-25 열람)
[^shimpubs]: 심형보 교수 개인 누리집 publications 페이지 <https://hyungbo.github.io/publications/> (By Year, By Topic 보기, 2026-10-25 열람)
[^leehome]: 이진규 교수 개인 누리집 Home 페이지 <https://jingyulee92.wordpress.com/> (About, Education and Career, Honors and Awards, Activities 칸, 2026-10-25 열람)
[^leepubs]: 이진규 교수 개인 누리집 Publications 페이지 <https://jingyulee92.wordpress.com/%ec%a0%95%eb%b3%b4/> (2026-10-25 열람)
[^leeri]: 이진규 교수 개인 누리집 Research Interests 페이지 <https://jingyulee92.wordpress.com/research-interests/> (2026-10-25 열람)
[^ecelab]: 서울대학교 전기·정보공학부 연구실 목록 <https://ece.snu.ac.kr/research-faculty/research/lab> (제어공학 연구그룹, 지능 및 로봇 공학 연구그룹, 2026-10-25 열람)
[^ecelab62]: 서울대학교 전기·정보공학부 연구실 상세(제어 및 동역학 연구실, 심형보 교수) <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=62> (2026-10-25 열람)
[^ecelab146]: 서울대학교 전기·정보공학부 연구실 상세(제어 및 동역학 연구실, 이진규 교수) <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=146> (2026-10-25 열람)
[^ecefac]: 서울대학교 전기·정보공학부 전임교수 목록 <https://ece.snu.ac.kr/research-faculty/faculty/full-time> (2026-10-25 열람)
[^eceshim]: 서울대학교 전기·정보공학부 교수 상세(심형보) <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p060> (2026-10-25 열람)
[^ecelee]: 서울대학교 전기·정보공학부 교수 상세(이진규) <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p904> (2026-10-25 열람)
[^p1]: H. Kim, G. Park, H. Shim, Automatica 174, 112100 (2025). <https://doi.org/10.1016/j.automatica.2024.112100> 초록 기준(연구실 논문 목록 게시 초록).
[^p2]: D. Song, H. Kim, H. Shim, International Journal of Control, Automation, and Systems 24, 1297-1307 (온라인 2026-04-22). <https://doi.org/10.1007/s12555-026-00072-z> 초록 기준(연구실 논문 목록 게시 초록).
[^p3]: J. W. Kim, J. G. Lee, D. Lee, H. Shim, Automatica 159, 111371 (2024). <https://doi.org/10.1016/j.automatica.2023.111371> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: S. Koo, J. G. Lee, H. Shim, IEEE Control Systems Letters 9, 1682-1687 (2025). <https://doi.org/10.1109/lcsys.2025.3583672> 초록 기준(연구실 논문 목록 게시 초록).
[^p5]: Y. Jang 외, H. Shim, IEEE Transactions on Control of Network Systems 13, 1715-1727 (2026). <https://doi.org/10.1109/tcns.2026.3698371> 초록 기준(연구실 논문 목록 게시 초록).
[^p6]: J. Lee, D. Lee, J. Kim, H. Shim, IEEE Transactions on Systems, Man, and Cybernetics: Systems 55, 158-169 (2025). <https://doi.org/10.1109/tsmc.2024.3452007> 초록 기준(연구실 논문 목록 게시 초록).
[^p7]: Y. Jang, H. Chang, H. Park, H. Shim, IEEE Control Systems Letters 8, 748-753 (2024). <https://doi.org/10.1109/lcsys.2024.3403525> 초록 기준(연구실 논문 목록 게시 초록).
[^p8]: D. Song, H. Jang, G. Scarciotti, J. G. Lee, Systems & Control Letters 217, 106559 (2026). <https://doi.org/10.1016/j.sysconle.2026.106559> 초록 기준(연구실 논문 목록 게시 초록).

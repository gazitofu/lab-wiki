# Wearable and Interactive Technology Lab (WIT Lab)

**KAIST 전기및전자공학부 · 이안 오클리(Ian Oakley) 교수**

- 분야: 스마트워치·이어버드 같은 착용형 기기의 새 입력 방법, 착용형 기기와 머리 착용형 디스플레이의 생체·행동 인증, 머리 착용형 디스플레이의 시선·머리 입력과 시선 추적 도구, 걸으며 쓰는 증강현실과 자율주행차-보행자 인터페이스
- 대분야: 컴퓨팅·AI
- 태그: 인간–컴퓨터 상호작용[^home][^ee][^p1], 가상·증강현실[^ee][^p5][^p7], 음향·오디오 AI[^p1][^p3], 모바일·유비쿼터스 센싱[^p1][^p2]
- 홈페이지: <https://wit.kaist.ac.kr/>
- 근거와 출처: [WIT Lab 근거 페이지](wit-sources.md)

> 스마트워치, 이어버드, 스마트 글라스, 가상·증강현실 헤드셋처럼 몸에 쓰는 기기를 사람이 더 쉽고 정확하고 안전하게 쓰도록, 새 입력 방법과 사용자 인증 방법을 만들고 사람을 대상으로 한 실험으로 평가하는 인간–컴퓨터 상호작용 연구실이다.[^home][^research][^p1][^p3][^p7]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 이안 오클리(Ian Oakley) 교수가 이끄는 Wearable and Interactive Technology Lab(WIT Lab)이다. 누리집은 연구실이 몸에 착용하거나 손으로 만지는 상호작용형 컴퓨팅 시스템을 설계·개발·평가한다고 소개하고, 디자인 관점과 컴퓨터과학 기술, 심리학 방법을 함께 써서 다음 세대의 인간–컴퓨터 인터페이스를 구상하고 만들고 연구한다고 적는다.[^home] 학부 교수 소개는 교수의 주요 연구를 인간–컴퓨터 상호작용(HCI)과 증강·가상현실로 적는다.[^ee] 첫 화면 소식에 따르면 연구실은 UNIST에 있다가 2023년 KAIST로 옮겨 왔다.[^home]

연구 페이지에 따르면 연구실은 모바일·착용형·내장형 기기를 위한 상호작용 시스템과 상호작용 기법(사용자가 기기에 뜻을 전하는 입력 방식과 그 동작 규칙)을 설계한다. 이런 기기는 작고, 손에 쥐거나 몸에 걸치며, 곳곳에 있고, 사람이 움직이거나 다른 일에 정신이 팔려 있거나 여러 일을 함께 할 때 쓰인다는 점을 설계에 반영한다. 설계는 사람의 마음과 몸이 할 수 있는 일을 세밀하게 이해하는 실험 연구에 바탕을 두고, 디지털 제작, 하드웨어·소프트웨어 시제품, 계산 최적화와 딥러닝 같은 분석 기법을 함께 써서 만든다. 지금 중심은 터치·시선·움직임이라는 입력 방식을 스마트워치와 스마트 글라스 같은 새 기기에, 그리고 증강·가상현실 같은 착용형 사용 상황에 적용하는 일이다.[^research]

대표 논문으로 보면 연구는 네 갈래다. 첫째는 착용형 기기의 작은 화면과 몸체를 넘어서는 입력이다. 대표 논문 1은 개조하지 않은 일반 스마트워치에서 소나(sonar, 소리를 내보내고 되돌아온 소리로 물체의 위치를 재는 방법)로 시계 주변의 손가락을 추적하고, 대표 논문 2는 자력계를 넣은 이어버드와 손가락에 낀 자석 반지로 어느 손가락으로 만졌는지를 구분한다.[^p1][^p2] 둘째는 착용형 기기의 사용자 인증이다. 대표 논문 3은 두개골을 지나며 바뀐 소리로 스마트 글라스 사용자를, 대표 논문 4는 손 관절의 움직임으로 머리 착용형 디스플레이(HMD, 머리에 쓰고 눈앞의 화면을 보는 가상·증강현실 기기) 사용자를 알아본다.[^p3][^p4] 셋째는 HMD에서 시선과 머리로 하는 입력이다. 대표 논문 5는 시선을 손·머리 입력과 묶어 화면을 확대하고 이동하는 기법을, 대표 논문 6은 여러 HMD에 외부 시선 추적기를 붙여 쓰는 공개 도구를 만들었다.[^p5][^p6] 넷째는 걷거나 달리면서 하는 상호작용이다. 대표 논문 7은 걸으면서 머리로 커서를 움직여 고르는 입력을 안정시키고, 대표 논문 8은 달리는 사람에게 자율주행차의 양보 의도를 알리는 인터페이스를 비교했다.[^p7][^p8] 최근 논문 목록에는 확장현실(XR, 가상현실과 증강현실을 함께 이르는 말)에서 만화를 보는 화면 배치, 가상현실 산업 훈련에서 무게를 흉내 내는 의사 촉각(pseudo-haptics), 손을 쓰지 않고 가상현실 게임을 하는 입력에 관한 논문도 있다.[^cr]

## 주요 연구 주제

### 1. 스마트워치·이어버드에서 하는 새 입력

스마트워치는 화면이 작아 입력 방식이 제한되고, 무선 이어버드는 작고 눈에 보이지 않는 곳에 있어 입력 종류가 적다.[^p1][^p2] 대표 논문 1은 개조하지 않은 소비자용 스마트워치에서 소나로 손가락을 한 방향으로 세밀하게 추적해 시계 주변 공간을 입력에 쓰는 시스템을 만들어 공개하고, 그 위에서 선택을 확정하는 방법(두 번 가로지르기, 머무르기, 손가락 두드리기)을 실험으로 비교했다.[^p1] 대표 논문 2는 스마트워치용 선행 연구를 바탕으로 자력계(magnetometer, 자기장의 세기와 방향을 재는 센서)를 넣은 이어버드가 손가락에 낀 자석 반지의 자기장을 감지하게 해, 만진 손가락마다 다른 명령을 내리는 손가락 식별 입력을 만들었다.[^p2] 연구 페이지는 손톱 다섯 개를 터치 면으로 쓰는 터치 감지 손톱과, 두 손가락의 빠른 두드림 패턴으로 스마트워치에 명령을 내리는 제스처도 이 연구실의 프로젝트로 소개한다.[^research] 최근 논문 목록에는 일반 스마트워치에서 손 자세를 계속 추적하는 연구(첫 화면 소식은 소나를 쓴 손 움직임 추적으로 소개한다)와, 스마트 기기와 마이크로컨트롤러에서 음향 데이터를 모으는 공개 도구도 있다.[^cr][^home] 대표 논문 1, 2.

### 2. 착용형 기기의 생체·행동 인증

대표 논문 3은 오른쪽 귀 뒤 뼈에 붙인 진동자로 신호음을 내고, 두개골 여러 곳에 붙인 접촉 마이크로 두개골을 지나며 바뀐 소리를 받아, 그 생체 음향 정보로 스마트 글라스 사용자를 인증했다.[^p3] 대표 논문 4는 HMD의 비밀번호가 입력이 번거롭고 어깨 너머로 엿보는 공격에 약하다는 문제에서 출발해, 사용자가 정한 손동작과 그 동작 중 손 관절의 움직임 신호로 사용자를 알아보는 행동 인증 시스템을 만들었다.[^p4] 연구 페이지는 손목을 지나는 소리로 스마트워치를 잠그고 여는 생체 음향 인증도 소개한다.[^research] 최근 논문 목록에는 제스처 비밀번호의 강도를 알려 주는 계기, 행동 특징으로 엿보기 공격에서 제스처 비밀번호를 지키는 방법, 비밀번호 점검 서비스의 사용과 보안 인식에 관한 논문도 있다.[^cr] 대표 논문 3, 4.

### 3. HMD의 시선·머리 입력과 시선 추적 도구

HMD에서 화면을 확대하고 이동하는 동작은 모바일 기기의 여러 손가락 터치 동작을 그대로 옮겨 와 두 손을 크게 움직여야 한다.[^p5] 대표 논문 5는 HMD의 시선 추적 기능을 두 손·한 손·머리 입력과 묶은 세 기법을 만들어 기존 두 손 기법과 비교했다.[^p5] 대표 논문 6은 시선 추적기가 없거나 시선 데이터를 열어 주지 않는 HMD가 많다는 문제를 풀려고, 외부 시선 추적기(Pupil Labs Neon)를 여러 HMD에 붙여 쓰는 공개 도구를 만들고 세 기기에서 정확도를 평가했다.[^p6] 최근 논문 목록에는 시선과 손을 함께 쓰는 입력에서 늦은 확정 동작(late-trigger)으로 생기는 오류를 줄이는 방법, 눈을 감은 상태의 특징으로 눈 위치를 추정하는 연구, 시선과 손동작의 복잡도가 시선·손가락 집기 입력의 성능에 주는 영향에 관한 논문도 있다.[^cr] 대표 논문 5, 6.

### 4. 걸으며 쓰는 증강현실과 자율주행차-보행자 인터페이스

착용형 증강현실 헤드셋은 걸으면서 쓰는 기기지만, 걷기가 만드는 흔들림에 맞춘 입력 방법 연구는 아직 초기 단계다.[^p7] 대표 논문 7은 머리 방향과 눈 방향이 맞을 때 머리 커서의 속도에 한계를 거는 방법과, 사용자가 노린 표적을 가까움 정도로 추정해 점수를 쌓는 방법을 묶어 걸으면서도 정확히 고르게 했다.[^p7] 대표 논문 8은 자율주행차가 길을 양보할지 알리는 인터페이스 연구가 걷는 보행자에 집중해 왔다는 점에서 출발해, 증강현실 시뮬레이터 속 횡단보도를 달려서 건너는 실외 실험으로 스마트워치·차량 외부 표시 장치·도로 투영 같은 알림 위치를 비교했다.[^p8] 최근 논문 목록에는 이동이 증강현실에서 눈·머리·손으로 가리키는 입력의 성능과 작업 부담에 미치는 영향, 자율주행차와 달리는 사람 사이의 차량 외부 인터페이스, 자율주행차와 도로 이용자의 상호작용을 실험하는 증강현실 시뮬레이터에 관한 논문도 있다.[^cr] 대표 논문 7, 8.

## 대표 논문

이안 오클리 교수가 KAIST 소속으로 저자에 오른 2024–2026년 논문 가운데 교수가 마지막 저자이고 초록을 구할 수 있는 논문을 연구 갈래마다 고르게 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학회·학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [Cross, Dwell, or Pinch: Designing and Evaluating Around-Device Selection Methods for Unmodified Smartwatches](https://doi.org/10.1145/3706598.3714308) · CHI 2025 | 스마트워치는 화면이 작아 입력의 표현력이 제한된다. 이 논문은 개조하지 않은 소비자용 스마트워치에서 소나로 손가락을 한 방향으로 세밀하게 추적해 시계 주변 공간을 입력에 쓰는 첫 시스템을 만들어 공개했다. 이 시스템으로 시계 주변 입력에서 선택을 어떻게 확정할지를 두 실험으로 살폈다. 첫 실험은 두 번 가로지르기(double-crossing)·머무르기(dwell)·손가락 두드리기를 둘 중 하나를 고르는 과제에서, 둘째 실험은 그 가운데 일부를 여러 표적 중 고르는 과제에서 촉각 피드백이 있을 때와 없을 때로 비교했다. 둘 중 고르는 과제에는 두 번 가로지르기가 알맞았고, 여러 표적 과제에서는 머무르기가 뛰어났으며, 촉각 피드백은 편안함은 높였지만 성능은 높이지 않았다. 지금의 소비자용 기기에 바로 쓸 수 있는 시계 주변 입력의 설계 지침을 제시했다.[^p1] | 1저자 J. Kim, 마지막 저자 이안 오클리 |
| 2 | 2025 | [BudsID: Mobile-Ready and Expressive Finger Identification Input for Earbuds](https://doi.org/10.1145/3706598.3714133) · CHI 2025 | 무선 이어버드는 이동 중에 쓰기 좋은 착용형 컴퓨팅 기기지만, 작고 눈에 보이지 않는 곳에 있어 지원하는 입력이 적다. 이 논문은 어느 손가락으로 만졌는지에 따라 다른 반응을 내는 손가락 식별 입력을 이어버드의 새 입력 기법으로 제안했다. 스마트워치용 선행 연구를 바탕으로, 자력계를 넣은 무선 이어버드가 자석 반지의 자기장을 감지하게 만들었다. 첫 실험에서 참가자들은 이동 중에도 여러 손가락으로 이어버드를 빠르고 정확하게 만졌고(시간 0.98초, 오류 5.6%), 만진 손가락은 96.9% 정확도로 구분됐다. 둘째 실험에서 여러 손가락으로 두 번 두드리는 더 다양한 입력도 좋은 성능(두드림 간격 0.39초, 오류 2.8%)과 높은 정확도(94.7%)를 보였다. 이어버드 손가락 식별 응용의 설계를 탐색·평가하고, 자원이 적은 기기에서도 이 시스템이 돌아갈 수 있음을 보였다.[^p2] | 1저자 J. Kim, 마지막 저자 이안 오클리 |
| 3 | 2024 | [SkullID: Through-Skull Sound Conduction based Authentication for Smartglasses](https://doi.org/10.1145/3613904.3642506) · CHI 2024 | 두개골을 통해 전달되는 소리로 스마트 글라스 사용자를 인증하는 방법을 연구했다. 오른쪽 귀 뒤 뼈(유양돌기)에 표면 진동자를 붙여 신호음을 내고, 두개골 여러 곳에 붙인 접촉 마이크로 두개골을 지나며 바뀐 소리를 받아, 이 생체 음향 정보를 사용자를 구분하는 특징으로 썼다. 첫 단일 회기 실험(25명)에서 이마(brow)와 왼쪽 유양돌기에 붙인 마이크로 평균 동일 오류율(EER, 본인을 잘못 거부하는 비율과 남을 잘못 받아들이는 비율이 같아지는 값) 5.68%와 7.95%를 얻었고, 두 신호를 합치면 2.35%로 크게 낮아졌다. 여러 회기 실험(30명)에서는 세 번의 재인증에서도 오류율이 유지됐고, 기기를 다시 쓸 때의 위치 차이와 배경 소음에도 견뎠다(EER 2.72%). 일주일간의 사용성 실험에서 참가자들은 높은 사용성(SUS 점수)과 적은 작업 부담을 보고했고, 보안 분석에서 위조·흉내 공격에도 견뎠다.[^p3] | 1저자 H. Shin, 마지막 저자 이안 오클리 |
| 4 | 2026 | [Leveraging Biometric-Rich Hand Gestures for Head-Mounted Display Authentication](https://doi.org/10.1145/3772318.3791682) · CHI 2026 | HMD의 사용자 인증은 입력이 번거롭고 어깨 너머로 엿보는 공격에 약한 비밀번호에 기대고 있다. 최근 연구는 흔한 HMD 작업 중 모은 행동 신호가 사람마다 뚜렷이 다르다는 점을 밝혔다. 이 논문은 이를 바탕으로, 사용자가 정한 손동작을 단서로 삼고 사용자마다 손 관절의 움직임 신호로 이상 탐지기(평소와 다른 입력을 골라내는 모델)를 학습시키는 HMD 행동 인증 시스템을 만들었다. 여러 회기 사용자 실험(20명)과 관찰 공격 실험(10명)에서, 영상으로 엿보는 최악의 경우의 공격에도 견뎠고(AUC 0.97, EER 3.58%) 일주일 뒤에도 높은 인증 성능을 유지했다(AUC 0.93, EER 9.82%). AUC(곡선 아래 면적)는 본인과 남을 얼마나 잘 가르는지 나타내는 지표다. 사용자가 만든 생체 정보가 풍부한 손동작이 HMD 보안에 유망한 방법이라고 밝혔다.[^p4] | 1저자 A. Jalilov, 마지막 저자 이안 오클리 |
| 5 | 2026 | [GazeZoom: Exploration of Gaze-Assisted Multimodal Techniques for Panning and Zooming](https://doi.org/10.1145/3772318.3790749) · CHI 2026 | 확대(zoom)와 이동(pan)은 이미지·지도·설계 같은 2차원·3차원 장면과 데이터를 살펴보는 기본 입력이다. 모바일 기기에서 효과가 입증된 여러 손가락 터치 확대·이동이 HMD로 그대로 옮겨져, HMD에서는 두 손을 크게 움직이는 동작으로 한다. 이 논문은 그런 동작이 비효율적이고 피로를 부른다고 보고, HMD의 시선 추적 기능으로 이를 개선하는 방법을 살폈다. 시선을 두 손·한 손·머리 입력과 묶은 세 기법을 기존 두 손 기법과 비교한 실험(24명)에서, 시선을 쓰는 두 손·한 손 기법은 기존 기법보다 17–36% 빨랐고, 머리 기반 기법은 기존 기법과 같은 수준의 성능을 내면서 손을 다른 일에 쓸 수 있게 했다. 이 기법들을 쓰는 가상현실 앱도 만들어 실제로 쓸 수 있음을 확인했다.[^p5] | 1저자 Y. Lin, 마지막 저자 이안 오클리 |
| 6 | 2026 | [OpenEye: Cross-Device Eye Tracking for Head-Mounted Displays](https://doi.org/10.1145/3806031) · Proceedings of the ACM on Human-Computer Interaction | 시선 추적은 HMD에서 새로운 상호작용과 데이터 수집의 기회를 주지만, 대부분의 HMD는 시선 추적기가 없거나 시선 데이터 접근을 막는다. 외부 시선 추적기를 붙이는 기존 방법은 평가된 경우가 드물고 특정 소프트웨어나 기기에 크게 의존한다. 이 논문은 검증된 공개(오픈소스) 기기 간 시선 추적 도구를 내놓았다. Pupil Labs Neon으로 도구를 만들고 Apple Vision Pro, Meta Quest 3, XREAL Air 2 Ultra 세 HMD에서 성능을 평가했는데, Quest 3에서는 Pupil Labs의 기존 구현보다 유의하게 나았고 다른 기기에서도 일관된 정확도를 유지했다. 도구를 공개해 증강·가상현실에서 누구나 쓰고 재현할 수 있는 시선 추적 연구의 바탕을 마련했다.[^p6] | 1저자 G. Park, 마지막 저자 이안 오클리 |
| 7 | 2025 | [StabilizAR: Enabling Hands-Free Head Pointing while Mobile](https://doi.org/10.1145/3746059.3747787) · UIST 2025 | 착용형 증강현실 헤드셋은 손을 쓰지 않고 걸어 다니며 쓰는 기기지만, 걷기처럼 흔들림을 만드는 상황에 맞춘 입력 방법 연구는 아직 초기 단계다. StabilizAR는 걸을 때 머리로 움직이는 커서(head cursor) 입력을 돕는 기법이다. 머리 방향과 눈 방향이 서로 맞을 때 커서 속도에 한계를 걸어, 큰 커서 이동의 속도는 해치지 않으면서 정밀한 겨냥을 돕는다. 여기에 사용자가 노린 표적을 가까움 정도로 추정해 점수를 쌓는 표적 점수 체계를 더해 선택에 필요한 정밀도를 낮췄다. 두 실험에서 이동 중 겨냥 성공률이 6%에서 91%로 크게 오르고, 사용성과 선호도 지표도 높아졌다.[^p7] | 1저자 Y. Shin, 마지막 저자 이안 오클리 |
| 8 | 2026 | [Hit and Run: Evaluating Interface Placements for Automated Vehicle-Runner Interaction](https://doi.org/10.1145/3828157.3828764) · AutomotiveUI 2026 | 자동차 사용자 인터페이스 연구는 자율주행차가 양보 의도를 알리고 주변 도로 이용자와 공간을 두고 생기는 충돌을 푸는 인터페이스를 다뤄 왔지만, 주로 걷는 보행자에 집중해 요구가 다른 달리는 사람은 빠져 있었다. 실외 실험에서 참가자들은 증강현실 시뮬레이터로 가상 횡단보도를 달리며 건넜고, 다가오는 자율주행차는 빨강(양보 안 함)·초록(양보) 신호로 의도를 알렸다. 알림 위치는 인터페이스 없음, 스마트워치, 차량 외부 표시 장치(eHMI, 차 바깥에서 보행자에게 차의 의도를 알리는 화면), 도로 투영 네 가지였다. 인터페이스 없음은 늘 성능이 낮았고, 스마트워치는 계속 쳐다봐야 해 길에서 주의를 빼앗고 움직임을 방해했으며, eHMI는 차에 가장 가까이 가야 읽혀 해석이 늦고 차의 실제 움직임보다 화면에 기대게 했다. 도로 투영은 잠깐 보는 것만으로 읽혀 주의를 빼앗지 않았고, 달리는 사람이 차의 움직임도 함께 살펴 위험한 횡단 판단을 줄였다.[^p8] | 1저자 A. Al-Taie, 마지막 저자 이안 오클리 |

## 교수와 전문 분야

이안 오클리 교수는 KAIST 전기및전자공학부 교수다. 학부 교수 소개는 소속 디비전을 Computer division으로, 주요 연구분야를 AI & Machine Learning, Security, Software Systems & Networking, Human Computer Interaction, Integrated Circuits & Semiconductor Systems로, 주요 연구를 Human Computer Interaction, Augmented and Virtual Reality로, 학위를 University of Glasgow 박사(2003)로 적는다.[^ee]

연구실 Team 페이지의 교수 소개에 따르면 컴퓨팅 과학·심리학 공동 전공 학사(BSc, Joint Honours First Class)와 University of Glasgow 컴퓨터과학 박사학위를 가지고 있다. 아일랜드(MIT MediaLab Europe), 한국(GIST, ETRI, UNIST), 포르투갈(University of Madeira)에서 일했고, 한국(KAIST)과 미국(Carnegie Mellon HCII, University of Washington iSchool)에서 방문 교수로 지냈다. 세 대륙에 걸친 15년 이상의 교수 경력 동안 박사 졸업생을 9명 이상 배출했다고 적는다.[^team] 첫 화면 소식은 교수가 UIST'25의 대회장(general co-chair), DIS'25의 프로그램 공동위원장, Ubicomp 2024 포스터·데모 공동위원장을 맡았고, 아시아 SIGCHI 위원회 구성원들과 함께 CHI'2024에서 아시아의 HCI 교육에 관한 토론 모임을 열었다고 적는다.[^home]

논문으로 보면 전문 분야는 네 갈래다. 첫째, 스마트워치·이어버드 같은 착용형 기기에서 소나·자력계로 손가락을 감지해 새 입력을 만드는 연구다(대표 논문 1, 2).[^p1][^p2] 둘째, 두개골을 지나는 소리나 손 관절의 움직임 같은 생체·행동 신호로 착용형 기기 사용자를 인증하는 연구다(대표 논문 3, 4).[^p3][^p4] 셋째, HMD에서 시선과 머리를 쓰는 입력과 시선 추적 도구다(대표 논문 5, 6).[^p5][^p6] 넷째, 걷거나 달리는 중에 쓰는 증강현실 입력과 자율주행차 인터페이스다(대표 논문 7, 8).[^p7][^p8]

## 응용 분야

대표 논문들은 개조하지 않은 소비자용 스마트워치의 입력(대표 논문 1), 무선 이어버드의 입력(대표 논문 2), 스마트 글라스와 HMD의 사용자 인증(대표 논문 3, 4), 가상현실에서 이미지·지도를 살피는 확대·이동(대표 논문 5), 증강·가상현실의 시선 추적 연구(대표 논문 6), 걸으면서 쓰는 증강현실 헤드셋(대표 논문 7), 자율주행차와 달리는 사람 사이의 소통(대표 논문 8)을 실험 대상으로 삼았다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8] 첫 화면 소식은 연구실이 Google의 2026년 Society-Centred AI 프로그램에서 용도 제한 없는 기부금(unrestricted gift) 200,000 USD를 받아 KAIST ID의 Hwajung Hong 교수 DxD 연구실과 함께 연구한다고 적고, KAIST로 옮긴 뒤 처음 나온 연구실 박사 졸업생이 미국 뉴욕 BehaviorAI의 창업 수석 엔지니어(founding lead engineer)로 자기 연구를 사업화하기 시작했다고 알린다.[^home]

## 구성원

연구실 Team 페이지의 현재 구성원 11명이다(박사후연구원 1, 박사과정 3, 석사과정 4, 학부 인턴 3). 연구 주제 칸은 각 구성원 소개 글에서 연구 관심을 적은 문장을 옮겼고, 시작 칸은 소개 글에 적힌 연구실 합류 시점이다. 페이지는 구성원 이메일을 적지 않는다.[^team] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Chiwoong Hwang | 박사후연구원 |  | With an interdisciplinary background in Computer Science and Psychology, his research focuses on the human-centered development of immersive and intelligent technologies using mixed methods. |  |
| Mingyu Han | 박사과정 |  | His recent research interests include various challenges in wearable eye-tracking systems, spanning egocentric datasets, input interaction, and gaze estimation in the wild. | 2, 5, 6, 7, 8 |
| Hyunyoung Han | 박사과정 |  | His research focuses on interactive systems and computational interaction for embodied activities grounded in user-centered design. | 8 |
| Gyeyoung Jung | 박사과정 |  | Currently, his research interests focus on wearable-based digital healthcare using head-mounted devices. |  |
| Gangtae Park | 석사과정 | since 2025 | His research interest lies in ‘Head Mounted Display (HMD) Interaction’. | 6 |
| Hohurn Jung | 석사과정 | 2025 fall semester | His current research is centered on designing interactive systems that leverage advanced sensing technologies. |  |
| Jieun Han | 석사과정 |  | She previously joined the lab as an undergraduate intern, where she studied wearable sensing technologies. |  |
| RUI ZHANG | 석사과정 |  | Her research focuses on human-computer and human-robot interaction, particularly how people naturally interact with intelligent assistants, and she is broadly interested in exploring human-AI interaction. |  |
| Thommakoon Nitheekulawatn | 학부 인턴 | Winter 2025 (intern) | His research focuses on head-mounted eye-tracking systems, where he works on event detection from gaze point data, aiming to develop robust algorithms that perform reliably in real-world scenarios involving natural head movements and dynamically changing environments. |  |
| Chani Kim | 학부 인턴 | Spring 2026 | His research interests include designing novel input interactions for smart glasses and augmented reality (AR) environments, with a focus on creative algorithms. |  |
| Juyoung Lee | 학부 인턴 |  | Her research interests include novel interaction techniques for VR devices, particularly hand tracking and AI-connected interaction systems. |  |

## 졸업생과 이전 구성원

Team 페이지 「Alumni」에 실린 15줄이다(박사후연구원 2, 박사과정 3, 방문 대학원생 2, 학부 인턴 8). 괄호 안은 페이지가 적은 당시 역할과 소속이고, 연도는 페이지 표기다. Eunyong Cheon은 박사과정(UNIST, 2025)과 박사후연구원(2026) 두 줄에 나온다. UNIST로 적힌 두 줄은 연구실이 UNIST에 있던 시기의 박사과정 학생이다. 페이지는 진로를 적지 않으며, 진로 칸은 첫 화면 소식이 적은 네 줄만 채웠다.[^team][^home]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Eunyong Cheon | 박사후연구원 (2026) | NICT (Tokyo) |
| Ammar Al-Taie | 박사후연구원 (2026) | Whoop (Doha office) |
| Jiwan Kim | 박사과정 (2026) | BehaviorAI, New York (founding lead engineer) |
| Yonghwan Shin | 박사과정 (UNIST) (2026) | NETLab at DGIST (postdoc) |
| Eunyong Cheon | 박사과정 (UNIST) (2025) |  |
| Yunqiang Pei | 방문 대학원생 (UESTC) (2026) |  |
| Yilong Lin | 방문 대학원생 (SUSTech) (2025) |  |
| Wutthipat Wutthipattharatham | 학부 인턴 (2026) |  |
| Nahyun Lee | 학부 인턴 (2026) |  |
| Amin Jalilov | 학부 인턴 (2026) |  |
| Yeji Park | 학부 인턴 (2025) |  |
| Hyein Jeong | 학부 인턴 (2025) |  |
| Dongseok Ji | 학부 인턴 (2024) |  |
| Seunghee Han | 학부 인턴 (2024) |  |
| Seungyun Yeom | 학부 인턴 (2024) |  |

## 최근 논문 목록 (2021–2026)

이안 오클리 교수가 저자로 참여한 2021–2026년 논문 48편이다(학회 논문 35, 학술지 10, 책 속 장 2, 사전 공개본 1). 저자·제목·학술지·학회 표기는 출판사가 등록한 서지를 따랐다. 학회 논문에는 워크숍·토론 모임 제안과 확장 초록도 들어 있고, 2026년의 SSRN 논문 한 편은 동료 심사 전 사전 공개본이다. 연구실은 2023년에 UNIST에서 KAIST로 옮겨 왔다. 2021–2023년 논문 가운데 출판사 서지에 교수 소속이 적힌 논문은 모두 UNIST로 적혀 있어, 이 시기 논문은 현재 KAIST 연구실의 성과로 묶지 않는다.[^cr][^home]

**2026**

- Eunjee Kim, Hyunjae Gil, Ian Oakley, Gwanseob Shin. "Vehicle-synchronized rotational peripheral cues reduce motion sickness in in-car virtual reality". *Applied Ergonomics*.
- Adrian Javier Leon Valencia, Pedro Tavares, Inês Alves, Ian Oakley, Augusto Esteves. "Hands-VRee: Towards Hands-Free Gaming in VR via Concurrent Input for Locomotion, Viewport Control, and Pointing". *Proceedings of the 28th International Conference On Multimodal Interaction*.
- Ammar Al-Taie, Mingyu Han, Ian Oakley. "ARena: Augmented Reality Simulator for Automated Vehicle-Human Road User Interaction". *Adjunct Proceedings of the 18th International Conference on Automotive User Interfaces and Interactive Vehicular Applications*.
- Ammar Al-Taie, Hyunyoung Han, Mingyu Han, Ian Oakley. "Hit and Run: Evaluating Interface Placements for Automated Vehicle-Runner Interaction". *Proceedings of the 18th International Conference on Automotive User Interfaces and Interactive Vehicular Applications*.
- Ammar Al-Taie, Hyunyoung Han, Ian Oakley. "ComiXR: Exploring Comic Layouts in eXtended Reality". *Proceedings of the 2026 Designing Interactive Systems Conference*.
- Gangtae Park, Mingyu Han, Ian Oakley. "OpenEye: Cross-Device Eye Tracking for Head-Mounted Displays". *Proceedings of the ACM on Human-Computer Interaction*.
- Chiwoong Hwang, Tiare Feuchtner, Ian Oakley, Kaj Grønbæk. "Calibrating Pseudo-Haptics: Toward Effective Weight Simulation for Industrial Training in Virtual Reality". *International Journal of Human–Computer Interaction*.
- Yilong Lin, Mingyu Han, Weitao Jiang, Seungwoo Je, Ian Oakley. "GazeZoom: Exploration of Gaze-Assisted Multimodal Techniques for Panning and Zooming". *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*.
- Amin Jalilov, Eunyong Cheon, Ian Oakley. "Leveraging Biometric-Rich Hand Gestures for Head-Mounted Display Authentication". *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*.
- Helen Stefanidi, Vincent van Rheden, Linjia He, Michelle Adiwangsa, Jan-Hendrik Sünderkamp, Alina Itzlinger, Andrii Matviienko, Julie R. Williamson, Ian Oakley, Markus Tatzgern, Alexander Meschtscherjakov. "Next Steps for Augmented Reality On-the-Move: Challenges and Opportunities". *Proceedings of the Extended Abstracts of the 2026 CHI Conference on Human Factors in Computing Systems*.
- Ammar Al-Taie, Thomas Goodge, Shaun Macdonald, Ian Oakley, Stephen Anthony Brewster. "Running into Traffic: Investigating External Human-Machine Interfaces for Automated Vehicle-Runner Interaction". *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*.
- Jiwan Kim, Chi-Jung Lee, Hohurn Jung, Tianhong Catherine Yu, Ruidong Zhang, Ian Oakley, Cheng Zhang. "WatchHand: Enabling Continuous Hand Pose Tracking On Off-the-Shelf Smartwatches". *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*.
- Mingyu Han, Yonghwan Shin, Yeji Park, Gangtae Park, Ian Oakley. "Effects of Stress on 3D Interface Interaction Techniques". *SSRN 사전 공개본*.

**2025**

- Jiwan Kim, Chi-Jung Lee, Xiaoran Fan, Dong Li, Edison Thomaz, Alanson Sample, Ian Oakley, Cheng Zhang. "Beyond Sound: The First Workshop on Intelligent Acoustic Sensing on Wearables". *Companion of the 2025 ACM International Joint Conference on Pervasive and Ubiquitous Computing*.
- Jiwan Kim, Hohurn Jung, Ian Oakley. "OpenAcoustics : An Open-Source Framework for Acoustic Data Capture on Smart Devices and Microcontrollers". *Companion of the 2025 ACM International Joint Conference on Pervasive and Ubiquitous Computing*.
- Yonghwan Shin, Augusto Esteves, Ian Oakley. "Using Augmented Reality on the go: Understanding the effects of mobility on user performance and subjective workload across eye, head, and hand ray pointing". *International Journal of Human-Computer Studies*.
- Yonghwan Shin, Mingyu Han, Ian Oakley. "StabilizAR: Enabling Hands-Free Head Pointing while Mobile". *Proceedings of the 38th Annual ACM Symposium on User Interface Software and Technology*.
- Yeji Park, Jiwan Kim, Ian Oakley. "GazeHandSync: Mitigating Late-Trigger Errors for Seamless Gaze-Hand Interactions". *Proceedings of the 2025 Symposium on Eye Tracking Research and Applications*.
- Jiwan Kim, Mingyu Han, Ian Oakley. "BudsID: Mobile-Ready and Expressive Finger Identification Input for Earbuds". *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*.
- Jiwan Kim, Jiwan Son, Ian Oakley. "Cross, Dwell, or Pinch: Designing and Evaluating Around-Device Selection Methods for Unmodified Smartwatches". *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*.
- Eunyong Cheon, Ian Oakley. "Securing Gesture Passwords Against Shoulder Surfing Using Behavioral Features". *Proceedings of the Extended Abstracts of the CHI Conference on Human Factors in Computing Systems*.
- Sanghak Oh, Heewon Baek, Jun Ho Huh, Taeyoung Kim, Woojin Jeon, Ian Oakley, Hyoungshick Kim. "Understanding and Improving User Adoption and Security Awareness in Password Checkup Services". *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*.
- Haiming Liu, Shengdong Zhao, Silang Wang, Preben Hansen, Ian Oakley, Khanh-Duy Le. "Designing Interactive Multimodal Information Retrieval and Access for Heads Up Computing (DIMIRA-HUC)". *Proceedings of the 2025 ACM SIGIR Conference on Human Information Interaction and Retrieval*.
- Adrian J. Leon Valencia, Ian Oakley, Augusto Esteves. "Multimodal Hands-Free VR For Wheelchair Users With Upper Limb Mobility Limitations: Leaning, Head-Gain, and Gaze Pointing". *2025 IEEE Conference on Virtual Reality and 3D User Interfaces Abstracts and Workshops (VRW)*.

**2024**

- Jiwan Kim, Hohurn Jung, Ian Oakley. "VibraHand: In-Hand Superpower Enabling Spying, Precognition, and Telekinesis". *The 37th Annual ACM Symposium on User Interface Software and Technology*.
- Chiwoong Hwang, Tiare Feuchtner, Ian Oakley, Kaj Grønbæk. "Enriching Industrial Training Experience in Virtual Reality with Pseudo-Haptics and Vibrotactile Stimulation". *30th ACM Symposium on Virtual Reality Software and Technology*.
- Mingyu Han, Ian Oakley. "EyeWithShut: Exploring Closed Eye Features to Estimate Eye Position". *Companion of the 2024 on ACM International Joint Conference on Pervasive and Ubiquitous Computing*.
- Shengdong Zhao, Ian Oakley, Yun Huang, Haiming Liu, Can Liu. "Heads-Up Computing: Opportunities and Challenges of the Next Interaction Paradigm with Wearable Intelligent Assistants". *Companion of the 2024 on ACM International Joint Conference on Pervasive and Ubiquitous Computing*.
- Yeji Park, Jiwan Kim, Ian Oakley. "The Impact of Gaze and Hand Gesture Complexity on Gaze-Pinch Interaction Performances". *Companion of the 2024 on ACM International Joint Conference on Pervasive and Ubiquitous Computing*.
- Jiwan Kim, Doyoung Lee, Mingyu Han, Jaeho Kim, Vassilis Kostakos, Ian Oakley. "Unpacking Instagram use: The impact of upward social comparisons on usage patterns and affective experiences in the wild". *International Journal of Human-Computer Studies*.
- Soohwan Lee, Seoyeong Hwang, Ian Oakley, Kyungho Lee. "Expanding the Design Space of Vision-based Interactive Systems for Group Dance Practice". *Designing Interactive Systems Conference*.
- Zhicong Lu, Ian Oakley, Chat Wacharamanotham. "A SIG on Understanding and Overcoming Barriers in Establishing HCI Degree Programs in Asia". *Extended Abstracts of the CHI Conference on Human Factors in Computing Systems*.
- Hyejin Shin, Jun Ho Huh, Bum Jun Kwon, Iljoo Kim, Eunyong Cheon, HongMin Kim, Choong-Hoon Lee, Ian Oakley. "SkullID: Through-Skull Sound Conduction based Authentication for Smartglasses". *Proceedings of the CHI Conference on Human Factors in Computing Systems*.

**2023**

- Jiwan Kim, Jongjin Park, Ian Oakley. "SonarAuth: Using Around Device Sensing to Improve Smartwatch Behavioral Biometrics". *Adjunct Proceedings of the 2023 ACM International Joint Conference on Pervasive and Ubiquitous Computing & the 2023 ACM International Symposium on Wearable Computing*.
- Eunyong Cheon, Jun Ho Huh, Ian Oakley. "GestureMeter: Design and Evaluation of a Gesture Password Strength Meter". *Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems*.
- Jiwan Kim, Doyoung Lee, Jaeho Kim, Ian Oakley. "Can Eye Gaze Improve Emotional State Detection on Off the Shelf Smart Devices". *2023 IEEE International Conference on Big Data and Smart Computing (BigComp)*.
- HongMin Kim, Ian Oakley. "Improving Hand Gesture Recognition via Infrared Tomography of the Wrist over Multiple Wearing Sessions". *Lecture Notes in Computer Science*.

**2022**

- Hyunjae Gil, Ian Oakley. "ThumbAir". *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies*.
- Jun Ho Huh, Hyejin Shin, HongMin Kim, Eunyong Cheon, Youngeun Song, Choong-Hoon Lee, Ian Oakley. "WristAcoustic". *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies*.
- Eunjee Kim, Hyunjae Gil, Jiwon Ryu, Ian Oakley, Gwanseob Shin. "The effect of peripheral cues on motion sickness mitigationwhen using a VR HMD in a car". *Proceedings of the Human Factors and Ergonomics Society Annual Meeting*.
- Jiwan Kim, Ian Oakley. "SonarID: Using Sonar to Identify Fingers on a Smartwatch". *CHI Conference on Human Factors in Computing Systems*.
- Mintra Ruensuk, Taewan Kim, Hwajung Hong, Ian Oakley. "Sad or just jealous? Using Experience Sampling to Understand and Detect Negative Affective Experiences on Instagram". *CHI Conference on Human Factors in Computing Systems*.
- Youngeun Song, Ian Oakley. "PushPIN: A Pressure-Based Behavioral Biometric Authentication System for Smartwatches". *International Journal of Human–Computer Interaction*.
- Youngeun Song, Ian Oakley. "PushID: A Pressure Control Interaction-Based Behavioral Biometric Authentication System for Smartwatches". *Lecture Notes in Computer Science*.

**2021**

- Paulo Bala, Ian Oakley, Valentina Nisi, Nuno Jardim Nunes. "Dynamic Field of View Restriction in 360° Video: Aligning Optical Flow and Visual SLAM to Mitigate VIMS". *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems*.
- DoYoung Lee, Jiwan Kim, Ian Oakley. "FingerText: Exploring and Optimizing Performance for Wearable, Mobile and One-Handed Typing". *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems*.
- Woojin Lee, Ramkrishna Prasad, Seungwoo Je, Yoonji Kim, Ian Oakley, Daniel Ashbrook, Andrea Bianchi. "VirtualWire: Supporting Rapid Prototyping with Instant Reconfigurations of Wires in Breadboarded Circuits". *Proceedings of the Fifteenth International Conference on Tangible, Embedded, and Embodied Interaction*.
- Seungji Lee, Doyoung Lee, Hyunjae Gil, Ian Oakley, Yang Seok Cho, Sung-Phil Kim. "Eye Fixation-Related Potentials during Visual Search on Acquaintance and Newly-Learned Faces". *Brain Sciences*.

## 소식

누리집 첫 화면 News의 36건 전부다(2024년 3월–2026년 10월). 날짜는 항목 끝에 적힌 월 표기이고, 날짜가 적혀 있지 않은 1건(UNIST 박사 졸업과 박사후연구원 이동 소식)은 날짜 없이 적었다. 문장은 게시된 그대로이며, UNIST 시기 학생의 졸업·논문 소식도 섞여 있다.[^home]

- October 2026 · Grant Awarded! WIT Lab was selected to receive an unrestricted gift of 200,000 USD as part of Google's 2026 Society-Centred AI program. We're excited to be working in collaboration with Hwajung Hong's DxD lab at KAIST ID on this project.
- September 2026 · Moving On! Ammar finished his productive stay in the lab as a post-doc by being headhunted to work at Whoop's new Doha office. We'll miss you Ammar!
- September 2026 · Papers at ICMI'26 and AutoUI'26. Together with collaborators from the University of Lisbon, we published work on interaction in VR games at ICMI, and Ammar presented work on how runners interact with different wearable interfaces that convey information about the vehicles around them at AutoUI
- September 2026 · New arrivals. Pleased to welcome Chiwoong Hwang as a BK21 post-doc and Rui Zhang as an MSc student.
- August 2026 · Graduation! Jiwan graduated from his PhD in record time - the first PhD from the lab since its move to KAIST in 2023. He's off to an amazing start commercializing his research as the founding lead engineer at BehaviorAI in New York. We can't wait to see what he builds.
- July 2026 · WIT Lab in the news! Our DIS'26 paper on XR Comics was covered by the local broadcaster TJB - check out the story or catch some of the print press coverage. Congrats to Ammar, who initiated and led this project out of his passion for the format. Now we have to figure out how to do more work on comic books ;-).
- June 2026 · Papers published at ACM DIS'26 and ACM ETRA'26! Ammar is presenting work on experiencing comic books in XR at DIS, and Gangtae will attend ETRA to present an open-source framework for integrating external eye tracking into HMDs, providing research-quality tracking across diverse headsets.
- May 2026 · IJHCI paper published. Happy to publish a collaboration with colleagues at the University of Aarhus and the University of Konstanz, covering work on pseudo-haptic illusions that Chiwoong Hwang completed during a research visit to the lab. Congrats Chiwoong!
- May 2026 · WIT Lab CHI papers in the press. WIT Lab's Ammar al Taie and our colleagues at MIG at the University of Glasgow were interviewed for BBC TechLife about our work on pedestrian-AV interaction. Jiwan Kim was interviewed, alongside colleagues at Cornell SciFi Lab, about our WatchHand paper: check out the press release for more info.
- April 2026 · Four Papers at CHI'26! Our papers cover interaction techniques for zoom and pan on HMDs (with the Immersive Design Group at SUSTech), hand motion tracking using sonar on commercial smartwatches (with the SciFi Lab at Cornell), pedestrian interactions with autonomous vehicles (with MIG at the University of Glasgow), and gesture authentication on HMDs - all credit to Amin Jalilov and Eunyong Cheon, who led this work and received an Honorable Mention award! It's going to be a busy week in Barcelona.
- March 2026 · New arrivals. Two new students join WIT Lab. Gyeyoung Jung joined the lab as a PhD student, and Jieun Han as an MSc student. Welcome to both!
- Graduations and departures. Yonghwan Shin, my final PhD student at UNIST, graduated and began as a postdoc at the NETLab at DGIST, while Eunyong Cheon finished up his postdoc and will shortly move to Tokyo to work at NICT. Congrats to both!
- February 2026 · Workshop at CHI'26. Join us at CHI'26 to discuss Next Steps Next Steps for Augmented Reality On-the-Move - or how AR can support interaction in dynamic, real-world settings. Looking forward to a fun event working with colleagues from the University of Salzburg, Salzburg University of Applied Science, Monash, KTH, and the University of Glasgow.
- October 2025 · UIST'25. The lab helped organize UIST'25, with Ian serving as general co-chair (with the amazing Jeeeun Kim), Jiwan as registration co-chair, and Mingyu as video recording co-chair. Yonghwan also presented his first UIST paper. Check the event out on the UIST'25 flickr, Thank you to all the people who helped make UIST'25 happen. Looking forward to UIST'26!
- September 2025 · New arrivals. With the start of the fall semester, Ammar Al-Taie joined the lab as a post-doc, Hyunyoung Han as a PhD student, and Hohurn Jung as an MSc student. Welcome all!
- September 2025 · Faculty job. Lab alumnus Hyunjae Gil (who graduated when the lab was based at UNIST) has started as a faculty member at DGIST. Welcome back to Korea, Hyunjae - looking forward to working together again in the future!
- August 2025 · Paper accepted to IJHCS. Yonghwan Shin (UNIST) published a paper documenting the disruptions to pointing on HMDs caused by walking. Thanks to collaborators at Instituto Superior Técnico!
- July 2025 · Paper accepted to UIST'25. Yonghwan Shin (UNIST) led work to improve the stability of head pointing during the use of HMDs while walking. Looking forward to going back to Busan!
- May 2025 · Short paper at ETRA'25. Yeji Park published her undergraduate internship project on hand-eye coordination errors during interaction in VR and AR. Congratulations to Yeji and her graduate student mentor Jiwan Kim!
- May 2025 · Workshop at Ubicomp/ISWC'25. Jiwan Kim and Ian Oakley are co-organizing "BeyondSound: The First Workshop on Intelligent Acoustic Sensing on Wearables" at Ubicomp/ISWC'25 in Finland in October 2025. We have an amazing team of co-organizers from Cornell, Google, UMBC, UT Austin, and U. Michigan. Submit by July 4, 2025!
- May 2025 · Arduino featured one of our CHI'25 papers, on multi-finger interaction with an earbud, on its LinkedIn page: ❤️ Arduino!
- Feb 2025 · Three papers and two posters were accepted to ACM CHI 2025. Two papers cover wearable input and interaction - one using sonar to interact with smartwatches and the other exploring finger identification input on earbuds. The final paper, a collaboration with SKKU and Samsung R&D, explores the usability issues of password checkup services. We also have two LBW posters on gesture-based authentication and alleviating dry-eye by promoting blinking during smart glass use. Looking forward to a busy CHI in Yokohama!
- Feb 2025 · Graduations! Eunyong Cheon (PhD), Hongmin Kim (PhD), and Mingyu Han (MSc), lab students at UNIST, all graduated on Feb 20th. Huge congratulations. Eunyong and Mingyu will continue their research as a post-doctoral scholar and PhD student at WIT Lab, while Hongmin has started his career at LG CNS Entrue Consulting.
- Nov 2024 · Winter Interns: WIT Lab is looking for interns for Jan/Feb 2025. Take a look at the projects (click here) and apply via email to Ian Oakley (ianoakley@kaist.ac.kr). Applications are due on Monday, 25th November
- Oct 2024 · UIST'25 General Co-Chair: Ian Oakley will serve as general co-chair for UIST'25, which will be held in Busan, Korea Sept 28-1st Oct 2025. I am looking forward to working with my star co-chair, Jeeeun Kim from Texas A&M, over the next year!
- Oct 2024 · Student Innovation Contest (SIC) at UIST'24: WIT Lab graduate student Jiwan Kim and undergraduate intern Hohurn Jung won the UIST'24 SIC People's Choice Award for a glove that gives its wearer superpowers. Three hours of hard work demoing the system in Pittsburgh paid off - congratulations!
- Sept 2024 · Paper accepted to VRST'24: in collaboration with colleagues at Aarhus University and the University of Konstanz we explored how psuedo-haptic feedback can enhance virtual reality training simulations - read more here.
- July 2024 · DIS'25 Program Co-Chair: Ian Oakley is one of the program co-chairs of ACM DIS'25, which will be held in Madeira, Portugal, in July 2025. Really excited to be part of an amazing team with Qian Yang from Cornell and Clement Zheng from NUS. Looking forward to a great event.
- June 2024 · Paper accepted to IJHCS: Together with colleagues at The University of Melbourne and UNIST, we investigated how users experience emotions when browsing social media in the wild - read more here.
- May 2024 · Paper accepted to ACM DIS'2024: Together with colleagues at UNIST Design, we studied the design space for augmented reality systems to support team dance learning - read more here.
- May 2024 · Workshop CfP Open: Join us at Ubicomp 2024 in Melbourne to discuss the latest research on Heads Up Computing. Submissions are due by July 7th.
- May 2024 · SIG at CHI'2024: Together with other members of the Asian SIGCHI Committee, Ian Oakley organized a discussion on HCI education in Asia, attracting around 50 attendees! We hope to use these insights to help support the development of HCI degree programs in Asia.
- April 2024 · Scholarship Awarded: Jiwan Kim, a PhD student in WIT Lab, received one of the prestigious inaugural presidential science scholarships for graduate students. Congratulations Jiwan!
- April 2024 · Summer Interns: WIT Lab is looking for interns for July/August 2024. Take a look at the projects (click here) and apply via email to Ian Oakley (ianoakley@kaist.ac.kr). Applications are due on Friday 24th May.
- March 2024 · Ubicomp 2024 Posters and Demos: I'm co-chairing Ubicomp 2024 Posters and Demos. Submit by 31st May 2024 and join us for an exciting Ubicomp program in Melbourne in October.
- March 2024 · Paper accepted to ACM CHI'2024: SkullID studies a novel bioacoustic biometric for smart glasses. Thanks to collaborators at UNIST and Samsung Research.

## 연락과 위치

- 연구실: KAIST IT융합빌딩(N1) 212호, (34141) 대전광역시 유성구 대학로 291[^home]
- 교수 연구실: IT융합빌딩(N1) 208호[^ee]
- 전화: 042-350-7476[^home][^ee]
- 교수 이메일: ianoakley@kaist.ac.kr[^ee]
- 모집 안내: 누리집은 석사·박사과정 학생을 모집하고 있다고 적는다.[^home]
[^p1]: J. Kim, J. Son, I. Oakley, Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems, 1-11 (온라인 2025-04-25). <https://doi.org/10.1145/3706598.3714308> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J. Kim, M. Han, I. Oakley, Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems, 1-17 (온라인 2025-04-25). <https://doi.org/10.1145/3706598.3714133> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: H. Shin 외, I. Oakley, Proceedings of the CHI Conference on Human Factors in Computing Systems, 1-19 (온라인 2024-05-11). <https://doi.org/10.1145/3613904.3642506> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: A. Jalilov, E. Cheon, I. Oakley, Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems, 1-19 (온라인 2026-04-13). <https://doi.org/10.1145/3772318.3791682> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: Y. Lin 외, I. Oakley, Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems, 1-18 (온라인 2026-04-13). <https://doi.org/10.1145/3772318.3790749> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: G. Park, M. Han, I. Oakley, Proceedings of the ACM on Human-Computer Interaction 10, 1-17 (온라인 2026-05-28). <https://doi.org/10.1145/3806031> 초록 기준.
[^p7]: Y. Shin, M. Han, I. Oakley, Proceedings of the 38th Annual ACM Symposium on User Interface Software and Technology, 1-13 (온라인 2025-09-27). <https://doi.org/10.1145/3746059.3747787> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: A. Al-Taie, H. Han, M. Han, I. Oakley, Proceedings of the 18th International Conference on Automotive User Interfaces and Interactive Vehicular Applications, 179-191 (온라인 2026-09-19). <https://doi.org/10.1145/3828157.3828764> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 연구실 누리집 첫 화면 <https://wit.kaist.ac.kr/> (연구실 소개, 모집 안내, News, Projects, 연락처, 2026-10-23 열람)
[^team]: 연구실 누리집 Team 페이지 <https://wit.kaist.ac.kr/team> (교수 소개, 구성원 소개, Alumni, 2026-10-23 열람)
[^research]: 연구실 누리집 Research 페이지 <https://wit.kaist.ac.kr/research> (연구 소개, 프로젝트 소개, 2026-10-23 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(이안 오클리) <https://ee.kaist.ac.kr/professor/%ec%9d%b4%ec%95%88-%ec%98%a4%ed%81%b4%eb%a6%ac/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 디비전, 학위, 2026-10-23 열람)
[^cr]: 2021–2026년 논문의 출판사 등록 서지(Crossref) <https://api.crossref.org/> (저자 확인 기준은 근거 페이지, 2026-10-23 조회)

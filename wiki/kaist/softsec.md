# 소프트웨어 보안 연구실 (Software Security Research Lab, SoftSec Lab)

**KAIST 전산학부·정보보호대학원 · 차상길 교수**

- 분야: 소프트웨어 보안(바이너리 분석, 퍼징, 기호 실행, 공격 검증, 악성코드 분석), 프로그램 분석, 소프트웨어 신뢰성
- 대분야: 컴퓨팅·AI
- 태그: 소프트웨어·시스템 보안[^home][^cslab][^p1], 퍼징[^home][^p1][^p4], 프로그램 분석·검증[^home][^cslab][^p7]
- 홈페이지: <https://softsec.kaist.ac.kr/>
- 근거와 출처: [SoftSec Lab 근거 페이지](softsec-sources.md)

> 컴퓨터 보안과 프로그램 분석이 만나는 곳에서 소프트웨어의 보안을 보장하는 시스템과 기법을 만드는 연구실로, 바이너리 분석, 공격 검증, 악성코드 분석, 퍼징, 기호 실행을 연구한다.[^home]

## 무엇을 연구하나

연구실은 KAIST 정보보호대학원과 전산학부의 차상길 교수가 이끄는 연구실이다.[^pi][^gsisfac] 누리집은 연구실 이름을 SoftSec Lab at KAIST와 Software Security Research Lab으로 적고, 창 제목에는 국문 이름 「소프트웨어 보안 연구실」을 함께 적는다.[^home] 전산학부 연구실 소개는 「소프트웨어 보안 연구실」로,[^cslab] 정보보호대학원 연구실 목록은 Software Security (SoftSec) Lab으로 적는다.[^gsislab] 정보보호대학원 교수진 목록은 교수의 소속을 전산학부와 정보보호대학원으로 적는다.[^gsisfac]

누리집은 연구실이 컴퓨터 보안과 프로그램 분석(program analysis, 프로그램의 코드나 실행을 살펴 그 동작과 성질을 알아내는 일)이 만나는 곳에서 소프트웨어 보안을 보장하는 시스템과 기법을 활발히 만들고 있다고 소개한다. 연구 관심사로는 바이너리 분석(binary analysis, 컴퓨터가 바로 실행하는 기계어 형태의 프로그램인 바이너리를 분석하는 일), 공격 검증(exploit verification), 악성코드 분석, 퍼징(fuzzing, 자동으로 만든 입력을 프로그램에 넣어 실행해 보며 오류와 취약점을 찾는 시험 기법), 기호 실행(symbolic execution, 입력을 구체적인 값 대신 기호로 두고 프로그램을 따라가며 각 실행 경로에 이르는 입력 조건을 구하는 분석 기법)을 든다.[^home] 연구 방법으로는 프로그램을 분석해 취약점을 찾는 일, 방어 기법을 만들기 위해 공격 해킹 기법을 연구하는 일, 안전하고 믿을 수 있는 소프트웨어 시스템을 만드는 일의 세 가지를 든다.[^home]

전산학부 연구실 소개는 연구실이 프로그램 바이너리에 대한 이해를 바탕으로 여러 형태의 보안 취약점을 탐지하고 방어하는 방법을 연구한다고 적는다. 주로 소프트웨어의 취약점 탐지, 악성코드의 분석과 분류, 공격 검증, 역공학(reverse engineering, 완성된 프로그램이나 제품을 분석해 그 구조와 동작 원리를 알아내는 일) 같은 바이너리 분석에 기반한 연구를 하며, 세상의 프로그램들을 자동으로 검사해 안전한 컴퓨팅 환경을 만드는 것을 비전으로 든다.[^cslab] 정보보호대학원 연구실 목록은 연구 분야를 Software security, Program analysis, Software reliability로 적고, 소프트웨어에 있는 버그(취약점)를 자동으로 탐지하기, 버그의 근본 원인을 파악해 디버깅하기, 소프트웨어 자체의 설계와 구현을 안전하게 하기 같은 주제를 함께 연구한다고 소개한다.[^gsislab] 교수 소개는 교수의 연구가 컴퓨터 보안과 소프트웨어 공학의 교차점에 있으며 대개 프로그램을 자동 분석하는 시스템을 설계·구현하고 평가하는 일을 포함한다고 적고,[^pikr][^csfac] 인턴십 안내 페이지는 연구실의 내부 과제 대부분이 프로그램 바이너리를 분석하는 크고 복잡한 시스템을 만드는 일이라고 적는다.[^intern]

첫째 갈래는 **퍼징으로 취약점 자동으로 찾기**다. 대표 논문에서는 Windows 운영체제의 시스템 호출(응용 프로그램이 운영체제 커널에 기능 수행을 요청하는 방법) 형식 정보를 정적 바이너리 분석으로 자동 추론해 커널 퍼징에 쓰는 NTFuzz를 만들어, 알려지지 않았던 커널 버그 11개를 찾았다.[^p1] 스마트 계약(블록체인에 올려 두고 정해진 조건이 맞으면 자동으로 실행되는 프로그램)의 바이트코드를 정적 분석과 동적 데이터 흐름 분석으로 살펴 퍼징을 이끄는 Smartian도 내놓았다.[^p2] 퍼저를 평가하는 데 쓰는 버그 든 프로그램을 만드는 문제를 미로 생성 문제로 바꿔, 버그의 정답이 정확히 알려진 벤치마크를 합성하는 Fuzzle과,[^p3] 어셈블러(사람이 읽는 어셈블리어 명령을 기계어로 바꾸는 프로그램)가 내는 오류 메시지로 그 문법 규칙을 추론해 어셈블러를 시험하는 AsFuzzer도 만들었다.[^p4] 최근 논문 목록에는 프로그램의 특정 목표 지점을 겨냥하는 지향성 퍼징을 제목에 단 DAFL(USENIX Security 2023)과 지향성 퍼저 평가(FSE 2024)·합성 벤치마크의 효과(APSEC 2023) 논문, 퍼징이 포화(saturation)에 이른 때를 알아내는 연구(FUZZING 2025), 블록체인 합의(consensus, 참여자들이 같은 거래 기록에 동의하는 절차) 구현을 위한 차등 퍼징(ICSE 2025), 대형 언어 모델의 도움을 받은 비행 소프트웨어 퍼징용 명령 구문 추출(WISA 2026)도 있다.[^pi][^news] 교수가 공저한 퍼징 개관 논문 「The Art, Science, and Engineering of Fuzzing: A Survey」(IEEE Transactions on Software Engineering, 2021)는 교수 누리집 목록에 Best Paper Award로 표시되어 있다.[^pi]

둘째 갈래는 **바이너리 코드 분석과 재조립**이다. 대표 논문에서는 정적 바이너리 재작성(static binary rewriting, 프로그램을 실행하지 않은 채 바이너리를 고쳐 새 바이너리를 만드는 일)의 한 갈래인 재조립(reassembly, 바이너리를 다시 조립할 수 있는 어셈블리 코드로 되돌린 뒤 고쳐 새 바이너리로 만드는 방법)에서, 기존 재조립 도구들에 생기는 오류의 유형을 형식적으로 정의하고 그 오류를 찾는 자동 도구 REASSESSOR와 대규모 벤치마크를 내놓았다.[^p5] 이어 주요 리눅스 배포판의 기본 설정이 되어 가는 보안 기능 CET가 바이너리에 남기는 성질을 이용해, 원래 의미를 해치지 않으면서 바이너리 안의 모든 메모리 참조를 기호화(symbolization, 메모리 위치를 가리키는 값을 찾아 코드가 옮겨져도 따라가는 이름표로 바꾸는 일)하는 재조립 도구 SURI를 만들었다.[^p6] 바이너리에서 함수를 찾아내는 문제에서는 CPU 구조에 묶이지 않는 단서 16가지를 확률적 추론으로 묶는 FunProbe를 만들었다.[^p7] 최근 논문 목록에는 Intel CET가 역공학의 함수 식별에 주는 영향(DSN 2022), 해석 가능한 특징으로 다시 살핀 바이너리 코드 유사도 분석(IEEE Transactions on Software Engineering, 2023), Python 디컴파일(decompilation, 기계어나 바이트코드로 된 프로그램을 사람이 읽을 수 있는 고급 언어 코드로 되돌리는 일)을 다룬 PyLingual(IEEE Symposium on Security and Privacy 2025)과 디컴파일러 출력의 수정 실태를 살핀 연구(CCS 2025), 이더리움 가상 머신(EVM) 디컴파일을 위한 타입 추론(type inference, 프로그램 속 값의 자료형을 알아내는 일) EVMpress(CBT 2025), 다양한 바이너리 데이터셋을 만드는 BinForge(APSEC 2026 채택)도 있다.[^pi][^news]

셋째 갈래는 **부정행위·공격의 탐지와 공격 기법 연구**다. 누리집은 방어 기법을 만들기 위해 공격 해킹 기법을 연구한다고 밝힌다.[^home] 대표 논문에서는 1인칭 슈팅(FPS) 게임에서 상대를 쓰러뜨리도록 돕는 부정 프로그램인 에임봇(aimbot)을 게임 이용자 쪽 컴퓨터에서 나눠 탐지해 서버 쪽 부담을 줄이고, 새 딥러닝 모델로 에임봇 사용이 일으키는 비정상 행동을 찾아내는 BotScreen을 만들었다.[^p8] 최근 논문 목록에는 익스플로잇(exploit, 소프트웨어의 취약점을 악용해 공격자가 원하는 동작을 일으키는 코드나 입력)을 쓰기 위한 도메인 특화 언어 PoE(SVCC 2024 포스터)가 있고,[^pi][^news] 연구실 News 페이지(2026년 8월)는 컴파일 플래그 악용을 제목에 단 논문 「Capture The Flag: Exploiting Compilation Flags to Summon Trojan Horses」가 NDSS 2027에 실린다고 알린다.[^news]

## 주요 연구 주제

### 1. 퍼징으로 취약점 자동으로 찾기

시스템 호출 형식을 추론하는 Windows 커널 퍼징(NTFuzz), 정적·동적 데이터 흐름 분석을 쓴 스마트 계약 퍼징(Smartian), 정답이 알려진 퍼저 평가용 벤치마크 합성(Fuzzle), 오류 메시지로 문법을 추론하는 어셈블러 시험(AsFuzzer).[^p1][^p2][^p3][^p4]

### 2. 바이너리 코드 분석과 재조립

재조립 도구의 오류 유형 정의와 오류 탐지(REASSESSOR), CET를 이용한 x86-64 바이너리의 재조립(SURI), 확률적 추론으로 바이너리의 함수 찾기(FunProbe).[^p5][^p6][^p7] 최근 논문 목록에는 Python과 이더리움 가상 머신 프로그램의 디컴파일 연구도 있다.[^pi][^news]

### 3. 부정행위·공격의 탐지와 공격 기법 연구

FPS 게임 에임봇을 이용자 쪽에서 탐지하는 BotScreen,[^p8] 익스플로잇 작성을 위한 도메인 특화 언어 PoE.[^pi][^news]

## 대표 논문

교수 누리집 Selected Publications 목록과 연구실 News 페이지의 2021–2026년 논문 가운데 차상길 교수가 저자인 학회 논문을 앞의 세 연구 갈래에 고르게 담도록 골랐고, 교수가 마지막 저자인 논문을 우선했다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pi] |
|---|---|---|---|---|
| 1 | 2021 | [NTFuzz: Enabling Type-Aware Kernel Fuzzing on Windows with Static Binary Analysis](https://doi.org/10.1109/sp40001.2021.00114) · 2021 IEEE Symposium on Security and Privacy (SP) | 커널 퍼저는 시스템 호출의 형식(타입) 정보를 활용하는 것이 흔한 관행이지만, Windows는 시스템 호출 대부분이 공개되지 않고 문서도 거의 없어 기존 Windows 커널 퍼저는 이 관행을 따르지 못했다. 이 논문은 Windows의 시스템 호출 형식을 대규모로 자동 추론하는 실용적인 정적 바이너리 분석기를 만들고, 이를 형식 정보를 쓰는 Windows 커널 퍼징 틀 NTFuzz에 넣었다. 저자들은 이것이 상용 운영체제(COTS OS)에서 확장 가능한 바이너리 분석을 활용하는 첫 실용 퍼징 시스템이라고 적는다. NTFuzz로 알려지지 않았던 커널 버그 11개를 찾았고, Microsoft의 버그 바운티(취약점을 찾아 알린 사람에게 보상하는 제도)에서 2만 5천 달러를 받아 커널 퍼저로서의 실용성을 확인했다.[^p1] | 1저자 Jaeseung Choi, 마지막 저자 차상길 |
| 2 | 2021 | [Smartian: Enhancing Smart Contract Fuzzing with Static and Dynamic Data-Flow Analyses](https://doi.org/10.1109/ase51524.2021.9678888) · 2021 36th IEEE/ACM International Conference on Automated Software Engineering (ASE) | 스마트 계약은 일반 소프트웨어와 달리 여러 거래(transaction)가 이어지며 계속 남는 상태를 함께 쓰는 독특한 구조라, 기존 퍼저는 중요한 거래 순서를 찾아내기 어렵다. 이 논문은 스마트 계약 퍼징에 정적 분석과 동적 분석을 함께 썼다. 먼저 스마트 계약 바이트코드를 정적으로 분석해 어떤 거래 순서가 효과적인 시험으로 이어질지 예측하고 각 거래가 만족해야 할 조건이 있는지 알아낸 뒤, 이 정보로 처음 시험 입력 묶음(초기 시드)을 만든다. 퍼징 중에는 가벼운 동적 데이터 흐름 분석으로 데이터 흐름에 기반한 피드백을 모아 퍼징을 이끈다. 이를 공개 소스 퍼저 Smartian으로 구현했고, Smartian은 소스 코드 없이 실제 스마트 계약의 버그를 찾을 수 있다. 실험에서 실제 계약에 있는 알려진 CVE(번호가 매겨져 공개된 보안 취약점)를 찾는 데 기존 최신 도구들보다 효과적이었고, 코드 커버리지(시험 중 실행된 코드의 범위)에서도 앞섰다.[^p2] | 1저자 Jaeseung Choi, 마지막 저자 차상길 |
| 3 | 2022 | [Fuzzle: Making a Puzzle for Fuzzers](https://doi.org/10.1145/3551349.3556908) · Proceedings of the 37th IEEE/ACM International Conference on Automated Software Engineering | 퍼징 기술이 빠르게 발전하면서 버그가 든 프로그램을 자동으로 합성하려는 수요가 커졌다. 기존 방법은 기존 프로그램에 버그를 심는 데 집중해, 만든 프로그램에 예상하지 못한 버그가 섞일 수 있어 정답(ground truth)을 주기 어려웠다. 이 논문은 버그 합성 문제를 미로 생성 문제로 바꾸었다. 미로 안의 이동 순서를 함수 호출의 사슬로 부호화해 버그가 든 프로그램 전체를 합성하므로, 설계상 합성한 벤치마크의 정확한 정답을 준다. 실제 취약점에서 뽑은 현실적인 경로 조건을 담은 벤치마크도 만들 수 있다. 이 생각을 도구 Fuzzle로 구현하고 최신 퍼저 다섯 개로 평가해 그 가치를 실증했다.[^p3] | 1저자 Haeun Lee, 마지막 저자 차상길 |
| 4 | 2024 | [AsFuzzer: Differential Testing of Assemblers with Error-Driven Grammar Inference](https://doi.org/10.1145/3650212.3680345) · Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis | 어셈블러는 컴파일러 도구 사슬의 핵심 구성 요소인데도 다른 구성 요소보다 덜 시험되어 왔다. 기존 문법 기반 퍼징 기법으로 어셈블러를 시험하기에는 어려움이 있다. 어셈블러마다 받아들이는 문법 규칙과 구문이 다르고 어셈블리 문법 명세가 없으며, 모든 어셈블러가 공개 소스가 아니라 소스 코드에서 문법 규칙을 뽑아내기도 어렵다. 이런 비공개 어셈블러에 쓸 수 있는 기존 블랙박스 문법 추론 방법은 확장성 문제로 어셈블러 시험에 쓰기 어렵다. 이 논문은 어셈블리 오류 메시지가 바탕 문법 규칙을 추론할 유용한 정보를 자주 담는다는 통찰에서 출발해, 대상 어셈블러에 몇 번만 물어보고 오류 메시지를 이용해 문법 규칙을 자동 추론하는 새 시험 방법을 제안했다. 이를 AsFuzzer로 구현해 Clang 통합 어셈블러(Clang), GNU 어셈블러(GAS), Intel 어셈블러(ICC), Microsoft 매크로 어셈블러(MASM)의 실제 어셈블러 4개로 평가했고, 널리 쓰이는 여섯 가지 프로세서 구조에서 버그가 있는 명령어 연산 코드(opcode) 497개를 찾아 개발자에게 알렸다.[^p4] | 1저자 Hyungseok Kim, 마지막 저자 차상길 |
| 5 | 2023 | [Reassembly is Hard: A Reflection on Challenges and Strategies](https://www.usenix.org/conference/usenixsecurity23/presentation/kim-hyungseok) · 32nd USENIX Security Symposium (USENIX Security 23) | 정적 바이너리 재작성의 한 갈래인 재조립은 오늘날 연구의 초점이 되었지만, 널리 쓰이고 관심도 많은데도 재조립 도구(reassembler)의 기법과 어려움을 체계적으로 살핀 연구는 없었다. 이 논문은 현재 재조립 도구들에서 생기는 오류의 여러 유형을 형식적으로 정의하고, 그런 오류를 찾는 자동 도구 REASSESSOR를 내놓았다. 이 도구와 저자들이 만든 대규모 벤치마크로 이 분야의 현재 어려움과 그 해결 방향을 보이려 했다.[^p5] | 1저자 Hyungseok Kim, 마지막 저자 차상길 |
| 6 | 2025 | [Towards Sound Reassembly of Modern x86-64 Binaries](https://doi.org/10.1145/3676641.3716026) · Proceedings of the 30th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 2 | 재조립은 소스 코드 없이 바이너리를 투명하게 고쳐 쓰는 유망한 방법이지만, 바이너리 안의 모든 메모리 참조를 정확히 찾아야 하는 건전한 기호화(sound symbolization)는 아직 풀리지 않은 문제다. 이 논문은 최신 x86-64 바이너리를 건전하게 재조립하기 위한 요구 조건을 체계적으로 연구하고, 원래 의미를 해치지 않으면서 모든 메모리 참조를 기호화하는 새 재조립 방법을 제시했다. 핵심 통찰은 두 가지다. 하나는 주요 리눅스 배포판의 기본 설정이 되어 가는 CET가 바이너리에 독특한 성질을 더해, 실행 중에 계산되는 포인터를 정확히 기호화하는 데 쓸 수 있다는 점이다. 다른 하나는 간접 분기(실행 중에 계산한 주소로 건너뛰는 명령)가 갈 수 있는 곳을 넉넉하게 잡아(과대 근사) 가능한 모든 메모리 참조를 포함하는 집합을 기호화 대상으로 삼는 것이다. 이 통찰로 새 재조립 도구 SURI를 설계·구현하고 실제 바이너리 9,600개에서 효과를 보였다.[^p6] | 1저자 Hyungseok Kim, 마지막 저자 차상길 |
| 7 | 2023 | [FunProbe: Probing Functions from Binary Code through Probabilistic Analysis](https://doi.org/10.1145/3611643.3616366) · Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering | 현재의 함수 식별 기법은 대부분 특정 CPU 구조용으로 컴파일된 특정 바이너리 집합에 맞춰져 있다. 최근의 딥러닝 기반 방법은 이론상 여러 구조의 바이너리를 다룰 수 있지만 학습과 추론에 계산 자원이 많이 들어 실용성이 떨어지고, 모델을 해석하기 어려워 그로부터 통찰을 얻기도 근본적으로 어렵다. 이 논문은 확률적 추론으로 바이너리에서 함수를 찾아내는 효율적인 시스템 FunProbe를 제안했다. CPU 구조에 묶이지 않는 함수 식별 단서 16가지를 찾고, 이를 확률적 틀 안에서 효과적으로 묶는 방법을 고안했다. 주요 CPU 구조 여섯 가지용으로 컴파일된 실제 바이너리 1만 9,872개로 이루어진 대규모 데이터셋에서 평가한 결과, 시험한 최신 도구 다섯 개와 견주어 가장 높은 정확도를 보였고 바이너리 하나를 분석하는 데 평균 6초가 걸렸다. 추론 단계에 GPU를 쓰는 최신 딥러닝 도구 XDA보다 함수 식별이 평균 6배 빨랐다.[^p7] | 1저자 Soomin Kim, 마지막 저자 차상길 |
| 8 | 2023 | [BotScreen: Trust Everybody, but Cut the Aimbots Yourself](https://www.usenix.org/conference/usenixsecurity23/presentation/choi) · 32nd USENIX Security Symposium (USENIX Security 23) | 1인칭 슈팅(FPS) 게임에서 플레이어가 상대를 쓰러뜨리도록 돕는 에임봇은 게임 산업에 상당한 위협이다. 에임봇을 자동으로 탐지하려는 연구가 많았지만 기존 연구는 서버 쪽 부담이 크거나 탐지 정확도가 낮았다. 이 논문은 인기 FPS 게임 Counter-Strike: Global Offensive(CS:GO)를 위한 이용자 컴퓨터(클라이언트) 쪽 에임봇 탐지 방법 BotScreen을 설계·구현했다. BotScreen은 에임봇을 분산 방식으로 탐지하는 첫 방법으로 서버 쪽 부담을 최소화하고, 새 딥러닝 모델로 에임봇 사용이 일으키는 비정상 행동을 정밀하게 탐지한다. CS:GO에서 정확도와 성능 양쪽의 효과를 보였고, 공개 과학을 지원하려고 도구와 데이터셋을 공개했다.[^p8] | 1저자 Minyeop Choi, 마지막 저자 차상길 |

## 교수와 전문 분야

차상길 교수는 Carnegie Mellon University에서 박사 학위를 받았다. 전산학부 교수 소개는 학위를 「박사, 카네기멜론 대학교, 2015」로 적고, 교수 누리집 논문 목록은 박사 논문을 「Towards Resource-Aware Security Testing of Software」(Ph.D. Thesis, Carnegie Mellon University, 2015)로 적는다.[^csfac][^pi] 교수 누리집은 교수를 KAIST 사이버보안연구센터(CSRC, Cyber Security Research Center) 센터장이자 정보보호대학원·전산학부 부교수(Associate Professor)로 적고,[^pi][^pikr] 전산학부 교수 소개의 직위 칸은 「교수」다.[^csfac] 연구실 News 페이지(2025년 7월)는 교수가 CSRC 센터장이자 정보보호대학원 책임교수(chief professor)로서 국내 보안 연구 발전에 이바지한 공로로 MSIT Minister Prize for Information Security를 받았다고 적는다.[^news] 전산학부 교수 소개의 전공 칸은 「소프트웨어 보안, 프로그램 분석」이고 연구분야 칸은 시스템·네트워크, 소프트웨어 디자인, 시큐어 컴퓨팅이며,[^csfac] 정보보호대학원 교수진 목록도 교수의 분야를 「소프트웨어 보안, 프로그램 분석」으로 적는다.[^gsisfac]

교수 소개는 교수를 컴퓨터 기반의 실험과학자로 소개하고, 주 연구 분야가 소프트웨어 보안과 프로그램 분석이며 연구가 컴퓨터 보안과 소프트웨어 공학의 교차점에 있다고 적는다.[^pikr][^csfac] 전산학부 교수 소개는 교수가 2014년과 2020년에 취약점 자동 탐지에 관한 논문으로 ACM distinguished paper award를 받았다고 적는다.[^csfac] 교수 누리집 논문 목록은 ICSE 2014 논문 「Enhancing Symbolic Execution with Veritesting」과 FSE 2020 논문 「Boosting Fuzzer Efficiency: An Information Theoretic Perspective」에 ACM Distinguished Paper Award를, NDSS Workshop on Binary Analysis Research 2019 논문 「B2R2: Building an Efficient Front-End for Binary Analysis」에 Best Paper Award를 표시한다.[^pi] 연구실 News 페이지는 교수가 2022년 5월 IEEE Security & Privacy Test-of-Time Award를, 2021년 12월 국내 사이버보안 전문 인력을 길러 낸 공로로 MSIT Minister Prize for Cybersecurity Education을, 2025년 12월 Cybersecurity Enhancement Conference에서 Certificate of Merit in Academic Achievement를 받았다고 알린다.[^news] 같은 페이지는 2025년 2월과 4월에 교수가 서울에서 열리는 제28회 Information Security Conference(ISC 2025)와 ASE NIER 2025의 TPC Chair(프로그램 위원장)를 맡는다고 알렸다.[^news]

교수 누리집 Teaching 칸은 정보보호대학원 과목 「Binary Code Analysis and Secure Software Systems」(IS-50601, 2016년 봄–2026년 가을 9개 학기), 「Advanced Software Security」(IS-893), 「Introduction to Information Security」(IS-511), 「Information Security Laboratory」(IS-521)와 전산학부 과목 「Programming Principles」(CS-20200), 「Introduction to Software Security」(CS-492E), 「Computer Science Project」(CS-40008)를 학기 표기와 함께 적는다.[^pi]

교수 누리집 논문 목록을 시기별로 보면, 2010–2015년 항목은 분산 악성코드 탐지(SplitScreen, NSDI 2010), 자동 익스플로잇 생성(AEG, NDSS 2011과 Communications of the ACM 2014), 「Unleashing Mayhem on Binary Code」(IEEE Symposium on Security and Privacy 2012), 기호 실행을 개선하는 Veritesting(ICSE 2014), 블랙박스 돌연변이 퍼징(mutational fuzzing, 기존 입력을 조금씩 바꿔 새 입력을 만드는 퍼징)의 일정 짜기(CCS 2013), 퍼징의 시드(seed, 퍼징이 변형을 시작하는 처음 입력) 선택 최적화(USENIX Security 2014), 프로그램에 맞춘 돌연변이 퍼징(IEEE Symposium on Security and Privacy 2015)을 제목에 단다. 2016–2020년 항목은 부분 메모리 덤프로 프로그램 충돌을 선별하는 RETracer(ICSE 2016), 바이너리 분석에 쓰는 중간 표현(intermediate representation, 분석 도구가 기계어를 옮겨 다루는 내부 표기)의 시험(ASE 2017), 추론한 모델에 기반한 퍼저 IMF(CCS 2017), 수업 안의 공격·방어 보안 대회를 운영하는 Git-based CTF(USENIX Workshop on Advances in Security Education 2018), 효율적인 바이너리 분석 앞단(front-end) B2R2(NDSS Workshop on Binary Analysis Research 2019), 바이너리 코드의 그레이박스(grey-box, 프로그램 내부 정보를 일부 관찰해 쓰는 방식) 콘콜릭 테스팅(concolic testing, 구체적인 입력으로 실행하면서 그 실행 경로의 조건을 기호로 모아 다른 경로로 갈 입력을 만드는 시험 기법, ICSE 2019), JavaScript 엔진의 취약점을 찾는 코드 생성 CodeAlchemist(NDSS 2019)와 신경망 언어 모델이 이끄는 JavaScript 엔진 퍼저 Montage(USENIX Security 2020), 그레이박스 퍼징을 이끄는 Ankou(ICSE 2020)를 제목에 단다.[^pi]

논문으로 보면 지금의 전문 분야는 세 갈래다. 첫째, Windows 커널·스마트 계약·어셈블러 같은 대상에 맞춘 퍼징과 퍼저 평가용 벤치마크다(대표 논문 1–4).[^p1][^p2][^p3][^p4] 둘째, 바이너리를 다시 조립할 수 있게 고쳐 쓰는 재조립과 바이너리의 함수 식별 같은 바이너리 코드 분석이다(대표 논문 5–7).[^p5][^p6][^p7] 셋째, 게임 부정 프로그램처럼 소프트웨어를 악용하는 행위의 탐지다(대표 논문 8).[^p8]

## 응용 분야

대표 논문은 Windows 운영체제 커널,[^p1] 블록체인 위의 스마트 계약,[^p2] 퍼저 평가용 벤치마크,[^p3] 컴파일러 도구 사슬의 어셈블러,[^p4] 소스 코드 없는 바이너리의 재작성,[^p5][^p6] 여러 CPU 구조용 바이너리의 함수 식별,[^p7] FPS 게임의 에임봇 탐지[^p8]를 대상으로 한다. NTFuzz로 찾은 커널 버그는 Microsoft의 버그 바운티 보상으로 이어졌다.[^p1] 연구실 News 페이지의 Black Hat USA 2024 소식은 Python 디컴파일 틀 PyLingual을 무료 온라인 서비스 <https://pylingual.io> 로 쓸 수 있다고 알린다.[^news] 최근 논문 목록에는 블록체인 합의 구현, 이더리움 가상 머신, 비행 소프트웨어를 대상으로 단 논문도 있다.[^pi][^news] 졸업생의 진로로는 서강대학교·충남대학교·이화여자대학교 조교수(assistant professor)와 KAIST 사이버보안연구센터(CSRC) 연구원(research scientist)이 있다.[^home][^news]

## 구성원

2026년 10월 25일 누리집 People 칸 기준이다. Ph.D. Students 칸 6명과 Master Students 칸 3명이며, 과정은 칸의 표기(Ph.D. Student, Master Student)를 옮겼다.[^home] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| JungHyun Kim | 박사과정 |  |
| Jungwoo Lee | 박사과정 | 4 |
| Steve Gustaman | 박사과정 |  |
| Geonwoo Park | 박사과정 |  |
| Sehoon Kim | 박사과정 |  |
| Minyeop Choi | 박사과정 | 8 |
| Dongwoo Kim | 석사과정 |  |
| Jinheon Lee | 석사과정 |  |
| HyungJoon Yoon | 석사과정 |  |

## 졸업생과 이전 구성원

누리집 첫 화면 Former Ph.D. Students 칸의 3명과, 연구실 News 페이지가 연구실에서 석사 학위(Master's degree)를 받았다고 적은 1명이다. 학위·과정 칸은 원문 표기이고 연도 표기는 없다. 진로는 News 페이지의 임용·합류 소식 표기와 그 소식의 월이다. Former Ph.D. Students 칸은 세 사람을 각각 now at Sogang University, now at Chungnam National University, now at Ewha Womans University로 적는다.[^home][^news]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jaeseung Choi | Former Ph.D. Student | assistant professor at Sogang University, Korea (2022년 9월 소식) |
| Hyungseok Kim | Former Ph.D. Student | assistant professor at Chungnam National University (CNU), Korea (2025년 9월 소식) |
| Soomin Kim | Former Ph.D. Student | assistant professor at Ewha Womans University, Korea (2026년 3월 소식) |
| Daeseok Kim | Master's degree | Cyber Security Research Center (CSRC) at KAIST, research scientist (2026년 3월 소식) |

## 최근 논문 목록 (2021–2026)

교수 누리집 Selected Publications 목록([1]–[36])의 2021–2025년 16편과, 연구실 News 페이지가 알린 논문 가운데 그 목록에 없는 2023–2026년 9편을 합한 25편이다(2026년 2편, 2025년 7편, 2024년 4편, 2023년 7편, 2022년 2편, 2021년 3편).[^pi][^news] 누리집 Publications 칸은 전체 논문 목록으로 DBLP와 Google Scholar 프로필을 가리킨다.[^home] 연도는 목록 표기의 연도이고, 제목·저자·학술지와 학회 이름은 원문 표기 그대로다. 괄호 안의 수상 표시는 교수 누리집 목록의 표기이고, News 페이지가 will appear로 알린 APSEC 2026 논문은 「채택」으로 표시했다.

**2026**

- HyungJoon Yoon and Sang Kil Cha. "BinForge: Facilitating Generation of Diversified Binary Datasets". *In Proceedings of the Asia-Pacific Software Engineering Conference, 2026 (채택)*.
- Geonwoo Park, Junhak Lee, and Sang Kil Cha. "LLM-Assisted Command Syntax Extraction for Flight Software Fuzzing". *In Proceedings of the World Conference on Information Security Applications, 2026*.

**2025**

- Josh Wiedemeier, Simon Klancher, Joel Flores, Max Zheng, Jaehyun Park, Sang Kil Cha, and Kangkook Jee. "Walking The Last Mile: Studying Decompiler Output Correction in Practice". *In Proceedings of the ACM Conference on Computer and Communications Security, 2025*.
- Won Hoi Kim, Hocheol Nam, Muoi Tran, Amin Jalilov, Zhenkai Liang, Sang Kil Cha, and Min Suk Kang. "Fork State-Aware Differential Fuzzing for Blockchain Consensus Implementations". *In Proceedings of the International Conference on Software Engineering, 2025*.
- Hyungseok Kim, Soomin Kim, and Sang Kil Cha. "Towards Sound Reassembly of Modern x86-64 Binaries". *In Proceedings of the International Conference on Architectural Support for Programming Languages and Operating Systems, 2025*.
- Josh Wiedemeier, Elliot Tarbet, Max Zheng, Sangsoo Ko, Jessica Ouyang, Sang Kil Cha, and Kangkook Jee. "PyLingual: Toward Perfect Decompilation of Evolving High-Level Languages". *In Proceedings of the IEEE Symposium on Security and Privacy, 2025*.
- Jung Hyun Kim, Soomin Kim, Jaeseung Choi, and Sang Kil Cha. "EVMpress: Precise Type Inference for Next-Generation EVM Decompilation". *In Proceedings of the International Workshop on Cryptocurrencies and Blockchain Technology, 2025*.
- Jungwoo Lee, Haeun Lee, Sangjun Park, and Sang Kil Cha. "On the Applicability of Benford's Law to Detect Saturation in Fuzzing". *In Proceedings of the International Workshop on Fuzzing, 2025*.
- Sanghyun Park, Haeun Lee, and Sang Kil Cha. "Systematic Bug Reproduction with Large Language Model". *In Proceedings of the International Conference on Software Engineering, 2025*.

**2024**

- Hyungseok Kim, Soomin Kim, Jungwoo Lee, and Sang Kil Cha. "AsFuzzer: Differential Testing of Assemblers with Error-Driven Grammar Inference". *In Proceedings of the International Symposium on Software Testing and Analysis, 2024 (ACM Distinguished Paper Award)*.
- Tae Eun Kim, Jaeseung Choi, Seongjae Im, Kihong Heo, and Sang Kil Cha. "Evaluating Directed Fuzzers: Are We Heading in the Right Direction?". *In Proceedings of the International Symposium on Foundations of Software Engineering, 2024*.
- Josh Wiedemeier, Elliot Tarbet, Max Zheng, Jerry Teng, Ximeng Liu, Muhyun Kim, Sang Kil Cha, Jessica Ouyang, and Kangkook Jee. "PyLingual: A Python Decompilation Framework for Evolving Python Versions". *In Proceedings of the Black Hat USA, 2024*.
- Jung Hyun Kim, Steve Gustaman, and Sang Kil Cha. "PoE: A Domain-Specific Language for Exploitation". *In Proceedings of the Silicon Valley Cybersecurity Conference, 2024*.

**2023**

- Soomin Kim, Hyungseok Kim, and Sang Kil Cha. "FunProbe: Probing Functions from Binary Code through Probabilistic Analysis". *In Proceedings of the International Symposium on Foundations of Software Engineering, 2023*.
- Tae Eun Kim, Jaeseung Choi, Kihong Heo, and Sang Kil Cha. "DAFL: Directed Grey-box Fuzzing Guided by Data Dependency". *In Proceedings of the USENIX Security Symposium, 2023*.
- Minyeop Choi, Gihyuk Ko, and Sang Kil Cha. "BotScreen: Trust Everybody, but Cut the Aimbots Yourself". *In Proceedings of the USENIX Security Symposium, 2023 (USENIX Distinguished Paper Award)*.
- Hyungseok Kim, Soomin Kim, Junoh Lee, Kangkook Jee, and Sang Kil Cha. "Reassembly is Hard: A Reflection on Challenges and Strategies". *In Proceedings of the USENIX Security Symposium, 2023*.
- Dongkwan Kim, Eunsoo Kim, Sang Kil Cha, Sooel Son, and Yongdae Kim. "Revisiting Binary Code Similarity Analysis using Interpretable Feature Engineering and Lessons Learned". *IEEE Transactions on Software Engineering, vol. 49, no. 4, 2023*.
- Haeun Lee, Hee Dong Yang, Su Geun Ji, and Sang Kil Cha. "On the Effectiveness of Synthetic Benchmarks for Evaluating Directed Grey-box Fuzzers". *In Proceedings of the Asia-Pacific Software Engineering Conference, 2023*.
- Marcel Böhme, Valentin Jean Marie Manès, and Sang Kil Cha. "Boosting Fuzzer Efficiency: An Information Theoretic Perspective". *CACM, Volume 66, Issue 11, Nov. 2023*.

**2022**

- Haeun Lee, Soomin Kim, and Sang Kil Cha. "Fuzzle: Making a Puzzle for Fuzzers". *In Proceedings of the IEEE/ACM International Conference on Automated Software Engineering, 2022 (ACM Distinguished Paper Award)*.
- Hyungseok Kim, Junoh Lee, Soomin Kim, Seungil Jung, and Sang Kil Cha. "How'd Security Benefit Reverse Engineers? The Implication of Intel CET on Function Identification". *In Proceedings of the International Conference on Dependable Systems Networks, 2022*.

**2021**

- Jaeseung Choi, Doyeon Kim, Soomin Kim, Gustavo Grieco, Alex Groce, and Sang Kil Cha. "Smartian: Enhancing Smart Contract Fuzzing with Static and Dynamic Data-Flow Analyses". *In Proceedings of the IEEE/ACM International Conference on Automated Software Engineering, 2021*.
- Jaeseung Choi, Kangsu Kim, Daejin Lee, and Sang Kil Cha. "NTFuzz: Enabling Type-Aware Kernel Fuzzing on Windows with Static Binary Analysis". *In Proceedings of the IEEE Symposium on Security and Privacy, 2021*.
- Valentin Jean Marie Manès, HyungSeok Han, Choongwoo Han, Sang Kil Cha, Manuel Egele, Edward J. Schwartz, and Maverick Woo. "The Art, Science, and Engineering of Fuzzing: A Survey". *IEEE Transactions on Software Engineering, vol. 47, no. 11, 2021 (Best Paper Award)*.

## 수상

연구실 News 페이지의 수상 소식 9건이다(2021년 12월–2026년 8월). 날짜는 소식의 월 표기이고, 문장은 소식 제목 그대로이며, 괄호 안은 소식이 함께 적은 논문 제목이나 행사 이름이다. ISSTA 2024와 IEEE TSE 수상 소식의 논문 이름은 교수 누리집 목록의 수상 표시에서 적었다.[^news][^pi]

- Aug. 2026 · Received Best Paper Award in WISA 2026 (LLM-Assisted Command Syntax Extraction for Flight Software Fuzzing)
- Dec. 2025 · Prof. Cha received the Certificate of Merit in Academic Achievement (Cybersecurity Enhancement Conference, Korea)
- Jul. 2025 · Prof. Cha received the MSIT Minister Prize for Information Security (Information Security Day, Korea)
- Sep. 2024 · Received ACM Distinguished Paper Award in ISSTA 2024! (AsFuzzer: Differential Testing of Assemblers with Error-Driven Grammar Inference)
- Aug. 2023 · Received USENIX Security '23 Distinguished Paper Award (BotScreen: Trust Everybody, but Cut the Aimbots Yourself)
- Dec. 2022 · Our paper is awarded the IEEE TSE Best Paper Award (The Art, Science, and Engineering of Fuzzing: A Survey)
- Oct. 2022 · Our paper is awarded the SIGSOFT ACM Distinguished Paper Award in ASE'22 (Fuzzle: Making a Puzzle for Fuzzers)
- May. 2022 · Prof. Cha received IEEE Security & Privacy Test-of-Time Award
- Dec. 2021 · Prof. Cha received the MSIT Minister Prize for Cybersecurity Education (For training professional cybersecurity experts in Korea)

## 소식

연구실 News 페이지 가운데 논문 채택·게재 소식 17건, 교수의 학회 프로그램 위원장(TPC Chair) 소식 2건, SIGSOFT Research Highlight 선정 소식 1건, 모두 20건이다(2022년 7월–2026년 8월). 날짜는 소식의 월 표기이고, 문장은 소식 제목 그대로이며, 괄호 안은 소식이 함께 적은 논문 제목이다.[^news]

- Aug. 2026 · Our paper will appear in NDSS'27 (Capture The Flag: Exploiting Compilation Flags to Summon Trojan Horses)
- Oct. 2025 · Our paper will appear in CCS 2025 (Walking The Last Mile: Studying Decompiler Output Correction in Practice)
- Sep. 2025 · Our paper will appear in CBT 2025 (EVMpress: Precise Type Inference for Next-Generation EVM Decompilation)
- May. 2025 · Our paper will appear in FUZZING'25 (On the Applicability of Benford's Law to Detect Saturation in Fuzzing)
- Apr. 2025 · Prof. Cha is serving as a TPC Chair of ASE NIER 2025
- Apr. 2025 · A short paper published in Springer LNCS (Systematic Bug Reproduction with Large Language Model)
- Mar. 2025 · Our work will appear in ICSE 2025 (Fork State-Aware Differential Fuzzing for Blockchain Consensus Implementations)
- Feb. 2025 · Our work will appear in ASPLOS 2025 (Towards Sound Reassembly of Modern x86-64 Binaries)
- Feb. 2025 · Prof. Cha is serving as a TPC Chair of ISC 2025
- Nov. 2024 · Our work will appear in Oakland 2025 (PyLingual: Toward Perfect Decompilation of Evolving High-Level Languages)
- Jul. 2024 · Our work will appear in ISSTA 2024 (AsFuzzer: Differential Testing of Assemblers with Error-Driven Grammar Inference)
- Jun. 2024 · Our work will appear in Black Hat USA 2024 (PyLingual: A Python Decompilation Framework for Evolving Python Versions)
- Jun. 2024 · Jung Hyun will present a poster in SVCC 2024 (PoE: A Domain-Specific Language for Exploitation)
- May. 2024 · A paper will appear in FSE 2024 (Evaluating Directed Fuzzers: Are We Heading in the Right Direction?)
- Nov. 2023 · A paper will appear in APSEC 2023 (On the Effectiveness of Synthetic Benchmarks for Evaluating Directed Grey-box Fuzzers)
- Oct. 2023 · An article will appear in CACM (Boosting Fuzzer Efficiency: An Information Theoretic Perspective)
- Aug. 2023 · A paper will appear in FSE 2023 (FunProbe: Probing Functions from Binary Code through Probabilistic Analysis)
- Jul. 2023 · Two more papers got accepted at USENIX Security 2023.
- Nov. 2022 · Our paper will appear in USENIX Security 2023 (Reassembly is Hard: A Reflection on Challenges and Strategies)
- Jul. 2022 · Our paper has been selected as SIGSOFT Research Highlight

## 연락과 위치

- 연구실: KAIST N5 #2310, 291 Daehak-ro, Yuseong-gu, Daejeon 34141, South Korea(누리집 표기)[^home]
- 연구실 사무실: N5 2310호, 전화 042-350-3569(전산학부 연구실 소개 표기)[^cslab]
- 교수연구실: N5동 2319호, 전화 +82-42-350-3569[^pi][^pikr][^csfac]
[^home]: 연구실 누리집 첫 화면 <https://softsec.kaist.ac.kr/> (연구 소개, News, People, Former Ph.D. Students, Publications, Contact 칸, 2026-10-25 열람)
[^news]: 연구실 News 페이지 <https://softsec.kaist.ac.kr/news.html> (SoftSec Lab News Archive, 2026-10-25 열람)
[^intern]: 연구실 인턴십 안내 페이지 <https://softsec.kaist.ac.kr/intern.html> (2026-10-25 열람)
[^pi]: 교수 누리집 <https://softsec.kaist.ac.kr/~sangkilc/> (소속, About Me, Teaching, Selected Publications 칸, 2026-10-25 열람)
[^pikr]: 교수 누리집 한국어 페이지 <https://softsec.kaist.ac.kr/~sangkilc/index.kr.html> (소속, 소개, 수업 칸, 2026-10-25 열람)
[^csfac]: KAIST 전산학부 교수 소개(차상길) <https://cs.kaist.ac.kr/people/view?idx=527&kind=faculty&menu=160> (2026-10-25 열람)
[^cslab]: KAIST 전산학부 연구실 소개(소프트웨어 보안 연구실) <https://cs.kaist.ac.kr/research/labView?sn=98&menu=64> (2026-10-25 열람)
[^gsisfac]: KAIST 정보보호대학원 교수진 목록 <https://gsis.kaist.ac.kr/people/faculty> (2026-10-25 열람)
[^gsislab]: KAIST 정보보호대학원 연구실 목록 <https://gsis.kaist.ac.kr/research/center> (Software Security (SoftSec) Lab 항목, 2026-10-25 열람)
[^p1]: J. Choi, K. Kim, D. Lee, S. K. Cha, 2021 IEEE Symposium on Security and Privacy (SP), 677-693 (2021). <https://doi.org/10.1109/sp40001.2021.00114> 초록 기준(OpenAlex 등록 초록).
[^p2]: J. Choi 외, S. K. Cha, 2021 36th IEEE/ACM International Conference on Automated Software Engineering (ASE), 227-239 (2021). <https://doi.org/10.1109/ase51524.2021.9678888> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: H. Lee, S. Kim, S. K. Cha, Proceedings of the 37th IEEE/ACM International Conference on Automated Software Engineering, 1-12 (온라인 2023-01-05). <https://doi.org/10.1145/3551349.3556908> 초록 기준(OpenAlex 등록 초록).
[^p4]: H. Kim, S. Kim, J. Lee, S. K. Cha, Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis, 1099-1111 (온라인 2024-09-11). <https://doi.org/10.1145/3650212.3680345> 초록 기준(OpenAlex 등록 초록).
[^p5]: H. Kim 외, S. K. Cha, 32nd USENIX Security Symposium (USENIX Security 23), 1469-1486 (2023). <https://www.usenix.org/conference/usenixsecurity23/presentation/kim-hyungseok> 초록 기준(학회 논문집 페이지 게시 초록).
[^p6]: H. Kim, S. Kim, S. K. Cha, Proceedings of the 30th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 2, 1317-1333 (온라인 2025-03-30). <https://doi.org/10.1145/3676641.3716026> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: S. Kim, H. Kim, S. K. Cha, Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering, 1419-1430 (온라인 2023-11-30). <https://doi.org/10.1145/3611643.3616366> 초록 기준(OpenAlex 등록 초록).
[^p8]: M. Choi, G. Ko, S. K. Cha, 32nd USENIX Security Symposium (USENIX Security 23), 481-498 (2023). <https://www.usenix.org/conference/usenixsecurity23/presentation/choi> 초록 기준(학회 논문집 페이지 게시 초록).

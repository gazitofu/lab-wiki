# 암호론 연구실 (Cryptology (Crypt) Lab)

**KAIST 전산학부·정보보호대학원 · 이주영 부교수**

- 분야: 대칭키 암호의 증명 가능한 안전성(인증 암호화와 메시지 인증 코드, 결정론적 난수 발생기), 동형 암호와 함께 쓰는 대칭키 암호 설계, 대칭키 암호 부품에 바탕을 둔 양자 내성 전자서명과 영지식 증명 친화 해시 함수, 조합론
- 대분야: 컴퓨팅·AI, 수학·통계
- 태그: 양자 컴퓨팅[^tc22], 암호학[^cslab]
- 홈페이지: <https://sites.google.com/view/cryptlab/home>
- 근거와 출처: [암호론 연구실 근거 페이지](cryptlab-sources.md)

> 대칭키 암호의 증명 가능한 안전성을 연구하는 KAIST 전산학부·정보보호대학원 이주영 교수의 연구실로, 인증 암호화 같은 운용 모드와 아코디언 암호를 설계해 그 안전성을 증명하고, 대칭키 암호 부품에 바탕을 둔 양자 내성 암호도 연구한다.[^home][^gsislab] 2021–2026년 논문은 인증 암호화와 메시지 인증 코드, 결정론적 난수 발생기, 동형 암호와 함께 쓰는 대칭키 암호, 양자 내성 전자서명과 영지식 증명 친화 해시 함수를 다룬다.[^home][^p1][^p3][^p5][^p8]

## 무엇을 연구하나

연구실은 KAIST 전산학부 이주영 교수가 이끄는 암호론 연구실이다. 전산학부 연구실 소개 페이지는 이름을 「암호론 연구실」로, 연구 분야를 전산이론과 시큐어 컴퓨팅으로 적고,[^cslab] 정보보호대학원 연구실 목록은 암호학 분야에 「Cryptology (Crypt) Lab」을 올리며 분야를 Cryptology / Information Security / Combinatorics로 적는다.[^gsislab] 누리집 첫 화면은 연구실이 대칭키 암호(암호화와 복호화에 같은 비밀 키를 쓰는 암호)의 증명 가능한 안전성(정해진 공격 모형과 가정 아래에서 암호 방식의 안전성을 수학적으로 증명하는 접근)을 연구한다고 소개한다. 인증 암호화 운용 모드와 아코디언 암호 같은 여러 운용 모드(기본 암호 부품을 되풀이해 써서 길이가 다양한 메시지를 처리하는 방식)를 설계하고 그 안전성을 증명하며, 대칭키 암호 부품에 바탕을 둔 양자 내성 암호(양자 컴퓨터를 이용한 공격에도 안전하도록 설계한 암호)도 탐구한다고 적는다.[^home]

전산학부 연구실 소개 페이지는 연구실이 암호학의 여러 주제를 주로 증명 가능한 안전성의 관점에서 연구하며, 이미 설계된 암호 알고리즘의 안전성을 분석하고, 증명 가능한 안전성과 효율성을 함께 제공하는 암호 알고리즘과 프로토콜을 설계한다고 적는다.[^cslab] 연구 항목은 두 갈래다. 「비밀키 암호 안전성 증명」 아래에는 블록 암호(정해진 길이의 데이터 덩어리를 비밀 키로 암호화하는 대칭키 암호)의 구조와 키 확장 방식의 안전성 증명, 블록 암호나 치환 함수에 바탕을 둔 해시 함수와 운용 모드의 설계와 안전성 증명을 둔다. 「양자 내성 암호 연구」 아래에는 화이트박스 암호의 설계와 분석, 대칭키 암호 기반 양자 내성 암호 알고리즘의 설계와 안전성 분석, 동형암호와 대칭키 암호를 결합한 구조와 동형암호에 알맞은 대칭키 암호 알고리즘의 설계를 둔다.[^cslab] 정보보호대학원 연구실 목록은 여기에 일방향 해시 함수(결과에서 입력을 되찾기 어려운 해시 함수) 기반 전자서명과 오류 정정 부호 기반 공개키 암호 시스템 같은 양자 내성 암호 연구를 더 적는다.[^gsislab]

누리집 논문 목록에 실린 2021–2026년 논문 23편은 크게 네 갈래다. 첫째는 인증 암호화와 메시지 인증 코드(MAC, 비밀 키로 계산해 메시지에 붙여서, 메시지가 바뀌지 않았고 키를 가진 쪽이 만들었음을 확인하게 하는 값)의 설계와 안전성 증명이다(대표 논문 1, 2).[^p1][^p2] 둘째는 결정론적 난수 발생기(DRBG, 예측하기 어려운 입력으로 내부 상태를 정한 뒤 정해진 계산 규칙으로 무작위처럼 보이는 비트열을 만들어 내는 알고리즘)의 안전성 증명으로, Linux 운영체제에 쓰이는 난수 발생기와 국제 표준의 난수 발생기를 다룬다(대표 논문 3, 4).[^p3][^p4][^ofb] 셋째는 동형 암호와 함께 쓰도록 설계한 대칭키 암호이고(대표 논문 5, 6),[^p5][^p6] 넷째는 대칭키 암호 부품의 안전성에만 기대는 양자 내성 전자서명과 영지식 증명에 알맞은 해시 함수다(대표 논문 7, 8).[^p7][^p8] 이 밖에 2022년 학술지 논문은 블록 암호가 그로버 탐색 알고리즘을 쓰는 양자 공격에 얼마나 견디는지는 그 알고리즘에서 대상 암호를 계산하는 부분을 구현하는 양자 회로(양자 컴퓨터에서 실행할 연산을 차례로 늘어놓은 계산 절차)에 드는 자원으로 평가한다는 점에서 출발해, AES의 S-box를 양자 회로로 구현하는 방법 세 가지를 계산 시간과 큐비트 수를 맞바꾸는 방식으로 제안했다.[^tc22]

KAIST 전산학부 소식은 2025년 8월 이주영 교수 연구팀이 결정론적 난수 발생기의 새 설계 방식을 개발했다고 전한다. 기존의 직렬 처리 방식을 병렬 처리 구조로 바꾸어 치환 기반 결정론적 난수 발생기의 최대 효율을 구현했고, 안전성 검증 과정을 2단계로 단순화한 새 방식으로 기존보다 약 50% 향상된 안전성을 입증했다고 적는다.[^drbg] 2025년 2월 소식은 연구팀이 삼성SDS와 공동 개발한 전자서명 알고리즘 AIMer가 2025년 1월 국가정보원과 국가보안기술연구소가 주관한 양자내성암호(PQC) 국가공모전에서 전자서명 부문 최종 알고리즘으로 선정되었다고 알린다.[^aimer]

## 주요 연구 주제

### 1. 인증 암호화와 메시지 인증 코드의 증명 가능한 안전성

블록 암호로 메시지를 숨기고 위조를 막는 운용 모드를 설계하고, 그 안전성이 어디까지 보장되는지를 증명하는 연구다. 대표 논문 1은 세계에서 가장 널리 쓰이는 인증 암호화 방식의 하나인 GCM이 논스 오용의 위험, 한 번에 암호화할 수 있는 메시지 길이의 제약, 모자란 안전성 수준이라는 문제를 안고 있다고 보고, GCM의 설계 원리를 따르면서 더 강한 안전성을 증명할 수 있고 더 긴 논스를 받아들이는 변형 eGCM과 eGCM-SIV를 제안했다. 두 방식은 효율을 크게 잃지 않고 생일 한계를 넘는 안전성을 얻는 새 암호화 모드 eCTR 위에 세웠다.[^p1] 대표 논문 2는 블록 암호로 만드는 MAC 구성 네 가지가 같은 논스를 되풀이하지 않는 조건에서 MAC 질의(공격자가 메시지를 넣고 그 MAC 값을 받아 보는 일) 2^n번까지 완전히 안전함을 증명해, 이전의 3n/4비트 안전성 한계를 높였다.[^p2] 논문 목록에는 이 밖에 생일 한계를 넘는 안전성을 갖춘 인증 암호화 모드 XOCB(Eurocrypt 2023), 완전한 안전성을 갖춘 온라인 인증 암호화 방식 ZLR(Designs, Codes and Cryptography 2024), 의사난수 순열에 바탕을 둔 완전 안전 인증 암호화 방식을 다룬 논문(Asiacrypt 2021), 의사난수 순열 하나로 생일 한계를 넘는 안전성을 얻는 조정 가능한 암호화 방식 CTET+(IACR Transactions on Symmetric Cryptology 2021)가 있고, 아코디언 암호의 안전성을 다룬 논문이 Asiacrypt 2026에 채택되어 있다.[^home]

### 2. 결정론적 난수 발생기의 안전성 증명

결정론적 난수 발생기는 현대 암호에서 안전하고 예측할 수 없는 난수를 만드는 데 쓰인다.[^ofb] 이런 난수 발생기가 얼마나 많은 질의까지 안전한지를 증명하고, 그 한계에 맞는 공격을 보여 증명이 빈틈없음을 확인하는 연구다. 대표 논문 4는 Linux 6.4.8의 난수 발생기를 Linux 4와 Linux 5.17에서 구조가 크게 바뀐 뒤 처음으로 증명 가능한 안전성 관점에서 분석해, 내부 부품의 출력 크기와 엔트로피 원천의 최소 엔트로피에 따라 정해지는 질의 수까지 안전함을 증명했다.[^p4] 대표 논문 3은 스펀지 구조에 바탕을 둔 치환 기반 난수 발생기의 안전성 한계를 생일 한계까지 끌어올리고, 같은 수준의 안전성을 유지하면서 출력률을 거의 1로 높인 새 난수 발생기 POSDRBG를 제안했다.[^p3] KAIST 전산학부 소식이 2025년 8월에 소개한 난수 발생기 성과의 사진 설명은 대표 논문 3의 저자 네 사람을 적는다.[^drbg] 2024년 학술지 논문은 ISO의 난수 발생기 표준에 든 네 알고리즘 가운데 따로 안전성 분석이 없던 OFB-DRBG의 안전성을 증명했고,[^ofb] 논문 목록에는 NIST SP800-90A의 해시 기반 난수 발생기를 다룬 Euro S&P 2026 논문도 있다.[^home]

### 3. 동형 암호와 함께 쓰는 대칭키 암호

트랜스사이퍼링 틀은 클라이언트가 대칭키 암호로 암호화한 자료를 서버가 동형 암호문으로 바꾸어, 클라이언트 쪽의 계산·통신 부담을 줄이는 방법이다. 이때 서버가 대칭키 암호를 동형 연산으로 계산해야 하므로, 동형 암호의 특성에 맞춘 새 대칭키 암호가 필요하다.[^p5][^p6] 연구실 논문 목록에는 근사 동형 암호를 위한 트랜스사이퍼링 틀을 다룬 Asiacrypt 2021 논문이 있다.[^home] 대표 논문 6은 대수 차수가 낮은 대칭키 암호에 잡음을 넣는 설계 전략으로 곱셈 복잡도를 줄인 암호 Rubato를 제안하고, Asiacrypt 2021에서 Cho 등이 제안한 RtF 틀 안에서 기존 암호 HERA와 처리량을 견주었다.[^p6] 대표 논문 5는 동형 암호 방식 TFHE에 맞춘 암호 FRAST를 제안하고, 무작위 S-box를 쓰는 라운드 함수 안의 여러 S-box 호출을 S-box 한 번의 비용으로 계산하는 기법을 내놓았다.[^p5] 2025년 ACM CCS 논문은 TFHE의 단계적(leveled) 동형 계산을 다듬은 방법과 그 응용을 다룬다.[^home]

### 4. 대칭키 암호 기반 양자 내성 전자서명과 영지식 증명 친화 해시 함수

대칭키 암호 부품과 증명 시스템을 결합해 양자 컴퓨터를 이용한 공격에도 안전하도록 설계한 전자서명을 만들고, 영지식 증명 안에서 계산하기 쉬운 해시 함수를 설계하는 연구다. 대표 논문 8은 MPC-in-the-Head 방식의 양자 내성 서명이 안전성을 밑에 쓰는 부품의 일방향성에만 기댄다는 점에 주목해, 대수적 공격(암호를 다항식 연립방정식으로 나타내 풀어 비밀 값을 찾으려는 공격)에 강한 새 일방향 함수 AIM을 제안하고 이를 증명 시스템 BN++와 결합해 서명 방식을 만들었다.[^p8] KAIST 전산학부 소식은 AIM을 쓰는 전자서명 알고리즘 AIMer가 양자내성암호 국가공모전의 최종 알고리즘으로 선정되었다고 전한다.[^aimer] 대표 논문 7은 거듭제곱 잉여를 이용해 만든 S-box를 쓰는 해시 함수 Polocolo를 제안해, 영지식 증명 시스템 Plonk에서 기존 영지식 증명 친화 해시 함수들보다 적은 게이트로 계산되게 했다.[^p7]

## 대표 논문

누리집 논문 목록의 2021–2026년 논문 가운데 네 연구 갈래에서 두 편씩 여덟 편을 골랐다. 모두 이주영 교수가 저자로 참여한 KAIST 재직 시기의 논문이다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [Making GCM Great Again: Toward Full Security and Longer Nonces](https://doi.org/10.1007/978-3-031-91107-1_2) · Advances in Cryptology – EUROCRYPT 2025 (LNCS 15601) | 인증 암호화(AE) 방식 GCM은 세계에서 가장 널리 쓰이는 인증 암호화 방식의 하나지만, 논스 오용의 위험, 한 번 암호화할 때의 짧은 메시지 길이, 모자란 안전성 수준이라는 문제를 안고 있다. 이 논문은 GCM의 설계 원리를 따르면서 표준 모형(이상화한 부품을 가정하지 않는 안전성 모형)에서 더 강한 증명 가능한 안전성을 갖추고, 더 긴 논스를 받아들이거나 논스 오용에 대한 저항을 주는 새 인증 암호화 방식을 설계하는 것을 목표로 했다. 그 결과 GCM과 GCM-SIV를 강화한 eGCM과 eGCM-SIV를 제안했다. 두 방식은 새 CENC형 암호화 모드 eCTR 위에 세웠는데, eCTR은 2n비트 카운터를 써서 효율을 크게 잃지 않고 생일 한계를 넘는 안전성을 얻는다. eCTR을 거의 균등하고 거의 보편적인 해시 함수와 결합해, 입력과 출력의 길이가 자유로운 의사난수 함수(무작위 함수와 구별할 수 없는, 비밀 키로 정해지는 함수) HteC도 만들었다. eGCM과 eGCM-SIV는 임의 길이의 논스를 받아들이고, 최대 입력 길이가 일정할 때 밑에 쓰는 블록 암호가 의사난수 순열(PRP)이라는 가정 아래 거의 완전한 안전성(n비트 블록 암호에 바탕을 두면 n비트 안전성)을 제공한다. 효율도 처리율과 전체 속도에서 GCM과 견줄 만하다.[^p1] | W. Chung, S. Hwang, S. Kim, B. Lee, 이주영 (5명, 교신저자 B. Lee·이주영) |
| 2 | 2024 | [Toward Full n-bit Security and Nonce Misuse Resistance of Block Cipher-Based MACs](https://doi.org/10.1007/978-981-96-0947-5_9) · Advances in Cryptology – ASIACRYPT 2024 (LNCS 15492) | Chen 등이 ASIACRYPT ’21에서 분류한 MAC 구성 가운데 일부의 안전성을 연구했다. Cogliati와 Seurin이 CRYPTO ’16에서 EWCDM이라 이름 붙인 구성을 포함한 네 구성이, 같은 논스를 되풀이하지 않는 설정에서 MAC 질의 2^n번까지 완전히 안전함을 증명해 이전의 3n/4비트 안전성 한계를 높였다. 그 가운데 두 구성은 밑에 쓰는 보편 해시 함수(키로 고른 함수에서 서로 다른 두 입력의 출력이 겹칠 확률이 정해진 한도 이하인 함수 묶음)가 다중 XOR 충돌 저항이라는 성질을 갖추면, 논스를 되풀이한 질의가 늘어나도 안전성이 서서히 줄어든다. 이를 증명하려고 서로 독립인 두 순열에 대한 확장 미러 이론(Mirror theory)이라는 새 도구를 만들었다. 또 다른 두 구성에는 논스를 되풀이하지 않고 MAC 질의 O(2^{3n/4})번과 검증 질의 O(1)번으로 통하는 공격을 보였다.[^p2] | W. Choi, 이주영, Y. Lee (3명, 교신저자 W. Choi·이주영·Y. Lee) |
| 3 | 2025 | [Enhancing Provable Security and Efficiency of Permutation-Based DRBGs](https://doi.org/10.1007/978-3-032-01901-1_15) · Advances in Cryptology – CRYPTO 2025 (LNCS 16004) | Coretti 등이 CRYPTO 2019에서 다룬 치환 기반 결정론적 난수 발생기(DRBG)의 안전성 분석을 다시 살폈다. 스펀지 구조에 바탕을 두어 이 논문이 Sponge-DRBG라 부르는 그 구성이 시드 없는 강건성 모형(난수 발생기에 따로 비밀 시드가 없다고 보고, 내부 상태가 드러난 뒤에도 충분한 엔트로피가 들어오면 다시 안전해지는지까지 따지는 안전성 모형)에서 O(min{2^{c/2}, 2^{λ/2}})번의 질의까지 안전함을 증명했다. 여기서 λ는 필요한 최소 엔트로피, c는 스펀지 구조의 용량이다. 이는 기존의 O(min{2^{c/3}, 2^{λ/2}})에서 생일 한계까지 증명 가능한 안전성 한계를 크게 높인 것이고, 이에 맞는 공격을 보여 이 한계가 빈틈없음도 보였다. Chung 등이 Asiacrypt 2024에서 제안한 다중 추출 게임 기반 환원은 Sponge-DRBG에 그대로 쓸 수 없어, 증명 기법을 다듬고 일반화해 더 넓은 범위의 난수 발생기에 쓸 수 있게 했다. 또 출력률이 거의 최적인 1에 이르는 새 치환 기반 난수 발생기 POSDRBG를 제안했다. Sponge-DRBG의 출력률은 r/n이다(n은 밑에 쓰는 치환의 출력 크기, r = n - c). POSDRBG도 O(min{2^{c/2}, 2^{λ/2}})번의 질의까지 빈틈없이 안전하며, 저자들이 아는 한 시드 없는 강건성 모형에서 Sponge-DRBG와 같은 수준의 증명 가능한 안전성을 유지하면서 최적 출력률 1을 얻은 첫 치환 기반 난수 발생기다.[^p3] | W. Chung, S. Hwang, H. Kim, 이주영 (4명, 교신저자 이주영) |
| 4 | 2024 | [Provable Security of Linux-DRBG in the Seedless Robustness Model](https://doi.org/10.1007/978-981-96-0938-3_15) · Advances in Cryptology – ASIACRYPT 2024 (LNCS 15489) | Linux 6.4.8에 쓰인 결정론적 난수 발생기(DRBG)의 증명 가능한 안전성을 연구했다. Linux 4와 Linux 5.17에서 구조가 크게 바뀐 뒤 Linux-DRBG를 증명 가능한 안전성 관점에서 분석한 첫 연구다. 시드 없는 강건성 모형에서 내부 부품의 출력 크기와 입력의 예측 어려움에 따라 정해지는 질의 수까지 안전함을 증명했다. 같은 규모의 질의로 가능한 구별 공격도 제시해, 증명한 한계가 빈틈없음을 보였다.[^p4] | W. Chung, H. Kim, 이주영, Y. Lee (4명, 교신저자 W. Chung) |
| 5 | 2024 | [FRAST: TFHE-Friendly Cipher Based on Random S-Boxes](https://doi.org/10.46586/tosc.v2024.i3.1-43) · IACR Transactions on Symmetric Cryptology 2024(3) | 하이브리드 동형 암호라고도 부르는 트랜스사이퍼링 틀은 클라이언트-서버 모형에서 동형 암호(HE) 방식과 대칭키 암호를 결합해 클라이언트 쪽의 계산·통신 부담을 줄이는 실용적인 방법이다. 이 틀에서는 서버가 대칭키 암호를 동형 연산으로 계산하므로, 동형 암호 방식의 특성을 고려한 「HE 친화」 암호의 새 설계 원리가 필요하다. 이 논문은 라운드 수를 줄이려고 무작위 S-box에 바탕을 둔 라운드 함수(블록 암호가 되풀이해 적용하는 기본 변환)를 쓰는 새 TFHE 친화 암호 FRAST를 제안했다. FRAST의 라운드 함수는 이중 블라인드 회전(double blind rotation)이라는 새 최적화 기법으로 TFHE에서 효율적으로 계산되고, 새 WoP-PBS 방법과 결합하면 라운드 함수 안의 여러 S-box 호출을 S-box 한 번 호출하는 비용으로 계산할 수 있다. 그 결과 트랜스사이퍼링 틀의 오프라인 단계에서 TFHE 키스트림(평문과 섞어 암호문을 만드는 데 쓰는 키 비트열)을 계산할 때 FRAST의 처리량은 Kreyvium보다 2.768배, Elisabeth보다 10.57배 높고, 대가로 통신 부담이 조금 더 크다.[^p5] | M. Cho, W. Chung, J. Ha, 이주영, E. Oh, M. Son (6명) |
| 6 | 2022 | [Rubato: Noisy Ciphers for Approximate Homomorphic Encryption](https://doi.org/10.1007/978-3-031-06944-4_20) · Advances in Cryptology – EUROCRYPT 2022 (LNCS 13275) | 트랜스사이퍼링 틀은 서버 쪽에서 대칭키 암호문을 동형 암호문으로 바꾸어 클라이언트 쪽의 계산·통신 부담을 줄인다. Asiacrypt 2021에서 Cho 등이 근사 계산을 지원하는 RtF 틀을 제안했다. 이 논문은 대수 차수가 낮은 대칭키 암호에 잡음을 넣는 새 설계 전략으로 잡음을 넣은 암호 묶음 Rubato를 제안했다. 이 전략으로 기존 HE 친화 암호와 견주어 전체 안전성을 떨어뜨리지 않고 암호의 곱셈 복잡도를 크게 줄였다. 보통 크기의 블록(16–64)에서 Rubato는 곱셈 깊이(계산 과정에서 곱셈이 차례로 이어지는 최대 단수)가 2–5로 낮고 암호화한 단어 하나당 곱셈이 2.1–6.25번으로 적으며, 대가로 암호문 확장(암호문 길이가 평문보다 늘어나는 비율)이 1.26–1.31로 조금 크다. 대칭키 암호 분석과 LWE(오차가 섞인 선형 방정식을 푸는 문제) 관점의 분석을 포함한 폭넓은 분석이 Rubato의 안전성을 뒷받침한다. RtF 틀 안에서 HERA와 견주면 클라이언트 쪽과 서버 쪽 처리량이 각각 22.9%, 32.2% 좋아지고, 암호문 확장은 1.6%만 더 크다.[^p6] | J. Ha, S. Kim, B. Lee, 이주영, M. Son (5명, 교신저자 S. Kim·이주영) |
| 7 | 2025 | [Polocolo: A ZK-Friendly Hash Function Based on S-Boxes Using Power Residues](https://doi.org/10.1007/978-3-031-91134-7_11) · Advances in Cryptology – EUROCRYPT 2025 (LNCS 15604) | 기존 해시 함수는 영지식 증명 환경에서 비효율적인 경우가 많아 여러 영지식(ZK) 친화 해시 함수가 설계되었다. 한편 최근 영지식 프로토콜에 조회 논증(어떤 값이 미리 정한 표에 들어 있음을 보이는 증명 기법)이 도입되어 「ZK 비친화」 연산을 더 효율적으로 다룰 수 있게 되었고, 조회표에 바탕을 둔 ZK 친화 해시 함수도 나왔다. 이 논문은 거듭제곱 잉여를 이용해 만든 S-box를 쓰는 새 ZK 친화 해시 함수 Polocolo를 제안했다. 이 방식은 특히 영지식 증명 시스템 Plonk와 결합할 때 조회표 사용에 드는 게이트(증명 회로를 이루는 기본 연산 단위) 수를 줄여, 이런 비선형 층(입력과 출력이 선형 관계가 아닌 변환 층)을 여러 라운드에 걸쳐 쓸 수 있게 한다. Polocolo의 선형 층에 쓸 새 MDS 행렬(Maximum Distance Separable 행렬, 입력의 변화를 출력의 많은 자리로 퍼뜨리는 성질이 최대가 되도록 만든 행렬)도 제안했다. 그 결과 Polocolo는 최신 ZK 친화 해시 함수들보다 Plonk 게이트가 적게 든다. 예를 들어 밑에 쓰는 순열의 크기를 나타내는 t가 8일 때 Anemoi보다 Plonk 게이트가 21% 적고, t가 3일 때 최근의 조회표 기반 ZK 친화 해시 함수인 Reinforced Concrete보다 24% 적다.[^p7] | J. Ha, S. Hwang, 이주영, S. Park, M. Son (5명, 교신저자 이주영·M. Son) |
| 8 | 2023 | [AIM: Symmetric Primitive for Shorter Signatures with Stronger Security](https://doi.org/10.1145/3576915.3616579) · Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security (ACM CCS 2023) | MPC-in-the-Head(MPCitH) 방식에 바탕을 둔 양자 내성 서명은 안전성이 밑에 쓰는 부품의 일방향성에만 달려 있어, 양자 내성 암호가 기대는 어려운 문제 가정을 다양하게 해 준다는 점에서 최근 주목받고 있다. 최근의 MPCitH 친화 암호들은 서명 성능을 높이려고 큰 체(field, 덧셈·뺄셈·곱셈과 0이 아닌 수로 나누기가 정의된 수 체계) 위에서 동작하는 단순한 대수적 S-box로 설계되었는데, 구조가 단순한 만큼 대수적 공격에 대한 안전성을 폭넓게 따져야 한다. 이 논문은 거듭제곱 연산에 바탕을 둔 S-box와 이런 S-box를 쓰는 암호 부품의 대수적 암호 분석을 다듬었다. 대수적 공격 기법인 그뢰브너 기저 공격의 이론적 복잡도를 바르게 추정하려면 S-box에서 얻는 이차 방정식의 정확한 개수가 결정적임을 실험으로 보였고, XL 공격도 가능한 이차 방정식을 모두 찾아 쓰면 더 빠를 수 있음을 보였다. 이렇게 다듬은 분석을 고려해 대수적 공격에 강한 MPCitH 친화 대칭키 부품인 새 일방향 함수 AIM을 제안하고, 대수적·통계적·양자·일반 공격에 대한 안전성을 폭넓게 분석했다. AIM을 BN++ 증명 시스템과 결합해 새 서명 방식을 만들었고, 구현 결과 서명 크기와 서명 시간에서 대칭키 부품에 바탕을 둔 기존 서명 방식들보다 나았다.[^p8] | 1저자 S. Kim, 마지막 저자 이주영 (11명) |

## 교수와 전문 분야

이주영 교수(Jooyoung Lee)는 KAIST 전산학부 부교수다. 전산학부 교수 소개는 연구 분야를 전산이론·시큐어 컴퓨팅으로, 전공을 암호론·조합론으로 적고,[^cs] 정보보호대학원 교수진 페이지는 소속을 「전산학부, 정보보호대학원」으로, 분야를 「암호론, 조합론」으로 적는다.[^gsis] 누리집 Members 페이지의 교수 카드는 2016년부터 KAIST School of Computing의 Associate Professor라고 적는다.[^members]

교수는 서울대학교 수학과에서 학사(1996)와 석사(1998)를, 2005년 University of Waterloo에서 암호론으로 박사 학위를 받았다. 2005년부터 2011년까지 국가보안기술연구소에서, 2011년부터 세종대학교 수학통계학부에서 일했고, 2016년 KAIST 전산학부(정보보호대학원)에 부교수로 부임했다.[^cs] 전산학부 소식은 부임일을 2016년 7월 1일로 적는다.[^arrive] 전산학부 교수 소개는 주요 연구 분야를 암호론과 조합론으로 들고, 최근에는 화이트박스 암호, 동형암호와 대칭키 암호의 하이브리드 구조, 대칭키 암호 기반 양자 내성 암호를 연구한다고 적는다.[^cs]

누리집 논문 목록으로 보면 교수의 전문 분야는 세 갈래다. 첫째는 대칭키 암호 구성의 증명 가능한 안전성이다. 2010–2018년 항목에는 이상적 암호 모형(블록 암호를 키마다 무작위로 고른 순열로 보는 모형)에서의 압축 함수 안전성, 키 길이 확장과 다중 암호화, Even-Mansour 암호, 무작위 순열의 합을 다룬 제목이 이어지고,[^home] 2021–2026년에는 인증 암호화, 메시지 인증 코드, 결정론적 난수 발생기의 안전성 증명으로 이어진다(대표 논문 1–4).[^p1][^p2][^p3][^p4] 둘째는 동형 암호, MPC-in-the-Head 서명, 영지식 증명처럼 다른 암호 기술 안에서 계산하기 쉽도록 맞춘 대칭키 암호 부품의 설계다(대표 논문 5–8).[^p5][^p6][^p7][^p8] 셋째는 조합론이다. 2004–2008년 항목에는 D. R. Stinson과 함께 쓴 센서 네트워크의 키 사전 분배와 조합 설계 논문들이 있다.[^home]

## 응용 분야

대표 논문 1은 개선 대상인 GCM을 세계에서 가장 널리 쓰이는 인증 암호화 방식의 하나로 소개하고,[^p1] 대표 논문 4는 Linux 6.4.8의 난수 발생기를, 2024년 학술지 논문은 ISO 난수 발생기 표준의 OFB-DRBG를 분석 대상으로 삼는다.[^p4][^ofb] 동형 암호에 맞춘 대칭키 암호 연구는 클라이언트-서버 모형에서 클라이언트 쪽의 계산·통신 부담을 줄이는 트랜스사이퍼링 틀을 겨냥한다.[^p5][^p6] KAIST 전산학부 소식은 2025년 난수 발생기 성과가 사물인터넷(IoT) 기기부터 대규모 클라우드 서버까지 폭넓게 활용될 수 있고, 국제 암호 표준 개정 과정에서 새로운 기준이 될 가능성도 열었다고 적는다.[^drbg] 또 양자내성암호 국가공모전에서 선정된 알고리즘이 정부가 추진하는 「범국가 양자내성암호 전환 마스터플랜」의 핵심 기술로 쓰일 예정이며, 연구팀이 산업계·학계·정부와 협력해 양자내성암호 기술 확산에 힘쓸 계획이라고 전한다.[^aimer] 대표 논문 7의 출판사 페이지는 이 연구가 LG전자와 KAIST의 협력 과제 지원을 받았다고 적는다.[^polack] 누리집 Members 페이지는 Former PhD Students 칸의 진로로 고려대학교 정보보호대학원, DGIST, 숭실대학교 같은 대학과 삼성SDS, 삼성전자, ETRI(한국전자통신연구원), DESILO를 적는다.[^members]

## 구성원

2026년 10월 25일에 읽은 누리집 Members 페이지의 PhD Students 칸 3명과 MS Students 칸 1명이다. 과정과 이메일은 페이지 표기이고, 황성하와 정우혁은 소속을 School of Computing (Graduate School of Information Security), KAIST로, 박승민과 김민순은 School of Computing, KAIST로 적는다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Seongha Hwang (황성하) | 박사과정 | mathience98@kaist.ac.kr | 1, 3, 7 |
| Woohyuk Chung (정우혁) | 박사과정 | hephaistus@kaist.ac.kr | 1, 3, 4, 5 |
| Seungmin Park (박승민) | 박사과정 | smpak@kaist.ac.kr | 7 |
| Minsun Kim (김민순) | 석사과정 | realdano@kaist.ac.kr |  |

## 졸업생과 이전 구성원

누리집 Members 페이지의 Former PhD Students 칸 8명과 Former Master's Students 칸 5명이다. 「학위·과정」 칸은 칸 이름이고, 진로는 Former PhD Students 칸의 이름 뒤에 적힌 표기다. Former Master's Students 칸은 이름만 적는다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Seongkwang Kim (김성광) | Former PhD Students | 고려대학교 정보보호대학원 |
| Wonseok Choi (최원석) | Former PhD Students | DGIST(대구경북과학기술원) 전기전자컴퓨터공학과 |
| Byeonghak Lee (이병학) | Former PhD Students | 삼성SDS |
| Doyoung Chung (정도영) | Former PhD Students | ETRI(한국전자통신연구원) |
| Yeongmin Lee (이영민) | Former PhD Students | DESILO |
| Hwigyeom Kim (김휘겸) | Former PhD Students | 삼성전자 |
| Jincheol Ha (하진철) | Former PhD Students | 숭실대학교 소프트웨어학부 |
| Mincheol Son(손민철) | Former PhD Students | DGIST 박사후과정 |
| Seunghan Hong (홍승한) | Former Master's Students |  |
| Heeseok Kim (김희석) | Former Master's Students |  |
| Hyojun Kim (김효준) | Former Master's Students |  |
| Mingyu Cho (조민규) | Former Master's Students |  |
| Sangheon Kim (김상헌) | Former Master's Students |  |

KAIST 전산학부 소식은 김성광이 KAIST에서 석사(2018)와 박사(2022) 학위를 받은 뒤 삼성SDS에서 일하다 2026년 3월 1일 고려대학교 정보보호대학원 조교수로,[^kim] 하진철이 KAIST에서 학사(2019)·석사(2021)·박사(2025) 학위를 받고 2026년 3월 1일 숭실대학교 AI소프트웨어학부 조교수로,[^ha] 최원석이 KAIST에서 석사(2018)와 박사(2022) 학위를 받고 고등과학원(KIAS), Purdue University, Georgia Institute of Technology의 박사후연구원을 거쳐 2025년 5월 12일 DGIST 전기전자컴퓨터공학과 조교수로 임용되었다고 알린다.[^choi] 하진철의 박사학위논문 제목은 「Practical and Efficient Methods to Use the TFHE Scheme」이다.[^ha]

## 최근 논문 목록 (2021–2026)

누리집 첫 화면 Publication 칸은 Refereed Conference Papers 36편과 Refereed Journal Papers 32편을 싣는다. 아래는 그 가운데 각 줄 끝의 서지 연도가 2021–2026년인 23편(학회 논문 15편, 학술지 논문 8편)이며, 학회 논문과 학술지 논문을 연도별로 함께 묶고 각 연도 안에서는 학회 논문을 먼저 적었다. 제목·저자·학회와 학술지 표기는 랩 표기 그대로다. 학회 이름 뒤에 「to appear」로 적힌 Asiacrypt 2026 논문 2편은 발표 전 채택 논문이라 「(채택)」을 붙여 출판 논문과 구분했다.[^home]

**2026**

- W. Chung, S. Hwang, S. Kim, B. Lee and J. Lee. "Extending Accordion Security for Tighter Reduction to AE Security". *Asiacrypt 2026, to appear (채택)*.
- J. Lee, S. Park and M. Son. "Addition-Efficient MDS Matrices from Superconcentrators". *Asiacrypt 2026, to appear (채택)*.
- W. Chung, S. Hwang, B. Lee, S. Kim and J. Lee. "Security of NIST SP800-90A Hash-based DRBGs in the Seedless Model". *Euro S&P 2026, pp.1-22, IEEE, 2026*.
- S. Han, J. Lee, S. Park and M. Son. "Secure Multi-party Matrix Invertibility Testing over Small Finite Fields". *IACR Communications in Cryptology, Vol. 3, No. 2, 2026*.

**2025**

- R. Wan, J. Ha, X. Shen, X. Lu, C. Chen, K. Wang and J. Lee. "Refined TFHE Leveled Homomorphic Evaluation and Its Application". *ACM CCS 2025, pp.2309-2323, ACM, 2025*.
- W. Chung, S. Hwang, H. Kim and J. Lee. "Enhancing Provable Security and Efficiency of Permutation-based DRBGs". *Crypto 2025 (Part V), LNCS 16004, pp.467-496, Springer, 2025*.
- J. Ha, S. Hwang, J. Lee, S. Park and M. Son. "Polocolo: A ZK-Friendly Hash Function Based on S-boxes Using Power Residues". *Eurocrypt 2025 (Part IV), LNCS 15604, pp.303-332, Springer, 2025*.
- W. Chung, S. Hwang, S. Kim, B. Lee and J. Lee. "Making GCM Great Again: Toward Full Security and Longer Nonces". *Eurocrypt 2025 (Part I), LNCS 15601, pp.33-61, Springer, 2025*.

**2024**

- W. Chung, H. Kim, J. Lee and Y. Lee. "Provable Security of Linux-DRBG in the Seedless Robustness Model". *Asiacrypt 2024 (Part VI), LNCS 15489, pp.461-490, Springer, 2024*.
- W. Choi, J. Lee and Y. Lee. "Toward Full n-bit Security and Nonce Misuse Resistance of Block Cipher-based MACs". *Asiacrypt 2024 (Part IX), LNCS 15492, pp.251-279, Springer, 2024*.
- M. Cho, W. Chung, J. Ha, J. Lee, E. Oh and M. Son. "FRAST: TFHE-friendly Cipher Based on Random S-boxes". *IACR Transactions on Symmetric Cryptology, Vol. 2024, No. 3, pp.1-43, 2024*.
- W. Chung, H. Kim, J. Lee and Y. Lee. "Security Analysis of the ISO standard OFB-DRBG". *Designs, Codes and Cryptography, Vol. 92, pp.3515-3532, 2024*.
- W. Choi, S. Hwang, B. Lee and J. Lee. "ZLR: A Fast Online Authenticated Encryption Scheme Achieving Full Security". *Designs, Codes and Cryptography, Vol. 92, pp.3261-3316, 2024*.
- W. Choi, J. Lee and Y. Lee. "Building PRFs from TPRPs: Beyond the Block and the Tweak Length Bounds". *IACR Transactions on Symmetric Cryptology, Vol. 2024, No. 1, pp.35-70, 2024*.

**2023**

- S. Kim, J. Ha, M. Son, B. Lee, D. Moon, J. Lee, S. Lee, J. Kwon, J. Cho, H. Yoon, and J. Lee. "AIM: Symmetric Primitive for Shorter Signatures with Stronger Security". *ACM CCS 2023, pp.401-415, ACM, 2023*.
- Z. Bao, S. Hwang, A. Inoue, B. Lee, J. Lee, and K. Minematsu. "XOCB: Beyond-Birthday-Bound Secure Authenticated Encryption Mode with Rate-One Computation". *Eurocrypt 2023 (Part IV), LNCS 14007, pp.532-561, Springer, 2023*.
- N. Jho and J. Lee. "Partition and Mix: Generalizing the Swap-or-Not Shuffle". *Designs, Codes and Cryptography, Vol. 91, pp.2237-2254, 2023*.

**2022**

- W. Choi, H. Kim, J. Lee and Y. Lee. "Multi-User Security of the Sum of Truncated Random Permutations". *Asiacrypt 2022 (Part II), LNCS 13792, pp.682-710, Springer, 2022*.
- J. Ha, S. Kim, B. Lee, J. Lee and M. Son. "Rubato: Noisy Ciphers for Approximate Homomorphic Encryption". *Eurocrypt 2022 (Part I), LNCS 13275, pp.581-610, Springer, 2022*.
- D. Chung, S. Lee, D. Choi and J. Lee. "Alternative Tower Field Construction for Quantum Implementation of the AES S-box". *IEEE Transactions on Computers, Vol. 71, issue 10, pp.2553-2564, 2022*.

**2021**

- J. Cho, J. Ha, S. Kim, B. Lee, J. Lee, J.Lee, D. Moon and H. Yoon. "Transciphering Framework for Approximate Homomorphic Encryption". *Asiacrypt 2021 (Part III), LNCS 13092, pp.640-669, Springer, 2021*.
- W. Choi, B. Lee, J. Lee and Y. Lee. "Toward a Fully Secure Authenticated Encryption Scheme From a Pseudorandom Permutation". *Asiacrypt 2021 (Part III), LNCS 13092, pp.407-434, Springer, 2021*.
- B. Cogliati, J. Ethan, V. Lallemand, B. Lee, J. Lee and M. Minier. "CTET+: A Beyond-Birthday-Bound Secure Tweakable Enciphering Scheme Using a Single Pseudorandom Permutation". *IACR Transactions on Symmetric Cryptology, Vol. 2021, No. 4, pp.1-35, 2021*.

## 소식

KAIST 전산학부 소식 게시판에 2021년 10월 13일 이후 실린 연구실 연구 소식 2건이다. 날짜와 제목은 게시판 표기 그대로다.[^drbg][^aimer]

- 2025-08-21 · KAIST, 보안성과 효율성 극대화한 차세대 난수발생기 개발
- 2025-02-04 · KAIST-삼성SDS 공동 개발 전자서명 알고리즘 AIMer, 국가공모전 최종 선정

## 연락과 위치

- 교수연구실: N5, 2318 (전산학부 교수 소개 표기), 전산학부 연구실 소개 페이지는 「N5 2318호」로 적는다.[^cs][^cslab]
- 전화: 042-350-3571[^cslab][^gsis]
- 이메일: hicalf@kaist.ac.kr (누리집 Members 페이지 표기)[^members]
- 대학원 진학: 누리집 첫 화면은 석박사 과정에 관심 있는 학생에게 이메일로 문의해 달라고 안내한다.[^home]
[^home]: 연구실 누리집 첫 화면 <https://sites.google.com/view/cryptlab/home> (연구실 소개 문장, Publication 칸의 Refereed Conference Papers·Refereed Journal Papers, 대학원 진학 안내, 2026-10-25 열람)
[^members]: 누리집 Members 페이지 <https://sites.google.com/view/cryptlab/members> (2026-10-25 열람)
[^gsis]: KAIST 정보보호대학원 교수진 <https://gsis.kaist.ac.kr/people/faculty> (이주영 교수 항목, 2026-10-25 열람)
[^gsislab]: KAIST 정보보호대학원 연구실 <https://gsis.kaist.ac.kr/research/center> (암호학 분야의 Cryptology (Crypt) Lab 항목, 2026-10-25 열람)
[^cs]: KAIST 전산학부 교수 소개 「이주영」 <https://cs.kaist.ac.kr/people/view?idx=536&kind=faculty&menu=160> (2026-10-25 열람)
[^cslab]: KAIST 전산학부 연구실 소개 「암호론 연구실」 <https://cs.kaist.ac.kr/research/labView?sn=99&menu=64> (2026-10-25 열람)
[^arrive]: KAIST 전산학부 소식 「이주영, 김주호 교수 부임 안내」 <https://cs.kaist.ac.kr/board/view?bbs_id=news&bbs_sn=7137&menu=83> (2016-07-05 게시, 2026-10-25 열람)
[^drbg]: KAIST 전산학부 소식 「KAIST, 보안성과 효율성 극대화한 차세대 난수발생기 개발」 <https://cs.kaist.ac.kr/board/view?bbs_id=news&bbs_sn=11547&menu=83> (2025-08-21 게시, 2026-10-25 열람)
[^aimer]: KAIST 전산학부 소식 「KAIST-삼성SDS 공동 개발 전자서명 알고리즘 AIMer, 국가공모전 최종 선정」 <https://cs.kaist.ac.kr/board/view?bbs_id=news&bbs_sn=11364&menu=83> (2025-02-04 게시, 2026-10-25 열람)
[^kim]: KAIST 전산학부 소식 「김성광 박사, 고려대 정보보호대학원 조교수 임용」 <https://cs.kaist.ac.kr/board/view?bbs_id=news&bbs_sn=11758&menu=83> (2026-03-03 게시, 2026-10-25 열람)
[^ha]: KAIST 전산학부 소식 「하진철 박사, 숭실대 AI소프트웨어학부 조교수 임용」 <https://cs.kaist.ac.kr/board/view?bbs_id=news&bbs_sn=11757&menu=83> (2026-03-03 게시, 2026-10-25 열람)
[^choi]: KAIST 전산학부 소식 「최원석 박사, 대구경북과학기술원(DGIST) 조교수 임용」 <https://cs.kaist.ac.kr/board/view?bbs_id=news&bbs_sn=11440&menu=83> (2025-05-10 게시, 2026-10-25 열람)
[^polack]: 대표 논문 7의 출판사 페이지 <https://link.springer.com/chapter/10.1007/978-3-031-91134-7_11> (연구 지원 문구, 2026-10-25 열람)
[^ofb]: W. Chung, H. Kim, J. Lee, Y. Lee, Designs, Codes and Cryptography 92, 3515-3532 (온라인 2024-06-27). <https://doi.org/10.1007/s10623-024-01449-z> 초록 기준.
[^tc22]: D. Chung, S. Lee, D. Choi, J. Lee, IEEE Transactions on Computers 71, 2553-2564 (2022). <https://doi.org/10.1109/tc.2021.3135759> 초록 기준(Semantic Scholar 등록 초록).
[^p1]: W. Chung 외, J. Lee, Advances in Cryptology – EUROCRYPT 2025, Lecture Notes in Computer Science 15601, 33-61 (온라인 2025-04-27). <https://doi.org/10.1007/978-3-031-91107-1_2> 초록 기준(출판사 논문 페이지).
[^p2]: W. Choi, J. Lee, Y. Lee, Advances in Cryptology – ASIACRYPT 2024, Lecture Notes in Computer Science 15492, 251-279 (온라인 2024-12-09). <https://doi.org/10.1007/978-981-96-0947-5_9> 초록 기준(출판사 논문 페이지).
[^p3]: W. Chung, S. Hwang, H. Kim, J. Lee, Advances in Cryptology – CRYPTO 2025, Lecture Notes in Computer Science 16004, 467-496 (온라인 2025-08-17). <https://doi.org/10.1007/978-3-032-01901-1_15> 초록 기준(출판사 논문 페이지).
[^p4]: W. Chung, H. Kim, J. Lee, Y. Lee, Advances in Cryptology – ASIACRYPT 2024, Lecture Notes in Computer Science 15489, 461-490 (온라인 2024-12-12). <https://doi.org/10.1007/978-981-96-0938-3_15> 초록 기준(출판사 논문 페이지).
[^p5]: M. Cho 외, M. Son, IACR Transactions on Symmetric Cryptology 2024(3), 1-43 (온라인 2024-09-06). <https://doi.org/10.46586/tosc.v2024.i3.1-43> 초록 기준.
[^p6]: J. Ha 외, M. Son, Advances in Cryptology – EUROCRYPT 2022, Lecture Notes in Computer Science 13275, 581-610 (온라인 2022-05-25). <https://doi.org/10.1007/978-3-031-06944-4_20> 초록 기준(출판사 논문 페이지).
[^p7]: J. Ha 외, M. Son, Advances in Cryptology – EUROCRYPT 2025, Lecture Notes in Computer Science 15604, 303-332 (온라인 2025-04-27). <https://doi.org/10.1007/978-3-031-91134-7_11> 초록 기준(출판사 논문 페이지).
[^p8]: S. Kim 외, J. Lee, Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security, 401-415 (온라인 2023-11-21). <https://doi.org/10.1145/3576915.3616579> 초록 기준(Semantic Scholar 등록 초록).

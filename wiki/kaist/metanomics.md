# 메타노믹스 연구실 (Metanomics Lab)

**KAIST 기술경영학부 · 정승원 교수**

- 분야: 미시경제 이론, 경매 이론, 메커니즘·시장 설계(매칭), 사회·경제 네트워크, 블록체인·암호화폐 경제, 기계학습 응용
- 홈페이지: <https://metanomics.kaist.ac.kr/>
- 근거와 출처: [Metanomics 근거 페이지](metanomics-sources.md)

> 경매와 입찰, 투표 같은 규칙이 사람들의 행동을 어떻게 바꾸는지 경제학으로 따지고, 더 나은 규칙을 설계하는 연구실이다. 정부 조달 입찰 자료 분석, 블록체인의 투표 규칙, 블록체인 소셜미디어의 자동 게시 봇 탐지까지 다룬다.[^home][^papers]

## 무엇을 연구하나

연구실을 이끄는 정승원 교수는 연구 관심사를 미시경제 이론(개인과 기업의 선택, 시장의 작동을 다루는 경제학), 경매, 메커니즘·시장 설계, 사회·경제 네트워크로 적고, 학제 연구 분야로 블록체인·암호화폐, ESG, 기계학습 응용을 든다.[^prof] 메커니즘 설계는 참여자들이 각자 이익을 좇아도 원하는 결과가 나오도록 게임의 규칙을 짜는 분야이고, 시장 설계(매칭)는 학교 배정처럼 짝을 맺어 주는 규칙을 다룬다. 연구실 소개는 여기에 메타버스와 기계학습을 함께 적는다.[^home]

첫 번째 갈래는 **경매와 입찰 규칙**이다. 대표 논문에서는 러시아 정부 조달 입찰 자료로 입찰자마다 다른 비용과 위험 회피 성향(손실 위험을 꺼리는 정도)을 추정했고,[^p1] 판매자가 정한 최저 가격(유보가격)을 낮추려는 가짜 입찰의 동기를 이론으로 밝혔으며,[^p2] 경제 분석에 쓰는 확률 부등식을 일반화했다.[^p3] 다른 사람을 추천해 경매에 끌어들이는 추천 경매의 규칙을 다룬 논문도 Games and Economic Behavior(2024)에 냈다.[^papers]

두 번째 갈래는 **블록체인의 경제학**이다. 대표 논문에서는 지분을 가진 사람들이 투표로 블록 생산자를 뽑는 위임 지분 증명(DPoS) 블록체인에서 계정당 표 수를 몇 표로 정해야 장악 위험을 줄일 수 있는지 분석했고,[^p4] 블록체인 기반 소셜미디어에서 보상을 노리고 글을 자동으로 올리는 봇을 기계학습으로 찾아냈다.[^p5]

세 번째로 의사결정 집단 속 소수 의견을 다루는 실험 연구에도 참여한다. 대표 논문에서는 집단에 대한 안정감을 느끼게 하면 소수 의견을 가진 사람이 더 설득력 있게 반대 의견을 낸다는 결과를 냈다.[^p6]

연구실이 적은 연구 과제로는 결혼·출산 기피를 게임 이론과 AI 에이전트 시뮬레이션으로 분석하는 과제, 대형 언어 모델 기반 AI 에이전트로 경제·사회 실험을 시뮬레이션하는 플랫폼 과제, 삼성전자 DS부문 산학 과제, 환경에 맞춰 바뀌는 실시간 XR(확장현실) 인터페이스 과제, 팬데믹 통계를 조작할 유인을 다룬 이론·실험 과제가 있다.[^home]

## 주요 연구 주제

### 1. 경매와 메커니즘 설계

조달 입찰의 실증 분석, 유보가격과 가짜 입찰, 확률 부등식.[^p1][^p2][^p3] 대표 논문 1–3.

### 2. 블록체인 경제

위임 지분 증명 블록체인의 투표 규칙, 블록체인 소셜미디어 봇 탐지.[^p4][^p5] 대표 논문 4, 5.

### 3. 조직 행동 학제 연구

의사결정 집단의 소수 의견.[^p6] 대표 논문 6.

## 대표 논문

교수 누리집 논문 목록의 2021–2026년 논문에서 세 연구 주제를 고르게 담도록 골랐다. 경제학 논문은 저자를 알파벳순으로 적는 관례가 있어, 저자 칸에는 저자를 순서대로 적었다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 저자[^papers] |
|---|---|---|---|---|
| 1 | 2023 | [Procurements with Bidder Asymmetry in Cost and Risk-Aversion](https://doi.org/10.1080/07350015.2022.2115497) · Journal of Business & Economic Statistics | 입찰자마다 비용 분포와 위험 회피 정도가 다른 최저가 조달 입찰을 분석하는 베이즈 통계 방법(사전 정보와 자료를 결합해 추정하는 통계 방법)을 만들어 러시아 정부의 인쇄용지 조달 자료에 적용했다. 입찰자들은 비용과 위험 회피 정도가 크게 달랐고, 입찰자를 한 명 더 부르면 조달 비용이 최소 5.5% 줄었다. 위험을 꺼리지 않는다고 잘못 가정하면 분석과 정책 권고가 크게 틀어진다는 점도 보였다.[^p1] | Gaurab Aryal, Hanna Charankevich, 정승원, Dong-Hyuk Kim |
| 2 | 2025 | [Reserve Price (In)equivalence: Shill-Bidding to Lower the Reserve Price](https://doi.org/10.1111/boer.12480) · Bulletin of Economic Research | 낙찰자가 두 번째로 높은 입찰가를 내는 2위 가격 경매는 입찰자 수와 관계없이 최적 유보가격이 같지만, 3위 가격 경매는 입찰자가 둘일 때와 그보다 많을 때 다르다. 이 결과를 여러 물건을 파는 경매로 일반화하고, 입찰자가 유보가격을 낮추려고 가짜 입찰(셸 입찰)을 할 새로운 유인을 밝혀, 과다 입찰로 생기는 예산 제약과 함께 3위 가격 경매가 현실에서 드문 이유를 설명할 수 있다고 봤다.[^p2] | 정승원 단독 |
| 3 | 2024 | [A Note on a Moment Inequality](https://doi.org/10.1515/bejte-2023-0045) · B.E. Journal of Theoretical Economics | 확률 변수의 제곱 평균이 평균의 제곱보다 크거나 같다는 잘 알려진 부등식을, 체비쇼프 합 부등식(같은 순서로 정렬된 수열의 곱의 평균에 관한 부등식)을 써서 여러 차수의 모멘트(확률 분포의 모양을 나타내는 값, 예: 평균)를 비교하는 일반적인 부등식으로 넓히고 경제학 응용을 보였다.[^p3] | 정승원 단독 |
| 4 | 2026 | [Centralized Decentralization: Simple Economics of the DPoS Blockchain Governance](https://doi.org/10.1080/13504851.2024.2445074) · Applied Economics Letters | 위임 지분 증명 블록체인에서는 블록 생산자의 압도적 다수가 규칙을 바꿀 수 있어 표가 한쪽에 몰리지 않게 하는 것이 중요하다. 장악 위험은 줄이면서 투표 자유도는 살리는 계정당 표 수를 찾았고, 표 수를 줄일수록 장악에 필요한 지분이 늘지만 어느 지점까지만 그렇다는 점을 보여 일부 블록체인의 "계정당 1표" 규칙이 꼭 필요하지는 않을 수 있다고 봤다.[^p4] | 정승원 단독 |
| 5 | 2021 | [Posting Bot Detection on Blockchain-Based Social Media Platform Using Machine Learning Techniques](https://doi.org/10.1609/icwsm.v15i1.18062) · ICWSM 2021 | 글이 추천을 받으면 암호화폐로 보상하는 블록체인 소셜미디어 스팀잇에서, 보상을 노리고 글을 자동으로 올리는 봇을 처음으로 연구했다. 글의 단어와 내용 사이 거리를 묶어 새 특징을 만들었고, 이 특징이 페이스북·트위터 봇 탐지에 쓰던 특징보다 분류 성능이 좋았다.[^p5] | Taehyun Kim, Hyomin Shin, Hyung Ju Hwang, 정승원 |
| 6 | 2026 | [The Role of Group Attachment Security in Minority Opinion Expression in Decision Making Groups](https://doi.org/10.1038/s41598-026-65147-7) · Scientific Reports | 자기 집단 안에서 소수 의견을 내기는 어렵다. 두 실험에서 집단에 대한 애착 안정감을 떠올리게 하자 소수 의견을 가진 사람이 과제에 더 집중하고 반대 의견이 더 설득력 있어졌으며, 다수 구성원도 그 반대 의견을 더 쓰려 했다. 다양한 사람이 모인 의사결정 집단에서 소수 의견이 힘을 얻는 조건을 제시했다.[^p6] | Tae Hyun Kim, Sujin Lee, Zoe Kinias, 정승원 |

## 교수와 전문 분야

정승원 교수는 미국 스탠퍼드대에서 박사를 받았고, 페이스북에서 New Faculty Fellow 이코노미스트로 일한 뒤 영국 브리스톨대 경제학부 강사를 거쳐 KAIST 경영대학 기술경영학부 부교수가 됐다. NYU-KAIST Global Innovation and Research Institute 겸임 교원이며, 메타버스대학원, 녹색성장지속가능대학원, AI대학 AX학과 겸임교수다.[^prof][^members] 콘텐츠 입찰가 선정과 메시지 처리에 관한 미국 특허 2건(2019, 2020)도 적는다.[^papers] 2021년 이전 연구로는 외부 효과가 있는 경매의 코어(어떤 참여자 집단도 따로 벗어날 이유가 없는 배분)를 다룬 논문을 RAND Journal of Economics(2020)에 냈다.[^papers]

논문으로 보면 전문 분야는 세 갈래다.

- **경매 이론과 조달 입찰의 실증 분석**.[^p1][^p2][^p3]
- **블록체인 거버넌스와 플랫폼의 경제 분석**.[^p4][^p5]
- **조직 의사결정의 실험 연구**.[^p6]

## 응용 분야

대표 논문과 과제로 보면 정부 조달과 경매 설계, 블록체인 운영 규칙, 소셜미디어 봇 대응, 다양한 사람이 모인 의사결정 집단, AI 에이전트를 이용한 경제·사회 정책 실험에 닿아 있다.[^p1][^p4][^p5][^p6][^home] 졸업생은 삼성전자 DS부문, 아스트라제네카, 한화시스템으로 진출했고 1명은 창업했다고 랩이 적는다.[^members]

## 구성원

2026년 10월 20일 랩 Members 페이지 기준이다. 괄호는 랩이 적은 소속 프로그램이고, 이메일은 랩이 적은 학교 주소다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Kyeongyeop Kim | 박사과정 (BTM) | Spring 2025 | kkyy7211@kaist.ac.kr |  |
| Kavin Cherdchanyapong | 박사과정 (GDI) | Fall 2022 | kavin@kaist.ac.kr |  |
| Doyoung Jung | 석사과정 (GSMV) | Fall 2026 | 0125dy@kaist.ac.kr |  |
| Sunghun Ko | 석사과정 (BTM) | Spring 2026 | kosunghun317@kaist.ac.kr |  |
| Soyeon Lee | 석사과정 (BTM) | Spring 2026 | lsy12348@kaist.ac.kr |  |
| Kanghyun Kim | 석사과정 (BTM) | Fall 2026 | david9767@kaist.ac.kr |  |
| Taehyun Kim | 박사과정 (BTM, co-advisee) |  | mannakth@kaist.ac.kr | 5, 6 |

## 졸업생

랩 Members 페이지의 졸업생 이름, 과정, 졸업 시기, 진로다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Sabillon Guzman Angel Ramon | BTM MS (Feb 2024) | Samsung DS |
| Minah Han | BIM MS (Aug 2024) | Astrazeneca |
| Chutipattana (Meen) Pidchayanin | BTM MS (Feb 2026) | ELKXA (founder) |
| Hyunwoo Park | BTM MS (Aug 2026) | Hanwha Systems |

## 최근 논문 목록 (2021–2026)

교수 누리집 Research 페이지의 2021년 이후 학술지·학회 논문이다. 공동 연구자는 랩 표기("joint work with")를 옮겼고, 게재 예정 논문은 「연도 표기 없음」에 있다.[^papers]

**2026**

- Seungwon Jeong. "Centralized Decentralization: Simple Economics of the DPoS Blockchain Governance". *Applied Economics Letters, 33(10), 1537-1542*.

**2025**

- Seungwon Jeong. "Reserve Price (In)equivalence: Shill-Bidding to Lower the Reserve Price". *Bulletin of Economic Research, 77(2), 121-127*.

**2024**

- Seungwon Jeong (joint work with Joosung Lee). "The Groupwise-Pivotal Referral Auction: Core-Selecting Referral Strategy-Proof Mechanism". *Games and Economic Behavior, 143, 191-203*.
- Seungwon Jeong. "A Note on a Moment Inequality". *B.E. Journal of Theoretical Economics, 24(1), 435-440*.
- Seungwon Jeong (joint work with Jingyu Jeong, Michael Seo). "Which Came First, Price or Activity? A Vicious Circle of a Blockchain-Based Social Media in the Bear Market". *Proceedings of the International AAAI Conference on Web and Social Media (ICWSM-2024), 18(1), 736-737*.

**2023**

- Seungwon Jeong (joint work with Gaurab Aryal, Hanna Charankevich, Dong-Hyuk Kim). "Procurements with Bidder Asymmetry in Cost and Risk-Aversion". *Journal of Business & Economic Statistics, 41(4), 1143-1156*.

**2021**

- Seungwon Jeong (joint work with Hyung Ju Hwang, Taehyun Kim, Hyomin Shin). "Posting Bot Detection on Blockchain-Based Social Media Platform Using Machine Learning Techniques". *Proceedings of the International AAAI Conference on Web and Social Media (ICWSM-2021), 15(1), 303-314*.

**연도 표기 없음**

- Seungwon Jeong (joint work with Tae Hyun Kim, Sujin Lee, Zoe Kinias). "The Role of Group Attachment Security in Minority Opinion Expression in Decision Making Groups". *Scientific Reports*.
- Seungwon Jeong (joint work with Tae Hyun Kim, Ye Kang Kim, and Sujin Lee). "How Do Leaders' Expressions of Gratitude Relate to Subordinates' Promotion Focus? Links to Job Crafting and Voice". *International Journal for Educational and Vocational Guidance*.

## 연구 과제

랩 첫 화면의 연구 과제와 지원 기관·과제 번호·기간이다.[^home]

- Game-Theoretic and AI Agent-Based Simulation for Overcoming Marriage and Fertility Avoidance (지원 Ministry of Education of the Republic of Korea and National Research Foundation of Korea; 번호 NRF-2026S1A5A8010743; 기간 2026.6-2028.5)
- Economic and Social Experiments Simulation Platform Using LLM-Based AI Agents (지원 National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT); 번호 RS-2026-25490638; 기간 2026.3-2029.2)
- Samsung DS Division Industry Collaboration Project (지원 Samsung Electronics DS; 기간 2025.10-2027.9)
- Real-Time XR Interface Technology for Environmental Adaptation (지원 Institute of Information & communications Technology Planning & Evaluation (IITP) grant funded by the Korea government (MSIT); 번호 RS-2024-00397663; 기간 2024.4-2026.12)
- Theory and Experiments on the Manipulation Incentive of the Pandemic Statistics (지원 National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT); 번호 RS-2022-00166647; 기간 2022.9-2025.2)
- British Academy/Leverhulme Small Research Grants (기간 2021.9-2023.8)
- Klaytn Blockchain Research Center, 4 years (postponed)

## 연락과 위치

- 교수 이메일: seungwon.jeong@kaist.ac.kr[^prof]
- 주소: KAIST 경영대학 기술경영학부(대전 유성구 대학로 291)[^prof]

[^home]: Metanomics Lab 누리집 첫 화면 <https://metanomics.kaist.ac.kr/> (2026-10-20 열람)
[^members]: Metanomics Lab Members 페이지 <https://metanomics.kaist.ac.kr/members> (2026-10-20 열람)
[^prof]: 정승원 교수 누리집 첫 화면 <https://jeong.kaist.ac.kr/> (2026-10-20 열람)
[^papers]: 정승원 교수 누리집 Research(논문·특허) 페이지 <https://jeong.kaist.ac.kr/research> (2026-10-20 열람)
[^p1]: G. Aryal, H. Charankevich, S. Jeong, D.-H. Kim, Journal of Business & Economic Statistics 41, 1143-1156 (온라인 2022-10-03). <https://doi.org/10.1080/07350015.2022.2115497> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: S. Jeong, Bulletin of Economic Research 77, 121-127 (온라인 2024-11-18). <https://doi.org/10.1111/boer.12480> 초록 기준.
[^p3]: S. Jeong, The B.E. Journal of Theoretical Economics 24, 435-440 (온라인 2023-09-21). <https://doi.org/10.1515/bejte-2023-0045> 초록 기준.
[^p4]: S. Jeong, Applied Economics Letters 33, 1537-1542 (온라인 2024-12-26). <https://doi.org/10.1080/13504851.2024.2445074> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: T. Kim, H. Shin, H. J. Hwang, S. Jeong, Proceedings of the International AAAI Conference on Web and Social Media 15, 303-314 (온라인 2021-05-22). <https://doi.org/10.1609/icwsm.v15i1.18062> 초록 기준.
[^p6]: T. H. Kim, S. Lee, Z. Kinias, S. Jeong, Scientific Reports (온라인 2026-08-04). <https://doi.org/10.1038/s41598-026-65147-7> 초록 기준.

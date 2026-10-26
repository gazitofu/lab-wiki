# 반도체 소자 연구실 (Device Research Laboratory, DRL)

**서울대학교 공과대학 전기·정보공학부 · 신형철 교수**

- 분야: 메모리 반도체의 물리 모델과 동작 분석, 쓰기·지우기·정보 보존의 신뢰성, 기계학습을 이용한 소자 특성 예측
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 메모리 반도체 소자[^home][^lab], 소자 설계 시뮬레이션[^lab][^p1][^p4], 과학·공학 AI[^home][^p3][^p7]
- 홈페이지: <https://snudrl.snu.ac.kr/>
- 근거와 출처: [DRL 근거 페이지](drl-sources.md)

> 정보를 저장하는 반도체가 어떻게 동작하고 오류를 일으키는지 물리 모델과 기계학습으로 설명하고, 쓰기·지우기·읽기 조건을 연구하는 연구실이다.[^home][^lab]

## 무엇을 연구하나

신형철 교수가 이끄는 DRL은 반도체 소자(전자 회로에서 특정 기능을 맡는 부품)의 동작을 모델링(대상의 구조와 작동 관계를 수식이나 계산 규칙으로 나타내는 일)하고 분석한다. 누리집은 주요 연구 대상으로 메모리(정보를 저장하는 장치)인 3차원 낸드 플래시를 들고, 기계학습(자료에서 규칙을 배워 새 자료의 결과를 예측하는 방법)으로 소자의 특성을 예측한다고 소개한다. 낸드 플래시는 블록 단위로 지우고 다시 쓸 수 있으며 전원을 꺼도 정보가 남는 반도체 메모리이고, 3차원 구조는 저장 소자를 수직으로 쌓은 구조다.[^home][^p1]

연구의 한 축은 소자 안의 물리 현상을 계산하는 것이다. 컴팩트 모델(소자의 핵심 동작을 제한된 수식과 변수로 표현한 모델)을 만들어 쓰기 과정의 변화를 예측한다. 대표 논문은 터널링(전자가 고전적으로 통과할 수 없는 에너지 장벽을 통과하는 양자 현상)과 트랩(전하를 붙잡아 둘 수 있는 물질 내부나 경계의 결함 상태)을 함께 다루며, 여러 층을 거치는 전자의 이동과 터널링층에 붙잡힌 전자가 쓰기에 미치는 영향을 반영한다. 다른 논문은 전자가 붙잡히는 과정을 다르게 표현한 두 모델을 변환 비율로 연결해 계산 시간과 예측 정확도를 함께 다룬다. 모델의 결과는 측정 자료나 소자 시뮬레이션(소자의 물리 현상과 동작을 컴퓨터로 계산하는 일)과 대조한다.[^p1][^p2]

다른 축은 메모리의 신뢰성(정해진 조건과 기간에 요구된 기능을 유지하는 성질)이다. 정보를 넣고 지우는 동작을 반복하면 나타나는 결함 경유 전류를 모델링하고, 두 차례 쓰기 사이 간격을 조절해 정보 보존 특성을 바꾸는 방안을 연구한다. 셀(정보를 저장하는 기본 단위)의 형상이 타원형으로 변할 때에는 전기장과 전류의 흐름이 달라져 잡음(원하는 동작이나 정보 외에 섞이는 불규칙한 변동)의 영향도 달라지는지 살핀다. 특히 임의 전신 잡음(Random Telegraph Noise, RTN, 전하의 포획과 방출에 따라 전기적 상태가 불규칙하게 바뀌는 잡음)이 문턱 전압(트랜지스터의 전류 흐름이 정해진 기준에 이르는 전압)에 미치는 영향을 분석한다. 트랜지스터는 전기적 입력으로 전류를 조절하는 소자다.[^p5][^p6][^p8]

물리 모델과 학습 모델을 결합하는 연구도 한다. 신경망(자료에서 규칙을 배우도록 계산 단위를 연결한 모형)의 한 종류인 장단기 기억(Long Short-Term Memory, LSTM, 순서가 있는 자료의 과거 정보를 선택적으로 유지하고 갱신하는 신경망 구조)을 이용해, 시간이 지나면서 바뀌는 문턱 전압의 분포(가능한 값과 각 값 또는 구간이 차지하는 비중)를 예측하고 정보 보존에 따른 수명을 추정한다. 또 다른 연구는 쓰기 과정의 물리 모델에 전자 주입의 차이, 잡음, 이웃 셀의 간섭, 단기적인 전하 손실을 함께 반영하고 기계학습으로 계산 결과를 보정한다. 이 환경에서 쓰기 조건에 따른 문턱 전압 분포를 비교해 동작 조건을 최적화(정해진 목표와 조건에 맞는 해를 찾는 일)한다.[^p3][^p7]

## 주요 연구 주제

### 1. 쓰기 동작의 물리 모델

여러 층을 거치는 터널링과 터널링층의 트랩이 쓰기 효율에 미치는 영향을 계산하고, 실험 자료와 소자 시뮬레이션으로 확인한다. 전자 포획을 다르게 표현한 모델 사이를 변환하는 비율을 사용해 여러 셀의 문턱 전압 분포를 계산하는 연구도 한다.[^p1][^p2]

### 2. 지우기 동작과 신뢰성

지우기 중 선택 게이트의 전압 상승과 신뢰성을 함께 다룬다. 선택 게이트는 메모리 셀들이 연결된 경로를 켜고 끄는 소자의 제어 전극이며, 전극은 외부 회로와 연결해 전압을 가하거나 전류를 주고받는 부분이다. 두 차례 쓰기 사이의 전하 손실, 반복 동작 중 결함을 거치는 전류, 셀 형상에 따른 잡음을 모델링하고 동작 조건을 바꾸는 방안을 분석한다.[^p4][^p5][^p6][^p8]

### 3. 기계학습을 이용한 소자 예측

LSTM으로 시간에 따른 문턱 전압 분포를 예측해 정보 보존 수명을 추정한다. 물리 모델에 여러 변동 요인과 기계학습 보정을 결합한 환경에서는 쓰기 조건을 비교하고 문턱 전압 분포의 폭을 줄이는 조건을 찾는다.[^p3][^p7]

## 대표 논문

신형철 교수가 마지막 저자인 서울대 재직 시기의 학술지 논문 8편이다. 쓰기 모델, 지우기와 신뢰성, 기계학습의 세 갈래를 담도록 2026년 논문 6편과 2025년 논문 2편을 골랐다. 연도는 누리집과 등록 자료의 연도 표기다. “쉽게 말하면” 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Modeling and Optimization of 3-D Bandgap-Engineered NAND Flash for Program Operation by Multilayer Tunneling With Trap Physics of Tunneling Nitride](https://doi.org/10.1109/ted.2026.3664277) · IEEE Transactions on Electron Devices | 여러 층을 거치는 터널링을 중심으로 낸드 플래시의 쓰기 동작을 설명하는 물리 모델을 제안했다. 터널링층의 트랩을 반영해 쓰기 효율과 문턱 전압 변화를 계산하고, 실험과 소자 시뮬레이션으로 확인했다. 터널링층 두께를 조절하는 설계에도 모델을 사용했다.[^p1] | 1저자 Haechan Choi, 마지막 저자 신형철 |
| 2 | 2026 | [Capture-cross-section conversion ratio for compact models enabling fast VT distribution simulation of 3-D NAND flash memory](https://doi.org/10.35848/1347-4065/ae9c13) · Japanese Journal of Applied Physics | 전자 포획을 다르게 표현하는 두 모델을 변환 비율로 연결했다. 이 비율은 전자가 붙잡히는 정도와 이동 특성, 전기장에 따른 차이를 반영한다. 변환을 적용한 모델이 다른 모델의 정확도를 재현하면서 계산 시간을 줄이는지 확인했다.[^p2] | 1저자 Haechan Choi, 마지막 저자 신형철 |
| 3 | 2026 | [A long short-term memory neural network-based approach for retention lifespan prediction in 3D NAND flash memory](https://doi.org/10.35848/1347-4065/ae334a) · Japanese Journal of Applied Physics | LSTM이 소자 시뮬레이션 자료에서 문턱 전압이 시간에 따라 변하는 경향을 학습하도록 했다. 전압 분포 전체를 예측하고 오류 기준과 기준 전압에 따라 정보 보존 수명을 계산한다. 먼 미래나 분포의 끝부분을 예측할 때 정확도가 낮아지는 한계도 보고했다.[^p3] | 1저자 Eunseok Oh, 마지막 저자 신형철 |
| 4 | 2026 | [Strategies to Improve Efficiency of Select-Gate Voltage Floating During GIDL-Assisted Erase in 3-D NAND Flash Memory](https://doi.org/10.1109/tcad.2026.3687153) · IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems | 지우기 동작 중 선택 게이트 전압의 상승이 주변 구조의 전하 저장 관계 때문에 억제되는 원인을 분석하고, 전압 변화를 예측하는 모델을 만들었다. 선택 게이트의 신뢰성과 지우기 효율을 함께 확보하는 방안을 제안하고 회로 기반 확률 시뮬레이션으로 확인했다.[^p4] | 1저자 Sungju Kim, 마지막 저자 신형철 |
| 5 | 2026 | [Investigation of retention characteristic improvement in reprogram process based on a physical model for 3D NAND flash memory](https://doi.org/10.1007/s10825-026-02599-0) · Journal of Computational Electronics | 정보를 두 차례에 나누어 쓸 때 중간 간격에 전자가 빠져나가는 과정과 이후 트랩 분포의 변화를 계산했다. 간격을 바꾸어 정보 보존 특성을 조절하는 관계와 전압 인가 방안을 제안했다. 결과를 측정 자료에 맞추고 소자 시뮬레이션으로 확인했다.[^p5] | 1저자 Jooyoung Lee, 마지막 저자 신형철 |
| 6 | 2025 | [Compact Modeling of Trap-Assisted Tunneling Current in 3-D NAND Flash Memory](https://doi.org/10.1109/ted.2025.3541603) · IEEE Transactions on Electron Devices | 쓰기와 지우기를 반복할 때 결함 상태를 거쳐 흐르는 전류를 설명하는 모델을 제안했다. 여러 종류의 전자 이동 경로를 결합하고 측정한 트랩의 밀도와 에너지 정보를 넣어, 다양한 전압과 반복 동작 조건의 측정 자료와 대조했다.[^p6] | 1저자 Hyungjun Jo, 마지막 저자 신형철 |
| 7 | 2026 | [Developing an ultimate 3D NAND flash memory simulation environment for operation and optimization](https://doi.org/10.1007/s10825-026-02613-5) · Journal of Computational Electronics | 쓰기 과정의 물리 모델에 전자 주입의 차이, 잡음, 이웃 셀 간섭과 단기 전하 손실을 함께 반영한 시뮬레이션 환경을 구성했다. 기계학습으로 결과를 보정하고, 다른 소자 특성을 떨어뜨리지 않으면서 문턱 전압 분포의 폭을 줄이는 쓰기 조건을 찾았다.[^p7] | 1저자 Jooyoung Lee, 마지막 저자 신형철 |
| 8 | 2025 | [Impact of Elliptical Cell Geometry and Program Voltage on RTN-Induced Threshold Voltage Shift in 3-D NAND Flash](https://doi.org/10.1109/ted.2025.3622558) · IEEE Transactions on Electron Devices | 저장 셀의 단면이 원형에서 타원형으로 변할 때 임의 전신 잡음이 문턱 전압에 미치는 영향을 소자 시뮬레이션으로 분석했다. 셀 형상과 쓰기 조건, 수직 위치의 영향을 살피고 쓰기 확인 전압의 배분을 바꾸는 방안으로 잡음에 따른 변동을 줄일 수 있음을 보였다.[^p8] | 1저자 Eunseok Oh, 마지막 저자 신형철 |

## 교수와 전문 분야

신형철 교수는 서울대학교에서 전자공학 학사(1985)와 석사(1987), 미국 UC Berkeley에서 전기공학 박사(1993) 학위를 받았다. Motorola의 소자 엔지니어(1994–1996), KAIST 교원(1996–2003), Qualcomm 연구원(2001–2002)을 거쳐 2003년부터 서울대 교수로 재직한다. 누리집은 2012–2014년 반도체공동연구소 소장을 지냈다고 적는다.[^pi] 학과 소개는 전공을 반도체 소자 및 회로로, 관심 분야를 나노 CMOS 기술, CMOS 논리 소자 기술, 소자 신뢰성으로 제시한다. CMOS(Complementary Metal-Oxide-Semiconductor)는 전기적 특성이 상보적인 두 종류의 트랜지스터를 함께 쓰는 기술이다.[^prof]

최근 대표 논문에서 드러나는 전문 분야는 메모리 소자의 물리 모델, 동작 조건에 따른 정보 보존과 오류 분석, 기계학습을 결합한 소자 특성 예측이다. 쓰기와 지우기 중 전하가 움직이는 과정을 계산하고, 소자 형상과 결함의 차이가 결과에 미치는 영향을 모델로 연결한다.[^p1][^p4][^p7][^p8]

## 응용 분야

주요 대상은 3차원 낸드 플래시 메모리다. 대표 논문은 저장 셀의 구조와 쓰기·지우기 조건을 검토하고, 반복 동작과 잡음에 따른 신뢰성을 분석하는 데 모델을 사용한다.[^p1][^p3][^p4][^p6][^p8] 학과 연구실 소개는 논리 소자와 DRAM(Dynamic Random-Access Memory, 전하로 정보를 저장하며 주기적으로 내용을 다시 유지해야 하는 메모리)도 연구 대상으로 제시한다.[^lab]

## 구성원

2026년 10월 27일 누리집의 MEMBER 목록과 개별 소개에 게시된 연구교수 3명, 박사과정 7명, 석사과정 2명이다. 교수는 위 절에 따로 소개했다. 과정은 목록과 개별 소개의 분류 표기, 연구 주제는 Research Area 표기를 옮겼다.[^members] “대표 논문 참여”는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 홍규식 (Kyushik, Hong) | 연구교수 | Logic Device |  |  |
| 전종욱 (Jongwook, Jeon) | 연구교수 | Memory & Logic Device |  |  |
| 송익현 (Ickhyun, Song) | 연구교수 | CMOS RF noise modeling |  |  |
| 안상민 (Sangmin, Ahn) | 박사과정 | NAND Flash | khutkd02@snu.ac.kr | 2 |
| 김성주 (SungJu, Kim) | 박사과정 | NAND Flash | dog9694@snu.ac.kr | 2, 4 |
| 최해찬 (Haechan, Choi) | 박사과정 | NAND Flash | haechan4043@snu.ac.kr | 1, 2 |
| 최환히찬 (Hwanheechan, Choi) | 박사과정 | NAND Flash | igzo25497@snu.ac.kr |  |
| 한인상 (Insang, Han) | 박사과정 | NAND Flash | haninsang@snu.ac.kr |  |
| 진명 (Myung, Jin) | 석사과정 | NAND Flash | gsjb1028@snu.ac.kr | 2 |
| 유진일 (Jinil, Yoo) | 박사과정 | NAND Flash | jiniltim@snu.ac.kr | 1, 2, 7 |
| 이주영 (Jooyoung, Lee) | 박사과정 | NAND Flash | skl131@snu.ac.kr | 5, 7 |
| 임동우 (Dongwoo Lim) | 석사과정 | NAND Flash | dw.lim@snu.ac.kr |  |

## 졸업생과 진로

누리집이 ALUMNI로 분류한 개별 소개 25쪽이다. 신형철 교수의 오랜 재직 기간 동안의 졸업생 기록이 섞여 있으며, 각 항목에 학위와 졸업 연도는 게시되어 있지 않다. 회사·기관과 연구 분야는 누리집의 표기를 그대로 옮겼다.[^alumni]

| 이름 | 누리집이 적은 회사·기관 | 연구 분야 |
|---|---|---|
| [DongHyuk, So](https://snudrl.snu.ac.kr/member/%ec%86%8c%eb%8f%99%ed%98%81/) | Samsung Electroincs | NAND Flash |
| [Hyungjun, Jo](https://snudrl.snu.ac.kr/member/%ec%a1%b0%ed%98%95/) | Samsung Electroincs | NAND Flash |
| [Juhyun, Kim](https://snudrl.snu.ac.kr/member/6250/) | SK Hynix | NAND Flash and Logic Device |
| [Chan, Lee](https://snudrl.snu.ac.kr/member/chan-lee/) | SK Hynix | NAND Flash |
| [Changbeom, Woo](https://snudrl.snu.ac.kr/member/changbeom-woo/) | SK Hynix | NAND Flash and Logic Device |
| [Changhyeok, Im](https://snudrl.snu.ac.kr/member/changhyeok-im/) | Samsung Electroincs | NAND Flash |
| [Dongchan, Lee](https://snudrl.snu.ac.kr/member/dongchan-lee/) | Samsung Electronics | NAND Flash |
| [Donghyun, Ryu](https://snudrl.snu.ac.kr/member/donghyun-ryu/) | Samsung Electronics | Logic Device |
| [Eunseok, Oh](https://snudrl.snu.ac.kr/member/eunseok-oh/) | Samsung Electroincs | NAND Flash |
| [Hyungwoo, Ko](https://snudrl.snu.ac.kr/member/hyungwoo-ko/) | Samsung Electronics | Logic Device |
| [Hyunsoo, Kim](https://snudrl.snu.ac.kr/member/hyunsoo-kim/) | Samsung Electronics | Logic Device |
| [Hyunwoo, Kim](https://snudrl.snu.ac.kr/member/hyunwoo-kim/) | Samsung Electronics | Logic Device |
| [Ickhyun, Song](https://snudrl.snu.ac.kr/member/ickhyun-song/) | Assistant Professor, Hanyang U | CMOS device physics |
| [Ilho Myeong](https://snudrl.snu.ac.kr/member/ilho-myeong/) | Professor, Myongji Univ | NAND Flash and Logic Device |
| [Jaeyeol, Park](https://snudrl.snu.ac.kr/member/jaeyeol-park/) | Samsung Electronics | NAND Flash and Logic Device |
| [Jaeyeop, Jung](https://snudrl.snu.ac.kr/member/jaeyeop-jung/) | SK Hynix | NAND Flash |
| [Jang Kyu, Lee](https://snudrl.snu.ac.kr/member/jang-kyu-lee/) | Samsung Electronics | Logic Device |
| [Jihye, Park](https://snudrl.snu.ac.kr/member/jihye-park/) | Samsung Electronics | NAND Flash |
| [Jongsu, Kim](https://snudrl.snu.ac.kr/member/jongsu-kim/) | Samsung Electronics | Logic Device |
| [Kul, Lee](https://snudrl.snu.ac.kr/member/kul-lee/) | Samsung Electronics | NAND Flash |
| [Kyul, Ko](https://snudrl.snu.ac.kr/member/kyul-ko/) | Samsung Electronics | Logic Device |
| [Sangbin, Jeon](https://snudrl.snu.ac.kr/member/sangbin-jeon/) | Hyundai Motor | Logic Device and DRAM |
| [Yeaji, Yoo](https://snudrl.snu.ac.kr/member/yeaji-yoo/) | Samsung Electronics | Logic Device |
| [Yongmin, Lee](https://snudrl.snu.ac.kr/member/yongmin-lee/) |  | NAND Flash |
| [Youngsoo, Seo](https://snudrl.snu.ac.kr/member/youngsoo-seo/) | Samsung Electronics | Logic Device and NAND Flash |

## 최근 논문 목록 (2021–2026)

누리집 PAPERS의 2021–2026년 개별 서지로 확인한 학술지 논문 48편과 CONFERENCES의 같은 연도 항목 18건이다. 연도는 누리집 표기이며, 2021년 구역은 연도 전체를 포함한다. 학회 목록의 「2026 SISPAD」 항목은 누리집의 제목 표기다.[^journals][^conferences]

**2026**

- Haechan Choi, Sangmin Ahn, Jinil Yoo, Sungju Kim, Myung Jin and Hyungcheol Shin. "Capture-cross-section conversion ratio for compact models enabling fast VT distribution simulation of 3-D NAND flash memory". *Japanese Journal of Applied Physics (JJAP)*.
- Jinil Yoo, Haechan Choi and Hyungcheol Shin. "Physics-Informed Neural Network for PGM Operation of 3-D CT-NANDs Under Data-Scarce Environments". *IEEE Transactions on Electron Devices (TED)*.
- Myung Jin, Haechan Choi, and Hyungcheol Shin. "Time-Step-Free Physics-Based Modeling of Retention Loss in Cryogenic 3-D NAND Flash". *IEEE Electron Device Letters (EDL)*.
- Jooyoung Lee, Jinil Yoo and Hyungcheol Shin. "Developing an ultimate 3D NAND flash memory simulation environment for operation and optimization". *Journal of Computational Electronics (JCE)*.
- Jooyoung Lee and Hyungcheol Shin. "Investigation of retention characteristic improvement in reprogram process based on a physical model for 3D NAND flash memory". *Journal of Computational Electronics (JCE)*.
- Sungju Kim; Jaeyeop Jung; Hyungcheol Shin. "Strategies to Improve Efficiency of Select-Gate Voltage Floating During GIDL-Assisted Erase in 3-D NAND Flash Memory". *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD)*.
- Haechan Choi, Jinil Yoo and Hyungcheol Shin. "Modeling and Optimization of 3-D Bandgap-Engineered NAND Flash for Program Operation by Multilayer Tunneling With Trap Physics of Tunneling Nitride". *IEEE Transactions on Electron Devices (TED)*.
- Chan Lee and Hyungcheol Shin. "Investigation and modeling of vertical redistribution in charge-trap-based 3D NAND Flash memory". *Japanese Journal of Applied Physics (JJAP)*.
- Eunseok Oh and Hyungcheol Shin. "A long short-term memory neural network-based approach for retention lifespan prediction in 3D NAND flash memory". *Japanese Journal of Applied Physics (JJAP)*.
- Dongwoo Lim, Hyungcheol Shin, “Cell-Level Analysis of Erase-Suspend Operation in 3D NAND Flash and a Physical-Model-Based Over-Erase Suppression Scheme”, 2026 10th IEEE Electron Devices Technology & Manufacturing Conference (EDTM), 2026
- [2026 SISPAD] Comprehensive SPICE Compact Modeling of Split-Gate Embedded Flash Memory for Transient and Worst-Case Operation Failure Simulation

**2025**

- Eunseok Oh and Hyungcheol Shin. "Impact of Elliptical Cell Geometry and Program Voltage on RTN-Induced Threshold Voltage Shift in 3-D NAND Flash". *IEEE Transactions on Electron Devices (TED)*.
- Hwanheechan Choi, Hyungjun Jo, Sangmin Ahn, Insang Han, and Hyungcheol Shin. "Machine learning-based prediction of the impact of random grain boundary Z-interference on Vt distribution in 3-D NAND flash memory". *Journal of Computational Electronics (JCE)*.
- Jinil Yoo, Haechan Choi and Hyungcheol Shin. "A semi-analytical physics-based transient model for program (PGM) operation of charge-trap-based 3-D NAND flash memories". *Journal of Computational Electronics (JCE)*.
- Jooyoung Lee, Jinil Yoo, Hyungcheol Shin. "Quantitative analysis on z-interference using reprogram scheme in 3D NAND flash memory Vth distribution". *Solid-State Electronics*.
- Myung Jin, Hyungcheol Shin. "Modeling Attempt-to-Escape Frequency: Tunneling Emission of Trapped Electrons in Tunneling Oxides of 3-D NAND Flash Memory". *IEEE Transactions on Electron Devices (TED)*.
- Haechan Choi, Hyungcheol Shin. "A Compact Model for Program Operation of Gate-All-Around Barrier-Engineered Charge-Trapping NAND Flash Memory in the FN-Tunneling Regime". *IEEE Journal of the Electron Devices Society (JEDS)*.
- Hyungjun Jo, Hyungcheol Shin. "Compact Modeling of Trap-Assisted Tunneling Current in 3-D nand Flash Memory". *IEEE Transactions on Electron Devices*.
- Sangmin Ahn, Hyungjun Jo, Sechun Park, Jongwoo Kim, Hyungcheol Shin. "Investigation of Cell Variation Effect on Z-Interference in Charge-Trap-Based 3-D NAND Flash Memory". *IEEE Transactions on Electron Devices*.
- Eunseok Oh, Hyungcheol Shin. "Investigation of Random Telegraph Noise Scaling Dependency in 3-D NAND Using Monte Carlo Simulator". *IEEE Transactions on Electron Devices*.
- Juhyun Kim, Hyungcheol Shin. "Modeling of effective mobility in 3D NAND flash memory with polycrystalline silicon channel". *Journal of Computational Electronics (JCE)*.
- Mingyu Kim, Ilho Myeong, Jaehyun Park, Sungil Park, Deukho Yeon, Daewon Ha, Hyungcheol Shin. "Development of SRAM in 3-Dimensional Stacked FET With Direct Backside Contact Beyond 1Nm Node". *IEEE Transactions on Nanotechnology (TNANO)*.
- Sungju Kim, Hyungcheol Shin. "Closed-Form Capacitance Network Compact Model and Monte Carlo Analysis of the GIDL Assisted Potential Growth in 3 D NAND Flash String". *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD)*.
- Jinil Yoo, Hyungcheol Shin. "Implementation of long short-term memory for randomized incremental step pulse programming and scheme-wise investigation of 3D NAND flash memories". *Japanese Journal of Applied Physics (JJAP)*.
- Jaeyeop Jung, Sungju Kim, Sechun Park, Sung-Hyun Hwang, Donghun Kwak, Hyungcheol Shin. "An advanced scheme to match electric field between program verify and read operation in 3D NAND flash memory". *Japanese Journal of Applied Physics (JJAP)*.
- Jaeyeop Jung, and Hyungcheol Shin. “Negative Boosting Control of Channel Potential in Open Block Read Operation for 3D NAND Flash Memory.”
- Sungju Kim, Haechan Choi, Sechun Park, and Hyungcheol Shin, “Physics-Based Closed-Form GIDL-Assisted Erase Compact Model: SPICE Framework for Vth Distribution Simulator of 3D NAND Flash”, 2025 71st IEEE International Electron Devices Meeting (IEDM), 2025
- Changhyeok Im, Sungju Kim and Hyungcheol Shin, “A Compact Model for GIDL-Assisted Erase Transients of 3D MONOS Charge-Trap NAND Flash Memories”, 2025 9th IEEE Electron Devices Technology & Manufacturing Conference (EDTM), 2025
- Jooyoung Lee, Jinil Yoo and Hyungcheol Shin, “Investigation of Reliability and Optimization of Reprogram Process in 3D NAND Flash Memory Based on Physical Model”, 2025 9th IEEE Electron Devices Technology & Manufacturing Conference (EDTM), 2025

**2024**

- Jinil Yoo, Sangmin Ahn, Hyungcheol Shin. "Integra-NANDSim: A New VT Distribution Simulator of 3-D NAND Flash Memories". *IEEE Journal of the Electron Devices Society*.
- Insang Han, Jang Kyu Lee, Sangmin Ahn, Hyungcheol Shin. "Machine Learning-Based Prediction of Threshold Voltage Distribution Due to Lateral Migration in 3-D NAND Flash Memory". *IEEE Transactions on Electron Devices*.
- Eunseok Oh, Hyungcheol Shin. "Prediction of Random Telegraph Noise-induced Threshold Voltage Shift and Its Scaling Dependency Using Machine Learning". *IEEE Journal of the Electron Devices Society*.
- Jinil Yoo, Haechan Choi, Hyungcheol Shin. "A New Semi-Analytical Model for Erase Transients of 3-D Gate-All-Around (GAA) NAND Flash Memories". *IEEE Transactions on Electron Devices(TED)*.
- Jinil Yoo, Hyungjun Jo, Hyungcheol Shin. "Time Constant Analysis of Lateral Charge Loss in 3-D NAND Flash Memories Through Multiscale Simulations". *IEEE Transactions on Electron Devices(TED)*.
- Sungju Kim, Sangmin Ahn, Sechun Park, Jongwoo Kim, Hyungcheol Shin. "Program Start Bias Grouping to Compensate for the Geometric Property of a String in 3-D NAND Flash Memory". *IEEE Journal of the Electron Devices Society*.
- Seongjae Cho, Sung-Tae Lee, Soomin Kim, Hyungcheol Shin. "A more practical indicator of MAC operational power efficiency inside memory-based synapse array". *JOURNAL OF SEMICONDUCTOR TECHNOLOGY AND SCIENCE*.
- Haechan Choi, Jinil Yoo, Hyungcheol Shin. "A New Physical Model for Program Transients of Cylindrical Charge-Trap-Based NAND Flash Memories". *IEEE Transactions on Electron Devices(TED)*.
- Hyungjun Jo, Jongwoo Kim, Yonggyu Cho, Hyunyoung Shim, Jaesung Sim, Hyungcheol Shin. "Investigation of Endurance Characteristics in 3-D nand Flash Memory With Trap Profile Analysis". *IEEE Transactions on Electron Devices(TED)*.
- Soomin Kim, Seongjae Cho, Woo Young Choi, and Hyungcheol Shin, “Processing and Characterization of Polycrystalline Silicon for Ultra-Low-Power Neuromorphic Applications,” Proceedings of 2024 Materials Research Society (MRS) Fall Meeting & Exhibit, EL05.11.03, Boston, MA, USA, Dec. 1–6, 2024.
- Haechan Choi, Hyungcheol Shin , “A Compact Model for Program Operation of Gate-All-Around Barrier-Engineered Charge-Trapping NAND Flash Memories” , IEEE Electron Devices Technology & Manufacturing Conference (EDTM), 2024
- Jinil Yoo and Hyungcheol Shin, “A Compact Model-Based Threshold Voltage Distribution Simulation of 3D Gate-All-Around (GAA) NAND Flash Memories,” IEEE Electron Devices Technology and Manufacturing Conference (EDTM), 2024.
- Donghyuk So and Hyungcheol Shin, “Temperature Dependency of Endurance and Recovery Characteristics in 3D NAND Flash Memories,” Korea Conference on Semiconductor (KCS), 2024.
- Insang Han, Sangmin Ahn, and Hyungcheol Shin, “Investigation of Grain Boundary Effect on Threshold Voltage and ISPP Slope in 3D NAND Flash Memories,” Korea Conference on Semiconductor (KCS), 2024.
- Hwanheechan Choi, Jangkyu Lee, and Hyungcheol Shin, “Process Variability Analysis in 3D NAND Macaroni Structures : Machine Learning for Predicting Program and Erase Characteristics,” Korea Conference on Semiconductor (KCS), 2024.
- Jooyoung Lee and Hyungcheol Shin, “Quantitative Analysis on Z-Interference using Reprogram Scheme in 3D NAND Flash Memory Vth Distribution,” Korea Conference on Semiconductor (KCS), 2024.

**2023**

- Juhyun Kim and Hyungcheol Shin. "Temperature Dependence Modeling of Grain Boundary Barrier Height in Macaroni MOSFETs". *IEEE Transactions on Electron Devices(TED)*.
- Quan Nguyen-Gia and Hyungcheol Shin. "Modeling of Threshold Voltage Shift by Neighboring Transistors for Macaroni Channel MOSFETs in Series". *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD)*.
- Jang Kyu Lee, Eunseok Oh and Hyungcheol Shin. "Monte Carlo Simulator for Threshold Voltage Distribution of 3-D nand Flash Memory Using Machine Learning". *IEEE Transactions on Electron Devices(TED)*.
- Sangmin Ahn, Hyungjun Jo, Sungju Kim, Sechun Park, Kyunam Lim, Jongwoo Kim and Hyungcheol Shin. "An Innovative Program Scheme for Reducing Z-Interference in Charge-Trap-Based 3-D NAND Flash Memory". *IEEE Transactions on Electron Devices(TED)*.
- Hyungjun Jo, Jongwoo Kim and Hyungcheol Shin. "A Novel Read Scheme Using GIDL Current to Suppress Read Disturbance in 3-D nand Flash Memories". *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD)*.
- Sungju Kim and Hyungcheol Shin, “Analysis of Vth distribution based on physical parameter variation for 3-D TLC NAND flash memory”, International Technical Conference on Circuits/Systems, Computers and Communications (ITC-CSCC), 2023.
- Haechan Choi and Hyungcheol Shin, “A Compact Model for Transient Program Operation of  Barrier Engineered Charge-Trapping NAND Flash Memories,” 대한전자공학회 하계학술대회, 2023.
- Sangmin Ahn and Hyungcheol Shin, “The Investigation of Random Telegraph Noise effect on the Extremely Narrow Vth Distribution in 3D NAND Flash Memory,” 대한전자공학회 하계학술대회, 2023.

**2022**

- Jongwoo Kim, Hyungjun Jo, Yonggyu Cho, Hyunyoung Shim, Jaesung Sim, and Hyungcheol Shin. "Investigation of endurance degradation for 3-D charge trap NAND flash memory with bandgap-engineered tunneling oxide". *IEICE Electronics Express*.
- Juhyun Kim, and Hyungcheol Shin. "Modeling of Grain Boundary Barrier Height for Undoped Polycrystalline Silicon Channel in Macaroni MOSFETs". *IEEE Transactions on Electron Devices(TED)*.
- Hyungjun Jo, Sangmin Ahn, and Hyungcheol Shin. "Investigation and Modeling of Z-Interference in Poly-Si Channel-Based 3-D NAND Flash Memories". *IEEE Transactions on Electron Devices(TED)*.
- Jang Kyu Lee, Kyul Ko, and Hyungcheol Shin. "Prediction of Random Grain Boundary Variation Effect of 3-D NAND Flash Memory Using a Machine Learning Approach". *IEEE Transactions on Electron Devices(TED)*.

**2021**

- Kul Lee and Hyungcheol Shin. "Distinguishing capture cross-section parameter between GIDL erase compact model and TCAD". *Japanese Journal of Applied Physics*.
- Shinkeun Kim and Hyungcheol Shin. "Analysis of the Effect of Residual Holes on Lateral Migration During the Retention Operation in 3-D NAND Flash Memory". *IEEE Transactions on Electron Devices(TED)*.
- Sangmin Ahn and Hyungcheol Shin. "Optimizing read disturb phenomenon with new read scheme by partial-boosting channel in 3-D NAND Flash memories". *IEICE Electronics Express*.
- Quan Nguyen-Gia and Hyungcheol Shin. "A Potential Model of Triple Macaroni Channel MOSFETs in Subthreshold Region". *IEEE Transactions on Electron Devices(TED)*.
- Minsoo Kim and Hyungcheol Shin. "Analysis and Compact Modeling of Fast Detrapping From Bandgap-Engineered Tunneling Oxide in 3-D NAND Flash Memories". *IEEE Transactions on Electron Devices(TED)*.
- Ilho Myeong and Hyungcheol Shin. "Study on self-heating effect and lifetime in vertical-channel field effect transistor". *Microelectronics Reliability*.
- Dongchan Lee and Hyungcheol Shin. "Machine learning model for predicting threshold voltage by taper angle variation and word line position in 3D NAND flash memory". *IEICE Electronics Express*.
- Quan Nguyen-Gia , Myounggon Kang, Jongwook Jeon, and Hyungcheol Shin, “Semi-Analytical Model of Subthreshold Current for Macaroni Channel MOSFET”, IEEE Silicon Nanoelectronics Workshop (SNW), 2021.
- Hyungjun Jo and Hyungcheol Shin, “New Read Schemes to Reduce Read Disturbance Due to HCI in Full Boosting Channel 3-D NAND Flash Memories”, IEEE Silicon Nanoelectronics Workshop (SNW), 2021.

## 연락과 위치

- 연구실: 서울특별시 관악구 관악로 1 서울대학교 301동 1017호[^contact]
- 교수 연구실: 104-1동 315호[^prof]
- 연구실 연락 이메일: khutkd02@snu.ac.kr[^home]
- 연구실 전화: 02-880-8647[^lab]
[^home]: 연구실 누리집 첫 화면. <https://snudrl.snu.ac.kr/> 연구실 이름, 반도체 소자 모델링·분석, 3차원 낸드 플래시, 기계학습 연구 소개와 연락 이메일.
[^lab]: 서울대학교 전기·정보공학부 연구실 상세 「반도체 소자 연구실」. <https://ece.snu.ac.kr/research-faculty/research/lab?labidx=56&md=view> 지도교수, Device Research Lab., 연구 분야와 전화.
[^prof]: 서울대학교 전기·정보공학부 신형철 교수 소개. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p059> 직위·전공·연구 관심·교수 연구실 위치.
[^pi]: 연구실 누리집 신형철 교수 약력. <https://snudrl.snu.ac.kr/member/%EC%8B%A0%ED%98%95%EC%B2%A0/> 학위·경력·서울대 2003년 재직 시작과 연구 대상.
[^members]: 연구실 MEMBER 목록 <https://snudrl.snu.ac.kr/member/> 및 각 구성원 개인 소개. 연구교수·과정·학교 이메일은 목록, 연구 주제는 개인 소개에 게시되어 있다. 추가 과정 분류는 유진일 <https://snudrl.snu.ac.kr/member/%EC%9C%A0%EC%A7%84%EC%9D%BC/>, 이주영 <https://snudrl.snu.ac.kr/member/%EC%9D%B4%EC%A3%BC%EC%98%81/>, 임동우 <https://snudrl.snu.ac.kr/member/%EC%9E%84%EB%8F%99%EC%9A%B0/>의 개인 소개에서 확인했다.
[^journals]: 연구실 PAPERS 목록 <https://snudrl.snu.ac.kr/journal/> 및 개별 논문 서지. 최근 논문 목록의 학술지 48편과 개별 주소는 근거 페이지의 읽은 자료 표에 적었다.
[^conferences]: 연구실 CONFERENCES 목록 <https://snudrl.snu.ac.kr/conference/> 및 개별 학회 서지. 누리집이 게시한 제목과 서지 문장을 옮겼다.
[^contact]: 연구실 홍규식 연구교수 개인 소개의 공통 연락처. <https://snudrl.snu.ac.kr/member/%ED%99%8D%EA%B7%9C%EC%8B%9D/> 서울대학교 301동 1017호.
[^alumni]: 누리집 ALUMNI 분류 <https://snudrl.snu.ac.kr/member_tax/alumni/>의 구성원 개별 소개 25쪽. 각 이름의 개별 주소는 졸업생 표에 연결했다.
[^p1]: H. Choi, J. Yoo, H. Shin, IEEE Transactions on Electron Devices (2026, 누리집·등록 연도). <https://doi.org/10.1109/ted.2026.3664277> 초록 기준(OpenAlex 등록 초록).
[^p2]: H. Choi 외, H. Shin, Japanese Journal of Applied Physics (2026, 누리집·등록 연도). <https://doi.org/10.35848/1347-4065/ae9c13> 초록 기준(Crossref 등록 초록).
[^p3]: E. Oh, H. Shin, Japanese Journal of Applied Physics (2026, 누리집·등록 연도). <https://doi.org/10.35848/1347-4065/ae334a> 초록 기준(Crossref 등록 초록).
[^p4]: S. Kim, J. Jung, H. Shin, IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2026, 누리집·등록 연도). <https://doi.org/10.1109/tcad.2026.3687153> 초록 기준(OpenAlex 등록 초록).
[^p5]: J. Lee, H. Shin, Journal of Computational Electronics (2026, 누리집·등록 연도). <https://doi.org/10.1007/s10825-026-02599-0> 초록 기준(Crossref 등록 초록).
[^p6]: H. Jo, H. Shin, IEEE Transactions on Electron Devices 72, 1745-1749 (2025). <https://doi.org/10.1109/ted.2025.3541603> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/389162636_Compact_Modeling_of_Trap-Assisted_Tunneling_Current_in_3-D_nand_Flash_Memory>
[^p7]: J. Lee, J. Yoo, H. Shin, Journal of Computational Electronics (2026, 누리집·등록 연도). <https://doi.org/10.1007/s10825-026-02613-5> 초록 기준(Crossref 등록 초록).
[^p8]: E. Oh, H. Shin, IEEE Transactions on Electron Devices 72, 6693-6698 (2025). <https://doi.org/10.1109/ted.2025.3622558> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/396993744_Impact_of_Elliptical_Cell_Geometry_and_Program_Voltage_on_RTN-Induced_Threshold_Voltage_Shift_in_3-D_NAND_Flash>

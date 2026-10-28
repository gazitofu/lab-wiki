# 센싱 지능 및 사이버-물리 보안 연구실 (Sensing Intelligence and Cyber-Physical Security Lab, CyPhy)

**KAIST 전산학부 · 한준 부교수**

- 분야: 일상 기기의 센싱, 모바일·무선 시스템의 보안과 프라이버시, 물리적 맥락을 이용한 인증, 디지털 자료의 진위와 출처 확인
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: 네트워크 보안·프라이버시[^p6], AI·기계학습 보안·프라이버시[^p4], 인간–컴퓨터 상호작용[^p2]
- 홈페이지: <https://www.cyphy.kaist.ac.kr/>
- 근거와 출처: [CyPhy 근거 페이지](cyphy-sources.md)

> 스마트폰·스마트워치와 주변의 물리 신호를 이용해 사물의 상태와 진위를 알아내고, 일상 기기에서 새어 나오는 정보와 인증 체계의 보안 문제를 연구한다.[^home][^research]

## 무엇을 연구하나

CyPhy는 한준 교수가 이끄는 연구실로, KAIST 전산학부와 싱가포르 국립대학교(NUS, National University of Singapore) 전산학부 구성원이 함께 참여한다. 센싱(주변 상태를 감지해 자료로 나타내는 일) 시스템과 모바일·임베디드 시스템(다른 기기 안에 들어가 특정 기능을 수행하는 컴퓨터 시스템), 무선 시스템의 보안과 프라이버시를 연구한다. 연구 대상에는 스마트 기기뿐 아니라 드론, 전동 킥보드, 차량과 사물인터넷(IoT, Internet of Things, 여러 사물이 통신망으로 연결되어 정보를 주고받는 체계)이 포함된다.[^home]

연구실은 물리적 맥락(기기 주변의 환경과 사건에 관한 정보)과 여러 종류의 센서 자료를 활용하는 Sensing-Augmented Physical AI를 제안한다. 센싱·모바일 시스템, 보안, 인공지능을 연결해 스마트 기기·차량·스마트홈·공장의 지능과 보안을 높이는 것이 목표다. 사이버-물리 시스템(CPS, Cyber-Physical Systems, 계산·통신과 물리적 과정이 연결되어 작동하는 시스템)을 대상으로 감지 능력을 확장하고, 물리 신호에서 비롯되는 보안 위험을 분석하며, 물리적 정보에 기반한 인증(주장한 신원을 확인하는 절차)을 연구한다.[^research]

일상 기기를 측정 도구로 쓰는 연구가 한 축이다. PowDew는 스마트폰으로 분말 식품의 진위를 판별하고, UniKey는 스마트워치로 평평한 표면에서의 타이핑을 알아낸다. 디지털 자료의 진위도 연구한다. CAMPrints는 편집된 이미지에 남은 카메라의 고유한 잡음 패턴을 비교해 이미지 도용을 탐지한다. 이렇게 이미 있는 기기의 감지 기능과 계산 방법을 연결해 새로운 확인 기능을 만드는 것이 공통된 접근이다.[^p1][^p2][^p3]

비접촉 센싱을 환자의 자세 기록에 연결하는 연구도 한다. SARPos는 밀리미터파 레이더(mmWave radar, 밀리미터 단위 파장의 전파를 보내고 반사 신호로 대상을 감지하는 장치)를 이용한 누운 자세 감시 시스템이다. 합성 개구 레이더(SAR, Synthetic Aperture Radar, 여러 관측 지점의 신호를 합쳐 영상을 얻는 레이더 방식)로 자세의 형상 정보를 얻고, 반지도 분류(정답이 붙은 자료와 정답 없는 자료를 함께 이용하는 분류 방법)를 결합한다. 민감한 시각 영상을 사용하지 않으면서 누운 자세를 기록할 가능성을 예비 평가로 보였다.[^p7]

또 다른 축은 시스템이 의도하지 않은 통로로 무엇을 드러내는지 확인하는 일이다. 부채널(정규 출력 밖에서 정보가 새어 나오는 통로)을 통해 인공지능 모델의 구조가 드러나는 위험, 얼굴 이미지로 만든 합성 음성이 음성 인증을 위협하는 문제, 무선 통신 정보에서 사람의 움직임이 드러나는 문제를 다룬다. 위험의 발견과 함께 무선 정보의 내용을 흐려 프라이버시를 보호하는 방어 방법도 제안한다.[^p4][^p5][^p6]

## 주요 연구 주제

### 감지·입력 기능 확장과 비접촉 관측

스마트폰 카메라와 스마트워치 같은 일상 기기를 활용해 원래의 사용 기능 밖에 있는 정보를 알아낸다. PowDew에서는 분말 위 물방울의 퍼짐과 스며듦을 관찰해 분말 식품의 진위를 판단한다. UniKey에서는 스마트워치로 표면을 두드리는 손가락의 움직임을 감지해 문자를 입력할 가능성을 시험한다. 두 연구는 별도 측정 장비나 입력 장치에 의존하는 문제를 일상 기기로 풀려는 접근을 보여 준다.[^p1][^p2]

SARPos는 레이더에서 얻은 자세의 형상과 분류 방법을 연결해 움직임이 제한된 환자의 누운 자세를 자동으로 기록하는 시스템을 제안한다. 자세 감시 시스템의 설계를 제시하고 예비 평가로 분류 가능성을 보였다.[^p7]

### 물리 신호와 인공지능 시스템의 보안

ModelSpy는 GPU(Graphics Processing Unit, 병렬 계산을 수행하는 처리 장치)에서 새어 나오는 전자기 신호와 신경망(서로 연결된 계산 단위로 자료의 관계를 학습하는 모형) 구조 사이의 관계를 분석해 모델 정보의 노출 위험을 평가한다. Foice 연구는 얼굴 이미지로부터 생성된 합성 음성이 음성 인증에 미치는 위험을 시험했다. 여기서 중요한 연구 질문은 모델 내부를 공개하지 않거나 음성 표본을 감춰 두는 것만으로 인증과 정보 보호가 성립하는가이다.[^p4][^p5]

### 통신 프라이버시와 디지털 자료의 출처

LeakyBeam은 WiFi의 빔포밍(신호를 특정 방향으로 보내도록 조절하는 기술) 피드백 정보가 사람의 움직임에 관한 정보를 드러낼 수 있음을 보이고, 그 정보를 흐리는 방어 방법을 제안한다. CAMPrints는 이미지의 편집 전후에 남은 카메라 잡음 패턴을 학습하고 비교해, 인터넷의 이미지와 사용자가 제시한 기준 이미지가 같은 카메라에서 왔는지 확인한다. 전자는 통신 이용자의 프라이버시를, 후자는 이미지의 출처와 도용 문제를 다룬다.[^p6][^p3]

### 물리적 맥락을 이용한 기기 인증

연구 소개의 Physics-guided Secure Authentication은 주변 환경과 센서 관측을 기기 인증에 연결하는 갈래다. 서로 다른 센서의 관측을 함께 이용하는 센서 융합(여러 감지 자료를 결합하는 방법)과 주변 사건에 대한 정보를 활용해 기기 사이의 연결을 인증한다. 연구실은 차량 안 기기 연결, 주변 사건을 함께 관측한 사물인터넷 기기의 연결, 드론 인증을 이 갈래의 연구 사례로 소개한다.[^research]

## 대표 논문

한준 교수의 KAIST 부임 이후인 2024–2026년 논문 중 초록을 읽을 수 있고 연구 갈래를 보여 주는 7편을 골랐다. 센싱·입력 기능, 디지털 자료의 진위, 시스템과 인공지능의 정보 유출, 환자 자세의 비접촉 센싱을 나누어 담았다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 교수의 역할 |
|---|---|---|---|---|
| 1 | 2024 | [PowDew: Detecting Counterfeit Powdered Food Products using a Commodity Smartphone](https://doi.org/10.1145/3643832.3661877) · ACM MobiSys | 스마트폰으로 분말 위 물방울의 움직임을 관찰해 위조 분유를 판별하는 시스템이다. 분말의 성질이 물방울의 퍼짐과 스며듦에 영향을 준다는 점을 이용한다. 여러 분유와 혼입물, 조건을 달리한 평가에서 전체 탐지 정확도가 최대 96.1%였다고 보고했다.[^p1] | 마지막 저자 |
| 2 | 2025 | [UniKey: Enabling Surface-Based Typing with Commodity Smartwatches via Cross-Modal Learning](https://doi.org/10.1145/3746059.3747611) · ACM UIST | 스마트워치로 평평한 표면에서 손가락을 두드리는 동작을 감지해 입력을 알아내는 방법이다. 사용자가 기존 키보드에서 보이는 타이핑 습관을 활용하며, 시제품과 여러 조건의 실험으로 일상적인 문자 입력에 쓸 가능성을 보였다.[^p2] | 마지막 저자 |
| 3 | 2025 | [CAMPrints: Leveraging the "Fingerprints" of Digital Cameras to Combat Image Theft](https://doi.org/10.1145/3711875.3729158) · ACM MobiSys | 인터넷에서 편집된 이미지를 찾았을 때, 그 이미지와 기준 이미지에 같은 카메라의 고유한 잡음 패턴이 남아 있는지 확인해 도용을 탐지한다. 다양한 편집 작업을 거친 뒤의 패턴을 학습하고 비교하는 시스템을 제시하고 실제 이미지로 평가했다.[^p3] | 마지막 저자 |
| 4 | 2026 | [Peering Inside the Black-Box: Long-Range and Scalable Model Architecture Snooping via GPU Electromagnetic Side-Channel](https://www.ndss-symposium.org/ndss-paper/peering-inside-the-black-box-long-range-and-scalable-model-architecture-snooping-via-gpu-electromagnetic-side-channel/) · NDSS | GPU의 물리 신호에서 공개되지 않은 인공지능 모델의 구조가 드러날 수 있는지를 평가한 연구다. 시제품과 실제 GPU 평가로 모델 구조의 기밀성이 물리적 정보 유출에 노출될 위험을 보였다.[^p4] | 공동 교신저자(랩 명시) |
| 5 | 2024 | [Can I Hear Your Face? Pervasive Attack on Voice Authentication Systems with a Single Face Image](https://www.usenix.org/conference/usenixsecurity24/presentation/jiang-nan) · USENIX Security | 얼굴 이미지로 만든 합성 음성이 음성 인증을 위협하는지 시험한 연구다. 음성 표본 없이도 만들어진 합성 음성에 대해 평가한 상용 서비스를 포함한 인증 시스템들이 취약함을 보였다.[^p5] | 마지막 저자 |
| 6 | 2025 | [Lend Me Your Beam: Privacy Implications of Plaintext Beamforming Feedback in WiFi](https://www.ndss-symposium.org/ndss-paper/lend-me-your-beam-privacy-implications-of-plaintext-beamforming-feedback-in-wifi/) · NDSS | WiFi가 주고받는 피드백 정보에 사람의 움직임에 관한 정보가 남아 프라이버시 위험으로 이어질 수 있음을 보였다. 이 정보를 흐리게 하는 방어 방법도 제안해 통신 기기의 정보 보호 문제를 다뤘다.[^p6] | 공저자(5명 중 4번째) |
| 7 | 2026 | [Poster: Lying Position Monitoring for Immobile Patients via mmWave Imaging](https://doi.org/10.1145/3812835.3814876) · ACM MobiSys Companion, 포스터 초록 | 움직임이 제한된 환자의 누운 자세를 자동으로 기록하는 SARPos 시스템을 제안한다. 레이더로 얻은 자세의 형상 정보와 반지도 분류를 결합하며, 민감한 시각 영상을 사용하지 않는 자세 감시의 가능성을 예비 평가로 보였다.[^p7] | 마지막 저자 |

## 교수와 전문 분야

한준(Jun Han) 교수는 KAIST 전산학부 부교수다. 2018년 Carnegie Mellon University에서 IoT 보안 연구로 컴퓨터공학 박사학위를 받았고, 싱가포르 국립대학교와 연세대학교에서 조교수로 근무한 뒤 2024년 2월 KAIST에 부임했다. 학과 소개는 연구분야를 시스템·네트워크, 시큐어 컴퓨팅, 인터랙티브 컴퓨팅으로, 전공을 IoT/CPS Security로 적는다.[^faculty]

전문 분야는 보안과 모바일·센싱 시스템이 만나는 지점에 있다. 주변의 환경과 사건에 관한 정보를 이용해 사물인터넷과 사이버-물리 시스템의 보안 문제를 해결하는 시스템을 제안한다.[^faculty] 최근 논문으로 보면 스마트폰을 이용한 물리적 진위 판별, 스마트워치 입력, 이미지 출처 확인, 인공지능 모델과 인증 시스템의 정보 보호, 레이더를 이용한 환자 자세 감시가 연결된다.[^p1][^p2][^p3][^p4][^p5][^p7] 연구실 소식에는 ACM MobiSys’24 Workshops Chair와 모바일·센싱·보안 학회 기술 프로그램 위원회 활동이 게시되어 있다.[^news]

## 응용 분야

스마트폰을 이용한 분말 식품 진위 확인, 스마트워치를 이용한 일상 문자 입력, 이미지 도용 탐지, 음성 인증과 무선 통신 이용자의 프라이버시 보호가 대표적인 응용이다.[^p1][^p2][^p3][^p5][^p6] SARPos는 움직임이 제한된 환자의 누운 자세 기록을 돕는 비접촉 감시를 목표로 한다.[^p7] 연구실은 스마트 기기·드론·차량·스마트홈·공장을 대상으로 물리적 맥락과 센싱을 활용해 보안과 지능을 높이는 방향을 제시한다.[^research]

## 구성원

2026년 10월 27일 Team 페이지가 게시한 교수 외 연구 구성원 18명이다. KAIST 학생 15명과 NUS 박사과정 3명이며, 과정·시작 시기·학교 이메일은 랩 표기다. ‘대표 논문 참여’는 위 표의 번호로, 이름 표기가 같은 저자를 같은 사람으로 보아 표시했다.[^team]

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Changgeon Kang | Ph.D. student at KAIST |  | kangha02@kaist.ac.kr |  |
| Gyuyeon Kim | Ph.D. student at KAIST |  | gyuyeonkim@kaist.ac.kr |  |
| Nayoung Kim | M.S. student at KAIST |  | skdud727@kaist.ac.kr |  |
| Jihyun Lee | Ph.D. student at KAIST | starting Fall 2026 | gh9439@kaist.ac.kr | 7 |
| Sungmin Park | M.S. student at KAIST |  | everydai@kaist.ac.kr |  |
| Dongjin Seo | M.S. student at KAIST |  | dongjinseo@kaist.ac.kr |  |
| Jaewoo Son | M.S. student at KAIST |  | jaewoo1940@kaist.ac.kr |  |
| Sihun Yang | Ph.D. student at KAIST |  | sihunyang@kaist.ac.kr | 7 |
| Dongmin Yu | M.S. student at KAIST |  | dongminyu@kaist.ac.kr | 7 |
| Jonghyuk Yun | Ph.D. student at KAIST |  | jonghyuk.yun@kaist.ac.kr | 1 |
| Yeongjun Joo | Undergraduate intern at KAIST |  |  |  |
| Minjoon Kee | Undergraduate intern at KAIST |  |  |  |
| Sojeong Kim | Undergraduate intern at KAIST |  |  |  |
| Jaejun Lee | Undergraduate intern at KAIST |  |  |  |
| Sangyoon Lim | Undergraduate intern at KAIST |  |  |  |
| Nan Jiang | Ph.D. candidate at NUS (co-advised by Prof. Terence Sim) |  | jiangnan@comp.nus.edu.sg | 5 |
| Bangjie Sun | Ph.D. candidate at NUS (co-advised by Prof. Mun Choon Chan) |  | bangjie@comp.nus.edu.sg | 1, 3, 5 |
| Sean RuiXiang Tan | Ph.D. candidate at NUS (co-advised by Prof. Mun Choon Chan) |  | seantanr@comp.nus.edu.sg | 2 |

## 졸업생과 이전 구성원

Team 페이지 Former Members의 52명이다. 박사학위 연도가 적힌 3명은 2022년과 2025년 졸업생이며, 나머지는 연도가 적혀 있지 않다. NUS·연세대학교 등 한준 교수의 이전 소속 시기 구성원도 함께 포함한다. 학위·과정과 진로는 랩 표기이며, 기관이 과정 칸에 함께 적힌 경우 당시의 소속이다.[^team]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Soundarya Ramesh | Ph.D., CS at NUS (co-advised by Prof. Mun Choon Chan) (2025) | Meta |
| Sriram Sami | Ph.D., CS at NUS (co-advised by Prof. Mun Choon Chan) (2025) | Lecturer, NUS |
| Nitya Lakshmanan | Ph.D., CS at NUS (co-advised by Prof. Min Suk Kang) (2022) | Lecturer, NUS |
| Jong Taek Lee | PostDoc, Computer Science at NUS | Associate Professor, Kyungpook National University |
| Jay Prakash | PostDoc, Computer Science at NUS | Founder and CEO, Silence Laboratory |
| Jinhyun Baek | Undergraduate Intern - KAIST |  |
| YeongBin Byeon | Undergraduate Intern - KAIST |  |
| Yuri Choi | Undergraduate Intern - Yonsei |  |
| Ivan Damnjanovic | M.S. Research Assistant - NUS |  |
| Anuj Dhawan | Undergraduate Intern - NUS |  |
| Seojun Hong | Undergraduate Intern - Yonsei |  |
| Hyewon Hwang | Undergraduate Intern - Yonsei |  |
| Jaeho Jeon | Undergraduate Intern - Yonsei |  |
| Seoyul Jeon | Undergraduate Intern - KAIST |  |
| Junhyeong Jeon | Undergraduate Intern - KAIST |  |
| Yunho Jung | Undergraduate Intern - Yonsei |  |
| Cherry Kim | M.S. student - Yonsei |  |
| Dongjun Kim | Undergraduate Intern - Yonsei |  |
| Byunghyun Kim | Undergraduate Intern - KAIST |  |
| Hyunwoo Kim | Undergraduate intern  - Yonsei |  |
| Hojune Kim | Undergraduate Intern - KAIST |  |
| Junhyeop Kim | Undergraduate intern - KAIST |  |
| Junyong Kim | Undergraduate Intern - KAIST |  |
| Seonho Kim | Undergraduate intern - Yonsei |  |
| Seungjae Kim | Undergraduate intern - KAIST |  |
| Sungtae Kim | Undergraduate Intern - Yonsei |  |
| Ananda Kumar | Undergraduate Research Assistant - NUS |  |
| Jun Kiat Kwok | M.S. Research Assistant - NUS |  |
| Donghun Lee | Undergraduate Intern - Yonsei |  |
| KyooSik Lee | Undergraduate Intern - Yonsei |  |
| Yeonjun Lee | Undergraduate Intern - KAIST |  |
| Eric Yu Kai Lim | M.S. Research Assistant - NUS |  |
| Sehoon Lim | Undergraduate Intern - KAIST |  |
| Jaeyoung Moon | Undergraduate Intern - KAIST |  |
| Wah Chun Ng | M.S. Research Assistant - NUS |  |
| Thomas Daniel Paul Pathier | M.S. Research Assistant - NUS |  |
| Jimin Park | Undergraduate Intern - KAIST |  |
| Seungbeom Park | Undergraduate Intern - KAIST |  |
| Yunseo Park | Undergraduate Intern - KAIST |  |
| Harini Ramprasad | Undergraduate Intern - NUS |  |
| Christian August Reksten-Monsen | M.S. Research Assistant - NUS |  |
| Zhiwei Ren | M.S. Research Assistant - NUS |  |
| Tomiris Sharipbay | Undergraduate Intern at KAIST |  |
| Smitha Sheshadri | M.S. Research Assistant - NUS |  |
| Jaewon Shin | Undergraduate Intern at KAIST |  |
| Madhan Vignesh Srinivasan | M.S. Research Assistant - NUS |  |
| Lionel Ee Siang Teo | M.S. Research Assistant - NUS |  |
| Rui Xiao | Undergraduate Research Assistant - NUS |  |
| Dai Yimin | Undergraduate Research Assistant - NUS |  |
| Seojin Yun | Undergraduate Intern at KAIST |  |
| Gucheng Wang | Ph.D. candidate - NUS | Currently advised by Prof. Terence Lim |
| Seongjin Wang | Undergraduate Intern - Yonsei |  |

## 최근 논문 목록 (2021–2026)

스마트 기기의 센싱과 입력, 환자의 자세·상태 인식, 영상의 진위, 무선·모바일 시스템의 보안과 프라이버시를 다룬다. Publications의 2021–2026년 구역에서 논문·초청 글·사전 공개본·포스터 초록·포스터 발표·데모 초록 45건을 실었다. 한준 교수의 2024년 2월 KAIST 부임 전 성과도 포함한다. 연도·제목·전체 저자·발표처는 랩 표기를 따르며, 2026년 ‘발표 예정’은 누리집의 To appear 표기다. 포스터와 데모, 확장 사전 공개본의 유형은 발표처 뒤에 표시했다.[^pubs][^faculty]

**2026**

- Kyoosik Lee, Jiha Kim, Jonghyuk Yun, Suwon Yoon, Jun Han\*, Inseok Hwang\* (\*co-corresponding). "Fold2Unfold: Screen Privacy Protection against Shoulder Surfing using Inter-Screen Reflection on Foldable Smartphones". *ACM Symposium on User Interface Software and Technology (발표 예정(누리집 표기))*.
- Gyuyeon Kim, Sehoon Lim, Jaewoo Son, Soundarya Ramesh, Jun Han. "AcousTag: Batteryless 3D-Printed Acoustic Tag for Smart Speaker-based Event Monitoring". *ACM International Joint Conference on Pervasive and Ubiquitous Computing (발표 예정(누리집 표기))*.
- Gyuyeon Kim, Jaewoo Son, Sungmin Park, and Jun Han. "AutoScale: Vision-Based Overweight Truck Detection Utilizing A Following Autonomous Vehicle". *IEEE/RSJ International Conference on Intelligent Robots and Systems*.
- Jonghyuk Yun, Jaeyoung Moon, Yunseo Park, Sean Rui Xiang Tan, Byunghyun Kim, Rajesh Krishna Balan, and Jun Han. "Hide-and-Sweep: Detecting Concealed Cameras via LED Illumination Sweeps". *ACM International Conference on Mobile Systems, Applications, and Services*.
- Nan Jiang, Juan Hu, Bangjie Sun, Terence Sim, and Jun Han. "WRATH: Turning Watermark Robustness Against Itself via a Watermark-Agnostic Black-Box Invalidation Attack". *IEEE Symposium on Security and Privacy*.
- Rui Xiao, Sibo Feng, Soundarya Ramesh, Jun Han\*, and Jinsong Han\* (\*co-corresponding). "Peering Inside the Black-Box: Long-Range and Scalable Model Architecture Snooping via GPU Electromagnetic Side-Channel". *Network and Distributed System Security Symposium*.
- Bangjie Sun, Sean Rui Xiang Tan, Rui Xiao, Mun Choon Chan, and Jun Han. "What Do Neighbors Know? Open-World Semantic Inference Attack on Intermediate Representations". *International Workshop on Networked AI Systems (Co-located workshop with ACM MobiSys'26)*.
- Nan Jiang, Bangjie Sun, Nayoung Kim, Terence Sim, and Jun Han. "RD-PHash: A Robustness Enhancement for DCT-Based Perceptual Hashing against Adversarial Bit-Flipping Attacks". *Workshop on Artwork Security and Provenance in the Age of AI (Co-located workshop with IEEE S&P'26)*.
- Jihyun Lee, Dongmin Yu, Sihun Yang, and Jun Han. "Poster: Lying Position Monitoring for Immobile Patients via mmWave Imaging". *ACM International Conference on Mobile Systems, Applications, and Services (포스터 초록)*.[^p7]
- Jonghyuk Yun, Jaeyoung Moon, Yunseo Park, Sean Rui Xiang Tan, Byunghyun Kim, Rajesh Balan, and Jun Han. "Poster: Detecting Hidden Cameras using LED Illumination Sweeps". *ACM International Conference on Mobile Systems, Applications, and Services (포스터 초록)*.
- Bangjie Sun, Sean Rui Xiang Tan, Rui Xiao, Mun Choon Chan, and Jun Han. "Poster: Discovering Unanticipated Semantic Leakage from Intermediate Representations". *ACM International Conference on Mobile Systems, Applications, and Services (포스터 초록)*.

**2025**

- Sean Rui Xiang Tan, Mun Choon Chan, and Jun Han. "UniKey: Enabling Surface-Based Typing with Commodity Smartwatches via Cross-Modal Learning". *ACM Symposium on User Interface Software and Technology*.
- Bangjie Sun, Mun Choon Chan, and Jun Han. "CAMPrints: Leveraging the "Fingerprints" of Digital Cameras to Combat Image Theft". *ACM International Conference on Mobile Systems, Applications, and Services*.
- Rui Xiao, Xiankai Chen, Yinghui He, Jun Han, and Jinsong Han. "Lend Me Your Beam: Privacy Implications of Beamforming Feedback Packets in WiFi". *Network and Distributed System Security Symposium*.
- Kichang Lee, Jonghyuk Yun, Jaeho Jin, Jun Han, JeongGil Ko. "Mind Your Indices! Index Hijacking Attacks on Collaborative Unpooling Autoencoder Systems". *Internet of Things, Volume 29, Article 101462, January 2025*.
- Bangjie Sun, Mun Choon Chan, and Jun Han. "Poster: CAMPrints: Leveraging the “Fingerprints” of Digital Cameras to Combat Image Theft". *ACM International Conference on Mobile Systems, Applications, and Services (포스터 발표)*.

**2024**

- Jonghyuk Yun, Kyoosik Lee, Kichang Lee, Bangjie Sun, Jaeho Jeon, JeongGil Ko, Inseok Hwang, and Jun Han. "A Smartphone to the Rescue: Detecting Counterfeit Powdered Food Products (Invited Article)". *ACM GetMobile: Mobile Computing and Communications*.
- Shubham Rohal, Dong Yoon Lee, Carlos Ruiz, Joshua Zhang, Jonathon Fagert, Jun Han, and Shijia Pan. "Don’t Crosstalk to Me: Origami Structure-Augmented Sensing for Scalable Surface Pressure Monitoring". *ACM Conference on Embedded Networked Sensor Systems*.
- Nan Jiang, Bangjie Sun, Terence Sim, and Jun Han. "Can I Hear Your Face? Pervasive Attack on Voice Authentication Systems with a Single Face Image". *USENIX Security Symposium*.
- Jonghyuk Yun, Kyoosik Lee, Kichang Lee, Bangjie Sun, Jaeho Jeon, JeongGil Ko, Inseok Hwang, and Jun Han. "PowDew: Detecting Counterfeit Powdered Food Products using a Commodity Smartphone". *ACM International Conference on Mobile Systems, Applications, and Services*.
- Cherry Kim, Seongjin Wang, Dongjun Kim, Shijia Pan, and Jun Han. "ImpacTile: Tile-level Localization for the Visually Impaired using Structural Uniqueness". *ACM International Workshop on Mobile Computing Systems and Applications*.
- Dongjin Seo, Jonghyuk Yun, Seongjin Wang, Jaewoo Son, and Jun Han. "Poster: Towards Privacy Preserving Patient State Classification in Psychiatric Seclusion Room using mmWave Radar". *ACM Conference on Embedded Networked Sensor Systems (포스터 초록)*.[^supp-c2]
- Jonghyuk Yun, Kyoosik Lee, Kichang Lee, Bangjie Sun, Jaeho Jeon, JeongGil Ko, Inseok Hwang, and Jun Han. "Poster: Towards Counterfeit Powdered Food Products Detection using a Commodity Smartphone". *ACM International Conference on Mobile Systems, Applications, and Services (포스터 초록)*.
- Gyuyeon Kim, Hyunwoo Kim, and Jun Han. "Poster: Towards Acoustic-Based Tagless Object Tracking with Smartwatches". *ACM International Conference on Mobile Systems, Applications, and Services (포스터 초록)*.
- Changgeon Kang, Dongjin Seo, Sihun Yang, and Jun Han. "Poster: Exploiting Keystroke Dynamics via mmWave Radar for Application Profiling". *ACM International Conference on Mobile Systems, Applications, and Services (포스터 초록)*.
- Cherry Kim, Seongjin Wang, Dongjun Kim, Shijia Pan, and Jun Han. "Poster: ImpacTile: Tile-level Localization for the Visually Impaired using Structural Uniqueness". *ACM International Workshop on Mobile Computing Systems and Applications (포스터 초록)*.

**2023**

- Bangjie Sun, Kanav Sabharwal, Gyuyeon Kim, Mun Choon Chan, and Jun Han. "Testing Masks and Air Filters With Your Smartphones". *ACM Conference on Embedded Networked Sensor Systems*.
- Rui Xiao, Tianyu Li, Soundarya Ramesh, Jun Han\*, and Jinsong Han\* (\*co-corresponding). "MagTracer: Detecting GPU Cryptojacking Attacks via Magnetic Leakage Signals". *ACM International Conference On Mobile Computing And Networking*.
- Jong Taek Lee, Yu Kai Lim, Shijia Pan, and Jun Han. "Don't Weight to Board: Augmenting Vision-based Passenger Weight Prediction via Viscoelastic Mat". *ACM International Joint Conference on Pervasive and Ubiquitous Computing*.
- Connor Bolton, Yan Long, Jun Han, Josiah Hester, and Kevin Fu. "Characterizing and Mitigating Touchtone Eavesdropping in Smartphone Motion Sensors". *International Symposium on Research in Attacks, Intrusions, and Defenses*.
- Jonghyuk Yun, Gyuyeon Kim, Soundarya Ramesh, and Jun Han. "RampScope: Ramp-level Localization of Shared Mobility Devices using Sidewalk Ramps". *ACM International Workshop on Mobile Computing Systems and Applications*.
- Nakul Garg, Irtaza Shahid, Erin Avllazagaj, Jennie Hill, Jun Han, and Nirupam Roy. "ThermWare: Towards Side-channel Defense for Tiny IoT Devices". *ACM International Workshop on Mobile Computing Systems and Applications*.
- Jonghyuk Yun, Gyuyeon Kim, Soundarya Ramesh, and Jun Han. "Ramp-level Localization of Shared Mobility Devices using Sidewalk Ramps". *ACM International Workshop on Mobile Computing Systems and Applications (포스터 발표)*.
- Kichang Lee, Jonghyuk Yun, Jun Han, and JeongGil Ko. "Exploiting Indices for Man-in-the-Middle Attacks on Collaborative Unpooling Autoencoders". *ACM International Conference on Mobile Systems, Applications, and Services (데모 초록)*.

**2022**

- Soundarya Ramesh,  Ghozali Suhariyanto Hadi, Sihun Yang, Mun Choon Chan, and Jun Han. "TickTock: Detecting Microphone Status in Laptops Leveraging Electromagnetic Leakage of Clock Signals". *ACM Conference on Computer and Communications Security*.
- Bangjie Sun, Sean Rui Xiang Tan, Zhiwei Ren, Mun Choon Chan, and Jun Han. "Detecting Counterfeit Liquid Food Products in a Sealed Bottle Using a Smartphone Camera". *ACM International Conference on Mobile Systems, Applications, and Services*.
- Nitya Lakshmanan, Abdelhak Bentley, Byoungjun Choi, Roger Zimmermann, Jun Han, and Min Suk Kang. "On Privacy Risks of Watching YouTube over Cellular Networks with Carrier Aggregation". *ACM International Joint Conference on Pervasive and Ubiquitous Computing*.
- Nan Jiang, Terence Sim, and Jun Han. "EarWalk: Towards Walking Posture Identification using Earables". *ACM International Workshop on Mobile Computing Systems and Applications*.[^supp-c4]
- Soundarya Ramesh,  Ghozali Suhariyanto Hadi, Sihun Yang, Mun Choon Chan, and Jun Han. "TickTock: Detecting Microphone Status in Laptops Leveraging Electromagnetic Leakage of Clock Signals (Extended Version of ACM CCS'22 paper)". *arXiv:2209.03197 [cs.CR], Sep. 2022 (사전 공개본)*.
- Bangjie Sun, Sean Rui Xiang Tan, Zhiwei Ren, Mun Choon Chan, and Jun Han. "Poster: On Utilizing Smartphone Cameras to Detect Counterfeit Liquid Food Products". *ACM International Conference on Mobile Systems, Applications, and Services (포스터 초록)*.

**2021**

- Sriram Sami, Sean Rui Xiang Tan, Bangjie Sun, and Jun Han. "LAPD: Hidden Spy Camera Detection using Smartphone Time-of-Flight Sensors". *ACM Conference on Embedded Networked Sensor Systems*.
- Soundarya Ramesh, Rui Xiao, Anindya Maiti, Jong Taek Lee, Ananda Kumar, Harini Ramprasad, Murtuza Jadliwala, and Jun Han. "Acoustics to the Rescue: Physical Key Inference Attack Revisited". *USENIX Security Symposium*.
- Nitya Lakshmanan, Nishant Budhdev, Min Suk Kang, Mun Choon Chan, and Jun Han. "A Stealthy Location Identification Attack Exploiting Carrier Aggregation in Cellular Networks". *USENIX Security Symposium*.
- Mikhail Fomichev, Julia Hesse\*, Lars Almon, Timm Lippert, Jun Han\*, and Matthias Hollick\* (\*co-corresponding). "FastZIP: Faster and More Secure Zero-Interaction Pairing". *ACM International Conference on Mobile Systems, Applications, and Services*.
- Sriram Sami, Sean Tan Rui Xiang, Bangjie Sun, and Jun Han. "On Utilizing Smartphone Time-of-Flight Sensors to Detect Hidden Spy Cameras". *ACM Conference on Embedded Networked Sensor Systems (포스터 초록)*.

## 연구 과제

2023년 9월과 2024년 8월 소식에 적힌 지원 과제 2건이다. 2023년 항목은 KAIST 부임 전 선정 소식이다. 날짜는 선정 소식의 게시 연월이며, 기간은 지원 기간으로 게시한 값이다.[^news]

- 2024.8 · STEAM Global Cooperative Convergence Research Program 국제 공동 연구 (역할 PI: Jun Han; 협력 기관 KAIST, MIT, NUS; 지원 National Research Foundation (NRF); 기간 4.5년; 연구비 54억 원)
- 2023.9 · Mid-Career Researcher Program (중견연구) (지원 National Research Foundation (NRF); 기간 4년)

## 수상과 선정

2021년 10월 13일–2026년 10월 13일 범위에서 수상 시기를 확인할 수 있는 8건이다. 상 이름과 수상 대상은 Awards & Recognition 표기를 따랐으며, 2022–2025년 연월은 연구실 소식의 수상 공지 시점이다. 2026년 NDSS 항목은 학회 개최 기간을 함께 적었다. 한준 교수의 KAIST 부임 전 수상도 포함한다.[^awards][^news][^ndss2026]

- 2026 (학회 2월 23–27일) · Distinguished Paper Award [NDSS'26] · Peering Inside the Black-Box: Long-Range and Scalable Model Architecture Snooping via GPU Electromagnetic Side-Channel · Rui Xiao, Sibo Feng, Soundarya Ramesh, Jun Han, Jinsong Han
- 2025.6 · Best Poster Award [MobiSys'25] · Poster: CAMPrints: Leveraging the “Fingerprints” of Digital Cameras to Combat Image Theft · Bangjie Sun, Mun Choon Chan, Jun Han
- 2024.11 · Best Poster Award [SenSys'24] · Poster: Towards Privacy Preserving Patient State Classification in Psychiatric Seclusion Room using mmWave Radar · Dongjin Seo, Jonghyuk Yun, Seongjin Wang, Jaewoo Son, Jun Han
- 2024.6 · Best Paper Award [MobiSys'24] · PowDew: Detecting Counterfeit Powdered Food Products using a Commodity Smartphone · Jonghyuk Yun, Kyoosik Lee, Kichang Lee, Bangjie Sun, Jaeho Jeon, JeongGil Ko, Inseok Hwang, Jun Han
- 2024.6 · Best Presentation Award of Rising Stars Forum [MobiSys'24] · Your Mic Leaks Too Much: A Double-Edged Sword for Security · Soundarya Ramesh
- 2023.4 · Google Research Scholar Award · Utilizing Road Context for Augmentation and Verification of Vehicular Applications · Jun Han
- 2023.2 · Best Poster Award [HotMobile'23] · Poster: Ramp-level Localization of Shared Mobility Devices using Sidewalk Ramps · Jonghyuk Yun, Gyuyeon Kim, Soundarya Ramesh, Jun Han
- 2022.6 · Best Poster Award [MobiSys'22] · Poster: On Utilizing Smartphone Cameras to Detect Counterfeit Liquid Food Products · Bangjie Sun, Sean Rui Xiang Tan, Zhiwei Ren, Mun Choon Chan, Jun Han

## 소식

2021년 11월–2025년 9월에 게시한 연구·학술 활동 소식 35건이다. 한준 교수의 KAIST 부임 전 소식도 포함하며, 논문의 채택과 수상 공지는 해당 소식 당시의 상태를 적었다.[^news]

- 2025.9 · 연구실 이름을 Sensing Intelligence and Cyber-Physical Security (CyPhy) Lab으로 변경했다.
- 2025.7 · UniKey 논문이 ACM UIST’25에 채택되었다.
- 2025.6 · Bangjie Sun의 포스터가 ACM MobiSys’25 Best Poster Award를 받았다.
- 2025.3 · CAMPrints 논문이 ACM MobiSys’25에 조건부 채택되었다.
- 2024.11 · Lend Me Your Beam 논문이 NDSS’25에 채택되었다. Zhejiang University 공동 연구다.
- 2024.11 · 환자 상태 분류 포스터가 ACM SenSys’24 Best Poster Award를 받았다.
- 2024.11 · Don’t Crosstalk to Me 논문이 ACM SenSys’24에 채택되었다. UC Merced 공동 연구다.
- 2024.10 · 한준 교수가 ACM MobiSys’25, ACM MobiCom’25, IEEE S&P’25, ACM CCS’25의 TPC(기술 프로그램 위원회) 위원으로 초청되었다.
- 2024.8 · 한준 교수가 KAIST·MIT·NUS 국제 공동 연구 과제의 PI(연구책임자)를 맡았다. 한국연구재단 STEAM Global Cooperative Convergence Research Program에 선정되었다.
- 2024.6 · PowDew 논문이 ACM MobiSys’24 Best Paper Award를 받았다.
- 2024.6 · Soundarya Ramesh가 ACM MobiSys’24 Rising Stars Forum의 Best Presentation Award를 받았다.
- 2024.5 · Can I Hear Your Face? 논문이 USENIX Security’24에 채택되었다.
- 2024.4 · PowDew 논문이 ACM MobiSys’24에 채택되었다.
- 2024.2 · CyPhy Lab이 KAIST 전산학부로 이전했다.
- 2023.12 · ImpacTile 논문이 ACM HotMobile’24에 채택되었다.
- 2023.9 · 한준 교수가 한국연구재단 중견연구의 4년 연구 지원 대상으로 선정되었다.
- 2023.9 · Testing Masks and Air Filters With Your Smartphones 논문이 ACM SenSys’23에 채택되었다.
- 2023.9 · 한준 교수가 ACM MobiSys’24와 ACM/IEEE IPSN’24의 TPC 위원 및 ACM MobiSys’24의 Workshops Chair로 초청되었다.
- 2023.9 · 한준 교수가 뉴욕 Google Jigsaw의 Confronting Digital Authoritarianism 행사의 연사로 초청받았다.
- 2023.8 · 한준 교수가 서울 Samsung Security Tech Forum 2023의 연사로 초청받았다.
- 2023.6 · MagTracer 논문이 ACM MobiCom’23에 채택되었다.
- 2023.6 · Characterizing and Mitigating Touchtone Eavesdropping in Smartphone Motion Sensors 논문이 RAID’23에 채택되었다. University of Michigan·Northeastern University·Georgia Tech 공동 연구다.
- 2023.5 · 한준 교수가 USENIX Security’24와 IEEE S&P’24의 TPC 위원을 맡았다.
- 2023.4 · 한준 교수가 Google Research Scholar Award 2023에 선정되었다.
- 2023.3 · 한준 교수가 ACM MobiSys’23, ACM SenSys’23, ACM HotMobile’23, ACM/IEEE IoTDI’23의 TPC 위원을 맡았다.
- 2023.2 · RampScope 포스터가 ACM HotMobile’23 Best Poster Award를 받았다.
- 2022.12 · RampScope 논문이 ACM HotMobile’23에 채택되었다.
- 2022.12 · ThermWare 논문이 ACM HotMobile’23에 채택되었다. University of Maryland College Park 공동 연구다.
- 2022.10 · Don’t Weight to Board 논문이 ACM UbiComp’23/IMWUT에 채택되었다.
- 2022.8 · TickTock 논문이 ACM CCS’22에 채택되었다.
- 2022.6 · On Utilizing Smartphone Cameras to Detect Counterfeit Liquid Food Products 포스터가 ACM MobiSys’22 Best Poster Award를 받았다.
- 2022.5 · On Utilizing Smartphone Cameras to Detect Counterfeit Liquid Food Products 포스터가 ACM MobiSys’22에 채택되었다.
- 2022.3 · Detecting Counterfeit Liquid Food Products in a Sealed Bottle Using a Smartphone Camera 논문이 ACM MobiSys 2022에 채택되었다.
- 2022.1 · On Privacy Risks of Watching YouTube over Cellular Networks with Carrier Aggregation 논문이 ACM UbiComp 2022/IMWUT에 채택되었다.
- 2021.11 · LAPD 논문이 Forbes, The Register, Y Combinator’s Hacker News, Techlog360에 소개되었다.

## 연락과 위치

- 연구실: KAIST N1 923호, 34141 대전광역시 유성구 대학로 291[^home]
- 교수 연구실: N1 901호[^faculty]
- 교수 이메일: jun.han@kaist.ac.kr, junhan@cyphy.kaist.ac.kr[^team]
- 교수 전화: 3516(학과 게시 내선)[^faculty]
[^home]: CyPhy Lab, 첫 화면. <https://www.cyphy.kaist.ac.kr/> 연구실 이름, KAIST·NUS 구성, 연구 대상과 위치. 열람 2026-10-27.
[^research]: CyPhy Lab, Research. <https://www.cyphy.kaist.ac.kr/research> Research Interests와 세 연구 갈래. 열람 2026-10-27.
[^team]: CyPhy Lab, Team. <https://www.cyphy.kaist.ac.kr/team> 교수·현재 구성원·Former Members의 게시 표기. 열람 2026-10-27.
[^faculty]: KAIST 전산학부, 한준 교수 소개. <https://cs.kaist.ac.kr/people/view?idx=645&kind=faculty&menu=160> 직급·학력·2024년 2월 부임·전문 분야·교수 연구실. 교수 명단 <https://cs.kaist.ac.kr/people/faculty>도 같은 이름·직급을 적는다. 열람 2026-10-27.
[^pubs]: CyPhy Lab, Publications. <https://www.cyphy.kaist.ac.kr/publications> 2021–2026년 구역. 열람 2026-10-27.
[^news]: CyPhy Lab, What's New? <https://www.cyphy.kaist.ac.kr/whats-new> 날짜별 연구·학술 활동과 과제·수상 소식. 열람 2026-10-27.
[^awards]: CyPhy Lab, Awards & Recognition. <https://www.cyphy.kaist.ac.kr/awards-recognition> 수상 이름과 대상. 열람 2026-10-27.
[^ndss2026]: NDSS Symposium 2026. <https://www.ndss-symposium.org/ndss2026/> 개최 기간 2026년 2월 23–27일과 Peering Inside the Black-Box 수상. 학회는 Best Paper Award Winners, 랩은 Distinguished Paper Award로 적는다. 열람 2026-10-27.
[^p1]: J. Yun 외, J. Han, ACM International Conference on Mobile Systems, Applications, and Services (2024). <https://doi.org/10.1145/3643832.3661877> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://www.cyphy.kaist.ac.kr/research/powdew> 열람 2026-10-27.
[^p2]: S. R. X. Tan, M. C. Chan, J. Han, ACM Symposium on User Interface Software and Technology, Article 64 (2025). <https://doi.org/10.1145/3746059.3747611> 초록 기준(논문 페이지 게시 초록). 저자 공개 저장소에 게시한 논문 초록. 초록 원문 <https://github.com/NUS-CIR/UniKey> 열람 2026-10-27.
[^p3]: B. Sun, M. C. Chan, J. Han, ACM International Conference on Mobile Systems, Applications, and Services (2025). <https://doi.org/10.1145/3711875.3729158> 초록 기준(논문 페이지 게시 초록). 저자 공개 저장소에 게시한 논문 초록. 초록 원문 <https://github.com/SunBangjie/CAMPrints> 열람 2026-10-27.
[^p4]: R. Xiao 외, J. Han, Network and Distributed System Security Symposium (2026). <https://www.ndss-symposium.org/ndss-paper/peering-inside-the-black-box-long-range-and-scalable-model-architecture-snooping-via-gpu-electromagnetic-side-channel/> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://www.ndss-symposium.org/ndss-paper/peering-inside-the-black-box-long-range-and-scalable-model-architecture-snooping-via-gpu-electromagnetic-side-channel/> 열람 2026-10-27.
[^p5]: N. Jiang, B. Sun, T. Sim, J. Han, 33rd USENIX Security Symposium (USENIX Security 24), 1045–1062 (2024). <https://www.usenix.org/conference/usenixsecurity24/presentation/jiang-nan> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://www.usenix.org/conference/usenixsecurity24/presentation/jiang-nan> 열람 2026-10-27.
[^p6]: R. Xiao 외, J. Han, Network and Distributed System Security Symposium (2025). <https://www.ndss-symposium.org/ndss-paper/lend-me-your-beam-privacy-implications-of-plaintext-beamforming-feedback-in-wifi/> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://www.ndss-symposium.org/ndss-paper/lend-me-your-beam-privacy-implications-of-plaintext-beamforming-feedback-in-wifi/> 열람 2026-10-27.
[^p7]: J. Lee, D. Yu, S. Yang, J. Han, Proceedings of the 24th Annual International Conference on Mobile Systems, Applications and Services Companion (2026). <https://doi.org/10.1145/3812835.3814876> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1145/3508396.3512883%7C10.1145/3572864.3581578%7C10.1145/3666025.3699418%7C10.1145/3812835.3814876> 열람 2026-10-28.
[^supp-c2]: Poster: Towards Privacy Preserving Patient State Classification in Psychiatric Seclusion Room using mmWave Radar, DOI 10.1145/3666025.3699418. <https://doi.org/10.1145/3666025.3699418> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1145/3508396.3512883%7C10.1145/3572864.3581578%7C10.1145/3666025.3699418%7C10.1145/3812835.3814876> 열람 2026-10-28.
[^supp-c4]: EarWalk: Towards Walking Posture Identification using Earables, DOI 10.1145/3508396.3512883. <https://doi.org/10.1145/3508396.3512883> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1145/3508396.3512883%7C10.1145/3572864.3581578%7C10.1145/3666025.3699418%7C10.1145/3812835.3814876> 열람 2026-10-28.

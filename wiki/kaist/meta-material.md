# 고등 광 재료 및 소자 연구실 (Advanced Photonic Materials and Devices Lab, APMD)

**KAIST 신소재공학과 · 신종화 교수**

- 분야: 메타물질·메타표면의 이론 설계와 제작, 이중층 메타표면과 벡터 홀로그래피, 가변 메타표면, 대면적 나노 공정(근접장 나노패터닝, 간섭 리소그래피), 머신러닝·최적화 기반 나노광소자 역설계, 복사 냉각
- 대분야: 소재, 전기전자·반도체·광학
- 태그: 메타물질·메타광학[^research][^mse][^mseen], 나노 패터닝·전사[^research][^p4][^p5], 소자 설계 시뮬레이션[^mse][^research][^p6], 과학·공학 AI[^research][^p6][^p7], 열전달·열관리[^research][^p8], 홀로그래피·라이트필드 3차원 영상[^p2], 설계 최적화(위상·형상 최적화)[^research]
- 홈페이지: <https://www.meta-material.org/>
- 근거와 출처: [APMD 근거 페이지](meta-material-sources.md)

> 파장보다 작은 메타물질과 메타표면을 이론과 시뮬레이션으로 설계하고, 머신러닝 기반 최적화를 거쳐 홀로그래피, 디스플레이, 복사 냉각, 마이크로파 흡수 같은 분야에 적용하는 신소재공학과 연구실이다.[^mse] 메타물질의 이론 설계부터 나노·마이크로 규모의 제작과 측정까지 다룬다고 소개한다.[^mseen]

## 무엇을 연구하나

연구실은 KAIST 신소재공학과 신종화 교수의 연구실이다. 누리집은 연구실을 Advanced Photonic Materials and Devices Lab(APMD)으로 부르고, 첫 화면 제목에 「LIGHT, PROGRAMMED.」와 「Metasurfaces and metamaterials engineered at KAIST」를 단다.[^home] 누리집 News 페이지의 외부보도 글(2024년 2월 안전관리 우수연구실 인증 소식)은 연구실의 국문 이름을 고등 광 재료 및 소자 연구실로 적는다.[^news]

신소재공학과 연구실 소개 페이지는 연구실을, 인공 광학 특성을 구현하려고 파장보다 작은 메타물질(metamaterial, 파장보다 작은 인공 구조를 배열해 자연 물질에 없는 성질을 내도록 만든 물질)과 메타표면(metasurface, 그런 인공 구조를 얇은 한 층으로 배열한 표면)을 이론과 시뮬레이션으로 설계하고, 머신러닝 기반 최적화를 거쳐 홀로그래피, 디스플레이, 복사냉각, 마이크로파 흡수 등 여러 분야에 적용하는 연구실로 소개한다.[^mse] 같은 페이지의 핵심어는 메타표면, 나노광학, 양자광학, AI 최적화, 디스플레이, 광센서다.[^mse]

신소재공학과 영문 연구실 목록은 연구실이 파동과, 메타물질을 포함한 구조화된 소재 사이의 새로운 상호작용에 초점을 둔다고 적는다. 음의 굴절률이나 매우 높은 굴절률 같은 극단적인 광학 성질과 광학 블랙홀, 투명 망토(invisible cloak) 같은 광학 현상을 구현할 수 있다고 소개하고, 메타물질의 이론 설계부터 나노·마이크로 규모의 제작과 측정까지 연구한다고 적는다.[^mseen]

누리집 Research 페이지는 네 연구 주제로 메타표면과 칩 결합 광학(Metasurface and Co-Packaged Optics), 대면적 나노 공정(Large-Area Nanofabrication), AI 기반 역설계(AI-Driven Inverse Design), 복사 냉각(Radiative Cooling)을 든다.[^research] Contact 페이지는 대학원생과 박사후연구원을 모집한다고 알리며 분야를 「Photonics, Materials, ML.」로 적는다.[^contact]

## 주요 연구 주제

### 1. 메타표면과 칩 결합 광학

Research 페이지는 빛의 진폭, 위상, 편광을 서로 따로 조절하는 메타표면 플랫폼이 여러 개의 기존 광학 부품을 얇은 한 층으로 대신할 수 있다고 적는다. 이 플랫폼을 칩 위에 바로 올리면 칩 결합 광학(co-packaged optics, 계산 칩 바로 옆에 광 연결 부품을 함께 넣는 방식)으로 쓸 수 있으며, GPU나 양자 프로세서 같은 계산 하드웨어 옆에 두는 광 연결로서, 지금은 전기 배선이 전력 소모와 신호 속도의 주된 제약이 되는 자리를 겨냥한다고 설명한다.[^research]

Research 페이지는 보통의 홀로그램이 편광 정보 없이 빛의 세기와 위상만 재현한다고 적고, 이 메타표면 플랫폼으로 편광과 진행 방향에 따라 다른 영상을 재현하는 홀로그램을 만들며, 정보를 싣는 자유도를 임의의 총 각운동량(빛의 편광과 꼬임 정도가 결합된 성질) 상태로 넓혀 여러 정보를 겹쳐 싣는 보안성 높은 광학 암호화에 쓴다고 설명한다.[^research][^news] 또 대부분의 메타표면은 제작 뒤 성질이 고정되지만 초점을 다시 맞추는 렌즈, 투명도가 바뀌는 창, 색이 바뀌는 필터처럼 제작 뒤 광학 반응을 바꿔야 하는 응용이 많다고 적는다. 연구실의 가변 메타표면은 반도체 층에 전하 운반자 주입, 기계적 변형이나 압축, 전압 인가 같은 외부 자극으로 제작 뒤 다시 설정되며, 응용은 다시 설정할 수 있는 레이저 초점 맞춤부터 압축에 반응하는 스마트 창까지라고 설명한다.[^research]

대표 논문 1은 굴절률이 높은 타원 기둥을 두 층으로 배열한 유니버설 메타표면으로, 두 입력 편광 상태 모두에 대해 투과하는 빛의 편광·진폭·위상을 따로 조절할 수 있음을 증명하고 이전에는 불가능했던 3차원 홀로그램 방식을 실험으로 보였다.[^p1] 대표 논문 2는 이중층 메타표면으로 어떤 입력 편광에도 일반화된 비대칭 투과를 이루고, 편광과 빛의 방향에 따라 네 개의 벡터 홀로그램 영상을 만드는 야누스 벡터 홀로그램과 이를 이용한 광학 암호화를 보였다.[^p2] 대표 논문 3은 두 메타렌즈를 돌리거나 간격을 바꿔 레이저 초점을 3차원 공간의 원하는 점으로 옮기는 기계 구동식 메타렌즈 쌍을 만들고, 두 메타표면의 정렬을 안내하는 홀로그램을 렌즈에 넣었다.[^p3] Research 페이지는 이 주제의 논문으로 총 각운동량 벡터 홀로그래피 논문(Advanced Materials 2026), 반도체 제조 장치에서 전자기장을 능동 제어하는 가변 메타물질 논문(Plasma Sources Science and Technology 2024), 압축에 반응하는 스마트 창 논문(Nature Communications 2024)도 든다.[^research][^pubs]

### 2. 대면적 나노 공정

Research 페이지는 전자빔 리소그래피(전자빔으로 감광 물질에 무늬를 직접 그리는 공정)나 집속 이온빔 가공 같은 고해상도 나노 공정이 본래 차례로 하나씩 그리는 직렬 방식이라, 구조가 거시적인 면적을 덮어야 할 때는 실용적이지 않다고 적는다. 연구실은 근접장 나노패터닝(proximity-field nanopatterning, PnP, 감광 물질에 밀착한 위상 마스크가 만드는 3차원 간섭 무늬로 나노 구조를 만드는 공정)과 간섭 리소그래피(여러 빛살이 겹쳐 생긴 간섭 무늬를 감광 물질에 새기는 공정) 같은 병렬 방식의 웨이퍼 규모 패터닝 방법을 개발해, 복잡한 광 구조를 한 번의 노광(감광 물질에 빛을 쬐어 무늬를 옮기는 단계)으로 넓은 면적에 복제한다고 설명한다. 직접 그리는 방식의 비용과 시간 가운데 일부만 들이면서도 소자에 필요한 파장보다 작은 해상도를 유지한다고 적는다.[^research]

대표 논문 4는 근접장 나노패터닝 공정에 역설계를 적용해, 여러 목표 격자와 무늬에 맞는 최적 위상 마스크를 찾고 기존 근접장 나노패터닝으로는 수직 입사 빛에서 보고된 적 없는 나노 채널의 2차원 직사각 배열을 만들었다.[^p4] 대표 논문 5는 각 회절 빛살의 진폭·위상·편광을 조절해 모든 2차원 브라베 격자를 3차원 공간에 구현할 수 있음을 보였다.[^p5] Research 페이지는 이 주제의 논문으로 스펙트럼으로 부호화한 근접장 나노패터닝 논문(Advanced Optical Materials 2026)도 든다.[^research][^pubs] 누리집 소식은 대표 논문 4를 신소재공학과 전석우 교수와의 공동 연구로, 3차원 나노 구조를 단 한 번의 노광으로 구현하는 공정으로 소개한다.[^news]

### 3. AI 기반 역설계

Research 페이지는 나노광소자를 보통 구조를 짐작하고 광학 반응을 시뮬레이션한 뒤 손으로 고치기를 되풀이해 설계하는데, 이 방식은 설계 변수의 수가 늘면 감당하기 어려워진다고 적는다. 역설계(inverse design)는 목표 광학 반응에서 출발해 그 반응을 내는 구조를 찾는 방법으로, 연구실은 생성적 적대 신경망, 위상 최적화(topology optimization), 최근에는 대형 언어 모델을 포함한 머신러닝과 최적화 방법을 다층 박막과 메타표면 설계에 쓴다고 설명한다.[^research]

대표 논문 6은 조건부 생성적 적대 신경망을 반복 최적화 과정에 넣어 공정 조건과 실제 구조 사이의 관계를 배우게 하고, 최적화 대상을 폭·높이·주기 같은 구조 변수에서 증착 속도·열처리 시간 같은 공정 변수로 옮겼다. 금속 격자로 만든 빨강·초록·파랑 색 필터 설계로 이 방법을 보였다.[^p6] 대표 논문 7은 대형 언어 모델이 문맥 내 학습으로 전문 지식이 없는 사용자도 다층 박막의 광학 반응을 수치 시뮬레이션으로 계산하게 하고, 대화로 목표 성질에 맞는 다층 박막 설계를 내놓을 수 있음을 보였다. 메타표면의 구조와 성질을 글로 표현한 자료로 미세조정한 모델은 입력과 출력을 뒤바꿔 목표 성질의 메타표면 설계를 생성했다.[^p7] 누리집 목록에는 전자기파를 여러 각도로 복잡하게 산란시키는 층상·구형 대칭 구조를 설계하는 위상 핵생성 알고리즘을 제목에 단 Eschallot 논문(Computer Physics Communications 2026)도 있다.[^pubs] 누리집 소식은 2023년 6월 Min Seok Jang 교수, Hamza Kurt 교수 연구 그룹과 함께 연 역설계 워크숍(Inverse Design Workshop)을 알린다.[^news]

### 4. 복사 냉각

Research 페이지는 모든 물체가 열을 열적외선 빛으로 내보낸다고 적는다. 대기가 우주 쪽으로 투명한 좁은 파장대에서 빛을 강하게 내보내면서 햇빛은 반사하도록 만든 표면은 흡수하는 열보다 많은 열을 하늘로 잃어, 에너지를 들이지 않고도 주변 온도보다 낮게 식을 수 있다고 설명한다. 연구실은 이 효과를 만드는 파장별·방향별 방출을 설계하고, 보통 필요한 흰색이나 금속 광택 코팅을 넘어 여러 색을 띠는 표면, 광발광(빛을 흡수한 물질이 다시 빛을 내는 현상) 기반 표면, 방출 각도를 고른 표면으로 복사 냉각을 넓힌다고 적는다.[^research]

대표 논문 8은 착색제와 열 방출체 사이의 열적 비평형을 이용해 복사로는 이어지고 전도로는 단열된 소재 시스템을 제안하고, 진공 단열 없이 검은색을 포함한 원하는 겉 색을 띠면서 하루 내내 주변 온도보다 낮게 식는 복사 냉각체를 만들었다.[^p8] Research 페이지는 이 주제의 논문으로 방향성 복사(Optics Express 2021)를 들고, 누리집 목록에는 광발광 기반 전색 복사 냉각 논문(ACS Photonics 2022)과 나노입자 잉크로 만든 유색 주간 복사 냉각 필름 논문(Materials Today Physics 2021)도 있다.[^research][^pubs]

## 대표 논문

신종화 교수가 저자인 2021–2026년 논문 가운데 Research 페이지의 네 연구 주제(메타표면과 칩 결합 광학, 대면적 나노 공정, AI 기반 역설계, 복사 냉각)에서 초록을 확인할 수 있는 여덟 편을 골랐다. 여덟 편 모두 누리집 목록에서 교수 이름에 ‡ 표시가 붙어 있고, 4번을 뺀 일곱 편은 교수가 마지막 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2022 | [Universal Metasurfaces for Complete Linear Control of Coherent Light Transmission](https://doi.org/10.1002/adma.202204085) · Advanced Materials 34 | 메타표면과 광학 나노 구조로 얇은 소자에서 들어오는 빛을 복잡하게 조절할 수 있게 됐지만, 얇은 나노 구조 배열 하나로 결맞은 빛(파동의 위상 관계가 일정하게 유지되는 빛)의 투과를 완전히 선형 제어할 수 있는지, 곧 두 입력 편광 상태 모두에 대해 편광·진폭·위상을 따로 조절할 수 있는지는 분명하지 않았다. 이 논문은 그것이 가능함을 증명하고, 굴절률이 높은 타원 기둥을 두 층으로 배열해 카이랄성(거울상과 겹쳐지지 않는 비대칭성)과 이방성(방향에 따라 성질이 달라지는 성질)을 모두 설계할 수 있는 유니버설 메타표면을 제안한다. 존스 행렬(편광 상태가 소자를 지나며 바뀌는 관계를 나타내는 행렬)로 빛 조절의 완전성을 수학적으로 보이고, 이전에는 불가능했던 새로운 3차원 홀로그램 방식을 실험으로 보였으며, 입력 상태에 반응하는 어떤 벡터 선형 광학 소자든 구현할 수 있는 체계적인 방법을 제시했다.[^p1] | 1저자 Taeyong Chang, 마지막 저자 신종화 (9명) |
| 2 | 2024 | [Bidirectional Vectorial Holography Using Bi-Layer Metasurfaces and Its Application to Optical Encryption](https://doi.org/10.1002/adma.202406717) · Advanced Materials 36 | 빛이 들어오는 방향에 따라 다르게 반응하는 광학계 연구가 커지고 있고, 야누스 메타표면(빛이 들어오는 면에 따라 다르게 작동하는 메타표면)은 얇은 막 안에서 화소 단위로 빛을 비대칭으로 조절할 수 있다. 그러나 이전 연구는 제한된 입력 편광에 대한 부분적 비대칭 투과 제어에 머물고 주로 스칼라 기능을 다뤘다. 이 논문은 어떤 입력 편광에도 완전히 일반화된 비대칭 투과를 이루는 이중층 메타표면을 내놓는다. 상반계(빛의 출발점과 도착점을 맞바꿔도 투과 관계가 유지되는 계)의 비대칭 투과 이론 모형으로 앞면과 뒷면의 존스 행렬 사이 관계를 밝혔고, 이 모형은 마주 보는 두 면의 편광·방향 채널 사이에 근본적인 상관이 있음을 보여 준다. 이 제약을 피하려고 투과 공간을 나눠 목표 부피 안에서 서로 다른 네 가지 벡터 기능을 구현했고, 네 개의 벡터 홀로그램 영상을 만드는 편광·방향 다중화 야누스 벡터 홀로그램을 실험으로 보였다. 계산으로 구현한 벡터 편광자 배열과 묶으면 은닉성이 높은 광학 암호화를 할 수 있다.[^p2] | 1저자 Hyeonhee Kim, 마지막 저자 신종화 (3명) |
| 3 | 2023 | [Three-dimensionally reconfigurable focusing of laser by mechanically tunable metalens doublet with built-in holograms for alignment](https://doi.org/10.1515/nanoph-2022-0634) · Nanophotonics 12 | 메타렌즈(나노 구조 배열로 만든 얇은 렌즈)는 부피가 큰 여러 기존 광학 부품을 대신할 수 있고, 초점을 다시 맞출 수 있는 능동 메타렌즈가 학계와 산업계의 관심을 받지만, 소재 성질과 제작의 어려움 때문에 조절 범위가 제한된다. 이 논문은 초점 위치를 3차원으로 옮길 수 있는 혼합 광학계를 제안하고 실험으로 보였다. 흔한 소재와 공정으로 쉽게 만들 수 있는 수동 메타렌즈 두 장을 기계적으로 움직이는 방식으로, 두 렌즈를 돌리거나 간격을 바꾸기만 하면 들어온 레이저를 3차원 공간의 원하는 점에 모을 수 있다. 메타표면의 편광 다중화 능력을 이용해 두 메타표면의 회전·위치 정렬을 안내하는 홀로그램도 렌즈에 넣었다.[^p3] | 1저자 Joonkyo Jung, 마지막 저자 신종화 (3명) |
| 4 | 2022 | [Photolithographic realization of target nanostructures in 3D space by inverse design of phase modulation](https://doi.org/10.1126/sciadv.abm6310) · Science Advances 8 | 정밀한 3차원 나노 무늬를 대량으로 만드는 일은 제작 기술의 오랜 목표다. 간섭 리소그래피와 근접장 나노패터닝이 부분적인 해법이 될 수 있지만, 각각 장치가 복잡하고 만들 수 있는 구조의 범위가 좁다는 문제가 남아 있었다. 이 논문은 근접장 나노패터닝 공정에 역설계를 적용했다. 수반 방법(adjoint method, 설계 변수마다 따로 계산하지 않고 추가 계산으로 성능의 기울기를 한꺼번에 구하는 최적화 방법)에 기반한 역설계 플랫폼이 여러 목표 격자와 무늬에 맞는 최적 위상 마스크를 효율적으로 찾는다. 개념 증명으로, 수직으로 들어오는 빛을 쓰는 기존 근접장 나노패터닝에서는 보고된 적 없는 나노 채널의 2차원 직사각 배열을 만들었고, 소재 변환도 보였다.[^p4] | 1저자 Sang-Hyeon Nam, 마지막 저자 Seokwoo Jeon (8명), 신종화 교수는 7번째 저자(누리집 ‡ 표시) |
| 5 | 2024 | [Realization of all two-dimensional Bravais lattices with metasurface-based interference lithography](https://doi.org/10.1515/nanoph-2023-0786) · Nanophotonics 13 | 근접장 나노패터닝은 밀착한 위상 마스크가 만드는 부피 간섭 무늬를 이용해 빠르고 비용이 적게 들며 넓은 면적을 만드는 제작 방법으로 쓰여 왔지만, 설계의 다양성은 충분히 탐구되지 않았다. 이 논문은 여러 무늬를 가진 어떤 2차원 격자든 만들 수 있음을 보였다. 각 회절 빛살의 진폭·위상·편광을 조절해 모든 2차원 브라베 격자를 3차원 공간에 구현할 수 있다. 이 결과는 광학 소재와 구조 소재부터 에너지 저장·변환 소재까지 3차원 나노 구조가 필요한 여러 응용에 쓰일 수 있다.[^p5] | 1저자 Myungjoon Kim, 마지막 저자 신종화 (3명) |
| 6 | 2022 | [Data-driven concurrent nanostructure optimization based on conditional generative adversarial networks](https://doi.org/10.1515/nanoph-2022-0005) · Nanophotonics 11 | 광학 나노 구조 설계에는 반복 수치 최적화를 널리 쓰지만, 변형 없는 이상적인 모양을 가정한 시뮬레이션 결과와 변형된 모양으로 만들어진 실제 측정값 사이에 큰 성능 차이가 날 수 있다. 이 논문은 조건부 생성적 적대 신경망(CGAN)을 표준 반복 최적화 과정에 넣어 공정과 구조의 관계를 배우게 하고, 제작 조건에 맞는 현실적인 시뮬레이션 설계를 만든다. 최적화 공간도 폭·높이·주기 같은 구조 변수에서 증착 속도·열처리 시간 같은 공정 변수로 옮긴다. 금속 격자로 만든 빨강·초록·파랑 색 필터 설계로 이 플랫폼을 보였고, CGAN 기반 최적화는 이상적인 구조를 쓰는 표준 최적화보다 성능 지수가 높은 현실적인 설계로 이어지는 제작 변수를 찾았다. 최적 구조 설계를 얻으면 최적 공정 변수를 자동으로 돌려주므로 설계 과정을 앞당길 수 있다.[^p6] | 1저자 Arthur Baucour, 마지막 저자 신종화 (3명) |
| 7 | 2025 | [Nanophotonic device design based on large language models: multilayer and metasurface examples](https://doi.org/10.1515/nanoph-2024-0674) · Nanophotonics 14 | 대형 언어 모델(LLM)은 언어 처리를 넘어 여러 과학 분야에서 시도되고 있지만 나노광소자 설계에서는 아직 많이 탐구되지 않았다. 이 논문은 사용자에게 분야 전문 지식이 없어도 LLM이 나노광학 설계 문제를 다룰 수 있는지 살폈다. 문맥 내 학습을 쓴 LLM은 비전문가 사용자가 수치 시뮬레이션으로 다층 박막의 광학 반응을 계산하게 해 주었고, LLM과 사용자가 대화와 피드백을 주고받아 사용자가 준 목표 광학 성질에 맞는 다층 박막 최적 설계도 낼 수 있었다. 또 메타표면의 구조와 성질을 글로 나타낸 자료로 LLM을 미세조정하고, 입력과 출력 글을 뒤바꿔 목표 성질을 갖는 메타표면 설계를 생성할 수 있음을 보였다.[^p7] | 1저자 Myungjoon Kim, 마지막 저자 신종화 (3명) |
| 8 | 2022 | [Daylong Sub-Ambient Radiative Cooling with Full-Color Exterior Based on Thermal Radiation and Solar Decoupling](https://doi.org/10.1002/adom.202202129) · Advanced Optical Materials 11 | 지상의 복사 냉각은 에너지를 쓰지 않는 냉각으로 주거·상업 부문의 냉방 수요를 줄이는 방법이지만, 복사 냉각체는 순백색이나 거울 같은 겉모습이라 건물 외벽과 차량에 대량으로 쓰면 보기에 단조롭고 안전 문제도 생길 수 있다. 이 논문은 색의 다양성과 냉각 성능 사이의 근본적인 상충을 넘으려고, 착색제와 열 방출체 사이의 열적 비평형을 이용해 복사로는 이어지고 전도로는 단열된 소재 시스템을 제안한다. 이 냉각체는 진공 단열 없이 검은색을 포함한 원하는 겉 색을 띠면서 하루 중 언제나 주변 온도보다 낮게 식는다. 실험에서 AM1.5 조건(지상 태양광 측정에 쓰는 표준 햇빛 조건)에서 태양 에너지 646 W m−2를 흡수하는 검은 냉각체도 낮 동안 주변 온도보다 최대 6.9 K(평균 3.5 K) 낮게 식었다.[^p8] | 1저자 Suwan Jeon, 마지막 저자 신종화 (6명) |

## 교수와 전문 분야

신종화 교수(Jonghwa Shin)는 KAIST 신소재공학과 교수다. 누리집 People 페이지는 교수의 현재 직위를 신소재공학과(Dept. of Materials Science and Engineering) Full Professor로 적는다.[^people]

People 페이지에 따르면 교수는 2001년 서울대학교에서 전기공학(Electrical Engineering) 학사, 2003년과 2008년 Stanford University에서 전기공학 석사와 박사 학위를 받았다. 2002–2008년 Stanford University Fan Group의 연구 조교(Research Assistant), 2008–2011년 KAIST 물리학과 박사후연구원(Postdoctoral Research Fellow), 2011–2012년 같은 학과 연구조교수(Research Assistant Professor)를 지냈다. 신소재공학과에서는 2012–2017년 조교수, 2017–2024년 부교수였고, 2024년부터 교수다.[^people] 누리집 소식은 교수가 2026년 7월 Optics and Photonics Congress 2026에서 메타표면의 주기성, 균일성, 일관성을 다룬 강연(「Periodicity, homogeneity and consistency in metasurfaces」)을 했다고 알린다.[^news]

신소재공학과 페이지들은 연구실을 메타물질과 메타표면의 이론 설계, 시뮬레이션, 나노·마이크로 규모의 제작과 측정을 하고 머신러닝 기반 최적화로 응용하는 연구실로 소개한다.[^mse][^mseen] Research 페이지의 네 주제와 2021–2026년 논문 목록을 함께 보면, 교수의 전문 분야는 메타물질·메타표면의 이론 설계와 이를 쓰는 광학 소자(벡터 홀로그래피, 가변 메타표면, 복사 냉각 표면), 근접장 나노패터닝 같은 대면적 나노 공정, 최적화와 머신러닝을 쓰는 나노광소자 역설계다.[^research][^pubs]

## 응용 분야

누리집 첫 화면 Research Applications 구역은 네 응용을 든다. 반도체 칩 위에 바로 무늬를 새긴 메타표면이 칩 안에서 빛살의 방향을 바꾸고 파장을 거르는 기능을 주는 광 반도체(Optical Semiconductors), 칩 바로 옆에 메타표면 광학을 넣는 칩 결합 광학(Co-Packaged Optics), 구조화된 빛을 쓰는 메타표면으로 얽힌 광자 상태를 만들고 다루는 양자 응용(Quantum Applications), 나노 구조 메타표면이 색과 홀로그램 영상을 직접 만들어 AR·VR 기기의 LCD·OLED 적층을 얇게 대신하는 디스플레이 기술(Display Technology)이다.[^home] 신소재공학과 연구실 소개 페이지는 적용 분야로 홀로그래피, 디스플레이, 복사냉각, 마이크로파 흡수를 든다.[^mse]

누리집 소식에 실린 학교 보도에서 교수는 야누스 메타표면 연구를 소개하며 광학 암호화 외에도 증강현실(AR), 홀로그램 디스플레이, 자율주행차의 라이다(LiDAR) 시스템 등에 응용되도록 광학 소자를 개발할 계획이라고 말했다.[^news] 대표 논문 8은 복사 냉각체를 탄소 배출 없는 열 관리와 색의 다양성이 함께 필요한 상업 건물과 주택 같은 실외 용도에 쓸 수 있다고 적는다.[^p8] 누리집 목록에는 마이크로파 흡수 메타표면과 그 대량 생산 공정을 제목에 단 논문(Scientific Reports 2021, Optics Express 2022, International Journal of Precision Engineering and Manufacturing 2025)과 이미지 센서용 색 화소 논문(Nanophotonics 2024)도 있다.[^pubs]

## 구성원

누리집 People 페이지의 박사후연구원(Post Doctoral Researchers) 2명, 박사과정(Ph.D. Candidates) 8명, 석박사통합과정(Integrated M.S. - Ph.D. Candidates) 1명, 석사과정(M.S. Candidates) 2명, 모두 13명이다. 이름 괄호의 국문 이름은 누리집 소식이 같은 사람을 국문으로 적은 표기다.[^people][^news] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Jung, Joonkyo (정준교) | 박사후연구원 | 1, 2, 3 |
| Kim, Hyeonhee (김현희) | 박사후연구원 | 1, 2, 3 |
| Park, Hyeonjin | 박사과정 | 7, 8 |
| Park, Junhyung | 박사과정 | 4 |
| Lee, Minyeul (이민열) | 박사과정 |  |
| Hyeong, Yun | 박사과정 |  |
| Hwang, Jisung (황지성) | 박사과정 |  |
| Lee, Seungchul | 박사과정 |  |
| Noh, Changgyun | 박사과정 |  |
| Kim, Minki | 박사과정 |  |
| Kim, Dohyun (김도현) | 석박사통합과정 |  |
| Kim, Jongmin | 석사과정 |  |
| Choi, Sungmin | 석사과정 |  |

## 졸업생

누리집 People 페이지 Alumni 구역의 26명이다. 학위·과정은 카드의 과정 표기(Post Doc., M.S., Ph.D.)이고, 괄호 안은 카드의 연도(박사후연구원은 기간)다. 진로는 카드에 적힌 현재 소속이며, 한 명은 진로를 적지 않는다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Chung, Kyungjae | Post Doc. (2014.03–2015.10) | Samsung Electronics |
| Choe, Meensoo | M.S. (2015) | LG Innotek |
| Kim, Juyoung | Ph.D. (2015) | Electronics and Telecommunications Research Institute (ETRI) |
| Lee, Nayeon | M.S. (2016) | Apple |
| Nam, Sanghyeon (남상현) | M.S. (2016) | Samsung Electronics |
| Mun, Jeongho | Ph.D. (2016) | Samsung Electronics |
| Kim, Hyowook | Ph.D. (2018) | ASML |
| Park, Junha | M.S. (2018) | Applied Materials Korea |
| Kang, Seokyoung | M.S. (2018) | SK Hynix |
| Heo, Minsung | Ph.D. (2019) | Samsung Electronics |
| Kim, Jonguk | Ph.D. (2019) | Samsung Electronics |
| Kim, Reehyang | Ph.D. (2019) | Samsung Display |
| Chang, Taeyong (장태용) | Ph.D. (2021) | Postdoc, Nanyang Technological University |
| Yun, Kyunsun | M.S. (2021) | LG Energy Solution |
| Jeon, Suwan | Ph.D. (2022) | Korea Institute of Machinery and Materials (KIMM) |
| Baucour, Arthur | Ph.D. (2023) | ASML |
| Chang, Gunho | M.S. (2023) | Ph.D. Candidate, Seoul National University |
| Kim, Nayoung (김나영) | Ph.D. (2023) | Samsung Display |
| Kim, Myungjoon (김명준) | Ph.D. (2023) | Postdoc, Cornell University |
| Harding, Joseph | M.S. (2024) | Samsung SDI |
| Yerezhep, Bakytgul | M.S. (2024) |  |
| Yoon, Jeongbin | M.S. (2025) | Samsung Electronics |
| Kang, Seungkyu | Ph.D. (2025) | Korea Electronics Technology Institute (KETI) |
| Min, Seokhwan | Ph.D. (2025) | Postdoc, Cornell University |
| Cho, Mingwan (조민관) | Post Doc. (2025.09–2026.08) | Samsung Electronics |
| Chen, Qiang | Ph.D. (2026) | Contemporary Amperex Technology (CATL) |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지의 2026–2021년 연도 구역에 있는 41편이다(2026년 6편, 2025년 7편, 2024년 9편, 2023년 5편, 2022년 9편, 2021년 5편).[^pubs] 저자와 제목 표기는 누리집 그대로이고, 학술지 칸은 누리집 화면처럼 학술지 이름과 연도 구역의 연도를 적었다. 같은 연도 안의 순서도 누리집과 같은 출판 날짜의 최신순이다. 저자 이름 뒤의 *와 ‡는 누리집이 뜻을 적지 않은 누리집 표시다. 목록 구성 기준은 근거 페이지에 적었다.

**2026**

- Jeongbin Yoon\*, Mingwan Cho\*‡, Hyeonhee Kim, Hyeonjin Park, In-Sung Joe, Jonghwa Shin‡. "Angle-and polarization-adaptive aperiodic-anisotropic metasurfaces for broadband reflectance suppression". *iScience (2026)*.
- Junhyung Park\*, Yun Hyeong\*, Hwanseok Chang, Dohyun Kim, Joonkyo Jung, Seokwoo Jeon, Jonghwa Shin‡. "Spectrally Encoded Proximity-Field Nanopatterning". *Advanced Optical Materials (2026)*.
- Kyungmin Lee, Minwook Kyung, Yung Kim, Jagang Park, Hansuek Lee, Joonhee Choi, C. T. Chan, Jonghwa Shin, Kun Woo Kim, Bumki Min. "Analogs of Spontaneous Emission and Lasing in Photonic Time Crystals". *Physical Review Letters (2026)*.
- Joonkyo Jung\*, Hyeonhee Kim, Jonghwa Shin‡. "Arbitrary Total Angular Momentum Vectorial Holography Using Bi-Layer Metasurfaces". *Advanced Materials (2026)*.
- Seokhwan Min, Jonghwa Shin. "Eschallot: A Topology Nucleation Algorithm for Designing Stratified, Spherically Symmetric Systems That Exhibit Complex Angular Scattering of Electromagnetic Waves". *Computer Physics Communications (2026)*.
- Oki Gunawan, Chaeyoun Kim, Bonfilio Nainggolan, Minyeul Lee, Jonghwa Shin, Dong Suk Kim, Yimhyun Jo, Minjin Kim, Julie Euvrard, Douglas Bishop, Frank Libsch, Teodor Todorov, Yunna Kim, Byungha Shin. "Electronic Trap Detection with Carrier-Resolved Photo-Hall Effect". *Science Advances (2026)*.

**2025**

- Je-Ryung Lee\*, Myungjoon Kim\*, Seung Hwan Moon, Doo-Sun Choi, Jonghwa Shin, Ik Soo Kang, Tae-Jin Je, Eun-chae Jeon. "Manufacturing of a Bitmap-Type Lightweight Microwave Absorber Metasurface". *International Journal of Precision Engineering and Manufacturing (2025)*.
- Dongha Kim\*, Geonhyeong Park\*, Yun-Seok Choi, Arthur Baucour, Jisung Hwang, Jaeyu Kim, Sanghyeok Park, Hee Seong Yun, Jonghwa Shin, Haiwen Wang, Shanhui Fan, Dong Ki Yoon‡, Min-Kyo Seo‡. "Dynamic realization of emergent high-dimensional optical vortices". *Nature Communications (2025)*.
- Jagang Park\*, Kyungmin Lee\*, Ruo-Yang Zhang, Hee-Chul Park, Jung-Wan Ryu, Gil Young Cho, Min Yeul Lee, Zhaoqing Zhang, Namkyoo Park, Wonju Jeon, Jonghwa Shin, C. T. Chan, Bumki Min‡. "Spontaneous Emission Decay and Excitation in Photonic Time Crystals". *Physical Review Letters (2025)*.
- Minyeul Lee\*, Suwan Jeon, Jonghwa Shin‡. "Angle- and Polarization-Tolerant Metasurface Designs Based on the Aperiodic Tiling". *Advanced Optical Materials (2025)*.
- Myungjoon Kim\*, Hyeonjin Park\*, Jonghwa Shin‡. "Nanophotonic device design based on large language models: multilayer and metasurface examples". *Nanophotonics (2025)*.
- Dohyeon Lee\*, Moosung Lee, Bakytgul Yerenzhep, Myungjoon Kim, Herve Hugonnet, Seokwoo Jeon, Jonghwa Shin, YongKeun Park‡. "Fast Free-Form Phase Mask Design for Three-Dimensional Photolithography Using Convergent Born Series". *ACS Photonics (2025)*.
- Junhyeong Kim\*, Jae-Yong Kim\*, Jungmin Kim, Yun Hyeong, Berkay Neseli, Jong-Bum You, Joonsup Shim, Jonghwa Shin, Hyo-Hoom Park, Hamza Kurt‡. "Inverse design of nanophotonic devices enabled by optimization algorithms and deep learning: recent achievements and future prospects". *Nanophotonics (2025)*.

**2024**

- Dae‐Hyeon Song\*, Chang Woo Song\*, Seunghee H. Cho\*, Tae Yoon Kwon, Hoeyun Jung, Ki Hyun Park, Jiyun Kim, Junyoung Seo, Jaeyoung Yoo, Minjoon Kim, Gyu Rac Lee, Jisung Hwang, Hyuck Mo Lee, Jonghwa Shin, Jennifer H. Shin, Yeon Sik Jung‡, Jae‐Byum Chang‡. "Highly Tunable, Nanomaterial-Functionalized Structural Templating of Intracellular Protein Structures Within Biological Species". *Advanced Science (2024)*.
- Seungkyun Lee\*, Minjae Ku\*, Heejin Lim\*, Jisung Hwang, Jong Min Kim, Hanhwi Kim, Jonghwa Shin, Hyeuk Jin Han‡, Yeon Sik Jung‡. "Realizing Square-Ordered Nanopillars with a 0.1-Tera-Density through a Superimposed Masking Strategy for Advanced Surface-Enhanced Raman Spectroscopy". *ACS Applied Materials & Interfaces (2024)*.
- Hyeonhee Kim\*, Joonkyo Jung\*, Jonghwa Shin‡. "Bidirectional Vectorial Holography Using Bi-Layer Metasurfaces and Its Application to Optical Encryption". *Advanced Materials (2024)*.
- Haomin Chen\*, Gunho Chang, Tae Hee Lee, Seokhwan Min, Sanghyeon Nam, Donghwi Cho, Kwonhwan Ko, Gwangmin Bae, Yoonseong Lee, Jirou Feng, Heng Zhang, Jang-Kyo Kim, Jonghwa Shin, Jung-Wuk Hong‡, Seokwoo Jeon‡. "Compression-Sensitive Smart Windows: Inclined Pores for Dynamic Transparency Changes". *Nature Communications (2024)*.
- Seung Kyu Kang\*, Kyoohyun Kim, Jinsoo Jeong, Sunghee Hong, YongKeun Park‡, Jonghwa Shin‡. "In silico full-angle high-dynamic range scattering of microscopic objects exploiting holotomography". *Biomedical Optics Express (2024)*.
- Qiang Chen\*, Minwoo Choi, Haomin Chen, Jin Kim, Caiyan Qin, Youngjin Ham, Myungwoo Choi, Haibo Zeng, Jonghwa Shin, Bong Jae Lee‡, Seokwoo Jeon‡. "Tree-Inspired Aerogel Comprising Nonoxidized Graphene Flakes and Cellulose as Solar Absorber for Efficient Water Generation". *Nano Letters (2024)*.
- Mingwan Cho\*, Joonkyo Jung, Myungjoon Kim, Jeong Yub Lee, Seokhwan Min, Jongwoo Hong, Shinho Lee, Minsung Heo, Jong Uk Kim, In-Sung Joe‡, Jonghwa Shin‡. "Color arrestor pixels for high-fidelity, high-sensitivity imaging sensors". *Nanophotonics (2024)*.
- Minyeul Lee\*, Sungyoung Yoon\*, Meehyun Lim, Sungyeol Kim, Jonghwa Shin‡. "Tunable metamaterials with carrier-induced effective permittivity for active control of electromagnetic fields in semiconductor manufacturing device". *Plasma Sources Science and Technology (2024)*.
- Myungjoon Kim\*, Nayoung Kim\*, Jonghwa Shin‡. "Realization of all two-dimensional Bravais lattices with metasurface-based interference lithography". *Nanophotonics (2024)*.

**2023**

- Suwan Jeon\*, Su Eon Lee\*, Wonjoong Kim\*, Seokhwan Min, Seung Won Seon, Seung Ho Han, Bong Hoon Kim‡, Heon Lee‡, Jonghwa Shin‡. "Visual and thermal camouflage on different terrestrial environments based on electrochromism". *Nanophotonics (2023)*.
- Nayoung Kim\*, Myungjoon Kim, Joonkyo Jung, Taeyong Chang, Suwan Jeon, Jonghwa Shin‡. "Highly angle-sensitive and efficient optical metasurfaces with broken mirror symmetry". *Nanophotonics (2023)*.
- Joonkyo Jung\*, Hyeonhee Kim\*, Jonghwa Shin‡. "Three-dimensionally reconfigurable focusing of laser by mechanically tunable metalens doublet with built-in holograms for alignment". *Nanophotonics (2023)*.
- Sanghyeok Park\*, Dongha Kim\*, Yun-Seok Choi, Arthur Baucour, Donghyeong Kim, Sangho Yoon, Kenji Watanabe, Takashi Taniguchi, Jonghwa Shin, Jonghwan Kim, Min-Kyo Seo‡. "Customizing Radiative Decay Dynamics of Two-Dimensional Excitons via Position- and Polarization-Dependent Vacuum-Field Interference". *Nano Letters (2023)*.
- Suwan Jeon\*, Soomin Son, Seokhwan Min, Hyeonjin Park, Heon Lee‡, Jonghwa Shin‡. "Daylong sub-ambient radiative cooling with full-color exterior based on thermal radiation and solar decoupling". *Advanced Optical Materials (2023)*.

**2022**

- Dongha Kim\*, Arthur Baucour, Yun-Seok Choi, Jonghwa Shin, Min-Kyo Seo‡. "Spontaneous generation and active manipulation of real-space optical vortices". *Nature (2022)*.
- Taeyong Chang\*, Joonkyo Jung\*, Sang-Hyeon Nam, Hyeonhee Kim, Jong Uk Kim, Nayoung Kim, Suwan Jeon, Minseong Heo, Jonghwa Shin‡. "Universal metasurfaces for complete linear control of coherent light transmission". *Advanced Materials (2022)*.
- Jun Sae Han\*, Hyeonjin Park, Ji-Young Jeong, Joonkyo Jung, Eun-Ji Gwak, Eun-chae Jeon, Tae-Jin Je, Jonghwa Shin, Doo-Sun Choi‡. "Ultrawide meta-film replication process for the mass production of a flexible microwave absorbing meta-surface". *Optics Express (2022)*.
- Jang Hwan Kim\*, Suwan Jeon, Jae Hyun In, Seonho Nam, Hyeong Min Jin, Kyu Hyo Han, Geon Gug Yang, Hee Jae Choi, Kyung Min Kim, Jonghwa Shin, Seung-Woo Son, Seok Joon Kwon‡, Bong Hoon Kim‡, Sang Ouk Kim‡. "Nanoscale physical unclonable function labels based on block copolymer self-assembly". *Nature Electronics (2022)*.
- Chi Hao Liow\*, Hyeonmuk Kang, Seunggu Kim, Moony Na, Yongju Lee, Arthur Baucour, Kihoon Bang, Yoonsu Shim, Jacob Choe, Gyuseong Hwang, Seongwoo Cho, Gun Park, Jiwon Yeom, Joshua C. Agar, Jong Min Yuk, Jonghwa Shin, Hyuck Mo Lee, Hye Ryung Byon, EunAe Cho, Seungbum Hong‡. "Machine learning assisted synthesis of lithium-ion batteries cathode materials". *Nano Energy (2022)*.
- Arthur Baucour\*, Myungjoon Kim, Jonghwa Shin‡. "Data-driven concurrent nanostructure optimization based on conditional generative adverserial networks". *Nanophotonics (2022)*.
- Sang-Hyeon Nam\*, Myungjoon Kim\*, Nayoung Kim\*, Donghwi Cho, Myungwoo Choi, Jun Hyung Park, Jonghwa Shin‡, Seokwoo Jeon‡. "Photolithographic realization of target nanostructures in 3D space by inverse design of phase modulation". *Science Advances (2022)*.
- Seokhwan Min\*, Suwan Jeon\*, Kyungsun Yun, Jonghwa Shin‡. "All-Color Sub-ambient Radiative Cooling Based on Photoluminescence". *ACS Photonics (2022)*.
- Xianji Piao\*, Jonghwa Shin, Namkyoo Park‡. "Photonic topological Lifshitz interfaces". *Nanophotonics (2022)*.

**2021**

- Yongjune Kim\*, Pyoungwon Park, Jeongdai Jo, Joonsik Lee, Leekyo Jeong, Jonghwa Shin, Jeong-Hae Lee‡, Hak-Joo Lee‡. "Ultrawideband electromagnetic metamaterial absorber utilizing coherent absorptions and surface plasmon polaritons based on double layer carbon metapatterns". *Scientific Reports (2021)*.
- Tae Yeol Yoon\*, Soomin Son\*, Seokhwan Min, Dongwoo Chae, Ho Young Woo, Ji-Yeon Chae, Hangyu Lim, Jonghwa Shin, Taejong Paik‡, Heon Lee‡. "Colloidal deposition of colored daytime radiative cooling films using nanoparticle-based inks". *Materials Today Physics (2021)*.
- Ji-Young Jeon\*, Je-Ryung Lee, Hyeonjin Park, Joonkyo Jung, Doo-Sun Choi, Eun-chae Jeon, Jonghwa Shin, Jun Sae Han‡, Tae-Jin Je‡. "Fabrication and characterization of resistive double square loop arrays for ultra-wide bandwidth microwave absorption". *Scientific Reports (2021)*.
- Nayeun Lee\*, Reehyang Kim, Ju Young Kim, Jong Beom Ko, Sang-Hee Ko Park, Sang Ouk Kim, Mark L. Brongersma, Jonghwa Shin‡. "Self-Assembled Nano-Lotus Pod Metasurface for Light Trapping". *ACS Photonics (2021)*.
- Suwan Jeon\*, Jonghwa Shin‡. "Directional radiation for optimal radiative cooling". *Optics Express (2021)*.

## 수상

누리집 News 페이지의 2021-10-13 이후 수상(Award) 글 5건이다. 날짜는 글의 날짜(여러 날에 걸친 학회는 기간)이고, 문장은 글의 요약문 그대로다.[^news]

- 2026-05-27 · Jisung Hwang received the Excellence Award in the KAIST Optics Group Student Research Poster Competition.
- 2026-02-06 · Dohyun Kim received the Excellent Paper Award at the OSK (Optical Society of Korea) 2026 Winter Annual Meeting.
- 2025-02-14 · Minyeol Lee received the Excellent Paper Award at the OSK (Optical Society of Korea) 2025 Winter Annual Meeting.
- 2024-07-25 · Hyeonhee Kim received the Excellence Award at the 2024 KAIST Optics Group Student Research Poster Competition.
- 2024-07-16–2024-07-19 · Mingwan Cho received the Best Poster Award at META 2024, the 14th International Conference on Metamaterials, Photonic Crystals and Plasmonics.

## 소식

누리집 News 페이지의 2021-10-13 이후 글 가운데 학회 참석 7건, 외부보도 5건, 연구실 행사로 분류된 역설계 워크숍 1건, 모두 13건이다. 대괄호는 누리집의 글 분류이고, 날짜는 글의 날짜(여러 날에 걸친 학회는 기간)다. 수상 글은 위 수상 목록에 두었다.[^news]

- 2026-07-19–2026-07-22 · [학회 참석] Attendance at Optics and Photonics Congress 2026 (OPC 2026)
- 2026-05-06 · [외부보도] '빛이 곧 열쇠가 된다' 신개념 홀로그램 기술 개발...복제 어려운 보안 구현
- 2024-10-15 · [외부보도] 빛의 방향에 따라 두 얼굴 야누스같은 메타표면 개발
- 2024-08-04–2024-08-09 · [학회 참석] Attendance at CLEO-PR 2024
- 2024-07-16–2024-07-19 · [학회 참석] Attendance at META 2024, Toyama
- 2024-02-14–2024-02-16 · [학회 참석] Attendance at OSK 35th General Assembly & 2024 Winter Annual Meeting
- 2024-02-13 · [외부보도] 4개 연구실, ′안전관리 우수연구실′ 인증 취득
- 2023-07-18–2023-07-21 · [학회 참석] Attendance at META 2023, Paris
- 2023-07-03–2023-07-06 · [학회 참석] Attendance at PIERS 2023, Prague
- 2023-06-23 · [연구실 행사] Inverse Design Workshop with Prof. Min Seok Jang & Prof. Hamza Kurt
- 2023-02-14–2023-02-17 · [학회 참석] Attendance at OSK 34th General Assembly & 2023 Winter Annual Meeting
- 2022-12-02 · [외부보도] 빛을 완전히 조절할 수 있는 메타렌즈 개발
- 2022-05-27 · [외부보도] 차세대 반도체 나노구조 공정을 혁신하는 새로운 3차원 노광 공정 개발

## 연락과 위치

- 위치: Room 5406, Applied Engineering Building (W1-1)(People 페이지의 교수 연락처 표기)[^people]
- 교수 이메일: qubit@kaist.ac.kr[^people]
[^p1]: T. Chang 외, J. Shin, Advanced Materials 34, 2204085 (온라인 2022-10-03). <https://doi.org/10.1002/adma.202204085> 초록 기준.
[^p2]: H. Kim, J. Jung, J. Shin, Advanced Materials 36, 2406717 (온라인 2024-09-13). <https://doi.org/10.1002/adma.202406717> 초록 기준.
[^p3]: J. Jung, H. Kim, J. Shin, Nanophotonics 12, 1373-1385 (온라인 2023-01-16). <https://doi.org/10.1515/nanoph-2022-0634> 초록 기준.
[^p4]: S.-H. Nam 외, S. Jeon, Science Advances 8, eabm6310 (2022). <https://doi.org/10.1126/sciadv.abm6310> 초록 기준.
[^p5]: M. Kim, N. Kim, J. Shin, Nanophotonics 13, 1467-1474 (온라인 2024-01-15). <https://doi.org/10.1515/nanoph-2023-0786> 초록 기준.
[^p6]: A. Baucour, M. Kim, J. Shin, Nanophotonics 11, 2865-2873 (온라인 2022-05-09). <https://doi.org/10.1515/nanoph-2022-0005> 초록 기준.
[^p7]: M. Kim, H. Park, J. Shin, Nanophotonics 14, 1273-1282 (온라인 2025-02-17). <https://doi.org/10.1515/nanoph-2024-0674> 초록 기준.
[^p8]: S. Jeon 외, J. Shin, Advanced Optical Materials 11, 2202129 (온라인 2022-12-22). <https://doi.org/10.1002/adom.202202129> 초록 기준.
[^home]: 연구실 누리집 첫 화면 <https://www.meta-material.org/> (제목, Research Applications 구역의 네 응용, Latest News 구역의 모집 안내, 2026-10-23 열람)
[^contact]: 연구실 누리집 Contact 페이지 <https://www.meta-material.org/contact.html> (모집 안내와 분야, 2026-10-23 열람)
[^research]: 연구실 누리집 Research 페이지 <https://www.meta-material.org/research.html> (네 연구 주제의 요약, 주제별 설명과 논문. 페이지가 불러오는 자료 파일 <https://www.meta-material.org/scripts/research-data.js>에서 읽음, 2026-10-23 열람)
[^people]: 연구실 누리집 People 페이지 <https://www.meta-material.org/people.html> (Professor 구역의 연락처·학위·경력, 구성원·Alumni 카드. 카드 내용은 페이지가 불러오는 자료 파일 <https://www.meta-material.org/scripts/people-data.js>에서 읽음, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publications 페이지 <https://www.meta-material.org/publication.html> (2026–2021년 연도 구역. 페이지가 불러오는 자료 파일 <https://www.meta-material.org/scripts/publication-data.js>에서 읽음, 2026-10-23 열람)
[^news]: 연구실 누리집 News 페이지 <https://www.meta-material.org/news.html> (수상·학회 참석·외부보도·연구실 행사 글. 페이지가 불러오는 자료 파일 <https://www.meta-material.org/scripts/news-data.js>에서 읽음, 2026-10-23 열람)
[^mse]: KAIST 신소재공학과 연구실 소개 페이지 「FIND YOUR LAB」 <https://mse.kaist.ac.kr/lab2026/lab01.html> (신종화 항목의 영문 연구실 명칭, Academic·Plain Language 한 줄 소개, 핵심어, 연구실 홈페이지, 2026-10-23 열람)
[^mseen]: KAIST 신소재공학과 영문 연구실 목록 <https://mse.kaist.ac.kr/index.php?mid=mse_lab_en> (Advanced Photonic Materials and Devices Lab 항목의 소개문, 2026-10-23 열람)

# 🚨 응급상황 자동 인식 및 응급실 연계 서비스 포털

<div align="center">
  <img src="https://github.com/user-attachments/assets/867b8b2f-6a96-4834-b7d5-edc4426c6772" alt="응급상황 서비스 로고" width="800px" />
  <br><br>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/Transformers-FF6F00?style=for-the-badge&logo=huggingface&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/NAVER_Maps-03C75A?style=for-the-badge&logo=naver&logoColor=white" />
  <img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <br><br>
  <p><i>KT AIVLE School AI 트랙 미니프로젝트 7차</i></p>
</div>

<br>

## 📋 프로젝트 개요

<div align="center">
  <h3><i>"응급상황 자동 인식부터 응급실 연계 서비스 포털 구축까지"</i></h3>
</div>

<br>

본 프로젝트는 응급 상황에서 환자의 생명을 구하기 위한 핵심 요소인 '빠른 판단'과 '신속한 이송'을 지원하는 AI 기반 서비스 포털을 개발하는 것을 목표로 합니다. 응급 전화를 통해 접수된 상황을 자동으로 인식하고, 응급 등급을 분류한 후, 환자와 가까운 적절한 응급실을 추천하는 통합 웹 애플리케이션을 구축했습니다.

본 프로젝트는 6차 미니프로젝트에서 개발한 기술을 고도화하여 사용자 친화적인 웹 포털로 발전시킨 것입니다. 사용자는 자신의 응급 상황을 입력하고 현재 위치 정보를 함께 제공하면, 시스템이 KTAS 등급을 분류하고 가까운 응급실을 추천해주는 서비스를 이용할 수 있습니다.

<br>

## ⏰ 프로젝트 기간
- 2025년 3월 1일 — 2025년 3월 6일 (6일간)

<br>

## 🔍 시스템 구성

### 📊 서비스 아키텍처

<div align="center">
  <img width="1121" alt="스크린샷 2025-03-05 오후 11 11 46" src="https://github.com/user-attachments/assets/5d2777f9-2e25-46a6-a466-4fe0a7dce694" />
</div>
<br>

### 주요 컴포넌트:

1. **프론트엔드 (View Template Engine with Spring Boot)**
   - 사용자 인터페이스 제공
   - 응급 상황 입력 및 위치 정보 수집
   - 응급실 추천 결과 표시

2. **백엔드 (Spring Boot + FastAPI)**
   - 프론트엔드와 AI 모델 서비스 연동
   - 사용자 요청 처리 및 응답 생성
   - 로그 기록 및 데이터 관리

3. **AI 모듈 (FastAPI)**
   - OpenAI Whisper: 음성 인식(STT)
   - GPT-3.5-turbo: 텍스트 요약 및 키워드 추출
   - KLUE/BERT: 한국어 응급상황 텍스트 분류
   - NAVER Maps API: 실시간 도로 거리 및 소요시간 계산
   - 공공데이터 포털 API: 전국 응급의료기관 정보 조회

4. **데이터베이스**
   - SQLite3: 로그 및 관리 데이터 저장

5. **인프라스트럭처**
   - Docker: 컨테이너화 및 배포
   - Microsoft Azure: 클라우드 웹 서버 환경 제공

<br>

## 🏥 한국 응급환자 중증도 분류 기준 (KTAS)
<div align="center">
  <img width="600" alt="KTAS 분류 기준" src="https://github.com/user-attachments/assets/dc6a3e6b-76e7-4d65-810d-37c5f18112b5" />
</div>

응급환자의 중증도 분류를 위해 한국 응급환자 중증도 분류기준(Korean Triage and Acuity Scale, KTAS)을 활용하였습니다. 이 기준은 보건복지부고시(제2023-287호, 2023.12.28. 시행 2024.1.1)에 의해 규정되어 있습니다.

### 중증도 등급 분류

| 등급 | 분류 | 상태 | 대응 필요성 |
|-----|-----|------|------------|
| 1등급 | 소생 | 생명이나 사지가 위험한 상태 | 즉시 처치 필요 |
| 2등급 | 긴급 | 생명이나 사지가 위험할 가능성이 있는 상태 | 매우 긴급한 처치 필요 |
| 3등급 | 응급 | 응급 처치가 필요하나 생명이나 사지 위험이 낮은 상태 | 긴급 처치 필요 |
| 4등급 | 준응급 | 환자 상태가 안정적이며 응급으로 치료할 필요가 낮은 상태 | 비교적 빠른 처치 필요 |
| 5등급 | 비응급 | 경증 질환 상태 | 긴급하지 않은 처치 가능 |

<br>

## 🛠️ 기술 스택

<div align="center">
  <table>
    <tr>
      <th colspan="2" align="center">분류</th>
      <th align="center">기술</th>
      <th align="center">용도</th>
    </tr>
    <tr>
      <td rowspan="3" width="10%">💻</td>
      <td width="20%"><b>언어</b></td>
      <td width="25%">Python, Java</td>
      <td width="45%">백엔드 및 AI 모델 개발</td>
    </tr>
    <tr>
      <td><b>데이터 처리</b></td>
      <td>Pandas, NumPy</td>
      <td>데이터프레임 조작 및 전처리</td>
    </tr>
    <tr>
      <td><b>프론트엔드</b></td>
      <td>HTML, CSS, JavaScript</td>
      <td>사용자 인터페이스 구현</td>
    </tr>
    <tr>
      <td rowspan="8">🤖</td>
      <td rowspan="3"><b>프레임워크</b></td>
      <td>Spring Boot</td>
      <td>웹 애플리케이션 백엔드 개발</td>
    </tr>
    <tr>
      <td>FastAPI</td>
      <td>AI 모델 서비스 API 구현</td>
    </tr>
    <tr>
      <td>Thymeleaf</td>
      <td>서버 사이드 템플릿 엔진</td>
    </tr>
    <tr>
      <td rowspan="2"><b>API</b></td>
      <td>OpenAI API</td>
      <td>음성 인식(Whisper) 및 텍스트 요약(GPT)</td>
    </tr>
    <tr>
      <td>NAVER Maps API</td>
      <td>도로 거리 및 소요 시간 계산</td>
    </tr>
    <tr>
      <td rowspan="3"><b>모델링</b></td>
      <td>Transformers</td>
      <td>BERT 모델 로딩 및 파인튜닝</td>
    </tr>
    <tr>
      <td>PyTorch</td>
      <td>딥러닝 모델 학습</td>
    </tr>
    <tr>
      <td>Scikit-learn</td>
      <td>데이터 전처리, 모델 평가</td>
    </tr>
    <tr>
      <td rowspan="3">☁️</td>
      <td rowspan="3"><b>인프라</b></td>
      <td>Docker</td>
      <td>컨테이너화 및 배포</td>
    </tr>
    <tr>
      <td>Microsoft Azure</td>
      <td>클라우드 웹 서버 배포</td>
    </tr>
    <tr>
      <td>SQLite3</td>
      <td>데이터베이스 관리</td>
    </tr>
  </table>
</div>

<br>

## 💻 주요 기능 및 화면 구성

### 1️⃣ 응급 상황 입력 및 위치 정보 수집

<img width="1121" alt="메인 화면 - 응급상황 입력" src="https://github.com/user-attachments/assets/cd1841cd-70d8-4909-9a52-971cac687c90" />

**주요 기능**
* 사용자가 응급 상황을 텍스트 또는 음성으로 입력
* 위도/경도 정보를 통한 현재 위치 파악
* 추천받을 응급실 개수 조정 가능

**화면 구성**
* 직관적인 응급 상황 텍스트 입력 필드
* 간편한 위도/경도 입력 필드
* 사용자 맞춤형 병원 추천 수 설정 옵션


### 2️⃣ KTAS 기반 응급 등급 분류

<img width="1121" alt="KTAS 정보 화면" src="https://github.com/user-attachments/assets/fd7cebe1-ce71-4d56-bf0f-b77eb0b9811d" />

**주요 기능**
* KLUE/BERT 모델을 활용한 응급 상황 텍스트 분석
* 1~5등급의 KTAS 중증도 분류 자동 수행
* 등급별 적절한 대응 방법 안내

**화면 구성**
* 직관적인 KTAS 분류 체계 설명
* 등급별 응급 상황 예시와 특징 제공
* 응급 상황 대처 방법 시각화


### 3️⃣ 최적 응급실 추천

<img width="1121" alt="응급실 추천 결과 화면" src="https://github.com/user-attachments/assets/bd7ab544-8356-4718-8920-4eafc9b02c9f" />

**주요 기능**
* 사용자 위치 기반 가까운 응급실 목록 제공
* 응급 등급과 거리를 고려한 최적 응급실 추천
* 응급실 상세 정보(이름, 주소, 유형, 전화번호) 제공

**화면 구성**
* 가독성 높은 응급실 목록 테이블
* 현재 위치 기준 거리 정보 표시
* KTAS 등급에 따른 맞춤형 권장 사항


### 4️⃣ 서비스 소개 및 응급처치 정보

<img width="1121" alt="사이트 소개 화면" src="https://github.com/user-attachments/assets/d8d2daa8-5897-42f0-81a7-727501320e53" />

**주요 기능**
* 서비스 목적 및 핵심 기능 안내
* 응급실 이용 가이드라인 제공
* 기본 응급처치 방법 설명

**화면 구성**
* 사용자 친화적 디자인
* 단계별 서비스 이용 방법 안내
* 응급 상황 대처 정보 시각화


### 5️⃣ 관리자 기능

<img width="1121" alt="관리자 페이지" src="https://github.com/user-attachments/assets/b270a985-76f4-4f07-86fd-969429ccbc0f" />

**주요 기능**
* 응급 상황 요청 이력 관리
* 기간별 로그 데이터 분석
* 사용자 커뮤니케이션을 위한 게시판 기능

**화면 구성**
* 종합 조회 기록 대시보드
* 상세 요청 정보(상황, 위치, 중증도) 표시
* 기간별 데이터 필터링 및 통계 시각화

> **참고**: 관리자 페이지는 개발 완료되었으나, 시간 제약으로 최종 배포 버전에는 포함되지 않았습니다. 향후 업데이트에서 추가될 예정입니다.

<br>

## 📝 데이터베이스 기능

### 로그 기록 기능
- 사용자의 응급 상황 입력 정보 저장
- 위치 데이터(위도/경도) 기록
- KTAS 등급 분류 결과 저장
- 추천된 응급실 정보 보관
- 요청 시간 타임스탬프 관리

### 동적 병원 정보 저장
- 추천 병원 수에 따른 동적 데이터 구조 지원
- 최대 10개까지 응급실 정보 저장 가능
- 병원명, 주소, 전화번호 등 상세 정보 보관
- 관리자 조회를 위한 데이터베이스 구조 최적화

### 게시판 기능
- 사용자 커뮤니케이션을 위한 게시판 구현
- 사용자 ID 및 비밀번호 기반 게시글 관리
- 게시글 작성, 조회, 삭제 기능 제공
- 다양한 검색 옵션을 통한 게시글 필터링

<br>
## 📚 프로젝트 배운점 및 회고

<div align="center">
  <table>
    <tr>
      <td width="30%" align="center">📊<br><b>API 연동의 중요성</b></td>
      <td width="70%">다양한 외부 API(OpenAI, NAVER Maps, 공공데이터)를 효과적으로 연동하여 복잡한 서비스 파이프라인 구축하는 방법 습득</td>
    </tr>
    <tr>
      <td align="center">🔄<br><b>파이프라인 설계</b></td>
      <td>음성 인식부터 응급실 추천까지 일관된 데이터 흐름을 설계하고 각 모듈 간 효율적인 연계 방식 학습</td>
    </tr>
    <tr>
      <td align="center">⚙️<br><b>모듈화된 시스템 설계</b></td>
      <td>각 기능을 독립적인 모듈로 분리함으로써 유지보수성을 높이고 단계별 성능 최적화가 가능한 구조 설계 방법 습득</td>
    </tr>
    <tr>
      <td align="center">💼<br><b>실제 응급 상황 이해</b></td>
      <td>한국 응급환자 중증도 분류기준(KTAS)과 실제 응급 의료 시스템에 대한 이해를 통해 실용적인 AI 솔루션 개발의 중요성 인식</td>
    </tr>
    <tr>
      <td align="center">🚨<br><b>사회적 문제 해결</b></td>
      <td>응급실 과밀화와 중증 응급환자의 적정 치료 문제와 같은 사회적 과제에 AI 기술을 적용하여 해결책을 모색하는 경험 획득</td>
    </tr>
    <tr>
      <td align="center">👥<br><b>협업 능력 향상</b></td>
      <td>각자 전문 분야가 다른 6명의 팀원들이 하나의 서비스를 위해 효율적으로 역할을 분담하고 통합하는 과정에서 협업 역량 강화</td>
    </tr>
    <tr>
      <td align="center">🔗<br><b>마이크로서비스 구현</b></td>
      <td>Spring Boot와 FastAPI를 연동한 마이크로서비스 아키텍처 설계로 각 서비스의 독립성을 보장하고 확장성을 높이는 방법 학습</td>
    </tr>
    <tr>
      <td align="center">🖥️<br><b>UI/UX 디자인 이해</b></td>
      <td>응급 상황에서 사용자가 빠르고 직관적으로 서비스를 이용할 수 있는 인터페이스 설계의 중요성 체득</td>
    </tr>
    <tr>
      <td align="center">⏱️<br><b>시간 제약 관리</b></td>
      <td>6일이라는 짧은 프로젝트 기간 내에 MVP를 구현하고 핵심 기능을 우선적으로 개발하는 전략적 의사결정 능력 향상</td>
    </tr>
    <tr>
      <td align="center">🚀<br><b>클라우드 배포 경험</b></td>
      <td>Docker 컨테이너화를 통한 애플리케이션 패키징과 Microsoft Azure 클라우드 플랫폼을 활용한 웹 서비스 배포 과정 습득</td>
    </tr>
    <tr>
  </table>
</div>

이번 프로젝트는 의료 AI와 공공 데이터를 활용한 실용적인 서비스 개발의 가능성을 확인하는 소중한 경험이었으며, 기술의 사회적 가치 창출에 대한 새로운 시각을 얻을 수 있었습니다.

## 📈 향후 개선 방향

1. **UI/UX 개선**
   - 사용자 위치 자동 감지 기능 추가
   - 응급실 길찾기 네비게이션 제공
   - 모바일 앱 개발을 통한 접근성 향상

2. **기능 확장**
   - 실시간 응급실 병상 정보 연동
   - 응급 의료진과의 실시간 커뮤니케이션 기능
   - 사용자 계정 관리 및 응급 연락처 저장 기능

3. **성능 개선**
   - KTAS 분류 모델의 정확도 향상을 위한 추가 학습
   - 마이크로서비스 간 통신 최적화
   - 실시간 교통 상황을 고려한 더 정확한 도착 시간 예측

4. **보안 강화**
   - 사용자 개인정보 보호 강화
   - 의료 데이터 암호화 및 안전한 저장
   - 시스템 접근 권한 관리 개선

<br>

## 👨‍💻 팀원

<div align="center">
  <table>
    <tr>
      <td align="center"><b>구종한</b></td>
      <td align="center"><b>김예은</b></td>
      <td align="center"><b>이대희</b></td>
      <td align="center"><b>정재원</b></td>
      <td align="center"><b>황유성</b></td>
      <td align="center"><b>황은비</b></td>
    </tr>
  </table>
</div>
<br>

---

<div align="center">
  <p>본 프로젝트는 KT AIVLE School AI 트랙 미니프로젝트 7차로 진행되었습니다.</p>
  <p>© 2025 KT AIVLE School 6기 AI 트랙 미니프로젝트</p>
</div>

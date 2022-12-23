# 필루미: 계층적 분류 모델을 적용한 스마트폰 알약 복약정보 시스템
#### 2022학년도 2학기 경희대학교 데이터분석캡스톤디자인 프로젝트 입니다.


## 💊 서비스 소개
약통이 사라져서 내가 가지고 있는 약이 소화제인지 소염제인지 헷갈렸던 적 있으신가요?  
인터넷에 검색을 해도 복잡하고 어려운 용어들로 구성된 알약 설명들이 읽기 힘드셨던 적은요?  

약물에 대한 전문 지식이 부족한 일반인들이 알약에 대해서 올바른 복약정보를 얻기는 쉽지 않습니다.  
따라서 저희는 일반인들이 약물오남용에 쉽게 노출되는 상황을 줄이기 위해 본 서비스를 기획하게 되었습니다.  

알약 앞/뒤 사진만으로 손쉽게 알약 복약정보를 검색해보세요!  
<img width="600" alt="main-pillumi" src="https://user-images.githubusercontent.com/57142322/202414358-dd2c3737-4507-42b7-8a48-8a67ccb2e1ea.png">

### README.md 모음
+ [모바일 앱: Flutter](https://github.com/sparksub/pillumi-khu/tree/main/front)
+ [서버: Flask](https://github.com/sparksub/pillumi-khu/tree/main/server)
+ [분석모델: Tensorflow]() TBA


## 🎯 개발 목표
* 공공데이터포털에 공개된 24774종 의약품 데이터에 대해 계층적 이미지 분류 모델 구축
* 스마트폰 카메라로 알약 앞, 뒷면을 촬영하여 2500여종 알약의 쉬운 복약정보를 검색할 수 있는 모바일 앱 및 서버 개발


## ⚙️ 기술스택 & 개발환경

### 사용언어 및 프레임워크
<img width="600" alt="framework-pillumi" src="https://user-images.githubusercontent.com/57142322/202414219-d129b61c-65f8-45bd-b5fc-9de5f1210eb0.png">

+ 모바일 앱: Flutter (Dart)
+ Backend: Flask (Python)
+ 분석 모델: Tensorflow (Python)


### 사용 데이터 셋 & API
<img width="600" alt="dataset-pillumi" src="https://user-images.githubusercontent.com/57142322/202414551-6aaee5be-2ba3-4df3-9a78-d933a4c7fcb1.png">

+ [식품의약품안전처: 의약품 낱알식별 정보](https://www.data.go.kr/data/15057639/openapi.do)
+ [식품의약품안전처: 의약품 개요정보 (e약은요)](https://www.data.go.kr/data/15075057/openapi.do) 
+ [약학정보원: 복약정보 픽토그램](https://www.health.kr/mediCounsel/pictogram_print.asp)


## 👊 팀 소개
### 경희대학교 소프트웨어융합학과 18학번 박재훈
🏠 Homepage: https://github.com/jaehun-park  
💻 Role: 분석 모델 개발

### 경희대학교 소프트웨어융합학과 19학번 박수빈
🏠 Homepage: https://nt.dariasubin.me/  
💻 Role: 모바일 앱, 서버 개발




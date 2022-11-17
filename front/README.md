# Flutter Project for Pillumi

필루미 모바일 앱에 대한 문서입니다.  

## Directory Tree
```bash
.
├── README.md
├── analysis_options.yaml
├── pubspec.lock
├── pubspec.yaml
├── android
├── ios
├── assets
└──  lib
    ├── main.dart
    ├── api
    │   ├── class
    │   └── search_pill.dart
    ├── screens
    ├── util
    └── widgets
        ├── button
        ├── card
        ├── dialog
        └── view
``` 

## Installation

1. Run ```flutter pub get```.  
2. Run ```flutter run```.  


## Networking Connecting
```bash
.
└── lib
    └── api
        └── search_pill.dart
```

```dart:search_pill.dart
String base_url = 'http://<YOUR IP ADDRESS>:5001';
```
만약, 기기를 연결해서 사용한다면 아래 내용을 참고해 ```base_url```를 수정해주세요.

### Android Emulator
[Android Emulator 네트워킹 설정](https://developer.android.com/studio/run/emulator-networking.html) 문서를 참고해주세요.  
```dart:search_pill.dart
String base_url = 'http://10.0.2.2:5001';
```

### ios Emulator
1. Terminal에서 서버를 돌리고 있는 내 local의 ip를 찾습니다.  

```bash
ipconfig getifaddr en0
```

2. ```base_url```을 찾은 ip로 수정해주세요.
```dart:search_pill.dart
String base_url = 'http://<Change ME>:5001';
```

## Permission
+ Camera  
+ Photo library

## Dart Packages
```yaml
...
dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^2.0.0
  permission_handler: ^10.2.0
  image_picker: ^0.8.6
  http: ^0.13.5
  flutter_native_splash: ^2.2.14
...
```


## UI Design
### Design system
<img width="600" alt="design-system-pillumi" src="https://user-images.githubusercontent.com/57142322/202423464-005c5426-5889-49de-a634-c5ba7452f0b0.png">  


### Flowchart
<img width="600" alt="ui-info2-pillumi" src="https://user-images.githubusercontent.com/57142322/202419827-4b1ec990-7f18-4651-afc0-5f8a90fe5a8c.png">

### Main feature
<img width="600" alt="ui-info1-pillumi" src="https://user-images.githubusercontent.com/57142322/202419834-2b2778ef-afa6-40cc-bda9-eef66c5bb15a.png">  
<img width="600" alt="ui-flowchart-pillumi" src="https://user-images.githubusercontent.com/57142322/202419839-aaddff93-fbca-4b12-b047-32390caf2f9c.png">

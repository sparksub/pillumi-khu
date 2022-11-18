# Flask Project for Pillumi

필루미 서버에 대한 문서입니다.  

## Directory Tree
```bash
.
├── README.md
├── app.py
├── utils.py
├── requirements.txt
├── .gitignore
├── api
│   ├── __init__.py
│   ├── pill_model
│   └── pill_search
│       ├── model
│       └── util
├── assets
│   └── pictogram
└── templates
    └── pillumi.html
```

## Installation

1. ```requirements.txt```를 참고하여 package를 다운 받아 주세요.    
2. ```utils.py```의 ```ip```와 ```serviceKey```를 수정해주세요.  
3. ```app.py```를 실행시켜주세요.  


## Setting IP Address
```bash
.
└── utils.py
```

```python:utils.py
...
ip = '<YOUR IP ADDRESS>'
```
만약, 기기를 연결해서 사용한다면 아래 내용을 참고해 ```ip```를 수정해주세요.

### No emulator
```python:utils.py
ip = '127.0.0.1'
```

### With android emulator
[Android Emulator 네트워킹 설정](https://developer.android.com/studio/run/emulator-networking.html) 문서를 참고해주세요.  
```python:utils.py
ip = '10.0.2.2'
```

### With ios emulator
1. Terminal에서 서버를 돌리고 있는 내 local의 ip를 찾습니다.  

```bash
ipconfig getifaddr en0
```

2. ```ip```을 찾은 ip로 수정해주세요.
```python:app.py
ip = '<YOUR IP ADDRESS>'
```

## Setting API

본 서버는 [식품의약품안전처의 의약품개요정보(e약은요)](https://www.data.go.kr/data/15075057/openapi.do) API와 연결되어 구동되는 서비스 입니다.  
따라서 서버를 동작하기 위해서는 위 링크에 접속하여 데이터 사용 신청을 해서 인증키를 받아야 합니다.  

데이터 사용 신청 이후 부여 받은 인증키를 아래 경로의 ```serviceKey``` 부분에 수정하여 사용해주세요.
```bash
.
└── utils.py
```

```python:utils.py
serviceKey = "<YOUR DECODE KEY>"
```

## Rest API Documents
```bash
.
└── templates
    └── pillumi.html
```
Swagger를 사용하여 Rest API를 구성했습니다.  
서버를 실행한 뒤, IP에 접속해서 확인해보세요!

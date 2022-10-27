import requests
import pprint
import PrivateKey

import pandas as pd
import bs4

# Response element #
'''
resultCode: 결과코드
resultMsg: 결과메시지
numOfRows: 한 페이지 결과수
pageNo: 페이지 번호
totalCount: 전체 결과 수
ITEM_SEQ: 품목 일련번호
ITEM_NAME: 품목명
ENTP_SEQ: 업체일련번호
ENTP_NAME: 업체명
CHART: 성상
ITEM_IMAGE: 큰제품이미지
PRINT_FRONT: 표시(앞)
PRINT_BACK: 표시(뒤)
DRUG_SHAPE: 의약품모양
COLOR_CLASS1: 색깔(앞)
COLOR_CLASS2: 색깔(뒤)
LINE_FRONT: 분할선(앞)
LINE_BACK: 분할선(뒤)
LENG_LONG: 크기(장축)
LENG_SHORT: 크기(단축)
THICK: 크기(두께)
IMG_REGIST_TS: 약학정보원 이미지 생성일
CLASS_NO: 분류번호
CLASS_NAME: 분류명
ETC_OTC_NAME: 전문/일반
ITEM_PERMIT_DATE: 품목허가일자
FORM_CODE_NAME: 제형코드이름
MARK_CODE_FRONT_ANAL: 마크내용(앞)
MARK_CODE_BACK_ANAL: 마크내용(뒤)
MARK_CODE_FRONT_IMG: 마크이미지(앞)
MARK_CODE_BACK_IMG: 마크이미지(뒤)
CHANGE_DATE: 변경일자
MARK_CODE_FRONT: 마크코드(앞)
MARK_CODE_BACK: 마크코드(뒤)
ITEM_ENG_NAME: 제품영문명
EDI_CODE: 보험코드
'''

# 인증키 입력
encoding = PrivateKey.encoding
decoding = PrivateKey.decoding


# final page number = 2474
pill_list = []
name_list = []  # 열이름값

for pageNo in range(1, 2474):
    print(pageNo)
    # url 입력
    url = 'http://apis.data.go.kr/1471000/MdcinGrnIdntfcInfoService01/getMdcinGrnIdntfcInfoList01'
    params = {'serviceKey': decoding,
              # 'item_name': '',
              # 'entp_name': '',
              # 'item_seq': '',
              # 'img_regist_ts': '',
              'pageNo': pageNo,
              'numOfRows': 10,
              # 'edi_code': '',
              # 'type': 'xml'
              }

    response = requests.get(url, params=params)

    # xml 내용
    content = response.text

    # 출력
    pp = pprint.PrettyPrinter(indent=4)
    # print(pp.pprint(content))


    # xml을 dataFrame으로 변환
    xml_obj = bs4.BeautifulSoup(content, 'lxml-xml')
    rows = xml_obj.findAll('item')
    # print(rows)

    # 각 행의 컬럼, 이름, 값을 가지는 리스트 만들기
    value_list = []  # 데이터값

    # xml 안의 데이터 수집
    for i in range(0, len(rows)):
        columns = rows[i].find_all()
        # 첫째 행 데이터 수집
        for j in range(0, len(columns)):
            if i == 0 and pageNo == 1:
                # 컬럼 이름 값 저장
                name_list.append(columns[j].name)
            # 컬럼의 각 데이터 값 저장
            value_list.append(columns[j].text)
        # 각 행의 value값 전체 저장
        pill_list.append(value_list)
        # 데이터 리스트 값 초기화
        value_list = []

print(name_list)
print(pill_list)

# xml값 DataFrame으로 만들기
pill_df = pd.DataFrame(pill_list, columns=name_list)

pill_df.to_csv('pill_kr.csv', encoding='utf-8-sig')

import requests
import bs4

from api.pill_search.util.make_pictogram_list import make_pictogram_list
import utils

def get_pill_info(pill_code, pill_class):
    """
    api 결과 정리 (** 알약 분류정보 없음**)
    # 0 'entpName' : 업체명
    # 1 'itemName' : 제품명
    # 3 'efcyQesitm' : 효능
    # 4 'useMethodQesitm' : 사용법
    # 5 'atpnWarnQesitm' : 사용전, 주의사항경고
    # 6 'atpnQesitm' : 사용 시, 주의사항
    # 7 'intrcQesitm' : 상호작용
    # 8 'seQesitm' : 부작용
    # 9 'depositMethodQesitm' : 보관법
    # 12 'itemImage' : 이미지
    """

    try:
        # decoding = PrivateKey.decoding

        url = 'http://apis.data.go.kr/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList'
        params = {
            'serviceKey': utils.serviceKey,
            'itemSeq': pill_code,
            # 'pageNo': pill_code,
            # 'numOfRows': '1',
        }

        response = requests.get(url, params=params)

        # xml 내용
        content = response.text
        # print(content)

        # xml을 dataFrame으로 변환
        xml_obj = bs4.BeautifulSoup(content, 'lxml-xml')
        rows = xml_obj.findAll('item')

        # 각 행의 컬럼, 이름, 값을 가지는 리스트 만들기
        value_list = []  # 데이터값
        name_list = []

        # xml 안의 데이터 수집
        for i in range(0, len(rows)):
            columns = rows[i].find_all()
            # 첫째 행 데이터 수집
            for j in range(0, len(columns)):
                name_list.append(columns[j].name)
                # 컬럼의 각 데이터 값 저장
                value_list.append(columns[j].text)
        # print(name_list)
        # print(value_list)

        for i in range(0, len(value_list)):
            txt = value_list[i]
            txt = txt.replace("</p><p>", "\n")
            txt = txt.replace("<p>", "")
            txt = txt.replace("</p>", "")
            txt = txt.replace("\n", " ")
            txt = txt.replace("HTTPS://NEDRUG.MFDS.GO.KR/PBP/CMN/ITEMIMAGEDOWNLOAD/", "http://nedrug.mfds.go.kr/pbp/cmn/itemImageDownload/")
            new_txt = txt.replace("\xa0", " ")
            value_list[i] = new_txt

        pictogram_list = make_pictogram_list(value_list)

        return {
            "ITEM_NAME": value_list[1],
            "ENTP_NAME": value_list[0],
            "CLASS_NAME": pill_class,
            "Efficacy": value_list[3],
            "Dosage": value_list[4],
            "AtpnWarnQesitm": value_list[5],
            "AtpnQesitm": value_list[6],
            "IntrcQesitm": value_list[7],
            "SeQesitm": value_list[8],
            "DepositMethodQesitm": value_list[9],
            "PillImg": value_list[12],
            "PictogramList": pictogram_list
        }
    # "http://nedrug.mfds.go.kr/pbp/cmn/itemImageDownload/147426411393800107"
    except Exception as e:
        return str(e)

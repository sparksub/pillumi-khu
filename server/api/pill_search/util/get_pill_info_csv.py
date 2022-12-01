import pandas as pd

from api.pill_search.util.make_pictogram_list import make_pictogram_list
from pykospacing import Spacing


def get_pill_info_csv(pill_code, pill_class, pill_img):
    try:
        pills_df = pd.read_csv("/Users/sparksub/Documents/GitHub/pillumi-khu/server/assets/easypill.csv",
                               encoding='utf-8')
        pills_info = pills_df.values

        for i in range(len(pills_info)):
            if pills_info[i][0] == pill_code:
                value_list = pills_info[i]
                for j in range(3, len(value_list)-2):
                    txt = str(value_list[j])
                    txt = txt.replace("  ", "\n")
                    txt = txt.replace(" ", " ")
                    txt = txt.replace("</p>", "")
                    txt = txt.replace("|", ", ")
                    txt = txt.replace(".", ".\n")
                    txt = txt.replace("HTTPS://NEDRUG.MFDS.GO.KR/PBP/CMN/ITEMIMAGEDOWNLOAD/",
                                      "http://nedrug.mfds.go.kr/pbp/cmn/itemImageDownload/")
                    txt = txt.replace("\xa0", " ")
                    # new_txt = Spacing(txt)
                    # print(new_txt)
                    value_list[j] = new_txt

                pictogram_list = make_pictogram_list(value_list)

                result = {
                    "ITEM_NAME": pills_info[i][1],
                    "ENTP_NAME": pills_info[i][2],
                    "CLASS_NAME": pill_class,
                    "Efficacy": pills_info[i][4],
                    "Dosage": pills_info[i][5],
                    "AtpnWarnQesitm": pills_info[i][6],
                    "AtpnQesitm": pills_info[i][7],
                    "IntrcQesitm": pills_info[i][8],
                    "SeQesitm": pills_info[i][9],
                    "DepositMethodQesitm": pills_info[i][10],
                    "PillImg": pill_img.replace("HTTPS://NEDRUG.MFDS.GO.KR/PBP/CMN/ITEMIMAGEDOWNLOAD/",
                                                "http://nedrug.mfds.go.kr/pbp/cmn/itemImageDownload/"),
                    "PictogramList": pictogram_list
                }
                return result

        result = {
            "ITEM_NAME": 'NONE',
            "ENTP_NAME": 'NONE',
            "CLASS_NAME": 'NONE',
            "Efficacy": 'NONE',
            "Dosage": 'NONE',
            "AtpnWarnQesitm": 'NONE',
            "AtpnQesitm": 'NONE',
            "IntrcQesitm": 'NONE',
            "SeQesitm": 'NONE',
            "DepositMethodQesitm": 'NONE',
            "PillImg": 'NONE',
            "PictogramList": []
        }
        return result

    except Exception as e:
        return str(e)

import urllib

import pandas as pd
from urllib import request

from __init__ import LocalPath

'''
/Users/sparksub/Documents/GitHub/IdentificationOfPills/
train_images =  "E:\\Study\\Pill\\SegTest\\Data\\firstDis2\\Training\\Src\\",
train_annotations = "E:\\Study\\Pill\\SegTest\\Data\\firstDis2\\Training\\Mask\\",
checkpoints_path = "E:\\Study\\Pill\\SegTest\\Data\\firstDis2\\Model\\Resnet50", epochs=5
'''

SavePath = LocalPath + "Data/Src/Raw/"
startNum = 10749

def GetPillImage():
    pill_data = pd.read_csv(LocalPath + "Data/Src/pill_kr_all.csv", delimiter=',', low_memory=False)
    print("======START GET PILL IMAGE======")

    FilePathList = pill_data["ITEM_IMAGE"]

    for i, each in enumerate(FilePathList):
        idx = i + startNum
        # 다운 받을 알약 이미지 url
        print("=== Download " + str(idx) + ": " + each)
        pillItemSEQ = str(pill_data.loc[idx, "ITEM_SEQ"])
        desFilePath = SavePath + pillItemSEQ + ".jpg"

        # 파일 다운로드
        urllib.request.urlretrieve(each, desFilePath)

        print("==== Item name: " + pillItemSEQ)
        print("==== Save path: " + desFilePath)

    return pill_data["ITEM_SEQ"]


GetPillImage()

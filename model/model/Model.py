import cv2 as cv
import pandas as pd
import numpy as np
import tensorflow as tf
import ShapePreprocess
import ColorManager

labels_df = pd.read_csv("pill_labels.csv", encoding='utf-8')
same_df = pd.read_csv("pill_same.csv", encoding='utf-8')
shape_model = tf.keras.models.load_model('shape_simplecnn.h5')
print_model = tf.keras.models.load_model('print_simplecnn.h5')


def pill_classification_top5(img_front, img_back):
    # 이미지 정규화
    img_front = ShapePreprocess.image_normalization(img_front)
    img_back = ShapePreprocess.image_normalization(img_back)

    # 모양 분류
    img = cv.cvtColor(img_front, cv.COLOR_BGR2GRAY)
    ret, thr = cv.threshold(img, 5, 1, cv.THRESH_BINARY)
    x_shape = np.expand_dims(thr, axis=0)
    shape = shape_model.predict(x_shape, verbose=0)

    # 색상 분류
    color = ColorManager.TestType(img_front)

    # 각인 분류
    img_front = cv.cvtColor(img_front, cv.COLOR_BGR2GRAY)
    img_front = cv.equalizeHist(img_front)
    img_front = cv.fastNlMeansDenoising(img_front, None, 10, 7, 21)
    img_front = img_front / 255

    img_back = cv.cvtColor(img_back, cv.COLOR_BGR2GRAY)
    img_back = cv.equalizeHist(img_back)
    img_back = cv.fastNlMeansDenoising(img_back, None, 10, 7, 21)
    img_back = img_back / 255

    img_front = np.expand_dims(img_front, axis=0)
    img_back = np.expand_dims(img_back, axis=0)
    print_front = print_model.predict(img_front, verbose=0)
    print_back = print_model.predict(img_back, verbose=0)

    # 분류 결과 바탕으로 search
    pred = []
    for i, row in labels_df.iterrows():
        temp = 1
        temp *= shape[0, row['SHAPE']]
        temp *= 1 if row['COLOR'] == color else 0

        # 앞/뒤 사진이 바뀌었을 경우를 대비해 두가지 경우 모두 체크
        temp_opp = temp

        temp *= print_front[0, row['PRINT_FRONT']]
        temp *= print_back[0, row['PRINT_BACK']]

        temp_opp *= print_front[0, row['PRINT_BACK']]
        temp_opp *= print_back[0, row['PRINT_FRONT']]

        pred.append([i, max(temp, temp_opp)])

    pred.sort(key=lambda x: x[1], reverse=True)

    # top5 알약 정보 반환
    results = []
    for i, prob in pred:
        if not (same_df['itemSeq'] == labels_df.loc[i, 'ITEM_SEQ']).any():
            continue
        item_info = {'ITEM_NAME': labels_df.loc[i, 'ITEM_NAME'],
                     'CLASS_NAME': labels_df.loc[i, 'CLASS_NAME'],
                     'ITEM_SEQ': labels_df.loc[i, 'ITEM_SEQ'],
                     'ITEM_IMAGE': labels_df.loc[i, 'ITEM_IMAGE'],
                     'ITEM_INDEX': i
                     }
        results.append(item_info)
        if len(results) == 5:
            break

    return results
'''
요약 : Localization 역할
이미지 하나에 알약의 앞면, 뒷면이 같이 나와 있는 경우
    앞면과 뒷면을 각각 잘라내어 저장한다.
'''

import cv2 as cv
import PositionManager
import numpy as np
import os.path as path
import glob


def crop_img(img, contour, save_path, file_name, side):
    # 전체 이미지의 크기
    img_y = img.shape[0]
    img_x = img.shape[1]

    # 현재 컨투어의 좌표
    min_x, min_y, max_x, max_y, cx, cy = PositionManager.GetMinMaxPosInContour(contour, '')

    width = max_x - min_x
    height = max_y - min_y

    diff_value = abs(width - height)

    # 정사각형 배경 안에 전경 이미지 영역을 최대한 크게 한다.
    offset_value = 15
    if width > height:
        x_offset = offset_value
        y_offset = diff_value // 2 + offset_value
    elif width < height:
        x_offset = diff_value // 2 + offset_value
        y_offset = offset_value
    else:
        x_offset = offset_value
        y_offset = offset_value

    init_x = min_x - x_offset
    if init_x < 0:
        init_x = 0

    max_x = max_x + x_offset

    # 전체 이미지의 크기를 벗어나지 않게 조절 한다.
    if max_x > img_x:
        max_x = img_x

    init_y = min_y - y_offset

    if init_y < 0:
        init_y = 0

    max_y = max_y + y_offset
    if max_y > img_y:
        max_y = img_y

    x_length = max_x - init_x
    y_length = max_y - init_y
    diff_xy = abs(x_length - y_length)
    if diff_xy is 0:
        if x_length > y_length:
            max_y = max_y + diff_xy
        else:
            max_x = max_x + diff_xy

    img_masking = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    cv.drawContours(img_masking, [contour], 0, (255, 255, 255), 0)

    # 내부를 흰색으로 채워 줌
    mask = np.zeros((img_masking.shape[0] + 2, img_masking.shape[1] + 2), np.uint8)
    mask[:] = 0
    cv.floodFill(img_masking, mask, (cx, cy), (255, 255, 255))

    # org_img에서 원하는 위치를 마스킹 함.
    dst = cv.copyTo(img, img_masking)

    # 마스킹된 원본 이미지에서 위에서 구한 좌표로 이미지를 잘라낸다.
    final_img = dst[init_y:max_y, init_x:max_x]

    if side == 'front':
        save_path = save_path + 'front/front_' + file_name
        print(save_path)
    else:
        save_path = save_path + 'back/back_' + file_name
        print(save_path)

    cv.imwrite(save_path, final_img)


def separate_front_and_back(file_path):
    file_name = file_path[-9:]

    # 배경 제거된 이미지 로드
    rmbg_img = cv.imread(file_path)

    # 마스킹 이미지 로드
    mask_img_path = '../mask/mask_' + file_name
    mask_img = cv.imread(mask_img_path)
    mask_img = mask_img * 255

    cv.imshow("img_contours", mask_img)
    cv.waitKey(0)

    contours, anomaly = PositionManager.GetPillContour(rmbg_img, mask_img, True)
    number_contour = len(contours)
    save_path = '../Data/separate/'
    if anomaly:
        cv.imwrite(f'../anomaly/img/{file_name}', rmbg_img)
        save_path = '../anomaly/'

    if number_contour == 1 or len(contours[0]) < 100:
        cv.imwrite(f'../anomaly/img_impossible/{file_name}', rmbg_img)
    else:
        crop_img(rmbg_img, contours[0], save_path, file_name, 'front')
        crop_img(rmbg_img, contours[1], save_path, file_name, 'back')


'''
main
'''
FilePathList = glob.glob(path.join('../remove_background', '*.png'))
for each in FilePathList:
    if each[-9:] == '22115.png':
        print('\n' + each)
        separate_front_and_back(each)
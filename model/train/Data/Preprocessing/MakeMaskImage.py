# Mask Image 생성 코드
# 배경 제거 이미지 -> Binary 이미지 {0,255} -> 전체 이미지 데이터를 255로 나눔 {0,1}

import cv2 as cv
import glob
import os.path as path

input_path = "../remove_background"
output_path = "../mask"
file_path_list = glob.glob(path.join(input_path, '*.png'))

# 배경 제거 이미지 -> Mask 이미지
for each in file_path_list:
    if each[-9:] == '22115.png':
        origin = cv.imread(each, cv.IMREAD_GRAYSCALE)

        # 10을 기준, binary data로 변환
        ret, thr = cv.threshold(origin, 5, 255, cv.THRESH_BINARY)

        # mask data는 {0,1} 값으로 구성됨(배경 : 0, 전경 :1 )
        thr = thr / 255

        print(f"{output_path}/mask_{each[-9:]}")
        cv.imwrite(f"{output_path}/mask_{each[-9:]}", thr)

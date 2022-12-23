# 배경 이미지를 잘라내어 전체 이미지에서 배경 비율을 줄이고
# 전경 비율을 늘린다.

import cv2 as cv
import numpy as np


def make_fit_size(img):
    while True:
        if np.all(img[0, :] == 0):
            img = np.delete(img, 0, axis=0)
        elif np.all(img[-1, :] == 0):
            img = np.delete(img, -1, axis=0)
        elif np.all(img[:, 0] == 0):
            img = np.delete(img, 0, axis=1)
        elif np.all(img[:, -1] == 0):
            img = np.delete(img, -1, axis=1)
        else:
            break
    return img


def make_square_size(img):
    height, width, chanel = img.shape
    if height > width:
        add_size = height - width
        for i in range(add_size):
            if i % 2 == 0:
                img = np.insert(img, 0, 0, axis=1)
                width += 1
            else:
                img = np.insert(img, width, 0, axis=1)
                width += 1
    else:
        add_size = width - height
        for i in range(add_size):
            if i % 2 == 0:
                img = np.insert(img, 0, 0, axis=0)
                height += 1
            else:
                img = np.insert(img, height, 0, axis=0)
                height += 1
    return img


def image_normalization(image):
    image = make_fit_size(image)
    image = make_square_size(image)
    image = cv.resize(image, dsize=(150, 150), interpolation=cv.INTER_AREA)
    return image

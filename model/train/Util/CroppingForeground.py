# 배경을 잘라내고 전경과 약간의 배경 이미지만 남긴다.

from Utils import PositionManager
import cv2 as cv
import numpy as np
import glob


def ForegroundCrop(FilePath, ShowFlag = False):
    try:
        PositionManager.CalcPillPositionInfo(FilePath, ShowFlag)
        imgY = PositionManager.foreGroundImg.shape[0]
        imgX = PositionManager.foreGroundImg.shape[1]

        width = PositionManager.maxX - PositionManager.minX
        height = PositionManager.maxY - PositionManager.minY

        diffValue = abs(width - height)

        # 정사각형 배경 안에 전경 이미지 영역을 최대한 크게 한다.
        xOffset = 0
        yOffset = 0
        offsetValue = 5
        if width > height:
            xOffset = offsetValue
            yOffset = diffValue // 2 + offsetValue
        elif width < height:
            xOffset = diffValue // 2 + offsetValue
            yOffset = offsetValue
        else:
            xOffset = offsetValue
            yOffset = offsetValue

        initX = PositionManager.minX - xOffset
        if initX < 0:
            initX = 0

        maxX = PositionManager.maxX + xOffset

        if maxX > imgX:
            maxX = imgX

        initY = PositionManager.minY - yOffset

        if initY < 0:
            initY = 0

        maxY = PositionManager.maxY + yOffset
        if maxY > imgY:
            maxY = imgY

        xLength = maxX - initX
        yLength = maxY - initY
        diffXY = abs(xLength - yLength)
        if diffXY is 0:
            if xLength > yLength:
                maxY = maxY + diffXY
            else:
                maxX = maxX + diffXY

        if ShowFlag:
            print(initX, maxX, initY, maxY)
            print(imgX, imgY)

        img_gray = cv.cvtColor(PositionManager.foreGroundImg, cv.COLOR_BGR2GRAY)
    except Exception:
        img_gray = cv.imread(FilePath, cv.IMREAD_GRAYSCALE)

    return  img_gray, initX, maxX, initY, maxY


def ExcuteCroping(FilePath, ShowFlag = False, SaveFlag = False, Blur = True):
    errFlag = False

    img_gray, initX, maxX, initY, maxY = ForegroundCrop(FilePath, ShowFlag)

    clahe = cv.createCLAHE(clipLimit=10, tileGridSize=(5, 5))
    img_gray = clahe.apply(img_gray)
    if Blur:
        img_gray = cv.fastNlMeansDenoising(img_gray, None, 50, 7, 15)

    if ShowFlag:
        cv.imshow("img_gray", img_gray)
        cv.waitKey(0)

    #img_clahe = cv.resize(img_gray,(300,300))
    kernel = np.ones((14, 14), np.uint8)


    blackhat = cv.morphologyEx(img_gray, cv.MORPH_BLACKHAT, kernel)
    if ShowFlag:
        cv.imshow('blackhat1', blackhat)
        cv.waitKey(0)

    cv.drawContours(blackhat, PositionManager.contours, PositionManager.lastIdx, (0, 0, 0), 10)


    croppingImg = blackhat[initY:maxY, initX:maxX]
    #croppingImg = cv.resize(croppingImg, (75,75))

    if ShowFlag:
        cv.imshow("blackhat2", croppingImg)
        cv.waitKey(0)

    if SaveFlag:
        cv.imwrite(FilePath, croppingImg)

    return croppingImg


if __name__ == "__main__" :
    FlagOfExcuteKind = True

    DataParentPath = "E:\\"
    fileName = '20.jpg'
    #fileName = '20200319_111819.jpg'
    FilePath = DataParentPath + fileName

    if FlagOfExcuteKind:
        ExcuteCroping(FilePath, ShowFlag=True, SaveFlag = False, Blur=False)

    else :
        backUpFilePath = ""
        #TargetPath = 'E:\\Study\\Pill\\ForegroundTest\\FirstDis\\Class3\\Train'
        TargetPath = 'E:\\Study\\Pill\\ForegroundTest\\FirstDis\\Class1_2\\Train\\Class5_7'
       # FilePathList = glob.glob(path.join(TargetPath, '*.*'))
        FilePathList = glob.iglob(TargetPath + '/**/*.jpg', recursive=True)

        for each in FilePathList:
            print(each)
            ExcuteCroping(each, ShowFlag=False, SaveFlag=True, Blur=True)

'''
import cv2 as cv
import numpy as np

#img_gray = cv.imread('e:\\test.jpg', cv.IMREAD_GRAYSCALE)
img_gray = cv.imread('e:\\2.jpg', cv.IMREAD_GRAYSCALE)
img_gray = cv.resize(img_gray,(150,150))
cv.imshow('img_gray', img_gray)
cv.waitKey(0)

clahe = cv.createCLAHE(clipLimit=20, tileGridSize=(5, 5))
img_clahe = clahe.apply(img_gray)

cv.imshow('img_clahe', img_clahe)
cv.waitKey(0)

kernel = np.ones((7, 7), np.uint8)

tophat = cv.morphologyEx(img_clahe, cv.MORPH_TOPHAT, kernel)
cv.imshow('tophat', tophat)
cv.waitKey(0)

kernel2 = np.ones((13, 13), np.uint8)
blackhat = cv.morphologyEx(img_clahe, cv.MORPH_BLACKHAT, kernel)
cv.imshow('blackhat', blackhat)
cv.waitKey(0)
'''
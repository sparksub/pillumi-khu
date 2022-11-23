'''
기타 유틸 알고리즘
'''

import cv2 as cv
import shutil

from Utils import PositionManager
from Color import ColorManager, Configuration
import os.path as path
import glob

def PrintColorInfo():
    srcFolderPath = 'E:\\Study\\Pill\\ForegroundTest\\FirstDis\\Class0\\Test\\'
    FilePathList = glob.iglob(srcFolderPath + '/**/*.jpg', recursive=True)
    for each in FilePathList:
        print(each)
        img_color = cv.imread(each)
        pillColor, sumedLowRatioValue, colors = ColorManager.GetColorInfo(forgroundImg=img_color, kClustterValue=5,
                                                                          ShowFlag=False)
        print(pillColor)

def CopySameColors(filePath, srcFolderPath, ShowFlag = False):

    #img_color = cv.imread(filePath)
    PositionManager.CalcPillPositionInfo(filePath, False)
    pillColor, sumedLowRatioValue, colors = ColorManager.GetColorInfo(forgroundImg=None, kClustterValue=5, ShowFlag=ShowFlag)
    if ShowFlag:
        #cv.imshow('org', img_color)
        cv.imshow('c', PositionManager.foreGroundImg)
        cv.waitKey(0)
        print(pillColor)


    if Configuration.Color.Class0 == pillColor:
        dstFolderPath = srcFolderPath + 'Class0\\'
        dstPath = dstFolderPath + path.split(filePath)[1]
    elif Configuration.Color.Class1 == pillColor:
        dstFolderPath = srcFolderPath + 'Class1\\'
        dstPath = dstFolderPath + path.split(filePath)[1]
    elif Configuration.Color.Class2 == pillColor:
        dstFolderPath = srcFolderPath + 'Class2\\'
        dstPath = dstFolderPath + path.split(filePath)[1]
    elif Configuration.Color.Class3 == pillColor:
        dstFolderPath = srcFolderPath + 'Class3\\'
        dstPath = dstFolderPath + path.split(filePath)[1]
    elif Configuration.Color.Class4 == pillColor:
        dstFolderPath = srcFolderPath + 'Class4\\'
        dstPath = dstFolderPath + path.split(filePath)[1]
    elif Configuration.Color.Class5 == pillColor:
        dstFolderPath = srcFolderPath + 'Class5\\'
        dstPath = dstFolderPath + path.split(filePath)[1]
    elif Configuration.Color.Class6 == pillColor:
        dstFolderPath = srcFolderPath + 'Class6\\'
        dstPath = dstFolderPath + path.split(filePath)[1]
    elif Configuration.Color.Class7 == pillColor:
        dstFolderPath = srcFolderPath + 'Class7\\'
        dstPath = dstFolderPath + path.split(filePath)[1]

    if ShowFlag == False:
        shutil.move(filePath, dstPath)

def CopySameColorExcute():
    srcFolderPath = 'E:\\Study\\Pill\\ForegroundTest\\FirstDis\\Class3\\Test\\'
    # srcFolderPath = 'E:\\Study\\Pill\\Firstdis_images\\image\\Circle\\aaa'
    #dstFolderPath = srcFolderPath + 'Class0\\'
    FilePathList = glob.glob(path.join(srcFolderPath, '*.*'))
    for each in FilePathList:
        print(each)
        CopySameColors(each, srcFolderPath, False)

# 전후면 알약의 높이 위치가 같은것을 찾아 복사한다.
def MoveSamehightPositionPill():
    srcFolderPath = 'E:\\Study\\Pill\\Firstdis_images\\image\\Ellipse\\Re'

    dstFolderPath = 'E:\\Study\\Pill\\Firstdis_images\\image\\Ellipse\\mask\\'
    FilePathList = glob.glob(path.join(srcFolderPath, '*.*'))
    for each in FilePathList:
        print(each)
        grabedImg = cv.imread(each)
        contours, lasIdx = PositionManager.GetPillContour(grabedImg, 200, True)
        cy = []
        idx = 0
        for cnt in contours:
            area = cv.contourArea(cnt)
            print(area)

            M = cv.moments(cnt)
           # print(M['m01'])
          #  print(M['m00'])
           # cy.append(int(M['m01'] / M['m00']))
            idx = idx + 1
           #if idx == 2:
           #     break;
        '''
        print(len(cy))
        if abs(cy[0] - cy[1]) <= 5:
            print("same height!")
            fileName = path.split(each)[1]
            dst = dstFolderPath + fileName
           # shutil.move(each, dst)
        '''


import numpy as np
# 전체 이미지가 정사각형이 아닌 경우 정사각형으로 만들어 준다.
def MakeSquareCanvas():
    srcFolderPath = 'E:\\Study\\Pill\\ForegroundTest\\FirstDis\\Class1_2\\Front\\Class4'
    srcFolderPath = 'E:\\Study\\Pill\\ForegroundTest\\FirstDis\\Class1_2\\Train\\Class3\\552'
    #dstFolderPath = 'E:\\Study\\Pill\\Firstdis_images\\image\\Class3\\Front\\'
    FilePathList = glob.glob(path.join(srcFolderPath, '*.*'))

    for each in FilePathList:
        print(each)
        img =  cv.imread(each)
        if img.shape[0] != img.shape[1]:
            # 가로와 세로 길이의 차를 구한다.
            offset = abs(img.shape[1] - img.shape[0])

            if img.shape[0] > img.shape[1]:
                # 가로 길이는 동일하고 세로 길이의 차만큼의 배경 이미지를 만든다.
                offsetImg = np.zeros((img.shape[0],offset, 3), np.uint8)
                # 원본이미지와 더한다.
                addImg = cv.hconcat([img, offsetImg])
               # print(1)
            else :
                # 세로 길이는 동일하고 가로 길이의 차만큼의 배경 이미지를 만든다.
                offsetImg = np.zeros((offset, img.shape[1], 3), np.uint8)
                # 원본이미지와 더한다.
                addImg = cv.vconcat([img, offsetImg])
                #print(2)

            #cv.imshow('offsetImg', offsetImg)
            #cv.waitKey(0)

            #cv.imshow('add', addImg)
            #cv.waitKey(0)
            cv.imwrite(each, addImg)
            print("revised!!")

        fileName = path.split(each)[1]
        #dstPath = dstFolderPath + fileName
        #shutil.move(each, dstPath)


# 캡슐타입 알약의 색상을 구분하기 위한 함수
# 완벽히 분리가 안되서 미완성임
def CheckHalfColorInCapsuleType(ShowFlag = False):
    srcFolderPath = 'E:\\Study\\Pill\\Firstdis_images\\image\\Class3\\1\\'
    #srcFolderPath = 'E:\\Study\\Pill\\TestData\\Capsule'
   # srcFolderPath = 'E:\\Study\\Pill\\Firstdis_images\\image\\Class3\\test\\'
    FilePathList = glob.glob(path.join(srcFolderPath, '*.*'))
    for each in FilePathList:
        print(each)
        PositionManager.CalcPillPositionInfo(each, False)
        img_color = PositionManager.foreGroundImg

        offsetXPos = (PositionManager.maxX - PositionManager.minX) // 15
        offsetYPos = (PositionManager.maxY - PositionManager.minY) // 15
        initY = PositionManager.minY + offsetYPos
        initX = PositionManager.minX + offsetXPos
        lastY = PositionManager.maxY - offsetYPos
        lastX = PositionManager.maxX - offsetXPos

        cropedImgTmp = img_color[initY:lastY, initX:lastX]

        if ShowFlag:
            cv.imshow("ss", cropedImgTmp)
            cv.waitKey(0)

        clustterVlaue = 5
        pillColor, sumedLowRatioValue, colors = ColorManager.GetColorInfo(forgroundImg=cropedImgTmp, kClustterValue=clustterVlaue,
                                                                          ShowFlag=ShowFlag)
        hueList = []
        saturationList = []
        valueList = []
        percentList = []
        
        # 캡슐의 좌우 색이 같으면 0, 다르면 1
        typeOfCapsule = 0
        if len(colors) == clustterVlaue:
            for idx, value in enumerate(colors):
                # print(idx)
                percent, color = value
                # 가장 작은 비율을 제외하고 hue, sat, value를 저장한다.
                percent = percent * 100
                #print(percent)

                hueList.append(value[1][0])
                saturationList.append(value[1][1])
                valueList.append(value[1][2])
                percentList.append(percent)

            # 각각의 차이를 구한다.
            hueDiff = abs(hueList[clustterVlaue - 1] - hueList[clustterVlaue - 2])
            satDiff = abs(saturationList[clustterVlaue - 1] - saturationList[clustterVlaue - 2])
            valDiff = abs(valueList[clustterVlaue - 1] - valueList[clustterVlaue - 2])
            percentDiff = abs(percentList[clustterVlaue - 1] - percentList[clustterVlaue - 2])

            '''
            if hueDiff > 50 or satDiff > 50 or valDiff > 50:
                # 가장 큰 비중과 두번째 큰 비중의 차가 30%를 안넘는 다면
                if percentDiff < 30:
                    typeOfCapsule = 1
            '''
            if hueDiff > 10 and hueDiff < 170:
                typeOfCapsule = 1
            elif hueDiff < 2 :
                typeOfCapsule = 0
            elif satDiff > 55 or valDiff > 60:
                typeOfCapsule = 1

            if ShowFlag :
                print(hueDiff, satDiff, valDiff, percentDiff)
                print(typeOfCapsule)

        fileName = path.split(each)[1]

        if ShowFlag == False:
            if typeOfCapsule == 1:
                dstFolderPath = 'E:\\Study\\Pill\\Firstdis_images\\image\\Class3\\1\\'
                dstPath = dstFolderPath + fileName
               # shutil.move(each, dstPath)
            else :
                dstFolderPath = 'E:\\Study\\Pill\\Firstdis_images\\image\\Class3\\2_1\\'
                dstPath = dstFolderPath + fileName
                shutil.move(each, dstPath)

# 이미지 세로 영역 일부를 검은색으로 마스킹 한다.
# 전경 이미지가 이미지 끝에 붙어서 전경추출이 잘 안되는 것 방지
def MakeMaskingSomeColomn():
    srcFolderPath = 'E:\\Study\\Pill\\ForegroundTest\\FirstDis\\Class1_2\\Front\\Class4'
    FilePathList = glob.glob(path.join(srcFolderPath, '*.*'))
    for each in FilePathList:
        print(each)
        img = cv.imread(each)
        #0,0 위치에서 가로 영역 2픽셀만큼의 세로로 긴 사각형을 그린다.
        cv.rectangle(img, (0, 0), (2, img.shape[0]), (0, 0, 0), -1)
        #cv.imshow('dd', img)
        #cv.waitKey(0)
        cv.imwrite(each, img)

def ResizeImg():
    srcFolderPath = 'E:\\Study\\Pill\\SegTest\\Data\\firstDis2\\org'
    FilePathList = glob.glob(path.join(srcFolderPath, '*.*'))
    i = 0
    for each in FilePathList:
        print(each)
        stream = open(each.encode("utf-8"), "rb")
        bytes = bytearray(stream.read())
        numpyArray = np.asarray(bytes, dtype=np.uint8)
        img =  cv.imdecode(numpyArray, cv.IMREAD_UNCHANGED)
        print(img.shape[1], img.shape[0])
        img = cv.resize(img, (300,300))
        print(img.shape[1], img.shape[0])
        #cv.imshow('aaa', img)
       # cv.waitKey(0)
        folerPath = 'E:\\Study\\Pill\\SegTest\\Data\\firstDis2\\org2\\'
        filePath = folerPath + str(i) +'.jpg'
        print(filePath)
        cv.imwrite(filePath, img)
        i = i + 1

#기존 알고리즘을 이용하여 배경 제거를 시도한다.
def DeleteBackground():
    srcFolderPath = 'E:\\Study\\Pill\\SegTest\\Data\\firstDis2\\grab'
    FilePathList = glob.glob(path.join(srcFolderPath, '*.*'))
    i = 0
    for each in FilePathList:
        print(each)
        PositionManager.CalcPillPositionInfo(each)
        img =  PositionManager.foreGroundImg
        dstFolder = 'E:\\Study\\Pill\\SegTest\\Data\\firstDis2\\maskSuccess\\'
        fileName = path.split(each)[1]
        dstPath = dstFolder + fileName
        cv.imwrite(each, img)
        shutil.move(each, dstPath)

#특정 데이터를 삭제한다.
import os
def DeleteMaskFileTmp():
    srcFolderPath = 'E:\\Study\\Pill\\SegTest\\Data\\firstDis2\\Mask\\'
    FilePathList = glob.glob(path.join(srcFolderPath, '*.*'))
    i = 0
    for i in range(0,271):
        dstPath = srcFolderPath + str(i) + ".png"
        print(dstPath)
        os.remove(dstPath)

# Mask Data가 올바르게 만들어 졌는지 확인 용도
# Data가 0,1로만 구성되어 있어서 눈으로 확인이 불가 하므로
# *255를 해줘서 확인 함.
def CheckMaskData():
    file = 'E:\\0_0_4211.png'
    img = cv.imread(file)
    print(img)
    cv.imshow('1', img)
    img = img * 255
    cv.imshow('2', img)
    cv.waitKey(0)

def MakeGrayScaleImg():
    srcFolderPath = 'E:\\Study\\Pill\\Shape\\GrayScale'
    FilePathList =  glob.iglob(srcFolderPath + '/**/*.jpg', recursive=True)
    for each in FilePathList:
        print(each)
        img = cv.imread(each, cv.IMREAD_GRAYSCALE)
        cv.imwrite(each, img)

'''
알약이 위나 아래로 치우쳐 있을때 가운데로 만들어 준다
'''
def ModifyThePosition():
    srcFolderPath = 'E:\\Study\\Pill\\ForegroundTest\\FirstDis\\Class1_2\\Front\\Class4'
    srcFolderPath = 'E:\\Study\\Pill\\ForegroundTest\\FirstDis\\Class1_2\\Train\\Class3\\552'
    #FilePathList = glob.iglob(srcFolderPath + '/**/*.jpg', recursive=True)
    FilePathList = glob.glob(path.join(srcFolderPath, '*.*'))
    for each in FilePathList:
        #each = "E:\\P0000000026269.jpg"
        print(each)
        PositionManager.CalcPillPositionInfo(each)
        imgY = PositionManager.foreGroundImg.shape[0]
        imgX = PositionManager.foreGroundImg.shape[1]

        print(imgY, PositionManager.cy)
        halfY = imgY //2
        posDiff = abs(halfY - PositionManager.cy)
        print(posDiff)
        modifyFlag = False
        # 아래 //는 알약의 모양을 보면서 조절해야 함.
        if posDiff > (halfY // 5) :
            modifyFlag = True
            print(modifyFlag)

        if modifyFlag:
            width = PositionManager.maxX - PositionManager.minX
            height = PositionManager.maxY - PositionManager.minY

            diffValue = abs(width - height)
            img = PositionManager.foreGroundImg;

            img = img[PositionManager.minX:PositionManager.maxY, :]#PositionManager.minX:PositionManager.maxX]
            #cv.imshow('aa', img)
            #cv.waitKey(0)

            offset = diffValue // 2
            offsetImg = np.zeros((offset, img.shape[1], 3), np.uint8)

            addImg = cv.vconcat([img, offsetImg])
            #cv.imshow('addImg', addImg)
            #cv.waitKey(0)
            addImg = cv.vconcat([offsetImg, addImg])
            #cv.imshow('addImg', addImg)
            #cv.waitKey(0)
            cv.imwrite(each, addImg)

#PrintColorInfo()
#ModifyThePosition()
#DeleteMaskFileTmp()
CopySameColorExcute()
#MoveSamehightPositionPill()
#MoveSameShape()
#MakeSquareCanvas()
#CheckHalfColorInCapsuleType(False)
#MakeMaskingSomeColomn()
#ResizeImg()
#DeleteBackground()
#MakeGrayScaleImg()






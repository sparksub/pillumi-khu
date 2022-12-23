from Color import Configuration
from sklearn.cluster import KMeans
import cv2 as cv
from Utils import PositionManager
import numpy as np


def GetColorHist(img, kClustterValue=2):
    hsvImg = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    reshape = hsvImg.reshape((hsvImg.shape[0] * hsvImg.shape[1]), 3)

    # Find and display most dominant colors
    cluster = KMeans(n_clusters=kClustterValue).fit(reshape)

    # Get the number of different clusters, create histogram, and normalize
    labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
    (hist, _) = np.histogram(cluster.labels_, bins=labels)
    hist = hist.astype("float")
    hist /= hist.sum()

    # Create frequency rect and iterate through each cluster's color and percentage
    rect = np.zeros((50, 300, 3), dtype=np.uint8)
    colors = sorted([(percent, color) for (percent, color) in zip(hist, cluster.cluster_centers_)])

    return colors, rect


def GetColorInfo(forgroundImg=None, kClustterValue=None, ShowFlag=False):
    global  pillColor
    if forgroundImg is None:
        forgroundImg = PositionManager.foreGroundImg

    if kClustterValue is None:
        kClustterValue = Configuration.KClustterValue

    pillColor = Configuration.Color.ETC

    try:
        colors, rect = GetColorHist(forgroundImg, kClustterValue)
    except Exception:
        colors, rect = GetColorHist(forgroundImg, 2)
    start = 0

    lowRatioValueColor = 0.0

    numberOfColors =  len(colors)
    for idx, value in enumerate(colors):
        #print(idx)
        percent, color = value

        # 하위 두개의 색 비율의 합을 구한다.
        if idx <= kClustterValue / 3:
            lowRatioValueColor += percent

        if ShowFlag :
            print(color, "{:0.2f}%".format(percent * 100))

        end = start + (percent * 300)
        cv.rectangle(rect, (int(start), 0), (int(end), 50),
                     color.astype("uint8").tolist(), -1)
        start = end

        # 2번째로 큰 비율의 색을 알약이 색이라 간주
        if idx == (numberOfColors - 2):
            pillColor = Configuration.GetColor(color)

        # 첫번째로 큰 비율의 색이 검정색이 아니라면 첫번째
        # 큰 비주의 색을 알약의 색이라 간주
        if idx == (numberOfColors - 1):
            # value가 일정값 이상
            if value[1][2] > 5.0:
                pillColor = Configuration.GetColor(color)

    visualizeData = cv.cvtColor(rect, cv.COLOR_HSV2BGR)
    lowRatioValueColor = lowRatioValueColor * 100.0

    if ShowFlag:
        cv.imshow('color', visualizeData)
        cv.waitKey(0)

    return pillColor, lowRatioValueColor, colors


def AnalizeType(colors, cropedImg):
    minH = 255
    maxH = 0
    minS = 255
    maxS = 0
    minV = 255
    maxV = 0
    for idx, value in enumerate(colors):
        percent, color = value
        currentHue = value[1][0]
        currentSaturation = value[1][1]
        currentValue = value[1][2]
        # hue 값 분석
        if currentHue > maxH:
            maxH = currentHue

        if currentHue < minH:
            minH = currentHue

        if currentSaturation > maxS:
            maxS = currentSaturation

        if currentSaturation < minS:
            minS = currentSaturation

        if currentValue > maxV:
            maxV = currentValue

        if currentValue < minV:
            minV = currentValue

    # print(minH, maxH)
    # print(minS, maxS)
    # print(minV, maxV)
    pillType = 1

    if (maxH - minH) < 40:
        if (maxS - minS < 60):
            if (maxV - minV < 100):
                pillType = 0
        elif (maxV - minV < 60):
            if (maxV - minV < 100):
                pillType = 0
    else:
        hueGap = 180 - (maxH - minH)
        if hueGap < 60:
            if (maxV - minV < 60) and (maxS - minS < 60):
                pillType = 0

    return pillType


def TestType(file_path, save=False):
    PositionManager.CalcPillPositionInfo(file_path, False)
    img_color = PositionManager.foreGroundImg

    initY = PositionManager.minY + (PositionManager.cy - PositionManager.minY) // 2
    initX = PositionManager.minX + (PositionManager.cx - PositionManager.minX) // 2
    lastY = PositionManager.cy + (PositionManager.maxY - PositionManager.cy) // 2
    lastX = PositionManager.cx + (PositionManager.maxX - PositionManager.cx) // 2
    # print(initY, initX, lastY, lastX)
    cropedImgTmp = img_color[initY:lastY, initX:lastX]

    pillColor, sumedLowRatioValue, colors = GetColorInfo(forgroundImg=cropedImgTmp, kClustterValue=3, ShowFlag=False)
    AnalizeType(colors, cropedImgTmp)

    if save:
        img = cv.imread(file_path)
        cv.imwrite(str(pillColor.value) +'/' + file_path[-9:], img)

    return pillColor.value

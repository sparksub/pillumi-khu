from api.pill_model.model.classification import Configuration
from sklearn.cluster import KMeans
import cv2 as cv
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
    pillColor = Configuration.Color.ETC

    try:
        colors, rect = GetColorHist(forgroundImg, kClustterValue)
    except Exception:
        colors, rect = GetColorHist(forgroundImg, 2)
    start = 0

    lowRatioValueColor = 0.0

    numberOfColors =  len(colors)
    for idx, value in enumerate(colors):
        percent, color = value

        # 하위 두개의 색 비율의 합을 구한다.
        if idx <= kClustterValue / 3:
            lowRatioValueColor += percent

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

    return pillColor

def TestType(image, save=False):
    pillColor = GetColorInfo(forgroundImg=image, kClustterValue=3, ShowFlag=False)
    
    return pillColor.value

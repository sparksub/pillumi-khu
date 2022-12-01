import enum

class Color(enum.Enum):
    Class0 = 0
    Class1 = 1
    Class2 = 2
    Class3 = 3
    Class4 = 4
    Class5 = 5
    Class6 = 6
    Class7 = 7
    ETC = 99


def GetColor(hsvInfo):
    hue = hsvInfo[0]
    saturation = hsvInfo[1]
    value = hsvInfo[2]

    retValue = Color.ETC

    if saturation < 20 and value > 150:
        retValue = Color.Class0
    elif value < 70:
        retValue = Color.Class1
    elif hue < 10 or hue > 160:
        retValue = Color.Class2
    elif hue <= 40:
        retValue = Color.Class3
    elif hue <= 70:
        retValue = Color.Class4
    elif hue <= 100:
        retValue = Color.Class5
    elif hue <= 130:
        retValue = Color.Class6
    elif hue <= 160:
        retValue = Color.Class7
   
    return retValue

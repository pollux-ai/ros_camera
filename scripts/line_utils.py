
##from https://github.com/JinFree
##from https://github.com/NamWoo

import cv2
import numpy as np
import math

def cal_angle(x1, y1, x2, y2):
    ang1 = np.arctan2(*(x1, y1)[::-1])
    ang2 = np.arctan2(*(x2, y2)[::-1])
    res = np.rad2deg((ang1 - ang2) % (2 * np.pi))
    return res

def cal_angle2(x1, y1, x2, y2):
    rad = math.atan2(y2-y1, x2-x1)
    deg = (rad*180)/math.pi
    return deg

def imageCopy(src):
    return np.copy(src)

def drawLine(image, point1, point2, color=(255, 0, 0), thickness=3, lineType=cv2.LINE_AA):
    result = imageCopy(image)
    return cv2.line(result, point1, point2, color, thickness, lineType)

def drawCircle(image, center, radius, color=(255, 0, 0), thickness=3, lineType=cv2.LINE_AA):
    result = imageCopy(image)
    return cv2.circle(result, center, radius, color, thickness, lineType)

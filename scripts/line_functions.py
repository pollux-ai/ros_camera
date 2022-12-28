
import cv2
import numpy as np
from line_utils import *

h_l = 0
s_l = 100
v_l = 120
h_u = 25
s_u = 255
v_u = 160

lower = np.array([h_l, s_l, v_l])
upper = np.array([h_u, s_u, v_u])

def line_dectecting(cv_image):
    
    cv_image = convertColor(cv_image, cv2.COLOR_BGR2HSV)
    cv_image = splitColor(cv_image, lower, upper)
    cv_image = convertColor(cv_image, cv2.COLOR_HSV2BGR)
    
    cv_image = cannyEdge(cv_image, 100, 200)
    
    lines = houghLinesP(cv_image, 1, np.pi/180, 100, 10, 50)
    cv_image = drawHoughLinesP(cv_image, lines)


    return cv_image
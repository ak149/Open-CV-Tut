# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:39:43 2020

@author: Aditya
"""

import cv2
import numpy as np

def emptyFuntion():
    pass


img = np.zeros((512,512,3),dtype = np.uint8)
cv2.namedWindow("BGR Color Palette")

cv2.createTrackbar("B" , "BGR Color Palette" , 0, 255 , emptyFuntion)
cv2.createTrackbar("G" , "BGR Color Palette" , 0, 255 , emptyFuntion)
cv2.createTrackbar("R" , "BGR Color Palette" , 0, 255 , emptyFuntion)

while(True):
    cv2.imshow("BGR Color Palette",img)
    if cv2.waitKey(1) == 27:
        break
    
    blue = cv2.getTrackbarPos("B" , "BGR Color Palette")
    green = cv2.getTrackbarPos("G" , "BGR Color Palette")
    red = cv2.getTrackbarPos("R" , "BGR Color Palette")
    
    img[:] = [blue,green,red]
    print(blue,green,red)

cv2.destroyAllWindows()

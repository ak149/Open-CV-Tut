# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 14:20:35 2020

@author: Aditya
"""


import cv2
import numpy as np

img_path = "D:\\CODING\\Open CV\\standard_test_images\\lena_color_256.tif"

#img = cv2.imread(img_path)

img = np.zeros((512,512,3),np.uint8)
cv2.line(img , (100,0) , (0,100) ,(255,255,255) , 2)
cv2.rectangle(img , (40,60) , (80,70) , (0,255,0) , 1)
cv2.circle(img , (360,360) , 20 , (0,0,255) , -1)
cv2.ellipse(img,(200,400) , (50,30) ,0 , 0, 360, (0,125,254) ,-1)

cv2.imshow("lena",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
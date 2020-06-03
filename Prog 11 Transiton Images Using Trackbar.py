# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:39:55 2020

@author: Aditya
"""


import cv2
import matplotlib.pyplot as plt
import numpy as np


def empty_function(self):
    pass


base_path = "D:\\CODING\\Open CV\\misc\\"
img1 = cv2.imread(base_path + "4.2.01.tiff")
img2 = cv2.imread(base_path + "4.2.03.tiff")

# =============================================================================
# plt.subplot(1,2,1)
# plt.imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
# plt.subplot(1,2,2)
# plt.imshow(cv2.cvtColor(img2,cv2.COLOR_BGR2RGB))
# 
# =============================================================================

window_name = "Transition Using Trackbar"
cv2.namedWindow(window_name)

output = cv2.addWeighted(img1,0,img2,1,0)
#cv2.imshow(window_name,output)

cv2.createTrackbar("Alpha" , window_name,0,10,empty_function)

while True:
    
    cv2.imshow(window_name,output)
    
    if cv2.waitKey(1) == 27:
        break
    alpha = cv2.getTrackbarPos("Alpha",window_name)/10
    output = cv2.addWeighted(img1,alpha,img2,1 - alpha,0)
    
    
    
    
cv2.destroyAllWindows()
    






# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 18:57:49 2020

@author: Aditya
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

img1 = cv2.imread("D:\\CODING\\Open CV\\misc\\4.2.01.tiff")
img2 = cv2.imread("D:\\CODING\\Open CV\\misc\\4.2.03.tiff")


alpha = 0.5
beta = 0.5
gamma = 0

blended = cv2.addWeighted(img1,alpha,img2,beta,gamma)

plt.imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
plt.imshow(cv2.cvtColor(img2,cv2.COLOR_BGR2RGB))
plt.imshow(cv2.cvtColor(blended,cv2.COLOR_BGR2RGB))

alpha1 = 0
beta1 = 1

for i in np.linspace(0,1,50):
    alpha1 = i
    beta1 = 1 - alpha1
    
    transitioned = cv2.addWeighted(img1,alpha1,img2,beta1,0)
    
    cv2.imshow("Transition Image",transitioned)
    time.sleep(0.1)
    
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()

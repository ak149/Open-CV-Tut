# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:56:37 2020

@author: Aditya
"""


import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:\\CODING\\Open CV\\misc\\7.1.06.tiff",0)


th = 0
max_val = 255

ret,output = cv2.threshold(img,th,max_val,cv2.THRESH_TRUNC + cv2.THRESH_OTSU) 


plt.subplot(1,2,1)
plt.imshow(img,cmap = "gray")

plt.subplot(1,2,2)
plt.imshow(output,cmap = "gray")

plt.show()
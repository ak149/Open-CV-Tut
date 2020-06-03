# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:18:16 2020

@author: Aditya
"""


import cv2
import matplotlib.pyplot as plt
import numpy as np



img = cv2.imread("D:\\CODING\\Open CV\\misc\\4.2.01.tiff")

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


rows,columns,channels = img.shape

R = cv2.getRotationMatrix2D((columns/2,rows/2),45,0.7)

output = cv2.warpAffine(img,R,(columns,rows))

plt.subplot(1,2,1)
plt.imshow(img)

plt.subplot(1,2,2)
plt.imshow(output)



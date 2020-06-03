# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:15:22 2020

@author: Aditya
"""


import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:\\CODING\\Open CV\\misc\\5.1.09.tiff",0)

block_size = 201
constant = 40

th1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,block_size,constant)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,block_size,constant)


plt.subplot(1,3,1)
plt.imshow(img,cmap = "gray")
plt.subplot(1,3,2)
plt.imshow(th1,cmap = "gray")
plt.subplot(1,3,3)
plt.imshow(th2,cmap = "gray")


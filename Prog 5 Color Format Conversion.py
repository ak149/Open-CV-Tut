# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 00:33:28 2020

@author: Aditya
"""


import cv2
import matplotlib.pyplot as plt

imgpath = "D:\CODING\Open CV\standard_test_images\lena_color_256.tif"

img = cv2.imread(imgpath , 1)

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


plt.imshow(img)
plt.show()



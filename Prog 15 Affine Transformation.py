# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 12:07:50 2020

@author: Aditya
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("D:\\CODING\\Open CV\\misc\\4.2.01.tiff")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

rows,columns,channels = img.shape

point1 = np.float32([[100,200],[50,100],[50,300]])
point2 = np.float32([[200,100],[50,60],[100,200]])

a = cv2.getAffineTransform(point1,point2)

print(a)

output = cv2.warpAffine(img,a,(columns,rows))

print(output)
plt.imshow(output)

cv2.destroyAllWindows()
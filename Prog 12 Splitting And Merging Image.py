# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:43:57 2020

@author: Aditya
"""


import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:\\CODING\\Open CV\\misc\\4.2.01.tiff",1)

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

r,g,b = cv2.split(img)

Title = ["Original Image","Red","Green","Blue"]

images = [cv2.merge((r,g,b)),r,g,b]
colormaps = [plt.cm.bone,plt.cm.Reds,plt.cm.Greens,plt.cm.Blues]
fig = plt.figure(figsize = (2,2))
for i in range(len(images)):
    ax = fig.add_subplot(2,2,i+1)
    plt.title(Title[i])
    plt.xticks([])
    plt.yticks([])
    ax.imshow(images[i],cmap = colormaps[i] )
    
plt.show()
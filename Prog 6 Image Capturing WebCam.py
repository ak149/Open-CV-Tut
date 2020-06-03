# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 02:55:07 2020

@author: Aditya
"""


import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret,frame = cap.read()
    print(ret,frame)
    
else:
    ret = False
    
    
cap.release()
img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
plt.imshow(img)
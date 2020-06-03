# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:02:03 2020

@author: Aditya
"""


import cv2
import matplotlib.pyplot as plt
import numpy as np

window_name = "ObjectTracking"
#cv2.namedWindow(window_name)

cap = cv2.VideoCapture(0)
 
if cap.isOpened():
    ret,frame = cap.read()
else:
    ret = False
    
while ret:
    ret,frame = cap.read()
    
    hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    low = np.array([100,50,50])
    high = np.array([140,255,255])
    
    image_mask = cv2.inRange(hsv_img , low , high)
    output = cv2.bitwise_and(frame , frame , mask  = image_mask)
    
    cv2.imshow("Image_mask" , image_mask)
    cv2.imshow("Original Feed" , frame)
    cv2.imshow("AND Feed" , output)
    
    
    
    
    
    if cv2.waitKey(1) == 27:
        break
    
    
    
cv2.destroyAllWindows()
cap.release()

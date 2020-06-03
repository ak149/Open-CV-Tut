# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:07:22 2020

@author: Aditya
"""

import cv2
import numpy as np

window_name = "Drawing"
img = np.zeros((512,512,3),dtype = np.uint8)
cv2.namedWindow(window_name)

#true if mouse pressed
drawing= False

#if true,draw rectangle. press m to toggle to curve
mode = True
(ix,iy) = (-1, -1)

def draw_shape(event, x , y , flags , params):
    global ix,iy,drawing,mode
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if drawing == True:
            if mode == True:
                cv2.rectangle()
            else:
                cv2.circle()
                
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle()
            else:
                cv2.circle()
                
    


# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:42:02 2020

@author: Aditya
"""

import cv2 
import numpy as np

window_name = "Drawing"
img = np.zeros((512,512,3),dtype = np.uint8)
cv2.namedWindow(window_name)

def action(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y) , 30 , (147,142,0), -1)
    
cv2.setMouseCallback(window_name , action)
   
while(True):
    
    cv2.imshow(window_name,img)    
    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()




    
    
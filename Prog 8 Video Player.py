# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:47:38 2020

@author: Aditya
"""


import cv2

window_name = "PlaybackVideoFile"
cv2.namedWindow(window_name)


filename = "D:\CODING\Open CV\VideoCapture\output.avi"
cap = cv2.VideoCapture(filename)


while cap.isOpened():
    ret,frame = cap.read()
        
    if ret:
        cv2.imshow(window_name , frame)
        if cv2.waitKey(60) == 27:
            break
    else:
        break
        
    
cap.release()
cv2.destroyAllWindows()

        
        
    
    






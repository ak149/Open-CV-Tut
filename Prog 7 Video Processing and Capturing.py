# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 03:08:53 2020

@author: Aditya
"""


import cv2

cap = cv2.VideoCapture(0)
window_name = "LiveVideoCapture"
cv2.namedWindow(window_name)


filename = "D:\CODING\Open CV\VideoCapture\output.avi"
codec = cv2.VideoWriter_fourcc('X' , 'V' , 'I' , 'D')
framerate = 30
resolution = (640,480)

VideoFileOutput = cv2.VideoWriter(filename , codec , framerate , resolution)

 
# =============================================================================
# print("Height : ",cap.get(4) )
# print("width : ", cap.get(3))
# 
# cap.set(3,1600)
# cap.set(4 , 900)
# 
# print("Height : ",cap.get(4) )
# print("width : ", cap.get(3))
# =============================================================================

if cap.isOpened():
    ret,frame = cap.read()
    
else:
    ret = False
    

while ret:
    ret,frame = cap.read()
    
    VideoFileOutput.write(frame)
    #output = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow(window_name,frame)
    if cv2.waitKey(1)  == 27:
        break

VideoFileOutput.release()
cv2.destroyAllWindows()
cap.release()



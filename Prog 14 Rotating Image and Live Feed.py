# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import cv2
import time

#img = cv2.imread("D:\\CODING\\Open CV\\misc\\4.2.06.tiff",1)


cap = cv2.VideoCapture(0)



angle = 0

while True:
    
    if angle == 360:
        angle = 0
    
    
    ret,frame = cap.read()
    
    rows,columns,channels = frame.shape        
    R = cv2.getRotationMatrix2D((columns/2,rows/2),angle,0.7)
    
    output = cv2.warpAffine(frame,R,(columns,rows))
    
    cv2.imshow("Rotating Image",output)
    
    angle += 1
    time.sleep(0.01)
    
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

    
    



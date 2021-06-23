# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 23:29:22 2021

@author: Ahmet
"""


import cv2
import numpy as np

frameWidth=640
frameHeight=480


cap=cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)



def empty(a):
    pass    #The pass statement is used to assign a null value.

cv2.namedWindow("HSV_") 
cv2.resizeWindow("HSV_", 640,280)

#create trackbars
cv2.createTrackbar("H Min","HSV_",0,179,empty)
cv2.createTrackbar("H Max","HSV_",179,179,empty)
cv2.createTrackbar("S Min","HSV_",0,255,empty)
cv2.createTrackbar("S Max","HSV_",255,255,empty)
cv2.createTrackbar("V Min","HSV_",0,255,empty)
cv2.createTrackbar("V Max","HSV_",255,255,empty)

while True:
    
    _,img=cap.read()
    
    img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #HSV SPACE
    
    # Get values from trackbars
    h_min=cv2.getTrackbarPos("H Min","HSV_")
    h_max=cv2.getTrackbarPos("H Max","HSV_")
    s_min=cv2.getTrackbarPos("S Min","HSV_")
    s_max=cv2.getTrackbarPos("S Max","HSV_")
    v_min=cv2.getTrackbarPos("V Min","HSV_")
    v_max=cv2.getTrackbarPos("V Max","HSV_")
    
    
    #mask
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(img_HSV,lower,upper)
    result=cv2.bitwise_and(img,img,mask=mask)
    
    img_stack=np.hstack([img,cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR),result])
    
    cv2.imshow("IMG",img_stack)
  
    if cv2.waitKey(1) & 0xFF==ord('x'):
        break

cap.release()
cv2.destroyAllWindows()



















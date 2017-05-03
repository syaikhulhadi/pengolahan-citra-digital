import numpy as np
import cv2 

cap=cv2.VideoCapture(0)
print(cap.isOpened())

while(True):
    ret, frame = cap.read()
    abu=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('webcam', 255-abu)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
cap.realease()
cv2.destroyAllwindows()


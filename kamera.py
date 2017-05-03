import numpy as np
import cv2 
cap=cv2.VideoCapture(0)
print(cap.isOpened()) 
while(True):
    ret, frame = cap.read()
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 
cap.realease()
cv2.destroyAllwindows()
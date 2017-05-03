import numpy as np
import cv2 
cap=cv2.VideoCapture(0)
print(cap.isOpened())
while(True):
    ret, frame = cap.read()
    bright = cv2.addWeighted(frame,1.5,np.zeros(frame.shape,frame.dtype),0, 25)
    cv2.imshow('webcam', bright)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
cap.realease()
cv2.destroyAllwindows()


import cv2
import numpy as np
cap = cv2.VideoCapture("C:/Users/Hema vershini/OneDrive/Desktop/WhatsApp Video 2023-11-18 at 12.49.24_23ae88c7.mp4")
if (cap.isOpened()== False):
    print("Error opening video file")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(250) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

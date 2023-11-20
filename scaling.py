import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("C:/Users/Hema vershini/OneDrive/Desktop/70.jpg",cv2.IMREAD_COLOR)
img = cv2.resize(img,(800,800))
cv2.imshow("image",img)
cv2.waitKey(0)

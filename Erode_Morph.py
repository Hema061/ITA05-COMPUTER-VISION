import cv2
import numpy as np
img = cv2.imread("C:/Users/Hema vershini/OneDrive/Pictures/Downloads/845ef870ae51686ea252043334f8325b.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
cv2.imshow("Original", img)
cv2.imshow("Eroded", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()

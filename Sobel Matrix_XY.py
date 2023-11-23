import cv2
img = cv2.imread("C:/Users/Hema vershini/OneDrive/Pictures/Downloads/845ef870ae51686ea252043334f8325b.jpg") 
# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y 
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.waitKey(0)

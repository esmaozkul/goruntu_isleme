import cv2
import numpy as np

image =cv2.imread('lenna.png')
cv2.imshow("orginal",image)

b,g,r=cv2.split(image)
cv2.imshow("blue",b)

cv2.imshow("green",g)

cv2.imshow("red",r)

cv2.waitKey(0)

# ret,thresh1=cv2.threshold(coins_gray_image,87,255,cv2.THRESH_BINARY)
# cv2.imshow("Threshold_image",thresh1)
# cv2.waitKey(0)
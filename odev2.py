import cv2
import numpy as np

# 225x225 boyutundaki Lena görüntüsünü oku
lenna_img = cv2.imread("lenna.jpg")

# Lena görüntüsünün boyutunu 255x510x3'e dönüştür
new_img = cv2.resize(lenna_img, (510, 255))

# Yeni görüntüyü kaydet
cv2.imwrite("lenna_resized.jpg", new_img)


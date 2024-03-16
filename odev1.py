import numpy as np
import cv2

# Görüntü boyutlarını belirleme
height = 200
width = 200

# Siyah bir görüntü oluşturma
black_image = np.zeros((height//2, width//2), dtype=np.uint8)

# Beyaz bir görüntü oluşturma
white_image = 255 * np.ones((height//2, width//2), dtype=np.uint8)

# Dört parçadan oluşan birleştirilmiş görüntü oluşturma
top_left = np.zeros((height//2, width//2), dtype=np.uint8)
top_right = np.zeros((height//2, width//2), dtype=np.uint8)
bottom_left = np.zeros((height//2, width//2), dtype=np.uint8)
bottom_right = np.zeros((height//2, width//2), dtype=np.uint8)

# Sol üst bölgenin renk geçişini oluşturma
for i in range(height//2):
    for j in range(width//2):
        top_left[i, j] = int(255 * ((width//2 - j) / (width//2)))

# Sağ üst bölgenin renk geçişini oluşturma
for i in range(height//2):
    for j in range(width//2):
        top_right[i, j] = int(255 * ((width//2 - j) / (width//2)))

# Sol alt bölgenin renk geçişini oluşturma
for i in range(height//2):
    for j in range(width//2):
        bottom_left[i, j] = int(255 * ((height//2 - i) / (height//2)))

# Sağ alt bölgenin renk geçişini oluşturma
for i in range(height//2):
    for j in range(width//2):
        bottom_right[i, j] = int(255 * ((height//2 - i) / (height//2)))

# Görüntü parçalarını birleştirme
final_image_top = np.hstack((top_left, top_right))
final_image_bottom = np.hstack((bottom_left, bottom_right))
final_image = np.vstack((final_image_top, final_image_bottom))

# Sonuç görüntüsünü ekranda gösterme
cv2.imshow('Sonuç Görüntüsü', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

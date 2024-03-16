import cv2
import numpy as np

#resim acma
resim=cv2.imread("peppers.png",0)
#resmi gri yapar
# resim=cv2.imread("peppers.png",0)
#resimi göstermek için immshow fonksiyonun kullanılır
cv2.imshow("peppers",resim)

# number_of_piksels=np.zeros(255,np.)


#ekstra siyah beyazını da kaydetmek istersek
cv2.imwrite("peppersyeni.png",resim)

#kapatmak için pencerenin tuşa basmamızı sağlar
cv2.waitKey(0)
#çarpıya bastıgımızda opencv pencereleri kapatmış oluyoruz
cv2.destroyAllWindows()

#mavi yesil ve kırmızı brg 

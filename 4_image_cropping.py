"""
Image Cropping:

Technique: Numpy technique
Module: cv2 

1. Read Image cv2.imread()
2. Check Numpy Types
3. Check Shape of image 
4. Cropping dimensions [rows, columns] = img[y:y+h, x:x+w]
5. Show Image cv2.imshow()
6. cv2.waitKey(0)
7. cv2.destroyAllWindows()

"""

import cv2 

img = cv2.imread("test.jpeg")

print(type(img))

print(img.shape)

crop_img = img[200:800, 100:700]

cv2.imshow("original image", img)

cv2.imshow("cropped image", crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()



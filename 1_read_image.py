"""
Window bitmaps - *.bmp, *.dib
JPEG files - *.jpeg, *.jpg, *.jpe
Portable Network Graphics - *.png
Portable image format- *.pbm, *.pgm, *.ppm
TIFF files - *.tiff, *.tif 

pip install opencv-python
pip install numpy
pip install matplotlib

import cv2

1. Read an image using cv2.imread()
2. GUI => cv2.imshow()
3. cv2.waitkey(0) to hold the image
4. Delete cv2.destroyAllWindows()

"""

import cv2

read_image = cv2.imread("test.jpeg",1)

cv2.imshow("my_image", read_image)

cv2.waitKey(0)

cv2.destroyAllWindows()


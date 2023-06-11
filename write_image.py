"""
**** Write Image ****

Required Modules: os and cv2

1. Current image location (path)
2. Where we need to store/write (directory)
3. Read image => cv2.imread()
4. Change directory => os.chdir()
5. file_name => my_image.jpeg
6. Write image => cv2.imwrite()
7. Check => os.listdir()
"""
import os
import cv2

image_path = r'test.jpeg'
directory = r'F:\MyLearning\OpenCV\Basics\images'

read_img = cv2.imread(image_path, 0)

os.chdir(directory)

file_name = 'my_image.jpeg'

cv2.imwrite(file_name, read_img)

print("List out images: ", os.listdir(directory))



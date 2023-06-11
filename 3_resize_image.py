"""
**** Resize Image ***

Modules: cv2

Steps:
1. Read the image cv2.imread('test.jpeg')

2. Downscale or Upscale 
    
    cv2.resize(image_object, down_points, interpolation= cv2.INTER_LINEAR)

    a) cv2.INTER_AREA: This is used when we need to shrink an image.
    b) cv2.INTER_CUBIC: This is slow but more efficient.
    c) cv2.INTER_LINEAR: This is primarily used when zooming is required. 
        => This is the default interpolation technique in OpenCV.
        => Bilinear interpolation
        => Finding the “nearest” pixel (y=mx+c)
    d) cv2.INTER_LANCZOS4 : 8 x 8 pixel neighborhood

3. Display cv2.imshow('window_name', resized_value) 
4. Wait Key : cv2.waitKey()
5. press any key to close the windows => cv2.destroyAllWindows()
"""
import cv2 

rd_img = cv2.imread('test.jpeg')

# cv2.imshow('original_image', rd_img)
# down_points = (300, 300)

# resized_value = cv2.resize(rd_img, down_points, interpolation= cv2.INTER_LINEAR)

# cv2.imshow('original_image', resized_value)

up_points = (600, 600)

resized_value = cv2.resize(rd_img, up_points, interpolation= cv2.INTER_LINEAR)

cv2.imshow('original_image', resized_value)

cv2.waitKey()
cv2.destroyAllWindows()
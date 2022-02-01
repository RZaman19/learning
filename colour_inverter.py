# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 15:16:23 2022

@author: RahbarZ
"""

import cv2
#reading image
image =cv2.imread("test1.jpg")

#converting BGR image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#image inversion
inverted_image=255 - gray_image

blurred  = cv2.GaussianBlur(inverted_image,(21,21),0)
inverted_blurred = 255-blurred
pencil_sketch = cv2.divide(gray_image,inverted_blurred,scale = 256.0)

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

cv2.imshow("Original Image", image)
cv2.imshow("Colour inverted", pencil_sketch)
cv2.waitKey(0)
#imports computer vision version 2
import cv2

#import the numercial processing library for python
import numpy

try:
    #load an image from the disk
    circleImage = cv2.imread('circles.jpg')

    #convert to grayscale
    grayImage = cv2.cvtColor(circleImage, cv2.COLOR_BGR2GRAY)

    cv2.imshow('detected circles', circleImage)
    cv2.waitKey(0)

    cv2.imshow('detected circles', grayImage)
    cv2.waitKey(0)
    
    #save the image to disk
    cv2.imwrite('greyscale.png', grayImage)

finally:
    cv2.destroyAllWindows()


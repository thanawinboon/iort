#imports computer vision version 2
import cv2

#import the numercial processing library for python, call it np for short
import numpy as np

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180




try:
    camera.start_preview()
    sleep(2)
    camera.capture("YAS.jpg")
    camera.stop_preview()
    
    #====================================================================================
    #load an image from the disk
    circleImage = cv2.imread("YAS.jpg")
    
    #blur the image, so that similar colors get combined
    #https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html
    blurImage = cv2.blur(circleImage,(5,5))
    
    #convert the image to grayscale
    grayImage = cv2.cvtColor(blurImage, cv2.COLOR_BGR2GRAY)
    
    #display the original image
    cv2.imshow("circles.jpg", circleImage)
    cv2.waitKey(0)

    #display the image that is greyscale and blurred.
    cv2.imshow("greyscale", grayImage)
    cv2.waitKey(0)

    
    #circle detection settings
    circles = cv2.HoughCircles(grayImage, cv2.HOUGH_GRADIENT, 1, minDist=30, param1=10, param2=22, minRadius=10, maxRadius=100)
    circles = np.uint16(np.around(circles))

    #set a counter for the circles
    circlesNum = 0
    
    fontWOW = cv2.FONT_HERSHEY_SIMPLEX
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(circleImage,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(circleImage,(i[0],i[1]),2,(0,0,255),3)
        circlesNum = circlesNum + 1
        cv2.putText(circleImage, str(circlesNum),(i[0],i[1]), fontWOW, 1,(0,0,0),2,cv2.LINE_AA)
    
    print(circlesNum)
    
    #display the image with the circles highlighted.
    cv2.imshow("final", circleImage)
    cv2.waitKey(0)
    
    #save the final image to disk'
    cv2.imwrite("final.jpg", circleImage)
    
finally:
    cv2.destroyAllWindows()
    camera.stop_preview()

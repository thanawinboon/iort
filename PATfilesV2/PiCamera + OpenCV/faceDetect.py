import numpy as np
import cv2 as cv

#download the cascades from https://github.com/opencv/opencv/tree/master/data/haarcascades
try:
    #frontface = 'haarcascade_frontalface_default.xml'
    #upperbody = 'haarcascade_upperbody.xml'
    #eyes = 'haarcascade_eye.xml'

    custom_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

    img = cv.imread('face.jpg')

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    detect = custom_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in detect:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv.imshow('img',img)
    cv.waitKey(0)

finally:
    cv.destroyAllWindows()
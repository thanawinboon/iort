import numpy as np
import cv2 as cv

#download the cascades from https://github.com/opencv/opencv/tree/master/data/haarcascades

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')

img = cv.imread('face.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+(h//2), x:x+w]
    roi_gray2 = gray[y+(h//2):y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    roi_color2 = img[y+(h//2):y+h, x:x+w]

    #detect eyes within the Region of Interest (ROI) - e.g. the face we found already

    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    smiles = smile_cascade.detectMultiScale(roi_gray2)
    for (ex,ey,ew,eh) in smiles:
        cv.rectangle(roi_color2,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
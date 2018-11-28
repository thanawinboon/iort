from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

try:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')


    
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 24
    camera.rotation = 180
    rawCapture = PiRGBArray(camera, size=(640, 480))
     
    # allow the camera to warmup
    time.sleep(0.1)
     
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image
        img = frame.array

        #convert to gray scale for the face detect algorithm
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #use the haar cascade to detect faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+(h//2), x:x+w]
            roi_gray2 = gray[y+(h//2):y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            roi_color2 = img[y+(h//2):y+h, x:x+w]

            #detect eyes within the Region of Interest (ROI) - e.g. the face we found already

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            smiles = smile_cascade.detectMultiScale(roi_gray2)
            for (ex,ey,ew,eh) in smiles:
                cv2.rectangle(roi_color2,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
                
        # show the frame
        cv2.imshow("Frame", img)
        
        key = cv2.waitKey(1) & 0xFF
 
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
 
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
	    
finally:
    cv2.destroyAllWindows()
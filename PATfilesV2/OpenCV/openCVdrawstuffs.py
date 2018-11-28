import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)
fontWOW = cv2.FONT_HERSHEY_SIMPLEX

try:
    #lines and shapes
    cv2.line(img,(0,0),(511,511),(255,0,0),10)
    cv2.line(img,(511,0),(0,511),(255,0,0),10)
    cv2.circle(img, (256,256), 100, (0,0,255), -1)
    cv2.rectangle(img, (206,306), (306,206), (0,255,0), -1)
    
    #font + text
    cv2.putText(img, 'OpenCV',(206,500), fontWOW, 1,(255,255,255),2,cv2.LINE_AA)
    
    cv2.imshow('image',img)
    cv2.waitKey(0)

finally:
    cv2.destroyAllWindows()
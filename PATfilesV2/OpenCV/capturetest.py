import cv2
import numpy as np

try:
  cap = cv2.VideoCapture(0)

  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

  while True:
    ret, frame = cap.read()
    gay = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(0):
      break

finally:
  cap.release()
  out.release()
  cv2.destroyAllWindows()

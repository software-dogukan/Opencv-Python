import numpy as np
import cv2 as cv

cap=cv.VideoCapture(0)

if not cap.isOpened():
    print("can not open camera")
    exit()
ret,frame=cap.read()
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
if not ret:
    print("Can not receive frame(stream end?).Exiting")
    exit()
gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
out.write(frame)
cv.imshow('frame',gray)
if cv.waitKey(1)==ord('q'):
    exit()
cap.release()
out.release()
cv.destroyAllWindows()



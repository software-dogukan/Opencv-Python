import numpy as np
import cv2 as cv
img =cv.imread("jpg_name.jpg")
assert img is not None,"File could not be read, chech with os.path.exists()"
b,g,r=cv.split(img)
img=cv.merge((b,g,r))
cv.imshow("deneme",img)
cv.waitKey(0)



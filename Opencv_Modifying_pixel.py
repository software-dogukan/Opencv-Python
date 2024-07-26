import numpy as np
import cv2 as cv
img =cv.imread("1.jpg")
assert img is not None,"File could not be read, chech with os.path.exists()"
forexample=img[280:340,330:390]
img[273:333,100:160]=forexample
cv.imshow("try",img)
cv.waitKey(0)



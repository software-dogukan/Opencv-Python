import cv2 as cv
import numpy as np

img1 = cv.imread('star.jpg', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('star2.jpg', cv.IMREAD_GRAYSCALE)
assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"

ret, thresh = cv.threshold(img1, 127, 255, 0)
ret, thresh2 = cv.threshold(img2, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, 2, 1)
cnt1 = contours[0]
contours, hierarchy = cv.findContours(thresh2, 2, 1)
cnt2 = contours[0]

ret = cv.matchShapes(cnt1, cnt2, 1, 0.0)
print(ret)
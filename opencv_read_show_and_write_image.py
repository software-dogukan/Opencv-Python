import cv2 as cv
import sys
image=cv.imread("dogukan_LOGO.jpg")
if image is None:
    sys.exit("Could not read the image")
cv.imshow("My LOGO",image)
k=cv.waitKey(0)
if k==ord("s"):
    cv.imwrite("starry_night.png", image)
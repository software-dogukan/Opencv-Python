import cv2 as cv

# Read images
img1 = cv.imread('dogukanlogo.jpg')
img2 = cv.imread('profesyonel_fotografci.jpg')

# Check if images are successfully loaded
if img1 is None:
    raise FileNotFoundError("dogukanlogo.jpg could not be read. Please check the file path.")
if img2 is None:
    raise FileNotFoundError("profesyonel_fotografci.jpg could not be read. Please check the file path.")

# Resize img2 to match the dimensions of img1 if they are different
img2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))

# Check if images have the same dimensions
if img1.shape != img2.shape:
    raise ValueError("Images must have the same dimensions. Please check the image sizes.")

# Blend the images with specified weights
dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)

# Display the blended image in a window
cv.imshow('Blended Image', dst)

# Wait indefinitely for a key press
cv.waitKey(0)

# Close all OpenCV windows
cv.destroyAllWindows()

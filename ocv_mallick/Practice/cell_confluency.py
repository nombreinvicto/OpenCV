import cv2
import imutils
from imutils import paths
import numpy as np

image = cv2.imread('792.JPG')

# load the image and convert it to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# do gaussian blurring to remove noise use 5x5 kernel
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
blurred = gray.copy()

# compute a "wide", "mid-range", and "tight" threshold for the edges
wide = cv2.Canny(blurred, 0, 255)
mid = cv2.Canny(blurred, 30, 150)
tight = cv2.Canny(blurred, 240, 250)

cv2.imshow('Threshold', mid)
cv2.waitKey(0)

# dilation - do it on mid to close contour gaps
# dilated = cv2.dilate(mid.copy(), (3, 3), iterations=1)
# dilated = wide.copy()
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilated = cv2.morphologyEx(mid, cv2.MORPH_CLOSE, kernel)
# find all contours in the image and draw ALL contours on the image
cnts = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_NONE)
cnts = imutils.grab_contours(cnts)
clone = image.copy()
cv2.drawContours(clone, cnts, -1, (0, 255, 0), 1)
print("Found {} contours".format(len(cnts)))

# calculate confluence area
total_area = 0
for i, c in enumerate(cnts):
    area = cv2.contourArea(c)
    total_area += area

total_image_area = mid.shape[0] * mid.shape[1]
print(mid.shape)
print(f"Area of total image: {total_image_area}")
print(f"Area enclosed by contours: {total_area}")
confluence = (total_area / total_image_area) * 100
print(f"Confluence: {confluence}")
cv2.imshow('Output', clone)
cv2.waitKey(0)


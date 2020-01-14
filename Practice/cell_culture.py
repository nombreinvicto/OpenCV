import numpy as np
import imutils
import cv2

# load image
image = cv2.imread('40%.jpg')

# load the image and convert it to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# do gaussian blurring to remove noise use 5x5 kernel
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# show the original and blurred images
cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)

# compute a "wide", "mid-range", and "tight" threshold for the edges
wide = cv2.Canny(blurred, 10, 200)
mid = cv2.Canny(blurred, 30, 150)
tight = cv2.Canny(blurred, 240, 250)

# show the edge maps - from images, mid threshold looks to be the best choice
cv2.imshow("Wide Edge Map", wide)
# cv2.imshow("Mid Edge Map", mid)
# cv2.imshow("Tight Edge Map", tight)


# dilation - do it on mid to close contour gaps
dilated = cv2.dilate(mid.copy(), None, iterations=1)
cv2.imshow("Dilated {} times".format(3), dilated)

# find all contours in the image and draw ALL contours on the image
cnts = cv2.findContours(dilated.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cnts = imutils.grab_contours(cnts)
clone = image.copy()
cv2.drawContours(clone, cnts, -1, (0, 255, 0), 1)
print("Found {} contours".format(len(cnts)))

# show the output image
cv2.imshow("All Contours", clone)

# calculate confluence area
total_area = 0
for i, c in enumerate(cnts):
    area = cv2.contourArea(c)
    total_area += area

total_image_area = mid.shape[0] * mid.shape[1]
print(mid.shape)
print(f"Area of total image: {total_image_area}")
print(f"Area enclosed by contours: {total_area}")
print(f"Confluence: {(total_area / total_image_area) * 100}")
cv2.waitKey(0)

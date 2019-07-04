# morphological operations

# first import all modules
import numpy as np
import imutils
import argparse
import cv2

# create the argparse
ag = argparse.ArgumentParser()
ag.add_argument("-i", "--image",
                required=True, help='path to the image')
args = vars(ag.parse_args())

# read and then load the image
img = cv2.imread(args.get("image"))

# grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # type: np.ndarray

# construct a rectangular kernel and do blackhat and tophat
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# blackHat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
# topHat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)
#
# # show the images
# cv2.imshow("Original", img)
# cv2.imshow("Grayscale", gray)
# cv2.imshow("BlackHat", blackHat)
# cv2.imshow("TopHat", topHat)
# cv2.waitKey(0)

# Lets do it step by step. First TopHat. Original Image is gray
# now do opening = erosion followed by dilation to remove noise
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, rectKernel)
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, rectKernel)
cv2.imshow("original", gray)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)
cv2.imshow("TopHat: original - opening", np.subtract(gray, opening))
cv2.imshow("BlackHat: close - original", np.subtract(closing, gray))
cv2.waitKey(0)
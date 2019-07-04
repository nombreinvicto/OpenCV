# import necessary packages
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help='Path to the image')
args = vars(ap.parse_args())

# load the image and display it using opencv
img = cv2.imread(args.get('image'))
cv2.imshow('loaded image', img)
cv2.waitKey(0)

# make the translation matrix
M = np.array([[1, 0, 25], [0, 1, 50]], dtype='float32')

# now do the translate
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow('shifted image', shifted)
cv2.waitKey(0)

# do another translation
M = np.array([[1, 0, -50], [0, 1, -90]], dtype='float32')
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow('shifted image reverse', shifted)
cv2.waitKey(0)

# using imutils
shifted = imutils.translate(img, 25, 50)
cv2.imshow('shifted using imutils', shifted)
cv2.waitKey(0)

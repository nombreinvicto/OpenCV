# import the necessary libraries
import argparse
import numpy
import cv2
import imutils

# create the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help='path to the image file')
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args['image'])
cv2.imshow("Loaded Image", image)
cv2.waitKey(0)

# grab the dimensions and calculate the center
h, w = image.shape[:2]
center = w // 2, h // 2

# rotate the image by 45 deg
m = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, m, (w, h))
cv2.imshow('Rotated of +45', rotated)
cv2.waitKey(0)

# rotate using imutils
r = imutils.rotate(image, 45, center)
cv2.imshow()

# do the imports
import argparse as ag
import cv2
import numpy as np

# create argpare
# ap = ag.ArgumentParser()
# ap.add_argument('-i', '--image', required=True)
# args = vars(ap.parse_args())

# load the image
img = cv2.imread("florida_trip.png")  # type: np.ndarray
cv2.imshow('loaded image', img)
cv2.waitKey(0)

# get the shape of the image and its center coordinate
height, width = img.shape[0:2]
cx, cy = width // 2, height // 2

# go crop the people
people = img[124:212, 225:380]
cv2.imshow('cropped', people)
cv2.waitKey(0)

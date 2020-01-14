import cv2
import argparse as ag
import imutils
import numpy as np

# construct the argument parser
# ap = ag.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Path to the loaded image")
# args = vars(ap.parse_args())

#img = cv2.imread(args.get('image'))
img = cv2.imread("./giraffe.png")
cv2.imshow('Loaded Image', img)
cv2.waitKey(0)

# create a translation matrix
Mt = np.float32(
    [
        [1, 0, 25],
        [0, 1, 50]
    ]
)

translated = cv2.warpAffine(img, Mt, (img.shape[1], img.shape[0]))
cv2.imshow('Translated', translated)
cv2.waitKey(0)
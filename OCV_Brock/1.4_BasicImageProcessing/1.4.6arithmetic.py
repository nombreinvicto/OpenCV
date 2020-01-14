# do the imports
import cv2
import numpy as np
import argparse as ag

# create the argeparser
ap = ag.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the required image")
args = vars(ap.parse_args())

# load and show the image
img = cv2.imread(args.get("image"))  # type:np.ndarray
cv2.imshow("loaded image", img)
cv2.waitKey(0)

# create a numpy matrix the same shape as image
M = np.ones(shape=img.shape, dtype='uint8') * 75
added = cv2.add(M, img)
cv2.imshow('added image', added)
cv2.waitKey(0)

print(added[152, 61])

# # now do the subtraction
# subtract = cv2.subtract(img, M)
# cv2.imshow('subtract image', subtract)
# cv2.waitKey(0)

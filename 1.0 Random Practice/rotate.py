# import the required modules
import numpy as np
import argparse as ag
import cv2

# create the argument parser
ap = ag.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the loaded image")
args = vars(ap.parse_args())

# show the loaded image
img = cv2.imread(args.get('image'))  # type: np.ndarray
print('size of the image is width {} and height {}'
      .format(img.shape[1], img.shape[0]))
cv2.imshow('Loaded Image', img)
cv2.waitKey(0)

# now rotate the image about the center
Mr = cv2.getRotationMatrix2D((0, 0), 45, 1.0)
rotatedImage = cv2.warpAffine(img, Mr, dsize=(img.shape[1], img.shape[0]))
cv2.imshow('Rotated By +45', rotatedImage)
cv2.waitKey(0)


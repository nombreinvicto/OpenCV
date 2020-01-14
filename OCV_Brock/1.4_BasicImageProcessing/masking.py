# do the imports
import cv2
import numpy as np
import argparse as ag

# create the argparser
ap = ag.ArgumentParser()
ap.add_argument("-i", "--image", help="Path to the image",
                required=True)
args = vars(ap.parse_args())

# load and show the image
img = cv2.imread(args.get("image"))
cv2.imshow('loaded image', img)
print(f'Shape of the image {img.shape}')
cv2.waitKey(0)

# create the mask
mask = np.zeros(shape=img.shape[0:2], dtype='uint8')
cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)
cv2.imshow('mask', mask)
cv2.waitKey(0)

# now apply the mask
masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('mask applied', masked)
cv2.waitKey(0)

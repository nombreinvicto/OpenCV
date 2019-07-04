# import the needed modules
import numpy as np
import argparse as ag
import cv2

# create the argument parser
ap = ag.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the loade image")
args = vars(ap.parse_args())

# show the loaded image
img = cv2.imread(args.get('image'))  # type: np.ndarray
cv2.imshow('Loaded image', img)
cv2.waitKey(0)

# now flip the image horizontally
flippedImage = cv2.flip(img, 1)
cv2.imshow('Flipped Image', flippedImage)
cv2.waitKey(0)

# now rotate the image +45
center = img.shape[1] // 2, img.shape[0] // 2

Mr = cv2.getRotationMatrix2D(center, 45, 1.0)
rotatedImage = cv2.warpAffine(flippedImage, Mr,
                              dsize=(flippedImage.shape[1],
                                     flippedImage.shape[0]))
cv2.imshow('Rotated Image', rotatedImage)
cv2.waitKey(0)


verticalFlippedImage = cv2.flip(rotatedImage, 0)
cv2.imshow('Vert Flipped Image', verticalFlippedImage)
cv2.waitKey(0)
print(verticalFlippedImage[189, 441])

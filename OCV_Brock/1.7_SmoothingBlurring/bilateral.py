# make necessary imports
import numpy as np
import cv2
import argparse

# create the argparse
ag = argparse.ArgumentParser()
ag.add_argument("-i", "--image",
                required=True,
                help="path to the required image")
args = vars(ag.parse_args())

# load the image and show it
img = cv2.imread(args.get("image"))  # type: np.ndarray
# see pixel values at a certain coordinate
cv2.imshow("original", img)
cv2.waitKey(0)

params = [
    (11, 21, 7),
    (11, 41, 21),
    (11, 61, 39)
]

for diameter, sigmaColor, sigmaSpace in params:
    # apply bilateral filtering and then display the image
    bilateralBlurred = cv2.bilateralFilter(img.copy(), diameter,
                                           sigmaColor, sigmaSpace)
    title = f"Blurred: d={diameter}, sc={sigmaColor}, sp={sigmaSpace}"
    cv2.imshow(title, bilateralBlurred)
    cv2.waitKey(0)

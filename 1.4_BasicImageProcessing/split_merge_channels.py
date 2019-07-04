# quiz
# do the imports
import cv2
import numpy as np
import argparse as ag

# create the argument parser
ap = ag.ArgumentParser()
ap.add_argument("-i", "--image", help="Path to the required image",
                required=True)
args = vars(ap.parse_args())

# load the image and show it
img = cv2.imread(args.get("image"))
cv2.imshow('loaded image', img)
cv2.waitKey()

# split the image into channels
B, G, R = cv2.split(img)
print(f"value of the RED channel at "
      f"x = 180 and y = 94 is {R[94, 180]}")

print(f"value of the BLUE channel at "
      f"x = 13 and y = 78 is {B[78, 13]}")

print(f"value of the GREEN channel at "
      f"x = 80 and y = 5 is {G[5, 80]}")

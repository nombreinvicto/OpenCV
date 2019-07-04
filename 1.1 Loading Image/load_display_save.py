# import necessary packages
import argparse as ag
import cv2

# construct the argument parser and parse the arguments
ap = ag.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to the image file to be read")
args = vars(ap.parse_args())

# open the image and then show it
image = cv2.imread(args["image"])
cv2.imshow("Florida Image", image)
cv2.waitKey(0)

# morphological operations

# first import all modules
import numpy as np
import argparse
import cv2

# create the argparse
ag = argparse.ArgumentParser()
ag.add_argument("-i", "--image",
                required=True, help='path to the image')
args = vars(ag.parse_args())

# read and then load the image
img = cv2.imread(args.get("image"))


def show_original_iamge():
    cv2.destroyAllWindows()
    cv2.imshow('original', img)
    cv2.waitKey(0)


# grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # type: np.ndarray
cv2.imshow('grayscale', gray)
cv2.waitKey(0)

# apply a series of erosions
# for i in range(3):
#     eroded = cv2.erode(gray.copy(), None, iterations=i+1)
#     cv2.imshow(f"eroded {i+1} times", eroded)
#     cv2.waitKey(0)


# apply dilation
# for i in range(3):
#     dilated = cv2.dilate(gray.copy(), None, iterations=i+1)
#     cv2.imshow(f"dilated {i+1} times", dilated)
#     cv2.waitKey(0)


# apply opening
kernelSizes = [(3, 3), (5, 5), (7, 7)]

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(gray.copy(), cv2.MORPH_OPEN, kernel)
    cv2.imshow(f"opening: {kernelSize[0]}, {kernelSize[1]}", opening)
    cv2.waitKey(0)

# make necessary imports
import numpy as np
import cv2
import imutils
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
print(img.shape)
sth = img[0:2, 0:2]
print(sth.shape)
cv2.imshow("original", img)
cv2.waitKey(0)
print("=" * 50)

# now do average blurrin, larger kernel, more is blurring
kernelSizes = [(3, 3), (9, 9), (15, 15)]

# for kernelSize in kernelSizes:
#     blurred = cv2.blur(img.copy(), kernelSize)
#     print(blurred[0:2, 0:2])
#     print("=" * 50)
#     cv2.imshow(f"average with kernelSize: {kernelSize}", blurred)
#     cv2.waitKey(0)


# now do gaussian blurring- more natural
# for kernelSize in kernelSizes:
#     blurred = cv2.GaussianBlur(img.copy(), kernelSize, 0)
#     print(blurred[0:2, 0:2])
#     print("=" * 50)
#     cv2.imshow(f"gaussian with kernelSize: {kernelSize}", blurred)
#     cv2.waitKey(0)

# now do some median blurring
for kernelSize in 3, 9, 15:
    medianBlurred = cv2.medianBlur(img.copy(), kernelSize)
    cv2.imshow(f"median blurred with kernelSize{kernelSize}",
               medianBlurred)
    cv2.waitKey(0)

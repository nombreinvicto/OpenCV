# import all the packages
import numpy as np
import argparse
import imutils
import cv2

# create the argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the image')
args = vars(ap.parse_args())

# load the image and show it
img = cv2.imread(args.get('image'))
cv2.imshow('original image', img)
cv2.waitKey(0)

# set the aspect ratio
width_new = 300.0
r = width_new / img.shape[1]
dim_new = int(width_new), int(r * img.shape[0])

# perform the resizing and show the image
resized = cv2.resize(img, dim_new, interpolation=cv2.INTER_AREA)
cv2.imshow(f'resized with r = {r}', resized)
cv2.waitKey(0)

# create a list of interpolation methods
interpolation_methods = {
    f'{cv2.INTER_NEAREST}': cv2.INTER_NEAREST,
    f'{cv2.INTER_LINEAR}': cv2.INTER_LINEAR,
    f'{cv2.INTER_AREA}': cv2.INTER_AREA,
    f'{cv2.INTER_CUBIC}': cv2.INTER_CUBIC,
    f'{cv2.INTER_LANCZOS4}': cv2.INTER_LANCZOS4
}
# increase width by 3 times i.e r has to be 3.0
r_new = 3
width_new_3X = img.shape[1] * r_new
height_new_3X = img.shape[0] * r_new
dim_new_3X = int(width_new_3X), int(height_new_3X)

for name, method in interpolation_methods.items():
    res = cv2.resize(img, dim_new_3X, interpolation=method)
    cv2.imshow(f'mag=3X :: alg={name}', res)
    cv2.waitKey(0)

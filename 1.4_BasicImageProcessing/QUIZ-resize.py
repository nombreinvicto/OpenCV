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

# make new width 100 px
print(img.shape)  # 188 x 250
width_new = 100.0
height_new = (width_new / img.shape[1]) * img.shape[0]
dim = int(width_new), int(height_new)
res = cv2.resize(img, dim, interpolation=cv2.INTER_NEAREST)
cv2.imshow('width = 100px', res)
cv2.waitKey(0)
print(f'B={res[74, 20][0]} ;; G={res[74, 20][1]} ;; R={res[74, 20][2]}')

# double the size of the image
width_2X = img.shape[1] * 2
height_2X = img.shape[0] * 2
dim = int(width_2X), int(height_2X)

res = cv2.resize(img, dim, interpolation=cv2.INTER_CUBIC)
cv2.imshow('width = 2X', res)
cv2.waitKey(0)
print(f'B={res[367, 170][0]} ;; G={res[367, 170][1]} ;; R={res[367, 170][2]}')

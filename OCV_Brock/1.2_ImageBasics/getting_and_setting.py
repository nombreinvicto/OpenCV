# import the packages

import argparse
import cv2

# construct the argument parser and parse the arguments
ag = argparse.ArgumentParser()
ag.add_argument("-i", "--image", required=True, help="Path to the image file")
args = vars(ag.parse_args())

# load the image, grab its dimensions and show it
image = cv2.imread(args["image"])
print("This is the shape of the image, ", image.shape)
cv2.imshow("Florida Trip Pic", image)
cv2.waitKey(0)

# image are just numpy arrays - Top Left pixel found at (0,0)
first_pixel = image[0, 0]
last_pixel = image[449, 599]

print(f"BGR values of first_pixel are: {first_pixel}")
print(f"BGR values of the last pixel are: {last_pixel}")

height_image = image.shape[0]
width_image = image.shape[1]

center_height = height_image // 2
center_width = width_image // 2

# show the top left corner of image
top_left = image[0: center_height + 1,
           # grab height - remember last index is not considered so +1
           0: center_width + 1]
cv2.imshow("Top Left", top_left)
cv2.waitKey(0)

# show the bottom right side of the pic
bottom_right = image[center_height:height_image, center_width:width_image]
cv2.imshow("Bottom Right", bottom_right)
cv2.waitKey(0)

# change the color of the top left corner and bottom right corner
image[0: center_height + 1, 0: center_width + 1] = (0, 0, 255)  # top left - red
image[center_height:height_image, center_width:width_image] = (
    0, 255, 0)  # bottom right - red

cv2.imshow("Edited Image", image)
cv2.waitKey(0)

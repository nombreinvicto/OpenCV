from cv2 import cv2

im = cv2.imread('792.JPG', cv2.IMREAD_GRAYSCALE)
print(im.shape)
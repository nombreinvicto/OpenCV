import cv2
import numpy as np

# load the image and show it
image = cv2.imread('./giraffe.png')
cv2.imshow('loaded image', image)
cv2.waitKey(0)

# do the imports
import cv2
import numpy as np
import argparse as ag

# create a rectangleCanvas
rectangleCanvas = np.zeros((300, 300, 1), dtype='uint8')
cv2.rectangle(rectangleCanvas, pt1=(25, 25), pt2=(275, 275), color=255,
              thickness=-1)
cv2.imshow('Canvas', rectangleCanvas)
cv2.waitKey(0)

# secondly lets draw a circle
circleCanvas = np.zeros((300, 300), dtype='uint8')
cv2.circle(circleCanvas, (150, 150), 150, 255, -1)
cv2.imshow('Circle', circleCanvas)
cv2.waitKey(0)

# AND logic
andLogicImage = cv2.bitwise_and(rectangleCanvas, circleCanvas)
cv2.imshow('AND', andLogicImage)
cv2.waitKey(0)

# OR logic
orLogicImage = cv2.bitwise_or(rectangleCanvas, circleCanvas)
cv2.imshow('OR', orLogicImage)
cv2.waitKey(0)

# XOR logic
xorLogicImage = cv2.bitwise_xor(rectangleCanvas, circleCanvas)
cv2.imshow('XOR', xorLogicImage)
cv2.waitKey(0)
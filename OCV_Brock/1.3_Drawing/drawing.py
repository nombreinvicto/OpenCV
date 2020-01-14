# load necessary packages
import numpy as np
import cv2
import random as rn

# initialise a 300 x 300 canvas with 3 channels
canvas = np.zeros((600, 300, 3), dtype='uint8')

# define the basic color tuples
green = 0, 255, 0
red = 0, 0, 255
blue = 255, 0, 0

# draw the lines
cv2.line(canvas, (0, 0), (150, 150), green)
cv2.imshow('Green Line', canvas)
cv2.waitKey(0)

# draw a rectangle
cv2.rectangle(canvas, (10, 10), (60, 60), green, -1)
cv2.imshow('Rectangle', canvas)
cv2.waitKey(0)

# draw the circles
cv2.circle(canvas, (canvas.shape[1] // 2, canvas.shape[0] // 2,), radius=50,
           color=red, thickness=-1)
cv2.imshow("Circle", canvas)
cv2.waitKey(0)

# create a new canvas
canvas_new = np.zeros((500, 500, 3 ), dtype='uint8')

# draw 25 random filled circles
for i in range(25):
    color = np.random.randint(0, 255, size=3).tolist()
    center = tuple(np.random.randint(low=0, high=300, size=2))
    radius = np.random.randint(5, 200)

    cv2.circle(canvas_new, center, radius, color, thickness=-1)

cv2.imshow("All Circles", canvas_new)
cv2.waitKey(0)




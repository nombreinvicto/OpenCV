import imutils
import math
import cv2
import os

cwd = os.getcwd()
IMAGE_FOLDER = cwd + r"\\static\\images\\"
confluence = None


def calculate_confluency(filename):
    global confluence
    try:
        # load image
        image = cv2.imread(IMAGE_FOLDER + filename)

        # load the image and convert it to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # do gaussian blurring to remove noise use 5x5 kernel
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # compute a "wide", "mid-range", and "tight" threshold for the edges
        wide = cv2.Canny(blurred, 10, 200)
        mid = cv2.Canny(blurred, 30, 150)
        tight = cv2.Canny(blurred, 240, 250)

        # dilation - do it on mid to close contour gaps
        dilated = cv2.dilate(mid.copy(), None, iterations=1)

        # find all contours in the image and draw ALL contours on the image
        cnts = cv2.findContours(dilated.copy(), cv2.RETR_LIST,
                                cv2.CHAIN_APPROX_NONE)
        cnts = imutils.grab_contours(cnts)
        clone = image.copy()
        cv2.drawContours(clone, cnts, -1, (0, 255, 0), 1)
        print("Found {} contours".format(len(cnts)))

        # calculate confluence area
        total_area = 0
        for i, c in enumerate(cnts):
            area = cv2.contourArea(c)
            total_area += area

        total_image_area = mid.shape[0] * mid.shape[1]
        print(mid.shape)
        print(f"Area of total image: {total_image_area}")
        print(f"Area enclosed by contours: {total_area}")
        confluence = (total_area / total_image_area) * 100
        print(f"Confluence: {confluence}")

        if confluence > 100:
            confluence = 100

        # predicting which cell type it is
        total_area = 0
        hull_total = 0
        for i, c in enumerate(cnts):
            area = cv2.contourArea(c)
            hull = cv2.convexHull(c)
            hull_area = cv2.contourArea(hull)
            total_area += area
            hull_total += hull_area

        solidity = total_area / hull_total

        if solidity > 0.79:
            cell_type = 'Primary Myoblast Cell'
        else:
            cell_type = 'NIH 3T3 Cell'

        return confluence, cell_type
    except Exception as msg:
        return msg


def estimate_overgrow(proliferation_hr):
    global confluence

    if not confluence or not proliferation_hr:
        return None

    else:
        # Estimating the confluency overgrown
        Day = []
        Hours = []
        proliferation_rate = float(proliferation_hr)
        day_conversion = proliferation_rate / 24
        overgrown = 100.1

        for n in range(100):
            while confluence * 2 ** n < overgrown:
                Day = math.floor(day_conversion * 2 ** (n - 1))
                Hours = math.floor(
                    ((overgrown - (
                            confluence * 2 ** n)) * proliferation_rate) / (
                            confluence * 2 ** n))
                break

        if 24 <= Hours <= 48:
            Day = Day + 1
            Hours = Hours - 24

        if 48 <= Hours <= 72:
            Day = Day + 2
            Hours = Hours - 48

        return f' {round(Day, 1)} Days and {round(Hours, 2)} Hrs'

import cv2
import numpy as np
import requests
from typing import List

DEVICE_LIST = {
    'WEBCAM': 0,
    'FILE': 'hasc_video.avi'
}

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(DEVICE_LIST['FILE'])

while camera.isOpened():
    ret, frame = camera.read()  # type: bool, np.ndarray

    if ret:
        frame_clone = frame.copy()

        # get the rects
        rects = detector.detectMultiScale(frame_clone,
                                          scaleFactor=1.1,
                                          minNeighbors=5,
                                          minSize=(30, 30),
                                          flags=cv2.CASCADE_SCALE_IMAGE)

        if len(rects) > 0:
            x, y, w, h = tuple(rects[0])
            cv2.rectangle(frame_clone, (x, y), (x + w, y + h), (0, 0, 255), 3)

        cv2.imshow("Video Output", frame_clone)
        retval = cv2.waitKey(1)
        if retval == ord('a'):
            print('User command to quit....')
            camera.release()
            cv2.destroyAllWindows()

    else:
        print('Video Capture Failed')
        camera.release()
        cv2.destroyAllWindows()
        break

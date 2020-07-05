import cv2
import numpy as np
import requests
from typing import List

DEVICE_LIST = {
    'WEBCAM': 0,
    'FILE': 'hasc_video.avi'
}

camera = cv2.VideoCapture(DEVICE_LIST['FILE'])

while camera.isOpened():
    ret, frame = camera.read()  # type: bool, np.ndarray

    if ret:
        frame_clone = frame.copy()
        frame_clone = cv2.resize(frame_clone, dsize=(600, 600))

        cv2.imshow("Video Output", frame_clone)
        retval = cv2.waitKey(50)
        if retval == 13: # 13 = enter
            print('User command to quit....')
            camera.release()
            cv2.destroyAllWindows()

    else:
        print('Video Capture Failed')
        camera.release()
        cv2.destroyAllWindows()
        break


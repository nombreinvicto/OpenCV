import requests
import numpy as np
import cv2

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
url = 'http://192.168.0.12:8080/shot.jpg'

while True:

    try:
        response = requests.get(url)
        img_array = np.array(bytearray(response.content), dtype=np.uint8)
        frame = cv2.imdecode(img_array, -1)  # type: np.ndarray

        if frame.any():
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
            retval = cv2.waitKey(100)
            if retval == ord('a'):
                print('User command to quit....')
                cv2.destroyAllWindows()

    except Exception as msg:
        print(msg)

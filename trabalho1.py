import cv2
import numpy as np
import time

video = cv2.VideoCapture(0)

while True:

    ret, frame = video.read()

    cv2.imshow("Video", frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

video.release()
cv2.destroyAllWindows()

import cv2 as cv
import numpy as np
import mediapipe as mp

camera =cv.VideoCapture(1)

while True:
    ret, frame = camera.read()
    cv.imshow('frame', frame )
    key = cv.waitKey(1)
    if key ==ord('q'):
        break
camera.release()
cv.destroyAllWindows()
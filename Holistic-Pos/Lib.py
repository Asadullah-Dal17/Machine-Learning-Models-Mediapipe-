import cv2 as cv
import numpy as np
import mediapipe as mp 


# TODO body landmarks detection (Create a function)
def PoseLandmarks(image, landmark):
    # print(landmark)
    FullBodyPoints = []
    for ID, marks in enumerate(landmark):
        # print(ID, "  ", marks)
        height, width, _ = image.shape
        Points = (int(marks.x * width), int(marks.y * height))
        # print(Points)
        FullBodyPoints.append(Points)
        # cv.circle(image, Points, 5, (255, 0, 255), 3)
        cv.putText(image, f'{ID}', Points, cv.FONT_HERSHEY_COMPLEX, 0.4, (125, 255,0), 1)

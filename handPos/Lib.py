import cv2 as cv
import numpy as np
import mediapipe as mp
import math

class handDetector():
    # colours
    YELLOW = (0, 255, 255)
    CYAN = (255, 255, 0)
    MAGENTA = (255, 0, 255)
    GOLDEN = (32, 218, 165)
    LIGHT_BLUE = (255, 30, 144)
    PURPLE = (128, 0, 128)
    CHOCOLATE = (30, 105, 210)
    PINK = (147, 20, 255)
    ORANGE = (0, 69, 255)
    def __init__(self, mode=False, max_num_hands=2, min_detection_conf=0.5, min_tracking_conf=0.5):
        self.mode = mode
        self.max_num_hands = max_num_hands
        self.min_detection_conf = min_detection_conf
        self.min_tracking_conf = min_tracking_conf

        self.mpHands = mp.solutions.hands
        self.hands =self.mpHands.Hands(self.mode, self.max_num_hands,self.min_detection_conf, self.min_tracking_conf)
        self.mpDraw = mp.solutions.drawing_utils

    def getHandLandmarks(self, image, Draw= True):
        # image.flags.writeable = False
        # get results from hand pos estimator
        RGB_image =cv.cvtColor(image, cv.COLOR_BGR2RGB)
        # print("working_")
        results = self.hands.process(RGB_image)
        RGB_image.flags.writeable = True
        if results.multi_hand_landmarks:
            for handMarks in results.multi_hand_landmarks:
                # print(handMarks)
                for IDs, HandPoints in enumerate(handMarks.landmark):
                    # cv.circle(image, (handMarks.landmark.x, handMarks.landmark.y), 2, (0,255,0), 2)
                    
                    print(f"{IDs}  {HandPoints.x}")
            # print("land marks are detected")
        return image


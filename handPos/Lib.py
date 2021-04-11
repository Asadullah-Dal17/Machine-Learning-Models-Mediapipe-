import cv2 as cv
import numpy as np
import mediapipe as mp
import math

class handDetector():
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
        print("working_")
        results = self.hands.process(RGB_image)
        RGB_image.flags.writeable = True
        if results.multi_hand_landmarks:
            print("land marks are detected")
        # return image


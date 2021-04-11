import cv2 as cv
import numpy as np
import mediapipe as mp
import time 

# Variable 
startingTime = time.time()
frameCounter = 0

#colours
YELLOW = (0,255,255)
CYAN = (255,255,0)
MAGENTA =(255,0,255)
GOLDEN = (32,218,165)
LIGHT_BLUE = (255,30,144)
PURPLE = (128,0,128)
CHOCOLATE = (30,105,210)
PINK = (147,20,255)
ORANGE = (0,69,255)

camera =cv.VideoCapture(1)

while True:
    ret, frame = camera.read()
    RGB_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    # cv.imshow('RGB_frame', RGB_frame)
    cv.imshow('frame', frame )
    key = cv.waitKey(1)
    if key ==ord('q'):
        break
camera.release()
cv.destroyAllWindows()
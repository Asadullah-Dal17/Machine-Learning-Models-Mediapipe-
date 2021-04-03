# importing required Modules 
import cv2 as cv
import numpy as np
import mediapipe as mp
import time

# Variable 
cameraID = 1
frameCounter = 0
StartTime = time.time()

# colors
RED = (0, 0 ,255)
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
YELLOW = (0, 255, 255)
BLACK = (0, 0, 0)

# objects 
camera = cv.VideoCapture(cameraID)

while True:
    ret, frame = camera.read()
    # getting image dimension 
    dim = frame.shape
    # creating empty image 
    Mask = np.zeros(dim, dtype=np.uint8)

    cv.imshow("frame", frame)
    
    key = cv.waitKey(1)
    
    if key == ord('q'):
        break
cv.destroyAllWindows()
camera.release()

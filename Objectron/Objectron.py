# importing required Modules 
import cv2 as cv
import numpy as np
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils
mp_objectron = mp.solutions.objectron


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
with mp_objectron.Objectron(static_image_mode=False,
                            max_num_objects=2,
                            min_detection_confidence=0.5,
                            min_tracking_confidence=0.99,
                            model_name='Shoe') as objectron:
    while True:
        ret, frame = camera.read()
        # getting image dimension 
        dim = frame.shape
        # creating empty image 
        Mask = np.zeros(dim, dtype=np.uint8)

        # converting image from BGR to RGB 
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        
        frame.flags.writeable = False

        results = objectron.process(frame)
        print(results)
        cv.imshow("frame", frame)
        
        key = cv.waitKey(1)
        
        if key == ord('q'):
            break
cv.destroyAllWindows()
camera.release()

# Required Modules 
import mediapipe as mp
import cv2 as cv
import numpy as np
import time 
# Variable
cameraID = 1

startTime = time.time()
frameCounter =0
fonts = cv.FONT_HERSHEY_COMPLEX
# colours
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

# create function 
def drawLeftHand(image, mpOut):
    # option = [", "right_hand_landmarks"]
    if mpOut.left_hand_landmarks:
        # print(mpOut.op)
        for ID, marks in enumerate(mpOut.left_hand_landmarks.landmark):
            # print(ID, "  ", marks)
            height, width, _ = image.shape
            pX, pY = int(width * marks.x), int(height * marks.y)
            cv.circle(image, (pX, pY), 2, GREEN, -1)

            # cv.putText(image, f'{ID}', (pX, pY), fonts, 0.5, RED, 1)
# create function 
def drawRightHand(image, mpOut):
    # option = [", "right_hand_landmarks"]
    if mpOut.right_hand_landmarks:
        # print(mpOut.op)
        for ID, marks in enumerate(mpOut.right_hand_landmarks.landmark):
            # print(ID, "  ", marks)
            height, width, _ = image.shape
            pX, pY = int(width * marks.x), int(height * marks.y)
            cv.circle(image, (pX, pY), 2, RED, -1)


# objects 
camera = cv.VideoCapture(cameraID)

# mediapipe objects 
mpHolistic = mp.solutions.holistic

# loading in the Models from mediapipe
with mpHolistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    while True:
        ret, frame = camera.read()
        frameCounter += 1

        # converting frame frame BGR to RGB
        rgbframe = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        # getting the width, height and channels,
        height, width, channeles = rgbframe.shape
        
        rgbframe.flags.writeable = False
        
        results = holistic.process(rgbframe)
        # print(results.pose_landmarks)
        valued = 'left_hand_landmarks'
        drawLeftHand(frame, results)
        drawRightHand(frame, results)
        # finding frame per seconds 
        endTime = time.time()
        second = endTime - startTime
        
        fps = frameCounter / second
        # showing the fps on the screen
        cv.putText(frame, f'FPS : {int(fps)}', (50,30), fonts, 0.8, GREEN, 2)

        #show the frame on the screen
        cv.imshow("frame", frame)
        
        # define the key to have a controll over the video, other operation
        key = cv.waitKey(1)
        
        # break the loop if q is pressed on the keyboard
        if key == ord('q'):
            break
# closing all the windows 
cv.destroyAllWindows()
# close the camera which was opened at first
camera.release()
    

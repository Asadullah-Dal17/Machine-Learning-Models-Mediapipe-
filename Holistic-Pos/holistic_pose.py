# Required Modules 
import mediapipe as mp
import cv2 as cv
import numpy as np
import Lib
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
YELLOW = (0, 255, 255)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
ORANGE = ( 255, 125, 0)
# create function
# objects 
camera = cv.VideoCapture(cameraID)

# mediapipe objects 
mpHolistic = mp.solutions.holistic

frameWidth = int(camera.get(3))
frameHeight = int(camera.get(4))


# video recording settings 

# fourcc = cv.VideoWriter_fourcc(* 'XVID')
# vidRecoder = cv.VideoWriter('output.mp4', fourcc, 10.0, (1280, 480))

# loading in the Models from mediapipe
with mpHolistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:

    # going through each frame comming from camera     
    while True:
        ret, frame = camera.read()
        frameCounter += 1
        
        mask = np.zeros((frame.shape), dtype=np.uint8)

        # converting frame frame BGR to RGB
        rgbframe = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        # getting the width, height and channels,
        height, width, channeles = rgbframe.shape
        
        rgbframe.flags.writeable = False
        
        results = holistic.process(rgbframe)
        # print(results.pose_landmarks)
        # drawLeftHand(frame, results)
        # drawRightHand(frame, results)
        if results.left_hand_landmarks:
            # print("True")
            # getting the hand points individual part of hand
            thumbLeft, indexLeft, middleLeft, ringLeft, pinkyLeft = Lib.getHandPoints(mask, results.left_hand_landmarks.landmark)
            # print(thumbLeft)
            # Calling hand point draw function 
            Lib.handDraw(mask, thumbLeft, GREEN, 2, True)
            Lib.handDraw(mask, indexLeft, RED, 2, True)
            Lib.handDraw(mask, middleLeft, BLUE,2, True, 4, (255,0, 244))
            Lib.handDraw(mask, ringLeft, YELLOW, 2,True, 4, (0,255,0) )
            Lib.handDraw(mask, pinkyLeft, ORANGE, 2, True)
            

        if results.right_hand_landmarks:
            # print("True")
            thumbRight, indexRight, middleRight, ringRight, pinkyRight = Lib.getHandPoints(mask, results.right_hand_landmarks.landmark)
            Lib.handDraw(mask, thumbRight, GREEN, 2, True)
            Lib.handDraw(mask, indexRight, RED, 2, True)
            Lib.handDraw(mask, middleRight, BLUE, 2, True)
            Lib.handDraw(mask, ringRight, YELLOW, 2, True)
            Lib.handDraw(mask, pinkyRight, ORANGE, 2, True)
        if results.pose_landmarks:
            Lib.PoseLandmarks(frame, results.pose_landmarks.landmark)
        #  finding frame per seconds 
        endTime = time.time()
        second = endTime - startTime
        
        fps = frameCounter / second
        # showing the fps on the screen
        cv.putText(frame, f'FPS : {int(fps)}', (50,30), fonts, 0.8, GREEN, 2)

        #show the frame on the screen
        combined = np.hstack([frame, mask])
        # print(combined.shape)
        cv.imshow("frame", combined)
        # Recode video 
        # vidRecoder.write(combined)
        # define the key to have a controll over the video, other operation
        key = cv.waitKey(1)
        
        # break the loop if q is pressed on the keyboard
        if key == ord('q'):

            break

    # vidRecoder.release()
    camera.release()
cv.destroyAllWindows()
# closing all the windows 

# close the camera which was opened at first


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

# objects 
camera = cv.VideoCapture(cameraID)
while True:
    ret, frame = camera.read()
    frameCounter += 1
    
    # converting frame frame BGR to RGB
    rgbframe = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
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
    
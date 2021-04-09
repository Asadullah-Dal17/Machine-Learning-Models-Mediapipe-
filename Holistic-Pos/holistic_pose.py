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
def drawLandmarks(image, landmark, colour=(0,255,0),radius=8):
    # option = [", "right_hand_landmarks"]
        # print(mpOut.op)
    linesPoints =[]
    for ID, marks in enumerate(landmark):
        # print(ID, "  ", marks)
        height, width, _ = image.shape
        pX, pY = int(width * marks.x), int(height * marks.y)
        cv.circle(image, (pX, pY), radius, colour, -1)
        linesPoints.append([pX, pY])



        # print(results.right_hand_landmarks.landmark[0])
        # n = len(landmark)
        # for j in range(0, n):
        #     print(j, "reversed", (j + 1) % n)
        #     x1, y1 = int(landmark[j].x * width), int(landmark[j].y * height)
        #     x2, y2 = int(landmark[(j + 1) % n].x *
        #                  width), int(landmark[(j + 1) % n].y * height)
            
        #     cv.line(image, (x1, y1), (x2, y2),BLUE, 1)

        cv.putText(image, f'{ID}', (pX, pY), fonts, 0.3, RED, 1)
    # print(linesPoints)
    # print(linesPoints[0:3])
    pts = np.array([linesPoints][0:4], np.int32)
    pts = pts.reshape((-1, 1, 2))
    # print(pts)
    # img = cv.polylines(image,[pts],False,(0,255,255))

# objects 
camera = cv.VideoCapture(cameraID)

# mediapipe objects 
mpHolistic = mp.solutions.holistic

frameWidth = int(camera.get(3))
frameHeight= int(camera.get(4))

# video recording settings 
# vidRecoder = cv.VideoWriter("OutResult.mp4", cv.VideoWriter_fourcc(*'XVID'), 10,(480, 1280) )
fourcc = cv.VideoWriter_fourcc(* 'XVID')
vidRecoder = cv.VideoWriter('output.mp4', fourcc, 10.0, (1280, 480))
# loading in the Models from mediapipe
with mpHolistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
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
            drawLandmarks(mask, results.left_hand_landmarks.landmark)
        if results.right_hand_landmarks:
            # print("True")
            drawLandmarks(mask, results.right_hand_landmarks.landmark, (255, 0, 255))
        # if results.pose_landmarks:
        #     drawLandmarks(mask, results.pose_landmarks.landmark)
        # # finding frame per seconds 
        endTime = time.time()
        second = endTime - startTime
        
        fps = frameCounter / second
        # showing the fps on the screen
        cv.putText(frame, f'FPS : {int(fps)}', (50,30), fonts, 0.8, GREEN, 2)


        #show the frame on the screen
        combined = np.hstack([frame, mask])
        # print(combined.shape)
        cv.imshow("frame", combined)
        # vidRecoder.write(combined)
        # define the key to have a controll over the video, other operation
        key = cv.waitKey(1)
        
        # break the loop if q is pressed on the keyboard
        if key == ord('q'):

            break

    vidRecoder.release()
    camera.release()
cv.destroyAllWindows()
# closing all the windows 

# close the camera which was opened at first


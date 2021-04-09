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
def getHandPoints(image, landmark, colour=(0,255,0),radius=2):
    # option = [", "right_hand_landmarks"]
        # print(mpOut.op)
    linesPoints = []
    # dicPoints = {}
    for ID, marks in enumerate(landmark):
        # print(ID, "  ", marks)
        
        height, width, _ = image.shape

        pX, pY = int(width * marks.x), int(height * marks.y)
        
        cv.circle(image, (pX, pY), radius, colour, -1)

        # updating hand points to the list 
        linesPoints.append((pX, pY))
        # dicPoints.update({ID: [pX, pY]})
        
        cv.putText(image, f'{ID}', (pX, pY), fonts, 0.3, RED, 1)
    # print(linesPoints)
    # print(tuple(linesPoints[0:4]))
    # cv.circle(image, tuple(linesPoints[0]), 6, (0, 255,255), 3)

    # print(dicPoints )
    thumb = linesPoints[1:5]
    indexFinger = linesPoints[5:9]
    middleFinger = linesPoints[9:13]
    ringFinger = linesPoints[13:17]
    pinkyFinger = linesPoints[17:21]
    # print(newPoints)
    # cv.circle(image, tuple(newPoints[0]), 6, (0, 255, 255), 3)
    # cv.circle(image, tuple(newPoints[1]), 6, (255, 255, 255), 3)
    # cv.circle(image, tuple(newPoints[2]), 6, (0, 25,255), 3)
    # pts = np.array([index], np.int32)
    # pts = pts.reshape((-1, 1, 2))
    # # print(pts)
    # print()
    # img = cv.polylines(image,[pts],False,(0,255,255),2)
    return thumb, indexFinger, middleFinger, ringFinger, pinkyFinger
def LinesFunc(image,listOfTuples, color, thickness):
        listOfList = list(map(list, listOfTuples))
        print(listOfList)
        pts = np.array([listOfList], np.int32)
        # pts = np.array([index], np.int32)
        pts = pts.reshape((-1, 1, 2))
        print(pts)
        # print()
        img = cv.polylines(image,[pts],False,color,3)
# objects 
camera = cv.VideoCapture(cameraID)

# mediapipe objects 
mpHolistic = mp.solutions.holistic

frameWidth = int(camera.get(3))
frameHeight= int(camera.get(4))

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
        
        rgbframe.flags.writeable = True
        
        results = holistic.process(rgbframe)
        # print(results.pose_landmarks)
        # drawLeftHand(frame, results)
        # drawRightHand(frame, results)
        if results.left_hand_landmarks:
            # print("True")
            thumbLeft, indexLeft, middleLeft, ringLeft, pinkyLeft = getHandPoints(mask, results.left_hand_landmarks.landmark)
            # print(thumbLeft)
            LinesFunc(mask, thumbLeft, GREEN, 2)

        if results.right_hand_landmarks:
            # print("True")
            getHandPoints(mask, results.right_hand_landmarks.landmark, (255, 0, 255))
        # if results.pose_landmarks:
        #     drawLandmarks(mask, results.pose_landmarks.landmark)
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


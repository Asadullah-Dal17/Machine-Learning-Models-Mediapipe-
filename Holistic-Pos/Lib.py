import cv2 as cv
import numpy as np
import mediapipe as mp 

# Getting hand points (Lnadmarks ) 
def getHandPoints(image, landmark, colour=(0,255,0),radius=2):
    # option = [", "right_hand_landmarks"]
        # print(mpOut.op)
    linesPoints = []
    for ID, marks in enumerate(landmark):
        # print(ID, "  ", marks)
        
        height, width, _ = image.shape

        pX, pY = int(width * marks.x), int(height * marks.y)
        
        # cv.circle(image, (pX, pY), radius, colour, -1)

        # updating hand points to the list 
        linesPoints.append((pX, pY))
        
        # cv.putText(image, f'{ID}', (pX, pY), fonts, 0.3, RED, 1)
    # print(linesPoints)
    # print(tuple(linesPoints[0:4]))
    # cv.circle(image, tuple(linesPoints[0]), 6, (0, 255,255), 3)

    # print(dicPoints )
    # dviding the list into different hand parts

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
# drawing the lines and circles on the hand 
def handDraw(image,listOfTuples, color, thickness,DrawCircle=False ,radius=5,circleColor=(255,255,255), CType=2 ):
        listOfList = list(map(list, listOfTuples))
        if DrawCircle == True:
            
            for points in listOfTuples:
                cv.circle(image, points, radius, circleColor, CType)
            # print(points)
        # print(listOfList)
        pts = np.array([listOfList], np.int32)
        # pts = np.array([index], np.int32)
        pts = pts.reshape((-1, 1, 2))
        # print(pts)
        # print()
        img = cv.polylines(image,[pts],False,color,3)



# TODO body landmarks detection (Create a function)
def PoseLandmarks(image, landmark):
    # print(landmark)
    FullBodyPoints = []
    for ID, marks in enumerate(landmark):
        # print(ID, "  ", marks)
        height, width, _ = image.shape
        Points = (int(marks.x * width), int(marks.y * height))
        # print(Points)
        FullBodyPoints.append(Points)
        # cv.circle(image, Points, 5, (255, 0, 255), 3)
        cv.putText(image, f'{ID}', Points, cv.FONT_HERSHEY_COMPLEX, 0.4, (125, 255,0), 1)

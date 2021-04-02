# importing required modules
import cv2 as cv
import mediapipe as mp
import time

# Variable
capID = 1
frame_count = 0
startTime = time.time()
fonts = cv.FONT_HERSHEY_COMPLEX
# objects
camera = cv.VideoCapture(capID)

while True:
  # starting frame counter
  frame_count += 1

  # read frame from the camera
  ret, frame = camera.read()

  # calculating the taken by total frame
  seconds = time.time() - startTime

  # calculating the frames per seconds FPS in short
  fps = frame_count / seconds

  # show the fps on the screen
  cv.putText(frame, f"FPS : {int(fps)}", (50, 20), fonts, 0.7, (0, 255, 255), 1)

  # show the frame on the screen
  cv.imshow("frame", frame)

  # define the key
  key = cv.waitKey(1)

  # break the loop if "q" is pressed on the keyboard
  if key == ord('q'):
    break

# close all the windows which has been create
cv.destroyAllWindows()
# close the camera
camera.release()

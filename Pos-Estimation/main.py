# importing required modules
import cv2 as cv
import mediapipe as mp
import time

# Variable
capID = 1
frame_count = 0
startTime = time.time()
fonts = cv.FONT_HERSHEY_COMPLEX

# colors BGR(BLUE GREEN RED) 
BLUE 	= (255,0,0)
GREEN 	= (0, 255, 0)
RED		= (0, 0, 255)
YELLOW 	=(0,255,255)
MAGENTA = (255, 0, 255)

# objects
camera = cv.VideoCapture(capID)

# Mdeda pipe objects 
mpPose = mp.solutions.pose

with mpPose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
	
	while True:
	# starting frame counter
		frame_count += 1

		# read frame from the camera
		ret, frame = camera.read()
		if not ret:
			print("if camera is loaded")
			break
		# converting BGR to RGB frame 
		RGB_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
		
		# findig frame height and width  of frame 
		height, width , channels = frame.shape # since frame is np array, shape attribute provide us height width, number channeles in image(depth)

		frame.flags.writeable = False
		
		# detection the pos
		resultsOut = pose.process(RGB_frame)

		# check if pose is detect or not 
		# print(resultsOut.pose_landmarks)
		if resultsOut.pose_landmarks:
			linePoints =[]
			# finding landmarks coordinates and ID of each landmark
			for ID, lMark in enumerate(resultsOut.pose_landmarks.landmark):
				# linePoints.append
				print(f"id {ID}   Values {lMark}")
			
				# converting normallied values in the pixels
				Px, Py = int(lMark.x * width), int(lMark.y * height)
				linePoints.append((Px, Py))


				cv.putText(frame, f"{ID}", (Px, Py), fonts, 0.5, YELLOW, 1)
			print(linePoints)

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

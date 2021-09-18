import cv2 as cv
import time 
import Lib

# Variable 
startingTime = time.time()
frameCounter = 0
fonts = cv.FONT_HERSHEY_COMPLEX
#colours
YELLOW = (0,255,255)
CYAN = (255,255,0)
MAGENTA =(255,0,255)
GOLDEN = (32,218,165)
LIGHT_BLUE = (255,30,144)
PURPLE = (128,0,128)
CHOCOLATE = (30,105,210)
PINK = (147,20,255)
ORANGE = (0,69,255)
# objects
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands
# initiations of camera  object
camera =cv.VideoCapture(0)
# camera.set(cv.CAP_PROP_FRAME_WIDTH, 320*3)
# camera.set(cv.CAP_PROP_FRAME_HEIGHT,240*3)
detector =Lib.handDetector()
while True:
	# Staring frame counter
	frameCounter += 1
	ret, frame = camera.read()
	# RGB_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
	image = detector.getHandLandmarks(frame)

		# RGB_frame.flags.writeable =False
		# get results from hand pos estimator
		# results =hands.process(RGB_frame)
		#
		# RGB_frame.flags.writeable =True
		#
		# if results.multi_hand_landmarks:
		# 	# print("land marks are detected")
		# 	for handLandMarks in(results.multi_hand_landmarks):
		# 		# print(len(handMarks))
		# 		for ID,Mark in enumerate(handLandMarks.landmark):
		# 			height, width, _ =frame.shape
		# 			pX,pY ,pZ= int(Mark.x* width), int(Mark.y* height), int(Mark.z* 100)
		# 			print(pX,pY, pZ)
		#
		# 		mp_drawing.draw_landmarks(frame, handLandMarks, mp_hands.HAND_CONNECTIONS)
		# 		# print(IDs)
				

				
	endingTime = time.time() - startingTime
	framePerSeconds = frameCounter/endingTime
	# print(framePerSeconds)
	cv.putText(frame, f"FPS: {round(framePerSeconds,2)}", (20, 30), fonts, 0.7, GOLDEN, 2)
	# cv.imshow('RGB_frame', RGB_frame)
	cv.imshow('frame', frame )
	key = cv.waitKey(1)
	if key ==ord('q'):
		break
camera.release()
cv.destroyAllWindows()
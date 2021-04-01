
import cv2
import mediapipe as mp
import time 
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
FramesCount =0
startTime = time.time()
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 15.0, (640, 480))
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    FramesCount +=1
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue
    # print(cap.get(cv2.CAP_PROP_FPS))
    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = pose.process(image)
    endTime = time.time()
    Second = endTime - startTime
    fps = FramesCount / Second
    print(fps)
    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    cv2.putText(image, f'FPS : {int(fps)}', (50,50),cv2.FONT_HERSHEY_COMPLEX, 0.6,(0,255,255), 2 )
    cv2.imshow('MediaPipe Pose', image)
    out.write(image)
    if cv2.waitKey(1) & 0xFF == 27:
      break
cap.release()
out.release()
cv2.destroyAllWindows()

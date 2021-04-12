# Hand Pose Estimation
This code detects the hands landmarks and draw on the screen, in the end I will provide you a demo, controlling RGB LED with Gesture,
we will be using Arduino controller to the hardware. 

## TODO

- [x] find hands landmarks
- [x] create function which allow to draw the landmarks
- [ ] Visual The hand landmarks on mask
- [ ] This code will provide list for hand landmarks, that can be easily assessed.
- [ ] control the colour of RGB LED with and Gesture Recognitions.

## Gesture Recognition
I am going to recognize the following gestures, on based of different gestures, I will try to control the colors of RGB LED.
idea will to send RGB values to LED using Arduino (MicroController), we will communicate with arduino using Library called PySerial, how can you communicate with Microcontroller (Arduino) check this Repository out

1. :ok_hand:
2. :v:
3. :love_you_gesture:
4. :call_me_hand:
5. :crossed_fingers:
6. :metal:

I will create complete video on that if you are interested checkout my youtube channel [**AiPhile**](https://www.youtube.com/c/aiphile)


## Hand Landmarks

![Hand landmarks](https://google.github.io/mediapipe/images/mobile/hand_landmarks.png)


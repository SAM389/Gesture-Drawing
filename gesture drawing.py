# imports
import cv2
import numpy as np
import mediapipe as mp
from collections import deque


# different arrays to handle colour points of different colour
vpoints = [deque(maxlen=1024)]
ipoints = [deque(maxlen=1024)]
bpoints = [deque(maxlen=1024)]
gpoints = [deque(maxlen=1024)]
ypoints = [deque(maxlen=1024)]
opoints = [deque(maxlen=1024)]
rpoints = [deque(maxlen=1024)]


# mark the points in particular arrays of specific colours
violet_index = 0
indigo_index = 0
blue_index = 0
green_index = 0
yellow_index=0
orange_index=0
red_index=0

#The kernel to be used for dilation purpose
kernel = np.ones((6,6),np.uint8)

colors = [(211, 0, 148), (130, 0, 75), (255, 0, 0), (0, 255, 0), (0,255,255),(0,127,255),(0,0,255)]
colorIndex = 0

# code for Canvas setup
paintWindow = np.zeros((720,1280,3)) + 255
paintWindow = cv2.rectangle(paintWindow, (40,1), (140,65), (0,0,0), 2)
paintWindow = cv2.rectangle(paintWindow, (160,1), (255,65), (211, 0, 148), 2)
paintWindow = cv2.rectangle(paintWindow, (275,1), (370,65), (130, 0, 75), 2)
paintWindow = cv2.rectangle(paintWindow, (390,1), (485,65), (255, 0, 0), 2)
paintWindow = cv2.rectangle(paintWindow, (505,1), (600,65), (0, 255, 0), 2)
paintWindow = cv2.rectangle(paintWindow, (615,1), (725,65), (0,255,255), 2)
paintWindow = cv2.rectangle(paintWindow, (735,1), (845,65), (0,127,255), 2)
paintWindow = cv2.rectangle(paintWindow, (855,1), (965,65), (0,0,255), 2)


cv2.putText(paintWindow, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "VIOLET", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "INDIGO", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "BLUE", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "GREEN", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "YELLOW", (620, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "ORANGE", (730, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "RED", (870, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)


# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.8, max_num_hands=1)
mpDraw = mp.solutions.drawing_utils


# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # Screen Resolution settings
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
ret = True
while ret:
    # Read each frame from the webcam
    ret, frame = cap.read()

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame = cv2.rectangle(frame, (40,1), (140,65), (0,0,0), 2)
    frame = cv2.rectangle(frame, (160,1), (255,65), (211, 0, 148), 2)
    frame = cv2.rectangle(frame, (275,1), (370,65), (130, 0, 75), 2)
    frame = cv2.rectangle(frame, (390,1), (485,65), (255, 0, 0), 2)
    frame = cv2.rectangle(frame, (505,1), (600,65), (0, 255, 0), 2)
    frame = cv2.rectangle(frame, (615,1), (725,65), (0,255,255), 2)
    frame = cv2.rectangle(frame, (735, 1), (845, 65), (0,127,255), 2)
    frame = cv2.rectangle(frame, (855, 1), (965, 65), (0,0,255), 2)

    cv2.putText(frame, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "VIOLET", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "INDIGO", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (620, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "ORANGE", (730, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "RED", (870, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)

    # Get hand landmark prediction
    result = hands.process(framergb)

    # post process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * 1280)
                lmy = int(lm.y * 720)

                landmarks.append([lmx, lmy])


            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
        fore_finger = (landmarks[8][0],landmarks[8][1])
        center = fore_finger
        thumb = (landmarks[4][0],landmarks[4][1])
        cv2.circle(frame, center, 3, (0,255,0),-1)
        print(center[1]-thumb[1])
        if (thumb[1]-center[1]<30):
            vpoints.append(deque(maxlen=512))
            violet_index += 1
            ipoints.append(deque(maxlen=512))
            indigo_index += 1
            bpoints.append(deque(maxlen=512))
            blue_index += 1
            gpoints.append(deque(maxlen=512))
            green_index += 1
            ypoints.append(deque(maxlen=512))
            yellow_index += 1
            opoints.append(deque(maxlen=512))
            orange_index += 1
            rpoints.append(deque(maxlen=512))
            red_index += 1


        elif center[1] <= 65:
            if 40 <= center[0] <= 140: # Clear Button
                vpoints = [deque(maxlen=512)]
                ipoints = [deque(maxlen=512)]
                bpoints = [deque(maxlen=512)]
                gpoints = [deque(maxlen=512)]
                ypoints = [deque(maxlen=512)]
                opoints = [deque(maxlen=512)]
                rpoints = [deque(maxlen=512)]

                violet_index = 0
                indigo_index = 0
                blue_index = 0
                green_index = 0
                yellow_index=0
                orange_index=0
                red_index=0

                paintWindow[67:,:,:] = 255
            elif 160 <= center[0] <= 255:
                    colorIndex = 0 # violet
            elif 275 <= center[0] <= 370:
                    colorIndex = 1 # indigo
            elif 390 <= center[0] <= 485:
                    colorIndex = 2 # blue
            elif 505 <= center[0] <= 600:
                    colorIndex = 3 # green
            elif 615 <= center[0]<= 715:
                    colorIndex = 4 #yellow
            elif 725 <= center[0] <= 830:
                    colorIndex = 5  # orange
            elif 835 <= center[0] <= 945:
                colorIndex = 6  # red

        else :
            if colorIndex == 0:
                vpoints[violet_index].appendleft(center)
            elif colorIndex == 1:
                ipoints[indigo_index].appendleft(center)
            elif colorIndex == 2:
                bpoints[blue_index].appendleft(center)
            elif colorIndex == 3:
                gpoints[green_index].appendleft(center)
            elif colorIndex == 4:
                ypoints[yellow_index].appendleft(center)
            elif colorIndex == 5:
                opoints[orange_index].appendleft(center)
            elif colorIndex == 6:
                rpoints[red_index].appendleft(center)
    # Append the next dequeue when nothing is detected to avoids messing up
    else:
        vpoints.append(deque(maxlen=512))
        violet_index += 1
        ipoints.append(deque(maxlen=512))
        indigo_index += 1
        bpoints.append(deque(maxlen=512))
        blue_index += 1
        gpoints.append(deque(maxlen=512))
        green_index += 1
        ypoints.append(deque(maxlen=512))
        yellow_index += 1
        opoints.append(deque(maxlen=512))
        orange_index += 1
        rpoints.append(deque(maxlen=512))
        red_index += 1

    # Draw lines of all the colors on the canvas and frame
    points = [vpoints, ipoints, bpoints, gpoints,ypoints,opoints,rpoints]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 2)
                cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 2)

    cv2.imshow("Output", frame)
    cv2.imshow("Paint", paintWindow)

    if cv2.waitKey(1) == ord('q'):
        break

# release webcam and destroy all active windows
cap.release()
cv2.destroyAllWindows()
import cv2
import mediapipe as mp
import numpy as np
import pyautogui

import HandTrackingModule as htm
import time
import pyautogui

####################

pyautogui.FAILSAFE = True

####################
cam = 0
wCam, hCam = 640, 480

frameR = 100
smoothening = 5

####################

pTime, cTime = 0 , 0
pX,pY = 0, 0
cX,cY = 0, 0
wScr, hScr = pyautogui.size()

cap = cv2.VideoCapture(cam)

cap.set(3,wCam)
cap.set(4,hCam)

detector = htm.HandTracker(maxHands=1)

# print(wScr,hScr)

while True:
    success, img = cap.read()

    img = detector.findHands(img)

    lmList, bbox = detector.findPosition(img)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # print(x1,y1, x2, y2)
        fingers = detector.fingersUp()
        # print(fingers)

        cv2.rectangle(img,(frameR,frameR), (wCam - frameR, hCam-frameR), (255,0,0),2)
        if fingers[1] == 1 and sum(fingers) == 1:

            x3 = np.interp(x1, (frameR, wCam -frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam -frameR), (0, hScr))

            cX = pX + (x3 - pX)/smoothening
            cY = pY + (y3 - pY)/smoothening

            pyautogui.moveTo(wScr - cX,cY)
            cv2.circle(img, (x1, y1), 14, (255, 0, 255), cv2.FILLED)
            pX,pY = cX, cY

        elif fingers[1] == 1 and fingers[2] == 1 and sum(fingers) == 2:
            length, img, lineInfo = detector.findDistance(8,12,img)
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 14, (0, 255, 0), cv2.FILLED)
                # time.sleep(0.1)
                pyautogui.click()

        elif sum(fingers) == 5:
            pyautogui.press('space')


    cTime = time.time()
    fps = 1/ (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)),(10, 70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0))

    cv2.imshow("Image",img)
    cv2.waitKey(1)
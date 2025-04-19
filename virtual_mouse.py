import cv2
import cvzone
import HandTrackingModule as htm
import time
import numpy as np
import autopy as ap
import pynput as p
from pynput.mouse import Button,Controller
frameR = 100
smoothening = 7
plocX, plocY = 0, 0
clocX, clocY = 0, 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector(maxHands=1)
pTime = 0
wCam, hCam = 640, 480
wScr, hScr = ap.screen.size()
while True:
     # 1. Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList,bbox = detector.findPosition(img,draw=False)
    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]
        # 3. Check which fingers are up
        fingers = detector.fingerUp()
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 25,25), 2)
        # print(fingers)
        # 4. Only Index Finger : Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:
        # 5. Convert Coordinates
            x3= np.interp(x1,(frameR, wCam - frameR),(0,wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
         # 6. Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening
            # 7. Move Mouse
            ap.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 10, (255, 25,25), cv2.FILLED)
            plocX, plocY = clocX, clocY
        # 8. Both Index and middle fingers are up : Clicking Mode(left click)
        if fingers[1] == 1 and fingers[2] == 1:
             # 9. Find distance between fingers
            l,img,_ = detector.findDis(8,12,img,draw=False)
            print(l)
            # 10. Click mouse if distance short
            if l<30:
                cv2.circle(img, ((x1+x2)//2, (y1+y2)//2), 10, (186, 66, 45), cv2.FILLED)
                ap.mouse.click()
        # 11.right click        
        if  fingers[0] == 1 and fingers[1]==1 and fingers[2] == 1 and fingers[3]==1 and fingers[4]==1:
            mouse = Controller()
            mouse.click(Button.right, 1)
    # 12. showing Instructions
    if bbox:
        cv2.putText(img,'* BRING INDEX & MIDDLE FINGER CLOSER FOR DOUBLE CLICK',(20,40),cv2.FONT_HERSHEY_PLAIN, 1.20,(0, 25,25), 2,)
        cv2.putText(img,'* OPEN HAND FOR RIGHT CLICK',(20,60),cv2.FONT_HERSHEY_PLAIN, 1.40,(0, 25,25), 2,)
    else:
        cv2.putText(img,'SHOW INDEX FINGER FOR POINTING',(20,40),cv2.FONT_HERSHEY_PLAIN, 1.50,(0, 25,25), 2,)
     # 13. Display
    cv2.imshow("VIRTUAL MOUSE", img)
   
    if cv2.waitKey(1) & 0xFF == 27:
        exit()

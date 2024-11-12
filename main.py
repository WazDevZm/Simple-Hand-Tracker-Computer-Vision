##Simple Hand Tracking App
##Developed by : Wazingwa Mugala
import cvzone
import mediapipe
import cv2
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)


while True:
    success, img = cap.read()
    img = cv2.flip (img, 1)
    
    detector.findHands(img, flipType=False)
    
    
    cv2.imshow("Hand-Tracker App", img)
    cv2.waitKey(1)
    

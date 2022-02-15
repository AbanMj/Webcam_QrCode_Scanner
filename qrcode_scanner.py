import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        print("Data", obj.data)
        
        cv2.putText(frame, str(obj.data),  (10, 50), font, 1,
                   (2, 1, 1), 1)


    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    if key == ord('1'):
       break

    
        
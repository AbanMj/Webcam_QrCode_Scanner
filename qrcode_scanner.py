
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import datetime

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
e = datetime.datetime.now()
while True:
    _, frame = cap.read()

    BarCode = pyzbar.decode(frame)

    for obj in BarCode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        # box size
        pts = pts.reshape((-1, 1, 2))
        thickness = 2
        isClosed = True
        # fill color (border)
        line_color = (0, 0, 255)
        cv2.polylines(frame, [pts], isClosed, line_color, thickness)
        
        BarCodeData = obj.data.decode("utf-8")
        the_text = "Data: " + str(BarCodeData)
        
        #text in the video/screen
        cv2.putText(frame, the_text,  (10, 430), font, 1,
                   (0,255,255), 1, lineType=1)
        cv2.putText(frame, e.strftime("Date & Time:  %a, %b %d, %Y    %I:%M:%S %p"), (10,450),
                    font, 1, (0,255,255), 1, lineType=1 )
        
        print("Data: " + BarCodeData + e.strftime("   Date & Time: %a, %b %d, %Y   %I:%M:%S %p"))

    cv2.imshow("WebCam QrCode Scanner", frame)
    
    key = cv2.waitKey(1)
    if key == ord('a'):
       break

    
        
import os
import sys
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import datetime

print ("\nProgram: Contact Tracing App.")
while True:
        start = input("Enter 'a' to start the program. \nCapital 'Q' to exit.  ").lower()
        if start[0] == 'q': 
            print ("The program is closing.")
            sys.exit()
        elif start[0] == 'a':
            print ("The WebCam QrCode Scanner is starting..... \nPlace the qr code infront of your Webcam" )
            break
        
def webcam_scanner():
    camera = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_PLAIN
    Date_scanned = datetime.datetime.now()
    counter=0      

    while True:
        _, frame = camera.read()

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
        
            Data = obj.data.decode("utf-8")
           
        #text in the video/screen
            cv2.putText(frame, Date_scanned.strftime("Date:  %a, %b %d, %Y" " Time:  %I:%M:%S %p"), (10,450),
                    font, 1, (0,255,255), 1, lineType=1 )

        if BarCode:                                                             
            current_date = date_and_time()                                
            qr_code = Data                               
            print("--- QR Code Scanned ---\n" + qr_code + "\n")      
            counter = create_txt(qr_code, counter, current_date)

        cv2.imshow("WebCam QrCode Scanner", frame)
    
        key = cv2.waitKey(1)
        if key == ord('Q'):
            print ("\nScanning Complete.\n")
        
            os.startfile('Traze_Me.txt') 
            break
    camera.release()
    cv2.destroyAllWindows()

def date_and_time():      
    Date_today = datetime.datetime.now()    

    Date_today.strftime("Date:  %a, %b %d, %Y" " Time:  %I:%M:%S %p")

    current_date= (Date_today.strftime("Date:  %a, %b %d, %Y" " Time:  %I:%M:%S %p"))
    return current_date

def create_txt(qr_code, counter, current_date):                       
    try:                                                           
        if counter == 0:                                         
            file = open("Traze_Me.txt","w")                       
            file.write(qr_code + "\n" + current_date +"\n\n")                       
            counter  =+ 1
        else:                                                      
            file = open('Traze_Me.txt', 'r')                         
            repeat = file.read().find(qr_code)                      
            if repeat != -1:                                        
                print("-  QR CODE ALREADY SCANNED -\n")
            else:                                                  
                file = open("Traze_Me.txt","a")                       
                file.write(qr_code + "\n" + current_date +"\n\n")         
        return counter   

    finally:
        file.close()    

def main():
    webcam_scanner()

if __name__ == "__main__":
	main()  
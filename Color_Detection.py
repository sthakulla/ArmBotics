
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import imutils
import numpy as np

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)
# capture frames from the camera


for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	frame = image.array
	# show the frame
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    	lower_yellow = np.array([25, 70, 120])
    	upper_yellow = np.array([30, 255, 255])

   	lower_green = np.array([40, 7,80])
    	upper_green = np.array([70, 255,255])

    	lower_red = np.array([0, 50,120])
    	upper_red = np.array([10, 255,255])


    	lower_blue = np.array([90, 60,0])
    	upper_blue = np.array([121, 255,255])

    	mask1 = cv2.inRange(hsv, lower_yellow, upper_yellow)
    	mask2 = cv2.inRange(hsv, lower_green, upper_green)
   	mask3 = cv2.inRange(hsv, lower_red, upper_red)
    	mask4 = cv2.inRange(hsv, lower_blue, upper_blue)

    	cnts1 = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    	cnts1 = imutils.grab_contours(cnts1)

    	cnts2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cnts2 = imutils.grab_contours(cnts2)

	cnts3 = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cnts3 = imutils.grab_contours(cnts3)

	cnts4 = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cnts4 = imutils.grab_contours(cnts4)

	for c in cnts1:
		area1 = cv2.contourArea(c)
		if area1 > 5000:

		    cv2.drawContours(frame, [c], -1, (0,255,0), 3)
		    M=cv2.moments(c)

		    cx = int(M["m10"] / M["m00"])
		    cy = int(M["m01"] / M["m00"])
		    cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
		    cv2.putText(frame, "Yellow", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)

	for c in cnts2:
		area2 = cv2.contourArea(c)
		if area2 > 5000:
		    cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
		    M = cv2.moments(c)

		    cx = int(M["m10"] / M["m00"])
		    cy = int(M["m01"] / M["m00"])

		    cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
		    cv2.putText(frame, "Green,", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)

	    for c in cnts3:
		area3 = cv2.contourArea(c)
		if area3 > 5000:
		    cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
		    M = cv2.moments(c)

		    cx = int(M["m10"] / M["m00"])
		    cy = int(M["m01"] / M["m00"])

		    cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
		    cv2.putText(frame, "red", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)

	    for c in cnts4:
		area4 = cv2.contourArea(c)
		if area4 > 5000:
		    cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
		    M = cv2.moments(c)

		    cx = int(M["m10"] / M["m00"])
		    cy = int(M["m01"] / M["m00"])

		    cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
		    cv2.putText(frame, "blue", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)

	   cv2.imshow("result", frame)

	   key = cv2.waitKey(1) & 0xFF
		# clear the stream in preparation for the next frame
		rawCapture.truncate(0)
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break

cv2.destroyAllWindows()
	
        
        
        
        
        
        
        
'''
# Source: https://www.youtube.com/watch?v=nty0zSKB4_k

# import the necessary packages
import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([25, 70, 120])
    upper_yellow = np.array([30, 255, 255])

    lower_green = np.array([40, 7,80])
    upper_green = np.array([70, 255,255])

    lower_red = np.array([0, 50,120])
    upper_red = np.array([10, 255,255])


    lower_blue = np.array([90, 60,0])
    upper_blue = np.array([121, 255,255])

    mask1 = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask2 = cv2.inRange(hsv, lower_green, upper_green)
    mask3 = cv2.inRange(hsv, lower_red, upper_red)
    mask4 = cv2.inRange(hsv, lower_blue, upper_blue)

    cnts1 = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts1 = imutils.grab_contours(cnts1)

    cnts2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts2 = imutils.grab_contours(cnts2)

    cnts3 = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts3 = imutils.grab_contours(cnts3)

    cnts4 = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts4 = imutils.grab_contours(cnts4)

    for c in cnts1:
        area1 = cv2.contourArea(c)
        if area1 > 5000:

            cv2.drawContours(frame, [c], -1, (0,255,0), 3)
            M=cv2.moments(c)

            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Yellow", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)

    for c in cnts2:
        area2 = cv2.contourArea(c)
        if area2 > 5000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            M = cv2.moments(c)

            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Green,", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)

    for c in cnts3:
        area3 = cv2.contourArea(c)
        if area3 > 5000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            M = cv2.moments(c)

            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "red", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)

    for c in cnts4:
        area4 = cv2.contourArea(c)
        if area4 > 5000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            M = cv2.moments(c)

            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "blue", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)

    cv2.imshow("result", frame)

    k = cv2.waitKey(5)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
'''

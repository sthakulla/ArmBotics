# only for camera test
import cv2
import numpy as np


#different function for Video capture depends on machine used
cap = cv2.VideoCapture(0)#test with camera, para=0
#cap = cv2.VideoCapture('video.avi') #load from file 
#set resulotion to 800*600
cap.set(3,800)
cap.set(4,600) 
# cap.get(3) check width and height of frame
#cap.get(4) 

while True:
# while (cap.isOpened()):
#returns a bool (True/False). If frame is read correctly, it will be True. So you can check end of the video by checking this return value.
    ret, frame = cap.read() #
    #if ret == True:
    main_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("Frame", frame)
     # Red color
    low_red = np.array([150, 155, 84])
    high_red = np.array([180, 255, 255])
    red_mask = cv2.inRange(main_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    
    cv2.imshow("Red", red)
    # Blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([125, 255, 255])
    blue_mask = cv2.inRange(main_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)# bitwise_and(sr1,scr2,dst) dst= outpyt array that have the same size as input array, for extract
    cv2.imshow("Blue", blue)
    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([100, 255, 255])
    green_mask = cv2.inRange(main_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    cv2.imshow("Green", green)

    low_yellow = np.array([20, 75, 115])
    high_yellow = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(main_frame, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)
    cv2.imshow("Yellow", yellow)

    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([180, 255, 255])
    mask = cv2.inRange(main_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Result", result)
    key = cv2.waitKey(1)
    if cv2.waitKey(20) & 0xFF == ord('q'):    
        break

# release capture when verything is done
cap.release()
cv2.destroyAllWindows()



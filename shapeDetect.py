import cv2

import numpy as np

from picamera.array import PiRGBArray

from picamera import PiCamera

import time



camera = PiCamera()

camera.resolution = (640, 480)

camera.framerate = 32

rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup

time.sleep(0.1)

# capture frames from the camera

def getContours(img):

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2:]

    for cnt in contours:

        area = cv2.contourArea(cnt)

        print(area)

        if area > 500:

            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)

            peri = cv2.arcLength(cnt, True)

            # print(peri)

            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            print(len(approx))

            objCor = len(approx)

            x, y, w, h = cv2.boundingRect(approx)



            if objCor == 3:

                objectType = "Tri"

            elif objCor == 4:

                aspRatio = w / float(h)

                if aspRatio > 0.98 and aspRatio < 1.03:

                    objectType = "Square"

                else:

                    objectType = "Rectangle"

            elif objCor > 4:

                objectType = "Circle"

            else:

                objectType = "None"



            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.putText(imgContour, objectType,

                        (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7,

                        (0, 0, 0), 2)





for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    # grab the raw NumPy array representing the image, then initialize the timestamp

    # and occupied/unoccupied text

    frame = image.array
    imgContour = frame.copy()

    # show the frame

    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)

    imgCanny = cv2.Canny(imgBlur, 100, 100)

    getContours(imgCanny)

    cv2.imshow("result", imgContour)
    key = cv2.waitKey(1) & 0xFF

    

        # clear the stream in preparation for the next frame

    rawCapture.truncate(0)

        # if the `q` key was pressed, break from the loop

    if key == ord("q"):

        break



cv2.destroyAllWindows()



import cv2
import numpy as np
#######################################################################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier(r"C:\Users\Bushra Ansari\PycharmProjects\OpencvPython\pictures\haarcascade_russian_plate_number.xml")
minArea = 500
color = (255, 0, 255)
########################################################################

cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0

while True :
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea :
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, "Number Plate", (x, y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y : y+h, x : x+w] #Cropping Region of Interest
            cv2.imshow("ROI", imgRoi)


    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord("s") :
        cv2.imwrite("pictures/Scanned/NoPlate_" + str(count) +".jpg", imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX, 2,
                    (0, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(60)
        count +=1




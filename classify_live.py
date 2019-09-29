import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("cant open camera")
    exit()

while True:
    ret,image = cap.read()
    if not ret:
        print("cant receive frame")
        break;
    grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
     
    faces = face_cascade.detectMultiScale(grayImage)
     
    #print (type(faces))
     
    if len(faces) == 0:
        print ("No faces found")
     
    else:
        print (faces)
        print(faces.shape)
        print ("Number of faces detected: " + str(faces.shape[0]))
     
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)
     
        cv2.rectangle(image, ((0,image.shape[0] -25)),(270, image.shape[0]), (255,255,255), -1)
        cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0,image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
     
        cv2.imshow('Image with faces',image)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
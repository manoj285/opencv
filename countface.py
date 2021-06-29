import cv2
import numpy as np
import dlib

# connect to default camera so use 0
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1) #capture frame by frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    # counter to count no of faces
    i = 0
    for face in faces:
        x, y = face.left(),face.top
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame,(x,y), (x1,y1), (0,255,0), 2)# get co-ordinates
        i+=1
        cv2.putText(frame,'face' + str(i), (x-10,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,0,255),2)
        print(face,i)
    cv2.imshow('frame',frame)
    if cv2.waitkey(1)&0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
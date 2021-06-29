import cv2

cap = cv2.VideoCapture(0)
cap.set(2,640)
cap.set(2,480)

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    

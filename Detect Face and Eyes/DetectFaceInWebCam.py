import cv2

facedatabase = cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")
eyesdatabse = cv2.CascadeClassifier("Haarcascades/haarcascade_eye.xml")
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedatabase.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )
    if faces == ():
        continue
    else:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            roi_gray=gray[y:y+h,x:x+w]
            roi_frame=frame[y:y+h,x:x+w]
            eyes=eyesdatabse.detectMultiScale(roi_gray,scaleFactor=1.2,minNeighbors=7)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_frame,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)


    cv2.imshow('Video', frame)
    if cv2.waitKey(1)  == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

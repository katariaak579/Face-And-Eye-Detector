import cv2
from cv2 import COLOR_BGR2GRAY

facedatabase=cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")
eyedatabase=cv2.CascadeClassifier("Haarcascades/haarcascade_eye.xml")

img = cv2.imread("Add Image Path here")
gray=cv2.cvtColor(img,COLOR_BGR2GRAY)

faces=facedatabase.detectMultiScale(gray,scaleFactor=1.35,minNeighbors=5)

if faces == ():
    print("No Faces Detected")

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
    roi_gray=gray[y:y+h,x:x+w]
    roi_color=img[y:y+h,x:x+h]
    # roi_gray=cv2.resize(roi_gray,None,fx=2,fy=2,interpolation=cv2.INTER_LANCZOS4)
    eyes=eyedatabase.detectMultiScale(roi_gray,scaleFactor=1.275,minNeighbors=7)
    #roi_gray=cv2.resize(roi_gray,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LANCZOS4)

    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),3)

cv2.imshow("Image To Detect Faces And Eyes",img)
cv2.waitKey(0)

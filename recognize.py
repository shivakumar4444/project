import cv2 

import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');


# capture frames from a camera 
cap = cv2.VideoCapture(0);
recognizer=cv2.createLBPHFaceRecognizer();
recognizer.load("training\\datatraining.yml")
id=0
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,4,1,1,4)
# loop runs if capturing has been initialized.
while 1:
    ret, img = cap.read() # reads frames from a camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5);
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,configuration=recognizer.predict(gray[y:y+h,x:x+w])
        if(id==1):
            id="shiva"
        elif(id==2):
            id="malli"
        elif(id==3):
            id="vamsi"
        else:
            id="new"
        cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
    cv2.imshow('img',img)
    if(cv2.waitKey(1)==ord('q')):
        break;
# Close the window
cap.release() 

# De-allocate any associated memory usage 
cv2.destroyAllWindows() 

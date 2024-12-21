import cv2 

import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');


# capture frames from a camera 
cap = cv2.VideoCapture(0);
id=raw_input('enter id for face')
extensionnumber=100;
# loop runs if capturing has been initialized.
while 1:
    ret, img = cap.read() # reads frames from a camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5);
    for (x,y,w,h) in faces:
        extensionnumber=extensionnumber+1;
        cv2.imwrite("faces/id."+str(id)+"."+str(extensionnumber)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(300);
    cv2.imshow('img',img)
    cv2.waitKey(1);
    if(extensionnumber>200):
        break
    
# Close the window 
cap.release() 

# De-allocate any associated memory usage 
cv2.destroyAllWindows() 

import cv2 

import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 




# capture frames from a camera 
cap = cv2.VideoCapture(0) 

# loop runs if capturing has been initialized. 
while 1: 

	# reads frames from a camera 
	ret, img = cap.read() 

	# convert to gray scale of each frames 
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

	# Detects faces of different sizes in the input image 
	faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

	for (x,y,w,h) in faces: 
		# To draw a rectangle in a face 
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
	cv2.imshow('img',img) 

	# Wait for Esc key to stop 
	k = cv2.waitKey(30) & 0xff
	if k == 27:  
		break

# Close the window 
cap.release() 

# De-allocate any associated memory usage 
cv2.destroyAllWindows() 

#we need to extract faces from folder so we need os lib
import os
import cv2
import numpy as np
from PIL import Image
path="faces" #path for images
recognizer=cv2.createLBPHFaceRecognizer();
def getimagefrompathwithid(path):
    imagepaths=[os.path.join(path,var) for var in os.listdir(path)]
    ids=[]
    faces=[]
    for imagepath in imagepaths:
        #intially open the image with using path which are available in imagepaths list
        #and convert into grey scale image
        faceimg=Image.open(imagepath).convert('L');
        #cv2 only works with numpy so images converted to numpy array
        facenumpyarray=np.array(faceimg,'uint8')
        id=int(os.path.split(imagepath)[-1].split('.')[1])
        faces.append(facenumpyarray)
        ids.append(id)
        cv2.imshow("training",facenumpyarray)
        cv2.waitKey(50)
    return np.array(ids),faces
ids,faces=getimagefrompathwithid(path)
recognizer.train(faces,ids)
recognizer.save('training/datatraining.yml')
cv2.destroyAllWindows()

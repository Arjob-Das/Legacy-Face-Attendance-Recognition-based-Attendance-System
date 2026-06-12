import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import  storage
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-44242-default-rtdb.firebaseio.com/",
    'storageBucket': "face-recognition-44242.appspot.com"
})

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath) #list of image file names
print(pathList)
imgList = []
studentIds = []
for path in pathList: #path contains each image name
    imgList.append(cv2.imread(os.path.join(folderPath, path)))  #joining folderPath and path to create the image path with name
    #"Images/100.jpg"
    studentIds.append(os.path.splitext(path)[0]) #appending the path without extension as name of image is studentid itself

    fileName = f'{folderPath}/{path}' #creating formatted string that containst the image directory with image name
    bucket = storage.bucket() #creating a storage bucket of firebase
    blob = bucket.blob(fileName) #creating blob type variable (datatype for storing images in database) to store image
    
    #in the database
    blob.upload_from_filename(fileName) #uploading image 

    # print(path)
    # print(os.path.splitext(path)[0])
print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0] 
        #encoding and storing so that it can be matched with the live feed from webcam
        #print(encode)
        encodeList.append(encode)

    return encodeList


print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
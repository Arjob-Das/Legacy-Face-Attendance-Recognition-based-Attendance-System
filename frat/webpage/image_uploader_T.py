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

cred = credentials.Certificate("serviceAccountKey2.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': "https://teacherid-f3bdd-default-rtdb.firebaseio.com/",
    'storageBucket': "teacherid-f3bdd.appspot.com"
})

# Importing student images
folderPath = 'ImagesT'
pathList = os.listdir(folderPath) #list of image file names
print(pathList)
imgList = []
teachids = []
for path in pathList: #path contains each image name
    imgx=cv2.imread(os.path.join(folderPath, path))
    imgy=cv2.resize(imgx,(216,216))
    
    cv2.imwrite((folderPath+"/"+os.path.splitext(path)[0]+".jpg"),imgy)
    imgList.append(imgy)  #joining folderPath and path to create the image path with name
    #"Images/100.jpg"
    teachids.append(os.path.splitext(path)[0]) #appending the path without extension as name of image is teachid itself

    fileName = f'{folderPath}/{path}' #creating formatted string that containst the image directory with image name
    bucket = storage.bucket() #creating a storage bucket of firebase
    blob = bucket.blob(fileName) #creating blob type variable (datatype for storing images in database) to store image
    print(fileName)
    #in the database
    blob.upload_from_filename(fileName) #uploading image 

    # print(path)
    # print(os.path.splitext(path)[0])
print(teachids)

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
encodeListKnownWithIds = [encodeListKnown, teachids]
print("Encoding Complete")

file = open("EncodeFileT.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
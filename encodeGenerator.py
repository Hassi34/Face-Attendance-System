import cv2, face_recognition, pickle, os
from pathlib import Path
import appConfig as CONFIG

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate("admin.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': CONFIG.databaseURL,
    'storageBucket': CONFIG.bucketURL
})

# Importing the student images
studentImgDir = os.path.relpath(Path(os.path.join('Images')).resolve())
imgFiles = os.listdir(studentImgDir)
imgList = []
studentIds = []
for img in imgFiles:
    imgPath = os.path.join(studentImgDir, img)
    imgResized = cv2.resize(cv2.imread(imgPath), CONFIG.stdImgSize) #Converting all the images to standard format to display on frontend
    cv2.imwrite(imgPath, imgResized)
    imgList.append(cv2.imread(imgPath))
    studentIds.append(img.split('.')[0])

    bucketPathForImg = f"{studentImgDir}/{img}"
    bucket = storage.bucket()
    blob = bucket.blob(bucketPathForImg)
    blob.upload_from_filename(imgPath)

def findEncodings(imgList):
    encodeList = []
    for img in imgList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList 

encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]

with open("encodeFile.pkl", "wb") as f:
    pickle.dump(encodeListKnownWithIds, f)


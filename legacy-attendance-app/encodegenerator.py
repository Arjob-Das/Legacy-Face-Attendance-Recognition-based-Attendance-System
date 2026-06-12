"""
Face Encoding Generator.

Reads student images from the Images/ directory, generates face encodings,
uploads images to Firebase Storage, and saves encodings to EncodeFile.p.
"""

import os
import pickle

import cv2
import face_recognition
from firebase_admin import storage

from firebase_config import initialize_firebase

# ── Firebase ────────────────────────────────────────────────────────
initialize_firebase(include_storage=True)

# ── Import student images ──────────────────────────────────────────
FOLDER_PATH = 'Images'
pathList = os.listdir(FOLDER_PATH)
print(pathList)

imgList = []
studentIds = []

for path in pathList:
    imgList.append(cv2.imread(os.path.join(FOLDER_PATH, path)))
    studentIds.append(os.path.splitext(path)[0])

    # Upload image to Firebase Storage
    fileName = f'{FOLDER_PATH}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print(studentIds)


# ── Encoding ────────────────────────────────────────────────────────
def find_encodings(images_list):
    """Generate face encodings for a list of images.

    Args:
        images_list: List of BGR images (numpy arrays).

    Returns:
        List of 128-dimensional face encoding vectors.
    """
    encode_list = []
    for img in images_list:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img_rgb)[0]
        encode_list.append(encode)
    return encode_list


print("Encoding Started ...")
encodeListKnown = find_encodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

with open("EncodeFile.p", 'wb') as f:
    pickle.dump(encodeListKnownWithIds, f)
print("File Saved")
"""
Image Uploader & Encoder (Students).

Reads images from Images/, resizes them to 216x216, uploads to Firebase Storage,
generates face encodings, and saves to EncodeFile.p.
"""

import os
import pickle
import sys

import cv2
import face_recognition

# Add parent directory to path to load centralized firebase_config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from firebase_config import initialize_firebase

# ── Firebase ────────────────────────────────────────────────────────
_, bucket = initialize_firebase(include_storage=True, is_teacher=False)

# ── Import student images ──────────────────────────────────────────
FOLDER_PATH = 'Images'
if not os.path.exists(FOLDER_PATH):
    os.makedirs(FOLDER_PATH, exist_ok=True)

pathList = os.listdir(FOLDER_PATH)
print(pathList)

imgList = []
studentIds = []

for path in pathList:
    full_path = os.path.join(FOLDER_PATH, path)
    img = cv2.imread(full_path)
    if img is None:
        continue

    # Resize to exactly 216x216
    img_resized = cv2.resize(img, (216, 216))
    cv2.imwrite(full_path, img_resized)

    imgList.append(img_resized)
    studentIds.append(os.path.splitext(path)[0])

    # Upload to Storage
    blob = bucket.blob(f'{FOLDER_PATH}/{path}')
    blob.upload_from_filename(full_path)

print(studentIds)


# ── Encoding ────────────────────────────────────────────────────────
def find_encodings(images_list):
    """Generate face encodings for a list of images."""
    encode_list = []
    for img in images_list:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img_rgb)
        if encodings:
            encode_list.append(encodings[0])
    return encode_list


print("Encoding Started ...")
encodeListKnown = find_encodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

with open("EncodeFile.p", 'wb') as f:
    pickle.dump(encodeListKnownWithIds, f)
print("File Saved")
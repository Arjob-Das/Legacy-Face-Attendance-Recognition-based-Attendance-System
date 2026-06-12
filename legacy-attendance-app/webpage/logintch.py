"""
Face Recognition Login (Teachers) — Web integration.

Checks webcam feed for a recognized teacher, prints their details, and exits.
Aborts if no recognized face is found after 25 attempts.
"""

import json
import os
import pickle
import sys

import cv2
import cvzone
import face_recognition
import numpy as np

# Add parent directory to path to load centralized firebase_config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from firebase_config import initialize_firebase

# ── Firebase ────────────────────────────────────────────────────────
db_ref, bucket = initialize_firebase(include_storage=True, is_teacher=True)

# ── Video capture ───────────────────────────────────────────────────
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

imgBackground = cv2.imread('Resources/background.png')

# ── Mode images ─────────────────────────────────────────────────────
FOLDER_MODE_PATH = 'Resources/Modes'
modePathList = os.listdir(FOLDER_MODE_PATH)
imgModeList = [cv2.imread(os.path.join(FOLDER_MODE_PATH, path)) for path in modePathList]

# ── Encoding file ───────────────────────────────────────────────────
with open('EncodeFileT.p', 'rb') as f:
    encodeListKnownWithIds = pickle.load(f)
encodeListKnown, teacherIds = encodeListKnownWithIds

# ── State variables ─────────────────────────────────────────────────
modeType = 0
counter = 0
teacher_uuid = -1
imgTeacher = []
no_face_counter = 0

# ── Main loop ───────────────────────────────────────────────────────
while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                teacher_uuid = teacherIds[matchIndex]

                if counter == 0:
                    cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                    cv2.imshow("Face Attendance", imgBackground)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1

        if counter == 0:
            no_face_counter += 1
            if no_face_counter == 25:
                print(json.dumps({"error": "Login Not Verified"}))
                break

        elif 0 < counter < 5:
            # Fetch teacher data from Firebase
            teacherInfo = db_ref(f'Teachers/{teacher_uuid}').get()

            # Fetch image from Storage
            blob = bucket.get_blob(f'ImagesT/{teacher_uuid}.jpg')
            array = np.frombuffer(blob.download_as_string(), np.uint8)
            imgTeacher = cv2.imdecode(array, cv2.IMREAD_COLOR)

            modeType = 1
            imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

            cv2.putText(imgBackground, str(teacherInfo.get('department')),
                        (1006, 550), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                        (255, 255, 255), 1)
            cv2.putText(imgBackground, str(teacher_uuid),
                        (1006, 493), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                        (255, 255, 255), 1)

            (w, _), _ = cv2.getTextSize(
                teacherInfo.get('name', ''), cv2.FONT_HERSHEY_COMPLEX, 1, 1
            )
            offset = (414 - w) // 2
            cv2.putText(imgBackground, str(teacherInfo.get('name')),
                        (808 + offset, 445), cv2.FONT_HERSHEY_COMPLEX, 1,
                        (50, 50, 50), 1)

            imgBackground[175:175 + 216, 909:909 + 216] = imgTeacher
            counter += 1

            if counter == 4:
                print(
                    json.dumps({
                        "id": teacher_uuid,
                        "name": teacherInfo.get('name'),
                        "total_attendance": teacherInfo.get('total_attendance'),
                        "assigned_class": teacherInfo.get('assigned_class'),
                        "department": teacherInfo.get('department'),
                        "year": teacherInfo.get('year'),
                        "starting_year": teacherInfo.get('starting_year'),
                        "last_attendance_time": teacherInfo.get('last_attendance_time')
                    })
                )

    if counter == 5:
        break

    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(33)
    if cv2.getWindowProperty('Face Attendance', 0) == -1:
        break

cap.release()
cv2.destroyAllWindows()
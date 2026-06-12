"""
Face Recognition Attendance (Students) — Web integration.

Checks webcam feed, identifies student, records attendance, updates Firebase DB,
prints attendance status on confirmation (counter > 20), and exits.
"""

import os
import pickle
import sys

import cv2
import cvzone
import face_recognition
import numpy as np
from datetime import datetime

# Add parent directory to path to load centralized firebase_config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from firebase_config import initialize_firebase

# ── Firebase ────────────────────────────────────────────────────────
db_ref, bucket = initialize_firebase(include_storage=True, is_teacher=False)

at = 0
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

imgBackground = cv2.imread('Resources/background.png')

# ── Mode images ─────────────────────────────────────────────────────
FOLDER_MODE_PATH = 'Resources/Modes'
modePathList = os.listdir(FOLDER_MODE_PATH)
imgModeList = [cv2.imread(os.path.join(FOLDER_MODE_PATH, path)) for path in modePathList]

# ── Encoding file ───────────────────────────────────────────────────
with open('EncodeFile.p', 'rb') as f:
    encodeListKnownWithIds = pickle.load(f)
encodeListKnown, studentIds = encodeListKnownWithIds

# ── State variables ─────────────────────────────────────────────────
modeType = 0
counter = 0
student_uuid = -1
imgStudent = []

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
                student_uuid = studentIds[matchIndex]

                if counter == 0:
                    cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                    cv2.imshow("Face Attendance", imgBackground)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1

        if counter != 0:
            if counter == 1:
                # Fetch student details from Firebase
                studentInfo = db_ref(f'Students/{student_uuid}').get()

                # Fetch image from Storage
                blob = bucket.get_blob(f'Images/{student_uuid}.jpg')
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgStudent = cv2.imdecode(array, cv2.IMREAD_COLOR)

                # Attendance Cooldown (300 seconds / 5 minutes)
                datetimeObject = datetime.strptime(
                    studentInfo['last_attendance_time'], "%Y-%m-%d %H:%M:%S"
                )
                secondsElapsed = (datetime.now() - datetimeObject).total_seconds()

                if secondsElapsed > 300:
                    ref = db_ref(f'Students/{student_uuid}')
                    studentInfo['total_attendance'] += 1
                    at = studentInfo['total_attendance']
                    ref.child('total_attendance').set(studentInfo['total_attendance'])
                    ref.child('last_attendance_time').set(
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    )
                else:
                    at = studentInfo['total_attendance']
                    modeType = 3
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

            if modeType != 3:
                if 10 < counter < 20:
                    modeType = 2

                imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

                if counter <= 10:
                    cv2.putText(imgBackground, str(studentInfo.get('total_attendance')),
                                (861, 125), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(studentInfo.get('major')),
                                (1006, 550), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                                (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(student_uuid),
                                (1006, 493), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                                (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(studentInfo.get('standing')),
                                (910, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6,
                                (100, 100, 100), 1)
                    cv2.putText(imgBackground, str(studentInfo.get('year')),
                                (1025, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6,
                                (100, 100, 100), 1)
                    cv2.putText(imgBackground, str(studentInfo.get('starting_year')),
                                (1125, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6,
                                (100, 100, 100), 1)

                    (w, _), _ = cv2.getTextSize(
                        studentInfo.get('name', ''), cv2.FONT_HERSHEY_COMPLEX, 1, 1
                    )
                    offset = (414 - w) // 2
                    cv2.putText(imgBackground, str(studentInfo.get('name')),
                                (808 + offset, 445), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (50, 50, 50), 1)

                    imgBackground[175:175 + 216, 909:909 + 216] = imgStudent

                if counter >= 22:
                    counter = 0
                    modeType = 0
                    studentInfo = []
                    imgStudent = []
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

        counter += 1
        if counter > 20:
            print(at)
            break
    else:
        modeType = 0
        counter = 0

    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(33)
    if cv2.getWindowProperty('Face Attendance', 0) == -1:
        print(at)
        break

cap.release()
cv2.destroyAllWindows()
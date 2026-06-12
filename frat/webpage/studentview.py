import os
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np
import sys

from datetime import datetime
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-44242-default-rtdb.firebaseio.com/",
    'storageBucket': "face-recognition-44242.appspot.com"
})
id=sys.argv[1]
studentInfo = db.reference(f'Students/{id}').get()
print(str(id)," ",str(studentInfo['name'])," ",str(studentInfo['total_attendance'])," ",str(studentInfo['standing'])," ",str(studentInfo['major'])," ",str(studentInfo['year'])," ",str(studentInfo['starting_year'])," ",str(studentInfo['last_attendance_time'])," ")

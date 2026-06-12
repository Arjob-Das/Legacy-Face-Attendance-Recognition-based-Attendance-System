import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import sys
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-44242-default-rtdb.firebaseio.com/"
})
name=sys.argv[1]+" "+sys.argv[2]
data = {}
ref = db.reference('Students')
c=8
major=""
while c<len(sys.argv):
    major=major+sys.argv[c]+" "
    c=c+1
data[sys.argv[3]]={
            "name": name,
            "major": major,
            "starting_year": int(sys.argv[5]),
            "total_attendance": int(sys.argv[7]),
            "standing": sys.argv[6],
            "year": int(sys.argv[4]),
            "last_attendance_time": "2022-12-11 00:54:34"
            }

for key, value in data.items():
    ref.child(key).set(value)
print("Data Added Succesfully")
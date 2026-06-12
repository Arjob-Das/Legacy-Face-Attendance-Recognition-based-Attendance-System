import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import sys
cred = credentials.Certificate("serviceAccountKey2.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://teacherid-f3bdd-default-rtdb.firebaseio.com/",
})
name=sys.argv[1]+" "+sys.argv[2]
data = {}
ref = db.reference('Teachers')
c=8
dept=""
while c<len(sys.argv):
    dept=dept+sys.argv[c]+" "
    c=c+1
data[sys.argv[3]]={
            "name": name,
            "department": dept,
            "starting_year": int(sys.argv[5]),
            "total_attendance": int(sys.argv[7]),
            "assigned_class": sys.argv[6],
            "year": int(sys.argv[4]),
            "last_attendance_time": "2022-12-11 00:54:34"
            }

for key, value in data.items():
    ref.child(key).set(value)
print("Data Added Succesfully")
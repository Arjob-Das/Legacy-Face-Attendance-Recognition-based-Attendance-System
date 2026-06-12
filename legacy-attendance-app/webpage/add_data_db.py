import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-44242-default-rtdb.firebaseio.com/"
})
data = {}
ref = db.reference('Students')
while True:
    
    id=input("Enter Student Id : ")
    name=input("Enter Name : ")
    major=input("Enter Major Subject : ")
    styr=int(input("Enter Starting Year : "))
    tad=int(input("Enter Total Attendance : "))
    stnd=input("Enter Standing (A-K) : ")    
    yr=int(input("Enter the year : "))
    
    
    
    data[id]={
            "name": name,
            "major": major,
            "starting_year": styr,
            "total_attendance": tad,
            "standing": stnd,
            "year": yr,
            "last_attendance_time": "2022-12-11 00:54:34"
            }
    
    ch=input("Enter Y to continue entering more : ")
    if(ch!='Y' and ch!='y'):
        break

for key, value in data.items():
    ref.child(key).set(value)
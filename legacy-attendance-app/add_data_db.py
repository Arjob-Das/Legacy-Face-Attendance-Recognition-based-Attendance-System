"""
Add Student Data to Firebase.

Interactive CLI tool that prompts for student details and writes
them to the Firebase Realtime Database under the Students/ node.
"""

from firebase_config import initialize_firebase

# ── Firebase (no storage needed) ────────────────────────────────────
db_ref, _ = initialize_firebase(include_storage=False)

ref = db_ref('Students')
data = {}

while True:
    student_id = input("Enter Student Id : ")
    name = input("Enter Name : ")
    major = input("Enter Major Subject : ")
    starting_year = int(input("Enter Starting Year : "))
    total_attendance = int(input("Enter Total Attendance : "))
    standing = input("Enter Standing (A-K) : ")
    year = int(input("Enter the year : "))

    data[student_id] = {
        "name": name,
        "major": major,
        "starting_year": starting_year,
        "total_attendance": total_attendance,
        "standing": standing,
        "year": year,
        "last_attendance_time": "2022-12-11 00:54:34",
    }

    choice = input("Enter Y to continue entering more : ")
    if choice not in ('Y', 'y'):
        break

for key, value in data.items():
    ref.child(key).set(value)

print(f"Successfully added {len(data)} student(s) to database.")
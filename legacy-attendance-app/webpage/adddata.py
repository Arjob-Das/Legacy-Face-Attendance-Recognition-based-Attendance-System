"""
Add Student Data.

Invoked by PHP registration form. Inserts student details into Firebase.
"""

import os
import sys

# Add parent directory to path to load centralized firebase_config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from firebase_config import initialize_firebase

if len(sys.argv) < 8:
    print("Error: Missing required student registration arguments.")
    sys.exit(1)

# Args: fname, lname, student_id, year, starting_year, standing, total_attendance, major_words...
first_name = sys.argv[1]
last_name = sys.argv[2]
student_id = sys.argv[3]
year = int(sys.argv[4])
starting_year = int(sys.argv[5])
standing = sys.argv[6]
total_attendance = int(sys.argv[7])

# Extract major (may consist of multiple words)
major = " ".join(sys.argv[8:])

db_ref, _ = initialize_firebase(include_storage=False, is_teacher=False)

student_data = {
    "name": f"{first_name} {last_name}".strip(),
    "major": major.strip(),
    "starting_year": starting_year,
    "total_attendance": total_attendance,
    "standing": standing,
    "year": year,
    "last_attendance_time": "2022-12-11 00:54:34"
}

db_ref(f'Students/{student_id}').set(student_data)
print("Data Added Succesfully")
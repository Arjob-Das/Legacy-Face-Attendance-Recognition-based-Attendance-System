"""
Add Teacher Data.

Invoked by PHP registration form. Inserts teacher details into Firebase.
"""

import os
import sys

# Add parent directory to path to load centralized firebase_config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from firebase_config import initialize_firebase

if len(sys.argv) < 8:
    print("Error: Missing required teacher registration arguments.")
    sys.exit(1)

# Args: fname, lname, teach_id, year, starting_year, assigned_class, total_attendance, dept_words...
first_name = sys.argv[1]
last_name = sys.argv[2]
teach_id = sys.argv[3]
year = int(sys.argv[4])
starting_year = int(sys.argv[5])
assigned_class = sys.argv[6]
total_attendance = int(sys.argv[7])

# Extract department (may consist of multiple words)
department = " ".join(sys.argv[8:])

db_ref, _ = initialize_firebase(include_storage=False, is_teacher=True)

teacher_data = {
    "name": f"{first_name} {last_name}".strip(),
    "department": department.strip(),
    "starting_year": starting_year,
    "total_attendance": total_attendance,
    "assigned_class": assigned_class,
    "year": year,
    "last_attendance_time": "2022-12-11 00:54:34"
}

db_ref(f'Teachers/{teach_id}').set(teacher_data)
print("Data Added Succesfully")
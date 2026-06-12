"""
Student Viewer.

Queries and prints information for a specific student ID passed as a CLI argument.
"""

import json
import os
import sys

# Add parent directory to path to load centralized firebase_config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from firebase_config import initialize_firebase

if len(sys.argv) < 2:
    print("Error: Missing student ID parameter.")
    sys.exit(1)

student_id = sys.argv[1]

# Initialize Firebase (student DB)
db_ref, _ = initialize_firebase(include_storage=False, is_teacher=False)

try:
    studentInfo = db_ref(f'Students/{student_id}').get()
    if not studentInfo:
        print(f"Error: Student with ID {student_id} not found.")
        sys.exit(1)

    print(
        json.dumps({
            "id": student_id,
            "name": studentInfo.get('name'),
            "total_attendance": studentInfo.get('total_attendance'),
            "standing": studentInfo.get('standing'),
            "major": studentInfo.get('major'),
            "year": studentInfo.get('year'),
            "starting_year": studentInfo.get('starting_year'),
            "last_attendance_time": studentInfo.get('last_attendance_time')
        })
    )
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

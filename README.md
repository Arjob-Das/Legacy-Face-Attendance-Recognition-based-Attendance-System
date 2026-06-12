# Legacy Face Recognition Attendance System

A face-recognition-based attendance system built with OpenCV, `face_recognition`, and Firebase. This legacy version uses a PHP frontend and Python backend for real-time face detection and attendance tracking.

> **Note:** This is the legacy/archived version of the project. For the modernised rewrite, see [Face-recognition-web-app-login-attendance-](https://github.com/Arjob-Das/Face-recognition-web-app-login-attendance-).

## Features

- Real-time face detection and recognition via webcam
- Student registration with face encoding generation
- Attendance tracking with cooldown to prevent duplicate entries
- Firebase Realtime Database for student data storage
- Firebase Cloud Storage for student images
- PHP-based web interface for login and attendance

## Project Structure

```
frat/
├── firebase_config.py          # Centralised Firebase initialisation
├── test.py                     # Main attendance loop
├── loginpt.py                  # Single-face login/identification
├── encodegenerator.py          # Generate face encodings & upload images
├── add_data_db.py              # CLI to add student data to Firebase
├── serviceAccountKey.json.template  # Firebase credentials template
├── requirements.txt            # Python dependencies
├── attendance.php              # PHP endpoint to trigger attendance
├── index1.php                  # Student registration form
├── index2.php                  # Student info display after login
├── style.css / style1.css      # CSS stylesheets
├── Resources/                  # Background images and mode overlays
│   ├── background.png
│   └── Modes/
├── Images/                     # Student face images (by ID)
└── webpage/                    # Extended web interface version
```

## Prerequisites

- Python 3.8+
- A webcam
- Firebase project with Realtime Database and Cloud Storage enabled
- PHP (if using the web interface)

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Arjob-Das/Legacy-Face-Attendance-Recognition-based-Attendance-System.git
   cd Legacy-Face-Attendance-Recognition-based-Attendance-System/frat
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Firebase:**
   - Copy `serviceAccountKey.json.template` to `serviceAccountKey.json`
   - Fill in your Firebase service account credentials
   - Update the `DATABASE_URL` and `STORAGE_BUCKET` in `firebase_config.py` if needed

4. **Add student data:**
   ```bash
   python add_data_db.py
   ```

5. **Add student images:**
   - Place student photos in `Images/` named as `<student_id>.jpg`

6. **Generate face encodings:**
   ```bash
   python encodegenerator.py
   ```

7. **Run the attendance system:**
   ```bash
   python test.py
   ```

## License

[MIT](LICENSE)

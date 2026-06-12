# Legacy Face Recognition Attendance System

A legacy face-recognition-based attendance system built with OpenCV, `face_recognition`, and Firebase. This system features a PHP web frontend coupled with a Python desktop backend for real-time face detection, user registration, and database management.

> ℹ️ **Status:** This is the legacy/archived desktop-focused repository. For the modernized, production-ready, and containerized web application, see the [FaceAttend Rewrite](https://github.com/Arjob-Das/Face-recognition-web-app-login-attendance-).

---

## 🌟 Features

- **Real-Time Recognition:** Desktop-based webcam feed recognition with face bounding boxes and status overlays.
- **Bi-Role Capabilities:** Separate support for Student and Teacher registration, login, and attendance tracking.
- **Smart Cooldown:** Integrated attendance check timeout (30 seconds for desktop / 5 minutes for webpage) to prevent duplicate log entries.
- **Centralized Firebase Integration:** Centralized configuration that supports dynamically routing connections to separate Student and Teacher databases.
- **Webpage Portal:** PHP-based user forms for student/teacher registration, login, and info viewing, invoking the Python scripts under the hood.

---

## 📂 Project Structure

```
legacy-attendance-app/
├── firebase_config.py          # Centralized Firebase initialization (multi-app support)
├── test.py                     # Main student attendance camera loop
├── loginpt.py                  # Student face-identification script
├── encodegenerator.py          # Script to generate student face encodings
├── add_data_db.py              # CLI tool to add student profiles to Firebase
├── serviceAccountKey.json.template   # Template for student Firebase service account
├── serviceAccountKey2.json.template  # Template for teacher Firebase service account
├── requirements.txt            # Python dependencies
├── attendance.php              # PHP script triggering student attendance loop
├── index1.php                  # PHP student registration portal
├── index2.php                  # PHP student verification display
├── style.css / style1.css      # Front-end stylesheets
├── Resources/                  # Desktop GUI assets (background, modes)
│   ├── background.png
│   └── Modes/
├── Images/                     # Local student face image directories
└── webpage/                    # Extended PHP web application portal
    ├── student_account_creation.php  # Student portal registration
    ├── teacher_account_creation.php  # Teacher portal registration
    ├── student_login.php             # Student face-recognition login form
    ├── teacher_login.php             # Teacher face-recognition login form
    ├── studentview.py                # Python backend to view student profile
    ├── adddata.py                    # Python backend to save student to database
    ├── adddatateacher.py             # Python backend to save teacher to database
    ├── image_uploader.py             # Python backend to upload/encode student images
    ├── image_uploader_T.py           # Python backend to upload/encode teacher images
    ├── loginpt.py                    # Python backend for student face login
    ├── logintch.py                   # Python backend for teacher face login
    ├── stud_face.py                  # Python backend for student attendance
    └── teach_face.py                 # Python backend for teacher attendance
```

---

## 🛠️ Prerequisites

- **Python:** 3.8+
- **PHP:** A web server running PHP (e.g., XAMPP, Apache)
- **Hardware:** Connected webcam for face capture
- **Firebase:** Two separate Firebase projects (one for Students, one for Teachers) with Realtime Database and Cloud Storage enabled.

---

## 🚀 Setup & Installation

### 1. Project Clone
```bash
git clone https://github.com/Arjob-Das/Legacy-Face-Attendance-Recognition-based-Attendance-System.git
cd Legacy-Face-Attendance-Recognition-based-Attendance-System/legacy-attendance-app
```

### 2. Python Dependencies
Install core face recognition and image processing dependencies:
```bash
pip install -r requirements.txt
```

### 3. Firebase Configuration
- Copy `serviceAccountKey.json.template` to `serviceAccountKey.json` and fill in your student-project credentials.
- Copy `serviceAccountKey2.json.template` to `serviceAccountKey2.json` and fill in your teacher-project credentials.
- Open `firebase_config.py` and verify/update the `STUDENT_DATABASE_URL`, `STUDENT_STORAGE_BUCKET`, `TEACHER_DATABASE_URL`, and `TEACHER_STORAGE_BUCKET` constants to match your projects.

---

## 💻 Running the Applications

### Desktop Mode
1. **Add student data via CLI:**
   ```bash
   python add_data_db.py
   ```
2. **Place student photos** inside `Images/` named as `<student_id>.jpg`.
3. **Generate face encodings:**
   ```bash
   python encodegenerator.py
   ```
4. **Launch the attendance loop:**
   ```bash
   python test.py
   ```

### Webpage Portal Mode
1. Place the `legacy-attendance-app` directory inside your local web server root (e.g., `C:/xampp/htdocs/legacy-attendance-app/`).
2. Run your Apache/PHP server.
3. Open `http://localhost/legacy-attendance-app/webpage/student_account_creation.php` in your browser to register.
4. Open `http://localhost/legacy-attendance-app/webpage/student_login.php` to log in using face recognition.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

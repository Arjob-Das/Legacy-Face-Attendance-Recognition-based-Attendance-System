"""
Centralized Firebase configuration.

All Firebase initialization is handled here to avoid duplicating
credentials and database URLs across multiple scripts.
"""

import firebase_admin
from firebase_admin import credentials, db, storage

# Firebase project settings
STUDENT_DATABASE_URL = "https://face-recognition-44242-default-rtdb.firebaseio.com/"
STUDENT_STORAGE_BUCKET = "face-recognition-44242.appspot.com"
STUDENT_SERVICE_ACCOUNT = "serviceAccountKey.json"

TEACHER_DATABASE_URL = "https://teacherid-f3bdd-default-rtdb.firebaseio.com/"
TEACHER_STORAGE_BUCKET = "teacherid-f3bdd.appspot.com"
TEACHER_SERVICE_ACCOUNT = "serviceAccountKey2.json"


def initialize_firebase(include_storage=True, is_teacher=False):
    """Initialize the Firebase app and return db reference getter and storage bucket.

    Args:
        include_storage: If True, include the storageBucket in the config.
        is_teacher: If True, initialize/use the teacher Firebase project.

    Returns:
        A tuple of (db_ref_func, storage bucket or None).
    """
    app_name = "teacher" if is_teacher else "[DEFAULT]"
    db_url = TEACHER_DATABASE_URL if is_teacher else STUDENT_DATABASE_URL
    storage_bucket = TEACHER_STORAGE_BUCKET if is_teacher else STUDENT_STORAGE_BUCKET
    service_account = TEACHER_SERVICE_ACCOUNT if is_teacher else STUDENT_SERVICE_ACCOUNT

    config = {"databaseURL": db_url}
    if include_storage and storage_bucket:
        config["storageBucket"] = storage_bucket

    try:
        app = firebase_admin.get_app(app_name)
    except ValueError:
        cred = credentials.Certificate(service_account)
        app = firebase_admin.initialize_app(cred, config, name=app_name)

    def db_ref(path=""):
        return db.reference(path, app=app)

    bucket = storage.bucket(app=app) if include_storage and storage_bucket else None
    return db_ref, bucket


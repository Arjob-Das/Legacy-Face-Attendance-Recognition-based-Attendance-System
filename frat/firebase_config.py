"""
Centralized Firebase configuration.

All Firebase initialization is handled here to avoid duplicating
credentials and database URLs across multiple scripts.
"""

import firebase_admin
from firebase_admin import credentials, db, storage

# Firebase project settings
DATABASE_URL = "https://face-recognition-44242-default-rtdb.firebaseio.com/"
STORAGE_BUCKET = "face-recognition-44242.appspot.com"
SERVICE_ACCOUNT_KEY = "serviceAccountKey.json"


def initialize_firebase(include_storage=True):
    """Initialize the Firebase app if it hasn't been initialized yet.

    Args:
        include_storage: If True, include the storageBucket in the config.

    Returns:
        A tuple of (db module, storage bucket or None).
    """
    config = {"databaseURL": DATABASE_URL}
    if include_storage:
        config["storageBucket"] = STORAGE_BUCKET

    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_KEY)
        firebase_admin.initialize_app(cred, config)

    bucket = storage.bucket() if include_storage else None
    return db, bucket

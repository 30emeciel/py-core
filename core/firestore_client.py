import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def db():
    # Use the application default credentials
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': "trentiemeciel",
    })

    return firestore.Client()

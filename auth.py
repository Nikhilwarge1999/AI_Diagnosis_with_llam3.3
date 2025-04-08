import pyrebase
from firebase_config import firebase_config

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        user_info = db.child("users").child(user['localId']).get()
        return True, {"name": user_info.val().get("name", "")}
    except Exception as e:
        return False, str(e)

def register_user(email, password, name):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        db.child("users").child(user['localId']).set({"email": email, "name": name})
        return True, "Registration successful!"
    except Exception as e:
        return False, str(e)

def reset_password(email):
    try:
        auth.send_password_reset_email(email)
        return True  # success
    except Exception as e:
        print("Reset Error:", e)
        return False  #  failure

import pyrebase

firebase_config = {
    "apiKey": "AIzaSyCU6cMAqGSvvJwmFNO22VbpsyUqrLhfCrY",
    "authDomain": "aibot-5fceb.firebaseapp.com",
    "databaseURL": "https://aibot-5fceb-default-rtdb.firebaseio.com/",  # <-- Add this!
    "projectId": "aibot-5fceb",
    "storageBucket": "aibot-5fceb.appspot.com",
    "messagingSenderId": "1048140543074",
    "appId": "1:1048140543074:web:d73da2b2926a9b97fc8d3b"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

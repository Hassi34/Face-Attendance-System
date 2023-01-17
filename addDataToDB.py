
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import appConfig as CONFIG

cred = credentials.Certificate("admin.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': CONFIG.databaseURL
})

ref = db.reference("students")

data = {
    "123":
    {
        "name": "Hasnain",
        "major": "AI",
        "starting_year": 2017,
        "total_attendance": 6,
        "standing": "G",
        "year": 3,
        "last_attendance_time": "2023-01-14 00:54:14"
    },
    "852741":
    {
        "name": "Emily",
        "major": "Data Science",
        "starting_year": 2018,
        "total_attendance": 4,
        "standing": "B",
        "year": 3,
        "last_attendance_time": "2023-01-14 00:54:14"
    },
        "963852":
    {
        "name": "Elon Musk",
        "major": "Physics",
        "starting_year": 2016,
        "total_attendance": 7,
        "standing": "G",
        "year": 7,
        "last_attendance_time": "2023-01-14 00:54:14"
    },
    
}

for k, v in data.items():
    ref.child(k).set(v)
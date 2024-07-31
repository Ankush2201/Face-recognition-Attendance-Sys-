from pymongo import MongoClient

def get_database():
    client = MongoClient('localhost', 27017)
    db = client['Attendance']
    return db

def get_students_collection():
    db = get_database()
    return db['students']

def get_attendance_collection():
    db = get_database()
    return db['attendance']

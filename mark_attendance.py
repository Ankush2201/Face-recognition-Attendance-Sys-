import cv2
import numpy as np
import face_recognition
from database import get_students_collection, get_attendance_collection
from datetime import datetime

def compare_faces(face_encoding1, face_encoding2):
    return np.linalg.norm(np.array(face_encoding1) - np.array(face_encoding2))

def detect_and_mark_attendance():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    students = get_students_collection()
    students_list = list(students.find())

    # Debug output to check the structure of documents
    for student in students_list:
        print(student)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            min_distance = float('inf')
            matched_student = None
            for student in students_list:
                if 'face_encoding' not in student:
                    print("Skipping student without face_encoding field.")
                    continue
                stored_encoding = np.array(student['face_encoding'])
                distance = compare_faces(face_encoding, stored_encoding)

                if distance < min_distance:
                    min_distance = distance
                    matched_student = student

            name = matched_student['name'] if matched_student and min_distance < 0.6 else 'Unknown'
            color = (255, 0, 0) if name != 'Unknown' else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            if matched_student and min_distance < 0.6:
                today_date = datetime.now().strftime("%Y-%m-%d")
                attendance = get_attendance_collection()
                
                # Check if the attendance record already exists
                existing_record = attendance.find_one({
                    "date": today_date,
                    "student_id": matched_student['student_id']
                })

                if not existing_record:
                    # Insert a new attendance record if not present
                    attendance_record = {
                        "date": today_date,
                        "student_id": matched_student['student_id'],
                        "status": "Present"
                    }
                    attendance.insert_one(attendance_record)
                    print(f'Attendance marked for {name}')
                else:
                    print(f'Attendance for {name} already marked today.')

        cv2.imshow('Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_and_mark_attendance()

import cv2
import numpy as np
import face_recognition
from database import get_students_collection

def capture_face_encodings(num_samples=3):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video device.")
        return None

    encodings = []

    print("Please look at the camera and follow the instructions.")
    for i in range(num_samples):
        print(f"Capturing image {i+1}/{num_samples}. Please adjust your position.")
        
        ret, frame = cap.read()
        if ret:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            
            if face_encodings:
                encodings.append(face_encodings[0])
                # Display the frame with a message
                cv2.putText(frame, f"Image {i+1}/{num_samples}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                print("No face detected in this frame. Please try again.")
            
            # Show the frame with instructions
            cv2.imshow('Capture Face', frame)
            cv2.waitKey(1000)  # Wait for a short period before capturing the next image
            
        else:
            print("Error: Could not read frame from video device.")
            cap.release()
            cv2.destroyAllWindows()
            return None

    cap.release()
    cv2.destroyAllWindows()
    
    if encodings:
        # Compute the average encoding
        avg_encoding = np.mean(encodings, axis=0).tolist()
        return avg_encoding
    else:
        print("No valid face encodings captured.")
        return None

def register_student(student_id, name):
    face_encoding = capture_face_encodings()
    if face_encoding:
        students = get_students_collection()
        student_data = {
            "student_id": student_id,
            "name": name,
            "face_encoding": face_encoding
        }
        students.insert_one(student_data)
        print(f'Student {name} registered successfully!')
    else:
        print('No valid face encodings captured, please try again.')

if __name__ == "__main__":
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    register_student(student_id, name)

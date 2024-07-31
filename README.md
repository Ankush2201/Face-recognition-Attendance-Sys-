

# Student Attendance Management System

## Overview

This project is a Python-based GUI application that interfaces with a MongoDB database to manage student attendance. It includes functionalities for registering new students and marking their attendance using face recognition.

## Project Structure

- `database.py`: Contains the code for connecting and interacting with the MongoDB database.
- `register.py`: Provides the functionality to register new students into the database.
- `mark_attendance.py`: Handles the attendance marking process using face recognition.
- `LICENSE`: Contains the license information for the project.
- `README.md`: This file, providing an overview and instructions for the project.
- `__pycache__/`: Contains the compiled Python files.

## Setup Instructions

### Prerequisites

1. Python 3.x
2. MongoDB
3. Required Python packages:
   - OpenCV
   - face_recognition
   - pymongo
   - Tkinter (for GUI)

### Installation

1. Clone the repository to your local machine.
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory.
    ```bash
    cd <project-directory>
    ```
3. Install the required Python packages.
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Ensure MongoDB is running on your local machine or a server you can access.
2. Update the MongoDB connection details in `database.py`.

## Usage

### Registering New Students

1. Run the `register.py` script.
    ```bash
    python register.py
    ```
2. Fill in the student details in the GUI form and submit to save the information to the database.

### Marking Attendance

1. Run the `mark_attendance.py` script.
    ```bash
    python mark_attendance.py
    ```
2. The application will open the camera and start detecting faces. It will display the names of detected individuals with blue rectangles around their faces. Unknown faces will be labeled as 'Unknown'.

## Contributing

1. Fork the repository.
2. Create a new branch.
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them.
    ```bash
    git commit -m "Description of changes"
    ```
4. Push to the branch.
    ```bash
    git push origin feature-branch
    ```
5. Open a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---

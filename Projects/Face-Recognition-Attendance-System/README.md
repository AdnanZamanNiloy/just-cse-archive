
# Face Recognition Attendance System 

**Enhancing Attendance Accuracy with Facial Recognition Technology**

## Overview

The Face Recognition Attendance System is an advanced desktop application designed to streamline attendance processes in universities using facial recognition and liveness detection. This system boosts accuracy, reduces manual workload, and prevents proxy attendance by ensuring students are physically present during attendance logging.

**Key Highlights**  
- 97% Recognition Accuracy  
- Liveness Detection using Blink Detection  
- Rejects Photos or Fake Face Attempts

## Key Features

- Student Registration & Login
- Forgot Password Recovery
- Detailed Student Info Form
- Real-time Face Recognition with Liveness Detection
- Train Data Module – Train face samples for recognition
- CSV-based Attendance Logs – Name, ID, Department, Date & Time
- Photo Repository – View all trained face samples together
- Interactive Chatbot – Project Q&A and usage help
- Support Section – For troubleshooting, with Developer Contact
- Exit Module – Clean exit with confirmation

## Functional Modules

### Authentication
- Account creation using Gmail
- Login with secure credentials
- Password recovery via email

### Student Details
- Select Department, Course, Semester, Year
- Input ID, Name, Gender, DOB, Phone, Email, Address, Teacher Name
- Take face sample directly from webcam

### Train Data
- Capture face samples and train them using Dlib + OpenCV
- Stores encoded facial data for accurate recognition

### Face Recognition & Attendance
- Real-time detection using webcam
- Liveness detection with blink tracking
- Ensures physical presence, blocks spoofing attempts
- Attendance saved to .csv with timestamp

### Attendance Management
- Import and view .csv records
- View by student, department, or date
- Shows Attendance ID, Name, Reg No, Status

### View All Trained Samples
- One-click access to all previously taken photo samples
- Helps verify if training data is stored properly

### Chatbot
- Get answers to common project-related questions:
  - What is face recognition?
  - How does blink detection work?
  - What is Dlib?

### Support
- Visit the Support tab for:
  - Help articles
  - Developer contact via Gmail integration
  - Links to Facebook and YouTube for video tutorials

### Exit Module
- Safely exit the app with confirmation prompt

## Tech Stack

| Component          | Technology                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| Frontend          | Python (Tkinter GUI)                                                       |
| Backend           | Python                                                                     |
| Database          | MySQL                                                                      |
| Face Recognition  | OpenCV, Dlib (dlib_face_recognition_resnet_model_v1.dat, shape_predictor_68_face_landmarks.dat) |
| Liveness Detection| Eye-blink detection via facial landmarks                                   |
| Webcam Integration| Real-time webcam using OpenCV                                              |


## Demo

Watch the full demo video here:  
https://drive.google.com/drive/u/3/folders/1EQ2hVCmWSwF8RAZXDq936VkX8est6bty

## Project Structure

```
├── main.py
├── login.py, register.py, student.py
├── face_recognition.py, train.py, attendance.py
├── chatbot.py, soupport.py
├── Face_Recog_Images/        # Image assets and face samples
├── attendancesheet.csv       # Attendance data
├── *.dat, *.pkl, *.xml       # Model and classifier artifacts
├── requirements.txt
└── README.md
```

This archive includes image assets that may contain identifiable faces, an
attendance CSV, and trained model artifacts. Review consent, access, and
distribution requirements before publishing or sharing the repository.

## Support

If you encounter any issues:

- Visit the Support tab
- Email the developer directly via the built-in Gmail module


## Acknowledgements

- OpenCV (https://opencv.org/)
- dlib (http://dlib.net/)
- Python (https://www.python.org/)
- Jessore University of Science and Technology

**Note**: This system is designed to detect live faces only.  
Fake attempts using photos, videos, or devices are rejected immediately with an "Unknown Face" warning.

**System Accuracy:**  
Achieves ~97% face recognition accuracy with real-time liveness detection.

import cv2
import os
import pickle
import numpy as np
import pandas as pd

os.makedirs("data", exist_ok=True)

# -----------------------------
# Employee Registration
# -----------------------------
emp_id = input("Enter Employee ID: ").strip().upper()
name = input("Enter Employee Name: ").strip().lower()
department = input("Enter Department: ").strip()
email = input("Enter Email ID: ").strip().lower()
shift_time = input("Enter Shift Start Time (HH:MM 24hr format): ").strip()

# Basic email validation
if "@" not in email or "." not in email:
    print("❌ Invalid email format.")
    exit()

employees_file = "data/employees.csv"

new_employee = pd.DataFrame(
    [[emp_id, name, department, email, shift_time]],
    columns=["EmpID", "Name", "Department", "Email", "ShiftStart"]
)

if not os.path.exists(employees_file):
    new_employee.to_csv(employees_file, index=False)
else:
    existing = pd.read_csv(employees_file)
    if emp_id not in existing["EmpID"].values:
        new_employee.to_csv(employees_file, mode='a', header=False, index=False)
    else:
        print("⚠ Employee already registered.")

# -----------------------------
# Face Capture
# -----------------------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

video = cv2.VideoCapture(0)
faces_data = []

print("Collecting face samples... Press ESC to stop.")

while True:
    ret, frame = video.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop = gray[y:y+h, x:x+w]
        resized = cv2.resize(crop, (100, 100))
        faces_data.append(resized)

        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow("Employee Face Capture", frame)

    if cv2.waitKey(1) == 27 or len(faces_data) >= 100:
        break

video.release()
cv2.destroyAllWindows()

faces_data = np.array(faces_data)
faces_data = faces_data.reshape(len(faces_data), -1)

name_file = "data/names.pkl"
face_file = "data/faces.pkl"

if os.path.exists(name_file):
    names = pickle.load(open(name_file, "rb"))
    faces = pickle.load(open(face_file, "rb"))
else:
    names = np.array([])
    faces = np.empty((0, faces_data.shape[1]))

names = np.append(names, [emp_id]*len(faces_data))
faces = np.append(faces, faces_data, axis=0)

pickle.dump(names, open(name_file, "wb"))
pickle.dump(faces, open(face_file, "wb"))

print("✅ Employee Registered Successfully!")
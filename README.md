# Smart Employee Attendance System using Computer Vision

## 📌 Overview
This project is an AI-based attendance system that uses face recognition to automate employee attendance tracking. It improves accuracy and eliminates manual attendance processes using computer vision and machine learning.

---

## 🚀 Features
- Face detection using OpenCV  
- Face recognition using K-Nearest Neighbors (KNN)  
- Employee registration with face data collection  
- Model training for face identification  
- Email alerts for late attendance  
- Modular system design  

---

## 🛠️ Tech Stack
- Python  
- OpenCV  
- NumPy  
- Pandas  
- Scikit-learn  

---

## 📂 Project Structure
```
smart-attendance-system/
│── data_collection.py  
│── train_model.py  
│── email_alert.py  
│── emotion_detector.py  
│── requirements.txt  
│── README.md  
```

---

## ⚙️ Installation

1. Clone the repository:
```
git clone https://github.com/your-username/smart-attendance-system.git
cd smart-attendance-system
```

2. Install dependencies:
```
pip install -r requirements.txt
```

---

## ▶️ Usage

### Step 1: Register Employee & Collect Face Data
```
python data_collection.py
```

### Step 2: Train Model
```
python train_model.py
```

---

## 📧 Email Alert System
- Sends automatic email notifications when an employee is marked late  
- Uses SMTP (Gmail) for sending alerts  

⚠️ Note: Store email credentials securely using environment variables instead of hardcoding.

---

## 🧠 How It Works
1. Capture employee face data using webcam  
2. Store face data and labels  
3. Train a KNN model on collected data  
4. Identify employees based on trained model  
5. Send email alerts when required  

---

## 📈 Future Improvements
- Add real-time attendance system (live face recognition)  
- Replace KNN with deep learning models (FaceNet, DeepFace)  
- Add real emotion detection using CNN  
- Build dashboard for attendance tracking  
- Integrate database (MySQL / Firebase)  

---

## 📌 Conclusion
This project demonstrates how computer vision and machine learning can automate attendance tracking and improve efficiency.

---


import smtplib
import pandas as pd
import os
from email.mime.text import MIMEText

# -----------------------------
# EMAIL CONFIGURATION
# -----------------------------
SENDER_EMAIL = "yamuna.hr26@gmail.com"
EMAIL_PASSWORD = "iajlmvoeazizscca"  # 16-character Gmail App Password

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


# -----------------------------
# Get Email from employees.csv
# -----------------------------
def get_email(employee_id):
    try:
        df = pd.read_csv("data/employees.csv")

        # Clean column names
        df.columns = df.columns.str.strip()

        # Ensure EmpID format matches
        df["EmpID"] = df["EmpID"].astype(str).str.strip().str.upper()
        employee_id = str(employee_id).strip().upper()

        row = df[df["EmpID"] == employee_id]

        if not row.empty:
            return row.iloc[0]["Email"]
        else:
            return None

    except Exception as e:
        print("CSV Error:", e)
        return None


# -----------------------------
# Send Late Alert Email
# -----------------------------
def send_email(employee_id, name, time, emotion, confidence):
    if not SENDER_EMAIL or not EMAIL_PASSWORD:
        print("❌ Email credentials not set.")
        return

    receiver = get_email(employee_id)

    if receiver is None:
        print(f"❌ Email not found for Employee ID: {employee_id}")
        return

    subject = "Late Attendance Alert - Company HR"

    body = f"""
Hello {name},

You were marked LATE today.

Employee ID: {employee_id}
Time: {time}
Emotion: {emotion}
Recognition Confidence: {confidence:.2f}%

Please ensure punctuality.

Regards,
HR Department
Smart Employee Attendance System
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"✅ Email sent to {receiver}")

    except Exception as e:
        print("❌ Email Error:", e)
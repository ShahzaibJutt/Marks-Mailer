import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from io import StringIO

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

# URL of the publicly accessible Google Sheets document
google_sheets_url = os.getenv('GOOGLE_SHEETS_URL')

# Download the Google Sheets document as CSV
response = requests.get(google_sheets_url)
csv_data = response.content.decode('utf-8')

# Create a DataFrame from the CSV data
df = pd.read_csv(StringIO(csv_data))

# SMTP server configuration
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = os.getenv('SMTP_PORT')
smtp_username = os.getenv('SMTP_USERNAME')
smtp_password = os.getenv('SMTP_PASSWORD')

# Email subject
subject = 'OOP - Gradebook So Far'

# Iterate through the DataFrame and send emails
for index, row in df.iterrows():
    roll_no = row['Roll No']
    student_name = row['Student Name']
    lab1_mark = row['LAB1']
    quiz1_mark = row['QUIZ1']
    # Email body
    body = f"""
Dear {student_name} {[roll_no]},

Your sessional scores in IT-260 Object Oriented Programming so far are as follows:

LAB1 (out of 10): {lab1_mark}
QUIZ1 (out of 5): {quiz1_mark}

If you have any questions or need further clarification on your marks, please feel free to reach out.

Best regards,
Muhammad Shahzaib
Teaching Assistant, OOP
Univeristy Of The Punjab
    """

    email = row['Roll No'].lower() + '@ibitpu.edu.pk'

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the Gmail SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, email, msg.as_string())
        server.quit()
        print(f"Email sent to {email}")
    except Exception as e:
        print(f"Failed to send email to {email}: {str(e)}")

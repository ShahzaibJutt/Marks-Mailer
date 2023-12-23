# Marks Mailer
This Python script automates the process of sending sessional score emails to students enrolled in the Object Oriented Programming (OOP) course. It reads student information and scores from a Google Sheets document, transforms the data into an email format, and sends personalized emails to each student.

## Setup

#### 1. Install Required Packages

Make sure to install the required Python packages by running:

```bash
pip -r requirements.txt
```

#### 2. Google Sheets Document
The script fetches student data from a Google Sheets document. Ensure that the document is publicly accessible. You can find the general URL format for a Google Sheets document here.
`https://docs.google.com/spreadsheets/d/your_spreadsheet_id/gviz/tq?tqx=out:csv&sheet=name_of_your_sheet`

#### 3. .env File
```bash
GOOGLE_SHEETS_URL=https://docs.google.com/spreadsheets/d/your_spreadsheet_id/gviz/tq?tqx=out:csv&sheet=name_of_your_sheet
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_gmail_app_password
```
You can create app passwords using the instructions given below. https://support.google.com/mail/answer/185833?hl=en

## Usage
Run the script using:
```bash
python main.py
```